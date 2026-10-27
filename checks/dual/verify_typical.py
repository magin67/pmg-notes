"""Exact verification for 'Экспоненты гринианов типовых графов'.

Run: python checks/dual/verify_typical.py
Standard library only. Does not write files. JSON output contains exact fractions.
Vector factors and all minors are compared in every grade, including Petersen.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import lcm, prod, comb
import json

from verify_vector import inverse, laplacian, determinant, forest_partition


def det_int(matrix):
    """Fraction-free elimination; includes empty and singular minors."""
    a = [list(row) for row in matrix]
    n = len(a)
    if not n:
        return 1
    previous, sign = 1, 1
    for k in range(n - 1):
        p = next((i for i in range(k, n) if a[i][k]), None)
        if p is None:
            return 0
        if p != k:
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in partitions(rest):
        yield ((first,),) + partition
        for i, block in enumerate(partition):
            yield partition[:i] + ((first,) + block,) + partition[i + 1:]


def matrix_data(n, edges):
    L = laplacian(n, edges)
    H = inverse([[L[i][j] + F(1, n) for j in range(n)] for i in range(n)])
    Gr = [[H[i][j] - F(1, n) for j in range(n)] for i in range(n)]
    pairs = [(i, j, -Gr[i][j]) for i, j in combinations(range(n), 2)]
    tau = determinant([row[:-1] for row in L[:-1]])
    assert laplacian(n, pairs) == Gr
    assert determinant([row[:-1] for row in Gr[:-1]]) == 1 / (n*n*tau)
    for i in range(n):
        for j in range(n):
            assert sum(L[i][k] * Gr[k][j] for k in range(n)) == int(i == j)-F(1,n)
    return L, Gr, pairs, tau


def vector_factors(n, pairs, scale):
    """Integer coefficients of exp(scale*Q1) in a_1,...,a_(n-1)."""
    d = n - 1
    vertices = [[int(i == j) for j in range(d)] for i in range(d)] + [[-1]*d]
    # mask -> possible singleton extensions and their exterior signs
    extensions = {}
    for mask in range(1 << d):
        extensions[mask] = [(i, mask | (1 << i), (-1)**((mask >> (i+1)).bit_count()))
                            for i in range(d) if not mask >> i & 1]
    grades = [{(0, 0): 1}] + [{} for _ in range(d)]
    for i, j, weight in pairs:
        weight = weight * scale
        assert weight.denominator == 1
        weight = int(weight)
        if not weight:
            continue
        u = [vertices[j][r] - vertices[i][r] for r in range(d)]
        ext = {mask: [(new, sign*u[r]) for r,new,sign in es if u[r]]
               for mask, es in extensions.items()}
        for k in range(d, 0, -1):
            target = grades[k]
            for (a,b), value in grades[k-1].items():
                value *= weight
                for aa, ca in ext[a]:
                    for bb, cb in ext[b]:
                        key = (aa,bb)
                        target[key] = target.get(key, 0) + value*ca*cb
            grades[k] = {key:value for key,value in target.items() if value}
    return grades


def all_minors(matrix):
    d = len(matrix)
    result = []
    for k in range(d+1):
        out = {}
        choices = [(I, sum(1 << i for i in I)) for I in combinations(range(d),k)]
        for I, a in choices:
            for J, b in choices:
                value = det_int([[matrix[i][j] for j in J] for i in I])
                if value:
                    out[a,b] = value
        result.append(out)
    return result


def coefficients_by_partitions(n, pairs, scale):
    """Tree weights of induced signed graphs, then all set partitions."""
    weights = {(i,j):int(c*scale) for i,j,c in pairs}
    blocks = {}
    for size in range(1,n+1):
        for B in combinations(range(n),size):
            L = [[0]*size for _ in B]
            for i,j in combinations(range(size),2):
                c = weights[tuple(sorted((B[i],B[j])))]
                L[i][i] += c; L[j][j] += c
                L[i][j] -= c; L[j][i] -= c
            blocks[B] = det_int([row[:-1] for row in L[:-1]])
    sums, rooted = [0]*n, [0]*n
    type_sums = Counter()
    for partition in partitions(list(range(n))):
        k = n-len(partition)
        coefficient = prod(blocks[B] for B in partition)
        sums[k] += coefficient
        rooted[k] += coefficient*prod(map(len,partition))
        typ = tuple(sorted((len(B)-1 for B in partition if len(B)>1),reverse=True))
        type_sums[typ] += coefficient
    return ([F(c,scale**k) for k,c in enumerate(sums)],
            [F(c,scale**k) for k,c in enumerate(rooted)], type_sums, blocks)


def verify(name,n,edges):
    L,Gr,pairs,tau = matrix_data(n,edges)
    scale = lcm(*(c.denominator for _,_,c in pairs))
    Ai = inverse([row[:-1] for row in L[:-1]])
    S = [[x*scale for x in row] for row in Ai]
    assert all(x.denominator == 1 for row in S for x in row)
    S = [[int(x) for x in row] for row in S]
    grades = vector_factors(n,pairs,scale)
    assert grades == all_minors(S)
    sums,rooted,types,blocks = coefficients_by_partitions(n,pairs,scale)
    P = [sum(determinant([[L[i][j] for j in I] for i in I])
             for I in combinations(range(n),k)) for k in range(n)]
    assert rooted == [x/(n*tau) for x in reversed(P)]
    assert sums[-1] == 1/(n*n*tau)
    top = (1 << (n-1))-1
    assert grades[-1] == {(top,top):scale**(n-1)/tau}
    triples = {''.join(str(i+1) for i in B):str(F(blocks[B],scale**2))
               for B in combinations(range(n),3)}
    if name == 'Petersen':
        E = {tuple(sorted((i,j))) for i,j,_ in edges}
        assert all(c == (-F(3,100) if (i,j) in E else F(7,100)) for i,j,c in pairs)
        counts = Counter(sum(tuple(sorted(e)) in E for e in combinations(B,2))
                         for B in combinations(range(n),3))
        assert counts == {0:30,1:60,2:30}
        for B in combinations(range(n),3):
            r = sum(tuple(sorted(e)) in E for e in combinations(B,2))
            assert blocks[B] == [147,7,-33][r]
        # Different verification of every induced block coefficient:
        # K_B = (7/100)(sI-11^T) - (1/10)L(Petersen[B]).
        for B,value in blocks.items():
            size=len(B)
            H=laplacian(size,[(i,j,1) for i,j in combinations(range(size),2)
                             if tuple(sorted((B[i],B[j]))) in E])
            K=[[7*(size*int(i==j)-1)-10*int(H[i][j])
                for j in range(size)] for i in range(size)]
            assert value == det_int([row[:-1] for row in K[:-1]])
    if name.startswith('C'):
        for i,j,c in pairs:
            s=j-i
            assert c==F(s*(n-s),2*n)-F(n*n-1,12*n)
    if name=='star4':
        assert all(c==F(1 if i==0 else n+1,n*n) for i,j,c in pairs)
    return dict(graph=name,n=n,tau=str(tau),scale=scale,
                gamma={f'{i+1}{j+1}':str(c) for i,j,c in pairs},
                signed_sums=list(map(str,sums)),rooted_sums=list(map(str,rooted)),
                triple_coefficients=triples if n<=6 else dict(Counter(triples.values())),
                type_sums={str(typ):str(F(c,scale**sum(typ))) for typ,c in sorted(types.items())},
                grades_checked=n,minor_coefficients_checked=comb(2*n-2,n-1))


def check_families():
    # Checks general complete/star formulas, independently of displayed examples.
    for n in range(2,9):
        for conductance in [F(1),F(3,2)]:
            _,_,pairs,_=matrix_data(n,[(i,j,conductance) for i,j in combinations(range(n),2)])
            assert all(c==1/(n*n*conductance) for _,_,c in pairs)
        _,star_Gr,pairs,_=matrix_data(n,[(0,j,1) for j in range(1,n)])
        assert all(c==F(1 if i==0 else n+1,n*n) for i,j,c in pairs)
        for B in combinations(range(n),min(n,4)):
            s=len(B)
            H=laplacian(s,[(i,j,-star_Gr[B[i]][B[j]])
                           for i,j in combinations(range(s),2)])
            actual=determinant([r[:-1] for r in H[:-1]])
            if 0 in B:
                r=s-1
                expected=F(1,n*n)*F(1+r*(n+1),n*n)**(r-1)
            else:
                expected=s**(s-2)*F(n+1,n*n)**(s-1)
            assert actual==expected


if __name__=='__main__':
    cases=[
        ('K4',4,[(i,j,1) for i,j in combinations(range(4),2)]),
        ('star4',4,[(0,j,1) for j in range(1,4)]),
        *[(f'C{n}',n,[(i,(i+1)%n,1) for i in range(n)]) for n in [4,5,6]],
        ('K4minus',4,[(i,j,1) for i,j in combinations(range(4),2) if (i,j)!=(0,1)]),
        ('weightedP4',4,[(0,1,2),(1,2,3),(2,3,5)]),
        ('Wikipedia',6,[(0,1,1),(0,4,1),(1,2,1),(1,4,1),(2,3,1),(3,4,1),(3,5,1)]),
        ('Petersen',10,[(i,(i+1)%5,1) for i in range(5)]
         +[(i,i+5,1) for i in range(5)]+[(i+5,(i+2)%5+5,1) for i in range(5)])]
    check_families()
    print(json.dumps([verify(*case) for case in cases],ensure_ascii=False,indent=2))

