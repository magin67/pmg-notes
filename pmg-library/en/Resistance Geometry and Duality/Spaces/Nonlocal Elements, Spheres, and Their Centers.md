---
title: Nonlocal Elements, Spheres, and Their Centers
date: 2026-10-15
updated: 2026-11-08
revision: 5
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: nonlocal-elements-spheres-and-centers
order: 3
description: "The center and norm of a nonlocal element, inner products of elements and vectors, orthogonality of spheres, and the geometry of negative norm."
aliases:
  - "en/Spaces/Nonlocal Elements, Spheres, and Their Centers"
---

An element is determined by its local center and norm. A positive norm defines a sphere, zero norm corresponds to a point, and a negative norm admits a representation by a point outside the subspace under consideration. Inner products describe point membership in a sphere, orthogonality of spheres, and the positions of their centers relative to a vector.

The construction uses the [[The Null Vector, Isotropic Representation, and the Boundary|extension with a null vector]]. The geometric discussion is followed by a proof of which metric quantities are preserved when elements are replaced by their centers: the norms and inner products of vectors and boundaries of every grade.

## Assumptions and notation

Consider an extended space $\widetilde V$ with a nondegenerate metric of signature $(d+1,1)$ and a distinguished null vector $z$. The displacement space $z^\perp/\mathbb Rz$ is positive definite and has dimension $d\ge1$. For a connected graph with positive coupling strengths, this is its resistance space, with $d=n-1$.

The affine weight of an object is $\varepsilon(u)=u\cdot z$. Elements form the affine hyperplane

$$
\mathcal H=\{s\in\widetilde V:s\cdot z=1\},\qquad z^2=0
$$

> [!info] Elements, points, and norms
> **Definition.** An element $s\in\mathcal H$ is local if $s^2=0$ and nonlocal if $s^2\ne0$. A local element is called a point. Elements, including points, are denoted by lowercase letters: $s,t,x,a,b,\ldots$.
>
> The norm of an element is the quadratic quantity $s^2=s\cdot s$. It can be positive, zero, or negative. For $s^2\ge0$, the square root $\|s\|=\sqrt{s^2}$ is called the linear norm. The numerical norm $s^2$ is distinct from the form $[s]^2$.

Objects of zero weight, including $z$, are vectors. Differences of elements belong to $z^\perp$. The metric on $z^\perp$ is degenerate: $z$ is orthogonal to all vectors, but not to elements, since $s\cdot z=1$.

The notation $\rho(G)$ is reserved for a graph's resistance radius. The norm of an arbitrary element is denoted by $s^2$.

## Decomposing an element into its center and norm

> [!info] Decomposing an element into its center and norm
> **Lemma.** Every element $s$ has a unique representation
>
> $$
> \boxed{s=s_0+\frac{s^2}{2}z,\qquad s_0^2=0,\qquad s_0\cdot z=1}
> \tag{1}
> $$
>
> The point $s_0$ is called the center of $s$ and is given by
>
> $$
> s_0=\pi(s)=s-\frac{s^2}{2}z
> $$

> [!note]- Proof
> **Proof.** For $s_0=s-s^2z/2$, one has $s_0\cdot z=1$ and $s_0^2=s^2-s^2(s\cdot z)=0$. Conversely, if $s=c+\lambda z$, where $c^2=0$ and $c\cdot z=1$, then $s^2=2\lambda$. Hence $\lambda=s^2/2$ and $c=s_0$. $\square$

All elements with the same center form the line $s_0+\mathbb Rz$. Moving an element along this line gives

$$
\pi(s+\lambda z)=\pi(s),\qquad (s+\lambda z)^2=s^2+2\lambda
$$

The center and norm are independent data of an element. With the center fixed, the norm can take any real value.

## A sphere as an orthogonality condition

A sphere and its defining element are distinct. The sphere consists of points $x$, while the element $s$ specifies an equation that those points satisfy. When its norm is nonzero, $s$ itself is not a point.

> [!info] A point and a sphere element
> **Theorem.** For an element $s$ with center $s_0$ and a local point $x$,
>
> $$
> \boxed{x\cdot s=\frac{s^2-(x-s_0)^2}{2}}
> \tag{2}
> $$
>
> Therefore
>
> $$
> x\cdot s=0\quad\Longleftrightarrow\quad(x-s_0)^2=s^2
> $$

> [!note]- Proof
> **Proof.** Since $x^2=s_0^2=0$, one has $x\cdot s_0=-(x-s_0)^2/2$. Substituting (1) and using $x\cdot z=1$ gives (2). $\square$

For $s^2>0$, this is a sphere with center $s_0$ and linear radius $r=\sqrt{s^2}$. In a space of dimension $d$, its dimension is $d-1$: for $d=2$ it is a circle, and for $d=3$ an ordinary two-dimensional sphere. A point is orthogonal to the sphere element if and only if it lies on the surface. Inside the sphere, $x\cdot s>0$; outside, $x\cdot s<0$.

For $s^2=0$, the set consists of the single point $s_0=s$. For $s^2<0$, it has no real points, since $(x-s_0)^2\ge0$. The element and its local center remain well defined.

### The circumsphere of a graph

Let the local vertices $a_1,\ldots,a_n$ form a nondegenerate resistance simplex. For its circumsphere, define

$$
s_G=h+\frac{\rho(G)}2z,\qquad
\rho(G)=(a_i-h)^2
$$

Here $h=\pi(s_G)$ is the local center of the sphere, and $\rho(G)$ does not depend on the vertex. By (2),

$$
s_G\cdot a_i=0,\qquad s_G^2=\rho(G),\qquad
h\cdot a_i=-\frac{\rho(G)}2
$$

**Remark.** The sphere element $s_G$ is orthogonal to every vertex. Its local center $h$ has zero norm and, for $\rho(G)>0$, is not orthogonal to the vertices.

In PMG metric-parameter terminology, the **resistance radius** of a graph is $\rho(G)=R_{\mathrm{sph}}^2$, and its **resistance diameter** is

$$
D_{\mathrm{res}}(G)=4\rho(G)=(2R_{\mathrm{sph}})^2
$$

Here “resistance” specifies a quadratic quantity. The linear diameter is $2R_{\mathrm{sph}}$. The parameter $D_{\mathrm{res}}$ is determined by the circumsphere and generally differs from the maximum pairwise effective resistance. Additivity under single-vertex gluing is proved in the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|note on graph gluing]].

![The circumcircle of a resistance triangle and the circumsphere of a tetrahedron, with their local centers](Circumcircle%20and%20Circumsphere.svg)

*Left: the unit path $a-b-c$ in the resistance metric, where its vertices form a right triangle. Right: the circumsphere of a tetrahedron. In both cases, the vertices are orthogonal to the sphere element $s_G$ and lie at equal distances from its local center $h$.*

### The center in the affine hull of the original vertices

In the notes on projections and gluing, centers can be calculated in the original affine space without introducing $z$. In the extension, the corresponding combination of original vertices need not be local. This distinction matters when comparing the formulas.

Let $h_V=\sum_i\alpha_i a_i$, with $\sum_i\alpha_i=1$, have the coordinates of the Euclidean circumcenter. Then

$$
h_V^2=-\rho(G),\qquad
h=\pi(h_V)=h_V+\frac{\rho(G)}2z,\qquad
s_G=h_V+\rho(G)z
$$

> [!note]- The norm of the affine combination giving the center
> **Proof.** For every vertex, $(a_i-h_V)^2=\rho(G)$. Since $a_i^2=0$, one obtains $a_i\cdot h_V=(h_V^2-\rho(G))/2$. Multiplication by $\alpha_i$ and summation give $h_V^2=(h_V^2-\rho(G))/2$. Hence $h_V^2=-\rho(G)$, and the remaining identities follow from (1). $\square$

Here $h_V$ denotes the affine combination, $h$ its local center, and $s_G$ the circumsphere element. These are different elements of one model, rather than additional types of geometric center.

### Example: three elements associated with one circle

In the coordinate model of the preceding note, the local vertices of the unit path $a-b-c$ are

$$
a=p_0,\qquad b=p_0+u-\frac12z,\qquad c=p_0+u+v-z
$$

Here $u^2=v^2=1$ and $u\cdot v=0$, while $p_0,z$ are orthogonal to $u,v$ and satisfy $p_0^2=z^2=0$ and $p_0\cdot z=1$. The pairwise effective resistances are $1,1,2$.

The circumcenter of the right triangle lies midway between $a,c$. Its affine combination, local center, and circle element are

$$
h_V=\frac{a+c}{2},\qquad h=h_V+\frac14z,\qquad s_G=h_V+\frac12z
$$

A direct calculation gives

$$
h_V^2=-\frac12,\qquad h^2=0,\qquad s_G^2=\frac12,\qquad
s_G\cdot a=s_G\cdot b=s_G\cdot c=0
$$

Hence $\rho(G)=1/2$ and $D_{\mathrm{res}}(G)=2$. All three elements have the same local center $h$, but different norms: $-1/2$, $0$, and $1/2$. The circle is defined by orthogonality to $s_G$. For $h_V$, the orthogonality condition has no real solutions.

## Inner products of elements

> [!info] The product in terms of centers and norms
> **Theorem.** For any elements $s,t$ with centers $s_0,t_0$,
>
> $$
> \boxed{s\cdot t=s_0\cdot t_0+\frac{s^2+t^2}{2}
> =\frac{s^2+t^2-(s_0-t_0)^2}{2}}
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** Substituting (1) for both elements gives the first identity, since $s_0\cdot z=t_0\cdot z=1$ and $z^2=0$. The centers are local, so $2s_0\cdot t_0=-(s_0-t_0)^2$, which gives the second identity. $\square$

The product depends on both norms and the distance between the centers. With the norms fixed, it decreases as the squared distance increases. For two points, $s^2=t^2=0$, this gives the usual isotropic-representation formula: $s\cdot t=-(s-t)^2/2$.

### Orthogonality of two spheres

By (3),

$$
\boxed{s\cdot t=0\quad\Longleftrightarrow\quad(s_0-t_0)^2=s^2+t^2}
$$

Let $s^2=r^2>0$, $t^2=R^2>0$, and $d\ge2$. The condition becomes

$$
(s_0-t_0)^2=r^2+R^2
$$

This is the orthogonality condition for ordinary spheres: at any common point $x$, their radius vectors $x-s_0$ and $x-t_0$ are perpendicular. For circles, the tangent lines are also perpendicular; for spheres in three-dimensional space, the tangent planes meet at a right angle.

> [!note]- The geometric meaning of orthogonality
> **Proof.** For the stated center distance $D=\sqrt{r^2+R^2}$, the inequalities $|r-R|<D<r+R$ hold. Hence the spheres intersect when $d\ge2$. At a common point $x$, polarization of the Euclidean metric gives
>
> $$
> (x-s_0)\cdot(x-t_0)
> =\frac{(x-s_0)^2+(x-t_0)^2-(s_0-t_0)^2}{2}
> =s\cdot t
> $$
>
> A zero inner product of the elements is equivalent to perpendicular radius vectors. $\square$

![Orthogonal spheres in a section through their centers and a common point; a point lying on a sphere](Sphere%20Orthogonality%20and%20Point%20Incidence.svg)

*Left: a section of two spheres by the plane through their centers and a common point $x$. The radius vectors form a right triangle, so the squared center distance equals the sum of the squared radii. Right: a point $x$ on the circle is orthogonal to its element, while the inner product for an interior point $y$ is positive.*

If one element is a point, orthogonality reduces to membership in the sphere, as in (2). Two points are orthogonal only when they coincide. The statement about intersecting ordinary spheres requires positive norms; the algebraic formula (3) holds for all signs.

## Elements of negative norm

Negative norm already occurs in affine combinations of points. For example, for distinct local points $a,b$, the element

$$
s=\frac{a+b}{2}
$$

has norm and center

$$
s^2=-\frac{(a-b)^2}{4}<0,\qquad
s_0=\frac{a+b}{2}+\frac{(a-b)^2}{8}z
$$

Thus the affine average of the local representatives differs from the local point at the Euclidean midpoint of the segment.

### Representation by a point outside a subspace

An element $s$ with $s^2=-\ell^2<0$ admits a visual representation. Add one perpendicular direction to the Euclidean space. Two points $q_+,q_-$ at distance $\ell$ on opposite sides of the original space have the same Euclidean projection $s_0$. In the isotropic model, their linear orthogonal projections onto $\widetilde V$ coincide with the element $s$.

![An element of negative norm as the projection of two symmetric external points](Negative%20Norm%20and%20External%20Points.svg)

*The figure shows the original Euclidean plane and two external points. Their ordinary projection onto the plane is the point $s_0$. The linear projection of their isotropic representatives onto the extended space of the plane is the element $s=s_0-\ell^2z/2$. The negative norm therefore encodes the squared height with the opposite sign. The condition $x\cdot s=0$ does not define a real circle.*

> [!note]- Verification of the representation
> **Proof.** Add an object $n$ with $n^2=1$, orthogonal to all of $\widetilde V$. Then
>
> $$
> q_\pm=s\pm\ell n=s_0\pm\ell n-\frac{\ell^2}{2}z
> $$
>
> satisfy $q_\pm\cdot z=1$ and $q_\pm^2=s^2+\ell^2=0$, so they are points of the larger space. Their linear projections onto $\widetilde V$ equal $s$, and their Euclidean heights above or below the original space have magnitude $\ell$.
>
> For any local point $x\in\widetilde V$,
>
> $$
> x\cdot q_\pm=x\cdot s
> =-\frac{(x-s_0)^2+\ell^2}{2}<0
> $$
>
> Both external points have the same inner products with points of the original space as the element $s$. $\square$

An element of negative norm is orthogonal to no local point of the original space. It can, however, be orthogonal to another nonlocal element. For example, the elements

$$
s=s_0-\frac{\ell^2}{2}z,\qquad
t=s_0+\frac{\ell^2}{2}z
$$

have a common center, opposite norms, and satisfy $s\cdot t=0$. Only $t$ defines a real sphere here, so algebraic orthogonality does not mean the intersection of two real surfaces. Two elements of strictly negative norm cannot be orthogonal: the right-hand side of (3) is always negative.

## The inner product of a vector and an element

> [!info] The product is determined by the center
> **Theorem.** For a vector $v$, that is, an object satisfying $v\cdot z=0$, and any element $s$,
>
> $$
> \boxed{v\cdot s=v\cdot s_0}
> $$
>
> With the center fixed, changing the norm of the element does not affect its inner product with a vector.

> [!note]- Proof
> **Proof.** By (1), $v\cdot s=v\cdot s_0+s^2(v\cdot z)/2=v\cdot s_0$. $\square$

### A vector between two points and the perpendicular bisector

Let $v=b-a$, where $a,b$ are distinct local points. By (2),

$$
\boxed{(b-a)\cdot s
=\frac{(a-s_0)^2-(b-s_0)^2}{2}}
$$

Therefore $v\cdot s=0$ if and only if the center $s_0$ is equidistant from $a$ and $b$. In the plane, these centers form the perpendicular bisector of the segment $ab$; in three-dimensional space, they form the plane perpendicular to the segment through its midpoint. The norm of the element $s$ is arbitrary.

![Orthogonality of an element to a vector between two points depends on the center position and not on the radius](Vector%20and%20Sphere%20Element.svg)

*Left: two elements of positive norm have a common center on the perpendicular bisector, so both are orthogonal to $v=b-a$ despite their different radii. Right: the center is shifted toward $b$. Its distance to $b$ is smaller than its distance to $a$, and the product is positive. A shift toward $a$ makes it negative.*

This condition describes the position of the center relative to the vector; it does not mean that the arrow intersects the sphere surface at a right angle. For nonlocal endpoints $a,b$, formula (3) gives an additional term:

$$
(b-a)\cdot s
=\frac{b^2-a^2+(a_0-s_0)^2-(b_0-s_0)^2}{2}
$$

Thus the zero level is generally shifted relative to the perpendicular bisector hyperplane of the centers $a_0,b_0$.

### An arbitrary vector

In the coordinate model, choose a local point $p_0$ and the Euclidean space $E=\{p_0,z\}^\perp$. Any vector and any local center can be written as

$$
v=w+\beta z,\qquad
s_0=p_0+q-\frac{q^2}{2}z,\qquad w,q\in E
$$

Then

$$
v\cdot s=w\cdot q+\beta
$$

For $w\ne0$, the condition $v\cdot s=0$ defines a hyperplane of centers perpendicular to $w$. The parameter $\beta$ determines its position. If $v=\beta z\ne0$, then $v\cdot s=\beta$ for every element, so no element is orthogonal to it. The zero vector is orthogonal to every element.

**Connection with the null vector.** Adding a multiple of $z$ to a vector preserves its inner products with all vectors but changes its product with every element:

$$
(v+\lambda z)\cdot s=v\cdot s+\lambda
$$

When working with elements, a vector therefore cannot be replaced by just its direction and length in the displacement space without losing information. Its component along $z$ determines the position of the zero hyperplane; the geometric meaning of translation is explained in the [[The Null Vector, Isotropic Representation, and the Boundary#The normal and the null vector|section on the normal]].

## What selecting the center preserves

Replacing elements by their centers changes the inner product of the elements themselves according to (3). For differences, however,

$$
\boxed{(s-t)^2=(s_0-t_0)^2}
\tag{4}
$$

This is the squared distance between the centers; in resistance geometry, it has the units of resistance. Distinct elements with the same center have a difference of zero norm. Therefore (4) specifies distance between centers but does not distinguish all elements of $\mathcal H$.

> [!note]- Preservation of the norm of a difference
> **Proof.** One has $s-t=s_0-t_0+(s^2-t^2)z/2$. Since $(s_0-t_0)\cdot z=0$ and $z^2=0$, the term along $z$ does not affect the norm. $\square$

### Why the projection is nonlinear

The map $\pi$ fixes local points and satisfies $\pi(\pi(s))=\pi(s)$. It does not, however, preserve affine combinations. For any elements $s,t$ and $\theta\in\mathbb R$,

$$
\pi((1-\theta)s+\theta t)
=(1-\theta)\pi(s)+\theta\pi(t)+\frac{\theta(1-\theta)}2(s-t)^2z
$$

This follows by expanding the norm of the combination. In particular, for distinct local points $a,b$,

$$
\pi\left(\frac{a+b}{2}\right)
=\frac{a+b}{2}+\frac{(a-b)^2}{8}z
$$

Preservation of (4) therefore does not make $\pi$ a linear or affine projection. Linear orthogonal projection onto a subspace and nonlinear selection of the center perform different tasks; they are compared in the [[Decomposing a Form into Atomic and Difference Parts#Coordinates in the isotropic extension|section on projection]].

## Inner products of vectors

Replacing the endpoints by their centers changes their difference only by a multiple of $z$. This term is orthogonal to every vector of weight $0$, including $z$ itself, so it does not change their inner products. This is the reason for the next identity.

> [!info] Inner products of vectors
> **Theorem.** For any $a_0,a_1,b_0,b_1\in\mathcal H$,
>
> $$
> (a_1-a_0)\cdot(b_1-b_0)
> =(\pi(a_1)-\pi(a_0))\cdot(\pi(b_1)-\pi(b_0))
> $$
>
> Consequently, the norms of the endpoints do not affect the norms and inner products of vectors when the centers of the endpoints remain fixed.

> [!note]- Proof
> **Proof.** Selecting the centers changes each difference only by a multiple of $z$. For any $u,v\in z^\perp$ and $\alpha,\beta\in\mathbb R$,
>
> $$
> (u+\alpha z)\cdot(v+\beta z)=u\cdot v
> $$
>
> This follows from $u\cdot z=v\cdot z=z^2=0$. $\square$

The statement also holds for arbitrary combinations of zero weight. If $\sum_i\alpha_i=\sum_j\beta_j=0$, then

$$
\left(\sum_i\alpha_ia_i\right)\cdot\left(\sum_j\beta_jb_j\right)
=\left(\sum_i\alpha_i\pi(a_i)\right)\cdot\left(\sum_j\beta_j\pi(b_j)\right)
$$

**The condition is essential.** Changing norms with centers fixed means replacing $a_i\mapsto a_i+\lambda_i z$. The inner products of the endpoints themselves then change consistently:

$$
(a_i+\lambda_i z)\cdot(a_j+\lambda_j z)
=a_i\cdot a_j+\lambda_i+\lambda_j
$$

Arbitrarily changing only the diagonal entries of the Gram matrix is not such a replacement and generally changes the norms of differences.

## Higher-grade boundaries

The inner product of boundaries is a determinant of inner products of their constituent vectors. Passing to centers preserves every entry of this matrix and therefore its determinant. This extends the vector result to areas and volumes.

For elements $a_0,\ldots,a_k$, the boundary formula remains

$$
B=(a_0\ldots a_k)=\bigwedge_{i=1}^k(a_i-a_0)
$$

Write $h_i=\pi(a_i)$ and $B_h=(h_0\ldots h_k)$. Boundaries use the same operator $\partial$ as in the [[The Null Vector, Isotropic Representation, and the Boundary#The boundary operator as contraction with $z$|note on the null vector]].

> [!info] Higher-grade boundaries
> **Theorem.** Replacing vertices by their local centers preserves the norms of boundaries of every grade and the inner products of any two boundaries of the same grade:
>
> $$
> \boxed{B^2=B_h^2,\qquad B\cdot C=B_h\cdot C_h}
> \tag{5}
> $$
>
> In the second identity, the boundary $C$ may be formed from a different set of elements.

> [!note]- Proof for decomposable boundaries and their sums
> **Proof.** For decomposable boundaries, the inner product is the mixed Gram determinant:
>
> $$
> B\cdot C=\det\bigl((a_i-a_0)\cdot(b_j-b_0)\bigr)_{i,j=1}^k
> $$
>
> Every matrix entry is preserved by the theorem on vectors, so the determinant is preserved. Taking $C=B$ gives equality of norms. For fixed linear combinations of boundaries, the result follows by bilinearity. In grade $0$, the replacement leaves scalars unchanged. $\square$

The statement therefore includes nondecomposable boundaries. In particular, it preserves the squared areas and volumes of simplices of centers, calculated as $B^2/(k!)^2$.

### What happens to the objects and forms themselves

Equal norms do not imply equal exterior structures. Expanding the factors gives

$$
B-B_h=z  K,\qquad K\in\Lambda^{k-1}(z^\perp)
$$

All terms containing two factors $z$ vanish. For any boundary $C\in\Lambda^k(z^\perp)$, one has $(z  K)\cdot C=0$: the determinant of inner products contains a zero row. This explains why the metric evaluation is preserved while the object changes.

The forms $[B,C]$ and $[B_h,C_h]$ need not coincide either. Their numerical evaluations $B\cdot C$ and $B_h\cdot C_h$ coincide. The same applies to sums of forms and products of forms on boundaries: their exterior arguments lie in powers of $z^\perp$, where additional terms containing $z$ do not affect the evaluation.

This restriction matters. In the full exterior algebra of the extension, $z$ is not orthogonal to every element. For example, for a local point $a$, one has $(z  a)^2=-1$. The result therefore does not extend to arbitrary simplices and forms outside the boundary subalgebra. The core metric identity through normalized potentials likewise does not automatically extend to all forms of the extended space.

## Local basis vertices do not restrict the graph model

> [!info] Local basis vertices do not restrict the graph model
> **Corollary.** Let $a_1,\ldots,a_n$ be elements, and let their local centers $h_i=\pi(a_i)$ form the resistance simplex of a connected graph with positive coupling strengths. Replacing $a_i\mapsto h_i$ preserves the resistance metric and gives an isomorphic representation of the algebra of forms on boundaries. The Laplacian and its exponential map to the corresponding forms on local vertices with the same coupling strengths.
>
> Thus the basis vertices can be chosen local without restricting the graph model under consideration. Their individual norms are additional data of the realization and are not determined by the metric on boundaries.

> [!note]- A linear change of the fixed basis
> **Proof.** In the minimal extension of dimension $n+1$, the elements $a_1,\ldots,a_n,z$ form a basis: independence follows from the affine independence of the spatial coordinates of their centers. The linear map $F$ on this basis is defined by:
>
> $$
> F(a_i)=h_i=a_i-\frac{a_i^2}{2}z,\qquad F(z)=z
> $$
>
> Its matrix is triangular with unit diagonal, so $F$ is invertible. It preserves affine weight. Its extension to the exterior algebra therefore commutes with the boundary operator: $\partial F=F\partial$.
>
> For any $u\in z^\perp$, the difference $F(u)-u$ is a multiple of $z$. Hence $F(u)\cdot F(v)=u\cdot v$ for $u,v\in z^\perp$. The determinant formula and bilinearity then show that inner products of boundaries of every grade are preserved.
>
> Extend the map to forms by $F([X,Y])=[F(X),F(Y)]$. It preserves the product of forms and the identity form. With the coefficients $c_{ij}$ fixed, one obtains
>
> $$
> L_a=\sum_{i<j}c_{ij}[a_j-a_i]^2,\qquad
> F(L_a)=L_h=\sum_{i<j}c_{ij}[h_j-h_i]^2
> $$
>
> $$
> F(\exp L_a)=\exp L_h
> $$
>
> The spanning-tree form $[(a_1\ldots a_n)]^2$ maps to $[(h_1\ldots h_n)]^2$. Consequently, coefficients relative to the respective spanning-tree forms, potentials, and normalized potentials of corresponding forms on boundaries are preserved. $\square$

**Remark on the two maps.** The linear map $F$ agrees with $\pi$ on the chosen basis vertices, but not on all elements of unit weight. If $p=\sum_i\alpha_ia_i$ and $\sum_i\alpha_i=1$, then

$$
F(p)=p-\frac12\left(\sum_i\alpha_ia_i^2\right)z,\qquad
\pi(p)=p-\frac{p^2}{2}z
$$

These elements have the same local center, but $F(p)$ need not be local. The linear change of a fixed basis provides the algebraic correspondence, whereas the nonlinear map $\pi$ selects the center of each individual element.

Isomorphism does not mean literal equality $L_a=L_h$ within the extended algebra. The structure and metric evaluations of forms on boundaries are preserved; the metric of the entire vertex space and the inner products of the vertices themselves generally change.

## The geometric model extends beyond positively weighted graphs

There are two distinct extensions of the graph description here.

First, even with the resistance metric fixed, it is possible to consider all elements $s=s_0+s^2z/2$, rather than only local vertices. Their norms matter for describing spheres, orthogonality conditions with points, and inner products of the elements themselves. Passing to centers preserves the metric on boundaries but discards each element's norm $s^2$. Thus freedom to choose the norms of basis vertices does not mean that the norms of all geometric objects lack content.

Second, a positive definite displacement metric can itself be specified independently of a graph. Not every Euclidean simplex is the resistance simplex of a graph with positive coupling strengths: the recovered Laplacian matrix must have nonpositive off-diagonal entries, as stated in the [[Core specification#The distance operator|core specification]]. Positivity of couplings is an additional condition of the graph model, rather than a condition for defining an arbitrary Euclidean simplex.

The geometric description therefore covers a broader class of metrics and objects. This is not simply a claim about a greater dimension: for a graph on $n$ vertices, the minimal extension with $z$ has dimension $n+1$.

In this note, the displacement metric remains positive definite, although the extended metric has signature $(d+1,1)$ and elements may have norms of any sign. Arbitrary signs of coupling strengths do not by themselves guarantee positivity or nondegeneracy of the displacement metric. Graphs with couplings of both signs and geometries with an indefinite displacement metric require separate conditions; results for positively weighted graphs do not automatically extend to them.


## Example: nonlocal vertices and an unchanged boundary norm

For the local vertices of the same path $a-b-c$, define the elements

$$
a'=a+z,\qquad b'=b-2z,\qquad c'=c+3z
$$

Their centers are $a,b,c$, and their norms are $2,-4,6$. The inner product $a'\cdot b'=-3/2$ differs from $a\cdot b=-1/2$. Direct calculation nevertheless gives

$$
(b'-a')^2=1,\qquad (c'-a')^2=2,\qquad (b'-a')\cdot(c'-a')=1
$$

Therefore

$$
(a'b'c')^2=\det\begin{pmatrix}1&1\\1&2\end{pmatrix}=1=(abc)^2
$$

The squared area of the triangle of centers is $1/4$. The boundaries themselves differ:

$$
(a'b'c')-(abc)=z \bigl(-3(c-a)-2(b-a)\bigr)
$$

The additional term is nonzero but orthogonal to every grade-$2$ boundary in $\Lambda^2(z^\perp)$.

## Status of the results and continuation

Decomposition (1), the spherical interpretation (2), the change in inner product (3), and invariance (4)-(5) are proved under the stated assumptions. The corollary on choosing local basis vertices additionally establishes the correspondence between Laplacians, their exponentials, and potentials of forms on boundaries. The numerical example was calculated directly from the bilinear metric of the extension. In the previous revision, additional checks using exact rational arithmetic covered the formula for selecting the center of an affine combination, the metric identities for vectors, and 226 mixed Gram determinants of boundaries in a model with a three-dimensional displacement space. These checks control formulas and signs; the general theorems rest on their proofs. The formulas for sphere orthogonality, the representation of negative norm, and the product of a vector and an element are derived above from (1)-(3). The note contains no working conjectures.

Representation of a sphere by an element is established in conformal geometric algebra. The comparison uses [H. Li, D. Hestenes, A. Rockwood, *Generalized Homogeneous Coordinates for Computational Geometry*](https://davidhestenes.net/geocalc/pdf/CompGeom-ch2.pdf), §2.3, equations (2.38)-(2.42). The source uses $x\cdot e=-1$, so $z$ as used here corresponds to $-e$. In the source, $\rho$ denotes the linear radius. In this note, the norm of an arbitrary element is denoted by $s^2$; the notation $s_G^2=\rho(G)=R_{\mathrm{sph}}^2$ is used only for the circumsphere of a graph. The Clifford product is not identified with the product of PMG forms.

This note completes the geometric foundation needed to study a graph's resistance radius and diameter. Their behavior under changes in couplings and their dimensionless combinations with other parameters belong to the series on metric parameters. The reciprocal $1/D_{\mathrm{res}}$ does not by itself acquire the electrical interpretation of conductance between specified terminals: such an interpretation requires a separate justification.

Next: [[Bi-coordinates and Di-coordinates]]. Navigation: [[en/Resistance Geometry and Duality/Spaces/Spaces|Spaces]].

