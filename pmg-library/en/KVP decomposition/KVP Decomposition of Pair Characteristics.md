---
title: KVP Decomposition of Pair Characteristics
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-decomposition-pair-characteristics
lang: en
order: 1
description: "The definition of KVP, the origin and normalization of its three components, uniqueness, coefficient orthogonality, and connections with PMG polyforms and known decompositions."
---

KVP decomposition separates a symmetric pair characteristic into an overall level, vertex heterogeneity, and residual pair structure. This note defines the components and explains why their formulas take this particular form. For a coupling table, the decomposition separates the mean pair weight, deviations of vertex degrees, and the structure remaining after these have been accounted for.

The decomposition also applies to resistances and other symmetric pair data. In each case, however, it is the chosen table that is decomposed: the coupling components and resistance components of the same graph generally differ. Detailed calculations for undirected graphs appear in [[KVP on Simple and Weighted Graphs]].

## The underlying object

Fix a set of $n\ge3$ elements. Consider the space of real symmetric tables with zero diagonal

$$
\mathcal A_n=\{A\in\mathbb R^{n\times n}:A^{\mathsf T}=A,\ A_{ii}=0\}
$$

For a table $A\in\mathcal A_n$, the independent coordinates are the values $A_{ij}$ with $i<j$. The diagonal is not part of the data: the characteristic is defined on pairs of distinct elements. All formulas for pair components below concern $i\ne j$, and their diagonals are zero.

For an undirected graph, $A=C=(c_{ij})$ is the coupling table. With unit couplings, $c_{ij}=1$ on edges and $c_{ij}=0$ on all other pairs. In a weighted graph, the coupling weight replaces the unit value. Absent edges are included as zero pairs; the decomposition uses **all** $\binom n2$ pairs of the specified vertex set. An unknown value is not equivalent to an absent coupling.

The decomposition itself requires neither positivity, connectedness, nor a previously specified metric. These assumptions are needed only for the corresponding graph and metric interpretations.

## Definition of KVP

**Definition.** The KVP decomposition of a table $A$ is a representation

$$
\boxed{A=A_K+A_V+A_P}
\tag{1}
$$

whose components have the following form:

$$
\begin{aligned}
(A_K)_{ij}&=\mu\\
(A_V)_{ij}&=\frac{v_i+v_j}{n-2},\qquad \sum_i v_i=0\\
(A_P)_{ij}&=p_{ij},\qquad p_{ij}=p_{ji},\qquad \sum_{j\ne i}p_{ij}=0
\end{aligned}
\tag{2}
$$

These conditions define three linear subspaces, or **sectors**: $\mathcal K_n$, $\mathcal V_n$, and $\mathcal P_n$. A sector consists of all tables of the corresponding form; a component $A_X$ is part of a particular table $A$.

| Component | Mathematical condition | What it identifies |
|---|---|---|
| K | One constant on all distinct pairs | The overall level of the pair characteristic |
| V | The sum of two vertex corrections with zero mean | Heterogeneity of row sums |
| P | A symmetric residual with zero sum in every row | Pair structure that does not change row sums |

The K-component has the coefficient structure of a complete graph with equal weights. The V-component is determined by a vertex vector. The connection between the P-component and PMG polar forms will be established after deriving the decomposition.

The conditions in (2) are essential. Without $\sum_i v_i=0$, a constant part could be transferred between K and V. Without zero row sums for P, some vertex corrections could remain in the residual. These normalizations remove the ambiguity.

## Deriving the component formulas

Denote the row sums and their mean by

$$
d_i^{(A)}=\sum_{j\ne i}A_{ij},\qquad
\bar d^{(A)}=\frac1n\sum_i d_i^{(A)}
$$

For couplings $C$, these are the weighted degrees and their mean. For an arbitrary table, they remain row sums, without an additional graph interpretation.

### The overall level K

The sum of all pair coefficients is zero for both V and P. The total weight of the table must therefore lie entirely in K. Writing $N=\binom n2$, we obtain

$$
\boxed{\mu_A=\frac1N\sum_{i<j}A_{ij}=\frac{\bar d^{(A)}}{n-1}}
\tag{3}
$$

This is the mean over all distinct pairs, including zero pairs. Averaging only over existing edges would give a different quantity.

Each row of $A_K$ contains $n-1$ entries equal to $\mu_A$, so its sum is $\bar d^{(A)}$. Subtracting K leaves the deviations

$$
v_i^{(A)}=d_i^{(A)}-\bar d^{(A)},\qquad \sum_i v_i^{(A)}=0
\tag{4}
$$

### The vertex correction V

We seek a symmetric correction obtained by adding contributions from the endpoints of each pair: $b_i+b_j$, with $\sum_i b_i=0$. A row sum of this table is

$$
\sum_{j\ne i}(b_i+b_j)=(n-1)b_i-b_i=(n-2)b_i
$$

To match the required deviation $v_i^{(A)}$, we must take $b_i=v_i^{(A)}/(n-2)$. Hence

$$
\boxed{(A_V)_{ij}=\frac{v_i^{(A)}+v_j^{(A)}}{n-2}}
\tag{5}
$$

Thus the denominator $n-2$ comes from computing the row sum. The vertex parameter $v_i^{(A)}$ measures a deviation of the **row sum**, whereas the contribution from one endpoint is $v_i^{(A)}/(n-2)$.

### The residual structure P

After accounting for the mean level and vertex deviations, the remainder is

$$
\boxed{A_P=A-A_K-A_V}
\tag{6}
$$

Its row sums are

$$
\sum_{j\ne i}(A_P)_{ij}=d_i^{(A)}-\bar d^{(A)}-v_i^{(A)}=0
$$

The P-component therefore changes the distribution of values among pairs while preserving the total characteristic of each element. In particular, two tables on the same set with identical row sums have identical K- and V-components, and their difference lies entirely in the P-sector.

## Existence, uniqueness, and projectors

**Theorem.** For $n\ge3$, every table $A\in\mathcal A_n$ has a unique KVP decomposition. Its components are given by formulas (3)-(6).

**Proof.** The constructed components satisfy all conditions in (2), proving existence. In any decomposition, the sum of pair values determines $\mu$ by (3). The row sums then determine $v_i$ by (4). The residual $A_P$ is consequently unique as well. $\square$

Denote the linear operators extracting the components by $\Pi_K$, $\Pi_V$, and $\Pi_P$:

$$
\begin{aligned}
(\Pi_K A)_{ij}&=\mu_A\\
(\Pi_V A)_{ij}&=\frac{v_i^{(A)}+v_j^{(A)}}{n-2}\\
\Pi_P A&=A-\Pi_K A-\Pi_V A
\end{aligned}
$$

Decomposing a pure component again returns that component and zero for all the others. These operators are therefore projectors:

$$
\Pi_X^2=\Pi_X,\qquad
\Pi_X\Pi_Y=0\quad(X\ne Y),\qquad
\Pi_K+\Pi_V+\Pi_P=\operatorname{Id}_{\mathcal A_n}
\tag{7}
$$

Relabeling the elements merely permutes the rows and columns of all three components. Canonicity refers to a fixed set of elements with all pairs treated equally. Adding a vertex, even an isolated one, changes $n$, the mean, and the projectors themselves.

## Coefficient orthogonality

Introduce an auxiliary inner product on the space of pair tables:

$$
\langle A,B\rangle_0=\sum_{i<j}A_{ij}B_{ij},\qquad
\|A\|_0^2=\sum_{i<j}A_{ij}^2
$$

Here $\langle A,B\rangle_0$ is the ordinary Euclidean inner product of table coordinates. It is not the metric inner product of PMG vertices or vectors. We call $\|A\|_0^2$ the **coefficient sum of squares**.

**Theorem.** The K-, V-, and P-sectors are pairwise orthogonal with respect to $\langle\ ,\ \rangle_0$. Consequently,

$$
\boxed{\mathcal A_n=\mathcal K_n\mathbin\oplus\mathcal V_n\mathbin\oplus\mathcal P_n}
$$

**Proof.** Every V- or P-table has zero sum of coefficients and is therefore orthogonal to a constant K-table. For $V(v)\in\mathcal V_n$ and $P\in\mathcal P_n$,

$$
\langle V(v),P\rangle_0
=\frac1{n-2}\sum_{i<j}(v_i+v_j)P_{ij}
=\frac1{n-2}\sum_i v_i\sum_{j\ne i}P_{ij}=0
$$

Orthogonality makes the sum direct, and the construction of the components has already proved that it exhausts the space. $\square$

The projectors are self-adjoint with respect to this inner product. The coefficient sum of squares splits into three terms:

$$
\boxed{\|A\|_0^2
=\binom n2\mu_A^2+\frac1{n-2}\sum_i\bigl(v_i^{(A)}\bigr)^2
+\sum_{i<j}(A_P)_{ij}^2}
\tag{8}
$$

For the V-term, we used $\sum_{i<j}(v_i+v_j)^2=(n-2)\sum_i v_i^2$ under the condition $\sum_i v_i=0$.

There is also a precise approximation interpretation: $A_K+A_V$ is the unique table of the form $b_i+b_j$ closest to $A$ in the sum of squared errors over pairs. Indeed, $K\oplus V$ consists exactly of such tables: for a given sum of components, take $b_i=\mu_A/2+v_i^{(A)}/(n-2)$, while an arbitrary vector $b$ splits into its mean and deviations. The residual $A_P$ is orthogonal to this subspace. This property depends on the chosen coefficient inner product; assigning different weights to pairs defines a different approximation problem.

## The number of independent parameters

**Corollary.** For $n\ge3$,

$$
\dim\mathcal K_n=1,\qquad
\dim\mathcal V_n=n-1,\qquad
\dim\mathcal P_n=\frac{n(n-3)}2
\tag{9}
$$

K is specified by one number. V is specified by $n$ numbers subject to one zero-sum constraint; the vector itself is recovered from the row sums. Subtracting these dimensions from $\dim\mathcal A_n=\binom n2$ gives the dimension of P.

| Number of elements $n$ | All pairs | K | V | P |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 0 |
| 3 | 3 | 1 | 2 | 0 |
| 4 | 6 | 1 | 3 | 2 |
| 5 | 10 | 1 | 4 | 5 |
| 6 | 15 | 1 | 5 | 9 |

On three elements, K and V exhaust every symmetric pair table. A nonzero P-component first becomes possible at $n=4$. For $n=2$, formulas dividing by $n-2$ do not apply: the only pair belongs entirely to K. For $n=1$, the pair space is zero.

## A path on four vertices

The unit-weight path $a-b-c-d$ has three couplings among six possible pairs. Thus

$$
\mu_C=\frac12,\qquad
d=(1,2,2,1),\qquad
v=\left(-\frac12,\frac12,\frac12,-\frac12\right)
$$

![[KVP decomposition of path P4.svg]]

*The original path and its three components on the same vertex set. K assigns weight $1/2$ to every pair. V contains two corrections: $+1/2$ on $bc$ and $-1/2$ on $ad$. In P, the coefficients on $ab,cd$ are positive and those on $ac,bd$ negative; their sum at each vertex is zero. Zero pairs are omitted. Dashed lines indicate negative coefficients.*

For example, the middle edge and the pair of endpoints give

$$
c_{bc}=\frac12+\frac12+0=1,\qquad
c_{ad}=\frac12-\frac12+0=0
$$

For an end edge and one of the absent diagonal couplings,

$$
c_{ab}=\frac12+0+\frac12=1,\qquad
c_{ac}=\frac12+0-\frac12=0
$$

Components may be nonzero on absent edges. Their positive and negative values cancel upon addition. An individual component therefore cannot be regarded as a separate graph with nonnegative couplings.

The complete calculation table and comparisons with complete graphs, cycles, stars, disconnected graphs, and weighted graphs appear in [[KVP on Simple and Weighted Graphs]].

## What the P-component identifies

Every vertex correction $B_{ij}=b_i+b_j$ belongs to $K\oplus V$. Indeed, with $\bar b=n^{-1}\sum_i b_i$, it equals $2\bar b+(b_i-\bar b)+(b_j-\bar b)$. Therefore

$$
\Pi_P(A+B)=\Pi_P A
$$

For four pairwise distinct elements, define

$$
\Delta_{ab|cd}(A)=\frac12(A_{ad}+A_{bc}-A_{ac}-A_{bd})
$$

Constant and vertex terms cancel in this combination:

$$
\Delta_{ab|cd}(A)=\Delta_{ab|cd}(A_P)
$$

This functional measures the difference between two ways of connecting the endpoints of the pairs that cannot be explained by separate vertex corrections. The requirement of four distinct elements is essential: if a vertex is shared, V does not generally cancel.

P is not a cycle count, a measure of connectedness, or a ready-made community partition. For example, a path has nonzero P despite having no cycles; a unit-weight star has zero P despite the strong difference between its center and leaves. The precise meaning of P is given by conditions (2).

## Passing to PMG polyforms

For formal vertices, set $q_{ij}=[(a_i a_j)]^2$. A table $A$ corresponds to the grade-one edge polyform

$$
L(A)=\sum_{i<j}A_{ij}q_{ij}
$$

By linearity, the coefficient decomposition carries over to forms:

$$
L(A)=L(A_K)+L(A_V)+L(A_P)
$$

For a coupling table $C$, this is the Laplacian polyform. The underlying objects are defined in [[Basic Objects and Operations of Polyform Algebra]].

The K-component is proportional to the principal symmetric edge polyform: $L(A_K)=\mu_A\sum_{i<j}q_{ij}$. The connection between P and polar forms is seen in the identity on four distinct vertices:

$$
\{(ab),(cd)\}=q_{ad}+q_{bc}-q_{ac}-q_{bd}
$$

The right-hand side has zero sum of coefficients at each vertex, so its pair table belongs to the P-sector. This is an identity of **forms**, not a numerical inner product. If the decomposed table $A=R$ already specifies resistance norms, metric evaluation gives

$$
(ab)\cdot(cd)=\Delta_{ab|cd}(R)=\Delta_{ab|cd}(R_P)
$$

The coupling table $C$ cannot be substituted for $R$ here. The metric is constructed from the whole Laplacian, and nonlinear inversion need not preserve its components separately.

The Laplacian matrix is written differently:

$$
\mathbf L(A)=\operatorname{diag}(A\mathbf1)-A
$$

Then $\mathbf L(A)=\sum_X\mathbf L(A_X)$, but $\mathbf L(A_X)$ and $A_X$ are different matrices: the K- and V-parts of the Laplacian acquire diagonal entries. In particular, $\mathbf L(A_P)=-A_P$ because P has zero row sums.

## Connections with known decompositions

**KVP is the PMG name for a known canonical decomposition.** Its components have exact counterparts in statistics, representation theory, and algebraic combinatorics.

### The Hoeffding-ANOVA decomposition

Choose two distinct vertices $X,Y$ uniformly, that is, sample without replacement. Setting $\alpha_i=v_i^{(A)}/(n-2)$, rewrite KVP as

$$
A_{XY}=\mu_A+\alpha_X+\alpha_Y+p_{XY}
$$

Here K is the mean, V is the sum of first-order effects, and P is a degenerate second-order interaction. Degeneracy means

$$
\mathbb E[p_{XY}\mid X=i]
=\frac1{n-1}\sum_{j\ne i}p_{ij}=0
$$

The probabilistic inner product is proportional to the coefficient inner product:

$$
\mathbb E[A_{XY}B_{XY}]
=\frac1{\binom n2}\langle A,B\rangle_0
$$

The orthogonal components therefore coincide. This is the finite-population case of the Hoeffding-ANOVA decomposition; its connection with representations is discussed by Peccati and Pycke [1]. Sampling **without replacement** is essential: $X$ and $Y$ are dependent, so formulas for independent observations require different normalizations.

### Representations of the symmetric group

Vertex permutations act on the space of functions on unordered pairs. For $n\ge4$, its known multiplicity-free decomposition is [1, Proposition 2]

$$
\mathcal A_n\cong S^{(n)}\oplus S^{(n-1,1)}\oplus S^{(n-2,2)}
$$

Here $S^\lambda$ denotes the irreducible Specht module of the indicated type.

| PMG sector | Representation | Dimension |
|---|---|---:|
| K | Trivial $S^{(n)}$ | $1$ |
| V | Standard $S^{(n-1,1)}$ | $n-1$ |
| P | $S^{(n-2,2)}$ | $n(n-3)/2$ |

These are the same subspaces with their permutation action, not merely matching dimensions. For $n=3$, only K and V remain.

### The Johnson scheme

Consider the auxiliary Johnson graph $J(n,2)$: its vertices are all unordered pairs of the original elements, and two pairs are adjacent if they share one element. It has $\binom n2$ vertices and is determined by the element set, independently of the entries of the decomposed table.

Its adjacency operator $T$ acts on a pair table as follows:

$$
(TA)_{ij}
=\sum_{k\ne i,j}(A_{ik}+A_{jk})
=d_i^{(A)}+d_j^{(A)}-2A_{ij}
$$

Substituting the definitions of K, V, and P directly gives

$$
T A_K=2(n-2)A_K,\qquad
T A_V=(n-4)A_V,\qquad
T A_P=-2A_P
$$

For $n\ge4$, these three eigenvalues are distinct. KVP is therefore also the spectral decomposition of $T$, and $\Pi_K,\Pi_V,\Pi_P$ coincide with the spectral projectors $E_0,E_1,E_2$ of the Johnson scheme. Filmus [2] gives a general construction of the eigenspaces and orthogonal bases.

This is the spectrum of an auxiliary operator on the space of pair tables. It is not the Laplacian spectrum of the original graph.

The linear decomposition itself is thus known independently of PMG. This series studies its geometric interpretation and applications to polyforms and pair characteristics; the novelty of particular consequences requires a separate comparison with the literature.

## Scope and connections

The definition and proofs concern symmetric pair tables with zero diagonal. They apply to signed data and to connected or disconnected undirected graphs. This three-component construction is insufficient for an arbitrary matrix with an independent diagonal. The oriented extension decomposes the skew-symmetric part and is developed in [[Oriented Extensions of KVP - Circulation and Imbalance]].

The component formulas, uniqueness, and coefficient orthogonality are proved here; the correspondence with irreducible representations relies on [1]. These results do not imply that the spanning-tree coefficient, resistances, or radius are additive over components of the original couplings. Coefficient orthogonality does not imply metric orthogonality of PMG objects either.

The exposition and PMG applications are based on the author's research; the connections with the literature are described above. Examples and their direct checks are collected in [[KVP on Simple and Weighted Graphs]]. The adopted notation and rules for forms are recorded in [[Core specification]] and [[PMG terminology]].

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.

## References

1. Peccati G., Pycke J.-R. *Hoeffding spaces and Specht modules*. ESAIM: Probability and Statistics, 15 (2011), S58-S68. [DOI: 10.1051/ps/2010022](https://doi.org/10.1051/ps/2010022); [open text](https://arxiv.org/abs/0904.3086). Proposition 2 and Theorem 4 relate the irreducible components to Hoeffding spaces.
2. Filmus Y. *An Orthogonal Basis for Functions over a Slice of the Boolean Hypercube*. The Electronic Journal of Combinatorics, 23(1) (2016), P1.23. [DOI: 10.37236/4567](https://doi.org/10.37236/4567); [open text, version v2](https://arxiv.org/abs/1406.0142v2). Section “Johnson association scheme”, Lemma 4.3 in this version: eigenspaces and compatible orthogonal bases.
