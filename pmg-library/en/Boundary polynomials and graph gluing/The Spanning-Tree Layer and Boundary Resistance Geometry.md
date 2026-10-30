---
title: "The Spanning-Tree Layer and Boundary Resistance Geometry"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: spanning-tree-layer-and-boundary-resistance-geometry
order: 4
description: "Groves as a layer of the full passport; spanning-tree pairing, boundary resistance Gram matrices, Schur complements, and the limits of reconstruction from electrical response."
---

The full forest polynomial of a gluing requires boundary-state polynomials. A single spanning-tree coefficient needs fewer data: the spanning-tree coefficient of each connected part and its resistance geometry on the shared boundary. We show how this reduction arises from grove pairing and why it cannot extend to the entire forest passport.

The main law is established in [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]. Groves and their spanning-tree pairing were introduced in [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]], and electrical response and the Schur complement in [[en/Spaces/Vertex Elimination and Induced Couplings|Vertex Elimination and Induced Couplings]]. Here we connect these constructions with the full boundary passport, recalling the necessary definitions and normalizations.

> [!info] Provenance of the results
> **From the literature.** Groves, their spanning-tree pairing, and electrical identities appear in [Kenyon–Wilson, §§2.1–2.2 and Appendix A](https://arxiv.org/html/math/0608422v4#S2.SS1). Schur complements and preservation of resistances belong to established electrical-network theory [2].
>
> **Derivations and exposition here.** These identities yield a law involving the sum of Gram matrices, connected here with the full passport in PMG notation. The examples demonstrate reconstruction limits, without claiming priority for the examples.
> “Derived here” identifies where a proof is given; no claim of scientific priority is made.

## Extracting groves from the full passport

Let $G=(V,E)$ be a finite undirected graph with positive conductances and nonempty marked boundary $B\subseteq V$, where $n=|V|$ and $k=|B|$. Parallel edges are distinguishable; loops may be removed because they belong to no forest. Connectivity is not yet required.

A spanning forest $H$ defines a boundary partition $\pi$. If it has $g$ edges, $b(\pi)$ blocks, and $k_0$ components disjoint from the boundary, then

$$
k_0=n-g-b(\pi)
$$

**Definition.** A grove relative to $B$ is a spanning forest whose every component meets $B$, that is, $k_0=0$. Denote the sum of the weights of groves of state $\pi$ by $g_\pi^{G,B}$, with weight equal to the product of the selected edge conductances.

The equality above and [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#Internal components and groves|the grove extraction formula]] give

$$
\boxed{g_\pi^{G,B}=[t^{\,n-b(\pi)}]\mathcal F^{G,B}_\pi(t)}
\tag{1}
$$

This is the highest possible degree of the state. The coefficient is zero if no such groves exist. Lower degrees correspond to forests with internal components.

Groves are extracted at different degrees in different states. Thus the “spanning-tree layer of the passport” does not mean one common degree of $t$ in all coordinates. For the fully connected state $\{B\}$, its weight is $g_{\{B\}}=\tau(G)$: a grove with one component is a spanning tree.

### Groves of the familiar path

For the unit-weight path $a-b-c-d-e$ with $B=\{a,c,e\}$, the polynomials and grove weights are

$$
\begin{array}{c|c|c|c}
\pi&\mathcal F_\pi(t)&n-b(\pi)&g_\pi\\\hline
ace&t^4&4&1\\
ac\mid e&t^2+2t^3&3&2\\
ae\mid c&0&3&0\\
a\mid ce&t^2+2t^3&3&2\\
a\mid c\mid e&1+4t+4t^2&2&4
\end{array}
$$

For example, the term $t^2$ of state $ac|e$ represents a forest with internal component $\{d\}$. The two contributions of degree $3$ are groves.

![[Three forests of one boundary state.svg]]

**One polynomial, different layers.** The figure from the full-passport note shows three forests of state $ac|e$. Spanning-tree gluing uses the two forests with no internal component; the full forest polynomial needs all three.

## Spanning-tree pairing as a layer of the full law

**An established pairing.** The combinatorial rule (2) corresponds to the spanning-tree matrix of Kenyon–Wilson [1, §§2.1–2.2, equations (5)–(6)]. Here it is derived by extracting a coefficient from the full forest law; the proof verifies that no planarity assumption is needed.

After matching names, let two parts share the boundary $B$, have distinct internal vertices, and have disjoint sets of edge labels. Edges retain their weights and are counted once each; coinciding endpoint pairs give parallel edges. The result has $n=n_1+n_2-k$ vertices.

Extract the coefficient of $t^{n-1}$ from [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#The bilinear law for the full forest polynomial|the full pairing]]. An admissible union of forests is a tree only if both forests are groves and all boundary vertices become connected. Hence

$$
\boxed{
\tau(G_1\#_B G_2)=
\sum_{\substack{\pi\vee\sigma=\{B\}\\b(\pi)+b(\sigma)=k+1}}
g_\pi^{G_1,B}g_\sigma^{G_2,B}
}
\tag{2}
$$

**Proof.** An internal component of either forest cannot connect to the other part, so it cannot occur in the resulting tree. For two groves, $\pi\vee\sigma=\{B\}$ is equivalent to connectivity of the union. Its edge count is $n_1+n_2-b(\pi)-b(\sigma)$, which equals $n-1$ exactly under the second condition in the sum. A connected graph with $n-1$ edges is a tree. Splitting a tree by edge labels and joining groves are inverse operations preserving the product of weights. $\square$

Thus the spanning-tree pairing matrix is obtained from the forest compatibility matrix by adding the connectivity condition $\pi\vee\sigma=\{B\}$. These are different matrices.

Formula (2) agrees with the previously published polyform expression. If $q_\pi=\prod_{A\in\pi}[(A)]^2$ is a partition form and $P_i=\sum_\pi g_\pi^{G_i,B}q_\pi$, then

$$
\tau(G_1\#_B G_2)=\tau_B(P_1P_2),\qquad
T_B=[(b_0\cdots b_{k-1})]^2
$$

Here $\tau_B$ extracts the coefficient of the fixed spanning form $T_B$ in grade $k-1$. This is a well-defined linear functional on polyforms. Its existence does not make the sum of all ordinary forest coefficients into such a functional.

## Electrical response on the boundary

**An established construction.** The Schur-complement definition and its electrical meaning are given in [1, Appendix A.1] and [2]. We recall the necessary theory in the notation of this series.

From now on, assume $G$ is connected. Write $I=V\setminus B$ for its internal vertices. Order the Laplacian matrix by $B,I$:

$$
\mathbf L=
\begin{pmatrix}
\mathbf L_{BB}&\mathbf L_{BI}\\
\mathbf L_{IB}&\mathbf L_{II}
\end{pmatrix}
$$

Prescribe potentials $\mathbf v_B$. There are no external currents at internal vertices, so

$$
\mathbf v_I=-\mathbf L_{II}^{-1}\mathbf L_{IB}\mathbf v_B
$$

The internal block is positive definite: with zero boundary values, zero energy in a connected graph is possible only for the zero potential. The diagonal of $\mathbf L_{II}$ includes connections to $B$; this is not the Laplacian of the graph obtained by deleting the boundary.

**Definition.** The electrical response matrix, or Dirichlet-to-Neumann operator on $B$, is

$$
\boxed{
\boldsymbol\Lambda_B
=\mathbf L_{BB}-\mathbf L_{BI}\mathbf L_{II}^{-1}\mathbf L_{IB},\qquad
\mathbf j_B=\boldsymbol\Lambda_B\mathbf v_B
}
\tag{3}
$$

Currents $\mathbf j_B$ are taken as entering the network. The matrix is symmetric and positive semidefinite, with kernel consisting of constant columns. Formula (3) is the Schur complement of the internal block. If $I=\varnothing$, set $\boldsymbol\Lambda_B=\mathbf L$ and $\det\mathbf L_{II}=1$.

Substituting the minimizing internal potentials into the energy gives

$$
\min_{\mathbf v_I}\mathbf v^{\mathsf T}\mathbf L\mathbf v
=\mathbf v_B^{\mathsf T}\boldsymbol\Lambda_B\mathbf v_B
$$

As proved in [[en/Spaces/Vertex Elimination and Induced Couplings#Response at the selected vertices|the note on elimination]], $-\Lambda_{pq}\ge0$ for $p\ne q$. Thus $\boldsymbol\Lambda_B$ is the Laplacian of an effective graph on $B$. Eliminating internal vertices preserves boundary electrical response and resistances; it does not contract the internal vertices into a chosen boundary vertex.

“Response” here has an electrical meaning. The polynomial responses $U(\sigma;t)=F_{G/\sigma}(t)$ to contraction tests in [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]] are different objects.

## The scale of the spanning-tree coefficient

Denote the total weight of groves with fully separated boundary by

$$
\delta_B(G)=g_{b_0|\cdots|b_{k-1}}^{G,B}
$$

**Theorem (an established identity [1, Lemma A.1]).** Choose $b_0\in B$ and delete its row and column from $\boldsymbol\Lambda_B$. For the resulting matrix $\mathbf H_B$ of size $k-1$,

$$
\boxed{
\delta_B(G)=\det\mathbf L_{II},\qquad
\tau(G)=\delta_B(G)\det\mathbf H_B
}
\tag{4}
$$

**Proof.** Contract all vertices of $B$ to one vertex $h$. By [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test#A linear test of the full passport|the selection rule]], the passing forests have all boundary vertices separated. Spanning trees of the quotient graph correspond exactly to groves of this state. After deleting $h$, the reduced Laplacian of the quotient graph is $\mathbf L_{II}$. By Kirchhoff's theorem, its determinant is $\delta_B(G)$.

Now delete the row and column of $b_0$ from the original Laplacian. Its determinant is $\tau(G)$. Block elimination of internal variables gives the product of $\det\mathbf L_{II}$ and the determinant of the Schur complement, namely $\det\mathbf H_B$. This proves the second equality. $\square$

The effective graph on $B$ has spanning-tree coefficient $\det\mathbf H_B$. The factor $\delta_B(G)$ retains the scale lost when the interior is eliminated. Thus $\boldsymbol\Lambda_B$ alone cannot recover the absolute value of $\tau(G)$. Formula (4) uses ordinary reduced determinants; the product of nonzero Laplacian eigenvalues would introduce an additional factor equal to the vertex count.

## The boundary resistance Gram matrix

On $B=\{b_0,b_1,\ldots,b_{k-1}\}$, fix the differences

$$
d_i=b_i-b_0,\qquad 1\le i\le k-1
$$

Their coordinates have coefficients $+1,-1$ and extend by zeros on internal vertices. Let $\mathbf D$ be the matrix of these columns. The **boundary resistance Gram matrix** is defined in the metric of the original graph:

$$
\mathbf G_B=(d_i\cdot d_j)_{i,j=1}^{k-1}
=\mathbf D^{\mathsf T}\mathbf{Gr}_G\mathbf D,\qquad
\mathbf{Gr}_G=\mathbf L_G^+
$$

Its entries are computed from boundary resistances:

$$
(\mathbf G_B)_{ij}
=\frac{R_{b_0b_i}+R_{b_0b_j}-R_{b_ib_j}}2
$$

**Theorem (resistance formulation of [1, Propositions A.2–A.3]).** In this basis,

$$
\boxed{
\mathbf G_B=\mathbf H_B^{-1},\qquad
\delta_B(G)=\tau(G)\det\mathbf G_B
}
\tag{5}
$$

**Proof.** Inject unit current at $b_j$ and withdraw it through $b_0$, setting the potential at $b_0$ to zero. After eliminating internal potentials, the boundary problem is $\mathbf H_B\mathbf v=\mathbf e_j$. Its $i$th response is the potential difference between $b_i$ and $b_0$, namely $d_i\cdot d_j$. Thus $\mathbf G_B=\mathbf H_B^{-1}$. Taking determinants in (4) gives the second equality. $\square$

In particular, $\boldsymbol\Lambda_B$ and $\mathbf G_B$ determine each other: $\mathbf H_B=\mathbf G_B^{-1}$, and zero row and column sums recover the deleted row and column. This does not identify the principal block of $\mathbf{Gr}_G$ with $\boldsymbol\Lambda_B^+$: their centerings refer to different vertex sets. What agrees is their metric evaluation on boundary differences.

For $k=1$, the matrices $\mathbf H_B,\mathbf G_B$ are empty and their determinants are $1$; then $\delta_B(G)=\tau(G)$. For a connected graph and any nonempty boundary, the data $(\tau(G),\mathbf G_B)$ are equivalent to $(\delta_B(G),\boldsymbol\Lambda_B)$ with names and basis fixed.

### The path after eliminating internal vertices

On the path $a-b-c-d-e$ with boundary $\{a,c,e\}$, eliminate $b,d$. The internal block is $\operatorname{diag}(2,2)$, so $\delta_B=4$. The response matrix and the Gram matrix in the basis $c-a,e-a$ are

$$
\boldsymbol\Lambda_B=\frac12
\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\qquad
\mathbf G_B=\begin{pmatrix}2&2\\2&4\end{pmatrix}
$$

The effective graph is the path $a-c-e$ with conductances $1/2,1/2$. Its spanning-tree coefficient is $1/4$, whereas the original path has $\tau=1$. Formula (4) recovers $1=4\cdot(1/4)$; formula (5) gives $\delta_B=1\cdot4=4$, as does the direct grove count in (1).

![[Boundary response of P5 and spanning-tree scale.svg]]

**Response is preserved, scale changes.** Both graphs have $R_{ac}=2$, $R_{ce}=2$, $R_{ae}=4$. The original path has four groves with fully separated boundary. Their weight $\delta_B=4$ compensates for the change in the spanning-tree coefficient when $b,d$ are eliminated.

## The determinant law for spanning-tree gluing

**Derivation in this note.** Formulas (6)–(8) follow from addition of responses and the established identities (4)–(5). The proof makes this step explicit.

Return to two parts with common boundary $B$ and disjoint edge labels. Now assume **each part is connected**. Boundary vertices are listed in the same order, and both parts use the differences $d_i=b_i-b_0$.

No edge joins an internal vertex of one part to an internal vertex of the other. Thus the internal Laplacian block of the result is block diagonal, and (3)–(4) give

$$
\boldsymbol\Lambda_{G,B}=\boldsymbol\Lambda_{1,B}+\boldsymbol\Lambda_{2,B},\qquad
\delta_B(G)=\delta_B(G_1)\delta_B(G_2)
$$

Responses add for the same boundary potentials. Deleting the shared row and column of $b_0$ gives

$$
\tau(G)=\delta_B(G_1)\delta_B(G_2)\det(\mathbf H_1+\mathbf H_2)
\tag{6}
$$

**Theorem (a consequence of electrical identities).** In the normalized boundary-difference basis,

$$
\boxed{
\tau(G_1\#_B G_2)
=\tau(G_1)\tau(G_2)\det(\mathbf G_1+\mathbf G_2)
}
\tag{7}
$$

**Proof.** By (5), $\delta_B(G_i)=\tau(G_i)\det\mathbf G_i$ and $\mathbf H_i=\mathbf G_i^{-1}$. For invertible matrices,

$$
\mathbf G_1^{-1}+\mathbf G_2^{-1}
=\mathbf G_1^{-1}(\mathbf G_1+\mathbf G_2)\mathbf G_2^{-1}
$$

Substitution into (6) and multiplication of determinants give (7). The matrices need not commute. $\square$

Thus (2) and (7) compute the same spanning-tree coefficient: the former sums grove pairs, and the latter uses their electrical representation. Formula (7) requires no planarity.

For one shared vertex, it gives $\tau(G)=\tau(G_1)\tau(G_2)$. For two vertices $\{a,b\}$, the Gram matrices have size $1$:

$$
\tau(G)=\tau(G_1)\tau(G_2)(R_{ab}^{(1)}+R_{ab}^{(2)})
$$

This is [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#The spanning-tree layer and boundary resistance|the two-point spanning-tree formula]].

### The sum of Gram matrices is not the metric of the result

The Gram matrix of the combined graph is obtained by inverting the sum of responses:

$$
\boxed{
\mathbf G_{G,B}
=(\mathbf G_1^{-1}+\mathbf G_2^{-1})^{-1}
}
\tag{8}
$$

The sum $\mathbf G_1+\mathbf G_2$ in (7) enters the spanning-tree coefficient. It does not equal $\mathbf G_{G,B}$. For a two-point boundary, (8) expresses ordinary parallel connection: $R_{ab}^{G}=(1/R_{ab}^{(1)}+1/R_{ab}^{(2)})^{-1}$.

In a common full vertex space, the Laplacians of the parts add after extension by zero on absent vertices. This does not give the sum of their Greenians: pseudoinversion is not linear, and centering changes with the full vertex set. Formula (8) concerns boundary Gram matrices in one basis.

### Basis normalization

Equality (7) without correction uses differences $b_i-b_0$ or the edges of any tree on $B$: changes between these bases have determinant $\pm1$. Under the same basis change $\mathbf D'=\mathbf D\mathbf A$ in both parts, we get $\mathbf G_i'=\mathbf A^{\mathsf T}\mathbf G_i\mathbf A$, hence

$$
\tau(G)=\tau(G_1)\tau(G_2)
\frac{\det(\mathbf G_1'+\mathbf G_2')}{(\det\mathbf A)^2}
$$

This normalization agrees with [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test#Basis normalization matters|the contraction-test determinant]]. Choosing bases independently in the two parts and adding their matrices without matching the bases is invalid.

Connectivity of each part is essential in (7)–(8). A disconnected part may have no common resistance Gram matrix even if the gluing is connected. Combinatorial formula (2) still applies. Schur formula (6) is also possible if each internal block is invertible, but passing to invertible $\mathbf H_i$ requires additional conditions.

## Two paths with a shared three-point boundary

Glue two unit-weight copies of $P_5$:

$$
G_1:\ a-b_1-c-d_1-e,\qquad
G_2:\ a-b_2-c-d_2-e
$$

Identify the boundary $B=\{a,c,e\}$ by name; $b_1,d_1,b_2,d_2$ are distinct, and no edges are shared. The result consists of two cycles $C_4$ sharing the single vertex $c$. By (7),

$$
\tau(G)=1\cdot1\cdot
\det\begin{pmatrix}4&4\\4&8\end{pmatrix}=16
$$

The nonzero grove contributions to (2) are

$$
1\cdot4+4\cdot1+2\cdot2+2\cdot2=16
$$

The first two terms join a tree of one part to a fully separated grove of the other. The next two correspond to states $ac|e$ and $a|ce$ in opposite orders. An independent check on the resulting graph chooses one of four edges to delete from each cycle, giving $4\cdot4=16$ trees.

Meanwhile, the Gram matrix of the result is

$$
\mathbf G_{G,B}=\frac12\mathbf G_1
=\begin{pmatrix}1&1\\1&2\end{pmatrix}
$$

![[Two copies of P5 and spanning-tree gluing.svg]]

**Three ways to obtain $16$.** The graph consists of two four-cycles with one shared vertex. Colors identify the parts containing the edges; all conductances are $1$. The determinant of the sum of Gram matrices, grove pairing, and direct tree counting agree. Boundary resistances are halved by gluing.

## Limits of reconstruction

### Groves and circular planarity

In a circular planar graph, all boundary vertices lie on the outer face in a specified cyclic order. For such a graph, the Kenyon–Wilson theorem [1, Theorem 1.1] expresses normalized grove weights $g_\pi/\delta_B$ for noncrossing partitions through the response matrix. Crossing states are impossible and have zero weight. Together with $\delta_B$, this recovers absolute grove weights as well. The boundary-placement condition matters for $k\ge4$.

A simple example of the limitation is a star with an internal center and four unit edges to $B=\{1,2,3,4\}$. It has $\delta_B=4$ and $g_{12|34}=0$: connecting both pairs would require the same center. Its effective graph is the complete $K_4$ on the boundary with conductances $1/4$. That graph has $\delta_B=1$ and $g_{12|34}=1/16$. The electrical responses coincide, but the normalized weights of this state differ: $0$ and $1/16$.

The graph $K_4$ is planar, but all four vertices cannot lie on a single outer face without edge crossings. Thus the example does not contradict the theorem for circular planar networks. Nor does it contradict (7): for arbitrary graphs, $(\tau,\mathbf G_B)$ suffices for spanning-tree gluing, but this does not promise recovery of every original grove coordinate.

### Even the whole grove layer does not determine the full passport

Fix boundary $B=\{a,b\}$ and four vertices $a,b,x,y$. The edge $ab$ has conductance $1$, and the internal leaves $x,y$ connect only to $a$. Compare two conductance assignments:

$$
G_A:\ c_{ax}=c_{ay}=1,\qquad
G_B:\ c_{ax}=2,\quad c_{ay}=\frac12
$$

In the Dirichlet problem, the leaf potentials equal the potential at $a$, so the leaves do not affect the boundary current. Both graphs have

$$
\boldsymbol\Lambda_B=
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
\mathbf G_B=(1),\qquad
\tau=\delta_B=1
$$

Their vertex counts also coincide. Both grove coordinates equal $1$: all leaves must be attached, and $ab$ is either selected or omitted. The full passport, however, depends on the free choices of leaf edges. Set

$$
A(t)=(1+t)^2,\qquad
B(t)=(1+2t)(1+\tfrac12t)=1+\tfrac52t+t^2
$$

Then

$$
\begin{array}{c|cc}
&\mathcal F_{a|b}(t)&\mathcal F_{ab}(t)\\\hline
G_A&A(t)&tA(t)\\
G_B&B(t)&tB(t)
\end{array}
$$

and consequently

$$
F_{G_A}(t)=1+3t+3t^2+t^3,\qquad
F_{G_B}(t)=1+\tfrac72t+\tfrac72t^2+t^3
$$

The difference comes from forests in which an internal leaf becomes a separate component. Such forests are absent from the grove layer.

![[The same response and different forest passports.svg]]

**Electrically indistinguishable parts with different passports.** The boundary and topology are identical; only two conductances change, with their product remaining $1$. The response, spanning-tree coefficient, and all grove weights therefore agree, but lower forest coefficients differ. Both graphs admit a circular planar realization with boundary $\{a,b\}$.

If the same additional unit edge $ab$ with a new label is attached to each graph, the resulting polynomials are $(1+2t)A(t)$ and $(1+2t)B(t)$. Both gluings have spanning-tree coefficient $2$, yet their full forest polynomials differ. Thus the reconstruction limit is visible in gluing itself.

## Status of the results and checks

Grove extraction (1) and pairing (2) follow from the full forest law and hold without planarity or connectivity of the parts. In the main setting, metric formulas (3)–(8) are proved for connected undirected graphs with positive conductances; in (7)–(8), both parts are connected and their boundary bases are matched. Boundary electrical response, test polynomials, and the algebraic compatibility matrix are kept distinct.

Reconstruction of normalized groves for circular planar networks is cited from [1]. The four-arm star and internal-leaf examples establish the stated limitations directly. They do not make electrical data unusable: formula (7) specifies exactly the task for which they suffice.

The [exact verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_spanning_geometry.py) compares grove enumeration, reduced determinants, the Schur complement, the original resistance Gram matrix, and both spanning-tree gluing formulas. It separately checks the metric of the result, basis changes, and all numerical examples. Rational arithmetic is used; [instructions for running the checks and reproducing the figures](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) accompany the script. Finite checks supplement the general proofs.

The spanning-tree reduction uses a special layer of the full passport. Reducing the number of linear coordinates while preserving the entire forest polynomial of a gluing requires a different analysis: the radical of the forest compatibility matrix. This reduction and the general Catalan dimension are proved in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]].

In [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]], the Schur complement is applied to the pencil $\xi I-\mathbf L_G$. The static response is obtained at $\xi=0$; for the characteristic polynomial, polynomial minors and the dependence of boundary data on $\xi$ are retained.

## Sources and connections

1. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325–1364. [arXiv:math/0608422, §1.1, Theorem 1.1; §§2.1–2.2; Appendix A, Lemma A.1 and Propositions A.2–A.3](https://arxiv.org/html/math/0608422v4). Groves, spanning-tree pairing, reconstruction of normalized weights under circular planarity, and the relation to the determinant of a reduced response matrix. The external variables $L_{ij}$ in that work equal $-\Lambda_{ij}$ for $i\ne j$, not entries of the original graph's Laplacian matrix.
2. F. Dörfler, F. Bullo. *Kron Reduction of Graphs with Applications to Electrical Networks*. [arXiv:1102.2950, §3.3, Theorem 11, item 1, equation (24)](https://arxiv.org/html/1102.2950#S3.SS3). Schur complements and preservation of effective resistances under elimination of internal vertices. Here we use ordinary Laplacians without additional grounding terms on the diagonal.

Supporting PMG notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]], [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]], [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]], [[en/Spaces/Selected Vertices and the Dirichlet Problem|Selected Vertices and the Dirichlet Problem]], [[en/Spaces/Vertex Elimination and Induced Couplings|Vertex Elimination and Induced Couplings]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/Остовной слой и граничная резистивная геометрия|Русский]]
