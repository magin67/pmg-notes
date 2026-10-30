---
title: "Boundary Forest States: What to Retain from a Component"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: boundary-forest-states
order: 1
description: "The full forest passport of a component: marked-boundary partitions, state polynomials, internal components, and groves. Five states of P5 and information lost when the boundary is forgotten."
---

When gluing graphs, we need to know which boundary vertices are already connected inside each part. Two internal paths between the same pair can form a cycle after gluing. The ordinary forest polynomial counts forests by their number of edges but does not record these connections. In general, it therefore does not suffice to compute the forest polynomial of the assembled graph.

The series *Boundary Polynomials and Graph Gluing* develops data that can replace a component in subsequent operations on its boundary. We first retain the polynomials of all boundary states, then describe contraction as a test of these data and gluing as a bilinear pairing. We extract spanning-tree data and resistance geometry from the full passport, and then reduce the number of linear coordinates. A separate final step concerns the characteristic polynomial: the ordinary forest passport and spectral boundary data serve different purposes.

This note defines the initial coordinates of the full forest passport. The main example is a five-vertex path with three marked boundary vertices. It exhibits different forests with the same state, components containing no boundary vertices, and information lost when the states are summed.

> [!info] Provenance of the results
> **From the literature.** Boundary partitions and tables of forest states appear in [Mannens–Nederlof, §4](https://arxiv.org/html/2307.01046#S4); groves appear in [Kenyon–Wilson, §1.1](https://arxiv.org/html/math/0608422v4#S1.SS1).
>
> **PMG exposition.** “Full forest passport” is the name used here for the vector of generating polynomials. Its comparison with partition forms and the examples serve the purposes of this series. The formulas counting internal components and extracting groves are elementary consequences of the definition of a forest.
> “Derived here” identifies where a proof is given; no claim of scientific priority is made.

## A graph with a marked boundary

Let $G=(V,E)$ be a finite undirected loopless graph, let $n=|V|$, and give each edge $\ell$ a positive conductance $c_\ell$. Parallel edges, when present, are distinct; selecting two parallel edges creates a cycle and does not give a forest. The graph $G$ need not be connected.

**Definition.** The boundary of a component is a nonempty set $B\subseteq V$ chosen in advance. The vertices in $V\setminus B$ are called internal. We write $(G,B)$ for the graph with its marked boundary.

Here “component” means a part of a future assembly, not necessarily a connected component. The boundary is part of the input data. Gluing also requires a specified correspondence between the boundary vertices of the parts. We assume neither a planar embedding nor a boundary on the outer face.

**Definition.** A spanning forest $H=(V,A)$ of $G$ is an acyclic subgraph on the entire vertex set $V$, where $A\subseteq E$. The set $A$ need not be maximal. In particular, the empty edge set gives a forest of $n$ isolated vertices.

Write the number of edges and the weight of a forest as

$$
g(H)=|A|,\qquad w(H)=\prod_{\ell\in A}c_\ell
$$

The empty product is $1$. No roots are chosen in the components. We retain the edge-count variable used in [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|the note on forest coefficients]]:

$$
F_G(t)=\sum_{H\text{ a spanning forest of }G}w(H)t^{g(H)}
$$

Our main example is

$$
G=P_5:\quad a-b-c-d-e,\qquad B=\{a,c,e\}
$$

All four conductances are $1$; the internal vertices are $b,d$.

![[Path P5 with a three-point boundary.svg]]

**The fixed boundary.** Gold circles mark $a,c,e$. Every forest of this graph retains all five vertices, including an isolated $b$ or $d$. Segment lengths in the drawing indicate only vertex placement, not resistance.

## The boundary partition induced by a forest

**Definition.** A forest $H$ induces a partition $\pi_B(H)$ of $B$: two boundary vertices belong to the same block if and only if they lie in the same connected component of $H$. This partition is called the boundary state of the forest.

Let $\Pi(B)$ be the set of all partitions of $B$, and let $b(\pi)$ be the number of blocks of $\pi$. The notation $ac|e$ means the blocks $\{a,c\}$ and $\{e\}$; their order is immaterial.

If $\mathcal C(H)$ is the set of components of the forest, then

$$
\pi_B(H)=\{C\cap B:C\in\mathcal C(H),\ C\cap B\ne\varnothing\}
$$

Thus a partition block consists only of boundary vertices. The corresponding forest component may also contain internal vertices. Components disjoint from $B$ do not enter the partition; we call them **internal components of the forest**.

A three-point boundary has five formal states:

$$
ace,\qquad ac|e,\qquad ae|c,\qquad a|ce,\qquad a|c|e
$$

![[Five partitions of a three-point boundary.svg]]

**Blocks and edges.** Colored regions group vertices belonging to the same block. These are partition diagrams, not subgraphs of $P_5$: the region joining $a$ and $e$ does not indicate an edge $ae$. The state $ae|c$ belongs to $\Pi(B)$, although no forest of this path realizes it.

## State polynomials and the full forest passport

**Origin of the construction.** [Definition 4.14 of Mannens–Nederlof](https://arxiv.org/html/2307.01046#S4.SS3) already groups forests by their boundary partition; internal components are allowed. Below, we equip this counting table with weights and an edge-count variable. This is a polynomial version of an established construction.

**Definition.** The polynomial of a state $\pi\in\Pi(B)$ is

$$
\boxed{
\mathcal F^{G,B}_\pi(t)
=\sum_{\substack{H\text{ a spanning forest of }G\\\pi_B(H)=\pi}}
w(H)t^{g(H)}
}
\tag{1}
$$

An unrealizable state has polynomial zero. We omit the superscripts when $G,B$ are fixed. The coefficient of $t^g$ is the sum of the weights of all forests with $g$ edges and the given state. Internal components are allowed and included in this count.

**Definition.** The full boundary forest passport in state coordinates is the vector

$$
\Sigma_B(G;t)=\bigl(\mathcal F^{G,B}_\pi(t)\bigr)_{\pi\in\Pi(B)}
$$

The boundary vertex names and the number $n$ are retained alongside this vector. The latter matters: adding an isolated internal vertex leaves the polynomials (1) unchanged but changes the number of components of every forest. “Full” means that all states and all spanning forests are included; it asserts neither reconstruction of the graph itself nor minimality of the number of coordinates.

### Free states and partition forms

For linear operations, first introduce the free space

$$
\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R\,s_\pi,
\qquad
\mathbf f_{G,B}(t)=\sum_{\pi\in\Pi(B)}\mathcal F^{G,B}_\pi(t)s_\pi
$$

The symbols $s_\pi$ are linearly independent by definition. The vector $\mathbf f_{G,B}(t)$ is a polynomial with values in $\mathscr S_B$.

The linear functional that forgets the boundary is well-defined on this space:

$$
\varepsilon(s_\pi)=1
$$

**Proposition.** Forgetting the state gives the ordinary forest polynomial:

$$
\boxed{
\varepsilon\bigl(\mathbf f_{G,B}(t)\bigr)
=\sum_{\pi\in\Pi(B)}\mathcal F^{G,B}_\pi(t)
=F_G(t)
}
\tag{2}
$$

**Proof.** Every forest induces exactly one boundary partition. Hence the sums in (1) divide all forests into disjoint classes without changing their weights or numbers of edges. $\square$

A state $s_\pi$ must be distinguished from the partition form

$$
q_\pi=[(B_1)\cdots(B_{b(\pi)})]^2,
\qquad \pi=B_1|\cdots|B_{b(\pi)}
$$

Singleton blocks contribute unit factors. The forms $q_\pi$, defined in [[en/Structural identities/Partition Forms and the Tetrahedron Identity|Partition Forms and the Tetrahedron Identity]], satisfy structural identities. The map $s_\pi\mapsto q_\pi$ can therefore have a nonzero kernel. For $\varepsilon$ to descend to its image, it must vanish on this kernel; this is not automatic. In particular, the tetrahedron identity equates a sum of three forms with a sum of four forms, while the sums of their formal coefficients differ.

Here the passport is defined before taking such a quotient. Gluing rules and valid reductions of its coordinates require their own justification.

## The five polynomials of the path P5

The path has four edges, and every subset is acyclic. There are $2^4=16$ forests in total. In the state order listed above, we obtain

$$
\begin{aligned}
\mathcal F_{ace}(t)&=t^4\\
\mathcal F_{ac|e}(t)&=t^2(1+2t)\\
\mathcal F_{ae|c}(t)&=0\\
\mathcal F_{a|ce}(t)&=t^2(1+2t)\\
\mathcal F_{a|c|e}(t)&=(1+2t)^2
\end{aligned}
\tag{3}
$$

We derive these formulas directly from the edge choices.

**State $ace$.** All three boundary vertices must be connected. The only such forest contains all four edges, has weight $1$, and contributes $t^4$.

**State $ac|e$.** The edges $ab,bc$ are required. From the pair $cd,de$, we may select neither edge or exactly one; selecting both would connect $e$ to $c$. The contribution is therefore $t^2(1+t+t)$. In the first of these three forests, $d$ is an isolated internal component; in the other two, every component meets the boundary.

![[Three forests of one boundary state.svg]]

**One state, three forests.** The boundary partition is $ac|e$ in every panel. Purple marks the internal component $\{d\}$; dashed lines show edges of the original path that are not selected. Every panel contains all vertices. Reflecting the path gives the three forests of state $a|ce$; its two-edge forest has internal component $\{b\}$.

**State $ae|c$.** The unique path from $a$ to $e$ passes through $c$. It is impossible to connect $a,e$ while leaving $c$ in another component.

**State $a|c|e$.** On the segment $a-b-c$, select no edge or one of the two edges. The same three possibilities arise independently on $c-d-e$. Combining any two such choices keeps distinct boundary vertices disconnected. This gives $3\cdot3=9$ forests and the polynomial $(1+2t)^2$.

![[Nine forests with separated boundary.svg]]

**Two independent choices.** Rows specify the edge choice on $a-b-c$; columns specify the choice on $c-d-e$. The empty choice on the first segment leaves the internal component $\{b\}$, and on the second leaves $\{d\}$. The four panels with one selected edge on each segment have no internal components.

Summing by degree gives

$$
\begin{aligned}
\sum_\pi\mathcal F_\pi(t)
&=t^4+2t^2(1+2t)+(1+2t)^2\\
&=1+4t+6t^2+4t^3+t^4=(1+t)^4
\end{aligned}
$$

The equality $\mathcal F_{ac|e}=\mathcal F_{a|ce}$ comes from the symmetry of this marked path. It is not an identity between two coordinates for an arbitrary graph with a three-point boundary.

## Internal components and groves

**An established definition and a direct consequence.** The term “grove” is used in [Kenyon–Wilson, §1.1](https://arxiv.org/html/math/0608422v4#S1.SS1). Formulas (4)–(5) below follow by counting forest components.

**Lemma.** If a forest $H$ has $g$ edges and state $\pi$, its number of internal components is

$$
\boxed{k_0(H)=n-g-b(\pi)}
\tag{4}
$$

**Proof.** A spanning forest on $n$ vertices with $g$ edges has $n-g$ components. Those meeting the boundary are in bijection with the blocks of $\pi$, so there are exactly $b(\pi)$ of them. The remaining components are internal. $\square$

For fixed $n,\pi$, the degree of a monomial therefore already determines the number of internal components. Formula (1) needs no separate variable for that number. The passport does not retain their sizes or vertex sets.

The rank of the boundary partition is $r(\pi)=|B|-b(\pi)$. It differs from the number of edges in the original forest:

$$
g=r(\pi)+(n-|B|)-k_0(H)
$$

The exponent of $t$ in a state polynomial is $g$, not $r(\pi)$.

> [!info] A grove relative to a boundary
> **Definition.** A grove of $G$ relative to $B$ is a spanning forest in which every component contains at least one vertex of $B$.
>
> An isolated boundary vertex is allowed; an isolated internal vertex violates this condition.

This definition was introduced in [[en/Structural identities/Structural Identities and Graph Gluing#Groves and polyforms on shared vertices|the note on spanning-tree gluing]]. Kenyon–Wilson [1, §1.1] primarily consider groves on planar graphs with boundary vertices on the outer face. Here the component condition is applied to an arbitrary marked set; electrical formulas requiring planarity do not follow from the definition alone.

As in the note on spanning-tree gluing, let $g_\pi$ denote the sum of the weights of groves of state $\pi$. This is a scalar coefficient, not a polynomial or the edge count $g$.

**Corollary.** Groves are extracted from the full passport by

$$
\boxed{g_\pi=[t^{\,n-b(\pi)}]\mathcal F^{G,B}_\pi(t)}
\tag{5}
$$

Here $[t^j]$ denotes extraction of the coefficient of $t^j$.

**Proof.** A grove is characterized by $k_0(H)=0$. By (4), this is equivalent to $g=n-b(\pi)$. The coefficient of this degree in (1) sums exactly the weights of the required forests. $\square$

The degree $n-b(\pi)$ is the highest allowed degree for the state, but its coefficient may be zero. Lower degrees count forests with internal components.

For the path $P_5$, formula (5) gives:

| State $\pi$ | Polynomial $\mathcal F_\pi(t)$ | Grove degree $n-b(\pi)$ | Grove weight sum $g_\pi$ |
| --- | --- | ---: | ---: |
| $ace$ | $t^4$ | 4 | 1 |
| $ac\mid e$ | $t^2+2t^3$ | 3 | 2 |
| $ae\mid c$ | $0$ | 3 | 0 |
| $a\mid ce$ | $t^2+2t^3$ | 3 | 2 |
| $a\mid c\mid e$ | $1+4t+4t^2$ | 2 | 4 |

Of the $16$ forests, $1+2+0+2+4=9$ are groves; the remaining seven contain internal components. In particular, the constant term $1$ in state $a|c|e$ counts the edgeless forest with two internal components $\{b\},\{d\}$.

For a connected graph, the one-block state $\{B\}$ satisfies $g_{\{B\}}=\tau(G)$: a grove with one component is a spanning tree. The other coefficients $g_\pi$ count groves with several components. All these data enter the previously published spanning-tree pairing; the full passport also retains the lower degrees of each state.

## One forest polynomial, different gluing results

Formula (2) sums the passport coordinates. To show that the lost information matters, take two markings of the same unit-weight path using the boundary names $x,y,z$:

$$
X:\quad x-b-y-d-z,\qquad
X':\quad x-b-z-d-y
$$

Both parts have boundary $\{x,y,z\}$; the internal names $b,d$ belong to their respective copies of the path. Both parts have the same ordinary forest polynomial:

$$
F_X(t)=F_{X'}(t)=(1+t)^4
$$

Fix a partner $J$ on vertices $x,y,z$: its only edge $xy$ has conductance $1$, and $z$ is isolated. In each gluing, identify boundary vertices with the same name. The edge sets of the parts are disjoint, no internal vertices are identified, and the edge $xy$ is included exactly once.

![[One partner and two markings of a path.svg]]

**The same partner.** The blue edge $xy$ belongs to $J$; the green edges belong to the chosen copy of the path. For $X$, the result is a triangle with a two-edge tail; for $X'$, it is the cycle $C_5$. Both graphs have five vertices and five edges; the boundary and the matching of names are specified before gluing.

The first graph has a unique cycle of three edges. A cyclic subset must contain all three, while the remaining two edges can be selected freely. Hence

$$
\begin{aligned}
F_{X\#J}(t)&=(1+t)^5-t^3(1+t)^2\\
&=1+5t+10t^2+9t^3+3t^4
\end{aligned}
\tag{6}
$$

In the second graph, the unique cycle uses all five edges:

$$
\begin{aligned}
F_{X'\#J}(t)&=(1+t)^5-t^5\\
&=1+5t+10t^2+10t^3+5t^4
\end{aligned}
\tag{7}
$$

Thus equality of the forest polynomials of the parts does not ensure equality after gluing to the same fixed partner.

The missing information is visible in the passport. The sum of the state polynomials in which $x,y$ are connected is

$$
\begin{aligned}
X:&\quad \mathcal F_{xyz}+\mathcal F_{xy|z}
=t^4+t^2(1+2t)=t^2(1+t)^2\\
X':&\quad \mathcal F_{xyz}+\mathcal F_{xy|z}
=t^4+0=t^4
\end{aligned}
$$

These are precisely the forests to which the edge $xy$ cannot be added. Multiplying the forbidden sum by $t$ gives the terms subtracted in (6) and (7). This is a particular boundary test derived directly from the definition of a cycle. The two-point version of the same mechanism is described in [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#Two boundary states of an ordinary forest|the note on two forest states]].

## What the passport retains

The polynomials $\mathcal F_\pi(t)$ retain the distribution of ordinary forest weights by edge count and connectivity of the marked boundary. Given $n$ and $\pi$, the number of internal components is also known; formula (5) extracts the groves. Summing over $\pi$ returns $F_G(t)$ and can erase distinctions relevant to gluing.

The sufficiency of these data for gluing is proved in [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]: compatibility of two partitions selects the forest pairs, and a bilinear formula computes the full forest polynomial and the states of the result. The test for acyclicity after identifying boundary vertices is proved in [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]]: the passport response equals the forest polynomial of the quotient graph. The test acts on formal states; the passage to polyforms and its limitations are treated separately.

The ordinary forest passport must not automatically be regarded as spectral. [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] distinguishes ordinary coefficients $f_g$ from rooted coefficients $p_g$: the additional root factors depend on component sizes, which a state $\pi$ does not retain. The spectrum and a full representation of the operator are likewise distinguished in [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]]. A separate passport for the characteristic polynomial and an example separating these tasks are constructed in [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]].

## Status of the results and computational verification

Equality (2), the count of internal components (4), and grove extraction (5) have been proved for the stated class of graphs. Formulas (3), (6), and (7) were derived directly for the specific examples. The general forest gluing formula, coordinate reduction, and spectral continuation are not proved in this note.

An independent [exact verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_forest_states.py) enumerates all $16$ edge subsets of $P_5$, determines their components and boundary partitions, and checks every coefficient in (3), the grove count, and the internal components. It also enumerates all $32$ edge subsets of each graph in (6), (7). Additional weighted and disconnected examples check that isolated vertices are retained, parallel edges are distinguished, and groves are extracted from the polynomials. [Instructions for running the checks and reproducing the figures](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) accompany the script.

These finite checks supplement the proofs; they do not replace them.

## Sources and connections

1. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325–1364. [arXiv:math/0608422](https://arxiv.org/abs/math/0608422), [§1.1: groves and boundary partitions](https://arxiv.org/html/math/0608422v4#S1.SS1). Planarity and placement of the boundary on the outer face are hypotheses of the corresponding electrical results.
2. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [arXiv:2307.01046, §4](https://arxiv.org/html/2307.01046#S4). Formal boundary partition states and the forest compatibility matrix; Definitions 4.3–4.5 and the forest-state table in Definition 4.14. The rank results are applied in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]].

Supporting library results: [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients: Grade, Components, and Corank]], [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]], [[en/Structural identities/Partition Forms and the Tetrahedron Identity|Partition Forms and the Tetrahedron Identity]], [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/Граничные лесные состояния - что нужно сохранить от компоненты|Русский]]
