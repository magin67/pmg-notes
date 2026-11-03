"""Exact checks for the PMG note on degree potential. Run with Python + SymPy.

All edge lists below are explicit; no external graph data are downloaded.
"""
from pathlib import Path
import json
import sympy as s

def matrices(n, edges):
    A = s.zeros(n)
    for edge in edges:
        i, j = edge[:2]
        w = edge[2] if len(edge) == 3 else 1
        A[i,j] = A[j,i] = w
    one = s.ones(n,1)
    d = A*one
    L = s.diag(*d)-A
    P = s.ones(n)/n
    G = (L+P).inv()-P
    b = d-one*sum(d)/n
    beta = one/n+G*b/2
    assert s.simplify(L*beta-b/2) == s.zeros(n,1)
    assert s.simplify(sum(beta)) == 1
    # Independent affine sphere equations, without pseudoinversion.
    Q = d*one.T+one*d.T-2*L
    M = Q.row_join(-2*one).col_join(one.T.row_join(s.zeros(1)))
    direct = M.inv()*s.Matrix([0]*n+[1])
    assert (direct[:n] == list(beta)) if not any(x.free_symbols for x in beta) else all(s.simplify(direct[i]-beta[i]) == 0 for i in range(n))
    return A,L,G,b,beta

def distances(n, edges):
    D = [[0 if i==j else n+1 for j in range(n)] for i in range(n)]
    for i,j in edges: D[i][j]=D[j][i]=1
    for k in range(n):
        for i in range(n):
            for j in range(n): D[i][j]=min(D[i][j],D[i][k]+D[k][j])
    return s.Matrix([sum(row) for row in D])

out = {}
for n,edges in [(5,[(0,1),(1,2),(2,3),(3,4)]),(5,[(0,i) for i in range(1,5)]),(7,[(0,1),(0,2),(1,3),(1,4),(2,5),(5,6)])]:
    A,L,G,b,beta = matrices(n,edges)
    T = distances(n,edges)
    assert L*T == 2*(n-1)*s.ones(n,1)-n*A*s.ones(n,1)
    assert beta == s.ones(n,1)/n+(s.ones(n,1)*sum(T)/n-T)/(2*n)
    out['tree_'+str(n)+'_'+str(edges)] = list(map(str,beta))

edges=[(0,1),(1,2),(0,2),(2,3),(3,4)]
A,L,G,b,beta=matrices(5,edges)
assert list(beta)==list(map(s.Rational,['1/2','1/2','1/2','0','-1/2']))
assert list(distances(5,edges)) == [7,7,5,6,9]

edges=[(0,1),(0,2),(0,3),(0,4),(1,3),(1,5),(2,3),(2,5)]
before=matrices(6,edges)[-1]; after=matrices(6,edges+[(1,4)])[-1]
assert before[:2]==[s.Rational(43,144),s.Rational(49,144)]
assert after[:2]==[s.Rational(112,366),s.Rational(97,366)]

edges=[(0,1),(1,2),(1,3),(1,4),(2,3),(2,4)]
beta=matrices(5,edges)[-1]
assert list(beta)==list(map(s.Rational,['-17/50','9/25','41/100','57/200','57/200']))
e=s.symbols('epsilon',real=True)
family=[(i,j,1 if (i,j) in edges else 1-e) for i in range(5) for j in range(i+1,5)]
A,L,G,b,beta=matrices(5,family)
gap=s.factor(beta[1]-beta[2])
expected=e*(8*e**2-35*e+25)/(10*(e-5)*(4*e-5))
assert s.simplify(gap-expected)==0
# First derivative at the regular graph, including sum-one eigenvector response.
h=A.diff(e)*s.ones(5,1); h0=h-s.ones(5,1)*sum(h)/5
vprime=G.subs(e,0)*h0/5
assert beta.diff(e).subs(e,0)==s.Rational(5,2)*vprime
out['family_gap']=str(gap)
out['threshold']=str((35-5*s.sqrt(17))/16)

edges=[(0,1),(0,2),(0,3),(0,5),(1,3),(1,4),(1,6),(2,3),(2,5),(3,4),(3,5),(3,6),(4,6),(5,6),(5,7),(6,7),(7,8),(8,9)]
A,L,G,b,beta=matrices(10,edges)
delta=s.zeros(10,1)
for i,j in edges:
    R=G[i,i]+G[j,j]-2*G[i,j]
    delta[i]+=R; delta[j]+=R
assert sum(delta)==18
out['kite_beta']=list(map(str,beta))
out['kite_tree']=list(map(str,delta/18))
import numpy as np
vals,vecs=np.linalg.eigh(np.array(A).astype(float))
v=vecs[:,-1]; v=v/sum(v)
assert np.max(np.abs(np.array(A).astype(float)@v-vals[-1]*v))<1e-12
out['kite_eigenvector']=list(map(float,v))
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print('All exact checks passed.')

# Reproducible illustration. Use a local cache on restricted hosts.
import os
os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).parent/'mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'svg.fonttype':'none', 'font.size':12})
fig,(ax,chart)=plt.subplots(1,2,figsize=(12,4.6),gridspec_kw={'width_ratios':[0.8,1.5]})
edges=[(0,1),(1,2),(1,3),(1,4),(2,3),(2,4)]
pos=np.array([[-1.4,0],[-0.5,0],[0.9,0],[0.2,0.95],[0.2,-0.95]])
for i,j in edges:
    ax.plot(pos[[i,j],0],pos[[i,j],1],color='#8996a5',lw=2,zorder=1)
for i,(x,y) in enumerate(pos):
    ax.scatter([x],[y],s=680,color='#eaf0f6',edgecolor='#41566c',lw=1.8,zorder=2)
    ax.text(x,y,'abcde'[i],ha='center',va='center',zorder=3,fontweight='bold')
ax.set(xlim=(-1.9,1.4),ylim=(-1.4,1.4),title='Конечный граф: ε = 1')
ax.set_aspect('equal'); ax.axis('off')
grid=np.linspace(0,1,251)
bg=grid*(8*grid**2-35*grid+25)/(10*(grid-5)*(4*grid-5))
vg=[]
for t in grid:
    a=np.zeros((5,5))
    for i in range(5):
        for j in range(i+1,5): a[i,j]=a[j,i]=1 if (i,j) in edges else 1-t
    ev,V=np.linalg.eigh(a); v=V[:,-1]/sum(V[:,-1])
    vg.append(2.5*(v[1]-v[2]))
threshold=float((35-5*s.sqrt(17))/16)
chart.axhline(0,color='#687381',lw=0.8)
chart.axvline(threshold,color='#8996a5',ls=':',lw=1.5)
chart.plot(grid,bg,label='βb − βc',color='#126c9c',lw=2.5)
chart.plot(grid,vg,label='(5/2)(vb − vc)',color='#bf6b24',lw=2.5)
chart.text(threshold-0.025,-0.046,'ε* ≈ 0.899',ha='right',fontsize=11)
chart.set(xlim=(0,1),xlabel='ε: ослабление четырёх связей',ylabel='Разность оценок b и c',title='От K₅ к конечному графу')
chart.spines[['top','right']].set_visible(False)
chart.grid(alpha=.2); chart.legend(loc='upper left',frameon=False)
fig.tight_layout(pad=1.5)
target=Path(__file__).with_name('Потенциал степеней - расхождение ранжирований')
fig.savefig(target.with_suffix('.svg'),bbox_inches='tight')
fig.savefig(target.with_suffix('.png'),dpi=160,bbox_inches='tight')
