---
title: Structural Identities and Graph Gluing
date: 2026-10-18
updated: 2026-10-18
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: structural-identities-and-graph-gluing
lang: en
description: "The spanning-tree coefficient of a glued graph through grove polyforms on shared vertices, a proof of the formula, coordinate reduction by structural identities, and examples with two and four shared vertices."
order: 4
---

When two graphs are glued along several vertices, we need to account for how forests within each piece connect those vertices. Different forests may induce the same partition of the shared set, and forms of different partitions may be linearly dependent. Structural identities reduce the number of coordinates while preserving the data needed to compute the spanning-tree coefficient after gluing.

We use [[Partition Forms and the Tetrahedron Identity|partition forms]], the [[Basis and Dimension of the Space of Partition Forms#The top coefficient and the partition pairing|pairing through the top coefficient]], and the [[Basis and Dimension of the Space of Partition Forms#Noncrossing partitions and the basis|noncrossing partition basis]]. Gluing along one or two vertices has already been considered in the [[Vertex Contraction and Graph Gluing|series on spaces]]. Here the main objects are polyforms on the shared vertex set.

Throughout this note, graphs are finite, undirected, and loopless. The weight of an existing edge $e$ is its conductance $c_e>0$. The weight of a forest is the product of its edge weights; the empty product is $1$. The main formula is proved as a polynomial identity in the edge weights and requires no choice of resistance metric.

## Gluing and a prescribed decomposition

Let two connected graphs $G_1,G_2$ have selected sets of $k\geqslant1$ vertices, with a specified bijection between them. After identifying corresponding vertices, denote their shared set by $S=\{s_1,\ldots,s_k\}$. There are no other shared vertices, and each edge retains its membership in one of the pieces:

$$
G=G_1\cup G_2,\qquad
V(G_1)\cap V(G_2)=S,\qquad
E(G)=E(G_1)\sqcup E(G_2)
$$

Edges with the same endpoints coming from different pieces are treated as distinct parallel edges in the proof. In the Laplacian, their conductances add according to the core conventions. The graph $G$ is connected because both pieces are connected and $S$ is nonempty.

The construction can also be read in reverse. If $G$ is already represented by two such pieces, replace each vertex $s\in S$ by copies $s^{(1)},s^{(2)}$. Endpoints of edges in $E(G_i)$ are assigned to the copy $s^{(i)}$. This produces two separate graphs, and identifying the copies recovers $G$.

Specifying $S$ alone is insufficient for this operation: both pieces and the assignment of every edge must be given. In particular, edges with both endpoints in $S$ must be assigned to pieces. In this note, the decomposition is prescribed and both pieces are connected. Choosing a decomposition and establishing when one exists are separate questions. Reversibility of this construction does not by itself establish an algebraic duality.

After substituting the shared vertex names, the full polyforms satisfy the familiar rule

$$
L_G=L_1+L_2,\qquad
M_G=\exp(L_1+L_2)=M_1M_2
$$

This exponential and product belong to the polyform algebra. The full polyforms also contain the interior vertices of the pieces. We now construct objects on $S$ alone that suffice to compute the spanning-tree coefficient.

## Groves and polyforms on shared vertices

> [!info] A grove relative to a selected set
> **Definition.** A grove of $G_i$ relative to $S$ is a spanning forest each of whose components contains at least one vertex of $S$.

The forest includes every vertex of $G_i$, including vertices isolated in the forest itself. An isolated vertex in $S$ is allowed; an isolated interior vertex violates the definition of a grove.

Kenyon and Wilson [1] consider groves in a planar graph with selected vertices on the outer face. Here the same condition on components is used for an arbitrary selected set $S$; planarity is not assumed.

A grove $F_i$ induces a partition $\pi(F_i)$ of $S$: two selected vertices lie in the same block if and only if they belong to the same forest component. Since every component meets $S$, the number of grove components equals the number of blocks $b(\pi)$.

For each partition $\pi$, set

$$
g_\pi^{(i)}
=\sum_{\substack{F_i\text{ is a grove in }G_i\\\pi(F_i)=\pi}}
\prod_{e\in F_i}c_e
$$

If there are no such groves, the coefficient is zero. This is an unnormalized weight sum; there is no division by the spanning-tree coefficient.

Recall that a partition $\pi=B_1|\cdots|B_{b(\pi)}$ of $S$ corresponds to the form

$$
q_\pi=[(B_1)\cdots(B_{b(\pi)})]^2,\qquad
\operatorname{gr}q_\pi=k-b(\pi)
$$

Singleton blocks contribute unit factors. The partition blocks describe only the vertices of $S$; the grove components themselves may also contain interior vertices.

> [!info] The grove polyform on shared vertices
> **Definition.** Define the grove polyform of the piece $G_i$ relative to $S$ by
>
> $$
> \boxed{
> P_i=\sum_{\pi\in\Pi(S)}g_\pi^{(i)}q_\pi
> }
> \tag{1}
> $$
>
> Here $\Pi(S)$ is the set of all partitions of $S$.

The polyform $P_i$ belongs to the space $\mathcal P_k$ from the previous note. It describes connections between the selected vertices through groves of the piece. The full metric polyform $M_i$ is defined on all vertices of $G_i$ and includes all its spanning forests. In general, these are different objects.

The grade of $q_\pi$ is $k-b(\pi)$, whereas the grove itself in a piece with $n_i$ vertices has $n_i-b(\pi)$ edges. These numbers agree only when there are no interior vertices.

## The spanning-tree coefficient after gluing

On the set $S$, fix the spanning-tree form and the functional that extracts its coefficient:

$$
T_S=[(s_1\ldots s_k)]^2,\qquad
P_{k-1}=\tau_S(P)T_S
$$

For $k=1$, we have $T_S=e$ and $\tau_S(e)=1$. The subscript $S$ specifies the vertex set on which the coefficient is extracted. The spanning-tree coefficient $\tau(G)$ of the entire graph refers to its full vertex set.

The [[Basis and Dimension of the Space of Partition Forms#The top coefficient and the partition pairing|pairing lemma]] gives

$$
\tau_S(q_\pi q_\rho)=
\begin{cases}
1,&b(\pi)+b(\rho)=k+1\text{ and }\pi\vee\rho=\{S\}\\
0,&\text{otherwise}
\end{cases}
$$

The partition $\pi\vee\rho$ groups together vertices connected by a chain of memberships in common blocks of $\pi$ or $\rho$. The condition $\pi\vee\rho=\{S\}$ means that all vertices of $S$ are connected in this way.

> [!info] The gluing formula
> **Theorem.** Under the stated assumptions on the graphs and their shared vertices,
>
> $$
> \boxed{\tau(G)=\tau_S(P_1P_2)}
> \tag{2}
> $$
>
> Equivalently,
>
> $$
> \tau(G)=
> \sum_{\substack{\pi,\rho\in\Pi(S)\\
> b(\pi)+b(\rho)=k+1\\
> \pi\vee\rho=\{S\}}}
> g_\pi^{(1)}g_\rho^{(2)}
> $$

> [!note]- Proof by splitting a spanning tree
> **Proof.** Let $T$ be a spanning tree of $G$. Restrict its edges to the two pieces:
>
> $$
> E(F_1)=E(T)\cap E(G_1),\qquad
> E(F_2)=E(T)\cap E(G_2)
> $$
>
> Each $F_i$ is considered on the full vertex set of $G_i$ and is therefore a spanning forest. If one of its components did not meet $S$, it could not connect to the other piece or to the rest of the tree $T$. Thus both $F_i$ are groves.
>
> Conversely, take two groves $F_1,F_2$ with partitions $\pi,\rho$. Their union contains every vertex of $G$. Every component of the union contains a vertex of $S$, so the union is connected if and only if $\pi\vee\rho=\{S\}$.
>
> Write $n_i=|V(G_i)|$ and $n=|V(G)|=n_1+n_2-k$. The groves have $n_1-b(\pi)$ and $n_2-b(\rho)$ edges, respectively. The edge sets of the pieces are disjoint, so
>
> $$
> |E(F_1\cup F_2)|
> =n_1+n_2-b(\pi)-b(\rho)
> =n+k-b(\pi)-b(\rho)
> $$
>
> A connected graph on $n$ vertices is a tree if and only if it has $n-1$ edges. Hence the union of the groves is a tree exactly when the two conditions in the theorem's sum hold. This remains valid with distinguishable parallel edges.
>
> Splitting and taking the union are inverse operations, and the weights multiply:
>
> $$
> w(F_1\cup F_2)=w(F_1)w(F_2)
> $$
>
> Summing over compatible pairs of groves gives $\tau(G)$. On the other hand, expanding $P_1P_2$ and applying the pairing lemma gives the same sum. This proves (2). $\square$

The condition on the number of blocks is equivalent to complementary grades:

$$
\operatorname{gr}q_\pi+\operatorname{gr}q_\rho=k-1
$$

There are no factorial factors in (2): each pair of individual groves is counted exactly once, and the coefficient of a compatible product of forms is $1$. The number of trees that can represent a block in the proof of the algebraic lemma is not an additional weight here.

With one shared vertex, every grove is a tree. Thus $P_i=\tau(G_i)e$, and (2) gives the familiar formula $\tau(G)=\tau(G_1)\tau(G_2)$.

For a prescribed decomposition of a graph, the same theorem computes its spanning-tree coefficient from the two pieces. The proof already includes both directions of the construction.

## Passing to the noncrossing partition basis

Fix a cyclic order of the vertices of $S$. By the [[Basis and Dimension of the Space of Partition Forms#Noncrossing partitions and the basis|basis theorem]], every partition form has a unique expansion

$$
q_\pi=\sum_{\sigma\in\mathrm{NC}_k}c_{\sigma\pi}q_\sigma
$$

This expansion preserves grade. Substitution into (1) gives

$$
P_i=\sum_{\sigma\in\mathrm{NC}_k}p_\sigma^{(i)}q_\sigma,
\qquad
p_\sigma^{(i)}=\sum_{\pi\in\Pi(S)}
c_{\sigma\pi}g_\pi^{(i)}
$$

The coefficients $g_\pi^{(i)}$ are weight sums of groves of a specified type. The coefficients $p_\sigma^{(i)}$ are coordinates of the same polyform in the chosen basis and may be negative. Structural identities relate the forms $q_\pi$; the original coefficients $g_\pi^{(i)}$ need not satisfy the same relations.

Let $\mathbf p_i$ be the column of new coordinates, and let $\mathbf K_k$ be the pairing matrix of noncrossing partitions from the previous note, in the same order:

$$
(\mathbf K_k)_{\sigma\rho}=\tau_S(q_\sigma q_\rho)
$$

Then (2) and bilinearity imply

$$
\boxed{\tau(G)=\mathbf p_1^{\mathsf T}\mathbf K_k\mathbf p_2}
\tag{3}
$$

The matrix depends on the shared set and the chosen basis. The internal structure of each piece enters through its coordinates. The dimension of the space of these polyforms is the Catalan number $C_k$; in grade $r$, the number of coordinates is the Narayana number $N(k,k-r)$.

Thus, for this algebraic representation, $C_k$ coordinates suffice in place of the $B_k$ coefficients indexed by all partitions. This reduction preserves the result of gluing with any partner represented by a polyform on the same $S$. It is not asserted to give the minimum number of arbitrary, possibly nonlinear, parameters of a particular graph.

For a different vertex identification, the vertices of one piece must first be relabeled according to the chosen bijection. Having the same number $k$ of vertices is not sufficient to apply (3).

## Two shared vertices

Let $S=\{a,b\}$. The first piece is the path $a-x-b$ with edge weights $\alpha,\beta$, and the second is the path $a-y-b$ with weights $\gamma,\delta$. The vertices $x,y$ are interior and distinct. Gluing produces the cycle $a-x-b-y-a$.

In the first piece, the grove of type $ab$ contains both edges and has weight $\alpha\beta$. Groves of type $a|b$ contain exactly one edge, with weights $\alpha$ and $\beta$. The empty forest is not a grove because its isolated vertex $x$ does not belong to $S$.

Write $q_{ab}=[(ab)]^2$. We obtain

$$
P_1=(\alpha+\beta)e+\alpha\beta q_{ab},
\qquad
P_2=(\gamma+\delta)e+\gamma\delta q_{ab}
$$

Here $T_S=q_{ab}$ and $q_{ab}q_{ab}=0$. Formula (2) gives

$$
\tau(G)=
(\alpha+\beta)\gamma\delta+
\alpha\beta(\gamma+\delta)
$$

Expanding yields the sum

$$
\alpha\gamma\delta+\beta\gamma\delta+
\alpha\beta\gamma+\alpha\beta\delta
$$

Each term corresponds to deleting one edge of the cycle. This is also a direct, independent count of its spanning trees. With unit weights, $\tau(G)=4$.

In this example, $B_2=C_2=2$, so there is no reduction in the number of coordinates yet. It illustrates the passage from forests with interior vertices to polyforms on $S$.

## Four shared vertices and the tetrahedron identity

Take two paths with unit edge weights:

$$
G_1:\ a-c-b-d,\qquad
G_2:\ b-a-d-c
$$

Their edge sets are disjoint, and all four vertices are shared: $S=\{a,b,c,d\}$. Their union contains all six vertex pairs and equals $K_4$.

![[Gluing Two Paths into K4.svg]]

*Figure 1. Two paths and their union after identifying vertices with the same names. Solid blue edges belong to $G_1$; dashed orange edges belong to $G_2$. The vertices are arranged in the cyclic order $a,b,c,d$. The crossing of diagonals in the figure is not a vertex.*

Since there are no interior vertices, every spanning forest of either piece is a grove, and $P_i=M_i$. In the notation $q_{ab}$ and $q_{abc}$, the remaining vertices of $S$ are understood to be singleton blocks. Set $T=T_S$.

Each path has three edges, and every subset of its edges is a forest. Hence

$$
\begin{aligned}
P_1&=e+(q_{ac}+q_{bc}+q_{bd})+
(q_{abc}+q_{bcd}+q_{ac|bd})+T\\
P_2&=e+(q_{ab}+q_{ad}+q_{cd})+
(q_{abd}+q_{acd}+q_{ab|cd})+T
\end{aligned}
$$

The parentheses group grades $1$ and $2$. In the order $a,b,c,d$, the only crossing partition is $ac|bd$. Apply the tetrahedron identity:

$$
\begin{aligned}
q_{ac|bd}
&=q_{a|bcd}+q_{b|acd}+q_{c|abd}+q_{d|abc}-\\
&\qquad-q_{ab|cd}-q_{ad|bc}
\end{aligned}
$$

It transforms the grade-$2$ coordinates as follows. Singleton blocks are written explicitly in the table.

| Form | $P_1$ before transformation | $P_1$ after transformation | $P_2$ |
|---|---:|---:|---:|
| $q_{a\mid bcd}$ | 1 | 2 | 0 |
| $q_{b\mid acd}$ | 0 | 1 | 1 |
| $q_{c\mid abd}$ | 0 | 1 | 1 |
| $q_{d\mid abc}$ | 1 | 2 | 0 |
| $q_{ab\mid cd}$ | 0 | -1 | 1 |
| $q_{ad\mid bc}$ | 0 | -1 | 0 |
| $q_{ac\mid bd}$ | 1 | 0 | 0 |

The first six forms constitute a basis of grade $2$. The coefficient of the seventh form has been eliminated by adjusting the others. The polyform $P_2$ is already expressed in this basis. Each path has three two-edge forests, but the transformed grade-$2$ coefficients of $P_1$ sum to $4$: these are coordinates of a form, not a new forest count.

Denote the grade-$r$ component by $P_{i,r}$. Only the grade pairs $(0,3),(1,2),(2,1),(3,0)$ contribute to the top coefficient of the product. The pairing criterion gives

$$
\begin{aligned}
\tau_S(P_{1,0}P_{2,3})&=1\\
\tau_S(P_{1,1}P_{2,2})&=2+3+2=7\\
\tau_S(P_{1,2}P_{2,1})&=2+2+3=7\\
\tau_S(P_{1,3}P_{2,0})&=1
\end{aligned}
$$

In the second line, the summands correspond to the pairs $ac,bc,bd$ from $P_1$: they join distinct blocks in two, three, and two partitions from $P_{2,2}$, respectively. In the third line, the summands correspond to the original forms $q_{abc},q_{bcd},q_{ac|bd}$.

After replacing $P_{1,2}$ according to the table, the third line becomes

$$
2\cdot2+1\cdot1+1\cdot1+2\cdot2-1\cdot1-1\cdot2=7
$$

Thus, both before and after the structural transformation,

$$
\tau(K_4)=1+7+7+1=16
$$

**Independent check.** There are $\binom63=20$ three-edge subsets in $K_4$. Four are triangles with an isolated fourth vertex; the remaining sixteen are spanning trees. Direct enumeration also gives $16$.

On four shared vertices, the full family contains $B_4=15$ partition forms, while the chosen basis contains $C_4=14$. The change occurs in grade $2$: seven forms are replaced by six. In this example, the table shows the reduction explicitly; preservation of the gluing result follows from the identity of forms, not merely from numerical agreement.

## What a structural transformation preserves

Formula (2) uses the top coefficient of a product. Equality of polyforms on $S$ therefore preserves the result of any subsequent spanning-tree pairing. This is an algebraic fact; no metric norms of forms are evaluated in the proof.

The full unrooted forest polynomial, which counts all spanning forests by their number of components, requires a separate construction. First, forests in the pieces may have components that do not meet $S$; such forests are absent from the grove polyforms. Second, ordinary summation of forest weights cannot be defined by a linear functional $q_\pi\mapsto1$ on the space of partition forms.

The latter point is already visible in the tetrahedron identity:

$$
q_{ab|cd}+q_{ac|bd}+q_{ad|bc}
=q_{a|bcd}+q_{b|acd}+q_{c|abd}+q_{d|abc}
$$

The coefficient sums of the two expressions are $3$ and $4$. A linear functional taking the value $1$ on every partition form would have to give the same number on equal polyforms, which is impossible.

Consequently, the reduction proved for the spanning-tree pairing cannot automatically be used for ordinary counting of all forests. The original weight sums, their transformed coordinates, and metric evaluations are different data.

## Status of the results and continuation

- **Proved directly:** the gluing formula (2), including the reverse computation from a prescribed decomposition. The proof establishes a weight-preserving bijection between spanning trees and compatible pairs of groves.
- **Follows from the previous note:** passage to the noncrossing basis, formula (3), and sufficiency of $C_k$ coordinates. The general basis result relies on the external combinatorial theorems cited in the third note.
- **Computed directly and checked independently:** the weighted cycle on four vertices and gluing two paths into $K_4$, including the coordinate transformation by the tetrahedron identity.
- **Requires separate study:** choosing a graph decomposition, comparing decompositions along vertices and edges, a possible connection with the dual polyform, and the full forest pairing.

[[Supports of Structural Identities]] continues the algebraic part of the series: it describes relations by their supports and counts new independent directions relative to transfer by adjoining singleton blocks.

## Sources

1. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325-1364. [arXiv:math/0608422v4](https://arxiv.org/abs/math/0608422v4), [DOI: 10.1090/S0002-9947-2010-04964-5](https://doi.org/10.1090/S0002-9947-2010-04964-5). Source for the notion of a grove and the description of its connectivity by a partition of selected vertices; the paper's planar assumptions are not used in the proof of (2).

This note is based on the author's research within PMG.

Algebraic definitions and normalizations: [[Core specification#Forms and polyform algebra]] and [[Core specification#The spanning-tree form and coefficient extraction]]. Full proof of the basis used here: [[Basis and Dimension of the Space of Partition Forms]].
