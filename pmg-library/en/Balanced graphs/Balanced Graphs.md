---
title: Balanced Graphs
date: 2026-10-24
updated: 2026-10-24
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: balanced-graphs-series-navigation
order: 0
description: "Balance, the bilinear Laplacian and its exponential, circulation, directional metrics and spheres, balancing, forest toponomes, and permutation digraphs."
---

This series extends PMG to **balanced graphs**: the total incoming weight equals the outgoing weight at every vertex. Undirected graphs form the symmetric special case. Balance retains boundary forms, a finite Laplacian exponential, and one common spanning-tree coefficient. Asymmetry adds a directional bilinear pairing and circulation.

Twelve notes form a complete introductory route. Algebraic definitions precede interpretations: one-way resistances are defined by form potentials and subsequently interpreted as hitting times. Electrical and geometric explanations state their applicability conditions.

## Contents and reading order

| Order | Note | Main content |
| ---: | --- | --- |
| 1 | [[Balanced Graphs and Spanning-Tree Potentials]] | Balance and symmetry, cycle decompositions, equal rooted potentials, a directed 3-cycle, and permutation digraphs |
| 2 | [[The Bilinear Laplacian of a Balanced Graph]] | Canonical centroid representation, admissible coefficients, and boundary products with arbitrary points |
| 3 | [[The Laplacian Exponential of a Balanced Graph]] | Finite bilinear-factor products, minors, directed forests, and the spanning-tree coefficient |
| 4 | [[The Circulation Form]] | An independent skew-symmetric form, triangulations, products, and the distinction from a nonnegative graph Laplacian |
| 5 | [[Balanced Variations]] | Spanning-tree changes, reassigning arcs, adding cycles, and inserting vertices |
| 6 | [[One-Way Resistance and Hitting Times]] | Directional resistance forms, matrix properties, Laplacian recovery, and the Markov interpretation |
| 7 | [[Resistance Geometry and Circulation]] | Euclidean geometry, nonreciprocal responses, circulation potentials, and three-vertex resistance |
| 8 | [[The Gram Matrix and Directional Coordinates of a Balanced Graph]] | The canonical vertex Gram matrix, source and receiver roles, bi-coordinates and di-coordinates |
| 9 | [[The Isotropic Space and Sphere of a Balanced Graph]] | The null vector, bordered inversion, two sphere representatives, one radius, and tree degrees |
| 10 | [[Balancing a Directed Graph by Spanning-Tree Potentials]] | Unique normalized scaling of outgoing couplings, computation, limitations, and the additive alternative |
| 11 | [[Toponomes of Balanced Graphs and Directed Forests]] | Rooted-forest types, two normalizations, the symmetric limit, determinants, and information loss |
| 12 | [[Permutation Digraphs and Cycle Combinatorics]] | Degree-one graphs, cycle probabilities and means, marked paths, and regular-graph decompositions |

## Main results

**Balance and one spanning-tree coefficient.** For a connected nonnegatively weighted graph, balance is equivalent to equal positive principal Laplacian minors of order $n-1$. They count weighted directed trees toward a chosen root. Symmetry is unnecessary.

**One algebra of forms.** With $h=(a_1+\cdots+a_n)/n$, the Laplacian is

$$
L=\sum_{i,j}L_{ij}[a_i-h,a_j-h],\qquad
M=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!}
$$

The coefficients $L_{ij}$ are scalar matrix entries. Powers use the commutative polyform product, which differs from matrix multiplication. Splitting the Laplacian into symmetric and skew-symmetric parts aids interpretation but is not required for multiplication.

**One-way resistance.** For a connected balanced graph, put $\mathbf{Gr}=\mathbf L^+$ and $P_M(F)=\tau(MF)/\tau(M)$. Then

$$
r_{ij}=P_M([a_j-h,a_j-a_i])=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij},\qquad
R_{ij}=r_{ij}+r_{ji}
$$

The first index of $r_{ij}$ is the initial vertex, the second the target. For a continuous-time chain with generator $-\mathbf L$, the mean hitting time is $H_{ij}=nr_{ij}$. Asymmetry of $r$ alone does not imply graph asymmetry: closed circulation sums matter, not only individual differences $r_{ij}-r_{ji}$.

**Geometry and directions.** The symmetric pairing part defines Euclidean geometry with squared distances $R_{ij}$. The skew part measures nonreciprocal response. The isotropic model defines directional sphere coordinates and one resistance radius; in general, this differs from the squared Euclidean circumradius of the symmetric metric.

**Forests and combinatorics.** The vertex polynomial reduction of the forest toponome is $\det(\mathbf I+t\mathbf L)$. Regular balanced graphs decompose into directed 1-factors. This partitions arcs on a common vertex set; its terms are not disjoint connected components.

## Reading routes

- **Algebra:** notes 1-5, after [[Basic Objects and Operations of Polyform Algebra]] and [[Laplacian Exponential]]. The main questions are what survives without symmetry and how to compute products.
- **Metrics and geometry:** notes 1-3 followed by 6-9. [[The Null Vector, Isotropic Representation, and the Boundary]] and [[Projections, Bi-coordinates, and Di-coordinates]] provide the symmetric starting point.
- **Balancing data and flows:** notes 1 and 10; add 6-9 for the resulting metric. Scaling preserves directions and outgoing proportions while changing weights.
- **Forests and toponomes:** notes 1-3 and 11 alongside [[Partition Toponomes]] and [[Polynomial Toponomes]]. Numerical types alone do not determine products on a common vertex set.
- **Permutation combinatorics:** notes 1 and 12, then [[Cyclic Partitions and the Combinatorial Potential of the First Kind]]. This route does not require the directional metric.

## Conventions and scope

For $i\to j$, the first index denotes the source and the second the receiver. The Laplacian uses outgoing weights. In a bilinear pairing, the first argument has the source role and the second the receiver role; argument order and the associated transpose are fixed in the metric notes.

“2-balanced graph” means a symmetric graph admitting a directed 2-cycle decomposition. “Regular balanced graph of degree 2” means two incoming and two outgoing arcs at every vertex. These are different conditions.

Circulation forms are defined beyond Laplacians with nonnegative weights. A toponome refers to a chosen forest representation, not an arbitrary polyform expression. Triangulating circulation does not imply a positive decomposition into directed 3-cycles.

The general algebra of marked types, component probabilities in regular balanced graphs, resistance symmetrization, and connections between circulation, electrodynamics, and holonomy remain research topics. Their questions and sources are recorded in the [project map (in Russian)](https://github.com/magin67/pmg-notes/blob/v5/pmg-library/ru/%D0%9A%D0%B0%D1%80%D1%82%D0%B0%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20PMG.md).

Proofs appear in the individual notes; computations supplement them. References to established results accompany the corresponding constructions. General definitions and terminology are in [[Core specification]] and [[PMG terminology]]; the core's main graph model remains symmetric.
