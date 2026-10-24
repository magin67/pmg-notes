---
title: Balanced Graphs and Spanning-Tree Potentials
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: balanced-graphs-spanning-tree-potentials
lang: en
description: Balance, directed-cycle decompositions, equality of rooted spanning-tree potentials, and the bilinear boundary representation of the Laplacian.
order: 1
source_revision: 6
---

In an undirected graph, symmetric couplings make all principal Laplacian minors of order $n-1$ equal. Their common value is the spanning-tree coefficient. This property extends to directed graphs: it is enough for the total incoming weight at each vertex to equal its total outgoing weight. We call these **balanced graphs**.

This note opens the balanced-graph series. Its main result is that, for a connected graph with nonnegative weights, balance is equivalent to all rooted spanning-tree potentials having the same positive value. The final section shows how balance expresses the Laplacian through bilinear forms on affine vectors, connecting these graphs to PMG algebra.

## From symmetric couplings to vertex balance

An undirected edge of weight $c$ can be replaced by two opposite arcs of the same weight. At either endpoint, its incoming and outgoing contributions both equal $c$. Every symmetric graph is therefore balanced at each vertex.

The converse fails. Consider the unit-weight directed triangle:

$$
a\longrightarrow b\longrightarrow c\longrightarrow a
$$

![[The Unit Directed 3-Cycle.svg]]

*A unit directed 3-cycle. Each vertex has one incoming and one outgoing arc of weight $1$. There are no reverse arcs: balance holds without symmetric couplings.*

A **directed $k$-cycle** visits $k$ distinct vertices in succession and returns to its starting vertex. As a weighted component of a balanced graph, it has the same weight on every arc.

Balance compares the incoming and outgoing weights at one vertex. It does not require different vertices to have equal total weights. For example, in a symmetric unit-weight path, both totals are $1$ at the endpoints and $2$ at internal vertices.

## Definition and Laplacian matrix

Consider a finite directed graph on $a_1,\ldots,a_n$, with $n\ge2$, without loops. The weight of $i\to j$ is $f_{ij}\ge0$; an absent arc has $f_{ij}=0$, and $f_{ii}=0$. Parallel arcs are represented by their total weight.

The outgoing and incoming weights are

$$
d_i^{\mathrm{out}}=\sum_j f_{ij},\qquad
d_i^{\mathrm{in}}=\sum_j f_{ji}
$$

> [!info] Balanced graph
> **Definition.** A graph is balanced if every vertex satisfies
>
> $$
> d_i^{\mathrm{out}}=d_i^{\mathrm{in}}
> $$

Here connectedness means connectedness of the positive-arc graph after forgetting directions. **Strong connectedness** means that every vertex is reachable from every other vertex by a directed path. Balance itself does not require connectedness.

Fix the convention that the first index of $f_{ij}$ is the source. Set $\mathbf F=(f_{ij})$ and define the Laplacian using outgoing weights:

$$
\mathbf L=\operatorname{diag}(d_1^{\mathrm{out}},\ldots,d_n^{\mathrm{out}})-\mathbf F
$$

Entries of $\mathbf L$ are written in ordinary type:

$$
L_{ii}=d_i^{\mathrm{out}},\qquad
L_{ij}=-f_{ij}\quad(i\ne j)
$$

When $f_{ij}=f_{ji}$, this is the usual Laplacian from [[Laplacian - graph, electrical network and quadratic form]]. In general it may be nonsymmetric.

Let $\mathbf1$ be the column of $n$ ones. Laplacian row sums always vanish; the sum of column $j$ is $d_j^{\mathrm{out}}-d_j^{\mathrm{in}}$. Thus

$$
\mathbf L\mathbf1=0,\qquad
\boxed{G\text{ is balanced}\ \Longleftrightarrow\ \mathbf1^{\mathsf T}\mathbf L=0}
$$

A balanced graph has zero sums on both sides of its Laplacian. This condition is weaker than symmetry $\mathbf L=\mathbf L^{\mathsf T}$.

## Decomposition into directed cycles

The sum of weighted graphs on a fixed vertex set adds the weights of corresponding arcs. Balance is preserved by addition and by multiplying all weights by a nonnegative scalar.

> [!info] Cycle decomposition
> **Theorem.** A graph with nonnegative weights is balanced if and only if its weights are a finite nonnegative combination of directed-cycle weights:
>
> $$
> \mathbf F=\sum_{s=1}^m t_s\mathbf F_{C_s},\qquad t_s>0
> $$
>
> Here $\mathbf F_{C_s}$ has ones on the arcs of $C_s$ and zeros elsewhere. The zero graph corresponds to the empty sum. The decomposition need not be unique.

> [!note]- Proof of cycle decomposition
> **Proof.** Each weighted directed cycle is balanced, so their sum is balanced.
>
> Conversely, start along a positive-weight arc of a nonzero balanced graph. At each reached vertex, a positive incoming weight ensures a positive outgoing weight, so the walk can continue. Finiteness forces a repeated vertex; the segment ending at the first repetition is a directed cycle.
>
> Subtract the smallest arc weight $t>0$ on this cycle from all its arcs. The remainder is nonnegative and balanced: at each cycle vertex, incoming and outgoing totals decrease by the same amount. At least one positive arc disappears.
>
> Repeating this procedure takes at most as many steps as there were initially positive arcs. The recorded weighted cycles give the required sum. $\square$

This is a special case of flow decomposition into paths and cycles; zero imbalance at every vertex leaves only cycles [1].

### Symmetric graphs as 2-balanced graphs

A directed 2-cycle consists of two opposite arcs between one pair of vertices. Consequently, a graph admits a decomposition entirely into directed 2-cycles exactly when $f_{ij}=f_{ji}$ for every pair. We may call these **2-balanced graphs**. The number $2$ refers to cycle lengths in a decomposition, not to vertex degrees. A regular balanced graph of degree $2$ instead has two incoming and two outgoing arcs at every vertex; see [[Permutation Digraphs and Cycle Combinatorics#Regular balanced graphs and permutation decompositions]].

The condition concerns the existence of a decomposition, not the lengths of all cycles contained in the graph. A symmetric unit triangle, for example, can be obtained either

- from three directed 2-cycles on $ab$, $bc$, and $ca$;
- from $a\to b\to c\to a$ and its reverse $a\to c\to b\to a$.

Both decompositions give the same weight matrix. Balance alone does not select a canonical one. These are nonnegative decompositions of arc weights; identities between skew-symmetric circulation forms are a separate algebraic construction.

### Degree-one balanced graphs and permutations

Consider balanced graphs in which exactly one arc enters and one arc leaves each vertex, with every weight equal to $1$. Degree one here counts arcs, rather than merely their total weight.

The unique recipient of an arc from $a_i$ defines a permutation $\sigma$ by $a_i\to a_{\sigma(i)}$. Uniqueness of incoming arcs ensures bijectivity. Excluding loops means $\sigma(i)\ne i$ for every $i$, so this is a derangement [3].

Such a graph decomposes uniquely into vertex-disjoint directed cycles. Following the unique outgoing arc reaches a cycle, and indegree $1$ excludes any attached incoming path. All cycle lengths are at least $2$. On five vertices, for example, there may be separate cycles $a\to b\to a$ and $c\to d\to e\to c$.

![[A Loopless Permutation Digraph.svg]]

*A degree-one balanced graph on five vertices: a directed 2-cycle and a directed 3-cycle, all weights $1$. Each vertex belongs to exactly one cycle. The graph is balanced although it has two connected components.*

In Secret Santa, this graph describes an assignment in which everyone gives and receives exactly one gift, with self-gifts excluded. Recipients must be assigned without repetition; independent choices from the full list do not ensure this. Counts by cycle type, mean cycle counts, and intermediate states containing open paths are discussed in [[Permutation Digraphs and Cycle Combinatorics]]. An exchange of recipients appears in [[Balanced Variations#Reassigning two couplings|the note on balanced variations]].

### Connectedness of a balanced graph

> [!info] From connectedness to strong connectedness
> **Lemma.** A connected balanced graph with nonnegative weights is strongly connected.

> [!note]- Proof
> **Proof.** Fix a vertex and let $S$ contain all vertices reachable from it. No positive arc leaves $S$, since its endpoint would also be reachable.
>
> Summing balance over $S$ cancels the internal arcs and gives
>
> $$
> \sum_{i\in S,\ j\notin S} f_{ij}
> =\sum_{i\notin S,\ j\in S} f_{ij}
> $$
>
> The left side is zero. Nonnegative weights imply that no positive arc enters $S$ either. Connectedness therefore forces $S=\{1,\ldots,n\}$. The starting vertex was arbitrary. $\square$

## The spanning-tree potential of a vertex

Delete row and column $r$ from $\mathbf L$, denoting the resulting matrix by $\mathbf L_{\widehat r,\widehat r}$.

> [!info] Spanning-tree potential
> **Definition.** The spanning-tree potential of vertex $r$ is
>
> $$
> \tau_r=\det\mathbf L_{\widehat r,\widehat r}
> $$

This definition applies to a directed graph before balance is assumed. The term denotes this particular minor. It is neither an electrical potential nor a replacement for the polyform potential $u_M(f)$ in [[Laplacian Exponential#The potential of a form|the Laplacian exponential note]].

**Definition.** A directed spanning tree **toward root $r$** includes every vertex and has a unique directed path from each vertex to $r$. Each nonroot vertex has one outgoing tree arc, and the root has none. Its weight is

$$
\operatorname{wt}(T)=\prod_{(i\to j)\in T}f_{ij}
$$

> [!info] Directed matrix-tree theorem
> **Theorem.** With the chosen Laplacian convention, the spanning-tree potential is the sum of weights of directed spanning trees toward the specified root:
>
> $$
> \tau_r=\sum_{T\text{ toward root }r}\operatorname{wt}(T)
> $$
>
> If there are no such trees, the sum is zero. Balance is not required.

Directed and weighted versions of the matrix-tree theorem appear, for example, in [2]. For completeness, we prove it directly from the Laplacian definition.

> [!note]- Proof by multilinearity of the determinant
> **Proof.** Let $\mathbf e_i^{\mathsf T}$ denote coordinate row $i$. Row $i\ne r$ of the reduced Laplacian is the sum of rows $f_{ij}(\mathbf e_i^{\mathsf T}-\mathbf e_j^{\mathsf T})$, with coordinate $r$ deleted.
>
> Multilinearity selects one arc $i\to j$ from each $i\ne r$. Each term is the product of the selected $f_{ij}$ multiplied by the determinant of the selected row differences.
>
> If these arcs contain a directed cycle, the corresponding rows sum to zero, so their determinant vanishes. Otherwise every walk ends at $r$, the only vertex without a selected outgoing arc. The selected arcs form a spanning tree toward $r$.
>
> Order nonroot vertices by increasing distance to the root along this tree. Applying the same permutation to rows and columns preserves the determinant. The matrix becomes lower triangular with diagonal entries $1$: any entry $-1$ lies in the column of a vertex closer to the root. Its determinant is $1$.
>
> Exactly the weights of spanning trees toward $r$ remain. $\square$

In particular, $\tau_r\ge0$. In a strongly connected graph, $\tau_r>0$ for every $r$: choose, from each nonroot vertex, the first step of a shortest directed path to $r$.

## A balance criterion using spanning-tree potentials

> [!info] Equality of potentials
> **Theorem.** Suppose a graph with nonnegative weights is connected after forgetting directions. Then
>
> $$
> \boxed{G\text{ is balanced}
> \quad\Longleftrightarrow\quad
> \tau_1=\cdots=\tau_n=\tau>0}
> $$

The proof uses the adjugate $\operatorname{adj}\mathbf L$, the transpose of the cofactor matrix. Its diagonal entries are $\tau_i$.

> [!note]- Proof of the criterion
> **Proof.** First suppose $\operatorname{rank}\mathbf L=n-1$. Since $\mathbf L\mathbf1=0$, its kernel is $\operatorname{span}\{\mathbf1\}$. The identity
>
> $$
> \mathbf L\operatorname{adj}\mathbf L
> =\operatorname{adj}\mathbf L\,\mathbf L=0
> $$
>
> shows that each adjugate column is constant. Its diagonal entry determines that value, so with $\boldsymbol\tau=(\tau_1,\ldots,\tau_n)^{\mathsf T}$,
>
> $$
> \operatorname{adj}\mathbf L=\mathbf1\boldsymbol\tau^{\mathsf T},\qquad
> \boldsymbol\tau^{\mathsf T}\mathbf L=0
> $$
>
> If the graph is connected and balanced, the lemma makes it strongly connected. The matrix-tree theorem gives $\tau_i>0$, hence $\operatorname{rank}\mathbf L=n-1$. Balance gives $\mathbf1^{\mathsf T}\mathbf L=0$. The left kernel is one-dimensional, so $\boldsymbol\tau$ is proportional to $\mathbf1$: all potentials have the same positive value.
>
> Conversely, suppose $\tau_i=\tau>0$ for all $i$. A nonzero minor of order $n-1$, together with $\mathbf L\mathbf1=0$, gives rank $n-1$. The preceding identity becomes
>
> $$
> 0=\boldsymbol\tau^{\mathsf T}\mathbf L
> =\tau\mathbf1^{\mathsf T}\mathbf L
> $$
>
> Dividing by $\tau\ne0$ gives zero column sums, hence balance. $\square$

**Definition.** The common value $\tau$ is the **spanning-tree coefficient of a connected balanced graph**. With unit weights, it counts directed spanning trees toward any fixed root. Counting trees with every possible root instead gives $n\tau$.

In a symmetric graph, each undirected spanning tree has exactly one orientation toward a chosen root, with the same product of weights. The coefficient therefore agrees with the undirected spanning-tree coefficient already used in PMG.

Equality of these potentials does not assert that vertices are interchangeable under automorphisms or have equal degrees. It concerns the total weights of trees with different roots.

### Why positivity matters

Consider two unit arcs $a\to b$ and $a\to c$. The graph is connected after forgetting directions but is not balanced. Its Laplacian is

$$
\mathbf L=
\begin{pmatrix}
2&-1&-1\\
0&0&0\\
0&0&0
\end{pmatrix}
$$

All three principal minors of order $2$ vanish: there is no spanning tree toward one root. Thus $\tau_1=\cdots=\tau_n=0$ does not imply balance.

A disconnected balanced graph also has zero global potentials. A positive spanning-tree coefficient is defined separately for each connected component with at least two vertices. For an isolated vertex, the usual convention assigns weight $1$ to its empty tree.

## A triangle with both cycle directions

On $a,b,c$, take the cycle $a\to b\to c\to a$ with weight $p$ and its reverse with weight $q$, where $p,q\ge0$ and $p+q>0$. At every vertex, the incoming and outgoing weights are $p+q$. In the order $a,b,c$, the Laplacian is

$$
\mathbf L=
\begin{pmatrix}
p+q&-p&-q\\
-q&p+q&-p\\
-p&-q&p+q
\end{pmatrix}
$$

Every principal minor of order $2$ equals

$$
\tau=(p+q)^2-pq=p^2+pq+q^2
$$

An independent check lists the trees toward $a$:

| Tree arcs | Weight |
| --- | --- |
| $b\to c$, $c\to a$ | $p^2$ |
| $b\to a$, $c\to a$ | $pq$ |
| $c\to b$, $b\to a$ | $q^2$ |

The fourth possible choice of outgoing arcs from $b$ and $c$ produces the directed 2-cycle $b\to c\to b$, leaving $a$ unreachable. It contributes no tree. Cyclically relabelling the vertices gives the same three weights for the other roots.

### The unit directed 3-cycle

Setting $p=1$, $q=0$ recovers the initial example:

$$
\mathbf L=
\begin{pmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{pmatrix},\qquad
\tau_a=\tau_b=\tau_c=1
$$

![[Spanning Trees of a Directed 3-Cycle.svg]]

*The three root choices for a unit directed 3-cycle. Root $a$ retains $b\to c\to a$, root $b$ retains $c\to a\to b$, and root $c$ retains $a\to b\to c$. In each case the root's outgoing arc is removed. All remaining arcs point toward the highlighted root.*

Exactly one spanning tree of weight $1$ leads to each root. The common spanning-tree coefficient is $1$, although counting all three roots gives three trees.

### The unit symmetric triangle

When $p=q=1$, every pair has two opposite unit arcs. This is the symmetric triangle, with

$$
\mathbf L=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix},\qquad
\tau=1+1+1=3
$$

The three trees toward a fixed root correspond to its three undirected spanning trees. The single formula $p^2+pq+q^2$ covers both directed and symmetric cases.

## Balance and forms on boundaries

Use the formal bilinear forms of [[Basic Objects and Operations of Polyform Algebra#Forms: bilinearity and basic operations|polyform algebra]]. Exchanging arguments requires explicit transposition; $[X,Y]=[Y,X]$ is not part of the definition.

The polyform representation of the Laplacian matrix is

$$
L=\sum_{i,j}L_{ij}[a_i,a_j]
$$

> [!info] Bilinear representation on affine vectors
> **Proposition.** For a balanced graph and any point $h$ of unit affine weight,
>
> $$
> \boxed{L=\sum_{i,j}L_{ij}[a_i-h,a_j-h]}
> $$
>
> Both arguments of every term belong to the affine-vector space $W=\ker\varepsilon$.

> [!note]- Proof
> **Proof.** Expand $[a_i-h,a_j-h]$ by bilinearity. In addition to $[a_i,a_j]$, this gives $-[a_i,h]$, $-[h,a_j]$, and $[h,h]$. Summing with coefficients $L_{ij}$ cancels these extra terms because row and column sums vanish. Differences of points have affine weight $0$, hence belong to $W$. $\square$

Affine vectors are boundaries of grade $1$. The balanced Laplacian therefore lies in the same boundary-form subalgebra used in PMG, although individual forms may now have different arguments. This algebraic consequence of balance does not require symmetry.

Conversely, the coefficient matrix of any $[u,v]$ with $u,v\in W$ has zero row and column sums: its entries are $u_i v_j$, and both coordinate sums vanish. Representability by bilinear forms on affine vectors expresses precisely these two linear conditions. A balanced-graph Laplacian with nonnegative weights must additionally satisfy $L_{ij}\le0$ for $i\ne j$; an arbitrary bilinear sum need not meet this sign condition.

The centroid choice, arc and vertex representations, reduction of the term count using a reference vertex, and multiplication rules are discussed in [[The Bilinear Laplacian of a Balanced Graph]].

## Sources and connections

1. MIT OpenCourseWare. *15.082J Network Optimization*, 2010. [Transformations and flow decomposition](https://ocw.mit.edu/courses/15-082j-network-optimization-fall-2010/0911d1fe02b68af5127a53657f25b5a8_MIT15_082JF10_lec04.pdf). Nonnegative flow decomposition into paths and cycles; a circulation needs only cycles.
2. A. Postnikov, notes by A. Lin. *18.212 Algebraic Combinatorics*, 2019. [Lecture 29: Proof of Directed Matrix Tree Theorem based on induction](https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/4b3d3325c633bfb7fdea92ab6d6f6d1e_MIT18_212S19_lec29.pdf). The directed matrix-tree theorem and its weighted formulation.
3. NIST Digital Library of Mathematical Functions. [§26.13: Permutations: Cycle Notation](https://dlmf.nist.gov/26.13). Disjoint cycle decomposition and derangements.

Conventions for affine vectors and forms: [[Core specification]] and [[PMG terminology]]. The relation between the Laplacian exponential and the spanning-tree coefficient in the symmetric case: [[Laplacian Exponential]].
