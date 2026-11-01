"""Exact checks for fixed P6 runners and constant SLR turns; no embedding assumptions."""
from pathlib import Path
from itertools import product
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'checks' / 'isomer-spectra'))
import verify_slr_code as slr
from verify_boundary_transfer import transfer, passport, laplacian, xi, J
import networkx as nx
import sympy as sp

OUT = Path(__file__).resolve().parent
T, U, s1 = slr.transfers()
s0 = sp.Matrix([xi*(xi-2), xi-1, xi-1, -1, 1])
q = sp.Symbol('q')
zero = sp.zeros(5, 1)
expand = lambda a: a.applyfunc(sp.expand)
path = [1, 2, 3, 4, 5, 0]
kernel = {tuple(sorted(e)): 1 for e in zip(path, path[1:])}


def weave(letters, reverse=True):
    """Start with an edge; add only five new path edges each time."""
    g = nx.Graph([(0, 1)])
    boundary = (0, 1)
    for c in letters:
        n = len(g)
        a, b = boundary
        mp = {0: b, 1: a} if reverse else {0: a, 1: b}
        mp.update({k: n+k-2 for k in range(2, 6)})
        fresh = [(mp[i], mp[j]) for i, j in zip(path, path[1:])]
        assert all(not g.has_edge(i, j) for i, j in fresh)
        g.add_edges_from(fresh)
        j = slr.EXIT[c]
        boundary = (mp[j], mp[j+1])
    return g, boundary


def marked_isomorphic(g, bg, h, bh):
    gg, hh = g.copy(), h.copy()
    for graph, boundary in [(gg, bg), (hh, bh)]:
        nx.set_node_attributes(graph, 0, 'mark')
        graph.nodes[boundary[0]]['mark'] = 1
        graph.nodes[boundary[1]]['mark'] = 2
    assert nx.is_isomorphic(gg, hh, node_match=nx.algorithms.isomorphism.categorical_node_match('mark', 0))


def polynomial_action(p, matrix, vector):
    out = sp.zeros(5, 1)
    for coefficient in sp.Poly(p, q).all_coeffs():
        out = expand(matrix*out + coefficient*vector)
    return out


result = {'source_commit': '4fa10ffe176625c864d56f0af6a223ac88317631'}
# Recompute from the runner with NO common edge, rather than reuse the cycle.
for c in 'SLR':
    assert transfer(kernel, 6, (slr.EXIT[c], slr.EXIT[c]+1))*J == U[c]
    assert expand(U[c]*s0-s1) == zero
    assert U[slr.mirror(c)] == J*U[c]*J
assert expand(T[2]*T[2]-U['L']*U['R']) == sp.zeros(5)
result['symbolic_runner_transfers'] = 3
print('PASS: runner transfers and seed', flush=True)

count = 0
for length in range(5):
    for letters in product('SLR', repeat=length):
        u = ''.join(letters)
        g, boundary = weave('S'+u+'S')
        h, _, hb, _ = slr.graph(u)
        marked_isomorphic(g, boundary, h, hb)
        assert len(g) == 4*(length+2)+2 and g.number_of_edges() == 5*(length+2)+1
        count += 1
result['marked_graph_comparisons'] = count
# Fixed nonreversing contacts generate alternating turns, up to global reflection.
for N in range(2, 9):
    for c in 'LR':
        g, _ = weave(c*N, reverse=False)
        u = ''.join(c if i % 2 == 0 else slr.mirror(c) for i in range(N-2))
        h, _, _, _ = slr.graph(u)
        assert nx.is_isomorphic(g, h)
result['nonreversing_alternating_graph_comparisons'] = 14
print('PASS: graph construction and contact ordering', flush=True)

spectral = {}
direct_checks = 0
for c in 'SL':
    M = U[c]
    characteristic = sp.factor(M.charpoly(q).as_expr())
    quartic, rem = sp.div(characteristic, q-1, q)
    assert rem == 0
    quartic = sp.Poly(quartic, q)
    coeff = quartic.all_coeffs()
    assert coeff[0] == coeff[-1] == 1 and coeff[1] == coeff[3]
    expected_a = ((xi**2-6*xi+6)*(xi**2-4*xi+2) if c == 'S'
                  else (xi-3)*(xi-2)*(xi**2-5*xi+2))
    expected_b = (2*(xi-1)*(xi**3-9*xi**2+25*xi-19) if c == 'S'
                  else xi**6-14*xi**5+75*xi**4-192*xi**3+242*xi**2-144*xi+38)
    assert sp.expand(coeff[1]+expected_a) == sp.expand(coeff[2]-expected_b) == 0
    remainder = polynomial_action(quartic.as_expr(), M, s0)
    assert expand((M-sp.eye(5))*remainder) == zero
    if c == 'S':
        assert remainder == zero
    else:
        assert sp.factor(remainder[0]) == -2*xi**2*(xi-3)**2
    state = s0
    states = []
    rooted_values = []
    trees = []
    for N in range(9):
        g, boundary = weave(c*N)
        edges = {tuple(sorted(e)): 1 for e in g.edges}
        L = laplacian(edges, len(g))
        direct = L.charpoly(xi).as_expr()
        assert sp.expand(direct-state[0]) == 0
        if N <= 3:
            assert expand(passport(xi*sp.eye(len(g))-L, boundary)-state) == zero
        rooted = int((sp.eye(len(g))+L).det(method='domain-ge'))
        assert rooted == state[0].subs(xi, -1)
        tau = int(L[1:, 1:].det(method='domain-ge'))
        rooted_values.append(rooted)
        trees.append(tau)
        states.append(state)
        direct_checks += 1
        state = expand(M*state)
    assert all(trees[N+2] == 6*trees[N+1]-trees[N] for N in range(7))
    for N in range(5):
        residual = sum(coeff[j]*states[N+4-j][0] for j in range(5))
        assert sp.expand(residual-remainder[0]) == 0
    hn = 4 if c == 'S' else 5
    hankel = sp.Matrix(hn, hn, lambda i, j: rooted_values[i+j])
    assert hankel.det() != 0
    spectral[c] = {
        'transfer_charpoly': str(characteristic),
        'a': str(sp.factor(-coeff[1])), 'b': str(sp.factor(coeff[2])),
        'quartic_residual': [str(sp.factor(x)) for x in remainder],
        'homogeneous_minimal_order': hn,
        'hankel_at_minus_one': str(hankel.det()),
        'P1_N0_to_N8': rooted_values, 'tau_N0_to_N8': trees,
        'initial_polynomials_N0_to_N3': [str(s[0]) for s in states[:4]],
    }
    print('PASS: symbolic recurrence and direct determinants', c, flush=True)
result['spectral'] = spectral
result['direct_characteristic_polynomial_checks'] = direct_checks
result['direct_full_polynomial_passports'] = 8
result['direct_integer_rooted_and_tree_determinants'] = 2*direct_checks

# Reflection covers R symbolically, and direct graph comparison confirms marks.
for N in range(1, 9):
    g, gb = weave('L'*N)
    h, hb = weave('R'*N)
    marked_isomorphic(g, gb, h, tuple(reversed(hb)))
result['reflection_graph_checks'] = 8

# Periodic runner LR: block-transfer product, independently constructed graph.
block = U['R']*U['L']
for k in range(5):
    g, _ = weave('LR'*k)
    edges = {tuple(sorted(e)): 1 for e in g.edges}
    direct = laplacian(edges, len(g)).charpoly(xi).as_expr()
    assert sp.expand((block**k*s0)[0]-direct) == 0
result['periodic_block_direct_checks'] = 5
result['contact_order_counterexample_N4'] = {
    'SLL_P1': int(slr.state('LL', U, s1)[0].subs(xi, -1)),
    'SLR_P1': int(slr.state('LR', U, s1)[0].subs(xi, -1)),
}
(OUT/'slr-weaving-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('PASS: reflection and periodic block; results saved', flush=True)
