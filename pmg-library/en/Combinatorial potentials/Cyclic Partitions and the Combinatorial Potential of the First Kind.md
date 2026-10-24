---
title: Cyclic Partitions and the Combinatorial Potential of the First Kind
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: cyclic-partitions-and-first-kind-combinatorial-potential
lang: en
description: Cyclic orders within partition blocks, the first-kind combinatorial potential, Stirling numbers, and the exclusion of fixed points.
order: 5
source_revision: 1
---

The [[Partitions and the Combinatorial Potential of the Second Kind|potential of the second kind]] counts set partitions with prescribed block sizes. Giving each block a cyclic order produces a **cyclic partition**, or a permutation written as disjoint cycles. We call the count of such objects of a specified type the combinatorial potential of the first kind. It connects partitions with [[Permutation Digraphs and Cycle Combinatorics|permutation digraphs]].

## From a block to a cycle

Three specified elements $a,b,c$ form one block $\{a,b,c\}$ but admit two cyclic orders:

$$
(a\,b\,c),\qquad (a\,c\,b)
$$

The first represents $a\to b\to c\to a$, the second its reverse. Shifting the written starting point leaves the cycle unchanged: $(a\,b\,c)=(b\,c\,a)=(c\,a\,b)$. For length at least $3$, reversing direction gives a different cycle.

A block of $k\geqslant1$ distinguishable elements has $(k-1)!$ cyclic orders: fix one specified element first and order the others freely. For $k=1$, the sole cycle is a fixed point; for $k=2$, there is also one cycle.

![Two cyclic orders on a triple with a fixed singleton](Two%20Cyclic%20Orders%20on%20a%20Triple.svg)

*Figure 1. The partition $abc\mid d$ gives two permutations, $(a\,b\,c)(d)$ and $(a\,c\,b)(d)$. The loop at $d$ denotes a fixed point. Four choices of singleton give $8$ permutations of type $[3,1]$.*

Parentheses around element names here denote permutation cycles, not PMG exterior boundaries. Order within a cycle matters; the order of listing distinct cycles does not.

## The potential of a cycle type

Let $\mathbf k=[k_1,\ldots,k_m]$ be positive cycle lengths, $n=w(\mathbf k)$, and let $\mu_j$ be the multiplicity of length $j$. Use the [[Partitions and the Combinatorial Potential of the Second Kind#The product of a collection|collection product]] $\mathbf k!=\prod_i k_i$ and write $\boldsymbol\mu$ for the collection of positive multiplicities.

**Definition.** The combinatorial potential of the first kind $s_1(\mathbf k)$ counts permutations of a fixed set of $n$ distinguishable elements whose cycle-length collection is $\mathbf k$.

**Proposition.** The two kinds of potential are related by

$$
\boxed{
s_1(\mathbf k)
=s_2(\mathbf k)\prod_{i=1}^{m}(k_i-1)!
=\frac{n!}{\mathbf k!\,[\mu_j!]!}
=\frac{n!}{\prod_{j\geqslant1}j^{\mu_j}\mu_j!}
}
\tag{1}
$$

> [!note]- Proof
> **Proof.** First partition the original set into blocks of sizes $\mathbf k$, in $s_2(\mathbf k)$ ways. Choose a cyclic order independently in each fixed block, giving factor $\prod_i(k_i-1)!$.
>
> Substituting the second-kind formula reduces each denominator factor $k_i!$ to $k_i$. Multiplicity factorials were already included in $s_2$ and require no further division. Each collection of disjoint cycles defines one permutation. $\square$

“Combinatorial potential” has its PMG meaning here. The number in (1) is the standard count of permutations of a prescribed cycle type [1]. It uses no metric and differs from a form potential defined through the Laplacian exponential.

For four elements:

| Type $\mathbf k$ | Cycles | $s_2(\mathbf k)$ | $\prod_i(k_i-1)!$ | $s_1(\mathbf k)$ |
| --- | ---: | ---: | ---: | ---: |
| $[4]$ | 1 | 1 | 6 | 6 |
| $[3,1]$ | 2 | 4 | 2 | 8 |
| $[2,2]$ | 2 | 3 | 1 | 3 |
| $[2,1,1]$ | 3 | 6 | 1 | 6 |
| $[1,1,1,1]$ | 4 | 1 | 1 | 1 |
| Total | | 15 | | 24 |

For example, $s_1([3,3,2])=280\cdot2\cdot2=1120$: each of $280$ partitions into two triples and a pair admits four combinations of cyclic orders.

## Summing types and Stirling numbers

Every permutation has a unique disjoint-cycle decomposition and numerical type. Therefore, for $n\geqslant1$,

$$
\boxed{\sum_{\substack{\mathbf k\vdash n}}s_1(\mathbf k)=n!}
$$

Notation $\mathbf k\vdash n$ means that $\mathbf k$ is an integer partition of $n$. This counts all permutations by type and requires no generating function.

Fixing the number of cycles gives the **unsigned Stirling numbers of the first kind** [2]:

$$
c(n,m)=
\sum_{\substack{\mathbf k\vdash n\\\#\mathbf k=m}}s_1(\mathbf k)
$$

Unlike $s_1$, the number $c(n,m)$ does not prescribe individual lengths. For example,

$$
c(4,2)=s_1([3,1])+s_1([2,2])=8+3=11
$$

The full row for $n=4$ is $6,11,6,1$. The comparison with [[Partitions and the Combinatorial Potential of the Second Kind#From type potentials to Stirling and Bell numbers|second-kind Stirling numbers]] is direct: there one sums ordinary partitions, here cyclic partitions.

## Excluding fixed points

The general formula permits parts $1$. For loopless digraphs, retain only types whose parts are at least $2$. Their total potential is the derangement count:

$$
D_n=
\sum_{\substack{\mathbf k\vdash n\\k_i\geqslant2}}s_1(\mathbf k)
=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}
\tag{2}
$$

Set $D_0=1$ for the empty permutation and $D_1=0$. For $n=4$, only $[4]$ and $[2,2]$ remain, so $D_4=6+3=9$.

> [!note]- Inclusion-exclusion derivation
> **Proof.** After choosing $j$ elements that must remain fixed, the others can be permuted in $(n-j)!$ ways. Inclusion-exclusion gives
>
> $$
> D_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!
> =n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}
> $$
>
> A derangement is counted once; a permutation with $q>0$ fixed points receives total coefficient $(1-1)^q=0$. $\square$

Summing types with $m$ cycles of length at least $2$ gives **associated Stirling numbers of the first kind** [3]:

$$
c_{\geqslant2}(n,m)=
\sum_{\substack{\mathbf k\vdash n\\\#\mathbf k=m\\k_i\geqslant2}}s_1(\mathbf k)
$$

These differ from ordinary $c(n,m)$: for example, $c_{\geqslant2}(4,2)=3$, whereas $c(4,2)=11$.

[[Permutation Digraphs and Cycle Combinatorics]] gives their graph interpretation and uses the type potential for probabilities and mean cycle counts. Its parts $\mathbf k$ are cycle lengths, not boundary grades or forest types from [[Partition Toponomes]].

## Checks and sources

Equations (1)-(2) are proved by counting objects. Enumeration of all permutations for $1\leqslant n\leqslant8$ additionally verified cycle-type distributions, sums by cycle count, and the fixed-point restriction.

The note draws on the author's PMG research. The potential terminology and notation belong to the project's language; the enumeration formulas are classical.

1. NIST DLMF. [§26.4, equations 26.4.7 and 26.4.8](https://dlmf.nist.gov/26.4#E7): permutation and set-partition counts by type.
2. NIST DLMF. [§26.13, Permutations: Cycle Notation](https://dlmf.nist.gov/26.13): cycle types, unsigned first-kind Stirling numbers, and derangements.
3. Howard, F. T. [Weighted Associated Stirling Numbers](https://www.fq.math.ca/Scanned/22-2/howard.pdf). *The Fibonacci Quarterly*, 22(2), 1984, 156-165. §1: associated first-kind numbers count permutations with cycles of length at least $2$.
