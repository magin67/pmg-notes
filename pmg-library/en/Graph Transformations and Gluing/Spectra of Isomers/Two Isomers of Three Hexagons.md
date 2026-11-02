---
title: Two Isomers of Three Hexagons
date: '2026-11-02'
updated: '2026-11-02'
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-three-hexagons
order: 1
description: 'Two chains with the same matroid parameters and different spectra: exact polynomials, the first rooted-forest difference, and elimination
  of end cores.'
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Два изомера трёх шестиугольников|Два изомера трёх шестиугольников]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

Two chains of three hexagons can have the same ordinary forest coefficients, spanning-tree count, and resistance radius, yet different Laplacian spectra. Such a pair is specified in [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. Here we compute both characteristic polynomials, explain the first difference between their coefficients, and derive a compact difference formula:

$$
\chi_{\mathrm A}(\xi)-\chi_{\text{B}}(\xi)
=\xi^2(\xi^2-5\xi+5)^4
=\chi_{C_5}(\xi)^2
$$

The question is not only whether the spectra differ. We want to understand which information about seam positions is lost in the matroid parameters and reappears in the rooted forest coefficients.

Prerequisites: [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]] explains the equality of ordinary forest data; [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] connects rooted forests with the spectrum; [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]] introduces the spectral Schur complement. The necessary conventions are recalled below.

> [!note] Origins of the results
> The matrix-forest formula is a classical result of Chebotarev and Shamis [1]. Eliminating internal vertices uses the standard Schur complement. The polynomials of the specified pair are computed directly and independently checked by forest enumeration; their difference formula is derived below. This derivation does not establish scientific priority. Comparison with the known spectrum of a linear hexagonal chain appears in [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons#Connection with classical spectral theory|Connection with classical spectral theory]].

## Two configurations of one chain

Write $N$ for the number of cores and $n$ for the number of vertices of the resulting graph. In this note, $N=3$. All graphs are undirected, and all conductances are one.

> [!info] The specified pair of graphs
> **Definition.** Let $C(v_0,\ldots,v_5)$ denote the cycle in the stated order, including the closing edge $v_5v_0$. Take
>
> $$
> \begin{aligned}
> K_1&=C(0,1,9,8,7,6),\\
> K_2&=C(0,1,2,3,4,5),\\
> K_3^{\mathrm A}&=C(3,4,13,12,11,10),\\
> K_3^{\text{B}}&=C(2,3,13,12,11,10)
> \end{aligned}
> \tag{1}
> $$
>
> Graph A is the union of $K_1,K_2,K_3^{\mathrm A}$, and graph B the union of $K_1,K_2,K_3^{\text{B}}$. Edges are combined as sets: each shared edge is counted once. There are no other identifications.

The input seam of the middle core is $01$. Its output seam is $34$ in A and $23$ in B. Each seam has two vertices and one edge; the input and output are disjoint. Both assemblies are therefore admissible in the sense of [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains#Admissible open chains of cycles|Admissible open chains of cycles]], and

$$
n=3\cdot6-2\cdot2=14,\qquad |E|=3\cdot6-2=16
$$

![Seam positions and induced subgraphs on degree-three vertices](Seams%20and%20Degree-Three%20Vertices.svg)

**One core scheme, two graphs.** The seam $01$ is red; the other seam is blue. The highlighted vertices have degree $3$. Their induced subgraph consists of two separate edges in A and a three-edge path in B. The layouts depict abstract graphs and are not resistance embeddings.

> [!info] Nonisomorphism and equal parameters
> **Proposition.** Graphs A and B are nonisomorphic but have isomorphic cycle matroids. In particular, their ordinary forest polynomials agree, and
>
> $$
> \tau_{\mathrm A}=\tau_{\text{B}}=204,\qquad
> \rho_{\mathrm A}=\rho_{\text{B}}=\frac{43595}{41616}
> \tag{2}
> $$
>
> Here $\rho$ is the resistance radius in the PMG normalization: the square of the Euclidean circumradius of the resistance simplex. The matroid statement and its conditions are proved in [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]].

> [!note]- Nonisomorphism and numerical checks
> **Proof.** An isomorphism preserves degrees and the number of edges between vertices of degree $3$. The figure gives $2$ and $3$, so no isomorphism exists. The spanning-tree count is independently obtained as the determinant of any reduced Laplacian. With reference vertex $13$, set $\mathbf A=\mathbf L_{\widehat{13},\widehat{13}}$ and $\mathbf d=\operatorname{diag}(\mathbf A^{-1})$. The formula in [[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance#The radius as Laplacian energy|The radius as Laplacian energy]] gives
>
> $$
> \tau=\det\mathbf A=204,\qquad
> \rho=\frac14\mathbf d^{\mathsf T}\mathbf A\mathbf d
> =\frac{43595}{41616}
> $$
>
> Both values are obtained for each graph from its own matrix in exact rational arithmetic. $\square$

## Laplacians and three different polynomials

With vertices ordered as $0,1,\ldots,13$, the common part of the edge lists is

$$
\begin{aligned}
E_* = \{&(0,1),(0,5),(0,6),(1,2),(1,9),\\
&(2,3),(3,4),(4,5),(6,7),(7,8),(8,9),\\
&(10,11),(11,12),(12,13)\}
\end{aligned}
$$

The complete lists are

$$
\begin{aligned}
E_{\mathrm A}&=E_*\cup\{(3,10),(4,13)\},\\
E_{\text{B}}&=E_*\cup\{(2,10),(3,13)\}
\end{aligned}
$$

These lists specify the Laplacians completely through the rule

$$
L_{ij}=\begin{cases}
\deg(i),&i=j,\\
-1,&\{i,j\}\in E,\\
0,&\text{otherwise}
\end{cases}
$$

Their diagonals are, respectively,

$$
\begin{aligned}
\operatorname{diag}\mathbf L_{\mathrm A}
&=(3,3,2,3,3,2,2,2,2,2,2,2,2,2),\\
\operatorname{diag}\mathbf L_{\text{B}}
&=(3,3,3,3,2,2,2,2,2,2,2,2,2,2)
\end{aligned}
$$

The spectrum belongs to the ordinary Laplacian operator on the vertex coordinate space. We distinguish the matrix $\mathbf L$ from the form $L=\sum_{\{i,j\}\in E}[a_{ij}]^2$ and its resistance evaluation; these correspondences are discussed in [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]].

For a spanning forest $T$ with $g$ edges, let $\operatorname{Comp}(T)$ be its set of components, including isolated vertices. The ordinary and rooted coefficients are

$$
\begin{aligned}
f_g(G)&=\sum_{\substack{T\text{ is a forest}\\|E(T)|=g}}1,\\
p_g(G)&=\sum_{\substack{T\text{ is a forest}\\|E(T)|=g}}
\prod_{C\in\operatorname{Comp}(T)}|V(C)|
\end{aligned}
$$

In the second case, one root is selected in each component. The matrix-forest theorem of Chebotarev and Shamis [1, Theorem 5, applied to conductances multiplied by $t$] gives

$$
\begin{aligned}
F_G(t)&=\sum_{g=0}^{13}f_g(G)t^g,\\
P_G(t)&=\sum_{g=0}^{13}p_g(G)t^g
=\det(\mathbf I_{14}+t\mathbf L_G),\\
\chi_G(\xi)&=\det(\xi\mathbf I_{14}-\mathbf L_G)
=\xi^{14}P_G(-1/\xi)
\end{aligned}
\tag{3}
$$

The last equality is a polynomial identity, including at $\xi=0$. The ordinary polynomial $F_G$, rooted polynomial $P_G$, and characteristic polynomial $\chi_G$ have different meanings. In polyform language, $p_g$ is the coordinate evaluation of grade $L^g/g!$, as in [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]]; equality of ordinary coefficients does not imply equality of this evaluation.

## Exact characteristic polynomials

> [!example] Direct calculation from the Laplacians
> **Computed directly.** For the graphs in (1), we obtain
>
> $$
> \begin{aligned}
> \chi_{\mathrm A}(\xi)={}&\xi^{14}-32\xi^{13}+458\xi^{12}-{}\\
> &-3872\xi^{11}+21509\xi^{10}-82624\xi^9+{}\\
> &+224918\xi^8-437304\xi^7+603954\xi^6-{}\\
> &-581144\xi^5+375104\xi^4-151536\xi^3+{}\\
> &+33425\xi^2-2856\xi
> \end{aligned}
> \tag{4}
> $$
>
> $$
> \begin{aligned}
> \chi_{\text{B}}(\xi)={}&\xi^{14}-32\xi^{13}+458\xi^{12}-{}\\
> &-3872\xi^{11}+21508\xi^{10}-82604\xi^9+{}\\
> &+224748\xi^8-436504\xi^7+601679\xi^6-{}\\
> &-577144\xi^5+370854\xi^4-149036\xi^3+{}\\
> &+32800\xi^2-2856\xi
> \end{aligned}
> \tag{5}
> $$

The factorizations into irreducible factors over $\mathbb Q$ are

$$
\begin{aligned}
\chi_{\mathrm A}(\xi)={}&\xi
(\xi^3-9\xi^2+24\xi-17)\cdot{}\\
&\cdot(\xi^3-7\xi^2+14\xi-7)\cdot{}\\
&\cdot(\xi^3-5\xi^2+6\xi-1)\cdot{}\\
&\cdot(\xi^4-11\xi^3+40\xi^2-55\xi+24)
\end{aligned}
\tag{6}
$$

$$
\begin{aligned}
\chi_{\text{B}}(\xi)={}&\xi(\xi-1)(\xi-3)
(\xi^2-6\xi+7)\cdot{}\\
&\cdot(\xi^2-4\xi+2)\,q_7(\xi),\\
q_7(\xi)={}&\xi^7-18\xi^6+130\xi^5-482\xi^4+{}\\
&+971\xi^3-1028\xi^2+496\xi-68
\end{aligned}
\tag{7}
$$

> [!info] A compact spectral difference
> **Proposition.** For the specified pair,
>
> $$
> \boxed{\chi_{\mathrm A}(\xi)-\chi_{\text{B}}(\xi)
> =\xi^2(\xi^2-5\xi+5)^4=\chi_{C_5}(\xi)^2}
> \tag{8}
> $$

Subtracting (5) from (4) directly verifies (8). The origin of the square is established in [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons#Eliminating the end cores and the squared difference|Eliminating the end cores and the squared difference]].

The coefficients of $\xi^{14},\xi^{13},\xi^{12},\xi^{11}$ agree. **The first difference in descending degree occurs at $\xi^{10}$**, that is, in $p_4$. Every coefficient from degree $10$ down to $2$ differs. The coefficients of $\xi$ agree and equal $-n\tau=-2856$; the constant terms are zero.

Moreover, $\gcd(\chi_{\mathrm A},\chi_{\text{B}})=\xi$: there are no shared nonzero eigenvalues. The factor $\chi_{C_5}^2$ belongs to the **difference**, not to both graph polynomials.

## The first difference in rooted forests

Substituting (3) into (8) gives

$$
\boxed{P_{\mathrm A}(t)-P_{\text{B}}(t)
=t^4(1+5t+5t^2)^4}
\tag{9}
$$

Thus $p_0,p_1,p_2,p_3,p_{13}$ agree, whereas $p_g(\mathrm A)>p_g(\text{B})$ for $4\le g\le12$. In particular,

$$
p_4(\mathrm A)=21509,\qquad p_4(\text{B})=21508
$$

The shortest cycle in either graph has length $6$, so every four-edge subset is a forest and $f_4=\binom{16}{4}=1820$. However, these forests have different distributions of component sizes.

![Component types of a four-edge forest and numbers of root choices](Root%20Weights%20of%20Four-Edge%20Forests.svg)

**From ordinary to rooted forests.** The figure shows representatives of the five types of non-singleton component sizes. Any vertex of a component can serve as its root; the numbers of choices multiply. Isolated vertices bring the total to $14$ and contribute a factor of $1$. The shape of a tree within a component does not affect this factor.

| Non-singleton component sizes | Forests in A | Forests in B | Root choices |
|---|---:|---:|---:|
| $5$ | 56 | 60 | 5 |
| $4,2$ | 314 | 317 | 8 |
| $3,3$ | 133 | 128 | 9 |
| $3,2,2$ | 888 | 880 | 12 |
| $2,2,2,2$ | 429 | 435 | 16 |

The ordinary sums of both columns are $1820$, whereas the difference of the rooted sums is

$$
-4\cdot5-3\cdot8+5\cdot9+8\cdot12-6\cdot16=1
$$

The matroid preserves the number of independent edge sets of each size. In general, it does not preserve the sizes of their vertex components. This is why equality of $F_G$ is compatible with different $P_G$ and spectra.

### The same difference through spectral moments

Write $s_j=\operatorname{tr}\mathbf L^j$. These are spectral power sums, not ordinary forest power parameters. Here

$$
\begin{aligned}
s_1&=32,\qquad s_2=108,\qquad s_3=416,\\
s_4(\mathrm A)&=1716,\qquad s_4(\text{B})=1720
\end{aligned}
$$

The fourth-moment difference is explained by adjacency between vertices of different degrees. For a graph without triangles or four-cycles,

$$
\begin{aligned}
\operatorname{tr}\mathbf L^4
={}&\sum_v(d_v^4+4d_v^3+2d_v^2)+{}\\
&+4\sum_{\{u,v\}\in E}d_ud_v-2|E|
\end{aligned}
\tag{10}
$$

> [!note]- Derivation of the moment formula
> **Proof.** Let $\mathbf D$ be the degree diagonal and $\mathbf A$ the adjacency matrix. In the trace expansion of $(\mathbf D-\mathbf A)^4$, cyclically equivalent words can be grouped:
>
> $$
> \begin{aligned}
> \operatorname{tr}\mathbf L^4={}&\operatorname{tr}\mathbf D^4
> +4\operatorname{tr}(\mathbf D^2\mathbf A^2)+{}\\
> &+2\operatorname{tr}(\mathbf D\mathbf A\mathbf D\mathbf A)-{}\\
> &-4\operatorname{tr}(\mathbf D\mathbf A^3)
> +\operatorname{tr}\mathbf A^4
> \end{aligned}
> $$
>
> Terms containing one $\mathbf A$ vanish. Next, $\operatorname{tr}(\mathbf D^2\mathbf A^2)=\sum_vd_v^3$ and $\operatorname{tr}(\mathbf D\mathbf A\mathbf D\mathbf A)=2\sum_{uv\in E}d_ud_v$. The absence of triangles makes $\operatorname{tr}(\mathbf D\mathbf A^3)$ zero. With no four-cycles, closed walks of length four give $\operatorname{tr}\mathbf A^4=2\sum_vd_v^2-2|E|$. This yields (10). $\square$

The degree sequences agree, but the edge sums are $90$ in A and $91$ in B. The fourth-moment difference is therefore $-4$. Newton's identity

$$
4p_4=p_3s_1-p_2s_2+p_1s_3-s_4
$$

again yields $p_4(\mathrm A)-p_4(\text{B})=1$.

## Eliminating the end cores and the squared difference

We derive (8) without expanding a determinant of size $14\times14$. Use the Schur complement of the spectral pencil from [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data#The Schur complement and Jacobi's identity|The Schur complement and Jacobi's identity]]. Set

$$
y=\xi-2,\qquad k=y^4-3y^2+1,\qquad \ell=y^3-2y
$$

The four vertices of an end core outside its seam form the internal block

$$
\mathbf T_4=
\begin{pmatrix}
y&1&0&0\\
1&y&1&0\\
0&1&y&1\\
0&0&1&y
\end{pmatrix},\qquad \det\mathbf T_4=k
$$

Its diagonal retains the original degrees $2$: this is a principal block of the pencil, not the characteristic matrix of a separate path with recalculated endpoint degrees. When $k\ne0$, the endpoint entries of its inverse are

$$
(\mathbf T_4^{-1})_{11}=(\mathbf T_4^{-1})_{44}=\frac\ell k,
\qquad (\mathbf T_4^{-1})_{14}=-\frac1k
$$

After eliminating this block, the diagonal at each seam endpoint becomes $d$, and the off-diagonal entry between them becomes $w$:

$$
d=y-1-\frac\ell k,\qquad w=1+\frac1k
\tag{11}
$$

The term $y-1=\xi-3$ accounts for the seam vertex's degree $3$. The one in $w$ represents the single original seam edge, while $1/k$ is the correction from the eliminated path. No second copy of the shared edge is added.

![Eliminating the end cores and the two pencils on the middle hexagon](Eliminating%20the%20End%20Cores.svg)

**Two identical eliminated blocks, two seam positions.** Each end block contributes a factor $k$ to the determinant. On the six remaining vertices, seam endpoints have diagonal entries $d$ and the other vertices $y$; seam entries are $w$, and other edge entries $1$. These are spectral matrices depending on $\xi$, not Laplacians of new unit-weight graphs.

In the order $0,\ldots,5$, the remaining matrices are

$$
\mathbf H_{\mathrm A}=
\begin{pmatrix}
d&w&0&0&0&1\\
w&d&1&0&0&0\\
0&1&y&1&0&0\\
0&0&1&d&w&0\\
0&0&0&w&d&1\\
1&0&0&0&1&y
\end{pmatrix}
\tag{12a}
$$

$$
\mathbf H_{\text{B}}=
\begin{pmatrix}
d&w&0&0&0&1\\
w&d&1&0&0&0\\
0&1&d&w&0&0\\
0&0&w&d&1&0\\
0&0&0&1&y&1\\
1&0&0&0&1&y
\end{pmatrix}
\tag{12b}
$$

For $k\ne0$, block elimination gives $\chi_G=k^2\det\mathbf H_G$.

> [!info] Difference of the two reduced determinants
> **Lemma.** For the matrices (12a), (12b), with independent $y,d,w$,
>
> $$
> \det\mathbf H_{\mathrm A}-\det\mathbf H_{\text{B}}
> =(-d^2+dy+w^2-1)^2
> \tag{13}
> $$

> [!note]- Proof of the lemma
> **Proof.** Write $\eta=d^2-w^2$. Expanding the determinants (12a), (12b) and grouping by $\eta$ gives
>
> $$
> \begin{aligned}
> \det\mathbf H_{\mathrm A}&=\eta(\eta y^2-4dy+4),\\
> \det\mathbf H_{\text{B}}&=\eta^2y^2-(\eta+dy-1)^2
> \end{aligned}
> $$
>
> Their difference is $(\eta+dy-1)^2-4\eta dy+4\eta=(\eta-dy+1)^2$. Substitution of $\eta=d^2-w^2$ yields (13). This is a polynomial identity in three independent variables. $\square$

> [!note]- Derivation of the spectral difference formula
> **Proof.** The continuants satisfy $\ell^2-yk\ell+k^2=1$, also verified by substituting their explicit expressions. Using (11), we obtain
>
> $$
> \begin{aligned}
> k(-d^2+dy+w^2-1)&=yk-2\ell+2\\
> &=(y+2)(y^2-y-1)^2\\
> &=\xi(\xi^2-5\xi+5)^2
> \end{aligned}
> $$
>
> Multiplying (13) by $k^2$ proves (8) for $k\ne0$. Both sides of (8) are polynomials, so the equality holds for every $\xi$, including zeros of $k$. Finally, $\chi_{C_5}(\xi)=\xi(\xi^2-5\xi+5)^2$, as follows from the cycle spectrum or its direct determinant. $\square$

The square already appears in the difference of the two reduced determinants. The factor $\chi_{C_5}$ comes from the particular expression $k(-d^2+dy+w^2-1)$ for an end hexagon. This explanation does not assume a subgraph $C_5$: both original graphs are bipartite and contain no odd cycles.

## Rooted forest counts and the Kirchhoff index

In general, $P_G(1)=(-1)^n\chi_G(-1)$. Here $n=14$ is even, so

$$
\begin{aligned}
P_{\mathrm A}(1)&=2518737,\\
P_{\text{B}}(1)&=2504096,\\
P_{\mathrm A}(1)-P_{\text{B}}(1)&=14641=11^4
\end{aligned}
$$

This single number already distinguishes the specified pair. The example does not establish the same conclusion for the entire chain family.

For a connected graph, the Kirchhoff index $\operatorname{Kf}(G)=\sum_{i<j}R_{ij}$ is expressed through rooted coefficients as $\operatorname{Kf}=np_{n-2}/p_{n-1}$; see [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]]. Hence

$$
\begin{aligned}
\operatorname{Kf}(\mathrm A)&=\frac{33425}{204},\\
\operatorname{Kf}(\text{B})&=\frac{32800}{204},\\
\operatorname{Kf}(\mathrm A)-\operatorname{Kf}(\text{B})&=\frac{625}{204}
\end{aligned}
$$

Equality of resistance radii does not imply equality of the sum of pairwise resistances or of the full resistance geometry.

## Connection with classical spectral theory

For a linear hexagonal chain of $N$ cores, Yang and Zhang [2, the Laplacian spectrum decomposition, also stated in the abstract] separate the spectrum of the path $P_{2N+1}$ and that of an additional symmetric tridiagonal matrix. In our case $N=3$, and the two cubic factors in (6), together with $\xi$, give

$$
\chi_{P_7}(\xi)=\xi(\xi^3-7\xi^2+14\xi-7)
(\xi^3-5\xi^2+6\xi-1)
$$

Thus the factorization for the straight configuration agrees with the known structure of its spectrum. The bent configuration has a different factorization. The matrix-forest theorem, spectral moments, continuants, and the Schur complement provide consistent ways to study this pair; the polyform expression connects them with the exponential's grades while preserving the distinction between ordinary and rooted forest evaluations.

## Checks and continuation

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_three_hexagons.py) reconstructs the graphs from the cycles in (1). For each graph, it independently performs:

1. Computation of $\det(\xi\mathbf I-\mathbf L)$ and its factorization in exact arithmetic.
2. Enumeration of all $2^{16}=65536$ edge subsets: cyclic sets are discarded, ordinary forests receive weight $1$, and rooted forests weight $\prod_C|V(C)|$.
3. Comparison of all coefficients, four-edge forest types, and values of $P_G(1)$.
4. Verification of $\tau$, the radius by two rational formulas, the Kirchhoff index, and the first four spectral moments.
5. Symbolic verification of end-block elimination, identity (13), and reconstruction of each full polynomial from $k^2\det\mathbf H_G$.

The [calculation results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/three-hexagons-results.json) retain complete matrices, edges, coefficients, and reference values. The [reproduction instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) include generation of all three figures. Forest enumeration uses neither transfer matrices nor the proposed difference formula.

For this pair, we have established different spectra with equal matroid parameters, explained the first difference in $p_4$, and derived the full difference (8). Sequential computation and closure on five coordinates are proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]]. A further question is the distinguishability of longer chains. Sufficiency of a fixed-pair passport, closure of transfer, and recovery of a configuration from one scalar polynomial are different statements; this note does not replace their proofs.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

## Sources

1. P. Chebotarev, E. Shamis. *Matrix-Forest Theorems*. [arXiv:math/0602575, Theorem 5](https://arxiv.org/abs/math/0602575). The determinant $\mathbf I+\mathbf L$ and rooted spanning forests; the weighted version gives the generating polynomial.
2. Y. Yang, H. Zhang. *Kirchhoff index of linear hexagonal chains*. International Journal of Quantum Chemistry **108** (2008), 503-512. [DOI: 10.1002/qua.21537](https://onlinelibrary.wiley.com/doi/10.1002/qua.21537). The Laplacian spectrum decomposition for a linear chain, also stated in the article's abstract.

Supporting library notes: [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]], [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]], [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]].
