---
title: "Why Chain Configuration Preserves Matroid Parameters"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: why-chain-configuration-preserves-matroid-parameters
order: 2
description: "A common plane dual proves matroid invariance; two nonisomorphic hexagonal chains have equal ordinary forest parameters and resistance radii."
---

Russian version: [[ru/Цепи из ядер/Почему конфигурация цепочки сохраняет матроидные параметры|Почему конфигурация цепочки сохраняет матроидные параметры]].

Moving seams on cycle cores can change the graph itself: distances between selected vertices, rooted forest coefficients, and the Laplacian spectrum. Yet admissible open chains with fixed ordered core sizes and seam lengths have isomorphic cycle matroids. Consequently, their ordinary forest polynomial, spanning-tree count, and resistance radius are preserved.

The assembly conditions were introduced in [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. We recall them briefly and prove the assertion. We then independently check two graphs formed from three hexagons: equality of the parameters, nonisomorphism, and the difference between rooted forests.

> [!note] Origin of the result
> The proof rests on standard plane duality for spanning trees and cycle matroids [1]. For polygon chains with single-edge gluings, independence of the spanning-tree count from polygon placement is established by Chen–Mohar [2, §3, Lemma 3.1 and the following paragraph]; the same passage notes that the dual graphs are isomorphic. Here this mechanism is presented for an explicitly specified model of connected seams. The radius consequence uses the forest identity of Richman–Shokrieh–Wu [3, Theorem C / 5.7] in the PMG normalization. This is an adaptation and deduction from known results, not a claim of priority.

## What remains fixed when the configuration changes

Let the cores $K_i$ be simple cycles $C_{m_i}$, where $m_i\ge3$ and $1\le i\le N$. Adjacent cores intersect in exactly a proper induced path $P_{s_i}$; $s_i$ counts **vertices**, and there are $s_i-1$ shared edges. For $s_i=1$ the gluing is at one vertex; for $s_i=2$ one edge is shared.

Nonadjacent cores have no common vertices. The input and output seams of an internal core are vertex-disjoint. There are no other identifications or closure. In particular,

$$
1\le s_i\le\min(m_i,m_{i+1})-1,\qquad
s_{i-1}+s_i\le m_i\quad(2\le i\le N-1)
$$

Every edge has unit conductance; a shared edge occurs once in the result. The resulting graph $G$ is connected. Its vertex count $n$ and edge count satisfy

$$
n=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}s_i,\qquad
|E|=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}(s_i-1),\qquad
|E|-n+1=N
\tag{1}
$$

> [!info] Changing the configuration of a chain
> **Definition.** A change of configuration changes the positions of seams within the cores or the direction of the seam vertex correspondence, while preserving admissibility and both **ordered** sequences
>
> $$
> (m_1,\ldots,m_N),\qquad(s_1,\ldots,s_{N-1})
> \tag{2}
> $$

An arbitrary permutation of core or seam sizes is not included. Reversing both sequences simultaneously merely reverses the direction in which the chain is read. The auxiliary path $P_N$, whose vertices represent cores, is neither the assembled graph nor its plane dual.

## A plane embedding with one face per core

> [!info] A plane embedding with one face per core
> **Lemma 1.** An admissible chain has a plane embedding in which each $K_i$ bounds a distinct bounded face $f_i$. There are no other bounded faces.

> [!note]- Proof of Lemma 1
> **Proof.** Start with one cycle. Suppose $K_1,\ldots,K_j$ have already been embedded and the output seam of $K_j$ is accessible from the outer face.
>
> If the next seam contains an edge, it is a connected arc of the outer-face boundary. The complementary path of the new cycle can be drawn on the outside, in a sufficiently narrow region around this arc, without meeting the rest of the graph. A new face bounded by $K_{j+1}$ appears, and the previous faces remain. For a one-vertex seam, place the new cycle in a free outer sector at the common vertex. Reversing the path correspondence is realized by reflecting the new cycle.
>
> The output seam of $K_{j+1}$ contains no vertex of its input seam. It therefore lies entirely on the new free boundary portion and remains accessible for the next attachment. The absence of contacts with nonadjacent cores excludes further constraints. This completes the induction.
>
> Each step adds exactly one bounded face. This also agrees with Euler's formula: by (1), the number of bounded faces of the connected plane graph is $|E|-n+1=N$. $\square$

Planarity is essential to this proof. Outerplanarity, meaning an embedding with **every** vertex on the outer face, is not required: internal vertices of a multi-edge seam may lie inside the embedding. Neither regular polygons nor a resistance embedding are used.

## Sizes determine the dual multigraph

Let $H$ be the plane dual of this embedding. Its vertices $f_1,\ldots,f_N$ correspond to the core faces, and $f_\infty$ to the outer face. Each edge of the original graph corresponds to a separate dual edge between its incident faces.

Set

$$
\ell_i=s_i-1\quad(1\le i<N),\qquad \ell_0=\ell_N=0
$$

The zero endpoint values mean that there are no external seams. The dual graph has:

- $\ell_i$ parallel edges between $f_i$ and $f_{i+1}$;
- $b_i=m_i-\ell_{i-1}-\ell_i$ parallel edges between $f_i$ and $f_\infty$;
- no other edges.

The formula for $b_i$ removes two disjoint sets of shared edges from the edges of the core. In particular,

$$
\boxed{b_i=m_i-(s_{i-1}-1)-(s_i-1)}
\tag{3}
$$

In (3), the missing term for an end core is taken to be zero. For internal cores, seam disjointness gives $b_i\ge2$; for end cores the same bound follows because the seam is a proper path. Thus every $f_i$ is adjacent to $f_\infty$, and $H$ is connected. For $N=1$, there are two dual vertices and $m_1$ parallel edges.

A one-vertex contact $s_i=1$ contributes no edge between $f_i$ and $f_{i+1}$: a shared primal vertex is not a shared edge. The graph $H$ nevertheless remains connected through $f_\infty$.

![The common dual multigraph of two chains of three hexagons](The%20Common%20Dual%20Multigraph%20of%20the%20Chains.svg)

**Three hexagons.** For $(m_1,m_2,m_3)=(6,6,6)$ and $(s_1,s_2)=(2,2)$, adjacent faces are joined by one edge, while bundles of $5,4,5$ edges join them to the outer face. This is one abstract multigraph for both configurations. All parallel edges remain distinct; a single line with their total weight does not replace them in the matroid.

Thus $H$ depends only on (2). Seam positions determine how the bundle edges are arranged in the plane embedding but do not change the abstract multigraph. For two configurations, match the vertices $f_i$ by index and choose any edge bijection within corresponding bundles.

## From the dual graph to the cycle matroid

> [!info] Cycle matroid
> **Definition.** The cycle matroid $M(G)$ has ground set $E(G)$; its independent sets are the edge sets containing no cycle. In a connected graph its bases are the spanning trees. In a multigraph, two parallel edges form a cycle of length two. See [[en/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges|The Cycle Matroid and Exterior Products of Edges]].

> [!info] Spanning-tree correspondence
> Recall the standard correspondence between spanning trees of a plane graph and its dual [1, the *spanning tree ↔ spanning cotree* corollary]:
>
> $$
> T\text{ is a spanning tree of }G
> \quad\Longleftrightarrow\quad
> (E(G)\setminus T)^*\text{ is a spanning tree of }H
> \tag{4}
> $$

> [!note]- Justification of correspondence (4)
> **Proof.** A cycle of complementary dual edges would separate two parts of the primal vertex set without crossing the tree $T$, which is impossible. The complement contains $|E|-(n-1)=N=|V(H)|-1$ edges, so the resulting acyclic spanning subgraph of $H$ is a tree. The converse follows by the same argument applied to the dual graph. $\square$

> [!info] Matroid invariance of configuration
> **Theorem 1.** Admissible open chains with the same data (2) have isomorphic cycle matroids.

> [!note]- Proof of Theorem 1
> **Proof.** Lemma 1 gives the stated plane embeddings of both chains. Their abstract dual multigraphs are isomorphic by (3). This isomorphism, together with the two primal-to-dual edge correspondences, defines a bijection
>
> $$
> \varphi:E(G_{\text{A}})\longrightarrow E(G_{\text{B}})
> $$
>
> By (4), this bijection maps spanning trees to spanning trees in both directions. Every forest of a connected graph extends to a spanning tree; therefore independent sets also map to independent sets in both directions. This is a matroid isomorphism. $\square$

In terms of the dual matroid, the same conclusion is written $M(G)\cong M(H)^*$. The bases of the dual matroid are the complements of the original bases. Here we compare the matroids of **two chains**; equality of their matroids does not mean that $G$ and $H$ have the same forest polynomial or resistance radius.

The bijection $\varphi$ matches edges. It need not arise from a vertex bijection, so the theorem does not assert that the graphs themselves are isomorphic.

## Which parameters are preserved

### Ordinary forests and the spanning-tree count

> [!info] Preservation of ordinary forest coefficients
> **Corollary.** Let $f_g(G)$ count ordinary spanning forests with $g$ edges: all vertices are retained and no roots are chosen. For the chains in Theorem 1,
>
> $$
> \boxed{f_g(G_{\text{A}})=f_g(G_{\text{B}}),\qquad
> F_{G_{\text{A}}}(t)=F_{G_{\text{B}}}(t)}
> \tag{5}
> $$
>
> Here $F_G(t)=\sum_{g=0}^{n-1}f_g(G)t^g$ and $\tau(G)=f_{n-1}(G)$. Parameters defined through ordinary forest coefficients and their normalizations are also preserved; see [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]] and [[en/Matroid parameters and forest characteristics of graphs/Forest Resistance Scales|Forest Resistance Scales]].

> [!note]- Proof of preservation of ordinary forest coefficients
> **Proof.** The matroid isomorphism of Theorem 1 matches independent sets of each size. These are precisely forests with the specified edge count, giving (5). The two connected chains have the same vertex count by (1), so their spanning-tree counts and the stated normalizations also agree. $\square$

### Edge resistances and the radius

For a unit edge $e=uv$, its effective resistance is its inclusion probability in a uniform random spanning tree:

$$
R_e=\Pr\{e\in T\}
\tag{6}
$$

This equality is derived in the [[en/Matroid parameters and forest characteristics of graphs/Edge Resistances and Random Spanning Trees#Differentiating a Laplacian cofactor|note on edge resistances]]. Since $\varphi$ matches all bases, it preserves $R_e$ on corresponding edges. In particular, it preserves $H_2=\sum_{e\in E}R_e^2$. This concerns original edges and their matroid correspondence; arbitrary vertex pairs are not matched in this way.

> [!info] Preservation of the resistance radius
> **Corollary.** The chains of Theorem 1 have the same resistance radius $\rho=R_{\mathrm{sph}}^2$ and diameter $D_{\mathrm{res}}=4\rho$. We use the following expression for the radius through the forest identity of Richman–Shokrieh–Wu [3, Theorem C / 5.7]:
>
> $$
> \boxed{\rho(G)=\frac{f_{n-2}(G)}{3\tau(G)}-\frac1{12}\sum_{e\in E(G)}R_e^2}
> \tag{7}
> $$
>
> The passage from the original identity to the radius, including the full derivation with conductances, appears in [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|Resistance Radius - Forest Formula and Matroid Invariance]].

> [!note]- Proof of preservation of the radius
> **Proof.** The ordinary two-component forest coefficients and spanning-tree counts agree by (5). By (6), resistances on corresponding edges agree, and hence so do their squared sums. Every quantity on the right of (7) is preserved by $\varphi$; therefore $\rho$ and $D_{\mathrm{res}}$ are preserved. $\square$

Equality of $\tau$ alone does not give this conclusion: (7) also uses ordinary two-component forests and edge resistances. In this theorem, the starting fact is the cycle matroid isomorphism.

### Why rooted forests and the spectrum require different data

In a rooted forest coefficient, each ordinary forest receives a factor equal to the product of its component sizes:

$$
p_g(G)=\sum_{\substack{T\text{ is a spanning forest}\\|E(T)|=g}}
\prod_{C\in\operatorname{Comp}(T)}|V(C)|
$$

The matroid bijection preserves the size of an edge set but need not preserve the vertex sizes of its components. Thus equality of $p_g$ does not follow from (5). By the [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|matrix-forest formula]],

$$
P_G(t)=\det(I+t\mathbf L_G)=\sum_{g=0}^{n-1}p_g(G)t^g,\qquad
\chi_G(\xi)=\xi^nP_G(-1/\xi)
\tag{8}
$$

The last equality is understood as a polynomial identity. The spectrum is related to $P_G$, not to the ordinary forest polynomial $F_G$. The following example exhibits an actual difference.

## Two chains of three hexagons

Write $C(v_0,\ldots,v_5)$ for the cycle joining consecutive vertices and including the closing edge $v_5v_0$. Take

$$
\begin{aligned}
K_1&=C(0,1,9,8,7,6)\\
K_2&=C(0,1,2,3,4,5)\\
K_3^{\text{A}}&=C(3,4,13,12,11,10)\\
K_3^{\text{B}}&=C(2,3,13,12,11,10)
\end{aligned}
\tag{9}
$$

Equal labels specify identified vertices. The middle core has input ordered pair $(0,1)$ and output $(3,4)$ in configuration A or $(2,3)$ in configuration B. The final edge set is the ordinary union of the three sets, with duplicate copies of shared edges removed. Both have $N=3$, $n=14$, and $|E|=16$; nonadjacent cores are disjoint, and the middle core's seams share no vertices.

![Two chains and the subgraphs induced by their degree-three vertices](Nonisomorphism%20of%20Two%20Hexagonal%20Chains.svg)

> [!note]- Proof that the two chains are nonisomorphic
> **Proof.** In configuration A, the vertices of degree $3$ are $0,1,3,4$. They induce the edges $01$ and $34$. In configuration B, the degree-$3$ vertices are $0,1,2,3$, inducing $01,12,23$. An isomorphism preserves degrees and induced subgraphs, but two disjoint edges are not isomorphic to a three-edge path. Hence $G_{\text{A}}\not\cong G_{\text{B}}$. $\square$

Both graphs have the dual multigraph shown above. Deleting the outer-face row and column from its Laplacian gives

$$
\mathbf B=\begin{pmatrix}6&-1&0\\-1&6&-1\\0&-1&6\end{pmatrix},\qquad
\det\mathbf B=6(36-1)-6=204
\tag{10}
$$

By (4) and the matrix-tree theorem, this is the spanning-tree count of both original graphs. The matrix $\mathbf B$ has size $N=3$; it is not the Laplacian of the original graph on $n=14$ vertices. The general determinant and recurrence in the number of cores are derived in [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]].

### Independent exact calculations

The calculation uses the explicit original graphs (9), without assuming invariance. Each graph has its own Laplacian $\mathbf L$; the determinant of a size-$13$ minor gives $\tau=204$.

For reference vertex $q=0$, set $\mathbf A=\mathbf L_{\widehat q,\widehat q}$ and $\mathbf d=\operatorname{diag}(\mathbf A^{-1})$. Then $d_v=R_{v0}$, and the [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance#The radius as Laplacian energy|energy formula for the radius]] gives

$$
\rho=\frac14\mathbf d^{\mathsf T}\mathbf A\mathbf d
=\frac{43595}{41616}
\tag{11}
$$

The second check starts by independently inverting $\mathbf L+\mathbf1\mathbf1^{\mathsf T}/n$ and constructing the centered Green matrix, followed by the resistance matrix $\mathbf R$. The circumcenter is found directly from equidistance conditions:

$$
\mathbf R\boldsymbol\alpha=c\mathbf1,\qquad
\mathbf1^{\mathsf T}\boldsymbol\alpha=1,\qquad \rho=c/2
\tag{12}
$$

Indeed, if $O=\sum_i\alpha_i A_i$ is the circumcenter of the resistance simplex, then $R_{ij}=(A_i-A_j)^2$ and every entry $(\mathbf R\boldsymbol\alpha)_i$ equals $2\rho$. The program solves (12) as a bordered linear system in rational arithmetic. The resulting radius agrees with (11); the energy is additionally checked for all $14$ choices of reference vertex.

Finally, enumerating all $2^{16}$ edge subsets of **each** graph gives ordinary and rooted forest coefficients and spanning-tree edge-inclusion frequencies:

| Parameter | Configuration A | Configuration B |
|---|---:|---:|
| Edges between degree-$3$ vertices | $2$ | $3$ |
| $\tau=f_{13}$ | $204$ | $204$ |
| $f_{12}$, ordinary two-component forests | $1181$ | $1181$ |
| $H_2=\sum_e R_e^2$ | $36713/3468$ | $36713/3468$ |
| $\rho$ | $43595/41616$ | $43595/41616$ |
| $f_4$, ordinary forests with four edges | $1820$ | $1820$ |
| $p_4$, rooted forests with four edges | $21509$ | $21508$ |

> [!example] The same radius with different spectra
> Substituting the independently counted forests and edge resistances into (7) gives a third consistent check:
>
> $$
> \rho=\frac{1181}{3\cdot204}-\frac{36713}{12\cdot3468}
> =\frac{43595}{41616}
> $$
>
> All ordinary coefficients $f_0,\ldots,f_{13}$ agree. The rooted coefficients are independently checked against $\det(I+t\mathbf L)$; already $p_4$ differs. By (8), the coefficients of $\xi^{10}$ in the characteristic polynomials differ, and so do the Laplacian spectra.

> [!info] Isomers with respect to the spanning-tree count and radius
> **Definition.** “Isomers with respect to $(\tau,\rho)$” are nonisomorphic graphs with the same pair of parameters. This is a working term of the series. The graphs (9) form such a pair; agreement of their spectra or full resistance geometry is not asserted.

## Scope and reproducibility

The proof uses cycle cores, connected seams, no contacts between nonadjacent cores, disjoint input and output seams, and an open chain. Reordering seams, changing the gluing scheme, adding contacts, closing the chain, or using other cores requires a fresh analysis of the dual graph or a different proof. A boundary gluing formula does not by itself establish matroid invariance.

The general assertion is proved through (3) and (4). Computations separately check particular constructions. The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_matroid_invariance.py) and [exact results](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/matroid-invariance-results.json) contain the cyclic core orders, seam vertex correspondences, final edges, and an explicit edge bijection for the two hexagonal chains.

The checks cover $11$ configurations and $278\,536$ edge subsets. For each subset, the rank identity of matroid duality is checked, rather than just equality of tree counts. Additional examples include a single cycle, one-vertex and multi-edge seams, both identification directions, different core sizes, and the limiting admissible case $s_{i-1}+s_i=m_i$. Finite enumeration does not replace the general proof. See the [reproduction and drawing instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md).

## Sources and connections

1. J. Erickson. *Tree-Cotree Decompositions*, lecture notes on computational topology. [Cycle-cut duality and the corollary on complementary spanning trees](https://jeffe.cs.illinois.edu/teaching/comptop/2023/notes/10-planar-tree-cotree.html). An exposition of the classical plane duality used in (4).
2. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). Independence of polygon-chain spanning-tree counts from single-edge seam placement and the observation that the dual graphs are isomorphic.
3. H. Richman, F. Shokrieh, C. Wu. *Counting two-forests and random cut size via potential theory*. [Theorem C / 5.7](https://arxiv.org/html/2308.03859v1). The forest identity yielding (7).

Chain construction: [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. Matroid foundations: [[en/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges|The Cycle Matroid and Exterior Products of Edges]], [[en/Matroid parameters and forest characteristics of graphs/Edge Resistances and Random Spanning Trees|Edge Resistances and Random Spanning Trees]], [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|Resistance Radius - Forest Formula and Matroid Invariance]]. Forest normalizations: [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]] and [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

Reading routes, applicability conditions, and the origins of results: [[en/Chains of cores/Chains of Cores|Chains of Cores navigator]].
