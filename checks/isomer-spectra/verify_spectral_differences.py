"""Exact local and mixed spectral differences in the published SLR convention."""
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp
from verify_slr_code import transfers, graph, state, LETTERS
from verify_boundary_transfer import xi, J, laplacian

OUT = Path(__file__).resolve().parent


def expand(value):
    return value.applyfunc(sp.expand) if isinstance(value, sp.MatrixBase) else sp.expand(value)


def words(length, alphabet=LETTERS):
    return [''.join(w) for w in product(alphabet, repeat=length)]


def run():
    T, U, initial = transfers()
    row = U['S'][0, :]
    q = xi*(xi**2-5*xi+5)**2
    f = xi*(4-xi)
    delta = U['S']-U['L']
    P = sp.Matrix([[0, 0], [xi-2, 1-xi], [0, 1], [-1, 1], [1, -1]])
    Q = sp.Matrix([[1, -xi, 0, 0, xi], [0, -1, 1, 0, 0]])
    K = Q*P
    H = delta*J
    K0 = Q*J*P
    assert expand(delta-P*Q) == sp.zeros(5)
    assert P.extract([2, 3], [0, 1]).det() == 1
    assert Q.extract([0, 1], [0, 2]).det() == 1
    assert expand(K.trace()-f) == 0 and expand(K.det()-f) == 0
    assert expand(K*K-f*K+f*sp.eye(2)) == sp.zeros(2)
    assert expand(delta**3-f*delta**2+f*delta) == sp.zeros(5)
    assert expand(K0*K0-f*sp.eye(2)) == sp.zeros(2)
    assert expand(H**3-f*H) == sp.zeros(5)
    assert expand(delta**3-f*delta) != sp.zeros(5)
    assert expand(row*P-sp.Matrix([[-q, q]])) == sp.zeros(1, 2)
    assert expand(Q*initial-sp.Matrix([-q, 0])) == sp.zeros(2, 1)
    assert expand(U['S']-U['R']-J*delta*J) == sp.zeros(5)

    def transfer(word):
        result = sp.eye(5)
        for letter in word:
            result = expand(U[letter]*result)
        return result

    polynomials = {}
    counts = {'direct_characteristic_polynomials': 0, 'local_replacements': 0,
              'separated_mixed_differences': 0, 'moment_checks': 0}
    for m in range(5):
        for u in words(m):
            g, _, _, edges = graph(u)
            L = laplacian(edges, len(g))
            direct = L.charpoly(xi).as_expr()
            assert expand(direct-state(u, U, initial)[0]) == 0
            polynomials[u] = direct
            counts['direct_characteristic_polynomials'] += 1
        print(f'PASS: direct polynomials for N={m+2}', flush=True)

    # Independently assembled integer Laplacians, including N=7.
    for m in range(6):
        for u in words(m):
            g, _, _, edges = graph(u)
            N, n = m+2, len(g)
            L = laplacian(edges, n)
            L2 = L*L
            moments = [sp.trace(L), sp.trace(L2), sp.trace(L2*L), sp.trace(L2*L2)]
            bends = len(u)-u.count('S')
            assert moments == [10*N+2, 36*N, 148*N-28, 648*N-228+4*bends]
            assert sum(g.degree(a)==3 and g.degree(b)==3 for a,b in g.edges) == N-1+bends
            if u in polynomials:
                # Newton's identities, applied to independently computed traces.
                e = [sp.Integer(1)]
                for k in range(1, 5):
                    e.append(sp.cancel(sum((-1)**(j-1)*e[k-j]*moments[j-1]
                                         for j in range(1, k+1))/k))
                cp = sp.Poly(polynomials[u], xi)
                assert all(cp.nth(n-k)==(-1)**k*e[k] for k in range(1, 5))
                tau0, tau1 = 1, 6
                for _ in range(2, N+1):
                    tau0, tau1 = tau1, 6*tau1-tau0
                assert cp.nth(0)==0 and cp.nth(1)==-n*tau1
            counts['moment_checks'] += 1
    print('PASS: moments, degree-three edges, and rooted coefficients', flush=True)

    cache = {u: transfer(u) for m in range(4) for u in words(m)}
    cache[''] = sp.eye(5)
    for m in range(1, 5):
        for i in range(m):
            for fixed in words(m-1):
                prefix, suffix = fixed[:i], fixed[i:]
                for a,b in combinations(LETTERS, 2):
                    direct = polynomials[prefix+a+suffix]-polynomials[prefix+b+suffix]
                    predicted = (row*cache[suffix]*(U[a]-U[b])*cache[prefix]*initial)[0]
                    assert expand(direct-predicted) == 0
                    if (a,b)==('S','L'):
                        assert expand(direct-(row*cache[suffix]*P*Q*cache[prefix]*initial)[0]) == 0
                    counts['local_replacements'] += 1
        # All pairs of variable S/L positions; the intervening word is retained.
        for i,j in combinations(range(m), 2):
            for fixed in words(m-2):
                total = 0
                for a,b in product('SL', repeat=2):
                    chars = iter(fixed); u = ''.join(a if k==i else b if k==j else next(chars) for k in range(m))
                    total += (-1)**((a=='L')+(b=='L'))*polynomials[u]
                matrices = iter(U[c] for c in fixed)
                result = initial
                for k in range(m):
                    result = expand((delta if k in (i,j) else next(matrices))*result)
                assert expand(total-(row*result)[0]) == 0
                counts['separated_mixed_differences'] += 1
    print('PASS: local replacements and separated mixed differences', flush=True)

    sequences = {'ordinary': [], 'reoriented': []}
    for label, operator in [('ordinary', delta), ('reoriented', H)]:
        vector = initial
        for r in range(1, 9):
            vector = expand(operator*vector)
            value = expand((row*vector)[0])
            sequences[label].append(value)
            if r<=4:
                total=0
                for choices in product([0,1], repeat=r):
                    u=''.join('S' if choice==0 else
                              ('L' if label=='ordinary' or (r-j)%2==0 else 'R')
                              for j,choice in enumerate(choices,1))
                    total += (-1)**sum(choices)*polynomials[u]
                assert expand(total-value)==0
        a=sequences[label]
        assert expand(a[0]-q*q)==0
        assert expand(a[1]-(f-2 if label=='ordinary' else 2)*q*q)==0
        for i in range(6):
            expected=f*(a[i+1]-a[i]) if label=='ordinary' else f*a[i]
            assert expand(a[i+2]-expected)==0

    pairs = [('S','L'), ('SS','SL'), ('LS','LL'), ('LL','LR'), ('SSS','SLS')]
    examples={}
    for a,b in pairs:
        difference=sp.factor(polynomials[a]-polynomials[b])
        examples['S'+a+' - S'+b]={'difference':str(difference),
            'at_minus_one':int(difference.subs(xi,-1)),
            'degree':sp.degree(difference,xi).__int__(),
            'coefficients_descending':list(map(int,sp.Poly(difference,xi).all_coeffs()))}
    assert expand(polynomials['S']-polynomials['L']-q*q)==0
    assert expand(polynomials['LL']-polynomials['LR']+(xi-2)**2*q*q)==0
    a=xi**2-4*xi+2
    h=xi**6-16*xi**5+101*xi**4-320*xi**3+534*xi**2-444*xi+143
    assert expand(polynomials['SS']-polynomials['SL']-xi**2*(xi**2-5*xi+5)**2*a*h)==0
    assert expand(polynomials['SSS']-polynomials['SLS']-xi**2*a*a*h*h)==0
    assert sp.rem(polynomials['SSS']-polynomials['SLS'],q*q,xi)!=0
    assert sp.rem(polynomials['SS']-polynomials['SL'],q*q,xi)!=0
    assert expand(polynomials['SS']-polynomials['SL']-polynomials['LS']+polynomials['LL']-(f-2)*q*q)==0
    assert expand(polynomials['SS']-polynomials['SL']-polynomials['LS']+polynomials['LR']-2*q*q)==0
    # A telescoping comparison in which every letter changes.
    a,b='SLR','RLS'
    telescoped=sum((row*transfer(a[i+1:])*(U[a[i]]-U[b[i]])*transfer(b[:i])*initial)[0] for i in range(3))
    assert expand(telescoped-polynomials[a]+polynomials[b])==0
    values={'S'+u:int(polynomials[u].subs(xi,-1)) for u in ['S','L','SS','SL','LS','LL','LR','SSS','SLS']}
    result={'convention':'U_L=T_2 J, U_S=T_3 J, U_R=T_4 J; input order reversed',
        'counts':counts, 'P':[[str(v) for v in row] for row in P.tolist()],
        'Q':[[str(v) for v in row] for row in Q.tolist()],
        'K':[[str(sp.factor(v)) for v in row] for row in K.tolist()],
        'K_reoriented':[[str(sp.factor(v)) for v in row] for row in K0.tolist()],
        'examples':examples, 'P_at_one':values,
        'sequences_divided_by_q_squared':{label:[str(sp.factor(v/q**2)) for v in a] for label,a in sequences.items()}}
    result['example_graphs']={'S'+u:{'vertices':len(graph(u)[0]), 'edges':sorted(graph(u)[3])}
                              for u in ['S','L','SS','SL','LS','LL','LR','SSS','SLS']}
    (OUT/'spectral-differences-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS:',counts,flush=True)


if __name__=='__main__':
    run()
