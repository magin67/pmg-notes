---
title: "Effective Resistance and Graph Geometry"
description: "Why effective resistance is a squared Euclidean distance and how the Green matrix defines a geometric representation of graph vertices."
lang: en
translation_key: effective-resistance-graph-geometry
text_prepared_by: "ChatGPT"
status: draft
revision: 1
date: 2026-10-03
---
In the previous note, [[Laplacian - graph, electrical network, and quadratic form|Laplacian: graph, electrical network, and quadratic form]], the effective resistance $R_{ij}$ was defined through an electrical network: a unit current is injected at one vertex and extracted at another, and the resulting potential difference is the effective resistance between them.

This quantity also has a geometric interpretation. The vertices of a connected undirected graph with positive conductances can be represented by points in a Euclidean space so that
$$
\boxed{R_{ij}=\|a_{ij}\|^2}
\tag{1}
$$
where $\quad a_{ij}=a_j-a_i \quad$ is the vector between the points corresponding to vertices $i$ and $j$.

This relation between effective resistance and the squared Euclidean norm is the main subject of this note.

## Why the Laplacian has to be inverted

Let $L$ be the Laplacian of a connected graph on $n$ vertices. For a potential vector $\varphi$ and an external-current vector $J$,

$$
L\varphi=J
$$

The rows of the Laplacian sum to zero, so

$$
L\mathbf 1=0
$$

Therefore the ordinary inverse $L^{-1}$ does not exist. Electrically, this reflects the fact that adding the same constant to all potentials does not change potential differences or currents.

Only the centered part of the space is essential:

$$
H = \mathbf 1^\perp = \left\{u\in\mathbb R^n: \sum_i u_i=0\right\}
$$

For a connected graph, the restriction of the Laplacian to $H$ is positive definite and invertible.

This inverse map, written in the full space, is represented by the Moore-Penrose pseudoinverse

$$
\boxed{G=L^+} \tag{2}
$$

We will call $G$ the **Green matrix of the Laplacian**.

> [!note] Remark
> The Green matrix is not an ordinary inverse of the Laplacian. It inverts $L$ on the subspace $H$, which contains balanced current vectors and coordinate representatives of vertex differences.

## Points, vectors, and coordinate columns

It is important to distinguish geometric objects from their coordinate representations.

Let $\quad a_1,\ldots,a_n \quad$ be the points of a Euclidean space corresponding to the graph vertices.

For each pair of vertices, define the vector $\quad a_{ij}=a_j-a_i \quad$

Now choose the centroid of these points as the origin and denote by $x_i$ the position vector of the point $a_i$ relative to this origin. Then
$$
\sum_i x_i=0
$$
and $\quad a_{ij}=x_j-x_i \quad$

Separately, consider the standard coordinate columns
$$
\mathbf e_i=(0,\ldots,0,1,0,\ldots,0)^{\mathsf T}
$$
in $\mathbb R^n$, and define
$$
\boxed{\mathbf e_{ij}=\mathbf e_j-\mathbf e_i} \tag{3}
$$
The column $\mathbf e_{ij}$ is not a new geometric point or vector in the resistance representation. It is the coordinate representative of the vertex difference with respect to the formal vertex basis.

Thus two different levels are used below:
- $a_i$, $x_i$, $a_{ij}$ are geometric objects;
- $\mathbf e_i$, $\mathbf e_{ij}$ are coordinate columns used in matrix formulas.

## Effective resistance through the Green matrix

Suppose a unit current is injected at vertex $j$ and extracted at vertex $i$. Its coordinate column is $\mathbf e_{ij}$. It belongs to $H$ because the sum of its coordinates is zero.

The centered solution of the network equation is
$$
\varphi=G\mathbf e_{ij}
$$
The potential difference between vertices $j$ and $i$ is
$$
R_{ij} = \mathbf e_{ij}^{\mathsf T} G \mathbf e_{ij} \tag{4}
$$
Expanding this expression gives
$$
R_{ij} = G_{ii}+G_{jj}-2G_{ij}
$$
This already has the standard form of a squared distance computed from a Gram matrix.

## The Green matrix as a Gram matrix

The Laplacian of a connected graph with positive conductances is positive semidefinite. Therefore $\quad G = L^+ \quad$ is also positive semidefinite.

Hence there exist Euclidean vectors $\quad x_1,\ldots,x_n \quad$ whose Gram matrix is
$$
\boxed{G_{ij}=\langle x_i,x_j\rangle} \tag{5}
$$
The condition
$$
G\mathbf 1=0
$$
corresponds to the chosen centering
$$
\sum_i x_i=0
$$
For the vector between two points, $\quad a_{ij}=x_j-x_i$
Therefore
$$
\begin{aligned}
\|a_{ij}\|^2
&=
\|x_j-x_i\|^2\\
&=
\langle x_i,x_i\rangle
+\langle x_j,x_j\rangle
-2\langle x_i,x_j\rangle\\
&=
G_{ii}+G_{jj}-2G_{ij}
\end{aligned}
$$
Comparing this expression with the effective-resistance formula gives
$$
\boxed{R_{ij} = \|a_{ij}\|^2 = \mathbf e_{ij}^{\mathsf T} G \mathbf e_{ij}} \tag{6}
$$
> [!info] Geometric interpretation
> The vertices of a connected graph can be represented by points in a Euclidean space so that the effective resistance between two vertices equals the squared norm of the vector between the corresponding points.

## Dimension of the geometric representation

For a connected graph,
$$
\operatorname{rank}L=n-1
$$
Pseudoinversion preserves rank, so
$$
\operatorname{rank}G=n-1
$$
Therefore the centered position vectors $x_1,\ldots,x_n$ span a space of dimension $n-1$.

A graph on $n$ vertices thus defines $n$ points forming a Euclidean simplex of affine dimension $n-1$.

It is important that this is not the usual drawing of a graph. Geometric distances here are determined not by the lengths of drawn edges but by the effective resistances of the entire network.

Two vertices need not be joined by an edge at all, yet the geometric norm of the corresponding vector $a_{ij}$ is still defined.

## Example: a three-vertex path

Return to the example from the previous note. Let the graph be $\quad 1-2-3$ with edge conductances
$$
c_{12}=1, \quad c_{23}=2
$$
The corresponding edge resistances are
$$
r_{12}=1, \quad r_{23}=\frac12
$$
For a tree, the effective resistance between two vertices is the sum of the edge resistances along the unique path between them. Hence
$$
R_{12}=1, \quad R_{23}=\frac12, \quad R_{13}=\frac32
$$
The Laplacian is
$$
L = \begin{pmatrix}
1&-1&0\\
-1&3&-2\\
0&-2&2
\end{pmatrix}
$$
and its Green matrix is
$$
G=L^+ =
\begin{pmatrix}
\frac12&-\frac16&-\frac13\\
-\frac16&\frac16&0\\
-\frac13&0&\frac13
\end{pmatrix}
$$
For example, $\quad R_{12} = G_{11}+G_{22}-2G_{12} = 1$

and $\quad R_{13} = G_{11}+G_{33}-2G_{13} = \frac32$

Now temporarily forget the original path drawing and require only
$$
\|a_{12}\|^2=1, \qquad \|a_{23}\|^2=\frac12, \qquad \|a_{13}\|^2=\frac32
$$
Since
$$
\|a_{13}\|^2 = \|a_{12}\|^2+\|a_{23}\|^2
$$
the three points form a right triangle with the right angle at $a_2$.

For example, after an arbitrary translation of the entire configuration, we may choose
$$
a_2=(0,0), \qquad a_1=(1,0), \qquad a_3=\left(0,\frac1{\sqrt2}\right)
$$
> [!example] The graph and its geometry
> The original graph $1-2-3$ is usually drawn as a straight path.
>
> In the resistance Euclidean representation, the same three vertices form a right triangle.
>
> Therefore a topological drawing of a graph and its metric representation are different objects.

## Why effective resistance is called a distance

Effective resistance $R_{ij}$ is often called **resistance distance**. This is justified: on the vertex set it satisfies the axioms of a metric.

However, the geometric representation is built through the quadratic quantity
$$
R_{ij}=\|a_{ij}\|^2
$$
For the further development, this is the primary form of the relation. It is consistent with the general logic of PMG, where metric characteristics are expressed mainly through quadratic forms and their polarizations.

## The distance operator

The formula
$$
R_{ij}=G_{ii}+G_{jj}-2G_{ij}
$$
can be viewed as an application of a distance operator.

For a symmetric matrix $B$, define
$$
\mathcal D(B)_{ij} = B_{ii}+B_{jj}-2B_{ij}
$$
If $B$ is a Gram matrix of points, then $\mathcal D(B)$ is the matrix of squared distances between them.

Therefore
$$
\boxed{R = \mathcal D(G)=\mathcal D(L^+)} \tag{7}
$$
For the purposes of this note, the chain
$$
L \longrightarrow G=L^+ \longrightarrow R=\mathcal D(G)
$$
is sufficient.

The exact forward and inverse transitions between the Laplacian, the Green matrix, and the resistance matrix will be collected separately in [[Laplacian, Green matrix, and resistance matrix]].

## What happens when connections are strengthened

The geometric interpretation gives another way to view changes in the graph.

If an edge with positive conductance is added, or the conductance of an existing edge is increased, effective resistances between vertices do not increase. Consequently, $\|a_{ij}\|^2$ does not increase either.

Conversely, weakening connections may increase effective resistances.

Thus strengthening the connectivity of the network can be interpreted as a metric contraction of its vertices. The entire point configuration changes, not only the quantity associated with the endpoints of the modified edge.

## Summary

The Laplacian of a connected weighted graph defines not only an electrical network but also a Euclidean geometric representation of its vertices.

The Green matrix $\quad G=L^+ \quad$ is the Gram matrix of the centered position vectors $x_i$, while effective resistances are given by
$$
\boxed{R_{ij} = \|a_{ij}\|^2 = \mathbf e_{ij}^{\mathsf T} L^+ \mathbf e_{ij}} \tag{8}
$$
Thus the connection structure of the graph determines the mutual arrangement of points in a Euclidean space.

The next step is to pass from the squared norm of one vector $a_{ij}$ to the inner product of two vectors $a_{ij}$ and $a_{kl}$. This will give a geometric interpretation of measuring a potential difference across one pair of vertices while passing current through another.

## About this note

An introductory presentation of the standard Euclidean interpretation of effective resistance and the Laplacian Green matrix. No special constructions of polyform algebra are used here.

The draft text was prepared by ChatGPT based on materials by the project author. The plan and editorial decisions were discussed jointly. The mathematical results presented here are standard. Revision 1, October 3, 2026.
