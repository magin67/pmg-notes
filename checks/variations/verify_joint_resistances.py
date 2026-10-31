"""Exact checks for joint resistance variations; standard library only.

Compare exterior factors, dual deletion, full and reduced linear systems,
centered inversion, signed tree/forest enumeration, and sequential updates.
Run: python checks/variations/verify_joint_resistances.py
"""

from fractions import Fraction as Q
from itertools import combinations
from math import prod
import json

from verify_single_edge import determinant, inverse, exterior_grade, forest_sums
from verify_one_greenian_coefficient import (
    principal, centered_inverse, laplacian, coefficients, compound, delete_from_top,
)
from verify_one_resistance import (
    multiply, scale, add, block, identity, positive, resistance, double_center,
)


def transpose(a):
    return [list(row) for row in zip(*a)]


def zeros(n, m=None):
    return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]


def embed(n, S, F):
    result = zeros(n)
    for a, i in enumerate(S):
        for b, j in enumerate(S):
            result[i][j] = F[a][b]
    return result


def from_pairs(n, changes):
    result = zeros(n)
    for (i, j), value in changes.items():
        result[i][j] = result[j][i] = Q(value)
    return result


def positive_small_criterion(H, F):
    """Rational Gram factor replaces a possibly irrational square root of H.

    H = Z diag(d) Z^T with independent columns and d > 0. The test is
    diag(1/d) - Z^T F Z/2 > 0; zero directions contribute unit eigenvalues.
    """
    remainder = [row[:] for row in H]
    columns, diagonal = [], []
    for i in range(len(H)):
        pivot = remainder[i][i]
        assert pivot >= 0
        if not pivot:
            assert all(x == 0 for x in remainder[i])
            continue
        z = [row[i]/pivot for row in remainder]
        columns.append(z)
        diagonal.append(pivot)
        remainder = add(remainder, scale(-pivot, [[x*y for y in z] for x in z]))
    assert remainder == zeros(len(H))
    if not columns:
        return True
    Z = transpose(columns)
    Dinv = [[(1/d if i == j else Q(0)) for j in range(len(diagonal))]
            for i, d in enumerate(diagonal)]
    test = add(Dinv, scale(-Q(1, 2), multiply(multiply(transpose(Z), F), Z)))
    return positive(test)


def factor_grades(n, gamma, dr):
    factors = []
    for k, l in combinations(range(n), 2):
        rho = dr[k][l]
        if not rho:
            continue
        pk = [Q(i == k)-Q(1, n) for i in range(n-1)]
        pl = [Q(i == l)-Q(1, n) for i in range(n-1)]
        factors.extend([(rho/4, [a-b for a, b in zip(pk, pl)]),
                        (-rho/4, [a+b for a, b in zip(pk, pl)])])
    result = []
    for grade in range(n):
        value = exterior_grade(n, gamma, grade)
        for size in range(1, min(grade, len(factors))+1):
            for chosen in combinations(factors, size):
                weight = prod((t for t, _ in chosen), start=Q(1))
                vectors = tuple(v for _, v in chosen)
                value = add(value, scale(weight, exterior_grade(n, gamma, grade, vectors)))
        result.append(value)
    return result


def one_resistance_update(L, k, l, rho):
    """Use the previous note's explicit scalar formula, not the block formula."""
    n = len(L)
    A, B, C = L[k][k], L[l][l], L[k][l]
    phi = 1-rho*C-rho*rho*(A*B-C*C)/4
    if not phi:
        return None, phi
    eta = 1-rho*C/2
    x, y = [row[k] for row in L], [row[l] for row in L]
    answer = [[L[i][j]+(rho*eta*(x[i]*y[j]+y[i]*x[j])/2
               +rho*rho*(B*x[i]*x[j]+A*y[i]*y[j])/4)/phi
               for j in range(n)] for i in range(n)]
    return answer, phi


def check_case(L, S, F):
    n, r = len(L), len(S)
    assert F == transpose(F) and all(F[i][i] == 0 for i in range(r))
    dr = embed(n, S, F)
    Gr = centered_inverse(L)
    R = resistance(Gr)
    new_R = add(R, dr)
    new_Gr = double_center(new_R)
    H = block(L, S, S)
    B = block(L, list(range(n)), S)
    A = add(identity(r), scale(-Q(1, 2), multiply(F, H)))
    phi = determinant(A)
    full_A = add(identity(n), scale(-Q(1, 2), multiply(dr, L)))
    assert determinant(full_A) == phi
    tau = determinant(principal(L))
    sigma = Q(1, n*n)/tau
    assert determinant(principal(new_Gr)) == sigma*phi
    assert resistance(new_Gr) == new_R
    gamma, new_gamma = coefficients(Gr), coefficients(new_Gr)
    grades = factor_grades(n, gamma, dr)
    for grade in range(n):
        assert grades[grade] == exterior_grade(n, new_gamma, grade)
    assert grades[-1] == [[sigma*phi]]
    # Direct forms and dual forms use distinct coordinate transformations.
    Z = [[Q(i == a)-Q(n-1 == a) for a in S] for i in range(n-1)]
    assert multiply(multiply(transpose(Z), principal(L)), Z) == H
    new_dual = add(inverse(principal(L)), scale(-Q(1, 2),
                   multiply(multiply(Z, F), transpose(Z))))
    assert determinant(new_dual) == n*n*sigma*phi
    is_positive = positive(principal(new_Gr))
    assert positive(new_dual) == is_positive == positive_small_criterion(H, F)
    if r < n:
        assert positive(add(inverse(H), scale(-Q(1, 2), F))) == is_positive
    # Differential formulas, including the spanning coefficient normalization.
    dL = scale(Q(1, 2), multiply(multiply(L, dr), L))
    trace_product = multiply(inverse(principal(L)), principal(dL))
    expected_trace = sum(L[i][j]*dr[i][j] for i, j in combinations(range(n), 2))
    assert sum(trace_product[i][i] for i in range(n-1)) == expected_trace
    for i, j in combinations(range(n), 2):
        assert dL[i][j] == sum((L[i][k]*L[j][l]+L[i][l]*L[j][k])*dr[k][l]/2
                              for k, l in combinations(range(n), 2))
    if not phi:
        assert not determinant(principal(new_Gr))
        return dict(singular=1, positive=0, nonnegative=0, sequential=0, blocked_orders=0)
    K = scale(Q(1, 2), multiply(inverse(A), F))
    assert K == transpose(K) and multiply(A, K) == scale(Q(1, 2), F)
    new_L = add(L, multiply(multiply(B, K), transpose(B)))
    assert new_L == centered_inverse(new_Gr) == multiply(L, inverse(full_A))
    assert new_L == multiply(inverse(transpose(full_A)), L)
    assert new_L == transpose(new_L) and all(sum(row) == 0 for row in new_L)
    X = block(new_L, list(range(n)), S)
    assert multiply(X, A) == B
    assert add(new_L, scale(-1, L)) == scale(Q(1, 2), multiply(multiply(new_L, dr), L))
    assert resistance(centered_inverse(new_L)) == new_R
    new_c = coefficients(new_L)
    new_tau, forests = forest_sums(n, new_c)
    assert new_tau == determinant(principal(new_L)) == tau/phi
    for pair, value in forests.items():
        assert value/new_tau == new_R[pair[0]][pair[1]]
    for grade in range(n):
        restored = scale(new_tau, delete_from_top(new_dual, grade))
        assert restored == compound(principal(new_L), n-1-grade)
    for i, row in enumerate(B):
        if all(x == 0 for x in row):
            assert new_L[i] == L[i]
    changes = [(k, l, dr[k][l]) for k, l in combinations(range(n), 2) if dr[k][l]]
    completed = blocked = 0
    for order in (changes, list(reversed(changes))):
        current, factor = L, Q(1)
        for k, l, rho in order:
            current, next_factor = one_resistance_update(current, k, l, rho)
            if current is None:
                blocked += 1
                break
            factor *= next_factor
        else:
            assert current == new_L and factor == phi
            completed += 1
    return dict(singular=0, positive=int(is_positive),
                nonnegative=int(all(c >= 0 for c in new_c.values())),
                sequential=completed, blocked_orders=blocked)


def graph_cases(L):
    n = len(L)
    R = resistance(centered_inverse(L))
    full = list(range(n))
    cases = [([0], [[Q(0)]])]
    # Include approaching, meeting, and crossing complete degeneration.
    for t in (Q(-2), Q(-1), -Q(99, 100), Q(0), Q(1, 5), Q(2)):
        cases.append((full, scale(t, R)))
    if n >= 3:
        S = [0, 1, 2]
        for a, b in ((Q(1, 6), Q(1, 3)), (Q(1, 3), Q(1, 3)),
                     (Q(-1, 10), Q(1, 5)), (Q(2), Q(2))):
            cases.append((S, from_pairs(3, {(0, 1): a, (0, 2): b})))
        for a in (Q(-1, 10), Q(1, 5)):
            cases.append(([0, 1], from_pairs(2, {(0, 1): a})))
    if n == 4:
        # Disjoint pairs give a rank-four F; adjacent pairs have rank two.
        for a, b in ((Q(1, 10), Q(1, 7)), (Q(1), Q(-1, 3)),
                     (Q(-1, 4), Q(-1, 5))):
            cases.append((full, from_pairs(4, {(0, 1): a, (2, 3): b})))
        cases.append(([1, 2], from_pairs(2, {(0, 1): Q(1, 10)})))
        dense = from_pairs(4, {e: Q((-1)**i*(i+1), 60)
                              for i, e in enumerate(combinations(range(4), 2))})
        cases.extend((full, scale(t, dense)) for t in (Q(1), Q(3)))
    return cases


def verify_graph(name, n, weights):
    L = laplacian(n, weights)
    totals = dict(variations=0, singular=0, positive=0, nonnegative=0,
                  sequential=0, blocked_orders=0)
    for S, F in graph_cases(L):
        result = check_case(L, S, F)
        totals['variations'] += 1
        for key, value in result.items():
            totals[key] += value
    return dict(graph=name, **totals)


def verify_displayed_examples():
    L = laplacian(3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)})
    R = resistance(centered_inverse(L))
    samples = ((Q(1, 3), Q(1, 3)), (Q(1, 3), Q(1, 6)),
               (Q(0), Q(1, 3)), (Q(2), Q(2)), (Q(-1), Q(-1)))
    for a, b in samples:
        F = from_pairs(3, {(0, 1): a, (0, 2): b})
        phi = 1+a+b-Q(3, 4)*(a-b)**2
        assert determinant(add(identity(3), scale(-Q(1, 2), multiply(F, L)))) == phi
        new_L = centered_inverse(double_center(add(R, F)))
        assert determinant(principal(new_L)) == 3/phi
        assert coefficients(new_L) == {(0, 1): (1-3*a/2+3*b/2)/phi,
             (0, 2): (1+3*a/2-3*b/2)/phi, (1, 2): (1+3*a/2+3*b/2)/phi}
    middle, phi1 = one_resistance_update(L, 0, 1, Q(1, 3))
    final, phi2 = one_resistance_update(middle, 0, 2, Q(1, 3))
    assert phi1 == Q(5, 4) and phi2 == Q(4, 3)
    assert coefficients(final) == {(0, 1): Q(3, 5), (0, 2): Q(3, 5), (1, 2): Q(6, 5)}
    assert determinant(principal(final)) == Q(9, 5)
    # Both one-coordinate orders meet a singular intermediate form.
    assert one_resistance_update(L, 0, 1, Q(2))[0] is None
    assert one_resistance_update(L, 0, 2, Q(2))[0] is None
    # A valid simultaneous change with a divergent simple fixed-point iteration.
    F = scale(2, R)
    T = scale(Q(1, 2), multiply(F, L))
    J = [[Q(i == j)-Q(1, 3) for j in range(3)] for i in range(3)]
    assert T == scale(-2, J)
    exact = scale(Q(1, 3), L)
    X = L
    initial_error = add(X, scale(-1, exact))
    for m in range(1, 7):
        X = add(L, multiply(X, T))
        assert add(X, scale(-1, exact)) == scale(Q((-2)**m), initial_error)
    # Exact locality allows an edge whose endpoints both lie outside S.
    path = laplacian(4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)})
    new_path, _ = one_resistance_update(path, 1, 2, Q(1, 10))
    assert path[0][3] == 0 and new_path[0][3] != 0


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
        total_variations=sum(x['variations'] for x in results),
        triangle_parameters=5, divergent_iteration=True, locality=True), indent=2))


if __name__ == '__main__':
    main()
