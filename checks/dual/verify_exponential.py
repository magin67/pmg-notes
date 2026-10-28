"""Exact checks for exterior exponentials, minors and complementary grades.

Run: python checks/dual/verify_exponential.py
Uses only the standard library; writes JSON to stdout and creates no files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
import random
import json

from exterior_checks import add, multiply as mul, act, det, inv, wedge, tensor, verify_forest_minors
unit = {(0, 0): F(1)}

def scale(p, c):
    return {key: value*c for key, value in p.items() if value*c}

def form(A):
    return {(1 << i, 1 << j): F(v) for i, row in enumerate(A)
            for j, v in enumerate(row) if v}

def powers(A):
    out, p = [], unit
    for k in range(len(A)+2):
        out.append(scale(p, F(1, factorial(k))))
        p = mul(p, form(A))
    return out

def minors(A, k):
    out = {}
    for I in combinations(range(len(A)), k):
        for J in combinations(range(len(A)), k):
            value = det([[A[i][j] for j in J] for i in I])
            if value:
                out[sum(1 << i for i in I), sum(1 << j for j in J)] = value
    return out

def main():
    rng = random.Random(20261026)
    cases = [[[0]], [[-3]], [[1, 2], [2, 4]],
             [[2, 1, 0], [1, -3, 2], [0, 2, 1]],
             [[1, 2, 3], [0, 0, 0], [0, 1, -2]]]
    for d in range(2, 6):
        for symmetric in [False, True]:
            for _ in range(3):
                A = [[F(rng.randrange(-3, 4)) for j in range(d)] for i in range(d)]
                if symmetric:
                    A = [[A[min(i, j)][max(i, j)] for j in range(d)] for i in range(d)]
                cases.append(A)
    dual_cases = 0
    for A in cases:
        E = powers(A)
        for k in range(len(E)):
            assert E[k] == minors(A, k), ('minors', A, k)
        if det(A) and all(A[i][j] == A[j][i] for i in range(len(A)) for j in range(len(A))):
            dual_cases += 1
            D = powers(inv(A))
            mask = (1 << len(A))-1
            T = {(mask, mask): F(1)}
            for k in range(len(A)+1):
                assert act(T, scale(D[k], det(A))) == E[len(A)-k], ('duality', A, k)

    def outer(v):
        return [[F(x*y) for y in v] for x in v]

    def rank_one_form(v):
        return form(outer(v))

    vectors = [[1, 0, 0], [1, 1, 0], [0, 0, 1], [2, -1, 1], [0, 1, -2]]
    coefficients = [F(2), F(-3), F(5), F(1, 2), F(-2)]
    S, factored = {}, unit
    for v, c in zip(vectors, coefficients):
        f = scale(rank_one_form(v), c)
        S = add(S, f)
        factored = mul(factored, add(unit, f))
    A = [[S.get((1 << i, 1 << j), F(0)) for j in range(3)] for i in range(3)]
    expanded = {}
    for p in powers(A):
        expanded = add(expanded, p)
    assert expanded == factored

    # Use a,b,d as a basis of the quotient; c=-a-b-d.
    a, b, c, d = [1, 0, 0], [0, 1, 0], [-1, -1, -1], [0, 0, 1]
    def wedge_square(u, v):
        ub = {1 << i: F(x) for i, x in enumerate(u) if x}
        vb = {1 << i: F(x) for i, x in enumerate(v) if x}
        w = wedge(ub, vb)
        return tensor(w, w)

    S = add(add(scale(rank_one_form(a), F(2)), scale(rank_one_form([1,1,0]), F(3))), scale(rank_one_form(d), F(5)))
    assert scale(mul(S, S), F(1,2)) == add(add(scale(wedge_square(a,b), F(6)), scale(wedge_square(a,d), F(10))), scale(wedge_square(c,d), F(15)))
    assert scale(mul(mul(S,S),S), F(1,6)) == {(7,7): F(30)}
    S0 = add(add(rank_one_form(a), rank_one_form(b)), rank_one_form([1,1,0]))
    assert scale(mul(S0,S0), F(1,2)) == {(3,3): F(3)}
    assert not mul(mul(S0,S0),S0)

    def mm(A, B):
        return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

    def tr(A):
        return list(map(list,zip(*A)))

    def centered_check(edges):
        n = 4
        L = [[F(0) for j in range(n)] for i in range(n)]
        for i,j,c in edges:
            L[i][i] += c; L[j][j] += c; L[i][j] -= c; L[j][i] -= c
        A = [row[:-1] for row in L[:-1]]
        U = [[F(int(i==j)-int(i==n-1)) for j in range(n-1)] for i in range(n)]
        C = [[F(int(i==j))-F(1,n) for j in range(n-1)] for i in range(n)]
        J = [[F(int(i==j))-F(1,n) for j in range(n)] for i in range(n)]
        assert mm(tr(U),C) == [[F(i==j) for j in range(n-1)] for i in range(n-1)]
        assert mm(U,tr(C)) == J
        K = mm(mm(C,inv(A)),tr(C))
        assert mm(mm(U,A),tr(U)) == L
        assert mm(L,K) == J
        assert all(sum(row)==0 for row in K)
        # Independent inverse of L+11^T/n, then remove 11^T/n.
        independent = inv([[L[i][j]+F(1,n) for j in range(n)] for i in range(n)])
        independent = [[x-F(1,n) for x in row] for row in independent]
        assert K == independent
        return K

    graphs = [('P4', 4, [(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
              ('weightedP4', 4, [(0,1,F(2)),(1,2,F(3)),(2,3,F(5))]),
              ('K4', 4, [(i,j,F(1)) for i,j in combinations(range(4),2)])]
    graph_results = []
    for name,n,edges in graphs:
        graph_results.append(verify_forest_minors(name,n,edges))
        K = centered_check(edges)
        if name == 'P4':
            assert K == [[F(x,8) for x in row] for row in [[7,1,-3,-5],[1,3,-1,-3],[-3,-1,3,1],[-5,-3,1,7]]]

    print(json.dumps({'matrix_cases':len(cases), 'inverse_duality_cases':dual_cases,
                      'factorization':'exact', 'cut_examples':'exact', 'graphs':graph_results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
