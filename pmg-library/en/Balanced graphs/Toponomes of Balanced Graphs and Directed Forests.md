---
title: Toponomes of Balanced Graphs and Directed Forests
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: balanced-graph-toponomes-and-directed-forests
order: 11
description: Directed rooted-forest toponomes, vertex and vector normalizations, the symmetric limit, the Laplacian polynomial, and the limitations of multiplication on types.
source_revision: 1
---

The forest expansion of a balanced graph's exponential yields a partition toponome by assigning each directed forest its component-size type. Vertex normalization is the natural starting point because arc directions already determine tree roots. In the symmetric case, the construction agrees with undirected graph toponomes.

This continues [[From Polyforms to Partitions]] and [[Vector and Vertex Normalizations of Toponomes]]. The main results reconcile both normalizations with the symmetric case and identify the vertex polynomial with $\det(\mathbf I+t\mathbf L)$. A fixed forest expansion's toponome differs from a universal reduction of arbitrary bilinear-polyform expressions; no such universal reduction or multiplication rule is assumed here.

## A directed forest in the exponential

Consider a finite loopless balanced graph $G$ on $a_1,\ldots,a_n$, $n\ge2$, with weights $f_{ij}\ge0$. Parallel arcs are combined by adding weights. Connectedness is not yet required. Use the outgoing Laplacian:

$$
\mathbf L=\operatorname{diag}\left(\sum_j f_{ij}\right)-\mathbf F,
\qquad \mathbf F=(f_{ij})
$$

> [!info] A directed forest in the exponential
> **Definition.** A directed spanning forest toward roots contains every vertex, including isolated ones. Each component is a tree with a directed path from every vertex to its root. A nonroot has one outgoing arc, while a root has none. Its weight is
>
> $$
> w(F)=\prod_{i\to j\in F}f_{ij}
> $$

Let $\mathcal F_k^{\to}(G)$ denote these forests with $k$ arcs. Each has $n-k$ components. The empty forest has weight $1$ and all vertices as singleton components.

In the [[The Laplacian Exponential of a Balanced Graph#Expansion over directed forests|forest expansion]], fix $h=(a_1+\cdots+a_n)/n$. Then

$$
M_k=\sum_{F\in\mathcal F_k^{\to}(G)}w(F)[A_F(h),B_F],
\qquad M_k=\frac{L^k}{k!}
$$

Using the same arc order in both products,

$$
A_F(h)=\prod_{i\to j\in F}(a_i-h),
\qquad
B_F=\prod_{i\to j\in F}(a_i-a_j)
$$

Every forest gives a nonzero form. Up to sign, the right argument is the product of component boundaries; the left depends on the selected sources. Generally $A_F(h)\ne B_F$.

For reduction, retain each term's forest label $F$ and weight $w(F)$, then replace the label by its component type. Do not first rewrite the forms using structural identities. This fixes a representation analogous to the edge-based forest expansion in the [[From Polyforms to Partitions#The Laplacian exponential and forest coefficients|symmetric case]].

## Component types and two normalizations

Let the forest components have vertex sets $B_1,\ldots,B_m$. Retain the positive-type convention from [[From Polyforms to Partitions#Singleton vertices and type parameters|the note on types]]:

$$
\lambda(F)=(|B_1|-1,\ldots,|B_m|-1)
$$

Omit zero parts and sort the others in decreasing order. Type $(2,1)$ means a triple and a pair, not components of sizes $2$ and $1$. For known $n$ and $\lambda=(k_1,\ldots,k_r)$, the singleton count is $n-\sum_s k_s-r$. The centroid is not an additional graph vertex and does not enter block sizes.

The empty type is $1$. Notation $(1^2)=(1,1)$ denotes two parts and differs from $(1)*(1)$ in the [[The Second-Kind Algebra on Partitions|second-kind algebra]].

> [!info] The directed rooted-forest toponome
> **Definition.** The vertex toponome of a balanced graph is the formal sum
>
> $$
> \boxed{
> T_G^{\mathrm{vert}}=\sum_\lambda c_G^{\mathrm{vert}}(\lambda)\lambda,
> \qquad
> c_G^{\mathrm{vert}}(\lambda)=\sum_{\lambda(F)=\lambda}w(F)
> }
> \tag{1}
> $$
>
> Sum over all directed spanning forests toward roots. With unit weights, the coefficient counts forests of the specified type.

No extra root-count factor is introduced: directions already fix each component's root. Coefficients depend on the weight matrix, not on a directed-cycle decomposition.

> [!info] Component types and two normalizations
> **Definition.** Obtain vector normalization by dividing each coefficient by the product of its component sizes:
>
> $$
> \boxed{
> c_G^{\mathrm{vec}}(k_1,\ldots,k_r)
> =\frac{c_G^{\mathrm{vert}}(k_1,\ldots,k_r)}{\prod_{s=1}^r(k_s+1)},
> \qquad
> T_G^{\mathrm{vec}}=\sum_\lambda c_G^{\mathrm{vec}}(\lambda)\lambda
> }
> \tag{2}
> $$

For the empty type, the denominator is $1$. This extends the [[Vector and Vertex Normalizations of Toponomes#Two normalizations before grouping types|symmetric normalizations]]. The transformation is reversible while types are retained. For a directed graph, vector coefficients can be fractional even with unit weights; they need not count undirected forests.

To use ordinary polynomials, replace $\lambda=(k_1,\ldots,k_r)$ by $x_\lambda=x_{k_1}\cdots x_{k_r}$. Then

$$
T_G^{\mathrm{vert}}(\mathbf x)
=T_G^{\mathrm{vec}}(\mathbf x)\big|_{x_j\mapsto(j+1)x_j}
$$

This variable product encodes the component list. It is not the second-kind product $*$.

## Agreement with undirected graph toponomes

Suppose $G$ is symmetric, with $f_{ij}=f_{ji}=c_{ij}$. Regard each opposite pair as one undirected coupling of weight $c_{ij}$.

> [!info] Symmetric limit
> **Theorem.** Toponomes (1)-(2) agree with the previously defined vertex and vector toponomes of the undirected graph.

> [!note]- Proof by choosing roots
> **Proof.** Fix an undirected spanning forest with components $B_1,\ldots,B_m$. Choose a root in each and direct every edge toward it. This gives one directed rooted forest. Symmetry ensures that the required arcs exist, with the same weight product.
>
> Conversely, forgetting directions gives such an undirected forest. There are $\prod_s|B_s|$ root choices. Its contribution to (1) is therefore its weight times the product of component sizes, exactly the former vertex normalization. Division in (2) recovers its weight and the former vector normalization. $\square$

Agreement with the symmetric case explains the names. For a nonsymmetric graph, (2) is a specified average of root weights, not an assertion that a corresponding undirected graph exists.

## Unit directed 3- and 4-cycles

### The directed 3-cycle

The cycle $a\to b\to c\to a$ has three one-arc forests of type $(1)$ and three two-arc trees of type $(2)$. The whole cycle is not a forest. Thus

$$
\begin{aligned}
T_G^{\mathrm{vert}}&=1+3(1)+3(2)\\
T_G^{\mathrm{vec}}&=1+\frac32(1)+(2)
\end{aligned}
$$

The second row's coefficient $3/2$ divides three rooted forests by their two-vertex component size; it does not count a fractional number of forests.

### The directed 4-cycle

Take $C_+:a\to b\to c\to d\to a$ with unit weights. Every proper subset of its arcs is a directed rooted forest.

![[Forest Types of a Directed 4-Cycle.svg]]

*Left: the original 4-cycle. Center: arcs $a\to b$, $b\to c$ give a triple rooted at $c$ and singleton $d$, type $(2)$. Right: $a\to b$, $c\to d$ give two pairs rooted at $b,d$, type $(1^2)$. Roots have a light background.*

| Selected arcs | Forest count | Components | Type | Divisor in (2) |
| --- | ---: | --- | --- | ---: |
| None | $1$ | Four singletons | $1$ | $1$ |
| One arc | $4$ | A pair and two singletons | $(1)$ | $2$ |
| Two adjacent arcs | $4$ | A triple and a singleton | $(2)$ | $3$ |
| Two opposite arcs | $2$ | Two pairs | $(1^2)$ | $4$ |
| Three arcs | $4$ | A four-vertex tree | $(3)$ | $4$ |

Therefore

$$
\boxed{T_{C_+}^{\mathrm{vert}}=1+4(1)+4(2)+2(1^2)+4(3)}
$$

$$
\boxed{T_{C_+}^{\mathrm{vec}}=1+2(1)+\frac43(2)+\frac12(1^2)+(3)}
$$

Type $(1^2)$ records two two-vertex components. It does not assert that the corresponding bilinear exponential term is the quadratic form $[(ab)(cd)]^2$.

## Two opposite directed 4-cycles

Add the reverse unit cycle $C_-:a\to d\to c\to b\to a$. Their sum is the symmetric unit cycle $C_4$. In polyform algebra,

$$
M_{C_4}=\exp(L_++L_-)=M_+M_-
$$

Alongside forests contained entirely in one directed cycle, mixed forests appear. Their vertex-normalized counts are:

| Type | Entirely in one cycle, combined | Using both cycles | Total |
| --- | ---: | ---: | ---: |
| $(1)$ | $8$ | $0$ | $8$ |
| $(2)$ | $8$ | $4$ | $12$ |
| $(1^2)$ | $4$ | $4$ | $8$ |
| $(3)$ | $8$ | $8$ | $16$ |

Count the empty forest once. Hence

$$
\begin{aligned}
T_{C_4}^{\mathrm{vert}}&=1+8(1)+12(2)+8(1^2)+16(3)\\
T_{C_4}^{\mathrm{vec}}&=1+4(1)+4(2)+2(1^2)+4(3)
\end{aligned}
$$

Here $T_{C_4}^{\mathrm{vec}}=T_{C_+}^{\mathrm{vert}}$. Every undirected forest of the cycle consists of paths and singletons; orienting its edges along $C_+$ gives exactly one directed rooted forest of the same type.

The factors' toponomes alone cannot recover mixed contributions without knowing how the graphs overlap. Cycles $C_+$ and $C_-$ have identical toponomes. But adding two coincident copies of $C_+$ gives arc weights $2$, with

$$
T_{2C_+}^{\mathrm{vert}}=1+8(1)+16(2)+8(1^2)+32(3)
$$

Each $k$-arc forest gains factor $2^k$. The input toponomes are the same as for the opposite pair, but the outputs differ. This illustrates the [[The Second-Kind Algebra on Partitions#Scope of application to toponomes|scope limitation of type algebra]]: numerical types forget intersections of labelled components.

## Passing to the Laplacian polynomial

Substitute $x_j=t^j$ in vertex normalization to obtain

$$
P_G(t)=T_G^{\mathrm{vert}}(\mathbf x)\big|_{x_j=t^j}
=\sum_{k=0}^{n-1}p_kt^k,
\qquad
p_k=\sum_{F\in\mathcal F_k^{\to}(G)}w(F)
$$

Equivalently, substitute $x_j=(j+1)t^j$ into the vector toponome, as in the [[Vector and Vertex Normalizations of Toponomes#One-variable toponomes|earlier definition]].

> [!info] Directed matrix-forest theorem
> **Theorem.** For the outgoing Laplacian,
>
> $$
> \boxed{
> P_G(t)=\det(\mathbf I+t\mathbf L),
> \qquad
> p_k=\sum_{\substack{I\subseteq\{1,\ldots,n\}\\|I|=k}}
> \det\mathbf L[I,I]
> }
> \tag{3}
> $$
>
> The matrix identity and forest interpretation also hold without balance.

> [!note]- Proof through principal minors
> **Proof.** Fix the set $I$ of nonroot vertices. Expand $\det\mathbf L[I,I]$ by multilinearity in rows, selecting one arc $i\to j$ with factor $f_{ij}$ from each $i\in I$.
>
> A directed cycle makes the corresponding row differences dependent, giving zero. Otherwise, every walk from $I$ ends in its complement, where no outgoing arcs were selected. The result is a forest with exactly one root per component and root set equal to the complement of $I$. Ordering vertices by distance to roots makes the selected-row determinant $1$. Thus the minor is the sum of these forest weights.
>
> Every rooted $k$-arc forest has a unique set of $k$ nonroots, so summing minors counts it once. Finally, for any square matrix,
>
> $$
> \det(\mathbf I+t\mathbf L)=\sum_I t^{|I|}\det\mathbf L[I,I]
> $$
>
> The full minor vanishes because $\mathbf L\mathbf1=0$. This proves (3). $\square$

Equation (3) is the known directed matrix-forest theorem [1, Theorems 3 and 3′]. It extends the [[Forest Coefficients and the Laplacian Polynomial#Summing minors and the Laplacian polynomial|toponome-determinant correspondence]] to nonsymmetric Laplacians.

### Direct contraction of the exponential

The polynomial can also be obtained without grouping by types. In the original vertex basis, put $a_I=a_{i_1}\cdots a_{i_k}$ with increasing indices. The [[The Laplacian Exponential of a Balanced Graph#Grade components and minors|minor formula]] becomes

$$
M_k=\sum_{|I|=|J|=k}\det\mathbf L[I,J]\,[a_I,a_J]
$$

The sum of coefficients of $[a_I]^2$ is therefore $p_k$. This auxiliary coordinate contraction is not a resistance-norm evaluation of vertices. In particular, it cannot be replaced by simply summing principal minors of a reduced Laplacian in a boundary basis; that basis change requires its coordinate metric.

> [!note]- Why each centroid forest term contributes one
> **Proof.** For this contraction only, introduce the auxiliary coordinate product $\langle a_i,a_j\rangle_0=\delta_{ij}$. On $[u_1\cdots u_k,v_1\cdots v_k]$, the sum of diagonal coefficients is $\det(\langle u_s,v_t\rangle_0)$. At the centroid,
>
> $$
> \langle a_i-h,a_p-a_q\rangle_0=\delta_{ip}-\delta_{iq}
> $$
>
> In a forest term, $i$ ranges over nonroots and $(p,q)$ over selected arcs. This gives the reduced forest incidence matrix with sources and arcs ordered consistently. Its determinant is $1$: ordering by distance to roots makes it triangular with unit diagonal. Hence $w(F)[A_F(h),B_F]$ contributes exactly $w(F)$, reconciling the contraction with (1) and (3). $\square$

### Coefficients and complex roots

For a connected balanced graph, the highest coefficient is

$$
p_{n-1}=n\tau
$$

The common spanning-tree coefficient is $\tau$: the order-$(n-1)$ principal-minor sum has $n$ equal terms. The first coefficients are $p_0=1$ and $p_1=\operatorname{tr}\mathbf L=\sum_i d_i^{\mathrm{out}}$.

The directed-cycle and symmetric-square examples give

$$
\begin{aligned}
P_{C_3^{\to}}(t)&=1+3t+3t^2\\
P_{C_4^{\to}}(t)&=1+4t+6t^2+4t^3\\
P_{C_4}(t)&=1+8t+20t^2+16t^3=(1+2t)^2(1+4t)
\end{aligned}
$$

The characteristic-polynomial relation survives:

$$
\chi_{\mathbf L}(x)=x^nP_G(-1/x)
$$

The identity is polynomial after expansion. The [[Forest Coefficients and the Laplacian Polynomial#Roots and factorization over the reals|symmetric theory's]] negative-real-root statement does not extend: already $1+3t+3t^2$ has negative discriminant. For known $n$, the polynomial still retains eigenvalues with algebraic multiplicities, but not eigenvectors or Jordan structure.

Reversing every arc of a balanced graph transposes its Laplacian, preserving $P_G(t)$. Without a separate proof, this polynomial property cannot be extended to every coefficient of the partition toponome.

## What is constructed and what remains open

Equations (1)-(2) define the toponome of a specified forest representation. Its types retain component sizes but forget vertex labels, root locations, and the two exterior form arguments. It agrees with the previous symmetric construction, and its vertex polynomial agrees with the determinant.

Representation dependence already occurs for quadratic forms, as discussed in [[Toponomes and Structural Identities]]. A bilinear type symbol cannot automatically be treated as the quadratic form of that type. Similarly, the product $*$ in [[The Second-Kind Algebra on Partitions]] remains a defined abstract operation, but not a universal rule for the toponome of a sum of balanced graphs.

For graphs on disjoint vertex sets, ordinary multiplication of type polynomials retains its meaning:

$$
T_{G\sqcup H}^{\mathrm{vert}}(\mathbf x)
=T_G^{\mathrm{vert}}(\mathbf x)T_H^{\mathrm{vert}}(\mathbf x)
$$

The vector normalization obeys the same rule: a union forest splits uniquely into two forests, while weights and products of component sizes multiply. This extends the [[Vector and Vertex Normalizations of Toponomes#Disjoint union and multiplication|disjoint-union lemma]]. Opposite cycles use a common vertex set and do not satisfy its assumptions.

Constructing richer types that retain roots and form arguments, with compatible multiplication, remains open. The present toponome definition neither solves this question nor requires prior symmetrization.

## Checks and sources

The 3-cycle, 4-cycle, and opposite-pair tables were checked by direct arc-subset enumeration. Weighted examples separately compared forest sums, principal minors, and diagonal coefficients of the polyform exponential. Independent enumeration of undirected forests checked the symmetric limit. Calculations used exact rational arithmetic.

“Toponome” and the two extended normalizations have the PMG meanings defined here. The directed matrix-forest theorem is an established result. The note also draws on the author's PMG research.

1. Chebotarev, P.; Agaev, R. [Forest matrices around the Laplacian matrix](https://arxiv.org/abs/math/0508178). *Linear Algebra and its Applications*, 356 (2002), 253-274. [DOI: 10.1016/S0024-3795(02)00388-9](https://doi.org/10.1016/S0024-3795(02)00388-9). In the [preprint](https://arxiv.org/pdf/math/0508178), §4, Theorems 3 and 3′ relate $\det(\mathbf I+t\mathbf L)$ to directed rooted-forest weights.

Connections to the toponome series:

- [[From Polyforms to Partitions]]: positive types and the toponome of a chosen representation.
- [[Toponomes and Structural Identities]]: criteria for representation-independent reduction.
- [[The Second-Kind Algebra on Partitions]]: the product $*$ and its applicability to particular forms.
- [[Vector and Vertex Normalizations of Toponomes]]: root factors and normalization changes.
- [[Forest Coefficients and the Laplacian Polynomial]]: minors, forests, and symmetric spectral interpretation.
