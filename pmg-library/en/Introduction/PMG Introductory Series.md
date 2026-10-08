---
title: "PMG Introductory Series"
date: 2026-10-08
updated: 2026-10-08
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: introductory-series-navigation
lang: en
description: "Reading order for the ten introductory PMG notes: resistance geometry, coupling variations, polyform algebra, and the Laplacian exponential. Prerequisites and recommended reading."
---

The introductory series connects the graph Laplacian, electrical networks, resistance geometry, and polyform algebra. Its ten notes form a sequential course, from current equations and effective resistance to the extraction of metric quantities from the Laplacian exponential in the algebra of forms.

The first seven notes present results from linear algebra, electrical network theory, and random spanning trees. The final three introduce the formal objects and operations adopted in PMG, the extension of the metric to exterior powers, and the construction of the metric polyform. Standard results and project definitions are distinguished as they are introduced.

## Prerequisites and reading order

Matrices, systems of linear equations, and inner products are sufficient to begin. Later notes use determinants, eigenvalues, and positive definite matrices. Basic concepts from graph theory and electrical networks are explained in the text. The sections on random spanning trees require elementary probability; the exterior product and boundary operator are introduced within the series.

The main reading order is **1-5, then 6-7, then 8-10**. These three groups correspond to the sections of [[Further Reading for the PMG Introductory Series|the reading recommendations]]. Collapsible proofs give general derivations; examples provide specific calculations and independent checks.

## Graphs, electrical networks, and resistance geometry

This group constructs a metric representation of a connected graph. Linear algebra is sufficient for the main development; the probabilistic interpretation appears at the end of the fifth note.

1. **[[Laplacian - graph, electrical network and quadratic form|Laplacian: Graph, Electrical Network and Quadratic Form]].** Conductances, potentials, and currents; the network equation and the freedom to choose a reference potential. The Laplacian quadratic form expresses network power and leads to the definition of effective resistance.

2. **[[Effective Resistance and Graph Geometry]].** The Green matrix is introduced as the inverse of the Laplacian on the zero-sum subspace. It defines the resistance simplex, in which resistances equal squared Euclidean distances. A separate proof shows that resistance itself also defines a metric on the vertices.

3. **[[Inner Product of Graph Vectors]].** The inner product of affine vectors is computed from four resistances and interpreted as a transfer voltage. The note discusses orientation, reciprocity of measurements, and the four-point identity. The eighth note returns to the structural form of this identity.

4. **[[Laplacian, Green Matrix, and Effective Resistance Matrix|Laplacian, Green Matrix, and Effective Resistance Matrix: Mutual Transformations]].** Forward and inverse transformations between the three matrices, double centering, and reconstruction of conductances from resistances. This develops the construction of the second note; the definition of the Green matrix is assumed to be known.

5. **[[From Lengths to Areas and Volumes]].** Gram and Cayley-Menger determinants compute areas and higher-dimensional volumes. The matrix-tree theorem relates the volume of the full resistance simplex to the spanning-tree coefficient. Gram determinants of edge vectors also express joint edge-inclusion probabilities in a random spanning tree.

Reading: [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|Doyle and Snell, Spielman, and Devriendt]]. For the fifth note, additional sources on determinants, exterior algebra, and random spanning trees are listed in the [[Further Reading for the PMG Introductory Series#Relation to the introductory notes|note-to-source table]].

## Coupling variations

This group explains how conductance changes affect resistances and the spanning-tree coefficient. It builds on inner products, Gram matrices, and the matrix-tree theorem from the first group. The formulas for finite changes do not require the changes to be small.

6. **[[Variation of a Single Edge]].** A rank-one perturbation gives exact changes in the Green matrix, resistances, and spanning-tree coefficient. The note derives conductance sensitivity, Rayleigh monotonicity, the bridge criterion, and the variation of separating spanning 2-forest weights. Conditions for preserving connectivity are distinguished from formulas that remain valid when connectivity is lost.

7. **[[Varying several couplings together|Varying Several Couplings Together]].** The Gram matrix of the selected couplings describes their joint effect. Its principal minors express mixed variation coefficients, volumes, and edge-inclusion probabilities in a spanning tree. The note considers deletion of an edge set, connectivity of intermediate networks, and concavity of the logarithm of the spanning-tree coefficient.

Reading: [[Further Reading for the PMG Introductory Series#Coupling variations|the Sherman-Morrison and Woodbury matrix identities]]. The source on transfer currents and random spanning trees is identified in the [[Further Reading for the PMG Introductory Series#Relation to the introductory notes|note-to-source table]].

## Exterior algebra and metric polyforms

This group introduces formal objects that can be manipulated before a metric is chosen. For a first reading, the preceding material on inner products and determinants is sufficient; prior familiarity with exterior algebra makes the proofs easier to follow.

8. **[[Basic Objects and Operations of Polyform Algebra]].** Points, affine vectors, exterior products, simplices, and their boundaries. Forms are defined through bilinearity, and their product through the exterior product of their arguments. The note proves the structural four-point identity, the rules for products of edge vectors, and nilpotence results for forms on boundaries.

9. **[[Metric of Higher-Grade Objects]].** The inner product of affine vectors extends to boundaries at each grade through mixed Gram determinants. The numerical squared norm is distinguished from the quadratic form of an object; simplex areas and volumes are computed from the norms of their boundaries.

10. **[[Laplacian Exponential]].** The exponential in the algebra of forms expands over spanning forests, and its top-grade component contains the spanning-tree coefficient. A general determinant lemma proves that normalized extraction of the top-grade coefficient reproduces the metric of the preceding note. Disconnected graphs and the distinction between algebraic variation and edge addition are also discussed.

Reading: [[Further Reading for the PMG Introductory Series#Exterior algebra and metric polyforms|exterior algebra, Gram determinants, and spanning trees]]. Forms and the metric polyform are defined directly in notes 8-10.

## Reading routes by task

| Task | Route |
|---|---|
| Understand the electrical and geometric meanings of resistance | 1-3 |
| Reconstruct conductances from pairwise resistances | 1-2, then 4 |
| Compute network changes when couplings are added or removed | 1-3, 5-7 |
| Move from matrix formulas to polyform algebra | 1-3, 5, then 8-10; notes 6-7 provide motivation through variations |

## Applications and further reading

Resistances and their variations can be used to analyze connectivity and select additional couplings. One modern example concerns information transmission in graph neural networks: effective resistance is used to analyze difficulty in passing information between distant vertices and to select edges to add. This approach is studied by M. Black, Z. Wan, A. Nayyeri, and Y. Wang in [Understanding Oversquashing in GNNs through the Lens of Effective Resistance](https://proceedings.mlr.press/v202/black23a.html), ICML 2023. Notes 2, 6, and 7 provide the mathematical background for reading this paper.

The Laplacian exponential in note 10 uses the product of forms. It should be distinguished from the matrix exponential used to describe diffusion on a graph.

Full bibliographic details, recommended sections, and access information are collected in [[Further Reading for the PMG Introductory Series]].
