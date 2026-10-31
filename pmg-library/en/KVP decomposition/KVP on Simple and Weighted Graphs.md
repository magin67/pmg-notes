---
title: KVP on Simple and Weighted Graphs
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-simple-weighted-graph-examples
lang: en
order: 2
description: "Complete graphs, cycles, stars, paths, disconnected graphs, and a weighted example. Explicit KVP components of coupling tables and checks of coefficient sums of squares."
---

This note computes KVP decompositions for simple undirected graphs with unit couplings, then for a graph with unequal weights. The object being decomposed is the **coupling table** $C=(c_{ij})$, including zero entries on absent edges. The resistance table is not computed here: its components would answer a different question.

Definitions and proofs appear in [[KVP Decomposition of Pair Characteristics]]. The examples show what each sector describes and why P should not be identified with cycles, connectedness, or graph heterogeneity in general.

## Calculation rule

On a fixed set of $n\ge3$ vertices, use

$$
\begin{aligned}
d_i&=\sum_{j\ne i}c_{ij},&
\bar d&=\frac1n\sum_i d_i\\
\mu&=\frac{\bar d}{n-1},&
v_i&=d_i-\bar d
\end{aligned}
$$

For all distinct pairs,

$$
\boxed{(C_K)_{ij}=\mu,\qquad
(C_V)_{ij}=\frac{v_i+v_j}{n-2},\qquad
(C_P)_{ij}=c_{ij}-\mu-\frac{v_i+v_j}{n-2}}
$$

The tables below need only list $i<j$: reversing a pair gives the same value. All component diagonals are zero.

For unit couplings, $\mu=m/\binom n2$, where $m$ is the number of edges. In addition to checking the sum of components on each pair, verify

$$
\sum_i v_i=0,\qquad C_V\mathbf1=v,\qquad C_P\mathbf1=0
$$

## Standard graphs on four vertices

![[Standard graphs for KVP.svg]]

*All six graphs use vertices $a,b,c,d$; each drawn edge has weight $1$. The nonzero components of the coupling table are listed below each graph. The star and the triangle with an isolated vertex have no P. The cycle and the two separate edges have no V. The path has K, V, and P.*

Four vertices give six pairs and $n-2=2$. This is the smallest size at which all three sectors can occur. Using the same vertex and pair order makes the examples directly comparable.

## The complete graph and the empty graph

In the unit-weight complete graph $K_n$, all pair values equal $1$. Thus $d_i=n-1$, $\bar d=n-1$, $\mu=1$, $v_i=0$, and

$$
C=C_K,\qquad C_V=C_P=0
$$

For example, $K_4$ has six edges, and all six K-coefficients equal $1$. If every coupling of the complete graph has the same weight $w$, the same calculation gives $\mu=w$: only the overall level changes.

In the empty graph, all pair values are zero, so all three components are zero. Isolated vertices nevertheless remain part of the specified set: removing them before calculation changes the problem.

## The star: heterogeneity without P

Consider the unit-weight star $K_{1,3}$ with center $a$ and leaves $b,c,d$. Its edges are $ab,ac,ad$. We have

$$
d=(3,1,1,1),\qquad \bar d=\frac32,\qquad
\mu=\frac12,\qquad
v=\left(\frac32,-\frac12,-\frac12,-\frac12\right)
$$

| Pairs | $c_{ij}$ | K | V | P |
|---|---:|---:|---:|---:|
| $ab,ac,ad$ | $1$ | $1/2$ | $1/2$ | $0$ |
| $bc,bd,cd$ | $0$ | $1/2$ | $-1/2$ | $0$ |

The overall level first assigns weight $1/2$ to every pair. The vertex correction increases the center's couplings to $1$ and sets the leaf pairs to zero. There is no residual.

This property holds for every unit-weight star $K_{1,n-1}$ with $n\ge3$:

$$
\mu=\frac2n,\qquad
v_a=\frac{(n-1)(n-2)}n,\qquad
v_i=-\frac{n-2}{n}\quad(i\ne a)
$$

Substitution gives $(C_V)_{ai}=1-2/n$ on spokes and $(C_V)_{ij}=-2/n$ between leaves. Hence $C_P=0$. Equivalently, the star table has the form $c_{ij}=b_i+b_j$, with $b_a=1$ and $b_i=0$ at every leaf.

> [!note] Conclusion from the example
> **Conclusion.** A zero P-component does not mean an absence of pronounced structure. It means that additive endpoint contributions describe the pair values completely. For the star, V captures the entire difference between center and leaves.

## The cycle: pair structure without V

The unit-weight cycle $C_4$ has edges $ab,bc,cd,ad$. Every degree equals $2$, so

$$
\mu=\frac23,\qquad v=0,\qquad C_V=0
$$

| Pairs | $c_{ij}$ | K | V | P |
|---|---:|---:|---:|---:|
| $ab,bc,cd,ad$ | $1$ | $2/3$ | $0$ | $1/3$ |
| $ac,bd$ | $0$ | $2/3$ | $0$ | $-2/3$ |

Every row of P contains two entries $1/3$ and one entry $-2/3$, with zero sum. Equal degrees eliminate V but do not eliminate the distinction between adjacent and opposite vertices.

Similarly, for the unit-weight cycle $C_n$ with $n\ge4$,

$$
\mu=\frac2{n-1},\qquad C_V=0,\qquad
(C_P)_{ij}=\begin{cases}
1-\dfrac2{n-1},&ij\text{ is an edge}\\
-\dfrac2{n-1},&ij\text{ is not an edge}
\end{cases}
$$

The cycle $C_3$ is the complete graph $K_3$, so only K remains.

In general, $C_V=0$ is equivalent to equality of all weighted vertex degrees. For a regular graph, P retains the arrangement of couplings after subtracting the constant level.

## The path: all three components

For the unit-weight path $P_4:a-b-c-d$,

$$
d=(1,2,2,1),\qquad \bar d=\frac32,\qquad
\mu=\frac12,\qquad
v=\left(-\frac12,\frac12,\frac12,-\frac12\right)
$$

| Pair | $c_{ij}$ | K | V | P |
|---|---:|---:|---:|---:|
| $ab$ | $1$ | $1/2$ | $0$ | $1/2$ |
| $ac$ | $0$ | $1/2$ | $0$ | $-1/2$ |
| $ad$ | $0$ | $1/2$ | $-1/2$ | $0$ |
| $bc$ | $1$ | $1/2$ | $1/2$ | $0$ |
| $bd$ | $0$ | $1/2$ | $0$ | $-1/2$ |
| $cd$ | $1$ | $1/2$ | $0$ | $1/2$ |

K coincides with the K-component of the star $K_{1,3}$: both graphs have three edges on four vertices. V differs because their degrees differ. For the path, a nonzero P-component remains after these two corrections.

For example, pairs $ab$ and $ac$ receive identical K- and V-contributions, yet one is an edge and the other is not. The P-values $1/2$ and $-1/2$ recover this distinction.

> [!note] Conclusion from the example
> **Conclusion.** Two trees with identical $n,m$ may have substantially different V- and P-components. Nonzero P in a path also shows that P does not indicate the presence of cycles.

## Two separate edges: P does not require connectedness

Let $2K_2$ consist of edges $ab$ and $cd$. All four degrees equal $1$, so

$$
\mu=\frac13,\qquad v=0
$$

| Pairs | $c_{ij}$ | K | V | P |
|---|---:|---:|---:|---:|
| $ab,cd$ | $1$ | $1/3$ | $0$ | $2/3$ |
| $ac,ad,bc,bd$ | $0$ | $1/3$ | $0$ | $-1/3$ |

Each row of P sums to $2/3-1/3-1/3=0$. Disconnectedness causes no difficulty: the decomposition is a linear operation on a table and does not require Laplacian inversion.

Replacing $ab,cd$ with $ac,bd$ preserves the degrees and K. On the fixed labeled vertices, only P changes. This illustrates the general statement about tables with identical row sums.

## A triangle with an isolated vertex

In $K_3\sqcup K_1$, vertices $a,b,c$ form a triangle and $d$ is isolated. Then

$$
d=(2,2,2,0),\qquad \mu=\frac12,\qquad
v=\left(\frac12,\frac12,\frac12,-\frac32\right)
$$

V equals $1/2$ on $ab,ac,bc$ and $-1/2$ on $ad,bd,cd$. Hence $C_P=0$.

The additive expression $c_{ij}=b_i+b_j$, with $b_a=b_b=b_c=1/2$ and $b_d=-1/2$, gives the same result. A negative auxiliary correction is admissible even though all original couplings are nonnegative.

Removing the isolated vertex leaves $K_3$, whose V is zero. There is no contradiction: KVP is defined relative to the entire chosen vertex set. Changing that set changes the mean and the projectors.

## Why P vanishes on three vertices

For the unit-weight path $P_3:a-b-c$,

$$
d=(1,2,1),\qquad \mu=\frac23,\qquad
v=\left(-\frac13,\frac23,-\frac13\right)
$$

Here $n-2=1$. V equals $1/3$ on edges $ab,bc$ and $-2/3$ on the absent pair $ac$. On all three pairs, K and V already reproduce the original value, so P is zero.

This holds for any three weights, including unequal ones: $\dim\mathcal P_3=0$. The first occurrence of P depends on the number of available pairs, not on reaching a particular level of connectivity complexity.

## Comparing unit-weight graphs

For four vertices, denote the coefficient sums of squares of the components by

$$
E_X=\|C_X\|_0^2=\sum_{i<j}(C_X)_{ij}^2
$$

For a unit-weight graph, $\sum_{i<j}c_{ij}^2=m$, so orthogonality gives $E_K+E_V+E_P=m$.

| Graph on four vertices | $m$ | $\mu$ | Nonzero components | $E_K$ | $E_V$ | $E_P$ |
|---|---:|---:|---|---:|---:|---:|
| Empty graph | $0$ | $0$ | None | $0$ | $0$ | $0$ |
| Two edges $2K_2$ | $2$ | $1/3$ | K, P | $2/3$ | $0$ | $4/3$ |
| Star $K_{1,3}$ | $3$ | $1/2$ | K, V | $3/2$ | $3/2$ | $0$ |
| Path $P_4$ | $3$ | $1/2$ | K, V, P | $3/2$ | $1/2$ | $1$ |
| Triangle and isolated vertex | $3$ | $1/2$ | K, V | $3/2$ | $3/2$ | $0$ |
| Cycle $C_4$ | $4$ | $2/3$ | K, P | $8/3$ | $0$ | $4/3$ |
| Complete graph $K_4$ | $6$ | $1$ | K | $6$ | $0$ | $0$ |

The star and the triangle with an isolated vertex have identical sums of squares for all three components, despite being different graphs. Thus the three scalars $E_K,E_V,E_P$ neither replace the full component tables nor determine a graph up to isomorphism.

## A graph with unequal weights

Take the undirected graph on $a,b,c,d$ with coupling table

$$
C=\begin{pmatrix}
0&4&2&0\\
4&0&1&3\\
2&1&0&2\\
0&3&2&0
\end{pmatrix}
$$

Pair $ad$ is not an edge; the other five couplings have weights $4,2,1,3,2$. The total weight is $12$. The weighted degrees and decomposition parameters are

$$
d=(6,8,5,5),\qquad \bar d=6,\qquad
\mu=2,\qquad v=(0,2,-1,-1)
$$

![[KVP decomposition of a weighted graph.svg]]

*The original nonnegative couplings appear on the left, followed by K, V, and P. On the absent pair $ad$, the values $2,-1/2,-3/2$ cancel. In P, opposite pairs have equal values: $1$ on $ab,cd$, $1/2$ on $ac,bd$, and $-3/2$ on $ad,bc$. Zero pairs are omitted; dashed lines indicate negative coefficients.*

### Calculation by pairs

| Pair | $c_{ij}$ | K | V | P |
|---|---:|---:|---:|---:|
| $ab$ | $4$ | $2$ | $1$ | $1$ |
| $ac$ | $2$ | $2$ | $-1/2$ | $1/2$ |
| $ad$ | $0$ | $2$ | $-1/2$ | $-3/2$ |
| $bc$ | $1$ | $2$ | $1/2$ | $-3/2$ |
| $bd$ | $3$ | $2$ | $1/2$ | $1/2$ |
| $cd$ | $2$ | $2$ | $-1$ | $1$ |

For example,

$$
(C_V)_{ac}=\frac{v_a+v_c}{2}=-\frac12,\qquad
(C_P)_{ac}=2-2+\frac12=\frac12
$$

In matrix form,

$$
C_V=\frac12\begin{pmatrix}
0&2&-1&-1\\
2&0&1&1\\
-1&1&0&-2\\
-1&1&-2&0
\end{pmatrix},\qquad
C_P=\frac12\begin{pmatrix}
0&2&1&-3\\
2&0&-3&1\\
1&-3&0&2\\
-3&1&2&0
\end{pmatrix}
$$

The row sums of $C_V$ are $(0,2,-1,-1)$, while every row sum of $C_P$ is zero. K and V together reproduce the degrees $(6,8,5,5)$; P then adjusts individual couplings without changing those degrees.

### Checking the sum of squares

Directly from the original couplings,

$$
\|C\|_0^2=4^2+2^2+0^2+1^2+3^2+2^2=34
$$

The individual components give

$$
E_K=6\cdot2^2=24,\qquad
E_V=\frac{0^2+2^2+(-1)^2+(-1)^2}{2}=3
$$

$$
E_P=1+\frac14+\frac94+\frac94+\frac14+1=7
$$

The total is $24+3+7=34$. This checks the coefficient decomposition; it does not compute resistance norms of the graph.

### The same edges with different weights

The number of nonzero sectors depends on more than the arrangement of edges. For example, for a star with $c_{ab}=1$, $c_{ac}=2$, $c_{ad}=3$ and zero couplings between leaves,

$$
\mu=1,\qquad d=(6,1,2,3),\qquad v=(3,-2,-1,0)
$$

In the pair order $ab,ac,ad,bc,bd,cd$, we obtain

$$
\begin{aligned}
C_V&:\quad \left(\frac12,1,\frac32,-\frac32,-1,-\frac12\right)\\
C_P&:\quad \left(-\frac12,0,\frac12,\frac12,0,-\frac12\right)
\end{aligned}
$$

P is now nonzero, although the edge set is the same as for the unit-weight star. The earlier conclusion $C_P=0$ used equality of all spoke weights.

## What the examples show

K determines the overall mean pair weight. V vanishes when weighted degrees are equal, while P vanishes when the entire table is expressible as sums of vertex corrections. These are distinct conditions that can hold independently: the cycle has zero V, whereas the star has zero P.

The decomposition does not require connectedness and may produce signed coefficients on absent edges. Even for a positive original graph, individual components are generally not positive graphs. Adding a vertex or changing weights requires a new calculation.

All listed values were computed directly from coupling tables. Independent checks in exact rational arithmetic include reconstruction of the original coefficients, component row sums, pairwise coefficient orthogonality, and sums of squares. For complete graphs, stars, and cycles, formulas were derived above for arbitrary vertex counts.

This note is based on the author's PMG research. General definitions and proofs: [[KVP Decomposition of Pair Characteristics]]. Conventions for forms and metric evaluation: [[Core specification]] and [[PMG terminology]].

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
