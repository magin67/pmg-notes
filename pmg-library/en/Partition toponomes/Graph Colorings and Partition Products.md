---
title: Graph Colorings and Partition Products
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: graph-colorings-and-partition-products
lang: en
description: "A graph model of the second-kind algebra: color classes, vertex-weighted complete graphs, disjoint union, and chromatic symmetric functions."
order: 4
---

In [[The Second-Kind Algebra on Partitions|the second-kind algebra]], multiplication enumerates partial matchings between the parts of two partitions. Graph colorings provide a model for this operation: parts are represented by weighted vertices, and shared colors match parts from different factors. This connects the algebra introduced for working with toponomes to the classical coloring problem and to chromatic symmetric functions.

The main correspondence is as follows: disjoint union of graphs becomes multiplication of the sums of their color-class types. We first define these sums, then examine examples and establish the connection with the [[The Second-Kind Algebra on Partitions#Realization by ordinary multiplication of symmetric functions|symmetric-function basis]].

## Proper colorings and color classes

Let $H=(V,E)$ be a finite simple undirected graph. Its vertices are distinguishable, and their number is $N=\#V$. For now, we impose no bound on the set of available colors.

> [!info] Proper colorings and color classes
> **Definition.** A proper coloring assigns a color to each vertex so that the endpoints of every edge have different colors. Vertices of the same color form a **color class**. There are no edges within such a class; a vertex set with this property is called **independent**, or stable.

Forget the names of the colors while retaining the membership of each class. This gives a partition

$$
\pi=B_1\mid\cdots\mid B_r
$$

into nonempty independent blocks. The order of the blocks is disregarded. Conversely, each such partition determines a proper coloring up to renaming the colors used: assign distinct colors to its blocks.

For example, two nonadjacent vertices $a,b$ admit two color-class partitions:

$$
a\mid b,\qquad ab
$$

The first assigns different colors, and the second a shared color. If an edge joins $a$ and $b$, only $a\mid b$ remains.

Below, the coefficients count **color-class partitions**. Assigning blue rather than green to a class does not create a new partition. Changing the membership of a class does create a different partition, even if the class sizes remain unchanged.

## Vertex weights and color-class types

Assign positive integer weights to the vertices:

$$
\omega:V\longrightarrow\mathbb Z_{>0}
$$

Whether a coloring is proper depends on the edges and is independent of these weights. The weight of a block and the total weight of the graph are

$$
\omega(B)=\sum_{v\in B}\omega(v),
\qquad
k=\omega(V)
$$

> [!info] Vertex weights and color-class types
> **Definition.** The weight type of a color-class partition is the integer partition
>
> $$
> \lambda_\omega(\pi)=\bigl(\omega(B_1),\ldots,\omega(B_r)\bigr)
> $$

Its weight is $k$, and its number of parts is the number $r$ of color classes. With unit vertex weights, the parts equal the class sizes. For arbitrary weights, these quantities can differ: two vertices of weights $2$ and $1$ in the same class give a part $3$.

Let $\Pi_{\mathrm{ind}}(H)$ denote the set of all partitions of $V$ into nonempty independent blocks. Define the formal sum of types

$$
\boxed{
\mathcal C(H,\omega)=\sum_{\pi\in\Pi_{\mathrm{ind}}(H)}\lambda_\omega(\pi)
}
$$

This is an element of the partition algebra. The coefficient of a type is the number of color-class partitions with that collection of weights. The graph with no vertices has one empty partition, so its sum is the unit $1$.

## A complete graph represents one type

Let $\lambda=(a_1,\ldots,a_r)$. Construct a complete graph on $r$ vertices $v_1,\ldots,v_r$, assigning weight $a_i$ to $v_i$. Denote this weighted graph by $K_\lambda$.

Any two vertices are adjacent, so every color class is a singleton. There is a unique color-class partition, and its collection of weights is $\lambda$:

$$
\boxed{\mathcal C(K_\lambda)=\lambda}
$$

The weights are included in the notation $K_\lambda$. For example, $K_{(2,1)}$ consists of two adjacent vertices of weights $2$ and $1$. They have different colors and give the type $(2,1)$. The graph $K_{(2)}$ consists of one vertex of weight $2$ and gives the type $(2)$. The empty type corresponds to the graph with no vertices.

Here, the complete graph requires the parts of a single factor to have distinct colors. This allows us to pass from a basis partition to a product of two partitions.

## Graph union and partition multiplication

Consider two graphs $(G,\omega_G)$ and $(H,\omega_H)$ on disjoint vertex sets. Their **disjoint union** $G\sqcup H$ retains all vertices and edges of both graphs, with no edges between the factors. Its weight function $\omega$ agrees with the original functions on the two vertex sets.

> [!info] Graph union and partition multiplication
> **Theorem.** The formal sums of color-class types satisfy
>
> $$
> \boxed{
> \mathcal C(G\sqcup H,\omega)
> =\mathcal C(G,\omega_G)*\mathcal C(H,\omega_H)
> }
> $$
>
> The symbol $*$ denotes the [[The Second-Kind Algebra on Partitions#The product through partial matchings|product through partial matchings]].

> [!note]- Proof
> **Proof.** Choose a partition of the vertices of $G$ into independent blocks $A_1,\ldots,A_r$ and a partition of the vertices of $H$ into independent blocks $B_1,\ldots,B_s$. Within each graph, different blocks have distinct colors.
>
> The color of a block $A_i$ may coincide with that of one block $B_j$. Such coincidences form a partial matching of blocks. Since there are no edges between the graphs, every partial matching is admissible: the blocks $A_i$ and $B_j$ merge into an independent color class, and their weights add. Unmatched blocks remain unchanged.
>
> Conversely, a color-class partition of $G\sqcup H$ uniquely recovers the two original partitions and their matching. Intersect each class with $V(G)$ and $V(H)$, discard empty intersections, and record the pairs of nonempty intersections belonging to the same class. Thus each possibility is enumerated once. Grouping by weight type gives the product $*$. $\square$

In particular, for two weighted complete graphs,

$$
\mathcal C(K_\lambda\sqcup K_\mu)=\lambda*\mu
$$

Thus the coefficients of a product of basis partitions can be obtained by enumerating the color-class partitions of a single graph $K_\lambda\sqcup K_\mu$.

## Two separate vertices

### Unit weights

For two one-part factors of weight $1$,

$$
(1)*(1)=(1^2)+(2)
$$

Each factor is represented by one vertex. Their disjoint union has no edge, so the vertices may have different colors or a shared color. These cases give the types $(1^2)$ and $(2)$, respectively.

### Weights two and one

With weights $2$ and $1$,

$$
(2)*(1)=(2,1)+(3)
$$

Different colors preserve the two parts $2$ and $1$. A shared color merges the vertices into a class of weight $3$. In both cases the graph has two vertices.

![Two color-class partitions of two separate vertices, first with weights 1 and 1, then with weights 2 and 1](Color%20classes%20of%20two%20vertices.svg)

*Figure 1. The number inside a circle is the vertex weight, and the letter below it is the vertex name. On the left, the vertices have different colors; on the right, they share a color. In the row with weights $2$ and $1$, the shared class gives a part $3$, although it contains two vertices. There are no edges between the vertices. Each panel shows one representative of a color-class partition; the colors may be renamed.*

## Seven possibilities for two edges

For the product of two types $(1^2)$,

$$
\boxed{
(1^2)*(1^2)=(1^4)+4(2,1^2)+2(2^2)
}
$$

Each factor is represented by a complete graph on two vertices of unit weight, that is, an edge. Call the first edge $ab$ and the second $cd$. Throughout this section, the graph consists of these two disjoint edges. The endpoints of each edge have different colors, while vertices from different edges may share a color.

The figure enumerates all color-class partitions of this graph.

![Seven color-class partitions of two disjoint edges: one with four classes, four with three classes, and two with two classes](Seven%20color-class%20partitions.svg)

*Figure 2. Every panel retains the edges $ab$ and $cd$ and the unit vertex weights. Letters inside the circles identify vertices, and colors indicate class membership. The classes are listed below each panel. No new edges are drawn between equally colored vertices from different edges.*

**Four classes.** All vertices have different colors. There is one partition:

$$
a\mid b\mid c\mid d
$$

Its type is $(1^4)$.

**Three classes.** One class contains two vertices, and the others are singletons. The pair must contain one vertex from each edge. This gives four partitions:

$$
ac\mid b\mid d,\qquad
ad\mid b\mid c,\qquad
bc\mid a\mid d,\qquad
bd\mid a\mid c
$$

Each has type $(2,1^2)$, yielding the coefficient $4$.

**Two classes.** Each class contains one vertex from each edge. There are two possible partitions:

$$
ac\mid bd,\qquad ad\mid bc
$$

Both have type $(2^2)$, yielding the coefficient $2$.

A class of three vertices is impossible: it would contain both endpoints of at least one edge. Thus the types $(3,1)$ and $(4)$ do not occur.

| Number of color classes $r$ | Type | Coefficient |
| --- | --- | ---: |
| $4$ | $(1^4)$ | $1$ |
| $3$ | $(2,1^2)$ | $4$ |
| $2$ | $(2^2)$ | $2$ |

In every case, the number of vertices is $N=4$, the total weight is $k=4$, and the graph has $2$ connected components. The number $r$ of color classes ranges from $2$ to $4$ and is a different quantity from the number of connected components. The sum of the coefficients is $7$: the number of admissible class partitions, disregarding color names.

## Isolated vertices and powers of the part of weight one

Let $I_k$ be the graph of $k$ isolated vertices of unit weight. It is the disjoint union of $k$ one-part representatives of $(1)$, so

$$
\mathcal C(I_k)=(1)^k
$$

The graph has no edges, and every partition of its vertices into color classes is admissible. The coefficient of $\lambda\vdash k$ is the number of set partitions of that type, namely the [[Partitions and the Combinatorial Potential of the Second Kind#The combinatorial potential of the second kind|combinatorial potential of the second kind]]:

$$
(1)^k=\sum_{\lambda\vdash k}s_2(\lambda)\lambda
$$

This is the graph interpretation of the [[The Second-Kind Algebra on Partitions#Powers of the part of weight one and combinatorial potentials|lemma on powers of the part of weight one]]. At $k=0$, both sides equal the unit.

For example, four isolated vertices give

$$
(1)^4=(1^4)+6(2,1^2)+3(2^2)+4(3,1)+(4)
$$

There are $15$ class partitions in total. Adding the edges $ab$ and $cd$ excludes partitions that place the endpoints of either edge in one class, leaving the seven possibilities in Figure 2.

Grouping by the number of classes and summing all coefficients gives the Stirling numbers of the second kind and the Bell numbers, respectively:

$$
\sum_{\substack{\lambda\vdash k\\\#\lambda=r}}s_2(\lambda)=S(k,r),
\qquad
\sum_{\lambda\vdash k}s_2(\lambda)=B_k
$$

## The chromatic symmetric function

Now retain the color names. Number the colors by positive integers and assign a variable $y_i$ to color $i$.

> [!info] The chromatic symmetric function
> **Definition.** The chromatic symmetric function of a vertex-weighted graph is
>
> $$
> X_{H,\omega}(\mathbf y)
> =\sum_{\kappa\ \text{proper}}\prod_{v\in V}y_{\kappa(v)}^{\omega(v)}
> $$
>
> Here $\kappa(v)$ is the color number assigned to vertex $v$. This is the standard definition for graphs with positive integer vertex weights [1, §3]. With unit weights, it gives the ordinary chromatic symmetric function. The variables are formal, so analytic convergence is not at issue.

Fix a color-class partition of weight type $\lambda=(a_1,\ldots,a_r)$. Distinct classes receive pairwise distinct color numbers. Their total contribution is

$$
\sum_{\substack{i_1,\ldots,i_r\geqslant1\\i_1,\ldots,i_r\ \text{pairwise distinct}}}
y_{i_1}^{a_1}\cdots y_{i_r}^{a_r}
=\widetilde m_\lambda(\mathbf y)
$$

This is the function used in the [[The Second-Kind Algebra on Partitions#Realization by ordinary multiplication of symmetric functions|realization of the partition algebra]]. Its standard name is **augmented monomial symmetric function** [2, §2]. With part multiplicities $\mu_j$, it is related to the ordinary monomial symmetric function by

$$
\widetilde m_\lambda=[\mu_j!]!\,m_\lambda
$$

For example, two singleton classes of unit weight give

$$
\widetilde m_{(1^2)}=\sum_{i\ne j}y_i y_j
=2\sum_{i<j}y_i y_j
$$

The assignments of colors $i,j$ to two distinguishable classes can be exchanged. They give the same monomial $y_i y_j$ but are two colorings with named colors. This accounts for the normalization when passing from class partitions to the symmetric function.

Let $c_{H,\omega}(\lambda)$ be the coefficient of type $\lambda$ in $\mathcal C(H,\omega)$. Grouping colorings by their class partitions yields

$$
\boxed{
X_{H,\omega}
=\sum_\lambda c_{H,\omega}(\lambda)\widetilde m_\lambda
=\Psi\bigl(\mathcal C(H,\omega)\bigr)
}
$$

Here $\Psi(\lambda)=\widetilde m_\lambda$ is the [[The Second-Kind Algebra on Partitions#Realization by ordinary multiplication of symmetric functions|isomorphism with the algebra of symmetric functions]]. This expansion also appears in [1, Lemma 1]. Since the functions $\widetilde m_\lambda$ form a basis, the formal sum of types $\mathcal C(H,\omega)$ and the chromatic symmetric function contain the same coefficients in different notations.

In particular,

$$
X_{K_\lambda}=\widetilde m_\lambda
$$

For a disjoint union, the colorings of the two graphs are chosen independently, so

$$
X_{G\sqcup H,\omega}=X_{G,\omega_G}X_{H,\omega_H}
$$

This is ordinary multiplication of symmetric functions. The isomorphism $\Psi$ carries the product $*$ of color-class type sums to this ordinary product.

## The place of this model in the series

[[From Polyforms to Partitions|Reduction to toponomes]] produces linear combinations of integer types. [[The Second-Kind Algebra on Partitions|The second-kind algebra]] defines an operation on such combinations. Colorings explain this operation through graph union and connect it to symmetric functions studied in combinatorics.

The sum $\mathcal C(H,\omega)$ is defined by color-class partitions. The toponome $T_G$ of the Laplacian exponential is defined by the chosen spanning-forest expansion. These are different ways of obtaining a sum of types. The [[Partition Products and Boundary Forms|boundary realization of the product]] uses a sum of partial gluings of components at chosen roots; that note also explains how it differs from ordinary multiplication of particular polyforms.

**Checks.** Besides the proof by restricting color classes to the two factors, the partitions of four vertices were enumerated independently. Of the $15$ partitions, checking the edges $ab$ and $cd$ leaves $7$, with coefficients $1,4,2$. The completeness of Figure 2 was checked against this list. The simple examples and the passage to $\widetilde m_\lambda$ were also checked by direct enumeration of colorings with four named colors.

## Sources and connections

This note develops a graph interpretation of the partition algebra used in PMG. Chromatic symmetric functions and their vertex-weighted version are standard constructions; the proofs explain their connection with the adopted product of types.

1. Logan Crew, Sophie Spirkl. [A Deletion-Contraction Relation for the Chromatic Symmetric Function](https://arxiv.org/abs/1910.11859). *European Journal of Combinatorics* **89** (2020), 103143. §3 and Lemma 1: vertex weights, expansion over independent blocks, and the representation of complete graphs.
2. Logan Crew, Sophie Spirkl. [A complete multipartite basis for the chromatic symmetric function](https://arxiv.org/abs/2009.14141), arXiv:2009.14141, version 2, 2021. §2: symmetric functions and the augmented monomial basis.
3. [[The Second-Kind Algebra on Partitions]]  -  the product of types, powers of $(1)$, and the isomorphism with symmetric functions.
4. [[Partitions and the Combinatorial Potential of the Second Kind]]  -  counting partitions of a given type, Stirling numbers, and Bell numbers.
