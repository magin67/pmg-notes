"""Exact checks of the examples and counts in the bilingual editorial revision.

Run with Python 3. No external packages are needed. Forms are expanded as
tensors of exterior-coordinate vectors; graph counts are obtained by enumeration.
"""
from itertools import combinations, product, permutations
from collections import Counter, defaultdict
from math import prod
import json

def clean(d):return {k:v for k,v in d.items() if v}
def exterior_basis(a,b):
    if a&b:return None,0
    inversions=sum((b&((1<<i)-1)).bit_count() for i in range(a.bit_length()) if a&(1<<i))
    return a|b,(-1)**inversions
def wedge(a,b):
    out=defaultdict(int)
    for x,u in a.items():
        for y,v in b.items():
            mask,sign=exterior_basis(x,y)
            if sign:out[mask]+=u*v*sign
    return clean(out)
def boundary(block):
    return {sum(1<<v for v in block if v!=missing):(-1)**i for i,missing in enumerate(block)}
def square_form(x):return {(a,b):u*v for a,u in x.items() for b,v in x.items()}
def partition_form(blocks):
    x={0:1}
    for block in blocks:x=wedge(x,boundary(block))
    return square_form(x)
def partitions(vertices):
    if not vertices:yield ();return
    first,*rest=vertices
    for blocks in partitions(rest):
        yield ((first,),)+blocks
        for i,block in enumerate(blocks):yield blocks[:i]+((first,)+block,)+blocks[i+1:]
def add(*forms):
    out=defaultdict(int)
    for f in forms:
        for k,v in f.items():out[k]+=v
    return clean(out)
def scale(f,c):return clean({k:c*v for k,v in f.items()})
def multiply(a,b):
    out=defaultdict(int)
    for (x,y),u in a.items():
        for (z,w),v in b.items():
            left,s=exterior_basis(x,z);right,t=exterior_basis(y,w)
            if s and t:out[left,right]+=u*v*s*t
    return clean(out)
def E(n,positive):
    total=sum(positive);full=tuple(sorted(tuple(positive)+(0,)*(n-total-len(positive)),reverse=True))
    return add(*(partition_form(p) for p in partitions(list(range(n))) if tuple(sorted((len(b)-1 for b in p),reverse=True))==full))

def components(n,edges):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for u,v in edges:
        u,v=root(u),root(v)
        if u==v:return None
        parent[u]=v
    groups=defaultdict(set)
    for v in range(n):groups[root(v)].add(v)
    return list(groups.values())
def all_forests(n):
    edges=list(combinations(range(n),2))
    for mask in range(1<<len(edges)):
        chosen=[e for i,e in enumerate(edges) if mask&(1<<i)]
        groups=components(n,chosen)
        if groups is not None:yield chosen,groups

def main():
    # Three orbits of pair partitions, eight vertex permutations per orbit.
    orbits=Counter(tuple(sorted((tuple(sorted(p[:2])),tuple(sorted(p[2:]))))) for p in permutations(range(4)))
    assert sorted(orbits.values())==[8,8,8]
    assert E(5,[2,1])==scale(E(5,[3]),3)
    t=E(4,[1]);t2=multiply(t,t);t3=multiply(t2,t);t4=multiply(t3,t);unit={(0,0):1}
    assert t2==scale(E(4,[2]),8) and t3==scale(E(4,[3]),96) and not t4
    assert multiply(add(unit,t,t2),add(unit,t2))==add(unit,t,scale(t2,2),t3)
    ordered=Counter()
    edges=list(combinations(range(4),2))
    for a,b in product(edges,repeat=2):ordered[len(set(a)&set(b))]+=1
    assert dict(ordered)=={2:6,1:24,0:6}
    forests=list(all_forests(5));counts=Counter(len(e) for e,_ in forests)
    assert [counts[i] for i in range(5)]==[1,10,45,110,125]
    types=Counter(tuple(sorted((len(g)-1 for g in groups),reverse=True)) for _,groups in forests)
    assert types[(2,1)]==30 and types[(2,0,0)]==30 and types[(1,1,0)]==15
    assert types[(3,0)]==80 and types[(4,)]==125
    cyc=[(0,1),(1,2),(2,3),(0,3)]
    assert sum(components(4,e) is not None for e in combinations(cyc,2))==6
    assert sum(components(4,e) is not None for e in combinations(cyc,3))==4
    prescribed=Counter()
    roots={3,4}
    for edges,groups in forests:
        if all(len(g&roots)==1 for g in groups):
            isolated=sum(g<=roots for g in groups);prescribed[isolated]+=1
    assert prescribed=={0:18,1:32}
    # Rooted forests on three vertices and partitions of their component sets.
    st=Counter()
    for edges,groups in all_forests(3):
        root_choices=prod(map(len,groups))
        for grouping in partitions(list(range(len(groups)))):st[len(grouping)]+=root_choices
    assert st=={1:16,2:9,3:1}
    # The illustration's root-deletion bijection, including roots of singletons.
    before=[(4,0),(4,2),(0,1),(5,3)]
    assert sorted(map(len,components(6,before)))==[2,4]
    after=[e for e in before if not set(e)&{4,5}]
    groups=components(4,after);assert sorted(map(len,groups))==[1,1,2]
    retained_roots={v for u,v in before if u in {4,5}}
    assert retained_roots=={0,2,3} and all(len(g&retained_roots)==1 for g in groups)
    print(json.dumps({'exact_form_equalities':'passed','permutation_orbits':sorted(orbits.values()),'ordered_edge_products':dict(ordered),'K5_forests_by_grade':[counts[i] for i in range(5)],'St_3':[st[i] for i in range(1,4)],'prescribed_root_forests':dict(prescribed),'root_deletion_example':'passed'},indent=2))
if __name__=='__main__':main()
