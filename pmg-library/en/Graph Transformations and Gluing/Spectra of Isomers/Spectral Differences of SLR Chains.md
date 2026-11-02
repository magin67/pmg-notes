---
title: Spectral Differences of SLR Chains
date: '2026-11-02'
updated: '2026-11-02'
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-spectral-differences
order: 4
description: 'Exact spectral differences caused by changing seam positions: a rank-two identity, mixed differences, and the first sensitive rooted coefficient.'
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Спектральные разности SLR-цепочек|Спектральные разности SLR-цепочек]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

In [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]], moving one seam changed the characteristic polynomial by the square $\chi_{C_5}$. We now consider such a change inside an arbitrary open hexagonal chain. [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]] separates the modified step from the surrounding fragments, while [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] fixes the seam endpoint order. This yields a compact formula involving two combinations of boundary coordinates. With several changes, it matters whether they are consecutive and whether a boundary permutation is inserted between steps.

> [!note] Origins and scope of the result
> Transfer computation of determinants, expansion of a difference of products, and the Cayley-Hamilton theorem are classical methods. Transfer determinant formulas appear, for example, in Molinari [1]. Neither their use nor their expression in PMG coordinates establishes scientific priority. Below we derive the specific difference identities from the published hexagon matrices. All statements concern the specified open-chain model.

## Two concrete differences first

We retain the conditions of [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains#The chains being encoded|The chains being encoded]]: cores $C_6$, unit conductances, shared edges counted once, and vertex-disjoint input and output seams in every internal core. There are no nonadjacent contacts or closure. The number of cores is $N$, and the number of vertices $n=4N+2$. The code $w=Su$ begins with a conventional marker, and its turn word $u$ has length $N-2$.

Set

$$
g=\xi^2-5\xi+5,\qquad q=\chi_{C_5}(\xi)=\xi g^2
$$

> [!example] Straight continuation and two turn directions
> **Computed directly.** For three and four cores, respectively,
>
> $$
> \begin{aligned}
> \chi_{SS}-\chi_{SL}&=q^2,\\
> \chi_{SLL}-\chi_{SLR}&=-(\xi-2)^2q^2
> \end{aligned}
> \tag{1}
> $$
>
> The second pair has the same number of bends. The spectrum detects their relative direction, not only their presence.

![Two pairs of chains differing at one seam position](One%20Seam%20and%20Two%20Spectral%20Differences.svg)

**One changed letter, different difference polynomials.** In the upper pair, $S$ is replaced by $L$; in the lower pair, the second $L$ is replaced by $R$. At $\xi=-1$, the differences are $14641$ and $-131769$. They are also differences of $P_G(1)$, because $n$ is even and $P_G(1)=(-1)^n\chi_G(-1)$.

Formula (1) does not yet imply that every difference between longer chains is divisible by $q^2$. An explicit counterexample to that generalization appears below.

## Locating the changed step

For an ordered active pair, use the spectral passport $s=(A,B,C,D,E)^{\mathsf T}$: $A=\det(\xi\mathbf I-\mathbf L)$; $B,C$ are the principal minors deleting the first and second endpoints; $D$ is the corresponding off-diagonal adjugate entry; and $E$ is the minor deleting both endpoints. Deleting rows and columns does not recalculate the remaining vertex degrees. Full definitions are given in [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]].

The matrix $\mathbf J$ interchanges $B,C$ and leaves the other coordinates unchanged. In the adopted SLR convention, the new core's input $(0,1)$ coincides with the old pair $(b,a)$, so

$$
\mathbf U_L=\mathbf T_2\mathbf J,\qquad
\mathbf U_S=\mathbf T_3\mathbf J,\qquad
\mathbf U_R=\mathbf T_4\mathbf J
\tag{2}
$$

Here $\mathbf T_j$ are given in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#Three outputs of a unit hexagon|Three outputs of a unit hexagon]]; they identify the input endpoints in the same order. The initial passport $s_1$ belongs to a single $C_6$. Let $\mathbf r$ denote the common first row of all $\mathbf U_\alpha$, representing the final core attachment.

For a word $u=\alpha_1\cdots\alpha_m$, define

$$
\begin{aligned}
\mathbf M(u)&=\mathbf U_{\alpha_m}\cdots\mathbf U_{\alpha_1},
&\mathbf M(\varnothing)&=\mathbf I_5,\\
\chi_{Su}&=\mathbf r\mathbf M(u)s_1
\end{aligned}
\tag{3}
$$

The initial symbol $S$ is not an extra transition. In (3), $m=N-2$, and the same row $\mathbf r$ completes the calculation for every word.

> [!info] One change in a fixed context
> **Proposition.** Let $p$ be the word before the changed position and $v$ the word after it. For any $\alpha,\beta\in\{S,L,R\}$,
>
> $$
> \boxed{
> \begin{aligned}
> &\chi_{Sp\alpha v}-\chi_{Sp\beta v}\\
> &\quad=\mathbf r\mathbf M(v)
> (\mathbf U_\alpha-\mathbf U_\beta)\mathbf M(p)s_1
> \end{aligned}
> }
> \tag{4}
> $$

> [!note]- Derivation of the single-change formula
> **Proof.** By the product-order definition, $\mathbf M(p\alpha v)=\mathbf M(v)\mathbf U_\alpha\mathbf M(p)$. Subtracting the two instances of (3) gives (4). No matrices are reordered. $\square$

The formula separates the left-fragment state $s_p=\mathbf M(p)s_1$ from the right-fragment functional $\ell_v=\mathbf r\mathbf M(v)$. It compares entire polynomials. For one substitution $\xi$, the matrices may first be evaluated at that value, but such a check does not replace polynomial equality.

## Two combinations instead of five in a local difference

Denote the ordinary difference of two letter transitions by $\boldsymbol\Delta=\mathbf U_S-\mathbf U_L$. Multiplication of matrices (2) gives the factorization

$$
\boldsymbol\Delta=\mathbf P\mathbf Q
\tag{5}
$$

where

$$
\mathbf P=
\begin{pmatrix}
0&0\\
\xi-2&1-\xi\\
0&1\\
-1&1\\
1&-1
\end{pmatrix},\qquad
\mathbf Q=
\begin{pmatrix}
1&-\xi&0&0&\xi\\
0&-1&1&0&0
\end{pmatrix}
\tag{6}
$$

Here $\mathbf P,\mathbf Q$ denote auxiliary rectangular matrices, not the rooted polynomial $P_G$ or the dual grades $Q_k$.

> [!info] A two-dimensional local difference
> **Proposition.** The matrix $\boldsymbol\Delta$ has rank $2$ for every $\xi$. In formula (4) for $S/L$, the old passport enters only through
>
> $$
> \mathbf Qs_p=
> \begin{pmatrix}
> A_p-\xi B_p+\xi E_p\\
> C_p-B_p
> \end{pmatrix}
> \tag{7}
> $$
>
> If $\ell_v\mathbf P=(\eta_1,\eta_2)$, then
>
> $$
> \chi_{SpSv}-\chi_{SpLv}
> =\eta_1(A_p-\xi B_p+\xi E_p)+\eta_2(C_p-B_p)
> \tag{8}
> $$

> [!note]- Checking the factorization and rank
> **Proof.** Subtract the recurrences for outputs $(3,4)$ and $(2,3)$, then interchange the input coordinates $B,C$. The result is product (6). The minor of $\mathbf P$ on rows $C,D$ equals $1$, and the minor of $\mathbf Q$ on columns $A,C$ also equals $1$. Thus $\mathbf P$ is injective from a two-dimensional space, $\mathbf Q$ is surjective onto it, and the product has rank $2$ with no exceptional parameter values. Formulas (7), (8) follow by multiplication. $\square$

![Left passport and right continuation in the local difference formula](Two%20Combinations%20in%20a%20Seam%20Difference.svg)

**The difference is reduced, not the entire spectral calculation.** The chosen change requires two combinations of the old passport and two coefficients of the right continuation. This does not imply a two-coordinate automaton for all chain letters: these two combinations are not asserted to form a closed state under ordinary continuation.

Reflection gives the other comparisons:

$$
\begin{aligned}
\mathbf U_S-\mathbf U_R&=\mathbf J\boldsymbol\Delta\mathbf J,\\
\mathbf U_L-\mathbf U_R&=\mathbf J\boldsymbol\Delta\mathbf J-\boldsymbol\Delta
\end{aligned}
\tag{9}
$$

For empty $p,v$, substituting the initial passport and final row gives

$$
\mathbf Qs_1=(-q,0)^{\mathsf T},\qquad
\mathbf r\mathbf P=(-q,q)
\tag{10}
$$

Consequently, $\chi_{SS}-\chi_{SL}=q^2$. This explains the square for three cores: one factor comes from the initial fragment and the other from the final attachment. For a nonempty context, the expressions in (10) change.

### The factor depends on the context

Introduce two polynomials

$$
\begin{aligned}
a&=\xi^2-4\xi+2,\\
h&=\xi^6-16\xi^5+101\xi^4-320\xi^3\\
&\quad+534\xi^2-444\xi+143
\end{aligned}
$$

> [!example] Three positions of a single S/L change
> **Computed directly.** Formula (8) and direct Laplacians give
>
> $$
> \begin{aligned}
> \chi_{SS}-\chi_{SL}&=\xi^2g^4,\\
> \chi_{SSS}-\chi_{SSL}&=\xi^2g^2ah,\\
> \chi_{SSSS}-\chi_{SSLS}&=\xi^2a^2h^2
> \end{aligned}
> \tag{11}
> $$

The last two differences are not divisible by $q^2=\xi^2g^4$. At $\xi=-1$, they equal $1320473$ and $119093569$. Each row changes one $S$ to $L$, but the number and positions of surrounding cores differ. The universal formula is (8), not a fixed factor $q^2$.

## Several changed seams

Two words of equal length can be compared by changing one letter at a time. Let $u=\alpha_1\cdots\alpha_m$ and $v=\beta_1\cdots\beta_m$. The telescoping expansion is

$$
\begin{aligned}
\chi_{Su}-\chi_{Sv}
={}&\sum_{i=1}^{m}
\mathbf r\mathbf M(\alpha_{i+1}\cdots\alpha_m)\\
&\quad\cdot(\mathbf U_{\alpha_i}-\mathbf U_{\beta_i})
\mathbf M(\beta_1\cdots\beta_{i-1})s_1
\end{aligned}
\tag{12}
$$

Empty products are identities. Each summand has its own intermediate context; in general, one cannot add local effects all computed solely in the original chain.

A different operation is a *mixed difference*: the alternating sum over independent choices of $S/L$ at several positions. For two selected positions separated by a fixed word $b$, it is

$$
\begin{aligned}
&\chi_{SpSbSv}-\chi_{SpLbSv}
 -\chi_{SpSbLv}+\chi_{SpLbLv}\\
&\qquad=\ell_v\boldsymbol\Delta\mathbf M(b)\boldsymbol\Delta s_p\\
&\qquad=\ell_v\mathbf P
 \bigl(\mathbf Q\mathbf M(b)\mathbf P\bigr)\mathbf Qs_p
\end{aligned}
\tag{13}
$$

> [!note]- Derivation of multiple differences
> **Proof.** For (12), consider the intermediate words $\beta_1\cdots\beta_i\alpha_{i+1}\cdots\alpha_m$ and add differences of consecutive polynomials using (4). For (13), expand the two factors $(\mathbf U_S-\mathbf U_L)$ distributively while retaining their order. The last equality uses (5). $\square$

The matrix between the two differences in (13) has size $2\times2$, but depends on the entire intervening word $b$. Three or more selected positions produce corresponding products of these blocks. If fixed letters separate the changed positions, the blocks cannot all be replaced by the same one.

## Mixed differences at consecutive letters

Now suppose the changed positions are consecutive. Define $f=\xi(4-\xi)$. By (5),

$$
\mathbf K=\mathbf Q\mathbf P=
\begin{pmatrix}
-\xi(\xi-3)&\xi(\xi-2)\\
2-\xi&\xi
\end{pmatrix},\qquad
\operatorname{tr}\mathbf K=\det\mathbf K=f
\tag{14}
$$

> [!info] A recurrence for ordinary S/L changes
> **Theorem.** Under convention (2),
>
> $$
> \boxed{\boldsymbol\Delta^3
> =f\boldsymbol\Delta^2-f\boldsymbol\Delta}
> \tag{15}
> $$
>
> For any fixed $\ell,s$ and $D_r=\ell\boldsymbol\Delta^rs$, when $r\ge1$,
>
> $$
> \boxed{D_{r+2}=f(D_{r+1}-D_r)}
> \tag{16}
> $$

> [!note]- Proof of the recurrence
> **Proof.** For the two-dimensional matrix (14), Cayley-Hamilton gives $\mathbf K^2-f\mathbf K+f\mathbf I_2=0$. Multiplying on the left by $\mathbf P$ and on the right by $\mathbf Q$ gives (15), since $\boldsymbol\Delta^r=\mathbf P\mathbf K^{r-1}\mathbf Q$ for $r\ge1$. Multiplying (15) by $\boldsymbol\Delta^{r-1}$ and then by $\ell,s$ gives (16). There is no division by $f$; zeros of $\xi=0,4$ are included. $\square$

For entire chains without additional context, set $\ell=\mathbf r$, $s=s_1$. Then $D_r$ concerns $N=r+2$ cores and has the exact combinatorial interpretation

$$
D_r=\sum_{u\in\{S,L\}^r}(-1)^{\#L(u)}\chi_{Su},
\qquad D_1=q^2,\quad D_2=(f-2)q^2
\tag{17}
$$

This is an alternating sum of polynomials of different graphs, not the characteristic polynomial of one graph. After division by $q^2$, its first values are

| $r$ | $D_r/q^2$ |
| --- | --- |
| $1$ | $1$ |
| $2$ | $f-2$ |
| $3$ | $f(f-3)$ |
| $4$ | $f(f^2-4f+2)$ |

For a fixed nonempty context, recurrence (16) still holds, but the initial $D_1,D_2$ and their divisibility change. For fixed gaps between selected positions, use (13).

## Why an extra permutation gives a different recurrence

Consider another operator,

$$
\mathbf H=\boldsymbol\Delta\mathbf J
=\mathbf T_3-\mathbf T_2
\tag{18}
$$

The right factor $\mathbf J$ interchanges the input endpoints before the difference step. It cannot be inserted into (17) while still treating all letters as independent choices from the same alphabet $\{S,L\}$.

> [!info] A difference with an extra boundary permutation
> **Proposition.** For operator (18),
>
> $$
> \mathbf H^3=f\mathbf H
> \tag{19}
> $$
>
> Therefore, for $\widehat D_r=\mathbf r\mathbf H^rs_1$,
>
> $$
> \begin{aligned}
> \widehat D_1&=q^2,&\widehat D_2&=2q^2,\\
> \widehat D_{r+2}&=f\widehat D_r\quad(r\ge1)
> \end{aligned}
> \tag{20}
> $$

> [!note]- Derivation and conversion back to SLR words
> **Proof.** The two-dimensional block is now
>
> $$
> \mathbf Q\mathbf J\mathbf P=
> \begin{pmatrix}\xi&-2\xi\\\xi-2&-\xi\end{pmatrix}
> $$
>
> Its square is $f\mathbf I_2$, proving (19). The initial values in (20) follow by substituting $s_1,\mathbf r$.
>
> In product $(\boldsymbol\Delta\mathbf J)^r$, move all $\mathbf J$ to the right using $\mathbf J^2=\mathbf I$ and $\mathbf Js_1=s_1$. The difference factors alternate between $\boldsymbol\Delta$ and $\mathbf J\boldsymbol\Delta\mathbf J=\mathbf U_S-\mathbf U_R$. Thus, in chronological position order $j=1,\ldots,r$, the choices are $S/L$ for even $r-j$ and $S/R$ for odd $r-j$, with a minus sign for each bend. This is a different alternating sum. $\square$

For two positions the distinction is particularly clear. Using graph reflection for the equalities $\chi_{SSR}=\chi_{SSL}$ and $\chi_{SRL}=\chi_{SLR}$, we obtain

$$
\begin{aligned}
D_2&=\chi_{SSS}-\chi_{SSL}-\chi_{SLS}+\chi_{SLL},\\
\widehat D_2&=\chi_{SSS}-\chi_{SSL}-\chi_{SLS}+\chi_{SLR}
\end{aligned}
\tag{21}
$$

![Ordinary and reoriented mixed differences of four chains](Two%20Mixed%20SLR%20Differences.svg)

**The final graph changes the recurrence.** At $\xi=-1$, the ordinary sum is $-102487$, and the sum with an extra permutation is $29282$. Their difference is $\chi_{SLL}(-1)-\chi_{SLR}(-1)=-131769$, as in (1). Identity (19) is valid, but cannot be applied to the ordinary $D_r$ in (17).

## How the number of bends appears in the coefficients

Write the rooted polynomial and its associated characteristic polynomial as

$$
\begin{aligned}
P_G(t)&=\sum_{k=0}^{n-1}p_k(G)t^k,\\
\chi_G(\xi)&=\sum_{k=0}^{n-1}(-1)^kp_k(G)\xi^{n-k}
\end{aligned}
\tag{22}
$$

Here $p_k$ are the rooted forest coefficients from [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], not coefficients of the ordinary forest polynomial. Let $b(G)$ be the number of letters $L,R$ in the turn word.

> [!info] The first sensitive rooted coefficient
> **Theorem.** All chains under consideration with the same $N$ share $p_0,p_1,p_2,p_3$. For any two such graphs,
>
> $$
> \boxed{p_4(G)-p_4(H)=b(H)-b(G)}
> \tag{23}
> $$
>
> Thus different bend counts first affect the coefficient of $\xi^{n-4}$ when reading $\chi$ in descending degree. If the bend counts are equal, this coefficient also agrees; later coefficients may differ.

> [!note]- Proof through vertex degrees and traces
> **Proof.** Each seam endpoint has degree $3$. Since seams are vertex-disjoint, there are $2N-2$ such vertices and $2N+4$ vertices of degree $2$. There are no triangles or four-cycles: by [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains#Which words specify the same graph|Which words specify the same graph]], a simple cycle has length $4k+2$.
>
> The $N-1$ seam edges join vertices of degree $3$. Each bend adds exactly one such edge inside an internal core; a straight continuation adds none. Their total number is therefore $m_{33}=N-1+b$. If $d_i$ are the vertex degrees, then
>
> $$
> \begin{aligned}
> \sum_{ij\in E(G)}d_id_j
> &=4(5N+1)+6(2N-2)+m_{33}\\
> &=33N-9+b
> \end{aligned}
> $$
>
> Expanding powers of the Laplacian matrix gives, for $\sigma_j=\operatorname{tr}(\mathbf L^j)$,
>
> $$
> \begin{aligned}
> \sigma_1&=10N+2,& \sigma_2&=36N,\\
> \sigma_3&=148N-28,& \sigma_4&=648N-228+4b
> \end{aligned}
> $$
>
> In particular, without triangles or four-cycles,
>
> $$
> \begin{aligned}
> \sigma_4&=\sum_i d_i^4+4\sum_i d_i^3+4\sum_{ij\in E(G)}d_id_j\\
> &\quad+2\sum_i d_i^2-2\#E(G)
> \end{aligned}
> $$
>
> The coefficients $p_k$ are elementary symmetric polynomials in the eigenvalues. The classical Newton identities read $kp_k=\sum_{j=1}^k(-1)^{j-1}p_{k-j}\sigma_j$. The first three traces agree, so $p_1,p_2,p_3$ agree as well. Subtracting the formulas for $4p_4$ leaves $-(\sigma_4(G)-\sigma_4(H))=-4(b(G)-b(H))$. This is (23). $\square$

![Edges between degree-three vertices at a straight continuation and a bend](A%20Bend%20and%20the%20Fourth%20Rooted%20Coefficient.svg)

**A bend adds one edge between seam endpoints.** The figure shows an internal core after its neighbors have been attached. Endpoints of the red seams have degree $3$. The additional blue edge occurs for $L$ or $R$ and increases the fourth spectral moment by $4$.

Replacing $S$ by $L$ or $R$ always changes the spectrum, regardless of context: the bend count increases by one. Formula (23) gives no such conclusion for replacing $L$ by $R$. For example, $SL$ and $SR$ are isomorphic, whereas $SLL$ and $SLR$ have different spectra. In the latter case, difference (1) has degree $12=n-6$; the first difference occurs later than $p_4$.

There is also a general constraint at low degrees. All chains with the same $N$ have the same spanning-tree count $\tau$ by [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. They are connected, so the constant coefficient of $\chi$ is zero and the coefficient of $\xi$ is $(-1)^{n-1}n\tau$. Consequently,

$$
\xi^2\ \mid\ \chi_G-\chi_H
\tag{24}
$$

Unlike $q^2$, this divisor is common to every pair in the stated class with the same number of cores. Formulas (22)-(24) connect spectral differences with rooted coefficients while preserving the distinction between ordinary and rooted forest data.

## Exact checks and limits of the conclusion

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_spectral_differences.py) constructs graphs from cycles and vertex identifications, without using transfer to construct edges. It performs:

- symbolic verification of factorization (5), both two-dimensional blocks, identities (15), (19), and initial values;
- independent computation of the full characteristic polynomials of integer Laplacians for all $121$ words with $2\le N\le6$;
- checks of all $426$ single-letter changes on this set, including $L/R$, and $64$ mixed differences at two chosen positions, retaining intervening letters;
- direct verification of traces, the number of edges between degree-$3$ vertices, and the formula for $\sigma_4$ for all $364$ words with $2\le N\le7$; comparison with the coefficients of all $121$ polynomials;
- comparison of ordinary and reoriented alternating sums with direct polynomials for $1\le r\le4$, verification of recurrences through $r=8$, and all examples (1), (11), (21).

The [exact results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/spectral-differences-results.json) include polynomial differences, example edge lists, and values of $P_G(1)$. [Reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) and the drawing program are stored alongside them. These checks require no numerical eigenvalue approximations.

**Proved:** the change formula in an arbitrary context, rank $2$ of the local difference, the expansion of several changes, distinct recurrences for the two boundary conventions, the dependence of $p_4$ on the bend count, and divisibility of every pairwise difference by $\xi^2$. Factorizations for specific pairs are additionally checked using direct Laplacians.

These results do not establish completeness of spectral data. The bend count can be recovered from the spectrum when $N$ is known, but this note does not recover the entire code. Injectivity of the full marked state at $\xi=-1$ is proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]. Injectivity of the characteristic polynomial and of one value $P_G(1)$ remain two separate questions.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

## Sources and connections

1. L. G. Molinari. *Determinants of Block Tridiagonal Matrices*. Linear Algebra and its Applications **429** (2008), 2221-2226. [arXiv:0712.0681](https://arxiv.org/abs/0712.0681), [DOI: 10.1016/j.laa.2008.06.015](https://doi.org/10.1016/j.laa.2008.06.015). Classical transfer computation of determinants; this note's specific difference matrices are derived from the hexagon transitions, not taken from that article.

Supporting notes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]].
