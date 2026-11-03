"""Exact higher-grade audit; Python standard library only.

Compare exterior minors, complementary forest potentials and rebuilt metrics.
All identities are checked as matrices of linear functionals on forms, so the
checks include mixed forms and non-decomposable exterior inputs.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import prod
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'variations'))
from verify_single_edge import determinant, inverse, vector, reduced_laplacian, pairing


def zero(rows, cols=None):
    return [[Q(0) for _ in range(rows if cols is None else cols)] for _ in range(rows)]


def compound(matrix, k):
    if k == 0:
        return [[Q(1)]]
    return [[determinant([[matrix[i][j] for j in J] for i in I])
             for J in combinations(range(len(matrix[0])), k)]
            for I in combinations(range(len(matrix)), k)]


def blade(columns, d):
    return [determinant([[v[i] for v in columns] for i in I])
            for I in combinations(range(d), len(columns))]


def add_outer(target, a, weight=Q(1)):
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            target[i][j] += weight * x * y


def matvec(matrix, v):
    return [sum(x*y for x, y in zip(row, v)) for row in matrix]


def forest_metric(n, weights, k):
    """Expand tau(M f) in complementary forests, without inverse matrices."""
    d = n-1
    indices = list(combinations(range(d), k))
    result = zero(len(indices))
    edges = [e for e, c in weights.items() if c]
    for F in combinations(edges, d-k):
        columns = [vector(n, e) for e in F]
        tests = []
        for I in indices:
            basis = [[Q(i == j) for i in range(d)] for j in I]
            tests.append(blade(basis + columns, d)[0])
        add_outer(result, tests, prod((weights[e] for e in F), start=Q(1)))
    return result


def data(n, weights, k, H=None):
    H = H or inverse(reduced_laplacian(n, weights))
    Hk = compound(H, k)
    rows = {}
    blades = {}
    for J in combinations(weights, k):
        b = blade([vector(n, e) for e in J], n-1)
        h = matvec(Hk, b)
        matrix = zero(len(h))
        add_outer(matrix, h, prod((weights[e] for e in J), start=Q(1)))
        rows[J] = matrix
        blades[J] = b
    return Hk, rows, blades


def audit_graph(n, weights):
    H = inverse(reduced_laplacian(n, weights))
    tau = forest_metric(n, weights, 0)[0][0]
    assert tau == determinant(reduced_laplacian(n, weights)) > 0
    counts = {'grades': n, 'finite_matrix_comparisons': 0, 'finite_form_entries': 0}
    grades = {}
    for k in range(n):
        Hk, rows, _ = data(n, weights, k, H)
        size = len(Hk)
        summed = [[sum(row[i][j] for row in rows.values()) for j in range(size)] for i in range(size)]
        assert summed == Hk
        forest = forest_metric(n, weights, k)
        assert [[x/tau for x in row] for row in forest] == Hk
        marginals = {e: [[sum(row[i][j] for J, row in rows.items() if e in J)
                          for j in range(size)] for i in range(size)] for e in weights}
        assert [[sum(A[i][j] for A in marginals.values()) for j in range(size)]
                for i in range(size)] == [[k*x for x in row] for row in Hk]
        # Right multiplication by an edge, independent of the graph metric.
        indices = list(combinations(range(n-1), k))
        for e in combinations(range(n), 2):
            a = vector(n, e)
            R = pairing(a, H, a)
            if k == n-1:
                product_metric = zero(size)
            else:
                basis = [[[Q(i == j) for i in range(n-1)] for j in I] for I in indices]
                wedges = [blade(cols + [a], n-1) for cols in basis]
                Hnext = compound(H, k+1)
                product_metric = [[pairing(u, Hnext, v) for v in wedges] for u in wedges]
            sensitivity = [[R*Hk[i][j]-product_metric[i][j] for j in range(size)] for i in range(size)]
            c = weights.get(e, Q(0))
            if c:
                assert marginals[e] == [[c*x for x in row] for row in sensitivity]
            grades[k, e] = Hk, sensitivity, R
        # Reversing any auxiliary edge orientation leaves its form and all
        # coefficient functionals unchanged.
        for J, row in rows.items():
            if J:
                cols = [vector(n, e) for e in J]
                cols[0] = [-x for x in cols[0]]
                h = matvec(Hk, blade(cols, n-1))
                reversed_row = zero(size)
                add_outer(reversed_row, h, prod((weights[e] for e in J), start=Q(1)))
                assert reversed_row == row
    for e in combinations(range(n), 2):
        c = weights.get(e, Q(0))
        deltas = [c, -c/2, c/3] if c else [Q(1), Q(1,3)]
        R = grades[0, e][2]
        if c and c*R < 1:
            deltas.append(-c)
        for t in deltas:
            changed = dict(weights); changed[e] = c+t
            Hnew = inverse(reduced_laplacian(n, changed))
            new_tau = forest_metric(n, changed, 0)[0][0]
            assert new_tau == tau*(1+t*R)
            for k in range(n):
                Hk, sensitivity, _ = grades[k, e]
                direct = compound(Hnew, k)
                expected = [[Hk[i][j]-t/(1+t*R)*sensitivity[i][j]
                             for j in range(len(Hk))] for i in range(len(Hk))]
                assert direct == expected
                forest = forest_metric(n, changed, k)
                assert direct == [[x/new_tau for x in row] for row in forest]
                counts['finite_matrix_comparisons'] += 1
                counts['finite_form_entries'] += len(Hk)**2
    return counts


def example(n, weights, labels, vertices, other=None):
    d = n-1
    k = len(vertices)-1
    X = blade([vector(n, (vertices[0], j)) for j in vertices[1:]], d)
    other = other or vertices
    Y = blade([vector(n, (other[0], j)) for j in other[1:]], d)
    H = inverse(reduced_laplacian(n, weights))
    Hk, rows, blades = data(n, weights, k, H)
    coeff = {J: pairing(X, row, Y) for J, row in rows.items()}
    value = pairing(X, Hk, Y)
    assert sum(coeff.values()) == value
    A = {e: sum(m for J, m in coeff.items() if e in J) for e in weights}
    assert sum(A.values()) == k*value
    edges = []
    for e, c in weights.items():
        a = vector(n, e)
        changed = dict(weights); changed[e] = 2*c
        direct = pairing(X, compound(inverse(reduced_laplacian(n, changed)), k), Y)
        R = pairing(a, H, a)
        assert direct == value-A[e]/(1+c*R)
        edges.append({'edge': labels[e], 'c': str(c), 'A': str(A[e]),
                      'R': str(R), 'doubled_value': str(direct), 'delta': str(direct-value)})
    return {'value': str(value), 'sum_A': str(sum(A.values())),
            'output_norm': str(sum(coeff[J]*pairing(b, Hk, b) for J, b in blades.items())),
            'coefficients': [{'edges': [labels[e] for e in J], 'm': str(m)} for J, m in coeff.items()],
            'edges': edges}


def review_examples():
    """Two forms with equal edge probes; interacting changes on a tree."""
    weights = {e: Q(1) for e in [(0,1),(1,2),(2,3),(0,3)]}
    Hk, rows, blades = data(4, weights, 2)
    triangles = [(0,1,2),(0,2,3),(0,1,3),(1,2,3)]
    objects = [blade([vector(4,(i,j)),vector(4,(i,k))],3) for i,j,k in triangles]
    forms = [objects[:2], objects[2:]]
    evaluate = lambda form, metric: sum(pairing(X,metric,X) for X in form)
    coeff = [{J: evaluate(form,row) for J,row in rows.items()} for form in forms]
    fields = [{e:sum(m for J,m in field.items() if e in J) for e in weights}
              for field in coeff]
    assert fields[0] == fields[1] == {e:Q(1,2) for e in weights}
    assert [evaluate(form,Hk) for form in forms] == [Q(1),Q(1)]
    pair = ((0,1),(1,2))
    assert [field[pair] for field in coeff] == [Q(1,4),Q(1,8)]
    output_difference = zero(3)
    for J,b in blades.items():
        add_outer(output_difference,b,coeff[0][J]-coeff[1][J])
    assert output_difference != zero(3)
    probe_count = 0
    for e in weights:
        for t in (Q(1),Q(-1,2),Q(1,3),Q(-1)):
            changed = dict(weights); changed[e] += t
            metric = compound(inverse(reduced_laplacian(4,changed)),2)
            expected = Q(1)-t*Q(1,2)/(1+t*Q(3,4))
            assert [evaluate(form,metric) for form in forms] == [expected,expected]
            tau = forest_metric(4,changed,0)[0][0]
            assert metric == [[x/tau for x in row] for row in forest_metric(4,changed,2)]
            probe_count += 1
    X = blade([vector(3,(0,1)),vector(3,(0,2))],2)
    tree_values = []
    for x,y in ((Q(1),Q(1)),(Q(2),Q(1)),(Q(1),Q(2)),(Q(2),Q(2))):
        tree = {(0,1):x,(1,2):y}
        metric = compound(inverse(reduced_laplacian(3,tree)),2)
        value = pairing(X,metric,X)
        assert value == 1/(x*y)
        tau = forest_metric(3,tree,0)[0][0]
        assert value == pairing(X,forest_metric(3,tree,2),X)/tau
        tree_values.append(value)
    initial,left,right,joint = tree_values
    additive = initial+(left-initial)+(right-initial)
    assert joint == Q(1,4) and additive == 0
    return {'square_same_field':{'value':'1','edge_influences':['1/2']*4,
                'pair_ab_bc':[str(field[pair]) for field in coeff],
                'outputs_differ':True,'finite_probe_comparisons':probe_count},
            'tree_joint_change':{'initial':str(initial),'separate_values':[str(left),str(right)],
                'joint':str(joint),'incorrect_sum_of_probes':str(additive)}}


def main():
    tri = [(0,1),(1,2),(0,2)]
    square = [(0,1),(1,2),(2,3),(0,3)]
    star = [(0,1),(0,2),(0,3),(0,4)]
    specs = [
        ('weighted_star',5,star,[1,2,3,1]), ('unit_star',5,star,[1]*4),
        ('unit_triangle',3,tri,[1]*3), ('weighted_triangle',3,tri,[2,3,5]),
        ('unit_square',4,square,[1]*4), ('weighted_square',4,square,[2,3,5,7]),
        ('square_bridge',4,square+[(1,3)],[1]*5),
        ('weighted_K4',4,list(combinations(range(4),2)),[1,2,3,4,5,6]),
        ('unit_K5',5,list(combinations(range(5),2)),[1]*10)]
    counts = {}; graphs = {}
    for name, n, edges, weights in specs:
        w = dict(zip(edges, map(Q, weights))); graphs[name] = n,w
        counts[name] = audit_graph(n,w)
        print(name + ': all grades, forests and finite changes passed', flush=True)
    examples = {}
    for name in ('unit_triangle','weighted_triangle','unit_square','weighted_square'):
        n,w = graphs[name]
        labels = {e: ''.join(chr(97+i) for i in e) for e in w}
        examples[name] = example(n,w,labels,[0,1,2])
    n,w = graphs['weighted_star']
    labels = {e:'h'+'abcd'[e[1]-1] for e in w}
    examples['weighted_star'] = example(n,w,labels,[1,2,3])
    assert examples['weighted_star']['value'] == '1'
    assert [e['A'] for e in examples['weighted_star']['edges']] == ['5/6','2/3','1/2','0']
    # Tree criterion: removing the pair separates the three marked vertices.
    for row in examples['weighted_star']['coefficients']:
        assert (Q(row['m']) > 0) == ('hd' not in row['edges'])
    assert examples['unit_square']['value'] == '1/2'
    assert [r['m'] for r in examples['unit_square']['coefficients']] == ['1/4','1/16','1/16','1/16','1/16','0']
    assert [e['doubled_value'] for e in examples['unit_square']['edges']] == ['2/7','2/7','3/7','3/7']
    n,w = graphs['unit_square']; labels = {e:''.join(chr(97+i) for i in e) for e in w}
    examples['square_mixed'] = example(n,w,labels,[0,1,2],[0,1,3])
    assert examples['square_mixed']['value'] == '1/4'
    assert [r['m'] for r in examples['square_mixed']['coefficients']] == ['1/8','-1/16','1/8','0','1/16','0']
    # Non-simple bivector on a 4-dimensional space: sum of two independent blades.
    n,w = graphs['unit_star']; Hk, rows, _ = data(n,w,2)
    left = blade([vector(n,(0,1)),vector(n,(0,2))],n-1)
    right = blade([vector(n,(0,3)),vector(n,(0,4))],n-1)
    X = [x+y for x,y in zip(left,right)]
    assert sum(pairing(X,row,X) for row in rows.values()) == pairing(X,Hk,X) == 2
    # A pair coefficient is not a mixed second derivative. For N=1/tau,
    # N_xy=2 tau_x tau_y/tau^3-tau_xy/tau^2 at x=y=z=1.
    mixed_derivative = 2*Q(2)*2/Q(3)**3-Q(1)/3**2
    assert mixed_derivative == Q(5,27) != Q(1,9)
    # Finite effects of separately doubled edges cannot be added.
    separate = Q(1,3)+2*(Q(1,5)-Q(1,3))
    joint = Q(1, 2*2+2*1+2*1)
    assert separate == Q(1,15) and joint == Q(1,8)
    totals = {key:sum(v[key] for v in counts.values()) for key in next(iter(counts.values()))}
    result = {'status':'passed','graphs':counts,'totals':totals,'examples':examples,
              'review_examples':review_examples(),
              'limits':{'mixed_second_derivative':str(mixed_derivative),'pair_coefficient':'1/9',
                        'joint_triangle_norm':str(joint),'incorrect_sum_of_probes':str(separate)}}
    Path(__file__).with_name('higher-grade-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':'passed','graphs':len(counts),**totals}))


if __name__ == '__main__':
    main()
