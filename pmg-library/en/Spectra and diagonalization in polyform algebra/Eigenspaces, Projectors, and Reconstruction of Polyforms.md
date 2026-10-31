---
title: "Eigenspaces, Projectors, and Reconstruction of Polyforms"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: eigenspaces-projectors-and-reconstruction-of-polyforms
order: 2
description: "Eigenspaces and projectors, reconstruction of polyforms and resistances, multiplicities, exterior powers, and a cospectral weighted pair with different forest coefficients."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Собственные подпространства, проекторы и восстановление полиформ|Русский]]

In the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|diagonal representation]], the grades of the exterior exponential are symmetric polynomials in eigendirection forms. Eigenvectors, however, need not be unique: an eigenspace associated with a repeated eigenvalue admits different orthonormal bases. Which parts of the representation change, and which are determined by the polyform itself?

Spectral projectors provide the answer. They retain eigenspaces in vertex coordinates and recover the Laplacian, the Greenian, and every grade of their exponentials. Individual modal terms can be grouped into forms of entire eigenspaces. Diagonal factorization then accounts for multiplicities while preserving symmetric polynomials and mutual duality of complementary grades.

The running example is the cycle $C_4$ with unit conductances. Its spectrum $0,2,2,4$ contains a two-dimensional eigenspace, so the distinction between a basis and a projector is visible on just four vertices.

## Spaces and normalization

Consider a connected undirected loopless graph on $n\ge2$ vertices, with positive conductances on existing edges. Write $d=n-1$. The coordinate space of affine vectors is

$$
H=\mathbf1^\perp\subset\mathbb R^n,\qquad
\langle\mathbf v,\mathbf w\rangle_0=\mathbf v^{\mathsf T}\mathbf w
$$

A column $\mathbf v\in H$ corresponds to $v=\sum_i v_i a_i\in W$. Eigenvectors are normalized using the auxiliary inner product $\langle\ ,\ \rangle_0$. The PMG resistance inner product is $v\cdot w=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf w$, where $\mathbf{Gr}=\mathbf L^+$. It does not replace coordinate normalization. Spaces and metrics are defined in [[en/Foundations/Core specification|Core specification]].

Let $\Sigma$ be the set of distinct positive eigenvalues of $\mathbf L$. For $\lambda\in\Sigma$, put

$$
H_\lambda=\ker(\mathbf L-\lambda I),\qquad
m_\lambda=\dim H_\lambda,\qquad
H=\bigoplus_{\lambda\in\Sigma}H_\lambda
$$

The sum is orthogonal with respect to $\langle\ ,\ \rangle_0$, and $\sum_\lambda m_\lambda=d$. On $H_\lambda$, the Green matrix acts with multiplier $\lambda^{-1}$. The constant zero mode $\mathbf1/\sqrt n$ is not in $H$.

## Replacing one eigenbasis by another

Number the vertices of $C_4$ along the cycle $1-2-3-4-1$. Its Laplacian is

$$
\mathbf L=
\begin{pmatrix}
2&-1&0&-1\\
-1&2&-1&0\\
0&-1&2&-1\\
-1&0&-1&2
\end{pmatrix}
$$

An orthonormal basis of $H_2$ is

$$
\mathbf u=\frac1{\sqrt2}(1,0,-1,0)^{\mathsf T},\qquad
\mathbf v=\frac1{\sqrt2}(0,1,0,-1)^{\mathsf T}
$$

The one-dimensional space $H_4$ is spanned by

$$
\mathbf w=\frac12(1,-1,1,-1)^{\mathsf T}
$$

Rotating the basis in $H_2$ gives other eigenvectors with the same eigenvalue:

$$
\begin{aligned}
\widetilde{\mathbf u}&=\frac{\mathbf u+\mathbf v}{\sqrt2}
=\frac12(1,1,-1,-1)^{\mathsf T}\\
\widetilde{\mathbf v}&=\frac{-\mathbf u+\mathbf v}{\sqrt2}
=\frac12(-1,1,1,-1)^{\mathsf T}
\end{aligned}
$$

For the first two modes, nonzero values are concentrated on opposite vertices; for the rotated modes, all four components are nonzero. These are different descriptions of one eigenspace. With a repeated eigenvalue, the signs and locations of components of an individual eigenvector are not uniquely determined graph characteristics.

![[Two Bases and a Common Projector of C4.svg]]

*Figure 1. Two orthonormal bases of the eigenspace $H_2$ of $C_4$. Color indicates the sign of a component; labels give exact values. The right-hand panel shows the same projector matrix $\mathbf E_2$ obtained in both bases. Individual modes change, but the eigenspace and its projector do not.*

## Projectors recover the operator action

Let the columns of $\mathbf U_\lambda$ be an orthonormal basis of $H_\lambda$. Define

$$
\mathbf E_\lambda=\mathbf U_\lambda\mathbf U_\lambda^{\mathsf T}
$$

> [!info] Projectors recover the operator action
> **Theorem.** The matrix $\mathbf E_\lambda$ is independent of the orthonormal basis chosen in $H_\lambda$ and is the orthogonal projector onto that space. For $\lambda,\mu\in\Sigma$,
>
> $$
> \mathbf E_\lambda^{\mathsf T}=\mathbf E_\lambda,\qquad
> \mathbf E_\lambda\mathbf E_\mu=\delta_{\lambda\mu}\mathbf E_\lambda,\qquad
> \sum_{\lambda\in\Sigma}\mathbf E_\lambda=\mathbf J
> $$
>
> Here $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$, and $\operatorname{tr}\mathbf E_\lambda=\operatorname{rank}\mathbf E_\lambda=m_\lambda$.

> [!note]- Proof
> **Proof.** Another orthonormal basis has the form $\mathbf U_\lambda\mathbf O$, where $\mathbf O\mathbf O^{\mathsf T}=I$. Hence $(\mathbf U_\lambda\mathbf O)(\mathbf U_\lambda\mathbf O)^{\mathsf T}=\mathbf E_\lambda$. The product identities follow from $\mathbf U_\lambda^{\mathsf T}\mathbf U_\lambda=I$ and orthogonality of distinct eigenspaces. Their direct sum is $H$, so the projectors sum to $\mathbf J$. $\square$

For $\mathbf z\in H$, put $\mathbf z_\lambda=\mathbf E_\lambda\mathbf z$. Then

$$
\mathbf z=\sum_\lambda\mathbf z_\lambda,\qquad
\mathbf L\mathbf z=\sum_\lambda\lambda\mathbf z_\lambda,\qquad
\mathbf{Gr}\mathbf z=\sum_\lambda\lambda^{-1}\mathbf z_\lambda
$$

Thus eigenvalues together with projectors recover both matrices:

$$
\boxed{
\mathbf L=\sum_\lambda\lambda\mathbf E_\lambda,\qquad
\mathbf{Gr}=\sum_\lambda\lambda^{-1}\mathbf E_\lambda
}
$$

In particular, for $C_4$,

$$
\mathbf E_2=\frac12
\begin{pmatrix}1&0&-1&0\\0&1&0&-1\\-1&0&1&0\\0&-1&0&1\end{pmatrix},\qquad
\mathbf E_4=\frac14
\begin{pmatrix}1&-1&1&-1\\-1&1&-1&1\\1&-1&1&-1\\-1&1&-1&1\end{pmatrix}
$$

They give $\mathbf L=2\mathbf E_2+4\mathbf E_4$ and

$$
\mathbf{Gr}=\frac12\mathbf E_2+\frac14\mathbf E_4
=\frac1{16}
\begin{pmatrix}5&-1&-3&-1\\-1&5&-1&-3\\-3&-1&5&-1\\-1&-3&-1&5\end{pmatrix}
$$

The zero mode is preserved by both matrices; it does not become an infinite eigenvalue.

## Projectors as polynomials in the Laplacian

Projectors can be obtained from the operator itself without choosing individual eigenvectors. Put $\Sigma_0=\{0\}\cup\Sigma$; each distinct eigenvalue occurs once in this set, regardless of multiplicity.

> [!info] Projectors as polynomials in the Laplacian
> **Proposition.** For $\lambda\in\Sigma_0$,
>
> $$
> \boxed{
> \mathbf E_\lambda=
> \prod_{\substack{\mu\in\Sigma_0\\\mu\ne\lambda}}
> \frac{\mathbf L-\mu I}{\lambda-\mu}
> }
> $$
>
> Here $\mathbf E_0=\mathbf1\mathbf1^{\mathsf T}/n$, the product is a matrix product, and $I$ acts on all of $\mathbb R^n$.

> [!note]- Proof
> **Proof.** The interpolation polynomial on the right equals $1$ at $\lambda$ and $0$ at every other element of $\Sigma_0$. On each eigenspace it therefore acts as the corresponding projector. The spectral theorem decomposes the whole space into these eigenspaces. $\square$

On $H$, only positive eigenvalues are needed if $\mathbf L$ is replaced by $\mathbf L|_H$ and $I$ by $I_H$. Applying this shortened formula to all of $\mathbb R^n$ may give the wrong action on the constant mode.

For $C_4$, the full formulas simplify to

$$
\mathbf E_2=\frac{\mathbf L(4I-\mathbf L)}4,\qquad
\mathbf E_4=\frac{\mathbf L(\mathbf L-2I)}8
$$

Here $\mathbf L^2$ is operator composition, not the second grade of the exterior exponential. More generally, for a polynomial $r$, we have $r(\mathbf L)=\sum_{\lambda\in\Sigma_0}r(\lambda)\mathbf E_\lambda$. This connects spectral decomposition to polynomial transformations of the Laplacian. The interpolation formula alone does not recover projectors from a list of numbers: it requires the matrix $\mathbf L$ itself.

## Forms of eigenspaces

Let $u_{\lambda,1},\ldots,u_{\lambda,m_\lambda}\in W$ correspond to the chosen orthonormal columns of $\mathbf U_\lambda$. Define the grade-one form

$$
S_\lambda=\sum_{a=1}^{m_\lambda}[u_{\lambda,a}]^2
$$

Under the auxiliary identification $[v,w]\mapsto(z\mapsto v\langle w,z\rangle_0)$, the form $S_\lambda$ corresponds to $\mathbf E_\lambda$. Basis independence of the projector also implies basis independence of $S_\lambda$. Hence

$$
L=\sum_\lambda\lambda S_\lambda,\qquad
\mathrm{Gr}=\sum_\lambda\lambda^{-1}S_\lambda
$$

**Distinguishing the operations.** The identity $\mathbf E_\lambda^2=\mathbf E_\lambda$ does not imply $S_\lambda^2=S_\lambda$. In polyform algebra, $S_\lambda^2$ has grade $2$. It vanishes if $m_\lambda=1$ and is nonzero if $m_\lambda\ge2$. Likewise, $\mathbf E_\lambda\mathbf E_\mu=0$ for $\lambda\ne\mu$ does not imply that the exterior product $S_\lambda S_\mu$ vanishes.

It is convenient to normalize the exterior powers of an eigenspace form:

$$
S_{\lambda,k}=\frac{S_\lambda^k}{k!},\qquad
S_{\lambda,0}=e,\qquad 0\le k\le m_\lambda
$$

Diagonal factorization gives

$$
S_{\lambda,k}=
\sum_{1\le a_1<\cdots<a_k\le m_\lambda}
[u_{\lambda,a_1}\cdots u_{\lambda,a_k}]^2
$$

Thus $S_{\lambda,k}$ is basis-independent and vanishes for $k>m_\lambda$. The auxiliary metric identification on the exterior power sends it to the orthogonal projector $\Lambda^k\mathbf E_\lambda$ onto $\Lambda^kH_\lambda$. Its rank is $\binom{m_\lambda}{k}$.

The spaces $H_\lambda$ are also orthogonal in the resistance metric, because on each one this metric differs from the coordinate metric by the constant factor $\lambda^{-1}$. However, identifying a **form** with an operator depends on the metric: under resistance contraction, $S_\lambda$ corresponds to $\lambda^{-1}\mathbf E_\lambda$, not $\mathbf E_\lambda$.

## Symmetric polynomials with multiplicities

Let $M(t)=\exp(tL)=\sum_{g=0}^d t^gM_g$. Grouping eigendirections by distinct eigenvalues gives

$$
\boxed{
M(t)=\prod_{\lambda\in\Sigma}
\left(\sum_{k=0}^{m_\lambda}t^k\lambda^k S_{\lambda,k}\right)
}
$$

This is the same factorization by eigendirections, but within each eigenspace the factors have been combined into invariant grade polyforms.

For an integer tuple $\mathbf k=(k_\lambda)_{\lambda\in\Sigma}$ with $0\le k_\lambda\le m_\lambda$, write

$$
|\mathbf k|=\sum_\lambda k_\lambda,\qquad
\lambda^{\mathbf k}=\prod_\lambda\lambda^{k_\lambda},\qquad
S_{\mathbf k}=\prod_\lambda S_{\lambda,k_\lambda}
$$

Then

$$
\boxed{M_g=\sum_{|\mathbf k|=g}\lambda^{\mathbf k}S_{\mathbf k}}
$$

> [!note]- Proof
> **Proof.** In the product of exponentials $\exp(t\lambda S_\lambda)$, choose grade $k_\lambda$ from each factor. Its contribution is $t^{k_\lambda}\lambda^{k_\lambda}S_{\lambda,k_\lambda}$. Collecting the coefficient of $t^g$ gives the stated sum. $\square$

The form $S_{\mathbf k}$ describes choosing $k_\lambda$ directions from each eigenspace. Its exterior basis arguments belong to mutually orthogonal subspaces of $\Lambda^gH$ for different tuples $\mathbf k$ of the same grade. Under the auxiliary identification, $S_{\mathbf k}$ is the projector onto the corresponding subspace, of dimension $\prod_\lambda\binom{m_\lambda}{k_\lambda}$.

The operator $\Lambda^g(\mathbf L|_H)$ acts there with multiplier $\lambda^{\mathbf k}$. Different tuples $\mathbf k$ may give the same eigenvalue product; their projectors then sum to a single spectral projector of the operator on the exterior power.

Let $\operatorname{ev}_0([X,Y])=\langle X,Y\rangle_0$ be linear coordinate evaluation, extended to exterior objects by Gram determinants. Orthonormality gives

$$
\operatorname{ev}_0(S_{\mathbf k})=
\prod_\lambda\binom{m_\lambda}{k_\lambda}
$$

The numerical rooted coefficients are therefore

$$
p_g=\operatorname{ev}_0(M_g)
=\sum_{|\mathbf k|=g}
\prod_\lambda\binom{m_\lambda}{k_\lambda}\lambda^{k_\lambda}
$$

and

$$
P_G(t)=\det(I+t\mathbf L)
=\prod_{\lambda\in\Sigma}(1+t\lambda)^{m_\lambda}
$$

The grades remain elementary symmetric polynomials in the weighted eigendirection forms. After grouping repeated modes they are expressed through $S_{\lambda,k}$. Binomial factors appear when these forms are evaluated numerically; they must not be inserted again into the coefficients of $S_{\mathbf k}$.

These are rooted coefficients $p_g$, not ordinary forest coefficients $f_g$. Their distinction and determinant interpretation are discussed in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]. Resistance evaluation also differs from coordinate evaluation: it multiplies the evaluation of each $S_{\mathbf k}$ by $\lambda^{-\mathbf k}$.

## Duality and complementation within each eigenspace

Let $u^{\lambda,a}\in W^*$ be the algebraically dual basis to all $u_{\lambda,a}$. Define

$$
S_\lambda^\vee=\sum_{a=1}^{m_\lambda}[u^{\lambda,a}]^2,\qquad
S_{\lambda,k}^\vee=\frac{(S_\lambda^\vee)^k}{k!},\qquad
S_{\mathbf k}^\vee=\prod_\lambda S_{\lambda,k_\lambda}^\vee
$$

The centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$, where $h=n^{-1}\sum_i a_i$, sends $u^{\lambda,a}$ to $u_{\lambda,a}$ and $S_\lambda^\vee$ to $S_\lambda$. Here $a_i^\vee$ is the coordinate functional restricted to $W$. This identification uses coordinate orthonormality; it is not the resistance Riesz identification.

The dual representation of the Greenian and its exponential are

$$
Q_1=\sum_\lambda\lambda^{-1}S_\lambda^\vee,\qquad
D(t)=\exp(tQ_1)=\sum_{g=0}^d t^gQ_g,\qquad
\mathcal C(D(t))=\exp(t\mathrm{Gr})
$$

Here $t$ marks the grade of the original dual pair at $t=1$; under conductance rescaling, $M(s)$ and $D(s^{-1})$ are mutually dual, according to the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter convention]].

Put $\mathbf m=(m_\lambda)_{\lambda\in\Sigma}$ and $\Delta=\prod_\lambda\lambda^{m_\lambda}$. Then

$$
\boxed{
Q_g=\sum_{|\mathbf k|=g}\lambda^{-\mathbf k}S_{\mathbf k}^\vee
=\frac1\Delta\sum_{|\mathbf k|=g}\lambda^{\mathbf m-\mathbf k}S_{\mathbf k}^\vee
}
$$

Thus the direct term $\lambda^{\mathbf m-\mathbf k}S_{\mathbf m-\mathbf k}$ of grade $d-g$ corresponds to a dual term of grade $g$. In each eigenspace the number of chosen directions is replaced by its complement:

$$
k_\lambda\longleftrightarrow m_\lambda-k_\lambda
$$

After passing to the dual space, the coefficient is divided by $\Delta$. Binomial factors agree with this transition because $\binom{m_\lambda}{k_\lambda}=\binom{m_\lambda}{m_\lambda-k_\lambda}$.

To connect this with exterior contraction, let $\Omega$ be the product of all eigenvectors in a fixed order. Then $M_d=\Delta[\Omega]^2$ and

$$
[\Omega]^2/S_{\mathbf k}^\vee=S_{\mathbf m-\mathbf k}
$$

Each contraction term leaves the complementary set in every eigenspace; the two orientation signs in the form cancel. Substitution into the expansion of $Q_g$ gives $M_d/Q_g=M_{d-g}$. The reverse identity $Q_d/M_g=Q_{d-g}$ follows in the same way. This is the mutual duality of [[en/Greenian and polyform duality/Laplacian and Greenian - Mutual Duality of Exponentials|Laplacian and Greenian - Mutual Duality of Exponentials]], expressed without choosing individual modes inside repeated eigenspaces.

Exterior contraction $/$ differs from ordinary form multiplication. After transfer to $W$, $\exp L\,\exp(\mathrm{Gr})=\exp(L+\mathrm{Gr})$; the multiplicative inverse of $\exp L$ is $\exp(-L)$.

## All grades of the cycle C4

For the vectors chosen above, put $A=[u]^2$, $B=[v]^2$, and $C=[w]^2$. Then

$$
S_2=A+B,\qquad S_{2,2}=\frac{S_2^2}{2}=AB,\qquad S_4=C
$$

The indices $2$ and $4$ in $S_\lambda$ denote eigenvalues, whereas the second index in $S_{\lambda,k}$ denotes the grade. In particular, $S_2$ has grade $1$ and $S_{2,2}$ has grade $2$.

A basis rotation changes $A$ and $B$ but preserves $A+B$ and $AB$. The factorization becomes

$$
M(t)=(e+2tS_2+4t^2S_{2,2})(e+4tS_4)
$$

Write the dual forms as $A^\vee=[u^\vee]^2$, $B^\vee=[v^\vee]^2$, and $C^\vee=[w^\vee]^2$, where $u^\vee,v^\vee,w^\vee$ is the basis of $W^*$ dual to $u,v,w$. All grades are

| $g$ | $M_g$ | $Q_g$ |
|---:|---|---|
| $0$ | $e$ | $e$ |
| $1$ | $2(A+B)+4C$ | $\frac12(A^\vee+B^\vee)+\frac14C^\vee$ |
| $2$ | $4AB+8(A+B)C$ | $\frac14A^\vee B^\vee+\frac18(A^\vee+B^\vee)C^\vee$ |
| $3$ | $16ABC$ | $\frac1{16}A^\vee B^\vee C^\vee$ |

![[Grades and Complementary Directions of C4.svg]]

*Figure 2. The six possible direction-count tuples $(k_2,k_4)$: choose $0$, $1$, or $2$ directions from $H_2$ and $0$ or $1$ from $H_4$. The cells show contributions to the direct and dual exponentials. Complementation sends $(k_2,k_4)$ to $(2-k_2,1-k_4)$, grade $g$ to $3-g$, and divides the direct coefficient by $\Delta=16$. The forms $S_{2,1}$ and $S_{2,1}^\vee$ already contain two terms each.*

For example, the term $8(A+B)C$ in direct grade two corresponds to $(A^\vee+B^\vee)/2$ in dual grade one. The term $4AB$ corresponds to $C^\vee/4$. Individual directions are complemented within $H_2$, but their sum expresses the transition independently of the chosen basis.

The numerical polynomials account for $\operatorname{ev}_0(A+B)=2$:

$$
\begin{aligned}
\det(I+t\mathbf L)&=(1+2t)^2(1+4t)
=1+8t+20t^2+16t^3\\
\det(I+t\mathbf{Gr})&=(1+t/2)^2(1+t/4)
=1+\frac54t+\frac12t^2+\frac1{16}t^3
\end{aligned}
$$

The coefficients of the second polynomial are obtained by reversing those of the first and dividing by $16$. For the fixed spanning-tree form $T_4=[(a_1a_2a_3a_4)]^2$, the normalizations are

$$
\Delta=16=4\tau(C_4),\qquad \tau(C_4)=4,\qquad
T_4=4ABC,\qquad M_3=4T_4,\qquad
N_3=\frac{T_4}{64}
$$

Here $N=\mathcal C(D)=\exp(\mathrm{Gr})$. The factor $1/16$ in the diagonal top grade and $1/64$ multiplying $T_4$ agree with the general normalization $N_d=T_n/(n^2\tau(G))$.

## Resistance geometry by eigenspaces

For $\mathbf z\in H$, the decomposition $\mathbf z=\sum_\lambda\mathbf z_\lambda$ gives two metric evaluations:

$$
P_M([z]^2)=\sum_\lambda\lambda^{-1}\|\mathbf z_\lambda\|_0^2,\qquad
P_N([z]^2)=\sum_\lambda\lambda\|\mathbf z_\lambda\|_0^2
$$

Here $\|\mathbf z_\lambda\|_0^2=\mathbf z_\lambda^{\mathsf T}\mathbf z_\lambda$, $M=\exp L$, and $N=\exp(\mathrm{Gr})$. These sums express the resistance and energy quadratic norms through the same orthogonal projections; their relation to normalized potentials is developed in [[en/Greenian and polyform duality/The Greenian Metric and Potentials|The Greenian Metric and Potentials]].

Let $\mathbf e_i$ be the standard coordinate column, and let $\mathbf b_{ij}=\mathbf e_j-\mathbf e_i$ correspond to $a_{ij}=a_j-a_i$. Symmetry and idempotence of the projectors imply

$$
\boxed{
R_{ij}=\sum_{\lambda\in\Sigma}
\frac{\|\mathbf E_\lambda\mathbf b_{ij}\|_0^2}{\lambda}
}
$$

Indeed, $R_{ij}=\mathbf b_{ij}^{\mathsf T}\mathbf{Gr}\mathbf b_{ij}$, and $\mathbf b_{ij}^{\mathsf T}\mathbf E_\lambda\mathbf b_{ij}=\|\mathbf E_\lambda\mathbf b_{ij}\|_0^2$. Each contribution is nonnegative and depends on the positions of the vertices relative to the eigenspace.

For $C_4$,

| Vertex pair | Contribution of $H_2$ | Contribution of $H_4$ | Effective resistance |
|---|---:|---:|---:|
| Adjacent, for example $1,2$ | $1/2$ | $1/4$ | $3/4$ |
| Opposite, for example $1,3$ | $1$ | $0$ | $1$ |

![[Spectral Contributions to Resistances in C4.svg]]

*Figure 3. Left: resistances of an adjacent and an opposite pair decomposed by eigenspaces. Right: the contribution of $H_2$ to $R_{12}$ decomposed into individual modes in two bases: $1/4+1/4$ and $0+1/2$. The total eigenspace contribution is preserved although its distribution among modes changes. Colors on the left denote eigenspaces; on the right they denote the two modes of the selected basis.*

In the original basis, both modes $\mathbf u,\mathbf v$ contribute $1/4$ to $R_{12}$. In the rotated basis, the components of $\widetilde{\mathbf u}$ at vertices $1$ and $2$ coincide, so its contribution vanishes; the entire $H_2$ contribution, $1/2$, comes from $\widetilde{\mathbf v}$. The contribution of $H_4$ remains $1/4$.

For the sum over all pairs, only the projector ranks are needed:

$$
\operatorname{Kf}(G)=n\operatorname{tr}\mathbf{Gr}
=n\sum_{\lambda\in\Sigma}\frac{m_\lambda}{\lambda}
$$

For $C_4$, $\operatorname{Kf}=4(2/2+1/4)=5$, agreeing with $4\cdot(3/4)+2\cdot1$. The total index is determined by the spectrum with multiplicities; resistances of specified pairs require projectors in vertex coordinates.

## Cospectral graphs with different forest polynomials

Consider two connected weighted graphs on vertices $1,2,3,4$. Graph $G_1$ contains all six edges: edge $12$ has conductance $3$ and the others have conductance $1$. Graph $G_2$ contains only the four edges between the parts $\{1,2\}$ and $\{3,4\}$, each of conductance $2$. The different edge counts already prove that the graphs are nonisomorphic.

Put $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/4$ and

$$
\mathbf z_1=\frac1{\sqrt2}(1,-1,0,0)^{\mathsf T},\qquad
\mathbf z_2=\frac12(1,1,-1,-1)^{\mathsf T}
$$

Direct construction from the edges gives

$$
\mathbf L_{G_1}=
\begin{pmatrix}
5&-3&-1&-1\\-3&5&-1&-1\\-1&-1&3&-1\\-1&-1&-1&3
\end{pmatrix}
=4\mathbf J+4\mathbf z_1\mathbf z_1^{\mathsf T}
$$

$$
\mathbf L_{G_2}=
\begin{pmatrix}
4&0&-2&-2\\0&4&-2&-2\\-2&-2&4&0\\-2&-2&0&4
\end{pmatrix}
=4\mathbf J+4\mathbf z_2\mathbf z_2^{\mathsf T}
$$

Both vectors are centered and have unit coordinate norm. Therefore, for $r=1,2$,

$$
\mathbf E_8^{(r)}=\mathbf z_r\mathbf z_r^{\mathsf T},\qquad
\mathbf E_4^{(r)}=\mathbf J-\mathbf E_8^{(r)},\qquad
\mathbf{Gr}_{G_r}=\frac14\mathbf E_4^{(r)}+\frac18\mathbf E_8^{(r)}
$$

The projector ranks are $1$ and $2$. Both graphs consequently have spectrum $0,4,4,8$, but their projectors for eigenvalue $8$ differ.

![[Cospectral Graphs and Eigendirections.svg]]

*Figure 4. A cospectral pair and normalized modes for eigenvalue $8$. Edge labels are conductances; vertex labels give mode components. Blue means positive, orange negative, and grey zero. Edge crossings do not introduce vertices. The same spectrum does not specify the position of an eigendirection in vertex coordinates.*

In this example there is even a **common eigenbasis**: $\mathbf z_1$, $\mathbf z_2$, and $\mathbf v=(0,0,1,-1)^{\mathsf T}/\sqrt2$ are mutually orthogonal. In this order their eigenvalues are $(8,4,4)$ for $G_1$ and $(4,8,4)$ for $G_2$. For the corresponding affine vectors put $A=[z_1]^2$, $B=[z_2]^2$, and $C=[v]^2$. Then

$$
M_{G_1}(t)=(e+8tA)(e+4tB)(e+4tC),\qquad
M_{G_2}(t)=(e+4tA)(e+8tB)(e+4tC)
$$

Their first and second grades differ; both top grades equal $128ABC=32T_4$. Scalar evaluation forgets which number belongs to which form and gives the same polynomial:

$$
P_{G_1}(t)=P_{G_2}(t)=(1+4t)^2(1+8t)
=1+16t+80t^2+128t^3
$$

Hence $\chi_{G_1}(\xi)=\chi_{G_2}(\xi)=\xi(\xi-4)^2(\xi-8)$, $\tau=128/4=32$, and $\operatorname{Kf}=4(1/4+1/4+1/8)=5/2$. The top grade of the transferred dual exponential is $T_4/512$ for both graphs.

Their ordinary forest polynomials nevertheless differ:

$$
F_{G_1}(t)=1+8t+25t^2+32t^3,\qquad
F_{G_2}(t)=1+8t+24t^2+32t^3
$$

Indeed, the conductances sum to $8$ in each graph. Any pair of distinct edges forms a forest, so

$$
f_2=\frac12\left(\left(\sum_e c_e\right)^2-\sum_e c_e^2\right),\qquad
f_2(G_1)=\frac{64-14}{2}=25,\qquad
f_2(G_2)=\frac{64-16}{2}=24
$$

Thus even all rooted coefficients together do not determine the ordinary forest coefficients. Formal factorization parameters of $F_G$ cannot be treated as Laplacian eigenvalues.

Individual effective resistances also differ. For the coordinate difference $\mathbf b_{ij}=\mathbf e_j-\mathbf e_i$, where $\mathbf e_i$ is the standard coordinate column,

$$
R_{ij}(G_r)=\frac{\|\mathbf E_4^{(r)}\mathbf b_{ij}\|_0^2}{4}
+\frac{\|\mathbf E_8^{(r)}\mathbf b_{ij}\|_0^2}{8}
$$

In $G_1$, the difference $\mathbf b_{12}$ lies entirely in the direction $\mathbf z_1$, so $R_{12}=2/8=1/4$. In $G_2$, it is orthogonal to $\mathbf z_2$ and belongs to the eigenspace for $4$, so $R_{12}=2/4=1/2$.

![[The Same Spectrum and Different Resistances.svg]]

*Figure 5. Contributions of the eigenspaces for $4$ and $8$ to two pairwise effective resistances. For pair $12$, the eigenspace containing the entire vertex difference changes; for pair $13$, both contributions are nonzero. The values of $R_{13}$ are $7/16$ and $3/8$. The total Kirchhoff index remains $5/2$.*

The spectrum retains eigenvalues and multiplicities; the full diagonal representation also retains their association with eigenspaces. The example concerns weighted graphs and does not rely on the existence of cospectral unweighted graphs.

## Which data have been recovered

The numbers $\lambda$ and projectors $\mathbf E_\lambda$ in fixed vertex coordinates determine $\mathbf L$, $\mathbf{Gr}$, the forms $L$, $\mathrm{Gr}$, and their exterior exponentials. In the undirected graph model, pair conductances are $c_{ij}=-L_{ij}$ for $i\ne j$. For parallel edges, the total conductances are recovered, not their division into individual conductors.

Recovering every grade here relies on the exponential law $M_g=L^g/g!$. For an arbitrary polyform, its first grade does not determine the others, and the eigenspaces of its first grade need not diagonalize the higher components.

Dimensions $m_\lambda$ alone do not locate the eigenspaces in vertex space. Replacing projectors by their ranks preserves scalar spectral coefficients but loses data needed to recover individual edges and resistances. Under relabeling of vertices, all projectors, like the Laplacian, are conjugated by the same permutation matrix.

The properties of orthogonal projectors and positivity of $\lambda$ alone do not ensure graph realizability: the off-diagonal signs of the reconstructed Laplacian must be checked. These constraints are studied in [[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]].

Projectors and their polynomial formulas also exist for a disconnected symmetric Laplacian, but its zero eigenspace is then multidimensional. The positive projectors sum to the projector onto the image of $\mathbf L$, not all of $H$. The duality formulas in this note with $\Delta=n\tau>0$ do not apply to that case. Nonsymmetric balanced-graph Laplacians require separate treatment.

## Status and sources

Spectral projectors, interpolation representations of functions of a symmetric operator, and exterior powers are classical constructions. The text proves basis independence of projectors, their polynomial expressions, grouping of grades by eigenspaces, and the rule for complementary direction counts. Their expression through forms and normalized potentials agrees with the PMG foundations.

The $C_4$ example was checked exactly in rational arithmetic: projectors were compared in two bases and through polynomials in the edge-built Laplacian; every grade was compared with an independent edge expansion; the Green matrix was computed by inversion on the centered space. Exterior contraction, the centered transfer, forest coefficients, and effective resistances were checked. The figures use these computed data.

- [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]] - eigendirection factorization, elementary symmetric polynomials, and graph normalizations.
- [[en/Foundations/Core specification|Core specification]] and [[en/Foundations/PMG terminology|PMG terminology]] - forms, metrics, and current notation.
- [[en/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian|The Exterior Exponential and Representations of the Greenian]] - the general exponential law of grades and dual contraction.
- [[en/Greenian and polyform duality/The Greenian Metric and Potentials|The Greenian Metric and Potentials]] and [[en/Polynomial toponomes/Coefficients and Kirchhoff Indices|Coefficients and Kirchhoff Indices]] - the two metric evaluations and total resistance characteristics.
- [Jonathan Kelner. Lecture 2, MIT 18.409, notes by Mergen Nachin](https://ocw.mit.edu/courses/18-409-topics-in-theoretical-computer-science-an-algorithmists-toolkit-fall-2009/7c5d4c779c64e9ed3a5783a80b7eb0a5_MIT18_409F09_scribe2.pdf) - Laplacian spectral theory and graph eigenmodes.
- [A. Belkhirat, M. L. Labbi. Interactions between the composition and exterior products of double forms and applications](https://arxiv.org/html/1402.4072v1#S5), § 5, Proposition 5.1 - the exterior exponential of a double form and the induced operator on the exterior algebra; §§ 2–3 distinguish exterior and composition products.
- [Exact checks and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral) - computations for $C_4$ and the cospectral weighted pair. For the pair, independent checks cover edge and modal expansions of every grade, projectors, Green matrices, enumeration of ordinary and rooted forests, effective resistances, and dual contractions under conductance rescaling.

In [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]], this construction is applied to entire graph families: explicit modes combine into projectors, recover polyforms, and give separate resistance contributions. Polynomial transformations of these operators are developed in [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]].

Navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
