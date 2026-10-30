"""Exact checks for the first boundary-forest note (Python 3.10+, stdlib)."""

from collections import Counter, defaultdict
from fractions import Fraction as Q


def forests(vertices, edges, boundary):
    """Enumerate edge-labelled forests; retain isolated vertices explicitly."""
    vertices, boundary = tuple(vertices), tuple(boundary)
    boundary_set = set(boundary)
    assert boundary_set and boundary_set <= set(vertices)
    for mask in range(1 << len(edges)):
        parent = {v: v for v in vertices}

        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v

        selected, weight = [], Q(1)
        for i, (u, v, conductance) in enumerate(edges):
            if not mask & (1 << i):
                continue
            a, b = find(u), find(v)
            if a == b:
                break
            parent[a] = b
            selected.append(i)
            weight *= conductance
        else:
            groups = defaultdict(set)
            for v in vertices:
                groups[find(v)].add(v)
            components = list(groups.values())
            state = tuple(sorted(tuple(v for v in boundary if v in c)
                                 for c in components if c & boundary_set))
            internal = tuple(frozenset(c) for c in components if not c & boundary_set)
            yield {'selected': tuple(selected), 'g': len(selected), 'weight': weight,
                   'state': state, 'internal': internal, 'components': components}


def state_name(state):
    return '|'.join(''.join(block) for block in state)


def state_polynomials(records):
    result = defaultdict(Counter)
    for forest in records:
        result[state_name(forest['state'])][forest['g']] += forest['weight']
    return dict(result)


def polynomial(records):
    result = Counter()
    for forest in records:
        result[forest['g']] += forest['weight']
    return result


def check_layers(vertices, edges, boundary):
    records = list(forests(vertices, edges, boundary))
    polys = state_polynomials(records)
    groves = Counter()
    for forest in records:
        assert len(forest['internal']) == len(vertices) - forest['g'] - len(forest['state'])
        if all(c & set(boundary) for c in forest['components']):
            groves[state_name(forest['state'])] += forest['weight']
    for state, poly in polys.items():
        assert poly[len(vertices) - len(state.split('|'))] == groves[state]
    assert sum((poly for poly in polys.values()), Counter()) == polynomial(records)
    return records


def main():
    vertices, boundary = tuple('abcde'), tuple('ace')
    edges = [(a, b, Q(1)) for a, b in zip(vertices, vertices[1:])]
    records = check_layers(vertices, edges, boundary)
    expected = {'ace': {4: 1}, 'ac|e': {2: 1, 3: 2},
                'a|ce': {2: 1, 3: 2}, 'a|c|e': {0: 1, 1: 4, 2: 4}}
    assert len(records) == 16
    assert state_polynomials(records) == expected
    assert 'ae|c' not in state_polynomials(records)
    assert polynomial(records) == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}
    assert sum(not f['internal'] for f in records) == 9
    assert Counter(state_name(f['state']) for f in records) == {
        'ace': 1, 'ac|e': 3, 'a|ce': 3, 'a|c|e': 9}

    weighted = [(a, b, Q(w)) for (a, b, _), w in zip(edges, [2, 3, 5, 7])]
    wr = check_layers(vertices, weighted, boundary)
    assert state_polynomials(wr) == {
        'ace': {4: 210}, 'ac|e': {2: 6, 3: 72},
        'a|ce': {2: 35, 3: 175}, 'a|c|e': {0: 1, 1: 17, 2: 60}}

    isolated = check_layers(tuple('abcdef'), edges, boundary)
    assert state_polynomials(isolated) == expected
    for original, extended in zip(records, isolated):
        assert len(extended['internal']) == len(original['internal']) + 1
        assert frozenset('f') in extended['internal']

    # The same boundary-labelled partner is used for both paths.
    probe_polys = []
    for path in ('xbydz', 'xbzdy'):
        path_edges = [(u, v, Q(1)) for u, v in zip(path, path[1:])]
        base = check_layers(tuple(path), path_edges, tuple('xyz'))
        assert polynomial(base) == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}
        joined = check_layers(tuple(path), path_edges + [('x', 'y', Q(1))], tuple('xyz'))
        probe_polys.append(polynomial(joined))
    assert probe_polys == [
        {0: 1, 1: 5, 2: 10, 3: 9, 4: 3},
        {0: 1, 1: 5, 2: 10, 3: 10, 4: 5}]

    # Boundary extremes, rational weights, a cycle and parallel edges.
    parallel = [('a', 'b', Q(1, 2)), ('a', 'b', Q(3, 2)), ('b', 'c', Q(2))]
    pr = check_layers(tuple('abcd'), parallel, tuple('ac'))
    assert polynomial(pr) == {0: 1, 1: 4, 2: 4}
    cases = [(vertices, edges, tuple('a')), (vertices, edges, vertices),
             (tuple('abcd'), [('a', 'b', Q(2)), ('b', 'c', Q(3)), ('c', 'a', Q(5))], tuple('ac'))]
    for args in cases:
        check_layers(*args)
    print('PASS: all 16 P5 forests, five states (one zero), nine groves;')
    print('weighted and isolated-vertex examples, both 32-subset gluing checks,')
    print('parallel edges and boundary extremes; exact rational arithmetic.')


if __name__ == '__main__':
    main()
