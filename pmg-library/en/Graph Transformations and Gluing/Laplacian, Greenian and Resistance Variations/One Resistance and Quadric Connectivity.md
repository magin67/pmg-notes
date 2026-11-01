---
title: One Resistance and Quadric Connectivity
date: 2026-10-31
updated: 2026-11-01
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: variations-one-resistance-and-quadric-connectivity
lang: en
description: 'Changing one resistance while preserving the others: an example, finite spanning-tree and conductance variations, and two Greenian factors. Quadric connectivity and its inverse relation to squared inner products on all pairs.'
order: 5
translated_revision: 5
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/One Resistance and Quadric Connectivity"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Один резистенс и квадросвязность|Русский]]

We now prescribe a change in exactly one resistance $R_{kl}$, keeping all others fixed. This differs from changing one Greenian coefficient: the required update affects several canonical coefficients. It can nevertheless be represented by just two vector contributions, allowing us to apply [[Joint Variation of Greenian Coefficients|the joint-variation formulas]].

The differential limit introduces quadric connectivity. Its matrix is the inverse of the matrix of squared resistance inner products. This identity applies to the full set of vertex pairs, including pairs with zero conductance.

## Example - only one side resistance changes

A unit triangle has all conductances equal to $1$, all resistances equal to $2/3$, and spanning-tree coefficient $\tau=3$. Prescribe

$$
R'_{12}=1,\qquad R'_{13}=R'_{23}=\frac23
$$

Thus only $R_{12}$ increases, by $\rho=1/3$.

![A unit triangle and the recovered conductances when only resistance 12 increases from two thirds to one](<images/One Resistance of a Triangle.svg>)

*Numbers beside edges denote conductances. Weakening coupling $12$ is accompanied by strengthening the other two couplings so that resistances $R_{13}$ and $R_{23}$ remain fixed.*

> [!example] The answer for the triangle
> The new conductances and spanning-tree coefficient are
>
> $$
> c'_{12}=\frac25,\qquad c'_{13}=c'_{23}=\frac65,
> \qquad \boxed{\tau'=\frac{12}5}
> $$
>
> Verification using trees and separating forests:
>
> $$
> \tau'=\frac25\frac65+\frac25\frac65+\frac65\frac65=\frac{12}5
> $$
>
> $$
> R'_{12}=\frac{c'_{13}+c'_{23}}{\tau'}=1,\qquad
> R'_{13}=R'_{23}=\frac{c'_{12}+c'_{23}}{\tau'}=\frac23
> $$

Changing conductance $c_{12}$ alone would also decrease or increase the other resistances. Here two additional conductance updates ensure that they are preserved.

## Explicit finite formulas

The original graph is undirected, its set of $n\ge2$ vertices is fixed, and its conductances are nonnegative. Its positive-conductance edges form a connected graph. Prescribe one independent symmetric coordinate:

$$
R'_{kl}=R_{kl}+\rho,\qquad R'_{lk}=R_{lk}+\rho,
\qquad k<l
$$

All other entries of $\mathbf R$ remain fixed, including the zero diagonal. The quantity $\rho$ is a finite increment. All unprimed data refer to the original graph.

For brevity, set

$$
\begin{gathered}
A=L_{kk},\qquad B=L_{ll},\qquad C=L_{kl},\\
x_i=L_{ik},\qquad y_i=L_{il}
\end{gathered}
$$

Here $\mathbf L$ is the Laplacian matrix, $A,B$ are weighted degrees, and $C=-c_{kl}$. Define

$$
\Phi(\rho)=1-\rho C-\frac{\rho^2}{4}(AB-C^2),
\qquad \eta(\rho)=1-\frac{\rho C}{2}
\tag{1}
$$

> [!info] The spanning-tree coefficient and conductances
> For $\Phi(\rho)\ne0$,
>
> $$
> \boxed{\tau'=\frac{\tau}{\Phi(\rho)},\qquad
> \Delta\tau=\tau\left(\frac1{\Phi(\rho)}-1\right)}
> \tag{2}
> $$
>
> For $i\ne j$,
>
> $$
> \boxed{\begin{aligned}
> \Delta c_{ij}={}&-\frac{\rho\eta(\rho)(x_i y_j+y_i x_j)}{2\Phi(\rho)}\\
> &-\frac{\rho^2(Bx_i x_j+Ay_i y_j)}{4\Phi(\rho)}
> \end{aligned}}
> \tag{3}
> $$
>
> For $\Delta L_{ij}$, the right-hand side has the opposite sign, including diagonal entries. A graph with nonnegative conductances requires the additional conditions below.

### Substitution for the triangle

For the selected pair $12$ of a unit triangle,

$$
A=B=2,\qquad C=-1,\qquad
\mathbf x=\begin{pmatrix}2\\-1\\-1\end{pmatrix},\qquad
\mathbf y=\begin{pmatrix}-1\\2\\-1\end{pmatrix}
$$

Formulas (1)-(3) give

$$
\Phi(\rho)=1+\rho-\frac34\rho^2,\qquad
\tau'=\frac3{\Phi(\rho)}
$$

$$
c'_{12}=\frac{1-3\rho/2}{\Phi(\rho)},\qquad
c'_{13}=c'_{23}=\frac{1+3\rho/2}{\Phi(\rho)}
$$

Substituting $\rho=1/3$ gives $\Phi=5/4$ and the numbers in the example. All conductances are nonnegative exactly when

$$
-\frac23<\rho\le\frac23
$$

At the right endpoint, $c'_{12}=0$, $c'_{13}=c'_{23}=3/2$: the graph becomes a path, and $R'_{12}=4/3$ equals the sum of the two preserved resistances. Positive definiteness of the Greenian alone allows the wider interval $-2/3<\rho<2$.

## Which Greenian coefficients change

Let $h=n^{-1}\sum_i a_i$, $p_i=a_i-h$, and $\mathbf J=\mathbf I-\mathbf1\mathbf1^{\mathsf T}/n$. Use [[The Canonical Vector Representation of the Greenian#Mean resistances and the inverse distance transformation|the exact linear transformation]]

$$
\mathbf{Gr}=-\frac12\mathbf J\mathbf R\mathbf J
$$

For one changing coordinate, it gives

$$
\Delta\mathbf{Gr}
=-\frac\rho2(\mathbf p_k\mathbf p_l^{\mathsf T}
+\mathbf p_l\mathbf p_k^{\mathsf T}),\qquad
\mathbf p_i=\mathbf e_i-\frac1n\mathbf1
\tag{4}
$$

> [!info] Changes in canonical coefficients
> **Corollary.** When all resistances except $R_{kl}=R_{lk}$ are preserved, the coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$ change as follows:
>
> | Pair $ij$ | Increment $\Delta\gamma_{ij}$ |
> |---|---:|
> | The pair $kl$ itself | $\displaystyle\frac{\rho(n^2-2n+2)}{2n^2}$ |
> | Exactly one vertex shared with $kl$ | $\displaystyle-\frac{\rho(n-2)}{2n^2}$ |
> | No vertex shared with $kl$ | $\displaystyle\frac\rho{n^2}$ |

> [!note]- Proof of the coefficient transformation
> **Proof.** For $i<j$, (4) gives
>
> $$
> \begin{aligned}
> \Delta\gamma_{ij}=\frac\rho2\bigl[&
> (\delta_{ik}-1/n)(\delta_{jl}-1/n)\\
> &+(\delta_{il}-1/n)(\delta_{jk}-1/n)\bigr]
> \end{aligned}
> $$
>
> Substituting the three possible pair-intersection types gives the table. For $n=2$ and $n=3$, some pair types are absent. $\square$

In the triangle example, for $\rho=1/3$ we obtain

$$
\Delta\gamma_{12}=\frac5{54},\qquad
\Delta\gamma_{13}=\Delta\gamma_{23}=-\frac1{54}
$$

The new coefficients are therefore $11/54,5/54,5/54$. The general formula can be applied to all these changes. However, update (4) itself admits a shorter representation using two vectors.

## One resistance as two vector contributions

In the direct centered representation, [[Greenian Coefficients and Vertex Variations#Resistances in the polar representation|the polar expression]] is

$$
\mathrm{Gr}=-\frac12\sum_{i<j}R_{ij}\{p_i,p_j\},\qquad
\{p_i,p_j\}=[p_i,p_j]+[p_j,p_i]
$$

Hence $\Delta\mathrm{Gr}=-(\rho/2)\{p_k,p_l\}$. Set

$$
u=p_k-p_l,\qquad v=p_k+p_l
$$

> [!info] Two fixed directions
> **Proposition.** A change in one resistance is represented by
>
> $$
> \boxed{\mathrm{Gr}'=\mathrm{Gr}+\frac\rho4[u]^2-\frac\rho4[v]^2}
> \tag{5}
> $$
>
> Thus, for $N=\exp(\mathrm{Gr})$,
>
> $$
> \boxed{N'=N\left(e+\frac\rho4[u]^2\right)
> \left(e-\frac\rho4[v]^2\right)}
> \tag{6}
> $$

> [!note]- Proof of the two-factor representation
> **Proof.** Polarization gives $[u]^2-[v]^2=-2\{p_k,p_l\}$. Multiplication by $\rho/4$ yields (5). The vanishing squares of vector forms and their commutativity give (6). For $n=2$, we have $v=0$, so the second factor is $e$. $\square$

The directions are fixed and independent of $\rho$. In general, $v$ is not a difference of two vertices, so its coefficient does not coincide with a single canonical $\gamma_{ij}$. Formulas for arbitrary affine directions were obtained in [[Joint Variation of Greenian Coefficients]].

## Deriving the finite formulas

In the metric of the Greenian exponential, inner products are given by the original Laplacian. For the selected directions,

$$
q_u=A+B-2C,\qquad q_v=A+B+2C,\qquad g=A-B
$$

$$
(\mathbf L\mathbf u)_i=x_i-y_i,\qquad
(\mathbf L\mathbf v)_i=x_i+y_i
$$

> [!info] Substitution into the joint Greenian variation
> **Theorem.** Formulas (2)-(3) follow from the two-factor representation (6) with parameters $s=\rho/4$, $t=-\rho/4$.

> [!note]- Proof of the spanning-tree and conductance formulas
> **Proof.** In [[Joint Variation of Greenian Coefficients#Explicit formulas for two coefficients|the two-factor multiplier]], we obtain
>
> $$
> \begin{aligned}
> 1+s q_u+tq_v+st(q_uq_v-g^2)
> &=1-\rho C-\frac{\rho^2}{4}(AB-C^2)\\
> &=\Phi(\rho)
> \end{aligned}
> $$
>
> The Greenian top-grade coefficient $\sigma=1/(n^2\tau)$ therefore changes to $\sigma'=\sigma\Phi$, yielding (2).
>
> For the conductances, substitute $\mathbf L\mathbf u=\mathbf x-\mathbf y$, $\mathbf L\mathbf v=\mathbf x+\mathbf y$ into the same two-factor formula. Expanding the brackets turns the numerator into
>
> $$
> \begin{aligned}
> &-\frac\rho2\left(1-\frac{\rho C}{2}\right)(x_i y_j+y_i x_j)\\
> &-\frac{\rho^2}{4}(Bx_i x_j+Ay_i y_j)
> \end{aligned}
> $$
>
> Division by $\Phi$ gives (3). Thus both the linear and quadratic terms come from the factor product with the new normalization. $\square$

The resistances are preserved in precisely the prescribed sense: (4) defines the Greenian of a matrix with just one changed symmetric coordinate. On symmetric zero-diagonal tables, double centering and recovery by $R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}$ are mutually inverse.

## Admissible increments

> [!info] Invertibility and graph constraints
> **Proposition.** For this single-resistance variation:
>
> - $\Phi(\rho)\ne0$ is equivalent to nondegeneracy of the new Greenian on $\mathbf1^\perp$;
> - $\Phi(\rho)>0$ is equivalent to its positive definiteness on that space;
> - a connected graph with nonnegative conductances additionally requires, and is ensured by, all inequalities $c_{ij}+\Delta c_{ij}\ge0$.
>
> Preserving absent couplings also requires $\Delta c_{ij}=0$ on the corresponding pairs.

> [!note]- Proof of the applicability conditions
> **Proof.** The first condition follows from the top-grade coefficient $\sigma'=\sigma\Phi$. For $n\ge3$, the centered vectors $p_k,p_l$ are independent, so their Laplacian Gram matrix is positive definite: $AB-C^2>0$.
>
> The polynomial $\Phi$ has a negative leading coefficient and $\Phi(0)=1$. Its positive region is one interval between two roots:
>
> $$
> \frac2{C-\sqrt{AB}}<\rho<\frac2{C+\sqrt{AB}}
> $$
>
> Within this interval, no Greenian eigenvalue vanishes, and at $\rho=0$ all are positive on $\mathbf1^\perp$. Positivity therefore holds throughout the interval. Outside it, the determinant is negative, so positive definiteness is impossible.
>
> For $n=2$ and conductance $c$, we have $\Phi=1+c\rho$ and $c'=c/(1+c\rho)$; the condition is again $\Phi>0$. Finally, positive definiteness of the recovered matrix on $\mathbf1^\perp$, zero row sums, and nonnegative conductances give a connected graph. $\square$

Sufficiency of the sign $\Phi>0$ here is specific to a single-resistance update. It fails for arbitrary multiple Greenian contributions, as shown by [[Joint Variation of Greenian Coefficients#Invertibility, positivity, and conductance signs|the general criterion]].

At $\Phi=0$, the factor product remains defined, but inversion on the whole zero-sum space is impossible. Substituting a pseudoinverse of the degenerate form does not solve the prescribed-resistance recovery problem. With negative conductances, the formulas remain algebraic, and $\tau'$ is interpreted as a signed spanning-tree cofactor.

## Quadric connectivity

To first order, formula (3) gives

$$
\left.\frac{dL_{ij}}{d\rho}\right|_{\rho=0}
=\frac12(L_{ik}L_{jl}+L_{il}L_{jk})
$$

> [!info] Quadric connectivity of two pairs
> **Definition.** The **quadric connectivity** of pairs $ij$ and $kl$, where $i<j$, $k<l$, is
>
> $$
> \boxed{Lq^{ij,kl}=\frac12(L_{ik}L_{jl}+L_{il}L_{jk})}
> \tag{7}
> $$
>
> The name and notation belong to PMG terminology. A single coordinate $R_{kl}$ here means changing the equal entries $R_{kl}$ and $R_{lk}$ together.

> [!info] Quadric connectivity as sensitivity
> **Corollary.** With all other resistances fixed,
>
> $$
> \boxed{\frac{\partial L_{ij}}{\partial R_{kl}}=Lq^{ij,kl},\qquad
> \frac{\partial c_{ij}}{\partial R_{kl}}=-Lq^{ij,kl}}
> \tag{8}
> $$
>
> For the spanning-tree coefficient and the Laplacian diagonal,
>
> $$
> \frac{\partial\tau}{\partial R_{kl}}=\tau L_{kl}=-\tau c_{kl},\qquad
> \frac{\partial L_{ii}}{\partial R_{kl}}=L_{ik}L_{il}
> $$

> [!note]- Proof of the differential formulas
> **Proof.** Differentiate (1)-(3) at $\rho=0$, where $\Phi=\eta=1$. The diagonal identities follow from the same formula for $\Delta L_{ij}$ with $i=j$. Equivalently, from $d\mathbf{Gr}=-\mathbf J(d\mathbf R)\mathbf J/2$ and the differential of inversion on $\mathbf1^\perp$,
>
> $$
> d\mathbf L=\frac12\mathbf L(d\mathbf R)\mathbf L
> $$
>
> For one symmetric coordinate, the two nonzero entries of $d\mathbf R$ give exactly (7)-(8), with no extra factor $2$. $\square$

Quadric connectivity is independent of pair orientation and symmetric under exchanging the pairs:

$$
Lq^{ij,kl}=Lq^{ji,kl}=Lq^{ij,lk}=Lq^{kl,ij}
$$

Its geometric expression uses centered vectors and metric $N$:

$$
\begin{aligned}
Lq^{ij,kl}=\frac12\bigl[&
(p_i\cdot_Np_k)(p_j\cdot_Np_l)\\
&+(p_i\cdot_Np_l)(p_j\cdot_Np_k)\bigr]
\end{aligned}
$$

This is a symmetrized product of two Laplacian inner products. Unlike the square of a single inner product, it may be negative.

If $d_i=L_{ii}$, substitution into (7) gives three useful cases:

| Pair arrangement | Quadric connectivity |
|---|---|
| Coincident pairs | $\displaystyle Lq^{ij,ij}=\frac{d_i d_j+c_{ij}^2}{2}>0$ |
| Common vertex $i$ | $\displaystyle Lq^{ij,ik}=\frac{c_{ij}c_{ik}-d_i c_{jk}}2$ |
| Four distinct vertices | $\displaystyle Lq^{ij,kl}=\frac{c_{ik}c_{jl}+c_{il}c_{jk}}2\ge0$ |

Increasing a pair's own resistance therefore decreases its conductance to first order. The response of adjacent couplings can have either sign. These derivatives refer to the original state: the finite increment (3) also contains quadratic terms and a changing denominator.

## Two matrices on the full set of pairs

Denote the set of all unordered pairs by

$$
\mathcal P=\{ij:1\le i<j\le n\},\qquad m=\binom n2
$$

These edge coordinates include every coefficient $c_{ij}$ of $[a_{ij}]^2$, including zero coefficients. Fix an order of pairs and form the columns $\boldsymbol c=(c_{ij})$ and $\boldsymbol R=(R_{ij})$.

At zero conductances, derivatives are considered in the space of nondegenerate centered forms. Admissibility of a direction within the class of nonnegative-conductance graphs is checked separately.

> [!info] Direct and inverse response matrices
> **Definition.** On $\mathcal P\times\mathcal P$, set
>
> $$
> \mathbf S_{ij,kl}=(a_{ij}\cdot_Ma_{kl})^2,
> \qquad \mathbf{Lq}_{ij,kl}=Lq^{ij,kl}
> \tag{9}
> $$
>
> In $\mathbf S$, use the original resistance metric with matrix $\mathbf{Gr}$. These are entrywise squares of inner products, not the ordinary matrix square of a Gram matrix. Diagonal pairs $ii$ are excluded from both matrices.

From [[One Changing Edge#Sensitivity and resistance preservation|direct resistance sensitivity]] and (8),

$$
d\boldsymbol R=-\mathbf S\,d\boldsymbol c,\qquad
d\boldsymbol c=-\mathbf{Lq}\,d\boldsymbol R
\tag{10}
$$

> [!info] Mutual inverses
> **Theorem.** For a connected undirected graph, both matrices in (9) are symmetric and positive definite. When indexed by all vertex pairs,
>
> $$
> \boxed{\mathbf S\,\mathbf{Lq}=\mathbf{Lq}\,\mathbf S=\mathbf I_m}
> \tag{11}
> $$
>
> There is no extra sign or factor in (11): both Jacobians in (10) carry a minus sign.

> [!note]- Direct proof of the inverse identity
> **Proof.** Fix a pair $e=ij$. Let $\mathbf a_e=\mathbf e_j-\mathbf e_i$, $\mathbf z=\mathbf{Gr}\mathbf a_e$. Then $\mathbf L\mathbf z=\mathbf a_e$ and
>
> $$
> \mathbf S_{e,ab}=(z_b-z_a)^2
> $$
>
> For column $kl$, the matrix product is
>
> $$
> \begin{aligned}
> (\mathbf S\mathbf{Lq})_{e,kl}
> &=\frac12\sum_{a<b}(z_a-z_b)^2
> (L_{ak}L_{bl}+L_{al}L_{bk})\\
> &=\frac12\sum_{a,b}(z_a-z_b)^2L_{ak}L_{bl}
> \end{aligned}
> $$
>
> Expand the square. Terms containing $z_a^2$ and $z_b^2$ vanish because the columns of $\mathbf L$ sum to zero. What remains is
>
> $$
> -(\mathbf L\mathbf z)_k(\mathbf L\mathbf z)_l
> =-(\mathbf a_e)_k(\mathbf a_e)_l
> $$
>
> For $k<l$, this number is $1$ for pair $kl=e$ and $0$ for the other pairs. This proves $\mathbf S\mathbf{Lq}=\mathbf I_m$. Both matrices are symmetric, so transposition gives the reverse product. $\square$

> [!note]- Why the matrices are positive definite
> **Proof.** On $H=\mathbf1^\perp$, matrix $\mathbf{Gr}$ is positive definite. Set $v_e=\mathbf{Gr}_H^{1/2}\mathbf a_e$. Then
>
> $$
> \mathbf S_{e,f}=(v_e^{\mathsf T}v_f)^2
> =\operatorname{tr}(v_ev_e^{\mathsf T}v_fv_f^{\mathsf T})
> $$
>
> This is the Gram matrix of the symmetric matrices $v_ev_e^{\mathsf T}$ under the Frobenius inner product. They are linearly independent: after an invertible transformation, it suffices to check matrices $\mathbf a_e\mathbf a_e^{\mathsf T}$; the off-diagonal entry $ij$ of the sum $\sum_e z_e\mathbf a_e\mathbf a_e^{\mathsf T}$ is $-z_{ij}$. A zero sum therefore requires all $z_e=0$.
>
> Thus $\mathbf S\succ0$, and its inverse $\mathbf{Lq}$ is positive definite as well. $\square$

There are more edge vectors than the dimension of the space, and their Gram matrix is usually singular. Their quadratic forms, however, form a basis of the symmetric-form space, whose dimension is $\binom n2$. The matrix of entrywise squared inner products consequently has full rank.

### Matrices for the unit triangle

In pair order $12,13,23$,

$$
\mathbf S=\frac19\begin{pmatrix}4&1&1\\1&4&1\\1&1&4\end{pmatrix},\qquad
\mathbf{Lq}=\frac12\begin{pmatrix}5&-1&-1\\-1&5&-1\\-1&-1&5\end{pmatrix}
$$

Their product is the identity. The quadric-connectivity column for changing $R_{12}$ gives

$$
\frac{dc_{12}}{dR_{12}}=-\frac52,\qquad
\frac{dc_{13}}{dR_{12}}=\frac{dc_{23}}{dR_{12}}=\frac12
$$

This is the differential limit of the finite formulas already obtained for the triangle.

## Restricting to existing edges

In general, rows and columns corresponding to zero couplings cannot be deleted from both matrices while preserving (11). Differentiating with respect to one resistance while holding all others fixed may require previously absent conductances to appear.

For example, for the unit path $1-2-3$ and its existing edge set $E=\{12,23\}$,

$$
\mathbf S_{EE}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathbf{Lq}_{EE}=\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}
$$

These submatrices are not mutual inverses. Identity (11) also requires pair $13$.

If conductances on the complement $Z=\mathcal P\setminus E$ are fixed, then $d\boldsymbol c_Z=0$ and $d\boldsymbol R_E=-\mathbf S_{EE}d\boldsymbol c_E$. Resistances on $Z$ are free to change. The corresponding inverse matrix is

$$
\boxed{(\mathbf S_{EE})^{-1}
=\mathbf{Lq}_{EE}-\mathbf{Lq}_{EZ}
(\mathbf{Lq}_{ZZ})^{-1}\mathbf{Lq}_{ZE}}
\tag{12}
$$

> [!note]- Proof for a restricted edge set
> **Proof.** For nonempty $Z$, block $\mathbf{Lq}_{ZZ}$ is positive definite. The second system in (10), together with $d\boldsymbol c_Z=0$, gives
>
> $$
> d\boldsymbol R_Z=-(\mathbf{Lq}_{ZZ})^{-1}
> \mathbf{Lq}_{ZE}d\boldsymbol R_E
> $$
>
> Substitute this into the equation for $d\boldsymbol c_E$. The Schur complement in (12) appears and inverts $\mathbf S_{EE}$. For empty $Z$, the original equality (11) remains. $\square$

Thus mutual inversion on all pairs describes independent variations of all resistances. Restricting the set of variable conductances leads to a different inverse problem.

## Provenance of the results and verification

The name “quadric connectivity” and formula (7) were used in the original PMG materials; this note fixes its differential meaning, the sign for conductances, and the precise domain of the matrix inverse identity. Identity (11) is proved directly. The finite formulas (2)-(3) are derived afresh from two Greenian vector contributions; they do not result from applying a differential equality to finite increments.

Double centering, differentiation of an inverse matrix, and the Schur complement belong to classical matrix theory; sources are listed in [[Further Reading for the PMG Introductory Series]]. The PMG term and an independent proof do not establish scientific priority for these matrix results.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_one_resistance.py) uses exact rational arithmetic. It compares the prescribed resistance matrix, double centering, two vector factors, recovery through exterior contraction, direct inversion, and spanning-tree sums. For one edge, triangles, the path $P_4$, and the cycle $C_4$, it checks finite formulas, preservation of other resistances, both inverse identities in (11), conductance signs, and degenerate cases. Submatrices and the Schur complement are checked separately.

From the repository root:

    python checks/variations/verify_one_resistance.py

For several independently prescribed resistances, their Greenian updates add linearly. [[Joint Variation of Resistances]] treats two increments, the general calculation on a selected vertex set, and direct solution of the finite matrix equation.

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
