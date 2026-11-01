"""Exact, independent checks for the first isomer-spectra note.

Run from any directory with Python 3.10+ and SymPy installed.
The forest enumeration does not use determinants or transfer matrices.
"""
from collections import Counter
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
xi, t = sp.symbols('xi t')
CORES = ([0, 1, 9, 8, 7, 6], [0, 1, 2, 3, 4, 5])


def cycle(vertices):
    return {tuple(sorted((a, b))) for a, b in zip(vertices, vertices[1:] + vertices[:1])}


def graph(label):
    third = [3, 4, 13, 12, 11, 10] if label == 'A' else [2, 3, 13, 12, 11, 10]
    cores = [*CORES, third]
    return cores, sorted(set().union(*(cycle(c) for c in cores)))


def laplacian(edges, n):
    matrix = sp.zeros(n)
    for a, b in edges:
        matrix[a, a] += 1
        matrix[b, b] += 1
        matrix[a, b] -= 1
        matrix[b, a] -= 1
    return matrix


def forests(edges, n):
    ordinary, rooted = [0] * n, [0] * n
    shapes = Counter()
    for mask in range(1 << len(edges)):
        parent, sizes = list(range(n)), [1] * n

        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a

        for i, (a, b) in enumerate(edges):
            if mask & (1 << i):
                a, b = find(a), find(b)
                if a == b:
                    break
                parent[a] = b
                sizes[b] += sizes[a]
        else:
            grade = mask.bit_count()
            component_sizes = [sizes[i] for i in range(n) if parent[i] == i]
            ordinary[grade] += 1
            rooted[grade] += int(sp.prod(component_sizes))
            if grade == 4:
                shapes[tuple(sorted((v for v in component_sizes if v > 1), reverse=True))] += 1
    return ordinary, rooted, shapes


def reduced_cycle(j, y, d, w):
    matrix = sp.diag(*([y] * 6))
    for i in range(6):
        matrix[i, (i + 1) % 6] = matrix[(i + 1) % 6, i] = 1
    for a, b in [(0, 1), (j, j + 1)]:
        matrix[a, a] = matrix[b, b] = d
        matrix[a, b] = matrix[b, a] = w
    return matrix


def verify():
    results, polynomials = {}, {}
    for label in ['A', 'B']:
        cores, edges = graph(label)
        assert len(edges) == 16 and set(sum(cores, [])) == set(range(14))
        assert set(cores[0]) & set(cores[1]) == {0, 1}
        assert not set(cores[0]) & set(cores[2])
        assert set(cores[1]) & set(cores[2]) == ({3, 4} if label == 'A' else {2, 3})
        matrix = laplacian(edges, 14)
        assert matrix == matrix.T and matrix * sp.ones(14, 1) == sp.zeros(14, 1)
        chi = sp.expand((xi * sp.eye(14) - matrix).det(method='domain-ge'))
        assert chi == matrix.charpoly(xi).as_expr()
        ordinary, rooted, shapes = forests(edges, 14)
        assert chi == sum((-1)**g * p * xi**(14-g) for g, p in enumerate(rooted))
        forest_poly = sum(p * t**g for g, p in enumerate(rooted))
        assert forest_poly == sp.expand((sp.eye(14) + t * matrix).det(method='domain-ge'))
        assert ordinary[-1] == 204 and rooted[-1] == 14 * 204
        red = matrix[:13, :13]
        inverse = red.inv()
        diagonal = sp.Matrix([inverse[i, i] for i in range(13)])
        radius = (diagonal.T * red * diagonal)[0] / 4
        assert red.det() == 204 and radius == sp.Rational(43595, 41616)
        centering = sp.ones(14) / 14
        green = (matrix + centering).inv() - centering
        resistance = sp.Matrix(14, 14, lambda i, j: green[i, i] + green[j, j] - 2*green[i, j])
        assert sp.Rational(1, 2) / (sp.ones(1, 14) * resistance.inv() * sp.ones(14, 1))[0] == radius
        kirchhoff = sum(resistance[i, j] for i in range(14) for j in range(i+1, 14))
        assert kirchhoff == sp.Rational(rooted[-2], 204)
        degrees = list(matrix.diagonal())
        adjacency = sp.diag(*degrees) - matrix
        assert sp.trace(adjacency**3) == 0
        assert sp.trace(adjacency**4) == 2*sum(v*v for v in degrees) - 32
        degree_product = sum(degrees[a]*degrees[b] for a, b in edges)
        traces = [sp.trace(matrix**j) for j in range(1, 5)]
        assert traces[3] == sum(v**4 + 4*v**3 + 2*v*v for v in degrees) + 4*degree_product - 32
        assert traces == [32, 108, 416, 1716 if label == 'A' else 1720]
        assert rooted[4] == (21509 if label == 'A' else 21508)
        induced = [(a, b) for a, b in edges if degrees[a] == degrees[b] == 3]
        assert len(induced) == (2 if label == 'A' else 3)
        results[label] = dict(cores=cores, edges=edges, laplacian=matrix.tolist(),
            degrees=degrees, chi=str(chi), factorization=str(sp.factor(chi)),
            ordinary=ordinary, rooted=rooted, P1=forest_poly.subs(t, 1),
            grade4_shapes={','.join(map(str, shape)):count for shape, count in sorted(shapes.items())},
            tau=red.det(), rho=str(radius), kirchhoff=str(kirchhoff),
            traces=traces, edge_degree_products=degree_product, degree3_edges=induced)
        polynomials[label] = chi
    delta = polynomials['A'] - polynomials['B']
    expected = xi**2 * (xi**2 - 5*xi + 5)**4
    assert sp.expand(delta - expected) == 0
    cycle5 = laplacian(sorted(cycle(list(range(5)))), 5).charpoly(xi).as_expr()
    assert sp.expand(delta - cycle5**2) == 0
    assert sp.gcd(polynomials['A'], polynomials['B']) == xi
    assert results['A']['ordinary'] == results['B']['ordinary']
    assert sum((a-b)*t**g for g, (a,b) in enumerate(zip(results['A']['rooted'], results['B']['rooted']))) == sp.expand(t**4*(1+5*t+5*t*t)**4)
    assert results['A']['P1'] == 2518737 and results['B']['P1'] == 2504096
    # The straight chain includes the path spectrum described by Yang--Zhang.
    path7 = laplacian([(i, i+1) for i in range(6)], 7).charpoly(xi).as_expr()
    assert sp.rem(polynomials['A'], path7, xi) == 0

    y, d, w = sp.symbols('y d w')
    k, ell = y**4 - 3*y*y + 1, y**3 - 2*y
    block = sp.diag(y, y, y, y)
    for i in range(3):
        block[i, i+1] = block[i+1, i] = 1
    assert sp.expand(block.det() - k) == 0
    assert sp.cancel(block.inv()[0, 0] - ell/k) == 0
    assert sp.cancel(block.inv()[0, 3] + 1/k) == 0
    assert sp.expand(ell**2 - y*k*ell + k*k) == 1
    a = d*d - w*w
    det_a = reduced_cycle(3, y, d, w).det(method='domain-ge')
    det_b = reduced_cycle(2, y, d, w).det(method='domain-ge')
    assert sp.expand(det_a - a*(a*y*y - 4*d*y + 4)) == 0
    assert sp.expand(det_b - (a*a*y*y - (a+d*y-1)**2)) == 0
    assert sp.expand(det_a-det_b-(-d*d+d*y+w*w-1)**2) == 0
    substitution = {d:y-1-ell/k, w:1+1/k}
    assert sp.cancel(k*(-d*d+d*y+w*w-1).subs(substitution)-(y*k-2*ell+2)) == 0
    assert sp.expand(y*k-2*ell+2-(y+2)*(y*y-y-1)**2) == 0
    for label, j in [('A', 3), ('B', 2)]:
        schur_poly = sp.cancel(k*k*reduced_cycle(j, y, d, w).det(method='domain-ge').subs(substitution))
        assert sp.expand(schur_poly.subs(y, xi-2)-polynomials[label]) == 0
    results['checks'] = dict(subsets_per_graph=65536, forest_and_determinant_agree=True,
        schur_identity=True, all_arithmetic='exact integer or rational',
        difference=str(sp.expand(delta)), difference_factor=str(sp.factor(delta)))
    (OUT/'three-hexagons-results.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2, default=lambda value:int(value))+'\n', encoding='utf-8')
    print('PASS: both determinants, 131072 edge subsets, radii, forest types, traces, and symbolic Schur proof.')


if __name__ == '__main__':
    verify()
