---
title: Partition Forms and the Tetrahedron Identity
date: 2026-10-18
updated: 2026-10-18
revision: 3
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: partition-forms-and-tetrahedron-identity
lang: en
description: "Forms associated with set partitions, the structural tetrahedron identity, and its proof. Area equalities as consequences of metric evaluation."
order: 1
---

A partition of a vertex set can be assigned a product of the forms of its block boundaries. The forms associated with different partitions may satisfy linear dependencies. Such dependencies are called structural identities. This note studies the tetrahedron identity: the sum of three forms built from pairs of opposite edges equals the sum of four forms of triangle boundaries.

The identity itself is an equality of forms and requires no choice of metric. Once an inner product is specified, it yields a numerical equality of norms and, in Euclidean geometry, an equality of sums of squared areas.

We use the definitions from [[Basic Objects and Operations of Polyform Algebra]]. The geometric part requires the [[Metric of Higher-Grade Objects|metric on exterior powers]]. The notation follows the [[Core specification|core specification]] and [[PMG terminology|PMG terminology]].

Juxtaposition of exterior elements denotes their exterior product.

## From a partition to a form

Let $A=\{a_1,\ldots,a_n\}$ be a set of basis vertices of the formal space $V$. Each vertex satisfies $\partial a_i=1$, and the space of affine vectors is $W=\ker\varepsilon$.

A partition

$$
\pi=B_1|\cdots|B_q
$$

consists of nonempty, pairwise disjoint blocks whose union is $A$. The vertical bar separates blocks; for example, $ab|c|d$ denotes the partition $\{a,b\}|\{c\}|\{d\}$.

Choose an ordering of the vertices within each block. If $B=\{b_1,\ldots,b_s\}$, write $(B)$ for the boundary $(b_1\ldots b_s)$. Its grade is $s-1$; for a singleton block, $(b)=1$.

> [!info] The form of a partition
> **Definition.** To a partition $\pi=B_1|\cdots|B_q$, assign the exterior element and its quadratic form:
>
> $$
> X_\pi=(B_1)\cdots(B_q),
> \qquad
> q_\pi=[X_\pi]^2
> $$
>
> By the rule for multiplying forms,
>
> $$
> q_\pi=[(B_1)]^2\cdots[(B_q)]^2
> $$

Changing the vertex order within a block changes $X_\pi$ only by a sign. Permuting the blocks likewise introduces only an orientation sign. Since $[-X]^2=[X]^2$, the form $q_\pi$ is independent of these choices.

The product of the boundaries of disjoint blocks of basis vertices is nonzero. Its grade, and that of the associated form, is

$$
\operatorname{gr}q_\pi=\sum_{i=1}^q(|B_i|-1)=n-q
$$

A singleton block contributes the factor $1$ to the exterior element and the unit form $e=[1,1]$ to the product of forms. Such blocks may therefore be omitted from the product while remaining part of the partition.

| Partition of four vertices | Partition form | Grade |
|---|---|---:|
| $a\mid b\mid c\mid d$ | $e$ | 0 |
| $ab\mid c\mid d$ | $[(ab)]^2$ | 1 |
| $abc\mid d$ | $[(abc)]^2$ | 2 |
| $ab\mid cd$ | $[(ab)(cd)]^2$ | 2 |
| $abcd$ | $[(abcd)]^2$ | 3 |

Partition forms occur, in particular, in the [[Laplacian Exponential#Grade components and spanning forests|forest expansion of the Laplacian exponential]]: the components of a forest define the blocks, and the product of its edge forms equals the form of that partition. Several different forests may give the same form.

## Structural identities

> [!info] Structural identity
> **Definition.** A structural identity is an equality
>
> $$
> \sum_\pi c_\pi q_\pi=0
> $$
>
> between forms of partitions of a fixed set of basis vertices that holds in the formal algebra of PMG. The coefficients $c_\pi$ are real numbers; for a nontrivial identity, they are not all zero.

It suffices to consider relations within one grade: equality of polyforms holds separately in each grade. Such relations arise from the properties of boundaries and the bilinearity of forms.

The partition $\pi$, the exterior element $X_\pi$, the form $q_\pi$, and its eventual numerical evaluation must be distinguished. A structural identity is established between forms. A numerical equality that happens to hold in one chosen metric does not by itself prove such an identity.

## The tetrahedron identity

Consider four distinct basis vertices $a,b,c,d$. They admit three partitions into two pairs and four partitions into a triple and a singleton. All seven forms have grade $2$.

> [!info] The tetrahedron identity
> **Theorem.** The following structural identity holds:
>
> $$
> \boxed{
> \begin{aligned}
> &[(ab)(cd)]^2+[(ac)(bd)]^2+[(ad)(bc)]^2=\\
> &\qquad=[(abc)]^2+[(abd)]^2+[(acd)]^2+[(bcd)]^2
> \end{aligned}
> }
> \tag{1}
> $$

The quantities being added here are forms. Both sides represent the same polyform of the second grade; no lengths or areas have been assigned in (1). The name refers to the geometric interpretation of the four vertices.

### A lemma on a zero sum

**Lemma.** Suppose that the exterior elements $X_1,X_2,X_3,X_4$ have the same grade and satisfy

$$
X_1+X_2+X_3+X_4=0
$$

Then

$$
[X_1+X_2]^2+[X_1+X_3]^2+[X_1+X_4]^2
=
\sum_{i=1}^4[X_i]^2
\tag{2}
$$

> [!note]- Proof of the lemma
> **Proof.** Use the polar form $\{X,Y\}=[X,Y]+[Y,X]$ without a factor of $1/2$. Expanding the three terms gives
>
> $$
> \begin{aligned}
> \sum_{j=2}^4[X_1+X_j]^2
> &=3[X_1]^2+\sum_{j=2}^4[X_j]^2+
> \left\{X_1,\sum_{j=2}^4X_j\right\}\\
> &=3[X_1]^2+\sum_{j=2}^4[X_j]^2-2[X_1]^2\\
> &=\sum_{i=1}^4[X_i]^2
> \end{aligned}
> $$
>
> The second line uses $\sum_{j=2}^4X_j=-X_1$. All these operations concern forms and require no inner product. $\square$

### Proof of the identity

> [!note]- Proof of the theorem
> **Proof.** Introduce consistently oriented face boundaries:
>
> $$
> X_a=(bcd),\qquad X_b=-(acd),\qquad
> X_c=(abd),\qquad X_d=-(abc)
> $$
>
> The boundary identity $\partial^2[abcd]=0$ gives
>
> $$
> X_a+X_b+X_c+X_d=0
> $$
>
> The pairwise sums involving $X_a$ are
>
> $$
> \begin{aligned}
> X_a+X_b&=-(ab)(cd)\\
> X_a+X_c&=(ac)(bd)\\
> X_a+X_d&=-(ad)(bc)
> \end{aligned}
> $$
>
> These equalities follow by expanding the boundaries. For example,
>
> $$
> \begin{aligned}
> (bcd)-(acd)
> &=[bc]-[bd]-[ac]+[ad]\\
> &=-(b-a)(d-c)
> \end{aligned}
> $$
>
> Apply lemma (2) to $X_a,X_b,X_c,X_d$. The orientation signs disappear upon passing to quadratic forms, giving (1). $\square$

The proof remains valid when arbitrary affine points of unit weight are substituted for the basis vertices, including degenerate configurations. The initial definition of a partition form used independent basis vertices; the identity just proved admits these substitutions.

## From forms to numbers

Now choose a positive definite inner product on the space of affine vectors $W$ and extend it to the exterior powers. The [[Metric of Higher-Grade Objects#Numerical evaluation of forms|metric evaluation]] rule

$$
[X,Y]\longmapsto X\cdot Y
$$

is linear. In particular, the form $[X]^2$ receives the numerical value $X^2=X\cdot X$, called the norm, or quadratic norm, in PMG.

Applying this evaluation to both sides of (1) gives

$$
\begin{aligned}
&\bigl((ab)(cd)\bigr)^2+
\bigl((ac)(bd)\bigr)^2+
\bigl((ad)(bc)\bigr)^2=\\
&\qquad=(abc)^2+(abd)^2+(acd)^2+(bcd)^2
\end{aligned}
\tag{3}
$$

**In (3), the quantities being added are numbers.** Their values depend on the chosen metric. Equality of these sums follows from the structural identity (1) and the linearity of metric evaluation.

For two vectors, the product of their forms is evaluated using the Gram determinant:

$$
\bigl((ab)(cd)\bigr)^2
=(ab)^2(cd)^2-\bigl((ab)\cdot(cd)\bigr)^2
$$

It therefore cannot be replaced by the product of the two numerical norms $(ab)^2(cd)^2$.

### Areas of triangles and parallelograms

Let $S_{abc}$ denote the ordinary Euclidean area of triangle $abc$, and let $S_{ab,cd}$ denote the area of the parallelogram spanned by the vectors $(ab)$ and $(cd)$. These vectors may be translated to a common origin.

The relation between norms and areas gives

$$
(abc)^2=4S_{abc}^2,\qquad
\bigl((ab)(cd)\bigr)^2=S_{ab,cd}^2
$$

The factor $4$ arises because a triangle has half the area of the parallelogram spanned by the two vectors from one vertex.

**Corollary.** In the chosen Euclidean metric,

$$
4\left(S_{abc}^2+S_{abd}^2+S_{acd}^2+S_{bcd}^2\right)
=
S_{ab,cd}^2+S_{ac,bd}^2+S_{ad,bc}^2
\tag{4}
$$

This numerical equality of areas is a metric consequence of the tetrahedron identity.

### The circumscribed parallelepiped

A nondegenerate tetrahedron can be inscribed in a parallelepiped so that its vertices occupy four alternating vertices of the parallelepiped. The edges of the tetrahedron are then diagonals of the parallelepiped's faces.

![[Tetrahedron in a Parallelepiped.png]]

*The tetrahedron $abcd$ is drawn with thick lines. The points $a_1,b_1,c_1,d_1$ complete its vertices to a parallelepiped. Each pair of opposite edges of the tetrahedron lies in two parallel faces of the parallelepiped.*

Let $F_1,F_2,F_3$ be the areas of three pairwise nonparallel faces of the parallelepiped.

> [!info] An equality of areas
> **Corollary.** The sum of the squared areas of the four faces of a tetrahedron equals the sum of the squared areas of three pairwise nonparallel faces of its circumscribed parallelepiped:
>
> $$
> S_{abc}^2+S_{abd}^2+S_{acd}^2+S_{bcd}^2
> =
> F_1^2+F_2^2+F_3^2
> \tag{5}
> $$

> [!note]- Construction of the parallelepiped and proof
> **Proof.** Set $u=b-a$, $v=c-a$, $w=d-a$, and define
>
> $$
> p=\frac{u+w-v}{2},\qquad
> q=\frac{u+v-w}{2},\qquad
> r=\frac{v+w-u}{2}
> $$
>
> Then
>
> $$
> b=a+p+q,\qquad c=a+q+r,\qquad d=a+p+r
> $$
>
> Thus the parallelepiped with vertex $a$ and edge vectors $p,q,r$ contains all four vertices of the tetrahedron. Nondegeneracy of the tetrahedron ensures that these three vectors are independent. In the figure, $p=(ad_1)$, $q=(ac_1)$, and $r=(aa_1)$.
>
> For the opposite edges, we obtain
>
> $$
> \begin{aligned}
> (ab)(cd)&=(p+q)(p-q)=-2pq\\
> (ac)(bd)&=(q+r)(r-q)=2qr\\
> (ad)(bc)&=(p+r)(r-p)=2pr
> \end{aligned}
> $$
>
> If $F_1,F_2,F_3$ correspond to the pairs $p,q$, $q,r$, and $p,r$, respectively, then
>
> $$
> S_{ab,cd}^2=4F_1^2,\qquad
> S_{ac,bd}^2=4F_2^2,\qquad
> S_{ad,bc}^2=4F_3^2
> $$
>
> Substitution into (4) and division by $4$ give (5). $\square$

## A numerical example

Choose orthonormal affine vectors $u,v,w$ and points

$$
b=a+u,\qquad c=a+v,\qquad d=a+w
$$

In a Euclidean realization, this is the tetrahedron with coordinates $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$. The exterior elements $uv$, $uw$, and $vw$ form an orthonormal basis of the second exterior power.

Compute all seven norms directly from the following expansions.

| Exterior element $X$ | Expansion | Norm $X^2$ |
|---|---|---:|
| $(abc)$ | $uv$ | 1 |
| $(abd)$ | $uw$ | 1 |
| $(acd)$ | $vw$ | 1 |
| $(bcd)$ | $uv-uw+vw$ | 3 |
| $(ab)(cd)$ | $uw-uv$ | 2 |
| $(ac)(bd)$ | $vw+uv$ | 2 |
| $(ad)(bc)$ | $uw-vw$ | 2 |

The sum of the four norms of triangle boundaries and the sum of the three norms of products of opposite edge vectors both equal $6$.

The three faces incident to vertex $a$ each have area $1/2$, and the fourth face has area $\sqrt3/2$. Hence

$$
S_{abc}^2+S_{abd}^2+S_{acd}^2+S_{bcd}^2
=
\frac14+\frac14+\frac14+\frac34=\frac32
$$

The three areas $S_{ab,cd}$, $S_{ac,bd}$, and $S_{ad,bc}$ all equal $\sqrt2$. Accordingly, (4) becomes the numerical equality $4\cdot(3/2)=2+2+2$.

This calculation uses the coordinates directly. It illustrates the metric consequence; the general structural identity was proved above without choosing a metric.

## Coefficients and symmetry

The left-hand side of (1) contains three forms with unit coefficients, whereas the right-hand side contains four. Thus one polyform has two representations with different coefficient sums: $3$ and $4$.

**Corollary.** The coefficient sum in an expansion into partition forms depends on the chosen representation. It is not determined by the polyform alone.

Metric evaluation behaves differently: it is linear on the space of forms itself and therefore assigns the same value to equal polyforms. In the numerical example, both expressions evaluate to $6$, despite having different coefficient sums.

Both sides of (1) are preserved by every permutation of the four vertices. A permutation merely rearranges the terms; any orientation signs disappear in the quadratic forms. The identity therefore also provides an example of equality between symmetric polyforms. Their general properties are treated separately.

For the continuation of the structural series, the relevant mechanism is how the equality is obtained: a zero sum of boundaries yields an equality of quadratic forms. Extending such identities to larger vertex sets and obtaining new relations by multiplying forms are treated in [[Constructing Structural Identities]].

## Connection with the literature

In Lemma 2.3 of *Boundary Partitions in Trees and Dimers*, R. Kenyon and D. Wilson give a seven-term relation between partitions of four elements: the sum of the partitions $1|234$, $2|134$, $3|124$, and $4|123$ is equivalent to the sum of $12|34$, $13|24$, and $14|23$ under their combinatorial pairing.

Assigning the forms $q_\pi$ to these partitions gives the same pattern of terms and coefficients as in (1). The proof presented here establishes the equality directly in the algebra of PMG.

R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325-1364. [arXiv:math/0608422, version 4, Lemma 2.3](https://arxiv.org/abs/math/0608422v4). [DOI: 10.1090/S0002-9947-2010-04964-5](https://doi.org/10.1090/S0002-9947-2010-04964-5).
