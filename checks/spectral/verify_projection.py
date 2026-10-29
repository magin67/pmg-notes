"""Exact fixed-basis projection checks; standard library and existing algebra.

All matrix entries and tensor coefficients are rational. Normalized modes are
handled by dividing rank-one tensors by integer squared lengths.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod, isqrt
import json
from verify_diagonal import (add, scale, square, vector, wedge, tensor,
    multiply, form_matrix, grades, exponential_from_factors, evaluate,
    matmul, determinant, inverse, laplacian, forest_partition, act)

Q = [(2, 1, -2, -1), (-1, 2, 1, -2), (1, -1, 1, -1)]
LENGTHS = [10, 10, 4]
E = [[[F(x*y, s) for y in q] for x in q] for q, s in zip(Q, LENGTHS)]
I4 = [[F(i == j) for j in range(4)] for i in range(4)]
J = [[I4[i][j]-F(1, 4) for j in range(4)] for i in range(4)]
PAIRS = list(combinations(range(4), 2))
MU = [F(10), F(4), F(4)]
MU_STAR = [F(554, 57), F(244, 57), F(248, 57)]


def matrix_add(A, B, factor=F(1)):
    return [[x+factor*y for x, y in zip(a, b)] for a, b in zip(A, B)]


def spectral(mu):
    return [[sum(c*e[i][j] for c, e in zip(mu, E)) for j in range(4)] for i in range(4)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def norm2(A):
    return sum(v*v for row in A for v in row)


def coefficients(A):
    return [trace(matmul(A, e)) for e in E]


def projection(A):
    return spectral(coefficients(A))


def family_edges(r):
    r = F(r)
    return [(0, 1, -(2+3*r)/10), (2, 3, -(2+3*r)/10),
            (0, 3, (22+3*r)/10), (1, 2, (22+3*r)/10),
            (0, 2, (17-2*r)/5), (1, 3, (8+2*r)/5)]


def family_matrix(r):
    mixed = [[F(r*(Q[0][i]*Q[1][j]+Q[1][i]*Q[0][j]), 10)
              for j in range(4)] for i in range(4)]
    return matrix_add(spectral(MU), mixed)


def green(L):
    inv = inverse([[v+F(1, 4) for v in row] for row in L])
    return [[v-F(1, 4) for v in row] for row in inv]


def exp_grades(form, dimension=3):
    result = [{(0, 0): F(1)}]
    for g in range(1, dimension+1):
        result.append(scale(multiply(result[-1], form), F(1, g)))
    return result


def forest_coefficients(edges):
    ordinary, rooted = [F(0)]*4, [F(0)]*4
    for g in range(4):
        for subset in combinations(edges, g):
            components = forest_partition(4, subset)
            if components is not None:
                w = prod(c for _, _, c in subset)
                ordinary[g] += w
                rooted[g] += w*prod(map(len, components))
    return ordinary, rooted


def minors_coefficients(A):
    return [sum(determinant([[A[i][j] for j in ind] for i in ind])
                for ind in combinations(range(len(A)), g)) for g in range(4)]


def exterior(qs):
    result = {0: F(1)}
    for q in qs:
        result = wedge(result, vector(q))
    return result


def compound_form(S, g, diagonal=False, modes=Q):
    result = {}
    indices = list(combinations(range(3), g))
    for left, right in product(indices, repeat=2):
        if diagonal and left != right:
            continue
        coefficient = determinant([[S[i][j] for j in right] for i in left])
        if not coefficient:
            continue
        squared_denominator = prod(LENGTHS[i] for i in left+right)
        denominator = isqrt(squared_denominator)
        assert denominator**2 == squared_denominator
        term = tensor(exterior([modes[i] for i in left]), exterior([modes[i] for i in right]))
        result = add(result, scale(term, coefficient/denominator))
    return result


def resistances(Gr):
    return [Gr[i][i]+Gr[j][j]-2*Gr[i][j] for i, j in PAIRS]


def polyform_check(r):
    r = F(r)
    L = laplacian(4, family_edges(r))
    S = [[F(10), r, F(0)], [r, F(4), F(0)], [F(0), F(0), F(4)]]
    M = exp_grades(form_matrix(L))
    edge_factors = []
    for i, j, w in family_edges(r):
        q = [0]*4
        q[i], q[j] = -1, 1
        edge_factors.append(scale(square(q), w))
    assert M == grades(exponential_from_factors(edge_factors), 3)
    assert M == [compound_form(S, g) for g in range(4)]
    p = [evaluate(g, I4) for g in M]
    f, rooted = forest_coefficients(family_edges(r))
    assert p == rooted == minors_coefficients(L) == [1, 18, 96-r*r, 4*(40-r*r)]
    assert f == [1, 9, (1428-36*r-17*r*r)/50, 40-r*r]
    Gr = green(L)
    N = exp_grades(form_matrix(Gr))
    assert matmul(L, Gr) == matmul(Gr, L) == J
    assert N == [compound_form(inverse(S), g) for g in range(4)]
    assert [evaluate(g, I4) for g in N] == [v/p[3] for v in reversed(p)]
    assert [evaluate(g, Gr) for g in M] == [1, 3, 3, 1]
    assert [evaluate(g, L) for g in N] == [1, 3, 3, 1]
    reduced = [row[:3] for row in L[:3]]
    Mr = exp_grades(form_matrix(reduced))
    dual = exp_grades(form_matrix(inverse(reduced)))
    dual_modes = [[q[i]-q[3] for i in range(3)] for q in Q]
    assert dual == [compound_form(inverse(S), g, modes=dual_modes) for g in range(4)]
    for g in range(4):
        assert act(Mr[3], dual[g]) == Mr[3-g]
        assert act(dual[3], Mr[g]) == dual[3-g]
    # C maps reduced dual functionals to the first three centered vertices.
    moved = [[sum(q[i]*J[i][j] for i in range(3)) for j in range(4)] for q in dual_modes]
    assert moved == [list(q) for q in Q]
    assert N == [compound_form(inverse(S), g, modes=moved) for g in range(4)]
    boundary = exterior([(1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1)])
    T = tensor(boundary, boundary)
    tau = determinant(reduced)
    assert tau == 40-r*r
    assert M[3] == scale(T, tau) and N[3] == scale(T, 1/(16*tau))
    projected_grades = [compound_form(S, g, diagonal=True) for g in range(4)]
    assert [evaluate(g, I4) for g in projected_grades] == p
    hat = exp_grades(form_matrix(spectral(MU)))
    pair12 = scale(square_from_exterior(exterior(Q[:2])), F(1, 100))
    assert projected_grades[2] == add(hat[2], scale(pair12, -r*r))
    assert projected_grades[3] == M[3]
    assert coefficients(Gr) == [4/(40-r*r), 10/(40-r*r), F(1, 4)]
    R = resistances(Gr)
    Kf = sum(R)
    assert Kf == 4*trace(Gr) == 1+56/(40-r*r)
    assert R[1] == F(2, 5)*(26+4*r)/(40-r*r)
    assert R[4] == F(2, 5)*(44-4*r)/(40-r*r)
    return dict(r=str(r), ordinary=list(map(str, f)), rooted=list(map(str, p)),
                tau=str(tau), Kirchhoff=str(Kf), R=list(map(str, R)))


def square_from_exterior(x):
    return tensor(x, x)


def check():
    for i, q in enumerate(Q):
        assert sum(q) == 0 and sum(v*v for v in q) == LENGTHS[i]
        for j, other in enumerate(Q):
            assert sum(x*y for x, y in zip(q, other)) == (LENGTHS[i] if i == j else 0)
    cycle = laplacian(4, [(0, 1, F(1)), (1, 2, F(1)), (2, 3, F(1)), (0, 3, F(1))])
    assert cycle == spectral([2, 2, 4])
    for r in [F(0), F(1)]:
        assert family_matrix(r) == laplacian(4, family_edges(r))
    L = family_matrix(-4)
    source = matrix_add(cycle, laplacian(4, [(0, 2, F(5))]))
    assert L == source
    hat, star = spectral(MU), spectral(MU_STAR)
    assert coefficients(L) == MU and projection(L) == hat
    assert [-hat[i][j] for i, j in PAIRS] == [F(-1, 5), F(17, 5), F(11, 5), F(11, 5), F(8, 5), F(-1, 5)]
    assert [-star[i][j] for i, j in PAIRS] == [0, F(184, 57), F(124, 57), F(124, 57), F(91, 57), 0]
    normal = [4, -4, -5]
    assert sum(c*x for c, x in zip(normal, MU)) == 4
    assert sum(c*x for c, x in zip(normal, MU_STAR)) == 0
    assert MU_STAR == [x-F(4, 57)*c for x, c in zip(MU, normal)]
    # The halfspace projection is feasible for every other cone inequality.
    assert all(star[i][j] <= 0 for i, j in PAIRS)
    assert norm2(matrix_add(L, hat, -1)) == 32
    assert norm2(matrix_add(hat, star, -1)) == F(16, 57)
    assert norm2(matrix_add(L, star, -1)) == F(1840, 57)
    assert trace(L) == trace(hat) == 18 and trace(star) == F(1046, 57)
    # Projecting to the two-dimensional eigenspace of C4 preserves the input.
    block = matrix_add(E[0], E[1])
    block_projection = matrix_add(matmul(matmul(block, L), block), matmul(matmul(E[2], L), E[2]))
    assert block_projection == L and matmul(cycle, L) == matmul(L, cycle)
    assert minors_coefficients(L) == [1, 18, 80, 96]
    assert minors_coefficients(hat) == [1, 18, 96, 160]
    assert coefficients(green(L)) == [F(1, 6), F(5, 12), F(1, 4)]
    assert coefficients(green(hat)) == [F(1, 10), F(1, 4), F(1, 4)]
    # A rational family verifies the lost coordinate and graph inequalities.
    family_count = 0
    for k in range(21):
        r = -4+F(k, 6)
        A = family_matrix(r)
        assert all(w >= 0 for _, _, w in family_edges(r))
        assert determinant([row[:3] for row in A[:3]]) > 0
        assert projection(A) == hat
        assert norm2(matrix_add(A, hat, -1)) == 2*r*r
        family_count += 1
    cases = [polyform_check(r) for r in [-4, -3, -2, -1, F(-2, 3), 0]]
    # All 64 simple graphs test the general identities in the same basis.
    connected = 0
    for choices in product((0, 1), repeat=6):
        A = laplacian(4, [(i, j, F(w)) for (i, j), w in zip(PAIRS, choices)])
        diag = projection(A)
        assert projection(diag) == diag
        assert trace(A) == trace(diag)
        assert norm2(A) == norm2(diag)+norm2(matrix_add(A, diag, -1))
        p, phat = minors_coefficients(A), minors_coefficients(diag)
        assert all(a <= b for a, b in zip(p, phat))
        assert phat[2]-p[2] == norm2(matrix_add(A, diag, -1))/2
        if p[3]:
            connected += 1
            assert all(x > 0 for x in coefficients(A))
            nu, inv_mu = coefficients(green(A)), [1/x for x in coefficients(A)]
            assert all(a >= b for a, b in zip(nu, inv_mu))
    assert connected == 38
    # A disconnected edge can project to a connected weighted P3.
    path_modes = [(1, 0, -1), (1, -2, 1)]
    edge = laplacian(3, [(0, 1, F(1))])
    path_projectors = [[[F(x*y, s) for y in q] for x in q]
                       for q, s in zip(path_modes, (2, 6))]
    path_mu = [trace(matmul(edge, e)) for e in path_projectors]
    assert path_mu == [F(1, 2), F(3, 2)]
    path_hat = [[sum(c*e[i][j] for c, e in zip(path_mu, path_projectors))
                 for j in range(3)] for i in range(3)]
    assert path_hat == laplacian(3, [(0, 1, F(1, 2)), (1, 2, F(1, 2))])
    assert determinant([row[:2] for row in edge[:2]]) == 0
    assert determinant([row[:2] for row in path_hat[:2]]) == F(1, 4)
    return dict(simple_graphs=64, connected_graphs=connected, family_points=family_count,
                polyform_cases=cases, mu_star=list(map(str, MU_STAR)),
                squared_errors=["32", "16/57", "1840/57"],
                checked="orthogonal and block projections; exact cone optimum; all grades and duality; forests; resistances; principal-minor inequalities")


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
