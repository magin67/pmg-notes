---
title: "Resistance Radius of a Set: Gram Matrix and Volume"
date: 2026-10-16
updated: 2026-10-16
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: resistance-radius-gram-matrix-and-volume
order: 2
description: "The radius and center coordinates from the Gram matrix of local points, the determinant's relation to volume and the spanning-tree coefficient, and monotonicity under passage to a subset."
---

The resistance radius can be considered for more than the full vertex set of a graph. Any subset, with its pairwise resistances preserved, defines its own simplex and circumsphere. The Gram matrix of the local points suffices to compute the radius; its determinant relates the radius to the volume of the simplex.

The normalizations $\rho=R_{\mathrm{sph}}^2$ and $D_{\mathrm{res}}=4\rho$ are introduced in [[Resistance Radius and Diameter of a Graph]]. Here we derive determinant formulas, check them on a segment, a triangle, and a tetrahedron, and prove monotonicity of the radius under passage to a subset. The geometric background is given in [[The Null Vector, Isotropic Representation, and the Boundary]] and [[Nonlocal Elements, Spheres, and Their Centers]].

## A set of points and two Gram matrices

Let $A=\{a_0,\ldots,a_l\}$ consist of $n=l+1\ge2$ local points in the isotropic representation. Their Euclidean coordinates $x_0,\ldots,x_l$ are assumed to be affinely independent. Equivalently, the differences $u_i=a_i-a_0$, $i=1,\ldots,l$, are independent and their metric is positive definite. In PMG, the norm is quadratic: $X^2=X\cdot X$; its square root, when the value is nonnegative, is called the linear norm.

These conditions hold for any subset of distinct vertices of a connected graph with positive conductances. The geometric statements below also hold for any nondegenerate Euclidean simplex. However, not every such simplex is the resistance simplex of a graph with nonnegative conductances.

Denote the squared pairwise distances by $R_{ij}=(a_i-a_j)^2$. For a set of graph vertices, these are the original resistances between the selected vertices. Since $a_i^2=0$, the Gram matrix of the local points is

$$
\mathbf G=(g_{ij})_{i,j=0}^l,\qquad g_{ij}=a_i\cdot a_j=-\frac12R_{ij}
$$

Thus $\mathbf G=-\mathbf R/2$. We denote the graph's Green matrix by $\mathbf{Gr}=\mathbf L^+$: it is the Gram matrix of the vectors from the vertices to the centroid, rather than of the local vertices themselves. For the full vertex set, $\mathbf{Gr}=\mathbf J\mathbf G\mathbf J$, where $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$ is the centering projector.

Adding the null vector to the set gives the extended Gram matrix

$$
\mathbf G_z=G(a_0,\ldots,a_l,z)
=\begin{pmatrix}\mathbf G&\mathbf1\\\mathbf1^{\mathsf T}&0\end{pmatrix}
$$

Its last row and column follow from $a_i\cdot z=1$ and $z^2=0$. The radius formulas below use $\mathbf G$, without the added row and column for $z$.

Denote the Gram matrix of the differences by $\mathbf G_u$:

$$
(\mathbf G_u)_{ij}=u_i\cdot u_j
=\frac{R_{0i}+R_{0j}-R_{ij}}2,
\qquad 1\le i,j\le l
$$

The matrix $\mathbf G_u$ is positive definite. It determines the ordinary $l$-dimensional volume of the simplex, $\mathrm{vol}(A)$:

$$
\det\mathbf G_u=(l!\,\mathrm{vol}(A))^2
$$

This is the [[From Lengths to Areas and Volumes#Volumes of parallelotopes and simplices|volume formula using the Gram matrix of differences]]. It differs from the determinant of $\mathbf G$, which concerns the local points themselves in the indefinite metric.

## The radius and center coordinates from the inverse Gram matrix

There is a unique circumsphere in the affine hull of $x_0,\ldots,x_l$. Denote its Euclidean center by $O_A$ and its squared linear radius by $\rho_A>0$. The center's bi-coordinates are defined by

$$
O_A=\sum_{i=0}^l\alpha_i x_i,
\qquad
\mathbf1^{\mathsf T}\boldsymbol\alpha=1
$$

In the isotropic representation, these coordinates specify the element $h_V=\sum_i\alpha_i a_i$. Its norm is $-\rho_A$, and its local center is $h=h_V+\rho_Az/2$. This distinction is established in the [[Nonlocal Elements, Spheres, and Their Centers#The center in the affine hull of the original vertices|note on spheres]]. The coordinates $\boldsymbol\alpha$ refer to $h_V$ and the Euclidean center $O_A$; representing the local point $h$ in the extended basis also requires a component along $z$.

> [!info] The radius and bi-coordinates of the center
> **Theorem.** Under the stated assumptions, the matrix $\mathbf G$ is invertible and
>
> $$
> \boxed{
> \rho_A=-\frac1{\mathbf1^{\mathsf T}\mathbf G^{-1}\mathbf1},
> \qquad
> \boldsymbol\alpha=
> \frac{\mathbf G^{-1}\mathbf1}{\mathbf1^{\mathsf T}\mathbf G^{-1}\mathbf1}
> }
> \tag{1}
> $$
>
> In particular, $\mathbf1^{\mathsf T}\mathbf G^{-1}\mathbf1<0$. The center coordinates need not be nonnegative.

> [!proof]- Invertibility and derivation of the formulas
> **Proof.** For every vertex, $(a_i-h_V)^2=\rho_A$. Locality of the vertices gives
>
> $$
> a_i\cdot h_V=\frac{h_V^2-\rho_A}{2}
> $$
>
> Multiplying by $\alpha_i$ and summing yields $h_V^2=-\rho_A$. Therefore
>
> $$
> a_i\cdot h_V=-\rho_A,
> \qquad
> u_i\cdot h_V=0
> $$
>
> The elements $h_V,u_1,\ldots,u_l$ form a basis of the linear span of the original local vertices: $h_V$ has affine weight $1$, while the $u_i$ form a basis of its zero-weight directions. The Gram matrix in this basis is $\operatorname{diag}(-\rho_A,\mathbf G_u)$ and is nonsingular. Hence $\mathbf G$ is also nonsingular and has signature $(l,1)$.
>
> The equalities $a_i\cdot h_V=-\rho_A$ can be written as $\mathbf G\boldsymbol\alpha=-\rho_A\mathbf1$. Inverting and normalizing the sum of the coordinates gives (1). $\square$

Since $\mathbf G^{-1}=-2\mathbf R^{-1}$, formula (1) gives $\rho_A=1/(2\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1)$. This expression in terms of the resistance matrix is also derived in [[Resistance Radius and Diameter of a Graph]].

The radial and diametral connectivities of the set are expressed through the sum of all entries of the inverse Gram matrix:

$$
\boxed{
c_{\mathrm{rad}}(A)=-\sum_{i,j}(\mathbf G^{-1})_{ij},
\qquad
c_{\mathrm{diam}}(A)=-\frac14\sum_{i,j}(\mathbf G^{-1})_{ij}
}
$$

These quantities equal $1/\rho_A$ and $1/(4\rho_A)$. Here “connectivity” denotes a metric parameter of PMG, not the minimum number of deletions needed to disconnect a graph.

The computation does not require the entire inverse matrix: it suffices to solve $\mathbf Gv=\mathbf1$, find $s=\sum_i v_i$, and set $\rho_A=-1/s$, $\boldsymbol\alpha=v/s$.

## Determinant, radius, and volume

**Definition.** Introduce the positive determinant parameter of the set

$$
g_A=-\det\mathbf G
$$

The sign matters. For the exterior object $\mathcal A=a_0\wedge\cdots\wedge a_l$, the induced metric of the isotropic space gives $\mathcal A^2=\det\mathbf G<0$. Thus $g_A=-\mathcal A^2$ is the negative of the exterior object's norm, rather than the norm itself under PMG conventions. Calling $g_A$ the “norm of the set” would require a separate naming convention; here we retain the determinant notation.

> [!info] The relation between radius and volume
> **Theorem.** For a nondegenerate set of $l+1$ local points,
>
> $$
> \boxed{
> g_A=\rho_A\det\mathbf G_u
> =\rho_A(l!\,\mathrm{vol}(A))^2
> }
> \tag{2}
> $$

> [!proof]- Proof using an orthogonal basis
> **Proof.** The change from $a_0,a_1,\ldots,a_l$ to $a_0,u_1,\ldots,u_l$ has determinant $1$: subtract $a_0$ from every vertex except the first. Next,
>
> $$
> h_V=a_0+\sum_{i=1}^l\alpha_i u_i
> $$
>
> Replacing $a_0$ by $h_V$ also has determinant $1$. The Gram determinant is therefore preserved. The proof of (1) established that $h_V$ is orthogonal to every $u_i$, so
>
> $$
> \det\mathbf G=\det\operatorname{diag}(-\rho_A,\mathbf G_u)
> =-\rho_A\det\mathbf G_u
> $$
>
> Substituting the volume formula proves (2). $\square$

In (2), the radius $\rho_A$ occurs to the first power. The equivalent expression in terms of the linear radius is

$$
g_A=(l!\,R_{\mathrm{sph}}\,\mathrm{vol}(A))^2
$$

Thus the expression $(l!\,\rho_A\,\mathrm{vol}(A))^2$ would contain an extra factor of $\rho_A$.

The formula also explains why the physical dimension of the radius is independent of the number of vertices. If the Gram entries have the dimension of resistance, then $g_A$ has the dimension of resistance to the power $l+1$, while $\det\mathbf G_u$ has resistance to the power $l$. Their ratio always has the dimension of resistance:

$$
\rho_A=\frac{g_A}{(l!\,\mathrm{vol}(A))^2}
$$

## Specialization to the full vertex set of a graph

Now let $A$ contain all vertices of a connected graph $G$ with positive conductances, with $l=n-1$. Its spanning-tree coefficient is

$$
\tau(G)=\sum_{T\text{ is a spanning tree}}\prod_{e\in T}c_e
$$

The [[From Lengths to Areas and Volumes#The volume of the full resistance simplex|note on volumes]] proves that $\mathbf G_u=\mathbf L_0^{-1}$, where $\mathbf L_0$ is obtained from the Laplacian by deleting the row and column of the reference vertex $0$. By the matrix-tree theorem, $\det\mathbf L_0=\tau(G)$. Consequently,

$$
\det\mathbf G_u=\frac1{\tau(G)},
\qquad
\mathrm{vol}(A)^2=\frac1{(l!)^2\tau(G)}
$$

Substituting into (2) gives

$$
\boxed{
g_A=\frac{\rho(G)}{\tau(G)},
\qquad
\rho(G)=-\tau(G)\det\mathbf G
}
\tag{3}
$$

For unit conductances, $\tau(G)$ is the number of spanning trees; for arbitrary conductances, it is a weighted sum and need not be an integer.

Formula (2) is geometric and applies to any set satisfying the stated assumptions. Formula (3) uses the full resistance simplex of a particular graph. For a proper subset, one cannot substitute the spanning-tree coefficient of the original graph or of the graph obtained by deleting the remaining vertices. If a graph interpretation is needed, the subset's metric is realized by [[Vertex Elimination and Induced Couplings|eliminating the remaining vertices through a Schur complement]]; the spanning-tree coefficient of the resulting induced graph is then used.

## Examples and normalization checks

### Two vertices: a segment

Let the resistance of the pair be $r>0$. Then

$$
\mathbf G=
\begin{pmatrix}0&-r/2\\-r/2&0\end{pmatrix},
\qquad
\mathbf G^{-1}=
\begin{pmatrix}0&-2/r\\-2/r&0\end{pmatrix}
$$

Direct computation gives

$$
g_A=\frac{r^2}{4},\qquad
\rho_A=\frac r4,\qquad
\boldsymbol\alpha=\begin{pmatrix}1/2\\1/2\end{pmatrix}
$$

The ordinary length of the segment is $\mathrm{vol}(A)=\sqrt r$, so $\rho_A\mathrm{vol}(A)^2=r^2/4=g_A$. Independently, the center of the segment is its midpoint, and its linear radius is $\sqrt r/2$.

### Three vertices: a triangle

Denote the ordinary linear side lengths by $a,b,c$ and the area by $S$. With a suitable ordering of the vertices,

$$
\mathbf G=-\frac12
\begin{pmatrix}
0&c^2&b^2\\
c^2&0&a^2\\
b^2&a^2&0
\end{pmatrix},
\qquad
\det\mathbf G=-\frac{a^2b^2c^2}{4}
$$

By (2), $g_A=\rho_A(2S)^2=4\rho_A S^2$. Therefore

$$
\boxed{a^2b^2c^2=16\rho_A S^2=4D_{\mathrm{res}}(A)S^2}
$$

This is the usual identity $abc=4R_{\mathrm{sph}}S$, squared. An independent geometric check is as follows: if the angle opposite side $a$ is $\theta$, then $S=bc\sin\theta/2$ and $a=2R_{\mathrm{sph}}\sin\theta$; eliminating $\sin\theta$ gives the stated identity.

For $K_3$ with unit conductances, $a^2=b^2=c^2=2/3$, $S^2=1/12$, and $\rho=2/9$. Direct evaluation of the determinant gives $g_A=2/27$, in agreement with $\rho/\tau=(2/9)/3$.

### Four vertices: a tetrahedron

For any nondegenerate tetrahedron with ordinary volume $V$, formula (2) becomes

$$
g_A=36\rho_A V^2
$$

If $\mathbf R$ contains the squares of the six edge lengths of the tetrahedron, then $\mathbf G=-\mathbf R/2$ and $\det\mathbf G=\det\mathbf R/16$. Hence

$$
\boxed{-\det\mathbf R=576\rho_A V^2}
$$

Here $\mathbf R$ is a $4\times4$ matrix with zero diagonal; it is not the bordered Cayley-Menger matrix.

For a **regular tetrahedron** with linear edge length $a$, the Gram matrix is

$$
\mathbf G=\frac{a^2}{2}(I_4-\mathbf1\mathbf1^{\mathsf T})
$$

It has eigenvalue $-3a^2/2$ on the constant column and eigenvalue $a^2/2$ of multiplicity $3$ on the zero-sum subspace. Directly,

$$
\det\mathbf G=-\frac{3a^8}{16},\qquad
\mathbf G^{-1}\mathbf1=-\frac{2}{3a^2}\mathbf1,
\qquad
\rho_A=\frac{3a^2}{8}
$$

All center coordinates equal $1/4$. An independent geometric check uses the tetrahedron's height $a\sqrt{2/3}$: the center divides it in the ratio $3:1$ measured from the vertex, so $R_{\mathrm{sph}}=a\sqrt6/4$. The base area is $\sqrt3a^2/4$, giving $V=a^3/(6\sqrt2)$. Thus

$$
36\rho_A V^2
=36\cdot\frac{3a^2}{8}\cdot\frac{a^6}{72}
=\frac{3a^8}{16}
=g_A
$$

For the resistance tetrahedron of $K_4$ with unit conductances, $a^2=1/2$. Its values are

$$
\rho=\frac3{16},\qquad
D_{\mathrm{res}}=\frac34,\qquad
V^2=\frac1{576},\qquad
g_A=\frac3{256}
$$

The reduced Laplacian is $4I_3-\mathbf1\mathbf1^{\mathsf T}$ and has determinant $16$. Therefore $\tau=16$ and $\rho/\tau=3/256$, as required by (3).

**An example without the symmetry of a regular simplex.** Take the tetrahedron with Euclidean vertices $0,e_1,e_2,e_3$, where the $e_i$ are orthonormal. This is the resistance simplex of the star $K_{1,3}$ with unit conductances. Its center is $O_A=(e_1+e_2+e_3)/2$, so $\rho_A=3/4$ and $V=1/6$. Direct computation gives

$$
\mathbf G=-\frac12
\begin{pmatrix}
0&1&1&1\\
1&0&2&2\\
1&2&0&2\\
1&2&2&0
\end{pmatrix},
\qquad
\det\mathbf G=-\frac34
$$

Thus $g_A=3/4=36\cdot(3/4)\cdot(1/36)$. The center's bi-coordinates are $(-1/2,1/2,1/2,1/2)$: the center lies outside the simplex, but all formulas remain valid.

## The radius of a subset and projection of the center

Let $C\subseteq A$ contain at least two vertices. We retain the original inner products and distances. The Gram matrix $\mathbf G_C$ is obtained by selecting the corresponding rows and columns of $\mathbf G_A$; $\det\mathbf G_C$ is a principal minor. In particular, deleting one vertex gives a principal submatrix of size $n-1$.

Denote the circumsphere centers in the respective Euclidean affine hulls by $O_A,O_C$.

> [!info] Monotonicity under passage to a subset
> **Theorem.** The center $O_C$ is the orthogonal projection of $O_A$ onto the affine hull of $C$, and
>
> $$
> \boxed{\rho_A=\rho_C+(O_A-O_C)^2}
> \tag{4}
> $$
>
> Consequently, $\rho_C\le\rho_A$, $D_{\mathrm{res}}(C)\le D_{\mathrm{res}}(A)$, and
>
> $$
> c_{\mathrm{rad}}(C)\ge c_{\mathrm{rad}}(A),
> \qquad
> c_{\mathrm{diam}}(C)\ge c_{\mathrm{diam}}(A)
> $$
>
> Equality holds if and only if $O_A$ lies in the affine hull of $C$; in that case, $O_C=O_A$.

> [!proof]- Proof using orthogonal projection
> **Proof.** Let $P$ be the orthogonal projection of $O_A$ onto the affine hull of $C$. For every vertex $x_i$ in $C$, the Pythagorean theorem gives
>
> $$
> \rho_A=(x_i-O_A)^2=(x_i-P)^2+(P-O_A)^2
> $$
>
> The last term is independent of the vertex, so $P$ is equidistant from all vertices of $C$. Affine independence of $C$ makes its center in its own affine hull unique: $P=O_C$. This gives (4). Positivity of the metric gives the inequality and the equality condition; for positive radii, taking reciprocals reverses the inequality. $\square$

For a face of a regular tetrahedron with edge length $a$, $\rho_C=a^2/3$, whereas $\rho_A=3a^2/8$. Their difference is $a^2/24$, equal to the squared distance from the tetrahedron's center to the plane of the face.

The decrease need not be strict. The circumcenter of a right triangle is the midpoint of its hypotenuse. Retaining only the endpoints of the hypotenuse preserves both the center and the radius.

For a single vertex, set $\rho_C=0$ and $O_C=x_i$; equality (4) remains valid. However, its Gram matrix is the zero $1\times1$ matrix, so the inverse formula (1) and finite reciprocal connectivities no longer apply.

## Which changes of the set the formulas cover

**A subset with the original metric.** Formula (4) concerns a single Euclidean realization: some points are removed, while the distances between the remaining points are preserved. This is geometric deletion, expressed through a principal submatrix of the Gram matrix. It does not mean an arbitrary graph minor obtained by deletions and contractions.

**Deleting a graph vertex and its edges.** This operation changes the Laplacian and generally the resistances between the remaining vertices; the graph may become disconnected. For example, in the path $a-b-c$ with unit conductances, the retained pair $a,c$ has $R_{ac}=2$ and $\rho=1/2$, the same radius as the full resistance triangle of the path. But deleting vertex $b$ together with its edges leaves two disconnected vertices, for which the previous finite effective resistance no longer exists.

**Identifying vertices and changing conductances.** These operations also change the metric and are outside the scope of the subset theorem. Monotonicity of the radius for these operations does not follow from (4). They will be considered in later notes of the series.

### If the original elements are nonlocal

Suppose $\mathbf G_p=(p_i\cdot p_j)$ is the Gram matrix of elements of unit weight in the same isotropic extension, but their norms $q_i=p_i^2$ may be nonzero. To compute the radius of the set of their local centers, first pass to $a_i=\pi(p_i)=p_i-q_i z/2$. By the [[Nonlocal Elements, Spheres, and Their Centers#What selecting the center preserves|formula for inner products of centers]],

$$
\mathbf G=\mathbf G_p-\frac12(q\mathbf1^{\mathsf T}+\mathbf1q^{\mathsf T}),
\qquad
R_{ij}=q_i+q_j-2(\mathbf G_p)_{ij}
$$

If the centers are affinely independent, all the geometric formulas above apply to $\mathbf G$. One cannot substitute $\mathbf G_p$ directly into (1) and (2): the norms of the original elements change its determinant and inverse, even though the metric of their differences agrees with that of the centers.

An arbitrary Gram matrix, without assumptions on weight, locality, and positivity of the metric on directions, does not guarantee the existence of a Euclidean circumsphere. For affinely dependent sets, a sphere may fail to exist or may exist in a lower dimension, but inversion of the full Gram matrix in the preceding form is inapplicable. These cases are not covered by the present theorems.

## Status of the results and continuation

The radius and coordinate formulas (1), the determinant identity (2), and subset monotonicity (4) are proved for nondegenerate Euclidean simplices in the local isotropic representation. The graph formula (3) additionally uses the identity $\det\mathbf G_u=1/\tau(G)$ proved in the introductory series.

For a segment, a triangle, a regular tetrahedron, and the star's tetrahedron, direct determinant calculations and geometric checks of the radius and volume are given. They check the determinant sign, the factors $4$ and $(l!)^2$, and the power of the radius, but do not replace the general proofs.

The formulas have also been checked using exact rational arithmetic: resistances were recovered from the inverse reduced Laplacian for a single edge and for $P_3$, $K_3$, $K_4$, and $K_{1,3}$ with unit conductances. The checks covered the radii, center coordinates, and equality $g_A=\rho_A/\tau(G)$ for the full sets, as well as identity (2) and nonincrease of the radius for all their subsets containing at least two vertices.

The center coordinates and other metric data will next be related to parameters of individual vertices and edges. The subset theorem prepares the analysis of the effect of eliminating one vertex; deleting a vertex together with its couplings will require separate consideration.
