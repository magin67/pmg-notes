---
title: Core Specification of PMG
date: 2026-10-09
updated: 2026-10-25
revision: 9
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-core-specification
lang: en
description: "Definitions, notation, and fundamental identities of the PMG core: exterior objects, boundaries, forms, the resistance metric, the Laplacian exponential, and the balanced extension."
order: 1
---

This specification records the definitions, notation, and fundamental identities of the Polyform Metric Geometry (PMG) core presented in the [[PMG Introductory Series|introductory series]]. It provides a reference for conventions and the conditions under which formulas apply. Proofs, examples, and references appear in the corresponding notes of the series.

## Purpose and scope

The algebraic construction is over the real numbers. The underlying space has a finite basis of vertices; forms are defined before a graph or metric is chosen.

The main graph model is a finite connected undirected graph without loops, with $n\ge2$ vertices. Existing edges have positive conductances; absent couplings have zero conductance. Parallel conductors between the same pair of vertices are represented by their total conductance. The balanced model and its differences are explicitly stated in [[Core specification#The balanced extension|the balanced extension section]].

Connectedness is required for the resistance metric on the entire space of affine vectors and for normalization by the spanning-tree coefficient. The algebra of forms, the Laplacian exponential, and the forest expansion also apply to disconnected graphs. That case is specified separately.

**Status of the statements.** Definitions and conventions specify the language used. Claims about its properties are proved in the introductory series, and the balanced extension in [[Balanced Graphs]]; links follow the relevant sections. Working conjectures are not part of the core.

## The underlying space, points, and vectors

Let $V$ be a real vector space with a linearly independent basis $a_1,\ldots,a_n$. The basis elements represent graph vertices. The coefficient-sum functional is

$$
\varepsilon\left(\sum_i x_i a_i\right)=\sum_i x_i
$$

Its value is called the affine weight.

> [!info] Points and affine vectors
> **Definition.** An element $x\in V$ is a point if $\varepsilon(x)=1$. The space of affine vectors is
>
> $$
> W=\ker\varepsilon=\left\{\sum_i u_i a_i:\sum_i u_i=0\right\},\qquad \dim W=n-1
> $$

Unless otherwise specified, a vector below means an affine vector in $W$. An arbitrary element of $V$ need be neither a point nor an affine vector. The difference of two points belongs to $W$; the sum of a point and an affine vector is a point.

For an ordered pair of vertices, the notation is

$$
a_{ij}=a_j-a_i=(a_i a_j)=(ij)
$$

The vector $a_{ij}$ is directed from $a_i$ to $a_j$, and $a_{ji}=-a_{ij}$. Its definition does not require an edge between the vertices.

Formal basis vertices in $V$ are distinct from the centered position vectors of a Euclidean realization. The linear independence of $a_1,\ldots,a_n$ concerns the formal space, not the centered position vectors, whose sum is zero.

Source: [[Basic Objects and Operations of Polyform Algebra#Points and affine vectors|points and affine vectors]].

## Exterior objects and boundaries

### The exterior product and grade

**Definition.** The space $\Lambda^kV$ consists of linear combinations of exterior products of $k$ elements of $V$. Its elements are called exterior objects of grade $k$. An object is decomposable if it can be expressed as a single exterior product.

Juxtaposition of exterior objects denotes their exterior product: $XY=X\wedge Y$. The inner product is written explicitly as $X\cdot Y$, and the exterior self-product as $X\wedge X$, since $X^2$ denotes the norm. The exterior product is bilinear and associative. For homogeneous objects $X\in\Lambda^kV$ and $Y\in\Lambda^mV$,

$$
XY=(-1)^{km}YX
$$

In particular, $x\wedge x=0$ for $x\in V$. The scalar $1\in\Lambda^0V$ is the identity for the exterior product. A nonzero product of objects of grades $k$ and $m$ has grade $k+m$.

An oriented simplex is written as

$$
[a_{i_1}\ldots a_{i_k}]=a_{i_1}\cdots a_{i_k}
$$

Its grade is the number of vertices, one greater than the usual geometric dimension of a nondegenerate simplex. The term “order” may be used as a synonym for grade when the object is explicitly specified. This specification consistently uses “grade”.

### The boundary operator

> [!info] Boundary operator
> **Definition.** The linear operator $\partial$ is specified by $\partial1=0$, $\partial a_i=1$, and
>
> $$
> \partial[a_{i_1}\ldots a_{i_k}]
> =\sum_{r=1}^k(-1)^{r-1}[a_{i_1}\ldots\widehat{a_{i_r}}\ldots a_{i_k}]
> $$
>
> The hat denotes omission. The empty exterior product is $1$.

On $V$, the operator agrees with the affine-weight functional: $\partial x=\varepsilon(x)$. For homogeneous $X$ of grade $k$,

$$
\partial^2=0,\qquad
\partial(XY)=(\partial X)Y+(-1)^kX(\partial Y)
$$

Simplex boundaries are denoted by parentheses:

$$
(ab)=b-a,\qquad
(abc)=[bc]-[ac]+[ab]
$$

> [!info] The space of boundaries
> **Proposition.** For every $0\le k\le n$, the space of boundaries of grade $k$ equals the kernel of $\partial$ in that grade and equals $\Lambda^kW$:
>
> $$
> \operatorname{im}(\partial:\Lambda^{k+1}V\to\Lambda^kV)
> =\ker(\partial|_{\Lambda^kV})=\Lambda^kW
> $$
>
> In grade $0$, every scalar is a boundary. In grade $n$, this space is zero.

Thus boundaries form a subalgebra of the exterior algebra. Nonzero boundaries have grades from $0$ to $n-1$. Affine vectors are boundaries of grade $1$.

### Products of simplex boundaries

For points $p,a_1,\ldots,a_r$,

$$
(pa_1\ldots a_r)=(a_1-p)\cdots(a_r-p)
$$

The following rules apply to boundaries of simplices on distinct basis vertices, with each simplex containing at least two vertices.

- If the only shared vertex $p$ is listed first in both simplices, then

$$
(pa_1\ldots a_r)(pb_1\ldots b_s)=(pa_1\ldots a_r b_1\ldots b_s)
$$

- Other vertex orders require the corresponding orientation signs.
- If at least two vertices are shared, the product is zero.
- If the vertex sets are disjoint, the product is nonzero and remains a product of two boundaries.

Products of arbitrary linear combinations are evaluated by bilinearity. The list of vertices appearing in a particular expression for such a combination does not by itself determine a merging or vanishing rule.

**Proposition.** The product of the vectors of selected edges is nonzero if and only if the edges form a forest. For a tree, this product equals the simplex boundary on its vertices up to sign; for a forest, it is the product of its component boundaries. An isolated vertex contributes the factor $\partial a_i=1$.

Sources: [[Basic Objects and Operations of Polyform Algebra#The boundary operator|the boundary operator]], [[Basic Objects and Operations of Polyform Algebra#Boundaries and exterior powers of affine vectors|the space of boundaries]], and [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|products of boundaries]].

## Forms and polyform algebra

### Formal forms

> [!info] Forms of one grade
> **Definition.** For $X,Y\in\Lambda^kV$, introduce symbols $[X,Y]$ subject only to bilinearity in their arguments. These symbols generate the space of forms of grade $k$. Symmetry $[X,Y]=[Y,X]$ is not assumed.

A form is a formal object. This definition does not specify a numerical bilinear function on $V$ and requires no inner product. Both arguments have the same grade.

The quadratic form, transpose, and polar form are defined by

$$
[X]^2=[X,X],\qquad
[X,Y]^{\mathsf T}=[Y,X],\qquad
\{X,Y\}=[X,Y]+[Y,X]
$$

Transposition extends linearly. The polar form is used without a factor of $1/2$; in particular,

$$
[X+Y]^2=[X]^2+\{X,Y\}+[Y]^2
$$

The notation $[X]^2$ denotes neither $X\wedge X$ nor a numerical norm. For nonzero $X$, the form $[X]^2$ is nonzero, and $[-X]^2=[X]^2$.

### Polyforms and their product

**Definition.** A polyform is a finite linear combination of forms, possibly of different grades. It is homogeneous if all its terms have the same grade. In the decomposition $P=\sum_{k=0}^nP_k$, the term $P_k$ is called a grade component.

> [!info] Product of forms
> **Definition.** For forms of grades $k$ and $m$, set
>
> $$
> [X,Y][A,B]=[XA,YB]
> $$
>
> The product extends bilinearly to polyforms. Its identity is the grade-$0$ form $e=[1,1]$.

**Proposition.** The product of forms is associative, distributive, and commutative. Grades add in nonzero products of homogeneous forms. On exchanging the factors, the two signs $(-1)^{km}$ from the exterior arguments cancel.

The scalar $1$ is the identity for exterior objects, whereas $e$ is the identity for polyforms. For scalars $s,t$, one has $[s,t]=st\,e$.

For quadratic forms,

$$
[X]^2[A]^2=[XA]^2,\qquad
([v]^2)^2=0\quad(v\in V)
\tag{1}
$$

The last equality does not extend to an arbitrary sum of forms or to every higher-grade form. For independent $u,v\in W$, for example,

$$
\bigl([u]^2+[v]^2\bigr)^2=2[uv]^2\ne0
$$

### Forms on boundaries

**Definition.** Forms with arguments $X,Y\in\Lambda^kW$ and their linear combinations form the subalgebra of forms on boundaries. Its grades range from $0$ to $n-1$, and its identity is also $e$.

For a polyform $P$ in this subalgebra with $P_0=0$, one has $P^n=0$. In the full algebra of forms on $V$, a polyform without a grade-$0$ component satisfies $P^{n+1}=0$.

Sources: [[Basic Objects and Operations of Polyform Algebra#Forms: bilinearity and basic operations|formal forms]], [[Basic Objects and Operations of Polyform Algebra#Polyforms and the product of forms|the polyform product]], and [[Basic Objects and Operations of Polyform Algebra#Nilpotence and forms on boundaries|nilpotence]].

## The graph and representations of its Laplacian

For an undirected graph $G$, conductances satisfy

$$
c_{ij}=c_{ji}\ge0,\qquad c_{ii}=0,\qquad d_i=\sum_jc_{ij}
$$

> [!info] Laplacian
> **Definition.** The matrix and polyform representations of the Laplacian are
>
> $$
> L_{ii}=d_i,\qquad L_{ij}=-c_{ij}\quad(i\ne j),\qquad
> L=\sum_{i<j}c_{ij}[a_{ij}]^2
> \tag{2}
> $$

The polyform $L$ has grade $1$ and belongs to the subalgebra of forms on boundaries. Its coefficient matrix in the forms $[a_i,a_j]$ is $\mathbf L$:

$$
L=\sum_{i,j}L_{ij}[a_i,a_j]
$$

The polyform product differs from matrix multiplication. In particular, $L^2$ and $\mathbf L^2$ are different objects.

For a connected graph, $\ker\mathbf L=\operatorname{span}\{\mathbf1\}$, and the restriction of $\mathbf L$ to the coordinate subspace

$$
H=\{\mathbf u\in\mathbb R^n:\mathbf1^{\mathsf T}\mathbf u=0\}
$$

is positive definite. A column $\mathbf u\in H$ represents the affine vector $u=\sum_i u_i a_i\in W$.

Sources: [[Laplacian - graph, electrical network and quadratic form]] and [[Basic Objects and Operations of Polyform Algebra#The polyform representation of the Laplacian|the polyform representation of the Laplacian]].

## The resistance metric

### The Green matrix and resistances

> [!info] Green matrix
> **Definition.** For a connected graph, $\mathbf{Gr}$ inverts $\mathbf L$ on $H$ and vanishes on constant columns. Equivalently, $\mathbf{Gr}=\mathbf L^+$, where $+$ denotes the Moore-Penrose pseudoinverse.

For the centering projector $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$,

$$
\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J,\qquad
\mathbf{Gr}\mathbf1=0,\qquad \mathbf{Gr}^+=\mathbf L
$$

**Definition.** The resistance inner product on $W$ and the effective resistances are given by

$$
u\cdot v=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v,\qquad
R_{ij}=a_{ij}\cdot a_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
\tag{3}
$$

This inner product is positive definite on $W$. In the electrical interpretation, when unit current enters at vertex $i$ and leaves at $j$, one has $R_{ij}=\varphi_i-\varphi_j$, where $\varphi_i$ is the electrical potential at vertex $i$.

For the centroid $b=n^{-1}\sum_i a_i$, the identity $\mathbf{Gr}\mathbf1=0$ gives

$$
\mathrm{Gr}_{ij}=(b-a_i)\cdot(b-a_j)
$$

In the symmetric model, the Green matrix is the Gram matrix of the vectors from the vertices to the centroid. In a balanced graph, directional argument order gives the transposed matrix, as specified in the balanced extension. The notation $\mathbf G=(g_{ij})$ is reserved for the Gram matrix of explicitly chosen elements, with $g_{ij}$ denoting their inner products. The expressions $\mathbf{Gr}$ and $\mathbf L^+$ denote the same object: the former names it, while the latter specifies how it is obtained.

For two vertex pairs,

$$
a_{ij}\cdot a_{kl}=\frac{R_{il}+R_{jk}-R_{ik}-R_{jl}}2
$$

### The distance operator

**Definition.** For a symmetric matrix $A$, set

$$
\mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}
$$

Writing $\mathbf R=(R_{ij})$, the transformations between representations are

$$
\mathbf R=\mathcal D(\mathbf{Gr}),\qquad
\mathbf{Gr}=-\frac12\mathbf J\mathbf R\mathbf J,\qquad
\mathbf L=\left(-\frac12\mathbf J\mathbf R\mathbf J\right)^+
$$

These reconstruction formulas use symmetry of the Green matrix. The distance transformation and double centering are linear operations, distinct from pseudoinversion. An arbitrary squared Euclidean distance matrix need not be the resistance matrix of a graph with nonnegative conductances. The recovered $\mathbf L$ must satisfy the Laplacian conditions in (2).

**Proposition.** The vertices of a connected graph form a nondegenerate resistance simplex of dimension $n-1$, in which $R_{ij}$ is the squared Euclidean distance. Both $R_{ij}$ and $\sqrt{R_{ij}}$ define metrics on the vertices; the Euclidean length in this realization is $\sqrt{R_{ij}}$.

Sources: [[Effective Resistance and Graph Geometry]], [[Inner Product of Graph Vectors]], and [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

## Metrics of higher-grade objects

Let $W$ carry a positive-definite inner product. The graph model uses (3).

> [!info] Induced metric
> **Definition.** For decomposable objects of the same grade,
>
> $$
> X=u_1\cdots u_k,\qquad Y=v_1\cdots v_k
> $$
>
> define their inner product by the mixed Gram determinant:
>
> $$
> X\cdot Y=\det(u_r\cdot v_s)_{r,s=1}^k
> $$
>
> Extend this rule to linear combinations by bilinearity. In grade $0$, it is ordinary scalar multiplication.

**Proposition.** This extension is well-defined and positive definite on each $\Lambda^kW$. This revision does not introduce an inner product between objects of different grades.

**Norm convention.** In PMG, the norm is the quadratic quantity $X^2=X\cdot X$. In the resistance metric it is the resistance norm. For $X^2\ge0$, its square root is called the **linear norm**, denoted $\|X\|=\sqrt{X^2}$. Thus, for a boundary $X$,

$$
X^2=X\cdot X=\|X\|^2
$$

This number is distinct from the formal form $[X]^2$ and the exterior product $X\wedge X$. For decomposable $X$, it is the squared volume of a parallelotope. For an arbitrary object, it is defined by bilinear extension and requires no representation by a single parallelotope.

For a simplex on points $a_0,\ldots,a_k$, the squared geometric volume is

$$
V_{a_0\ldots a_k}^2=\frac{(a_0\ldots a_k)^2}{(k!)^2}
$$

This formula uses the norm of the boundary and does not define the norm of the formal simplex $[a_0\ldots a_k]\in\Lambda^{k+1}V$.

**Definition.** Numerical metric evaluation of a form on boundaries is specified by $[X,Y]\mapsto X\cdot Y$ and extended linearly within each grade. In particular, $[X]^2$ evaluates to $X^2$, $\{X,Y\}/2$ to $X\cdot Y$, and $e$ to $1$.

The evaluation of a product of forms generally differs from the product of their evaluations. For $u,v\in W$, for example,

$$
\text{evaluation of }[u]^2[v]^2=u^2v^2-(u\cdot v)^2
$$

Source: [[Metric of Higher-Grade Objects]]. The relation to geometric volumes is also discussed in [[From Lengths to Areas and Volumes]].

## The metric polyform

> [!info] Laplacian exponential
> **Definition.** The metric polyform of a graph is
>
> $$
> M_G=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!},\qquad L^0=e
> $$
>
> Powers use the product of forms. The series terminates because $L^n=0$.

The matrix exponential $\exp\mathbf L$ uses a different multiplication and is not $M_G$. Commutativity of forms and (1) give

$$
M_G=\prod_{\{i,j\}\in E}\bigl(e+c_{ij}[a_{ij}]^2\bigr)
$$

The multiplier $e+c_{ij}[a_{ij}]^2$ is called an edge factor. The form $[a_{ij}]^2$, its weighted contribution $c_{ij}[a_{ij}]^2$, and the edge factor are distinct objects.

### Addition, deletion, and the inverse exponential

For $p=[a_{ij}]^2$, we have $p^2=0$, so

$$
(e+cp)^{-1}=e-cp,\qquad
\exp(L+tp)=M_G(e+tp)
$$

If the conductance of the pair $ij$ changes by $t$, this adds conductance when $t>0$ and deletes an existing edge when $t=-c_{ij}$. The graph interpretation requires $c_{ij}+t\ge0$. The inverse exponential is

$$
M_G^{-1}=\exp(-L)
=\prod_{\{i,j\}\in E}\bigl(e-c_{ij}[a_{ij}]^2\bigr)
=\sum_{k=0}^{n-1}(-1)^kM_k
$$

Here $M_k=L^k/k!$. Invertibility refers to the polyform algebra and also holds for disconnected graphs. Sources: [[Laplacian Exponential#Adding and deleting an edge|edge operations]] and [[Laplacian Exponential#The inverse exponential|the inverse exponential]].

### The forest expansion

For an edge set $F$, choose any order and orientations and set

$$
B_F=\bigwedge_{\{i,j\}\in F}a_{ij},\qquad
w(F)=\prod_{\{i,j\}\in F}c_{ij}
$$

For the empty set, $B_F=1$ and $w(F)=1$. The quadratic form $[B_F]^2$ is independent of the chosen order and orientations.

> [!info] Grade components
> **Proposition.** For $0\le k\le n-1$,
>
> $$
> M_k=\frac{L^k}{k!}
> =\sum_{\substack{F\subseteq E\text{ is a forest}\\|F|=k}}w(F)[B_F]^2
> \tag{4}
> $$
>
> Each forest includes all vertices, including isolated ones, and has $n-k$ components.

Forest forms may satisfy linear relations. The sum of weights of forests of a given size therefore refers to expansion (4), not to an arbitrary expression for the same grade component.

Sources: [[Laplacian Exponential#The exponential in the algebra of forms|the exponential]] and [[Laplacian Exponential#Grade components and spanning forests|the forest expansion]].

## The spanning-tree form and coefficient extraction

> [!info] Spanning-tree form
> **Definition.** On a fixed vertex set, define
>
> $$
> T_n=[(a_1\ldots a_n)]^2
> $$
>
> It spans the one-dimensional space of forms on boundaries of grade $n-1$. Permuting the vertices does not change $T_n$.

**Definition.** For any polyform $P$ on boundaries, the functional $\tau(P)$ is defined by

$$
P_{n-1}=\tau(P)T_n
\tag{5}
$$

The functional is linear. If the grade-$(n-1)$ component is absent, its value is zero. The form $T_n$ is fixed by the original vertex set and is not replaced when passing from $P$ to another polyform or product.

**Proposition.** For a graph's metric polyform,

$$
\tau(M_G)=\tau(G)=\sum_{T\text{ is a spanning tree}}\prod_{\{i,j\}\in T}c_{ij},\qquad
M_{n-1}=\tau(G)T_n
$$

In the public series, $\tau(G)$ is called the **spanning-tree coefficient**. For unit conductances, it is the spanning-tree count. The earlier Russian term “остовное число” in the weighted setting refers to this same coefficient and does not assert that it is an integer.

For a connected graph, $\tau(G)>0$. By the matrix-tree theorem, it equals the determinant of any reduced Laplacian. Consequently, $L^{n-1}\ne0$, and the highest nonzero grade of $M_G$ is $n-1$.

In this model, $T_n$ is also called the top-grade form; $M_{n-1}$ is the top-grade component, and $M_{n-2}$ the next-to-top-grade component. These names do not change the definition of the functional in (5).

Sources: [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|the spanning-tree form]] and [[From Lengths to Areas and Volumes|the matrix-tree theorem and resistance-simplex volume]].

## Potential and the metric identity

> [!info] Potential of a form
> **Definition.** For a fixed metric polyform $M=M_G$ and a form $f$ on boundaries,
>
> $$
> u_M(f)=\tau(Mf),\qquad u_M(e)=\tau(M)
> \tag{6}
> $$
>
> If $\tau(M)\ne0$, the normalized potential is
>
> $$
> \frac{u_M(f)}{u_M(e)}=\frac{\tau(Mf)}{\tau(M)}
> \tag{7}
> $$

For fixed $M$, both maps are linear in $f$. Formula (6) extends to polyforms on boundaries. For a homogeneous form of grade $k$, only the complementary grade of the exponential contributes:

$$
u_M(f)=\tau(M_{n-1-k}f)
$$

> [!info] Metric identity
> **Theorem.** For a connected graph with nonnegative conductances and any $X,Y\in\Lambda^kW$, $0\le k\le n-1$,
>
> $$
> \frac{\tau(M_G[X,Y])}{\tau(M_G)}=X\cdot Y,\qquad
> \frac{\tau(M_G[X]^2)}{\tau(M_G)}=X^2
> $$
>
> The right-hand sides use the resistance metric and its induced extension. The identities also hold for nondecomposable exterior objects.

In particular,

$$
u_M([a_{ij}]^2)=\tau(G)R_{ij},\qquad
\frac{u_M(\{X,Y\}/2)}{u_M(e)}=X\cdot Y
$$

**Terminological convention.** The normalized potential is called the norm of a form. For a quadratic form $[X]^2$, it equals the norm of its argument $X^2=X\cdot X$. For a general form, it is a linear evaluation that may have either sign. The notation $\|X\|$ denotes the linear norm; the normalized potential is written as the ratio in (7).

The potential of a form, $u_M(f)$, differs from the electrical potential $\varphi_i$ at a vertex. The latter depends on applied currents or prescribed conditions, whereas $u_M(f)$ is determined by the fixed $M$ and $f$.

Sources: [[Laplacian Exponential#The potential of a form|the potential of a form]], [[Laplacian Exponential#A general lemma on the top-grade coefficient|the determinant lemma]], and [[Laplacian Exponential#Agreement with the resistance metric|the metric identity]].

## Variations of couplings

### A single variation

For any $v\in W$ and real $t$, (1) implies the algebraic identity

$$
\exp(L+t[v]^2)=M_G(e+t[v]^2)
\tag{8}
$$

Consequently,

$$
\tau\bigl(\exp(L+t[v]^2)\bigr)=\tau(M_G)+t\,u_{M_G}([v]^2)
\tag{9}
$$

For $v=a_{ij}$, this changes the conductance of pair $ij$ by $t$. It is admissible in the main graph model if $c_{ij}+t\ge0$. Then

$$
\tau(G')=\tau(G)(1+tR_{ij})
$$

The formula remains valid if the final graph becomes disconnected. For nonnegative final conductances, connectedness is equivalent to $1+tR_{ij}>0$.

For arbitrary $v=\sum_i v_i a_i\in W$, the matrix update is $t\mathbf v\mathbf v^{\mathsf T}$. It changes several pair coefficients according to

$$
c'_{ij}=c_{ij}-t v_i v_j\qquad(i\ne j)
$$

Such a variation need not represent the addition of a single edge. A graph interpretation requires checking that every $c'_{ij}$ is nonnegative. Algebraic identities (8)-(9) do not require this check.

### Several variations

For $v_1,\ldots,v_m\in W$ and real $t_1,\ldots,t_m$,

$$
\exp\left(L+\sum_{\alpha=1}^m t_\alpha[v_\alpha]^2\right)
=M_G\prod_{\alpha=1}^m(e+t_\alpha[v_\alpha]^2)
\tag{10}
$$

Let $g_{\alpha\beta}=v_\alpha\cdot v_\beta,\quad \mathbf G=(g_{\alpha\beta})$ and $D=\operatorname{diag}(t_1,\ldots,t_m)$. For a connected initial graph,

$$
\frac{\tau\left(\exp\left(L+\sum_\alpha t_\alpha[v_\alpha]^2\right)\right)}{\tau(M_G)}
=\det(I_m+D\mathbf G)
\tag{11}
$$

The coefficient of $\prod_{\alpha\in S}t_\alpha$ is the principal minor $\det\mathbf G_S$. It is the norm of the exterior product of the selected vectors. For the empty set, both the product and determinant are $1$.

For vectors of distinct vertex pairs, (10)-(11) describe joint conductance variations. The determinant formula remains meaningful for a disconnected final graph; inverse-update formulas for its Green matrix on the original subspace require connectedness to be preserved.

Sources: [[Variation of a Single Edge]], [[Varying several couplings together]], and [[Laplacian Exponential#Algebraic variation and edge addition|algebraic variation]].

## The balanced extension

This section extends the graph model to finite loopless balanced digraphs with nonnegative arc weights. The algebra of forms and its product are unchanged: symmetry of the arguments was never assumed. Graph and metric statements in the other sections use the symmetric model unless an extension is explicitly stated. Proofs and examples are collected in [[Balanced Graphs]].

### The Laplacian, balance, and rooted potentials

Write $f_{ij}$ for the weight of arc $i\to j$. Use the outgoing Laplacian convention:

$$
L_{ii}=\sum_jf_{ij},\qquad L_{ij}=-f_{ij}\quad(i\ne j),\qquad
\mathbf L\mathbf1=0
$$

**Definition.** A graph is balanced if $\sum_jf_{ij}=\sum_jf_{ji}$ at every vertex. Equivalently, $\mathbf1^{\mathsf T}\mathbf L=0$. PMG uses the Russian abbreviation **балграф**. An undirected graph corresponds to $f_{ij}=f_{ji}$ and is a special case.

With $h=n^{-1}\sum_i a_i$ and $x_i=a_i-h$, the canonical centered representation is

$$
L=\sum_{i,j}L_{ij}[x_i,x_j]
$$

Because $\sum_i x_i=0$, arbitrary coefficients in this expression are not unique. The canonical choice fixes the centroid and the unique coefficient matrix with zero row and column sums. Balance places $L$ in the boundary-form subalgebra; the condition $f_{ij}\ge0$ is checked separately.

**Definition.** The spanning-tree potential of vertex $i$ is $\tau_i=\det\mathbf L_{\widehat i,\widehat i}$. It is the sum of weights of spanning arborescences directed toward root $i$. For the outgoing Laplacian, $\mathbf L^{\mathsf T}\boldsymbol\tau=0$.

A connected balanced graph with nonnegative weights is strongly connected, and all $\tau_i$ equal one positive spanning-tree coefficient $\tau$. This is the sum toward one fixed root; summing over all roots gives $n\tau$. Conversely, equality of all $\tau_i$ to one positive number implies balance. Equality of zero minors provides no such criterion.

The exponential and its top component retain the form

$$
M=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!},\qquad
M_{n-1}=\tau T_n
$$

Sources: [[Balanced Graphs and Spanning-Tree Potentials]], [[The Bilinear Laplacian of a Balanced Graph]], and [[The Laplacian Exponential of a Balanced Graph]]. Throughout the rest of this section, the graph is connected.

### Directional pairing and resistances

The matrix $\mathbf{Gr}=\mathbf L^+$ inverts $\mathbf L$ on $H$; the identities $\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J$ and zero row and column sums remain valid. Write $P_M(F)=\tau(MF)/\tau(M)$ for the normalized potential.

**Definition.** For $u,v\in W$, use the source-receiver argument order:

$$
\boxed{\beta(u,v)=P_M([u,v])
=u^{\mathrm{out}}\cdot v^{\mathrm{in}}
=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u}
$$

Argument order matters. This is a bilinear pairing, generally nonsymmetric; the ordinary Euclidean inner product is its symmetric part

$$
g(u,v)=\frac{\beta(u,v)+\beta(v,u)}2,\qquad
\gamma(u,v)=\frac{\beta(u,v)-\beta(v,u)}2
$$

The form $g$ is positive definite on $W$. The formal circulation $\omega(u,v)=[u,v]-[v,u]$ has PMG grade one. For three points, $w(abc)=\omega(b-a,c-a)$, and its numerical evaluation is $\chi_{abc}=P_M(w(abc))=2\gamma(b-a,c-a)$. Distinguish the form from its potential.

**Definition.** One-way resistance is defined algebraically:

$$
\boxed{r_{ij}=P_M([a_j-h,a_j-a_i])
=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}},\qquad
R_{ij}=r_{ij}+r_{ji}
$$

It is defined whether or not the arc exists and can be asymmetric even in an undirected graph. The notation $r_{ij}$ is not used for the resistance $1/c_{ij}$ of an individual edge. In the continuous-time Markov model with generator $-\mathbf L$, the quantity $nr_{ij}$ is interpreted as the mean hitting time; this interpretation is not part of the resistance definition.

The matrix $\mathbf r=(r_{ij})$ determines the entire Laplacian:

$$
\mathbf{Gr}=-\mathbf J\mathbf r,\qquad
\mathbf L=\mathbf{Gr}^{+}
$$

The symmetric matrix $\mathbf R=(R_{ij})$ determines only the symmetric part of the Green matrix:

$$
-\frac12\mathbf J\mathbf R\mathbf J
=\frac{\mathbf{Gr}+\mathbf{Gr}^{\mathsf T}}2
$$

Thus $\mathbf R$ alone generally cannot reconstruct the original balanced graph. Directional data are needed for the full pairing. Sources: [[One-Way Resistance and Hitting Times]], [[The Circulation Form]], and [[Resistance Geometry and Circulation]].

### Higher grades and geometric interpretation

For decomposable exterior elements, the normalized potential is determined by the full bilinear pairing:

$$
P_M([u_1\cdots u_k,v_1\cdots v_k])
=\det\bigl(\beta(u_r,v_s)\bigr)_{r,s=1}^k
$$

Extend the rule to linear combinations by bilinearity. It cannot be replaced by a determinant using only the symmetric part $g$. For example, if $A_{abc}$ is the triangle's area in the Euclidean metric $g$, then

$$
P_M([(abc)]^2)=4A_{abc}^2+\frac{\chi_{abc}^2}{4}
$$

Identifying the potential of a quadratic boundary form with a squared Euclidean volume therefore requires the symmetric case or a separate check. The definition of a form norm as its normalized potential is retained. The determinant rule and the three-vertex identity are proved in the [[Resistance Geometry and Circulation#Three-vertex resistance|three-vertex resistance section]].

### The Gram matrix, coordinates, and isotropic extension

With the chosen role order, $\beta(x_i,x_j)=\mathrm{Gr}_{ji}$, so the Gram matrix of centered vectors is $\mathbf{Gr}^{\mathsf T}$. For canonical local vertices, the conditions $a_i^2=0$ and $a_i\cdot h=h\cdot a_i$ give

$$
g_{ij}=a_i^{\mathrm{out}}\cdot a_j^{\mathrm{in}}
=\mathrm{Gr}_{ji}-\frac{q_i+q_j}{2},\qquad
q_i=\mathrm{Gr}_{ii}
$$

Consequently, $\mathbf G=-\mathbf R/2$ holds in the symmetric case; a general balanced graph satisfies $(\mathbf G+\mathbf G^{\mathsf T})/2=-\mathbf R/2$. The centroid condition fixes the freedom in extending the pairing from differences to vertices.

Bi-coordinates remain the expansion coefficients of a specified representative in the basis of its own role. Di-coordinates pair it with the basis of the opposite role:

$$
\mathbf d_{\mathrm{out}}=\mathbf G^{\mathsf T}\mathbf b_{\mathrm{out}},\qquad
\mathbf d_{\mathrm{in}}=\mathbf G\mathbf b_{\mathrm{in}}
$$

The two roles do not give two different expansions of a fixed linear representative. Different coordinate sets can represent one functional by pairing from different sides. This is how the two metric representatives of the sphere arise.

The unit border $\mathbf G_z=\left(\begin{smallmatrix}\mathbf G&\mathbf1\\\mathbf1^{\mathsf T}&0\end{smallmatrix}\right)$ is retained. The vertex block of its inverse is $\mathbf L^{\mathsf T}$, and the corner entry defines the single resistance radius

$$
\rho=(\mathbf G_z^{-1})_{n+1,n+1}>0
$$

This algebraic definition retains PMG's quadratic normalization. Only in the symmetric case does it automatically equal the squared Euclidean circumradius; for a balanced graph, the radius of the Euclidean realization of $g$ may differ. Sources: [[The Gram Matrix and Directional Coordinates of a Balanced Graph]] and [[The Isotropic Space and Sphere of a Balanced Graph]].

The rooted potential $\tau_i$, form potential $u_M(F)$, and electrical potential $\varphi_i$ are different quantities. Their relation after adding one arc and the distinction between two Dirichlet problems are stated in [[Balanced Variations#One-way variation and loss of balance|one-way variation]] and the [[Selected Vertices and the Dirichlet Problem#Two Dirichlet problems in a balanced graph|balanced-graph extension]]. An electrical model of a nonsymmetric Laplacian requires nonreciprocal elements or controlled sources; it is not a network of ordinary resistors.

## Limitations and extensions

### Disconnected graphs

For a graph with $c$ connected components, including isolated vertices, and positive conductances on existing edges,

$$
\deg M_G=\operatorname{rank}\mathbf L=n-c
$$

Here $\deg M_G$ denotes the highest nonzero grade. With $r=n-c$, one has $L^r\ne0$ and $L^{r+1}=0$; when $r=0$, use $L^0=e$.

The highest nonzero component is the quadratic form of the product of component boundaries, multiplied by the product of their spanning-tree coefficients. For an isolated vertex, both its boundary and its spanning-tree coefficient are $1$.

If $c>1$, the coefficient of the fixed $T_n$ is zero. Thus $\tau(M_G)=0$, and normalization (7) does not apply. The number of components is $c=n-\deg M_G$, not the number of terms in a chosen expression for the highest component.

The pseudoinverse $\mathbf L^+$ also exists for a disconnected graph, but it no longer inverts $\mathbf L$ on all of $H$. Formula (3) does not give a finite effective resistance between different components. The resistance metric within each nontrivial component can be considered separately.

Source: [[Laplacian Exponential#Disconnected graphs|disconnected graphs]].

### Scope of the metric model

A metric on $W$ and its exterior powers does not automatically define metric evaluations of forms of points or arbitrary simplices outside the boundary subalgebra. Such evaluations require an additional construction on $V$ or an extension of it.

Algebraic polynomial identities may remain valid for real coupling coefficients of either sign. This does not imply positivity of the metric, an electrical interpretation, positivity of the spanning-tree coefficient, or the connectedness criteria established for nonnegative conductances.

### Thematic extensions

A full treatment of the following thematic extensions requires separate definitions and applicability conditions; this specification records only the explicitly stated conventions:

- the isotropic extension, the distinguished null vector, and bi-coordinates and di-coordinates;
- general unbalanced digraphs and the KVP/KVPOU structural decompositions;
- dual polyforms, cut forms, and the function $\operatorname{dex}$;
- structural identities of partition forms, symmetric polyforms, and their combinatorial coefficients;
- partition toponomes, the second-kind algebra, and further component evaluations;
- metric-value decompositions and interval forms;
- problems with values prescribed on a selected vertex set, including the Dirichlet problem.

Definitions of the isotropic representation and the null vector are given in [[The Null Vector, Isotropic Representation, and the Boundary]], coordinates and frames in [[Projections, Bi-coordinates, and Di-coordinates]], and the problem with prescribed values in [[Selected Vertices and the Dirichlet Problem]]. Their terminology is collected in the [[PMG terminology#Terminology of extensions|glossary of extensions]].

Partition forms and their structural identities are defined in [[Partition Forms and the Tetrahedron Identity]], and symmetric sums and representation sizes in [[Symmetric Polyforms - Types and Normalizations]]. The [[Combinatorial Potentials]] series establishes the combinatorial coefficients of these sums and the distinction between partition counts and forest counts. Its general collection notation is recorded below; terminology from these series is included in the [[PMG terminology|glossary]]. Thematic definitions do not remove the applicability conditions of the base model or the explicitly stated balanced extension.

In this specification, a boundary is an image of $\partial$, equivalently an element of $\Lambda^kW$. A selected vertex set in a Dirichlet problem is not a boundary in this algebraic sense. When using the standard expression “boundary vertices”, the two notions must be explicitly distinguished.

## Principal notation

| Notation | Meaning |
|---|---|
| $V$, $a_i$ | Formal space and its basis vertices |
| $\varepsilon$, $W$ | Affine weight and the space of affine vectors |
| $[a_1\ldots a_k]$ | Simplex of grade $k$ |
| $\partial$, $(a_1\ldots a_k)$ | Boundary operator and simplex boundary |
| $a_{ij}=(ij)$ | The vector $a_j-a_i$ |
| $[X,Y]$, $[X]^2$ | Formal bilinear and quadratic forms |
| $\{X,Y\}$ | Polar form without a factor of $1/2$ |
| $1$, $e=[1,1]$ | Identity for exterior objects and the unit form |
| $XY$ | Exterior product of objects; the exterior self-product is written as $X\wedge X$ |
| $X\cdot Y$, $X^2=\lVert X\rVert^2$ | Numerical inner product and quadratic norm; $\|X\|$ is the linear norm |
| $c_{ij}$, $d_i$ | Conductances and weighted vertex degrees |
| $G$ | Graph |
| $L$, $\mathbf L$ | Laplacian polyform and Laplacian matrix |
| $\mathbf{Gr}=\mathbf L^+$, $\mathbf R$ | Green matrix and resistance matrix |
| $\mathbf G=(g_{ij})$ | Gram matrix of chosen elements; $g_{ij}$ are their inner products |
| $\mathbf G_z$ | In the isotropic extension: the Gram matrix of the vertices together with the null vector $z$ |
| $\mathbf B$ | Bi-coordinate matrix, including the influence matrix in the Dirichlet problem |
| $H$, $\mathbf J$ | Zero-sum coordinate subspace and centering projector |
| $\mathcal D$ | Distance operator |
| $M_G$, $M_k$ | Metric polyform and its grade components |
| $T_n$ | Fixed spanning-tree form of grade $n-1$ |
| $\tau(P)$ | Coefficient of $T_n$ in a polyform on boundaries |
| $\tau(G)=\tau(M_G)$ | Spanning-tree coefficient of the graph |
| $u_M(f)$, $P_M(f)$ | Form potential and its normalized value $P_M(f)=\tau(Mf)/\tau(M)$ |
| $f_{ij}$, $\tau_i$ | Directed arc weight and rooted spanning-tree potential |
| $h$, $x_i=a_i-h$ | Centroid and centered vectors in the balanced extension |
| $\beta(u,v)$, $g(u,v)$, $\gamma(u,v)$ | Directional pairing and its symmetric and skew-symmetric parts |
| $\omega(u,v)$, $w(abc)$, $\chi_{abc}$ | Circulation form, triangular notation, and normalized potential |
| $r_{ij}$, $\mathbf r$ | One-way resistances and their matrix; individual edge resistance is written as $1/c_{ij}$ |
| $\mathrm{out}$, $\mathrm{in}$ | Source and receiver roles |
| $\rho$, $D_{\mathrm{res}}=4\rho$ | Quadratic resistance radius and diameter |

When matrix and polyform representations occur together, bold type denotes a matrix. Notes in which the representation is unambiguous may use ordinary letters $L,G,R$. Scalar matrix entries use ordinary type: $L_{ij}$, $\mathrm{Gr}_{ij}$; submatrices remain bold. Equation numbering is local to this specification.

### Collections in combinatorial formulas

A numerical collection $\mathbf x=[x_1,\ldots,x_m]$ is a finite multiset: enumeration order is immaterial, and repetitions are retained. For a finite set or collection $X$, the notation $\#X$ denotes its **size**, or cardinality; every occurrence in a collection is counted. When $\mathbf x$ lists the block sizes of a partition, $m=\#\mathbf x$ is the number of components, while its weight $w(\mathbf x)$ is the size of the set being partitioned.

First specify the collection, then the operation on it:

$$
w(\mathbf x)=x_1+\cdots+x_m,\qquad
\mathbf x!=[x_i]!=x_1\cdots x_m
$$

For nonnegative integers $x_i$, the notation $[x_i!]$ specifies the collection of factorials with the same indices and repetitions, and $[x_i!]!$ is the product of its elements. The ordinary factorial of a number retains its meaning: $[5]!=5$, whereas $5!=120$. The empty product equals $1$. The weight of a numerical collection differs from the affine weight of an element of $V$.

Square brackets for a numerical collection $[x_i]$, a simplex $[a_1\ldots a_k]$, and a form $[X,Y]$ are distinguished by the types of their arguments. Numerical collections use bold letters, such as $\mathbf x$ and $\boldsymbol\mu$; this convention is separate from the use of bold type for matrices. In a type such as $[1^\ell]$, the superscript denotes $\ell$ repetitions of one. When ambiguity is possible, repetitions are written out explicitly.

The parts of a combinatorial type specify block sizes. The parts of an SPF type specify their boundary grades: a block of $b$ vertices contributes the part $b-1$. For a full type on $n$ vertices whose parts sum to $k$, the component count is $m=n-k$, including singleton blocks of grade zero. The representation size $\#E_n[\lambda]$ counts terms in the chosen sum over partitions; it depends on the representation and differs from the number of forests. Definitions and normalizations appear in [[Partitions and the Combinatorial Potential of the Second Kind]] and [[Symmetric Polyforms - Types and Normalizations]].

### Types and toponomes of chosen representations

In the [[Partition Toponomes]] series, a standalone positive type is written as $\lambda=(k_1,\ldots,k_r)$, where $k_i\geqslant1$ are the boundary grades of the blocks. For a specified vertex count $n$,

$$
k=w(\lambda),\qquad r=\#\lambda,\qquad
m=n-k,\qquad \ell=n-k-r\geqslant0
$$

Here $m$ is the full number of components, $r$ the number of nontrivial components, and $\ell$ the number of singleton vertices. The empty type is denoted by $1$ and corresponds to the form $e$. The multiplicity notation $(1^2)=(1,1)$ differs from the product power $(1)^2$. Square brackets for collections, forms, and SPFs $E_n[\lambda]$ are retained; parentheses for numerical types do not change the notation for boundaries on named vertices.

For a chosen formal sum $\mathcal E=\sum_\pi c_\pi q_\pi$, reduction gives $T_{\mathcal E}=\sum_\pi c_\pi\lambda(\pi)$. It is linear on chosen expressions. Independence from representation requires preservation of all structural relations; free types do not generally satisfy this condition. For the graph toponome $T_G$, the expansion of the factors of $\exp L$ is fixed: coefficients sum products of edge weights of spanning forests by type. See [[From Polyforms to Partitions]] and [[Toponomes and Structural Identities]].

The notation $\lambda\leftrightarrow x_{k_1}\cdots x_{k_r}$ preserves the type. The product $*$ in [[The Second-Kind Algebra on Partitions|the second-kind algebra]] sums partial matchings of parts and differs from ordinary multiplication of these monomials. Its [[Partition Products and Boundary Forms|boundary realization]] requires chosen roots and a sum of partial gluings; types alone do not determine the ordinary product of particular polyforms.

The table $\mathcal A_{\mathcal E}=(a_{k,r})$ groups coefficients of types with the same $(k,r)$; $n$ is retained separately. It loses the distribution among types within a cell and does not in general determine a graph up to isomorphism. These constructions are a thematic extension; definitions and proofs are given in the series, and concise terminology in the [[PMG terminology#Partition toponomes and operations on types|glossary]].

## Sources and revision history

The balanced extension is based on the published [[Balanced Graphs]] series. Links after its subsections lead to definitions and proofs, including applicability conditions.

The ten notes of the [[PMG Introductory Series|introductory series]] provide the supporting material. External references and their correspondence to individual notes are listed in [[Further Reading for the PMG Introductory Series|further reading]]. This specification records the conventions of the published corpus; subsequent substantive changes require corresponding updates to related definitions and terminology.

| Revision | Date | Content |
|---|---|---|
| 9 | 2026-10-25 | Added the balanced extension: rooted potentials, directional pairing, one-way resistance and circulation, higher grades, Gram matrix, and radius. Specified the scope of symmetric formulas and reconstruction from the one-way resistance matrix. Aligned scalar matrix entries and terminology with Russian revision 9. |
| 8 | 2026-10-22 | Recorded notation for positive and empty types, the distinction between multiplicity and product powers, and the dependence of a toponome on its chosen expression. Specified the scope of $*$ and information loss in coefficient tables. Added links to the completed toponome series; the mathematical statements of the required core are unchanged. Aligned with Russian core specification revision 8. |
| 7 | 2026-10-20 | Recorded numerical-collection size and weight, collection products, and products of element factorials. Distinguished block-size types, SPF types, and representation size; added links to the structural, symmetric, and combinatorial series. Aligned exterior-product notation. The scope and mathematical statements of the core are unchanged. Aligned with Russian core specification revision 7. |
| 5 | 2026-10-16 | Aligned notation: Green matrix $\mathbf{Gr}=\mathbf L^+$, Gram matrix $\mathbf G$ with entries $g_{ij}$, extended Gram matrix $\mathbf G_z$, and bi-coordinate matrix $\mathbf B$. Clarified the geometric meaning of the Green matrix. |
| 3 | 2026-10-14 | Added links to the published definitions in the spaces series and aligned the names bi-coordinates and di-coordinates across languages. The mathematical content of the core is unchanged. This English version follows Russian revision 3. |
| 2 | 2026-10-09 | Removed unnecessary equation numbers; retained and consecutively renumbered only equations referenced in the text. This English version follows Russian revision 2. |
| 1 | 2026-10-09 | First public core specification, aligned with the introductory series. Clarified formal forms, the space of boundaries, the domain of metric evaluation, the spanning-tree coefficient, and conditions for variation formulas. |

Internal specification version 0.2 of 2026-09-21 was used as source material. Its core definitions are superseded by this document; its material on thematic extensions does not automatically become part of the core. Earlier revisions are historical records, not parallel current specifications.



