"""Exact checks for periodic internal words and periodic P6 runners."""
from pathlib import Path
import json
import sys
import sympy as sp
import networkx as nx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'checks/isomer-spectra'))
import verify_slr_code as slr
from verify_boundary_transfer import xi, J, laplacian

T,U,s1=slr.transfers()
s0=sp.Matrix([xi*(xi-2),xi-1,xi-1,-1,1])
row=U['S'][0,:]
q=sp.Symbol('q');z=sp.Symbol('z');m=sp.Symbol('m',integer=True,nonnegative=True)
expand=lambda a:a.applyfunc(sp.expand)
H=sp.zeros(5);H[0,4]=H[4,0]=1;H[1,2]=H[2,1]=-1;H[3,3]=2


def block(word):
    M=sp.eye(5)
    for c in word:M=expand(U[c]*M)
    return M


def polynomial_action(coeff,M,v):
    y=sp.zeros(5,1)
    for c in coeff:y=expand(M*y+c*v)
    return y


def rooted_sequence(M,v,r,length=12):
    M=M.subs(xi,-1);v=v.subs(xi,-1);r=r.subs(xi,-1)
    result=[]
    for _ in range(length):result.append(int((r*v)[0]));v=M*v
    return result


def runner_graph(letters):
    graph=nx.Graph([(0,1)]);boundary=(0,1)
    for c in letters:
        a,b=boundary;n=len(graph)
        core=[b,a]+list(range(n,n+4))
        path=[core[i] for i in [1,2,3,4,5,0]]
        graph.add_edges_from(zip(path,path[1:]))
        j=slr.EXIT[c];boundary=core[j],core[j+1]
    return graph


def direct_polynomial(graph):
    edges={tuple(sorted(e)):1 for e in graph.edges}
    return laplacian(edges,len(graph)).charpoly(xi).as_expr()


def degree_statistics(u):
    return sum(c!='S' for c in u),sum(a==b and a!='S' for a,b in zip(u,u[1:]))


def displayed_coefficients(word):
    # Independently transcribed from the note, in x=xi-2.
    x=sp.Symbol('x')
    alpha=x**4-2*x**3-4*x**2+4*x+4
    beta=3*x**4-4*x**3-8*x**2+8*x+6
    if word=='LR':
        vals=(alpha**2-2*beta,beta**2-2*alpha**2+2,
              2*(x+2)**2*x**4*(x*x-x-1)**2)
    elif word=='SL':
        vals=(x**8-4*x**7-4*x**6+24*x**5+3*x**4-40*x**3-3*x**2+16*x,
              x**10-4*x**9-2*x**8+24*x**7-72*x**5+2*x**4+96*x**3+10*x**2-32*x-2,
              2*(x+2)**2*(x*x-2)*(2*x**3-3*x*x-2*x+2))
    else:
        vals=(x**12-6*x**11+52*x**9-44*x**8-164*x**7+155*x**6+240*x**5-172*x**4-162*x**3+48*x*x+36*x+4,
              x**16-6*x**15+x**14+56*x**13-64*x**12-236*x**11+358*x**10+556*x**9-891*x**8-818*x**7+1107*x**6+764*x**5-628*x**4-372*x**3+132*x*x+72*x+6,
              -2*(x+2)**2*x*x*(x*x-x-1)**2*(x**3-2*x*x-x+3)*(2*x**3-3*x*x-4*x+3))
    return [sp.expand(t.subs(x,xi-2)) for t in vals]


def run():
    for c in 'SLR':
        assert expand(U[c].T*H*U[c]-H)==sp.zeros(5)
        assert sp.expand(U[c].det())==1
    result={'common_quadratic_form':'A*E-B*C+D**2','gram_determinant':int(H.det()),'periods':{},'phases':{}}
    matrices={};coefficients={}
    for word in ['LR','SL','LLS']:
        M=block(word);matrices[word]=M
        a=sp.expand(sp.trace(M)-1)
        b=sp.expand((a*a+1-sp.trace(M*M))/2)
        quartic=q**4-a*q**3+b*q*q-a*q+1
        assert sp.expand(M.charpoly(q).as_expr()-(q-1)*quartic)==0
        coeff=sp.Poly(quartic,q).all_coeffs();coefficients[word]=coeff
        rem=polynomial_action(coeff,M,s1)
        assert expand((M-sp.eye(5))*rem)==sp.zeros(5,1)
        K=sp.factor((row*rem)[0])
        assert all(sp.expand(actual-written)==0 for actual,written in zip((a,b,K),displayed_coefficients(word)))
        runner_K=sp.factor((sp.eye(5)[0,:]*polynomial_action(coeff,M,s0))[0])
        if word=='LLS':assert runner_K.subs(xi,-1)==-901692
        seq=rooted_sequence(M,s1,row)
        aa,bb,kk=[int(x.subs(xi,-1)) for x in [a,b,K]]
        assert all(seq[k+4]-aa*seq[k+3]+bb*seq[k+2]-aa*seq[k+1]+seq[k]==kk for k in range(8))
        hankel=sp.Matrix(5,5,lambda i,j:seq[i+j]);det=int(hankel.det());assert det!=0
        # Four-step scalar relation plus a constant produces this rational GF.
        numerator=(1-z)*(seq[0]+(seq[1]-aa*seq[0])*z+(seq[2]-aa*seq[1]+bb*seq[0])*z**2
                         +(seq[3]-aa*seq[2]+bb*seq[1]-aa*seq[0])*z**3)+kk*z**4
        denominator=(1-z)*(1-aa*z+bb*z*z-aa*z**3+z**4)
        series=sp.Poly(sum(seq[i]*z**i for i in range(len(seq)))*denominator-numerator,z)
        assert all(series.nth(i)==0 for i in range(len(seq)))
        assert sp.gcd(sp.Poly(numerator,z),sp.Poly(denominator,z)).degree()==0
        # Four distinct positive reciprocal multipliers and the constant mode.
        assert aa>4 and aa*aa-4*(bb-2)>0 and bb-2*aa+2>0
        zz=(aa+sp.sqrt(aa*aa-4*(bb-2)))/2
        dominant=(zz+sp.sqrt(zz*zz-4))/2
        result['periods'][word]={'a':str(sp.factor(a)),'b':str(sp.factor(b)),'K':str(K),'runner_K':str(runner_K),
            'quartic':str(quartic),'at_minus_one':{'a':aa,'b':bb,'K':kk,'sequence':seq,
            'hankel5':det,'hankel5_mod101':det%101,'GF_numerator':str(sp.expand(numerator)),
            'GF_denominator':str(sp.expand(denominator)),
            'dominant_multiplier':str(sp.N(dominant,30)),
            'growth_per_core':str(sp.N(dominant**sp.Rational(1,len(word)),30))}}
        print('PASS symbolic recurrence and minimality',word,flush=True)

    capped_checks=0;runner_checks=0
    for word in ['LR','RL','SL','LS','LLS','LSL','SLL']:
        family='LR' if word in ['LR','RL'] else 'SL' if len(word)==2 else 'LLS'
        M=block(word);coeff=coefficients[family]
        rotated=word[1:]+word[0]
        assert expand(block(rotated)*U[word[0]]-U[word[0]]*M)==sp.zeros(5)
        assert sp.expand(M.charpoly(q).as_expr()-(q-1)*sp.Poly.from_list(coeff,q).as_expr())==0
        seq=rooted_sequence(M,s1,row)
        phase_K=sp.factor((row*polynomial_action(coeff,M,s1))[0])
        if word=='LSL':assert phase_K.subs(xi,-1)==-85698
        det=int(sp.Matrix(5,5,lambda i,j:seq[i+j]).det());assert det!=0
        # A scalar annihilator at xi=2, certified on the full 5-dimensional Krylov space.
        M2=M.subs(xi,2);v2=s1.subs(xi,2);r2=row.subs(xi,2)
        v=(M2-sp.eye(5))**3*v2
        for k in range(5):assert (r2*M2**k*v)[0]==0
        f2=(-4*(m+1)*(m+2) if len(word)==2 else
            -4*(2*m+1)*(m+2) if word=='LSL' else -8*(m+1)**2)
        for k in range(3):assert (r2*M2**k*v2)[0]==f2.subs(m,k)
        assert sp.expand(f2.subs(m,m+2)-2*f2.subs(m,m+1)+f2)!=0
        phase={'P1_sequence':seq,'K':str(phase_K),'hankel5':det,'hankel5_mod101':det%101,
               'chi_at2':str(sp.factor(f2)),'capped_polynomials':[],'runner_polynomials':[]}
        state=s1
        edge_state=s0
        for k in range(5):
            g,_,_,_=slr.graph(word*k)
            direct=direct_polynomial(g)
            expected=sp.expand((row*state)[0]);assert sp.expand(direct-expected)==0
            assert direct.subs(xi,-1)==seq[k]
            assert direct.subs(xi,2)==f2.subs(m,k)
            phase['capped_polynomials'].append(str(direct));capped_checks+=1
            state=expand(M*state)
            if k<=3:
                g=runner_graph(word*k);dp=direct_polynomial(g)
                assert sp.expand(dp-edge_state[0])==0
                if k:
                    other,_,_,_=slr.graph((word*k)[1:-1])
                    assert nx.is_isomorphic(g,other)
                phase['runner_polynomials'].append(str(dp));runner_checks+=1
                edge_state=expand(M*edge_state)
        result['phases'][word]=phase
        print('PASS independent Laplacians, phase and xi=2',word,flush=True)

    for k in range(1,5):
        for a,b in [('LR','RL'),('SL','LS'),('LLS','SLL')]:
            assert slr.canonical(a*k)==slr.canonical(b*k)
        assert degree_statistics('LLS'*k)==(2*k,k)
        assert degree_statistics('LSL'*k)==(2*k,k-1)
        diff=sp.Poly(sp.sympify(result['phases']['LLS']['capped_polynomials'][k],locals={'xi':xi})
                     -sp.sympify(result['phases']['LSL']['capped_polynomials'][k],locals={'xi':xi}),xi)
        assert diff.degree()==4*(3*k+2)+2-6 and diff.LC()==-1
        assert diff.eval(2)==4*k
        assert not nx.is_isomorphic(slr.graph('LLS'*k)[0],slr.graph('LSL'*k)[0])
    result['direct_capped_polynomial_checks']=capped_checks
    result['direct_runner_polynomial_checks']=runner_checks
    (HERE/'periodic-slr-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS all checks',capped_checks,runner_checks,flush=True)


if __name__=='__main__':run()
