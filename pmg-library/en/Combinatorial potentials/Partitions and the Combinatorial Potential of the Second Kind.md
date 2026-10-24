---
title: Partitions and the Combinatorial Potential of the Second Kind
date: 2026-10-20
updated: 2026-10-24
revision: 2
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: partitions-and-second-kind-combinatorial-potential
lang: en
description: "From set partitions to the potential of a numerical type: collections, multiplicities, products, repeated counts, and Stirling and Bell numbers."
order: 1
---

The numerical type of a partition specifies the sizes of its components, but does not say which elements belong to each component. The combinatorial potential of the second kind counts the ways to fill this structure with distinguishable elements. To derive its formula, we first examine the partitions themselves, then identify the repetitions that arise when enumerating them.

## One type and three partitions

Take the set $\mathbf A=\{a,b,c\}$. We want one pair and one singleton. There are exactly three partitions:

$$
ab\mid c,\qquad ac\mid b,\qquad bc\mid a
$$

The vertical bar separates blocks. For example, $ab\mid c$ denotes the collection of two subsets $\{a,b\}$ and $\{c\}$. Neither the order of elements within a block nor the order of blocks matters: $ab\mid c$, $ba\mid c$, and $c\mid ab$ denote the same partition.

![Three partitions of a three-element set into a pair and a singleton](Partitions%2021.svg)

*Figure 1. An edge joins two elements into a pair; the remaining vertex forms a singleton block. The pair changes, while the collection of block sizes remains $[2,1]$.*

Thus the numerical type $[2,1]$ corresponds to three set partitions. This is expressed by

$$
s_2([2,1])=3
$$

The number $3$ does not depend on the names of the elements. It characterises the partition type itself.

## A collection, its size, and its weight

### Numerical collections

**Definition.** A finite numerical collection is an unordered collection of numbers in which repetitions are retained: a multiset. We use a bold letter for the collection and ordinary letters for its elements:

$$
\mathbf x=[x_1,\ldots,x_m]
$$

Indices identify individual occurrences of elements. The order of listing is not a property of the collection: $[3,3,2]=[2,3,3]$. Repetitions matter: $[3,3,2]$ and $[3,2]$ are different collections.

The **size**, or cardinality, of a collection is denoted by a hash sign. Its **weight** is the sum of its elements:

$$
\#\mathbf x=m,\qquad
w(\mathbf x)=x_1+\cdots+x_m
$$

For example,

$$
\mathbf x=[3,3,2],\qquad
\#\mathbf x=3,\qquad
w(\mathbf x)=8
$$

**Definition.** A partition of a positive integer $w$ is a numerical collection of positive integers with weight $w$. For example, $[3,3,2]$ is a partition of $8$.

### Set partitions

**Definition.** A partition of a finite set $\mathbf A$ is a collection of nonempty, pairwise disjoint subsets whose union is $\mathbf A$. These subsets are called **blocks**, or components of the partition. The blocks are unnumbered.

Let $m$ be the number of components and $x_1,\ldots,x_m$ their sizes. The collection

$$
\mathbf x=[x_1,\ldots,x_m]
$$

is the **numerical type of the partition**. Then

$$
\#\mathbf x=m,\qquad w(\mathbf x)=\#\mathbf A
$$

For example, the partition $abc\mid de\mid fg$ has three components, type $[3,2,2]$, and seven elements in the original set. The number of components is the size of the collection of block sizes; the number of original elements is its weight.

### Multiplicities

A value may occur several times in a numerical collection. Its number of occurrences is its **multiplicity**.

Let $J$ be the set of distinct values occurring in $\mathbf x$. For each $j\in J$, put

$$
\mu_j=\#\{i:x_i=j\},\qquad
\boldsymbol\mu=[\mu_j]_{j\in J}
$$

The collection $\boldsymbol\mu$ contains one multiplicity for each distinct value in the original collection. Equal multiplicities remain separate elements. For example, $[3,2]$ gives $[1,1]$, not $[1]$.

For $\mathbf x=[3,3,2]$,

$$
J=\{2,3\},\qquad
\mu_2=1,\qquad \mu_3=2,\qquad
\boldsymbol\mu=[1,2]
$$

The sum of the multiplicities is the number of components:

$$
w(\boldsymbol\mu)=m
$$

Repeated parts can be written compactly:

$$
[3,3,2]=[3^2,2],\qquad
[1,1,1,1]=[1^4]
$$

In this notation for a type, the superscript denotes multiplicity, not numerical exponentiation. Where ambiguity is possible, we list repetitions explicitly.

## The product of a collection

We first define the collection, then apply the required operation to it.

**Definition.** The product of the elements of a finite numerical collection is denoted by an exclamation mark after the collection:

$$
\boxed{
\mathbf x!=[x_1,\ldots,x_m]!=x_1\cdots x_m
}
$$

In conventional notation, $\mathbf x!=\prod_{i=1}^m x_i$. For example,

$$
[3,3,2]!=18,\qquad [5]!=5
$$

The ordinary factorial of a nonnegative integer retains its meaning. For $n\geqslant1$, it is the product of a consecutive collection:

$$
n!=[1,2,\ldots,n]!
$$

Thus $5!=120$, whereas $[5]!=5$. The first operation takes a number as its argument; the second takes a collection. The product of the empty collection is defined to be $1$, consistently with $0!=1$.

A new collection can be obtained by transforming every element of a given one. For a collection of nonnegative integers, $[x_i!]$ denotes the **collection of factorials of its elements**. The indices are inherited from the original collection. For example,

$$
\mathbf x=[3,3,2]
\quad\Longrightarrow\quad
[x_i!]=[3!,3!,2!]=[6,6,2]
$$

We can now take the product of the resulting collection:

$$
[x_i!]!=[6,6,2]!=72
$$

The three operations give different results:

| Notation | Quantity computed | For $\mathbf x=[3,3,2]$ |
| --- | --- | ---: |
| $\mathbf x!$ | Product of the elements | $18$ |
| $[x_i!]!$ | Product of their factorials | $72$ |
| $w(\mathbf x)!$ | Factorial of their sum | $40320$ |

The brackets in $[x_i!]!$ preserve the sequence of operations: first transform the elements, then multiply the results. We do not abbreviate this to $\mathbf x!!$; below, $n!!$ has its usual meaning as the double factorial of a number.

## The combinatorial potential of the second kind

> [!info] Definition
> Let $\mathbf x=[x_1,\ldots,x_m]$ be a partition of $w$. The **combinatorial potential of the second kind** $s_2(\mathbf x)$ is the number of partitions of a set of $w$ distinguishable elements into unordered nonempty blocks with collection of sizes $\mathbf x$.

All block sizes are fixed. Specifying only $w$ and $m$ is insufficient: on four elements, two blocks may have sizes $[3,1]$ or $[2,2]$, and these types have different potentials.

Here, “combinatorial potential” is the PMG term for this counting function. The qualifier “of the second kind” will be explained by its relation to Stirling numbers of the second kind. Giving the blocks cyclic orders leads to the [[Cyclic Partitions and the Combinatorial Potential of the First Kind|combinatorial potential of the first kind]].

### Two pairs

Partition $\{a,b,c,d\}$ into two pairs. There are exactly three partitions:

$$
ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc
$$

![Three partitions of four elements into two pairs](Partitions%2022.svg)

*Figure 2. All partitions of type $[2,2]$. Each drawing contains two two-element blocks; exchanging the blocks does not create a new partition.*

A single pair can be chosen from four elements in six ways. This counts each resulting partition twice. Choosing $ab$ leaves $cd$, while choosing $cd$ leaves $ab$. Both choices give the same partition $ab\mid cd$.

Therefore,

$$
s_2([2,2])=\frac{\binom42}{2!}=3
$$

Here $\binom42=6$ is the number of ways to choose two elements from four. Division by $2!$ removes the repetition caused by choosing one of two interchangeable pairs.

### A triple and a singleton

Type $[3,1]$ gives four partitions:

$$
abc\mid d,\qquad abd\mid c,\qquad acd\mid b,\qquad bcd\mid a
$$

![Four partitions of four elements into a triple and a singleton](Partitions%2031.svg)

*Figure 3. All partitions of type $[3,1]$. The outline marks the members of the three-element block. No edges within that block have been chosen.*

It is enough to choose the singleton. Its complement is the triple, so

$$
s_2([3,1])=4
$$

There is no further division by $2!$. The blocks are still unordered, but their sizes distinguish them: the singleton cannot be mistaken for the triple. Choosing the singleton produces each partition exactly once.

## From repeated counts to the general formula

Let $\mathbf x=[x_1,\ldots,x_m]$ be a numerical type, let $w=w(\mathbf x)$, and let $\boldsymbol\mu=[\mu_j]_{j\in J}$ be its collection of positive multiplicities. The indices $i$ range over all occurrences of parts; the indices $j$ range over their distinct values.

**Theorem.** The combinatorial potential of the second kind is

$$
\boxed{
s_2(\mathbf x)=\frac{w!}{[x_i!]!\,[\mu_j!]!}
}
$$

**Proof.** Fix one order of listing the sizes $x_1,\ldots,x_m$. Arrange the $w$ distinguishable elements in a row, then cut the row into consecutive block positions of these sizes. There are $w!$ rows.

First forget the order of elements within each position. A block of size $x_i$ has $x_i!$ internal arrangements with the same members. Independent rearrangements in all blocks give the product $[x_i!]!$.

After division, we obtain

$$
P(\mathbf x)=\frac{w!}{[x_i!]!}
$$

This is the **multinomial coefficient**: the number of ways to distribute elements among distinguishable positions with prescribed sizes. For sizes $[2,2]$, placing $ab$ first and $cd$ second still differs from the reverse placement.

Now forget the position numbers. The blocks of size $j$ can be assigned to the $\mu_j$ positions of that size in $\mu_j!$ ways. These permutations are independent for different sizes, giving $[\mu_j!]!$ repetitions in total.

Blocks of different sizes introduce no additional factor: the size of each position was already fixed. Thus each unordered partition was counted $[x_i!]!\,[\mu_j!]!$ times. Dividing $w!$ by this number proves the formula. $\square$

The denominator separates two sources of repetition: permutations of **elements within blocks** and permutations of **blocks of equal size**. This is why the product of multiplicity factorials appears instead of a common factor $m!$.

### Two triples and a pair

For $\mathbf x=[3,3,2]$,

$$
w=8,\qquad
[x_i!]=[6,6,2],\qquad
\boldsymbol\mu=[2,1],\qquad
[\mu_j!]=[2,1]
$$

Hence

$$
s_2([3,3,2])
=\frac{8!}{[3!,3!,2!]!\,[2!,1!]!}
=\frac{40320}{72\cdot2}
=280
$$

We can count the same objects another way. First choose the pair from eight elements, then one triple from the remaining six. The two triples are interchangeable, so divide by $2$:

$$
s_2([3,3,2])
=\binom82\frac{\binom63}{2}
=28\cdot10
=280
$$

This direct choice of blocks independently confirms the result of the general formula.

## Some characteristic types

### One block and all singletons

If all elements belong to one block, the partition is unique. If each element forms its own block, the partition is also unique:

$$
s_2([w])=1,\qquad s_2([1^w])=1
$$

In the first case, all permutations take place within the sole block. In the second, they permute singleton blocks. The two sources of repetition give the same result through different mechanisms.

### One pair

For $w\geqslant2$, type $[2,1^{w-2}]$ contains one pair and $w-2$ singletons. Choosing the pair determines the partition completely:

$$
s_2([2,1^{w-2}])=\binom w2=\frac{w!}{2!(w-2)!}
$$

For $w=4$, these are the six partitions

$$
\begin{aligned}
&ab\mid c\mid d,\qquad ac\mid b\mid d,\qquad ad\mid b\mid c\vphantom{\Big|}\\
&bc\mid a\mid d,\qquad bd\mid a\mid c,\qquad cd\mid a\mid b
\end{aligned}
$$

### All blocks are pairs

For $m\geqslant1$, partition $2m$ elements into $m$ pairs. The general formula gives

$$
s_2([2^m])=\frac{(2m)!}{2^m m!}
$$

Here $[2^m]$ is the collection of $m$ twos, whereas $2^m$ in the denominator is an ordinary numerical power.

For a direct count, number the original elements. The first element has $2m-1$ possible partners. After that pair is chosen, the least remaining element has $2m-3$ possible partners. Continuing gives

$$
s_2([2^m])=(2m-1)(2m-3)\cdots3\cdot1=(2m-1)!!
$$

Each partition is listed once because the next element whose partner is to be chosen is uniquely determined. For $m=1$, the product has the single factor $1$.

Thus four elements have $3$ pair partitions, six have $15$, and eight have $105$.

## From type potentials to Stirling and Bell numbers

A four-element set has five numerical partition types. Their potentials have already been obtained above:

| Type $\mathbf x$ | Number of components $m=\#\mathbf x$ | $s_2(\mathbf x)$ |
| --- | ---: | ---: |
| $[4]$ | 1 | 1 |
| $[3,1]$ | 2 | 4 |
| $[2,2]$ | 2 | 3 |
| $[2,1,1]$ | 3 | 6 |
| $[1,1,1,1]$ | 4 | 1 |

Every set partition has exactly one type. To count all partitions with a prescribed number of components, we therefore add the potentials of the corresponding types.

**Definition.** The number of partitions of a $w$-element set into $m$ nonempty blocks is the **Stirling number of the second kind**, denoted by $S(w,m)$ [1].

First specify the set of types: let $\mathcal T_{w,m}$ contain all partitions of the integer $w$ into $m$ positive parts. Then

$$
S(w,m)=\sum_{\mathbf x\in\mathcal T_{w,m}}s_2(\mathbf x)
$$

Two blocks on four elements allow two types, so

$$
S(4,2)=s_2([3,1])+s_2([2,2])=4+3=7
$$

The full row by number of blocks is

$$
S(4,1)=1,\qquad S(4,2)=7,\qquad S(4,3)=6,\qquad S(4,4)=1
$$

**Definition.** The total number of partitions of a $w$-element set is the **Bell number**, denoted by $B_w$ [2].

If $\mathcal T_w$ is the set of all numerical partitions of weight $w$, then

$$
B_w=\sum_{\mathbf x\in\mathcal T_w}s_2(\mathbf x)
=\sum_{m=1}^w S(w,m),\qquad w\geqslant1
$$

In particular,

$$
B_4=1+4+3+6+1=1+7+6+1=15
$$

The number of types themselves is denoted by $p(w)$: the number of integer partitions of $w$ [3]. Hence $p(4)=5$, although $B_4=15$.

| What is fixed | What is counted | On four elements |
| --- | --- | ---: |
| Type $[2,2]$ | Set partitions of precisely this type | $s_2([2,2])=3$ |
| Two components | Set partitions of all types with two blocks | $S(4,2)=7$ |
| Only the original set | All its partitions | $B_4=15$ |
| Only the total weight | Numerical types | $p(4)=5$ |

## Relation to partitions in PMG

In this note, the parts of a numerical type specify **block sizes**. In [[Symmetric Polyforms - Types and Normalizations|symmetric polyform types]], they specify the **grades of block boundaries**. The boundary of a block of $r$ vertices has grade $r-1$.

For example, the vertex partition $abc\mid de$ has block sizes $[3,2]$, while its form has type $[2,1]$. The same combinatorial potential can therefore be applied to different collections: before calculating it, we must identify which objects are being partitioned and what the parts of the type mean.

The passage from block sizes to types described by edges, the counting of forests, and the role of the potential in SPF coefficients are developed in [[Combinatorial Potentials in Symmetric Polyforms]].

The potential formula was proved by counting repetitions. Its relations to Stirling and Bell numbers follow by grouping partitions by type. In addition, all set partitions for $1\leqslant w\leqslant8$ were independently enumerated and grouped by block sizes: the counts agreed with the formula for every type. This finite check supplements the general proof.

## Sources and notation

“Combinatorial potential” and the notation for the product of a numerical collection are used in the PMG sense defined here. The standard definitions of partitions and Stirling and Bell numbers agree with the sources below. This note is based on the author's research within PMG.

1. NIST Digital Library of Mathematical Functions. [§26.8(i), Set Partitions: Stirling Numbers](https://dlmf.nist.gov/26.8#i): definition of $S(w,m)$ and Table 26.8.2.
2. NIST Digital Library of Mathematical Functions. [§26.7(i), Set Partitions: Bell Numbers](https://dlmf.nist.gov/26.7#i): definition of Bell numbers and their relation to Stirling numbers.
3. NIST Digital Library of Mathematical Functions. [§26.9(i), Integer Partitions](https://dlmf.nist.gov/26.9#i): definitions of integer partitions and $p(w)$.

