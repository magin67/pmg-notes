"""Exact checks for the two-terminal Laplacian spectral passport (stdlib only).

Run: python checks/boundary/verify_spectral_boundary.py
Polynomial coefficients are stored in ascending order over Fraction.
Graph edges are labelled occurrences; loops have zero incidence contribution.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from functools import lru_cache
from verify_forest_states import forests


def poly(*values):
    result = list(map(Q, values)) or [Q(0)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


ZERO, ONE, X = poly(0), poly(1), poly(0, 1)


def add(*terms):
    result = [Q(0)] * max(map(len, terms), default=1)
    for term in terms:
        for i, c in enumerate(term):
            result[i] += c
    return poly(*result)


def scale(term, factor):
    return poly(*(factor*c for c in term))


def mul(*terms):
    result = ONE
    for term in terms:
        out = [Q(0)] * (len(result)+len(term)-1)
        for i, a in enumerate(result):
            for j, b in enumerate(term):
                out[i+j] += a*b
        result = poly(*out)
    return result


def at(term, x):
    result = Q(0)
    for c in reversed(term):
        result = result*x+c
    return result


def pdet(matrix):
    """Division-free subset expansion, including nonsymmetric cofactor minors."""
    n = len(matrix)
    states = {0: ONE}
    for row in range(n):
        next_states = {}
        for mask, value in states.items():
            for col in range(n):
                if mask & (1 << col):
                    continue
                sign = (-1)**(mask >> (col+1)).bit_count()
                key = mask | (1 << col)
                term = scale(mul(value, matrix[row][col]), sign)
                next_states[key] = add(next_states.get(key, ZERO), term)
        states = next_states
    return states[(1 << n)-1]


def qdet(matrix):
    """Independent rational Gaussian determinant, with row pivoting."""
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
        for i in range(j+1, len(a)):
            f = a[i][j]/a[j][j]
            for k in range(j+1, len(a)):
                a[i][k] -= f*a[j][k]
    return result


def minor(matrix, rows=(), cols=None):
    cols = rows if cols is None else cols
    return [[entry for j, entry in enumerate(row) if j not in cols]
            for i, row in enumerate(matrix) if i not in rows]


def pencil(vertices, edges):
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    lap = [[Q(0) for _ in vertices] for _ in vertices]
    for u, v, weight in edges:
        i, j = index[u], index[v]
        if i == j:
            continue
        lap[i][i] += weight
        lap[j][j] += weight
        lap[i][j] -= weight
        lap[j][i] -= weight
    return [[poly(-lap[i][j], int(i == j)) for j in range(n)] for i in range(n)]


@lru_cache(None)
def passport(vertices, edges, boundary=('a', 'b')):
    m = pencil(vertices, edges)
    a, b = (vertices.index(v) for v in boundary)
    return (pdet(m), pdet(minor(m, (a,))), pdet(minor(m, (b,))),
            scale(pdet(minor(m, (b,), (a,))), (-1)**(a+b)),
            pdet(minor(m, (a, b))))


def combine(first, second, common=0):
    """Full component Laplacians; optional one shared ab edge of this weight."""
    a, b, c, d, e = first
    aa, bb, cc, dd, ee = second
    e0 = mul(e, ee)
    b0, c0, d0 = add(mul(b, ee), mul(e, bb)), add(mul(c, ee), mul(e, cc)), add(mul(d, ee), mul(e, dd))
    core = add(mul(a, ee), mul(e, aa), mul(b, cc), mul(c, bb), scale(mul(d, dd), -2))
    shift = poly(common, -1)
    new_a = add(core, mul(shift, add(b0, c0)), scale(d0, -2*common), mul(poly(0, -2*common, 1), e0))
    return (new_a, add(b0, mul(shift, e0)), add(c0, mul(shift, e0)),
            add(d0, scale(e0, common)), e0)


def glue(g1, g2, common=0):
    vertices = tuple(dict.fromkeys(g1[0]+g2[0]))
    assert set(g1[0]) & set(g2[0]) == {'a', 'b'}
    edges = list(g1[1]+g2[1])
    if common:
        assert sum({u, v} == {'a', 'b'} and w == common for u, v, w in edges) >= 2
        edges.remove(next(e for e in edges if set(e[:2]) == {'a', 'b'} and e[2] == common))
    return vertices, tuple(edges)


def state_polynomials(vertices, edges):
    result = {}
    for f in forests(vertices, edges, ('a', 'b')):
        key = len(f['state'])
        term = poly(*([0]*f['g']), f['weight'])
        result[key] = add(result.get(key, ZERO), term)
    return result


def check_one(graph):
    m = pencil(*graph)
    a, b, c, d, e = passport(*graph)
    assert mul(a, e) == add(mul(b, c), scale(mul(d, d), -1))
    for x in (Q(-1), Q(0), Q(2), Q(7, 3)):
        assert at(a, x) == qdet([[at(z, x) for z in row] for row in m])
    # Independently enumerate rooted forests, including isolated vertices.
    rooted = ZERO
    for f in forests(*graph, ('a', 'b')):
        weight = f['weight']
        for block in f['components']:
            weight *= len(block)
        rooted = add(rooted, poly(*([0]*(len(graph[0])-f['g'])), (-1)**f['g']*weight))
    assert a == rooted


def main():
    path = (tuple('abcd'), (('a', 'b', 1), ('b', 'c', 1), ('c', 'd', 1)))
    star = (tuple('abcd'), (('a', 'b', 1), ('b', 'c', 1), ('b', 'd', 1)))
    assert state_polynomials(*path) == state_polynomials(*star) == {2: poly(1, 2, 1), 1: poly(0, 1, 2, 1)}
    assert passport(*path)[0] == poly(0, -4, 10, -6, 1)
    assert passport(*star)[0] == poly(0, -4, 9, -6, 1)
    p3 = (tuple('aub'), (('a', 'u', 1), ('u', 'b', 1)))
    q3 = (tuple('avb'), (('a', 'v', 1), ('v', 'b', 1)))
    s3 = passport(*p3)
    assert s3 == (poly(0, 3, -4, 1), poly(1, -3, 1), poly(1, -3, 1), ONE, poly(-2, 1))
    assert combine(s3, s3)[0] == poly(0, -16, 20, -8, 1)
    assert at(combine(s3, s3)[0], 2) == 0  # Both interior determinants vanish here.
    # A principal minor retains the original degrees; it is not chi of G-a.
    assert s3[1] != passport(('a', 'b'), (('a', 'b', 1),))[0]
    near = passport(*p3, boundary=('a', 'u'))
    assert near[0] == s3[0] and near[4] == poly(-1, 1) != s3[4]
    t1, t2 = (p3[0], p3[1]+(('a', 'b', 1),)), (q3[0], q3[1]+(('a', 'b', 1),))
    single = passport(*glue(t1, t2, 1))
    double = passport(*glue(t1, t2))
    assert single == combine(passport(*t1), passport(*t2), 1)
    assert single[0] == poly(0, -32, 32, -10, 1)
    assert double[0] == poly(0, -48, 44, -12, 1)
    assert single == combine(passport(*t1), passport(*q3))  # One owner for ab.

    k4_edges = tuple((u, v, 1) for u, v in combinations('abcd', 2))
    k3_edges = (('a', 'u', Q(1, 2)), ('b', 'u', Q(3, 2)), ('a', 'b', 2))
    left = [(tuple('abcd'), tuple(e for j, e in enumerate(k4_edges) if mask >> j & 1)) for mask in range(64)]
    right = [(tuple('abu'), tuple(e for j, e in enumerate(k3_edges) if mask >> j & 1)) for mask in range(8)]
    exceptional = [(tuple('abci'), (('a', 'b', Q(1, 2)), ('a', 'b', Q(2, 3)), ('b', 'c', 2), ('c', 'c', 7))),
                   (tuple('ab'), ()), path, star, p3, q3, t1, t2]
    for graph in left+right+exceptional:
        check_one(graph)
    for g1 in left+exceptional[:2]:
        for g2 in right:
            assert combine(passport(*g1), passport(*g2)) == passport(*glue(g1, g2))

    # Weighted common edge: all subsets of the remaining four triangle edges.
    shared_count = 0
    for weight in (Q(1, 2), Q(1), Q(3, 2)):
        for mask in range(16):
            g1 = (tuple('abc'), (('a', 'b', weight),)+tuple(e for j, e in enumerate((('a', 'c', 2), ('b', 'c', Q(1, 3)))) if mask >> j & 1))
            g2 = (tuple('abu'), (('a', 'b', weight),)+tuple(e for j, e in enumerate((('a', 'u', Q(2, 3)), ('b', 'u', 3))) if mask >> (j+2) & 1))
            got = combine(passport(*g1), passport(*g2), weight)
            assert got == passport(*glue(g1, g2, weight))
            assert mul(got[0], got[4]) == add(mul(got[1], got[2]), scale(mul(got[3], got[3]), -1))
            shared_count += 1
    # Cofactor signs must survive arbitrary storage orders and a boundary reversal.
    for order in permutations('abcd'):
        state = passport(order, path[1])
        assert state == passport(*path)
        a, b, c, d, e = state
        assert passport(order, path[1], ('b', 'a')) == (a, c, b, d, e)
    third = (tuple('abz'), (('a', 'z', 2), ('z', 'b', 3)))
    s1, s2, s0 = passport(*p3), passport(*q3), passport(*third)
    assert combine(combine(s1, s2), s0) == combine(s1, combine(s2, s0)) == passport(*glue(glue(p3, q3), third))
    # Electrical specialization S(0)=-Lambda on the endpoint boundary of P3.
    assert Q(at(s3[2], 0), at(s3[4], 0)) == -Q(1, 2)
    assert -Q(at(s3[3], 0), at(s3[4], 0)) == Q(1, 2)
    print('PASS: 80 component graphs; Jacobi and independently enumerated rooted forests.')
    print('PASS: 528 edge-disjoint gluings and 48 weighted common-edge gluings; all five coordinates compared with direct minors.')
    print('PASS: path/star counterexample, changed boundary, principal-minor warning, singular xi=2, shared/parallel edges, 24 vertex orders and associativity.')


if __name__ == '__main__':
    main()
