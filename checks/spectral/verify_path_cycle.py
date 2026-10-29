"""Exact P6/C6/C5 checks and numerical family checks for the third note.

Requires SymPy and NumPy. Exact projectors are obtained from the edge
Laplacian by interpolation, independently of the trigonometric mode formulas.
Run without -O. No files are written and no network access is used.
"""
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import prod
import json
import numpy as np
import sympy as sp
from verify_diagonal import add, multiply, scale, form_matrix, forest_partition


def laplacian(n, cycle):
    edges = [(i, i+1, 1) for i in range(n-1)]
    if cycle:
        edges.append((n-1, 0, 1))
    matrix = sp.zeros(n)
    for i, j, _ in edges:
        matrix[i, i] += 1
        matrix[j, j] += 1
        matrix[i, j] -= 1
        matrix[j, i] -= 1
    return matrix, edges


def modes(n, cycle):
    """Return numerical columns, eigenvalues, and frequency labels."""
    r = np.arange(n)
    columns = [np.ones(n)/np.sqrt(n)]
    eigenvalues, labels = [0.0], ["0"]
    if cycle:
        for k in range(1, (n-1)//2+1):
            theta = 2*np.pi*k/n
            columns.extend([np.sqrt(2/n)*np.cos(theta*r),
                            np.sqrt(2/n)*np.sin(theta*r)])
            eigenvalues.extend([2-2*np.cos(theta)]*2)
            labels.extend([f"{k}c", f"{k}s"])
        if n % 2 == 0:
            columns.append((-1.0)**r/np.sqrt(n))
            eigenvalues.append(4.0)
            labels.append("pi")
    else:
        for k in range(1, n):
            theta = np.pi*k/n
            columns.append(np.sqrt(2/n)*np.cos(theta*(r+.5)))
            eigenvalues.append(2-2*np.cos(theta))
            labels.append(str(k))
    return np.column_stack(columns), np.array(eigenvalues), labels


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def equal(a, b):
    if isinstance(a, sp.MatrixBase):
        assert clean(a-b) == sp.zeros(*a.shape)
    else:
        assert sp.simplify(a-b) == 0


def projector(matrix, value, distinct):
    result = sp.eye(matrix.rows)
    for other in distinct:
        if other != value:
            result = clean(result*(matrix-other*sp.eye(matrix.rows))/(value-other))
    return result


def coefficients(matrix):
    t = sp.Symbol("t")
    p = sp.Poly((sp.eye(matrix.rows)+t*matrix).det(), t)
    return [p.nth(g) for g in range(matrix.rows)]


def exact_example(n, cycle, spectrum, expected):
    L, edges = laplacian(n, cycle)
    identity, constant = sp.eye(n), sp.ones(n)/n
    Gr = (L+constant).inv()-constant
    distinct = list(dict.fromkeys(spectrum))
    E = [projector(L, value, distinct) for value in distinct]
    equal(sum(E, sp.zeros(n)), identity)
    equal(E[0], constant)
    for i, (value, project) in enumerate(zip(distinct, E)):
        equal(project*project, project)
        equal(L*project, value*project)
        equal(sp.trace(project), spectrum.count(value))
        for other in E[:i]:
            equal(project*other, sp.zeros(n))
    equal(sum((value*project for value, project in zip(distinct, E)), sp.zeros(n)), L)
    equal(sum((project/value for value, project in zip(distinct[1:], E[1:])), sp.zeros(n)), Gr)
    equal(L*Gr, identity-constant)

    U, lambdas, labels = modes(n, cycle)
    for value, project in zip(distinct, E):
        selected = U[:, np.isclose(lambdas, float(value), atol=1e-12, rtol=0)]
        assert np.max(np.abs(selected@selected.T-np.array(project, dtype=float))) < 1e-12

    p = coefficients(L)
    assert p == expected
    t = sp.Symbol("t")
    spectral_polynomial = sp.Poly(sp.expand(prod(1+t*v for v in spectrum)), t)
    assert [sp.simplify(spectral_polynomial.nth(g)) for g in range(n)] == p
    Delta = sp.simplify(prod(spectrum[1:]))
    tau = L[:-1, :-1].det()
    assert tau == (n if cycle else 1)
    equal(Delta, n*tau)
    assert coefficients(Gr) == [v/Delta for v in reversed(p)]

    ordinary, rooted = [0]*n, [0]*n
    for g in range(n):
        for subset in combinations(edges, g):
            parts = forest_partition(n, subset)
            if parts is not None:
                ordinary[g] += 1
                rooted[g] += prod(map(len, parts))
    assert rooted == p
    if not cycle:
        assert ordinary == [sp.binomial(n-1, g) for g in range(n)]

    # A top exterior form is determined by its principal (n-1)-minors.
    # These are the coefficients of T_n in the vertex-coordinate model.
    for deleted in range(n):
        keep = [i for i in range(n) if i != deleted]
        equal(L.extract(keep, keep).det(), tau)
        equal(Gr.extract(keep, keep).det(), 1/(n*n*tau))

    R = sp.zeros(n)
    for i, j in combinations(range(n), 2):
        q = j-i
        R[i, j] = R[j, i] = Gr[i, i]+Gr[j, j]-2*Gr[i, j]
        equal(R[i, j], sp.Rational(q*(n-q), n) if cycle else q)
        contributions = [(project[i, i]+project[j, j]-2*project[i, j])/value
                         for value, project in zip(distinct[1:], E[1:])]
        equal(sum(contributions), R[i, j])
    Kf = sum(R[i, j] for i, j in combinations(range(n), 2))
    equal(Kf, n*sp.trace(Gr))
    equal(Kf, sp.Rational(n**3-n, 12 if cycle else 6))

    pairs = [(0, 5), (2, 3)] if not cycle else ([(0, 1), (0, 2), (0, 3)] if n == 6 else [(0, 1), (0, 2)])
    rows = [[sp.simplify((project[i, i]+project[j, j]-2*project[i, j])/value)
             for value, project in zip(distinct[1:], E[1:])] for i, j in pairs]
    if not cycle:
        assert rows == [[(7+4*sp.sqrt(3))/3, 0, sp.Rational(1, 3), 0, (7-4*sp.sqrt(3))/3],
                        [sp.Rational(1, 3), 0, sp.Rational(1, 3), 0, sp.Rational(1, 3)]]
    elif n == 6:
        assert rows == [[sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 6)],
                        [1, sp.Rational(1, 3), 0], [sp.Rational(4, 3), 0, sp.Rational(1, 6)]]
        # Check the grouped second polyform grade, not just its scalar evaluation.
        S1, S2, B = [form_matrix(project.tolist()) for project in E[1:]]
        grouped = reduce(add, [scale(multiply(S1, S1), F(1, 2)),
                      scale(multiply(S2, S2), F(9, 2)),
                      scale(multiply(S1, S2), F(3)),
                      scale(multiply(S1, B), F(4)),
                      scale(multiply(S2, B), F(12))])
        Lform = form_matrix(L.tolist())
        assert grouped == scale(multiply(Lform, Lform), F(1, 2))
        assert multiply(multiply(S1, S1), S1) == multiply(multiply(S2, S2), S2) == multiply(B, B) == {}

    return {"name": ("C" if cycle else "P")+str(n), "modes": U.tolist(),
            "labels": labels, "eigenvalues": [str(v) for v in spectrum],
            "rooted": list(map(str, p)), "ordinary": ordinary,
            "Delta": str(Delta), "tau": str(tau), "Kirchhoff": str(Kf),
            "resistance_contributions": [[str(v) for v in row] for row in rows]}


def check_family():
    maximum, count = 0.0, 0
    for cycle in (False, True):
        for n in range(3 if cycle else 2, 25):
            L = np.array(laplacian(n, cycle)[0], dtype=float)
            U, values, _ = modes(n, cycle)
            constant = np.ones((n, n))/n
            Gr = np.linalg.inv(L+constant)-constant
            reconstructed = (U[:, 1:]/values[1:])@U[:, 1:].T
            q = np.abs(np.arange(n)[:, None]-np.arange(n)[None, :])
            resistance = q*(n-q)/n if cycle else q
            numerical = np.diag(Gr)[:, None]+np.diag(Gr)[None, :]-2*Gr
            errors = [np.max(np.abs(U.T@U-np.eye(n))),
                      np.max(np.abs(L@U-U*values)),
                      np.max(np.abs(Gr-reconstructed)),
                      np.max(np.abs(numerical-resistance))]
            maximum = max(maximum, *errors)
            count += 1
    assert maximum < 1e-11
    return {"graphs": count, "path_sizes": "2..24", "cycle_sizes": "3..24",
            "maximum_absolute_residual": maximum, "tolerance": 1e-11}


def check():
    results = {}
    cases = [(6, False, [0, 2-sp.sqrt(3), 1, 2, 3, 2+sp.sqrt(3)], [1, 10, 36, 56, 35, 6]),
             (6, True, [0, 1, 1, 3, 3, 4], [1, 12, 54, 112, 105, 36]),
             (5, True, [0, (5-sp.sqrt(5))/2, (5-sp.sqrt(5))/2, (5+sp.sqrt(5))/2, (5+sp.sqrt(5))/2],
              [1, 10, 35, 50, 25])]
    for args in cases:
        result = exact_example(*args)
        results[result["name"]] = result
    results["family"] = check_family()
    return results


if __name__ == "__main__":
    data = check()
    print(json.dumps({name: {key: value for key, value in result.items() if key != "modes"}
                      for name, result in data.items()}, ensure_ascii=False, indent=2))
