---
title: Toponomes of the Greenian Exponential and Dual Pairs
date: 2026-10-28
updated: 2026-10-28
revision: 2
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: greenian-exponential-toponomes-and-dual-pairs
lang: en
description: "The canonical forest toponome of the Greenian, signed coefficients, two normalizations, structural identities, dual pairs, and exact reversal of spectral polynomial coefficients."
order: 9
---

[[ru/Гриниан и дуальность полиформ/Топономы экспоненты гриниана и дуальные пары|Русский]]

A toponome of the Greenian exponential is constructed in the same way as a toponome of the Laplacian exponential: vector factors are expanded over forests, then labeled partitions are replaced by component types. The coupling coefficients change, and with them the forest weights. For the Greenian, these weights and even their sums for an individual type may be negative.

Mutually pseudoinverse Laplacian and Greenian matrices give two full toponomes. Under vertex specialization, these become polynomials of reciprocal nonzero spectra. This exact relationship does not mean reversing the coefficient list of the full toponome: different types within one grade are combined only upon specialization.

We use [[The Canonical Vector Representation of the Greenian]], the [[From Polyforms to Partitions|definition of the toponome of a chosen representation]], and [[Symmetric Identities of the Greenian]].

## The canonical forest representation

Let $G$ be a connected undirected graph on $n\ge2$ vertices, with positive conductances on existing edges. Absent couplings have weight $0$. Write $d=n-1$, $\tau=\tau(G)$, and

$$
a_{ij}=a_j-a_i=(a_i a_j),\qquad
\mathbf{Gr}=\mathbf L^+,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

In one direct space, consider the vector forms and their exterior exponentials:

$$
\begin{aligned}
L&=\sum_{i<j}c_{ij}[a_{ij}]^2,& M&=\exp L\\
\mathrm{Gr}&=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,& N&=\exp(\mathrm{Gr})
\end{aligned}
$$

If the dual representation $D=\exp Q_1$ is used, then $N=\mathcal C(D)$ under the [[The Exterior Exponential and Representations of the Greenian#The centered image and the Greenian|centered identification]]. Centering preserves differences, so the canonical forest coefficients and their types coincide in these two expressions.

Let $\mathcal F_n$ be the set of all spanning forests of the complete graph on the given vertices. Isolated vertices belong to a forest; maximality under inclusion is not required. Zero weights allow the same set $\mathcal F_n$ to be used for both exponentials.

For a forest $F$ with component partition $\pi(F)=B_1\mid\cdots\mid B_m$, set

$$
q_{\pi(F)}=[(B_1)\cdots(B_m)]^2,\qquad
w_\gamma(F)=\prod_{ij\in E(F)}\gamma_{ij}
$$

A singleton component has boundary $1$. The empty edge set has weight $1$ and form $e$.

Expanding the vector factors gives

$$
\boxed{
N=\prod_{i<j}\bigl(e+\gamma_{ij}[a_{ij}]^2\bigr)
=\sum_{F\in\mathcal F_n}w_\gamma(F)q_{\pi(F)}
}
\tag{1}
$$

A repeated vector or a cycle makes the exterior product vanish. For a tree, the edge product agrees with the boundary of its vertices up to a sign that disappears in the quadratic form. Thus a forest with $k$ edges enters grade $N_k=\mathrm{Gr}^k/k!$ with the product of its weights, without an additional factor of $k!$.

This algebraic expansion holds for any symmetric vector form with real coefficients. Connectedness and positivity of the original graph will be needed for metric and spectral conclusions about the pair $L,\mathrm{Gr}$.

## The full toponome and the meaning of its coefficients

A vertex partition, its numerical type, and the corresponding toponome monomial are different levels of notation. For the fixed set $\{a,b,c,d\}$, the correspondence is:

| Vertex partition $\pi$ | Positive type $\lambda(\pi)$ | Monomial $x_{\lambda(\pi)}$ |
| --- | --- | --- |
| $a\mid b\mid c\mid d$ | Empty type | $1$ |
| $ab\mid c\mid d$ | $(1)$ | $x_1$ |
| $abc\mid d$ | $(2)$ | $x_2$ |
| $ab\mid cd$ | $(1,1)$ | $x_1^2$ |
| $abcd$ | $(3)$ | $x_3$ |

In the first column, $ab$ denotes the block $\{a,b\}$, not an edge or exterior product. Parts of a type are boundary grades, not block sizes: type $(2)$ corresponds to one nontrivial component on three vertices. Types classify forests and index sums; polynomial calculations use monomials $x_2$, $x_1^2$, and so on. This correspondence continues the conventions of [[From Polyforms to Partitions]].

A nontrivial component on $j+1$ vertices has grade $j$ and is replaced by the variable $x_j$. For a forest $F$, let $\lambda(F)=(k_1,\ldots,k_r)$ be its positive type: the unordered collection of grades of its nontrivial components. Then

$$
x_{\lambda(F)}=\prod_{\alpha=1}^r x_{k_\alpha},\qquad
\sum_{\alpha=1}^r k_\alpha=\#E(F)
$$

The empty index set is denoted by $\varnothing$; its basis symbol in type notation and its corresponding monomial are both $1$. Thus $x_\varnothing=1$. The number $n$ is retained separately: together with the type, it recovers the number of isolated vertices, $n-\sum_\alpha k_\alpha-r$.

> [!info] The full toponome and the meaning of its coefficients
> **Definition.** The canonical toponome of the Greenian exponential is the polynomial expression for the reduction of forest representation (1):
>
> $$
> \boxed{
> T_{\mathrm{Gr}}(\mathbf x)
> =\sum_{F\in\mathcal F_n}w_\gamma(F)x_{\lambda(F)}
> =\sum_\lambda c_{\mathrm{Gr}}(\lambda)x_\lambda
> }
> \tag{2}
> $$
>
> Its coefficient
>
> $$
> c_{\mathrm{Gr}}(\lambda)
> =\sum_{\substack{F\in\mathcal F_n\\\lambda(F)=\lambda}}
> \prod_{ij\in E(F)}\gamma_{ij}
> $$
>
> is the signed sum of weights of all forests of the specified type. A positive type means that its parts $k_\alpha$ are positive; it imposes no positivity requirement on the toponome coefficient.

Denote the analogous expression with $c_{ij}$ in place of $\gamma_{ij}$ by $T_L(\mathbf x)$. This is the original graph's toponome $T_G$ from [[Vector and Vertex Normalizations of Toponomes]]; the index $L$ distinguishes the members of the pair.

One may also sum over partitions. Let $t_\gamma(B)$ be the total weight of spanning trees on block $B$, with coupling weights $\gamma_{ij}$ within the block; set $t_\gamma(\{a_i\})=1$. Then

$$
c_{\mathrm{Gr}}(\lambda)
=\sum_{\substack{\pi\text{ a vertex partition}\\\lambda(\pi)=\lambda}}
\prod_{B\in\pi}t_\gamma(B)
$$

For each block, $t_\gamma(B)$ is calculated as a Laplacian cofactor of its internal couplings. This is the Laplacian of the induced weight system, not simply a principal submatrix of $\mathbf{Gr}$: the diagonal is recalculated from couplings within the block. This method is used in the [[Greenian Exponentials of Standard Graphs#Summing over partitions|formula for all grades through partitions]].

The first and top coefficients have direct interpretations:

$$
\begin{aligned}
c_{\mathrm{Gr}}(\varnothing)&=1\\
c_{\mathrm{Gr}}((1))&=\sum_{i<j}\gamma_{ij}
=\frac12\operatorname{tr}\mathbf{Gr}
=\frac{Kf(G)}{2n}\\
c_{\mathrm{Gr}}((d))&=\tau_\gamma=\frac1{n^2\tau}
\end{aligned}
\tag{3}
$$

Here $\varnothing$ indexes the empty type and is not a separate monomial; $Kf(G)=\sum_{i<j}R_{ij}$ is the Kirchhoff index. The grade-one equality follows from the zero row sums of $\mathbf{Gr}$ and the formula $R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}$. The top normalization is proved in [[The Canonical Vector Representation of the Greenian]]. In particular, the product of the top coefficients of the two full toponomes is $1/n^2$.

## Two normalizations and symmetric identities

The rooted weight of a type is determined by its component sizes:

$$
h(\lambda)=\prod_{\alpha=1}^r(k_\alpha+1),\qquad
h(\varnothing)=1
$$

It counts the choices of one root in each forest component. Vector normalization preserves $c_{\mathrm{Gr}}(\lambda)$, while vertex normalization multiplies it by $h(\lambda)$:

$$
T_{\mathrm{Gr}}^{\mathrm{vert}}(\mathbf x)
=\sum_\lambda h(\lambda)c_{\mathrm{Gr}}(\lambda)x_\lambda
=T_{\mathrm{Gr}}\bigl(2x_1,3x_2,4x_3,\ldots\bigr)
$$

As long as types are retained, this transition is invertible. Negative coefficients may remain in both normalizations; root choices merely multiply each forest weight by a positive integer.

To combine types, define two specializations:

$$
\begin{aligned}
F_{\mathrm{Gr}}(t,u)&=T_{\mathrm{Gr}}(\mathbf x)\big|_{x_j=t^ju}\\
P_{\mathrm{Gr}}(t,u)&=T_{\mathrm{Gr}}(\mathbf x)\big|_{x_j=(j+1)t^ju}
\end{aligned}
$$

The parameter $t$ marks the number of edges, and $u$ the number of nontrivial components. Setting $u=1$ gives univariate polynomials:

$$
F_{\mathrm{Gr}}(t)=\sum_{k=0}^d f_{\mathrm{Gr},k}t^k,
\qquad
P_{\mathrm{Gr}}(t)=\sum_{k=0}^d p_{\mathrm{Gr},k}t^k
$$

The first sums original forest weights, and the second sums forest weights with choices of roots. These definitions repeat the [[Vector and Vertex Normalizations of Toponomes|two Laplacian normalizations]] exactly, allowing signed weights.

The [[Symmetric Identities of the Greenian#Preservation of boundary identities|tetrahedron identity]] relates a sum of three forms of type $(1,1)$ to a sum of four forms of type $(2)$. Reduction gives:

| Stage | First expression | Second expression |
|---|---|---|
| Full toponome in vector normalization | $3x_1^2$ | $4x_2$ |
| Full toponome in vertex normalization | $12x_1^2$ | $12x_2$ |
| Substitution $x_j=t^j$ in the original toponome | $3t^2$ | $4t^2$ |
| Substitution $x_j=(j+1)t^j$ in the original toponome | $12t^2$ | $12t^2$ |

Equality appears in the last row. Multiplying coefficients by rooted weights does not yet identify different types. Retaining $u$ leaves distinct expressions $12t^2u^2$ and $12t^2u$.

Thus the full toponome belongs to the fixed forest representation (1). Structurally transforming the sum of forms before termwise reduction may change the toponome. The canonical choice of vector factors removes this ambiguity from the definition, but does not make an arbitrary reduction by types a linear map on the space of polyforms.

The univariate vertex evaluation preserves every structural identity: in the auxiliary Euclidean evaluation with orthonormal original vertices, the form $q_\pi$ receives the value $\prod_{B\in\pi}\#B$. The proof appears in the [[Vector and Vertex Normalizations of Toponomes#Compatibility with structural identities|theorem on independence of vertex evaluation]]. This is an auxiliary evaluation of forms, not their potential in the metric $N$.

## The vertex polynomial and the determinant

> [!info] The vertex polynomial and the determinant
> **Theorem.** The vertex specialization of the canonical Greenian toponome is
>
> $$
> \boxed{P_{\mathrm{Gr}}(t)=\det(\mathbf I+t\mathbf{Gr})}
> \tag{4}
> $$
>
> The equality holds for any symmetric matrix with zero row sums when its vector weights are defined as the negatives of its off-diagonal entries.

> [!note]- Proof
> **Proof.** Let $\mathbf B$ be the coordinate matrix of all pair vectors: its column for pair $ij$ is $\mathbf e_j-\mathbf e_i$. Let $\mathbf D_\gamma$ be the diagonal matrix of weights $\gamma_{ij}$. Zero row sums give
>
> $$
> \mathbf{Gr}=\mathbf B\mathbf D_\gamma\mathbf B^{\mathsf T}
> $$
>
> Expanding the determinant and applying Cauchy–Binet gives
>
> $$
> \det(\mathbf I+t\mathbf{Gr})
> =\sum_{S}t^{\#S}
> \left(\prod_{ij\in S}\gamma_{ij}\right)
> \det(\mathbf B_S^{\mathsf T}\mathbf B_S)
> $$
>
> The sum runs over sets of pairs. If a set contains a cycle, its columns are dependent and the determinant is zero. For a forest $F$, the Gram determinant of its columns is $\prod_{B\in\pi(F)}\#B=h(\lambda(F))$: a tree on $s$ vertices has $s$ nonzero maximal incidence minors, each equal to $\pm1$, and disjoint components give independent blocks. The empty forest contributes $1$. This is exactly the substitution $x_j=(j+1)t^j$ in (2). No restriction was imposed on the signs of $\gamma_{ij}$. $\square$

This is the matrix-forest theorem; the standard weighted-graph formulation appears in Chebotarev and Shamis [1, Theorem 5]. Their definition of weights allows negative values. The proof above explains why signs of Greenian coefficients do not prevent use of the formula.

For an arbitrary signed vector form, determinant coefficients may have either sign. For the Greenian of a connected graph with positive original conductances, all $p_{\mathrm{Gr},k}$, $0\le k\le d$, are positive: they are elementary symmetric sums of the positive nonzero eigenvalues of $\mathbf{Gr}$. This conclusion concerns the combined rooted sums, not each individual $c_{\mathrm{Gr}}(\lambda)$.

## The dual pair and reversal of spectral coefficients

We call the full toponomes $T_L$ and $T_{\mathrm{Gr}}$ a dual pair in the sense that they arise from mutually pseudoinverse matrices on the same vertex set. This name introduces no separate operation on arbitrary polynomials of types.

Set

$$
P_L(t)=\det(\mathbf I+t\mathbf L)
=\sum_{k=0}^d p_{L,k}t^k
$$

> [!info] The dual pair and reversal of spectral coefficients
> **Theorem.** For a connected graph with positive conductances,
>
> $$
> \boxed{
> P_{\mathrm{Gr}}(t)=\frac{t^d}{n\tau}P_L(1/t),
> \qquad
> p_{\mathrm{Gr},k}=\frac{p_{L,d-k}}{n\tau}
> }
> \tag{5}
> $$
>
> At $t=0$, the right-hand side is understood as the polynomial obtained after expansion.

> [!note]- Proof
> **Proof.** Denote the nonzero eigenvalues of $\mathbf L$ by $\mu_1,\ldots,\mu_d$. On $\mathbf1^\perp$, the matrix $\mathbf{Gr}$ has eigenvalues $\mu_i^{-1}$. By the matrix-tree theorem, $\prod_i\mu_i=n\tau$, so
>
> $$
> P_{\mathrm{Gr}}(t)
> =\prod_{i=1}^d\left(1+\frac{t}{\mu_i}\right)
> =\frac1{n\tau}\prod_{i=1}^d(t+\mu_i)
> =\frac{t^d}{n\tau}P_L(1/t)
> $$
>
> Comparing coefficients gives (5). $\square$

The roots of the polynomials are $-1/\mu_i$ and $-\mu_i$, respectively. They are pairwise reciprocals, including multiplicities. This concerns the nonzero spectrum; the common zero eigenvalue of both matrices contributes a factor of $1$ to the determinants.

The top coefficients of the rooted polynomials are

$$
p_{L,d}=n\tau,\qquad
p_{\mathrm{Gr},d}=\frac1{n\tau}
$$

The difference from $\tau$ and $1/(n^2\tau)$ in the full toponomes comes from the $n$ choices of a root in the single spanning component. The polyform's own normalization does not change.

For grade two, for example,

$$
p_{\mathrm{Gr},2}
=3c_{\mathrm{Gr}}((2))+4c_{\mathrm{Gr}}((1,1))
$$

Here $c_{\mathrm{Gr}}((2))$ is the coefficient of $x_2$, while $c_{\mathrm{Gr}}((1,1))$ is the coefficient of $x_1^2$. Formula (5) specifies this weighted sum, not its individual terms. By itself, it does not recover the full Greenian toponome from the Laplacian spectral polynomial.

## Examples of dual pairs

### The unit path on four vertices

Let the original graph have edges $ab,bc,cd$ of weight $1$. Its spanning coefficient is $\tau=1$. The Greenian vector coefficients are:

| Pair | $ab$ | $ac$ | $ad$ | $bc$ | $bd$ | $cd$ |
|---|---:|---:|---:|---:|---:|---:|
| $\gamma_{ij}$ | $-1/8$ | $3/8$ | $5/8$ | $1/8$ | $3/8$ | $-1/8$ |

Enumerating forests gives the pair

$$
\begin{aligned}
T_L(\mathbf x)&=1+3x_1+2x_2+x_1^2+x_3\\
T_{\mathrm{Gr}}(\mathbf x)&=1+\frac54x_1+\frac3{16}x_2
+\frac{15}{64}x_1^2+\frac1{16}x_3
\end{aligned}
\tag{6}
$$

In grade two, the coefficient of $x_2$ collects adjacent edge pairs, while the coefficient of $x_1^2$ collects disjoint edge pairs. For example, the coefficient of $x_1^2$ is

$$
\gamma_{ab}\gamma_{cd}+\gamma_{ac}\gamma_{bd}+\gamma_{ad}\gamma_{bc}
=\frac{1+9+5}{64}
=\frac{15}{64}
$$

The univariate vector polynomials are

$$
F_L(t)=1+3t+3t^2+t^3,\qquad
F_{\mathrm{Gr}}(t)=1+\frac54t+\frac{27}{64}t^2+\frac1{16}t^3
$$

The rooted specializations give

$$
P_L(t)=1+6t+10t^2+4t^3,\qquad
P_{\mathrm{Gr}}(t)=1+\frac52t+\frac32t^2+\frac14t^3
$$

Indeed, $P_{\mathrm{Gr}}(t)=t^3P_L(1/t)/4$. The vector polynomials are not related by this reversal: $t^3F_L(1/t)=F_L(t)\ne F_{\mathrm{Gr}}(t)$.

### A weighted path and a negative type coefficient

Retain the path $a-b-c-d$, setting $c_{ab}=c_{cd}=1$ and $c_{bc}=1/2$. Then $\tau=1/2$, and in pair order $ab,ac,ad,bc,bd,cd$,

$$
(\gamma_{ab},\gamma_{ac},\gamma_{ad},\gamma_{bc},\gamma_{bd},\gamma_{cd})
=\frac18(-3,5,7,3,5,-3)
$$

The exact toponomes are

$$
\begin{aligned}
T_L(\mathbf x)&=1+\frac52x_1+x_2+x_1^2+\frac12x_3\\
T_{\mathrm{Gr}}(\mathbf x)&=1+\frac74x_1-\frac5{16}x_2
+\frac{55}{64}x_1^2+\frac18x_3
\end{aligned}
\tag{7}
$$

The coefficient of $x_2$, corresponding to type $(2)$, is $-5/16$. Nevertheless, after vertex specialization the grade-two contribution is positive:

$$
3\left(-\frac5{16}\right)+4\frac{55}{64}=\frac52
$$

The polynomials of the pair are

$$
P_L(t)=1+5t+7t^2+2t^3,\qquad
P_{\mathrm{Gr}}(t)=1+\frac72t+\frac52t^2+\frac12t^3
$$

They satisfy (5) with $n\tau=2$. Thus positive definiteness of the Greenian on $\mathbf1^\perp$ is compatible with a negative total coefficient of an individual forest type.

### The complete graph

For the unit $K_n$, all Greenian coefficients are $1/n^2$. Thus each forest with $k$ edges acquires a factor $n^{-2k}$ relative to its original weight:

$$
T_{\mathrm{Gr}}(\mathbf x)
=T_L\left(\frac{x_1}{n^2},\frac{x_2}{n^4},\ldots,
\frac{x_d}{n^{2d}}\right)
$$

Here a relation is established for the full toponome itself. It follows from uniform rescaling of all couplings and is a special property of the complete graph.

For $K_4$, we obtain

$$
\begin{aligned}
T_L(\mathbf x)&=1+6x_1+12x_2+3x_1^2+16x_3\\
T_{\mathrm{Gr}}(\mathbf x)&=1+\frac38x_1+\frac3{64}x_2
+\frac3{256}x_1^2+\frac1{256}x_3
\end{aligned}
$$

The rooted polynomials are $P_L(t)=(1+4t)^3$ and $P_{\mathrm{Gr}}(t)=(1+t/4)^3$. The spanning coefficients $16$ and $1/256$ have product $1/16=1/n^2$.

## Greenian forests and original forests in the cut expression

In [[Cuts and Forest Grades of the Greenian Exponential]], the same grade $N_k$ is represented through forests of the original graph with $d-k$ edges. Its terms have the form $(w_c(F)/\tau)\mathcal C(\Phi_{\pi(F)})$, where $\Phi_\pi$ is built from sums of dual elements over blocks.

The two expressions use different data:

| Data for grade $N_k$ | Canonical vector expression | Cut expression |
|---|---|---|
| Indexing forest | On pairs with weights $\gamma_{ij}$ | In the original graph with weights $c_{ij}$ |
| Number of edges | $k$ | $d-k$ |
| Number of forest components | $n-k$ | $k+1$ |
| Form argument | Product of component boundaries | Product of block sums |
| Term weight | $w_\gamma(F)$ | $w_c(F)/\tau$ |

The forest type on the right describes the original partition. It is not automatically the type of the boundary components of the form $\mathcal C(\Phi_{\pi(F)})$ itself. Thus replacing this indexing forest by the monomial of its original type defines a different reduction; it does not coincide with (2) by definition.

After rooted spectral specialization, the comparison becomes exact. Formula (5) and the forest formula for $p_{L,d-k}$ give

$$
\boxed{
p_{\mathrm{Gr},k}
=\frac1{n\tau}
\sum_{\substack{F\in\mathcal F(G)\\\#E(F)=d-k}}
w_c(F)\prod_{B\in\pi(F)}\#B
}
\tag{8}
$$

Thus one coefficient can be calculated either from signed $k$-edge Greenian forests with rooted weights of their components, or from positive $(d-k)$-edge forests of the original graph with factor $1/(n\tau)$. The formula does not specify a pairwise correspondence between individual forests.

The factor $1/n$ can be seen directly in the evaluation of the cut form. Suppose the original vertices are orthonormal in an auxiliary inner product, with $p_i=a_i-h$, $h=n^{-1}\sum_i a_i$, and $s_B=\sum_{i\in B}p_i$. For a partition $B_1\mid\cdots\mid B_{k+1}$ with sizes $b_\alpha=\#B_\alpha$, the Gram matrix $\mathbf G_s$ of the first $k$ block sums has entries

$$
g_{\alpha\beta}
=b_\alpha\delta_{\alpha\beta}-\frac{b_\alpha b_\beta}{n},
\qquad 1\le\alpha,\beta\le k
$$

The rank-one determinant update lemma gives

$$
\det\mathbf G_s
=\left(\prod_{\alpha=1}^k b_\alpha\right)
\left(1-\frac{\sum_{\alpha=1}^k b_\alpha}{n}\right)
=\frac1n\prod_{\alpha=1}^{k+1}b_\alpha
$$

This is exactly the evaluation assigned to $\mathcal C(\Phi_\pi)=[s_{B_1}\cdots s_{B_k}]^2$. Multiplication by the coefficient $w_c(F)/\tau$ reproduces (8). At $k=0$, the empty determinant is $1$ and the sole block has size $n$, so the formula remains valid. This factor belongs to the spectral evaluation and does not change the normalization $Q_0=e$.

## Retained data and limits of the result

The full toponome retains the total weight of each positive type and, if $n$ is known, the vertex counts of all components. It does not retain vertex names, individual forests, or individual coupling weights. Coefficient tables further combine types with the same grade and number of nontrivial components; the spectral polynomial retains the rooted sum of each grade.

Potentials of labeled forms likewise cannot be recovered from their type. For example, for the unit path $a-b-c-d$, in the [[The Greenian Metric and Potentials#A path on four vertices|metric $N$]], the normalized potentials of $[a_{ab}]^2$ and $[a_{bc}]^2$ are $5$ and $6$, respectively, although both forms have type $(1)$. Their connection with the original Laplacian requires retaining the selected vertices.

The canonical forest formula, determinant specialization, and spectral reversal (5) are proved. Pairs (6), (7), and the example $K_4$ are calculated exactly; forest sums are compared with independent calculations of determinant coefficients through principal minors. The negative coefficient of $x_2$ in (7) is a calculated example, not a conjecture about every graph. The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/dual/verify_toponomes.py) reproduces these pairs and also checks the cycle $C_5$, a star on five vertices, and a nonuniformly weighted five-vertex graph. Run:

    python checks/dual/verify_toponomes.py

A general transformation from the full $T_L$ to the full $T_{\mathrm{Gr}}$, if possible without recovering the labeled matrix, is not established here. Its existence, required additional data, and limitations form a separate problem. Spectral formula (5) does not solve it. Directed and balanced extensions likewise require a separate definition of the corresponding Greenian and its bilinear exponential.

## Sources and connections

1. Chebotarev P., Shamis E. [Matrix-Forest Theorems](https://arxiv.org/abs/math/0602575v2). Manuscript from 1994–1997, arXiv revision of 2023. Theorem 5 expresses $\det(I+L)$ through the weight of rooted spanning forests; the preliminary definitions allow negative weights. Substituting $t\gamma_{ij}$ gives (4).
2. [[Forest Coefficients and the Laplacian Polynomial]]: a proof through principal minors, the role of roots, and the connection with the characteristic polynomial.
3. [[Toponomes and Structural Identities]] and [[Symmetric Identities of the Greenian]]: dependence of the full reduction on representation and admissible component evaluations.
4. [[Greenian Exponentials of Standard Graphs]]: matrices and forest grades of cycles, stars, complete graphs, paths, and more complex examples.
5. [[Laplacian and Greenian - Mutual Duality of Exponentials]]: mutual polyform duality before reduction by types; [[The Greenian Metric and Potentials]]: potentials of specific forms.

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
