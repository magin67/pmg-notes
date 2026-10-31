---
title: The Second-Order Symmetric Potential and KVP Decomposition
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: second-order-symmetric-potential-and-kvp
lang: en
order: 8
description: "Definition of the second-order symmetric potential, its connection with the tetrahedron identity, the general KVP formula, geometric constraints, and examples. A circulation correction for balanced graphs."
---

The second-order symmetric potential is obtained by summing the potentials of the boundaries of all vertex triples. In a symmetric resistance metric, its normalized value is the sum of the norms of those boundaries, or four times the sum of squared triangle areas. As a function of pair resistances, it is a quadratic form whose eigenspaces are the K-, V-, and P-sectors.

Studying this quadratic form originally led to KVP decomposition within PMG. Here the reverse exposition derives a formula for any number of vertices from the already defined projectors. On four vertices, there is another derivation through [[Partition Forms and the Tetrahedron Identity|the tetrahedron identity]], which relates triangle boundaries to products of opposite edges.

## Scope and underlying objects

Until the section on balanced graphs, consider a connected loopless undirected graph on $n\ge3$ vertices with nonnegative conductances $c_{ij}$. Its metric polyform is $M=\exp L$, and its spanning-tree coefficient $\tau=\tau(M)$ is positive. The exponential here is the polyform exponential, as in [[Laplacian Exponential]], not the matrix exponential.

Use [[Core specification#Potential and the metric identity|the form potential and its normalization]]:

$$
u_M(F)=\tau(MF),\qquad
P_M(F)=\frac{u_M(F)}\tau
$$

For boundaries, the metric identity is $P_M([X,Y])=X\cdot Y$. On exterior products, the inner product is computed by the Gram determinant, as explained in [[Metric of Higher-Grade Objects]]. In particular,

$$
R_{ij}=P_M([(ij)]^2)=(ij)^2
$$

In PMG, a norm is a quadratic quantity. Thus $R_{ij}$ corresponds to squared Euclidean distance, and the linear distance is $\sqrt{R_{ij}}$.

Below, KVP decomposition is applied to the symmetric **resistance table R**, including pairs without an edge. It is not a decomposition of the conductance table C or the Green matrix. Transformations between these objects are discussed in [[KVP Decomposition of the Green Matrix and Resistances]]. The algebraic formulas for $H_n$ also hold for any real symmetric zero-diagonal table R, without assuming metric realizability.

## Definition and the meaning of second order

> [!info] Definition and the meaning of second order
> **Definition.** Let $A=\{a_1,\ldots,a_n\}$ be the vertex set. With the normalization of [[Symmetric Polyforms - Types and Normalizations|principal symmetric polyforms]], for $1\le k\le n-1$ set
>
> $$
> E_n[k]=\sum_{\substack{B\subseteq A\\\#B=k+1}}[(B)]^2,\qquad
> U_k=u_M(E_n[k]),\qquad \nu_k=P_M(E_n[k])=\frac{U_k}\tau
> $$

Each subset is counted once. Order $k$ is the boundary grade: second order concerns vertex triples and two independent vectors. It must not be confused with [[Partitions and the Combinatorial Potential of the Second Kind|the combinatorial potential of the second kind]].

For a triple $i,j,k$, we have $(ijk)=(ij)(ik)$. Polarization gives

$$
(ij)\cdot(ik)=\frac{R_{ij}+R_{ik}-R_{jk}}2
$$

The normalized potential of its boundary is therefore

$$
\begin{aligned}
h_{ijk}(R)&=P_M([(ijk)]^2)\\
&=R_{ij}R_{ik}-\frac14(R_{ij}+R_{ik}-R_{jk})^2
\end{aligned}
\tag{1}
$$

This is the Gram determinant of vectors $(ij),(ik)$. In the symmetric metric, $h_{ijk}=4A_{ijk}^2$, where $A_{ijk}$ is the ordinary triangle area. An expression symmetric in all three arguments is

$$
h_{ijk}(R)=\frac14\left(2R_{ij}R_{ik}+2R_{ij}R_{jk}+2R_{ik}R_{jk}-R_{ij}^2-R_{ik}^2-R_{jk}^2\right)
$$

> [!info] Definition and the meaning of second order
> **Definition.** For any symmetric pair table, set
>
> $$
> \boxed{H_n(R)=\sum_{i<j<k}h_{ijk}(R)}
> \tag{2}
> $$

For the resistance table of the graph under consideration,

$$
\boxed{\nu_2=H_n(R),\qquad U_2=\tau H_n(R)}
\tag{3}
$$

If the data are unnormalized edge potentials $w_{ij}=u_M([(ij)]^2)=\tau R_{ij}$ rather than resistances, degree-two homogeneity gives $U_2=H_n(w)/\tau$. Substituting w for R without adjusting the normalization is incorrect.

### Why second order

The normalized first-order potential equals the Kirchhoff index:

$$
\nu_1=\sum_{i<j}R_{ij}=\operatorname{Kf}
$$

The V- and P-components have zero coefficient sums, so $\nu_1$ sees only the K-component of resistances. This agrees with [[KVP Components and Metric Graph Parameters|the KVP analysis of metric parameters]].

Second order gives the first nonlinear dependence on R: a quadratic form. For $n\ge4$, it responds to the magnitudes of all three components, although one scalar value clearly cannot recover the whole table. For $n=3$, the P-sector is zero. For orders $k\ge3$, determinant expressions have degree k in resistances; coefficient orthogonality alone does not eliminate mixed terms in these polynomials.

## The tetrahedron identity and four vertices

On four vertices $a,b,c,d$, [[Partition Forms and the Tetrahedron Identity#The tetrahedron identity|the structural identity]] states

$$
E_4[2,0]=E_4[1,1]
$$

The left side contains the four triangle-boundary forms; the right side contains the three forms $[(ab)(cd)]^2$, $[(ac)(bd)]^2$, and $[(ad)(bc)]^2$. The equality holds before choosing a metric. Linearity of metric evaluation allows either side to be evaluated.

Write

$$
\pi_1=(ab)\cdot(cd),\qquad
\pi_2=(ac)\cdot(bd),\qquad
\pi_3=(ad)\cdot(bc)
$$

By the determinant rule, $P_M([(ab)(cd)]^2)=R_{ab}R_{cd}-\pi_1^2$. Hence

$$
\boxed{H_4(R)=R_{ab}R_{cd}+R_{ac}R_{bd}+R_{ad}R_{bc}-\sum_{\alpha=1}^3\pi_\alpha^2}
\tag{4}
$$

Evaluation of a product of forms is not the product of their numerical evaluations: the terms $-\pi_\alpha^2$ are necessary.

[[KVP Decomposition of Pair Characteristics#What the P-component identifies|The description of the P-component]] shows that four-point polar values use only P. For example,

$$
\pi_1=\frac12(R_{ad}+R_{bc}-R_{ac}-R_{bd})
$$

Substituting a constant K-component or a sum of two vertex corrections from V gives zero.

> [!info] The tetrahedron identity and four vertices
> **Lemma 1.** For four vertices and the coefficient sum of squares $\|B\|_0^2=\sum_{i<j}B_{ij}^2$,
>
> $$
> \begin{aligned}
> R_{ab}R_{cd}+R_{ac}R_{bd}+R_{ad}R_{bc}
> &=\frac12\left(\|R_K\|_0^2-\|R_V\|_0^2+\|R_P\|_0^2\right)\\
> \sum_{\alpha=1}^3\pi_\alpha^2&=\frac32\|R_P\|_0^2
> \end{aligned}
> \tag{5}
> $$

> [!note]- Proof
> **Proof.** Replacing each vertex pair by its opposite preserves K- and P-tables and negates V-tables. For V, this follows from $v_a+v_b=-(v_c+v_d)$. For P, zero row sums imply equal values on opposite pairs. The coefficient inner product of a table with its image under this replacement is twice the sum of the three products in the first line of (5). KVP orthogonality gives the required formula.
>
> Let the P-values on the three pairs of opposite edges be $x,y,z$, respectively. Then $x+y+z=0$, $\|R_P\|_0^2=2(x^2+y^2+z^2)$, and the polar values are $z-y$, $z-x$, and $y-x$. Their squared sum is $3(x^2+y^2+z^2)$, proving the second line. $\square$

The tetrahedron identity and (5) give

$$
\boxed{H_4(R)=\frac12\|R_K\|_0^2-\frac12\|R_V\|_0^2-\|R_P\|_0^2}
\tag{6}
$$

Thus a structural SPF equality becomes a formula for its potential and then a KVP decomposition of a quadratic function of pair data. These are distinct levels of description. In particular, (5) means that on four vertices, $R_P=0$ is equivalent to orthogonality of each of the three opposite edge pairs.

### Summing over four-element subsets

For any $n\ge4$, summing the tetrahedron identity over all four-element subsets gives

$$
\boxed{E_n[1,1]=(n-3)E_n[2]}
\tag{7}
$$

Indeed, each pair of disjoint edges belongs to exactly one four-element subset, while each vertex triple belongs to $n-3$ such subsets. Zeros in types are omitted according to the general SPF normalization. This passage from local identities to symmetric sums is described in [[Constructing Structural Identities]].

Evaluating (7) expresses $(n-3)H_n(R)$ as the sum of Gram determinants over all unordered pairs of disjoint edges on the complete vertex set. These are vertex pairs regardless of whether the original graph contains a coupling between them.

## The general KVP formula

Recall the required decomposition data:

$$
s_i=\sum_{j\ne i}R_{ij},\qquad
\mu=\frac1{\binom n2}\sum_{i<j}R_{ij},\qquad
v_i=s_i-(n-1)\mu
$$

For $i\ne j$,

$$
(R_K)_{ij}=\mu,\qquad
(R_V)_{ij}=\frac{v_i+v_j}{n-2},\qquad
R_P=R-R_K-R_V
$$

All diagonals are zero, $\sum_i v_i=0$, and $R_P\mathbf1=0$. The projectors are denoted by $\Pi_K,\Pi_V,\Pi_P$.

> [!info] The general KVP formula
> **Lemma 2.** The quadratic form (2) can be written as
>
> $$
> H_n(R)=\frac14\left(\sum_i s_i^2-n\sum_{i<j}R_{ij}^2\right)
> \tag{8}
> $$

> [!note]- Proof
> **Proof.** In the sum over triples, each square $R_{ij}^2$ occurs $n-2$ times with coefficient $-1/4$. Each product of two pairs sharing one vertex occurs once with coefficient $1/2$. In $\sum_i s_i^2$, squares occur twice, and such products also occur twice. Subtracting $n\sum_{i<j}R_{ij}^2$ and dividing by 4 gives (8). $\square$

Let $\langle A,B\rangle_0=\sum_{i<j}A_{ij}B_{ij}$. The self-adjoint operator of this quadratic form acts on pair-table space:

$$
(\mathsf Q_nR)_{ij}=\frac{s_i+s_j-nR_{ij}}4,\qquad
H_n(R)=\langle R,\mathsf Q_nR\rangle_0
$$

It acts on a space of dimension $\binom n2$; its representing matrix has size $\binom n2\times\binom n2$, not $n\times n$. It is neither the Green matrix nor the operator of the PMG metric inner product.

> [!info] The general KVP formula
> **Theorem 1.** For any real symmetric zero-diagonal table on $n\ge3$ vertices,
>
> $$
> \mathsf Q_n=\frac{n-2}{4}\Pi_K-\frac12\Pi_V-\frac n4\Pi_P
> $$
>
> and consequently,
>
> $$
> \boxed{H_n(R)=\frac{n-2}{4}\|R_K\|_0^2-\frac12\|R_V\|_0^2-\frac n4\|R_P\|_0^2}
> \tag{9}
> $$

| Sector | Eigenvalue of $\mathsf Q_n$ | Dimension |
| --- | ---: | ---: |
| K | $(n-2)/4$ | $1$ |
| V | $-1/2$ | $n-1$ |
| P | $-n/4$ | $n(n-3)/2$ |

> [!note]- Proof
> **Proof.** For K, the row sums are $(n-1)\mu$, and the operator multiplies the table by $(n-2)/4$. For V, the row sum is $v_i$; since $v_i+v_j=(n-2)(R_V)_{ij}$, the multiplier is $-1/2$. For P, both row sums vanish, and the multiplier is $-n/4$. The three sectors are coefficient-orthogonal, so mixed terms vanish. Dimensions are established in [[KVP Decomposition of Pair Characteristics#The number of independent parameters|the KVP dimension theorem]]. $\square$

For $n\ge4$, these are three distinct eigenvalues. For $n=3$, the P-sector is zero. If $S=R_{12}+R_{13}+R_{23}$, then

$$
H_3(R)=\frac{S^2}{12}-\frac12\|R_V\|_0^2
$$

The coefficient of $S^2$ here is $1/12$ because the subtracted coefficient sum of squares is that of the V-component, not of the whole table.

The absence of mixed terms in (9) follows from the scalar action of this particular operator $\mathsf Q_n$ on the sectors. Additivity of KVP alone would not suffice for an arbitrary nonlinear characteristic. Components of R may contain negative coefficients; they need not be realized as separate positive graphs.

## The P-component as a collection of four-point responses

The connection of P with inner products of disjoint pairs has a general quantitative expression. For each four-element subset $a<b<c<d$, take the three polar values $\pi_1,\pi_2,\pi_3$ defined above and set

$$
Z_n(R)=\sum_{a<b<c<d}\left(\pi_1^2+\pi_2^2+\pi_3^2\right)
$$

Here polar values are computed from R on the corresponding four-element subset; the subset's own KVP-components are not identified with restrictions of the global components.

> [!info] The P-component as a collection of four-point responses
> **Corollary 1.** For $n\ge4$,
>
> $$
> \boxed{Z_n(R)=\frac{(n-1)(n-2)}4\|R_P\|_0^2}
> \tag{10}
> $$

> [!note]- Proof
> **Proof.** Let $S=\sum_{i<j}R_{ij}$. The sum of resistance products over all unordered pairs of disjoint edges is
>
> $$
> \frac12\left(S^2+\|R\|_0^2-\sum_i s_i^2\right)
> $$
>
> This follows by expanding $S^2$ and separating pairs sharing a vertex. Subtract $(n-3)H_n(R)$, as required by metric evaluation of (7), and apply (8):
>
> $$
> Z_n(R)=\frac12S^2-\frac{n-1}{4}\sum_i s_i^2+\frac{(n-1)(n-2)}4\|R\|_0^2
> $$
>
> Substitution of KVP and the equalities $S=\binom n2\mu$, $\sum_i s_i^2=n(n-1)^2\mu^2+\sum_i v_i^2$, and $\|R_V\|_0^2=\sum_i v_i^2/(n-2)$ cancels the K- and V-contributions, leaving (10). $\square$

Thus the coefficient magnitude of P is determined by the total intensity of all four-point polar responses. This connects the second-order potential with [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis|four-electrode measurements]]. An individual response sees only one linear combination of P; equality (10) concerns the full collection of four-element subsets.

## Geometric constraints and a fixed overall level

On the full space of pair tables, $H_n$ is indefinite: the K-direction is positive, while nonzero V- and P-directions are negative. For squared Euclidean distances, every $h_{ijk}\ge0$, so

$$
\frac12\|R_V\|_0^2+\frac n4\|R_P\|_0^2
\le\frac{n-2}{4}\|R_K\|_0^2
\tag{11}
$$

This is necessary but generally insufficient for Euclidean realizability. The complete criterion through positive semidefiniteness after double centering is given in [[The Distance Operator and KVP Decomposition]]. Negative coefficients in (9) do not imply a negative metric for the original graph.

In a Euclidean realization, $H_n=0$ exactly when all triples are degenerate, that is, the points are collinear or coincide. For a connected graph of the specified class, resistance geometry is nondegenerate on a space of dimension $n-1$, so $H_n>0$ for $n\ge3$.

> [!info] Geometric constraints and a fixed overall level
> **Corollary 2.** For fixed n and Kirchhoff index,
>
> $$
> \boxed{0<\nu_2\le\frac{n-2}{2n(n-1)}\operatorname{Kf}^2}
> \tag{12}
> $$
>
> The upper bound is attained exactly by the complete graph with equal positive conductances.

> [!note]- Proof
> **Proof.** We have $\|R_K\|_0^2=\operatorname{Kf}^2/\binom n2$, and (9) gives the bound. Equality means $R_V=R_P=0$, that is, $R_{ij}=\mu>0$ for every $i\ne j$. Then $\mathrm{Gr}=\mu J/2$, where $J=I-\mathbf1\mathbf1^{\mathsf T}/n$, and $\mathbf L=2J/\mu$. Every conductance is therefore $2/(n\mu)$. The same formula proves the converse. $\square$

This statement concerns the normalized potential $\nu_2$. For $U_2=\tau\nu_2$, changes in $\tau$ must also be considered. Moreover, changing one coupling of the original graph generally changes all components of R; formula (9) does not provide independent physical controls for K, V, and P.

## Examples on four vertices

Consider the complete graph $K_4$, cycle $a-b-c-d-a$, star with center a, and path $a-b-c-d$. The first four examples have conductance 1 on every existing coupling. In the final path, $c_{ab},c_{bc},c_{cd}$ are $1,2,3$, respectively; all other conductances are zero.

For $n=4$, denote the contributions in (6) by

$$
H_K=\frac12\|R_K\|_0^2,\qquad
H_V=-\frac12\|R_V\|_0^2,\qquad
H_P=-\|R_P\|_0^2
$$

| Graph | $H_K$ | $H_V$ | $H_P$ | $\nu_2$ | $\tau$ | $U_2$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Complete graph $K_4$ | $3/4$ | $0$ | $0$ | $3/4$ | $16$ | $12$ |
| Cycle $C_4$ | $25/12$ | $0$ | $-1/12$ | $2$ | $4$ | $8$ |
| Star $K_{1,3}$ | $27/4$ | $-3/4$ | $0$ | $6$ | $1$ | $6$ |
| Path $P_4$ | $25/3$ | $-1$ | $-4/3$ | $6$ | $1$ | $6$ |
| Path with weights $1,2,3$ | $3$ | $-2/3$ | $-1/3$ | $2$ | $6$ | $12$ |

### The complete graph, cycle, and star

For $K_4$, every resistance is $1/2$, so only K is present. Each of the four triples gives $h_{ijk}=3/16$, summing to $3/4$.

For the cycle, adjacent vertices have resistance $3/4$ and opposite vertices have resistance 1. Equal row sums give $R_V=0$, but $R_P\ne0$. Each triple gives $h_{ijk}=1/2$. This is a pure P-correction to the overall K-level.

For the star, the center-to-leaf resistance is 1 and the leaf-to-leaf resistance is 2. Here $R_P=0$, but $R_V\ne0$. The three triples containing the center contribute 1 each, and the triple of leaves contributes 3. Every opposite edge pair in the resistance tetrahedron is orthogonal, as predicted by (5).

### Unit-weight and weighted paths

For the unit-weight path, resistances equal the lengths of the unique paths:

$$
R=\begin{pmatrix}
0&1&2&3\\
1&0&1&2\\
2&1&0&1\\
3&2&1&0
\end{pmatrix}
$$

In triple order $abc,abd,acd,bcd$, the Gram determinants are $1,2,2,1$. They give $\nu_2=6$, as for the star, although the KVP-contributions differ. One scalar potential does not determine graph structure. Moreover, the resistance vertices of the path are not collinear: linear distances add along a straight line, whereas here their squares add along the path.

For the weighted path, individual edge resistances are $1,1/2,1/3$. In pair order $ab,ac,ad,bc,bd,cd$,

$$
(R_{ab},R_{ac},R_{ad},R_{bc},R_{bd},R_{cd})
=\left(1,\frac32,\frac{11}6,\frac12,\frac56,\frac13\right)
$$

The four triples give $1/2,5/6,1/2,1/6$, so $\nu_2=2$. The unique spanning tree has weight $1\cdot2\cdot3=6$, hence $U_2=12$.

### An independent check of the unnormalized potential

On four vertices, $[(abc)]^2$ has grade 2, so only grade 1 of M, namely L, contributes to $u_M([(abc)]^2)$. Exactly the couplings from d to a, b, c complete it to the spanning-tree grade. Therefore,

$$
u_M([(abc)]^2)=c_{ad}+c_{bd}+c_{cd},\qquad
\boxed{U_2=2\sum_{i<j}c_{ij}\quad(n=4)}
\tag{13}
$$

Each edge is counted twice. This gives $12,8,6,6,12$ directly from conductances, independently of KVP and the area formula.

On four vertices, $U_2$ thus depends only on the K-component of **conductances C**, whereas $\nu_2=U_2/\tau$ is expressed through all three components of **resistances R**. There is no contradiction: both the table and the normalization have changed. On three vertices it is simpler still: $E_3[2]=T_3$, so $U_2=1$ and $\nu_2=1/\tau$.

## What changes for balanced graphs

Now let the graph be connected and balanced, with nonnegative arc weights. Balance does not imply regularity and does not eliminate V. The definition $U_2=u_M(E_n[2])$ and normalization $\nu_2=U_2/\tau$ remain, where $\tau$ is the common spanning-tree coefficient of one fixed root.

By [[Resistance Geometry and Circulation#Three-vertex resistance|the determinant rule for a balanced graph]], the normalized potential of a triple is

$$
P_M([(ijk)]^2)=h_{ijk}(R)+\frac{\chi_{ijk}^2}{4}
$$

Here $R=r+r^{\mathsf T}$, $r_{ij}=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}$, and

$$
\chi_{ijk}=r_{ij}+r_{jk}+r_{ki}-r_{ik}-r_{kj}-r_{ji}
$$

Indeed, the full pairing $\beta=g+\gamma$ gives the determinant $g(u,u)g(v,v)-g(u,v)^2+\gamma(u,v)^2$ on two vectors, with $\chi=2\gamma$. Euclidean areas describe only the first term $h_{ijk}$.

> [!info] What changes for balanced graphs
> **Theorem 2.** Let $r_O$ be the O-component of the KVPOU decomposition of the one-way resistance table. Then
>
> $$
> \boxed{\nu_2=H_n(R)+n\|r_O\|_0^2}
> \tag{14}
> $$
>
> For a skew-symmetric table, use $\|A\|_0^2=\frac12\sum_{i\ne j}A_{ij}^2=\sum_{i<j}A_{ij}^2$.

> [!note]- Proof
> **Proof.** Symmetric components cancel in the circulation sum. U is a difference of vertex values and also cancels around a closed walk. Thus $\chi_{ijk}=2((r_O)_{ij}+(r_O)_{jk}+(r_O)_{ki})$. For any skew-symmetric A, expanding squares gives
>
> $$
> \sum_{i<j<k}(A_{ij}+A_{jk}+A_{ki})^2
> =n\|A\|_0^2-\sum_i\left(\sum_jA_{ij}\right)^2
> $$
>
> Each entry square occurs in $n-2$ triples; the mixed terms equal $2\|A\|_0^2-\sum_i(\sum_jA_{ij})^2$. The row sums of $r_O$ are zero, so the corrections $\chi^2/4$ sum to $n\|r_O\|_0^2$. Summing the triple potentials proves (14). $\square$

Writing all components for the single table r, we have $R_X=2r_X$ for $X=K,V,P$, so the formula becomes

$$
\nu_2=(n-2)\|r_K\|_0^2-2\|r_V\|_0^2-n\|r_P\|_0^2+n\|r_O\|_0^2
$$

For the unit directed 3-cycle, $R_{ij}=1$, $\chi_{123}=-1$, and $\|r_O\|_0^2=1/12$. Thus $\nu_2=3/4+1/4=1$, agreeing with $\tau=1$ and $U_2=1$. The undirected triangle with conductance $2/3$ on each edge has the same R but zero circulation and $\nu_2=3/4$. An identical symmetric resistance table does not determine the full potential of a balanced graph.

The structural tetrahedron identity remains valid; its metric evaluation changes. Formula (9) still computes $H_n(R)$, but it cannot be identified with $\nu_2$ without the O-correction. No such metric extension to arbitrary unbalanced digraphs is asserted here.

## Status of results and connections

The general spectral formula, its four-vertex derivation through the tetrahedron identity, the quantitative relation between P and four-point responses, and the circulation correction are proved in the text. They are not conjectures based only on small examples.

Additional checks used exact rational arithmetic: the quadratic-form operator was constructed directly from triples for $n=3,4,5,6,7$ and compared with KVP projectors. Sums over four-element subsets and all numerical examples were also checked. Gram determinants and the balanced correction were additionally compared on 15 symmetric and 15 balanced graphs with 3-7 vertices. On four vertices, unnormalized potentials were independently computed by directly completing forms to the spanning-tree grade using (13).

This note is based on the author's PMG research. The formal definitions and proofs used here are available in [[Symmetric Polyforms - Types and Normalizations]], [[Partition Forms and the Tetrahedron Identity]], [[Metric of Higher-Grade Objects]], [[KVP Decomposition of Pair Characteristics]], and [[Resistance Geometry and Circulation]].

For higher-order potentials, the question concerns the structure of polynomials in components and their mixed invariants. The related problem of mixed forest coefficients is studied in [[Forest Toponomes of KVP Components]]. There the coupling table C is decomposed; the diagonal quadratic formula (9) for resistance R does not replace a separate proof for those objects.

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
