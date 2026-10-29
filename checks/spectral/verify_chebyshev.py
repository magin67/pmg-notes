"""Exact orbit, polyform and duality checks for the fourth spectral note.

Requires SymPy. Matrix recurrence and folded-graph construction are independent.
No files are written. Run without -O because checks use assert.
"""
from fractions import Fraction as F
from math import gcd, factorial
from collections import Counter
import json
import sympy as sp
from verify_diagonal import (add, multiply, scale, form_matrix, square, vector,
                            wedge, tensor, act, grades, exponential_from_factors)


def mmul(a, b):
    return [[sum(x*y for x, y in zip(row, column)) for column in zip(*b)] for row in a]


def combine(a, b, x=1, y=1):
    return [[x*u+y*v for u, v in zip(row, other)] for row, other in zip(a, b)]


def path_matrix(n):
    out = [[0]*n for _ in range(n)]
    for i in range(n-1):
        out[i][i] += 1
        out[i+1][i+1] += 1
        out[i][i+1] = out[i+1][i] = -1
    return out


def orbit(base, last):
    n = len(base)
    result = [[[0]*n for _ in range(n)]]
    if last == 0:
        return result
    result.append(base)
    two_minus = [[2*(i == j)-base[i][j] for j in range(n)] for i in range(n)]
    for m in range(1, last):
        result.append(combine(combine(base, mmul(two_minus, result[m]), 2, 1), result[m-1], 1, -1))
    return result


def fold(n, m):
    def representative(j):
        j %= 2*n
        return min(j, 2*n-1-j)
    out = [[0]*n for _ in range(n)]
    for i in range(n):
        out[i][i] = 2
        out[i][representative(i+m)] -= 1
        out[i][representative(i-m)] -= 1
    return out


def edges(matrix):
    return [(i+1, j+1, -matrix[i][j]) for i in range(len(matrix))
            for j in range(i+1, len(matrix)) if matrix[i][j]]


def components(matrix):
    n = len(matrix)
    remaining, result = set(range(n)), []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        part, stack = [start], [start]
        while stack:
            i = stack.pop()
            new = [j for j in remaining if matrix[i][j] < 0]
            for j in new:
                remaining.remove(j)
                part.append(j)
                stack.append(j)
        result.append(sorted(part))
    return result


def exact_family():
    count = 0
    for n in range(2, 19):
        matrices = orbit(path_matrix(n), 2*n+1)
        for m, matrix in enumerate(matrices):
            assert matrix == fold(n, m)
            assert all(sum(row) == 0 for row in matrix)
            assert all(matrix[i][j] == matrix[j][i] <= 0 for i in range(n) for j in range(i+1, n))
            parts = components(matrix)
            assert len(parts) == sum((m*k) % (2*n) == 0 for k in range(n))
            count += 1
            if 1 <= m < n:
                assert all(weight == 1 for _, _, weight in edges(matrix))
                shapes = []
                for part in parts:
                    degrees = [matrix[i][i] for i in part]
                    if all(degree == 2 for degree in degrees):
                        shapes.append(("C", len(part)))
                    else:
                        assert degrees.count(1) == 2 and all(degree in (1, 2) for degree in degrees)
                        shapes.append(("P", len(part)))
                if m % 2:
                    q = gcd(m, n)
                    expected = [("P", n//q)]+[("C", 2*n//q)]*((q-1)//2)
                else:
                    q = gcd(m//2, n)
                    expected = [("C", n//q)]*q
                assert Counter(shapes) == Counter(expected)
            if m == n:
                assert edges(matrix) == [(i+1, n-i, 2) for i in range(n//2)]
        assert matrices[2*n] == matrices[0] and matrices[2*n+1] == matrices[1]
        assert all(matrices[2*n-m] == matrices[m] for m in range(n+1))
    return count


def exp_grades(form, dimension):
    result, current = [], {(0, 0): F(1)}
    for g in range(dimension+1):
        result.append(scale(current, F(1, factorial(g))))
        current = multiply(current, form)
    return result


def exact_projector(matrix, value, values):
    out = sp.eye(matrix.rows)
    for other in values:
        if other != value:
            out = (out*(matrix-other*sp.eye(matrix.rows))/(value-other)).applyfunc(sp.simplify)
    return out


def check():
    family_count = exact_family()
    matrices = orbit(path_matrix(6), 72)
    for q in range(7):
        transformed = orbit(matrices[q], 6)
        for p in range(7):
            assert transformed[p] == matrices[p*q]
    expected_edges = sorted([(1, 2, 1), (2, 4, 1), (4, 6, 1), (5, 6, 1), (3, 5, 1), (1, 3, 1)])
    assert edges(matrices[2]) == expected_edges
    order = [0, 1, 3, 5, 4, 2]
    cycle = [[matrices[2][i][j] for j in order] for i in order]
    assert cycle == [[2*(i == j)-int((i-j) % 6 in (1, 5)) for j in range(6)] for i in range(6)]

    L, identity, constant = sp.Matrix(matrices[2]), sp.eye(6), sp.ones(6)/6
    Gr = (L+constant).inv()-constant
    assert L*Gr == Gr*L == identity-constant
    assert L[:5, :5].det() == 6
    projectors = [exact_projector(L, value, [0, 1, 3, 4]) for value in [1, 3, 4]]
    assert sum(projectors, sp.zeros(6)) == identity-constant
    assert sum((E/value for E, value in zip(projectors, [1, 3, 4])), sp.zeros(6)) == Gr
    assert [sp.trace(E) for E in projectors] == [2, 2, 1]

    # Exact path projectors check the pairing of the original modes.
    original = sp.Matrix(matrices[1])
    spectrum = [0, 2-sp.sqrt(3), 1, 2, 3, 2+sp.sqrt(3)]
    Eold = [exact_projector(original, value, spectrum) for value in spectrum[1:]]
    assert (Eold[0]+Eold[4]-projectors[0]).applyfunc(sp.simplify) == sp.zeros(6)
    assert Eold[1]+Eold[3] == projectors[1] and Eold[2] == projectors[2]
    values = [1, 3, 4, 3, 1]
    contributions = [sp.simplify((E[0, 0]+E[5, 5]-2*E[0, 5])/value) for E, value in zip(Eold, values)]
    expected = [(2+sp.sqrt(3))/3, 0, sp.Rational(1, 6), 0, (2-sp.sqrt(3))/3]
    assert all(sp.simplify(x-y) == 0 for x, y in zip(contributions, expected))
    assert Gr[0, 0]+Gr[5, 5]-2*Gr[0, 5] == sp.Rational(3, 2)

    # Three independent full-polyform constructions: edges, matrix and blocks.
    edge_factors = []
    for i, j, weight in edges(matrices[2]):
        q = [0]*6
        q[i-1], q[j-1] = -1, 1
        edge_factors.append(scale(square(q), F(weight)))
    M = grades(exponential_from_factors(edge_factors), 5)
    assert M == exp_grades(form_matrix(L.tolist()), 5)
    grouped, green_grouped = {(0, 0): F(1)}, {(0, 0): F(1)}
    for E, value, rank in zip(projectors, [1, 3, 4], [2, 2, 1]):
        S = form_matrix(E.tolist())
        block, green_block = {}, {}
        for g, term in enumerate(exp_grades(S, rank)):
            block = add(block, scale(term, F(value)**g))
            green_block = add(green_block, scale(term, F(1, value)**g))
        grouped = multiply(grouped, block)
        green_grouped = multiply(green_grouped, green_block)
    assert grades(grouped, 5) == M
    N = exp_grades(form_matrix(Gr.tolist()), 5)
    assert grades(green_grouped, 5) == N
    p = [sum(v for (i, j), v in grade.items() if i == j) for grade in M]
    q = [sum(v for (i, j), v in grade.items() if i == j) for grade in N]
    assert p == [1, 12, 54, 112, 105, 36]
    assert q == [v/F(36) for v in reversed(p)]

    boundary = {0: F(1)}
    for i in range(5):
        v = [0]*6
        v[i], v[5] = 1, -1
        boundary = wedge(boundary, vector(v))
    T = tensor(boundary, boundary)
    assert M[5] == scale(T, F(6)) and N[5] == scale(T, F(1, 216))
    reduced = L[:5, :5]
    Mr = exp_grades(form_matrix(reduced.tolist()), 5)
    Q = exp_grades(form_matrix(reduced.inv().tolist()), 5)
    for g in range(6):
        assert act(Mr[5], Q[g]) == Mr[5-g]
        assert act(Q[5], Mr[g]) == Q[5-g]

    disconnected = sp.Matrix(matrices[3])
    assert disconnected.rank() == 4
    assert disconnected.eigenvals() == {sp.Integer(0): 2, sp.Integer(2): 3, sp.Integer(4): 1}
    assert exp_grades(form_matrix(disconnected.tolist()), 5)[5] == {}
    return {"family": {"path_sizes": "2..18", "exact_matrices": family_count,
                       "step_range": "0..2n+1", "composition_pairs_P6": 49},
            "P6": [{"m": m, "edges": edges(matrices[m]),
                    "components": [[i+1 for i in part] for part in components(matrices[m])],
                    "nullity": len(components(matrices[m]))} for m in range(7)],
            "P6_to_C6": {"rooted": list(map(str, p)), "green_coefficients": list(map(str, q)),
                         "R16_mode_contributions": list(map(str, contributions)),
                         "R16": "3/2", "tree_coefficient": 6,
                         "direct_top": "6 T6", "green_top": "T6/216",
                         "dual_grade_checks": 12}}


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
