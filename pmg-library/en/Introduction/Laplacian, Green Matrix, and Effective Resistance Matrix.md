---
title: "Laplacian, Green Matrix, and Effective Resistance Matrix"
description: "How the Laplacian, Green matrix, and effective resistance matrix can be reconstructed from one another, and why centering connects these three representations."
lang: en
translation_key: laplacian-green-resistance-matrices
status: draft
revision: 1
date: 2026-10-04
---
For a connected undirected graph with positive conductances, the same structure can be described by three matrices: the Laplacian $L$, the Green matrix $G$, and the effective resistance matrix $R$.

These representations are related by
$$
L \longleftrightarrow G \longleftrightarrow R
$$
but the two transitions are different in nature. The relation $L \leftrightarrow G$ is an operator inversion with the common zero direction taken into account, while the relation $G \leftrightarrow R$ converts inner products into squared distances and back.

The purpose of this note is to collect these transitions in one place and explain why they work.

## Three matrices of the same network

Let $L$ be the Laplacian of a connected graph on $n$ vertices.

Its rows and columns have zero sum, so
$$
L\mathbf 1=0
$$
where $\mathbf 1$ is the column vector of $n$ ones.

The Green matrix, equivalently the Laplacian Green's function in matrix form, is defined as the Moore-Penrose pseudoinverse:
$$
\boxed{G=L^+}
\tag{1}
$$
For the purposes of this note, pseudoinversion can be understood as follows: a common shift of all potentials is irrelevant, while on vectors whose coordinates sum to zero, $G$ acts as the ordinary inverse of $L$.

The effective resistance matrix
$$
R=(R_{ij})
$$
contains the effective resistances between all pairs of vertices. On the diagonal,
$$
R_{ii}=0
$$

For the coordinate column
$$
\mathbf e_{ij}=\mathbf e_j-\mathbf e_i
$$
the effective resistance is expressed through the Green matrix as
$$
R_{ij}
=
\mathbf e_{ij}^{\mathsf T}G\mathbf e_{ij}
=
G_{ii}+G_{jj}-2G_{ij}
$$

Thus $L$, $G$, and $R$ describe the same network from different viewpoints.

## Why the Laplacian has no ordinary inverse

If the same constant is added to every potential, potential differences do not change. Therefore, the electrical state of the network does not depend on the common potential level.

In matrix form, this is expressed by
$$
L\mathbf 1=0
$$
Hence the ordinary inverse $L^{-1}$ does not exist.

However, if the coordinates of a vector sum to zero,
$$
x_1+\cdots+x_n=0
$$
then the common constant level has already been removed. For a connected graph, the Laplacian is invertible on such vectors.

This inversion is exactly what the Green matrix $G=L^+$ represents.

## The centering matrix

To remove the common constant level explicitly, introduce
$$
\boxed{
J
=
I-\frac1n\mathbf 1\mathbf 1^{\mathsf T}
}
\tag{2}
$$
Let
$$
\bar x=\frac1n\sum_i x_i
$$
Then
$$
Jx=x-\bar x\,\mathbf 1
$$
Thus multiplication by $J$ simply subtracts the mean value from all coordinates.

After this operation, the coordinates sum to zero:
$$
\sum_i (Jx)_i=0
$$
If the original vector already has zero coordinate sum, then
$$
Jx=x
$$

For this reason, $J$ is called the **centering matrix**.

At the same time, $J$ is a projector. Here the projection has a direct meaning: from any vector it removes the part corresponding to the common constant level and keeps the part whose coordinates sum to zero. Repeating the centering operation changes nothing:
$$
J^2=J
$$

> [!note] $J$ as the Laplacian of a complete graph
> The matrix $J$ itself is the Laplacian of the complete graph $K_n$ if every edge is assigned conductance $1/n$.
>
> Then every off-diagonal Laplacian entry is $-1/n$, while every diagonal entry is $(n-1)/n$, which gives exactly
> $$
> J=I-\frac1n\mathbf 1\mathbf 1^{\mathsf T}
> $$

## $J$ as the identity for zero-sum matrices

Let $A$ be a matrix whose row and column sums are zero:
$$
A\mathbf 1=0,
\qquad
\mathbf 1^{\mathsf T}A=0
$$
Then
$$
JA=AJ=A
$$

Thus, within the class of such matrices, $J$ plays the same role that the ordinary identity matrix $I$ plays for arbitrary matrices.

Both the Laplacian $L$ and the Green matrix $G$ have zero row and column sums. Their product is
$$
\boxed{
LG=GL=J
}
\tag{3}
$$

This equality gives a simple interpretation of pseudoinversion. For ordinary inverse matrices, the product equals $I$. For $L$ and $G$, the common constant direction has been removed, so the role of the identity is played by $J$.

## From the Green matrix to the effective resistance matrix

The Green matrix is the Gram matrix of a centered Euclidean representation of the vertices:
$$
G_{ij}=\langle x_i,x_j\rangle,
\qquad
\sum_i x_i=0
$$
Therefore, the squared distance between vertices $i$ and $j$ is
$$
\begin{aligned}
\|x_j-x_i\|^2
&=
\langle x_i,x_i\rangle
+\langle x_j,x_j\rangle
-2\langle x_i,x_j\rangle\\
&=
G_{ii}+G_{jj}-2G_{ij}
\end{aligned}
$$

In the resistance representation, this squared distance is equal to the effective resistance:
$$
\boxed{
R_{ij}
=
G_{ii}+G_{jj}-2G_{ij}
}
\tag{4}
$$

For any symmetric matrix $B$, define the distance operator by
$$
\mathcal D(B)_{ij}
=
B_{ii}+B_{jj}-2B_{ij}
$$
Then formula (4) can be written compactly as
$$
R=\mathcal D(G)
$$

This is not a matrix inversion. The distance operator converts data about inner products into data about squared distances.

## What is lost when passing to distances

Suppose all points $x_i$ are translated by the same vector $t$:
$$
x_i\longmapsto x_i+t
$$
All pairwise differences remain unchanged:
$$
(x_j+t)-(x_i+t)=x_j-x_i
$$
Therefore, the distance matrix $R$ contains no information about the position of the coordinate origin.

The Gram matrix, by contrast, depends on the choice of origin. To reconstruct it uniquely from distances, the origin must be fixed.

The natural choice is to place the origin at the centroid of the configuration:
$$
\sum_i x_i=0
$$
This is exactly the centering performed by the matrix $J$.

## From the effective resistance matrix to the Green matrix

Start with
$$
R_{ij}=G_{ii}+G_{jj}-2G_{ij}
$$
The terms $G_{ii}$ and $G_{jj}$ form respectively repeated column and row parts. When multiplied by $J$ from the left and right, these parts disappear because
$$
J\mathbf 1=0
$$
Moreover, for the centered Green matrix,
$$
JG=GJ=G
$$
Therefore,
$$
JRJ=-2G
$$
and the inverse formula is
$$
\boxed{
G=-\frac12JRJ
}
\tag{5}
$$

Thus the matrix of all effective resistances completely determines the centered Green matrix.

The same formula can be written entrywise. Let the mean of row $i$ be
$$
\bar R_i=\frac1n\sum_j R_{ij}
$$
and let the mean over the entire matrix be
$$
\bar R=\frac1{n^2}\sum_{i,j}R_{ij}
$$
Then
$$
G_{ij}
=
\frac12
\left(
\bar R_i+\bar R_j-R_{ij}-\bar R
\right)
$$

The matrix formula $G=-\frac12JRJ$ and this entrywise formula are equivalent.

## Returning to the Laplacian

Since
$$
G=L^+
$$
the pseudoinverse can be taken once again:
$$
\boxed{
L=G^+
}
\tag{6}
$$

Hence the Laplacian can also be reconstructed from the effective resistance matrix:
$$
\boxed{
L=
\left(
-\frac12JRJ
\right)^+
}
\tag{7}
$$

In the opposite direction,
$$
\boxed{
R_{ij}
=
\mathbf e_{ij}^{\mathsf T}L^+\mathbf e_{ij}
}
\tag{8}
$$

Thus, for a connected undirected graph with positive conductances, all three representations can be reconstructed from one another.

## Complete transition scheme

The main transitions can be collected in a single scheme:
$$
\boxed{
L
\overset{+}{\longleftrightarrow}
G
\overset{\mathcal D}{\longleftrightarrow}
R
}
\tag{9}
$$

The two kinds of transition have different meanings:

| Transition | Formula | Meaning |
|---|---|---|
| $L\to G$ | $G=L^+$ | inversion of the Laplacian after removing the common constant level |
| $G\to L$ | $L=G^+$ | inverse transition |
| $G\to R$ | $R_{ij}=G_{ii}+G_{jj}-2G_{ij}$ | from inner products to squared distances |
| $R\to G$ | $G=-\frac12JRJ$ | reconstruction of the centered Gram matrix from distances |

The three matrices can also be viewed as three levels of description of the same structure:

| Matrix | What it directly describes |
|---|---|
| $L$ | conductances and the local connection structure |
| $G$ | the inverse metric structure and inner products |
| $R$ | effective resistances, that is, squared pairwise distances |

## Example: a three-vertex path

Consider the graph
$$
1-2-3
$$
with conductances
$$
c_{12}=1,
\qquad
c_{23}=2
$$

Its Laplacian is
$$
L=
\begin{pmatrix}
1&-1&0\\
-1&3&-2\\
0&-2&2
\end{pmatrix}
$$

The centering matrix for three vertices is
$$
J=
\begin{pmatrix}
\frac23&-\frac13&-\frac13\\
-\frac13&\frac23&-\frac13\\
-\frac13&-\frac13&\frac23
\end{pmatrix}
$$

The Green matrix is
$$
G=L^+
=
\begin{pmatrix}
\frac12&-\frac16&-\frac13\\
-\frac16&\frac16&0\\
-\frac13&0&\frac13
\end{pmatrix}
$$

Direct multiplication gives
$$
LG=GL=J
$$

The effective resistances are
$$
R_{12}=1,
\qquad
R_{23}=\frac12,
\qquad
R_{13}=\frac32
$$
and therefore
$$
R=
\begin{pmatrix}
0&1&\frac32\\
1&0&\frac12\\
\frac32&\frac12&0
\end{pmatrix}
$$

Now perform the reverse transition:
$$
-\frac12JRJ
=
\begin{pmatrix}
\frac12&-\frac16&-\frac13\\
-\frac16&\frac16&0\\
-\frac13&0&\frac13
\end{pmatrix}
=
G
$$
and taking the pseudoinverse once more returns the original Laplacian:
$$
G^+
=
\begin{pmatrix}
1&-1&0\\
-1&3&-2\\
0&-2&2
\end{pmatrix}
=
L
$$

In this example, the complete cycle
$$
L\longrightarrow G\longrightarrow R\longrightarrow G\longrightarrow L
$$
recovers the original matrices without loss of information.

## Conditions for the reverse transition

The formula
$$
G=-\frac12JRJ
$$
has a more general meaning: it reconstructs the Gram matrix of a Euclidean configuration, centered at its centroid, from the matrix of squared Euclidean distances.

However, not every matrix of squared Euclidean distances is the effective resistance matrix of a graph with positive conductances.

Therefore, in this note the reverse scheme
$$
R\longrightarrow G\longrightarrow L
$$
is considered for an $R$ that is already known to arise from a connected undirected graph with positive conductances. In that case, the reconstructed $L$ is the original graph Laplacian.

> [!info] Main point
> The Laplacian, Green matrix, and effective resistance matrix are not three independent sets of data.
>
> For a connected graph with positive conductances, each of them determines the other two:
> $$
> G=L^+,
> \qquad
> R=\mathcal D(G),
> \qquad
> G=-\frac12JRJ,
> \qquad
> L=G^+
> $$

## Related notes

- [[Laplacian - Graph, Electrical Network and Quadratic Form|Laplacian: Graph, Electrical Network and Quadratic Form]]
- [[Effective Resistance and Graph Geometry]]
- [[Inner Product of Graph Vectors]]

## Summary

For a connected undirected graph with positive conductances, the Laplacian $L$, the Green matrix $G$, and the effective resistance matrix $R$ are mutually reconstructible representations of the same structure.

The transition
$$
L\longleftrightarrow G
$$
is associated with inverting the Laplacian after removing the common constant potential level.

The transition
$$
G\longleftrightarrow R
$$
has a geometric meaning: it is the transition between inner products of centered position vectors and squared distances between the corresponding points.

The centering matrix
$$
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$
connects these two descriptions. It removes the common constant level, acts as a projector onto vectors whose coordinates sum to zero, and plays the role of the identity for matrices with zero row and column sums.

As a result, the entire scheme reduces to four main formulas:
$$
G=L^+,
\qquad
LG=GL=J
$$
$$
R=\mathcal D(G),
\qquad
G=-\frac12JRJ
$$
