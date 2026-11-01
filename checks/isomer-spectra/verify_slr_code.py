"""Exact SLR coding, graph isomorphism, and spectral symmetry checks."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
import networkx as nx
import sympy as sp
from verify_boundary_transfer import xi, J, laplacian, passport

OUT = Path(__file__).resolve().parent
LETTERS = 'SLR'
EXIT = {'L':2, 'S':3, 'R':4}
BAR = str.maketrans('SLR', 'SRL')


def mirror(u):
    return u.translate(BAR)


def reverse_chain(u):
    return mirror(u[::-1])


def orbit(u):
    return {u, mirror(u), u[::-1], reverse_chain(u)}


def canonical(u):
    order = {c:i for i,c in enumerate(LETTERS)}
    return min(orbit(u), key=lambda v:tuple(order[c] for c in v))


def graph(u, reverse_input=True):
    """u has N-2 turns; the final S selects a free terminal boundary only."""
    cores = [list(range(6))]
    active = (0,1)
    n = 6
    for letter in u+'S':
        a,b = active
        core = [b,a] if reverse_input else [a,b]
        core += list(range(n,n+4))
        n += 4
        cores.append(core)
        j = EXIT[letter]
        active = (core[j],core[j+1])
    edges = {tuple(sorted((a,b))):1 for core in cores
        for a,b in zip(core,core[1:]+core[:1])}
    g = nx.Graph()
    g.add_nodes_from(range(n)); g.add_edges_from(edges)
    return g, cores, active, edges


def six_cycles(g):
    """Bounded DFS on adjacency only; no access to the construction's cores."""
    found=set()
    for start in g:
        def walk(path):
            if len(path)==6:
                if g.has_edge(path[-1],start):
                    found.add(frozenset(tuple(sorted(e)) for e in zip(path,path[1:]+path[:1])))
                return
            for v in g[path[-1]]:
                if v>start and v not in path:
                    walk(path+[v])
        walk([start])
    return found


def transfers():
    data=json.loads((OUT/'boundary-transfer-results.json').read_text(encoding='utf-8'))
    T={int(j):sp.Matrix([[sp.sympify(x,locals={'xi':xi}) for x in row] for row in rows])
        for j,rows in data['T'].items()}
    initial=sp.Matrix([sp.sympify(x,locals={'xi':xi}) for x in data['initial']])
    return T,{c:T[j]*J for c,j in EXIT.items()},initial


def state(u, U, initial):
    s=initial
    for c in u+'S':
        s=(U[c]*s).applyfunc(sp.expand)
    return s


def verified_mapping(g,h):
    matcher=nx.algorithms.isomorphism.GraphMatcher(g,h)
    assert matcher.is_isomorphic()
    mapping=matcher.mapping
    assert set(mapping)==set(g) and set(mapping.values())==set(h)
    assert {frozenset((mapping[a],mapping[b])) for a,b in g.edges} == {frozenset(e) for e in h.edges}
    return mapping


def run():
    T,U,initial=transfers()
    assert J*initial==initial
    assert all(U[mirror(c)]==J*U[c]*J for c in LETTERS)
    row=T[3][0,:]
    assert row*J==row and all(U[c][0,:]==row for c in LETTERS)
    counts=[]; polynomial_checks=0; passport_checks=0; cycle_checks=0; symmetry_checks=0
    examples={}; all_values={}
    for m in range(6):
        words=[''.join(t) for t in product(LETTERS,repeat=m)]
        classes=[]; buckets=defaultdict(list); spectral={}
        for u in words:
            g,cores,boundary,edges=graph(u)
            N=m+2; n=4*N+2
            assert len(g)==n and g.number_of_edges()==5*N+1
            assert all(set(cores[i]).isdisjoint(cores[j]) for i in range(N) for j in range(i+2,N))
            expected={frozenset(tuple(sorted(e)) for e in zip(c,c[1:]+c[:1])) for c in cores}
            assert six_cycles(g)==expected
            cycle_checks+=1
            # Classify graphs independently; the code orbit is checked only afterwards.
            key=nx.weisfeiler_lehman_graph_hash(g)
            index=None
            for candidate in buckets[key]:
                if nx.is_isomorphic(g,classes[candidate]['graph']):
                    index=candidate;break
            if index is None:
                index=len(classes);buckets[key].append(index)
                classes.append({'graph':g,'words':[]})
            classes[index]['words'].append(u)
            for transform in [mirror,reverse_chain]:
                h,_,_,_=graph(transform(u))
                verified_mapping(g,h)
                symmetry_checks+=1
            if m<=4:
                s=state(u,U,initial)
                direct=laplacian(edges,n).charpoly(xi).as_expr()
                assert sp.expand(s[0]-direct)==0
                spectral[u]=sp.Poly(direct,xi)
                polynomial_checks+=1
                assert state(mirror(u),U,initial)==J*s
                assert sp.expand(state(reverse_chain(u),U,initial)[0]-s[0])==0
                if m<=2:
                    assert passport(xi*sp.eye(n)-laplacian(edges,n),boundary)==s
                    passport_checks+=1
            z=sp.diag(1,-1,-1,-1,1)*state(u,{c:M.subs(xi,-1) for c,M in U.items()},initial.subs(xi,-1))
            all_values['S'+u]=int(z[0])
            if u in ['','S','L','LL','LR','LS','SR']:
                examples['S'+u]={'rooted_state':list(z),'P1':int(z[0]),'boundary':boundary,
                    'edges':sorted(edges),'n':n}
        partition={frozenset(c['words']) for c in classes}
        expected={frozenset(orbit(u)) for u in words}
        assert partition==expected
        formula=(3**m+1+3**((m+1)//2)+3**(m//2))//4
        assert len(classes)==formula
        counts.append(dict(N=m+2,words=len(words),classes=len(classes)))
        print('PASS:',counts[-1],flush=True)
    for m in [6,7,8]:
        words=[''.join(t) for t in product(LETTERS,repeat=m)]
        assert len({canonical(u) for u in words})==(3**m+1+3**((m+1)//2)+3**(m//2))//4
    # Same-order gluing is a different coding convention: LL becomes LR up to reflection.
    wrong,_,_,wrong_edges=graph('LL',reverse_input=False)
    right,_,_,_=graph('LR')
    assert nx.is_isomorphic(wrong,right)
    assert not nx.is_isomorphic(wrong,graph('LL')[0])
    wrong_value=sp.det(sp.eye(len(wrong))+laplacian(wrong_edges,len(wrong)))
    assert wrong_value==examples['SLR']['P1']!=examples['SLL']['P1']
    assert examples['SLS']['rooted_state']!=examples['SSR']['rooted_state']
    assert sp.Matrix(examples['SLS']['rooted_state'])!=J*sp.Matrix(examples['SSR']['rooted_state'])
    # Explicit maps for the four words in a representative orbit.
    u='LS';g,_,_,edges=graph(u)
    maps={('S'+v):verified_mapping(g,graph(v)[0]) for v in sorted(orbit(u))}
    reversed_end=graph('SR')[2]
    inverse={v:k for k,v in maps['SSR'].items()}
    left=tuple(inverse[v] for v in reversed_end)
    assert left==(3,4)
    left_state=sp.diag(1,-1,-1,-1,1)*passport(-sp.eye(len(g))-laplacian(edges,len(g)),left)
    assert list(left_state)==examples['SSR']['rooted_state']
    # The regular development of SLLLL has a new contact, excluded from our abstract graph.
    root3=sp.sqrt(3); step=sp.Matrix([root3,0]); center=step
    turn=sp.Matrix([[sp.Rational(1,2),-root3/2],[root3/2,sp.Rational(1,2)]])
    for _ in range(4):
        step=(turn*step).applyfunc(sp.simplify);center=(center+step).applyfunc(sp.simplify)
    assert center==sp.Matrix([-root3/2,sp.Rational(3,2)]) and center.dot(center)==3
    out=dict(convention='w=S u; len(u)=N-2; input (0,1)=(b,a); L=2,S=3,R=4',
        counts=counts,checks=dict(six_cycle_recovery=cycle_checks,graph_symmetries=symmetry_checks,
        full_characteristic_polynomials=polynomial_checks,full_polynomial_passports=passport_checks),
        examples=examples,orbit_example=maps,same_order_error_value=int(wrong_value),
        left_end_in_SLS=left,left_end_state=list(left_state))
    (OUT/'slr-code-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=int)+'\n',encoding='utf-8')
    print('PASS:',out['checks'],flush=True)


if __name__=='__main__':
    run()
