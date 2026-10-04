---
title: Inner Product of Graph Vectors
date: 2026-10-03
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: inner-product-vectors
lang: en
description: Why effective resistance is a squared Euclidean distance and how the Green matrix defines a geometric representation of graph vertices.
---
For a connected undirected graph with positive edge conductances, effective resistance can be interpreted as the squared Euclidean distance between the corresponding vertices. This makes it possible to consider not only the lengths of individual vectors between vertices, but also their inner products.

For two vertices $i$ and $j$, define the oriented geometric vector
$$a_{ij}=a_j-a_i$$
and its coordinate representative
$$\mathbf e_{ij}=\mathbf e_j-\mathbf e_i$$
If $L$ is the graph Laplacian and $G = L^+$ is its Green matrix, then the effective resistance is
$$R_{ij}=\|a_{ij}\|^2=\mathbf e_{ij}^{\mathsf T} \ G \ \mathbf e_{ij}$$
The geometric interpretation of this formula is discussed in more detail in [[Effective Resistance and Graph Geometry]]. Here we focus on the mixed quantity associated with two pairs of vertices.

## Inner product through the Green matrix

For two oriented vectors
$$
a_{ij}=a_j-a_i,\qquad a_{kl}=a_l-a_k
$$
their inner product is determined by the same Gram matrix:
$$
\langle a_{ij},a_{kl}\rangle
=
\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}
\tag{1}
$$
Expanding the coordinate vectors gives
$$
\langle a_{ij},a_{kl}\rangle
=
G_{jl}-G_{jk}-G_{il}+G_{ik}
$$
Only differences of Green-matrix entries occur in this expression, so it does not depend on the choice of the zero level of electric potential.

## Formula through effective resistances

For any two vertices,
$$
R_{pq}=G_{pp}+G_{qq}-2G_{pq}
$$
Consider the combination
$$
R_{il}+R_{jk}-R_{ik}-R_{jl}
$$
After substitution, all diagonal terms cancel:
$$
R_{il}+R_{jk}-R_{ik}-R_{jl}
=
2(G_{ik}+G_{jl}-G_{il}-G_{jk})
$$
Comparing this expression with (1), we obtain the main formula:
$$
\boxed{
\langle a_{ij},a_{kl}\rangle
=
\frac12
\left(
R_{il}+R_{jk}-R_{ik}-R_{jl}
\right)
}
\tag{2}
$$
Thus, the inner product of any two vectors between graph vertices can be reconstructed solely from pairwise effective resistances.

> [!note] Orientation check
> Formula (2) is written for the convention $a_{ij}=a_j-a_i$. Reversing one of the vectors changes the sign of the inner product:
> $$\langle a_{ji},a_{kl}\rangle=-\langle a_{ij},a_{kl}\rangle$$
> Reversing both vectors preserves the sign.

## Why the norms of individual points do not appear

Formula (2) depends only on distances between points, but this can also be seen directly. In an arbitrary Euclidean coordinate system,
$$
R_{pq}
=
\|a_q-a_p\|^2
=
\|a_p\|^2+\|a_q\|^2-2\langle a_p,a_q\rangle
$$
Substitute these expressions into the combination from (2):
$$
R_{il}+R_{jk}-R_{ik}-R_{jl}
$$
Each of the four point norms
$$
\|a_i\|^2,\qquad
\|a_j\|^2,\qquad
\|a_k\|^2,\qquad
\|a_l\|^2
$$
appears once with a plus sign and once with a minus sign, so all of them cancel.

What remains depends only on the relative positions of the points. In particular, the inner product of the two vectors does not depend on the choice of origin and is determined entirely by the metric configuration of the four vertices.

## Polarization of squared distance

Formula (2) can also be obtained directly from Euclidean geometry. For any four points,
$$
2\langle a_j-a_i,a_l-a_k\rangle
=
\|a_i-a_l\|^2+\|a_j-a_k\|^2
-\|a_i-a_k\|^2-\|a_j-a_l\|^2
$$
In the resistance embedding of a graph, squared distances are equal to effective resistances, so this identity immediately becomes (2).

This is the standard polarization of a quadratic metric. No PMG-specific construction is required.

## Electrical interpretation

Suppose a unit current is injected at vertex $l$ and extracted at vertex $k$. The external current vector is then
$$
b=\mathbf e_l-\mathbf e_k=\mathbf e_{kl}
$$
With zero mean potential, the solution of Kirchhoff's equation
$$L \ \varphi = b$$
is
$$\varphi = G \ \mathbf e_{kl}$$
The potential difference between vertices $j$ and $i$ is
$$\varphi_j-\varphi_i = \mathbf e_{ij}^{\mathsf T}\varphi = \mathbf e_{ij}^{\mathsf T} \ G \ \mathbf e_{kl}$$
By formula (1),
$$
\boxed{
\varphi_j-\varphi_i
=
\langle a_{ij},a_{kl}\rangle
}
\tag{3}
$$
Therefore, the inner product of two graph vectors can be measured electrically: one oriented pair specifies the external current, while the potential difference is measured across the other pair.

> [!warning] Current direction and sign
> In (3), current is injected at $l$ and extracted at $k$, so the external current vector is $\mathbf e_{kl}=\mathbf e_l-\mathbf e_k$.
>
> If one instead says that "current flows from $k$ to $l$", the external current vector is $\mathbf e_k-\mathbf e_l=-\mathbf e_{kl}$, and the value of $\varphi_j-\varphi_i$ changes sign.

## Three pairings of four points

For four distinct vertices $i,j,k,l$, there are three inner products formed by vectors joining disjoint pairs of points:
$$
\langle a_{ij},a_{kl}\rangle,\qquad
\langle a_{jk},a_{il}\rangle,\qquad
\langle a_{ik},a_{lj}\rangle
$$
They satisfy the identity
$$
\boxed{
\langle a_{ij},a_{kl}\rangle
+
\langle a_{jk},a_{il}\rangle
+
\langle a_{ik},a_{lj}\rangle
=
0
}
\tag{4}
$$
This can be checked directly from formula (2):
$$
2\langle a_{ij},a_{kl}\rangle
=
R_{il}+R_{jk}-R_{ik}-R_{jl}
$$
$$
2\langle a_{jk},a_{il}\rangle
=
R_{jl}+R_{ik}-R_{ij}-R_{kl}
$$
$$
2\langle a_{ik},a_{lj}\rangle
=
R_{ij}+R_{kl}-R_{il}-R_{jk}
$$
When the three expressions are added, all resistance terms cancel pairwise.

Therefore, only two of these three mixed quantities are independent. The third is uniquely determined by their sum.

In electrical terms, the same identity gives a linear dependence among three reciprocal four-terminal measurements when the current and measurement orientations are chosen according to (4). This relation is useful, in particular, in four-electrode measurements.

## Special case: effective resistance

If the two vertex pairs coincide, then (2) gives
$$
\langle a_{ij},a_{ij}\rangle
=
\frac12(R_{ij}+R_{ji}-R_{ii}-R_{jj})
=
R_{ij}
$$
because $R_{ij}=R_{ji}$ and $R_{ii}=0$.

Thus effective resistance is the diagonal case of the more general bilinear quantity:
$$R_{ij} = \langle a_{ij},a_{ij}\rangle = \|a_{ij}\|^2$$
## Reciprocity

The Green matrix is symmetric, hence $\quad \langle a_{ij},a_{kl}\rangle = \langle a_{kl},a_{ij}\rangle$
In electrical terms, this means reciprocity of measurement: the voltage across the pair $(i,j)$ produced by the unit external current $\mathbf e_{kl}$ is equal to the voltage across $(k,l)$ produced by the unit external current $\mathbf e_{ij}$.

This is a special case of the reciprocity principle for linear resistive networks.

## Example: a triangle

Consider the triangle $K_3$ in which all three edges have unit resistance. For every pair of distinct vertices,
$$
R_{12}=R_{23}=R_{13}=\frac23
$$
Then
$$
\langle a_{12},a_{13}\rangle
=
\frac12(R_{13}+R_{21}-R_{11}-R_{23})
=
\frac13
$$
while for the consecutively oriented vectors $a_{12}$ and $a_{23}$,
$$
\langle a_{12},a_{23}\rangle
=
\frac12(R_{13}+R_{22}-R_{12}-R_{23})
=
-\frac13
$$
The sign depends on the relative orientation of the vectors. At the same time,
$$
\|a_{12}\|^2=\|a_{23}\|^2=\|a_{13}\|^2=\frac23
$$
so the three vertices form an equilateral triangle in the resistance embedding.

## From lengths to geometry

Effective resistance gives the length of a single vector:
$$
R_{ij}=\|a_{ij}\|^2
$$
The inner product describes the relative position of two vectors:
$$
\langle a_{ij},a_{kl}\rangle
$$
It can be positive, zero, or negative. Geometrically, this distinguishes acute, right, and obtuse angles between oriented vectors. Electrically, the sign records the direction of the measured potential difference relative to the chosen orientation of the pair.

Vector geometry is only the first level of the construction. For several vectors, one can consider determinants of their Gram matrices. For two vectors, such a determinant gives the squared area of the corresponding parallelogram, while for larger sets it gives squared higher-dimensional volumes. These quantities will be considered separately when passing from vectors to higher-order geometric objects.

## Related notes

- [[Effective Resistance and Graph Geometry]] - the Euclidean representation of a graph and the formula $R_{ij}=\|a_{ij}\|^2$
- [[Laplacian, Green Matrix, and Effective Resistance Matrix]] - direct and inverse transformations between $L$, $G=L^+$, and $R$
