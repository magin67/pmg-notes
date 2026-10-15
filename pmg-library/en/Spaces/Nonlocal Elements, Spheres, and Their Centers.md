---
title: Nonlocal Elements, Spheres, and Their Centers
date: 2026-10-15
updated: 2026-10-15
revision: 2
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: nonlocal-elements-spheres-and-centers
order: 3
description: "The spherical interpretation of an element's norm, selection of its local center, and preservation of metric evaluations of vectors and boundaries when the norms of their vertices change."
---

An element of unit affine weight need not be a local point. Its nonzero norm carries an additional parameter that can change while the center remains fixed. This note explains the geometric meaning of that parameter and proves that such changes preserve the norms and inner products of differences, as well as metric evaluations of boundaries of every grade.

The construction uses the [[The Null Vector, Isotropic Representation, and the Boundary|extension with a null vector]]. Throughout, norm has its PMG meaning: $U^2=U\cdot U$. For $U^2\ge0$, the square root $\|U\|=\sqrt{U^2}$ is called the linear norm. The formal form $[U]^2$ is distinct from the numerical norm $U^2$.

## Assumptions and notation

We work in a single extended space $\widetilde V$ with a nondegenerate metric of signature $(d+1,1)$ and a distinguished null vector $z$. The displacement space $z^\perp/\mathbb Rz$ is positive definite and has dimension $d\ge1$. For a connected graph with positive conductances, this is its resistance space, with $d=n-1$.

The affine weight of an element is $\varepsilon(U)=U\cdot z$. We consider the affine hyperplane

$$
\mathcal H=\{S\in\widetilde V:S\cdot z=1\},\qquad z^2=0
$$

**Definition.** An element $S\in\mathcal H$ is local if $S^2=0$ and nonlocal if $S^2\ne0$. Local elements are denoted directly as points $x,h,a_i$. No separate notation for their representatives is introduced.

Elements of zero weight, including $z$, are not called local points. Differences of elements of $\mathcal H$ belong to $z^\perp$; in the extended space, this extends the notion of an affine vector from the PMG core. The metric on $z^\perp$ is degenerate: $z$ is orthogonal to this entire subspace.

## Decomposing an element into its center and norm

**Lemma.** Every $S\in\mathcal H$ has a unique representation

$$
\boxed{S=h+\frac{\rho}{2}z,\qquad h^2=0,\qquad h\cdot z=1,\qquad \rho=S^2}
\tag{1}
$$

The local point $h$ is called the center of $S$ and is given by

$$
h=\pi(S)=S-\frac{S^2}{2}z
$$

> [!proof]- Proof
> **Proof.** For $h=S-S^2z/2$, we have $h\cdot z=1$ and $h^2=S^2-S^2(S\cdot z)=0$. Conversely, $S=h+\rho z/2$ under the stated conditions gives $S^2=\rho$. Hence both the coefficient and the center are uniquely determined. $\square$

All elements with the same center form the line $h+\mathbb Rz$. Moving an element along this line gives

$$
\pi(S+\lambda z)=\pi(S),\qquad (S+\lambda z)^2=S^2+2\lambda
$$

Thus the center and norm are independent data of a normalized element. With the center fixed, the norm can take any real value.

## A sphere as an orthogonality condition

**Theorem.** Let $S=h+\rho z/2$, and let $x$ be a local point. Then

$$
\boxed{x\cdot S=\frac{\rho-(x-h)^2}{2}}
\tag{2}
$$

Consequently, the local points orthogonal to $S$ satisfy

$$
x\cdot S=0\quad\Longleftrightarrow\quad(x-h)^2=\rho
$$

> [!proof]- Proof
> **Proof.** Since $x^2=h^2=0$, we have $x\cdot h=-(x-h)^2/2$. Substituting (1) and using $x\cdot z=1$ gives (2). $\square$

For $\rho>0$, this is a sphere with center $h$ and linear radius $\sqrt\rho$. In a displacement space of dimension $d$, the sphere has dimension $d-1$. For $\rho=0$, the set consists of the single local point $h$. For $\rho<0$, it has no real local points, since $(x-h)^2\ge0$.

Thus a positive norm of a normalized element has the precise meaning of a squared sphere radius. A negative norm retains its algebraic meaning as the parameter in (2), but is not the squared radius of a real sphere. The center exists in all three cases.

### The circumsphere of a graph

Let the local vertices $a_1,\ldots,a_n$ form a nondegenerate resistance simplex. For its circumsphere, define

$$
S_G=h+\frac{\rho(G)}2z,\qquad
\rho(G)=(a_i-h)^2
$$

Here $h$ is the local center of the sphere, and $\rho(G)$ does not depend on the vertex. By (2),

$$
S_G\cdot a_i=0,\qquad S_G^2=\rho(G),\qquad
h\cdot a_i=-\frac{\rho(G)}2
$$

**Remark.** The sphere element $S_G$ is orthogonal to every vertex. Its local center $h$ has zero norm and, for $\rho(G)>0$, is not orthogonal to the vertices. These are distinct elements of the same space.

In PMG metric-parameter terminology, the **resistance radius** of a graph is $\rho(G)=R_{\mathrm{sph}}^2$, and its **resistance diameter** is

$$
D_{\mathrm{res}}(G)=4\rho(G)=(2R_{\mathrm{sph}})^2
$$

Here “resistance” specifies a quadratic quantity. The linear diameter is $2R_{\mathrm{sph}}$. The parameter $D_{\mathrm{res}}$ is determined by the circumsphere and generally differs from the maximum pairwise effective resistance. Additivity under single-vertex gluing is proved in the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|note on graph gluing]].

### The center in the affine hull of the original vertices

In the notes on projections and gluing, centers can be calculated in the original affine space without introducing $z$. In the extension, the corresponding combination of original vertices need not be local. This distinction matters when comparing the formulas.

Let $h_V=\sum_i\alpha_i a_i$, with $\sum_i\alpha_i=1$, have the coordinates of the Euclidean circumcenter. Then

$$
h_V^2=-\rho(G),\qquad
h=\pi(h_V)=h_V+\frac{\rho(G)}2z,\qquad
S_G=h_V+\rho(G)z
$$

> [!proof]- The norm of the affine combination giving the center
> **Proof.** For every vertex, $(a_i-h_V)^2=\rho(G)$. Since $a_i^2=0$, we obtain $a_i\cdot h_V=(h_V^2-\rho(G))/2$. Multiply by $\alpha_i$ and sum: $h_V^2=(h_V^2-\rho(G))/2$. Hence $h_V^2=-\rho(G)$, and the remaining identities follow from (1). $\square$

Here $h_V$ denotes the original affine combination, $h$ its local center, and $S_G$ the circumsphere element. These symbols identify particular elements of one model, rather than additional types of geometric center.

## What selecting the center preserves

Let $S,T\in\mathcal H$, $h=\pi(S)$, and $k=\pi(T)$. Equation (1) gives

$$
\boxed{S\cdot T=h\cdot k+\frac{S^2+T^2}{2}}
\tag{3}
$$

Thus the inner product of the elements themselves is generally not preserved: it depends on both norms. For differences, however, we obtain

$$
\boxed{(S-T)^2=(h-k)^2}
\tag{4}
$$

This is the squared distance between the centers; in resistance geometry, it has the units of resistance. Distinct elements with the same center have a difference of zero norm. Therefore (4) specifies distance between centers but does not distinguish all elements of $\mathcal H$.

> [!proof]- Preservation of the norm of a difference
> **Proof.** We have $S-T=h-k+(S^2-T^2)z/2$. Since $(h-k)\cdot z=0$ and $z^2=0$, the term along $z$ does not affect the norm. $\square$

### Why the projection is nonlinear

The map $\pi$ fixes local points and satisfies $\pi(\pi(S))=\pi(S)$. It does not, however, preserve affine combinations. For any $S,T\in\mathcal H$ and $t\in\mathbb R$,

$$
\pi((1-t)S+tT)
=(1-t)\pi(S)+t\pi(T)+\frac{t(1-t)}2(S-T)^2z
$$

This follows by expanding the norm of the combination. In particular, for distinct local points $a,b$,

$$
\pi\left(\frac{a+b}{2}\right)
=\frac{a+b}{2}+\frac{(a-b)^2}{8}z
$$

Preservation of (4) therefore does not make $\pi$ a linear or affine projection. Linear orthogonal projection onto a subspace and nonlinear selection of the center perform different tasks; they are compared in the [[Projections, Bi-coordinates, and Di-coordinates#Coordinates in the isotropic extension|note on coordinates]].

## Inner products of vectors

**Theorem.** For any $S_0,S_1,T_0,T_1\in\mathcal H$,

$$
(S_1-S_0)\cdot(T_1-T_0)
=(\pi(S_1)-\pi(S_0))\cdot(\pi(T_1)-\pi(T_0))
$$

Consequently, the norms of the endpoints do not affect the norms and inner products of vectors when the centers of the endpoints remain fixed.

> [!proof]- Proof
> **Proof.** Selecting the centers changes each difference only by a multiple of $z$. For any $u,v\in z^\perp$ and $\alpha,\beta\in\mathbb R$,
>
> $$
> (u+\alpha z)\cdot(v+\beta z)=u\cdot v
> $$
>
> This follows from $u\cdot z=v\cdot z=z^2=0$. $\square$

The statement also holds for arbitrary combinations of zero weight. If $\sum_i\alpha_i=\sum_j\beta_j=0$, then

$$
\left(\sum_i\alpha_iS_i\right)\cdot\left(\sum_j\beta_jT_j\right)
=\left(\sum_i\alpha_i\pi(S_i)\right)\cdot\left(\sum_j\beta_j\pi(T_j)\right)
$$

**The condition is essential.** Changing norms with centers fixed means replacing $S_i\mapsto S_i+\lambda_i z$. The inner products of the endpoints themselves then change consistently:

$$
(S_i+\lambda_i z)\cdot(S_j+\lambda_j z)
=S_i\cdot S_j+\lambda_i+\lambda_j
$$

Arbitrarily changing only the diagonal entries of the Gram matrix is not such a replacement and generally changes the norms of differences.

## Higher-grade boundaries

For elements $S_0,\ldots,S_k$ of unit weight, the boundary formula remains

$$
B=(S_0\ldots S_k)=\bigwedge_{i=1}^k(S_i-S_0)
$$

Write $h_i=\pi(S_i)$ and $B_h=(h_0\ldots h_k)$. Boundaries use the same operator $\partial$ as in the [[The Null Vector, Isotropic Representation, and the Boundary#The boundary operator as contraction with $z$|note on the null vector]].

**Theorem.** Replacing vertices by their local centers preserves the norms of boundaries of every grade and the inner products of any two boundaries of the same grade:

$$
\boxed{B^2=B_h^2,\qquad B\cdot C=B_h\cdot C_h}
\tag{5}
$$

In the second identity, the boundary $C$ may be formed from a different set of elements of unit weight.

> [!proof]- Proof for decomposable boundaries and their sums
> **Proof.** For decomposable boundaries, the inner product is the mixed Gram determinant:
>
> $$
> B\cdot C=\det\bigl((S_i-S_0)\cdot(T_j-T_0)\bigr)_{i,j=1}^k
> $$
>
> Every matrix entry is preserved by the theorem on vectors, so the determinant is preserved. Taking $C=B$ gives equality of norms. For fixed linear combinations of boundaries, the result follows by bilinearity. In grade $0$, the replacement leaves scalars unchanged. $\square$

The statement therefore includes nondecomposable boundaries. In particular, it preserves the squared areas and volumes of simplices of centers, calculated as $B^2/(k!)^2$.

### What happens to the objects and forms themselves

Equal norms do not imply equal exterior objects. Expanding the factors gives

$$
B-B_h=z\wedge K,\qquad K\in\Lambda^{k-1}(z^\perp)
$$

All terms containing two factors $z$ vanish. For any boundary $C\in\Lambda^k(z^\perp)$, we have $(z\wedge K)\cdot C=0$: the determinant of inner products contains a zero row. This explains why the metric evaluation is preserved while the object changes.

The forms $[B,C]$ and $[B_h,C_h]$ need not coincide either. Their numerical evaluations $B\cdot C$ and $B_h\cdot C_h$ coincide. The same applies to sums of forms and products of forms on boundaries: their exterior arguments lie in powers of $z^\perp$, where additional terms containing $z$ do not affect the evaluation.

This restriction matters. In the full exterior algebra of the extension, $z$ is not orthogonal to every element. For example, for a local point $a$, we have $(z\wedge a)^2=-1$. The result therefore does not extend to arbitrary simplices and forms outside the boundary subalgebra. The core metric identity through normalized potentials likewise does not automatically extend to all forms of the extended space.

## Local basis vertices do not restrict the graph model

**Corollary.** Let $A_1,\ldots,A_n$ have unit affine weight, and let their local centers $h_i=\pi(A_i)$ form the resistance simplex of a connected graph with positive conductances. Replacing $A_i\mapsto h_i$ preserves the resistance metric and gives an isomorphic representation of the algebra of forms on boundaries. The Laplacian and its exponential map to the corresponding forms on local vertices with the same coupling coefficients.

Thus the basis vertices can be chosen local without restricting the graph model under consideration. Their individual norms are additional data of the realization and are not determined by the metric on boundaries.

> [!proof]- A linear change of the fixed basis
> **Proof.** In the minimal extension of dimension $n+1$, the elements $A_1,\ldots,A_n,z$ form a basis: independence follows from the affine independence of the spatial coordinates of their centers. Define a linear map $F$ on this basis:
>
> $$
> F(A_i)=h_i=A_i-\frac{A_i^2}{2}z,\qquad F(z)=z
> $$
>
> Its matrix is triangular with unit diagonal, so $F$ is invertible. It preserves affine weight. Its extension to the exterior algebra therefore commutes with the boundary operator: $\partial F=F\partial$.
>
> For any $u\in z^\perp$, the difference $F(u)-u$ is a multiple of $z$. Hence $F(u)\cdot F(v)=u\cdot v$ for $u,v\in z^\perp$. The determinant formula and bilinearity then show that inner products of boundaries of every grade are preserved.
>
> Extend the map to forms by $F([X,Y])=[F(X),F(Y)]$. It preserves the product of forms and the identity form. With the coefficients $c_{ij}$ fixed, we obtain
>
> $$
> L_A=\sum_{i<j}c_{ij}[A_j-A_i]^2,\qquad
> F(L_A)=L_h=\sum_{i<j}c_{ij}[h_j-h_i]^2
> $$
>
> $$
> F(\exp L_A)=\exp L_h
> $$
>
> The spanning-tree form $[(A_1\ldots A_n)]^2$ maps to $[(h_1\ldots h_n)]^2$. Consequently, coefficients relative to the respective spanning-tree forms, potentials, and normalized potentials of corresponding forms on boundaries are preserved. $\square$

**Remark on the two maps.** The linear map $F$ agrees with $\pi$ on the chosen basis vertices, but not on all elements of unit weight. If $p=\sum_i\alpha_iA_i$ and $\sum_i\alpha_i=1$, then

$$
F(p)=p-\frac12\left(\sum_i\alpha_iA_i^2\right)z,\qquad
\pi(p)=p-\frac{p^2}{2}z
$$

These elements have the same local center, but $F(p)$ need not be local. The linear change of a fixed basis provides the algebraic correspondence, whereas the nonlinear map $\pi$ selects the center of each individual element.

Isomorphism does not mean literal equality $L_A=L_h$ within the extended algebra. The structure and metric evaluations of forms on boundaries are preserved; the metric of the entire vertex space and the inner products of the vertices themselves generally change.

## The geometric model extends beyond positively weighted graphs

There are two distinct extensions of the graph description here.

First, even with the resistance metric fixed, we can consider all elements $h+\rho z/2$, rather than only local vertices. Their norms matter for describing spheres, orthogonality conditions with points, and inner products of the elements themselves. Passing to centers preserves the metric on boundaries but discards each element's parameter $\rho$. Thus freedom to choose the norms of basis vertices does not mean that the norms of all geometric objects lack content.

Second, a positive definite displacement metric can itself be specified independently of a graph. Not every Euclidean simplex is the resistance simplex of a graph with positive conductances: the recovered Laplacian matrix must have nonpositive off-diagonal entries, as stated in the [[Core specification#The distance operator|core specification]]. Positivity of couplings is an additional condition of the graph model, rather than a condition for defining an arbitrary Euclidean simplex.

The geometric description therefore covers a broader class of metrics and objects. This is not simply a claim about a greater dimension: for a graph on $n$ vertices, the minimal extension with $z$ has dimension $n+1$.

In this note, the displacement metric remains positive definite, although the extended metric has signature $(d+1,1)$ and normalized elements may have norms of any sign. Arbitrary signs of coupling coefficients do not by themselves guarantee positivity or nondegeneracy of the displacement metric. Graphs with couplings of both signs and geometries with an indefinite displacement metric require separate conditions; results for positively weighted graphs do not automatically extend to them.


## Example on a three-vertex path

Take the local vertices of the unit path $a-b-c$. In the coordinate model of the preceding note,

$$
a=o,\qquad b=o+u-\frac12z,\qquad c=o+u+v-z
$$

Here $u^2=v^2=1$ and $u\cdot v=0$, while $o,z$ are orthogonal to $u,v$ and satisfy $o^2=z^2=0$ and $o\cdot z=1$. The pairwise effective resistances are $1,1,2$.

### The center and the circumcircle element

The circumcenter of the right triangle lies midway between $a,c$. Its affine combination, local center, and circle element are

$$
h_V=\frac{a+c}{2},\qquad h=h_V+\frac14z,\qquad S_G=h_V+\frac12z
$$

A direct calculation gives

$$
h_V^2=-\frac12,\qquad h^2=0,\qquad S_G^2=\frac12,\qquad
S_G\cdot a=S_G\cdot b=S_G\cdot c=0
$$

Hence $\rho(G)=1/2$ and $D_{\mathrm{res}}(G)=2$. For $h_V$, the condition of orthogonality to a local point does not define a real circle: its norm is negative. Nevertheless, $h_V$ has the same center as $S_G$.

### Nonlocal vertices and an unchanged boundary norm

Replace the vertices by

$$
A=a+z,\qquad B=b-2z,\qquad C=c+3z
$$

Their centers are $a,b,c$, and their norms are $2,-4,6$. The inner product $A\cdot B=-3/2$ differs from $a\cdot b=-1/2$. Direct calculation nevertheless gives

$$
(B-A)^2=1,\qquad (C-A)^2=2,\qquad (B-A)\cdot(C-A)=1
$$

Therefore

$$
(ABC)^2=\det\begin{pmatrix}1&1\\1&2\end{pmatrix}=1=(abc)^2
$$

The squared area of the triangle of centers is $1/4$. The boundaries themselves differ:

$$
(ABC)-(abc)=z\wedge\bigl(-3(c-a)-2(b-a)\bigr)
$$

The additional term is nonzero but orthogonal to every grade-$2$ boundary in $\Lambda^2(z^\perp)$.

## Status of the results and continuation

Decomposition (1), the spherical interpretation (2), the change in inner product (3), and invariance (4)-(5) are proved under the stated assumptions. The corollary on choosing local basis vertices additionally establishes the correspondence between Laplacians, their exponentials, and potentials of forms on boundaries. The numerical example was calculated directly from the bilinear metric of the extension. Additional checks using exact rational arithmetic covered the formula for selecting the center of an affine combination, the metric identities for vectors, and 226 mixed Gram determinants of boundaries in a model with a three-dimensional displacement space. These checks control formulas and signs; the general theorems rest on their proofs. The note contains no working conjectures.

Representation of a sphere by a normalized element is established in conformal geometric algebra. The comparison uses [H. Li, D. Hestenes, A. Rockwood, *Generalized Homogeneous Coordinates for Computational Geometry*](https://davidhestenes.net/geocalc/pdf/CompGeom-ch2.pdf), §2.3, equations (2.38)-(2.42). The source uses $x\cdot e=-1$, so our $z$ corresponds to $-e$. Its linear radius is denoted by $\rho$; here $\rho$ denotes the squared linear radius. The Clifford product is not identified with the product of PMG forms.

This note completes the geometric foundation needed to study a graph's resistance radius and diameter. Their behavior under changes in couplings and their dimensionless combinations with other parameters belong to the series on metric parameters. The reciprocal $1/D_{\mathrm{res}}$ does not by itself acquire the electrical interpretation of conductance between specified terminals: such an interpretation requires a separate justification.

Next: [[Projections, Bi-coordinates, and Di-coordinates]]. Navigation: [[Spaces and Subspaces in PMG]].
