---
date: 2026-10-04
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: lengths-areas-volumes
lang: en
description: How lengths and inner products give rise to areas and volumes, why their squares are Gram determinants, and how this geometry is connected with effective resistance and spanning trees.
title: From Lengths to Areas and Volumes
---

Effective resistance allows us to regard a graph as a metric space: the resistance $R_{ij}$ plays the role of the squared distance between vertices, while mixed measurements between graph vectors give their inner products.

But geometry does not end with lengths and angles. The same inner products determine areas, volumes, and their higher-dimensional analogues. The key object here is the **Gram determinant**.

This construction is especially important for graphs. It connects three aspects of the same problem that at first seem unrelated:

- geometry - through areas and volumes;
- electrical networks - through effective resistances and transfer quantities;
- combinatorics - through spanning trees.

## From length to area

Let $u$ and $v$ be two vectors. Their lengths are $\|u\|$ and $\|v\|$, and let the angle between them be $\theta$.

The area of the parallelogram spanned by these vectors is
$$
S_{\parallel}=\|u\|\,\|v\|\sin\theta.
$$
On the other hand,
$$
u\cdot v=\|u\|\,\|v\|\cos\theta.
$$
Therefore
$$
S_{\parallel}^2
=
\|u\|^2\|v\|^2-(u\cdot v)^2.
\tag{1}
$$
The right-hand side can be written as a determinant:
$$
\boxed{
S_{\parallel}^2=
\det
\begin{pmatrix}
u\cdot u & u\cdot v\\
v\cdot u & v\cdot v
\end{pmatrix}.
}
\tag{2}
$$

Thus, area arises directly from inner products. The angle $\theta$ is no longer needed in the final formula.

> [!definition] Gram matrix and Gram determinant
> For vectors $u_1,\ldots,u_k$, the **Gram matrix** is the matrix of their pairwise inner products:
> $$
> G(u_1,\ldots,u_k)=
> \begin{pmatrix}
> u_1\cdot u_1 & \cdots & u_1\cdot u_k\\
> \vdots & \ddots & \vdots\\
> u_k\cdot u_1 & \cdots & u_k\cdot u_k
> \end{pmatrix}.
> $$
> Its determinant
> $$
> \det G(u_1,\ldots,u_k)
> $$
> is called the **Gram determinant**.

For two vectors, formula (2) says that the Gram determinant equals the squared area of the parallelogram.

If we need the area of the triangle spanned by the same two vectors, it is half as large:
$$
S_\triangle=\frac12S_{\parallel}.
$$
Therefore
$$
\boxed{
S_\triangle^2=
\frac14\det G(u,v).
}
\tag{3}
$$

## A triangle from its side lengths

Consider a triangle with vertices $a,b,c$ and choose two vectors issuing from $a$:
$$
u=b-a,\qquad v=c-a.
$$
Let the side lengths be
$$
\|u\|=c,\qquad
\|v\|=b,\qquad
\|v-u\|=a.
$$
From the formula expressing an inner product through three distances,
$$
u\cdot v=
\frac{b^2+c^2-a^2}{2}.
$$
Substituting this into the Gram determinant gives
$$
4S_\triangle^2
=
b^2c^2-
\frac14(b^2+c^2-a^2)^2.
$$
After expanding,
$$
\boxed{
16S_\triangle^2
=
2a^2b^2+2b^2c^2+2c^2a^2
-a^4-b^4-c^4.
}
\tag{4}
$$

This is a symmetric form of the classical formula usually known as Heron's formula.

If
$$
p=\frac{a+b+c}{2},
$$
then the standard form of Heron's formula is
$$
\boxed{
S_\triangle^2=p(p-a)(p-b)(p-c).
}
\tag{5}
$$

This reveals an important general principle: **area does not require any new independent metric information**. Its square is completely determined by the side lengths, that is, by first-order metric data.

## The resistance triangle

Now return to a graph.

For three vertices $i,j,k$, consider the graph vectors
$$
u=(ij),\qquad v=(ik).
$$
In resistance geometry,
$$
u\cdot u=R_{ij},
\qquad
v\cdot v=R_{ik}.
$$
Their inner product was obtained earlier:
$$
u\cdot v=
\frac{R_{ij}+R_{ik}-R_{jk}}{2}.
$$
Hence
$$
\det G(u,v)
=
R_{ij}R_{ik}
-
\frac14
\left(
R_{ij}+R_{ik}-R_{jk}
\right)^2.
\tag{6}
$$
Since the area of the triangle is half the area of the corresponding parallelogram,
$$
\boxed{
16S_{ijk}^2=
2R_{ij}R_{ik}
+2R_{ik}R_{jk}
+2R_{jk}R_{ij}
-R_{ij}^2-R_{ik}^2-R_{jk}^2.
}
\tag{7}
$$

This is Heron's formula written directly in terms of effective resistances.

Thus, the three pairwise effective resistances determine not only the shape of the resistance triangle, but also its area.

> [!example] The triangle $K_3$
> Consider the complete graph on three vertices with unit conductances.
>
> For every pair of vertices,
> $$
> R_{12}=R_{13}=R_{23}=\frac23.
> $$
> Take
> $$
> u=(12),\qquad v=(13).
> $$
> Then
> $$
> u\cdot v
> =
> \frac{R_{12}+R_{13}-R_{23}}2
> =
> \frac13.
> $$
> Therefore
> $$
> \det G(u,v)
> =
> \frac23\frac23-\frac19
> =
> \frac13.
> $$
> The squared area of the resistance triangle is
> $$
> S_\triangle^2=\frac1{12}.
> $$

## From area to volume

The same principle extends to three vectors.

Let $u,v,w$ be given. The ordinary three-dimensional parallelepiped spanned by these vectors has volume $V_{\parallel}$ satisfying
$$
\boxed{
V_{\parallel}^2=
\det
\begin{pmatrix}
u\cdot u & u\cdot v & u\cdot w\\
v\cdot u & v\cdot v & v\cdot w\\
w\cdot u & w\cdot v & w\cdot w
\end{pmatrix}.
}
\tag{8}
$$

For the tetrahedron determined by the same three vectors issuing from one vertex,
$$
V_{\mathrm{tet}}=\frac1{3!}V_{\parallel}.
$$
Therefore
$$
V_{\mathrm{tet}}^2=
\frac1{(3!)^2}\det G(u,v,w).
$$

No new principle appears here compared with the area case. The Gram matrix simply becomes larger.

## The general case

Let $u_1,\ldots,u_k$ be $k$ vectors.

They span the $k$-dimensional analogue of a parallelepiped. In standard geometric terminology, such a figure is called a **parallelotope**: it is the set of points
$$
t_1u_1+\cdots+t_ku_k,
\qquad
0\leq t_i\leq1.
$$
For $k=2$ this is a parallelogram, and for $k=3$ an ordinary parallelepiped.

The square of its $k$-dimensional volume is
$$
\boxed{
V_k^2=\det G(u_1,\ldots,u_k).
}
\tag{9}
$$

If instead we consider a $k$-dimensional simplex with vertices
$$
p_0,p_1,\ldots,p_k
$$
and
$$
u_i=p_i-p_0,
$$
then its volume is smaller by a factor of $k!$:
$$
\boxed{
V_{\mathrm{simplex}}^2=
\frac{\det G(u_1,\ldots,u_k)}{(k!)^2}.
}
\tag{10}
$$

Thus the same construction gives, step by step:

- for $k=1$ - squared length;
- for $k=2$ - squared area;
- for $k=3$ - squared volume;
- for arbitrary $k$ - squared $k$-dimensional volume.

## Zero determinant and degeneracy

The Gram determinant has another simple geometric meaning.

If the vectors $u_1,\ldots,u_k$ are linearly dependent, the figure they span degenerates and its $k$-dimensional volume is zero. Therefore
$$
\det G(u_1,\ldots,u_k)=0.
$$
The converse is also true in Euclidean geometry:
$$
\boxed{
\det G(u_1,\ldots,u_k)=0
\quad\Longleftrightarrow\quad
u_1,\ldots,u_k
\text{ are linearly dependent}.
}
\tag{11}
$$

For two vectors this means that the parallelogram collapses to a segment. For three, the parallelepiped lies in a single plane.

Thus the Gram determinant measures both the magnitude of an object and whether it is nondegenerate.

## Why the Gram matrix is simpler than distances

The volume of a simplex can also be computed directly from the pairwise distances between its vertices.

For this one uses the **Cayley-Menger determinant**.

Let
$$
d_{ij}^2=\|p_i-p_j\|^2.
$$
Then for a $k$-dimensional simplex,
$$
V_{\mathrm{simplex}}^2
=
\frac{(-1)^{k+1}}{2^k(k!)^2}
\det
\begin{pmatrix}
0 & 1 & 1 & \cdots & 1\\
1 & 0 & d_{01}^2 & \cdots & d_{0k}^2\\
1 & d_{10}^2 & 0 & \cdots & d_{1k}^2\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
1 & d_{k0}^2 & d_{k1}^2 & \cdots & 0
\end{pmatrix}.
\tag{12}
$$

The formula is symmetric in all vertices, but it looks noticeably more complicated than the Gram formula (10).

The origin of the factor $2^k$ becomes clear if we choose one vertex $p_0$ as the origin and pass from distances to the vectors
$$
u_i=p_i-p_0.
$$
Then the entries of their Gram matrix are
$$
\boxed{
u_i\cdot u_j
=
\frac{
d_{0i}^2+d_{0j}^2-d_{ij}^2
}{2}.
}
\tag{13}
$$

Thus the distance matrix must first be converted into a matrix of inner products. This transition introduces a factor $1/2$ in each Gram entry, which leads to the power $2^k$ in the determinant.

From this point of view, the Cayley-Menger determinant and the Gram determinant describe the same volume, but use different input data:

- Cayley-Menger works directly with squared pairwise distances;
- Gram works with inner products of vectors issuing from a chosen vertex.

For later PMG constructions, the second form is usually more natural.

## The spanning-tree count as a squared volume

An unexpected connection with graph combinatorics now appears.

Let $B$ be an oriented incidence matrix of a connected graph, and let
$$
C=\operatorname{diag}(c_e)
$$
be the diagonal matrix of edge conductances.

Delete one row from $B$ and denote the resulting matrix by $B_0$. Then the reduced Laplacian is
$$
L_0=B_0CB_0^T.
$$
It can be written as
$$
L_0=
(B_0C^{1/2})(B_0C^{1/2})^T.
\tag{14}
$$

But a matrix of the form $AA^T$ is the Gram matrix of the rows of $A$. Therefore $L_0$ itself is a Gram matrix for a system of $n-1$ vectors.

Hence
$$
\det L_0
$$
has the geometric meaning of the squared $(n-1)$-dimensional volume of that system.

On the other hand, by Kirchhoff's matrix-tree theorem,
$$
\boxed{
\det L_0=\tau(G),
}
\tag{15}
$$
where $\tau(G)$ is the spanning-tree count of the graph, or, in the weighted case, the sum of the weights of its spanning trees.

Thus one and the same number appears:
$$
\boxed{
\tau(G)
=
\text{the square of a certain }(n-1)\text{-dimensional volume}.
}
\tag{16}
$$

This is one of the important passages between graph combinatorics and geometry. The number of spanning trees appears not only as a counting result - it is also a Gram determinant.

## The inverse side: volume of the resistance simplex

There is also another, in a sense inverse, geometric picture.

Choose a vertex $0$ and consider the $n-1$ graph vectors
$$
u_i=(0i),
\qquad
i=1,\ldots,n-1.
$$
Their inner products are determined by effective resistances:
$$
u_i\cdot u_j
=
\frac{R_{0i}+R_{0j}-R_{ij}}2.
$$
Denote this Gram matrix by $G_R$.

From the relation between the Green matrix and effective resistances,
$$
G_R=L_0^{-1}.
$$
Therefore
$$
\det G_R
=
\frac1{\det L_0}
=
\frac1{\tau(G)}.
\tag{17}
$$

Thus the squared $(n-1)$-dimensional volume spanned by the resistance vectors $(0i)$ is
$$
\boxed{
V_{\parallel,R}^2=\frac1{\tau(G)}.
}
\tag{18}
$$
For the resistance simplex formed by all $n$ vertices,
$$
\boxed{
V_R^2=
\frac1{((n-1)!)^2\tau(G)}.
}
\tag{19}
$$

This gives a characteristic duality:

- on the Laplacian side, the spanning-tree count equals a squared volume;
- on the resistance side, the corresponding squared volume is inversely proportional to the spanning-tree count.

> [!example] $K_3$ again
> For the unit triangle graph,
> $$
> \tau(K_3)=3.
> $$
> Earlier we obtained
> $$
> \det G((12),(13))=\frac13.
> $$
> This is exactly
> $$
> \det G=\frac1{\tau(K_3)}.
> $$
> The area of the resistance triangle satisfies
> $$
> S_\triangle^2
> =
> \frac1{(2!)^2\tau(K_3)}
> =
> \frac1{12}.
> $$

## Do areas have an electrical meaning?

Effective resistance has a direct two-terminal interpretation: current is passed through two vertices and the resulting potential difference is measured.

For second- and higher-order Gram determinants, there is no equally simple two-terminal interpretation. Nevertheless, they arise naturally in electrical network theory.

Let $e$ and $f$ be two oriented edges of the original graph. Denote their graph vectors by $t_e$ and $t_f$, and set
$$
g(e,f)=t_e\cdot t_f.
$$
Then
$$
g(e,e)=R_e
$$
is the effective resistance between the endpoints of edge $e$, while
$$
\det
\begin{pmatrix}
R_e & g(e,f)\\
g(e,f) & R_f
\end{pmatrix}
=
R_eR_f-g(e,f)^2
\tag{20}
$$
is the Gram determinant of the two edge vectors.

Now choose a random spanning tree, with the probability of a tree proportional to the product of the conductances of its edges.

For one edge,
$$
\Pr(e\in T)=c_eR_e.
\tag{21}
$$
For two edges, the transfer-current theorem gives
$$
\boxed{
\Pr(e,f\in T)
=
c_ec_f
\left(
R_eR_f-g(e,f)^2
\right).
}
\tag{22}
$$

The right-hand side is the same Gram determinant, multiplied by the conductances of the two edges.

Thus a second-order quantity acquires a concrete network and combinatorial meaning: it determines the probability of the **joint** occurrence of two edges in a random spanning tree.

For $k$ chosen edges, one obtains a $k\times k$ determinant of the corresponding transfer-current matrix.

> [!remark] Not a "second-order resistance"
> Such quantities may be viewed as a natural extension of effective resistance to several directions considered simultaneously. However, calling them "second-order effective resistances" without an explicit definition would be misleading.
>
> Effective resistance is a standard two-point characteristic of a network. Higher-order Gram determinants have a different meaning - they describe joint multivector characteristics.

For the unit triangle graph $K_3$, two specified edges belong simultaneously to exactly one of the three spanning trees. Therefore
$$
\Pr(e,f\in T)=\frac13.
$$
But above we already found
$$
\det G(e,f)=\frac13.
$$

The same quantity therefore appears simultaneously as:

- the squared area of a parallelogram in resistance geometry;
- the reciprocal of the spanning-tree count;
- the probability that two edges occur jointly in a random spanning tree.

## Toward higher-grade objects

So far we have used only vectors and matrices of their inner products. That is sufficient to define areas and volumes.

However, the expression
$$
\det G(u_1,\ldots,u_k)
$$
suggests treating a system of several vectors as a single new geometric object.

In the language of exterior algebra, such an object is written
$$
u_1\wedge\cdots\wedge u_k.
$$
Its squared norm is
$$
\boxed{
\left\|
u_1\wedge\cdots\wedge u_k
\right\|^2
=
\det G(u_1,\ldots,u_k).
}
\tag{23}
$$

Exterior products were not needed in this note: all results were obtained from ordinary lengths and inner products.

Later, this notation will allow us to treat areas, volumes, and higher-grade objects in a uniform way. This is why Gram determinants arise naturally in PMG.

## Summary

Passing from lengths to areas and volumes does not require introducing a new independent metric.

The basic data remain the inner products of vectors:
$$
u_i\cdot u_j.
$$
From them we build the Gram matrix, and its determinant gives the square of the corresponding multidimensional volume:
$$
\boxed{
V_k^2=\det G(u_1,\ldots,u_k).
}
$$

For a graph, these same inner products are expressed through effective resistances. Therefore the resistance metric determines not only distances between vertices, but also areas, volumes, and all higher Gram characteristics.

At the same time, determinants unexpectedly return us to combinatorics: the same mechanism connects geometric volumes with the spanning-tree count and with joint edge probabilities in random spanning trees.

Thus we obtain the first construction in which lengths, electrical networks, volumes, and spanning trees appear as manifestations of the same determinantal mechanism.

## Classical results used in this note

- the Gram determinant and its interpretation as squared multidimensional volume;
- Heron's formula;
- the Cayley-Menger determinant;
- Kirchhoff's matrix-tree theorem;
- the transfer-current theorem for random spanning trees.
