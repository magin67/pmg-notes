"""Exact checks for the canonical vector representation; Python standard library.

Run from any directory: python /path/to/checks/dual/verify_vector.py
No files are written. All arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, prod
import json


def add(a, b, scale=F(1)):
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, F(0)) + scale * value
        if not result[key]:
            del result[key]
    return result


def wedge_sign(a, b):
    if a & b:
        return 0
    return (-1) ** sum((b & ((1 << i) - 1)).bit_count()
                       for i in range(a.bit_length()) if a >> i & 1)


def wedge(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out = add(out, {i | j: x * y * wedge_sign(i, j)})
    return out


def tensor(a, b):
    return {(i, j): x * y for i, x in a.items() for j, y in b.items()}


def multiply(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            coefficient = x * y * wedge_sign(i, k) * wedge_sign(j, l)
            out = add(out, {(i | k, j | l): coefficient})
    return out


def determinant(A):
    a = [list(map(F, row)) for row in A]
    d = F(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            d = -d
        d *= a[k][k]
        for i in range(k + 1, len(a)):
            ratio = a[i][k] / a[k][k]
            for j in range(k + 1, len(a)):
                a[i][j] -= ratio * a[k][j]
    return d


def inverse(A):
    n = len(A)
    a = [list(map(F, row)) + [F(i == j) for j in range(n)]
         for i, row in enumerate(A)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        divisor = a[k][k]
        a[k] = [x / divisor for x in a[k]]
        for i in range(n):
            if i != k:
                multiplier = a[i][k]
                a[i] = [x - multiplier * y for x, y in zip(a[i], a[k])]
    return [row[n:] for row in a]


def laplacian(n, edges):
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, c in edges:
        A[i][i] += c
        A[j][j] += c
        A[i][j] -= c
        A[j][i] -= c
    return A


def forest_partition(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j, _ in edges:
        a, b = root(i), root(j)
        if a == b:
            return None
        parent[a] = b
    groups = {}
    for i in range(n):
        groups.setdefault(root(i), []).append(i)
    return sorted(groups.values())


def coform(group, n):
    return {1 << i: F(int(i in group) - int(n - 1 in group))
            for i in range(n - 1)
            if int(i in group) != int(n - 1 in group)}


def minor_form(A, k):
    out = {}
    for I in combinations(range(len(A)), k):
        for J in combinations(range(len(A)), k):
            coefficient = determinant([[A[i][j] for j in J] for i in I])
            if coefficient:
                out[sum(1 << i for i in I), sum(1 << j for j in J)] = coefficient
    return out


def verify(name, n, source_edges):
    edges = [(i, j, F(c)) for i, j, c in source_edges]
    L = laplacian(n, edges)
    A = [row[:-1] for row in L[:-1]]
    tau = determinant(A)
    Ainv = inverse(A)
    Gr = inverse([[L[i][j] + F(1, n) for j in range(n)] for i in range(n)])
    Gr = [[x - F(1, n) for x in row] for row in Gr]
    R = [[Gr[i][i] + Gr[j][j] - 2 * Gr[i][j] for j in range(n)] for i in range(n)]
    rows = list(map(sum, R))
    pairs = [(i, j, -Gr[i][j]) for i, j in combinations(range(n), 2)]
    gamma_lap = laplacian(n, pairs)
    assert gamma_lap == Gr
    assert determinant([row[:-1] for row in Gr[:-1]]) == F(1, n * n) / tau
    vertices = [coform([i], n) for i in range(n)]
    vectors = [add(vertices[j], vertices[i], -1) for i, j, _ in pairs]
    vector_form = {}
    polar_form = {}
    for (i, j, gamma), u in zip(pairs, vectors):
        assert gamma == (R[i][j] - rows[i] / n - rows[j] / n + sum(rows) / (n*n)) / 2
        vector_form = add(vector_form, tensor(u, u), gamma)
        polar_form = add(polar_form, add(tensor(vertices[i], vertices[j]),
                                         tensor(vertices[j], vertices[i])), -R[i][j]/2)
    assert vector_form == polar_form == minor_form(Ainv, 1)
    forest_grades = [{} for _ in range(n)]
    positive, negative, counts = F(0), F(0), [0, 0, 0]
    tree_groups = {}
    for k in range(n):
        for selected in combinations(range(len(pairs)), k):
            selected_edges = [pairs[i] for i in selected]
            partition = forest_partition(n, selected_edges)
            blade = {0: F(1)}
            for i in selected:
                blade = wedge(blade, vectors[i])
            assert bool(blade) == (partition is not None)
            weight = prod((pairs[i][2] for i in selected), start=F(1))
            forest_grades[k] = add(forest_grades[k], tensor(blade, blade), weight)
            if partition is not None and k == n-1:
                negatives = sum(pairs[i][2] < 0 for i in selected)
                count, total = tree_groups.get(negatives, (0, F(0)))
                tree_groups[negatives] = (count + 1, total + weight)
                if weight > 0:
                    positive += weight
                    counts[0] += 1
                elif weight < 0:
                    negative += weight
                    counts[1] += 1
                else:
                    counts[2] += 1
    assert positive + negative == F(1, n*n) / tau
    source_forest_grades = [{} for _ in range(n)]
    for k in range(n):
        for subset in combinations(edges, k):
            partition = forest_partition(n, subset)
            if partition is None:
                continue
            blade = {0: F(1)}
            for group in partition[:-1]:
                blade = wedge(blade, coform(group, n))
            weight = prod((c for _, _, c in subset), start=F(1)) / tau
            grade = n - 1 - k
            source_forest_grades[grade] = add(source_forest_grades[grade], tensor(blade, blade), weight)
    power = {(0, 0): F(1)}
    factored = dict(power)
    for (_, _, gamma), u in zip(pairs, vectors):
        factored = multiply(factored, add({(0, 0): F(1)}, tensor(u, u), gamma))
    for k in range(n):
        expected = minor_form(Ainv, k)
        exponential = {key: value / factorial(k) for key, value in power.items()}
        assert forest_grades[k] == source_forest_grades[k] == expected == exponential
        assert {key: value for key, value in factored.items() if key[0].bit_count() == k} == expected
        power = multiply(power, vector_form)
    assert not power
    top_mask = (1 << (n-1)) - 1
    assert forest_grades[-1] == {(top_mask, top_mask): F(1) / tau}
    if name == 'P4':
        assert tree_groups == {0: (4, F(84, 512)), 1: (8, F(-64, 512)), 2: (4, F(12, 512))}
        def boundary_of(group):
            blade = {0: F(1)}
            for i in group[1:]:
                blade = wedge(blade, add(vertices[i], vertices[group[0]], -1))
            return blade
        explicit_q2 = {}
        for group, coefficient in [([0, 1, 2], -1), ([0, 1, 3], 7),
                                    ([0, 2, 3], 7), ([1, 2, 3], -1)]:
            blade = boundary_of(group)
            explicit_q2 = add(explicit_q2, tensor(blade, blade), F(coefficient, 64))
        for first, second, coefficient in [([0, 1], [2, 3], 1),
                                           ([0, 2], [1, 3], 9),
                                           ([0, 3], [1, 2], 5)]:
            blade = wedge(boundary_of(first), boundary_of(second))
            explicit_q2 = add(explicit_q2, tensor(blade, blade), F(coefficient, 64))
        assert explicit_q2 == forest_grades[2]
        short_q2 = {}
        for i, j in [(0, 1), (0, 3), (2, 3)]:
            blade = wedge(vertices[i], vertices[j])
            short_q2 = add(short_q2, tensor(blade, blade))
        assert short_q2 == explicit_q2
    # Full boundary of the dependent dual vertices, computed as an alternating sum.
    boundary = {}
    for omit in range(n):
        blade = {0: F(1)}
        for i in range(n):
            if i != omit:
                blade = wedge(blade, vertices[i])
        boundary = add(boundary, blade, F((-1)**omit))
    assert tensor(boundary, boundary) == {(top_mask, top_mask): F(n*n)}
    return dict(graph=name, n=n, tau=str(tau), signed_tree_sum=str(positive+negative),
                positive_sum=str(positive), negative_sum=str(negative),
                tree_counts_positive_negative_zero=counts, grades_checked=n)


if __name__ == '__main__':
    cases = [
        ('edge2', 2, [(0, 1, 2)]),
        ('P3', 3, [(0, 1, 1), (1, 2, 1)]),
        ('P4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
        ('weightedP4', 4, [(0, 1, 2), (1, 2, 3), (2, 3, 5)]),
        ('C4', 4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]),
        ('K4', 4, [(i, j, 1) for i, j in combinations(range(4), 2)]),
        ('weightedK5', 5, [(i, j, 2) for i, j in combinations(range(5), 2)]),
        ('weighted5', 5, [(0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 0, 11), (0, 2, 13)]),
        ('P6', 6, [(i, i+1, 1) for i in range(5)]),
    ]
    print(json.dumps([verify(*case) for case in cases], ensure_ascii=False, indent=2))
