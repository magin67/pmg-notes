"""Exact Greenian forest toponomes and reciprocal rooted polynomials.

Run: python checks/dual/verify_toponomes.py
Uses only the standard library; writes JSON to stdout and creates no files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
import json
import verify_vector as v

def top(n,edges):
    out={}
    for k in range(n):
        for selected in combinations(edges,k):
            partition=v.forest_partition(n,selected)
            if partition is None: continue
            typ=tuple(sorted((len(b)-1 for b in partition if len(b)>1),reverse=True))
            out[typ]=out.get(typ,F(0))+prod((e[2] for e in selected),start=F(1))
    return {key:value for key,value in out.items() if value}

def specialize(n,poly,rooted):
    out=[F(0) for _ in range(n)]
    for typ,value in poly.items():
        out[sum(typ)]+=value*(prod(k+1 for k in typ) if rooted else 1)
    return out

def characteristic_coefficients(A):
    n=len(A)
    return [sum((v.determinant([[A[i][j] for j in S] for i in S])
                 for S in combinations(range(n),k)),start=F(0)) for k in range(n)]

def main():
    graphs={
        'P4':(4,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
        'P4_weighted':(4,[(0,1,F(1)),(1,2,F(1,2)),(2,3,F(1))]),
        'K4':(4,[(i,j,F(1)) for i,j in combinations(range(4),2)]),
        'C5':(5,[(i,(i+1)%5,F(1)) for i in range(5)]),
        'star5':(5,[(0,j,F(1)) for j in range(1,5)]),
        'weighted5':(5,[(0,1,F(2)),(1,2,F(3)),(2,3,F(1,2)),(3,4,F(1)),(4,0,F(4)),(1,3,F(2,3))])
    }
    results={}
    for name,(n,edges) in graphs.items():
        L=v.laplacian(n,edges)
        inv=v.inverse([[L[i][j]+F(1,n) for j in range(n)]for i in range(n)])
        Gr=[[x-F(1,n) for x in row]for row in inv]
        gamma=[(i,j,-Gr[i][j])for i,j in combinations(range(n),2)]
        TL,TG=top(n,edges),top(n,gamma)
        PL,PG=specialize(n,TL,True),specialize(n,TG,True)
        tau=v.determinant([row[:-1]for row in L[:-1]])
        assert PL==characteristic_coefficients(L)
        assert PG==characteristic_coefficients(Gr)
        assert PG==[c/(n*tau)for c in PL[::-1]]
        assert TG[(n-1,)]==F(1,n*n)/tau
        assert TG[(1,)]==sum(Gr[i][i]for i in range(n))/2
        assert all(c>0 for c in PG)
        for k in range(n):
            total=F(0)
            for selected in combinations(edges,n-1-k):
                partition=v.forest_partition(n,selected)
                if partition is None:continue
                total+=prod((e[2]for e in selected),start=F(1))*prod(len(b)for b in partition)
            assert PG[k]==total/(n*tau)
        results[name]={'tau':str(tau),'gamma':[(i,j,str(c))for i,j,c in gamma],
                       'TL':{str(k):str(c)for k,c in TL.items()},'TGr':{str(k):str(c)for k,c in TG.items()},
                       'PL':list(map(str,PL)),'PGr':list(map(str,PG)),
                       'FGr':list(map(str,specialize(n,TG,False)))}

    assert results['P4']['TGr']=={'()':'1','(1,)':'5/4','(2,)':'3/16','(1, 1)':'15/64','(3,)':'1/16'}
    assert results['P4_weighted']['TGr']=={'()':'1','(1,)':'7/4','(2,)':'-5/16','(1, 1)':'55/64','(3,)':'1/8'}
    assert results['K4']['TGr']=={'()':'1','(1,)':'3/8','(2,)':'3/64','(1, 1)':'3/256','(3,)':'1/256'}
    print(json.dumps({'verified':list(results),'examples':{k:results[k]for k in ('P4','P4_weighted','K4')}},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
