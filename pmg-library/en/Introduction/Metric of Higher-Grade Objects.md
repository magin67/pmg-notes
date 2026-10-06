---
title: Metric of Higher-Grade Objects
date: 2026-10-06
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: higher-grade-object-metric
lang: en
description: How the scalar product extends to higher-grade boundaries, why the mixed Gram determinant gives their metric value, and how this metric is related to the exterior product of forms.
---

The note [[Basic Objects and Operations of Polyform Algebra]] introduced points, simplices, boundaries, forms, and the exterior product. The next question concerns the measurement and comparison of boundaries of different grades.

A simplex and its boundary have different grades. The oriented segment $[ab]=a\wedge b$ has grade $2$, while its boundary $(ab)=b-a$ has grade $1$. The oriented triangle $[abc]=a\wedge b\wedge c$ has grade $3$, while its boundary $(abc)$ has grade $2$.

These boundaries arise from exterior products of graph vectors. Their metric values are expressed by Gram determinants.

## Simplex, boundary, and grade

For the first few grades one obtains the following table.

| Geometric object | Simplex | Simplex grade | Boundary | Expanded boundary form | Boundary grade |
|---|---|---:|---|---|---:|
| point | $a$ | 1 | $(a)$ | $1$ | 0 |
| oriented segment | $[ab]=a\wedge b$ | 2 | $(ab)$ | $b-a$ | 1 |
| oriented triangle | $[abc]=a\wedge b\wedge c$ | 3 | $(abc)$ | $[ab]-[ac]+[bc]$ | 2 |
| oriented tetrahedron | $[abcd]=a\wedge b\wedge c\wedge d$ | 4 | $(abcd)$ | $[bcd]-[acd]+[abd]-[abc]$ | 3 |

The boundary of a point is taken to be the scalar $1$, so scalars have grade $0$.

For every simplex,

$$
\operatorname{gr}\partial X=\operatorname{gr}X-1 \tag{1}
$$

The geometric dimension of a simplex coincides with the grade of its boundary.

For graph vectors one has the fusion rule for adjacent boundaries:

$$
(ab)(bc)=(abc) \tag{2}
$$

The same boundary value is obtained from two vectors with a common initial point:

$$
(ab)(ac)=(abc) \tag{3}
$$

The right-hand side of formulas (2) and (3) denotes the boundary of the triangle, not the simplex $[abc]$ itself.

> [!remark] A simplex and its boundary
> The exterior product of points $a\wedge b\wedge c=[abc]$ gives an oriented triangle of grade $3$.
>
> The exterior product of two adjacent vectors $(ab)(ac)=(abc)$ gives its boundary of grade $2$.
>
> These objects are related by the boundary operator, but they are not the same object.

## Scalar product of boundaries of the same grade

Let

$$
X=u_1\wedge\cdots\wedge u_k,
\qquad
Y=v_1\wedge\cdots\wedge v_k
$$

where the $u_i$ and $v_i$ are vectors of grade $1$. Then $X$ and $Y$ have grade $k$. If the original vectors are boundaries, then their exterior products are boundaries as well.

> [!definition] Mixed Gram determinant
> The scalar product of simple objects of the same grade is defined by
>
> $$
> X\cdot Y=
> \det\bigl(u_i\cdot v_j\bigr)_{i,j=1}^k \tag{4}
> $$

For $k=1$, formula (4) is the ordinary scalar product of vectors.

For $X=Y$ one obtains

$$
X^2=
\det\bigl(u_i\cdot u_j\bigr)_{i,j=1}^k \tag{5}
$$

If the vectors $u_1,\ldots,u_k$ are linearly dependent, then $X=0$ and the Gram determinant vanishes. For linearly independent vectors, the quantity $X^2$ equals the square of the $k$-dimensional volume of the parallelepiped spanned by these vectors.

The note [[From Lengths to Areas and Volumes]] introduced the same quantity geometrically. Formulas (4) and (5) identify the exterior object measured by the Gram determinant.

## Two triangles with a common side

Consider the oriented triangles $[abc]$ and $[abd]$ with a common side $[ab]$. Their grade-$2$ boundaries are

$$
X=(abc)=(ab)(ac),
\qquad
Y=(abd)=(ab)(ad) \tag{6}
$$

![[Metric of Higher-Grade Objects - two triangles.svg]]

By formula (4),

$$
(abc)\cdot(abd)=
\det
\begin{pmatrix}
(ab)^2 & (ab)\cdot(ad) \\
(ac)\cdot(ab) & (ac)\cdot(ad)
\end{pmatrix} \tag{7}
$$

The three points $a,b,c$ determine two vectors $(ab)$ and $(ac)$ with common initial point $a$. The parallelogram spanned by these vectors has area square

$$
S_{\parallel,abc}^2=(abc)^2 \tag{8}
$$

The triangle $[abc]$ occupies one half of this parallelogram, hence

$$
S_{abc}^2=\frac14(abc)^2 \tag{9}
$$

or equivalently,

$$
(abc)^2=4S_{abc}^2 \tag{10}
$$

Formula (10) refers to the metric value of the boundary $(abc)$. The simplex $[abc]$ itself has grade $3$.

Similarly, the four points $a,b,c,d$ determine the three vectors $(ab)$, $(ac)$, $(ad)$ and the parallelepiped spanned by them. For the boundary of the tetrahedron,

$$
(abcd)=(ab)(ac)(ad) \tag{11}
$$

its square equals the square of the volume of this parallelepiped:

$$
(abcd)^2=V_{\parallel,abcd}^2 \tag{12}
$$

The volume of the tetrahedron $[abcd]$ is one sixth of the volume of the parallelepiped, so

$$
V_{abcd}^2=\frac1{36}(abcd)^2 \tag{13}
$$

> [!remark] Orientation and orthogonality
> For two nondegenerate triangles in the same plane, the sign of $(abc)\cdot(abd)$ is determined by their relative orientation. If the points $c$ and $d$ lie on the same side of the line $ab$, the sign is positive; if they lie on opposite sides, the sign is negative.
>
> In higher-dimensional space, nonzero grade-$2$ boundaries can be orthogonal. If the planes of the triangles $[abc]$ and $[abd]$ are mutually orthogonal along the common side $[ab]$, then
>
> $$
> (abc)\cdot(abd)=0 \tag{14}
> $$

A second-grade scalar product measures the mutual position of oriented two-dimensional boundary objects in the same way that the ordinary scalar product measures the mutual position of vectors.

## Bilinear and quadratic forms

The numerical scalar product and the formal bilinear form should be distinguished.

- $X\cdot Y$ is the numerical scalar product of objects of the same grade;
- $X^2=X\cdot X$ is the square of the metric value of an object;
- $[X,Y]$ is a bilinear form;
- $[X]^2=[X,X]$ is a quadratic form;
- $[Y,X]$ is the transposed form.

The polar form is defined by

$$
\{X,Y\}=[X,Y]+[Y,X] \tag{15}
$$

The corresponding symmetric bilinear form is

$$
\frac12\{X,Y\} \tag{16}
$$

The polarization identity has the form

$$
[X+Y]^2=[X]^2+\{X,Y\}+[Y]^2 \tag{17}
$$

> [!remark] Numerical value and form
> The expressions $X^2$ and $[X]^2$ denote different objects.
>
> $X^2$ is a numerical metric value.
>
> $[X]^2$ is a quadratic form. A numerical value appears only after a metric has been assigned and the form has been evaluated.

## Exterior product of forms and its metric meaning

For bilinear forms, the exterior product is defined through the exterior product of the arguments:

$$
[X,Y]\wedge[A,B]=[X\wedge A,Y\wedge B] \tag{18}
$$

No other product of forms will be used, so the sign $\wedge$ between forms may be omitted:

$$
[X,Y][A,B]=[X\wedge A,Y\wedge B] \tag{19}
$$

For quadratic forms one gets

$$
[X]^2\wedge[A]^2=[X\wedge A]^2 \tag{20}
$$

and in shortened notation,

$$
[X]^2[A]^2=[X\wedge A]^2 \tag{21}
$$

For example,

$$
[(ab)]^2[(ac)]^2=[(abc)]^2 \tag{22}
$$

The left-hand side of formula (22) consists of two quadratic forms of grade $1$. The right-hand side is one quadratic form of grade $2$ with argument $(abc)$.

Its metric value is given by the Gram determinant:

$$
(abc)^2=
\det
\begin{pmatrix}
(ab)^2 & (ab)\cdot(ac) \\
(ac)\cdot(ab) & (ac)^2
\end{pmatrix} \tag{23}
$$

Thus, the exterior product of forms combines first-grade objects into a higher-grade form, while the mixed Gram determinant gives the metric value of its argument.

Such products arise when quadratic edge forms of a graph are multiplied. [[Laplacian Exponential]] collects them across all grades into one polyform.

## Summary

The simplex $[a_0\ldots a_k]$ has grade $k+1$, while its boundary $(a_0\ldots a_k)$ has grade $k$. The boundary of a point is the scalar $1$ of grade $0$.

Exterior products of graph vectors produce higher-grade boundaries. Their scalar product is given by the mixed Gram determinant, and the square of such an object equals the square of the volume of the corresponding parallelepiped.

Bilinear and quadratic forms preserve the same graded structure: their exterior product is defined through the exterior product of their arguments. This connects the algebraic product of forms with metric values of higher-grade boundaries.
