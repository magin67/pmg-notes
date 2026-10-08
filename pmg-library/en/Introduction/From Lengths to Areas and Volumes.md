---
title: "From Lengths to Areas and Volumes"
date: 2026-10-04
updated: 2026-10-08
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: lengths-areas-volumes
lang: en
description: "Gram determinants, areas, and volumes of resistance simplices. Connections with the spanning-tree coefficient and edge-inclusion probabilities in a random spanning tree."
---

Inner products determine lengths and angles as well as areas, volumes, and their higher-dimensional analogues. The squares of these quantities are expressed by Gram determinants. In the resistance representation of a graph, Gram matrix entries are computed from effective resistances, and Gram determinants are related to spanning trees.

We consider a finite connected undirected graph without loops on $n\ge2$ vertices, with positive edge conductances. We retain the notation $a_{ij}=a_j-a_i$ for affine vectors and $G=L^+$ for the Green matrix. From the preceding notes,

$$
\|a_{ij}\|^2=R_{ij},\qquad
a_{ij}\cdot a_{kl}=\frac12(R_{il}+R_{jk}-R_{ik}-R_{jl})
$$

## The Gram determinant and area

> [!info] The Gram matrix
> **Definition.** For Euclidean vectors $u_1,\ldots,u_k$, the matrix
>
> $$
> G(u_1,\ldots,u_k)=(u_i\cdot u_j)_{i,j=1}^k
> $$
>
> is called the Gram matrix, and its determinant is called the Gram determinant. The notation $G$ without arguments continues to denote the Green matrix of the graph.

For nonzero vectors $u,v$ with angle $\theta$ between them, the area of the parallelogram is $\|u\|\|v\|\sin\theta$. Substituting $u\cdot v=\|u\|\|v\|\cos\theta$ gives

$$
S_{\parallel}^2=\|u\|^2\|v\|^2-(u\cdot v)^2
=\det\begin{pmatrix}u\cdot u&u\cdot v\\v\cdot u&v\cdot v\end{pmatrix}
\tag{1}
$$

Formula (1) remains valid when one of the vectors is zero: both sides vanish. The triangle spanned by the same vectors has half the area of the parallelogram, so

$$
S_\triangle^2=\frac14\det G(u,v)
\tag{2}
$$

## The area of a triangle from its side lengths

For a triangle with vertices $a_1,a_2,a_3$, set $u=a_{12}$, $v=a_{13}$ and denote the side lengths by $\ell_{12},\ell_{13},\ell_{23}$. Then

$$
u\cdot v=\frac{\ell_{12}^2+\ell_{13}^2-\ell_{23}^2}{2}
$$

Formula (2) gives

$$
4S_\triangle^2=\ell_{12}^2\ell_{13}^2
-\frac14(\ell_{12}^2+\ell_{13}^2-\ell_{23}^2)^2
$$

This identity is equivalent to Heron's formula:

$$
S_\triangle^2=p(p-\ell_{12})(p-\ell_{13})(p-\ell_{23}),\qquad
p=\frac{\ell_{12}+\ell_{13}+\ell_{23}}2
$$

For three distinct graph vertices $i,j,k$, we have $\ell_{ij}^2=R_{ij}$. Hence

$$
\det G(a_{ij},a_{ik})
=R_{ij}R_{ik}-\frac14(R_{ij}+R_{ik}-R_{jk})^2
$$

Expanding the square gives a symmetric formula for the area of the resistance triangle:

$$
16S_{ijk}^2=2R_{ij}R_{ik}+2R_{ik}R_{jk}+2R_{jk}R_{ij}
-R_{ij}^2-R_{ik}^2-R_{jk}^2
$$

> [!example] The resistance triangle of $K_3$
> In the complete graph on three vertices with unit conductances, $R_{12}=R_{13}=R_{23}=2/3$. For $u=a_{12}$ and $v=a_{13}$, we obtain
>
> $$
> G(u,v)=\begin{pmatrix}\frac23&\frac13\\\frac13&\frac23\end{pmatrix},\qquad
> \det G(u,v)=\frac49-\frac19=\frac13
> $$
>
> Formula (2) gives $S_\triangle^2=1/12$. An independent check uses the area of an equilateral triangle with side length $\ell=\sqrt{2/3}$:
>
> $$
> S_\triangle^2=\frac3{16}\ell^4=\frac3{16}\cdot\frac49=\frac1{12}
> $$

## Volumes of parallelotopes and simplices

> [!info] A parallelotope
> **Definition.** The vectors $u_1,\ldots,u_k$ define the parallelotope
>
> $$
> \left\{\sum_{i=1}^k t_i u_i:0\le t_i\le1\right\}
> $$
>
> Its dimension is the rank of the system of vectors. If they are linearly dependent, it is degenerate as a $k$-dimensional figure and its $k$-dimensional volume is zero.

> [!info] Volume formulas
> **Theorem.** The squared $k$-dimensional volume of the parallelotope is
>
> $$
> V_{\parallel}^2=\det G(u_1,\ldots,u_k)
> \tag{3}
> $$
>
> For a simplex with vertices $p_0,\ldots,p_k$ and vectors $u_i=p_i-p_0$,
>
> $$
> V_\triangle^2=\frac{\det G(u_1,\ldots,u_k)}{(k!)^2}
> \tag{4}
> $$
>
> The notation $V_\triangle$ denotes the volume of a simplex in any dimension. Both formulas include the degenerate case.

> [!note]- Proof of the Gram formula
> **Proof.** Suppose the vectors are linearly independent. Choose an orthonormal basis of their $k$-dimensional span and form the square matrix $U$ whose columns are their coordinate vectors. Then $G(u_1,\ldots,u_k)=U^{\mathsf T}U$, and the volume of the parallelotope is $|\det U|$. Therefore,
>
> $$
> \det G(u_1,\ldots,u_k)=(\det U)^2=V_{\parallel}^2
> $$
>
> If the vectors are linearly dependent, the Gram matrix is singular and the $k$-dimensional volume is zero. The simplex spanned by the same vectors has $1/k!$ times the volume of the parallelotope: they are the images of the standard simplex and the unit cube, respectively, under the same linear map. This gives (4). $\square$

For $k=3$, formula (3) computes the squared volume of a parallelepiped, while for a tetrahedron the factor in (4) is $1/(3!)^2=1/36$.

The Gram determinant vanishes if and only if the vectors are linearly dependent. For two vectors, the figure may degenerate into a segment or a point; for three, its dimension may drop to two, one, or zero. The determinant also depends on the scales of the vectors and is not, by itself, a dimensionless measure of nondegeneracy.

## The Cayley-Menger determinant

Let $\ell_{ij}=\|p_j-p_i\|$ for vertices $p_0,\ldots,p_k$, and define the matrix

$$
M=\begin{pmatrix}
0&1&1&\cdots&1\\
1&0&\ell_{01}^2&\cdots&\ell_{0k}^2\\
1&\ell_{10}^2&0&\cdots&\ell_{1k}^2\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&\ell_{k0}^2&\ell_{k1}^2&\cdots&0
\end{pmatrix}
$$

> [!info] The Cayley-Menger formula
> The squared volume of a simplex is expressed through its squared side lengths:
>
> $$
> V_\triangle^2=\frac{(-1)^{k+1}}{2^k(k!)^2}\det M
> \tag{5}
> $$

> [!note]- Relation to the Gram determinant
> **Proof.** Set $u_i=p_i-p_0$. From each row of $M$ corresponding to $p_i$ with $i\ge1$, subtract the row corresponding to $p_0$, then perform the same operations on the columns. The block indexed by $i,j\ge1$ becomes
>
> $$
> \ell_{ij}^2-\ell_{0i}^2-\ell_{0j}^2=-2u_i\cdot u_j
> $$
>
> In the first row and the first column, the only remaining nonzero entry is a single $1$ in the position corresponding to $p_0$. Expanding the determinant along them gives
>
> $$
> \det M=-\det(-2G(u_1,\ldots,u_k))
> =(-1)^{k+1}2^k\det G(u_1,\ldots,u_k)
> $$
>
> Substitution into (4) proves (5). $\square$

For a resistance simplex, the entries substituted into $M$ are the effective resistances $R_{ij}$, which already equal squared distances. They must not be squared again in this substitution.

## The spanning-tree coefficient as a Gram determinant

> [!info] The spanning-tree coefficient
> **Definition.** For a weighted graph,
>
> $$
> \tau=\sum_T\prod_{e\in T}c_e
> $$
>
> where the sum runs over all spanning trees. A spanning tree contains every vertex of the graph, is connected, and has no cycles. When all conductances are one, $\tau$ is the number of spanning trees.

Choose an orientation for each edge. Let $B$ be the incidence matrix: the column of an edge oriented from $i$ to $j$ is $\mathbf e_j-\mathbf e_i$. Denote the diagonal matrix of edge conductances by $W=\operatorname{diag}(c_e)$. Then $L=BWB^{\mathsf T}$.

Choose a vertex $0$, relabeling the vertices as $0,1,\ldots,n-1$. Delete its row from $B$ to obtain $B_0$. Deleting the row and column of this vertex from $L$ gives the reduced Laplacian

$$
L_0=B_0WB_0^{\mathsf T}=AA^{\mathsf T},\qquad A=B_0W^{1/2}
$$

Thus $L_0$ is the Gram matrix of the $n-1$ rows of $A$. By the weighted matrix-tree theorem,

$$
\det L_0=\tau
\tag{6}
$$

> [!note]- Derivation by the Cauchy-Binet formula
> **Proof.** For an edge set $F$ of size $n-1$, let $B_{0,F}$ be the square submatrix consisting of the corresponding columns. The Cauchy-Binet formula gives
>
> $$
> \det L_0=\sum_{|F|=n-1}(\det B_{0,F})^2\prod_{e\in F}c_e
> $$
>
> If $F$ contains a cycle, the columns are linearly dependent and the determinant is zero. An acyclic set of $n-1$ edges on $n$ vertices is a spanning tree. For a tree, $\det B_{0,F}=\pm1$: this follows by successively expanding along rows corresponding to leaves other than vertex $0$. Exactly the weights of spanning trees remain in the sum, proving (6). $\square$

By (3), the spanning-tree coefficient is the squared volume of the parallelotope spanned by the rows of $A$. These vectors lie in the space of edge coordinates and differ from the affine vectors of the resistance representation.

## The volume of the full resistance simplex

Consider the affine vectors $a_{0i}$ for $i=1,\ldots,n-1$, and denote their Gram matrix by $G_R$. Its entries are

$$
(G_R)_{ij}=a_{0i}\cdot a_{0j}=\frac12(R_{0i}+R_{0j}-R_{ij})
$$

> [!info] The Gram matrix relative to one vertex
> **Lemma.** The Gram matrix of resistance vectors based at vertex $0$ is
>
> $$
> G_R=L_0^{-1}
> \tag{7}
> $$

> [!note]- Proof using potentials
> **Proof.** Inject a unit current at vertex $j$ and withdraw it at vertex $0$. Choose the reference potential $\varphi_0=0$. The equations for the remaining vertices are
>
> $$
> L_0\widehat\varphi=\widehat{\mathbf e}_j
> $$
>
> Here $\widehat\varphi$ contains the potentials at vertices $1,\ldots,n-1$, and $\widehat{\mathbf e}_j$ is the corresponding standard basis column vector. Hence $\varphi_i=(L_0^{-1})_{ij}$.
>
> By the [[Inner Product of Graph Vectors#Electrical interpretation|electrical interpretation of the inner product]],
>
> $$
> \varphi_i-\varphi_0=a_{0i}\cdot a_{0j}=(G_R)_{ij}
> $$
>
> This proves (7) for all $i,j$. $\square$

Formulas (6) and (7) imply $\det G_R=1/\tau$. Thus, for the parallelotope spanned by the vectors $a_{0i}$ and for the full resistance simplex,

$$
V_{\parallel,R}^2=\frac1\tau,\qquad
V_R^2=\frac1{((n-1)!)^2\tau}
\tag{8}
$$

> [!example] The spanning-tree coefficient and area for $K_3$
> The triangle graph with unit conductances has three spanning trees, so $\tau=3$. Choosing vertex $1$ as the reference vertex gives
>
> $$
> L_0=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
> L_0^{-1}=\begin{pmatrix}\frac23&\frac13\\\frac13&\frac23\end{pmatrix}
> $$
>
> The inverse matrix equals the previously computed Gram matrix $G(a_{12},a_{13})$. Formula (8) gives $S_\triangle^2=1/((2!)^2\cdot3)=1/12$, in agreement with the direct area calculation.

## Edge-inclusion probabilities in a spanning tree

For an edge $e$ oriented from $i$ to $j$, set $t_e=a_{ij}$, $R_e=R_{ij}$, and $g(e,f)=t_e\cdot t_f$. Choose a random spanning tree $T$ according to the distribution

$$
\Pr(T)=\frac1\tau\prod_{e\in T}c_e
$$

> [!info] The transfer-current theorem
> For pairwise distinct unoriented edges $e_1,\ldots,e_k$, each assigned an arbitrary orientation,
>
> $$
> \Pr(e_1,\ldots,e_k\in T)
> =\left(\prod_{r=1}^k c_{e_r}\right)\det G(t_{e_1},\ldots,t_{e_k})
> \tag{9}
> $$

Formula (9) expresses the transfer-current theorem through the Gram matrix of resistance vectors. A proof is given in R. Lyons and Y. Peres, *Probability on Trees and Networks*, Section 4.2, “Electrical Interpretations,” under “The Transfer-Current Theorem,” formula (4.5) ([open full text](https://rdlyons.pages.iu.edu/prbtree/), source [9] in [[Further Reading for the PMG Introductory Series|the reading recommendations]]).

For one edge, $\Pr(e\in T)=c_eR_e$. For two **distinct** edges,

$$
\Pr(e,f\in T)=c_ec_f\bigl(R_eR_f-g(e,f)^2\bigr)
$$

By (1), the expression in parentheses is the squared area of the parallelogram spanned by $t_e,t_f$. Reversing the orientation of an edge changes the signs of the corresponding row and column of the Gram matrix, leaving its determinant unchanged. If the chosen edges contain a cycle, their vectors are linearly dependent and both sides of (9) vanish.

> [!example] Two edges of a triangle
> In $K_3$ with unit conductances, two specified distinct edges belong to exactly one of the three equally likely spanning trees. Their joint inclusion probability is therefore $1/3$. This direct count agrees with (9): the conductances are one, and the Gram determinant of the two vectors is $1/3$.

Higher-order determinants describe volumes and joint edge-inclusion probabilities. They are not two-point effective resistances.

## Further reading

[[Variation of a Single Edge]] examines how resistances and the spanning-tree coefficient change when one conductance varies. The connection between Gram determinants and exterior products will be introduced after the algebra is defined, in [[Basic Objects and Operations of Polyform Algebra]] and [[Metric of Higher-Grade Objects]].

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], sources [7] and [8] cover Gram determinants and multilinear algebra, [3] covers the matrix-tree theorem, and [9] covers random spanning trees and the transfer-current theorem.
