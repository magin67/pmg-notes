"""Exact independent checks for examples in the Balanced Graphs series.
Run from any directory with Python 3 and SymPy. No files are modified.
"""
from pathlib import Path
from itertools import combinations,product,permutations
from collections import defaultdict,Counter
import json,random
import sympy as s

ROOT=Path(__file__).resolve().parent
Q=s.Rational
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
def lap(F):return s.diag(*[sum(F.row(i)) for i in range(F.rows)])-F
def green(L):
    n=L.rows; Pi=s.ones(n)/n
    return (L+Pi).inv()-Pi
def mins(L):
    return s.Matrix([L.minor_submatrix(i,i).det() for i in range(L.rows)])
def forests(F):
    n=F.rows; arcs=[(i,j) for i in range(n) for j in range(n) if F[i,j]>0]
    out=[]
    for k in range(n):
        for edges in combinations(arcs,k):
            source=[i for i,j in edges]
            if len(set(source))!=k:continue
            nxt=dict(edges); valid=True
            for i in range(n):
                seen=set();p=i
                while p in nxt:
                    if p in seen:valid=False;break
                    seen.add(p);p=nxt[p]
                if not valid:break
            if not valid:continue
            roots=Counter()
            for i in range(n):
                while i in nxt:i=nxt[i]
                roots[i]+=1
            typ=tuple(sorted((v-1 for v in roots.values() if v>1),reverse=True))
            w=s.prod(F[i,j] for i,j in edges)
            out.append((edges,typ,w))
    return out
def tree_degrees(F):
    n=F.rows; trees=[(edges,w) for edges,typ,w in forests(F) if len(edges)==n-1]
    weight=sum(w for edges,w in trees)
    return s.Matrix([sum(w*sum(i in e for e in edges) for edges,w in trees)/weight for i in range(n)]),len(trees),weight

# Printed nonuniform triangle: independent inversion and tree enumeration.
F=s.Matrix([[0,2,0],[1,0,1],[1,0,0]])
L=lap(F); Gr=green(L); one=s.ones(3,1);q=s.Matrix([Gr[i,i] for i in range(3)])
r=one*q.T-Gr; G=Gr.T-(q*one.T+one*q.T)/2
check('weighted triangle Green matrix',Gr==s.Matrix([[4,1,-5],[-2,4,-2],[-2,-5,7]])/18)
check('weighted triangle one-way matrix',r==s.Matrix([[0,1,4],[2,0,3],[2,3,0]])/6)
check('weighted triangle Gram matrix',G==s.Matrix([[0,-4,-5],[-2,0,-7],[-7,-5,0]])/12)
Gz=G.row_join(one).col_join(one.T.row_join(s.zeros(1)))
expected=s.Matrix([[2,-1,-1,Q(1,4)],[-2,2,0,Q(1,3)],[0,-1,1,Q(5,12)],[Q(1,3),Q(1,4),Q(5,12),Q(41,144)]])
check('bordered Gram inverse',Gz.inv()==expected)
for name,Ft,col in [('in',F,expected[:3,3]),('out',F.T,expected[3,:3].T)]:
    avg,count,weight=tree_degrees(Ft)
    check('sphere coordinates via '+name+' trees',one-avg/2==col and count==4 and weight==6)
R=r+r.T
c=(R.inv()*one)/(one.T*R.inv()*one)[0]
rho=(c.T*R*c)[0]/2
check('Euclidean circumcenter and radius',c==s.Matrix([Q(2,7),Q(2,7),Q(3,7)]) and rho==Q(2,7))

# Printed balancing example.
F=s.Matrix([[0,1,2],[2,0,1],[1,1,0]]);L=lap(F);tau=mins(L)
sigma=3*tau/sum(tau); Fb=s.diag(*sigma)*F
check('unbalanced cofactors',tau==s.Matrix([5,4,7]))
check('balanced graph cofactors',mins(lap(Fb))==s.ones(3,1)*Q(315,64))
check('row-scaling balance',Fb*s.ones(3,1)==Fb.T*s.ones(3,1))

# The 4-cycle tables, including mixed forests.
F=s.zeros(4)
for i in range(4):F[i,(i+1)%4]=1
for title,Ft,expected in [
    ('directed cycle',F,{():1,(1,):4,(2,):4,(1,1):2,(3,):4}),
    ('opposite cycles',F+F.T,{():1,(1,):8,(2,):12,(1,1):8,(3,):16}),
    ('doubled cycle',2*F,{():1,(1,):8,(2,):16,(1,1):8,(3,):32})]:
    totals=defaultdict(int)
    for edges,typ,w in forests(Ft):totals[typ]+=w
    check('forest table '+title,dict(totals)==expected)
    t=s.symbols('t');pol=sum(w*t**len(edges) for edges,typ,w in forests(Ft))
    check('forest determinant '+title,s.expand(pol-(s.eye(4)+t*lap(Ft)).det())==0)

# Exact identities on 12 independently generated positive balanced graphs.
rng=random.Random(1906)
for trial in range(12):
    n=3+trial%3;F=s.zeros(n)
    for cycle in [list(range(n))]+[rng.sample(range(n),rng.randint(2,n)) for _ in range(3)]:
        w=Q(rng.randint(1,3),rng.randint(1,3))
        for i,j in zip(cycle,cycle[1:]+cycle[:1]):F[i,j]+=w
    L=lap(F);Gr=green(L);one=s.ones(n,1);q=s.Matrix([Gr[i,i] for i in range(n)]);r=one*q.T-Gr
    for j in range(n):
        ids=[i for i in range(n) if i!=j]
        H=L.extract(ids,ids).inv()*s.ones(n-1,1)
        assert H==n*r.extract(ids,[j])
    check(f'first-passage systems {trial+1}',True)
    tau=mins(L)[0];a,b=0,1;d=s.eye(n)[:,a]-s.eye(n)[:,b]
    y=Gr.T*d; t=Q(2,3)
    check(f'single arc variation {trial+1}',mins(L+t*s.eye(n)[:,a]*d.T)==tau*(one+t*(y[a]*one-y)))
    G=Gr.T-(q*one.T+one*q.T)/2
    Gz=G.row_join(one).col_join(one.T.row_join(s.zeros(1)))
    bi=one/n+L.T*q/2;bo=one/n+L*q/2;rho=sum(q)/n+(q.T*L*q)[0]/4
    inv=L.T.row_join(bi).col_join(bo.T.row_join(s.Matrix([[rho]])))
    check(f'bordered inverse identity {trial+1}',Gz*inv==s.eye(n+1))
    for a,b,c in combinations(range(n),3):
        u=s.eye(n)[:,b]-s.eye(n)[:,a];v=s.eye(n)[:,c]-s.eye(n)[:,a]
        beta=lambda u,v:(v.T*Gr*u)[0]
        x=beta(u,v)-beta(v,u);g=(beta(u,v)+beta(v,u))/2
        resistance=beta(u,u)*beta(v,v)-beta(u,v)*beta(v,u)
        assert resistance==beta(u,u)*beta(v,v)-g*g+x*x/4
    check(f'triangle circulation identity {trial+1}',True)

# Small permutation examples, independent explicit enumeration.
for n in range(2,8):
    perms=[p for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
    counts=Counter()
    for p in perms:
        seen=set()
        for i in range(n):
            if i in seen:continue
            j=i;k=0
            while j not in seen:seen.add(j);k+=1;j=p[j]
            counts[k]+=1
    D=lambda m:s.factorial(m)*sum((-1)**j/s.factorial(j) for j in range(m+1))
    check(f'derangement cycle means n={n}',all(Q(counts[k],len(perms))==s.binomial(n,k)*s.factorial(k-1)*D(n-k)/D(n) for k in range(2,n+1)))

# New editorial examples: contractions, projections, and figure coordinates.
F=s.Matrix([[0,2,0],[1,0,1],[1,0,0]]);L=lap(F);Gr=green(L)
q=s.Matrix([Gr[i,i] for i in range(3)]);one=s.ones(3,1)
G=Gr.T-(q*one.T+one*q.T)/2
u=s.Matrix([1,0,-1]);v=s.Matrix([0,1,-1])
check('nonbasis outgoing di-coordinates',u.T*G==s.Matrix([[7,1,-5]])/12)
check('nonbasis incoming di-coordinates',G*v==s.Matrix([1,7,-5])/12)
check('two contractions and argument reversal',(u.T*(G*v))[0]==((u.T*G)*v)[0]==Q(1,2) and (v.T*G*u)[0]==1)
Gz=G.row_join(one).col_join(one.T.row_join(s.zeros(1)))
h=s.Matrix([Q(1,3)]*3+[0]);z=s.Matrix([0,0,0,1]);h2=(h.T*Gz*h)[0];h0=h-h2*z/2
check('local centroid correction',h2==-sum(q)/3 and (h0.T*Gz*h0)[0]==0)
xy=[s.Matrix([0,0]),s.Matrix([s.sqrt(Q(1,2)),0]),s.Matrix([s.sqrt(Q(1,2))/2,s.sqrt(Q(7,8))])]
bary=[s.Matrix([Q(1,3),Q(1,4),Q(5,12)]),s.Matrix([Q(1,4),Q(1,3),Q(5,12)]),s.Matrix([Q(2,7),Q(2,7),Q(3,7)])]
centers=[sum((co[i]*xy[i] for i in range(3)),s.zeros(2,1)) for co in bary]
check('circumcircle figure distances',all(s.simplify((p-centers[2]).dot(p-centers[2]))==Q(2,7) for p in xy))
check('three distinct center positions',len(set(tuple(x) for x in centers))==3 and Q(41,144)!=Q(2,7))
F=s.Matrix([[0,1,0],[0,0,1],[1,0,0]]);Gr=green(lap(F));q=s.Matrix([Gr[i,i] for i in range(3)]);r=s.ones(3,1)*q.T-Gr
w=s.Matrix([-1,0,1]);v=s.Matrix([-1,1,0]);beta=lambda u,v:(v.T*Gr*u)[0]
R=beta(v,v);out=beta(w,v)/R;inc=beta(v,w)/R;g=(beta(w,v)+beta(v,w))/(2*R)
check('three cycle projections',out==1 and inc==0 and g==Q(1,2))
chi=lambda r:r[0,1]+r[1,2]+r[2,0]-r[0,2]-r[2,1]-r[1,0]
check('cycle circulation and projection difference',chi(r)==-1 and inc-out==chi(r)/R)
Fp=s.Matrix([[0,1,0],[1,0,1],[0,1,0]]);Gp=green(lap(Fp));qp=s.Matrix([Gp[i,i] for i in range(3)]);rp=s.ones(3,1)*qp.T-Gp
check('same pair but distinct circulation',r[0,1]==rp[0,1]==Q(1,3) and r[1,0]==rp[1,0]==Q(2,3) and chi(rp)==0)
F=s.Matrix([[0,1,2],[2,0,1],[1,1,0]]);tau=mins(lap(F));sig=3*tau/sum(tau);Fb=s.diag(*sig)*F
check('balancing figure arc weights',Fb==s.Matrix([[0,15,30],[24,0,12],[21,21,0]])/16)
check('balancing figure degrees',Fb*s.ones(3,1)==s.Matrix([45,36,42])/16)
check('repeat balancing and recovery',3*mins(lap(Fb))/sum(mins(lap(Fb)))==s.ones(3,1) and s.diag(*[1/x for x in sig])*Fb==F)
C=s.zeros(4)
for i in range(4):C[i,(i+1)%4]=1
check('mixed forest in the figure',any(set(e)=={(0,1),(2,1)} and typ==(2,) for e,typ,w in forests(C+C.T)))
C3=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
check('two permutation factors',C3+C3.T==s.ones(3)-s.eye(3) and C3*s.ones(3,1)==C3.T*s.ones(3,1)==s.ones(3,1))
L=lap(C3);B=s.Matrix([[1,0],[0,1],[-1,-1]]);A=s.Matrix([[1,-1],[0,1]])
check('centered two-factor example',B*A*B.T==L and A.det()==1)
def cycle(n,seq):
    f=s.zeros(n)
    for i,j in zip(seq,seq[1:]+seq[:1]):f[i,j]+=1
    return lap(f)
L1=cycle(4,[0,1,2]);L2=cycle(4,[0,2,3]);L4=cycle(4,[0,1,2,3]);d=s.Matrix([1,0,-1,0])
check('quadrilateral diagonal in the Laplacian',L1+L2-L4==d*d.T)
check('quadrilateral diagonal cancels in circulation',(L1+L2-L4)-(L1+L2-L4).T==s.zeros(4))
print(json.dumps({'checks':len(checks),'passed':checks},ensure_ascii=False,indent=2))
