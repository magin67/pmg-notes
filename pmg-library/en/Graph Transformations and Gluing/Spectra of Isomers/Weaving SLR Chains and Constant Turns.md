---
title: Weaving SLR Chains and Constant Turns
date: '2026-11-02'
updated: 2026-11-02
revision: 2
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: weaving-slr-chains-and-constant-turn
order: 7
description: Path runners, plugs and sockets, constant SLR turns without a planarity requirement, and exact spectral recurrences.
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Плетение SLR-цепочек и постоянный поворот|Плетение SLR-цепочек и постоянный поворот]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

A hexagonal chain can be grown using the same component: a path of five edges. Its endpoints form the plug, and a chosen internal edge is the socket for the next step. Three socket positions correspond to S, L, and R. Repeating one marked runner gives a constant turn; repeating a block of runners gives a periodic SLR code.

There is no planarity requirement. A spatial spiral provides an illustration of a chain with a repeated turn. The definition uses vertices, edges, and the matching of contacts; lengths, angles, and spatial positions of cells are not part of it. Any finite sequence of steps can be continued by adding new vertices. Closing the ends is a separate operation.

> [!note] The result in plain language
> Three things must be fixed for the repeated component: which contacts attach to the existing graph, where the next component attaches, and which contact is matched to which. The graph and its boundary data then grow by one fixed rule.
>
> Straight chains and chains with constant turns have the same spanning-tree recurrence. Their spectral recurrences differ. To compute the characteristic polynomial of the next chain, a few preceding polynomials suffice: four for a straight chain, and five for constant L or R, when the recurrence is linear and homogeneous. All these statements concern abstract graphs and require no planar layout.

The runner is defined in [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]], the factorization law in [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]], and the letter and orientation conventions in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]. Here we establish their precise correspondence and derive recurrences for the constant families.

## One path and three marked runners

All conductances are one. The starting graph $G_0$ is an edge with ordered socket $(a,b)$. The runner $K$ has six vertices and five edges:

$$
K=P_6:\quad 1-2-3-4-5-0
$$

Its plug is $\mathcal P=(1,0)$. At each attachment, identify $1\mapsto a$ and $0\mapsto b$. The other four vertices are new. The old edge $ab$ and the five path edges form a cycle $C(0,1,2,3,4,5)$. The runner contains no copy of the edge $01$, so each seam is counted once.

| Letter $\alpha$ | Ordered socket $\mathcal Q_\alpha$ | Position relative to the input edge $01$ |
|---|---|---|
| L | $(2,3)$ | One side output |
| S | $(3,4)$ | The opposite edge |
| R | $(4,5)$ | The other side output |

All three outputs are vertex-disjoint from the plug. Thus repetition of the runner introduces no common vertices between nonadjacent cores, and the two seams within an intermediate core remain disjoint. This is exactly the class of open chains in [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]].

![A path of five edges, an ordered plug, and three socket positions](Three%20SLR%20Runners.svg)

The dashed edge in the figure already belongs to the assembled graph. The blue edges are added; the colored output arrow shows the contact order. The plug and socket are vertex markings, not additional connections.

> [!info] Correspondence between weaving and the code
> **Proposition 1.** After $N$ runner attachments with outputs $\alpha_1,\ldots,\alpha_N$, the graph has
>
> $$
> n=4N+2,\qquad |E|=5N+1
> $$
>
> For $N\ge2$, its full SLR code under the library conventions is
>
> $$
> w=S\alpha_2\cdots\alpha_{N-1}
> \tag{1}
> $$
>
> The letter $\alpha_1$ selects the output of the first core; all such marked single cycles are isomorphic. The letter $\alpha_N$ selects the terminal boundary and does not change the graph already constructed. The initial S in (1) is a marker, not an additional step.

> [!note]- Proof of the correspondence
> **Proof.** Every step adds four vertices and five edges, giving the count. In the new cycle the input is at $01$, with $0$ identified with the second old contact and $1$ with the first. This is the SLR transfer rule. For every intermediate core, the output choice is exactly its letter. The first core has no input from another core, and the last has no used output. Any ordered pair of adjacent vertices of the first $C_6$ can be mapped to any other by a cycle automorphism. The internal letters therefore have the form (1). $\square$

## Constant turns and spatial chains

> [!info] A constant SLR turn
> **Definition.** A chain has constant SLR turn $\alpha\in\{S,L,R\}$ if all its internal letters equal $\alpha$. Denote the corresponding family by $G_N^{\alpha}$. It is constructed by repeating a single marked runner $K_\alpha$:
>
> $$
> w_N=S\alpha^{N-2},\qquad N\ge2
> \tag{2}
> $$

Here “turn” means the relative position of two seams in a core, taking contact order into account. In a local planar drawing with regular hexagons, the letters S, L, R correspond to angles $0,+\pi/3,-\pi/3$. These angles help read the code but do not require the entire chain to lie in one plane.

![A straight chain, alternating turns, and a spatial spiral with constant letter L](A%20Straight%20Chain%20Zigzag%20and%20Spiral.svg)

The lower part of the figure joins six-edge cycles in sequence with a constant L choice. Adjacent cycles share an edge; the viewpoint shows their spatial arrangement. A crossing of projected lines creates no vertex. Geometric coordinates serve only to draw the graph.

“Constant curvature” can be understood as a visual name for a constant local rule. Numerical Euclidean curvature and torsion of a spatial curve require a separately specified embedding; the SLR code does not determine them. Likewise, a spatial spiral need not be the only realization of a given graph.

Reflection exchanges L and R and preserves S. Thus $G_N^L$ and $G_N^R$ are isomorphic as unmarked graphs and have the same characteristic polynomials. Comparing marked states also requires exchanging the terminal contacts.

Closure requires an additional identification of the initial and terminal boundaries with a specified matching. It does not follow from repetition of a letter or from the shape of a drawing; the corresponding operations are discussed in [[en/Graph Transformations and Gluing/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain: Rings and the Möbius Effect]].

## Why the contact matching changes the family

The socket position alone does not determine the SLR turn. If $0\mapsto a$ and $1\mapsto b$ are used at every step instead of $1\mapsto a$ and $0\mapsto b$, the local cycle order relative to the continuation changes. For a fixed side output, this produces alternating L and R, up to a global reflection.

![Two fixed contact matchings produce constant and alternating turns](Contact%20Matching%20and%20the%20SLR%20Turn.svg)

Both rules are fixed weaving constructions. They use the same unmarked path but different marked runners. The distinction is already visible with four cores:

$$
P_{SLL}(1)=220348791,\qquad P_{SLR}(1)=220480560
\tag{3}
$$

Here $P_G(t)=\det(\mathbf I+t\mathbf L_G)$ is the rooted forest polynomial. In both cases, $\tau=1189$. Equality of spanning-tree counts cannot detect an error in the contact matching.

The algebraic explanation uses the permutation

$$
\mathbf J(A,B,C,D,E)^{\mathsf T}=(A,C,B,D,E)^{\mathsf T}
$$

Let $\mathbf T_j$ be the matrix in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]] for input $0\mapsto a$, $1\mapsto b$ and output $(j,j+1)$. The correct SLR matrices are then

$$
\mathbf U_L=\mathbf T_2\mathbf J,\qquad
\mathbf U_S=\mathbf T_3\mathbf J,\qquad
\mathbf U_R=\mathbf T_4\mathbf J
\tag{4}
$$

Using $\mathbf U_R=\mathbf J\mathbf U_L\mathbf J$, we obtain

$$
\mathbf T_2^2=\mathbf U_L\mathbf U_R
\tag{5}
$$

On the right, R acts first and L second. Thus two steps with the other fixed matching are equivalent to two alternating SLR steps. The terminal marking may differ; for the unmarked graph, the overall choice of reflected representative is immaterial.

## Repetition of the factor and the growth operator

For the Laplacian polyform $L_G$, write $M_G(t)=\exp(tL_G)$. This is the exponential in polyform algebra, with its commutative product. For the runner,

$$
M_K(t)=\prod_{uv\in E(K)}\bigl(e+t[a_v-a_u]^2\bigr)
$$

If $\iota_\alpha$ embeds the old part and $\jmath_\alpha$ embeds the new path copy into the graph after attachment, then

$$
M_{G_{N+1}^{\alpha}}(t)=
\iota_\alpha\bigl(M_{G_N^{\alpha}}(t)\bigr)\,
\jmath_\alpha\bigl(M_K(t)\bigr)
\tag{6}
$$

The embeddings account for shared contacts and fresh names for the other vertices. Law (6) follows from addition of the Laplacians of parts with disjoint edge sets; its proof and graded convolution are given in [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]].

Fix a relabeling rule that returns the new socket to two standard names while keeping all other vertices distinct. The right-hand side of (6) then defines one growth operator $\mathcal W_{\alpha,t}$ on polyforms with a marked pair. For the starting edge $M_0(t)=e+t[b-a]^2$,

$$
M_{G_N^{\alpha}}(t)=\mathcal W_{\alpha,t}^{\,N}\bigl(M_0(t)\bigr)
\tag{7}
$$

The power means composition of attachment and relabeling operations. An ordinary power $M_K(t)^N$ on a fixed vertex set would give $\exp(NtL_K)$, changing conductances. New vertices are created by the growth operator itself.

## Five coordinates and a power of one matrix

Set $\mathbf H_G(\xi)=\xi\mathbf I_n-\mathbf L_G$. For the current ordered socket $(a,b)$, use the state

$$
\boldsymbol s_G=
\begin{pmatrix}A\\B\\C\\D\\E\end{pmatrix}
=\begin{pmatrix}
\det\mathbf H_G\\
\det(\mathbf H_G)_{\widehat a,\widehat a}\\
\det(\mathbf H_G)_{\widehat b,\widehat b}\\
(\operatorname{adj}\mathbf H_G)_{ab}\\
\det(\mathbf H_G)_{\widehat{a,b},\widehat{a,b}}
\end{pmatrix}
\tag{8}
$$

The minors retain the vertex degrees of the original graph. They cannot be replaced by Laplacians of induced subgraphs. The empty determinant equals $1$.

> [!info] Constant spectral transfer
> **Proposition 2.** For the boundary selected by the runner itself,
>
> $$
> \boldsymbol s_N^{\alpha}=\mathbf U_\alpha^{\,N}\boldsymbol s_0,
> \qquad
> \boldsymbol s_0=(\xi(\xi-2),\xi-1,\xi-1,-1,1)^{\mathsf T}
> \tag{9}
> $$
>
> The first coordinate is $\chi_N^\alpha(\xi)=\det(\xi\mathbf I_{4N+2}-\mathbf L_{G_N^\alpha})$. For all three letters, $\mathbf U_\alpha\boldsymbol s_0=\boldsymbol s_1$, where $\boldsymbol s_1$ is the state of a single $C_6$.

> [!note]- Proof and the terminal boundary
> **Proof.** The edge state is computed from the matrix with diagonal $\xi-1$ and off-diagonal entries $1$, giving $\boldsymbol s_0$. The theorem on transfer to a new two-vertex boundary in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]] applies to the path with disjoint edges. Permuting the input gives (4). Induction proves (9). After the first step, all ordered edges of the cycle are equivalent, so $\boldsymbol s_1$ is independent of the letter.
>
> In [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], the terminal boundary is chosen opposite the input of the last core. For that boundary, when $N\ge2$, the state is $\mathbf U_S\mathbf U_\alpha^{N-2}\boldsymbol s_1$. In (9), the output of the last core is $\mathcal Q_\alpha$. The full states may differ, but the first rows of all $\mathbf U_\alpha$ are identical, so the characteristic polynomials coincide. $\square$

For reproducibility of the calculations below, we give a compact description of the matrix actions. Introduce

$$
y=\xi-2,\quad m=y^2-1,\quad \ell=y^3-2y,\quad k=y^4-3y^2+1
$$

For $\boldsymbol s=(A,B,C,D,E)^{\mathsf T}$, set

$$
\begin{aligned}
A'&=kA-(k+\ell)(B+C)+2D+(k+2\ell+m)E\\
\phi&=ymA-(y+1)m(B+C)+(y+1)(m+y)E\\
E_L&=mA-mB-(m+y)C+(m+y)E\\
E_S&=y^2A-y(y+1)(B+C)+(y+1)^2E
\end{aligned}
$$

Then

$$
\mathbf U_L\boldsymbol s=
\begin{pmatrix}
A'\\
\ell A-\ell B-(\ell+m)C+(\ell+m)E\\
\phi-C\\D-E_L\\E_L
\end{pmatrix},\qquad
\mathbf U_S\boldsymbol s=
\begin{pmatrix}
A'\\\phi-C\\\phi-B\\D-E_S\\E_S
\end{pmatrix}
\tag{10}
$$

The third matrix is determined by reflection $\mathbf U_R=\mathbf J\mathbf U_L\mathbf J$. Formulas (10) follow by expanding boundary determinants as in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], with a permutation of input coordinates. In particular, $\mathbf J\boldsymbol s_0=\boldsymbol s_0$ and $\boldsymbol s_N^R=\mathbf J\boldsymbol s_N^L$.

## Spectral recurrences for the constant families

Here $N$ is the number of cores, while $q$ is an auxiliary variable in the characteristic polynomial of the transfer matrix. It differs from the graph spectral parameter $\xi$.

Introduce two polynomials of degree four in $q$:

$$
Q_\alpha(q)=q^4-a_\alpha q^3+b_\alpha q^2-a_\alpha q+1,
\qquad \alpha\in\{S,L\}
\tag{11}
$$

Their coefficients are

$$
\begin{aligned}
a_S&=(\xi^2-6\xi+6)(\xi^2-4\xi+2)\\
b_S&=2(\xi-1)(\xi^3-9\xi^2+25\xi-19)\\
a_L&=(\xi-3)(\xi-2)(\xi^2-5\xi+2)\\
b_L&=\xi^6-14\xi^5+75\xi^4-192\xi^3+{}\\
&\quad{}+242\xi^2-144\xi+38
\end{aligned}
\tag{12}
$$

> [!info] Recurrences for characteristic polynomials
> **Theorem 1.** For every $N\ge0$,
>
> $$
> \chi_{N+4}^{\alpha}-a_\alpha\chi_{N+3}^{\alpha}
> +b_\alpha\chi_{N+2}^{\alpha}-a_\alpha\chi_{N+1}^{\alpha}
> +\chi_N^{\alpha}=r_\alpha
> \tag{13}
> $$
>
> where $r_S=0$ and $r_L=-2\xi^2(\xi-3)^2$. The formula for R is the same as for L. Here $G_0$ is the starting edge.
>
> The minimal order of a homogeneous linear recurrence over $\mathbb Q(\xi)$, with coefficients independent of $N$, is $4$ for S and $5$ for L and R.

> [!note]- Proof of the recurrences
> **Proof.** Substituting (10) gives the exact polynomial identities
>
> $$
> \det(q\mathbf I_5-\mathbf U_\alpha)=(q-1)Q_\alpha(q),
> \qquad \det\mathbf U_\alpha=1
> $$
>
> In addition,
>
> $$
> Q_S(\mathbf U_S)\boldsymbol s_0=0,\qquad
> Q_L(\mathbf U_L)\boldsymbol s_0=\boldsymbol v,\qquad
> \mathbf U_L\boldsymbol v=\boldsymbol v
> $$
>
> where
>
> $$
> \boldsymbol v=
> \begin{pmatrix}
> -2\xi^2(\xi-3)^2\\
> 2\xi(\xi-3)\\
> -2\xi(\xi-3)^2(\xi-1)\\
> \xi(\xi-3)(\xi^3-7\xi^2+12\xi-2)\\
> 0
> \end{pmatrix}
> $$
>
> These equalities are checked by multiplication of explicitly specified matrices and vectors, so they are identities for every $\xi$. Multiplying them by $\mathbf U_\alpha^N$ and taking the first coordinate gives (13). Subtracting (13) for consecutive $N$ gives a homogeneous recurrence of order five for L. Reflection transfers the result to R. $\square$

Four initial polynomials are needed to start (13) uniquely. They are

$$
\begin{aligned}
\chi_0&=\xi(\xi-2)\\
\chi_1&=\xi(\xi-4)(\xi-3)^2(\xi-1)^2\\
\chi_2&=(\mathbf U_S\boldsymbol s_1)_1\\
\chi_3^\alpha&=(\mathbf U_S\mathbf U_\alpha\boldsymbol s_1)_1
\end{aligned}
\tag{14}
$$

The subscript $1$ denotes the first coordinate; $\boldsymbol s_1=\mathbf U_S\boldsymbol s_0$ is computed explicitly from (10). Thus (14) requires no new definition of the graph. The fully expanded initial polynomials are given in the exact results file. For three cores, $\chi_3^S$ and $\chi_3^L$ coincide with polynomials A and B in [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]].

## Numerical specialization and minimality

The number of vertices $n=4N+2$ is even. Hence at $\xi=-1$,

$$
c_N^\alpha:=P_{G_N^\alpha}(1)=\chi_N^\alpha(-1)
$$

For the general normalization, remember the sign $P_G(1)=(-1)^n\chi_G(-1)$. From (12)–(13),

$$
\begin{aligned}
c_{N+4}^S&=91c_{N+3}^S-216c_{N+2}^S+91c_{N+1}^S-c_N^S\\
c_{N+4}^L&=96c_{N+3}^L-706c_{N+2}^L+96c_{N+1}^L-c_N^L-32
\end{aligned}
\tag{15}
$$

| Number of cores $N$ | Straight chain: $c_N^S$ | Constant L or R: $c_N^L$ | Common spanning-tree count $\tau_N$ |
|---|---:|---:|---:|
| 0, starting edge | 3 | 3 | 1 |
| 1 | 320 | 320 | 6 |
| 2 | 28435 | 28435 | 35 |
| 3 | 2518737 | 2504096 | 204 |
| 4 | 223092224 | 220348791 | 1189 |

The common spanning-tree matrix of the runner is $\left(\begin{smallmatrix}5&1\\4&1\end{smallmatrix}\right)$; its characteristic polynomial $q^2-6q+1$ gives $\tau_{N+2}=6\tau_{N+1}-\tau_N$. The derivation through trees and separating forests is given in [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]]. This two-coordinate reduction loses the position of the path's output edge. The five spectral coordinates retain it.

> [!note]- Proof of minimality of the orders
> **Proof.** A homogeneous linear recurrence of order $d$, with coefficients constant in $N$, implies rank at most $d$ for the Hankel matrix $(\chi_{i+j})_{i,j\ge0}$. This follows from the same linear dependence of each subsequent column on the preceding $d$ columns.
>
> At $\xi=-1$, exact computation of the leading minors gives
>
> $$
> \det(c_{i+j}^S)_{i,j=0}^{3}=2800526400,\qquad
> \det(c_{i+j}^L)_{i,j=0}^{4}=-1927817515468800
> $$
>
> Thus the corresponding determinants formed from the polynomials $\chi_N(\xi)$ are not identically zero. Over $\mathbb Q(\xi)$, the orders are at least $4$ and $5$. The recurrences already proved give the opposite bounds. The same check establishes minimality of the homogeneous recurrences for the numerical sequences $c_N$ at $\xi=-1$. At other special values of $\xi$, the order may drop; for example, at $\xi=0$, all $\chi_N$ vanish. $\square$

This concerns the minimal order of a scalar recurrence for two specific families. It does not prove minimality of the five-coordinate passport among all possible graph encodings, nor injectivity of a single characteristic polynomial.

## A periodic code and a composite runner

Let a block of outputs $v=\beta_1\cdots\beta_p$ be given. Combine $p$ successive paths into one component, retaining the first plug and the last socket. The composite runner itself has no starting edge. It has $4p+2$ vertices and $5p$ edges; the other seams are already internal to the component.

![Two paths as one composite runner and the product of spectral transitions](A%20Periodic%20SLR%20Runner.svg)

> [!info] Transfer over one period
> **Proposition 3.** Repetition of the composite runner has spectral matrix
>
> $$
> \mathbf V_v=\mathbf U_{\beta_p}\cdots\mathbf U_{\beta_1},
> \qquad \boldsymbol s_{mp}=\mathbf V_v^{\,m}\boldsymbol s_0
> \tag{16}
> $$
>
> The number of cores is $N=mp$, while $m$ counts composite steps. The sequence $\chi_{mp}$ satisfies a homogeneous linear recurrence of order at most $5$ in $m$.

> [!note]- Proof for a periodic block
> **Proof.** Successively identifying fresh path copies produces the same vertices and edges as first joining them into a block and then attaching the block. The initial and terminal pairs are disjoint. The sequence of state transfers is therefore the product in (16), with the rightmost factor acting first. The Cayley–Hamilton theorem for a matrix of size $5$ gives a recurrence in the number of blocks. Its actual order may be smaller. $\square$

For example, the block LR has $\mathbf V_{LR}=\mathbf U_R\mathbf U_L$. Repeating it gives alternating turns, after removing the first and last output letters when writing the full code (1). This is fixed weaving with a composite runner, even though the individual internal letters are not constant. The period phase and terminal boundary must be specified when comparing states.

## Exact checks and the status of the results

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_slr_weaving.py) uses integers and exact polynomials. It performs the following checks:

- the three matrices are derived afresh from the boundary determinants of the path $P_6$ without the input edge and compared with the SLR matrices;
- for all $121$ words with $2\le N\le6$, graphs constructed from paths are compared with an independent construction from cycles; the order of terminal contacts is also checked;
- for $14$ variants of the other input matching with $2\le N\le8$, alternation of letters is checked up to isomorphism of unmarked graphs;
- for S and L at $0\le N\le8$, $18$ characteristic polynomials, $18$ rooted determinants $\det(\mathbf I+\mathbf L)$, and $18$ spanning-tree cofactors are computed directly from edge lists;
- for these two families at $0\le N\le3$, all five coordinates are independently computed: $8$ polynomial passports;
- the coefficients (12), vector identities in the proof, recurrences, and minimality certificates are checked symbolically; $8$ reflected marked graphs and $5$ direct determinants for LR blocks, including the starting edge, are checked separately.

The full data, initial polynomials, and integer sequences are in the [results file](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/slr-weaving-results.json); the [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) and figure program are in the same directory. Approximate coordinates are used only for illustrations. Neither the proofs nor the graph checks impose planarity.

The correspondence between weaving and the SLR code, the formulas for constant families, and transfer over a period are proved for every finite length. Enumeration of short chains independently checks the implementation. Closures and minimal recurrences for arbitrary periods require their own boundary conditions and separate calculations. Recovery from a single polynomial or number remains distinct from the proved recovery of the full marked state in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]].

Recovery of configurations from moments and the characteristic polynomial is studied in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]]: formulas for partial recovery and insufficiency of any fixed number of leading coefficients are proved, and an exact catalog up to 18 cores is given. General distinguishability by the polynomial or by a single value remains conjectural.

Continuation: [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra|Periodic SLR Chains: Recurrences and Spectra]]. Exact recurrences are obtained for LR, SL, and LLS; the effects of end cores, cyclic shifts of the period, and growth of the number of rooted forests are discussed.

## Sources and related notes

The ternary description of hexagonal chains is classical: Milosavljević–Stevanović [1, §2] use F/R/L and markers for both end cores. In this library, F is replaced by S, and the final marker is omitted from the full code (1). The general connection between repeated graph constructions and linear recurrences belongs to the transfer-matrix method; see Noy–Ribó [2]. Here that method is applied to specific Laplacian boundary data, with explicit coefficients, orientations, and a proof of minimal orders. Independent scientific priority of these formulas is not established.

1. N. Milosavljević, D. Stevanović. *Detour Index of Hexagonal Chains*. MATCH **72** (2014), 137–152. [§2, Definition 1 and Figure 2](https://match.pmf.kg.ac.rs/electronic_versions/Match72/n1/match72n1_137-152.pdf#page=3).
2. M. Noy, A. Ribó. *Recursively constructible families of graphs*. Advances in Applied Mathematics **32** (2004), 350–363. [DOI](https://doi.org/10.1016/S0196-8858(03)00088-5); [author's publication list](https://sites.google.com/view/marcnoy/publications).

Related notes: [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]], [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]], [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]]. Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].
