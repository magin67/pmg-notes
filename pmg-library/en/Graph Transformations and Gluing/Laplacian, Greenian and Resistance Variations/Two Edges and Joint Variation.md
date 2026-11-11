---
title: Two Edges and Joint Variation
date: 2026-10-31
updated: 2026-11-11
revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: variations-two-edges-and-joint-variation
lang: en
description: Two changing triangle edges, explicit finite variations, and interaction. A derivation through Laplacian exponential factors, forest-potential normalization, and Gram determinants, extended to several couplings.
order: 2
translated_revision: 7
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/Two Edges and Joint Variation"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Две связи и совместная вариация|Русский]]

In [[One Changing Edge|the variation of one edge]], the spanning-tree coefficient and unnormalized potentials change linearly with the conductance increment. Changing two edges introduces a mixed term. We begin with a triangle, then give explicit formulas for two arbitrary pairs and derive them from the product of Laplacian exponential factors.

## Example - strengthening two edges of a triangle

See [[en/PythonExamples/Example - Laplacian, Greenian and Resistance Variations#Changing two conductances together|the notebook calculation]].

A unit triangle has $c_{12}=c_{13}=c_{23}=1$, $\tau=3$, and all its resistances equal $2/3$. Increase conductances $12$ and $13$ to $2$, keeping $c_{23}=1$.

![A unit triangle and the result of increasing conductances 12 and 13 to 2](<images/Two Changing Edges of a Triangle.svg>)

*Numbers beside edges denote conductances. The two varied edges are distinguished by different colors and greater thickness.*

The three spanning trees now have weights $4,2,2$, so $\tau'=8$. Between $1$ and $2$, the parallel paths have resistances $1/2$ and $3/2$; between $2$ and $3$, both paths have resistance $1$. Thus

$$
R'_{12}=R'_{13}=\frac{(1/2)(3/2)}{1/2+3/2}=\frac38,
\qquad R'_{23}=\frac{1\cdot1}{1+1}=\frac12
$$

Compare the joint change with two separate experiments, each starting from the original graph:

| Quantity | Original graph | Only $c_{12}=2$ | Only $c_{13}=2$ | Both conductances equal $2$ |
|---|---:|---:|---:|---:|
| $\tau$ | $3$ | $5$ | $5$ | $8$ |
| $R_{12}$ | $2/3$ | $2/5$ | $3/5$ | $3/8$ |
| $R_{13}$ | $2/3$ | $3/5$ | $2/5$ | $3/8$ |
| $R_{23}$ | $2/3$ | $3/5$ | $3/5$ | $1/2$ |

Adding the separate increments would give spanning-tree coefficient $3+2+2=7$ instead of $8$. For $R_{12}$, it would give $2/3-4/15-1/15=1/3$ instead of $3/8$. The joint result requires accounting for the interaction between changes.

> [!example] Explicit formulas for the triangle
> Set $c'_{12}=1+s$, $c'_{13}=1+t$, $c'_{23}=1$, where $s,t\ge-1$. Direct tree enumeration and parallel-path calculations give
>
> $$
> \tau'=3+2s+2t+st
> $$
>
> $$
> R'_{12}=\frac{2+t}{3+2s+2t+st},\qquad
> R'_{13}=\frac{2+s}{3+2s+2t+st}
> $$
>
> $$
> R'_{23}=\frac{2+s+t}{3+2s+2t+st}
> $$
>
> The resistance formulas require a nonzero denominator. In this domain, it vanishes only at $s=t=-1$: vertex $1$ becomes isolated. Either edge removal on its own preserves connectedness.

## Explicit formulas for two edges

Consider an undirected graph on fixed vertices $a_1,\ldots,a_n$ with nonnegative conductances. The graph formed by edges of positive conductance is assumed connected. Choose two distinct pairs $e_1,e_2$ and orient their vectors arbitrarily:

$$
u=a_{e_1},\qquad v=a_{e_2},\qquad
c'_{e_1}=c_{e_1}+s,\qquad c'_{e_2}=c_{e_2}+t
$$

Require $s\ge-c_{e_1}$ and $t\ge-c_{e_2}$. Keep the other conductances fixed. A prime denotes the new value, and $\Delta$ a finite increment. All unprimed metric data are calculated in the original graph.

> [!info] Data for a joint variation
> **Notation.** For the measured pair $ij$, set $w=a_{ij}$ and
>
> $$
> R_u=u^2,\qquad R_v=v^2,\qquad
> g=u\cdot v,\qquad x=w\cdot u,\qquad y=w\cdot v
> $$
>
> Here $R_u,R_v$ are the resistances between the endpoints of the two varied edges, and $w^2=R_{ij}$. The quantities $g,x,y$ are determined by the original resistances through polarization:
>
> $$
> a_{ij}\cdot a_{kl}
> =\frac{R_{il}+R_{jk}-R_{ik}-R_{jl}}2
> $$

Denote the common normalization factor by

$$
\Phi(s,t)=1+sR_u+tR_v+st(R_uR_v-g^2)
\tag{1}
$$

> [!info] Two response formulas
> The working formulas, derived below through exponential factors, are
>
> $$
> \boxed{\Delta\tau=\tau\bigl(sR_u+tR_v+st(R_uR_v-g^2)\bigr)}
> \tag{2}
> $$
>
> $$
> \boxed{
> \Delta R_{ij}=
> -\frac{s x^2+t y^2+st(R_vx^2+R_uy^2-2gxy)}{\Phi(s,t)}
> }
> \tag{3}
> $$
>
> The spanning-tree coefficient is $\tau'=\tau\Phi(s,t)$. For nonnegative final conductances, connectedness of the final graph is equivalent to $\Phi(s,t)>0$. This condition is required for (3); formula (2) remains valid when connectedness is lost.

Setting $t=0$ gives the formulas for [[One Changing Edge|one changing edge]]. Reversing $u$ changes the signs of $g$ and $x$; reversing $v$ changes the signs of $g$ and $y$. The entire answer, including the product $gxy$, is therefore independent of orientation.

For the triangle with $u=a_{12}$, $v=a_{13}$, we have $R_u=R_v=2/3$, $g=1/3$. Hence

$$
\Phi(s,t)=1+\frac23s+\frac23t+\frac13st
$$

When measuring $R_{12}$, the quantities are $x=2/3$, $y=1/3$. Substituting $s=t=1$ into (3) gives $\Delta R_{12}=-7/24$, that is, $R'_{12}=2/3-7/24=3/8$.

## Two factors and the mixed term

Let $L$ be the Laplacian polyform, $M=\exp L$ its exterior exponential, and $e$ the unit form. Set $p_1=[u]^2$, $p_2=[v]^2$. Then $L'=L+sp_1+tp_2$. All products in this section are polyform products; no matrix exponential is used.

> [!info] The product of two factors
> **Proposition.** The following exact identity holds:
>
> $$
> \boxed{M'=M(e+sp_1)(e+tp_2)}
> \tag{4}
> $$
>
> Expanding the product,
>
> $$
> M'=M+sMp_1+tMp_2+stMp_1p_2
> $$
>
> Grade by grade,
>
> $$
> M'_r=M_r+sM_{r-1}p_1+tM_{r-1}p_2+stM_{r-2}p_1p_2
> $$
>
> Here $0\le r\le n-1$ and $M_k=0$ for $k<0$.

> [!note]- Proof
> **Proof.** The forms commute, and $p_1^2=p_2^2=0$. Hence $\exp(sp_1)=e+sp_1$, $\exp(tp_2)=e+tp_2$. Multiplication and extraction of grade $r$ give (4) and its grade-wise version. $\square$

Each variable appears to at most the first power, but multiplying distinct factors produces the term $st$. Commutativity removes dependence on multiplication order while retaining mixed terms.

As in [[One Changing Edge#Extracting the spanning-tree coefficient from the factor|the one-factor derivation]], the functional $\tau(P)$ extracts the coefficient of the fixed spanning-tree form $T_n=[(a_1\ldots a_n)]^2$, and the potential of a form is $u_M(f)=\tau(Mf)$.

> [!info] Joint variation of a potential
> **Lemma.** For any fixed form $f$,
>
> $$
> \begin{aligned}
> u_{M'}(f)={}&u_M(f)+s\,u_M(fp_1)+t\,u_M(fp_2)\\
> &+st\,u_M(fp_1p_2)
> \end{aligned}
> \tag{5}
> $$

> [!note]- Proof
> **Proof.** Multiply (4) by $f$ and apply the linear functional $\tau$. Connectedness of the final graph is not required. $\square$

![Where the Mixed Term Comes From](<images/Where the Mixed Term Comes From.svg>)

*Only the triangle tree containing both changed edges contributes the product $st$. Repeating one edge within an exterior product gives zero.*

## The spanning-tree coefficient and the Gram determinant

In [[Laplacian Exponential#Agreement with the resistance metric|the metric identity]], the potential of a product of vector forms is expressed by the norm of the exterior product. In particular,

$$
u_M(p_1)=\tau R_u,\qquad
u_M(p_2)=\tau R_v,\qquad
u_M(p_1p_2)=\tau(R_uR_v-g^2)
$$

The last bracket equals the determinant

$$
\det\mathbf G(u,v)=
\det\begin{pmatrix}R_u&g\\g&R_v\end{pmatrix}
=R_uR_v-g^2
$$

This is the norm of the exterior product $uv$, geometrically the squared area of the parallelogram spanned by the two vectors in the original resistance metric.

> [!info] The spanning-tree coefficient under two changes
> **Corollary.** We have $\tau'=\tau\Phi(s,t)$, which is formula (2).

> [!note]- Proof
> **Proof.** Set $f=e$ in (5) and substitute the three metric identities. For nonnegative conductances, $\tau'>0$ is equivalent to connectedness of the final graph; initially, $\tau>0$. The connectedness criterion is therefore $\Phi(s,t)>0$. $\square$

## Resistances and the changing normalization

For $f=[w]^2$, the potential $m_{ij}=u_M(f)=\tau R_{ij}$ is the weighted sum of spanning two-component forests separating $i$ and $j$. This unnormalized quantity is also defined when the final graph is disconnected.

The mixed potential now contains three vectors:

$$
\frac{u_M(fp_1p_2)}\tau
=\det\begin{pmatrix}
R_{ij}&x&y\\
x&R_u&g\\
y&g&R_v
\end{pmatrix}
$$

The determinant equals $R_{ij}(R_uR_v-g^2)-R_vx^2-R_uy^2+2gxy$. It vanishes when the three vectors are linearly dependent, in particular for any triangle. The corresponding exterior product vanishes as well.

> [!info] The forest potential and the final resistance
> **Corollary.** For admissible conductance changes,
>
> $$
> \frac{m'_{ij}}\tau
> =R_{ij}\Phi(s,t)-s x^2-t y^2-st(R_vx^2+R_uy^2-2gxy)
> \tag{6}
> $$
>
> If $\Phi(s,t)>0$, division by the new spanning-tree coefficient $\tau'=\tau\Phi(s,t)$ gives formula (3).

> [!note]- Proof
> **Proof.** Take $f=[w]^2$ in (5). Dividing by the original $\tau$ gives
>
> $$
> \begin{aligned}
> \frac{m'_{ij}}\tau
> ={}&R_{ij}+s(R_{ij}R_u-x^2)+t(R_{ij}R_v-y^2)\\
> &+st\det\mathbf G(w,u,v)
> \end{aligned}
> $$
>
> Expand the determinant and collect terms containing $R_{ij}$: their sum is $R_{ij}\Phi(s,t)$. This yields (6). If connectedness is preserved, use $R'_{ij}=m'_{ij}/\tau'$ and subtract $R_{ij}$. $\square$

For the triangle, $m'_{12}=2+t$, $m'_{13}=2+s$, $m'_{23}=2+s+t$: these numerators have no mixed terms. The common denominator $3+2s+2t+st$ does contain them, however. Thus vanishing of one mixed forest coefficient does not yet imply independence of resistance responses.

## Sequential changes and interaction

Suppose that the graph remains connected after the first change $c_{e_1}\mapsto c_{e_1}+s$. By [[One Changing Edge|the single-variation formula]],

$$
\tau_1=\tau(1+sR_u)
$$

$$
R_v^{(1)}=R_v-\frac{s g^2}{1+sR_u},\qquad
R_{ij}^{(1)}=R_{ij}-\frac{s x^2}{1+sR_u}
$$

The second step also needs the updated inner product. Polarization of the same formula gives

$$
y^{(1)}=w\cdot_1 v=y-\frac{s xg}{1+sR_u}
$$

The subscript $1$ indicates the metric of the intermediate graph. The second step is

$$
\tau'=\tau_1(1+tR_v^{(1)}),\qquad
R'_{ij}=R_{ij}^{(1)}-\frac{t(y^{(1)})^2}{1+tR_v^{(1)}}
$$

> [!info] Agreement of sequential and joint calculations
> **Proposition.** If the intermediate and final graphs are connected, sequential recalculation gives (2)-(3).

> [!note]- Proof
> **Proof.** Set $A=1+sR_u$. Then
>
> $$
> A(1+tR_v^{(1)})
> =(1+sR_u)(1+tR_v)-stg^2=\Phi(s,t)
> $$
>
> For the resistance, the sequential increment is
>
> $$
> -\frac{s x^2}{A}-\frac{t(Ay-sxg)^2}{A\Phi(s,t)}
> $$
>
> Bringing the terms to a common denominator and expanding the square gives (3). $\square$

In the numerical example, strengthening $12$ gives $\tau_1=5$, $R_{13}^{(1)}=3/5$. The second step therefore gives $\tau'=5(1+3/5)=8$. Substituting the original $R_{13}=2/3$ instead of the updated value would incorrectly give $25/3$.

For the spanning-tree coefficient, the following expression is particularly informative:

$$
\frac{\tau'}\tau=(1+sR_u)(1+tR_v)-stg^2
$$

Here $g^2$ describes how changing one selected pair affects the resistance of the other, whereas $R_uR_v-g^2$ is the mixed coefficient in the full spanning-tree change.

> [!info] Orthogonal directions
> **Corollary.** If $g=0$, then
>
> $$
> \Phi(s,t)=(1+sR_u)(1+tR_v)
> $$
>
> $$
> \Delta R_{ij}=-\frac{s x^2}{1+sR_u}-\frac{t y^2}{1+tR_v}
> $$
>
> In this case the separate resistance responses do add. The mixed term in the spanning-tree coefficient is $stR_uR_v$ and generally does not vanish.

> [!note]- Proof
> **Proof.** Substitute $g=0$ into (1) and (3). The numerator of (3) groups as $s x^2(1+tR_v)+t y^2(1+sR_u)$. $\square$

> [!note] Connectedness of intermediate graphs
> The final graph does not depend on the order of changes, but an intermediate graph may be disconnected. For example, in the path $1-2-3$, removing $12$ and adding $13$ yields a connected final graph. Starting with removal makes the stepwise resistance formula inapplicable.
>
> When both the original and final graphs are connected, the order “all additions and strengthenings first, then weakenings and removals” is safe: the first stage retains the original connected network, and every intermediate graph in the second stage contains the final connected network.

![Recalculation Between Two Steps](<images/Recalculation Between Two Steps.svg>)

*The second step uses resistance $3/5$ from the intermediate graph. Reusing the original $2/3$ would give the incorrect $25/3$ instead of $8$.*

## Several changing edges

The generalization below is intended for a second reading. The two-factor example already contains the mechanism: expand the factors, evaluate the potentials, and divide by the new normalization.

Choose $m$ distinct pairs $e_\alpha$ with vectors $u_\alpha=a_{e_\alpha}$ and prescribe finite increments $t_\alpha\ge-c_{e_\alpha}$. Keep all other couplings fixed. The factor representation is

$$
M'=M\prod_{\alpha=1}^m\bigl(e+t_\alpha[u_\alpha]^2\bigr)
$$

> [!info] The Gram matrix of the selected directions
> **Definition.** Set
>
> $$
> \mathbf G=(u_\alpha\cdot u_\beta)_{\alpha,\beta=1}^m,
> \qquad \mathbf D=\operatorname{diag}(t_1,\ldots,t_m)
> $$
>
> For an index set $S$, let $\mathbf G_S$ be the corresponding principal submatrix and $t_S=\prod_{\alpha\in S}t_\alpha$ the product of increments. For $S=\varnothing$, adopt $t_S=\det\mathbf G_S=1$.

> [!info] The spanning-tree coefficient from all factors
> **Theorem.** For admissible finite changes,
>
> $$
> \boxed{
> \begin{aligned}
> \frac{\tau'}\tau=\Phi(\mathbf t)
> &=\sum_{S\subseteq\{1,\ldots,m\}}t_S\det\mathbf G_S\\
> &=\det(\mathbf I_m+\mathbf D\mathbf G)
> \end{aligned}
> }
> \tag{7}
> $$
>
> The final graph is connected if and only if $\Phi(\mathbf t)>0$.

> [!note]- Proof by expanding the factors
> **Proof.** For each $S$, choose the terms $t_\alpha[u_\alpha]^2$ in the product and $e$ from the remaining factors. By the metric identity, the potential of the resulting product is $\tau\det\mathbf G_S$. Extracting the top-grade coefficient gives the sum in (7).
>
> The last equality follows from multilinearity of the determinant: selecting rows indexed by $S$ from $\mathbf D\mathbf G$ and the other rows from $\mathbf I_m$ leaves $t_S\det\mathbf G_S$. The connectedness criterion follows from $\tau'=\tau\Phi$ and nonnegativity of the final conductances. $\square$

For resistance, add the measured vector $w=a_{ij}$ to each selected set. Denote the resulting Gram matrix by $\mathbf G(w,u_S)$; for empty $S$, this is the one-entry matrix $(R_{ij})$.

> [!info] Resistance from the normalized potential
> **Theorem.** If the final graph is connected, then
>
> $$
> \boxed{
> R'_{ij}=
> \frac{\displaystyle\sum_{S\subseteq\{1,\ldots,m\}}
> t_S\det\mathbf G(w,u_S)}{\Phi(\mathbf t)}
> }
> \tag{8}
> $$
>
> The numerator equals $m'_{ij}/\tau$ and remains defined when connectedness is lost. In both numerator and denominator, each parameter appears to at most the first power.

> [!note]- Proof
> **Proof.** Multiply the factor expansion of $M'$ by $[w]^2$. For a selected $S$, the metric identity gives $u_M([w]^2\prod_{\alpha\in S}[u_\alpha]^2)=\tau\det\mathbf G(w,u_S)$. Sum these contributions and divide $m'_{ij}$ by $\tau'$. If the number of vectors exceeds $n-1$, the exterior product and its determinant vanish. $\square$

The general calculation thus follows the two-factor pattern: first compute unnormalized coefficients, then divide by the new spanning-tree coefficient.

## Dependent directions and a compact matrix form

If the vectors indexed by $S$ are linearly dependent, then $\det\mathbf G_S=0$. For distinct graph pairs, this occurs when the selected edges contain a cycle. For example, $a_{12}+a_{23}=a_{13}$, so varying all three edges of a triangle produces no term $t_1t_2t_3$ in the spanning-tree coefficient. Lower-degree terms remain.

The Gram matrix $\mathbf G$ itself need not be inverted. Set $\mathbf z=(w\cdot u_\alpha)_{\alpha=1}^m$.

> [!info] Joint variation without enumerating subsets
> **Corollary.** For $\Phi(\mathbf t)>0$, formula (8) is equivalent to
>
> $$
> \boxed{\Delta R_{ij}=
> -\mathbf z^{\mathsf T}(\mathbf I_m+\mathbf D\mathbf G)^{-1}\mathbf D\mathbf z}
> \tag{9}
> $$
>
> This formula allows dependent directions and zero increments: neither $\mathbf G$ nor $\mathbf D$ needs to be inverted.

> [!note]- Proof using an additional factor
> **Proof.** Add the measured factor $e+h[w]^2$. By (7), the spanning-tree coefficient divided by the original $\tau$ is
>
> $$
> \det\begin{pmatrix}
> 1+hR_{ij}&h\mathbf z^{\mathsf T}\\
> \mathbf D\mathbf z&\mathbf I_m+\mathbf D\mathbf G
> \end{pmatrix}
> $$
>
> The coefficient of $h$ is the numerator in (8). Evaluating the same determinant through the Schur complement gives
>
> $$
> \Phi(\mathbf t)
> \left(1+h\left[R_{ij}-\mathbf z^{\mathsf T}
> (\mathbf I_m+\mathbf D\mathbf G)^{-1}\mathbf D\mathbf z\right]\right)
> $$
>
> Compare the coefficients of $h$ and divide by $\Phi(\mathbf t)$. $\square$

## Independent verification and provenance of the results

For the matrix check, form the matrix of coordinate columns $\mathbf B=(\mathbf a_{e_1},\ldots,\mathbf a_{e_m})$, where $\mathbf a_{ij}=\mathbf e_j-\mathbf e_i$ in the standard vertex-coordinate basis. Then

$$
\mathbf L'=\mathbf L+\mathbf B\mathbf D\mathbf B^{\mathsf T},
\qquad \mathbf G=\mathbf B^{\mathsf T}\mathbf{Gr}\mathbf B
$$

> [!note]- Verification by inverting the Laplacian
> **Proof.** On $\mathbf1^\perp$, the finite-rank determinant formula gives (7), and the Woodbury formula in a form not requiring $\mathbf D^{-1}$ gives
>
> $$
> \mathbf{Gr}'=\mathbf{Gr}-
> \mathbf{Gr}\mathbf B(\mathbf I_m+\mathbf D\mathbf G)^{-1}
> \mathbf D\mathbf B^{\mathsf T}\mathbf{Gr}
> $$
>
> Both sides annihilate the constant column. Multiplication on the left and right by the coordinate column of the measured vector gives (9). A detailed verification by multiplication appears in [[Varying several couplings together#The Green matrix and resistances|the matrix treatment of the joint update]]. $\square$

The determinant and inverse formulas for finite-rank updates are established results. Their graph application is presented in [[Varying several couplings together]], with external sources in [[Further Reading for the PMG Introductory Series]]. This note obtains the same answers from exponential factorization and potential normalization.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_joint_edges.py) uses exact rational arithmetic to compare independent calculations: vector-factor expansions by grade, enumeration of trees and separating forests, direct matrix inversion, explicit two-factor formulas, and sequential changes in both orders. It checks unit and weighted triangles, the path $P_4$, a weighted cycle $C_4$, dependent directions, zero increments, and loss of connectedness. These computational checks supplement the proofs.

From the repository root:

    python checks/variations/verify_joint_edges.py

The reverse direction begins in [[One Greenian Coefficient]]: a change in one vector coefficient, the resulting variations of the spanning-tree coefficient and conductances, and a derivation through a Greenian exponential factor.

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
