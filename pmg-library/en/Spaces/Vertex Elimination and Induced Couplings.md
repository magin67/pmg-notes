---
title: Vertex Elimination and Induced Couplings
date: 2026-10-14
updated: 2026-10-15
revision: 5
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: vertex-elimination-and-induced-couplings
order: 7
description: "A graph on selected vertices: projecting the Laplacian, induced couplings, the response matrix, and preservation of the resistance metric through factorization of the metric polyform."
---

Select several vertices of a graph. Can we construct a graph on just these vertices while preserving their resistance geometry? Simply deleting the other vertices is not enough: this also removes couplings that contributed to the original metric. Their contribution must be accounted for by new coupling coefficients between the remaining vertices.

We will call this operation elimination of the internal vertices. Geometrically, it preserves the metric of the selected subspace. In polyform algebra, it is expressed by projecting the Laplacian and factoring its exponential.

It uses [[Selected Vertices and the Dirichlet Problem|projections and the influence matrix]], the [[Projections, Bi-coordinates, and Di-coordinates|decomposition of the quadratic form of a frame]], and the [[Core specification|metric identity]]. We consider a finite, connected, undirected graph without loops. All existing couplings have positive coefficients; absent couplings have coefficient zero.

## What should remain after elimination

Return to the path $a-x-y-b$ with coupling coefficients $2,1,3$. Select $a,b$. The effective resistance between them is

$$
R_{ab}=\frac12+1+\frac13=\frac{11}{6}
$$

A graph on two vertices can reproduce this effective resistance with a single coupling of coefficient $6/11$. This coupling accounts for the entire original path.

We distinguish three operations.

| Operation | What happens to the vertices and couplings |
|---|---|
| Deleting $x,y$ | These vertices and their incident couplings are removed. Vertices $a,b$ remain disconnected. |
| Contraction | Chosen vertices are identified. For example, identifying $x=a$, $y=b$ leaves a coupling $ab$ of coefficient $1$. |
| Eliminating $x,y$ | Vertices $a,b$ remain distinct, and their coupling receives coefficient $6/11$, preserving the original effective resistance. |

Contraction is discussed in a [[Vertex Contraction and Graph Gluing|separate note]]. Neither deletion nor contraction preserves the original effective resistance $11/6$ in this example.

## The selected subspace and projection of the Laplacian

Write $\mathcal V$ for the set of all vertices, $P$ for the retained set, and $I=\mathcal V\setminus P$ for the internal vertices. For now, assume that $2\le |P|<|\mathcal V|$; the vertical bars here denote the number of elements in a set.

The points of the selected affine subspace and its vectors have the forms

$$
\mathcal A_P=\left\{\sum_{p\in P}t_pp:\sum_pt_p=1\right\},\qquad
W_P=\left\{\sum_{p\in P}h_pp:\sum_ph_p=0\right\}
$$

The original resistance metric is already defined on the space $W$ of all affine vectors. We want to preserve its restriction to $W_P$: inner products of vectors in this subspace must remain unchanged.

For each internal vertex, use its orthogonal projection and the frame established in the note on the Dirichlet problem:

$$
q_x=\sum_{p\in P}b_{xp}p,\qquad
\sum_pb_{xp}=1,\qquad
r_x=x-q_x\perp W_P
$$

The symbol $\perp$ denotes orthogonality: the inner product of $r_x$ with every vector in $W_P$ is zero. The coefficients $b_{xp}$ are the bi-coordinates of the projection $q_x$, not of the vertex $x$ itself. For a retained vertex, set $q_p=p$, $r_p=0$.

On vectors, the projection $\pi$ is given by $\pi(a_j-a_i)=q_j-q_i$. It extends to exterior products by acting on each factor, and to forms by $\pi([X,Y])=[\pi X,\pi Y]$. This extension preserves the polyform product.

> [!info] Projection of the Laplacian
> **Definition.** Denote the projection of the original Laplacian polyform by $L_P$:
>
> $$
> \boxed{L_P=\pi(L)=\sum_{i<j}c_{ij}[q_j-q_i]^2}
> \tag{1}
> $$
>
> The sum runs over unordered pairs of original vertices, with each pair counted once. All arguments of forms in $L_P$ belong to $W_P$.

For now, (1) is written in terms of the projections of all original couplings. We will express it in terms of pairs of retained vertices and prove that its exponential defines the required metric.

For the path, set $d=b-a$. The projections already calculated are $q_x=a+3d/11$, $q_y=a+9d/11$. Hence

$$
L_P=\left(2\left(\frac3{11}\right)^2+\left(\frac6{11}\right)^2+3\left(\frac2{11}\right)^2\right)[d]^2
=\frac6{11}[d]^2
$$

The coefficient $6/11$ has been obtained directly by projecting the polyform.

## Eliminating a single vertex

First eliminate only vertex $x$, retaining all others. Let $d_x=\sum_{p\ne x}c_{xp}>0$ denote the sum of its incident coupling coefficients. The Dirichlet equation for projections gives

$$
q_x=\frac1{d_x}\sum_{p\ne x}c_{xp}p,\qquad r_x=x-q_x
$$

> [!info] Single-vertex elimination lemma
> The part of the Laplacian containing the couplings incident to $x$ decomposes as
>
> $$
> \sum_{p\ne x}c_{xp}[x-p]^2
> =d_x[r_x]^2+\frac1{d_x}\sum_{\substack{p<q\\p,q\ne x}}c_{xp}c_{xq}[(pq)]^2
> \tag{2}
> $$
>
> The first term vanishes under projection. The coupling coefficients between the remaining vertices are therefore
>
> $$
> \boxed{c'_{pq}=c_{pq}+\frac{c_{px}c_{xq}}{d_x},\qquad p\ne q}
> \tag{3}
> $$

Here $(pq)=q-p$ denotes the vector of a vertex pair. In (3), $c_{pq}$ is the previous coupling coefficient, and the second term is the induced increment. If both vertices were coupled to $x$, the increment is positive, including when no coupling $pq$ previously existed.

> [!proof]- Proof of the lemma
> Substitute $x-p=r_x+(q_x-p)$ and expand the quadratic forms. The mixed part is $\{r_x,\sum_pc_{xp}(q_x-p)\}=0$, because the sum in the second argument is zero. Here $\{u,v\}=[u,v]+[v,u]$ is the polar form. This leaves
>
> $$
> \sum_pc_{xp}[x-p]^2=d_x[r_x]^2+\sum_pc_{xp}[q_x-p]^2
> $$
>
> Expanding the last square and using $\sum_pc_{xp}p=d_xq_x$ gives
>
> $$
> \sum_pc_{xp}[q_x-p]^2
> =\sum_pc_{xp}[p]^2-d_x[q_x]^2
> =\frac1{d_x}\sum_{p<q}c_{xp}c_{xq}[q-p]^2
> $$
>
> The last equality is the decomposition of the quadratic form of the frame $q_x$ from the note on coordinates. Point forms in the intermediate expression are used formally; their metric values are not needed here. Adding the couplings not incident to $x$ gives (3). $\square$

### A star becomes a triangle

Let $x$ be joined to $a,b,c$ by three unit couplings. Then $q_x=(a+b+c)/3$, $d_x=3$, and each induced coupling has coefficient $1/3$. Decomposition (2) takes the form

$$
[x-a]^2+[x-b]^2+[x-c]^2
=\frac13\left([(ab)]^2+[(ac)]^2+[(bc)]^2\right)+3[r_x]^2
$$

![[Eliminating the Center of a Star.svg]]

*Figure 1. Eliminating the center of a unit star. The numbers beside the couplings are their coefficients; vertex positions are schematic. The center $x$ is not identified with any retained vertex.*

In the original star, the effective resistance between any two leaves is $2$. In the resulting triangle, the pair $a,b$ has a direct coupling with edge resistance $3$ and a path through $c$ with resistance $6$. Their combined effective resistance is $(1/3+1/6)^{-1}=2$. This checks the example; general preservation of the metric will be proved below.

With three or more retained vertices, an individual induced coupling coefficient generally differs from the reciprocal of the pairwise effective resistance. In this example, $c^{(P)}_{ab}=1/3$, whereas $1/R_{ab}=1/2$: the path through the third vertex also contributes to the effective resistance.

### Sequential elimination along the path

On the path $a-x-y-b$, eliminate $x$ first. The increment to the coupling $ay$ is $2\cdot1/(2+1)=2/3$. Then eliminate $y$ to obtain

$$
c^{(P)}_{ab}=\frac{(2/3)\cdot3}{2/3+3}=\frac6{11}
$$

![[Sequential Elimination Along a Path.svg]]

*Figure 2. Two elimination steps. Each step uses the current coupling coefficients. Vertices $a,b$ are retained throughout the calculation.*

In the reverse order, the first step gives a coupling $xb$ of coefficient $3/4$, and the second gives a coupling $ab$ of coefficient $2(3/4)/(2+3/4)=6/11$. We will establish general independence of the order through the Dirichlet problem.

## Response at the selected vertices

Prescribe values $f_p$ on $P$ and find their extension $f_x=\sum_pb_{xp}f_p$. The balance at each internal vertex is zero. At the retained vertices, compute

$$
j_p=\sum_{j\in\mathcal V}c_{pj}(f_p-f_j),\qquad p\in P
$$

We call $j_p$ the response at vertex $p$. In the electrical interpretation, $f$ represents vertex potentials, and $j_p$ is the current injected into the network. The definition itself uses only coupling coefficients and function values.

Order the vertices with $P$ first and $I$ second. The matrix representation of the original Laplacian is

$$
\mathbf L=
\begin{pmatrix}
\mathbf L_{PP}&-\mathbf C^{\mathsf T}\\
-\mathbf C&\mathbf A
\end{pmatrix},\qquad
\mathbf A=\mathbf L_{II},\qquad C_{xp}=c_{xp}
$$

The internal block $\mathbf A$ is positive definite; its diagonal also accounts for couplings to $P$. It is not the Laplacian of the graph obtained by deleting the selected vertices. From the Dirichlet problem, we have $\mathbf B=\mathbf A^{-1}\mathbf C$ and $\mathbf f_I=\mathbf B\mathbf f_P$.

> [!info] The response matrix and induced couplings
> **Theorem.** The response of the original graph and the polyform (1) are determined by the same matrix:
>
> $$
> \boxed{\mathbf j_P=\boldsymbol\Lambda\mathbf f_P,\qquad
> \boldsymbol\Lambda=\mathbf L_{PP}-\mathbf C^{\mathsf T}\mathbf A^{-1}\mathbf C}
> \tag{4}
> $$
>
> The polyform $L_P$ is the Laplacian of a graph on $P$:
>
> $$
> L_P=\sum_{\substack{p<q\\p,q\in P}}c^{(P)}_{pq}[(pq)]^2,\qquad
> c^{(P)}_{pq}=-\Lambda_{pq}
> =c_{pq}+\sum_{x\in I}c_{px}b_{xq}\ge0
> \tag{5}
> $$

> [!proof]- Proof
> Substituting $\mathbf f_I=\mathbf A^{-1}\mathbf C\mathbf f_P$ into $\mathbf j_P=\mathbf L_{PP}\mathbf f_P-\mathbf C^{\mathsf T}\mathbf f_I$ gives (4).
>
> In the polyform (1), replace each vertex by its projection. The coefficient matrix of the result is
>
> $$
> \mathbf L_{PP}-\mathbf C^{\mathsf T}\mathbf B-\mathbf B^{\mathsf T}\mathbf C+\mathbf B^{\mathsf T}\mathbf A\mathbf B
> =\mathbf L_{PP}-\mathbf C^{\mathsf T}\mathbf A^{-1}\mathbf C
> $$
>
> This matrix is symmetric. Its row sums are zero, because constant prescribed values extend to a constant function and produce zero response. For $p\ne q$, its entries are $-c_{pq}-\sum_xc_{px}b_{xq}\le0$: nonnegativity of $b_{xq}$ was proved in the note on the Dirichlet problem. The matrix is therefore a Laplacian with coefficients (5). $\square$

The influence matrix $\mathbf B$ and the response matrix $\boldsymbol\Lambda$ perform different tasks: the first extends values to internal vertices, while the second computes the response at retained vertices. The set $P$ is not a boundary in the sense of the operator $\partial$.

Expression (4) is called the **Schur complement** with respect to the internal block. The corresponding vertex elimination is known as **Kron reduction** [1]. This name refers to the graph operation considered here; the separate construction of reduction of arbitrary polyforms is not used.

### Energy and the order of elimination

Recall the numerical function $E_G(f)=\sum_{i<j}c_{ij}(f_i-f_j)^2$. With values on $P$ fixed, its unique minimum is attained at the solution of the Dirichlet problem. For this solution, $f_i=f(q_i)$ if the prescribed values are extended affinely over $\mathcal A_P$. Substitution into (1) gives

$$
\min_{f_I}E_G(f)=E_P(f_P)
=\sum_{p<q}c^{(P)}_{pq}(f_p-f_q)^2
\tag{6}
$$

Here we substitute function values into the arguments of the forms; this is distinct from their resistance-metric evaluation.

On the path, the prescribed values $f_a=0$, $f_b=11$ extend to $f_x=3$, $f_y=9$. In the original graph, the energy is $2\cdot3^2+6^2+3\cdot2^2=66$. In the new graph, it is $(6/11)\cdot11^2=66$, and the response in both models is $j_a=-6$, $j_b=6$.

**Corollary.** The result of eliminating internal vertices does not depend on their order.

> [!proof]- Proof of independence of the order
> Each single-vertex elimination step minimizes the energy over that vertex's value with all other values fixed. The resulting minimum becomes a new function of the remaining values. Eliminating all internal variables sequentially gives the same minimum as eliminating them simultaneously. Thus every order gives the same function $E_P(f_P)$ for all prescribed values. A quadratic function uniquely determines its symmetric coefficient matrix, so all coupling coefficients also agree. $\square$

The resulting graph is connected. Indeed, zero energy in (6) is possible only for constant values on $P$: their minimizing extension must be constant on the original connected graph. A disconnected graph on $P$ would admit nonconstant values with zero energy.

## Decomposing the Laplacian over two subspaces

Return to the residual vectors $r_x$. Together they generate the orthogonal complement $W_P^\perp$ within $W$. This means that every vector in $W$ has a unique representation as the sum of a vector in $W_P$ and a linear combination of the $r_x$ orthogonal to $W_P$.

> [!info] Decomposition of the Laplacian polyform
> **Theorem.** For projections defined by the original resistance metric,
>
> $$
> \boxed{L=L_P+L_\perp,\qquad
> L_\perp=\sum_{i<j}c_{ij}[r_j-r_i]^2}
> \tag{7}
> $$
>
> The arguments of $L_P$ belong to $W_P$, and those of $L_\perp$ belong to $W_P^\perp$. For retained vertices, we use $r_p=0$.

> [!proof]- Proof of the decomposition
> Substitute $a_j-a_i=(q_j-q_i)+(r_j-r_i)$ into the original Laplacian. In addition to $L_P$ and $L_\perp$, this produces the mixed part
>
> $$
> \sum_{i<j}c_{ij}\{q_j-q_i,r_j-r_i\}
> =\sum_i\left\{\sum_jc_{ij}(q_i-q_j),r_i\right\}
> $$
>
> For $i\in P$, the second argument is zero. For $i\in I$, the first argument is zero by the Dirichlet equations for projections. The entire mixed polyform is zero. This is a formal equality, stronger than the vanishing of its numerical metric evaluation. $\square$

For our path, the decomposition becomes

$$
L=\frac6{11}[(ab)]^2+2[r_x]^2+[r_y-r_x]^2+3[r_y]^2
$$

Contracting $a,b$ to a single vertex $o$ gives a triangle with couplings $ox=2$, $xy=1$, $oy=3$. Its Laplacian becomes $L_\perp$ under the substitution $(ox)\mapsto r_x$, $(oy)\mapsto r_y$. This is the isometry established in the [[Selected Vertices and the Dirichlet Problem#Contraction and the metric of residuals|note on the Dirichlet problem]].

Thus eliminating internal vertices preserves the part of the geometry on $W_P$, while contracting all selected vertices describes the orthogonal part on $W_P^\perp$. These are two different passages from the same original space.

## Factoring the exponential and preserving the metric

Set $M=\exp L$, $M_P=\exp L_P$, $M_\perp=\exp L_\perp$. Commutativity of the product of forms and (7) give

$$
\boxed{M=M_PM_\perp,\qquad \pi(M)=M_P}
\tag{8}
$$

The exponential here is taken in polyform algebra. The equality involving projection follows from (1) and preservation of the product under projection; $\pi(M_\perp)=e$, where $e$ is the unit form.

For the star with three leaves, $L_\perp=3[r_x]^2$. Since $([r_x]^2)^2=0$, we have $M_\perp=e+3[r_x]^2$. Eliminating the center leaves the factor $M_P$ associated with the plane of triangle $abc$.

Let $\tau_G=u_M(e)$ be the spanning-tree coefficient of the original graph and $\tau_P=u_{M_P}(e)$ that of the resulting graph. These potentials are computed using different spanning-tree forms: one on all original vertices, the other on the vertices of $P$.

> [!info] Preservation of normalized potentials
> **Theorem.** For any form $\Phi$ whose arguments belong to exterior powers of $W_P$,
>
> $$
> \tau_G=\tau_P\det\mathbf A,\qquad
> u_M(\Phi)=\det\mathbf A\,u_{M_P}(\Phi)
> \tag{9}
> $$
>
> Consequently,
>
> $$
> \boxed{\frac{u_M(\Phi)}{u_M(e)}
> =\frac{u_{M_P}(\Phi)}{u_{M_P}(e)}}
> \tag{10}
> $$

> [!proof]- Proof using the top grades
> Choose $p_0\in P$ and order the other retained vertices, followed by the internal vertices $x_1,\ldots,x_m$. Here $m=|I|$. Replace the vector basis $p-p_0$, $x-p_0$ by $p-p_0$, $r_x$. This change has determinant $1$, since
>
> $$
> r_x=(x-p_0)-\sum_{p\in P}b_{xp}(p-p_0)
> $$
>
> Therefore, for $T_P=[(p_0\ldots p_{|P|-1})]^2$ and $T_\perp=[r_{x_1}\wedge\cdots\wedge r_{x_m}]^2$, the product $T_PT_\perp$ is the original spanning-tree form. Orientation signs disappear in the quadratic form.
>
> The coefficient matrix of $L_\perp$ in the basis $r_x$ is $\mathbf A$. The top-grade component of $M_\perp$ is therefore $(\det\mathbf A)T_\perp$, by the determinant formula for the exponential in the PMG core. This is also the spanning-tree coefficient of the graph in which all of $P$ is contracted to one vertex.
>
> In factorization (8), multiplied by $\Phi$, the full top grade can arise only from the top grade on each of the two subspaces. Its coefficient is therefore $\det\mathbf A$ times the top coefficient of $M_P\Phi$. This proves the second equality in (9). Setting $\Phi=e$ gives the first; division gives (10). $\square$

By the metric identity, the normalized potential of $[u,v]$ equals the inner product $u\cdot v$. Thus (10) proves preservation of the entire metric on $W_P$. In particular, it preserves the effective resistances $R_{pq}$ and the metric values of exterior objects on this subspace, including areas and volumes of simplices with vertices in $P$.

The unnormalized potentials and the spanning-tree coefficient do change. For the path,

$$
\mathbf A=\begin{pmatrix}3&-1\\-1&4\end{pmatrix},\qquad
\det\mathbf A=11,\qquad
\tau_G=6,\qquad \tau_P=\frac6{11}
$$

In the new graph, $M_P=e+(6/11)[(ab)]^2$, so $u_{M_P}([(ab)]^2)=1$. In the original graph, $u_M([(ab)]^2)=11$. After normalization, both give $11/6$.

For the star, $\tau_G=1$, $\det\mathbf A=3$, $\tau_P=1/3$: the triangle has three spanning trees, each of weight $1/9$. We can also check the second grade. In the original metric, the vectors $b-a$, $c-a$ have norms $2$ and inner product $1$, so $(abc)^2=2\cdot2-1^2=3$. In the triangle, the normalized potential of the top-grade form gives the same result: $1/\tau_P=3$. The squared geometric area is $3/4$.

## Resistance radius and projection of the circumcenter

Preservation of the metric allows us to compare the resistance radii of the original and induced graphs. Recall the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|definition]]: the resistance radius $\rho$ is the squared circumradius of the basis. Let $h$ be the circumcenter of the original graph, and let $h_P\in\mathcal A_P$ be the circumcenter of the selected vertices. Both centers are considered in the original metric.

> [!info] Resistance radius of the selected subspace
> **Lemma.** For any nonempty set of selected vertices of a connected graph, the center $h_P$ is the orthogonal projection of $h$ onto $\mathcal A_P$. Therefore
>
> $$
> \boxed{\rho_G=\rho_P+\|h-h_P\|^2,\qquad \rho_P\le\rho_G}
> \tag{11}
> $$
>
> For a single selected vertex, its center is the vertex itself and $\rho_P=0$.

> [!proof]- Projection of the circumcenter
> Let $h'$ be the orthogonal projection of $h$ onto $\mathcal A_P$. For any vertex $p\in P$, the Pythagorean theorem gives
>
> $$
> \|p-h'\|^2=\|p-h\|^2-\|h-h'\|^2
> =\rho_G-\|h-h'\|^2
> $$
>
> The right-hand side is independent of $p$. Thus $h'$ is equidistant from the selected vertices and lies in their affine subspace. These vertices are affinely independent, so their circumcenter is unique: $h'=h_P$. Preservation of the metric identifies this sphere with the circumsphere of the induced graph. This proves (11). $\square$

For a star with three unit couplings, the tree resistance radius formula gives $\rho_G=3/4$. Its leaves form an equilateral triangle with squared side length $2$, so $\rho_P=2/3$. Formula (11) gives $\|h-h_P\|^2=1/12$.

The lemma applies to any selected vertex set. In a [[Couplings Within One Part of a Bipartite Graph#Why the resistance radii of the parts do not add up|bipartite graph]], it applies separately to each part.

## Conditions and limitations

For a connected graph with nonnegative coupling coefficients, any nonempty $P$ determines a unique result. Reconstruction of the graph from the preserved resistance metric is unique by the [[Laplacian, Green Matrix, and Effective Resistance Matrix|formulas converting a resistance matrix to a Laplacian]].

If only one vertex is retained, $W_P$ has dimension zero, $L_P=0$, $M_P=e$. The response is zero for any prescribed value. The spanning-tree coefficient of a one-vertex graph is taken to be $1$, and (9) becomes the usual Kirchhoff formula $\tau_G=\det\mathbf A$. If all vertices are retained, there is nothing to eliminate and $L_P=L$.

For a disconnected graph, distinguish two cases.

- If every component contains a selected vertex, the internal block $\mathbf A$ is invertible. The response and induced-coupling formulas apply to the whole graph. No new couplings arise between different components; metric identities and normalizations are applied separately within each component.
- A component with no selected vertex makes the full internal block singular. Its constant value is arbitrary and does not affect the response on $P$. To compute that response, such a component can be treated separately and discarded as a whole; the formula $\mathbf A^{-1}$ cannot be applied to the full block.

For example, take two disconnected couplings $a-x$ and $b-y$ with $P=\{a,b\}$. Eliminating $x,y$ leaves two isolated vertices. A zero response matrix does not mean that the effective resistance between them is zero: a finite resistance metric between components is not defined here. If instead $P=\{a\}$, the second component does not contribute to the response at all.

With coefficients of different signs, some algebraic identities may remain valid, but positivity of the metric, existence of a minimum, and nonnegativity of induced couplings require separate checks. Such graphs are outside the main setting of this note.

The null vector $z$ is not required for these results. We restricted the metric of affine vectors and their exterior products. Metric evaluation of the formal points themselves outside this space was not used in the proofs.

## Moving to bipartite graphs

In a bipartite graph, we can retain one part and eliminate the other. There are no couplings between the eliminated vertices, so the internal block $\mathbf A$ is diagonal. Each eliminated vertex adds couplings between its neighbors according to (3). This provides a construction for passing from a rectangular table of couplings between two sets of objects to couplings within one set. This is developed in [[Couplings Within One Part of a Bipartite Graph]].

## Sources and status of the results

Vertex elimination, the Schur complement, Kron reduction, and preservation of effective resistances are classical results [1]. This note derives them for the adopted graph model and represents them through projection of arguments, decomposition of the Laplacian, and factorization of the metric polyform. This presentation makes no claim of novelty for the classical operation itself.

The text uses the current definitions in the [[Core specification|core specification]] and [[PMG terminology|terminology]], together with the names for bi-coordinates and graph quantities agreed on in this series.

The path and star calculations are given in the text. In addition, eight settings were checked using exact rational arithmetic, including cases with one selected vertex and with all vertices selected. Projections computed from the original Gram matrix were compared with induced couplings and the response matrix. Direct exterior multiplication verified the factorization of the exponential and normalized potentials on bases of every exterior grade of the retained subspace. Elimination order and disconnected cases were checked separately. These checks verify formulas and examples; the general statements rest on the proofs given above. The note contains no hypotheses.

1. Dörfler, F.; Bullo, F. [Kron Reduction of Graphs with Applications to Electrical Networks](https://arxiv.org/abs/1102.2950). Preprint, 2011. Formula (3.4): single-vertex elimination; Lemma 3.3: sequential elimination; Theorem 3.9: preservation of effective resistances.

