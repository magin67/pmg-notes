---
title: Density, Compactness, and Tree Invariance
date: 2026-10-17
updated: 2026-10-17
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: density-compactness-and-tree-invariance
order: 4
description: "Dimensionless graph characteristics: radius compactness, the Kirchhoff index, algebraic connectivity, and efficiency; tree invariance, polyform expressions, and limits of interpretation."
---

The number of edges, the size of the resistance simplex, and the presence of a weak connection between parts of a graph describe different properties. To compare them, we consider several dimensionless measures. The main focus is normalized radius compactness: we explain its geometric meaning, prove its independence of tree shape, and compare it with characteristics that distinguish branching patterns.

The resistance radius is defined in [[Resistance Radius and Diameter of a Graph]], and its relation to the Gram matrix and volume is discussed in [[Resistance Radius of a Set - Gram Matrix and Volume]]. The decomposition through the centroid and the polyform expressions build on [[Centroid, Spanning-Tree, and Eigenvector Centralities]]. This note studies parameters of the whole graph; it does not redefine individual vertex centralities.

## The model and comparable scales

Let $G$ be a connected undirected graph without loops on $n\ge2$ vertices. Existing edges have positive conductances $c_e$; parallel conductors are represented by the sum of their conductances. Write $m$ for the number of distinct adjacent pairs, and define the total conductance and mean weighted degree by

$$
C=\sum_e c_e,\qquad d_i=\sum_jc_{ij},\qquad \bar d=\frac1n\sum_i d_i=\frac{2C}{n}
$$

For a graph with unit conductances, $C=m$. We use the quadratic parameters of PMG:

$$
\rho=R_{\mathrm{sph}}^2,\qquad D_{\mathrm{res}}=4\rho,\qquad Kf=\sum_{i<j}R_{ij}=n\operatorname{tr}\mathbf{Gr}
$$

Here $\mathbf{Gr}=\mathbf L^+$ is the Green matrix. The resistance diameter does not mean the maximum pairwise resistance. Under uniform scaling $c_e\mapsto t c_e$, $t>0$, the mean degree $\bar d$ and the Laplacian eigenvalues are multiplied by $t$, while $R_{ij},\rho,Kf$ are divided by $t$.

For comparison at fixed $n$ and $C$, introduce a reference graph: the complete graph with every edge conductance equal to

$$
c_* = \frac{2C}{n(n-1)}=\frac{\bar d}{n-1}
$$

It has the same mean weighted degree as the original graph. Its parameters are

$$
\rho_* = \frac{(n-1)^2}{n^2\bar d},\qquad
Kf_* = \frac{(n-1)^2}{\bar d},\qquad
\lambda_* = \frac{n\bar d}{n-1}
$$

The last quantity is the common value of the $n-1$ nonzero eigenvalues of the reference Laplacian.

## What the measures capture

### Edge density

The standard density of a simple undirected graph [1] is

$$
p=\frac{2m}{n(n-1)}
$$

It gives the fraction of vertex pairs that are adjacent. For unit conductances, $p=\bar d/(n-1)$. This last identity no longer holds for arbitrary conductances: $p$ records the presence of an edge, not its strength. At fixed $n$, adding a missing edge increases $p$, while strengthening an existing edge leaves it unchanged.

### Normalized radius compactness

**Definition.** The normalized radius compactness is

$$
\boxed{\eta_\rho=\frac{\rho_*}{\rho}
=\frac{(n-1)^2}{n^2\bar d\,\rho}
=\frac{4(n-1)^2}{n^2\bar d\,D_{\mathrm{res}}}}
$$

This is the ratio of the reference radius to the radius of the graph under study. Its reciprocal $\eta_\rho^{-1}=\rho/\rho_*$ is the relative resistance radius: it gives the factor by which the radius exceeds the reference value at the same vertex count and total conductance.

In [2], the original parameter $r(G)$ is defined as the squared linear radius and therefore corresponds to $\rho$. The product $r(G)\bar d$ was called a sparsity index, and its reciprocal a compactness or density index. Applying the complete-graph normalization specified there gives $\eta_\rho$. When using $D_{\mathrm{res}}$, the factor $4$ in the numerator is essential.

Here, “normalized” refers to the choice of reference graph. It does not assert statistical unbiasedness: no probability model or statistical estimand has been specified. The qualifier “radius” identifies the circumsphere; its radius generally differs both from a mean resistance and from the radius of the minimum enclosing ball.

### Compactness based on the Kirchhoff index

The Kirchhoff index accounts for all unordered vertex pairs. Its matrix and spectral representations are standard [3]. To compare it with $\eta_\rho$, use the same reference model:

$$
\boxed{\eta_K=\frac{Kf_*}{Kf}=\frac{(n-1)^2}{\bar d\,Kf}}
$$

At fixed $n$, this is also the ratio of the reference mean pairwise resistance to the graph's mean pairwise resistance. In centroid terms, the same quantity is the ratio of the mean resistances to the centroid. Multiplying all conductances by one positive factor leaves $\eta_K$ unchanged.

### Normalized algebraic connectivity

Let $0=\lambda_1<\lambda_2\le\cdots\le\lambda_n$ be the spectrum of $\mathbf L$. The number $\lambda_2$ is called algebraic connectivity [4]. Define

$$
\eta_2=\frac{\lambda_2}{\lambda_*}
=\frac{(n-1)\lambda_2}{n\bar d}
$$

This measure compares the smallest nonzero eigenvalue with the mean nonzero eigenvalue. A small value indicates a direction in which the Laplacian energy is small relative to the mean scale. This helps detect a weak connection between large parts of the graph.

We use the ordinary weighted Laplacian $\mathbf L$. Normalizing one of its eigenvalues does not mean replacing it by the normalized Laplacian $\mathbf D^{-1/2}\mathbf L\mathbf D^{-1/2}$, where $\mathbf D=\operatorname{diag}(d_i)$.

The names $\eta_\rho,\eta_K,\eta_2$ and their common normalization are specified in this note. The standard status of the underlying quantities $Kf$ and $\lambda_2$ does not imply that these ratios are the only accepted normalizations.

### Efficiency based on shortest paths

For a graph with unit conductances, consider the global efficiency of Latora and Marchiori [5]:

$$
E=\frac1{n(n-1)}\sum_{i\ne j}\frac1{\ell_{ij}}
$$

Here $\ell_{ij}$ is the number of edges in a shortest path. For the complete graph, $E=1$. The measure describes shortest routes, whereas effective resistance accounts for the combined action of all conducting paths.

In the table below, $E$ is computed only for graphs with unit conductances. In a weighted setting, edge lengths and a reference model must first be chosen: conductance is not itself a length. The formula therefore cannot be applied directly to conductances without additional conventions.

### Arboricity as a separate density measure

The arboricity $a(G)$ is the minimum number of forests into which the edge set can be partitioned. By the Nash-Williams theorem [6],

$$
a(G)=\left\lceil\max_{\substack{S\subseteq V\\|S|\ge2}}\frac{|E(S)|}{|S|-1}\right\rceil
$$

Here $E(S)$ denotes the edges with both endpoints in $S$. Unlike $p$, arboricity detects dense subgraphs. It is $1$ for every nontrivial tree, $2$ for a cycle, and $\lceil n/2\rceil$ for $K_n$. We do not normalize it to the complete graph here, and apply it to the structure of existing edges, independently of their conductances.

Forests are explicitly part of this parameter's construction. This is a concrete connection with the graphic matroid; the subsequent results require no general theory of matroid parameters.

## Bounds and decomposition of radius compactness

> [!info] Comparing the normalized parameters
> **Theorem.** For a connected graph with positive conductances,
>
> $$
> 0<\eta_\rho\le\eta_K\le1,\qquad 0<\eta_2\le\eta_K\le1
> $$
>
> Equality $\eta_K=1$ holds precisely for a complete graph with equal conductances. In that case, $\eta_\rho=\eta_2=1$ as well.

> [!proof]- Spectral and geometric proof
> **Proof.** The nonzero eigenvalues satisfy
>
> $$
> \sum_{k=2}^n\lambda_k=n\bar d,\qquad
> \sum_{k=2}^n\frac1{\lambda_k}=\frac{Kf}{n}
> $$
>
> Write $A_\lambda$ and $H_\lambda$ for their arithmetic and harmonic means. Then
>
> $$
> \eta_K=\frac{H_\lambda}{A_\lambda},\qquad
> \eta_2=\frac{\lambda_2}{A_\lambda}
> $$
>
> The inequalities $\lambda_2\le H_\lambda\le A_\lambda$ give the spectral bounds. The two means are equal only when $\lambda_2=\cdots=\lambda_n=a>0$. Then $\mathbf L=a(I-\mathbf1\mathbf1^{\mathsf T}/n)$, so every pair is joined by an edge of conductance $a/n$.
>
> Let $b$ be the centroid and $O$ the circumcenter in a Euclidean realization. The [[Centroid, Spanning-Tree, and Eigenvector Centralities#Total resistance to the centroid, the Kirchhoff index, and the radius|decomposition of the resistance radius]] establishes
>
> $$
> \rho=\frac{Kf}{n^2}+(O-b)^2\ge\frac{Kf}{n^2}
> $$
>
> Substituting into the definition of $\eta_\rho$ gives $\eta_\rho\le\eta_K$. All denominators are positive. $\square$

Introduce the ratio

$$
\chi=\frac{Kf}{n^2\rho}=1-\frac{(O-b)^2}{\rho},\qquad 0<\chi\le1
$$

The definitions give the exact factorization

$$
\boxed{\eta_\rho=\eta_K\chi}
$$

Radius compactness combines two properties: compactness based on mean pairwise resistance, and the relative displacement of the circumcenter from the centroid. Equality $\eta_\rho=\eta_K$ is equivalent to $O=b$, or to a constant Green diagonal. It does not require the graph to be complete. In particular, it holds for vertex-transitive graphs: their symmetries make all diagonal entries of the Green matrix equal.

The two proved chains of inequalities do not establish an ordering between $\eta_\rho$ and $\eta_2$. For example, a star on ten vertices has $\eta_\rho=0.2<0.5=\eta_2$, whereas a path has $\eta_\rho=0.2>\eta_2\approx0.0489$.

## Representation through polyforms

Let $L=\sum_{i<j}c_{ij}[a_j-a_i]^2$, $M=\exp L$, and $M_{n-2}=L^{n-2}/(n-2)!$. Products here are polyform products. Write $\tau(P)$ for the coefficient of the fixed spanning-tree form $T_n=[(a_1\ldots a_n)]^2$; then $\tau(M)=\tau(G)$.

For the auxiliary form of the complete graph with unit conductances,

$$
L_{K_n}=\sum_{i<j}[a_j-a_i]^2
$$

the metric identity gives

$$
Kf=\frac{\tau(M_{n-2}L_{K_n})}{\tau(G)},\qquad
\boxed{\eta_K=\frac{(n-1)^2\tau(G)}{\bar d\,\tau(M_{n-2}L_{K_n})}}
$$

The form $L_{K_n}$ is fixed by the chosen vertex set, but is evaluated in the metric of the original graph $G$. Using this form does not replace the original graph by a complete graph.

Let $b_V=n^{-1}\sum_i a_i$, and let $h_V$ represent the circumcenter. The [[Centroid, Spanning-Tree, and Eigenvector Centralities#The Green matrix, centroid, and local part of the Laplacian|decomposition of centroid forms]] gives

$$
\Psi=\sum_i[b_V-a_i]^2=\frac1nL_{K_n}
$$

Therefore,

$$
\rho=\frac{\tau\!\left(M_{n-2}\left(\frac1{n^2}L_{K_n}+[h_V-b_V]^2\right)\right)}{\tau(G)}
$$

This is a polyform expression for the two terms of the radius, and hence for the two factors $\eta_K$ and $\chi$. The form $[h_V-b_V]^2$ depends on the metric through the center's position. All forms being evaluated belong to the subalgebra of forms on boundaries; norms of the point representatives themselves are not used.

The combinatorial meaning of the next-to-top-grade component is visible in the spanning 2-forest expression

$$
Kf=\frac1{\tau(G)}\sum_{F\in\mathcal F_2}w(F)|A_F|\,|B_F|
$$

Here $\mathcal F_2$ is the set of spanning forests with two components, $A_F,B_F$ are their components, and $w(F)$ is the product of conductances. The coefficients of the next-to-top grade enter with factors determined by component sizes. Simply summing coefficients in an arbitrary expression for the polyform does not reproduce this quantity. The derivation is given in [[Centroid, Spanning-Tree, and Eigenvector Centralities#Spanning 2-forest coefficients and component sizes]].

## Tree invariance

**Definition.** In this note, a parameter is called tree-invariant if it is constant across all trees with unit conductances and a given number of vertices. This specifies a particular property; it does not assert matroid invariance on arbitrary graphs.

> [!info] Radius compactness of any tree
> **Theorem.** If all conductances of a tree on $n\ge2$ vertices equal the same $c>0$, then
>
> $$
> \boxed{\eta_\rho(T)=\frac2n,\qquad \eta_\rho(T)^{-1}=\frac n2}
> $$
>
> The values depend neither on tree shape nor on the common conductance scale.

> [!proof]- Gluing individual edges
> **Proof.** A tree is obtained by successively gluing $n-1$ edges at single vertices. The [[Resistance Radius and Diameter of a Graph#Trees|additivity of the resistance radius]] gives
>
> $$
> \rho(T)=\frac{n-1}{4c},\qquad \bar d(T)=\frac{2c(n-1)}n
> $$
>
> Substitution yields
>
> $$
> \eta_\rho(T)=\frac{(n-1)^2}{n^2\cdot\frac{2c(n-1)}n\cdot\frac{n-1}{4c}}=\frac2n
> $$
>
> Taking the reciprocal of this positive quantity completes the proof. $\square$

This is a general proof. Agreement between a path and a star alone would not suffice to establish the result for all trees.

### Unequal conductances

For an arbitrary positively weighted tree,

$$
\rho(T)=\frac14\sum_e\frac1{c_e},\qquad \bar d(T)=\frac2n\sum_e c_e
$$

Consequently,

$$
\boxed{\eta_\rho(T)=\frac{2(n-1)^2}{n\left(\sum_e c_e\right)\left(\sum_e c_e^{-1}\right)}=\frac2n\frac{H_c}{A_c}\le\frac2n}
$$

Here $A_c$ and $H_c$ are the arithmetic and harmonic means of the $n-1$ conductances. The final bound follows from the inequality between these means; equality holds precisely when all conductances are equal.

Thus, for a fixed multiset of conductances, $\eta_\rho$ is independent of both tree shape and the assignment of those conductances to the edges. Equal vertex counts or equal total conductances alone are insufficient for weighted trees.

For example, a path and a star on four vertices with conductances $1,2,3$ have

$$
\rho=\frac{11}{24},\qquad \bar d=3,\qquad \eta_\rho=\frac9{22}
$$

If all three conductances equal $2$, the total conductance remains $6$, but $\eta_\rho=1/2$. Here the measure responds to conductance heterogeneity, regardless of tree shape.

### Which parameters distinguish branching patterns

The Kirchhoff index of a tree satisfies a different formula [3]:

$$
Kf(T)=\sum_e\frac{s_e(n-s_e)}{c_e}
$$

The numbers $s_e$ and $n-s_e$ are the component sizes after deleting edge $e$. Each of the $s_e(n-s_e)$ separated pairs uses this edge in its unique path. Summing the contributions of the edge resistance $1/c_e$ over all pairs proves the formula.

In a tree with unit conductances, deleting any one edge also produces a spanning forest with two components. The formula therefore agrees directly with the next-to-top-grade component: it accounts for the sizes of the two parts, not just the number of edges being deleted.

For paths and stars with unit conductances,

$$
Kf(P_n)=\sum_{s=1}^{n-1}s(n-s)=\frac{n(n^2-1)}6,\qquad
Kf(K_{1,n-1})=(n-1)^2
$$

Hence

$$
\eta_K(P_n)=\frac3{n+1},\qquad
\eta_K(K_{1,n-1})=\frac{n}{2(n-1)}
$$

For $n\ge4$, the values differ. As $n$ grows, both compactness measures tend to zero for the path. For the star, $\eta_\rho\to0$, but $\eta_K\to1/2$. Independence of the conductance scale therefore does not imply independence of vertex count.

| Parameter | Constant across trees of a given order with unit conductances | Value or reason for variation |
| --- | --- | --- |
| Edge density $p$ | Yes | $2/n$ |
| Radius compactness $\eta_\rho$ | Yes | $2/n$ |
| Relative radius $\eta_\rho^{-1}$ | Yes | $n/2$ |
| Arboricity $a(G)$ | Yes | $1$ |
| Compactness $\eta_K$ | No | Accounts for component sizes when edges are cut |
| Normalized algebraic connectivity $\eta_2$ | No | Accounts for the smallest nonzero eigenvalue |
| Efficiency $E$ | No | Accounts for shortest-path lengths |

Here “No” means that the general property fails, not that every pair of nonisomorphic trees must have different values. The term “tree invariance” describes a parameter's behavior. “Spanning-tree” retains its meaning of a construction through spanning trees, for example when averaging degrees. Without an additional definition, “forest” is not used to label the radius measures: in the adopted model, a disconnected forest has no common finite resistance metric on all its vertices.

## Comparing graphs of the same order

In all the following examples, $n=10$ and every conductance equals $1$. The fan is $K_1\vee P_9$: a new vertex joined to every vertex of a path. The wheel is $K_1\vee C_9$: a new vertex joined to every vertex of a cycle. Thus both names refer to ten vertices in total, including the hub.

The pentagonal prism consists of two cycles $C_5$ joined by five edges between corresponding vertices. The Petersen graph has an outer cycle $C_5$, five edges to the inner vertices, and inner edges joining vertices $2$ steps apart in cyclic order. “Two $K_5$ graphs and a bridge” means two disjoint cliques joined by a single edge. The incomplete graph is obtained from $K_{10}$ by deleting a perfect matching of five edges.

![[Graph Examples for Comparing Compactness.svg]]

The figure shows the fan, wheel, Petersen graph, and two cliques joined by a bridge. Each drawing specifies only the edge topology; the point positions in the plane are not a resistance realization. Adding the closing edge turns the fan into the wheel. The bridge between the cliques is highlighted; deleting it disconnects the graph.

| Graph | $m$ | $p$ | $\eta_\rho$ | $\eta_K$ | $\eta_2$ | $E$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Complete graph $K_{10}$ | 45 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| $K_{10}$ minus a perfect matching | 40 | 0.8889 | 0.9878 | 0.9878 | 0.9000 | 0.9444 |
| Path $P_{10}$ | 9 | 0.2000 | 0.2000 | 0.2727 | 0.0489 | 0.4287 |
| Star $K_{1,9}$ | 9 | 0.2000 | 0.2000 | 0.5556 | 0.5000 | 0.6000 |
| Cycle $C_{10}$ | 10 | 0.2222 | 0.4909 | 0.4909 | 0.1719 | 0.4852 |
| Fan $K_1\vee P_9$ | 17 | 0.3778 | 0.4215 | 0.6759 | 0.2966 | 0.6889 |
| Wheel $K_1\vee C_9$ | 18 | 0.4000 | 0.4997 | 0.7197 | 0.3670 | 0.7000 |
| Complete bipartite graph $K_{5,5}$ | 25 | 0.5556 | 0.9529 | 0.9529 | 0.9000 | 0.7778 |
| Petersen graph | 15 | 0.3333 | 0.8182 | 0.8182 | 0.6000 | 0.6667 |
| Pentagonal prism | 15 | 0.3333 | 0.7832 | 0.7832 | 0.4146 | 0.6296 |
| Two $K_5$ graphs and a bridge | 21 | 0.4667 | 0.3383 | 0.3936 | 0.0640 | 0.6741 |

Values are rounded to four decimal places. They were computed directly for the specified graphs; the ranking does not automatically extend to all orders of these graph families.

The path and star agree in $p$ and $\eta_\rho$, but differ substantially in the other three measures. The geometric reason for the difference between the two compactness measures is visible in $\chi$: for the path, $\chi=11/15$, and for the star, $\chi=9/25$. The star's greater compactness based on the Kirchhoff index is accompanied by a larger relative displacement of the circumcenter, leaving the product $\eta_K\chi$ unchanged.

The fan is denser than the cycle in edge count and more compact according to $Kf$, but has lower radius compactness. For the wheel, $\eta_\rho$ and $\eta_K$ also differ. Thus “compactness” without specifying the measured object does not determine a unique comparison.

The Petersen graph and pentagonal prism have the same $n,m$ and the same degree at every vertex, but different metric measures. Two $K_5$ graphs joined by a bridge are denser than either graph, yet have much lower $\eta_2$: the number of internal edges in the cliques does not remove the weak connection between them.

The arboricity of two $K_5$ graphs joined by a bridge is $3$, as it is for $K_{5,5}$; for the Petersen graph and pentagonal prism it is $2$. These values were obtained by maximizing $|E(S)|/(|S|-1)$ over vertex subsets. Arboricity captures subgraph density, but does not by itself measure the strength of the connections between subgraphs.

## Changing edges and limits of interpretation

### A common conductance scale

The measures $\eta_\rho,\eta_K,\eta_2$ are unchanged under $c_e\mapsto t c_e$. Edge density and arboricity are also preserved, since the edge structure is unchanged. This separates the common conductance scale from the conductance distribution, but does not remove dependence on $n$.

### Adding an edge

For a fixed vertex set, adding a conducting edge does not increase any effective resistance. Consequently, $Kf$ is nonincreasing and $\lambda_2$ is nondecreasing. No analogous general property holds for $\rho$. Moreover, adding an edge changes $\bar d$, and hence changes the reference graph for the normalized measures.

Consider $K_{2,3}$ with unit conductances, and add an edge of conductance $t\ge0$ between the two vertices in the part of size $2$. Direct calculation gives

$$
\rho(t)=\frac13+\frac{t^2}{6(3+2t)^2},\qquad
Kf(t)=6+\frac5{3+2t},\qquad
\bar d(t)=\frac{12+2t}{5}
$$

> [!example]- Checking the radius from the circumcenter system
> Symmetry partitions the vertices into parts of sizes $2$ and $3$. The resistances within the first part, within the second part, and between the parts are respectively
>
> $$
> R_A=\frac2{3+2t},\qquad R_B=1,\qquad R_{AB}=\frac12+\frac1{2(3+2t)}
> $$
>
> If the circumcenter bi-coordinate is $x$ at each vertex of the first part and $y$ at each vertex of the second, then $2x+3y=1$. Equating the two types of rows in $\mathbf R\boldsymbol\alpha=2\rho\mathbf1$ gives
>
> $$
> x=-\frac{t}{2(3+2t)},\qquad y=\frac{1+t}{3+2t}
> $$
>
> Substitution into $2\rho=R_Ax+3R_{AB}y$ reproduces the formula for $\rho(t)$. Summing the resistances gives $Kf=R_A+3R_B+6R_{AB}$. The increase in the radius is thus checked through the equal-distance condition for the circumcenter, independently of the centroid decomposition.

| Graph | $p$ | $\rho$ | $Kf$ | $\eta_\rho$ | $\eta_K$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original $K_{2,3}$ | $3/5$ | $1/3$ | $23/3$ | $4/5$ | $20/23$ |
| After adding an edge of unit conductance | $7/10$ | $17/50$ | $7$ | $80/119$ | $40/49$ |

Edge density increases, no pairwise resistance increases, yet both normalized compactness measures decrease. For $\eta_K$, this reflects the changing reference scale; for $\eta_\rho$, the circumsphere radius itself also increases. In the same example, $\lambda_2=2$ remains unchanged, while $\eta_2$ decreases from $2/3$ to $4/7$ because $\bar d$ increases.

Thus none of the three normalized metric measures can be interpreted, without additional conditions, as necessarily increasing when an edge is added. Efficiency $E$ behaves differently in the model with unit conductances: adding an edge cannot lengthen shortest paths, so $E$ is nondecreasing.

### Weakening a bridge

Take two $K_5$ graphs with unit conductances, and set the conductance of their single connecting bridge to $\varepsilon>0$. The edge structure, $p=7/15$, and $a(G)=3$ remain unchanged, but

$$
\rho=\frac8{25}+\frac1{4\varepsilon},\qquad
Kf=24+\frac{25}{\varepsilon},\qquad
\bar d=4+\frac{\varepsilon}{5}
$$

The radius formula follows by gluing the two cliques and the edge at single vertices. Each of the $25$ pairs lying in different cliques uses the bridge, giving the term $25/\varepsilon$ in $Kf$; the remaining contributions sum to $24$.

As $\varepsilon\to0+$, both compactness measures tend to zero. The bound $0<\eta_2\le\eta_K$ gives the same limit for $\eta_2$. This shows why structural density alone is insufficient to describe metric connectivity. At $\varepsilon=0$, the graph is disconnected; common values of $\rho$ and $Kf$ are not defined in the adopted finite resistance model. The limiting statement does not automatically define parameters for a disconnected graph.

## Choosing a characteristic

| Question | Suitable measure | Important limitation |
| --- | --- | --- |
| What fraction of vertex pairs are directly joined? | $p$ | Ignores conductances and edge arrangement |
| Is there a dense subgraph? | $a(G)$ | Does not assess weak connections between dense parts |
| How small is the circumsphere radius relative to the reference? | $\eta_\rho$ | Does not distinguish tree shape for unit conductances; includes center displacement |
| How small are mean pairwise resistances relative to the reference? | $\eta_K$ | Averages over pairs; the normalization changes with total conductance |
| How weak is the least-energy spectral direction relative to the mean? | $\eta_2$ | Describes one end of the spectrum |
| How short are the shortest routes? | $E$ | Does not account for parallel paths as an electrical network does |

Tree invariance is not inherently a drawback: it is useful when all minimal connected structures of a given order are to receive the same value. But such a measure is insufficient for distinguishing long chains from highly branched trees. A name based on geometric meaning, together with an explicit statement of tree invariance, is more precise than a general label such as “spanning-tree density”.

No universal ranking of graphs by a single “density” is specified here. For metric comparison, retaining the pair $(\eta_K,\chi)$ is useful: it explains which part of radius compactness comes from mean resistances and which from the circumcenter's position.

## Status of the results

The bounds on the normalized parameters, the factorization $\eta_\rho=\eta_K\chi$, tree invariance of radius compactness, and its weighted extension are proved. The polyform expressions follow from the metric identity and the previously proved radius decomposition; links to those results appear in the relevant sections. Arboricity and the theorem on partitioning edges into forests are taken from the cited literature.

The ten-vertex table and the edge-change examples were computed directly. For rational conductances, the Green matrix was obtained in exact rational arithmetic from

$$
\mathbf{Gr}=\left(\mathbf L+\frac1n\mathbf1\mathbf1^{\mathsf T}\right)^{-1}-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

It was used to obtain the resistances and $Kf$. The radius was computed independently in two ways: from the system $\mathbf R\boldsymbol\alpha=2\rho\mathbf1$, $\mathbf1^{\mathsf T}\boldsymbol\alpha=1$, and from the formula $\rho=\operatorname{tr}\mathbf{Gr}/n+\mathbf r^{\mathsf T}\mathbf L\mathbf r/4$, where $r_i=\mathbf{Gr}_{ii}$. For $\eta_2$, numerical diagonalization was used with a check of the eigenvector equation; shortest-path lengths were computed by breadth-first search. Arboricity values were checked by enumerating vertex subsets.

Additional checks covered three different trees with unit conductances on six vertices, a path and a star with conductances $1,2,3$, and two cliques with several positive bridge conductances. These checks supplement the general proofs and do not replace them.

The choice of a measure of damage caused by deleting a vertex together with its edges remains open. It requires a way to compare graphs of different orders and a rule for handling any resulting components. The normalizations considered here do not determine that choice automatically.

## Sources

1. NetworkX. [Density](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.density.html). Standard edge density of a simple undirected graph.
2. D. Malyugin. [Express Analysis of Metric Parameters of Graphs](https://habr.com/ru/articles/534182/), 2020 (in Russian). The original radius-based sparsity and compactness indices; this note clarifies their normalization, naming, and limits of interpretation.
3. A. Ghosh, S. Boyd, A. Saberi. *Minimizing Effective Resistance of a Graph*. SIAM Review, 50(1), 37-66, 2008. [Full text](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf). Total effective resistance, spectral expressions, allocation of fixed total conductance, and tree formulas.
4. M. Fiedler. *Algebraic connectivity of graphs*. Czechoslovak Mathematical Journal, 23(2), 298-305, 1973. [Full text](https://snap.stanford.edu/class/cs224w-readings/fiedler73connectivity.pdf). Algebraic connectivity; the normalization $\eta_2$ is specified separately in this note.
5. V. Latora, M. Marchiori. *Efficient Behavior of Small-World Networks*. Physical Review Letters, 87, 198701, 2001. [Full text](https://www.w3.org/People/Massimo/papers/2001/efficiency_prl_01.pdf). Global efficiency; this note uses the version with unit edge lengths.
6. H. Xiao, Q. Fang. *Arboricity games: the core and the nucleolus*. Mathematical Programming, 198, 1-25, 2023. [Open text](https://doi.org/10.1007/s10107-021-01752-w), Section 3. Definition of arboricity and statement of the theorem of C. S. J. A. Nash-Williams, *Decomposition of finite graphs into forests*, Journal of the London Mathematical Society, 39, 12, 1964.
