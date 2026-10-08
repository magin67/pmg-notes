---
title: "Laplacian, Green Matrix, and Effective Resistance Matrix: Mutual Transformations"
date: 2026-10-04
updated: 2026-10-08
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: laplacian-green-resistance-matrices
lang: en
description: "Forward and inverse transformations between the Laplacian, Green matrix, and effective resistance matrix. Centering and reconstruction of a network from effective resistances."
---

The Laplacian $L$, Green matrix $G$, and effective resistance matrix $R$ are mutually reconstructible representations of the same network. The Laplacian specifies the conductances, the Green matrix specifies the inner products of centered position vectors, and the resistance matrix contains the squared pairwise distances.

We consider a finite connected undirected graph without loops on $n\ge2$ vertices, with positive conductances on its edges. Its geometric representation was constructed in [[Effective Resistance and Graph Geometry]]. This note derives the inverse transformations and collects all the formulas in one table.

## The centering matrix

Let $\mathbf1$ denote the column vector of $n$ ones and $I$ the identity matrix. Column vectors whose coordinates sum to zero form the subspace

$$
H=\mathbf1^\perp=\left\{x\in\mathbb R^n:\sum_i x_i=0\right\}
$$

> [!info] The centering matrix
> **Definition.** The matrix
>
> $$
> J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
> $$
>
> is called the centering matrix. It subtracts the mean from each coordinate of a column vector:
>
> $$
> Jx=x-\bar x\mathbf1,\qquad \bar x=\frac1n\sum_i x_i
> $$

In the preceding notes, $J$ denoted the column vector of external currents. In this note and in the matrix transformation formulas, $J$ denotes the centering matrix; external current vectors do not occur in these formulas.

For $x\in H$, we have $Jx=x$, while $J\mathbf1=0$. Moreover,

$$
J^{\mathsf T}=J,\qquad J^2=J
$$

Thus $J$ is the orthogonal projector onto $H$ with respect to the usual inner product on $\mathbb R^n$.

If a matrix $A$ has zero row and column sums, then

$$
JA=AJ=A
$$

This follows by substituting the definition of $J$ and using $A\mathbf1=0$ and $\mathbf1^{\mathsf T}A=0$. Hence $J$ acts as the identity for such matrices.

> [!note] Centering and the complete graph
> The matrix $J$ is the Laplacian of the complete graph $K_n$ with conductance $1/n$ on every edge. Its off-diagonal entries are $-1/n$ and its diagonal entries are $(n-1)/n$.

## The Laplacian and the Green matrix

For a connected graph, the kernel of $L$ consists of constant column vectors, and the restriction of $L$ to $H$ is positive definite. The Green matrix $G=L^+$ inverts $L$ on $H$ and acts as zero on constant column vectors. This definition and its electrical meaning are discussed in [[Effective Resistance and Graph Geometry#The Green matrix|the preceding note on the Green matrix]].

Both matrices are symmetric and have zero row and column sums. Their product acts as the identity on $H$ and sends constant column vectors to zero. Therefore,

$$
LG=GL=J
\tag{1}
$$

Taking the pseudoinverse again recovers the original matrix:

$$
L=G^+
$$

Indeed, on $H$ this operation inverts $(L|_H)^{-1}$, while on constant column vectors it retains the zero action. Formula (1) expresses the fact that $L$ and $G$ are inverses on $H$.

## From the Green matrix to resistances

Let $x_i$ be the position vectors of the points in the resistance representation, with the centroid as the origin. Then

$$
x_i\cdot x_j=G_{ij},\qquad \sum_i x_i=0
$$

The effective resistance equals the squared distance:

$$
R_{ij}=\|x_j-x_i\|^2=G_{ii}+G_{jj}-2G_{ij}
\tag{2}
$$

> [!info] The resistance matrix and the distance operator
> **Definition.** The symmetric matrix $R=(R_{ij})$ of all pairwise effective resistances is called the resistance matrix. Its diagonal entries are zero.
>
> For a symmetric matrix $B$, the distance operator is defined by
>
> $$
> \mathcal D(B)_{ij}=B_{ii}+B_{jj}-2B_{ij}
> $$
>
> In this notation, formula (2) reads $R=\mathcal D(G)$.

The distance operator converts inner products into squared distances. This operation differs from matrix inversion.

## Reconstructing the Green matrix

A common translation of the points preserves their differences and pairwise distances. The Gram matrix of their position vectors depends on the choice of origin. The condition $\sum_i x_i=0$ fixes the origin at the centroid and allows the Gram matrix to be reconstructed uniquely from the distances.

> [!info] Double centering
> **Lemma.** The Green matrix can be reconstructed from the resistance matrix:
>
> $$
> G=-\frac12JRJ
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** Let $g=(G_{11},\ldots,G_{nn})^{\mathsf T}$ be the column vector of diagonal entries of $G$. Formula (2) can be written as
>
> $$
> R=g\mathbf1^{\mathsf T}+\mathbf1g^{\mathsf T}-2G
> $$
>
> Multiply both sides by $J$ on the left and on the right. The first two terms vanish because $J\mathbf1=0$ and $\mathbf1^{\mathsf T}J=0$. For the last term, $JGJ=G$, so
>
> $$
> JRJ=-2G
> $$
>
> This is equivalent to (3). $\square$

For the entrywise formula, introduce the row means and the mean over the entire matrix:

$$
\bar R_i=\frac1n\sum_j R_{ij},\qquad
\bar R=\frac1{n^2}\sum_{i,j}R_{ij}
$$

Using the symmetry of $R$, formula (3) becomes

$$
G_{ij}=\frac12(\bar R_i+\bar R_j-R_{ij}-\bar R)
\tag{4}
$$

Multiplication by $J$ on the left subtracts the column means, while multiplication on the right subtracts the row means. The overall mean is added back once.

## Transformation table and network reconstruction

| Transformation | Formula | Meaning |
|---|---|---|
| $L\to G$ | $G=L^+$ | Inversion on $H$, zero action on constant column vectors |
| $G\to L$ | $L=G^+$ | The inverse transformation on the same subspace |
| $G\to R$ | $R=\mathcal D(G)$ | From inner products to squared distances |
| $R\to G$ | $G=-\frac12JRJ$ | Reconstruction of the centered Gram matrix |

Composing the two inverse transformations gives

$$
L=\left(-\frac12JRJ\right)^+
$$

Once $L$ has been reconstructed, the conductances are determined by its off-diagonal entries:

$$
c_{ij}=-L_{ij}\qquad(i\ne j)
$$

Zero conductances correspond to absent edges. Thus the complete set of pairwise resistances determines the original weighted graph for a fixed vertex labeling.

> [!note] Conditions for the inverse transformation
> Double centering applies to any matrix of squared Euclidean distances: it yields the Gram matrix of the centered configuration. However, the pseudoinverse of that Gram matrix need not be the Laplacian of a graph with positive conductances.
>
> In particular, the off-diagonal entries of a Laplacian must be nonpositive. An arbitrary Euclidean configuration does not ensure this condition. In this note, $R$ is known to arise from a connected resistive network, so the inverse transformation recovers its original Laplacian.

## Example: a three-vertex path

Consider the path $1-2-3$ with conductances $c_{12}=1$ and $c_{23}=2$. Its resistances were computed electrically in the first two notes: $R_{12}=1$, $R_{23}=1/2$, $R_{13}=3/2$.

> [!example] The network matrices
>
> $$
> L=\begin{pmatrix}
> 1&-1&0\\
> -1&3&-2\\
> 0&-2&2
> \end{pmatrix},\qquad
> J=\frac13\begin{pmatrix}
> 2&-1&-1\\
> -1&2&-1\\
> -1&-1&2
> \end{pmatrix}
> $$
>
> $$
> G=\begin{pmatrix}
> \frac12&-\frac16&-\frac13\\
> -\frac16&\frac16&0\\
> -\frac13&0&\frac13
> \end{pmatrix},\qquad
> R=\begin{pmatrix}
> 0&1&\frac32\\
> 1&0&\frac12\\
> \frac32&\frac12&0
> \end{pmatrix}
> $$
>
> Direct multiplication verifies $LG=GL=J$ and $G\mathbf1=0$. Thus the displayed matrix $G$ is indeed $L^+$.

> [!example] Reconstruction from resistances
> For this matrix $R$, the means are
>
> $$
> \bar R_1=\frac56,\qquad \bar R_2=\frac12,\qquad
> \bar R_3=\frac23,\qquad \bar R=\frac23
> $$
>
> For example, formula (4) gives
>
> $$
> G_{11}=\frac12\left(\frac56+\frac56-\frac23\right)=\frac12
> $$
>
> $$
> G_{12}=\frac12\left(\frac56+\frac12-1-\frac23\right)=-\frac16
> $$
>
> The full double-centering calculation gives
>
> $$
> JRJ=\begin{pmatrix}
> -1&\frac13&\frac23\\
> \frac13&-\frac13&0\\
> \frac23&0&-\frac23
> \end{pmatrix}=-2G
> $$
>
> From $G$, we recover $L=G^+$ and obtain $c_{12}=1$, $c_{23}=2$, $c_{13}=0$. The inverse transformation recovers both the conductances and the absence of an edge between vertices $1$ and $3$.

## Further reading

In [[Inner Product of Graph Vectors]], the Green matrix is used to compute inner products of affine vectors. The next note, [[From Lengths to Areas and Volumes]], develops this construction: Gram determinants express squared areas and higher-dimensional volumes.

Sources on Laplacians and resistance geometry are listed in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the first section of the reading recommendations]].
