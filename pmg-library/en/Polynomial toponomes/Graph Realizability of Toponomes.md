---
title: Graph Realizability of Toponomes
date: 2026-10-23
updated: 2026-10-23
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: graph-realizability-of-toponomes
lang: en
description: "Necessary conditions and an exact finite system for graph realizability of toponomes, Mason's theorem, a nonrealizable triangle, and a complete weighted spectral criterion."
order: 5
---

The canonical forest expansion of the Laplacian exponential produces a partition toponome, a coefficient triangle, and one-variable polynomials. The inverse question is whether a graph exists that gives prescribed coefficients. Not every table of nonnegative integers is a graph table: its cells must simultaneously describe forests of one edge system.

**Graph realizability can be expressed by an exact finite system of equations. Necessary conditions on individual coefficients provide simpler tests but do not replace that system. For the one-variable vertex toponome with arbitrary positive conductances, there is a short complete criterion: the constant term is one and all roots are real and negative.**

## What graph realizability means

**Definition.** Graph realizability of a toponome or coefficient table in a specified graph class means that some graph in that class has a canonical forest expansion producing the prescribed object under the chosen reduction and normalization.

The [[From Polyforms to Partitions#The Laplacian exponential and forest coefficients|forest expansion of the exponential]] is fixed. Arbitrary rewriting of the polyform using structural identities can change its formal toponome and is not allowed here. Realizability means existence of a graph; uniqueness of reconstruction is a separate question. Already, [[Coefficient Tables of Toponomes#Does the table distinguish all graphs?|different trees can have the same table]].

The main sections concern finite simple undirected graphs with unit conductances and **vector normalization**. The weighted case and vertex normalization are specified separately. The vertex count $n$ may be prescribed additionally. Isolated vertices change neither positive types nor polynomial toponomes.

Suppose a finite table is given as the polynomial

$$
A(t,u)=1+\sum_{k\geqslant1}\sum_{r=1}^k a_{k,r}t^ku^r
$$

For a graph table, $a_{k,r}$ counts spanning forests with $k$ edges and $r$ nontrivial components. Denote the column sums by

$$
f_0=1,\qquad f_k=\sum_r a_{k,r},\qquad A(t,1)=\sum_k f_kt^k
$$

The case $A=1$ is realized by an edgeless graph. When discussing the highest column below, assume $d=\deg_t A\geqslant1$.

## First necessary conditions

### Signs, integrality, and admissible cells

For unit conductances,

$$
a_{k,r}\in\mathbb Z_{\geqslant0},\qquad
A(t,0)=A(0,u)=1
$$

A nontrivial component contains at least one edge, and a forest with parameters $(k,r)$ occupies $k+r$ nonisolated vertices. Thus, for prescribed $n$,

$$
a_{k,r}=0\quad\text{if }r>k\text{ or }k+r>n
$$

Moreover, $f_k>0$ for every $0\leqslant k\leqslant d$: deleting edges from a maximum-size forest gives forests of every smaller size. These conditions capture only the most general properties of the table's support.

### The highest column and the number of nonisolated vertices

> [!info] A unique highest cell
> **Lemma.** The highest column of the table of a graph with positive conductances has exactly one nonzero cell. Its second index is the number of graph components containing edges. If there are $q$ such components, then
>
> $$
> [t^d]A(t,u)=\gamma u^q,\qquad \gamma>0
> $$
>
> The table determines the number of nonisolated vertices:
>
> $$
> \boxed{N=d+q}
> $$

> [!proof]- Proof
> **Proof.** Let $G_1,\ldots,G_q$ be the components with edges, of sizes $n_i$. A maximum-size forest contains one spanning tree in each. Therefore
>
> $$
> d=\sum_{i=1}^q(n_i-1),\qquad N=\sum_{i=1}^q n_i=d+q
> $$
>
> All such forests have $q$ nontrivial components. Their total weight in vector normalization is $\gamma=\prod_i\tau(G_i)>0$. In vertex normalization, this is additionally multiplied by $\prod_i n_i$; the cell position is unchanged. $\square$

If a proposed table has two nonzero cells in its highest column, no graph with positive conductances realizes it. If that cell is unique, the restrictions $k+r\leqslant N$ must also be checked in the other columns. If the total vertex count is given, $n\geqslant N$ is necessary; the difference $n-N$ counts isolated vertices.

For the full partition toponome, the condition is stronger: the positive type of highest grade is unique and equals $(n_1-1,\ldots,n_q-1)$. It therefore determines the sizes of all nontrivial components. The table retains only their number.

### One and two connections

Set $M=a_{1,1}$. In the unweighted case, this is the edge count, so in particular $d\leqslant M\leqslant\binom N2$.

**Lemma.** The two cells in the second column sum to the number of all edge pairs. Their distribution distinguishes adjacent and independent pairs:

$$
\boxed{a_{2,1}+a_{2,2}=\binom M2}
$$

$$
a_{2,1}=\sum_{v}\binom{\deg v}{2},
\qquad
a_{2,2}=\binom M2-a_{2,1}
$$

**Proof.** Any two distinct edges in a simple graph form a forest. If they share a vertex, they give one nontrivial component; otherwise they give two. An adjacent pair has exactly one shared vertex, so the vertex sum counts each such pair once. $\square$

Consequently, realization requires degrees $\delta_1,\ldots,\delta_N$ satisfying

$$
1\leqslant\delta_i\leqslant N-1,
\qquad
\sum_i\delta_i=2M,
\qquad
\sum_i\binom{\delta_i}{2}=a_{2,1}
$$

These equalities alone do not guarantee a graph with those degrees and the other prescribed coefficients.

**Corollary.** The number of adjacent pairs has the lower bound

$$
\boxed{a_{2,1}\geqslant M-q}
$$

**Proof.** Replace each graph edge by a vertex of an auxiliary graph, joining two such vertices when the original edges are adjacent. This gives $M$ vertices, $q$ connected components, and $a_{2,1}$ edges. Each connected component has at least its vertex count minus one edges. Summing gives the inequality. $\square$

### Column sums

For every $k$, $f_k\leqslant\binom Mk$, since forests are among all edge subsets. More precisely,

$$
f_1=M,\qquad f_2=\binom M2,
\qquad f_3=\binom M3-N_\triangle(G)
$$

Here $N_\triangle(G)$ is the triangle count. The last equality follows because a three-edge set contains a cycle exactly when it is itself a triangle.

Forest counts of different sizes are also related. For example, double-counting pairs consisting of a $k$-edge forest and an edge that can be added without creating a cycle gives

$$
(k+1)f_{k+1}\leqslant(M-k)f_k
$$

Every $(k+1)$-edge forest arises in $k+1$ ways, while a $k$-edge forest admits at most $M-k$ added edges. A stronger general restriction appears in the section on Mason's theorem.

## A nonrealizable triangle with valid column sums

Consider the formal polynomial

$$
\boxed{A_*(t,u)=1+3tu+t^2u+2t^2u^2+t^3u}
$$

Its triangle in our chosen orientation is

$$
\begin{array}{ccc}
3&1&1\\
&2&
\end{array}
$$

Columns correspond to $k=1,2,3$, and rows to $r=1,2$; the unit term is omitted. The coefficients are nonnegative integers. The highest cell gives $d=3$, $q=1$, and $N=4$, and all cell positions are admissible. The column sums are also consistent:

$$
A_*(t,1)=1+3t+3t^2+t^3=(1+t)^3
$$

This is the one-variable vector toponome of every three-edge tree. Yet the triangle itself is not realized by a simple unweighted graph: it requires $M=3$ and $a_{2,1}=1$, violating $a_{2,1}\geqslant M-q=2$.

The same contradiction can be seen by listing possible trees. After removing isolated vertices, the required graph must be connected on four vertices with three edges. Only the path $P_4$ and the star $K_{1,3}$ are possible:

| Object | Adjacent pairs $a_{2,1}$ | Independent pairs $a_{2,2}$ |
| --- | ---: | ---: |
| Path $P_4$ | 2 | 1 |
| Star $K_{1,3}$ | 3 | 0 |
| Table $A_*$ | 1 | 2 |

![The four-vertex path and star have two and three adjacent edge pairs, respectively; the proposed triangle requires only one](Graph%20Realizability%20-%20Path%20and%20Star.svg)

*Figure 1. All trees on four vertices up to isomorphism. In both cases, the second column sums to three, but its distribution between adjacent and independent pairs differs.*

**Corollary.** Realizability of a one-variable reduction does not guarantee realizability of the original coefficient table.

## What reducibility conditions provide

Under ordinary multiplication, a graph triangle has a [[Reducibility of Toponomes#The two-variable toponome and the coefficient triangle|factorization by nontrivial components]]. Thus, for $q>1$, there must be $q$ graph factors; for $q=1$, the polynomial is irreducible. Under the [[Reducibility of Toponomes#Irreducibility of the table under the second-kind product|second-kind product]], every nonempty forest table is irreducible regardless of connectivity. Both irreducibility statements hold over $\mathbb R$ and $\mathbb C$.

These results provide necessary tests but not a sufficient criterion. The polynomial $A_*$ is also irreducible under ordinary multiplication: $A_*(t,0)=A_*(0,u)=1$, and its leading coefficient in $t$ is $u$, so the argument of the two-variable theorem applies.

In the falling-power representation of the second-kind product, the image of $A_*$ is

$$
\widehat A_*(t,u)=1+3tu+t^2u+2t^2u(u-1)+t^3u
$$

It has the same values on the coordinate axes and the same leading coefficient $u$, so it too is irreducible. The counterexample thus passes both irreducibility tests while retaining the combinatorial contradiction in its second column.

## Mason's theorem and forest counts

### Why a matroid appears here

A matroid describes a family of independent subsets of a finite set. Deleting elements preserves independence; moreover, if one independent set is smaller than another, some element of the larger can be added to the smaller while preserving independence. In the graphic matroid, the ground set consists of **edges**, and independent sets are acyclic edge sets.

For forests, the exchange property is immediate. If a forest $F$ has fewer edges than a forest $H$, some edge of $H$ joins different components of $F$ and can be added to it. Otherwise every edge of $H$ would lie within a component of $F$, and acyclicity would give $|H|\leqslant|F|$.

“Graphic matroid” is the standard name for this construction; we use “graph realizability” for the problem considered here. Independent sets of a matroid must not be confused with independent sets of graph **vertices**. Here, as throughout the series, forests are completed with all original vertices, including isolated ones.

### Statement and meaning of the inequalities

Mason's strong conjecture, formulated in 1972, has now been proved. Independent proofs were given by Anari, Liu, Oveis Gharan, and Vinzant [1], and by Brändén and Huh [2]. We use an established theorem below, not a new PMG result.

> [!info] Ultra-log-concavity of forest counts
> **Theorem.** Forest counts divided by the numbers of all edge subsets of the same size form a log-concave sequence. For a graph with $M$ edges, set
>
> $$
> g_k=\frac{f_k}{\binom Mk},\qquad 0\leqslant k\leqslant M
> $$
>
> Then
>
> $$
> \boxed{g_k^2\geqslant g_{k-1}g_{k+1}},\qquad 1\leqslant k<M
> $$

**Justification of the application.** The general theorem gives this inequality for the numbers of independent sets of any matroid on $M$ elements [1, Theorem 1.2; 2, Theorem 4.14]. For the graphic matroid, those numbers are $f_k$. The general proof is given in the sources and is not reproduced here. In our simple graph, the boundary case $k=1$ also follows directly from $f_1=M$ and $f_2=\binom M2$. For $M\leqslant1$, there is nothing to check.

The number $g_k$ has a simple meaning: the probability that a uniformly selected $k$-edge subset is a forest. Log-concavity means that, for positive terms, the ratios $g_{k+1}/g_k$ do not increase. This is stronger than mere monotonicity of $g_k$, which follows from the double count above. In unnormalized coefficients,

$$
f_k^2\geqslant
\frac{(k+1)(M-k+1)}{k(M-k)}\,f_{k-1}f_{k+1},
\qquad 1\leqslant k<M
$$

The denominator of $g_k$ uses the edge count $M$, not the vertex count $n$ or the highest grade $d$. This normalization of combinatorial counts differs from the vector and vertex normalizations of a toponome. Set $f_k=0$ for $k>d$.

**Example.** For the unit-weight complete graph $K_4$,

$$
(f_0,\ldots,f_6)=(1,6,15,16,0,0,0),
\qquad
(g_0,\ldots,g_6)=(1,1,1,4/5,0,0,0)
$$

Of the twenty three-edge sets, four are triangles and sixteen are trees. The inequalities hold. For the nonrealizable triangle $A_*$, the sequence $g_k$ is $(1,1,1,1)$ and also satisfies them. **Mason's theorem restricts column sums but does not establish realizability of their distribution among rows.** The stated version concerns unweighted forest counts; replacing them with arbitrary weighted sums requires separate justification.

## An exact realizability system

### Graphs with unit conductances

Fix $n$. Introduce an unknown $x_{ij}$ for each vertex pair and require

$$
x_{ij}\in\{0,1\},\qquad 1\leqslant i<j\leqslant n
$$

Let $\mathcal F(K_n)$ be all spanning forests of the complete graph, and $r(F)$ the number of nontrivial components of a forest. Define the universal polynomial

$$
\mathcal U_n(t,u;\mathbf x)=
\sum_{F\in\mathcal F(K_n)}
\left(\prod_{ij\in E(F)}x_{ij}\right)t^{|E(F)|}u^{r(F)}
$$

> [!info] A criterion by existence of a solution
> **Theorem.** A table is realized by a simple unweighted graph on $n$ vertices if and only if there are values $x_{ij}\in\{0,1\}$ for which $\mathcal U_n(t,u;\mathbf x)=A(t,u)$. Coefficientwise, this is the finite system
>
> $$
> \boxed{
> a_{k,r}=
> \sum_{\substack{F\in\mathcal F(K_n)\\|E(F)|=k,\ r(F)=r}}
> \prod_{ij\in E(F)}x_{ij}
> }
> $$
>
> The equalities are required for all cells, including prescribed zero coefficients and $a_{0,0}=1$.

**Proof.** From a solution, construct the graph whose edges are the pairs $ij$ with $x_{ij}=1$. The variable product is one exactly for forests of this graph; all other terms vanish. Thus the system gives its table. Conversely, edge indicators of any realizing graph satisfy every equality. $\square$

The Boolean conditions can be written as equations $x_{ij}^2-x_{ij}=0$ over the reals. One can search by enumerating graphs or solving a system with Boolean variables. The criterion is exact, but promises no fast algorithm and does not reduce to the coefficient inequalities already listed.

If $n$ is unknown, the highest column must first have the form $\gamma u^q$. It suffices to check realization on $N=d+q$ vertices: isolated vertices can be removed from any solution. For a prescribed $n\geqslant N$, they are then added back. The case $A=1$ is treated separately.

### Other normalizations and reductions

For graphs with arbitrary positive conductances on existing edges, replace the Boolean conditions by $x_{ij}\geqslant0$. Zero means an absent edge, and a positive value is its conductance. The same system now sums forest weights.

For vertex normalization, additionally multiply each forest's contribution by its root weight

$$
h(F)=\prod_{C\in\pi(F)}|C|
$$

Here $\pi(F)$ consists of the forest components; singleton vertices contribute a factor of $1$. For the full partition toponome, forests are grouped by positive type; for a one-variable polynomial, only by edge count. Each kind of toponome thus has its own system of equalities in the same edge variables.

If only a one-variable polynomial of positive degree $d$ is specified, the number $q$ of nontrivial components is no longer known. However, $1\leqslant q\leqslant d$, so $N=d+q\leqslant2d$. For either conductance convention, it suffices to search for a graph on $2d$ vertices, allowing isolated ones; if a smaller $n$ is prescribed, search on $n$ vertices. This uses positivity of weights, which prevents cancellation of highest-grade forest contributions.

## A complete criterion for the weighted vertex polynomial

Here arbitrary positive real conductances are allowed, and the graph structure is not fixed in advance. We consider specifically **one-variable vertex normalization**, $P_G(t)=\det(I+t\mathbf L)$.

> [!info] A spectral realizability criterion
> **Theorem.** A nonconstant real polynomial is the vertex toponome of some simple undirected graph with positive conductances if and only if its constant term is one and all its roots are real and strictly negative. A degree-$d$ polynomial can be realized by a weighted complete graph on $d+1$ vertices.

> [!proof]- Proof through the inverse eigenvalue problem
> **Proof.** Necessity follows from the [[Forest Coefficients and the Laplacian Polynomial#Roots and factorization over the reals|spectral representation]]
>
> $$
> P_G(t)=\prod_{j=1}^d(1+\lambda_jt),\qquad\lambda_j>0
> $$
>
> Conversely, if the roots $t_j$ are negative and $P(0)=1$, set $\lambda_j=-1/t_j>0$. Then $P(t)=\prod_j(1+\lambda_jt)$, with multiplicities. By Theorem 2.5 of Fallat, Gupta, and Lin [3], any list $0,\lambda_1,\ldots,\lambda_d$ is the Laplacian spectrum of a complete graph on $d+1$ vertices with suitable positive conductances. Its determinant $\det(I+t\mathbf L)$ equals $P(t)$. $\square$

For a prescribed vertex count, the additional necessary and sufficient condition is $n\geqslant d+1$: extra vertices can be isolated. A connected realization requires $n=d+1$. The polynomial $P=1$ is realized by an edgeless graph.

**Why conductances matter.** The polynomial

$$
P(t)=(1+t)^2=1+2t+t^2
$$

is realized by a triangle with all three conductances equal to $1/3$: its Laplacian is $I_3-J_3/3$, where $J_3$ is the all-ones matrix, and its spectrum is $0,1,1$. An unweighted realization is impossible: $p_1=2$ would require exactly one edge, whose toponome has degree $1$.

This criterion does not extend to vector normalization, the coefficient triangle, or a prescribed graph structure.

## Status of the results and independent checks

The conditions on support, the highest column, nonisolated vertex count, first coefficients, and adjacent edge pairs have been proved directly. The exact system gives a necessary and sufficient criterion through existence of a solution. A short complete characterization of coefficient triangles by internal equalities and inequalities alone has not been established here.

Mason's theorem is used with references to its proofs [1, 2]; the spectral criterion is derived from the inverse-problem result [3]. The necessary tests presented are not claimed to be sufficient: $A_*$ shows the limitations of column-sum and irreducibility tests.

Forests were independently enumerated for all $1099$ simple labeled graphs on $1\leqslant n\leqslant5$ vertices. The unique highest cell, $N=d+q$, the formulas for edge pairs and triangles, and the double-counting and Mason inequalities were checked. The $596$ labeled three-edge graphs on $2\leqslant n\leqslant6$ vertices yielded five distinct coefficient tables; $A_*$ was absent. Six vertices suffice because three edges have at most six endpoints. These computations supplement the general proofs.

The spectral example with conductances $1/3$ was checked by direct forest enumeration with root weights and by independent determinant computation. The universal system on four vertices was compared with direct forest enumeration for all $64$ simple graphs on those vertices.

## Sources and connections

The question of graph realizability of toponomes and its presentation in PMG notation are based on the author's research. The general results on matroids and Laplacian spectra used here have the following accessible sources.

1. Nima Anari, Kuikui Liu, Shayan Oveis Gharan, Cynthia Vinzant. *Log-concave polynomials III: Mason's ultra-log-concavity conjecture for independent sets of matroids*. Proceedings of the American Mathematical Society **152** (2024), 1969–1981. [DOI: 10.1090/proc/16724](https://doi.org/10.1090/proc/16724). [Open preprint arXiv:1811.01600](https://arxiv.org/abs/1811.01600), 2018, Theorem 1.2; §2.1 defines matroids, and §5 gives the proof.
2. Petter Brändén, June Huh. *Lorentzian polynomials*. Annals of Mathematics **192** (2020), 821–891. [DOI: 10.4007/annals.2020.192.3.4](https://doi.org/10.4007/annals.2020.192.3.4). [Open text](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n3-p04-s.pdf), Theorem 4.14, p. 877: an independent proof of Mason's strong conjecture.
3. Shaun Fallat, Himanshu Gupta, Jephian C.-H. Lin. *Inverse eigenvalue problem for Laplacian matrices of a graph*. [Open preprint arXiv:2411.00292v2](https://arxiv.org/abs/2411.00292v2), 2024, Theorem 2.5: realization of any positive nonzero spectrum on a weighted complete graph.
4. [[Coefficient Tables of Toponomes]] — cell meanings, triangle orientation, and information loss under reduction.
5. [[Vector and Vertex Normalizations of Toponomes]] — normalizations and root weights.
6. [[Reducibility of Toponomes]] — factorization by components and irreducibility under the second-kind product.
7. [[Forest Coefficients and the Laplacian Polynomial]] — the vertex polynomial's relation to the determinant and spectrum.
