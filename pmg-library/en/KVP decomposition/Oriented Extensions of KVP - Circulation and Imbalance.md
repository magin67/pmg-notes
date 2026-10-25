---
title: Oriented Extensions of KVP - Circulation and Imbalance
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-oriented-extensions-circulation-imbalance
lang: en
order: 3
description: "Definitions of KVPOU and KVPO, circulation and gradient components, balance without regularity, five digraph examples, and the connection with Hodge decomposition."
---

A symmetric pair characteristic has a KVP decomposition into an overall level, vertex heterogeneity, and residual pair structure. Oriented data introduce two further components: **O, the circulation part**, and **U, directional imbalance**. This note defines them mathematically, derives their projectors, and explains why balance eliminates U while allowing nonzero V.

The symmetric part relies on [[KVP Decomposition of Pair Characteristics]]. Balanced graphs and their connection with spanning-tree potentials are defined in [[Balanced Graphs and Spanning-Tree Potentials]]. Here the object being decomposed is the chosen pair table; passage to the Laplacian is specified separately.

## A characteristic of ordered pairs

Fix a set of $n\ge3$ elements. The underlying space consists of real tables with zero diagonal:

$$
\mathcal C_n=\{C\in\mathbb R^{n\times n}:C_{ii}=0\},\qquad
\dim\mathcal C_n=n(n-1)
$$

For a coupling table, $C_{ij}$ is the weight in direction $i\to j$. The two directions of a pair are independent coordinates. An absent arc has zero weight, but its pair still participates in the decomposition. An unknown value is not automatically replaced by zero.

The linear decomposition permits coefficients of either sign and requires no connectedness. The original weights in the graph examples below are nonnegative.

Split the table into its symmetric and skew-symmetric parts:

$$
S=\frac{C+C^{\mathsf T}}2,\qquad
H=\frac{C-C^{\mathsf T}}2,\qquad
C=S+H
$$

The symmetric part $S$ has a KVP decomposition. The new task is to split $H$ into circulation and vertex parts. All formulas for pair components concern $i\ne j$; component diagonals are zero.

## Two different vertex vectors

Introduce outgoing and incoming sums:

$$
d^{out}=C\mathbf1,\qquad d^{in}=C^{\mathsf T}\mathbf1
$$

For a graph, these are the outgoing and incoming weighted degrees. Their half-sum and half-difference are

$$
s=\frac{d^{out}+d^{in}}2=S\mathbf1,\qquad
u=\frac{d^{out}-d^{in}}2=H\mathbf1
$$

Define the mean over ordered distinct pairs and the deviations of the symmetric row sums:

$$
\mu=\frac{\sum_{i\ne j}C_{ij}}{n(n-1)},\qquad
v=s-(n-1)\mu\mathbf1
$$

We have $\sum_i v_i=\sum_i u_i=0$, but the two vectors have different meanings.

| Vector | What is compared | Component determined |
|---|---|---|
| $v$ | A vertex's mean incoming and outgoing weight versus the overall mean across vertices | Symmetric V |
| $u$ | Outgoing versus incoming weight at the same vertex | Skew-symmetric U |

For an undirected graph, $d^{out}=d^{in}$, hence $u=0$. Degrees may nevertheless differ between vertices, and $v$ may be nonzero.

## Definitions of U and O

**Definition.** The skew-symmetric vertex sector is

$$
\mathcal U_n=
\left\{U:U_{ij}=\frac{u_i-u_j}{n},\quad \sum_i u_i=0\right\}
$$

**Definition.** The circulation sector is

$$
\mathcal O_n=
\{O:O^{\mathsf T}=-O,\quad O\mathbf1=0\}
$$

An O-table also has zero column sums. These conditions define linear subspaces and do not require positive coefficients.

**Lemma.** Every skew-symmetric table $H$ has a unique representation

$$
H=C_U+C_O,\qquad
(C_U)_{ij}=\frac{u_i-u_j}{n},\qquad
u=H\mathbf1,\qquad
C_O=H-C_U
$$

**Proof.** Skew-symmetry gives $\sum_i u_i=0$. Seek a correction $\phi_i-\phi_j$ with $\sum_i\phi_i=0$. Its row sum is

$$
\sum_{j\ne i}(\phi_i-\phi_j)
=(n-1)\phi_i+\phi_i=n\phi_i
$$

To reproduce $u_i$, we must therefore set $\phi_i=u_i/n$. The residual $C_O$ is skew-symmetric with zero row sums. In any such decomposition, $u$ is recovered from the row sums of $H$, proving uniqueness. $\square$

The denominators in V and U have different origins: summing two vertex contributions yields the factor $n-2$, while taking their difference yields $n$.

The centering matrix $J=I-\mathbf1\mathbf1^{\mathsf T}/n$ gives another expression for the projector:

$$
C_O=JHJ
$$

Indeed, $H\mathbf1=u$, $\mathbf1^{\mathsf T}H=-u^{\mathsf T}$, and $\mathbf1^{\mathsf T}H\mathbf1=0$, so $JHJ=H-(u\mathbf1^{\mathsf T}-\mathbf1u^{\mathsf T})/n$.

## The full KVPOU decomposition

**Theorem.** Every table $C\in\mathcal C_n$ has a unique decomposition

$$
\boxed{C=C_K+C_V+C_P+C_O+C_U}
\tag{1}
$$

Its components are given by

$$
\begin{aligned}
(C_K)_{ij}&=\mu\\
(C_V)_{ij}&=\frac{v_i+v_j}{n-2}\\
C_P&=S-C_K-C_V\\
(C_U)_{ij}&=\frac{u_i-u_j}{n}\\
C_O&=H-C_U
\end{aligned}
\tag{2}
$$

**Proof.** The symmetric and skew-symmetric parts of $C$ are uniquely determined. Apply the KVP theorem from [[KVP Decomposition of Pair Characteristics#Existence, uniqueness, and projectors]] to the former and the lemma proved above to the latter. $\square$

It is useful to record how both systems of row sums are reconstructed:

$$
d^{out}=(n-1)\mu\mathbf1+v+u,\qquad
d^{in}=(n-1)\mu\mathbf1+v-u
$$

P and O change neither incoming nor outgoing sums.

### Coefficient orthogonality and projectors

On the space of oriented tables, use the inner product

$$
\langle C,D\rangle_0=\frac12\sum_{i\ne j}C_{ij}D_{ij}
$$

On symmetric tables, it agrees with the KVP inner product $\sum_{i<j}C_{ij}D_{ij}$. The factor $1/2$ preserves this normalization when both directions are included.

**Theorem.** The five sectors are pairwise orthogonal with respect to $\langle\ ,\ \rangle_0$.

**Proof.** Symmetric tables are orthogonal to skew-symmetric tables because the contributions of directions $ij$ and $ji$ cancel. Orthogonality of K, V, and P has already been proved. For the remaining pair,

$$
\langle U(u),O\rangle_0
=\frac1{2n}\sum_{i,j}(u_i-u_j)O_{ij}
=\frac1n\sum_i u_i\sum_jO_{ij}=0
$$

The last step uses skew-symmetry of O. $\square$

The linear operators $\Pi_X:C\mapsto C_X$ are self-adjoint projectors:

$$
\Pi_X^2=\Pi_X,\qquad
\Pi_X\Pi_Y=0\quad(X\ne Y),\qquad
\sum_{X\in\{K,V,P,O,U\}}\Pi_X=\operatorname{Id}_{\mathcal C_n}
$$

Writing $\|C\|_0^2=\langle C,C\rangle_0$, we obtain

$$
\boxed{\|C\|_0^2
=\binom n2\mu^2
+\frac{\sum_i v_i^2}{n-2}
+\sum_{i<j}(C_P)_{ij}^2
+\sum_{i<j}(C_O)_{ij}^2
+\frac{\sum_i u_i^2}{n}}
\tag{3}
$$

For U, we used $\sum_{i<j}(u_i-u_j)^2=n\sum_i u_i^2$. Formula (3) concerns table coefficients and does not define the PMG metric inner product.

### Dimensions and reversal of directions

| Sector | Table type | Row sums | Dimension |
|---|---|---|---:|
| K | Symmetric, constant | $(n-1)\mu\mathbf1$ | $1$ |
| V | Symmetric, vertex-based | $v$ | $n-1$ |
| P | Symmetric, residual | $0$ | $n(n-3)/2$ |
| O | Skew-symmetric, circulation | $0$ | $(n-1)(n-2)/2$ |
| U | Skew-symmetric, vertex-based | $u$ | $n-1$ |

U is specified by $n$ numbers with one zero-sum constraint, and the vector is recovered from row sums. The dimension of O is obtained by subtracting $n-1$ from the dimension $n(n-1)/2$ of all skew-symmetric tables. The five dimensions sum to $n(n-1)$.

For $n=3$, the P-sector is zero and the O-sector is one-dimensional. For $n=2$, only K and U remain; the formula dividing by $n-2$ must not be used. For $n=1$, the pair space is zero.

Relabeling vertices permutes the coordinates of all components. Reversing every direction gives

$$
C^{\mathsf T}=C_K+C_V+C_P-C_O-C_U
$$

Thus V and U have the same dimension but different symmetries under transposition.

## Circulations and a triangular basis

The expression $U_{ij}=\phi_i-\phi_j$ means that U is the gradient, or potential, part in pair space. Here $\phi_i=u_i/n$ is defined from the imbalance of the chosen table; these numbers are not vertex spanning-tree potentials.

For any closed walk $i_1\to i_2\to\cdots\to i_m\to i_1$,

$$
U_{i_1i_2}+U_{i_2i_3}+\cdots+U_{i_mi_1}=0
$$

The vertex values cancel in pairs. Thus O completely determines the sums of the skew-symmetric part H around closed walks.

The condition $O\mathbf1=0$ means that the signed flow on the complete graph of pairs has no sources or sinks. Its connection with cycles can be made explicit.

**Lemma.** Choose vertex $n$. For $1\le i<j<n$, let $T^{ij}$ be the unit skew-symmetric circulation around the triangle $i\to j\to n\to i$: its entries are $+1$ along the traversal and $-1$ in reverse. Then

$$
\boxed{O=\sum_{1\le i<j<n}O_{ij}T^{ij}}
\tag{4}
$$

**Proof.** The right-hand side agrees with O on every pair not containing vertex $n$. Zero row sums uniquely determine the remaining values. Each $T^{ij}$ has its own unique pair $(i,j)$ away from vertex $n$, so these tables are linearly independent. $\square$

This gives a basis of $\binom{n-1}{2}$ triangular circulations. Choosing a different vertex changes the basis but not the sector or projector. Components may be nonzero on absent arcs of the original graph: the decomposition takes place in the full pair space.

## Balance and reduced decompositions

**Definition.** A pair table is balanced if $d^{out}=d^{in}$.

**Corollary.** Balance is equivalent to $u=0$ and $C_U=0$. In this case, the **KVPO decomposition** remains:

$$
C=C_K+C_V+C_P+C_O
$$

If also $C=C^{\mathsf T}$, O vanishes and the result is KVP. Conversely, $C_O=C_U=0$ together imply symmetry of C.

| Class of tables | Components necessarily zero | Decomposition |
|---|---|---|
| Arbitrary oriented | None | KVPOU |
| Balanced oriented | U | KVPO |
| Symmetric | O and U | KVP |

**Balance does not imply regularity.** It compares incoming and outgoing sums at each vertex, not the degrees of different vertices. V vanishes exactly when all $s_i$ are equal. For a balanced graph, this means equality of its weighted degrees.

For $n\ge3$, the space of balanced tables has dimension $n(n-1)-(n-1)=(n-1)^2$. Even in the balanced case, individual components may contain negative coefficients and need not be positive graphs.

## Directed graph examples

![[Graph examples for KVPOU.svg]]

*The first four examples. Unlabeled arcs have weight 1. The two opposite arcs between $a$ and $d$ are drawn separately. Nonzero components of the coupling tables are listed below the graphs. Only the last graph has weight 2 on $a\to b$.*

The following tables list coefficients for $i<j$. Reversing a direction preserves the signs of K, V, and P but reverses those of O and U:

$$
C_{ji}=(C_K)_{ij}+(C_V)_{ij}+(C_P)_{ij}-(C_O)_{ij}-(C_U)_{ij}
$$

This reconstructs the full oriented table, not just its upper half.

### The unit directed 3-cycle: K and O

For $a\to b\to c\to a$,

$$
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\qquad
d^{out}=d^{in}=(1,1,1)
$$

Here $\mu=1/2$, $v=u=0$, and P is absent on three vertices. Thus $(C_K)_{ij}=1/2$ on all distinct pairs, and

$$
C_O=\frac12
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix}
$$

Along the traversal, $1/2+1/2=1$; against it, $1/2-1/2=0$. Hence $C=C_K+C_O$. Reversing the directed cycle changes the sign of O and preserves K.

### The unit directed 4-cycle: P appears

For $a\to b\to c\to d\to a$, both degrees of every vertex equal 1. Thus $\mu=1/3$ and $v=u=0$.

The symmetric part is half the coupling table of the undirected cycle: adjacent pairs have value $1/2$, while diagonals $ac,bd$ have value 0. Therefore,

$$
(C_P)_{ij}=
\begin{cases}
1/6,&\text{on adjacent pairs}\\
-1/3,&\text{on diagonal pairs}
\end{cases}
$$

O has coefficient $1/2$ along the traversal, $-1/2$ against it, and 0 on the diagonals. The symmetric sum on an adjacent pair is $1/3+1/6=1/2$; on a diagonal pair it is $1/3-1/3=0$.

Thus $C=C_K+C_P+C_O$. Regularity eliminated V but not P.

### A balanced graph with unequal degrees: all four KVPO components

Add vertex $d$ and unit-weight arcs $a\to d$, $d\to a$ to the unit directed 3-cycle $a\to b\to c\to a$:

$$
C=\begin{pmatrix}
0&1&0&1\\
0&0&1&0\\
1&0&0&0\\
1&0&0&0
\end{pmatrix}
$$

We obtain

$$
d^{out}=d^{in}=(2,1,1,1),\qquad
\mu=\frac5{12},\qquad
v=\left(\frac34,-\frac14,-\frac14,-\frac14\right),\qquad u=0
$$

The component table is

| Pair | K | V | P | O | U |
|---|---:|---:|---:|---:|---:|
| $ab$ | $5/12$ | $1/4$ | $-1/6$ | $1/2$ | $0$ |
| $ac$ | $5/12$ | $1/4$ | $-1/6$ | $-1/2$ | $0$ |
| $ad$ | $5/12$ | $1/4$ | $1/3$ | $0$ | $0$ |
| $bc$ | $5/12$ | $-1/4$ | $1/3$ | $1/2$ | $0$ |
| $bd$ | $5/12$ | $-1/4$ | $-1/6$ | $0$ | $0$ |
| $cd$ | $5/12$ | $-1/4$ | $-1/6$ | $0$ | $0$ |

The graph is balanced, but V is nonzero because vertex $a$ is distinguished. For example,

$$
C_{ad}=\frac5{12}+\frac14+\frac13=1,\qquad
C_{bd}=\frac5{12}-\frac14-\frac16=0
$$

O remains a circulation around triangle $abc$. All four components K, V, P, and O are nonzero.

### Changing one weight: all five components

Now increase only the weight of $a\to b$ from 1 to 2. The other four arcs retain unit weight. Then

$$
d^{out}=(3,1,1,1),\qquad
d^{in}=(2,2,1,1)
$$

and

$$
\mu=\frac12,\qquad
v=\left(1,0,-\frac12,-\frac12\right),\qquad
u=\left(\frac12,-\frac12,0,0\right)
$$

The full decomposition is

| Pair | K | V | P | O | U |
|---|---:|---:|---:|---:|---:|
| $ab$ | $1/2$ | $1/2$ | $0$ | $3/4$ | $1/4$ |
| $ac$ | $1/2$ | $1/4$ | $-1/4$ | $-5/8$ | $1/8$ |
| $ad$ | $1/2$ | $1/4$ | $1/4$ | $-1/8$ | $1/8$ |
| $bc$ | $1/2$ | $-1/4$ | $1/4$ | $5/8$ | $-1/8$ |
| $bd$ | $1/2$ | $-1/4$ | $-1/4$ | $1/8$ | $-1/8$ |
| $cd$ | $1/2$ | $-1/2$ | $0$ | $0$ | $0$ |

Checking both directions of the first pair gives

$$
C_{ab}=\frac12+\frac12+\frac34+\frac14=2,\qquad
C_{ba}=\frac12+\frac12-\frac34-\frac14=0
$$

On the absent pair $bd$, the symmetric and skew-symmetric contributions cancel separately:

$$
\frac12-\frac14-\frac14=0,\qquad
\frac18-\frac18=0
$$

Changing one arc affected all five components. In particular, it is not merely an addition of U.

An independent numerical check verifies the orthogonal sum. The original weights give $\|C\|_0^2=(2^2+1+1+1+1)/2=4$. Directly summing the squares in the table columns gives, respectively,

$$
\|C_K\|_0^2=\frac32,\quad
\|C_V\|_0^2=\frac34,\quad
\|C_P\|_0^2=\frac14,\quad
\|C_O\|_0^2=\frac{11}8,\quad
\|C_U\|_0^2=\frac18
$$

Their sum is 4. For each individual component, the sum of squares over $i<j$ equals half the sum over all directions, because the component is symmetric or skew-symmetric. For the original oriented table, both directions must be included.

### One arc without directed cycles: why O is still nonzero

On three vertices, let the only arc be $a\to b$ of weight 1, with $c$ isolated. Then

$$
C=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
\mu=\frac16,\qquad
v=\left(\frac16,\frac16,-\frac13\right),\qquad
u=\left(\frac12,-\frac12,0\right)
$$

The decomposition is

| Pair | K | V | P | O | U |
|---|---:|---:|---:|---:|---:|
| $ab$ | $1/6$ | $1/3$ | $0$ | $1/6$ | $1/3$ |
| $ac$ | $1/6$ | $-1/6$ | $0$ | $-1/6$ | $1/6$ |
| $bc$ | $1/6$ | $-1/6$ | $0$ | $1/6$ | $-1/6$ |

![[One arc - decomposition into U and O.svg]]

*Decomposition of the skew-symmetric part H of one arc: $H=C_U+C_O$. In these three panels, an arrow labeled $t>0$ means coefficient $+t$ in its direction and $-t$ in reverse. O forms a triangular circulation of weight $1/6$. On pairs $ac$ and $bc$, U and O cancel.*

Here $C_O$ is $1/6$ of the unit circulation $a\to b\to c\to a$, although the original digraph contains no directed cycle. There is no contradiction: O describes the circulation part of a signed skew-symmetric table **on the complete set of pairs**, not a subgraph of the original digraph.

If the same arc is considered on only two vertices, there is no O-sector at all. Adding an isolated vertex changes pair space and its projectors.

## Connection with the PMG circulation form

[[The Circulation Form]] defines the triangular bilinear form

$$
w(abc)=[b-a,c-a]-[c-a,b-a]
$$

Its expanded expression contains $[a,b]+[b,c]+[c,a]$ with positive signs and the three reversed terms with negative signs. This is the coefficient structure of a unit skew-symmetric circulation.

However, passing from a coupling table to the Laplacian introduces a sign. For an arbitrary table C, use

$$
\mathbf L(C)=\operatorname{diag}(C\mathbf1)-C,\qquad
L(C)=\sum_{i\ne j}C_{ij}[a_i,a_i-a_j]
$$

The first expression is a matrix expression, the second a polyform expression. Since $C_O\mathbf1=0$,

$$
\mathbf L(C_O)=-C_O,\qquad
L(C_O)=-\sum_{i<j<n}(C_O)_{ij}w(a_i a_j a_n)
$$

For the unit directed 3-cycle, $L(C_O)=-w(abc)/2$. Hence

$$
L_{abc}=\frac12\left([(ab)]^2+[(bc)]^2+[(ca)]^2-w(abc)\right)
$$

The sign and factor $1/2$ agree with the normalization in [[The Bilinear Laplacian of a Balanced Graph]] and [[The Circulation Form]].

For U, the transformation is different: $\mathbf L(C_U)=\operatorname{diag}(u)-C_U$. A component of the coupling table therefore cannot be identified with the corresponding Laplacian term. The Green matrix and resistance tables also require their own decompositions. The distance transformation and its action on components are treated in [[The Distance Operator and KVP Decomposition]].

## Connection with discrete Hodge decomposition

On the complete graph of pairs, a skew-symmetric table is a signed flow. The decomposition $H=C_U+C_O$ is the orthogonal splitting into a gradient part and a divergence-free part. This is a special case of graph Hodge decomposition, used, for example, in pairwise comparison analysis [1].

With our normalization, $C_U$ is the table of the form $\phi_i-\phi_j$ closest to H in the coefficient sum of squared errors. This follows from the proved orthogonality: $C_U$ belongs to the gradient subspace, while $C_O$ is orthogonal to it. The condition $\sum_i\phi_i=0$ makes the vertex values unique.

The assumptions behind this correspondence matter: all pairs are present and receive equal weight in the inner product. Decomposing only on the edges of a chosen sparse graph, or with different comparison weights, defines different projectors. In particular, decomposing one arc on its own support differs from the example on three vertices.

KVPO and KVPOU are the PMG names for the combined notation of the known symmetric and gradient-circulation decompositions. Applications to PMG geometry require separate definitions and proofs.

## Scope and connections

All linear decomposition formulas, orthogonality, dimensions, and the triangular basis are proved here or reduced to results in [[KVP Decomposition of Pair Characteristics]]. The examples are computed directly from the definitions; the full weighted example also includes a separate check of the coefficient sum of squares.

Symmetric graphs, balanced graphs, and arbitrary digraphs differ in the conditions imposed on U and O. Balance concerns the chosen table and does not automatically survive inversion or other transformations. Additivity of the decomposition likewise does not imply additivity of resistances, the spanning-tree coefficient, or resistance radius over the original coupling components.

Undirected examples are collected in [[KVP on Simple and Weighted Graphs]]. The algebraic meaning of balance is developed in [[The Bilinear Laplacian of a Balanced Graph]], and that of circulation in [[The Circulation Form]]. Current notation is recorded in [[Core specification]] and [[PMG terminology]].

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.

## References

1. Jiang X., Lim L.-H., Yao Y., Ye Y. *Statistical ranking and combinatorial Hodge theory*. Mathematical Programming, 127 (2011), 203-244. [DOI: 10.1007/s10107-010-0419-x](https://doi.org/10.1007/s10107-010-0419-x); [open text](https://arxiv.org/abs/0811.1067). Orthogonal decomposition of pair flows into gradient and circulation parts.
