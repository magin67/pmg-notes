---
title: One Greenian Coefficient
date: 2026-10-31
updated: 2026-11-11
revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: variations-one-greenian-coefficient
lang: en
description: 'Changing one vector coefficient of the Greenian: a path example, exact variations of the spanning-tree coefficient and conductances, an exponential-factor derivation, and admissible parameters.'
order: 3
translated_revision: 7
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/One Greenian Coefficient"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Один коэффициент гриниана|Русский]]

In [[One Changing Edge|the variation of one edge]], a conductance change was prescribed and the spanning-tree coefficient and resistances were calculated. We now prescribe a change in one Greenian coefficient at a fixed vector form. We seek two answers: how the spanning-tree coefficient changes and what the graph conductances become.

## Example - one Greenian coefficient of a path

See [[en/PythonExamples/Example - Laplacian, Greenian and Resistance Variations#One Greenian coefficient|the notebook calculation]].

Take the path $1-2-3-4$ with unit conductances. It has one spanning tree, so $\tau=1$. In [[The Canonical Vector Representation of the Greenian#Full example: a path on four vertices|the canonical Greenian expansion of this path]], the coefficient of $[a_{12}]^2$ is $\gamma_{12}=-1/8$.

Increase this coefficient by $t=1/5$, keeping the other coefficients and the vectors themselves fixed:

$$
\mathrm{Gr}'=\mathrm{Gr}+\frac15[a_{12}]^2,
\qquad \gamma'_{12}=-\frac18+\frac15=\frac3{40}
$$

This changes a Greenian coefficient. It does not yet prescribe the new conductance $c_{12}$: that conductance must be recovered together with the other couplings.

![The unit path and the graph after increasing the Greenian coefficient of pair form 12 by one fifth](<images/One Greenian Coefficient of a Path.svg>)

*Numbers beside edges denote conductances. The change introduces coupling $13$, decreases two path conductances, and preserves coupling $34$.*

> [!example] The answer for the path
> The new conductances and spanning-tree coefficient are
>
> $$
> c'_{12}=\frac25,\qquad c'_{23}=\frac7{10},\qquad
> c'_{13}=\frac15,\qquad c'_{34}=1
> $$
>
> $$
> c'_{14}=c'_{24}=0,\qquad \boxed{\tau'=\frac12}
> $$

In the new graph, edge $34$ belongs to every spanning tree, and two edges are chosen from triangle $123$. Direct counting confirms the answer:

$$
\tau'=1\left(\frac25\frac7{10}+\frac25\frac15+\frac7{10}\frac15\right)
=\frac12
$$

Why did one coefficient change affect several couplings, and where did these fractions come from? Two general formulas answer these questions.

For a fixed direction $u=a_{kl}$, denote its coordinates by $u_i$.

Changing one Greenian coefficient is not equivalent to independently changing one resistance. Since $\mathbf{Gr}'=\mathbf{Gr}+t\mathbf u\mathbf u^{\mathsf T}$ and $R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}$, the following exact linear equality holds:

$$
\Delta R_{ij}=t(u_i-u_j)^2
$$

For $u=a_{kl}$, resistance $R_{kl}$ changes by $4t$, resistances of pairs with exactly one endpoint in $\{k,l\}$ change by $t$, and all others remain fixed. Thus “change only $R_{kl}$” requires a different combination of vector contributions. Joint vector contributions are treated in [[Joint Variation of Greenian Coefficients]], and their required combination for a single resistance in [[One Resistance and Quadric Connectivity]].

## Two formulas for one coefficient

The original graph is undirected, with nonnegative conductances on a fixed set of $n\ge2$ vertices. Its positive-conductance edges form a connected graph. Use the direct centered representation

$$
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,
\qquad \gamma_{ij}=-\mathrm{Gr}_{ij},\qquad a_{ij}=a_j-a_i
$$

Here $\mathbf{Gr}$ is the Green matrix, $\mathbf L$ the Laplacian matrix, and $L$ the corresponding polyform. For $i\ne j$, we have $c_{ij}=-L_{ij}$. The weighted degree of a vertex is denoted by $d_i=L_{ii}=\sum_{j\ne i}c_{ij}$.

Choose a pair $k<l$ and change only $\gamma_{kl}$ by the finite amount $t$:

$$
\gamma'_{kl}=\gamma_{kl}+t,\qquad
\mathrm{Gr}'=\mathrm{Gr}+t[a_{kl}]^2
$$

All unprimed quantities in the following formulas refer to the original graph.

> [!info] The norm of the varied direction
> **Notation.** Set
>
> $$
> q_{kl}=L_{kk}+L_{ll}-2L_{kl}
> =d_k+d_l+2c_{kl}>0
> $$
>
> This is the norm of the vector $a_{kl}$ in the metric of the Greenian exponential, described in [[The Greenian Metric and Potentials]]. In terms of conductances,
>
> $$
> q_{kl}=4c_{kl}+\sum_{r\ne k,l}(c_{kr}+c_{lr})
> $$
>
> It differs from the resistance $R_{kl}$ and generally equals neither $1/c_{kl}$ nor $1/R_{kl}$.

> [!info] The spanning-tree coefficient and conductances
> For $1+tq_{kl}\ne0$, the exact response formulas are
>
> $$
> \boxed{\tau'=\frac{\tau}{1+tq_{kl}},\qquad
> \Delta\tau=-\frac{\tau t q_{kl}}{1+tq_{kl}}}
> \tag{1}
> $$
>
> $$
> \boxed{\Delta c_{ij}
> =\frac{t(L_{ik}-L_{il})(L_{jk}-L_{jl})}{1+tq_{kl}}},
> \qquad i\ne j
> \tag{2}
> $$
>
> Here $\Delta c_{ij}=c'_{ij}-c_{ij}$. To remain within the class of graphs with nonnegative conductances, also require $1+tq_{kl}>0$ and $c'_{ij}\ge0$ for every pair. These conditions are examined below.

In particular, the conductance of the selected pair changes according to

$$
\Delta c_{kl}
=-\frac{t(d_k+c_{kl})(d_l+c_{kl})}{1+tq_{kl}}
$$

For $t>0$, it decreases. Other conductances may decrease or increase: the sign is determined by the product of two differences in (2). Interchanging $k,l$ changes both signs and preserves the answer.

For the entries of the Laplacian matrix, including the diagonal, the sign is opposite:

$$
\Delta L_{ij}
=-\frac{t(L_{ik}-L_{il})(L_{jk}-L_{jl})}{1+tq_{kl}}
\tag{3}
$$

## Substitution for the path

For the unit path $1-2-3-4$ and pair $12$,

$$
q_{12}=1+2+2=5,\qquad
\begin{pmatrix}L_{11}-L_{12}\\L_{21}-L_{22}\\L_{31}-L_{32}\\L_{41}-L_{42}\end{pmatrix}
=\begin{pmatrix}2\\-3\\1\\0\end{pmatrix}
$$

Thus (1)-(2) give, for arbitrary $t\ne-1/5$,

$$
\tau'=\frac1{1+5t},\qquad
c'_{12}=1-\frac{6t}{1+5t}=\frac{1-t}{1+5t}
$$

$$
c'_{23}=1-\frac{3t}{1+5t}=\frac{1+2t}{1+5t},\qquad
c'_{13}=\frac{2t}{1+5t}
$$

Coupling $34$ is preserved, while $14$ and $24$ remain zero. At $t=1/5$, we recover the values in the example.

Within $t>-1/5$, all conductances are nonnegative exactly when $0\le t\le1$. At the right endpoint $t=1$, coupling $12$ disappears, but the graph remains connected: $c'_{13}=1/3$, $c'_{23}=1/2$, $c'_{34}=1$. For $t>1$, conductance $12$ becomes negative; for $-1/5<t<0$, the new coupling $13$ is negative.

Positive definiteness of the new Greenian therefore permits a wider range than nonnegativity of all conductances. If the previously absent coupling $13$ is also forbidden, this example allows only $t=0$.

![Admissible Greenian Parameter](<images/Admissible Greenian Parameter.svg>)

*Nonsingularity, metric positivity, and nonnegative conductances impose different conditions. This diagram shows the positive region; preserving the absent edge $13$ reduces the graph region to $t=0$.*

## One factor of the Greenian exponential

Write $u=a_{kl}$, $N=\exp(\mathrm{Gr})$, $N'=\exp(\mathrm{Gr}')$. Here and below, the exponential is the exterior exponential of a form, not a matrix exponential.

> [!info] Adding one factor
> **Proposition.** Changing the coefficient of a fixed vector gives
>
> $$
> \boxed{N'=N\bigl(e+t[u]^2\bigr)}
> \tag{4}
> $$
>
> Grade by grade,
>
> $$
> N'_r=N_r+tN_{r-1}[u]^2,\qquad 0\le r\le n-1
> $$
>
> Here $N_{-1}=0$. These equalities are exact for every real $t$, including when the new form is degenerate.

> [!note]- Proof of the factorization
> **Proof.** Quadratic forms commute, and $([u]^2)^2=0$. Therefore $\exp(t[u]^2)=e+t[u]^2$. Multiplication by $N$ and extraction of grade $r$ give the claim. $\square$

The coefficient at the original vector $u$ changes; the vector itself does not. In the canonical factorization, this replaces the factor $e+\gamma_{kl}[u]^2$ by $e+(\gamma_{kl}+t)[u]^2$.

## The top-grade coefficient and spanning-tree normalization

Let $T_n=[(a_1\ldots a_n)]^2$, $d=n-1$. Denote by $\tau(F)$ the coefficient of $T_n$ in the polyform $F$. The Laplacian and Greenian exponentials have [[Laplacian and Greenian - Mutual Duality of Exponentials#Representations and normalizations at a glance|different established top-grade normalizations]]:

$$
M_d=\tau T_n,\qquad N_d=\sigma T_n,\qquad
\sigma=\tau(N)=\frac1{n^2\tau}
$$

Here $\tau$ without an argument is the original graph's spanning-tree coefficient. The normalized potential of a form in $N$ is

$$
P_N(f)=\frac{\tau(Nf)}\sigma
$$

> [!info] How the factor changes the spanning-tree coefficient
> **Corollary.** If $q=P_N([u]^2)$, then
>
> $$
> \sigma'=\sigma(1+tq),\qquad
> \tau'=\frac{\tau}{1+tq}\quad(1+tq\ne0)
> $$

> [!note]- Proof through the top grade
> **Proof.** From (4) and linearity of coefficient extraction,
>
> $$
> \sigma'=\tau(N')=\tau(N)+t\tau(N[u]^2)
> =\sigma(1+tq)
> $$
>
> By [[The Greenian Metric and Potentials#The Laplacian as the metric of the Greenian exponential|the metric identity]], $q=\mathbf u^{\mathsf T}\mathbf L\mathbf u$, where $\mathbf u$ is the zero-sum coordinate column of vector $u$. For $u=a_{kl}$, we obtain $q=q_{kl}$.
>
> If the new form is nondegenerate on the zero-sum space, exponential duality gives the same normalization $\sigma'=1/(n^2\tau')$. Thus $\tau/\tau'=\sigma'/\sigma=1+tq$. Subtracting the original $\tau$ gives (1). $\square$

It is the top-grade coefficient $\sigma$ of the Greenian exponential that changes linearly. The spanning-tree coefficient on the original side is proportional to $1/\sigma$, so its finite variation has denominator $1+tq$.

## Conductances from normalized potentials

Set $h=n^{-1}\sum_i a_i$, $p_i=a_i-h$. By [[The Greenian Metric and Potentials#Potentials of centered vertices|the potentials of centered vertices]],

$$
P_N([p_i,p_j])=L_{ij}
$$

After changing the Greenian, the same potential in the new exponential recovers $L'_{ij}$. This expresses mutual duality: the metric of the Greenian exponential is given by the Laplacian.

> [!info] The response of a potential
> **Lemma.** For any fixed form $f$ and $1+tq\ne0$,
>
> $$
> P_{N'}(f)=\frac{P_N(f)+tP_N(f[u]^2)}{1+tq}
> \tag{5}
> $$

> [!note]- Proof accounting for the new normalization
> **Proof.** Multiply (4) by $f$, extract the top-grade coefficient, and divide by $\sigma'=\sigma(1+tq)$. Both numerator and denominator come from the same changed exponential. $\square$

Now write

$$
b_i=P_N([p_i,u])=(\mathbf L\mathbf u)_i
$$

For the form $[p_i,p_j][u]^2=[p_i u,p_j u]$, the potential is expressed by a second-order determinant:

$$
P_N([p_i u,p_j u])
=\det\begin{pmatrix}L_{ij}&b_i\\b_j&q\end{pmatrix}
=L_{ij}q-b_i b_j
$$

> [!info] The recovered Laplacian
> **Theorem.** For any fixed nonzero affine vector $u$ with coordinate column $\mathbf u\in\mathbf1^\perp$ and variation $\mathrm{Gr}'=\mathrm{Gr}+t[u]^2$,
>
> $$
> \boxed{L'_{ij}=L_{ij}-\frac{t b_i b_j}{1+tq}}
> \tag{6}
> $$
>
> Here
>
> $$
> q=\mathbf u^{\mathsf T}\mathbf L\mathbf u,\qquad
> \mathbf b=\mathbf L\mathbf u
> $$
>
> The applicability condition is $1+tq\ne0$. The same answer as a polyform is
>
> $$
> L'=L-\frac{t}{1+tq}[v]^2,\qquad
> v=\sum_i b_i a_i
> $$

> [!note]- Proof through products of forms
> **Proof.** Substitute $f=[p_i,p_j]$ into (5):
>
> $$
> L'_{ij}=\frac{L_{ij}+t(L_{ij}q-b_i b_j)}{1+tq}
> =L_{ij}-\frac{t b_i b_j}{1+tq}
> $$
>
> Since $\sum_i b_i=0$, vector $v$ belongs to the space of affine vectors. The coefficient matrix of $[v]^2$ is $\mathbf b\mathbf b^{\mathsf T}$, which gives the polyform expression.
>
> For $u=a_{kl}$, we have $b_i=L_{il}-L_{ik}$. The product $b_i b_j$ equals $(L_{ik}-L_{il})(L_{jk}-L_{jl})$, yielding (3). For $i\ne j$, the passage $c_{ij}=-L_{ij}$ reverses the sign and gives (2). $\square$

> [!note]- The same construction using exterior contraction
> **Proof.** To write duality explicitly, transfer $N$ to the dual space: $D=\mathcal C^{-1}(N)=\exp Q_1$, $u^\vee=\mathcal C^{-1}(u)$, where $\mathcal C(a_i^\vee)=p_i$. Then
>
> $$
> D'=D(e+t[u^\vee]^2),\qquad
> Q'_r=Q_r+tQ_{r-1}[u^\vee]^2
> $$
>
> For $Q_{-1}=0$, recovery of the first direct grade gives
>
> $$
> \begin{aligned}
> L'&=\tau'\bigl(T_n/Q'_{d-1}\bigr)\\
> &=\tau'\bigl(T_n/Q_{d-1}+t\,T_n/(Q_{d-2}[u^\vee]^2)\bigr)
> \end{aligned}
> $$
>
> A slash with a form on the right denotes exterior contraction, linear in the form being contracted. The coefficient $\tau'$ stands outside and must already be updated. The equivalent potential formulas (5)-(6) compute the entries of the same recovered form without expanding all dual grades. $\square$

## Admissible parameters and degeneracy

For fixed nonzero $u$, the original $q=\mathbf u^{\mathsf T}\mathbf L\mathbf u$ is positive. Invertibility, positive definiteness, and conductance signs must be distinguished.

> [!info] Domains of applicability
> **Proposition.** The new Greenian form:
>
> - is nondegenerate on $\mathbf1^\perp$ exactly when $1+tq\ne0$;
> - is positive definite on that space exactly when $1+tq>0$;
> - recovers a graph with nonnegative conductances exactly when the preceding strict inequality and all the conditions
>
> $$
> c_{ij}+t(c_{ij}q+b_i b_j)\ge0,\qquad i<j
> \tag{7}
> $$
>
> hold.

> [!note]- Proof of the conditions
> **Proof.** On the zero-sum space, denote the original positive definite Greenian matrix by $A$. Congruence with $A^{-1/2}$ takes $A+t\mathbf u\mathbf u^{\mathsf T}$ to $I+tzz^{\mathsf T}$, where $z=A^{-1/2}\mathbf u$ and $z^{\mathsf T}z=q$. The latter matrix has one eigenvalue $1+tq$, with all others equal to $1$. This proves the first two conditions.
>
> For $1+tq>0$, inequality $c'_{ij}=c_{ij}+t b_i b_j/(1+tq)\ge0$ is equivalent to (7). The new matrix is symmetric, has zero row sums, and is positive definite on $\mathbf1^\perp$. Together with nonnegative conductances, this gives a connected graph. $\square$

Conditions (7) are linear in the single parameter $t$. Their intersection with $t>-1/q$ gives the exact admissible domain, not merely a small-change estimate. The coefficient $\gamma'_{kl}$ itself need not be positive.

If absent couplings must remain zero, each such pair additionally requires $t b_i b_j=0$. This may forbid every nonzero change of a single selected coefficient, as in the path example.

At $t=-1/q$, a new null direction appears: $\mathbf{Gr}'\mathbf b=0$, where $\mathbf b=\mathbf L\mathbf u\ne0$. The exponential $N'$ exists, but its top-grade coefficient $\sigma'$ is zero. No finite Laplacian inverse to it on all of $\mathbf1^\perp$ can then be recovered. As $t\downarrow-1/q$ approaches the boundary from the positive definite region, $\tau'$ and the magnitude of the Laplacian update grow without bound. This is Greenian degeneracy, not ordinary bridge removal where the spanning-tree coefficient vanishes.

For $t<-1/q$, the inversion formulas are algebraically defined again, but the form has one negative direction. In this region, $\tau'$ is understood as a signed cofactor of the recovered matrix; the interpretation as a graph with nonnegative conductances does not apply.

## The differential limit and resistances

At $t\to0$, the finite formulas give derivatives at the original state:

$$
\frac{\partial\tau}{\partial\gamma_{kl}}=-\tau q_{kl}
$$

$$
\frac{\partial c_{ij}}{\partial\gamma_{kl}}
=(L_{ik}-L_{il})(L_{jk}-L_{jl})
$$

For a finite increment, the denominator $1+tq_{kl}$ must be retained. Before a subsequent coefficient change, the data $\mathbf L$, $q_{kl}$, and $\tau$ must be recalculated.

Resistance changes under one coefficient update are given before the general formulas above.

## Independent matrix verification

> [!note]- Verification by direct multiplication
> **Proof.** Write $\mathbf J=\mathbf I-\mathbf1\mathbf1^{\mathsf T}/n$. We have $\mathbf{Gr}\mathbf L=\mathbf J$, $\mathbf{Gr}\mathbf b=\mathbf u$, $\mathbf u^{\mathsf T}\mathbf b=q$. Then
>
> $$
> (\mathbf{Gr}+t\mathbf u\mathbf u^{\mathsf T})
> \left(\mathbf L-\frac{t}{1+tq}\mathbf b\mathbf b^{\mathsf T}\right)
> =\mathbf J
> $$
>
> Indeed, the coefficient of the additional term $\mathbf u\mathbf b^{\mathsf T}$ is $t-t/(1+tq)-t^2q/(1+tq)=0$. Symmetry gives the reverse-order product, and both matrices annihilate the constant column. This independently verifies (6) by inversion on $\mathbf1^\perp$.
>
> The rank-one determinant formula gives $\det_H\mathbf{Gr}'=\det_H\mathbf{Gr}(1+tq)$, where $H=\mathbf1^\perp$. From $\det_H\mathbf L=n\tau$ and mutual invertibility on $H$, we recover (1). $\square$

> [!example] Checking the factor of four on one edge
> For a single edge of conductance $c>0$, we have $\gamma_{12}=1/(4c)$ and $q_{12}=4c$. After adding $t[a_{12}]^2$,
>
> $$
> c'=\tau'=\frac{c}{1+4ct}
> $$
>
> This agrees with directly inverting $\gamma'_{12}=1/(4c)+t$. The entire admissible domain here is $t>-1/(4c)$.

The matrix formula (6) is the Sherman-Morrison identity applied to the Greenian on the zero-sum space; sources for the classical inversion formulas are collected in [[Further Reading for the PMG Introductory Series]]. The polyform derivation uses factor (4), the top-grade normalization of duality, and the second-grade potential determinant.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_one_greenian_coefficient.py) compares factor expansions by grade, recovery through exterior contraction, direct matrix inversion, and spanning-tree enumeration. All calculations use exact rational arithmetic. Cases include one weighted edge, triangles, the path $P_4$, and the cycle $C_4$, negative Greenian coefficients, new couplings, approach to degeneracy, and the degenerate point itself.

From the repository root:

    python checks/variations/verify_one_greenian_coefficient.py

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
