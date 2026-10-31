"""Exact checks for 'One Greenian coefficient'; standard library only.

Compare exterior factors, dual contraction, direct centered inversion, and
tree enumeration. Singular forms are tested without assigning an inverse.
Run: python checks/variations/verify_one_greenian_coefficient.py
"""

from fractions import Fraction as Q
from itertools import combinations
import json

from verify_single_edge import determinant, inverse, exterior_grade, forest_sums


def matvec(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def pairing(v, a, w):
    return sum(x*y for x, y in zip(v, matvec(a, w)))


def rank_update(a, t, v):
    return [[x + t*v[i]*v[j] for j, x in enumerate(row)] for i, row in enumerate(a)]


def principal(a):
    return [row[:-1] for row in a[:-1]]


def centered_inverse(a):
    n = len(a)
    shifted = [[x+Q(1, n) for x in row] for row in a]
    return [[x-Q(1, n) for x in row] for row in inverse(shifted)]


def laplacian(n, weights):
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for (i, j), c in weights.items():
        a[i][i] += c
        a[j][j] += c
        a[i][j] -= c
        a[j][i] -= c
    return a


def coefficients(a):
    return {(i, j): -a[i][j] for i, j in combinations(range(len(a)), 2)}


def compound(a, k):
    indices = list(combinations(range(len(a)), k))
    return [[determinant([[a[i][j] for j in J] for i in I]) for J in indices]
            for I in indices]


def delete_from_top(a, k):
    """Apply dual grade exp(a)_k to the fixed squared volume form."""
    d = len(a)
    indices = list(combinations(range(d), k))
    remainder = list(combinations(range(d), d-k))
    lookup = {I: i for i, I in enumerate(remainder)}
    result = [[Q(0) for _ in remainder] for _ in remainder]
    for I in indices:
        Ic = tuple(i for i in range(d) if i not in I)
        si = (-1)**(sum(I)-k*(k-1)//2)
        for J in indices:
            Jc = tuple(j for j in range(d) if j not in J)
            sj = (-1)**(sum(J)-k*(k-1)//2)
            result[lookup[Ic]][lookup[Jc]] = si*sj*determinant(
                [[a[i][j] for j in J] for i in I])
    return result


def potential(n, gamma, v, w, extra=()):
    """Extract a mixed top coefficient using polarization of exterior forms."""
    def quadratic(x):
        return exterior_grade(n, gamma, n-1, (x,) + extra)[0][0]
    return (quadratic([a+b for a, b in zip(v, w)])-quadratic(v)-quadratic(w))/2


def verify_graph(name, n, weights):
    L = laplacian(n, weights)
    Gr = centered_inverse(L)
    gamma = coefficients(Gr)
    tau = determinant(principal(L))
    assert tau == forest_sums(n, weights)[0] > 0
    sigma = Q(1, n*n)/tau
    assert determinant(principal(Gr)) == sigma
    grades = [exterior_grade(n, gamma, r) for r in range(n)]
    assert grades[-1] == [[sigma]]
    dual = inverse(principal(L))
    centers = [[Q(i == j)-Q(1, n) for j in range(n-1)] for i in range(n)]
    directions = [([Q(i == l)-Q(i == k) for i in range(n)], (k, l))
                  for k, l in combinations(range(n), 2)]
    if n >= 3:
        directions.append(([Q(1), Q(2), Q(-3)] + [Q(0)]*(n-3), None))
    cases = singular = graph_cases = positive_signed = indefinite = 0
    for u, edge in directions:
        b = matvec(L, u)
        q = sum(x*y for x, y in zip(u, b))
        assert q > 0
        if edge:
            k, l = edge
            assert q == L[k][k]+L[l][l]-2*L[k][l]
        extra = [exterior_grade(n, gamma, r, (u[:-1],)) for r in range(n)]
        assert extra[-1] == [[sigma*q]]
        for i in range(n):
            for j in range(n):
                assert potential(n, gamma, centers[i], centers[j]) == sigma*L[i][j]
                assert potential(n, gamma, centers[i], centers[j], (u[:-1],)) == (
                    sigma*(L[i][j]*q-b[i]*b[j]))
        for t in (Q(0), 1/(5*q), 1/q, -1/(2*q), -Q(99, 100)/q, -1/q, -2/q, Q(1)):
            denominator = 1+t*q
            new_Gr = rank_update(Gr, t, u)
            new_gamma = coefficients(new_Gr)
            if edge:
                for pair in gamma:
                    assert new_gamma[pair]-gamma[pair] == (t if pair == edge else 0)
            for r in range(n):
                expected = [[x+t*y for x, y in zip(row, add)]
                            for row, add in zip(grades[r], extra[r])]
                assert exterior_grade(n, new_gamma, r) == expected
            new_sigma = determinant(principal(new_Gr))
            assert new_sigma == sigma*denominator
            z = [u[i]-u[-1] for i in range(n-1)]
            new_dual = rank_update(dual, t, z)
            assert determinant(new_dual) == n*n*new_sigma
            for i, j in combinations(range(n), 2):
                old_r = Gr[i][i]+Gr[j][j]-2*Gr[i][j]
                new_r = new_Gr[i][i]+new_Gr[j][j]-2*new_Gr[i][j]
                assert new_r-old_r == t*(u[i]-u[j])**2
            cases += 1
            if not denominator:
                assert matvec(new_Gr, b) == [0]*n
                assert any(b)
                singular += 1
                continue
            new_L = centered_inverse(new_Gr)
            assert new_L == rank_update(L, -t/denominator, b)
            new_c = coefficients(new_L)
            new_tau = determinant(principal(new_L))
            assert new_tau == tau/denominator == forest_sums(n, new_c)[0]
            for i, j in combinations(range(n), 2):
                assert new_c[(i, j)] == weights.get((i, j), 0)+t*b[i]*b[j]/denominator
                assert potential(n, new_gamma, centers[i], centers[j])/new_sigma == new_L[i][j]
            for k in range(n):
                restored = [[new_tau*x for x in row] for row in delete_from_top(new_dual, k)]
                assert restored == compound(principal(new_L), n-1-k)
            if denominator > 0:
                for k in range(1, n):
                    assert determinant([row[:k] for row in new_Gr[:k]]) > 0
                nonnegative = all(c >= 0 for c in new_c.values())
                inequalities = all(weights.get((i, j), 0)+t*(weights.get((i, j), 0)*q+b[i]*b[j]) >= 0
                                   for i, j in combinations(range(n), 2))
                assert nonnegative == inequalities
                if nonnegative: graph_cases += 1
                else: positive_signed += 1
            else:
                assert new_sigma < 0
                indefinite += 1
    return dict(graph=name, cases=cases, singular=singular, nonnegative_graphs=graph_cases,
                positive_definite_with_negative_conductances=positive_signed, indefinite=indefinite)


def verify_displayed_path():
    n = 4
    L = laplacian(n, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)})
    Gr = centered_inverse(L)
    assert -Gr[0][1] == -Q(1, 8)
    assert any(c < 0 for c in coefficients(Gr).values())
    u = [Q(-1), Q(1), Q(0), Q(0)]
    samples = (Q(-19, 100), Q(-1, 10), Q(0), Q(1, 5), Q(1), Q(2))
    for t in samples:
        new_Gr = rank_update(Gr, t, u)
        new_c = coefficients(centered_inverse(new_Gr))
        den = 1+5*t
        expected = {(0, 1): (1-t)/den, (1, 2): (1+2*t)/den,
                    (0, 2): 2*t/den, (2, 3): Q(1), (0, 3): Q(0), (1, 3): Q(0)}
        assert new_c == expected
        assert forest_sums(n, new_c)[0] == 1/den
        assert all(c >= 0 for c in new_c.values()) == (0 <= t <= 1)
    altered = rank_update(Gr, Q(1, 5), u)
    assert -altered[0][1] == Q(3, 40)
    assert coefficients(centered_inverse(altered)) == {
        (0, 1): Q(2, 5), (1, 2): Q(7, 10), (0, 2): Q(1, 5),
        (2, 3): Q(1), (0, 3): Q(0), (1, 3): Q(0)}


def main():
    graphs = [
        ('weighted_edge', 2, {(0, 1): Q(3, 2)}),
        ('unit_triangle', 3, {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}),
        ('weighted_triangle', 3, {(0, 1): Q(2), (0, 2): Q(5), (1, 2): Q(3)}),
        ('unit_P4', 4, {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}),
        ('weighted_C4', 4, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(5), (0, 3): Q(7)}),
    ]
    results = [verify_graph(*g) for g in graphs]
    verify_displayed_path()
    print(json.dumps(dict(status='passed', graphs=results,
                          total_variations=sum(r['cases'] for r in results),
                          displayed_path_parameters=6), indent=2))


if __name__ == '__main__':
    main()
