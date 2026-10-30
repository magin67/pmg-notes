"""Exact boundary-state reduction checks (Python 3.10+, standard library).

Run from the repository root: python checks/boundary/verify_reduction.py
General theorems are proved in the note; finite tests are independent examples.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb
from verify_forest_states import forests, polynomial
from verify_contraction import (partitions, join, compatible, auxiliary,
                                incidence, rank, determinant, inverse)
from verify_pairing import (passport, matrix, apply, pair, glue, responses,
                            add, clean, scale)


def parse(label):
    return tuple(sorted(tuple(ord(v) - ord('a') for v in block)
                        for block in label.split('|')))


LABELS = ['a|b|c|d', 'ab|c|d', 'ac|b|d', 'ad|b|c', 'a|bc|d',
          'a|bd|c', 'a|b|cd', 'abc|d', 'abd|c', 'acd|b', 'a|bcd',
          'ab|cd', 'ad|bc', 'abcd', 'ac|bd']
PS = tuple(map(parse, LABELS))
C = matrix(PS, 4)
H = [row[:14] for row in C[:14]]
ETA = [0] * 7 + [-1] * 4 + [1] * 4
REDUCTION = [[Q(i == j) for j in range(14)] + [Q(-ETA[i])]
             for i in range(14)]


def transpose(a):
    return list(map(list, zip(*a)))


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def noncrossing(p):
    return not any(a < b < c < d or b < a < d < c
                   for u, v in combinations(p, 2)
                   for a, c in combinations(u, 2) for b, d in combinations(v, 2))


def spanning_matrix(ps, k):
    return [[int(len(p) + len(s) == k + 1 and len(join(p, s)) == 1)
             for s in ps] for p in ps]


def check_general_matrices():
    results = []
    for k in range(1, 6):
        ps = tuple(partitions(tuple(range(k))))
        nc = tuple(p for p in ps if noncrossing(p))
        full, reduced, tree = matrix(ps, k), matrix(nc, k), spanning_matrix(nc, k)
        catalan = comb(2 * k, k) // (k + 1)
        assert len(nc) == rank(full) == rank(reduced) == rank(tree) == catalan
        assert determinant(reduced) == determinant(tree) != 0
        # Check every matrix entry by an independent incidence-rank criterion.
        for i, p in enumerate(ps):
            for j, s in enumerate(ps):
                edges = auxiliary(p) + auxiliary(s)
                assert full[i][j] == (rank(incidence(k, edges)) == len(edges))
        for r in range(k):
            rows = [i for i, p in enumerate(nc) if k - len(p) == r]
            cols = [j for j, s in enumerate(nc) if k - len(s) == k - 1 - r]
            block = [[reduced[i][j] for j in cols] for i in rows]
            assert len(rows) == len(cols) and determinant(block) != 0
        for i, p in enumerate(nc):
            for j, s in enumerate(nc):
                total_rank = 2 * k - len(p) - len(s)
                if total_rank > k - 1:
                    assert reduced[i][j] == 0
                elif total_rank == k - 1:
                    assert reduced[i][j] == tree[i][j]
        results.append((k, len(ps), catalan, determinant(reduced)))
    return results


def check_four_matrix():
    assert len(set(PS)) == 15 and all(noncrossing(p) for p in PS[:14])
    assert not noncrossing(PS[14])
    assert [sum(a * b for a, b in zip(row, ETA)) for row in C] == [0] * 15
    A = [row[7:13] for row in H[1:7]]
    expected = [[0,0,1,1,0,1], [0,1,0,1,1,1], [1,0,0,1,1,0],
                [0,1,1,0,1,0], [1,0,1,0,1,1], [1,1,0,0,0,1]]
    assert A == expected and abs(determinant(A)) == 8
    assert determinant(H) == -64 and rank(C) == 14
    assert matmul(transpose(REDUCTION), matmul(H, REDUCTION)) == C
    theta = ETA.copy()
    theta[13] = 0
    # Structural relation fails the forest pairing on the discrete test.
    assert [sum(a * b for a, b in zip(row, theta)) for row in C] == [-1] + [0] * 14
    for mapping in permutations(range(4)):
        renamed = [tuple(sorted(tuple(sorted(mapping[v] for v in block)) for block in p)) for p in PS]
        assert matrix(renamed, 4) == C
        assert [sum(a * b for a, b in zip(row, ETA)) for row in matrix(renamed, 4)] == [0] * 15
    return A


def check_graph(n, edges):
    data = passport(n, edges, 4)
    f = [data.get(p, {}) for p in PS]
    reduced = apply(REDUCTION, f)
    u = responses(n, edges, PS)  # Direct enumeration on the fifteen quotients.
    assert apply(C, f) == u
    assert add(*(scale(p, c) for p, c in zip(u, ETA))) == {}
    assert apply(H, reduced) == u[:14]
    assert apply(inverse(H), u[:14]) == reduced
    return f, reduced, u


def check_pair(left, right, mapping=None):
    n1, e1 = left
    n2, e2 = right
    if mapping is not None:
        e2 = [(mapping[u] if u < 4 else u, mapping[v] if v < 4 else v, w) for u, v, w in e2]
    f = [passport(n1, e1, 4).get(p, {}) for p in PS]
    g = [passport(n2, e2, 4).get(p, {}) for p in PS]
    rf, rg = apply(REDUCTION, f), apply(REDUCTION, g)
    uf, ug = apply(C, f)[:14], apply(C, g)[:14]
    n, edges = glue(n1, e1, n2, e2, 4)
    direct = clean(polynomial(forests(range(n), edges, range(4))))
    assert pair(f, C, g) == pair(rf, H, rg) == pair(uf, inverse(H), ug) == direct
    return direct


def main():
    results = check_general_matrices()
    A = check_four_matrix()
    host = [(u, v, Q(w)) for (u, v), w in zip(combinations(range(4), 2), [1,2,3,5,7,11])]
    family = [(4, [e for j, e in enumerate(host) if mask & (1 << j)]) for mask in range(64)]
    matching = (4, [(0,2,Q(1)),(1,3,Q(1))])
    edge = (4, [(0,1,Q(1))])
    star = (5, [(v,4,Q(1)) for v in range(4)])
    extra = (6, [(0,4,Q(1,2)),(4,2,Q(3)),(1,3,Q(2)),(1,3,Q(5)),(2,2,Q(7))])
    for graph in family + [matching, star, extra]:
        check_graph(*graph)
    pairs = 0
    for graph in family:
        for partner in [edge, matching, star]:
            check_pair(graph, partner)
            pairs += 1
    weighted_star = (5, [(v,4,Q(w)) for v,w in enumerate([1,2,3,5])])
    for mapping in permutations(range(4)):
        check_pair(extra, weighted_star, mapping)
        pairs += 1
    assert check_pair(matching, edge) == {0:1,1:3,2:3,3:1}
    pairs += 1
    f, reduced, _ = check_graph(*matching)
    assert f[14] == {2:1} and f[13] == {}
    assert reduced[7:11] == [{2:1}] * 4
    assert reduced[11:14] == [{2:-1}] * 3
    assert add(*(scale(p, c) for p, c in zip(f, ETA))) == {2:1}
    dropped = f.copy()
    dropped[14] = {}
    partner = [passport(*edge,4).get(p,{}) for p in PS]
    assert pair(dropped,C,partner) == {0:1,1:3,2:2}
    for k, bell, catalan, det in results:
        print(f'k={k}: states={bell}, rank={catalan}, det(NC)={det}')
    print(f'PASS: 67 graph passports, {pairs} graph-pair configurations and all 24 boundary permutations.')
    print(f'PASS: radical, reduced matrix, det(A)={determinant(A)}, det(H)=-64, state/response formulas and counterexample.')


if __name__ == '__main__':
    main()
