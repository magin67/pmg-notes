---
title: The Distance Operator and KVP Decomposition
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: distance-operator-kvp-decomposition
lang: en
order: 4
description: "The distance transformation and double centering, their action on KVP and KVPO, the distinction between matrix and pair components, and U-V mixing without balance."
---

The distance operator is already defined in [[Laplacian, Green Matrix, and Effective Resistance Matrix#From the Green matrix to resistances|the introductory note on matrix transformations]]. Here that definition is connected with KVP decomposition, extended to oriented tables, and used to compare components before and after the transformation.

The main distinction concerns the objects being compared. The distance operator itself takes a matrix with a diagonal to a pair table with zero diagonal. The multipliers $2n,n,2,2$ arise for the composition that first builds a Laplacian from pair coefficients and then applies the distance operator.

Components and projectors are defined in [[KVP Decomposition of Pair Characteristics]] and [[Oriented Extensions of KVP - Circulation and Imbalance]]. All matrices are real and refer to the same fixed set of $n\ge3$ vertices.

## Definition and geometric meaning

> [!info] The distance operator
> For a symmetric matrix $A$, the distance operator is
>
> $$
> \boxed{\mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}}
> \tag{1}
> $$

If $G=(g_{ij})$ is the Gram matrix of vectors $x_i$, then

$$
\mathcal D(G)_{ij}
=(x_i-x_j)\cdot(x_i-x_j)
$$

This is the quadratic norm of the difference; in Euclidean geometry, it is the squared distance. In particular, for a connected undirected graph,

$$
R=\mathcal D(\mathrm{Gr}),\qquad \mathrm{Gr}=L^+
$$

Here $\mathrm{Gr}$ denotes the Green matrix and $G$ a Gram matrix. Formula (1) is linear in $A$ and is not matrix inversion.

For an arbitrary symmetric $A$, it remains an algebraic definition. A Euclidean interpretation requires the centered Gram matrix to be positive semidefinite; signed coefficients alone do not ensure this.

> [!info] Definition and geometric meaning
> **Definition.** Extend the operator to nonsymmetric matrices using the same formula (1). The result has zero diagonal but may be nonsymmetric. It is an oriented pair table, not an ordinary table of squared distances.

If $A=S+H$, with $S^{\mathsf T}=S$ and $H^{\mathsf T}=-H$, then

$$
\mathcal D(A)=\mathcal D(S)-2H
$$

The ordinary quadratic evaluation of a difference uses $A_{ii}+A_{jj}-A_{ij}-A_{ji}$ and therefore sees only $S$. The oriented extension also retains skew-symmetric data.

## Three objects and two successive transformations

For a pair table $C$ with zero diagonal, set

$$
A=\mathscr L(C)=\operatorname{diag}(C\mathbf1)-C,\qquad
Q=\mathcal D(A)
$$

In the graph interpretation, $C$ is the coupling table and $A$ the Laplacian matrix. Signed $C$ are also admissible in the linear formulas.

| Object | Diagonal | Entries for $i\ne j$ |
|---|---|---|
| Pair coefficients $C$ | Zero | $C_{ij}$ |
| Matrix $A=\mathscr L(C)$ | $A_{ii}=d_i^{out}$ | $A_{ij}=-C_{ij}$ |
| Distance table $Q$ | Zero | $Q_{ij}=d_i^{out}+d_j^{out}+2C_{ij}$ |

Here $d^{out}=C\mathbf1$ and $d^{in}=C^{\mathsf T}\mathbf1$. Hence

$$
A\mathbf1=0,\qquad
A^{\mathsf T}\mathbf1=d^{out}-d^{in}
$$

> [!info] Three objects and two successive transformations
> **Lemma.** The map $\mathscr L$ is an isomorphism between balanced pair tables and doubly centered matrices
>
> $$
> \mathcal Z_n=\{A:A\mathbf1=A^{\mathsf T}\mathbf1=0\}
> $$

> [!note]- Proof
> **Proof.** Balance means $d^{out}=d^{in}$, so both sums of $A$ vanish. Conversely, for a centered $A$, set $C_{ij}=-A_{ij}$ for $i\ne j$ and $C_{ii}=0$. Zero row and column sums of $A$ give $d_i^{out}=d_i^{in}=A_{ii}$ and $\mathscr L(C)=A$. $\square$

In the symmetric case, this gives an isomorphism between symmetric pair tables and symmetric centered matrices. All these statements refer to a fixed vertex set.

## Centering and the inverse distance transformation

Set

$$
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

For any $A$, including nonsymmetric matrices, and the column vector $q_i=A_{ii}$,

$$
\mathcal D(A)=q\mathbf1^{\mathsf T}+\mathbf1q^{\mathsf T}-2A
$$

Since $J\mathbf1=0$, it follows that

$$
\boxed{-\frac12J\mathcal D(A)J=JAJ}
\tag{2}
$$

On the full matrix space, recovery of $A$ is not unique. Indeed, the kernel consists exactly of the matrices

$$
\ker\mathcal D=
\left\{\frac12(w\mathbf1^{\mathsf T}+\mathbf1w^{\mathsf T}):w\in\mathbb R^n\right\}
$$

The condition $\mathcal D(A)=0$ is equivalent to $A_{ij}=(A_{ii}+A_{jj})/2$, proving this expression with $w_i=A_{ii}$. For a symmetric Gram matrix, the ambiguity reflects the choice of origin; centering selects the representative relative to the centroid.

> [!info] Centering and the inverse distance transformation
> **Theorem.** The distance operator is a linear isomorphism between $\mathcal Z_n$ and balanced pair tables with zero diagonal. Its inverse is
>
> $$
> \boxed{A=-\frac12JQJ}
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** Let $A$ be doubly centered and $Q=\mathcal D(A)$. Then
>
> $$
> Q\mathbf1=Q^{\mathsf T}\mathbf1=nq+(\operatorname{tr}A)\mathbf1
> $$
>
> Thus $Q$ is balanced. Formula (2) recovers $A$ because $JAJ=A$.
>
> Conversely, let $Q$ be balanced with $Q_{ii}=0$. Denote its coinciding row and corresponding column means, and its overall mean, by
>
> $$
> \bar Q_i=\frac1n\sum_jQ_{ij}=\frac1n\sum_jQ_{ji},\qquad
> \bar Q=\frac1{n^2}\sum_{i,j}Q_{ij}
> $$
>
> Double centering gives
>
> $$
> A_{ij}=\frac{\bar Q_i+\bar Q_j-Q_{ij}-\bar Q}{2},\qquad
> A_{ii}=\bar Q_i-\frac{\bar Q}{2}
> $$
>
> The matrix $A$ is centered by construction. Substituting into (1) recovers $Q_{ij}$, proving invertibility. $\square$

Both spaces have dimension $(n-1)^2$. Restricting to symmetric matrices gives the isomorphism between spaces of dimension $\binom n2$ familiar from the introductory series.

> [!info] Centering and the inverse distance transformation
> **Corollary.** A symmetric zero-diagonal $Q$ is a table of squared Euclidean distances if and only if $-JQJ/2$ is positive semidefinite. In one direction, this is the centered Gram matrix of the original points; in the other, represent the positive semidefinite matrix as a Gram matrix and apply the inverse transformation just proved. Linear invertibility in (3) itself requires no positivity.

## Action on KVP and KVPO

To compare pair tables with pair tables, introduce

$$
\boxed{\mathcal F=\mathcal D\circ\mathscr L}
\tag{4}
$$

For symmetric $C$, this is an operator on KVP space; for balanced oriented $C$, it acts on KVPO space.

> [!info] Action on KVP and KVPO
> **Theorem.** On balanced pair tables,
>
> $$
> \boxed{\mathcal F=2n\Pi_K+n\Pi_V+2\Pi_P+2\Pi_O}
> \tag{5}
> $$
>
> For symmetric tables, O is absent.

> [!note]- Proof
> **Proof.** Under balance, write
>
> $$
> C_{ij}=\mu+\frac{v_i+v_j}{n-2}+p_{ij}+o_{ij},\qquad
> d_i^{out}=(n-1)\mu+v_i
> $$
>
> Here $\sum_i v_i=0$, and P and O have zero row sums. For distinct i and j, directly applying the two operators gives
>
> $$
> \begin{aligned}
> Q_{ij}
> &=d_i^{out}+d_j^{out}+2C_{ij}\\
> &=2n\mu+\frac{n}{n-2}(v_i+v_j)+2p_{ij}+2o_{ij}
> \end{aligned}
> $$
>
> The four terms belong to their respective sectors. Uniqueness of KVPO decomposition proves (5). $\square$

Thus

$$
Q_K=2nC_K,\qquad
Q_V=nC_V,\qquad
Q_P=2C_P,\qquad
Q_O=2C_O
$$

In particular, $\mu_Q=2n\mu_C$ and $v^{(Q)}=nv^{(C)}$. Balance does not eliminate V: it allows V to transform separately, without mixing with other sectors.

### What happens to the matrix components themselves

For $A=\mathscr L(C)$, define the **transported matrix components**

$$
A_X=\mathscr L(C_X),\qquad
\widetilde\Pi_X=\mathscr L\Pi_X\mathscr L^{-1},
\qquad X\in\{K,V,P,O\}
$$

This defines sectors of centered matrices through the previously defined pair sectors. It does not mean applying zero-diagonal table projectors directly to $A$ with its diagonal.

| Sector | Matrix component $A_X$ | Its distance image |
|---|---|---|
| K | $n\mu J$ | Constant entries $2n\mu$ for $i\ne j$ |
| V | $\operatorname{diag}(v)-C_V$ | $nC_V$ |
| P | $-C_P$ | $-2A_P=2C_P$ |
| O | $-C_O$ | $-2A_O=2C_O$ |

The correct relation between projectors is therefore

$$
\Pi_X\mathcal D(A)=\mathcal D(\widetilde\Pi_XA)
$$

The equalities $Q_K=2nA_K$ and $Q_V=nA_V$ generally fail: the $Q$-components have zero diagonal, whereas the corresponding $A$-components may have nonzero diagonal. The signs $-2$ and $+2$ in the P and O rows reflect the change of representation.

A short check clarifies the multipliers. The output $\mathcal D(A)$ always has zero diagonal, so on the entire matrix space,

$$
\boxed{\mathcal D(\mathcal D(A))=-2\mathcal D(A)}
$$

Thus $2n,n,2,2$ are multipliers of the composition $\mathcal F$, not eigenvalues of $\mathcal D$ itself on all matrices.

### The inverse transformation by components

Formula (5) and the projector identities imply

$$
\mathcal F^{-1}
=\frac1{2n}\Pi_K+\frac1n\Pi_V+\frac12\Pi_P+\frac12\Pi_O
$$

Consequently, for balanced $Q$,

$$
\boxed{-\frac12JQJ
=\mathscr L\left(\frac{Q_K}{2n}+\frac{Q_V}{n}
+\frac{Q_P}{2}+\frac{Q_O}{2}\right)}
\tag{6}
$$

These are two ways to recover the same centered matrix: double centering, or division of the pair components by their multipliers.

## What changes without balance

For arbitrary oriented $C$, set

$$
u=\frac{d^{out}-d^{in}}2,\qquad
V(u)_{ij}=\frac{u_i+u_j}{n-2}\quad(i\ne j),\qquad V(u)_{ii}=0
$$

The notation $V(u)$ means the symmetric V-table constructed from the imbalance vector u. It differs from the original component $C_V=V(v)$.

> [!info] What changes without balance
> **Theorem.** For $Q=\mathcal F(C)$ on the entire KVPOU space,
>
> $$
> \boxed{
> \begin{aligned}
> Q_K&=2nC_K\\
> Q_V&=nC_V+(n-2)V(u)\\
> Q_P&=2C_P\\
> Q_O&=2C_O\\
> Q_U&=2C_U
> \end{aligned}}
> \tag{7}
> $$

> [!note]- Proof
> **Proof.** Now $d^{out}=(n-1)\mu\mathbf1+v+u$. Substitute this expression and the KVPOU decomposition of $C$ into $Q_{ij}=d_i^{out}+d_j^{out}+2C_{ij}$. In addition to the terms in (5), we obtain $2(C_U)_{ij}$ and the symmetric contribution $u_i+u_j=(n-2)V(u)_{ij}$. Uniqueness of the decomposition gives (7). $\square$

A pure U-component therefore produces two parts:

$$
\mathcal F(C_U)=2C_U+(n-2)V(u)
$$

The reason for mixing is also visible in matrix form: $\mathscr L(C_U)=\operatorname{diag}(u)-C_U$. Its diagonal contains u and produces the symmetric sums $u_i+u_j$ under the distance transformation.

The composition $\mathcal F$ remains invertible. First recover $C_U=Q_U/2$ and u from $Q_U$; then subtract $(n-2)V(u)$ from $Q_V$ and divide the remainder by n. The other components are recovered by division by the multipliers in (7).

### Exactly what double centering loses

> [!info] Exactly what double centering loses
> **Lemma.** For every zero-diagonal $Q$,
>
> $$
> \boxed{\mathcal D\left(-\frac12JQJ\right)=Q-Q_U}
> \tag{8}
> $$

> [!note]- Proof
> **Proof.** The inverse transformation theorem recovers the balanced part $Q-Q_U$. For the gradient table $Q_U=(u^{(Q)}\mathbf1^{\mathsf T}-\mathbf1(u^{(Q)})^{\mathsf T})/n$, we have $JQ_UJ=0$. Double centering therefore retains only the balanced part. $\square$

The balance assumption in (3) is essential. If $Q$ comes from an unbalanced $C$, then $-JQJ/2$ equals $J\mathscr L(C)J$, not the original Laplacian.

Nevertheless, $A$ can be recovered from $Q$ if only the **row** sums are required to vanish. For an arbitrary zero-diagonal $Q$, let $\bar Q_i$ be its row means and $\bar Q$ its overall mean. The unique matrix with $A\mathbf1=0$ and $\mathcal D(A)=Q$ is

$$
A_{ij}=\frac{\bar Q_i+\bar Q_j-Q_{ij}-\bar Q}{2}
$$

Indeed, if $q_i=A_{ii}$ and $t=\operatorname{tr}A$, then $\sum_jQ_{ij}=nq_i+t$. Summation gives $t=n\bar Q/2$, hence $q_i=\bar Q_i-\bar Q/2$, and (1) determines the formula for $A$. Direct substitution verifies zero row sums.

Without balance, this is **not** double centering: row means are used for both indices. If $u^{(Q)}=(Q\mathbf1-Q^{\mathsf T}\mathbf1)/2$, the difference is explicit:

$$
A=-\frac12JQJ+\frac1n\mathbf1(u^{(Q)})^{\mathsf T}
$$

Under balance, the additional term vanishes.

## Example: a path on four vertices

For the unit-weight path $a-b-c-d$, set $L=\mathscr L(C)$. Then

$$
L=\begin{pmatrix}
1&-1&0&0\\
-1&2&-1&0\\
0&-1&2&-1\\
0&0&-1&1
\end{pmatrix},\qquad
Q=\mathcal D(L)=
\begin{pmatrix}
0&5&3&2\\
5&0&6&3\\
3&6&0&5\\
2&3&5&0
\end{pmatrix}
$$

![[Distance transformation for path P4.svg]]

*Left: the original path's couplings. Center: its Laplacian. Right: pair values $Q$. The right panel shows distance-table values, not couplings of a new resistive network. For example, $Q$ equals 2 on the absent coupling $ad$ and 5 on the existing coupling $ab$.*

For the original couplings,

$$
\mu_C=\frac12,\qquad
v^{(C)}=\left(-\frac12,\frac12,\frac12,-\frac12\right)
$$

The directly computed $Q$ has row sums $(10,14,14,10)$. Thus

$$
\mu_Q=4,\qquad v^{(Q)}=(-2,2,2,-2)
$$

Decomposing $Q$ independently from these sums gives

| Component | Values for $C$ | Values for $Q$ | Multiplier |
|---|---|---|---:|
| K: $\mu$ | $1/2$ | $4$ | $8$ |
| V: $v$ | $(-1/2,1/2,1/2,-1/2)$ | $(-2,2,2,-2)$ | $4$ |
| P: pair coefficients | $(1/2,-1/2,0,0,-1/2,1/2)$ | $(1,-1,0,0,-1,1)$ | $2$ |

In the P row, pairs are ordered as $ab,ac,ad,bc,bd,cd$. For example, $Q_{ad}=4-2+0=2$, while $Q_{ab}=4+0+1=5$.

The row means of $Q$ are $(5/2,7/2,7/2,5/2)$, and the overall mean is 3. Formula (3) recovers the diagonal $(1,2,2,1)$ and all off-diagonal entries of $L$. The original path's decomposition is worked out in [[KVP on Simple and Weighted Graphs#The path: all three components]].

## Example: the unit directed 3-cycle

For $a\to b\to c\to a$,

$$
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\qquad
L=I-C,\qquad
Q=\begin{pmatrix}0&4&2\\2&0&4\\4&2&0\end{pmatrix}
$$

The table $C$ contains only K and O: a constant symmetric background of $1/2$ and a circulation of weight $1/2$ along the traversal. In $Q$, the background is 3 and the circulation weight is 1. Therefore

$$
Q_K=6C_K,\qquad Q_O=2C_O
$$

The row and column sums of $Q$ equal 6. Double centering recovers $L$. Orientation is retained: the values 4 and 2 distinguish the directions of a pair, so $Q$ cannot be interpreted as an ordinary symmetric table of squared distances.

## Example: a nonregular balanced graph

Take the unit directed 3-cycle $a\to b\to c\to a$ and add unit-weight arcs $a\to d$, $d\to a$. Its full KVPO decomposition appears in [[Oriented Extensions of KVP - Circulation and Imbalance#A balanced graph with unequal degrees: all four KVPO components]].

Here $d^{out}=d^{in}=(2,1,1,1)$. Direct calculation gives

$$
C=\begin{pmatrix}
0&1&0&1\\0&0&1&0\\1&0&0&0\\1&0&0&0
\end{pmatrix},\qquad
Q=\begin{pmatrix}
0&5&3&5\\3&0&4&2\\5&2&0&2\\5&2&2&0
\end{pmatrix}
$$

The incoming and outgoing sums of $Q$ coincide and equal $(13,9,9,9)$. Hence

$$
\mu_Q=\frac{10}3=8\mu_C,\qquad
v^{(Q)}=(3,-1,-1,-1)=4v^{(C)}
$$

The skew-symmetric part of $Q$ is a unit circulation around $abc$, so $Q_O=2C_O$. After subtracting K, V, and O, the P-residual on pairs $ab,ac,ad,bc,bd,cd$ is

$$
\left(-\frac13,-\frac13,\frac23,\frac23,-\frac13,-\frac13\right)
$$

This is twice the P-component of the original table. Thus a single balanced graph with nonzero V checks all four multipliers.

## Example: one arc and mixing of U with V

On three vertices, retain only the unit-weight arc $a\to b$. Then

$$
C=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
L=\begin{pmatrix}1&-1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}0&3&1\\1&0&0\\1&0&0\end{pmatrix}
$$

For $C$, we know

$$
v^{(C)}=\left(\frac16,\frac16,-\frac13\right),\qquad
u^{(C)}=\left(\frac12,-\frac12,0\right)
$$

Direct decomposition of $Q$ gives $\mu_Q=1$ and

$$
v^{(Q)}=(1,0,-1),\qquad u^{(Q)}=(1,-1,0)
$$

The vertex parameters satisfy (7):

$$
\begin{aligned}
v^{(Q)}&=3v^{(C)}+u^{(C)}\\
&=\left(\frac12,\frac12,-1\right)+\left(\frac12,-\frac12,0\right)\\
&=(1,0,-1)
\end{aligned}
$$

Thus $Q_V$ is not $3C_V$: U contributed an additional V-term.

The row sums of $Q$ are $(4,1,1)$ and its column sums are $(2,3,1)$, so $Q$ is unbalanced. Double centering gives

$$
-\frac12JQJ
=\begin{pmatrix}
2/3&-2/3&0\\
-1/3&1/3&0\\
-1/3&1/3&0
\end{pmatrix}
=JLJ\ne L
$$

Adding $\mathbf1(u^{(Q)})^{\mathsf T}/3$ recovers $L$. This explicitly checks why the double-centering formula cannot be applied unchanged to the unbalanced case.

## The Laplacian and Green matrix give different pair tables

For a connected undirected graph with nonnegative couplings and positive weights on existing edges, both $L$ and $\mathrm{Gr}=L^+$ are symmetric, centered, and positive semidefinite. The same operator gives

$$
Q=\mathcal D(L),\qquad R=\mathcal D(\mathrm{Gr})
$$

Both tables admit Euclidean interpretations, but they correspond to different Gram matrices. R contains effective resistances. For the unit-weight path $P_4$, for example, $Q_{ab}=5$ while $R_{ab}=1$.

To apply the component formula to R, use the pair coefficients of the **Green matrix**:

$$
\gamma_{ij}=-\mathrm{Gr}_{ij}\quad(i\ne j),\qquad
\gamma_{ii}=0,\qquad
\mathrm{Gr}=\mathscr L(\gamma)
$$

Then

$$
R_K=2n\gamma_K,\qquad
R_V=n\gamma_V,\qquad
R_P=2\gamma_P
$$

These equalities do not relate R directly to the components of the original couplings $C$. Between $C$ and $\gamma$ lies the nonlinear pseudoinversion $L\mapsto L^+$. Component properties do not pass through it automatically.

In the balanced case, $\mathcal D(\mathrm{Gr})$ is also defined as an oriented table, but it must not be identified with the one-way resistance table $r_{ij}$ without checking normalizations. The precise correspondence between these tables, their components, and their normalizations is given in [[KVP Decomposition of the Green Matrix and Resistances]].

## Status of results and connections

Invertibility, the action on components, and U-V mixing are proved in the text. Numerical examples were checked by constructing $Q=\mathcal D(\mathscr L(C))$ directly, decomposing $Q$ independently from its row and column sums, and recovering the original matrix.

The distance operator, centering, and the connection with effective resistance are introduced in [[Laplacian, Green Matrix, and Effective Resistance Matrix]]. Projectors and coefficient orthogonality are defined in [[KVP Decomposition of Pair Characteristics]] and [[Oriented Extensions of KVP - Circulation and Imbalance]]. That orthogonality concerns the coefficient inner product and does not replace the PMG metric inner product.

This note establishes linear transformations between chosen representations. [[KVP Decomposition of the Green Matrix and Resistances]] continues the analysis, accounting for nonlinear Laplacian inversion and the differences between symmetric, one-way, and balanced resistance tables.

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
