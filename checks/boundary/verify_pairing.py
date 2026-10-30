"""Exact checks for full boundary pairing (Python 3.10+, standard library).

Run from the repository root: python checks/boundary/verify_pairing.py
The first two boundary-note checkers supply forest enumeration and exact matrices.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
from verify_forest_states import forests, polynomial
from verify_contraction import (partitions, join, compatible, auxiliary, incidence,
                                rank, determinant, inverse, quotient)


def clean(poly):
    return {g: Q(c) for g, c in poly.items() if c}


def add(*polys):
    out = defaultdict(Q)
    for poly in polys:
        for g, c in poly.items():
            out[g] += c
    return clean(out)


def scale(poly, c):
    return clean({g: c * w for g, w in poly.items()})


def multiply(a, b):
    out = defaultdict(Q)
    for g, x in a.items():
        for h, y in b.items():
            out[g + h] += x * y
    return clean(out)


def passport(n, edges, k):
    result = defaultdict(lambda: defaultdict(Q))
    for f in forests(range(n), edges, range(k)):
        result[f['state']][f['g']] += f['weight']
    return {p: clean(poly) for p, poly in result.items()}


def compose(a, b, k):
    out = {}
    for p, x in a.items():
        for s, y in b.items():
            if compatible(p, s, k):
                state = join(p, s)
                out[state] = add(out.get(state, {}), multiply(x, y))
    return {s: p for s, p in out.items() if p}


def glue(n1, e1, n2, e2, k, mapping=None):
    mapping = tuple(range(k)) if mapping is None else mapping
    rename = {v: mapping[v] if v < k else n1 + v - k for v in range(n2)}
    return n1 + n2 - k, e1 + [(rename[u], rename[v], w) for u, v, w in e2]


def rename_passport(data, mapping):
    return {tuple(sorted(tuple(sorted(mapping[v] for v in block)) for block in p)): poly
            for p, poly in data.items()}


def matrix(ps, k):
    return [[Q(compatible(p, s, k)) for s in ps] for p in ps]


def apply(mat, vector):
    return [add(*(scale(p, c) for c, p in zip(row, vector))) for row in mat]


def pair(a, mat, b):
    return add(*(scale(multiply(x, y), mat[i][j])
                 for i, x in enumerate(a) for j, y in enumerate(b)))


def responses(n, edges, ps):
    out = []
    for sigma in ps:
        qn, qe = quotient(n, edges, sigma)
        out.append(clean(polynomial(forests(range(qn), qe, range(qn)))))
    return out


def check_case(n1, e1, n2, e2, k, mapping=None):
    mapping = tuple(range(k)) if mapping is None else mapping
    ps = tuple(partitions(tuple(range(k))))
    C = matrix(ps, k)
    p1, p2 = passport(n1, e1, k), passport(n2, e2, k)
    p2 = rename_passport(p2, mapping)
    n, edges = glue(n1, e1, n2, e2, k, mapping)
    direct = passport(n, edges, k)
    combined = compose(p1, p2, k)
    assert combined == direct, (k, mapping, combined, direct)
    f1, f2 = [p1.get(p, {}) for p in ps], [p2.get(p, {}) for p in ps]
    total = clean(polynomial(forests(range(n), edges, range(k))))
    assert pair(f1, C, f2) == total == add(*combined.values())
    # Responses are independently enumerated on contracted graphs.
    re2 = [(mapping[u] if u < k else u, mapping[v] if v < k else v, w) for u, v, w in e2]
    u1, u2 = responses(n1, e1, ps), responses(n2, re2, ps)
    assert apply(C, f1) == u1 and apply(C, f2) == u2
    if k <= 3:
        inv = inverse(C)
        assert apply(inv, u1) == f1 and apply(inv, u2) == f2
        assert pair(u1, inv, u2) == total
    # At the level of individual forests the same bijection preserves edge IDs.
    valid = {f['selected'] for f in forests(range(n), edges, range(k))}
    lifted = set()
    for a in forests(range(n1), e1, range(k)):
        for b in forests(range(n2), re2, range(k)):
            selected = a['selected'] + tuple(len(e1) + j for j in b['selected'])
            passed = compatible(a['state'], b['state'], k)
            assert passed == (selected in valid)
            if passed:
                lifted.add(selected)
    assert lifted == valid
    return total


def main():
    matrix_pairs = 0
    for k in range(1, 5):
        ps = tuple(partitions(tuple(range(k))))
        assert len(ps) == [1, 2, 5, 15][k - 1]
        C = matrix(ps, k)
        for i, p in enumerate(ps):
            for j, s in enumerate(ps):
                edges = auxiliary(p) + auxiliary(s)
                assert C[i][j] == (rank(incidence(k, edges)) == len(edges))
                matrix_pairs += 1
        for mapping in permutations(range(k)):
            perm = [tuple(sorted(tuple(sorted(mapping[v] for v in block)) for block in p)) for p in ps]
            assert matrix(perm, k) == C
    p2 = (((0,), (1,)), ((0, 1),))
    p3 = (((0,), (1,), (2,)), ((0, 1), (2,)), ((0, 2), (1,)), ((0,), (1, 2)), ((0, 1, 2),))
    C2 = [[1, 1], [1, 0]]
    C3 = [[1,1,1,1,1],[1,0,1,1,0],[1,1,0,1,0],[1,1,1,0,0],[1,0,0,0,0]]
    C3inv2 = [[0,0,0,0,2],[0,-1,1,1,-1],[0,1,-1,1,-1],[0,1,1,-1,-1],[2,-1,-1,-1,1]]
    assert matrix(p2, 2) == C2 and determinant(C2) == -1
    assert matrix(p3, 3) == C3 and determinant(C3) == -2
    assert inverse(C3) == [[Q(c, 2) for c in row] for row in C3inv2]
    assert inverse(C2) == [[0,1],[1,-1]]

    cases = 0
    # Exhaustive pairs of the 16 subgraphs of a fixed weighted four-vertex graph.
    host = [(0,3,Q(2)),(1,3,Q(3)),(2,3,Q(5)),(0,1,Q(7))]
    family = [[e for j, e in enumerate(host) if mask & (1 << j)] for mask in range(16)]
    for k in (1, 2, 3):
        for e1 in family:
            for e2 in family:
                check_case(4, e1, 4, e2, k)
                cases += 1

    path2 = [(0,2,Q(1)), (2,1,Q(1))]
    assert check_case(3, path2, 3, path2, 2) == {0:1,1:4,2:6,3:4}
    cases += 1
    X = [(0,3,Q(1)),(3,1,Q(1)),(1,4,Q(1)),(4,2,Q(1))]
    Xp = [(0,3,Q(1)),(3,2,Q(1)),(2,4,Q(1)),(4,1,Q(1))]
    J = [(0,1,Q(1))]
    A, Qp = {0:1,1:4,2:4}, {2:1,3:2}
    assert [passport(5,X,3).get(p,{}) for p in p3] == [A,Qp,{},Qp,{4:1}]
    assert [passport(5,Xp,3).get(p,{}) for p in p3] == [A,{},Qp,Qp,{4:1}]
    assert check_case(5, X, 3, J, 3) == {0:1,1:5,2:10,3:9,4:3}
    assert check_case(5, Xp, 3, J, 3) == {0:1,1:5,2:10,3:10,4:5}
    cases += 2
    for mapping in permutations(range(3)):
        check_case(5, X, 4, host, 3, mapping)
        cases += 1

    # Parallel copies, one true seam edge, and no seam are different graphs.
    assert check_case(2,[(0,1,Q(1))],2,[(0,1,Q(1))],2) == {0:1,1:2}
    assert check_case(2,[(0,1,Q(1))],2,[],2) == {0:1,1:1}
    cases += 2
    e1 = [(0,1,Q(1,2)),(0,1,Q(3,2)),(1,2,Q(2)),(2,2,Q(7))]
    check_case(4,e1,3,path2,2,(1,0))  # An isolated internal vertex and a loop.
    cases += 1
    check_case(4,host,4,host,4)  # The full compatibility matrix need not be inverted.
    cases += 1

    # Sequential gluing: compare both bracketings and direct graph enumeration.
    pa, pb, pc = passport(5,X,3), passport(3,J,3), passport(4,host,3)
    left = compose(compose(pa,pb,3),pc,3)
    right = compose(pa,compose(pb,pc,3),3)
    n, es = glue(5,X,3,J,3)
    n, es = glue(n,es,4,host,3)
    assert left == right == passport(n,es,3)
    print(f'PASS: {cases} graph-pair configurations; {matrix_pairs} representative-state pairs.')
    print('Full output passports, labelled-forest bijections, direct contraction responses and inverse pairings agree.')
    print('Examples, all boundary permutations, rational parallel edges, loops, internal components and three-part gluing passed.')


if __name__ == '__main__':
    main()
