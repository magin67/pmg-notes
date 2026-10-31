"""Exact checks of vertex identifications, cyclic strips, and prism closures."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

from verify_admissible_chains import cycle, determinant, edge, inverse, laplacian
from verify_matroid_invariance import direct_metrics, multiply
from verify_invariance_limits import rank


def cheb(N, z, second=False):
    a, b = Q(1), (2*z if second else z)
    if N == 0:
        return a
    for _ in range(1, N):
        a, b = b, 2*z*b-a
    return b


def quotient(vertices, edges, cores, identification, duplicated, name):
    """Retain one edge per prescribed seam, without summing conductances."""
    target = {v: identification.get(v, v) for v in vertices}
    ids = {v: i for i, v in enumerate(sorted(set(target.values())))}
    mp = {v: ids[target[v]] for v in vertices}
    images = [edge(mp[a], mp[b]) for a, b in sorted(edges)]
    assert all(a != b for a, b in images)
    counts = Counter(images)
    duplicate_images = {edge(mp[a], mp[b]) for a, b in duplicated}
    assert {e for e, count in counts.items() if count == 2} == duplicate_images
    assert all(count <= 2 for count in counts.values())
    final_edges = set(images)
    n = len(ids)
    assert rank(range(n), final_edges) == n-1
    final_cores = [[mp[v] for v in core] for core in cores]
    assert all(len(c) == len(set(c)) for c in final_cores)
    # This is C^T L_H C, with one copy of the terminal seam removed first.
    H = edges-set(duplicated)
    assert len(H) == len(final_edges)
    LH = laplacian(set(vertices), sorted(H))
    push = [[0]*n for _ in range(n)]
    for a in vertices:
        for b in vertices:
            push[mp[a]][mp[b]] += LH[a][b]
    L, R, tau, rho, d, alpha = direct_metrics(set(range(n)), sorted(final_edges))
    assert push == L
    # Keeping both seam copies gives a different weighted network.
    bad = laplacian(set(range(n)), images)
    extra = laplacian(set(range(n)), sorted(duplicate_images))
    assert bad == [[L[i][j]+extra[i][j] for j in range(n)] for i in range(n)]
    intersections = []
    for i, j in combinations(range(len(cores)), 2):
        shared = set(final_cores[i]) & set(final_cores[j])
        if shared:
            intersections.append({'cores': [i, j], 'vertices': sorted(shared),
                                 'edges': sorted(e for e in final_edges if set(e) <= shared)})
    rec = dict(name=name, N=len(cores), n=n, E=len(final_edges), beta=len(final_edges)-n+1,
               open_vertices=list(vertices), open_edges=sorted(edges), open_core_vertex_maps=cores,
               terminal_identification=sorted(identification.items()),
               removed_duplicate_edges=sorted(duplicated), quotient_map=[mp[v] for v in vertices],
               core_vertex_maps=final_cores, actual_intersections=intersections,
               vertices=list(range(n)), edges=sorted(final_edges), tau=tau, rho=str(rho),
               rho_decimal=float(rho), degree_counts=sorted(Counter(Counter(v for e in final_edges for v in e).values()).items()),
               resistances_to_vertex_zero=list(map(str, d)), circumcenter_weights=list(map(str, alpha)))
    return rec, L, R


def check_seams(rec, expected):
    actual = {tuple(x['cores']): (set(x['vertices']), set(map(tuple, x['edges'])))
              for x in rec['actual_intersections']}
    assert actual == expected


def contraction_test(rec):
    """Compare boundary-state compatibility and forests of the actual quotient."""
    N = rec['N']
    boundary = [0, 1, 2*N, 2*N+1]
    es = sorted(set(map(tuple, rec['open_edges']))-set(map(tuple, rec['removed_duplicate_edges'])))
    mp = rec['quotient_map']
    sigma = [[0, 2], [1, 3]] if not rec['twist'] else [[0, 3], [1, 2]]
    sigma_edges = [tuple(block) for block in sigma]
    direct = [0]*rec['n']
    tested = [0]*rec['n']
    passport = {}
    for mask in range(1 << len(es)):
        chosen = [e for i, e in enumerate(es) if mask >> i & 1]
        g = len(chosen)
        final = [edge(mp[a], mp[b]) for a, b in chosen]
        if rank(range(rec['n']), final) == g:
            direct[g] += 1
        if rank(rec['open_vertices'], chosen) != g:
            continue
        # Recover the partition from connectivity of the open forest.
        parent = list(rec['open_vertices'])
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        for a, b in chosen:
            parent[find(a)] = find(b)
        blocks = {}
        for i, v in enumerate(boundary):
            blocks.setdefault(find(v), []).append(i)
        state = tuple(sorted(map(tuple, blocks.values())))
        pi_edges = [(block[0], v) for block in state for v in block[1:]]
        compatible = rank(range(4), pi_edges+sigma_edges) == (4-len(state))+2
        passport.setdefault(state, Counter())[g] += 1
        if compatible:
            tested[g] += 1
    assert tested == direct and direct[-1] == rec['tau']
    rec.update(contraction_subsets=1 << len(es), ordinary_forest_coefficients=direct,
               boundary_states_checked=len(passport))


def strip(N, p=1, q=None, twist=False):
    q = p if q is None else q
    assert N >= 3 and p >= 1 and q >= 1
    es = {(2*i, 2*i+1) for i in range(N+1)}
    fresh = 2*(N+1)
    paths, cores = [], []
    for i in range(N):
        pair = []
        for row, length in enumerate((p, q)):
            path = [2*i+row]+list(range(fresh, fresh+length-1))+[2*(i+1)+row]
            fresh += length-1
            es.update(edge(a, b) for a, b in zip(path, path[1:]))
            pair.append(path)
        paths.append(pair)
        cores.append(pair[0]+list(reversed(pair[1])))
    assert len(es) == N*(p+q+1)+1 and fresh == N*(p+q)+2
    # Check the open construction before the terminal identification.
    for i, j in combinations(range(N), 2):
        want = {2*j, 2*j+1} if j == i+1 else set()
        assert set(cores[i]) & set(cores[j]) == want
    ident = {2*N: int(twist), 2*N+1: 1-int(twist)}
    rec, L, R = quotient(range(fresh), es, cores, ident, {(2*N, 2*N+1)},
                          f'strip_N{N}_p{p}_q{q}_twist{int(twist)}')
    mp = rec['quotient_map']
    final_paths = [[[mp[v] for v in path] for path in pair] for pair in paths]
    rec.update(p=p, q=q, twist=twist, cell_size=p+q+2, rail_paths=final_paths,
               core_cycles=rec['core_vertex_maps'])
    assert rec['n'] == N*(p+q) and rec['E'] == N*(p+q+1) and rec['beta'] == N+1
    expected = {(i, i+1): ({2*i+2, 2*i+3}, {(2*i+2, 2*i+3)}) for i in range(N-1)}
    expected[0, N-1] = ({0, 1}, {(0, 1)})
    check_seams(rec, expected)
    assert set().union(*(cycle(c) for c in rec['core_cycles'])) == set(map(tuple, rec['edges']))
    if p == q:
        ell = p
        c = Q(1, ell)
        expected_tau = N*ell*(cheb(N, ell+1)+(1 if twist else -1))
        assert rec['tau'] == expected_tau
        # Exact Schur reduction of every internal path; its determinant scale is essential.
        k = 2*N
        W = [[Q(0)]*k for _ in range(k)]
        for i in range(N):
            for a, b, w in [(2*i, 2*i+1, Q(1))]+[(pair[0], pair[-1], c) for pair in final_paths[i]]:
                W[a][a] += w; W[b][b] += w; W[a][b] -= w; W[b][a] -= w
        if ell > 1:
            D = [row[k:] for row in L[k:]]
            B = [row[k:] for row in L[:k]]
            correction = multiply(multiply(B, inverse(D)), list(map(list, zip(*B))))
            reduced = [[Q(L[i][j])-correction[i][j] for j in range(k)] for i in range(k)]
            assert reduced == W and determinant(D) == ell**(2*N)
        assert determinant([row[1:] for row in W[1:]])*ell**(2*N) == rec['tau']
        # Symmetric and antisymmetric blocks of the reduced graph.
        B0 = [[Q(0)]*N for _ in range(N)]
        B1 = [[Q(0)]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                B0[i][j] = W[2*i][2*j]+W[2*i][2*j+1]
                B1[i][j] = W[2*i][2*j]-W[2*i][2*j+1]
                assert B0[i][j] == W[2*i+1][2*j]+W[2*i+1][2*j+1]
                assert -B1[i][j] == W[2*i+1][2*j]-W[2*i+1][2*j+1]
        assert determinant(B1) == 2*c**N*(cheb(N, ell+1)+(1 if twist else -1))
        invB1 = inverse(B1)
        assert sum(invB1[i][i] for i in range(N)) == Q(N, 2*c)*cheb(N-1, ell+1, True)/(cheb(N, ell+1)+(1 if twist else -1))
        rec.update(reduced_conductance=str(c), internal_determinant=ell**(2*N),
                   chebyshev_tau=int(expected_tau), symmetric_block=[[str(x) for x in r] for r in B0],
                   antisymmetric_block=[[str(x) for x in r] for r in B1])
        if ell == 1:
            expected_rho = Q(N*N-1, 24*N)+cheb(N-1, 2, True)/(4*(cheb(N, 2)+(1 if twist else -1)))
            assert Q(rec['rho']) == expected_rho
            assert all(Q(x) == Q(1, 2*N) for x in rec['circumcenter_weights'])
            # Shift along the two rails (exchanging them at the twisted seam) is transitive with row swap.
            shift = {2*i+r: (2*(i+1)+r if i < N-1 else (1-r if twist else r)) for i in range(N) for r in (0, 1)}
            flip = {2*i+r: 2*i+1-r for i in range(N) for r in (0, 1)}
            final_es = set(map(tuple, rec['edges']))
            for perm in (shift, flip):
                assert {edge(perm[a], perm[b]) for a, b in final_es} == final_es
            rec['chebyshev_rho'] = str(expected_rho)
            if N in (3,4):
                contraction_test(rec)
    return rec


def prism_closure(N, m, shift):
    assert N >= 3 and m >= 3 and 0 <= shift < m
    bases = [list(range(i*m, (i+1)*m)) for i in range(N+1)]
    es = set().union(*(cycle(base) for base in bases))
    es.update((i*m+j, (i+1)*m+j) for i in range(N) for j in range(m))
    cores = [bases[i]+bases[i+1] for i in range(N)]
    rec, L, R = quotient(range((N+1)*m), es, cores,
                        {N*m+j: (j+shift)%m for j in range(m)}, cycle(bases[-1]),
                        f'prisms_N{N}_m{m}_r{shift}')
    expected = {(i, i+1): (set(bases[i+1]), cycle(bases[i+1])) for i in range(N-1)}
    expected[0, N-1] = (set(bases[0]), cycle(bases[0]))
    check_seams(rec, expected)
    assert rec['n'] == N*m and rec['E'] == 2*N*m and rec['degree_counts'] == [(4, N*m)]
    assert all(Q(x) == Q(1, N*m) for x in rec['circumcenter_weights'])
    # Evaluate the Chebyshev product exactly through the transverse cyclic-shift matrix.
    # A=2T_0(Z), B=2T_1(Z), Z=2I-(S+S^-1)/2. No floating point roots of unity.
    S = [[int(j == (i+1)%m) for j in range(m)] for i in range(m)]
    C = [[4*int(i == j)-S[i][j]-S[j][i] for j in range(m)] for i in range(m)]
    A = [[2*int(i == j) for j in range(m)] for i in range(m)]
    B = C
    for _ in range(1, N):
        product = multiply(C, B)
        A, B = B, [[product[i][j]-A[i][j] for j in range(m)] for i in range(m)]
    M = [[B[i][j]-int(j == (i+shift)%m)-int(j == (i-shift)%m) for j in range(m)] for i in range(m)]
    assert all(sum(row) == 0 for row in M)
    assert N*determinant([row[1:] for row in M[1:]]) == rec['tau']
    rec.update(base_size=m, shift=shift, chebyshev_product_matrix=M)
    return rec


def lattice_ring(rec):
    """Independent hexagonal-lattice construction and an explicit isomorphism."""
    corners = [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
    centers = [(1,1),(-1,2),(-2,1),(-1,-1),(1,-2),(2,-1)]
    ids, cores = {}, []
    for x, y in centers:
        ps = [(x+a, y+b) for a, b in corners]
        for v in ps:
            if v not in ids:
                ids[v] = len(ids)
        cores.append([ids[v] for v in ps])
    es = set().union(*(cycle(c) for c in cores))
    adj = {v: set() for v in ids.values()}
    for a, b in es:
        adj[a].add(b); adj[b].add(a)
    inner = [ids[v] for v in corners]
    outer = [next(iter(adj[v]-set(inner))) for v in inner]
    mp = {2*i: inner[i] for i in range(6)} | {2*i+1: outer[i] for i in range(6)}
    for i in range(6):
        a, b = outer[i], outer[(i+1)%6]
        candidates = [[a,x,y,b] for x in adj[a]-set(inner) for y in adj[x]-{a} if b in adj[y]]
        assert len(candidates) == 1
        for u, v in zip(rec['rail_paths'][i][1], candidates[0]):
            assert u not in mp or mp[u] == v
            mp[u] = v
    assert len(mp) == len(set(mp.values())) == 24
    assert {edge(mp[a],mp[b]) for a,b in rec['edges']} == es
    rec.update(lattice_coordinates=[list(v) for v, _ in sorted(ids.items(), key=lambda x:x[1])],
               lattice_core_cycles=cores, lattice_edges=sorted(es), strip_to_lattice=[mp[i] for i in range(24)])


def main():
    records = []
    for N in (3,4,5,6):
        for ell in (1,2,3):
            pair = [strip(N, ell, twist=t) for t in (False, True)]
            assert pair[1]['tau']-pair[0]['tau'] == 2*N*ell
            if ell == 1:
                assert Q(pair[0]['rho']) > Q(pair[1]['rho'])
            records.extend(pair)
    ring = strip(6, 1, 3)
    lattice_ring(ring)
    assert ring['tau'] == 176400 and ring['rho'] == '4745753/4233600'
    records.append(ring)
    for N,m in ((3,3),(4,4),(3,5)):
        family = [prism_closure(N,m,r) for r in range(m)]
        for r in range(1,m):
            assert family[r]['tau'] > family[0]['tau']
            assert (family[r]['tau'],family[r]['rho']) == (family[m-r]['tau'],family[m-r]['rho'])
            inv = {i*m+j: i*m+(-j)%m for i in range(N) for j in range(m)}
            assert {edge(inv[a],inv[b]) for a,b in family[r]['edges']} == set(map(tuple,family[m-r]['edges']))
        records.extend(family)
    expected = {
        'strip_N4_p1_q1_twist0': (384, '29/96'),
        'strip_N4_p1_q1_twist1': (392, '67/224'),
        'strip_N6_p1_q1_twist0': (8100, '31/80'),
        'strip_N6_p1_q1_twist1': (8112, '725/1872'),
        'strip_N6_p2_q2_twist0': (235200, '1339547/1411200'),
        'strip_N6_p2_q2_twist1': (235224, '99229/104544'),
        'prisms_N4_m4_r0': (42467328, '103/384'),
        'prisms_N4_m4_r1': (43507216, '28133/105536'),
        'prisms_N4_m4_r2': (44255232, '713/2688')}
    for rec in records:
        if rec['name'] in expected:
            assert (rec['tau'], rec['rho']) == expected[rec['name']], (rec['name'],rec['tau'],rec['rho'])
        print(rec['name'],rec['n'],rec['E'],rec['tau'],rec['rho'],flush=True)
    result = {'graph_count':len(records), 'graphs':records,
              'scope':'Exact finite checks, two independent radius calculations, explicit quotient maps. General proofs are in the note.'}
    Path(__file__).with_name('closure-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Verified',len(records),'closed graphs and all terminal edge-identification corrections.')


if __name__ == '__main__':
    main()
