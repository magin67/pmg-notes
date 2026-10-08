---
title: "Effective Resistance and Graph Geometry"
date: 2026-10-03
updated: 2026-10-08
revision: 2
source_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: effective-resistance-graph-geometry
lang: en
description: "The Green matrix as the Gram matrix of a resistance simplex. A Euclidean representation of graph vertices and the distinction between resistance and geometric distance."
---

Effective resistance, introduced in [[Laplacian - graph, electrical network and quadratic form|Laplacian: graph, electrical network and quadratic form]], admits a Euclidean representation. Graph vertices can be represented by points whose squared pairwise distances equal the effective resistances. This representation is constructed from the Green matrix of the Laplacian.

We consider a finite connected undirected graph without loops on $n\ge2$ vertices. Existing edges have positive conductances; for absent edges, $c_{ij}=0$. The Laplacian matrix is denoted by $L$.

## The Green matrix

The current equation is $L\varphi=J$, where $\varphi$ contains the vertex potentials and $J$ the external currents. Since $L\mathbf1=0$, the ordinary inverse $L^{-1}$ does not exist. Adding a common constant to all potentials leaves the currents unchanged.

Balanced external currents belong to the subspace

$$
H=\mathbf1^\perp=\left\{u\in\mathbb R^n:\sum_i u_i=0\right\}
$$

Here $\mathbf1$ is the column vector of ones, and orthogonality is taken with respect to the ordinary inner product in $\mathbb R^n$. For a connected graph, the restriction of $L$ to $H$ is positive definite and invertible.

> [!info] Green matrix
> **Definition.** The Green matrix $G$ inverts $L$ on $H$ and vanishes on constant columns:
>
> $$
> G|_H=(L|_H)^{-1},\qquad G\mathbf1=0
> $$
>
> It is the Moore-Penrose pseudoinverse: $G=L^+$.

The definition gives

$$
G^{\mathsf T}=G,\qquad LG=GL=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

where $I$ is the identity matrix. The matrix $G$ is positive semidefinite and has rank $n-1$. For any balanced $J$, the centered solution of the current equation is $\varphi=GJ$; centering means that $\sum_i\varphi_i=0$.

## Resistance through the Green matrix

Denote the standard coordinate columns by $\mathbf e_i$ and set

$$
\mathbf e_{ij}=\mathbf e_j-\mathbf e_i
$$

The column $\mathbf e_{ij}$ specifies a unit current injected at vertex $j$ and withdrawn at vertex $i$. The centered potentials are $\varphi=G\mathbf e_{ij}$. Hence

$$
R_{ij}=\varphi_j-\varphi_i
=\mathbf e_{ij}^{\mathsf T}G\mathbf e_{ij}
=G_{ii}+G_{jj}-2G_{ij}
\tag{1}
$$

For $i=j$, set $R_{ii}=0$. Formula (1) remains valid in this case.

## A Euclidean representation of the vertices

A positive semidefinite matrix is the Gram matrix of a family of Euclidean vectors. Thus there exist position vectors $x_1,\ldots,x_n$ in $\mathbb R^{n-1}$ such that

$$
x_i\cdot x_j=G_{ij}
\tag{2}
$$

> [!note]- Construction from eigenvectors
> **Proof.** Let $q_1,\ldots,q_{n-1}$ be an orthonormal basis of $H$ consisting of eigenvectors of $L$, with corresponding eigenvalues $\lambda_1,\ldots,\lambda_{n-1}>0$. Then
>
> $$
> G=\sum_{\alpha=1}^{n-1}\lambda_\alpha^{-1}q_\alpha q_\alpha^{\mathsf T}
> $$
>
> If $q_{\alpha i}$ denotes the $i$th coordinate of $q_\alpha$, we may choose
>
> $$
> x_i=\left(\frac{q_{1i}}{\sqrt{\lambda_1}},\ldots,\frac{q_{n-1,i}}{\sqrt{\lambda_{n-1}}}\right)
> $$
>
> Their inner products equal the entries of $G$. $\square$

From (2) and $G\mathbf1=0$, we obtain

$$
\left\|\sum_i x_i\right\|^2=\mathbf1^{\mathsf T}G\mathbf1=0
$$

Consequently, $\sum_i x_i=0$. The points $a_i$ with position vectors $x_i$ have their centroid at the origin.

> [!info] Affine vectors
> **Definition.** The point difference
>
> $$
> a_{ij}=a_j-a_i=x_j-x_i
> $$
>
> is the affine vector from $a_i$ to $a_j$. More generally, an affine vector has the form $u=\sum_i u_i a_i$, where $\sum_i u_i=0$; in the chosen realization, it is represented by $\sum_i u_i x_i$.

The column $\mathbf e_{ij}$ is the coordinate representative of $a_{ij}$ with respect to the vertices. It records the coefficients of the difference, while $x_j-x_i$ expresses that difference in the chosen Euclidean coordinates. In particular, the ordinary coordinate squared norm $\mathbf e_{ij}^{\mathsf T}\mathbf e_{ij}=2$ for $i\ne j$ does not express resistance: resistance is computed using $G$.

By (1) and (2),

$$
\begin{aligned}
\|a_{ij}\|^2&=\|x_j-x_i\|^2\\
&=x_i\cdot x_i+x_j\cdot x_j-2x_i\cdot x_j\\
&=G_{ii}+G_{jj}-2G_{ij}=R_{ij}
\end{aligned}
$$

> [!info] Euclidean resistance representation
> **Theorem.** The vertices of a connected graph admit a Euclidean representation in which
>
> $$
> R_{ij}=\|a_{ij}\|^2,\qquad \|a_{ij}\|=\sqrt{R_{ij}}
> \tag{3}
> $$
>
> The Green matrix is the Gram matrix of the centered position vectors of these points.

## Dimension and the resistance simplex

The rank of a Gram matrix equals the dimension of the linear span of its vectors. Hence $x_1,\ldots,x_n$ span a space of dimension $n-1$.

The origin is the centroid of the points and belongs to their affine hull. The affine hull therefore also has dimension $n-1$: the points $a_1,\ldots,a_n$ are affinely independent.

> [!info] Resistance simplex
> **Definition.** A simplex with vertices $a_1,\ldots,a_n$ satisfying (3) is called the resistance simplex of the graph. For a connected graph, it is nondegenerate and has dimension $n-1$.

Its geometry is uniquely determined up to a Euclidean isometry: a translation and an orthogonal transformation. Two vertices need not be joined by an edge for the distance between their corresponding points to be defined.

## Example: a three-vertex path

Consider the path from the first note.

```mermaid
graph LR
    a1((1)) ---|"c12 = 1"| a2((2))
    a2 ---|"c23 = 2"| a3((3))
```

> [!example] Resistances and the Green matrix
> The edge resistances are $r_{12}=1$ and $r_{23}=1/2$. When current is passed between the endpoints of the path, the two edges are in series, so $R_{13}=3/2$. When current is passed between adjacent vertices, the remaining edge carries no current. Thus,
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
> G=\begin{pmatrix}
> \frac12&-\frac16&-\frac13\\
> -\frac16&\frac16&0\\
> -\frac13&0&\frac13
> \end{pmatrix}
> $$
>
> Direct multiplication gives $G\mathbf1=0$ and $LG=I-\mathbf1\mathbf1^{\mathsf T}/3$. Formula (1) independently reproduces the electrical calculation:
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
> A Euclidean realization may be chosen with coordinates
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
> These coordinates are not centered. After subtracting the centroid $(1/3,1/(3\sqrt2))$, the position vectors have the Gram matrix $G$ displayed above.

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
> **Proof.** Symmetry and positivity follow from (1) and the positive definiteness of $G$ on $H$. For the triangle inequality, it suffices to consider distinct $i,j,k$.
>
> Inject a unit current at $j$ and withdraw it at $k$. Then $\varphi=G(\mathbf e_j-\mathbf e_k)$. At every other vertex $v$, the potential is a weighted average of the potentials at its neighbors:
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
> &=2(G_{kk}-G_{ik}-G_{kj}+G_{ij})\\
> &=2(\varphi_i-\varphi_k)\ge0
> \end{aligned}
> $$
>
> If any indices coincide, the inequality follows from $R_{ii}=0$ and the nonnegativity of resistances. $\square$

Thus resistance distance $R_{ij}$ and the distance $\sqrt{R_{ij}}$ in the resistance simplex are two different metrics on the same vertex set.

## The distance operator

> [!info] Distance operator
> **Definition.** For a symmetric matrix $B$, set
>
> $$
> \mathcal D(B)_{ij}=B_{ii}+B_{jj}-2B_{ij}
> $$
>
> If $B$ is the Gram matrix of the position vectors of points, then $\mathcal D(B)$ is their squared-distance matrix.

The resistance matrix $R=(R_{ij})$ is obtained from the Green matrix by (1):

$$
R=\mathcal D(G)=\mathcal D(L^+)
$$

The forward and inverse transformations between these matrices are considered in [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

## Geometric changes when couplings are strengthened

Adding an edge with positive conductance or increasing the conductance of an existing edge cannot increase any effective resistance. This property is called Rayleigh monotonicity; its justification through the exact resistance variation formula is given in [[Variation of a Single Edge]].

By (3), pairwise distances in the resistance simplex also cannot increase. Some distances may remain unchanged: strengthening one coupling need not affect every measurement. When a coupling is weakened, resistances cannot decrease as long as the graph remains connected.

## Further reading

In [[Inner Product of Graph Vectors]], we pass from squared norms of $a_{ij}$ to inner products of two affine vectors. Electrically, these express the potential difference across one pair of vertices when a unit current is passed through another pair.

Sources on electrical networks and resistance geometry are collected in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the first section of the reading recommendations]].
