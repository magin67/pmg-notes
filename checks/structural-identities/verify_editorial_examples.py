"""Exact checks for the examples and diagrams; finite checks do not prove the general basis theorem."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
import sympy as sp

@lru_cache(None)
def partitions(vertices):
 if not vertices:return ((),)
 a,*rest=vertices;out=[]
 for p in partitions(tuple(rest)):
  out.append(((a,),)+p)
  for i,b in enumerate(p):out.append(tuple(sorted(p[:i]+(tuple(sorted((a,)+b)),)+p[i+1:])))
 return tuple(out)
def canon(blocks):return tuple(sorted(tuple(sorted(b)) for b in blocks))
def grade(p):return sum(len(b)-1 for b in p)
def support(p):return {v for b in p if len(b)>1 for v in b}
def crossing(p):
 for b,c in combinations(p,2):
  for a,d in combinations(b,2):
   for e,f in combinations(c,2):
    if a<e<d<f or e<a<f<d:return True
 return False
def wedge(x,y):
 z=Counter()
 for a,c in x.items():
  for b,d in y.items():
   if a&b:continue
   inv=sum((b&((1<<i)-1)).bit_count() for i in range(a.bit_length()) if a>>i&1)
   z[a|b]+=c*d*(-1 if inv%2 else 1)
 return {k:v for k,v in z.items() if v}
def qcolumn(p,vertices,r):
 pos={v:i for i,v in enumerate(vertices)}
 def point(v):return {} if pos[v]==0 else {1<<(pos[v]-1):1}
 x={0:1}
 for block in p:
  a=block[0]
  for v in block[1:]:
   diff=Counter(point(v));diff.subtract(point(a));x=wedge(x,{k:c for k,c in diff.items() if c})
 masks=[sum(1<<i for i in b) for b in combinations(range(len(vertices)-1),r)]
 return sp.Matrix([x.get(i,0)*x.get(j,0) for i in masks for j in masks])
def forms(vertices,r):
 ps=[p for p in partitions(tuple(vertices)) if grade(p)==r]
 return ps,sp.Matrix.hstack(*(qcolumn(p,vertices,r) for p in ps))
def tetra(a,b,c,d,extra=()):
 plus=[[(a,b),(c,d)],[(a,c),(b,d)],[(a,d),(b,c)]]
 minus=[[(a,),(b,c,d)],[(b,),(a,c,d)],[(c,),(a,b,d)],[(d,),(a,b,c)]]
 return {canon(p+list(extra)):sign for terms,sign in [(plus,1),(minus,-1)] for p in terms}
def relation_vec(ps,rel):return sp.Matrix([rel.get(p,0) for p in ps])
def tree(n,edges):
 parent=list(range(n))
 def root(a):
  while parent[a]!=a:a=parent[a]
  return a
 for a,b in edges:
  a,b=root(a),root(b)
  if a==b:return False
  parent[a]=b
 return len(edges)==n-1

def main():
 ps,m=forms(tuple(range(4)),2);rel=tetra(0,1,2,3)
 assert m*relation_vec(ps,rel)==sp.zeros(m.rows,1)
 assert m.rank()==6
 paircols=[i for i,p in enumerate(ps) if all(len(b)==2 for b in p)]
 assert m[:,paircols].rank()==3
 assert tree(4,[(0,1),(2,3),(0,2)])
 assert not tree(4,[(0,1),(1,2),(0,2)])
 H=sp.Matrix([[1,1,0,0,0,1],[1,0,1,0,1,1],[1,0,0,1,1,0],[0,1,1,0,1,0],[0,1,0,1,1,1],[0,0,1,1,0,1]])
 assert H.det()==8
 # The support of a sum is larger than each generator's support.
 ps5,m5=forms(tuple(range(5)),2);a=tetra(0,1,2,3,((4,),));b=tetra(0,1,2,4,((3,),));rs=Counter(a);rs.update(b)
 assert m5*relation_vec(ps5,rs)==sp.zeros(m5.rows,1)
 assert set.union(*(support(p) for p,c in rs.items() if c))==set(range(5))
 # No-singleton count table, computed by independent enumeration.
 expected=[(4,2,3,2,1),(5,3,10,5,5),(6,3,15,5,10),(6,4,25,9,16),(7,4,105,21,84),(8,4,105,14,91)]
 for n,r,total,nc,primitive in expected:
  pp=[p for p in partitions(tuple(range(n))) if grade(p)==r and all(len(b)>1 for b in p)]
  assert len(pp)==total and sum(not crossing(p) for p in pp)==nc and total-nc==primitive
 # Transfer subspace and the product relation on six vertices.
 vertices=tuple(range(6));ps6,m6=forms(vertices,3);assert len(ps6)-m6.rank()==40
 index={p:i for i,p in enumerate(ps6)};cols=[]
 for sub in combinations(vertices,5):
  pp,mm=forms(sub,3);outside=set(vertices)-set(sub)
  for v in mm.nullspace():
   col=sp.zeros(len(ps6),1)
   for p,c in zip(pp,v):col[index[canon(p+tuple((x,) for x in outside))]]=c
   cols.append(col)
 transferred=sp.Matrix.hstack(*cols);assert transferred.rank()==30
 product=relation_vec(ps6,tetra(0,1,2,3,((4,5),)))
 assert m6*product==sp.zeros(m6.rows,1)
 assert transferred.row_join(product).rank()==31
 # Groves of a-x-b: empty subset is invalid; the other three meet the boundary.
 alpha,beta,gamma,delta=sp.symbols('alpha beta gamma delta');weights=[alpha,beta,gamma,delta]
 edges=[(0,2),(2,1),(0,3),(3,1)]
 tau=sum(sp.prod(weights[i] for i in subset) for subset in combinations(range(4),3) if tree(4,[edges[i] for i in subset]))
 assert sp.expand(tau-((alpha+beta)*gamma*delta+alpha*beta*(gamma+delta)))==0
 assert sum(tree(4,list(e)) for e in combinations(list(combinations(range(4),2)),3))==16
 # K4 grade-2 replacement changes coordinates, not the represented form.
 before={canon(p):1 for p in [[(0,1,2),(3,)],[(1,2,3),(0,)],[(0,2),(1,3)]]}
 coeff=[2,1,1,2,-1,-1]
 ordered=[canon(p) for p in [[(0,),(1,2,3)],[(1,),(0,2,3)],[(2,),(0,1,3)],[(3,),(0,1,2)],[(0,1),(2,3)],[(0,3),(1,2)]]]
 after=dict(zip(ordered,coeff));assert m*relation_vec(ps,before)==m*relation_vec(ps,after)
 print('PASS: tetrahedron identity; rank 6 and pair-family rank 3; pairing determinant 8; five-vertex sum support; six count-table rows; transfer rank 30, full kernel 40, product extension rank 31; weighted cycle and K4 count 16; signed basis coordinates.')
if __name__=='__main__':main()
