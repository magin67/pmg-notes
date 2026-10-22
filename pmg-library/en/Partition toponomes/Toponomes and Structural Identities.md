---
title: Toponomes and Structural Identities
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: partition-toponomes-and-structural-identities
lang: en
description: "Why equal polyforms can have different toponomes of their chosen representations: the tetrahedron identity, grade two of the K4 exponential, and a criterion for representation-independent reduction."
order: 2
---

In [[From Polyforms to Partitions]], a toponome is defined for a chosen sum of partition forms: each term is replaced by its positive type, and coefficients of equal types are collected. We now examine what happens if a structural identity is applied before this replacement.

The main example is the [[Partition Forms and the Tetrahedron Identity#The tetrahedron identity|tetrahedron identity]]. It relates forms of different types and exposes the distinction between equality of polyforms and equality of toponomes. The same passage is then considered within the exponential of the complete graph $K_4$.

## One identity and two toponomes

Let $A=\{a,b,c,d\}$ be a set of four independent basis vertices. In the adopted normalization of symmetric sums,

$$
E_4[1,1]=[(ab)(cd)]^2+[(ac)(bd)]^2+[(ad)(bc)]^2
$$

$$
E_4[2,0]=[(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2
$$

The first sum lists all three partitions into two pairs. The second lists all four partitions into a triple and a singleton; the boundary of the singleton block is $1$ and is omitted from the form argument. Each partition has coefficient $1$.

Square brackets in $E_n[\lambda]$ retain the notation for symmetric polyforms. Standalone toponome types are written in parentheses, following the [[From Polyforms to Partitions#From a partition form to its type|definition of a type]].

The tetrahedron identity states that these polyforms are equal:

$$
\boxed{E_4[1,1]=E_4[2,0]}
$$

![Three partitions of four vertices into pairs and four partitions into a triple and a singleton](Partitions%20in%20the%20tetrahedron%20identity.svg)

*Figure 1. Each diagram shows all four vertices. The three upper partitions have positive type $(1^2)$; the four lower partitions have type $(2)$. Triangles depict three-vertex blocks, not edge sets of a spanning forest. Both cases have grade $k=2$ and total component count $m=2$; their numbers of nontrivial components and singleton vertices differ.*

Denote the displayed expressions by $\mathcal E_L$ and $\mathcal E_R$. The definition of a toponome gives

$$
T_{\mathcal E_L}=3(1^2),\qquad T_{\mathcal E_R}=4(2)
$$

These are different elements of the space of formal linear combinations of types. The symbols $(1^2)$ and $(2)$ are independent, so

$$
3(1^2)-4(2)\ne0
$$

Thus, equality of polyforms is not preserved when each form is replaced by its type. The tetrahedron identity remains valid; the reduction rule is incompatible with it.

## A formal sum and the polyform it represents

For a fixed set $A$ of size $n=\#A$, the partition $\pi=B_1|\cdots|B_m$ corresponds to the form

$$
q_\pi=[(B_1)\cdots(B_m)]^2
$$

The positive type $\lambda(\pi)$ consists of the nonzero grades $\#B_i-1$. If its weight is $k$ and its number of parts is $r$, then $m=n-k$ and the number of singleton vertices is $\ell=n-k-r$.

In a formal sum, each labelled partition is a separate symbol. Passage to a polyform replaces that symbol by $q_\pi$. Different formal sums may give the same polyform because the forms $q_\pi$ satisfy linear relations. This distinction is already used in the [[Basis and Dimension of the Space of Partition Forms#The space whose dimension we compute|definition of the space of partition forms]].

Reduction by types makes a different replacement: a labelled partition maps to $\lambda(\pi)$. Linearity on formal sums does not ensure independence from the polyform representation. Such independence requires every relation between forms to be preserved.

**Remark.** Vertex relabelling and application of a structural identity are different transformations. A vertex permutation maps every partition to one of the same type and therefore preserves the toponome when coefficients are carried along with the terms. A structural identity may relate different collections of types, as in the tetrahedron example. Invariance under relabelling does not remove dependence on representation.

## Grade two of the complete-graph exponential

Consider the complete graph $K_4$ with unit weights on all six edges. Its Laplacian is

$$
\begin{aligned}
L={}&[(ab)]^2+[(ac)]^2+[(ad)]^2+\\
&+[(bc)]^2+[(bd)]^2+[(cd)]^2
\end{aligned}
$$

We consider the grade component $M_2=L^2/2$ of $\exp L$. The square of each individual edge form is zero; a product of two distinct edge forms occurs twice in $L^2$. Hence $M_2$ contains one contribution for every unordered pair of distinct edges.

There are $\binom62=15$ such pairs. Each gives a two-edge spanning forest on four vertices. Three pairs have disjoint edges: $ab,cd$; $ac,bd$; $ad,bc$. The other twelve share a vertex and are distributed over four three-vertex blocks.

Each such block supports three trees. For example, on $\{a,b,c\}$,

$$
[(ab)(ac)]^2=[(ab)(bc)]^2=[(ac)(bc)]^2=[(abc)]^2
$$

Thus, the form of each three-vertex block has coefficient $3$. Written in full, the representation $\mathcal E_F$ obtained from the edge factors is

$$
\begin{aligned}
M_2={}&3[(abc)]^2+3[(abd)]^2+3[(acd)]^2+3[(bcd)]^2+\\
&+[(ab)(cd)]^2+[(ac)(bd)]^2+[(ad)(bc)]^2
\end{aligned}
$$

In symmetric-sum notation,

$$
M_2=3E_4[2,0]+E_4[1,1]
$$

Applying the tetrahedron identity gives another representation $\mathcal E_P$ of the same grade component:

$$
\begin{aligned}
M_2&=4E_4[2,0]\\
&=4[(abc)]^2+4[(abd)]^2+4[(acd)]^2+4[(bcd)]^2
\end{aligned}
$$

This agrees with the [[Symmetric Polyforms of the Complete Graph#The Laplacian and exponential of the complete graph|general formula for the grade components of the complete-graph exponential]], $M_k=n^{k-1}E_n[k]$ for $k\geqslant1$.

The two expressions have different toponomes:

$$
\boxed{T_{\mathcal E_F}=12(2)+3(1^2),\qquad T_{\mathcal E_P}=16(2)}
$$

Their difference is $3(1^2)-4(2)$. In $\mathcal E_F$, the coefficient sum $12+3=15$ counts two-edge spanning forests. In $\mathcal E_P$, it is $16$ and no longer has this meaning: the coefficients were obtained by applying a structural identity.

The number of forests of the graph has not changed. The polyform expression has changed, together with the meaning of its coefficient sum. Nor does the coefficient $4$ in $\mathcal E_P$ mean that a fourth tree has appeared on a fixed triple.

## A criterion for representation-independent reduction

Assign to each partition $\pi$ an element $s_\pi$ of a real vector space $U$. Define a linear rule on formal sums by carrying the coefficient $c_\pi$ from $\pi$ to $s_\pi$. The space $U$ may be a space of types, polynomials, or numbers.

> [!info] Preserving structural relations
> **Proposition.** The rule defines a linear map on the space of partition forms $\mathcal P_n$, independent of the chosen expression, if and only if the following condition holds for every choice of real coefficients $c_\pi$:
>
> $$
> \sum_\pi c_\pi q_\pi=0
> \quad\Longrightarrow\quad
> \sum_\pi c_\pi s_\pi=0
> $$

> [!note]- Formal statement and proof
> **Proof.** Use the [[Basis and Dimension of the Space of Partition Forms#The space whose dimension we compute|free partition symbols]] $b_\pi$. Let $\mathcal F_n$ be the direct sum of the spaces $\mathcal F_{n,k}$ over all grades. Define the linear maps
>
> $$
> \Phi_n:\mathcal F_n\longrightarrow\mathcal P_n,
> \qquad \Phi_n(b_\pi)=q_\pi
> $$
>
> $$
> S:\mathcal F_n\longrightarrow U,
> \qquad S(b_\pi)=s_\pi
> $$
>
> The structural relations form $\ker\Phi_n$. The condition in the proposition is
>
> $$
> \ker\Phi_n\subseteq\ker S
> $$
>
> If a linear map $\overline S:\mathcal P_n\to U$ exists with $S=\overline S\circ\Phi_n$, this inclusion is necessary.
>
> Conversely, assume the inclusion. For $P=\Phi_n(v)$, set $\overline S(P)=S(v)$. If $\Phi_n(v)=\Phi_n(w)$, then $v-w\in\ker\Phi_n\subseteq\ker S$, so $S(v)=S(w)$. The value is independent of the representative, and linearity follows from that of $S$. The map is unique because the forms $q_\pi$ span $\mathcal P_n$. $\square$

For the usual reduction by types, $s_\pi=\lambda(\pi)$. The tetrahedron identity shows that the criterion fails: a zero relation between forms maps to the nonzero combination $3(1^2)-4(2)$.

One could impose relations on the type symbols by requiring such combinations to vanish. The types would then cease to be independent basis symbols. This would be a different object requiring its own definition; polyform equalities cannot automatically be transferred to the toponome space of the [[From Polyforms to Partitions#The toponome of a chosen representation|original definition]].

## Convention for the toponome of an exponential

For a graph $G$ with specified weights, fix the exponential representation obtained by expanding its edge factors. Each spanning forest contributes the product of its edge weights; contributions are then grouped by type. The notation $T_G$ in the [[From Polyforms to Partitions#The Laplacian exponential and forest coefficients|definition of a graph toponome]] refers to this expression.

Within the chosen expression, terms may be reordered and coefficients of repeated labelled partitions collected without changing the toponome. Replacing a sum of forms by another sum using a structural identity before reduction requires a separate check. For $K_4$, the distinction is expressed by the two computed grade-$2$ toponomes.

This convention allows us to speak of the toponome of a graph or its exponential with a fixed expansion procedure. It selects a representation; it does not turn termwise reduction of arbitrary expressions into a linear map on the whole polyform algebra.

## Numerical evaluations and preservation of identities

Some numerical evaluations respect structural identities. For example, replacing a grade-$j$ component by its vertex count $j+1$, multiplying component weights, and summing contributions maps both sides of the tetrahedron identity to the same number:

$$
3(1^2)\longmapsto3\cdot2^2=12,
\qquad
4(2)\longmapsto4\cdot3=12
$$

The general condition on component weights preserving all equalities of the fundamental theorem of SPFs is proved in the [[Fundamental Theorem of Symmetric Polyforms#Substituting numbers for components while preserving identities|corollary on admissible weights]]. That section also explains the relation to choosing one root vertex in each component.

A numerical evaluation combines information about different types. Multiplying the coefficients by those weights while retaining the types gives the distinct formal combinations $12(1^2)$ and $12(2)$. Equality of numerical values therefore does not imply equality of toponomes or remove the distinction between chosen representations.

## Results used

- [[From Polyforms to Partitions]] - the toponome of a chosen representation and the meaning of its coefficients.
- [[Partition Forms and the Tetrahedron Identity]] - the proof of the structural identity on four vertices.
- [[Basis and Dimension of the Space of Partition Forms]] - free partition symbols, the map to the space of forms, and the kernel of structural relations.
- [[Symmetric Polyforms of the Complete Graph]] - grade components of the complete-graph exponential and forest counts.
- [[Fundamental Theorem of Symmetric Polyforms]] - numerical component weights that preserve symmetric identities.
