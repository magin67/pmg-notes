---
title: Joint Variation of Greenian Coefficients
date: 2026-10-31
updated: 2026-11-08
revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: variations-joint-greenian-coefficients
lang: en
description: 'Two Greenian coefficients: a triangle example, exact spanning-tree and conductance changes, and interaction. A factor derivation and generalization through the direction Gram matrix in the Greenian exponential metric.'
order: 4
translated_revision: 6
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/Joint Variation of Greenian Coefficients"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Совместная вариация коэффициентов гриниана|Русский]]

In [[One Greenian Coefficient|the variation of one Greenian coefficient]], the response was determined by the norm of the selected direction and one denominator. With two changes, the inner product of the directions enters. It couples the changes: a conductance preserved in each separate experiment may change under their joint action.

## Example - two Greenian coefficients of a triangle

A unit triangle has $c_{12}=c_{13}=c_{23}=1$, $\tau=3$. Its canonical Greenian coefficients are $\gamma_{12}=\gamma_{13}=\gamma_{23}=1/9$.

Increase $\gamma_{12}$ and $\gamma_{13}$ by $1/3$, keeping $\gamma_{23}$ and the vectors themselves fixed:

$$
\mathrm{Gr}'=\mathrm{Gr}+\frac13[a_{12}]^2+\frac13[a_{13}]^2
$$

![A unit triangle and the conductances after jointly increasing the Greenian coefficients of pairs 12 and 13 by one third](<images/Two Greenian Coefficients of a Triangle.svg>)

*Numbers beside edges denote conductances of the recovered graph. Changing two Greenian coefficients affects all three couplings.*

> [!example] The joint response
> We obtain
>
> $$
> c'_{12}=c'_{13}=\frac14,\qquad c'_{23}=\frac58,
> \qquad \boxed{\tau'=\frac38}
> $$
>
> Verification by enumerating the three spanning trees:
>
> $$
> \tau'=\frac14\frac14+\frac14\frac58+\frac14\frac58=\frac38
> $$

Compare this result with separate increases by $1/3$, each starting from the original graph:

| Quantity | Original graph | Only $\gamma_{12}$ | Only $\gamma_{13}$ | Both changes |
|---|---:|---:|---:|---:|
| $c_{12}$ | $1$ | $0$ | $1$ | $1/4$ |
| $c_{13}$ | $1$ | $1$ | $0$ | $1/4$ |
| $c_{23}$ | $1$ | $1$ | $1$ | $5/8$ |
| $\tau$ | $3$ | $1$ | $1$ | $3/8$ |

Each separate change preserves $c_{23}$. Together, they decrease this conductance by $3/8$. Adding separate responses is therefore insufficient even for a coupling unchanged in either experiment.

## Data for two changing coefficients

Compare with [[Two Edges and Joint Variation|direct variation]]:

| Changed data | Metric on directions | Spanning-tree response |
|---|---|---|
| Conductances | Matrix $\mathbf{Gr}$ | $\tau'=\tau\Phi$ |
| Greenian coefficients | Matrix $\mathbf L$ | $\tau'=\tau/\Phi$ |

Each row uses its own Gram matrix and factor $\Phi$. The shared formula structure does not allow the data of one row to be used in the other.

The original graph is undirected, its set of $n\ge2$ vertices is fixed, and its conductances are nonnegative. Positive-conductance edges form a connected graph. Work with the direct centered Greenian representation

$$
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,
\qquad \gamma_{ij}=-\mathrm{Gr}_{ij}
$$

Choose two distinct pairs $e_1,e_2$, set $u=a_{e_1}$, $v=a_{e_2}$, and prescribe finite changes $s,t$:

$$
\mathrm{Gr}'=\mathrm{Gr}+s[u]^2+t[v]^2
$$

All unprimed quantities below are calculated in the original graph. The notation $\mathbf u,\mathbf v$ denotes the zero-sum coordinate columns of the vectors, and $\mathbf L$ the Laplacian matrix. The directions themselves remain fixed.

> [!info] Norms, interaction, and vertex responses
> **Notation.** Set
>
> $$
> q_u=\mathbf u^{\mathsf T}\mathbf L\mathbf u,\qquad
> q_v=\mathbf v^{\mathsf T}\mathbf L\mathbf v,\qquad
> g=\mathbf u^{\mathsf T}\mathbf L\mathbf v
> $$
>
> $$
> \mathbf x=\mathbf L\mathbf u,\qquad
> \mathbf y=\mathbf L\mathbf v
> $$
>
> Inner products here are taken in [[The Greenian Metric and Potentials|the metric of the Greenian exponential]] $N=\exp(\mathrm{Gr})$, given by the original Laplacian. Thus $q_u=u\cdot_N u$, $q_v=v\cdot_N v$, $g=u\cdot_N v$.

For $u=a_{kl}$ and $v=a_{pq}$, the data can be obtained directly from the Laplacian entries:

$$
q_u=L_{kk}+L_{ll}-2L_{kl},\qquad
q_v=L_{pp}+L_{qq}-2L_{pq}
$$

$$
g=L_{lq}-L_{lp}-L_{kq}+L_{kp}
$$

$$
x_i=L_{il}-L_{ik},\qquad y_i=L_{iq}-L_{ip}
$$

In [[Two Edges and Joint Variation|the direct variation of couplings]], interactions were calculated in the resistance metric using the Green matrix. Here the roles of the two matrices are exchanged.

## Explicit formulas for two coefficients

Denote the common factor by

$$
\Phi(s,t)=1+s q_u+t q_v+st(q_uq_v-g^2)
\tag{1}
$$

> [!info] The spanning-tree coefficient and conductances
> For $\Phi(s,t)\ne0$, the exact responses are
>
> $$
> \boxed{\tau'=\frac{\tau}{\Phi(s,t)},\qquad
> \Delta\tau=\tau\left(\frac1{\Phi(s,t)}-1\right)}
> \tag{2}
> $$
>
> For $i\ne j$,
>
> $$
> \boxed{\begin{aligned}
> \Delta c_{ij}={}&
> \frac{s(1+tq_v)x_i x_j+t(1+sq_u)y_i y_j}{\Phi(s,t)}\\
> &-\frac{stg(x_i y_j+y_i x_j)}{\Phi(s,t)}
> \end{aligned}}
> \tag{3}
> $$
>
> For the Laplacian matrix, the response has the opposite sign: $\Delta L_{ij}$ is minus the right-hand side of (3), including when $i=j$.

Setting $t=0$ gives the formulas for [[One Greenian Coefficient|one coefficient]]. Reversing the orientation of $u$ changes the signs of $\mathbf x$ and $g$; reversing $v$ changes those of $\mathbf y$ and $g$. The full answer is preserved.

A nonzero denominator ensures algebraic invertibility. To obtain a graph with nonnegative conductances, one must also check positive definiteness of the new Greenian and all signs $c'_{ij}$. Unlike the one-direction case, $\Phi>0$ alone does not ensure positive definiteness.

### Substitution for the triangle

For $u=a_{12}$, $v=a_{13}$ in the unit triangle,

$$
q_u=q_v=6,\qquad g=3,\qquad
\mathbf x=\begin{pmatrix}-3\\3\\0\end{pmatrix},\qquad
\mathbf y=\begin{pmatrix}-3\\0\\3\end{pmatrix}
$$

Hence

$$
\Phi(s,t)=1+6s+6t+27st,\qquad
\tau'=\frac3{1+6s+6t+27st}
$$

$$
c'_{12}=\frac{1-3s+6t}{\Phi(s,t)},\qquad
c'_{13}=\frac{1+6s-3t}{\Phi(s,t)}
$$

$$
c'_{23}=\frac{1+6s+6t}{\Phi(s,t)}
=1-\frac{27st}{\Phi(s,t)}
$$

At $s=t=1/3$, we have $\Phi=8$ and obtain the numbers in the example. The change in $c_{23}$ contains only a joint contribution: it vanishes if $s=0$ or $t=0$.

## Two factors of the Greenian exponential

Let $N=\exp(\mathrm{Gr})$, $p=[u]^2$, $r=[v]^2$. All products in this section are polyform products; no matrix exponential is used.

> [!info] Two factors and grades
> **Proposition.** The following exact equalities hold:
>
> $$
> \boxed{N'=N(e+sp)(e+tr)}
> \tag{4}
> $$
>
> $$
> N'=N+sNp+tNr+stNpr
> $$
>
> $$
> N'_k=N_k+sN_{k-1}p+tN_{k-1}r+stN_{k-2}pr
> $$
>
> Here $N_j=0$ for $j<0$. These equalities remain valid when the new form is degenerate.

> [!note]- Proof of the factorization
> **Proof.** The forms commute, and $p^2=r^2=0$. Thus $\exp(sp)=e+sp$, $\exp(tr)=e+tr$. Expand the product and extract grade $k$. $\square$

It is the squares of the forms $p$ and $r$ that vanish, not the squares of the factors: for example, $(e+sp)^2=e+2sp$. The product $pr$ of two different vector forms is generally nonzero; it produces the term $st$.

## The top-grade coefficient and the spanning-tree response

Set $d=n-1$, $T_n=[(a_1\ldots a_n)]^2$. By [[Laplacian and Greenian - Mutual Duality of Exponentials#Representations and normalizations at a glance|the normalization of mutual duality]],

$$
N_d=\sigma T_n,\qquad \sigma=\frac1{n^2\tau}
$$

The functional $\tau(F)$ extracts the coefficient of $T_n$, and the normalized potential is $P_N(f)=\tau(Nf)/\sigma$. By [[The Greenian Metric and Potentials#The Laplacian as the metric of the Greenian exponential|the metric identity]],

$$
P_N(p)=q_u,\qquad P_N(r)=q_v,\qquad
P_N(pr)=\det\begin{pmatrix}q_u&g\\g&q_v\end{pmatrix}
=q_uq_v-g^2
$$

The last quantity is the norm of the exterior product $uv$ in metric $N$, geometrically the squared area of the corresponding parallelogram.

> [!info] Change of the top-grade normalization
> **Corollary.** We have
>
> $$
> \sigma'=\sigma\Phi(s,t)
> $$
>
> For $\Phi\ne0$, this yields the spanning-tree formula (2).

> [!note]- Proof through the top grade
> **Proof.** Extracting the top-grade coefficient in (4) gives
>
> $$
> \frac{\sigma'}\sigma
> =1+sP_N(p)+tP_N(r)+stP_N(pr)=\Phi(s,t)
> $$
>
> If the new form is nondegenerate, $\sigma'=1/(n^2\tau')$ still holds, so $\tau'=\tau/\Phi$. $\square$

The top-grade coefficient of the Greenian exponential changes polynomially. The spanning-tree coefficient of the recovered Laplacian is obtained by inverting this normalization.

## Conductances from a third-grade potential

Introduce the centered vectors $p_i=a_i-h$, where $h=n^{-1}\sum_i a_i$. For them, $P_N([p_i,p_j])=L_{ij}$. After changing the exponential, the same potential recovers $L'_{ij}$.

> [!info] Joint variation of a potential
> **Lemma.** For a fixed form $f$ and $\Phi\ne0$,
>
> $$
> P_{N'}(f)=
> \frac{P_N(f)+sP_N(fp)+tP_N(fr)+stP_N(fpr)}{\Phi(s,t)}
> \tag{5}
> $$

> [!note]- Proof of the potential variation
> **Proof.** Multiply (4) by $f$, extract the top-grade coefficient, and divide by the new $\sigma'=\sigma\Phi$. $\square$

For $f=[p_i,p_j]$, the one-factor terms are

$$
P_N(fp)=L_{ij}q_u-x_i x_j,\qquad
P_N(fr)=L_{ij}q_v-y_i y_j
$$

The joint contribution is expressed by a mixed determinant:

$$
P_N(fpr)=
\det\begin{pmatrix}
L_{ij}&x_i&y_i\\
x_j&q_u&g\\
y_j&g&q_v
\end{pmatrix}
$$

Its rows correspond to vectors $p_i,u,v$, and its columns to $p_j,u,v$. For $i\ne j$, this is a mixed inner product of exterior objects rather than the norm of one object; it may have either sign.

> [!info] Recovering conductances
> **Corollary.** Substituting these potentials into (5) gives (3).

> [!note]- Proof through the mixed determinant
> **Proof.** Expanding the determinant gives
>
> $$
> \begin{aligned}
> P_N(fpr)={}&L_{ij}(q_uq_v-g^2)-q_vx_ix_j-q_uy_iy_j\\
> &+g(x_iy_j+y_ix_j)
> \end{aligned}
> $$
>
> In the numerator of (5), all terms containing $L_{ij}$ combine into $L_{ij}\Phi$. The remaining terms are minus the numerator of (3). Division by $\Phi$ gives $\Delta L_{ij}$, and the passage $c_{ij}=-L_{ij}$ reverses the sign. $\square$

For a triangle, the affine-vector space is two-dimensional, so the third-order determinant vanishes. This does not eliminate the joint response: the mixed term remains in the normalization factor $\Phi$.

## Sequential calculation and interaction

If the Greenian is nondegenerate after the first change, set $A=1+s q_u\ne0$. By [[One Greenian Coefficient|the one-factor formulas]],

$$
\tau_1=\frac{\tau}{A},\qquad
\mathbf L_1=\mathbf L-\frac{s}{A}\mathbf x\mathbf x^{\mathsf T}
$$

The second step uses the updated data:

$$
q_v^{(1)}=q_v-\frac{s g^2}{A},\qquad
\mathbf y^{(1)}=\mathbf L_1\mathbf v
=\mathbf y-\frac{s g}{A}\mathbf x
$$

> [!info] Agreement of the two calculations
> **Proposition.** For $A\ne0$ and $\Phi\ne0$, sequential changes give
>
> $$
> \tau'=\frac{\tau_1}{1+tq_v^{(1)}}
> $$
>
> $$
> \Delta c_{ij}=\frac{s x_i x_j}{A}
> +\frac{t y_i^{(1)}y_j^{(1)}}{1+tq_v^{(1)}}
> $$
>
> These expressions agree with (2)-(3).

> [!note]- Proof by sequential recalculation
> **Proof.** We have
>
> $$
> A(1+tq_v^{(1)})=(1+s q_u)(1+tq_v)-stg^2=\Phi
> $$
>
> This proves the spanning-tree formula. In the conductance formula, substitute $y_i^{(1)}=y_i-sgx_i/A$ and bring the fractions to a common denominator. The coefficients of $x_ix_j$, $y_iy_j$, and $x_iy_j+y_ix_j$ become $s(1+tq_v)/\Phi$, $t(1+sq_u)/\Phi$, and $-stg/\Phi$, respectively. $\square$

In the triangle example, after the first change we have $\tau_1=1$ and $q_v^{(1)}=6-(1/3)\cdot9/3=5$. The second step gives $\tau'=1/(1+5/3)=3/8$. Using the old $q_v=6$ would incorrectly give $1/3$.

The quantity $g^2$ determines how the first step changes the norm of the second direction. If $g=0$, then

$$
\Phi=(1+s q_u)(1+tq_v),\qquad
\tau'=\frac{\tau}{(1+s q_u)(1+tq_v)}
$$

$$
\Delta c_{ij}=\frac{s x_i x_j}{1+s q_u}
+\frac{t y_i y_j}{1+tq_v}
$$

These equalities follow directly from (1)-(3). Here the separate conductance responses add, although the mixed term $stq_uq_v$ remains in $\Phi$.

If an intermediate Greenian is degenerate, stepwise inversion through it is inapplicable even when the joint answer is defined. For positive definite original and final forms, all positive additions can be performed first, followed by the negative ones: intermediate forms remain positive definite. This order alone does not guarantee nonnegative intermediate conductances.

## Several Greenian coefficients

This section and the next give the general extension. On a first reading, after the two-factor calculation, proceed to [[#Invertibility, positivity, and conductance signs|admissibility conditions]]: a nonzero determinant permits inversion but alone guarantees neither metric positivity nor conductance signs.

For fixed directions $u_1,\ldots,u_m$, prescribe

$$
\mathrm{Gr}'=\mathrm{Gr}+\sum_{\alpha=1}^m t_\alpha[u_\alpha]^2
$$

$$
N'=N\prod_{\alpha=1}^m(e+t_\alpha[u_\alpha]^2)
$$

When varying canonical coefficients, the directions are differences of selected vertex pairs. The formulas also hold for arbitrary fixed affine vectors.

> [!info] The interaction Gram matrix
> **Definition.** Let $\mathbf U$ contain the coordinate columns of the selected directions. Set
>
> $$
> \mathbf G=(u_\alpha\cdot_Nu_\beta)_{\alpha,\beta=1}^m
> =\mathbf U^{\mathsf T}\mathbf L\mathbf U
> $$
>
> $$
> \mathbf D=\operatorname{diag}(t_1,\ldots,t_m)
> $$
>
> For an index subset $S$, denote the principal submatrix by $\mathbf G_S$ and the product of increments by $t_S=\prod_{\alpha\in S}t_\alpha$. For empty $S$, adopt $t_S=\det\mathbf G_S=1$.

> [!info] The general spanning-tree response
> **Theorem.** The multiplier of the top-grade coefficient is
>
> $$
> \boxed{\begin{aligned}
> \Phi(\mathbf t)&=\frac{\sigma'}\sigma
> =\sum_{S\subseteq\{1,\ldots,m\}}t_S\det\mathbf G_S\\
> &=\det(\mathbf I_m+\mathbf D\mathbf G)
> \end{aligned}}
> \tag{6}
> $$
>
> For $\Phi\ne0$, we have $\tau'=\tau/\Phi$.

> [!note]- Proof by expanding the factors
> **Proof.** In the product expansion, select a set $S$ of vector forms. Its normalized potential in the original $N$ is $\det\mathbf G_S$. Summation gives the first equality in (6). The second follows by expanding the determinant according to the choice of rows from $\mathbf I_m$ or $\mathbf D\mathbf G$. Finally, $\sigma=1/(n^2\tau)$ and $\sigma'=1/(n^2\tau')$ give the spanning-tree response. $\square$

For vertex $i$, collect its interactions with the directions in a column:

$$
\mathbf b_i=\bigl((\mathbf L\mathbf u_\alpha)_i\bigr)_{\alpha=1}^m
$$

> [!info] The general conductance response
> **Theorem.** For $\Phi\ne0$, set
>
> $$
> \mathbf K=(\mathbf I_m+\mathbf D\mathbf G)^{-1}\mathbf D
> $$
>
> Then
>
> $$
> \boxed{\Delta c_{ij}=\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j},
> \qquad i\ne j
> \tag{7}
> $$
>
> In matrix form, with $\mathbf B=\mathbf L\mathbf U$,
>
> $$
> \boxed{\mathbf L'=\mathbf L-\mathbf B\mathbf K\mathbf B^{\mathsf T}}
> \tag{8}
> $$
>
> The matrix $\mathbf K$ is symmetric. These formulas do not require inversion of $\mathbf G$ or $\mathbf D$ and allow dependent directions and zero increments.

> [!note]- Proof using an additional measured factor
> **Proof.** For a fixed vector $w$, set $q_w=w\cdot_N w$ and $\mathbf z=(w\cdot_Nu_\alpha)_\alpha$. Add the factor $e+\lambda[w]^2$ to $N'$. By (6), its top-grade coefficient divided by the original $\sigma$ equals
>
> $$
> \det\begin{pmatrix}
> 1+\lambda q_w&\lambda\mathbf z^{\mathsf T}\\
> \mathbf D\mathbf z&\mathbf I_m+\mathbf D\mathbf G
> \end{pmatrix}
> $$
>
> By the Schur complement formula, this is
>
> $$
> \Phi\bigl(1+\lambda(q_w-\mathbf z^{\mathsf T}\mathbf K\mathbf z)\bigr)
> $$
>
> Comparing coefficients of $\lambda$ and dividing by $\Phi$ gives
>
> $$
> P_{N'}([w]^2)=P_N([w]^2)-\mathbf z^{\mathsf T}\mathbf K\mathbf z
> $$
>
> Polarize this equality for the centered vectors $p_i,p_j$. This yields $L'_{ij}=L_{ij}-\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j$ and (7)-(8).
>
> From $(\mathbf I_m+\mathbf D\mathbf G)\mathbf D=\mathbf D(\mathbf I_m+\mathbf G\mathbf D)$, we obtain $\mathbf K=\mathbf D(\mathbf I_m+\mathbf G\mathbf D)^{-1}$. The last expression is the transpose of the original one, so $\mathbf K$ is symmetric. $\square$

The product of factors itself also gives, for every $f$,

$$
P_{N'}(f)=\frac{\displaystyle\sum_S t_S
P_N\left(f\prod_{\alpha\in S}[u_\alpha]^2\right)}{\Phi(\mathbf t)}
$$

Thus the compact matrix formula computes the same normalized potential as expansion of all the factors.

## Dependent directions

If the vectors indexed by $S$ are linearly dependent, their exterior product and $\det\mathbf G_S$ vanish. For distinct graph pairs, this happens when the selected edges contain a cycle. The Gram matrix itself need not be invertible for (6)-(8).

For example, $a_{12}+a_{23}=a_{13}$. Changing all three Greenian coefficients of a unit triangle by the same amount $t$ gives

$$
\Phi(t,t,t)=(1+9t)^2,\qquad
c'_{ij}=\frac1{1+9t},\qquad
\tau'=\frac3{(1+9t)^2}
$$

The cubic term is absent because the three directions are dependent. The conductance formulas apply for $t\ne-1/9$, and the graph domain is $t>-1/9$. This can also be checked from $\mathbf L=3\mathbf J$, $\mathbf{Gr}=\mathbf J/3$, and $\sum_{i<j}\mathbf a_{ij}\mathbf a_{ij}^{\mathsf T}=3\mathbf J$, where $\mathbf a_{ij}=\mathbf e_j-\mathbf e_i$.

## Invertibility, positivity, and conductance signs

These conditions must be checked separately. The first is determined by the multiplier already found: the new form is nondegenerate on $\mathbf1^\perp$ exactly when $\Phi\ne0$.

> [!info] A positive definiteness criterion
> **Proposition.** Let $\mathbf G^{1/2}$ be the symmetric nonnegative square root of the original Gram matrix. The new Greenian is positive definite on $\mathbf1^\perp$ if and only if
>
> $$
> \mathbf I_m+\mathbf G^{1/2}\mathbf D\mathbf G^{1/2}\succ0
> \tag{9}
> $$
>
> For two directions, this is equivalent to the two scalar conditions
>
> $$
> \boxed{\Phi(s,t)>0,\qquad 2+s q_u+tq_v>0}
> \tag{10}
> $$

> [!note]- Proof of the positivity criterion
> **Proof.** On the zero-sum space, congruence of the changed Greenian with $\mathbf L^{1/2}$ gives $I+\mathbf X\mathbf D\mathbf X^{\mathsf T}$, where $\mathbf X=\mathbf L^{1/2}\mathbf U$.
>
> We have $\mathbf X^{\mathsf T}\mathbf X=\mathbf G$. The polar decomposition $\mathbf X=\mathbf V\mathbf G^{1/2}$ identifies the ranges of $\mathbf G$ and $\mathbf X$ isometrically. On these ranges, the two matrices in the criterion have the same restrictions; on the complementary subspaces, they act as the identity. This proves (9), including a singular Gram matrix.
>
> For a symmetric matrix of size $2$, positivity of both eigenvalues is equivalent to positivity of its determinant and trace. These are $\Phi$ and $2+s q_u+tq_v$, respectively. $\square$

If all $t_\alpha\ge0$, positive definiteness is automatically preserved. With arbitrary signs, a positive determinant is insufficient. For example, for the two directions of the triangle above, $s=t=-1$ gives $\Phi=16>0$ but $2+6s+6t=-10<0$; the new Greenian has two negative directions.

After checking (9), calculate the conductances by (7). To obtain a connected graph with nonnegative conductances, it is necessary and sufficient to require $c_{ij}+\Delta c_{ij}\ge0$ for every $i<j$. If absent couplings must remain zero, those pairs additionally require $\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j=0$.

At $\Phi=0$, the product of factors and all its grades remain defined, but the top-grade coefficient vanishes. Division by it and recovery of an inverse form on all of $\mathbf1^\perp$ are impossible. In regions with negative conductances, $\tau'$ denotes a signed spanning-tree cofactor; positivity of that number alone does not certify graph conductance signs.

## Independent verification and continuation

> [!note]- Verification by matrix multiplication
> **Proof.** We have $\mathbf{Gr}'=\mathbf{Gr}+\mathbf U\mathbf D\mathbf U^{\mathsf T}$, $\mathbf{Gr}\mathbf B=\mathbf U$, and $\mathbf U^{\mathsf T}\mathbf B=\mathbf G$. Thus the product of the new Greenian and the right-hand side of (8) is
>
> $$
> \mathbf J+\mathbf U(\mathbf D-\mathbf K-\mathbf D\mathbf G\mathbf K)\mathbf B^{\mathsf T}
> =\mathbf J
> $$
>
> The last equality follows from $(\mathbf I_m+\mathbf D\mathbf G)\mathbf K=\mathbf D$. Symmetry gives the reverse-order product; both matrices annihilate the constant column. This independently verifies inversion on $\mathbf1^\perp$. The finite-rank determinant formula gives the same factor $\Phi$. $\square$

The matrix equalities are variants of the Woodbury identity and the determinant formula for finite-rank updates; sources are collected in [[Further Reading for the PMG Introductory Series]]. Here they are derived through vector factors of the Greenian exponential, potentials, and duality normalization.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_joint_greenian_coefficients.py) uses exact rational arithmetic. It compares factor expansions in every grade, recovery through exterior contraction, direct matrix inversion, spanning-tree enumeration, explicit two-factor formulas, and sequential recalculation. Checks include weighted triangles, the path $P_4$, the cycle $C_4$, dependent directions, zero increments, degeneracy, and the distinction between a positive determinant and positive definiteness.

From the repository root:

    python checks/variations/verify_joint_greenian_coefficients.py

The passage to independent resistance changes begins in [[One Resistance and Quadric Connectivity]]: a single-resistance update is represented by two fixed vector contributions, and the formulas obtained here give the changes in the spanning-tree coefficient and conductances.

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
