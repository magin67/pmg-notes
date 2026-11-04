---
title: Metric Parameters of Graphs
date: 2026-10-18
updated: 2026-11-04
revision: 4
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
translation_key: metric-parameters-series-navigation
lang: en
description: "Reading order for eight notes on resistance radius, Gram matrices and volumes, centralities, dimensionless parameters, vertex deletion, the centers of both graph simplices, degree potential, and internal Laplacian norms. A guide to results and their polyform representations."
order: 0
tags:
  - resistances
  - forests-and-spanning-trees
  - variations
aliases:
  - "en/Metric parameters/Metric Parameters of Graphs"
  - "en/Metric parameters/index"
---

How can the size of a graph's resistance simplex be described by a single number? How do central vertices differ from critical ones? Which parameters distinguish a path from a star, and which are the same for all trees of the same order? The eight notes in this series connect these questions with circumsphere geometry, the Green matrix, spanning trees, and the Laplacian exponential.

The series considers finite connected undirected loopless graphs with positive conductances on existing edges. Parameters of the whole graph are distinguished from characteristics of individual vertices; restrictions concerning the number of vertices, degeneracy, and disconnection are stated in the relevant notes.

In PMG, the norm is quadratic: $X^2=X\cdot X$. The resistance radius $\rho=R_{\mathrm{sph}}^2$ and resistance diameter $D_{\mathrm{res}}=4\rho$ have the physical dimension of resistance. The latter is the square of the ordinary diameter of the circumsphere; in general, it does not equal the maximum pairwise resistance.

## Place in the library

Primary section: [[en/Resistance Geometry and Duality/Resistance Geometry and Duality|Resistance Geometry and Duality]].

Secondary thematic entries:

- [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]]: tree invariance and the distinguishing power of parameters.

[[en/Cross-cutting Tags|Cross-cutting Tags]] · [[en/Thematic Index|Thematic Index]].

## Prerequisites

The graph part requires [[Effective Resistance and Graph Geometry|effective resistance and the resistance simplex]], and [[Laplacian, Green Matrix, and Effective Resistance Matrix|conversions between the Laplacian, Green matrix, and resistance matrix]]. The polyform expressions build on [[Laplacian Exponential|the Laplacian exponential and normalized potentials]].

The geometric background is developed in [[en/Resistance Geometry and Duality/Spaces/Spaces and Subspaces in PMG|Spaces and Subspaces in PMG]]. Particularly relevant are [[Nonlocal Elements, Spheres, and Their Centers|the distinction between a sphere element and its center]], [[Projections, Bi-coordinates, and Di-coordinates|projections and coordinates]], and, for comparing the two types of vertex removal, [[Vertex Elimination and Induced Couplings|elimination that preserves the metric]].

General definitions and notation are given in the [[Core specification|core specification]] and [[PMG terminology|PMG terminology]].

## Notes in the series

1. **[[Resistance Radius and Diameter of a Graph]].** Definitions and normalizations, the distinction between the circumsphere diameter and the maximum resistance, and computation of the center and radius from the resistance matrix and through polyforms. Examples include a single edge, a triangle, trees, and complete graphs; reciprocal connectivity parameters and the limits of their interpretation are discussed.

2. **[[Resistance Radius of a Set - Gram Matrix and Volume]].** The radius and center coordinates from the inverse Gram matrix of local points; the relation between the determinant, volume, and spanning-tree coefficient. The formulas are checked on a segment, triangle, and tetrahedron. Monotonicity of the radius under passage to a subset with the original metric is proved.

3. **[[Centroid, Spanning-Tree, and Eigenvector Centralities]].** The minimizing property of the centroid, the Green diagonal and trace, the Kirchhoff index, and a decomposition of the radius. Expected spanning-tree degrees determine the circumcenter coordinates. Three normalized centralities are compared on simple graphs and the Krackhardt kite graph; a formula is derived for the change in radius under geometric removal of a vertex.

4. **[[Density, Compactness, and Tree Invariance]].** Comparison of edge density, radius compactness, measures based on the Kirchhoff index and algebraic connectivity, efficiency, and arboricity. Bounds and tree invariance of radius compactness are proved. Paths, stars, cycles, wheels, fans, complete, bipartite, and named graphs illustrate differences between the measures; examples of edge changes reveal limits of their interpretations.

5. **[[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius]].** Deleting a vertex together with its edges is compared with removing a point while preserving resistances. Relative changes in the spanning-tree coefficient are related to weighted degree and the probability of being a leaf in a random spanning tree; the change in radius under preservation of the metric is related to a circumcenter coordinate. Polyform expressions and a counterexample clarify the meaning of vertex criticality.

6. **[[Sphere Centers and Graph Heterogeneity]].** The circumcenters of the simplices with Laplacian and Green Gram matrices, coordinate formulas, and bordering. Electrical and diffusion interpretations of displacement, equality of both displacements on unit-conductance trees, exact examples, a counterexample to a structural-symmetry criterion, and conditional sensitivity to weak cuts.

7. **[[Degree Potential and Centralities]].** Ranking by the Laplacian circumcenter coordinates; agreement with closeness and centroid centrality on unit-conductance trees, links to generalized degree and eigenvector centrality. Exact counterexamples, positive normalization, and comparison on the Krackhardt kite graph.

8. **[[Norms of Subgraph Laplacians]].** Internal Laplacians evaluated in the metric of the whole graph: expected internal edge counts in random spanning trees, bounds, trees and blocks, partitions and sensitivity. Partial observations and Kron reduction, comparison with boundary and Greenian norms, and the search for a group of maximum norm.

## Reading routes

**For the full series:** follow the order above. Definitions and examples are in the main text; proofs and details of independent computational checks are available in collapsible blocks.

**Choosing a characteristic:** start with [[Resistance Radius and Diameter of a Graph|the radius and diameter]], then move to [[Centroid, Spanning-Tree, and Eigenvector Centralities|vertex centralities]] or [[Density, Compactness, and Tree Invariance|dimensionless parameters of the whole graph]]. Equal parameter values do not imply identical graph structures.

**The effect of vertex removal:** read the [[Resistance Radius of a Set - Gram Matrix and Volume#The radius of a subset and projection of the center|subset theorem]], then the [[Centroid, Spanning-Tree, and Eigenvector Centralities#Removing a point while preserving the metric|formula for removing a single point]], and the [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius|comparison of the two types of removal]]. Deleting a row and column from the Gram matrix preserves the metric of the remaining points; deleting a vertex from the network requires a new metric and may disconnect the graph.

**Comparing centers and heterogeneity:** after the [[Centroid, Spanning-Tree, and Eigenvector Centralities|resistance center]], move to the [[Sphere Centers and Graph Heterogeneity|two simplex geometries]]. Coincidence of the circumcenter and centroid characterizes the corresponding type of regularity and does not guarantee structural symmetry.

**Degree potential as a centrality:** after the geometric definition of the center, read [[Degree Potential and Centralities]]. Agreement with established rankings depends on the graph class; positive normalization does not remove nonmonotonicity.

**Comparing vertex groups:** read [[Norms of Subgraph Laplacians]]. Keep the metric of the whole graph fixed; distinguish internal connectivity in a random spanning tree from density and criticality under vertex deletion.

## Guide to results

| What to find | Where to read |
|---|---|
| The radius of a tree and additivity under single-vertex gluing | [[Resistance Radius and Diameter of a Graph#Trees\|Trees]] |
| The Gram determinant, radius, and simplex volume | [[Resistance Radius of a Set - Gram Matrix and Volume#Determinant, radius, and volume\|The determinant formula]] |
| The Green trace, Kirchhoff index, and displacement of the circumcenter from the centroid | [[Centroid, Spanning-Tree, and Eigenvector Centralities#Total resistance to the centroid, the Kirchhoff index, and the radius\|Decomposition of the radius]] |
| Expected spanning-tree degree and circumcenter bi-coordinates | [[Centroid, Spanning-Tree, and Eigenvector Centralities#Expected spanning-tree degree and circumcenter coordinates\|The degree-coordinate relation]] |
| Why radius compactness is the same for all unit-conductance trees of a given order | [[Density, Compactness, and Tree Invariance#Tree invariance\|Tree invariance]] |
| Why strengthening a coupling can increase the radius | [[Density, Compactness, and Tree Invariance#Adding an edge\|A counterexample on a complete bipartite graph]] |
| Spanning-tree ratios under the two types of vertex removal | [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius#The spanning-tree ratio and leaf probability\|Ratios and leaf probability]] |
| Why a small positive spanning-tree ratio does not imply proximity to disconnection | [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius#A limitation of the criticality interpretation\|A counterexample to the criticality interpretation]] |
| Laplacian circumcenter, bordered Green matrix, and degree diffusion | [[Sphere Centers and Graph Heterogeneity#The Laplacian circumcenter\|Center formulas]]; [[Sphere Centers and Graph Heterogeneity#Center displacement and diffusion\|Diffusion interpretation]] |
| Why zero displacement does not imply structural symmetry | [[Sphere Centers and Graph Heterogeneity#Coincident centers and structural symmetry\|An asymmetric graph with coincident centers]] |
| Equal displacements on unit-conductance trees | [[Sphere Centers and Graph Heterogeneity#Equal displacements on unit-conductance trees\|Equality of displacements]] |
| Degree potential, closeness on trees, and eigenvector centrality | [[Degree Potential and Centralities]] |
| Internal Laplacian norms, spanning-tree interpretation, and partial observations | [[Norms of Subgraph Laplacians]] |
| Why a fixed group's norm can decrease under enlarged observations | [[Norms of Subgraph Laplacians#Enlarging the observed set\|Effective couplings and the Schur complement]] |

## How the parameters are expressed through polyforms

The computation of the [[Resistance Radius and Diameter of a Graph#Computing the center and radius using polyforms|radius]] and [[Centroid, Spanning-Tree, and Eigenvector Centralities#The next-to-top-grade component and vertex parameters|vertex parameters]] uses normalized potentials of grade-one forms, obtained through the next-to-top-grade component of the Laplacian exponential. The [[Resistance Radius of a Set - Gram Matrix and Volume#Subset volume through grade components of the exponential|volume of a subset]] requires the component whose grade complements that of its boundary form to the top grade.

[[Density, Compactness, and Tree Invariance#Representation through polyforms|Dimensionless metric parameters]] are built from these evaluations. In the [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius#Vertex properties through polyforms|study of vertex removal]], marking the vertex's incident edges in the exponential gives its spanning-tree degree distribution. Elimination that preserves the metric is expressed by projection, whereas deletion from the network changes the Laplacian and its exponential. Polyforms describe characteristics of vertices and the whole graph as well as characteristics of edges.

## Status and scope of the series

Definitions, proved claims, and computational examples are distinguished in each note, together with sources and applicability conditions. Normalization on a complete graph is not described as statistical unbiasedness. None of the centralities or compactness measures is proposed as a universal measure of graph resilience.

A compact expression for the radius after deleting a vertex together with its edges, in terms of a small number of vertex characteristics in the original graph, remains an open question. Computation from the new Laplacian and its polyform exponential is defined; this computation is not equivalent to the sought compact formula.

All eight notes are available in Russian and English, with matching notation and reading orders.


## Origins of the results in the centrality supplement

| Result | Source or derivation | Role in PMG | Novelty claim |
|---|---|---|---|
| Degree potential and center coordinates | Laplacian simplex-center formula and the Poisson equation | Geometric vertex ranking | None |
| Limiting relation to generalized degree | Csató's family; spectral derivation in the note | Comparison with an established centrality | Priority not separately established |
| Closeness and centroid centrality on trees; eigenvector centrality to first order | Proofs in the note | Conditions for agreement of rankings | None |
| Disagreement and nonmonotonicity | Exact finite examples | Limits of application | Illustrations, not a priority claim |
| Equal displacements on unit-conductance trees | Consequence of the Green diagonal and distance-sum formulas | Relation between the two geometries | None |

## Origins of the results on subgraph norms

| Result | Source or derivation | Role in PMG | Novelty claim |
|---|---|---|---|
| Internal Laplacian norm and its bounds | Kirchhoff's edge formula and forest edge counts | Evaluating groups in a fixed metric | None |
| Trees and biconnected blocks | Uniqueness of the spanning tree; local Foster formula | Exact extremal examples | None |
| Sensitivity and decrease under enlarged observations | Spanning-tree derivative and Kron reduction | Distinguishing forms, metrics, and observations | Consequences of established formulas |
| Comparison with boundary and Greenian norms | Gram determinants, the two exponential metrics, and signed forest sums | Distinguishing grades and interpretations | Exposition and examples, not a priority claim |
