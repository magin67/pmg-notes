"""Exact checks for the polar Greenian and vertex deletion/attachment.

Run: python checks/dual/verify_variations.py
Uses only the standard library; writes JSON to stdout and creates no files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, prod
import json

from exterior_checks import add, multiply as mul, act, det, inv, wedge, tensor, component_coform
unit={(0,0):F(1)}
def scale(P,t):return {k:v*t for k,v in P.items() if v*t}
def lap(n,edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,c in edges:
        L[i][i]+=c;L[j][j]+=c;L[i][j]-=c;L[j][i]-=c
    return L
def tree_number(n,edges):
    L=lap(n,edges)
    return det([r[:-1] for r in L[:-1]])
def forests(n,edges):
    out=[]
    for mask in range(1<<len(edges)):
        p=list(range(n));w=F(1);chosen=[]
        def root(i):
            while p[i]!=i:i=p[i]
            return i
        for k,(i,j,c) in enumerate(edges):
            if mask>>k&1:
                x,y=root(i),root(j)
                if x==y:break
                p[x]=y;w*=c;chosen.append((i,j))
        else:
            groups={}
            for i in range(n):groups.setdefault(root(i),[]).append(i)
            out.append((tuple(sorted(tuple(g) for g in groups.values())),w,chosen))
    return out
def induced_tau(n,edges,vertices):
    ix={v:i for i,v in enumerate(vertices)}
    return tree_number(len(vertices),[(ix[i],ix[j],c) for i,j,c in edges if i in ix and j in ix])
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def form(A):return {(1<<i,1<<j):v for i,row in enumerate(A) for j,v in enumerate(row) if v}
def main():
    cases=[
     ('edge2',2,[(0,1,F(2))]),
     ('P4',4,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
     ('weightedP4',4,[(0,1,F(2)),(1,2,F(3)),(2,3,F(5))]),
     ('triangle235',3,[(0,1,F(2)),(1,2,F(3)),(0,2,F(5))]),
     ('C4',4,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1)),(3,0,F(1))]),
     ('K4',4,[(i,j,F(1)) for i,j in combinations(range(4),2)])
    ]
    results=[];attachment_checks=0;deletion_checks=0
    for name,n,edges in cases:
        L=lap(n,edges);tau=tree_number(n,edges);ff=forests(n,edges)
        Gr=inv([[L[i][j]+F(1,n) for j in range(n)] for i in range(n)])
        Gr=[[v-F(1,n) for v in row] for row in Gr]
        R=[[Gr[i][i]+Gr[j][j]-2*Gr[i][j] for j in range(n)] for i in range(n)]
        verts=[component_coform([i],n) for i in range(n)]
        polar={}
        for i,j in combinations(range(n),2):
            polar=add(polar,add(tensor(verts[i],verts[j]),tensor(verts[j],verts[i])),-R[i][j]/2)
        assert polar==form(inv([row[:-1] for row in L[:-1]]))
        q=[{} for _ in range(n)];mu={}
        for groups,w,chosen in ff:
            mu[groups]=mu.get(groups,F(0))+w
            blade={0:F(1)}
            for g in groups[:-1]:
                blade=wedge(blade,component_coform(g,n))
            q[len(groups)-1]=add(q[len(groups)-1],tensor(blade,blade),w/tau)
        assert q[0]==unit and q[1]==polar
        power=unit
        for k in range(n):
            assert q[k]==scale(power,F(1,factorial(k)))
            power=mul(power,polar)
        # Direct graph exponential, then removal from its actual top component.
        direct=unit
        for i,j,c in edges:
            v={1<<i:F(-1),1<<j:F(1)}
            direct=mul(direct,add(unit,tensor(v,v),c))
        grades=[{k:v for k,v in direct.items() if k[0].bit_count()==grade} for grade in range(n)]
        for k in range(n):
            assert act(grades[-1],q[k])==grades[n-1-k]
        for i,j in combinations(range(n),2):
            v={1<<i:F(-1),1<<j:F(1)}
            assert act(tensor(v,v),polar)=={(0,0):R[i][j]}
            sep=sum(w for gs,w,ch in ff if len(gs)==2 and not any(i in g and j in g for g in gs))
            assert sep/tau==R[i][j]
            assert tree_number(n,edges+[(i,j,F(3,2))])==tau*(1+F(3,2)*R[i][j])
        for m in range(1,n):
            for removed in combinations(range(n),m):
                left=[i for i in range(n) if i not in removed]
                partition=tuple(sorted([(i,) for i in removed]+[tuple(left)]))
                assert mu.get(partition,F(0))==induced_tau(n,edges,left)
                deletion_checks+=1
        attachments=[[F(0)]*n,[F(7)]+[F(0)]*(n-1),
                     [F(1)]+[F(0)]*(n-2)+[F(2)],
                     [F(i+1) for i in range(n)]]
        if name=='P4':attachments.append([F(1),F(0),F(0),F(1)])
        if name=='weightedP4':attachments.append([F(1),F(0),F(2),F(0)])
        if name=='triangle235':attachments.append([F(7),F(11),F(13)])
        values=[]
        for t in attachments:
            by_grade=[F(0)]*n
            for gs,w,ch in ff:
                by_grade[len(gs)-1]+=w*prod(sum(t[i] for i in g) for g in gs)
            f=sum(by_grade)
            d=det([[L[i][j]+(t[i] if i==j else 0) for j in range(n)] for i in range(n)])
            augmented=edges+[(i,n,t[i]) for i in range(n) if t[i]]
            trees=[(gs,w,ch) for gs,w,ch in forests(n+1,augmented) if len(gs)==1]
            enumerated=sum((w for gs,w,ch in trees),F(0))
            assert f==d==enumerated
            for k in range(n):
                assert by_grade[k]==sum((w for gs,w,ch in trees if sum(n in e for e in ch)==k+1),F(0))
            sigma=sum(t)
            if sigma:
                K=[[F(i==j)*t[i]-t[i]*t[j]/sigma for j in range(n)] for i in range(n)]
                GK=mm(Gr,K)
                assert sigma*tau*det([[F(i==j)+GK[i][j] for j in range(n)] for i in range(n)])==f
            active=[i for i,v in enumerate(t) if v]
            if len(active)==2:
                i,j=active
                assert tau*(t[i]+t[j]+t[i]*t[j]*R[i][j])==f
            attachment_checks+=1
            values.append({'t':list(map(str,t)),'tau_new':str(f),'grades':list(map(str,by_grade))})
        results.append({'graph':name,'tau':str(tau),'forests':len(ff),'attachments':values})
    print(json.dumps({'graphs':len(cases),'deletion_subsets':deletion_checks,'attachment_cases':attachment_checks,
                      'results':results},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
