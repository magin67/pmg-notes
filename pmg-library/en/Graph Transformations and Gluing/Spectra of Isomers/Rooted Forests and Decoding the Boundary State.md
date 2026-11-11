---
title: Rooted Forests and Decoding the Boundary State
date: '2026-11-02'
updated: 2026-11-11
revision: 3
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-rooted-decoding
order: 5
description: Rooted-forest meanings of five integer coordinates, invariant sectors, exact decoding, and a terminating reachability criterion.
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Корневые леса и декодирование граничного состояния|Корневые леса и декодирование граничного состояния]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

A closed rule for transferring five spectral coordinates was obtained in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], while [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] fixed the letters, the ordering of seam endpoints, and the symmetries of a chain. Here we consider the inverse problem: can the sequence of attachments be recovered from the final boundary state?

For open hexagonal chains, specialization at $\xi=-1$ is sufficient. With the signs chosen consistently, the five coordinates become integers that count rooted forests. They retain the entire oriented word: the signs of two linear expressions identify its last letter, and an inverse integer matrix removes one step. This statement has a general proof and is not restricted to the lengths covered by enumeration.

> [!note] Which data recover the code
> The full state contains five numbers on a **marked ordered boundary**. Its injectivity does not imply injectivity of the single number $P_G(1)$ or the characteristic polynomial $\chi_G$. These data do not retain the same boundary marking. The forest interpretations below rely on the classical matrix-forest theorems [1]; the specific algorithm for the chosen SLR transitions is proved separately. Neither a new proof nor an expression of known identities in PMG notation establishes scientific priority.

## The chain, the boundary, and the rooted polynomial

We retain the model of [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]: cores $C_6$ form an open path, joined along edges; the two seams of an intermediate core have no common vertices; nonadjacent cores do not intersect. There are no additional identifications or closure. All conductances are one, and each shared edge is counted once. The number of cores is $N$, and the number of vertices is $n=4N+2$.

For $N\ge2$, the full code has the form $w=Su$, where $u$ contains $N-2$ turn letters. The initial $S$ is a marker, not an operation on the state. For the active pair $(x,y)$, the new core is numbered so that $(0,1)=(y,x)$; the outputs $L,S,R$ are respectively $(2,3),(3,4),(4,5)$. This convention is essential for all the matrices below.

The rooted polynomial and the characteristic polynomial satisfy

$$
P_G(t)=\det(\mathbf I_n+t\mathbf L_G),\qquad
\chi_G(\xi)=\xi^nP_G(-1/\xi)
$$

For arbitrary $n$, we have $P_G(1)=(-1)^n\chi_G(-1)$. In our chains, $n$ is even, so the sign is positive. The ordinary forest polynomial $F_G(t)$ is not used here: it counts each spanning forest without multiplying by the number of choices of roots.

## What the five coordinates count

Set $\mathbf H_G=\mathbf I_n+\mathbf L_G$. For an ordered pair $(x,y)$, define the state

$$
\mathbf z=(a,b,c,d,e)^{\mathsf T}
$$

The letters $a,b,c,d,e$ denote numerical coordinates in this note; in particular, the last coordinate $e$ does not denote the unit form of polyform algebra.

> [!info] The rooted boundary state
> **Definition.** The five coordinates are defined by determinants and a cofactor:
>
> $$
> \begin{aligned}
> a&=\det\mathbf H_G=P_G(1)\\
> b&=\det(\mathbf H_G)_{\widehat x},\qquad
> c=\det(\mathbf H_G)_{\widehat y}\\
> d&=(\operatorname{adj}\mathbf H_G)_{xy},\qquad
> e=\det(\mathbf H_G)_{\widehat{\{x,y\}}}
> \end{aligned}
> \tag{1}
> $$
>
> A hat denotes deletion of the corresponding rows and columns. The degrees of the remaining vertices are not recomputed.

A spanning rooted forest contains all vertices of the graph and exactly one chosen root in each component, including isolated vertices. For unit conductances, the coordinates have the following meanings.

| Coordinate | Rooted forests counted |
| --- | --- |
| $a$ | All spanning rooted forests |
| $b$ | Vertex $x$ is the root of its component |
| $c$ | Vertex $y$ is the root of its component |
| $d$ | Vertices $x,y$ belong to the same component, whose chosen root is $y$ |
| $e$ | Vertices $x,y$ are the roots of two distinct components |

For $d$, one may choose $x$ instead of $y$ as the root: reassigning the root of the same component gives a bijection. Roots in the other components remain free to choose. These are five overlapping conditions, not a partition of forests into five disjoint classes.

> [!note]- Proof of the forest interpretation
> **Proof.** The matrix-forest theorems [1, Theorems 5–6] interpret the determinant $\mathbf I+\mathbf L$ and its cofactors, including $a,b,c,d$. For principal minors, it is also useful to assign variable root weights to the vertices:
>
> $$
> \det(\mathbf L+\operatorname{diag}(q_v))
> =\sum_{F}\prod_{T\in\pi(F)}\left(\sum_{v\in T}q_v\right)
> \tag{2}
> $$
>
> Here the sum is over spanning forests without chosen roots, and $\pi(F)$ is their set of components. This identity follows from the matrix-tree theorem: add a vertex $*$ and an edge $*v$ of weight $q_v$ to each vertex $v$; removing $*$ from a spanning tree leaves a forest with one chosen edge to $*$ per component.
>
> The derivative with respect to $q_x$, evaluated at all $q_v=1$, equals $b$ and requires $x$ to be chosen as a root. The mixed derivative with respect to $q_x,q_y$ equals $e$: the two variables can only come from distinct components. This proves the remaining interpretation and accounts for all the principal minors. $\square$

![Five conditions on forest roots and marked vertices](images/Five%20Rooted%20Coordinates.svg)

**Roots and boundary markings have different roles.** The figure shows one forest satisfying each condition. A filled green vertex is a root; rings mark $x,y$. The same rooted forest may contribute to several coordinates.

### Signs at the spectral specialization

Let $\mathbf s=(A,B,C,D,E)^{\mathsf T}$ be the spectral passport of [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]]. Since $\mathbf M_G(-1)=-\mathbf H_G$ and $n$ is even,

$$
\mathbf z=\mathbf R\mathbf s(-1),\qquad
\mathbf R=\operatorname{diag}(1,-1,-1,-1,1)
\tag{3}
$$

The sign of the cofactor $D$ changes in the same way as those of the minors of order $n-1$. Without this adjustment, the coordinates would not have the positive forest interpretation given above.

## Integer transfer and the terminal marking

In [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], the physical transitions are denoted by $\mathbf U_L=\mathbf T_2\mathbf J$, $\mathbf U_S=\mathbf T_3\mathbf J$, and $\mathbf U_R=\mathbf T_4\mathbf J$, where $\mathbf J$ exchanges the second and third coordinates. It is specifically the input pair that is permuted on the right.

Set $\mathbf N_\alpha=\mathbf R\mathbf U_\alpha(-1)\mathbf R$. Bold $\mathbf N_\alpha$ denotes a matrix, in contrast to the number of cores $N$. We obtain

$$
\mathbf N_S=\begin{pmatrix}
55&34&34&-2&21\\
24&16&15&0&10\\
24&15&16&0&10\\
9&6&6&1&4\\
9&6&6&0&4
\end{pmatrix}
\tag{4}
$$

$$
\mathbf N_L=\begin{pmatrix}
55&34&34&-2&21\\
21&21&13&0&13\\
24&16&15&0&10\\
8&8&5&1&5\\
8&8&5&0&5
\end{pmatrix}
\tag{5}
$$

$$
\mathbf N_R=\begin{pmatrix}
55&34&34&-2&21\\
24&15&16&0&10\\
21&13&21&0&13\\
8&5&8&1&5\\
8&5&8&0&5
\end{pmatrix}
\tag{6}
$$

The initial state of a single $C_6$ on a chosen edge is

$$
\mathbf z_0=(320,144,144,56,55)^{\mathsf T}
\tag{7}
$$

If $u=\alpha_1\cdots\alpha_m$, define the working state

$$
\mathbf z(u)=\mathbf N_{\alpha_m}\cdots\mathbf N_{\alpha_1}\mathbf z_0,
\qquad \mathbf z(\varnothing)=\mathbf z_0
\tag{8}
$$

After these $m=N-2$ operations, $N-1$ cores have been constructed. To complete the graph, the last core must be attached. On it, choose a free edge opposite the input edge, with its endpoints ordered according to convention $S$.

> [!info] The full state of a chain
> **Definition.** The full marked state of the code $w=Su$ is
>
> $$
> \boxed{\mathbf Z_{Su}=\mathbf N_S\mathbf z(u)=\mathbf z(uS)}
> \tag{9}
> $$
>
> Its first coordinate is $P_{G(Su)}(1)$. If $\mathbf r=(55,34,34,-2,21)$ is the common first row of the three matrices, then
>
> $$
> P_{G(Su)}(1)=\mathbf r\mathbf z(u)
> \tag{10}
> $$

The initial marker $S$ in the code $Su$ and the final factor $\mathbf N_S$ in (9) have different roles. The final factor actually adds a core, while the letter $S$ fixes only its free output marking. Decoding the full state recovers the operation word $uS$; removing the final $S$ and adding the initial marker gives the code $Su$.

### Jacobi's identity

> [!info] A quadratic constraint
> **Proposition.** Every rooted state satisfies
>
> $$
> Q(\mathbf z):=ae-bc+d^2=0
> \tag{11}
> $$
>
> All three matrices have determinant $1$ and preserve this quadratic form throughout the space: $Q(\mathbf N_\alpha\mathbf z)=Q(\mathbf z)$.

> [!note]- Proof of the quadratic constraint
> **Proof.** Equation (11) is the classical Jacobi identity for the determinant and minors of the symmetric matrix $\mathbf H_G$. Write $Q(\mathbf z)=\mathbf z^{\mathsf T}\mathbf Q\mathbf z$, where the nonzero entries of $\mathbf Q$ are $Q_{15}=Q_{51}=1/2$, $Q_{23}=Q_{32}=-1/2$, and $Q_{44}=1$. Substitution of (4)–(6) gives $\mathbf N_\alpha^{\mathsf T}\mathbf Q\mathbf N_\alpha=\mathbf Q$ and $\det\mathbf N_\alpha=1$. These finite matrix identities are checked exactly and hold for every vector. The initial state satisfies (11). $\square$

The five coordinates are not independent: when $a>0$, one can recover $e=(bc-d^2)/a$. The five-dimensional representation is convenient because the transfer remains linear. Minimality of this linear description is not established here.

### How the inverse step will work

For the full state $\mathbf Z_{SLR}$ in the worked example below, the two numbers are

$$
(9b-4a,9c-4a)=(3676257,3384873)
$$

Both signs are positive, so the last operation will be $S$. The inverse matrix $\mathbf N_S^{-1}$ removes it; the same procedure then removes $R$ and $L$ and stops at $\mathbf z_0$. This recovers the operations $LRS$, hence the code $SLR$.

It remains to justify why the signs always select the correct letter. The invariant region serves this purpose: it contains all reachable states, and the three transitions send it into different sectors. Its fractional bounds are auxiliary sufficient estimates for the proof, not additional data about the unknown chain.

## An invariant region and three sectors

Invertibility of the matrices alone is insufficient to recover a word: we must first identify which matrix to invert. To do this, we find a region whose images under the three transitions are distinguished by signs.

> [!info] The region of rooted states
> **Definition.** Let $\mathcal K$ denote the cone defined by
>
> $$
> \begin{gathered}
> a>0,\qquad \frac{43}{100}\le\frac ba,\frac ca\le\frac9{20}\\
> \frac{83}{500}\le\frac da\le\frac7{40},\qquad
> \frac4{25}\le\frac ea\le\frac9{50}
> \end{gathered}
> \tag{12}
> $$
>
> The cone itself is unbounded; its section $a=1$ is a four-dimensional box.

> [!info] Invariance of the region and growth of the first coordinate
> **Lemma.** The initial state belongs to $\mathcal K$. Each $\mathbf N_\alpha$ maps $\mathcal K$ strictly into the interior with respect to all four ratio constraints. If $\mathbf z'=\mathbf N_\alpha\mathbf z$, then
>
> $$
> \frac{349}{4}\le\frac{a'}a\le\frac{11131}{125}
> \tag{13}
> $$

> [!note]- Proof of invariance
> **Proof.** Set $r=b/a$, $s=c/a$, $h=d/a$, and $k=e/a$. The common first row gives
>
> $$
> a'/a=55+34r+34s-2h+21k
> $$
>
> The minimum and maximum over the box (12) are the bounds in (13); in particular, the denominator is positive. Let $\ell_i,u_i$ be the lower and upper bounds for $z_i/a$, where $i$ ranges over the coordinates $b,c,d,e$. The inequalities for the image are equivalent to positivity of $(z'_i-\ell_i a')/a$ and $(u_i a'-z'_i)/a$. These are affine functions of $r,s,h,k$, so their extrema occur at the $16$ vertices of the box. The minima taken over all three matrices are as follows:
>
> | Coordinate $i$ | Lower margin | Upper margin |
> | --- | --- | --- |
> | $b,c$ | $3559/25000$ | $123/400$ |
> | $d$ | $7079/125000$ | $1141/4000$ |
> | $e$ | $5229/12500$ | $4503/5000$ |
>
> All margins are strictly positive. Substituting (7) verifies that the initial state belongs to the region. Checking the vertices here gives an exact proof of affine inequalities throughout the region, rather than an experiment on a finite collection of chains. $\square$

Introduce the linear expressions

$$
U(\mathbf z)=9b-4a,\qquad V(\mathbf z)=9c-4a
\tag{14}
$$

> [!info] The last letter from two signs
> **Lemma.** For every $\mathbf z\in\mathcal K$, the signs in the image determine the transition:
>
> | Last transition | $U(\mathbf N_\alpha\mathbf z)$ | $V(\mathbf N_\alpha\mathbf z)$ |
> | --- | --- | --- |
> | $L$ | $-$ | $+$ |
> | $S$ | $+$ | $+$ |
> | $R$ | $+$ | $-$ |
>
> Neither sign is zero. Thus the three images $\mathbf N_L\mathcal K$, $\mathbf N_S\mathcal K$, and $\mathbf N_R\mathcal K$ are pairwise disjoint.

> [!note]- Proof of sector separation
> **Proof.** For the normalized coordinates used in the proof of (13), set
>
> $$
> \begin{aligned}
> p(r,s,h,k)&=-4+8r-s+8h+6k\\
> q(r,s,h,k)&=-31+53r-19s+8h+33k
> \end{aligned}
> $$
>
> Direct multiplication of (4)–(6) gives the pairs $(U(\mathbf z')/a,V(\mathbf z')/a)$:
>
> $$
> \begin{aligned}
> S&:\ (p(r,s,h,k),p(s,r,h,k))\\
> L&:\ (q(r,s,h,k),p(r,s,h,k))\\
> R&:\ (p(s,r,h,k),q(s,r,h,k))
> \end{aligned}
> $$
>
> Division is by the old positive coordinate $a$, which does not affect the signs. On the box (12),
>
> $$
> \frac{639}{500}\le p\le\frac{33}{20},\qquad
> -\frac{1269}{125}\le q\le-\frac{399}{50}
> $$
>
> These bounds follow from the signs of the coefficients of the affine functions; exchanging $r,s$ preserves the region. This proves the sign table. $\square$

![Separation of states by ratios of two rooted coordinates](images/Three%20Decoding%20Sectors.svg)

**The thresholds are $b/a=c/a=4/9$.** Colors show the three possible sectors of the last transition within the projection $\mathcal K$; the points represent the initial state and several of its descendants. Shading a sector does not mean that every point in it is reachable. The initial state also lies in sector $(+,+)$, so it must be checked before selecting a letter.

## The inverse algorithm and the decoding theorem

See [[en/PythonExamples/Example - Spectra of Isomers#Decoding a rooted state|the notebook calculation]].

> [!info] Injectivity of the full state
> **Theorem.** The map $u\mapsto\mathbf z(u)$ is injective on all finite oriented words over $\{S,L,R\}$, including the empty word. A reachable state determines the word and its length. Consequently, the full marked state $\mathbf Z_{Su}$ uniquely determines the code $Su$ and the number of cores $N$.

> [!note]- Proof of the decoding theorem
> **Proof.** All reachable states lie in $\mathcal K$. By (13), each operation increases $a$ by a factor greater than $87$; hence a nonempty word cannot produce $\mathbf z_0$. If the state is not initial, the sign table uniquely identifies the last letter $\alpha$. The matrix $\mathbf N_\alpha$ is invertible, so the previous state equals $\mathbf N_\alpha^{-1}\mathbf z$ and is also uniquely determined.
>
> Repeating this step recovers the word from right to left. For two words with the same state, the last letters coincide; removing identical invertible transitions either leads to two empty words or to an impossible equality between the initial state and a nonempty descendant. This proves injectivity for all lengths.
>
> For the full state, apply (9): the recovered word is $uS$, of length $N-1$. Removing the terminal $S$ and adding the initial marker gives $Su$. $\square$

Since the matrix determinants are $1$, the inverse matrices also have integer entries. Every step of the decoder uses integer arithmetic; the bounds (12) are checked by multiplying by positive denominators.

> [!example]- Inverse matrices for exact computation
>
> $$
> \mathbf N_S^{-1}=\begin{pmatrix}
> 4&-10&-10&8&21\\
> -6&16&15&-12&-34\\
> -6&15&16&-12&-34\\
> 0&0&0&1&-1\\
> 9&-24&-24&18&55
> \end{pmatrix}
> $$
>
> $$
> \mathbf N_L^{-1}=\begin{pmatrix}
> 5&-10&-13&10&21\\
> -5&15&13&-10&-34\\
> -8&16&21&-16&-34\\
> 0&0&0&1&-1\\
> 8&-24&-21&16&55
> \end{pmatrix}
> $$
>
> $$
> \mathbf N_R^{-1}=\begin{pmatrix}
> 5&-13&-10&10&21\\
> -8&21&16&-16&-34\\
> -5&13&15&-10&-34\\
> 0&0&0&1&-1\\
> 8&-21&-24&16&55
> \end{pmatrix}
> $$

### Recognizing an arbitrary candidate

The decoder can also be used when reachability of an integer vector is not known in advance.

1. If the vector does not belong to $\mathcal K$ or violates (11), reject it.
2. If the vector equals $\mathbf z_0$, stop and read the accumulated letters in reverse order.
3. Use the signs (14) to select $L,S,R$. A zero sign or the pair $(-,-)$ means rejection.
4. Compute $\mathbf z_{\mathrm{prev}}=\mathbf N_\alpha^{-1}\mathbf z$. If $0<a_{\mathrm{prev}}<a$ fails, reject the candidate.
5. Record $\alpha$, move to $\mathbf z_{\mathrm{prev}}$, and repeat.

> [!info] An exact reachability criterion
> **Corollary.** The algorithm terminates on every integer input. It accepts a vector if and only if it has the form $\mathbf z(u)$.

> [!note]- Proof of the reachability criterion
> **Proof.** At each continuing step, the positive integer $a$ strictly decreases, so an infinite computation is impossible. For a reachable state, the theorem guarantees the correct letter, and (13) guarantees the required decrease in $a$; the computation reaches the initial state. Conversely, if the algorithm reaches $\mathbf z_0$, reversing the equalities explicitly expresses the original vector as a product of the matrices (4)–(6) applied to $\mathbf z_0$. $\square$

To recognize a full chain state with the chosen terminal marking, the recovered nonempty operation word must additionally end in $S$. Then $N$ is one more than its length. A single core $N=1$ is represented separately by the state $\mathbf z_0$.

**The two preliminary constraints are insufficient.** The vector $2\mathbf z_0$ belongs to $\mathcal K$ and satisfies (11), but is not reachable. Its signs select $S$, after which

$$
\mathbf N_S^{-1}(2\mathbf z_0)=(6,4,4,2,2)^{\mathsf T}\notin\mathcal K
$$

This candidate is rejected. Neither the quadratic identity nor membership in one of the three sectors alone replaces the inverse algorithm.

## Example: recovering the code SLR

For the code $w=SLR$, the turn word is $u=LR$, and the number of cores is $N=4$. The full state uses the operation sequence $LRS$. We obtain

$$
\mathbf Z_{SLR}=
(220480560,98399833,98367457,37829429,37410444)^{\mathsf T}
\tag{15}
$$

In particular, $P_{G(SLR)}(1)=220480560$. The successive inverse steps are shown in the table; all numbers are exact.

| State | $U$ | $V$ | Action |
| --- | ---: | ---: | --- |
| $\mathbf z(LRS)$ | $3676257$ | $3384873$ | Remove $S$ |
| $\mathbf z(LR)$ | $41827$ | $-249557$ | Remove $R$ |
| $\mathbf z(L)$ | $-2761$ | $506$ | Remove $L$ |
| $\mathbf z_0$ | $16$ | $16$ | Stop |

The intermediate vectors are

$$
\mathbf z(LR)=(2504096,1117579,1085203,418985,414222)^{\mathsf T}
$$

$$
\mathbf z(L)=(28435,12331,12694,4763,4707)^{\mathsf T}
$$

![Removing the last core and recovering the operation word LRS](images/Reading%20SLR%20Backwards.svg)

**The inverse computation reads operations from right to left.** First it removes the terminal operation $S$, which specifies the marked last core. It then removes $R$ and $L$. In forward order, this is $LRS$; the corresponding chain code is $SLR$.

Checking for the initial state before selecting a sector is essential. Although $U(\mathbf z_0)=V(\mathbf z_0)=16$, there is no further letter $S$ here. Formally continuing would give $\mathbf N_S^{-1}\mathbf z_0=(3,2,2,1,1)^{\mathsf T}$, which lies outside $\mathcal K$.

## What has been recovered and what remains open

The theorem recovers an **oriented word under specified boundary conventions**. Reflection exchanges $L$ and $R$ and permutes $b,c$. Reversing a chain moves the marking to the other end and, in general, cannot be reduced to this permutation. These actions are compared in detail in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]].

If the required object is an unmarked graph class rather than an oriented code, decoding must be followed by identifying the four words $u,\bar u,u^{\leftarrow},\overline{u^{\leftarrow}}$. Their completeness for this class of chains is proved in the same note. Isomorphic graphs with different terminal markings may have different states; this is consistent with injectivity of the decoder.

The full polynomial boundary passport also distinguishes oriented words: equality of all five polynomials would imply equality of their specializations (3), and hence equality of the words. However, discarding four coordinates does not preserve the proved recovery criterion.

| Data | Result established here |
| --- | --- |
| Five integer coordinates on the chosen boundary | Exact decoding and recognition of reachability for every length |
| Five polynomial coordinates on the same boundary | Injectivity as a consequence of specialization |
| A single characteristic polynomial $\chi_G$ | Recovery of the entire graph class is not proved |
| A single number $P_G(1)$ | Recovery of the entire graph class is not proved |

It was already shown in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]] that the spectrum determines the number of bends when $N$ is known. Recovering their order from a single polynomial or number remains a separate question. Minimality of the linear state and extension of this decoding method to other cores, seams, or closed chains are also open.

In [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]], it is shown that the five integer coordinates can be recovered from three exact rational entries of the matrix $(\mathbf I+\mathbf L_G)^{-1}$ on the chosen boundary. Primitivity of the states restores the scale lost in normalization. That note also gives electrical and probabilistic interpretations and proves that there is no uniform positive error tolerance for chains of unbounded length.

## Exact checks

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_decoding.py) performs several checks with different logical roles.

- **Identities and certificates for the general proof:** specialization of the polynomial transitions, determinants and integer inverse matrices, preservation of $Q$, all $16$ vertices of the section $\mathcal K$ for each matrix, exact inequality margins, and bounds for the sign sectors.
- **Independent direct passports:** the matrices $\mathbf I+\mathbf L$ are constructed from edge lists; all five determinants and cofactors are compared with transfer for $C_6$ and all $13$ words $u$ of lengths $0$ through $2$, giving $14$ marked graphs.
- **Independent forest enumeration:** for $C_6,S,SS,SL$, all edge subsets are enumerated, cyclic subsets are discarded, and admissible root choices are counted from component sizes. All five coordinates are checked. In total, $133184$ edge subsets are examined, including the discarded cyclic ones.
- **Decoder implementation checks:** all $88573=\sum_{m=0}^{10}3^m$ operation words of length at most $10$, including the empty word, are recovered without errors or state collisions. The checks include stopping at the initial state, rejection of $2\mathbf z_0$, the full example (15), and removal of the terminal $S$.

For independent forest counting, an unrooted forest with components $T$ contributes $W=\prod_T\#T$ to $a$. If $T_x,T_y$ contain the marked vertices, the contributions to $b,c$ are $W/\#T_x,W/\#T_y$. The contribution to $d$ is $W/\#T_x$ when $T_x=T_y$, and zero otherwise; the contribution to $e$ is $W/(\#T_x\#T_y)$ when $T_x\ne T_y$, and zero otherwise. This enumeration does not use transfer matrices.

The [exact results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/decoding-results.json) record the matrices, rational certificates, example states, and counts. The [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) and the program for the three figures are in the same directory. The main computations use integers and rational fractions only; approximate coordinates are used solely for the illustrations.

Finite enumeration checks the implementation and examples. Injectivity for arbitrary length follows from invariance of $\mathcal K$, separation of its three images, and invertibility of the transitions.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

## Sources and related notes

1. P. Chebotarev, E. Shamis. *Matrix-Forest Theorems*. Manuscript, 1994–1997, [arXiv:math/0602575](https://arxiv.org/abs/math/0602575), Theorems 5–6 for undirected graphs. The determinant $\mathbf I+\mathbf L$ and its cofactors count rooted forests with the stated conditions on marked vertices.

Foundational notes: [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]].
