"""Exact checks for the PMG note on normalized forest power sums.

Run from the repository root:
    python checks/matroid/verify_forest_power_sums.py

Only the Python standard library is required. Forest enumeration, formal-log
expansion and rational matrix calculations are separate verification routes.
These finite checks supplement, rather than replace, the proofs in the note.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations


ORDER = 8


def multiply(a, b, order=None):
    size = len(a) + len(b) - 1
    if order is not None:
        size = min(size, order + 1)
    out = [Q(0)] * size
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j < size:
                out[i + j] += ai * bj
    return out


def forest_coefficients(n, edges):
    """Enumerate edge subsets, keeping parallel edges distinct."""
    ordinary = [Q(0)] * n
    rooted = [Q(0)] * n
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def root(v):
            while v != parent[v]:
                v = parent[v]
            return v

        weight = Q(1)
        grade = 0
        for i, (a, b, conductance) in enumerate(edges):
            if not (mask >> i) & 1:
                continue
            ra, rb = root(a), root(b)
            if ra == rb:
                break
            parent[ra] = rb
            weight *= conductance
            grade += 1
        else:
            root_choices = 1
            for size in Counter(root(v) for v in range(n)).values():
                root_choices *= size
            ordinary[grade] += weight
            rooted[grade] += weight * root_choices
    return ordinary, rooted


def normalized(f):
    assert f[-1] > 0
    return [x / f[-1] for x in reversed(f)]


def newton(alpha, order=ORDER):
    power = [Q(0)]
    for m in range(1, order + 1):
        rhs = m * (alpha[m] if m < len(alpha) else Q(0))
        rhs -= sum(
            (-1) ** (j - 1) * alpha[m - j] * power[j]
            for j in range(1, m)
            if m - j < len(alpha)
        )
        power.append((-1) ** (m - 1) * rhs)
    return power[1:]


def direct_log(alpha, order=ORDER):
    """Expand sum (-1)^(q-1) (Phi-1)^q/q, without Newton recurrence."""
    v = list(alpha)
    v[0] -= 1
    log_coeff = [Q(0)] * (order + 1)
    v_power = [Q(1)]
    for q in range(1, order + 1):
        v_power = multiply(v_power, v, order)
        for k, coeff in enumerate(v_power):
            log_coeff[k] += Q((-1) ** (q - 1), q) * coeff
    return [(-1) ** (m - 1) * m * log_coeff[m]
            for m in range(1, order + 1)]


def recover_alpha(power, degree):
    alpha = [Q(1)]
    for m in range(1, degree + 1):
        alpha.append(sum(
            (-1) ** (j - 1) * alpha[m - j] * power[j - 1]
            for j in range(1, m + 1)
        ) / m)
    return alpha


def laplacian(n, edges):
    matrix = [[Q(0) for _ in range(n)] for _ in range(n)]
    for a, b, c in edges:
        matrix[a][a] += c
        matrix[b][b] += c
        matrix[a][b] -= c
        matrix[b][a] -= c
    return matrix


def inverse(matrix):
    n = len(matrix)
    a = [list(row) + [Q(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        divisor = a[k][k]
        a[k] = [x / divisor for x in a[k]]
        for i in range(n):
            if i != k:
                factor = a[i][k]
                a[i] = [x - factor * y for x, y in zip(a[i], a[k])]
    return [row[n:] for row in a]


def greenian(matrix):
    n = len(matrix)
    shift = Q(1, n)
    inv = inverse([[x + shift for x in row] for row in matrix])
    return [[x - shift for x in row] for row in inv]


def determinant(matrix):
    if not matrix:
        return Q(1)
    a = [list(row) for row in matrix]
    det = Q(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        divisor = a[k][k]
        det *= divisor
        for i in range(k + 1, len(a)):
            factor = a[i][k] / divisor
            for j in range(k + 1, len(a)):
                a[i][j] -= factor * a[k][j]
    return det


def determinant_polynomial(matrix):
    """Coefficients of det(I+t A), from principal minors."""
    n = len(matrix)
    coeff = [Q(0)] * (n + 1)
    for size in range(n + 1):
        for subset in combinations(range(n), size):
            coeff[size] += determinant(
                [[matrix[i][j] for j in subset] for i in subset]
            )
    while len(coeff) > 1 and coeff[-1] == 0:
        coeff.pop()
    return coeff


def matrix_multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def trace_powers(matrix, order=ORDER):
    n = len(matrix)
    current = [[Q(i == j) for j in range(n)] for i in range(n)]
    traces = []
    for _ in range(order):
        current = matrix_multiply(current, matrix)
        traces.append(sum(current[i][i] for i in range(n)))
    return traces


def check_graph(n, edges):
    f, rooted = forest_coefficients(n, edges)
    alpha = normalized(f)
    powers = newton(alpha)
    assert powers == direct_log(alpha)
    recovered = recover_alpha(powers, n - 1)
    assert recovered == alpha
    assert [x / recovered[-1] for x in reversed(recovered)] == f

    matrix = laplacian(n, edges)
    gr = greenian(matrix)
    p_l = determinant_polynomial(matrix)
    p_gr = determinant_polynomial(gr)
    assert p_l == rooted
    assert p_gr == [x / (n * f[-1]) for x in reversed(rooted)]
    assert newton(p_l) == trace_powers(matrix)
    assert newton(p_gr) == trace_powers(gr)
    assert all(value > 0 for value in trace_powers(gr))

    sigma = Q(3, 2)
    scaled = [(a, b, sigma * c) for a, b, c in edges]
    scaled_f, _ = forest_coefficients(n, scaled)
    assert normalized(scaled_f) == [x / sigma ** k
                                   for k, x in enumerate(alpha)]
    assert newton(normalized(scaled_f)) == [x / sigma ** m
                                          for m, x in enumerate(powers, 1)]

    # A new vertex and one edge meet the old graph only at vertex 0.
    edge_c = Q(2)
    joined_f, _ = forest_coefficients(n + 1, edges + [(0, n, edge_c)])
    assert normalized(joined_f) == multiply(alpha, [Q(1), 1 / edge_c])
    assert newton(normalized(joined_f)) == [x + edge_c ** (-m)
                                          for m, x in enumerate(powers, 1)]
    return f, alpha, powers, gr


def main():
    triangle = [(0, 1, Q(1)), (0, 2, Q(1)), (1, 2, Q(1))]
    complete = [(a, b, Q(1)) for a, b in combinations(range(4), 2)]
    path = [(i, i + 1, Q(1)) for i in range(3)]
    tree = [(i, i + 1, Q(i + 1)) for i in range(3)]
    star = [(0, i, Q(1)) for i in range(1, 4)]
    h1 = [(0, 1, Q(1))] * 4 + [(1, 2, Q(1)), (2, 0, Q(1))]
    h2 = [(0, 1, Q(1))] * 3 + [(1, 2, Q(1))] * 3
    cases = {
        "edge": (2, [(0, 1, Q(1))]),
        "weighted_tree": (4, tree),
        "triangle": (3, triangle),
        "K4": (4, complete),
        "path": (4, path),
        "star": (4, star),
        "H1": (3, h1),
        "H2": (3, h2),
    }
    weights = [Q(x) for x in (1, 2, 3, 5, 7, 11)]
    weighted_k4 = [(a, b, c) for (a, b), c in
                   zip(combinations(range(4), 2), weights)]
    for mask in range(64):
        edges = [edge for i, edge in enumerate(weighted_k4) if (mask >> i) & 1]
        if forest_coefficients(4, edges)[0][-1] > 0:
            cases[f"K4_subset_{mask}"] = (4, edges)

    results = {name: check_graph(n, edges)
               for name, (n, edges) in cases.items()}
    assert len(results) == 46
    assert results["triangle"][0] == [1, 3, 3]
    assert results["triangle"][2][:4] == [1, Q(1, 3), 0, Q(-1, 9)]
    assert results["K4"][0] == [1, 6, 15, 16]
    assert results["K4"][2][:4] == [Q(15, 16), Q(33, 256),
                                         Q(-177, 4096), Q(-1983, 65536)]
    assert results["weighted_tree"][1] == [1, Q(11, 6), 1, Q(1, 6)]
    assert results["weighted_tree"][2] == [sum(c ** (-m) for _, _, c in tree)
                                           for m in range(1, ORDER + 1)]
    assert results["path"][2] == results["star"][2] == [3] * ORDER
    assert trace_powers(results["path"][3])[0] == Q(5, 2)
    assert trace_powers(results["star"][3])[0] == Q(9, 4)
    assert trace_powers(results["edge"][3])[0] == Q(1, 2)
    assert results["H1"][0] == results["H2"][0] == [1, 6, 9]
    assert results["H1"][2] == results["H2"][2] == [Q(2, 3 ** m)
                                                     for m in range(1, ORDER + 1)]
    classes1 = sorted(Counter(tuple(sorted((a, b))) for a, b, _ in h1).values())
    classes2 = sorted(Counter(tuple(sorted((a, b))) for a, b, _ in h2).values())
    assert classes1 == [1, 1, 4] and classes2 == [3, 3]

    gr_triangle = results["triangle"][3]
    gamma_edges = [(a, b, -gr_triangle[a][b]) for a, b in combinations(range(3), 2)]
    assert forest_coefficients(3, gamma_edges)[0] == [1, Q(1, 3), Q(1, 27)]
    assert trace_powers(gr_triangle) == [Q(2, 3 ** m) for m in range(1, ORDER + 1)]
    assert trace_powers(results["K4"][3]) == [Q(3, 4 ** m)
                                            for m in range(1, ORDER + 1)]
    print(f"OK: {len(results)} connected graphs; power sums through order {ORDER}.")
    print("Exact enumeration, direct logarithm, Newton recovery, matrix powers,")
    print("rooted reversal, scaling, one-point attachment, and note examples agree.")


if __name__ == "__main__":
    main()
