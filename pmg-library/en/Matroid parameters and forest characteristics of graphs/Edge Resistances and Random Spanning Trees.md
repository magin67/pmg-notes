---
title: "Edge Resistances and Random Spanning Trees"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: edge-resistances-and-random-spanning-trees
lang: en
description: "Edge inclusion probabilities, derivatives of the spanning-tree polynomial, and the Green matrix. The matroid family H_q, intersections of independent trees, one-point gluing, and combining parallel conductors."
order: 5
---

Forest coefficients sum the weights of independent edge sets. To obtain characteristics of individual edges, ask what fraction of the spanning-tree weight comes from trees containing a chosen edge. The answer is simultaneously an inclusion probability, a derivative of the spanning-tree polynomial, and a metric quantity computed through the Greenian.

This connection was introduced in the [[The Cycle Matroid and Exterior Products of Edges#Edge resistance as a link between the two sides|description of edge resistance]]. Here we prove it using a Laplacian cofactor and construct a family $H_q$ with resistance dimension. It complements the [[The Normalized Forest Polynomial and Power-Sum Parameters|forest power-sum family]] and [[Forest Resistance Scales|neighboring forest ratios]]. The $H_q$ add under one-point gluing; this law is proved separately from matroid invariance.

## The graph and three quantities for an edge

Let $G=(\mathcal V,E)$ be a finite connected undirected loopless graph on $n\ge2$ vertices. Existing edges have positive conductances $c_\ell$, and $d=n-1$. Parallel edges are allowed and retain separate labels. All derivatives with respect to $c_\ell$ hold other edge conductances fixed.

For an existing edge $\ell=\{i,j\}$, distinguish:

| Quantity | Definition | Meaning |
| --- | --- | --- |
| $1/c_\ell$ | The conductor's own resistance | A characteristic of this edge |
| $R_\ell=R_{ij}$ | Effective resistance between its endpoints in the whole graph | Includes all possible paths between $i,j$ |
| $\eta_\ell=c_\ell R_\ell$ | A dimensionless edge characteristic | Identified below with its inclusion probability |

In PMG notation, $a_{ij}=a_j-a_i$ and $R_{ij}=a_{ij}^2=a_{ij}\cdot a_{ij}$. This is a quadratic norm; the linear distance in a Euclidean realization is $\sqrt{R_{ij}}$.

Choose orientation $i\to j$, and let $\mathbf b_\ell$ be the coordinate column of $a_{ij}$: entries at $i,j$ are $-1,+1$, and the others are zero. Then

$$
\mathbf L=\sum_{\ell\in E}c_\ell\mathbf b_\ell\mathbf b_\ell^{\mathsf T},\qquad
\mathbf{Gr}=\mathbf L^+
$$

$$
R_\ell=\mathbf b_\ell^{\mathsf T}\mathbf{Gr}\mathbf b_\ell
=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
\tag{1}
$$

Reversing orientation changes the sign of $\mathbf b_\ell$ but not (1). Parallel edges have the same $R_\ell$, although their conductances and $\eta_\ell$ may differ.

## The spanning-tree distribution

The spanning-tree polynomial and tree weight are

$$
\tau(G;\mathbf c)=\sum_{T\text{ a spanning tree}}w(T),\qquad
w(T)=\prod_{\ell\in T}c_\ell
$$

Positive conductances give $\tau>0$. Throughout this note, $T$ is an ordinary spanning tree without a chosen root.

> [!info] The spanning-tree distribution
> **Definition.** A weighted random spanning tree is sampled from
>
> $$
> \Pr(T)=\frac{w(T)}\tau
> \tag{2}
> $$

If every conductance is the same, all trees have equal weight and the distribution is uniform. Unequal conductances generally give a nonuniform distribution.

The polynomial $\tau$ has degree $d$ and is linear in each individual variable $c_\ell$: a tree cannot contain an edge twice. This remains true with parallel edges because their labels are distinct.

## Kirchhoff's formula in three representations

> [!info] Kirchhoff's formula in three representations
> **Theorem.** For every existing edge,
>
> $$
> \boxed{
> \Pr(\ell\in T)
> =c_\ell\frac{\partial\log\tau}{\partial c_\ell}
> =c_\ell R_\ell
> =\eta_\ell
> }
> \tag{3}
> $$
>
> The probabilistic equality involving effective resistance is Kirchhoff's classical formula; see [1, Section 4.2]. Below it is derived from the weighted matrix-tree theorem in the notation of the current PMG series.

### Differentiating the spanning-tree polynomial

Trees not containing $\ell$ contribute nothing to the derivative. For the others, differentiation removes the factor $c_\ell$ from the weight. Thus

$$
c_\ell\frac{\partial\tau}{\partial c_\ell}
=\sum_{T\ni\ell}w(T)
$$

Division by $\tau$ gives the first equality in (3). This step is combinatorial: only the trees and their weights have been used.

### Differentiating a Laplacian cofactor

Choose a reference vertex $r$ and delete its row and column from $\mathbf L$. This gives the positive definite matrix

$$
\mathbf A=\mathbf L_{\widehat r,\widehat r},\qquad
\det\mathbf A=\tau
$$

The last equality is the [[Forest Coefficients and the Laplacian Polynomial|weighted matrix-tree theorem]]. Let $\widehat{\mathbf b}_\ell$ be $\mathbf b_\ell$ with its entry at $r$ removed. Then

$$
\frac{\partial\mathbf A}{\partial c_\ell}
=\widehat{\mathbf b}_\ell\widehat{\mathbf b}_\ell^{\mathsf T}
$$

Differentiating the determinant gives

$$
\frac{\partial\log\tau}{\partial c_\ell}
=\operatorname{tr}\left(\mathbf A^{-1}
\widehat{\mathbf b}_\ell\widehat{\mathbf b}_\ell^{\mathsf T}\right)
=\widehat{\mathbf b}_\ell^{\mathsf T}\mathbf A^{-1}\widehat{\mathbf b}_\ell
$$

To verify the passage from the cofactor to the Greenian, extend $\mathbf A^{-1}\widehat{\mathbf b}_\ell$ by a zero entry at $r$ and call the result $\mathbf v$. Then $\mathbf L\mathbf v=\mathbf b_\ell$: all other rows satisfy the equation by construction, and row $r$ follows from the zero row sums and $\mathbf1^{\mathsf T}\mathbf b_\ell=0$.

All solutions differ by a constant column, so $\mathbf v=\mathbf{Gr}\mathbf b_\ell+t\mathbf1$. Consequently,

$$
\widehat{\mathbf b}_\ell^{\mathsf T}\mathbf A^{-1}\widehat{\mathbf b}_\ell
=\mathbf b_\ell^{\mathsf T}\mathbf v
=\mathbf b_\ell^{\mathsf T}\mathbf{Gr}\mathbf b_\ell
=R_\ell
$$

This proves the second equality in (3); the last is the definition of $\eta_\ell$. $\square$

### Connection with polyforms

On the Laplacian side, $\tau$ is the coefficient of the top grade $M_d=\tau T_n$ of $M=\exp L$. Varying one edge conductance extracts its contribution to that coefficient.

On the Greenian side, the same derivative is the resistance norm of the original edge vector, computed by (1). The first grade $N_1=\mathrm{Gr}$ of $N=\exp(\mathrm{Gr})$ suffices. Thus a matroid edge characteristic has both Laplacian and Greenian representations. It uses the original edge, not an arbitrary coefficient of the canonical Greenian expansion.

In particular, $\gamma_{ij}=-\mathrm{Gr}_{ij}$ differs from both $R_{ij}$ and $\eta_\ell$. It may be negative, whereas the probabilities (3) are positive. General conventions for the two representations appear in [[Laplacian and Greenian - Mutual Duality of Exponentials]].

## Matroid invariance, bridges, and Foster's formula

**Matroid invariance.** An isomorphism of cycle matroids preserving corresponding conductances gives a bijection of spanning trees preserving their weights and inclusion of each matched edge. Hence it preserves

$$
\eta_\ell,\qquad R_\ell=\frac{\eta_\ell}{c_\ell}
$$

This concerns corresponding edges. A matroid isomorphism need not match arbitrary vertex pairs, so it does not recover the whole resistance matrix $\mathbf R$. The distinction already appears in the [[The Cycle Matroid and Exterior Products of Edges#One matroid, different vertex geometry|path-and-star example]].

**Bridges and probability bounds.** Every existing nonloop edge belongs to at least one spanning tree. Positive weights give

$$
0<\eta_\ell\le1,\qquad 0<R_\ell\le\frac1{c_\ell}
$$

Equality $\eta_\ell=1$ holds exactly when $\ell$ is a bridge. Indeed, every spanning tree contains every bridge. If an edge is not a bridge, its deletion leaves a connected graph with a positive-weight tree omitting it.

Thus the effective resistance of the endpoints equals the edge's own resistance exactly for a bridge. For other edges, the inequality is strict.

**Foster's formula.** The sum of inclusion probabilities equals the number of edges in each spanning tree:

$$
\boxed{\sum_{\ell\in E}\eta_\ell
=\sum_{\ell\in E}c_\ell R_\ell=n-1}
\tag{4}
$$

The combinatorial proof averages $\sum_\ell\mathbf1_{\{\ell\in T\}}=n-1$. A matrix proof directly links the two sides:

$$
\sum_\ell c_\ell\mathbf b_\ell^{\mathsf T}\mathbf{Gr}\mathbf b_\ell
=\operatorname{tr}(\mathbf L\mathbf{Gr})
=\operatorname{tr}\left(\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T}\right)
=n-1
$$

## The edge-parameter family

> [!info] The edge-parameter family
> **Definition.** For integers $q\ge1$, put
>
> $$
> \boxed{
> H_q(G)=\sum_{\ell\in E}\frac{\eta_\ell^q}{c_\ell}
> =\sum_{\ell\in E}c_\ell^{q-1}R_\ell^q
> }
> \tag{5}
> $$
>
> Here $q$ is not a forest grade. It specifies a power of one edge's inclusion probability. In particular,
>
> $$
> H_1=\sum_{\ell\in E}R_\ell,\qquad
> H_2=\sum_{\ell\in E}c_\ell R_\ell^2
> $$

The sum in $H_1$ runs over original edges with multiplicities. It differs from the Kirchhoff index $Kf=\sum_{i<j}R_{ij}$, which counts each vertex pair once.

Every $H_q$ is determined by the weighted cycle matroid: both probabilities and corresponding conductances in (5) are preserved. If conductance has dimension $C$, then

$$
[\eta_\ell]=1,\qquad [R_\ell]=C^{-1},\qquad [H_q]=C^{-1}
$$

Square brackets denote dimensions. Unlike $s_m^{\mathrm{for}}$, with dimension $C^{-m}$, the whole family $H_q$ has one resistance dimension.

Multiplying all conductances by $\sigma>0$ multiplies all tree weights by the common factor $\sigma^d$. Thus distribution (2) and $\eta_\ell$ stay unchanged, while

$$
R_\ell(\sigma G)=\sigma^{-1}R_\ell(G),\qquad
H_q(\sigma G)=\sigma^{-1}H_q(G)
\tag{6}
$$

### Intersections of independent trees

Let $T_1,\ldots,T_q$ be independent trees sampled from (2). For a fixed edge,

$$
\Pr(\ell\in T_1\cap\cdots\cap T_q)=\eta_\ell^q
$$

Linearity of expectation gives

$$
\boxed{
H_q=\mathbb E\left[
\sum_{\ell\in T_1\cap\cdots\cap T_q}\frac1{c_\ell}
\right]
}
\tag{7}
$$

Thus $H_q$ is the expected sum of conductor resistances shared by $q$ independently sampled trees. At $q=1$, this is the sum over one random tree; at $q=2$, over the intersection of two.

Independence here concerns different trees. Inclusion events for different edges in one tree are not assumed independent. In particular, $\eta_\ell^q$ does not describe joint inclusion of $q$ distinct edges in a single tree; that problem requires additional data.

### Monotonicity in the index and the limiting value

Since $0<\eta_\ell\le1$,

$$
0<H_{q+1}\le H_q\le H_1
$$

If the graph has at least one nonbridge edge, then $H_{q+1}<H_q$ for every finite $q$. For a tree, all probabilities equal $1$, and the sequence is constant.

There are finitely many edges, so the limit can be taken term by term:

$$
\boxed{
\lim_{q\to\infty}H_q
=\sum_{\ell\text{ a bridge}}\frac1{c_\ell}
}
\tag{8}
$$

For a graph without bridges the limit is zero. Bridges in (8), like the sums (5), refer to the chosen set of individual edges.

If all conductances equal $c$, Foster's formula gives

$$
H_1=\frac{n-1}{c}
$$

Thus for fixed $n,c$, the first parameter does not distinguish graphs. The second, $H_2$, can already do so.

## One-point gluing

Let $G=G_1\vee G_2$ identify exactly one vertex of two connected graphs with disjoint edge sets. Conductances are retained, and no additional identifications are made.

> [!info] One-point gluing
> **Proposition.** Each edge of either piece retains its inclusion probability and effective resistance after gluing. For every integer $q\ge1$,
>
> $$
> \boxed{H_q(G_1\vee G_2)=H_q(G_1)+H_q(G_2)}
> \tag{9}
> $$

> [!note]- Proof
> **Proof.** Every spanning tree of the result is uniquely the union of spanning trees $T_1,T_2$ of the pieces. Weights multiply and $\tau(G)=\tau(G_1)\tau(G_2)$. Therefore
>
> $$
> \Pr_G(T_1\cup T_2)
> =\frac{w(T_1)}{\tau(G_1)}\frac{w(T_2)}{\tau(G_2)}
> $$
>
> The restrictions of a random tree to the pieces are independent and have the original distributions. Hence $\eta_\ell$ is preserved for $\ell\in E(G_j)$, as is $R_\ell=\eta_\ell/c_\ell$. The sum (5) splits over disjoint edge sets, proving (9). $\square$

Matroid invariance and additivity have different justifications. The former follows from the distribution on weighted bases. The latter uses the special tree decomposition of this gluing. For the forest parameters $s_m^{\mathrm{for}}$, additivity came from the logarithm of a product of forest polynomials; here it comes from preservation of edge probabilities.

In successive one-point gluings of fixed pieces, $H_q$ does not depend on attachment vertices. Formula (9) does not automatically extend to gluing at several vertices or along a shared edge subgraph.

## Examples

### Tree

A tree is its own unique spanning tree. Hence

$$
\eta_\ell=1,\qquad R_\ell=\frac1{c_\ell},\qquad
H_q(T)=\sum_{\ell\in E(T)}\frac1{c_\ell}
\tag{10}
$$

By the [[Forest Resistance Scales#Weighted tree|tree formula]], this sum equals $\xi_1=s_1^{\mathrm{for}}$. The equality covers all $H_q$ but only the first member of the forest power-sum family.

### Equal conductances

For a cycle $C_n$, $n\ge3$, a tree is obtained by deleting one edge. With common conductance $c$, all $n$ choices are equally likely, so $\eta_\ell=(n-1)/n$.

For the complete graph $K_n$, symmetry makes all edge probabilities equal. Foster's formula and the edge count $n(n-1)/2$ give $\eta_\ell=2/n$. The tree $T$ in the table also has $n$ vertices; $T_n$ remains reserved for the PMG top form.

| Graph, each edge of conductance $c$ | $R_\ell$ | $\eta_\ell$ | $H_q$ |
| --- | --- | --- | --- |
| Tree $T$ | $1/c$ | $1$ | $(n-1)/c$ |
| Cycle $C_n$ | $(n-1)/(nc)$ | $(n-1)/n$ | $\frac nc\bigl(\frac{n-1}{n}\bigr)^q$ |
| Complete graph $K_n$ | $2/(nc)$ | $2/n$ | $\frac{n(n-1)}{2c}\bigl(\frac2n\bigr)^q$ |

For example, with unit conductances and four vertices, $H_1=3$ for every connected graph, but for any tree $T$ on these vertices,

$$
H_2(T)=3,\qquad H_2(C_4)=\frac94,\qquad H_2(K_4)=\frac32
$$

### Triangle with conductances $1,2,3$

Let $\ell_1=ab$, $\ell_2=ac$, $\ell_3=bc$ have conductances $c_1=1,c_2=2,c_3=3$. Then

$$
\tau=c_1c_2+c_1c_3+c_2c_3=11
$$

![[Three Random Trees of a Weighted Triangle.svg]]

**All spanning trees.** Write $T_1=\{ab,ac\}$, $T_2=\{ab,bc\}$, $T_3=\{ac,bc\}$. Their weights are $2,3,6$ and probabilities $2/11,3/11,6/11$. An edge's inclusion probability is the sum of probabilities of drawings in which it is solid. For example, $ab$ belongs to $T_1,T_2$, so $\eta_{\ell_1}=5/11$.

Summing tree probabilities for each edge gives

$$
(\eta_{\ell_1},\eta_{\ell_2},\eta_{\ell_3})=\left(\frac5{11},\frac8{11},\frac9{11}\right)
$$

An independent computation from $\mathbf L^+$ gives

$$
(R_{\ell_1},R_{\ell_2},R_{\ell_3})=\left(\frac5{11},\frac4{11},\frac3{11}\right)
$$

Both (3) and Foster's formula are checked: $5/11+8/11+9/11=2$. For the family,

$$
H_1=\frac{12}{11},\qquad
H_2=\frac{25+32+27}{121}=\frac{84}{121},\qquad
H_3=\frac{624}{1331}
$$

For $H_2$, all nine intersections can be displayed:

![[Tree Intersections and Parameter H2.svg]]

**Weighted averaging of intersections.** Every cell uses the same vertex layout: $a$ above, $b$ left, $c$ right. For example, $T_1\cap T_2=\{ab\}$ contributes conductor resistance $1$, while $T_1\cap T_3=\{ac\}$ contributes $1/2$. In the diagonal cell $T_1\cap T_1=T_1$, the sum is $1+1/2=3/2$. Each value is multiplied by its ordered-pair probability $\Pr(T_i)\Pr(T_j)$; all nine contributions sum to $84/121$. Cells are not equally likely. For $H_3$, one similarly uses 27 ordered triples.

## Computation by deletion and contraction

For an existing edge $\ell$, split trees into those containing it and those omitting it. Removing $\ell$ from a tree of the first class and identifying its endpoints gives a tree of $G/\ell$. Therefore

$$
\tau(G)=\tau(G\setminus\ell)+c_\ell\tau(G/\ell),\qquad
\frac{\partial\tau}{\partial c_\ell}=\tau(G/\ell)
$$

It follows that

$$
\boxed{
\eta_\ell=\frac{c_\ell\tau(G/\ell)}{\tau(G)}
=1-\frac{\tau(G\setminus\ell)}{\tau(G)},\qquad
R_\ell=\frac{\tau(G/\ell)}{\tau(G)}
}
\tag{11}
$$

Edge deletion retains every vertex. If it disconnects the graph, $\tau(G\setminus\ell)=0$. This is the global spanning-tree coefficient, not the product of component spanning-tree coefficients. For a single-vertex graph, set $\tau=1$.

After contraction, other conductors parallel to $\ell$ become loops. Loops belong to no spanning tree and are discarded in computing $\tau(G/\ell)$. Other parallel edges retain distinct labels.

Three computational routes are therefore available: direct tree enumeration; cofactors and operations (11); or solving a Laplacian system. In the last approach, for each required edge it suffices to solve

$$
\mathbf A\mathbf x=\widehat{\mathbf b}_\ell,\qquad
R_\ell=\widehat{\mathbf b}_\ell^{\mathsf T}\mathbf x
$$

The entire matrix $\mathbf{Gr}$ need not be constructed explicitly. The resulting $R_\ell$ give $\eta_\ell$ and all required $H_q$ through (3), (5).

## Parallel conductors and the edge representation

Suppose two parallel conductors have conductances $c_1,c_2$ and common endpoint effective resistance $R$. Replacing them by one conductor of conductance $c_1+c_2$ leaves $\mathbf L$, $\mathbf{Gr}$, and the resistance metric unchanged. The ground set of the cycle matroid, however, changes.

Before merging, the probabilities are $c_1R,c_2R$; afterwards the probability is $(c_1+c_2)R$. Two parallel edges cannot both belong to a tree, so the latter is the probability that at least one was included before merging.

The pair's contribution to (5) is

$$
\bigl(c_1^{q-1}+c_2^{q-1}\bigr)R^q
$$

After merging, it is $(c_1+c_2)^{q-1}R^q$. These generally differ. For $q=2$, there is an exact equality:

$$
\boxed{c_1R^2+c_2R^2=(c_1+c_2)R^2}
\tag{12}
$$

Thus $H_2$ is preserved when parallel conductors are merged and can be computed from total pair conductances:

$$
H_2=\sum_{i<j}c_{ij}R_{ij}^2,\qquad
c_{ij}=\sum_{\ell\text{ between }i,j}c_\ell
$$

Other edges retain their resistances and conductances, so their contributions need no comparison. Preservation of $H_2$ under this operation is an additional property; it does not follow from matroid invariance, since the matroids before and after merging may differ.

For example, two vertices with parallel conductances $1,2$ have $R=1/3$. This gives

| Coupling representation | Inclusion probabilities | $H_1$ | $H_2$ | $H_3$ |
| --- | --- | ---: | ---: | ---: |
| Two edges, conductances $1,2$ | $1/3,2/3$ | $2/3$ | $1/3$ | $5/27$ |
| One edge, conductance $3$ | $1$ | $1/3$ | $1/3$ | $1/3$ |

Thus the general family $H_q$ requires a fixed set of individual edges. Electrically merging parallel conductors does not preserve the entire family.

## Connection with the forest family and continuation

We now have two matroid families additive under one-point gluing:

- $s_m^{\mathrm{for}}$, obtained from the logarithm of the normalized forest polynomial;
- $H_q$, obtained from individual edge-inclusion probabilities.

Their definitions, dimensions, and probabilistic meanings differ. For trees, every $H_q$ equals $s_1^{\mathrm{for}}=\xi_1$, but this fails for general graphs. For the unit triangle, for example, $\xi_1=1$ while $H_1=2$ and $H_2=4/3$.

The forest formula for the resistance radius uses precisely $\xi_1=f_{n-2}/\tau$ and $H_2$. Its original source, proof, and translation into the normalization $\rho=R_{\mathrm{sph}}^2$ appear in [[Resistance Radius - Forest Formula and Matroid Invariance]]. Matroid invariance of the two terms and their gluing laws are established independently of the radius formula.

## Status of the results and verification

Kirchhoff's formula, the weighted matrix-tree theorem, and Foster's formula are classical results, not claimed as PMG discoveries. The derivations here connect probabilities, derivatives of the spanning-tree polynomial, and the Green matrix in the adopted notation.

For family (5), the note proves matroid invariance, the independent-tree intersection interpretation, scaling, monotonicity in $q$, the limiting bridge sum, additivity under the specified one-point gluing, and preservation of $H_2$ when parallel conductors are merged. Standard-graph formulas and displayed rational values are computed directly.

Exact rational checks on 53 connected test graphs with 200 edge instances compare spanning-tree enumeration, Laplacian cofactors for every reference vertex, and $\mathbf L^+$. Separate checks cover deletion-contraction, bridges, Foster's formula, $H_1,\ldots,H_5$, scaling, one-point gluing, and parallel-conductor merging. Direct intersection averaging is performed for the weighted and unit triangles and a pair of parallel edges: 84 ordered pairs and triples of trees in total. The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_edge_resistances.py) uses helpers from the adjacent verify_forest_power_sums.py and requires only the Python standard library. Run from the repository root:

    python checks/matroid/verify_edge_resistances.py

Finite checks supplement the general proofs. All probabilistic and metric statements use positive conductances and a connected undirected graph. Orientations used in coordinate computations are arbitrary and do not make the graph balanced; no extension to the balanced model is made.

## References and connections

1. Lyons R., Peres Y. *Probability on Trees and Networks*. Cambridge University Press, 2016, Cambridge Series in Statistical and Probabilistic Mathematics, vol. 42. [DOI: 10.1017/9781316672815](https://doi.org/10.1017/9781316672815). [Author's page with open editions](https://rdlyons.pages.iu.edu/prbtree/prbtree.html). Chapter 4, Section 4.2, *Kirchhoff’s Effective Resistance Formula*: weighted edge-inclusion probabilities and effective resistance.
2. [[The Cycle Matroid and Exterior Products of Edges]]: independent edge sets, bases, and the distinction between edge characteristics and all vertex-pair resistances.
3. [[Forest Coefficients and the Laplacian Polynomial]] and [[Variation of a Single Edge]]: Laplacian cofactors and the spanning-tree coefficient under variation of one conductance.
4. [[The Normalized Forest Polynomial and Power-Sum Parameters]] and [[Forest Resistance Scales]]: forest families, normalizations, and gluing laws.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Рёберные резистенсы и случайное остовное дерево|Русская версия]].
