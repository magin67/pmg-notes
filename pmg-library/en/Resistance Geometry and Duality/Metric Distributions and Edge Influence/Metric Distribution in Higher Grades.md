---
title: Metric Distribution in Higher Grades
date: 2026-11-03
updated: 2026-11-03
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 3
translation_key: metric-distributions-higher-grades
order: 4
description: "The norm of a triangle boundary, distribution over edge pairs, and recovery of individual-edge influence; extending D to every grade."
---

[[ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/Метрическое распределение высших грейдов|Русский]]


Adding a coupling also changes a triangle's norm. The influence-measurement procedure remains the same: fix the form, change one conductance, and compare values. In grade two, however, the metric distribution is indexed by pairs of edges. The influence of one edge is obtained by summing over all pairs containing it.

For vectors these two levels coincided: one distribution coefficient belonged to one edge. Here the contribution of a pair must be distinguished from the total influence of an edge. This extends the operator in [[Edge Influence and Metric Distribution]], with the same variation mechanism and with the grade of the output form preserved.

## Triangle norm and a probe of one coupling

Let the graph be finite, connected, and undirected, with fixed vertices and positive conductances on existing edges. Write $a_\ell=a_j-a_i$, $q_\ell=[a_\ell]^2$, and $L=\sum_\ell c_\ell q_\ell$. All inner products refer to the resistance metric of $L$.

The metric evaluation $N_L(f)=\tau((\exp L)f)/\tau(\exp L)$ is defined by the normalized potential in [[Laplacian Exponential]]. For a form $[X,Y]$ on boundaries, it equals $X\cdot Y$.

A triangle boundary has grade two:

$$
X=(abc)=(ab)(ac)=vw,\qquad v=(ab),\quad w=(ac)
$$

By [[Metric of Higher-Grade Objects]], its norm is a Gram determinant:

$$
N_L([X]^2)=X^2=v^2w^2-(v\cdot w)^2
$$

Under the PMG convention, this is a quadratic quantity. The square of the ordinary triangle area in resistance geometry is $X^2/4$. The graph diagrams below show couplings, not that geometric realization.

For the fixed form $f=[X]^2$, denote the sensitivity of an existing edge by $A_\ell$. The single-variation formula applies to a form of any grade:

$$
A_\ell(f)=-c_\ell\frac{\partial N_L(f)}{\partial c_\ell}
=c_\ell\bigl(R_\ell N_L(f)-N_L(fq_\ell)\bigr),
\qquad R_\ell=N_L(q_\ell)
$$

For a relative change $c'_\ell=(1+\varepsilon)c_\ell$, the exact finite influence is

$$
\Delta_\ell(\varepsilon c_\ell;f)
=-\frac{\varepsilon A_\ell(f)}{1+\varepsilon c_\ell R_\ell}
\tag{1}
$$

All quantities on the right are evaluated in the initial metric. Final conductances must be nonnegative, and the graph must remain connected. As in [[Edge Influence and Metric Distribution]], every independent probe starts from the same initial graph. For an absent coupling, use the addition formula in that note without dividing by the initial conductance.

## From two responses to edge pairs

For each edge, find two metric responses:

$$
s_\ell=v\cdot a_\ell,\qquad t_\ell=w\cdot a_\ell
$$

The inner product of exterior objects is evaluated by a determinant:

$$
X\cdot(a_\ell a_m)=s_\ell t_m-s_m t_\ell
$$

> [!info] Distribution in grade two
> **Definition.** For $f=[vw]^2$, the contribution of an unordered pair of distinct edges is
>
> $$
> \boxed{m_{\ell m}(f)=c_\ell c_m(s_\ell t_m-s_m t_\ell)^2}
> \tag{2}
> $$
>
> With a fixed ordering of the edges, assemble these coefficients into a form:
>
> $$
> D_{L,2}(f)=\sum_{\ell<m}m_{\ell m}(f)q_\ell q_m
> $$

The form $q_\ell q_m=[a_\ell a_m]^2$ has grade two. The edges in a pair need not be adjacent. Exchanging the edges or reversing their auxiliary orientations changes neither the contribution nor the output form.

The determinant in (2) measures the difference between two response directions. If the pairs of numbers $(s_\ell,t_\ell)$ and $(s_m,t_m)$ are proportional, the contribution is zero, even when both edges participate in both vector responses.

Two different sums hold for the triangle norm:

$$
\boxed{\sum_{\ell<m}m_{\ell m}(f)=N_L(f),\qquad
A_\ell(f)=\sum_{m\ne\ell}m_{\ell m}(f)}
\tag{3}
$$

The first decomposes the norm; the second recovers the influence of one edge. Hence

$$
\sum_\ell A_\ell(f)=2N_L(f)
$$

Each pair is counted twice. If an edge diagram whose labels sum to the norm is needed, the labels may be $A_\ell/2$, but the relative-sensitivity coefficient in (1) remains $A_\ell$. Edge probes alone do not specify a decomposition into pairs; in (2), the exterior product and metric specify it. A proof of (3) for every grade is given below.

## Which pairs are selected on a tree

On a tree, the edge vectors form an orthogonal basis, with $a_\ell^2=1/c_\ell$. This property was used in [[Path Intersection as an Influence Field on a Tree]]. For a triangle boundary, it gives the following analogue of the tree rule.

> [!info] Separating three vertices
> **Proposition.** For $X=(abc)$ on a tree, the nonzero contributions come from exactly those pairs whose deletion places $a,b,c$ in three different components. For such a pair,
>
> $$
> m_{\ell m}([X]^2)=\frac1{c_\ell c_m}
> $$

> [!note]- Proof of the tree criterion
> **Proof.** Expand $v=(ab)$ and $w=(ac)$ in the edge basis. Their coordinates are $0,1,-1$ and mark the unique paths. The coefficient of $a_\ell a_m$ in $vw$ is a minor of these two coordinate rows. It is nonzero exactly when deleting the two edges separates the three marked vertices; in that case it is $\pm1$. Orthogonality gives $(a_\ell a_m)^2=1/(c_\ell c_m)$. Substitution into (2) proves the claim. $\square$

Consider a tree with center $h$ and leaves $a,b,c,d$:

$$
c_{ha}=1,\qquad c_{hb}=2,\qquad c_{hc}=3,\qquad c_{hd}=1
$$

For $X=(abc)$, there are three nonzero contributions:

$$
m_{ha,hb}=\frac12,\qquad m_{ha,hc}=\frac13,\qquad
m_{hb,hc}=\frac16,\qquad X^2=1
$$

![Three edge pairs separating the marked vertices of the tree](<images/Triangle Pair Contributions on a Tree.svg>)

*Dashed lines mark the deleted pair. In each case vertices $a,b,c$ end up in different components. Numbers beside edges are the initial conductances; numbers below the diagrams are pair contributions. Branch $hd$ belongs to no pair with a nonzero contribution.*

Direct evaluation in the metric gives $v^2=3/2$, $w^2=4/3$, and $v\cdot w=1$, so $X^2=(3/2)(4/3)-1=1$. The edge sums are

$$
(A_{ha},A_{hb},A_{hc},A_{hd})=
\left(\frac56,\frac23,\frac12,0\right)
$$

Increasing the conductance of $hb$ from $2$ to $4$ gives $c_{hb}R_{hb}=1$, so by (1) the new norm is $1-(2/3)/2=2/3$. Changing only $hd$ does not affect the norm as long as connectedness is preserved.

Finite changes of different edges can interact even on a tree. For the path $a-b-c$ with conductances $x,y>0$, we have $N_L([(abc)]^2)=1/(xy)$. At $x=y=1$ the norm is $1$; doubling either conductance alone gives $1/2$, while doubling both gives $1/4$. Adding the two independent increments would incorrectly give $1-1/2-1/2=0$. The additivity in the [[Path Intersection as an Influence Field on a Tree#Detecting the intersection by edge probes|tree note]] concerns inner products of grade one and does not extend to higher grades.

What is selected here is a family of pairs separating three vertices. It should not be drawn as one triangular intersection region: the output consists of edge-pair forms, interpreted through their metric contributions.

## A zero pair contribution with nonzero edge influences on a square

Take the unit cycle $a-b-c-d-a$ and the same input $X=(abc)$. For the calculation, choose orientations $ab,bc,cd,ad$. The responses of the two vectors are

$$
(s_\ell)=\frac14(3,-1,-1,1),\qquad
(t_\ell)=\frac12(1,1,-1,1)
$$

Formula (2) gives:

| Edge pair | Contribution $m_{\ell m}$ |
|---|---:|
| $ab,bc$ | $1/4$ |
| $ab,cd$ | $1/16$ |
| $ab,ad$ | $1/16$ |
| $bc,cd$ | $1/16$ |
| $bc,ad$ | $1/16$ |
| $cd,ad$ | $0$ |

Their sum is $X^2=1/2$. An independent check gives $v^2=3/4$, $w^2=1$, and $v\cdot w=1/2$, hence $X^2=3/4-1/4=1/2$.

![Pair contributions and edge sums for a triangle boundary on a square](<images/Pairs and Edge Influence on a Square.svg>)

*On the left are the coefficients of unordered pairs, with each pair counted once. On the right are the sums $A_\ell$ over all pairs containing an edge. The input boundary has vertices $a,b,c$; vertex $d$ belongs to the network and affects its metric.*

On $cd$ and $ad$, the response pairs are opposite, so their determinant vanishes. At the same time,

$$
(A_{ab},A_{bc},A_{cd},A_{ad})=
\left(\frac38,\frac38,\frac18,\frac18\right)
$$

Both edges $cd,ad$ influence the norm through pairs with other edges. A zero pair contribution means neither zero influence of each edge nor the absence of a joint finite effect.

For a mixed input $f=\{X,Y\}/2$, the squared determinant is replaced by a product of two determinants. Contributions can have different signs. For example, for $X=(abc)$ and $Y=(abd)$ on this square, $m_{ab,cd}=-1/16$, although $X\cdot Y=1/4$. A consistently oriented shared side of two triangles does not guarantee that all contributions are positive.

## Edge influence on a triangle norm

The effective resistance between the endpoints of every edge of the unit square is $3/4$. When one conductance is doubled, formula (1) becomes

$$
\Delta_\ell(c_\ell;[X]^2)=-\frac47A_\ell([X]^2)
$$

Doubling $ab$ or $bc$ changes the norm from $1/2$ to $2/7$. Doubling $cd$ or $ad$ changes it to $3/7$. Edges in the first pair have three times the influence under these equal relative probes.

![Independent conductance changes on a square and the new triangle norm](<images/Triangle Norm Probes on a Square.svg>)

*Color and the number $2$ mark the single strengthened edge. Both probes start independently from the initial unit square. The labels below the drawings give the norm of boundary $(abc)$, not the area of the drawn region.*

The full pair distribution shows which combinations make up an edge's influence. Computing the $A_\ell$ themselves does not require listing all pairs. Set $\alpha=v^2$, $\beta=v\cdot w$, and $\gamma=w^2$. Then

$$
\boxed{A_\ell([vw]^2)=c_\ell
\bigl(\gamma s_\ell^2-2\beta s_\ell t_\ell+\alpha t_\ell^2\bigr)}
\tag{4}
$$

This follows by summing (2): the grade-one identity gives $\sum_m c_ms_m^2=\alpha$, $\sum_m c_mt_m^2=\gamma$, and $\sum_m c_ms_mt_m=\beta$. For the square, formula (4) returns $3/8,3/8,1/8,1/8$.

### The edge field does not determine pair contributions

On the unit square, consider two forms:

$$
f_1=[(abc)]^2+[(acd)]^2,\qquad
f_2=[(abd)]^2+[(bcd)]^2
$$

Both have value $1$ and the same field $A_{ab}=A_{bc}=A_{cd}=A_{ad}=1/2$. However, $m_{ab,bc}(f_1)=1/4$, whereas $m_{ab,bc}(f_2)=1/8$. These values follow from (2) by adding the contributions of two squares; formula (4) independently gives identical edge sums.

Since the initial $R_\ell$ are also identical, (1) gives identical results for every admissible independent finite probe of one existing edge. The pair distributions nevertheless differ. The edge field is obtained by summing pair contributions, but those contributions cannot in general be recovered from the field alone.

## One definition for every grade

Let $X,Y\in\Lambda^kW$, where $W$ is the affine-vector space. For an unordered set $J$ of $k$ distinct existing edges, set

$$
B_J=\prod_{\ell\in J}a_\ell,\qquad
q_J=[B_J]^2,\qquad w_J=\prod_{\ell\in J}c_\ell
$$

Choosing a different order of factors changes only the sign of $B_J$. If the set contains a cycle, $B_J=0$.

> [!info] Extending the metric distribution
> **Definition.** For a form $f=[X,Y]$, define
>
> $$
> \boxed{m_J(f)=w_J(X\cdot B_J)(Y\cdot B_J),\qquad
> D_{L,k}(f)=\sum_{|J|=k}m_J(f)q_J}
> \tag{5}
> $$
>
> The definition extends linearly to forms of grade $k$ and grade by grade to polyforms on boundaries. At $k=0$ it is the identity on scalars. At $k=1$ it gives $D_L$ from [[Edge Influence and Metric Distribution]].

This is one family indexed by grade. Bilinearity in $X,Y$ ensures independence from a decomposition of the input form. The coefficients for $\{X,Y\}/2$ are the same; the skew-symmetric part is annihilated. Existing edges and output vectors $a_j-a_i$ are fixed: an arbitrary change of edge representation is not part of the definition.

> [!info] Sum of contributions and edge influence
> **Theorem.** For a form $f$ of grade $k$ on boundaries,
>
> $$
> \boxed{\sum_{|J|=k}m_J(f)=N_L(f)}
> $$
>
> For an existing edge,
>
> $$
> A_\ell(f)=\sum_{J\ni\ell}m_J(f)
> =c_\ell\bigl(R_\ell N_L(f)-N_L(fq_\ell)\bigr)
> $$
>
> Thus the finite-influence formula (1) remains valid, and
>
> $$
> \boxed{\sum_\ell A_\ell(f)=kN_L(f)}
> $$
>
> For $f=[X]^2$, all $m_J$ and $A_\ell$ are nonnegative. Strengthening one coupling does not increase the norm of such an input.

The sum formula rests on the classical Cauchy-Binet formula; see R. Stanley, [Topics in Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/algcomb.pdf), Theorem 9.4. Below it is applied to the resistance metric; the relation to variations is derived through the normalized PMG potential.

> [!note]- Proof of the contribution sum
> **Proof.** The vectors $\sqrt{c_\ell}a_\ell$ satisfy the Parseval identity in grade one:
>
> $$
> \sum_\ell c_\ell(v\cdot a_\ell)(u\cdot a_\ell)=v\cdot u
> $$
>
> For decomposable $X=v_1\cdots v_k$ and $Y=u_1\cdots u_k$, apply the Cauchy-Binet formula to the matrix $(v_i\cdot u_j)$. The result is a sum of products of minors of $(v_i\cdot a_\ell)$ and $(u_i\cdot a_\ell)$ with weights $w_J$, that is, (5) after summation. Bilinearity extends the identity to arbitrary exterior objects and forms. Each unordered set is counted once, with no factor $k!$. For a square, every contribution is nonnegative. $\square$

> [!note]- Proof of the relation to variations
> **Proof.** At $k=0$, a scalar's evaluation is independent of the metric, and no empty set contains $\ell$, so $A_\ell=0$. Now let $k\ge1$; it suffices to consider $f=[X,Y]$. Set $u=a_\ell/\sqrt{R_\ell}$ and decompose
>
> $$
> X=uX_1+X_0,\qquad Y=uY_1+Y_0
> $$
>
> Here $X_1,Y_1\in\Lambda^{k-1}(u^\perp)$ and $X_0,Y_0\in\Lambda^k(u^\perp)$. Then
>
> $$
> R_\ell N_L(f)-N_L(fq_\ell)=R_\ell(X_1\cdot Y_1)
> $$
>
> Use [[Laplacian and Greenian - Mutual Duality of Exponentials#The interior product and deletion notation|contraction]] with the metric functional $a_\ell^\flat(z)=a_\ell\cdot z$. For every $B\in\Lambda^{k-1}W$, the definitions of contraction and the exterior metric give
>
> $$
> \iota_{a_\ell^\flat}X=\sqrt{R_\ell}X_1,\qquad
> (\iota_{a_\ell^\flat}X)\cdot B=X\cdot(a_\ell B)
> $$
>
> The same holds for $Y$, so the inner product of these contractions is $R_\ell(X_1\cdot Y_1)$. Applying the Parseval identity in grade $k-1$ to them gives
>
> $$
> \begin{aligned}
> c_\ell R_\ell(X_1\cdot Y_1)
> &=c_\ell\sum_{|K|=k-1}w_K
> \bigl(X\cdot(a_\ell B_K)\bigr)
> \bigl(Y\cdot(a_\ell B_K)\bigr)\\
> &=\sum_{J\ni\ell}m_J(f)
> \end{aligned}
> $$
>
> Terms with $\ell\in K$ vanish because the edge is repeated. The remaining terms correspond once each to sets $J=K\cup\{\ell\}$; the sign from reordering factors is the same in both inner products and cancels. This proves the formula for $A_\ell$.
>
> Every $m_J$ occurs in exactly $k$ edge sums, so their sum is $kN_L(f)$. Finally, since $q_\ell^2=0$, replacing $L$ by $L+tq_\ell$ gives
>
> $$
> N_{L+tq_\ell}(f)=\frac{N_L(f)+tN_L(fq_\ell)}{1+tR_\ell}
> $$
>
> Subtracting $N_L(f)$ recovers (1), and differentiation at $t=0$ gives $A_\ell=-c_\ell\partial N_L(f)/\partial c_\ell$. $\square$

On a tree the general result is especially simple. If $X=\sum_Jx_JB_J$ and $Y=\sum_Jy_JB_J$ in the exterior edge basis, then $m_J=x_Jy_J/w_J$. Common edges of two paths are replaced by common sets of $k$ edges in the expansions of exterior objects. This is an algebraic overlap of terms, with their signs and conductances taken into account.

## The sum, the output form, and limits of interpretation

The operator preserves grade. As in [[Edge Influence and Metric Distribution#Value of the output form|grade one]], the contribution sum equals the original value, while evaluation of the result includes the norms of the output forms:

$$
N_L(D_{L,k}(f))=\sum_Jm_J(f)N_L(q_J)
$$

| Graph and input $f=[X]^2$ | $N_L(f)=\sum_Jm_J$ | $\sum_\ell A_\ell$ | $N_L(D_{L,2}(f))$ |
|---|---:|---:|---:|
| Tree with center $h$, $X=(abc)$ | $1$ | $2$ | $7/18$ |
| Unit square, $X=(abc)$ | $1/2$ | $1$ | $1/4$ |
| Triangle graph, $c_{ab}=2,c_{bc}=3,c_{ac}=5$, $X=(abc)$ | $1/31$ | $2/31$ | $1/961$ |

In the last row, the spanning-tree coefficient is $\tau=2\cdot3+2\cdot5+3\cdot5=31$. The three pair contributions are $6/961,10/961,15/961$. All three output forms coincide with $[(abc)]^2$, so $D_{L,2}([(abc)]^2)=\frac1{31}[(abc)]^2$. It is useful to retain the pair labels together with the assembled form.

A pair contribution **is not a mixed second derivative** and does not measure a finite probe changing two couplings at once. For the triangle graph with conductances $x,y,z$, we have $N([(abc)]^2)=1/(xy+xz+yz)$. At $x=y=z=1$, the pair contribution is $1/9$, whereas $\partial^2N/\partial x\partial y=5/27$. Doubling both $x,y$ gives norm $1/8$; adding the two independently measured increments to the initial norm would incorrectly give $1/15$. Joint finite changes require the formulas in [[Two Edges and Joint Variation]] or recomputation of the metric.

## Computation and checks

For a triangle, two Laplacian solutions suffice to obtain $s_\ell,t_\ell$. One can then compute all pair determinants (2), or directly compute edge influences by (4). For a decomposable object $X=v_1\cdots v_k$, the calculation requires $k$ right-hand sides with one matrix and minors of order $k$. Computing $D_{L,k}$ does not require enumerating spanning trees; the full list can contain up to $\binom{|E|}{k}$ coefficients.

If only edge influences are needed and the Gram matrix $\mathbf G_X=(v_i\cdot v_j)$ is nonsingular, then with $h_\ell=(v_i\cdot a_\ell)_{i=1}^k$,

$$
A_\ell([X]^2)=c_\ell\det(\mathbf G_X)
h_\ell^{\mathsf T}\mathbf G_X^{-1}h_\ell
$$

This is the derivative of the Gram determinant with the metric change included. Formula (4) is its $k=2$ case. A finite probe additionally requires the initial $R_\ell$. The bound of $k$ solves applies to one decomposable object; an arbitrary input is processed linearly through its representation.

The general identities are proved above. Examples were checked in exact rational arithmetic by comparing exterior powers of the inverse Laplacian, an independent expansion of the normalized potential over forests of complementary grade, and direct recomputation of changed metrics. On nine graphs, 37 grades and 8024 scalar equalities for finite variations of forms were checked, including mixed inputs, addition of absent couplings, and admissible deletion. The [reproducible checks](https://github.com/magin67/pmg-notes/tree/v5/checks/metric-distributions) also test orientations and a nondecomposable exterior input. The forest formula independently checks the numerical evaluation; its individual forest contributions are not identified with the coefficients of $D_{L,k}$.

Exterior powers, the Cauchy-Binet formula, and differentiation of the metric justify the construction beyond tree examples. Expressing these identities in PMG and interpreting edge sums as an influence field do not establish scientific priority.

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distributions and Edge Influence|Back to Metric Distributions and Edge Influence]].
