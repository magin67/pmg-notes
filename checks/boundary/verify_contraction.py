"""Exact contraction checks: partitions, quotient forests and matrix minors.

Run: python checks/boundary/verify_contraction.py
Python 3.10+ and the adjacent verify_forest_states.py are sufficient.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from verify_forest_states import forests, polynomial


def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for part in partitions(rest):
        yield ((first,),) + part
        for i, block in enumerate(part):
            yield tuple(sorted(part[:i] + ((first,) + block,) + part[i + 1:]))


def join(pi, sigma):
    blocks = [set(block) for block in pi]
    for block in sigma:
        meeting = [b for b in blocks if b.intersection(block)]
        merged = set(block).union(*meeting)
        blocks = [b for b in blocks if not b.intersection(block)] + [merged]
    return tuple(sorted(tuple(sorted(b)) for b in blocks))


def compatible(pi, sigma, size):
    return size - len(join(pi, sigma)) == 2 * size - len(pi) - len(sigma)


def quotient(n, edges, sigma):
    mapping = {}
    for i, block in enumerate(sigma):
        for v in block:
            mapping[v] = i
    for v in range(n):
        if v not in mapping:
            mapping[v] = len(set(mapping.values()))
    return len(set(mapping.values())), [(mapping[u], mapping[v], w) for u, v, w in edges]


def auxiliary(sigma):
    return [(block[0], v, Q(1)) for block in sigma for v in block[1:]]


def rank(matrix):
    a = [list(map(Q, row)) for row in matrix]
    row = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [x / scale for x in a[row]]
        for i in range(row + 1, len(a)):
            scale = a[i][col]
            a[i] = [x - scale * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def incidence(n, edges):
    return [[Q((i == v) - (i == u)) for u, v, _ in edges] for i in range(n)]


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        result *= a[j][j]
        for i in range(j + 1, len(a)):
            scale = a[i][j] / a[j][j]
            a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    return result


def inverse(matrix):
    n = len(matrix)
    a = [list(map(Q, row)) + [Q(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def laplacian(n, edges):
    result = [[Q(0)] * n for _ in range(n)]
    for u, v, w in edges:
        result[u][u] += w
        result[v][v] += w
        result[u][v] -= w
        result[v][u] -= w
    return result


def tau(matrix):
    return determinant([row[:-1] for row in matrix[:-1]])


def greenian(matrix):
    n = len(matrix)
    shifted = [[x + Q(1, n) for x in row] for row in matrix]
    return [[x - Q(1, n) for x in row] for row in inverse(shifted)]


def gram(columns, metric):
    return [[sum(x * metric[i][j] * y for i, x in enumerate(u) for j, y in enumerate(v))
             for v in columns] for u in columns]


def merged_edges(edges):
    weights = Counter()
    for u, v, w in edges:
        if u != v:
            weights[tuple(sorted((u, v)))] += w
    return [(u, v, w) for (u, v), w in weights.items()]


def verify_case(n, edges, boundaries):
    L = laplacian(n, edges)
    original_tau = tau(L)
    metric = greenian(L) if original_tau else None
    comparisons, determinant_checks = 0, 0
    for boundary in boundaries:
        original = list(forests(range(n), edges, boundary))
        assert polynomial(original)[n - 1] == original_tau
        for sigma in partitions(boundary):
            r = len(boundary) - len(sigma)
            qn, qe = quotient(n, edges, sigma)
            assert qn == n - r
            direct = list(forests(range(qn), qe, range(qn)))
            selected_sets = {f['selected'] for f in direct}
            accepted = []
            aux = auxiliary(sigma)
            columns = list(zip(*incidence(n, aux))) if aux else []
            for f in original:
                passed = compatible(f['state'], sigma, len(boundary))
                assert passed == (f['selected'] in selected_sets)
                augmented = [edges[i] for i in f['selected']] + aux
                independent = rank(incidence(n, augmented)) == len(augmented)
                assert passed == independent
                if passed:
                    accepted.append(f)
            assert {f['selected'] for f in accepted} == selected_sets
            assert polynomial(accepted) == polynomial(direct)
            combined = list(forests(range(qn), merged_edges(qe), range(qn)))
            assert polynomial(combined) == polynomial(direct)
            quotient_tau = tau(laplacian(qn, qe))
            assert polynomial(direct)[qn - 1] == quotient_tau
            comparisons += 1
            if metric is not None:
                assert original_tau * determinant(gram(columns, metric)) == quotient_tau
                # Scaling one basis column changes the Gram determinant by four.
                scaled = [tuple(2 * x for x in columns[0])] + columns[1:] if columns else []
                correction = 4 if columns else 1
                assert original_tau * determinant(gram(scaled, metric)) / correction == quotient_tau
                determinant_checks += 1
    return comparisons, determinant_checks


def main():
    path = [(i, i + 1, Q(1)) for i in range(4)]
    totals = list(verify_case(5, path, [(0, 2, 4)]))
    expected = {
        ((0, 2), (4,)): {0: 1, 1: 4, 2: 5, 3: 2},
        ((0, 4), (2,)): {0: 1, 1: 4, 2: 6, 3: 4},
        ((0, 2, 4),): {0: 1, 1: 4, 2: 4}}
    for sigma, coefficients in expected.items():
        qn, qe = quotient(5, path, sigma)
        assert polynomial(forests(range(qn), qe, range(qn))) == coefficients
    gr = gram([(Q(-1), 0, 1, 0, 0), (Q(-1), 0, 0, 0, 1)], greenian(laplacian(5, path)))
    assert gr == [[2, 2], [2, 4]] and determinant(gr) == 4

    triangle = [(0, 1, Q(2)), (0, 2, Q(3)), (1, 2, Q(5))]
    qn, qe = quotient(3, triangle, ((0, 1),))
    assert polynomial(forests(range(qn), qe, range(qn))) == {0: 1, 1: 8}
    assert tau(laplacian(3, triangle)) == 31
    assert gram([(-1, 1, 0)], greenian(laplacian(3, triangle))) == [[Q(8, 31)]]
    assert not compatible(((0, 2), (1, 3)), ((0, 1), (2, 3)), 4)
    assert rank(incidence(3, [(0, 1, 1), (1, 2, 1), (2, 0, 1)])) == 2
    assert rank(incidence(3, auxiliary(((0, 1, 2),)))) == 2

    complete = [(u, v, Q(w)) for (u, v), w in zip(combinations(range(4), 2), [1, 2, 3, 5, 7, 11])]
    boundaries = [b for size in range(1, 5) for b in combinations(range(4), size)]
    for mask in range(64):
        edges = [e for i, e in enumerate(complete) if mask & (1 << i)]
        counts = verify_case(4, edges, boundaries)
        totals = [a + b for a, b in zip(totals, counts)]
    extras = [
        (3, triangle, [(0, 1), (0, 1, 2)]),
        (3, [(0, 1, Q(1, 2)), (0, 1, Q(3, 2)), (1, 2, Q(2)), (1, 1, Q(7))], [(0, 1, 2)]),
        (4, [(0, 1, Q(1)), (2, 3, Q(1))], [(0, 2)]),
        (1, [], [(0,)])]
    for args in extras:
        counts = verify_case(*args)
        totals = [a + b for a, b in zip(totals, counts)]
    qn, qe = quotient(4, [(0, 1, 1), (2, 3, 1)], ((0, 2),))
    assert tau(laplacian(qn, qe)) == 1
    print(f'PASS: {totals[0]} contraction configurations; {totals[1]} connected Gram/cofactor checks.')
    print('Forest states, labelled quotient subsets, auxiliary incidence ranks and merged weights agree.')
    print('P5, weighted triangle, loops, parallel edges, disconnection, redundant pairs and basis scaling passed.')


if __name__ == '__main__':
    main()
