"""Exact graph, dual-rank, forest, radius and spectrum checks; standard library."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
import json

from verify_admissible_chains import (
    cycle, determinant, edge, hex_pair, inverse, laplacian, record, validate,
)


def configuration(sizes, seams, starts, reverse):
    """A local cyclic order starts with the input seam; names specify gluing."""
    cores, joins, fresh = [], [], 0
    for i, size in enumerate(sizes):
        shared = []
        if i:
            shared = cores[-1][starts[i-1]:starts[i-1]+seams[i-1]]
            if reverse[i-1]:
                shared = shared[::-1]
            joins.append(shared)
        new = list(range(fresh, fresh+size-len(shared)))
        fresh += len(new)
        cores.append(shared+new)
    validate(cores, joins)
    return cores, joins


def dual_data(cores, joins):
    """Keep one separately labelled dual edge per original edge; 0 is exterior."""
    vertices, edges = validate(cores, joins)
    memberships = defaultdict(list)
    for i, core in enumerate(cores, 1):
        for e in cycle(core):
            memberships[e].append(i)
    dual = {e: tuple([0]+fs) if len(fs) == 1 else tuple(fs)
            for e, fs in memberships.items()}
    assert all(len(pair) == 2 for pair in dual.values())
    multiplicities = Counter(dual.values())
    lengths = [0]+[len(s)-1 for s in joins]+[0]
    expected = Counter({(0, i): len(c)-lengths[i-1]-lengths[i]
                        for i, c in enumerate(cores, 1)})
    expected.update({(i, i+1): lengths[i] for i in range(1, len(cores)) if lengths[i]})
    assert multiplicities == expected
    ordered = sorted(edges, key=lambda e: (dual[e], e))
    return vertices, ordered, [dual[e] for e in ordered], multiplicities


def components(n, edges, mask):
    parent = list(range(n))
    sizes = [1]*n
    rank = 0
    for i, (a, b) in enumerate(edges):
        if not mask >> i & 1:
            continue
        while parent[a] != a:
            a = parent[a]
        while parent[b] != b:
            b = parent[b]
        if a != b:
            if sizes[a] < sizes[b]:
                a, b = b, a
            parent[b] = a
            sizes[a] += sizes[b]
            rank += 1
    return rank, [sizes[i] for i in range(n) if parent[i] == i]


def enumerate_subsets(n, edges, N, dual):
    """Test the full dual rank identity, not only equality of tree counts."""
    total = 1 << len(edges)
    ranks = bytearray(total)
    ordinary, rooted = [0]*n, [0]*n
    inclusion = [0]*len(edges)
    trees = 0
    for mask in range(total):
        rank, sizes = components(n, edges, mask)
        dual_rank, _ = components(N+1, dual, total-1-mask)
        g = mask.bit_count()
        assert rank == g+dual_rank-N, (mask, rank, dual_rank)
        ranks[mask] = rank
        if rank != g:
            continue
        ordinary[g] += 1
        rooted[g] += prod(sizes)
        if rank == n-1:
            trees += 1
            assert dual_rank == N and len(edges)-g == N
            for i in range(len(edges)):
                inclusion[i] += mask >> i & 1
    return ordinary, rooted, inclusion, trees, ranks


def multiply(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def rooted_from_laplacian(L):
    """Newton identities for det(I+tL), independent of forest enumeration."""
    n = len(L)
    power = [[Q(i == j) for j in range(n)] for i in range(n)]
    traces, coefficients = [0], [Q(1)]
    for k in range(1, n+1):
        power = multiply(power, L)
        traces.append(sum(power[i][i] for i in range(n)))
        coefficients.append(sum((-1)**(j-1)*coefficients[k-j]*traces[j]
                                for j in range(1, k+1))/k)
    assert coefficients[-1] == 0
    assert all(v.denominator == 1 for v in coefficients)
    return [int(v) for v in coefficients[:-1]]


def direct_metrics(vertices, edges):
    """Two separate inversions and the equal-distance equations for the sphere."""
    L = laplacian(vertices, edges)
    n = len(L)
    A = [row[1:] for row in L[1:]]
    K = inverse(A)
    d = [Q(0)]+[K[i][i] for i in range(n-1)]
    rho_energy = sum(d[i]*L[i][j]*d[j] for i in range(n) for j in range(n))/4
    Z = inverse([[L[i][j]+Q(1, n) for j in range(n)] for i in range(n)])
    Gr = [[Z[i][j]-Q(1, n) for j in range(n)] for i in range(n)]
    R = [[Gr[i][i]+Gr[j][j]-2*Gr[i][j] for j in range(n)] for i in range(n)]
    assert [R[i][0] for i in range(n)] == d
    # R alpha = c 1 and sum(alpha)=1 characterize the circumcenter; c=2 rho.
    bordered = [row+[Q(-1)] for row in R]+[[Q(1)]*n+[Q(0)]]
    solution = [row[-1] for row in inverse(bordered)]
    alpha, c = solution[:-1], solution[-1]
    assert sum(alpha) == 1
    assert all(sum(R[i][j]*alpha[j] for j in range(n)) == c for i in range(n))
    assert c/2 == rho_energy
    for q in range(n):
        rq = [R[i][q] for i in range(n)]
        assert sum((rq[a]-rq[b])**2 for a, b in edges)/4 == rho_energy
    return L, R, int(determinant(A)), rho_energy, d, alpha


def inspect(cores, joins):
    vertices, edges, dual, multiplicities = dual_data(cores, joins)
    n, N = len(vertices), len(cores)
    f, p, counts, tree_count, ranks = enumerate_subsets(n, edges, N, dual)
    L, R, tau, rho, d, alpha = direct_metrics(vertices, edges)
    assert f[-1] == tau == tree_count
    assert p == rooted_from_laplacian(L)
    edge_r = [R[a][b] for a, b in edges]
    assert edge_r == [Q(count, tau) for count in counts]
    H2 = sum(x*x for x in edge_r)
    assert rho == Q(f[-2], 3*tau)-H2/12
    H = laplacian(set(range(N+1)), dual)
    assert determinant([row[1:] for row in H[1:]]) == tau
    degree = Counter(v for e in edges for v in e)
    degree3 = sorted(v for v in vertices if degree[v] == 3)
    induced = [e for e in edges if set(e) <= set(degree3)]
    result = record(cores, joins)
    result.update(
        dual_vertex_zero_is_exterior=True,
        dual_bundles=[{'faces':list(k), 'multiplicity':v} for k, v in sorted(multiplicities.items())],
        edge_dual_correspondence=[{'edge':e, 'dual_endpoints':h} for e, h in zip(edges, dual)],
        subsets_checked=len(ranks), rank_signature_sha256=sha256(ranks).hexdigest(),
        ordinary_forest_coefficients=f, rooted_forest_coefficients=p,
        characteristic_coefficients_descending=[(-1)**i*v for i, v in enumerate(p)]+[0],
        spanning_tree_edge_counts=counts, edge_resistances=list(map(str, edge_r)),
        tau=tau, rho=str(rho), H2=str(H2), two_forest_count=f[-2],
        resistances_to_vertex_zero=list(map(str, d)), circumcenter_weights=list(map(str, alpha)),
        kirchhoff_index=str(sum(R[a][b] for a, b in combinations(range(n), 2))),
        degree3_vertices=degree3, degree3_induced_edges=induced,
    )
    return result, ranks


def main():
    pairs, pair_ranks = [], []
    for start in [3, 2]:
        r, ranks = inspect(*hex_pair(start))
        assert r['tau'] == 204 and r['rho'] == '43595/41616'
        assert len(r['degree3_induced_edges']) == (2 if start == 3 else 3)
        pairs.append(r); pair_ranks.append(ranks)
    assert pair_ranks[0] == pair_ranks[1]
    assert pairs[0]['ordinary_forest_coefficients'] == pairs[1]['ordinary_forest_coefficients']
    assert pairs[0]['rooted_forest_coefficients'] != pairs[1]['rooted_forest_coefficients']
    witnesses = []
    for a, b in zip(pairs[0]['edge_dual_correspondence'], pairs[1]['edge_dual_correspondence']):
        assert a['dual_endpoints'] == b['dual_endpoints']
        witnesses.append({'edge_A':a['edge'], 'edge_B':b['edge'], 'dual_endpoints':a['dual_endpoints']})
    cases = []
    families = [
        ([3], [], [([], [])]),
        ([4,5,4], [1,1], [([0,1],[False,False]), ([0,3],[True,True])]),
        ([5,6,5], [2,2], [([0,2],[False,False]), ([0,4],[True,False])]),
        ([6,6,6], [3,3], [([0,3],[False,False]), ([0,3],[True,True])]),
        ([3,4,5,6], [1,2,3], [([0,1,2],[False]*3), ([0,2,2],[True,False,True])]),
    ]
    for sizes, seams, variants in families:
        reference = None
        for starts, reverse in variants:
            r, ranks = inspect(*configuration(sizes, seams, starts, reverse))
            if reference is not None:
                assert ranks == reference
            reference = ranks
            cases.append(r)
    report = {'hex_pair':pairs, 'hex_pair_edge_bijection':witnesses,
              'additional_configurations':cases,
              'total_configurations':len(pairs)+len(cases),
              'total_edge_subsets_checked':sum(r['subsets_checked'] for r in pairs+cases),
              'scope':'Finite exact checks support the examples; the general theorem is proved in the note.'}
    Path(__file__).with_name('matroid-invariance-results.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('PASS:', report['total_configurations'], 'configurations;',
          report['total_edge_subsets_checked'], 'edge subsets; dual ranks, forests, direct radii and spectra.')
    for name, r in zip(['A', 'B'], pairs):
        print(name, json.dumps({key:r[key] for key in ['tau','rho','two_forest_count','H2',
            'rooted_forest_coefficients','ordinary_forest_coefficients','kirchhoff_index']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
