---
title: Constructing Structural Identities
date: 2026-10-18
updated: 2026-10-18
revision: 1
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: constructing-structural-identities
lang: en
description: "Types of partition forms, the tetrahedron identity for four blocks, examples on five and six vertices, and the passage to symmetric sums."
order: 2
---

An existing structural identity can yield others: relabel the vertices, add singleton vertices, multiply both sides by the same form, or add the resulting equalities. This note extends the tetrahedron identity from four vertices to four disjoint blocks. Examples on five and six vertices show how these operations change the types of the terms and how coefficients arise when identities are summed.

We use [[Partition Forms and the Tetrahedron Identity|partition forms and the tetrahedron identity]], together with the [[Basic Objects and Operations of Polyform Algebra#Polyforms and the product of forms|product of forms]]. All equalities hold in the formal algebra of PMG. Their proofs require neither a metric nor numerical norms.

## Types of partition forms

Let $S$ consist of $n$ basis vertices, and let $\pi=B_1|\cdots|B_q$ be a partition of $S$ into nonempty blocks. In the context of set partitions, we use **“block”** and **“component”** as synonyms.

Recall the notation

$$
q_\pi=[(B_1)\cdots(B_q)]^2
$$

The **size of a block** is the number of vertices it contains. If a block has size $s$, its boundary has grade $s-1$. The **type of a form** lists the grades of the block boundaries in the corresponding partition; singleton vertices contribute zero parts.

For example, the block $\{a,b\}$ has size $2$, whereas its boundary $(ab)=b-a$ is a vector of grade $1$. Thus the partition $ab|cd$ has block sizes $[2,2]$ and form type $[1,1]$.

> [!info] The type of a partition form
> **Definition.** The type of the partition form $q_\pi$ in the specified representation is the list
>
> $$
> \lambda(\pi)=[|B_1|-1,\ldots,|B_q|-1]
> $$
>
> The parts are arranged in nonincreasing order. Their sum equals the grade of the form:
>
> $$
> r=\sum_{i=1}^q(|B_i|-1)=n-q
> $$

The positive parts of the type form an integer partition of $r$; the zeros record the singleton blocks. The type defined by grades differs from the list of block sizes.

| Set partition | Block sizes | Form type | Grade |
|---|---|---|---:|
| $ab\mid cd$ | $[2,2]$ | $[1,1]$ | 2 |
| $abc\mid d$ | $[3,1]$ | $[2,0]$ | 2 |
| $abc\mid de$ | $[3,2]$ | $[2,1]$ | 3 |
| $abc\mid de\mid f$ | $[3,2,1]$ | $[2,1,0]$ | 3 |

If there are $m$ positive parts with sum $r$, they account for $r+m$ vertices. The number of singleton blocks is

$$
\ell=n-r-m\geqslant0
$$

For fixed $n$, zeros may be omitted: the type $[2,1]$ on six vertices means the full type $[2,1,0]$. Without specifying the underlying vertex set, this abbreviation does not determine the number of singleton vertices.

**Remark.** A type describes a partition and a chosen expression for a sum of forms. A structural identity may relate sums of different types, so the type of an expression should not be regarded as a uniquely determined property of the polyform itself. In the [[Core specification#Forms and polyform algebra|core specification]], homogeneity means that all terms have the same grade; their types need not coincide.

## Transferring and multiplying identities

Relabeling basis vertices preserves a structural identity: the linear map sending the old basis vertices to the new ones respects the boundary operator and the product. Adding new singleton vertices also preserves the equality. The original space is then embedded in a larger one, and singleton blocks are added to each partition. The grades of the forms remain unchanged, while their full types acquire zero parts.

By bilinearity of the product, $\sum_\pi c_\pi q_\pi=0$ implies, for any fixed form $F$,

$$
\sum_\pi c_\pi q_\pi F=0
$$

Multiplication by a pair form $[(xy)]^2$ has a particularly simple effect.

> [!info] Joining a pair
> **Lemma.** Let $x,y$ be distinct vertices of the fixed set $S$. If they belong to different blocks of the partition $\pi$, then
>
> $$
> q_\pi[(xy)]^2=q_{\pi'}
> $$
>
> Here $\pi'$ is obtained by merging those two blocks. If $x,y$ belong to the same block, then
>
> $$
> q_\pi[(xy)]^2=0
> $$

> [!note]- Proof
> **Proof.** Choose a tree within each block of $\pi$; a singleton block has no edges. By the [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|theorem on edge products]], the product of these edge vectors equals the exterior element of the partition up to sign. Hence the product of the edge forms equals $q_\pi$.
>
> If $x,y$ lie in different blocks, the added pair joins two trees into one. The product gives the boundary of the merged block, and the sign disappears upon passing to the quadratic form. No additional numerical factor occurs.
>
> If $x,y$ lie in the same block, the vector $(xy)$ is a linear combination of the vectors along the path between them in the chosen tree. The exterior product of linearly dependent vectors is zero, so the product of forms is also zero. $\square$

In the nonzero case, the number of blocks decreases by one and the grade increases by one. If the joined blocks have type parts $i$ and $j$, the new type replaces them by $i+j+1$.

For example,

$$
q_{ab|cd}[(ac)]^2=q_{abcd},\qquad
q_{abc|d}[(ab)]^2=0
$$

A new vertex is first added as a singleton block. It can then be attached to a chosen block:

$$
q_{ab|cd|e}[(ae)]^2=q_{abe|cd}
$$

The chosen trees provide a way to compute the product. The pairs need not be edges of any given graph. Multiplication preserves the equality, but may turn it into $0=0$ or produce an identity dependent on those already known.

## The tetrahedron identity for four blocks

Let $A,B,C,D$ be nonempty, pairwise disjoint sets of basis vertices, and let $S=A\cup B\cup C\cup D$. In form subscripts, write $AB$ for $A\cup B$, $BCD$ for $B\cup C\cup D$, and similarly for other unions.

> [!info] The four-block identity
> **Theorem.** The following structural identity holds:
>
> $$
> \boxed{
> \begin{aligned}
> &q_{AB|CD}+q_{AC|BD}+q_{AD|BC}=\\
> &\qquad=q_{A|BCD}+q_{B|ACD}+q_{C|ABD}+q_{D|ABC}
> \end{aligned}
> }
> \tag{1}
> $$
>
> All seven forms have grade $|S|-2$.

> [!note]- Proof
> **Proof.** Choose $a\in A$, $b\in B$, $c\in C$, and $d\in D$. Take the tetrahedron identity on $a,b,c,d$ and add the remaining vertices of $S$ as singleton blocks.
>
> Within each of the four sets, join the chosen vertex to every other vertex of that set. The product of the corresponding forms is
>
> $$
> H=
> \prod_{x\in A\setminus\{a\}}[(ax)]^2
> \prod_{x\in B\setminus\{b\}}[(bx)]^2
> \prod_{x\in C\setminus\{c\}}[(cx)]^2
> \prod_{x\in D\setminus\{d\}}[(dx)]^2
> $$
>
> An empty product of forms means $e$. Multiply both sides of the original identity by $H$. As the factors are applied successively, each new vertex joins the block containing its chosen vertex. By the lemma, none of the seven terms vanishes and every coefficient remains $1$.
>
> For example, $ab|cd$ becomes $AB|CD$, and $a|bcd$ becomes $A|BCD$. This gives all the terms in (1). The form $H$ has grade $|S|-4$, so the resulting grade is $2+(|S|-4)=|S|-2$. $\square$

The same additional blocks on vertices outside $S$ may be appended to every partition in (1). This amounts to multiplying the equality by the form of their partition. Thus the identity can be applied within a larger partition while keeping the other blocks fixed.

## Five vertices and a distinguished argument

Another way to obtain identities extends the [[Partition Forms and the Tetrahedron Identity#A lemma on a zero sum|lemma on a zero sum]].

**Lemma.** Let the exterior elements $X_1,\ldots,X_m$ have the same grade, with $m\geqslant4$, and satisfy $\sum_{j=1}^mX_j=0$. For any chosen index $i$,

$$
\sum_{j\ne i}[X_i+X_j]^2
=(m-3)[X_i]^2+\sum_{j\ne i}[X_j]^2
\tag{2}
$$

> [!note]- Proof
> **Proof.** Expand each quadratic form using the polar form $\{X,Y\}=[X,Y]+[Y,X]$, with no factor of $1/2$:
>
> $$
> \begin{aligned}
> \sum_{j\ne i}[X_i+X_j]^2
> &=(m-1)[X_i]^2+\sum_{j\ne i}[X_j]^2+
> \left\{X_i,\sum_{j\ne i}X_j\right\}\\
> &=(m-1)[X_i]^2+\sum_{j\ne i}[X_j]^2-2[X_i]^2\\
> &=(m-3)[X_i]^2+\sum_{j\ne i}[X_j]^2
> \end{aligned}
> $$
>
> Here we used $\sum_{j\ne i}X_j=-X_i$. $\square$

On five vertices $a,b,c,d,e$, introduce the oriented boundaries

$$
\begin{aligned}
X_a&=(bcde),& X_b&=-(acde),& X_c&=(abde)\\
X_d&=-(abce),& X_e&=(abcd)
\end{aligned}
$$

They have grade $3$ and sum to zero because $\partial^2[abcde]=0$.

**Corollary.** For the distinguished vertex $a$,

$$
\boxed{
\begin{aligned}
&q_{ab|cde}+q_{ac|bde}+q_{ad|bce}+q_{ae|bcd}=\\
&\qquad=2q_{a|bcde}+q_{b|acde}+q_{c|abde}+q_{d|abce}+q_{e|abcd}
\end{aligned}
}
\tag{3}
$$

> [!note]- Proof
> **Proof.** Expanding the boundaries gives
>
> $$
> \begin{aligned}
> X_a+X_b&=-(ab)(cde)\\
> X_a+X_c&=(ac)(bde)\\
> X_a+X_d&=-(ad)(bce)\\
> X_a+X_e&=(ae)(bcd)
> \end{aligned}
> $$
>
> Substitute these equalities into (2) with $m=5$ and $i=a$. The signs disappear in the quadratic forms; the coefficient of $[X_a]^2$ is $m-3=2$. This gives (3). $\square$

All forms in (3) have grade $3$. The left-hand side is a sum of type $[2,1]$, while the right-hand side uses forms of type $[3,0]$. Choosing each of the five vertices as the distinguished one gives five identities. An individual identity is invariant under permutations of the other four vertices, but not under all permutations of the five vertices.

## Two examples on six vertices

### An additional pair

Add singleton vertices $e,f$ to the tetrahedron identity on $a,b,c,d$ and multiply both sides by $[(ef)]^2$. We obtain

$$
\begin{aligned}
&q_{ab|cd|ef}+q_{ac|bd|ef}+q_{ad|bc|ef}=\\
&\qquad=q_{abc|d|ef}+q_{abd|c|ef}+q_{acd|b|ef}+q_{bcd|a|ef}
\end{aligned}
\tag{4}
$$

The grade is $3$. The type on the left is $[1,1,1]$, and that on the right is $[2,1,0]$. The form of the additional pair multiplies each term once, so all coefficients remain equal to one.

### Enlarging one block

In (1), take $A=\{a\}$, $B=\{b\}$, $C=\{c\}$, and $D=\{d,e,f\}$. Move three terms to the right-hand side and isolate the form $q_{abc|def}$:

$$
\begin{aligned}
q_{abc|def}
&=q_{ab|cdef}+q_{ac|bdef}+q_{bc|adef}-\\
&\qquad-q_{a|bcdef}-q_{b|acdef}-q_{c|abdef}
\end{aligned}
\tag{5}
$$

All terms have grade $4$. The formula expresses a form of type $[2,2]$ in terms of forms of types $[3,1]$ and $[4,0]$. It can be obtained directly from the tetrahedron identity by adding singleton vertices $e,f$ and multiplying by $[(de)]^2[(df)]^2$.

**Independent verification of the examples.** Formulas (3)-(5) were also checked by directly expanding the boundaries in the basis of affine vectors $b-a,c-a,\ldots$. If $X=\sum_I x_Iu_I$ in a basis of the corresponding exterior power, then $[X]^2=\sum_{I,J}x_Ix_J[u_I,u_J]$. Exact integer comparison of the coefficients of $[u_I,u_J]$ gives zero difference between the two sides in all three cases. This check uses the definitions of boundaries and forms; the general proofs of extension and polarization are given above.

## From local identities to symmetric sums

To remove the choice of a distinguished vertex, sum the identities obtained from all its possible choices. To express the result, introduce a symmetric sum of a given type.

> [!info] Symmetric sum
> **Definition.** On a fixed set $S$ of $n$ vertices, set
>
> $$
> E_n[\lambda]=\sum_{\pi:\,\lambda(\pi)=\lambda}q_\pi
> $$
>
> The sum runs over partitions of $S$ into unordered blocks. Each partition is counted exactly once.

A permutation of the vertices permutes the terms in this sum, so $E_n[\lambda]$ is a symmetric polyform. In particular, permuting blocks of equal size creates no additional terms. The subscript $n$ indicates the size of the already chosen vertex set; when working with different sets of the same size, the set itself must also be specified.

On four vertices, the tetrahedron identity becomes

$$
E_4[1,1]=E_4[2,0]
$$

**Corollary.** On five vertices,

$$
\boxed{E_5[2,1]=3E_5[3,0]}
\tag{6}
$$

> [!note]- Counting the coefficients
> **Proof.** Add the five equalities (3), choosing each vertex in turn as the distinguished one.
>
> A fixed partition of type $[2,1]$, such as $ab|cde$, occurs on the left twice: when $a$ is distinguished and when $b$ is distinguished. Its total coefficient is $2$.
>
> A fixed partition of type $[3,0]$, such as $a|bcde$, occurs on the right with coefficient $2$ when its singleton vertex $a$ is distinguished, and with coefficient $1$ for each of the other four choices. Its total coefficient is $2+4=6$.
>
> Therefore,
>
> $$
> 2E_5[2,1]=6E_5[3,0]
> $$
>
> Dividing by $2$ gives (6). $\square$

Formula (6) was also checked by directly expanding both symmetric sums in the basis forms $[u_I,u_J]$, without using the local identities (3).

The expression $E_5[2,1]$ contains ten partitions, whereas $E_5[3,0]$ contains five. Hence the sum of coefficients on the left of (6) is $10$, and that on the right is $15$. Equality of polyforms does not imply equality of the sums of coefficients in different representations. If a metric evaluation is subsequently specified, its linearity gives equal numerical values for both sides.

We have established one relation between symmetric sums. General relations for arbitrary types belong to the series on symmetric polyforms.

## Completeness and independence

Extension to four blocks and polarization of a zero sum have been proved under the stated conditions. The examples show how to construct specific relations and count their coefficients. The next question concerns completeness: which relations suffice to express all partition forms in terms of an independent set, and what is the dimension of their linear span? The answer requires a separate proof; the number of constructed identities alone does not establish their independence.

## Connection with the literature

The seven-term pattern in (1), including additional unchanged blocks, has the same partitions and coefficients as Rule 1 in R. Kenyon and D. Wilson's *Boundary Partitions in Trees and Dimers*. Their rule transforms partitions within the framework of a combinatorial pairing. Here the equality is proved directly for the forms $q_\pi$ in the algebra of PMG, without assumptions on graph planarity or a choice of metric.

R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325-1364. [arXiv:math/0608422, version 4, Section 1.2, Rule 1](https://arxiv.org/abs/math/0608422v4). [DOI: 10.1090/S0002-9947-2010-04964-5](https://doi.org/10.1090/S0002-9947-2010-04964-5).
