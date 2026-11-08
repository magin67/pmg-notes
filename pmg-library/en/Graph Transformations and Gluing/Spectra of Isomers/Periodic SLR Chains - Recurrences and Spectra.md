---
title: 'Periodic SLR Chains: Recurrences and Spectra'
date: '2026-11-02'
updated: 2026-11-08
revision: 3
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: periodic-slr-chains-recurrences-and-spectra
order: 9
description: 'Exact recurrences for periods LR, SL, and LLS: reciprocal transfer, minimal orders, phase and end effects, and rooted-forest growth.'
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Периодические SLR-цепочки - рекурсии и спектры|Периодические SLR-цепочки: рекурсии и спектры]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

A repeated turn word reduces the spectral calculation for a chain to a power of one matrix. Exact recurrences for characteristic polynomials are derived below for the periods LR, SL, and LLS. Their generic homogeneous order is five; a special value of the spectral parameter may lower it. We also explain why the same transfer over a period need not give identical spectra of finite chains.

> [!note] The result in plain language
> Fix a short pattern of straight continuations and turns, and repeat it. To compute the spectral polynomial of an increasingly long chain, it suffices to retain five preceding polynomials. For the three patterns considered here, this number cannot be reduced if one requires a single homogeneous linear recurrence whose coefficients remain unchanged as the chain grows.
>
> The same period can start at different letters. The transfer matrices over a period are similar and retain their eigenvalues, but the end conditions of the finite chain change. For example, chains repeating LLS and LSL have different spectra for every positive number of repetitions. Nevertheless, their numbers of rooted forests grow at the same rate per core.

This note continues [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]] and [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]]. Closing the chain into a ring is not considered here: it requires different boundary conditions.

## What is repeated

We consider open abstract chains of cycles $C_6$ with unit conductances. Adjacent cores share exactly one edge, counted once. The input and output seams of an intermediate core have no common vertices; nonadjacent cores do not intersect. There are no other identifications. A regular-hexagon layout is not required.

Let $v=\beta_1\cdots\beta_p$ be a nonempty word over S, L, R. The letter S denotes the opposite output seam, and L and R the side outputs under the conventions of [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]. The period $v$ need not be the shortest one.

> [!info] A periodic chain with two end cores
> **Definition.** Let $G_m^{(v)}$ denote the chain with internal word $u=v^m$ and full code $w=Sv^m$, where the first S is the initial marker. Set
>
> $$
> N=pm+2,\qquad n=4pm+10,\qquad m\ge0
> \tag{1}
> $$
>
> Here $N$ is the number of cores, $n$ the number of vertices, and $m$ the number of period repetitions. At $m=0$, two hexagons sharing an edge remain.

There is another convention: repeat the composite runner $v$ directly from the starting edge. Then $N=pm$, and at $m=0$ the graph is a single edge. This is the family in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns#A periodic code and a composite runner|A periodic code and a composite runner]]. The two families share a period matrix but have different initial and terminal conditions.

![Repeating the internal word and repeating the runner from an edge](images/Two%20Period%20Conventions.svg)

In runner language, the main family corresponds to the output sequence $Sv^mS$. The first S creates the first core; the last S selects the boundary after the final attachment. The internal letters $v^m$ specify seam positions. If only $v^m$ is repeated from an edge, then for $pm\ge2$ its internal word is obtained by removing the first and last letters. At $pm=0$, the starting edge remains; at $pm=1$, there is one core with no internal word. This is why the two additional cores in (1) cannot be omitted.

## Five coordinates and the period matrix

Set $\mathbf H_G=\xi\mathbf I_n-\mathbf L_G$. For an ordered active pair $(a,b)$, use the data

$$
\boldsymbol s=(A,B,C,D,E)^{\mathsf T}
$$

Here $A=\det\mathbf H_G$; $B$ and $C$ are principal minors with vertex $a$ and $b$ deleted, respectively; $D=(\operatorname{adj}\mathbf H_G)_{ab}$; and $E$ is the principal minor with the pair deleted. A minor retains the vertex degrees of the original graph. It is not the Laplacian of an induced subgraph.

The matrices $\mathbf U_S,\mathbf U_L,\mathbf U_R$ are defined and derived in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns#Five coordinates and a power of one matrix|Five coordinates and a power of one matrix]]. Unlike the transition with the earlier input orientation, here $\mathbf U_\beta=\mathbf T_{j(\beta)}\mathbf J$: the input $(0,1)$ of the new core is identified with $(b,a)$. The outputs L, S, R are $(2,3)$, $(3,4)$, $(4,5)$.

For a period,

$$
\mathbf V_v=\mathbf U_{\beta_p}\cdots\mathbf U_{\beta_1},\qquad
\mathbf r=\mathbf e_1^{\mathsf T}\mathbf U_S
\tag{2}
$$

The rightmost factor acts first. All three matrices $\mathbf U_\beta$ have the same first row: selecting the next boundary does not change the graph already built.

Let $\boldsymbol s_0$ be the state of the starting edge, and $\boldsymbol s_1$ the state of a single hexagon. Then

$$
\boldsymbol s_0=(\xi(\xi-2),\xi-1,\xi-1,-1,1)^{\mathsf T},
\qquad \boldsymbol s_1=\mathbf U_S\boldsymbol s_0
$$

> [!info] The characteristic polynomial through a period
> **Proposition 1.** For the family (1),
>
> $$
> F_m^{(v)}(\xi):=\chi_{G_m^{(v)}}(\xi)
> =\mathbf r\mathbf V_v^{\,m}\boldsymbol s_1
> \tag{3}
> $$
>
> Repeating the runner directly from an edge instead gives $\widehat F_m^{(v)}=\mathbf e_1^{\mathsf T}\mathbf V_v^{\,m}\boldsymbol s_0$.

> [!note]- Proof of the transfer formula
> **Proof.** The attachment sequence $Sv^mS$ maps $\boldsymbol s_0$ to $\mathbf U_S\mathbf V_v^m\mathbf U_S\boldsymbol s_0$. The first coordinate is the determinant of the whole graph, giving (3). Omitting the two end attachments gives the second formula. Each step adds four new vertices, yielding (1). $\square$

Matrix powers here mean composition of linear transitions. They are not powers of the Laplacian form in polyform algebra.

## Why transfer multipliers come in reciprocal pairs

For an actual boundary state, Jacobi's identity gives $AE-BC+D^2=0$. The transitions preserve the corresponding quadratic form throughout the five-coordinate space, not only on graph states. This is a stronger matrix identity.

> [!info] The general structure of transfer
> **Proposition 2.** For every word $v$, the characteristic polynomial of the period matrix has the form
>
> $$
> \det(q\mathbf I_5-\mathbf V_v)=(q-1)Q_v(q)
> \tag{4}
> $$
>
> $$
> Q_v(q)=q^4-a_vq^3+b_vq^2-a_vq+1
> \tag{5}
> $$
>
> The coefficients belong to $\mathbb Z[\xi]$ and are computed by
>
> $$
> a_v=\operatorname{tr}\mathbf V_v-1,\qquad
> b_v=\frac{a_v^2+1-\operatorname{tr}(\mathbf V_v^2)}{2}
> \tag{6}
> $$

> [!note]- Proof of reciprocity
> **Proof.** For the form $2(AE-BC+D^2)$, take the matrix
>
> $$
> \mathbf M=\begin{pmatrix}
> 0&0&0&0&1\\
> 0&0&-1&0&0\\
> 0&-1&0&0&0\\
> 0&0&0&2&0\\
> 1&0&0&0&0
> \end{pmatrix},\qquad \det\mathbf M=2
> $$
>
> Substitution of the three explicit transition matrices gives the polynomial identities
>
> $$
> \mathbf U_\beta^{\mathsf T}\mathbf M\mathbf U_\beta=\mathbf M,
> \qquad \det\mathbf U_\beta=1
> \tag{7}
> $$
>
> These are checked by ordinary matrix multiplication; reproducible symbolic verification is provided below. The same equalities hold for the product $\mathbf V_v$, so
>
> $$
> \mathbf V_v^{-1}=\mathbf M^{-1}\mathbf V_v^{\mathsf T}\mathbf M
> $$
>
> The spectra of $\mathbf V_v$ and $\mathbf V_v^{-1}$ coincide with multiplicities. Unpaired multipliers can only be $1$ and $-1$. The dimension is five and the determinant is one, so the multiplier $1$ must occur. Removing it leaves the reciprocal quartic (5). The coefficients (6) follow from the first two Newton identities for $\mathbf V_v$. This proof applies at every $\xi$, including values where multipliers coincide. $\square$

The variable $q$ describes transfer multipliers when a whole period is added. It does not denote a Laplacian eigenvalue. The spectrum of the finite graph consists of the roots of $F_m(\xi)$ in the variable $\xi$. These two spectral questions are related by (3) but are distinct.

## A recurrence with a constant right-hand side

Temporarily omit the subscript $v$. By the Cayley–Hamilton theorem, $(\mathbf V-\mathbf I)Q(\mathbf V)=0$. Thus the vector $Q(\mathbf V)\boldsymbol s_1$ is fixed by transfer. Write

$$
\kappa_v=\mathbf rQ_v(\mathbf V_v)\boldsymbol s_1
\tag{8}
$$

> [!info] Two forms of one recurrence
> **Proposition 3.** For every $m\ge0$, the following nonhomogeneous recurrence of order four holds:
>
> $$
> F_{m+4}-aF_{m+3}+bF_{m+2}-aF_{m+1}+F_m=\kappa
> \tag{9}
> $$
>
> Its corresponding homogeneous recurrence of order five is
>
> $$
> \begin{aligned}
> F_{m+5}-(a+1)F_{m+4}+(a+b)F_{m+3}-{}\\
> {}-(a+b)F_{m+2}+(a+1)F_{m+1}-F_m=0
> \end{aligned}
> \tag{10}
> $$

> [!note]- Proof of the recurrences
> **Proof.** The left-hand side of (9) equals $\mathbf r\mathbf V^mQ(\mathbf V)\boldsymbol s_1$. Since the last vector is fixed, this equals (8) for every $m$. Subtracting consecutive instances of (9) gives (10). In particular, the differences $F_{m+1}-F_m$ satisfy the homogeneous recurrence with polynomial $Q$. $\square$

The coefficients $a,b$ are determined by the period. The quantity $\kappa$ and the initial values also depend on the end cores. For the family starting from an edge, replace $\mathbf r,\boldsymbol s_1$ by $\mathbf e_1^{\mathsf T},\boldsymbol s_0$ in (8).

## A worked recurrence for period LR

The rooted polynomial is $P_G(t)=\det(\mathbf I_n+t\mathbf L_G)$. It counts spanning forests with a chosen root in each component, unlike the ordinary forest polynomial. Since $n$ in (1) is even,

$$
c_m^{(v)}:=P_{G_m^{(v)}}(1)=(-1)^nF_m^{(v)}(-1)=F_m^{(v)}(-1)
$$

At $\xi=-1$, recurrence (9) has the following integer coefficients:

| Period $v$ | $a_v(-1)$ | $b_v(-1)$ | $\kappa_v(-1)$ |
|---|---:|---:|---:|
| LR | 7759 | 51561 | 19602 |
| SL | 7809 | 87421 | -1022 |
| LLS | 686236 | 59155926 | -5606172 |

The initial value $c_0=28435$ is common. The other three values needed for the nonhomogeneous recurrence are:

| $m$ | LR | SL | LLS |
|---|---:|---:|---:|
| 1 | 220480560 | 221771751 | 19514594869 |
| 2 | 1709242570740 | 1729329809694 | 13389935419018422 |
| 3 | 13250645128864264 | 13484949197704165 | 9187501318295042810386 |

For LLS, the family starting from an edge has a different right-hand side: $\widehat\kappa_{LLS}(-1)=-901692$. Replacing the initial conditions without changing this quantity would give an incorrect recurrence.

One recurrence step uses four preceding values and the constant right-hand side. Substitution of the LR table gives

$$
\begin{aligned}
c_4^{(LR)}&=7759\,c_3^{(LR)}-51561\,c_2^{(LR)}\\
&\quad+7759\,c_1^{(LR)}-c_0^{(LR)}+19602\\
&=102723627009376555443
\end{aligned}
$$

Here $m=4$ means $N=2m+2=10$ cores. A fifth preceding value is unnecessary while the inhomogeneous form (9) is retained; the homogeneous form (10) uses five. The exact coefficients in $\xi$ underlying the numerical table follow below.

## Exact coefficients for LR, SL, and LLS

The matrices of the three periods are

$$
\mathbf V_{LR}=\mathbf U_R\mathbf U_L,\qquad
\mathbf V_{SL}=\mathbf U_L\mathbf U_S,\qquad
\mathbf V_{LLS}=\mathbf U_S\mathbf U_L^2
$$

To shorten the coefficients, set $x=\xi-2$ below. All formulas in this section refer to the family with two end cores (1).

> [!example]- Expanded coefficients of the three periods
> **Period LR.** Introduce two auxiliary polynomials
>
> $$
> \begin{aligned}
> \alpha&=x^4-2x^3-4x^2+4x+4\\
> \beta&=3x^4-4x^3-8x^2+8x+6
> \end{aligned}
> $$
>
> Then
>
> $$
> a_{LR}=\alpha^2-2\beta,\qquad
> b_{LR}=\beta^2-2\alpha^2+2
> \tag{11}
> $$
>
> $$
> \kappa_{LR}=2(x+2)^2x^4(x^2-x-1)^2
> $$
>
> **Period SL.** The coefficients are
>
> $$
> \begin{aligned}
> a_{SL}={}&x^8-4x^7-4x^6+24x^5+{}\\
> &{}+3x^4-40x^3-3x^2+16x
> \end{aligned}
> \tag{12}
> $$
>
> $$
> \begin{aligned}
> b_{SL}={}&x^{10}-4x^9-2x^8+24x^7-72x^5+{}\\
> &{}+2x^4+96x^3+10x^2-32x-2
> \end{aligned}
> $$
>
> $$
> \kappa_{SL}=2(x+2)^2(x^2-2)(2x^3-3x^2-2x+2)
> $$
>
> **Period LLS.** We obtain
>
> $$
> \begin{aligned}
> a_{LLS}={}&x^{12}-6x^{11}+52x^9-44x^8-164x^7+{}\\
> &{}+155x^6+240x^5-172x^4-162x^3+{}\\
> &{}+48x^2+36x+4
> \end{aligned}
> \tag{13}
> $$
>
> $$
> \begin{aligned}
> b_{LLS}={}&x^{16}-6x^{15}+x^{14}+56x^{13}-64x^{12}-{}\\
> &{}-236x^{11}+358x^{10}+556x^9-891x^8-{}\\
> &{}-818x^7+1107x^6+764x^5-628x^4-{}\\
> &{}-372x^3+132x^2+72x+6
> \end{aligned}
> $$
>
> $$
> \begin{aligned}
> \kappa_{LLS}={}&-2(x+2)^2x^2(x^2-x-1)^2\,\cdot\\
> &\cdot\,(x^3-2x^2-x+3)(2x^3-3x^2-4x+3)
> \end{aligned}
> $$

These are polynomial identities in $\xi$, not interpolation from a few numerical values. To reproduce the initial conditions (3), the following state of a single core suffices:

$$
\boldsymbol s_1=
\begin{pmatrix}
(x^2-4)(x^2-1)^2\\
x(x^2-1)(x^2-3)\\
x(x^2-1)(x^2-3)\\
-(x^2-1)(x^2-2)\\
x^4-3x^2+1
\end{pmatrix}
\tag{14}
$$

With $d_4=x^4-3x^2+1$ and $f_4=-d_4-x^3+2x$, the common first row is

$$
\mathbf r=(d_4,f_4,f_4,2,x^4+2x^3-2x^2-4x)
$$

The initial polynomials for (9) are specified exactly by $F_j=\mathbf r\mathbf V_v^j\boldsymbol s_1$, $j=0,1,2,3$. The common $F_0$ factors as

$$
\begin{aligned}
F_0(\xi)={}&\xi(\xi^2-5\xi+5)^2(\xi^2-3\xi+1)\,\cdot\\
&\cdot\,(\xi^3-9\xi^2+23\xi-14)
\end{aligned}
$$

The fully expanded initial polynomials and results of direct Laplacian calculations are published in the [exact data](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/periodic-slr-results.json).

## Rooted forests and the minimal order

> [!info] The minimal homogeneous order
> **Proposition 4.** For each of the periods LR, SL, and LLS, the minimal order of a homogeneous linear recurrence with coefficients constant in $m$ is five, both over $\mathbb Q(\xi)$ for $F_m(\xi)$ and over $\mathbb Q$ for $c_m$.

> [!note]- Proof of minimality
> **Proof.** A recurrence of order $d$ implies rank at most $d$ for the Hankel matrix $(F_{i+j})_{i,j\ge0}$: every subsequent column is a linear combination of the preceding $d$ columns. For the numbers $c_0,\ldots,c_8$ obtained by exact transfer, compute the integer determinant $H_5=\det(c_{i+j})_{i,j=0}^4$. Its residues provide short certificates that it is nonzero:
>
> | Period | $H_5\pmod{101}$ |
> |---|---:|
> | LR | 53 |
> | SL | 61 |
> | LLS | 51 |
>
> Hence $H_5\ne0$. The corresponding polynomial determinant formed from $F_j(\xi)$ is also not identically zero, since it is nonzero at $\xi=-1$. Thus the order is at least five. Recurrence (10) gives the opposite bound. The full integer determinants and underlying sequences are recorded in the results file. $\square$

The fourth-order recurrence (9) does not contradict this: it has a nonzero constant right-hand side. Minimality concerns homogeneous recurrences with coefficients independent of $m$. Nor does it imply minimality of five coordinates among all possible descriptions of the graph.

## Shifting the start of the period and the role of the ends

A cyclic shift of a period replaces $v=\beta_1\cdots\beta_p$ by $v'=\beta_2\cdots\beta_p\beta_1$. The graphs remain open: the letters of the block are cyclically permuted, rather than the chain ends being identified.

> [!info] Similar transfer matrices and different finite spectra
> **Proposition 5.** The matrices $\mathbf V_v$ and $\mathbf V_{v'}$ are similar, so their $a,b$ coincide. However, $F_m^{(v)}$ and $F_m^{(v')}$ may differ. In particular, for every $m\ge1$, chains with internal words $(LLS)^m$ and $(LSL)^m$ have different spectra.

> [!note]- Proof of phase dependence
> **Proof.** By (7), all $\mathbf U_\beta$ are invertible even at special values of $\xi$. Permuting the factors gives
>
> $$
> \mathbf V_{v'}=\mathbf U_{\beta_1}\mathbf V_v\mathbf U_{\beta_1}^{-1}
> \tag{15}
> $$
>
> However, when the word changes, the initial vector $\boldsymbol s_1$ and terminal row $\mathbf r$ in (3) remain fixed instead of undergoing the corresponding conjugate transformations. Thus similarity does not imply equality of the scalar polynomials.
>
> In both words $(LLS)^m$ and $(LSL)^m$, the number of bends is $b_{\mathrm{turn}}=2m$. The numbers of adjacent identical turns are $h=m$ and $h=m-1$, respectively. The formulas in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]] imply equality of the first five moments and the sixth-moment difference
>
> $$
> s_6(G_m^{(LLS)})-s_6(G_m^{(LSL)})=6
> $$
>
> Newton's identities give, for the rooted coefficients,
>
> $$
> p_j(G_m^{(LLS)})=p_j(G_m^{(LSL)})\quad(0\le j\le5)
> $$
>
> $$
> p_6(G_m^{(LLS)})-p_6(G_m^{(LSL)})=-1
> \tag{16}
> $$
>
> Hence the first differing coefficient of the characteristic polynomials is that of $\xi^{n-6}$, with difference $-1$. $\square$

![Three starting phases of LLS and two different finite-chain spectra](images/Three%20Phases%20of%20the%20LLS%20Period.svg)

In the figure, $h$ is the number of adjacent LL or RR pairs in the internal word.

LR and RL give isomorphic chains by reflection; SL and LS do so by composing reflection with reversal: reversing letter order alone preserves L, whereas chain reversal under our convention also changes L to R. Similarly, $(LLS)^m$ and $(SLL)^m$ belong to the same unmarked class. The three phases of LLS give two classes, not three. At $m=1$,

$$
c_1^{(LLS)}=c_1^{(SLL)}=19514594869,\qquad
c_1^{(LSL)}=19526487399
$$

For phase LSL, the right-hand side of (9) at $\xi=-1$ is $-85698$, even though the coefficients $a,b$ coincide with those for LLS. This is a concrete effect of the end conditions.

## A special parameter and a drop in order

The generic order over $\mathbb Q(\xi)$ cannot automatically be assigned to every numerical value of $\xi$. At $\xi=0$, all $F_m$ vanish. A more informative example occurs at $\xi=2$.

> [!info] The value at $\xi=2$
> **Proposition 6.** For every $m\ge0$,
>
> $$
> \begin{aligned}
> F_m^{(LR)}(2)=F_m^{(SL)}(2)&=-4(m+1)(m+2)\\
> F_m^{(LLS)}(2)=F_m^{(SLL)}(2)&=-8(m+1)^2\\
> F_m^{(LSL)}(2)&=-4(2m+1)(m+2)
> \end{aligned}
> \tag{17}
> $$
>
> For these numerical sequences, the minimal homogeneous order is three. The number $2$ belongs to the spectrum of none of the specified finite chains.

> [!note]- Proof of the specialized formulas
> **Proof.** Write $\mathbf V_2=\mathbf V_v(2)$, $\mathbf r_2=\mathbf r(2)$, and $\boldsymbol t=\boldsymbol s_1(2)$. From (14) and the row following it,
>
> $$
> \boldsymbol t=(-4,0,0,-2,1)^{\mathsf T},\qquad
> \mathbf r_2=(1,-1,-1,2,0)
> $$
>
> For each of the five words LR, SL, LLS, SLL, and LSL, direct multiplication of integer matrices gives the certificate
>
> $$
> \mathbf r_2\mathbf V_2^j(\mathbf V_2-\mathbf I)^3\boldsymbol t=0,
> \qquad j=0,1,2,3,4
> \tag{18}
> $$
>
> By the Cayley–Hamilton theorem, these five zeros imply the same equality for all $j\ge0$. Thus the third finite difference of the sequence $F_m(2)$ vanishes identically. The first three values determine a polynomial in $m$; substitution gives (17). Its second difference is nonzero, so the minimal homogeneous annihilator is $(q-1)^3$. All expressions in (17) are negative for $m\ge0$, proving the absence of the eigenvalue $2$. $\square$

For example, the characteristic polynomial of $\mathbf V_{SL}(2)$ is $(q-1)^3(q+1)^2$, but the factor $q+1$ does not appear in the scalar sequence (17). The transfer matrix and the sequence observed through specified ends may have different minimal polynomials.

Another check of phase dependence follows directly from (17): $F_m^{(LLS)}(2)-F_m^{(LSL)}(2)=4m$.

## The generating function and growth of rooted forest counts

Let $z$ mark the number of period repetitions. Define

$$
\begin{aligned}
R_v(z)={}&F_0+(F_1-aF_0)z+{}\\
&{}+(F_2-aF_1+bF_0)z^2+{}\\
&{}+(F_3-aF_2+bF_1-aF_0)z^3
\end{aligned}
$$

Multiplying the formal series by the denominator and applying (9) gives

$$
\sum_{m\ge0}F_mz^m=
\frac{(1-z)R_v(z)+\kappa z^4}
{(1-z)(1-az+bz^2-az^3+z^4)}
\tag{19}
$$

This is an identity of formal series; no convergence assumption is needed. At $\xi=-1$, numerator and denominator are coprime for all three main periods, consistent with minimal order five.

Reciprocity reduces finding the multipliers to two quadratic equations. Indeed,

$$
Q_v(q)=q^2\bigl[(q+q^{-1})^2-a(q+q^{-1})+b-2\bigr]
$$

In the following formulas, $a,b$ have already been evaluated at $\xi=-1$. Set

$$
y_\pm=\frac{a\pm\sqrt{a^2-4(b-2)}}2,\qquad
\lambda_\pm=\frac{y_\pm+\sqrt{y_\pm^2-4}}2
\tag{20}
$$

For LR, SL, and LLS, we have $y_+>y_->2$. The five distinct positive multipliers are

$$
\lambda_+,\quad\lambda_-,\quad1,\quad\lambda_-^{-1},\quad\lambda_+^{-1}
$$

> [!info] Growth per core
> **Proposition 7.** For the three main periods and all their cyclic phases, there exists $C_v>0$ such that
>
> $$
> c_m^{(v)}\sim C_v\lambda_+^m,\qquad
> \lim_{m\to\infty}(c_m^{(v)})^{1/(pm+2)}=\gamma_v=\lambda_+^{1/p}
> \tag{21}
> $$
>
> A cyclic shift of the period preserves $\gamma_v$, although it may change $C_v$ and all finite polynomials.

> [!note]- Proof of the asymptotic formula
> **Proof.** The integers in the table satisfy $a>4$, $a^2-4(b-2)>0$, and $b-2a+2>0$. The vertex of the parabola $y^2-ay+b-2$ lies to the right of $2$, its value at $2$ is positive, and its discriminant is positive. Both roots therefore exceed $2$, proving the stated ordering of multipliers.
>
> The sequence $c_m$ is a linear combination of powers of the five distinct multipliers. The nonzero Hankel determinant in Proposition 4 means that all five coefficients are nonzero. For phases RL, LS, and SLL, this also follows from isomorphism; for LSL, the residue of $H_5$ modulo $101$ is $55$. The coefficient of the dominant multiplier $\lambda_+$ is positive; otherwise, $c_m$ would be negative for large $m$. This gives (21). Similarity (15) preserves the multipliers and hence the growth per core. $\square$

| Period | Length $p$ | Dominant multiplier $\lambda_+$ | Growth per core $\gamma_v$ |
|---|---:|---:|---:|
| LR | 2 | 7752,349113 | 88,047425 |
| SL | 2 | 7797,789130 | 88,305091 |
| LLS | 3 | 686149,785698 | 88,200892 |

The numbers in this table are rounded; their exact definition is given by (20)–(21). The multipliers for LR and LLS cannot be compared directly without accounting for period length: one step adds different numbers of cores.

![Growth rate of rooted forest counts per core](images/Rooted%20Forest%20Growth%20in%20Periodic%20Chains.svg)

This asymptotic result concerns the total number of rooted forests of finite graphs. It does not itself describe spectral bands of an infinite chain or prove that a period can be recovered from a single growth rate.

## Exact checks and the status of the results

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_periodic_slr.py) uses integer and polynomial arithmetic. It checks:

- identities (7) for the three transitions, characteristic polynomials of the period matrices, coefficients (11)–(13), invariance of $Q_v(\mathbf V_v)\boldsymbol s_1$, and the right-hand sides of the recurrences;
- $35$ full characteristic polynomials of family (1): the seven phases LR, RL, SL, LS, LLS, LSL, SLL at $0\le m\le4$, up to $N=14$ and $n=58$;
- a further $28$ polynomials for runners starting from an edge at $0\le m\le3$, with a separate check of the corresponding internal words;
- similarity of the phases, minimality certificates, equalities (18), generating functions, and the first differences between phases LLS and LSL;
- correspondence of figure edges with independently constructed graphs; approximate coordinates are used only for illustration.

Direct polynomials are computed from Laplacians of graphs constructed by attaching fresh vertices, without using spectral transfer matrices. The check count includes repeated graphs for different phases and the common initial value. The [full results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/periodic-slr-results.json) and [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) are available with the sources.

| Result | Status |
|---|---|
| Reciprocal structure (4)–(7) for every period | Proved by matrix identities |
| Recurrences for every length with specified ends | Proved by the Cayley–Hamilton theorem |
| Minimal order five for LR, SL, and LLS | Proved by exact Hankel certificates |
| Difference between phases LLS and LSL for every $m\ge1$ | Proved by the sixth coefficient and independently by (17) |
| Formulas at $\xi=2$ and asymptotic formula (21) | Proved for the specified periods and phases |
| Agreement of direct determinants with transfer in the stated range | Independent finite computational verification |

The minimal order for an arbitrary period, classification of coinciding spectra of different periodic families, ring closures, and the spectrum of an infinite chain remain separate problems. The conjectures in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]] on full distinguishability by the characteristic polynomial or by $P_G(1)$ are not proved here. No new conjectures asserting universal injectivity of periodic data are introduced.

## Sources and related notes

Powers of a period matrix, linear recurrences, and rational generating functions belong to the classical transfer-matrix method. The relation between determinants of block tridiagonal matrices and transfer is studied, for example, by Molinari [1]. That work provides general methodological context, not the specific coefficients for SLR periods. The computations here use five boundary minors of the Laplacian with explicitly selected ends; scientific priority of these specializations is not established.

1. L. G. Molinari. *Determinants of Block Tridiagonal Matrices*. Linear Algebra and its Applications **429** (2008), 2221-2226. [arXiv:0712.0681](https://arxiv.org/abs/0712.0681); [DOI](https://doi.org/10.1016/j.laa.2008.06.015).

Related notes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]], [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]. Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].
