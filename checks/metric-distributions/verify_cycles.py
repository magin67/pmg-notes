"""Exact cycle examples, electrical-flow checks and independent forest audits."""
from fractions import Fraction as Q
from pathlib import Path
import json
from verify_influence import audit_graph, inverse, reduced_laplacian, vector, pairing


def record(n, weights, p, q):
    H = inverse(reduced_laplacian(n, weights))
    v, u = vector(n, p), vector(n, q)
    value = pairing(v, H, u)
    rows = []
    currents = []
    for e, c in weights.items():
        a = vector(n, e)
        Iv, Iu = c * pairing(v, H, a), c * pairing(u, H, a)
        m, R = Iv * Iu / c, pairing(a, H, a)
        changed = weights.copy()
        changed[e] *= 2
        new_value = pairing(v, inverse(reduced_laplacian(n, changed)), u)
        assert new_value - value == -m / (1 + c * R)
        # Reversing the auxiliary edge orientation preserves its contribution.
        backwards = vector(n, e[::-1])
        assert m == c * pairing(v, H, backwards) * pairing(u, H, backwards)
        currents.append((e, Iv, Iu))
        rows.append({'edge': ''.join(chr(97+i) for i in e), 'c': str(c),
                     'Iv': str(Iv), 'Iu': str(Iu), 'm': str(m), 'R': str(R),
                     'doubled_value': str(new_value), 'change': str(new_value - value)})
    # Kirchhoff conservation in incidence convention: sink minus source = vector.
    for pair, which in ((p, 1), (q, 2)):
        balance = [Q(0)] * n
        for row in currents:
            e, current = row[0], row[which]
            balance[e[0]] -= current
            balance[e[1]] += current
        assert balance == [Q(i == pair[1]) - Q(i == pair[0]) for i in range(n)]
    assert sum(Q(r['m']) for r in rows) == value
    return {'v': ''.join(chr(97+i) for i in p), 'u': ''.join(chr(97+i) for i in q),
            'value': str(value), 'output_value': str(sum(Q(r['m']) * Q(r['R']) for r in rows)),
            'edges': rows}


def main():
    tri = {(0, 1): Q(1), (1, 2): Q(1), (0, 2): Q(1)}
    tri2 = dict(tri); tri2[(0, 2)] = Q(2)
    sq = {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1), (0, 3): Q(1)}
    bridge = dict(sq); bridge[(1, 3)] = Q(1)
    asym = dict(bridge); asym[(0, 1)] = Q(2)
    subdivision = {(0, 1): Q(1), (1, 2): Q(1), (0, 3): Q(2), (2, 3): Q(2)}
    graphs = [
        ('unit_triangle', 3, tri), ('reinforced_triangle', 3, tri2),
        ('triangle_235', 3, {(0, 1): Q(2), (1, 2): Q(3), (0, 2): Q(5)}),
        ('unit_square', 4, sq),
        ('square_2357', 4, dict(zip(sq, map(Q, (2, 3, 5, 7))))),
        ('balanced_bridge', 4, bridge), ('unbalanced_bridge', 4, asym),
        ('subdivided_triangle', 4, subdivision),
    ]
    counts = {name: audit_graph(n, weights) for name, n, weights in graphs}
    cases = {
        'triangle': record(3, tri, (0, 2), (0, 2)),
        'reinforced_triangle': record(3, tri2, (0, 2), (0, 2)),
        'square_norm': record(4, sq, (0, 2), (0, 2)),
        'square_mixed': record(4, sq, (0, 2), (1, 3)),
        'balanced_bridge': record(4, bridge, (0, 2), (0, 2)),
        'unbalanced_bridge': record(4, asym, (0, 2), (0, 2)),
        'subdivision': record(4, subdivision, (0, 2), (0, 2)),
    }
    assert [r['m'] for r in cases['triangle']['edges']] == ['1/9', '1/9', '4/9']
    assert [r['m'] for r in cases['reinforced_triangle']['edges']] == ['1/25', '1/25', '8/25']
    assert [r['m'] for r in cases['square_norm']['edges']] == ['1/4'] * 4
    assert [r['m'] for r in cases['square_mixed']['edges']] == ['-1/4', '1/4', '-1/4', '1/4']
    assert [r['change'] for r in cases['square_mixed']['edges']] == ['1/7', '-1/7', '1/7', '-1/7']
    assert cases['square_mixed']['value'] == cases['square_mixed']['output_value'] == '0'
    assert cases['balanced_bridge']['edges'][-1]['m'] == '0'
    # Independent series/parallel calculation for the triangle, with two routes.
    for direct_c, key in ((Q(1), 'triangle'), (Q(2), 'reinforced_triangle')):
        total = direct_c + Q(1, 2)
        current_direct, current_detour = direct_c / total, Q(1, 2) / total
        assert Q(cases[key]['value']) == 1 / total
        assert Q(cases[key]['edges'][0]['Iv']) == current_detour
        assert Q(cases[key]['edges'][2]['Iv']) == current_direct
    # Every old-vertex mixed form is preserved under the degree-two subdivision.
    old_pairs = [(0, 1), (0, 2), (1, 2)]
    for p in old_pairs:
        for q in old_pairs:
            before = record(3, tri, p, q)
            after = record(4, subdivision, p, q)
            assert before['value'] == after['value']
            bm = {r['edge']: Q(r['m']) for r in before['edges']}
            am = {r['edge']: Q(r['m']) for r in after['edges']}
            assert bm['ab'] == am['ab'] and bm['bc'] == am['bc']
            assert bm['ac'] == am['ad'] + am['cd']
            assert am['ad'] == am['cd'] == bm['ac'] / 2
    # Balanced bridge has zero response for arbitrary tested bridge conductance.
    for conductance in (Q(0), Q(1, 3), Q(1), Q(7)):
        weights = dict(sq); weights[(1, 3)] = conductance
        H = inverse(reduced_laplacian(4, weights))
        assert pairing(vector(4, (0, 2)), H, vector(4, (0, 2))) == 1
        assert pairing(vector(4, (0, 2)), H, vector(4, (1, 3))) == 0
    # Joint finite changes are not the sum of independent baseline probes.
    both = dict(sq); both[(0, 1)] = both[(1, 2)] = Q(2)
    joint = pairing(vector(4, (0, 2)), inverse(reduced_laplacian(4, both)), vector(4, (0, 2)))
    assert joint == Q(2, 3)
    assert 1 + sum(Q(r['change']) for r in cases['square_norm']['edges'][:2]) == Q(5, 7)
    result = {'status': 'passed', 'graphs': counts, 'finite_form_comparisons': sum(counts.values()),
              'cases': cases, 'joint_square_value': str(joint), 'incorrect_added_probes': '5/7'}
    Path(__file__).with_name('cycle-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'status': 'passed', 'graphs': len(counts),
                      'finite_form_comparisons': sum(counts.values())}))


if __name__ == '__main__':
    main()
