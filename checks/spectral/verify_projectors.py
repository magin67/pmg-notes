"""Exact C4 checks for eigenspaces, projector forms and complementary grades.

Uses fractions.Fraction and the existing exterior-algebra helpers. The original
and rotated modes have integer representatives; their squared lengths absorb
all square roots in the tensors. No files are written. Run without -O.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, prod
import json

from verify_diagonal import (scale, vector, square, form_matrix, grades,
                            exponential_from_factors, evaluate, matmul,
                            add, multiply, wedge, tensor, determinant, inverse,
                            laplacian, forest_partition, act)


def mscale(matrix, scalar):
    return [[scalar*v for v in row] for row in matrix]


def madd(a,b):
    return [[x+y for x,y in zip(rowa,rowb)] for rowa,rowb in zip(a,b)]


def projector(raw, norms):
    n = len(raw[0])
    return [[sum(F(q[i]*q[j],s) for q,s in zip(raw,norms))
             for j in range(n)] for i in range(n)]


def power(form,k):
    out = {(0,0):F(1)}
    for _ in range(k):
        out = multiply(out,form)
    return out


def exponential(form,d):
    out = {}
    for g in range(d+1):
        out = add(out,scale(power(form,g),F(1,factorial(g))))
    return out


def block_forms(s2,s4):
    return {(k,l):multiply(scale(power(s2,k),F(1,factorial(k))),power(s4,l))
            for k,l in product(range(3),range(2))}


def exterior_matrix(form,indices):
    masks = [sum(1<<i for i in I) for I in indices]
    return [[form.get((a,b),F(0)) for b in masks] for a in masks]


def check():
    n,d = 4,3
    edges = [(0,1,F(1)),(1,2,F(1)),(2,3,F(1)),(3,0,F(1))]
    L = laplacian(n,edges)
    identity = [[F(i==j) for j in range(n)] for i in range(n)]
    J = [[identity[i][j]-F(1,n) for j in range(n)] for i in range(n)]
    inv = inverse([[L[i][j]+F(1,n) for j in range(n)] for i in range(n)])
    Gr = [[v-F(1,n) for v in row] for row in inv]
    expected_green = [[F(v,16) for v in row] for row in
                      [[5,-1,-3,-1],[-1,5,-1,-3],[-3,-1,5,-1],[-1,-3,-1,5]]]
    assert Gr == expected_green
    assert matmul(L,Gr) == matmul(Gr,L) == J

    raw = [(1,0,-1,0),(0,1,0,-1),(1,-1,1,-1)]
    norms = [2,2,4]
    rotated = [(1,1,-1,-1),(-1,1,1,-1),(1,-1,1,-1)]
    rotated_norms = [4,4,4]
    lambdas = [F(2),F(2),F(4)]
    for vectors,lengths in [(raw,norms),(rotated,rotated_norms)]:
        for q,s,lam in zip(vectors,lengths,lambdas):
            assert sum(q)==0 and sum(v*v for v in q)==s
            assert [sum(x*y for x,y in zip(row,q)) for row in L] == [lam*v for v in q]
        for q,r in combinations(vectors,2):
            assert sum(x*y for x,y in zip(q,r))==0
    E2 = projector(raw[:2],norms[:2])
    E4 = projector(raw[2:],norms[2:])
    assert E2 == projector(rotated[:2],rotated_norms[:2])
    zero = [[F(0)]*n for _ in range(n)]
    assert matmul(E2,E2)==E2 and matmul(E4,E4)==E4
    assert matmul(E2,E4)==matmul(E4,E2)==zero
    assert madd(E2,E4)==J
    assert sum(E2[i][i] for i in range(n))==2
    assert sum(E4[i][i] for i in range(n))==1
    assert madd(mscale(E2,2),mscale(E4,4))==L
    assert madd(mscale(E2,F(1,2)),mscale(E4,F(1,4)))==Gr
    L2 = matmul(L,L)
    assert madd(L,mscale(L2,F(-1,4)))==E2
    assert madd(mscale(L2,F(1,8)),mscale(L,F(-1,4)))==E4
    # The positive-spectrum interpolation on H needs J, not I, when extended.
    assert madd(mscale(J,2),mscale(L,F(-1,2)))==E2

    A,B,C = [scale(square(q),F(1,s)) for q,s in zip(raw,norms)]
    Ar,Br,Cr = [scale(square(q),F(1,s)) for q,s in zip(rotated,rotated_norms)]
    S2,S4 = add(A,B),C
    assert add(Ar,Br)==S2 and Cr==C
    assert multiply(A,B)==multiply(Ar,Br)
    assert form_matrix(E2)==S2 and form_matrix(E4)==S4
    assert power(S2,2) and not power(S2,3) and not power(S4,2)
    assert multiply(S2,S4)
    blocks = block_forms(S2,S4)
    M_block = {}; N_block = {}
    for (k,l),form in blocks.items():
        coefficient = F(2**k*4**l)
        M_block = add(M_block,scale(form,coefficient))
        N_block = add(N_block,scale(form,1/coefficient))
        assert evaluate(form,identity)==comb(2,k)*comb(1,l)
        assert evaluate(form,Gr)==F(comb(2,k)*comb(1,l),coefficient)

    edge_forms = []
    for i,j,c in edges:
        q = [F(0)]*n; q[i],q[j] = -1,1
        edge_forms.append(scale(square(q),c))
    M_edges = exponential_from_factors(edge_forms)
    M_modes = exponential_from_factors([scale(a,l) for a,l in zip([A,B,C],lambdas)])
    M_rotated = exponential_from_factors([scale(a,l) for a,l in zip([Ar,Br,Cr],lambdas)])
    assert M_edges==M_modes==M_rotated==M_block
    assert N_block==exponential(form_matrix(Gr),d)
    Mg,Ng = grades(M_block,d),grades(N_block,d)

    # Each block is an actual orthogonal projector on the appropriate exterior power.
    for g in range(d+1):
        indices = list(combinations(range(n),g))
        matrices = [exterior_matrix(form,indices) for (k,l),form in blocks.items() if k+l==g]
        for matrix in matrices:
            assert matmul(matrix,matrix)==matrix
        for a,b in combinations(matrices,2):
            assert not any(v for row in matmul(a,b) for v in row)
        compound = [[determinant([[L[i][j] for j in K] for i in I]) for K in indices] for I in indices]
        assert exterior_matrix(Mg[g],indices)==compound

    # Independent reduced coordinates b_i=a_i-a_4 and their algebraic duals.
    direct = [q[:d] for q in raw]
    dual = [[q[i]-q[-1] for i in range(d)] for q in raw]
    direct_forms = [scale(square(q),F(1,s)) for q,s in zip(direct,norms)]
    dual_forms = [scale(square(q),F(1,s)) for q,s in zip(dual,norms)]
    rb = block_forms(add(direct_forms[0],direct_forms[1]),direct_forms[2])
    qb = block_forms(add(dual_forms[0],dual_forms[1]),dual_forms[2])
    Mr = grades(exponential_from_factors([scale(a,l) for a,l in zip(direct_forms,lambdas)]),d)
    Q = grades(exponential_from_factors([scale(a,1/l) for a,l in zip(dual_forms,lambdas)]),d)
    reduced_L = [row[:d] for row in L[:d]]
    assert Q[1]==form_matrix(inverse(reduced_L))
    for g in range(d+1):
        assert act(Mr[d],Q[g])==Mr[d-g]
        assert act(Q[d],Mr[g])==Q[d-g]
    delta = prod(lambdas)
    unit_top = scale(Mr[d],1/delta)
    for (k,l),form in qb.items():
        assert act(unit_top,form)==rb[(2-k,1-l)]
    centered = [[F(i==j)-F(1,n) for j in range(n)] for i in range(d)]
    C_factors = []
    for q,s,lam in zip(dual,norms,lambdas):
        cq = [sum(q[i]*centered[i][j] for i in range(d)) for j in range(n)]
        C_factors.append(scale(square(cq),1/(s*lam)))
    assert grades(exponential_from_factors(C_factors),d)==Ng

    boundary = {0:F(1)}
    for i in range(d):
        q = [F(j==i)-F(j==d) for j in range(n)]
        boundary = wedge(boundary,vector(q))
    T = tensor(boundary,boundary)
    tau = determinant(reduced_L)
    assert tau==4 and delta==n*tau==16
    assert Mg[d]==scale(T,4) and Ng[d]==scale(T,F(1,64))
    assert multiply(multiply(A,B),C)==scale(T,F(1,4))

    p = [evaluate(form,identity) for form in Mg]
    pgr = [evaluate(form,identity) for form in Ng]
    assert p==[1,8,20,16] and pgr==[1,F(5,4),F(1,2),F(1,16)]
    assert pgr==[v/delta for v in reversed(p)]
    assert [evaluate(form,Gr) for form in Mg]==[1,3,3,1]
    assert [evaluate(form,L) for form in Ng]==[1,3,3,1]
    ordinary = [F(0)]*n; rooted = [F(0)]*n
    for g in range(len(edges)+1):
        for subset in combinations(edges,g):
            components = forest_partition(n,subset)
            if components is not None:
                weight = prod(c for _,_,c in subset)
                ordinary[g] += weight
                rooted[g] += weight*prod(map(len,components))
    assert ordinary==[1,4,6,4] and rooted==p

    R = [[Gr[i][i]+Gr[j][j]-2*Gr[i][j] for j in range(n)] for i in range(n)]
    contributions = []
    for i,j in [(0,1),(0,2)]:
        values = [(E[i][i]+E[j][j]-2*E[i][j])/lam for E,lam in [(E2,F(2)),(E4,F(4))]]
        assert sum(values)==R[i][j]
        contributions.append(values)
    assert contributions==[[F(1,2),F(1,4)],[F(1),F(0)]]
    mode_contributions = [[F((q[1]-q[0])**2,s)/2 for q,s in zip(vectors[:2],lengths[:2])]
                          for vectors,lengths in [(raw,norms),(rotated,rotated_norms)]]
    assert mode_contributions==[[F(1,4),F(1,4)],[F(0),F(1,2)]]
    Kf = sum(R[i][j] for i,j in combinations(range(n),2))
    assert Kf==n*sum(Gr[i][i] for i in range(n))==5
    return dict(graph="C4", raw_modes=raw, squared_lengths=norms,
                rotated_modes=rotated, rotated_squared_lengths=rotated_norms,
                E2=[[str(v) for v in row] for row in E2],
                spectrum=[0,2,2,4], rooted=list(map(str,p)),green_rooted=list(map(str,pgr)),
                ordinary=list(map(str,ordinary)),tau=str(tau),delta=str(delta),
                green_top_coefficient="1/64",Kirchhoff_index=str(Kf),
                resistance_contributions=[[str(v) for v in row] for row in contributions],
                mode_contributions=[[str(v) for v in row] for row in mode_contributions],
                checks="two bases, polynomial projectors, all six exterior blocks, edge expansion, contractions, C, forests, metrics")


if __name__=="__main__":
    print(json.dumps(check(),ensure_ascii=False,indent=2))
