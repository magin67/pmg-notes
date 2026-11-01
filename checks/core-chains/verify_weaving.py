"""Exact two-contact weaving checks. Python 3.10+, standard library only.

Direct Laplacian minors and independent edge-subset enumeration are compared
with the claimed transfer. All copied edges remain separately labelled.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'checks/boundary'))
from verify_contraction import determinant, inverse, laplacian
from verify_forest_states import forests


def minor(matrix, removed):
    keep = [i for i in range(len(matrix)) if i not in removed]
    return [[matrix[i][j] for j in keep] for i in keep]


def state(n, edges, boundary):
    L = laplacian(n, edges)
    return [determinant(minor(L, {0})),
            determinant(minor(L, set(boundary))) if boundary[0] != boundary[1] else Q(0)]


def forest_state(n, edges, boundary):
    result = [Q(0), Q(0)]
    for f in forests(range(n), edges, boundary):
        if len(f['components']) == 1:
            result[0] += f['weight']
        if len(f['components']) == 2 and len(f['state']) == 2:
            result[1] += f['weight']
    return result


def contract_pair(n, edges, p, q):
    labels = [p[0] if v == p[1] else v for v in range(n)]
    keys = sorted(set(labels))
    mapping = {v: keys.index(labels[v]) for v in range(n)}
    new_edges = [(mapping[u], mapping[v], w) for u, v, w in edges
                 if mapping[u] != mapping[v]]
    return len(keys), new_edges, tuple(mapping[v] for v in q)


def passport(n, edges, p, q):
    L = laplacian(n, edges)
    inv = inverse(minor(L, {n-1}))
    pv = [Q(i == p[1])-Q(i == p[0]) for i in range(n-1)]
    qv = [Q(i == q[1])-Q(i == q[0]) for i in range(n-1)]

    def dot(u, v):
        return sum(u[i]*inv[i][j]*v[j] for i in range(n-1) for j in range(n-1))

    kappa = determinant(minor(L, {n-1}))
    alpha, beta, gamma = dot(pv,pv), dot(qv,qv), dot(pv,qv)
    T = [[kappa*alpha, kappa], [kappa*(alpha*beta-gamma*gamma), kappa*beta]]
    cn, ce, cq = contract_pair(n, edges, p, q)
    assert T == [[state(n,edges,p)[1], kappa],
                 [state(cn,ce,cq)[1], state(n,edges,q)[1]]]
    assert all(x >= 0 for row in T for x in row)
    assert determinant(T) == kappa*kappa*gamma*gamma
    return {'kappa':kappa, 'alpha':alpha, 'beta':beta, 'gamma':gamma,
            'T':T, 'trace':T[0][0]+T[1][1], 'det':determinant(T)}


def apply(T, v):
    return [sum(a*b for a,b in zip(row,v)) for row in T]


def multiply(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def attach(n, edges, boundary, kn, ke, p, q, reverse=False):
    old = boundary[::-1] if reverse else boundary
    mapping = {p[0]: old[0], p[1]: old[1]}
    next_vertex = n
    for v in range(kn):
        if v not in mapping:
            mapping[v] = next_vertex
            next_vertex += 1
    result = list(edges) + [(mapping[u],mapping[v],w) for u,v,w in ke]
    return next_vertex, result, tuple(mapping[v] for v in q)


def path(n, weights=None):
    weights = weights or [Q(1)]*(n-1)
    return [(i,i+1,Q(weights[i])) for i in range(n-1)]


def examples():
    return {
        'square_ladder': (4,path(4),(0,3),(1,2)),
        'hexagon_chain': (6,path(6),(0,5),(2,3)),
        'weighted_path': (4,path(4,[2,3,5]),(0,3),(1,2)),
        'square_with_input_edge': (4,path(4)+[(3,0,Q(1))],(0,1),(3,2)),
        'K4_minus_input_edge': (4,[(u,v,Q(1)) for u,v in combinations(range(4),2)
                                  if (u,v)!=(0,1)],(0,1),(2,3)),
        'triangle_fan': (3,path(3),(0,2),(0,1)),
        'rational_path': (4,path(4,[Q(2,3),Q(5,2),Q(7,4)]),(0,3),(1,2)),
    }


def run():
    report = {'examples': {}, 'exhaustive': {}, 'variable_and_periodic': {}}
    enumerated = direct_checks = subset_checks = 0
    for name, (kn,ke,p,q) in examples().items():
        core = passport(kn,ke,p,q)
        n, edges, boundary = 2, [(0,1,Q(1))], (0,1)
        history = []
        expected = [Q(1),Q(1)]
        for k in range(6):
            actual = state(n,edges,boundary)
            assert expected == actual
            direct_checks += 1
            if k <= 2:
                assert forest_state(n,edges,boundary) == actual
                enumerated += 1
                subset_checks += 1 << len(edges)
            if k >= 2:
                for coord in range(2):
                    assert actual[coord] == core['trace']*history[-1]['state'][coord] - core['det']*history[-2]['state'][coord]
            assert n == 2+k*(kn-2)
            assert len(edges) == 1+k*len(ke)
            history.append({'steps':k,'n':n,'edges':edges,'boundary':boundary,'state':actual})
            expected = apply(core['T'],expected)
            n,edges,boundary = attach(n,edges,boundary,kn,ke,p,q)
        report['examples'][name] = {'n':kn,'edges':ke,'plug':p,'socket':q,
                                     **core,'history':history}

    # All connected simple labelled graphs on four vertices, every unordered
    # input/output pair, and both interface bijections; overlaps are included.
    all_edges = list(combinations(range(4),2))
    pairs = list(combinations(range(4),2))
    count_graphs = count_steps = 0
    seed_edges = [(0,1,Q(2)),(1,2,Q(3)),(2,0,Q(5))]
    seed_state = state(3,seed_edges,(0,2))
    for mask in range(1 << 6):
        ke = [(u,v,Q(1)) for i,(u,v) in enumerate(all_edges) if mask & (1<<i)]
        if not state(4,ke,(0,1))[0]:
            continue
        count_graphs += 1
        for p,q in product(pairs,repeat=2):
            core = passport(4,ke,p,q)
            assert all(x.denominator == 1 for row in core['T'] for x in row)
            assert (core['kappa']*core['gamma']).denominator == 1
            for reverse in [False,True]:
                n,edges,boundary = attach(3,seed_edges,(0,2),4,ke,p,q,reverse)
                assert state(n,edges,boundary) == apply(core['T'],seed_state)
                count_steps += 1
    assert count_graphs == 38 and count_steps == 2736
    report['exhaustive'] = {'connected_kernels':count_graphs,'input_output_pairs_per_kernel':36,
                           'bijections':2,'direct_steps':count_steps}

    # Moving the output edge of a path preserves the two-coordinate tree state.
    T = passport(6,path(6),(0,5),(2,3))['T']
    variable_count = 0
    for word in product([1,2,3],repeat=3):
        n,edges,boundary = 2,[(0,1,Q(1))],(0,1)
        expected = [Q(1),Q(1)]
        for j in word:
            q = (j,j+1)
            assert passport(6,path(6),(0,5),q)['T'] == T
            n,edges,boundary = attach(n,edges,boundary,6,path(6),(0,5),q,True)
            expected = apply(T,expected)
        assert state(n,edges,boundary) == expected == [Q(204),Q(169)]
        variable_count += 1

    # A two-step period becomes one fixed product, with its own recurrence.
    A = examples()['square_ladder']
    B = examples()['hexagon_chain']
    M = multiply(passport(*B)['T'],passport(*A)['T'])
    n,edges,boundary = 2,[(0,1,Q(1))],(0,1)
    periodic = [[Q(1),Q(1)]]
    for k in range(1,5):
        for kn,ke,p,q in [A,B]:
            n,edges,boundary = attach(n,edges,boundary,kn,ke,p,q)
        actual = state(n,edges,boundary)
        assert actual == apply(M,periodic[-1])
        periodic.append(actual)
        if k>=2:
            assert actual[0] == (M[0][0]+M[1][1])*periodic[-2][0]-determinant(M)*periodic[-3][0]
    report['variable_and_periodic'] = {'variable_hexagon_words':variable_count,
                                      'period_matrix':M,'period_states':periodic}
    report['checks'] = {'example_direct_minors':direct_checks,'independent_forest_graphs':enumerated,
                        'enumerated_edge_subsets':subset_checks}
    def encode(value):
        if isinstance(value,Q):
            return int(value) if value.denominator==1 else str(value)
        if isinstance(value,dict):
            return {k:encode(v) for k,v in value.items()}
        if isinstance(value,(list,tuple)):
            return [encode(v) for v in value]
        return value
    out = Path(__file__).with_name('weaving-results.json')
    out.write_text(json.dumps(encode(report),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed',**report['checks'],**report['exhaustive']},ensure_ascii=False))
    for name,ex in report['examples'].items():
        print(name, 'T =',ex['T'],'tau =',[v['state'][0] for v in ex['history']])


if __name__ == '__main__':
    run()
