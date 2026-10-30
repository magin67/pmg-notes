"""Exact continuant checks against assembled graphs; Python standard library."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb, prod
from pathlib import Path
import json

from verify_admissible_chains import cycle, determinant, laplacian, validate
from verify_matroid_invariance import configuration, dual_data


def recurrence(sizes, seams):
    values = [1]
    for j, m in enumerate(sizes):
        values.append(m * values[-1] - ((seams[j-1]-1)**2 * values[-2] if j else 0))
    return values


def tridiagonal(sizes, seams):
    n = len(sizes)
    return [[sizes[i] if i == j else -(seams[min(i,j)]-1) if abs(i-j) == 1 else 0
             for j in range(n)] for i in range(n)]


def matchings(n):
    for k in range(n//2+1):
        for es in combinations(range(n-1), k):
            if all(b > a+1 for a,b in zip(es,es[1:])):
                yield es


def matching_sum(sizes, seams):
    return sum((-1)**len(es) * prod((seams[i]-1)**2 for i in es) *
               prod(m for i,m in enumerate(sizes) if all(i not in (e,e+1) for e in es))
               for es in matchings(len(sizes)))


def polynomial_add(*terms):
    out = defaultdict(int)
    for p in terms:
        for k,v in p.items():
            out[k] += v
    return {k:v for k,v in out.items() if v}


def shifted(p, offset, factor=1):
    return {k+offset:factor*v for k,v in p.items() if factor*v}


def normalized(n):
    a,b = {0:1},{0:1}
    for _ in range(2,n+1):
        a,b = b,polynomial_add(b,shifted(a,2,-1))
    return a if n == 0 else b


def multiply(a,b):
    return polynomial_add(*(shifted(b,k,v) for k,v in a.items()))


def chebyshev_u(n):
    a,b = {0:1},{1:2}
    for _ in range(2,n+1):
        a,b = b,polynomial_add(shifted(b,1,2),shifted(a,0,-1))
    return a if n == 0 else b


def evaluate(p,x):
    return sum(v*x**k for k,v in p.items())


def formal_continuant(n):
    """Compare multivariate coefficients from all permutations and matchings."""
    width = 2*n-1
    det = defaultdict(int)
    for perm in permutations(range(n)):
        if any(abs(i-j)>1 for i,j in enumerate(perm)):
            continue
        sign = (-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        powers = [0]*width
        for i,j in enumerate(perm):
            if i == j:
                powers[i] += 1
            else:
                powers[n+min(i,j)] += 1
                sign *= -1
        det[tuple(powers)] += sign
    matched = defaultdict(int)
    for es in matchings(n):
        covered = {v for e in es for v in (e,e+1)}
        powers = [int(i not in covered) for i in range(n)]+[2*int(i in es) for i in range(n-1)]
        matched[tuple(powers)] += (-1)**len(es)
    assert dict(det) == dict(matched)
    assert all(sum(p)==n for p in det)
    return len(det)


def check_graph(name, sizes, seams, reverse=False, starts=None):
    if starts is None:
        starts = [0]+seams[:-1] if seams else []
    cores, joins = configuration(sizes,seams,starts,[reverse]*len(seams))
    vertices, edges = validate(cores,joins)
    expected = recurrence(sizes,seams)
    direct = [1]
    for j in range(1,len(sizes)+1):
        vs,es = validate(cores[:j],joins[:j-1])
        L = laplacian(vs,es)
        tau = determinant([row[:-1] for row in L[:-1]])
        M = tridiagonal(sizes[:j],seams[:j-1])
        assert tau == expected[j] == determinant(M) == matching_sum(sizes[:j],seams[:j-1])
        # Build the dual cofactor from edge memberships, independently of M.
        _,_,dual,_ = dual_data(cores[:j],joins[:j-1])
        DL = [[0]*(j+1) for _ in range(j+1)]
        for a,b in dual:
            DL[a][a] += 1; DL[b][b] += 1
            DL[a][b] -= 1; DL[b][a] -= 1
        assert [row[1:] for row in DL[1:]] == M
        direct.append(int(tau))
    assert expected[-1] == recurrence(sizes[::-1],seams[::-1])[-1]
    for i,s in enumerate(seams):
        if s == 1:
            assert expected[-1] == recurrence(sizes[:i+1],seams[:i])[-1] * recurrence(sizes[i+1:],seams[i+1:])[-1]
    # A rational row normalization verifies the determinant without square roots.
    scaled = [[Q(v,sizes[i]) for v in row] for i,row in enumerate(tridiagonal(sizes,seams))]
    assert determinant(scaled) == Q(expected[-1],prod(sizes))
    return dict(name=name, sizes=sizes, seams_in_vertices=seams, starts=starts,
                reverse=reverse, cores=cores, seams=joins,
                vertex_identifications=[[[cores[i].index(v),cores[i+1].index(v),v] for v in join]
                                        for i,join in enumerate(joins)],
                vertices=sorted(vertices), edges=sorted(edges), n=len(vertices), E=len(edges),
                tau=expected[-1], prefix_tau_from_original_laplacians=direct)


def main():
    cases=[]
    def add(name,m,s,**kw):
        cases.append(check_graph(name,m,s,**kw))
    for m in (3,4,6):
        add(f'single_{m}',[m],[])
    for s in range(1,6):
        for reverse in (False,True):
            add(f'two_6_7_s{s}_r{int(reverse)}',[6,7],[s],reverse=reverse)
    for n in range(3,7):
        for m in (4,6,8):
            for s in sorted({1,2,m//2}):
                add(f'homogeneous_{n}_{m}_{s}',[m]*n,[s]*(n-1))
                tau=cases[-1]['tau']
                assert Q(tau,m**n) == evaluate(normalized(n),Q(s-1,m))
    add('mixed_3_4_5_6',[3,4,5,6],[1,2,3])
    add('mixed_3_4_5_6_reversed',[6,5,4,3],[3,2,1],reverse=True)
    add('mixed_three_1_2',[3,5,6],[1,2])
    add('mixed_three_2_1',[3,5,6],[2,1])
    add('mixed_three_reversed_1_2',[6,5,3],[2,1])
    add('hexagons_opposite',[6,6,6],[2,2],starts=[0,3])
    for seam_set in ((1,2,3),(2,3,4)):
        for order in permutations(seam_set):
            for reverse in (False,True):
                s=list(order)
                add('order_'+''.join(map(str,s))+f'_r{int(reverse)}',[8]*4,s,reverse=reverse)
                assert cases[-1]['tau'] == 8**4-8**2*sum((v-1)**2 for v in s)+(s[0]-1)**2*(s[2]-1)**2
    expected = {'mixed_3_4_5_6':294,'mixed_three_1_2':87,'mixed_three_2_1':84,'mixed_three_reversed_1_2':87,
                'homogeneous_3_6_2':204,'homogeneous_3_8_3':448,
                'order_123_r0':3776,'order_213_r0':3780,'order_132_r0':3776}
    # The three-octagon example is not one of the homogeneous boundary cases.
    add('homogeneous_3_8_3',[8]*3,[3,3])
    actual={c['name']:c['tau'] for c in cases}
    assert all(actual[k]==v for k,v in expected.items())
    symbolic=[]
    for n in range(21):
        d=normalized(n)
        explicit={2*k:(-1)**k*comb(n-k,k) for k in range(n//2+1)}
        from_u={n-k:Q(v,2**k) for k,v in chebyshev_u(n).items()}
        assert d == explicit == from_u
        assert evaluate(d,Q(0)) == 1
        assert evaluate(d,Q(1,2)) == Q(n+1,2**n)
        symbolic.append({'N':n,'D_coefficients':{str(k):v for k,v in sorted(d.items())}})
    for a in range(1,9):
        for b in range(1,9):
            assert normalized(a+b)==polynomial_add(multiply(normalized(a),normalized(b)),shifted(multiply(normalized(a-1),normalized(b-1)),2,-1))
    formal={str(n):formal_continuant(n) for n in range(1,8)}
    # Characteristic polynomial of path adjacency, by determinant evaluations.
    for n in range(1,9):
        for xi in map(Q,[-3,-1,0,1,2,3]):
            A=[[xi if i==j else -1 if abs(i-j)==1 else 0 for j in range(n)] for i in range(n)]
            assert determinant(A)==evaluate(chebyshev_u(n),xi/2)
    result={'graph_count':len(cases),'prefix_laplacian_checks':sum(len(c['sizes']) for c in cases),
            'formal_continuants_N_1_to_7':formal,'normalized_polynomials':symbolic,'graphs':cases,
            'scope':'Finite exact checks support the examples; general identities are proved in the note.'}
    Path(__file__).with_name('spanning-polynomials-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'graphs':len(cases),'prefix_laplacian_checks':result['prefix_laplacian_checks'],
                      'formal_continuants':7,'normalized_polynomials':21,'examples':expected},ensure_ascii=False))


if __name__=='__main__':
    main()
