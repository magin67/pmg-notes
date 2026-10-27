"""Exact checks for metric and potentials of exp(Greenian).

Run: python checks/dual/verify_potentials.py
Uses only the standard library and the adjacent verify_vector.py.
Builds the exterior exponential from signed vector factors, independently
of the Laplacian Gram determinants used to check its potentials.
No files are written. All arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod
import json

from verify_vector import (add, wedge, tensor, multiply, determinant, inverse,
                           laplacian, forest_partition, minor_form)


def pairing(u, A, v):
    return sum((u[i] * A[i][j] * v[j]
                for i in range(len(A)) for j in range(len(A))), F(0))


def edge_vector(n, i, j):
    return [F((t == j) - (t == i)) for t in range(n)]


def as_blade(v):
    # In the direct basis a_i-a_n, a zero-sum vector has coordinates v[:-1].
    return {1 << i: x for i, x in enumerate(v[:-1]) if x}


def exterior(columns):
    out = {0: F(1)}
    for v in columns:
        out = wedge(out, as_blade(v))
    return out


def gram(U, A, V=None):
    if V is None:
        V = U
    return [[pairing(u, A, v) for v in V] for u in U]


def verify(name, n, source_edges):
    edges = [(i, j, F(c)) for i, j, c in source_edges]
    d, full = n - 1, (1 << (n - 1)) - 1
    L = laplacian(n, edges)
    tau = determinant([row[:-1] for row in L[:-1]])
    Gr = inverse([[L[i][j] + F(1, n) for j in range(n)] for i in range(n)])
    Gr = [[v - F(1, n) for v in row] for row in Gr]
    sigma = F(1, n*n) / tau
    N = {(0, 0): F(1)}
    for i, j in combinations(range(n), 2):
        v = as_blade(edge_vector(n, i, j))
        N = multiply(N, add({(0, 0): F(1)}, tensor(v, v), -Gr[i][j]))
    assert N[(full, full)] == sigma
    Grhat = [row[:-1] for row in Gr[:-1]]
    for k in range(n):
        assert {ij: c for ij, c in N.items() if ij[0].bit_count() == k} == minor_form(Grhat, k)

    def P(X, Y=None):
        if Y is None:
            Y = X
        return multiply(N, tensor(X, Y)).get((full, full), F(0)) / sigma

    counts = dict(mixed_basis=0, centered_pairs=0, cuts=0, contrasts=0,
                  boundaries=0, cauchy_binet_terms=0, dirichlet_pairs=0)
    basis = [edge_vector(n, n-1, i) for i in range(d)]
    for k in range(n):
        for I in combinations(range(d), k):
            for J in combinations(range(d), k):
                U, V = [basis[i] for i in I], [basis[j] for j in J]
                assert P(exterior(U), exterior(V)) == determinant(gram(U, L, V))
                counts['mixed_basis'] += 1
    centered = [[F(i == j) - F(1, n) for j in range(n)] for i in range(n)]
    for i, j in product(range(n), repeat=2):
        assert P(as_blade(centered[i]), as_blade(centered[j])) == L[i][j]
        counts['centered_pairs'] += 1
    for mask in range(1, (1 << n)-1):
        members = [i for i in range(n) if mask >> i & 1]
        s = [F(i in members) - F(len(members), n) for i in range(n)]
        cut = sum((c for i, j, c in edges if (i in members) != (j in members)), F(0))
        assert P(as_blade(s)) == cut
        counts['cuts'] += 1
    for phi in product((-1, 0, 1), repeat=n):
        if -1 not in phi or 1 not in phi:
            continue
        s = [F(v) - F(sum(phi), n) for v in phi]
        cross = F(0)
        for i, j, c in edges:
            if phi[i] == phi[j]:
                continue
            cross += (4 if phi[i] * phi[j] == -1 else 1) * c
        assert P(as_blade(s)) == cross
        counts['contrasts'] += 1
    values = {}
    for size in range(2, n+1):
        for S in combinations(range(n), size):
            U = [edge_vector(n, S[0], j) for j in S[1:]]
            X = exterior(U)
            value = P(X)
            assert value == determinant(gram(U, L)) > 0
            cb = F(0)
            for chosen in combinations(edges, size-1):
                V = [edge_vector(n, i, j) for i, j, _ in chosen]
                D = determinant([[sum((x*y for x, y in zip(u, v)), F(0))
                                  for v in V] for u in U])
                if forest_partition(n, chosen) is None:
                    assert D == 0
                cb += prod((c for _, _, c in chosen), start=F(1)) * D * D
                counts['cauchy_binet_terms'] += 1
            assert value == cb
            values[''.join(chr(97+i) for i in S)] = str(value)
            counts['boundaries'] += 1
    assert P({full: F(1)}) == n*n*tau
    assert multiply(N, {(full, full): F(1)})[(full, full)] == 1

    for i, j in combinations(range(n), 2):
        w = edge_vector(n, i, j)
        R = pairing(w, Gr, w)
        S = P(as_blade(w))
        cij = -L[i][j]
        assert S == L[i][i] + L[j][j] + 2*cij
        I = [v for v in range(n) if v not in (i, j)]
        phi = [F(0)] * n
        phi[i], phi[j] = F(-1), F(1)
        Ainv = inverse([[L[a][b] for b in I] for a in I])
        rhs = [L[a][i] - L[a][j] for a in I]
        for row, a in enumerate(I):
            phi[a] = sum((Ainv[row][b] * rhs[b] for b in range(len(I))), F(0))
        assert all(sum((L[a][b]*phi[b] for b in range(n)), F(0)) == 0 for a in I)
        assert pairing(phi, L, phi) == 4 / R
        assert S * R >= 4
        Lw = [sum((L[a][b]*w[b] for b in range(n)), F(0)) for a in range(n)]
        assert (S*R == 4) == (Lw == [S/2 * v for v in w])
        counts['dirichlet_pairs'] += 1
    if n >= 5:
        # A nondecomposable bivector: bilinear continuation beyond blades.
        X = add(exterior(basis[:2]), exterior(basis[2:4]))
        expected = sum((determinant(gram(U, L, V))
                        for U in (basis[:2], basis[2:4])
                        for V in (basis[:2], basis[2:4])), F(0))
        assert P(X) == expected > 0
    return dict(name=name, tau=str(tau), sigma=str(sigma), checks=counts, values=values)


def main():
    cases = [
        ('weighted_edge', 2, [(0, 1, 2)]),
        ('P3', 3, [(0, 1, 1), (1, 2, 1)]),
        ('P4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
        ('weighted_P4', 4, [(0, 1, 2), (1, 2, 3), (2, 3, 5)]),
        ('weighted_K3', 3, [(0, 1, 2), (0, 2, 3), (1, 2, 5)]),
        ('K4', 4, [(i, j, 1) for i, j in combinations(range(4), 2)]),
        ('C4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)]),
        ('star4', 4, [(0, i, 1) for i in range(1, 4)]),
        ('weighted5', 5, [(0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 4, 7), (0, 4, 11), (1, 3, 13)])]
    results = [verify(*case) for case in cases]
    indexed = {r['name']: r for r in results}
    assert indexed['P4']['values'] == dict(ab='5', ac='3', ad='2', bc='6', bd='3', cd='5',
                                         abc='14', abd='6', acd='6', bcd='14', abcd='16')
    assert indexed['weighted_P4']['values'] == dict(ab='11', ac='10', ad='7', bc='19', bd='10', cd='23',
                                                  abc='109', abd='61', acd='61', bcd='181', abcd='480')
    assert indexed['weighted_K3']['values'] == dict(ab='16', ac='19', bc='25', abc='279')
    assert indexed['K4']['values']['ab'] == '8'
    assert indexed['K4']['values']['abc'] == '48'
    assert indexed['K4']['values']['abcd'] == '256'
    # Check the three coefficients 9, 4, 1 independently of edge weights.
    U = [edge_vector(4, 0, 1), edge_vector(4, 0, 2)]
    V = [edge_vector(4, i, i+1) for i in range(3)]
    assert [determinant([[sum(x*y for x, y in zip(u, v)) for v in pair] for u in U])**2
            for pair in combinations(V, 2)] == [9, 4, 1]
    complete_checks = 0
    for n in range(2, 8):
        c = F(2, 3)
        L = laplacian(n, [(i, j, c) for i, j in combinations(range(n), 2)])
        for k in range(n):
            U = [edge_vector(n, 0, i) for i in range(1, k+1)]
            assert determinant(gram(U, L)) == (k+1)*(n*c)**k
            complete_checks += 1
    totals = {key: sum(r['checks'][key] for r in results) for key in results[0]['checks']}
    print(json.dumps(dict(status='passed', graphs=len(results), checks=totals,
                          complete_graph_grades=complete_checks, results=results), indent=2))


if __name__ == '__main__':
    main()
