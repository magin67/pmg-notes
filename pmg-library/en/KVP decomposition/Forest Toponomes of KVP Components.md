---
title: Forest Toponomes of KVP Components
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: forest-toponomes-of-kvp-components
lang: en
order: 9
description: "Forest toponomes of signed KVP components, balance identities for P, and the joint toponome. Grade two without mixed terms, examples of interactions, and limits of reconstruction from pure components."
---

KVP decomposition makes it possible to trace how the overall coupling level, vertex heterogeneity, and residual pair structure contribute to forest coefficients. We consider the toponomes of individual components and a joint toponome with three parameters. At grade two, mixed coefficients cancel; at higher grades, interactions appear. Zero row sums of P generate a family of identities among forest coefficients.

The exponential here supplies the forest representation to which reduction to types is applied. The general theory is given in [[Laplacian Exponential]], [[From Polyforms to Partitions]], and [[Forest Coefficients and the Laplacian Polynomial]]. This note asks what additional constraints and methods of analysis arise after KVP decomposition.

## The coupling table and its components

Let $n\ge3$, and let C be a real symmetric zero-diagonal table. Use [[KVP Decomposition of Pair Characteristics|the decomposition]]

$$
C=C_K+C_V+C_P,\qquad
c_{ij}=\mu+\frac{v_i+v_j}{n-2}+p_{ij}
$$

Here $\sum_i v_i=0$, $\sum_{j\ne i}p_{ij}=0$, and all diagonals are zero. In particular,

$$
\mu=\frac{\sum_{i<j}c_{ij}}{\binom n2},\qquad
v_i=\sum_{j\ne i}c_{ij}-(n-1)\mu
$$

The object being decomposed is the **coupling table C**, including zero entries on absent edges. Components of the resistance table R in [[The Second-Order Symmetric Potential and KVP Decomposition]] concern a different object.

Associate with C the Laplacian polyform and matrix:

$$
L(C)=\sum_{i<j}c_{ij}q_{ij},\qquad q_{ij}=[(a_i a_j)]^2,\qquad
\mathbf L(C)=\operatorname{diag}(C\mathbf1)-C
$$

The index X denotes a component: $L_X=L(C_X)$ and $\mathbf L_X=\mathbf L(C_X)$, where $X\in\{K,V,P\}$. The polyform uses an ordinary letter; the matrix uses boldface.

The algebraic statements require neither connectedness nor positivity. For $c_{ij}\ge0$, forest coefficients of the original graph are nonnegative, but individual KVP-components may have weights of both signs. They are not regarded as separate positive metric graphs.

## The exponential and a fixed forest representation

> [!info] The exponential and a fixed forest representation
> **Lemma 1.** In polyform algebra,
>
> $$
> \boxed{M(C)=\exp L(C)=M_KM_VM_P},\qquad M_X=\exp L_X
> \tag{1}
> $$
>
> For arbitrary real weights, we also have
>
> $$
> M(C)=\prod_{i<j}(e+c_{ij}q_{ij})
> \tag{2}
> $$

> [!note]- Proof
> **Proof.** Form multiplication is commutative, so the exponential of a sum factorizes. Since $q_{ij}^2=0$, we have $\exp(c_{ij}q_{ij})=e+c_{ij}q_{ij}$. Every series is finite: a product of grade above $n-1$ on boundaries vanishes. $\square$

Formula (1) concerns the polyform exponential. Matrix multiplication behaves differently; in particular, $\mathbf L_V$ and $\mathbf L_P$ generally do not commute.

In the expansion of (2), an edge set containing a cycle gives zero because its vectors are linearly dependent. Every remaining set is a spanning forest covering all n vertices, including isolated ones. If $\lambda(F)$ is its positive type, given by the grades of its nontrivial components, a tree on $r+1$ vertices contributes a part r.

> [!info] The exponential and a fixed forest representation
> **Definition.** The forest toponome of C, in polynomial notation, is
>
> $$
> \boxed{\mathcal T_C(\mathbf x)=\sum_{F\text{ a forest}}c(F)x_{\lambda(F)}
> =1+\sum_\lambda A_\lambda(C)x_\lambda}
> \tag{3}
> $$
>
> Here $c(F)=\prod_{ij\in E(F)}c_{ij}$, $x_\lambda=\prod_s x_{\lambda_s}$, and the empty forest contributes 1. Each forest is counted once. In this note, $A_\lambda$ denotes a scalar type coefficient; for example, $A_2=A_{(2)}$ and $A_{11}=A_{(1,1)}$.

This is the partition toponome in [[Vector and Vertex Normalizations of Toponomes|vector normalization]], extended to signed weights. Types are retained and vertex names are forgotten. The number n is stored separately.

The choice of representation matters. Formula (3) uses specifically the edge-factor expansion (2). Replacing a sum of forms by the tetrahedron identity, or choosing another factorization of the exponential before reduction, may change type coefficients. This limitation is discussed in [[Toponomes and Structural Identities]].

### Root weighting and the univariate polynomial

Choosing one root in each component counts a tree on $r+1$ vertices $r+1$ times. Thus the vertex, or rooted, reduction is

$$
\boxed{P_C(t)=\left.\mathcal T_C(\mathbf x)\right|_{x_r=(r+1)t^r}
=\det(I+t\mathbf L(C))}
\tag{4}
$$

This retains the notation $P_G(t)$ from [[en/Polynomial toponomes/Polynomial Toponomes|Polynomial Toponomes]]. The subscript C specifies the coupling table; the letter P in the polynomial name does not mean extraction of the P-component. For that component, write $P_{C_P}(t)$.

The determinant equality is [[Forest Coefficients and the Laplacian Polynomial#Summing minors and the Laplacian polynomial|the matrix-forest theorem]]. It extends to signed weights by polynomiality: both sides are polynomials in all $c_{ij}$ and agree on the open set of positive weights. The degree is at most $n-1$ and may decrease through degeneracy or cancellation.

## The overall level K and vertex heterogeneity V

All weights of the K-component equal $\mu$. A forest of grade k acquires the factor $\mu^k$, so $A_\lambda(C_K)$ is the number of forests of type $\lambda$ in the unit-weight complete graph multiplied by $\mu^k$. Its matrix is

$$
\mathbf L_K=\mu(nI-\mathbf1\mathbf1^{\mathsf T})=n\mu J,\qquad
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

On $\mathbf1^\perp$, this is a scalar operator. Consequently,

$$
\boxed{P_{C_K}(t)=(1+n\mu t)^{n-1}}
\tag{5}
$$

> [!info] The overall level K and vertex heterogeneity V
> **Corollary 1 (separating the K-background).** Let $B=\nu C_V+\pi C_P$ and $a=1+n\mu\kappa t$. Then
>
> $$
> \boxed{P_{\kappa C_K+B}(t)=a^{n-1}P_B(t/a)}
> \tag{6}
> $$

> [!note]- Proof
> **Proof.** On $\mathbf1^\perp$, $I+t\mathbf L(\kappa C_K+B)=aI+t\mathbf L(B)$. Factor a out of the determinant of dimension $n-1$. The direction $\mathbf1$ contributes a factor 1. The equality is first obtained for $a\ne0$; after denominators cancel, the right side is a polynomial, and the identity holds for all t. $\square$

Thus K supplies a common spectral shift, while V and P determine deviations from it. Formula (6) does not split V and P into independent spectra.

V is determined by the zero-sum vector $(v_1,\ldots,v_n)$. Permuting its coordinates merely relabels vertices. Each $A_\lambda(C_V)$ is therefore a symmetric homogeneous polynomial in v of degree equal to the type's grade. This does not assert that the toponome recovers the full collection of $v_i$.

## Grade two without mixed coefficients

Two distinct edges either share a vertex, giving type $(2)$, or are disjoint, giving type $(1,1)$. Write

$$
w=\sum_{i<j}c_{ij},\qquad d_i=\sum_{j\ne i}c_{ij},\qquad
N_2=\sum_{i<j}c_{ij}^2
$$

> [!info] Grade two without mixed coefficients
> **Lemma 2.**
>
> $$
> \boxed{A_2(C)=\frac12\sum_i d_i^2-N_2,\qquad
> A_{11}(C)=\frac12w^2-\frac12\sum_i d_i^2+\frac12N_2}
> \tag{7}
> $$

> [!note]- Proof
> **Proof.** The sum of products over adjacent edge pairs is $\frac12\sum_i(d_i^2-\sum_{j\ne i}c_{ij}^2)$, giving the first formula. The sum over all unordered pairs of distinct edges is $(w^2-N_2)/2$. Subtracting the adjacent pairs gives the second formula. $\square$

Put $V_2=\sum_i v_i^2$ and $P_2=\|C_P\|_0^2=\sum_{i<j}p_{ij}^2$. Formula (7) gives

| Component | $A_2$ | $A_{11}$ |
| --- | ---: | ---: |
| K | $3\binom n3\mu^2$ | $3\binom n4\mu^2$ |
| V | $\dfrac{n-4}{2(n-2)}V_2$ | $-\dfrac{n-3}{2(n-2)}V_2$ |
| P | $-P_2$ | $P_2/2$ |

A binomial coefficient is zero if its lower index exceeds n. For K, this counts three trees on each triple and three matchings on each four-element subset. For V, use $w=0$, $d=v$, and $N_2=V_2/(n-2)$. For P, $w=0$ and $d=0$.

> [!info] Grade two without mixed coefficients
> **Corollary 2.** For $\kappa C_K+\nu C_V+\pi C_P$, both grade-two coefficients are sums of pure contributions:
>
> $$
> A_\lambda(\kappa C_K+\nu C_V+\pi C_P)
> =\kappa^2A_\lambda(C_K)+\nu^2A_\lambda(C_V)+\pi^2A_\lambda(C_P),\qquad
> \lambda\in\{(2),(1,1)\}
> \tag{8}
> $$

> [!note]- Proof
> **Proof.** Coefficient orthogonality splits $N_2$ into three coefficient sums of squares. The row sums of K are constant, those of V form a zero-sum vector, and those of P vanish. Thus $\sum_i d_i^2$ has no mixed terms. Only K contributes to w. Apply (7). $\square$

This statement concerns two scalar forest sums. It does not imply $L_KL_V=0$, $L_KL_P=0$, or $L_VL_P=0$. Coefficient orthogonality is not PMG metric orthogonality and does not eliminate arbitrary nonlinear interactions.

### Which KVP data the ordinary toponome already contains

The first coefficient is $A_1=w$. Write $D_2=\sum_i d_i^2$. Solving (7) gives

$$
N_2=w^2-2A_2-2A_{11},\qquad
D_2=2w^2-2A_2-4A_{11}
$$

For known n, this recovers

$$
\begin{aligned}
\|C_K\|_0^2&=\frac{w^2}{\binom n2}\\
\|C_V\|_0^2&=\frac{D_2-4w^2/n}{n-2}\\
\|C_P\|_0^2&=N_2-\|C_K\|_0^2-\|C_V\|_0^2
\end{aligned}
\tag{9}
$$

The three coefficient sums of squares therefore provide no additional information beyond the first two grades of the partition toponome. KVP gives these data a component interpretation. This statement does not concern the univariate $P_C(t)$ alone: its second coefficient combines the types as $3A_2+4A_{11}$.

## Balance identities for a pure P-component

P has zero row sums, so $\mathbf L_P=-C_P$, $\operatorname{diag}\mathbf L_P=0$, and $\operatorname{tr}\mathbf L_P=0$. A nonzero symmetric $\mathbf L_P$ has eigenvalues of both signs on $\mathbf1^\perp$. A nonzero P-table necessarily contains coefficients of both signs: a row consisting entirely of nonnegative or entirely of nonpositive entries can have zero sum only if every entry is zero. Thus a nonzero pure P-component is not a coupling table of a graph with nonnegative weights.

The sum of all edge weights is zero, so $A_1(C_P)=0$. Nevertheless, the first grade of the exponential itself is $L_P$ and is generally nonzero. Cancellation occurs after vertex names are forgotten.

All coefficients $A_\lambda$ in the following discussion refer to $C_P$.

> [!info] Balance identities for a pure P-component
> **Theorem 1.** For every $k\ge2$,
>
> $$
> \boxed{A_{2,1^{k-2}}=-kA_{1^k}}
> \tag{10}
> $$
>
> The coefficient of a type impossible on n vertices is taken to be zero. Balance here means precisely zero row sums of the signed symmetric P-table.

> [!note]- Proof
> **Proof.** Enumerate matchings M with $k-1$ edges. Let $p(M)$ be the product of their weights, and let $U(M)$ be the set of free vertices. Zero row sums give
>
> $$
> 0=\sum_{M:\,|M|=k-1}p(M)\sum_{i\in U(M)}\sum_{j\ne i}p_{ij}
> $$
>
> Split the added edges $ij$ into two cases.
>
> 1. If j is free, the result is a matching of k edges. Each result is counted $2k$ times: any of its k edges may be removed, and either endpoint chosen as i. The contribution is $2kA_{1^k}$.
> 2. If j is occupied, the new edge attaches to one edge of M. The result has one three-vertex component and $k-2$ separate edges, hence type $(2,1^{k-2})$. Each result is counted twice: remove either edge of the three-vertex tree; the freed endpoint uniquely determines i. The contribution is $2A_{2,1^{k-2}}$.
>
> There are no other cases. The two contributions sum to zero, proving (10). Positivity of weights was not used. $\square$

![[Balance of P-component forest coefficients.svg]]

*For grade three, the initial matching has two edges. Adding an edge between free vertices gives type $(1,1,1)$ with multiplicity 6; attaching it to an occupied vertex gives type $(2,1)$ with multiplicity 2. Summing over all initial matchings yields $A_{21}=-3A_{111}$. Color indicates the edge's role in the counting argument, not the sign of its weight.*

Type $1^k$ requires $2k$ vertices, while type $(2,1^{k-2})$ requires $2k-1$. Thus for $n=2k-1$, the second type exists, but its total weight must vanish. In particular, $A_{21}=0$ on five vertices. This is cancellation of weights of different forests, not absence of the forests themselves.

## Example: the P-component of a five-vertex path

For the unit-weight path $a-b-c-d-e$, $\mu=2/5$ and $v=(-3,2,2,2,-3)/5$. Its P-component in vertex order $a,b,c,d,e$ is

$$
C_P=\frac13\begin{pmatrix}
0&2&-1&-1&0\\
2&0&1&-2&-1\\
-1&1&0&1&-1\\
-1&-2&1&0&2\\
0&-1&-1&2&0
\end{pmatrix}
$$

The row sums are zero and $P_2=2$. Direct enumeration of forests with these weights gives

$$
\boxed{\mathcal T_{C_P}(\mathbf x)=1-2x_2+x_1^2-\frac2{27}x_3+\frac19x_4}
\tag{11}
$$

There is no linear term, and the grade-two coefficients are $-2$ and 1. The term $x_2x_1$ is absent by Theorem 1. Root weighting gives

$$
\boxed{P_{C_P}(t)=1-2t^2-\frac8{27}t^3+\frac59t^4}
\tag{12}
$$

Checking through $\det(I+t\mathbf L_P)$ is independent of grouping forests by type. Negative coefficients are admissible: this is the polynomial of a signed component.

For comparison, grade two of the full path splits as follows:

| Coefficient | K | V | P | Full path |
| --- | ---: | ---: | ---: | ---: |
| $A_2$ | $24/5$ | $1/5$ | $-2$ | $3$ |
| $A_{11}$ | $12/5$ | $-2/5$ | $1$ | $3$ |

Both totals count the corresponding two-edge forests of the original path, enumerated in [[From Polyforms to Partitions#The six two-edge forests|the path example]]. Pure contributions do not count subsets of those forests: the components introduce other vertex pairs and signed weights.

## The joint KVP toponome and mixed contributions

> [!info] The joint KVP toponome and mixed contributions
> **Definition.** The joint KVP toponome of a fixed table C is
>
> $$
> \boxed{\mathcal T_{KVP}(\mathbf x;\kappa,\nu,\pi)
> =\mathcal T_{\kappa C_K+\nu C_V+\pi C_P}(\mathbf x)}
> \tag{13}
> $$

The parameters $\kappa,\nu,\pi$ retain the origin of each edge factor. The coefficient of a type of grade k becomes a homogeneous polynomial of degree k in these parameters. For example, a term $\nu\pi^2$ collects contributions with one factor from V and two from P. For a graph interpretation of a particular parameter choice, nonnegativity of the resulting weights must be checked separately.

The ordinary toponome is obtained at $(\kappa,\nu,\pi)=(1,1,1)$, while pure toponomes occur at $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$. The coefficient of type $(n-1)$ is the spanning-tree polynomial $\Theta(\kappa,\nu,\pi)$ whose derivatives were studied in [[KVP Components and Metric Graph Parameters#The spanning-tree coefficient and matching Foster contributions|the decomposition of spanning-tree sensitivities]]. Here all intermediate forest types are retained as well.

In general,

$$
\mathcal T_C\ne\mathcal T_{C_K}\mathcal T_{C_V}\mathcal T_{C_P}
$$

After reduction, vertex names are lost. The ordinary product of three polynomials no longer determines which edges intersect, join components, or form a cycle. The components occupy the same vertex set, so the product rule for toponomes of disjoint graphs does not apply.

### Mixed terms of grade three

For the path $P_5$, on the slice $\nu=0$, formulas (6) and (12) give the rooted reduction

$$
P_{\kappa C_K+\pi C_P}(t)
=a^4-2\pi^2t^2a^2-\frac8{27}\pi^3t^3a+\frac59\pi^4t^4,\qquad a=1+2\kappa t
$$

Consequently,

$$
[t^3]P_{\kappa C_K+\pi C_P}(t)
=32\kappa^3-8\kappa\pi^2-\frac8{27}\pi^3
\tag{14}
$$

The term $-8\kappa\pi^2$ shows interaction between K and P. It occurs despite the vanishing of mixed scalar grade-two coefficients. On this slice, the mixed contribution is determined by the simple K-shift; interaction between V and P requires additional data.

## Why three pure toponomes are insufficient

Consider two complete graphs on four vertices with positive conductances. The table also lists their common K- and V-components and the P-component of the first graph:

| Pair | $C_+$ | $C_-$ | Common $C_K$ | Common $C_V$ | $C_{P,+}$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $ab$ | $3$ | $1$ | $3$ | $-1$ | $1$ |
| $ac$ | $2$ | $4$ | $3$ | $0$ | $-1$ |
| $ad$ | $2$ | $2$ | $3$ | $-1$ | $0$ |
| $bc$ | $4$ | $4$ | $3$ | $1$ | $0$ |
| $bd$ | $2$ | $4$ | $3$ | $0$ | $-1$ |
| $cd$ | $5$ | $3$ | $3$ | $1$ | $1$ |

Both tables have degrees $(7,9,11,9)$, so $\mu=3$ and $v=(-2,0,2,0)$. Their P-components are opposite: $C_{P,-}=-C_{P,+}$.

The P-component has four nonzero edges. One-edge and three-edge contributions cancel, four adjacent pairs contribute $-1$ each, and two disjoint pairs contribute $1$ each. Thus for both signs,

$$
\mathcal T_{C_{P,+}}=\mathcal T_{C_{P,-}}=1-4x_2+2x_1^2
$$

The K- and V-tables are literally identical, so their toponomes coincide too. Nevertheless, the original graphs have different spanning-tree coefficients:

$$
\begin{aligned}
\tau(C_+)&=\det\begin{pmatrix}9&-4&-2\\-4&11&-5\\-2&-5&9\end{pmatrix}=398\\
\tau(C_-)&=\det\begin{pmatrix}9&-4&-4\\-4&11&-3\\-4&-3&9\end{pmatrix}=394
\end{aligned}
$$

These are principal Laplacian minors obtained by deleting row and column a. The full toponomes are

$$
\mathcal T_{C_+}=1+18x_1+104x_2+27x_1^2+398x_3
$$

$$
\mathcal T_{C_-}=1+18x_1+104x_2+27x_1^2+394x_3
$$

The distinction is explicit in the joint toponome. For each graph, the parameters refer to its own KVP-components. Directly expanding the same cofactor with parameters gives

$$
\boxed{A_3^\pm(\kappa,\nu,\pi)
=432\kappa^3-24\kappa\nu^2-12\kappa\pi^2\pm2\nu^2\pi}
\tag{15}
$$

At $(1,1,1)$, this gives $396\pm2$. Pure slices cannot see the sign of the mixed term $\nu^2\pi$.

> [!info] Why three pure toponomes are insufficient
> **Corollary 3.** In general, the three pure toponomes of K, V, and P determine neither the full toponome nor the spanning-tree coefficient of the original positively weighted graph. The joint toponome retains information about interactions that the pure slices lose.
>
> This example does not establish the distinguishing power of the joint toponome among graphs with identical full ordinary toponomes: here the ordinary toponomes already differ. That remains a separate question.

## What carries over to balanced graphs

For a balanced arc table, $C=C_K+C_V+C_P+C_O$. U is absent, but V generally remains. By [[The Laplacian Exponential of a Balanced Graph#Factorization by bilinear terms|commutativity of bilinear forms]],

$$
\exp L=\exp L_K\,\exp L_V\,\exp L_P\,\exp L_O
$$

Thus the exponential of a balanced graph and its factorization are not open questions. Forest reduction requires a consistent directed representation and the normalizations from [[Toponomes of Balanced Graphs and Directed Forests]], rather than replacing oriented couplings with undirected ones.

For a pure O-component, $\mathbf L_O=-C_O$ is skew-symmetric. Its rooted polynomial is even:

$$
\det(I+t\mathbf L_O)=\det((I+t\mathbf L_O)^{\mathsf T})
=\det(I-t\mathbf L_O)
$$

This is a statement about a matrix polynomial. It does not imply that odd grades of the polyform exponential itself vanish; its first grade is $L_O$.

The symmetric balance identities (10) and the conjecture of their completeness do not automatically extend to directed forest types. An arbitrary unbalanced table with a U-component requires additional conventions about representation and metric model. The open extension concerns analysis of types and interactions of oriented components, not redefining the already constructed exponential of a balanced graph.

## Completeness of balance relations and open questions

Let $\mathfrak p(k)$ be the number of partitions of k. For fixed n and k, let $r_{n,k}$ be the dimension of the linear span of vectors

$$
\bigl(A_\lambda(C_P)\bigr)_{\lambda\vdash k}
$$

as P ranges over all P-tables on n vertices. This is a linear-span dimension; the coefficients themselves are polynomials in the weights, and their set of value vectors need not be a linear space.

For $n\ge2k$, all types of grade k are admissible. Theorem 1 gives $r_{n,k}\le\mathfrak p(k)-1$.

**Working conjecture.** For every $k\ge2$ and $n\ge2k$,

$$
r_{n,k}=\mathfrak p(k)-1
\tag{16}
$$

In other words, the balance identity found above generates all universal linear dependencies of that grade. This is not a conjecture that nonlinear dependencies are absent.

Exact computational witnesses have been obtained for small grades:

| Grade k | Number of vertices | $\mathfrak p(k)$ | Rank of the coefficient-vector set |
| --- | ---: | ---: | ---: |
| $2$ | $4$ | $2$ | $1$ |
| $3$ | $6$ | $3$ | $2$ |
| $4$ | $8$ | $5$ | $4$ |

The [rank verification data](P%20toponome%20rank%20verification.json) provide integer P-matrices, the order of types, and their coefficient vectors. Coefficients were obtained by forest enumeration without using (10); ranks were computed in exact rational arithmetic. Together with the proved upper bound, these examples establish equality for the indicated n. Adding isolated vertices preserves P and all forest coefficients, so equality extends to every $n\ge2k$ for $k=2,3,4$. A general proof for arbitrary k is not yet available.

Other open problems include classifying higher mixed coefficients, interpreting them, and comparing the distinguishing power of ordinary, pure, and joint toponomes. The oriented extension with O and U requires a separate study. Vanishing mixed grade-two terms do not automatically resolve any of these questions.

## Checks and connections

The grade-two formulas and the balance identity are proved by direct counting. The toponome of the path's P-component, mixed coefficients, and the example with spanning-tree coefficients 398 and 394 were checked by forest enumeration. Rooted polynomials were computed independently through sums of principal Laplacian minors. General formulas were additionally checked on eight signed tables with 3-6 vertices; rank verification is described separately above.

This note is based on the author's PMG research. The definitions and general results used here are available in [[KVP Decomposition of Pair Characteristics]], [[From Polyforms to Partitions]], [[Toponomes and Structural Identities]], [[Vector and Vertex Normalizations of Toponomes]], [[Forest Coefficients and the Laplacian Polynomial]], and [[Toponomes of Balanced Graphs and Directed Forests]].

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
