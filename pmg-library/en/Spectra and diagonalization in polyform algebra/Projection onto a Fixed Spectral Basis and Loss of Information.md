---
title: "Projection onto a Fixed Spectral Basis and Loss of Information"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: projection-onto-a-fixed-spectral-basis
order: 6
description: "Diagonal and block projections, the nearest graph in a spectral cone, lost mixed coefficients, and effects on exterior exponentials, forest coefficients, the Greenian, and duality."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Проекция на фиксированный спектральный базис и потеря информации|Русский]]

An eigenbasis of one graph can serve as a system of directions for describing another. A complete change of coordinates preserves the operator. Information is lost when only the diagonal of the matrix in the new basis is retained: the evaluations of individual directions remain, while their mixed coefficients are discarded.

[[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]] describes admissible Laplacians with prescribed modes. Here we approximate an arbitrary Laplacian by such operators and examine the effect on polyforms, their grades, and duality. A single example will distinguish diagonal projection, the nearest graph in the cone, and projection onto entire eigenspaces.

## Space, metric, and retained coordinates

Let $\mathbf L$ be the Laplacian of a connected undirected graph with nonnegative conductances on a fixed set of $n$ vertices, $n\ge2$. Set $d=n-1$, $H=\mathbf1^\perp$, and use the coordinate inner product $\langle\mathbf z,\mathbf y\rangle_0=\mathbf z^{\mathsf T}\mathbf y$. Fix an orthonormal basis

$$
\mathbf U=(\mathbf u_0,\mathbf u_1,\ldots,\mathbf u_d),\qquad
\mathbf u_0=\frac{\mathbf1}{\sqrt n}
$$

It may be an eigenbasis of a reference graph, such as a path or cycle. It is not assumed to be an eigenbasis of the $\mathbf L$ under investigation. If $\mathbf U_H=(\mathbf u_1,\ldots,\mathbf u_d)$, then

$$
\mathbf S=\mathbf U_H^{\mathsf T}\mathbf L\mathbf U_H,\qquad
\mathbf U^{\mathsf T}\mathbf L\mathbf U=
\begin{pmatrix}0&0\\0&\mathbf S\end{pmatrix},\qquad
\mathbf L=\mathbf U_H\mathbf S\mathbf U_H^{\mathsf T}
$$

The matrix $\mathbf S$ is positive definite. Taken together, all its entries reconstruct $\mathbf L$; its diagonal entries alone do not. Write

$$
\mu_k=S_{kk}=\mathbf u_k^{\mathsf T}\mathbf L\mathbf u_k
=\sum_{i<j}w_{ij}\bigl(u_k(i)-u_k(j)\bigr)^2
$$

These are the energy evaluations of the chosen unit directions. In general, they are not eigenvalues of the original operator.

We measure distances between matrices using the Frobenius inner product:

$$
\langle\mathbf A,\mathbf C\rangle_F=\operatorname{tr}(\mathbf A^{\mathsf T}\mathbf C),\qquad
\|\mathbf A\|_F^2=\sum_{i,j}A_{ij}^2
$$

Here $\|\cdot\|_F$ is a linear matrix norm. This is an auxiliary coordinate geometry on the space of operators. It differs from the PMG resistance metric defined by $\mathbf{Gr}=\mathbf L^+$ on $H$; the conventions for these identifications are given in [[en/Foundations/Core specification|Core specification]].

## Diagonal projection and the exact error

Let $\mathbf E_k=\mathbf u_k\mathbf u_k^{\mathsf T}$. These matrices are orthonormal for the Frobenius inner product. The space of centered symmetric matrices diagonal in $\mathbf U$ is

$$
\mathcal A_U=\left\{\sum_{k=1}^d\nu_k\mathbf E_k:\boldsymbol\nu\in\mathbb R^d\right\}
$$

**Proposition.** The unique matrix in $\mathcal A_U$ nearest to $\mathbf L$ is

$$
\boxed{\widehat{\mathbf L}=\Pi_U(\mathbf L)=\sum_{k=1}^d\mu_k\mathbf E_k}
$$

For every $\boldsymbol\nu\in\mathbb R^d$,

$$
\left\|\mathbf L-\sum_k\nu_k\mathbf E_k\right\|_F^2
=\sum_{i\ne j}S_{ij}^2+\sum_k(\mu_k-\nu_k)^2
$$

**Proof.** An orthogonal change of basis preserves the Frobenius inner product. In the basis $\mathbf U_H$, the difference consists of the fixed off-diagonal entries $S_{ij}$ and the diagonal entries $\mu_k-\nu_k$. Their sum of squares is minimized only at $\boldsymbol\nu=\boldsymbol\mu$. $\square$

Thus,

$$
\boxed{\|\mathbf L-\Pi_U(\mathbf L)\|_F^2=\sum_{i\ne j}S_{ij}^2},\qquad
\|\mathbf L\|_F^2=\|\Pi_U(\mathbf L)\|_F^2+\|\mathbf L-\Pi_U(\mathbf L)\|_F^2
$$

The projection is linear and idempotent. It preserves the $\mu_k$, the matrix trace, and the constant zero mode. Since $\mu_k>0$, its result is positive definite on $H$. However, its off-diagonal entries in vertex coordinates may still have signs incompatible with a graph.

Removing off-diagonal blocks is known in matrix theory as *pinching*; diagonal projection is a special case. A classical survey is [R. Bhatia, Pinching, Trimming, Truncating, and Averaging of Matrices (2000)](https://doi.org/10.1080/00029890.2000.12005245). The derivation for the chosen norm is given in full above.

## The nearest graph in the spectral cone

Let $\mathcal K_U$ be the cone from [[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]]:

$$
\mathcal K_U=\left\{\boldsymbol\nu:\ -\sum_k\nu_k u_k(i)u_k(j)\ge0\ \text{for all }i<j\right\}
$$

If $\boldsymbol\mu\notin\mathcal K_U$, the unconstrained diagonal projection is not a graph Laplacian. The nearest admissible operator is obtained by solving

$$
\boldsymbol\mu_*=\underset{\boldsymbol\nu\in\mathcal K_U}{\operatorname{argmin}}
\sum_k(\nu_k-\mu_k)^2,\qquad
\mathbf L_*=\sum_k\mu_{*,k}\mathbf E_k
$$

This is a strictly convex quadratic problem with linear constraints. The cone is nonempty and closed; a minimum exists because the objective tends to infinity as $\|\boldsymbol\nu\|\to\infty$, and strict convexity makes it unique. The general theory of Euclidean projection is presented in [Boyd–Vandenberghe, Convex Optimization, §8.1.1, printed p. 398](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=412).

By the error decomposition proved above,

$$
\boxed{\|\mathbf L-\mathbf L_*\|_F^2=\|\mathbf L-\widehat{\mathbf L}\|_F^2+\|\boldsymbol\mu-\boldsymbol\mu_*\|_2^2}
$$

The first term measures the discarded mixing of modes; the second measures the additional change to the diagonal needed to satisfy the graph sign conditions. If $\boldsymbol\mu$ already lies in the cone, the second term vanishes. Unlike $\Pi_U$, projection onto the cone is generally nonlinear and need not preserve the trace. To use the connected resistance model, the result must satisfy $\mu_{*,k}>0$ for every $k$.

## Example: a cycle, rotated modes, and negative conductances

Consider the unit cycle $1-2-3-4-1$ with the following eigenbasis on $H$:

$$
\mathbf u_1=\frac1{\sqrt{10}}(2,1,-2,-1)^{\mathsf T},\qquad
\mathbf u_2=\frac1{\sqrt{10}}(-1,2,1,-2)^{\mathsf T},\qquad
\mathbf u_3=\frac12(1,-1,1,-1)^{\mathsf T}
$$

The first two modes belong to the eigenspace with eigenvalue $2$; the third has eigenvalue $4$. The vertex labels and this particular basis remain fixed below.

Add an edge $\{1,3\}$ of conductance $5$ to the cycle. For the resulting graph,

$$
\mathbf S=
\begin{pmatrix}10&-4&0\\-4&4&0\\0&0&4\end{pmatrix},\qquad
\boldsymbol\mu=(10,4,4)
$$

The original nonzero eigenvalues are $2,4,12$. After removing the mixed coefficients, they become $10,4,4$, and the squared error is $(-4)^2+(-4)^2=32$.

For an arbitrary diagonal $(a,b,c)$ in this basis, the candidate conductances are

$$
\begin{aligned}
w_{12}=w_{34}&=\frac c4-\frac{a-b}{5}\\
w_{14}=w_{23}&=\frac c4+\frac{a-b}{5}\\
w_{13}&=\frac{4a+b}{10}-\frac c4\\
w_{24}&=\frac{a+4b}{10}-\frac c4
\end{aligned}
$$

At $(a,b,c)=(10,4,4)$, this gives

$$
w_{12}=w_{34}=-\frac15,\qquad
w_{14}=w_{23}=\frac{11}{5},\qquad
w_{13}=\frac{17}{5},\qquad w_{24}=\frac85
$$

The negative values indicate a violation of the graph condition. They are not admissible conductances of an ordinary electrical network.

The nearest point in the cone can be found exactly. The violated inequality is $4a-4b-5c\le0$. Orthogonal projection onto its boundary plane gives

$$
\boldsymbol\mu_*=(10,4,4)-\frac4{57}(4,-4,-5)
=\frac1{57}(554,244,248)
$$

Substitution into the remaining conditions yields nonnegative conductances:

$$
w^*_{12}=w^*_{34}=0,\qquad
w^*_{14}=w^*_{23}=\frac{124}{57},\qquad
w^*_{13}=\frac{184}{57},\qquad w^*_{24}=\frac{91}{57}
$$

This proves optimality: the entire cone lies in the indicated half-space, and the nearest point in that half-space already belongs to the cone. The resulting graph is connected. For this graph,

$$
\|\boldsymbol\mu-\boldsymbol\mu_*\|_2^2=\frac{16}{57},\qquad
\|\mathbf L-\mathbf L_*\|_F^2=32+\frac{16}{57}=\frac{1840}{57}
$$

The trace of the unconstrained projection equals the original trace $18$, whereas the trace of $\mathbf L_*$ is $1046/57$. The trace change is computed directly here.

![[Diagonal Projection and the Nearest Graph on Four Vertices.svg]]

*Figure 1. The original cycle with an additional conductance of $5$, its unconstrained diagonal projection, and the nearest graph in the cone. The dashed orange links in the middle diagram have negative coefficients. These links are absent from the nearest admissible graph. The vertex labels are the same in all three diagrams.*

## Different graphs with the same projection

Replace the two mixed coefficients $-4$ by a parameter $r$:

$$
\mathbf S_r=\begin{pmatrix}10&r&0\\r&4&0\\0&0&4\end{pmatrix}
$$

In vertex coordinates, this gives

$$
\begin{aligned}
w_{12}=w_{34}&=-\frac{2+3r}{10}\\
w_{14}=w_{23}&=\frac{22+3r}{10}\\
w_{13}&=\frac{17-2r}{5},\qquad
w_{24}=\frac{8+2r}{5}
\end{aligned}
$$

All conductances are nonnegative for $-4\le r\le-2/3$. The graphs are connected throughout this interval: $\det\mathbf S_r=4(40-r^2)>0$. Yet their diagonal projections coincide, and their squared errors are $2r^2$. Their nearest points in the cone also coincide, since that problem depends only on $\boldsymbol\mu$.

However, the rooted forest polynomial, spanning-tree coefficient, and Kirchhoff index vary:

$$
\begin{aligned}
P_r(t)&=1+18t+(96-r^2)t^2+4(40-r^2)t^3\\
\tau_r&=40-r^2,\qquad
\operatorname{Kf}_r=1+\frac{56}{40-r^2}
\end{aligned}
$$

For example:

| Quantity | $r=-4$ | $r=-2$ |
|---|---:|---:|
| Diagonal coefficients | $(10,4,4)$ | $(10,4,4)$ |
| Spanning-tree coefficient $\tau$ | $24$ | $36$ |
| Rooted coefficient $p_2$ | $80$ | $92$ |
| Ordinary forest coefficient $f_2$ | $26$ | $716/25$ |
| Kirchhoff index | $10/3$ | $23/9$ |
| Resistance $R_{13}$ | $1/6$ | $1/5$ |
| Resistance $R_{24}$ | $1$ | $26/45$ |

The graph at $r=-4$ has no edge $\{2,4\}$, whereas all six edges are present at $r=-2$. These are different weighted graphs, already distinguished by $\tau$. Their common projection determines neither the forest polynomials nor the individual resistances; the latter may change in opposite directions.

![[Different Graphs with One Spectral Projection.svg]]

*Figure 2. Two members of the family $\mathbf S_r$ have the same diagonal projection but different conductances, spanning-tree coefficients, and resistances. The right panel shows how two resistances vary over the full admissible parameter interval. The marked points identify the graphs in the table.*

In this family, equal projections accompany different spectra. A different loss of data is illustrated by the [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms#Cospectral graphs with different forest polynomials|cospectral pair on four vertices]]: there the spectrum is the same, but its assignment to eigenspaces differs. Having the same spectrum and having the same projection onto a prescribed basis are different conditions.

## Projection of grades and the exponential of a projection

Pass to the affine vectors $u_k=\sum_i u_k(i)a_i\in W$ and the forms $A_k=[u_k]^2$. Use the coordinate identification of a form with an operator adopted in [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]]. The full first-grade expression is

$$
L=\sum_i\mu_i A_i+\sum_{i<j}S_{ij}\{u_i,u_j\},\qquad
\widehat L=\sum_i\mu_i A_i
$$

Here $\{u_i,u_j\}=[u_i,u_j]+[u_j,u_i]$, without a factor of $1/2$. After projection, diagonal factorization gives

$$
\widehat M(t)=\exp(t\widehat L)=\prod_i(e+t\mu_iA_i),\qquad
\widehat M_g=e_g(\mu_1A_1,\ldots,\mu_dA_d)
$$

This is the exterior exponential in the algebra of forms. No matrix exponential is used here.

For the original $M(t)=\exp(tL)$, the coefficients in the exterior-product basis are minors. If $I=(i_1<\cdots<i_g)$ and $u_I=u_{i_1}\cdots u_{i_g}$, then

$$
M_g=\sum_{|I|=|J|=g}\det\mathbf S_{I,J}\,[u_I,u_J]
$$

Indeed, $M_g=L^g/g!$. Expanding the product and antisymmetrizing its two exterior arguments gives the determinant $\det\mathbf S_{I,J}$, while the factor $g!$ accounts for the orders in which the terms can be selected. This is also the matrix of the exterior power of the operator $\Lambda^g(\mathbf L|_H)$; the identification used here is explained in [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]].

Define $\Pi_U^{(g)}$ by removing the mixed coefficients of a form **in the already constructed** grade-$g$ basis $u_I$. Then

$$
\Pi_U^{(g)}(M_g)=\sum_{|I|=g}\det\mathbf S_{I,I}\,[u_I]^2,\qquad
\widehat M_g=\sum_{|I|=g}\left(\prod_{i\in I}\mu_i\right)[u_I]^2
$$

In general, these are different forms. At $g=2$, the difference is visible in every diagonal coefficient:

$$
\det\begin{pmatrix}\mu_i&S_{ij}\\S_{ij}&\mu_j\end{pmatrix}
=\mu_i\mu_j-S_{ij}^2
$$

For the family $\mathbf S_r$, we obtain

$$
\begin{aligned}
M_2&=(40-r^2)[u_1u_2]^2+40[u_1u_3]^2+16[u_2u_3]^2+4r\{u_1u_3,u_2u_3\}\\
M_3&=4(40-r^2)[u_1u_2u_3]^2
\end{aligned}
$$

Projection of the already formed second grade removes the final mixed term but retains the coefficient $40-r^2$. Constructing $\widehat M_2$ from the projected first grade replaces this coefficient by $40$. The top grade is already one-dimensional, so $\Pi_U^{(3)}(M_3)=M_3$, whereas $\widehat M_3=160[u_1u_2u_3]^2$.

Consequently, projection is not a homomorphism of the polyform algebra: it does not commute with multiplication or the exterior exponential. To discuss projection of an arbitrary polyform, its action on each grade must be defined separately; diagonalizing the first grade alone is insufficient.

## What is preserved in the scalar coefficients

The coordinate evaluation $\operatorname{ev}_0([u_I,u_J])=\delta_{IJ}$ gives

$$
p_g=\sum_{|I|=g}\det\mathbf S_{I,I},\qquad
\widehat p_g=e_g(\mu_1,\ldots,\mu_d)
$$

Thus, projecting each already formed grade preserves its coordinate evaluation: $\operatorname{ev}_0(\Pi_U^{(g)}M_g)=p_g$. The exponential of the projected first grade, however, has different evaluations $\widehat p_g$.

For a positive definite matrix, Hadamard's inequality bounds the determinant by the product of the diagonal entries; see [N. Higham, What Is the Determinant of a Matrix?, Theorem 1](https://nhigham.com/2021/06/22/what-is-the-determinant-of-a-matrix/). Applying it to each principal minor of $\mathbf S$ gives

$$
p_g\le\widehat p_g,\qquad
p_0=\widehat p_0=1,\qquad p_1=\widehat p_1=\operatorname{tr}\mathbf L
$$

For $d\ge2$, the second coefficient satisfies the exact identity

$$
\boxed{\widehat p_2-p_2=\sum_{i<j}S_{ij}^2
=\frac12\|\mathbf L-\Pi_U(\mathbf L)\|_F^2}
$$

For a graph Laplacian, $p_1=2\sum_{i<j}w_{ij}=2f_1$. Thus the unconstrained projection preserves the total sum of edge coefficients. The remaining ordinary forest coefficients $f_g$ cannot be replaced by the rooted coefficients $p_g$; the inequality above is established specifically for $p_g$. The different normalizations are explained in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

In the example under consideration, $P_{-4}(t)=1+18t+80t^2+96t^3$, whereas $\widehat P(t)=1+18t+96t^2+160t^3$. The latter polynomial is obtained here from the positive form $\widehat L$ with a signed edge expression. It cannot be attributed to the admissible approximating graph $G_*$. After the additional projection onto the cone, the coefficients must be recomputed; preservation of $p_1$ and the comparisons with $\widehat p_g$ do not automatically carry over to that step.

## The Greenian, inversion, and dual grades

On $H$, the Green matrix is represented by the inverse matrix $\mathbf S^{-1}$. Thus two natural operations give

$$
\Pi_U(\mathbf{Gr})=\sum_k\nu_k\mathbf E_k,\qquad
\nu_k=(\mathbf S^{-1})_{kk},\qquad
\widehat{\mathbf L}^{+}=\sum_k\mu_k^{-1}\mathbf E_k
$$

In general, $\nu_k\ne\mu_k^{-1}$. For a selected index $k$, move it to the first position and write $\mathbf S$ as

$$
\mathbf S=\begin{pmatrix}\mu_k&\mathbf s^{\mathsf T}\\\mathbf s&\mathbf C\end{pmatrix},\qquad
\nu_k=\frac1{\mu_k-\mathbf s^{\mathsf T}\mathbf C^{-1}\mathbf s}\ge\frac1{\mu_k}
$$

This is the Schur complement formula for inversion; its classical derivation is given in [N. Higham, What Is the Schur Complement of a Matrix?](https://nhigham.com/2023/06/01/what-is-the-schur-complement-of-a-matrix/). The denominator is positive, and the subtracted quantity is nonnegative. Equality for a given $k$ means that its row contains no mixed coefficients. When $d=1$, there are no mixed coefficients, and equality holds directly.

It follows that $\operatorname{tr}\widehat{\mathbf L}^{+}\le\operatorname{tr}\mathbf{Gr}$. If the unconstrained projection is itself a connected graph Laplacian, this gives $\operatorname{Kf}(\widehat G)\le\operatorname{Kf}(G)$. No componentwise ordering of individual resistances follows: the original Greenian still contains mixed coefficients.

For the graph at $r=-4$,

$$
\mathbf S^{-1}=\begin{pmatrix}1/6&1/6&0\\1/6&5/12&0\\0&0&1/4\end{pmatrix},\qquad
\boldsymbol\nu=(1/6,5/12,1/4),\qquad
\boldsymbol\mu^{-1}=(1/10,1/4,1/4)
$$

Thus, projection of the Laplacian and projection of the Greenian do not form an inverse pair on $H$.

In the language of polyforms, this distinction requires retaining the algebraic dual space. Let $u^k$ be the basis dual to $u_k$, and let $A_k^\vee=[u^k]^2$. The exponential dual to $\widehat M(1)$ is $\widehat D(1)$; its grade-generating expression is

$$
\widehat D(t)=\prod_k(e+t\mu_k^{-1}A_k^\vee),\qquad
\widehat M_d/\widehat Q_g=\widehat M_{d-g}
$$

Here $\widehat Q_g$ and $\widehat M_g$ are the grades of $\widehat D(1)$ and $\widehat M(1)$, and $/$ denotes dual contraction. Scaling the first grade by $s>0$ makes $\widehat D(s^{-1})$ dual to $\widehat M(s)$; see the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter convention]]. The centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$ takes $\widehat D(t)$ to $\exp(t\widehat{\mathrm{Gr}})$, where $\widehat{\mathrm{Gr}}$ corresponds to $\widehat{\mathbf L}^{+}$. This differs from the resistance identification. The formulas and normalizations are established in [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]].

If instead the original dual first grade is projected independently, its coefficients become $\nu_k$. The exponential $\prod_k(e+\nu_kA_k^\vee)$ is generally not dual to $\widehat M(1)$.

At $r=-4$, we have $T_4=4[u_1u_2u_3]^2$. The top grades of the original and unconstrained projected forms are

$$
M_3=24T_4,\qquad N_3=\frac{T_4}{384},\qquad
\widehat M_3=40T_4,\qquad \widehat N_3=\frac{T_4}{640}
$$

Here $N=\exp(\mathrm{Gr})$, and $\widehat N=\mathcal C(\widehat D)$ at $t=1$. The number $40$ in the second pair is a coefficient of a positive form with a signed edge expression; it should not be called the spanning-tree coefficient of the admissible approximating graph $G_*$. For $G_*$, the dual pair is constructed anew from $\mathbf L_*$ and $\mathbf L_*^+$.

A small Laplacian error alone does not guarantee a small resistance error when the positive eigenvalues are small. More precisely, for two connected graph Laplacians $\mathbf L$ and $\widetilde{\mathbf L}$ whose smallest eigenvalues on $H$ are $\gamma>0$ and $\widetilde\gamma>0$,

$$
\left\|\mathbf L^+-\widetilde{\mathbf L}^{+}\right\|_{\mathrm{op}}
\le\frac{\|\mathbf L-\widetilde{\mathbf L}\|_F}{\gamma\widetilde\gamma},\qquad
|R_{ij}-\widetilde R_{ij}|
\le\frac{2\|\mathbf L-\widetilde{\mathbf L}\|_F}{\gamma\widetilde\gamma}
$$

This follows from the identity for the difference of inverse operators on $H$, the bound of the operator norm by the Frobenius norm, and $\|\mathbf e_i-\mathbf e_j\|_0^2=2$. Here $\mathbf e_i$ is a standard coordinate vector.

## Multiplicities and projection onto eigenspaces

If the reference Laplacian $\mathbf L_0$ has repeated eigenvalues, the choice of individual $\mathbf u_k$ within its eigenspaces is not canonical. Hence $\Pi_U$ depends on that choice. An alternative operation preserves whole blocks:

$$
\Pi_{\mathrm{blk}}(\mathbf L)=\sum_\lambda\mathbf F_\lambda\mathbf L\mathbf F_\lambda
$$

Here $\mathbf F_\lambda$ are the orthogonal spectral projectors of the **reference** $\mathbf L_0$. This is the Frobenius projection onto the space of symmetric matrices commuting with $\mathbf L_0$: diagonal blocks are retained, while blocks between distinct eigenspaces are set to zero. This follows from the block representation of the matrix; for projectors, see [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]].

For a simple spectrum, the two projections coincide. With multiplicities, block projection is independent of basis rotations within each eigenspace and preserves more data:

$$
\|\mathbf L-\Pi_U(\mathbf L)\|_F^2=\|\mathbf L-\Pi_{\mathrm{blk}}(\mathbf L)\|_F^2+\|\Pi_{\mathrm{blk}}(\mathbf L)-\Pi_U(\mathbf L)\|_F^2
$$

In our example, the entire block $\begin{pmatrix}10&r\\r&4\end{pmatrix}$ lies within the two-dimensional eigenspace of $C_4$ with eigenvalue $2$. Therefore $\Pi_{\mathrm{blk}}(\mathbf L_r)=\mathbf L_r$. The whole error $2r^2$ arises from the additional removal of mixed coefficients within this eigenspace. In general, the result of block projection also requires verification of the graph sign conditions.

A disconnected original graph requires a separate qualification. Its positive semidefinite matrix can have strictly positive diagonal evaluations in every chosen direction of $H$, so diagonal projection can increase rank. For example, in the basis of the path $P_3$, a unit edge $\{1,2\}$ with isolated vertex $3$ has evaluations $(1/2,3/2)$ and projects to a path with both conductances equal to $1/2$. Connectivity of the projection does not prove connectivity of the original graph; the inversion formulas for a positive definite $\mathbf S$ above do not apply to a disconnected original graph.

## Limits of spectral comparison and sources

The full matrix $\mathbf S$ in a fixed basis stores the original operator. Its diagonal stores only the evaluations of the chosen directions. The spectrum of the original operator, in turn, stores eigenvalues with multiplicities but not the positions of the eigenspaces in vertex coordinates. These are three different datasets.

A centered symmetric operator has $d(d+1)/2$ independent coordinates; diagonal projection retains $d$ of them. The discarded $d(d-1)/2$ mixed coordinates affect eigendirections, forest coefficients, conductances, and resistances. Equal diagonal projections therefore imply neither equal spectra nor graph isomorphism. Comparisons require consistent vertex labels and a consistent choice of basis.

Diagonal and block projections, projection onto a convex cone, Hadamard's inequality, and inversion formulas are classical matrix constructions. Here they are expressed in the language of polyforms, explicitly distinguishing projection of grades, the exterior exponential, and duality. Boundary polynomials and gluing, followed by spectra of chains of cores, remain separate continuations: ordinary forest states cannot be identified with characteristic boundary data without proof.

Exact computations independently compare edge matrices, projections, principal minors, exterior exponentials, and forest enumeration. The checks cover all 64 simple labeled graphs on four vertices in the chosen basis, 21 rational points of the family, and full polyform calculations for five admissible graphs and the unconstrained projection. Optimality of the projection onto the cone is proved using a half-space; computations verify its coordinates and every sign condition. The figures are constructed from these formulas.

- [R. Bhatia. Pinching, Trimming, Truncating, and Averaging of Matrices](https://doi.org/10.1080/00029890.2000.12005245). The American Mathematical Monthly, 107(7), 602–608, 2000: classical operations that remove matrix blocks and their relation to norms.
- [S. Boyd, L. Vandenberghe. Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), §8.1.1: Euclidean projection onto a convex set, a half-space, and a cone. [The authors' book page](https://web.stanford.edu/~boyd/cvxbook/).
- [N. J. Higham. What Is the Determinant of a Matrix?](https://nhigham.com/2021/06/22/what-is-the-determinant-of-a-matrix/), Theorem 1: Hadamard's inequality; [What Is the Schur Complement of a Matrix?](https://nhigham.com/2023/06/01/what-is-the-schur-complement-of-a-matrix/): the Schur complement and block inversion.
- [[en/Foundations/Core specification|Core specification]], [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]], [[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]]: spaces, forms, projectors, normalizations, and graph sign conditions.
- [Checks and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral): exact calculations for projections and the family $\mathbf S_r$.

Series navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
