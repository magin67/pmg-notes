---
title: Bi-coordinates and Di-coordinates
date: 2026-10-13
updated: 2026-11-08
revision: 11
translated_revision: 11
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: bi-coordinates-and-di-coordinates
order: 4
description: "Bi-coordinates and di-coordinates, the metric and inverse metric tensors, raising and lowering indices, and the reciprocal basis."
aliases:
  - "en/Spaces/Projections, Bi-coordinates, and Di-coordinates"
  - "en/Resistance Geometry and Duality/Spaces/Projections, Bi-coordinates, and Di-coordinates"
---

An object can be described by its expansion coefficients in a basis or by its inner products with the basis objects. In PMG, the former are called bi-coordinates and the latter di-coordinates. With a nondegenerate metric, either set determines the other: the conversion uses the metric tensor and its inverse.

This note builds on the notion of a [[Basis|basis]]. It covers the standard linear algebra of coordinates. Frames, form decompositions, and the shared material on projections are treated in [[Decomposing a Form into Atomic and Difference Parts]].

## Index convention

The indices $i,j,k$ range over the basis objects. An index appearing twice in a product, once above and once below, indicates summation over that index. No summation sign is used for such a contraction. An index appearing once is free; the equality holds for each of its values.

An upper coordinate index specifies its contravariant type rather than a power. For example, $b^i h_i$ is summed over $i$, whereas in $d_i=g_{ij}b^j$ only $j$ is summed. An explicit summation sign is retained for a restricted range, such as $i<j$, and in expressions that are not contractions of this kind.

<span id="bi-coordinates-and-frames"></span>

## Bi-coordinates

Let $h_1,\ldots,h_m$ form a basis of a linear space $U$.

> [!info] Bi-coordinates
> **Definition.** The bi-coordinates of an object $y\in U$ are the coefficients $b^i$ of its unique expansion
>
> $$
> y=b^i h_i
> \tag{1}
> $$

No metric is needed to define bi-coordinates. A basis may consist of elements, vectors, or other objects of the relevant linear space. Exterior structures of a fixed grade can likewise be expanded in a basis of that grade.

Barycentric coordinates of elements are a special case of bi-coordinates. If every $h_i$ has affine weight $1$, the weight of $y$ is the sum of its coefficients: $1$ for an element and $0$ for a vector. In a mixed basis, the weights of the basis objects must be included:

$$
\varepsilon_i=\varepsilon(h_i),\qquad
\varepsilon(y)=\varepsilon_i b^i
$$

This rule applies where an affine-weight functional $\varepsilon$ is defined.

> [!example] Elements, vectors, and a mixed basis
> In a basis of elements $(a,b)$, the element $2a-b$ has bi-coordinates $(2,-1)$, while the vector $b-a$ has bi-coordinates $(-1,1)$.
>
> If $u=b-a$, the same element is written as $a-u$ in the mixed basis $(a,u)$. Its coordinates are $(1,-1)$, but its weight is $1$: the vector $u$ has weight $0$.
>
> In a vector basis $(u,v)$, the vector $2u+3v$ has coordinates $(2,3)$. Their sum is unrestricted.

## Di-coordinates: inner products

Suppose the ambient space has a symmetric bilinear metric. It may be positive definite or indefinite.

> [!info] Di-coordinates
> **Definition.** The di-coordinates of an object $y$ relative to the basis $h_1,\ldots,h_m$ are the numbers
>
> $$
> d_i=y\cdot h_i
> \tag{2}
> $$

Di-coordinates depend on the metric. They are also defined for an object outside $U$, provided it belongs to the ambient metric space. Such an object has no bi-coordinates in the basis of $U$. Reconstruction from these di-coordinates is explained in the [[Decomposing a Form into Atomic and Difference Parts#Which coordinates determine the projection|section on projection]].

<span id="converting-between-the-two-sets-of-coordinates"></span>

## Metric tensors

The components of the metric tensor in the chosen basis are

$$
g_{ij}=h_i\cdot h_j
$$

They form the Gram matrix $\mathbf G=(g_{ij})$. Substituting (1) into (2) lowers the index:

$$
d_i=g_{ij}b^j
$$

If the metric on $U$ is nondegenerate, $\mathbf G$ is invertible. The inverse metric tensor has components $g^{ij}$ satisfying

$$
g^{ij}g_{jk}=\delta^i_k
$$

Here $\delta^i_k$ is the Kronecker symbol: $1$ if $i=k$ and $0$ otherwise. Raising the index gives

$$
b^i=g^{ij}d_j
$$

For column vectors $\mathbf b$ and $\mathbf d$, the two operations have the matrix form

$$
\boxed{\mathbf d=\mathbf G\mathbf b,\qquad
\mathbf b=\mathbf G^{-1}\mathbf d}
\tag{3}
$$

For objects $y=b^i h_i$ and $x=c^i h_i$, with $c_i=g_{ij}c^j$, the inner product and norm are

$$
y\cdot x=g_{ij}b^i c^j=b^i c_i,
\qquad
y^2=b^i d_i=g_{ij}b^i b^j=g^{ij}d_i d_j
$$

Norm here has its PMG meaning: $y^2=y\cdot y$. In an indefinite metric it can have any sign.

### Behavior under a change of basis

Let a new basis be related to the old one by an invertible matrix $A$:

$$
\widetilde h_i=h_j A^j{}_i
$$

The expansion coefficients then transform by the inverse matrix, while the inner products with the basis objects transform by the matrix itself:

$$
\widetilde b^i=(A^{-1})^i{}_j b^j,
\qquad
\widetilde d_i=A^j{}_i d_j
$$

These are the contravariant and covariant transformation laws. The metric tensors transform accordingly:

$$
\widetilde g_{ij}=A^k{}_i A^l{}_j g_{kl},
\qquad
\widetilde g^{ij}=(A^{-1})^i{}_k(A^{-1})^j{}_l g^{kl}
$$

The contractions $b^i d_i$ and $g_{ij}b^i c^j$ are unchanged by a change of basis. Upper and lower indices therefore express a transformation law, rather than merely a numbering convention.

## The reciprocal basis

If the metric on $U$ is nondegenerate, there is a unique basis $h^1,\ldots,h^m$ in the same space satisfying

$$
h^i\cdot h_j=\delta^i_j
$$

It is called the **reciprocal**, or metrically dual, basis and is expressed through the inverse metric tensor:

$$
h^i=g^{ij}h_j
$$

For $y\in U$,

$$
\boxed{b^i=y\cdot h^i,\qquad y=b^i h_i=d_i h^i}
\tag{4}
$$

> [!note]- Proof
> **Proof.** The definition of $g^{ij}$ gives $h^i\cdot h_k=g^{ij}g_{jk}=\delta^i_k$. Taking the inner product of (1) with $h^i$ yields $y\cdot h^i=b^j\delta^i_j=b^i$. Finally, $d_i h^i=d_i g^{ij}h_j=b^j h_j=y$. $\square$

Thus an object's di-coordinates are its expansion coefficients in the reciprocal basis. Bi-coordinates and di-coordinates differ in the basis used for the expansion and in the role of the metric.

## An example with a nonorthogonal basis

Let $u,v$ be orthogonal unit vectors: $u^2=v^2=1$, $u\cdot v=0$. For the basis $h_1=u$, $h_2=u+v$ and the object $y=v$,

$$
\mathbf b=\begin{pmatrix}-1\\1\end{pmatrix},\qquad
\mathbf d=\begin{pmatrix}0\\1\end{pmatrix},\qquad
\mathbf G=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad
\mathbf G^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}
$$

Indeed, $v=-h_1+h_2$, but $v\cdot h_1=0$ and $v\cdot h_2=1$. The matrices satisfy (3). The reciprocal basis is

$$
h^1=u-v,\qquad h^2=v
$$

The same object is therefore written as $v=-h_1+h_2=0h^1+1h^2$.

![Coordinates](<Coordinates.svg>)

*The basis vectors $h_1,h_2$ are not orthogonal. The expansion coefficients of $v$ are $(-1,1)$, while its inner products with the basis vectors are $(0,1)$. The reciprocal basis connects these two descriptions.*

## Applicability conditions

Bi-coordinates are unique only in a basis. On a linearly dependent set, representation coefficients may be nonunique; such representations are treated as [[Decomposing a Form into Atomic and Difference Parts#The frame of an object|frames]] in the second note.

Di-coordinates are defined even for a degenerate metric. Recovering bi-coordinates from them and constructing a reciprocal basis, however, require the restriction of the metric to $U$ to be nondegenerate. In a positive definite space, this holds for every subspace. In an indefinite space, independence of the basis objects alone is insufficient.

## Status of the results and continuation

Coordinate expansions, the metric and inverse metric tensors, raising and lowering indices, and the reciprocal basis are standard constructions of linear algebra. Here they are expressed in PMG's terminology of bi-coordinates and di-coordinates; the required identities follow from the definitions as shown above. The example is calculated directly.

<span id="an-element-and-its-projection"></span>
<span id="which-coordinates-determine-the-projection"></span>
<span id="decomposing-a-form-using-frame-elements-and-their-differences"></span>
<span id="the-difference-part-and-the-laplacian-of-a-frame"></span>
<span id="the-center-and-the-moment-of-inertia"></span>
<span id="decomposition-of-the-polar-form"></span>
<span id="calculation-using-polyforms"></span>
<span id="a-direct-calculation-on-the-path"></span>
<span id="distance-to-a-subspace"></span>
<span id="projection-of-exterior-structures-and-forms"></span>
<span id="coordinates-in-the-isotropic-extension"></span>
<span id="the-linear-midpoint-and-its-local-center"></span>
<span id="when-the-construction-needs-qualification"></span>
<span id="sources-and-status-of-the-results"></span>

Continuation: [[Decomposing a Form into Atomic and Difference Parts|frames and form decompositions]], including [[Decomposing a Form into Atomic and Difference Parts#Which coordinates determine the projection|projections]], [[Decomposing a Form into Atomic and Difference Parts#Calculation using polyforms|polyform calculations]], and [[Decomposing a Form into Atomic and Difference Parts#Coordinates in the isotropic extension|isotropic coordinates]]. Navigation: [[en/Resistance Geometry and Duality/Spaces/Spaces|Spaces]].
