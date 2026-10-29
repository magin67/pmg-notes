---
title: "Unit Triangle Geometry in Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-unit-triangle-geometry
lang: en
description: "Inner products, quadratic boundary norm, and area of the resistance triangle of K3."
order: 3
---

This example reproduces the resistance triangle of $K_3$ from [[From Lengths to Areas and Volumes]] and [[Metric of Higher-Grade Objects]]. All three conductances equal one. This does not mean unit geometric sides: pair resistances are $2/3$, and the resistance triangle has side length $\sqrt{2/3}$.

[[ru/PythonExamples/Геометрия единичного треугольника на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

## Code and execution

The [program](https://github.com/magin67/polyform_algebra/blob/a678839a1eb3aab467a1b043bd1d0b9c7b5716ad/examples/introductory/note05_triangle_geometry.py) and [tests](https://github.com/magin67/polyform_algebra/blob/a678839a1eb3aab467a1b043bd1d0b9c7b5716ad/tests/introductory/test_triangle_geometry.py) were checked at revision `a678839`. Follow [[Installing the Library and Running Examples|the setup guide]]. In an existing separate examples checkout, run `git fetch origin`, then `git checkout a678839a1eb3aab467a1b043bd1d0b9c7b5716ad`: earlier revisions may not contain this module.

From the repository root, using the selected environment's interpreter:

```powershell
python -m examples.introductory.note05_triangle_geometry
python -m pytest tests/introductory/test_triangle_geometry.py -q
```

On Windows you can replace `python` with `.\.venv\Scripts\python.exe`; on Linux/macOS use `.venv/bin/python`. In Colab, follow the source-cloning route in the setup guide and run:

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "examples.introductory.note05_triangle_geometry"],
    check=True,
)
```

After installing the package, the following standalone fragment can run in a file or a notebook cell:

```python
from math import sqrt
import numpy as np
from polyform_algebra import Point, quForm

a, b, c = Point.create_list(["1", "2", "3"])
f12 = quForm([(a, b)])
f13 = quForm([(a, c)])
f23 = quForm([(b, c)])
metric = (f12 + f13 + f23).exp()
u, v, w = b-a, c-a, c-b

# @ creates a scalar polyform; norm evaluates it in the graph metric.
uv = metric.norm(u @ v)
gram = np.array([
    [metric.norm(u @ u), uv],
    [metric.norm(v @ u), metric.norm(v @ v)],
])
# Use the quadratic boundary form directly; no higher-grade @ is required.
boundary_norm = metric.norm(quForm([(a, b, c)]))
area_squared = boundary_norm / 4
area = sqrt(area_squared)
print("u dot v =", uv)
print("u dot w =", metric.norm(u @ w))
print("Gram matrix =", gram)
print("Gram determinant =", np.linalg.det(gram))
print("boundary norm =", boundary_norm)
print("area squared =", area_squared)
print("area =", area)
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

## Why norms cannot simply be multiplied

The product $f_{12}f_{13}$ is the quadratic form of the triangle boundary. Its metric evaluation differs from the product of the evaluations:

$$
P_M(f_{12}f_{13})=\frac13
\ne P_M(f_{12})P_M(f_{13})=\frac49
$$
The Gram determinant subtracts $(u\cdot v)^2=1/9$. The full program prints both results as `product_form_norm` and `product_of_norms`.

## Independent checks

Tests compare the results with the inverse of the grounded Laplacian $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ and explicit coordinates of an equilateral triangle of side $\sqrt{2/3}$. Area is checked using an edge-coordinate determinant and the formula $S^2=3\ell^4/16$. All six vertex permutations preserve the quadratic boundary norm and Gram determinant.

**Status: computed directly.** All 238 project tests passed on Python 3.12, including eight checks for this example and general execution and import checks. The note's code fragments were checked locally; a hosted Google Colab session was not separately run. The quadratic algebra core was unchanged.
