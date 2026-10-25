#!/usr/bin/env python3
"""Exact reproducible calculations for the Russian KVP series.

Run with Python 3.9+ from any directory; see README.md.
Standard library only. No network access and no file writes.
The implementation uses Fraction, direct grounded solves, forest enumeration,
principal minors and interpolation. These checks do not replace the proofs.
"""
from pathlib import Path
from itertools import permutations, product
from functools import lru_cache
import argparse
import contextlib
import io
import json
import re
import sys

REPO = Path(__file__).resolve().parents[2]
NOTES = REPO / "pmg-library/ru/KVP-разложение"
SEED = 25102026

from fractions import Fraction as F
from itertools import combinations
from random import Random
def mat(n,f): return [[F(f(i,j)) for j in range(n)] for i in range(n)]
def zero(n):return mat(n,lambda i,j:0)
def eye(n):return mat(n,lambda i,j:i==j)
def trans(A):return list(map(list,zip(*A)))
def scale(A,c):return [[x*c for x in row] for row in A]
def add(*As):return [[sum(A[i][j] for A in As) for j in range(len(As[0][0]))] for i in range(len(As[0]))]
def sub(A,B):return add(A,scale(B,-1))
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def rows(A):return list(map(sum,A))
def trace(A):return sum(A[i][i] for i in range(len(A)))
def inner(A,B):return sum(a*b for ar,br in zip(A,B) for a,b in zip(ar,br))/2
def inv(A):
 n=len(A); a=[row+ident for row,ident in zip(A,eye(n))]
 for j in range(n):
  p=next(i for i in range(j,n) if a[i][j]);a[j],a[p]=a[p],a[j]
  c=a[j][j];a[j]=[x/c for x in a[j]]
  for i in range(n):
   if i!=j:
    c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[j])]
 return [row[n:] for row in a]
def rank(A):
 a=[[F(x) for x in row] for row in A];m=len(a); n=len(a[0]); r=0
 for j in range(n):
  p=next((i for i in range(r,m) if a[i][j]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];c=a[r][j];a[r]=[x/c for x in a[r]]
  for i in range(r+1,m):
   c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==m:break
 return r
def dec(C):
 n=len(C);S=scale(add(C,trans(C)),F(1,2));A=scale(sub(C,trans(C)),F(1,2))
 mu=sum(rows(C))/n/(n-1);v=[x-(n-1)*mu for x in rows(S)];u=rows(A)
 K=mat(n,lambda i,j:mu if i!=j else 0)
 V=mat(n,lambda i,j:(v[i]+v[j])/(n-2) if i!=j else 0)
 U=mat(n,lambda i,j:(u[i]-u[j])/n)
 return [K,V,sub(S,add(K,V)),sub(A,U),U],v,u
def lap(C):
 d=rows(C);return mat(len(C),lambda i,j:d[i] if i==j else -C[i][j])
def dist(B):return mat(len(B),lambda i,j:B[i][i]+B[j][j]-2*B[i][j])
def H(R):return sum((2*(R[i][j]*R[i][k]+R[i][j]*R[j][k]+R[i][k]*R[j][k])-R[i][j]**2-R[i][k]**2-R[j][k]**2)/4 for i,j,k in combinations(range(len(R)),3))
def forest_subsets(n,k):
 edges=list(combinations(range(n),2));result=[]
 for ix in combinations(range(len(edges)),k):
  p=list(range(n));size=[1]*n
  def root(a):
   while p[a]!=a:a=p[a]
   return a
  for e in ix:
   a,b=map(root,edges[e])
   if a==b:break
   p[a]=b;size[b]+=size[a]
  else:result.append((ix,tuple(sorted((size[i]-1 for i in range(n) if p[i]==i and size[i]>1),reverse=True))))
 return edges,result
def coeffs(vals,forest):
 ans={}
 for ix,typ in forest:
  w=1
  for e in ix:w*=vals[e]
  ans[typ]=ans.get(typ,0)+w
 return ans

def check_symmetric():
    rng = Random(SEED)

    pairs = list(combinations(range(4), 2))
    cases = [
        ("complete", [1,1,1,1,1,1], [6,0,0]),
        ("cycle", [1,0,1,1,0,1], [F(8,3),0,F(4,3)]),
        ("star", [1,1,1,0,0,0], [F(3,2),F(3,2),0]),
        ("path", [1,0,0,1,0,1], [F(3,2),F(1,2),1]),
        ("matching", [1,0,0,0,0,1], [F(2,3),0,F(4,3)]),
        ("triangle", [1,1,0,1,0,0], [F(3,2),F(3,2),0]),
        ("empty", [0]*6, [0,0,0]),
        ("weighted", [4,2,0,1,3,2], [24,3,7]),
        ("weighted_star", [1,2,3,0,0,0], [6,7,1]),
    ]
    for name, weights, expected in cases:
        C = zero(4)
        for (i,j), w in zip(pairs, weights):
            C[i][j] = C[j][i] = F(w)
        parts = dec(C)[0][:3]
        assert [inner(X,X) for X in parts] == expected, name
        assert add(*parts) == C and rows(parts[2]) == [0]*4
        for X,Y in combinations(parts,2):
            assert inner(X,Y) == 0
    for n in range(3,13):
        for kind in ("complete", "star", "cycle"):
            C = mat(n, lambda i,j: i != j and (
                kind == "complete" or
                kind == "star" and (i == 0 or j == 0) or
                kind == "cycle" and (i-j) % n in (1,n-1)))
            K,V,P = dec(C)[0][:3]
            if kind in ("complete","star"):
                assert P == zero(n)
            if kind in ("complete","cycle"):
                assert V == zero(n)
    print("PASS 9 symmetric examples and complete/star/cycle families n=3..12")


def check_oriented():
    rng = Random(SEED)
    note = (NOTES / "Ориентированные расширения KVP - циркуляция и дисбаланс.md").read_text(encoding="utf-8")

    def decompose(C):
        n=len(C)
        S=[[(C[i][j]+C[j][i])/2 for j in range(n)] for i in range(n)]
        H=[[(C[i][j]-C[j][i])/2 for j in range(n)] for i in range(n)]
        mu=sum(map(sum,C))/F(n*(n-1))
        v=[sum(S[i])-(n-1)*mu for i in range(n)]
        u=list(map(sum,H))
        K=[[mu if i!=j else F(0) for j in range(n)] for i in range(n)]
        V=[[(v[i]+v[j])/(n-2) if i!=j else F(0) for j in range(n)] for i in range(n)]
        U=[[(u[i]-u[j])/n for j in range(n)] for i in range(n)]
        P=[[S[i][j]-K[i][j]-V[i][j] for j in range(n)] for i in range(n)]
        O=[[H[i][j]-U[i][j] for j in range(n)] for i in range(n)]
        return [K,V,P,O,U]

    def inner(A,B):
        return sum(x*y for a,b in zip(A,B) for x,y in zip(a,b))/2

    def matrix(n,edges):
        C=[[F(0) for j in range(n)] for i in range(n)]
        for i,j,w in edges:C[i][j]=F(w)
        return C

    base=[(0,1,1),(1,2,1),(2,0,1),(0,3,1),(3,0,1)]
    cases=[
     ('Единичный 3-орцикл',3,base[:3],'KO'),
     ('Единичный 4-орцикл',4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)],'KPO'),
     ('Балграф с неодинаковыми степенями',4,base,'KVPO'),
     ('Изменение одного веса',4,[(0,1,2)]+base[1:],'KVPOU'),
     ('Одна дуга без орциклов',3,[(0,1,1)],'KVOU')
    ]
    for name,n,edges,nonzero in cases:
        C=matrix(n,edges);parts=decompose(C)
        assert ''.join(s for s,X in zip('KVPOU',parts) if any(any(r) for r in X))==nonzero
        assert sum(inner(X,X) for X in parts)==inner(C,C)
        section=note.split('### '+name)[1].split('\n##')[0]
        rows=[row.split('|')[1:-1] for row in section.splitlines() if re.match(r'^\| \$[abcd]{2}\$',row)]
        if rows:
            assert len(rows)==n*(n-1)//2
            restored=matrix(n,[])
            for row in rows:
                i,j=['abcd'.index(c) for c in row[0].strip().strip('$')]
                numbers=[F(cell.strip().strip('$')) for cell in row[1:]]
                assert numbers==[X[i][j] for X in parts],(name,i,j,numbers)
                restored[i][j]=sum(numbers)
                restored[j][i]=sum(numbers[:3])-sum(numbers[3:])
            assert restored==C
        print('PASS example and printed table:',name)

    # Check the projectors on a complete coordinate basis, rather than selected graphs.
    for n in range(3,7):
        for i in range(n):
            for j in range(n):
                if i==j:continue
                C=matrix(n,[(i,j,1)])
                parts=decompose(C)
                assert all(sum(X[a][b] for X in parts)==C[a][b] for a in range(n) for b in range(n))
                for p,X in enumerate(parts):
                    assert all(X[a][b]==((-1 if p>=3 else 1)*X[b][a]) for a in range(n) for b in range(n))
                    xp=decompose(X)
                    assert all(xp[q]==(X if q==p else matrix(n,[])) for q in range(5))
                    if p in (2,3):assert all(sum(row)==0 for row in X)
                    for Y in parts[p+1:]:assert inner(X,Y)==0
                O=parts[3]
                tri=matrix(n,[])
                for a,b in combinations(range(n-1),2):
                    w=O[a][b]
                    for x,y in ((a,b),(b,n-1),(n-1,a)):
                        tri[x][y]+=w;tri[y][x]-=w
                assert tri==O
    print('PASS projector identities, orthogonality and triangle reconstruction on all ordered pair basis vectors, n=3..6')

    # Direct coefficient comparison with the PMG triangle form w(abc).
    C=matrix(3,[(0,1,1),(1,2,1),(2,0,1)])
    O=decompose(C)[3]
    w=matrix(3,[(0,1,1),(1,2,1),(2,0,1),(1,0,-1),(2,1,-1),(0,2,-1)])
    L_O=[[(sum(O[i]) if i==j else F(0))-O[i][j] for j in range(3)] for i in range(3)]
    assert L_O==[[-x/2 for x in row] for row in w]
    print('PASS PMG sign and factor: L(O)=-w/2 for unit triangle')


def check_distance():
    rng = Random(SEED)
    def center(n):
     return sub(eye(n),mat(n,lambda i,j:F(1,n)))
    def restore(Q):
     n=len(Q);r=[sum(row)/n for row in Q];m=sum(r)/n
     return mat(n,lambda i,j:(r[i]+r[j]-m-Q[i][j])/2)
    def vv(u):
     n=len(u);return mat(n,lambda i,j:(u[i]+u[j])/(n-2) if i!=j else 0)
    for n in range(3,7):
     J=center(n)
     for a in range(n):
      for b in range(n):
       A=mat(n,lambda i,j:i==a and j==b)
       assert dist(dist(A))==scale(dist(A),-2)
       assert scale(mul(mul(J,dist(A)),J),F(-1,2))==mul(mul(J,A),J)
       if a==b:continue
       C=A;Q=dist(lap(C));parts,v,u=dec(C);qparts,vq,uq=dec(Q)
       expected=[scale(parts[0],2*n),add(scale(parts[1],n),scale(vv(u),n-2)),scale(parts[2],2),scale(parts[3],2),scale(parts[4],2)]
       assert qparts==expected
       assert restore(Q)==lap(C)
       Cinv=add(scale(qparts[0],F(1,2*n)),scale(qparts[1],F(1,n)),scale(qparts[2],F(1,2)),scale(qparts[3],F(1,2)),scale(qparts[4],F(1,2)),scale(vv(uq),-F(n-2,2*n)))
       assert Cinv==C
       AQ=scale(mul(mul(J,C),J),F(-1,2))
       assert dist(AQ)==sub(C,parts[4])
       assert restore(C)==add(AQ,mat(n,lambda i,j:u[j]/n))
       for p in range(4):
        X=parts[p];LX=lap(X);DX=dist(LX)
        assert DX==scale(X,[2*n,n,2,2][p])
        assert scale(mul(mul(J,DX),J),F(-1,2))==LX
    print('PASS all coordinate basis vectors n=3..6: D^2, centering, KVPO multipliers, U-to-V mixing, both inverse rules')
    examples={
    'path':mat(4,lambda i,j:abs(i-j)==1),
    'cycle':mat(3,lambda i,j:j==(i+1)%3),
    'balanced':mat(4,lambda i,j:(i,j) in [(0,1),(1,2),(2,0),(0,3),(3,0)]),
    'arrow':mat(3,lambda i,j:(i,j)==(0,1))
    }
    for name,C in examples.items():
     Q=dist(lap(C));d=dec(Q)
     print(name,'Q=',[[str(x) for x in row] for row in Q],'mu=',str(d[0][0][0][1]),'v=',list(map(str,d[1])),'u=',list(map(str,d[2])))
     assert restore(Q)==lap(C)


def check_green():
    rng = Random(SEED)


    def analyze(C):
        n = len(C)
        Z = mat(n, lambda i,j:F(1,n))
        J = sub(eye(n),Z)
        L = lap(C)
        Gr = sub(inv(add(L,Z)),Z)
        q = [Gr[i][i] for i in range(n)]
        t = sum(q)
        eta = [x-t/n for x in q]
        r = mat(n,lambda i,j:q[j]-Gr[i][j])
        R = add(r,trans(r))
        gamma = mat(n,lambda i,j:-Gr[i][j] if i!=j else 0)
        Gd = dec(gamma)[0]
        rd,rv,ru = dec(r)
        Rd,Rv,Ru = dec(R)
        tilde = scale(dist(Gr),F(1,2))
        assert mul(L,Gr)==J==mul(Gr,L)
        assert lap(gamma)==Gr
        assert rows(gamma)==q
        assert Gd[4]==zero(n)
        assert rd[:4]==[scale(Gd[0],n),scale(Gd[1],F(n,2)),Gd[2],Gd[3]]
        assert Rd==[scale(Gd[0],2*n),scale(Gd[1],n),scale(Gd[2],2),zero(n),zero(n)]
        assert rd[4]==mat(n,lambda i,j:(eta[j]-eta[i])/2)
        assert rd[3]==scale(sub(Gr,trans(Gr)),F(-1,2))
        assert rd[1]==mat(n,lambda i,j:F(n,2*(n-2))*(eta[i]+eta[j]) if i!=j else 0)
        assert rv==[F(n,2)*x for x in eta]
        assert ru==[-x for x in rv]
        assert rows(r)==[t]*n
        assert rows(trans(r))==[n*x for x in q]
        assert rows(R)==[n*x+t for x in q]
        assert tilde==sub(r,rd[4])==add(scale(R,F(1,2)),rd[3])
        assert dec(tilde)[0]==rd[:4]+[zero(n)]
        assert Gr==scale(mul(J,r),-1)==scale(mul(mul(J,tilde),J),-1)
        assert scale(add(Gr,trans(Gr)),F(1,2))==scale(mul(mul(J,R),J),F(-1,2))
        assert lap(Gd[0])==scale(J,t/(n-1))
        assert lap(Gd[1])==scale(mul(mul(J,mat(n,lambda i,j:eta[i] if i==j else 0)),J),F(n,n-2))
        assert lap(Gd[3])==scale(sub(Gr,trans(Gr)),F(1,2))
        assert all(lap(Gd[2])[i][i]==0 for i in range(n))
        # Independent construction of each one-sided resistance column via a grounded system.
        independent = zero(n)
        for j in range(n):
            keep=[i for i in range(n) if i!=j]
            reduced=[[L[a][b] for b in keep] for a in keep]
            sol=mul(inv(reduced),[[F(1,n)] for _ in keep])
            for i,value in zip(keep,sol):independent[i][j]=value[0]
        assert independent==r
        assert all(r[i][j]>0 for i in range(n) for j in range(n) if i!=j)
        for a,b,c,d in combinations(range(n),4):
            delta=lambda X:(X[a][d]+X[b][c]-X[a][c]-X[b][d])/2
            assert delta(R)==delta(Rd[2])
        return dict(C=C,Gr=Gr,q=q,t=t,eta=eta,gamma=gamma,r=r,R=R,tilde=tilde,
                    gamma_components=Gd,r_components=rd,R_components=Rd)

    examples={}
    examples['path']=analyze(mat(4,lambda i,j:abs(i-j)==1))
    examples['cycle']=analyze(mat(3,lambda i,j:j==(i+1)%3))
    C=zero(4)
    for i,j in [(0,1),(1,2),(2,0),(0,3),(3,0)]:C[i][j]=F(1)
    examples['tail']=analyze(C)
    b=[0,0,1,1]
    examples['weighted']=analyze(mat(4,lambda i,j:b[i]+b[j] if i!=j else 0))
    assert dec(examples['weighted']['C'])[0][2]==zero(4)
    assert examples['weighted']['R_components'][2]!=zero(4)
    assert examples['path']['r'][0][1]==F(1,4)
    assert examples['path']['r'][1][0]==F(3,4)
    assert examples['tail']['r_components'][3][0][3]==0
    assert all(X!=zero(4) for X in examples['tail']['r_components'])

    # A regular nonnegative graph whose resistance table has a nonzero V component.
    C = mat(5, lambda i,j: i != j)
    for i,j,w in [(0,1,2),(2,3,2),(0,2,0),(1,3,0)]:
        C[i][j] = C[j][i] = F(w)
    ex = analyze(C)
    assert rows(C) == [4]*5 and dec(C)[0][1] == zero(5)
    assert ex["q"] == [F(94,525)]*4 + [F(4,25)]
    assert ex["t"] == F(92,105)
    assert dec(ex["R"])[1] == [F(2,105)]*4 + [-F(8,105)]
    assert ex["R_components"][0][0][1] == F(46,105)
    expected = {
        (0,1):F(12,35), (0,2):F(8,15), (0,3):F(10,21),
        (1,2):F(10,21), (1,3):F(8,15), (2,3):F(12,35),
    }
    expected.update({(i,4):F(44,105) for i in range(4)})
    # Independent ordinary two-terminal Kirchhoff solve, with target b grounded.
    L = lap(C)
    for (a,b), value in expected.items():
        keep = [i for i in range(5) if i != b]
        grounded = [[L[i][j] for j in keep] for i in keep]
        phi = mul(inv(grounded), [[F(i == a)] for i in keep])
        assert phi[keep.index(a)][0] == ex["R"][a][b] == value
        expected_v = F(4,315) if b != 4 else -F(2,105)
        assert ex["R_components"][1][a][b] == expected_v
    examples["regular"] = ex

    count=0
    for n in range(3,8):
        for k in range(4):
            C=zero(n)
            for i in range(n):C[i][(i+1)%n]=F(rng.randrange(1,5))
            C=add(C,trans(C))
            for i,j in combinations(range(n),2):
                w=F(rng.randrange(0,5));C[i][j]+=w;C[j][i]+=w
            analyze(C);count+=1
            C=zero(n)
            for i in range(n):C[i][(i+1)%n]=F(1)
            for _ in range(n):
                cyc=rng.sample(range(n),rng.randrange(2,n+1));w=F(rng.randrange(1,5))
                for i,j in zip(cyc,cyc[1:]+cyc[:1]):C[i][j]+=w
            analyze(C);count+=1
    print(f'PASS: five printed examples and {count} additional symmetric/balanced graphs, n=3..7; exact component formulas, recovery, and independent grounded solves.')


def check_applications():
    rng = Random(SEED)


    def green(C):
        n=len(C);Z=mat(n,lambda i,j:F(1,n))
        return sub(inv(add(lap(C),Z)),Z)

    def ground_potentials(C,a,b):
        n=len(C);L=lap(C);ref=n-1;keep=list(range(n-1))
        source=[F((i==a)-(i==b)) for i in range(n)]
        reduced=[[L[i][j] for j in keep] for i in keep]
        phi=[row[0] for row in mul(inv(reduced),[[source[i]] for i in keep])]
        return phi+[F(0)]

    def transfer(R,a,b,m,n):return (R[a][n]+R[b][m]-R[a][m]-R[b][n])/2

    def network(weight,contacts=False):
        count=8 if contacts else 4
        C=zero(count)
        for i,j in [(0,1),(1,2),(2,3),(3,0)]:
            C[i][j]=C[j][i]=F(weight if (i,j)==(0,1) else 1)
        eps=[F(1,4),F(1,2),F(3,4),F(1)]
        if contacts:
            for i,e in enumerate(eps):C[i][i+4]=C[i+4][i]=1/e
        terminals=list(range(4,8)) if contacts else list(range(4))
        fullR=dist(green(C))
        R=[[fullR[i][j] for j in terminals] for i in terminals]
        # Independently obtain each resistance and transfer from grounded Kirchhoff equations.
        for a,b in combinations(range(4),2):
            phi=ground_potentials(C,terminals[a],terminals[b])
            assert phi[terminals[a]]-phi[terminals[b]]==R[a][b]
            for m,n in combinations([i for i in range(4) if i not in (a,b)],2):
                assert phi[terminals[m]]-phi[terminals[n]]==transfer(R,a,b,m,n)
        D,v,u=dec(R)
        triples=[(0,1,2,3),(0,2,1,3),(0,3,1,2)]
        T=[transfer(R,*p) for p in triples]
        assert T[0]-T[1]+T[2]==0
        return dict(C=C,R=R,components=D[:3],T=T)

    examples={name:network(w,contact) for name,w,contact in [
        ('base',1,False),('contacts',1,True),('changed',2,False),('changed_contacts',2,True)]}
    epsilon=[F(1,4),F(1,2),F(3,4),F(1)]
    for left,right in [('base','contacts'),('changed','changed_contacts')]:
        a,b=examples[left],examples[right]
        assert sub(b['R'],a['R'])==mat(4,lambda i,j:epsilon[i]+epsilon[j] if i!=j else 0)
        assert a['components'][2]==b['components'][2]
        assert a['T']==b['T']
    Pdelta=sub(examples['changed']['components'][2],examples['base']['components'][2])
    assert [Pdelta[i][j] for i,j in combinations(range(4),2)]==[F(x,84) for x in [-5,-2,7,7,-2,-5]]

    A0=mat(4,lambda i,j:10 if i!=j else 0)
    star=mat(4,lambda i,j:4 if i!=j and (i==0 or j==0) else 0)
    pair=mat(4,lambda i,j:6 if {i,j}=={2,3} else 0)
    A1=add(A0,star);A2=add(A1,pair)
    ds=dec(star)[0][:3];dp=dec(pair)[0][:3]
    assert ds[2]==zero(4)
    assert [dp[2][i][j] for i,j in combinations(range(4),2)]==[F(x) for x in [2,-1,-1,-1,-1,2]]
    assert dec(A2)[0][2]==dp[2]
    assert [inner(X,X) for X in dp]==[F(6),F(18),F(12)]
    assert [inner(X,X) for X in ds]==[F(24),F(24),F(0)]
    examples['interactions']=dict(A0=A0,star=star,pair=pair,A1=A1,A2=A2,star_components=ds,pair_components=dp)

    # All disjoint four-point combinations: exact rank matches dim P for n=4..8.
    for n in range(4,9):
        edges=list(combinations(range(n),2));rowsT=[]
        for a,b,c,d in combinations(range(n),4):
            for i,j,k,l in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
                row=[F(0)]*len(edges)
                for x,y,coef in [(i,l,1),(j,k,1),(i,k,-1),(j,l,-1)]:
                    row[edges.index(tuple(sorted((x,y))))]+=F(coef,2)
                rowsT.append(row)
        assert rank(rowsT)==n*(n-3)//2
        for _ in range(3):
            A=zero(n)
            for i,j in edges:A[i][j]=A[j][i]=F(rng.randrange(-5,8))
            b=[F(rng.randrange(-4,5)) for _ in range(n)]
            B=mat(n,lambda i,j:b[i]+b[j] if i!=j else 0)
            assert dec(add(A,B))[0][2]==dec(A)[0][2]
            J=sub(eye(n),mat(n,lambda i,j:F(1,n)))
            assert mul(mul(J,B),J)==scale(mul(mul(J,mat(n,lambda i,j:b[i] if i==j else 0)),J),-2)

    print('PASS: four electrical networks, independent grounded current solves, terminal selection, exact contact invariance, pair/vertex interaction changes, and contrast ranks n=4..8.')
    for name in ['base','contacts','changed']:
        x=examples[name]
        print(name,'R=',[[str(v) for v in row] for row in x['R']], 'T=',list(map(str,x['T'])))


def check_metrics():
    rng = Random(SEED)


    def det(A):
        a=[row[:] for row in A];out=F(1);n=len(a)
        for j in range(n):
            pivot=next((i for i in range(j,n) if a[i][j]),None)
            if pivot is None:return F(0)
            if pivot!=j:a[j],a[pivot]=a[pivot],a[j];out=-out
            v=a[j][j];out*=v
            for i in range(j+1,n):
                factor=a[i][j]/v
                for k in range(j+1,n):a[i][k]-=factor*a[j][k]
        return out

    def tau(C):return det([row[:-1] for row in lap(C)[:-1]])

    def derivative_at_zero(values):
        # Polynomial interpolation, independent of the trace derivative formula.
        total=F(0)
        for i,y in enumerate(values):
            poly=[F(1)];den=F(1)
            for j in range(len(values)):
                if j==i:continue
                nxt=[F(0)]*(len(poly)+1)
                for k,x in enumerate(poly):nxt[k]-=j*x;nxt[k+1]+=x
                poly=nxt;den*=i-j
            total+=y*poly[1]/den
        return total

    def green(C):
        n=len(C);Z=mat(n,lambda i,j:F(1,n));return sub(inv(add(lap(C),Z)),Z)

    def analyze(C,check_derivatives=True):
        n=len(C);L=lap(C);Gr=green(C);R=dist(Gr);t=trace(Gr);q=[[Gr[i][i]] for i in range(n)]
        s=rows(R);Kf=sum(s)/2;w=[[x-2*Kf/n] for x in s]
        D=dec(C)[0][:3];RD=dec(R)[0][:3];Ls=[lap(X) for X in D]
        Fx=[trace(mul(Gr,X)) for X in Ls]
        assert Fx==[inner(X,Y) for X,Y in zip(D,RD)]
        assert sum(Fx)==n-1
        assert Fx[0]>=n-1
        alpha=add([[F(1,n)] for _ in range(n)],scale(mul(L,w),F(1,2*n)))
        rho0=Kf/(n*n);parts=[mul(trans(w),mul(X,w))[0][0]/(4*n*n) for X in Ls]
        rho=rho0+sum(parts)
        a=[scale(mul(X,w),F(1,2*n)) for X in Ls]
        M=[[mul(trans(x),mul(Gr,y))[0][0] for y in a] for x in a]
        assert rows(M)==parts
        assert all(sum(x[0] for x in vec)==0 for vec in a)
        assert sum(sum(row) for row in M)==rho-rho0
        assert rho==t/n+mul(trans(q),mul(L,q))[0][0]/4
        z=mul(inv(R),[[F(1)] for _ in range(n)])
        rho_direct=1/(2*sum(x[0] for x in z))
        assert rho==rho_direct
        assert alpha==scale(z,2*rho)
        degrees=[sum(C[i][j]*R[i][j] for j in range(n)) for i in range(n)]
        assert [x[0] for x in alpha]==[1-x/2 for x in degrees]
        assert sum(parts)>=0
        assert (sum(parts)==0)==(RD[1]==zero(n))
        mu=D[0][0][1];v=dec(C)[1];ws=[x[0] for x in w]
        assert parts[0]==mu*sum(x*x for x in ws)/(4*n)
        assert parts[1]==sum(vv*ww*ww for vv,ww in zip(v,ws))/(4*n*(n-2))
        assert parts[2]==-sum(D[2][i][j]*ws[i]*ws[j] for i,j in combinations(range(n),2))/(2*n*n)
        dbar=sum(rows(C))/n
        etaK=(n-1)**2/(dbar*Kf)
        etarho=(n-1)**2/(n*n*dbar*rho)
        assert etaK==(n-1)/Fx[0]
        assert etarho==etaK*rho0/rho
        if check_derivatives:
            for X,f in zip(D,Fx):
                values=[tau(add(C,scale(X,F(k)))) for k in range(n)]
                assert derivative_at_zero(values)/tau(C)==f
        return dict(C=C,Gr=Gr,R=R,q=q,w=w,Kf=Kf,tau=tau(C),components=D,R_components=RD,F=Fx,alpha=alpha,
                    rho0=rho0,rho_components=parts,rho=rho,center_components=a,center_gram=M,etaK=etaK,etarho=etarho)

    examples={
     'complete':analyze(mat(5,lambda i,j:i!=j)),
     'cycle':analyze(mat(5,lambda i,j:(i-j)%5 in [1,4])),
     'star':analyze(mat(5,lambda i,j:i!=j and (i==0 or j==0))),
     'path':analyze(mat(5,lambda i,j:abs(i-j)==1))}
    for z,name in [(F(0),'samekv0'),(F(1,4),'samekv1')]:
        alphaR=[F(1,4),-F(1,4),-F(1,4),F(1,4)]
        P=mat(4,lambda i,j:0 if i==j else (-2 if {i,j} in [{0,1},{2,3}] else 1))
        R=mat(4,lambda i,j:0 if i==j else 2+alphaR[i]+alphaR[j]+z*P[i][j])
        Z=mat(4,lambda i,j:F(1,4));J=sub(eye(4),Z)
        Gr=scale(mul(mul(J,R),J),F(-1,2));L=sub(inv(add(Gr,Z)),Z)
        C=mat(4,lambda i,j:-L[i][j] if i!=j else 0)
        assert all(C[i][j]>0 for i,j in combinations(range(4),2))
        examples[name]=analyze(C)
        assert examples[name]['R']==R
    assert examples['samekv0']['R_components'][:2]==examples['samekv1']['R_components'][:2]
    assert examples['samekv0']['q']==examples['samekv1']['q']
    assert examples['samekv0']['rho']!=examples['samekv1']['rho']

    # Independent spanning-tree enumeration verifies tau and expected vertex degrees.
    for name in ['complete','cycle','star','path','samekv0','samekv1']:
        ex=examples[name];C=ex['C'];n=len(C)
        edges=[(i,j) for i,j in combinations(range(n),2) if C[i][j]>0]
        total=F(0);degrees=[F(0)]*n
        for chosen in combinations(edges,n-1):
            parent=list(range(n))
            def find(x):
                while parent[x]!=x:x=parent[x]
                return x
            weight=F(1);ds=[0]*n
            for i,j in chosen:
                a,b=find(i),find(j)
                if a==b:break
                parent[a]=b;weight*=C[i][j];ds[i]+=1;ds[j]+=1
            else:
                total+=weight
                degrees=[x+weight*d for x,d in zip(degrees,ds)]
        assert total==ex['tau']
        assert [x/total for x in degrees]==[2*(1-x[0]) for x in ex['alpha']]

    for n in range(3,8):
        for _ in range(3):
            C=zero(n)
            for i,j in combinations(range(n),2):C[i][j]=C[j][i]=F(rng.randrange(1,6))
            analyze(C)

    # Balanced extension: trace contractions use reversed one-sided resistances.
    balanced=[]
    for n in range(3,7):
        for _ in range(3):
            C=zero(n)
            for i in range(n):C[i][(i+1)%n]=F(1)
            if _:
                for z in range(n):
                    cycle=rng.sample(range(n),rng.randrange(2,n+1));weight=F(rng.randrange(1,4))
                    for i,j in zip(cycle,cycle[1:]+cycle[:1]):C[i][j]+=weight
            Gr=green(C);q=[Gr[i][i] for i in range(n)];r=mat(n,lambda i,j:q[j]-Gr[i][j]);R=add(r,trans(r))
            D=dec(C)[0][:4];rd=dec(r)[0];RD=dec(R)[0]
            Fx=[trace(mul(Gr,lap(X))) for X in D]
            expected=[inner(D[i],RD[i]) for i in range(3)]+[-2*inner(D[3],rd[3])]
            assert Fx==expected and sum(Fx)==n-1
            for X,f in zip(D,Fx):
                assert derivative_at_zero([tau(add(C,scale(X,F(k)))) for k in range(n)])/tau(C)==f
            if n==3 and _==0:balanced=Fx
    assert balanced==[F(3,2),F(0),F(0),F(1,2)]

    print('PASS six detailed examples, 15 additional symmetric graphs and 12 balgraphs; exact radius from R inverse, tree enumeration, polynomial derivatives, center Gram matrix and contractions.')
    for name,x in examples.items():
        print(name,'tau',x['tau'],'Kf',x['Kf'],'F',x['F'],'rho0',x['rho0'],'rhoX',x['rho_components'],'rho',x['rho'],'alpha',[v[0] for v in x['alpha']])


def check_potential():
    rng = Random(SEED)


    def det(A):
        if not A: return F(1)
        a=[row[:] for row in A]; value=F(1)
        for j in range(len(a)):
            p=next((i for i in range(j,len(a)) if a[i][j]),None)
            if p is None:return F(0)
            if p!=j:a[j],a[p]=a[p],a[j];value=-value
            pivot=a[j][j];value*=pivot
            for i in range(j+1,len(a)):
                factor=a[i][j]/pivot
                for k in range(j+1,len(a)):a[i][k]-=factor*a[j][k]
        return value

    def principal(A,indices):return [[A[i][j] for j in indices] for i in indices]

    # Compare every coefficient of quadratic forms, not just selected input tables.
    for n in range(3,8):
        pairs=list(combinations(range(n),2)); m=len(pairs)
        basis={p:[F(int(k==i)) for k in range(m)] for i,p in enumerate(pairs)}
        def Rv(i,j):return basis[tuple(sorted((i,j)))]
        def vecsum(vs):return [sum(x,F(0)) for x in zip(*vs)]
        def scaled(v,c):return [x*c for x in v]
        def mz():return [[F(0) for _ in range(m)] for _ in range(m)]
        def prod(M,u,v,c=F(1)):
            for i in range(m):
                for j in range(m):M[i][j]+=c*(u[i]*v[j]+v[i]*u[j])/2
        mu=[F(1,m)]*m
        ds=[vecsum([Rv(i,j) for j in range(n) if i!=j]) for i in range(n)]
        vs=[vecsum([d,scaled(mu,1-n)]) for d in ds]
        ps=[vecsum([Rv(i,j),scaled(mu,-1),scaled(vecsum([vs[i],vs[j]]),-F(1,n-2))]) for i,j in pairs]
        HM,AM,ZM,KM,VM,PM=[mz() for _ in range(6)]
        for i,j,k in combinations(range(n),3):
            prod(HM,Rv(i,j),Rv(i,k))
            v=vecsum([Rv(i,j),Rv(i,k),scaled(Rv(j,k),-1)])
            prod(HM,v,v,-F(1,4))
        for a,b,c,d in combinations(range(n),4):
            for i,j,k,l in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
                prod(AM,Rv(i,j),Rv(k,l))
                v=scaled(vecsum([Rv(i,l),Rv(j,k),scaled(Rv(i,k),-1),scaled(Rv(j,l),-1)]),F(1,2))
                prod(ZM,v,v)
        prod(KM,mu,mu,m)
        for v in vs:prod(VM,v,v,F(1,n-2))
        for p in ps:prod(PM,p,p)
        for i in range(m):
            for j in range(m):
                assert AM[i][j]-ZM[i][j]==(n-3)*HM[i][j]
                assert ZM[i][j]==F((n-1)*(n-2),4)*PM[i][j]
                assert HM[i][j]==F(n-2,4)*KM[i][j]-VM[i][j]/2-F(n,4)*PM[i][j]
                if n==4:assert AM[i][j]==(KM[i][j]-VM[i][j]+PM[i][j])/2
    print('PASS all quadratic-form coefficients n=3..7: tetrahedron sums, P contrast norm and KVP formula')

    def check_graph(C):
        n=len(C);L=lap(C);Z=mat(n,lambda i,j:F(1,n));Gr=sub(inv(add(L,Z)),Z)
        r=mat(n,lambda i,j:Gr[j][j]-Gr[i][j]);R=add(r,trans(r))
        parts=dec(R)[0];rparts=dec(r)[0]
        hparts=[F(n-2,4)*inner(parts[0],parts[0]),-inner(parts[1],parts[1])/2,-F(n,4)*inner(parts[2],parts[2])]
        assert H(R)==sum(hparts)
        coefs=[det(principal(L,[i for i in range(n) if i!=j])) for j in range(n)]
        assert len(set(coefs))==1
        tau=coefs[0];assert tau>0
        triangles=[];chi2=F(0);direct=F(0)
        for i,j,k in combinations(range(n),3):
            aa=Gr[j][j]-Gr[j][i]-Gr[i][j]+Gr[i][i]
            bb=Gr[k][k]-Gr[k][i]-Gr[i][k]+Gr[i][i]
            ab=Gr[j][k]-Gr[j][i]-Gr[i][k]+Gr[i][i]
            ba=Gr[k][j]-Gr[k][i]-Gr[i][j]+Gr[i][i]
            value=aa*bb-ab*ba;direct+=value
            triangles.append(value)
            chi=r[i][j]+r[j][k]+r[k][i]-r[i][k]-r[k][j]-r[j][i]
            chi2+=chi**2
            # Independent rooted-forest principal minor for the complement of the triple.
            assert tau*value==det(principal(L,[q for q in range(n) if q not in (i,j,k)]))
        assert chi2/4==n*inner(rparts[3],rparts[3])
        assert direct==H(R)+n*inner(rparts[3],rparts[3])
        assert direct==(n-2)*inner(rparts[0],rparts[0])-2*inner(rparts[1],rparts[1])-n*inner(rparts[2],rparts[2])+n*inner(rparts[3],rparts[3])
        if n==3:assert tau*direct==1
        if n==4:assert tau*direct==trace(L)
        if C==trans(C):
            assert direct==H(R)>0
            assert direct<=F(n-2,2*n*(n-1))*(sum(rows(R))/2)**2
        return dict(C=C,R=R,r=r,tau=tau,Hparts=hparts,nu2=direct,U2=tau*direct,triangles=triangles)

    def graph(n,edges):
        C=zero(n)
        for i,j,w in edges:C[i][j]=C[j][i]=F(w)
        return C

    examples={}
    examples['complete']=check_graph(graph(4,[(i,j,1) for i,j in combinations(range(4),2)]))
    examples['cycle']=check_graph(graph(4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)]))
    examples['star']=check_graph(graph(4,[(0,i,1) for i in range(1,4)]))
    examples['path']=check_graph(graph(4,[(i,i+1,1) for i in range(3)]))
    examples['weighted']=check_graph(graph(4,[(i,i+1,i+1) for i in range(3)]))
    examples['orcycle']=check_graph(mat(3,lambda i,j:int(j==(i+1)%3)))
    examples['triangle']=check_graph(graph(3,[(i,j,F(2,3)) for i,j in combinations(range(3),2)]))
    assert examples['orcycle']['R']==examples['triangle']['R']
    assert examples['orcycle']['nu2']==1 and examples['triangle']['nu2']==F(3,4)
    for key,ex in examples.items():
        print(key, [str(x) for x in ex['Hparts']], 'nu2',ex['nu2'],'tau',ex['tau'],'U2',ex['U2'],'triangles',[str(x) for x in ex['triangles']])

    rng=Random(251020262)
    for n in range(3,8):
        for _ in range(3):
            C=graph(n,[(i,i+1,1) for i in range(n-1)])
            for i,j in combinations(range(n),2):C[i][j]+=F(rng.randrange(4));C[j][i]=C[i][j]
            check_graph(C)
            C=mat(n,lambda i,j:int(j==(i+1)%n))
            for _ in range(n+2):
                cycle=rng.sample(range(n),rng.randrange(2,n+1));weight=F(rng.randrange(1,4))
                for i,j in zip(cycle,cycle[1:]+cycle[:1]):C[i][j]+=weight
            check_graph(C)
    print('PASS 15 additional symmetric graphs and 15 balanced graphs n=3..7; direct Gram determinants and independent principal minors')


def check_forests():
    rng = Random(SEED)
    @lru_cache(None)
    def forests(n,k):return forest_subsets(n,k)

    def det(A):
        a=[row[:] for row in A];ans=F(1)
        for j in range(len(a)):
            p=next((i for i in range(j,len(a)) if a[i][j]),None)
            if p is None:return F(0)
            if p!=j:a[p],a[j]=a[j],a[p];ans=-ans
            pivot=a[j][j];ans*=pivot
            for i in range(j+1,len(a)):
                factor=a[i][j]/pivot
                for k in range(j+1,len(a)):a[i][k]-=factor*a[j][k]
        return ans

    def forest_coefs(C,k):
        edges,ff=forests(len(C),k)
        return coeffs([C[i][j] for i,j in edges],ff)

    def rooted(C):
        n=len(C);p=[F(1)]
        for k in range(1,n):
            a=forest_coefs(C,k);p.append(sum(value*root_factor(typ) for typ,value in a.items()))
        return p

    def root_factor(typ):
        w=1
        for r in typ:w*=r+1
        return w

    def minor_poly(L):
        n=len(L)
        return [sum(det([[L[i][j] for j in inds] for i in inds]) for inds in combinations(range(n),k)) for k in range(n)]

    def joint(C,k):
        parts=dec(C)[0][:3];edges,ff=forests(len(C),k);result={}
        for ix,typ in ff:
            out=result.setdefault(typ,{})
            for labels in product(range(3),repeat=k):
                w=F(1)
                for e,x in zip(ix,labels):
                    i,j=edges[e];w*=parts[x][i][j]
                abc=tuple(labels.count(i) for i in range(3))
                out[abc]=out.get(abc,F(0))+w
        return {typ:{abc:v for abc,v in d.items() if v} for typ,d in result.items()}

    def verify(C):
        n=len(C);K,V,P=dec(C)[0][:3];w=sum(rows(C))/2
        d2=sum(d*d for d in rows(C));norm=inner(C,C)
        a=forest_coefs(C,2);a2=a.get((2,),F(0));a11=a.get((1,1),F(0))
        assert a2==d2/2-norm and a11==w*w/2-d2/2+norm/2
        vv=sum(v*v for v in dec(C)[1]);pp=inner(P,P)
        v2=forest_coefs(V,2);p2=forest_coefs(P,2)
        assert v2.get((2,),0)==F(n-4,2*(n-2))*vv
        assert v2.get((1,1),0)==-F(n-3,2*(n-2))*vv
        assert p2.get((2,),0)==-pp and p2.get((1,1),0)==pp/2
        recovered_N=w*w-2*a2-2*a11
        recovered_D=2*w*w-2*a2-4*a11
        recovered_K=w*w/F(n*(n-1),2)
        recovered_V=(recovered_D-4*w*w/n)/(n-2)
        recovered_P=recovered_N-recovered_K-recovered_V
        assert [recovered_K,recovered_V,recovered_P]==[inner(X,X) for X in [K,V,P]]
        assert recovered_D==d2 and recovered_N==norm
        for k in range(2,min(4,n-1)+1):
            a=forest_coefs(P,k)
            assert a.get((2,)+(1,)*(k-2),0)==-k*a.get((1,)*k,0)
        for X in [C,K,V,P]:assert rooted(X)==minor_poly(lap(X))
        mu=w/F(n*(n-1),2);B=add(V,P);L=lap(C)
        for t in [F(-1,7),F(1,5),F(2,3)]:
            a=1+n*mu*t
            if a:
                left=det(add(eye(n),scale(L,t)))
                right=a**(n-1)*det(add(eye(n),scale(lap(B),t/a)))
                assert left==right

    data={}
    for name,C in [('path',mat(5,lambda i,j:abs(i-j)==1)),('weighted',mat(4,lambda i,j:(min(i,j)+1) if abs(i-j)==1 else 0))]:
        verify(C);parts=dec(C)[0][:3]
        data[name]={'parts':parts,'types':{},'rooted':{}}
        for key,X in zip(['C','K','V','P'],[C]+parts):
            allcoefs={():F(1)}
            for k in range(1,len(C)):allcoefs.update(forest_coefs(X,k))
            data[name]['types'][key]={str(typ):v for typ,v in allcoefs.items()}
            data[name]['rooted'][key]=rooted(X)
        j2=joint(C,2)
        assert all(sum(z>0 for z in abc)==1 for d in j2.values() for abc in d)
        j3=joint(C,3);p3={}
        for typ,d in j3.items():
            for abc,val in d.items():p3[abc]=p3.get(abc,F(0))+root_factor(typ)*val
        p3={abc:val for abc,val in p3.items() if val}
        for pars in [(1,1,1),(1,0,1),(2,-1,3),(0,1,-1)]:
            X=add(*[scale(A,F(a)) for A,a in zip(parts,pars)])
            expected=sum(val*pars[0]**abc[0]*pars[1]**abc[1]*pars[2]**abc[2] for abc,val in p3.items())
            assert minor_poly(lap(X))[3]==expected
        data[name]['joint3']={str(abc):v for abc,v in p3.items()}
        print(name,'rooted pure polynomials:',{key:list(map(str,val)) for key,val in data[name]['rooted'].items()})
        print(name,'joint rooted third coefficient:',data[name]['joint3'])

    base=mat(4,lambda i,j:(min(i,j)+1) if abs(i-j)==1 else 0)
    K,V,P=dec(base)[0][:3]
    pair=[]
    for label,sign in [('plus',1),('minus',-1)]:
        C=add(scale(K,F(3)),V,scale(P,F(sign)));verify(C)
        assert all(C[i][j]>0 for i,j in combinations(range(4),2))
        D=dec(C)[0][:3];t={}
        for key,X in zip(['C','K','V','P'],[C]+D):
            a={():F(1)}
            for k in range(1,4):a.update(forest_coefs(X,k))
            t[key]=a
        pair.append(t)
        j3=joint(C,3)[(3,)]
        assert j3=={(3,0,0):F(432),(1,2,0):F(-24),(1,0,2):F(-12),(0,2,1):F(2*sign)}
        data[label]={'C':C,'types':{key:{str(typ):val for typ,val in a.items()} for key,a in t.items()},'rooted':rooted(C),'joint_tree':{str(abc):val for abc,val in j3.items()}}
    assert all(pair[0][key]==pair[1][key] for key in ['K','V','P'])
    assert pair[0]['C'][(3,)]==398 and pair[1]['C'][(3,)]==394
    print('PASS two positive weighted graphs with identical pure K/V/P toponomes but tree coefficients 398 and 394')

    rng=Random(251020269)
    for n in range(3,7):
        for _ in range(2):
            C=zero(n)
            for i,j in combinations(range(n),2):C[i][j]=C[j][i]=F(rng.randrange(-2,4))
            verify(C)
    print('PASS 2 examples and 8 signed tables n=3..6: low grades, reconstruction, balance identities, K shift and independent determinant coefficients')

    # Exact rank witnesses; use integral balanced generators, without imposing forest relations.
    def p_generator(n,verts,x=1,y=0):
        a,b,c,d=verts;P=zero(n)
        for i,j,w in [(a,b,x),(c,d,x),(a,c,y),(b,d,y),(a,d,-x-y),(b,c,-x-y)]:P[i][j]=P[j][i]=F(w)
        return P

    rank_data={}
    for k in [2,3,4]:
        n=2*k;types=sorted({typ for ix,typ in forests(n,k)[1]});rs=[];examples=[]
        for rep in range(12):
            P=zero(n)
            for _ in range(n):P=add(P,p_generator(n,rng.sample(range(n),4),rng.randrange(-1,2),rng.randrange(-1,2)))
            a=forest_coefs(P,k);row=[a.get(typ,F(0)) for typ in types]
            if rank(rs+[row])>len(rs):
                rs.append(row);examples.append(P)
            if len(rs)==len(types)-1:break
        assert len(rs)==len(types)-1
        rank_data[str(k)]={'n':n,'types':types,'rows':rs,'P':examples}
        print('PASS exact P coefficient rank k='+str(k)+', n='+str(n)+': '+str(len(rs)))
    data['rank_witnesses']=rank_data

    # Recompute the already published integer witnesses, not only a newly generated set.
    published = json.loads((NOTES / "Проверка рангов P-топономов.json").read_text(encoding="utf-8"))
    for key, witness in published["grades"].items():
        k = int(key)
        n = witness["n"]
        types = [tuple(t) for t in witness["types"]]
        actual_rows = []
        for matrix, recorded in zip(witness["P"], witness["rows"]):
            P = [[F(x) for x in row] for row in matrix]
            assert len(P) == n and all(len(row) == n for row in P)
            assert P == trans(P) and rows(P) == [0]*n
            assert all(P[i][i] == 0 for i in range(n))
            actual = forest_coefs(P,k)
            row = [actual.get(t,F(0)) for t in types]
            assert row == [F(x) for x in recorded]
            actual_rows.append(row)
        assert len(witness["P"]) == len(witness["rows"])
        assert rank(actual_rows) == witness["rank"] == len(types)-1
        print("PASS published witness dataset, grade", k)


CHECKS = {
    "symmetric": check_symmetric,
    "oriented": check_oriented,
    "distance": check_distance,
    "green": check_green,
    "applications": check_applications,
    "metrics": check_metrics,
    "potential": check_potential,
    "forests": check_forests,
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=CHECKS, help="Run one group")
    parser.add_argument("--verbose", action="store_true", help="Show intermediate exact results")
    args = parser.parse_args()
    if not __debug__:
        parser.error("Assertions are required: run without -O or PYTHONOPTIMIZE")
    selected = {args.only: CHECKS[args.only]} if args.only else CHECKS
    for name, check in selected.items():
        log = io.StringIO()
        try:
            with contextlib.redirect_stdout(log):
                check()
        except Exception:
            print(log.getvalue(), end="")
            print("FAIL", name)
            raise
        print("PASS", name)
        if args.verbose:
            print(log.getvalue(), end="")
    print(f"All {len(selected)} check groups passed.")

if __name__ == "__main__":
    main()
