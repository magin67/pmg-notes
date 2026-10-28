"""Shared exact operations for the supplementary Greenian checks.

The contraction acts in the fixed coordinate pairing. Determinants and exterior
products are calculated independently; no graph metric is built into contraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
from verify_vector import add, wedge, tensor, multiply, coform as component_coform
from verify_vector import determinant as det, inverse as inv

def delete(mask, co):
    sign = 1
    for i in range(co.bit_length()):
        if not co >> i & 1:
            continue
        if not mask >> i & 1:
            return 0, 0
        sign *= (-1) ** (mask & ((1 << i)-1)).bit_count()
        mask ^= 1 << i
    return mask, sign

def act(top, coform):
    out = {}
    for (i,j), v in top.items():
        for (p,q), w in coform.items():
            a,s = delete(i,p)
            b,t = delete(j,q)
            if s*t:
                out = add(out, {(a,b): v*w*s*t})
    return out

def zero(n,m=None): return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]

def verify_forest_minors(name,n,edges):
 d=n-1;L=zero(n)
 for i,j,c in edges:
  L[i][i]+=c;L[j][j]+=c;L[i][j]-=c;L[j][i]-=c
 red=[row[:d] for row in L[:d]];tau=det(red);S=inv(red)
 Gr=inv([[L[i][j]+F(1,n) for j in range(n)] for i in range(n)])
 Gr=[[v-F(1,n) for v in row] for row in Gr]
 assert S==[[Gr[i][j]-Gr[i][d]-Gr[d][j]+Gr[d][d] for j in range(d)] for i in range(d)]
 ids={k:list(combinations(range(d),k)) for k in range(1,n)}
 sums={k:zero(len(ids[k])) for k in ids}; rooted={k:F(0) for k in ids};counts={k:0 for k in range(n)};ts=F(0)
 for mask in range(1<<len(edges)):
  parent=list(range(n))
  def root(i):
   while parent[i]!=i:i=parent[i]
   return i
  w=F(1);ok=True
  for j,(a,b,c) in enumerate(edges):
   if not mask>>j&1:continue
   ra,rb=root(a),root(b)
   if ra==rb:ok=False;break
   parent[ra]=rb;w*=c
  if not ok:continue
  groups={}
  for i in range(n):groups.setdefault(root(i),[]).append(i)
  groups=list(groups.values());k=len(groups)-1;counts[k]+=1
  if not k:ts+=w;continue
  cols=[[F(int(i in g)-int(d in g)) for i in range(d)] for g in groups[:-1]]
  v=[det([[col[i] for col in cols] for i in I]) for I in ids[k]]
  for i,x in enumerate(v):
   for j,y in enumerate(v):sums[k][i][j]+=w*x*y
  rooted[k]+=w*F(prod(map(len,groups)),n)
 assert ts==tau
 for k,inds in ids.items():
  expected=[[tau*det([[S[i][j] for j in J] for i in I]) for J in inds] for I in inds]
  assert sums[k]==expected,(name,k)
  spectral=sum(det([[Gr[i][j] for j in I] for i in I]) for I in combinations(range(n),k))
  assert rooted[k]/tau==spectral,(name,k,'spectral')
 assert sums[d]==[[F(1)]]
 return dict(name=name,n=n,tau=str(tau),forests=sum(counts.values()),grades=d,status='all tensor entries and spectral coefficients agree exactly')

