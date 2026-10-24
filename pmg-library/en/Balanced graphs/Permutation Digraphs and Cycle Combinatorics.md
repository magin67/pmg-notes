---
title: Permutation Digraphs and Cycle Combinatorics
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: permutation-digraphs-and-cycle-combinatorics
lang: en
description: Permutation digraphs, cycle-type probabilities and mean cycle counts, marked open paths, and decomposition of regular balanced digraphs into directed 1-factors.
order: 12
source_revision: 3
---

Degree-one balanced graphs connect directed graph theory with permutations: their components are disjoint directed cycles. Component sizes define the cycle type, and the [[Cyclic Partitions and the Combinatorial Potential of the First Kind|potential of the first kind]] counts graphs of that type on specified vertices. This also answers a probability question: how many cycles of each length occur on average?

Consider finite graphs on $n\geqslant2$ distinguishable vertices, without loops, and with unit arc weights. We also briefly describe intermediate states with open paths, a starting point for an algebra of marked partitions.

## A degree-one balanced graph

**Definition.** A permutation digraph has exactly one outgoing and one incoming arc at each vertex. With unit weights it is a [[Balanced Graphs and Spanning-Tree Potentials#Degree-one balanced graphs and permutations|degree-one balanced graph]].

The unique arc $a_i\to a_{\sigma(i)}$ defines a permutation $\sigma$; excluding loops means $\sigma(i)\ne i$. Unique incoming arcs ensure bijectivity. Independent recipient choices at each vertex do not ensure this condition.

**Proposition.** Such a graph decomposes uniquely into vertex-disjoint directed cycles of length at least $2$.

Following the unique outgoing arc eventually reaches a cycle. An external path cannot enter that cycle, since its entry vertex would then have two incoming arcs. Every vertex therefore already belongs to a cycle. $\square$

For the permutation matrix with $P_{ij}=1$ when $j=\sigma(i)$,

$$
\mathbf L=\mathbf I-\mathbf P,\qquad
\mathbf P\mathbf1=\mathbf1,\qquad
\mathbf P^{\mathsf T}\mathbf1=\mathbf1
$$

Both Laplacian balance conditions hold automatically. “Permutation digraph” here specifically means the directed graph of arcs $i\to\sigma(i)$.

In Secret Santa, a vertex represents a participant and an arc a gift from donor to recipient. Each participant has one recipient and one donor; self-gifts are excluded.

## Graph type and its probability

Write the cycle lengths as $\mathbf k=[k_1,\ldots,k_m]$, with $k_i\geqslant2$ and $\sum_i k_i=n$. The cycle count is $m$. If $\mu_j$ is the multiplicity of length $j$, the number of graphs of this type on specified vertices is

$$
s_1(\mathbf k)=\frac{n!}{\prod_i k_i\prod_j\mu_j!}
$$

The definition and proof appear in [[Cyclic Partitions and the Combinatorial Potential of the First Kind#The potential of a cycle type|the first-kind potential note]].

**Probability model.** Choose uniformly from the $D_n$ derangements, where

$$
D_n=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!},\qquad
D_0=1,\qquad D_1=0
$$

The type probability is $s_1(\mathbf k)/D_n$. Uniformity refers to concrete permutations of distinguishable vertices; numerical types are generally not equiprobable.

![Two types of loopless permutation digraphs on four vertices](Two%20Permutation%20Types%20on%20Four%20Vertices.svg)

*Figure 1. Four vertices permit one directed 4-cycle or two directed 2-cycles. One representative of each type is shown. There are $6$ graphs of the first type and $3$ of the second, totaling $D_4=9$.*

| Type | Graph count | Probability |
| --- | ---: | ---: |
| $[4]$ | $4!/4=6$ | $2/3$ |
| $[2,2]$ | $4!/(2\cdot2\cdot2!)=3$ | $1/3$ |

For unrestricted permutations, including fixed points, grouping by cycle count gives unsigned Stirling numbers of the first kind. Excluding loops gives their [[Cyclic Partitions and the Combinatorial Potential of the First Kind#Excluding fixed points|associated variants]], counting only cycles of length at least $2$.

## Mean number of cycles of a specified length

Let $N_k(\sigma)$ count the selected permutation's directed $k$-cycles.

**Proposition.** For a uniform derangement,

$$
\boxed{
\mathbb E N_k=
\binom nk(k-1)!\frac{D_{n-k}}{D_n}
}
\qquad 2\leqslant k\leqslant n
\tag{1}
$$

> [!note]- Proof
> **Proof.** Count pairs consisting of a permutation and one marked $k$-cycle in it. There are $\binom nk$ choices of vertices, $(k-1)!$ cyclic orders, and $D_{n-k}$ derangements of the remaining vertices.
>
> Each permutation $\sigma$ is counted $N_k(\sigma)$ times. Dividing the pair count by $D_n$ therefore gives the mean. $\square$

For $n=4$,

$$
\mathbb E N_2=\frac23,\qquad
\mathbb E N_3=0,\qquad
\mathbb E N_4=\frac23
$$

The mean number of 2-cycles is $2/3$, while type $[2,2]$ has probability $1/3$: that type contains two cycles. The mean total component count is $4/3$.

If fixed points are allowed and all $n!$ permutations are sampled, the same count gives

$$
\mathbb E N_k=\frac{\binom nk(k-1)!(n-k)!}{n!}=\frac1k,
\qquad 1\leqslant k\leqslant n
$$

The loopless model generally does not give $1/k$. For instance, when $n\geqslant3$, a cycle of length $n-1$ would leave a vertex requiring a loop. Formula (1) expresses this through $D_1=0$.

## Open paths and marked components

During sequential arc addition, retain indegree and outdegree at most $1$. An intermediate graph consists of closed directed cycles, open directed paths, and isolated vertices. Nontrivial open paths have imbalanced endpoints, so these states are not yet completed degree-one balanced graphs.

Mark path components with an underline:

- $k$: a closed directed cycle with $k$ arcs and $k$ vertices;
- $\underline{k}$: an open directed path with $k$ arcs and $k+1$ vertices;
- $\underline0$: an isolated vertex.

For example, $[3,\underline1]$ is a directed 3-cycle and a separate arc, using five vertices. Several components may be marked; the mark specifies component kind rather than a distinguished root vertex.

An arc can be added only from the end of an open path to the beginning of an open path. There are two cases:

$$
\underline{k}\longrightarrow k+1
\qquad(k\geqslant1)
$$

$$
[\underline{k},\underline{\ell}]
\longrightarrow\underline{k+\ell+1}
\qquad(k,\ell\geqslant0)
$$

The first closes a path; the second joins two different paths. Closing $\underline0\to1$ is excluded by the no-loop condition. Already closed cycles cannot participate in arc addition.

![A cycle with an open path, path closure, and joining two paths](Open%20Paths%20and%20Closing%20Directed%20Cycles.svg)

*Figure 2. Top: state $[3,\underline1]$. Below: closing $\underline2$ into a 3-cycle and joining two paths $\underline1$ into $\underline3$. The green arc is added to the blue arcs; the vertex count is unchanged.*

Denote the sum of all admissible single-arc additions by multiplication by $\underline1$, the type of one directed arc. For a formal type combination $F$, this defines

$$
T(F)=F*\underline1
$$

For example,

$$
[\underline1,\underline1]*\underline1
=2[2,\underline1]+2[\underline3]
$$

Either of the two paths can be closed, and they can be joined in two directions. Coefficients count concrete arc additions. This specifies multiplication by the generator $\underline1$. A general product of marked types and its algebraic properties remain a separate investigation. The symbol $*$ here concerns marked path-and-cycle types; agreement with [[The Second-Kind Algebra on Partitions]] is not assumed.

**Random-construction remark.** Uniformly choosing an available arc at each step does not guarantee a uniform completed derangement. Construction may stall: state $[3,\underline0]$ on four vertices cannot be completed. Formula (1) therefore refers to uniform completed permutations. One way to sample them is to choose a uniform permutation and repeat the entire draw whenever a fixed point occurs.

## Regular balanced graphs and permutation decompositions

Call a balanced graph **regular of degree $d$** if each vertex has exactly $d$ incoming and $d$ outgoing arcs. Here $d\geqslant1$, all weights are $1$, loops and repeated arcs are excluded, and opposite arcs are allowed. Degree-two regularity differs from “2-balanced”: the latter means a symmetric graph admitting a decomposition into 2-cycles, without restricting vertex degrees.

**Theorem.** Every such graph decomposes into $d$ arc-disjoint permutation digraphs, each spanning all original vertices.

In digraph theory this is a decomposition into directed 1-factors; see source 3.

> [!note]- Proof
> **Proof.** Create source and receiver copies of the vertex set. Replace $a_i\to a_j$ by an edge from source $a_i$ to receiver $a_j$. The resulting bipartite graph is $d$-regular.
>
> For a source set $S$, let $N(S)$ be its receiver neighbors. There are $d|S|$ edges from $S$, and at most $d|N(S)|$ such edges can enter $N(S)$. Thus $|N(S)|\geqslant|S|$. Hall's theorem gives a perfect matching, assigning one receiver to each source and using every receiver exactly once.
>
> This matching is a permutation digraph. Removing it leaves a regular balanced graph of degree $d-1$. Repeat until no arcs remain. $\square$

If $\mathbf A$ is the original adjacency matrix and $\mathbf P_\alpha$ the extracted permutation matrices, then

$$
\mathbf A=\sum_{\alpha=1}^{d}\mathbf P_\alpha,\qquad
\mathbf L=d\mathbf I-\mathbf A
=\sum_{\alpha=1}^{d}(\mathbf I-\mathbf P_\alpha)
$$

The decomposition need not be unique. Its terms share vertices: **it partitions arcs, not connected components**. The product rule for toponomes of disjoint components therefore does not apply directly.

For Secret Santa with two distinct recipients and two donors per participant, every completed assignment can be split into two assignments in which everyone gives and receives once. A closed three-participant component, for example, consists of two opposite directed 3-cycles.

## Polyforms and the scope of further work

A permutation digraph's cycles have disjoint vertex sets. Its Laplacian is the sum of component Laplacians; the [[The Laplacian Exponential of a Balanced Graph|polyform exponential]] and [[Toponomes of Balanced Graphs and Directed Forests#What is constructed and what remains open|toponomes of the fixed forest representation]] multiply over components. The connected balanced-graph metric applies within each cycle separately.

Cycle lengths and forest toponomes describe different objects. A cycle of length $k$ has $k$ arcs, while its vertex-set boundary has grade $k-1$. A permutation's numerical type cannot be substituted for a forest-form type without an additional transformation.

The algebra of marked partitions, potentials of intermediate states, and transitions between them belong to a further combinatorial topic. Here we have specified the states, two arc-addition rules, and the connection between completed graphs and the first-kind potential.

The regular-graph theorem suggests another extension: their Laplacian polyform is a sum of permutation-digraph Laplacians. Its exponential factors over these terms under [[The Laplacian Exponential of a Balanced Graph#Conventions and the finite exponential|polyform multiplication]]. The analogous ordinary matrix-exponential factorization needs additional conditions.

## Checks and sources

The mean formula is proved by counting marked pairs. Enumeration of all permutations for $2\leqslant n\leqslant8$ also checked type counts and mean $N_k$ after fixed points were excluded. Both transition rules were checked by enumerating partial permutations on up to five vertices.

The note draws on the author's PMG research, including marked components for open paths. Standard definitions and formulas follow:

1. NIST DLMF. [§26.13, Permutations: Cycle Notation](https://dlmf.nist.gov/26.13): cycle decompositions, first-kind Stirling numbers, and derangements.
2. [[Cyclic Partitions and the Combinatorial Potential of the First Kind]]: graph counts of a fixed type and the no-loop restriction.
3. Chishwashwa N., Faber V., Streib N. [Algebraic Constructions for Digraph Routing Problems, §3](https://arxiv.org/html/2405.12374v3#S3): directed 1-factor decompositions and the bipartite proof.
