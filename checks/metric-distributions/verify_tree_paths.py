"""Exact path-coordinate, matrix, forest, and finite-variation comparisons.

Run from the repository root: python checks/metric-distributions/verify_tree_paths.py
Only the Python standard library is required.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json

from verify_influence import inverse, reduced_laplacian, vector, pairing, forest_sums, forest_pair


def path_coordinates(n, weights, start, finish):
    """Find the unique path combinatorially, without any metric calculation."""
    adjacency = [[] for _ in range(n)]
    for i, j in weights:
        adjacency[i].append(j)
        adjacency[j].append(i)
    parent = {start: None}
    pending = [start]
    while pending:
        i = pending.pop()
        for j in adjacency[i]:
            if j not in parent:
                parent[j] = i
                pending.append(j)
    result = dict.fromkeys(weights, Q(0))
    j = finish
    while j != start:
        i = parent[j]
        edge = tuple(sorted((i, j)))
        result[edge] = Q(1 if i < j else -1)
        j = i
    return result


def audit_tree(n, weights):
    pairs = list(permutations(range(n), 2))
    vectors = {p: vector(n, p) for p in pairs}
    paths = {p: path_coordinates(n, weights, *p) for p in pairs}
    H = inverse(reduced_laplacian(n, weights))
    tau, forests = forest_sums(n, weights)
    R = {p: value / tau for p, value in forests.items()}
    old = {(p, q): pairing(vectors[p], H, vectors[q]) for p in pairs for q in pairs}
    for e in weights:
        for h in weights:
            assert pairing(vector(n, e), H, vector(n, h)) == (1 / weights[e] if e == h else 0)
    for p in pairs:
        for q in pairs:
            coeff = {e: paths[p][e] * paths[q][e] / c for e, c in weights.items()}
            matrix_coeff = {e: c * pairing(vectors[p], H, vector(n, e)) *
                           pairing(vectors[q], H, vector(n, e)) for e, c in weights.items()}
            assert coeff == matrix_coeff
            assert sum(coeff.values()) == old[p, q] == forest_pair(p, q, R)
            common = {e for e in weights if paths[p][e] and paths[q][e]}
            assert {e for e, m in coeff.items() if m} == common
            assert len({1 if coeff[e] > 0 else -1 for e in common}) <= 1
            assert old[p[::-1], q] == -old[p, q]
            assert old[p[::-1], q[::-1]] == old[p, q]
            if p == q:
                assert all(m >= 0 for m in coeff.values())
    count = 0
    for e, c in weights.items():
        for t in (c, Q(1, 3), -c / 2):
            changed = weights.copy()
            changed[e] += t
            Hnew = inverse(reduced_laplacian(n, changed))
            tau_new, forests_new = forest_sums(n, changed)
            Rnew = {p: value / tau_new for p, value in forests_new.items()}
            assert tau_new == tau * (1 + t / c)
            for p in pairs:
                for q in pairs:
                    m = paths[p][e] * paths[q][e] / c
                    new = pairing(vectors[p], Hnew, vectors[q])
                    assert new == forest_pair(p, q, Rnew)
                    assert new - old[p, q] == -t * m / (c + t)
                    assert bool(new - old[p, q]) == bool(m)
                    count += 1
    # Joint finite changes are separable on a fixed tree.
    changed = {e: c * Q(i + 2, i + 1) for i, (e, c) in enumerate(weights.items())}
    Hnew = inverse(reduced_laplacian(n, changed))
    for p in pairs:
        for q in pairs:
            assert pairing(vectors[p], Hnew, vectors[q]) == sum(
                paths[p][e] * paths[q][e] / c for e, c in changed.items())
    return count


def main():
    path = [(0, 1), (1, 2), (2, 3), (3, 4)]
    weighted = dict(zip(path, map(Q, (3, 2, Q(1, 2), 4))))
    specs = [
        ('unit_path5', 5, dict.fromkeys(path, Q(1))),
        ('weighted_path5', 5, weighted),
        ('weighted_star5', 5, {(0, 1): Q(2), (0, 2): Q(1, 3), (0, 3): Q(4), (0, 4): Q(3, 2)}),
        ('branched_tree6', 6, {(0, 1): Q(2), (1, 2): Q(3), (2, 3): Q(1, 2),
                              (1, 4): Q(5), (2, 5): Q(2, 3)}),
    ]
    counts = {name: audit_tree(n, w) for name, n, w in specs}
    H = inverse(reduced_laplacian(5, weighted))
    v, u = vector(5, (0, 3)), vector(5, (1, 4))
    initial = pairing(v, H, u)
    assert initial == Q(5, 2)
    rows = []
    for e, label in zip(path, ('ab', 'bc', 'cd', 'de')):
        c = weighted[e]
        m = c * pairing(v, H, vector(5, e)) * pairing(u, H, vector(5, e))
        w = weighted.copy()
        w[e] *= 2
        new = pairing(v, inverse(reduced_laplacian(5, w)), u)
        rows.append(dict(edge=label, c=str(c), m=str(m), new_c=str(2 * c),
                         new_value=str(new), change=str(new - initial)))
    assert [r['m'] for r in rows] == ['0', '1/2', '2', '0']
    assert [r['change'] for r in rows] == ['0', '-1/4', '-1', '0']
    output_value = sum(Q(row['m']) / Q(row['c']) for row in rows)
    assert output_value == Q(17, 4)
    # A previously absent chord can affect disjoint paths: do not generalize support.
    chain4 = {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}
    chord_rows = []
    for t in (Q(0), Q(1, 3), Q(1), Q(2)):
        w = chain4.copy()
        w[(0, 3)] = t
        value = pairing(vector(4, (0, 1)), inverse(reduced_laplacian(4, w)), vector(4, (2, 3)))
        tau, forests = forest_sums(4, w)
        assert value == forest_pair((0, 1), (2, 3), {p: f / tau for p, f in forests.items()})
        assert value == -t / (1 + 3 * t)
        chord_rows.append({'t': str(t), 'value': str(value)})
    result = dict(status='passed', graphs=counts, finite_form_comparisons=sum(counts.values()),
                  weighted_initial=str(initial), weighted_probes=rows,
                  weighted_output_value=str(output_value), new_chord=chord_rows)
    Path(__file__).with_name('tree-path-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'status': result['status'], 'graphs': len(counts),
                      'finite_form_comparisons': result['finite_form_comparisons']}))


if __name__ == '__main__':
    main()
