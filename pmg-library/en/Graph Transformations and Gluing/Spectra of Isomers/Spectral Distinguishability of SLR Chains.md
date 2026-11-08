---
title: Spectral Distinguishability of SLR Chains
date: '2026-11-02'
updated: '2026-11-02'
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: spectral-distinguishability-of-slr-chains
order: 8
description: Recovery of bend statistics from spectral moments, limitations of leading coefficients, an exact catalog up to 18 cores, and distinguishability
  conjectures.
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Спектральная различимость SLR-цепочек|Спектральная различимость SLR-цепочек]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

The Laplacian spectrum determines the number of bends in a hexagonal chain and the number of adjacent turns in the same direction. Both results have general proofs. Recovering the entire configuration from the spectrum remains a separate problem: exact enumeration up to 18 cores finds no collisions even for a single value of the rooted polynomial, but does not by itself settle the question for chains of arbitrary length.

> [!note] The result in plain language
> The spectrum lets us count the turns in a chain and then determine how often a left turn is immediately followed by a left turn, or a right turn by a right turn. A fixed number of leading coefficients is provably insufficient to recover chains of all lengths.
>
> The situation is different if all coefficients are used, or one exact integer obtained by summing them. Among all 16,150,725 chain classes with 2–18 cores, this integer never repeated. This is an exhaustive check of the stated range. The claim for arbitrary length is formulated below as a conjecture.

The problem continues [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]] and [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]]. Recovery of an oriented word from five boundary numbers was already proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]. Here we study data without a marked boundary: the characteristic polynomial, its leading coefficients, and a single value.

## The class of chains and the meaning of distinguishability

All graphs are finite and open, with unit conductances. Every core is a cycle $C_6$. Adjacent cores share exactly one edge, counted once. The input and output seams of an intermediate core have no common vertices; nonadjacent cores do not intersect. There are no other identifications. Neither planarity nor a layout on a planar hexagonal lattice is required.

For the number of cores $N\ge2$ and the number of vertices $n$,

$$
n=4N+2,\qquad |E(G)|=5N+1,\qquad w=Su,\qquad |u|=N-2
$$

The first letter of the full code $w$ is a marker. It is not part of the internal turn word $u$. Under the conventions of [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], S denotes the opposite output seam, and L and R the two side outputs. When a new cycle is attached to an ordered seam $(a,b)$, its vertices $0,1$ are identified with $b,a$; the outputs are $(2,3)$, $(3,4)$, and $(4,5)$ for L, S, and R, respectively.

Let $\bar u$ exchange L and R while preserving S, and let $u^{\leftarrow}$ reverse letter order. By the classification proved in that note, an unmarked graph is specified by the orbit

$$
[u]=\{u,\bar u,u^{\leftarrow},\overline{u^{\leftarrow}}\}
\tag{1}
$$

An orbit may contain fewer than four words. Reflected or reversed descriptions of the same graph are not examples of cospectrality between different chains.

> [!info] Spectral distinguishability within the class
> **Definition.** Two chain classes are spectrally distinguishable if the characteristic polynomials of their Laplacian matrices differ. The class of chains is spectrally distinguishable if equality of these polynomials implies that the words belong to the same orbit (1).

This is a reconstruction problem within a specified family. It is weaker than determination of a graph by its spectrum among all graphs, as studied in classical spectral theory [1, §1]. The ordinary spectrum retains neither the chosen chain end, the order of boundary contacts, nor the eigenvectors.

## The spectrum, rooted coefficients, and a single number

We use the Laplacian matrix $\mathbf L_G$, the characteristic polynomial $\chi_G$, and the rooted polynomial $P_G$:

$$
\chi_G(\xi)=\det(\xi\mathbf I_n-\mathbf L_G),\qquad
P_G(t)=\det(\mathbf I_n+t\mathbf L_G)=\sum_{j=0}^{n-1}p_j(G)t^j
\tag{2}
$$

The graph is connected, so its zero eigenvalue is simple. With $p_0=1$ and $p_n=0$, the normalizations are related by

$$
\chi_G(\xi)=\sum_{j=0}^{n}(-1)^j p_j(G)\xi^{n-j}
\tag{3}
$$

By the Chebotarev–Shamis matrix-forest theorem [2, Theorem 5], the coefficient $p_j$ counts spanning forests with $j$ edges and a chosen root in every component. A forest without chosen roots contributes the product of its component sizes. Thus $P_G$ differs from the ordinary forest polynomial, which has no such factor; see [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

Introduce the spectral moments

$$
s_k(G)=\operatorname{tr}(\mathbf L_G^k)=\sum_{i=1}^{n}\lambda_i^k
$$

Here a power means matrix multiplication, not the polyform product. The Laplacian form $L_G$ and the operator with matrix $\mathbf L_G$ are related by the chosen coordinate representation, but their powers are not identified.

Newton's identities relate the moments and rooted coefficients:

$$
jp_j=\sum_{k=1}^{j}(-1)^{k-1}p_{j-k}s_k
\tag{4}
$$

They follow by differentiating $\prod_i(1+t\lambda_i)$ and comparing coefficients. Thus, for the same $n$, equality of the first $r$ moments is equivalent to equality of $p_1,\ldots,p_r$. By (3), this compares characteristic-polynomial coefficients starting at the highest degrees.

A separate scalar invariant is

$$
P_G(1)=\sum_{j=0}^{n-1}p_j(G)=(-1)^n\chi_G(-1)=\chi_G(-1)
\tag{5}
$$

The last equality uses evenness of $n=4N+2$. This is one exact integer, not a rounded numerical estimate. It involves every rooted coefficient.

![The full boundary state, the spectrum, and a single value](images/Data%20for%20Distinguishing%20SLR%20Chains.svg)

**Three reconstruction problems.** The full boundary state retains markings and admits proved decoding. For the two scalar spectral representations, a general inverse passage to the graph class remains conjectural. A value can always be computed from the polynomial; injectivity of that value on the family requires separate study.

## Bends and adjacent turns in the same direction

> [!info] Two word parameters
> **Definition.** For the internal word $u=u_1\cdots u_{N-2}$, set
>
> $$
> b(u)=\#\{i:u_i\ne S\},\qquad
> h(u)=\#\{i:u_i=u_{i+1}\in\{L,R\}\}
> \tag{6}
> $$
>
> The number $b$ counts bends, and $h$ counts adjacent pairs LL and RR. Pairs may overlap: LLL contains two LL pairs. When $N=2$, both numbers are zero.

The parameters $b,h$ are invariant under all four operations (1), so they are defined for the unmarked graph. The number $h$ does not distinguish LL from RR: global reflection exchanges them.

> [!info] The first six moments
> **Proposition. Proved.** For every chain in the specified class with $N\ge2$,
>
> $$
> \begin{aligned}
> s_1&=10N+2, & s_2&=36N,\\
> s_3&=148N-28, & s_4&=648N-228+4b,\\
> s_5&=2940N-1428+60b
> \end{aligned}
> $$
>
> $$
> \boxed{s_6=13656N-8112+576b+6h}
> \tag{7}
> $$

The dependence of $s_4$ on the number of bends was already established in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains#How the number of bends appears in the coefficients|How the number of bends appears in the coefficients]]. Below we give a general combinatorial derivation of (7), including the contribution of $h$. We use the classical method of counting closed walks through powers of the adjacency matrix [3, §1.3.3]. Specialization to SLR chains and a separate derivation do not establish scientific priority of the formulas.

> [!note]- Proof of the moment formulas
> **Proof.** Denote the degree of a vertex by $d_v$, the number of degree-$r$ vertices by $n_r$, and the number of edges with endpoint degrees $r,s$ by $m_{rs}$. All vertices have degree 2 or 3. The endpoints of the $N-1$ seams are distinct, so
>
> $$
> n_2=2N+4,\qquad n_3=2N-2
> $$
>
> Every bend adds one edge between degree-3 vertices beyond the seams themselves. Counting incidences gives
>
> $$
> m_{33}=N-1+b,\qquad m_{23}=4N-4-2b,\qquad m_{22}=6+b
> \tag{8}
> $$
>
> Set $k_v=\#\{w\sim v:d_w=3\}$ and $S_v=\sum_{w\sim v}d_w=2d_v+k_v$. A degree-2 vertex has two degree-3 neighbors precisely in the two gaps between opposite seams of a straight core. A degree-3 vertex has one degree-3 neighbor on its seam; additional neighbors arise from bends in adjacent cores. Both additional connections reach the same seam endpoint exactly for LL or RR. Hence
>
> $$
> \sum_{d_v=2}\binom{k_v}{2}=2(N-2-b),\qquad
> \sum_{d_v=3}\binom{k_v}{2}=2b+h
> $$
>
> Also, $\sum_v k_v=6(N-1)$ and $\sum_v d_vk_v=14(N-1)+2b$. Expanding the square $S_v^2$ gives
>
> $$
> \sum_v S_v^2=170N-78+8b+2h
> \tag{9}
> $$
>
> Let $\mathbf A$ be the adjacency matrix and $\mathbf D=\operatorname{diag}(d_v)$, so $\mathbf L=\mathbf D-\mathbf A$. The graph is bipartite, has no 4-cycles, and contains exactly $N$ cycles of length 6. The last assertion also follows from the core recovery lemma in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]: a cycle enclosing $r$ successive cores has length $4r+2$.
>
> For brevity, write $D_j=\sum_v d_v^j$ and $E_{11}=\sum_{vw\in E}d_vd_w$. Expanding traces of powers up to the fifth gives
>
> $$
> \begin{aligned}
> s_1&=D_1,\qquad s_2=D_2+D_1,\qquad s_3=D_3+3D_2,\\
> s_4&=D_4+4D_3+4E_{11}+2D_2-D_1,\\
> s_5&=D_5+5D_4+5\sum_{vw\in E}d_vd_w(d_v+d_w)+{}\\
> &\quad+5(D_3-D_2+2E_{11})
> \end{aligned}
> $$
>
> Substitution of (8) gives the first five formulas. For the sixth moment, only words with 0, 2, 4, or 6 factors $\mathbf A$ remain in the trace. Cyclic permutation of factors inside the trace gives
>
> $$
> \begin{aligned}
> s_6={}&\operatorname{tr}\mathbf D^6+
> 3\sum_{i=0}^4\operatorname{tr}(\mathbf D^i\mathbf A\mathbf D^{4-i}\mathbf A)+{}\\
> &+6\operatorname{tr}(\mathbf D^2\mathbf A^4)+6\operatorname{tr}(\mathbf D\mathbf A\mathbf D\mathbf A^3)+{}\\
> &+3\operatorname{tr}(\mathbf D\mathbf A^2\mathbf D\mathbf A^2)+\operatorname{tr}\mathbf A^6
> \end{aligned}
> $$
>
> Here $(A^4)_{vv}=d_v^2-d_v+S_v$, and for an edge $vw$, we have $(A^3)_{vw}=d_v+d_w-1$. Distinct vertices have at most one common neighbor, so
>
> $$
> \operatorname{tr}(\mathbf D\mathbf A^2\mathbf D\mathbf A^2)=D_4-D_3+\sum_v S_v^2
> $$
>
> Closed walks of length 6 use an edge, a path of two or three edges, a three-leaf star, or a 6-cycle. Counting them gives
>
> $$
> \begin{aligned}
> \operatorname{tr}\mathbf A^6={}&2|E|+12\sum_v\binom{d_v}{2}+
> 6\sum_{vw\in E}(d_v-1)(d_w-1)+{}\\
> &+12\sum_v\binom{d_v}{3}+12N
> \end{aligned}
> $$
>
> After (8)–(9), the six terms in the expansion of $s_6$, in the stated order, are
>
> $$
> \begin{aligned}
> &1586N-1202,\\
> &7494N-4614+378b,\\
> &1788N-924+60b,\\
> &1692N-828+108b,\\
> &882N-462+24b+6h,\\
> &214N-82+6b
> \end{aligned}
> $$
>
> Their sum is (7). $\square$

> [!info] Partial recovery from the spectrum
> **Corollary. Proved.** The spectrum with multiplicities determines $n$, then $N=(n-2)/4$, and
>
> $$
> b=\frac{s_4-648N+228}{4},\qquad
> h=\frac{s_6-13656N+8112-576b}{6}
> \tag{10}
> $$
>
> For two chains with the same $N,b$,
>
> $$
> p_6(G)-p_6(H)=-\bigl(h(G)-h(H)\bigr)
> \tag{11}
> $$

> [!note]- Proof of the corollary
> **Proof.** The recovery formulas follow from (7). With the same $N,b$, the values $s_1,\ldots,s_5$ coincide, so (4) gives equality of $p_1,\ldots,p_5$. Subtracting Newton's identities at $j=6$ leaves $6\Delta p_6=-\Delta s_6=-6\Delta h$. $\square$

![The same number of bends with different adjacent turn pairs](images/The%20Sixth%20Moment%20and%20Adjacent%20Turns.svg)

**Two bends, different adjacencies.** In SLL, one endpoint of the middle seam has three degree-3 neighbors; SLR has no such endpoint. This local difference gives $\Delta h=1$, $\Delta s_6=6$, and $\Delta p_6=-1$. Blue marks seams; red marks degree-3 vertices and additional connections between them. The filled red vertex has three degree-3 neighbors.

## Coinciding leading coefficients

> [!example] Two turns in the same or opposite directions
> **Computed directly.** For the two graphs with four cores,
>
> $$
> \chi_{SLL}(\xi)-\chi_{SLR}(\xi)
> =-\xi^2(\xi-2)^2(\xi^2-5\xi+5)^4
> \tag{12}
> $$
>
> The difference has degree 12 with $n=18$. Thus the first difference occurs in the coefficient of $\xi^{n-6}$, that is, in $p_6$, and equals $-1$ in both representations. The values $P_G(1)$ are $220348791$ and $220480560$.

The parameters $b,h$ do not determine the entire code. Words in the table include the initial marker S; the two graphs in every row are nonisomorphic.

| Full codes | $N$ | $b$ | $h$, left and right | First differing $p_j$ | $p_j$ on the left minus $p_j$ on the right |
|---|---:|---:|---|---:|---:|
| SLL, SLR | 4 | 2 | 1 and 0 | $p_6$ | $-1$ |
| SSSL, SSLS | 5 | 1 | 0 and 0 | $p_8$ | $1$ |
| SLSLL, SLLSR | 6 | 3 | 1 and 1 | $p_{10}$ | $-1$ |

**Computed directly.** In the last row, all nine coefficients $p_1,\ldots,p_9$ coincide. The difference has the form

$$
\chi_{SLSLL}(\xi)-\chi_{SLLSR}(\xi)
=-\xi^2(\xi-2)^2(\xi^2-5\xi+5)^2q(\xi)
\tag{13}
$$

where

$$
\begin{aligned}
q(\xi)={}&\xi^8-20\xi^7+168\xi^6-770\xi^5+2092\xi^4-{}\\
&-3420\xi^3+3247\xi^2-1610\xi+311
\end{aligned}
$$

The full polynomials of both pairs, edge lists, and isomorphism checks are recorded in the [exact data](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/spectral-distinguishability-results.json). The polynomial differences here are computed directly from Laplacians; the moment formulas provide a separate check of their leading coefficients.

![Chain differences appear at different depths in the polynomial](images/Coinciding%20Leading%20Rooted%20Coefficients.svg)

**Depth of the first difference.** The pair with one bend shares its first seven coefficients; the displayed pair with three bends shares its first nine. Colored cells mark the first differing coefficient, and gray cells the common leading segment. The figure shows only this segment, not all coefficients.

## Why a fixed number of leading coefficients is insufficient

> [!info] A limitation of partial spectral recovery
> **Theorem. Proved.** For every fixed integer $k\ge1$ and all sufficiently large $N$, there are two nonisomorphic SLR chains with the same number of cores $N$ and the same $p_1,\ldots,p_k$. Equivalently, their first $k$ spectral moments coincide.

> [!note]- Proof by counting possible data
> **Proof.** For a real column $x$,
>
> $$
> 0\le x^{\mathsf T}\mathbf Lx
> =\sum_{vw\in E}(x_v-x_w)^2
> \le2\sum_v d_vx_v^2\le6\,x^{\mathsf T}x
> $$
>
> Hence all eigenvalues lie in $[0,6]$, and integrality of $\mathbf L$ gives
>
> $$
> s_j\in\mathbb Z,\qquad 0\le s_j\le n6^j
> $$
>
> For fixed $N,k$, the number of possible tuples $(s_1,\ldots,s_k)$ is at most
>
> $$
> \prod_{j=1}^{k}(n6^j+1)=O_k(n^k)
> \tag{14}
> $$
>
> Meanwhile, classification (1) and Burnside's lemma give the exact number of classes for $m=N-2$:
>
> $$
> c_N=\frac{3^m+1+3^{\lceil m/2\rceil}+3^{\lfloor m/2\rfloor}}4
> \tag{15}
> $$
>
> This grows exponentially in $N$, while (14) grows polynomially for $n=4N+2$. For all sufficiently large $N$, there are more classes than data tuples. Two distinct classes therefore have identical moments; identities (4) give equality of the leading coefficients. $\square$

The theorem concerns a fixed number of coefficients counted from $p_1$. It does not assert that cospectral chains exist: the number of coefficients of the full polynomial grows with $N$. Nor does it exclude distinguishability by $P_G(1)$, which sums coefficients of every order and itself grows in digit length.

For illustration, bound (14) already guarantees that some distinct classes have the same first ten moments at $N=152$. This is a crude sufficient bound, not a minimal size. Unlike the table of explicit pairs, the proof does not exhibit the colliding words.

## An exact catalog up to 18 cores

For each $N$, choose the lexicographically least word in orbit (1), with letter order $S<L<R$. Then compute the integer (5), using the transfer proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], specialized at $\xi=-1$ and normalized as in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]].

The initial state of a single hexagon is

$$
\mathbf z_1=(320,144,144,56,55)^{\mathsf T}
$$

If $\mathbf V_S,\mathbf V_L,\mathbf V_R$ are the integer transitions in this normalization, then for $u=u_1\cdots u_m$,

$$
\mathbf z(u)=\mathbf V_{u_m}\cdots\mathbf V_{u_1}\mathbf z_1,\qquad
P_{G(Su)}(1)=(55,34,34,-2,21)\mathbf z(u)
\tag{16}
$$

The row in (16) completes the chain with the last core. It is common to all three outputs; S is used for the canonical terminal boundary. When $u$ is empty, the matrix product is the identity and gives a chain of two cores.

> [!example] The result of exhaustive finite enumeration
> **Computed directly.** Among all $16\,150\,725$ classes with $2\le N\le18$, the values $P_G(1)$ are pairwise distinct. Consequently, their characteristic polynomials are pairwise distinct as well. There are also no collisions between different numbers of cores within this range.

| $N$ | Graph classes | Distinct values of $P_G(1)$ |
|---:|---:|---:|
| 2 | 1 | 1 |
| 3 | 2 | 2 |
| 4 | 4 | 4 |
| 5 | 10 | 10 |
| 6 | 25 | 25 |
| 7 | 70 | 70 |
| 8 | 196 | 196 |
| 9 | 574 | 574 |
| 10 | 1 681 | 1 681 |
| 11 | 5 002 | 5 002 |
| 12 | 14 884 | 14 884 |
| 13 | 44 530 | 44 530 |
| 14 | 133 225 | 133 225 |
| 15 | 399 310 | 399 310 |
| 16 | 1 196 836 | 1 196 836 |
| 17 | 3 589 414 | 3 589 414 |
| 18 | 10 764 961 | 10 764 961 |

The total number of oriented internal words in this range is $64\,570\,081$. Comparison is between class representatives, not all these words: symmetric descriptions necessarily produce the same number.

Integer values are compared in full, without rounding or replacing them by modular residues. The number of representatives is checked against (15). For consecutive sizes, the maximum at $N$ is strictly below the minimum at $N+1$, excluding collisions across sizes throughout the stated range. A single $C_6$ has value $320$, below the minimum $28435$ at $N=2$; it is not included in the class count shown.

The finite catalog permits recovery of a class by lookup of an exact value. It provides neither a decoder for arbitrary length nor a proof of stability under approximate measurements. The latter problem is studied separately for the boundary response in [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]].

## Two conjectures on full distinguishability

> [!note] A working conjecture about the characteristic polynomial
> **Conjecture 1.** For any two SLR chains in the specified class,
>
> $$
> \chi_{G(Su)}=\chi_{G(Sv)}\quad\Longrightarrow\quad [u]=[v]
> \tag{17}
> $$
>
> Equality of the polynomials already ensures the same $n$ and the same $N$.

> [!note] A working conjecture about a single value
> **Conjecture 2.** For every fixed $N$ and $|u|=|v|=N-2$,
>
> $$
> P_{G(Su)}(1)=P_{G(Sv)}(1)\quad\Longrightarrow\quad [u]=[v]
> \tag{18}
> $$

Conjecture 2 is stronger than Conjecture 1: equal polynomials have equal values at $\xi=-1$. The converse does not follow. Equality of a single value for different, previously unknown $N$ is an even stronger question and is not included in (18).

The proved recovery of an oriented word from the full vector $\mathbf z$ proves neither (17) nor (18). Only one linear combination of the five coordinates is retained in (16). Distinct full states can have the same such combination; this must be excluded specifically on the set of admissible words, taking their orbits into account.

The connection with [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]] suggests a concrete continuation: study scalar equalities between products of transfer matrices, beginning with constant and periodic words. Agreement of several initial terms or a common recurrence form alone does not establish equality of spectral families.

## Exact checks and the status of the results

The [main verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_spectral_distinguishability.py) and [large-enumeration program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/catalog_spectral_values.py) serve different purposes:

- for all 1,093 oriented words with $2\le N\le8$, graphs are built from cycles, integer traces of matrix powers through the eighth are computed directly, and (7)–(9) are checked;
- on the same set, the fast integer transitions are checked against the original polynomial matrices by substituting $\xi=-1$;
- for all 42 classes with $2\le N\le6$, full characteristic polynomials are computed directly from Laplacians; their values at $-1$ are compared with transfer;
- 78 determinants $\det(\mathbf I+\mathbf L)$ are computed separately: for these 42 graphs and for the straight, constantly turning, and reproducibly selected mixed chain of each size $7\le N\le18$;
- for the pairs in the table, full differences, first differing coefficients, and nonisomorphism are checked; the isomorphic pair SSL and SLS is a reversal control example;
- symbolic verification confirms the expansion of the sixth moment and corollary (11), while exhaustive enumeration of representatives confirms the finite table and separation of sizes.

Independent construction of the Laplacian and computation of its determinant do not use transfer matrices. All mathematical comparisons use integers or polynomials; numerical coordinates are needed only for figures. The [independent verification results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/spectral-distinguishability-results.json), [catalog summary](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/slr-distinguishability-catalog.json), and [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) are published with the note.

| Result | Status and scope |
|---|---|
| Moment formulas and recovery of $b,h$ | Proved for all $N\ge2$ in the specified class |
| Insufficiency of a fixed number of leading coefficients | Proved for all sufficiently large $N$ for each fixed $k$ |
| Differences of explicit pairs | Computed directly from Laplacians |
| Distinguishability by $P_G(1)$, hence by $\chi_G$, up to 18 cores | Exhaustive finite computational verification |
| Recovery of an oriented word from the full boundary state | Proved in a separate note for arbitrary length |
| Full spectral distinguishability for arbitrary length | Working Conjecture 1 |
| Distinguishability by a single value for every fixed $N$ | Working Conjecture 2 |

Scientific priority of the specific formulas and conjectures is not established here. The general problem of spectral determination, the moment method, Newton's identities, and the matrix-forest interpretation are classical foundations. The specific proofs and exact catalog concern the stated class of abstract SLR chains.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

Continuation: [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra|Periodic SLR Chains: Recurrences and Spectra]]. Exact recurrences are obtained for LR, SL, and LLS; the effects of end cores, cyclic shifts of the period, and growth of the number of rooted forests are discussed.

## Sources and related notes

1. E. R. van Dam, W. H. Haemers. *Which graphs are determined by their spectrum?* Linear Algebra and its Applications **373** (2003), 241–272. [DOI: 10.1016/S0024-3795(03)00483-X](https://doi.org/10.1016/S0024-3795(03)00483-X). §1: the problem of determination by the spectrum; the article also treats the Laplacian. It is not used as a proof of conjectures (17)–(18).
2. P. Chebotarev, E. Shamis. *Matrix-Forest Theorems*. Manuscript, 1994–1997, [arXiv:math/0602575](https://arxiv.org/abs/math/0602575), Theorem 5. The determinant $\mathbf I+\mathbf L$ counts spanning rooted forests; applying it to $t\mathbf L$ gives the coefficients $P_G(t)$.
3. A. E. Brouwer, W. H. Haemers. *Spectra of Graphs*. Springer, 2012. [Author's page and available text](https://homepages.cwi.nl/~aeb/math/ipm/), §1.3.3, “Walks”: powers of the adjacency matrix and closed walks. Formula (7) is derived here by specializing the count to the degrees and seams of an SLR chain.

Foundational notes: [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]], [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].
