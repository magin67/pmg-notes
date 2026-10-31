"""Exact checks for 'One resistance and quadric connectivity'.

Standard library only. Compare prescribed resistance data, Greenian factors,
dual contraction, direct inversion, tree/forest sums, and full pair Jacobians.
Run: python checks/variations/verify_one_resistance.py
"""

from fractions import Fraction as Q
from itertools import combinations
import json

from verify_single_edge import determinant, inverse, exterior_grade, forest_sums
from verify_one_greenian_coefficient import (
    matvec, pairing, rank_update, principal, centered_inverse, laplacian,
    coefficients, compound, delete_from_top,
)


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def scale(t, a):
    return [[t*x for x in row] for row in a]


def add(*matrices):
    return [[sum(entries) for entries in zip(*rows)] for rows in zip(*matrices)]


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def positive(a):
    return all(determinant([row[:k] for row in a[:k]]) > 0
               for k in range(1, len(a)+1))


def resistance(green):
    return [[green[i][i]+green[j][j]-2*green[i][j] for j in range(len(green))]
            for i in range(len(green))]


def double_center(r):
    n = len(r)
    j = [[Q(i == k)-Q(1, n) for k in range(n)] for i in range(n)]
    return scale(-Q(1, 2), multiply(multiply(j, r), j))


def pair_matrices(L, Gr):
    pairs = list(combinations(range(len(L)), 2))
    S = [[(Gr[i][k]-Gr[i][l]-Gr[j][k]+Gr[j][l])**2
          for k, l in pairs] for i, j in pairs]
    Lq = [[(L[i][k]*L[j][l]+L[i][l]*L[j][k])/2
           for k, l in pairs] for i, j in pairs]
    return pairs, S, Lq


def verify_pair_matrices(L, Gr, weights):
    pairs, S, Lq = pair_matrices(L, Gr)
    assert multiply(S, Lq) == multiply(Lq, S) == identity(len(pairs))
    assert inverse(S) == Lq and positive(S) and positive(Lq)
    E = [i for i, e in enumerate(pairs) if weights.get(e, 0)]
    Z = [i for i, e in enumerate(pairs) if not weights.get(e, 0)]
    if Z:
        schur = add(block(Lq, E, E), scale(-1, multiply(multiply(
            block(Lq, E, Z), inverse(block(Lq, Z, Z))), block(Lq, Z, E))))
        assert inverse(block(S, E, E)) == schur
    # Differentiate the inverse directly for each independent symmetric R entry.
    n = len(L)
    for column, (k, l) in enumerate(pairs):
        dr = [[Q(0) for _ in range(n)] for _ in range(n)]
        dr[k][l] = dr[l][k] = Q(1)
        dg = double_center(dr)
        dl = scale(-1, multiply(multiply(L, dg), L))
        assert dl == scale(Q(1, 2), multiply(multiply(L, dr), L))
        for row, (i, j) in enumerate(pairs):
            assert dl[i][j] == Lq[row][column]
        # Derivative of det of a reduced Laplacian, independent of the formula.
        product = multiply(inverse(principal(L)), principal(dl))
        assert sum(product[i][i] for i in range(n-1)) == L[k][l]
    return bool(Z)


def verify_graph(name, n, weights):
    L = laplacian(n, weights)
    Gr = centered_inverse(L)
    gamma = coefficients(Gr)
    R = resistance(Gr)
    assert double_center(R) == Gr
    tau = determinant(principal(L))
    assert tau == forest_sums(n, weights)[0] > 0
    sigma = Q(1, n*n)/tau
    grades = [exterior_grade(n, gamma, r) for r in range(n)]
    dual = inverse(principal(L))
    restricted = verify_pair_matrices(L, Gr, weights)
    cases = singular = nonnegative = signed_positive = indefinite = 0
    for k, l in combinations(range(n), 2):
        A, B, C = L[k][k], L[l][l], L[k][l]
        x, y = [row[k] for row in L], [row[l] for row in L]
        pk = [Q(i == k)-Q(1, n) for i in range(n)]
        pl = [Q(i == l)-Q(1, n) for i in range(n)]
        u, v = [a-b for a, b in zip(pk, pl)], [a+b for a, b in zip(pk, pl)]
        assert pairing(u, L, u) == A+B-2*C
        assert pairing(v, L, v) == A+B+2*C
        assert pairing(u, L, v) == A-B
        extras = [[exterior_grade(n, gamma, r, directions) for r in range(n)]
                  for directions in ((u[:-1],), (v[:-1],), (u[:-1], v[:-1]))]
        samples = {Q(0), R[k][l]/4, -R[k][l]/4, R[k][l]/2,
                   R[k][l], -R[k][l], 3*R[k][l]}
        if name == 'unit_triangle':
            samples.update({-Q(2, 3), -Q(2, 3)+Q(1, 100), Q(1, 3), Q(2, 3), Q(1), Q(2)})
        for rho in sorted(samples):
            phi = 1-rho*C-rho*rho*(A*B-C*C)/4
            eta = 1-rho*C/2
            s, t = rho/4, -rho/4
            new_R = [row[:] for row in R]
            new_R[k][l] += rho
            new_R[l][k] += rho
            new_Gr = double_center(new_R)
            assert resistance(new_Gr) == new_R
            assert new_Gr == rank_update(rank_update(Gr, s, u), t, v)
            new_gamma = coefficients(new_Gr)
            for (i, j), value in new_gamma.items():
                expected = rho*(pk[i]*pl[j]+pl[i]*pk[j])/2
                overlap = len({i, j} & {k, l})
                table = {2: rho*Q(n*n-2*n+2, 2*n*n),
                         1: -rho*Q(n-2, 2*n*n), 0: rho/Q(n*n)}
                assert value-gamma[i, j] == expected == table[overlap]
            for r in range(n):
                factored = add(grades[r], scale(s, extras[0][r]),
                               scale(t, extras[1][r]), scale(s*t, extras[2][r]))
                assert exterior_grade(n, new_gamma, r) == factored
            new_sigma = determinant(principal(new_Gr))
            assert new_sigma == sigma*phi
            z = [u[i]-u[-1] for i in range(n-1)]
            w = [v[i]-v[-1] for i in range(n-1)]
            new_dual = rank_update(rank_update(dual, s, z), t, w)
            assert determinant(new_dual) == n*n*new_sigma
            assert positive(principal(new_Gr)) == (phi > 0)
            cases += 1
            if not phi:
                assert exterior_grade(n, new_gamma, n-1) == [[Q(0)]]
                singular += 1
                continue
            new_L = centered_inverse(new_Gr)
            formula = [[L[i][j] + (rho*eta*(x[i]*y[j]+y[i]*x[j])/2
                       +rho*rho*(B*x[i]*x[j]+A*y[i]*y[j])/4)/phi
                        for j in range(n)] for i in range(n)]
            assert new_L == formula
            new_c = coefficients(new_L)
            new_tau = determinant(principal(new_L))
            tree_tau, forests = forest_sums(n, new_c)
            assert new_tau == tree_tau == tau/phi
            assert resistance(centered_inverse(new_L)) == new_R
            for i, j in combinations(range(n), 2):
                assert forests[i, j]/new_tau == new_R[i][j]
            for r in range(n):
                restored = scale(new_tau, delete_from_top(new_dual, r))
                assert restored == compound(principal(new_L), n-1-r)
            # Exact finite inverse identity includes the factor 1/2.
            dr = add(new_R, scale(-1, R))
            assert add(new_L, scale(-1, L)) == scale(Q(1, 2),
                multiply(multiply(new_L, dr), L))
            if phi > 0:
                if all(c >= 0 for c in new_c.values()):
                    nonnegative += 1
                else:
                    signed_positive += 1
            else:
                indefinite += 1
    return dict(graph=name, variations=cases, singular=singular,
                nonnegative_graphs=nonnegative, positive_with_negative_conductances=signed_positive,
                indefinite=indefinite, restricted_edge_schur_checked=restricted)


def verify_displayed_examples():
    L = laplacian(3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)})
    Gr = centered_inverse(L)
    R = resistance(Gr)
    pairs, S, Lq = pair_matrices(L, Gr)
    assert pairs == [(0, 1), (0, 2), (1, 2)]
    assert S == scale(Q(1, 9), [[4, 1, 1], [1, 4, 1], [1, 1, 4]])
    assert Lq == scale(Q(1, 2), [[5, -1, -1], [-1, 5, -1], [-1, -1, 5]])
    samples = (-Q(2, 3)+Q(1, 100), -Q(1, 3), Q(0), Q(1, 3), Q(2, 3), Q(1), Q(3))
    for rho in samples:
        new_R = [row[:] for row in R]
        new_R[0][1] += rho
        new_R[1][0] += rho
        new_Gr = double_center(new_R)
        new_L = centered_inverse(new_Gr)
        phi = 1+rho-Q(3, 4)*rho*rho
        expected = {(0, 1): (1-3*rho/2)/phi,
                    (0, 2): (1+3*rho/2)/phi, (1, 2): (1+3*rho/2)/phi}
        assert coefficients(new_L) == expected
        assert all(c >= 0 for c in expected.values()) == (-Q(2, 3) < rho <= Q(2, 3))
        if rho == Q(1, 3):
            assert expected == {(0, 1): Q(2, 5), (0, 2): Q(6, 5), (1, 2): Q(6, 5)}
            assert determinant(principal(new_L)) == Q(12, 5)
            assert coefficients(new_Gr) == {(0, 1): Q(11, 54), (0, 2): Q(5, 54), (1, 2): Q(5, 54)}
    path = laplacian(3, {(0, 1): Q(1), (1, 2): Q(1)})
    _, S, Lq = pair_matrices(path, centered_inverse(path))
    assert block(S, [0, 2], [0, 2]) == identity(2)
    assert block(Lq, [0, 2], [0, 2]) == [[Q(3, 2), Q(1, 2)], [Q(1, 2), Q(3, 2)]]
    assert verify_pair_matrices(path, centered_inverse(path), {(0, 1): Q(1), (1, 2): Q(1)})


def main():
    graphs = [
        ('weighted_edge', 2, {(0, 1): Q(3, 2)}),
        ('unit_triangle', 3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}),
        ('weighted_triangle', 3, {(0, 1): Q(2), (0, 2): Q(5), (1, 2): Q(3)}),
        ('unit_P4', 4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}),
        ('weighted_C4', 4, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)}),
    ]
    results = [verify_graph(*g) for g in graphs]
    verify_displayed_examples()
    print(json.dumps(dict(status='passed', graphs=results,
                          total_variations=sum(r['variations'] for r in results),
                          displayed_triangle_parameters=7, path_counterexample=True), indent=2))


if __name__ == '__main__':
    main()
