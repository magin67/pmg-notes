---
title: "Centroid, Spanning-Tree, and Eigenvector Centralities"
date: 2026-10-16
updated: 2026-10-16
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: centroid-spanning-tree-and-eigenvector-centralities
order: 3
description: "The minimizing property of the centroid, the Green-matrix trace and Kirchhoff index, the relation between spanning-tree degrees and the circumcenter, and a comparison of three centralities on the Krackhardt kite graph."
---

Parameters of a graph as a whole do not determine the roles of individual vertices. All trees with unit conductances and the same number of vertices have the same resistance radius, although their branching and vertex positions may differ substantially. To compare vertices, we consider three characteristics: proximity to the centroid, expected degree in a spanning tree, and centrality based on an eigenvector of the adjacency matrix.

The centroid and spanning-tree characteristics connect matrix data with simplex geometry. The diagonal of the Green matrix gives resistances to the centroid, while expected spanning-tree degrees determine the bi-coordinates of the circumcenter. Comparison with eigenvector centrality shows which differences between vertices each approach captures.

Definitions of the resistance radius and center coordinates are given in [[Resistance Radius and Diameter of a Graph]] and [[Resistance Radius of a Set - Gram Matrix and Volume]]. The same normalizations are used here.

## The underlying model and notation

Consider a finite connected undirected graph $G$ on $n\ge2$ vertices without loops. Existing edges have positive conductances. The adjacency matrix with conductances as weights, the degrees, and the Laplacian are

$$
\mathbf A=(c_{ij}),\qquad
c_{ii}=0,\qquad
d_i=\sum_jc_{ij},\qquad
\mathbf L=\operatorname{diag}(d_i)-\mathbf A
$$

Write $k_i$ for the number of neighbors of vertex $i$. This differs from the weighted degree $d_i$; for unit conductances, $d_i=k_i$.

The Green matrix is denoted by $\mathbf{Gr}=\mathbf L^+$, and the resistance matrix by $\mathbf R=(R_{ij})$. The notation $\mathbf G$ is reserved for the Gram matrix of the chosen elements; for local vertices, $\mathbf G=-\mathbf R/2$. The graph $G$ and the matrix $\mathbf G$ are distinguished typographically.

Let $x_1,\ldots,x_n$ be the vertices of a Euclidean realization of the resistance simplex. Then

$$
(x_i-x_j)^2=R_{ij},\qquad
b=\frac1n\sum_i x_i,\qquad
r_i=(x_i-b)^2=\mathbf{Gr}_{ii}
$$

Here $b$ is the centroid, and $r_i$ is the resistance from a vertex to the centroid. Under the PMG convention, norm is quadratic: $X^2=X\cdot X$; its square root is called the linear norm. Thus $r_i$ is a squared ordinary Euclidean distance.

All $r_i$ are positive: the centroid of a nondegenerate simplex on $n\ge2$ vertices does not coincide with any vertex. Set $\mathbf r=(r_1,\ldots,r_n)^{\mathsf T}$ and $\mathbf1=(1,\ldots,1)^{\mathsf T}$. We use the identities

$$
\mathbf{Gr}\mathbf1=0,\qquad
\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L
=\mathbf J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

Denote the circumcenter by $O$ and its bi-coordinates by $\alpha_i$:

$$
O=\sum_i\alpha_i x_i,\qquad
\sum_i\alpha_i=1,\qquad
(x_i-O)^2=\rho
$$

The resistance radius is $\rho=R_{\mathrm{sph}}^2$, and the resistance diameter is $D_{\mathrm{res}}=4\rho$. Distances to $O$ are equal for all vertices, so they do not provide a ranking on their own.

**Remark on the isotropic representation.** The average of local vertices $b_V=n^{-1}\sum_i a_i$ may be a nonlocal element. The geometric centroid corresponds to its local center $\pi(b_V)=b_V-b_V^2z/2$. Norms of differences are preserved, so the formulas for $r_i$ agree in both representations. This distinction is discussed in the [[Nonlocal Elements, Spheres, and Their Centers#What selecting the center preserves|note on local centers]].

## The centroid minimizes the sum of resistances

For a point $x$ in the entire affine space of the simplex, set $R(x,x_i)=(x-x_i)^2$. This is a geometric extension of resistance; it does not require adding a new node to the electrical network.

> [!info] The minimizing property of the centroid
> **Theorem.** For every point $x$,
>
> $$
> \boxed{
> \sum_i R(x,x_i)=\sum_i r_i+n(x-b)^2
> }
> \tag{1}
> $$
>
> Consequently, the centroid $b$ is the unique minimizer of the sum of resistances to all vertices.

> [!proof]- Decomposition relative to the centroid
> **Proof.** Write $x-x_i=(x-b)+(b-x_i)$ and expand the norm. On summation, the cross term vanishes because $\sum_i(b-x_i)=0$. This gives (1). The metric on the space of directions is positive definite, so $(x-b)^2\ge0$, with equality only at $x=b$. $\square$

The statement holds for every nondegenerate Euclidean simplex. It uses the sum of squared distances. Minimizing the sum of linear distances $\sum_i\sqrt{R(x,x_i)}$ is a different problem and generally gives a different point.

All vertices in (1) receive equal weight. Edge conductances affect the metric. If positive vertex weights $\mu_i$ are additionally specified, the minimum of $\sum_i\mu_iR(x,x_i)$ is attained at their weighted average $\sum_i\mu_i x_i/\sum_i\mu_i$; this is a separate choice of averaging model.

## Total resistance to the centroid, the Kirchhoff index, and the radius

**Definition.** The total resistance to the centroid is

$$
S_{\mathrm{cent}}(G)=\sum_i r_i=\operatorname{tr}\mathbf{Gr}
$$

By (1), this is the minimum sum of resistances from a single point to all vertices. The mean resistance is $S_{\mathrm{cent}}/n$. Both quantities have the physical dimension of resistance.

**Definition.** The Kirchhoff index is the sum over unordered pairs of distinct vertices:

$$
Kf(G)=\sum_{i<j}R_{ij}
$$

> [!info] Three expressions for one parameter
> **Theorem.** For a connected graph,
>
> $$
> \boxed{
> Kf(G)=nS_{\mathrm{cent}}(G)
> =n\operatorname{tr}\mathbf{Gr}
> }
> \tag{2}
> $$

> [!proof]- Summing the distance formula
> **Proof.** The identities $R_{ij}=r_i+r_j-2\mathbf{Gr}_{ij}$ and $\mathbf{Gr}\mathbf1=0$ imply
>
> $$
> \sum_jR_{ij}=nr_i+S_{\mathrm{cent}}
> $$
>
> Summing over $i$ gives $2Kf=2nS_{\mathrm{cent}}$. The factor $2$ on the left arises because each unordered pair is counted twice. $\square$

If $0=\lambda_1<\lambda_2\le\cdots\le\lambda_n$ are the Laplacian eigenvalues, then

$$
S_{\mathrm{cent}}=\sum_{k=2}^n\frac1{\lambda_k}
$$

Thus the total resistance to the centroid is not independent of the Kirchhoff index: it is the same parameter scaled by $1/n$. Its representations through resistances, the trace of the pseudoinverse Laplacian, and the Laplacian spectrum are standard [1].

The relation to the radius also involves the distance between the two centers.

> [!info] The centroid and the circumcenter
> **Theorem.** The following identity holds:
>
> $$
> \boxed{
> \rho=\frac{S_{\mathrm{cent}}}{n}+(O-b)^2
> =\frac{Kf(G)}{n^2}+(O-b)^2
> }
> \tag{3}
> $$
>
> In particular, $Kf(G)\le n^2\rho$, with equality if and only if $O=b$.

> [!proof]- Substituting the circumcenter
> **Proof.** At $x=O$, the left-hand side of (1) equals $n\rho$, since $O$ is equidistant from all vertices. Dividing by $n$ and using (2) gives (3). $\square$

The centers coincide if and only if all $r_i$ are equal. Indeed, in this case $b$ is equidistant from the vertices and is the circumcenter. Thus the radius captures the mean resistance to the centroid together with the displacement of the circumcenter; in general, $S_{\mathrm{cent}}$ alone is insufficient to recover $\rho$.

## Centroid centrality

**Definition.** The centroid centrality of a vertex is the normalized reciprocal of its resistance to the centroid:

$$
C_i^{\mathrm{cent}}
=\frac{1/r_i}{\sum_j1/r_j}
=\frac{1/\mathbf{Gr}_{ii}}{\sum_j1/\mathbf{Gr}_{jj}}
$$

A larger value corresponds to a smaller distance to the centroid. The name and normalization are fixed here for this series; they do not imply a new definition of the Green matrix itself.

By the proof of (2), the sum of resistances from a vertex to all others equals $nr_i+S_{\mathrm{cent}}$. Hence

$$
C_{\mathrm{CF}}(i)=\frac{n-1}{\sum_{j\ne i}R_{ij}}
=\frac{n-1}{nr_i+S_{\mathrm{cent}}}
$$

is a different numerical score but gives exactly the same ranking of the vertices within a graph. The quantity $C_{\mathrm{CF}}$ is current-flow closeness centrality; its relation to information centrality is established in [2]. Normalizations in the literature may differ by a constant factor.

Identical rankings do not imply identical normalized values. Replacing $1/r_i$ with $1/(nr_i+S_{\mathrm{cent}})$ changes the ratios between scores. The tables below use $C_i^{\mathrm{cent}}$ as defined above.

## Expected spanning-tree degree and circumcenter coordinates

Let $\tau(G)$ be the spanning-tree coefficient. Choose a random spanning tree according to

$$
\Pr(T)=\frac1{\tau(G)}\prod_{e\in T}c_e
$$

For unit conductances, all spanning trees are equally likely.

**Definition.** The expected spanning-tree degree of a vertex is

$$
\delta_i=\mathbb E[\deg_T(i)]
$$

Here $\deg_T(i)$ counts the tree edges incident to the vertex; it is not the sum of their conductances. Conductances are already included in the probability of selecting a tree.

The [[From Lengths to Areas and Volumes#Edge-inclusion probabilities in a spanning tree|edge-inclusion formula]] $\Pr(\{i,j\}\in T)=c_{ij}R_{ij}$ gives

$$
\boxed{
\delta_i=\sum_jc_{ij}R_{ij},
\qquad
\sum_i\delta_i=2(n-1)
}
\tag{4}
$$

The first equality follows by summing the inclusion indicators of incident edges. The second follows because the degree sum of every spanning tree is $2(n-1)$. In particular, $1\le\delta_i\le k_i$.

**Definition.** Spanning-tree centrality in this note is defined by

$$
C_i^{\mathrm{tree}}=\frac{\delta_i}{2(n-1)}
$$

It has a direct probabilistic interpretation: select a random spanning tree, then uniformly select one of its $2(n-1)$ edge ends. The probability of obtaining vertex $i$ is $C_i^{\mathrm{tree}}$.

Expected spanning-tree degree must be distinguished from expected degree over arbitrary forests. For forests, one must additionally specify the number of components, or a distribution over that number, and the weights. Such averages are not used here.

> [!info] Spanning-tree degrees and the bi-coordinates of the center
> **Theorem.** The bi-coordinates of the circumcenter satisfy
>
> $$
> \boxed{
> \boldsymbol\alpha=\frac1n\mathbf1+\frac12\mathbf L\mathbf r,
> \qquad
> \alpha_i=1-\frac{\delta_i}{2}
> }
> \tag{5}
> $$

> [!proof]- Derivation using the Laplacian and the resistance matrix
> **Proof.** The distance formula can be written as
>
> $$
> \mathbf R=\mathbf r\mathbf1^{\mathsf T}+\mathbf1\mathbf r^{\mathsf T}-2\mathbf{Gr}
> $$
>
> Consequently, $\mathbf L\mathbf R=(\mathbf L\mathbf r)\mathbf1^{\mathsf T}-2\mathbf J$. Multiply the identity $\mathbf R\boldsymbol\alpha=2\rho\mathbf1$ from the [[Resistance Radius and Diameter of a Graph#Computation from the resistance matrix|center-coordinate formula]] on the left by $\mathbf L$. Using $\mathbf1^{\mathsf T}\boldsymbol\alpha=1$, we obtain
>
> $$
> 0=\mathbf L\mathbf r-2\boldsymbol\alpha+\frac2n\mathbf1
> $$
>
> This is the first equality in (5). On the other hand, the $i$-th diagonal entry of $\mathbf L\mathbf R$ equals $-\delta_i$, since $R_{ii}=0$. Therefore
>
> $$
> -\delta_i=(\mathbf L\mathbf r)_i-2+\frac2n
> $$
>
> Substitution gives the second equality in (5). $\square$

The quantity $1-\delta_i/2$ is also known as vertex resistance curvature; its relation to the coordinates of the circumcenter is described in [3]. It differs from the reciprocal resistance radius of the entire graph, called radial connectivity in PMG.

Formula (5) explains the signs of the coordinates: $\alpha_i$ is positive when $\delta_i<2$, zero when $\delta_i=2$, and negative when $\delta_i>2$. Thus the $\alpha_i$ themselves are unsuitable as positive centrality weights. With the chosen normalization,

$$
C_i^{\mathrm{tree}}=\frac{1-\alpha_i}{n-1}
$$

Greater spanning-tree centrality corresponds to a smaller coordinate of the circumcenter.

Formula (5) also yields a computational supplement to (3). Since $(O-b)^2=\boldsymbol\alpha^{\mathsf T}\mathbf{Gr}\boldsymbol\alpha$ and $\mathbf L\mathbf{Gr}\mathbf L=\mathbf L$, we have

$$
(O-b)^2=\frac14\mathbf r^{\mathsf T}\mathbf L\mathbf r,
\qquad
\rho=\frac{S_{\mathrm{cent}}}{n}+\frac14\mathbf r^{\mathsf T}\mathbf L\mathbf r
$$

The quadratic form on the right is nonnegative and vanishes exactly when the column $\mathbf r$ is constant.

## Eigenvector centrality and a common normalization

**Definition.** Eigenvector centrality is defined by a positive eigenvector of the adjacency matrix:

$$
\mathbf A v=\lambda_{\max}(\mathbf A)v,\qquad v_i>0,
\qquad
C_i^{\mathrm{eig}}=\frac{v_i}{\sum_jv_j}
$$

For a connected graph, this vector exists and is unique up to scaling by the Perron-Frobenius theorem [4]. In component form, $\lambda_{\max}v_i=\sum_jc_{ij}v_j$: the score of a vertex is determined by the weighted scores of its neighbors.

This definition uses the adjacency matrix $\mathbf A$, not the Laplacian $\mathbf L$. The sum of reciprocal nonzero Laplacian eigenvalues in the formula for $S_{\mathrm{cent}}$ concerns a different spectral object.

All three centralities use a common normalization:

| Centrality | Initial positive score $s_i$ | Normalized score |
| --- | --- | --- |
| Eigenvector | $v_i$ | $C_i^{\mathrm{eig}}=v_i/\sum_jv_j$ |
| Spanning-tree | $\delta_i$ | $C_i^{\mathrm{tree}}=\delta_i/[2(n-1)]$ |
| Centroid | $1/r_i$ | $C_i^{\mathrm{cent}}=(1/r_i)/\sum_j(1/r_j)$ |

**Corollary.** Every column satisfies $C_i>0$, $\sum_iC_i=1$. The uniform score is $1/n$; comparison with it can use $nC_i$, whose mean is $1$.

Multiplying all conductances by $t>0$ multiplies $\mathbf A,\mathbf L$ by $t$ and divides $\mathbf{Gr},\mathbf R$ by $t$. The eigenvector $v$ and the products $c_{ij}R_{ij}$ remain unchanged; all $1/r_i$ are multiplied by the same factor. Therefore the three normalized centralities are unchanged.

A common sum allows the distributions of scores across vertices to be compared, but does not turn different definitions into one measure of importance. A value of $0.15$ in one column has no universal substantive equivalent in another. Comparisons between graphs of different sizes must also account for the baseline $1/n$.

Normalization on the complete graph is a check of consistency with symmetry. It does not imply statistical unbiasedness: that claim would require a statistical model and an estimand.

## The complete graph, a path, and a star

### The complete graph

For $K_n$ with unit conductances,

$$
\mathbf{Gr}=\frac1n\mathbf J,\qquad
r_i=\frac{n-1}{n^2},\qquad
\delta_i=\frac{2(n-1)}n,\qquad
\alpha_i=\frac1n
$$

All three centralities equal $1/n$, and $O=b$. Here $S_{\mathrm{cent}}=(n-1)/n$, $Kf=n-1$, and $\rho=(n-1)/n^2$.

### A five-vertex path

Let a path with unit conductances visit the vertices $1,2,3,4,5$ in order. Its unique spanning tree is the graph itself, so

$$
\boldsymbol\delta=(1,2,2,2,1)^{\mathsf T},\qquad
\boldsymbol\alpha=(1/2,0,0,0,1/2)^{\mathsf T}
$$

The resistances are $R_{ij}=|i-j|$. The row sums of the resistance matrix are $(10,7,6,7,10)^{\mathsf T}$, and $S_{\mathrm{cent}}=4$. Hence

$$
\mathbf r=(6/5,3/5,2/5,3/5,6/5)^{\mathsf T}
$$

The three centralities are

$$
C^{\mathrm{eig}}=
\frac{(1,\sqrt3,2,\sqrt3,1)^{\mathsf T}}{4+2\sqrt3},
\qquad
C^{\mathrm{tree}}=\frac{(1,2,2,2,1)^{\mathsf T}}8,
\qquad
C^{\mathrm{cent}}=\frac{(1,2,3,2,1)^{\mathsf T}}9
$$

The eigenvector is verified by direct multiplication by the adjacency matrix: its eigenvalue is $\sqrt3$. The spanning-tree score does not distinguish the three internal vertices. The eigenvector and centroid scores single out the middle vertex, but give different score ratios.

### A five-vertex star

Consider the star $K_{1,4}$ with unit conductances, a central vertex $o$, and four leaves. Again, there is exactly one spanning tree, so $\delta_o=4$ and $\delta_{\mathrm{leaf}}=1$. The circumcenter coordinates are $\alpha_o=-1$ and $\alpha_{\mathrm{leaf}}=1/2$.

For the centroid, we obtain

$$
r_o=\frac4{25},\qquad r_{\mathrm{leaf}}=\frac{19}{25}
$$

**Independent geometric check.** Realize the star by the points $0,e_1,e_2,e_3,e_4$, where the $e_i$ are orthonormal. Their centroid is $(e_1+e_2+e_3+e_4)/5$. Direct norms of differences give $4/25$ for the central vertex and $19/25$ for each leaf.

The eigenvector is proportional to $(2,1,1,1,1)$ and has eigenvalue $2$. Therefore

| Vertex | Eigenvector | Spanning-tree | Centroid |
| --- | --- | --- | --- |
| Center $o$ | $1/3$ | $1/2$ | $19/35$ |
| Each leaf | $1/6$ | $1/8$ | $4/35$ |

The ranking is the same, but the degree to which the center stands out differs.

### Equal radii do not imply equal Green-matrix traces

For the above five-vertex graphs with unit conductances:

| Graph | $S_{\mathrm{cent}}$ | $Kf$ | $\rho$ | $(O-b)^2$ |
| --- | --- | --- | --- | --- |
| $K_5$ | $4/5$ | $4$ | $4/25$ | $0$ |
| $P_5$ | $4$ | $20$ | $1$ | $1/5$ |
| $K_{1,4}$ | $16/5$ | $16$ | $1$ | $9/25$ |

The path and the star have the same resistance radius but different total resistances to the centroid. Their values agree with (3). For an independent check of the radius, use the star realization already given and realize the path by $0,e_1,e_1+e_2,e_1+e_2+e_3,e_1+e_2+e_3+e_4$. In both cases, the circumcenter is $(e_1+e_2+e_3+e_4)/2$, and every vertex has resistance $1$ to it.

## Comparison on the Krackhardt kite graph

The Krackhardt kite graph was introduced to compare different centralities. We use its standard ten-vertex implementation from NetworkX, with vertices numbered $0,\ldots,9$ [5]. All conductances are one.

For reproducibility, the 18 edges are listed below; $ij$ denotes the unordered pair of vertices $i,j$:

$$
E=\{01,02,03,05,13,14,16,23,25,34,35,36,46,56,57,67,78,89\}
$$

Vertices $0,\ldots,6$ form the dense part. Vertex $7$ is adjacent to $5,6$ and leads into the chain $7-8-9$. Vertex $3$ has the largest degree, namely $6$.

![[Vertex Centralities - Krackhardt Kite Graph.svg]]

*Figure 1. Three centralities of the same graph. Vertex positions are identical; circle area is proportional to the normalized score, with the same area scale in all panels. The layout shows the connections and is not a Euclidean realization of the resistance simplex. Labels 8 and 9 are placed outside the circles so that small scores remain legible.*

Computed values are given as percentages. In grouped rows, the value is for each vertex, not for the pair as a whole.

| Vertex | Eigenvector, % | Spanning-tree, % | Centroid, % |
| --- | ---: | ---: | ---: |
| $0,1$ | $12.545$ | $9.422$ | $10.741$ |
| $2,4$ | $10.181$ | $7.620$ | $8.609$ |
| $3$ | **$17.133$** | **$12.838$** | $14.806$ |
| $5,6$ | $14.165$ | $12.125$ | **$15.150$** |
| $7$ | $6.976$ | $12.162$ | $10.419$ |
| $8$ | $1.712$ | $11.111$ | $3.751$ |
| $9$ | $0.398$ | $5.556$ | $2.024$ |

Before rounding, scores over the ten vertices sum to $100\%$ in each column. Equality within the pairs $0,1$, $2,4$, and $5,6$ follows from graph symmetry.

**Eigenvector score.** Vertex $3$, with six neighbors in the dense part, has the largest value. Scores decrease rapidly along the chain: vertex $8$ receives only about $1.7\%$, and vertex $9$ about $0.4\%$.

**Centroid score.** The maximum is attained at $5,6$. Their resistance to the centroid is $687/2960$, whereas vertex $3$ has resistance $19/80=703/2960$. Thus $5,6$ are slightly closer to the centroid and have a smaller sum of resistances to all vertices.

**Spanning-tree score.** The maximum remains at $3$, but vertices $7,8$ receive substantially larger shares than under eigenvector ranking. Both edges incident to vertex $8$ are bridges and occur in every spanning tree, so $\delta_8=2$ and $C_8^{\mathrm{tree}}=2/18=1/9$. Vertex $7$ has expected spanning-tree degree $81/37$, slightly greater than the value $323/148$ at each of $5,6$.

The graph's spanning-tree coefficient is $\tau=2368$. The expected spanning-tree degrees from (4) were independently checked by enumerating all 2368 trees. The total metric parameters are

$$
S_{\mathrm{cent}}=\frac{1535}{296},\qquad
Kf=\frac{7675}{148}
$$

## Spanning-tree degree and disconnection after vertex deletion

The high score of vertex $8$ has a specific cause: its two mandatory edges. The number of components after deletion is related to expected spanning-tree degree but does not determine it completely.

**Lemma.** Suppose deleting vertex $i$ together with its incident edges leaves $q_i$ components. Then

$$
\delta_i\ge q_i
$$

> [!proof]- Component count and degree in a spanning tree
> **Proof.** For every spanning tree $T$, deleting $i$ produces exactly $\deg_T(i)$ components. The graph $T-i$ is a spanning subgraph of $G-i$, so it cannot have fewer components than $G-i$. Therefore $\deg_T(i)\ge q_i$ for every $T$. Taking expectations proves the claim. $\square$

At vertex $8$ of the Krackhardt kite graph, $q_8=\delta_8=2$. However, the common vertex of two triangles with unit conductances glued at one point also has $q_i=2$, but $\delta_i=8/3$: each triangle contributes an average of $4/3$ incident edges. The same number of components after deletion is compatible with different expected spanning-tree degrees.

In the Krackhardt kite graph, vertices $7,8$ are articulation points, whereas vertex $3$, which leads in spanning-tree centrality, is not. Consequently, ranking by $C^{\mathrm{tree}}$ does not coincide with ranking by the ability of a vertex's deletion to disconnect the graph.

## Removing a point while preserving the metric

Geometric removal of one vertex admits an exact formula. Let $\rho_{\widehat i}$ denote the radius of the remaining vertex set with the original pairwise resistances preserved; for a single remaining vertex, set $\rho_{\widehat i}=0$. This set corresponds to a principal submatrix of the original Gram matrix. For the graph $G-i$ obtained by deleting the vertex and its incident edges, the resistances must be computed anew.

> [!info] Change in radius on removing one point
> **Theorem.** Under the stated assumptions,
>
> $$
> \boxed{
> \rho-\rho_{\widehat i}
> =\frac{\alpha_i^2}{d_i}
> =\frac{(1-\delta_i/2)^2}{d_i}
> }
> \tag{6}
> $$
>
> Here $d_i$ is the weighted degree of the vertex in the original graph.

> [!proof]- Distance to the opposite face
> **Proof.** Let $y_j=x_j-b$ and $w_i=\sum_j\mathbf L_{ij}y_j$. Since the Gram matrix of the $y_j$ is $\mathbf{Gr}$,
>
> $$
> w_i\cdot(x_j-x_k)=\delta_{ij}^{\mathrm{Kr}}-\delta_{ik}^{\mathrm{Kr}},
> \qquad
> w_i^2=(\mathbf L\mathbf{Gr}\mathbf L)_{ii}=d_i
> $$
>
> Here $\delta_{ij}^{\mathrm{Kr}}$ denotes the Kronecker delta, not expected spanning-tree degree.
>
> Thus $w_i$ is the gradient of the affine function giving the $i$-th barycentric coordinate. This function is zero on the affine hull of the opposite face and one at $x_i$. Its value at the center $O$ is $\alpha_i$, so the squared distance from $O$ to that affine hull is $\alpha_i^2/w_i^2=\alpha_i^2/d_i$.
>
> By the [[Resistance Radius of a Set - Gram Matrix and Volume#The radius of a subset and projection of the center|center-projection theorem]], this squared distance equals the difference of resistance radii $\rho-\rho_{\widehat i}$. Substituting (5) completes the proof. $\square$

In particular, when $\delta_i=2$, geometric removal of the vertex preserves the radius. This is exactly what happens at vertex $8$ of the Krackhardt kite graph: $\alpha_8=0$ and $\rho_{\widehat8}=\rho$. At the same time, deleting node $8$ with its edges makes the graph disconnected.

Formula (6) also explains why spanning-tree centrality and influence on the radius do not give the same ranking. The radius difference depends on the square of $1-\delta_i/2$ and on $d_i$, rather than monotonically on $\delta_i$ alone.

## Status of the results and continuation

The minimizing property of the centroid (1), identities (2)-(3), the relation between spanning-tree degrees and center coordinates (4)-(5), the bound in terms of component count, and the geometric removal formula (6) have been proved under explicit assumptions. The resistance-geometry identities and the spanning-tree distribution used here agree with the published literature. The centralities and their common normalization are definitions; no ranking is claimed to be universally superior.

Numerical values were checked for $K_5$, $P_5$, $K_{1,4}$, the Krackhardt kite graph, and two triangles sharing one vertex, all with unit conductances. An additional check used a triangle with conductances $2,3,4$: its spanning-tree coefficient is $26$, and degrees were averaged using tree weights rather than equal probabilities.

Resistances were computed in exact rational arithmetic from the inverse of a reduced Laplacian. Radii and center coordinates were independently obtained by solving $\mathbf R\boldsymbol\alpha=2\rho\mathbf1$. Formulas (2)-(6) were checked against these data, including every single-vertex removal. Spanning-tree degrees were additionally obtained by direct tree enumeration; explicit Euclidean realizations were used for the path and the star. Eigenvector scores were computed numerically, with checks of the eigenvector equation and normalization.

The next question is the effect of deleting a vertex together with its edges. This requires a new Laplacian, a new metric, and a separate decision on how to compare the result when several components appear. None of the three centralities considered here is assumed in advance to measure such damage.

## Sources

1. A. Ghosh, S. Boyd, A. Saberi. *Minimizing Effective Resistance of a Graph*. SIAM Review, 50(1), 37-66, 2008. [Full text](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf). The sum of effective resistances, the pseudoinverse Laplacian, and spectral representations.
2. U. Brandes, D. Fleischer. *Centrality Measures Based on Current Flow*. STACS 2005, 533-544. [Full text](https://kim246.wwwdns.kim.uni-konstanz.de/publications/bf-cmbcf-05.pdf). Closeness centrality based on effective resistances and its relation to information centrality.
3. K. Devriendt, R. Lambiotte. *Discrete curvature on graphs from the effective resistance*. Journal of Physics: Complexity, 3, 025008, 2022. [Open version](https://arxiv.org/abs/2201.06385). Vertex resistance curvature $1-\delta_i/2$; its geometric interpretation through the circumcenter is given in Appendix B.3.
4. NetworkX. [Eigenvector centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.eigenvector_centrality.html). The adjacency-matrix definition and conditions for a positive eigenvector. This note normalizes by the sum, not the Euclidean length of the vector.
5. NetworkX. [Krackhardt kite graph](https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.krackhardt_kite_graph.html), [edge list in the source code](https://networkx.org/documentation/stable/_modules/networkx/generators/small.html#krackhardt_kite_graph). Source of the graph topology and numbering; the figure and the three centrality calculations were prepared for this note.
