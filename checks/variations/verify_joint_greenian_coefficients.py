"""Exact checks for joint Greenian-coefficient variations; standard library.

Run: python checks/variations/verify_joint_greenian_coefficients.py
Compare exterior coefficients, dual contraction, centered inversion,
spanning-tree enumeration, two-direction formulas, and both sequential orders.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
import json

from verify_single_edge import determinant, inverse, exterior_grade, forest_sums
from verify_one_greenian_coefficient import (
    matvec, pairing, rank_update, principal, centered_inverse, laplacian,
    coefficients, compound, delete_from_top,
)


def vector(n, edge):
    i, j = edge
    return [Q(k == j)-Q(k == i) for k in range(n)]


def subsets(size):
    return [s for k in range(size+1) for s in combinations(range(size), k)]


def positive(a):
    """Sylvester's criterion on a full-rank vertex-coordinate section."""
    return all(determinant([row[:k] for row in a[:k]]) > 0 for k in range(1, len(a)))


def setup(n, weights):
    L = laplacian(n, weights)
    Gr = centered_inverse(L)
    tau = forest_sums(n, weights)[0]
    assert determinant(principal(L)) == tau > 0
    gamma = coefficients(Gr)
    grades = [exterior_grade(n, gamma, k) for k in range(n)]
    assert grades[-1] == [[Q(1, n*n)/tau]]
    return n, L, Gr, tau, gamma, grades, inverse(principal(L))


def prepare(base, directions):
    n, L, Gr, tau, gamma, grades, dual = base
    vectors = [list(map(Q, u)) for u in directions]
    assert all(sum(u) == 0 for u in vectors)
    G = [[pairing(u, L, v) for v in vectors] for u in vectors]
    B = [matvec(L, u) for u in vectors]
    selections = subsets(len(vectors))
    contributions = {
        s: [exterior_grade(n, gamma, k, tuple(vectors[i][:-1] for i in s))
            for k in range(n)] for s in selections
    }
    minors = {s: determinant([[G[i][j] for j in s] for i in s]) for s in selections}
    return vectors, G, B, selections, contributions, minors


def verify(base, prepared, changes):
    n, L, Gr, tau, gamma, grades, dual = base
    vectors, G, B, selections, contributions, minors = prepared
    m = len(vectors)
    changes = list(map(Q, changes))
    products = {s: prod((changes[i] for i in s), start=Q(1)) for s in selections}
    H = [[Q(i == j)+changes[i]*G[i][j] for j in range(m)] for i in range(m)]
    phi = sum(products[s]*minors[s] for s in selections)
    assert phi == determinant(H)
    new_Gr = Gr
    new_dual = dual
    for u, t in zip(vectors, changes):
        new_Gr = rank_update(new_Gr, t, u)
        new_dual = rank_update(new_dual, t, [u[i]-u[-1] for i in range(n-1)])
    new_gamma = coefficients(new_Gr)
    sigma = Q(1, n*n)/tau
    new_sigma = determinant(principal(new_Gr))
    assert new_sigma == sigma*phi
    assert determinant(new_dual) == n*n*new_sigma
    for k in range(n):
        result = [[Q(0) for _ in row] for row in grades[k]]
        for s in selections:
            for i in range(len(result)):
                for j in range(len(result)):
                    result[i][j] += products[s]*contributions[s][k][i][j]
        assert result == exterior_grade(n, new_gamma, k)
    pd = positive(new_Gr)
    # I + sqrt(G) D sqrt(G) is symmetric and has the characteristic
    # polynomial of H. Its real eigenvalues are positive exactly when all
    # elementary symmetric coefficients are positive (Descartes' rule).
    positive_symmetric_criterion = all(
        sum(determinant([[H[i][j] for j in s] for i in s])
            for s in combinations(range(m), k)) > 0 for k in range(1, m+1))
    assert pd == positive_symmetric_criterion
    if m == 2:
        s, t = changes
        qu, qv, g = G[0][0], G[1][1], G[0][1]
        assert phi == 1+s*qu+t*qv+s*t*(qu*qv-g*g)
        assert pd == (phi > 0 and 2+s*qu+t*qv > 0)
    stats = dict(singular=not bool(phi), positive_definite=pd,
                 positive_determinant_not_positive_definite=bool(phi > 0 and not pd),
                 nonnegative_graph=False, sequential_orders=0, singular_intermediates=0)
    if not phi:
        assert not pd
        return stats
    new_L = centered_inverse(new_Gr)
    new_tau = determinant(principal(new_L))
    new_c = coefficients(new_L)
    assert new_tau == tau/phi == forest_sums(n, new_c)[0]
    Hinv = inverse(H)
    K = [[Hinv[i][j]*changes[j] for j in range(m)] for i in range(m)]
    assert K == [list(row) for row in zip(*K)]
    for i in range(n):
        for j in range(n):
            correction = sum(B[a][i]*K[a][b]*B[b][j] for a in range(m) for b in range(m))
            assert new_L[i][j] == L[i][j]-correction
            if m == 2:
                x, y = B
                explicit = (s*(1+t*qv)*x[i]*x[j]+t*(1+s*qu)*y[i]*y[j]
                            -s*t*g*(x[i]*y[j]+y[i]*x[j]))/phi
                assert correction == explicit
    for k in range(n):
        restored = [[new_tau*x for x in row] for row in delete_from_top(new_dual, k)]
        assert restored == compound(principal(new_L), n-1-k)
    stats['nonnegative_graph'] = all(c >= 0 for c in new_c.values())
    if stats['nonnegative_graph']:
        assert pd
    if m == 2:
        for first, second in ((0, 1), (1, 0)):
            a, b = changes[first], changes[second]
            u, v = vectors[first], vectors[second]
            x, y = B[first], B[second]
            A = 1+a*G[first][first]
            if not A:
                stats['singular_intermediates'] += 1
                continue
            mid_Gr = rank_update(Gr, a, u)
            mid_L = centered_inverse(mid_Gr)
            q2 = G[second][second]-a*g*g/A
            y2 = [yi-a*g*xi/A for xi, yi in zip(x, y)]
            assert q2 == pairing(v, mid_L, v)
            assert y2 == matvec(mid_L, v)
            assert A*(1+b*q2) == phi
            assert tau/A/(1+b*q2) == new_tau
            for i in range(n):
                for j in range(n):
                    assert new_L[i][j] == L[i][j]-a*x[i]*x[j]/A-b*y2[i]*y2[j]/(1+b*q2)
            stats['sequential_orders'] += 1
    return stats


def check_two(name, n, weights):
    base = setup(n, weights)
    edges = list(combinations(range(n), 2))
    totals = dict(graph=name, cases=0, singular=0, positive_definite=0,
                  positive_determinant_not_positive_definite=0,
                  nonnegative_graph=0, sequential_orders=0, singular_intermediates=0)
    for edges2 in combinations(edges, 2):
        prepared = prepare(base, [vector(n, e) for e in edges2])
        qu, qv = prepared[1][0][0], prepared[1][1][1]
        for s, t in product((Q(0),1/qu,-1/(2*qu),-1/qu,-2/qu),
                            (Q(0),1/qv,-1/(2*qv),-1/qv,-2/qv)):
            result = verify(base, prepared, (s, t))
            totals['cases'] += 1
            for key, value in result.items():
                totals[key] += int(value)
    return totals


def main():
    triangle = {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}
    examples = [
        ('unit_triangle', 3, triangle),
        ('weighted_triangle', 3, {(0, 1): Q(2), (0, 2): Q(5), (1, 2): Q(3)}),
        ('unit_P4', 4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}),
        ('weighted_C4', 4, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)}),
    ]
    results = [check_two(*g) for g in examples]
    base = setup(3, triangle)
    u, v = vector(3, (0, 1)), vector(3, (0, 2))
    prepared = prepare(base, (u, v))
    parameters = (Q(-1), Q(-1, 6), Q(0), Q(1, 6), Q(1, 3))
    for s, t in product(parameters, repeat=2):
        verify(base, prepared, (s, t))
        phi = 1+6*s+6*t+27*s*t
        if not phi:
            continue
        updated = rank_update(rank_update(base[2], s, u), t, v)
        expected = {(0, 1): (1-3*s+6*t)/phi, (0, 2): (1+6*s-3*t)/phi,
                    (1, 2): (1+6*s+6*t)/phi}
        assert coefficients(centered_inverse(updated)) == expected
        assert forest_sums(3, expected)[0] == 3/phi
    multiple_cases = 0
    for _, n, weights in examples:
        base = setup(n, weights)
        edges = list(combinations(range(n), 2))
        prepared = prepare(base, [vector(n, e) for e in edges])
        choices = [
            [Q(0)]*len(edges), [Q(1, 10)]*len(edges),
            [Q(0) if i % 2 else Q(1, 10) for i in range(len(edges))],
            [(-1 if i % 2 else 1)/(2*prepared[1][i][i]) for i in range(len(edges))],
            [-base[4][e] for e in edges],
        ]
        for changes in choices:
            verify(base, prepared, changes)
            multiple_cases += 1
    base = setup(3, triangle)
    prepared = prepare(base, [vector(3, e) for e in combinations(range(3), 2)])
    for t in (Q(-1, 9), Q(0), Q(1, 9), Q(1, 3)):
        verify(base, prepared, [t]*3)
        changed = base[2]
        for w in prepared[0]: changed = rank_update(changed, t, w)
        phi = determinant(principal(changed))*27
        assert phi == (1+9*t)**2
        if phi: assert all(c == 1/(1+9*t) for c in coefficients(centered_inverse(changed)).values())
        multiple_cases += 1
    # Dependent directions with opposite changes cancel exactly.
    verify(base, prepare(base, (u, [2*x for x in u])), [Q(1, 3), Q(-1, 12)])
    # Approach a singular first update from its positive side.
    verify(base, prepare(base, (u, v)), [-Q(99, 100)/6, Q(0)])
    edge_base = setup(2, {(0, 1): Q(3, 2)})
    verify(edge_base, prepare(edge_base, (vector(2, (0, 1)),)), [Q(1, 5)])
    multiple_cases += 3
    assert sum(r['positive_determinant_not_positive_definite'] for r in results) > 0
    assert sum(r['singular_intermediates'] for r in results) > 0
    print(json.dumps(dict(status='passed', graphs=results,
                          total_two_direction_cases=sum(r['cases'] for r in results),
                          displayed_triangle_parameters=25, additional_cases=multiple_cases), indent=2))


if __name__ == '__main__':
    main()
