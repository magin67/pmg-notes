---
title: "Eigenmodes of Paths and Cycles"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: eigenmodes-of-paths-and-cycles
order: 3
description: "Explicit eigenvalues, real eigenvectors, and projectors of paths and cycles. Diagonal polyforms, dual grades, forest coefficients, and modal contributions to resistances."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Собственные моды путей и циклов|Русский]]

A path has two endpoints, whereas a cycle requires mode values to agree after a complete circuit. This difference determines the Laplacian eigendirections. A path gives a cosine basis shifted by half a step; a cycle gives periodic sine and cosine pairs. These directions recover not only the Laplacian and Green matrices, but also every grade of their exterior exponentials.

[[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]] develops factorization by eigendirections. [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]] shows how to group repeated modes into eigenspace forms. Here we apply both expressions to entire graph families, derive eigenbases, and follow their resistance interpretation. The main examples are $P_6$, $C_6$, and $C_5$.

## Graphs, coordinates, and metrics

Every edge has unit conductance. The path $P_n$, $n\ge2$, has vertices $1,\ldots,n$ and edges between consecutive labels. The cycle $C_n$, $n\ge3$, also contains the edge joining $n$ and $1$. We use the ordinary Laplacian $\mathbf L$, whose diagonal entries are vertex degrees and whose edge entries are $-1$.

Eigenvectors are normalized using the coordinate inner product

$$
\langle\mathbf z,\mathbf y\rangle_0=\mathbf z^{\mathsf T}\mathbf y,\qquad
H=\mathbf1^\perp,\qquad d=n-1
$$

A column $\mathbf z\in H$ corresponds to $z=\sum_r z_r a_r\in W$. The PMG resistance inner product is determined by $\mathbf{Gr}=\mathbf L^+$:

$$
z\cdot y=\mathbf z^{\mathsf T}\mathbf{Gr}\mathbf y
$$

Both matrices vanish on the constant mode $\mathbf1/\sqrt n$ and are mutual inverses on $H$. Auxiliary coordinate normalization and the resistance metric serve different purposes; their definitions are fixed in [[en/Foundations/Core specification|Core specification]].

## Why a path gives a cosine basis

For a numerical column $\mathbf f=(f_1,\ldots,f_n)^{\mathsf T}$, the interior Laplacian rows are

$$
(\mathbf L\mathbf f)_r=2f_r-f_{r-1}-f_{r+1},\qquad 2\le r\le n-1
$$

At the endpoints the expressions are $f_1-f_2$ and $f_n-f_{n-1}$. For the derivation, introduce auxiliary values $f_0=f_1$ and $f_{n+1}=f_n$. The same difference formula then holds in every row. These values extend the mode; they do not add graph vertices.

Substitute $f_r=\cos(\theta(r-1/2))$. A trigonometric identity gives

$$
2f_r-f_{r-1}-f_{r+1}=(2-2\cos\theta)f_r
$$

The left condition $f_0=f_1$ holds automatically. The right condition follows from

$$
f_{n+1}-f_n=-2\sin(n\theta)\sin(\theta/2)
$$

This selects the angles $\theta_k=\pi k/n$.

> [!info] Why a path gives a cosine basis
> **Theorem (path modes).** An orthonormal eigenbasis of the Laplacian of $P_n$ is given by
>
> $$
> u_0(r)=\frac1{\sqrt n},\qquad
> u_k(r)=\sqrt{\frac2n}\cos\left(\frac{\pi k}{n}\left(r-\frac12\right)\right),
> \quad 1\le k\le n-1
> $$
>
> The eigenvalues are
>
> $$
> \boxed{\lambda_k=2-2\cos\frac{\pi k}{n},\qquad 0\le k\le n-1}
> $$
>
> They are all distinct; $\lambda_0=0$ and $\lambda_k>0$ for $k>0$. Write $\mathbf u_k$ for the column with components $u_k(r)$.

> [!note]- Proof
> **Proof.** Substitution and the endpoint conditions already give the eigenvalue equation. Orthogonality and normalization follow from the sum formula
>
> $$
> \sum_{r=1}^n\cos\left(\left(r-\frac12\right)\theta\right)
> =\frac{\sin(n\theta)}{2\sin(\theta/2)}
> $$
>
> for $\sin(\theta/2)\ne0$ and the product identity for two cosines. For $k>0$, the components sum to zero, their unnormalized squares sum to $n/2$, and pairwise inner products vanish. For $k=0$ this gives the constant column normalized by $1/\sqrt n$. Cosine is strictly decreasing on the angles $0\le\pi k/n<\pi$, so the values $\lambda_k$ are distinct. The resulting $n$ orthonormal vectors form a complete basis. $\square$

This cosine basis corresponds to the type-II discrete cosine transform, DCT-II. The shift $r-1/2$ is essential for matching the mode to the path endpoints.

For $P_6$, the nonzero eigenvalues are

$$
2-\sqrt3,\quad 1,\quad 2,\quad 3,\quad 2+\sqrt3
$$

![[Eigenmodes of the Path P6.svg]]

*Figure 1. All six coordinate-normalized modes of $P_6$, including the constant mode. Color indicates component sign; numerical labels are rounded to three decimal places. The Laplacian and Greenian eigenvalues are compared on the right. Both matrices vanish on the constant mode, while all other multipliers are reciprocal.*

## Periodic modes of a cycle

For a cycle, the difference formula holds for every $r$ with periodic indices: $f_0=f_n$ and $f_{n+1}=f_1$. Its periodic solutions have angles $\vartheta_k=2\pi k/n$ and eigenvalues

$$
\mu_k=2-2\cos\frac{2\pi k}{n},\qquad 0\le k\le n-1
$$

Since $\mu_k=\mu_{n-k}$, an eigenvalue usually corresponds to two real modes. Put $m=\lfloor(n-1)/2\rfloor$. For $1\le k\le m$, define

$$
v_k^c(r)=\sqrt{\frac2n}\cos\frac{2\pi k(r-1)}n,\qquad
v_k^s(r)=\sqrt{\frac2n}\sin\frac{2\pi k(r-1)}n
$$

> [!info] Periodic modes of a cycle
> **Theorem (cycle modes).** A real orthonormal eigenbasis of $C_n$ consists of the constant mode $1/\sqrt n$, the pairs $\mathbf v_k^c,\mathbf v_k^s$, $1\le k\le m$, and, for even $n$, one additional mode
>
> $$
> w(r)=\frac{(-1)^{r-1}}{\sqrt n},\qquad
> \mathbf L\mathbf w=4\mathbf w
> $$
>
> Each pair has eigenvalue $\mu_k$ of multiplicity $2$. The constant mode has eigenvalue $0$ of multiplicity $1$, and the additional mode of an even cycle has eigenvalue $4$ of multiplicity $1$.

> [!note]- Proof
> **Proof.** Substituting sine and cosine into the difference formula gives the multiplier $2-2\cos\vartheta_k$. Periodicity follows from $n\vartheta_k=2\pi k$. Orthogonality follows from the root-of-unity sum $\sum_{r=0}^{n-1}\exp(2\pi i\ell r/n)=0$ for $\ell\not\equiv0\pmod n$; its real and imaginary parts give the required trigonometric sums. In these pairs, squared sine and cosine values each sum to $n/2$.
>
> For even $n$, the angle $\pi$ gives an alternating cosine whose squares sum to $n$; the sine is identically zero. For odd $n$, the sequence $(-1)^{r-1}$ is incompatible with period $n$, so this mode is absent. The values $\mu_k$ are distinct at the selected angles $0<2\pi k/n<\pi$. The number of basis vectors is $1+2m$ for odd $n$ and $2+2m$ for even $n$, equal to $n$ in both cases. $\square$

Changing the starting vertex rotates the sine-cosine basis within each pair while preserving the eigenspace. In an arbitrary orthonormal basis of that space, individual modes may look different.

For $C_6$, there are two pairs with eigenvalues $1$ and $3$, and a separate alternating mode with eigenvalue $4$:

$$
\operatorname{spec}\mathbf L_{C_6}=(0,1,1,3,3,4)
$$

![[Real Modes of the Cycle C6.svg]]

*Figure 2. A real basis for the cycle $C_6$. The top row shows the one-dimensional constant and alternating modes; the next two rows contain cosine-sine pairs for eigenvalues $1$ and $3$. Components are coordinate-normalized and rounded to three decimal places. Vertex labels agree across all diagrams.*

The odd cycle $C_5$ has only two pairs of nonzero modes:

$$
\mu_1=\frac{5-\sqrt5}{2},\qquad
\mu_2=\frac{5+\sqrt5}{2},\qquad
\operatorname{spec}\mathbf L_{C_5}=(0,\mu_1,\mu_1,\mu_2,\mu_2)
$$

![[Paired Modes of the Odd Cycle C5.svg]]

*Figure 3. The four nonzero modes of $C_5$, grouped into two pairs. Together with the constant mode $1/\sqrt5$, they form a complete basis. There is no separate alternating direction with eigenvalue $4$. Component labels are rounded to three decimal places.*

## Projectors and a common basis for the Laplacian and Greenian

For a path, each nonzero eigenspace is one-dimensional, with projector

$$
\mathbf E_k^P=\mathbf u_k\mathbf u_k^{\mathsf T},\qquad
\mathbf L_{P_n}=\sum_{k=1}^{n-1}\lambda_k\mathbf E_k^P,\qquad
\mathbf{Gr}_{P_n}=\sum_{k=1}^{n-1}\lambda_k^{-1}\mathbf E_k^P
$$

In particular,

$$
\mathrm{Gr}_{rs}^{P_n}=\frac2n\sum_{k=1}^{n-1}
\frac{\cos(\theta_k(r-1/2))\cos(\theta_k(s-1/2))}{\lambda_k}
$$

For a cycle, the projector onto a paired eigenspace is

$$
\mathbf E_k^C=\mathbf v_k^c(\mathbf v_k^c)^{\mathsf T}
+\mathbf v_k^s(\mathbf v_k^s)^{\mathsf T},\qquad
(E_k^C)_{rs}=\frac2n\cos\frac{2\pi k(r-s)}n
$$

The last equality follows from the cosine difference formula. It expresses the projector through the difference of vertex labels and is independent of the phase origin of the sine-cosine pair. Its rank is $2$.

Let $\epsilon_n$ equal $1$ for even $n$ and $0$ for odd $n$. For even $n$, introduce $\mathbf E_\pi=\mathbf w\mathbf w^{\mathsf T}$; for odd $n$, put $\mathbf E_\pi=0$. Then

$$
\mathbf L_{C_n}=\sum_{k=1}^m\mu_k\mathbf E_k^C+4\mathbf E_\pi,\qquad
\mathbf{Gr}_{C_n}=\sum_{k=1}^m\mu_k^{-1}\mathbf E_k^C+\frac14\mathbf E_\pi
$$

and

$$
\mathrm{Gr}_{rs}^{C_n}=\frac2n\sum_{k=1}^m
\frac{\cos(2\pi k(r-s)/n)}{\mu_k}
+\epsilon_n\frac{(-1)^{r-s}}{4n}
$$

Thus the Laplacian and Greenian have the same eigenspaces, with reciprocal eigenvalues on them. The constant-mode projector does not enter the Green matrix formulas. The numbers $\lambda_k^{-1}$ and $\mu_k^{-1}$ are also the quadratic resistance evaluations of the corresponding coordinate-unit modes: $u_k^2=\lambda_k^{-1}$ and $(v_k^c)^2=(v_k^s)^2=\mu_k^{-1}$.

## Diagonal polyforms of a path

Pass from columns to vectors in $W$ and their forms. For a path, put $\ell_k=\lambda_k[u_k]^2$. Then

$$
L_{P_n}=\sum_{k=1}^{n-1}\ell_k,\qquad
\mathrm{Gr}_{P_n}=\sum_{k=1}^{n-1}\lambda_k^{-1}[u_k]^2
$$

Introduce a formal parameter $t$. The exterior exponential and its grades are

$$
\begin{aligned}
M(t)&=\exp(tL_{P_n})=\sum_{g=0}^{d}t^gM_g
=\prod_{k=1}^{n-1}(e+t\ell_k)\\
M_g&=e_g(\ell_1,\ldots,\ell_{n-1})
\end{aligned}
$$

Here $e_g$ is the elementary symmetric polynomial evaluated in the commutative algebra of forms, with $e_0=e$. In particular,

$$
M_2=\sum_{1\le j<k\le n-1}\lambda_j\lambda_k[u_j u_k]^2
$$

For $P_6$, the top grade is

$$
M_5=6[u_1u_2u_3u_4u_5]^2=T_6
$$

The radicals in individual eigenvalues therefore disappear in the product of all nonzero eigenvalues. The top grade contains the volume form of all of $H$ and no longer distinguishes individual orthonormal basis directions. The coordinate evaluation of each basis term $[u_I]^2$ is $1$; its resistance evaluation is the reciprocal product of the corresponding eigenvalues.

## Cycle grades grouped by paired eigenspaces

For a cyclic pair, define

$$
S_k=[v_k^c]^2+[v_k^s]^2,\qquad 1\le k\le m
$$

Here $k$ is the frequency index, not the grade or the eigenvalue itself. For even $n$, put $B=[w]^2$; for odd $n$, put $B=0$. Then

$$
L_{C_n}=\sum_{k=1}^m\mu_k S_k+4B,\qquad
\mathrm{Gr}_{C_n}=\sum_{k=1}^m\mu_k^{-1}S_k+\frac14B
$$

Since the paired eigenspace is two-dimensional, $S_k^3=0$ and $S_k^2/2=[v_k^c v_k^s]^2$. Hence

$$
\boxed{
M(t)=\prod_{k=1}^m
\left(e+t\mu_kS_k+\frac{t^2\mu_k^2}{2}S_k^2\right)(e+4tB)
}
$$

The last factor is $e$ for odd $n$. To obtain grade $g$, choose $a_k\in\{0,1,2\}$ directions from each pair and, when the alternating mode is present, $b\in\{0,1\}$. This gives

$$
M_g=
\sum_{\substack{a_1+\cdots+a_m+b=g\\0\le a_k\le2,\ 0\le b\le\epsilon_n}}
\left(\prod_{k=1}^m\mu_k^{a_k}\frac{S_k^{a_k}}{a_k!}\right)(4B)^b
$$

For $b=0$, the last factor is $e$. This is the grouped elementary symmetric polynomial in the weighted forms of individual modes. Its expression through $S_k$ is independent of rotations within each pair.

For $C_6$, $L=S_1+3S_2+4B$, with the explicit second grade

$$
M_2=\frac12S_1^2+\frac92S_2^2+3S_1S_2+4S_1B+12S_2B
$$

Under coordinate evaluation, $S_1$ and $S_2$ each give $2$, while $S_1^2/2$, $S_2^2/2$, and $B$ each give $1$. Thus the second-grade coefficient is $1+9+12+8+24=54$. No additional binomial factors are attached to the forms: the choice of directions is already accounted for within $S_k^{a_k}/a_k!$.

## Dual grades and scalar polynomials

For duality, use algebraically dual bases in $W^*$. Denote their forms by $[u^k]^2$, $S_k^\vee=[v^{k,c}]^2+[v^{k,s}]^2$, and $B^\vee=[w^\vee]^2$ for even $n$; for odd $n$, put $B^\vee=0$. The centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$, $h=n^{-1}\sum_i a_i$, sends these forms to their direct counterparts. It uses coordinate orthonormality, not resistance pairing.

For a path,

$$
D(t)=\exp(tQ_1)=\sum_{g=0}^{d}t^gQ_g=\prod_{k=1}^{n-1}
\bigl(e+t\lambda_k^{-1}[u^k]^2\bigr)
$$

For a cycle, the same construction gives

$$
D(t)=\prod_{k=1}^m
\left(e+\frac{t}{\mu_k}S_k^\vee+
\frac{t^2}{2\mu_k^2}(S_k^\vee)^2\right)
\left(e+\frac t4B^\vee\right)
$$

After transfer, $\mathcal C(D(t))=\exp(t\mathrm{Gr})$. In the cyclic expression, the complementary direction set is specified by $a_k\mapsto2-a_k$ and $b\mapsto\epsilon_n-b$. For a path, the selected set of one-dimensional modes is complemented. In both cases direct grade $d-g$ corresponds to dual grade $g$, with the diagonal coefficient divided by $\Delta$, the product of the nonzero eigenvalues.

The parameter $t$ marks the grade: the dual pair here is taken at $t=1$. Multiplying conductances by $s>0$ gives the mutually dual pair $M(s)$ and $D(s^{-1})$; see the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter convention]].

A path has one spanning tree; removing any of the $n$ edges of a cycle produces a tree. Kirchhoff's theorem therefore gives

$$
\Delta(P_n)=n,\qquad \Delta(C_n)=n^2
$$

For the common spanning-tree form $T_n=[(a_1\ldots a_n)]^2$ and $N=\exp(\mathrm{Gr})$,

| Graph | $M_d$ | $N_d$ |
|---|---|---|
| $P_n$ | $T_n$ | $T_n/n^2$ |
| $C_n$ | $nT_n$ | $T_n/n^3$ |

This agrees with $T_n=n[\Omega]^2$, where $\Omega=z_1\cdots z_d$ for any coordinate-orthonormal basis $z_1,\ldots,z_d$ of $H$ transferred to $W$. Duality is expressed by exterior contraction $M_d/Q_g=M_{d-g}$, not by ordinary multiplication of exponentials.

Coordinate evaluation of the grades gives the rooted polynomials

$$
P_{P_n}(t)=\prod_{k=1}^{n-1}(1+t\lambda_k),\qquad
P_{C_n}(t)=\prod_{k=1}^m(1+t\mu_k)^2(1+4t)^{\epsilon_n}
$$

For the main examples they are

$$
\begin{aligned}
P_{P_6}(t)&=1+10t+36t^2+56t^3+35t^4+6t^5\\
P_{C_6}(t)&=1+12t+54t^2+112t^3+105t^4+36t^5\\
P_{C_5}(t)&=1+10t+35t^2+50t^3+25t^4
\end{aligned}
$$

The coefficients of $\det(I+t\mathbf{Gr})$ are obtained by reversing these sequences and dividing by $6$, $36$, and $25$, respectively. They are numerical evaluations of dual grades after the transfer $\mathcal C$. Ordinary forest coefficients $f_g$ have a different meaning: for example, the ordinary forest polynomial of $P_6$ is $(1+t)^5$. The determinant interpretation of the rooted polynomial is developed in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

## Which modes contribute to an effective resistance

For the difference $a_{rs}=a_s-a_r$, the quadratic resistance evaluation is $a_{rs}^2=R_{rs}$. The path's spectral formula is

$$
R_{rs}^{P_n}=\frac2n\sum_{k=1}^{n-1}
\frac{\bigl(\cos(\theta_k(r-1/2))-\cos(\theta_k(s-1/2))\bigr)^2}{\lambda_k}
$$

Every term is nonnegative. If a mode has equal components at the two selected vertices, its contribution vanishes. On the other hand, the unit resistances of path edges are connected in series, so

$$
R_{rs}^{P_n}=|r-s|
$$

For a cycle, put $q=|r-s|$, $0\le q\le n-1$. The projector formula gives

$$
R_{rs}^{C_n}=\frac4n\sum_{k=1}^m
\frac{1-\cos(2\pi kq/n)}{\mu_k}
+\epsilon_n\frac{1-(-1)^q}{2n}
$$

For each $k$, the first summand combines the contribution of the entire sine-cosine pair. The last term is the contribution of the alternating mode, which exists only for even $n$.

The two cycle arcs between the selected vertices have resistances $q$ and $n-q$ and are connected in parallel. Hence

$$
R_{rs}^{C_n}=\frac{q(n-q)}n
$$

For $r=s$, both sides vanish. The spectral and electrical formulas were obtained independently; equating them gives the corresponding trigonometric identities.

On $P_6$, only modes $k=1,3,5$ contribute to the endpoint pair $1,6$:

$$
R_{16}^{P_6}=\frac{7+4\sqrt3}{3}+\frac13+\frac{7-4\sqrt3}{3}=5
$$

For the central edge $3,4$, the same three modes contribute equally, each giving $1/3$, and $R_{34}^{P_6}=1$. Thus dominance of a mode depends on the selected vertex pair.

For $C_6$, the spectral contributions are

| Pair | Eigenspace $\mu_1=1$ | Eigenspace $\mu_2=3$ | Mode $4$ | $R_{rs}$ |
|---|---:|---:|---:|---:|
| $1,2$ | $1/3$ | $1/3$ | $1/6$ | $5/6$ |
| $1,3$ | $1$ | $1/3$ | $0$ | $4/3$ |
| $1,4$ | $4/3$ | $0$ | $1/6$ | $3/2$ |

![[Spectral Contributions to Resistances in P6 and C6.svg]]

*Figure 4. Distribution of resistance among path modes and cycle eigenspaces. For the endpoints of $P_6$, the first mode provides the largest share; for the central edge, the three odd modes contribute equally. For $C_6$, the full contributions of paired eigenspaces and the separate mode $4$ are shown. Labels give exact values; segment heights use their numerical values. The vertical scales of the two panels differ.*

For $C_5$, the formula gives $R=4/5$ for neighbors and $R=6/5$ for vertices two edges apart. The absence of an alternating mode agrees with the fact that the full resistance comes from two paired eigenspaces.

Summing over all vertex pairs gives the Kirchhoff indices

$$
\operatorname{Kf}(P_n)=\frac{n^3-n}{6},\qquad
\operatorname{Kf}(C_n)=\frac{n^3-n}{12}
$$

For a path this is the sum $\sum_{q=1}^{n-1}(n-q)q$. For a cycle, sum over ordered pairs and divide by $2$, giving $\frac12\sum_{q=1}^{n-1}q(n-q)$. In particular, the values for $P_6$, $C_6$, and $C_5$ are $35$, $35/2$, and $10$. They agree with $n\operatorname{tr}\mathbf{Gr}$; their connection with polynomial coefficients appears in [[en/Polynomial toponomes/Coefficients and Kirchhoff Indices|Coefficients and Kirchhoff Indices]].

## Preparing the Chebyshev connection

Eigenvalues in both families have the form $2-2\cos\theta$. A path selects angles $\pi k/n$, while a cycle selects $2\pi k/n$. Angle doubling is expressed by the polynomial

$$
\Phi_2(\xi)=\xi(4-\xi),\qquad
\Phi_2(2-2\cos\theta)=2-2\cos(2\theta)
$$

Consequently, for $n\ge3$, the matrix $4\mathbf L_{P_n}-\mathbf L_{P_n}^2$ has the eigenvalues of $C_n$, with multiplicities. It preserves the eigenbasis of the path; when transformed values coincide, the corresponding one-dimensional eigenspaces merge.

This spectral statement alone does not identify the matrix with the cycle Laplacian in the chosen vertex order. A graph interpretation requires examining its off-diagonal entries and vertex order. That step, general angle-multiplication polynomials, and the resulting graphs are developed in [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]]. The classical formula $T_m(\cos\theta)=\cos(m\theta)$ explains the appearance of Chebyshev polynomials.

All polynomial transformations here use matrix composition. Exterior powers of the form $L$ and grades $L^g/g!$ use another operation: they describe selections of eigendirections rather than multiplication of the spectral angle.

## Status and sources

The spectra and eigenbases of paths and cycles are classical results. The text derives them from difference equations and supplies normalization, real projectors, and consistent PMG polyform expressions. Exponential factorization and reversal of complementary grades use results proved in [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]] and [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]].

For $P_6$, $C_6$, and $C_5$, eigenvalues, projectors, Green matrices, polynomial coefficients, and resistance contributions were checked exactly using rational numbers and radicals. Trigonometric components for the figures were computed numerically and compared with exact projectors. Additional numerical basis checks cover a finite set of sizes; they control computations rather than replacing general proofs. Rounding figure labels does not change the exact formulas used in the text.

- [[en/Foundations/Core specification|Core specification]] and [[en/Foundations/PMG terminology|PMG terminology]] - spaces, metrics, and current notation.
- [[en/Greenian and polyform duality/The Greenian Metric and Potentials|The Greenian Metric and Potentials]] - resistance and energy evaluations in polyform language.
- [K. K. K. R. Perera, Y. Mizoguchi. Bipartition of graphs based on the normalized cut and spectral methods](https://arxiv.org/html/1210.7253v2#S4.SS1), § 4.1, Propositions 4.4(2) and 4.8(2) - eigenvalues and eigenvectors of the ordinary cycle and path Laplacians, respectively; formulas for the normalized Laplacian are not used here.
- [Jonathan Kelner. Lecture 2, MIT 18.409, notes by Mergen Nachin](https://ocw.mit.edu/courses/18-409-topics-in-theoretical-computer-science-an-algorithmists-toolkit-fall-2009/7c5d4c779c64e9ed3a5783a80b7eb0a5_MIT18_409F09_scribe2.pdf) - Laplacian spectral theory and modes of standard graphs.
- [NIST Digital Library of Mathematical Functions, §18.5](https://dlmf.nist.gov/18.5) - trigonometric representations of Chebyshev polynomials.
- [Checks and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral) - exact and numerical checks of the formulas in this note.

Navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
