---
title: The Potential of Path-and-Cycle States
date: 2026-10-25
updated: 2026-10-25
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: path-and-cycle-state-potential
lang: en
order: 6
description: "A proof of the mixed-state potential formula, separate path and cycle multiplicities, arc labels, graph and construction-history counts, and the connection to Laguerre configurations."
---

The [[Cyclic Partitions and the Combinatorial Potential of the First Kind|potential of the first kind]] counts permutations of a prescribed cycle type. Intermediate states in the process of adding arcs also contain open paths. The author's research suggested the formula $u(\lambda_k)=k!/(f[m_j!]!)$ for these states. Here it receives a precise combinatorial definition and a proof.

The essential distinction concerns the labels: $u$ counts ways to arrange **distinct arcs** within components of prescribed types. Counting graphs on distinct vertices introduces an additional factor. This explains both the factorial of the arc count and the coefficients accompanying falling factorials.

## The state type and vertex count

Consider finite digraphs in which each vertex has indegree and outdegree at most $1$. Their components are directed cycles, directed paths, and isolated vertices. We follow the notation in [[Permutation Digraphs and Cycle Combinatorics#Open paths and marked components|the note on permutation digraphs]]:

- $j$ denotes a closed cycle with $j$ arcs and $j$ vertices;
- $\underline j$ denotes an open path with $j$ arcs and $j+1$ vertices.

This note allows loops, which are cycles of type $1$. For the loopless model, exclude these components.

**Definition.** The reduced type $\lambda_k$ contains only components with a positive number of arcs. Let $c_j$ count cycles of type $j$, and let $p_j$ count paths of type $\underline j$, where $j\geqslant1$. Then

$$
k=\sum_{j\geqslant1}j(c_j+p_j),\qquad
p=\sum_{j\geqslant1}p_j,\qquad
v=k+p
$$

Here $k$ is the arc count, $p$ the number of nonempty open paths, and $v$ the number of incident vertices. For example, $[3,\underline1]$ has $k=4$, $p=1$, and $v=5$.

Isolated vertices $\underline0$ are omitted from the reduced type. On a prescribed set of $n$ vertices, their count is recovered as $n-v$. Their multiplicity therefore does not enter the denominator in the formula for $u$. The empty type has $k=p=v=0$.

## The potential formula and its proof

**Definition.** The potential $u(\lambda_k)$ counts partitions of the arc-label set $\{1,\ldots,k\}$ into components of the prescribed type, with a cyclic order on each cycle and a linear order on each path. Components are unordered. A cycle has no distinguished initial position, but its direction is retained.

Equivalently, this counts graphs with no isolated vertices, distinctly labelled arcs, and unlabelled vertices, up to isomorphisms preserving directions and arc labels.

> [!info] The potential of a mixed state
> **Theorem.** For a reduced type $\lambda_k$,
>
> $$
> \boxed{
> u(\lambda_k)=
> \frac{k!}{\displaystyle\prod_{j\geqslant1}j^{c_j}c_j!p_j!}
> =\frac{k!}{\displaystyle f\prod_{j\geqslant1}c_j!p_j!},
> \qquad
> f=\prod_{j\geqslant1}j^{c_j}
> }
> \tag{1}
> $$
>
> Empty products and $u(\varnothing)$ equal $1$.

> [!note]- Proof
> **Proof.** First distribute the $k$ distinct labels among blocks: $c_j$ blocks of size $j$ are to become cycles, and $p_j$ blocks of that size are to become paths. Removing repetitions as in the [[Partitions and the Combinatorial Potential of the Second Kind|potential of the second kind]] gives
>
> $$
> \frac{k!}{\displaystyle\prod_{j\geqslant1}(j!)^{c_j+p_j}c_j!p_j!}
> $$
>
> Give each path block a linear order, with $j!$ choices. Give each cycle block a cyclic order, with $(j-1)!$ choices: the $j$ choices of initial position describe the same cycle. The number of objects is therefore
>
> $$
> \frac{k!\displaystyle\prod_{j\geqslant1}((j-1)!)^{c_j}(j!)^{p_j}}
> {\displaystyle\prod_{j\geqslant1}(j!)^{c_j+p_j}c_j!p_j!}
> =
> \frac{k!}{\displaystyle\prod_{j\geqslant1}j^{c_j}c_j!p_j!}
> $$
>
> The resulting structure uniquely specifies the typed partition and the orders within its blocks, so nothing is omitted or counted twice. $\square$

Thus the **cycle factor** arises only from closed components. A path has an initial vertex, so its linear orders are not divided by its length.

The multiplicities $c_j$ and $p_j$ must be treated separately. Interchanging two cycles of the same size changes nothing, as does interchanging two paths of the same size. Exchanging the labels assigned to a cycle block and a path block changes the object. The denominator therefore contains $c_j!p_j!$, not $(c_j+p_j)!$. In the original notation, $[m_j!]!$ means the product of factorials from both groups of multiplicities without adding them together.

When there are no paths, (1) agrees with the potential of the first kind. With paths present, it extends that potential to blocks of two kinds.

## Small examples

Labels in the table refer to arcs.

| Type $\lambda_k$ | $k$ | $f$ | $u(\lambda_k)$ |
| --- | ---: | ---: | ---: |
| $[1,1]$ | 2 | 1 | $2!/2!=1$ |
| $[1,\underline1]$ | 2 | 1 | $2!=2$ |
| $[2]$ | 2 | 2 | $2!/2=1$ |
| $[\underline2]$ | 2 | 1 | $2!=2$ |
| $[\underline1,\underline1]$ | 2 | 1 | $2!/2!=1$ |
| $[2,\underline1]$ | 3 | 2 | $3!/2=3$ |
| $[1,\underline2]$ | 3 | 1 | $3!=6$ |

For $[\underline2]$, the labels along the path may occur as $1,2$ or $2,1$. For $[2]$, these two sequences describe one cyclic order. For $[1,\underline1]$, choose which of the two labels goes to the loop and which goes to the open path.

![[Arc Labels in Paths and Cycles.svg]]

*Figure 1. Numbers beside arrows are arc labels; circles have no individual labels. Direction distinguishes the initial vertex of an open path, whereas a cycle has no distinguished initial position. A loop and an open arc are components of different kinds.*

## Graphs on prescribed vertices and construction histories

Now fix a set of $n$ distinct vertices. Let $N_n(\lambda_k)$ count graphs of reduced type $\lambda_k$, and let $H_n(\lambda_k)$ count sequences adding their $k$ arcs to the empty graph. The degree restrictions hold at every step, and arcs are not repeated.

Use the [[Falling Factorials, Rooted Forests, and Stirling Numbers|falling factorial]]

$$
n_{\underline v}=n(n-1)\cdots(n-v+1),\qquad n_{\underline0}=1
$$

For an integer $n\geqslant0$ and $v>n$, it is zero.

> [!info] Two counts for one type
> **Corollary.** With $v=k+p$,
>
> $$
> \boxed{
> N_n(\lambda_k)=\frac{u(\lambda_k)}{k!}\,n_{\underline{k+p}},
> \qquad
> H_n(\lambda_k)=u(\lambda_k)\,n_{\underline{k+p}}
> }
> \tag{2}
> $$

> [!note]- Proof
> **Proof.** Take an object counted by $u$: all its arcs are distinct, and it has no isolated vertices. It has no nontrivial automorphism preserving every arc label. The source and target of each labelled arc are fixed, and every vertex is incident to at least one arc.
>
> Assigning its $v$ vertices distinct labels from the prescribed $n$-element set therefore gives exactly $n_{\underline v}$ choices. This produces $u(\lambda_k)n_{\underline v}$ graphs with both vertex and arc labels. Each graph on labelled vertices has $k!$ arc labellings, proving the first formula.
>
> The arc labels $1,\ldots,k$ may be read as their order of addition. All $k!$ orders are admissible: every subgraph of the final state also has indegree and outdegree at most $1$. This proves the second formula. $\square$

Thus $u(\lambda_k)$ is precisely the **coefficient of the falling factorial** in the history count. The potential itself does not equal the number of graphs on $n$ vertices.

For example, for a path $[\underline2]$ on three prescribed vertices,

$$
u([\underline2])=2,\qquad
N_3([\underline2])=\frac{2}{2!}\,3_{\underline3}=6,\qquad
H_3([\underline2])=2\cdot3_{\underline3}=12
$$

The six graphs correspond to the six orders of the three vertices along the path. Each graph can be constructed in two orders of arc addition.

Formulas (1)-(2) remain valid in the loopless model for types with $c_1=0$. Probabilities under sequential random choice require a separately specified rule for choosing arcs; a potential alone does not determine that rule.

## The connection to Laguerre configurations

In the literature, digraphs with indegree and outdegree at most $1$ are called **Laguerre digraphs**. Their description as collections of paths and cycles appears in Foata and Strehl [1, §§2-3] and in the modern work of Deb, Dyachenko, Pétréolle, and Sokal [2, §1.2].

To relate this model to $u$, turn each labelled arc of the original state into a vertex of an auxiliary graph. Join two such vertices by an arc when the corresponding original arcs immediately follow one another along a path or cycle. A cycle of length $j$ remains a cycle on $j$ vertices; a path $\underline j$ becomes a path on $j$ vertices. A loop remains a loop, whereas $\underline1$ becomes an isolated vertex.

This is a bijection between objects counted by $u$ and Laguerre digraphs on $k$ labelled vertices with prescribed component sizes and kinds. The auxiliary graph's vertex count equals the original graph's **arc count**.

The correspondence gives a simple aggregate count. Let $\mathcal T_{k,p}$ contain the reduced types with $k$ arcs and $p$ open paths. Loops are allowed. Then

$$
\boxed{
\sum_{\lambda_k\in\mathcal T_{k,p}}u(\lambda_k)
=\frac{k!}{p!}\binom{k}{p},
\qquad 0\leqslant p\leqslant k
}
\tag{3}
$$

**Proof.** The auxiliary graph on $k$ vertices with $p$ paths has $k-p$ arcs. Choose their sources in $\binom{k}{p}$ ways, then choose an injection from those sources into the full vertex set in $k!/p!$ ways. The degree restrictions hold, and each graph is obtained uniquely. $\square$

This specializes the classical enumeration of Laguerre configurations; formula (1) refines it by the complete component type. The sources provide the model and aggregate formulas, while the proof for our fixed type is given above.

For $k=4$, the sums by number of open paths are:

| $p$ | 0 | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| $\sum_{\lambda_4\in\mathcal T_{4,p}}u(\lambda_4)$ | 24 | 96 | 72 | 16 | 1 |

The last case consists of four separate open arcs. For the loopless model, (3) must be modified because injections with fixed points are excluded.

Summing (2) over all types gives the identity

$$
\bigl(n_{\underline k}\bigr)^2
=\sum_{\lambda_k}u(\lambda_k)n_{\underline{k+p(\lambda_k)}}
=\sum_{p=0}^{k}\frac{k!}{p!}\binom{k}{p}n_{\underline{k+p}}
\tag{4}
$$

Indeed, a history of $k$ additions is specified by two ordered lists of distinct vertices: its sources and its receivers. Each list has $n_{\underline k}$ choices. On the right, the same histories are grouped first by complete type and then by path count. This identity allows loops.

## Status and sources

Formulas (1)-(4) are proved under the stated conventions. Independent enumeration of all partial injections on sets of up to seven labels produced 146048 auxiliary graphs and verified (1) for all 249 types across these set sizes. Separate checks covered 15126 original graphs on sets of up to six vertices, including 7512 loopless graphs, and direct enumeration of 1407 histories of all lengths on sets of up to four vertices. These checks supplement the proofs.

This note is based on the author's research within PMG. The formula conjectured there is now justified both as a potential of an arc-label partition and as a coefficient in the history count. It is a combinatorial cardinality, distinct from the potential of a form relative to a metric polyform. The general product of marked types, its properties, and a full algebra of states are not constructed here.

1. Foata D., Strehl V. [Combinatorics of Laguerre Polynomials](https://irma.math.unistra.fr/~foata/paper/pub47.pdf). In *Enumeration and Design*, 1984, pp. 123-140. §§2-3, Lemma 2.1 and Proposition 3.1: injections, paths, cycles, and the combinatorial model of Laguerre polynomials.
2. Deb B., Dyachenko A., Pétréolle M., Sokal A. [Lattice paths and branched continued fractions III. Generalizations of the Laguerre, rook and Lah polynomials](https://arxiv.org/html/2312.11081v1#S1.SS2). §1.2, equations (1.19)-(1.22): Laguerre digraphs and their enumeration.
