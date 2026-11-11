---
title: "Example: Spectra and Diagonalization in Polyform Algebra"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-spectral-diagonalization
lang: en
description: "Six exact diagonalization examples. Reconstruct Laplacians, Greenians, and polyforms from modes, transform a path into a cycle by a Chebyshev polynomial, and check what information diagonal projection loses."
order: 21
---

Six exact diagonalization examples. Reconstruct Laplacians, Greenians, and polyforms from modes, transform a path into a cycle by a Chebyshev polynomial, and check what information diagonal projection loses.

[[ru/PythonExamples/Пример - Спектры и диагонализация в алгебре полиформ|Русский]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra ba4e62a](https://github.com/magin67/polyform_algebra/commit/ba4e62a1c1bc7b1d7957fc33fdd3d6ae45b9cfcf).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/spectral-diagonalization.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/spectral-diagonalization.ipynb)

## Diagonalizing the path P3

Find the projectors of the two nonzero modes of the path $a-b-c$. Reconstruct the Laplacian and Greenian, then compare grades one and two of the exponentials built from modes and from vertex-pair coefficients.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#All grades and duality for the path P3|Related section of the note]].

```python
from fractions import Fraction as Q

from sympy import Matrix, cos, pi, simplify, sqrt, zeros

from polyform_algebra.core import (
    InvalidInput, equivalent, exterior, form_exp, grade_part, green, laplacian,
    laplacian_form, network, network_from_laplacian, polar_form, resistance,
)
from polyform_algebra.duality import greenian_form
from polyform_algebra.spectral import (
    chebyshev_laplacian, fixed_basis_projection, laplacian_projectors,
)
from polyform_algebra.toponomes import laplacian_polynomial


def path(labels):
    return network(tuple(labels), [(a, b, 1) for a, b in zip(labels, labels[1:])])


def cycle(labels):
    return network(tuple(labels), [(a, b, 1) for a, b in zip(labels, labels[1:] + labels[:1])])


def lap_matrix(graph):
    return Matrix(laplacian(graph).value.values)


def projector(mode):
    vector = Matrix(mode)
    return vector * vector.T / vector.dot(vector)


def modal_form(context, mode):
    vector = exterior(context, tuple(((i,), value) for i, value in enumerate(mode) if value))
    return polar_form(vector, vector).value * Q(1, 2 * sum(value**2 for value in mode))


def modal_sum(context, modes, coefficients):
    first, *rest = [modal_form(context, mode) * coefficient
                    for mode, coefficient in zip(modes, coefficients, strict=True)]
    return sum(rest, first)


p3 = path("abc")
modes = ((1, 0, -1), (1, -2, 1))
p3_blocks = laplacian_projectors(p3)
assert set(p3_blocks) == {0, 1, 3}
assert p3_blocks[1] == projector(modes[0])
assert p3_blocks[3] == projector(modes[1])
assert p3_blocks[1] + 3*p3_blocks[3] == lap_matrix(p3)
assert p3_blocks[1] + p3_blocks[3]/3 == Matrix(green(p3).value.values)

for weights, direct in (((1, 3), laplacian_form(p3).value),
                        ((1, Q(1, 3)), greenian_form(p3).value)):
    from_modes = form_exp(modal_sum(p3.context, modes, weights)).value
    from_pairs = form_exp(direct).value
    for grade in (1, 2):
        left = grade_part(from_modes, grade).value
        right = grade_part(from_pairs, grade).value
        assert equivalent(left, right).value
print("P3: eigenvalues 0, 1, 3; Laplacian and Greenian grades 1 and 2 agree")
```

## A repeated eigenvalue of C4

Change the basis in the two-dimensional eigenspace for $\lambda=2$. Check that the projector, the second grade, and all pair resistances agree for both bases.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms#The second grade of C4: counting directions|Related section of the note]].

```python
c4 = cycle("abcd")
blocks = laplacian_projectors(c4)
assert {value: block.trace() for value, block in blocks.items()} == {0: 1, 2: 2, 4: 1}
original_modes = ((1, 0, -1, 0), (0, 1, 0, -1))
rotated_modes = ((1, 1, -1, -1), (1, -1, -1, 1))
mode4 = (1, -1, 1, -1)
for basis in (original_modes, rotated_modes):
    assert sum(map(projector, basis), zeros(4)) == blocks[2]
    modal_exponential = form_exp(modal_sum(c4.context, (*basis, mode4), (2, 2, 4))).value
    edge_exponential = form_exp(laplacian_form(c4).value).value
    assert equivalent(grade_part(modal_exponential, 2).value, grade_part(edge_exponential, 2).value).value
    reconstructed = sum(map(projector, basis), zeros(4))/2 + projector(mode4)/4
    by_mode = Matrix(4, 4, lambda i, j: reconstructed[i, i] + reconstructed[j, j] - 2*reconstructed[i, j])
    assert by_mode == Matrix(resistance(c4).value.values)
print("C4: rank-two projector, second grade and resistances survive a basis change")
```

## Eigenmodes of P6 and C6

Check the exact eigenvalues and multiplicities, and verify the cosine modes of the path. For opposite vertices $a,d$ of the cycle, sum the contributions of the eigenspaces to the resistance.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles#Which modes contribute to an effective resistance|Related section of the note]].

```python
p6 = path("abcdef")
c6 = cycle("abcdef")
for graph, expected in (
    (p6, (0, 2-sqrt(3), 1, 2, 3, 2+sqrt(3))),
    (c6, (0, 1, 1, 3, 3, 4)),
):
    spectrum = laplacian_projectors(graph)
    for value in set(expected):
        assert spectrum[value].trace() == expected.count(value)
    assert len(spectrum) == len(set(expected))

for k in range(6):
    mode = Matrix([cos(pi*k*(i+Q(1, 2))/6) for i in range(6)])
    eigenvalue = 2 - 2*cos(pi*k/6)
    assert (lap_matrix(p6)*mode - eigenvalue*mode).applyfunc(simplify) == zeros(6, 1)

c6_blocks = laplacian_projectors(c6)
difference = Matrix([1, 0, 0, -1, 0, 0])
contributions = {value: (difference.T*block*difference)[0]/value
                 for value, block in c6_blocks.items() if value}
assert sum(contributions.values()) == resistance(c6, pairs=(("a", "d"),)).value.values[0] == Q(3, 2)
print("C6 opposite-pair resistance contributions:", {str(key): str(value) for key, value in contributions.items()})
```

## Chebyshev transformation from P6 to C6

Compute $4L-L^2$ and reorder the vertices to compare the full matrix with the Laplacian of $C_6$. Check that the third step produces a second component.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle#Angle doubling turns a path into a cycle|Related section of the note]].

```python
original = lap_matrix(p6)
doubled = chebyshev_laplacian(p6, 2)
assert doubled == 4*original - original**2
order = [p6.context.labels.index(label) for label in "abdfec"]
assert doubled.extract(order, order) == lap_matrix(c6)
assert doubled.charpoly().all_coeffs() == lap_matrix(c6).charpoly().all_coeffs()
assert len(network_from_laplacian(chebyshev_laplacian(p6, 3).tolist(), p6.context.labels).value.components) == 2
print("P6 doubled: cycle order a-b-d-f-e-c-a; the step-three transform disconnects")
```

## The cone in the fixed P3 basis

Recover conductances from two spectral coordinates $a,b$. Check the condition $a\geq0$ and $0\leq b\leq3a$ inside the cone, on its boundary, and outside it.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis#A complete example: the eigenbasis of P3|Related section of the note]].

```python
for a, b in ((0, 0), (2, 0), (1, 3), (2, 3), (1, 4), (-1, 0)):
    candidate = a*p3_blocks[1] + b*p3_blocks[3]
    conductances = tuple(-candidate[i, j] for i, j in ((0, 1), (0, 2), (1, 2)))
    assert conductances == (Q(b, 3), Q(3*a-b, 6), Q(b, 3))
    inside = a >= 0 and 0 <= b <= 3*a
    assert inside == all(value >= 0 for value in conductances)
    if inside:
        rebuilt = network_from_laplacian(candidate.tolist(), p3.context.labels).value
        assert fixed_basis_projection(rebuilt, modes) == ((a, b), candidate)
    print("P3 cone", (a, b), "conductances:", tuple(map(str, conductances)))
```

## Different graphs with the same projection

Two weighted graphs have identical diagonal coordinates in the fixed basis. Compare their original rooted polynomials and check the sign of a conductance in the projected matrix.

[[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Projection onto a Fixed Spectral Basis and Loss of Information#Different graphs with the same projection|Related section of the note]].

```python
rotated = ((2, 1, -2, -1), (-1, 2, 1, -2), (1, -1, 1, -1))


def weighted_cycle_family(r):
    return network(tuple("abcd"), [
        ("a", "b", -(2+3*r)/10), ("c", "d", -(2+3*r)/10),
        ("a", "d", (22+3*r)/10), ("b", "c", (22+3*r)/10),
        ("a", "c", (17-2*r)/5), ("b", "d", (8+2*r)/5),
    ])


first, second = (weighted_cycle_family(Q(r)) for r in (-4, -3))
values, projected = fixed_basis_projection(first, rotated)
assert fixed_basis_projection(second, rotated) == (values, projected)
assert values == (10, 4, 4)
assert lap_matrix(first) != lap_matrix(second)
assert laplacian_polynomial(first) == (1, 18, 80, 96)
assert laplacian_polynomial(second) == (1, 18, 87, 124)
assert -projected[0, 1] == -Q(1, 5)
try:
    network_from_laplacian(projected.tolist(), tuple("abcd"))
except InvalidInput:
    pass
else:
    raise AssertionError("the projected matrix has a negative conductance")
print("Same projection (10, 4, 4); different rooted polynomials:",
      tuple(map(str, laplacian_polynomial(first))), tuple(map(str, laplacian_polynomial(second))))
```
