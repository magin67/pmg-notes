"""Exact algebra behind the moment formulas; not a finite substitute for proof."""
import sympy as sp


def verify_proofs():
    N, b, h = sp.symbols('N b h', integer=True)
    n2, n3 = 2*N+4, 2*N-2
    edges = {(2, 2): 6+b, (2, 3): 4*N-4-2*b, (3, 3): N-1+b}
    degrees = lambda j: n2*2**j+n3*3**j
    edge_sum = lambda f: sum(count*f(x, y) for (x, y), count in edges.items())
    Sv2 = 170*N-78+8*b+2*h
    k_sum = 6*(N-1)
    dk_sum = 14*(N-1)+2*b
    k_pairs = 2*(N-2-b)+2*b+h
    assert sp.expand(4*degrees(2)+4*dk_sum+k_sum+2*k_pairs) == Sv2

    first = [degrees(1), degrees(2)+degrees(1), degrees(3)+3*degrees(2),
             degrees(4)+4*degrees(3)+4*edge_sum(lambda x,y:x*y)+2*degrees(2)-degrees(1),
             degrees(5)+5*degrees(4)+5*edge_sum(lambda x,y:x*y*(x+y))
             +5*(degrees(3)-degrees(2)+2*edge_sum(lambda x,y:x*y))]
    expected = [10*N+2, 36*N, 148*N-28, 648*N-228+4*b, 2940*N-1428+60*b]
    assert list(map(sp.expand,first)) == expected

    terms = [degrees(6),
        3*edge_sum(lambda x,y:sum(x**i*y**(4-i)+y**i*x**(4-i) for i in range(5))),
        6*(degrees(4)-degrees(3)+edge_sum(lambda x,y:x*x*y+y*y*x)),
        12*edge_sum(lambda x,y:x*y*(x+y-1)),
        3*(degrees(4)-degrees(3)+Sv2),
        2*(5*N+1)+12*(n2+3*n3)+6*edge_sum(lambda x,y:(x-1)*(y-1))+12*n3+12*N]
    terms = list(map(sp.expand,terms))
    sixth = 13656*N-8112+576*b+6*h
    assert sp.expand(sum(terms)) == sixth
    moments = [None]+expected+[sixth]
    p = [sp.Integer(1)]
    for k in range(1,7):
        p.append(sp.expand(sum((-1)**(j-1)*p[k-j]*moments[j] for j in range(1,k+1))/k))
    assert sp.diff(p[4],b) == -1
    assert sp.diff(p[6],h) == -1
    # Illustrate the counting proof by a sufficient bound, not a sharp threshold.
    N0, k = 152, 10
    n, m = 4*N0+2, N0-2
    classes = (3**m+1+3**((m+1)//2)+3**(m//2))//4
    capacity = sp.prod(n*6**j+1 for j in range(1,k+1))
    assert classes > capacity
    return {'moments':list(map(str,moments[1:])), 'sixth_trace_terms':list(map(str,terms)),
            'p4_b_derivative':-1,'p6_h_derivative':-1,
            'pigeonhole_example':{'N':N0,'k':k,'graph_classes':classes,'capacity_bound':int(capacity)}}


if __name__ == '__main__':
    print(verify_proofs())
