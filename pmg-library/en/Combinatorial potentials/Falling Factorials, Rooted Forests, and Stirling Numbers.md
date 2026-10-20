---
title: "Falling Factorials, Rooted Forests, and Stirling Numbers"
date: 2026-10-20
updated: 2026-10-20
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: falling-factorials-rooted-forests-and-stirling-numbers
lang: en
description: "Graph interpretations of power and Abel polynomial expansions, rooted-forest codes, finite differences, and the exact relation between forest coefficients and r-Stirling numbers."
order: 4
---

Ordinary powers, falling factorials, and Abel polynomials arise from different rules for constructing graphs. Their expansions group constructions by the number of occupied roots or by partition type. A shift of the variable also has a combinatorial meaning: some possible values are distinguished in advance.

We use [[Partitions and the Combinatorial Potential of the Second Kind|partitions and the potential of the second kind]] and [[Cayley's Theorem and Joining Prescribed Components|Cayley's formula]]. The coefficients introduced in [[Forest Coefficients and Abel Polynomials]] receive a further interpretation through forest codes. This establishes an explicit correspondence with $r$-Stirling numbers; the proof does not require polyforms.

## Star forests and ordinary powers

Let $U$ be a set of $w\geqslant1$ labelled ordinary vertices and $R$ a disjoint set of $q\geqslant1$ prescribed roots. Join each vertex of $U$ to exactly one root. There are no edges within $U$ or within $R$. The result is a forest of stars with $q$ components, including isolated roots.

The choices for the $w$ vertices are independent, giving $q^w$ forests. Now group them by the number $m$ of **nonisolated** roots. Vertices attached to the same root form a nonempty block of a partition of $U$. First choose the partition into $m$ blocks, then assign distinct roots to them:

$$
q^w=\sum_{m=1}^{w}S(w,m)q_{\underline m}
$$

Here $S(w,m)$ is the ordinary Stirling number of the second kind, and

$$
x_{\underline m}=[x,x-1,\ldots,x-m+1]!,\qquad
x_{\underline0}=1
$$

is the falling factorial. For an integer $q<m$, it is zero: there are too few distinct roots for $m$ blocks. The notation $[\ldots]!$ denotes the [[Partitions and the Combinatorial Potential of the Second Kind#The product of a collection|product of a collection]].

If the block sizes $\lambda=[w_1,\ldots,w_m]\vdash w$ are also fixed, the potential $s_2(\lambda)$ replaces $S(w,m)$. Thus

$$
q^w=\sum_{\lambda\vdash w}s_2(\lambda)q_{\underline{\#\lambda}}
$$

Type $\lambda$ specifies both the number of ordinary vertices and the number of edges in each nonisolated star. The full number of components is $q$, the number of nonisolated components is $m$, and the number of isolated roots is $q-m$.

## Allowing any tree within a component

Keep $U$ and $R$, but now allow edges between ordinary vertices. Require each component to be a tree containing exactly one root from $R$. Such forests have $w+q$ vertices, $q$ components, and $w$ edges.

Adding a prescribed root to a block of $j$ ordinary vertices gives $j+1$ vertices, supporting $(j+1)^{j-1}$ trees. For a positive type $\lambda=[w_1,\ldots,w_m]$, this introduces the factors

$$
t(\lambda)=[(w_i+1)^{w_i-1}]!,\qquad
\operatorname{St}(w,m)=
\sum_{\substack{\lambda\vdash w\\\#\lambda=m}}
s_2(\lambda)t(\lambda)
$$

The product indices range over $1,\ldots,m$. The number $\operatorname{St}(w,m)$ counts these constructions: partition $U$ into $m$ nonempty unordered blocks, add a separate root to each block, and choose a tree. The added roots do not yet have individual labels; each is identified by its component.

Assigning distinct labels from $R$ to these $m$ roots gives $q_{\underline m}$ choices. Hence the total number of forests is

$$
A_w(q)=\sum_{m=1}^{w}\operatorname{St}(w,m)q_{\underline m}
$$

Star forests and general rooted forests differ in the choice of tree within each block: the first has a unique choice, while the second introduces $t(\lambda)$.

### Nine forests on three ordinary vertices

For $U=\{a,b,c\}$ and two nonempty blocks, there are three partitions: $ac\mid b$, $bc\mid a$, and $ab\mid c$. A two-vertex ordinary block with an added root has three trees; a singleton ordinary block with a root has one. Therefore $\operatorname{St}(3,2)=3\cdot3=9$.

![Nine forests: three partitions of ordinary vertices into a pair and a singleton, with three trees on each pair and its root](Nine%20Rooted%20Forests.svg)

*Figure 1. The scheme of nine possibilities is retained from the author's research drawing. Ordinary vertices are labelled $a,b,c$; added roots are coloured and marked $\circledast$. The roots have no individual labels. Each row fixes the partition of ordinary vertices and varies the tree on the triple.*

Giving the roots two distinct labels produces $2!\cdot9=18$ possibilities. This is not the count of all forests of type $[2,1]$ on an arbitrary five-element labelled vertex set: [[Combinatorial Potentials in Symmetric Polyforms#What the numbers 3, 10, and 30 mean|that count is $30$]]. Here the roles of ordinary vertices and roots are fixed in advance.

## A code for a rooted forest

The formula for $A_w(q)$ can be obtained directly from the graph. Fix a linear order on the ordinary labels. Repeatedly delete the least ordinary leaf and record its sole neighbour. Roots are never deleted. After $w$ steps, only roots remain.

The resulting code has the form

$$
(p_1,\ldots,p_{w-1};\rho),\qquad
p_i\in U\cup R,\qquad \rho\in R
$$

The last entry must be a root: no other ordinary vertex can still be adjacent to the last ordinary leaf.

> [!proof]- Why the coding is reversible
> **Proof.** Take any sequence of the stated form. Among the remaining ordinary labels, choose the least one absent from the entire remaining code. Join it to the first code entry, then remove the chosen label and that entry. Repeat until all ordinary vertices have been removed.
>
> If $t$ ordinary vertices remain, the code has $t$ entries, the last of which is a root. At most $t-1$ ordinary labels can therefore occur in it, so a suitable label exists. A previously deleted vertex cannot occur in the remaining code: it was absent from that code when deleted.
>
> Viewed in reverse order, each step adds a new leaf to an already constructed forest. Thus no cycle arises, and each component contains exactly one root. In the original forest, an ordinary vertex is absent from the remaining code exactly when it is a leaf: an occurrence of its label would record the deletion of one of its children. Coding and reconstruction are therefore inverse operations. $\square$

**Example.** Let the ordinary vertices be ordered $a<b<c<d$, let the roots be $\alpha,\beta$, and let the forest edges be $ab,b\alpha,cd,d\beta$.

![A rooted forest with paths from a to alpha and from c to beta; leaf deletion gives the code b, alpha, d, beta](Encoding%20a%20Rooted%20Forest.svg)

*Figure 2. Delete $a,b,c,d$ and record their neighbours $b,\alpha,d,\beta$. The code is $(b,\alpha,d;\beta)$. Numbers beside the ordinary vertices show the deletion order. A root occurs in the code as many times as its degree.*

The first $w-1$ entries are independently chosen from $w+q$ labels; the last is chosen from the $q$ roots. This gives Abel's formula:

$$
\boxed{
A_w(q)=q(q+w)^{w-1}
=\sum_{m=1}^{w}\operatorname{St}(w,m)q_{\underline m}
}
\tag{1}
$$

The combinatorial proof applies to integers $q\geqslant1$. Since both sides are polynomials, the identity extends to an arbitrary variable $x$. For $w=0$, define $A_0(x)=1$ separately: all roots are isolated and the forest is unique.

## Finite differences exclude unused roots

Now take exactly $m$ prescribed labelled roots and require each to be nonisolated. The block construction gives $m!\operatorname{St}(w,m)$ such forests.

Inclusion-exclusion gives the same result. If only $j$ roots may be used, the others remain isolated, and the forest on the ordinary vertices and allowed roots can be chosen in $A_w(j)$ ways. Thus, for $w\geqslant1$,

$$
m!\operatorname{St}(w,m)
=\sum_{j=0}^{m}(-1)^{m-j}\binom mj A_w(j)
=\Delta^m A_w(0)
$$

Here $\Delta f(x)=f(x+1)-f(x)$ and $A_w(0)=0$. The finite difference therefore has a concrete meaning: it excludes constructions leaving at least one prescribed root unused.

For star forests, the same count gives

$$
m!S(w,m)=\Delta^m(x^w)\big|_{x=0}
=\sum_{j=0}^{m}(-1)^{m-j}\binom mj j^w
$$

For example, $S(4,2)=s_2([3,1])+s_2([2,2])=4+3=(2^4-2)/2!$. The positive sum groups objects by block type; the alternating sum removes empty blocks. These are two counts of the same set.

For three ordinary vertices and two roots, the total forest count is $A_3(2)=50$. There are $A_3(1)=16$ forests with each specified root isolated. Both roots cannot be isolated simultaneously. Thus $50-16-16=18=2!\operatorname{St}(3,2)$, agreeing with Figure 1.

## Distinguished values and r-Stirling numbers

Suppose there are $w\geqslant0$ labelled positions whose values are chosen from two disjoint sets: $r\geqslant0$ distinguished labels and $q\geqslant0$ other labels. There are $(q+r)^w$ sequences. Group them by the number $m$ of labels used from the second set.

Let $c_r(w,m)$ count the constructions before assigning concrete labels to these $m$ values. Positions with a distinguished value are attached to one of the $r$ prescribed labels; the other positions are partitioned into $m$ nonempty unordered blocks. Then

$$
(q+r)^w=\sum_{m=0}^{w}c_r(w,m)q_{\underline m}
$$

Adding $r$ separate marker elements to the positions gives an ordinary partition of a $(w+r)$-element set into $m+r$ blocks, with all markers in different blocks. This defines the **$r$-Stirling numbers of the second kind** [1, 2]. In the notation using the full sizes of the set and partition,

$$
\boxed{c_r(w,m)=\left\{\begin{matrix}w+r\\m+r\end{matrix}\right\}_r}
\tag{2}
$$

Here $r$ is the number of distinguished elements; it does not denote the number of nontrivial components of an SPF type. The number $m$ counts blocks without distinguished elements, and the full number of blocks is $m+r$.

**Graph model.** Represent each block containing a distinguished label by a star centred at that label. Represent each block without a distinguished label by a star centred at its least element. This centre is uniquely determined, so each partition corresponds to one forest. Distinguished vertices lie in different components; singleton blocks give isolated vertices. We do not choose arbitrary trees inside these blocks, which would introduce an additional tree factor.

Choosing the $j$ positions assigned nondistinguished values gives

$$
c_r(w,m)=\sum_{j=m}^{w}\binom wj r^{w-j}S(j,m)
$$

For $r=0$, these are ordinary Stirling numbers: $c_0(w,m)=S(w,m)$. We use $S(0,0)=1$ and $0^0=1$, corresponding to the unique empty choice. The formula defines a polynomial in $r$; the partition count applies to integers $r\geqslant0$.

> [!note] Two indexing conventions
> The literature uses both full-size indices $w+r,m+r$ and shifted indices $w,m$; [2] uses the latter. The name “$r$-Stirling number” alone is therefore insufficient when comparing tables. Here braces always use full sizes, while $c_r(w,m)$ uses the number of ordinary elements and the number of blocks without markers.

## Why forest coefficients are r-Stirling numbers

Take a construction counted by $\operatorname{St}(k,m)$: $k\geqslant1$ ordinary labelled vertices and $m$ added roots without individual labels, each nonisolated. Encode the forest by deleting ordinary leaves. The deletion order depends only on ordinary labels, so the roots need not be named in advance.

Call the last recorded root $\rho_0$. The first $k-1$ code positions may contain:

- The $k$ ordinary labels and $\rho_0$: each of these $k+1$ labels may occur any number of times, including zero.
- The other $m-1$ roots: each must occur at least once, because it is nonisolated and does not occupy the final position.

Equal occurrences of one of the latter roots form a block of positions. These roots have no individual names, giving $m-1$ unordered nonempty blocks. This is exactly a construction counted by $c_{k+1}(k-1,m-1)$.

Conversely, given such a construction, add a root for each unlabelled block, append $\rho_0$ to the code, and reconstruct the forest. All roots are nonisolated. We have a bijection, not merely equality of polynomial coefficients:

$$
\boxed{
\operatorname{St}(k,m)
=c_{k+1}(k-1,m-1)
=\left\{\begin{matrix}2k\\k+m\end{matrix}\right\}_{k+1}
},\qquad 1\leqslant m\leqslant k
\tag{3}
$$

In the partition on the right, marker elements represent **allowed code values**, while ordinary elements represent **code positions**. Even when a value is the label of a vertex of the original forest, its marker and a code position remain different objects.

> [!example] An example of the bijection
> For the forest in Figure 2, the final root is $\rho_0=\beta$. The first three code positions are $(b,\alpha,d)$: position one is attached to distinguished label $b$, position three to distinguished label $d$, and position two forms the sole block without a marker. There are five distinguished labels: $a,b,c,d,\rho_0$. This gives a partition of eight elements into six blocks with five separated markers, an object counted by $\left\{\begin{smallmatrix}8\\6\end{smallmatrix}\right\}_5$.

Thus row $k$ of the forest table corresponds to parameter $r=k+1$. For example, $16,9,1$ belong to $r=4$, while $125,91,18,1$ belong to $r=5$. The whole forest table is not a table for one fixed $r$.

### Two graph interpretations of the number 91

A forest on four ordinary vertices with two added roots has ordinary block sizes $[3,1]$ or $[2,2]$. Therefore,

$$
\operatorname{St}(4,2)=4\cdot16+3\cdot3^2=64+27=91
$$

The first term chooses the singleton and a tree on the other three vertices with their root. The second chooses one of three pair partitions and one of three trees on each pair with its root.

> [!example]- All 27 possibilities for two pairs
> ![Three partitions of four ordinary vertices into two pairs, with nine independent tree choices for each partition](Twenty%20Seven%20Rooted%20Forests.svg)
>
> *Figure 3. All $27$ possibilities from the author's research drawing are retained, regrouped by $ab\mid cd$, $ac\mid bd$, and $ad\mid bc$. Within each panel, rows vary the tree on the first pair and columns vary the tree on the second. Roots are coloured and have no individual labels.*

Now count the same forests through their codes. Call the final root $\rho_0$ and the other root $\rho_1$. The first three positions must contain $\rho_1$ at least once. All other values are chosen from $a,b,c,d,\rho_0$. Grouping by the number of occurrences of $\rho_1$ gives

$$
\operatorname{St}(4,2)
=\binom31 5^2+\binom32 5+1
=75+15+1=91
$$

A root's number of occurrences equals its degree in the graph. The first sum therefore groups forests by component sizes; the second groups them by the degree of the root that does not end the code. The individual counts $64,27$ and $75,15,1$ need not match: they partition the same set of forests into different classes.

## Why one power admits different expansions

The shifted power $(x+a)^w$ and the power $x^w$ are related by a change of variable. For any numerical $a$, the formula for $c_a$ gives

$$
x^w=\sum_{m=0}^{w}c_a(w,m)(x-a)_{\underline m}
$$

For integers $a\geqslant0$ and $x\geqslant a$, this counts sequences by the number of values used outside the distinguished set of size $a$. At other values, the polynomial identity remains valid, but its individual terms need not count objects.

For the square:

$$
\begin{aligned}
x^2&=x_{\underline2}+x\\
x^2&=(x-1)_{\underline2}+3(x-1)+1\\
x^2&=(x-4)_{\underline2}+9(x-4)+16
\end{aligned}
$$

The coefficients in the last row also equal $\operatorname{St}(3,3)$, $\operatorname{St}(3,2)$, and $\operatorname{St}(3,1)$. In general, (3) gives

$$
x^w=\sum_{m=0}^{w}
\operatorname{St}(w+1,m+1)(x-w-2)_{\underline m}
$$

For graphs, this passage is explained by the rooted-forest code. For polynomials, the basis changes: for each fixed $a$, the polynomials $(x-a)_{\underline m}$ have distinct degrees and leading coefficient $1$. They therefore form a basis, and the expansion in that basis is unique.

## The discrete Taylor formula

**Theorem.** For a polynomial $P$ of degree at most $d$ and any $a$,

$$
\boxed{
P(x)=\sum_{m=0}^{d}\frac{\Delta^mP(a)}{m!}(x-a)_{\underline m}
}
$$

This is Newton's formula for equally spaced nodes, the polynomial analogue of a Taylor series [3]. The notation $\Delta^mP(a)$ means the value of the $m$th finite difference at $a$.

> [!proof]- Extracting a coefficient by a finite difference
> **Proof.** We have $\Delta(x-a)_{\underline j}=j(x-a)_{\underline{j-1}}$. After $m$ applications of $\Delta$ and substitution of $x=a$, the result is $m!$ when $j=m$ and zero when $j\ne m$. Applying this to the unique expansion of $P$ in the stated basis gives the coefficient $\Delta^mP(a)/m!$. $\square$

In particular,

$$
c_a(w,m)=\frac{\left.\Delta^m(x^w)\right|_{x=a}}{m!}
=\frac1{m!}\sum_{j=0}^{m}(-1)^{m-j}\binom mj(a+j)^w
$$

For an integer $a\geqslant0$, the last expression excludes sequences that omit at least one of $m$ required labels. The other $a$ labels may be absent. Division by $m!$ removes the numbering of the required labels.

**Scope.** For an arbitrary function, equality to an infinite Newton series requires additional conditions. For example, $\sin(\pi x)$ vanishes at every integer, and all its finite differences at zero vanish, but the function itself is not zero. For polynomials, the sum is finite and this difficulty does not arise.

## Verification and further connections

All general identities above have been proved. Bijection (3) follows from reversible forest coding. It complements the [[Forest Coefficients and Abel Polynomials|derivation from SPF identities]] and explains why the two combinatorial counts agree.

An independent check enumerated edge sets for $1\leqslant k\leqslant4$ ordinary vertices and $1\leqslant q\leqslant3$ prescribed roots, tested acyclicity and the presence of exactly one root per component, then compared codes and position partitions. It found the $9$ constructions in Figure 1, the $27$ in Figure 3, and $91$ constructions for $k=4,m=2$. Grouping the last set by block sizes and by the degree of the root not ending the code gave $64+27$ and $75+15+1$, respectively. Separately, sums over types, the formula using ordinary Stirling numbers, and finite differences were compared through degree $8$; this was an algebraic check, not graph enumeration.

Within PMG, this note fixes the ordinary Stirling numbers of the second kind $S(w,m)$, their extension $c_r(w,m)$ with distinguished elements, and the exact position of forest coefficients within that extension. A general classification of Stirling-number families, including first-kind numbers and other block restrictions, lies outside PMG and belongs to a separate project on combinatorics and partition algebra.

This note is based on the author's research within PMG. The two figures showing complete sets of forests were adapted from those materials; labels and roots were added to identify the counted objects unambiguously.

## References

1. Andrei Z. Broder. *The r-Stirling numbers*. Discrete Mathematics 49 (1984), 241-259. [DOI](https://doi.org/10.1016/0012-365X(84)90161-4), [open Stanford technical report](https://i.stanford.edu/pub/cstr/reports/cs/tr/82/949/CS-TR-82-949.pdf). Definition by separated distinguished elements; indices denote full sizes.
2. Grzegorz Serafin. *Identities behind some congruences for r-Bell and derangement polynomials*. Research in Number Theory 6, 39 (2020). [Open text, §2.1](https://link.springer.com/article/10.1007/s40993-020-00216-y). Shifted indexing, the expansion of $(x+r)^w$, and the finite-difference formula.
3. NIST Digital Library of Mathematical Functions. [§3.3(iv), Newton's Interpolation Formula](https://dlmf.nist.gov/3.3.iv). Newton's formula in terms of divided differences; for equally spaced nodes it is expressed using finite differences.

