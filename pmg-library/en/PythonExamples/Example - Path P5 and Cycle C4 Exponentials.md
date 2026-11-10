---
title: "Example: Path P5 and Cycle C4 Exponentials"
date: 2026-10-29
updated: 2026-11-10
revision: 3
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: python-path-cycle-exponentials
lang: en
description: "Forest grade components of the P5 and C4 exponentials, spanning-tree coefficients, and effective resistances."
order: 5
aliases:
  - "en/PythonExamples/Path P5 and Cycle C4 Exponentials in Python"
---

This example displays the forms of the Laplacian and its exponential: boundary products, merging components, and grade decomposition. Numerical potentials and resistances are evaluated only after the polyforms have been constructed.

[[ru/PythonExamples/Пример - Экспоненты пути P5 и цикла C4|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

[Open the symbolic notebook in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symbolic-polyforms.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/symbolic-polyforms.ipynb)

Uses `polyform_algebra 0.9.0`; see [[Installing the Library and Running Examples]] for setup. Run the code in order. Vertices use letters; numbers denote coefficients and grades.

![[images/Path and cycle in the forest expansion.svg]]

## Elements and forms

The variable `e` below is a vertex; `unit` is the algebra unit $\mathrm{e}$. The form `f_ab` is $[(ab)]^2$, where $(ab)=b-a$. The package prints this quadratic form as `f[(a, b)]` and the algebra unit as `f[1]`.

```python
from fractions import Fraction
from math import factorial
from polyform_algebra import Point, Polyform, quForm

a, b, c, d, e = Point.create_list("abcde")
f_ab = quForm([(a, b)])
f_bc = quForm([(b, c)])
f_cd = quForm([(c, d)])
f_de = quForm([(d, e)])
f_ad = quForm([(a, d)])
unit = Polyform.one()
print("vertices:", a, b, c, d, e)
print("f_ab =", f_ab)
```

## Multiplication: merging, separate components, and vanishing

$$
[(ab)]^2[(bc)]^2=[(abc)]^2,\qquad [(ab)]^2[(cd)]^2=[(ab)(cd)]^2.
$$

A shared vertex merges the boundaries. Disjoint edges retain two components. A repeated edge or a closed cycle gives a zero product.

```python
merged = f_ab * f_bc
separate = f_ab * f_cd
print("f_ab * f_bc =", merged)
print("f_ab * f_cd =", separate)
print("f_ab * f_ab =", f_ab * f_ab)
print("f_ab * f_bc * f_ad * f_cd =", f_ab * f_bc * f_ad * f_cd)
assert merged.as_polyform().is_equivalent(quForm([(a, b, c)]).as_polyform())
assert separate.as_polyform().is_equivalent(quForm([(a, b), (c, d)]).as_polyform())
assert (f_ab * f_ab).is_zero()
assert (f_ab * f_bc * f_cd * f_ad).is_zero()
```

## Path P5: the full symbolic output

$a-b-c-d-e$. All conductances equal one. `print(M_path)` groups the exponential by grade: `g0` is the unit, `g1` contains edge forms, `g2` contains two-edge products, and so on.

```python
L_path = f_ab + f_bc + f_cd + f_de
M_path = L_path.exp()
print("L_path =", L_path)
print("exp(L_path):")
print(M_path)
```

### How the grades arise

$$
\exp L=\prod_{xy\in E}(\mathrm{e}+f_{xy}),\qquad M_k=\frac{L^k}{k!}.
$$

Each factor adds the alternatives containing the next edge. The following output shows every intermediate polyform, not just its top coefficient.

```python
partial = unit
for edge in (f_ab, f_bc, f_cd, f_de):
    partial = partial * (unit + edge)
    print("Factor:", unit + edge)
    print(partial)
    print()
assert partial.is_equivalent(M_path)
```

## Cycle C4: four trees, one form

$a-b-c-d-a$. Any three edges give the form $[(abcd)]^2$. All four edges form a cycle and give zero. Thus the highest nonzero grade is $4[(abcd)]^2$.

```python
L_cycle = f_ab + f_bc + f_cd + f_ad
M_cycle = L_cycle.exp()
print("L_cycle =", L_cycle)
print("exp(L_cycle):")
print(M_cycle)
```

## Coefficients of forms

Change only conductance $ab$ to $3/2$. Three trees contain this edge and one does not, so their total weight is $3\cdot3/2+1=11/2$. The form remains $[(abcd)]^2$. These coefficients are exact rationals; vertex symbols are not replaced with numeric labels.

```python
L_weighted = Fraction(3, 2) * f_ab + f_bc + f_cd + f_ad
M_weighted = L_weighted.exp()
print(M_weighted)

assert M_weighted.extract_grade(3).is_equivalent(Fraction(11, 2) * quForm([(a, b, c, d)]))
```

## Why the coefficient is four

Deleting any one cycle edge gives one of four trees, all with the form $[(abcd)]^2$. Their sum is $4[(abcd)]^2$, not four distinct forms. Grade 4 vanishes. The highest-grade form of path $P_5$ is $[(abcde)]^2$ with coefficient 1.

## Checks and further reading

The notebook checks the exponential against the product of edge factors and checks $M_k=L^k/k!$ at every grade. A separate final cell demonstrates evaluation into spanning-tree coefficients and resistance. Theory: [[Laplacian Exponential]].

A calculation for one example does not replace a general proof.
