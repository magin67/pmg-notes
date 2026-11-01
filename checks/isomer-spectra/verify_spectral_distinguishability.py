"""Independent integer Laplacian moments and partial reconstruction."""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json
import random
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'checks/isomer-spectra'))
import verify_slr_code as slr
from verify_boundary_transfer import laplacian, xi, J
from catalog_spectral_values import value

OUT=Path(__file__).resolve().parent

def traces(graph,K=8):
    n=len(graph);deg=[graph.degree(i) for i in range(n)]
    adjacent=[list(graph[i]) for i in range(n)]
    M=[[int(i==j) for j in range(n)] for i in range(n)]
    answer=[]
    for _ in range(K):
        M=[[row[j]*deg[j]-sum(row[k] for k in adjacent[j]) for j in range(n)] for row in M]
        answer.append(sum(M[i][i] for i in range(n)))
    return answer

data=[];count=0;polynomial_count=0;integer_det_count=0
T,U,initial=slr.transfers()
R=sp.diag(1,-1,-1,-1,1)
V={c:R*M.subs(xi,-1)*R for c,M in U.items()}
start=R*initial.subs(xi,-1)
for m in range(7):
    for letters in product('SLR',repeat=m):
        u=''.join(letters);N=m+2
        graph,_,_,edges=slr.graph(u)
        b=sum(c!='S' for c in u)
        h=sum(a==c and a!='S' for a,c in zip(u,u[1:]))
        deg=dict(graph.degree())
        assert sum(d==2 for d in deg.values())==2*N+4
        assert sum(d==3 for d in deg.values())==2*N-2
        edge_types={pair:sum(tuple(sorted((deg[a],deg[c])))==pair for a,c in graph.edges)
                    for pair in [(2,2),(2,3),(3,3)]}
        assert edge_types=={(2,2):6+b,(2,3):4*N-4-2*b,(3,3):N-1+b}
        Sv={v:sum(deg[w] for w in graph[v]) for v in graph}
        assert sum(x*x for x in Sv.values())==170*N-78+8*b+2*h
        tr=traces(graph)
        expected=[10*N+2,36*N,148*N-28,648*N-228+4*b,
                  2940*N-1428+60*b,13656*N-8112+576*b+6*h]
        assert tr[:6]==expected,(u,tr,expected)
        z=start
        for c in u+'S':z=V[c]*z
        assert z[0]==value(u)
        if slr.canonical(u)==u:
            data.append({'code':'S'+u,'N':N,'b':b,'h':h,'traces':tr,'P1':value(u)})
            if N<=6:
                L=laplacian(edges,len(graph));poly=L.charpoly(xi).as_expr()
                assert poly.subs(xi,-1)==value(u)
                assert (sp.eye(len(graph))+L).det(method='domain-ge')==value(u)
                polynomial_count+=1;integer_det_count+=1
        count+=1
    print('PASS moments, all words: N=',N,flush=True)

rng=random.Random(19601)
samples=[]
for N in range(7,19):
    for u in ['S'*(N-2),'L'*(N-2),''.join(rng.choices('SLR',k=N-2))]:
        graph,_,_,edges=slr.graph(u);L=laplacian(edges,len(graph))
        determinant=(sp.eye(len(graph))+L).det(method='domain-ge')
        assert determinant==value(u)
        integer_det_count+=1
        samples.append({'code':'S'+u,'P1':value(u)})

examples={}
for ua,ub in [('LL','LR'),('SL','LS'),('LSL','LRL'),('SLL','LSL'),('SSL','SLS'),('LSLL','LLSR')]:
    ga,_,_,ea=slr.graph(ua);gb,_,_,eb=slr.graph(ub)
    ca=laplacian(ea,len(ga)).charpoly(xi).as_expr()
    cb=laplacian(eb,len(gb)).charpoly(xi).as_expr()
    diff=sp.Poly(ca-cb,xi)
    expected_grade={('LL','LR'):6,('SL','LS'):None,('LSL','LRL'):4,
                    ('SLL','LSL'):6,('SSL','SLS'):8,('LSLL','LLSR'):10}[(ua,ub)]
    assert (None if diff.is_zero else len(ga)-diff.degree())==expected_grade
    assert slr.nx.is_isomorphic(ga,gb)==(expected_grade is None)
    examples['S'+ua+' / S'+ub]={'isomorphic':slr.nx.is_isomorphic(ga,gb),
        'difference':str(sp.factor(diff.as_expr())),
        'first_different_grade':None if diff.is_zero else len(ga)-diff.degree(),
        'leading_difference':0 if diff.is_zero else int(diff.LC()),
        'P1_difference':value(ua)-value(ub),
        'P1_values':[value(ua),value(ub)],
        'polynomials':[str(sp.expand(ca)),str(sp.expand(cb))],
        'edge_lists':[sorted(map(list,ga.edges)),sorted(map(list,gb.edges))]}

# Within each N, assess how much the initial moments distinguish.
levels=[]
for N in range(2,9):
    entries=[r for r in data if r['N']==N]
    groups={k:len({tuple(r['traces'][:k]) for r in entries}) for k in [3,4,5,6,7,8]}
    levels.append({'N':N,'classes':len(entries),'moment_classes':groups})

from verify_distinguishability_proofs import verify_proofs
proofs=verify_proofs()
result={'symbolic_proofs':proofs,'all_word_checks':count,'direct_characteristic_polynomials':polynomial_count,
        'direct_integer_determinants':integer_det_count,'examples':examples,
        'separation_by_moments':levels,'long_samples':samples,'short_catalog':data}
(OUT/'spectral-distinguishability-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks':count,'polynomials':polynomial_count,'determinants':integer_det_count,
                  'example_grades':{k:v['first_different_grade'] for k,v in examples.items()},'moments':levels},ensure_ascii=False),flush=True)
