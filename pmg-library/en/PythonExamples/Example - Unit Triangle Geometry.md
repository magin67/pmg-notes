---
title: "Example: Unit Triangle Geometry"
date: 2026-10-29
updated: 2026-11-10
revision: 4
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: python-unit-triangle-geometry
lang: en
description: "Inner products, quadratic boundary norm, and area of the resistance triangle of K3."
order: 3
aliases:
  - "en/PythonExamples/Unit Triangle Geometry in Python"
---

This example reproduces the resistance triangle of $K_3$ from [[From Lengths to Areas and Volumes]] and [[Metric of Higher-Grade Objects]]. All three conductances equal one. This does not mean unit geometric sides: pair resistances are $2/3$, and the resistance triangle has side length $\sqrt{2/3}$.

[[ru/PythonExamples/Пример - Геометрия единичного треугольника|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


This example was checked with `polyform_algebra 0.9.0`. Environment setup: [[Installing the Library and Running Examples]]. Run the Python cells in order.

![[images/Vectors of the resistance triangle.svg]]

## Constructing the metric

First define the vertices and three unit conductances.

```python
from math import sqrt
import numpy as np
from polyform_algebra import Point, quForm

a, b, c = Point.create_list("abc")
f_ab = quForm([(a, b)])
f_ac = quForm([(a, c)])
f_bc = quForm([(b, c)])
metric = (f_ab + f_ac + f_bc).exp()
u, v, w = b-a, c-a, c-b
```

## Inner products and orientation

The code uses $u=b-a$, $v=c-a$, and $w=c-b=v-u$. The `@` operator constructs a scalar polyform; `metric.norm` gives its numerical evaluation. With these orientations,

$$
u^2=v^2=w^2=\frac23,\qquad
u\cdot v=\frac13,\qquad
u\cdot w=-\frac13,\qquad
v\cdot w=\frac13
$$

$$
\mathbf G(u,v)=
\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad
\det\mathbf G=\frac13
$$
Vectors $u,v$ share their starting vertex and form a $60^\circ$ angle. Vectors $u,w$ follow consecutive sides; as free vectors they form a $120^\circ$ angle, so their inner product is negative. Replacing $u$ with $-u$ reverses the sign of $u\cdot v$ while preserving $u^2$.

```python
# @ creates a scalar polyform; norm evaluates it in the graph metric.
uv = metric.norm(u @ v)
gram = np.array([
    [metric.norm(u @ u), uv],
    [metric.norm(v @ u), metric.norm(v @ v)],
])
print("u dot v =", uv)
print("u dot w =", metric.norm(u @ w))
print("Gram matrix =", gram)
print("Gram determinant =", np.linalg.det(gram))

```

## Boundary and area

The triangle boundary has grade 2. Its quadratic form is `quForm([(a, b, c)])`. Under the PMG convention, the norm is a quadratic quantity:

$$
X=(abc)=uv,\qquad X^2=\det\mathbf G=\frac13
$$

$$
\sqrt{X^2}=\frac1{\sqrt3},\qquad
S^2=\frac{X^2}{4}=\frac1{12},\qquad
S=\frac{\sqrt{X^2}}2=\frac{\sqrt3}{6}
$$
The boundary's linear norm equals the area of the parallelogram on $u,v$. The triangle has half that area. Dividing the quadratic norm by 4 therefore gives the squared area, not the area itself.

| Quantity | Exact value |
|---|---:|
| Spanning-tree coefficient $\tau$ | $3$ |
| Squared length of each side | $2/3$ |
| Quadratic boundary norm $X^2$ | $1/3$ |
| Linear boundary norm | $1/\sqrt3$ |
| Squared area $S^2$ | $1/12$ |
| Area $S$ | $\sqrt3/6\approx0.288675$ |

The grade-two boundary is not evaluated through `X @ X` here: its supported quadratic form can be evaluated without higher-grade polarization.

```python
# Use the quadratic boundary form directly; no higher-grade @ is required.
boundary_norm = metric.norm(quForm([(a, b, c)]))
area_squared = boundary_norm / 4
area = sqrt(area_squared)
print("boundary norm =", boundary_norm)
print("area squared =", area_squared)
print("area =", area)
```

## Why norms cannot simply be multiplied

The product $f_{ab}f_{ac}$ is the quadratic form of the triangle boundary. Its metric evaluation differs from the product of the evaluations:

$$
P_M(f_{ab}f_{ac})=\frac13
\ne P_M(f_{ab})P_M(f_{ac})=\frac49
$$
The Gram determinant subtracts $(u\cdot v)^2=1/9$. The full program prints both results as `product_form_norm` and `product_of_norms`.

## Two boundaries and the volume of a tetrahedron

Take the complete graph $K_4$ on vertices $a,b,c,d$ with unit conductances. Its resistance simplex is a regular tetrahedron. The boundaries $(abc)$ and $(abd)$ share the edge $(ab)$. For $u=(ab)$, $v=(ac)$, and $w=(ad)$, each squared norm is $1/2$ and the inner product of two different vectors is $1/4$. The cross Gram determinant gives

$$
(abc)\cdot(abd)=
\det\begin{pmatrix}1/2&1/4\\1/4&1/4\end{pmatrix}
=\frac1{16}.
$$

The code uses coefficients of formal vertices in the order $a,b,c,d$. For example, $u=b-a$ has coordinates $(-1,1,0,0)$. The package computes inner products in the resistance metric of the graph.

As a check, use polarization. The difference $(abc)-(abd)$ equals $(ab)(dc)$, so subtract its squared norm from the sum of the two squared norms and divide by two.

```python
from fractions import Fraction
from itertools import combinations
from polyform_algebra.core import (
    blade_inner_product, coordinates, network, simplex_volume_squared,
)

vertices = ("a", "b", "c", "d")
tetrahedron = network(vertices, [(i, j, 1) for i, j in combinations(vertices, 2)])
u = coordinates(tetrahedron.context, (-1, 1, 0, 0))
v = coordinates(tetrahedron.context, (-1, 0, 1, 0))
w = coordinates(tetrahedron.context, (-1, 0, 0, 1))

mixed = blade_inner_product(tetrahedron, (u, v), (u, w)).value
reversed_mixed = blade_inner_product(tetrahedron, (v, u), (u, w)).value
difference = coordinates(tetrahedron.context, (0, 0, 1, -1))
polarized = (
    blade_inner_product(tetrahedron, (u, v), (u, v)).value
    + blade_inner_product(tetrahedron, (u, w), (u, w)).value
    - blade_inner_product(tetrahedron, (u, difference), (u, difference)).value
) / 2
volume_squared = simplex_volume_squared(tetrahedron, vertices).value
print("(abc) · (abd) =", mixed)
print("(acb) · (abd) =", reversed_mixed)
print("V² =", volume_squared)

assert mixed == Fraction(1, 16)
assert reversed_mixed == -mixed
assert polarized == mixed
assert volume_squared == Fraction(1, 576)
```

Swapping $b,c$ reverses the first boundary and changes the sign of the inner product. The Gram matrix of the three vectors has determinant $1/16$. Thus the squared volume is $(1/16)/(3!)^2=1/576$, and the volume is $1/24$.

## Independent checks

Tests compare the results with the inverse of the grounded Laplacian $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ and explicit coordinates of an equilateral triangle of side $\sqrt{2/3}$. Area is checked using an edge-coordinate determinant and the formula $S^2=3\ell^4/16$. All six vertex permutations preserve the quadratic boundary norm and Gram determinant.



## Try changing the input

Replace $u$ with $-u$. Check the sign change in the mixed inner product and the unchanged area.

These numerical checks concern this example and do not replace a general proof.
