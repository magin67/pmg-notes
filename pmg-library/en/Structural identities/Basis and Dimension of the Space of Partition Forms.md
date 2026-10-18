---
title: Basis and Dimension of the Space of Partition Forms
date: 2026-10-18
updated: 2026-10-18
revision: 2
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: partition-form-basis-and-dimension
lang: en
description: "A basis of noncrossing partition forms, a proof using structural identities and a pairing, Narayana and Catalan numbers, and the number of independent relations."
order: 3
---

Structural identities express some partition forms in terms of others. This raises two questions: which family of forms suffices for all such expressions, and why are there no further dependencies within the chosen family? A basis of noncrossing partition forms answers both questions. The number of basis elements in each grade is a Narayana number; the total over all grades is a Catalan number.

One application that motivates these questions is gluing two initially separate graphs along several vertices. Forests within each piece induce partitions of the shared vertex set. For computations, we need to know how many independent coordinates to retain in the corresponding polyforms. This note establishes the algebraic result about partition forms; the gluing formula is treated in [[Structural Identities and Graph Gluing]].

We use [[Partition Forms and the Tetrahedron Identity|partition forms]], the [[Constructing Structural Identities#The tetrahedron identity for four blocks|four-block identity]], and [[Core specification#The spanning-tree form and coefficient extraction|top-coefficient extraction]]. All spaces are over $\mathbb R$, before a graph or metric is chosen.

The general proof uses two known combinatorial results: the Kenyon-Wilson algorithm and the nonsingularity of the pairing matrix for noncrossing partitions. We state these results with precise references and prove separately that they apply to PMG forms.

## The space whose dimension we compute

Let $A=\{a_1,\ldots,a_n\}$, $n\geqslant1$, be a basis of the formal space $V$, and let $W=\ker\varepsilon$ be the $(n-1)$-dimensional space of affine vectors. For a partition $\pi=B_1|\cdots|B_k$, recall

$$
X_\pi=(B_1)\cdots(B_k),\qquad
q_\pi=[X_\pi]^2,\qquad
\operatorname{gr}q_\pi=n-k
$$

A block and a component of a partition mean the same thing. A block of $s$ vertices gives a boundary of grade $s-1$; a singleton block contributes the unit form $e$.

**Definition.** For $0\leqslant r\leqslant n-1$, set

$$
\mathcal P_{n,r}
=\operatorname{span}_{\mathbb R}
\{q_\pi:\pi\text{ has }n-r\text{ blocks}\},
\qquad
\mathcal P_n=\bigoplus_{r=0}^{n-1}\mathcal P_{n,r}
$$

This is the space of partition forms on the fixed set $A$. It differs both from the space $\Lambda^rW$ of exterior objects and from the full space of forms $[X,Y]$ with $X,Y\in\Lambda^rW$.

For comparison, if $d=\binom{n-1}{r}$, then the exterior space has dimension $d$, while the full space of forms on it has dimension $d^2$. The latter follows from the definition of forms, whose only defining relations are bilinearity: for a basis $u_I$, all $[u_I,u_J]$ form a basis of the space of forms. The space $\mathcal P_{n,r}$ is spanned by the special quadratic forms $q_\pi$ and can be substantially smaller.

To distinguish partitions from their associated forms, introduce the free vector space $\mathcal F_{n,r}$ with basis symbols $b_\pi$, one for each partition of grade $r$, and the map

$$
\Phi_{n,r}:\mathcal F_{n,r}\longrightarrow\mathcal P_{n,r},
\qquad b_\pi\longmapsto q_\pi
$$

The symbols $b_\pi$ are independent by definition; the forms $q_\pi$ may be dependent. Thus

$$
\dim\mathcal F_{n,r}=S(n,n-r),\qquad
\operatorname{rank}\Phi_{n,r}=\dim\mathcal P_{n,r}
$$

Here $S(n,k)$ is a Stirling number of the second kind: the number of partitions of an $n$-element set into $k$ nonempty unordered blocks. Structural identities correspond to the kernel $\ker\Phi_{n,r}$.

## Noncrossing partitions and the basis

Fix a cyclic order of the vertices $a_1,\ldots,a_n$, and abbreviate the vertices by their indices.

**Definition.** A partition is **noncrossing** if there are no four indices $i<j<k<\ell$ such that $i,k$ lie in one block and $j,\ell$ lie in another. Denote the set of these partitions by $\mathrm{NC}_n$.

For example, in the order $a,b,c,d$, the partition $ac|bd$ is crossing, whereas $ab|cd$ and $ad|bc$ are noncrossing. With the vertices drawn on a circle, the distinction is visible in the crossings of chords joining vertices within different blocks.

The order serves to choose a basis. The definitions of forms and structural identities do not depend on it. No graph is assumed to be planar.

> [!info] A basis of partition forms
> **Theorem.** For a fixed cyclic order, the family
>
> $$
> \mathcal B_n=\{q_\sigma:\sigma\in\mathrm{NC}_n\}
> $$
>
> is a basis of $\mathcal P_n$. Its grade-$r$ subfamily is a basis of $\mathcal P_{n,r}$. Every partition form has a unique expansion in this basis, with integer coefficients.

The proof consists of spanning and independence. The first part uses the four-block identity; the second uses the top coefficient of a product of forms.

## Why the chosen forms span the space

The [[Constructing Structural Identities#The tetrahedron identity for four blocks|previous note]] proves an identity for nonempty pairwise disjoint sets $A,B,C,D$. Solve it for one term:

$$
\begin{aligned}
q_{AC|BD}
&=q_{A|BCD}+q_{B|ACD}+q_{C|ABD}+q_{D|ABC}-\\
&\qquad-q_{AB|CD}-q_{AD|BC}
\end{aligned}
\tag{1}
$$

Unions of sets are abbreviated as $AC$, $BCD$, and so on. The same additional blocks may be included in all seven partitions. The number of blocks, and hence the grade, is preserved. The coefficients on the right are $1$ or $-1$.

**Combinatorial result used.** The Kenyon-Wilson algorithm expresses any partition as an integer linear combination of noncrossing partitions by means of the seven-term rule (1). The result is stated in Theorem 1.2 of [1]; a terminating sequence of transformations is constructed in the proof of Theorem 2.6, using Lemmas 2.3-2.5 and Rule 1 of Section 1.2.

> [!note]- Proof of spanning using the Kenyon-Wilson algorithm
> **Proof.** Apply that sequence of transformations to a partition $\pi$. In PMG, each application of the seven-term rule is an equality of forms by (1).
>
> The other operations in the algorithm also preserve equalities: adding a separate vertex means adding a singleton block, while inserting a new vertex $x$ into the block containing vertex $j$ is implemented by subsequent multiplication by $[(jx)]^2$. These operations are proved in the [[Constructing Structural Identities#Transferring and multiplying identities|lemma on joining a pair]]. Additional blocks are adjoined by multiplication by their forms.
>
> The entire sequence therefore carries over to the PMG algebra and terminates in an equality
>
> $$
> q_\pi=\sum_{\sigma\in\mathrm{NC}_n}c_{\sigma\pi}q_\sigma,
> \qquad c_{\sigma\pi}\in\mathbb Z
> \tag{2}
> $$
>
> Only forms of the same grade as $q_\pi$ remain in the sum. Integrality follows from the coefficients in (1): no division occurs in the transformations. Hence the chosen forms span the space. $\square$

The existence of a terminating sequence, proved in [1], is essential. Applying (1) arbitrarily to any visible crossing does not itself prove termination. Spanning alone also does not establish independence.

## The top coefficient and the partition pairing

Let $T_n=[(a_1\ldots a_n)]^2$ be the spanning-tree form, and let $\tau(P)$ be its coefficient in the top-grade component of a polyform $P$. We use the normalization in the [[Core specification#The spanning-tree form and coefficient extraction|specification]]:

$$
P_{n-1}=\tau(P)T_n
$$

**Definition.** Introduce the bilinear pairing on $\mathcal P_n$

$$
\beta(P,Q)=\tau(PQ)
$$

The pairing is defined by the formal product and coefficient extraction. It is not a metric evaluation and requires no inner product. For homogeneous forms, it can be nonzero only when the grades sum to $n-1$.

Write $b(\pi)$ for the number of blocks of a partition. The partition $\pi\vee\rho$ groups together all vertices connected by a chain of memberships in common blocks of $\pi$ or $\rho$. The condition $\pi\vee\rho=\{A\}$ means that all vertices are connected in this way.

> [!info] Pairing partition forms
> **Lemma.** For any partitions $\pi,\rho$ of $A$,
>
> $$
> \boxed{
> \beta(q_\pi,q_\rho)=
> \begin{cases}
> 1,&b(\pi)+b(\rho)=n+1\text{ and }\pi\vee\rho=\{A\}\\
> 0,&\text{otherwise}
> \end{cases}
> }
> \tag{3}
> $$

> [!note]- Proof of the pairing formula
> **Proof.** If the sum of the grades differs from $n-1$, the top coefficient of the product is zero. Consider complementary grades, for which $b(\pi)+b(\rho)=n+1$.
>
> Choose a tree on the vertices of each block of both partitions. By the [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|edge-product rule]], the product of the edge forms of the first forest is $q_\pi$, and that of the second is $q_\rho$. Their union has exactly
>
> $$
> (n-b(\pi))+(n-b(\rho))=n-1
> $$
>
> edges, counted with multiplicity. An edge present in both forests is counted twice.
>
> The components of the union are described by $\pi\vee\rho$. If the union is connected, its $n-1$ edges make it a tree. The product of its edge vectors equals $(a_1\ldots a_n)$ up to sign. Thus the product of the forms is $T_n$, and the coefficient is $1$.
>
> If the union is disconnected, its $n-1$ edge vectors are linearly dependent: with $c\geqslant2$ components, they lie in a subspace of dimension $n-c<n-1$. Their exterior product, and hence the product of the forms, is zero. A repeated edge also gives a linear dependence.
>
> For $n=1$, both forests are empty, $T_1=e$, and $\tau(e)=1$, in agreement with the formula. $\square$

Formula (3) contains no factorial factors or tree weights. One tree is chosen in each block for the calculation; there is no sum over trees. Orientation signs disappear in quadratic forms.

## Why the chosen forms are independent

Denote the right-hand side of (3) by $\kappa(\pi,\rho)$ and form the square matrix

$$
\mathbf K_n=
\bigl(\kappa(\sigma,\rho)\bigr)_{\sigma,\rho\in\mathrm{NC}_n}
$$

Rows and columns are indexed by all noncrossing partitions, with all possible numbers of blocks.

**External theorem used.** The matrix $\mathbf K_n$ is nonsingular over $\mathbb R$ for every $n\geqslant1$. In Kenyon-Wilson, this is the matrix $M_t$: see its definition and equations (3)-(4) in Sections 2.1-2.2 of [1]. Nonsingularity follows from the result of Di Francesco-Golinelli-Guitter on the meander determinant [2], equations (5.14)-(5.18).

The definition of $M_t$ in terms of block counts and connectivity of the union agrees exactly with (3). Thus the cited result applies to the same matrix obtained from PMG forms. We do not reproduce the proof of the general meander determinant here; it is an external foundation for the following argument.

> [!note]- Proof of independence
> **Proof.** Suppose
>
> $$
> \sum_{\sigma\in\mathrm{NC}_n}d_\sigma q_\sigma=0
> $$
>
> Multiply by each form $q_\rho$, $\rho\in\mathrm{NC}_n$, and apply $\tau$. The lemma gives
>
> $$
> \sum_{\sigma\in\mathrm{NC}_n}
> d_\sigma\kappa(\sigma,\rho)=0
> $$
>
> Nonsingularity of $\mathbf K_n$ implies $d_\sigma=0$ for every $\sigma$. The forms are therefore independent. Together with spanning, this proves the basis theorem, including uniqueness of the expansion (2). $\square$

In particular, $\beta$ is nondegenerate on $\mathcal P_n$ and pairs grades $r$ and $n-1-r$. This is an algebraic pairing; no positive-definiteness claim is made.

## Narayana and Catalan numbers

Noncrossing partitions into $k$ blocks are counted by the **Narayana numbers**:

$$
N(n,k)=\frac1n\binom nk\binom n{k-1},
\qquad 1\leqslant k\leqslant n
$$

This is a known combinatorial formula; it appears, for example, in Section 3 of [3]. For completeness, we derive it independently of the algebra of forms.

> [!note]- Counting noncrossing partitions
> **Proof.** Write $c_{n,k}$ for the desired counts and introduce the formal generating series
>
> $$
> F(x,y)=1+\sum_{n\geqslant1}\sum_{k=1}^n c_{n,k}x^ny^k
> $$
>
> Suppose the block containing the first vertex has size $s$. Its vertices determine $s$ intervals, each of which is independently filled by a noncrossing partition. Hence
>
> $$
> F=1+y\sum_{s\geqslant1}x^sF^s
> =1+\frac{yxF}{1-xF}
> $$
>
> Setting $H=F-1$ gives the equivalent equation $H=x(1+H)(y+H)$. Lagrange inversion yields, for $n\geqslant1$,
>
> $$
> \begin{aligned}
> c_{n,k}
> &=[x^ny^k]H\\
> &=\frac1n[t^{n-1}y^k](1+t)^n(y+t)^n\\
> &=\frac1n\binom nk\binom n{k-1}
> \end{aligned}
> $$
>
> Here square brackets containing a monomial denote coefficient extraction from a generating series. $\square$

In grade $r$, the number of blocks is $k=n-r$. The basis theorem now gives

$$
\boxed{
\operatorname{rank}\Phi_{n,r}
=\dim\mathcal P_{n,r}
=N(n,n-r)
=\frac1n\binom nr\binom n{r+1}
}
\tag{4}
$$

The rank of the family of all partition forms equals the number of elements in the chosen basis. The formula counts labeled vertices and unordered blocks; no additional division by block permutations is required.

Summing over the grades gives the **Catalan number**:

$$
\boxed{
\dim\mathcal P_n
=\sum_{r=0}^{n-1}N(n,n-r)
=C_n
=\frac1{n+1}\binom{2n}{n}
}
\tag{5}
$$

> [!note]- Summing over the grades
> **Proof.** By Vandermonde's identity,
>
> $$
> \begin{aligned}
> \sum_{k=1}^n N(n,k)
> &=\frac1n\sum_{k=1}^n\binom nk\binom n{k-1}\\
> &=\frac1n\binom{2n}{n-1}\\
> &=\frac1{n+1}\binom{2n}{n}
> \end{aligned}
> $$
>
> The grades form a direct sum, so their dimensions add. $\square$

At the extreme grades, $\dim\mathcal P_{n,0}=\dim\mathcal P_{n,n-1}=1$. For $n\geqslant2$, also $\dim\mathcal P_{n,1}=\binom n2$: all vertex-pair forms are independent.

## Four vertices: a basis and an explicit check

Fix the order $a,b,c,d$. The seven partitions of grade $2$ consist of four triples with a singleton and three partitions into pairs. The only crossing partition is $ac|bd$. The tetrahedron identity expresses its form in terms of the others:

$$
\begin{aligned}
q_{ac|bd}
&=q_{a|bcd}+q_{b|acd}+q_{c|abd}+q_{d|abc}-\\
&\qquad-q_{ab|cd}-q_{ad|bc}
\end{aligned}
$$

Thus a basis can be chosen in the order

$$
q_{a|bcd},\ q_{b|acd},\ q_{c|abd},\ q_{d|abc},\ q_{ab|cd},\ q_{ad|bc}
$$

In this case, independence can be checked without the general external theorem. Pair these six forms with the pair forms $ab,ac,ad,bc,bd,cd$, in that order. In the partition for each pair, the remaining vertices are singleton blocks. Formula (3) gives the matrix

$$
\mathbf H=
\begin{pmatrix}
1&1&0&0&0&1\\
1&0&1&0&1&1\\
1&0&0&1&1&0\\
0&1&1&0&1&0\\
0&1&0&1&1&1\\
0&0&1&1&0&1
\end{pmatrix},
\qquad \det\mathbf H=8\ne0
$$

Rows correspond to pair forms; columns correspond to the six grade-$2$ forms listed above. For example, the pair $ab$ joins different blocks in $a|bcd$, $b|acd$, and $ad|bc$, giving three ones in the first row.

Nonsingularity of this matrix proves independence of the six forms. Consequently,

$$
\dim\mathcal P_{4,2}=6=N(4,2),\qquad
\dim\mathcal P_4=1+6+6+1=14=C_4
$$

Meanwhile, $\dim W=3$, $\dim\Lambda^2W=3$, and the full space of grade-$2$ forms on $W$ has dimension $9$. These numbers refer to different spaces.

## The number of independent identities

The rank-nullity theorem gives

$$
\boxed{
I_{n,r}:=\dim\ker\Phi_{n,r}
=S(n,n-r)-N(n,n-r)
}
\tag{6}
$$

This is the number of independent linear relations among partition forms. There are infinitely many expressions for identities: one may take linear combinations and multiply equalities by scalars.

Summing over the grades gives

$$
I_n=B_n-C_n,\qquad
B_n=\sum_{k=1}^n S(n,k)
$$

Here $B_n$ is the Bell number: the number of all partitions of a set of $n$ vertices.

| $n$ | All partitions $B_n$ | Dimension $C_n$ | Independent relations $I_n$ |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 5 | 5 | 0 |
| 4 | 15 | 14 | 1 |
| 5 | 52 | 42 | 10 |
| 6 | 203 | 132 | 71 |

For six vertices, the distribution by grade is:

| Grade $r$ | Blocks $n-r$ | Forms $S(6,6-r)$ | Rank $N(6,6-r)$ | Relations $I_{6,r}$ |
|---:|---:|---:|---:|---:|
| 0 | 6 | 1 | 1 | 0 |
| 1 | 5 | 15 | 15 | 0 |
| 2 | 4 | 65 | 50 | 15 |
| 3 | 3 | 90 | 50 | 40 |
| 4 | 2 | 31 | 15 | 16 |
| 5 | 1 | 1 | 1 | 0 |
| Total | | 203 | 132 | 71 |

**Independent computational check.** For $1\leqslant n\leqslant6$, all partition forms were expanded directly in the basis $u_i=a_i-a_1$, $i=2,\ldots,n$. If $X_\pi=\sum_I x_{\pi,I}u_I$, the column for $q_\pi$ consists of the coefficients $x_{\pi,I}x_{\pi,J}$ of $[u_I,u_J]$. Exact Gaussian elimination over the rationals gave the ranks in (4); the noncrossing subfamilies had the same ranks and were independent. Formula (3) was also checked by direct exterior multiplication for every pair of partitions of complementary grades in these cases. These computations confirm the examples, but the general proof does not depend on them.

## Completeness of the four-block identity

The basis theorem does more than count dimensions. For a fixed cyclic order, it also provides a basis of the structural relations themselves.

For each crossing partition $\pi$, use the unique coefficients from (2) and set, in the free vector space,

$$
R_\pi=b_\pi-\sum_{\sigma\in\mathrm{NC}_n}c_{\sigma\pi}b_\sigma
$$

The sum is over partitions of the same grade.

**Corollary.** The relations $R_\pi$, one for each crossing partition of grade $r$, form a basis of $\ker\Phi_{n,r}$. All structural identities are generated by the four-block identity with additional unchanged blocks.

> [!note]- Proof of completeness
> **Proof.** By (2), each $R_\pi$ lies in the kernel. Among its coordinates at crossing partitions, there is exactly one nonzero entry, equal to $1$, at $b_\pi$. Hence all $R_\pi$ are independent.
>
> From any element of the kernel, subtract a linear combination of the $R_\pi$ that eliminates its coefficients at crossing partitions. The remainder lies in the kernel and involves only symbols for noncrossing partitions. Independence of the corresponding forms makes the remainder zero. Thus the $R_\pi$ span the entire kernel.
>
> Each transformation producing (2) is an application of the seven-term relation. Inserting vertices into its blocks and adjoining additional blocks preserve this pattern. Therefore $R_\pi$ is a linear combination of instances of the four-block identity, as is every element of the kernel. $\square$

Thus a correspondence between crossing partitions and basis relations exists **after a cyclic order has been chosen**. The basis depends on that choice. Its compatibility with transfer by adjoining singleton blocks, and the count of new independent relations by support size, are proved in [[Supports of Structural Identities]].

## Applying the basis to graph gluing

Let $n$ now denote the number of vertices shared by two graph pieces. The basis preserves all values of the pairing $\beta$, which uses the top coefficient. If

$$
P=\sum_{\sigma\in\mathrm{NC}_n}p_\sigma q_\sigma
$$

then, for any $Q\in\mathcal P_n$, bilinearity gives

$$
\tau(PQ)=\sum_{\sigma\in\mathrm{NC}_n}
p_\sigma\,\tau(q_\sigma Q)
$$

Hence the $C_n$ coordinates of $P$ in the chosen basis suffice for all such pairings. Within a single grade, the Narayana number in (4) suffices.

For an initial expression $P=\sum_\pi g_\pi q_\pi$, passing to the basis transforms the coefficients by

$$
p_\sigma=\sum_\pi c_{\sigma\pi}g_\pi
$$

Structural identities concern the forms $q_\pi$. They do not imply that the original coefficients $g_\pi$, such as weight sums of forests of specified types, satisfy the same relations.

[[Structural Identities and Graph Gluing]] proves how the spanning-tree coefficient of a glued graph is expressed by such a pairing of polyforms on the shared vertices. It also considers the reverse reading of the construction: computing from a prescribed graph decomposition. The full unrooted spanning-forest polynomial requires a separate compatibility check; the result about $\beta$ does not transfer to it automatically. Here $C_n$ describes a linear space of forms and is not asserted to be the minimum number of arbitrary, possibly nonlinear, parameters of a particular graph.

## Status of the results and scope

- **Proved using external theorems:** noncrossing forms constitute a basis; the dimension formulas (4)-(5), the relation count (6), and completeness of the seven-term relations hold for every $n\geqslant1$.
- **Proved directly in PMG:** the pairing formula (3) and the passage from the two combinatorial results to statements about forms. The four-block identity is proved in the previous note.
- **External foundations:** the terminating expansion algorithm from [1] and nonsingularity of the matrix from [1]-[2]. No wholly internal proof of the general result that avoids these combinatorial theorems is offered here.
- **Computed directly:** the ranks for $n\leqslant6$ and the determinant $8$ in the four-vertex example.

The cyclic order affects the choice of basis and its coordinates, but not the dimension of the space. All vertices in the proof are independent basis elements of $V$. Substituting affine points in a lower-dimensional space may introduce additional dependencies; formula (4) then does not automatically give the rank of the substituted family.

Choosing a metric preserves the equalities of forms already proved. Numerical values after metric evaluation do not provide a criterion for linear independence of the forms. Moreover, this note concerns all labeled partitions; the space of symmetric sums $E_n[\lambda]$ is a separate subject for the next series.

## Sources

1. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325-1364. [arXiv:math/0608422v4](https://arxiv.org/abs/math/0608422v4), Section 1.2, Rule 1 and Theorem 1.2; Sections 2.1-2.2, matrix $M_t$ and equations (3)-(4); Section 2.3, Lemmas 2.3-2.5 and the proof of Theorem 2.6. [DOI: 10.1090/S0002-9947-2010-04964-5](https://doi.org/10.1090/S0002-9947-2010-04964-5).
2. P. Di Francesco, O. Golinelli, E. Guitter. *Meanders and the Temperley-Lieb Algebra*. Communications in Mathematical Physics, 186 (1997), 1-59. [arXiv:hep-th/9602025](https://arxiv.org/abs/hep-th/9602025), Section 5: the meander determinant (5.6), its derivation in Section 5.4, and nonsingularity of the one-component matrix in (5.14)-(5.18). [DOI: 10.1007/BF02885671](https://doi.org/10.1007/BF02885671).
3. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du. *Reduction of m-Regular Noncrossing Partitions*. [arXiv:math/0406180](https://arxiv.org/abs/math/0406180), Section 3: Narayana numbers as the counts of noncrossing partitions with a specified number of blocks.

This note is based on the author's research within PMG. The passage from combinatorial results to statements about forms is proved above using the cited external theorems.