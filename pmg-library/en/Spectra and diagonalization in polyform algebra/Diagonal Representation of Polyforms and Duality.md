---
title: "Diagonal Representation of Polyforms and Duality"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: diagonal-representation-of-polyforms-and-duality
order: 1
description: "Eigendirections of the Laplacian and Greenian, exterior-exponential grades as elementary symmetric polynomials in forms, and reversal of complementary grades under duality. An exact P3 example."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Диагональное представление полиформ и дуальность|Русский]]

Forest polynomials and scalar parameters allow graphs to be compared, but do not show the directions along which their Laplacians act. A spectral representation retains these directions. In the language of polyforms it has a particularly simple expression: the exterior exponential splits into factors associated with eigenvectors, and its grades become elementary symmetric polynomials in the corresponding forms. The same law applies on the dual side; reciprocal eigenvalues relate complementary grades in reverse order.

This is the opening note of the series “Spectra and Diagonalization in Polyform Algebra”. The main example is the three-vertex path. It allows every form to be written explicitly and shows exactly what survives when a full polyform is replaced by a numerical polynomial. The general algebra of the exterior exponential is developed in [[en/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian|The Exterior Exponential and Representations of the Greenian]]; here we study its diagonal expression and spectral meaning.

## Space, metric, and operator

Let $G$ be a connected undirected loopless graph on $n\ge2$ vertices, with positive conductances on its existing edges. Put $d=n-1$. Its Laplacian matrix $\mathbf L$ is symmetric, has zero row sums, and satisfies $L_{ij}=-c_{ij}\le0$ for $i\ne j$.

In the coordinate space, distinguish

$$
H=\{\mathbf v\in\mathbb R^n:\mathbf1^{\mathsf T}\mathbf v=0\},\qquad
\langle\mathbf v,\mathbf w\rangle_0=\mathbf v^{\mathsf T}\mathbf w
$$

A column $\mathbf v\in H$ corresponds to the affine vector $v=\sum_i v_i a_i$ in $W$. Transfer the auxiliary inner product $\langle\ ,\ \rangle_0$ to $W$. It determines the coordinate normalization of eigenvectors. The PMG resistance inner product is defined differently:

$$
v\cdot w=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf w,\qquad
\mathbf{Gr}=\mathbf L^+
$$

Here $\mathbf{Gr}$ inverts $\mathbf L$ on $H$ and vanishes on constant columns. These definitions agree with the [[en/Foundations/Core specification#The resistance metric|core specification]].

The formal form $[v,w]$ is not itself an operator. Given the auxiliary inner product, it corresponds to the operator $z\mapsto v\langle w,z\rangle_0$. Under precisely this identification, the form

$$
L=\sum_{i<j}c_{ij}[a_j-a_i]^2
$$

represents the ordinary Laplacian operator. The choice of metric matters: contracting the second argument of the same form using the resistance inner product gives the operator $\mathbf L\mathbf{Gr}|_H=I_H$.

By the spectral theorem, $H$ has a basis $\mathbf u_1,\ldots,\mathbf u_d$, orthonormal with respect to $\langle\ ,\ \rangle_0$, such that

$$
\mathbf L\mathbf u_\alpha=\lambda_\alpha\mathbf u_\alpha,\qquad
\mathbf{Gr}\mathbf u_\alpha=\lambda_\alpha^{-1}\mathbf u_\alpha,\qquad
\lambda_\alpha>0
$$

The constant mode $\mathbf u_0=\mathbf1/\sqrt n$ has eigenvalue $0$ for both matrices and does not belong to $H$. Hence

$$
\mathbf L=\sum_{\alpha=1}^d\lambda_\alpha\mathbf u_\alpha\mathbf u_\alpha^{\mathsf T},\qquad
\mathbf{Gr}=\sum_{\alpha=1}^d\lambda_\alpha^{-1}\mathbf u_\alpha\mathbf u_\alpha^{\mathsf T}
$$

Eigenvectors specify directions, and eigenvalues specify the multipliers along them. In the resistance metric these vectors are orthogonal, but their quadratic norms are $u_\alpha\cdot u_\alpha=\lambda_\alpha^{-1}$, rather than $1$.

For a repeated eigenvalue, the individual vectors within its eigenspace can be changed by an orthogonal transformation. The uniquely determined object is the projector

$$
\mathbf E_\lambda=\sum_{\alpha:\lambda_\alpha=\lambda}
\mathbf u_\alpha\mathbf u_\alpha^{\mathsf T}
$$

Thus the basis-independent expressions are $\mathbf L=\sum_{\lambda>0}\lambda\mathbf E_\lambda$ and $\mathbf{Gr}=\sum_{\lambda>0}\lambda^{-1}\mathbf E_\lambda$. These projectors sum to $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$.

## Eigenmodes of the three-vertex path

For the path $1-2-3$ with unit conductances,

$$
\mathbf L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\qquad
\mathbf{Gr}=\frac19\begin{pmatrix}5&-1&-4\\-1&2&-1\\-4&-1&5\end{pmatrix}
$$

The nonzero modes and their corresponding vectors in $W$ are

$$
\begin{aligned}
\mathbf u_1&=\frac1{\sqrt2}(1,0,-1)^{\mathsf T},&
u_1&=\frac{a_1-a_3}{\sqrt2},&\lambda_1&=1\\
\mathbf u_2&=\frac1{\sqrt6}(1,-2,1)^{\mathsf T},&
u_2&=\frac{a_1-2a_2+a_3}{\sqrt6},&\lambda_2&=3
\end{aligned}
$$

The first mode distinguishes the endpoints; the second distinguishes the middle vertex from the two endpoints. Reversing the signs of all components of a mode changes neither its projector nor its quadratic form.

![[Eigenmodes of the Path P3.svg]]

*Figure 1. Eigenvector components at the path vertices. Blue means a positive component, orange a negative one, and grey zero; the numbers are exact. The multipliers of the Laplacian and Green matrices are shown on the right. The constant mode is separated from the two directions of the centered space.*

One common basis serves two matrices with different eigenvalues. This already shows why sharing an eigenbasis does not mean having the same spectrum.

## Diagonal forms and symmetric polynomials of the grades

Return to an arbitrary connected graph. Denote the forms associated with its eigenvectors by

$$
\ell_\alpha=\lambda_\alpha[u_\alpha]^2
$$

The first grade then has the diagonal expression

$$
L=\ell_1+\cdots+\ell_d
$$

Polyform algebra uses the rule $[X,Y][A,B]=[XA,YB]$. Products of arguments are exterior products; the form product is commutative because the two interchange signs cancel. For each eigendirection,

$$
\ell_\alpha^2=\lambda_\alpha^2[u_\alpha\wedge u_\alpha]^2=0
$$

**Theorem (diagonal factorization).** For the exterior exponential $M=\exp L$ and a formal scalar parameter $t$,

$$
\boxed{
M(t)=\exp(tL)=\prod_{\alpha=1}^d(e+t\ell_\alpha)
=\sum_{g=0}^d t^g M_g,\qquad
M_g=\frac{L^g}{g!}
}
$$

If $e_g$ denotes the elementary symmetric polynomial evaluated in the commutative algebra of forms, then

$$
\boxed{
M_g=e_g(\ell_1,\ldots,\ell_d)
=\sum_{\#I=g}\lambda_I[u_I]^2
}
$$

Here $I\subseteq\{1,\ldots,d\}$, $u_I=u_{i_1}\cdots u_{i_g}$ with $i_1<\cdots<i_g$, and $\lambda_I=\prod_{\alpha\in I}\lambda_\alpha$. For the empty set, $u_\varnothing=1$, $\lambda_\varnothing=1$, and $[1]^2=e$. In the algebra of forms, $e_0=e$; for numerical arguments, $e_0=1$.

**Proof.** Commutativity allows the exponential of a sum to be written as a product of exponentials. Since $\ell_\alpha^2=0$, we have $\exp(t\ell_\alpha)=e+t\ell_\alpha$. Selecting $g$ nonzero terms produces a product of forms associated with $g$ distinct directions. Each such set occurs $g!$ times in $L^g$, giving the stated grade component. $\square$

For example, for three eigendirections all grades are

$$
\begin{aligned}
M_0&=e\\
M_1&=\ell_1+\ell_2+\ell_3\\
M_2&=\ell_1\ell_2+\ell_1\ell_3+\ell_2\ell_3\\
M_3&=\ell_1\ell_2\ell_3
\end{aligned}
$$

These are symmetric polynomials **in the eigendirection forms weighted by $\lambda_\alpha$**. Grade $g$ is diagonal in the induced exterior basis $u_I$. Its individual diagonal coefficients are the products $\lambda_I$; their sum is the numerical elementary symmetric polynomial in the eigenvalues.

Changing the basis within a repeated eigenspace may change individual terms, but not the sum $M_g=L^g/g!$. Moreover, the formula concerns the exponential of a symmetric grade-one form: the higher grades of an arbitrary polyform need not be determined by its first grade or diagonalized by the same basis of the underlying space.

## From grade polyforms to numerical coefficients

Extend the auxiliary inner product to exterior powers through the Gram determinant. Write its linear evaluation on forms as $\operatorname{ev}_0$:

$$
\operatorname{ev}_0([X,Y])=\langle X,Y\rangle_0,\qquad
\operatorname{ev}_0([u_I]^2)=1
$$

Then

$$
\operatorname{ev}_0(M_g)=\sum_{\#I=g}\lambda_I
=e_g(\lambda_1,\ldots,\lambda_d)=p_g
$$

This gives the rooted forest polynomial

$$
P_G(t)=\sum_{g=0}^d p_g t^g
=\prod_{\alpha=1}^d(1+t\lambda_\alpha)
=\det(I+t\mathbf L)
$$

The equality of these coefficients with sums of rooted forest weights is proved in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]. Ordinary forest coefficients $f_g$ do not include a choice of root in each component and differ from $p_g$. A formal factorization of their polynomial does not turn its parameters into eigenvalues; this distinction is discussed in [[en/Matroid parameters and forest characteristics of graphs/The Normalized Forest Polynomial and Power-Sum Parameters|The Normalized Forest Polynomial and Power-Sum Parameters]].

The evaluation $\operatorname{ev}_0$ is linear but is not an algebra homomorphism. For example, $([u_\alpha]^2)^2=0$, whereas $\operatorname{ev}_0([u_\alpha]^2)=1$. The formula for $P_G$ follows from the diagonal expansion, where every term uses distinct directions.

Resistance evaluation gives different numbers. For $M=\exp L$, the normalized potential is defined by $P_M(f)=\tau(Mf)/\tau(M)$ and agrees with metric evaluation of forms. Therefore

$$
P_M([u_I]^2)=\lambda_I^{-1},\qquad
P_M(M_g)=\binom dg
$$

Here $\tau$ extracts the coefficient of the fixed spanning-tree form $T_n=[(a_1\ldots a_n)]^2$. Thus **a grade coefficient in a coordinate basis and its resistance evaluation are different data**. For one diagonal term, the product of the coefficient $\lambda_I$ and the resistance norm $\lambda_I^{-1}$ is $1$.

## The spectrum and recoverable scalar data

The characteristic polynomial is expressed through the same rooted coefficients:

$$
\chi_G(\xi)=\det(\xi I-\mathbf L)
=\sum_{g=0}^d(-1)^g p_g\xi^{n-g}
=\xi^nP_G(-1/\xi)
$$

For $\xi\ne0$, the last expression follows by substituting the parameter; after expansion it is a polynomial identity, valid also at $\xi=0$. With $n$ known, the spectrum with multiplicities, $\chi_G$, and $P_G$ determine one another.

For a connected graph,

$$
\boxed{
\tau(G)=\frac{p_d}{n},\qquad
\operatorname{tr}\mathbf{Gr}=\frac{p_{d-1}}{p_d},\qquad
\operatorname{Kf}(G)=n\frac{p_{d-1}}{p_d}
}
$$

The first equality is the spectral form of Kirchhoff's theorem. The second follows from $e_{d-1}(\lambda)/e_d(\lambda)=\sum_\alpha\lambda_\alpha^{-1}$; the third uses $\operatorname{Kf}=n\operatorname{tr}\mathbf{Gr}$, justified in [[en/Polynomial toponomes/Coefficients and Kirchhoff Indices|Coefficients and Kirchhoff Indices]]. The highest rooted coefficients therefore connect the spanning-tree weight with the total resistance characteristic.

| Data | Is the spectrum with multiplicities sufficient? |
|---|---|
| $p_g$, $\chi_G$, $\tau(G)$, $\operatorname{tr}\mathbf{Gr}$, $\operatorname{Kf}(G)$ | Yes |
| The forms $L$, $\mathrm{Gr}$ and full grades $M_g$, $N_g$ | In general, projectors in vertex coordinates are needed |
| Conductances $c_{ij}$ and individual effective resistances $R_{ij}$ | In general, projectors are needed |
| Ordinary forest coefficients $f_g$ | In general, the spectrum is insufficient |

The last distinction already appears on four vertices: a [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms#Cospectral graphs with different forest polynomials|cospectral pair]] has identical $p_g$ but different $f_2$. Full polyforms retain data that disappear under numerical evaluation.

## The dual exponential and complementary directions

Let $u^1,\ldots,u^d\in W^*$ be the algebraically dual basis: $u^\alpha(u_\beta)=\delta_{\alpha\beta}$. These functionals must be distinguished from the resistance covectors $u_\alpha\cdot(\ )$, which equal $\lambda_\alpha^{-1}u^\alpha$.

The dual representation of the Greenian is

$$
Q_1=\sum_{\alpha=1}^d\lambda_\alpha^{-1}[u^\alpha]^2
$$

Let $a_i^\vee$ denote the restriction of the $i$th coordinate functional to $W$. Under the centered identification

$$
\mathcal C:a_i^\vee\mapsto a_i-h,\qquad
h=\frac1n\sum_i a_i
$$

we have $\mathcal C(u^\alpha)=u_\alpha$, since the eigenbasis is orthonormal in the auxiliary coordinate metric. This identification, rather than the resistance Riesz identification, is used in the formulas

$$
\mathrm{Gr}=\mathcal C(Q_1)=\sum_\alpha\lambda_\alpha^{-1}[u_\alpha]^2,\qquad
D=\exp Q_1,\qquad N=\mathcal C(D)=\exp(\mathrm{Gr})
$$

Write $u^I=u^{i_1}\cdots u^{i_g}$ for the exterior product of dual elements in increasing index order. The dual exponential factors in the same way:

$$
D(t)=\prod_{\alpha=1}^d\bigl(e+t\lambda_\alpha^{-1}[u^\alpha]^2\bigr)
$$

$$
Q_g=e_g\bigl(\lambda_1^{-1}[u^1]^2,\ldots,\lambda_d^{-1}[u^d]^2\bigr)
=\sum_{\#I=g}\lambda_I^{-1}[u^I]^2
$$

Put $\Delta=\prod_{\alpha=1}^d\lambda_\alpha$. Since $\lambda_I^{-1}=\lambda_{I^c}/\Delta$,

$$
\boxed{
Q_g=\frac1\Delta\sum_{\#I=g}\lambda_{I^c}[u^I]^2
}
$$

This is the precise meaning of reversing the order: the term $\lambda_{I^c}[u_{I^c}]^2$ in direct grade $d-g$ corresponds to $\lambda_{I^c}[u^I]^2/\Delta$ in dual grade $g$. One must take the complementary set of directions, pass to the dual space, and divide the coefficient by $\Delta$. Simply reversing the symbols $M_0,\ldots,M_d$ does not express this operation.

The connection with the definition of duality through exterior contraction is

$$
M_d/Q_g=M_{d-g},\qquad Q_d/M_g=Q_{d-g}
$$

Indeed, contracting $u_1\cdots u_d$ by $u^I$ leaves $u_{I^c}$ up to sign. The signs cancel between the two form arguments, while $\Delta\lambda_I^{-1}$ becomes $\lambda_{I^c}$. Full proofs of mutuality appear in [[en/Greenian and polyform duality/Laplacian and Greenian - Mutual Duality of Exponentials|Laplacian and Greenian - Mutual Duality of Exponentials]] and the [[en/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian#The dual exponential of a nondegenerate symmetric form|exponential duality theorem]].

Graph normalization must account for volume. The Gram matrix of the differences $a_i-a_n$, $1\le i<n$, in the auxiliary metric has determinant $n$. Hence

$$
T_n=n[u_1\cdots u_d]^2,\qquad
\Delta=n\tau(G)
$$

The second equality also follows from Kirchhoff's theorem. Consequently,

$$
M_d=\tau(G)T_n,\qquad
N_d=\frac{T_n}{n^2\tau(G)}
$$

The factor $1/\Delta$ in the diagonal coefficients and the factor $1/(n^2\tau)$ multiplying $T_n$ refer to different basis forms. They cannot be substituted for one another.

Numerical evaluation after the transfer $\mathcal C$ gives the corresponding reversal of coefficients:

$$
e_g(\lambda_1^{-1},\ldots,\lambda_d^{-1})
=\frac{e_{d-g}(\lambda_1,\ldots,\lambda_d)}{\Delta}
$$

It follows from the richer relationship between grade polyforms, which retains the eigendirections.

## The grade parameter and rescaling a dual pair

In $M(t)=\sum_g t^gM_g$ and $D(t)=\sum_g t^gQ_g$, the parameter $t$ marks the grade. The forms $M_g$ and $Q_g$ are the components of the original dual pair $M=M(1)$, $D=D(1)$. Thus $M_d/Q_g=M_{d-g}$ refers to these coefficients; $M(t)$ and $D(t)$ themselves do not in general form a dual pair at the same arbitrary $t$.

Now consider physical rescaling: multiply all conductances by a number $s>0$. Then $\mathbf L$ is multiplied by $s$ and $\mathbf{Gr}$ by $s^{-1}$, and the mutually dual exponentials become

$$
M(s)=\exp(sL),\qquad D(s^{-1})=\exp(s^{-1}Q_1)
$$

Their grades are $s^gM_g$ and $s^{-g}Q_g$. Bilinearity of exterior contraction gives the consistent scaling:

$$
(s^dM_d)/(s^{-g}Q_g)=s^{d-g}M_{d-g}
$$

The symbol $/$ denotes contraction: the coefficient of the contracting form multiplies the result rather than being inverted. Incorrectly substituting $s^gQ_g$ would produce $s^{d+g}$. This convention for the formal parameter and physical scale is used throughout the series.

## All grades and duality for the path P3

For brevity put $A=[u_1]^2$, $B=[u_2]^2$, $A^\vee=[u^1]^2$, and $B^\vee=[u^2]^2$. In this section $A,B$ denote forms, not matrices. For the path, $\lambda_1=1$, $\lambda_2=3$, $\Delta=3$, and $\tau=1$. Thus

$$
\begin{aligned}
L&=A+3B,&M(t)&=(e+tA)(e+3tB)\\
Q_1&=A^\vee+\tfrac13B^\vee,&D(t)&=(e+tA^\vee)(e+\tfrac t3B^\vee)
\end{aligned}
$$

All grades are collected in the table.

| Grade $g$ | $M_g$ | $Q_g$ | $\operatorname{ev}_0(M_g)$ | $P_M(M_g)$ |
|---:|---|---|---:|---:|
| $0$ | $e$ | $e$ | $1$ | $1$ |
| $1$ | $A+3B$ | $A^\vee+\frac13B^\vee$ | $4$ | $2$ |
| $2$ | $3AB$ | $\frac13A^\vee B^\vee$ | $3$ | $1$ |

Here $T_3=3AB$, so $M_2=T_3$ and $N_2=T_3/9$. In particular, $A^2=B^2=0$ and commutativity give $L^2=6AB$ and $M_2=L^2/2=3AB$.

![[Complementary Grades of the Path P3.svg]]

*Figure 2. Termwise correspondence between the direct and dual exponentials. Each row replaces a direction set by its complement and divides its coefficient by $\Delta=3$. Direct grade zero becomes dual grade two, and direct grade two becomes dual grade zero. In grade one the directions are also exchanged: the coefficient of $A$ determines that of $B^\vee$, and the coefficient of $B$ determines that of $A^\vee$.*

For example,

$$
(3AB)/(A^\vee+\tfrac13B^\vee)=3B+A=M_1
$$

The two extreme identities are $(3AB)/e=M_2$ and $(3AB)/(A^\vee B^\vee/3)=e=M_0$. In every case, $/$ means exterior contraction, not division in the commutative algebra.

Duality does not mean invertibility under ordinary polyform multiplication. After transfer to $W$, we have $MN=\exp(L+\mathrm{Gr})$, whereas the multiplicative inverse of $M$ is $\exp(-L)$.

The scalar polynomials are

$$
\det(I+t\mathbf L)=1+4t+3t^2,\qquad
\det(I+t\mathbf{Gr})=1+\frac43t+\frac13t^2
$$

Reversing $(1,4,3)$ and dividing by $3$ gives $(1,4/3,1/3)$. The ordinary forest polynomial of the same path is $F_{P_3}(t)=1+2t+t^2$: there are two one-edge forests and one spanning tree. In the rooted count, a one-edge forest has two choices of root in its two-vertex component, and the tree has three choices. This produces the coefficients $4$ and $3$.

## Two metric evaluations in one eigenbasis

The polyform $M=\exp L$ induces the resistance metric, and $N=\exp(\mathrm{Gr})$ the energy metric, as established in [[en/Greenian and polyform duality/The Greenian Metric and Potentials|The Greenian Metric and Potentials]]. For $w=a u_1+b u_2$ on the path $P_3$,

$$
P_M([w]^2)=a^2+\frac{b^2}{3},\qquad
P_N([w]^2)=a^2+3b^2
$$

These are quadratic norms. The auxiliary coordinate quadratic norm of the same vector is $a^2+b^2$.

![[Two Metrics in the P3 Basis.svg]]

*Figure 3. Unit level sets of the resistance and energy evaluations in the coefficient plane $(a,b)$. The dashed curve is the unit level set of the auxiliary coordinate metric. Along $u_1$ the evaluations agree; along $u_2$ their coefficients $1/3$ and $3$ are reciprocal. The figure depicts the vector space $W$, not positions of graph vertices.*

Effective resistances are recovered using eigenvector components:

$$
R_{ij}=\sum_{\alpha=1}^d
\frac{(u_{\alpha i}-u_{\alpha j})^2}{\lambda_\alpha}
$$

For the path, $R_{12}=R_{23}=1$ and $R_{13}=2$. Eigenvalues alone suffice for the sum over all pairs:

$$
\operatorname{Kf}(G)=\sum_{i<j}R_{ij}
=n\operatorname{tr}\mathbf{Gr}
=n\sum_{\alpha=1}^d\lambda_\alpha^{-1}
$$

In this example, $\operatorname{Kf}(P_3)=3(1+1/3)=4$. Coefficient formulas for this index appear in [[en/Polynomial toponomes/Coefficients and Kirchhoff Indices|Coefficients and Kirchhoff Indices]].

## What the diagonal representation retains

A full representation consists of eigenvalues and projectors in fixed vertex coordinates. It recovers $\mathbf L$ and $\mathbf{Gr}$, hence the forms $L$, $\mathrm{Gr}$, their exponentials, and pairwise effective resistances. For a simple weighted graph, conductances are recovered as $c_{ij}=-L_{ij}$; if parallel edges are allowed, the matrix determines only their total conductances.

Eigenvalues alone determine the sums of diagonal grade coefficients, but not the forms $[u_I]^2$ themselves. With $n$ known, the spectrum with multiplicities and the characteristic polynomial $\det(\xi I-\mathbf L)=\xi\prod_{\alpha=1}^d(\xi-\lambda_\alpha)$ contain the same information. That information omits the projectors and generally does not determine a graph up to isomorphism.

When constructing an operator from prescribed modes and positive numbers, the off-diagonal signs must be checked separately. Positive semidefiniteness and zero row sums alone do not ensure $L_{ij}\le0$. These additional constraints define the spectral cone of a fixed basis.

Finally, distinguish three constructions. Under the auxiliary metric identification, grade $M_g$ corresponds to $\Lambda^g(\mathbf L|_H)$, whose eigenvalues are the products $\lambda_I$. The operator obtained by summing the actions of $\mathbf L$ on each of the $g$ exterior factors has eigenvalues $\sum_{\alpha\in I}\lambda_\alpha$. The matrix exponential $\exp(t\mathbf L)$ acts on the original space with multipliers $\exp(t\lambda_\alpha)$. It differs from the polyform $\exp(tL)$, which combines several grades.

All inversion formulas here concern the connected symmetric case. For a disconnected graph the pseudoinverse still exists, but $H$ contains zero directions, $\Delta=0$, and division by $\Delta$ is unavailable. Nonsymmetric balanced-graph Laplacians also require separate treatment.

## Status and sources

Diagonalization of a symmetric operator, exterior powers, and the relationship between elementary symmetric polynomials and the determinant are classical results. Here they are reconciled with PMG formal forms, mutual duality of exponentials, and the established normalization of $T_n$. Factorization and complementary coefficient reversal are proved in the text; the figures and numerical identities for $P_3$ come from exact computation. A computational example does not replace a general proof.

- [[en/Foundations/Core specification|Core specification]] and [[en/Foundations/PMG terminology|PMG terminology]] - spaces, forms, normalized potentials, and current notation.
- [[en/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian|The Exterior Exponential and Representations of the Greenian]] - factorization, minors, and mutual duality of exponentials in an arbitrary basis.
- [[en/Greenian and polyform duality/Laplacian and Greenian - Mutual Duality of Exponentials|Laplacian and Greenian - Mutual Duality of Exponentials]] - complementary grades defined through exterior contraction.
- [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] and [[en/Greenian and polyform duality/The Greenian Metric and Potentials|The Greenian Metric and Potentials]] - scalar polynomials and the two metric evaluations.
- [Jonathan Kelner. Lecture on spectral graph theory, MIT 18.409](https://ocw.mit.edu/courses/18-409-topics-in-theoretical-computer-science-an-algorithmists-toolkit-fall-2009/7c5d4c779c64e9ed3a5783a80b7eb0a5_MIT18_409F09_scribe2.pdf), notes by Mergen Nachin - the Laplacian, eigenvalues, and eigenvectors.
- [A. Belkhirat, M. L. Labbi. Interactions between the composition and exterior products of double forms and applications](https://arxiv.org/html/1402.4072v1#S5), § 5, Proposition 5.1 - correspondence between the exterior exponential of a double form and the induced operator on the exterior algebra; exterior and composition products are defined in §§ 2–3.
- [P. Chebotarev, E. Shamis. Matrix-Forest Theorems](https://arxiv.org/abs/math/0602575) - Laplacian-type determinants and rooted forests.
- [Exact verification and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral) - comparison of edge and spectral expansions, grades, metrics, and normalizations.

Basis independence for repeated eigenvalues and operator reconstruction are developed in [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]]. Explicit families are studied in [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]] and [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]], and sign constraints in [[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]]. Boundary polynomials and gluing, as well as spectra of chains of cores, remain separate directions.

Navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
