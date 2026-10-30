"""Exact C01 checks. Python 3.10+, standard library; run without -O."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'checks/boundary'))
from verify_forest_states import forests
from verify_contraction import compatible, determinant, inverse, join


def edge(a, b):
    return tuple(sorted((a, b)))


def cycle(vs):
    return {edge(a, b) for a, b in zip(vs, vs[1:] + vs[:1])}


def hex_pair(start):
    return [[0,1,9,8,7,6], list(range(6)), [start,start+1,13,12,11,10]], [[0,1],[start,start+1]]


def make_chain(sizes, seams, reverse=False):
    cores, joins, nxt = [], [], 0
    for i,m in enumerate(sizes):
        common = []
        if i:
            start = seams[i-2] if i > 1 else 0
            common = cores[-1][start:start+seams[i-1]]
            if reverse:
                common = common[::-1]
            joins.append(common)
        fresh = list(range(nxt, nxt+m-len(common)))
        nxt += len(fresh)
        cores.append(common + fresh)
    return cores,joins


def validate(cores, joins):
    assert cores and len(joins) == len(cores)-1
    assert all(len(c) >= 3 and len(set(c)) == len(c) for c in cores)
    es = [cycle(c) for c in cores]
    for i,j in combinations(range(len(cores)),2):
        common = set(cores[i]) & set(cores[j])
        if j != i+1:
            assert not common, 'nonadjacent cores meet'
            continue
        s = joins[i]
        assert 1 <= len(s) < min(len(cores[i]),len(cores[j]))
        assert len(set(s)) == len(s) and common == set(s)
        shared = {edge(a,b) for a,b in zip(s,s[1:])}
        assert es[i] & es[j] == shared, 'intersection is not the specified path'
        for k in [i,j]:
            assert {e for e in es[k] if set(e) <= common} == shared
    for i in range(1,len(cores)-1):
        assert not (set(joins[i-1]) & set(joins[i]))
    vertices, edges = set().union(*map(set,cores)), set().union(*es)
    visited, pending = set(), [next(iter(vertices))]
    while pending:
        v = pending.pop()
        if v in visited:
            continue
        visited.add(v)
        pending.extend(b if a == v else a for a,b in edges if v in (a,b))
    assert visited == vertices
    assert len(vertices) == sum(map(len,cores))-sum(map(len,joins))
    assert len(edges) == sum(map(len,cores))-sum(len(s)-1 for s in joins)
    assert len(edges)-len(vertices)+1 == len(cores)
    return vertices,edges


def passport(vertices, edges, boundary):
    out = defaultdict(lambda: defaultdict(Q))
    for f in forests(sorted(vertices),[(a,b,Q(1)) for a,b in sorted(edges)],sorted(boundary)):
        out[f['state']][f['g']] += f['weight']
    return {p: dict(v) for p,v in out.items()}


def restrict(state, boundary):
    return tuple(sorted(tuple(v for v in block if v in boundary)
                        for block in state if set(block) & set(boundary)))


def transfer(old, incoming, B, C):
    D = set(B) | set(C)
    out = defaultdict(lambda: defaultdict(Q))
    for pi,p in old.items():
        lifted = tuple(sorted(pi + tuple((v,) for v in C)))
        for sigma,q in incoming.items():
            if not compatible(lifted,sigma,len(D)):
                continue
            eta = restrict(join(lifted,sigma),C)
            for g,x in p.items():
                for h,y in q.items():
                    out[eta][g+h] += x*y
    return {s:dict(p) for s,p in out.items()}


def check_transfer(cores, joins):
    validate(cores,joins)
    vertices,edges = set(cores[0]),cycle(cores[0])
    if not joins:
        return 0
    current = passport(vertices,edges,joins[0])
    steps = 0
    for i in range(1,len(cores)):
        B = set(joins[i-1])
        shared = {edge(a,b) for a,b in zip(joins[i-1],joins[i-1][1:])}
        core_vertices,core_edges = set(cores[i]),cycle(cores[i])-shared
        assert core_vertices & vertices == B
        assert not core_edges & edges
        # All isolated vertices are retained when constructing this passport.
        isolated = core_vertices - {v for e in core_edges for v in e}
        assert isolated == set(joins[i-1][1:-1])
        vertices |= core_vertices
        edges |= core_edges
        if i < len(cores)-1:
            C = set(joins[i])
            incoming = passport(core_vertices,core_edges,B|C)
            predicted = transfer(current,incoming,B,C)
            direct = passport(vertices,edges,C)
            assert predicted == direct
            current = predicted
        else:
            # No new output: keep the input boundary while gluing, then sum states.
            incoming = passport(core_vertices,core_edges,B)
            predicted = defaultdict(Q)
            for p,x in current.items():
                for q,y in incoming.items():
                    if compatible(p,q,len(B)):
                        for g,a in x.items():
                            for h,b in y.items():
                                predicted[g+h] += a*b
            direct = defaultdict(Q)
            for poly in passport(vertices,edges,B).values():
                for g,c in poly.items():
                    direct[g] += c
            assert dict(predicted) == dict(direct)
        steps += 1
    return steps


def laplacian(vertices, edges):
    vs = sorted(vertices)
    ix = {v:i for i,v in enumerate(vs)}
    L = [[Q(0) for _ in vs] for _ in vs]
    for a,b in edges:
        a,b = ix[a],ix[b]
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    return L


def exact_metrics(vertices, edges):
    L = laplacian(vertices,edges)
    n = len(L)
    A = [row[:-1] for row in L[:-1]]
    K = inverse(A)
    d = [K[i][i] for i in range(n-1)]
    rho = sum(d[i]*A[i][j]*d[j] for i in range(n-1) for j in range(n-1))/4
    # Independent centering formula: Gr = (L + 11^T/n)^-1 - 11^T/n.
    Z = inverse([[L[i][j]+Q(1,n) for j in range(n)] for i in range(n)])
    diag = [Z[i][i]-Q(1,n) for i in range(n)]
    centered = sum(diag)/n + sum(diag[i]*L[i][j]*diag[j] for i in range(n) for j in range(n))/4
    assert rho == centered
    return int(determinant(A)), str(rho)


def record(cores, joins):
    vertices,edges = validate(cores,joins)
    return {'cores_cyclic_vertex_order':cores,
            'seams_ordered_identified_vertices':joins,
            'vertices':sorted(vertices),'edges':sorted(edges),
            'n':len(vertices),'edge_count':len(edges)}


def negative_cases():
    # Panel B: both seams meet at vertex 1; cores 1 and 3 also meet there.
    intersecting = [[0,1,9,8,7,6],list(range(6)),[1,2,13,12,11,10]]
    # Panel C: an additional identification of vertex 12 with vertex 7.
    extra = [[0,1,9,8,7,6],list(range(6)),[3,4,13,7,11,10]]
    # Panel D: two induced disjoint edges, not one connected path.
    disconnected = [list(range(8)),[0,1,8,9,4,5,10,11]]
    return [(intersecting,[[0,1],[1,2]]), (extra,[[0,1],[3,4]]),
            (disconnected,[[0,1,4,5]])]


def main():
    report = {'hex_pair':[], 'transfer_cases':[], 'rejected_models':3, 'rejected_examples':[]}
    for start in [3,2]:
        cores,joins = hex_pair(start)
        v,e = validate(cores,joins)
        tau,rho = exact_metrics(v,e)
        degree = {a:sum(a in edge_ for edge_ in e) for a in v}
        d3edges = sum(degree[a] == degree[b] == 3 for a,b in e)
        assert tau == 204 and rho == '43595/41616'
        assert d3edges == (2 if start == 3 else 3)
        data = record(cores,joins)
        data.update(tau=tau,rho=rho,degree3_induced_edges=d3edges)
        report['hex_pair'].append(data)
        report['transfer_cases'].append({'model':record(cores,joins),'steps':check_transfer(cores,joins)})
    cases = [([3],[]),([3,3],[1]),([3,3],[2]),([4,4,4],[2,2]),
             ([5,5,5],[1,2]),([6,6,6],[3,3]),([3,4,5,6],[1,2,3])]
    for sizes,seams in cases:
        for rev in [False,True]:
            cores,joins = make_chain(sizes,seams,rev)
            data = record(cores,joins)
            report['transfer_cases'].append({'model':data,'steps':check_transfer(cores,joins)})
    for cores,joins in negative_cases():
        vertices,edges = set().union(*map(set,cores)),set().union(*(cycle(c) for c in cores))
        report['rejected_examples'].append({
            'cores_cyclic_vertex_order':cores,
            'intended_ordered_contacts':joins,
            'vertices':sorted(vertices),'edges':sorted(edges),
            'pairwise_vertex_intersections':[
                {'core_indices':[i,j], 'vertices':sorted(set(cores[i]) & set(cores[j]))}
                for i,j in combinations(range(len(cores)),2)]})
        try:
            validate(cores,joins)
        except AssertionError:
            pass
        else:
            raise AssertionError('Invalid model accepted')
    # Removing a boundary mark does not remove a component or change its degree.
    p = passport({0,1,2,3},{(0,1),(2,3)},{0,1,2})
    restricted = defaultdict(lambda:defaultdict(Q))
    for state,poly in p.items():
        for g,c in poly.items():
            restricted[restrict(state,{2})][g] += c
    assert {s:dict(p) for s,p in restricted.items()} == passport({0,1,2,3},{(0,1),(2,3)},{2})
    # The loss of the final mark can turn a boundary component into an internal one.
    report['forget_internal_component'] = True
    report['transfer_steps_checked'] = sum(x['steps'] for x in report['transfer_cases'])
    out = Path(__file__).with_name('admissible-chains-results.json')
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"PASS: {len(report['transfer_cases'])} chain configurations; "
          f"{report['transfer_steps_checked']} assembly steps; 3 rejected models; "
          "two exact radius formulas; boundary forgetting.")


if __name__ == '__main__':
    main()
