---
title: "Vertex Contraction as a Boundary Test"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: vertex-contraction-as-boundary-test
order: 2
description: "Acyclicity under boundary identification, the forest polynomial of a quotient graph, formal contraction tests, polyform maps, and resistance determinant normalization."
---

The boundary forest passport should let us operate on a component without returning to its internal edges. We begin with contraction: several selected vertices are treated as one, and forests that become cyclic subgraphs are excluded. We determine how this selection depends only on the boundary partition and how it gives the forest polynomial of the new graph.

The input consists of the state polynomials from [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]]. Algebraic vertex identification and its resistance geometry were introduced in [[en/Spaces/Vertex Contraction and Graph Gluing|Vertex Contraction and Graph Gluing]]. Here we distinguish two related constructions: mapping a polyform into a quotient space and testing it in the original space. Their connection on the spanning-tree layer yields a formula involving a resistance Gram matrix.

> [!info] Provenance of the results
> **From the literature.** Forest compatibility is defined in [Mannens–Nederlof, §4.2](https://arxiv.org/html/2307.01046#S4.SS2); the relation between contractions and spanning groves is described in [Kenyon–Wilson, §2.2](https://arxiv.org/html/math/0608422v4#S2.SS2).
>
> **Derivations and interpretation here.** The criterion is expressed through partition ranks and proved by counting components. The polynomial formula follows from a bijection of forests. The distinction between the polyform map and the test, and the metric formulation, use previously introduced PMG constructions.
> “Derived here” identifies where a proof is given; no claim of scientific priority is made.

## What contracting a partition means

Let $G=(V,E)$ be a finite undirected graph on $n$ vertices with positive conductances, and let $B\subseteq V$ be a nonempty marked boundary. Edges are distinguishable; parallel edges are allowed. Existing loops may be removed beforehand because they belong to no forest. Connectivity is needed only in the section on the resistance determinant.

**Definition.** Let

$$
\sigma=B_1|\cdots|B_s\in\Pi(B)
$$

Contraction by $\sigma$ identifies all vertices of each block $B_i$ with a single vertex $h_i$. Distinct blocks remain distinct; internal vertices $V\setminus B$ are retained. Denote the resulting graph by $G/\sigma$.

Write the number of blocks as $b(\sigma)$ and the rank as

$$
r(\sigma)=|B|-b(\sigma)
$$

The number of vertices after contraction is

$$
n'=n-r(\sigma)
$$

Each original edge is transferred between the images of its endpoints with the same label and conductance. If the endpoints coincide, it becomes a loop and cannot be selected in a forest. Edges with identical new endpoints remain distinguishable parallel edges. The rule for combining their weights will be justified separately.

Contraction does not require an edge between the identified vertices. It is an operation on vertices, not the selection of an obligatory forest edge. The discrete partition into singleton blocks changes nothing.

## When the image of a forest remains a forest

**Connection with an established construction.** The following criterion expresses forest compatibility [1, Definitions 4.3–4.5] through partition ranks. We give a direct proof for vertex identification.

For a spanning forest $H$, write $\pi=\pi_B(H)$ for its induced boundary partition. Its blocks describe connectivity between boundary vertices; internal forest components do not enter $\pi$.

**Definition.** The join $\pi\vee\sigma$ is the partition in which two vertices are equivalent if they can be connected by a sequence of steps within blocks of $\pi$ or $\sigma$. It is the least common coarsening of the two partitions.

**Theorem (selection criterion).** The image of a forest $H$ after contraction by $\sigma$ is acyclic if and only if

$$
\boxed{r(\pi\vee\sigma)=r(\pi)+r(\sigma)}
\tag{1}
$$

The image retains every selected edge label, including any loops or parallel edges produced; a cycle is precisely what excludes the selection.

**Proof.** Suppose $H$ has $g$ edges and $c=n-g$ components, of which $k_0=c-b(\pi)$ are internal. Contraction leaves internal components unchanged. Components meeting the boundary merge according to $\pi\vee\sigma$. The image therefore has

$$
c'=k_0+b(\pi\vee\sigma)=c-b(\pi)+b(\pi\vee\sigma)
$$

components, $n'=n-r(\sigma)$ vertices, and $g$ distinguishable edges. For any undirected multigraph, $g-n'+c'$ is the number of independent cycles; it is zero exactly for a forest. This includes loops as one-edge cycles and parallel pairs as two-edge cycles. Substitution gives

$$
\begin{aligned}
g-n'+c'
&=r(\sigma)-b(\pi)+b(\pi\vee\sigma)\\
&=r(\pi)+r(\sigma)-r(\pi\vee\sigma)
\end{aligned}
$$

Thus acyclicity is equivalent to (1). $\square$

Selection depends only on the boundary state, not on the shapes of the internal trees or the number of internal components. Their contributions remain in the state polynomials.

### Checking individual blocks is insufficient

For one contracted pair $a,b$, the criterion says that $a,b$ must lie in different forest components. If a path already connects them, identification closes it into a cycle.

For several blocks, the condition “within each block, all vertices lie in different forest components” is necessary but insufficient. Take

$$
\pi=ac|bd,\qquad \sigma=ab|cd
$$

Let $H$ consist of the edges $ac,bd$. Within each block of $\sigma$, the vertices belong to different components of $H$. Yet contraction produces two parallel edges between $h_1=\{a,b\}$ and $h_2=\{c,d\}$, hence a cycle. Indeed,

$$
r(\pi)=r(\sigma)=2,\qquad r(\pi\vee\sigma)=r(abcd)=3
$$

![[A cycle between two contracted blocks.svg]]

**A cycle between blocks.** The green edges $ac,bd$ form the original forest. Gold dashed lines mark the auxiliary pairs $ab,cd$ specifying the identifications; these are not edges of the original graph. After contraction, the two selected edges have the same endpoints. Criterion (1) detects the dependence of the entire system of identifications.

## A linear test of the full passport

Introduce the numerical compatibility function

$$
C(\pi,\sigma)=
\begin{cases}
1,&r(\pi\vee\sigma)=r(\pi)+r(\sigma)\\
0,&\text{otherwise}
\end{cases}
$$

On the free boundary-state space $\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R s_\pi$, define the linear functional

$$
\mathcal T_\sigma(s_\pi)=C(\pi,\sigma)
$$

**Definition.** The response of a component to the contraction test $\sigma$ is the polynomial

$$
U_{G,B}(\sigma;t)
=\mathcal T_\sigma\bigl(\mathbf f_{G,B}(t)\bigr)
=\sum_{\pi\in\Pi(B)}C(\pi,\sigma)\mathcal F^{G,B}_\pi(t)
$$

**Theorem (polynomial consequence of the selection criterion).** With the edge-transfer rules specified above,

$$
\boxed{F_{G/\sigma}(t)=U_{G,B}(\sigma;t)}
\tag{2}
$$

**Proof.** Every forest of the quotient graph specifies a unique subset of original edge labels. Splitting identified vertices cannot create cycles, so this subset is a forest of $G$ satisfying (1). Conversely, every forest passing test (1) gives a forest of the quotient graph. The correspondence is bijective and preserves labels, edge count, and the product of conductances. Summing weights gives (2). $\square$

The degree of $t$ remains the number of selected original edges. The number of vertices has decreased, but every forest passing the test retains its edge count. Thus (2) has **no additional factor $t^{-r(\sigma)}$**.

For discrete $\sigma$, all states pass the test and $U_{G,B}(\sigma;t)=F_G(t)$. If the entire boundary is contracted to one vertex, only the discrete forest state passes:

$$
F_{G/B}(t)=\mathcal F^{G,B}_{b_1|\cdots|b_k}(t),\qquad B=\{b_1,\ldots,b_k\}
$$

State polynomials and responses are different coordinates: $\mathcal F_\pi$ counts forests with an exact partition, whereas $U(\sigma;t)$ sums all states compatible with the test. We do not assume that the transformation between these data is invertible.

### Where the factor in the corank convention comes from

Now suppose $G$ is connected, $d=n-1$, and $r=r(\sigma)$. Then $G/\sigma$ is connected and has dimension $d-r$. To compare with the corank convention, set

$$
\widehat F_G(u)=u^dF_G(u^{-1})=\tau(G)\Phi_G(u),\qquad
\widehat U_{G,B}(\sigma;u)=u^dU_{G,B}(\sigma;u^{-1})
$$

Equation (2) implies

$$
\widehat F_{G/\sigma}(u)=u^{-r}\widehat U_{G,B}(\sigma;u)
$$

The factor comes from the different top degrees $d$ and $d-r$ when the variable is inverted. The response $\widehat U$ itself is divisible by $u^r$, since forests passing the test have at most $d-r$ edges. This identity agrees with [[en/Matroid parameters and forest characteristics of graphs/The Normalized Forest Polynomial and Power-Sum Parameters|the normalized forest polynomial]] and does not alter (2) in the edge-count variable.

## Example: three contractions of P5

Retain the path $a-b-c-d-e$ with unit conductances and boundary $B=\{a,c,e\}$. Its five state polynomials were computed in [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#The five polynomials of the path P5|the main example of the full passport]].

**Identifying $a,c$.** For $\sigma=ac|e$, the passing states are $a|c|e$, $a|ce$, and $ae|c$. The last has zero polynomial on this path. Hence

$$
\begin{aligned}
F_{G/(ac)}(t)
&=\mathcal F_{a|c|e}(t)+\mathcal F_{a|ce}(t)+\mathcal F_{ae|c}(t)\\
&=(1+2t)^2+t^2(1+2t)=(1+2t)(1+t)^2
\end{aligned}
$$

After contraction, two parallel unit edges join $h=\{a,c\}$ to $b$, and the path $h-d-e$ remains. Select neither parallel edge or one of the two, and select the remaining edges independently. This gives the same polynomial directly from the quotient graph.

**Identifying $a,e$.** For $\sigma=ae|c$, the passing states are $a|c|e$, $ac|e$, and $a|ce$. The quotient graph is the cycle $C_4$, so

$$
\begin{aligned}
F_{G/(ae)}(t)
&=(1+2t)^2+2t^2(1+2t)\\
&=1+4t+6t^2+4t^3=(1+t)^4-t^4
\end{aligned}
$$

**Identifying the entire boundary.** For $\sigma=ace$, only $a|c|e$ passes, giving

$$
F_{G/(ace)}(t)=(1+2t)^2
$$

The quotient graph has three vertices $h,b,d$ and two parallel pairs, one between $h,b$ and one between $h,d$. The choices in these pairs are independent.

![[Three contractions of the boundary of P5.svg]]

**Three results for one component.** Each pair of parallel unit edges is replaced in the drawing by one connection of conductance $2$. The formulas below the graphs follow both from the passport test and from direct forest enumeration. Their leading coefficients are $2,4,4$, and their degrees are $3,3,2$.

Although no forest of this path realizes the state $ae|c$, the partition $ae|c$ can still specify a contraction. A state partition and a test partition have different roles.

## Loops, parallel edges, and their weights

A loop belongs to no forest and contributes no factor $1+c_\ell t$. Among parallel edges with conductances $c_1,\ldots,c_m$, a forest can select at most one. For any fixed selection of the other edges, all these alternatives have the same endpoints and the same admissibility. Their total weight is $c_1+\cdots+c_m$.

Thus, when computing the forest polynomial, distinguishable parallel edges may be replaced by one edge whose conductance is their sum. This sums the weights of alternatives; it is not a bijection between individual forests after merging the edges.

Take a triangle with conductances

$$
c_{ab}=2,\qquad c_{ac}=3,\qquad c_{bc}=5
$$

Identifying $a,b$ turns $ab$ into a loop and $ac,bc$ into parallel edges between $h=\{a,b\}$ and $c$. Therefore,

$$
F_{G/(ab)}(t)=1+(3+5)t=1+8t
$$

The product $(1+3t)(1+5t)$ is incorrect here: its term $15t^2$ selects both parallel edges and creates a cycle. The conductance of the former edge $ab$ does not enter the result.

![[A loop and parallel edges after contraction.svg]]

**Transferring labels and summing weights.** The middle panel retains all three original labels: the loop of conductance $2$ is excluded from forests, and at most one edge of the parallel pair $3,5$ is selected. The right panel shows the connection of conductance $8$ that is equivalent for forest counting.

## Mapping a polyform and testing in the original space

**PMG interpretation.** We now compare the established combinatorial selection with the exterior-algebra map and multiplication of forms. These operations are developed in [[en/Spaces/Vertex Contraction and Graph Gluing|Vertex Contraction and Graph Gluing]] and [[en/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges|The Cycle Matroid and Exterior Products of Edges]].

### The polyform of the quotient graph

In the linear space of basis vertices introduced in [[en/Foundations/Core specification#The underlying space, points, and vectors|the core specification]], define $\varphi_\sigma$ to map each vertex of $B_i$ to $h_i$ and retain the internal vertices. This map is linear, preserves affine weight, and extends to exterior objects and forms:

$$
\varphi_\sigma(XY)=\varphi_\sigma(X)\varphi_\sigma(Y),\qquad
\varphi_\sigma([X,Y])=[\varphi_\sigma(X),\varphi_\sigma(Y)]
$$

Its kernel on the affine-vector space consists of differences within blocks and has dimension $r(\sigma)$. The new space is therefore the quotient by these directions.

As with contraction of a pair, we obtain

$$
\boxed{L_{G/\sigma}=\varphi_\sigma(L_G),\qquad
\exp(tL_{G/\sigma})=\varphi_\sigma\bigl(\exp(tL_G)\bigr)}
\tag{3}
$$

A loop gives a zero endpoint difference. Parallel connections map to identical forms and add by conductance. Formula (3) describes the polyform of the new graph itself.

### Auxiliary differences

Choose a tree on the vertices of each block $B_i$. Its edges are **auxiliary identification connections** and need not belong to $G$. Denote the union of these trees by $K_\sigma$. It has exactly $r=r(\sigma)$ edges. Orienting them gives independent differences $d_1,\ldots,d_r$.

The partition form is

$$
q_\sigma=\prod_i[(B_i)]^2=[d_1\cdots d_r]^2
$$

This equality uses ordinary endpoint differences with coefficients $+1,-1$. For a tree on one block, the product of differences equals the boundary of that block up to sign; the sign disappears in the quadratic form. Changing the trees, order, or orientations leaves $q_\sigma$ unchanged.

**Lemma (forest-form test).** Let $X_H$ be the exterior product of the edge vectors of a forest $H$. Then

$$
[X_H]^2q_\sigma\ne0
\quad\Longleftrightarrow\quad
H\text{ passes test }\sigma
\tag{4}
$$

**Proof.** The left-hand side is nonzero exactly when the edges of $H$, together with the auxiliary edges of $K_\sigma$, form a forest: a cycle is equivalent to linear dependence of the edge vectors. Auxiliary edge labels are distinct from original labels even when endpoints coincide.

After adding $K_\sigma$, the number of components is $k_0+b(\pi\vee\sigma)$, the number of edges is $g+r$, and the number of vertices is still $n$. The number of independent cycles is

$$
(g+r)-n+k_0+b(\pi\vee\sigma)
=r(\pi)+r(\sigma)-r(\pi\vee\sigma)
$$

It vanishes under the same condition (1). $\square$

Thus $\varphi_\sigma([X_H]^2)$ and $[X_H]^2q_\sigma$ vanish for exactly the same original forests. However, these forms lie in different spaces and have different grades: a surviving image has grade $g$, while the nonzero product in the original space has grade $g+r$.

In the labeled forest expansion of $\exp(tL_G)$, multiplication by $q_\sigma$ can test each term. Its coefficient still has degree $t^g$: auxiliary connections are not edges of the forest being counted. After selection, weights are summed using the original labels. This gives $U_{G,B}(\sigma;t)$.

Multiplication of polyforms is linear, but the subsequent instruction “sum the coefficients of the surviving forests” acts on the labeled expansion. It does not thereby become a linear functional on the polyform space modulo structural identities. The linear test $\mathcal T_\sigma$ is defined on the free states $s_\pi$; replacing them with forms $q_\pi$ requires a separate check that the operation descends to the quotient.

### Redundant identification conditions

If identifications are specified as a list of pairs, first find its connected blocks and choose a tree within each block. For example, the three conditions $a\sim b$, $b\sim c$, $c\sim a$ have rank two. The product of all three pair forms is zero:

$$
[(ab)]^2[(bc)]^2[(ca)]^2=0
$$

This reflects dependence of the chosen auxiliary connections, not impossibility of contraction. A correct test uses any two pairs forming a tree on $\{a,b,c\}$, for example

$$
q_{abc}=[(ab)(ac)]^2=[(abc)]^2
$$

## The spanning-tree coefficient and the resistance determinant

First extract the leading coefficient of (2). Set $r=r(\sigma)$ and $n'=n-r$. For $V=\{v_1,\ldots,v_n\}$, the original spanning form is $T_V=[(v_1\cdots v_n)]^2$. The functional $\tau_V$ extracts the coefficient of $T_V$ in the space of the original $n$ vertices. Write a forest weight as $w(H)=\prod_{e\in E(H)}c_e$.

**Theorem.** With the stated normalization of $q_\sigma$,

$$
\boxed{
\tau(G/\sigma)
=[t^{n'-1}]U_{G,B}(\sigma;t)
=\tau_V(M_Gq_\sigma),\qquad M_G=\exp L_G
}
\tag{5}
$$

**Proof.** The top grade of the product involves forests $H$ with $n-1-r=n'-1$ edges. For each forest passing the test, $H\cup K_\sigma$ is acyclic and has $n-1$ edges on $n$ vertices, hence is a tree. Its form is $T_V$ with coefficient $1$, and the original edges have weight $w(H)$. The coefficient of $T_V$ therefore sums exactly the weights of the spanning trees of the quotient graph. $\square$

Unlike summing arbitrary forest coefficients, extracting the coefficient of $T_V$ is a well-defined linear functional on polyforms themselves. The spanning-tree result (5) may therefore be evaluated after structural transformations.

Now assume the original graph $G$ is connected. Denote the resistance Gram matrix of the chosen differences by

$$
\mathbf G_d=(d_i\cdot d_j)_{i,j=1}^r
$$

The inner product is evaluated in the resistance metric of the **original** graph. By [[en/Foundations/Core specification#Potential and the metric identity|the metric identity]] and [[en/Introduction/Metric of Higher-Grade Objects|the determinant rule for higher grades]],

$$
\frac{\tau_V(M_G[d_1\cdots d_r]^2)}{\tau(G)}
=(d_1\cdots d_r)^2=\det\mathbf G_d
$$

**Consequence of library results.** Together with (5), the PMG metric identity gives the following determinant formula. We specify its normalization and its relation to the test:

$$
\boxed{\tau(G/\sigma)=\tau(G)\det\mathbf G_d}
\tag{6}
$$

For $r=0$, the empty determinant is $1$. If all vertices are contracted to one, the quotient has a unique empty spanning tree of weight $1$; the formulas still hold.

If $\mathbf D$ is the matrix whose columns are the coordinates of $d_i$, then

$$
\mathbf G_d=\mathbf D^{\mathsf T}\mathbf{Gr}_G\mathbf D,
\qquad \mathbf{Gr}_G=\mathbf L_G^+
$$

Here $\mathbf G_d$ is the Gram matrix of the chosen differences, whereas $\mathbf{Gr}_G$ is the Green matrix of the entire original graph. For $d_i=v-u$, $d_j=y-x$, the Gram entries are expressed through pairwise resistances:

$$
d_i\cdot d_j=\frac{R_{uy}+R_{vx}-R_{ux}-R_{vy}}2
$$

For one pair, $\mathbf G_d=(R_{ab})$, and (6) reduces to the previously published formula $\tau(G/(ab))=\tau(G)R_{ab}$.

### Basis normalization matters

Formula (6) without correction uses edge differences of the trees $K_\sigma$, for example $b_j-b_0$ in each block. For an arbitrary other basis of the same directions,

$$
e_j=\sum_i d_i A_{ij},\qquad \det\mathbf A\ne0
$$

we have

$$
\mathbf G_e=\mathbf A^{\mathsf T}\mathbf G_d\mathbf A,
\qquad
[e_1\cdots e_r]^2=(\det\mathbf A)^2q_\sigma
$$

The correct formula in that basis is therefore

$$
\boxed{\tau(G/\sigma)=\tau(G)\frac{\det\mathbf G_e}{(\det\mathbf A)^2}}
\tag{7}
$$

Changing from one tree to another within the same blocks gives $\det\mathbf A=\pm1$. Arbitrary rescaling or orthonormalization need not do so. Knowing only the subspace of disappearing directions does not fix the scale of their exterior product.

The Gram determinant here is the squared volume of a parallelotope. If one uses the geometric volume of the $r$-dimensional simplex on the same differences instead, its square must be multiplied by $(r!)^2$. The spanning-tree coefficient is computed from a reduced Kirchhoff determinant; the product of the nonzero Laplacian eigenvalues is $n\tau(G)$ and has a different normalization.

### Checks on the path and a weighted triangle

For $P_5$ and the contraction $ace$, choose

$$
d_1=c-a,\qquad d_2=e-a
$$

Resistances on the unit path equal edge-count distances: $R_{ac}=2$, $R_{ae}=4$, $R_{ce}=2$. Hence

$$
\mathbf G_d=
\begin{pmatrix}2&2\\2&4\end{pmatrix},\qquad
\det\mathbf G_d=4
$$

Since $\tau(P_5)=1$, we obtain $\tau(G/(ace))=4$, as from $(1+2t)^2$. For the basis $e_1=2d_1$, $e_2=d_2$, the Gram matrix is

$$
\mathbf G_e=
\begin{pmatrix}8&4\\4&4\end{pmatrix},\qquad
\det\mathbf G_e=16
$$

Dividing by $(\det\mathbf A)^2=4$ restores the result $4$.

The triangle with conductances $2,3,5$ has spanning-tree coefficient $31$ and $R_{ab}=8/31$. Contracting $ab$ gives $31\cdot8/31=8$, agreeing with the coefficient of $t$ in $1+8t$.

Connectivity of the original graph is essential in (6)–(7). For example, two disjoint unit edges $ab,cd$ become a tree with spanning-tree coefficient $1$ after identifying $a,c$, although the original $\tau(G)=0$. The combinatorial test (2) and equality (5) remain valid, but division by $\tau(G)$ and a single resistance metric for the original graph are inapplicable.

## What the boundary test provides

Contraction by a specified partition is evaluated by a linear functional of the full forest passport. Formula (1) selects the states; formula (2) retains their ordinary edge-count degrees. Map (3) constructs the quotient graph's polyform, while multiplication by $q_\sigma$ tests compatibility in the original space.

On the spanning-tree layer, the test admits a well-defined metric evaluation: $\tau(G)$ and the resistance Gram matrix of the normalized contraction differences suffice. The whole polynomial requires the full response $U_{G,B}(\sigma;t)$; its lower coefficients do not follow from a single resistance determinant. Connections with the Dirichlet-to-Neumann operator, spanning-tree gluing, and reconstruction limits are discussed in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]].

The function $C(\pi,\sigma)$ is symmetric in its two partitions. In [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]], the other side is supplied by another graph's state polynomials. That note proves the bilinear law, distinguishes state coordinates from test responses, and specifies the space on which the pairing matrix may be inverted.

## Status of the results and checks

Criterion (1), forest response formula (2), form test (4), and spanning-tree extraction (5) have been proved for finite undirected graphs with edge labels retained. Resistance formulas (6)–(7) additionally require connectivity of the original graph and the stated basis normalization. None of these statements uses planarity.

An independent [exact verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_contraction.py) compares three selection methods: the partition criterion, direct cycle detection in the quotient graph, and edge independence after adding the auxiliary forest. It also compares the state-polynomial responses with direct enumeration of quotient forests, and reduced Laplacian determinants with resistance Gram determinants. Checks cover the examples in this note, all subgraphs of weighted $K_4$, different boundaries, loops, parallel edges, disconnected graphs, redundant pairs, and basis changes. All arithmetic is exact and rational; [the instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) include figure reproduction.

Computational checks supplement the general proofs; they do not replace them.

## Sources and connections

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [arXiv:2307.01046, §4.2, Definitions 4.3–4.5](https://arxiv.org/html/2307.01046#S4.SS2). The forest compatibility matrix is defined by the absence of a cycle in the union of partition representatives. Criterion (1) expresses this compatibility through ranks and is proved here directly for contraction.
2. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325–1364. [arXiv:math/0608422, §2.2, equation (6) and Lemma 2.1; §2.3](https://arxiv.org/html/math/0608422v4#S2.SS2). Contracting a boundary partition relates groves to spanning trees of the quotient graph. The lemma is stated for a circular planar graph and noncrossing partitions; at the start of §2.3, the authors extend it to arbitrary graphs by summing over all partitions.

Supporting PMG notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Spaces/Vertex Contraction and Graph Gluing|Vertex Contraction and Graph Gluing]], [[en/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges|The Cycle Matroid and Exterior Products of Edges]], [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]], [[en/Introduction/Metric of Higher-Grade Objects|Metric of Higher-Grade Objects]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/Стягивание вершин как граничный тест|Русский]]
