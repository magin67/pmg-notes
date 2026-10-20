---
title: "Products and Powers of Symmetric Polyforms"
date: 2026-10-19
updated: 2026-10-20
revision: 4
source_revision: 5
status: draft
text_prepared_by: ChatGPT
translation_key: products-and-powers-of-symmetric-polyforms
lang: en
description: "The product rule for principal symmetric polyforms, powers, nilpotency, a single generator, and factorial normalizations."
order: 3
---

The fundamental theorem of symmetric polyforms (SPFs) expresses sums of different types through principal symmetric polyforms (principal SPFs) of the same grade. To compute products of SPFs, it therefore suffices to establish a multiplication rule for principal SPFs. The rule is particularly simple: the product is proportional to the principal polyform of the total grade, provided that this grade does not exceed $n-1$.

We derive the rule by counting block intersections and applying the [[Fundamental Theorem of Symmetric Polyforms|fundamental theorem]]. It then yields formulas for powers and an expression for all SPFs on boundaries in terms of a single generator $E_n[1]$.

## Definitions and the product

Fix a set $A=\{a_1,\ldots,a_n\}$ of independent basis vertices, with $n\geqslant2$. All polyforms below are defined on the same set $A$. The space of affine vectors $W=\ker\varepsilon$ has dimension $n-1$.

We use the normalization from [[Symmetric Polyforms - Types and Normalizations|Symmetric Polyforms: Types and Normalizations]]: in the sum $E_n[\lambda]$, each partition into unordered blocks is counted once with coefficient $1$. A principal SPF of positive grade has the form

$$
E_n[k]=\sum_{\substack{B\subseteq A\\\#B=k+1}}[(B)]^2,
\qquad 1\leqslant k\leqslant n-1
$$

The remaining vertices in each term form singleton blocks. At grade zero, we retain the separate convention $E_n[0^n]=e$.

Recall the [[Basic Objects and Operations of Polyform Algebra#Polyforms and the product of forms|product of forms]]:

$$
[X,Y][U,V]=[XU,YV],\qquad
[X]^2[U]^2=[XU]^2
$$

The exterior product is implicit in the arguments. Multiplication of forms extends bilinearly to polyforms, is commutative, and has the unit $e=[1,1]$. A power $P^h$ of a polyform means repeated application of this product; in particular, $P^0=e$. The notation $[X]^2$ for a quadratic form retains its separate meaning.

The product of symmetric polyforms is symmetric: for any permutation of the vertices $\sigma$, we have $\sigma(PQ)=(\sigma P)(\sigma Q)=PQ$. Thus addition and multiplication preserve the class under consideration.

## Three cases of block intersection

Let $1\leqslant p,q\leqslant n-1$. Expanding $E_n[p]E_n[q]$ amounts to choosing two blocks $B,C\subseteq A$ of sizes $p+1$ and $q+1$. The corresponding term is

$$
[(B)]^2[(C)]^2=[(B)(C)]^2
$$

Its form is determined by the [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|rules for products of simplex boundaries]].

| Block intersection | Result |
|---|---|
| $B\cap C=\varnothing$ | A form with two nontrivial blocks $[(B)(C)]^2$ |
| $B\cap C=\{s\}$ | The form of a single boundary $[(B\cup C)]^2$ |
| $\#(B\cap C)\geqslant2$ | The zero form |

When there is one common vertex, the boundaries can be written as products of differences relative to that vertex. Their product gives the boundary of the union up to a sign, which disappears in the quadratic form. When two vertices are shared, the same difference of these vertices occurs in both products, so the exterior product vanishes.

For example,

$$
[(ab)]^2[(cd)]^2=[(ab)(cd)]^2,\qquad
[(ab)]^2[(bc)]^2=[(abc)]^2,\qquad
[(abc)]^2[(bcd)]^2=0
$$

These rules apply to individual terms. After summing over blocks, the contribution of disjoint blocks can also be expressed through the principal polyform by the fundamental theorem.

## The product of two principal polyforms

> [!info] The product rule
> **Theorem.** Let $1\leqslant p,q\leqslant n-1$. If $p+q\leqslant n-1$, then
>
> $$
> \boxed{
> E_n[p]E_n[q]
> =n\binom{p+q}{p}E_n[p+q]
> }
> \tag{1}
> $$
>
> If $p+q\geqslant n$, then $E_n[p]E_n[q]=0$.

> [!note]- Proof
> **Proof.** Write $k=p+q$ and first assume that $k\leqslant n-1$. Expand the product over pairs of blocks $B,C$.
>
> **One common vertex.** Fix a union $D=B\cup C$ consisting of $k+1$ vertices. The common vertex can be chosen in $k+1$ ways. Then choose $p$ of the remaining $k$ vertices for $B$; the remaining $q$ belong to $C$. This gives
>
> $$
> (k+1)\binom{k}{p}
> $$
>
> pairs of blocks with the given union. Each pair contributes the form $[(D)]^2$. The total contribution of this case is
>
> $$
> (k+1)\binom{k}{p}E_n[k]
> $$
>
> Even when $p=q$, this coefficient should not be divided by $2$: in the product expansion, a choice from the first factor is distinguished from a choice from the second. Both orders occur in the sum.
>
> **Disjoint blocks.** This case is possible only when $k+2\leqslant n$. If $p\ne q$, the two sizes distinguish the blocks, and the contribution is $E_n[p,q]$. If $p=q$, each partition occurs in both orders, so the contribution is $2E_n[p,p]$.
>
> By the fundamental theorem, taking the $n-k-2$ singleton blocks into account,
>
> $$
> E_n[p,q]=(n-k-1)\binom{k}{p}E_n[k],
> \qquad p\ne q
> $$
>
> $$
> 2E_n[p,p]=(n-2p-1)\binom{2p}{p}E_n[2p]
> $$
>
> The second formula accounts for the divisor $2!$ for equal components in the basic normalization. Thus, in both cases the contribution of disjoint blocks is
>
> $$
> (n-k-1)\binom{k}{p}E_n[k]
> $$
>
> When $k=n-1$, no disjoint blocks are possible. Their contribution is zero; no sum of the inadmissible type $[p,q]$ is introduced in this case.
>
> **At least two common vertices.** All such terms are zero. Adding the two nonzero contributions gives
>
> $$
> E_n[p]E_n[q]
> =\bigl((k+1)+(n-k-1)\bigr)\binom{k}{p}E_n[k]
> =n\binom{k}{p}E_n[k]
> $$
>
> When $k=n-1$, the contribution from one common vertex alone gives the same result: $k+1=n$.
>
> Finally, if $p+q\geqslant n$, then for any admissible blocks
>
> $$
> \#(B\cap C)\geqslant \#B+\#C-n=p+q+2-n\geqslant2
> $$
>
> Every term in the product is therefore zero. This also follows from $\Lambda^{p+q}W=0$ when $p+q\geqslant n$. $\square$

The factor $n$ in (1) combines two different counts: $k+1$ possible common vertices within the union block, and the coefficient $n-k-1$ obtained after transforming the sum over disjoint blocks. The ratio of representation sizes alone does not provide such a proof.

## Several factors and powers

Repeated application of (1) gives a formula for any number of principal factors. For a positive grade collection $\boldsymbol k=[k_1,\ldots,k_r]$ of weight $K$, use the [[Partitions and the Combinatorial Potential of the Second Kind#From repeated counts to the general formula|multinomial coefficient]]

$$
P(\boldsymbol k)=\frac{K!}{[k_i!]!}
=s_2(\boldsymbol k)[\mu_j!]!
$$

Here $[k_i!]!$ is the product of the grade factorials and $[\mu_j!]!$ the product of the factorials of their positive multiplicities. In this section, $r$ is the number of factors; below, the exponent $h$ counts repetitions of one factor.

> [!info] A product of principal polyforms
> **Corollary.** Let $r\geqslant1$, $1\leqslant k_i\leqslant n-1$, and $K=k_1+\cdots+k_r$. For $K\leqslant n-1$,
>
> $$
> \boxed{
> \prod_{i=1}^r E_n[k_i]
> =n^{r-1}P(\boldsymbol k)E_n[K]
> }
> \tag{2}
> $$
>
> For $K\geqslant n$, the product is zero.

> [!note]- Proof
> **Proof.** For $r=1$, the statement holds directly. By (1), each subsequent factor contributes an additional coefficient $n$ and a binomial coefficient. Collect these binomial coefficients in
>
> $$
> \mathbf b=\left[\binom{k_1+\cdots+k_j}{k_j}\right]_{j=2}^{r}
> $$
>
> Its product is
>
> $$
> \mathbf b!=\frac{K!}{[k_i!]!}=P(\boldsymbol k)
> $$
>
> because the factorials of the intermediate sums cancel. There are $r-1$ multiplications in total, which gives (2). If $K\geqslant n$, the grade of the product exceeds the dimension of $W$, so the product is zero. $\square$

The coefficient $P(\boldsymbol k)$ counts distributions of $K$ distinct elements into **distinguishable** groups of prescribed sizes. There is therefore no additional division by factorials of the multiplicities of equal $k_i$: the factors specify separate positions for the choices.

In particular,

$$
E_n[k]E_n[1]=n(k+1)E_n[k+1],
\qquad 1\leqslant k\leqslant n-2
$$

For $1\leqslant k\leqslant n-1$, taking equal factors gives

$$
\boxed{
\bigl(E_n[k]\bigr)^h
=n^{h-1}\frac{(kh)!}{(k!)^h}E_n[kh]
},
\qquad h\geqslant1,\quad kh\leqslant n-1
\tag{3}
$$

For $kh\geqslant n$, this power is zero. Formula (3) follows from (2) with $r=h$ and $k_1=\cdots=k_h=k$. It includes, for example, the square

$$
\bigl(E_n[k]\bigr)^2
=n\binom{2k}{k}E_n[2k],
\qquad 2k\leqslant n-1
$$

The case of the first grade is especially useful:

$$
\boxed{
\bigl(E_n[1]\bigr)^k=n^{k-1}k!\,E_n[k]
},
\qquad 1\leqslant k\leqslant n-1
\tag{4}
$$

The polyforms $E_n[k]$ are nonzero, as proved in the [[Fundamental Theorem of Symmetric Polyforms#One symmetric polyform in each grade|section on the symmetric subspace]]. Thus all powers in the range (4) are nonzero, but

$$
\bigl(E_n[1]\bigr)^n=0
$$

The polyform $E_n[1]$ is therefore nilpotent of index $n$: the smallest positive power at which it vanishes is exactly $n$.

## A single generator

By the [[Fundamental Theorem of Symmetric Polyforms#Correspondence with classical representation theory|fundamental theorem and its extension to all forms on boundaries]], every symmetric polyform has a unique representation

$$
P=c_0e+\sum_{k=1}^{n-1}c_kE_n[k]
$$

Substituting (4), we obtain

$$
P=c_0e+\sum_{k=1}^{n-1}
\frac{c_k}{n^{k-1}k!}\bigl(E_n[1]\bigr)^k
$$

Thus a symmetric polyform can be specified by a polynomial in $E_n[1]$ of degree at most $n-1$.

> [!info] The algebra of symmetric polyforms
> **Corollary.** The algebra of symmetric polyforms on boundaries on a fixed set of $n$ vertices is isomorphic to
>
> $$
> \mathbb R[t]/(t^n)
> $$
>
> under the correspondence $t\mapsto E_n[1]$ and $1\mapsto e$. This is the algebra of polynomials with the rule $t^n=0$.

> [!note]- Proof
> **Proof.** Substitution $t\mapsto E_n[1]$ preserves addition and multiplication and, by (4), yields all symmetric polyforms. Since $(E_n[1])^n=0$, polynomials that differ by a multiple of $t^n$ define the same polyform.
>
> Conversely, the elements $e,E_n[1],(E_n[1])^2,\ldots,(E_n[1])^{n-1}$ are linearly independent: they are nonzero and have distinct grades. A polynomial of degree less than $n$ can therefore give the zero polyform only if all its coefficients are zero. This proves the claim. $\square$

In practice, this means that the product of two symmetric polyforms can be computed by ordinary multiplication of their polynomial expressions, discarding powers $t^n$ and higher. The reduction to a single generator relies specifically on symmetry under all permutations of the vertices.

For sums of arbitrary types, we can first apply the fundamental theorem to each factor and then use (1) or (2). For example, on six vertices,

$$
E_6[1,1]E_6[2]
=3\bigl(E_6[2]\bigr)^2
=108E_6[4]
$$

Here $E_6[1,1]=3E_6[2]$ follows from the fundamental theorem, and the square of the principal polyform is computed using (3).

## Factorial normalizations and grade zero

The binomial coefficient in (1) arises from factorials of the grades. If we use the factorial normalization $k!E_n[k]$ at positive grades, the rule becomes

$$
\bigl(p!E_n[p]\bigr)\bigl(q!E_n[q]\bigr)
=n(p+q)!E_n[p+q]
$$

Dividing each of these polyforms by $n$ also removes the factor $n$:

$$
\left(\frac{p!}{n}E_n[p]\right)
\left(\frac{q!}{n}E_n[q]\right)
=\frac{(p+q)!}{n}E_n[p+q]
$$

Both formulas apply when $p,q\geqslant1$ and $p+q\leqslant n-1$. They are obtained by multiplying (1) by the corresponding scalar coefficients.

By (4),

$$
\frac{k!}{n}E_n[k]
=\left(\frac{E_n[1]}{n}\right)^k,
\qquad 1\leqslant k\leqslant n-1
$$

Thus the sequence

$$
e,\quad
\frac{E_n[1]}{n},\quad
\frac{2!E_n[2]}{n},\quad
\ldots,\quad
\frac{(n-1)!E_n[n-1]}{n}
$$

is the sequence of powers of $E_n[1]/n$, starting with the zeroth power. These normalizations do not require changing the basic notation $E_n[k]$.

**A remark on grade zero.** Formulas (1)-(4) are stated for factors of positive grade. They cannot be used to redefine grade zero. The unit remains

$$
E_n[0^n]=e,\qquad eP=P,\qquad P^0=e
$$

In particular, the zeroth power of $E_n[1]/n$ is $e$, not $e/n$. The formal sum over all singleton subsets gives $ne$; its distinction from the unique partition into singleton blocks is discussed in the [[Symmetric Polyforms - Types and Normalizations#Grade zero|section on grade zero]]. The polyform $ne$ is not a multiplicative unit when $n\geqslant2$.

## Examples on four, five, and six vertices

### Four vertices: squaring the first grade

On the set $\{a,b,c,d\}$,

$$
E_4[1]
=[(ab)]^2+[(ac)]^2+[(ad)]^2+[(bc)]^2+[(bd)]^2+[(cd)]^2
$$

This is the [[Laplacian - graph, electrical network and quadratic form|Laplacian polyform]] $L=E_4[1]$ of the complete graph $K_4$ with unit conductances: all six of its edges occur in the sum.

Squaring produces $36$ ordered pairs of terms. The six products of an edge form with itself are zero. Of the remaining $30$ pairs:

- $24$ have one common vertex; each of the four triples occurs $6$ times;
- $6$ consist of disjoint pairs; each of the three partitions of type $[1,1]$ occurs twice.

Therefore,

$$
\bigl(E_4[1]\bigr)^2
=6E_4[2]+2E_4[1,1]
=8E_4[2]
$$

The last step uses the [[Partition Forms and the Tetrahedron Identity#The tetrahedron identity|tetrahedron identity]]. Written in terms of vertices, the result is

$$
\begin{aligned}
&\bigl([(ab)]^2+[(ac)]^2+[(ad)]^2+[(bc)]^2+[(bd)]^2+[(cd)]^2\bigr)^2=\\
&=8\bigl([(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2\bigr)
\end{aligned}
$$

In the product $E_4[1]E_4[2]$, disjoint blocks are no longer possible. For each of the four triples, three pairs connect a vertex of that triple to the remaining vertex. All $12$ products give the same top-grade form:

$$
E_4[1]E_4[2]=12[(abcd)]^2
$$

Hence

$$
\bigl(E_4[1]\bigr)^3=96[(abcd)]^2,\qquad
\bigl(E_4[1]\bigr)^4=0
$$

The [[Laplacian Exponential|polyform exponential]] of the Laplacian of $K_4$ is therefore

$$
M_{K_4}=\exp L
=e+L+\frac{L^2}{2!}+\frac{L^3}{3!}
=e+E_4[1]+4E_4[2]+16E_4[3]
$$

Here $E_4[3]=[(abcd)]^2$. The sum is finite because $L^4=0$, and the coefficients $4$ and $16$ are obtained by dividing the coefficients of the powers by $2!$ and $3!$. All powers and the exponential are computed in the algebra of polyforms. This is distinct from the matrix exponential of the Laplacian.

### Five vertices: different grades

In the product $E_5[1]E_5[2]$, a pair and a triple can be disjoint or share one or two vertices. Two common vertices give a zero contribution. For each union of four vertices, there are $4\binom{3}{1}=12$ choices with one common vertex. Disjoint blocks contribute $E_5[2,1]$ without an additional multiplicity. Therefore,

$$
E_5[1]E_5[2]
=12E_5[3]+E_5[2,1]
=15E_5[3]
$$

Here we used $E_5[2,1]=3E_5[3]$, expanded in the [[Fundamental Theorem of Symmetric Polyforms#Five vertices: type $[2,1]$|example on five vertices]]. The result is

$$
\begin{aligned}
E_5[1]E_5[2]
&=15\bigl([(abcd)]^2+[(abce)]^2+[(abde)]^2+\\
&\qquad+[(acde)]^2+[(bcde)]^2\bigr)
\end{aligned}
$$

We also have $E_5[1]E_5[3]=20E_5[4]$, whereas $E_5[2]E_5[3]=0$: in the latter case, the total grade exceeds $4$.

### Six vertices: equal grades

The square of $E_6[2]$ multiplies forms of triples. For each union of five vertices, there are $5\binom{4}{2}=30$ ordered pairs of triples with one common vertex. Each partition into two disjoint triples occurs twice. Hence

$$
\bigl(E_6[2]\bigr)^2
=30E_6[4]+2E_6[2,2]
=36E_6[4]
$$

The last step uses $E_6[2,2]=3E_6[4]$ from the [[Fundamental Theorem of Symmetric Polyforms#Six vertices: type $[2,2]$|example with two triples]]. The expanded result is

$$
\begin{aligned}
\bigl(E_6[2]\bigr)^2
&=36\bigl([(abcde)]^2+[(abcdf)]^2+[(abcef)]^2+\\
&\qquad+[(abdef)]^2+[(acdef)]^2+[(bcdef)]^2\bigr)
\end{aligned}
$$

The square is nonzero, but $\bigl(E_6[2]\bigr)^3=0$, since grade $6$ exceeds the dimension of the affine vector space, which is $5$.

**Independent computational check.** For every $2\leqslant n\leqslant8$ and all $1\leqslant p,q\leqslant n-1$, the product was computed directly from the definition: pairs of subsets were enumerated, their boundaries were expanded in the exterior basis of vertices, and the quadratic form of the product was then expanded. All coefficients were compared with (1), including the vanishing cases. This checked $140$ ordered pairs of grades. Separately, repeated multiplication of the coefficient expressions for forms verified the powers of every $E_n[k]$ up to and including the first zero power. The computations used exact integer arithmetic and confirmed every equality in the stated range. This check supplements the general proof.

## Metric evaluation and further applications

All the equalities obtained are identities of forms before a metric is chosen. Linear metric evaluation preserves them, but the product of forms must be evaluated as a whole.

For example, $q=[(ab)]^2$ satisfies $q^2=0$, although its evaluation $(ab)\cdot(ab)$ in a positive definite metric is positive. Thus the evaluation of a product is generally not the product of the evaluations of its factors. The quadratic norm of an exterior object is still denoted by $X^2=X\cdot X$; it differs from the product of polyforms.

The principal polyform $E_n[1]$ is the [[Laplacian - graph, electrical network and quadratic form|Laplacian polyform]] of the complete graph with unit conductances. Formula (4) therefore directly determines all positive grades of its [[Laplacian Exponential|polyform exponential]]. Applications to the complete graph, Cayley's formula, and expansions by forest type are discussed in [[Symmetric Polyforms of the Complete Graph]].

This note is based on the author's research within PMG. The product and power rules are proved for all stated grades and all $n\geqslant2$; the use of the fundamental theorem and the grade restriction are indicated explicitly.
