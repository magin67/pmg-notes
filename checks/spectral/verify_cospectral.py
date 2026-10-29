"""Exact cospectral weighted graphs, forest counts and physical-scale duality.

All identities use rational arithmetic. Edge expansions, spectral expansions,
forest enumeration and reduced-matrix inverses are computed independently.
Run without Python's -O flag. No files are written.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
import json

from verify_diagonal import (
    scale, square, form_matrix, grades, exponential_from_factors, evaluate,
    matmul, multiply, determinant, inverse, laplacian, forest_partition, act,
)
from verify_projectors import mscale, madd, projector

RAW = [(1, -1, 0, 0), (1, 1, -1, -1), (0, 0, 1, -1)]
NORMS = [2, 4, 2]
EDGES = [
    [(i, j, F(3 if (i, j) == (0, 1) else 1))
     for i, j in combinations(range(4), 2)],
    [(i, j, F(2)) for i in (0, 1) for j in (2, 3)],
]
LAMBDAS = [[F(8), F(4), F(4)], [F(4), F(8), F(4)]]


def edge_expansion(edges, reduced=False):
    factors = []
    for i, j, weight in edges:
        q = [F(0)] * 4
        q[i], q[j] = -1, 1
        factors.append(scale(square(q[:3] if reduced else q), weight))
    return exponential_from_factors(factors)


def forest_coefficients(edges):
    ordinary, rooted = [F(0)] * 4, [F(0)] * 4
    for g in range(4):
        for subset in combinations(edges, g):
            components = forest_partition(4, subset)
            if components is not None:
                weight = prod(c for _, _, c in subset)
                ordinary[g] += weight
                rooted[g] += weight * prod(len(c) for c in components)
    return ordinary, rooted


def quadratic(matrix, v):
    return sum(v[i] * matrix[i][j] * v[j] for i in range(4) for j in range(4))


def check():
    identity = [[F(i == j) for j in range(4)] for i in range(4)]
    J = [[identity[i][j] - F(1, 4) for j in range(4)] for i in range(4)]
    zero = [[F(0)] * 4 for _ in range(4)]
    forms = [scale(square(q), F(1, norm)) for q, norm in zip(RAW, NORMS)]
    dual_forms = [scale(square([q[i] - q[-1] for i in range(3)]), F(1, norm))
                  for q, norm in zip(RAW, NORMS)]
    cases, full_grades = [], []
    for index, (edges, eigenvalues) in enumerate(zip(EDGES, LAMBDAS)):
        L = laplacian(4, edges)
        E8 = projector([RAW[index]], [NORMS[index]])
        E4 = madd(J, mscale(E8, -1))
        assert matmul(E8, E8) == E8 and matmul(E4, E4) == E4
        assert matmul(E4, E8) == matmul(E8, E4) == zero
        assert sum(E8[i][i] for i in range(4)) == 1
        assert sum(E4[i][i] for i in range(4)) == 2
        assert L == madd(mscale(J, 4), mscale(E8, 4))
        for q, norm, eigenvalue in zip(RAW, NORMS, eigenvalues):
            assert sum(q) == 0 and sum(v*v for v in q) == norm
            assert [sum(a*b for a, b in zip(row, q)) for row in L] == [eigenvalue*v for v in q]
        for q, r in combinations(RAW, 2):
            assert sum(a*b for a, b in zip(q, r)) == 0

        inv = inverse([[L[i][j]+F(1, 4) for j in range(4)] for i in range(4)])
        Gr = [[v-F(1, 4) for v in row] for row in inv]
        assert Gr == madd(mscale(E4, F(1, 4)), mscale(E8, F(1, 8)))
        assert matmul(L, Gr) == matmul(Gr, L) == J
        M = edge_expansion(edges)
        assert M == exponential_from_factors([scale(a, l) for a, l in zip(forms, eigenvalues)])
        Mg = grades(M, 3)
        full_grades.append(Mg)
        Ng = grades(exponential_from_factors([scale(a, 1/l) for a, l in zip(forms, eigenvalues)]), 3)
        ordinary, rooted = forest_coefficients(edges)
        assert rooted == [1, 16, 80, 128]
        assert ordinary == [1, 8, 25-index, 32]
        assert [evaluate(m, identity) for m in Mg] == rooted
        assert [evaluate(m, identity) for m in Ng] == [F(rooted[3-g], 128) for g in range(4)]
        assert all(evaluate(Mg[g], Gr) == [1, 3, 3, 1][g] for g in range(4))
        # Five exact evaluations determine the characteristic polynomial of degree four.
        for xi in [-2, 0, 1, 4, 9]:
            chi = determinant([[xi*identity[i][j]-L[i][j] for j in range(4)] for i in range(4)])
            assert chi == sum((-1)**g * rooted[g] * xi**(4-g) for g in range(4))
            assert chi == xi*(xi-4)**2*(xi-8)
        volume = multiply(multiply(forms[0], forms[1]), forms[2])
        T4 = scale(volume, 4)
        assert Mg[3] == scale(T4, 32) and Ng[3] == scale(T4, F(1, 512))
        assert determinant([row[:3] for row in L[:3]]) == 32

        # Conductance rescaling changes the algebraically dual exponential inversely.
        for s in [F(1, 2), F(1), F(2), F(3)]:
            scaled_edges = [(i, j, s*c) for i, j, c in edges]
            scaled_L = laplacian(4, scaled_edges)
            Mr = grades(edge_expansion(scaled_edges, reduced=True), 3)
            reduced_inverse = inverse([row[:3] for row in scaled_L[:3]])
            Q = grades(exponential_from_factors(
                [scale(a, 1/(s*l)) for a, l in zip(dual_forms, eigenvalues)]), 3)
            assert Q[1] == form_matrix(reduced_inverse)
            for g in range(4):
                assert act(Mr[3], Q[g]) == Mr[3-g]
                assert act(Q[3], Mr[g]) == Q[3-g]
            if s != 1:
                wrong_Q = grades(exponential_from_factors(
                    [scale(a, s/l) for a, l in zip(dual_forms, eigenvalues)]), 3)
                assert act(Mr[3], wrong_Q[1]) != Mr[2]

        resistances, contributions = {}, {}
        for i, j in combinations(range(4), 2):
            b = [F(0)] * 4
            b[i], b[j] = -1, 1
            parts = [quadratic(E4, b)/4, quadratic(E8, b)/8]
            resistance = quadratic(Gr, b)
            assert sum(parts) == resistance
            key = f"{i+1}{j+1}"
            resistances[key], contributions[key] = resistance, parts
        assert resistances["12"] == [F(1, 4), F(1, 2)][index]
        assert resistances["13"] == [F(7, 16), F(3, 8)][index]
        assert sum(resistances.values()) == 4*sum(Gr[i][i] for i in range(4)) == F(5, 2)
        cases.append({"graph": index+1, "edges": edges, "L": L, "Gr": Gr,
                      "eigenvalues_in_common_basis": eigenvalues,
                      "ordinary": ordinary, "rooted": rooted,
                      "R": resistances, "contributions": contributions,
                      "tau": F(32), "Kf": F(5, 2)})
    assert full_grades[0][1] != full_grades[1][1]
    assert full_grades[0][2] != full_grades[1][2]
    assert full_grades[0][3] == full_grades[1][3]
    return {"cases": cases, "physical_scales_checked": ["1/2", "1", "2", "3"]}


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2, default=str))
