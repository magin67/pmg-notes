---
title: Partition Products and Boundary Forms
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: partition-products-and-boundary-forms
lang: en
description: "Realizing partition multiplication by gluing boundary components at chosen roots: examples, coefficients, and the distinction from ordinary polyform multiplication."
order: 5
---

In [[The Second-Kind Algebra on Partitions|the second-kind algebra]], multiplication enumerates partial matchings of parts: matched parts merge by adding their weights. In the boundary interpretation, this addition is realized by gluing two components at one vertex. Choosing a root in each component and summing over partial matchings of roots gives a family of forms whose toponome is the product of the original types.

Below, we compare this construction with ordinary multiplication of particular forms. In the latter, the shared vertices are already specified, whereas the sum of gluings ranges over different arrangements of components. The construction requires no metric.

## A partition part as the grade of a boundary

Let $k\geqslant1$, and let $A$ be a collection of $k+1$ distinct basis vertices. The boundary $(A)$ has grade $k$. The product of the edge vectors of any tree on $A$ equals this boundary up to sign. Thus the quadratic form $[(A)]^2$ has positive type $(k)$ and can be depicted by such a tree.

For pairwise disjoint blocks $A_1,\ldots,A_r$, each containing at least two vertices,

$$
q=\bigl[(A_1)\cdots(A_r)\bigr]^2,
\qquad
\lambda(q)=(\#A_1-1,\ldots,\#A_r-1)
$$

Here $\lambda(q)$ refers to the specified partition. [[From Polyforms to Partitions#Singleton vertices and type parameters|Singleton blocks]] contribute unit factors and are omitted from the positive type.

| Positive type | Representative form | Graph depiction |
| --- | --- | --- |
| $(1)$ | $[(ab)]^2$ | One edge |
| $(2)$ | $[(abc)]^2$ | A tree on three vertices |
| $(1^2)$ | $[(ab)(cd)]^2$ | Two disjoint edges |
| $(2,1)$ | $[(abc)(de)]^2$ | A three-vertex tree and a separate edge |

![Four positive types of forms depicted by trees: one edge, a two-edge tree, two separate edges, and a two-edge tree with a separate edge](Boundary%20types%20and%20trees.svg)

*Figure 1. A part of the type records the grade of a boundary. For a tree, this is the number of edges, one less than the number of vertices. Isolated vertices are not shown. The depicted trees are representatives of boundaries; no sum over all trees on a block is taken here.*

In the [[Graph Colorings and Partition Products|coloring model]], parts were represented by vertices of an auxiliary complete graph, with their values giving the vertex weights. Here, the part $(1)$ is represented by a connection between two vertices. The abstract multiplication rule for types remains the same; its realization changes.

## The product of two particular components

Quadratic forms satisfy

$$
[X]^2[Y]^2=[XY]^2
$$

The result is determined by the exterior product of the arguments. For boundaries on sets of distinct basis vertices, the [[Core specification#Products of simplex boundaries|boundary multiplication rules]] apply:

1. If the vertex sets are disjoint, the two components remain separate.
2. If they share exactly one vertex, the components merge and their grades add.
3. If they share at least two vertices, the product is zero.

For example,

$$
[(ab)]^2[(cd)]^2=[(ab)(cd)]^2
$$

$$
[(ab)]^2[(bc)]^2=[(abc)]^2
$$

$$
[(ab)]^2[(ab)]^2=0
$$

In every case, both factors have type $(1)$, but the results differ. Thus the types of the factors alone, without data on shared vertices, do not determine the product of particular forms.

**Lemma.** Suppose $A$ and $B$ share exactly one vertex $p$, and their boundaries have grades $k$ and $l$. Then

$$
[(A)]^2[(B)]^2=[(A\cup B)]^2,
\qquad
\#(A\cup B)-1=k+l
$$

> [!note]- Proof
> **Proof.** Put $p$ first in both ordered vertex lists. The boundaries are products of differences relative to $p$:
>
> $$
> (pa_1\ldots a_k)=(a_1-p)\cdots(a_k-p)
> $$
>
> Their product is therefore the boundary $(pa_1\ldots a_kb_1\ldots b_l)$. A different vertex order may introduce a sign, which disappears in the quadratic form. The union has $(k+1)+(l+1)-1$ vertices, giving the formula for its grade. $\square$

## Partial gluings at chosen roots

Take two types

$$
\lambda=(k_1,\ldots,k_r),\qquad
\mu=(l_1,\ldots,l_s)
$$

Choose blocks $A_1,\ldots,A_r,B_1,\ldots,B_s$ that are pairwise disjoint throughout the list and have sizes

$$
\#A_i=k_i+1,\qquad \#B_j=l_j+1
$$

Choose one vertex in each block in advance: $p_i\in A_i$, $q_j\in B_j$. Call it the **root**. This is additional data for the construction; a root does not change the original boundary or its form.

**Definition.** For a partial matching $H$ between the indices of the two types, glue the roots $p_i$ and $q_j$ of each pair $(i,j)\in H$. Make no other identifications. Each component participates in at most one pair.

Gluing identifies vertices without adding an edge between them. Two trees become one tree with a shared root vertex. Unmatched components remain unchanged.

### Writing all results on one vertex set

All results can be written in a single original space. For each pair $(i,j)\in H$, replace $q_j$ with $p_i$ in the second factor, leaving all other vertices unchanged. Denote this linear substitution by $\varphi_H$ and extend it to exterior products. Then

$$
U=(A_1)\cdots(A_r),\qquad
V=(B_1)\cdots(B_s)
$$

$$
q_H=[U]^2[\varphi_H(V)]^2=\bigl[U\varphi_H(V)\bigr]^2
$$

The substitution replaces one basis vertex with another and commutes with the boundary operator. The label $q_j$ no longer occurs in the argument of the result. If the original vertex set is retained, $q_j$ is counted as a singleton block. In this way, the forms $q_H$ for all $H$ belong to the same polyform algebra.

**Theorem.** Let $\mathcal E_{\lambda,\mu}$ be the chosen representation as a sum of forms over all partial matchings, including the empty matching:

$$
\mathcal E_{\lambda,\mu}=\sum_H q_H
$$

Its toponome equals the product of types in the second-kind algebra:

$$
\boxed{T_{\mathcal E_{\lambda,\mu}}=\lambda*\mu}
$$

> [!note]- Proof
> **Proof.** For the empty matching, all components remain separate. For each pair $(i,j)\in H$, the corresponding blocks share one vertex after substitution. By the lemma, their forms give one component of grade $k_i+l_j$. All other blocks remain disjoint because no index is repeated in a matching and no other identifications are made.
>
> Thus the positive type of $q_H$ is obtained by replacing each pair $k_i,l_j$ with their sum $k_i+l_j$ and retaining all unmatched parts. This is the type $\nu_H$ in the definition of $\lambda*\mu$. Each matching occurs once, so passing to types gives $\sum_H\nu_H=\lambda*\mu$. $\square$

The particular roots and the trees chosen for the figures do not affect the resulting coefficients of types. The forms on named vertices may nevertheless depend on the chosen roots. The statement concerns the toponome of the specified representation.

If one type is empty, there is a unique matching and no gluing. The unit form $e$ corresponds to the empty type $1$, which preserves the other factor.

## Simple examples

Two one-part types admit two matchings: the empty matching and a single pair. Hence

$$
(1)*(1)=(1^2)+(2)
$$

Take edges $ab$ and $cd$, with roots $a$ and $c$. The two terms in the sum of gluings are

$$
\mathcal E_{(1),(1)}=[(ab)(cd)]^2+[(abd)]^2
$$

The second term is obtained by the substitution $c\mapsto a$; if the four original vertices are retained, $c$ becomes a singleton block.

For a boundary of grade $2$ and a separate connection, we similarly obtain

$$
(2)*(1)=(2,1)+(3)
$$

Choosing root $a$ in the block $abc$ and root $d$ in the block $de$ gives

$$
\mathcal E_{(2),(1)}=[(abc)(de)]^2+[(abce)]^2
$$

Here the second term corresponds to the substitution $d\mapsto a$.

![Two possibilities for the products (1)*(1) and (2)*(1): keep the components separate or glue their chosen roots](Simple%20gluings%20of%20boundary%20components.svg)

*Figure 2. Blue edges represent the first factor, and orange edges the second. A double circle marks a root. On the left, there is no gluing; on the right, the roots are identified. The upper row gives types $(1^2)$ and $(2)$, and the lower row gives $(2,1)$ and $(3)$. The freed labels $c$ and $d$, counted as isolated vertices in the common space, are omitted from the right-hand panels.*

## Seven gluings for two pairs of connections

For two factors of type $(1^2)$,

$$
\boxed{(1^2)*(1^2)=(1^4)+4(2,1^2)+2(2^2)}
$$

Represent the first factor by edges $p_1a_1,p_2a_2$, and the second by edges $q_1b_1,q_2b_2$. All eight vertices are initially distinct. The roots are $p_1,p_2,q_1,q_2$.

![Seven gluings of two pairs of edges: one with no gluing, four with one gluing, and two with two gluings](Seven%20gluings%20of%20boundary%20components.svg)

*Figure 3. All partial matchings of two pairs of components are shown. Edge colors retain membership in the original factor, and double circles mark roots. A label $p_i=q_j$ at a shared vertex indicates gluing; the formulas use the name $p_i$. Isolated vertices arising when the results are written on the common set of eight vertices are omitted.*

**No gluings.** The empty matching gives one form

$$
\bigl[(p_1a_1)(p_2a_2)(q_1b_1)(q_2b_2)\bigr]^2
$$

Its type is $(1^4)$.

**One gluing.** Either of the two roots of the first factor can be paired with either root of the second. This gives four matchings. For example, the substitution $q_1\mapsto p_1$ gives

$$
\bigl[(p_1a_1b_1)(p_2a_2)(q_2b_2)\bigr]^2
$$

Each of the four forms consists of one component of grade $2$ and two components of grade $1$. Their combined contribution is $4(2,1^2)$.

**Two gluings.** There are two bijections between the two pairs of roots. They give the forms

$$
\bigl[(p_1a_1b_1)(p_2a_2b_2)\bigr]^2,
\qquad
\bigl[(p_1a_1b_2)(p_2a_2b_1)\bigr]^2
$$

Both have type $(2^2)$, contributing $2(2^2)$.

### Grade and number of components

All seven terms have grade $4$. The number of vertices incident to edges depends on the number of gluings. If the original set of $n=8$ vertices is retained, the full number of components in every term is $m=n-4=4$:

| Number of gluings $h$ | Positive type | Vertices in nontrivial components | Nontrivial components | Singleton vertices $\ell$ | Full number of components $m$ |
| --- | --- | ---: | ---: | ---: | ---: |
| $0$ | $(1^4)$ | $8$ | $4$ | $0$ | $4$ |
| $1$ | $(2,1^2)$ | $7$ | $3$ | $1$ | $4$ |
| $2$ | $(2^2)$ | $6$ | $2$ | $2$ | $4$ |

In the general construction with no original singleton blocks, write $k=w(\lambda)+w(\mu)$ for the total grade. Then $n=k+r+s$. A matching of $h$ pairs leaves $r+s-h$ nontrivial components and $h$ singleton vertices, so $m=r+s=n-k$. Any original singleton blocks remain unchanged and increase $n$, $m$, and $\ell$ by the same number.

## Coefficients and sums of forms

The coefficient of a type counts partial matchings of components. It does not include the number of ways to choose roots: the roots have already been chosen in this construction. If, for one pair of blocks of grades $k,l$, we also enumerate all choices of vertices to identify, there are $(k+1)(l+1)$ possibilities. That would be a different count.

The product of block sizes $[k_i+1]!$ appears when [[Fundamental Theorem of Symmetric Polyforms#Substituting numbers for components while preserving identities|all choices of roots are counted]]. No such weight is introduced here. Roots make each matching unambiguous.

The construction extends by bilinearity to chosen representations

$$
\mathcal E=\sum_\pi c_\pi q_\pi,
\qquad
\mathcal F=\sum_\sigma d_\sigma q_\sigma
$$

First place the two representations on disjoint copies of their vertex sets and choose roots in the nontrivial blocks of each term. For each pair $\pi,\sigma$, enumerate the partial gluings and retain the factor $c_\pi d_\sigma$. If $\mathcal G$ denotes the resulting representation as a sum of forms, the theorem and linearity of reduction give

$$
T_{\mathcal G}=T_{\mathcal E}*T_{\mathcal F}
$$

This statement concerns the constructed sum of gluings. The dependence of reduction on the chosen representation, discussed in the [[Toponomes and Structural Identities|note on structural identities]], remains.

## Limits of the model and ordinary polyform multiplication

In a partial matching, each component of one factor interacts with at most one component of the other. Particular forms on a common vertex set may have other patterns of intersection.

For example,

$$
\boxed{[(ab)(cd)]^2[(bc)]^2=[(abcd)]^2}
$$

The first factor has type $(1^2)$ and the second type $(1)$. The connection $bc$ joins two components of the first factor. The result is a tree of grade $3$, hence of type $(3)$.

![Two blue connections ab and cd, multiplied by the orange connection bc, form the path abcd: one component of the second factor joins two components of the first](An%20edge%20joining%20two%20components.svg)

*Figure 4. The vertex names in all three panels refer to the same set $\{a,b,c,d\}$. The product retains all three connections. In this arrangement, the connection in the second factor intersects both components of the first, so a partial matching of components does not describe it.*

The second-kind algebra gives a different expansion:

$$
(1^2)*(1)=(1^3)+2(2,1)
$$

The type $(3)$ does not occur in it. Thus equality between the toponome of an ordinary product and the product of the toponomes is not a general rule. Moreover, the union of particular edge sets may contain a cycle, in which case the corresponding product of forms is zero.

On disjoint vertex sets, ordinary multiplication of forms keeps all components separate. For the chosen exponential expansions, this means that disjoint graph union concatenates the lists of forest parts. In the [[From Polyforms to Partitions#Partitions and polynomials in several variables|polynomial notation for types]], this corresponds to ordinary multiplication of monomials. The nonempty matchings in $*$ arise only after the additional gluing operation is introduced.

## Checks and connections

The general correspondence was proved using the multiplication rule for boundaries sharing one vertex. The simple examples, the seven gluings in Figure 3, and the example in Figure 4 were checked independently by expanding exterior products of differences of basis vertices. For all seven gluings, acyclicity, types, and the number of components on the fixed set of eight vertices were also checked. These calculations verify the examples and figures; the general statement rests on the proof above.

The construction uses definitions and results from published PMG notes:

- [[Core specification#Products of simplex boundaries|Products of simplex boundaries]]  -  rules for disjoint blocks and blocks sharing one vertex.
- [[From Polyforms to Partitions]]  -  positive types, singleton blocks, and the toponome of a chosen representation.
- [[The Second-Kind Algebra on Partitions]]  -  partial matchings and product coefficients; that note also gives the correspondence with the standard algebra of symmetric functions.
- [[Graph Colorings and Partition Products]]  -  realization of the same product through color classes.
- [[Toponomes and Structural Identities]]  -  limitations on representation-independent reduction.

The sum of partial gluings is introduced here as a specific model of type multiplication within PMG. It is not identified with ordinary multiplication of polyforms.
