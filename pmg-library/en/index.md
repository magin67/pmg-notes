---
title: "PMG — Research Notes"
description: "The foundations of resistance geometry and the development of polyform algebra."
lang: en
translation_key: pmg-home
revision: 17
translated_revision: 19
updated: 2026-10-29
---

[Русский](../ru/index.md) · [Choose a language](../index.md)

**Polyform Metric Geometry (PMG)** is a research project devoted to polyform algebra and its connections with geometry, graph theory, and electrical networks.

The library brings together established results, explanations of basic concepts, and research within PMG. Its aim is to help readers build a conceptual foundation and see the connections between objects that are often studied separately: Laplacians, potentials, effective resistances, metric forms, and spanning forests.

The approach is based on polyform algebra. One of the questions that led to its development was how changing one or more couplings affects the properties of an entire system. Products of forms and the Laplacian exponential in this algebra describe the joint effects of couplings and the resulting metric and combinatorial characteristics.

## Introductory series

Ten notes introduce the Laplacian, resistance geometry, coupling variations, and polyform algebra.

- [[PMG Introductory Series|Reading order and brief descriptions of the notes]].
- [[Further Reading for the PMG Introductory Series|Recommended reading]].

## Spaces and subspaces

Eight notes on choosing a subspace, the null vector, coordinates, and graph operations. The series connects the geometric description with the Dirichlet problem and the construction of couplings within one part of a bipartite graph.

- [[Spaces and Subspaces in PMG|Notes, prerequisites, and reading routes]].

## Metric parameters of graphs

Five notes on resistance radius and diameter, vertex centralities, dimensionless graph characteristics, and two types of vertex removal. The radius, volumes, and spanning-tree characteristics are expressed through polyforms.

- [[Metric Parameters of Graphs|Notes, reading routes, and a guide to results]].

## Structural identities

Five notes on dependencies among partition forms. The main results are the noncrossing basis and its dimension, completeness of the four-block identity, the graph gluing formula, and decomposition of relations by supports.

- [[en/Structural identities/Structural Identities|Main results, reading order, and descriptions of the notes]].

## Symmetric polyforms

Five notes on symmetry of forms under vertex permutations. The main result is the fundamental theorem of SPFs: a symmetric sum of any admissible type is expressed through the principal polyform of the same grade with an explicit coefficient. Consequences cover products and powers, the exponential of the complete graph, and Abel polynomials.

- [[en/Symmetric polyforms/Symmetric Polyforms|The fundamental theorem, its consequences, and reading order]].

## Combinatorial potentials

Six notes on ordinary and cyclic partitions and counting by component sizes. The series introduces the potentials of the first and second kinds, distinguishes SPF representation sizes from forest counts, proves the Cayley-Moon formula for joining prescribed components, and explains falling-factorial expansions through rooted forests and $r$-Stirling numbers. The potential of path-and-cycle states relates arc labels to graph and construction-history counts.

- [[en/Combinatorial potentials/Combinatorial Potentials|Main results, notation, and reading routes]].

## Partition toponomes

Six notes on passing from a chosen polyform representation to partition types. The series establishes the limits of the reduction, introduces the second-kind algebra and its graph interpretations, develops coefficient triangles, and shows why they do not distinguish all graphs.

- [[en/Partition toponomes/Partition Toponomes|Main results, reading order, and scope]].

## Polynomial toponomes

Five notes on polynomial reductions of partition toponomes. Vector and vertex normalizations are compared through forest weights; the vertex reduction of the exponential is proved to equal the determinant of $I+t\mathbf L$. Coefficient ratios express the Kirchhoff index and reciprocal spectral sums and relate the polynomial to the centroid and resistance radius. The series also examines reducibility under different products and graph realizability of toponomes.

- [[en/Polynomial toponomes/Polynomial Toponomes|Contents and reading order]].

## Balanced graphs

Twelve notes extend PMG to balanced directed graphs. They develop the bilinear Laplacian and its exponential, circulation forms, one-way resistance, directional coordinates and the sphere, graph balancing, directed forest toponomes, and permutation digraphs. Definitions and algebraic results precede geometric, electrical, and probabilistic interpretations.

- [[en/Balanced graphs/Balanced Graphs|Main results, reading order, and five reading routes]].

## KVP decomposition and oriented extensions

Nine notes on separating pair characteristics into an overall level, vertex heterogeneity, residual pair structure, circulation, and directional imbalance. The series develops the projectors, graph examples, the distance transformation, Green and resistance components, applications, metric parameters, the second-order symmetric potential, and forest toponomes. Proved results are distinguished from computational examples and open questions.

- [[KVP Decomposition and Oriented Extensions|Main results, reading order, and five reading routes]].

## Greenian and Polyform Duality

Nine notes on the Laplacian and Greenian as vector forms, mutual duality of their exterior exponentials, canonical coefficients and signed forests, cut representations, vertex variations, metric potentials, symmetric identities, and toponomes. Exact examples include complete graphs, stars, cycles, weighted paths, and the Petersen graph.

- [[en/Greenian and polyform duality/Greenian and Polyform Duality|Main results, reading order, normalizations, and reproducible checks]].

## Matroid parameters and forest characteristics of graphs

Seven notes explain which graph characteristics are determined by the cycle matroid and how to compute them. Forest coefficients are developed on both sides of Laplacian-Greenian duality, followed by normalized power sums, resistance scales, edge probabilities, and the forest formula for the resistance radius. One-point gluing and Whitney twists establish the scope and limits of invariance.

- [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Definitions, reading routes, main results, and reproducible checks]].

## Python examples

Executable examples show how to reproduce calculations from the notes with `polyform_algebra`. The first companion covers strengthening one and two couplings of a triangle.

- [[en/PythonExamples/PythonExamples|Programming examples: code, expected results, and checks]].

## PMG Foundations

- [[Core specification|Core specification]]: definitions, notation, fundamental identities, and applicability conditions.
- [[PMG terminology|Terminology]]: English and Russian terms, naming conventions, and distinctions between related concepts.

## Research topics

As the library grows, collections will be prepared on the following topics:

- **Geometric representations:** points and vectors, the Gram matrix of isotropic point representatives, the distinguished null vector, and bi- and di-coordinates.
- **Polyform algebra:** grades, potentials and norms, symmetric polyforms, and dual constructions.
- **Forests, cuts, and toponomes:** combinatorial coefficients, generating polynomials, and their reductions.
- **Graph spectra:** Laplacians of paths and cycles, and spectral properties of graph configurations.
- **Graph gluing and invariants:** gluing constructions, chains of cores, preserved characteristics, and the limits of their invariance.

Each collection will include a brief reading guide: what it covers, what background is needed, and which order to follow. A note may belong to more than one reading route.

## Status of results

Established results are presented with references to their sources. Research claims state their conditions of applicability and the strength of their justification:

- **Proved:** a general proof is provided in the note or available through a precise reference.
- **Computed directly:** the result has been obtained for a particular configuration.
- **Checked on examples:** checks have been performed in several cases; they do not replace a general proof.
- **Working conjecture:** a general claim is proposed but has not yet been proved.
- **Tentative interpretation:** an interpretation requires further justification.

The status applies to an individual claim: proved results and open questions may appear in the same note. Computational checks are accompanied by a description of the method and the scope of the checks.

Terms introduced or redefined within PMG are explained when first used. If a definition differs from the one used in another field, this is stated explicitly.

## About the project

**Project founder and library editor:** Dmitry Malugin.

The project is developed with the participation of **ChatGPT (OpenAI)** as an AI research assistant. Its role includes discussing problems, developing candidate proofs, searching for counterexamples, and preparing computational code, texts, and translations. The library editor selects the material and approves published versions. Substantial AI contributions to individual materials are acknowledged in the corresponding notes.

---

The approach developed through the study of object ranking, electrical networks, and the geometric properties of graphs. Work with Laplacians, Green matrices, and effective resistances led to resistance geometry. The study of coupling variations was the next stage and led to the construction of polyform algebra.

The library grows through small thematic collections. The Russian text serves as the basis for the English translation; links between language versions are added as the translations become available.

- Project started: **2026**
- Library last updated: **29 October 2026**
