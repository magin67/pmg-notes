---
title: "PMG — Research Notes"
description: "The foundations of resistance geometry and the development of polyform algebra."
lang: en
translation_key: pmg-home
revision: 30
translated_revision: 29
updated: 2026-11-02
---

[Русский](../ru/index.md) · [Choose a language](../index.md)

**Polyform Metric Geometry (PMG)** is a research project devoted to polyform algebra and its connections with geometry, graph theory, and electrical networks.

The library brings together established results, explanations of basic concepts, and research within PMG. Its aim is to help readers build a conceptual foundation and see the connections between objects that are often studied separately: Laplacians, potentials, effective resistances, metric forms, and spanning forests.

The approach is based on polyform algebra. One of the questions that led to its development was how changing one or more couplings affects the properties of an entire system. Products of forms and the Laplacian exponential in this algebra describe the joint effects of couplings and the resulting metric and combinatorial characteristics.

## Getting started and foundations

[[en/Getting Started and Foundations/Getting Started and Foundations|Getting Started and Foundations]] brings together the introductory series, specification, terminology, and general reading routes.

## Thematic sections

The library contains 17 completed bilingual series: 123 substantive notes in each language. Each series has one primary home, chosen by its main question. Section pages provide descriptions, prerequisites, reading routes, and connections.

- **[[en/Polyform Algebra and Combinatorics/Polyform Algebra and Combinatorics|Polyform Algebra and Combinatorics]]**. What objects does polyform algebra construct, which identities do they satisfy, and what do their coefficients count?
- **[[en/Resistance Geometry and Duality/Resistance Geometry and Duality|Resistance Geometry and Duality]]**. How are spaces, the resistance metric, geometric characteristics, and dual representations organized?
- **[[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]]**. Which features of a graph do its characteristics and decompositions retain? What can be reconstructed from them?
- **[[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]**. How do characteristics change when couplings vary, vertices are eliminated, or a graph is assembled from parts?
- **[[en/Directed Graphs and Extensions/Directed Graphs and Extensions|Directed Graphs and Extensions]]**. What changes when couplings become directed and constructions become nonsymmetric?

[[en/Thematic Index|All series and their primary homes]] · [[en/Cross-cutting Tags|Cross-cutting Tags]].

## Programming examples

[[en/PythonExamples/PythonExamples|Programming Examples]] connect the mathematical notes to executable `polyform_algebra` code, expected results, and checks.

## Development plan

The [[ru/Карта библиотеки PMG|library map, in Russian]] records research directions, preparation status, and open questions. [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]] completes the current bilingual series of nine substantive notes on spectral differences, boundary transfer, decoding, response, and periodic chains. The navigator separates proofs, finite computations, and conjectures. All notes, the navigator, and labels for 35 figures are available in English.

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
- Library last updated: **1 November 2026**
