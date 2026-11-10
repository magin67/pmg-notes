---
title: "Example: Triangle Coupling Variations"
date: 2026-10-29
updated: 2026-11-10
revision: 6
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
translation_key: python-triangle-coupling-variations
lang: en
description: "Implementing one-edge and two-edge strengthening of a triangle through factors of the metric polyform."
order: 4
aliases:
  - "en/PythonExamples/Triangle Coupling Variations in Python"
---

This note reproduces the triangle-strengthening examples from [[Variation of a Single Edge#Example: strengthening an edge of a triangle|Variation of a Single Edge]] and [[Varying several couplings together#Example: strengthening two couplings of a triangle|Varying Several Couplings Together]]. The main calculation uses the algebra of quadratic forms; matrix formulas provide comparison checks.

[[ru/PythonExamples/Пример - Вариации связей треугольника|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


This example was checked with `polyform_algebra 0.9.0`. Environment setup: [[Installing the Library and Running Examples]]. Run the Python cells in order.

![[images/Strengthening triangle couplings.svg]]

## Initial objects

Let $a,b,c$ be the vertices; for a pair $x,y$, write $f_{xy}=[y-x]^2$. All three conductances of the initial $K_3$ equal one. Following [[Laplacian Exponential]], set

$$
L=f_{ab}+f_{ac}+f_{bc},\qquad M=\exp L
$$

```python
from polyform_algebra import Point, Polyform, quForm

a, b, c = Point.create_list("abc")
f_ab = quForm([(a, b)])
f_ac = quForm([(a, c)])
f_bc = quForm([(b, c)])
laplacian = f_ab + f_ac + f_bc
metric = laplacian.exp()

tau = metric.potential(quForm.one())
r_ab = metric.norm(f_ab)
coupling = metric.norm((b-a) @ (c-a))
```

The `potential` method extracts the coefficient of the fixed spanning-tree form after multiplication, while `norm` divides it by $\tau(M)$:

$$
u_M(f)=\tau(Mf),\qquad P_M(f)=\frac{\tau(Mf)}{\tau(M)}
$$

Thus `tau` is $3$, `r_ab` is $2/3$, and `coupling` is $1/3$. The `@` operator first constructs a scalar polyform: half the polar form for supported grade-one arguments. Evaluation through `norm` gives the numerical inner product. A polyform potential is distinct from the electrical potential at a vertex.

## Strengthening one coupling

Increase $c_{ab}$ from $1$ to $2$, so $\delta=1$. Since $f_{ab}f_{ab}=0$,

$$
\exp(L+\delta f_{ab})=M(e+\delta f_{ab})
$$

```python
delta = 1
after_one = metric * (Polyform.one() + delta*f_ab)
assert after_one.is_equivalent((laplacian + delta*f_ab).exp())

tau_one = after_one.potential(quForm.one())
r_ab_one = after_one.norm(f_ab)
r_ac_one = after_one.norm(f_ac)
probability_ab = (1 + delta)*r_ab_one
forest_ac = after_one.potential(f_ac)
```

| Quantity | Before | After |
|---|---:|---:|
| $\tau$ | $3$ | $5$ |
| $R_{ab}$ | $2/3$ | $2/5$ |
| $R_{ac}$ | $2/3$ | $3/5$ |
| $R_{bc}$ | $2/3$ | $3/5$ |
| $\Pr(ab\in T)$ | $2/3$ | $4/5$ |
| Weight of 2-forests separating a and c | $2$ | $3$ |

The edge probability is $c_{ab}R_{ab}$, so the updated conductance $2$ must be used after the change. The unnormalized potential `after_one.potential(f_ac)` equals the weight of the corresponding separating spanning 2-forests.

The program also compares the results with the formulas in the theoretical note. With $g=(ab)\cdot (ac)=1/3$,

$$
\tau'=\tau(1+\delta R_{ab}),\qquad
R'_{ac}=R_{ac}-\frac{\delta g^2}{1+\delta R_{ab}}
$$

The forest-weight increment is $\delta\tau(R_{ab}R_{ac}-g^2)=1$.

## Strengthening two couplings

Now increase both conductances $c_{ab},c_{ac}$ from $1$ to $2$. Use the initial metric $M$ and two factors:

```python
after_two = metric * (Polyform.one() + f_ab) * (Polyform.one() + f_ac)
assert after_two.is_equivalent((laplacian + f_ab + f_ac).exp())
assert after_two.is_equivalent(
    metric * (Polyform.one() + f_ac) * (Polyform.one() + f_ab)
)

tau_two = after_two.potential(quForm.one())
r_bc_two = after_two.norm(f_bc)
mixed_coefficient = metric.potential(f_ab*f_ac)
```

Orient both selected vectors away from vertex $a$. For the measured vector $(bc)$, the Gram matrix and interaction column are

$$
\mathbf G=
\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},
\qquad
q=\begin{pmatrix}-1/3\\1/3\end{pmatrix}
$$

| Quantity | Result |
|---|---:|
| $\tau$ after the first change | $5$ |
| $R_{ac}$ after the first change | $3/5$ |
| $\tau$ after both changes | $8$ |
| $R_{bc}$ after both changes | $1/2$ |
| $\det(I_2+\mathbf G)$ | $8/3$ |
| Coefficient of $\delta_1\delta_2$ in $\tau'$ | $1$ |
| $\Pr(ab,ac\in T)$ in the initial network | $1/3$ |

The interaction coefficient is computed directly as `metric.potential(f_ab*f_ac)` and equals $\tau\det\mathbf G=1$. In general, evaluating a product of forms does not give the product of their evaluations.

The complete program checks

$$
\tau'=\tau\det(I_2+\mathbf G),\qquad
R'_{bc}=R_{bc}-q^{\mathsf T}(I_2+\mathbf G)^{-1}q
$$

The inverse action is computed with `numpy.linalg.solve`. The sequential calculation uses the updated metric after the first step: $5(1+3/5)=8$.

## Independent checks and status

The [example tests](https://github.com/magin67/polyform_algebra/blob/v0.9.0/tests/introductory/test_triangle_variations.py) check the values in the notes, orientation signs, factor order, and complete recomputation of the exponential. In addition, the Laplacian matrix is constructed directly from the conductances: a cofactor gives $\tau$, while solving the current equations with vertex $c$ grounded gives $R_{bc}$. This check does not use polyform products.



Here, coupling changes are expressed through products of edge factors. General formal definitions appear in [[Core specification]], and evaluation conventions in [[PMG terminology]].

## Try changing the input

Strengthen an edge by $\delta=2$ instead of 1. Compare the factor update with a newly computed exponential.

These numerical checks concern this example and do not replace a general proof.
