---
title: Core Specification of PMG
date: 2026-10-09
updated: 2026-10-30
revision: 15
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-core-specification
lang: en
description: "Definitions and conventions of the PMG core: polyform algebra, resistance metric, Laplacian and Greenian, forest and spectral parameters, boundary passports and gluing laws; conditions for the balanced extension."
order: 1
---

This specification records the definitions, notation, and fundamental identities of the Polyform Metric Geometry (PMG) core presented in the [[PMG Introductory Series|introductory series]]. It provides a reference for conventions and the conditions under which formulas apply. Proofs, examples, and references appear in the corresponding notes of the series.

Russian version: [[ru/Основания/Спецификация ядра PMG|Спецификация ядра PMG]].

## Purpose and scope

The algebraic construction is over the real numbers. The underlying space has a finite basis of vertices; forms are defined before a graph or metric is chosen.

The main graph model is a finite connected undirected graph without loops, with $n\ge2$ vertices. Existing edges have positive conductances; absent couplings have zero conductance. For the matrix and metric model, parallel conductors between the same pair of vertices are represented by the total conductance $c_{ij}=\sum_{\ell:\,\ell=\{i,j\}}c_\ell$. For the cycle matroid and edge parameters, the set of individual edges $E$ with conductances $c_\ell$ is fixed: aggregation preserves the Laplacian and resistance metric, but is not a matroid isomorphism and does not preserve all edge parameters. See [[Edge Resistances and Random Spanning Trees]]. The balanced model and its differences are explicitly stated in [[Core specification#The balanced extension|the balanced extension section]].

Connectedness is required for the resistance metric on the entire space of affine vectors and for normalization by the spanning-tree coefficient. The algebra of forms, the Laplacian exponential, and the forest expansion also apply to disconnected graphs. That case is specified separately.

**Status of the statements.** Definitions and conventions specify the language used. Claims about its properties are proved in the introductory series, and the balanced extension in [[en/Balanced graphs/Balanced Graphs|Balanced Graphs]]; links follow the relevant sections. For thematic extensions, links lead to the corresponding published series. Working conjectures are not part of the core.

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

> [!info] The exterior product and grade
> **Definition.** The space $\Lambda^kV$ consists of linear combinations of exterior products of $k$ elements of $V$. Its elements are called exterior objects of grade $k$. An object is decomposable if it can be expressed as a single exterior product.

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

> [!info] Products of simplex boundaries
> **Proposition.** The product of the vectors of selected edges is nonzero if and only if the edges form a forest. For a tree, this product equals the simplex boundary on its vertices up to sign; for a forest, it is the product of its component boundaries. An isolated vertex contributes the factor $\partial a_i=1$.
>
> Sources: [[Basic Objects and Operations of Polyform Algebra#The boundary operator|the boundary operator]], [[Basic Objects and Operations of Polyform Algebra#Boundaries and exterior powers of affine vectors|the space of boundaries]], and [[Basic Objects and Operations of Polyform Algebra#Products of simplex boundaries|products of boundaries]].

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

> [!info] Polyforms and their product
> **Definition.** A polyform is a finite linear combination of forms, possibly of different grades. It is homogeneous if all its terms have the same grade. In the decomposition $P=\sum_{k=0}^nP_k$, the term $P_k$ is called a grade component.

> [!info] Product of forms
> **Definition.** For forms of grades $k$ and $m$, set
>
> $$
> [X,Y][A,B]=[XA,YB]
> $$
>
> The product extends bilinearly to polyforms. Its identity is the grade-$0$ form $e=[1,1]$.

> [!info] Polyforms and their product
> **Proposition.** The product of forms is associative, distributive, and commutative. Grades add in nonzero products of homogeneous forms. On exchanging the factors, the two signs $(-1)^{km}$ from the exterior arguments cancel.
>
> The scalar $1$ is the identity for exterior objects, whereas $e$ is the identity for polyforms. For scalars $s,t$, one has $[s,t]=st\,e$.
>
> For quadratic forms,
>
> $$
> [X]^2[A]^2=[XA]^2,\qquad
> ([v]^2)^2=0\quad(v\in V)
> \tag{1}
> $$
>
> The last equality does not extend to an arbitrary sum of forms or to every higher-grade form. For independent $u,v\in W$, for example,
>
> $$
> \bigl([u]^2+[v]^2\bigr)^2=2[uv]^2\ne0
> $$

### Forms on boundaries

> [!info] Forms on boundaries
> **Definition.** Forms with arguments $X,Y\in\Lambda^kW$ and their linear combinations form the subalgebra of forms on boundaries. Its grades range from $0$ to $n-1$, and its identity is also $e$.

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

> [!info] The Green matrix and resistances
> **Definition.** The resistance inner product on $W$ and the effective resistances are given by
>
> $$
> u\cdot v=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v,\qquad
> R_{ij}=a_{ij}\cdot a_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
> \tag{3}
> $$

This inner product is positive definite on $W$. In the electrical interpretation, when unit current enters at vertex $i$ and leaves at $j$, one has $R_{ij}=\varphi_i-\varphi_j$, where $\varphi_i$ is the electrical potential at vertex $i$.

For the centroid $h=n^{-1}\sum_i a_i$, the identity $\mathbf{Gr}\mathbf1=0$ gives

$$
\mathrm{Gr}_{ij}=(h-a_i)\cdot(h-a_j)
$$

In the symmetric model, the Green matrix is the Gram matrix of the vectors from the vertices to the centroid. In a balanced graph, directional argument order gives the transposed matrix, as specified in the balanced extension. The notation $\mathbf G=(g_{ij})$ is reserved for the Gram matrix of explicitly chosen elements, with $g_{ij}$ denoting their inner products. The expressions $\mathbf{Gr}$ and $\mathbf L^+$ denote the same object: the former names it, while the latter specifies how it is obtained.

For two vertex pairs,

$$
a_{ij}\cdot a_{kl}=\frac{R_{il}+R_{jk}-R_{ik}-R_{jl}}2
$$

### Resistance radius and diameter

For a connected undirected graph with positive conductances, the resistances $R_{ij}$ are squared distances between the vertices of a nondegenerate Euclidean simplex of dimension $n-1$. Let $O$ be its circumcenter and $R_{\mathrm{sph}}$ its linear circumradius. The center $O$ generally differs from the centroid $h$.

> [!info] Resistance radius and diameter
> **Definition.** The resistance radius and diameter are quadratic quantities:
>
> $$
> \rho=R_{\mathrm{sph}}^2,\qquad D_{\mathrm{res}}=4\rho=(2R_{\mathrm{sph}})^2
> $$

The resistance diameter does not mean the maximum pairwise resistance. The definition and the forest formula with its verified normalization are given in [[Resistance Radius - Forest Formula and Matroid Invariance]]. The former name “metric mass” is not used without checking the correspondence between normalizations. The algebraic extension to balanced graphs appears in the balanced extension; its Euclidean interpretation requires a separate check.

### The distance operator

> [!info] The distance operator
> **Definition.** For a symmetric matrix $A$, set
>
> $$
> \mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}
> $$

Writing $\mathbf R=(R_{ij})$, the transformations between representations are

$$
\mathbf R=\mathcal D(\mathbf{Gr}),\qquad
\mathbf{Gr}=-\frac12\mathbf J\mathbf R\mathbf J,\qquad
\mathbf L=\left(-\frac12\mathbf J\mathbf R\mathbf J\right)^+
$$

These reconstruction formulas use symmetry of the Green matrix. The distance transformation and double centering are linear operations, distinct from pseudoinversion. An arbitrary squared Euclidean distance matrix need not be the resistance matrix of a graph with nonnegative conductances. The recovered $\mathbf L$ must satisfy the Laplacian conditions in (2).

> [!info] The distance operator
> **Proposition.** The vertices of a connected graph form a nondegenerate resistance simplex of dimension $n-1$, in which $R_{ij}$ is the squared Euclidean distance. Both $R_{ij}$ and $\sqrt{R_{ij}}$ define metrics on the vertices; the Euclidean length in this realization is $\sqrt{R_{ij}}$.
>
> Sources: [[Effective Resistance and Graph Geometry]], [[Inner Product of Graph Vectors]], and [[Laplacian, Green Matrix, and Effective Resistance Matrix]].

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

> [!info] Metrics of higher-grade objects
> **Proposition.** This extension is well-defined and positive definite on each $\Lambda^kW$. This revision does not introduce an inner product between objects of different grades.

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

> [!info] Metrics of higher-grade objects
> **Definition.** Numerical metric evaluation of a form on boundaries is specified by $[X,Y]\mapsto X\cdot Y$ and extended linearly within each grade. In particular, $[X]^2$ evaluates to $X^2$, $\{X,Y\}/2$ to $X\cdot Y$, and $e$ to $1$.

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

> [!info] The spanning-tree form and coefficient extraction
> **Definition.** For any polyform $P$ on boundaries, the functional $\tau(P)$ is defined by
>
> $$
> P_{n-1}=\tau(P)T_n
> \tag{5}
> $$

The functional is linear. If the grade-$(n-1)$ component is absent, its value is zero. The form $T_n$ is fixed by the original vertex set and is not replaced when passing from $P$ to another polyform or product.

> [!info] The spanning-tree form and coefficient extraction
> **Proposition.** For a graph's metric polyform,
>
> $$
> \tau(M_G)=\tau(G)=\sum_{T\text{ is a spanning tree}}\prod_{\{i,j\}\in T}c_{ij},\qquad
> M_{n-1}=\tau(G)T_n
> $$
>
> In the public series, $\tau(G)$ is called the **spanning-tree coefficient**. For unit conductances, it is the spanning-tree count. The earlier Russian term “остовное число” in the weighted setting refers to this same coefficient and does not assert that it is an integer.
>
> For a connected graph, $\tau(G)>0$. By the matrix-tree theorem, it equals the determinant of any reduced Laplacian. Consequently, $L^{n-1}\ne0$, and the highest nonzero grade of $M_G$ is $n-1$.
>
> In this model, $T_n$ is also called the top-grade form; $M_{n-1}$ is the top-grade component, and $M_{n-2}$ the next-to-top-grade component. These names do not change the definition of the functional in (5).
>
> Sources: [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|the spanning-tree form]] and [[From Lengths to Areas and Volumes|the matrix-tree theorem and resistance-simplex volume]].

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

This section extends the graph model to finite loopless balanced digraphs with nonnegative arc weights. The algebra of forms and its product are unchanged: symmetry of the arguments was never assumed. Graph and metric statements in the other sections use the symmetric model unless an extension is explicitly stated. Proofs and examples are collected in [[en/Balanced graphs/Balanced Graphs|Balanced Graphs]].

### The Laplacian, balance, and rooted potentials

Write $f_{ij}$ for the weight of arc $i\to j$. Use the outgoing Laplacian convention:

$$
L_{ii}=\sum_jf_{ij},\qquad L_{ij}=-f_{ij}\quad(i\ne j),\qquad
\mathbf L\mathbf1=0
$$

> [!info] The Laplacian, balance, and rooted potentials
> **Definition.** A graph is balanced if $\sum_jf_{ij}=\sum_jf_{ji}$ at every vertex. Equivalently, $\mathbf1^{\mathsf T}\mathbf L=0$. PMG uses the Russian abbreviation **балграф**. An undirected graph corresponds to $f_{ij}=f_{ji}$ and is a special case.

With $h=n^{-1}\sum_i a_i$ and $x_i=a_i-h$, the canonical centered representation is

$$
L=\sum_{i,j}L_{ij}[x_i,x_j]
$$

Because $\sum_i x_i=0$, arbitrary coefficients in this expression are not unique. The canonical choice fixes the centroid and the unique coefficient matrix with zero row and column sums. Balance places $L$ in the boundary-form subalgebra; the condition $f_{ij}\ge0$ is checked separately.

> [!info] The Laplacian, balance, and rooted potentials
> **Definition.** The spanning-tree potential of vertex $i$ is $\tau_i=\det\mathbf L_{\widehat i,\widehat i}$. It is the sum of weights of spanning arborescences directed toward root $i$. For the outgoing Laplacian, $\mathbf L^{\mathsf T}\boldsymbol\tau=0$.

A connected balanced graph with nonnegative weights is strongly connected, and all $\tau_i$ equal one positive spanning-tree coefficient $\tau$. This is the sum toward one fixed root; summing over all roots gives $n\tau$. Conversely, equality of all $\tau_i$ to one positive number implies balance. Equality of zero minors provides no such criterion.

The exponential and its top component retain the form

$$
M=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!},\qquad
M_{n-1}=\tau T_n
$$

Sources: [[Balanced Graphs and Spanning-Tree Potentials]], [[The Bilinear Laplacian of a Balanced Graph]], and [[The Laplacian Exponential of a Balanced Graph]]. Throughout the rest of this section, the graph is connected.

### Directional pairing and resistances

The matrix $\mathbf{Gr}=\mathbf L^+$ inverts $\mathbf L$ on $H$; the identities $\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J$ and zero row and column sums remain valid. Write $P_M(F)=\tau(MF)/\tau(M)$ for the normalized potential.

> [!info] Directional pairing and resistances
> **Definition.** For $u,v\in W$, use the source-receiver argument order:
>
> $$
> \boxed{\beta(u,v)=P_M([u,v])
> =u^{\mathrm{out}}\cdot v^{\mathrm{in}}
> =\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u}
> $$

Argument order matters. This is a bilinear pairing, generally nonsymmetric; the ordinary Euclidean inner product is its symmetric part

$$
g(u,v)=\frac{\beta(u,v)+\beta(v,u)}2,\qquad
\gamma(u,v)=\frac{\beta(u,v)-\beta(v,u)}2
$$

The form $g$ is positive definite on $W$. The formal circulation $\omega(u,v)=[u,v]-[v,u]$ has PMG grade one. For three points, $w(abc)=\omega(b-a,c-a)$, and its numerical evaluation is $\chi_{abc}=P_M(w(abc))=2\gamma(b-a,c-a)$. Distinguish the form from its potential.

> [!info] Directional pairing and resistances
> **Definition.** One-way resistance is defined algebraically:
>
> $$
> \boxed{r_{ij}=P_M([a_j-h,a_j-a_i])
> =\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}},\qquad
> R_{ij}=r_{ij}+r_{ji}
> $$

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
- KVP/KVPOU structural decompositions of specified pair tables; a general metric model for unbalanced digraphs requires separate justification;
- the Greenian, mutual duality of exterior exponentials, and cut representations;
- structural identities of partition forms, symmetric polyforms, and their combinatorial coefficients;
- partition toponomes, the second-kind algebra, and vector and vertex normalizations of polynomial toponomes;
- the cycle matroid, ordinary and rooted forest coefficients, and normalized forest and edge parameters;
- spectral representations of a symmetric first grade and its exponential, spectral projectors, graph cones, and projections;
- full boundary forest passports, their spanning-tree layer, and separate spectral boundary data;
- metric-value decompositions and interval forms;
- problems with values prescribed on a selected vertex set, including the Dirichlet problem.

Definitions of the isotropic representation and the null vector are given in [[The Null Vector, Isotropic Representation, and the Boundary]], coordinates and frames in [[Projections, Bi-coordinates, and Di-coordinates]], and the problem with prescribed values in [[Selected Vertices and the Dirichlet Problem]]. Their terminology is collected in the [[PMG terminology#Terminology of extensions|glossary of extensions]].

Partition forms and their structural identities are defined in [[Partition Forms and the Tetrahedron Identity]], and symmetric sums and representation sizes in [[Symmetric Polyforms - Types and Normalizations]]. The [[en/Combinatorial potentials/Combinatorial Potentials|Combinatorial Potentials]] series establishes the combinatorial coefficients of these sums and the distinction between partition counts and forest counts. Its general collection notation is recorded below; terminology from these series is included in the [[PMG terminology|glossary]]. Thematic definitions do not remove the applicability conditions of the base model or the explicitly stated balanced extension.

Published definitions of structural decompositions are collected in [[en/KVP decomposition/KVP Decomposition and Oriented Extensions|the KVP series]], and the two forest normalizations and Laplacian polynomial in [[en/Polynomial toponomes/Polynomial Toponomes|the polynomial toponome series]]. Matroid parameters and gluing laws are developed in [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|the matroid series]]. The conventions needed here are recorded below; these extensions are not developed in full.

An algebraic boundary is an image of $\partial$ and belongs to the corresponding exterior power $\Lambda^kW$. A marked graph boundary is a selected set of vertices for a Dirichlet, contraction, or gluing problem. These two meanings of “boundary” are distinct; conventions for a marked boundary are recorded below.

### The Greenian and mutual duality in the symmetric case

For a connected undirected graph, the **Greenian** is the grade-one form associated with the Green matrix:

$$
\mathrm{Gr}=\sum_{i,j}\mathrm{Gr}_{ij}[a_i-h,a_j-h]
=-\sum_{i<j}\mathrm{Gr}_{ij}[a_{ij}]^2,\qquad
h=\frac1n\sum_i a_i
$$

The Laplacian $L$ and the Greenian $\mathrm{Gr}$ are vector forms; their exterior exponentials are boundary polyforms. The vector representation concerns grade one; higher grades contain forms on exterior products of vectors. The Greenian coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$ may have either sign.

The matrices $\mathbf L$ and $\mathbf{Gr}$ are mutual pseudoinverses and ordinary inverses on $\mathbf1^\perp$. Exponential duality distinguishes the direct space $W$ from its dual $W^*$. When both spaces occur together, write an independent direct vertex as $a_i$ and the class of its coordinate functional in $W^*$ as $a_i^\vee$. Let $Q_1$ denote the dual representation of the Greenian and $\mathcal C:a_i^\vee\mapsto p_i=a_i-h$ the centered identification:

$$
\mathcal C(Q_1)=\mathrm{Gr},\qquad
M=\exp L,\qquad D=\exp Q_1,\qquad
\mathcal C(D)=\exp(\mathrm{Gr})
$$

For $d=n-1$,

$$
M_d/Q_k=M_{d-k},\qquad Q_d/M_k=Q_{d-k},\qquad M_0=Q_0=e
$$

Here $/$ is linear exterior contraction in both arguments of a form. Duality is a mutual relation, not the name of a separate type of polyform. After identification in one space, the ordinary product is $\exp L\,\exp(\mathrm{Gr})=\exp(L+\mathrm{Gr})$; the multiplicative inverse of $\exp L$ is $\exp(-L)$.

After the centered transfer, both exponentials define normalized potentials in the same space $W$. With the same fixed top-grade form $T_n=[(a_1\ldots a_n)]^2$, we have

$$
N=\exp(\mathrm{Gr})=\mathcal C(D),\qquad
P_N(f)=\frac{\tau(Nf)}{\tau(N)},\qquad
\tau(M)=\tau(G),\qquad \tau(N)=\frac{1}{n^2\tau(G)}
$$

| Exponential | Matrix of the induced metric on $W$ | Normalized potential |
|---|---|---|
| $M=\exp L$ | $\mathbf{Gr}=\mathbf L^+$ | $P_M([u,v])=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v$ |
| $N=\exp(\mathrm{Gr})$ | $\mathbf L$ | $P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v$ |

Here $u,v\in W$, and $\mathbf u,\mathbf v$ are their coefficient columns in the direct vertices. The metrics extend to exterior elements through Gram determinants and bilinearity. The chosen exponential must therefore be specified when discussing norms. The Greenian coefficients $\gamma_{ij}$ may have either sign, while both metrics above are positive definite on $W$. Proof and normalization: [[The Greenian Metric and Potentials]].

Definitions and proofs appear in [[Laplacian and Greenian - Mutual Duality of Exponentials]], [[The Canonical Vector Representation of the Greenian]], and [[The Exterior Exponential and Representations of the Greenian]]. These statements about quadratic vector forms do not automatically extend to nonsymmetric balanced-graph Laplacians; their bilinear boundary representation remains valid.

### Spectral representation in the symmetric case

In this section the graph is connected, undirected, and loopless, with positive conductances on existing edges; $d=n-1$. Definitions and proofs are collected in [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].

**The metric and the associated operator.** On $H=\mathbf1^\perp$, use the auxiliary coordinate inner product $\langle\mathbf v,\mathbf w\rangle_0=\mathbf v^{\mathsf T}\mathbf w$, transferred to $W$ by $v=\sum_i v_i a_i$. With this product, the form $[v,w]$ represents the operator $z\mapsto v\langle w,z\rangle_0$, and $L$ represents the usual Laplacian operator. Contracting the second argument of the same form $L$ using the resistance inner product gives a different operator: $\mathbf L\mathbf{Gr}|_H=I_H$. Distinguish the form, its coefficient matrix, the operator, and its numerical metric evaluation.

Let $\mathbf u_\alpha$ be a coordinate-orthonormal eigenbasis of $H$, with $u_\alpha=\sum_i u_{\alpha i}a_i$. Then

$$
\mathbf L\mathbf u_\alpha=\lambda_\alpha\mathbf u_\alpha,\qquad
\mathbf{Gr}\mathbf u_\alpha=\lambda_\alpha^{-1}\mathbf u_\alpha,\qquad
u_\alpha\cdot u_\beta=\lambda_\alpha^{-1}\delta_{\alpha\beta}
$$

Here $\lambda_\alpha>0$. The constant mode $\mathbf1/\sqrt n$ has eigenvalue $0$ for both matrices. With multiplicities, individual eigenvectors are not canonical; the eigenspaces $H_\lambda$ and their coordinate-orthogonal projectors are unique:

$$
\mathbf E_\lambda=\sum_{\alpha:\lambda_\alpha=\lambda}\mathbf u_\alpha\mathbf u_\alpha^{\mathsf T},\qquad
\mathbf L=\sum_{\lambda>0}\lambda\mathbf E_\lambda,\qquad
\mathbf{Gr}=\sum_{\lambda>0}\lambda^{-1}\mathbf E_\lambda,\qquad
\sum_{\lambda>0}\mathbf E_\lambda=\mathbf J
$$

A full spectral representation retains the eigenvalues and projectors in fixed vertex coordinates. It reconstructs both matrices and the total conductance of each pair, but not the decomposition of that conductance into individual parallel conductors. Eigenvalues with multiplicities alone do not reconstruct the operator; equal spectra do not imply graph isomorphism. A common eigenbasis does not imply equal spectra. For a family of real symmetric operators, simultaneous orthogonal diagonalization is equivalent to pairwise commutation. See [[Eigenspaces, Projectors, and Reconstruction of Polyforms]] and [[The Spectral Cone of a Fixed Basis]].

**Grades and evaluations.** Put $\ell_\alpha=\lambda_\alpha[u_\alpha]^2$. These forms commute and satisfy $\ell_\alpha^2=0$. Hence

$$
M(t)=\exp(tL)=\prod_{\alpha=1}^{d}(e+t\ell_\alpha),\qquad
M_g=\frac{L^g}{g!}=e_g(\ell_1,\ldots,\ell_d)
=\sum_{\#I=g}\lambda_I[u_I]^2
$$

Here $u_I$ is the exterior product of the selected eigenvectors in increasing index order, $\lambda_I=\prod_{\alpha\in I}\lambda_\alpha$, and $e_g$ is the elementary symmetric polynomial; $e_0=e$ for form arguments and $e_0=1$ for numbers. This symmetry in eigendirections does not imply invariance of the polyform under all vertex permutations, as required in the definition of an SPF.

Under the auxiliary identification on $\Lambda^gH$, the grade $M_g$ corresponds to the exterior power $\Lambda^g(\mathbf L|_H)$ with eigenvalues $\lambda_I$. The additive action obtained by summing the action of $\mathbf L$ on each exterior factor has eigenvalues $\sum_{\alpha\in I}\lambda_\alpha$ and is a different construction. Both operations differ from the matrix exponential. Diagonal factorization applies to the exponential of a symmetric first grade, not to an arbitrary polyform with independently prescribed higher grades.

Extend the coordinate inner product to exterior elements by Gram determinants, and denote the resulting linear evaluation of forms by $\operatorname{ev}_0$. Then

$$
\operatorname{ev}_0([X,Y])=\langle X,Y\rangle_0,\qquad
\operatorname{ev}_0(M_g)=e_g(\lambda_1,\ldots,\lambda_d)=p_g,\qquad
P_M(M_g)=\binom dg
$$

The evaluation $\operatorname{ev}_0$ is not an algebra homomorphism. The numbers $p_g$ are rooted forest coefficients; they do not replace the ordinary $f_g$ or normalized $\alpha_k$. The spectrum determines $P_G(t)=\prod_\alpha(1+t\lambda_\alpha)$, $\tau=p_d/n$, $\operatorname{tr}\mathbf{Gr}=\sum_\alpha\lambda_\alpha^{-1}$, and the Kirchhoff index $\operatorname{Kf}=n\operatorname{tr}\mathbf{Gr}$, but in general determines neither $F_G(t)$ nor individual $R_{ij}$. Proofs and a cospectral example: [[Diagonal Representation of Polyforms and Duality]], [[Eigenspaces, Projectors, and Reconstruction of Polyforms]].

**Complementary grades and scaling.** For the algebraic dual basis $u^\alpha(u_\beta)=\delta_{\alpha\beta}$, we have $\mathcal C(u^\alpha)=u_\alpha$. The centered identification $\mathcal C$ is not the resistance Riesz identification: $u_\alpha\cdot(\ )=\lambda_\alpha^{-1}u^\alpha$. With $I^c=\{1,\ldots,d\}\setminus I$,

$$
Q_g=\sum_{\#I=g}\lambda_I^{-1}[u^I]^2
=\frac1\Delta\sum_{\#I=g}\lambda_{I^c}[u^I]^2,\qquad
\Delta=\prod_{\alpha=1}^{d}\lambda_\alpha=n\tau(G)
$$

Thus reversing grade order involves taking complementary sets of directions, passing to $W^*$, and dividing coefficients by $\Delta$. The normalizations $M_d=\tau T_n$ and $N_d=T_n/(n^2\tau)$ remain unchanged: $T_n=n[u_1\cdots u_d]^2$. In $M(t)=\sum_g t^gM_g$ and $D(t)=\sum_g t^gQ_g$, the parameter only marks the grades of the original pair. When conductances are scaled by $s>0$, the mutually dual pair is $M(s)$ and $D(s^{-1})$, not the two exponentials with the same arbitrary parameter. See [[Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|the scaling convention]].

**Graph signs and projections.** Fix a coordinate-orthonormal basis $\mathbf U=(\mathbf1/\sqrt n,\mathbf u_1,\ldots,\mathbf u_d)$. Its Laplacian spectral cone is defined by

$$
\mathbf L(\boldsymbol\mu)=\mathbf U\operatorname{diag}(0,\mu_1,\ldots,\mu_d)\mathbf U^{\mathsf T},\qquad
\mathcal K_U=\{\boldsymbol\mu:\ -L_{ij}(\boldsymbol\mu)\ge0\text{ for }i<j\}
$$

Each coordinate $\mu_k$ belongs to a specified direction. The sign conditions imply positive semidefiniteness; the converse fails even with zero row sums. Within the cone, connectedness is equivalent to $\mu_k>0$ for all $k$. The boundary of the cone may contain connected graphs with missing edges. A polynomial in the Laplacian preserves its eigenspaces, but may merge eigenvalues and violate graph signs; the Chebyshev orbit of a path is not identified with the full cone. Definitions and conditions: [[Chebyshev Transformations of the Laplacian - From Path to Cycle]], [[The Spectral Cone of a Fixed Basis]].

Operator projections use the auxiliary Frobenius inner product $\langle\mathbf A,\mathbf C\rangle_F=\operatorname{tr}(\mathbf A^{\mathsf T}\mathbf C)$, not the resistance metric on $W$. For an arbitrary Laplacian under study, the diagonal evaluations $\mu_k=\mathbf u_k^{\mathsf T}\mathbf L\mathbf u_k$ in a reference basis need not be its eigenvalues. Distinguish

$$
\Pi_U(\mathbf L)=\sum_k\mu_k\mathbf u_k\mathbf u_k^{\mathsf T},\qquad
\Pi_{\mathrm{blk}}(\mathbf L)=\sum_\lambda\mathbf F_\lambda\mathbf L\mathbf F_\lambda
$$

Here $\mathbf F_\lambda$ are the spectral projectors of the reference operator. Block projection retains mixing within a repeated eigenspace and is independent of its basis. Both linear projections require graph-sign checks; the nearest point of the graph cone is obtained by a separate projection that is generally nonlinear. Projecting the Greenian generally differs from taking the pseudoinverse of the projected Laplacian, and diagonal projection of higher grades differs from the corresponding grades of the exponential of the projected first grade. Proofs and examples: [[Projection onto a Fixed Spectral Basis and Loss of Information]].

For disconnected graphs, zero modes remain in $H$. Reciprocal eigenvalues are used only on positive eigenspaces; division by $\Delta=\prod_{\alpha=1}^{d}\lambda_\alpha=0$ is invalid. Connectedness of a diagonal projection does not prove connectedness of the original graph. Nonsymmetric balanced-graph Laplacians require a separate spectral theory; the orthogonal decompositions above do not automatically extend to them.

### The cycle matroid and forest coefficients

The cycle matroid $M(G)$ consists of the edge set $E$ and its independent subsets, namely forests. An edge $\ell=\{i,j\}$ is represented by $a_j-a_i$; the exterior product of these vectors is nonzero exactly for a forest. The formal matroid definition and the definitions of basis, circuit, and matroid parameter appear in [[PMG terminology#Matroids and forest parameters|the terminology]], and the correspondence is proved in [[The Cycle Matroid and Exterior Products of Edges]].

Let $\kappa(G)$ count the components of the original graph, including isolated vertices. The matroid rank $r$, grade $g$, forest component count $m$, and forest corank $k$ satisfy

$$
r=n-\kappa(G),\qquad g=\#E(F),\qquad m=n-g,\qquad k=r-g=m-\kappa(G)
$$

For a connected graph, $r=d=n-1$ and $m=k+1$. The vertex count $n$ is retained separately: isolated vertices are not recorded by the cycle matroid.

For a spanning forest $F$, put $w(F)=\prod_{\ell\in E(F)}c_\ell$ and let $\pi(F)$ partition all vertices into components. Ordinary and rooted coefficients are distinguished:

$$
f_g(G)=\sum_{\substack{F\text{ - forest}\\\#E(F)=g}}w(F),\qquad
p_g(G)=\sum_{\substack{F\text{ - forest}\\\#E(F)=g}}w(F)\prod_{C\in\pi(F)}\#C
$$

In $p_g$, one root is chosen in each component, including singleton components. Hence

$$
F_G(t)=\sum_{g=0}^{r}f_g(G)t^g,\qquad
P_G(t)=\sum_{g=0}^{r}p_g(G)t^g=\det(I+t\mathbf L)
$$

The ordinary coefficients $f_g$ are determined by the weighted cycle matroid. The rooted coefficients $p_g$ and the full toponome of component types are not matroid invariants in general. The numbers $\operatorname{St}(k,m)$ from the combinatorial series belong to a different auxiliary construction; they do not rename either $f_g$ or $p_g$. Definitions and proofs: [[Forest Coefficients - Grade, Components, and Corank]], [[Forest Coefficients and the Laplacian Polynomial]].

For a connected graph with $\tau(G)=f_d>0$, normalized corank coefficients are defined by

$$
\alpha_k=\frac{f_{d-k}}{\tau(G)},\qquad
\Phi_G(u)=\sum_{k=0}^{d}\alpha_k u^k,\qquad \alpha_0=1
$$

In the fixed cut-based forest representation of the dual grade $Q_k$, the coefficient sum is $\alpha_k$. This is distinct from the canonical edge-based forest sum of the Greenian with weights $\gamma_{ij}=-\mathrm{Gr}_{ij}$, which may have either sign. Forest sums refer to the specified representations, not to an arbitrary expression for the same form. Formal factors of $\Phi_G$ are not identified with the spectrum of $\mathbf L$ or $\mathbf{Gr}$; it is the rooted polynomial $P_G$ that has a spectral interpretation. See [[The Normalized Forest Polynomial and Power-Sum Parameters]].

Matroid invariance means preservation under a matroid isomorphism that preserves corresponding weights. It does not establish a gluing law. Under one-vertex gluing of connected graphs with disjoint edge sets, $F_G$, $\Phi_G$, and $\tau$ multiply; forest power-sum parameters, $H_q$, and $\rho$ add, while the coefficients $\alpha_k$ convolve. The families are defined in the terminology; separate proofs of the laws appear in [[Gluing and the Limits of Matroid Invariance]]. These laws are not assumed for other gluings. Agreement of several parameters does not prove matroid isomorphism. The results do not extend automatically to balanced graphs.

### Boundary passports and graph gluing

This section records the conventions of the completed [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]] series. The full forest passport, its spanning-tree layer, and the spectral passport describe different data. “Passport” denotes the organization of coordinates adopted in the series; it does not assert novelty of the underlying theorems. The notes and navigator identify the origins of the results.

#### Marked boundaries and formal states

Here $G$ is a finite undirected graph with positive weights on individual edges, $B\subseteq V(G)$ is a nonempty set of marked vertices, $k=|B|$, and $n=|V(G)|$. The forest formulas require neither connectivity nor planarity. A “component” in a gluing problem is a constituent part and need not be a connected component. The boundary $B$ differs from the algebraic boundary $\partial X$.

All forests span all vertices, including isolated ones. A forest $H$ induces the connectivity partition $\pi_B(H)$ of $B$. For $\pi\in\Pi(B)$, set $b(\pi)=|\pi|$ and $r(\pi)=k-b(\pi)$. The state polynomial and full forest passport are

$$
\mathcal F^{G,B}_\pi(t)=\sum_{\pi_B(H)=\pi}w(H)t^{|E(H)|},\qquad
\mathbf f_G(t)=(\mathcal F^{G,B}_\pi(t))_{\pi\in\Pi(B)},\qquad
F_G(t)=\sum_\pi\mathcal F^{G,B}_\pi(t)
$$

In state $\pi$, a forest with $g$ edges has $n-g-b(\pi)$ components that do not meet the boundary. They are included in the sum. The vertex count and the boundary names and correspondence are retained separately: adding an isolated internal vertex leaves the polynomials unchanged. Definitions and examples: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component]].

States are first defined as independent symbols in the free space

$$
\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R s_\pi
$$

They must not be identified with partition forms $q_\pi=\prod_{A\in\pi}[(A)]^2$, which satisfy structural identities. Summing the coefficients of a chosen forest expansion does not by itself define a linear evaluation on the space of actual polyforms. Any descent of such a rule to a quotient must be justified separately.

#### Compatibility, contraction, and gluing

Let $\pi\vee\sigma$ be the least common coarsening of the partitions. The forest compatibility matrix is defined by

$$
(\mathbf C_B)_{\pi\sigma}=C(\pi,\sigma)=
\begin{cases}
1,&r(\pi\vee\sigma)=r(\pi)+r(\sigma)\\
0,&\text{otherwise}
\end{cases}
$$

This is a symmetric algebraic pairing of formal states, not the resistance inner product. Contracting the vertices of each block of $\sigma$ gives the test response

$$
U_G(\sigma;t)=F_{G/\sigma}(t)=\sum_\pi C(\pi,\sigma)\mathcal F^{G,B}_\pi(t),\qquad
\mathbf u_G(t)=\mathbf C_B\mathbf f_G(t)
$$

Edge labels are retained: a loop belongs to no forest, and two parallel edges together form a cycle. The polynomial counts the original selected edges, so there is no additional power of $t$. Mapping polyforms to the quotient space under vertex identification differs from multiplying the original expansion by $q_\sigma$, which is a test in the original space. The selection rule and the relation between these constructions are proved in [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test]].

Gluing $G_1\#_B G_2$ requires a fixed correspondence of the vertices of $B$, distinct internal vertices, and disjoint sets of labelled edges. Then

$$
\begin{aligned}
F_{G_1\#_B G_2}(t)&=\mathbf f_1(t)^{\mathsf T}\mathbf C_B\mathbf f_2(t)\\
\mathcal F^{G_1\#_B G_2,B}_\rho(t)&=
\sum_{\substack{\pi\vee\sigma=\rho\\C(\pi,\sigma)=1}}
\mathcal F^{G_1,B}_\pi(t)\mathcal F^{G_2,B}_\sigma(t)
\end{aligned}
$$

A shared edge that is to occur once in the result is assigned to one part beforehand; retaining two copies means two parallel edges. State coordinates differ from test responses. The pairing matrix may be inverted only on a nondegenerate space. The forest law specializes established rules for combining connectivity tables; its proof, comparison with external sources, and two- and three-point examples appear in [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data]].

#### Reducing a linear passport

All forest gluings can be evaluated on the quotient by the radical of the pairing:

$$
\mathscr R_B=\ker\mathbf C_B,\qquad
\mathscr H_B=\mathscr S_B/\mathscr R_B,\qquad
\dim\mathscr H_B=\operatorname{rank}\mathbf C_B=\mathrm{Cat}_k
=\frac1{k+1}\binom{2k}{k}
$$

For polynomial passports, the quotient is taken coefficientwise in $t$. The classes of noncrossing partitions in a chosen cyclic order on $B$ form a basis; this does not require graph planarity. The number $\mathrm{Cat}_k$ is minimal among universal linear passports with a fixed bilinear gluing law. This is not a bound for arbitrary nonlinear encodings. Reduced coordinates may be negative and need not count forests of an individual state.

In [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction]], the exact equality is derived from the upper bound of Mannens–Nederlof, §4.2, Theorem 4.2, and the nonsingularity of the noncrossing spanning-tree pairing in Kenyon–Wilson, §§2.1–2.2. This is a proved combination of external results, not a claim of scientific priority. The computed ranks $2,5,14,42$ for $k=2,3,4,5$ illustrate the general argument.

For $k=4$, the radical is one-dimensional, but its relation mixes partition ranks $2$ and $3$. It is not the tetrahedron structural identity. Equal dimensions do not identify the forest-state quotient with the space of partition forms or transfer their grading to it.

#### The spanning-tree layer and electrical response

A grove is a spanning forest every component of which meets $B$. Its weight in state $\pi$ is extracted from the full passport:

$$
g^{G,B}_\pi=[t^{n-b(\pi)}]\mathcal F^{G,B}_\pi(t)
$$

The degree of the extracted coefficient depends on the state. Spanning-tree pairing retains only pairs with $\pi\vee\sigma=\{B\}$ and $r(\pi)+r(\sigma)=k-1$. These conditions and the connection with the published grove pairing are discussed in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry]].

The following electrical formulas require $G$ to be connected. With $I=V(G)\setminus B$, the Dirichlet-to-Neumann response matrix and the fully separated grove scale are

$$
\boldsymbol\Lambda_B=\mathbf L_{BB}-\mathbf L_{BI}\mathbf L_{II}^{-1}\mathbf L_{IB},\qquad
\delta_B(G)=\det\mathbf L_{II}
$$

Currents are positive into the network. The principal block $\mathbf L_{II}$ retains original vertex degrees; it is not the Laplacian of the induced subgraph. For an empty interior, the eliminated contribution is zero and the empty determinant is $1$.

Choose $B=\{b_0,\ldots,b_{k-1}\}$ and let the columns of $\mathbf D$ be $d_i=b_i-b_0$. If $\mathbf H_B$ is obtained by deleting the row and column of $b_0$ from $\boldsymbol\Lambda_B$, then

$$
\mathbf G_B=\mathbf D^{\mathsf T}\mathbf{Gr}_G\mathbf D=\mathbf H_B^{-1},\qquad
\tau(G)=\delta_B(G)\det\mathbf H_B,\qquad
\delta_B(G)=\tau(G)\det\mathbf G_B
$$

These are standard electrical and determinant identities expressed in resistance geometry; precise attribution appears in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry]]. The principal block of the full Green matrix is not identified with $\boldsymbol\Lambda_B^+$: their evaluations on boundary differences agree, but their centerings refer to different vertex sets.

For two connected parts with a common boundary and disjoint edges, in the same boundary-difference basis,

$$
\boldsymbol\Lambda_{B,\#}=\boldsymbol\Lambda_{B,1}+\boldsymbol\Lambda_{B,2},\qquad
\tau(G_1\#_B G_2)=\tau(G_1)\tau(G_2)\det(\mathbf G_{B,1}+\mathbf G_{B,2})
$$

The resulting Gram matrix is $(\mathbf G_{B,1}^{-1}+\mathbf G_{B,2}^{-1})^{-1}$, not the sum of Gram matrices. Laplacians add after embedding in a common space; no analogous addition of Greenians is assumed.

The determinant formulas without correction use unscaled unit differences $b_i-b_0$ or the edges of a tree on $B$. Under the same basis change $\mathbf D'=\mathbf D\mathbf A$, the determinant of the sum of Gram matrices is divided by $(\det\mathbf A)^2$. The same normalization applies to the contraction formula $\tau(G/\sigma)=\tau(G)\det\mathbf G_\sigma$, where $\mathbf G_\sigma$ is the resistance Gram matrix of unit differences from trees within the blocks of $\sigma$. Ordinary reduced determinants are used; the product of nonzero Laplacian eigenvalues is $n\tau(G)$. For $k=1$, empty boundary determinants are $1$.

The electrical response together with its scale suffices for spanning-tree gluing but does not recover the full forest passport. Recovery of individual normalized grove weights from the response in the results of Kenyon–Wilson requires circular planarity: an embedding in a disk with the marked vertices on its boundary in the prescribed order. Choosing a noncrossing coordinate basis does not supply this condition.

#### A separate spectral passport

The spectral variable is $\xi$. The Laplacian pencil and characteristic polynomial use the conventions

$$
\mathbf M_G(\xi)=\xi I-\mathbf L_G,\qquad
\chi_G(\xi)=\det\mathbf M_G(\xi)=\xi^nP_G(-1/\xi)
$$

The last equality is a polynomial identity, including at $\xi=0$. It connects the spectrum with the rooted polynomial $P_G$, not the ordinary polynomial $F_G$.

For an ordered pair $\mathcal B=(a,b)$ and $J=V(G)\setminus\{a,b\}$, the spectral passport consists of five polynomials:

$$
\begin{aligned}
A&=\det\mathbf M_G\\
B&=\det(\mathbf M_G)_{\widehat a},\qquad
C=\det(\mathbf M_G)_{\widehat b}\\
D&=(\operatorname{adj}\mathbf M_G)_{ab},\qquad
E=\det(\mathbf M_G)_{JJ}
\end{aligned}
$$

A hat means deletion of a row and column without recalculating the degrees of remaining vertices. Here $B,C,D,E$ are local polynomial names, and $\mathcal B$ denotes the boundary. The classical Jacobi identity and the Schur complement give

$$
AE=BC-D^2,\qquad
\mathbf S_G(\xi)=\frac1E\begin{pmatrix}C&-D\\-D&B\end{pmatrix},\qquad
A=E\det\mathbf S_G
$$

The rational expression for $\mathbf S_G$ applies when $E\ne0$; polynomial determinant identities also hold at zeros of $E$. The five coordinates are not asserted to be algebraically independent or minimal.

For two parts with the same ordered pair and disjoint edges,

$$
E_\#=E_1E_2,\qquad
\mathbf S_\#=\mathbf S_1+\mathbf S_2-\xi I_2
$$

The correction counts shared vertices once. If both parts contain the same edge $ab$ of weight $w$, which is to occur only once in the result, add $\mathbf L_e=w\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)$ to the right-hand side. If two parallel copies are retained, there is no such correction. Polynomial formulas for all five coordinates, checks at degenerate values, and attribution of the determinant methods appear in [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data]].

For a connected graph, $\mathbf S_G(0)=-\boldsymbol\Lambda_{\mathcal B}$. The static electrical response does not replace the dependence on $\xi$. A passport for a fixed pair does not establish closure of a transfer rule when input and output boundaries change; those rules and chain closures belong to the next stage.

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
| $\mathrm{Gr}$, $Q_1$, $D$ | Greenian, its dual representation, and the exponential $D=\exp Q_1$ |
| $\mathbf{Gr}=\mathbf L^+$, $\mathbf R$ | Green matrix and resistance matrix |
| $\mathbf G=(g_{ij})$ | Gram matrix of chosen elements; $g_{ij}$ are their inner products |
| $\mathbf G_z$ | In the isotropic extension: the Gram matrix of the vertices together with the null vector $z$ |
| $\mathbf B$ | Bi-coordinate matrix, including the influence matrix in the Dirichlet problem |
| $H$, $\mathbf J$ | Zero-sum coordinate subspace and centering projector |
| $\langle\ ,\ \rangle_0$, $\operatorname{ev}_0$ | Auxiliary coordinate inner product and its linear evaluation of forms |
| $u_\alpha$, $u^\alpha$, $\ell_\alpha$ | Eigenvectors in $W$, algebraic dual elements, and forms $\lambda_\alpha[u_\alpha]^2$ |
| $\mathbf E_\lambda$, $\mathbf F_\lambda$ | Spectral projectors of the operator under study and of the reference operator |
| $e_g$, $\Delta=n\tau$ | Elementary symmetric polynomial and product of the positive eigenvalues of a connected graph |
| $\mathcal K_U$, $\Pi_U$, $\Pi_{\mathrm{blk}}$ | Spectral cone of a basis, diagonal and block operator projections |
| $\mathcal D$ | Distance operator |
| $M_G$, $M_k$ | Metric polyform and its grade components |
| $T_n$ | Fixed spanning-tree form of grade $n-1$ |
| $\tau(P)$ | Coefficient of $T_n$ in a polyform on boundaries |
| $\tau(G)=\tau(M_G)$ | Spanning-tree coefficient of the graph |
| $u_M(f)$, $P_M(f)$ | Form potential and its normalized value $P_M(f)=\tau(Mf)/\tau(M)$ |
| $N=\exp(\mathrm{Gr})$, $P_N(f)$ | Greenian exponential in the direct space and its normalized potential |
| $B$, $\mathcal B$ | Marked graph boundary; ordered pair for a spectral passport, distinct from the operator $\partial$ |
| $\mathcal F^{G,B}_\pi(t)$, $\mathbf f_G(t)$ | State polynomial and full forest passport; the degree of $t$ counts edges |
| $\mathbf C_B$, $\mathbf u_G(t)$ | Forest compatibility matrix and vector of test responses |
| $\mathscr S_B$, $\mathscr R_B$, $\mathscr H_B$ | Free states, the radical of the forest pairing, and its quotient |
| $g^{G,B}_\pi$, $\delta_B(G)$ | Grove weight of a state and fully separated grove scale |
| $\boldsymbol\Lambda_B$, $\mathbf G_B$, $\mathbf D$ | Electrical response, boundary resistance Gram matrix, and matrix of chosen differences |
| $\xi$, $\mathbf M_G(\xi)$, $\mathbf S_G(\xi)$ | Spectral variable, the pencil $\xi I-\mathbf L_G$, and its boundary Schur complement |
| $A,B,C,D,E$ | Local polynomial coordinates of a pair's spectral passport; here $D$ is not an exponential and $E$ is not the projector $\mathbf E_\lambda$ |
| $f_g$, $p_g$, $\alpha_k$ | Ordinary, rooted, and normalized corank forest coefficients |
| $f_{ij}$, $\tau_i$ | Directed arc weight and rooted spanning-tree potential |
| $c_\ell$, $c_{ij}$ | Individual edge conductance and total conductance of a vertex pair |
| $h$, $x_i=a_i-h$ | Centroid and centered vectors; the Greenian representation also uses $p_i=a_i-h$ |
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

In the [[en/Partition toponomes/Partition Toponomes|Partition Toponomes]] series, a standalone positive type is written as $\lambda=(k_1,\ldots,k_r)$, where $k_i\geqslant1$ are the boundary grades of the blocks. For a specified vertex count $n$,

$$
k=w(\lambda),\qquad r=\#\lambda,\qquad
m=n-k,\qquad \ell=n-k-r\geqslant0
$$

Here $m$ is the full number of components, $r$ the number of nontrivial components, and $\ell$ the number of singleton vertices. The empty type is denoted by $1$ and corresponds to the form $e$. The multiplicity notation $(1^2)=(1,1)$ differs from the product power $(1)^2$. Square brackets for collections, forms, and SPFs $E_n[\lambda]$ are retained; parentheses for numerical types do not change the notation for boundaries on named vertices.

For a chosen formal sum $\mathcal E=\sum_\pi c_\pi q_\pi$, reduction gives $T_{\mathcal E}=\sum_\pi c_\pi\lambda(\pi)$. It is linear on chosen expressions. Independence from representation requires preservation of all structural relations; free types do not generally satisfy this condition. For the graph toponome $T_G$, the expansion of the factors of $\exp L$ is fixed: coefficients sum products of edge weights of spanning forests by type. See [[From Polyforms to Partitions]] and [[Toponomes and Structural Identities]].

The notation $\lambda\leftrightarrow x_{k_1}\cdots x_{k_r}$ preserves the type. The product $*$ in [[The Second-Kind Algebra on Partitions|the second-kind algebra]] sums partial matchings of parts and differs from ordinary multiplication of these monomials. Its [[Partition Products and Boundary Forms|boundary realization]] requires chosen roots and a sum of partial gluings; types alone do not determine the ordinary product of particular polyforms.

The table $\mathcal A_{\mathcal E}=(a_{k,r})$ groups coefficients of types with the same $(k,r)$; $n$ is retained separately. It loses the distribution among types within a cell and does not in general determine a graph up to isomorphism. These constructions are a thematic extension; definitions and proofs are given in the series, and concise terminology in the [[PMG terminology#Partition toponomes and operations on types|glossary]].

## Sources and revision history

The balanced extension is based on the published [[en/Balanced graphs/Balanced Graphs|Balanced Graphs]] series. Links after its subsections lead to definitions and proofs, including applicability conditions.

The ten notes of the [[PMG Introductory Series|introductory series]] provide the supporting material. External references and their correspondence to individual notes are listed in [[Further Reading for the PMG Introductory Series|further reading]]. This specification records the conventions of the published corpus; subsequent substantive changes require corresponding updates to related definitions and terminology.

| Revision | Date | Content |
|---|---|---|
| 15 | 2026-10-30 | Replaced the internal series code in the revision history with its descriptive title. Mathematical conventions are unchanged. Aligned with Russian revision 15. |
| 14 | 2026-10-30 | Recorded conventions of the completed “Boundary Polynomials and Graph Gluing” series: the full forest passport, contraction tests, pairing and the Catalan linear quotient, groves and electrical scale, and a separate spectral passport. Clarified formal states, determinant normalizations, shared vertices and edges, reconstruction conditions, and external foundations. Aligned with Russian revision 14. |
| 13 | 2026-10-30 | Recorded spectral conventions: coordinate and resistance metrics, projectors, diagonal grades and their evaluations, complementary dual directions, and scaling. Distinguished exterior powers, additive action, graph cones, and projection types; added limitations and links to the completed series. Aligned with Russian revision 13. |
| 12 | 2026-10-28 | Aligned individual edges and aggregated couplings, centroid notation, and quadratic radius. Added the two metric roles of the exponentials, matroid and forest conventions, and links to published extensions. Aligned with Russian revision 12. |
| 11 | 2026-10-28 | Aligned direct and dual notation with Russian revision 11 and linked the completed English Greenian series. |
| 10 | 2026-10-27 | Defined the Greenian and mutual exponential duality; distinguished grade-one vector forms from boundary polyforms, dual from centered representations, and exterior multiplication from matrix composition. Removed dex from the current extension list. Aligned with Russian revision 10; the series itself remains in Russian pending review. |
| 9 | 2026-10-25 | Added the balanced extension: rooted potentials, directional pairing, one-way resistance and circulation, higher grades, Gram matrix, and radius. Specified the scope of symmetric formulas and reconstruction from the one-way resistance matrix. Aligned scalar matrix entries and terminology with Russian revision 9. |
| 8 | 2026-10-22 | Recorded notation for positive and empty types, the distinction between multiplicity and product powers, and the dependence of a toponome on its chosen expression. Specified the scope of $*$ and information loss in coefficient tables. Added links to the completed toponome series; the mathematical statements of the required core are unchanged. Aligned with Russian core specification revision 8. |
| 7 | 2026-10-20 | Recorded numerical-collection size and weight, collection products, and products of element factorials. Distinguished block-size types, SPF types, and representation size; added links to the structural, symmetric, and combinatorial series. Aligned exterior-product notation. The scope and mathematical statements of the core are unchanged. Aligned with Russian core specification revision 7. |
| 5 | 2026-10-16 | Aligned notation: Green matrix $\mathbf{Gr}=\mathbf L^+$, Gram matrix $\mathbf G$ with entries $g_{ij}$, extended Gram matrix $\mathbf G_z$, and bi-coordinate matrix $\mathbf B$. Clarified the geometric meaning of the Green matrix. |
| 3 | 2026-10-14 | Added links to the published definitions in the spaces series and aligned the names bi-coordinates and di-coordinates across languages. The mathematical content of the core is unchanged. This English version follows Russian revision 3. |
| 2 | 2026-10-09 | Removed unnecessary equation numbers; retained and consecutively renumbered only equations referenced in the text. This English version follows Russian revision 2. |
| 1 | 2026-10-09 | First public core specification, aligned with the introductory series. Clarified formal forms, the space of boundaries, the domain of metric evaluation, the spanning-tree coefficient, and conditions for variation formulas. |

Internal specification version 0.2 of 2026-09-21 was used as source material. Its core definitions are superseded by this document; its material on thematic extensions does not automatically become part of the core. Earlier revisions are historical records, not parallel current specifications.
