---
title: Core Specification of PMG
date: 2026-10-09
updated: 2026-10-09
revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-core-specification
lang: en
description: "Definitions, notation, and fundamental identities of the PMG core: exterior objects, boundaries, forms, the resistance metric, and the Laplacian exponential."
order: 1
---

This specification records the definitions, notation, and fundamental identities of the Polyform Metric Geometry (PMG) core presented in the [[PMG Introductory Series|introductory series]]. It provides a reference for conventions and the conditions under which formulas apply. Proofs, examples, and references appear in the corresponding notes of the series.

## Purpose and scope

The algebraic construction is over the real numbers. The underlying space has a finite basis of vertices; forms are defined before a graph or metric is chosen.

The main graph model is a finite connected undirected graph without loops, with $n\ge2$ vertices. Existing edges have positive conductances; absent couplings have zero conductance. Parallel conductors between the same pair of vertices are represented by their total conductance.

Connectedness is required for the resistance metric on the entire space of affine vectors and for normalization by the spanning-tree coefficient. The algebra of forms, the Laplacian exponential, and the forest expansion also apply to disconnected graphs. That case is specified separately.

**Status of the statements.** Definitions and conventions specify the language used. Claims about its properties are proved in the introductory series; links follow the relevant sections. Working conjectures are not part of the core.

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

The exterior product is bilinear and associative. For homogeneous objects $X\in\Lambda^kV$ and $Y\in\Lambda^mV$,

$$
X\wedge Y=(-1)^{km}Y\wedge X
$$

In particular, $x\wedge x=0$ for $x\in V$. The scalar $1\in\Lambda^0V$ is the identity for the exterior product. A nonzero product of objects of grades $k$ and $m$ has grade $k+m$.

An oriented simplex is written as

$$
[a_{i_1}\ldots a_{i_k}]=a_{i_1}\wedge\cdots\wedge a_{i_k}
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
\partial(X\wedge Y)=\partial X\wedge Y+(-1)^kX\wedge\partial Y
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
(pa_1\ldots a_r)=(a_1-p)\wedge\cdots\wedge(a_r-p)
$$

The following rules apply to boundaries of simplices on distinct basis vertices, with each simplex containing at least two vertices.

- If the only shared vertex $p$ is listed first in both simplices, then

$$
(pa_1\ldots a_r)\wedge(pb_1\ldots b_s)=(pa_1\ldots a_r b_1\ldots b_s)
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

The notation $[X]^2$ denotes neither $X\wedge X$ nor a numerical squared norm. For nonzero $X$, the form $[X]^2$ is nonzero, and $[-X]^2=[X]^2$.

### Polyforms and their product

**Definition.** A polyform is a finite linear combination of forms, possibly of different grades. It is homogeneous if all its terms have the same grade. In the decomposition $P=\sum_{k=0}^nP_k$, the term $P_k$ is called a grade component.

> [!info] Product of forms
> **Definition.** For forms of grades $k$ and $m$, set
>
> $$
> [X,Y][A,B]=[X\wedge A,Y\wedge B]
> $$
>
> The product extends bilinearly to polyforms. Its identity is the grade-$0$ form $e=[1,1]$.

**Proposition.** The product of forms is associative, distributive, and commutative. Grades add in nonzero products of homogeneous forms. On exchanging the factors, the two signs $(-1)^{km}$ from the exterior arguments cancel.

The scalar $1$ is the identity for exterior objects, whereas $e$ is the identity for polyforms. For scalars $s,t$, one has $[s,t]=st\,e$.

For quadratic forms,

$$
[X]^2[A]^2=[X\wedge A]^2,\qquad
([v]^2)^2=0\quad(v\in V)
\tag{1}
$$

The last equality does not extend to an arbitrary sum of forms or to every higher-grade form. For independent $u,v\in W$, for example,

$$
\bigl([u]^2+[v]^2\bigr)^2=2[u\wedge v]^2\ne0
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
> \mathbf L_{ii}=d_i,\qquad \mathbf L_{ij}=-c_{ij}\quad(i\ne j),\qquad
> L=\sum_{i<j}c_{ij}[a_{ij}]^2
> \tag{2}
> $$

The polyform $L$ has grade $1$ and belongs to the subalgebra of forms on boundaries. Its coefficient matrix in the forms $[a_i,a_j]$ is $\mathbf L$:

$$
L=\sum_{i,j}\mathbf L_{ij}[a_i,a_j]
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
> **Definition.** For a connected graph, $\mathbf G$ inverts $\mathbf L$ on $H$ and vanishes on constant columns. Equivalently, $\mathbf G=\mathbf L^+$, where $+$ denotes the Moore-Penrose pseudoinverse.

For the centering projector $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$,

$$
\mathbf L\mathbf G=\mathbf G\mathbf L=\mathbf J,\qquad
\mathbf G\mathbf1=0,\qquad \mathbf G^+=\mathbf L
$$

**Definition.** The resistance inner product on $W$ and the effective resistances are given by

$$
u\cdot v=\mathbf u^{\mathsf T}\mathbf G\mathbf v,\qquad
R_{ij}=a_{ij}\cdot a_{ij}=\mathbf G_{ii}+\mathbf G_{jj}-2\mathbf G_{ij}
\tag{3}
$$

This inner product is positive definite on $W$. In the electrical interpretation, when unit current enters at vertex $i$ and leaves at $j$, one has $R_{ij}=\varphi_i-\varphi_j$, where $\varphi_i$ is the electrical potential at vertex $i$.

For two vertex pairs,

$$
a_{ij}\cdot a_{kl}=\frac{R_{il}+R_{jk}-R_{ik}-R_{jl}}2
$$

### The distance operator

**Definition.** For a symmetric matrix $B$, set

$$
\mathcal D(B)_{ij}=B_{ii}+B_{jj}-2B_{ij}
$$

Writing $\mathbf R=(R_{ij})$, the transformations between representations are

$$
\mathbf R=\mathcal D(\mathbf G),\qquad
\mathbf G=-\frac12\mathbf J\mathbf R\mathbf J,\qquad
\mathbf L=\left(-\frac12\mathbf J\mathbf R\mathbf J\right)^+
$$

The distance transformation and double centering are linear operations, distinct from pseudoinversion. An arbitrary squared Euclidean distance matrix need not be the resistance matrix of a graph with nonnegative conductances. The recovered $\mathbf L$ must satisfy the Laplacian conditions in (2).

**Proposition.** The vertices of a connected graph form a nondegenerate resistance simplex of dimension $n-1$, in which $R_{ij}$ is the squared Euclidean distance. Both $R_{ij}$ and $\sqrt{R_{ij}}$ define metrics on the vertices; the Euclidean length in this realization is $\sqrt{R_{ij}}$.

Sources: [[Effective Resistance and Graph Geometry]], [[Inner Product of Graph Vectors]], and [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

## Metrics of higher-grade objects

Let $W$ carry a positive-definite inner product. The graph model uses (3).

> [!info] Induced metric
> **Definition.** For decomposable objects of the same grade,
>
> $$
> X=u_1\wedge\cdots\wedge u_k,\qquad Y=v_1\wedge\cdots\wedge v_k
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

For a boundary $X$, the numerical square and Euclidean norm satisfy

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

**Terminological convention.** In PMG, the normalized potential is also called the norm of a form. For a general form, it is a linear evaluation that can have either sign and is not a norm in the usual sense. For a quadratic form $[X]^2$, it equals the squared Euclidean norm of its argument. In this specification, $\|X\|$ retains its usual Euclidean meaning; the normalized potential is written as the ratio in (7).

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

Let $K_{\alpha\beta}=v_\alpha\cdot v_\beta$ and $D=\operatorname{diag}(t_1,\ldots,t_m)$. For a connected initial graph,

$$
\frac{\tau\left(\exp\left(L+\sum_\alpha t_\alpha[v_\alpha]^2\right)\right)}{\tau(M_G)}
=\det(I_m+DK)
\tag{11}
$$

The coefficient of $\prod_{\alpha\in S}t_\alpha$ is the principal minor $\det K_S$. It is the squared norm of the exterior product of the selected vectors. For the empty set, both the product and determinant are $1$.

For vectors of distinct vertex pairs, (10)-(11) describe joint conductance variations. The determinant formula remains meaningful for a disconnected final graph; inverse-update formulas for its Green matrix on the original subspace require connectedness to be preserved.

Sources: [[Variation of a Single Edge]], [[Varying several couplings together]], and [[Laplacian Exponential#Algebraic variation and edge addition|algebraic variation]].

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

The following constructions are outside this revision of the core and require separate definitions and applicability conditions:

- the isotropic extension, the distinguished null vector, and barycentric and metric dual coordinates;
- directed graphs and the KVP/KVPOU structural decompositions;
- dual polyforms, cut forms, and the function $\operatorname{dex}$;
- symmetric polyforms, toponomes, and component reductions;
- metric-value decompositions and interval forms;
- problems with values prescribed on a selected vertex set, including the Dirichlet problem.

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
| $X\wedge Y$ | Exterior product of objects |
| $X\cdot Y$, $X^2=\lVert X\rVert^2$ | Numerical inner product and squared norm |
| $c_{ij}$, $d_i$ | Conductances and weighted vertex degrees |
| $G$ | Graph |
| $L$, $\mathbf L$ | Laplacian polyform and Laplacian matrix |
| $\mathbf G$, $\mathbf R$ | Green matrix and resistance matrix |
| $H$, $\mathbf J$ | Zero-sum coordinate subspace and centering projector |
| $\mathcal D$ | Distance operator |
| $M_G$, $M_k$ | Metric polyform and its grade components |
| $T_n$ | Fixed spanning-tree form of grade $n-1$ |
| $\tau(P)$ | Coefficient of $T_n$ in a polyform on boundaries |
| $\tau(G)=\tau(M_G)$ | Spanning-tree coefficient of the graph |
| $u_M(f)$ | Potential of a form in the fixed metric |

When matrix and polyform representations occur together, bold type denotes a matrix. Notes in which the representation is unambiguous may use ordinary letters $L,G,R$. Equation numbering is local to this specification.

## Sources and revision history

The ten notes of the [[PMG Introductory Series|introductory series]] provide the supporting material. External references and their correspondence to individual notes are listed in [[Further Reading for the PMG Introductory Series|further reading]]. This specification records the conventions of the published corpus; subsequent substantive changes require corresponding updates to related definitions and terminology.

| Revision | Date | Content |
|---|---|---|
| 2 | 2026-10-09 | Removed unnecessary equation numbers; retained and consecutively renumbered only equations referenced in the text. This English version follows Russian revision 2. |
| 1 | 2026-10-09 | First public core specification, aligned with the introductory series. Clarified formal forms, the space of boundaries, the domain of metric evaluation, the spanning-tree coefficient, and conditions for variation formulas. |

Internal specification version 0.2 of 2026-09-21 was used as source material. Its core definitions are superseded by this document; its material on thematic extensions does not automatically become part of the core. Earlier revisions are historical records, not parallel current specifications.
