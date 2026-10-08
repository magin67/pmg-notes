---
title: "Variation of a Single Edge"
date: 2026-10-04
updated: 2026-10-08
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: single-edge-variation
lang: en
description: "Exact changes in the Green matrix, effective resistances, spanning-tree coefficient, and weights of separating spanning 2-forests when one conductance varies."
---

Changing one conductance produces a perturbation of rank at most one in the Laplacian. This yields exact formulas for the Green matrix, effective resistances, and spanning-tree coefficient. Resistance sensitivities are expressed through inner products of affine vectors, while changes in the weights of separating spanning forests are related to Gram determinants.

## Setup and change in the Laplacian

We consider a finite connected undirected graph without loops on $n\ge2$ vertices. The conductances $c_{ij}=c_{ji}$ are nonnegative; positive values correspond to existing edges. Choose distinct vertices $k,l$ and change only one conductance:

$$
c'_{kl}=c_{kl}+\delta,\qquad \delta\ge-c_{kl}
$$

For $\delta>0$, the coupling is strengthened or added; for $-c_{kl}<\delta<0$, it is weakened; and for $\delta=-c_{kl}$, an existing edge is removed. A prime denotes quantities after the change, and $\Delta$ denotes the new value minus the original value.

We retain $a_{ij}=a_j-a_i$ and $\mathbf e_{ij}=\mathbf e_j-\mathbf e_i$. All unprimed resistances and inner products are computed in the **original graph**. The contribution of the coupling $kl$ to the Laplacian is $c_{kl}\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}$, so

$$
L'=L+\delta\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}
\tag{1}
$$

For $\delta\ne0$, the perturbation has rank one; for $\delta=0$, it is zero. The change preserves zero row and column sums.

## The spanning-tree coefficient and connectivity

The spanning-tree coefficient is defined by

$$
\tau=\sum_T\prod_{e\in T}c_e
$$

where the sum runs over spanning trees. By the [[From Lengths to Areas and Volumes|matrix-tree theorem]], $\tau$ equals the determinant of a reduced Laplacian. For a connected graph, $\tau>0$; for a disconnected graph, $\tau=0$, since there are no spanning trees.

> [!info] Change in the spanning-tree coefficient
> **Lemma.** For every $\delta\ge-c_{kl}$,
>
> $$
> \tau'=\tau(1+\delta R_{kl})
> \tag{2}
> $$
>
> The modified graph is connected if and only if $1+\delta R_{kl}>0$.

> [!note]- Proof
> **Proof.** Choose vertex $k$ as the reference vertex and delete its row and column from $L$, obtaining an invertible matrix $L_0$. Let $b$ be the column vector $\mathbf e_{kl}$ with coordinate $k$ deleted. Then $L'_0=L_0+\delta bb^{\mathsf T}$.
>
> The determinant formula for a rank-one perturbation gives
>
> $$
> \det L'_0=\det L_0\bigl(1+\delta b^{\mathsf T}L_0^{-1}b\bigr)
> $$
>
> The preceding note established that the Gram matrix of resistance vectors based at one vertex equals the inverse reduced Laplacian. Hence $b^{\mathsf T}L_0^{-1}b=R_{kl}$. The matrix-tree theorem gives (2), including when $L'_0$ is singular.
>
> With nonnegative conductances, $\tau'>0$ is equivalent to the existence of a spanning tree, hence to connectivity. Since $\tau>0$, this proves the criterion $1+\delta R_{kl}>0$. $\square$

In particular, while connectivity is preserved,

$$
\frac{\partial\tau}{\partial c_{kl}}=\tau R_{kl},\qquad
\frac{\partial\log\tau}{\partial c_{kl}}=R_{kl}
\tag{3}
$$

The resistance expresses the relative sensitivity of the spanning-tree coefficient to a conductance change.

## Change in the Green matrix

For the formulas in this section and the formulas for finite resistance changes, assume that the modified graph remains connected. Denote the Green matrices by $G=L^+$ and $G'=(L')^+$. On the subspace $H=\mathbf1^\perp$, they are the ordinary inverses of the restricted Laplacians.

> [!info] The Green matrix update
> **Lemma.** If $1+\delta R_{kl}>0$, then
>
> $$
> G'=G-\frac{\delta}{1+\delta R_{kl}}
> G\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}G
> \tag{4}
> $$

> [!note]- Derivation by the Sherman-Morrison formula
> **Proof.** For an invertible matrix $A$ and a column vector $b$, provided the denominator is nonzero,
>
> $$
> (A+\delta bb^{\mathsf T})^{-1}
> =A^{-1}-\frac{\delta A^{-1}bb^{\mathsf T}A^{-1}}{1+\delta b^{\mathsf T}A^{-1}b}
> $$
>
> Apply this identity to the restriction of (1) to $H$, using an orthonormal basis of that subspace. The column vector $\mathbf e_{kl}$ belongs to $H$, and $\mathbf e_{kl}^{\mathsf T}G\mathbf e_{kl}=R_{kl}$. Both sides of (4) act as zero on constant column vectors. Thus the formula holds on the full space. $\square$

Formula (4) is exact and requires no smallness assumption on $\delta$. The column vector $G\mathbf e_{kl}$ gives the centered potentials for a unit current injected at $l$ and withdrawn at $k$. For $\delta\ne0$, the change in $G$ has rank one because this column vector is nonzero.

## Finite change in resistance

For any vertices $i,j$, we have $R_{ij}=\mathbf e_{ij}^{\mathsf T}G\mathbf e_{ij}$. Substituting (4) and using $\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}=a_{ij}\cdot a_{kl}$ gives the following result.

> [!info] Change in effective resistance
> **Corollary.** If connectivity is preserved, then
>
> $$
> \Delta R_{ij}=-\frac{\delta}{1+\delta R_{kl}}(a_{ij}\cdot a_{kl})^2
> \tag{5}
> $$
>
> In terms of the resistances of the original graph, this is
>
> $$
> \Delta R_{ij}=-\frac{\delta}{4(1+\delta R_{kl})}
> (R_{il}+R_{jk}-R_{ik}-R_{jl})^2
> $$

The mixed factor has an electrical interpretation. For a unit current injected at $l$ and withdrawn at $k$,

$$
\varphi_j-\varphi_i=a_{ij}\cdot a_{kl}
$$

Thus the resistance change is determined by the squared transfer voltage. By reciprocity, the current pair and the measurement pair can be interchanged while retaining their orientations.

> [!note] Monotonicity and unchanged measurements
> The denominator in (5) is positive. Hence strengthening a coupling cannot increase resistances, and weakening it cannot decrease them. This is Rayleigh's monotonicity principle for variation of a single coupling.
>
> If $a_{ij}\cdot a_{kl}=0$, then $R_{ij}$ remains unchanged for every admissible $\delta$ that preserves connectivity. For nonzero $\delta$, this condition is also necessary for $\Delta R_{ij}=0$.

For the endpoints of the varied coupling itself, $a_{kl}\cdot a_{kl}=R_{kl}$. Formula (5) gives

$$
R'_{kl}=\frac{R_{kl}}{1+\delta R_{kl}},\qquad
\frac1{R'_{kl}}=\frac1{R_{kl}}+\delta
\tag{6}
$$

For $\delta>0$, the second identity expresses the addition of conductance $\delta$ in parallel between the same vertices.

## Derivatives with respect to conductance

Dividing (5) by $\delta$ and taking the limit as $\delta\to0$ gives

$$
\frac{\partial R_{ij}}{\partial c_{kl}}=-(a_{ij}\cdot a_{kl})^2,\qquad
\frac{\partial R_{kl}}{\partial c_{kl}}=-R_{kl}^2
\tag{7}
$$

For $c_{kl}>0$, the derivatives in (3) and (7) are ordinary two-sided derivatives: sufficiently small changes preserve connectivity. For $c_{kl}=0$, the physically admissible derivative is a right derivative, since the conductance can only increase. The algebraic expressions extend to a neighborhood of zero, but negative conductance lies outside the network model considered here.

## Edge probability and bridge deletion

Let $c_{kl}>0$. Choose a spanning tree with probability proportional to the product of its edge conductances. Differentiating $\tau$ with respect to $c_{kl}$ leaves only the contributions from trees containing this edge. Hence, by (3),

$$
\Pr(kl\in T)=\frac{c_{kl}}\tau\frac{\partial\tau}{\partial c_{kl}}
=c_{kl}R_{kl}
$$

When the edge is deleted completely, $\delta=-c_{kl}$, formula (2) becomes

$$
\tau'=\tau(1-c_{kl}R_{kl})
$$

> [!info] The bridge criterion
> **Proposition.** For an existing edge of a connected graph, the following conditions are equivalent:
>
> - The edge $kl$ is a bridge, meaning that its deletion disconnects the graph.
> - The edge belongs to every spanning tree.
> - $c_{kl}R_{kl}=1$.

If the edge is not a bridge, there is a spanning tree of positive weight that does not contain it. Therefore $c_{kl}R_{kl}<1$, and formulas (4)-(6) remain applicable through complete deletion.

When a bridge is deleted, the denominator vanishes and $\tau'=0$. Resistances between different components cease to be finite: injecting current into one component and withdrawing it from another admits no steady-state solution, even though the total external current is balanced. The pseudoinverse of the disconnected Laplacian exists, but formula (4) does not compute it, and the usual resistance formula using that pseudoinverse does not give an effective resistance between components.

## Weights of separating spanning forests

> [!info] A separating spanning 2-forest
> **Definition.** For distinct vertices $i,j$, a separating spanning 2-forest contains all vertices of the graph, has no cycles, and has exactly two components, with $i$ and $j$ in different components. Its weight is the product of its edge conductances. Denote the sum of these weights by
>
> $$
> m_{ij}=\sum_{F}\prod_{e\in F}c_e
> $$
>
> Each forest is counted once, with no ordering of its components. The product over an empty edge set is one.

> [!info] The forest formula for resistance
> **Lemma.** For the connected original graph,
>
> $$
> m_{ij}=\tau R_{ij}
> \tag{8}
> $$

> [!note]- Proof by adding a coupling
> **Proof.** Increase the conductance of the pair $ij$ by $t\ge0$, adding the edge if it was absent. The weight of each spanning tree depends at most linearly on this conductance. The coefficient of $t$ is obtained by deleting the edge $ij$ from the tree.
>
> This deletion produces a separating spanning 2-forest. Conversely, adding the edge $ij$ to any such forest produces a spanning tree. This is a bijection that preserves the product of the conductances of the remaining edges. Thus the new spanning-tree coefficient is $\tau+t m_{ij}$.
>
> By (2), the same coefficient is $\tau(1+tR_{ij})$. Comparing coefficients of $t$ proves (8). $\square$

## Variation of forest weight and area

As long as the modified graph is connected, multiplying (2) by $R'_{ij}=R_{ij}+\Delta R_{ij}$ from (5) gives

$$
\Delta m_{ij}=\delta\tau\bigl(R_{ij}R_{kl}-(a_{ij}\cdot a_{kl})^2\bigr)
$$

The expression in parentheses is the Gram determinant of two affine vectors. Using the notation of the preceding note, we obtain the following result.

> [!info] Change in spanning 2-forest weight
> **Corollary.** For every $\delta\ge-c_{kl}$, including bridge deletion,
>
> $$
> \Delta m_{ij}=\delta\tau\det G(a_{ij},a_{kl})
> =\delta\tau S_{\parallel}^2
> \tag{9}
> $$
>
> The parallelogram area $S_{\parallel}$ is computed in the original resistance representation.

> [!note]- Extension to bridge deletion
> **Proof.** With the other conductances fixed, $m'_{ij}$ is a polynomial of degree at most one in $\delta$: each edge occurs in a forest at most once. The right-hand side of (9) is also linear in $\delta$. The equality has already been proved for $\delta\ge0$, when connectivity is preserved. It is therefore a polynomial identity and also holds at $\delta=-c_{kl}$.
>
> After a bridge is deleted, $m'_{ij}$ is defined by the sum of forest weights. Formula (8) is not applied to the disconnected network: the product of a zero spanning-tree coefficient and an infinite resistance is undefined. $\square$

For the varied pair itself, $i=k$, $j=l$, the determinant in (9) is zero, so $m'_{kl}=m_{kl}$. This agrees with the definition: a forest separating $k$ and $l$ cannot contain the edge $kl$.

## Example: strengthening an edge of a triangle

> [!example] Resistances and the spanning-tree coefficient
> In $K_3$ with unit conductances, $\tau=3$ and $R_{12}=R_{13}=R_{23}=2/3$. Increase $c_{12}$ from $1$ to $2$, so $\delta=1$.
>
> Formulas (6) and (5), with $a_{13}\cdot a_{12}=1/3$, give
>
> $$
> R'_{12}=\frac{2/3}{1+2/3}=\frac25,\qquad
> R'_{13}=\frac23-\frac{1/9}{1+2/3}=\frac35
> $$
>
> By symmetry, $R'_{23}=3/5$. Formula (2) gives $\tau'=3(1+2/3)=5$.
>
> An independent check of the resistances uses parallel paths. Between $1$ and $2$, the branch resistances are $1/2$ and $2$; between $1$ and $3$, they are $1$ and $3/2$:
>
> $$
> R'_{12}=\frac{(1/2)\cdot2}{1/2+2}=\frac25,\qquad
> R'_{13}=\frac{1\cdot(3/2)}{1+3/2}=\frac35
> $$
>
> The three spanning trees have weights $2,2,1$, whose sum is $5$. The probability of edge $12$ increases from $2/3$ to $c'_{12}R'_{12}=4/5$.

> [!example] Forest weight
> Before the change, $m_{13}=\tau R_{13}=2$. After the change, $m'_{13}=\tau'R'_{13}=3$. Formula (9) gives
>
> $$
> \Delta m_{13}=1\cdot3\left(\frac23\cdot\frac23-\frac19\right)=1
> $$
>
> Direct enumeration: the spanning 2-forests separating vertices $1$ and $3$ consist of the single edge $12$ or $23$. Their total weight changes from $1+1=2$ to $2+1=3$.

## Further reading

[[Varying several couplings together]] considers simultaneous changes in several conductances. Their interactions are described by the matrix of inner products of the corresponding affine vectors.

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], the Sherman-Morrison formula is covered in sources [5] and [6], Rayleigh monotonicity in [2], the matrix-tree theorem in [3], and the probabilistic interpretation of edges in [9]. The forest formula (8) and its variation (9) are derived directly in this note.
