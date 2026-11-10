---
title: Degree Potential and Centralities
date: 2026-11-03
updated: 2026-11-10
revision: 3
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: degree-potential-and-centralities
order: 7
description: "Ranking by Laplacian circumcenter coordinates: the potential of degree equalization, closeness on trees, generalized degree, eigenvector centrality, and limits of monotonicity."
---

The coordinates of the Laplacian circumcenter define a vertex ranking that accounts for the degree distribution throughout the graph. Its meaning can be expressed without a simplex: it is the potential arising from redistribution of degree surpluses and deficits relative to the mean. On unit-conductance trees, this ranking agrees with closeness; near a regular graph, it agrees with eigenvector centrality to first order. These agreements fail in general.

The geometric definition and diffusion formulas are given in [[Sphere Centers and Graph Heterogeneity]]. This note studies the ranking itself: its relation to the established generalized degree, positive normalization, and limits of interpretation. We also use the [[Centroid, Spanning-Tree, and Eigenvector Centralities|comparison of three centralities]].

Russian version: [[Потенциал степеней и центральности]].

Bi-coordinates $\beta^i$ have upper indices. We use the upper/lower summation convention from [[Bi-coordinates and Di-coordinates|the coordinate note]].

## Degree potential and center coordinates

Consider a finite connected undirected loopless graph on $n\ge2$ vertices. The adjacency matrix $\mathbf A$ contains conductances $c_{ij}=c_{ji}\ge0$; the positive edges form a connected graph. Put

$$
d=\mathbf A\mathbf1,\qquad
\bar d=\frac1n\sum_i d_i,\qquad
b=d-\bar d\mathbf1,\qquad u=\frac1n\mathbf1
$$

The Laplacian and Green matrices are $\mathbf L=\operatorname{diag}(d)-\mathbf A$ and $\mathbf{Gr}=\mathbf L^+$. The columns $d,b,u$ are indexed by vertices; centroids in the series are denoted by $h$, while $b$ denotes degree deviations.

> [!info] Degree potential
> **Definition.** The degree potential is the unique solution
>
> $$
> \boxed{\mathbf L\varphi=b,\qquad
> \mathbf1^{\mathsf T}\varphi=0,\qquad
> \varphi=\mathbf{Gr}\,b}
> \tag{1}
> $$
>
> The associated ranking prefers vertex $i$ to vertex $j$ if $\varphi_i>\varphi_j$. It agrees with ranking by the Laplacian circumcenter coordinates
>
> $$
> \boxed{\beta=u+\frac12\varphi}
> \tag{2}
> $$

Existence and uniqueness follow from $b\perp\mathbf1$ and invertibility of $\mathbf L$ on $\mathbf1^\perp$. The geometric meaning of (2) is proved in the [[Sphere Centers and Graph Heterogeneity#The Laplacian circumcenter|center formulas]]. The coordinates $\beta$ sum to $1$ but need not be nonnegative: a circumcenter can lie outside its simplex.

**Electrical interpretation.** Vertices with $d_i>\bar d$ act as sources, and those with $d_i<\bar d$ as sinks. The potential depends on the paths along which these currents redistribute throughout the network. Vertex degree and vertex potential are therefore not interchangeable characteristics. This electrical potential differs from the normalized potential of a polyform.

**Diffusion interpretation.** For symmetric diffusion with the unnormalized Laplacian,

$$
\dot x(t)=-\mathbf Lx(t),\qquad x(0)=d
$$

we have

$$
\varphi_i=\int_0^\infty\bigl(x_i(t)-\bar d\bigr)\,dt
$$

This is an accumulated **signed** deviation from the mean: surpluses and deficits can cancel. Convergence and the identity are proved in the [[Sphere Centers and Graph Heterogeneity#Center displacement and diffusion|diffusion section]]. The exponential $e^{-t\mathbf L}$ in this process is a matrix exponential, not the exterior exponential of a polyform.


### A first calculation: a three-vertex path

The unit path $a-b-c$ has degrees $(1,2,1)$, so $\bar d=4/3$ and $b=(-1,2,-1)^{\mathsf T}/3$. The endpoint equations and zero-mean condition give

$$
\varphi_a-\varphi_b=-\frac13,\qquad
\varphi_c-\varphi_b=-\frac13,\qquad
\varphi_a+\varphi_b+\varphi_c=0
$$

Hence

$$
\varphi=\frac19(-1,2,-1)^{\mathsf T},\qquad
\beta=\left(\frac5{18},\frac49,\frac5{18}\right)^{\mathsf T}
$$

The middle vertex supplies current $2/3$, while each endpoint receives $1/3$. The potential drop across either unit edge is $1/3$. Degrees first produce a current distribution, then the potential, and finally center coordinates and a ranking.

![The path calculation displays degrees, deviations from mean degree, and potentials separately](<images/Degree Potential on a Path.svg>)

*The path calculation displays degrees, deviations from mean degree, and potentials separately. Arrows point from the source to the sinks; prescribed currents and potentials both sum to zero.*

The [[en/PythonExamples/Example - Metric Parameters of Graphs#Degree potential on a path|Python example]] reproduces this calculation.

## Why cycles change the result

Take the triangle $a,b,c$ and attach the path $c-d-e$. All five edges have unit conductance. To compare with ordinary closeness, let $T_i$ be the sum of shortest-path distances from $i$ to the other vertices, measured by edge count.

| Vertex | $a$ | $b$ | $c$ | $d$ | $e$ |
|---|---:|---:|---:|---:|---:|
| Degree $d_i$ | $2$ | $2$ | $3$ | $2$ | $1$ |
| Coordinate $\beta^i$ | $1/2$ | $1/2$ | $1/2$ | $0$ | $-1/2$ |
| Distance sum $T_i$ | $7$ | $7$ | $5$ | $6$ | $9$ |

Vertex $d$ is closer to the others on average than $a$, but receives a smaller $\beta$. All three triangle vertices have the same potential despite having different degrees.

Here $\bar d=2$ and $b=(0,0,1,0,-1)^{\mathsf T}$. Unit current flows from $c$ to $e$ along $c-d-e$. Vertices $a,b$ have no external sources or sinks, and all current supplied at $c$ leaves along the attached path. Thus no current flows along the triangle edges, and its vertices are equipotential. The example shows what the measure captures and why it differs from closeness.

![Current flows from $c$ to $e$ through $d$](<images/Equal Potentials in a Triangle.svg>)

*Current flows from $c$ to $e$ through $d$. The triangle vertices $a,b,c$ have equal potential, indicated by equal color. Arrows show this external-current distribution, not an orientation of the graph edges.*

## Agreement with closeness on trees

Let the graph be a tree with every conductance equal to $1$. Write $\operatorname{dist}(i,j)$ for the number of edges in its unique path, and put

$$
T_i=\sum_j\operatorname{dist}(i,j),\qquad
\overline T=\frac1n\sum_iT_i
$$

Closeness centrality in a connected graph can be normalized as $(n-1)/T_i$: a smaller distance sum means greater closeness.

> [!info] Trees with unit conductances
> **Theorem.** For such a tree,
>
> $$
> \boxed{\varphi_i=\frac{\overline T-T_i}{n},\qquad
> \beta^i=\frac1n+\frac{\overline T-T_i}{2n}}
> \tag{3}
> $$
>
> Ranking by degree potential therefore agrees exactly with ranking by closeness, including all ties.

> [!note]- Derivation through branch sizes
> **Proof.** For adjacent $i,j$, let $s_{ij}$ be the number of vertices in the component containing $j$ after edge $ij$ is removed. Moving from $i$ to $j$ decreases the distances to these $s_{ij}$ vertices by $1$ and increases the distances to the others by $1$. Thus
>
> $$
> T_j-T_i=n-2s_{ij}
> $$
>
> The components beyond all neighbors of $i$ partition the remaining $n-1$ vertices. Hence
>
> $$
> (\mathbf LT)_i=\sum_{j\sim i}(T_i-T_j)
> =2(n-1)-nd_i
> $$
>
> A tree has $\bar d=2(n-1)/n$, so $\mathbf LT=-nb$. The column $(\overline T\mathbf1-T)/n$ has zero sum and solves (1). Uniqueness gives (3). $\square$

This also gives agreement with resistance closeness: on a unit-conductance tree, effective resistance equals the number of path edges. It does not automatically extend to trees with unequal conductances: (1) uses **weighted** degrees, whereas the branch count above uses unit edges.

### Relation to centroid centrality

> [!info] Three matching rankings on a tree
> **Corollary.** Let all conductances of a tree equal $1$, and put $r_i=\mathrm{Gr}_{ii}$ and $\bar r=n^{-1}\sum_i r_i$. Then
>
> $$
> \boxed{\varphi_i=\bar r-r_i,\qquad
> \beta^i=\frac1n+\frac{\bar r-r_i}{2}}
> $$
>
> Rankings by $\beta$, closeness, and centroid centrality $C_i^{\mathrm{cent}}\propto1/r_i$ agree, including ties. The numerical values of the normalized centralities still differ.

> [!note]- From distances to the Green diagonal
> **Proof.** On a unit-conductance tree, $R_{ij}=\operatorname{dist}(i,j)$. By the [[Centroid, Spanning-Tree, and Eigenvector Centralities#Total resistance to the centroid, the Kirchhoff index, and the radius|resistance-sum formula]],
>
> $$
> T_i=nr_i+\operatorname{tr}\mathbf{Gr},\qquad
> \overline T=2\operatorname{tr}\mathbf{Gr}
> $$
>
> Substitution into (3) gives both formulas. A smaller $r_i>0$ corresponds to a larger $\beta^i$ and greater centroid centrality. $\square$

For any common conductance $c>0$, we have $\varphi_i=c(\bar r-r_i)$; agreement of the rankings is preserved. The unit-scale formula also leads to [[Sphere Centers and Graph Heterogeneity#Equal displacements on unit-conductance trees|equality of the two center displacements]].

## Invariance and choice of scale

> [!info] Basic properties
> **Proposition.** The potential $\varphi$ and coordinates $\beta$ are preserved by uniform scaling of all conductances. Relabeling vertices permutes their coordinates; conductance-preserving automorphisms relate vertices with equal values. Furthermore,
>
> $$
> \varphi=0\quad\Longleftrightarrow\quad
> \beta=u\quad\Longleftrightarrow\quad d_1=\cdots=d_n
> $$

> [!note]- Proof
> **Proof.** Under $c_{ij}\mapsto a c_{ij}$, $a>0$, $\mathbf{Gr}$ is divided by $a$ and $b$ is multiplied by $a$, preserving their product. For a permutation matrix $\mathbf P$, uniqueness sends the solution of (1) to $\mathbf P\varphi$. Finally, $\varphi=0$ is equivalent to $b=0$, since $\mathbf L\varphi=b$. $\square$

Thus the measure does not distinguish vertices of a regular graph, even when no automorphism relates them. Equal scores do not provide a criterion for structural symmetry.

Positivity is unnecessary for ranking. If a positive unit-sum column is required, one may choose

$$
C_i^{(\beta)}=
\frac{\beta^i-\beta_{\min}+1/n}{2-n\beta_{\min}},
\qquad \beta_{\min}=\min_j\beta^j
$$

Since $\beta_{\min}\le1/n$, the denominator is positive, every $C_i^{(\beta)}>0$, the scores sum to $1$, and their order is preserved. The additive term $1/n$ is a scale convention. It does not follow from the geometric definition and does not by itself provide a probabilistic interpretation. Other positive additive terms give the same order but different shares.

For example, on the unit-conductance path $a-b-c-d-e$,

$$
\beta=\left(0,\frac3{10},\frac25,\frac3{10},0\right)^{\mathsf T},
\qquad
C^{(\beta)}=\left(\frac1{10},\frac14,\frac3{10},\frac14,\frac1{10}\right)^{\mathsf T}
$$

Unlike [[Centroid, Spanning-Tree, and Eigenvector Centralities#Expected spanning-tree degree and circumcenter coordinates|expected spanning-tree degree]], this positive normalization currently serves only to display a ranking. Comparing score magnitudes across different graphs requires a separate justification of the chosen scale.

### Ranking direction and the two centers

For the resistance circumcenter, $\alpha^i=1-\delta_i/2$, so [[Centroid, Spanning-Tree, and Eigenvector Centralities#Expected spanning-tree degree and circumcenter coordinates|spanning-tree centrality]] is

$$
C_i^{\mathrm{tree}}=\frac{1-\alpha^i}{n-1}
$$

A larger spanning-tree score corresponds to a **smaller** $\alpha^i$. In (2), preference is instead assigned to a **larger** $\beta^i$, hence a larger potential $\varphi_i$. These are different rules justified by different interpretations. Geometric duality of the two centers does not itself establish a common direction of “greater vertex importance”.

## Adding an edge does not guarantee a better rank

Adding an edge changes both the degree distribution $b$ and the operator $\mathbf{Gr}$. An increase in degree therefore need not increase the potential. Preserving the relative advantage of a vertex that acquires an edge is a rank-monotonicity requirement; it is discussed for generalized degree in [1, §3].

Consider the unit-conductance graph on vertices $1,\ldots,6$ with edges

$$
12,\ 13,\ 14,\ 15,\ 24,\ 26,\ 34,\ 36
$$

Add the unit-conductance edge $25$.

| Coordinate | Before addition | After addition |
|---|---:|---:|
| $\beta^1$ | $43/144$ | $112/366$ |
| $\beta^2$ | $49/144$ | $97/366$ |

Before addition, $\beta^2>\beta^1$; afterward, $\beta^2<\beta^1$. Vertex $2$ acquires an edge but falls below vertex $1$, which is not incident to the new edge. Its own coordinate decreases as well. Every strictly increasing normalization preserves this rank reversal, although changes in the normalized numerical scores may differ.

This is an exact counterexample, not a conclusion from rounded numbers. It limits interpretation as a “vertex's gain from a new edge”, but does not contradict the definition as a potential of degree redistribution.

## Comparison on the Krackhardt kite graph

Use the same numbering and unit conductances as in the [[Centroid, Spanning-Tree, and Eigenvector Centralities#Comparison on the Krackhardt kite graph|centrality comparison on the Krackhardt kite graph]]. For reproducibility, repeat the edge list:

$$
E=\{01,02,03,05,13,14,16,23,25,34,35,36,46,56,57,67,78,89\}
$$

Spanning-tree centrality is $C_i^{\mathrm{tree}}=\delta_i/[2(n-1)]$, where $\delta_i$ is the expected degree of vertex $i$ in a random spanning tree; a tree's probability is proportional to the product of its edge conductances. With unit conductances, the trees are equally likely. The eigenvector $v$ is normalized to sum to $1$.

| Vertex | Coordinate $\beta^i$ | Eigenvector, % | Spanning-tree, % |
|---|---:|---:|---:|
| $0,1$ | $89/80$ | $12.545$ | $9.422$ |
| $2,4$ | $79/80$ | $10.181$ | $7.620$ |
| $3$ | $97/80$ | $17.133$ | $12.838$ |
| $5,6$ | $15/16$ | $14.165$ | $12.125$ |
| $7$ | $-21/80$ | $6.976$ | $12.162$ |
| $8$ | $-189/80$ | $1.712$ | $11.111$ |
| $9$ | $-293/80$ | $0.398$ | $5.556$ |

Grouped rows give the value for each vertex. The ten coordinates $\beta^i$ sum to $1$; these coordinates are **not percentages**. Negative values and values exceeding one are valid affine center coordinates.

The leading ranks are:

| Measure | Highest positions |
|---|---|
| Eigenvector centrality | $3>5=6>0=1$ |
| Spanning-tree centrality | $3>7>5=6$ |
| Degree potential | $3>0=1>2=4>5=6$ |

The mean degree is $18/5$. The degrees along the chain $7-8-9$ are below the mean, so these vertices act as sinks in (1); the potential decreases toward the end of the chain. The spanning-tree score answers a different question: the two bridge edges at vertex $8$ belong to every spanning tree, giving $\delta_8=2$. Its spanning-tree share therefore remains substantial, even though degree potential and eigenvector centrality rank it low.

## What the measure captures

Degree potential favors vertices with a larger accumulated excess over the mean during degree equalization. It combines the initial imbalance with the structure of redistribution paths. In the spectral representation, nonzero Laplacian modes receive factors $1/\lambda_k$, but only modes present in $b$ contribute.

This does not imply a universal measure of vertex importance. Regular graphs produce a constant ranking; adding an edge can worsen a rank; closeness is reproduced on unit-conductance trees but not on all graphs. Positive normalization does not change these limitations. Applicability depends on whether degree equalization matches the meaning of the particular task.

## Relation to generalized degree

Further detail: the meaning of the measure and its examples have been covered. The following sections establish links with other centrality families; applying definition (1) does not require these limit arguments.

László Csató defines **generalized degree** for an unweighted undirected graph by [1, Definition 4]

$$
x(s)=(\mathbf I+s\mathbf L)^{-1}d,\qquad s>0
$$

In [1, Proposition 1, item 7], the limits $x(s)\to d$ as $s\to0$ and $x(s)\to\bar d\mathbf1$ as $s\to\infty$ are established for a connected graph. Here $s$ is the generalized-degree parameter, not diffusion time.

> [!info] The first nonconstant part of the limit
> **Proposition.** For a fixed connected graph,
>
> $$
> x(s)=\bar d\mathbf1+\frac1s\mathbf{Gr}\,b+O(s^{-2}),
> \qquad s\to\infty
> $$
>
> Consequently,
>
> $$
> \boxed{\beta=u+\frac12\lim_{s\to\infty}
> s\bigl(x(s)-\bar d\mathbf1\bigr)}
> \tag{4}
> $$

This is a derivation from the definition of the known family, carried out here. It remains valid for positive edge conductances; the weighted formulation is not attributed to [1].

> [!note]- Spectral expansion
> **Proof.** The constant component of $d$ is preserved by $(\mathbf I+s\mathbf L)^{-1}$. On every eigendirection in $\mathbf1^\perp$ with eigenvalue $\lambda>0$,
>
> $$
> \frac1{1+s\lambda}=\frac1{s\lambda}+O(s^{-2})
> $$
>
> Summing over a finite orthonormal eigenbasis gives the stated expansion and (4). $\square$

If $\beta^i>\beta^j$, then $x_i(s)>x_j(s)$ for sufficiently large $s$. If $\beta^i=\beta^j$, subsequent expansion terms may distinguish the vertices. Thus the precise statement concerns the first nonconstant part of the limit, not full agreement of rankings for all parameter values.

The diffusion connection can also be seen directly:

$$
x(s)=\int_0^\infty e^{-t}e^{-st\mathbf L}d\,dt
$$

Integration on each eigendirection gives the factor $(1+s\lambda)^{-1}$. Changing time to $\tau=st$ gives

$$
s\bigl(x(s)-\bar d\mathbf1\bigr)
=\int_0^\infty e^{-\tau/s}e^{-\tau\mathbf L}b\,d\tau
\longrightarrow\varphi
$$

Exponential decay on $\mathbf1^\perp$ ensures convergence. The electrical, diffusion, and limiting interpretations therefore describe the same column.

## Eigenvector centrality near a regular graph

Eigenvector, or spectral, centrality here means the positive eigenvector of the **adjacency matrix** associated with its largest eigenvalue, normalized by $\mathbf1^{\mathsf T}v=1$. This is the same definition as in the [[Centroid, Spanning-Tree, and Eigenvector Centralities|comparative note]]; it differs from choosing a nonzero Laplacian eigenvector.

Let $\mathbf A_0$ describe a connected weighted regular graph of degree $r$. Consider

$$
\mathbf A(\varepsilon)=\mathbf A_0+\varepsilon\mathbf E,\qquad
f=\mathbf E\mathbf1,\qquad
f_0=f-\bar f\mathbf1,\qquad
\bar f=\frac1n\mathbf1^{\mathsf T}f
$$

The matrix $\mathbf E$ is symmetric with zero diagonal. The parameter is restricted to keep conductances nonnegative and the graph connected. The matrix $\mathbf E$ specifies the adjacency perturbation.

> [!info] First-order agreement
> **Theorem.** Under these conditions, $v(0)=\beta(0)=u$ and
>
> $$
> v'(0)=\frac1n\mathbf{Gr}_0f_0,\qquad
> \beta'(0)=\frac12\mathbf{Gr}_0f_0
> $$
>
> In particular,
>
> $$
> \boxed{\beta(\varepsilon)-u
> =\frac n2\bigl(v(\varepsilon)-u\bigr)+O(\varepsilon^2)}
> \tag{5}
> $$

> [!note]- Differentiating the eigenvector equation
> **Proof.** For a connected nonnegative symmetric adjacency matrix, the largest eigenvalue is simple. At the regular starting point it equals $r$ and has eigenvector $u$, so the eigenpair can be differentiated. From $\mathbf Av=\lambda v$ and $\mathbf1^{\mathsf T}v=1$,
>
> $$
> (r\mathbf I-\mathbf A_0)v'(0)
> =\frac1n\bigl(f-\lambda'(0)\mathbf1\bigr),
> \qquad\mathbf1^{\mathsf T}v'(0)=0
> $$
>
> Summing gives $\lambda'(0)=\bar f$, and $r\mathbf I-\mathbf A_0=\mathbf L_0$, proving the first formula. In (2), $b(0)=0$ and $b'(0)=f_0$; the derivative of the Green matrix multiplies the zero column. Hence $\beta'(0)=\mathbf{Gr}_0f_0/2$. Taylor expansion gives (5). For perturbations admissible on only one side, use the corresponding one-sided limit. $\square$

If two vertices have different first-order corrections, the two rankings agree for sufficiently small positive $\varepsilon$. If their first-order corrections agree, higher orders decide. The theorem does not establish agreement away from regular graphs.

### An exact example of disagreement

Take five vertices $a,b,c,d,e$ with unit-conductance edges

$$
ab,\ bc,\ bd,\ be,\ cd,\ ce
$$

Vertex $b$ is adjacent to every other vertex. Direct solution of (1)-(2) gives

$$
\beta=\left(-\frac{17}{50},\frac9{25},\frac{41}{100},
\frac{57}{200},\frac{57}{200}\right)^{\mathsf T}
$$

Thus $\beta^c>\beta^b$. Yet subtracting the eigenvector equations at $b,c$ gives

$$
(\lambda+1)(v_b-v_c)=v_a>0
$$

so eigenvector centrality prefers $b$.

For a continuous transition from a regular graph, start from $K_5$. Keep conductance $1$ on the six listed edges and assign $1-\varepsilon$ to the other four, where $0\le\varepsilon\le1$. Exact solution gives

$$
\beta^b-\beta^c=
\frac{\varepsilon(8\varepsilon^2-35\varepsilon+25)}
{10(\varepsilon-5)(4\varepsilon-5)}
$$

The denominator is positive on the entire interval. The order reverses at

$$
\varepsilon_*=\frac{35-5\sqrt{17}}{16}\approx0.89903
$$

For eigenvector centrality, throughout the family,

$$
(\lambda+1)(v_b-v_c)=\varepsilon v_a>0
\qquad(\varepsilon>0)
$$

Thus both measures prefer $b$ for $0<\varepsilon<\varepsilon_*$; at $\varepsilon=\varepsilon_*$, the coordinates $\beta^b,\beta^c$ are equal; and for $\varepsilon_*<\varepsilon\le1$, the orders are opposite. Disagreement begins while all edge conductances are still positive.

![[images/Degree Potential - Ranking Disagreement.svg]]

*Left: the final graph at $\varepsilon=1$. Right: score differences along the family. Eigenvector centrality is normalized to sum to $1$; its difference is multiplied by $n/2=5/2$ to match the first-order approximation (5). The comparison concerns the signs of the differences, not the absolute scales of centralities.*

## Status of the results and verification

| Result | Origin and status |
|---|---|
| Geometric formula $\beta=u+\mathbf{Gr}b/2$ | Simplex-center formulas; derivation and external foundations in the sphere-centers note |
| Electrical and diffusion interpretations | Consequences of the Poisson equation for distribution $b$; proved |
| Relation to generalized degree | Csató's family [1]; limiting relation (4) derived here |
| Agreement with closeness and centroid centrality on unit-conductance trees | Formula (3) proved by branch counting; the Green-diagonal relation is a separate corollary |
| Relation to eigenvector centrality | Formula (5) proved by differentiating the eigenvector equation |
| Disagreement and nonmonotonicity | Exact computations on explicitly specified finite graphs |
| Positive scale $C^{(\beta)}$ | A chosen convention; no probabilistic interpretation established |

Proof of a formula is not a claim of scientific novelty. Comparison with [1] establishes the connection to a known family; an exhaustive priority search specifically for $\mathbf{Gr}b$ as a centrality has not been performed.

> [!example]- Reproducible computations
> The script [verify_degree_potential.py](https://github.com/magin67/pmg-notes/blob/v5/checks/metric-parameters/verify_degree_potential.py) checks the stated rational values, the distance identity on three trees, the Green-diagonal relation, equality of the displacements with uniform conductance scaling accounted for, and the difference formula in the one-parameter family. Coordinates are computed independently through the pseudoinverse Laplacian and the circumcenter's equidistance system. For the Krackhardt example, spanning-tree degrees are computed through edge resistances; eigenvector centrality is computed numerically with a check of the eigenvector equation. The script also reproduces the ranking-disagreement figure.

## Source

1. L. Csató. *Measuring centrality by a generalization of degree*. Central European Journal of Operations Research 25(4), 771-790, 2017. [arXiv:1507.02103v3](https://arxiv.org/abs/1507.02103v3), [DOI](https://doi.org/10.1007/s10100-016-0439-6). Definition 4: generalized degree; Proposition 1, item 7: limiting values; §3: rank monotonicity.
