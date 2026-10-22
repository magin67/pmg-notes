---
title: From Polyforms to Partitions
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: from-polyforms-to-partitions
lang: en
description: "The toponome of a chosen polyform representation: component-grade types, spanning-forest coefficients, and equivalent notation as a polynomial in several variables. A path on five vertices."
order: 1
---

Each nonzero term obtained by expanding the factors of a Laplacian exponential corresponds to a spanning forest. The forest partitions the vertices into components, and the grades of their boundaries form a numerical type. Replacing each term by its type and collecting equal types gives a **partition toponome**.

This representation records component types and their total coefficients without listing every labelled partition. This note defines the reduction and develops the example of a path on five vertices. It uses the concepts introduced in [[Partition Forms and the Tetrahedron Identity]], [[Partitions and the Combinatorial Potential of the Second Kind]], and [[Laplacian Exponential]].

## From a partition form to its type

Let $A=\{a_1,\ldots,a_n\}$ be a fixed set of basis vertices, with $n=\#A$. The partition

$$
\pi=B_1\mid\cdots\mid B_m
$$

corresponds to the form

$$
q_\pi=[(B_1)\cdots(B_m)]^2
$$

Here $(B_i)$ denotes the simplex boundary on the vertices of block $B_i$. Its grade is $\#B_i-1$. Reordering the vertices within a block or the blocks themselves can change the sign of the exterior argument, but not its quadratic form.

For example,

$$
abc\mid de
\quad\longmapsto\quad
[(abc)(de)]^2
\quad\longmapsto\quad
(2,1)
$$

The first block contains three vertices and gives a boundary of grade $2$; the second contains two vertices and gives a boundary of grade $1$.

![Two blocks of three and two vertices and the corresponding form type (2,1)](Partition%20form%20type.svg)

*Figure 1. The block sizes are $3$ and $2$, while their boundary grades are $2$ and $1$. Edges depict tree representatives of the blocks; the type records grades rather than vertex names or the chosen tree shapes.*

**Definition.** The full type of a partition form is the unordered collection of the boundary grades of all its blocks:

$$
\lambda_{\mathrm{full}}(\pi)
=(\#B_1-1,\ldots,\#B_m-1)
$$

In this series, integer partitions are written in parentheses. The order of parts is immaterial; for definiteness, they may be arranged in decreasing order. The multiplicity of an equal part is indicated by an exponent inside the parentheses:

$$
(2,1,1)=(2,1^2),\qquad (1,1)=(1^2)
$$

This differs from the product power $(1)^2$, whose meaning requires a definition of multiplication of types. Square brackets retain their established meanings for collections, simplices, and forms; in particular, $[x_i]!$ denotes the product of a collection.

**Remark.** A grade type differs from the block-size type used in [[Partitions and the Combinatorial Potential of the Second Kind#Set partitions|combinatorial counting]]. For $abc\mid de$, the sizes form the collection $[3,2]$, whereas the form type is $(2,1)$.

## Singleton vertices and type parameters

A singleton block $\{a\}$ gives the boundary $(a)=1$ and a zero part in the full type. For example, on the set $\{a,b,c,d,e,f\}$,

$$
abc\mid de\mid f
\quad\longmapsto\quad
[(abc)(de)(f)]^2=[(abc)(de)]^2
$$

The full type is $(2,1,0)$.

**Convention.** When the vertex count $n$ is known, zero parts are omitted. The resulting **positive type** is denoted by

$$
\lambda=(k_1,\ldots,k_r),\qquad k_i\geqslant1
$$

Hereafter, a type in a toponome means a positive type. Its weight and number of parts are

$$
k=\sum_{i=1}^{r}k_i,\qquad r=\#\lambda
$$

The type weight equals the grade of the form. The number $r$ counts only nontrivial components. We denote the total number of components by $m$ and the number of singleton vertices by $\ell$:

$$
\boxed{m=n-k,\qquad \ell=m-r=n-k-r}
$$

The sum of the grades of all blocks is $\sum_{i=1}^{m}(\#B_i-1)=n-m$. Thus, $n$ and the positive type uniquely determine the number of zero parts.

For type $(2,1)$ on five vertices, $k=3$, $r=m=2$, and $\ell=0$. On six vertices, the same positive type has $m=3$ and $\ell=1$. Hence $n$ is part of the input data; a positive type alone does not determine it.

If all blocks are singletons, the positive type is empty. We denote the corresponding basis symbol by $1$. For fixed $n$, it represents the partition into $n$ singleton vertices and the form $e=[1]^2$.

## The toponome of a chosen representation

Consider a polyform specified by a particular sum of partition forms on $A$. Denote this expression by $\mathcal E$:

$$
P=\sum_\pi c_\pi q_\pi
$$

The coefficient $c_\pi$ includes all occurrences of the same partition in the chosen expression.

> [!info] Partition toponome
> **Definition.** The partition toponome of a representation $\mathcal E$ is the formal linear combination of positive types
>
> $$
> T_{\mathcal E}=\sum_\lambda C_{\mathcal E}(\lambda)\,\lambda,
> \qquad
> C_{\mathcal E}(\lambda)=\sum_{\pi:\,\lambda(\pi)=\lambda}c_\pi
> $$
>
> Each numerical type is a separate basis symbol; the empty type is denoted by $1$. The term “toponome” is used in PMG as the author's name for this construction.

For example, three terms of the same type with coefficients $u,v,w$ contribute $(u+v+w)\lambda$. On chosen formal sums, the reduction is linear: it respects addition of expressions and scalar multiplication of their coefficients.

Partition forms satisfy structural identities, so equal polyforms may be expressed using different types. The definition does not assume that the reduction preserves all such identities. This distinction is illustrated by the [[Toponomes and Structural Identities#One identity and two toponomes|tetrahedron identity]].

### The Laplacian exponential and forest coefficients

Let $G$ be a finite simple undirected graph on $A$, with positive weights $c_{ij}$ on its edges. Connectivity is not required. The [[Laplacian Exponential|factor representation of the exponential]] gives

$$
L=\sum_{\{i,j\}\in E}c_{ij}[(a_i a_j)]^2,
\qquad
M_G=\exp L=\prod_{\{i,j\}\in E}\bigl(e+c_{ij}[(a_i a_j)]^2\bigr)
$$

A **spanning forest** here includes every vertex of $A$, including isolated vertices. Any acyclic edge set of the graph becomes such a forest by including the remaining vertices as singleton components; maximality of the edge set is not required.

In the product expansion, cyclic edge sets contribute zero. The product over the edges of a tree equals the boundary on its vertices up to sign; this sign disappears in the quadratic form. Thus, expanding the factors gives the representation

$$
M_G=\sum_{F\in\mathcal F(G)}w(F)q_{\pi(F)},
\qquad
w(F)=\prod_{\{i,j\}\in E(F)}c_{ij}
$$

Here $\mathcal F(G)$ is the set of all spanning forests, and $\pi(F)$ is the partition into their components. The empty product of weights is $1$. This expansion is justified by the [[Laplacian Exponential#Grade components and spanning forests|formula for the grade components of the exponential]].

For this specific representation, write $T_G$:

$$
\boxed{
T_G=\sum_\lambda c_G(\lambda)\,\lambda,
\qquad
c_G(\lambda)=\sum_{\substack{F\in\mathcal F(G)\\\lambda(\pi(F))=\lambda}}w(F)
}
$$

For unit weights, $c_G(\lambda)$ counts spanning forests of the given type. For arbitrary numerical weights, it is the sum of products of their edge weights.

Several trees on the same block can give the same partition form, but every forest contributes separately to the coefficient. For example, a triangle with unit weights has three spanning trees. All give the form $[(abc)]^2$, so the coefficient of type $(2)$ is $3$, although there is only one partition $abc$. The distinction between partition counts and forest counts agrees with the [[Combinatorial Potentials in Symmetric Polyforms|combinatorial coefficients of SPFs]].

## Example: a path on five vertices

Consider the path $P_5$ with vertices $a,b,c,d,e$ in order and unit weights on its four edges. Its exponential is

$$
M_{P_5}=
\bigl(e+[(ab)]^2\bigr)
\bigl(e+[(bc)]^2\bigr)
\bigl(e+[(cd)]^2\bigr)
\bigl(e+[(de)]^2\bigr)
$$

### All grade components of the exponential

Expand the product and group terms by grade:

$$
M_{P_5}=M_0+M_1+M_2+M_3+M_4
$$

Here $M_k$ is the component of grade $k$. Writing each component in full gives

$$
M_0=e
$$

$$
M_1=L=[(ab)]^2+[(bc)]^2+[(cd)]^2+[(de)]^2
$$

$$
\begin{aligned}
M_2={}&[(abc)]^2+[(bcd)]^2+[(cde)]^2+\\
&+[(ab)(cd)]^2+[(ab)(de)]^2+[(bc)(de)]^2
\end{aligned}
$$

$$
\begin{aligned}
M_3={}&[(abcd)]^2+[(bcde)]^2+\\
&+[(abc)(de)]^2+[(ab)(cde)]^2
\end{aligned}
$$

$$
M_4=[(abcde)]^2
$$

Every edge set of the path is a forest. The expansion therefore gives one term for each of the $16$ edge sets, with counts $1,4,6,4,1$ by grade. Singleton vertices are omitted from the form arguments; for example, $[(abc)]^2$ here corresponds to $abc\mid d\mid e$.

The types can now be read directly from these formulas. Only the empty type occurs in $M_0$, while the four terms of $M_1$ have type $(1)$ and contribute $4(1)$. Grades $2$ and $3$, where more than one type occurs, deserve a closer look.

### The six two-edge forests

Two selected edges are either adjacent or share no vertex. In the first case, they form a three-vertex component of type $(2)$; in the second, they form two two-vertex components of type $(1^2)$.

![All six two-edge spanning forests of P5, grouped by types (2) and (1²)](Two-edge%20forests%20of%20P5.svg)

*Figure 2. Three forests of type $(2)$ on the left and three of type $(1^2)$ on the right. Solid colored edges belong to the forest; dashed lines show unselected edges of the original path. All five vertices are retained. Both columns have $m=3$ components in total, but the numbers of nontrivial components are $r=1$ and $r=2$, respectively.*

The first line of $M_2$ contains the three forms of adjacent edge pairs, of type $(2)$. The second contains the three forms of nonadjacent pairs, of type $(1^2)$. Thus, grade $2$ maps to $3(2)+3(1^2)$.

### The remaining grades

Selecting three edges omits exactly one of the four. Omitting an end edge leaves a four-vertex path and a singleton: two forests of type $(3)$. Omitting either internal edge splits the path into components of two and three vertices: two forests of type $(2,1)$. All four edges give the unique tree of type $(4)$.

| Grade $k$ | Positive type | Total components $m$ | Nontrivial components $r$ | Singleton vertices $\ell$ | Coefficient |
| --- | --- | --- | --- | --- | --- |
| $0$ | Empty type $1$ | $5$ | $0$ | $5$ | $1$ |
| $1$ | $(1)$ | $4$ | $1$ | $3$ | $4$ |
| $2$ | $(2)$ | $3$ | $1$ | $2$ | $3$ |
| $2$ | $(1^2)$ | $3$ | $2$ | $1$ | $3$ |
| $3$ | $(3)$ | $2$ | $1$ | $1$ | $2$ |
| $3$ | $(2,1)$ | $2$ | $2$ | $0$ | $2$ |
| $4$ | $(4)$ | $1$ | $1$ | $0$ | $1$ |

We obtain

$$
\boxed{T_{P_5}=1+4(1)+3(2)+3(1^2)+2(3)+2(2,1)+(4)}
$$

**Check.** The coefficient sum is $1+4+3+3+2+2+1=16=2^4$, the number of all subsets of the four edges. The counts by grade are $1,4,6,4,1$. Listing the types refines these binomial coefficients: the six two-edge forests are distributed between two types.

### A short weighted example

For a three-vertex path with weight $p$ on $ab$ and $q$ on $bc$,

$$
M=\bigl(e+p[(ab)]^2\bigr)\bigl(e+q[(bc)]^2\bigr)
=e+p[(ab)]^2+q[(bc)]^2+pq[(abc)]^2
$$

Hence

$$
T=1+(p+q)(1)+pq(2)
$$

The coefficient $p+q$ combines two distinct one-edge contributions, while $pq$ is the weight of the unique two-edge tree. With positive noninteger weights, these coefficients need not be integers.

## Partitions and polynomials in several variables

Assign an independent variable $x_j$ to each positive grade $j$. A type is written as the monomial

$$
\lambda=(k_1,\ldots,k_r)
\quad\longleftrightarrow\quad
x_\lambda=x_{k_1}\cdots x_{k_r}
$$

For example,

$$
(2,1)\longleftrightarrow x_2x_1,
\qquad
(1^2)\longleftrightarrow x_1^2,
\qquad
1\longleftrightarrow1
$$

Distinct positive types give distinct monomials: the exponent of $x_j$ is the multiplicity of part $j$. This correspondence therefore extends to a linear bijection between formal sums of types and their polynomial expressions. For fixed $n$, the types satisfy $k+r\leqslant n$.

> [!note] Two notations for the same data
> A partition expression and a polynomial in several variables represent the same toponome. This change of notation is not a further reduction and loses no type information. The original vertex count $n$ is retained separately in both expressions.

In polynomial notation, the graph toponome is

$$
T_G(\mathbf x)=\sum_\lambda c_G(\lambda)x_\lambda
$$

In particular,

$$
T_{P_5}(\mathbf x)=1+4x_1+3x_2+3x_1^2+2x_3+2x_2x_1+x_4
$$

The type weight $k$ is the weighted degree of the monomial when $\deg x_j=j$. Its ordinary total degree is the number of positive parts $r$.

This establishes a correspondence of expressions and their linear operations. Ordinary monomial multiplication concatenates lists of parts; other products of types require separate definitions and do not follow merely from $\lambda\leftrightarrow x_\lambda$. A product allowing components to merge is defined in the [[The Second-Kind Algebra on Partitions#The product through partial matchings|second-kind algebra on partitions]], which also explains its difference from ordinary monomial multiplication.

## Retained information and dependence on representation

For fixed $n$, the toponome retains:

- positive component types and their total coefficients;
- grade $k$, the number $r$ of nontrivial components, and the recovered counts $m$ and $\ell$ for each type;
- for a weighted graph, sums of forest weights grouped by type.

It does not specify which labelled vertices form particular blocks or which individual forests contribute to each coefficient. The internal tree shape on a fixed block is already indistinguishable in $q_\pi$: different trees give the same quadratic form of the boundary. Passing to types additionally forgets the vertex composition of the blocks.

The numerical coefficients of a weighted graph's toponome depend on its edge weights. Here weights are specified numbers. If independent variables attached to labelled edges are retained, the coefficients themselves carry extra information; the reduction then requires further qualification.

For a graph $G$, $T_G$ refers to the expansion of the factors of $\exp L$. Relabelling vertices together with their edges and weights preserves the resulting type coefficients. Replacing a sum of forms by an equal sum using a structural identity is a different operation: it may change the toponome of the representation.

[[Partition Forms and the Tetrahedron Identity|Structural identities]] can relate forms of different types. Thus, passage to types is not declared to be a representation-independent linear map on the polyform algebra itself. The compatibility condition is given by the [[Toponomes and Structural Identities#A criterion for representation-independent reduction|criterion for independence from representation]].

## Sources and correspondence with the literature

The term “partition toponome” and its application to a chosen polyform representation are used within PMG. Forms and the initial exponential representation are defined in the published notes:

- [[Partition Forms and the Tetrahedron Identity]];
- [[Laplacian Exponential]];
- [[Partitions and the Combinatorial Potential of the Second Kind]].

Component generating polynomials of graphs have their own history. For a graph with unit weights, the polynomial expression $T_G$ is obtained from the Noble-Welsh $U$-polynomial: setting its second parameter to $y=1$ retains spanning forests, after which the variable for a component of size $1$ is replaced by $1$, and the variable for size $j+1$ by $x_j$. This follows directly from the spanning-subgraph expansion in [C. Merino, S. D. Noble, *The Equivalence of Two Graph Polynomials and a Symmetric Function*](https://arxiv.org/abs/0805.4793), equation (3.2).

This correspondence concerns the forest generator by component type. Compatibility of the reduction with structural identities of polyforms is a separate question.
