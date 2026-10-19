---
title: "Symmetric Polyforms of the Complete Graph"
date: 2026-10-19
updated: 2026-10-19
revision: 2
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: symmetric-polyforms-of-the-complete-graph
lang: en
description: "The Laplacian exponential of the complete graph, a derivation of Cayley's formula, an expansion by forest type, and a detailed K5 example."
order: 4
---

Symmetric polyforms (SPFs) give a compact representation of the exponential of the complete graph. With unit conductances, its Laplacian is the principal symmetric polyform (principal SPF) of grade one. The rules in [[Products and Powers of Symmetric Polyforms]] therefore immediately determine all grades of its exponential.

This exponential has two useful representations: in terms of principal SPFs and in terms of sums of partition forms of different types. The first gives a compact expression and the formula for the number of spanning trees. The second retains information about the sizes of forest components. Comparing them yields a numerical identity for the coefficients of the fundamental theorem.

## The Laplacian and exponential of the complete graph

Consider the complete undirected graph $K_n$ on a set of independent basis vertices $A=\{a_1,\ldots,a_n\}$, with $n\geqslant2$. Every pair of vertices is joined by an edge of unit conductance. Its [[Laplacian - graph, electrical network and quadratic form|Laplacian polyform]] is

$$
L=\sum_{1\leqslant i<j\leqslant n}[(a_i a_j)]^2=E_n[1]
$$

All products below are computed in the algebra of polyforms. The unit is $e=[1,1]$, and the metric polyform is defined by the [[Laplacian Exponential#The exponential in the algebra of forms|polyform exponential]]

$$
M_{K_n}=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!}
$$

The sum is finite because $L^n=0$. The matrix exponential $\exp\mathbf L$ uses a different product.

> [!info] Expansion in principal polyforms
> **Theorem.** For the complete graph with unit conductances,
>
> $$
> \boxed{
> M_{K_n}=e+\sum_{k=1}^{n-1}n^{k-1}E_n[k]
> }
> \tag{1}
> $$
>
> In particular, its grade components are $M_0=e$ and $M_k=n^{k-1}E_n[k]$ for $1\leqslant k\leqslant n-1$.

> [!note]- Proof
> **Proof.** The [[Products and Powers of Symmetric Polyforms#Several factors and powers|formula for powers of the principal polyform of grade one]] establishes
>
> $$
> L^k=\bigl(E_n[1]\bigr)^k=n^{k-1}k!\,E_n[k],
> \qquad 1\leqslant k\leqslant n-1
> $$
>
> Division by $k!$ gives each positive grade in (1). Grade zero is $L^0=e$. $\square$

Grade zero is written separately: we retain the convention $E_n[0^n]=e$. Extending the coefficient $n^{k-1}$ to $k=0$ with this convention would give the incorrect constant term $e/n$.

If all edges have the same conductance $c>0$, then $L=cE_n[1]$ and

$$
M_{K_n}=e+\sum_{k=1}^{n-1}c^k n^{k-1}E_n[k]
$$

This follows from $(cE_n[1])^k=c^k(E_n[1])^k$. Below, conductances are again taken to be one unless stated otherwise.

## The top grade and Cayley's formula

The principal SPF of the top grade contains one partition into a single block:

$$
E_n[n-1]=[(a_1\ldots a_n)]^2=T_n
$$

By the [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|forest interpretation of the top grade]], the coefficient of $T_n$ in $M_{K_n}$ is the number of spanning trees. Thus (1) gives

$$
\boxed{\tau(K_n)=n^{n-2}}
\tag{2}
$$

**Proof.** In the expansion of the exponential, every spanning forest with $n-1$ edges is a tree on all $n$ vertices. The product of its edge vectors equals the boundary $(a_1\ldots a_n)$ up to a sign, which disappears in the quadratic form. Each tree therefore contributes one copy of $T_n$. By (1), the sum of these contributions is $n^{n-2}T_n$. Since the form $T_n$ is nonzero, the number of trees is $n^{n-2}$. $\square$

Equality (2) is the classical **Cayley formula** for trees on a prescribed set of labelled vertices. Stanley gives it in Example 9.11; three combinatorial proofs appear in the appendix to Chapter 9 [1]. Here it follows from the fundamental theorem of SPFs and the product rule. Their proofs do not use Cayley's enumeration of trees, so there is no circular dependence.

With a common conductance $c$, every tree has weight $c^{n-1}$. The spanning-tree coefficient is then

$$
\tau(K_n)=c^{n-1}n^{n-2}
$$

It is the sum of the weights of the trees; the number of trees itself remains (2).

## Expansion by forest type

The exponential factors as

$$
M_{K_n}
=\prod_{1\leqslant i<j\leqslant n}\bigl(e+[(a_i a_j)]^2\bigr)
$$

In the [[Laplacian Exponential#Grade components and spanning forests|forest expansion]], each edge subset is selected once. A cycle makes the product of edge vectors zero, so only forests remain. All vertices are retained, including isolated vertices.

Suppose a forest has $k$ edges. The positive grades of the boundaries of its nontrivial components form an integer partition

$$
\lambda=[k_1,\ldots,k_m],\qquad
k_i\geqslant1,\qquad
\sum_{i=1}^m k_i=k
$$

For definiteness, the parts are written in nonincreasing order. A component of grade $k_i$ has $k_i+1$ vertices and $k_i$ edges. The number of isolated vertices and the total number of components are

$$
\ell=n-k-m\geqslant0,\qquad m+\ell=n-k
$$

The partition $\lambda$ specifies the component sizes. A particular allocation of vertices to these components is a partition of the set $A$. In the sum $E_n[\lambda,0^\ell]$, each such set partition is counted once, as specified in the [[Symmetric Polyforms - Types and Normalizations|definition and normalization of symmetric sums]].

Fix one partition of the vertex set of this type. By (2), a block of $k_i+1$ vertices admits $(k_i+1)^{k_i-1}$ trees. Choices of trees in different blocks are independent. The number of forests with this partition into components is therefore

$$
t(\lambda)=\prod_{i=1}^m(k_i+1)^{k_i-1}
$$

A singleton block contributes the unique choice with no edges and the factor $1$. The coefficient $t(\lambda)$ does not include the choice of the blocks themselves. Nor does it include a choice of roots: the trees considered here have no distinguished roots.

> [!info] Expansion by type
> **Theorem.** For $1\leqslant k\leqslant n-1$, the grade component of the exponential of the complete graph is
>
> $$
> \boxed{
> M_k=
> \sum_{\substack{\lambda\vdash k\\m\leqslant n-k}}
> t(\lambda)\,E_n[\lambda,0^{\,n-k-m}]
> }
> \tag{3}
> $$
>
> Here $\lambda\vdash k$ means a partition of the integer $k$ into positive parts, and $m$ is the number of parts of that partition. Grade zero is $M_0=e$.

> [!note]- Proof
> **Proof.** Group the forest expansion of $M_k$ by partitions of the vertex set into components. For a fixed set partition, all forests give the same form of the product of block boundaries: changing the tree within a block changes the exterior argument only by a sign.
>
> The number of such choices is $t(\lambda)$. Next, group the set partitions by type. By definition, the sum of the forms of a given type with unit coefficients is $E_n[\lambda,0^{\,n-k-m}]$. The condition $m\leqslant n-k$ ensures that the number of singleton blocks is nonnegative. This gives (3). $\square$

No additional factors for permutations of equal components are introduced: the blocks are already unordered in the definition of $E_n$. There is also no factorial $k!$ in (3). It is needed when recovering the power $L^k=k!M_k$, where each edge set is selected in all $k!$ orders.

The types in (3) refer to the chosen forest representation. SPFs of different types satisfy structural identities, so (3) is not an expansion in a linearly independent basis.

## Counting forests of a given type

Let $\mu_j=\#\{i:k_i=j\}$ be the multiplicity of the positive part $j$ in $\lambda$. By the [[Symmetric Polyforms - Types and Normalizations#Representation size and factorial factors|formula for representation size]], the number of partitions of the vertex set of this type is

$$
\#E_n[\lambda,0^\ell]
=\frac{n!}
{\ell!\displaystyle\prod_{i=1}^m(k_i+1)!\displaystyle\prod_{j\geqslant1}\mu_j!}
$$

Each set partition corresponds to $t(\lambda)$ forests. Thus the number of forests of the given type is

$$
\boxed{
t(\lambda)\,\#E_n[\lambda,0^\ell]
=
\frac{n!\displaystyle\prod_{i=1}^m(k_i+1)^{k_i-1}}
{\ell!\displaystyle\prod_{i=1}^m(k_i+1)!\displaystyle\prod_{j\geqslant1}\mu_j!}
}
\tag{4}
$$

This separately accounts for three sources of factors: choosing the blocks, removing repetitions of equal block sizes, and choosing a tree within each block. The last choice appears only in the numerator.

Retain the notation $s_k(K_n)$ for the number of spanning forests with $k$ edges, as used in the [[Laplacian Exponential#Grade components and spanning forests|forest expansion of the exponential]]. Summing (4) over admissible types gives

$$
s_k(K_n)=
\sum_{\substack{\lambda\vdash k\\m\leqslant n-k}}
t(\lambda)\,\#E_n[\lambda,0^{\,n-k-m}],
\qquad 1\leqslant k\leqslant n-1
$$

For $k=0$, we have $s_0(K_n)=1$, corresponding to the forest with no edges. With a common conductance $c$, the corresponding sum of forest weights is $c^k s_k(K_n)$, where $s_k(K_n)$ on the right denotes the number of forests of the graph with unit conductances.

The size of the sum $E_n[\lambda,0^\ell]$ counts set partitions, not individual forests. The coefficient $t(\lambda)$ recovers the number of forests for each partition. After further transformation of the forms by the fundamental theorem, the ordinary sum of coefficients need no longer retain this combinatorial meaning.

## The complete graph on five vertices

For $K_5$ on vertices $\{a,b,c,d,e\}$, formula (3) gives

$$
\begin{aligned}
M_0&=e\\
M_1&=E_5[1]\\
M_2&=3E_5[2]+E_5[1,1]\\
M_3&=16E_5[3]+3E_5[2,1]\\
M_4&=125E_5[4]
\end{aligned}
$$

Zero parts of the types are omitted here; their multiplicity is uniquely recovered from the vertex count $5$. All types and their forest contributions are listed in the table.

| Grade | Full type | Size of $E_5$ | Coefficient $t(\lambda)$ | Number of forests |
|---:|---|---:|---:|---:|
| $0$ | $[0^5]$ | $1$ | $1$ | $1$ |
| $1$ | $[1,0^3]$ | $10$ | $1$ | $10$ |
| $2$ | $[2,0^2]$ | $10$ | $3$ | $30$ |
| $2$ | $[1,1,0]$ | $15$ | $1$ | $15$ |
| $3$ | $[3,0]$ | $5$ | $16$ | $80$ |
| $3$ | $[2,1]$ | $10$ | $3$ | $30$ |
| $4$ | $[4]$ | $1$ | $125$ | $125$ |

In the grade-zero row, the coefficient $1$ corresponds to the unique empty forest. In all other rows, it is computed by the formula for $t(\lambda)$.

For example, fix the partition $\{a,b,c\}|\{d,e\}$ of type $[2,1]$. One of three trees can be chosen on the triple, while there is only one edge on the pair. Their contribution is

$$
\begin{aligned}
&[(ab)(ac)(de)]^2+[(ab)(bc)(de)]^2+[(ac)(bc)(de)]^2=\\
&=3[(abc)(de)]^2
\end{aligned}
$$

The same coefficient $3$ occurs for each of the ten set partitions of type $[2,1]$. The full contribution of this type is therefore $3E_5[2,1]$ and accounts for $30$ forests.

Now apply the [[Fundamental Theorem of Symmetric Polyforms|fundamental theorem]]:

$$
E_5[1,1]=2E_5[2],\qquad
E_5[2,1]=3E_5[3]
$$

We obtain

$$
M_2=(3+2)E_5[2]=5E_5[2],\qquad
M_3=(16+3\cdot3)E_5[3]=25E_5[3]
$$

Hence

$$
\boxed{
M_{K_5}=e+E_5[1]+5E_5[2]+25E_5[3]+125E_5[4]
}
$$

This agrees with (1), with $E_5[4]=[(abcde)]^2$.

### Forest counts and the sum of coefficients

The table gives the forest counts by grade:

$$
\bigl(s_0(K_5),s_1(K_5),s_2(K_5),s_3(K_5),s_4(K_5)\bigr)
=(1,10,45,110,125)
$$

There are $291$ spanning forests in total, including the empty forest.

At grade two, expanding the symmetric sums in the forest representation $3E_5[2]+E_5[1,1]$ gives a representation of size $10+15=25$ and a coefficient sum of $3\cdot10+15=45$. After transformation to $5E_5[2]$, the size is $10$ and the coefficient sum is $50$.

At grade three, the forest representation has coefficient sum $16\cdot5+3\cdot10=110$. The same polyform written as $25E_5[3]$ has coefficient sum $125$.

There is no contradiction: structural identities preserve the polyform, but not an arbitrary sum of the coefficients in its representation. The coefficient $5$ of $E_5[2]$ therefore cannot be interpreted as the number of trees on a triple: that number is $3$. The additional contribution arose from transforming forms of two disjoint edges.

Numerical metric evaluation is a linear function of the form and is preserved under these transformations. Simply adding the coefficients of all forms in a chosen representation does not define such a function.

## A numerical identity from the two expansions

Comparing (1) and (3) gives a further consequence. Use the exact coefficient from the [[Fundamental Theorem of Symmetric Polyforms#Statement and scope|fundamental theorem]]:

$$
E_n[\lambda,0^{\,n-k-m}]
=
\frac{(n-k-1)!\,k!}
{(n-k-m)!\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!}
E_n[k]
$$

After substitution into (3), all types are expressed through the single nonzero polyform $E_n[k]$. Comparing its coefficient with (1), we obtain, for $1\leqslant k\leqslant n-1$,

$$
\boxed{
\sum_{\substack{\lambda\vdash k\\m\leqslant n-k}}
\frac{(n-k-1)!\,k!}
{(n-k-m)!\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!}
\prod_{i=1}^m(k_i+1)^{k_i-1}
=n^{k-1}
}
\tag{5}
$$

This proof uses equality of forms and the fact that $E_n[k]$ is nonzero. It does not assume linear independence of sums of different types. The admissibility condition in the sum is essential: it excludes types requiring more vertices than are available.

For $k=2$ and $n\geqslant4$, the types are $[2]$ and $[1,1]$. Their contributions to (5) give

$$
3+(n-3)=n
$$

For $k=3$ and $n\geqslant6$, three types are admissible, so

$$
M_3=16E_n[3]+3E_n[2,1]+E_n[1,1,1]
$$

The fundamental theorem gives

$$
E_n[2,1]=3(n-4)E_n[3],\qquad
E_n[1,1,1]=(n-4)(n-5)E_n[3]
$$

The corresponding numerical identity is

$$
16+9(n-4)+(n-4)(n-5)=n^2
$$

For the third power itself, the factor $3!$ must be restored:

$$
\bigl(E_n[1]\bigr)^3
=96E_n[3]+18E_n[2,1]+6E_n[1,1,1],
\qquad n\geqslant6
$$

When $n=5$, the type $[1,1,1]$ is absent, leaving the equality $16+9=25$. When $n=4$, only the type $[3]$ remains, with coefficient $16$. No inadmissible sums are introduced.

Identity (5) connects the coefficients of the fundamental theorem with the numbers of trees within components. In [[Forest Coefficients and Abel Polynomials]], its terms are grouped by the number of nontrivial components. This gives an expansion of Abel polynomials in falling factorials and explains the combinatorial meaning of its coefficients.

## Verification and scope of the results

**Independent computational check.** All $33866$ edge subsets of $K_2,\ldots,K_6$ were enumerated. Cycle detection identified $3270$ forests. For each forest, the exterior product of its edge vectors was computed directly, and its quadratic form was expanded in the vertex basis. After summation over forests, every coefficient of each grade component agreed with (1). The coefficient $t(\lambda)$ was checked separately for every set partition, as was the count (4) after grouping by type. The computations used exact integer arithmetic; they confirm the examples and supplement the general proofs.

This note is based on the author's research within PMG. Representations (1) and (3), the count (4), and identity (5) are proved for all stated $n$ and grades. Cayley's formula is a classical result; here it is derived from previously proved identities of polyforms.

All equalities of forms were obtained before choosing a metric. With a common conductance $c$, the contribution of grade $k$ is multiplied by $c^k$. For arbitrary unequal conductances, the forest expansion remains valid, but symmetry under all permutations of the vertices is generally lost, and formula (1) does not apply.

## References

1. Richard P. Stanley. *Topics in Algebraic Combinatorics*. Version of 1 February 2013. [Author's open text](https://math.mit.edu/~rstan/algcomb/algcomb.pdf). Chapter 9, Example 9.11, p. 178: the number of spanning trees of the complete graph; appendix to Chapter 9, pp. 180-183: proofs by Prüfer, Joyal, and Pitman.
