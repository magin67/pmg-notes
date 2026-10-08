---
title: Metric of Higher-Grade Objects
date: 2026-10-06
updated: 2026-10-08
revision: 2
source_revision: 5
status: draft
text_prepared_by: ChatGPT
translation_key: higher-grade-object-metric
lang: en
description: Extension of the inner product to boundaries at each grade. Mixed Gram determinants, squared norms, areas and volumes, and numerical evaluation of forms.
order: "9"
---

In [[Basic Objects and Operations of Polyform Algebra]], boundaries of grade $k$ were identified with the exterior power $\Lambda^kW$ of the space of affine vectors $W$. An inner product on $W$ determines a metric on each of these exterior powers. Objects are compared within the same grade; no inner product between different grades is introduced here.

The original metric on $W$ is assumed to be positive definite. For a graph, this is the resistance metric of a finite connected undirected graph with positive conductances on its existing edges. This note does not define a metric on the entire space of formal vertices $V$.

## A simplex and its boundary

We retain the conventions $\partial a=1$, $\partial1=0$, and parentheses for boundaries.

| Object | Simplex and its grade | Boundary | Boundary grade |
|---|---|---|---:|
| Point | $a$, grade $1$ | $1$ | 0 |
| Oriented segment | $[ab]$, grade $2$ | $(ab)=b-a$ | 1 |
| Oriented triangle | $[abc]$, grade $3$ | $(abc)=[bc]-[ac]+[ab]$ | 2 |
| Oriented tetrahedron | $[abcd]$, grade $4$ | $(abcd)=[bcd]-[acd]+[abd]-[abc]$ | 3 |

A nonzero boundary has grade one less than the original simplex. Its grade equals the geometric dimension of a nondegenerate simplex.

The difference $a_{ij}=a_j-a_i$ is also written as $(a_i a_j)$. The exterior product of consecutive affine vectors gives

$$
(ab)\wedge(bc)=(ab)\wedge(ac)=(abc)
$$

The right-hand side is the triangle boundary of grade $2$, rather than the simplex $[abc]$ of grade $3$. As in the preceding note, the symbol $\wedge$ between exterior objects may be omitted below.

## The inner product within one grade

An exterior object is called simple if it can be represented as a single product of vectors. Let

$$
X=u_1\wedge\cdots\wedge u_k,\qquad
Y=v_1\wedge\cdots\wedge v_k,\qquad u_i,v_i\in W
$$

> [!info] The induced inner product
> **Definition.** For simple objects of grade $k$, set
>
> $$
> X\cdot Y=\det(u_i\cdot v_j)_{i,j=1}^k
> \tag{1}
> $$
>
> The right-hand side is called the mixed Gram determinant. The rule extends to linear combinations of simple objects by bilinearity:
>
> $$
> \left(\sum_\alpha s_\alpha X_\alpha\right)\cdot
> \left(\sum_\beta t_\beta Y_\beta\right)
> =\sum_{\alpha,\beta}s_\alpha t_\beta(X_\alpha\cdot Y_\beta)
> $$

For $k=1$, this is the original metric on $W$. For $k=0$, the inner product of scalars is their ordinary product; in particular, $1\cdot1=1$.

> [!info] Well-definedness and positivity
> **Theorem.** Formula (1) and its bilinear extension define a unique positive definite inner product on $\Lambda^kW$. The result depends on the objects $X,Y$, rather than on the chosen decomposition into exterior products.

> [!note]- Proof
> **Proof.** Choose an orthonormal basis $w_1,\ldots,w_d$ of $W$. The products
>
> $$
> w_{i_1}\wedge\cdots\wedge w_{i_k},\qquad i_1<\cdots<i_k
> $$
>
> form a basis of $\Lambda^kW$. Declare this basis orthonormal. This defines a positive definite inner product on all linear combinations.
>
> If $U$ and $V$ contain the coordinate columns of $u_i$ and $v_i$, then the coordinates of the simple objects $X$ and $Y$ in this exterior basis are the corresponding minors of $U$ and $V$. By the Cauchy-Binet formula, the sum of the products of these minors is $\det(U^{\mathsf T}V)$, the right-hand side of (1).
>
> Thus (1) agrees with the defined inner product and is independent of the representation of the object. Simple objects span $\Lambda^kW$, so the bilinear extension is unique. $\square$

## Squared norm and volume

> [!info] The numerical square of an object
> **Definition.** For a boundary $X$, write
>
> $$
> X^2=X\cdot X=\|X\|^2
> $$
>
> This is a number: the squared norm in the induced Euclidean metric. It differs from the exterior product $X\wedge X$ and from the formal quadratic form $[X]^2$. When needed, the product of an object with itself is written explicitly as $X\wedge X$.

For a simple object $X=u_1\wedge\cdots\wedge u_k$, formula (1) gives

$$
X^2=\det(u_i\cdot u_j)_{i,j=1}^k=V_{\parallel}^2
\tag{2}
$$

Here $V_{\parallel}$ is the $k$-dimensional volume of the parallelotope spanned by the vectors $u_i$. It is zero when those vectors are linearly dependent. Positive definiteness gives $X^2=0$ if and only if $X=0$, including for nonsimple exterior objects.

For a general object, the norm is computed using the bilinear extension. For example, if $X,Y$ have the same grade, then

$$
(X+Y)^2=X^2+2X\cdot Y+Y^2
$$

A general linear combination of exterior products need not be representable by a single parallelotope. Its norm is defined independently of such a geometric interpretation.

## Two triangles with a common side

Consider points $a,b,c,d$ in an affine space whose vector space is $W$. These points need not be base vertices of the graph. Set

$$
u=(ab),\qquad v=(ac),\qquad w=(ad)
$$

The triangle boundaries are $X=(abc)=u\wedge v$ and $Y=(abd)=u\wedge w$. By (1),

$$
(abc)\cdot(abd)
=\det\begin{pmatrix}u^2&u\cdot w\\v\cdot u&v\cdot w\end{pmatrix}
=u^2(v\cdot w)-(u\cdot v)(u\cdot w)
\tag{3}
$$

![[Metric of Higher-Grade Objects - two triangles.svg]]

The figure shows general Euclidean configurations. Its planar case does not represent four distinct base vertices of a resistance simplex: such vertices are affinely independent.

For $u\ne0$, decompose $v$ and $w$ into components parallel and perpendicular to $u$. Denoting the perpendicular components by $v_\perp,w_\perp$, formula (3) gives

$$
(abc)\cdot(abd)=u^2(v_\perp\cdot w_\perp)
$$

For nondegenerate triangles in the same plane, the sign is positive when $c,d$ lie on the same side of the line $ab$, and negative when they lie on opposite sides. In higher-dimensional space, the inner product is zero when the transverse directions $v_\perp,w_\perp$ are orthogonal.

> [!example] Orthogonal boundaries of grade two
> Let $u,v,w$ be orthonormal affine vectors, and set $b=a+u$, $c=a+v$, $d=a+w$. Then
>
> $$
> (abc)^2=(abd)^2=1,\qquad (abc)\cdot(abd)=0
> $$
>
> Both boundaries are nonzero and orthogonal. The triangles each have area $1/2$.

Reversing the orientation of one boundary changes the sign of the mixed inner product but preserves its squared norm. Reversing both orientations also preserves the mixed inner product.

## Areas and volumes of simplices

A simplex boundary is expressed through vectors based at one vertex:

$$
(a_0\ldots a_k)=(a_1-a_0)\wedge\cdots\wedge(a_k-a_0)
$$

Its squared norm is the squared volume of the corresponding parallelotope. The simplex itself has $1/k!$ times that volume, so

$$
V_{a_0\ldots a_k}^2=\frac{(a_0\ldots a_k)^2}{(k!)^2}
\tag{4}
$$

For a triangle and a tetrahedron,

$$
S_{abc}^2=\frac14(abc)^2,\qquad
V_{abcd}^2=\frac1{36}(abcd)^2
$$

Formula (4) computes the geometric volume of a simplex from the norm of its boundary. It does not define a norm of the formal object $[a_0\ldots a_k]$ in $\Lambda^{k+1}V$.

> [!example] The resistance triangle of $K_3$
> For $K_3$ with unit conductances, $(ab)^2=(ac)^2=2/3$ and $(ab)\cdot(ac)=1/3$. Hence
>
> $$
> (abc)^2=\det\begin{pmatrix}\frac23&\frac13\\\frac13&\frac23\end{pmatrix}
> =\frac13,\qquad S_{abc}^2=\frac1{12}
> $$
>
> This agrees with the calculation in [[From Lengths to Areas and Volumes]].

## Numerical evaluation of forms

Forms, their transposition, and polarization were defined in [[Basic Objects and Operations of Polyform Algebra|the preceding note]]. Once the metric is specified, a form on boundaries $[X,Y]$ is assigned the numerical value $X\cdot Y$. Evaluation extends linearly to forms of a fixed grade.

| Formal object | Numerical evaluation |
|---|---|
| $[X,Y]$ | $X\cdot Y$ |
| $[X]^2=[X,X]$ | $X^2=\|X\|^2$ |
| $[Y,X]$ | $Y\cdot X=X\cdot Y$ |
| $\{X,Y\}=[X,Y]+[Y,X]$ | $2X\cdot Y$ |
| $e=[1,1]$ | $1$ |

Symmetry of the numerical evaluation does not imply equality of the forms $[X,Y]$ and $[Y,X]$. In particular, their difference may be a nonzero form with zero evaluation.

The product of forms retains the rule

$$
[X,Y][A,B]=[X\wedge A,Y\wedge B]
$$

Its numerical evaluation is $(X\wedge A)\cdot(Y\wedge B)$. For vectors of grade one, formula (1) gives

$$
(X\wedge A)\cdot(Y\wedge B)
=(X\cdot Y)(A\cdot B)-(X\cdot B)(A\cdot Y)
$$

Thus the evaluation of a product of forms is generally not the product of their evaluations. For example,

$$
[(ab)]^2[(ac)]^2=[(abc)]^2
$$

The evaluation of the right-hand side is $(abc)^2$, determined by (2), rather than the product $(ab)^2(ac)^2$.

## Further reading

The next note, [[Laplacian Exponential]], collects products of coupling forms by grade into a single polyform. It will prove that evaluating a form using the induced metric agrees with normalized extraction of the highest-grade coefficient from its product with the Laplacian exponential.

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], sources [7] and [8] cover exterior powers, bilinear forms, and Gram determinants; the geometry of the resistance simplex is discussed in [4].
