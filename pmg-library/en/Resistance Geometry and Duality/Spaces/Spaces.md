---
title: Spaces
date: 2026-10-14
updated: 2026-11-11
revision: 10
translated_revision: 10
status: draft
text_prepared_by: ChatGPT
translation_key: spaces-subspaces-series-navigation
lang: en
description: "Reading order for nine notes on PMG spaces: choosing a basis, the null vector, nonlocal elements and spheres, coordinates, form decompositions, contraction, the Dirichlet problem, and induced couplings. Prerequisites and reading routes."
order: 0
tags:
  - resistances
  - boundary-data
  - gluing
aliases:
  - "en/Spaces/Spaces and Subspaces in PMG"
  - "en/Spaces/index"
  - "en/Resistance Geometry and Duality/Spaces/Spaces and Subspaces in PMG"
---

Choose several vertices of a graph. They generate a subspace relative to which we can describe the remaining vertices and their positions. Which coordinates do we need? How are projection onto the chosen subspace, extension of prescribed values, and construction of a graph on the selected vertices related?

The nine notes in this series connect these questions. We begin with spaces of elements and vectors, then consider nonlocal elements, spheres, coordinates, form decompositions, and graph operations. We finish with an application: using a table of employee-document couplings to construct couplings between employees or between documents.

Forms and polyforms participate at every stage: they provide metric evaluations and describe projections and changes of space under graph operations. Matrices are used for proofs, computation, and comparison with established constructions.

## Place in the library

Primary section: [[en/Resistance Geometry and Duality/Resistance Geometry and Duality|Resistance Geometry and Duality]].

Secondary thematic entries:

- [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]: the Dirichlet problem, vertex elimination, and contraction.

[[en/Getting Started and Foundations/Navigation/Thematic Index#Search by tags|Search by tags]] · [[en/Getting Started and Foundations/Navigation/Thematic Index|Thematic Index]].

## Prerequisites

The foundation is the [[en/Getting Started and Foundations/Introduction/PMG Introductory Series|Introductory Series]]. The following topics are particularly useful here:

- objects, elements, affine vectors, exterior products, boundaries, and forms - [[Basic Objects and Operations of Polyform Algebra]];
- resistance geometry, inner products, and norms of exterior structures - [[Effective Resistance and Graph Geometry]], [[Inner Product of Graph Vectors]], and [[Metric of Higher-Grade Objects]];
- the metric polyform and computation of the metric through normalized potentials - [[Laplacian Exponential]].

Definitions and notation are collected in the [[Core specification|Core Specification]], and names and terminological distinctions in [[PMG terminology|Terminology]]. The results on coupling variations from the introductory series are not required for the main route.

## Notes in the series

1. **[[Basis]].** We distinguish the linear space of formal vertices, the space of affine vectors, and the affine space of elements. Selected vertices generate subspaces; a basis lets us write their exterior structures and forms. Metric evaluations are obtained through potentials of forms.

2. **[[The Null Vector, Isotropic Representation, and the Boundary]].** We construct an isotropic model with local points and a correction selecting the center of an element. The distinguished null vector connects affine weight, flat geometry, and the boundary operator. This note develops the geometric part of the series; its constructions are also used in the section on isotropic coordinates.

3. **[[Nonlocal Elements, Spheres, and Their Centers]].** The norm of an element specifies a sphere parameter, while a nonlinear correction selects its local center. We distinguish the sphere element from its center and prove that the norms and inner products of vectors and boundaries of every grade are preserved when vertex norms change with centers fixed.

4. **[[Bi-coordinates and Di-coordinates]].** Bi-coordinates are expansion coefficients; di-coordinates are inner products with the basis objects. The metric and inverse metric tensors connect the two descriptions. The note covers index contraction, changes of basis, and the reciprocal basis.

5. **[[Decomposing a Form into Atomic and Difference Parts]].** A frame determines the atomic and difference parts of quadratic and polar forms. The difference part defines the Laplacian of a frame. The shared geometry, projections, and potential calculations are collected here; linear projection is compared with the local center in the isotropic model.

6. **[[Vertex Contraction and Graph Gluing]].** Identifying vertices produces a space that can be realized as an orthogonal subspace of the original one. Gluing at a single vertex joins the spaces of the components. The Laplacian exponential describes independent components and their combination; under single-vertex gluing, spanning-tree coefficients multiply and resistance radii add.

7. **[[Selected Vertices and the Dirichlet Problem]].** We prescribe values at selected vertices and extend them with minimum energy. The extension coefficients are the bi-coordinates of projections and form the influence matrix. The metric of residuals is computed through the polyform of a contracted graph. We state the conditions that ensure uniqueness.

8. **[[Vertex Elimination and Induced Couplings]].** We construct a graph on selected vertices that preserves effective resistances between them, minimum energy, and response. Decomposition of the Laplacian and factorization of its exponential explain preservation of the metric. The Schur complement gives the matrix form of elimination; projection of the circumcenter lets us compare the resistance radii of the original and induced graphs.

9. **[[Couplings Within One Part of a Bipartite Graph]].** We apply vertex elimination to a rectangular table of couplings. The Laplacians of projection frames define induced couplings within the chosen part. We compare the two possible induced graphs, define a common normalized spanning-tree parameter of the original graph, and explain why the resistance radii of the parts generally do not add up.

## Reading routes

**For the full series:** follow the order above. Examples explain the constructions, while collapsible proofs give general derivations. Conditions on connectivity, nondegeneracy, and the presence of selected vertices in each component are stated where they are needed.

**Graphs and applications:** start with [[Basis|spaces and the choice of a basis]], then move to [[Bi-coordinates and Di-coordinates|coordinates]] and [[Decomposing a Form into Atomic and Difference Parts|form decompositions and projections]]. Continue with [[Vertex Contraction and Graph Gluing|contraction and gluing]], [[Selected Vertices and the Dirichlet Problem|the Dirichlet problem]], [[Vertex Elimination and Induced Couplings|vertex elimination]], and [[Couplings Within One Part of a Bipartite Graph|the bipartite application]]. The isotropic extension is not required for this route. The supplement on the two Dirichlet problems in a balanced directed graph can be skipped until the directed model has been studied.

**Isotropic geometry:** after [[Basis|spaces and the choice of a basis]], read about [[The Null Vector, Isotropic Representation, and the Boundary|the null vector and the boundary]], then [[Nonlocal Elements, Spheres, and Their Centers|nonlocal elements and spheres]] and [[Bi-coordinates and Di-coordinates|coordinates]]. The comparison between linear projection and selection of the center is in the section on [[Decomposing a Form into Atomic and Difference Parts#Coordinates in the isotropic extension|isotropic coordinates]].

All nine notes are available in Russian and English, with matching reading orders.

## Programming companion

[[en/PythonExamples/Example - Subspaces and Graph Transformations|Subspaces and Graph Transformations]] - potentials, bi- and di-coordinates, Dirichlet extension, contraction, and elimination. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/spaces.ipynb).

## Continuations and sources

Spectral relations between the parts of a bipartite graph, gluing at several vertices, a fuller treatment of Lorentzian geometry, and possible physical interpretations are reserved for separate notes. General polyform reduction and the spanning-tree operator also belong to a separate continuation. These questions and their dependencies are tracked in the [[en/Getting Started and Foundations/Navigation/Library Map|library map]].

Sources and the status of results are given in each note. Established constructions are compared with their presentation in PMG after the objects involved have been defined.

