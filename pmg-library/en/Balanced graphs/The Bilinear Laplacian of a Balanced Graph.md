---
title: The Bilinear Laplacian of a Balanced Graph
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: balanced-graph-bilinear-laplacian
lang: en
description: The canonical centered Laplacian, arc and vertex representations, and multiplication of boundaries involving arbitrary affine points.
order: 2
source_revision: 3
---

[[Balanced Graphs and Spanning-Tree Potentials]] establishes that a balanced Laplacian has zero row and column sums. It can therefore be represented by bilinear forms whose arguments are affine vectors. Here we choose a canonical centered representation, compare arc and vertex expansions, and verify multiplication rules involving auxiliary points, particularly the centroid.

The arc representation retains each coupling and its weight. Grouping by vertices reduces the number of forms. Both use the same bilinear algebra; neither requires first splitting the Laplacian into symmetric and skew-symmetric parts.

## Conventions and the contribution of one arc

Let $a_1,\ldots,a_n$ be formal basis vertices, $n\ge2$, and let $W=\ker\varepsilon$ be the affine-vector space. A point has affine weight $1$, and a vector has weight $0$. Forms $[X,Y]$ are bilinear in their arguments; symmetry $[X,Y]=[Y,X]$ is not assumed. Definitions appear in [[Basic Objects and Operations of Polyform Algebra#Points and affine vectors|the polyform algebra note]].

The graph has no loops. Arc $i\to j$ has weight $f_{ij}\ge0$, with $f_{ii}=0$. We retain the outgoing-weight convention:

$$
L_{ii}=\sum_j f_{ij},\qquad L_{ij}=-f_{ij}\quad(i\ne j)
$$

The matrix is $\mathbf L$, its scalar entries are $L_{ij}$, and the polyform is $L$. Connectedness is not needed for these algebraic representations.

The contribution of arc $i\to j$ is

$$
f_{ij}[a_i,a_i-a_j]=f_{ij}[a_i,a_i]-f_{ij}[a_i,a_j]
$$

It creates two matrix entries: $f_{ij}$ on the diagonal in row $i$, and $-f_{ij}$ at $(i,j)$. Its first argument is a point and its second an affine vector. Summing gives

$$
L=\sum_{i\ne j}f_{ij}[a_i,a_i-a_j]
=\sum_{i,j}L_{ij}[a_i,a_j]
$$

This holds for every directed graph of the specified kind, without using balance.

## Balance and a common reference point

Let $h$ be any point of unit affine weight in $V$: a graph vertex, the centroid, or another affine combination of vertices.

> [!info] Representation on two affine vectors
> **Theorem.** For a balanced graph,
>
> $$
> \boxed{L=\sum_{i\ne j}f_{ij}[a_i-h,a_i-a_j]}
> \tag{1}
> $$
>
> Both arguments of each term lie in $W$, and the sum is independent of $h$.

> [!note]- Proof of reference-point independence
> **Proof.** By bilinearity, the difference between the original representation and the right side of (1) is
>
> $$
> \left[h,\sum_{i\ne j}f_{ij}(a_i-a_j)\right]
> $$
>
> The coefficient of $a_i$ in the second argument is its outgoing weight minus its incoming weight. Hence
>
> $$
> \sum_{i\ne j}f_{ij}(a_i-a_j)
> =\sum_i(d_i^{\mathrm{out}}-d_i^{\mathrm{in}})a_i=0
> $$
>
> The correction vanishes. Differences of points have affine weight $0$, so both arguments belong to $W$. $\square$

For an individual arc, replacing $[a_i,a_i-a_j]$ by $[a_i-h,a_i-a_j]$ generally changes the form. Balance cancels the corrections only in the full sum. A centered term is labelled by its original arc and weight, but is not the Laplacian of that arc alone.

This distinction matters: the matrix of any form on two affine vectors has zero row and column sums, whereas a single directed arc is unbalanced. A centered term may also have positive off-diagonal entries. Nonnegative original weights are checked on the full matrix through $L_{ij}\le0$ for $i\ne j$.

## The canonical centered representation

Choose the centroid of the specified vertex set and write $x_i$ for the centered vectors:

$$
h=\frac1n\sum_i a_i,\qquad x_i=a_i-h
$$

Then

$$
\sum_i x_i=0,\qquad x_i-x_j=a_i-a_j
$$

The centroid treats all vertices equally without selecting one. Since the original $a_i$ are linearly independent and $n\ge2$, every $x_i$ is nonzero. They span $W$ but are linearly dependent.

> [!info] Canonical centering
> **Definition.** The canonical centered representation of the Laplacian relative to the specified vertex set is
>
> $$
> \boxed{L=\sum_{i,j}L_{ij}[x_i,x_j]}
> \tag{2}
> $$
>
> Here $h$ is the centroid and $L_{ij}$ are the entries of the original Laplacian matrix.

Equation (2) follows from the [[Balanced Graphs and Spanning-Tree Potentials#Balance and forms on boundaries|arbitrary-reference representation]]: zero row and column sums cancel all correction terms. Arc weights are read directly from off-diagonal coefficients, $f_{ij}=-L_{ij}$.

### Why the coefficients need a normalization condition

Because $\sum_i x_i=0$, an arbitrary expression $L=\sum C_{ij}[x_i,x_j]$ does not have unique coefficients. Adding the same number to every coefficient of one row changes the form by a multiple of $[x_i,\sum_j x_j]=0$. Columns can be changed similarly.

> [!info] Unique coefficients with zero sums
> **Theorem.** Exactly one coefficient matrix $\mathbf C$ representing $L$ in the forms $[x_i,x_j]$ has zero row and column sums. It is the original Laplacian $\mathbf L$.

> [!note]- Proof
> **Proof.** The coordinate columns of $x_i$ in the original basis form the matrix
>
> $$
> \mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T},\qquad
> \mathbf J^{\mathsf T}=\mathbf J
> $$
>
> Thus the coefficient matrix of $\sum C_{ij}[x_i,x_j]$ in the original vertices is $\mathbf J\mathbf C\mathbf J$. The form equals $L$ exactly when
>
> $$
> \mathbf J\mathbf C\mathbf J=\mathbf L
> $$
>
> If $\mathbf C\mathbf1=0$ and $\mathbf1^{\mathsf T}\mathbf C=0$, then $\mathbf J\mathbf C\mathbf J=\mathbf C$, hence $\mathbf C=\mathbf L$. Conversely, a balanced Laplacian has both sums zero, so $\mathbf C=\mathbf L$ satisfies the requirement. $\square$

Canonical here means a consistent reference point and normalized coefficients for a fixed vertex set. It neither makes the dependent vectors $x_i$ a basis nor selects a directed-cycle decomposition.

## A separate term for every arc

For the centroid, (1) becomes

$$
\boxed{L=\sum_{i\ne j}f_{ij}[x_i,x_i-x_j]}
\tag{3}
$$

This also follows directly from (2) by substituting $L_{ii}=\sum_j f_{ij}$. Every positive arc contributes a term with its original weight $f_{ij}$. Both arguments are nonzero: $x_i\ne0$ and $x_i-x_j=a_i-a_j\ne0$. Centering therefore removes no positive arc from the list of terms.

The distinction between the whole and its terms remains: each term is a form on two vectors, and their sum recovers the graph. Individual terms need not represent subgraphs with nonnegative weights.

### Two opposite arcs

If $f_{ij}=f_{ji}=f$, the corresponding terms combine into a quadratic form:

$$
f[x_i,x_i-x_j]+f[x_j,x_j-x_i]
=f[x_i-x_j]^2=f[(a_i a_j)]^2
$$

The first equality is a bilinear identity: the sum equals $f[x_i-x_j,x_i-x_j]$. It holds for any common reference point $h$.

Consequently, a symmetric graph recovers the familiar representation

$$
L=\sum_{i<j}f_{ij}[(a_i a_j)]^2
$$

One undirected coupling combines two directed terms of equal weight. The new representation agrees with the quadratic representation of 2-balanced graphs.

## Grouping by vertices

Return to an arbitrary reference point $h$. For each vertex, define

$$
v_i=\sum_j f_{ij}(a_i-a_j)=\sum_j L_{ij}a_j
$$

This is the weighted sum of source-minus-recipient differences for the outgoing arcs. Each $v_i$ belongs to $W$, and balance gives $\sum_i v_i=0$. Grouping the arc terms gives

$$
\boxed{L=\sum_i[a_i-h,v_i]}
\tag{4}
$$

There are at most $n$ forms, rather than one per arc. Several outgoing couplings enter one argument $v_i$. Choosing the centroid treats all vertices equally.

### A reference vertex and the reduced Laplacian

Choose $h=a_r$. The term $[a_r-a_r,v_r]$ in (4) vanishes, leaving at most $n-1$ forms. This shortens the representation without deleting the vertex or its arcs.

In the double sum with the same reference point, terms with $i=r$ or $j=r$ vanish:

$$
L=\sum_{i\ne r}\sum_{j\ne r}L_{ij}[a_i-a_r,a_j-a_r]
$$

The vectors $a_i-a_r$, $i\ne r$, form a basis of $W$. Its coefficient matrix is the reduced Laplacian $\mathbf L_{\widehat r,\widehat r}$. Vertex $a_r$ remains in the differences; the omitted row and column are recovered from zero sums:

$$
L_{ir}=-\sum_{j\ne r}L_{ij}\quad(i\ne r),\qquad
L_{rj}=-\sum_{i\ne r}L_{ij}\quad(j\ne r)
$$

$$
L_{rr}=\sum_{i\ne r}\sum_{j\ne r}L_{ij}
$$

**Remark.** For a connected balanced graph with nonnegative weights, $n-1$ is the smallest number of grade-one terms $[u,v]$. The [[Balanced Graphs and Spanning-Tree Potentials#A balance criterion using spanning-tree potentials|balance criterion]] gives $\operatorname{rank}\mathbf L=n-1$, while one nonzero term has matrix rank $1$. Fewer than $n-1$ terms cannot attain the required rank. This concerns term count, not overall computational complexity.

| Representation | Number of terms | Directly visible data |
| --- | --- | --- |
| By arcs, using the centroid | Number of positive arcs | Weight and direction of each original coupling |
| By vertices, using the centroid | At most $n$ | Each vertex's outgoing-coupling vector $v_i$ |
| By vertices, with $h=a_r$ | At most $n-1$ | A shorter sum; reference-vertex couplings remain in the full form |

## One directed 3-cycle in different representations

For the unit cycle $a\to b\to c\to a$, the matrix and original polyform are

$$
\mathbf L=
\begin{pmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{pmatrix},\qquad
L=[a,a-b]+[b,b-c]+[c,c-a]
$$

Choose $h=(a+b+c)/3$ and set $x_a=a-h$, $x_b=b-h$, $x_c=c-h$. Then $x_a+x_b+x_c=0$ and

$$
L=[x_a,x_a-x_b]+[x_b,x_b-x_c]+[x_c,x_c-x_a]
$$

![[A Directed 3-Cycle and Centroid Vectors.svg]]

*Left: the arcs of the unit directed 3-cycle. Right: the affine vectors $x_a=a-h$, $x_b=b-h$, $x_c=c-h$ from the centroid. The right-hand arrows represent vectors, not additional graph arcs. The figure shows affine relations and specifies no resistance lengths.*

Expanding the arguments gives the canonical expression with the original coefficient matrix:

$$
L=[x_a]^2+[x_b]^2+[x_c]^2-[x_a,x_b]-[x_b,x_c]-[x_c,x_a]
$$

Each vertex has one outgoing arc, so the arc and vertex expansions contain the same three terms.

### Choosing vertex $c$ as the reference point

Set $h=c$, $u=a-c$, $v=b-c$. The outgoing-coupling vectors are $v_a=u-v$, $v_b=v$, $v_c=-u$. Equation (4) gives

$$
L=[u,u-v]+[v,v]=[u]^2-[u,v]+[v]^2
$$

The term with first argument $c-c$ vanishes. Expanding the remaining two forms nevertheless gives

$$
L=[a,a]+[b,b]+[c,c]-[a,b]-[b,c]-[c,a]
$$

All three arcs remain, including $c\to a$, represented by coefficient $-1$ at $[c,a]$. The coefficient matrix in basis $u,v$ is

$$
\mathbf L_{\widehat c,\widehat c}
=\begin{pmatrix}1&-1\\0&1\end{pmatrix}
$$

### Comparison with the symmetric triangle

Add the reverse unit 3-cycle. Combining opposite arcs gives

$$
L_{\mathrm{sym}}=[(ab)]^2+[(bc)]^2+[(ca)]^2
$$

In the same vectors $u=a-c$, $v=b-c$, this becomes

$$
L_{\mathrm{sym}}=[v-u]^2+[v]^2+[u]^2
=2[u]^2+2[v]^2-\{u,v\}
$$

Here $\{u,v\}=[u,v]+[v,u]$. The three quadratic forms retain the correspondence with undirected couplings, while the expanded expression uses the chosen basis. Both describe one Laplacian.

## Boundaries involving an arbitrary point

The centered representation uses vectors $(ha_i)=a_i-h$, where $h$ is usually not a basis vertex. We must therefore check boundary multiplication rules for such arguments.

The [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|introductory note]] states the rules for basis vertices. The basic identity remains valid for any points of unit affine weight, even affinely dependent ones.

> [!info] A boundary through differences of arbitrary points
> **Lemma.** If $\varepsilon(h)=\varepsilon(b_i)=1$, then
>
> $$
> (hb_1\ldots b_k)=(b_1-h)\cdots(b_k-h)
> $$
>
> Linear independence of the points is not required.

> [!note]- Proof
> **Proof.** Call the right side $B$. Each factor is an affine vector, so $\partial B=0$. Multiplying by $h$ kills all expansion terms containing a repeated $h$, hence
>
> $$
> hB=[hb_1\ldots b_k]
> $$
>
> Applying the boundary product rule and $\partial h=1$ gives
>
> $$
> (hb_1\ldots b_k)=\partial(hB)
> =(\partial h)B-h\partial B=B
> $$
>
> This proves the identity, including the case where both sides vanish. $\square$

### Merging at a shared point

If the common point $h$ is listed first in both boundaries, the lemma immediately gives

$$
(hb_1\ldots b_k)(hc_1\ldots c_m)
=(hb_1\ldots b_kc_1\ldots c_m)
$$

Other positions require the permutation signs. In particular, for arbitrary points $a,h,b$,

$$
\boxed{(ah)(hb)=(h-a)(b-h)=(ahb)}
$$

The sign is positive. Direct expansion gives $[hb]-[ab]+[ah]=\partial[ahb]$.

For the triangle centroid $h=(a+b+c)/3$, substitution also verifies

$$
(ah)(hb)=(ahb)=-\frac13(abc)
$$

The final equality uses multilinearity of the boundary and the exchange of $b,c$. No metric properties of the triangle are needed.

### Vanishing and additional dependencies

Two shared points still force a product of boundaries to vanish. Listing one common point first produces the same difference to the second common point in both factors. Its exterior self-product is zero.

Arbitrary affine points may, however, satisfy additional linear dependencies. Absence of repeated points alone does not ensure a nonzero product.

For the same triangle centroid, for example,

$$
(ha)+(hb)+(hc)=0,\qquad
(ha)(hb)(hc)=(habc)=0
$$

The three segments from $h$ form a star, but their vectors are dependent. The introductory forest criterion for a nonzero product of edge vectors applies to the original independent basis vertices. Adding the centroid as an auxiliary point does not make it a new independent vertex.

The merging and vanishing identities therefore survive. Deciding whether a product is nonzero requires all linear dependencies, not just repeated letters in its expression.

## Products of bilinear forms on boundaries

In [[Basic Objects and Operations of Polyform Algebra#Polyforms and the product of forms|polyform algebra]], multiplication is defined by

$$
[X,Y][U,V]=[XU,YV]
$$

If $X,Y$ are boundaries of grade $k$ and $U,V$ of grade $m$, then $XU,YV\in\Lambda^{k+m}W$. The result remains a bilinear form on boundaries. It vanishes if either exterior argument vanishes.

For arbitrary points $a,b,c,h$, for example, merging gives

$$
[(ah),(bh)][(hb),(hc)]=[(ahb),(bhc)]
$$

Both resulting arguments have grade $2$. They can be expanded in the original vertices to check any additional dependencies.

> [!info] The square of one term vanishes
> **Lemma.** For affine vectors $u,v\in W$, the form $H=[u,v]$ satisfies
>
> $$
> H^2=[u\wedge u,v\wedge v]=0
> $$

The wedge signs in self-products distinguish them from quadratic norms. The lemma follows from alternation of the exterior product. It applies to a single grade-one form; an arbitrary sum may have a nonzero square.

Every individual term of the arc and grouped representations has this form. Their products remain in one bilinear algebra, with grades bounded by $\dim W=n-1$. Factorization of the exponential, its grade components, and their combinatorial meaning are developed in [[The Laplacian Exponential of a Balanced Graph]]. The symmetric construction appears in [[Laplacian Exponential]].

## Connections to other notes

- [[Balanced Graphs and Spanning-Tree Potentials]]: balance, its matrix criterion, and the common spanning-tree coefficient.
- [[The Laplacian Exponential of a Balanced Graph]]: factorization, minors, directed forests, and tree contributions for a chosen reference point.
- [[Basic Objects and Operations of Polyform Algebra]]: affine vectors, the boundary operator, forms, and multiplication.
- [[Core specification]]: conventions for arguments, grades, and exterior self-products.
- [[Laplacian Exponential]]: the polyform exponential and spanning-tree coefficient in the symmetric case.
