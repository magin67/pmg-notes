"""Exact grove, Schur-complement and boundary resistance checks.

Run: python checks/boundary/verify_spanning_geometry.py
Python 3.10+, standard library, and the first three adjacent boundary checkers.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from verify_forest_states import forests, polynomial
from verify_contraction import laplacian, determinant, inverse, greenian, gram, partitions, join
from verify_pairing import passport, glue, clean


def transpose(a):
    return list(map(list, zip(*a))) if a else []


def multiply(a, b):
    cols = transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in a]


def plus(a, b, sign=1):
    return [[x+sign*y for x,y in zip(row1,row2)] for row1,row2 in zip(a,b)]


def principal(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def relabel(n, edges, boundary):
    order = list(boundary) + [v for v in range(n) if v not in boundary]
    p = {old:new for new,old in enumerate(order)}
    return [(p[u],p[v],w) for u,v,w in edges]


def response(n, edges, k):
    L = laplacian(n, edges)
    A = principal(L, range(k,n))
    top = principal(L, range(k))
    if k < n:
        cross = [[L[i][j] for j in range(k,n)] for i in range(k)]
        reduced = plus(top, multiply(multiply(cross,inverse(A)),transpose(cross)), -1)
    else:
        reduced = top
    H = principal(reduced, range(1,k))
    columns = [tuple(Q(j==i)-Q(j==0) for j in range(n)) for i in range(1,k)]
    G = gram(columns, greenian(L))
    return {'L':L,'delta':determinant(A),'tau':determinant(principal(L,range(1,n))),
            'response':reduced,'H':H,'G':G}


def grove_weights(n, edges, k):
    result = defaultdict(Q)
    for f in forests(range(n), edges, range(k)):
        if not f['internal']:
            result[f['state']] += f['weight']
    return dict(result)


def check_graph(n, edges, k):
    m = response(n,edges,k)
    g = grove_weights(n,edges,k)
    polys = passport(n,edges,k)
    for pi in partitions(tuple(range(k))):
        assert g.get(pi,0) == polys.get(pi,{}).get(n-len(pi),0)
    discrete = tuple((i,) for i in range(k))
    connected = (tuple(range(k)),)
    assert m['delta'] == g[discrete]
    assert m['tau'] == g[connected]
    assert m['tau'] == m['delta']*determinant(m['H'])
    assert m['G'] == inverse(m['H'])
    assert m['delta'] == m['tau']*determinant(m['G'])
    assert all(sum(row)==0 for row in m['response'])
    assert all(m['response'][i][j] <= 0 for i in range(k) for j in range(k) if i!=j)
    # Effective resistances agree after elimination, without identifying Green blocks.
    redgr = greenian(m['response'])
    cols = [tuple(Q(j==i)-Q(j==0) for j in range(k)) for i in range(1,k)]
    assert gram(cols,redgr) == m['G']
    return m,g


def grove_pair(g1,g2,k):
    return sum(x*y for p,x in g1.items() for s,y in g2.items()
               if len(p)+len(s)==k+1 and len(join(p,s))==1)


def check_pair(n1,e1,n2,e2,k,mapping=None):
    mapping = tuple(range(k)) if mapping is None else mapping
    renamed = [(mapping[u] if u<k else u,mapping[v] if v<k else v,w) for u,v,w in e2]
    a,ga=check_graph(n1,e1,k)
    b,gb=check_graph(n2,renamed,k)
    n,edges=glue(n1,e1,n2,e2,k,mapping)
    m,_=check_graph(n,edges,k)
    assert m['response']==plus(a['response'],b['response'])
    assert m['delta']==a['delta']*b['delta']
    assert m['tau']==a['delta']*b['delta']*determinant(plus(a['H'],b['H']))
    assert m['tau']==a['tau']*b['tau']*determinant(plus(a['G'],b['G']))
    assert m['tau']==grove_pair(ga,gb,k)
    assert m['G']==inverse(plus(inverse(a['G']),inverse(b['G'])))
    # One common, non-unit-determinant basis change; no hidden normalization.
    size=k-1
    A=[[Q(i==j) for j in range(size)] for i in range(size)]
    if size:
        A[0][0]=2
    if size>1:
        A[0][1]=1
    def transform(G):
        return multiply(multiply(transpose(A),G),A)
    aa,bb=transform(a['G']),transform(b['G'])
    assert m['tau']==a['tau']*b['tau']*determinant(plus(aa,bb))/determinant(A)**2
    assert transform(m['G'])==inverse(plus(inverse(aa),inverse(bb)))
    return m


def main():
    all_edges=[(a,b,Q(w)) for (a,b),w in zip(combinations(range(4),2),[1,2,3,5,7,11])]
    connected=[]
    single_cases=0
    for mask in range(64):
        edges=[e for j,e in enumerate(all_edges) if mask & (1<<j)]
        if not determinant(principal(laplacian(4,edges),range(1,4))):
            continue
        connected.append(edges)
        for size in range(1,5):
            for B in combinations(range(4),size):
                check_graph(4,relabel(4,edges,B),size)
                single_cases+=1
    assert len(connected)==38 and single_cases==570

    # A reproducible spread of sparse and dense graphs, including K4 itself.
    family=[connected[i] for i in [0,5,10,15,20,25,30,37]]
    pair_cases=0
    for k in range(1,5):
        for e1 in family:
            for e2 in family:
                check_pair(4,e1,4,e2,k)
                pair_cases+=1

    # P5: boundary a,c,e has indices 0,1,2; b,d have indices 3,4.
    path=[(0,3,Q(1)),(3,1,Q(1)),(1,4,Q(1)),(4,2,Q(1))]
    p,g=check_graph(5,path,3)
    assert p['tau']==1 and p['delta']==4
    assert p['G']==[[2,2],[2,4]]
    assert p['response']==[[Q(1,2),Q(-1,2),0],[Q(-1,2),1,Q(-1,2)],[0,Q(-1,2),Q(1,2)]]
    assert g=={((0,),(1,),(2,)):4,((0,1),(2,)):2,((0,),(1,2)):2,((0,1,2),):1}
    joined=check_pair(5,path,5,path,3)
    assert joined['tau']==16 and joined['G']==[[1,1],[1,2]]
    pair_cases+=1
    for permutation in permutations(range(3)):
        check_pair(5,path,4,family[-1],3,permutation)
        pair_cases+=1

    # The same boundary geometry and spanning scale, but different full passports.
    ga=[(0,1,Q(1)),(0,2,Q(1)),(0,3,Q(1))]
    gb=[(0,1,Q(1)),(0,2,Q(2)),(0,3,Q(1,2))]
    ma,groves_a=check_graph(4,ga,2)
    mb,groves_b=check_graph(4,gb,2)
    assert ma['tau']==mb['tau']==ma['delta']==mb['delta']==1
    assert ma['response']==mb['response']==[[1,-1],[-1,1]]
    assert ma['G']==mb['G']==[[1]] and groves_a==groves_b
    pa,pb=passport(4,ga,2),passport(4,gb,2)
    assert pa[((0,),(1,))]=={0:1,1:2,2:1}
    assert pb[((0,),(1,))]=={0:1,1:Q(5,2),2:1}
    assert clean(polynomial(forests(range(4),ga,range(2))))=={0:1,1:3,2:3,3:1}
    assert clean(polynomial(forests(range(4),gb,range(2))))=={0:1,1:Q(7,2),2:Q(7,2),3:1}
    for edges,expected in [(ga,{0:1,1:4,2:5,3:2}),(gb,{0:1,1:Q(9,2),2:6,3:2})]:
        m=check_pair(4,edges,2,[(0,1,Q(1))],2)
        assert m['tau']==2
        assert clean(polynomial(forests(range(4),edges+[(0,1,Q(1))],range(2))))==expected
        pair_cases+=1

    # Four-leaf star versus its electrically equivalent complete boundary graph.
    star=[(i,4,Q(1)) for i in range(4)]
    complete=[(a,b,Q(1,4)) for a,b in combinations(range(4),2)]
    ms,gs=check_graph(5,star,4)
    mc,gc=check_graph(4,complete,4)
    assert ms['response']==mc['response']
    assert ms['delta']==4 and mc['delta']==1
    assert ms['tau']==1 and mc['tau']==Q(1,4)
    assert gs.get(((0,1),(2,3)),0)==0 and gc[((0,1),(2,3))]==Q(1,16)
    # A loop and labelled rational parallel edges do not break the conventions.
    parallel=[(0,1,Q(1,2)),(0,1,Q(3,2)),(1,2,Q(2)),(1,1,Q(7))]
    check_pair(3,parallel,3,parallel,2)
    pair_cases+=1
    check_graph(1,[],1)
    print(f'PASS: {single_cases} connected graph/boundary configurations and {pair_cases} graph-pair configurations.')
    print('Grove extraction, Schur response, tree cofactors, resistance Gram matrices and both gluing formulas agree exactly.')
    print('P5, boundary permutations, basis normalization, empty matrices, loops, parallel edges and both recovery counterexamples passed.')


if __name__=='__main__':
    main()
