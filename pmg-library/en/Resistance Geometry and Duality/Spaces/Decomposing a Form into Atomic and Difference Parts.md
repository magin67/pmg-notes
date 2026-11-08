---
title: Decomposing a Form into Atomic and Difference Parts
date: 2026-11-08
updated: 2026-11-08
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: atomic-and-difference-parts-of-a-form
order: 5
description: "Frames, atomic and difference parts of quadratic and polar forms, the Laplacian of a frame, and polyform calculations of projections."
---

The form of an object can be decomposed into an atomic part built from the forms of selected objects and a difference part built from the forms of their differences. The coefficients are determined by the frame. This is an identity of forms and requires no choice of metric.

Coordinates, metric tensors, and the reciprocal basis are defined in [[Bi-coordinates and Di-coordinates]]. This note collects frames, polyform identities, and the shared material on projections: a geometric example, calculation through potentials, and comparison with the isotropic extension.

## The frame of an object

> [!info] The frame of an object
> **Definition.** A frame is a representation of an object as a linear combination of selected objects:
>
> $$
> q=q^i a_i
> $$
>
> The frame includes the objects $a_i$ and the coefficients $q^i$. A repeated upper and lower index indicates summation. If the set is a basis, the coefficients are bi-coordinates. On a linearly dependent set, the representation may be nonunique.

For example, the element $q=(a+c)/2$ has the frames

$$
q=\frac12a+\frac12c=a+\frac12(c-a)
$$

The first uses the elements $a,c$, and the second the element $a$ and the vector $c-a$. The object is unchanged, while the constituents of the representation and their coefficients change. On the dependent set $(w,2w)$, the equalities $w=1w+0(2w)=0w+\frac12(2w)$ give different frames on the same set.

The term “frame” is used here in its PMG sense. In frame theory, it usually denotes a family of vectors rather than a representation of an individual object [2].

The examples below use objects of grade one. The form identities also hold for exterior structures of any single fixed grade. Independence of the constituents is not required. The geometric examples use the unit path $a-b-c$; its resistance geometry is explained after the algebraic identities.

## Decomposing a form using frame elements and their differences

A frame lets us express the quadratic form of an object through the forms of the chosen elements and their differences. This is an identity of PMG forms; it requires neither a metric nor linear independence of the frame elements. It will be used when [[Vertex Elimination and Induced Couplings#Eliminating a single vertex|eliminating the center of a star]] and constructing [[Couplings Within One Part of a Bipartite Graph|couplings within one part of a bipartite graph]].

> [!info] Decomposition of a quadratic form
> **Lemma.** Let $q=q^i a_i$ be a frame, and let $s_q=\sum_i q^i$ be the sum of its coefficients. Then
>
> $$
> [q]^2=s_q\sum_i q^i[a_i]^2
> -\sum_{i<j}q^i q^j[a_j-a_i]^2
> \tag{1}
> $$

Call the first contribution, including the factor $s_q$, the **atomic part**, and the sum of difference forms being subtracted the **difference part**. The word “atomic” refers to the chosen frame elements: they are the basic constituents of this representation.

If all $a_i$ have affine weight $1$, then $s_q$ is the weight of $q$, and the differences are boundaries $(a_i a_j)=a_j-a_i$. In a mixed basis or a vector basis, the sum of the coefficients alone does not determine affine weight. If all $a_i$ are points, the atomic part may also be called the point part. The difference part is a vector form for any frame made of elements.

> [!note]- Proof
> **Proof.** By bilinearity,
>
> $$
> [q]^2=\sum_i(q^i)^2[a_i]^2
> +\sum_{i<j}q^i q^j\{a_i,a_j\}
> $$
>
> Here $\{a_i,a_j\}=[a_i,a_j]+[a_j,a_i]$ is the polar form. Expanding the square of a difference gives
>
> $$
> \{a_i,a_j\}=[a_i]^2+[a_j]^2-[a_j-a_i]^2
> $$
>
> After substitution, the coefficient of $[a_i]^2$ is $(q^i)^2+q^i\sum_{j\ne i}q^j=s_q q^i$. The remaining terms form the second sum in (1). $\square$

> [!example] The form of a midpoint
> For the element $q=(a+c)/2$, one has $s_q=1$, so
>
> $$
> [q]^2=\frac12[a]^2+\frac12[c]^2-\frac14[(ac)]^2
> $$
>
> The quadratic form of the midpoint differs from the average of the endpoint forms by a term depending on their difference.

For a vector in an element basis, $s_q=0$, and the first part of the decomposition vanishes. Its quadratic form is therefore expressed entirely through forms of differences.

> [!example] A vector with three nonzero coordinates
> Let $y=a+b-2c$. Its coefficients sum to zero. By (1),
>
> $$
> [y]^2=-[(ab)]^2+2[(ac)]^2+2[(bc)]^2
> $$
>
> One coefficient is negative. An expansion of a form in squares of differences does not require all coefficients to be positive.

Changing the frame changes the parts of (1), but their difference remains the form $[q]^2$ of the original object.

The atomic part is diagonal in the chosen forms $[a_i]^2$: it contains no mixed forms $[a_i,a_j]$ with $i\ne j$. Its coefficients are $s_q q^i$, rather than $(q^i)^2$ as in the diagonal terms of the directly expanded square. In the midpoint example, its coefficients are $1/2$, whereas direct expansion of $[(a+c)/2]^2$ gives coefficients $1/4$ for $[a]^2$ and $[c]^2$. The rest of the contribution is contained in the square of the difference.

### The difference part and the Laplacian of a frame

Denote the difference part by

$$
L_q=\sum_{i<j}q^i q^j[a_j-a_i]^2
$$

For a frame consisting of elements, this is the polyform representation of a Laplacian with coupling strengths $c_{ij}=q^i q^j$. Call $L_q$ the **Laplacian of this frame**. The subscript $q$ is convenient while the frame is fixed: changing the frame may also change $L_q$.

For an arbitrary frame, a graph can be defined on the indices of its elements. Substituting the elements for the formal vertices gives the same form $L_q$; if their affine weights differ, their differences need not be affine vectors.

If all $q^i$ are positive, one obtains a complete graph on the frame elements. Zero coefficients give isolated vertices. If the coefficients have different signs, some couplings are negative. This is an algebraic extension of the Laplacian definition beyond the core graph model.

> [!example] Two frames on a pair of vertices
> For the midpoint $q=(a+c)/2$, the frame Laplacian is $L_q=\frac14[(ac)]^2$: it specifies one coupling of magnitude $1/4$. This coupling comes from the frame coefficients; the original path $a-b-c$ has no coupling $ac$.
>
> For the vector $y=c-a$, the coefficients are $(-1,1)$, so $L_y=-[(ac)]^2$. Identity (1) becomes $[y]^2=-L_y$.

The Laplacian of a frame differs from the Laplacian of the original graph that defines the metric. Formula (1) constructs it directly from the representation of the object.

### The center and the moment of inertia

If $s_q\ne0$, define $c=q/s_q$. For a frame consisting of elements, this is an element whose coefficients sum to $1$. The difference part has another expression:

$$
L_q=s_q\sum_i q^i[a_i-c]^2
$$

> [!note]- Proof
> **Proof.** Expanding the squares and using $q=s_qc$, one obtains
>
> $$
> s_q\sum_iq^i[a_i-c]^2
> =s_q\sum_iq^i[a_i]^2-[q]^2=L_q
> $$
>
> The last equality follows from (1). $\square$

For the geometric interpretation, choose an origin. Let $x_i$ be the position vectors of the elements, let $\lambda_i\ge0$, $\sum_i\lambda_i=1$, and let $\bar x=\sum_i\lambda_i x_i$ be the position vector of their center. Metric evaluation gives the familiar Lagrange and Huygens-Leibniz identities [1, §2, equations (4)-(6)]:

$$
\sum_i\lambda_i\|x_i\|^2
=\|\bar x\|^2+\sum_i\lambda_i\|x_i-\bar x\|^2
$$

$$
\sum_i\lambda_i\|x_i-\bar x\|^2
=\sum_{i<j}\lambda_i\lambda_j\|x_j-x_i\|^2
$$

The atomic sum gives the second moment about the chosen origin. The difference sum gives the second central moment, or the moment of inertia about the center for unit total mass. The difference is the squared distance from the chosen origin to the center.

> [!example] Two elements on a line
> Take elements at $0$ and $2$, each with weight $1/2$. Their center is at $1$. The atomic sum is $\frac12\cdot0^2+\frac12\cdot2^2=2$, and the difference sum is $\frac14(2-0)^2=1$. The square of the center's coordinate is $2-1=1$.

The name “inertial part” explains the metric meaning of the difference part under these assumptions. We retain the algebraic names in the general lemma: when $s_q=0$, the center $q/s_q$ is undefined, but (1) still holds.

## Decomposition of the polar form

Now consider two objects given by frames on the same set of elements:

$$
p=p^i a_i,\qquad q=q^i a_i,
\qquad s_p=\sum_i p^i,\quad s_q=\sum_i q^i
$$

Recall that the polar form $\{p,q\}=[p,q]+[q,p]$ is symmetric, and $\{q,q\}=2[q]^2$.

> [!info] Decomposition of the polar form
> **Lemma.** For these frames,
>
> $$
> \{p,q\}=\sum_i(s_qp^i+s_pq^i)[a_i]^2-\sum_{i<j}(p^iq^j+p^jq^i)[a_j-a_i]^2
> \tag{2}
> $$

When $p=q$, both sides are doubled, giving (1). If $s_p=s_q=0$, the atomic contribution vanishes. In particular, this occurs for two vectors expressed in an element basis.

> [!note]- Proof
> **Proof.** By the definition of the polar form,
>
> $$
> \{p,q\}=[p+q]^2-[p]^2-[q]^2
> $$
>
> Apply (1) to the three squares. The remaining coefficient of $[a_i]^2$ is $(s_p+s_q)(p^i+q^i)-s_pp^i-s_qq^i=s_qp^i+s_pq^i$. The remaining coefficient of a squared difference is $-(p^iq^j+p^jq^i)$. This gives (2). $\square$

> [!example] Two adjacent vectors of the path
> Take $p=b-a$ and $q=c-b$. Their bi-coordinates in the basis $(a,b,c)$ are $(-1,1,0)$ and $(0,-1,1)$. By (2),
>
> $$
> \{p,q\}=-[(ab)]^2+[(ac)]^2-[(bc)]^2
> $$
>
> Check this using the sum of the vectors: $p+q=c-a$, so the same formula follows from $\{p,q\}=[p+q]^2-[p]^2-[q]^2$.

This identity concerns the symmetric polar form. In PMG algebra, the individual form $[p,q]$ need not equal $[q,p]$ and cannot be recovered from their sum alone. Under metric evaluation the distinction disappears: the polar form gives the number $2p\cdot q$.

## An element and its projection

Graph applications assume a finite connected undirected graph with positive strengths of its existing couplings. The affine-vector space $W$ has a positive definite resistance metric; $\mathcal A$ denotes the affine space of elements.

In this part, a projection is written as an element of affine space: a vertex combination of weight $1$. The norms of the elements themselves are not specified; distances are evaluated on differences. The local center of a projection in the isotropic model is treated separately.

Continue with the path $a-b-c$ with unit coupling strengths. Set

$$
u=b-a,\qquad v=c-b,\qquad w=c-a=u+v
$$

The PMG parentheses denote the same vectors: $u=(ab)$, $v=(bc)$, $w=(ac)$. For this path, $R_{ab}=R_{bc}=1$, $R_{ac}=2$. Effective resistances are squared distances, so

$$
u^2=v^2=1,\qquad u\cdot v=0,\qquad w^2=2
$$

The notation $y^2=y\cdot y$ denotes the norm in the PMG convention. It is nonnegative on $W$ and may have either sign in the isotropic extension. The linear norm $\|y\|=\sqrt{y^2}$ is used when $y^2\ge0$. The formal quadratic form is denoted by $[y]^2$.

Select the vertices $a,c$. They determine the line of elements $a+tw$, where $t$ ranges over the real numbers. We seek an element $q$ on this line such that the residual $b-q$ is orthogonal to the direction $w$:

$$
(b-q)\cdot w=0,\qquad q=a+tw
$$

Substitution gives $u\cdot w-tw^2=0$. Hence

$$
t=\frac12,\qquad q=\frac{a+c}{2},\qquad
r=b-q=\frac{u-v}{2},\qquad r^2=\frac12
$$

The element $q$ is the orthogonal projection of $b$ onto the selected line. The coefficient pair $(1/2,1/2)$ describes $q$ in the basis $(a,c)$. The vertex $b$ itself has no such expansion.

![Projection](<Projection.svg>)

*The left panel shows the graph; the right panel shows its resistance geometry. The line through $a,c$ is blue, and the residual $b-q$ is red. The segment $ac$ in the geometric diagram does not imply a coupling $ac$ in the graph.*

## Which coordinates determine the projection

Let $h_1,\ldots,h_k$ form a basis of a subspace $U$, let $g_{ij}=h_i\cdot h_j$, and let $h^i$ denote the reciprocal basis when the metric on $U$ is nondegenerate. These conventions agree with the [[Bi-coordinates and Di-coordinates|first note]].

> [!info] Orthogonal projection
> **Definition.** The projection of $y$ onto $U$ is an object $y_U\in U$ such that $y-y_U$ is orthogonal to all of $U$. We denote it by $\pi_U(y)$.

If the metric on $U$ is nondegenerate, the projection exists and is unique. Indeed, for $y_U=b^j h_j$, the orthogonality conditions are

$$
g_{ij}b^j=y\cdot h_i\qquad(i=1,\ldots,k)
$$

This is the system $\mathbf G\mathbf b=\mathbf d$ with a unique solution, discussed in the [[Bi-coordinates and Di-coordinates#Metric tensors|note on coordinates]]. This gives

$$
\pi_U(y)=(y\cdot h^i)h_i
=(y\cdot h_i)h^i
\tag{3}
$$

The object $y$ and its projection have the same di-coordinates relative to the chosen basis. If $y\in U$, the projection equals $y$. If $y\notin U$, the recovered bi-coordinates describe $\pi_U(y)$.

> [!example] A single direction
> For $U=\operatorname{span}(w)$, the notation $\operatorname{span}(w)$ means the set of all multiples of $w$. The reciprocal vector to $w$ is $w/w^2$, so
>
> $$
> \pi_U(y)=\frac{y\cdot w}{w^2}w
> $$
>
> On the path, $u\cdot w=v\cdot w=1$. The vectors $u$ and $v$ have the same di-coordinate relative to $w$ and the same projection $w/2$, although the vectors themselves differ.

For an affine subspace $p_0+U$, the projection of an element $x$ is obtained using a difference:

$$
q=p_0+\pi_U(x-p_0),\qquad r=x-q
$$

Choosing another reference element in the same subspace does not change $q$. This follows because the projection of any vector in $U$ is the vector itself.

In a positive definite metric, $q$ is the nearest element. For any other element $q+t$, where $t\in U$, orthogonality gives

$$
\|x-(q+t)\|^2=\|r\|^2+\|t\|^2
$$

The minimum occurs only at $t=0$. In the path example, this equality is $\|b-(q+sw)\|^2=1/2+2s^2$.

## Calculation using polyforms

For graph vectors, all the inner products used in the geometric sections can be calculated by the PMG metric identity. Recall the notation: $L$ is the Laplacian polyform, $M=\exp L$ is its exponential, and $e$ is the unit form. The potential of a form $f$ is $u_M(f)=\tau(Mf)$, where $\tau$ extracts the coefficient of a fixed spanning-tree form.

For any exterior structures $Y,Z$ of the same grade, formed from vectors in $W$,

$$
Y\cdot Z=\frac{u_M([Y,Z])}{u_M(e)}
$$

In particular, for a basis of a vector subspace, the di-coordinates and Gram matrix entries are

$$
d_i=\frac{u_M([y,h_i])}{u_M(e)},\qquad
g_{ij}=\frac{u_M([h_i,h_j])}{u_M(e)}
$$

This rule applies to the vector arguments of the core. Inner products involving local points and $z$ are defined by the metric in the [[The Null Vector, Isotropic Representation, and the Boundary#The original points and the extended space|note on isotropic representation]].

Decomposition (1) gives another direct application. For a vector $y=y^i a_i$ in the vertex basis, where $\sum_i y^i=0$, apply metric evaluation to the form $[y]^2$:

$$
y^2=-\sum_{i<j}y^i y^jR_{ij}
$$

For $y=a+b-2c$ on the path, this gives $y^2=-R_{ab}+2R_{ac}+2R_{bc}=-1+4+2=5$. Check directly: $y=-u-2v$, and $u^2=v^2=1$, $u\cdot v=0$ also give $y^2=5$.

Similarly, for two vectors $p,q$ in an element basis, formula (2) gives

$$
p\cdot q=-\frac12\sum_{i<j}(p^iq^j+p^jq^i)R_{ij}
$$

The factor $1/2$ appears because the metric evaluation of $\{p,q\}$ is $2p\cdot q$. For $p=b-a$, $q=c-b$ on the path, one obtains $p\cdot q=(-R_{ab}+R_{ac}-R_{bc})/2=(-1+2-1)/2=0$. This agrees with the orthogonality of $u,v$ established at the start of the note.

For a single direction, the normalizing denominator cancels, and the projection formula becomes

$$
\pi_U(y)=\frac{u_M([y,w])}{u_M([w]^2)}w
\tag{4}
$$

### A direct calculation on the path

For the graph,

$$
L=[u]^2+[v]^2,\qquad
M=e+[u]^2+[v]^2+[u  v]^2
$$

The spanning-tree form is $T_3=[u  v]^2$, and $u_M(e)=1$. Calculate the potentials by expanding products of forms. For $[u,w]$, only the factor $[v]^2$ contributes to $T_3$:

$$
[v]^2[u,w]=[v  u,v  w]=T_3
$$

For $[w]^2$, the factors $[u]^2$ and $[v]^2$ each contribute one such term. Hence

$$
u_M([u,w])=1,\qquad u_M([w]^2)=2
$$

Formula (4) gives $\pi_U(u)=w/2$, the same result obtained earlier from effective resistances.

### Distance to a subspace

Let $h_1,\ldots,h_k$ form a basis of a nonzero subspace $U\subseteq W$, with $x,p_0\in\mathcal A$. Use the positive definite resistance metric on $W$ and set $\Omega=h_1 \cdots  h_k$. The nonzero exterior structure $\Omega$ specifies the direction subspace, as shown in the [[Basis#Specifying a subspace by an exterior structure|note on choosing a subspace]].

> [!info] Distance to a subspace
> **Lemma.** If $q$ is the projection of $x$ onto $p_0+U$, then
>
> $$
> \|x-q\|^2
> =\frac{\|\,(x-p_0) \Omega\,\|^2}{\|\Omega\|^2}
> =\frac{u_M([(x-p_0) \Omega]^2)}{u_M([\Omega]^2)}
> \tag{5}
> $$

> [!note]- Proof
> **Proof.** Write $x-p_0=s+r$, where $s\in U$ and $r=x-q$ is orthogonal to $U$. Then $s \Omega=0$. The Gram determinant for a vector $r$ orthogonal to $U$ gives $\|r \Omega\|^2=r^2\|\Omega\|^2$. Applying the metric identity completes the proof. The denominator is positive because the $h_i$ are independent and the metric is positive definite. $\square$

For the path, take $p_0=a$, $x=b$, $\Omega=w=u+v$. Then $u  w=u  v$, and

$$
\|b-q\|^2
=\frac{u_M([u  v]^2)}{u_M([w]^2)}
=\frac12
$$

The numerator is $1$: when $M$ is multiplied by $T_3$, only the unit term $e$ contributes to the required grade. Geometrically, this is the ratio of the squared area of a parallelogram to the squared length of its base.

## Projection of exterior structures and forms

A linear projection of vectors extends to exterior products by projecting each factor. For example, the image of $y_1  y_2$ is $\pi_U(y_1) \pi_U(y_2)$. The rule is then extended by linearity.

For a form $[Y,Z]$, project both arguments. This action respects multiplication of forms, since that multiplication is defined by exterior products of their arguments. It defines a linear substitution in a polyform.

On the path, $\pi_U(u)=\pi_U(v)=w/2$. Hence

$$
[u]^2\ \longmapsto\ \frac14[w]^2,\qquad
[u  v]^2\ \longmapsto\ 0
$$

Area vanishes when the plane is projected onto a line. The evaluation of the first form changes from $1$ to $1/2$.

> [!note] Forms and their evaluations
> From $u=s+r$, where $s=w/2$ and $s\cdot r=0$, one obtains
>
> $$
> [u]^2=[s]^2+[s,r]+[r,s]+[r]^2
> $$
>
> The mixed forms $[s,r]$ and $[r,s]$ do not vanish. Their metric evaluations are zero. Thus the numerical equality $u^2=s^2+r^2$ does not imply the equality of forms $[u]^2=[s]^2+[r]^2$.

## Coordinates in the isotropic extension

The properties of selecting the local center and preservation of metric evaluations of differences are discussed in [[Nonlocal Elements, Spheres, and Their Centers]]. Here we compare this operation with linear orthogonal projection.

In this section, use the direct notation from the [[The Null Vector, Isotropic Representation, and the Boundary#Local points|note on the isotropic model]]: local points $x,p_i,q$ are themselves elements of the extension, with $x^2=0$ and $x\cdot z=1$. A linear combination of unit weight can be nonlocal; its center is selected by $\pi(p)=p-p^2z/2$. The preceding sections used ordinary affine notation; here we explicitly distinguish a linear combination from its local center.

In this section, the index $i$ ranges over $0,\ldots,k$. Let local points $p_0,\ldots,p_k$ have affinely independent Euclidean coordinates. Consider

$$
S=\operatorname{span}(z,p_0,\ldots,p_k)
$$

The metric restricted to $S$ is nondegenerate. Indeed, an object in $S$ orthogonal to all of $S$ is, by orthogonality to $z$, expressible using $z$ and the differences $p_i-p_0$. Orthogonality to these differences and positive definiteness of the displacement metric leave only a multiple of $z$; orthogonality to $p_0$ makes it zero.

Hence the orthogonal projection $\widehat x=\pi_S(x)$ exists and is unique. It has the expression

$$
\widehat x=w_xz+\beta^i p_i,\qquad
\sum_{i=0}^k\beta^i=1
$$

The coefficient sum follows from $\widehat x\cdot z=x\cdot z=1$. The coefficient $w_x$ of $z$ is the **orbital relative to the chosen extended basis**. It is a bi-coordinate; the di-coordinate relative to $z$ is $1$.

> [!info] Coordinates in the isotropic extension
> **Proposition.** Let $q$ be the nearest local point in the Euclidean affine hull of $p_0,\ldots,p_k$. Then
>
> $$
> q=\pi\left(\beta^i p_i\right),\qquad
> \widehat x=q-\frac{(x-q)^2}{2}z,\qquad
> \widehat x^2=-(x-q)^2
> \tag{6}
> $$
>
> The coefficients $\beta^i$ give the affine coordinates of the center $q$; the linear combination in parentheses need not itself be local.

> [!note]- Proof
> **Proof.** Write $\delta=(x-q)^2$ for the squared distance from $x$ to $q$. The Pythagorean theorem in Euclidean coordinates gives $(x-p_i)^2=(q-p_i)^2+\delta$. By the distance formula for local points,
>
> $$
> x\cdot p_i=q\cdot p_i-\frac{\delta}{2}
> $$
>
> Thus $q-\delta z/2$ has the same di-coordinates relative to $p_i,z$ as $x$. This element belongs to $S$, since $q$ differs from a normalized linear combination of the $p_i$ only by a multiple of $z$. Uniqueness of orthogonal projection gives $\widehat x=q-\delta z/2$. Comparing the coefficients of $p_i$ gives the first formula in (6), and evaluating the norm gives the last. $\square$

The operations $\pi_S$ and $\pi$ differ: the former is linear orthogonal projection onto $S$, while the latter selects the local center by correction along $z$. In particular, $\pi(\widehat x)=q$.

### The linear midpoint and its local center

For the path, choose orthogonal unit coordinate directions $u_0,v_0$. Then

$$
a=p_0,\qquad b=p_0+u_0-\frac12z,\qquad c=p_0+u_0+v_0-z
$$

The subscripts distinguish these directions from the vertex differences $u=b-a$, $v=c-b$ in the preceding sections. The linear midpoint $p=(a+c)/2$ has norm

$$
p^2=\frac12a^2+\frac12c^2-\frac14(c-a)^2=-\frac12
$$

Its local center $q=\pi(p)=(a+c)/2+z/4$ is the nearest point on the line $ac$ to $b$. Since $(b-q)^2=1/2$, formula (6) gives

$$
\widehat b=\pi_S(b)=q-\frac14z=\frac{a+c}{2}=p
$$

The equality of the orthogonal projection and the linear midpoint is specific to this example. A **sub-basis** is a selected part of a full basis generating its own subspace. The table uses the sub-basis $(z,a,c)$, with coordinates listed in that order.

| Object | Bi-coordinates in $(z,a,c)$ | Di-coordinates relative to $(z,a,c)$ | Norm |
| --- | --- | --- | --- |
| Local point $b$ | No expansion in this sub-basis | $(1,-1/2,-1/2)$ | $0$ |
| Orthogonal projection $\widehat b=p$ | $(0,1/2,1/2)$ | $(1,-1/2,-1/2)$ | $-1/2$ |
| Local center $q=\pi(p)$ | $(1/4,1/2,1/2)$ | $(1,-1/4,-1/4)$ | $0$ |

The elements $b$ and $\widehat b$ have the same di-coordinates relative to the sub-basis but different norms. Correction along $z$ returns the local center $q$ and changes the di-coordinates relative to $a,c$.

## When the construction needs qualification

In the positive definite space $W$, every subspace admits a unique orthogonal projection. The set used to specify it may nevertheless be redundant. For example, $w$ and $2w$ generate the same line, while the expansion $w=\alpha w+\beta(2w)$ allows every pair with $\alpha+2\beta=1$. The projection is unique, but the coefficients on this set are not: it is not a basis.

In an indefinite metric, independence of the basis elements does not guarantee a nondegenerate Gram matrix. For the direction $\mathbb Rz$, the set of all multiples of $z$, the Gram matrix is $(0)$. The projection of $p_0$ onto it does not exist: $(p_0-tz)\cdot z=1$ for every $t$. For the original object $z$, however, every $tz$ satisfies the orthogonality condition on the residual. Uniqueness fails as well.

For a disconnected graph, the arguments apply separately to each connected component. The published core does not define a finite resistance metric between different components; using a pseudoinverse matrix alone does not remove this limitation.

These definitions do not require nonnegative bi-coordinates. [[Selected Vertices and the Dirichlet Problem]] derives nonnegativity from the graph properties and proves that influence coefficients equal the bi-coordinates of projections. The geometry of residuals connects this problem to [[Vertex Contraction and Graph Gluing|vertex contraction and graph gluing]].

## Sources and status of the results

The definitions of objects, elements, points, vectors, forms, and potentials agree with the [[Core specification|core specification]]. This note is based on the author's PMG research; definitions and proofs are given here. The distinction between the PMG meaning of “frame” and its external usage is explained with reference to [2].

The quadratic and polar form decompositions (1), (2) are proved by bilinearity. The Laplacian of a frame names the difference part defined here; negative couplings explicitly use an algebraic extension of the main graph model. The metric interpretation through a center and moment of inertia is compared with the known identities in [1]. Orthogonal projection is a standard linear-algebra construction; its relation to di-coordinates and its expression through potentials are derived here. Formulas (5), (6) are also proved in the text.

The examples are calculated directly; the potential calculation on the path uses the product of forms independently of the geometric calculation. In the previous combined revision, exact rational arithmetic verified the projections, the isotropic-coordinate table, distance to a subspace, and the coefficients of the quadratic and polar decompositions, including frames with negative coefficients and zero coefficient sum. Splitting the note preserves these identities and proofs. No working conjectures are included.

1. Havel, T. F. [Heron’s Formula in Higher Dimensions](https://doi.org/10.1007/s00006-023-01305-8). *Advances in Applied Clifford Algebras*, 34, 9 (2024), §2. Lagrange and Huygens-Leibniz identities for weighted centers.
2. Casazza, P. G.; Lynch, R. G. [A brief introduction to Hilbert space frame theory and its applications](https://arxiv.org/abs/1509.07347). The use of frame for a family of vectors in a Hilbert space.

Next: [[Vertex Contraction and Graph Gluing]]. Navigation: [[en/Resistance Geometry and Duality/Spaces/Spaces|Spaces]].
