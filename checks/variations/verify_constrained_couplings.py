"""Exact rational checks for variations with constrained conductances.

Verify the triangular prism, its feasible family, Kron reduction, finite edge
updates, full resistance recovery, tree/forest sums, and restricted Jacobians.
Run: python checks/variations/verify_constrained_couplings.py
"""

from fractions import Fraction as Q
from itertools import combinations
import json

from verify_single_edge import determinant, inverse, forest_sums
from verify_one_greenian_coefficient import principal, centered_inverse, laplacian
from verify_one_resistance import multiply, scale, add, block, identity, resistance, double_center


P = [0, 1, 2]
INTERIOR = [3, 4, 5]
V = [(3, 4), (3, 5), (4, 5), (0, 3), (1, 4), (2, 5)]
FIXED = [(0, 1), (0, 2), (1, 2)]
Z = set(combinations(range(6), 2)) - set(V) - set(FIXED)
BASE = {e: Q(1) for e in FIXED + V}


def transpose(a):
    return [list(row) for row in zip(*a)]


def zeros(n, m=None):
    return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]


def column(v):
    return [[x] for x in v]


def vector(n, edge):
    i, j = edge
    return [Q(k == j)-Q(k == i) for k in range(n)]


def kron(L, boundary):
    interior = [i for i in range(len(L)) if i not in boundary]
    if not interior:
        return L
    return add(block(L, boundary, boundary), scale(-1, multiply(multiply(
        block(L, boundary, interior), inverse(block(L, interior, interior))),
        block(L, interior, boundary))))


def target(k):
    r = Q(8, 15)
    return [[Q(0), k*r, r], [k*r, Q(0), r], [r, r, Q(0)]]


def added_weights(k):
    a = (4*k*k-31*k+30)/(4*k*(4-k))
    b = (4*k-1)/(4*(4-k))
    return a, b


def choose_g(k):
    a, b = added_weights(k)
    assert a > 0 and b >= 0
    return 1+max(2*a+b, 3*b, b*(2*a+b)/a)


def construct(k, g):
    a, b = added_weights(k)
    assert g > max(2*a+b, 3*b)
    nu = g*b/(g-3*b)
    x = g*(a*g-b*(2*a+b))/((g-2*a-b)*(g-3*b))
    w = dict(BASE)
    w.update({(3, 4): x, (3, 5): nu, (4, 5): nu,
              (0, 3): g, (1, 4): g, (2, 5): g})
    return w


def verify_finite_formula(new_weights):
    L0 = laplacian(6, BASE)
    Gr0 = centered_inverse(L0)
    R0 = resistance(Gr0)
    U = transpose([vector(6, e) for e in V])
    G = multiply(multiply(transpose(U), Gr0), U)
    t = [new_weights[e]-BASE[e] for e in V]
    D = [[t[i] if i == j else Q(0) for j in range(len(V))] for i in range(len(V))]
    A = add(identity(len(V)), multiply(D, G))
    phi = determinant(A)
    assert phi > 0
    K = multiply(inverse(A), D)
    assert K == transpose(K)
    L = laplacian(6, new_weights)
    Gr = centered_inverse(L)
    GU = multiply(Gr0, U)
    assert Gr == add(Gr0, scale(-1, multiply(multiply(GU, K), transpose(GU))))
    R = resistance(Gr)
    assert determinant(principal(L)) == determinant(principal(L0))*phi
    for i, j in combinations(range(6), 2):
        z = multiply(multiply(transpose(U), Gr0), column(vector(6, (i, j))))
        delta = multiply(multiply(transpose(z), K), z)[0][0]
        assert R[i][j] == R0[i][j]-delta
    return phi


def verify_prism(k, g):
    weights = construct(k, g)
    assert all(c >= 0 for c in weights.values())
    assert all(weights.get(e, Q(0)) == 0 for e in Z)
    assert all(weights[e] == 1 for e in FIXED)
    L = laplacian(6, weights)
    Gr = centered_inverse(L)
    R = resistance(Gr)
    assert block(R, P, P) == target(k)
    reduced = kron(L, P)
    expected = laplacian(3, {(0, 1): 15*(2-k)/(4*k*(4-k)),
                           (0, 2): 15/(4*(4-k)), (1, 2): 15/(4*(4-k))})
    assert reduced == expected == centered_inverse(double_center(target(k)))
    assert resistance(centered_inverse(reduced)) == target(k)
    # Elimination preserves boundary resistances, not the full Greenian block.
    assert block(Gr, P, P) != centered_inverse(reduced)
    tau, forests = forest_sums(6, weights)
    assert tau == determinant(principal(L)) > 0
    for i, j in combinations(range(6), 2):
        assert forests[i, j]/tau == R[i][j]
    assert tau == determinant(block(L, INTERIOR, INTERIOR))*determinant(principal(reduced))
    verify_finite_formula(weights)
    return weights, tau


def verify_boundary_obstruction():
    # Exact cofactor identities used to exclude a = 0, b > 0 at the upper end.
    examples = [((1, 1, 1), (1, 1, 1)), ((2, 3, 5), (0, 1, 2)),
                ((2, 3, 5), (0, 0, 2)), ((0, 3, 5), (1, 1, 2)),
                ((Q(1, 2), Q(2, 3), Q(3, 4)), (Q(1, 5), Q(2, 5), Q(0)))]
    for gs, xyz in examples:
        g1, g2, g3 = map(Q, gs)
        x, y, z = map(Q, xyz)
        H = laplacian(3, {(0, 1): x, (0, 2): y, (1, 2): z})
        D = [[gs[i] if i == j else Q(0) for j in range(3)] for i in range(3)]
        M = add(D, H)
        det = determinant(M)
        assert det > 0
        C = add(D, scale(-1, multiply(multiply(D, inverse(M)), D)))
        assert -C[0][1] == g1*g2*(x*(g3+y+z)+y*z)/det
        assert -C[0][2] == g1*g3*(y*(g2+x+z)+x*z)/det
        assert -C[1][2] == g2*g3*(z*(g1+x+y)+x*y)/det
    # Necessary inequalities fail outside the asserted interval.
    for k in (Q(1, 5), Q(8, 7), Q(3, 2), Q(2)):
        a, b = added_weights(k)
        assert a < 0 or b < 0
    assert 15*(2-Q(2))/(4*Q(2)*(4-Q(2))) == 0
    polynomial = lambda k: 4*k*k-31*k+30
    lo, hi = Q(1133535, 1000000), Q(1133536, 1000000)
    assert polynomial(lo) > 0 > polynomial(hi)
    assert 8*lo < 31 and 8*hi < 31


def verify_jacobian():
    L = laplacian(6, BASE)
    Gr = centered_inverse(L)
    R0 = resistance(Gr)
    boundary_pairs = list(combinations(P, 2))
    U = transpose([vector(6, e) for e in V])
    S = []
    for p in boundary_pairs:
        z = multiply(multiply(transpose(U), Gr), column(vector(6, p)))
        S.append([v[0]**2 for v in z])
    expected = scale(Q(1, 225), [[4, 1, 1, 9, 9, 0],
                                [1, 4, 1, 9, 0, 9], [1, 1, 4, 0, 9, 9]])
    assert S == expected
    assert determinant(block(S, [0, 1, 2], [0, 1, 2])) != 0
    for col, edge in enumerate(V):
        edge_r = R0[edge[0]][edge[1]]
        for t in (Q(1, 10), -Q(1, 4)):
            weights = dict(BASE)
            weights[edge] += t
            R = resistance(centered_inverse(laplacian(6, weights)))
            for row, (i, j) in enumerate(boundary_pairs):
                assert (R[i][j]-R0[i][j])*(1+t*edge_r)/t == -S[row][col]


def verify_free_remote_edge():
    weights = {(i, i+1): Q(1) for i in range(5)}
    L = laplacian(6, weights)
    R = resistance(centered_inverse(L))
    weights[4, 5] = Q(2)
    new_R = resistance(centered_inverse(laplacian(6, weights)))
    assert new_R[0][1] == R[0][1] == 1
    assert new_R[4][5] != R[4][5]


def main():
    initial = laplacian(6, BASE)
    assert block(resistance(centered_inverse(initial)), P, P) == target(Q(1))
    assert determinant(principal(initial)) == 75
    assert kron(initial, P) == laplacian(3, {e: Q(5, 4) for e in combinations(range(3), 2)})
    displayed, tau = verify_prism(Q(9, 8), Q(7))
    assert displayed[3, 4] == 0 and displayed[3, 5] == displayed[4, 5] == Q(7, 20)
    assert tau == Q(7203, 4)
    original, _ = verify_prism(Q(1), Q(1))
    assert original == BASE
    lower, _ = verify_prism(Q(1, 4), Q(24))
    assert lower[3, 4] == 12 and lower[3, 5] == lower[4, 5] == 0
    # Near the original point only the second face needs to vary.
    local, _ = verify_prism(Q(101, 100), Q(1))
    assert all(c > 0 for c in local.values())
    samples = [Q(1, 3), Q(1, 2), Q(3, 4), Q(1), Q(21, 20), Q(11, 10),
               Q(9, 8), Q(113, 100), Q(1133, 1000), Q(11335, 10000), Q(113353, 100000)]
    for k in samples:
        g = choose_g(k)
        for v in (g, g+1):
            weights, _ = verify_prism(k, v)
            assert all(weights[e] > 0 for e in V)
    near = samples[-5:]
    assert all(choose_g(a) < choose_g(b) for a, b in zip(near, near[1:]))
    assert all(added_weights(a)[0] > added_weights(b)[0] > 0 for a, b in zip(near, near[1:]))
    verify_boundary_obstruction()
    verify_jacobian()
    verify_free_remote_edge()
    print(json.dumps(dict(status='passed', exact_prism_realizations=4+2*len(samples),
        cofactor_checks=5, excluded_targets=4, sensitivity_variations=12,
        displayed_spanning_coefficient=str(tau), zero_and_fixed_edges=True,
        near_upper_boundary=True, local_jacobian_rank=3, free_remote_edge=True), indent=2))


if __name__ == '__main__':
    main()
