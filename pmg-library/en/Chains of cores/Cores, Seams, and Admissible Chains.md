---
title: "Cores, Seams, and Admissible Chains"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: cores-seams-and-admissible-chains
order: 1
description: "Cores and seams, admissible open chains, shared-edge accounting, and transfer of the active boundary."
---

Russian version: [[ru/Цепи из ядер/Ядра, швы и допустимые цепочки|Ядра, швы и допустимые цепочки]].

The same collection of cycles can be assembled into different graphs. The positions of seams within the cores, the correspondence between their vertices, and the gluing scheme itself may change. The purpose of the “Chains of Cores” series is to determine which of these changes preserve graph characteristics and where that preservation ends.

We begin with open chains of cycles. Changes of configuration with fixed ordered core and seam sizes must be distinguished from permuting seams, branching, and closure. The two chains of three hexagons below provide the initial example: the graphs are nonisomorphic but have the same spanning-tree count and resistance radius. The general explanation is given in [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]], and the spanning-tree calculation in [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]].

Here we define the object and its sequential assembly rule. Boundary data come from [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States - What to Retain from a Component]] and [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]; the necessary definitions are recalled below. Matroid and spectral characteristics are distinguished in [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]] and [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

> [!note] Origins of the constructions
> **From the literature.** Polygon chains whose adjacent cycles share one edge are studied by [Chen–Mohar, §3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). Forest connectivity tables and the operations of introducing, forgetting, and joining boundaries are used by [Mannens–Nederlof, §4.3, Definition 4.14 and Lemmas 4.17, 4.18, 4.21](https://arxiv.org/html/2307.01046#S4.SS3).
>
> **Presentation here.** The terms “core” and “seam” specify the construction data. Established boundary operations are applied to the [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#State polynomials and the full forest passport|full forest passport]], with shared edges accounted for explicitly. The vertex and edge counts, transfer rule, and examples are justified below. No independent priority is claimed.

## Cores and the gluing scheme

> [!info] Cores and the chain scheme
> **Definition.** The cores are specified finite connected simple graphs $K_1,\ldots,K_N$ from which a graph $G$ is assembled. Write $N$ for the number of cores and $n=|V(G)|$ for the number of vertices of the result.
>
> The scheme of an open chain is an auxiliary path $P_N$: its vertex $i$ represents the entire core $K_i$, and its edge $\{i,i+1\}$ represents a prescribed gluing. This is a different graph from $G$. For example, the scheme of a chain of three hexagons has three vertices, whereas the assembled graph below has fourteen.

For each pair of adjacent cores, choose an output subgraph $S_i^+\subset K_i$, an input subgraph $S_{i+1}^-\subset K_{i+1}$, and an isomorphism

$$
\varphi_i:S_i^+\longrightarrow S_{i+1}^-,\qquad 1\le i<N
$$

Assembly identifies corresponding vertices and edges. The image of the selected subgraphs in the result is denoted by $S_i$ and called a seam. An open chain has no initial input or final output; additional external boundaries can be marked separately when another problem requires them.

The correspondence $\varphi_i$ is part of the data. Equal boundary sizes do not specify which vertex of one part is identified with which vertex of the other. In particular, permuting only one side of a seam may change the graph.

## Connected seams and counting shared edges once

From now on the cores are simple cycles $K_i=C_{m_i}$, $m_i\ge3$, with unit conductance on every edge.

> [!info] Connected seam: length measured in vertices
> **Definition.** A connected seam of size $s$ is a proper induced path $P_s$ on $s$ consecutive vertices of a cycle. In this series, seam length is measured **in vertices**:
>
> | $s$ | Seam | Number of shared edges |
> | ---: | --- | ---: |
> | 1 | One vertex | 0 |
> | 2 | One edge with its endpoints | 1 |
> | 3 | A two-edge path | 2 |

For $s\ge2$, the two directions of a path isomorphism are given by $a_j\mapsto b_j$ and $a_j\mapsto b_{s-1-j}$, $0\le j<s$. An arrow along the seam specifies the chosen order of its vertices; the edges of the resulting graph remain undirected. For $s=1$, the correspondence is unique.

> [!info] A shared edge retains unit conductance
> **Shared-edge rule.** Two copies of a seam edge become one edge of conductance $1$. Conductances are not added. Retaining two unit copies would describe a different model: two parallel conductors, electrically equivalent to conductance $2$.

The actual intersection of the core images must be checked. If consecutive vertices $0,1,2,3$ of two cycles are identified in the same order, all three edges $01,12,23$ become shared. Marking only $01$ and $23$ in a drawing does not make this intersection a disconnected seam.

## Admissible open chains of cycles

> [!info] Admissible open chain
> **Definition.** For $N\ge1$, an assembly of cycles is an admissible open chain if the core images retain their vertices and edges and the following conditions hold:
>
> 1. Adjacent cores $K_i,K_{i+1}$ intersect in exactly the prescribed seam $S_i\cong P_{s_i}$.
> 2. Nonadjacent cores have no common vertices.
> 3. In every internal core, the input and output seams are vertex-disjoint.
> 4. There are no other identifications, additional edges, or closure.
>
> In particular,
>
> $$
> 1\le s_i\le\min(m_i,m_{i+1})-1,\qquad
> s_{i-1}+s_i\le m_i\quad(2\le i<N)
> \tag{1}
> $$

The second inequality concerns internal cores only. These numerical inequalities test whether the seams can be placed; the actual intersections must still be checked for a particular assembly. Condition 3 is useful as a local check: intersecting seams would create a common vertex of $K_{i-1}$ and $K_{i+1}$.

> [!info] Numbers of vertices, edges, and independent cycles
> **Proposition 1 (numbers of vertices, edges, and independent cycles).** An admissible chain is connected, and
>
> $$
> \boxed{
> n=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}s_i,\qquad
> |E(G)|=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}(s_i-1)
> }
> \tag{2}
> $$
>
> Consequently, its cycle rank is $|E(G)|-n+1=N$.

> [!note]- Proof of Proposition 1
> **Proof.** Each new cycle is attached along a nonempty path and preserves connectivity. The core $K_i$, $i>1$, adds exactly $m_i-s_{i-1}$ vertices and $m_i-(s_{i-1}-1)$ edges. There are no other intersections. Summing the increments gives (2), and subtracting them gives the cycle rank. For $N=1$, the seam sums are empty. $\square$

These conditions concern the abstract graph. Crossing lines in a drawing without a marked vertex do not create a contact. Regularity of the polygons and the spatial dimension of the drawing are not part of the definition.

![An admissible chain and three violations of its conditions](An%20Admissible%20Chain%20and%20Violations.svg)

**Four constructions.** In the admissible case, the two seams of the middle core share no vertices. The other panels separately show a common vertex of two seams, an additional contact between the end cores, and a disconnected intersection of adjacent cores. The last example retains two shared edges, but they do not form a path. Leaving the conditions of the definition does not mean that every invariant must change; it requires a different analysis.

## Input, output, and active boundaries

> [!info] Input, output, and active boundaries
> The input and output boundaries of a core are the vertex sets of its input and output seams:
>
> $$
> B_i^-=V(S_i^-),\qquad B_i^+=V(S_i^+)
> $$
>
> A boundary here is a marked vertex set. It differs from the algebraic boundary $\partial X$ in PMG and need not be the outer boundary of a plane drawing.
>
> Let $H_j$ be the part already assembled from the first $j$ cores. For $j<N$, its active boundary $B_j=V(S_j)$ consists of the vertices through which $K_{j+1}$ will be attached. Until that step, retain the names of the vertices in $B_j$, their correspondence with the input of the new core, the count $n_j=|V(H_j)|$, and the chosen boundary passport.

After attachment, the internal boundary $B_j$ loses its marks. Its vertices remain in the graph, while the output boundary $B_{j+1}$ of the new core becomes active. The other vertices of the new core also become internal. The last core has no new output: after assembly, summing all states of the remaining marked boundary gives the full forest polynomial.

### Accounting for shared edges when gluing

The formulas for [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#If the parts are intended to share an edge|gluing along a common boundary]] use disjoint edge sets. At each step, therefore, keep the input seam edges in $H_j$ and delete only their duplicate copies from the new core:

$$
K_{j+1}^-=K_{j+1}\setminus E(S_{j+1}^-),\qquad
V(K_{j+1}^-)=V(K_{j+1})
\tag{3}
$$

After matching the boundary names, $H_{j+1}=H_j\cup K_{j+1}^-$ has disjoint constituent edge sets. The output edges stay with the new core and belong to the assembled part at the next step.

If the input seam has $s\ge3$ vertices, its $s-2$ internal vertices become isolated in the separate part $K_{j+1}^-$. In the assembled graph, they remain connected by the seam edges retained in $H_j$. These vertices must not be removed from the data. The full forest passport allows disconnected parts; resistance formulas that require each part to be connected do not automatically apply to this decomposition.

![Attaching a core, changing the active boundary, and an isolated input vertex](Attaching%20a%20Core%20and%20Transferring%20the%20Active%20Boundary.svg)

**One assembly step.** The red seam stays with the assembled part; the blue seam becomes the new output. After gluing, the red vertices remain but are no longer active. In the inset for $s=3$, the middle input vertex is isolated only in the separate fragment $K^-$. This explains why the vertex set must be stored independently of the edge list.

### Transferring the full forest passport

> [!info] Boundary forest state polynomial
> Recall the definition. For a nonempty boundary $B$ and a partition $\pi\in\Pi(B)$, the polynomial
>
> $$
> \mathcal F^{H,B}_\pi(t)=
> \sum_{\pi_B(T)=\pi}t^{|E(T)|}
> \tag{4}
> $$
>
> sums all spanning forests $T$ of $H$ that induce the connectivity partition $\pi$ on $B$. All vertices and components not meeting the boundary are included. The weighted version has the additional factor $\prod_{e\in E(T)}c_e$; in the basic model all $c_e=1$.

> [!info] Removing boundary marks
> **Lemma 2 (removing boundary marks).** Let $C\subseteq D\subseteq V(H)$ with $C\ne\varnothing$. Write $\omega|_C$ for the partition obtained by intersecting the blocks of $\omega$ with $C$ and discarding empty intersections. Then
>
> $$
> \boxed{
> \mathcal F^{H,C}_\eta(t)=
> \sum_{\substack{\omega\in\Pi(D)\\\omega|_C=\eta}}
> \mathcal F^{H,D}_\omega(t)
> }
> \tag{5}
> $$

This is the polynomial form of the standard operation of forgetting a boundary vertex; its counting version is used by Mannens–Nederlof [1, Lemma 4.18].

> [!note]- Proof of Lemma 2
> **Proof.** For each forest $T$, the partition on the smaller boundary is $\pi_C(T)=\pi_D(T)|_C$. Thus the right-hand side groups exactly the same forests as the left-hand side. No edges or vertices of the forest are removed, and the power of $t$ does not change. A component losing its last boundary mark becomes internal and remains in the sum. $\square$

For a step with a new output, set $B=B_j$, $C=B_{j+1}$, and $D=B\cup C$; after renaming, $B$ is also the input of the new core. Admissibility gives $C\cap V(H_j)=\varnothing$. Transfer consists of three operations:

1. **Enlarge the marked set.** Temporarily add the vertices of $C$ to $H_j$ as isolated vertices. A state $\pi$ on $B$ becomes $\pi^\uparrow=\pi\cup\{\{c\}:c\in C\}$ on $D$, with the same polynomial. All other states of this extension are zero.
2. **Attach the fragment.** Form the full passport of $K_{j+1}^-$ relative to $D$ and apply the [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#The passport of the result|pairing law for boundary forest states]] on the common boundary $D$.
3. **Remove the input marks.** Apply (5), retaining only $C$.

> [!info] Transfer formula for the full forest passport
> **Proposition.** To write the step explicitly, let $\mathcal C_D(\alpha,\beta)$ be the forest compatibility indicator. With $r_D(\alpha)=|D|-|\alpha|$, it equals $1$ when $r_D(\alpha\vee\beta)=r_D(\alpha)+r_D(\beta)$ and $0$ otherwise; $\alpha\vee\beta$ is the least common coarsening. Then
>
> $$
> \boxed{
> \mathcal F^{H_{j+1},C}_\eta(t)=
> \sum_{\substack{\pi\in\Pi(B),\ \sigma\in\Pi(D)\\
> (\pi^\uparrow\vee\sigma)|_C=\eta}}
> \mathcal C_D(\pi^\uparrow,\sigma)\,
> \mathcal F^{H_j,B}_\pi(t)\,
> \mathcal F^{K_{j+1}^-,D}_\sigma(t)
> }
> \tag{6}
> $$

> [!note]- Justification of the transfer formula
> **Proof.** After the temporary extension, both parts have common boundary $D$ and disjoint edge sets. The [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#The passport of the result|pairing law for boundary forest states]] selects compatible forests and gives their combined state $\pi^\uparrow\vee\sigma$. Lemma 2 groups these states by the output. The temporary copies of $C$ are identified with the actual output vertices of the core, so no extra vertices remain in the result. The vertex increment is $m_{j+1}-s_j$, as in (2). $\square$

Thus open assembly requires the full passport on the current input and the passport of the new fragment on the union of its input and output. The boundary size may change. For $N>1$, the initial data are the passport of $K_1$ on its output; at the last step, gluing along the input and summing states suffice. For $N=1$, no gluing is required.

Formula (6) concerns the full ordinary forest passport. Transferring reduced coordinates requires compatibility with their quotient construction. The characteristic polynomial $\chi_G(\xi)=\det(\xi I-\mathbf L_G)$ requires separate data from [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]]; sufficiency of a passport for a fixed pair does not by itself define a spectral automaton when the pair changes.

## Two assemblies of three hexagons

Let $N=3$, $m_1=m_2=m_3=6$, and $s_1=s_2=2$. Number the vertices of the middle core $K_2$ as $0,1,\ldots,5$ around the cycle. The input seam is the edge $01$. Choose the output seam as $34$ in configuration A and $23$ in configuration B.

![Two assemblies of three hexagons with marked seams and the core scheme](Two%20Assemblies%20of%20Three%20Hexagons.svg)

**One scheme, two configurations.** In both cases the core scheme is the path $1-2-3$. The red input and blue output of the middle core each have two vertices and are disjoint. Arrows specify the order of seam endpoints; equal numbers denote the same vertex. The geometric drawings represent abstract graphs, not their resistance embeddings.

To specify the graphs independently of the drawing, let $C(v_0,\ldots,v_5)$ denote the cycle in the indicated order, including the last edge $v_5v_0$. Take

$$
\begin{aligned}
K_1&=C(0,1,9,8,7,6),\qquad K_2=C(0,1,2,3,4,5),\\
K_3^{\text{A}}&=C(3,4,13,12,11,10),\qquad
K_3^{\text{B}}=C(2,3,13,12,11,10)
\end{aligned}
\tag{7}
$$

The first seam identifies the ordered pairs $(0,1)$ of the two cores. The second identifies $(3,4)$ or $(2,3)$ of the middle core with the first pair of the third cycle. The final edge set is the union of the edges of the three listed cycles, with every shared edge included once. There are no other identifications.

> [!note]- Proof that the two assemblies are nonisomorphic
> **Proof.** Formula (2) gives $n=18-4=14$ and $|E|=18-2=16$. Each graph has four vertices of degree $3$. Their induced subgraph has two edges in A and three in B: the latter includes the additional edge $12$. Since an isomorphism preserves degrees and adjacency, the graphs are nonisomorphic. $\square$

> [!example] Equal spanning-tree counts and radii
> **Computed directly.** Both graphs have
>
> $$
> \tau=204,\qquad \rho=\frac{43595}{41616}
> \tag{8}
> $$
>
> Here $\tau$ is the spanning-tree count, $\rho=R_{\mathrm{sph}}^2$ is the resistance radius, and $D_{\mathrm{res}}=4\rho$. Definitions and normalization appear in [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|Resistance Radius - Forest Formula and Matroid Invariance]]. We use “isomers with respect to $(\tau,\rho)$” as a working term for nonisomorphic graphs sharing this pair of parameters; agreement of all metric or spectral characteristics is not implied.

The check of (8) uses the original graphs (7), not an assumption of invariance. The spanning-tree count is the determinant of a reduced Laplacian. For a reference vertex $q$, put $\mathbf A=\mathbf L_{\widehat q,\widehat q}$ and $\mathbf d=\operatorname{diag}(\mathbf A^{-1})$. By the [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance#The radius as Laplacian energy|Laplacian energy formula]],

$$
\rho=\frac14\mathbf d^{\mathsf T}\mathbf A\mathbf d
\tag{9}
$$

The program evaluates this in exact rational arithmetic and independently checks it against the centered Green matrix. Equality of the parameter pair in this example is a computational fact. The general proof, a separate nonisomorphism check, and the difference between rooted forests appear in [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]].

## Limits of the model and continuation

Moving seams within cores while retaining $(m_1,\ldots,m_N)$ and $(s_1,\ldots,s_{N-1})$ differs from reordering these data or replacing $P_N$ by a tree. Disconnected seams, additional contacts, and cores other than cycles also define different classes of constructions.

Closure requires marking the initial seam in advance and retaining its vertices together with the current active boundary. A passport only on the current output no longer retains the required connectivity with the forgotten start. The last vertex correspondence and shared-edge rule define ordinary or twisted closure; they change the graph itself. Precise constructions and examples appear in [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain - Rings and the Möbius Effect]].

Other schemes and core types are considered in [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores|Limits of Invariance - Branching, Disconnected Seams, and Other Cores]]. The full spectral automaton and isomer classification belong to the “Spectra of Isomers” direction. Composite cores made from rings of hexagons remain a separate research problem.

## Status and reproducibility

The counting formulas (2), removal of marks (5), and full forest passport transfer (6) are proved. Formula (6) applies established connectivity-table operations and the [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#The passport of the result|pairing law for boundary forest states]]. For the pair (7), nonisomorphism is justified structurally and the parameters (8) are computed directly.

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_admissible_chains.py) records explicit cores, vertex correspondences, and final edges. It checks connectivity, intersections, sizes, transfer of every forest state, one-vertex and multi-edge seams, reversed endpoint correspondence, isolated vertices of separate parts, and the three violations in the figure. The two hexagonal chains are evaluated exactly using two radius formulas. The [instructions and SVG drawing program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md) reproduce the three figures. Finite checks supplement the proofs.

## Sources

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [§4.3, Definition 4.14; Lemmas 4.17, 4.18, 4.21](https://arxiv.org/html/2307.01046#S4.SS3). Forest tables and boundary introduction, forgetting, and joining.
2. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). Polygon chains and the established independence of the spanning-tree count from the placement of single-edge gluings.

Background notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States - What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]], [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]], [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|Resistance Radius - Forest Formula and Matroid Invariance]].

Reading routes, applicability conditions, and the origins of results: [[en/Chains of cores/Chains of Cores|Chains of Cores navigator]].
