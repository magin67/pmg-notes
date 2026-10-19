---
title: "Symmetric Polyforms: Types and Normalizations"
date: 2026-10-19
updated: 2026-10-20
revision: 5
source_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: symmetric-polyforms-types-and-normalizations
lang: en
description: "Symmetry under vertex permutations, sums of partition forms of a given type, repeated blocks, and principal symmetric polyforms."
order: 1
---

The sum of all partition forms of one type is invariant under every permutation of the basis vertices. Such sums provide natural examples of symmetric polyforms (SPFs). Sums of different types can nevertheless represent the same polyform: the familiar tetrahedron identity reads $E_4[1,1]=E_4[2,0]$.

This note defines symmetry, specifies the types and normalization of the sums $E_n[\lambda]$, and introduces principal symmetric polyforms (principal SPFs), whose terms have one nontrivial component. The main question for the continuation of the series is how to express a symmetric sum of an arbitrary type in terms of the principal polyform of the same grade.

We use the [[Basic Objects and Operations of Polyform Algebra|algebra of forms]] and [[Partition Forms and the Tetrahedron Identity|partition forms]]. The definition of $E_n[\lambda]$ is retained from the note on [[Constructing Structural Identities#From local identities to symmetric sums|constructing structural identities]]. The algebraic part requires no choice of graph or metric.

## Vertex permutations and symmetry

Fix a set $A=\{a_1,\ldots,a_n\}$ of independent basis vertices of a real vector space $V$, where $n\geqslant2$. As in the PMG core, $\varepsilon(a_i)=1$ and $W=\ker\varepsilon$.

A vertex permutation $\sigma$ acts by $\sigma a_i=a_{\sigma(i)}$. This action extends linearly to $V$ and then to exterior products and forms:

$$
\sigma(XY)=(\sigma X)(\sigma Y),\qquad
\sigma[X,Y]=[\sigma X,\sigma Y]
$$

A permutation preserves the affine weight and commutes with the boundary operator: $\partial(\sigma X)=\sigma(\partial X)$. The latter equality follows directly from the formula for a simplex boundary. The action therefore preserves the space of boundaries, grades, and the product of forms.

> [!info] Symmetric polyform (SPF)
> **Definition.** A polyform $P$ on boundaries is **symmetric on $A$** if
>
> $$
> \sigma P=P\qquad\text{for all }\sigma\in S_n
> $$
>
> Here $S_n$ denotes the group of all permutations of the chosen vertex set.

The permutation acts simultaneously on all occurrences of vertices in both arguments of every form. Coefficients remain fixed real numbers. An SPF may contain several grades; since permutations preserve grade, each of its grade components is also symmetric.

**Example.** On three vertices $a,b,c$, the polyform

$$
e+[(ab)]^2+[(ac)]^2+[(bc)]^2+[(abc)]^2
$$

is symmetric. Permutations rearrange the three pair forms and may reverse the sign of the boundary $(abc)$. The sign disappears in the quadratic form.

Symmetry refers to the specified basis vertex set. If a fourth vertex $d$ is added, the sum $[(ab)]^2+[(ac)]^2+[(bc)]^2$ remains invariant under permutations of $a,b,c$, but is no longer symmetric on the whole set $A$. For example, exchanging $c\leftrightarrow d$ gives the sum of pair forms on $a,b,d$. These forms differ: in an expansion in basis forms, the coefficient of $[c,c]$ is $2$ in the first sum and $0$ in the second. Invariance only under a chosen subgroup of permutations may be called **partial symmetry**, with the subgroup explicitly specified.

### Properties to distinguish

| Property | What is transformed |
|---|---|
| Symmetry under vertex permutations | Basis vertices are relabeled simultaneously in all arguments |
| Symmetry under transposition | The arguments are exchanged: $[X,Y]^{\mathsf T}=[Y,X]$ |
| Commutativity of the product of forms | The order of factors is exchanged: $FG=GF$ |

For example, the form $[(ab)]^2$ equals its transpose, but on the set $\{a,b,c\}$ it is not invariant under $b\leftrightarrow c$. Commutativity of the product of forms holds throughout the algebra and does not by itself establish symmetry under vertex permutations.

## Partitions and types

A partition $\pi=B_1|\cdots|B_q$ of $A$ consists of nonempty pairwise disjoint blocks. Here **“block”** and **“component of a partition”** mean the same thing. Recall the associated exterior object and form:

$$
X_\pi=(B_1)\cdots(B_q),\qquad
q_\pi=[X_\pi]^2
$$

Products of boundaries are exterior products by default. The order of vertices within the blocks and the order of the blocks themselves may change the sign of $X_\pi$, but not the form $q_\pi$. A singleton block contributes the boundary $(a_i)=1$ and the factor $e=[1,1]$ in the product of forms.

**Definition.** The full type of a partition form in the given representation is the list of grades of its block boundaries:

$$
\lambda(\pi)=[|B_1|-1,\ldots,|B_q|-1]
$$

The parts are arranged in nonincreasing order. The size of a block is its number of vertices, and the corresponding part of the type is one less than that size.

Let the positive parts of the type be $k_1,\ldots,k_m$. Write $k$ for their sum and $\ell$ for the number of singleton blocks. Then

$$
k=\sum_{i=1}^m k_i=\operatorname{gr}q_\pi,\qquad
n=k+m+\ell,\qquad q=m+\ell=n-k
$$

The full type is written as $[k_1,\ldots,k_m,0^\ell]$. The notation $0^\ell$ means $\ell$ repetitions of zero in the list. It indicates the multiplicity of a part, not a numerical power.

| Partition | Block sizes | Full type | Grade |
|---|---|---|---:|
| $ab\mid cd$ | $[2,2]$ | $[1,1]$ | 2 |
| $abc\mid d$ | $[3,1]$ | $[2,0]$ | 2 |
| $abc\mid de\mid f$ | $[3,2,1]$ | $[2,1,0]$ | 3 |
| $ab\mid c\mid d\mid e$ | $[2,1,1,1]$ | $[1,0^3]$ | 1 |

The positive list $[k_1,\ldots,k_m]$ is a partition of the **integer** $k$. The partition $\pi$ is a partition of the **vertex set**. A single integer type usually corresponds to many set partitions. A positive type is admissible on $n$ vertices if $k+m\leqslant n$; then $\ell=n-k-m$.

### When zeros may be omitted

For fixed $n$, the positive parts uniquely determine the number of zeros. We therefore allow the abbreviation

$$
E_n[k_1,\ldots,k_m]
=E_n[k_1,\ldots,k_m,0^{\,n-k-m}]
$$

For example, $E_4[2]=E_4[2,0]$ and $E_6[2,1]=E_6[2,1,0]$. We will display the zeros when the number of singleton blocks or a change in that number needs to be explicit. In $E_4[1,1]=E_4[2,0]$, the zero emphasizes that each three-vertex block on the right is accompanied by one singleton vertex.

**Remark.** A type refers to a partition and to a chosen representation of a sum of forms. Structural identities relate sums of different types, so the type of an expression is not a uniquely determined property of the polyform itself. In PMG terminology, homogeneity means a single grade; it does not require all terms to have the same type.

## The symmetric sum of a given type

> [!info] The basic normalization
> **Definition.** For an admissible type $\lambda$, set
>
> $$
> \boxed{E_n[\lambda]=\sum_{\pi:\,\lambda(\pi)=\lambda}q_\pi}
> \tag{1}
> $$
>
> The sum runs over partitions of the fixed set $A$ into **unordered blocks**. Each partition occurs exactly once, with coefficient $1$.

If zeros are omitted from $\lambda$, they are restored using $n$ before applying (1). The subscript $n$ specifies the cardinality of the chosen set; when several vertex sets are compared, the sets themselves must also be specified.

**Proposition.** The polyform $E_n[\lambda]$ is symmetric.

**Proof.** For every permutation $\sigma$, one has $\sigma q_\pi=q_{\sigma\pi}$, where $\sigma\pi$ is obtained by relabeling the vertices in each block. The permutation preserves block sizes and bijectively permutes all partitions of the given type. Hence the sum (1) is unchanged. $\square$

On four vertices $a,b,c,d$, we obtain

$$
E_4[1,1]=[(ab)(cd)]^2+[(ac)(bd)]^2+[(ad)(bc)]^2
$$

$$
E_4[2,0]=[(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2
$$

In the first sum, $ab|cd$ and $cd|ab$ are not counted as different partitions. Similarly, permuting vertices within a block does not create a new term.

The definition sums over partitions, rather than all forests of the given type. A single partition may have several tree realizations. For example, there are three trees on three vertices, each giving the form $[(abc)]^2$. The sum of these three forms is $3E_3[2]$, whereas $E_3[2]$ counts the partition $abc$ only once.

## Representation size and factorial factors

Let $\lambda=[k_1,\ldots,k_m]$ contain positive parts, with $k=\sum_i k_i$ and $\ell=n-k-m\geqslant0$. For $j\geqslant1$, let $\mu_j$ denote the number of occurrences of $j$ in this list:

$$
\mu_j=\#\{i:k_i=j\},\qquad \sum_{j\geqslant1}\mu_j=m
$$

**Definition.** The **size of a polyform representation** is the number of terms in the chosen expression as a sum of forms with coefficients. When the representation is specified, we will simply say **size**. It depends on the expression: equal polyforms may have representations of different sizes.

In the basic normalization, $\#E_n[\lambda,0^\ell]$ denotes the size of representation (1), namely the number of partitions of the given type. Each partition occurs once, with coefficient $1$.

> [!info] The size of a symmetric sum
> **Theorem.** With normalization (1),
>
> $$
> \boxed{
> \#E_n[\lambda,0^\ell]
> =\frac{n!}{\ell!\displaystyle\prod_{i=1}^m(k_i+1)!\displaystyle\prod_{j\geqslant1}\mu_j!}
> }
> \tag{2}
> $$
>
> All products are finite: absent parts have $\mu_j=0$, and $0!=1$.

> [!note]- Proof
> **Proof.** Arrange all $n$ vertices in a row; there are $n!$ ways to do so. Divide the row into $m$ consecutive groups of sizes $k_1+1,\ldots,k_m+1$, followed by $\ell$ singleton groups.
>
> The internal order of the $i$-th nontrivial group does not affect its block, giving the divisor $(k_i+1)!$. Permutations of the $\mu_j$ groups of the same size $j+1$ also leave the partition unchanged, giving the divisor $\mu_j!$. Finally, the remaining vertices form an unordered collection of singleton blocks, so we divide by $\ell!$.
>
> Each partition is counted as many times as the product of these factors. Dividing $n!$ by that product gives (2). $\square$

| Sum | Count from formula (2) | Size |
|---|---|---:|
| $E_4[1,1]$ | $4!/((2!)^2\,2!)$ | 3 |
| $E_4[2,0]$ | $4!/3!$ | 4 |
| $E_5[1,0^3]$ | $5!/(3!\,2!)$ | 10 |
| $E_5[2,1]$ | $5!/(3!\,2!)$ | 10 |
| $E_6[1,1,1]$ | $6!/((2!)^3\,3!)$ | 15 |
| $E_6[2,1,0]$ | $6!/(3!\,2!)$ | 60 |

### When blocks are distinguishable

It is sometimes convenient to temporarily number the nontrivial blocks, prescribing size $k_i+1$ for block $i$. Each collection of $\mu_j$ blocks of the same size can then be assigned to the corresponding numbers in $\mu_j!$ ways. If singleton blocks remain unordered, the resulting sum equals

$$
\left(\prod_{j\geqslant1}\mu_j!\right)E_n[\lambda,0^\ell]
$$

If all singleton blocks are also numbered, an additional factor of $\ell!$ appears. These are different conventions for enumerating terms. Before collecting like terms, the size increases by the same factor.

For example, distinguishing the two blocks of size $2$ changes $E_4[1,1]$ into $2E_4[1,1]$. For type $[1,0^3]$, the sole nontrivial block is already distinguished by its size, whereas numbering the three singleton vertices gives a factor of $3!$.

When using the names “compact” and “full” sum, one must specify which blocks are distinguishable. The basic notation $E_n[\lambda]$ always means normalization (1), with no implicit factorial factors.

## Symmetrization: sum and average

Any two partitions of the same type are related by a vertex permutation: match blocks of equal size and choose bijections between their vertices. This set of partitions is called an **orbit** of the action of $S_n$.

For a fixed partition $\pi$ of type $[k_1,\ldots,k_m,0^\ell]$, summing over all permutations gives

$$
\sum_{\sigma\in S_n}\sigma q_\pi
=\ell!\left(\prod_{i=1}^m(k_i+1)!\right)
\left(\prod_{j\geqslant1}\mu_j!\right)E_n[\lambda,0^\ell]
$$

**Proof.** Every partition in the orbit is obtained by the same number of permutations. To find this number, it suffices to consider permutations preserving the original partition: one can permute vertices within blocks, blocks of equal size, and singleton blocks. The number of these permutations is the factor multiplying $E_n$ in the formula. $\square$

Dividing by $n!$ and using (2) yields the average over permutations:

$$
\boxed{
\frac1{n!}\sum_{\sigma\in S_n}\sigma q_\pi
=\frac{E_n[\lambda,0^\ell]}{\#E_n[\lambda,0^\ell]}
}
\tag{3}
$$

Thus $E_n[\lambda]$ is the sum over the partitions in an orbit, with unit coefficients. Averaging a single form over permutations gives the sum over partitions of its type divided by the size of that sum.

**Corollary.** Every symmetric polyform in the linear span of partition forms on $A$ can be expressed as a linear combination of the sums $E_n[\lambda]$.

> [!note]- Proof
> **Proof.** Choose any representation $P=\sum_\pi c_\pi q_\pi$. By symmetry,
>
> $$
> P=\frac1{n!}\sum_{\sigma\in S_n}\sigma P
> =\sum_\pi c_\pi\left(\frac1{n!}\sum_{\sigma\in S_n}\sigma q_\pi\right)
> $$
>
> By (3), each parenthesized expression is a scalar multiple of the sum of its type. Grouping by type gives the required representation. $\square$

The corollary establishes the existence of such a representation. It does not assert uniqueness: structural identities relate the sums $E_n[\lambda]$ themselves. Checking the symmetry of an arbitrary expression requires taking identities between forms into account, rather than merely comparing the displayed coefficients. The proof does not require choosing a basis of the space of partition forms.

## Principal symmetric polyforms

> [!info] Principal symmetric polyform (principal SPF)
> **Definition.** For $1\leqslant k\leqslant n-1$, the principal symmetric polyform (principal SPF) of grade $k$ is
>
> $$
> \boxed{
> E_n[k]=E_n[k,0^{\,n-k-1}]
> =\sum_{\substack{B\subseteq A\\|B|=k+1}}[(B)]^2
> }
> \tag{4}
> $$
>
> Each partition in this sum has exactly one nontrivial block; all remaining vertices form singleton blocks.

Choosing the nontrivial block determines the partition completely. Hence the size of the principal polyform in representation (4) is

$$
\#E_n[k]=\binom{n}{k+1}
$$

This is also the special case of (2) with $m=1$, $\mu_k=1$, and $\ell=n-k-1$.

In grade $1$, we sum the forms of all pairs:

$$
E_n[1]=\sum_{1\leqslant i<j\leqslant n}[(a_i a_j)]^2
$$

By the definition of the [[Laplacian - graph, electrical network and quadratic form|Laplacian]], this is the Laplacian polyform of the complete graph with unit conductances. This interpretation does not require a graph to be chosen in advance when defining $E_n[1]$.

In the next grade, $E_n[2]$ sums the boundary forms of all three-vertex subsets. In the top grade, the size is $1$:

$$
E_n[n-1]=[(a_1\ldots a_n)]^2=T_n
$$

Thus the [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|spanning-tree form]] is the principal symmetric polyform of the top grade. The name “principal” refers to the single nontrivial component in each term; it does not mean that the whole partition is connected when singleton vertices are present.

### Grade zero

There is a unique partition into $n$ singleton blocks, and its form is $e$. Under normalization (1),

$$
E_n[0^n]=e
$$

Definition (4) of principal polyforms applies only to positive $k$. Formally substituting $k=0$ into its subset sum would give

$$
\sum_{\substack{B\subseteq A\\|B|=1}}[(B)]^2=ne
$$

The difference arises because this sum makes $n$ choices of a distinguished singleton block within the same partition. We therefore denote the unit form by $e$ or $E_n[0^n]$, without extending the formula for choosing a nontrivial block to this case.

## Type, coefficients, and metric evaluation

On four vertices, the [[Partition Forms and the Tetrahedron Identity#The tetrahedron identity|tetrahedron identity]] gives

$$
E_4[1,1]=E_4[2,0]=E_4[2]
$$

The representations on the left and right have sizes $3$ and $4$, respectively. This is one polyform of grade $2$ with two representations of different types and sizes. Since all coefficients are $1$, the coefficient sums here equal the sizes.

On five vertices, the [[Constructing Structural Identities#From local identities to symmetric sums|structural identities series]] proves

$$
E_5[2,1]=3E_5[3,0]=3E_5[3]
$$

After expanding the sums $E$, the representation on the left has size $10$ with coefficients $1$, whereas the one on the right has size $5$ with coefficients $3$. The coefficient sums are $10$ and $15$, respectively. Thus size and coefficient sum are different characteristics of a representation; both may change when passing to an equal expression.

Metric evaluation behaves differently. Once a metric is chosen, the map $[X,Y]\mapsto X\cdot Y$ is linear on the space of forms and therefore takes the same value on equal polyforms. In the resistance metric of a connected graph, the normalized evaluation of a quadratic form is

$$
\frac{u_M([X]^2)}{u_M(e)}=X^2=X\cdot X
$$

Here $[X]^2$ is a form, whereas $X^2$ is its numerical quadratic norm in the PMG convention. The detailed definition appears in the [[Laplacian Exponential#The potential of a form|note on the Laplacian exponential]]. Symmetry of a sum under vertex permutations does not require all its terms to have the same evaluation in a chosen metric.

## Toward the fundamental identity

This note proves the invariance of the sums $E_n[\lambda]$, the formula for the size of their representations, and the representation of a symmetric polyform in the space of partition forms as a combination of these sums. The equalities on four and five vertices are proved in [[Partition Forms and the Tetrahedron Identity]] and [[Constructing Structural Identities]].

The next question concerns dependencies between symmetric sums: for a fixed grade $k$, can every admissible type be expressed in terms of $E_n[k]$, and how is the coefficient computed? This is the subject of [[Fundamental Theorem of Symmetric Polyforms]]. Comparing sizes alone does not prove such an equality; an identity in the algebra of forms is required.

This note is based on the author's research within PMG. The definitions of forms and types, and the starting identities, are aligned with the linked public notes in the library.
