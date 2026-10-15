---
title: Couplings Within One Part of a Bipartite Graph
date: 2026-10-14
updated: 2026-10-15
revision: 4
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: couplings-within-one-part-of-a-bipartite-graph
order: 7
description: "From a participation table to couplings between objects: projections, decomposition of the Laplacian and its exponential, preservation of effective resistances, and the meaning of the common spanning-tree parameter."
---

Suppose we know which documents each employee has contributed to. We want to obtain couplings between employees that reflect their joint participation. Similar problems arise with products and purchases, words and texts, or contributors and projects. The input is a rectangular table; the result should be a graph on the elements of one selected set.

In PMG, this transition has a metric requirement: effective resistances between the retained vertices must remain unchanged. This determines the new coupling coefficients. We will examine how this requirement relates to projections and polyforms, how to perform the calculation column by column, and what the results for the two sides of the table have in common.

This is the final note in the series “Spaces and Subspaces in PMG”. It uses [[Projections, Bi-coordinates, and Di-coordinates|bi-coordinates and the Laplacian of a frame]], [[Selected Vertices and the Dirichlet Problem|projections in the Dirichlet problem]], and [[Vertex Elimination and Induced Couplings|elimination of internal vertices]].

## The participation table and the choice of a subspace

Take the example from article [1]. Three employees contribute to four documents. Denote Andrey by $a$, Boris by $b$, and Vladimir by $c$. A one indicates participation; a zero indicates its absence.

| Employee | $x_1$ | $x_2$ | $x_3$ | $x_4$ | Total |
|---|---:|---:|---:|---:|---:|
| Andrey, $a$ | 1 | 1 | 0 | 0 | 2 |
| Boris, $b$ | 1 | 1 | 1 | 0 | 3 |
| Vladimir, $c$ | 0 | 1 | 1 | 1 | 3 |
| Total | 2 | 3 | 2 | 1 | 8 |

This table defines a bipartite graph. Its parts $P=\{a,b,c\}$ and $X=\{x_1,x_2,x_3,x_4\}$ consist of employees and documents. Couplings occur only between the parts. In general, the entry $c_{px}\ge0$ specifies the coupling coefficient between $p\in P$ and $x\in X$; existing couplings have positive coefficients.

For now, assume that the original graph is connected and each part contains at least two vertices. The resistance metric is then defined on the entire space of affine vectors. The absence of a direct coupling between two employees does not mean that there is no effective resistance between them: paths through documents connect them.

Select part $P$. It generates an affine subspace of points and the corresponding vector space:

$$
\mathcal A_P=\left\{\sum_{p\in P}t_pp:\sum_pt_p=1\right\},
\qquad
W_P=\left\{\sum_{p\in P}h_pp:\sum_ph_p=0\right\}
$$

For example, $(a+b)/2$ is a point of $\mathcal A_P$, whereas $b-a$ is a vector of $W_P$. The vertices of $P$ form a selected set of formal basis vertices; they are not themselves a basis of the vector space $W_P$. With $a$ as the reference point, a basis of $W_P$ is given by $b-a,c-a$.

The two parts of a connected graph define two subspaces of one metric space. They are not independent components. Our task is to construct a graph on $P$ that reproduces the restriction of the original metric to $W_P$.

The original Laplacian has the polyform representation

$$
L=\sum_{x\in X}\sum_{p\in P}c_{px}[(px)]^2,
\qquad (px)=x-p
$$

The square in this notation denotes a formal quadratic form in PMG. Metric evaluation of $[(px)]^2$ gives the effective resistance $R_{px}$, which is the squared geometric length of the vector $x-p$.

## The projection of a vertex and its frame

Denote the sum of the coupling coefficients incident to document $x$ by

$$
d_x=\sum_{p\in P}c_{px}
$$

This is its weighted degree in the original graph. Suppose values $f_p$ are prescribed at the retained vertices and are to be extended to the documents. Vertices in part $X$ are not coupled to one another, so the Dirichlet condition at each of them is $d_xf_x=\sum_pc_{px}f_p$. As established in the note on the [[Selected Vertices and the Dirichlet Problem|Dirichlet problem]], the same coefficients determine the orthogonal projection of the vertex onto the selected affine subspace:

$$
\boxed{
q_x=\sum_{p\in P}b_{xp}p,
\qquad b_{xp}=\frac{c_{px}}{d_x},
\qquad \sum_pb_{xp}=1
}
\tag{1}
$$

The coefficients $b_{xp}$ are the bi-coordinates of the projection $q_x$, not of the original vertex $x$. Together with the selected vertices, they specify a frame of $q_x$. The residual $r_x=x-q_x$ is orthogonal to $W_P$.

In our example,

$$
q_{x_1}=\frac{a+b}{2},\qquad
q_{x_2}=\frac{a+b+c}{3},\qquad
q_{x_3}=\frac{b+c}{2},\qquad
q_{x_4}=c
$$

The last equality does not identify document $x_4$ with employee $c$. They are distinct points in the original space, but the projection of the document coincides with this vertex.

For the chosen frame, define its Laplacian:

$$
L_{q_x}=\sum_{p<q}b_{xp}b_{xq}[(pq)]^2
$$

The condition $p<q$ means that each unordered pair of vertices is counted once. The order is arbitrary and does not affect the quadratic forms.

> [!info] Decomposing a star
> **Lemma.** The contribution of all couplings incident to vertex $x$ decomposes into two forms:
>
> $$
> \sum_pc_{px}[x-p]^2
> =d_x[r_x]^2+d_xL_{q_x}
> \tag{2}
> $$
>
> The first concerns the direction of the projection residual; the second has its arguments in $W_P$.

> [!proof]- Proof
> From $\sum_pb_{xp}=1$ and $\sum_pb_{xp}p=q_x$, bilinearity gives
>
> $$
> \sum_pb_{xp}[x-p]^2
> =[x-q_x]^2+\sum_pb_{xp}[p-q_x]^2
> $$
>
> By the identity for the difference part of a frame, the last sum equals $L_{q_x}$. Multiplication by $d_x$ gives (2). This is an equality of forms; its proof requires no metric evaluation. $\square$

For document $x_1$, for example, $d_{x_1}=2$ and $L_{q_{x_1}}=\frac14[(ab)]^2$. Eliminating this document therefore leaves the contribution $2L_{q_{x_1}}=\frac12[(ab)]^2$.

## Induced couplings as a sum of frame Laplacians

Project the arguments of the original Laplacian onto $W_P$. The residuals $r_x$ map to zero, while forms on $W_P$ are preserved. Summing (2) gives

$$
\boxed{
\begin{aligned}
L_P&=\sum_x d_xL_{q_x}=\sum_{p<q}c^{(P)}_{pq}[(pq)]^2\\
c^{(P)}_{pq}&=\sum_x\frac{c_{px}c_{qx}}{d_x}
\end{aligned}
}
\tag{3}
$$

Thus each document contributes its frame Laplacian multiplied by $d_x$. Since the coefficients are nonnegative, a direct induced coupling between two employees is positive if and only if they have at least one document in common.

Calculate the contributions from the columns of the original table.

| Document | $d_x$ | Contribution to $ab$ | Contribution to $ac$ | Contribution to $bc$ |
|---|---:|---:|---:|---:|
| $x_1$ | 2 | $1/2$ | 0 | 0 |
| $x_2$ | 3 | $1/3$ | $1/3$ | $1/3$ |
| $x_3$ | 2 | 0 | 0 | $1/2$ |
| $x_4$ | 1 | 0 | 0 | 0 |
| Total | | $5/6$ | $1/3$ | $5/6$ |

Hence

$$
L_P=\frac56[(ab)]^2+\frac13[(ac)]^2+\frac56[(bc)]^2
$$

![[From Documents to Employee Couplings.svg]]

*Figure 1. Left: the original bipartite graph, with all eight coupling coefficients equal to $1$. Right: the employee graph after eliminating the documents. Vertex positions are schematic; the lengths of the drawn lines do not represent effective resistances.*

Document $x_4$ is coupled only to Vladimir, so its frame contains a single vertex and $L_{q_{x_4}}=0$. Such a document does not affect effective resistances between employees. The transformation describes their mutual couplings; an employee's individual activity can be recorded by a separate measure of the original data.

By the result on [[Vertex Elimination and Induced Couplings|vertex elimination]], the graph with Laplacian $L_P$ preserves all inner products of vectors in $W_P$ and of their exterior products. In particular, it preserves pairwise effective resistances. In our example,

$$
R_{ab}=R_{bc}=\frac{14}{15},\qquad R_{ac}=\frac43
$$

> [!proof]- Effective resistances of the resulting triangle
> Denote the three coupling coefficients by $u=c^{(P)}_{ab}$, $v=c^{(P)}_{ac}$, and $w=c^{(P)}_{bc}$. The spanning-tree coefficient is
>
> $$
> \tau_P=uv+uw+vw=\frac54
> $$
>
> In the product $\exp(L_P)[(ab)]^2$, the couplings $ac$ and $bc$ contribute to the spanning-tree form. The normalized potential therefore gives $R_{ab}=(v+w)/\tau_P$. Similarly, $R_{ac}=(u+w)/\tau_P$. Substitution gives the stated values; the equality $R_{ab}=R_{bc}$ follows by symmetry. $\square$

In a general graph, an individual coupling coefficient is not the reciprocal of the effective resistance between its endpoints. For example, here $1/c^{(P)}_{ab}=6/5$, whereas $R_{ab}=14/15$: the path through $c$ also affects the effective resistance.

The minimum energy and the response at the selected vertices $P$ are also preserved. For any prescribed values $f_p$, the energy of the resulting graph equals the minimum energy of the original graph over the document values, and the response at the retained vertices remains the same. This is a statement about the same metric transition, not an additional definition of the new couplings.

## Orthogonal residuals and the Laplacian exponential

A bipartite graph has a special property: the residuals $r_x=x-q_x$ are not only orthogonal to $W_P$, but also pairwise orthogonal to one another. Their squared lengths are expressed directly through the vertex degrees:

$$
\boxed{
r_x\cdot r_y=
\begin{cases}
1/d_x,&x=y\\
0,&x\ne y
\end{cases}
}
\tag{4}
$$

Contraction gives a geometric explanation. Identify all vertices of $P$ as a single vertex $o$. Since there are no couplings within $X$, the result is a star: each vertex $x$ is coupled only to $o$, with coefficient $d_x$. By the result on the [[Selected Vertices and the Dirichlet Problem|metric of residuals]], the edge vectors of this star correspond to the residuals $r_x$.

Summing the decompositions (2) gives an orthogonal decomposition of the Laplacian and a factorization of its exponential:

$$
\boxed{
\begin{aligned}
L&=L_P+\sum_xd_x[r_x]^2\\
M_G=\exp(L)&=M_P\prod_x\bigl(e+d_x[r_x]^2\bigr)
\end{aligned}
}
\tag{5}
$$

Here $M_P=\exp(L_P)$, and $e$ is the unit form. The exponential is taken in polyform algebra: $\exp(L)=e+L+L^2/2!+\cdots$, using its product of forms. The sum is finite because exterior products of degree greater than the dimension of the vector space vanish.

The first part of the Laplacian describes the selected subspace. Each remaining term belongs to one perpendicular direction. Thus eliminating part $X$ leaves the factor $M_P$ in the metric polyform.

> [!proof]- Orthogonality and factorization
> The vectors of distinct edges of a tree are orthogonal in the resistance metric, and the squared length of an edge vector is the reciprocal of its coupling coefficient. Apply this to the star described above. The isometry between its vector space and the space of residuals gives (4).
>
> In polyform algebra, the exponential of a sum equals the product of exponentials. For the form of a single vector, $([r_x]^2)^2=0$, since $r_x\wedge r_x=0$. Hence $\exp(d_x[r_x]^2)=e+d_x[r_x]^2$, which together with the first equality in (5) proves the second. $\square$

In the main example, the squared lengths of the residuals are $1/2,1/3,1/2,1$. Write $r_i=r_{x_i}$ for brevity. Then

$$
M_G=M_P
\bigl(e+2[r_1]^2\bigr)\bigl(e+3[r_2]^2\bigr)
\bigl(e+2[r_3]^2\bigr)\bigl(e+[r_4]^2\bigr)
$$

Document $x_4$ adds no couplings between employees, since $q_{x_4}=c$ and $L_{q_{x_4}}=0$. In the original space, however, it has a nonzero residual $r_{x_4}=x_4-c$ of squared length $1$. Its factor is present in the full metric polyform.

Each of these factors describes a residual direction, not a separate connected component: the original graph remains connected. Selecting part $X$ instead of $P$ gives a different orthogonal decomposition of the same Laplacian. The metric polyform of the induced document graph takes the role of $M_P$; the other factors correspond to the residuals of the employee projections onto the document space.

## The matrix representation and its diagonal

Denote the original rectangular table by $\mathbf H=(c_{px})$: its rows correspond to $P$, and its columns to $X$. Let $\mathbf D_X$ be the diagonal matrix of degrees $d_x$, and let $\mathbf D_P$ contain the original degrees $d_p=\sum_xc_{px}$.

The original Laplacian matrix has the block form

$$
\mathbf L=
\begin{pmatrix}
\mathbf D_P&-\mathbf H\\
-\mathbf H^{\mathsf T}&\mathbf D_X
\end{pmatrix}
$$

The superscript $\mathsf T$ denotes transposition, which exchanges rows and columns. The diagonal form of both blocks $\mathbf D_P,\mathbf D_X$ expresses the absence of couplings within the parts.

Introduce the auxiliary matrix

$$
\mathbf K=\mathbf H\mathbf D_X^{-1}\mathbf H^{\mathsf T},
\qquad
\mathbf L_P=\mathbf D_P-\mathbf K
\tag{6}
$$

The inverse diagonal matrix $\mathbf D_X^{-1}$ contains the numbers $1/d_x$. The rows of the influence matrix from the Dirichlet problem correspond to documents, so in this notation $\mathbf B=\mathbf D_X^{-1}\mathbf H^{\mathsf T}$ and $\mathbf K=\mathbf H\mathbf B$.

In the notation of the notes on the Dirichlet problem and elimination, this means

$$
I=X,\qquad \mathbf C=\mathbf H^{\mathsf T},\qquad
\mathbf A=\mathbf D_X,\qquad \boldsymbol\Lambda=\mathbf L_P,\qquad
\mathbf{Fm}=\mathbf D_X^{-1}
$$

The diagonal form of $\mathbf{Fm}$ again expresses the orthogonality of the residual vectors of different documents.

The off-diagonal entries $K_{pq}$ are the induced coupling coefficients. The diagonal entries are generally nonzero as well:

$$
K_{pp}=\sum_x\frac{c_{px}^2}{d_x}
$$

They do not specify loops in the graph model considered here. When constructing the Laplacian, its diagonal is determined by the sum of coupling coefficients to other vertices. Indeed,

$$
\sum_qK_{pq}=d_p,
\qquad
d^{(P)}_p=\sum_{q\ne p}c^{(P)}_{pq}=d_p-K_{pp}
$$

Thus preserving the row sums of the full matrix $\mathbf K$ does not mean preserving the degrees of the resulting graph.

In our example,

$$
\mathbf K=\frac16
\begin{pmatrix}
5&5&2\\
5&8&5\\
2&5&11
\end{pmatrix},
\qquad
\mathbf L_P=\frac16
\begin{pmatrix}
7&-5&-2\\
-5&10&-5\\
-2&-5&7
\end{pmatrix}
$$

The row sums of $\mathbf K$ are the original degrees $2,3,3$, whereas the new degrees are $7/6,10/6,7/6$. Their sum is $4$, although the sum of the original employee degrees is $8$.

The factor $1/6$ is essential. If only the integer matrix is displayed for convenience, this factor must still be retained in calculations: multiplying all coupling coefficients by six divides every effective resistance by six.

## What normalization by document degree means

If a document has unit couplings to $k$ employees, its contribution to each pair is $1/k$. For $k=2$, we obtain a single coupling of coefficient $1/2$; for $k=3$, a triangle with coupling coefficients $1/3$.

Division by $d_x$ follows from vertex elimination and preservation of the metric. For binary data, simply multiplying the table by its transpose, $\mathbf H\mathbf H^{\mathsf T}$, counts common documents, but in general it defines different couplings and a different metric.

This division must be distinguished from normalizing the original columns beforehand. Replacing $c_{px}$ by $\widehat c_{px}=c_{px}/d_x$ makes the sum of each nonempty column equal to $1$. Applying (3) to this table gives

$$
\widehat c^{(P)}_{pq}=\sum_x\frac{c_{px}c_{qx}}{d_x^2}
=\sum_xb_{xp}b_{xq}
$$

This eliminates vertices from a different original graph. For example, two couplings of coefficient $1$ through a single document yield an induced coupling of coefficient $1/2$. After column normalization, the original coefficients become $1/2$ and the induced coefficient becomes $1/4$; the effective resistance between the employees increases from $2$ to $4$.

For heterogeneous data, choosing the original coupling coefficients is part of building the model. Hours, comment counts, and monetary amounts cannot simply be added as quantities of the same kind. Column normalization is one possible modeling choice, but does not by itself justify assigning equal importance to different features. A claim of metric preservation always refers to a specific chosen table.

## Two induced graphs

We can exchange the roles of the parts: retain the documents and eliminate the employees. Then

$$
c^{(X)}_{xy}=\sum_p\frac{c_{px}c_{py}}{d_p},
\qquad x\ne y
$$

This gives two alternative graphs, each preserving the metric of its own part. It does not split the original space into independent components. Constructing the document graph is also not the inverse operation to constructing the employee graph.

Their common origin does not require the two graphs to have equal resistance radii, degree sums, or spanning-tree coefficients. Consider a small weighted example.

| Employee | $x$ | $y$ | $d_p$ |
|---|---:|---:|---:|
| $a$ | 1 | 1 | 2 |
| $b$ | 2 | 0 | 2 |
| $d_x$ | 3 | 1 | 4 |

After eliminating the documents, the coupling coefficient of $ab$ is $1\cdot2/3=2/3$. After eliminating the employees, the coefficient of $xy$ is $1\cdot1/2=1/2$.

![[Two Parts and Two Induced Graphs.svg]]

*Figure 2. One weighted bipartite graph and two results of elimination. Colors identify the parts; edge labels give coupling coefficients. The lower graphs correspond to two alternative choices of the retained subspace.*

| Quantity | Graph on $\{a,b\}$ | Graph on $\{x,y\}$ |
|---|---:|---:|
| Coupling coefficient | $2/3$ | $1/2$ |
| Sum of degrees | $4/3$ | $1$ |
| Effective resistance between the vertices | $3/2$ | $2$ |
| Resistance radius $\rho$ | $3/8$ | $1/2$ |
| Spanning-tree coefficient $\tau$ | $2/3$ | $1/2$ |

By the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|definition of resistance radius]], $\rho$ is the squared radius of the circumsphere. For two vertices with effective resistance $r$, it equals $r/4$. The spanning-tree coefficient of a graph consisting of a single coupling is its coupling coefficient.

## Why the resistance radii of the parts do not add up

Unequal resistance radii of the two induced graphs do not yet answer another question: does their sum equal the resistance radius of the original graph? Denote the resistance radii of the graphs on $P$ and $X$ by $\rho_P,\rho_X$.

In the example of Figure 2, the original graph is a tree with coupling coefficients $1,1,2$. By the tree resistance radius formula from the note on [[Vertex Contraction and Graph Gluing|graph gluing]],

$$
\rho(G)=\frac14\left(1+1+\frac12\right)=\frac58,
\qquad
\rho_P+\rho_X=\frac38+\frac12=\frac78
$$

Thus the resistance radii of the two induced graphs are not additive in general.

The geometric relation is expressed through the circumcenters. Denote the circumcenter of the original graph by $h$, and those of the two parts by $h_P,h_X$. All three centers are considered in the original metric space: the induced graphs preserve the metrics of their respective parts.

By the [[Vertex Elimination and Induced Couplings#Resistance radius and projection of the circumcenter|general lemma on the resistance radius of a selected subspace]], the centers $h_P,h_X$ are the orthogonal projections of $h$ onto the affine subspaces of the corresponding parts. Therefore

$$
\boxed{
\rho(G)=\rho_P+\|h-h_P\|^2
=\rho_X+\|h-h_X\|^2
}
\tag{7}
$$

Here $\|h-h_P\|^2$ is the squared distance between the centers. In particular, each individual resistance radius does not exceed the original resistance radius: $\rho_P\le\rho(G)$ and $\rho_X\le\rho(G)$.

In the example of Figure 2, the squared distances from the original circumcenter to the circumcenters of the parts are $5/8-3/8=1/4$ and $5/8-1/2=1/8$. These two distances explain the change in each resistance radius, but do not give an additive decomposition of resistance radius over the parts.

Nor is there a universal direction of inequality for the sum. Consider the complete bipartite graph $K_{2,6}$: one part has two vertices, the other six, and every vertex of the first part is coupled to every vertex of the second with coefficient $1$. Direct calculation gives

$$
\rho_P=\frac1{12},\qquad
\rho_X=\frac5{12},\qquad
\rho(G)=\frac{29}{48}
$$

Here $\rho_P+\rho_X=1/2<29/48=\rho(G)$, whereas in the example of Figure 2 the sum exceeds the original resistance radius.

> [!example]- Calculating the resistance radii for $K_{2,6}$
> Denote the parts by $P=\{a,b\}$ and $X=\{x_1,\ldots,x_6\}$. Eliminating $X$ gives a coupling of coefficient $3$ between $a,b$; eliminating $P$ gives coefficient $1/3$ between every pair of distinct $x_i$. The resistances are
>
> $$
> R_{ab}=\frac13,\qquad R_{x_i x_j}=1\ (i\ne j),\qquad
> R_{a x_i}=R_{b x_i}=\frac7{12}
> $$
>
> The last value follows from the Laplacian equations with response $1$ at $a$, $-1$ at $x_1$, and $0$ at the other vertices: fixing the value at $x_1$ to $0$ gives $7/12$ at $a$, $5/12$ at $b$, and $1/2$ at the other $x_i$. The difference between the values at $a,x_1$ is the resistance.
>
> For $m$ equidistant vertices with common resistance $r$, the center is their mean, and the frame form decomposition gives $\rho=(m-1)r/(2m)$. Hence $\rho_P=1/12$ and $\rho_X=5/12$.
>
> Find the center of the whole graph using the frame
>
> $$
> h=-\frac34(a+b)+\frac5{12}\sum_{i=1}^{6}x_i
> $$
>
> Its coefficients $h^w$ sum to $1$. For any vertex $v$, set $t_v=\sum_w h^wR_{vw}$. On the two parts, we obtain
>
> $$
> \begin{aligned}
> t_a=t_b&=-\frac34\cdot\frac13+6\cdot\frac5{12}\cdot\frac7{12}=\frac{29}{24}\\
> t_{x_i}&=2\left(-\frac34\right)\frac7{12}+5\cdot\frac5{12}=\frac{29}{24}
> \end{aligned}
> $$
>
> By the [[Projections, Bi-coordinates, and Di-coordinates#Decomposing a form using frame elements and their differences|frame form decomposition]], the vector $v-h$ has norm
>
> $$
> \|v-h\|^2=t_v-\frac12\sum_w h^w t_w
> =\frac{29}{24}-\frac{29}{48}=\frac{29}{48}
> $$
>
> This value is independent of $v$, so $h$ is the circumcenter and $\rho_G=29/48$.

Gluing at a single vertex joins orthogonal spaces with a common point, and resistance radius is additive. Selecting the two parts is a different construction. Their vector spaces are generally not orthogonal, and the sum of their dimensions is one less than the dimension of the entire space: a direction between the parts is also needed. The additivity rule for gluing therefore does not apply here.

## A common spanning-tree parameter of the original graph

Denote the spanning-tree coefficient of the original bipartite graph by $\tau_G$, and those of the two induced graphs by $\tau_P,\tau_X$. The quantity $\tau$ is the sum, over spanning trees, of the products of their coupling coefficients; for a graph with unit coefficients, it is the number of spanning trees.

> [!info] Two ways to calculate one spanning-tree coefficient
> **Lemma.** For a connected bipartite graph,
>
> $$
> \boxed{
> \tau_G=\tau_P\prod_{x\in X}d_x
> =\tau_X\prod_{p\in P}d_p
> }
> \tag{8}
> $$
>
> All degrees in this formula belong to the original graph.

> [!proof]- Proof through the metric polyform
> Consider the highest nonzero grade component of the product (5). Select a reference vertex $p_0\in P$. The note on vertex elimination shows that replacing the vectors $x-p_0$ with the residuals $r_x$, while retaining a basis of $W_P$, is a change of basis with determinant $1$. Thus the product of the spanning-tree form on $P$ and the squares of all $r_x$ is the original spanning-tree form. Its coefficient in (5) is $\tau_P\prod_xd_x$. Eliminating part $P$ gives the second expression for the same coefficient $\tau_G$. $\square$

The sum of all original coupling coefficients is

$$
S=\sum_{p,x}c_{px}=\sum_pd_p=\sum_xd_x
$$

**Definition.** Let $J(G)$ denote the following dimensionless normalization of the spanning-tree coefficient of the original bipartite graph. We will call it the **common spanning-tree parameter of the two parts**:

$$
\boxed{
\begin{aligned}
J(G)&=\frac{S\tau_G}{\left(\prod_pd_p\right)\left(\prod_xd_x\right)}\\
&=\frac{S\tau_P}{\prod_pd_p}=\frac{S\tau_X}{\prod_xd_x}
\end{aligned}
}
\tag{9}
$$

The first line of (9) is the definition; the equalities in the second line follow from (8). The notation $J(G)$ is introduced in this note. It is a parameter of the original graph that can be calculated through either part, provided the original degrees are retained.

Multiplying all original coupling coefficients by the same positive factor leaves $J(G)$ unchanged. Indeed, if there are $N$ vertices in total, every spanning tree contains $N-1$ edges. The numerator and denominator of the first expression in (9) are therefore multiplied by the same power of that factor, namely $N$.

To explain the normalization, construct a comparison graph $G_0$ on the same vertices:

$$
c^{(0)}_{px}=\frac{d_pd_x}{S}
$$

It has the same original weighted degrees: summing over $x$ gives $d_p$, and summing over $p$ gives $d_x$. Each vertex of $P$ is now coupled to every vertex of $X$, and the fraction of its total coupling assigned to document $x$ is $d_x/S$, the same for every employee.

The spanning-tree coefficient of this graph and the ratio of the two spanning-tree coefficients are

$$
\tau_{G_0}=\frac{\left(\prod_pd_p\right)\left(\prod_xd_x\right)}{S},
\qquad
\boxed{J(G)=\frac{\tau_G}{\tau_{G_0}}}
\tag{10}
$$

Thus $J(G)$ compares the weighted spanning-tree sum of the original graph with that of a complete bipartite graph whose degrees are preserved and whose couplings are distributed by the formula above.

> [!proof]- The spanning-tree coefficient of the comparison graph
> Eliminating part $X$ from $G_0$ by (3) gives the couplings
>
> $$
> c^{(P,0)}_{pq}
> =\sum_x\frac{(d_pd_x/S)(d_qd_x/S)}{d_x}
> =\frac{d_pd_q}{S}
> $$
>
> The same couplings result from taking a star with center $o$, coupling it to each vertex $p$ with coefficient $d_p$, and eliminating the center. This star has a single spanning tree, so its spanning-tree coefficient is $\prod_pd_p$. The center has degree $S$. By the rule for the change in the spanning-tree coefficient under single-vertex elimination, the induced graph has coefficient $\tau_{P,0}=(\prod_pd_p)/S$. Applying (8) to $G_0$ gives $\tau_{G_0}=\tau_{P,0}\prod_xd_x$, which proves (10). $\square$

In the example of Figure 2, the original graph is itself a tree, so $\tau_G=2$. We obtain

$$
\tau_Pd_xd_y=\frac23\cdot3\cdot1=2,
\qquad
\tau_Xd_ad_b=\frac12\cdot2\cdot2=2
$$

The comparison graph for this example is specified by the table

$$
\mathbf H_0=
\begin{pmatrix}
3/2&1/2\\
3/2&1/2
\end{pmatrix}
$$

Its row sums remain $2,2$, and its column sums are $3,1$. Its spanning-tree coefficient is $2\cdot2\cdot3\cdot1/4=3$. Hence $J(G)=2/3$; the same value is obtained through either induced graph.

For the main example with three employees and four documents, $S=8$, $\prod_pd_p=18$, and $\prod_xd_x=12$. From $\tau_P=5/4$, we obtain $\tau_G=15$, $\tau_X=5/6$, and

$$
J(G)=\frac{8\cdot(5/4)}{18}
=\frac{8\cdot(5/6)}{12}=\frac59
$$

Here the comparison graph has spanning-tree coefficient $\tau_{G_0}=18\cdot12/8=27$. The ratio $15/27$ again gives $5/9$.

Equality (9) relates two representations of a single characteristic of the bipartite graph. To calculate it through an induced graph, we must retain the original vertex degrees. They differ from the new degrees and generally cannot be recovered from the new couplings alone.

Mutual projections of the two subspaces also allow common spectral characteristics to be studied. That problem requires a separate treatment of angles between subspaces and lies beyond the present applied construction.

## Calculation from a table and limitations

The following algorithm suffices to obtain couplings within part $P$.

1. Sum the entries of each column to obtain $d_x$.
2. In each nonempty column, consider pairs of distinct rows with nonzero entries.
3. For a pair $p,q$, add $c_{px}c_{qx}/d_x$ to its coupling coefficient.
4. Sum the contributions of all columns for each pair.
5. If characteristics of both parts are needed, retain the original row and column sums alongside the result.

No large matrix inversion is required. If the data are stored as records of the form “object, document, coupling coefficient”, first combine repeated records for the same pair by summation. Then group the records by document and form pairs of objects within each group.

Consider the special cases.

- **Zero column.** It represents an isolated document, has no effect on the result, and is omitted from the calculation. Division by $d_x=0$ is undefined.
- **Zero row.** The corresponding object remains isolated. No finite effective resistance between it and other components is created.
- **Disconnected original graph.** Apply the construction component by component. Each component containing edges gives a connected graph on the vertices of its retained part; if there is only one such vertex, the result is a single point. Formulas normalized by $\tau_G$ are applied separately within connected components.
- **A single retained vertex.** There are no induced couplings: $L_P=0$, $M_P=e$, and $\tau_P=1$. The retained vector space is zero-dimensional.
- **Removing small induced couplings.** This additional processing generally changes the metric. Exact preservation of effective resistances refers to the full result (3).

If every connected component of the original graph contains at least one retained vertex, the number of resulting components equals the original number. The reason is simple: a path between two vertices of one part consists of two-step transitions through the opposite part, and each such transition creates a positive induced coupling. Vertices in different components have no common neighbors.

The construction uses the metric of affine vectors, projections, and the polyform algebra of the published core. The isotropic representation and the null vector are not required for these results.

## Sources and status of the results

The application and the original table of the main example come from [1]. Here the transformation is presented through a selected subspace, bi-coordinates of projections, and frame Laplacians. Classical vertex elimination, the Schur complement, and preservation of effective resistances are compared with [2]. Their presentation in the language of PMG makes no claim of novelty for the operation itself.

The star decomposition (2), the induced Laplacian (3), orthogonality of residuals (4), factorization of the exponential (5), the relation between resistance radii through circumcenters (7), and the spanning-tree relations (8)-(10) are derived in the text using results from the preceding notes and the [[Core specification|core specification]]. The notation $J(G)$ and the name “common spanning-tree parameter” are used here for normalization (9); equality (10) explains its meaning. The applicability conditions and notation follow the [[PMG terminology|terminology]]. The note contains no working conjectures.

The numerical examples were checked using exact rational arithmetic. Effective resistances were calculated separately from the original and induced Laplacians; spanning-tree coefficients were checked by direct enumeration of spanning trees. The coefficients of the polyform decomposition (2), the effect of column normalization, and equality (8) for both parts were also checked. For the two bipartite examples, inner products of residuals were calculated from the original metric, and spanning-tree coefficients of the comparison graphs were checked by tree enumeration. Resistance radii and circumcenters in the example of Figure 2 and in $K_{2,6}$ were calculated from the equations of equal distance to the vertices, and equality (7) was verified.

1. Malyugin, D. V. [How to Connect the Unconnected](https://habr.com/ru/articles/533544/) (in Russian). Habr, 24 December 2020. The application, the transformation of a coupling table, and the example with three objects and four intermediaries.
2. Dörfler, F.; Bullo, F. [Kron Reduction of Graphs with Applications to Electrical Networks](https://arxiv.org/abs/1102.2950). Preprint, 2011. Formula (3.4): single-vertex elimination; Theorem 3.9: preservation of effective resistances. The general vertex-elimination result is applied here to a part with no internal couplings.

