"""Exact P3 checks for the first spectral note; standard library only.

Integer eigenvectors are kept unnormalised. Their squared lengths divide
rank-one tensors, so all tensor, metric and duality checks use rational numbers.
The edge expansion, spectral expansion, matrix inverse and forest enumeration
are computed independently. Run without Python's -O flag.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "dual"))
from verify_vector import (add, multiply, wedge, tensor, determinant, inverse,
                           laplacian, forest_partition)
from exterior_checks import act


def scale(form, c):
    return {k: c*v for k, v in form.items() if c*v}


def vector(values):
    return {1 << i: F(v) for i, v in enumerate(values) if v}


def square(values):
    v = vector(values)
    return tensor(v, v)


def form_matrix(matrix):
    return {(1 << i, 1 << j): F(v) for i, row in enumerate(matrix)
            for j, v in enumerate(row) if v}


def grades(form, dimension):
    return [{k: v for k, v in form.items() if k[0].bit_count() == g}
            for g in range(dimension+1)]


def exponential_from_factors(factors):
    result = {(0, 0): F(1)}
    for term in factors:
        result = multiply(result, add({(0, 0): F(1)}, term))
    return result


def evaluate(form, metric):
    total = F(0)
    for (a, b), c in form.items():
        rows = [i for i in range(len(metric)) if a >> i & 1]
        cols = [j for j in range(len(metric)) if b >> j & 1]
        total += c*determinant([[metric[i][j] for j in cols] for i in rows])
    return total


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def check():
    n, d = 3, 2
    edges = [(0, 1, F(1)), (1, 2, F(1))]
    L = laplacian(n, edges)
    identity = [[F(i == j) for j in range(n)] for i in range(n)]
    J = [[identity[i][j]-F(1, n) for j in range(n)] for i in range(n)]
    inv = inverse([[L[i][j]+F(1, n) for j in range(n)] for i in range(n)])
    Gr = [[v-F(1, n) for v in row] for row in inv]
    assert Gr == [[F(v, 9) for v in row] for row in [[5,-1,-4],[-1,2,-1],[-4,-1,5]]]
    assert matmul(L, Gr) == matmul(Gr, L) == J

    raw_modes = [(1, 0, -1), (1, -2, 1)]
    lengths = [sum(v*v for v in row) for row in raw_modes]
    lambdas = [F(1), F(3)]
    assert lengths == [2, 6]
    for q, eigenvalue in zip(raw_modes, lambdas):
        assert sum(q) == 0
        assert [sum(v*w for v,w in zip(row,q)) for row in L] == [eigenvalue*v for v in q]
    assert sum(a*b for a,b in zip(*raw_modes)) == 0
    modal_forms = [scale(square(q), F(1, s)) for q,s in zip(raw_modes, lengths)]
    direct_factors = [scale(a,l) for a,l in zip(modal_forms, lambdas)]
    green_factors = [scale(a,1/l) for a,l in zip(modal_forms, lambdas)]
    assert add(*direct_factors) == form_matrix(L)
    assert add(*green_factors) == form_matrix(Gr)
    for a in modal_forms:
        assert multiply(a, a) == {}

    edge_forms = []
    for i,j,c in edges:
        q = [F(0)]*n; q[i], q[j] = -1, 1
        edge_forms.append(scale(square(q), c))
    M = exponential_from_factors(direct_factors)
    assert M == exponential_from_factors(edge_forms)
    Mgrades = grades(M,d)
    Ngrades = grades(exponential_from_factors(green_factors),d)
    assert Mgrades[2] == scale(multiply(form_matrix(L),form_matrix(L)),F(1,2))

    # T3 is the square of the wedge of vertex differences, independently of modes.
    boundary = wedge(vector((1,0,-1)),vector((0,1,-1)))
    T = tensor(boundary,boundary)
    assert Mgrades[2] == T
    assert Ngrades[2] == scale(T,F(1,9))
    assert evaluate(T,identity) == 3
    assert multiply(*modal_forms) == scale(T,F(1,3))

    # In the basis b1=a1-a3, b2=a2-a3 the dual coordinate pairing is exact.
    b = [(1,0,-1),(0,1,-1)]
    direct_coordinates = [q[:2] for q in raw_modes]
    dual_coordinates = [[sum(qi*bi for qi,bi in zip(q, bj)) for bj in b] for q in raw_modes]
    direct_reduced = [scale(square(q),l/s) for q,l,s in zip(direct_coordinates,lambdas,lengths)]
    dual_reduced = [scale(square(q),1/(l*s)) for q,l,s in zip(dual_coordinates,lambdas,lengths)]
    Mr = grades(exponential_from_factors(direct_reduced),d)
    Q = grades(exponential_from_factors(dual_reduced),d)
    reduced_L = [row[:d] for row in L[:d]]
    assert Q[1] == form_matrix(inverse(reduced_L))
    for g in range(d+1):
        assert act(Mr[d],Q[g]) == Mr[d-g]
        assert act(Q[d],Mr[g]) == Q[d-g]

    # C sends the two reduced dual coordinate functionals to a_i-h.
    centered = [[F(i == j)-F(1,n) for j in range(n)] for i in range(d)]
    C_factors = []
    for q,l,s in zip(dual_coordinates,lambdas,lengths):
        cq = [sum(q[i]*centered[i][j] for i in range(d)) for j in range(n)]
        C_factors.append(scale(square(cq),1/(l*s)))
    assert grades(exponential_from_factors(C_factors),d) == Ngrades

    p = [evaluate(g,identity) for g in Mgrades]
    p_green = [evaluate(g,identity) for g in Ngrades]
    assert p == [1,4,3] and p_green == [1,F(4,3),F(1,3)]
    assert p_green == [v/prod(lambdas) for v in reversed(p)]
    assert [evaluate(g,Gr) for g in Mgrades] == [1,2,1]
    assert [evaluate(g,L) for g in Ngrades] == [1,2,1]
    assert [evaluate(a,Gr) for a in modal_forms] == [1,F(1,3)]
    assert [evaluate(a,L) for a in modal_forms] == [1,3]
    for matrix, coefficients in [(L,p),(Gr,p_green)]:
        for g in range(d+1):
            minor_sum = sum(determinant([[matrix[i][j] for j in I] for i in I])
                            for I in combinations(range(n),g))
            assert minor_sum == coefficients[g]

    ordinary = [F(0)]*n; rooted = [F(0)]*n
    for g in range(len(edges)+1):
        for subset in combinations(edges,g):
            components = forest_partition(n,subset)
            if components is not None:
                weight = prod(c for _,_,c in subset)
                ordinary[g] += weight
                rooted[g] += weight*prod(map(len,components))
    assert ordinary == [1,2,1] and rooted == p
    tau = determinant(reduced_L)
    assert tau == 1 and prod(lambdas) == n*tau
    R = [[Gr[i][i]+Gr[j][j]-2*Gr[i][j] for j in range(n)] for i in range(n)]
    assert R == [[0,1,2],[1,0,1],[2,1,0]]
    for i,j in combinations(range(n),2):
        assert R[i][j] == sum(F((q[i]-q[j])**2,s)/l for q,s,l in zip(raw_modes,lengths,lambdas))
    Kf = sum(R[i][j] for i,j in combinations(range(n),2))
    assert Kf == n*sum(Gr[i][i] for i in range(n)) == 4
    return dict(graph="P3", raw_modes=raw_modes, squared_lengths=lengths,
                eigenvalues=list(map(str,lambdas)), rooted=list(map(str,p)),
                green_rooted=list(map(str,p_green)), ordinary=list(map(str,ordinary)),
                tau=str(tau), green_top_coefficient="1/9", Kirchhoff_index=str(Kf),
                checked="edge and modal tensors; both contractions; C; all grade evaluations; forests; resistances")


if __name__ == "__main__":
    print(json.dumps(check(),ensure_ascii=False,indent=2))
