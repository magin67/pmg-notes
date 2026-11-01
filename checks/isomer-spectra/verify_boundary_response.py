"""Exact boundary response, recovery, and stability certificates."""
from pathlib import Path
from itertools import product, combinations
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm, isqrt
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
import verify_decoding as v

SEED=v.SEED
M=v.INT_M
INV=v.INT_INV
AMIN=F(349,4)
BMAX=F(11131,125)
BOX=list(zip(map(F,v.lo),map(F,v.hi)))


def working(word):
    z=SEED
    for c in word:z=v.matvec(M[c],z)
    return z


def normalized(z):
    return tuple(F(x,z[0]) for x in z[1:])


def response(z):
    return normalized(z)[:3]


def recover(r,s,h):
    z=(F(1),r,s,h,r*s-h*h)
    scale=lcm(*(x.denominator for x in z))
    return tuple(int(scale*x) for x in z)


def projective(letter,p,backward=False):
    z=(F(1),)+tuple(p)
    q=v.matvec(INV[letter] if backward else M[letter],z)
    assert q[0]>0
    return tuple(x/q[0] for x in q[1:])


def contraction_certificates():
    bounds={}
    for letter,N in v.M.items():
        rows=[]
        for i in range(1,5):
            numerator=[max(abs(N[i,j]*(N*z)[0]-N[0,j]*(N*z)[i])
                           for z in v.corners) for j in range(1,5)]
            rows.append(F(sum(numerator))/AMIN**2)
        assert max(rows)<(F(3,100) if letter=='S' else F(3,20))
        bounds[letter]={'row_bounds':rows,'maximum':max(rows)}
    sector=F(639,500)/(9*BMAX)
    seed_gap=F(123,400)/BMAX
    assert sector==F(71,44524) and sector<seed_gap/2
    eigen_lower=BOX[0][0]-BOX[2][1]
    eigen_upper=BOX[0][1]+BOX[2][1]
    assert eigen_lower==F(51,200) and eigen_upper==F(5,8)
    return {'jacobian_row_sums':bounds,'sector_margin':sector,'seed_gap':seed_gap,
            'seed_threshold':F(9,20)-seed_gap/2,
            'response_eigenvalue_bounds':[eigen_lower,eigen_upper],
            'response_condition_bound':eigen_upper/eigen_lower}


def exact_recovery(max_length=8):
    count=0; seen=set()
    assert reduce(gcd,SEED)==1 and recover(*response(SEED))==SEED
    for m in range(max_length+1):
        for letters in product('SLR',repeat=m):
            u=''.join(letters);z=working(u+'S');p=normalized(z)
            assert reduce(gcd,z)==1
            assert recover(*p[:3])==z
            assert v.decode_chain(recover(*p[:3]))=='S'+u
            assert p[3]==p[0]*p[1]-p[2]**2
            # Only the joint law of the two root indicators is needed.
            variance_gap=p[0]*p[1]-p[3]
            num,den=isqrt(variance_gap.numerator),isqrt(variance_gap.denominator)
            assert num*num==variance_gap.numerator and den*den==variance_gap.denominator
            h_from_roots=F(num,den)
            assert h_from_roots==p[2] and recover(p[0],p[1],h_from_roots)==z
            assert p[:3] not in seen
            seen.add(p[:3]);count+=1
            previous=projective('S',p,True)
            assert previous==normalized(working(u))
    return {'full_states':count,'max_turn_length':max_length,'plus_single_C6':1}


def direct_models():
    examples={};count=0;forest_count=0
    for u in [None]+[''.join(w) for m in range(3) for w in product('SLR',repeat=m)]:
        if u is None:
            edges={tuple(sorted((i,(i+1)%6))):1 for i in range(6)}
            n=6;B=(0,1);z=SEED;name='C6'
        else:
            g,_,B,edges=v.graph(u);n=len(g);z=working(u+'S');name='S'+u
        L=v.laplacian(edges,n);H=sp.eye(n)+L
        # Build the grounded electrical graph independently of the transfer.
        augmented=dict(edges)
        augmented.update({(i,n):1 for i in range(n)})
        ground_L=v.laplacian(augmented,n+1)
        assert ground_L[:n,:n]==H
        injections=sp.zeros(n,2)
        for j,b in enumerate(B):injections[b,j]=1
        voltages=H.inv()*injections
        K=voltages.extract(B,[0,1])
        a,b,c,d,e=z
        expected=sp.Matrix([[sp.Rational(b,a),sp.Rational(d,a)],
                            [sp.Rational(d,a),sp.Rational(c,a)]])
        assert K==expected
        interior=[i for i in range(n) if i not in B]
        schur=H.extract(B,B)-H.extract(B,interior)*H.extract(interior,interior).inv()*H.extract(interior,B)
        assert schur==K.inv()==sp.Matrix([[c,-d],[-d,b]])/e
        # Embedded killed walk: each neighbor and the killing action have
        # probability 1/(degree+1). This is not a unit-rate simple random walk.
        degree=sp.diag(*[L[i,i] for i in range(n)])
        adjacency=degree-L
        kill=(sp.eye(n)+degree).inv()
        P=kill*adjacency
        W=(sp.eye(n)-P).inv()*kill
        assert W==H.inv() and W*sp.ones(n,1)==sp.ones(n,1)
        assert W.extract(B,B)==K
        if name in ('C6','S','SS','SL'):
            enumerated=v.forest_counts(edges,n,B)
            assert tuple(enumerated)==z
            forest_count+=1
        if name in ('C6','SS','SL','SLR'):
            examples[name]={'n':n,'boundary':list(B),'state':z,
                            'K':K.tolist(),'Lambda':schur.tolist()}
        count+=1
    # The published independent forest enumeration supplies counts of events.
    forest_data=json.loads((ROOT/'decoding-results.json').read_text(encoding='utf-8'))
    for key,item in forest_data['direct_checks']['forest_examples'].items():
        a,b,c,d,e=item['state']
        r,s,h=F(b,a),F(c,a),F(d,a)
        assert F(e,a)==r*s-h*h
        assert F(e,a)-r*s==-h*h
    return {'direct_graphs':count,'independent_forest_enumerations':forest_count,
            'forest_event_checks':4,'examples':examples}


def hidden_bend(max_k=12):
    straight=working('S');bend=working('L')
    initial=max(abs(x-y) for x,y in zip(normalized(straight),normalized(bend)))
    assert initial==F(3,235)
    result=[]
    for k in range(1,max_k+1):
        straight=v.matvec(M['S'],straight);bend=v.matvec(M['S'],bend)
        p,q=normalized(straight),normalized(bend)
        delta=max(abs(p[i]-q[i]) for i in range(3))
        delta4=max(abs(x-y) for x,y in zip(p,q))
        upper=initial*F(3,100)**k
        assert 0<delta<=delta4<=upper
        assert v.decode_chain(straight)=='S'*(k+1)
        assert v.decode_chain(bend)=='SL'+'S'*(k-1)
        result.append({'N':k+2,'straight':'S'*(k+1),'one_bend':'SL'+'S'*(k-1),
                       'entry_distance':delta,'decimal':float(delta),'upper_bound':upper})
    return result


def distance(p,q):
    return max(abs(x-y) for x,y in zip(p,q))


def finite_catalogue(max_N=7):
    states=[('C6',1,response(SEED))]
    for N in range(2,max_N+1):
        for letters in product('SLR',repeat=N-2):
            u=''.join(letters)
            states.append(('S'+u,N,response(working(u+'S'))))
    summaries=[]
    for limit in range(3,max_N+1):
        entries=[e for e in states if e[1]<=limit]
        minimum=None;pair=None
        for (w1,_,p1),(w2,_,p2) in combinations(entries,2):
            d=distance(p1,p2)
            assert d>0
            if minimum is None or d<minimum:minimum=d;pair=[w1,w2]
        cap=(320*BMAX**(limit-1)).__ceil__()
        assert minimum>=F(1,cap*cap)
        summaries.append({'max_N':limit,'states':len(entries),'minimum':minimum,
                          'decimal':float(minimum),'closest_pair':pair,
                          'denominator_bound':cap,'safe_error_bound':F(1,2*cap*cap)})
    # One measurement box admits two distinct (non-isomorphic) graphs.
    p=response(working('S'*6));q=response(working('L'+'S'*5))
    middle=tuple((x+y)/2 for x,y in zip(p,q));eps=distance(p,q)/2
    matches=[w for w,N,x in states if distance(x,middle)<=eps]
    assert 'SSSSSS' in matches and 'SLSSSS' in matches
    exact=response(working('LRS'))
    rounded=tuple(F(round(x*10**14),10**14) for x in exact)
    round_error=F(1,2*10**14)
    assert distance(exact,rounded)<=round_error
    unique=[w for w,N,x in states if distance(x,rounded)<=round_error]
    assert unique==['SLR']
    return {'separation':summaries,
            'ambiguous_example':{'measurement':middle,'error':eps,'matches':matches},
            'rounded_example':{'measurement':rounded,'error':round_error,'matches':unique}}


def interval(lo,hi=None):return (F(lo),F(lo if hi is None else hi))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    vals=[a*b for a in x for b in y]
    return (min(vals),max(vals))
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))


def interval_tail(K,eps,max_steps,known_operations=None):
    r,s,h=[interval(x-eps,x+eps) for x in K]
    assert h[0]>0
    k=add(mul(r,s),(-h[1]**2,-h[0]**2))
    box=[r,s,h,k];letters=[];trace=[]
    for _ in range(max_steps):
        if all(lo<=x<=hi for x,(lo,hi) in zip(normalized(SEED),box)):
            return {'confirmed_backwards':''.join(letters),'stop':'initial state not excluded','trace':trace}
        a,b=box[0],box[1];threshold=F(4,9)
        sig=lambda t: 1 if t[0]>threshold else -1 if t[1]<threshold else 0
        letter={(1,1):'S',(-1,1):'L',(1,-1):'R'}.get((sig(a),sig(b)))
        if letter is None:return {'confirmed_backwards':''.join(letters),'stop':'ambiguous sector','trace':trace}
        inp=[interval(1)]+box
        out=[]
        for row in INV[letter]:
            total=interval(0)
            for coefficient,x in zip(row,inp):total=add(total,mul(interval(coefficient),x))
            out.append(total)
        if out[0][0]<=0:return {'confirmed_backwards':''.join(letters)+letter,'stop':'inverse denominator uncertified','trace':trace}
        box=[div(x,out[0]) for x in out[1:]]
        letters.append(letter)
        if known_operations is not None:
            truth=normalized(working(known_operations[:-len(letters)]))
            assert all(lo<=x<=hi for x,(lo,hi) in zip(truth,box))
        trace.append({'letter':letter,'max_width':max(y-x for x,y in box)})
    return {'confirmed_backwards':''.join(letters),'stop':'specified depth reached','trace':trace}


def interval_examples():
    code='SLRSSLR'
    operations=code[1:]+'S'
    K=response(working(operations))
    examples=[]
    for exponent in (4,6,8,10,12,16,20):
        eps=F(1,10**exponent)
        result=interval_tail(K,eps,len(operations),operations)
        assert operations[::-1].startswith(result['confirmed_backwards'])
        examples.append({'epsilon':eps,**result})
    return {'code':code,'operations':operations,'examples':examples}


def encode(x):
    if isinstance(x,(F,sp.Rational,sp.Integer)):return str(x)
    raise TypeError(type(x))


if __name__=='__main__':
    data={'transfer_certificates':v.rational_certificates(),
          'certificates':contraction_certificates()}
    print('PASS: rational contraction and sector certificates',flush=True)
    data['direct_models']=direct_models()
    print('PASS: direct electrical, Schur, killed-walk, and forest interpretations',flush=True)
    data['recovery']=exact_recovery()
    print('PASS: exact recovery',data['recovery'],flush=True)
    data['hidden_bend']=hidden_bend()
    data['catalogue']=finite_catalogue()
    data['intervals']=interval_examples()
    (ROOT/'boundary-response-results.json').write_text(json.dumps(data,default=encode,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: hidden-bend family, exact finite separations, and interval examples',flush=True)
    for row in data['catalogue']['separation']:
        print('N <=',row['max_N'],'states',row['states'],'minimum',row['decimal'],'pair',row['closest_pair'])
    for row in data['intervals']['examples']:
        print('epsilon',str(row['epsilon']),'certified',row['confirmed_backwards'],row['stop'])
