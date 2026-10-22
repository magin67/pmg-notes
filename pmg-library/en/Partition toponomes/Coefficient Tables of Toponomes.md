---
title: Coefficient Tables of Toponomes
date: 2026-10-22
updated: 2026-10-22
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: coefficient-tables-of-toponomes
lang: en
description: "Grouping types by weight and number of nontrivial components: admissible indices, triangular tables, multiplication, and limits on distinguishing graphs."
order: 6
---

In a [[From Polyforms to Partitions|partition toponome]], each type has its own coefficient. A further reduction groups types of equal weight with the same number of positive parts. The result is conveniently stored in a table with two indices.

Columns will be indexed by weight $k$, and rows by the number $r$ of nontrivial components. The rows narrow from top to bottom: each successive row loses one position at either end. In this arrangement, we call the table a **coefficient triangle**. The unit term $e$ is treated separately; zero cells in figures and tables are left blank.

## From types to two indices

Let $\mathcal E$ be a chosen representation of a polyform on a collection $A$, with $n=\#A$. Its toponome has the form

$$
T_{\mathcal E}=\sum_\lambda C_{\mathcal E}(\lambda)\,\lambda
$$

For a positive type $\lambda=(k_1,\ldots,k_r)$, set

$$
w(\lambda)=k_1+\cdots+k_r=k,
\qquad
r=\#\lambda
$$

The weight of the type equals the total grade, and the number of parts equals the number of nontrivial components. The empty type $1$ has $k=r=0$.

> [!info] Coefficient table
> **Definition.** The coefficient of a toponome at weight $k$ and number $r$ of positive parts is
>
> $$
> a_{k,r}(\mathcal E)=
> \sum_{\substack{\lambda:\,w(\lambda)=k\\\#\lambda=r}}
> C_{\mathcal E}(\lambda)
> $$
>
> These coefficients form the table $\mathcal A_{\mathcal E}=(a_{k,r}(\mathcal E))$.

Here $r$ does not replace the established notation $m$ for the **full** number of partition components. If $\ell$ components are singleton vertices, then

$$
m=r+\ell=n-k,
\qquad
\ell=n-k-r
$$

Thus, when $n$ is known, the indices $(k,r)$ recover $m$ and $\ell$. If the second index were the full number $m$ of components, it would already be determined by the grade for fixed $n$: $m=n-k$. The two-dimensional table arises from counting nontrivial components.

The reduction applies to the same chosen representation $\mathcal E$ as the original toponome. It does not by itself remove [[Toponomes and Structural Identities|representation dependence or incompatibility with some structural identities]].

For a finite simple undirected graph $G$, use the representation obtained by expanding the factors of the Laplacian exponential. Then

$$
a_{k,r}(G)=
\sum_{\substack{F\in\mathcal F(G)\\
\#E(F)=k,\ r(F)=r}}w(F),
\qquad
w(F)=\prod_{e\in E(F)}c_e
$$

Here $\mathcal F(G)$ is the set of spanning forests, $r(F)$ is the number of their nontrivial components, and $c_e$ is the edge weight. With unit weights, $a_{k,r}(G)$ counts forests with the specified parameters. With numerical weights, it is a sum of products of weights and therefore contains more than information about the unweighted structure. The empty forest gives $a_{0,0}(G)=1$.

## Example: a path on six vertices

Consider the unweighted path $P_6$ with five edges. Every subset of its edges forms a spanning forest when all six vertices are retained.

Four-edge forests are obtained by deleting one edge. Deleting either end edge leaves type $(4)$; deleting either of the next two edges gives $(3,1)$; deleting the middle edge gives $(2^2)$. Thus the weight-$4$ part of the toponome is

$$
T_{P_6}^{[4]}=2(4)+2(3,1)+(2^2)
$$

Passing to the table groups the last two types:

$$
a_{4,1}(P_6)=2,
\qquad
a_{4,2}(P_6)=2+1=3
$$

Arrange the coefficients in columns indexed by weight $k$ and rows indexed by the number $r$ of components, increasing from top to bottom. The result is the triangle

$$
\begin{array}{ccccc}
5&4&3&2&1\\
&6&6&3&\\
&&1&&
\end{array}
$$

The columns, from left to right, correspond to $k=1,\ldots,5$, and the rows, from top to bottom, to $r=1,2,3$. The unit term $e$ and zero cells are omitted.

The first row counts connected segments of $k$ edges: $5,4,3,2,1$. The second counts forests with two nontrivial components: for $k=2,3,4$, the values are $6,6,3$. The third row contains the unique matching of three edges.

Each column sums to $\binom5k$, since $k$ edges are chosen from five. The displayed coefficients sum to $31$; including the unit term gives $2^5=32$.

The table retains the number of forests with $k$ edges and $r$ nontrivial components. It no longer records how the weight $k$ is distributed among those components: the value $3$ at $k=4$, $r=2$ does not recover the separate coefficients of $(3,1)$ and $(2^2)$.

## Why the shape is triangular

Each of the $r$ nontrivial components contains at least one edge, so the total grade $k$ is at least $r$. A component of grade $k_i$ occupies $k_i+1$ vertices, and all nontrivial components together occupy $k+r$ vertices. Hence

$$
r\le k,
\qquad
k+r\le n
$$

The admissible columns in row $r$ are therefore

$$
k=r,r+1,\ldots,n-r
$$

The number of positions in this row is

$$
(n-r)-r+1=n-2r+1
$$

**Passing to the next row removes one position at each end.** The left boundary moves from $k=r$ to $k=r+1$, and the right boundary from $k=n-r$ to $k=n-r-1$. The rows thus narrow successively to form a triangle.

For $n=6$:

| Row $r$ | Admissible columns $k$ | Number of positions |
| ---: | --- | ---: |
| $1$ | $1,2,3,4,5$ | $5$ |
| $2$ | $2,3,4$ | $3$ |
| $3$ | $3$ | $1$ |

For arbitrary $n$, there are at most $\lfloor n/2\rfloor$ rows. The last admissible row has one position when $n$ is even and two when $n$ is odd.

These bounds concern possible types: for every admissible pair $(k,r)$, take the type $(k-r+1,1^{r-1})$ and add $n-k-r$ singleton vertices. For a particular graph, some coefficients inside the triangle may be zero. For example, every nonempty edge subset of a star has one nontrivial component, so only the first row is filled:

$$
a_{k,1}(K_{1,n-1})=\binom{n-1}{k},
\qquad 1\le k\le n-1
$$

Zero cells are left blank, preserving the column positions of the other coefficients. Entirely zero rows may be omitted.

## Multiplication of tables

Grouping by $(k,r)$ is compatible with the product in [[The Second-Kind Algebra on Partitions|the second-kind algebra on partitions]], provided that the tables use the induced product.

Let $u_{k,r}$ denote the formal table with a one in cell $(k,r)$ and zeros elsewhere. Reduction of a type is given by the linear map

$$
\rho(\lambda)=u_{w(\lambda),\#\lambda}
$$

**Proposition.** The rule

$$
u_{k,r}*u_{l,s}=
\sum_{h=0}^{\min(r,s)}
\binom rh\binom sh h!\,
u_{k+l,r+s-h}
$$

defines a product for which

$$
\rho(\lambda*\mu)=\rho(\lambda)*\rho(\mu)
$$

The unit is $u_{0,0}$. Here, tables are considered without fixing a common $n$: multiplication may increase the number of vertices required.

> [!note]- Proof
> **Proof.** Suppose $\lambda$ has $r$ parts and $\mu$ has $s$. A partial matching of size $h$ can be chosen in $\binom rh\binom sh h!$ ways: choose $h$ parts in each factor and a bijection between them. After the matched parts merge, the weight is $k+l$ and the number of parts is $r+s-h$. These parameters do not depend on the individual part sizes, so all matchings of size $h$ give the same table cell. Bilinear extension proves compatibility of the reduction with multiplication. Associativity and commutativity are inherited from the partition algebra. $\square$

For example, the expansion

$$
(1^2)*(1^2)=(1^4)+4(2,1^2)+2(2^2)
$$

becomes

$$
u_{2,2}*u_{2,2}=u_{4,4}+4u_{4,3}+2u_{4,2}
$$

This product enumerates partial matchings of components. As explained in the [[Partition Products and Boundary Forms|boundary interpretation]], it does not determine the ordinary product of two particular polyforms without data on their shared vertices.

A different rule applies to disjoint union of graphs: a forest is chosen independently in each graph, and components from the two graphs do not merge. Hence

$$
a_{k,r}(G\sqcup H)=
\sum_{\substack{i+j=k\\p+q=r}}
a_{i,p}(G)\,a_{j,q}(H)
$$

This is ordinary convolution in two indices. It should be distinguished from the product $*$, which sums over matchings.

## What information is retained

For the graph representation, the table is invariant under vertex relabeling. With fixed weights, relabeling must also carry the edge weights. The table determines:

- the total weight of all spanning forests of each grade: $\sum_r a_{k,r}(G)$;
- their distribution by the number of nontrivial components;
- when $n$ is known, their distribution by the full number of components $m=n-k$ and the number of singleton vertices $\ell=n-k-r$;
- for a simple unweighted graph, the number of edges $a_{1,1}(G)$, the numbers of $k$-edge matchings $a_{k,k}(G)$, and the number of spanning trees $a_{n-1,1}(G)$ for $n\ge2$.

The last formulas follow from the definitions: when $r=k$, all positive parts equal $1$; when $k=n-1$ and $r=1$, the single component contains every vertex. In a graph with positive weights, the absence of spanning trees means that the graph is disconnected. If signed weights are allowed, contributions may cancel, so a zero coefficient no longer implies disconnection.

The size $n$ of the original collection must be retained separately. Adding an isolated vertex changes neither the positive types of forests nor the coefficients $a_{k,r}$. Thus graph comparisons use the data $(n,\mathcal A_G)$.

The table does not retain vertex labels, individual forests, or the distribution of coefficients among types with the same $(k,r)$. This last loss of information is additional to the losses incurred when passing from the graph representation to the toponome.

## Does the table distinguish all graphs?

Consider the precise question: do $n$ and all the numbers $a_{k,r}(G)$ determine an unweighted simple graph up to isomorphism?

**In general, the answer is no, even for trees.** The following two edge sets define trees on the same set $A=\{a,b,c,d,e,f,g,h,i,j\}$:

$$
E(T_1)=\{ab,ac,ad,be,bf,cg,dh,gi,ij\}
$$

$$
E(T_2)=\{ab,ac,ad,be,bf,cg,eh,gi,hj\}
$$

![Two trees on ten vertices with the same coefficient table: the branches at their adjacent degree-three vertices have lengths 4,2 and 1,1 in the first tree, and 3,1 and 3,1 in the second](Trees%20with%20the%20same%20coefficient%20table.svg)

*Figure 1. In both trees, vertices $a$ and $b$ have degree $3$ and are joined by an edge. In $T_1$, the two additional branches at $a$ have lengths $4$ and $2$, and those at $b$ have lengths $1$ and $1$. In $T_2$, the branch lengths at each of these vertices are $3$ and $1$.*

The trees have diameters $6$ and $7$, respectively, so they are nonisomorphic. Their tables nevertheless agree:

| $r\backslash k$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $1$ | 9 | 10 | 12 | 14 | 14 | 12 | 8 | 4 | 1 |
| $2$ | | 26 | 44 | 53 | 52 | 38 | 20 | 5 | |
| $3$ | | | 28 | 50 | 48 | 30 | 8 | | |
| $4$ | | | | 9 | 12 | 4 | | | |

**Checking the example.** All $2^9=512$ edge subsets were enumerated for each tree. For each subset, connected components were found on the full set of ten vertices; the number of edges gives $k$, and the number of components of size at least two gives $r$. Counting these pairs produces the displayed table. The column sums are $\binom9k$. The displayed coefficients sum to $511$, or $512$ including the unit term. This is a finite computational verification of a particular counterexample.

The full toponomes of these trees differ. In particular,

$$
c_{T_1}((4^2))=0,
\qquad
c_{T_2}((4^2))=1
$$

In $T_2$, deleting edge $ab$ gives two components of five vertices each. No edge deletion in $T_1$ splits it in this way. Under grouping, both contributions enter the common cell $(8,2)$ along with other types, and the distinction disappears.

### Connection with a known graph polynomial

Martin Trinks [1] studies the *covered components polynomial*, which enumerates spanning subgraphs by their number of edges, full number of components, and number of nontrivial components. For a tree $T$, every such subgraph is a forest, and the full number of components is $n-k$. Thus, in the notation of this note,

$$
C(T;x,y,z)=\sum_{k,r}a_{k,r}(T)x^{n-k}y^kz^r
$$

When $n$ is known, this polynomial and the table of a tree contain the same data. A pair of nonisomorphic trees on ten vertices not distinguished by this polynomial already appears in [1, Remark 33 and Figure 2]. For a general graph, the polynomial $C$ also includes cyclic subgraphs; our table is extracted only from its forest terms, which satisfy $m+k=n$.

This correspondence with the literature helps establish the limits of the invariant. It does not turn the coefficient table into an operator spectrum or a full diagonalization of a polyform. Comparison with characteristic polynomials and other graph invariants requires separate treatment.

## Further directions

The table lies between the record of all types and coarser sums of coefficients. It can be stored as an array or encoded as a polynomial; changing the notation does not recover the lost types.

The [[Карта библиотеки PMG|PMG library map (in Russian)]] records future work on graph classes distinguished by such tables and on richer data: retaining individual types, adding component weights, and considering rooted variants. The distinguishing power of each specific construction must be checked separately. The counterexample above concerns the table $a_{k,r}$ and does not refute possible statements about more detailed invariants.

## Source

1. Martin Trinks. *The covered components polynomial: A new representation of the edge elimination polynomial*. [arXiv:1103.2218](https://arxiv.org/abs/1103.2218). Definition 3; Remark 33 and Figure 2; Section 10.
