---
title: "Weaving Graphs: Plug, Socket, and Recurrence"
date: 2026-11-02
updated: 2026-11-11
revision: 3
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: graph-weaving-plug-socket-and-recurrence
order: 1
description: "Repeating a fixed runner core: plug, socket, two spanning states, and a general recurrence. Ladders, hexagonal chains, weighted runners and runners with cycles; variable outputs and closure."
---

Russian version: [[ru/Преобразования и сочленения графов/Цепи из ядер/Плетение графов - вилка, розетка и рекурсия|Плетение графов: вилка, розетка и рекурсия]].

A graph can be grown by repeatedly attaching a copy of the same piece. Two groups of vertices are marked on the piece in advance: the **plug**, which is identified with the current contacts of the assembled graph, and the **socket**, where the next attachment will take place. We call the repeated piece a **runner core**, or simply a **runner**, and the sequential assembly **graph weaving**.

The essential point is more than a repeated drawing. A small set of boundary data can be updated along with the graph. If the runner, its markings, and the attachment rule remain fixed, the same matrix acts at every step. This yields a recurrence for the spanning-tree coefficients of the entire sequence of graphs.

We begin with an ordinary ladder. We then define weaving and prove a two-coordinate transfer rule for an arbitrary connected runner with two input and two output contacts. Allowing the socket to vary connects this construction to [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]; passing to five spectral coordinates connects it to [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]].

> [!note] The result in plain language
> To keep counting spanning trees, we do not need to retain the whole graph already assembled. With two contacts, two numbers suffice: the total weight of its spanning trees and the total weight of its spanning forests with two components separating those contacts. The same piece updates these two numbers by the same rule. Consequently, the spanning-tree coefficient of the next graph is expressed through the preceding two coefficients.
>
> This statement concerns open weaving with precisely specified edge accounting. It does not say that two numbers suffice for the spectrum, graph reconstruction, or arbitrary closure of the ends.

> [!note] Origins of the construction and formulas
> The scheme continues the internal discussion of graph weaving in the PMG project. Dmitry Malyugin introduced the words “plug” and “socket” as intuitive names for the marked boundaries. They do not denote a new graph operation.
>
> Repeated constructions and linear recurrences belong to the classical transfer-matrix method; Noy–Ribó [1] give a general formulation. Two-contact laws for trees and separating forests appear in [Barrett et al., Theorems 7 and 9](https://arxiv.org/html/1901.00053v2#S2). Below, these laws are written as a single matrix and expressed through the resistance geometry of the runner. The weighted version, normalizations, examples, and transitions are justified explicitly; no scientific priority is claimed.

For a visual introduction, the first sections suffice: one edge, a square runner, and two spanning states. Then continue to [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|chain admissibility]] or follow the computational route in [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|the note on the exponential and toponomes]].

## Starting with a square ladder

See [[en/PythonExamples/Example - Boundary Data and Chains of Cores#Spanning trees of a square ladder|the notebook calculation]].

Let the initial graph $G_0$ consist of one unit edge $ab$. Its socket is the pair $(a,b)$. The runner $K$ is a path of three unit edges:

$$
p_0-q_0-q_1-p_1
$$

The plug consists of the path endpoints $(p_0,p_1)$; the socket is the middle pair $(q_0,q_1)$. Identify $p_0$ with $a$, and $p_1$ with $b$. The old edge and the new three-edge path form a square. Now attach the same kind of path to $(q_0,q_1)$ and repeat.

![The plug and socket of a path, the first square, and three repetitions of one runner](images/Plug%20and%20Socket%20in%20Graph%20Weaving.svg)

**Exactly what is added.** The plug consists of two vertices with no edge between them in the runner. The existing socket edge remains in the assembled graph. Each step adds two vertices and three edges. After $k$ steps, we obtain a ladder of $k$ squares with $2k+2$ vertices and $3k+1$ edges.

Its spanning-tree counts begin as follows:

$$
1,\ 4,\ 15,\ 56,\ 209,\ 780
$$

The first number refers to the initial edge. Below, we derive the recurrence $\tau_{k+2}=4\tau_{k+1}-\tau_k$ and explain which runner data determine the coefficients $4$ and $1$.

## The runner and a fixed attachment rule

We consider finite undirected graphs with positive conductances. Parallel edges are allowed and counted separately; the original pieces have no loops. The spanning-tree coefficient $\tau(G)$ is the sum, over spanning trees, of the products of their edge conductances. For unit conductances it is the usual spanning-tree count.

> [!info] Weaving data
> **Definition.** A marked runner consists of a connected graph $K$, two ordered lists of distinct vertices
>
> $$
> \mathcal P=(p_0,\ldots,p_{r-1}),\qquad
> \mathcal Q=(q_0,\ldots,q_{r-1})
> $$
>
> and a fixed correspondence of contacts. The list $\mathcal P$ is the plug, and $\mathcal Q$ is the socket. The initial connected graph $G_0$ has a marked socket $\mathcal B_0$ of size $r$.
>
> To construct $G_{k+1}$, take a fresh copy of $K$. Identify its plug with the current socket $\mathcal B_k$ using the specified correspondence; make no other identifications. The image of $\mathcal Q$ becomes the new socket $\mathcal B_{k+1}$.

Ordering the contacts lets us write the correspondence as $p_i\mapsto b_i$. If a permutation is required, it is fixed once and included in the rule. Choosing a new correspondence at each step instead defines variable weaving. The plug and socket mark vertices; they are neither extra edges nor algebraic boundaries $\partial X$.

In the basic model, every edge of the new copy is added. Edges with the same endpoints remain parallel: their conductances add in the Laplacian. If the common edge of two cycles must be counted once, its duplicate is removed from the runner in advance. Thus a square core gives the runner $P_4$, and a hexagonal core gives $P_6$. The conditions for this assignment are discussed in [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains#Accounting for shared edges when gluing|Cores, Seams, and Admissible Chains]].

> [!info] The number of steps and the graph size
> **Proposition.** If the runner has $v_K$ vertices and $e_K$ edges, then after $k$ attachments
>
> $$
> n_k=n_0+k(v_K-r),\qquad
> |E(G_k)|=|E(G_0)|+ke_K
> \tag{1}
> $$

> [!note]- Proof of the count
> **Proof.** Exactly $r$ distinct vertices of the new copy are identified with existing vertices. The other $v_K-r$ vertices are new. The edge sets of the pieces are disjoint, and no edge is removed. Summing these increments gives (1). $\square$

Here $k$ counts attached runners, while $n_k$ counts vertices. In examples starting from an edge, each runner completes one new cycle, so the number of cyclic cores $N$ equals $k$. No such identification is assumed for an arbitrary runner.

If $\mathcal P\cap\mathcal Q=\varnothing$, every output contact is created at the current step. If these sets overlap, some old contacts may persist for many steps: for example, a path $P_3$ with its plug at the endpoints and its socket on the first edge generates a fan of triangles. This weaving is allowed, but it violates the prohibition of nonadjacent contacts in the narrower model of [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains#Admissible open chains of cycles|Cores, Seams, and Admissible Chains]].

## Two numbers for two contacts

From now on, $r=2$. The plug $\mathcal P=(p_0,p_1)$ and socket $\mathcal Q=(q_0,q_1)$ may overlap; within each pair the vertices are distinct.

> [!info] The spanning boundary state
> **Definition.** Let $\sigma_G(x,y)$ denote the total weight of spanning forests with exactly two components in which $x$ and $y$ belong to different components. No roots are chosen. For $\mathcal B_k=(x_k,y_k)$, set
>
> $$
> \tau_k=\tau(G_k),\qquad
> \sigma_k=\sigma_{G_k}(x_k,y_k),\qquad
> s_k=\begin{pmatrix}\tau_k\\\sigma_k\end{pmatrix}
> \tag{2}
> $$

These are two states of the spanning-tree layer: the contacts are either joined by a tree or separated by a two-component forest. They differ from the full forest passport, which also accounts for other component counts, and from the five-coordinate spectral passport.

The forest-minor theorem and the resistance identity give

$$
\sigma_G(x,y)=\det\mathbf L_{\widehat{x,y},\widehat{x,y}}
=\tau(G)R_{xy}
\tag{3}
$$

Vertex degrees of the original graph are retained in the principal minor. For a graph with two vertices, the empty determinant equals $1$. This is a special case of [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]; see also [Barrett et al., §1, Theorem 3](https://arxiv.org/html/1901.00053v2#S1).

![A tree and a separating two-component forest as the two states of the current socket](images/Two%20Spanning%20States%20of%20Graph%20Weaving.svg)

**Two weights, rather than two individual forests.** For the square in the figure, $\tau=4$, $\sigma=3$: each coordinate sums all admissible choices. The next runner transforms this vector into $(15,11)^{\mathsf T}$, and one more transforms it into $(56,41)^{\mathsf T}$.

## Transfer from the runner's forest data

Form the graph $K/\mathcal P$ by identifying the two input vertices. Delete the resulting loops and retain parallel edges. Continue to denote the images of the output vertices by $q_0,q_1$. If they coincide, set $\sigma_{K/\mathcal P}(q_0,q_1)=0$.

> [!info] Closed transfer of two coordinates
> **Theorem 1.** For open weaving with two contacts and disjoint edge sets of the pieces,
>
> $$
> \boxed{s_{k+1}=\mathbf T_Ks_k},\qquad
> \mathbf T_K=
> \begin{pmatrix}
> \sigma_K(p_0,p_1)&\tau(K)\\
> \sigma_{K/\mathcal P}(q_0,q_1)&\sigma_K(q_0,q_1)
> \end{pmatrix}
> \tag{4}
> $$
>
> All four entries are nonnegative. For integer conductances they are integers. The same matrix applies at every step, regardless of the size of the graph assembled so far.

This is a matrix form of the two-vertex gluing laws in [Barrett et al., Theorems 7 and 9](https://arxiv.org/html/1901.00053v2#S2). The proof by partitioning forests remains valid for positive weights.

> [!note]- Proof of Theorem 1
> **Proof.** The restriction of a spanning tree of the result to the old part has one of two forms: a tree, or a two-component forest separating the input contacts. In the first case the new part must separate the contacts; in the second it must join them. Multiplying weights gives the first row of (4).
>
> For a forest separating the output contacts, the old part likewise cannot have a component without an input contact: both components of the result must meet the output, which lies in $K$. If the old part separates the inputs, the new part must be a two-component forest separating the outputs. Its contribution is $\sigma_k\sigma_K(q_0,q_1)$.
>
> If the old part is a tree, its path between the inputs can be contracted. The admissible restrictions to the new part are then in a weight-preserving bijection with separating forests of $K/\mathcal P$. The contribution is $\tau_k\sigma_{K/\mathcal P}(q_0,q_1)$. This gives the second row. $\square$

Reversing the order of the input contacts does not change this spanning matrix: the two states do not distinguish endpoint labels. This is a special property of this reduction. The graph itself and its spectral passport may change; the fixed correspondence remains part of the definition of weaving.

## Resistance data and the general recurrence

Set $\kappa=\tau(K)$. In the resistance metric of the runner itself, take the vectors $p=p_1-p_0$, $q=q_1-q_0$ and the three numbers

$$
\alpha=p^2=R_{p_0p_1},\qquad
\beta=q^2=R_{q_0q_1},\qquad
\gamma=p\cdot q
\tag{5}
$$

The norm here is quadratic, as in [[en/Getting Started and Foundations/Foundations/PMG terminology|PMG Terminology]]. In coordinates, $\gamma=\mathbf p^{\mathsf T}\mathbf{Gr}_K\mathbf q$, where $\mathbf{Gr}_K=\mathbf L_K^+$; this is an inner product, not the product of two resistances. It can be found from pairwise resistances alone:

$$
\gamma=\frac{R_{p_0q_1}+R_{p_1q_0}-R_{p_0q_0}-R_{p_1q_1}}2
$$

> [!info] The matrix in terms of runner geometry
> **Lemma.** Matrix (4) has the form
>
> $$
> \boxed{
> \mathbf T_K=\kappa
> \begin{pmatrix}
> \alpha&1\\
> \alpha\beta-\gamma^2&\beta
> \end{pmatrix}}
> \tag{6}
> $$
>
> In particular,
>
> $$
> \operatorname{tr}\mathbf T_K=\kappa(\alpha+\beta),\qquad
> \det\mathbf T_K=\kappa^2\gamma^2
> \tag{7}
> $$

> [!note]- Proof of the resistance expression
> **Proof.** By (3), the diagonal entries are $\kappa\alpha$ and $\kappa\beta$. Let $K_c$ be the graph obtained by adding a test edge of conductance $c$ between the inputs of $K$. The matrix determinant lemma and the rank-one inverse update formula give
>
> $$
> \tau(K_c)=\kappa(1+c\alpha),\qquad
> R_q(K_c)=\beta-\frac{c\gamma^2}{1+c\alpha}
> $$
>
> The Laplacian form changes according to $L_{K_c}=L_K+c[p]^2$; the corresponding laws are derived in [[en/Getting Started and Foundations/Introduction/Variation of a Single Edge|Variation of a Single Edge]]. Multiply the equalities using (3):
>
> $$
> \sigma_{K_c}(q_0,q_1)
> =\kappa\beta+c\kappa(\alpha\beta-\gamma^2)
> $$
>
> The coefficient of $c$ counts forests containing the new edge. Contracting it gives separating forests of $K/\mathcal P$, so the lower-left entry is $\kappa(\alpha\beta-\gamma^2)$. If the output vertices merge, this coefficient is zero. Computing the trace and determinant gives (7). $\square$

The number $\alpha\beta-\gamma^2$ is the determinant of the resistance Gram matrix of the pair $p,q$. This connects the transfer rule to [[en/Getting Started and Foundations/Introduction/From Lengths to Areas and Volumes|From Lengths to Areas and Volumes]]. Nonnegativity also follows from the Cauchy–Schwarz inequality. The formal form $[p]^2$, the vector $p$, and the numerical norm $\alpha$ have different roles.

> [!info] The spanning-tree recurrence of a fixed runner
> **Theorem 2.** For an unchanged marked runner and all $k\ge0$,
>
> $$
> \boxed{
> \tau_{k+2}=\kappa(\alpha+\beta)\tau_{k+1}
> -\kappa^2\gamma^2\tau_k}
> \tag{8}
> $$
>
> The initial values are determined by the starting graph:
>
> $$
> \tau_0=\tau(G_0),\qquad
> \tau_1=\kappa(\alpha\tau_0+\sigma_0)
> \tag{9}
> $$
>
> The same recurrence holds for $\sigma_k$. Its order is at most two; the minimal order may be lower.

> [!note]- Proof of the recurrence
> **Proof.** The Cayley–Hamilton identity for a matrix of size $2$ is
>
> $$
> \mathbf T_K^2-(\operatorname{tr}\mathbf T_K)\mathbf T_K
> +(\det\mathbf T_K)\mathbf I_2=0
> $$
>
> Apply it to $s_k$ and substitute (7). This gives a vector recurrence and hence each coordinate recurrence. Formula (9) is the first row of (6). $\square$

In particular, when $\gamma=0$, the subtracted term vanishes: starting at $\tau_1$, the sequence is geometric with ratio $\kappa(\alpha+\beta)$. A necessarily second-order recurrence cannot be asserted.

### Normalization of the earlier weaving formula

The internal materials used coefficients $p^2+q^2$ and $(p\cdot q)^2$. For a unit path, $\kappa=1$, so that expression agrees exactly with (8). For an arbitrary runner, the factors $\kappa$ are necessary.

Without them, the recurrence holds for the normalized sequence $\widehat\tau_k=\tau_k/\kappa^k$:

$$
\widehat\tau_{k+2}=(\alpha+\beta)\widehat\tau_{k+1}
-\gamma^2\widehat\tau_k
\tag{10}
$$

Even if the runner is a tree, its spanning-tree coefficient may differ from $1$ when conductances are not all one. Being a tree and having the normalization $\kappa=1$ are therefore different conditions.

## Paths, ladders, and hexagons

Let the runner be a unit path $P_m$ on $m\ge3$ vertices $v_0,\ldots,v_{m-1}$. Its plug consists of the endpoints, and its socket of adjacent vertices $(v_j,v_{j+1})$, $0\le j\le m-2$. Orient both vectors along the path. Then

$$
\kappa=1,\qquad \alpha=m-1,\qquad \beta=1,\qquad \gamma=1
$$

> [!note]- Proof of the path data
> **Proof.** A tree has one spanning tree. Resistance along a unit path equals its number of edges, giving $\alpha$ and $\beta$. A unit current between the endpoints passes through every edge; the potential drop across the chosen edge is $1$. By reciprocity, this is the value $p\cdot q=1$ with consistent orientations. $\square$

Hence, independently of the position of the chosen edge,

$$
\mathbf T_m=\begin{pmatrix}m-1&1\\m-2&1\end{pmatrix},\qquad
\tau_{k+2}=m\tau_{k+1}-\tau_k
\tag{11}
$$

For a unit initial edge, $s_0=(1,1)^{\mathsf T}$, so $\tau_1=m$. For an initial unit path of $\ell$ edges with its socket at the endpoints, $s_0=(1,\ell)^{\mathsf T}$ and $\tau_1=m-1+\ell$: the initial data change, while the runner matrix stays the same.

![A path for squares, a path for hexagons, and a runner with cycles and eight spanning trees](images/Three%20Runners%20and%20Their%20Recurrences.svg)

**Count vertices and edges separately.** A square is formed by attaching $P_4$: three edges and four vertices. A hexagon is formed by attaching $P_6$: five edges and six vertices, two of which are identified with old vertices. Each new hexagon therefore adds four vertices. Attaching the endpoints of a five-vertex path to an edge would form a pentagon.

| Runner and socket | Recurrence | $\tau_0,\tau_1,\tau_2,\tau_3,\tau_4$ |
| --- | --- | --- |
| $P_4$, middle edge | $\tau_{k+2}=4\tau_{k+1}-\tau_k$ | $1,4,15,56,209$ |
| $P_6$, middle edge | $\tau_{k+2}=6\tau_{k+1}-\tau_k$ | $1,6,35,204,1189$ |
| $P_3$, first edge; fan | $\tau_{k+2}=3\tau_{k+1}-\tau_k$ | $1,3,8,21,55$ |

For disjoint input and output seams, this is the same special case derived from a dual determinant in [[en/Graph Transformations and Gluing/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#Recurrence in the number of cores|Spanning-Tree Polynomials of Chains: Determinant and Recurrence]]. The runner explains the repetition of the computational step; the dual graph explains invariance under changes in seam position. Formula (11) applies to the fan even though the assumptions of the narrower model of admissible cycle chains are violated.

## Runners with weights and internal cycles

### A weighted path

Give the path $p_0-q_0-q_1-p_1$ conductances $2,3,5$ in that order. Its plug and socket are the same as for the square ladder. Then

$$
\kappa=30,\qquad
\alpha=\frac{31}{30},\qquad \beta=\gamma=\frac13,\qquad
\mathbf T_K=\begin{pmatrix}31&30\\7&10\end{pmatrix}
$$

With a unit initial edge, we obtain

$$
\tau_{k+2}=41\tau_{k+1}-100\tau_k,\qquad
\tau_0=1,\quad\tau_1=61,\quad\tau_2=2401,\quad\tau_3=92341
$$

Here $\tau_k$ are spanning-tree coefficients: conductances enter as weights. Removing the factors $\kappa$ would give a different sequence.

### A runner with two independent cycles

Take $K=K_4\setminus\{01\}$, with plug $(0,1)$ and socket $(2,3)$. Its edges $02,03,12,13,23$ are unit edges. Here

$$
\kappa=8,\qquad \alpha=1,\qquad\beta=\frac12,\qquad\gamma=0,\qquad
\mathbf T_K=\begin{pmatrix}8&8\\4&4\end{pmatrix}
$$

The initial edge restores the missing edge $01$, so the first graph is $K_4$ and has $16$ spanning trees. Subsequently,

$$
\tau_{k+2}=12\tau_{k+1},\qquad
\tau_0=1,\quad\tau_1=16,\quad\tau_2=192,\quad\tau_3=2304
$$

A zero value of $\gamma$ means that there is no potential difference between the output vertices under a current through the input pair. It does not mean that the graph is disconnected.

### Adding the input edge a second time

If we use the whole square $C(0,1,2,3)$ instead of $P_4$, with plug $(0,1)$ and socket $(3,2)$, the disjoint-edge rule adds a second edge between the input contacts. The matrix is then

$$
\mathbf T_K=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
\tau_0=1,\quad\tau_1=7,\quad\tau_2=41
$$

This is a different network. To obtain an ordinary ladder with unit rungs, remove the input edge from the repeated piece in advance. Switching between these two rules is not a change of notation.

## A variable socket and periodic weaving

If step $k$ uses a runner or marking $K_k$, then

$$
s_N=\mathbf T_{K_{N-1}}\cdots\mathbf T_{K_0}s_0
\tag{12}
$$

A finite state dimension alone no longer implies constant coefficients in a scalar recurrence. However, a period of $r$ steps can be combined into a composite runner. The period matrix is $\mathbf M=\mathbf T_{K_{r-1}}\cdots\mathbf T_{K_0}$; the sequence $s_{jr}$ follows transfer by $\mathbf M$ and a two-step recurrence given by the trace and determinant of $\mathbf M$.

For example, alternating the paths for a square and a hexagon gives

$$
\mathbf M=\mathbf T_6\mathbf T_4=
\begin{pmatrix}17&6\\14&5\end{pmatrix},\qquad
\tau_{2j+4}=22\tau_{2j+2}-\tau_{2j}
$$

For an initial edge, $\tau_0=1$, $\tau_2=23$, $\tau_4=505$. Here one period index corresponds to two added cycles.

For the unit path $P_6$, each of the three internal sockets disjoint from the plug gives the same spanning matrix $\mathbf T_6$. This is precisely why the corresponding turns are invisible in $\tau_k$ and $\sigma_k$. Spectral data distinguish these choices: they use the different matrices $\mathbf U_S,\mathbf U_L,\mathbf U_R$ from [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains#Letter codes and spectral matrices|SLR Codes of Hexagonal Chains]].

With a fixed runner and fixed output pair, the five spectral coordinates also transfer by one matrix $\mathbf U(\xi)$. By the Cayley–Hamilton identity, their sequences satisfy a recurrence in the number of steps of order at most five, with coefficients depending on $\xi$. This follows from the proved closure result in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]]; it does not assert the minimal order of a particular recurrence.

A fixed output specifies a constant local continuation rule. For hexagonal markings, one may consider the turn words $SSS\ldots$, $LLL\ldots$, and $RRR\ldots$. The last two families are mirror images. Here “constant curvature” is only an informal description of a **constant combinatorial turn**: no geometric curvature is assigned to an abstract graph. Crossings in a regular layout do not automatically create new connections.

## Closure requires retaining the start

In open weaving, the starting graph supplies the initial conditions. Closure additionally requires choosing an initial boundary, the final socket, and a correspondence between them. It is a separate operation on the assembled chain.

![Open repetition of a runner and two contact correspondences at closure](images/Starting%20and%20Closing%20a%20Weaving.svg)

**Two different final steps.** In a square strip, the top contact may be identified with the top contact and the bottom with the bottom, or they may be exchanged. These choices give ordinary and twisted closures. If the end edges must become one unit edge, one duplicate copy is removed before identification.

The vector $(\tau_k,\sigma_k)$ stores data only at the current socket and has already forgotten its joint connectivity with the start. Thus substituting “the last socket equals the first” into the open recurrence does not yield a formula for a ring. A general boundary calculation must retain joint data for the initial and current boundaries; two disjoint pairs mean four marked vertices. An exact example, edge accounting, and the different closures are discussed in [[en/Graph Transformations and Gluing/Chains of cores/Closing a Chain - Rings and the Möbius Effect#Edge accounting and retaining the initial boundary|Closing a Chain: Rings and the Möbius Effect]].

A closed graph can instead be defined directly as a cyclic gluing of runner copies, with no distinguished starting piece. In that case all correspondences must be specified from the outset and the resulting identifications checked. The open two-coordinate recurrence alone does not solve this problem.

## Exact checks and limits of the result

All numerical data were obtained in integer or rational arithmetic. The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_weaving.py) and [saved data](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/weaving-results.json) contain the runners, contacts, correspondences, and edge sets of the constructed graphs.

- For seven runners, states from step zero through step five were checked: 42 pairs of direct Laplacian minors were compared with transfer and recurrence. The cases include unit paths, overlapping boundaries of a fan, a whole square, $K_4$ without its input edge, and integer and rational conductances.
- For 21 small graphs, all 5254 edge subsets were independently enumerated. Trees and separating two-component forests were summed separately without using the recurrence being checked.
- For all 38 connected simple graphs on four labeled vertices, 36 combinations of input and output pairs and two contact correspondences were checked: 2736 attachments to a weighted initial triangle. The cases include coincident and overlapping pairs, zero mixed inner product, and parallel edges after gluing.
- For all 27 sequences of three internal outputs of the path $P_6$, direct minors gave $(\tau_3,\sigma_3)=(204,169)$. Periodic alternation of square and hexagonal steps was checked separately through four full periods.

The general statements in this note have the proofs given above; finite checks test the examples and implementation. No new numerical or general results on spectra of closed chains are claimed here. A boundary with more than two vertices requires a richer state; the general second-order recurrence of this note does not extend to it. For a disconnected runner, the resistance parameters (5) are not defined in the stated form, so one must return to the full forest data.

The full exponential, transfer of forest component sizes, and the connection to five rooted coordinates are discussed in [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]]. The exact correspondence between the three path sockets and the letters S, L, R, constant turns, and spectral recurrences is given in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]].

## Sources and connections

1. M. Noy, A. Ribó. *Recursively constructible families of graphs*. Advances in Applied Mathematics **32** (2004), 350-363. [DOI: 10.1016/S0196-8858(03)00088-5](https://doi.org/10.1016/S0196-8858(03)00088-5); [author's publication list](https://sites.google.com/view/marcnoy/publications). General theory of repeated graph constructions and recurrences; the specific matrix (4) is derived here from two-contact forest laws.
2. W. Barrett, E. J. Evans, A. E. Francis, M. Kempton, J. Sinkovic. *Spanning 2-Forests and Resistance Distance in 2-Connected Graphs*. [§§1-2, Theorems 3, 7, and 9](https://arxiv.org/html/1901.00053v2). Separating forests, resistances, and decomposition under two-vertex gluing.
3. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1](https://arxiv.org/html/1907.08450v1#S3). The spanning-tree recurrence for polygon chains with one shared edge.

Definitions and edge accounting: [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. Full boundary data: [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]] and [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]. Rank-one update: [[en/Getting Started and Foundations/Introduction/Variation of a Single Edge|Variation of a Single Edge]]. An alternative derivation of spanning-tree recurrences: [[en/Graph Transformations and Gluing/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains: Determinant and Recurrence]]. Closures: [[en/Graph Transformations and Gluing/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain: Rings and the Möbius Effect]]. Spectral continuation: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], and [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]].

Thematic entries: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].
