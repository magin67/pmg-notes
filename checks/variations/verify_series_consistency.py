"""Exact checks of transitions between the Russian variation notes.

Follow a finite conductance change through Greenian coefficients, resistances,
and back to conductances. Check reciprocal determinant factors, n^2 top-grade
normalization, differential inverse maps, and a positive-determinant obstruction.
Standard library only. Run: python checks/variations/verify_series_consistency.py
"""

from fractions import Fraction as Q
from itertools import combinations
import json

from verify_single_edge import determinant, inverse, exterior_grade, forest_sums
from verify_one_greenian_coefficient import principal, centered_inverse, laplacian, coefficients
from verify_one_resistance import multiply, scale, add, identity, resistance, double_center, pair_matrices
from verify_joint_resistances import one_resistance_update


def transpose(a):
    return [list(row) for row in zip(*a)]


def diagonal(entries):
    return [[x if i == j else Q(0) for j in range(len(entries))]
            for i, x in enumerate(entries)]


def round_trip(n, weights, changes):
    pairs = list(combinations(range(n), 2))
    weights = {pair: Q(weights.get(pair, 0)) for pair in pairs}
    final = {pair: c+Q(changes.get(pair, 0)) for pair, c in weights.items()}
    assert min(final.values()) >= 0
    old_l, new_l = laplacian(n, weights), laplacian(n, final)
    old_g, new_g = centered_inverse(old_l), centered_inverse(new_l)
    old_tau, old_f = forest_sums(n, weights)
    new_tau, new_f = forest_sums(n, final)
    assert old_tau > 0 and new_tau > 0
    assert determinant(principal(new_l)) == new_tau
    # All pair columns, including initially absent edges and dependent cycles.
    u = [[Q(i == b)-Q(i == a) for a, b in pairs] for i in range(n)]
    ut = transpose(u)
    dc = diagonal([final[e]-weights[e] for e in pairs])
    gram_r = multiply(multiply(ut, old_g), u)
    forward = add(identity(len(pairs)), multiply(dc, gram_r))
    phi_c = determinant(forward)
    assert phi_c == new_tau/old_tau
    k_c = multiply(inverse(forward), dc)
    gu = multiply(old_g, u)
    assert add(old_g, scale(-1, multiply(multiply(gu, k_c), transpose(gu)))) == new_g
    # Canonical Greenian increments are generally signed even for positive graphs.
    dg = add(new_g, scale(-1, old_g))
    gamma = coefficients(dg)
    assert laplacian(n, gamma) == dg
    dg_diag = diagonal([gamma[e] for e in pairs])
    gram_l = multiply(multiply(ut, old_l), u)
    reverse = add(identity(len(pairs)), multiply(dg_diag, gram_l))
    phi_g = determinant(reverse)
    assert phi_g*phi_c == 1
    k_g = multiply(inverse(reverse), dg_diag)
    lu = multiply(old_l, u)
    recovered = add(old_l, scale(-1, multiply(multiply(lu, k_g), transpose(lu))))
    assert recovered == new_l
    # The two top coefficients use the same fixed form T_n.
    sigma0, sigma1 = determinant(principal(old_g)), determinant(principal(new_g))
    assert n*n*old_tau*sigma0 == n*n*new_tau*sigma1 == 1
    assert sigma1/sigma0 == phi_g
    for gr, sigma in ((old_g, sigma0), (new_g, sigma1)):
        assert exterior_grade(n, coefficients(gr), n-1) == [[sigma]]
    # Prescribe the full resistance increment and solve the finite matrix equation.
    old_r, new_r = resistance(old_g), resistance(new_g)
    dr = add(new_r, scale(-1, old_r))
    assert double_center(dr) == dg
    for a, b in pairs:
        assert old_r[a][b] == old_f[a, b]/old_tau
        assert new_r[a][b] == new_f[a, b]/new_tau
    a = add(identity(n), scale(-Q(1, 2), multiply(dr, old_l)))
    assert determinant(a) == phi_g
    k_r = multiply(inverse(a), scale(Q(1, 2), dr))
    assert k_r == transpose(k_r)
    assert add(old_l, multiply(multiply(old_l, k_r), old_l)) == new_l
    assert multiply(old_l, inverse(a)) == new_l
    dl = add(new_l, scale(-1, old_l))
    assert dl == scale(Q(1, 2), multiply(multiply(new_l, dr), old_l))
    assert dl == scale(Q(1, 2), multiply(multiply(old_l, dr), new_l))
    # Differentiate the same conductance direction, then apply the inverse Jacobian.
    delta_c = [[Q(changes.get(e, 0))] for e in pairs]
    tangent_l = laplacian(n, changes)
    tangent_g = scale(-1, multiply(multiply(old_g, tangent_l), old_g))
    tangent_r = resistance(tangent_g)
    _, sensitivity, quadric = pair_matrices(old_l, old_g)
    tangent_column = [[tangent_r[a][b]] for a, b in pairs]
    assert tangent_column == scale(-1, multiply(sensitivity, delta_c))
    assert scale(-1, multiply(quadric, tangent_column)) == delta_c
    assert multiply(sensitivity, quadric) == multiply(quadric, sensitivity) == identity(len(pairs))
    return any(value < 0 for value in gamma.values())


def factor_is_not_nilpotent():
    n, t = 4, Q(2, 3)
    v = [Q(-1), Q(1), Q(0)]
    square = exterior_grade(n, {}, 2, (v, v))
    assert square == [[0]*3 for _ in range(3)]
    for grade in range(n):
        result = add(exterior_grade(n, {}, grade),
            scale(2*t, exterior_grade(n, {}, grade, (v,))),
            scale(t*t, exterior_grade(n, {}, grade, (v, v))))
        assert result == exterior_grade(n, {(0, 1): 2*t}, grade)
    assert exterior_grade(n, {(0, 1): 2*t}, 0) == [[1]]


def obstructions():
    # A positive determinant does not imply positivity with several directions.
    l = laplacian(3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)})
    g = centered_inverse(l)
    negative_g = scale(-1, g)
    assert determinant(principal(negative_g))/determinant(principal(g)) == 1
    assert negative_g[0][0] < 0 and centered_inverse(negative_g) == scale(-1, l)
    # Locality is an algebraic support statement; it need not preserve signs.
    path = laplacian(4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)})
    new_path, phi = one_resistance_update(path, 1, 2, Q(1, 2))
    assert phi > 0 and -new_path[0][3] == -Q(5, 21)


def main():
    graphs = [
        (2, {(0, 1): Q(3, 2)}),
        (3, {(0, 1): Q(2), (0, 2): Q(3), (1, 2): Q(5)}),
        (4, {(0, 1): Q(1), (1, 2): Q(2), (2, 3): Q(3)}),
        (4, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)})]
    cases = signed_gamma = 0
    for n, weights in graphs:
        existing = list(weights)
        changes = [{}, {existing[0]: weights[existing[0]]/3},
                   {e: -c/4 for e, c in weights.items()}]
        if n > 2:
            changes.append({existing[0]: weights[existing[0]]/2,
                            existing[-1]: -weights[existing[-1]]/3})
        absent = [e for e in combinations(range(n), 2) if e not in weights]
        if absent:
            changes.append({absent[0]: Q(2, 5)})
        for change in changes:
            signed_gamma += round_trip(n, weights, change)
            cases += 1
    factor_is_not_nilpotent()
    obstructions()
    print(json.dumps(dict(graphs=len(graphs), finite_round_trips=cases,
        signed_greenian_increment_cases=signed_gamma,
        factor_square_checked=True, sign_obstructions_checked=True), indent=2))


if __name__ == '__main__':
    main()
