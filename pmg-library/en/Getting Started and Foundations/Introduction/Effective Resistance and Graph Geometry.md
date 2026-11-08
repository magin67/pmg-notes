---
title: Effective Resistance and Graph Geometry
date: 2026-10-03
updated: 2026-11-08
revision: 11
translated_revision: 13
source_revision: 13
status: draft
text_prepared_by: ChatGPT
translation_key: effective-resistance-graph-geometry
lang: en
description: The Green matrix and distance operator in resistance calculations. Two-point and affine vectors, the resistance simplex, and the distinction between resistance and distance.
order: "2"
aliases:
  - "en/Introduction/Effective Resistance and Graph Geometry"
---

In the Euclidean geometry of a graph, effective resistance is interpreted as the squared distance between vertices. The distance itself is the square root of the resistance. Effective resistance was introduced in [[Laplacian - graph, electrical network and quadratic form|Laplacian: graph, electrical network and quadratic form]]; here we examine its geometric meaning.

Resistances can be calculated from the Laplacian through the Green matrix. We first obtain this matrix by taking the pseudoinverse of the Laplacian, then apply the distance operator. We then define inner products of graph vectors and show why resistances equal squared lengths.

We consider a finite connected undirected graph without loops on $n\ge2$ vertices. Existing edges have positive coupling strengths; for absent edges, $c_{ij}=0$. The Laplacian matrix is denoted by $L$.

In PMG, the norm of a vector is $u\cdot u$, its squared Euclidean length; the square root is called its linear norm. In the resistance metric, the norm of a vertex-pair vector equals effective resistance.

## The Green matrix

The Laplacian computes differences between values at neighboring vertices, taking the coupling strengths into account. Adding the same number to every value leaves the result unchanged. Hence the original collection of values cannot be recovered uniquely from the result of applying $L$, and the ordinary inverse $L^{-1}$ does not exist.

> [!info] Green matrix
> **Definition.** The Green matrix of a graph is the Moore-Penrose pseudoinverse of its Laplacian:
>
> $$
> \mathrm{Gr}=L^+
> $$
>
> The symbol $+$ denotes pseudoinversion, which also applies to matrices with no ordinary inverse.

To explain its action, subtract the mean from a collection of values to obtain a collection whose sum is zero. For example, subtracting the mean $2$ from $(3,1,2)$ gives $(1,-1,0)$. This operation is called **centering**.

For a connected graph, the Laplacian is uniquely invertible on collections with zero sum. The Green matrix performs this inversion. It sends a collection of equal values, such as $(2,2,2)$, to zero.

Let $\mathbf1$ denote the column of $n$ ones. Collections of values are written as columns when multiplying matrices. The Green matrix then has the properties

$$
\mathrm{Gr}Lu=L\mathrm{Gr}u=u
\quad\text{when }\sum_i u_i=0,
\qquad \mathrm{Gr}(\alpha\mathbf1)=0
$$

For an arbitrary collection $u$, both compositions subtract its mean:

$$
\mathrm{Gr}^{\mathsf T}=\mathrm{Gr},\qquad
L\mathrm{Gr}=\mathrm{Gr}L=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

Here $I$ is the identity matrix, and $\alpha\mathbf1$ has every entry equal to $\alpha$. The Green matrix has rank $n-1$ and is positive definite on nonzero collections with zero sum: for these, $u^{\mathsf T}\mathrm{Gr}u>0$. It is positive semidefinite on all collections.

In an electrical network, $J_i$ is the current supplied externally to vertex $i$; it is negative when current is withdrawn. The condition $\sum_iJ_i=0$ means that the total supplied current equals the total withdrawn current. The solution of $L\varphi=J$ with zero sum of potentials is

$$
\varphi=\mathrm{Gr}J,\qquad \sum_i\varphi_i=0
$$

## The distance operator

To obtain resistances from the Green matrix, we need the following operation on matrix entries.

> [!info] Distance operator
> **Definition.** For a symmetric matrix $A$, the distance operator $\mathcal D$ is defined by
>
> $$
> \mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}
> $$

For each pair of indices, add the two diagonal entries and subtract twice $A_{ij}$. The result is a symmetric matrix with zero diagonal. The operator is linear: it respects matrix addition and scalar multiplication.

Its name comes from the squared-length formula for a difference of vectors. If $A_{ij}=p_i\cdot p_j$, then

$$
\mathcal D(A)_{ij}=p_i\cdot p_i+p_j\cdot p_j-2p_i\cdot p_j
=\|p_j-p_i\|^2
$$

Thus the matrix of inner products, or **Gram matrix**, becomes a matrix of squared distances. For an arbitrary symmetric matrix $A$, no geometric meaning of the result is assumed.

## Resistance through the Green matrix

Apply the distance operator to the Green matrix.

> [!info] Effective resistances and the resistance matrix
> **Definition.** The effective resistance between vertices $i,j$ is
>
> $$
> R_{ij}=\mathcal D(\mathrm{Gr})_{ij}
> =\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
> \tag{1}
> $$
>
> The matrix $R=(R_{ij})$ is called the **resistance matrix**. The entire calculation from the Laplacian is therefore
>
> $$
> R=\mathcal D(\mathrm{Gr})=\mathcal D(L^+)
> $$

For $i=j$, the formula gives $R_{ii}=0$. For distinct vertices, we can explain its electrical meaning by injecting a unit current at vertex $j$ and withdrawing it at $i$. In the collection $J$, the entry at $j$ is $1$, the entry at $i$ is $-1$, and the others are zero. Hence $\varphi=\mathrm{Gr}J$ gives

$$
\varphi_k=\mathrm{Gr}_{kj}-\mathrm{Gr}_{ki}
$$

The potential difference between the injection and withdrawal vertices is

$$
\varphi_j-\varphi_i
=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ji}-\mathrm{Gr}_{ij}+\mathrm{Gr}_{ii}
=R_{ij}
$$

The last equality uses the symmetry of the Green matrix. For unit current, this potential difference is the effective resistance. Forward and inverse matrix transformations are discussed in [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

## Euclidean geometry of the graph

In the algebraic description, vertices are elements of weight $1$. A geometric drawing depicts their locations as points; the norms of their position vectors are not the norms of the elements themselves. Below, the metric is defined only on differences. Choosing vertices to be local points of zero norm is explained in the [[The Null Vector, Isotropic Representation, and the Boundary|isotropic model]].

We treat the vertices as points $a_1,\ldots,a_n$. Their positions in an arbitrary drawing of the graph do not yet specify distances: the drawing usually shows only which edges are present. To define lengths and angles, we specify an inner product of graph vectors.

> [!info] Vertex-pair vector
> **Definition.** The vector from vertex $a_i$ to vertex $a_j$ is
>
> $$
> a_{ij}=a_j-a_i
> $$
>
> It is called a vertex-pair vector, and is defined whether or not an edge is present.

Vertex-pair vectors are a special case of **affine vectors** $u=\sum_i u_i a_i$ with $\sum_i u_i=0$. Here the $u_i$ are numerical coefficients at vertices. We treat the vertices as independent in these formal linear combinations. For $a_{ij}$, the nonzero coefficients are $-1$ and $1$. A general affine vector may involve more vertices, for example $a_1+a_2-2a_3$. The zero-sum condition is essential: an arbitrary linear combination of vertices need not be an affine vector. See the [[Basic Objects and Operations of Polyform Algebra#Points and affine vectors|definition of points and affine vectors]] for details.

> [!info] Resistance inner product
> **Definition.** For affine vectors $u=\sum_i u_i a_i$ and $v=\sum_i v_i a_i$, set
>
> $$
> u\cdot v=\sum_{i,j}u_i\mathrm{Gr}_{ij}v_j
> $$

This inner product is positive definite: the coefficients of an affine vector sum to zero, and the Green matrix is positive definite on such nonzero collections. The resulting metric is therefore Euclidean.

Choose the origin at the **centroid**, the average of all vertices:

$$
h=\frac1n\sum_i a_i,\qquad p_i=a_i-h
$$

The vectors $p_i$ point from the centroid to the vertices and satisfy $\sum_i p_i=0$. In $p_i$, the coefficient of $a_i$ is $1-1/n$ and all other coefficients are $-1/n$. Substituting these coefficients into the inner product and using the zero row and column sums of $\mathrm{Gr}$ gives

$$
p_i\cdot p_j=\mathrm{Gr}_{ij}
\tag{2}
$$

Thus the Green matrix is the Gram matrix of the vectors $p_i$. In this note, $p_i$ denotes a vector, not a numerical value assigned to a vertex.

> [!note]- Euclidean coordinates from eigenvectors
> **Construction.** Let $q_1,\ldots,q_{n-1}$ be orthonormal eigenvectors of $L$ with nonzero eigenvalues $\lambda_1,\ldots,\lambda_{n-1}>0$. Their coordinates sum to zero. Pseudoinversion replaces nonzero eigenvalues by their reciprocals and leaves the zero eigenvalue unchanged:
>
> $$
> \mathrm{Gr}=\sum_{\alpha=1}^{n-1}\lambda_\alpha^{-1}q_\alpha q_\alpha^{\mathsf T}
> $$
>
> If $q_{\alpha i}$ is the $i$th coordinate of $q_\alpha$, coordinates of the centered vectors $p_i$ can be chosen as
>
> $$
> p_i=\left(\frac{q_{1i}}{\sqrt{\lambda_1}},\ldots,\frac{q_{n-1,i}}{\sqrt{\lambda_{n-1}}}\right)
> $$
>
> The ordinary Euclidean inner products of these coordinate collections equal $\mathrm{Gr}_{ij}$, and their sum is zero. $\square$

Subtracting the centroid preserves differences: $a_{ij}=a_j-a_i=p_j-p_i$. By (1) and (2),

$$
\begin{aligned}
\|a_{ij}\|^2&=\|p_j-p_i\|^2\\
&=p_i\cdot p_i+p_j\cdot p_j-2p_i\cdot p_j\\
&=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}=R_{ij}
\end{aligned}
$$

> [!info] Resistance and the length of a vertex-pair vector
> **Theorem.** In the graph's Euclidean resistance metric,
>
> $$
> R_{ij}=\|a_{ij}\|^2,\qquad \|a_{ij}\|=\sqrt{R_{ij}}
> \tag{3}
> $$
>
> Thus resistance equals the squared distance between vertices.

## Dimension and the resistance simplex

The rank of a Gram matrix equals the dimension of the linear span of its vectors. Hence $p_1,\ldots,p_n$ span a space of dimension $n-1$.

The origin is the centroid of the points and belongs to their affine hull. The affine hull therefore also has dimension $n-1$: the points $a_1,\ldots,a_n$ are affinely independent.

A simplex generalizes a segment, a filled triangle, and a solid tetrahedron. For vertices $a_1,\ldots,a_n$, it consists of all points $\sum_i t_i a_i$ with $t_i\ge0$ and $\sum_i t_i=1$. If $a_2-a_1,\ldots,a_n-a_1$ are linearly independent, the simplex is nondegenerate and has dimension $n-1$.

> [!info] Resistance simplex
> **Definition.** A simplex with vertices $a_1,\ldots,a_n$ satisfying (3) is called the resistance simplex of the graph. For a connected graph, it is nondegenerate and has dimension $n-1$.

Its geometry is uniquely determined up to a Euclidean isometry: a translation and an orthogonal transformation. The distance is defined between any two vertices, whether or not an edge joins them.

## Example: a three-vertex path

Consider a path with coupling strengths $c_{12}=1$ and $c_{23}=2$.

![A path and its resistance simplex](Path%20and%20resistance%20triangle.svg)

The left panel shows the couplings and their strengths; the right panel shows the resistance simplex of the same graph. Labels on the right give **lengths** $\sqrt{R_{ij}}$. The dashed side joins vertices $1$ and $3$, which have no direct edge in the original graph.

> [!example] Resistances and the Green matrix
> The individual edge resistances are $1/c_{12}=1$ and $1/c_{23}=1/2$. When current is passed between the endpoints of the path, the two edges are in series, so $R_{13}=3/2$. When current is passed between adjacent vertices, the remaining edge carries no current. Thus,
>
> $$
> R_{12}=1,\qquad R_{23}=\frac12,\qquad R_{13}=\frac32
> $$
>
> The Laplacian and Green matrix are
>
> $$
> L=\begin{pmatrix}
> 1&-1&0\\
> -1&3&-2\\
> 0&-2&2
> \end{pmatrix},\qquad
> \mathrm{Gr}=\begin{pmatrix}
> \frac12&-\frac16&-\frac13\\
> -\frac16&\frac16&0\\
> -\frac13&0&\frac13
> \end{pmatrix}
> $$
>
> Direct multiplication gives $\mathrm{Gr}\mathbf1=0$ and $L\mathrm{Gr}=I-\mathbf1\mathbf1^{\mathsf T}/3$. Formula (1) independently reproduces the electrical calculation:
>
> $$
> R_{12}=\frac12+\frac16+\frac13=1,\qquad
> R_{23}=\frac16+\frac13=\frac12
> $$
>
> $$
> R_{13}=\frac12+\frac13+\frac23=\frac32
> $$

> [!example] Coordinates and a right angle
> Choose the following coordinates for the vertices:
>
> $$
> a_2=(0,0),\qquad a_1=(1,0),\qquad
> a_3=\left(0,\frac1{\sqrt2}\right)
> $$
>
> The squared distances are $1$, $1/2$, and $3/2$. The points form a right triangle with the right angle at $a_2$, since
>
> $$
> \|a_{13}\|^2=\|a_{12}\|^2+\|a_{23}\|^2
> $$
>
> These coordinates are not centered. After subtracting the centroid $(1/3,1/(3\sqrt2))$, the centered vectors $p_i$ have the Gram matrix $\mathrm{Gr}$ displayed above.

The path diagram and its resistance simplex have different geometric meanings. The diagram shows which connections are present; the simplex represents the resistances of the entire network as squared Euclidean distances.

## Two metrics on the vertices

Formula (3) shows that $\sqrt{R_{ij}}$ is a Euclidean distance. The resistance $R_{ij}$ itself also satisfies the metric axioms, but this requires a separate argument: squares of arbitrary Euclidean distances can violate the triangle inequality.

> [!info] Resistance distance
> **Theorem.** For a connected graph, $R_{ij}=R_{ji}$, $R_{ij}>0$ for $i\ne j$, $R_{ii}=0$, and
>
> $$
> R_{ij}\le R_{ik}+R_{kj}
> $$
>
> Effective resistance therefore defines a metric on the vertex set, called resistance distance.

> [!note]- Proof of the triangle inequality
> **Proof.** Symmetry and positivity follow from (1) and the positive definiteness of the resistance inner product. For the triangle inequality, it suffices to consider distinct $i,j,k$.
>
> Inject a unit current at $j$ and withdraw it at $k$. The potential at each vertex $v$ is then $\varphi_v=\mathrm{Gr}_{vj}-\mathrm{Gr}_{vk}$. At every other vertex $v$, the potential is a weighted average of the potentials at its neighbors:
>
> $$
> \varphi_v=\frac{\sum_w c_{vw}\varphi_w}{\sum_w c_{vw}}
> $$
>
> The minimum potential is attained at $k$. Indeed, $j$ cannot be a minimum because $(L\varphi)_j=1>0$. If the minimum is attained at another vertex, equality with the weighted average forces all its neighbors to have the same potential. By connectedness, propagation of this equality reaches one of the two current terminals, which can only be $k$. Hence $\varphi_i-\varphi_k\ge0$.
>
> Substituting (1) gives
>
> $$
> \begin{aligned}
> R_{ik}+R_{kj}-R_{ij}
> &=2(\mathrm{Gr}_{kk}-\mathrm{Gr}_{ik}-\mathrm{Gr}_{kj}+\mathrm{Gr}_{ij})\\
> &=2(\varphi_i-\varphi_k)\ge0
> \end{aligned}
> $$
>
> If any indices coincide, the inequality follows from $R_{ii}=0$ and the nonnegativity of resistances. $\square$

Thus resistance distance $R_{ij}$ and the distance $\sqrt{R_{ij}}$ in the resistance simplex are two different metrics on the same vertex set.

## Geometric changes when couplings are strengthened

Adding an edge with positive conductance or increasing the conductance of an existing edge cannot increase any effective resistance. This property is called Rayleigh monotonicity; its justification through the exact resistance variation formula is given in [[Variation of a Single Edge]].

By (3), pairwise distances in the resistance simplex also cannot increase. Some distances may remain unchanged: strengthening one coupling need not affect every measurement. When a coupling is weakened, resistances cannot decrease as long as the graph remains connected.

## Further reading

In [[Inner Product of Graph Vectors]], we pass from norms of $a_{ij}$ to inner products of two vertex-pair vectors. Electrically, these express the potential difference across one pair of vertices when a unit current is passed through another pair.

Sources on electrical networks and resistance geometry are collected in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the first section of the reading recommendations]].
