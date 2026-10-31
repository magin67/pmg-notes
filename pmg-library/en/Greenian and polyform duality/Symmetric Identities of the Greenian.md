---
title: Symmetric Identities of the Greenian
date: 2026-10-28
updated: 2026-10-28
revision: 2
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: greenian-symmetric-identities
lang: en
description: "Boundary identities and their cut images: centering, the zero sum of dual elements, complementary grades, and evaluations compatible with structural identities."
order: 8
---

[[ru/Гриниан и дуальность полиформ/Симметрические тождества гриниана|Русский]]

The vector representation of the Greenian obeys the same structural identities as the Laplacian. In the cut representation, these relations are written through sums of dual or centered elements. The zero-sum condition concerns the choice of these elements and does not by itself characterize the Greenian coefficients.

Here “symmetric identities” means identities between full sums over partitions of specified types. An arbitrary Greenian need not be invariant under all vertex permutations; the identities of its arguments hold independently of such invariance.

## Independent vertices and centered elements

Let $a_1,\ldots,a_n$, with $n\ge2$, be independent vertices of the direct space. Write

$$
a_{ij}=a_j-a_i=(a_i a_j),\qquad
h=\frac1n\sum_i a_i,\qquad p_i=a_i-h
$$

Then

$$
\sum_i p_i=0,\qquad p_j-p_i=a_{ij}
$$

Any independently specified vector form is preserved by centering:

$$
S=\sum_{i<j}s_{ij}[a_{ij}]^2
=\sum_{i<j}s_{ij}[p_j-p_i]^2
\tag{1}
$$

The coefficients $s_{ij}$ may be arbitrary real numbers. No previously specified Laplacian is required for (1). In particular, the equality applies to $L$ and to $\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2$, where $\gamma_{ij}=-\mathrm{Gr}_{ij}$.

The zero sum of the $p_i$ does not imply a zero sum of the independent vertices $a_i$. Centering may change an arbitrary form on vertices: no equality $[a_i]^2=[p_i]^2$ is asserted. Preservation in (1) follows because the arguments are differences.

In the dual space $W^*=V^*/\mathbb R\varepsilon$, where $\varepsilon(a_i)=1$ and $W=\ker\varepsilon$, the classes of coordinate functionals also sum to zero. To distinguish the spaces in this note, denote them by $a_i^\vee$. The [[The Exterior Exponential and Representations of the Greenian#The centered image and the Greenian|centered identification]] is

$$
\sum_i a_i^\vee=0,\qquad
\mathcal C:W^*\longrightarrow W,\qquad
\mathcal C(a_i^\vee)=p_i
$$

Thus the zero sum on the dual side follows from the definition of the space, and the zero sum for $p_i$ from subtracting the centroid. Zero row sums of a coefficient matrix must be distinguished from both statements about representing elements.

## Preservation of boundary identities

> [!info] Preservation of boundary identities
> **Proposition.** Centering preserves every boundary and every product of boundaries. Thus all structural identities of boundary forms remain valid in the vector representation of the Greenian.

> [!note]- Proof
> **Proof.** A boundary on $k+1$ vertices is expressed through differences with a common initial vertex:
>
> $$
> (a_{i_0}\ldots a_{i_k})
> =(a_{i_1}-a_{i_0})\cdots(a_{i_k}-a_{i_0})
> $$
>
> Every factor is preserved when $a_i$ is replaced by $p_i$. Hence boundaries, their exterior products, and forms on these arguments are preserved. Moreover, centering is the identity on $W$, so it creates no additional linear relations among these forms. $\square$

In particular, the tetrahedron identity holds for four vertices:

$$
\begin{aligned}
&[a_{ab}a_{cd}]^2+[a_{ac}a_{bd}]^2+[a_{ad}a_{bc}]^2\\
&\qquad=[(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2
\end{aligned}
\tag{2}
$$

Here $a_{ab}=b-a$, and similarly for other pairs. Relation (2) is independent of graph or Greenian coefficients.

The entire [[Fundamental Theorem of Symmetric Polyforms|fundamental theorem of symmetric polyforms]], including its coefficients for arbitrary types, transfers in the same way. The condition $\partial^2=0$ is used in its original proof on independent vertices. One cannot redefine an operator with $\partial p_i=1$ on centered elements: that would contradict $\sum_i p_i=0$. For these elements, boundaries are defined by the displayed formula through differences.

## Symmetric sums of cuts

For a subset of indices $A$, set

$$
s_A=\sum_{i\in A}p_i,\qquad
s_{A^c}=-s_A
$$

Thus the quadratic form $[s_A]^2$ depends on the unordered cut $A\mid A^c$.

> [!info] Symmetric sums of cuts
> **Lemma.** For $1\le r\le n-1$,
>
> $$
> \boxed{
> \sum_{\substack{A\subseteq\{1,\ldots,n\}\\\#A=r}}[s_A]^2
> =\binom{n-2}{r-1}\sum_{i=1}^n[p_i]^2
> }
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** For $r=1$, the formula is immediate. For $r\ge2$, expanding the left-hand side gives
>
> $$
> \binom{n-1}{r-1}\sum_i[p_i]^2
> +\binom{n-2}{r-2}\sum_{i<j}\{p_i,p_j\}
> $$
>
> From $[\sum_i p_i]^2=0$, we obtain $\sum_{i<j}\{p_i,p_j\}=-\sum_i[p_i]^2$. The difference of the two binomial coefficients is $\binom{n-2}{r-1}$. $\square$

This applies the [[Fundamental Theorem of Symmetric Polyforms#A quadratic identity under a zero-sum condition|zero-sum lemma]]. In the proof of boundary identities, its arguments arise from $\partial^2=0$; here they are the centered elements themselves.

For $n=4$ and $r=2$, each unordered cut is counted twice. Dividing by two gives

$$
\boxed{
[p_a+p_b]^2+[p_a+p_c]^2+[p_a+p_d]^2
=[p_a]^2+[p_b]^2+[p_c]^2+[p_d]^2
}
\tag{4}
$$

In coordinates with zero centroid, $p_a,p_b,p_c,p_d$ may simply be denoted by $a,b,c,d$. Then (4) is written through vertex sums, but these letters no longer denote an independent basis of the direct space.

## Complementary grades and the dual image of an identity

Let $\pi=B_1\mid\cdots\mid B_m$ be a partition of all $n$ vertices. It determines a direct boundary form and a dual partition form:

$$
q_\pi=[(B_1)\cdots(B_m)]^2,\qquad
\Phi_\pi=[a_{B_1}^\vee\cdots a_{B_{m-1}}^\vee]^2,\qquad
a_B^\vee=\sum_{i\in B}a_i^\vee
$$

The omitted block in $\Phi_\pi$ is immaterial because all block elements sum to zero. The grades of $q_\pi$ and $\Phi_\pi$ are $n-m$ and $m-1$, respectively; their sum is $n-1$.

For $T=[(a_1\ldots a_n)]^2$, the following [[Cuts and Forest Grades of the Greenian Exponential#The deletion identity for a single partition|deletion identity]] has been proved:

$$
T/\Phi_\pi=q_\pi
$$

> [!info] Complementary grades and the dual image of an identity
> **Corollary.** For partitions with a fixed number of blocks and arbitrary coefficients $b_\pi$,
>
> $$
> \sum_\pi b_\pi q_\pi=0
> \quad\Longleftrightarrow\quad
> \sum_\pi b_\pi\Phi_\pi=0
> \tag{5}
> $$

> [!note]- Proof
> **Proof.** Deletion from a nonzero top form is a linear isomorphism between forms of complementary grades: in matched exterior bases, it replaces each index set by its complement, with a nonzero common factor and signs. Applying this isomorphism to the sum on the right gives the sum on the left. $\square$

Thus all symmetric boundary identities have dual counterparts with the same coefficients. In this transfer, types index the original partitions; they cannot automatically be regarded as component types of the dual form itself.

For four vertices, the correspondence is:

| Partition | Direct form $q_\pi$ | Centered image $\mathcal C(\Phi_\pi)$ |
|---|---|---|
| $ab\mid cd$ | $[a_{ab}a_{cd}]^2$ | $[p_a+p_b]^2$ |
| $a\mid bcd$ | $[(bcd)]^2$ | $[p_a]^2$ |

The other partitions follow by permuting vertices. Under (5), the tetrahedron identity (2) becomes the cut identity (4). Grade $2$ is replaced by grade $1$, while the coefficients remain one. No particular Greenian needs to be constructed for this transfer.

## Which evaluations preserve the identities

Simply replacing each term by one maps the two sides of (2), and likewise of (4), to $3$ and $4$. This evaluation is incompatible with the identity.

For a direct partition form, the rooted weight is the product of block sizes. The same weight may be retained for a dual form indexed by the same partition. In the four-vertex example, this gives

$$
3\cdot(2\cdot2)=4\cdot(1\cdot3)=12
$$

Thus a cut $A\mid A^c$ receives weight $\#A\,\#A^c$. This must be distinguished from the cut conductance and from the [[The Greenian Metric and Potentials#The potential of a cut form|potential of the cut form in a specific metric]].

The general [[Fundamental Theorem of Symmetric Polyforms#Substituting numbers for components while preserving identities|condition on component weights]] applies to the canonical boundary representation: if a weight depends only on component grade, multiplies over components, and must preserve every symmetric identity for all $n$, then

$$
\boxed{x_j=(j+1)t^j,\qquad j\ge1}
\tag{6}
$$

The parameter $t$ marks the grade. For a single fixed $n$, the condition is weaker; in particular, symmetric identities do not constrain the weight of the sole top type. On the cut side, transferred rooted weights use the block sizes of the original partition, not a “dual grade plus one” rule.

**Remark.** Multiplying the coefficients of a full toponome by rooted weights does not make different types equal. For (2), the original toponomes are $3x_1^2$ and $4x_2$. Vertex normalization turns them into $12x_1^2$ and $12x_2$, which remain distinct. It is specialization (6), applied to the original toponomes, that maps both sides to $12t^2$. The distinction between normalization and subsequent evaluation is discussed in [[Toponomes and Structural Identities]].

Thus the distinction between forest coefficients and their rooted evaluations persists for the Greenian exponential. One original toponome can underlie both specializations; the zero-sum condition does not turn them into the same operation. The construction and examples are given in [[Toponomes of the Greenian Exponential and Dual Pairs]], which also proves the connection of the rooted evaluation with the determinant and the reciprocal nonzero Laplacian spectrum.

## Status and connections

The zero-sum and tetrahedron identities were additionally checked coefficient by coefficient in exact rational arithmetic: 154 tensor equalities on systems of 2–8 elements. Run the [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/dual/verify_symmetry.py) from the repository root:

    python checks/dual/verify_symmetry.py

This finite check supplements the proofs above.

All displayed identities are algebraic and proved over $\mathbb R$ for independent original vertices and the specified centered and dual spaces. They require neither positive coefficients, nondegeneracy of the vector form, nor a previously specified graph. Transferring a structural identity neither establishes a correspondence between individual forests of the two exponentials nor determines their coefficients.

The main results on symmetric sums and admissible evaluations appear in [[Fundamental Theorem of Symmetric Polyforms]]. The deletion action and its standard exterior-algebraic foundations are presented in [[Laplacian and Greenian - Mutual Duality of Exponentials]], and its application to partitions in [[Cuts and Forest Grades of the Greenian Exponential]].

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
