---
title: Polynomial Toponomes
date: 2026-10-23
updated: 2026-10-30
revision: 2
source_revision: 9
status: draft
text_prepared_by: ChatGPT
translation_key: polynomial-toponomes-series-navigation
lang: en
description: "Polynomial reductions of forest toponomes: normalizations, Laplacian coefficients, Kirchhoff indices, reducibility, and graph realizability."
order: 0
---

This series continues [[Partition Toponomes]] and studies polynomial reductions through their coefficients. The main question is which graph parameters these coefficients express and how their meaning depends on normalization.

## Reading order and series status

The series is complete in its current form of five substantive notes, with Russian and English versions available.

1. **[[Vector and Vertex Normalizations of Toponomes]].** Original forest coefficients and root weights; passage to one-variable and two-variable polynomials; triangles of the path $P_6$; multiplication under disjoint union; and preservation of structural identities.
2. **[[Forest Coefficients and the Laplacian Polynomial]].** Principal minors and forests with prescribed roots; proof of $P_G(t)=\det(I+t\mathbf L)$; first and highest coefficients. Roots, factorization, and component count; the complete graph and Abel polynomials. A full analysis of $C_4$ and a weighted example.
3. **[[Coefficients and Kirchhoff Indices]].** Two-forest sums and resistances; the Kirchhoff index from the ratio of the two highest coefficients; root sums and reciprocal spectral sums; and the relation to the resistance radius. A path and a star illustrate the distinction between normalizations.
4. **[[Reducibility of Toponomes]].** Irreducibility of full and two-variable toponomes of a connected graph with edges; factorization by independent components; irreducibility of the full forest toponome and its coefficient table under the second-kind product; and new factors after passage to one variable.
5. **[[Graph Realizability of Toponomes]].** The inverse question: which coefficients come from a graph? Necessary conditions, a nonrealizable triangle, Mason's theorem on forest counts with sources, an exact system of equations, and a complete criterion for the weighted vertex polynomial.

## Main results

- **The forest and matrix constructions coincide.** Vertex reduction of the canonical forest expansion of the exponential gives the same polynomial as $\det(I+t\mathbf L)$. Principal minors explain this equality through forests with prescribed roots.
- **Normalization determines the meaning of coefficients.** Vector evaluation retains forest weights; vertex evaluation incorporates root choices in the components. For a connected graph on $n\geqslant2$ vertices, the two highest vertex coefficients give the Kirchhoff index: $Kf(G)=n\,p_{n-2}/p_{n-1}$. The relation to the resistance radius also requires the position of the circumcenter.
- **Reducibility depends on the product and reduction.** Under ordinary multiplication, full and two-variable toponomes factor by components with edges. Under the second-kind product, nonempty forest toponomes and tables are irreducible; one-variable reductions have different properties.
- **Graph realizability is a separate problem.** Necessary coefficient tests and Mason's theorem do not replace a complete criterion. The exact system in edge variables gives an existence criterion; a spectral criterion is provided for the one-variable vertex polynomial with arbitrary positive conductances.

## Prerequisites

Required concepts are the [[From Polyforms to Partitions|toponome of a chosen representation]], the [[Toponomes and Structural Identities|distinction between a representation and a polyform]], and [[Coefficient Tables of Toponomes|grouping types by two parameters]]. The forest expansion is established in [[Laplacian Exponential]]. Conventions for objects and norms are recorded in the [[Core specification|specification]] and [[PMG terminology|terminology]].

## Scope and continuations

The series concerns undirected graphs with positive conductances. Requirements of unit conductances and connectivity are stated in the relevant results. Irreducibility always refers to the specified product and coefficient field; an edgeless graph gives the unit.

Balanced graphs are reserved for a separate future series: first balance, potentials, and circulation; then the bilinear exponential and directed forests; and then toponomes, normalizations, and the characteristic polynomial. That continuation must establish the correspondence between forest grouping and reduction of the full bilinear exponential, and determine which results require symmetry. The plan is recorded in the [[ru/Карта библиотеки PMG#Серия «Балансовые графы»|“Balanced Graphs” section of the library map (in Russian)]].

Basic root properties are treated here as polynomial characteristics. Full diagonalization of a polyform, eigenvectors, and spectral subspaces remain a separate continuation. Toponomes of the dual polyform follow introduction of the dual construction itself; the [[Карта библиотеки PMG|PMG library map (in Russian)]] records the status of these topics.
