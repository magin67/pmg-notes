"""Exact independent checks for 'One changing edge'; standard library only.

Run from the repository root: python checks/variations/verify_single_edge.py
Exterior forms are represented by their coefficient matrices in each exterior
power of the affine basis (a_1-a_n, ..., a_{n-1}-a_n). This compares actual
forms, including their linear dependencies, rather than formal edge labels.
"""

from fractions import Fraction as Q
from itertools import combinations
from math import prod
import json


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j + 1, len(a)):
            multiplier = a[i][j] / value
            for k in range(j + 1, len(a)):
                a[i][k] -= multiplier * a[j][k]
    return result


def inverse(matrix):
    n = len(matrix)
    a = [list(map(Q, row)) + [Q(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def vector(n, edge):
    i, j = edge
    return [Q(k == j) - Q(k == i) for k in range(n - 1)]


def reduced_laplacian(n, weights):
    d = n - 1
    result = [[Q(0) for _ in range(d)] for _ in range(d)]
    for edge, c in weights.items():
        v = vector(n, edge)
        for i in range(d):
            for j in range(d):
                result[i][j] += c * v[i] * v[j]
    return result


def pairing(a, matrix, b):
    return sum(a[i] * matrix[i][j] * b[j]
               for i in range(len(a)) for j in range(len(b)))


def forest_sums(n, weights):
    """Enumerate trees and separating 2-forests, independently of matrices."""
    edges = [e for e, c in weights.items() if c]
    tau = Q(0)
    pairs = list(combinations(range(n), 2))
    forests = {p: Q(0) for p in pairs}
    for size in (n - 2, n - 1):
        for chosen in combinations(edges, size):
            parent = list(range(n))

            def root(i):
                while parent[i] != i:
                    i = parent[i]
                return i

            for i, j in chosen:
                a, b = root(i), root(j)
                if a == b:
                    break
                parent[a] = b
            else:
                weight = prod((weights[e] for e in chosen), start=Q(1))
                if size == n - 1:
                    tau += weight
                else:
                    for p in pairs:
                        if root(p[0]) != root(p[1]):
                            forests[p] += weight
    return tau, forests


def exterior_grade(n, weights, grade, extra=()):
    """Expand a grade of M times fixed vector forms using exterior minors."""
    d = n - 1
    rows = list(combinations(range(d), grade))
    result = [[Q(0) for _ in rows] for _ in rows]
    count = grade - len(extra)
    if count < 0:
        return result
    edges = [e for e, c in weights.items() if c]
    for chosen in combinations(edges, count):
        columns = [vector(n, e) for e in chosen] + list(extra)
        wedge = [determinant([[v[i] for v in columns] for i in subset])
                 for subset in rows]
        weight = prod((weights[e] for e in chosen), start=Q(1))
        for i, x in enumerate(wedge):
            for j, y in enumerate(wedge):
                result[i][j] += weight * x * y
    return result


def verify_graph(name, n, weights):
    pairs = list(combinations(range(n), 2))
    vectors = {p: vector(n, p) for p in pairs}
    tau, forests = forest_sums(n, weights)
    lap = reduced_laplacian(n, weights)
    green = inverse(lap)
    assert determinant(lap) == tau > 0
    grades = [exterior_grade(n, weights, k) for k in range(n)]
    assert grades[-1] == [[tau]]
    R = {p: pairing(vectors[p], green, vectors[p]) for p in pairs}
    for p in pairs:
        assert exterior_grade(n, weights, n - 1, (vectors[p],))[0][0] == forests[p]
        assert forests[p] == tau * R[p]

    cases = disconnected = 0
    for edge in pairs:
        c = weights.get(edge, Q(0))
        variations = [Q(1, 2)] + ([-c / 2, -c] if c else [])
        v = vectors[edge]
        for t in variations:
            changed = dict(weights)
            changed[edge] = c + t
            new_tau, new_forests = forest_sums(n, changed)
            denominator = 1 + t * R[edge]
            assert new_tau == tau * denominator
            new_lap = reduced_laplacian(n, changed)
            assert determinant(new_lap) == new_tau
            for k in range(n):
                direct = exterior_grade(n, changed, k)
                added = exterior_grade(n, weights, k, (v,))
                expected = [[x + t * y for x, y in zip(row, add)]
                            for row, add in zip(grades[k], added)]
                assert direct == expected, (name, edge, t, k)

            for p in pairs:
                g = pairing(vectors[p], green, v)
                mixed = exterior_grade(n, weights, n - 1, (vectors[p], v))
                gram = R[p] * R[edge] - g * g
                assert mixed[0][0] == tau * gram
                assert new_forests[p] == forests[p] + t * tau * gram

            if new_tau:
                new_green = inverse(new_lap)
                gv = [sum(row[j] * v[j] for j in range(n - 1)) for row in green]
                for i in range(n - 1):
                    for j in range(n - 1):
                        assert new_green[i][j] == green[i][j] - t * gv[i] * gv[j] / denominator
                for p in pairs:
                    actual = pairing(vectors[p], new_green, vectors[p])
                    g = pairing(vectors[p], green, v)
                    assert actual == R[p] - t * g * g / denominator
                    assert actual == new_forests[p] / new_tau
            else:
                # Never interpret a disconnected pseudoinverse as finite intercomponent resistance.
                assert denominator == 0
                disconnected += 1
            cases += 1
    return {'graph': name, 'finite_variations': cases, 'bridge_deletions': disconnected}


def main():
    examples = [
        ('weighted_edge', 2, {(0, 1): Q(3, 2)}),
        ('unit_triangle', 3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}),
        ('weighted_triangle', 3, {(0, 1): Q(2), (0, 2): Q(5), (1, 2): Q(3)}),
        ('unit_P4', 4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}),
        ('weighted_C4', 4, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)}),
    ]
    results = [verify_graph(*example) for example in examples]
    # Independently check the displayed triangle formulas at rational parameters.
    for t in (Q(-1), Q(-1, 2), Q(0), Q(1), Q(3, 2)):
        w = {(0, 1): 1 + t, (0, 2): Q(1), (1, 2): Q(1)}
        tau, m = forest_sums(3, w)
        assert tau == 3 + 2 * t
        assert m[(0, 1)] == 2
        assert m[(0, 2)] == m[(1, 2)] == 2 + t
        inv = inverse(reduced_laplacian(3, w))
        for p in m:
            assert pairing(vector(3, p), inv, vector(3, p)) == m[p] / tau
    print(json.dumps({'status': 'passed', 'graphs': results,
                      'total_variations': sum(r['finite_variations'] for r in results),
                      'triangle_parameters': 5}, indent=2))


if __name__ == '__main__':
    main()
