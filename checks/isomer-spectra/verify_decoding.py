"""Exact forest-state certificates, direct minors, enumeration, and SLR decoding."""
from pathlib import Path
from itertools import product
from math import prod
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
from verify_slr_code import transfers, graph
from verify_boundary_transfer import xi, laplacian, passport

T,U,s1 = transfers()
sign = sp.diag(1,-1,-1,-1,1)
z0 = sign*s1.subs(xi,-1)
M = {c:sign*U[c].subs(xi,-1)*sign for c in 'SLR'}
H = sp.zeros(5)
H[0,4]=H[4,0]=sp.Rational(1,2)
H[1,2]=H[2,1]=-sp.Rational(1,2)
H[3,3]=1
row = M['S'][0,:]
lo = [sp.Rational(43,100),sp.Rational(43,100),sp.Rational(83,500),sp.Rational(4,25)]
hi = [sp.Rational(9,20),sp.Rational(9,20),sp.Rational(7,40),sp.Rational(9,50)]
corners = [sp.Matrix((1,)+v) for v in product(*zip(lo,hi))]


def rational_certificates():
    result={}
    forms=sp.Matrix([[-4,9,0,0,0],[-4,0,9,0,0]])
    for c,N in M.items():
        assert N.det()==1 and all(v.q==1 for v in N.inv())
        assert N.T*H*N==H
        assert N*N.inv()==sp.eye(5)
        points=[N*z for z in corners]
        growth=[p[0] for p in points]
        assert min(growth)==sp.Rational(349,4)
        assert max(growth)==sp.Rational(11131,125)
        margins=[]
        for i in range(4):
            lower=min(p[i+1]-lo[i]*p[0] for p in points)
            upper=min(hi[i]*p[0]-p[i+1] for p in points)
            assert lower>0 and upper>0
            margins.append([str(lower),str(upper)])
        ranges=[[min((forms*p)[i] for p in points),max((forms*p)[i] for p in points)] for i in range(2)]
        expected={'L':(-1,1),'S':(1,1),'R':(1,-1)}[c]
        for i,e in enumerate(expected):
            if e==1: assert ranges[i]==[sp.Rational(639,500),sp.Rational(33,20)]
            else: assert ranges[i]==[-sp.Rational(1269,125),-sp.Rational(399,50)]
        result[c]={'growth_bounds':list(map(str,[min(growth),max(growth)])),
                   'invariance_margins':margins,'sector_ranges':[[str(v) for v in pair] for pair in ranges]}
    assert (z0.T*H*z0)[0]==0
    assert all(N[0,:]==row for N in M.values())
    expected=[['3559/25000','123/400'],['3559/25000','123/400'],
              ['7079/125000','1141/4000'],['5229/12500','4503/5000']]
    aggregate=[[str(min(sp.Rational(result[c]['invariance_margins'][i][j])
                       for c in M)) for j in range(2)] for i in range(4)]
    assert aggregate==expected
    return result


INT_M={c:tuple(tuple(int(v) for v in row) for row in N.tolist()) for c,N in M.items()}
INT_INV={c:tuple(tuple(int(v) for v in row) for row in N.inv().tolist()) for c,N in M.items()}
SEED=tuple(map(int,z0))


def matvec(A,z):
    return tuple(sum(a*b for a,b in zip(r,z)) for r in A)


def in_cone(z):
    a,b,c,d,e=z
    return a>0 and 43*a<=100*b<=45*a and 43*a<=100*c<=45*a and 83*a<=500*d and 40*d<=7*a and 4*a<=25*e and 50*e<=9*a


def quadric(z):
    a,b,c,d,e=z
    return a*e-b*c+d*d


def sector(z):
    a,b,c,_,_=z
    u,v=9*b-4*a,9*c-4*a
    if u>0 and v>0:return 'S'
    if u<0 and v>0:return 'L'
    if u>0 and v<0:return 'R'
    return None


def decode(z):
    """Recognize the seed orbit; rejects arbitrary integer candidates too."""
    backwards=[]
    while True:
        if not in_cone(z) or quadric(z)!=0:return None
        if z==SEED:return ''.join(reversed(backwards))
        c=sector(z)
        if c is None:return None
        previous=matvec(INT_INV[c],z)
        if not 0<previous[0]<z[0]:return None
        backwards.append(c)
        z=previous


def decode_chain(z):
    """Return the full code Su; C6 is a separate one-core case."""
    operations=decode(z)
    if operations and operations.endswith('S'):
        return 'S'+operations[:-1]
    return None


def forest_counts(edges,n,boundary):
    """Enumerate acyclic edge sets; root choices are counted by component sizes."""
    edge_list=list(edges)
    totals=[0]*5
    x,y=boundary
    for mask in range(1<<len(edge_list)):
        parent=list(range(n));sizes=[1]*n
        def find(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        valid=True
        for k,(a,b) in enumerate(edge_list):
            if mask>>k&1:
                ra,rb=find(a),find(b)
                if ra==rb:
                    valid=False;break
                parent[rb]=ra;sizes[ra]+=sizes[rb]
        if not valid:continue
        roots=[i for i in range(n) if parent[i]==i]
        weight=prod(sizes[i] for i in roots)
        rx,ry=find(x),find(y)
        totals[0]+=weight
        totals[1]+=weight//sizes[rx]
        totals[2]+=weight//sizes[ry]
        if rx==ry:totals[3]+=weight//sizes[rx]
        else:totals[4]+=weight//(sizes[rx]*sizes[ry])
    return totals


def direct_checks():
    seed_edges={tuple(sorted((i,(i+1)%6))):1 for i in range(6)}
    seed_direct=passport(sp.eye(6)+laplacian(seed_edges,6),(0,1))
    seed_forests=forest_counts(seed_edges,6,(0,1))
    assert tuple(map(int,seed_direct))==tuple(seed_forests)==SEED
    count=1;forest_examples={'C6':{'boundary':[0,1],'state':seed_forests,'edge_subsets':64}}
    for length in range(3):
        for letters in product('SLR',repeat=length):
            u=''.join(letters)
            z=SEED
            for c in u+'S':z=matvec(INT_M[c],z)
            g,_,boundary,edges=graph(u)
            direct=passport(sp.eye(len(g))+laplacian(edges,len(g)),boundary)
            assert tuple(map(int,direct))==z
            assert decode(z)==u+'S'
            assert decode_chain(z)=='S'+u
            count+=1
            if u in ('','S','L'):
                forests=forest_counts(edges,len(g),boundary)
                assert tuple(forests)==z
                forest_examples['S'+u]={'boundary':list(boundary),'state':forests,'edge_subsets':1<<len(edges)}
    return {'full_passports':count,'forest_examples':forest_examples}


def finite_decoding(max_length=10):
    stack=[('',SEED)];seen=set();counts=[0]*(max_length+1)
    while stack:
        word,z=stack.pop()
        assert decode(z)==word and z not in seen
        seen.add(z);counts[len(word)]+=1
        if len(word)<max_length:
            for c in 'SLR':stack.append((word+c,matvec(INT_M[c],z)))
    # The invariant cone and Jacobi quadric alone do not characterize the orbit.
    twice=tuple(2*v for v in SEED)
    assert in_cone(twice) and quadric(twice)==0 and decode(twice) is None
    assert decode(SEED)=='' and decode_chain(SEED) is None
    assert decode_chain(matvec(INT_M['L'],SEED)) is None
    return {'lengths':list(range(max_length+1)),'counts':counts,'total':sum(counts),
            'rejected_candidate':list(twice),'inverse_S_of_seed':list(matvec(INT_INV['S'],SEED))}


if __name__=='__main__':
    result={'certificates':rational_certificates()}
    print('PASS: exact cone, sectors, inverses, and quadratic invariant',flush=True)
    result['direct_checks']=direct_checks()
    print('PASS: direct passports and independent forest enumeration',flush=True)
    result['decoding']=finite_decoding()
    print('PASS:',result['decoding']['total'],'decoded states',flush=True)
    z=SEED;example=[{'word':'','state':list(z),'sector':sector(z)}]
    for i,c in enumerate('LRS'):
        z=matvec(INT_M[c],z)
        example.append({'word':'LRS'[:i+1],'state':list(z),'sector':sector(z),
                        'U':9*z[1]-4*z[0],'V':9*z[2]-4*z[0]})
    result['example']=example
    result['matrices']={c:[list(row) for row in N] for c,N in INT_M.items()}
    result['inverse_matrices']={c:[list(row) for row in N] for c,N in INT_INV.items()}
    assert decode_chain(z)=='SLR'
    assert z[0]==220480560
    (ROOT/'decoding-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
