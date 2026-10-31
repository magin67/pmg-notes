---
title: Combinatorial Potentials in Symmetric Polyforms
date: 2026-10-20
updated: 2026-10-20
revision: 1
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: combinatorial-potentials-in-symmetric-polyforms
lang: en
description: "Forest types by edges and vertices, zero components, the size of a symmetric sum, and the meaning of its coefficients: a detailed example with the numbers 3, 10, and 30."
order: 2
---

In [[Partitions and the Combinatorial Potential of the Second Kind|the note on the combinatorial potential of the second kind]], the parts of a numerical type specify block sizes. In symmetric polyforms, they specify the grades of block boundaries. In a forest drawing, such a grade is the number of edges in the corresponding component: one edge has type $[1]$, two disjoint edges have type $[1,1]$, and two adjacent edges have type $[2]$.

This change alters the argument of the combinatorial potential. Using type $[2,1]$, we examine three numbers: $3$ as an identity coefficient, $10$ as the number of vertex partitions, and $30$ as the number of forests of the complete graph.

## Drawing a type by its edges

All graphs below have labelled vertices and undirected edges. A forest consists of tree components, including isolated vertices. No roots are distinguished.

A tree on $q$ vertices has $q-1$ edges. The boundary of this vertex set also has grade $q-1$. Each forest component therefore has two descriptions:

$$
\text{vertex block size }q
\quad\longleftrightarrow\quad
\text{boundary grade and number of edges }q-1
$$

![Six forests with types specified by vertex block sizes and by edge counts](Forest%20Types%20by%20Edges.svg)

*Figure 1. One forest is described by two numerical collections. Each block size is one greater than the corresponding part of the type by edges. An isolated vertex has size $1$ and grade $0$.*

Two edges contribute differently to the type depending on whether they share a vertex. If they do, they form one component of type $[2]$; otherwise, they form two components of type $[1,1]$.

Interpreting grade as an edge count applies specifically to forests. A component containing a cycle has more edges than its number of vertices minus one. A triangle, for example, has three edges, but the boundary of its three vertices has grade $2$. In the [[Laplacian Exponential|forest expansion of the exponential]], cyclic edge sets contribute no terms: the product of their affine vectors is zero.

## The full type, positive parts, and zero components

Let a forest have $n$ vertices and $m$ components. Here $m$ means the **total number of components**, including isolated vertices. Of these, $r$ components contain at least one edge and $\ell$ are isolated vertices:

$$
m=r+\ell
$$

The positive grades form the collection $\boldsymbol k=[k_1,\ldots,k_r]$; adding zeros gives the full type:

$$
\boldsymbol\lambda=[k_1,\ldots,k_r,0^\ell],\qquad
k_i\geqslant1
$$

Let $k=w(\boldsymbol k)$ be the total number of edges. Then

$$
\#\boldsymbol k=r,\qquad
\#\boldsymbol\lambda=m,\qquad
w(\boldsymbol\lambda)=k,\qquad
n=k+m=k+r+\ell
$$

The collection of vertex block sizes is

$$
\mathbf x=[k_1+1,\ldots,k_r+1,1^\ell]
$$

It has the same size $m$, but weight $n$. For example,

$$
[2,1,0,0]\longleftrightarrow[3,2,1,1]
$$

Here $k=3$, $r=2$, $\ell=2$, $m=4$, and $n=7$.

**Remark.** A zero grade means a singleton block, not an empty block. The zero appears when passing from vertex count to grade. All blocks in the set partition remain nonempty.

For fixed $n$, the positive parts determine the number of zeros: $\ell=n-k-r$. Thus zeros may be omitted in SPF notation, according to the [[Symmetric Polyforms - Types and Normalizations|convention for abbreviated types]]. For example, $E_5[2,1]$ has no zero parts, while $E_6[2,1]$ means $E_6[2,1,0]$.

## Type [2,1] on five vertices

Consider positive type $[2,1]$ on $\mathbf A=\{a,b,c,d,e\}$. The component with two edges contains three vertices, and the component with one edge contains two. The block sizes are $[3,2]$.

All corresponding vertex partitions can be listed:

$$
\begin{aligned}
&abc\mid de,\qquad abd\mid ce,\qquad abe\mid cd\\
&acd\mid be,\qquad ace\mid bd,\qquad ade\mid bc\\
&bcd\mid ae,\qquad bce\mid ad,\qquad bde\mid ac\\
&cde\mid ab
\end{aligned}
$$

![All ten partitions of five vertices into blocks of sizes three and two, represented by forests](Ten%20Partitions%20of%20Type%2021.svg)

*Figure 2. Each drawing has two adjacent edges and one separate edge, giving type $[2,1]$ by edges. One way to connect each triple has been chosen. Thus ten block partitions are represented by ten forests; the other trees within each triple have not yet been listed.*

The pair can be chosen in $\binom52=10$ ways, after which the triple is determined. The sizes distinguish the blocks, so there is no further division by $2!$. Hence

$$
s_2([3,2])=\frac{5!}{[3!,2!]!\,[1!,1!]!}=10
$$

### From a partition to a form

Fix independent basis vertices over $\mathbb R$ and use [[Basic Objects and Operations of Polyform Algebra|PMG form algebra]]. The partition $abc\mid de$ corresponds to the form

$$
q_{abc\mid de}=[(abc)(de)]^2
$$

The boundary $(abc)$ has grade $2$, the boundary $(de)$ has grade $1$, and their product has grade $3$. Square brackets with exponent $2$ here denote a formal quadratic form, not a numerical collection or its metric evaluation.

> [!info] From a partition to a form
> **Definition.** Let $\mathcal P_n(\boldsymbol\lambda)$ be the set of all partitions of a fixed $n$-vertex set with the given boundary type. For a partition $\pi=\{B_1,\ldots,B_m\}$, put
>
> $$
> q_\pi=[(B_1)\cdots(B_m)]^2
> $$
>
> Here $(B_i)$ denotes the boundary of a block, and the boundary of a singleton is the unit. Passing to the quadratic form removes signs arising from permutations of vertices and blocks. The symmetric sum of this type is
>
> $$
> E_n[\boldsymbol\lambda]
> =\sum_{\pi\in\mathcal P_n(\boldsymbol\lambda)}q_\pi
> $$

Each partition is counted once with coefficient $1$. This is the normalisation in the [[Symmetric Polyforms - Types and Normalizations|definition of symmetric sums]]. Therefore,

$$
\#E_5[2,1]=s_2([3,2])=10
$$

The sign $\#$ denotes the size of this particular representation: the number of terms before applying structural identities. It does not denote a vector-space dimension or an invariant of the polyform itself.

## The size of a symmetric sum

Let $J$ be the set of distinct positive grades in $\boldsymbol k$. For $j\in J$, let $\mu_j$ be the number of parts $k_i$ equal to $j$. Then $\boldsymbol\mu=[\mu_j]_{j\in J}$ is their collection of positive multiplicities.

We use the [[Partitions and the Combinatorial Potential of the Second Kind#The product of a collection|collection product notation]]: $[u_i]!$ is the product of the elements and $[u_i!]!$ is the product of their factorials.

> [!info] The size of a symmetric sum
> **Proposition.** For $r\geqslant1$, $k_i\geqslant1$, and $\ell=n-k-r\geqslant0$, the size of the symmetric sum is
>
> $$
> \boxed{
> \#E_n[k_1,\ldots,k_r,0^\ell]
> =s_2([k_1+1,\ldots,k_r+1,1^\ell])
> =\frac{n!}{\ell!\,[(k_i+1)!]!\,[\mu_j!]!}
> }
> $$

> [!note]- Proof
> **Proof.** Partition the original vertices into blocks of sizes $k_i+1$ and $\ell$ singletons. Apply the potential formula to this collection of sizes. The shift $k_i\mapsto k_i+1$ preserves the multiplicities of the positive parts. All these blocks have size at least $2$, so the singletons form a separate group of multiplicity $\ell$. Their permutations supply the factor $\ell!$, giving the stated formula. $\square$

For type $[2,1,0]$ on six vertices,

$$
\#E_6[2,1,0]
=s_2([3,2,1])
=\frac{6!}{1!\,[3!,2!]!\,[1!,1!]!}
=60
$$

The number $60$ also follows directly: choose the isolated vertex in six ways, then partition the remaining five vertices into a triple and a pair in ten ways.

For type $[2,1,0,0]$ on seven vertices, choose the two isolated vertices as an unordered pair:

$$
\#E_7[2,1,0,0]=\binom72\cdot10=210
$$

### Choosing a subset and the external potential

Let a numerical type $\mathbf x$ have positive parts and weight $v\leqslant n$. First choose $v$ elements from an $n$-element set, then partition the chosen subset according to $\mathbf x$.

> [!info] Choosing a subset and the external potential
> **Definition.** The number of such partial partitions is the **external combinatorial potential**:
>
> $$
> e_n(\mathbf x)=\binom nv s_2(\mathbf x),\qquad v=w(\mathbf x)
> $$

Unchosen elements remain outside the partitioned subset. This condition is part of the object being counted.

If every part of $\mathbf x$ is at least $2$, the unchosen vertices can be added uniquely as singleton blocks. This is precisely the count for symmetric sums:

$$
\#E_n[k_1,\ldots,k_r,0^\ell]
=e_n([k_1+1,\ldots,k_r+1])
=\binom{n}{k+r}s_2([k_1+1,\ldots,k_r+1])
$$

For positive type $[2,1]$, this gives the single expression

$$
\#E_n[2,1,0^{n-5}]=10\binom n5,\qquad n\geqslant5
$$

The absence of parts equal to $1$ is essential for uniqueness of this extension. For example,

$$
e_4([2,1])=\binom43\cdot3=12,
\qquad
s_2([2,1,1])=6
$$

The first count distinguishes a singleton in the chosen subset from an unchosen element. Forgetting this distinction and treating both as ordinary singleton blocks turns each pair of partial partitions into one full partition. For example, $ab\mid c$ with $d$ left outside and $ab\mid d$ with $c$ left outside both give $ab\mid c\mid d$.

## Why there are ten partitions but thirty forests

A block partition specifies the vertices of each component, but does not yet choose its internal edges. On a fixed triple $\{a,b,c\}$ there are three trees:

$$
\{ab,ac\},\qquad \{ab,bc\},\qquad \{ac,bc\}
$$

![Three trees on the same three-vertex set](Three%20Trees%20on%20Three%20Vertices.svg)

*Figure 3. In every case, the vertices form one block of size $3$, and the type by edges is $[2]$. The edge sets differ; each tree has a different central vertex.*

By the [[Basic Objects and Operations of Polyform Algebra|boundary-merging rule]], all three trees give the same quadratic form:

$$
[(ab)(ac)]^2=[(ab)(bc)]^2=[(ac)(bc)]^2=[(abc)]^2
$$

Thus each partition $abc\mid de$ corresponds to three forests: the tree on the triple has three choices, while the edge on the pair is determined. Across all ten partitions, this gives

$$
10\cdot3=30
$$

This is the number of forests of type $[2,1]$ in the complete graph $K_5$. The sum of their forms is $3E_5[2,1]$: each of the ten terms occurs three times.

### Counting forests of a prescribed type

By [[Symmetric Polyforms of the Complete Graph|Cayley's formula]], a fixed set of $k_i+1\geqslant2$ labelled vertices supports $(k_i+1)^{k_i-1}$ trees. Choices in different blocks are independent.

> [!info] Counting forests of a prescribed type
> **Definition.** Denote the number of tree realisations of one fixed block partition by
>
> $$
> t(\boldsymbol k)=[(k_i+1)^{k_i-1}]!
> $$

Each singleton has one realisation without edges. Therefore, the number of forests of this type in $K_n$ is

$$
\boxed{
F_n(\boldsymbol\lambda)
=\#E_n[\boldsymbol\lambda]\,t(\boldsymbol k)
}
$$

> [!note]- Proof
> **Proof.** First choose a vertex partition, in $\#E_n[\boldsymbol\lambda]$ ways. Then choose a tree on each block, in $t(\boldsymbol k)$ independent combinations. Each forest uniquely determines its component partition and the trees on those components, so there is no repetition. $\square$

For $\boldsymbol k=[2,1]$, $t(\boldsymbol k)=[3,1]!=3$. For $[1,1]$, both blocks are pairs, so $t([1,1])=1$: the three pair partitions of four vertices give exactly three forests.

In the formula for $t$, the exponents in the explicitly defined collection $[(k_i+1)^{k_i-1}]$ are ordinary numerical powers. This differs from the shorthand for multiplicities in a type, such as $[1^r]$.

The count $F_n$ applies to the complete graph, where all edges within each block are available. In a general graph, some trees may be absent. The number of its spanning forests with fixed vertex blocks depends on the spanning-tree counts of the induced subgraphs; block sizes alone are insufficient.

## The potential in the fundamental theorem coefficient

Vertex partitions were counted using $[k_i+1,1^\ell]$. Now apply the same function $s_2$ to the **collection of positive grades**:

$$
s_2(\boldsymbol k)=\frac{k!}{[k_i!]!\,[\mu_j!]!}
$$

This potential counts partitions of an auxiliary set of $k$ distinct labels into blocks of sizes $k_1,\ldots,k_r$.

For $\boldsymbol k=[2,1]$, take labels $\alpha,\beta,\gamma$. The three partitions are

$$
\alpha\beta\mid\gamma,\qquad
\alpha\gamma\mid\beta,\qquad
\beta\gamma\mid\alpha
$$

Hence $s_2([2,1])=3$. Here an auxiliary three-element set is partitioned. The five original vertices are partitioned according to different sizes, $[3,2]$, giving $10$ possibilities.

### From the potential to the coefficient

For $k\geqslant1$, the principal polyform $E_n[k]$ has one block of $k+1$ vertices; the other $n-k-1$ vertices are singletons. The general [[Fundamental Theorem of Symmetric Polyforms|fundamental theorem of SPFs]] gives

$$
E_n[k_1,\ldots,k_r,0^\ell]
=\frac{(n-k-1)!\,k!}{\ell!\,[k_i!]!\,[\mu_j!]!}E_n[k]
$$

Separating the combinatorial potential within this coefficient yields

$$
\boxed{
E_n[k_1,\ldots,k_r,0^\ell]
=\frac{(n-k-1)!}{\ell!}\,s_2(\boldsymbol k)E_n[k]
=\frac{(m-1)!}{\ell!}\,s_2(\boldsymbol k)E_n[k]
}
$$

The last expression uses $m=n-k$. The principal representation has $m-1$ singletons, while the original representation has $\ell$. The factorial ratio relates these two numbers; it is an additional factor from the fundamental theorem, outside the ordinary potential $s_2(\boldsymbol k)$.

For type $[2,1]$ on five vertices, $m=2$ and $\ell=0$. The factorial ratio is $1$, so

$$
E_5[2,1]=s_2([2,1])E_5[3]=3E_5[3]
$$

The three auxiliary partitions explain the number $s_2([2,1])$, but do not by themselves prove the form identity. Its algebraic justification is given in [[Fundamental Theorem of Symmetric Polyforms|the proof of the fundamental theorem]].

### Zero components change the coefficient

Adding an isolated vertex preserves the positive collection $[2,1]$ and its potential $3$. However, both the number of vertex partitions and the identity coefficient change:

| $n$ | Full type | $\#E_n$ | Coefficient of $E_n[3]$ | Forest count $F_n$ |
| ---: | --- | ---: | ---: | ---: |
| 5 | $[2,1]$ | 10 | 3 | 30 |
| 6 | $[2,1,0]$ | 60 | 6 | 180 |
| 7 | $[2,1,0,0]$ | 210 | 9 | 630 |

Throughout this family, $r=2$, $k=3$, and $\ell=n-5$. Therefore,

$$
E_n[2,1,0^{n-5}]
=3\frac{(n-4)!}{(n-5)!}E_n[3]
=3(n-4)E_n[3],\qquad n\geqslant5
$$

Even when there are no zeros, the extra factor cannot always be omitted. If $\ell=0$, the total number of components is $r$, and the coefficient is $(r-1)!s_2(\boldsymbol k)$. For three disjoint edges, for example,

$$
s_2([1,1,1])=1,
\qquad
E_6[1,1,1]=2E_6[3]
$$

The additional factor is $2!=2$.

Grade zero is treated separately: $E_n[0^n]=e$. Its sole partition consists of singletons, and its sole forest has no edges. The formula involving $s_2(\boldsymbol k)$ assumes at least one positive part and does not apply to this case.

## What the numbers 3, 10, and 30 mean

For type $[2,1]$ by edges on five vertices, the results are:

| Quantity | Objects counted | Value |
| --- | --- | ---: |
| $s_2([2,1])$ | Partitions of three auxiliary labels into a pair and a singleton | 3 |
| $\#E_5[2,1]=s_2([3,2])$ | Partitions of five vertices into a triple and a pair | 10 |
| $t([2,1])$ | Choices of trees on already fixed vertex blocks | 3 |
| $F_5([2,1])$ | All complete-graph forests with component sizes $3$ and $2$ | 30 |

The equality $s_2([2,1])=t([2,1])=3$ belongs to this example. These are different functions: for instance, $s_2([2])=1$, whereas $t([2])=3$.

The identity coefficient cannot be found by dividing representation sizes either. The sum $E_5[3]$ has five terms, since its four-vertex block can be chosen in five ways. Thus in

$$
E_5[2,1]=3E_5[3]
$$

the left side has ten terms with coefficient $1$, and the right side has five terms with coefficient $3$. The sums of coefficients are $10$ and $15$; the polyforms are equal because of a structural identity, not because their written term counts agree.

## Verification and related notes

The numbers $10,60,210$ were independently checked by enumerating partitions of five-, six-, and seven-vertex sets into blocks of sizes $3,2$ and singletons. The numbers $30,180,630$ were checked by separately enumerating three-edge forests of the complete graphs on those sets. The identities $E_5[2,1]=3E_5[3]$, $E_6[2,1,0]=6E_6[3]$, and $E_6[1,1,1]=2E_6[3]$ were also checked by exact expansion of boundaries and quadratic forms in an exterior-product basis. These checks concern the stated finite examples; the general formulas are proved here or in the linked notes.

In the [[Symmetric Polyforms of the Complete Graph|forest representation of the complete-graph exponential]], the factor $t(\boldsymbol k)$ multiplies the symmetric sum of the corresponding type. [[Forest Coefficients and Abel Polynomials|Forest coefficients]] use products $s_2(\boldsymbol k)t(\boldsymbol k)$ and their sums over positive types. Their combinatorial meaning is treated separately and is not simply the number of forests of a fixed type on the original $n$ vertices.

The number of ways to join prescribed components into one tree is considered in [[Cayley's Theorem and Joining Prescribed Components]]. That count takes place after the internal trees have been chosen and depends only on their block sizes.

This note is based on the author's research within PMG. The potential and collection notation are defined in [[Partitions and the Combinatorial Potential of the Second Kind]]; form definitions, normalisations, and general identities follow the linked public notes.
