---
title: "Laplacian: graph, electrical network and quadratic form"
date: 2026-10-03
updated: 2026-11-08
revision: 8
translated_revision: 12
source_revision: 12
status: draft
text_prepared_by: ChatGPT
translation_key: laplacian-graph-network-quadratic-form
lang: en
description: Coupling strengths, the Laplacian matrix and its action on vertex values. A scalar-valued quadratic form, the electrical interpretation, and effective resistance.
order: "1"
aliases:
  - "en/Introduction/Laplacian - graph, electrical network and quadratic form"
---

In these notes, a graph is specified by the strengths of the couplings between its vertices. The Laplacian collects these strengths into a matrix: its action on vertex values is expressed through differences across edges. This matrix is used to construct graph geometry, describe Markov chains, and calculate electrical networks.

Here we define the Laplacian matrix and examine its action. An electrical network serves as an example: coupling strengths are interpreted as conductances, and vertex values as potentials. This example explains the electrical meaning of effective resistance and of the quadratic function associated with the Laplacian matrix.

We consider finite undirected graphs without loops, with nonnegative coupling strengths. Basic familiarity with matrices and systems of linear equations is sufficient.

## Couplings and conductances

> [!info] Definition. Graph
> A graph consists of vertices and edges joining them. The vertices are labeled $1,\ldots,n$, where $n\ge2$. The coupling strengths $c_{ij}$ satisfy
>
> $$
> c_{ij}=c_{ji}\ge0,
> \qquad c_{ii}=0
> $$
>
> An edge between distinct vertices $i,j$ exists when $c_{ij}>0$; the value $c_{ij}=0$ means that no edge is present. The matrix $C=(c_{ij})$ is called the **adjacency matrix**.

The coupling strength is the weight of an edge. In the electrical interpretation, this weight is called its **conductance**. Other notes in the library also use this name for the same quantity $c_{ij}$.

Consider a path on three vertices with coupling strengths $c_{12}=1$ and $c_{23}=2$.

![A path with coupling strengths inside rectangles](<images/Path with coupling strengths.svg>)

Circles represent vertices and rectangles represent couplings. The labels inside the rectangles give the coupling strengths $c_{ij}$; in the electrical interpretation, these are conductances.

> [!example] Adjacency matrix of the path
> The adjacency matrix is
>
> $$
> C=\begin{pmatrix}
> 0&1&0\\
> 1&0&2\\
> 0&2&0
> \end{pmatrix}
> $$
>
> There is no direct edge between vertices $1$ and $3$. The lengths of the segments in the diagram specify neither coupling strengths nor distances in the graph metric.

## The Laplacian matrix

> [!info] Definition. Vertex degree and Laplacian
> In these notes, the **degree of a vertex** is the sum of its coupling strengths to neighboring vertices:
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

Throughout this note, $L$ denotes the Laplacian matrix.

> [!example] Laplacian of the path
> For coupling strengths $c_{12}=1$, $c_{23}=2$, the vertex degrees are $d_1=1$, $d_2=3$, $d_3=2$. Hence
>
> $$
> L=\begin{pmatrix}
> 1&-1&0\\
> -1&3&-2\\
> 0&-2&2
> \end{pmatrix}
> $$

Suppose numerical values $x_i$ are assigned to the graph vertices. For example, the vertices may represent observation sites, with $x_i$ giving the temperature measured at each site. Collect these values into a column:

$$
x=\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}
$$

The matrix $L$ transforms the column $x$ into a new column $Lx$. Its $i$th entry is calculated as follows:

$$
(Lx)_i=d_i x_i-\sum_jc_{ij}x_j
=\sum_jc_{ij}(x_i-x_j)
$$

In other words, for each vertex, subtract each neighboring value from its own value, multiply by the corresponding coupling strength, and add the results. The second sum follows from the definition $d_i=\sum_jc_{ij}$. If all values are equal, every difference and the result are zero.

> [!example] Applying the Laplacian to vertex values
> Suppose the temperatures measured at the three observation sites on the path are $20$, $21$, and $24$ degrees. Then
>
> $$
> Lx=\begin{pmatrix}
> 1&-1&0\\
> -1&3&-2\\
> 0&-2&2
> \end{pmatrix}
> \begin{pmatrix}20\\21\\24\end{pmatrix}
> =\begin{pmatrix}-1\\-5\\6\end{pmatrix}
> $$
>
> Consider the middle vertex. It has two neighbors, with coupling strengths $1$ and $2$:
>
> $$
> (Lx)_2=1\cdot(21-20)+2\cdot(21-24)=1-6=-5
> $$
>
> The difference from the first neighbor contributes $1$, and the difference from the second contributes $-6$. The column $Lx$ contains the sum of these contributions at each vertex.

The Laplacian is symmetric and its rows sum to zero:

$$
L^{\mathsf T}=L,
\qquad L\mathbf1=0
$$

The superscript $\mathsf T$ denotes transposition, and $\mathbf1$ is the column vector of ones. Since $\mathbf1\ne0$, the ordinary inverse $L^{-1}$ does not exist.

## Potentials and currents

As an application, consider a network of linear resistors in a steady state. In the electrical interpretation, vertices correspond to network nodes and edges to resistors.

> [!info] Definition. Conductance
> The resistance of an individual existing edge is $1/c_{ij}$, where $c_{ij}>0$ is its conductance.

Conductance is measured in siemens and resistance in ohms. Increasing the conductance strengthens the coupling: a larger current flows through the edge under the same voltage. Path length or travel time therefore cannot directly replace conductance in this model.

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

This is Kirchhoff's current law.

Expanding (2) gives $d_i\varphi_i-\sum_{j\ne i}c_{ij}\varphi_j=J_i$. The network equations therefore take the matrix form

$$
L\varphi=J
\tag{3}
$$

The columns $\varphi$ and $J$ contain the potentials and external currents. The matrix $L$ specifies the network, while $J$ specifies the applied currents. Conductances alone, without external currents or boundary conditions, do not determine a particular potential distribution.

Summing over all vertices cancels the internal currents, giving the necessary condition for a solution:

$$
\sum_iJ_i=0
$$

> [!example] Current equations for the path
> For the electrical example, take the path edge conductances to be $1$ siemens and $2$ siemens. Inject a current of $2$ amperes at vertex $1$ and withdraw the same current at vertex $3$. Then $J=(2,0,-2)^{\mathsf T}$, and equations (2) become
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

## Quadratic form and network power

> [!info] Definition. Scalar-valued quadratic form of a matrix
> For any collection of numerical vertex values $x_1,\ldots,x_n$, set
>
> $$
> \mathcal Q(x)=x^{\mathsf T}Lx
> $$
>
> Here $x$ denotes the entire collection of values. In the matrix product, $x$ is written as a column and $x^{\mathsf T}$ as the corresponding row; this is a notation convention for the collection.
>
> This is a scalar-valued quadratic form in the usual linear-algebra sense: a homogeneous polynomial of degree two in the values $x_i$.

Symmetry of the coupling strengths gives

$$
\begin{aligned}
x^{\mathsf T}Lx
&=\sum_i d_ix_i^2-\sum_{i,j}c_{ij}x_ix_j\\
&=\sum_{i<j}c_{ij}(x_i^2+x_j^2-2x_ix_j)
\end{aligned}
$$

Thus,

$$
\mathcal Q(x)=\sum_{i<j}c_{ij}(x_i-x_j)^2
\tag{4}
$$

Each undirected edge is counted once. Summing over all ordered pairs would require a factor of $1/2$.

Every term in (4) is nonnegative, so $L$ is **positive semidefinite**: $x^{\mathsf T}Lx\ge0$ for every $x$. Equality holds if and only if the values $x_i$ agree at the endpoints of every edge.

Now take the vertex values $x_i$ to be electrical potentials $\varphi_i$. The power dissipated in an edge is the product of its voltage and current. By (1),

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

### Numerical differences and vectors

For the geometric description of a graph, its vertices are represented by formal basis elements $a_1,\ldots,a_n$. Linear combinations of these elements can be formed. The elements $a_i$ and the numbers $x_i$ assigned to the vertices play different roles.

> [!info] Vertex-pair vectors and affine vectors
> **Definition.** The difference between the elements representing two vertices,
>
> $$
> a_{ij}=a_j-a_i
> $$
>
> is called a **vertex-pair vector**. It is directed from $a_i$ to $a_j$ and is defined whether or not an edge joins them.
>
> A more general vector has the form $u=\sum_i u_i a_i$, where the $u_i$ are numerical coefficients and $\sum_i u_i=0$. If three or more basis vertices have nonzero coefficients in this expression, the expression involves several vertices; with local vertices it is called **multipoint**.

For example, $a_1+a_2-2a_3$ is one vector expressed using three basis vertices: its coefficients sum to $1+1-2=0$. It decomposes into two vertex-pair vectors:

$$
a_1+a_2-2a_3=(a_1-a_3)+(a_2-a_3)
$$

By contrast, $x_j-x_i$ is a difference of **numbers** assigned to the vertices. In the temperature example, $x_2-x_1=21-20=1$, while $a_{12}=a_2-a_1$ remains a vertex-pair vector. Changing the temperatures changes the numerical difference but does not change $a_{12}$. The number of vertices involved refers to the chosen basis; the general case is discussed in the [[Basic Objects and Operations of Polyform Algebra#Points and affine vectors|definition of affine vectors]].

The Laplacian polyform is a linear combination of quadratic forms of vertex-pair vectors. Its [[Basic Objects and Operations of Polyform Algebra#The polyform representation of the Laplacian|definition and relation to the scalar-valued quadratic form]] are discussed in polyform algebra. In this note, $\mathcal Q$ denotes the function of numerical vertex values.

## Choosing a reference potential

Adding the same constant $\alpha$ to every potential preserves voltages and currents:

$$
L(\varphi+\alpha\mathbf1)=L\varphi
$$

> [!info] Paths, connectedness, and connected components
> **Definition.** A path between vertices is a sequence of vertices in which consecutive vertices are joined by an edge and no vertex is repeated. A path may consist of a single vertex.
>
> A graph is **connected** if any two of its vertices are joined by a path.
>
> A **connected component** consists of a chosen vertex, all vertices reachable from it by paths, and all edges between these vertices. A vertex with no edges joining it to other vertices is **isolated** and forms a component of its own. A graph with several components is **disconnected**.

In a connected graph, agreement of the potentials at the endpoints of every edge implies that the potential is the same at all vertices.

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
> For example, adding an isolated vertex $4$ to the path $1$-$2$-$3$ gives two components: the path and the isolated vertex.
>
> Each connected component admits its own independent additive constant for the potentials. A solution exists if and only if the external currents sum to zero within each component separately. Injecting current into one component and withdrawing it from another is impossible without an additional connection between them.

## Effective resistance

Let the graph be connected. Invert $L$ on the subspace of columns whose coordinates sum to zero, and let the resulting operator vanish on constant columns. The resulting Green matrix $\mathrm{Gr}=L^+$ allows effective resistances to be computed directly from the graph. This inversion is explained in the [[Effective Resistance and Graph Geometry#The Green matrix|definition of the Green matrix]].

> [!info] Definition. Effective resistance
> The effective resistance between vertices $i,j$ is
>
> $$
> R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
> $$

To see its electrical meaning, inject a current $I>0$ at vertex $i$ and withdraw the same current at a distinct vertex $j$. The external currents at all other vertices are zero. The solution of $L\varphi=J$ has the form

$$
\varphi_k=I(\mathrm{Gr}_{ki}-\mathrm{Gr}_{kj})+\alpha
$$

where $\alpha$ selects the reference potential. Subtracting the values at $k=i$ and $k=j$ and using symmetry of the Green matrix gives

$$
R_{ij}=\frac{\varphi_i-\varphi_j}{I}
\tag{6}
$$

Thus, Laplacian inversion and the test-current calculation give the same quantity. Solving the network equations determines potentials; effective resistance is obtained from their difference for this specific choice of external currents.

Linearity of equation (3) means that changing the magnitude of the test current scales all potential differences by the same factor. The ratio (6) therefore depends only on the network and the chosen pair of vertices. It is independent of the reference potential.

Effective resistance is defined even when there is no direct edge. If an edge exists, its own resistance $1/c_{ij}$ may differ from $R_{ij}$ because current can also flow along other paths.

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
| Graph | The edges present and their coupling strengths |
| Laplacian matrix $L$ | The operator $x\mapsto Lx$, summing differences from neighbors multiplied by the coupling strengths |
| Scalar-valued quadratic form $\mathcal Q$ | The sum of squared differences across edges, multiplied by the coupling strengths |

With fixed vertex labels, these representations determine one another. Coupling strengths are recovered from the off-diagonal Laplacian entries as $c_{ij}=-L_{ij}$. In the expanded quadratic form, the coefficient of $x_i x_j$ for $i<j$ is $-2c_{ij}$. Reconstruction requires the entire quadratic function, rather than its value at a single choice of numbers $x_i$.

In the electrical interpretation, vertex values become potentials, the equation $L\varphi=J$ determines them from the external currents, and $\mathcal Q(\varphi)$ is the dissipated power. The definitions of the graph, Laplacian, and function $\mathcal Q$ do not require this interpretation.

## Further reading

In [[Effective Resistance and Graph Geometry]], effective resistances are represented as squared Euclidean distances between points corresponding to the vertices.

Sources are listed in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the reading recommendations for the introductory series]]: Diestel for graph terminology; Doyle and Snell for electrical networks; Spielman for the Laplacian and its quadratic form.
