---
title: KVP Decomposition of the Green Matrix and Resistances
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-decomposition-green-matrix-and-resistances
lang: en
order: 5
description: "KVP and KVPO of the Green matrix, components of pair and one-way resistances, the V-U relation, preservation of circulation, and nonlinear Laplacian inversion. Five computed examples."
---

KVP decomposition can be applied to both the coupling table and the resistance table of a graph. The components have different meanings in these tables: the former describes direct couplings, the latter the metric determined by the whole graph. Between them lies Laplacian inversion, which generally mixes components.

We first define a decomposition of the Green matrix itself, then establish exact formulas for resistances. For an undirected graph, the symmetric resistance table has a KVP decomposition. For a balanced graph, we must additionally distinguish symmetric pair resistances, one-way resistances, and the balanced table obtained using the distance operator.

The projectors are defined in [[KVP Decomposition of Pair Characteristics]] and [[Oriented Extensions of KVP - Circulation and Imbalance]]. Their action in passing from a centered matrix to pair data is proved in [[The Distance Operator and KVP Decomposition]].

## Scope and initial definitions

Consider a fixed set of $n\ge3$ vertices. The graph is connected and loopless, with nonnegative coupling weights. Initially the coupling table $C$ is symmetric. Sections on the oriented case allow a connected balanced graph: $C\mathbf1=C^{\mathsf T}\mathbf1$, but $C$ may be nonsymmetric. With nonnegative weights, a connected balanced graph is strongly connected.

The outgoing Laplacian and the centering matrix are

$$
L=\mathscr L(C)=\operatorname{diag}(C\mathbf1)-C,
\qquad
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

> [!info] Scope and initial definitions
> **Definition.** The Green matrix $\mathrm{Gr}=L^+$ inverts $L$ on $H=\mathbf1^\perp$ and vanishes on constant column vectors. In both models considered here,
>
> $$
> L\mathrm{Gr}=\mathrm{Gr}L=J,
> \qquad
> \mathrm{Gr}\mathbf1=0,
> \qquad
> \mathbf1^{\mathsf T}\mathrm{Gr}=0
> $$

A useful computational identity is

$$
\mathrm{Gr}=
\left(L+\frac1n\mathbf1\mathbf1^{\mathsf T}\right)^{-1}
-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

Introduce the diagonal data and their deviations from the mean:

$$
q_i=\mathrm{Gr}_{ii},\qquad
t=\operatorname{tr}\mathrm{Gr},\qquad
\eta_i=q_i-\frac tn,\qquad
\sum_i\eta_i=0
\tag{1}
$$

The notation $\mathrm{Gr}$ denotes the Green matrix. $G$ remains reserved for the Gram matrix of chosen elements. If $h=n^{-1}\sum_i a_i$ is the centroid and $x_i=a_i-h$, then in the symmetric case $\mathrm{Gr}_{ij}=x_i\cdot x_j$ and $q_i=x_i^2$. For a balanced graph, with the adopted order of roles,

$$
\beta(u,v)=u^{\mathrm{out}}\cdot v^{\mathrm{in}}
=\mathbf v^{\mathsf T}\mathrm{Gr}\mathbf u,
\qquad
\beta(x_i,x_j)=\mathrm{Gr}_{ji}
$$

Thus the Gram matrix of the centered vectors of a balanced graph is $\mathrm{Gr}^{\mathsf T}$. The diagonal entry $q_i$ still equals the quadratic norm of $x_i$. The argument order is explained in [[The Gram Matrix and Directional Coordinates of a Balanced Graph]].

## What decomposition of the Green matrix means

The Green matrix has a nonzero diagonal. Projectors for zero-diagonal pair tables therefore cannot be applied to it without specifying the change of representation.

> [!info] What decomposition of the Green matrix means
> **Definition.** The pair coefficients of the Green matrix are the table
>
> $$
> \gamma_{ij}=-\mathrm{Gr}_{ij}\quad(i\ne j),
> \qquad \gamma_{ii}=0
> \tag{2}
> $$

The zero row and column sums of $\mathrm{Gr}$ give

$$
\gamma\mathbf1=\gamma^{\mathsf T}\mathbf1=\mathbf q,
\qquad
\mathrm{Gr}=\mathscr L(\gamma)
$$

Thus $\gamma$ is symmetric for an undirected graph and balanced for a balanced graph. Its coefficients may have either sign: $\gamma$ need not be a table of positive conductances.

Decompose $\gamma$ into pair sectors and transport the result using $\mathscr L$:

$$
\mathrm{Gr}_X=\mathscr L(\gamma_X),
\qquad X\in\{K,V,P,O\}
$$

Then

$$
\mathrm{Gr}=\mathrm{Gr}_K+\mathrm{Gr}_V+\mathrm{Gr}_P+\mathrm{Gr}_O
$$

In the symmetric case, $\gamma_O=\mathrm{Gr}_O=0$, leaving KVP. The U-component is absent from this representation because $\gamma$ is balanced.

The K- and V-parameters follow directly from (1):

$$
\mu_\gamma=\frac{t}{n(n-1)},
\qquad
v_i^{(\gamma)}=\eta_i,
\qquad
(\gamma_V)_{ij}=\frac{\eta_i+\eta_j}{n-2}\quad(i\ne j)
$$

The matrix components have explicit formulas

$$
\boxed{
\mathrm{Gr}_K=\frac{t}{n-1}J,
\qquad
\mathrm{Gr}_V=\frac{n}{n-2}J\operatorname{diag}(\boldsymbol\eta)J
}
\tag{3}
$$

Moreover,

$$
\mathrm{Gr}_O=\frac{\mathrm{Gr}-\mathrm{Gr}^{\mathsf T}}2,
\qquad
\mathrm{Gr}_P=\frac{\mathrm{Gr}+\mathrm{Gr}^{\mathsf T}}2
-\mathrm{Gr}_K-\mathrm{Gr}_V
$$

> [!note]- Proof
> **Proof.** The row and column sums of $\gamma$ equal $q_i$, and the sum of all its entries is $t$. This gives $\mu_\gamma$ and $v^{(\gamma)}$. The Laplacian of a constant pair table is $n\mu_\gamma J$. For the V-component, its diagonal is $\eta_i$ and its off-diagonal entries are $-(\eta_i+\eta_j)/(n-2)$, giving the second matrix in (3). The skew-symmetric part of $\gamma$ has zero row sums, so $\gamma_O=-(\mathrm{Gr}-\mathrm{Gr}^{\mathsf T})/2$ and $\mathscr L(\gamma_O)=-\gamma_O$. $\square$

The component $\mathrm{Gr}_K$ carries the entire trace $t$. The diagonal of $\mathrm{Gr}_V$ is $\boldsymbol\eta$, while those of $\mathrm{Gr}_P$ and $\mathrm{Gr}_O$ are zero. V therefore describes precisely the nonuniformity of the Green diagonal; in resistance geometry, this is the nonuniformity of quadratic distances to the centroid.

Coefficient orthogonality in KVP/KVPO concerns the inner product of pair tables defined in the projector notes. It does not imply metric orthogonality of PMG objects. Individual components of $\mathrm{Gr}$ are not assumed to inherit the positivity of the whole graph's metric either.

## Symmetric resistances: mean, vertex contribution, and residual

For now, the graph is undirected. **Definition.** The resistance of a pair is the quadratic norm of its vector:

$$
R_{ij}=(a_i-a_j)^2
=q_i+q_j-2\mathrm{Gr}_{ij},
\qquad R=\mathcal D(\mathrm{Gr})
$$

This is the effective resistance of the pair, not the resistance of an individual edge. The linear distance in a Euclidean realization is $\sqrt{R_{ij}}$.

> [!info] Symmetric resistances: mean, vertex contribution, and residual
> **Theorem.** The components of $R$ are related to the pair coefficients of the Green matrix by
>
> $$
> \boxed{
> R_K=2n\gamma_K,\qquad
> R_V=n\gamma_V,\qquad
> R_P=2\gamma_P
> }
> \tag{4}
> $$

> [!note]- Proof
> **Proof.** Substitute $\mathrm{Gr}=\mathscr L(\gamma)$ into $R=\mathcal D(\mathrm{Gr})$. The composition $\mathcal D\circ\mathscr L$ has multipliers $2n,n,2$ on the pair sectors K, V, P, as proved in [[The Distance Operator and KVP Decomposition#Action on KVP and KVPO|the formula for the action on components]]. $\square$

Expanding (4), for $i\ne j$ we obtain

$$
(R_K)_{ij}=\frac{2t}{n-1},
\qquad
(R_V)_{ij}=\frac{n}{n-2}(\eta_i+\eta_j),
\qquad
R_P=R-R_K-R_V
\tag{5}
$$

The row sums $s_i=\sum_jR_{ij}$ provide an independent way to obtain the same parameters:

$$
s_i=nq_i+t,
\qquad
\frac1n\sum_i s_i=2t,
\qquad
v_i^{(R)}=s_i-2t=n\eta_i
$$

Three interpretations follow.

- **K specifies the mean resistance.** The Kirchhoff index is $\operatorname{Kf}=\sum_{i<j}R_{ij}=nt$, so $\mu_R=\operatorname{Kf}/\binom n2$. As a linear functional of $R$, the Kirchhoff index depends only on its K-component.
- **V specifies the heterogeneity of total resistance distance.** The condition $R_V=0$ is equivalent to constancy of $q_i$ and of $s_i$. It concerns the metric of the whole graph. Regularity of the original couplings, $C_V=0$, is checked on a different table.
- **P specifies the residual symmetric pair structure.** It has zero row sums. Its values describe what cannot be represented as an overall level plus two vertex contributions.

In particular, for four pairwise distinct vertices,

$$
\begin{aligned}
(ab)\cdot(cd)
&=\frac12(R_{ad}+R_{bc}-R_{ac}-R_{bd})\\
&=\frac12\bigl((R_P)_{ad}+(R_P)_{bc}-(R_P)_{ac}-(R_P)_{bd}\bigr)
\end{aligned}
\tag{6}
$$

The K- and V-contributions cancel. Such cancellation generally fails for vectors sharing a vertex. The connection of (6) with four-electrode measurements, completeness of such data for P, and an exact model of contact corrections are discussed in [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]].

## Why coupling components cannot be inverted independently

The sequence of transformations is

$$
C\ \xrightarrow{\ \mathscr L\ }\ L
\ \xrightarrow{\ +\ }\ \mathrm{Gr}
\ \xrightarrow{\ \mathcal D\ }\ R
$$

The first and last transformations are linear. Pseudoinversion in the middle is nonlinear: in general,

$$
\mathrm{Gr}\ne L_K^++L_V^++L_P^+
$$

Consequently, formula (4) does not become $R_K=2nC_K$ or analogous equalities for V and P. It involves $\gamma$, not $C$.

For example, when couplings vary while connectedness is preserved, the usual derivative formula for an inverse matrix holds on $H$:

$$
\delta\mathrm{Gr}=-\mathrm{Gr}(\delta L)\mathrm{Gr},
\qquad
\delta R=\mathcal D(\delta\mathrm{Gr})
\tag{7}
$$

This is a differential, not an exact formula for a finite difference. Even if $\delta C$ lies in one KVP-sector, multiplication on both sides by $\mathrm{Gr}$ need not preserve that sector.

Thus “the Kirchhoff index is determined by the K-component of $R$” does not mean that it is determined by $C_K$ alone. Neither the spanning-tree coefficient nor resistance radius becomes additive over coupling components without a separate proof. A graph with $C_P=0$ but $R_P\ne0$ is given below.

## A balanced graph: three different resistance tables

Now $C$ may be nonsymmetric but remains balanced. The Green matrix and $\gamma$ are defined by the same formulas, and the decomposition of $\mathrm{Gr}$ is KVPO.

> [!info] A balanced graph: three different resistance tables
> **Definition.** In the centroid normalization adopted in PMG, one-way resistance is defined by the potential of the form
>
> $$
> \Phi_{ij}=[a_j-h,a_j-a_i],
> \qquad
> r_{ij}=P_M(\Phi_{ij})=q_j-\mathrm{Gr}_{ij}
> \tag{8}
> $$
>
> Here $M$ is the graph's metric polyform, and $P_M(F)=\tau(MF)/\tau(M)$ is the normalized potential. The definition, argument order, and subsequent hitting-time interpretation are given in [[One-Way Resistance and Hitting Times]].

> [!info] A balanced graph: three different resistance tables
> **Definition.** Denote the symmetric pair resistance and balanced distance table, respectively, by
>
> $$
> \boxed{
> R_{ij}=r_{ij}+r_{ji}
> =q_i+q_j-\mathrm{Gr}_{ij}-\mathrm{Gr}_{ji}
> }
> \tag{9}
> $$
>
> $$
> \boxed{
> \widetilde r_{ij}=\frac12\mathcal D(\mathrm{Gr})_{ij}
> =\frac{q_i+q_j}{2}-\mathrm{Gr}_{ij}
> }
> \tag{10}
> $$

The table $R$ is symmetric; $\widetilde r$ is generally nonsymmetric. In particular, $\mathcal D(\mathrm{Gr})=2\widetilde r$, but usually $\mathcal D(\mathrm{Gr})\ne R$ and $\widetilde r\ne r$.

If $\mathrm{Gr}_{\mathrm s}=(\mathrm{Gr}+\mathrm{Gr}^{\mathsf T})/2$, then

$$
R=\mathcal D(\mathrm{Gr}_{\mathrm s}),
\qquad
R=\widetilde r+\widetilde r^{\mathsf T}
$$

Formulas (4)-(5) for the symmetric components of $R$ remain valid for a balanced graph: the O-component of $\gamma$ disappears under symmetrization. In general, however, $\mathrm{Gr}_{\mathrm s}\ne((L+L^{\mathsf T})/2)^+$. Resistances of a balanced graph cannot be computed by simply averaging the original arcs before inversion.

## The origins of O and U in one-way resistances

> [!info] The origins of O and U in one-way resistances
> **Theorem.** The table $r$ has the KVPOU decomposition
>
> $$
> \boxed{
> r_K=\frac12R_K,\qquad
> r_V=\frac12R_V,\qquad
> r_P=\frac12R_P
> }
> $$
>
> $$
> \boxed{
> r_O=-\frac{\mathrm{Gr}-\mathrm{Gr}^{\mathsf T}}2,
> \qquad
> (r_U)_{ij}=\frac{q_j-q_i}{2}
> }
> \tag{11}
> $$

> [!note]- Proof
> **Proof.** The symmetric part of $r$ equals $R/2$, giving the first three components. From $r=\mathbf1\mathbf q^{\mathsf T}-\mathrm{Gr}$, its sums are
>
> $$
> d_i^{out}(r)=t,
> \qquad
> d_i^{in}(r)=nq_i
> $$
>
> The definitions of the KVPOU parameters give
>
> $$
> v_i^{(r)}=\frac n2\eta_i,
> \qquad
> u_i^{(r)}=\frac{t-nq_i}{2}=-\frac n2\eta_i=-v_i^{(r)}
> $$
>
> Hence $(r_U)_{ij}=(u_i^{(r)}-u_j^{(r)})/n=(q_j-q_i)/2$. The skew-symmetric part of $r$ is
>
> $$
> \frac{r-r^{\mathsf T}}2
> =r_U-\frac{\mathrm{Gr}-\mathrm{Gr}^{\mathsf T}}2
> $$
>
> The second term has zero row sums, so it is $r_O$. $\square$

The decomposition separates two sources of asymmetry in $r$.

- **U arises from unequal diagonal entries of the Green matrix.** This component may be nonzero even for an undirected graph. It describes imbalance of the table $r$, not of the original coupling table $C$.
- **O retains the skew-symmetric part of the Green matrix.** It describes the circulation part of the metric response. For a connected balanced graph, $r_O=0$ if and only if $C$ is symmetric: pseudoinversion preserves symmetry in both directions.

The sum of U-coefficients around any closed walk is zero. Thus the circulation norm from [[One-Way Resistance and Hitting Times#Pair resistance and circulation|the definition using a traversal of a triple]] depends only on O:

$$
\chi_{ijk}
=2\bigl((r_O)_{ij}+(r_O)_{jk}+(r_O)_{ki}\bigr)
$$

> [!info] The origins of O and U in one-way resistances
> **Corollary.** For the one-way resistance table of a connected balanced graph,
>
> $$
> r_U=0\quad\Longleftrightarrow\quad r_V=0
> \quad\Longleftrightarrow\quad q_1=\cdots=q_n
> \tag{12}
> $$
>
> This is a special property of $r$, not a property of arbitrary KVPOU decompositions. It does not mean that balance eliminates V in every table. In particular, $\widetilde r$ is always balanced, while its V may be nonzero.
>
> For an undirected graph, $r_O=0$, but
>
> $$
> r_{ij}=\frac{R_{ij}+q_j-q_i}{2}
> $$
>
> Thus usually $r\ne R/2$. Equality holds exactly when $q_i$ is constant. The term “one-way resistance” also applies in this case.

## Comparing components and recovering data

Formulas (10)-(11) imply

$$
\boxed{\widetilde r=r-r_U=\frac12R+r_O}
\tag{13}
$$

Its row and column sums coincide and equal $(nq_i+t)/2$. Removing U therefore makes the table balanced while preserving K, V, P, and O.

The multipliers can be collected in one table. Here $\gamma$ denotes the pair coefficients of the Green matrix from (2), not the original couplings.

| Table | K | V | P | O | U |
| --- | --- | --- | --- | --- | --- |
| $\gamma$ | $\gamma_K$ | $\gamma_V$ | $\gamma_P$ | $\gamma_O$ | $0$ |
| $R$ | $2n\gamma_K$ | $n\gamma_V$ | $2\gamma_P$ | $0$ | $0$ |
| $r$ | $n\gamma_K$ | $\frac n2\gamma_V$ | $\gamma_P$ | $\gamma_O$ | $(q_j-q_i)/2$ |
| $\widetilde r$ | $n\gamma_K$ | $\frac n2\gamma_V$ | $\gamma_P$ | $\gamma_O$ | $0$ |

Both $r$ and $\widetilde r$ determine the full Green matrix:

$$
\boxed{\mathrm{Gr}=-Jr=-J\widetilde rJ}
\tag{14}
$$

The first equality follows from $J\mathbf1=0$ and centering of $\mathrm{Gr}$. The second follows by double centering in (10). Removing U from $r$ loses no information about the graph, because here U is determined by the same data $\boldsymbol\eta$ already present in V.

By contrast, the symmetric table $R$ recovers only

$$
\boxed{\mathrm{Gr}_{\mathrm s}=-\frac12JRJ}
$$

Recovering a balanced graph also requires the circulation part:

$$
\mathrm{Gr}=-\frac12JRJ-r_O,
\qquad
L=\mathrm{Gr}^+,
\qquad
C_{ij}=-L_{ij}\quad(i\ne j)
$$

Ordinary double centering of $R$ does not recover the lost O-component. The unit directed 3-cycle illustrates this loss.

## Examples: five different effects

![[Graphs for Green and resistance decompositions.svg]]

*The figure shows the four original examples: a path, a weighted undirected graph, a directed 3-cycle, and a directed 3-cycle with a bidirectionally attached vertex. Unspecified weights of existing couplings are 1. The path has asymmetric one-way resistances without circulation; the weighted graph acquires P after inversion; the directed cycle illustrates the loss of O on passing to R; the last balanced graph gives all five components of r. An additional regular weighted example is specified below by its conductance matrix.*

### A unit-weight path: U without orientation of the original graph

For the path $a-b-c-d$, direct calculation gives

$$
\mathrm{Gr}=\frac18
\begin{pmatrix}
7&1&-3&-5\\
1&3&-1&-3\\
-3&-1&3&1\\
-5&-3&1&7
\end{pmatrix},
\qquad
R=\begin{pmatrix}
0&1&2&3\\
1&0&1&2\\
2&1&0&1\\
3&2&1&0
\end{pmatrix}
$$

We have $t=5/2$ and $\boldsymbol\eta=(1,-1,-1,1)/4$. The table lists all independent coefficients in the decomposition of $R$.

| Pair | $R_{ij}$ | $(R_K)_{ij}$ | $(R_V)_{ij}$ | $(R_P)_{ij}$ |
| --- | ---: | ---: | ---: | ---: |
| $ab$ | $1$ | $5/3$ | $0$ | $-2/3$ |
| $ac$ | $2$ | $5/3$ | $0$ | $1/3$ |
| $ad$ | $3$ | $5/3$ | $1$ | $1/3$ |
| $bc$ | $1$ | $5/3$ | $-1$ | $1/3$ |
| $bd$ | $2$ | $5/3$ | $0$ | $1/3$ |
| $cd$ | $1$ | $5/3$ | $0$ | $-2/3$ |

Meanwhile,

$$
r=\frac14
\begin{pmatrix}
0&1&3&6\\
3&0&2&5\\
5&2&0&3\\
6&3&1&0
\end{pmatrix}
$$

For example, $r_{ab}=1/4$ whereas $r_{ba}=3/4$. Here $r_O=0$, but $(r_U)_{ab}=-1/4$. The entire asymmetry comes from the difference between $q_a=7/8$ and $q_b=3/8$.

Moreover, $\gamma_{ab}=-\mathrm{Gr}_{ab}=-1/8<0$: the pair coefficients of the Green matrix are no longer positive couplings of the original path. For disjoint vectors $(ab)$ and $(cd)$, formula (6) gives $(ab)\cdot(cd)=0$, obtained both directly from R and using only its P-component.

### A weighted graph: P appears after inversion

Take $b=(0,0,1,1)$ and set $C_{ij}=b_i+b_j$ for $i\ne j$. Then

$$
C=\begin{pmatrix}
0&0&1&1\\
0&0&1&1\\
1&1&0&2\\
1&1&2&0
\end{pmatrix}
$$

This graph is connected: four unit couplings join the parts $\{a,b\}$ and $\{c,d\}$, and coupling $cd$ has weight 2. C is additive in pair endpoints, so $C_P=0$.

However, the resistances are

$$
R=\frac1{12}
\begin{pmatrix}
0&12&7&7\\
12&0&7&7\\
7&7&0&4\\
7&7&4&0
\end{pmatrix}
$$

Here $\mu_R=11/18$. On pairs $ab,ac,ad,bc,bd,cd$, we obtain

$$
R_V:\quad\left(\frac13,0,0,0,0,-\frac13\right),
\qquad
R_P:\quad\frac1{36}(2,-1,-1,-1,-1,2)
$$

Thus $R_P\ne0$ although $C_P=0$. This directly disproves preservation of the set of nonzero KVP-components when passing from couplings to resistances.

### A regular weighted graph: V appears in resistances

On vertices $a,b,c,d,e$, specify the symmetric conductance table

$$
C=\begin{pmatrix}
0&2&0&1&1\\
2&0&1&0&1\\
0&1&0&2&1\\
1&0&2&0&1\\
1&1&1&1&0
\end{pmatrix}
$$

The graph is connected, all weights are nonnegative, and every weighted degree equals 4. Hence $\mu_C=1$, $v^{(C)}=0$, and $C_V=0$.

Inverting the Laplacian on the centered space gives

$$
\mathbf q=\frac1{525}(94,94,94,94,84)^{\mathsf T},
\qquad
t=\frac{92}{105},
\qquad
v^{(R)}=5\mathbf q-t\mathbf1
=\frac1{105}(2,2,2,2,-8)^{\mathsf T}
$$

Thus $\mu_R=46/105$, and the V-component of the resistance table is nonzero:

$$
(R_V)_{ij}=
\begin{cases}
4/315,&i,j\in\{a,b,c,d\},\ i\ne j\\
-2/105,&\text{one vertex of the pair is }e
\end{cases}
$$

In particular, $R_{ab}=R_{cd}=12/35$, $R_{ac}=R_{bd}=8/15$, $R_{ad}=R_{bc}=10/21$, and all four $R_{ie}$ equal $44/105$. These values are independently obtained by solving Kirchhoff systems with unit current between the selected vertices.

Thus $C_V=0$ does not imply $R_V=0$: equal weighted degrees do not ensure equal Green diagonal entries or total resistances. Here vertex e has a smaller quadratic distance to the centroid than the other four vertices. Regularity of couplings and uniformity of resistance data concern different tables.

### The unit directed 3-cycle: symmetric resistances lose O

For $a\to b\to c\to a$,

$$
\mathrm{Gr}=\frac13
\begin{pmatrix}
1&0&-1\\
-1&1&0\\
0&-1&1
\end{pmatrix},
\qquad
r=\frac13
\begin{pmatrix}
0&1&2\\
2&0&1\\
1&2&0
\end{pmatrix}
$$

All $q_i=1/3$, so $r_V=r_U=0$. On three vertices, the P-sector is zero. Only K and O remain:

$$
(r_K)_{ij}=\frac12\quad(i\ne j),
\qquad
r_O=\frac16
\begin{pmatrix}
0&-1&1\\
1&0&-1\\
-1&1&0
\end{pmatrix}
$$

The symmetric resistances are $R_{ij}=1$ for all distinct pairs, so $R=R_K$. Reversing the directed cycle transposes $r$, changes the sign of O, and leaves $R$ unchanged. Thus R alone cannot determine the traversal direction.

Here $r=\widetilde r$, but $\mathcal D(\mathrm{Gr})=2r\ne R$. The circulation norm is $\chi_{abc}=-1$: the sum along $a\to b\to c\to a$ is 1, while the reverse sum is 2.

### A nonregular balanced graph: all five components of r

Add two unit arcs $a\to d$ and $d\to a$ to the same directed 3-cycle. Incoming and outgoing degrees coincide and equal $(2,1,1,1)$. The graph is balanced but nonregular.

Direct calculation gives

$$
\mathrm{Gr}=\frac14
\begin{pmatrix}
1&0&-1&0\\
-1&2&1&-2\\
0&-1&2&-1\\
0&-1&-2&3
\end{pmatrix},
\qquad
r=\frac14
\begin{pmatrix}
0&2&3&3\\
2&0&1&5\\
1&3&0&4\\
1&3&4&0
\end{pmatrix}
$$

Here $q=(1/4,1/2,1/2,3/4)$ and $t=2$. The row sums of r are $(2,2,2,2)$, while its column sums are $(1,2,2,3)$. The one-way resistance table is therefore unbalanced even though the original graph is balanced.

| Pair | $r_{ij}$ | $(r_K)_{ij}$ | $(r_V)_{ij}$ | $(r_P)_{ij}$ | $(r_O)_{ij}$ | $(r_U)_{ij}$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $ab$ | $1/2$ | $2/3$ | $-1/4$ | $1/12$ | $-1/8$ | $1/8$ |
| $ac$ | $3/4$ | $2/3$ | $-1/4$ | $1/12$ | $1/8$ | $1/8$ |
| $ad$ | $3/4$ | $2/3$ | $0$ | $-1/6$ | $0$ | $1/4$ |
| $bc$ | $1/4$ | $2/3$ | $0$ | $-1/6$ | $-1/4$ | $0$ |
| $bd$ | $5/4$ | $2/3$ | $1/4$ | $1/12$ | $1/8$ | $1/8$ |
| $cd$ | $1$ | $2/3$ | $1/4$ | $1/12$ | $-1/8$ | $1/8$ |

On reversed pairs, K, V, and P are unchanged, while O and U change sign. For example,

$$
r_{ad}=\frac23-\frac16+\frac14=\frac34,
\qquad
r_{da}=\frac23-\frac16-\frac14=\frac14
$$

For pair $ad$, the O-contribution is zero: the difference between these two values belongs entirely to U. After removing U, $\widetilde r$ has equal incoming and outgoing sums $(3/2,2,2,5/2)$. Its V-component remains nonzero. This example shows why balance of the original graph, balance of the resistance table, and regularity must be distinguished.

## Status of results and further uses

Decompositions (3)-(5), (11)-(13), and recovery formulas (14) are proved under the stated assumptions. The five examples were computed using exact rational arithmetic. The formulas were additionally checked on 40 symmetric and balanced graphs with 3-7 vertices. For an independent check, each column of r was obtained from

$$
L_{\widehat j,\widehat j}\,r_{\widehat j,j}=\frac1n\mathbf1,
\qquad r_{jj}=0
$$

The results agreed with computation through the Green matrix; the components were then extracted directly from the row and column sums of the tables. These computational checks complement the proofs.

For an arbitrary unbalanced digraph, the algebraic KVPOU decomposition of pair data remains valid. However, this note's formulas for $L^+$, $r$, and their recovery use balance of the Laplacian and cannot be carried over unchanged. One way to obtain a balanced model is described in [[Balancing a Directed Graph by Spanning-Tree Potentials]]; the table being decomposed then belongs to the chosen model.

Linear transformations are compared in [[The Distance Operator and KVP Decomposition]], and the geometric meaning of one-way resistances and circulation is explained in [[One-Way Resistance and Hitting Times]] and [[Resistance Geometry and Circulation]]. [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]] gives computed examples and limits of applied interpretations. [[KVP Components and Metric Graph Parameters]] connects the decomposition with centralities, radius, center bi-coordinates, and spanning-tree sensitivities, distinguishing contributions at a fixed metric from nonlinear dependencies.

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
