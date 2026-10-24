---
title: The Circulation Form
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: circulation-form
lang: en
description: 'Circulation as an independent skew-symmetric PMG form: orientation, triangular decompositions, pure circulation polyforms, and their products.'
order: 4
source_revision: 1
---

The Laplacian of a directed 3-cycle has a skew-symmetric part that changes sign when every arc is reversed. It leads to an independent PMG object, the **circulation form**. Its definition needs only bilinear forms on the boundary space, without a graph, positive weights, or a metric.

[[The Bilinear Laplacian of a Balanced Graph]] and [[The Laplacian Exponential of a Balanced Graph]] give the general algebraic representation of the Laplacian and its exponential. Here we isolate circulation, establish its basic properties, and define polyforms composed solely of such forms. Their detailed study remains a separate task.

## How circulation appears in a directed 3-cycle

Let $a,b,c$ be the vertices of the unit cycle $a\to b\to c\to a$. Under the outgoing Laplacian convention,

$$
L_{abc}=[a,a-b]+[b,b-c]+[c,c-a]
$$

The reverse cycle has Laplacian $L_{acb}=L_{abc}^{\mathsf T}$, where $[X,Y]^{\mathsf T}=[Y,X]$. Their sum gives the symmetric triangle:

$$
L_{abc}+L_{acb}=[(ab)]^2+[(bc)]^2+[(ca)]^2
$$

Their difference isolates the orientation. Denote it by $w(abc)$:

$$
\begin{aligned}
w(abc)&=L_{acb}-L_{abc}\\
&=[a,b]-[b,a]+[b,c]-[c,b]+[c,a]-[a,c]
\end{aligned}
$$

Expansion gives an expression using two vectors with a common origin:

$$
\boxed{w(abc)=[b-a,c-a]-[c-a,b-a]}
\tag{1}
$$

![[The Circulation Form of a Directed 3-Cycle.svg]]

*Left and center: opposite unit directed cycles. Their Laplacian difference $L_{acb}-L_{abc}$ equals $w(abc)$. Right: the same points define $u=b-a$ and $v=c-a$, giving $[u,v]-[v,u]$. The figure specifies directions and arguments, without a metric.*

The full Laplacian of the original cycle is therefore

$$
\boxed{L_{abc}=\frac12\left([(ab)]^2+[(bc)]^2+[(ca)]^2-w(abc)\right)}
\tag{2}
$$

With this normalization, its skew-symmetric part is $-w(abc)/2$. The factor $1/2$ and sign belong to the Laplacian decomposition, not to the definition of circulation.

## Definition and geometric properties

Work over $\mathbb R$. Let $V$ be the formal vertex space, $\varepsilon$ its affine-weight functional, and $W=\ker\varepsilon$ the vector space of grade-one boundaries. A point has $\varepsilon(a)=1$, while $\varepsilon(b-a)=0$.

> [!info] A skew-symmetric form on two vectors
> **Definition.** For $u,v\in W$, set
>
> $$
> \boxed{\omega(u,v)=[u,v]-[v,u]}
> \tag{3}
> $$
>
> For three affine points, define the **triangular circulation form** by $w(abc)=\omega(b-a,c-a)$.

The form $\omega$ is bilinear in $u,v$ and satisfies

$$
\omega(v,u)=-\omega(u,v),\qquad
\omega(u,u)=0,\qquad
\omega(u,v)^{\mathsf T}=-\omega(u,v)
$$

These are two manifestations of skew-symmetry: exchanging the vectors changes the sign, and transposing the resulting form also changes the sign. Since both arguments are vectors, $\omega(u,v)$ has **PMG grade one**, or bigrade $(1,1)$.

“Commutator” may describe the difference in (3), but this is not a commutator for polyform multiplication, which is commutative. “Circulation form” emphasizes the object's geometric meaning.

### Orientation and the choice of initial vertex

**Proposition.** Triangular circulation is invariant under cyclic shifts of its vertices and changes sign under orientation reversal:

$$
w(abc)=w(bca)=w(cab),\qquad w(acb)=-w(abc)
$$

> [!note]- Proof
> **Proof.** In the expanded expression for $w(abc)$, a cyclic permutation merely permutes the three pairs of terms. Reversing the order changes every pair's sign. $\square$

A common translation also preserves the form: $w(a+t,b+t,c+t)=w(abc)$ for $t\in W$, since point differences are unchanged. Writing vectors from $a$ therefore gives it no distinguished geometric role.

For arbitrary affine points, $w(abc)=0$ exactly when $b-a$ and $c-a$ are linearly dependent. This includes repeated points and affine collinearity. For independent $u,v$, the forms $[u,v]$ and $[v,u]$ are distinct basis tensors, so their difference is nonzero.

### Relation to the triangle boundary

With $u=b-a$, $v=c-a$, the boundary is $(abc)=uv$. The rule

$$
uv\longmapsto\omega(u,v)
$$

defines a linear bijection from $\Lambda^2W$ to the skew-symmetric grade-one forms on $W$. Indeed, for a basis $b_1,\ldots,b_d$, the basis elements $b_i b_j$, $i<j$, correspond to independent forms $[b_i,b_j]-[b_j,b_i]$.

Thus $w(abc)$ retains the oriented-boundary information in $(abc)$ as a skew-symmetric bilinear form. Their object types differ: $(abc)$ is an exterior boundary of grade two, whereas $w(abc)$ is a form of grade one. This linear correspondence does not identify their multiplications.

The distinction between ordinary exterior forms and skew-symmetric double forms is discussed in [1, §5.1]. As explained in [[The Laplacian Exponential of a Balanced Graph#Why these are called double forms|the double-form section]], formal PMG forms can be regarded as double forms on $W^*$ without choosing a metric.

## Circulation around a closed contour

For the ordered contour $a_1\to\cdots\to a_k\to a_1$ and any affine point $h$, set

$$
w(a_1\ldots a_k)=\sum_{i=1}^k\omega(a_i-h,a_{i+1}-h),\qquad a_{k+1}=a_1
\tag{4}
$$

**Proposition.** This sum is independent of $h$.

> [!note]- Proof
> **Proof.** On replacing $h$ by $h+t$, write $x_i=a_i-h$. Bilinearity gives
>
> $$
> \omega(x_i-t,x_{i+1}-t)-\omega(x_i,x_{i+1})
> =\omega(t,x_i-x_{i+1})
> $$
>
> Summing the right sides gives zero because $\sum_i(x_i-x_{i+1})=0$. $\square$

For $k=3$, definition (4) agrees with (1), as seen by taking $h=a_1$. Circulation is invariant under cyclic shifts and reverses sign with the contour. For two points, $w(ab)=0$: the opposite contributions cancel.

Choosing $h=a_1$ immediately triangulates the contour:

$$
\boxed{w(a_1\ldots a_k)=\sum_{i=2}^{k-1}w(a_1a_i a_{i+1})}
\tag{5}
$$

A longer contour therefore introduces no new independent kind of grade-one circulation form. For example,

$$
w(abcd)=w(abc)+w(acd)=w(abd)+w(bcd)
$$

Averaging the two equivalent decompositions treats both diagonals symmetrically:

$$
w(abcd)=\frac12\left(w(abc)+w(acd)+w(abd)+w(bcd)\right)
$$

The equality can also be checked directly: in $w(abc)+w(acd)$, the terms $[a,c]-[c,a]$ and $[c,a]-[a,c]$ cancel, leaving the outer sides.

### Circulation and the full Laplacian

For the unit cycle $a_1\to\cdots\to a_k\to a_1$, the analogue of (2) is

$$
L_{a_1\ldots a_k}
=\frac12\left(\sum_{i=1}^k[(a_i a_{i+1})]^2-w(a_1\ldots a_k)\right)
$$

The forward and reverse Laplacians sum to the quadratic forms of the sides; their difference is $w(a_1\ldots a_k)$.

A circulation decomposition does not give the same decomposition of the full Laplacian. For unit directed cycles, for example,

$$
L_{abc}+L_{acd}=L_{abcd}+[(ac)]^2
$$

Adding the two triangular cycles creates a directed 2-cycle on diagonal $ac$. Its skew-symmetric contribution vanishes, but its quadratic form remains. Positive-cycle decompositions and circulation decompositions therefore address different questions.

For any balanced graph, summing the circulation parts of its cycles gives the skew-symmetric part of $L$. Although the cycle decomposition may be nonunique, the result is always $(L-L^{\mathsf T})/2$, independent of that choice.

## Polyforms made only of circulations

**Definition.** A pure grade-one circulation polyform is an expression

$$
C=\sum_\alpha c_\alpha\,\omega(u_\alpha,v_\alpha),\qquad
u_\alpha,v_\alpha\in W,\quad c_\alpha\in\mathbb R
$$

It satisfies $C^{\mathsf T}=-C$. Its symmetric part is absent, and coefficients have no positivity restriction.

> [!info] Completeness of triangular circulations
> **Proposition.** For independent formal vertices $a_1,\ldots,a_n$, every skew-symmetric grade-one form on their boundary space has the representation
>
> $$
> C=\sum_{1\le i<j\le n-1}c_{ij}\,w(a_n a_i a_j)
> \tag{6}
> $$
>
> For fixed reference vertex $a_n$, the coefficients are unique. The dimension is $\binom{n-1}{2}$.

> [!note]- Proof
> **Proof.** The vectors $b_i=a_i-a_n$, $1\le i\le n-1$, form a basis of $W$. Write $C=\sum_{i,j}C_{ij}[b_i,b_j]$. Skew-symmetry gives $C_{ji}=-C_{ij}$ and $C_{ii}=0$. Thus
>
> $$
> C=\sum_{i<j}C_{ij}\bigl([b_i,b_j]-[b_j,b_i]\bigr)
> =\sum_{i<j}C_{ij}w(a_n a_i a_j)
> $$
>
> Independence of the original basis tensors gives uniqueness and the stated dimension. $\square$

Triangular circulations therefore describe the entire skew-symmetric sector of grade one on $W$. A reference vertex supplies a convenient basis without changing $C$. Representations treating every vertex equally, and criteria for calling them canonical, require a separate study.

### Why this need not be a graph Laplacian

In the original vertex basis, the coefficient matrix of such a polyform satisfies

$$
\mathbf C^{\mathsf T}=-\mathbf C,\qquad
\mathbf C\mathbf1=0,\qquad
\mathbf1^{\mathsf T}\mathbf C=0
$$

Both sums vanish because each argument lies in $W$. For $C=w(abc)$, in the order $a,b,c$,

$$
\mathbf C=
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix}
$$

A graph Laplacian with nonnegative weights has nonpositive off-diagonal entries. Combined with $C_{ji}=-C_{ij}$, this would force every entry to vanish. Thus **a nonzero pure circulation is not the Laplacian of a graph with nonnegative weights**.

Allowing signed weights permits a Laplacian representation: take $f_{ij}=-C_{ij}$ for $i\ne j$. Outgoing and incoming weight sums then vanish, as does the diagonal. Another graph interpretation treats $C_{ij}$ as a signed divergence-free flow. The restriction concerns nonnegative graph Laplacians, not the existence of the PMG form.

### What happens under multiplication

Pure circulations form a vector space. The algebra they generate also contains symmetric forms. For two vectors,

$$
\boxed{\omega(u,v)^2=2[uv]^2}
\tag{7}
$$

> [!note]- Direct verification from the multiplication rule
> **Proof.** Use $[X,Y][U,V]=[XU,YV]$. The squares $[u,v]^2$ and $[v,u]^2$ vanish because of vector self-products. The mixed terms give
>
> $$
> \omega(u,v)^2=-[uv,vu]-[vu,uv]=2[uv]^2
> $$
>
> Here $vu=-uv$. $\square$

In particular, $w(abc)^2=2[(abc)]^2$. A polyform may have no symmetric part initially, while its powers and exponential do. Classification, potentials, and exponentials of these polyforms can be studied independently, without assuming a graph or metric interpretation.

## A possible connection with electrodynamics

Skew-symmetric forms have an independent physical role. In electrodynamics, the electromagnetic field is a differential 2-form $F$, locally expressible as $F=dA$, whose components combine electric and magnetic fields [2, §2.4.2].

This suggests a future comparison with circulation polyforms. So far, the established relation is algebraic: skew-symmetric grade-one forms correspond to exterior bivectors on $W$, equivalently 2-forms on $W^*$. A physical interpretation must specify the space, coefficients, and corresponding operations. In particular, PMG multiplication cannot simply be replaced by the ordinary wedge product of differential forms.

This note introduces circulation as an independent PMG object and proves its basic identities. A connection with a specific electrodynamic model remains a research direction. Skew-symmetric bilinear forms are already studied in double-form theory [1]; the notation and geometric presentation here are not claims that antisymmetrization itself is new.

## Sources and connections

1. M. L. Labbi. [On some algebraic identities and the exterior product of double forms](https://arxiv.org/abs/1112.1346). *Archivum Mathematicum* **49** (2013), 241-271. [DOI: 10.5817/AM2013-4-241](https://doi.org/10.5817/AM2013-4-241). Double-form algebra: §1.1. A skew-symmetric bilinear form as an ordinary 2-form and a double form of bigrade $(1,1)$, the distinction between products, and the Pfaffian: §5.1.
2. D. Tong. [General Relativity, Chapter 2: Introducing Differential Geometry](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S2.html). §2.4.2, *The Electromagnetic Field*: electromagnetic fields as differential 2-forms.

Related library notes:

- [[Basic Objects and Operations of Polyform Algebra]]: formal forms, boundaries, and multiplication.
- [[The Bilinear Laplacian of a Balanced Graph]]: boundary forms and the affine reference point.
- [[The Laplacian Exponential of a Balanced Graph]]: the exterior exponential, double forms, and determinant coefficients.
- [[Balanced Graphs and Spanning-Tree Potentials]]: balanced graphs, cycle decompositions, and weight conditions.
