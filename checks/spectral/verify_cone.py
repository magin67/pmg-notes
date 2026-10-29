"""Exact rational checks for the fixed P3 eigenbasis cone; standard library only.

The spectral and edge constructions, matrix inversion, forest enumeration and
dual contractions are independent. Assertions must be enabled.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod
import json
from verify_diagonal import (add, scale, square, vector, wedge, tensor,
    multiply, form_matrix, grades, exponential_from_factors, evaluate,
    matmul, determinant, inverse, laplacian, forest_partition, act)

MODES = [(1, 0, -1), (1, -2, 1)]
LENGTHS = [2, 6]
E = [[[F(x*y, s) for y in q] for x in q] for q, s in zip(MODES, LENGTHS)]
IDENTITY = [[F(i == j) for j in range(3)] for i in range(3)]
CENTERED = [[IDENTITY[i][j]-F(1, 3) for j in range(3)] for i in range(3)]


def spectral(a, b):
    return [[a*E[0][i][j]+b*E[1][i][j] for j in range(3)] for i in range(3)]


def weights(a, b):
    return [(0, 1, b/3), (1, 2, b/3), (0, 2, (3*a-b)/6)]


def matvec(matrix, q):
    return [sum(x*y for x, y in zip(row, q)) for row in matrix]


def in_cone(a, b):
    return a >= 0 and 0 <= b <= 3*a


def check_polyforms(a, b):
    a, b = F(a), F(b)
    L = spectral(a, b)
    edges = weights(a, b)
    A = [form_matrix(projector) for projector in E]
    factors = [scale(A[0], a), scale(A[1], b)]
    edge_factors = []
    for i, j, w in edges:
        q = [0]*3
        q[i], q[j] = -1, 1
        edge_factors.append(scale(square(q), w))
    M = grades(exponential_from_factors(factors), 2)
    assert M == grades(exponential_from_factors(edge_factors), 2)
    boundary = wedge(vector((1, 0, -1)), vector((0, 1, -1)))
    T = tensor(boundary, boundary)
    assert multiply(*A) == scale(T, F(1, 3))
    assert M[2] == scale(T, a*b/3)
    assert all(multiply(v, v) == {} for v in A)
    p = [evaluate(g, IDENTITY) for g in M]
    assert p == [1, a+b, a*b]
    ordinary, rooted = [F(0)]*3, [F(0)]*3
    for g in range(4):
        for subset in combinations(edges, g):
            components = forest_partition(3, subset)
            if components is not None:
                w = prod(c for _, _, c in subset)
                ordinary[g] += w
                rooted[g] += w*prod(map(len, components))
    assert ordinary == [1, (a+b)/2, a*b/3] and rooted == p
    tau = determinant([row[:2] for row in L[:2]])
    assert tau == a*b/3
    if not a*b:
        assert M[2] == {}
        return
    Gr = spectral(1/a, 1/b)
    inv = inverse([[v+F(1, 3) for v in row] for row in L])
    assert Gr == [[v-F(1, 3) for v in row] for row in inv]
    assert matmul(L, Gr) == matmul(Gr, L) == CENTERED
    N = grades(exponential_from_factors([scale(A[0], 1/a), scale(A[1], 1/b)]), 2)
    assert N[2] == scale(T, 1/(3*a*b))
    assert [evaluate(g, IDENTITY) for g in N] == [v/(a*b) for v in reversed(p)]
    assert [evaluate(g, Gr) for g in M] == [1, 2, 1]
    assert [evaluate(g, L) for g in N] == [1, 2, 1]
    basis = [(1, 0, -1), (0, 1, -1)]
    dual_q = [[sum(x*y for x, y in zip(q, v)) for v in basis] for q in MODES]
    Mr = grades(exponential_from_factors([
        scale(square(q[:2]), c/s) for q, c, s in zip(MODES, (a, b), LENGTHS)]), 2)
    Q = grades(exponential_from_factors([
        scale(square(q), 1/(c*s)) for q, c, s in zip(dual_q, (a, b), LENGTHS)]), 2)
    assert Q[1] == form_matrix(inverse([row[:2] for row in L[:2]]))
    for g in range(3):
        assert act(Mr[2], Q[g]) == Mr[2-g]
        assert act(Q[2], Mr[g]) == Q[2-g]
    centered_factors = []
    for q, c, s in zip(dual_q, (a, b), LENGTHS):
        cq = [sum(q[i]*CENTERED[i][j] for i in range(2)) for j in range(3)]
        centered_factors.append(scale(square(cq), 1/(c*s)))
    assert grades(exponential_from_factors(centered_factors), 2) == N
    R = [[Gr[i][i]+Gr[j][j]-2*Gr[i][j] for j in range(3)] for i in range(3)]
    assert R[0][2] == 2/a
    assert R[0][1] == R[1][2] == 1/(2*a)+3/(2*b)
    Kf = sum(R[i][j] for i, j in combinations(range(3), 2))
    assert Kf == 3*sum(Gr[i][i] for i in range(3)) == 3*(1/a+1/b)


def check():
    # Checking both coefficient matrices proves the affine matrix identity.
    for a, b in [(F(1), F(0)), (F(0), F(1))]:
        assert spectral(a, b) == laplacian(3, weights(a, b))
    count = reciprocal = 0
    for a, b in product([F(i, 2) for i in range(-4, 13)],
                        [F(i, 2) for i in range(-4, 37)]):
        L = spectral(a, b)
        assert L == laplacian(3, weights(a, b))
        assert all(sum(row) == 0 for row in L)
        assert in_cone(a, b) == all(w >= 0 for _, _, w in weights(a, b))
        assert (0 < b < 3*a) == all(w > 0 for _, _, w in weights(a, b))
        for q, c in zip(MODES, (a, b)):
            assert matvec(L, q) == [c*x for x in q]
        assert (a, b) == (b/3+2*(3*a-b)/6, b)
        if a > 0 and b > 0:
            alpha, beta = 1/a, 1/b
            assert in_cone(a, b) == (beta >= alpha/3)
            if in_cone(a, b):
                assert in_cone(alpha, beta) == (a/3 <= b <= 3*a)
            reciprocal += 1
        if in_cone(a, b):
            # Forward shift into the entrywise nonnegative spectracone.
            s = max(L[i][i] for i in range(3))
            A = [[s*IDENTITY[i][j]-L[i][j] for j in range(3)] for i in range(3)]
            assert all(v >= 0 for row in A for v in row)
            assert matvec(A, [1, 1, 1]) == [s]*3
            for q, c in zip(MODES, (a, b)):
                assert matvec(A, q) == [(s-c)*x for x in q]
        count += 1
    perron_count = 0
    for eta in product(range(-2, 5), repeat=3):
        A = spectral(F(eta[1]), F(eta[2]))
        A = [[v+F(eta[0], 3) for v in row] for row in A]
        if all(v >= 0 for row in A for v in row):
            a, b = F(eta[0]-eta[1]), F(eta[0]-eta[2])
            assert in_cone(a, b)
            assert spectral(a, b) == [[eta[0]*IDENTITY[i][j]-A[i][j] for j in range(3)] for i in range(3)]
            perron_count += 1
    simple_points = []
    for ws in product((0, 1), repeat=3):
        L = laplacian(3, [(i, j, F(w)) for (i, j), w in zip([(0, 1), (1, 2), (0, 2)], ws)])
        mu = [sum(x*y for x, y in zip(q, matvec(L, q)))/F(s) for q, s in zip(MODES, LENGTHS)]
        if L == spectral(*mu):
            simple_points.append(tuple(mu))
    assert set(simple_points) == {(0, 0), (2, 0), (1, 3), (3, 3)}
    cases = [(1, 3), (3, 3), (4, 1), (3, 1), (2, 2), (1, F(1, 2)), (2, 0), (0, 0)]
    for a, b in cases:
        check_polyforms(a, b)
    Gr = spectral(F(1, 4), F(1))
    assert Gr == [[F(v, 24) for v in row] for row in [(7, -8, 1), (-8, 16, -8), (1, -8, 7)]]
    assert Gr[0][2] > 0
    # A repeated eigenspace allows commuting matrices with mixed fixed modes.
    K = spectral(F(3), F(3))
    edge12 = laplacian(3, [(0, 1, F(1))])
    assert matmul(K, edge12) == matmul(edge12, K)
    assert sum(x*y for x, y in zip(MODES[0], matvec(edge12, MODES[1]))) == 3
    # Phi_0=0, Phi_1=x and Phi_(m+1)=(2-x)Phi_m-Phi_(m-1)+2x.
    orbit = [(0, 0), (1, 3)]
    for m in range(1, 6):
        orbit.append(tuple((2-c)*orbit[m][k]-orbit[m-1][k]+2*c for k, c in enumerate((1, 3))))
    assert orbit == [(0, 0), (1, 3), (3, 3), (4, 0), (3, 3), (1, 3), (0, 0)]
    return dict(rational_matrix_cases=count, reciprocal_cases=reciprocal,
                nonnegative_perron_examples=perron_count, polyform_cases=len(cases),
                simple_points=[[int(a), int(b)] for a, b in simple_points],
                example_green=[[str(v) for v in row] for row in Gr],
                checked="edge matrices; cone; shifts; simple graphs; all grades; duality; forests; metrics; resistances; orbit")


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
