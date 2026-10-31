"""Exact independent checks for 'Two edges and joint variation'.

Run: python checks/variations/verify_joint_edges.py
Uses standard-library rational arithmetic and the independently implemented
forest enumeration and exterior coefficient matrices from the first note.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
import json

from verify_single_edge import (
    determinant, inverse, vector, reduced_laplacian, pairing,
    forest_sums, exterior_grade,
)


def subsets(size):
    return [s for k in range(size + 1) for s in combinations(range(size), k)]


def gram(vectors, metric):
    return [[pairing(u, metric, v) for v in vectors] for u in vectors]


def choices(c):
    return [Q(0), Q(1, 2)] + ([-c / 2, -c] if c else [])


def changed_weights(weights, edges, changes):
    result = dict(weights)
    for e, t in zip(edges, changes):
        result[e] = result.get(e, Q(0)) + t
        assert result[e] >= 0
    return result


def verify_two(name, n, weights):
    pairs = list(combinations(range(n), 2))
    vec = {p: vector(n, p) for p in pairs}
    tau, forests = forest_sums(n, weights)
    metric = inverse(reduced_laplacian(n, weights))
    R = {p: pairing(vec[p], metric, vec[p]) for p in pairs}
    grades = [exterior_grade(n, weights, k) for k in range(n)]
    cases = disconnected = sequential = skipped = 0
    for e, f in combinations(pairs, 2):
        u, v = vec[e], vec[f]
        ru, rv = R[e], R[f]
        g = pairing(u, metric, v)
        contributions = [
            [exterior_grade(n, weights, k, extra) for k in range(n)]
            for extra in ((u,), (v,), (u, v))
        ]
        for s, t in product(choices(weights.get(e, 0)), choices(weights.get(f, 0))):
            new = changed_weights(weights, (e, f), (s, t))
            new_tau, new_forests = forest_sums(n, new)
            new_lap = reduced_laplacian(n, new)
            phi = 1 + s * ru + t * rv + s * t * (ru * rv - g * g)
            assert new_tau == determinant(new_lap) == tau * phi
            for k in range(n):
                expected = [row[:] for row in grades[k]]
                for coefficient, contribution in zip((s, t, s * t), contributions):
                    for i in range(len(expected)):
                        for j in range(len(expected)):
                            expected[i][j] += coefficient * contribution[k][i][j]
                assert exterior_grade(n, new, k) == expected, (name, e, f, s, t, k)
            for p in pairs:
                x, y = pairing(vec[p], metric, u), pairing(vec[p], metric, v)
                correction = s*x*x + t*y*y + s*t*(rv*x*x + ru*y*y - 2*g*x*y)
                assert new_forests[p] == tau * (R[p] * phi - correction)
                assert determinant(gram((vec[p], u, v), metric)) == (
                    R[p]*(ru*rv-g*g) - rv*x*x - ru*y*y + 2*g*x*y)
            if new_tau:
                new_metric = inverse(new_lap)
                actual = {p: pairing(vec[p], new_metric, vec[p]) for p in pairs}
                for p in pairs:
                    x, y = pairing(vec[p], metric, u), pairing(vec[p], metric, v)
                    assert actual[p] == new_forests[p] / new_tau
                    assert actual[p] == R[p] - (
                        s*x*x + t*y*y + s*t*(rv*x*x + ru*y*y - 2*g*x*y)) / phi
                for first, second, a, b in ((e, f, s, t), (f, e, t, s)):
                    middle = changed_weights(weights, (first,), (a,))
                    mid_tau = determinant(reduced_laplacian(n, middle))
                    if not mid_tau:
                        skipped += 1
                        continue
                    mid_metric = inverse(reduced_laplacian(n, middle))
                    A = 1 + a * R[first]
                    r2 = R[second] - a*g*g/A
                    assert mid_tau == tau*A
                    assert r2 == pairing(vec[second], mid_metric, vec[second])
                    assert mid_tau*(1+b*r2) == new_tau
                    for p in pairs:
                        x = pairing(vec[p], metric, vec[first])
                        y = pairing(vec[p], metric, vec[second])
                        mid_r = R[p] - a*x*x/A
                        mid_y = y - a*x*g/A
                        assert mid_y == pairing(vec[p], mid_metric, vec[second])
                        assert actual[p] == mid_r - b*mid_y*mid_y/(1+b*r2)
                    sequential += 1
            else:
                assert phi == 0
                disconnected += 1
            cases += 1
    return dict(graph=name, two_edge_cases=cases, disconnected=disconnected,
                sequential_orders=sequential, disconnected_intermediates=skipped)


def verify_multiple(n, weights, edges, changes):
    tau, _ = forest_sums(n, weights)
    metric = inverse(reduced_laplacian(n, weights))
    vectors = [vector(n, e) for e in edges]
    G = gram(vectors, metric)
    size = len(edges)
    selected = subsets(size)
    terms = [(s, prod((changes[i] for i in s), start=Q(1))) for s in selected]
    H = [[Q(i == j) + changes[i]*G[i][j] for j in range(size)] for i in range(size)]
    phi = sum(t * determinant([[G[i][j] for j in s] for i in s]) for s, t in terms)
    assert phi == determinant(H)
    new = changed_weights(weights, edges, changes)
    new_tau, new_forests = forest_sums(n, new)
    new_lap = reduced_laplacian(n, new)
    assert new_tau == tau*phi == determinant(new_lap)
    for k in range(n):
        expected = [[Q(0) for _ in row] for row in exterior_grade(n, weights, k)]
        for s, t in terms:
            if not t:
                continue
            contribution = exterior_grade(n, weights, k, tuple(vectors[i] for i in s))
            for i in range(len(expected)):
                for j in range(len(expected)):
                    expected[i][j] += t*contribution[i][j]
        assert expected == exterior_grade(n, new, k)
    new_metric = inverse(new_lap) if phi else None
    Hinv = inverse(H) if phi else None
    for p in combinations(range(n), 2):
        w = vector(n, p)
        numerator = sum(t * determinant(gram([w] + [vectors[i] for i in s], metric))
                        for s, t in terms)
        assert tau*numerator == new_forests[p]
        if phi:
            z = [pairing(w, metric, v) for v in vectors]
            correction = sum(z[i]*Hinv[i][j]*changes[j]*z[j]
                             for i in range(size) for j in range(size))
            actual = pairing(w, new_metric, w)
            assert actual == numerator/phi == pairing(w, metric, w)-correction


def main():
    triangle = {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}
    path = {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}
    cycle = {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)}
    examples = [
        ('unit_triangle', 3, triangle),
        ('weighted_triangle', 3, {(0, 1): Q(2), (0, 2): Q(5), (1, 2): Q(3)}),
        ('unit_P4', 4, path),
        ('weighted_C4', 4, cycle),
    ]
    results = [verify_two(*example) for example in examples]
    parameters = (Q(-1), Q(-1, 2), Q(0), Q(1), Q(3, 2))
    for s, t in product(parameters, repeat=2):
        weights = changed_weights(triangle, ((0, 1), (0, 2)), (s, t))
        tau, forests = forest_sums(3, weights)
        assert tau == 3 + 2*s + 2*t + s*t
        assert forests == {(0, 1): 2+t, (0, 2): 2+s, (1, 2): 2+s+t}
        if tau:
            metric = inverse(reduced_laplacian(3, weights))
            for p in forests:
                assert pairing(vector(3, p), metric, vector(3, p)) == forests[p]/tau
    multiple = 0
    for _, n, weights in examples:
        edges = list(combinations(range(n), 2))
        changes_list = [
            [Q(1, 2) for _ in edges],
            [Q(0) if i % 2 else Q(1, 2) for i in range(len(edges))],
            [-weights.get(e, Q(0))/2 for e in edges],
            [-weights.get(e, Q(0)) for e in edges],
        ]
        for changes in changes_list:
            verify_multiple(n, weights, edges, changes)
            multiple += 1
    verify_multiple(2, {(0, 1): Q(3, 2)}, [(0, 1)], [Q(1, 2)])
    # Final connectivity does not guarantee connectivity in both orders.
    p3 = {(0, 1): Q(1), (1, 2): Q(1)}
    assert determinant(reduced_laplacian(3, changed_weights(p3, [(0, 1)], [-1]))) == 0
    assert determinant(reduced_laplacian(3, changed_weights(p3, [(0, 2)], [1]))) > 0
    verify_multiple(3, p3, [(0, 1), (0, 2)], [Q(-1), Q(1)])
    print(json.dumps(dict(status='passed', graphs=results,
                          total_two_edge_cases=sum(r['two_edge_cases'] for r in results),
                          triangle_parameter_pairs=25, multiple_cases=multiple+2), indent=2))


if __name__ == '__main__':
    main()
