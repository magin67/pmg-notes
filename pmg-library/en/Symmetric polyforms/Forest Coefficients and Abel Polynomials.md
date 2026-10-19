---
title: "Forest Coefficients and Abel Polynomials"
date: 2026-10-19
updated: 2026-10-19
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: forest-coefficients-and-abel-polynomials
lang: en
description: "The falling-factorial expansion of Abel polynomials derived from SPF identities, the combinatorial meaning of its coefficients, and connections with Stirling numbers and OEIS A360177."
order: 5
---

Comparing two representations of the exponential of the complete graph in [[Symmetric Polyforms of the Complete Graph]] yielded a numerical identity. Grouping its terms by the number of nontrivial components gives an expansion of Abel polynomials in falling factorials.

The connection between Abel polynomials, labelled trees, and rooted forests is classical. Here we trace how it arises from identities of symmetric polyforms (SPFs) and clarify the meaning of the coefficients in the falling-factorial expansion. They count rooted forests together with a partition of their set of components into groups. The same coefficient triangle is recorded in OEIS as [A360177](https://oeis.org/A360177).

## From SPF types to a numerical identity

Let $k\geqslant1$ and

$$
\lambda=[k_1,\ldots,k_m]\vdash k,\qquad
k_i\geqslant1,\qquad
\sum_{i=1}^m k_i=k
$$

This is a partition of the integer $k$ into $m$ positive parts. In the forest representation of an SPF, the parts specify the grades of the boundaries of its nontrivial components: the corresponding vertex blocks have sizes $k_i+1$. Let $\mu_j$ denote the multiplicity of the part $j$.

Separate two factors:

$$
s(\lambda)=
\frac{k!}{\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!},
\qquad
t(\lambda)=\prod_{i=1}^m(k_i+1)^{k_i-1}
$$

The number $s(\lambda)$ counts partitions of a set of $k$ distinct labels into unordered blocks of sizes $k_1,\ldots,k_m$. Indeed, permutations of labels within blocks give the factors $k_i!$, while permutations of blocks of equal size give the factors $\mu_j!$.

For now, these $k$ labels form an auxiliary set. The representation size of $E_n[\lambda,0^{\,n-k-m}]$ counts partitions of the original $n$ vertices into blocks of sizes $k_i+1$ and singleton blocks; its formula is given in the [[Symmetric Polyforms - Types and Normalizations#Representation size and factorial factors|note on types and normalizations]]. Thus $s(\lambda)$ is not the representation size of this SPF.

The factor $t(\lambda)$ already appeared in the [[Symmetric Polyforms of the Complete Graph#Expansion by forest type|expansion by forest type]]. It counts independent choices of trees on prescribed blocks of sizes $k_i+1$. No roots are chosen in these trees.

The [[Symmetric Polyforms of the Complete Graph#A numerical identity from the two expansions|numerical identity from the two expansions]] establishes that, for $n\geqslant k+1$,

$$
\sum_{\substack{\lambda\vdash k\\m\leqslant n-k}}
\frac{(n-k-1)!}{(n-k-m)!}\,
s(\lambda)t(\lambda)
=n^{k-1}
$$

The condition $m\leqslant n-k$ means that enough vertices are available for the type. The factorial ratio comes from the [[Fundamental Theorem of Symmetric Polyforms#Statement and scope|fundamental theorem of SPFs]]; its proof need not be repeated here.

## Forest coefficients

**Definition.** For $1\leqslant m\leqslant k$, set

$$
\boxed{
\operatorname{St}(k,m)=
\sum_{\substack{\lambda\vdash k\\\lambda\text{ has }m\text{ parts}}}
s(\lambda)t(\lambda)
}
\tag{1}
$$

We call these numbers **forest coefficients**. This name is used in this note for the coefficients (1). They differ from the spanning-tree coefficient of a graph, $\tau(G)$, and from the Stirling numbers $S(k,m)$.

For the boundary cases, set $\operatorname{St}(0,0)=1$, $\operatorname{St}(k,0)=0$ for $k>0$, and $\operatorname{St}(k,m)=0$ for $m>k$.

The first values are:

| $k\backslash m$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---:|---:|---:|---:|---:|---:|---:|
| $1$ | $1$ | | | | | |
| $2$ | $3$ | $1$ | | | | |
| $3$ | $16$ | $9$ | $1$ | | | |
| $4$ | $125$ | $91$ | $18$ | $1$ | | |
| $5$ | $1296$ | $1105$ | $295$ | $30$ | $1$ | |
| $6$ | $16807$ | $15961$ | $5160$ | $725$ | $45$ | $1$ |

For example, with $k=4$ and $m=2$, there are two integer partitions: $[3,1]$ and $[2,2]$. Hence

$$
\operatorname{St}(4,2)=
\frac{4!}{3!\,1!}\,16+
\frac{4!}{2!\,2!\,2!}\,3^2
=64+27=91
$$

The final factor $2!$ in the second denominator accounts for the two equal parts. With $k=4$ and $m=3$, the only type is $[2,1,1]$:

$$
\operatorname{St}(4,3)=
\frac{4!}{2!\,1!\,1!\,2!}\,3=18
$$

The extreme values follow directly from the types $[k]$ and $[1^k]$:

$$
\operatorname{St}(k,1)=(k+1)^{k-1},
\qquad
\operatorname{St}(k,k)=1
$$

## The expansion of Abel polynomials

**Definition.** The falling factorial is defined as the polynomial

$$
x_{\underline m}=\prod_{j=0}^{m-1}(x-j),
\qquad
x_{\underline0}=1
$$

For an integer $x\geqslant m$, it equals $x!/(x-m)!$. The product definition also applies to other values of $x$; in particular, $x_{\underline m}=0$ for an integer $0\leqslant x<m$.

The polynomials $1,x_{\underline1},\ldots,x_{\underline k}$ form a basis of the space of polynomials of degree at most $k$: each has degree equal to its index and leading coefficient $1$.

In the normalization used by Lando [1], the **Abel polynomials** are

$$
A_0(x)=1,\qquad
A_k(x)=x(x+k)^{k-1}\quad(k\geqslant1)
$$

> [!info] Expansion in falling factorials
> **Theorem.** For every $k\geqslant1$, the following polynomial identity holds:
>
> $$
> \boxed{
> A_k(x)=\sum_{m=1}^k\operatorname{St}(k,m)x_{\underline m}
> }
> \tag{2}
> $$

> [!note]- Derivation from SPF identities
> **Proof.** Fix $k$ and take an integer $x\geqslant k$. Set $n=k+x$. Every partition $\lambda\vdash k$ is then admissible in the numerical identity: its number of parts does not exceed $k\leqslant n-k$.
>
> Group the terms by $m$ and multiply the equality by $x=n-k$. This gives
>
> $$
> x(x+k)^{k-1}
> =\sum_{m=1}^k
> \operatorname{St}(k,m)\,
> \frac{x(x-1)!}{(x-m)!}
> =\sum_{m=1}^k\operatorname{St}(k,m)x_{\underline m}
> $$
>
> For fixed $k$, both sides are polynomials in $x$. They agree at infinitely many integers $x\geqslant k$, so they agree identically. This proves (2) without using factorials of negative integers. $\square$

For a positive integer $x<k$, the terms with $m>x$ vanish automatically. This corresponds exactly to the restriction on the number of components in the original SPF identity. For arbitrary real or complex $x$, the equality is a polynomial identity.

**Example.** For $k=3$, we obtain two representations of the same polynomial:

$$
\begin{aligned}
A_3(x)&=16x+9x(x-1)+x(x-1)(x-2)\\
&=9x+6x^2+x^3
\end{aligned}
$$

For $k=4$:

$$
\begin{aligned}
A_4(x)&=125x+91x_{\underline2}+18x_{\underline3}+x_{\underline4}\\
&=64x+48x^2+12x^3+x^4
\end{aligned}
$$

The two sets of coefficients refer to different bases of the polynomial space. Their combinatorial meanings also differ.

## What forest coefficients count

Consider a set $U$ of $k$ labelled vertices. Partition it into $m$ nonempty unordered blocks $B_1,\ldots,B_m$. Add one new vertex $\rho_i$ to each block and choose a tree on $B_i\cup\{\rho_i\}$.

The vertex $\rho_i$ is distinguished in advance as the root. It is attached to its block; neither roots nor blocks have an independent ordering. If $|B_i|=k_i$, the number of trees is $(k_i+1)^{k_i-1}$ by [[Symmetric Polyforms of the Complete Graph#The top grade and Cayley's formula|Cayley's formula]]. No additional factor for choosing a root occurs.

**Proposition.** The number of such collections of blocks with trees is $\operatorname{St}(k,m)$.

**Proof.** For a fixed list of sizes $\lambda$, there are $s(\lambda)$ partitions of $U$ and $t(\lambda)$ independent choices of trees. Summing over all $\lambda$ with $m$ parts gives (1). $\square$

Although the sizes of the augmented trees agree with the sizes of the nontrivial components in the SPF type, this is a separate model on $k$ labelled vertices and $m$ added roots. It does not count all forests of the original $K_n$.

### Deleting the added roots

**Definition.** A rooted forest is a forest with one distinguished vertex, called the root, in each component. A singleton component also has a root.

> [!info] A forest with grouped components
> **Theorem.** The number $\operatorname{St}(k,m)$ counts pairs consisting of:
>
> - a rooted forest on a prescribed set of $k$ labelled vertices;
> - a partition of its set of components into $m$ nonempty unordered groups.
>
> The forest itself may have more than $m$ components.

> [!note]- Proof by a bijection
> **Proof.** In each tree on $B_i\cup\{\rho_i\}$, delete $\rho_i$ and all edges incident to it. The result is a nonempty forest on $B_i$. Each of its components contained exactly one neighbor of $\rho_i$: having none would contradict connectedness of the original tree, while having two would create a cycle.
>
> Distinguish this neighbor as the root of the component. Put all components obtained from one $B_i$ into one group. This gives a rooted forest on $U$ with $m$ nonempty groups of components.
>
> Conversely, for each group, add one vertex $\rho_i$ and join it to the roots of all components in that group. The result is a connected graph without cycles, hence a tree. The union of the vertex sets of the components in the group recovers the block $B_i$.
>
> The constructions are mutually inverse and introduce no ordering of the groups. Thus the number of pairs is (1). $\square$

When $m=1$, all components of any rooted forest are placed in a single group. Hence $\operatorname{St}(k,1)=(k+1)^{k-1}$ counts all rooted forests on $k$ vertices. The bijection identifies them with trees on the same vertices together with one added vertex.

## Ordinary coefficients and Stirling numbers

In *Graphs and Topology*, Section 8.3, Theorem 8.3.1 [1], Lando proves that the coefficient of $x^r$ in $A_k(x)$ is the number of rooted labelled forests on $k$ vertices with $r$ components. Expanding $x(x+k)^{k-1}$ gives this count explicitly:

$$
[x^r]A_k(x)=\binom{k-1}{r-1}k^{k-r},
\qquad 1\leqslant r\leqslant k
$$

Here $[x^r]$ denotes extraction of the coefficient of the ordinary power.

**Definition.** The Stirling number of the second kind $S(r,m)$ counts partitions of a set of $r$ elements into $m$ nonempty unordered blocks.

Each rooted forest with $r$ components admits $S(r,m)$ ways to group those components. The bijection proved above therefore gives

$$
\boxed{
\operatorname{St}(k,m)=
\sum_{r=m}^k
\binom{k-1}{r-1}k^{k-r}S(r,m)
}
\tag{3}
$$

Thus the forest coefficients are obtained from the ordinary coefficients of the Abel polynomial by a transformation using Stirling numbers of the second kind.

**Algebraic check of the correspondence.** For an integer $x\geqslant0$, the number of maps from a set of $r$ elements to a set of $x$ elements is $x^r$. If the image has size $m$, the nonempty fibers form a partition into $m$ blocks. Distinct values can be assigned to these blocks in $x_{\underline m}$ ways. Hence

$$
x^r=\sum_{m=0}^r S(r,m)x_{\underline m}
$$

The equality extends to all $x$ as a polynomial identity. Substitution into the ordinary power expansion of $A_k(x)$ and uniqueness of coefficients in the falling-factorial basis give (3) again.

**Example on three vertices.** There are $9$ rooted trees, $6$ rooted forests with two components, and one forest with three singleton components. Therefore

$$
\begin{aligned}
\operatorname{St}(3,1)&=9+6+1=16\\
\operatorname{St}(3,2)&=6\cdot1+1\cdot3=9\\
\operatorname{St}(3,3)&=1
\end{aligned}
$$

In the second line, a forest with two components has only one grouping into two groups. Three singleton components can be partitioned into two groups in three ways.

## Forests with prescribed roots

Expansion (2) also solves another counting problem. Take $k$ ordinary labelled vertices and $q\geqslant1$ additional labelled root vertices. Count spanning forests of the complete graph $K_{k+q}$ in which each component contains exactly one prescribed root. A root may be isolated.

**Corollary.** The number of such forests is

$$
A_k(q)=q(q+k)^{k-1}
$$

**Proof.** Suppose exactly $m$ roots belong to nontrivial components. Partitioning the ordinary vertices into the corresponding blocks and choosing trees with added roots gives $\operatorname{St}(k,m)$ possibilities. Distinct roots from the prescribed set can be assigned to these $m$ blocks in $q_{\underline m}$ ways. The remaining roots are isolated.

Thus the number of forests is $\sum_m\operatorname{St}(k,m)q_{\underline m}$, which equals $A_k(q)$ by (2). $\square$

In particular, on $k+m$ vertices with $m$ prescribed roots, the number of such forests without isolated roots is $m!\operatorname{St}(k,m)$. The factorial accounts for assigning distinct root labels to the unordered blocks.

**Example.** For three ordinary vertices and two prescribed roots,

$$
A_3(2)=2\cdot5^2=50
=2\operatorname{St}(3,1)+2\operatorname{St}(3,2)
=32+18
$$

In $32$ forests, one root is isolated and the other belongs to a tree containing the three ordinary vertices. In $18$ forests, both roots belong to nontrivial components.

## Finite differences and the exact correspondence with OEIS

For a polynomial $f$, define the finite-difference operator by

$$
\Delta f(x)=f(x+1)-f(x)
$$

The notation $\Delta^m f(0)$ means the value of the polynomial $\Delta^m f(x)$ at $x=0$.

> [!info] An explicit formula for forest coefficients
> **Theorem.** For $1\leqslant m\leqslant k$,
>
> $$
> \boxed{
> \operatorname{St}(k,m)
> =\frac{\Delta^m A_k(0)}{m!}
> =\frac1{m!}\sum_{i=1}^m
> (-1)^{m-i}\binom mi\,i(k+i)^{k-1}
> }
> \tag{4}
> $$

> [!note]- Proof and an equivalent formula
> **Proof.** For falling factorials,
>
> $$
> \Delta x_{\underline j}=j\,x_{\underline{j-1}},
> \qquad j\geqslant1
> $$
>
> After applying $\Delta$ a total of $m$ times and setting $x=0$, the result is zero for $j\ne m$ and $m!$ for $j=m$. Applying this to (2) gives the first equality in (4).
>
> If $Tf(x)=f(x+1)$, then $\Delta=T-I$. The binomial formula for $(T-I)^m$ yields
>
> $$
> \Delta^m f(0)=
> \sum_{i=0}^m(-1)^{m-i}\binom mi f(i)
> $$
>
> Substitute $f=A_k$ and use $A_k(0)=0$. This gives the second equality in (4).
>
> Finally, $i\binom mi=m\binom{m-1}{i-1}$ implies
>
> $$
> \operatorname{St}(k,m)=
> \frac1{(m-1)!}
> \sum_{i=0}^{m-1}(-1)^{m-1-i}
> \binom{m-1}{i}(k+1+i)^{k-1}
> $$
>
> Equivalently,
>
> $$
> \operatorname{St}(k,m)=
> \frac{\left.\Delta^{m-1}(x+k+1)^{k-1}\right|_{x=0}}{(m-1)!}
> \tag{5}
> $$
>
> In all these formulas, the difference operator acts on the variable $x$. $\square$

For $k\geqslant m$, the first cases are

$$
\begin{aligned}
\operatorname{St}(k,1)&=(k+1)^{k-1}\\
\operatorname{St}(k,2)&=(k+2)^{k-1}-(k+1)^{k-1}\\
2!\operatorname{St}(k,3)&=(k+3)^{k-1}-2(k+2)^{k-1}+(k+1)^{k-1}
\end{aligned}
$$

For $m=4$:

$$
\begin{aligned}
3!\operatorname{St}(k,4)
&=(k+4)^{k-1}-3(k+3)^{k-1}+\\
&\quad+3(k+2)^{k-1}-(k+1)^{k-1}
\end{aligned}
$$

Expanding the binomial coefficient in (5) gives

$$
\operatorname{St}(k,m)=
\sum_{i=0}^{m-1}
\frac{(-1)^{m-1-i}(k+i+1)^{k-1}}
{i!(m-1-i)!}
$$

This is precisely the formula defining the triangle [OEIS A360177](https://oeis.org/A360177) [2], with its indices $n=k$ and $k=m$ in the notation of the entry. The signs agree because the exponents $m-1-i$ and $i-m-1$ differ by an even integer. The diagonal entries are $1$; the row and column with index zero agree with our boundary conventions. The correspondence is established by the general formula, rather than merely by matching a few rows of the table.

## Verification and the role of the result

**Independent computational check.** For $1\leqslant k\leqslant6$, the edge subsets of the complete graph on $k$ vertices were enumerated, forests were identified, and every choice of a root in each component was counted. A separate enumeration of partitions of the component set gave the numbers of pairs consisting of a rooted forest and a grouping. These agreed with the table computed from (1). For $1\leqslant k\leqslant10$, the sums over types were checked against both finite-difference formulas. The example with three ordinary vertices and two prescribed roots independently gave $32+18=50$ forests.

This note is based on the author's research within PMG. The derivation of (2) relies on proved SPF identities. The combinatorial interpretations are related by an explicit bijection; formulas (3)-(5) also have general proofs.

Abel polynomials and their connection with rooted forests are classical results [1]. The triangle $\operatorname{St}(k,m)$ is recorded in OEIS [2]. This note aligns these objects with SPF normalizations and explains the transitions between the counting problems. No novelty is claimed for the numerical formulas.

All coefficients considered here are defined combinatorially and require no resistance metric. The sum (1), the representation size of an SPF, and the metric evaluation of a polyform are different quantities.

## References

1. S. K. Lando. *Graphs and Topology*. Lecture notes, 1 June 2018 (in Russian). [Open text on the HSE University website](https://electives.hse.ru/data/2018/06/01/1150198748/GraphTopology18.pdf). Section 4.2, pp. 26-27: the Abel polynomial of a graph defined through rooted spanning forests; Section 8.3, Theorem 8.3.1, p. 67: the forest interpretation of the ordinary coefficients of $A_k(x)=x(x+k)^{k-1}$. Theorem 8.3.2, p. 68, gives the corresponding exponential generating function.
2. Peter Luschny. [A360177](https://oeis.org/A360177). *The On-Line Encyclopedia of Integer Sequences*, entry dated 28 January 2023. The triangle agrees with $\operatorname{St}(k,m)$; the correspondence between its explicit formula and (5) is shown in the text.
