"""Exact first-grade influence audit; Python standard library only.

Compare rebuilt Laplacians, independently enumerated forest potentials,
relative sensitivities, and the assembled metric distribution.
Run from the repository root: python checks/metric-distributions/verify_influence.py
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'variations'))
from verify_single_edge import inverse, reduced_laplacian, vector, pairing, forest_sums


def forest_pair(p,q,resistances):
    def R(i,j):
        return Q(0) if i==j else resistances[tuple(sorted((i,j)))]
    i,j=p; k,l=q
    return (R(i,l)+R(j,k)-R(i,k)-R(j,l))/2


def audit_graph(n,weights):
    pairs=list(combinations(range(n),2))
    vectors={p:vector(n,p) for p in pairs}
    H=inverse(reduced_laplacian(n,weights))
    tau,forests=forest_sums(n,weights)
    R={p:forests[p]/tau for p in pairs}
    for p in pairs:
        assert R[p]==pairing(vectors[p],H,vectors[p])
    count=0
    for e in pairs:
        c=weights.get(e,Q(0))
        for delta in ([Q(1),Q(1,3),-c/2] if c else [Q(1),Q(1,3)]):
            changed=weights.copy(); changed[e]=c+delta
            Hnew=inverse(reduced_laplacian(n,changed))
            new_tau,new_forests=forest_sums(n,changed)
            assert new_tau==tau*(1+delta*R[e])
            new_R={p:new_forests[p]/new_tau for p in pairs}
            for p in pairs:
                for q in pairs:
                    old=pairing(vectors[p],H,vectors[q])
                    assert old==forest_pair(p,q,R)
                    new=pairing(vectors[p],Hnew,vectors[q])
                    assert new==forest_pair(p,q,new_R)
                    cross=pairing(vectors[p],H,vectors[e])*pairing(vectors[q],H,vectors[e])
                    assert new-old==-delta/(1+delta*R[e])*cross
                    m=c*cross
                    if c:
                        recovered=-c*(1+delta*R[e])/delta*(new-old)
                        assert recovered==m
                    count+=1
    for p in pairs:
        for q in pairs:
            coeff={e:c*pairing(vectors[p],H,vectors[e])*pairing(vectors[q],H,vectors[e])
                   for e,c in weights.items()}
            assert sum(coeff.values())==pairing(vectors[p],H,vectors[q])
            if p==q:
                assert all(m>=0 for m in coeff.values())
    return count


def main():
    specs=[('path3',3,{(0,1):Q(1),(1,2):Q(1)}),
           ('triangle',3,{(0,1):Q(1),(1,2):Q(1),(0,2):Q(1)}),
           ('weighted_triangle',3,{(0,1):Q(2),(1,2):Q(3),(0,2):Q(5)}),
           ('weighted_path4',4,{(0,1):Q(2),(1,2):Q(3),(2,3):Q(5)}),
           ('weighted_square',4,{(0,1):Q(2),(1,2):Q(3),(2,3):Q(5),(0,3):Q(7)})]
    counts={name:audit_graph(n,w) for name,n,w in specs}
    chain={ (0,1):Q(1),(1,2):Q(1)}
    v=vector(3,(0,2)); path_values=[]
    for t in [Q(0),Q(1,3),Q(1),Q(2)]:
        w=chain.copy();w[(0,2)]=t
        H=inverse(reduced_laplacian(3,w))
        value=pairing(v,H,v)
        assert value==2/(1+2*t)
        path_values.append({'t':str(t),'value':str(value),'change':str(value-2)})
    tri={ (0,1):Q(1),(1,2):Q(1),(0,2):Q(1)}
    H=inverse(reduced_laplacian(3,tri)); probes=[]
    for e, label in [((0,1),'ab'),((1,2),'bc'),((0,2),'ac')]:
        w=tri.copy();w[e]+=1
        value=pairing(v,inverse(reduced_laplacian(3,w)),v)
        m=pairing(v,H,vector(3,e))**2
        probes.append({'edge':label,'new_value':str(value),'change':str(value-Q(2,3)),'m':str(m)})
    assert [r['new_value'] for r in probes]==['3/5','3/5','2/5']
    assert [r['m'] for r in probes]==['1/9','1/9','4/9']
    # Mixed form: orientation in an argument matters; edge orientation does not.
    ab=vector(3,(0,1));bc=vector(3,(1,2));ac=vector(3,(0,2))
    mixed=[pairing(ab,H,vector(3,e))*pairing(bc,H,vector(3,e)) for e in tri]
    assert mixed==[Q(-2,9),Q(-2,9),Q(1,9)]
    assert sum(mixed)==Q(-1,3)
    out={'status':'passed','graphs':counts,'finite_form_comparisons':sum(counts.values()),
         'path_addition':path_values,'triangle_probes':probes,
         'triangle_coefficient_sum':'2/3','triangle_output_norm':'4/9',
         'mixed_ab_bc':list(map(str,mixed))}
    Path(__file__).with_name('influence-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':out['status'],'graphs':len(counts),'finite_form_comparisons':sum(counts.values())}))


if __name__=='__main__':
    main()
