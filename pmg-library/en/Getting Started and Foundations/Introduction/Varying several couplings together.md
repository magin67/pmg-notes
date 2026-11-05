---
title: Varying Several Couplings Together
date: 2026-10-05
updated: 2026-11-05
revision: 5
source_revision: 6
status: draft
text_prepared_by: ChatGPT
translation_key: joint-edge-variation
lang: en
description: Exact formulas for simultaneous conductance changes. Gram determinants as variation coefficients of the spanning-tree coefficient, edge probabilities, and criteria for preserving connectivity.
order: "7"
aliases:
  - "en/Introduction/Varying several couplings together"
---

When two couplings change, adding their separate effects computed in the original graph generally gives the wrong result: the first change alters the effect of the second. We begin with two couplings, then express the general result through their matrix of inner products.

## Two couplings and sequential changes

Start with two distinct vertex pairs $e,f$ in a finite connected undirected network without loops, with nonnegative conductances. Choose an orientation for each pair and the corresponding difference vector $a_e$ or $a_f$. Let $R_e,R_f$ be the resistances between their endpoints, and let $g_{ef}=a_e\cdot a_f$. All three quantities initially refer to the original network.

Change the conductances by $\delta_e,\delta_f$, keeping them nonnegative. If $e$ is changed first and the intermediate graph remains connected, the [[Variation of a Single Edge#Finite change in resistance|single-coupling variation formula]] gives the new resistance of the second pair:

$$
R_f^{(e)}=R_f-\frac{\delta_e g_{ef}^2}{1+\delta_eR_e}
$$

Let $\tau$ and $\tau'$ denote the spanning-tree coefficients of the original and final networks. The first step multiplies this coefficient by $1+\delta_eR_e$, and the second by $1+\delta_fR_f^{(e)}$. Hence

$$
\begin{aligned}
\frac{\tau'}\tau
&=(1+\delta_eR_e)(1+\delta_fR_f^{(e)})\\
&=(1+\delta_eR_e)(1+\delta_fR_f)-\delta_e\delta_f g_{ef}^2\\
&=1+\delta_eR_e+\delta_fR_f+\delta_e\delta_f(R_eR_f-g_{ef}^2)
\end{aligned}
\tag{1}
$$

The second step requires the **updated** resistance $R_f^{(e)}$. Substituting the original $R_f$ would lose the term $-\delta_e\delta_f g_{ef}^2$, which accounts for how the first coupling changed the effect of the second.

The mixed coefficient $R_eR_f-g_{ef}^2$ is the determinant of the Gram matrix

$$
G=\begin{pmatrix}R_e&g_{ef}\\g_{ef}&R_f\end{pmatrix}
$$

It is the squared area of the parallelogram on the two resistance vectors. This is why joint variations involve areas and, for more couplings, higher-dimensional volumes.

### Example: two couplings of a triangle

For unit-conductance $K_3$, we have $\tau=3$, $R_e=R_f=2/3$, and $g_{ef}=1/3$ for $e=12$, $f=13$, oriented away from vertex $1$. Increase both conductances by one. Formula (1) gives

$$
\frac{\tau'}\tau=1+\frac23+\frac23+\left(\frac49-\frac19\right)=\frac83,\qquad \tau'=8
$$

Sequentially, strengthening $12$ gives $\tau_e=5$ and $R_f^{(e)}=3/5$, then $\tau'=5(1+3/5)=8$. Directly summing the weights of the three spanning trees gives the same value, $4+2+2=8$.

## Problem setup

We consider a finite connected undirected graph without loops on $n\ge2$ vertices, with nonnegative coupling strengths. Choose $m$ distinct unordered vertex pairs and denote them by $e_1,\ldots,e_m$. A pair may be an existing edge or an absent coupling of strength zero.

Choose an orientation for each pair. If pair $\alpha$ is directed from $i$ to $j$, set

$$
t_\alpha=a_j-a_i,\qquad b_\alpha=\mathbf e_j-\mathbf e_i
$$

Thus $t_\alpha$ is a two-point vector, and $b_\alpha$ is its coefficient column: $-1$ at the start, $1$ at the end, and zeros elsewhere. Denote the coupling strength by $c_\alpha$ and the resistance between its endpoints by $R_\alpha$. Here $i,j$ name the endpoints of the selected pair and vary from pair to pair.

Change the coupling strengths by $\delta_\alpha$, keeping $c_\alpha+\delta_\alpha\ge0$. Collect the coefficients and changes into matrices:

$$
B=(b_1\ \cdots\ b_m),\qquad
\Delta=\operatorname{diag}(\delta_1,\ldots,\delta_m)
$$

A prime denotes the modified graph; all unprimed quantities refer to the original graph. In particular, $\mathrm{Gr}=L^+$ and $\tau>0$ are the original Green matrix and spanning-tree coefficient.

Summing the contributions of the couplings gives

$$
L'=L+B\Delta B^{\mathsf T}
\tag{2}
$$

The rank of the perturbation is at most $\min(m,n-1)$ and may be smaller because of linearly dependent columns, zero variations, or cancellation between terms.

## The Gram matrix of the selected couplings

> [!info] The Gram matrix of the varied couplings
> **Definition.** The matrix
>
> $$
> G=(g_{\alpha\beta})=B^{\mathsf T}\mathrm{Gr}B,\qquad
> g_{\alpha\beta}=t_\alpha\cdot t_\beta
> \tag{3}
> $$
>
> is the Gram matrix of the selected two-point vectors. Its diagonal entries are $g_{\alpha\alpha}=R_\alpha$, where $R_\alpha$ denotes the resistance between the endpoints of the pair.

The matrix $G$ is symmetric and positive semidefinite. It describes the selected directions and differs from the Green matrix $\mathrm{Gr}$, which is indexed by all vertices.

For a unit current injected at the end of pair $\beta$ and withdrawn at its start, $g_{\alpha\beta}$ is the end-minus-start potential difference across pair $\alpha$.

For a set of indices $S$, retain only the rows and columns of $G$ with indices in $S$. The resulting matrix $G_S$ is a **principal submatrix**, and its determinant $\det G_S$ is a **principal minor**. For example, $S=\{1,3\}$ retains rows $1,3$ and columns $1,3$. Reversing one pair changes the signs of the corresponding row and column of $G$, so every principal minor is preserved.

## The spanning-tree coefficient and the connectivity condition

> [!info] The determinant formula
> **Lemma.** For all admissible variations,
>
> $$
> \tau'=\tau\det(I_m+\Delta G)
> \tag{4}
> $$
>
> Here $I_m$ is the identity matrix of size $m$. The modified graph is connected if and only if $\det(I_m+\Delta G)>0$.

> [!note]- Proof
> **Proof.** Delete the row and column of a reference vertex from $L$, obtaining an invertible reduced Laplacian $L_0$. Let $B_0$ be obtained by deleting the same row from $B$. Applying the matrix determinant lemma to the reduced version of (2) gives
>
> $$
> \det L'_0=\det L_0\det(I_m+\Delta B_0^{\mathsf T}L_0^{-1}B_0)
> $$
>
> In [[From Lengths to Areas and Volumes]], the Gram matrix of vectors based at a reference vertex was shown to equal the inverse reduced Laplacian. It follows that $B_0^{\mathsf T}L_0^{-1}B_0=G$. The matrix-tree theorem gives (4), including when $L'_0$ is singular.
>
> With nonnegative conductances, $\tau'>0$ is equivalent to connectivity. Since the original $\tau>0$, the determinant condition follows. $\square$

Thus, in the admissible region, invertibility of $I_m+\Delta G$ is equivalent to connectivity of the final graph. Formula (4) does not require the final graph to be connected; the following inversion formulas do.

For $m=2$, expanding the determinant in (4) reproduces (1). Thus the two-coupling formula remains valid even if the chosen order of separate changes temporarily disconnects the graph.

## The Green matrix and resistances

> [!info] The joint Green matrix update
> **Lemma.** If the modified graph is connected, then
>
> $$
> \mathrm{Gr}'=\mathrm{Gr}-\mathrm{Gr}B(I_m+\Delta G)^{-1}\Delta B^{\mathsf T}\mathrm{Gr}
> \tag{5}
> $$
>
> Individual $\delta_\alpha$ may be zero: the formula does not require inversion of $\Delta$.

> [!note]- Derivation of the inversion formula
> **Proof.** On $H=\mathbf1^\perp$, the matrix $\mathrm{Gr}$ is the inverse of $L$. This allows the Woodbury formula to be applied in the form (5). We verify it without assuming that $\Delta$ is invertible.
>
> Temporarily write $M=(I_m+\Delta G)^{-1}\Delta$. Then
>
> $$
> M+\Delta GM=\Delta
> $$
>
> Multiplying the right-hand side of (5) on the left by $L'=L+B\Delta B^{\mathsf T}$ and using $L\mathrm{Gr}=J$ and $JB=B$, we obtain
>
> $$
> L'(\mathrm{Gr}-\mathrm{Gr}BMB^{\mathsf T}\mathrm{Gr})
> =J+B(\Delta-M-\Delta GM)B^{\mathsf T}\mathrm{Gr}=J
> $$
>
> Here $J=I_n-\mathbf1\mathbf1^{\mathsf T}/n$ is the centering matrix. The right-hand side of (5) sends lists with equal entries to zero and maps $H$ into $H$. Therefore it equals $\mathrm{Gr}'$. $\square$

To find the resistance change between $i$ and $j$, we need the inner product of the measured vector $a_{ij}$ with each varied direction $t_\alpha$. Collect these inner products in a list $q$, written as a column:

$$
q=B^{\mathsf T}\mathrm{Gr}\mathbf e_{ij},\qquad
q_\alpha=a_{ij}\cdot t_\alpha
$$

Substituting (5) into $R'_{ij}=\mathbf e_{ij}^{\mathsf T}\mathrm{Gr}'\mathbf e_{ij}$ gives the exact formula

$$
R'_{ij}=R_{ij}-q^{\mathsf T}(I_m+\Delta G)^{-1}\Delta q
\tag{6}
$$

## Example: strengthening two couplings of a triangle

Return to the strengthening of pairs $12$ and $13$ in unit-conductance $K_3$. We now apply the general matrix formula to the resistance of the third pair. Here $\Delta=I_2$ and

$$
G=\begin{pmatrix}\frac23&\frac13\\\frac13&\frac23\end{pmatrix}
$$

> [!example] Resistance between vertices $2$ and $3$
> For the measured vector $a_{23}$,
>
> $$
> q=\begin{pmatrix}-\frac13\\\frac13\end{pmatrix},\qquad
> (I_2+G)^{-1}=\frac18\begin{pmatrix}5&-1\\-1&5\end{pmatrix}
> $$
>
> By (6),
>
> $$
> R'_{23}=\frac23-q^{\mathsf T}(I_2+G)^{-1}q
> =\frac23-\frac16=\frac12
> $$
>
> An independent electrical check: the direct edge $23$ has resistance $1$, and the path through vertex $1$ has resistance $1/2+1/2=1$. Their parallel connection gives $R'_{23}=1/2$.

### Strengthening and intermediate graphs

For $m=1$, formulas (4)-(6) reduce to the results of [[Variation of a Single Edge]]. Consider strengthening the couplings, so that $\delta_\alpha\ge0$ for every $\alpha$. For the diagonal matrix $\Delta$, this is written as $\Delta\succeq0$. In general, $A\succeq0$ means $z^{\mathsf T}Az\ge0$ for every real list $z$; a symmetric matrix with this property is called positive semidefinite. We have

$$
(I_m+\Delta G)^{-1}\Delta
=\Delta^{1/2}(I_m+\Delta^{1/2}G\Delta^{1/2})^{-1}\Delta^{1/2}\succeq0
$$

The middle matrix is positive definite because $G\succeq0$. Hence the correction subtracted in (6) is nonnegative: strengthening several couplings together cannot increase any resistance. This statement includes zero variations.

> [!note] Connectivity of intermediate graphs
> The order of changes does not affect the final graph. However, applying the Green matrix and resistance formulas one step at a time requires every intermediate graph to be connected.
>
> For example, in the path $1-2-3$, one can delete edge $12$ and add edge $13$. The final graph is connected, but deleting $12$ first disconnects the network. The simultaneous formulas (5)-(6) apply, while sequential inversion in this order is impossible.
>
> If the initial and final graphs are connected, a valid order is to perform all strengthening and additions first, followed by weakening and deletions. The first stage retains the original connected graph. During the second stage, every intermediate graph contains all couplings of the final graph, with conductances at least as large as their final values.


## Mixed coefficients and volumes

Use the principal submatrices $G_S$ defined above, with $S\subseteq\{1,\ldots,m\}$. Multilinearity of the determinant in its rows gives the expansion

$$
\frac{\tau'}\tau=\det(I_m+\Delta G)
=\sum_{S\subseteq\{1,\ldots,m\}}
\left(\prod_{\alpha\in S}\delta_\alpha\right)\det G_S
\tag{7}
$$

For the empty set, both the product and the determinant are one. When rows with indices in $S$ are selected from $\Delta G$, the remaining identity rows select the corresponding principal minor. This proves (7).

By the Gram formula, $\det G_S$ is the squared $|S|$-dimensional volume of the parallelotope spanned by the selected two-point vectors. For one vector, it is a squared length; for two, a squared area; for three, a squared volume. If the vectors are linearly dependent, both the volume and the coefficient vanish. In particular, this occurs when the selected pairs contain a cycle.

Choose any $r$ pairs and, for brevity, relabel them $1,\ldots,r$. Formula (7) implies

$$
\frac1\tau
\frac{\partial^r\tau}{\partial c_1\cdots\partial c_r}
=\det G_S,\qquad S=\{1,\ldots,r\}
\tag{8}
$$

There is no factor $r!$: each variable occurs once in the monomial. Differentiating twice with respect to the same conductance gives zero, since the spanning-tree coefficient has degree at most one in each conductance. At zero conductance, physically admissible derivatives are understood as right derivatives; as polynomial derivatives, they are defined without this restriction.

## Random spanning trees and transfer currents

Suppose the selected pairs are existing edges with positive conductances. Choose a spanning tree with probability $\Pr(T)=\tau^{-1}\prod_{e\in T}c_e$. The mixed derivative in (8) selects trees containing all the chosen edges and removes the corresponding factors from their weights. Therefore,

$$
\Pr(e_\alpha\in T\text{ for all }\alpha\in S)
=\left(\prod_{\alpha\in S}c_\alpha\right)\det G_S
\tag{9}
$$

> [!info] Transfer current
> **Definition.** Orient the edges as $e:i\to j$ and $f:k\to l$. Inject a unit current at $i$ and withdraw it at $j$. With $b_e=\mathbf e_j-\mathbf e_i$, the external current list is $-b_e$ and the centered potentials are $\varphi=-\mathrm{Gr}b_e$.
>
> The transfer current $Y(e,f)$ is measured in the direction $k\to l$. By Ohm's law,
>
> $$
> Y(e,f)=c_f(\varphi_k-\varphi_l)
> =c_f b_f^{\mathsf T}\mathrm{Gr}b_e=c_f g_{ef}
> $$
>
> Here $b_f=\mathbf e_l-\mathbf e_k$ and $g_{ef}=a_{ij}\cdot a_{kl}$.

The two measurements use different direction conventions. For the same pairs $e:i\to j$, $f:k\to l$:

| Quantity | Injection vertex | Withdrawal vertex | Measurement across $f$ |
|---|---|---|---|
| $g_{ef}$ | $j$ | $i$ | $\varphi_l-\varphi_k$ |
| $Y(e,f)$ | $i$ | $j$ | $c_f(\varphi_k-\varphi_l)$ |

In the second row, both the current and the order of potential subtraction are reversed. The two sign changes cancel, so $Y(e,f)=c_f g_{ef}$.

Multiplying the columns of $G_S$ by the conductances gives the matrix $Y_S$, so (9) is equivalent to $\Pr(S\subseteq T)=\det Y_S$. This is the transfer-current theorem, given in source [9] of [[Further Reading for the PMG Introductory Series|the reading recommendations]], Section 4.2, formula (4.5).

For two distinct edges, (9) gives

$$
\Pr(e,f\in T)-\Pr(e\in T)\Pr(f\in T)
=-c_ec_f g_{ef}^2\le0
$$

The probability that both edges are included is no greater than the product of their separate inclusion probabilities. This is called nonpositive covariance of the events. When $g_{ef}=0$, these two events are independent.

## Deleting a set of edges

Let $S$ be a set of existing edges to be deleted completely. Write $W_S=\operatorname{diag}(c_e:e\in S)$. Substituting $\Delta=-W_S$ into (4) gives

$$
\frac{\tau'}\tau=\det(I_{|S|}-W_SG_S)
=\Pr(T\cap S=\varnothing)
\tag{10}
$$

The last equality follows by directly counting weights: the modified network retains exactly those spanning trees that use no edge from $S$.

The determinant in (10) is zero if and only if deleting $S$ disconnects the graph. For one edge, this recovers the bridge criterion $c_eR_e=1$. When the determinant is zero, formula (4) remains valid, but the inversion formulas (5)-(6) do not apply.

## Concavity of the logarithm of the spanning-tree coefficient

This is an additional consequence for conductance optimization; it is not needed for the transition to polyform algebra.

The single-coupling formula $\partial\log\tau/\partial c_e=R_e$ and resistance sensitivity give

$$
\frac{\partial^2\log\tau}{\partial c_\alpha\partial c_\beta}
=-g_{\alpha\beta}^2
\tag{11}
$$

The matrix of entrywise squares of $G$ is positive semidefinite. Hence the matrix of second derivatives (the Hessian) in (11) is negative semidefinite, and $\log\tau$ is concave in the conductances on the domain of connected networks.

> [!note]- Sign of the Hessian
> **Proof.** Write $G=P^{\mathsf T}P$, where the columns of $P$ are Euclidean coordinates of the selected two-point vectors. For any real column vector $h$,
>
> $$
> \sum_{\alpha,\beta}h_\alpha h_\beta g_{\alpha\beta}^2
> =\sum_{r,s}\left(\sum_\alpha h_\alpha P_{r\alpha}P_{s\alpha}\right)^2\ge0
> $$
>
> Therefore the second derivative of $\log\tau$ along any linear conductance variation is nonpositive. The domain of nonnegative conductances with a connected graph is convex: at an interior point of a line segment between two such networks, every positive coupling of either network remains positive. On the boundary of the domain, concavity extends by continuity wherever $\tau>0$. $\square$

## Further reading

The determinants in (7) express volumes, mixed derivatives, and joint edge-inclusion probabilities. The note [[Basic Objects and Operations of Polyform Algebra]] introduces the algebraic language for treating several affine vectors as one object. Its metric properties are discussed in [[Metric of Higher-Grade Objects]].

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], matrix identities for inverses and determinants are collected in [5] and [6], Gram determinants and multilinear algebra in [7] and [8], and random spanning trees and transfer currents in [9].

