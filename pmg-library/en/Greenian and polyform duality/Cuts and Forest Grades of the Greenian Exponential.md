---
title: Cuts and Forest Grades of the Greenian Exponential
date: 2026-10-28
updated: 2026-10-28
revision: 1
translated_revision: 9
status: draft
text_prepared_by: ChatGPT
translation_key: dual-polyform-cuts-forest-grades
lang: en
order: 3
description: "Cut representations of the Greenian and its exponential through original graph forests: partition forms, exterior deletion, positive forest weights, and comparison with signed forests."
---

The vector representation of the Greenian expands its exponential over signed forests with coefficients $-\mathrm{Gr}_{ij}$. Here we construct another representation of the same form, using positive weights of forests in the original graph and dual vertex sums of their components.

The Greenian is denoted by $\mathrm{Gr}$, and its dual representation by $Q_1$. Below, $Q_k=Q_1^k/k!$, $D=\exp Q_1$, and the centered image is $\mathcal C(D)=\exp(\mathrm{Gr})$. The name “dual grade” refers to its relationship with the complementary grade of $M=\exp L$. Both exponentials have boundary representations; the cut expression changes the arguments of the terms while preserving the form itself.

Each original spanning forest partitions the vertices into components. This partition determines a dual form whose deletion from the top form recovers the product of the direct component boundaries. Summing with the original forest weights and dividing by the spanning coefficient gives an explicit representation of every dual grade. It reveals the combinatorial meaning of the coefficients and is used for vertex variations.

The definition of duality, the deletion operation, and its connection with the standard interior product are presented in [[Laplacian and Greenian - Mutual Duality of Exponentials]]. Here we prove the combinatorial formula for dual grades: first for a single partition, then for the whole graph. General background on exterior algebra is also given in [1].

## Initial objects and notation

Let $G$ be a connected undirected graph on the vertex set $\mathcal V=\{a_1,\ldots,a_n\}$, with $n\ge2$. Existing edges have positive conductances; absent edges have zero conductance. Write differences as $a_{ij}=a_j-a_i=(a_i a_j)$; direct and dual arguments are distinguished by the specified space.

The direct vertices form a basis of $V$, and the space of affine vectors is $W=\ker\varepsilon$, where $\varepsilon(a_i)=1$. Set

$$
d=n-1,\qquad
\Omega=(a_1\ldots a_n),\qquad
T=[\Omega]^2
$$

The Laplacian polyform, the metric polyform, and its dual grades satisfy

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
M=\exp L=\sum_{j=0}^{d}M_j,\qquad
M_d/Q_k=M_{d-k}
\tag{1}
$$

Here $M_j=L^j/j!$, $M_0=e$, and $M_d=\tau T$, where $\tau=\tau(G)$ is the spanning coefficient. The basic normalization has $Q_0=e$. For unnormalized forest sums, we use only the auxiliary notation $\widetilde Q_k=\tau Q_k$ and $\widetilde D=\tau D$.

Dual arguments belong to $W^*\cong V^*/\mathbb R\varepsilon$. In vertex notation, they satisfy

$$
a_1+\cdots+a_n=0
$$

Here the relation concerns dual deletion elements. The direct vertices in $V$ remain independent; their centered images $a_i-h$, where $h=n^{-1}\sum_i a_i$, also sum to zero. The distinction between these representations and the transfer of identities to complementary grades are discussed in [[Symmetric Identities of the Greenian]].

For direct objects $X,Y$ and dual objects $A,B$, we use the action

$$
[X,Y]/[A,B]=[X/A,Y/B]
$$

It is linear in both arguments: a coefficient of the dual form multiplies the deletion result. The notation $[X]^2$ means the formal quadratic form $[X,X]$.

## Two forest representations

In the [[The Canonical Vector Representation of the Greenian#Signed forest grades|vector exponential]], grade $Q_k$ is assembled from forests with $k$ edges on the complete set of pairs. Their coefficients are products of $\gamma_{ij}=-\mathrm{Gr}_{ij}$ and may have either sign. The arguments are component boundaries on the dual side.

In the formulas of this note, the indexing forest belongs to the original graph and contains $d-k$ edges. Its positive weight is divided by $\tau$, and the dual argument is built from vertex sums of blocks. These are different expansions of equal forms. No correspondence between individual forests of the two expansions is asserted.

## The dual form of a partition

Let

$$
\pi=\{C_1,\ldots,C_{k+1}\},\qquad 0\le k\le d
$$

be a partition of $\mathcal V$ into nonempty blocks. The blocks are unordered; indices are used only for notation.

**Definition.** The dual vertex sum of a block $C$ is the element

$$
a_C=\sum_{a_i\in C}a_i
$$

For a full partition,

$$
a_{C_1}+\cdots+a_{C_{k+1}}=0
$$

**Definition.** The dual form of a partition $\pi$ is

$$
\boxed{\Phi_\pi=[a_{C_1}\cdots a_{C_k}]^2}
\tag{2}
$$

One block is omitted on the right, here $C_{k+1}$. For $k=0$, the product is empty and $\Phi_\pi=e$.

**Lemma.** The form $\Phi_\pi$ is independent of the omitted block and the order of the remaining blocks.

**Proof.** Permuting factors changes only the sign of their exterior product. If $C_r$ is omitted instead of $C_{k+1}$, use

$$
a_{C_{k+1}}=-\sum_{j=1}^{k}a_{C_j}
$$

Substitution into the product of all other block sums leaves only the term containing $a_{C_r}$: the others contain a repeated factor and vanish. Thus the new product agrees with the old one up to sign. The sign disappears in the quadratic form. $\square$

On the direct side, let $(C_j)$ denote the boundary of the simplex on the vertices of block $C_j$, taken in any order. A singleton block gives $(a_i)=1$. The corresponding [[Partition Forms and the Tetrahedron Identity|partition form]] is

$$
q_\pi=[(C_1)\cdots(C_{k+1})]^2
$$

Its grade is

$$
\sum_{j=1}^{k+1}(\#C_j-1)=n-k-1=d-k
$$

Thus $\Phi_\pi$ has dual grade $k$, while $q_\pi$ has the complementary direct grade $d-k$.

## The deletion identity for a single partition

**Lemma.** For any partition $\pi$ into $k+1$ nonempty blocks,

$$
\boxed{
T/\Phi_\pi=[(C_1)\cdots(C_{k+1})]^2=q_\pi
}
\tag{3}
$$

The coefficient is one and is independent of the block sizes.

**Proof.** Choose a vertex $p_j\in C_j$ in each block and place it first in the boundary notation. Write

$$
U_j=(C_j)=\prod_{a_i\in C_j\setminus\{p_j\}}(a_i-p_j)
$$

Fix any order of factors. For a singleton block, $U_j=1$.

Take the connecting vectors to be

$$
v_j=p_j-p_{k+1},\qquad 1\le j\le k
$$

All internal vectors $a_i-p_j$, together with $v_1,\ldots,v_k$, form the edge system of a tree on $\mathcal V$: each block contains a star, and the selected block vertices are joined to $p_{k+1}$. This is an auxiliary tree on the vertex set; its edges need not belong to $G$.

By the [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|product rule for tree vectors]],

$$
\Omega=\pm v_1\cdots v_k\,U_1\cdots U_{k+1}
$$

Now, for $1\le i,j\le k$,

$$
v_j/a_{C_i}=\delta_{ij}
$$

Moreover, each block sum $a_{C_i}$ vanishes on every internal vector $a_\ell-p_j$: both vertices lie in one block, so their contributions are either $1-1$ or $0-0$.

Successively deleting $a_{C_1},\ldots,a_{C_k}$ removes precisely the connecting vectors $v_1,\ldots,v_k$. We obtain

$$
\Omega/(a_{C_1}\cdots a_{C_k})
=\pm U_1\cdots U_{k+1}
$$

Passing to quadratic forms removes the sign and gives (3). For $k=0$, there are no deletions, and the equality means $T/e=T$. $\square$

The proof also establishes that the product in (2) is nonzero. No factors $\#C_j$ or factorials appear here: the deletion element takes the value $1$ on the corresponding connecting vector.

**Example.** For the partition $\{a,b\}\mid\{c,d\}$,

$$
\Phi_\pi=[a+b]^2=[c+d]^2,\qquad
T/\Phi_\pi=[(ab)(cd)]^2
$$

For the partition $\{a,b\}\mid\{c\}\mid\{d\}$, the block $\{a,b\}$ may be omitted:

$$
\Phi_\pi=[cd]^2,\qquad
T/[cd]^2=[(ab)]^2
$$

In the last formula, $cd$ is the exterior product of two dual elements, while $(ab)$ is a direct boundary.

## The forest formula for grades of the Greenian exponential

Let $\mathcal F_m(G)$ denote the set of spanning forests of the graph with exactly $m$ components. Each forest includes every vertex, including isolated ones. Its weight is

$$
w(F)=\prod_{\{i,j\}\in F}c_{ij}
$$

For the empty forest, $w(F)=1$. Denote the partition into forest components by $\pi(F)$.

**Theorem (forest grades).** For $0\le k\le d$,

$$
\boxed{
Q_k=\frac1\tau\sum_{F\in\mathcal F_{k+1}(G)}w(F)\Phi_{\pi(F)}
}
\tag{4}
$$

**Proof.** A forest with $k+1$ components has $n-k-1=d-k$ edges. The [[Laplacian Exponential#Grade components and spanning forests|forest expansion of the metric polyform]] gives

$$
M_{d-k}=\sum_{F\in\mathcal F_{k+1}(G)}w(F)q_{\pi(F)}
$$

Apply $M_d/\cdot=(\tau T)/\cdot$ to the right-hand side of (4), using (3). The factors $\tau$ and $1/\tau$ cancel, giving exactly $M_{d-k}$. By [[Laplacian and Greenian - Mutual Duality of Exponentials#Existence and uniqueness|uniqueness of the dual grade]], the right-hand side of (4) equals $Q_k$. $\square$

The sum in (4) runs over undirected forests without choosing roots in their components. Each edge set is counted once.

### Extreme grades

At $k=0$, the sum runs over spanning trees. Each has one block $\mathcal V$ and form $e$, so division by $\tau$ gives

$$
Q_0=e
$$

At $k=d$, there is only the empty forest. Consequently,

$$
Q_d=\frac1\tau[a_1\cdots a_{n-1}]^2,\qquad M_d/Q_d=e
\tag{5}
$$

Any vertex may be omitted. The top dual coefficient of this vertex form is the reciprocal of the original graph's spanning coefficient. In the vector representation, the full dual boundary has square $n^2[a_1\cdots a_{n-1}]^2$, so the signed sum of products of $\gamma_{ij}$ over trees is $1/(n^2\tau)$. The difference is explained by the normalization of the top argument.

### Normalized grades

All $Q_k$ already have the basic normalization $Q_0=e$. Unnormalized forest sums are auxiliary:

$$
\widetilde Q_k=\tau Q_k
=\sum_{F\in\mathcal F_{k+1}(G)}w(F)\Phi_{\pi(F)},\qquad
T/\widetilde Q_k=M_{d-k}
\tag{6}
$$

In particular, $\widetilde Q_0=\tau e$, while $\widetilde Q_d=[a_1\cdots a_{n-1}]^2$.

Each forest in (6) contains $d-k$ edges. Multiplying every conductance by $t>0$ gives

$$
\tau\longmapsto t^d\tau,\qquad
\widetilde Q_k\longmapsto t^{d-k}\widetilde Q_k,\qquad
Q_k\longmapsto t^{-k}Q_k
$$

The first dual form scales inversely to conductances, just as resistances do.

## Combining forests with identical components

Different forests may determine the same partition and the same form $\Phi_\pi$. Fix $\pi=\{C_1,\ldots,C_{k+1}\}$.

Constructing a forest with these components requires choosing a spanning tree independently in each induced graph $G[C_j]$, with the original conductances. Edges between blocks do not belong to this forest. Thus the total weight of forests with the given partition is

$$
\boxed{
\mu_\pi=\sum_{\substack{F\in\mathcal F_{k+1}(G)\\\pi(F)=\pi}}w(F)
=\prod_{j=1}^{k+1}\tau(G[C_j])
}
\tag{7}
$$

We set $\tau(G[C])=1$ for a one-vertex graph and $\tau(G[C])=0$ for a disconnected induced graph. With positive conductances, $\mu_\pi>0$ holds if and only if every block induces a connected graph.

Denote the set of partitions of $\mathcal V$ into $k+1$ blocks by $\Pi_{k+1}(\mathcal V)$. Grouping the terms in (4) gives

$$
\boxed{
Q_k=\frac1\tau\sum_{\pi\in\Pi_{k+1}(\mathcal V)}
\left(\prod_{C\in\pi}\tau(G[C])\right)\Phi_\pi
}
\tag{8}
$$

Each unordered partition is counted once. There is no multiplication or division by $(k+1)!$ in (8).

## Representing the Greenian through cuts

Let $A$ be a nonempty proper subset of $\mathcal V$, and let $A^c=\mathcal V\setminus A$. The notation $A\mid A^c$ denotes an unordered partition of the vertices into two parts.

**Definition.** The dual cut form of $A\mid A^c$ is

$$
[a_A]^2,\qquad a_A=\sum_{a_i\in A}a_i
$$

Since $a_{A^c}=-a_A$, the choice of part does not change the form:

$$
[a_{A^c}]^2=[a_A]^2
$$

For $k=1$, formula (8) gives

$$
\boxed{
Q_1=\frac1\tau\sum_{A\mid A^c}
\tau(G[A])\tau(G[A^c])[a_A]^2
}
\tag{9}
$$

Each cut is counted once in the sum. Summing over all nonempty proper subsets $A$ would count each cut twice and require a factor of $1/2$ before that sum.

Formula (9) uses spanning-tree weights **within the two parts**. They differ from the total conductance of crossing edges,

$$
\sum_{\{i,j\}\in\delta_G(A)}c_{ij},\qquad
\delta_G(A)=\{\{i,j\}\in E:a_i\in A,\ a_j\in A^c\}
$$

Here $\delta_G(A)$ is the set of cut edges. These edges do not belong to the two-component forests counted for the given $A\mid A^c$.

The total conductance of crossing edges appears as the normalized potential of the cut form in the Greenian exponential. For $s_A=\sum_{i\in A}(a_i-h)$ and $N=\exp(\mathrm{Gr})$, we have $P_N([s_A]^2)=\sum_{\{i,j\}\in\delta_G(A)}c_{ij}$. The proof and the distinction between coefficient and potential are given in the [[The Greenian Metric and Potentials#The potential of a cut form|section on cut potential]].

### The partition, cut edges, and forest

For $K_4$ and the partition $\{a,b\}\mid\{c,d\}$, distinguish:

| Object | Contents |
|---|---|
| Vertex partition | Two blocks $\{a,b\}$ and $\{c,d\}$ |
| Set of cut edges | $\{ac,ad,bc,bd\}$ |
| Spanning forest with these components | $\{ab,cd\}$ |
| Dual cut form | $[a+b]^2=[c+d]^2$ |
| Direct forest form | $[(ab)(cd)]^2$ |

With unit conductances, this partition has forest weight $1$, although four edges cross it. For arbitrary positive conductances on $K_4$, the weight is $c_{ab}c_{cd}$. Its coefficient in $Q_1$ is obtained by dividing this weight by $\tau$.

For the partition $\{a\}\mid\{b,c,d\}$, there are three forests, with edge sets

$$
\{bc,bd\},\qquad \{bc,cd\},\qquad \{bd,cd\}
$$

They all give the same dual form $[a]^2$. Their total weight is

$$
\tau(G[\{a\}])\tau(G[\{b,c,d\}])
=c_{bc}c_{bd}+c_{bc}c_{cd}+c_{bd}c_{cd}
$$

Thus one cut form may collect several different spanning 2-forests.

## Full example: the unit complete graph K4

Let all six conductances on vertices $a,b,c,d$ equal $1$, and let $T=[(abcd)]^2$.

### Forests and coefficients

There are $16$ spanning trees: four stars and $4!/2=12$ paths. Thus $\tau=16$.

| Number of components | Component sizes | Number of partitions | Forests per partition | Total forests |
|---:|---|---:|---:|---:|
| $1$ | $[4]$ | $1$ | $16$ | $16$ |
| $2$ | $[3,1]$ | $4$ | $3$ | $12$ |
| $2$ | $[2,2]$ | $3$ | $1$ | $3$ |
| $3$ | $[2,1,1]$ | $6$ | $1$ | $6$ |
| $4$ | $[1,1,1,1]$ | $1$ | $1$ | $1$ |

The component sizes in the table are sizes of vertex blocks. They must not be confused with the grades of the boundaries of those blocks.

### Direct grades

The forest expansion gives

$$
M_0=e
$$

$$
M_1=[(ab)]^2+[(ac)]^2+[(ad)]^2+[(bc)]^2+[(bd)]^2+[(cd)]^2
$$

$$
\begin{aligned}
M_2={}&3\bigl([(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2\bigr)+\\
&+[(ab)(cd)]^2+[(ac)(bd)]^2+[(ad)(bc)]^2
\end{aligned}
$$

$$
M_3=16T
$$

The coefficient $3$ of each three-vertex boundary counts the three trees on that triple. The three remaining terms correspond to partitions into two pairs.

### Dual grades

For clarity, first write the unnormalized forest sums $\widetilde Q_k=16Q_k$:

$$
\widetilde Q_0=16e
$$

$$
\boxed{
\begin{aligned}
\widetilde Q_1={}&3\bigl([a]^2+[b]^2+[c]^2+[d]^2\bigr)+\\
&+[a+b]^2+[a+c]^2+[a+d]^2
\end{aligned}
}
\tag{10}
$$

$$
\widetilde Q_2=[ab]^2+[ac]^2+[ad]^2+[bc]^2+[bd]^2+[cd]^2,\qquad
\widetilde Q_3=[abc]^2
\tag{11}
$$

In $\widetilde Q_1$, the three two-element sums represent three different partitions into pairs. In $\widetilde Q_2$, each argument is a product of two dual vertices, not a boundary.

Check the correspondence independently of the coefficient count. Formula (3) gives

$$
T/[a]^2=[(bcd)]^2,\qquad
T/[a+b]^2=[(ab)(cd)]^2
$$

The other one-block and two-block choices follow by vertex permutations. For the second dual grade,

$$
T/[ab]^2=[(cd)]^2,\qquad
T/[ac]^2=[(bd)]^2,\qquad
T/[ad]^2=[(bc)]^2
$$

The three remaining pairs recover complementary edges similarly. Finally,

$$
T/[abc]^2=e
$$

Consequently,

$$
T/\widetilde Q_0=M_3,\qquad
T/\widetilde Q_1=M_2,\qquad
T/\widetilde Q_2=M_1,\qquad
T/\widetilde Q_3=M_0
$$

In the forest normalization, $\widetilde D=16e+\widetilde Q_1+\widetilde Q_2+\widetilde Q_3$. The Greenian exponential in the basic normalization is $D=\widetilde D/16$:

$$
D=e+\frac{\widetilde Q_1}{16}+\frac{\widetilde Q_2}{16}+\frac{[abc]^2}{16},\qquad
(16T)/D=M
$$

## A weighted triangle

Let all three conductances $c_{ab},c_{ac},c_{bc}$ be positive. Here

$$
T=[(abc)]^2,\qquad
\tau=c_{ab}c_{ac}+c_{ab}c_{bc}+c_{ac}c_{bc}
$$

The direct grades are

$$
M_0=e,\qquad
M_1=c_{ab}[(ab)]^2+c_{ac}[(ac)]^2+c_{bc}[(bc)]^2,\qquad
M_2=\tau T
$$

Each spanning 2-forest consists of one edge and an isolated vertex:

| Forest edge | Partition into components | Contribution to $\widetilde Q_1=\tau Q_1$ |
|---|---|---|
| $bc$ | $\{a\}\mid\{b,c\}$ | $c_{bc}[a]^2$ |
| $ac$ | $\{b\}\mid\{a,c\}$ | $c_{ac}[b]^2$ |
| $ab$ | $\{c\}\mid\{a,b\}$ | $c_{ab}[c]^2$ |

Therefore

$$
\boxed{
\widetilde Q_0=\tau e,\qquad
\widetilde Q_1=c_{bc}[a]^2+c_{ac}[b]^2+c_{ab}[c]^2,\qquad
\widetilde Q_2=[ab]^2
}
\tag{12}
$$

On the dual side, $a+b+c=0$. Direct deletion gives

$$
T/[a]^2=[(bc)]^2,\qquad
T/[b]^2=[(ac)]^2,\qquad
T/[c]^2=[(ab)]^2,\qquad
T/[ab]^2=e
$$

Thus the action $T/\widetilde Q_k$ for all three grades in (12) recovers the corresponding direct grades. The Greenian exponential in the basic normalization is

$$
D=
e+\frac{c_{bc}[a]^2+c_{ac}[b]^2+c_{ab}[c]^2}{\tau}
+\frac{[ab]^2}{\tau}
$$

The coefficient of $[a]^2$ in $Q_1$ is $c_{bc}/\tau$ and is determined by the edge $bc$ within the opposite part of the partition. It is not the sum of conductances $c_{ab}+c_{ac}$ incident to vertex $a$.

## Uniqueness of the form and nonuniqueness of its expansion

The forest coefficients (7) are uniquely determined by the original graph and the specified blocks. However, forms of different partitions may be linearly dependent.

Under $a+b+c+d=0$, the dual space satisfies

$$
\boxed{
[a+b]^2+[a+c]^2+[a+d]^2
=[a]^2+[b]^2+[c]^2+[d]^2
}
\tag{13}
$$

**Proof.** Expanding the left-hand side by bilinearity gives

$$
3[a]^2+[b]^2+[c]^2+[d]^2+\{a,b+c+d\}
$$

Since $b+c+d=-a$, the last term equals $-2[a]^2$. The remaining expression is the right-hand side of (13). $\square$

Thus form (10) can be reduced to

$$
\widetilde Q_1=4\bigl([a]^2+[b]^2+[c]^2+[d]^2\bigr)
$$

In the original unnormalized forest representation, the coefficient sum is $4\cdot3+3=15$, counting spanning 2-forests of $K_4$. In the reduced expression, the coefficient sum is $4\cdot4=16$. The dual form itself has not changed.

This yields an important distinction: forest coefficients must be read in **representation (8)**, including the common factor $1/\tau$. An arbitrary algebraic rewriting of the same form need not preserve the combinatorial meaning of individual terms or their coefficient sum.

This does not contradict recovery of the graph from the full Greenian exponential. The top grade of $D$ determines $\tau$, while the action $M_d/D$ recovers $M$ and its first grade $L$, after which the forest coefficients can be recalculated from the graph. However, they are not coefficients in a linearly independent basis of all partition forms. The canonical vector coefficients determine the Green matrix; the transition from them to the resistances in the polar expression and to the original forest weights is discussed in [[Greenian Coefficients and Vertex Variations]].

## Products of cut forms and further development

The main calculation of the exponential uses vector factors from the [[The Canonical Vector Representation of the Greenian#Multiplication of vector forms and the exponential|canonical representation]]. Direct multiplication of cut forms is also valid, but individual terms may require polarization and need not be a single partition form.

The product of two cut forms is defined by the exterior product of their dual arguments:

$$
[a_A]^2[a_B]^2=[a_Aa_B]^2
$$

A repeated factor makes the product zero. For distinct cuts, the result is a dual form of grade two, but its connection with an individual forest must be checked: two bipartitions do not automatically determine a partition into three components.

For example, take the crossing cuts $\{a,b\}\mid\{c,d\}$ and $\{a,c\}\mid\{b,d\}$ on four vertices. Then

$$
(a+b)(a+c)=-ab+ac+bc
$$

Here all factors are dual elements, and parentheses group sums. Passing to the form $[-ab+ac+bc]^2$ also produces polar terms. Thus each individual term in a product of cut sums cannot be identified with one forest.

The equality of the full sums, $Q_k=Q_1^k/k!$, is proved in the [[The Exterior Exponential and Representations of the Greenian#Application to the metric polyform of a graph|exponential law for dual grades]]. The connection between the cut form and the Greenian is established there as well. This equality does not require individual cut products to correspond to individual forests.

## Status of results and connections with the literature

The text proves the deletion identity (3), the forest formula (4), grouping by partitions (8), and the formula for the first dual form (9). The examples of $K_4$ and a weighted triangle were obtained by enumerating forests and checked through deletion. These proofs do not use the general power law for dual grades.

In addition, identity (3) and independence of the omitted block were checked in exact rational arithmetic for all 277 partitions of sets with 2–6 vertices. For $K_4$, two choices of triangle weights, and a weighted path, the forest coefficients (7) were checked against products of Laplacian cofactors of the induced blocks. These finite checks supplement the general proofs above.

The algebraic foundation is the standard interior product and duality of complementary exterior powers [1]; its precise comparison with double forms and the Poincaré map appears in the [[Laplacian and Greenian - Mutual Duality of Exponentials#Connection with classical exterior duality|discussion of exterior duality]].

The all-minors Laplacian theorem provides the classical matrix representation of forest sums; Chaiken gives a combinatorial proof [2]. There, restrictions on forests are specified by the deleted sets of rows and columns. In this note, forests are grouped by full vertex partitions and counted without choosing roots. Thus weights (7) must not be replaced by rooted-forest weights with additional factors of component sizes.

The general graph statements here concern connected undirected graphs with positive conductances. Identity (3) itself is algebraic and requires neither a graph nor a metric. The balanced extension of the graph formulas requires separate treatment.

## References

1. Greub W. *Multilinear Algebra*. 2nd ed. Springer, 1978. [DOI: 10.1007/978-1-4613-9425-9](https://doi.org/10.1007/978-1-4613-9425-9). Chapters 5, “Exterior Algebra”, and 6, “Mixed Exterior Algebra”: the standard machinery of exterior and mixed exterior algebra.
2. Chaiken S. *A Combinatorial Proof of the All Minors Matrix Tree Theorem*. SIAM Journal on Algebraic Discrete Methods, 3(3) (1982), 319–329. [DOI: 10.1137/0603033](https://doi.org/10.1137/0603033). The theorem expresses Laplacian minors through weighted forests with conditions on designated vertices.

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
