---
title: Spaces and Subspaces in PMG
date: 2026-10-14
updated: 2026-10-15
revision: 2
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: spaces-subspaces-series-navigation
lang: en
description: "Reading order for seven notes on PMG spaces: choosing a basis, the null vector, coordinates, contraction, the Dirichlet problem, and induced couplings. Prerequisites and reading routes."
order: 0
---

Choose several vertices of a graph. They generate a subspace relative to which we can describe the remaining vertices and their positions. Which coordinates do we need? How are projection onto the chosen subspace, extension of prescribed values, and construction of a graph on the selected vertices related?

The seven notes in this series connect these questions. We begin with spaces of points and vectors, then consider coordinates and graph operations. We finish with an application: using a table of employee-document couplings to construct couplings between employees or between documents.

Forms and polyforms participate at every stage: they provide metric evaluations and describe projections and changes of space under graph operations. Matrices are used for proofs, computation, and comparison with established constructions.

## Prerequisites

The foundation is the [[PMG Introductory Series]]. The following topics are particularly useful here:

- points, affine vectors, exterior products, boundaries, and forms - [[Basic Objects and Operations of Polyform Algebra]];
- resistance geometry, inner products, and norms of exterior elements - [[Effective Resistance and Graph Geometry]], [[Inner Product of Graph Vectors]], and [[Metric of Higher-Grade Objects]];
- the metric polyform and computation of the metric through normalized potentials - [[Laplacian Exponential]].

Definitions and notation are collected in the [[Core specification|core specification]], and names and terminological distinctions in [[PMG terminology|PMG terminology]]. The results on coupling variations from the introductory series are not required for the main route.

## Notes in the series

1. **[[Spaces, Subspaces, and the Choice of a Basis]].** We distinguish the linear space of formal vertices, the space of affine vectors, and the affine space of points. Selected vertices generate subspaces; a basis lets us write their exterior elements and forms. Metric evaluations are obtained through potentials of forms.

2. **[[The Null Vector, Isotropic Representation, and the Boundary]].** We construct an isotropic model with local points and a correction selecting the center of a normalized element. The distinguished null vector connects affine weight, flat geometry, and the boundary operator. This note develops the geometric part of the series; its constructions are also used in the section on isotropic coordinates.

3. **[[Projections, Bi-coordinates, and Di-coordinates]].** Bi-coordinates specify an expansion of an object in chosen elements; di-coordinates are inner products with those elements. We consider frames, coordinates of a projection, and uniqueness conditions. We decompose quadratic and polar forms using frame elements and their differences, and express projection through polyforms.

4. **[[Vertex Contraction and Graph Gluing]].** Identifying vertices produces a space that can be realized as an orthogonal subspace of the original one. Gluing at a single vertex joins the spaces of the components. The Laplacian exponential describes independent components and their combination; under single-vertex gluing, spanning-tree coefficients multiply and metric masses add.

5. **[[Selected Vertices and the Dirichlet Problem]].** We prescribe values at selected vertices and extend them with minimum energy. The extension coefficients are the bi-coordinates of projections and form the influence matrix. The metric of residuals is computed through the polyform of a contracted graph. We state the conditions that ensure uniqueness.

6. **[[Vertex Elimination and Induced Couplings]].** We construct a graph on selected vertices that preserves effective resistances between them, minimum energy, and response. Decomposition of the Laplacian and factorization of its exponential explain preservation of the metric. The Schur complement gives the matrix form of elimination; projection of the circumcenter lets us compare the masses of the original and induced graphs.

7. **[[Couplings Within One Part of a Bipartite Graph]].** We apply vertex elimination to a rectangular table of couplings. The Laplacians of projection frames define induced couplings within the chosen part. We compare the two possible induced graphs, define a common normalized spanning-tree parameter of the original graph, and explain why the masses of the parts generally do not add up.

## Reading routes

**For the full series:** follow the order above. Examples explain the constructions, while collapsible proofs give general derivations. Conditions on connectivity, nondegeneracy, and the presence of selected vertices in each component are stated where they are needed.

**Graphs and applications:** start with [[Spaces, Subspaces, and the Choice of a Basis|spaces and the choice of a basis]], then move to [[Projections, Bi-coordinates, and Di-coordinates|projections and coordinates]]. Continue with [[Vertex Contraction and Graph Gluing|contraction and gluing]], [[Selected Vertices and the Dirichlet Problem|the Dirichlet problem]], [[Vertex Elimination and Induced Couplings|vertex elimination]], and [[Couplings Within One Part of a Bipartite Graph|the bipartite application]]. The isotropic extension is not required for this route.

**Isotropic geometry:** after [[Spaces, Subspaces, and the Choice of a Basis|spaces and the choice of a basis]], read about [[The Null Vector, Isotropic Representation, and the Boundary|the null vector and the boundary]], then [[Projections, Bi-coordinates, and Di-coordinates|coordinates]], including the section on [[Projections, Bi-coordinates, and Di-coordinates#Coordinates in the isotropic extension|the isotropic extension]]. The main part of the coordinates note builds on spaces and the metric; the null vector is needed for its isotropic constructions and the example of a degenerate subspace.

## Continuations and sources

Spectral relations between the parts of a bipartite graph, gluing at several vertices, a fuller treatment of Lorentzian geometry, and possible physical interpretations are reserved for separate notes. General polyform reduction and the spanning-tree operator also belong to a separate continuation. These questions and their dependencies are tracked in the [[Карта библиотеки PMG|library map (in Russian)]].

Sources and the status of results are given in each note. Established constructions are compared with their presentation in PMG after the objects involved have been defined.

