---
title: Vector and Vertex Normalizations of Toponomes
date: 2026-10-23
updated: 2026-10-23
revision: 1
source_revision: 6
status: draft
text_prepared_by: ChatGPT
translation_key: vector-and-vertex-normalizations-of-toponomes
lang: en
description: "Two normalizations of forest toponomes: root weights, polynomials in one and two variables, products of disjoint graphs, and preservation of structural identities."
order: 1
---

A partition toponome retains component types and their coefficients. To obtain a polynomial in one or two variables, several types are grouped by selected parameters. Before doing so, we must choose the weight assigned to each component. The two principal normalizations produce different coefficients and different graph characteristics.

In **vector normalization**, the original coefficients of the forest representation are retained. In **vertex normalization**, each forest contributes its weight multiplied by the number of ways to choose one root vertex in each component. This note defines both normalizations, explains the order of the reductions, and shows why vertex evaluation, after grouping types of the same grade, respects structural identities.

The construction starts with the Laplacian exponential in the polyform algebra and passes through partition types. The key result, proved in the [[Forest Coefficients and the Laplacian Polynomial#Summing minors and the Laplacian polynomial|theorem identifying the two constructions]], is that the resulting one-variable vertex toponome equals $\det(I+t\mathbf L)$, constructed directly from the Laplacian matrix. The normalization thus also determines the relation between reduction and the matrix characteristic polynomial.

Prerequisites are the [[From Polyforms to Partitions|toponome of a chosen representation]], the [[Toponomes and Structural Identities|criterion for representation-independent reduction]], and [[Coefficient Tables of Toponomes|coefficient triangles]]. The overall reading route appears in [[en/Polynomial toponomes/Polynomial Toponomes|Polynomial Toponomes]].

## Initial data and two kinds of weight

Let $G$ be a finite simple undirected graph on $n\geqslant1$ vertices, with positive conductances on its existing edges. Connectivity is not required for the constructions in this note. Fix the forest representation of the Laplacian exponential obtained by expanding its edge factors:

$$
M_G=\exp L=\sum_{F\in\mathcal F(G)}w(F)q_{\pi(F)},
\qquad
w(F)=\prod_{e\in E(F)}c_e
$$

Here $\mathcal F(G)$ contains all spanning forests, including the empty edge set. Every forest covers all $n$ vertices; its components define a partition $\pi(F)$. A forest need not be maximal.

If the positive type of the partition is $\lambda=(k_1,\ldots,k_r)$, then

$$
k=w(\lambda)=\sum_{i=1}^r k_i,
\qquad m=n-k,
\qquad \ell=n-k-r
$$

The grade $k$ is the number of forest edges, $r$ is the number of nontrivial components, $m$ is the total number of components, and $\ell$ is the number of singleton vertices. A component of grade $k_i$ contains $k_i+1$ vertices. For the empty type $1$, set $k=r=0$ and $m=\ell=n$.

The polynomial notation for the toponome is

$$
T_G(\mathbf x)=\sum_\lambda c_G(\lambda)x_\lambda,
\qquad
x_\lambda=\prod_{i=1}^r x_{k_i},
\qquad
c_G(\lambda)=\sum_{F:\,\lambda(F)=\lambda}w(F)
$$

The empty type corresponds to the monomial $1$, with coefficient $c_G(1)=1$. The original vertex count $n$ is retained separately.

These formulas distinguish the type weight $w(\lambda)=k$ from the forest weight $w(F)$: the former is an integer grade, and the latter is a product of conductances. We now introduce another factor, determined by component sizes.

## Vertex weight and root choices

> [!info] The root weight of a type
> **Definition.** For a positive type $\lambda=(k_1,\ldots,k_r)$, set
>
> $$
> \boxed{h(\lambda)=[k_i+1]!=\prod_{i=1}^r(k_i+1)}
> $$
>
> For the empty type, $h(1)=1$. Under the PMG convention, $[k_i+1]!$ denotes the product of the entries of a collection, not the factorial of a number.

> [!info] Vertex weight and root choices
> **Proposition.** If a forest $F$ has type $\lambda$, the number of ways to choose one root in each component is $h(\lambda)$.

> [!note]- Proof
> **Proof.** Any of the $k_i+1$ vertices of a component of grade $k_i$ can be its root. Choices in different components are independent, so their numbers multiply. A singleton component has exactly one choice and contributes a factor of $1$. $\square$

For the partition $abc\mid de\mid f$, we have $n=6$, $\lambda=(2,1)$, $k=3$, $r=2$, $m=3$, and $\ell=1$. Hence

$$
h(2,1)=3\cdot2\cdot1=6
$$

![Six root choices in the components abc, de, and f](Six%20Root%20Choices.svg)

*Figure 1. All six diagrams show the same forest, with edges $ab,bc,de$ and singleton vertex $f$. The selected roots are circled. The root of the three-vertex component runs through $a,b,c$, and that of the two-vertex component is $d$ or $e$; vertex $f$ is always the root of its component. Choosing roots changes neither the edges nor their weights.*

A root is an additional mark on a vertex. Enumerating roots creates no new unmarked forests and does not glue components together.

## Two normalizations before grouping types

> [!info] Toponome normalizations
> **Definition.** Vector normalization retains the coefficient of each positive type. Vertex normalization multiplies it by $h(\lambda)$:
>
> $$
> \begin{aligned}
> T_G^{\mathrm{vec}}(\mathbf x)&=\sum_\lambda c_G(\lambda)x_\lambda=T_G(\mathbf x)\\
> T_G^{\mathrm{vert}}(\mathbf x)&=\sum_\lambda c_G(\lambda)h(\lambda)x_\lambda
> \end{aligned}
> $$

The passage between them is the componentwise substitution

$$
x_j\longmapsto(j+1)x_j
$$

In this notation, variable indices remain grades in both normalizations. In particular, type $(2,1)$ gives $x_2x_1$ in vector notation and $6x_2x_1$ in vertex notation.

If we additionally replace grades by block sizes, the same contribution on six vertices can be written as $6(3,2,1)$. Here $(3,2,1)$ denotes a **vertex type**, rather than a positive type indexed by grades. Reindexing the parts and multiplying the coefficient by $6$ are separate operations. We retain grade indices below to compare coefficients in the same positions.

In this note, “normalization” refers to the weights of summands under reduction. It does not mean dividing a polyform by its spanning-tree coefficient or changing the graph's resistance metric.

As long as individual types are retained, the passage is invertible: since $h(\lambda)>0$, each coefficient can be divided by its known weight. Information is lost when distinct types are subsequently grouped.

## Polynomials in two variables

Let the formal variable $t$ record the grade $k$, and $u$ the number $r$ of nontrivial components. These are independent parameters: the total component count $m=n-k$ is already determined by the grade and cannot replace $r$ without changing the meaning of the expression.

> [!info] Two-variable toponomes
> **Definition.** The vector and vertex polynomial toponomes are defined by the respective substitutions
>
> $$
> \begin{aligned}
> F_G(t,u)&=T_G(\mathbf x)\big|_{x_j=t^ju}\\
> P_G(t,u)&=T_G(\mathbf x)\big|_{x_j=(j+1)t^ju}
> \end{aligned}
> $$

Both polynomials contain the constant term $1$. For nonempty types, this gives

$$
\begin{aligned}
F_G(t,u)&=1+\sum_{k=1}^{n-1}\sum_{r=1}^{\min(k,n-k)}a_{k,r}t^ku^r\\
P_G(t,u)&=1+\sum_{k=1}^{n-1}\sum_{r=1}^{\min(k,n-k)}b_{k,r}t^ku^r
\end{aligned}
$$

The coefficients are

$$
\boxed{
\begin{aligned}
a_{k,r}&=\sum_{\substack{w(\lambda)=k\\\#\lambda=r}}c_G(\lambda)\\
b_{k,r}&=\sum_{\substack{w(\lambda)=k\\\#\lambda=r}}c_G(\lambda)h(\lambda)
\end{aligned}
}
$$

For unit conductances, $a_{k,r}$ counts forests with $k$ edges and $r$ nontrivial components, whereas $b_{k,r}$ counts such forests together with a root chosen in every component. For arbitrary positive conductances, the weights of these objects are summed.

The admissible indices are the same in both normalizations: $r\leqslant k\leqslant n-r$. Root weights change cell values while preserving the layout of the [[Coefficient Tables of Toponomes#Why the shape is triangular|coefficient triangle]].

### Why normalization precedes grouping

In general, passing from $a_{k,r}$ to $b_{k,r}$ cannot be achieved by multiplying a cell by a number depending only on $k,r$. For example, when $k=4$ and $r=2$, two types are possible:

| Type | Nontrivial block sizes | Root weight |
| --- | --- | ---: |
| $(3,1)$ | $4,2$ | $8$ |
| $(2^2)$ | $3,3$ | $9$ |

Thus

$$
\begin{aligned}
a_{4,2}&=c_G(3,1)+c_G(2^2)\\
b_{4,2}&=8c_G(3,1)+9c_G(2^2)
\end{aligned}
$$

Knowing the unweighted sum does not determine the weighted sum. Both tables are naturally obtained from the full partition toponome, rather than one from the other using a universal cell multiplier. This statement concerns information lost under grouping; it does not assert that every arbitrarily prescribed pair of coefficients is realized by graphs.

## One-variable toponomes

If we no longer distinguish the number of nontrivial components, set $u=1$:

$$
\boxed{
F_G(t)=F_G(t,1)=\sum_{k=0}^{n-1}f_kt^k,
\qquad
P_G(t)=P_G(t,1)=\sum_{k=0}^{n-1}p_kt^k
}
$$

Here $f_0=p_0=1$, and for $k\geqslant1$,

$$
f_k=\sum_r a_{k,r},\qquad p_k=\sum_r b_{k,r}
$$

In other words, the one-variable coefficients are the column sums of the corresponding triangle. The number $n$ is still retained separately; adding an isolated vertex changes none of these polynomials.

The full route to the vertex polynomial is

$$
\exp L\longrightarrow T_G(\mathbf x)
\xrightarrow{x_j=(j+1)t^j}P_G(t)
$$

The first arrow expands the exponential into its forest representation and replaces partition forms by their types. The second incorporates component sizes and groups types of the same grade. Neither the determinant nor the eigenvalues of the Laplacian matrix enter this definition of $P_G(t)$; equality with the matrix polynomial is a separate statement requiring proof.

A single connection of conductance $c$ already distinguishes the normalizations:

$$
F_G(t)=1+ct,\qquad P_G(t)=1+2ct
$$

The nonempty forest of this graph has one two-vertex component and two root choices.

## Disjoint union and multiplication

Let $G\sqcup H$ be the union of graphs on disjoint vertex sets, with no connections between them. We call these parts independent in the combinatorial sense. If $G$ and $H$ are themselves connected, the union has two components.

> [!info] Products of toponomes of independent graphs
> **Lemma.** The toponome of a disjoint union of graphs is the ordinary product of their toponomes. This holds in both normalizations and after passing to one or two variables:
>
> $$
> \begin{aligned}
> T_{G\sqcup H}(\mathbf x)&=T_G(\mathbf x)T_H(\mathbf x)\\
> F_{G\sqcup H}(t,u)&=F_G(t,u)F_H(t,u)\\
> P_{G\sqcup H}(t,u)&=P_G(t,u)P_H(t,u)
> \end{aligned}
> $$

> [!note]- Proof
> **Proof.** Every spanning forest of the union is uniquely specified by a pair of forests in $G$ and $H$. Their weights multiply and their lists of nontrivial components concatenate. Thus the type monomial of the union is the product of the two forest type monomials. Root weights also multiply. Summing over all pairs proves the claim; setting $u=1$ gives the one-variable identities. $\square$

For the full toponome in vertex normalization, the identity follows from the same componentwise substitution $x_j\mapsto(j+1)x_j$. This uses ordinary polynomial multiplication, which concatenates component lists. It differs from the product $*$ in the [[The Second-Kind Algebra on Partitions|second-kind algebra]], which sums partial component matchings. At the table level, ordinary multiplication gives [[Coefficient Tables of Toponomes#Multiplication of tables|convolution in two indices]].

### What changes after passing to one variable

**Irreducibility theorem.** The full and two-variable toponomes of a connected graph on $n\geqslant2$ vertices are irreducible under ordinary multiplication over $\mathbb R$ and $\mathbb C$ in both normalizations. For an arbitrary graph, their irreducible factors correspond to components with edges; isolated vertices contribute a factor of $1$.

Proofs appear in the [[Reducibility of Toponomes#The full toponome under ordinary multiplication|theorem for the full toponome]] and the [[Reducibility of Toponomes#The two-variable toponome and the coefficient triangle|theorem for two variables]]. They exclude arbitrary nonconstant polynomial factors, not only factors that are themselves graph toponomes.

Irreducibility can be lost after substituting $u=1$. Already for the unit-weight path on three vertices,

$$
F_{P_3}(t)=(1+t)^2=F_{K_2}(t)^2
$$

A connected graph can have the same one-variable polynomial as a disjoint union of other graphs. In vertex normalization, a [[Forest Coefficients and the Laplacian Polynomial#Factorization does not determine components|cycle, triangle, and star provide an example]]. Ordinary algebraic reducibility of a polynomial must be distinguished from representing its factors as graph toponomes.

## The path on six vertices

Consider the path $P_6$ with edges $ab,bc,cd,de,ef$, all of conductance $1$. Enumerating subsets of the five edges gives

$$
\begin{aligned}
T_{P_6}(\mathbf x)={}&1+5x_1+(4x_2+6x_1^2)+\\
&+(3x_3+6x_2x_1+x_1^3)+\\
&+(2x_4+2x_3x_1+x_2^2)+x_5
\end{aligned}
$$

Parentheses group equal grades. In grade $4$, the five ways to delete one edge give two forests of type $(4)$, two of type $(3,1)$, and one of type $(2^2)$. Thus the cell considered above is

$$
a_{4,2}=2+1=3,\qquad b_{4,2}=2\cdot8+1\cdot9=25
$$

The two polynomial expressions are

$$
\begin{aligned}
F_{P_6}(t,u)={}&1+5tu+(4u+6u^2)t^2+\\
&+(3u+6u^2+u^3)t^3+(2u+3u^2)t^4+ut^5
\end{aligned}
$$

$$
\begin{aligned}
P_{P_6}(t,u)={}&1+10tu+(12u+24u^2)t^2+\\
&+(12u+36u^2+8u^3)t^3+(10u+25u^2)t^4+6ut^5
\end{aligned}
$$

Their coefficient triangles, with $k$ indexing columns and $r$ indexing rows, are

$$
\mathcal A_{P_6}=\begin{array}{ccccc}
5&4&3&2&1\\
&6&6&3&\\
&&1&&
\end{array}
\qquad
\mathcal B_{P_6}=\begin{array}{ccccc}
10&12&12&10&6\\
&24&36&25&\\
&&8&&
\end{array}
$$

The unit term is kept outside the triangles, and zero positions are left blank. Summing the columns gives

$$
F_{P_6}(t)=1+5t+10t^2+10t^3+5t^4+t^5=(1+t)^5
$$

$$
P_{P_6}(t)=1+10t+36t^2+56t^3+35t^4+6t^5
$$

**Check.** The vector sum $F_{P_6}(1)=32$ counts all $2^5$ edge subsets. The vertex sum $P_{P_6}(1)=144$ counts every root choice in all these forests. The two counts concern different sets of objects.

For any tree on $n$ vertices with unit conductances, the vector polynomial is $(1+t)^{n-1}$, since every edge subset is acyclic. Thus this one-variable polynomial no longer distinguishes tree branching patterns. Vertex coefficients additionally record the sizes of the components produced by edge deletion.

For a path and a cycle on the same number of vertices, dividing each column of the vector triangles by its top entry produces identical triangles. The general proof and an eleven-vertex example appear in the [[Coefficient Tables of Toponomes#Paths and cycles: equal normalized triangles|note on coefficient tables]]. This additional division of cells should be distinguished from choosing vector or root weights for forests.

## Compatibility with structural identities

The [[Toponomes and Structural Identities#One identity and two toponomes|tetrahedron identity]] gives the polyform equality $E_4[1,1]=E_4[2,0]$. The displayed representations map to $3(1^2)$ and $4(2)$.

| Reduction stage | Left-hand side | Right-hand side |
| --- | --- | --- |
| Vector notation retaining types | $3x_1^2$ | $4x_2$ |
| Vertex notation retaining types | $12x_1^2$ | $12x_2$ |
| Vector polynomial in two variables | $3t^2u^2$ | $4t^2u$ |
| Vertex polynomial in two variables | $12t^2u^2$ | $12t^2u$ |
| Vector polynomial in one variable | $3t^2$ | $4t^2$ |
| Vertex polynomial in one variable | $12t^2$ | $12t^2$ |

Equality appears in the last row. Retaining a separate variable for the number of nontrivial components prevents equality: the structural identity relates types with different $r$.

> [!info] Representation-independent vertex evaluation
> **Theorem.** On a fixed set of base vertices, the rule
>
> $$
> q_\pi\longmapsto h(\lambda(\pi))t^{\operatorname{gr}q_\pi}
> $$
>
> extends linearly to a map from the space of partition forms to polynomials and preserves every structural identity. Consequently, the one-variable vertex toponome is independent of the representation of a polyform as a sum of partition forms.

> [!note]- Proof using an auxiliary inner product
> **Proof.** Equip the space of formal vertices with an auxiliary positive definite inner product $\langle\ ,\ \rangle_0$ in which the base vertices are orthonormal. This is a technical evaluation, not the graph's resistance metric. Extend it to exterior powers using Gram determinants.
>
> By bilinearity of forms, the map
>
> $$
> [X,Y]\longmapsto\langle X,Y\rangle_0t^k,
> \qquad X,Y\in\Lambda^kV
> $$
>
> is defined on the forms themselves and preserves all their linear equalities.
>
> For a block $B=\{b_0,\ldots,b_j\}$, its boundary is the exterior product of the differences $b_i-b_0$, $i=1,\ldots,j$. Their auxiliary Gram matrix is $I_j+\mathbf1_j\mathbf1_j^{\mathsf T}$: diagonal entries are $2$, and all others are $1$. Its determinant is $j+1$, since its eigenvalues are $j+1$ and $1$ with multiplicity $j-1$.
>
> Differences formed within disjoint blocks of the partition are orthogonal in this auxiliary metric. The Gram matrix of the entire product of boundaries is block diagonal. Its determinant is $\prod_i(k_i+1)=h(\lambda(\pi))$. Singleton blocks contribute empty determinants, equal to $1$.
>
> Thus the constructed linear map agrees with the stated rule on every partition form. It preserves every structural identity. $\square$

This explanation complements the [[Fundamental Theorem of Symmetric Polyforms#Substituting numbers for components while preserving identities|criterion for admissible component weights]]: there, the weights $(j+1)\alpha^j$ follow from requiring preservation of all equalities in the fundamental SPF theorem. Here, with a formal parameter $t$, preservation of arbitrary linear relations among partition forms has been established.

**Remark.** A linear evaluation need not preserve polyform products. For example, $([(ab)]^2)^2=0$, whereas the product of the two evaluations is $(2t)^2$. Likewise, the definitions of $F_G$ and $P_G$ alone establish no correspondence with the product $*$ of the [[The Second-Kind Algebra on Partitions|second-kind algebra]].

Vector toponomes and the two-variable vertex toponome remain characteristics of a chosen representation. For a graph, that representation is fixed by expanding the edge factors of $\exp L$; arbitrary structural substitutions before reduction require checking their effect.

## Meaning of the coefficients and continuation

| Object | Contributions grouped together | Additional weight |
| --- | --- | --- |
| $T_G^{\mathrm{vec}}(\mathbf x)$ | One positive type | $1$ |
| $T_G^{\mathrm{vert}}(\mathbf x)$ | One positive type | $h(\lambda)$ |
| $F_G(t,u)$ | One grade $k$ and nontrivial component count $r$ | $1$ |
| $P_G(t,u)$ | One grade $k$ and nontrivial component count $r$ | $h(\lambda)$ before grouping |
| $F_G(t)$ | One grade $k$ | $1$ |
| $P_G(t)$ | One grade $k$ | $h(\lambda)$ before grouping |

We have proved the root interpretation of $h$, the coefficient-grouping formulas, and representation independence of the one-variable vertex evaluation. Both normalizations have been computed explicitly for $P_6$. We have also proved multiplicativity under disjoint union and explained why passing to one variable changes conclusions about factorization into graph toponomes.

> [!example]- Independent checks of the examples
> All $32$ edge subsets of $P_6$ were enumerated. Vector coefficients were obtained from the components of each forest. Vertex coefficients were checked independently by enumerating vertex subsets with exactly one root in each component, giving $144$ rooted forests. The tetrahedron identity was additionally checked by expanding the forms in the exterior basis of orthonormal formal vertices.

[[Forest Coefficients and the Laplacian Polynomial]] compares two constructions: reduction of the polyform exponential through partition types, and computation of the determinant of $I+t\mathbf L$. The forest interpretation of principal minors proves that, in vertex normalization, they give the same polynomial. That note also examines its first and highest coefficients. [[Coefficients and Kirchhoff Indices]] relates ratios of vertex coefficients to resistances, the reciprocal spectrum, and the resistance radius.

## Results used

- [[From Polyforms to Partitions]] — types, the forest representation of the exponential, and polynomial notation for a toponome.
- [[Coefficient Tables of Toponomes]] — grouping by grade and number of nontrivial components, and the triangular layout.
- [[Toponomes and Structural Identities]] — representation dependence and the criterion for a well-defined reduction.
- [[Fundamental Theorem of Symmetric Polyforms]] — auxiliary orthonormal evaluation and admissible component weights.
- [[Falling Factorials, Rooted Forests, and Stirling Numbers]] — the combinatorial meaning of root choices.
