---
title: The Second-Kind Algebra on Partitions
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: second-kind-algebra-on-partitions
lang: en
description: "Partition multiplication through partial matchings of components, its connection with symmetric functions, and powers of the part of weight one in terms of combinatorial potentials of the second kind."
order: 3
---

The toponome in the [[From Polyforms to Partitions|note on polyform reduction]] is a linear combination of integer partitions. To multiply such combinations, we need to define the product of basis types and explain its coefficients.

This note introduces **the second-kind algebra on partitions**. Its product enumerates partial matchings between the components of two factors: matched components merge by adding their weights, while unmatched components remain unchanged. The designation “second-kind” refers to the algebra. It reflects the fact that the coefficients in the expansion of $(1)^k$ are [[Partitions and the Combinatorial Potential of the Second Kind|combinatorial potentials of the second kind]]; grouping them by the number of parts gives Stirling numbers of the second kind.

This name is used as a PMG term. Below, we establish a correspondence with the standard algebra of symmetric functions in the augmented monomial basis. Applying the product to polyforms requires a separate correspondence with operations on named components.

## Basis partitions and the unit

Consider the real vector space $\mathcal A$ with a basis consisting of all integer partitions of positive integers and the empty partition. Its elements are finite sums

$$
T=\sum_\lambda c_\lambda\lambda
$$

For a basis partition

$$
\lambda=(a_1,\ldots,a_r),\qquad a_i\geqslant1
$$

set

$$
\#\lambda=r,\qquad w(\lambda)=a_1+\cdots+a_r
$$

The order of parts is disregarded. When listing types, we place larger parts before smaller ones. Repetition is denoted by an exponent inside the parentheses:

$$
(2,1,1)=(2,1^2),\qquad (1,1)=(1^2)
$$

Denote the empty partition by $1$; its weight and number of parts are zero. The symbol $1$ differs from the one-part partition $(1)$ of weight $1$. We write $*$ for the product in $\mathcal A$ and use an ordinary exponent for a repeated product:

$$
(1)*(1)=(1)^2
$$

Thus, $(1^2)$ is a single basis type, whereas $(1)^2$ is a product to be expanded in the basis.

No bound on the number of vertices is imposed here. If $\lambda$ is interpreted as the positive type of a form on $n$ vertices, the conditions in the [[From Polyforms to Partitions#Singleton vertices and type parameters|definition of type parameters]] also apply: for $k=w(\lambda)$, we have $k+r\leqslant n$, the full number of components is $m=n-k$, and the number of singleton vertices is $\ell=n-k-r$. In the abstract algebra, $r$ counts only the positive parts displayed; no value of $n$ is specified.

## The product through partial matchings

Let

$$
\lambda=(a_1,\ldots,a_r),\qquad
\mu=(b_1,\ldots,b_s)
$$

Temporarily distinguish occurrences of parts by indices, even when their values coincide.

**Definition.** A partial matching of components is a set of index pairs $H\subseteq\{1,\ldots,r\}\times\{1,\ldots,s\}$ in which each index of either factor occurs at most once. Equivalently, we select some components from each factor and choose a bijection between the selected components.

For each such $H$, construct a partition $\nu_H$:

- replace each pair $(i,j)\in H$ by a single part $a_i+b_j$;
- leave every unmatched part unchanged;
- forget the temporary indices and sort the parts.

**Definition.** The product of basis partitions is

$$
\boxed{
\lambda*\mu=\sum_H\nu_H
}
$$

The sum includes the empty matching. Extend the product to linear combinations by bilinearity. Identical resulting types are collected: their coefficients count the distinct matchings that produce the same type.

In particular, two one-part factors admit two possibilities: keep the parts separate or merge them:

$$
(a)*(b)=(a,b)+(a+b)
$$

For two factors $(1^2)$, we obtain

$$
\boxed{
(1^2)*(1^2)=(1^4)+4(2,1^2)+2(2^2)
}
$$

The figure shows all the matchings contributing to the coefficients of this expansion.

![Seven partial matchings of two pairs of components: one with no pairs, four with one pair, and two with two pairs](Partial%20matchings%20of%20partition%20components.svg)

*Figure 1. The product $(1^2)*(1^2)$. Blue circles represent occurrences of parts in the first factor, and orange circles represent those in the second. Each circle has weight $1$; a line matches two parts. The temporary labels $a_1,a_2,b_1,b_2$ distinguish the matchings and are forgotten in the resulting type. This is a diagram of an operation on parts, rather than a drawing of the edges of the original graph.*

The empty matching gives $(1^4)$. A single pair can be chosen in $2\cdot2=4$ ways, each giving $(2,1^2)$. Two pairs can be formed in two ways, both giving $(2^2)$.

If the first factor has $r$ parts and the second has $s$, the number of matchings with exactly $q$ pairs is $\binom rq\binom sq q!$. Hence the sum of the coefficients in the product of two basis partitions is

$$
\sum_{q=0}^{\min(r,s)}\binom rq\binom sq q!
$$

This number depends on the numbers of parts in the factors. Its distribution among the resulting types also depends on the values of the parts.

## Why this defines an algebra

**Theorem.** The product is well-defined on unordered types, commutative, and associative. The empty partition $1$ is its unit. The weights of the factors add.

> [!note]- Proof
> **Proof.** Reindexing occurrences of parts changes the matching indices while preserving all resulting types and their multiplicities. Thus the result is independent of the temporary indices. Exchanging the factors reverses every matched pair, proving commutativity. The empty factor has no parts to match, leaving a single possibility that preserves the other factor.
>
> For associativity, temporarily mark the parts of three factors with three different colors and individual indices. Both parenthesizations enumerate partitions of these occurrences into groups containing at most one part of each color. Each group produces a part whose weight is the sum of the weights in that group.
>
> In $(\lambda*\mu)*\eta$, a final group uniquely determines its intermediate group: remove the part from the third factor, if present. A group containing only a part of the third factor is absent at the intermediate step. Conversely, two successive matching operations uniquely determine the final grouping. The same holds for $\lambda*(\mu*\eta)$. Thus both expressions enumerate the same groupings exactly once. After the indices are forgotten, the coefficients of identical types also agree. Bilinearity extends the equality to arbitrary elements of $\mathcal A$.
>
> Merging parts adds their weights without changing the total. Thus every type in $\lambda*\mu$ has weight $w(\lambda)+w(\mu)$. $\square$

The algebra is graded by weight:

$$
\mathcal A=\bigoplus_{k\geqslant0}\mathcal A_k,
\qquad
\mathcal A_k*\mathcal A_l\subseteq\mathcal A_{k+l}
$$

Here $\mathcal A_k$ is spanned by the partitions of weight $k$, and $\dim\mathcal A_k=p(k)$ is the number of integer partitions of $k$. If $q$ pairs are matched, the resulting type has $r+s-q$ parts. The number of parts therefore does not define an analogous grading: a single product can contain types with different numbers of parts.

## Multiplication by one part

### The rule for a part of weight one

The right factor $(1)$ has one component. It either remains separate or is matched with one of the $r$ components of the left factor. Hence

$$
\boxed{
(a_1,\ldots,a_r)*(1)
=(a_1,\ldots,a_r,1)
+\sum_{i=1}^r(a_1,\ldots,a_i+1,\ldots,a_r)
}
$$

For example,

$$
(1)*(1)=(1^2)+(2)
$$

$$
(1^2)*(1)=(1^3)+2(2,1)
$$

$$
(2,1)*(1)=(2,1^2)+(3,1)+(2^2)
$$

The coefficient $2$ in the second equality comes from two possible matches with equal parts. It does not double the weight of the merged component.

### Passing to a part of weight two

The first equality gives

$$
(2)=(1)^2-(1^2)
$$

Thus, for any $\lambda$,

$$
\lambda*(2)=(\lambda*(1))*(1)-\lambda*(1^2)
$$

In the first term, two successively distinguishable ones are added. In the second, these ones belong to different components of a single factor, so the matching rule keeps them in different final components. Subtraction leaves precisely the cases in which both ones end up together: they either form a new part of weight $2$ or both join one original part. Consequently,

$$
\boxed{
(a_1,\ldots,a_r)*(2)
=(a_1,\ldots,a_r,2)
+\sum_{i=1}^r(a_1,\ldots,a_i+2,\ldots,a_r)
}
$$

For example, applying the rule for $(1)$ successively gives

$$
(1^2)*(1)^2=(1^4)+5(2,1^2)+2(3,1)+2(2^2)
$$

Subtracting the product $(1^2)*(1^2)$ computed above yields

$$
(1^2)*(2)=(2,1^2)+2(3,1)
$$

This calculation uses $(2)=(1)^2-(1^2)$ together with the general matching rule, which determines the terms in $\lambda*(1^2)$.

### An arbitrary one-part component

The same choice - keep the new part separate or match it with an existing part - gives, for any $b\geqslant1$,

$$
\boxed{
(a_1,\ldots,a_r)*(b)
=(a_1,\ldots,a_r,b)
+\sum_{i=1}^r(a_1,\ldots,a_i+b,\ldots,a_r)
}
$$

For example,

$$
(2,1)*(2)=(2^2,1)+(4,1)+(3,2)
$$

The part $(b)$ is added as a whole. It differs from the product $(1)^b$, which is itself a sum of different types.

## Computing an arbitrary product

The general definition allows us to enumerate all partial matchings directly. There is also a recursive procedure using only multiplication by one part.

Let $\mu=(b_1,\ldots,b_s)$, with $s\geqslant2$, and let $\mu'=(b_1,\ldots,b_{s-1})$. Write $\mu'_j$ for the partition obtained by replacing $b_j$ with $b_j+b_s$ in $\mu'$. Then

$$
\mu'*(b_s)=\mu+\sum_{j=1}^{s-1}\mu'_j
$$

By associativity and bilinearity,

$$
\boxed{
\lambda*\mu
=(\lambda*\mu')*(b_s)
-\sum_{j=1}^{s-1}\lambda*\mu'_j
}
$$

All the right factors $\mu'$ and $\mu'_j$ have fewer parts than $\mu$. Together with the rule for $(b)$ and the unit, this formula therefore gives a finite algorithm for computing any product. Repeated occurrences of $\mu'_j$ are counted with their multiplicities.

For example, $(2)*(2)=(2^2)+(4)$, so

$$
\lambda*(2^2)=(\lambda*(2))*(2)-\lambda*(4)
$$

For $\lambda=(1^2)$, the matching rule gives

$$
(1^2)*(2^2)=(2^2,1^2)+4(3,2,1)+2(3^2)
$$

There is one matching with no pairs, four with one pair, and two with two pairs. Despite the subtractions in the recursive algorithm, the coefficients in a product of basis types are always nonnegative: they count matchings.

## Powers of the part of weight one and combinatorial potentials

**Lemma.** For every $k\geqslant0$,

$$
\boxed{
(1)^k=\sum_{\lambda\vdash k}s_2(\lambda)\,\lambda
}
$$

Here $\lambda\vdash k$ means that $\lambda$ ranges over all integer partitions of weight $k$. For $\lambda=(a_1,\ldots,a_r)$ with part multiplicities $\mu_j$, we use the abbreviation

$$
s_2(\lambda)=s_2([a_1,\ldots,a_r])
=\frac{k!}{[a_i!]!\,[\mu_j!]!}
$$

This is the [[Partitions and the Combinatorial Potential of the Second Kind#The combinatorial potential of the second kind|combinatorial potential of the second kind]] introduced for a numerical collection. At $k=0$, only the empty partition occurs; its potential and the zeroth power both equal $1$.

**Proof.** Temporarily give the $k$ factors $(1)$ distinct labels. When the next factor is multiplied in, its label either forms a new block or joins an existing block. The rule for multiplication by $(1)$ enumerates these possibilities.

Every set partition of the labels arises exactly once. Removing the last label uniquely recovers the preceding partition and the step taken; if its block was a singleton, the entire block is removed. Forgetting the labels leaves the block sizes, namely the integer type $\lambda$. Its coefficient is the number of set partitions of that type, which is $s_2(\lambda)$. $\square$

The first powers are

$$
(1)^2=(2)+(1^2)
$$

$$
(1)^3=(3)+3(2,1)+(1^3)
$$

$$
(1)^4=(4)+4(3,1)+3(2^2)+6(2,1^2)+(1^4)
$$

Every type of weight $k$ occurs with a positive coefficient. Thus the expansion may be called the **partition spectrum of the power** $(1)^k$, provided that “spectrum” explicitly means the collection of types and their coefficients. This is a combinatorial use of the word; no operator or eigenvalues are introduced here.

Grouping by the number of parts gives

$$
\sum_{\substack{\lambda\vdash k\\\#\lambda=r}}s_2(\lambda)=S(k,r),
\qquad
\sum_{\lambda\vdash k}s_2(\lambda)=B_k
$$

Here $S(k,r)$ is a Stirling number of the second kind, and $B_k$ is a Bell number. For example, at $k=4$:

| Number of parts $r$ | Contributions of the types | $S(4,r)$ |
| --- | --- | ---: |
| $1$ | $s_2((4))=1$ | $1$ |
| $2$ | $s_2((3,1))+s_2((2^2))=4+3$ | $7$ |
| $3$ | $s_2((2,1^2))=6$ | $6$ |
| $4$ | $s_2((1^4))=1$ | $1$ |

The sum is $B_4=15$. This connection motivates the name of the algebra.

The proof partitions the labels of the factors, not graph vertices. If the parts of $\lambda$ are later interpreted as grades of form components, the coefficient $s_2(\lambda)$ does not automatically become the number of vertex partitions of that type. This distinction agrees with the [[Combinatorial Potentials in Symmetric Polyforms|use of potentials in SPFs]].

## Polynomial notation and symmetric functions

### A monomial as a notation for a type

In the [[From Polyforms to Partitions#Partitions and polynomials in several variables|polynomial notation for a toponome]], each type corresponds to one monomial:

$$
\lambda=(a_1,\ldots,a_r)
\quad\longleftrightarrow\quad
x_\lambda=x_{a_1}\cdots x_{a_r}
$$

This linear correspondence preserves types. Ordinary multiplication of monomials concatenates the lists of parts, whereas $*$ also accounts for their matchings. For example,

$$
x_1x_1=x_1^2,
\qquad
x_1*x_1=x_1^2+x_2
$$

Transporting $*$ to these polynomial expressions gives a convenient form of the one-part rule. For a polynomial $F$ in several variables,

$$
F*x_b=x_bF+\sum_{j\geqslant1}x_{j+b}\frac{\partial F}{\partial x_j}
$$

Only finitely many terms are nonzero. The first term adds a separate part; the derivative selects one occurrence of a part $j$, accounting for its multiplicity, and the factor $x_{j+b}$ replaces the selected part with the merged one.

### Realization by ordinary multiplication of symmetric functions

There is another representation in which $*$ becomes ordinary multiplication. Take formal variables $y_1,y_2,\ldots$ and assign to a type the function

$$
\Psi(\lambda)=\widetilde m_\lambda(\mathbf y)
=\sum_{\substack{i_1,\ldots,i_r\geqslant1\\i_1,\ldots,i_r\ \text{pairwise distinct}}}
y_{i_1}^{a_1}\cdots y_{i_r}^{a_r}
$$

The empty type corresponds to $1$. We use the algebra of symmetric functions of bounded degree in a countable set of variables; no analytic convergence is required. With only $N$ variables, the same formula defines a symmetric polynomial. Taking $N\geqslant k$ suffices to preserve all types of weight $k$.

The ordinary monomial symmetric function $m_\lambda$ lists each distinct monomial once. Here, assignments of indices to separate occurrences of equal parts are distinguished. Thus

$$
\widetilde m_\lambda=[\mu_j!]!\,m_\lambda
$$

This is the standard basis of **augmented monomial symmetric functions**, defined, for example, in [1, §2]. The normalization factor accounts for permutations of equal parts:

$$
\widetilde m_{(1^2)}=\sum_{i\ne j}y_i y_j
=2\sum_{i<j}y_i y_j
$$

**Proposition.** The map $\Psi$ is an isomorphism from $\mathcal A$ onto the real algebra of symmetric functions.

**Proof.** In the product $\widetilde m_\lambda\widetilde m_\mu$, the indices within each factor are distinct. Index coincidences between the factors therefore form a partial matching: an index in the first factor can coincide with at most one index in the second. Coincident indices add their exponents. Grouping all possible coincidences gives

$$
\widetilde m_\lambda\widetilde m_\mu
=\sum_H\widetilde m_{\nu_H}
=\Psi(\lambda*\mu)
$$

The functions $\widetilde m_\lambda$ form a basis because they are obtained from the monomial basis by multiplication by the nonzero numbers $[\mu_j!]!$. Hence $\Psi$ is a linear bijection that preserves products. $\square$

In particular, $(b)$ corresponds to the power sum $p_b=\sum_i y_i^b$. The lemma on powers of $(1)$ becomes the expansion of $p_1^k$ in the basis $\widetilde m_\lambda$. The proposed name thus highlights a basis useful in PMG and the combinatorial meaning of the coefficients of a known algebra.

## Scope of application to toponomes

The product $*$ is defined on all formal linear combinations of types, so it can also be applied to toponomes. Their coefficients are sufficient for this operation. However, equating the product of toponomes with the toponome of a product of particular polyforms requires additional conditions.

A partial matching selects which components of the two factors merge and sums all admissible possibilities according to the given rule. For particular forms, the intersections of their vertex sets are already fixed. The types alone do not specify these intersections. Compatibility between the operation on types and polyform multiplication requires a graph realization of the matchings and conditions for its applicability.

The [[Toponomes and Structural Identities#A criterion for representation-independent reduction|dependence of reduction on the chosen representation]] also remains. Introducing a product on free types adds no relations between them and does not remove the obstruction illustrated by the tetrahedron identity.

**Checks.** In addition to the general proofs, independent enumeration of set partitions and recursive computation of $(1)^k$ were performed for $0\leqslant k\leqslant8$, with comparison against the formula for $s_2$ for every type. The example products were also checked by ordinary multiplication of the corresponding symmetric polynomials in sufficiently many variables.

## Sources and connections

This note is based on the author's research within PMG. The name “the second-kind algebra on partitions” and the term “combinatorial potential” are used in the senses defined here. The connection with the standard algebra of symmetric functions is established by the explicit map $\Psi$.

1. Logan Crew, Sophie Spirkl. [A complete multipartite basis for the chromatic symmetric function](https://arxiv.org/abs/2009.14141), arXiv:2009.14141, version 2, 2021. §2: the monomial basis, power sums, and augmented monomial symmetric functions.
2. NIST Digital Library of Mathematical Functions. [§26.8, Set Partitions: Stirling Numbers](https://dlmf.nist.gov/26.8): the standard definition of Stirling numbers of the second kind.
3. [[Partitions and the Combinatorial Potential of the Second Kind]]  -  the definition of $s_2$, its factorial formula, and its connection with Stirling and Bell numbers.
4. [[From Polyforms to Partitions]]  -  positive types, the toponome of a chosen representation, and notation using polynomials in several variables.
5. [[Toponomes and Structural Identities]]  -  conditions for representation-independent reduction.
