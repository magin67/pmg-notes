"""Exact checks for the polyform exponential under graph weaving.

Python 3.10+ and SymPy. No floating-point arithmetic; run without -O.
Boundary size transfer, exhaustive forests, and Laplacian minors are independent.
"""
from collections import Counter
from itertools import combinations, product
from math import prod
from pathlib import Path
import json
import sympy as sp

t = sp.Symbol('t')


def find(parent, a):
    while parent[a] != a:
        a = parent[a]
    return a


def join(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a == b:
        return False
    parent[b] = a
    return True


def forest_data(n, edges, boundary):
    """Independent exhaustive edge-subset enumeration, including isolates."""
    types, states = Counter(), Counter()
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        for i, (a, b) in enumerate(edges):
            if mask >> i & 1 and not join(parent, a, b):
                break
        else:
            blocks = Counter(find(parent, i) for i in range(n))
            roots = tuple(find(parent, i) for i in boundary)
            active = (blocks[roots[0]],) if roots[0] == roots[1] else tuple(blocks[r] for r in roots)
            closed = tuple(sorted(s for r, s in blocks.items() if r not in roots and s > 1))
            states[(active, closed)] += 1
            types[tuple(sorted(s-1 for s in blocks.values() if s > 1))] += 1
    return types, states


def step(states, m, output, reverse=False):
    """Runner P_m: endpoints 0,m-1 are inputs; output is a path edge."""
    result = Counter()
    for (active, closed), count in states.items():
        sizes = active[::-1] if reverse else active
        connected = len(sizes) == 1
        weights = list(sizes) + [1]*(m-2)
        offset = len(sizes)
        mapping = {0: 0, m-1: 0 if connected else 1}
        mapping.update({i: offset+i-1 for i in range(1, m-1)})
        for mask in range(1 << (m-1)):
            parent = list(range(len(weights)))
            for i in range(m-1):
                if mask >> i & 1 and not join(parent, mapping[i], mapping[i+1]):
                    break
            else:
                totals = Counter()
                for i, weight in enumerate(weights):
                    totals[find(parent, i)] += weight
                roots = tuple(find(parent, mapping[i]) for i in output)
                anew = (totals[roots[0]],) if roots[0] == roots[1] else tuple(totals[r] for r in roots)
                cnew = tuple(sorted(closed + tuple(s for r,s in totals.items() if r not in roots and s > 1)))
                result[(anew,cnew)] += count
    return result


def square_explicit_step(states):
    """Independently written seven/eight-term local rules, t-grading implicit."""
    result = Counter()
    for (a,c), weight in states.items():
        def add(active, newclosed=(), multiplicity=1):
            result[(active, tuple(sorted(c+tuple(x for x in newclosed if x>1))))] += weight*multiplicity
        if len(a)==1:
            s=a[0]
            add((1,1),(s,)); add((2,),(s,))
            add((s+1,1)); add((1,s+1)); add((s+2,),multiplicity=3)
        else:
            r,s=a
            add((1,1),(r,s)); add((2,),(r,s))
            add((r+1,1),(s,)); add((1,s+1),(r,))
            add((r+1,s+1)); add((r+2,),(s,)); add((s+2,),(r,)); add((r+s+2,))
    return result


def close_states(states):
    result = Counter()
    for (active, closed), count in states.items():
        result[tuple(sorted(x-1 for x in active+closed if x>1))] += count
    return result


def projections(types):
    f, p = Counter(), Counter()
    for typ, count in types.items():
        g = sum(typ)
        f[g] += count
        p[g] += count*prod(x+1 for x in typ)
    return sp.Poly.from_dict({(g,):c for g,c in f.items()},t).as_expr(), sp.Poly.from_dict({(g,):c for g,c in p.items()},t).as_expr()


def glue(n, edges, boundary, m, output, reverse=False):
    a,b = boundary[::-1] if reverse else boundary
    mapping = {0:a,m-1:b}
    mapping.update({i:n+i-1 for i in range(1,m-1)})
    return n+m-2, edges+[(mapping[i],mapping[i+1]) for i in range(m-1)], tuple(mapping[i] for i in output)


def laplacian(n,edges):
    L=sp.zeros(n)
    for a,b in edges:
        L[a,a]+=1; L[b,b]+=1; L[a,b]-=1; L[b,a]-=1
    return L


def grade_two_check(n, edges, L):
    """Every coefficient of M_2 equals the corresponding 2x2 Laplacian minor."""
    pairs=list(combinations(range(n),2))
    coef=[[0]*len(pairs) for _ in pairs]
    for e,f in combinations(edges,2):
        u=[int(i==e[1])-int(i==e[0]) for i in range(n)]
        v=[int(i==f[1])-int(i==f[0]) for i in range(n)]
        terms=[(k,u[a]*v[b]-u[b]*v[a]) for k,(a,b) in enumerate(pairs)]
        terms=[(k,c) for k,c in terms if c]
        for i,a in terms:
            for j,b in terms:
                coef[i][j]+=a*b
    for i,(a,b) in enumerate(pairs):
        for j,(c,d) in enumerate(pairs):
            assert coef[i][j] == L[a,c]*L[b,d]-L[a,d]*L[b,c]
    return len(pairs)**2


def matrix(m):
    A=(1+t)**(m-2); b=t**(m-2)
    return sp.Matrix([[t*A+(1-t)*b,t*A],[A-b,A]])


def rooted_moments(states):
    """C0,C1,D00,D10,D01,D11, with closed components weighted by size."""
    moments=[0]*6
    for (active,closed),count in states.items():
        w=count*prod(closed)*t**sum(s-1 for s in active+closed)
        if len(active)==1:
            moments[0]+=w; moments[1]+=active[0]*w
        else:
            r,s=active
            moments[2]+=w; moments[3]+=r*w; moments[4]+=s*w; moments[5]+=r*s*w
    c0,c1,d0,dr,ds,drs=moments
    return list(map(sp.expand,[c1+drs,c0+ds,c0+dr,c0,d0]))


def rooted_det(matrix):
    return sp.Add(*(int(c)*(-t)**i for i,c in enumerate(matrix.charpoly().all_coeffs())))


def main():
    report={'checks':{}, 'families':{}, 'toponomes':{}, 'graphs':[]}
    compounds=0; forests=0; subsets=0; comparisons=0
    saved={}
    for m,output,name in [(4,(1,2),'square'),(6,(2,3),'hex_straight'),(6,(1,2),'hex_turn')]:
        states=Counter({((2,),()):1,((1,1),()):1})
        n,edges,boundary=2,[(0,1)],(0,1)
        Fseq=[]; values=[]
        M=matrix(m)
        scalar=sp.Matrix([t,1])
        for N in range(4):
            typ=close_states(states)
            f,p=projections(typ)
            direct, dstates=forest_data(n,edges,boundary)
            assert typ==direct and states==dstates
            assert sp.expand(f-sum(scalar))==0
            L=laplacian(n,edges)
            chi=L.charpoly().as_expr(); x=next(iter(chi.free_symbols))
            assert sp.expand(p-t**n*chi.subs(x,-1/t)*(-1)**n)==0
            A,B,C,D,E=rooted_moments(states)
            a,b=boundary
            keep=lambda removed:[i for i in range(n) if i not in removed]
            for predicted,removed in [(A,()),(B,(a,)),(C,(b,)),(E,(a,b))]:
                assert sp.expand(predicted-rooted_det(L.extract(keep(removed),keep(removed))))==0
            assert sp.expand(B*C-A*E-D*D)==0
            numerical=sp.eye(n)+L
            cofactor=(-1)**(a+b)*numerical.extract(keep((b,)),keep((a,))).det()
            assert D.subs(t,1)==cofactor
            compounds+=grade_two_check(n,edges,L)
            comparisons+=1; subsets+=1<<len(edges); forests+=sum(typ.values())
            report['graphs'].append({'family':name,'N':N,'n':n,'edges':edges,'boundary':boundary,'rooted_passport':[str(q) for q in (A,B,C,D,E)],'toponome':[{'type':k,'count':v} for k,v in sorted(typ.items())]})
            Fseq.append(f); values.append({'N':N,'n':n,'edges':len(edges),'types':len(typ),'forests':sum(typ.values()),'tau':int(sp.expand(f).coeff(t,n-1)),'P1':int(p.subs(t,1))})
            if N>=2:
                assert sp.expand(Fseq[N]-sp.trace(M)*Fseq[N-1]+M.det()*Fseq[N-2])==0
            if name=='square':
                assert step(states,4,(1,2))==square_explicit_step(states)
            if N==2 and name=='square': report['toponomes']['two_squares']=[{'type':k,'count':v} for k,v in sorted(typ.items())]
            if N==3 and name.startswith('hex'): saved[name]=(typ,p)
            if N<3:
                states=step(states,m,output)
                n,edges,boundary=glue(n,edges,boundary,m,output)
                scalar=(M*scalar).applyfunc(sp.expand)
        report['families'][name]={'values':values,'F':[str(x) for x in Fseq], 'trace':str(sp.expand(sp.trace(M))), 'det':str(sp.factor(M.det()))}
    ta,pa=saved['hex_straight'];tb,pb=saved['hex_turn']
    diff={typ:ta[typ]-tb[typ] for typ in ta.keys()|tb.keys() if ta[typ]!=tb[typ]}
    first=min(sum(k) for k in diff)
    report['toponomes']['hex_first_difference']={'grade':first,'terms':[{'type':typ,'coefficient':c} for typ,c in sorted(diff.items()) if sum(typ)==first]}
    assert first==3
    assert {typ:c for typ,c in diff.items() if sum(typ)==3} == {(1,1,1):-1,(1,2):2,(3,):-1}
    report['toponomes']['hex_grade_three_counts']=[{'type':typ,'A':ta[typ],'B':tb[typ]} for typ in [(3,),(1,2),(1,1,1)]]
    report['toponomes']['hex_grade_four_difference']=[{'type':typ,'coefficient':c} for typ,c in sorted(diff.items()) if sum(typ)==4]
    assert sp.factor(pa-pb)==t**4*(5*t**2+5*t+1)**4
    report['toponomes']['rooted_difference']=str(sp.factor(pa-pb))
    # The exact original labelled pair from the public three-hexagon example.
    def cycle(vertices):
        return {tuple(sorted((vertices[i],vertices[(i+1)%len(vertices)]))) for i in range(len(vertices))}
    common=cycle([0,1,9,8,7,6])|cycle([0,1,2,3,4,5])
    original=[]
    for name,last,expected in [('A',[3,4,13,12,11,10],ta),('B',[2,3,13,12,11,10],tb)]:
        edges=sorted(common|cycle(last))
        typ,_=forest_data(14,edges,(11,12))
        assert typ==expected
        original.append({'name':name,'n':14,'edges':edges})
    report['original_isomers']=original
    general_cases=0
    for m in range(3,9):
        for output_edge in range(m-1):
            for col,active in enumerate([(2,),(1,1)]):
                oldgrade=sum(s-1 for s in active)
                updated=step(Counter({(active,()):1}),m,(output_edge,output_edge+1))
                entries=[0,0]
                for (a,c),count in updated.items():
                    increase=sum(s-1 for s in a+c)-oldgrade
                    entries[0 if len(a)==1 else 1]+=count*t**increase
                assert all(sp.expand(entries[row]-matrix(m)[row,col])==0 for row in range(2))
                general_cases+=1
    # All choices of output and both input correspondences, three hexagon steps.
    for steps in product(product([(1,2),(2,3),(3,4)], [False,True]), repeat=3):
        state=Counter({((2,),()):1,((1,1),()):1})
        for output,reverse in steps: state=step(state,6,output,reverse)
        f,p=projections(close_states(state))
        assert f==Fseq[3]
        assert sp.expand(f).coeff(t,13)==204
    # Relabelled square factor operator builds the exact expected edges.
    Es={(0,1)}
    for N in range(1,6):
        Es={tuple(v+2 for v in e) for e in Es}|{(0,1),(0,2),(1,3)}
        expected={(2*j,2*j+1) for j in range(N+1)}|{(2*j,2*j+2) for j in range(N)}|{(2*j+1,2*j+3) for j in range(N)}
        assert Es==expected
    report['checks']={'direct_graph_comparisons':comparisons,'edge_subsets':subsets,'forests_enumerated':forests,'compound_grade_two_coefficients':compounds,'hex_step_choices':216,'general_path_columns':general_cases,'shift_factor_steps':5,'original_isomer_subsets':2*2**16,'explicit_square_rule':'matches generic transfer for 4 stages','rooted_five_coordinates':'4 polynomial determinants, Jacobi identity, and signed off-diagonal cofactor at t=1 for each of 12 graphs'}
    path=Path(__file__).with_name('weaving-exponential-results.json')
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report['checks'],ensure_ascii=False,indent=2))


if __name__=='__main__': main()
