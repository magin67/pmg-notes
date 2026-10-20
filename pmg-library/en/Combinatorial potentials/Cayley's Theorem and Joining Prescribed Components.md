---
title: Cayley's Theorem and Joining Prescribed Components
date: 2026-10-20
updated: 2026-10-20
revision: 1
source_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: cayleys-formula-and-connecting-given-components
lang: en
description: "Completing a prescribed forest to a tree: the Cayley-Moon formula, eight explicit completions, types of added edges, and contraction to a weighted graph."
order: 3
---

In [[Partitions and the Combinatorial Potential of the Second Kind|the note on partitions]], we counted ways to distribute elements among blocks of prescribed sizes. In [[Combinatorial Potentials in Symmetric Polyforms|the application of potentials to SPFs]], we then chose trees within those blocks. Now the trees have already been chosen: a particular forest is given. How many ways are there to join its components into one tree?

The answer depends only on the component sizes. The internal structure of each prescribed tree does not affect the number of completions. This generalisation of Cayley's formula is known as Moon's formula; a proof is given in [1, Lemma 3].

## What is given and what we count

Let $F$ be a fixed forest on $n$ labelled vertices, and let $B_1,\ldots,B_m$ be the vertex sets of its components. Isolated vertices also count as components. Write

$$
x_i=\#B_i,\qquad
\mathbf x=[x_1,\ldots,x_m],\qquad
\#\mathbf x=m,\qquad w(\mathbf x)=n
$$

Here $x_i\geqslant1$, and $m$ is the total number of components. The sizes form an unordered numerical collection retaining repetitions, as in the [[Partitions and the Combinatorial Potential of the Second Kind#Numerical collections|collection notation]].

All edges of $F$ are retained. Any edge of the complete graph $K_n$ may be drawn between vertices in different components. We seek an **unordered set of $m-1$ new edges** whose addition produces a tree on all $n$ vertices. The order of adding edges is irrelevant.

Denote the number of completions by $T(\mathbf x)$. The proof will establish that this count is independent of the shapes of the original trees. For example, a path and a star on four vertices allow the same number of completions when the remaining components are the same.

**Remark.** If an original block contains a cycle, retaining all its edges cannot produce a tree. One can separately count minimal connections between arbitrary connected blocks, but then it is the graph of connections between blocks that is a tree. Here $F$ is a forest, so the resulting graph itself is a tree.

## Eight ways to join three components

Take four vertices $a,b,c,d$. The edge $ab$ is prescribed, while $c$ and $d$ are isolated. The component sizes are $[2,1,1]$. Two new edges are needed to obtain a tree.

![Eight ways to complete the prescribed edge ab and isolated vertices c and d to a tree](Eight%20Completions%20of%20Three%20Components.svg)

*Figure 1. The prescribed edge $ab$ is blue; new edges are black. In the upper group the new edges are disjoint, with positive type $[1,1]$. In the lower group they share a vertex, giving type $[2]$. A crossing without a marked vertex does not create a connection. Adapted from the author's research materials.*

The upper two cases have new edge sets

$$
\{ac,bd\},\qquad \{ad,bc\}
$$

The remaining six are

$$
\begin{aligned}
&\{ac,ad\},\qquad \{ac,cd\},\qquad \{ad,cd\}\\
&\{bc,bd\},\qquad \{bc,cd\},\qquad \{bd,cd\}
\end{aligned}
$$

The list is easily checked for completeness. Five new edges are available: $ac,ad,bc,bd,cd$. Of their ten pairs, two are invalid: $\{ac,bc\}$ closes the cycle $abc$, and $\{ad,bd\}$ closes $abd$. Thus

$$
T([2,1,1])=\binom52-2=8
$$

Three different types occur in this example:

| Object | Type |
| --- | --- |
| Component sizes of the original forest | $[2,1,1]$ |
| Positive component grades of the new edges | $[2]$ or $[1,1]$ |
| Positive type of the resulting tree | $[3]$ |

Both types of new edges produce a connected tree because $ab$ is already present. Zero parts have been omitted from the new-edge types: two adjacent edges on the four original vertices have full type $[2,0]$.

## The general formula for joining components

**Theorem (Cayley-Moon formula).** For a fixed forest with component-size collection $\mathbf x$, where $\#\mathbf x=m$ and $w(\mathbf x)=n\geqslant1$, the number of completions to a tree of the complete graph is

$$
\boxed{
T(\mathbf x)=\mathbf x!\,n^{m-2}
=\mathbf x!\,w(\mathbf x)^{\#\mathbf x-2}
}
$$

Here $\mathbf x!=[x_i]!$ is the product of the component sizes. This is the [[Partitions and the Combinatorial Potential of the Second Kind#The product of a collection|collection product notation]]; the factorial of a scalar retains its usual meaning.

For the proof, first consider trees on the components themselves. Temporarily number them from $1$ to $m$, and let $\mathcal T_m$ be the set of all trees on these labels. For $S\in\mathcal T_m$, let $d_i(S)$ be the degree of vertex $i$ in $S$.

**Lemma (weighted Cayley formula).** For $m\geqslant2$,

$$
\sum_{S\in\mathcal T_m}[x_i^{d_i(S)}]!
=\mathbf x!\,w(\mathbf x)^{m-2}
$$

The exponents in $[x_i^{d_i(S)}]$ are ordinary numerical powers. The index $i$ ranges over all $m$ components.

> [!proof]- Proof of the weighted formula by the Prüfer code
> **Proof.** A tree on labels $1,\ldots,m$ corresponds to a Prüfer code of $m-2$ labels. Construct the code by repeatedly deleting the least-labelled leaf and recording its neighbour until two vertices remain.
>
> Reconstruction is also unique: join the first label of the remaining code to the least undeleted label absent from that code. Then remove the chosen leaf and the first code entry. Finally join the two remaining vertices. Thus all sequences of $m-2$ labels are in bijection with the trees.
>
> Vertex $i$ occurs in the code $d_i(S)-1$ times. For code $(a_1,\ldots,a_{m-2})$, the tree weight is therefore
>
> $$
> [x_i^{d_i(S)}]!
> =\mathbf x!\,[x_{a_1},\ldots,x_{a_{m-2}}]!
> $$
>
> Summing over all codes, each position independently contributes $w(\mathbf x)$. The sum is therefore $\mathbf x!\,w(\mathbf x)^{m-2}$. For $m=2$, the code is empty and its weight product is $1$, so the formula still holds. $\square$

**Proof of the theorem.** Contract every original component $B_i$ to a single vertex. Any completion of the forest to a tree determines a tree $S$ on these $m$ vertices.

For an edge $ij$ of $S$, choose one endpoint in $B_i$ and the other in $B_j$, giving $x_i x_j$ choices. Endpoint choices for different edges are independent: several new edges may meet at the same original vertex. Hence the number of realisations of a fixed tree $S$ is

$$
[x_i^{d_i(S)}]!
$$

Each completion uniquely determines $S$ and all new-edge endpoints. Conversely, each such choice joins the original trees without cycles. Summing over $S\in\mathcal T_m$ and applying the weighted Cayley formula proves the result.

For $m=1$, the original forest is already a tree, and its only completion is the empty edge set. The formula gives $T([n])=n\cdot n^{-1}=1$. $\square$

Equal component sizes do not require division by multiplicity factorials: the blocks are already fixed and distinguished by their vertices. Two prescribed pairs, for example, can be joined by any of four edges, so $T([2,2])=4$.

## Special cases and the meaning of the factors

| Original components | Number of completions | Explanation |
| --- | --- | --- |
| $[1^n]$ | $n^{n-2}$ | All vertices are isolated: the ordinary Cayley formula |
| $[n]$ | $1$ | The entire tree is already given |
| $[a,b]$ | $ab$ | Choose the endpoints of the sole new edge |
| $[q,1^{n-q}]$ | $q\,n^{n-q-1}$ | One fixed tree on $q$ vertices, with all other vertices isolated |
| $[2,1,1]$ | $2\cdot4=8$ | The example in Figure 1 |
| $[2,2,1]$ | $4\cdot5=20$ | Two prescribed pairs and a singleton |

As in the [[Partitions and the Combinatorial Potential of the Second Kind|partition notation]], $[1^n]$ means $n$ unit parts. The row containing $q$ assumes $1\leqslant q\leqslant n$.

The proof explains both factors. In the Prüfer code, each component supplies one compulsory factor $x_i$, while summing over each of the $m-2$ code positions supplies $n$. This produces the size product $\mathbf x!$ and the power $n^{m-2}$.

**Remark.** $T(\mathbf x)$ counts completions of one fixed forest. If its internal trees still have to be chosen, that is a separate count. For fixed blocks $abc\mid de$, the triple admits three trees, and each resulting forest has six completions. Thus there are $3\cdot6=18$ trees in which both prescribed blocks are connected. If the vertex partition is also varied, the same final tree may be counted more than once.

## Prüfer code type and the number of leaves

For $n\geqslant3$, the count $n^{n-2}$ can be refined by the multiplicities of labels in the Prüfer code. Let $\lambda\vdash n-2$ be the collection of positive multiplicities, and let $m=\#\lambda$ be the number of blocks obtained by grouping code positions with equal values. There are $s_2(\lambda)$ partitions of this type and $n_{\underline m}$ assignments of distinct vertices to the blocks. Thus the number of trees of this multiplicity type is

$$
s_2(\lambda)n_{\underline m},\qquad
n^{n-2}=\sum_{\lambda\vdash n-2}s_2(\lambda)n_{\underline{\#\lambda}}
$$

Here $n_{\underline m}=[n,n-1,\ldots,n-m+1]!$. A vertex of degree $d$ occurs in the code $d-1$ times. Consequently, $m$ is the number of nonleaf vertices and $n-m$ is the number of leaves. The positive parts of $\lambda$ are the degrees of nonleaf vertices **minus one**; this is not a forest type by component edge counts.

For five vertices:

| Code multiplicities | Vertex degrees of the tree | Number of trees |
| --- | --- | ---: |
| $[3]$ | $[4,1,1,1,1]$ | $1\cdot5=5$ |
| $[2,1]$ | $[3,2,1,1,1]$ | $3\cdot5\cdot4=60$ |
| $[1,1,1]$ | $[2,2,2,1,1]$ | $1\cdot5\cdot4\cdot3=60$ |

The total is $5+60+60=125$. Summing over types with $m$ parts gives $S(n-2,m)n_{\underline m}$ trees with $n-m$ leaves. The falling factorial counts assignments of distinct labels to blocks; this principle and its extension to rooted forests are developed in [[Falling Factorials, Rooted Forests, and Stirling Numbers]].

## Contraction to a weighted graph

After contracting the components, $x_i x_j$ possible original edges remain between vertices $i$ and $j$. These parallel edges can be replaced by one coupling of conductance

$$
c_{ij}=x_i x_j
$$

Denote the resulting complete weighted graph by $H_{\mathbf x}$. Its spanning-tree coefficient sums the products of conductances over its trees. Therefore,

$$
\tau(H_{\mathbf x})=T(\mathbf x)=\mathbf x!\,n^{m-2}
$$

This is precisely the graph obtained by [[Vertex Contraction and Graph Gluing|contracting the blocks]] of $K_n$: edges within blocks disappear, while conductances between blocks add.

![Blocks of sizes two, two, and one contracted to a weighted triangle with conductances four, two, and two](Block%20Contraction%20for%20Cayleys%20Formula.svg)

*Figure 2. The prescribed components on the left are $A=\{a,b\}$, $B=\{c,d\}$, and $C=\{e\}$. All complete-graph edges between them are available. After contraction, the number of choices for each interblock edge becomes its conductance: $c_{AB}=4$ and $c_{AC}=c_{BC}=2$.*

A triangle has three spanning trees, giving

$$
T([2,2,1])=4\cdot2+4\cdot2+2\cdot2=20
$$

### How the new edges are distributed

Consider these twenty completions on the original five vertices. There are two new edges, so their possible positive types are $[2]$ and $[1,1]$.

The tree on three contracted vertices has a central component incident to both new edges. Let its size be $a$, and the sizes of the other two components be $b,c$. There are $a^2bc$ endpoint choices altogether. If the two endpoints in the central component coincide, the new edges are adjacent, giving $abc$ choices. If they differ, there are $a(a-1)bc$ choices of type $[1,1]$.

For the blocks $A,B,C$ in Figure 2:

| Central component | All completions | Type $[2]$ | Type $[1,1]$ |
| --- | ---: | ---: | ---: |
| $A$, size $2$ | 8 | 4 | 4 |
| $B$, size $2$ | 8 | 4 | 4 |
| $C$, size $1$ | 4 | 4 | 0 |
| **Total** | **20** | **12** | **8** |

Contraction preserves the total completion count but hides the distinction between two endpoints within a block. The type of the new edges must therefore be determined **on the original vertices**, before contraction. Two adjacent edges on five vertices have full type $[2,0,0]$; two disjoint edges have type $[1,1,0]$.

## Passage to polyforms

Let $b_1,\ldots,b_m$ be basis vertices of $H_{\mathbf x}$. Define the set of index pairs $\mathcal I_m=\{(i,j):1\leqslant i<j\leqslant m\}$. By the [[Basic Objects and Operations of Polyform Algebra|definition of the Laplacian polyform]],

$$
L_{\mathbf x}=\sum_{(i,j)\in\mathcal I_m}x_i x_j[(b_i b_j)]^2
$$

The top grade of the [[Laplacian Exponential|Laplacian exponential]] gives

$$
\boxed{
\frac{L_{\mathbf x}^{m-1}}{(m-1)!}
=\mathbf x!\,n^{m-2}[(b_1\ldots b_m)]^2
}
$$

For $m=1$, both sides equal $e$. The number of completions of the prescribed forest thus becomes the coefficient of the boundary form on the contracted vertices.

For sizes $[2,2,1]$, this identity is

$$
\frac{\bigl(4[(AB)]^2+2[(AC)]^2+2[(BC)]^2\bigr)^2}{2!}
=20[(ABC)]^2
$$

Here $A,B,C$ denote the contracted vertices. The number $20$ has been obtained in three consistent ways: from the general formula, by summing the weights of the triangle's three trees, and as the top coefficient of its polyform.

## Verification and the role of the result

The general formula was proved using the weighted Cayley formula. Equality with the spanning-tree coefficient follows from the explicit correspondence between completions and trees of the contracted graph; the polyform expression follows from the forest expansion of the exponential.

Independent enumeration of new-edge sets for sizes $[2,1,1]$, $[2,2,1]$, and $[2,2,1,1]$ gave $8$, $20$, and $144$ completions, respectively. Grouping by positive types of the new edges gave $2+6$, $12+8$, and $64+72+8$. For $[2,2,1,1]$, the last three counts belong to types $[3]$, $[2,1]$, and $[1,1,1]$. All eight drawings in Figure 1 agreed with the enumeration.

The potential $s_2$ counts partitions into prescribed sizes; the factor $t$ in [[Combinatorial Potentials in Symmetric Polyforms#Counting forests of a prescribed type|the forest count]] counts choices of trees within the blocks; and $T(\mathbf x)$ counts completions of an already prescribed forest. They describe three different stages of construction.

This note is based on the author's research within PMG. The classical forest-completion formula appears in [1]; the figures, examples, and adaptation to the present notation were prepared for this collection of notes.

The ordinary Cayley formula is independently derived from SPF identities in [[Symmetric Polyforms of the Complete Graph|the note on the complete graph]]. Here the Prüfer code gives the general number of ways to join prescribed components; the two derivations complement each other.

## References

1. Jim Pitman. *Coalescent Random Forests*. [Open text at UC Berkeley](https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf). Lemma 3 (Moon), equation (7): the number of trees containing a prescribed forest; §5: relation to the multinomial Cayley formula.
