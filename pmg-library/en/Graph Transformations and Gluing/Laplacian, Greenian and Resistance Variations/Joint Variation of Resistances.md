---
title: Joint Variation of Resistances
date: 2026-10-31
updated: 2026-11-08
revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: variations-joint-resistances
lang: en
description: 'Two changing resistances and the general case on a vertex set: the spanning-tree coefficient, conductances, Greenian factors, and direct solution of the matrix equation.'
order: 6
translated_revision: 6
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/Joint Variation of Resistances"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Совместное изменение резистенсов|Русский]]

In [[One Resistance and Quadric Connectivity]], one resistance changed while all others were preserved. We now prescribe several changes simultaneously. Greenian updates add linearly, but the resulting conductance updates cannot simply be added: inversion accounts for their joint action.

We begin with two resistances of a triangle, then obtain a formula for changes between vertices of a prescribed set $S$. Every resistance with no assigned increment is preserved. The calculation reduces to a linear system of size $|S|$.

## An example with two resistances

A unit triangle has $c_{12}=c_{13}=c_{23}=1$, all resistances equal to $2/3$, and spanning-tree coefficient $\tau=3$. Prescribe

$$
R'_{12}=R'_{13}=1,\qquad R'_{23}=\frac23
$$

Thus two resistances increase by $1/3$, while the third remains fixed.

![A unit triangle and the new conductances when resistances 12 and 13 increase to one while resistance 23 is preserved](<images/Two Resistances of a Triangle.svg>)

*Numbers beside edges denote conductances. Two couplings weaken and the third strengthens, although its corresponding resistance remains fixed.*

> [!example] The answer for the triangle
> The new conductances and spanning-tree coefficient are
>
> $$
> c'_{12}=c'_{13}=\frac35,\qquad c'_{23}=\frac65,
> \qquad \boxed{\tau'=\frac95}
> $$
>
> Verification using trees and separating forests:
>
> $$
> \tau'=\frac35\frac35+\frac35\frac65+\frac35\frac65=\frac95
> $$
>
> $$
> R'_{12}=R'_{13}=\frac{3/5+6/5}{9/5}=1,\qquad
> R'_{23}=\frac{3/5+3/5}{9/5}=\frac23
> $$

### Two arbitrary increments

Set $R'_{12}=2/3+\alpha$, $R'_{13}=2/3+\beta$, keeping $R'_{23}=2/3$. Introduce the common denominator

$$
\Phi(\alpha,\beta)=1+\alpha+\beta-\frac34(\alpha-\beta)^2
\tag{1}
$$

> [!info] Explicit formulas for two resistances of a triangle
> For $\Phi\ne0$,
>
> $$
> \boxed{\begin{gathered}
> \tau'=\frac3\Phi,\\
> c'_{12}=\frac{1-3\alpha/2+3\beta/2}{\Phi},\\
> c'_{13}=\frac{1+3\alpha/2-3\beta/2}{\Phi},\\
> c'_{23}=\frac{1+3\alpha/2+3\beta/2}{\Phi}
> \end{gathered}}
> \tag{2}
> $$
>
> The increments are obtained by subtracting the original values: $\Delta\tau=3/\Phi-3$, $\Delta c_{ij}=c'_{ij}-1$.

Formulas (1)-(2) will be derived below by substitution into the general formula. Setting $\alpha=\beta=1/3$ gives $\Phi=5/3$ and the numbers in the example. Setting $\beta=0$ recovers [[One Resistance and Quadric Connectivity#Substitution for the triangle|the single-resistance formulas]].

The mixed term is directly visible here:

$$
\Phi=1+\alpha+\beta-\frac34\alpha^2
+\frac32\alpha\beta-\frac34\beta^2
$$

The joint response is therefore not the sum of two responses calculated from the original graph. A sequential calculation gives the same answer if the intermediate Greenian is nondegenerate; the second step uses the changed Laplacian. In the numerical example, the first step gives $\tau_1=12/5$ and conductances $2/5,6/5,6/5$. The multiplier at the second step is $4/3$, so $\tau'=(12/5)/(4/3)=9/5$.

## Changes on a prescribed vertex set

Here the **entire** new resistance table is prescribed: increments outside the selected block are zero. In [[Variations with Conductance Constraints|the constrained problem]], only boundary resistances will be prescribed and the others will be free. These are different inverse problems.

The original graph is undirected, its conductances are nonnegative, and its set of $n\ge2$ vertices is fixed. Connectedness is determined by edges of positive conductance and is assumed initially. Matrices $\mathbf L$ and $\mathbf{Gr}$ are mutual inverses on $\mathbf1^\perp$ and annihilate the constant column.

Choose $S=\{s_1,\ldots,s_r\}$ and prescribe a symmetric increment matrix $\mathbf F$ of size $r$ with zero diagonal:

$$
F_{ab}=\Delta R_{s_a s_b},\qquad F_{aa}=0
$$

A zero entry $F_{ab}$ means that the corresponding resistance is preserved. All resistances with at least one endpoint outside $S$ also remain fixed. This specifies the entire new resistance matrix, not just boundary values.

Let $\mathbf E$ be the vertex-selection matrix: its columns are $\mathbf e_{s_1},\ldots,\mathbf e_{s_r}$. Then

$$
\Delta\mathbf R=\mathbf E\mathbf F\mathbf E^{\mathsf T},\qquad
\mathbf R'=\mathbf R+\Delta\mathbf R
\tag{3}
$$

### Matrices needed for the calculation

All the following quantities are calculated from the original Laplacian:

$$
\mathbf H=\mathbf E^{\mathsf T}\mathbf L\mathbf E=\mathbf L_{SS},
\qquad \mathbf B=\mathbf L\mathbf E
$$

Matrix $\mathbf H$ has size $r\times r$, while $\mathbf B$ consists of the selected columns of $\mathbf L$. Write row $i$ of matrix $\mathbf B$ as a transposed column:

$$
\mathbf b_i=(L_{i s_1},\ldots,L_{i s_r})^{\mathsf T}
$$

> [!info] The joint response of the spanning-tree coefficient and couplings
> **Theorem.** Set
>
> $$
> \mathbf A=\mathbf I_r-\frac12\mathbf F\mathbf H,
> \qquad \Phi=\det\mathbf A
> \tag{4}
> $$
>
> For $\Phi\ne0$, define
>
> $$
> \mathbf K=\mathbf A^{-1}\frac{\mathbf F}{2}
> \tag{5}
> $$
>
> Then
>
> $$
> \boxed{\tau'=\frac\tau\Phi,\qquad
> \Delta\tau=\tau\left(\frac1\Phi-1\right)}
> \tag{6}
> $$
>
> $$
> \boxed{\mathbf L'=\mathbf L+\mathbf B\mathbf K\mathbf B^{\mathsf T}}
> \tag{7}
> $$
>
> For $i\ne j$,
>
> $$
> \boxed{\Delta c_{ij}=-\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j}
> \tag{8}
> $$
>
> Matrix $\mathbf K$ is symmetric. Neither $\mathbf F$ nor $\mathbf H$ needs to be inverted: zero increments, singular $\mathbf F$, and choosing $S$ as the full vertex set are allowed.

These are finite formulas. Sign and metric constraints are given after the derivation; invertibility of $\mathbf A$ alone does not ensure nonnegative conductances.

> [!note]- Substitution for two resistances of a triangle
> **Proof.** In the example, $S=\{1,2,3\}$, $\mathbf E=\mathbf I_3$, $\mathbf H=\mathbf B=\mathbf L$, and
>
> $$
> \mathbf F=\begin{pmatrix}
> 0&\alpha&\beta\\\alpha&0&0\\\beta&0&0
> \end{pmatrix},\qquad
> \mathbf L=\begin{pmatrix}
> 2&-1&-1\\-1&2&-1\\-1&-1&2
> \end{pmatrix}
> $$
>
> Calculating $\det(\mathbf I_3-\mathbf F\mathbf L/2)$ gives (1). Substitution into (5)-(8) gives (2). An independent check substitutes conductances (2) into the three triangle resistance formulas and the spanning-tree sum. $\square$

### Calculation guide

| Matrix | Size | Role |
|---|---|---|
| $\mathbf E$ | $n\times r$ | Selects the vertices in $S$ |
| $\mathbf F$ | $r\times r$ | Prescribed resistance increments |
| $\mathbf H$ | $r\times r$ | Initial block $\mathbf L_{SS}$ |
| $\mathbf B$ | $n\times r$ | Selected columns of the initial Laplacian |
| $\mathbf A$ | $r\times r$ | System matrix in $\mathbf A\mathbf K=\mathbf F/2$ |
| $\mathbf K$ | $r\times r$ | Update matrix yielding $\Delta\mathbf L$ |

First form $\mathbf F,\mathbf H,\mathbf B$, then check admissibility and solve one linear system for $\mathbf K$. Compute the new conductances and verify the resistances. This fully prescribed table does not require iterative search.

For example, in the unit triangle take $S=\{1,2\}$ and $\Delta R_{12}=1/3$. Then

$$
\mathbf F=\frac13\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\mathbf H=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
\mathbf A=\begin{pmatrix}7/6&-1/3\\-1/3&7/6\end{pmatrix}
$$

$$
\Phi=\frac54,\qquad
\mathbf K=\frac1{45}\begin{pmatrix}2&7\\7&2\end{pmatrix}
$$

For pair $12$, the columns $\mathbf b_1=(2,-1)^{\mathsf T}$, $\mathbf b_2=(-1,2)^{\mathsf T}$ give $\Delta c_{12}=-3/5$, hence $c'_{12}=2/5$. This recovers the verified example with one changed resistance coordinate.

## Derivation through Greenian factors

Set $h=n^{-1}\sum_i a_i$, $p_i=a_i-h$, and $\mathbf J=\mathbf I_n-\mathbf1\mathbf1^{\mathsf T}/n$. By [[The Canonical Vector Representation of the Greenian|the linear transformation from resistances]],

$$
\begin{aligned}
\Delta\mathbf{Gr}&=-\frac12\mathbf J\Delta\mathbf R\mathbf J\\
&=-\frac12\mathbf J\mathbf E\mathbf F\mathbf E^{\mathsf T}\mathbf J
\end{aligned}
\tag{9}
$$

In particular, the canonical coefficients change linearly: $\Delta\gamma_{ij}=(\mathbf J\Delta\mathbf R\mathbf J)_{ij}/2$ for $i<j$.

### Two factors for each changing pair

For each pair $k<l$ with increment $\delta_{kl}$, introduce fixed directions

$$
u_{kl}=p_k-p_l,\qquad v_{kl}=p_k+p_l
$$

As shown by [[One Resistance and Quadric Connectivity#One resistance as two vector contributions|the two-factor representation of a single-resistance change]],

$$
\Delta\mathrm{Gr}=\sum_{k<l}\frac{\delta_{kl}}4
\bigl([u_{kl}]^2-[v_{kl}]^2\bigr)
$$

Thus, for the exterior exponential $N=\exp(\mathrm{Gr})$,

$$
N'=N\prod_{k<l}
\left(e+\frac{\delta_{kl}}4[u_{kl}]^2\right)
\left(e-\frac{\delta_{kl}}4[v_{kl}]^2\right)
\tag{10}
$$

The product need only run over the changing pairs. Two resistances give up to four vector factors. Their mixed products are included in the expansion; dependencies among directions make the corresponding exterior products vanish.

### Reduction to a matrix indexed by the selected vertices

> [!note]- Proof of the general formula from the factor representation
> **Proof.** To apply [[Joint Variation of Greenian Coefficients#Several Greenian coefficients|the general vector-contribution formula]], diagonalize the symmetric increment matrix:
>
> $$
> \begin{gathered}
> \mathbf F=\mathbf O\operatorname{diag}(f_1,\ldots,f_r)\mathbf O^{\mathsf T},\\
> \mathbf O^{\mathsf T}\mathbf O=\mathbf I_r
> \end{gathered}
> $$
>
> Introduce $u_\alpha=\sum_a O_{a\alpha}p_{s_a}$ and $t_\alpha=-f_\alpha/2$. From (9),
>
> $$
> \mathrm{Gr}'=\mathrm{Gr}+\sum_\alpha t_\alpha[u_\alpha]^2,
> \qquad N'=N\prod_\alpha(e+t_\alpha[u_\alpha]^2)
> $$
>
> The Gram matrix of these directions in metric $N$ is $\mathbf G=\mathbf O^{\mathsf T}\mathbf H\mathbf O$. The top-grade coefficient formula gives
>
> $$
> \begin{aligned}
> \frac{\sigma'}\sigma
> &=\det\left(\mathbf I_r-\frac12
> \operatorname{diag}(f_\alpha)\mathbf G\right)\\
> &=\det\left(\mathbf I_r-\frac12\mathbf F\mathbf H\right)=\Phi
> \end{aligned}
> $$
>
> For $\sigma=1/(n^2\tau)$, this is exactly (6). The Laplacian update formula from the same note, after returning to the original coordinates, gives
>
> $$
> \mathbf L'-\mathbf L
> =\mathbf B\left(\mathbf I_r-\frac12\mathbf F\mathbf H\right)^{-1}
> \frac{\mathbf F}{2}\mathbf B^{\mathsf T}
> $$
>
> This proves (7)-(8). Finally,
>
> $$
> \left(\mathbf I_r-\frac12\mathbf F\mathbf H\right)\mathbf F
> =\mathbf F\left(\mathbf I_r-\frac12\mathbf H\mathbf F\right)
> $$
>
> implies
>
> $$
> \begin{aligned}
> \mathbf K&=\left(\mathbf I_r-\frac12\mathbf F\mathbf H\right)^{-1}
> \frac{\mathbf F}{2}\\
> &=\frac{\mathbf F}{2}\left(\mathbf I_r-\frac12\mathbf H\mathbf F\right)^{-1}
> \end{aligned}
> $$
>
> The outer expressions are transposes of one another, so $\mathbf K$ is symmetric. $\square$

Diagonalization is used here for the derivation. It is unnecessary for calculating (4)-(8). Representation (10) and the eigenvector representation describe the same Greenian update, hence the same exterior exponential and its grades.

## Solving the matrix equation

Let $\Delta\mathbf L=\mathbf L'-\mathbf L$. From (9) and inversion on the zero-sum space, the exact identity is

$$
\boxed{\begin{aligned}
\Delta\mathbf L&=\frac12\mathbf L'\Delta\mathbf R\mathbf L\\
&=\frac12\mathbf L\Delta\mathbf R\mathbf L'
\end{aligned}}
\tag{11}
$$

The factor $1/2$ corresponds to our symmetric matrix $\Delta\mathbf R$: changing one independent coordinate places equal increments in two entries, $kl$ and $lk$.

> [!note]- Proof of the finite matrix identity
> **Proof.** Both pairs of mutually inverse matrices on $\mathbf1^\perp$ satisfy $\mathbf L\mathbf{Gr}=\mathbf L'\mathbf{Gr}'=\mathbf J$. Thus
>
> $$
> \mathbf L'(\mathbf{Gr}'-\mathbf{Gr})\mathbf L
> =\mathbf L-\mathbf L'
> $$
>
> Substitute $\Delta\mathbf{Gr}=-\mathbf J\Delta\mathbf R\mathbf J/2$ and use $\mathbf L'\mathbf J=\mathbf L'$, $\mathbf J\mathbf L=\mathbf L$. This gives the first equality in (11). Transposition gives the second. $\square$

The presence of $\mathbf L'$ on the right does not make the equation nonlinear: the unknown matrix appears only once in each term. Move it to the left-hand side:

$$
\mathbf L'\left(\mathbf I_n-\frac12\Delta\mathbf R\mathbf L\right)=\mathbf L
$$

> [!info] Direct solution
> **Theorem.** For $\Phi\ne0$, equation (11) has a unique solution:
>
> $$
> \boxed{\mathbf L'
> =\mathbf L\left(\mathbf I_n-\frac12\Delta\mathbf R\mathbf L\right)^{-1}}
> \tag{12}
> $$
>
> Equivalently, $\mathbf L'=(\mathbf I_n-\mathbf L\Delta\mathbf R/2)^{-1}\mathbf L$. The solution is symmetric, has zero row sums, and recovers the entire prescribed matrix $\mathbf R'$.

> [!note]- Why a solution exists exactly when the multiplier is nonzero
> **Proof.** The identity $\det(I-UV)=\det(I-VU)$ gives
>
> $$
> \begin{aligned}
> \det\left(\mathbf I_n-\frac12\Delta\mathbf R\mathbf L\right)
> &=\det\left(\mathbf I_r-\frac12\mathbf F\mathbf H\right)\\
> &=\Phi
> \end{aligned}
> $$
>
> For $\Phi\ne0$, the matrix on the right is therefore invertible and the solution is unique. Formula (7), already derived through the Greenian, satisfies the same equation. This confirms symmetry and agreement of (7) with (12). The factor in brackets preserves the constant column, so $\mathbf L'\mathbf1=0$.
>
> For $\Phi=0$, there is a nonzero $\mathbf x$ satisfying $(\mathbf I_n-\Delta\mathbf R\mathbf L/2)\mathbf x=0$. Moreover, $\mathbf L\mathbf x\ne0$; otherwise, that equality would imply $\mathbf x=0$. Hence the equation $\mathbf L'(\mathbf I_n-\Delta\mathbf R\mathbf L/2)=\mathbf L$ is inconsistent. There is no finite solution of (11). $\square$

Formula (12) is a form of the classical matrix-sum inversion identity for this variation. For comparison, see Petersen and Pedersen, [*The Matrix Cookbook*, § 3.2.3, formula (159)](https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf#page=18). Here it is also obtained from Greenian factors and independently checked by the finite identity (11).

### Solving only for the selected columns

There is no need to invert the full matrix of size $n$. Set $\mathbf X=\mathbf L'\mathbf E$. Multiplying (11) on the right by $\mathbf E$ gives

$$
\mathbf X=\mathbf B+\frac12\mathbf X\mathbf F\mathbf H,
\qquad \mathbf X\mathbf A=\mathbf B
$$

Hence $\mathbf X=\mathbf B\mathbf A^{-1}$ and

$$
\Delta\mathbf L=\frac12\mathbf X\mathbf F\mathbf B^{\mathsf T}
=\mathbf B\mathbf K\mathbf B^{\mathsf T}
$$

This obtains (7) directly from the matrix equation. In practice, it suffices to solve $\mathbf A\mathbf K=\mathbf F/2$ with several right-hand sides; explicitly computing $\mathbf A^{-1}$ is optional.

## Invertibility and graph admissibility

> [!info] Three separate checks
> **Proposition.** For an initially connected graph:
>
> 1. The new Greenian is nondegenerate on $\mathbf1^\perp$ if and only if $\Phi\ne0$.
> 2. It is positive definite on that space if and only if
>
> $$
> \boxed{\mathbf I_r-\frac12\mathbf H^{1/2}\mathbf F\mathbf H^{1/2}\succ0}
> \tag{13}
> $$
>
> 3. After (13) is checked, a connected graph with nonnegative conductances is obtained if and only if all $c'_{ij}=c_{ij}-\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j$ are nonnegative.

> [!note]- Proof of the positivity criterion
> **Proof.** On $\mathbf1^\perp$, multiplying (9) on both sides by $\mathbf L^{1/2}$ gives $I-\mathbf Y\mathbf F\mathbf Y^{\mathsf T}/2$, where $\mathbf Y=\mathbf L^{1/2}\mathbf J\mathbf E$ and $\mathbf Y^{\mathsf T}\mathbf Y=\mathbf H$.
>
> As in [[Joint Variation of Greenian Coefficients#Invertibility, positivity, and conductance signs|the criterion for multiple contributions]], the polar decomposition of $\mathbf Y$ identifies its range with that of $\mathbf H^{1/2}$. On these ranges, the resulting matrix and the matrix in (13) have the same restrictions, while on the complementary subspaces they act as the identity. Their positive definiteness is therefore equivalent. The argument allows singular $\mathbf H$.
>
> Under (13), the inverse form is also positive definite on $\mathbf1^\perp$. Together with zero row sums and nonnegative conductances, this gives a connected graph. $\square$

A positive determinant $\Phi>0$ is generally insufficient for (13). If $S$ is a proper nonempty subset of vertices, $\mathbf H$ is positive definite and (13) can be replaced by the equivalent condition $\mathbf H^{-1}-\mathbf F/2\succ0$. This replacement is inapplicable when $S$ contains all vertices.

At $\Phi=0$, the factor product remains meaningful, but the top-grade coefficient vanishes and the inverse form cannot be recovered. With negative conductances, the formulas remain algebraic, and $\tau'$ denotes a signed spanning-tree cofactor.

## Which couplings can change

Formula (8) gives exact locality:

$$
\mathbf b_i=0\quad\Longrightarrow\quad
\Delta L_{ij}=0\quad\text{for all }j
$$

Let $W$ denote $S$ together with all its neighbors in the original graph. For nonnegative original conductances, the nonzero rows of $\mathbf B$ correspond precisely to vertices in $W$. Thus only pairs with **both endpoints in $W$** can change.

This does not mean that a changing coupling must have an endpoint in $S$. For example, on the path $1-2-3-4$ with $S=\{2,3\}$, the recovered matrix may acquire a nonzero coefficient for pair $14$. This describes the location of the update; nonnegativity of the resulting conductances is checked separately. Originally zero couplings within $W$ are not automatically preserved.

To preserve $c_{ij}=0$ on a selected pair, one must check $\mathbf b_i^{\mathsf T}\mathbf K\mathbf b_j=0$. When $\mathbf R'$ is fully prescribed, the solution is already unique: its conductances cannot be adjusted further while preserving the entire resistance matrix. A fixed-edge-set problem needs other free data, for example permission to change some of the remaining resistances.

![Where a Coupling Can Change](<images/Where a Coupling Can Change.svg>)

*Changing the resistance of pair $23$ can affect pair $14$, although both endpoints lie outside $S$. The diagram shows the algebraic support of the update; conductance signs must be checked separately.*

## Differentials and sequential changes

For a small update $\mathbf F$, we have $\mathbf K=\mathbf F/2+O(\|\mathbf F\|^2)$. The finite formulas therefore reduce to

$$
d\mathbf L=\frac12\mathbf L(d\mathbf R)\mathbf L
$$

In independent coordinates $R_{kl}=R_{lk}$, this means

$$
dc_{ij}=-\sum_{k<l}Lq^{ij,kl}\,dR_{kl},\qquad
\frac{d\tau}{\tau}=\sum_{k<l}L_{kl}\,dR_{kl}
$$

Thus [[One Resistance and Quadric Connectivity#Quadric connectivity|quadric connectivity]] gives the first-order part of the general finite response.

If changes are applied sequentially, recalculate $\mathbf L$, $\mathbf H$, $\mathbf B$, and $\tau$ at every step. If intermediate forms are invertible, the result agrees with the simultaneous calculation: updates of $\mathbf{Gr}$ add, and its inverse is unique. The normalization factors of consecutive steps multiply. If an intermediate form is degenerate, that order of recalculation is inapplicable even when the joint final update is invertible.

For example, in the triangle with $\alpha=\beta=2$, formulas (1)-(2) give positive conductances $1/5,1/5,7/5$. But changing only one of the two resistances by $2$ first makes its separate multiplier $1+2-3\cdot2^2/4$ zero. Both two-step sequences break down, whereas the joint calculation is defined.

![A Joint Step and a Singular Intermediate State](<images/A Joint Step and a Singular Intermediate State.svg>)

*At $\alpha=\beta=2$, the joint response has positive conductances. Either full first step makes the intermediate Greenian singular.*

### Is iteration needed?

One linear system $\mathbf A\mathbf K=\mathbf F/2$ suffices. The iteration $\mathbf X_{m+1}=\mathbf B+\mathbf X_m\mathbf F\mathbf H/2$ can also be considered, but its convergence requires a separate condition.

> [!note]- A sufficient convergence condition and its limitation
> **Proof.** Suppose the spectral radius of $\mathbf T=\mathbf F\mathbf H/2$ is less than $1$. Then $\mathbf T^m\to0$, and the Neumann series gives $(\mathbf I_r-\mathbf T)^{-1}=\sum_{m\ge0}\mathbf T^m$. The iteration error is multiplied on the right by $\mathbf T$, so it tends to zero from every initial approximation.
>
> Invertibility of $\mathbf I_r-\mathbf T$ alone does not ensure such convergence. For example, if all resistances of a unit triangle are increased by a factor of $3$, then $\mathbf F=2\mathbf R$, $\mathbf T=-2\mathbf J$. The exact solution is entirely admissible: $\mathbf L'=\mathbf L/3$, all conductances equal $1/3$, and $\tau'=1/3$. But the spectral radius of $\mathbf T$ is $2$, and the iteration starting at $\mathbf X_0=\mathbf B$ diverges. $\square$

## Calculation procedure and verification

1. Form a symmetric $\mathbf F$ with zero diagonal; all preserved coordinates have zero increments.
2. Take $\mathbf H=\mathbf L_{SS}$ and $\mathbf B=\mathbf L\mathbf E$, and calculate $\mathbf A$ and $\Phi$ using (4).
3. Check $\Phi\ne0$. For a graph solution, also check positivity in (13).
4. Solve $\mathbf A\mathbf K=\mathbf F/2$. Obtain $\tau'$ from (6), and $\mathbf L'$ and the conductances from (7)-(8).
5. Check the required signs and preservation of prescribed zero couplings. Recover the resistances from the new Greenian and compare them with the entire matrix $\mathbf R+\Delta\mathbf R$.

Approximate-number calculations near $\Phi=0$ require conditioning checks: a small input change can produce large changes in the inverse form. The small examples below are checked in exact rational arithmetic.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_joint_resistances.py) compares vector-factor expansions by grade, recovery through exterior contraction, direct inversion, solution of full and reduced matrix systems, and enumeration of trees and separating forests. Checks include one weighted edge, triangles, the path $P_4$, and the cycle $C_4$; changes to two adjacent or two disjoint pairs; proper vertex subsets and all vertices; singular updates, negative conductances, and approach to degeneracy. Sequential recalculation and the divergent-iteration example are checked separately.

From the repository root:

    python checks/variations/verify_joint_resistances.py

Finite-rank matrix inversion and the determinant identity belong to classical matrix theory; further sources are collected in [[Further Reading for the PMG Introductory Series]]. This note establishes their agreement with Greenian vector factors, spanning-tree normalization, and independent resistance coordinates.

In [[Variations with Conductance Constraints]], resistances are prescribed only on a selected vertex set, leaving the others free. This allows the problem of preserving zero couplings and nonnegativity of permitted conductances to be posed; the prism example shows the limits of its solvability.

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
