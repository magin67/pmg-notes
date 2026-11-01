"""Exact checks for spectral transfer to a new two-vertex boundary."""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
xi, u, v, w = sp.symbols('xi u v w')
J = sp.eye(5)
J[1, 1] = J[2, 2] = 0
J[1, 2] = J[2, 1] = 1


def laplacian(edges, n):
    matrix = sp.zeros(n)
    for (a, b), weight in edges.items():
        matrix[a, a] += weight
        matrix[b, b] += weight
        matrix[a, b] -= weight
        matrix[b, a] -= weight
    return matrix


def passport(matrix, boundary):
    a, b = boundary
    ids = list(range(matrix.rows))
    keep = lambda removed: [i for i in ids if i not in removed]
    det = lambda rows, cols: sp.expand(matrix.extract(rows, cols).det(method='domain-ge'))
    return sp.Matrix([det(ids, ids), det(keep([a]), keep([a])),
        det(keep([b]), keep([b])),
        (-1)**(a+b)*det(keep([b]), keep([a])),
        det(keep([a, b]), keep([a, b]))])


def lap_passport(edges, n, boundary, parameter=xi):
    return passport(parameter*sp.eye(n)-laplacian(edges, n), boundary)


def coefficient_row(f):
    p = sp.Poly(f, u, v, w)
    alpha = p.coeff_monomial(u*w)
    beta, gamma = p.coeff_monomial(u), p.coeff_monomial(w)
    delta, epsilon = p.coeff_monomial(v), p.coeff_monomial(1)
    assert sp.expand(f-alpha*(u*w-v*v)-beta*u-gamma*w-delta*v-epsilon) == 0
    # Five determinant evaluations independently recover the same coefficients.
    q00, q10, q01, q11, qo = [f.subs({u:a, v:b, w:c}) for a,b,c in
        [(0,0,0), (1,0,0), (0,0,1), (1,0,1), (0,1,0)]]
    assert sp.expand(alpha-(q11-q10-q01+q00)) == 0
    assert sp.expand(beta-(q10-q00)) == 0
    assert sp.expand(gamma-(q01-q00)) == 0
    assert sp.expand(delta-(qo-q00+alpha)) == 0
    return [alpha, gamma, beta, -delta, epsilon]


def transfer(kernel, size, boundary, shared=0):
    # Input is always (0,1); shared is the conductance counted once in the union.
    matrix = xi*sp.eye(size)-laplacian(kernel, size)
    matrix[0,0] += -xi+shared
    matrix[1,1] += -xi+shared
    matrix[0,1] -= shared
    matrix[1,0] -= shared
    matrix[0,0] += u
    matrix[1,1] += w
    matrix[0,1] += v
    matrix[1,0] += v
    return sp.Matrix([coefficient_row(f) for f in passport(matrix, boundary)])


def glue(old, old_n, old_boundary, kernel, kernel_n, output, shared=0):
    mapping = {0:old_boundary[0], 1:old_boundary[1]}
    mapping.update({i:old_n+i-2 for i in range(2, kernel_n)})
    edges = old.copy()
    for (a,b), weight in kernel.items():
        key = tuple(sorted((mapping[a], mapping[b])))
        edges[key] = edges.get(key, 0)+weight
    seam = tuple(sorted(old_boundary))
    if shared:
        assert old.get(seam, 0) >= shared and kernel.get((0,1), 0) >= shared
        edges[seam] -= shared
    return edges, old_n+kernel_n-2, tuple(mapping[i] for i in output)


def check_case(old, old_n, kernel, kernel_n, output, shared=0):
    T = transfer(kernel, kernel_n, output, shared)
    state = lap_passport(old, old_n, (0,1))
    edges, n, boundary = glue(old, old_n, (0,1), kernel, kernel_n, output, shared)
    direct = lap_passport(edges, n, boundary)
    assert (T*state-direct).applyfunc(sp.expand) == sp.zeros(5,1)
    assert sp.expand(direct[0]*direct[4]-direct[1]*direct[2]+direct[3]**2) == 0
    return T, direct


def hexagon_transfers():
    kernel = {tuple(sorted((i,(i+1)%6))):sp.Integer(1) for i in range(6)}
    matrices = {j:transfer(kernel, 6, (j,j+1), 1) for j in [2,3,4]}
    state = lap_passport(kernel, 6, (0,1))
    y = xi-2
    m, ell, k = y*y-1, y**3-2*y, y**4-3*y*y+1
    A,B,C,D,E = sp.symbols('A B C D E')
    s = sp.Matrix([A,B,C,D,E])
    phi = y*m*A-(y+1)*m*(B+C)+(y+1)*(m+y)*E
    Aprime = k*A-(k+ell)*(B+C)+2*D+(k+2*ell+m)*E
    E2 = m*A-(m+y)*B-m*C+(m+y)*E
    E3 = y*y*A-y*(y+1)*(B+C)+(y+1)**2*E
    compact = {
        2:sp.Matrix([Aprime, ell*A-(ell+m)*B-ell*C+(ell+m)*E, phi-B, D-E2, E2]),
        3:sp.Matrix([Aprime, phi-B, phi-C, D-E3, E3])}
    for j in [2,3]:
        assert (matrices[j]*s-compact[j]).applyfunc(sp.expand) == sp.zeros(5,1)
    assert matrices[4] == J*matrices[2]*J
    assert matrices[3] == J*matrices[3]*J
    assert all(matrices[j][0,:] == matrices[3][0,:] for j in [2,4])
    initial = sp.Matrix([xi*(xi-4)*(xi-3)**2*(xi-1)**2,
        (xi-3)*(xi-2)*(xi-1)*(xi*xi-4*xi+1),
        (xi-3)*(xi-2)*(xi-1)*(xi*xi-4*xi+1),
        -(xi-3)*(xi-1)*(xi*xi-4*xi+2), (xi*xi-5*xi+5)*(xi*xi-3*xi+1)])
    assert (initial-state).applyfunc(sp.expand) == sp.zeros(5,1)
    c5 = xi*(xi*xi-5*xi+5)**2
    vector = sp.Matrix([0,y,0,-1,1])
    assert ((matrices[3]-matrices[2])*state+c5*vector).applyfunc(sp.expand) == sp.zeros(5,1)
    assert sp.expand((matrices[3][0,:]*vector)[0]+c5) == 0
    # The published, vertex-labelled pair is checked against its separate data file.
    pair = json.loads((OUT/'three-hexagons-results.json').read_text(encoding='utf-8'))
    for label,j in [('A',3),('B',2)]:
        chi = (matrices[3][0,:]*matrices[j]*state)[0]
        assert sp.expand(chi-sp.sympify(pair[label]['chi'],locals={'xi':xi})) == 0
    R = sp.diag(1,-1,-1,-1,1)
    numeric = {j:R*matrices[j].subs(xi,-1)*R for j in matrices}
    z0 = R*state.subs(xi,-1)
    assert z0 == sp.Matrix([320,144,144,56,55])
    assert numeric[2]*z0 == sp.Matrix([28435,12331,12694,4763,4707])
    assert numeric[3]*z0 == sp.Matrix([28435,12694,12694,4884,4828])
    return kernel, matrices, state, numeric, z0


def verify():
    counts = dict(overlapping_boundary=0, disjoint_boundary=0, weighted=0,
        permuted=0, polynomial_chains=0, numeric_chain_states=0)
    # All simple graphs on three vertices, including disconnected graphs.
    old_edges = list(combinations(range(3),2))
    olds = [{e:sp.Integer(1) for i,e in enumerate(old_edges) if mask>>i&1} for mask in range(8)]
    for old,kernel in product(olds, repeat=2):
        shared = int((0,1) in old and (0,1) in kernel)
        check_case(old,3,kernel,3,(1,2),shared)
        counts['overlapping_boundary'] += 1
    base = {(0,2):sp.Integer(1),(2,3):sp.Integer(1),(1,3):sp.Integer(1)}
    kernels=[]
    for bits in product([0,1],repeat=3):
        k=base.copy()
        k.update({edge:sp.Integer(1) for edge,bit in zip([(0,1),(0,3),(1,2)],bits) if bit})
        kernels.append(k)
    for old,kernel in product(olds,kernels):
        shared=int((0,1) in old and (0,1) in kernel)
        check_case(old,3,kernel,4,(2,3),shared)
        counts['disjoint_boundary'] += 1
    print('PASS: 128 general unweighted gluing cases.',flush=True)
    for i in range(4):
        old={(0,1):sp.Rational(3,2),(0,2):sp.Rational(i+1,3),(1,2):sp.Integer(2)}
        kernel={(0,1):sp.Rational(3,2),(0,2):sp.Rational(2,3),(2,3):sp.Integer(i+1),
                (1,3):sp.Rational(5,4),(0,3):sp.Rational(1,2)}
        for shared in [0,sp.Rational(3,2)]:
            for output in [(2,3),(0,2),(0,1),(1,0)]:
                T,direct=check_case(old,3,kernel,4,output,shared)
                counts['weighted'] += 1
                edges,n,boundary=glue(old,3,(0,1),kernel,4,output,shared)
                permutation=[2,4,1,0,3]
                M=xi*sp.eye(n)-laplacian(edges,n)
                permuted=M.extract(permutation,permutation)
                out=tuple(permutation.index(a) for a in boundary)
                assert passport(permuted,out) == direct
                counts['permuted'] += 1
    print('PASS: 32 weighted cases and cofactor signs under permutation.',flush=True)
    # E_old(2)=0: paths a-u-b and a-c-d-b join to a pentagon, output (c,d).
    _, singular=check_case({(0,2):1,(1,2):1},3,base,4,(2,3))
    assert lap_passport({(0,2):1,(1,2):1},3,(0,1)).subs(xi,2)==sp.Matrix([-2,-1,-1,1,0])
    assert singular.subs(xi,2)==sp.Matrix([2,1,1,1,0])
    kernel,matrices,s0,numeric,z0=hexagon_transfers()
    for length in range(3):
        for word in product([2,3,4],repeat=length):
            edges,n,boundary,state=kernel.copy(),6,(0,1),s0
            for j in word:
                edges,n,boundary=glue(edges,n,boundary,kernel,6,(j,j+1),1)
                state=(matrices[j]*state).applyfunc(sp.expand)
            assert lap_passport(edges,n,boundary)==state
            counts['polynomial_chains'] += 1
    # Longer chains use direct integer determinants at three exact parameters.
    for word in [(2,3,4), (4,2,3), (2,2,4,3), (4,3,2,2,4), (3,)*7]:
        edges,n,boundary=kernel.copy(),6,(0,1)
        states={value:s0.subs(xi,value) for value in [-1,0,2]}
        for j in word:
            edges,n,boundary=glue(edges,n,boundary,kernel,6,(j,j+1),1)
            states={value:matrices[j].subs(xi,value)*s for value,s in states.items()}
        for value,s in states.items():
            assert lap_passport(edges,n,boundary,value)==s
            counts['numeric_chain_states'] += 1
    results=dict(convention='input (0,1)=(a,b); output (j,j+1); shared edge counted once',
        T={str(j):[[str(x) for x in row] for row in T.tolist()] for j,T in matrices.items()},
        initial=[str(x) for x in s0],
        at_minus_one={str(j):T.tolist() for j,T in numeric.items()},
        rooted_initial=list(z0),rooted_two_hexagons={str(j):list(T*z0) for j,T in numeric.items()},
        singular_input=[-2,-1,-1,1,0],singular_output=[2,1,1,1,0],checks=counts)
    (OUT/'boundary-transfer-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2,
        default=lambda z:int(z))+'\n',encoding='utf-8')
    print('PASS:',json.dumps(counts),flush=True)


if __name__=='__main__':
    verify()
