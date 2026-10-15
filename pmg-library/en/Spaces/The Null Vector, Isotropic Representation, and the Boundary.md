---
title: The Null Vector, Isotropic Representation, and the Boundary
date: 2026-10-12
updated: 2026-10-15
revision: 4
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: null-vector-isotropic-representation-and-boundary
order: 2
description: "Local points and their linear combinations, the distinguished null vector, flat subspaces, the boundary operator, and metric evaluations of PMG forms."
---

The [[Spaces, Subspaces, and the Choice of a Basis|previous note]] defines the metric on differences of points. Here we construct a space with a null vector $z$ in which local points themselves are isotropic elements. We denote vertices and points directly by $a,b,x$, without separate notation for their representatives.

A linear combination of local points need not be local. For an element of unit affine weight, a correction along $z$ selects its local center. This distinction is needed for coordinates, exterior descriptions of subspaces, and the boundary operator.

## The original points and the extended space

Let $W_0$ be a positive definite displacement space of dimension $d$. For a connected graph with positive conductances, it is a Euclidean realization of the resistance metric, with $d=n-1$.

**Definition.** Add two independent elements $o,z$ to $W_0$ and denote the resulting linear space by $\widetilde V$. Its metric is specified by

$$
o^2=z^2=0,\qquad o\cdot z=1,\qquad
o\cdot w=z\cdot w=0\quad(w\in W_0)
\tag{1}
$$

Here $U^2=U\cdot U$ is the **norm** in the PMG convention. It is a quadratic quantity that may have either sign in the extension. For $U^2\ge0$, the quantity $\|U\|=\sqrt{U^2}$ is the **linear norm**. For arbitrary elements,

$$
(\alpha o+w+\beta z)\cdot(\alpha' o+w'+\beta' z)
=w\cdot w'+\alpha\beta'+\beta\alpha'
$$

The elements $(o+z)/\sqrt2$ and $(o-z)/\sqrt2$ are orthogonal and have norms $1$ and $-1$. Hence $\widetilde V$ has signature $(d+1,1)$ and dimension $d+2$. All subsequent elements belong to this space; $W_0$ is used for their coordinate expressions.

> [!info] The null vector and the zero element
> A nonzero linear element with zero norm $U\cdot U=0$ is **isotropic**. The distinguished element $z\ne0$, with $z^2=0$, is called the null vector. It is not the zero element: $z\cdot o=1$.

## Local points

> [!info] A local point
> **Definition.** A local element has unit affine weight and zero norm. Geometrically, it is a local point $x\in\widetilde V$:
>
> $$
> x^2=0,\qquad x\cdot z=1
> $$

Locality includes the weight condition; isotropy only means that a nonzero linear element has zero norm. Thus local elements are isotropic, but the null vector $z$ is not local: its affine weight $z\cdot z$ is $0$. For points, we use “local” below.

Every local point has the unique expression

$$
x=o+w-\frac{w^2}{2}z,\qquad w\in W_0
\tag{2}
$$

Indeed, for $x=\alpha o+w+\beta z$, normalization gives $\alpha=1$, and isotropy gives $\beta=-w^2/2$. The point $o$ is the chosen origin. The element $z$ is not a local point, since $z\cdot z=0$.

For $x=o+w-w^2z/2$ and $y=o+v-v^2z/2$, direct calculation gives

$$
x\cdot y=-\frac{(w-v)^2}{2},\qquad
(y-x)^2=-2x\cdot y=(v-w)^2
$$

Thus the norm of a difference of local points equals their squared Euclidean distance. In the resistance realization, $(a_j-a_i)^2=R_{ij}$.

Choose local vertices $a_1,\ldots,a_n$ whose coordinates in $W_0$ are affinely independent. Then $a_1,\ldots,a_n,z$ are linearly independent. The span $V=\operatorname{span}(a_1,\ldots,a_n)$ retains the algebraic structure of the vertex space in the [[Core specification|PMG core]]. Its elements of unit affine weight can have nonzero norm. Locality is an additional condition in this metric model.

### Example: the same three-vertex path

For the path $a-b-c$ with unit conductances, choose orthogonal directions $u,v\in W_0$ with $u^2=v^2=1$. Its local vertices are

$$
a=o,\qquad b=o+u-\frac12z,\qquad c=o+u+v-z
$$

Thus $a\cdot b=b\cdot c=-1/2$ and $a\cdot c=-1$, giving $R_{ab}=R_{bc}=1$ and $R_{ac}=2$. In the extension, the vertex differences are $b-a=u-z/2$ and $c-b=v-z/2$; their metric products agree with those of $u,v$.

## Linear combinations and correction along the null vector

A linear combination $p=\sum_i p_i a_i$ with $\sum_i p_i=1$ has affine weight $1$, but need not have zero norm. If $p^2\ne0$, we call it a **nonlocal element** of unit weight.

> [!info] Isotropic correction
> **Lemma.** For $p\cdot z=1$, the unique local point on the line $p+\mathbb Rz$ is
>
> $$
> \pi(p)=p-\frac{p^2}{2}z
> \tag{3}
> $$

> [!proof]- Proof
> We have $(p+\lambda z)^2=p^2+2\lambda$ and $(p+\lambda z)\cdot z=1$. The norm therefore vanishes exactly when $\lambda=-p^2/2$. $\square$

The point $\pi(p)$ is called the **local center** of $p$. The operation preserves the coordinate $w$ in $p=o+w+\beta z$. It fixes local points, satisfies $\pi(\pi(p))=\pi(p)$, and is constant along $p+\mathbb Rz$. It is a nonlinear projection along $z$ onto the set of local points, not an orthogonal projection onto a linear subspace.

### The midpoint and the entire line

For the end vertices of our path, set

$$
p(t)=(1-t)a+tc,\qquad p(t)^2=-2t(1-t)
$$

The local points on the line through $a,c$ are

$$
x(t)=\pi(p(t))=(1-t)a+tc+t(1-t)z
$$

In particular, the linear midpoint $p_m$ and the local midpoint $m$ differ:

$$
p_m=\frac{a+c}{2},\qquad p_m^2=-\frac12,\qquad
m=\pi(p_m)=\frac{a+c}{2}+\frac14z
$$

This also shows nonlinearity: $\pi((a+c)/2)\ne(\pi(a)+\pi(c))/2$.

![[Isotropic.svg]]

*The left panel shows the Euclidean geometry of centers in the resistance plane. The right panel uses the coordinates of expressions $(1-t)a+tc+\eta z$: the horizontal coordinate is $t$ and the vertical coordinate is $\eta$. The line $\eta=0$ contains the linear combinations $p(t)$; the parabola $\eta=t(1-t)$ contains the local points $x(t)$. This is a coordinate diagram, not a depiction of Euclidean lengths in the extension.*

All real $t$ describe the local line; $0\le t\le1$ selects the segment. We have

$$
(x(t)-x(s))^2=2(t-s)^2
$$

Distance is determined by this formula, not by arc length along the drawn parabola.

## Affine weight and the space of displacements

Every element of the extension has a unique expression $U=\sum_i u_i a_i+\beta z$. Affine weight is given by

$$
\varepsilon(U)=z\cdot U=\sum_i u_i
\tag{4}
$$

On $V$, this is the original coefficient-sum functional. The coefficient of $z$ is not included. For example, $z\cdot(2a-b+3z)=1$, but $(2a-b+3z)^2=8$: unit weight does not imply locality.

Write the space of elements of weight zero as

$$
z^\perp=\{U\in\widetilde V:z\cdot U=0\}
$$

The element $z$ belongs to this space and is orthogonal to every element in it. Hence the metric on $z^\perp$ is degenerate. For $U,V\in z^\perp$,

$$
(U+\alpha z)\cdot(V+\beta z)=U\cdot V
$$

In particular, correction (3) preserves norms of differences of normalized elements:

$$
(\pi(p)-\pi(q))^2=(p-q)^2
$$

**Definition.** Regard $U$ and $U+\alpha z$ in $z^\perp$ as the same displacement. The space of these classes, denoted $z^\perp/\mathbb Rz$, is a quotient space. Each class has a unique coordinate $w\in W_0$, and its metric agrees with that of $W_0$:

$$
z^\perp/\mathbb Rz\simeq W_0
$$

For example, $m-a=(u+v)/2-z/4$ and $(c-a)/2=(u+v)/2-z/2$ are different elements but the same displacement. The core affine-vector space $W=\{\sum_i u_i a_i:\sum_i u_i=0\}$ also contains exactly one element of each class and retains the original positive definite metric.

## Where the flat geometry appears, and which normal is involved

The condition $x\cdot z=1$ defines an affine hyperplane in $\widetilde V$. Its direction space is $z^\perp$, so $z$ is a normal to it. Since $z^2=0$, this normal also belongs to the direction space.

Local points lie at the intersection of this hyperplane with the null cone $x^2=0$. This intersection is not an affine plane in the ambient linear space. Nevertheless, its distances reproduce flat Euclidean geometry. The curvature of the coordinate parabola is not the intrinsic curvature of that geometry.

### A normal to a selected direction need not be $z$

In the example with $a,c$, set $N=-a-c$. Then

$$
N\cdot a=N\cdot c=1,\qquad N\cdot(c-a)=0,\qquad N^2=-2
$$

The element $N$ is normal to the selected direction $c-a$, but not to the entire normalization hyperplane. Along the local line,

$$
N\cdot x(t)=1-2t(1-t),\qquad z\cdot x(t)=1
$$

Thus a discussion of a normal must specify the relevant subspace or section. Sections with other normals and the geometry of spheres remain a separate continuation.

## Affine subspaces in exterior form

Exterior products are defined for all linear elements of $\widetilde V$. Antisymmetry gives

$$
z\wedge(p+\lambda z)=z\wedge p,\qquad z\wedge\pi(p)=z\wedge p
$$

For example, $z\wedge m=z\wedge(a+c)/2$, although $m\ne(a+c)/2$.

### A point and a line

For a local point $a$, the condition $x\wedge z\wedge a=0$ means $x=\alpha a+\beta z$. If also $x\cdot z=1$ and $x^2=0$, then $\alpha=1$ and $\beta=0$. Only the point $a$ remains.

The line through $a,c$ is specified by $z\wedge a\wedge c$. The condition

$$
x\wedge z\wedge a\wedge c=0
$$

gives $x=\alpha a+\beta c+\eta z$. Normalization requires $\alpha+\beta=1$, and locality gives $\eta=\beta(1-\beta)$. These are the points $x(t)$ found above. Without $z$, the span specified by $a\wedge c$ contains only the two local points $a,c$.

### A subspace of arbitrary dimension

Let local points $q_0,\ldots,q_k$ have affinely independent coordinates in $W_0$. Then

$$
F=z\wedge q_0\wedge\cdots\wedge q_k
$$

is nonzero and specifies their $k$-dimensional Euclidean affine hull: its local points satisfy $x\wedge F=0$, $x^2=0$, and $x\cdot z=1$.

> [!proof]- Proof
> Independence of $z,q_0,\ldots,q_k$ follows from independence of the spatial differences. The condition $x\wedge F=0$ gives $x=\sum_i\lambda_iq_i+\eta z$. Normalization requires $\sum_i\lambda_i=1$, and locality uniquely determines $\eta$ by (3). Hence the required points are $x=\pi(\sum_i\lambda_iq_i)$; their coordinates in $W_0$ form the usual affine hull of the coordinates of $q_i$. $\square$

For example, $z\wedge a\wedge b\wedge c$ specifies the entire resistance plane of our path. In its minimal four-dimensional extension, $x\wedge F=0$ holds automatically by dimension; the locality and normalization conditions remain. The triangle is selected by the additional inequalities $\lambda_i\ge0$.

## The boundary operator as contraction with $z$

In the PMG core, the boundary operator is defined by affine weight and requires no metric. In the extension, the same weight has the metric expression (4).

**Definition.** On an exterior product of linear elements $U_1,\ldots,U_k\in\widetilde V$, set

$$
\partial(U_1\wedge\cdots\wedge U_k)
=\sum_{i=1}^k(-1)^{i-1}(z\cdot U_i)
U_1\wedge\cdots\wedge\widehat{U_i}\wedge\cdots\wedge U_k
\tag{5}
$$

The hat over a factor means that it is omitted. The operation extends by linearity; on scalars, set $\partial1=0$. Removing one factor at a time with these weights and signs is called **contraction with the functional** $\varepsilon$, or, here, contraction with $z$.

For local vertices, $z\cdot a_i=1$. Thus the formula on their span agrees with the PMG boundary operator. For example,

$$
\partial(a\wedge c)=c-a
$$

$$
\partial(a\wedge b\wedge c)
=b\wedge c-a\wedge c+a\wedge b
=(b-a)\wedge(c-a)
$$

The last expression is the boundary $(abc)$ in the vertex space $V$. Parentheses still denote an algebraic boundary, not the selected vertex set of a Dirichlet problem.

On an element of grade $1$, we have $\partial U=z\cdot U$. For example, $\partial(c-a+3z)=0$. The boundary of a scalar is zero, so even for a pair of points we have $\partial^2(a\wedge c)=\partial(c-a)=1-1=0$.

In general, each removal of a pair of factors occurs twice with opposite signs. Hence $\partial^2=0$. For a homogeneous exterior element $S$ of grade $k$, expanding (5) also gives

$$
\partial(S\wedge T)=\partial S\wedge T+(-1)^kS\wedge\partial T
$$

In particular, since $\partial z=0$,

$$
\partial(z\wedge T)=-z\wedge\partial T
$$

For example, $\partial(z\wedge a)=-z$, while $\partial(z\wedge a\wedge c)=-z\wedge(c-a)$.

> [!note] Multiplication and the boundary
> Exterior multiplication by $z$ raises the grade by one. The boundary operator lowers it by one. They are related by an identity but are not the same operation. The operator $\partial$ itself does not require a null vector: the affine-weight functional is sufficient to define it. The condition $z^2=0$ belongs to the chosen metric realization.

## Metric evaluations of exterior elements and forms

The inner product extends to exterior elements of the larger space just as in [[Metric of Higher-Grade Objects]]: the inner product of two decomposable elements of the same grade is the determinant of the matrix of pairwise inner products of their factors. The rule extends to sums by bilinearity.

In particular, the norm of a decomposable element is the determinant of its Gram matrix, the matrix of inner products of its factors with one another. This numerical evaluation may be negative; the notation $S^2=S\cdot S$ denotes the quadratic norm in PMG.

For example,

$$
(z\wedge a)^2=
\det\begin{pmatrix}0&1\\1&0\end{pmatrix}=-1
$$

For the end vertices of our path, an independent calculation gives

$$
(z\wedge a\wedge c)^2=
\det\begin{pmatrix}
0&1&1\\
1&0&-1\\
1&-1&0
\end{pmatrix}=-2
$$

The negative sign does not mean that the squared distance between $a,c$ is negative. The connection with distance is given by the following identity.

> [!info] The null vector and metric evaluation of the boundary
> **Theorem.** For every homogeneous exterior element $S$ of the extended space,
>
> $$
> (z\wedge S)^2=-(\partial S)^2
> \tag{6}
> $$

> [!proof]- Proof
> Expanding the determinant along a row gives
>
> $$
> (z\wedge B)\cdot C=B\cdot\partial C
> $$
>
> for elements $B,C$ of grades $k-1,k$. For decomposable elements, the expansion coefficients are exactly $(-1)^{i-1}(z\cdot C_i)$ from (5); the equality then extends by bilinearity. Apply it twice:
>
> $$
> \begin{aligned}
> (z\wedge S)^2
> &=S\cdot\partial(z\wedge S)\\
> &=-S\cdot(z\wedge\partial S)\\
> &=-(\partial S)\cdot(\partial S)
> \end{aligned}
> $$
>
> For scalar grade, both sides of (6) are directly zero. $\square$

If $S=a\wedge c$, the right-hand side is $-(c-a)^2=-2$, in agreement with the direct determinant calculation. If $S=a\wedge b\wedge c$, then

$$
(z\wedge a\wedge b\wedge c)^2
=-\bigl((b-a)\wedge(c-a)\bigr)^2=-1
$$

Here $b-a=u-z/2$ and $c-a=u+v-z$. Their norms are $1,2$, and their inner product is $1$. The norm of the boundary is therefore $1\cdot2-1^2=1$. This is the squared area of the parallelogram; the triangle itself has area $1/2$.

### Passing to PMG forms

Formal forms $[S,T]$ can now be constructed with exterior arguments from $\widetilde V$. Their product follows the same rule as before:

$$
[S,T][P,Q]=[S\wedge P,T\wedge Q]
$$

As before, $[S]^2$ means $[S,S]$. The form itself is distinct from the number $S^2$.

For example, the form $[z]^2$ is nonzero: its definition imposes only bilinearity relations, and $z$ is a nonzero basis element of the extension. Yet its numerical metric evaluation is $z^2=0$. We also have

$$
([z]^2)^2=[z\wedge z]^2=0
$$

The last equality follows from antisymmetry of the exterior product and holds for the form of every linear element, not only an isotropic one.

Multiplication by another form can produce a nonzero evaluation:

$$
[z]^2[a\wedge c]^2=[z\wedge a\wedge c]^2
\quad\longmapsto\quad -2
$$

The arrow denotes the passage from a formal form to its numerical metric evaluation. Thus a form with zero evaluation can have a product with nonzero evaluation. Metric evaluation of a product is not multiplication of the numerical evaluations of its factors.

For mixed arguments, the same proof gives

$$
(z\wedge S)\cdot(z\wedge T)
=-(\partial S)\cdot(\partial T)
$$

This applies to $S,T$ of the same grade and extends by linearity to forms and polyforms. It is an equality of **metric evaluations**, not an equality of the forms $[z\wedge S,z\wedge T]$ and $-[\partial S,\partial T]$: their grades differ.

### What is preserved from the graph's metric polyform

The space $W=\{\sum_i u_i a_i:\sum_i u_i=0\}$ retains the core resistance metric. Forms on $W$, their products, and their metric evaluations therefore remain unchanged. In particular,

$$
L=\sum_{i<j}c_{ij}[a_j-a_i]^2,\qquad M_G=\exp L
$$

The spanning-tree form and the functional extracting its coefficient are defined in the original vertex span $V$. Normalized potentials of forms on $W$ retain their previous values. For example, the evaluation of $[c-a]^2$ on our path is $2$; identity (6) expresses the same number through $[z\wedge a\wedge c]^2$ with a minus sign.

The core metric identity does not automatically extend to all forms in the larger space. Forms whose arguments contain $z$ or local points receive a numerical evaluation from the extended bilinear metric. Expressing it through a separate metric polyform of the extension requires an additional definition.

## Scope and the role of the construction

The construction uses the positive definite displacement metric. For a connected graph, the published PMG core provides it. For a disconnected graph, the model can be constructed separately on each component; the original construction does not provide finite distances between components.

The exterior description of a subspace requires affine independence of the Euclidean coordinates of its generators. For example, local points $a,m,c$ lie on one Euclidean line. Although they are linearly independent as elements of the extension in the span of $a,c,z$, the product $z\wedge a\wedge m\wedge c$ vanishes. It does not specify a plane: $z\wedge a\wedge c$ suffices for this line.

Introducing $z$ is not necessary for calculating effective resistances, finding projections in $W$, or solving the Dirichlet problem. Here it connects local points, affine weight, exterior descriptions of subspaces, and the metric realization of the boundary. The geometry of spheres remains a separate continuation.

The [[Projections, Bi-coordinates, and Di-coordinates#Coordinates in the isotropic extension|note on coordinates in the isotropic extension]] distinguishes linear orthogonal projection from selection of the local center.

## Sources and status of the results

The algebraic definitions of vertices, vectors, boundaries, and forms follow the [[Core specification|core specification]]. The extension, isotropic correction, criterion for the exterior description of an affine subspace, and identity (6) are proved in the text. Numerical examples are calculated directly; the determinant for $z\wedge a\wedge c$ is calculated independently of (6).

The previous revision included exact rational checks in the four-dimensional model: local points, the midpoint correction, distances, and determinant evaluations. The bilinear version of (6) was checked on all 70 pairs of exterior basis elements of the same grade. During the notation revision, the example formulas and projection coordinates in the related note were checked again. These calculations verify signs and do not replace the general proof. No working conjectures are included.

The internal Russian notes “Isotropic Representation of Points and the Null Vector”, “Sphere Normals and Lorentzian Geometry”, and “The Null Vector: Exterior Products and the Boundary” were checked during preparation. Local points are now denoted directly; their linear combinations and local centers are explicitly distinguished. “Local point” and “nonlocal element” are used here in the stated PMG sense.

The isotropic model of Euclidean points and the exterior description of lines are known constructions in conformal geometric algebra. The correspondence was checked against [H. Li, D. Hestenes, A. Rockwood, *Generalized Homogeneous Coordinates for Computational Geometry*](https://davidhestenes.net/geocalc/pdf/CompGeom-ch2.pdf), §2.3, equations (2.25), (2.26), and (2.32)–(2.34). That source uses $x\cdot e=-1$; our notation corresponds to $z=-e$ and $o=e_0$. The geometric product of Clifford algebra is not identified with the PMG product of forms.

