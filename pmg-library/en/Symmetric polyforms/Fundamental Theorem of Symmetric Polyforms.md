---
title: "Fundamental Theorem of Symmetric Polyforms"
date: 2026-10-19
updated: 2026-10-19
revision: 2
source_revision: 6
status: draft
text_prepared_by: ChatGPT
translation_key: fundamental-theorem-of-symmetric-polyforms
lang: en
description: "Expressing a symmetric sum of any admissible type through a principal polyform: the exact coefficient, a proof by merging blocks, and the connection with representation theory."
order: 2
---

At a fixed positive grade, all symmetric sums of partition forms are proportional to a single principal polyform. The coefficient depends on the number of vertices, the grades of the components, and their multiplicities. We will call this statement the **fundamental theorem of symmetric polyforms**.

The theorem is stated below in the normalization $E_n[\lambda]$, where each partition into unordered blocks is counted once. The idea of the main proof is due to Dmitry Malugin; the exposition was prepared by ChatGPT. An independent explanation using classical representation theory is given at the end.

We use the definitions in [[Symmetric Polyforms - Types and Normalizations|Symmetric Polyforms: Types and Normalizations]] and the properties of the [[Basic Objects and Operations of Polyform Algebra#The boundary operator|boundary operator]]. The main proof requires neither a graph nor a metric.

## Statement and scope

Let $A=\{a_1,\ldots,a_n\}$, $n\geqslant2$, be a basis of a real vector space $V$, and let $W=\ker\varepsilon$ be the space of affine vectors. For a partition $\pi=B_1|\cdots|B_q$ of $A$, the partition form is

$$
q_\pi=[(B_1)\cdots(B_q)]^2
$$

The size of a block is its number of vertices; the grade of its boundary is one less. A singleton block contributes the exterior-product unit $1$, so the corresponding factor in the form is $e$.

Fix positive grades

$$
k_1,\ldots,k_m\geqslant1,\qquad
k=\sum_{i=1}^m k_i,\qquad
\ell=n-k-m\geqslant0
$$

Here $m\geqslant1$ is the number of nontrivial blocks, and $\ell$ is the number of singleton blocks. For each $j\geqslant1$, set

$$
\mu_j=\#\{i:k_i=j\}
$$

The sum $E_n[k_1,\ldots,k_m,0^\ell]$ contains all partitions of this type, each with coefficient $1$. The principal polyform of the same grade is

$$
E_n[k]=E_n[k,0^{\,n-k-1}]
=\sum_{\substack{B\subseteq A\\|B|=k+1}}[(B)]^2
$$

> [!info] Fundamental theorem
> **Theorem.** Under these assumptions, the following identity of forms holds:
>
> $$
> \boxed{
> E_n[k_1,\ldots,k_m,0^\ell]
> =
> \frac{(n-k-1)!\,k!}
> {\ell!\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!}
> E_n[k]
> }
> \tag{1}
> $$
>
> The product over $j$ has only finitely many factors different from $1$.

The number of singleton blocks on the right is $r=n-k-1=\ell+m-1$. Thus $r\geqslant\ell$, with equality when $m=1$. In that case, the coefficient in (1) is $1$.

If there are no singleton vertices, that is, if $\ell=0$, the formula becomes

$$
E_n[k_1,\ldots,k_m]
=
\frac{(m-1)!\,k!}
{\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!}
E_n[k]
$$

This is the case $n=k+m$. Grade zero is treated separately: $E_n[0^n]=e$. Formula (1) applies to positive grades and leaves this convention unchanged.

The factor

$$
\frac{k!}{\displaystyle\prod_i k_i!\displaystyle\prod_j\mu_j!}
$$

has the usual combinatorial interpretation: it counts partitions of a $k$-element set into unordered blocks of sizes $k_1,\ldots,k_m$. To obtain it, distribute the $k$ elements among the blocks and divide by the permutations within blocks and among blocks of equal size. Here the sizes are the **grades** $k_i$. This auxiliary count differs from partitioning the original $n$ vertices into blocks of sizes $k_i+1$.

## Outline of the proof

The main proof has three steps.

1. **A quadratic identity under a zero-sum condition.** By bilinearity of forms, the sum of squares of subset sums can be expressed using the sum of squares of the individual arguments. The zero-sum condition eliminates the polar terms and gives the binomial coefficient in (2).
2. **Merging two blocks.** Identity (2) is applied to oriented boundaries of faces whose sum is zero because $\partial^2=0$. This gives formula (3), replacing a sum of forms with two blocks by a sum of forms with one larger block and a singleton vertex.
3. **Successive merging and counting multiplicities.** Formula (3) is applied successively to all nontrivial blocks. Each step accounts for the choice of the vertex that becomes a singleton, giving a factor of $\ell+1$ when the current number of singleton vertices is $\ell$. Temporarily numbering the nontrivial blocks accounts for repeated grades; removing the numbering yields the coefficient in (1).

## A quadratic identity under a zero-sum condition

The following lemma applies to arbitrary exterior objects of the same grade. They need not be decomposable or representable as simplex boundaries.

> [!info] Subset sums
> **Lemma 1.** Let $X_1,\ldots,X_N$ be exterior objects of the same grade, with $N\geqslant2$, and suppose that
>
> $$
> \sum_{i=1}^N X_i=0
> $$
>
> Then, for $1\leqslant a\leqslant N-1$,
>
> $$
> \boxed{
> \sum_{\substack{I\subseteq\{1,\ldots,N\}\\|I|=a}}
> \left[\sum_{i\in I}X_i\right]^2
> =
> \binom{N-2}{a-1}\sum_{i=1}^N[X_i]^2
> }
> \tag{2}
> $$

> [!note]- Proof
> **Proof.** For $a=1$, the equality follows directly from the sums. Suppose that $a\geqslant2$.
>
> Expand each quadratic form by bilinearity. The form $[X_i]^2$ occurs in $\binom{N-1}{a-1}$ subsets, while the polar form $\{X_i,X_j\}=[X_i,X_j]+[X_j,X_i]$, for $i<j$, occurs in $\binom{N-2}{a-2}$ subsets. Hence
>
> $$
> \sum_{|I|=a}\left[\sum_{i\in I}X_i\right]^2
> =
> \binom{N-1}{a-1}\sum_i[X_i]^2
> +\binom{N-2}{a-2}\sum_{i<j}\{X_i,X_j\}
> $$
>
> The zero-sum condition gives
>
> $$
> 0=\left[\sum_iX_i\right]^2
> =\sum_i[X_i]^2+\sum_{i<j}\{X_i,X_j\}
> $$
>
> Replace the sum of polar forms by $-\sum_i[X_i]^2$. The remaining coefficient is
>
> $$
> \binom{N-1}{a-1}-\binom{N-2}{a-2}
> =\binom{N-2}{a-1}
> $$
>
> This proves (2). $\square$

Equality (2) is an identity in the space of forms. It is proved before applying any numerical evaluation $[X,Y]\mapsto X\cdot Y$.

## Merging two blocks

When positive grades $p$ and $q$ are merged, the larger block has $p+q+1$ vertices. One of the original $p+q+2$ vertices becomes a separate singleton block. The following identity describes this transition for the sum over all partitions involved.

> [!info] Two distinguishable blocks
> **Lemma 2.** Let $p,q\geqslant1$, and let $C$ be a set of $N=p+q+2$ basis vertices. Then
>
> $$
> \boxed{
> \sum_{\substack{B\subseteq C\\|B|=p+1}}
> [(B)(C\setminus B)]^2
> =
> \binom{p+q}{p}
> \sum_{s\in C}[(C\setminus\{s\})]^2
> }
> \tag{3}
> $$

On the left, the block $B$ is distinguished by its position in the expression. If $p=q$, each partition into two unordered blocks is counted twice, once for each choice of the distinguished block. If $p\ne q$, the prescribed size $p+1$ distinguishes the blocks, and there is no repetition.

> [!note]- Proof
> **Proof.** Fix an ordering $C=(c_1,\ldots,c_N)$ and introduce the oriented boundaries
>
> $$
> Y_i=(-1)^{i-1}(c_1\ldots\widehat{c_i}\ldots c_N)
> $$
>
> They all have grade $N-2=p+q$. The identity $\partial^2=0$ gives
>
> $$
> \sum_{i=1}^N Y_i
> =\partial^2[c_1\ldots c_N]=0
> $$
>
> For a subset $B\subset C$, set $D=C\setminus B$. We claim that
>
> $$
> \left[\sum_{c_i\in B}Y_i\right]^2=[(B)(D)]^2
> $$
>
> First place the vertices of $B$ before those of $D$. The part of the sum $\partial[C]$ obtained by deleting one vertex at a time from $B$ is $(B)[D]$. Applying $\partial$ to this part and using $\partial(B)=0$, we obtain
>
> $$
> \sum_{c_i\in B}Y_i
> =\partial\bigl((B)[D]\bigr)
> =(-1)^p(B)(D)
> $$
>
> Returning to the original vertex order may introduce an overall sign, which disappears in the quadratic form. Here $[D]$ denotes the oriented simplex, and $(D)=\partial[D]$ its boundary.
>
> Now apply Lemma 1 to $Y_1,\ldots,Y_N$ and subsets of size $a=p+1$. The coefficient in (2) is
>
> $$
> \binom{N-2}{a-1}=\binom{p+q}{p}
> $$
>
> Each form $[Y_i]^2$ equals $[(C\setminus\{c_i\})]^2$. This gives (3). $\square$

On a set of $p+q+2$ vertices, the right-hand side of (3) is $\binom{p+q}{p}E_{p+q+2}[p+q,0]$. When $p=q$, obtaining the basic normalization $E$ requires dividing the left-hand side by $2$.

For $p=q=1$, both sides of (3) contain a factor of $2$. Cancelling it gives the [[Partition Forms and the Tetrahedron Identity#The tetrahedron identity|tetrahedron identity]]. For $p=2$, $q=1$, we obtain $E_5[2,1]=3E_5[3,0]$.

**Remark.** Merging applies to the entire sum in (3). It does not assert that an individual form $[(B)(D)]^2$ equals a single form of a larger block.

## Proof of the fundamental theorem

The main counting difficulty is that every merger increases the number of singleton vertices, while some positive grades may coincide. Temporarily number the nontrivial blocks, leaving the singleton blocks unordered. This lets us account for the two kinds of multiplicity separately.

> [!note]- Proof of the theorem
> **Proof.** Require block $i$ to have size $k_i+1$. Under this numbering, each original partition of type $[k_1,\ldots,k_m,0^\ell]$ occurs $\prod_j\mu_j!$ times: numbers may be permuted only among blocks of equal size. Thus the sum with numbered nontrivial blocks is
>
> $$
> \left(\prod_j\mu_j!\right)E_n[k_1,\ldots,k_m,0^\ell]
> $$
>
> For $m=1$, the theorem already holds. Suppose that $m\geqslant2$. Fix the blocks numbered $3,\ldots,m$ and a set $F$ of $\ell$ singleton vertices. The first two blocks occupy the remaining set $C$, which has $k_1+k_2+2$ vertices.
>
> Apply (3) with $p=k_1$, $q=k_2$, and multiply both sides by the forms of the remaining blocks. On the right, the first two blocks are replaced by one block of grade $k_1+k_2$ and a singleton vertex $s$. The merged block retains a distinguished number, and the other nontrivial blocks retain their numbers.
>
> Sum over all admissible choices of the fixed data: the blocks numbered $3,\ldots,m$ and the sets $F$. Each partition of the new type with numbered nontrivial blocks occurs exactly $\ell+1$ times. Indeed, it has $\ell+1$ singleton vertices, any of which may be chosen as the vertex $s$ separated off by merging. Once $s$ is chosen, the original fixed data are recovered uniquely: $F$ consists of the other singleton vertices, and $C$ is the union of the merged block and $\{s\}$.
>
> Consequently, the first merger multiplies the sum of the new type, with block numbers retained, by
>
> $$
> (\ell+1)\binom{k_1+k_2}{k_1}
> $$
>
> If the merged block has the same size as another block, their numbers remain distinct. No further multiplication or division by a multiplicity is therefore needed at this step.
>
> Next merge the distinguished block successively with the blocks of grades $k_3,\ldots,k_m$. The factor accounting for singleton vertices is $\ell+2$ at the next step, then $\ell+3$, and so on. After $m-1$ mergers, a single nontrivial block of grade $k$ remains. We obtain
>
> $$
> \left(\prod_j\mu_j!\right)E_n[k_1,\ldots,k_m,0^\ell]
> =
> \left(\prod_{t=1}^{m-1}(\ell+t)\right)
> \left(\prod_{t=2}^{m}\binom{k_1+\cdots+k_t}{k_t}\right)
> E_n[k]
> $$
>
> The first product is
>
> $$
> \prod_{t=1}^{m-1}(\ell+t)
> =\frac{(\ell+m-1)!}{\ell!}
> =\frac{(n-k-1)!}{\ell!}
> $$
>
> In the second product, the factorials of successive partial sums cancel:
>
> $$
> \prod_{t=2}^{m}\binom{k_1+\cdots+k_t}{k_t}
> =\frac{k!}{\prod_{i=1}^m k_i!}
> $$
>
> Dividing by $\prod_j\mu_j!$ gives (1). For $m=1$, both empty products equal $1$, so the same final formula remains valid. $\square$

Thus the factor $(n-k-1)!/\ell!$ is obtained by counting specific repetitions during merging. The proof does not infer equality of polyforms from the ratio of their representation sizes.

## Examples and normalization checks

The table displays zeros explicitly to show how the number of singleton blocks changes.

| Original type | $\ell$ | Multiplicities of positive parts | Identity |
|---|---:|---|---|
| $[1,1]$ on 4 vertices | 0 | $\mu_1=2$ | $E_4[1,1]=E_4[2,0]$ |
| $[2,1]$ on 5 vertices | 0 | $\mu_1=\mu_2=1$ | $E_5[2,1]=3E_5[3,0]$ |
| $[1,1,1]$ on 6 vertices | 0 | $\mu_1=3$ | $E_6[1,1,1]=2E_6[3,0^2]$ |
| $[2,1,0]$ on 6 vertices | 1 | $\mu_1=\mu_2=1$ | $E_6[2,1,0]=6E_6[3,0^2]$ |
| $[2,2]$ on 6 vertices | 0 | $\mu_2=2$ | $E_6[2,2]=3E_6[4,0]$ |

For example, for three components of grade $1$, the coefficient is

$$
\frac{(6-3-1)!\,3!}{0!\,(1!)^3\,3!}=2
$$

For type $[2,1,0]$, the positive grades are distinct, so there is no divisor $2!$ for permuting the nontrivial blocks:

$$
\frac{(6-3-1)!\,3!}{1!\,2!\,1!}=6
$$

Two useful families follow from (1):

$$
E_n[1,1]=(n-3)E_n[2],\qquad n\geqslant4
$$

$$
E_n[\underbrace{1,\ldots,1}_{m}]
=\frac{(n-m-1)!}{(n-2m)!}E_n[m],
\qquad m\geqslant1,\quad n\geqslant2m
$$

The number of omitted zeros in these two formulas is determined by $n$, according to the [[Symmetric Polyforms - Types and Normalizations#When zeros may be omitted|convention for omitting zero components]].

### Five vertices: type $[2,1]$

On the set $\{a,b,c,d,e\}$, the equality $E_5[2,1]=3E_5[3,0]$ expands as follows:

$$
\begin{aligned}
&[(ab)(cde)]^2+[(ac)(bde)]^2+\\
&+[(ad)(bce)]^2+[(ae)(bcd)]^2+\\
&+[(bc)(ade)]^2+[(bd)(ace)]^2+\\
&+[(be)(acd)]^2+[(cd)(abe)]^2+\\
&+[(ce)(abd)]^2+[(de)(abc)]^2=\\
&=3\bigl([(abcd)]^2+[(abce)]^2+[(abde)]^2+[(acde)]^2+[(bcde)]^2\bigr)
\end{aligned}
$$

The left-hand side contains ten partitions into a pair and a triple. Each pair uniquely determines its complementary triple; the blocks are distinguished by size, so there is no division by $2$. On the right are five four-vertex boundaries, each with coefficient $3$. The vertex not displayed in a term forms a singleton block.

### Six vertices: type $[1,1,1]$

On the set $\{a,b,c,d,e,f\}$, the equality $E_6[1,1,1]=2E_6[3,0^2]$ takes the form

$$
\begin{aligned}
&[(ab)(cd)(ef)]^2+[(ab)(ce)(df)]^2+[(ab)(cf)(de)]^2+\\
&+[(ac)(bd)(ef)]^2+[(ac)(be)(df)]^2+[(ac)(bf)(de)]^2+\\
&+[(ad)(bc)(ef)]^2+[(ad)(be)(cf)]^2+[(ad)(bf)(ce)]^2+\\
&+[(ae)(bc)(df)]^2+[(ae)(bd)(cf)]^2+[(ae)(bf)(cd)]^2+\\
&+[(af)(bc)(de)]^2+[(af)(bd)(ce)]^2+[(af)(be)(cd)]^2=\\
&=2\bigl([(abcd)]^2+[(abce)]^2+[(abcf)]^2+\\
&\qquad+[(abde)]^2+[(abdf)]^2+[(abef)]^2+\\
&\qquad+[(acde)]^2+[(acdf)]^2+[(acef)]^2+\\
&\qquad+[(adef)]^2+[(bcde)]^2+[(bcdf)]^2+\\
&\qquad+[(bcef)]^2+[(bdef)]^2+[(cdef)]^2\bigr)
\end{aligned}
$$

The left-hand side contains all $15$ partitions into three unordered pairs. To enumerate them, first choose the partner of vertex $a$ in five ways, then partition the remaining four vertices into pairs in three ways. Permuting the three pairs does not create a new term.

The right-hand side contains all $15$ four-vertex boundaries with coefficient $2$; the two remaining vertices form separate singleton blocks. Thus the equality relates expressions with coefficient sums $15$ and $30$.

### Six vertices: type $[2,2]$

On the same vertex set, the equality $E_6[2,2]=3E_6[4,0]$ expands to

$$
\begin{aligned}
&[(abc)(def)]^2+[(abd)(cef)]^2+\\
&+[(abe)(cdf)]^2+[(abf)(cde)]^2+\\
&+[(acd)(bef)]^2+[(ace)(bdf)]^2+\\
&+[(acf)(bde)]^2+[(ade)(bcf)]^2+\\
&+[(adf)(bce)]^2+[(aef)(bcd)]^2=\\
&=3\bigl([(abcde)]^2+[(abcdf)]^2+[(abcef)]^2+[(abdef)]^2+[(acdef)]^2+[(bcdef)]^2\bigr)
\end{aligned}
$$

On the left, each partition into two triples is displayed once: $a$ always belongs to the first block. There are therefore $\binom{5}{2}=10$ terms. Enumerating all $\binom{6}{3}=20$ triples without this restriction would count each partition twice.

On the right are six five-vertex boundaries with coefficient $3$; each term leaves one vertex as a singleton. All three expanded equalities are identities of forms before any metric is chosen.

**Independent computational check.** All partitions of the vertex set were enumerated for each $2\leqslant n\leqslant8$. Each boundary was expanded in the basis of exterior products of vertices, and the product of boundaries and its quadratic form were then expanded directly by bilinearity. The sums were grouped by type and compared with the right-hand side of (1) at every coefficient of the forms $[U_I,U_J]$. Computations used exact integer and rational arithmetic; for $n=8$, all $4140$ partitions were processed. The equalities held for every admissible type in this range. This is a check from the definition, supplementary to the general proof.

## One symmetric polyform in each grade

Let $\mathcal P_{n,k}$ be the [[Basis and Dimension of the Space of Partition Forms#The space whose dimension we compute|space of partition forms of grade $k$]]. The [[Symmetric Polyforms - Types and Normalizations#Symmetrization: sum and average|section on symmetrization]] proves that every element of this space invariant under all vertex permutations can be expressed through the sums $E_n[\lambda]$. Theorem (1) reduces these sums to a single principal polyform.

> [!info] The symmetric part of the space of partition forms
> **Corollary.** For $1\leqslant k\leqslant n-1$,
>
> $$
> (\mathcal P_{n,k})^{S_n}=\mathbb R E_n[k],
> \qquad \dim(\mathcal P_{n,k})^{S_n}=1
> $$
>
> In grade zero, $(\mathcal P_{n,0})^{S_n}=\mathbb R e$. Therefore every symmetric polyform in $\mathcal P_n$ has a unique representation
>
> $$
> \boxed{
> P=c_0e+\sum_{k=1}^{n-1}c_kE_n[k]
> }
> \tag{4}
> $$

> [!note]- Proof
> **Proof.** Expressibility through $E_n[k]$ in each positive grade follows from [[Symmetric Polyforms - Types and Normalizations#Symmetrization: sum and average|averaging over permutations]] and formula (1).
>
> We check that $E_n[k]\ne0$. Choose a real basis $U_I$ of $\Lambda^kW$ and expand each boundary $(B)$ in this basis. The coefficient of $[U_I,U_I]$ in $E_n[k]$ is a sum of squares of the corresponding real coefficients of the boundaries. These coefficients cannot all vanish: the boundary of any $(k+1)$-element subset of independent vertices is nonzero. Hence at least one diagonal coefficient is positive.
>
> The symmetric subspace in each grade therefore has dimension exactly $1$. Different grades form a direct sum, and $e\ne0$, proving uniqueness in (4). $\square$

In particular, $\dim\mathcal P_n^{S_n}=n$. Uniqueness concerns the coefficients $c_k$ in the principal representation (4). An expression through sums of different types may be nonunique; the type still refers to the chosen representation of the polyform.

Every linear metric evaluation preserves identity (1). For a form $[X]^2$, such an evaluation gives the quadratic norm $X^2=X\cdot X$. The coefficient sum of an arbitrary expression does not have this property: for example, the identity $E_4[1,1]=E_4[2,0]$ relates expressions with three and four terms of unit coefficient.

## The number of independent symmetric identities

There are infinitely many ways to write identities: they can be added and multiplied by scalars. Here we count the dimension of the space of linear relations among formal type symbols that become zero when each symbol is replaced by the corresponding sum $E_n[\lambda]$.

Let $p_m(k)$ denote the number of partitions of the integer $k$ into exactly $m$ positive parts, and let $p(n)$ be the number of all partitions of the integer $n$.

> [!info] The number of symmetric relations
> **Corollary.** For $1\leqslant k\leqslant n-1$, the number of independent fully symmetric relations of grade $k$ is
>
> $$
> J_{n,k}=\sum_{m=1}^{\min(k,n-k)}p_m(k)-1
> $$
>
> Summed over all grades,
>
> $$
> \boxed{J_n=p(n)-n}
> $$

> [!note]- Proof
> **Proof.** A positive type of grade $k$ is a partition of the integer $k$ into $m$ positive parts. It is admissible on $n$ vertices when $k+m\leqslant n$, which gives the stated number of types. By the fundamental theorem, their sums span a one-dimensional space, so the number of independent relations is one less than the number of types.
>
> All types on $n$ vertices, including zero components, correspond bijectively to partitions of the integer $n$ into block sizes: add $1$ to each component grade. Thus the total number of types is $p(n)$. Their images span a symmetric space of dimension $n$, with one nonzero polyform in each grade from $0$ to $n-1$. The difference of dimensions gives $J_n=p(n)-n$. $\square$

Applying formula (1) once to each nonprincipal type gives a basis of these relations. Indeed, each relation contains its own nonprincipal type symbol with coefficient $1$, while the remaining term has the principal type of the same grade. The relations are therefore independent and suffice to eliminate all nonprincipal types.

The sequence $J_n$ appears in OEIS as [A000094](https://oeis.org/A000094) [3], with an index shift:

$$
J_n=p(n)-n=\mathrm{A000094}(n+1)
$$

The OEIS entry includes an interpretation in terms of partitions of the integer $n$ with at least two parts greater than $1$. For polyform types, the parts of these integer partitions specify block sizes, so the condition means that there are at least two nontrivial blocks. The $n$ excluded partitions have the form $(s,1^{n-s})$, $1\leqslant s\leqslant n$: $s=1$ gives the unit form, and $s\geqslant2$ gives the principal polyforms. Thus the combinatorial interpretation in OEIS corresponds directly to counting nonprincipal types.

This count must be distinguished from the number of **all** independent structural relations among the forms of individual vertex-set partitions. The [[Basis and Dimension of the Space of Partition Forms#The number of independent identities|structural identities series]] proves

$$
I_n=B_n-C_n
$$

Here $B_n$ is the Bell number and $C_n$ the Catalan number. Symmetric relations form a subspace of all structural relations.

| $n$ | Types $p(n)$ | Symmetric relations $J_n=p(n)-n$ | All structural relations $I_n=B_n-C_n$ |
|---:|---:|---:|---:|
| 4 | 5 | 1 | 1 |
| 5 | 7 | 2 | 10 |
| 6 | 11 | 5 | 71 |
| 7 | 15 | 8 | 448 |
| 8 | 22 | 14 | 2710 |

For example, on five vertices we may choose the following two independent symmetric relations:

$$
E_5[1,1]=2E_5[2],\qquad E_5[2,1]=3E_5[3]
$$

On six vertices, a complete set consists of five relations:

$$
\begin{aligned}
E_6[1,1]&=3E_6[2]\\
E_6[2,1]&=6E_6[3]\\
E_6[1,1,1]&=2E_6[3]\\
E_6[3,1]&=4E_6[4]\\
E_6[2,2]&=3E_6[4]
\end{aligned}
$$

Zero components are omitted here. The numbers of relations in positive grades $1,2,3,4,5$ are $0,1,2,2,0$, respectively.

## Connection with symmetric quadratic polynomials

Lemma 1 has an exact scalar counterpart. If $x_1+\cdots+x_N=0$, then

$$
\sum_{i<j}x_ix_j=-\frac12\sum_i x_i^2
$$

This follows by expanding the square of the sum. Every homogeneous symmetric polynomial of degree $2$ is a linear combination of $\sum_i x_i^2$ and $\sum_{i<j}x_ix_j$: permutations act separately on variable squares and on products of two distinct variables. Under the zero-sum condition, the two expressions are proportional.

The passage to quadratic forms in the proof of Lemma 1 uses the correspondence

$$
x_i^2\longmapsto[X_i]^2,\qquad
2x_ix_j\longmapsto\{X_i,X_j\}
$$

Bilinearity gives the same coefficients, and the condition $\sum_iX_i=0$ eliminates the sum of polar forms. In block merging, suitable arguments $X_i$ arise from $\partial^2=0$.

This correspondence concerns quadratic expressions. Polynomial degree $2$ is distinct from the exterior grade of the arguments $X_i$, which may be arbitrary in the lemma. The name of the fundamental theorem emphasizes that all symmetric sums can be expressed through distinguished principal polyforms; the proof itself and the precise correspondence with the literature are given separately from this analogy.

## Correspondence with classical representation theory

The one-dimensionality of the symmetric subspace has a classical explanation. The complexification of $W=\ker\varepsilon$ is the standard $(n-1)$-dimensional representation of $S_n$. For $0\leqslant k\leqslant n-1$, its exterior power $\Lambda^kW_{\mathbb C}$ is the irreducible representation corresponding to the partition $(n-k,1^k)$, a hook diagram. This classical fact is stated in the introduction to Ivan Marin's paper [1]. Together with Schur's lemma in the form of Corollary 1.17 in the book by Etingof and coauthors [2], it yields the following result.

**Proposition.** In the full space of forms $[X,Y]$ on $\Lambda^kW$, the subspace invariant under vertex permutations is one-dimensional. It is spanned by $E_n[k]$ for $k\geqslant1$, and by $e$ for $k=0$.

> [!note]- Proof and an independent derivation of the coefficient
> **Proof.** Set $U=\Lambda^kW$. By the definition of forms, their full space is identified with $U\otimes U$: the symbol $[X,Y]$ corresponds to $X\otimes Y$.
>
> Introduce an auxiliary Euclidean inner product on $V$ in which the basis vertices are orthonormal. It is preserved by permutations and induces an inner product on $U$. Using it, identify the form $[X,Y]$ with the operator sending $Z$ to $X$ multiplied by the auxiliary inner product of $Y$ and $Z$. This is a linear isomorphism between the space of forms and $\operatorname{End}(U)$, compatible with the action of $S_n$.
>
> Invariant forms correspond to operators commuting with every permutation. After complexification, the representation $U_{\mathbb C}$ is irreducible. By Schur's lemma, these operators are scalar. A real operator whose complexification is scalar has a real scalar, so the real invariant subspace is also one-dimensional.
>
> The polyform $E_n[k]$ is invariant and nonzero, as proved above. It spans this subspace for $k\geqslant1$; the case $k=0$ gives $e$.
>
> We now derive the coefficient in (1) without merging blocks. The trace of the operator corresponding to $[X]^2$ is the auxiliary quadratic norm of $X$. For a block of size $k_i+1$, its boundary contains $k_i+1$ orthonormal exterior basis terms with coefficients $\pm1$. Its auxiliary quadratic norm is therefore $k_i+1$.
>
> Distinct blocks lie in orthogonal coordinate subspaces. The quadratic norm of the product of their boundaries equals the product of their quadratic norms; this also follows by direct expansion in the orthonormal exterior basis. Thus
>
> $$
> \operatorname{tr}q_\pi=\prod_{i=1}^m(k_i+1)
> $$
>
> Multiplying by the [[Symmetric Polyforms - Types and Normalizations#Representation size and factorial factors|representation size of the symmetric sum]], we obtain
>
> $$
> \operatorname{tr}E_n[k_1,\ldots,k_m,0^\ell]
> =
> \frac{n!}{\ell!\displaystyle\prod_i k_i!\displaystyle\prod_j\mu_j!}
> $$
>
> For the principal polyform,
>
> $$
> \operatorname{tr}E_n[k]
> =\binom{n}{k+1}(k+1)
> =\frac{n!}{k!(n-k-1)!}
> $$
>
> Proportionality of these polyforms has already been established through the one-dimensionality of the invariant subspace. The ratio of their traces therefore determines the coefficient of proportionality and gives exactly (1). $\square$

The auxiliary inner product is used here to identify forms with operators and to compute traces. It does not define the resistance metric of a graph. Equal traces alone would not suffice to establish equality of arbitrary forms; the proof first establishes their proportionality.

This argument also extends Corollary (4): it holds for every symmetric polyform **on boundaries**, even if membership in the space of partition forms is not assumed initially. The condition “on boundaries” is essential: the full space of forms on $V$ is a different representation of the group.

The name “fundamental theorem of symmetric polyforms” is used here for this result within PMG. The verified correspondence with the literature consists of the irreducibility of exterior powers of the standard representation and Schur's lemma. Sources [1, 2] provide these general results; their application to PMG forms and the explicit coefficient (1) are derived in this note. No separate, generally accepted name for formula (1) itself has been established from the sources checked.

## Status of the result and further work

Formula (1) is proved for all admissible types on any finite set of independent basis vertices over $\mathbb R$. The main proof uses only bilinearity of forms, properties of the boundary operator, and partition counts. The independent derivation through representation theory relies on the precisely cited external results.

The theorem explains linear dependencies among symmetric sums of different types. The multiplication rules for principal polyforms and their consequences are discussed in [[Products and Powers of Symmetric Polyforms]].

## References

1. Ivan Marin. *Hooks Generate the Representation Ring of the Symmetric Group*. [arXiv:1112.3127v1](https://arxiv.org/abs/1112.3127v1), 2011. §1, p. 1: the standard representation of $S_n$ and its exterior powers corresponding to hook diagrams.
2. Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob, Elena Yudovina. *Introduction to Representation Theory*. [arXiv:0901.0827v5](https://arxiv.org/abs/0901.0827v5), 2011. §1.3, Proposition 1.16 and Corollary 1.17: Schur's lemma and scalar endomorphisms of an irreducible representation over an algebraically closed field.
3. *The On-Line Encyclopedia of Integer Sequences*. [A000094: Number of trees of diameter 4](https://oeis.org/A000094). FORMULA and COMMENTS sections: the formula $a(n+1)=p(n)-n$ for $n>0$ and the interpretation via partitions with at least two parts of size at least $2$.
