---
title: "Laplacian: graph, electrical network and quadratic form"
date: 2026-10-03
updated: 2026-10-08
revision: 2
source_revision: 6
status: draft
text_prepared_by: ChatGPT
translation_key: laplacian-graph-network-quadratic-form
lang: en
description: "The weighted graph Laplacian, current equations, the choice of reference potential, and the quadratic form of dissipated power."
---

The Laplacian of a weighted graph relates coupling coefficients to the equations of an electrical network. Its quadratic form expresses dissipated power, while solutions of the network equations determine effective resistances between vertices.

We consider finite undirected graphs without loops and their corresponding networks of linear resistors in a steady state. Basic familiarity with matrices and systems of linear equations is sufficient.

## Couplings and conductances

> [!info] Definition. Weighted graph
> A graph consists of vertices and edges joining them. The vertices are labeled $1,\ldots,n$, where $n\ge2$. The coupling coefficients satisfy
>
> $$
> c_{ij}=c_{ji}\ge0,
> \qquad c_{ii}=0
> $$
>
> An edge between distinct vertices $i,j$ exists when $c_{ij}>0$; the value $c_{ij}=0$ means that no edge is present. The matrix $C=(c_{ij})$ is called the **weighted adjacency matrix**.

In the electrical interpretation, vertices correspond to network nodes and edges to resistors.

> [!info] Definition. Conductance
> The conductance $c_{ij}$ of an existing edge is the reciprocal of its resistance $r_{ij}$:
>
> $$
> r_{ij}=\frac1{c_{ij}}
> $$

Conductance is measured in siemens and resistance in ohms. Increasing the conductance strengthens the coupling: a larger current flows through the edge under the same voltage. Path length or travel time therefore cannot directly replace conductance in this model.

Consider a path on three vertices with conductances $c_{12}=1$ and $c_{23}=2$.

```mermaid
graph LR
    a(("1")) ---|"c12 = 1"| b(("2"))
    b ---|"c23 = 2"| c(("3"))
```

> [!example] Adjacency matrix of the path
> With conductances in siemens, the edge resistances are $r_{12}=1$ ohm and $r_{23}=1/2$ ohm. The adjacency matrix is
>
> $$
> C=\begin{pmatrix}
> 0&1&0\\
> 1&0&2\\
> 0&2&0
> \end{pmatrix}
> $$
>
> There is no direct edge between vertices $1$ and $3$. The lengths of the segments in the diagram do not specify resistances.

## Potentials and currents

Let $\varphi_i$ be the electrical potential of vertex $i$. The voltage between vertices $i,j$ is $\varphi_i-\varphi_j$. By Ohm's law, the oriented current from $i$ to $j$ is

$$
I_{ij}=c_{ij}(\varphi_i-\varphi_j)
\tag{1}
$$

A positive value of $I_{ij}$ means that current flows from $i$ to $j$; a negative value means that it flows in the opposite direction. The equality $I_{ji}=-I_{ij}$ expresses a reversal of the measurement orientation. The underlying graph remains undirected.

Write $J_i$ for the external current entering vertex $i$: $J_i>0$ denotes injection into the network, and $J_i<0$ denotes withdrawal. When $J_i=0$, the net external current at that vertex is zero.

In a steady state, charge does not accumulate at a node. The total current leaving along the edges equals the external inflow:

$$
\sum_jc_{ij}(\varphi_i-\varphi_j)=J_i
\tag{2}
$$

This is Kirchhoff's current law. Summing over all vertices cancels the internal currents, giving the necessary condition for a solution:

$$
\sum_iJ_i=0
$$

> [!example] Current equations for the path
> Inject a current of $2$ amperes at vertex $1$ and withdraw the same current at vertex $3$. Then $J=(2,0,-2)^{\mathsf T}$, and equations (2) become
>
> $$
> \begin{aligned}
> \varphi_1-\varphi_2&=2\\
> (\varphi_2-\varphi_1)+2(\varphi_2-\varphi_3)&=0\\
> 2(\varphi_3-\varphi_2)&=-2
> \end{aligned}
> $$
>
> A current of $2$ amperes flows through both edges. The voltage drops are $2$ volts across the first edge and $1$ volt across the second.

## The Laplacian matrix

> [!info] Definition. Weighted degree and Laplacian
> The **weighted degree of a vertex** is the sum of the conductances of its incident edges:
>
> $$
> d_i=\sum_jc_{ij}
> $$
>
> The **graph Laplacian** is the matrix
>
> $$
> L=\operatorname{diag}(d_1,\ldots,d_n)-C
> $$
>
> Its entries are $L_{ii}=d_i$ and $L_{ij}=-c_{ij}$ for $i\ne j$. For unit edge weights, $d_i$ equals the number of neighbors of the vertex.

Expanding (2) gives $d_i\varphi_i-\sum_{j\ne i}c_{ij}\varphi_j=J_i$. The network equations therefore take the matrix form

$$
L\varphi=J
\tag{3}
$$

The columns $\varphi$ and $J$ contain the potentials and external currents. The matrix $L$ specifies the network, while $J$ specifies the applied currents. Conductances alone, without external currents or boundary conditions, do not determine a particular potential distribution.

> [!example] Laplacian of the path
> For conductances $c_{12}=1$, $c_{23}=2$, the weighted degrees are $d_1=1$, $d_2=3$, $d_3=2$. Hence
>
> $$
> L=\begin{pmatrix}
> 1&-1&0\\
> -1&3&-2\\
> 0&-2&2
> \end{pmatrix}
> $$

The Laplacian is symmetric and its rows sum to zero:

$$
L^{\mathsf T}=L,
\qquad L\mathbf1=0
$$

The superscript $\mathsf T$ denotes transposition, and $\mathbf1$ is the column vector of ones. Since $\mathbf1\ne0$, the ordinary inverse $L^{-1}$ does not exist.

## Quadratic form and network power

> [!info] Definition. Quadratic form of the Laplacian
> The Laplacian defines the scalar-valued quadratic form
>
> $$
> \mathcal Q(\varphi)=\varphi^{\mathsf T}L\varphi
> $$
>
> This is a homogeneous polynomial of degree two in the potentials, consisting of their squares and pairwise products.

Symmetry of the conductances gives

$$
\begin{aligned}
\varphi^{\mathsf T}L\varphi
&=\sum_i d_i\varphi_i^2-\sum_{i,j}c_{ij}\varphi_i\varphi_j\\
&=\sum_{i<j}c_{ij}(\varphi_i^2+\varphi_j^2-2\varphi_i\varphi_j)
\end{aligned}
$$

Thus,

$$
\mathcal Q(\varphi)=\sum_{i<j}c_{ij}(\varphi_i-\varphi_j)^2
\tag{4}
$$

Each undirected edge is counted once. Summing over all ordered pairs would require a factor of $1/2$.

Every term in (4) is nonnegative, so $L$ is **positive semidefinite**: $\varphi^{\mathsf T}L\varphi\ge0$ for every $\varphi$. Equality holds if and only if the potentials agree at the endpoints of every edge.

The power dissipated in an edge is the product of its voltage and current. By (1),

$$
P_{ij}=(\varphi_i-\varphi_j)I_{ij}
=c_{ij}(\varphi_i-\varphi_j)^2
$$

Consequently, $\mathcal Q(\varphi)$ is the total power dissipated in the network. With potentials in volts and conductances in siemens, it is measured in watts.

If the potentials satisfy equation (3), then

$$
\mathcal Q(\varphi)=\varphi^{\mathsf T}J=\sum_i\varphi_iJ_i
\tag{5}
$$

The right-hand side is the power supplied by external sources. Its equality to the sum of the edge powers expresses the power balance of the network.

## Choosing a reference potential

Adding the same constant $\alpha$ to every potential preserves voltages and currents:

$$
L(\varphi+\alpha\mathbf1)=L\varphi
$$

A graph is **connected** if any two vertices are joined by a path. In a connected graph, agreement of the potentials at the endpoints of every edge implies that the potential is the same at all vertices.

> [!info] Solvability of the network equations
> **Theorem.** For a connected graph, the equation $L\varphi=J$ has a solution if and only if $\sum_iJ_i=0$. Any two solutions differ by a constant column $\alpha\mathbf1$.

> [!note]- Proof
> **Proof.** If $Lx=0$, then $x^{\mathsf T}Lx=0$. By (4), the coordinates of $x$ agree at the endpoints of every edge. Connectedness implies that all coordinates are equal. Hence
>
> $$
> \ker L=\operatorname{span}\{\mathbf1\}
> $$
>
> The image of a symmetric matrix is the orthogonal complement of its kernel with respect to the ordinary coordinate inner product. Therefore,
>
> $$
> \operatorname{im}L=\{J:\mathbf1^{\mathsf T}J=0\}
> $$
>
> This establishes the solvability condition. The difference of any two solutions belongs to the kernel of $L$, so it equals $\alpha\mathbf1$. $\square$

To select the potentials uniquely, it is sufficient to fix the potential of one vertex, for example $\varphi_n=0$, or to require zero mean:

$$
\sum_i\varphi_i=0
$$

Both conditions choose a reference potential without changing the network or the external currents. The power in (5) is also preserved by a common potential shift, since $\sum_iJ_i=0$.

> [!example] Potentials and power of the path
> With $\varphi_3=0$, the first two network equations are
>
> $$
> \begin{pmatrix}1&-1\\-1&3\end{pmatrix}
> \begin{pmatrix}\varphi_1\\\varphi_2\end{pmatrix}
> =\begin{pmatrix}2\\0\end{pmatrix}
> $$
>
> Their solution gives $\varphi=(3,1,0)^{\mathsf T}$. The third equation also holds: $2(0-1)=-2$.
>
> Subtracting the mean potential $4/3$ gives the centered solution
>
> $$
> \widetilde\varphi=
> \begin{pmatrix}5/3\\-1/3\\-4/3\end{pmatrix}
> $$
>
> The potential differences across the edges are $2$ volts and $1$ volt in both cases. The sum of the edge powers is
>
> $$
> \mathcal Q(\varphi)=1\cdot(3-1)^2+2\cdot(1-0)^2=6
> $$
>
> The first edge dissipates $4$ watts and the second $2$ watts. An independent calculation using the external currents gives the same value:
>
> $$
> \varphi^{\mathsf T}J=3\cdot2+1\cdot0+0\cdot(-2)=6
> $$

> [!note] Disconnected graph
> Each connected component admits its own independent additive constant for the potentials. A solution exists if and only if the external currents sum to zero within each component separately. Injecting current into one component and withdrawing it from another is impossible without an additional connection between them.

## Effective resistance

Let the graph be connected. Inject a current $I>0$ at vertex $i$ and withdraw the same current at a distinct vertex $j$. The external currents at all other vertices are zero.

> [!info] Definition. Effective resistance
> The effective resistance between vertices $i,j$ is the ratio of the resulting potential difference to the test current:
>
> $$
> R_{ij}=\frac{\varphi_i-\varphi_j}{I}
> \tag{6}
> $$

Linearity of equation (3) means that changing the magnitude of the test current scales all potential differences by the same factor. The ratio (6) therefore depends only on the network and the chosen pair of vertices. It is independent of the reference potential.

Effective resistance is defined even when there is no direct edge. If an edge exists, its own resistance $r_{ij}=1/c_{ij}$ may differ from $R_{ij}$ because current can also flow along other paths.

The power balance (5) gives

$$
\mathcal Q(\varphi)=I\varphi_i-I\varphi_j
=I(\varphi_i-\varphi_j)=I^2R_{ij}
$$

For a nonzero test current, the potentials cannot be constant. Hence, in a connected graph, $\mathcal Q(\varphi)>0$ and $R_{ij}>0$. Reversing the test current changes the sign of the potential difference and preserves the resistance: $R_{ji}=R_{ij}$. For coincident vertices, set $R_{ii}=0$.

> [!example] Resistance between the endpoints of the path
> A current of $2$ amperes produces a potential difference of $3$ volts between vertices $1$ and $3$. Therefore,
>
> $$
> R_{13}=\frac32\text{ ohms}
> $$
>
> This agrees with the sum of the resistances of the two edges in series: $1+1/2=3/2$ ohms. The power computed from the effective resistance is
>
> $$
> I^2R_{13}=2^2\cdot\frac32=6\text{ W}
> $$

## Correspondence between representations

| Representation | Content |
|---|---|
| Weighted graph | The edges present and their conductances |
| Laplacian $L$ | The linear relation between potentials and external currents |
| Quadratic form $\mathcal Q$ | The dependence of total power on the potentials |

With fixed vertex labels, these representations determine one another. Conductances are recovered from the off-diagonal Laplacian entries as $c_{ij}=-L_{ij}$. In the expanded quadratic form, the coefficient of $\varphi_i\varphi_j$ for $i<j$ is $-2c_{ij}$. Reconstruction requires the entire quadratic function, rather than its value at a single potential distribution.

Formula (4) also applies to arbitrary numerical values on the vertices: it sums their squared differences with coupling coefficients as weights. The electrical network gives these values the meaning of potentials and the quadratic form the meaning of power.

## Further reading

In [[Effective Resistance and Graph Geometry]], effective resistances are represented as squared Euclidean distances between points corresponding to the vertices.

Sources are listed in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the reading recommendations for the introductory series]]: Diestel for graph terminology; Doyle and Snell for electrical networks; Spielman for the Laplacian and its quadratic form.
