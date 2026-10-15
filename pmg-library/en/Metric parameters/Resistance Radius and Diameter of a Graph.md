---
title: Resistance Radius and Diameter of a Graph
date: 2026-10-15
updated: 2026-10-16
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: resistance-radius-and-diameter
order: 1
description: "The circumradius of a resistance simplex, the quadratic normalization of its diameter, computation from the resistance matrix, and reciprocal connectivity parameters."
---

Resistances $R_{ij}$ characterize pairs of vertices. To obtain a metric characteristic of the entire graph, consider the sphere passing through every vertex of its resistance simplex. Its radius provides a parameter with the same physical dimension for graphs with different numbers of vertices. However, the size of the circumsphere determines neither all pairwise distances nor the network's robustness to edge deletion.

This note opens the series "Metric Parameters of Graphs". The geometry of a sphere and its center is developed in [[Nonlocal Elements, Spheres, and Their Centers]], and additivity of the radius under gluing is established in [[Vertex Contraction and Graph Gluing]]. Here we align the normalizations, derive a computational formula, and check it on simple graphs.

## The underlying model

We consider a finite connected undirected graph $G$ on $n\ge2$ vertices, without loops. Existing edges have positive conductances $c_{ij}$; absent couplings have $c_{ij}=0$. Parallel conductors are represented by their total conductance.

The matrix of pairwise effective resistances is denoted by $\mathbf R=(R_{ij})$. It determines a nondegenerate Euclidean simplex of dimension $n-1$, whose vertices $x_1,\ldots,x_n$ satisfy

$$
(x_i-x_j)^2=R_{ij}
$$

Here $x_i$ are points of the Euclidean realization, and $x_i-x_j$ are affine vectors. In PMG, the norm is quadratic: $v^2=v\cdot v$. The linear norm of a vector is $\|v\|=\sqrt{v^2}$. In particular, the linear distance between simplex vertices is $\sqrt{R_{ij}}$, not $R_{ij}$.

The resistance simplex and the transformations between matrix representations are discussed in [[Effective Resistance and Graph Geometry]] and [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

## Radius and diameter of the circumsphere

In the affine hull of a nondegenerate simplex, there is a unique sphere passing through all its vertices. Denote its center by $h$ and its ordinary linear radius by $R_{\mathrm{sph}}$.

> [!info] Radius and diameter in quadratic normalization
> **Definition.** The resistance radius of a graph is
>
> $$
> \boxed{\rho(G)=(x_i-h)^2=R_{\mathrm{sph}}^2}
> $$
>
> This value is independent of the chosen vertex $i$. The resistance diameter is
>
> $$
> \boxed{D_{\mathrm{res}}(G)=4\rho(G)=(2R_{\mathrm{sph}})^2}
> \tag{1}
> $$

| Parameter | Notation and value | Physical dimension in the electrical interpretation |
| --- | --- | --- |
| Linear radius of the sphere | $R_{\mathrm{sph}}=\sqrt{\rho}$ | Square root of resistance |
| Resistance radius | $\rho=R_{\mathrm{sph}}^2$ | Resistance |
| Linear diameter of the sphere | $2R_{\mathrm{sph}}$ | Square root of resistance |
| Resistance diameter | $D_{\mathrm{res}}=4\rho$ | Resistance |

The physical dimensions of $\rho$ and $D_{\mathrm{res}}$ do not depend on the number of vertices. This allows values to be compared across graphs of different orders, but does not by itself remove dependence on the order or on the overall conductance scale.

The center $h$ need not coincide with the centroid $b=n^{-1}\sum_i x_i$ and may lie outside the simplex. The center of the circumsphere is not the orthocenter, the intersection of the altitudes.

**Remark on the isotropic representation.** In this note, $h$ is the Euclidean center. Its bi-coordinates specify an affine combination of the original local vertices, $h_V=\sum_i\alpha_i a_i$, but $h_V$ need not be a local element of the extension. The distinction between $h_V$, its local center, and the sphere element is established in the [[Nonlocal Elements, Spheres, and Their Centers#The center in the affine hull of the original vertices|note on spheres]]. It does not change the Euclidean distances used here.

The earlier name "metric mass" is no longer used as a current term. When comparing older calculations, check whether their parameter equals $\rho$ or $4\rho$.

## Difference from the maximum pairwise resistance

For comparison, denote the maximum pairwise resistance by

$$
R_{\max}(G)=\max_{i,j}R_{ij}
$$

**Proposition.** For every graph in the class under consideration,

$$
\boxed{R_{\max}(G)\le D_{\mathrm{res}}(G)}
\tag{2}
$$

Equality holds if and only if two simplex vertices are diametrically opposite on the circumsphere, meaning that their midpoint is $h$.

> [!proof]- Proof and equality condition
> **Proof.** For $u=x_i-h$ and $v=x_j-h$, one has $u^2=v^2=\rho$. Hence
>
> $$
> R_{ij}=(u-v)^2=2\rho-2u\cdot v\le4\rho
> $$
>
> The Cauchy-Schwarz inequality gives $u\cdot v\ge-\rho$. Equality holds precisely when $v=-u$, equivalently $x_i+x_j=2h$. Since the maximum is taken over finitely many pairs, the same condition characterizes equality in (2). $\square$

Thus $D_{\mathrm{res}}$ is the sharp upper bound on squared distances between arbitrary points of the circumsphere. This bound need not be attained by any pair of graph vertices.

The circumsphere also differs from the smallest ball containing all vertices. Some vertices may lie in the interior of that ball; equality of its radius with $R_{\mathrm{sph}}$ requires an additional condition.

## Computation from the resistance matrix

Write the center in bi-coordinates relative to the vertices:

$$
h=\sum_i\alpha_i x_i,\qquad
\sum_i\alpha_i=1
$$

For an affine point basis, these are the ordinary barycentric coordinates. They are unique but need not be nonnegative. Write $\mathbf1$ for the column of ones and $\boldsymbol\alpha$ for the coordinate column.

**Lemma.** The center coordinates and the resistance radius satisfy

$$
\boxed{
\mathbf R\boldsymbol\alpha=2\rho\,\mathbf1,\qquad
\mathbf1^{\mathsf T}\boldsymbol\alpha=1
}
\tag{3}
$$

> [!proof]- Derivation from equal distances to the vertices
> **Proof.** Set $y_i=x_i-h$. Then $y_i^2=\rho$ and $\sum_i\alpha_i y_i=0$. For each row of the resistance matrix,
>
> $$
> \sum_jR_{ij}\alpha_j
> =\sum_j\bigl(y_i^2+y_j^2-2y_i\cdot y_j\bigr)\alpha_j
> =2\rho
> $$
>
> This is the first equality in (3); the second is the affine-weight condition for the center. $\square$

**Theorem.** For $n\ge2$, the resistance matrix of a connected graph is invertible, and

$$
\boxed{
\rho=\frac{1}{2\,\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1},
\qquad
D_{\mathrm{res}}=\frac{2}{\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1}
}
\tag{4}
$$

The center coordinates are expressed through the same matrix:

$$
\boldsymbol\alpha=
\frac{\mathbf R^{-1}\mathbf1}
{\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1}
$$

> [!proof]- Invertibility and normalization
> **Proof.** For any column $\mathbf v$ with $\mathbf1^{\mathsf T}\mathbf v=0$, the distance formula gives
>
> $$
> \mathbf v^{\mathsf T}\mathbf R\mathbf v
> =-2\left(\sum_i v_i x_i\right)^2
> $$
>
> If $\mathbf v\ne0$, the right-hand side is negative: affine independence of the vertices implies that the corresponding affine vector is nonzero.
>
> Now suppose that $\mathbf R\mathbf v=0$. Left multiplication by $\boldsymbol\alpha^{\mathsf T}$ and (3) give $2\rho\,\mathbf1^{\mathsf T}\mathbf v=0$. Since $\rho>0$, the entries of $\mathbf v$ sum to zero. The preceding equality then rules out $\mathbf v\ne0$. Thus $\mathbf R$ is invertible.
>
> By (3), $\boldsymbol\alpha=2\rho\,\mathbf R^{-1}\mathbf1$. Summing the entries gives $1=2\rho\,\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1$, which yields (4) and the coordinate formula. In particular, the denominator is positive. $\square$

For computation, the full inverse matrix is unnecessary. Solve $\mathbf R\mathbf v=\mathbf1$, calculate $s=\sum_i v_i$, and set $\rho=1/(2s)$, $D_{\mathrm{res}}=2/s$, and $\boldsymbol\alpha=\mathbf v/s$.

Formula (4) uses the resistance matrix. It cannot be replaced by the Green matrix $\mathbf{Gr}=\mathbf L^+$: the latter satisfies $\mathbf{Gr}\mathbf1=0$ and is singular. A representation using the Gram matrix of local vertices will be considered separately.

## Reciprocal connectivity parameters

> [!info] Radial and diametral connectivity
> **Definition.** For a connected graph on $n\ge2$ vertices, define
>
> $$
> \boxed{
> c_{\mathrm{rad}}(G)=\frac1{\rho(G)},\qquad
> c_{\mathrm{diam}}(G)=\frac1{D_{\mathrm{res}}(G)}
> =\frac14c_{\mathrm{rad}}(G)
> }
> $$

These are metric parameters of PMG. They are distinct from vertex or edge connectivity defined in terms of the minimum number of vertices or edges to remove.

By (4),

$$
c_{\mathrm{rad}}=2\,\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1,
\qquad
c_{\mathrm{diam}}=\frac12\,\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1
$$

Both quantities have the physical dimension of conductance. A larger value corresponds to a smaller circumsphere under the respective normalization. A general electrical interpretation for a set of more than two vertices does not follow from physical dimensions alone and remains a separate question.

For a pair of vertices with resistance $r$, one obtains $c_{\mathrm{diam}}=1/r$. This is the effective conductance between the selected vertices. For a graph consisting of a single edge, it equals that edge's conductance; within a larger network, alternative paths also contribute. This normalization makes diametral connectivity convenient for comparison with a two-terminal network.

## Simple examples

### A single edge

Let two vertices be joined by conductance $c>0$. Their resistance is $r=1/c$, and the resistance simplex is a segment of linear length $\sqrt r$. Its center is the midpoint. Hence

$$
\rho=\frac{r}{4}=\frac1{4c},\qquad
D_{\mathrm{res}}=r=\frac1c,\qquad
c_{\mathrm{diam}}=c
$$

This direct geometric calculation checks the factor of $4$ in (1).

### A triangle with unit conductances

In $K_3$ with unit conductances, each vertex pair is connected by an edge of resistance $1$ in parallel with an alternative path of resistance $2$. Therefore,

$$
R_{ij}=\frac{1\cdot2}{1+2}=\frac23
$$

The resistance simplex is an equilateral triangle with squared side length $2/3$. Its squared circumradius is one third of the squared side length:

$$
\rho=\frac29,\qquad
D_{\mathrm{res}}=\frac89,\qquad
R_{\max}=\frac23<\frac89
$$

Symmetry gives $\alpha_i=1/3$. Substitution into (3) independently checks the matrix normalization: every entry of $\mathbf R\boldsymbol\alpha$ equals $4/9=2\rho$.

### Trees

Resistance radii add when graphs are glued at a single vertex. The proof using orthogonality of the spaces of the parts is given in the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|note on gluing]].

Every tree can be assembled by gluing individual edges in this way, so

$$
\boxed{
\rho(T)=\frac14\sum_{e\in E(T)}\frac1{c_e},
\qquad
D_{\mathrm{res}}(T)=\sum_{e\in E(T)}\frac1{c_e}
}
\tag{5}
$$

For a tree on $n$ vertices with unit conductances, this gives $\rho=(n-1)/4$ and $D_{\mathrm{res}}=n-1$. All such trees have the same values, regardless of their branching structure.

Compare the path $P_4$ with edges $ab,bc,cd$ and the star $K_{1,3}$ with edges $oa,ob,oc$. All conductances are one.

| Graph | $\rho$ | $D_{\mathrm{res}}$ | $R_{\max}$ | $c_{\mathrm{diam}}$ |
| --- | --- | --- | --- | --- |
| Path $P_4$ | $3/4$ | $3$ | $3$ | $1/3$ |
| Star $K_{1,3}$ | $3/4$ | $3$ | $2$ | $1/3$ |

In a tree, the resistance of a pair is the sum of edge resistances along the unique path between its vertices. The endpoints of $P_4$ are joined by all three edges, whereas any path in the star has at most two edges. Thus their maximum pairwise resistances differ.

> [!example]- An independent geometric check for the path and the star
> Take orthonormal vectors $e_1,e_2,e_3$. The path is realized by the points $0,e_1,e_1+e_2,e_1+e_2+e_3$, and the star by $0,e_1,e_2,e_3$. In both cases, squared distances equal the corresponding path lengths in the tree.
>
> For each set, the circumsphere center is $h=(e_1+e_2+e_3)/2$, and the norm of the difference between any vertex and $h$ is $3/4$. The first and last vertices of the path are diametrically opposite; the star has no such pair.
>
> In the star's basis, the center coordinates are $(-1/2,1/2,1/2,1/2)$, with the first coordinate referring to the central graph vertex. The negative coordinate shows that the sphere center lies outside the simplex.

This example also distinguishes the circumsphere from the smallest enclosing ball: for the star, the ball centered at $(e_1+e_2+e_3)/3$ with squared radius $2/3$ contains all four vertices and is smaller than the circumscribed ball of squared radius $3/4$.

### The complete graph

Suppose every edge of the complete graph $K_n$ has the same conductance $c>0$. Then

$$
\mathbf L=nc\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right),
\qquad
\mathbf{Gr}=\frac1{nc}\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right)
$$

The distance formula gives

$$
R_{ij}=\frac2{nc}\qquad(i\ne j)
$$

The resistance simplex is regular, its center is the centroid, and $\alpha_i=1/n$. Substitution into (3) yields

$$
\boxed{
\rho(K_n)=\frac{n-1}{n^2c},\qquad
D_{\mathrm{res}}(K_n)=\frac{4(n-1)}{n^2c}
}
\tag{6}
$$

Consequently,

$$
c_{\mathrm{diam}}(K_n)=\frac{n^2c}{4(n-1)},\qquad
\frac{D_{\mathrm{res}}(K_n)}{R_{\max}(K_n)}
=\frac{2(n-1)}n
$$

For $n>2$, inequality (2) is strict even for the complete graph. For $K_5$ with unit conductances, $\rho=4/25$ and $D_{\mathrm{res}}=16/25$.

## What the parameter measures and its limitations

**Size, rather than the entire geometry.** The circumradius is a single scalar. Equal radii do not imply equal resistance matrices, simplex shapes, vertex degrees, or centralities. The path and star above provide a direct example.

**Scale dependence.** Multiplying every conductance by $\lambda>0$ divides every resistance by $\lambda$. The Euclidean simplex is scaled by $1/\sqrt\lambda$, so $\rho$ and $D_{\mathrm{res}}$ are divided by $\lambda$, while the reciprocal connectivity parameters are multiplied by $\lambda$. Dimensionless comparisons require additional normalization.

**No general monotonicity with respect to edges is assumed.** A decrease in pairwise resistances when couplings are strengthened does not automatically imply a decrease in the circumradius: the center also changes. Behavior under conductance variations will be considered separately.

**A vertex set and a new network.** When only some vertices are selected, their original resistances can be retained and the circumsphere of that subset constructed. Deleting the remaining vertices together with their edges produces a different network and, in general, a different metric. Preservation of the metric under elimination by a Schur complement is discussed in [[Vertex Elimination and Induced Couplings]].

**A single vertex and a disconnected graph.** For one vertex, set $\rho=D_{\mathrm{res}}=0$, but the reciprocal connectivity parameters are no longer finite, and formula (4) is undefined. A disconnected graph has no common finite resistance metric between different components. Radii may be considered component by component; mechanically substituting the pseudoinverse Laplacian of a disconnected graph does not recover the previous electrical interpretation.

## Status of the results and continuation

The definitions of $\rho$, $D_{\mathrm{res}}$, $c_{\mathrm{rad}}$, and $c_{\mathrm{diam}}$ specify the normalizations used. Inequality (2), system (3), and formulas (4) are proved above. The tree formula (5) relies on the proved additivity under gluing; the complete-graph formula (6) is derived from its Laplacian.

For a single edge, the triangle, the path, and the star, geometric or electrical calculations are given that do not use inversion of the resistance matrix. In addition, (3)-(4) were checked with exact rational arithmetic on these graphs and on $K_5$ with unit conductances. These checks supplement the general proofs.

The next note will relate the radius to the Gram matrix of a vertex set, its determinant, and the simplex volume. Subsequent notes will address center coordinates, vertex and edge parameters, the two types of vertex removal, and dimensionless characteristics. No general electrical interpretation of the reciprocal connectivity parameters for sets of more than two vertices is asserted here.

## Sources and correspondence of notation

- [[Nonlocal Elements, Spheres, and Their Centers]]: the geometric definition of a sphere and the distinction between its representatives.
- [[Vertex Contraction and Graph Gluing]]: additivity of the resistance radius and the tree formula.
- K. Devriendt, R. Lambiotte. [Discrete curvature on graphs from the effective resistance](https://arxiv.org/abs/2201.06385), 2022, Appendix B.2-B.3 in version v3: matrix and geometric characterizations of the circumsphere center. Their $\sigma^2$ corresponds to our $\rho$, and their $\mathbf p$ to the column $\boldsymbol\alpha$.
- D. Malyugin. [Express Analysis of Metric Parameters of Graphs](https://habr.com/ru/articles/534182/), 2020 (in Russian): the original discussion of metric characteristics. The parameter $r(G)$, defined there as the squared radius, corresponds to $\rho(G)$; passing to $D_{\mathrm{res}}$ requires a factor of $4$.

