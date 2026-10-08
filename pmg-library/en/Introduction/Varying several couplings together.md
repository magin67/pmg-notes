---
title: Varying Several Couplings Together
date: 2026-10-05
updated: 2026-10-08
revision: 2
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: joint-edge-variation
lang: en
description: Exact formulas for simultaneous conductance changes. Gram determinants as variation coefficients of the spanning-tree coefficient, edge probabilities, and criteria for preserving connectivity.
order: "7"
---

When several conductances change, their effect on resistances is determined by the same Green matrix. The interaction of the selected couplings is described by the matrix of inner products of the corresponding affine vectors. Its principal minors are coefficients in the change of the spanning-tree coefficient and squared higher-dimensional volumes.

## Problem setup

We consider a finite connected undirected graph without loops on $n\ge2$ vertices, with nonnegative conductances. Choose $m$ distinct unordered vertex pairs $e_\alpha$, assigning each an orientation from $k_\alpha$ to $l_\alpha$. A pair may be an existing edge or an absent coupling with zero conductance.

Set

$$
b_\alpha=\mathbf e_{l_\alpha}-\mathbf e_{k_\alpha},\qquad
a_{e_\alpha}=a_{l_\alpha}-a_{k_\alpha}
$$

Change the conductances by $\delta_\alpha$, keeping $c_{e_\alpha}+\delta_\alpha\ge0$. Write

$$
B=(b_1\ \cdots\ b_m),\qquad
\Delta=\operatorname{diag}(\delta_1,\ldots,\delta_m)
$$

The matrix $B$ contains only the selected pairs. A prime denotes the modified network; all unprimed quantities refer to the original network. In particular, $G=L^+$ and $\tau>0$ are the original Green matrix and spanning-tree coefficient.

Summing the contributions of the couplings gives

$$
L'=L+B\Delta B^{\mathsf T}
\tag{1}
$$

The rank of the perturbation is at most $\min(m,n-1)$ and may be smaller because of linearly dependent columns, zero variations, or cancellation between terms.

## The Gram matrix of the selected couplings

> [!info] The Gram matrix of the varied couplings
> **Definition.** The matrix
>
> $$
> K=B^{\mathsf T}GB,\qquad
> K_{\alpha\beta}=a_{e_\alpha}\cdot a_{e_\beta}
> \tag{2}
> $$
>
> is the Gram matrix of the selected affine vectors. Its diagonal entries are $K_{\alpha\alpha}=R_{e_\alpha}$, where $R_{e_\alpha}$ denotes the resistance between the endpoints of the pair.

The matrix $K$ is symmetric and positive semidefinite. It describes the selected directions and differs from the Green matrix $G$, which is indexed by all vertices.

For a unit current injected at $l_\beta$ and withdrawn at $k_\beta$, the entry $K_{\alpha\beta}$ equals the potential difference $\varphi_{l_\alpha}-\varphi_{k_\alpha}$. Reversing the orientation of one pair changes the signs of the corresponding row and column of $K$, preserving its principal minors and all resulting network quantities.

## The spanning-tree coefficient and the connectivity condition

> [!info] The determinant formula
> **Lemma.** For all admissible variations,
>
> $$
> \tau'=\tau\det(I_m+\Delta K)
> \tag{3}
> $$
>
> Here $I_m$ is the identity matrix of size $m$. The modified graph is connected if and only if $\det(I_m+\Delta K)>0$.

> [!note]- Proof
> **Proof.** Delete the row and column of a reference vertex from $L$, obtaining an invertible reduced Laplacian $L_0$. Let $B_0$ be obtained by deleting the same row from $B$. Applying the matrix determinant lemma to the reduced version of (1) gives
>
> $$
> \det L'_0=\det L_0\det(I_m+\Delta B_0^{\mathsf T}L_0^{-1}B_0)
> $$
>
> In [[From Lengths to Areas and Volumes]], the Gram matrix of vectors based at a reference vertex was shown to equal the inverse reduced Laplacian. It follows that $B_0^{\mathsf T}L_0^{-1}B_0=K$. The matrix-tree theorem gives (3), including when $L'_0$ is singular.
>
> With nonnegative conductances, $\tau'>0$ is equivalent to connectivity. Since the original $\tau>0$, the determinant condition follows. $\square$

Thus, in the admissible region, invertibility of $I_m+\Delta K$ is equivalent to connectivity of the final graph. Formula (3) does not require the final graph to be connected; the following inversion formulas do.

## The Green matrix and resistances

> [!info] The joint Green matrix update
> **Lemma.** If the modified graph is connected, then
>
> $$
> G'=G-GB(I_m+\Delta K)^{-1}\Delta B^{\mathsf T}G
> \tag{4}
> $$
>
> Individual $\delta_\alpha$ may be zero: the formula does not require inversion of $\Delta$.

> [!note]- Derivation of the inversion formula
> **Proof.** On $H=\mathbf1^\perp$, the matrix $G$ is the inverse of $L$. This allows the Woodbury formula to be applied in the form (4). We verify it without assuming that $\Delta$ is invertible.
>
> Temporarily write $M=(I_m+\Delta K)^{-1}\Delta$. Then
>
> $$
> M+\Delta KM=\Delta
> $$
>
> Multiplying the right-hand side of (4) on the left by $L'=L+B\Delta B^{\mathsf T}$ and using $LG=J$ and $JB=B$, we obtain
>
> $$
> L'(G-GBMB^{\mathsf T}G)
> =J+B(\Delta-M-\Delta KM)B^{\mathsf T}G=J
> $$
>
> Here $J=I_n-\mathbf1\mathbf1^{\mathsf T}/n$ is the centering matrix. The right-hand side of (4) sends constant column vectors to zero and maps $H$ into $H$. Therefore it equals $G'$. $\square$

For a measured pair $i,j$, set

$$
q=B^{\mathsf T}G\mathbf e_{ij},\qquad
q_\alpha=a_{ij}\cdot a_{e_\alpha}
$$

Substituting (4) into $R'_{ij}=\mathbf e_{ij}^{\mathsf T}G'\mathbf e_{ij}$ gives the exact formula

$$
R'_{ij}=R_{ij}-q^{\mathsf T}(I_m+\Delta K)^{-1}\Delta q
\tag{5}
$$

For $m=1$, formulas (3)-(5) reduce to the results of [[Variation of a Single Edge]]. If $\Delta\succeq0$, then

$$
(I_m+\Delta K)^{-1}\Delta
=\Delta^{1/2}(I_m+\Delta^{1/2}K\Delta^{1/2})^{-1}\Delta^{1/2}\succeq0
$$

The middle matrix is positive definite because $K\succeq0$. Hence the correction subtracted in (5) is nonnegative: strengthening several couplings together cannot increase any resistance. This statement includes zero variations.

## Two couplings and sequential changes

For two selected pairs $e,f$, set $g_{ef}=a_e\cdot a_f$. Then

$$
K=\begin{pmatrix}R_e&g_{ef}\\g_{ef}&R_f\end{pmatrix}
$$

Expanding the determinant in (3) gives

$$
\frac{\tau'}\tau
=1+\delta_eR_e+\delta_fR_f+\delta_e\delta_f(R_eR_f-g_{ef}^2)
\tag{6}
$$

The mixed coefficient $R_eR_f-g_{ef}^2$ is the Gram determinant of the two affine vectors, hence the squared area of the parallelogram they span.

If $e$ is changed first and the intermediate graph remains connected, the resistance of the second pair becomes

$$
R_f^{(e)}=R_f-\frac{\delta_e g_{ef}^2}{1+\delta_eR_e}
$$

The second step gives

$$
\frac{\tau'}\tau
=(1+\delta_eR_e)(1+\delta_fR_f^{(e)})
=(1+\delta_eR_e)(1+\delta_fR_f)-\delta_e\delta_f g_{ef}^2
$$

This agrees with (6). The second step uses the modified resistance $R_f^{(e)}$, rather than the original $R_f$.

> [!note] Connectivity of intermediate graphs
> The order of changes does not affect the final graph. However, applying the Green matrix and resistance formulas one step at a time requires every intermediate graph to be connected.
>
> For example, in the path $1-2-3$, one can delete edge $12$ and add edge $13$. The final graph is connected, but deleting $12$ first disconnects the network. The simultaneous formulas (4)-(5) apply, while sequential inversion in this order is impossible.
>
> If the initial and final graphs are connected, a valid order is to perform all strengthening and additions first, followed by weakening and deletions. The first stage retains the original connected graph. During the second stage, every intermediate graph contains all couplings of the final graph, with conductances at least as large as their final values.

## Mixed coefficients and volumes

For an index set $S\subseteq\{1,\ldots,m\}$, let $K_S$ denote the principal submatrix with those indices. Multilinearity of the determinant in its rows gives the expansion

$$
\frac{\tau'}\tau=\det(I_m+\Delta K)
=\sum_{S\subseteq\{1,\ldots,m\}}
\left(\prod_{\alpha\in S}\delta_\alpha\right)\det K_S
\tag{7}
$$

For the empty set, both the product and the determinant are one. When rows with indices in $S$ are selected from $\Delta K$, the remaining identity rows select the corresponding principal minor. This proves (7).

By the Gram formula, $\det K_S$ is the squared $|S|$-dimensional volume of the parallelotope spanned by the selected affine vectors. For one vector, it is a squared length; for two, a squared area; for three, a squared volume. If the vectors are linearly dependent, both the volume and the coefficient vanish. In particular, this occurs when the selected pairs contain a cycle.

For $r$ distinct indices $\alpha_1,\ldots,\alpha_r$, formula (7) implies

$$
\frac1\tau
\frac{\partial^r\tau}{\partial c_{e_{\alpha_1}}\cdots\partial c_{e_{\alpha_r}}}
=\det K_S,\qquad S=\{\alpha_1,\ldots,\alpha_r\}
\tag{8}
$$

There is no factor $r!$: each variable occurs once in the monomial. Differentiating twice with respect to the same conductance gives zero, since the spanning-tree coefficient has degree at most one in each conductance. At zero conductance, physically admissible derivatives are understood as right derivatives; as polynomial derivatives, they are defined without this restriction.

## Random spanning trees and transfer currents

Suppose the selected pairs are existing edges with positive conductances. Choose a spanning tree with probability $\Pr(T)=\tau^{-1}\prod_{e\in T}c_e$. The mixed derivative in (8) selects trees containing all the chosen edges and removes the corresponding factors from their weights. Therefore,

$$
\Pr(e_\alpha\in T\text{ for all }\alpha\in S)
=\left(\prod_{\alpha\in S}c_{e_\alpha}\right)\det K_S
\tag{9}
$$

> [!info] Transfer current
> **Definition.** For oriented edges $e:k_e\to l_e$ and $f:k_f\to l_f$, inject a unit current at $k_e$ and withdraw it at $l_e$. The external current column vector is $-b_e$, and the centered potentials are $\varphi=-Gb_e$.
>
> The transfer current $Y(e,f)$ is measured in the direction $k_f\to l_f$. By Ohm's law,
>
> $$
> Y(e,f)=c_f(\varphi_{k_f}-\varphi_{l_f})
> =c_f b_f^{\mathsf T}Gb_e=c_f g_{ef}
> $$

The injection direction is specified explicitly: in the definition of $Y$, current enters at the initial vertex of the oriented edge. In the potential convention for (2), it enters at the terminal vertex. This distinction gives the consistent sign for current measured along the edge orientation.

Multiplying the columns of $K_S$ by the conductances gives the matrix $Y_S$, so (9) is equivalent to $\Pr(S\subseteq T)=\det Y_S$. This is the transfer-current theorem, given in source [9] of [[Further Reading for the PMG Introductory Series|the reading recommendations]], Section 4.2, formula (4.5).

For two distinct edges, (9) gives

$$
\Pr(e,f\in T)-\Pr(e\in T)\Pr(f\in T)
=-c_ec_f g_{ef}^2\le0
$$

Thus the two edge-inclusion events have nonpositive covariance. When $g_{ef}=0$, these two events are independent.

## Deleting a set of edges

Let $S$ be a set of existing edges to be deleted completely. Write $W_S=\operatorname{diag}(c_e:e\in S)$. Substituting $\Delta=-W_S$ into (3) gives

$$
\frac{\tau'}\tau=\det(I_{|S|}-W_SK_S)
=\Pr(T\cap S=\varnothing)
\tag{10}
$$

The last equality follows by directly counting weights: the modified network retains exactly those spanning trees that use no edge from $S$.

The determinant in (10) is zero if and only if deleting $S$ disconnects the graph. For one edge, this recovers the bridge criterion $c_eR_e=1$. When the determinant is zero, formula (3) remains valid, but the inversion formulas (4)-(5) do not apply.

## Concavity of the logarithm of the spanning-tree coefficient

The single-coupling formula $\partial\log\tau/\partial c_e=R_e$ and resistance sensitivity give

$$
\frac{\partial^2\log\tau}{\partial c_{e_\alpha}\partial c_{e_\beta}}
=-K_{\alpha\beta}^2
\tag{11}
$$

The matrix of entrywise squares of $K$ is positive semidefinite. Hence the Hessian in (11) is negative semidefinite, and $\log\tau$ is concave in the conductances on the domain of connected networks.

> [!note]- Sign of the Hessian
> **Proof.** Write $K=P^{\mathsf T}P$, where the columns of $P$ are Euclidean coordinates of the selected affine vectors. For any real column vector $h$,
>
> $$
> \sum_{\alpha,\beta}h_\alpha h_\beta K_{\alpha\beta}^2
> =\sum_{r,s}\left(\sum_\alpha h_\alpha P_{r\alpha}P_{s\alpha}\right)^2\ge0
> $$
>
> Therefore the second derivative of $\log\tau$ along any linear conductance variation is nonpositive. The domain of nonnegative conductances with a connected graph is convex: at an interior point of a line segment between two such networks, every positive coupling of either network remains positive. On the boundary of the domain, concavity extends by continuity wherever $\tau>0$. $\square$

## Example: strengthening two couplings of a triangle

> [!example] The spanning-tree coefficient
> For $K_3$ with unit conductances, $\tau=3$ and all resistances are $2/3$. Choose the pairs $e=12$, $f=13$, both oriented away from vertex $1$. Then
>
> $$
> K=\begin{pmatrix}\frac23&\frac13\\\frac13&\frac23\end{pmatrix}
> $$
>
> Increase both conductances by one, so $\Delta=I_2$. By (3),
>
> $$
> \frac{\tau'}\tau=\det\begin{pmatrix}\frac53&\frac13\\\frac13&\frac53\end{pmatrix}
> =\frac83,\qquad \tau'=8
> $$
>
> Direct enumeration gives spanning-tree weights $4,2,2$, whose sum is $8$.
>
> Sequential calculation is also valid. After strengthening $12$, we have $\tau_e=5$ and $R_f^{(e)}=3/5$. The second step gives $\tau'=5(1+3/5)=8$.

> [!example] Resistance between vertices $2$ and $3$
> For the measured vector $a_{23}$,
>
> $$
> q=\begin{pmatrix}-\frac13\\\frac13\end{pmatrix},\qquad
> (I_2+K)^{-1}=\frac18\begin{pmatrix}5&-1\\-1&5\end{pmatrix}
> $$
>
> By (5),
>
> $$
> R'_{23}=\frac23-q^{\mathsf T}(I_2+K)^{-1}q
> =\frac23-\frac16=\frac12
> $$
>
> An independent electrical check: the direct edge $23$ has resistance $1$, and the path through vertex $1$ has resistance $1/2+1/2=1$. Their parallel connection gives $R'_{23}=1/2$.

## Further reading

The determinants in (7) express volumes, mixed derivatives, and joint edge-inclusion probabilities. The next note, [[Basic Objects and Operations of Polyform Algebra]], introduces the algebraic language for treating several affine vectors as one object. Its metric properties are discussed in [[Metric of Higher-Grade Objects]].

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], matrix identities for inverses and determinants are collected in [5] and [6], Gram determinants and multilinear algebra in [7] and [8], and random spanning trees and transfer currents in [9].
