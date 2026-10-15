---
title: Projections, Bi-coordinates, and Di-coordinates
date: 2026-10-13
updated: 2026-10-15
revision: 3
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: projections-bi-coordinates-and-di-coordinates
order: 3
description: "Frames, bi- and di-coordinates, decompositions of quadratic and polar forms, the Laplacian of a frame, and projection calculations using polyforms."
---

Select several vertices of a graph. How can we describe the other vertices relative to them? We can calculate distances and inner products. We can also find the nearest point in the affine subspace they generate. In general, however, an arbitrary original vertex cannot be expressed as a linear combination of the selected vertices.

This note examines which coordinates describe the object itself, which describe its projection, and how to calculate them using metric polyforms.

This is the third note in the series “Spaces and Subspaces in PMG”. The main part builds on [[Spaces, Subspaces, and the Choice of a Basis]]. [[The Null Vector, Isotropic Representation, and the Boundary]] is needed for the section “Coordinates in the isotropic extension” and the example of degeneracy along $\mathbb Rz$. Definitions of forms and potentials are collected in the [[Core specification|core specification]]. The graph model remains the same: the graph is connected and undirected, with positive coefficients for all existing couplings. The space of affine vectors $W$ carries a positive definite resistance metric.

We first define bi-coordinates and decompose the forms of frames. We then consider di-coordinates and projections, and finally extend the coordinate description to the isotropic model.

## A point and its projection

Continue with the path $a-b-c$ with unit coupling coefficients. Set

$$
u=b-a,\qquad v=c-b,\qquad w=c-a=u+v
$$

The PMG parentheses denote the same vectors: $u=(ab)$, $v=(bc)$, $w=(ac)$. For this path, $R_{ab}=R_{bc}=1$, $R_{ac}=2$. Effective resistances are squared distances, so

$$
u^2=v^2=1,\qquad u\cdot v=0,\qquad w^2=2
$$

For $y\in W$, the notation $y^2=y\cdot y$ denotes a number, the squared norm in the positive definite metric. In the isotropic extension, the same notation denotes the metric square, which can be negative. The formal quadratic form is denoted by $[y]^2$.

Select the vertices $a,c$. They determine the line of points $a+tw$, where $t$ ranges over the real numbers. We seek a point $q$ on this line such that the residual $b-q$ is orthogonal to the direction $w$:

$$
(b-q)\cdot w=0,\qquad q=a+tw
$$

Substitution gives $u\cdot w-tw^2=0$. Hence

$$
t=\frac12,\qquad q=\frac{a+c}{2},\qquad
r=b-q=\frac{u-v}{2},\qquad r^2=\frac12
$$

The point $q$ is the orthogonal projection of $b$ onto the selected line. The coefficient pair $(1/2,1/2)$ describes $q$ in the basis $(a,c)$. The vertex $b$ itself has no such expansion.

![[Projection.svg]]

*The left panel shows the graph; the right panel shows its resistance geometry. The line through $a,c$ is blue, and the residual $b-q$ is red. The segment $ac$ in the geometric diagram does not imply a coupling $ac$ in the graph.*

## Bi-coordinates and frames

Let $h_1,\ldots,h_k$ be a basis of a linear space $U$. This means that every object in $U$ has a unique expansion in these objects.

> [!info] Bi-coordinates
> **Definition.** The bi-coordinates of an object $y\in U$ in the chosen basis are the coefficients $b^i$ in the expansion
>
> $$
> y=\sum_{i=1}^k b^i h_i
> \tag{1}
> $$

The superscript in $b^i$ is a coordinate index, not an exponent.

We call the representation (1) a **frame of the object**. A frame includes the chosen elements and the coefficients of their linear combination. This distinguishes the object itself from its different representations.

For example, the point $q=(a+c)/2$ has two frames:

$$
q=\frac12a+\frac12c=a+\frac12(c-a)
$$

The first uses the points $a,c$; the second uses the point $a$ and the vector $c-a$. The coefficients differ, while the object remains the same.

A frame may also use a linearly dependent set. For example, the vector $w$ has the representations $w=1w+0(2w)$ and $w=0w+\frac12(2w)$. The set $(w,2w)$ is not a basis, and its coefficients are not unique. We use bases when discussing coordinates below; the identities for forms also hold for redundant frames.

The term “frame” is used here in the PMG sense. In frame theory, it usually denotes the family of vectors itself, rather than a representation of an individual object.

Bi-coordinates require no metric. A basis may consist of points, vectors, or other objects in the relevant linear space. For example, exterior elements of one grade can be expanded in a basis of that grade.

The barycentric coordinates of points are a special case of bi-coordinates. If every $h_i$ has affine weight $1$, the weight of $y$ is the sum of its coefficients. This sum is $1$ for a point and $0$ for a vector.

> [!example] Points, vectors, and a mixed basis
> In the basis $(a,b)$, the point $2a-b$ has bi-coordinates $(2,-1)$, and the vector $b-a$ has bi-coordinates $(-1,1)$.
>
> The same point can be written as $2a-b=a-u$, where $u=b-a$. In the mixed basis $(a,u)$, its coordinates are $(1,-1)$. Their sum is zero, although the object remains a point: only the first basis element has nonzero affine weight.
>
> In the vector basis $(u,v)$, the vector $2u+3v$ has coordinates $(2,3)$. There is no restriction on their sum.

The general rule is

$$
\varepsilon(y)=\sum_i b^i\varepsilon(h_i)
$$

Here $\varepsilon$ denotes affine weight. This equality applies in spaces where such a functional is defined.

Coordinates depend on the basis. The vector $v$ has coordinates $(0,1)$ in the basis $(u,v)$ and $(-1,1)$ in the basis $(u,u+v)$, since $v=-u+(u+v)$.

## Decomposing a form using frame elements and their differences

A frame lets us express the quadratic form of an object through the forms of the chosen elements and their differences. This is an identity of PMG forms; it requires neither a metric nor linear independence of the frame elements. It will be used when [[Vertex Elimination and Induced Couplings#Eliminating a single vertex|eliminating the center of a star]] and constructing [[Couplings Within One Part of a Bipartite Graph|couplings within one part of a bipartite graph]].

In the identities for forms below, all frame elements belong to the same space $\Lambda^kV$ at a fixed grade $k$. Points and affine vectors may occur in one frame: they all have grade $1$.

> [!info] Decomposition of a quadratic form
> **Lemma.** Let $q=\sum_i q^i a_i$ be a frame, and let $s_q=\sum_i q^i$ be the sum of its coefficients. Then
>
> $$
> [q]^2=s_q\sum_i q^i[a_i]^2
> -\sum_{i<j}q^i q^j[a_j-a_i]^2
> \tag{2}
> $$

We call the first contribution, including the factor $s_q$, the **atomic part**, and the sum of difference forms being subtracted the **difference part**. The word “atomic” refers to the chosen frame elements: they are the basic constituents of this representation.

If all $a_i$ have affine weight $1$, then $s_q$ is the weight of $q$, and the differences are boundaries $(a_i a_j)=a_j-a_i$. In a mixed basis or a vector basis, the sum of the coefficients alone does not determine affine weight. Thus the names “point part” and “vector part” apply only to a frame consisting of points.

> [!proof]- Proof
> By bilinearity,
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
> After substitution, the coefficient of $[a_i]^2$ is $(q^i)^2+q^i\sum_{j\ne i}q^j=s_q q^i$. The remaining terms form the second sum in (2). $\square$

> [!example] The form of a midpoint
> For the point $q=(a+c)/2$, we have $s_q=1$, so
>
> $$
> [q]^2=\frac12[a]^2+\frac12[c]^2-\frac14[(ac)]^2
> $$
>
> The quadratic form of the midpoint differs from the average of the endpoint forms by a term depending on their difference.

For a vector in a point basis, $s_q=0$, and the first part of the decomposition vanishes. Its quadratic form is therefore expressed entirely through forms of differences.

> [!example] A vector with three nonzero coordinates
> Let $y=a+b-2c$. Its coefficients sum to zero. By (2),
>
> $$
> [y]^2=-[(ab)]^2+2[(ac)]^2+2[(bc)]^2
> $$
>
> One coefficient is negative. An expansion of a form in squares of differences does not require all coefficients to be positive.

Changing the frame changes the parts of (2), but their difference remains the form $[q]^2$ of the original object.

The atomic part consists of forms $[a_i]^2$, but it is not the usual diagonal part of the expanded square. In the midpoint example, its coefficients are $1/2$, whereas direct expansion of $[(a+c)/2]^2$ gives coefficients $1/4$ for $[a]^2$ and $[c]^2$. The rest of the contribution is contained in the square of the difference.

### The difference part and the Laplacian of a frame

Denote the difference part by

$$
L_q=\sum_{i<j}q^i q^j[a_j-a_i]^2
$$

For a frame consisting of points, this is the polyform representation of a Laplacian with coupling coefficients $c_{ij}=q^i q^j$. We call $L_q$ the **Laplacian of this frame**. The subscript $q$ is convenient while the frame is fixed: changing the frame may also change $L_q$.

For an arbitrary frame, a graph can be defined on the indices of its elements. Substituting the elements for the formal vertices gives the same form $L_q$; if their affine weights differ, their differences need not be affine vectors.

If all $q^i$ are positive, we obtain a complete weighted graph on the frame elements. Zero coefficients give isolated vertices. If the coefficients have different signs, some couplings are negative. This is an algebraic extension of the Laplacian definition beyond the core graph model.

> [!example] Two frames on a pair of vertices
> For the midpoint $q=(a+c)/2$, the frame Laplacian is $L_q=\frac14[(ac)]^2$: it specifies one coupling of magnitude $1/4$. This coupling comes from the frame coefficients; the original path $a-b-c$ has no coupling $ac$.
>
> For the vector $y=c-a$, the coefficients are $(-1,1)$, so $L_y=-[(ac)]^2$. Identity (2) becomes $[y]^2=-L_y$.

The Laplacian of a frame differs from the Laplacian of the original graph that defines the metric. Formula (2) constructs it directly from the representation of the object.

### The center and the moment of inertia

If $s_q\ne0$, define $c=q/s_q$. For a frame consisting of points, this is a point whose coefficients sum to $1$. The difference part has another expression:

$$
L_q=s_q\sum_i q^i[a_i-c]^2
$$

> [!proof]- Proof
> Expanding the squares and using $q=s_qc$, we obtain
>
> $$
> s_q\sum_iq^i[a_i-c]^2
> =s_q\sum_iq^i[a_i]^2-[q]^2=L_q
> $$
>
> The last equality follows from (2). $\square$

For the geometric interpretation, choose an origin. Let $x_i$ be the position vectors of the points, let $\lambda_i\ge0$, $\sum_i\lambda_i=1$, and let $\bar x=\sum_i\lambda_i x_i$ be the position vector of their center. Metric evaluation gives the familiar Lagrange and Huygens-Leibniz identities [1, §2, equations (4)-(6)]:

$$
\sum_i\lambda_i\|x_i\|^2
=\|\bar x\|^2+\sum_i\lambda_i\|x_i-\bar x\|^2
$$

$$
\sum_i\lambda_i\|x_i-\bar x\|^2
=\sum_{i<j}\lambda_i\lambda_j\|x_j-x_i\|^2
$$

The atomic sum gives the second moment about the chosen origin. The difference sum gives the second central moment, or the moment of inertia about the center for unit total mass. The squared norm of the center itself is the difference between these quantities.

> [!example] Two points on a line
> Take points at $0$ and $2$, each with weight $1/2$. Their center is at $1$. The atomic sum is $\frac12\cdot0^2+\frac12\cdot2^2=2$, and the difference sum is $\frac14(2-0)^2=1$. The square of the center's coordinate is $2-1=1$.

The name “inertial part” explains the metric meaning of the difference part under these assumptions. We retain the algebraic names in the general lemma: when $s_q=0$, the center $q/s_q$ is undefined, but (2) still holds.

## Decomposition of the polar form

Now consider two objects given by frames on the same set of elements:

$$
p=\sum_i p^i a_i,\qquad q=\sum_i q^i a_i,
\qquad s_p=\sum_i p^i,\quad s_q=\sum_i q^i
$$

Recall that the polar form $\{p,q\}=[p,q]+[q,p]$ is symmetric, and $\{q,q\}=2[q]^2$.

> [!info] Decomposition of the polar form
> **Lemma.** For these frames,
>
> $$
> \{p,q\}=\sum_i(s_qp^i+s_pq^i)[a_i]^2-\sum_{i<j}(p^iq^j+p^jq^i)[a_j-a_i]^2
> \tag{3}
> $$

When $p=q$, both sides are doubled, giving (2). If $s_p=s_q=0$, the atomic contribution vanishes. In particular, this occurs for two vectors expressed in a point basis.

> [!proof]- Proof
> By the definition of the polar form,
>
> $$
> \{p,q\}=[p+q]^2-[p]^2-[q]^2
> $$
>
> Apply (2) to the three squares. The remaining coefficient of $[a_i]^2$ is $(s_p+s_q)(p^i+q^i)-s_pp^i-s_qq^i=s_qp^i+s_pq^i$. The remaining coefficient of a squared difference is $-(p^iq^j+p^jq^i)$. This gives (3). $\square$

> [!example] Two adjacent vectors of the path
> Take $p=b-a$ and $q=c-b$. Their bi-coordinates in the basis $(a,b,c)$ are $(-1,1,0)$ and $(0,-1,1)$. By (3),
>
> $$
> \{p,q\}=-[(ab)]^2+[(ac)]^2-[(bc)]^2
> $$
>
> Check this using the sum of the vectors: $p+q=c-a$, so the same formula follows from $\{p,q\}=[p+q]^2-[p]^2-[q]^2$.

This identity concerns the symmetric polar form. In PMG algebra, the individual form $[p,q]$ need not equal $[q,p]$ and cannot be recovered from their sum alone. Under metric evaluation the distinction disappears: the polar form gives the number $2p\cdot q$.

## Di-coordinates: inner products

Now suppose that the space carries an inner product. Here this means a symmetric bilinear metric; in the isotropic extension it may be indefinite.

> [!info] Di-coordinates
> **Definition.** The di-coordinates of an object $y$ relative to the basis $h_1,\ldots,h_k$ are the numbers
>
> $$
> d_i=y\cdot h_i
> \tag{4}
> $$

They are also defined for an object outside $U$, provided it belongs to the ambient metric space. Unlike bi-coordinates, di-coordinates depend on the metric.

### An example with a nonorthogonal basis

In the plane of our path, choose $h_1=u$, $h_2=u+v$. For $y=v$, we have already found the bi-coordinates $(-1,1)$. The di-coordinates are

$$
d_1=v\cdot u=0,\qquad d_2=v\cdot(u+v)=1
$$

Thus the same object has bi-coordinates $(-1,1)$ and di-coordinates $(0,1)$. The value $d_2=1$ is not the coefficient of orthogonal projection onto the direction $h_2$: that coefficient is $d_2/h_2^2=1/2$.

![[Coordinates.svg]]

*The basis vectors $h_1,h_2$ are not orthogonal. To obtain $v$, we add $-h_1$ to $h_2$. At the same time, the inner product $v\cdot h_1$ is zero.*

### Converting between the two sets of coordinates

Let $\mathbf K$ be the Gram matrix of the basis, whose entries are $K_{ij}=h_i\cdot h_j$. Substituting (1) into (4) gives

$$
d_i=\sum_j K_{ij}b^j
$$

If $\mathbf b$ and $\mathbf d$ are written as columns, this becomes

$$
\mathbf d=\mathbf K\mathbf b,\qquad
\mathbf b=\mathbf K^{-1}\mathbf d
\tag{5}
$$

The second formula requires $\mathbf K$ to be invertible. Equivalently, the metric on $U$ must be nondegenerate: no nonzero object in $U$ is orthogonal to all of $U$. In our example,

$$
\mathbf K=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad
\mathbf K\begin{pmatrix}-1\\1\end{pmatrix}
=\begin{pmatrix}0\\1\end{pmatrix}
$$

The matrix simply collects the inner products already defined.

### The reciprocal basis

If the metric on $U$ is nondegenerate, there is a unique basis $h^1,\ldots,h^k$ in the same space $U$ such that

$$
h^i\cdot h_j=\delta^i_j
$$

The symbol $\delta^i_j$ equals $1$ when $i=j$ and $0$ otherwise. This basis is called the **reciprocal basis**, or the metric dual basis. Its elements are obtained from the columns of the inverse Gram matrix: $h^i=\sum_j(\mathbf K^{-1})_{ji}h_j$.

For $y\in U$, we have

$$
b^i=y\cdot h^i,\qquad y=\sum_i d_i h^i
$$

The first equality follows by taking the inner product of (1) with $h^i$. For the second, take the inner product of both sides with each $h_j$: the products agree, and nondegeneracy of the metric implies equality of the objects.

Thus di-coordinates are also the coefficients of expansion in the reciprocal basis. This is their duality with bi-coordinates.

In our example, $h^1=u-v$, $h^2=v$. Check that $(u-v)\cdot u=1$, $(u-v)\cdot(u+v)=0$, $v\cdot u=0$, and $v\cdot(u+v)=1$. The di-coordinates $(0,1)$ therefore give the expansion $v=0h^1+1h^2$.

## Which coordinates determine the projection

> [!info] Orthogonal projection of a vector
> **Definition.** The projection of $y$ onto $U$ is an element $y_U\in U$ such that $y-y_U$ is orthogonal to every element of $U$. We denote it by $\pi_U(y)$.

If the metric on $U$ is nondegenerate, the projection exists and is unique. Indeed, for $y_U=\sum_j b^j h_j$, the orthogonality conditions are

$$
\sum_j K_{ij}b^j=y\cdot h_i\qquad(i=1,\ldots,k)
$$

This is system (5), which has a unique solution. We obtain

$$
\pi_U(y)=\sum_i(y\cdot h^i)h_i
=\sum_i(y\cdot h_i)h^i
\tag{6}
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

For an affine subspace $p_0+U$, the projection of a point $x$ is obtained using a difference:

$$
q=p_0+\pi_U(x-p_0),\qquad r=x-q
$$

Choosing another reference point in the same subspace does not change $q$. This follows because the projection of any vector in $U$ is the vector itself.

In a positive definite metric, $q$ is the nearest point. For any other point $q+t$, where $t\in U$, orthogonality gives

$$
\|x-(q+t)\|^2=\|r\|^2+\|t\|^2
$$

The minimum occurs only at $t=0$. In the path example, this equality is $\|b-(q+sw)\|^2=1/2+2s^2$.

## Calculation using polyforms

For graph vectors, all the inner products used above can be calculated by the PMG metric identity. Recall the notation: $L$ is the Laplacian polyform, $M_G=\exp L$ is its exponential, and $e$ is the unit form. The potential of a form $f$ is $u_{M_G}(f)=\tau(M_Gf)$, where $\tau$ extracts the coefficient of a fixed spanning-tree form.

For any exterior elements $Y,Z$ of the same grade, formed from vectors in $W$,

$$
Y\cdot Z=\frac{u_{M_G}([Y,Z])}{u_{M_G}(e)}
$$

In particular, for a basis of a vector subspace, the di-coordinates and Gram matrix entries are

$$
d_i=\frac{u_{M_G}([y,h_i])}{u_{M_G}(e)},\qquad
K_{ij}=\frac{u_{M_G}([h_i,h_j])}{u_{M_G}(e)}
$$

This rule applies to the vector arguments of the core. Inner products involving local points and $z$ are defined by the metric in the [[The Null Vector, Isotropic Representation, and the Boundary#The original points and the extended space|note on isotropic representation]].

Decomposition (2) gives another direct application. For a vector $y=\sum_i y^i a_i$ in the vertex basis, where $\sum_i y^i=0$, apply metric evaluation to the form $[y]^2$:

$$
y^2=-\sum_{i<j}y^i y^jR_{ij}
$$

For $y=a+b-2c$ on our path, this gives $y^2=-R_{ab}+2R_{ac}+2R_{bc}=-1+4+2=5$. Check directly: $y=-u-2v$, and $u^2=v^2=1$, $u\cdot v=0$ also give $y^2=5$.

Similarly, for two vectors $p,q$ in a point basis, formula (3) gives

$$
p\cdot q=-\frac12\sum_{i<j}(p^iq^j+p^jq^i)R_{ij}
$$

The factor $1/2$ appears because the metric evaluation of $\{p,q\}$ is $2p\cdot q$. For $p=b-a$, $q=c-b$ on our path, we obtain $p\cdot q=(-R_{ab}+R_{ac}-R_{bc})/2=(-1+2-1)/2=0$. This agrees with the orthogonality of $u,v$ established at the start of the note.

For a single direction, the normalizing denominator cancels, and the projection formula becomes

$$
\pi_U(y)=\frac{u_{M_G}([y,w])}{u_{M_G}([w]^2)}w
\tag{7}
$$

### A direct calculation on the path

For our graph,

$$
L=[u]^2+[v]^2,\qquad
M_G=e+[u]^2+[v]^2+[u\wedge v]^2
$$

The spanning-tree form is $T_3=[u\wedge v]^2$, and $u_{M_G}(e)=1$. Calculate the potentials by expanding products of forms. For $[u,w]$, only the factor $[v]^2$ contributes to $T_3$:

$$
[v]^2[u,w]=[v\wedge u,v\wedge w]=T_3
$$

For $[w]^2$, the factors $[u]^2$ and $[v]^2$ each contribute one such term. Hence

$$
u_{M_G}([u,w])=1,\qquad u_{M_G}([w]^2)=2
$$

Formula (7) gives $\pi_U(u)=w/2$, the same result obtained earlier from effective resistances.

### Distance to a subspace

Let $h_1,\ldots,h_k$ form a basis of a nonzero subspace $U\subseteq W$, with $x,p_0\in\mathcal A$. Use the positive definite resistance metric on $W$ and set $\Omega=h_1\wedge\cdots\wedge h_k$. The nonzero exterior element $\Omega$ specifies the direction subspace, as shown in the [[Spaces, Subspaces, and the Choice of a Basis#Specifying a subspace by an exterior element|note on choosing a subspace]].

**Lemma.** If $q$ is the projection of $x$ onto $p_0+U$, then

$$
\|x-q\|^2
=\frac{\|\,(x-p_0)\wedge\Omega\,\|^2}{\|\Omega\|^2}
=\frac{u_{M_G}([(x-p_0)\wedge\Omega]^2)}{u_{M_G}([\Omega]^2)}
\tag{8}
$$

> [!proof]- Proof
> Write $x-p_0=s+r$, where $s\in U$ and $r=x-q$ is orthogonal to $U$. Then $s\wedge\Omega=0$. The Gram determinant for a vector $r$ orthogonal to $U$ gives $\|r\wedge\Omega\|^2=r^2\|\Omega\|^2$. Applying the metric identity completes the proof. The denominator is positive because the $h_i$ are independent and the metric is positive definite. $\square$

For the path, take $p_0=a$, $x=b$, $\Omega=w=u+v$. Then $u\wedge w=u\wedge v$, and

$$
\|b-q\|^2
=\frac{u_{M_G}([u\wedge v]^2)}{u_{M_G}([w]^2)}
=\frac12
$$

The numerator is $1$: when $M_G$ is multiplied by $T_3$, only the unit term $e$ contributes to the required grade. Geometrically, this is the ratio of the squared area of a parallelogram to the squared length of its base.

## Projection of exterior elements and forms

A linear projection of vectors extends to exterior products by projecting each factor. For example, the image of $y_1\wedge y_2$ is $\pi_U(y_1)\wedge\pi_U(y_2)$. The rule is then extended by linearity.

For a form $[Y,Z]$, project both arguments. This action respects multiplication of forms, since that multiplication is defined by exterior products of their arguments. It defines a linear substitution in a polyform.

On our path, $\pi_U(u)=\pi_U(v)=w/2$. Hence

$$
[u]^2\ \longmapsto\ \frac14[w]^2,\qquad
[u\wedge v]^2\ \longmapsto\ 0
$$

Area vanishes when the plane is projected onto a line. The evaluation of the first form changes from $1$ to $1/2$.

> [!note] Forms and their evaluations
> From $u=s+r$, where $s=w/2$ and $s\cdot r=0$, we obtain
>
> $$
> [u]^2=[s]^2+[s,r]+[r,s]+[r]^2
> $$
>
> The mixed forms $[s,r]$ and $[r,s]$ do not vanish. Their metric evaluations are zero. Thus the numerical equality $u^2=s^2+r^2$ does not imply the equality of forms $[u]^2=[s]^2+[r]^2$.

## Coordinates in the isotropic extension

In this section, use the direct notation from the [[The Null Vector, Isotropic Representation, and the Boundary#Local points|note on the isotropic model]]: local points $x,p_i,q$ are themselves elements of the extension, with $x^2=0$ and $x\cdot z=1$. A linear combination of unit weight can be nonlocal; its center is selected by $\pi(p)=p-p^2z/2$. The preceding sections used ordinary affine notation; here we explicitly distinguish a linear combination from its local center.

Let local points $p_0,\ldots,p_k$ have affinely independent Euclidean coordinates. Consider

$$
S=\operatorname{span}(z,p_0,\ldots,p_k)
$$

The metric restricted to $S$ is nondegenerate. Indeed, an element of $S$ orthogonal to all of $S$ is, by orthogonality to $z$, expressible using $z$ and the differences $p_i-p_0$. Orthogonality to these differences and positive definiteness of the displacement metric leave only a multiple of $z$; orthogonality to $p_0$ makes it zero.

Hence the orthogonal projection $\widehat x=\pi_S(x)$ exists and is unique. It has the expression

$$
\widehat x=w_xz+\sum_{i=0}^k\beta^i p_i,\qquad
\sum_{i=0}^k\beta^i=1
$$

The coefficient sum follows from $\widehat x\cdot z=x\cdot z=1$. The coefficient $w_x$ of $z$ is the **orbital relative to the chosen extended basis**. It is a bi-coordinate; the di-coordinate relative to $z$ is $1$.

**Proposition.** Let $q$ be the nearest local point in the Euclidean affine hull of $p_0,\ldots,p_k$. Then

$$
q=\pi\left(\sum_i\beta^i p_i\right),\qquad
\widehat x=q-\frac{(x-q)^2}{2}z,\qquad
\widehat x^2=-(x-q)^2
\tag{9}
$$

The coefficients $\beta^i$ give the affine coordinates of the center $q$; the linear combination in parentheses need not itself be local.

> [!proof]- Proof
> Write $\delta=(x-q)^2$ for the squared distance from $x$ to $q$. The Pythagorean theorem in Euclidean coordinates gives $(x-p_i)^2=(q-p_i)^2+\delta$. By the distance formula for local points,
>
> $$
> x\cdot p_i=q\cdot p_i-\frac{\delta}{2}
> $$
>
> Thus $q-\delta z/2$ has the same di-coordinates relative to $p_i,z$ as $x$. This element belongs to $S$, since $q$ differs from a normalized linear combination of the $p_i$ only by a multiple of $z$. Uniqueness of orthogonal projection gives $\widehat x=q-\delta z/2$. Comparing the coefficients of $p_i$ gives the first formula in (9), and expanding the square gives the last. $\square$

The operations $\pi_S$ and $\pi$ differ: the former is linear orthogonal projection onto $S$, while the latter selects the local center by correction along $z$. In particular, $\pi(\widehat x)=q$.

### The linear midpoint and its local center

For our path, choose orthogonal unit coordinate directions $u_0,v_0$. Then

$$
a=o,\qquad b=o+u_0-\frac12z,\qquad c=o+u_0+v_0-z
$$

The subscripts distinguish these directions from the vertex differences $u=b-a$, $v=c-b$ in the preceding sections. The linear midpoint $p=(a+c)/2$ has square

$$
p^2=\frac12a^2+\frac12c^2-\frac14(c-a)^2=-\frac12
$$

Its local center $q=\pi(p)=(a+c)/2+z/4$ is the nearest point on the line $ac$ to $b$. Since $(b-q)^2=1/2$, formula (9) gives

$$
\widehat b=\pi_S(b)=q-\frac14z=\frac{a+c}{2}=p
$$

The equality of the orthogonal projection and the linear midpoint is specific to this example. Coordinates are listed in the order $(z,a,c)$:

| Object | Bi-coordinates in $(z,a,c)$ | Di-coordinates relative to $(z,a,c)$ | Metric square |
| --- | --- | --- | --- |
| Local point $b$ | No expansion in this sub-basis | $(1,-1/2,-1/2)$ | $0$ |
| Orthogonal projection $\widehat b=p$ | $(0,1/2,1/2)$ | $(1,-1/2,-1/2)$ | $-1/2$ |
| Local center $q=\pi(p)$ | $(1/4,1/2,1/2)$ | $(1,-1/4,-1/4)$ | $0$ |

A **sub-basis** is a selected part of a full basis generating its own subspace. The elements $b$ and $\widehat b$ have the same di-coordinates relative to the sub-basis but different squares. Correction along $z$ returns the local center $q$ and changes the di-coordinates relative to $a,c$.

## When the construction needs qualification

In the positive definite space $W$, every subspace admits a unique orthogonal projection. The set used to specify it may nevertheless be redundant. For example, $w$ and $2w$ generate the same line, while the expansion $w=\alpha w+\beta(2w)$ allows every pair with $\alpha+2\beta=1$. The projection is unique, but the coefficients on this set are not: it is not a basis.

In an indefinite metric, independence of the basis elements does not guarantee a nondegenerate Gram matrix. For the direction $\mathbb Rz$, the set of all multiples of $z$, the Gram matrix is $(0)$. The projection of $o$ onto it does not exist: $(o-tz)\cdot z=1$ for every $t$. For the original object $z$, however, every $tz$ satisfies the orthogonality condition on the residual. Uniqueness fails as well.

For a disconnected graph, the arguments apply separately to each connected component. The published core does not define a finite resistance metric between different components; using a pseudoinverse matrix alone does not remove this limitation.

These definitions do not require nonnegative bi-coordinates. [[Selected Vertices and the Dirichlet Problem]] derives nonnegativity from the graph properties and proves that influence coefficients equal the bi-coordinates of projections. The geometry of residuals connects this problem to [[Vertex Contraction and Graph Gluing|vertex contraction and graph gluing]].

## Sources and status of the results

The definitions of points, vectors, forms, and metric potentials follow the [[Core specification|core specification]]. The terms “bi-coordinates” and “di-coordinates” are used in the general sense of §3.4 of Dmitry Malyugin's article *On the Properties of Affine Metric Spaces*, version 1.11, 2018–2021: expansion coefficients and metrically dual coordinates. Barycentric descriptions of points are treated as a special case. The term “frame” and the quadratic form decomposition were checked against Dmitry Malyugin's article *Foundations of Polyform Algebra*, sections “Frames” and “Forms of Frames”. The distinction from the external use of the word *frame* follows [2].

The internal notes “The Null Vector and Coordinates” and “Graph Subspaces” were also consulted. Orthogonal projection in the extension is explicitly distinguished from selection of the local center.

The relation between the two kinds of coordinates, the reciprocal basis, and orthogonal projection are standard constructions of linear algebra. This note gives their derivations and expressions through PMG forms and potentials. The quadratic and polar decompositions (2), (3) are proved by bilinearity. The Laplacian of a frame is the name given here to its difference part; negative couplings explicitly require an algebraic extension of the core graph model. The metric interpretation in terms of the center and moment of inertia is compared with the known identities in [1]. Formulas (8) and (9) are also proved in the text. The examples are calculated directly; the potentials on the path are calculated by multiplying forms, independently of the geometric calculation.

The reciprocal basis, projections, and coordinate table were checked using exact rational arithmetic. Formula (9) was compared with a direct solution of the Gram system, and formula (8) was checked on a nonorthogonal basis of a plane in three-dimensional space. The quadratic and polar decompositions were also checked as equalities of coefficients of every form $[a_i,a_j]$, including frames with negative coefficients and zero coefficient sum. No working conjectures are included in this note.

1. Havel, T. F. [Heron’s Formula in Higher Dimensions](https://doi.org/10.1007/s00006-023-01305-8). *Advances in Applied Clifford Algebras*, 34, 9 (2024), §2. Lagrange and Huygens-Leibniz identities for weighted centers.
2. Casazza, P. G.; Lynch, R. G. [A brief introduction to Hilbert space frame theory and its applications](https://arxiv.org/abs/1509.07347). The use of the term *frame* for a family of vectors in a Hilbert space.

