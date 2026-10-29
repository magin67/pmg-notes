---
title: "Triangle Coupling Variations in Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-triangle-coupling-variations
lang: en
description: "Implementing one-edge and two-edge strengthening of a triangle through factors of the metric polyform."
order: 1
---

This note reproduces the triangle-strengthening examples from [[Variation of a Single Edge#Example: strengthening an edge of a triangle|Variation of a Single Edge]] and [[Varying several couplings together#Example: strengthening two couplings of a triangle|Varying Several Couplings Together]]. The main calculation uses the algebra of quadratic forms; matrix formulas provide comparison checks.

[[ru/PythonExamples/Вариации связей треугольника на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

## Code and execution

Tested Python revision: [`76c433d`](https://github.com/magin67/polyform_algebra/commit/76c433de082b348caca5c0afdcb5c372361aa9f2). Complete programs: [one edge](https://github.com/magin67/polyform_algebra/blob/76c433de082b348caca5c0afdcb5c372361aa9f2/examples/introductory/note06_single_edge.py), [two edges](https://github.com/magin67/polyform_algebra/blob/76c433de082b348caca5c0afdcb5c372361aa9f2/examples/introductory/note07_two_edges.py). To prepare a separate checkout and run the examples in PowerShell:

```powershell
git clone https://github.com/magin67/polyform_algebra.git polyform-examples
cd polyform-examples
git checkout 76c433de082b348caca5c0afdcb5c372361aa9f2
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m examples.introductory.note06_single_edge
.\.venv\Scripts\python.exe -m examples.introductory.note07_two_edges
.\.venv\Scripts\python.exe -m pytest tests/introductory -q
```

Activation is optional. On Linux/macOS, replace the interpreter path with `.venv/bin/python`. Run the full test suite with `python -m pytest -q` using the selected environment. The code revision is fixed, but these commands do not pin dependency versions.

## Initial objects

Let $a_1,a_2,a_3$ be the vertices, $a_{ij}=a_j-a_i$, and $f_{ij}=[a_{ij}]^2$. All three conductances of the initial $K_3$ equal one. Following [[Laplacian Exponential]], set

$$
L=f_{12}+f_{13}+f_{23},\qquad M=\exp L
$$

```python
from polyform_algebra import Point, Polyform, quForm

a, b, c = Point.create_list(["1", "2", "3"])
f12 = quForm([(a, b)])
f13 = quForm([(a, c)])
f23 = quForm([(b, c)])
laplacian = f12 + f13 + f23
metric = laplacian.exp()

tau = metric.potential(quForm.one())
r12 = metric.norm(f12)
coupling = metric.norm((b-a) @ (c-a))
```

Here `a, b, c` denote $a_1,a_2,a_3$. The `potential` method extracts the coefficient of the fixed spanning-tree form after multiplication, while `norm` divides it by $\tau(M)$:

$$
u_M(f)=\tau(Mf),\qquad P_M(f)=\frac{\tau(Mf)}{\tau(M)}
$$

Thus `tau` is $3$, `r12` is $2/3$, and `coupling` is $1/3$. The `@` operator first constructs a scalar polyform: half the polar form for supported grade-one arguments. Evaluation through `norm` gives the numerical inner product. A polyform potential is distinct from the electrical potential at a vertex.

## Strengthening one coupling

Increase $c_{12}$ from $1$ to $2$, so $\delta=1$. Since $f_{12}f_{12}=0$,

$$
\exp(L+\delta f_{12})=M(e+\delta f_{12})
$$

```python
delta = 1
after_one = metric * (Polyform.one() + delta*f12)
assert after_one.is_equivalent((laplacian + delta*f12).exp())

tau_one = after_one.potential(quForm.one())
r12_one = after_one.norm(f12)
r13_one = after_one.norm(f13)
probability12 = (1 + delta)*r12_one
forest13 = after_one.potential(f13)
```

| Quantity | Before | After |
|---|---:|---:|
| $\tau$ | $3$ | $5$ |
| $R_{12}$ | $2/3$ | $2/5$ |
| $R_{13}$ | $2/3$ | $3/5$ |
| $R_{23}$ | $2/3$ | $3/5$ |
| $\Pr(12\in T)$ | $2/3$ | $4/5$ |
| Weight of 2-forests separating 1 and 3 | $2$ | $3$ |

The edge probability is $c_{12}R_{12}$, so the updated conductance $2$ must be used after the change. The unnormalized potential `after_one.potential(f13)` equals the weight of the corresponding separating spanning 2-forests.

The program also compares the results with the formulas in the theoretical note. With $g=a_{12}\cdot a_{13}=1/3$,

$$
\tau'=\tau(1+\delta R_{12}),\qquad
R'_{13}=R_{13}-\frac{\delta g^2}{1+\delta R_{12}}
$$

The forest-weight increment is $\delta\tau(R_{12}R_{13}-g^2)=1$.

## Strengthening two couplings

Now increase both $c_{12}$ and $c_{13}$ from $1$ to $2$. Use the initial metric $M$ and two factors:

```python
after_two = metric * (Polyform.one() + f12) * (Polyform.one() + f13)
assert after_two.is_equivalent((laplacian + f12 + f13).exp())
assert after_two.is_equivalent(
    metric * (Polyform.one() + f13) * (Polyform.one() + f12)
)

tau_two = after_two.potential(quForm.one())
r23_two = after_two.norm(f23)
mixed_coefficient = metric.potential(f12*f13)
```

Orient both selected vectors away from vertex $1$. For the measured vector $a_{23}$, the Gram matrix and interaction column are

$$
\mathbf G=
\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},
\qquad
q=\begin{pmatrix}-1/3\\1/3\end{pmatrix}
$$

| Quantity | Result |
|---|---:|
| $\tau$ after the first change | $5$ |
| $R_{13}$ after the first change | $3/5$ |
| $\tau$ after both changes | $8$ |
| $R_{23}$ after both changes | $1/2$ |
| $\det(I_2+\mathbf G)$ | $8/3$ |
| Coefficient of $\delta_1\delta_2$ in $\tau'$ | $1$ |
| $\Pr(12,13\in T)$ in the initial network | $1/3$ |

The interaction coefficient is computed directly as `metric.potential(f12*f13)` and equals $\tau\det\mathbf G=1$. In general, evaluating a product of forms does not give the product of their evaluations.

The complete program checks

$$
\tau'=\tau\det(I_2+\mathbf G),\qquad
R'_{23}=R_{23}-q^{\mathsf T}(I_2+\mathbf G)^{-1}q
$$

The inverse action is computed with `numpy.linalg.solve`. The sequential calculation uses the updated metric after the first step: $5(1+3/5)=8$.

## Independent checks and status

The [example tests](https://github.com/magin67/polyform_algebra/blob/76c433de082b348caca5c0afdcb5c372361aa9f2/tests/introductory/test_triangle_variations.py) check the values in the notes, orientation signs, factor order, and complete recomputation of the exponential. In addition, the Laplacian matrix is constructed directly from the conductances: a cofactor gives $\tau$, while solving the current equations with vertex $3$ grounded gives $R_{23}$. This check does not use polyform products.

**Status: computed directly** for the two stated changes of $K_3$. At the tested revision, 223 tests passed, including example execution and import checks, both in the checkout and with the installed package outside it. Validation used Python 3.12; it is neither a proof of the general formulas nor a check of every declared Python version.

The examples do not introduce a general variation API or handle arbitrary bridge deletion. The public software interface remains restricted to supported quadratic forms. General formal definitions appear in [[Core specification]], and evaluation conventions in [[PMG terminology]].
