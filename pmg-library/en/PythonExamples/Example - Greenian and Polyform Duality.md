---
title: "Example: Greenian and Polyform Duality"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-greenian-duality
lang: en
description: "Nine exact calculations for the Greenian, duality, cuts, and toponomes."
order: 16
---

Nine calculations check the Laplacian and Greenian exponentials, cut forms, potentials, and coefficient reversal.

[[ru/PythonExamples/Пример - Гриниан и дуальность полиформ|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra e7a9647](https://github.com/magin67/polyform_algebra/commit/e7a9647f448ca0ca743f89c067601e418ef604ed).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/greenian-duality.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/greenian-duality.ipynb)

## Mutual duality on a weighted path

Build both exponentials and compare every coefficient in both deletion directions. With weights 2, 3, and 5 the top coefficients are 30 and $1/480$.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Laplacian and Greenian - Mutual Duality of Exponentials#Full example: a path on four vertices|Related section of the note]].

```python
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import prod

from sympy import Matrix, expand, eye, symbols, zeros

from polyform_algebra.core import (
    equivalent, form_exp, grade_part, green, laplacian, laplacian_form,
    network, partition_form, potential, resistance, spanning_coefficient, spanning_tree_weight,
)
from polyform_algebra.duality import (
    affine_coefficients, cut_partition_form, dual_coefficients, greenian_form,
)
from polyform_algebra.kvp import signed_forest_toponome
from polyform_algebra.toponomes import laplacian_polynomial, vertex_toponome


def path(weights):
    return network(tuple("abcd"), tuple((a, b, w) for (a, b), w in zip(("ab", "bc", "cd"), weights)))


def exponential(net, constructor):
    return form_exp(constructor(net).value).value


weighted = path((2, 3, 5))
T = partition_form(weighted.context, (weighted.context.labels,)).value
M = exponential(weighted, laplacian_form)
N = exponential(weighted, greenian_form)
tau = spanning_coefficient(M).value
sigma = spanning_coefficient(N).value
assert (tau, sigma) == (30, Fraction(1, 480))
assert dual_coefficients(M, sigma * T) == affine_coefficients(N)
assert dual_coefficients(N, tau * T) == affine_coefficients(M)
print("Weighted P₄: tau = 30, sigma = 1/480, both deletions agree")
```

## Canonical vector coefficients

Double-center the resistance table to obtain the signed vector coefficients and compare them with off-diagonal Greenian entries. Check the signed spanning-tree weight.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/The Canonical Vector Representation of the Greenian#Full example: a path on four vertices|Related section of the note]].

```python
unit_path = path((1, 1, 1))
labels = unit_path.context.labels
indices = tuple(combinations(range(len(labels)), 2))
G = Matrix(green(unit_path).value.values)
R = Matrix(resistance(unit_path).value.values)
sums = [sum(R.row(i)) for i in range(4)]
grand_mean = sum(sums) / 16
gamma = zeros(4)
for i, j in indices:
    coefficient = (R[i, j] - sums[i] / 4 - sums[j] / 4 + grand_mean) / 2
    gamma[i, j] = gamma[j, i] = coefficient
    assert coefficient == -G[i, j]
assert tuple(gamma[i, j] for i, j in indices) == tuple(Fraction(k, 8) for k in (-1, 3, 5, 1, 3, -1))
signed = signed_forest_toponome(gamma)
assert signed[(3,)] == Fraction(1, 16)
print("P₄ signed vector coefficients:", tuple(gamma[i, j] for i, j in indices))
```

## The cut expansion over original forests

Enumerate the eight forests of the original path, build their dual partition forms, and compare their sum with the Greenian exponential.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Cuts and Forest Grades of the Greenian Exponential#The forest formula for grades of the Greenian exponential|Related section of the note]].

```python
forests = Counter()
for k in range(4):
    for edges in combinations(unit_path.edges, k):
        blocks = network(labels, edges).components
        forests[blocks] += prod(weight for _, _, weight in edges)
cut_sum = sum(
    (coefficient * cut_partition_form(unit_path.context, blocks).value
     for blocks, coefficient in forests.items()),
    start=0 * partition_form(unit_path.context, ()).value,
)
unit_N = exponential(unit_path, greenian_form)
assert len(forests) == 8
assert equivalent(cut_sum, unit_N).value
blocks = (("a", "b"), ("c",), ("d",))
cut = cut_partition_form(unit_path.context, blocks).value
top = partition_form(unit_path.context, (labels,)).value
assert dual_coefficients(cut, top) == affine_coefficients(partition_form(unit_path.context, blocks).value)
print("P₄: all eight original forests give the same cut exponential")
```

## Minors of every grade

In the difference basis at the last vertex, compare the coefficients of every exponential grade with the corresponding minors.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian#Higher-grade coefficients are minors|Related section of the note]].

```python
for net in (unit_path, weighted):
    matrix = Matrix(green(net).value.values)[:-1, :-1]
    exp_green = exponential(net, greenian_form)
    for k in range(4):
        blades = tuple(combinations(range(3), k))
        minors = {(left, right): matrix.extract(left, right).det()
                  for left in blades for right in blades}
        assert affine_coefficients(grade_part(exp_green, k).value) == {
            key: value for key, value in minors.items() if value
        }
print("All affine minors checked for both four-vertex paths")
```

## Attaching a vertex

Attach a vertex to the weighted triangle. Check the three contributions by the new vertex degree, the determinant, and the spanning-tree weight.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Greenian Coefficients and Vertex Variations#Attachment examples|Related section of the note]].

```python
triangle = network(tuple("abc"), (("a", "b", 2), ("b", "c", 3), ("a", "c", 5)))
attachments = (7, 11, 13)
attached = network(tuple("abcp"), triangle.edges + tuple(
    (a, "p", weight) for a, weight in zip(triangle.context.labels, attachments)
))
base_tau = spanning_tree_weight(triangle).value
ta, tb, tc = attachments
terms = (base_tau * sum(attachments), 2*(ta + tb)*tc + 3*(tb + tc)*ta + 5*(ta + tc)*tb,
         ta * tb * tc)
determinant = Matrix(laplacian(attached).value.values)[:3, :3].det()
assert terms == (961, 2072, 1001)
assert sum(terms) == determinant == spanning_tree_weight(attached).value == 4034
print("Attachment contributions by degree:", terms, "| tau =", determinant)
```

## A complete graph and a star

For the complete graph and star, sum the rooted coefficients of signed forests by grade and check the top-form normalization.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Greenian Exponentials of Standard Graphs#The complete graph|Related section of the note]].

```python
complete = network(labels, tuple((a, b, 1) for a, b in combinations(labels, 2)))
star = network(labels, (("a", "b", 1), ("a", "c", 1), ("a", "d", 1)))
for net, coefficients in ((complete, (1, Fraction(3, 4), Fraction(3, 16), Fraction(1, 64))),
                          (star, (1, Fraction(9, 4), Fraction(3, 2), Fraction(1, 4)))):
    G = Matrix(green(net).value.values)
    gamma_matrix = zeros(4)
    for i, j in indices:
        gamma_matrix[i, j] = gamma_matrix[j, i] = -G[i, j]
    forests = vertex_toponome(signed_forest_toponome(gamma_matrix))
    sums = tuple(sum(value for kind, value in forests.items() if sum(kind) == k) for k in range(4))
    assert sums == coefficients
    assert spanning_coefficient(exponential(net, greenian_form)).value == coefficients[-1] / 4
print("K₄ and the star: vertex coefficients and top-form normalization agree")
```

## Potentials of differences, cuts, and boundaries

For a difference, cut, triangle boundary, and top form, compute Greenian-exponential potentials with a common normalization.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/The Greenian Metric and Potentials#Examples and the top form|Related section of the note]].

```python
forms = (
    partition_form(unit_path.context, (("a", "b"),)).value,
    cut_partition_form(unit_path.context, (("a", "b"), ("c", "d"))).value,
    partition_form(unit_path.context, (("a", "b", "c"),)).value,
    top,
)
unit_sigma = spanning_coefficient(unit_N).value
normalized = tuple(potential(unit_N, form).value / unit_sigma for form in forms)
assert normalized == (5, 1, 14, 16)
print("P₄ Greenian potentials: difference, cut, triangle, top =", normalized)
```

## A cut identity

Compare the sum of three cut squares with the sum of four centered vertex squares. Then compare their dual images.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Symmetric Identities of the Greenian#Symmetric sums of cuts|Related section of the note]].

```python
def cut_form(side):
    complement = tuple(vertex for vertex in labels if vertex not in side)
    return cut_partition_form(unit_path.context, (tuple(side), complement)).value


left = sum((cut_form(side) for side in ("ab", "ac", "ad")), start=0 * top)
right = sum((cut_form((vertex,)) for vertex in labels), start=0 * top)
assert equivalent(left, right).value
assert dual_coefficients(left, top) == dual_coefficients(right, top)
print("Three cuts equal the sum of four centered vertex squares")
```

## Toponomes of a dual pair

Check the full signed toponome of the path, reversal of the vertex coefficients, and the Greenian determinant.

[[en/Resistance Geometry and Duality/Greenian and polyform duality/Toponomes of the Greenian Exponential and Dual Pairs#Examples of dual pairs|Related section of the note]].

```python
assert signed == {
    (): 1, (1,): Fraction(5, 4), (2,): Fraction(3, 16),
    (1, 1): Fraction(15, 64), (3,): Fraction(1, 16),
}
rooted = vertex_toponome(signed)
p_green = tuple(sum(v for kind, v in rooted.items() if sum(kind) == k) for k in range(4))
p_laplacian = laplacian_polynomial(unit_path)
assert p_green == tuple(value / p_laplacian[-1] for value in reversed(p_laplacian))
t = symbols("t")
assert expand((eye(4) + t * Matrix(green(unit_path).value.values)).det()) == sum(
    value * t**k for k, value in enumerate(p_green)
)
print("Dual P₄ vertex coefficients:", p_laplacian, "→", p_green)
```
