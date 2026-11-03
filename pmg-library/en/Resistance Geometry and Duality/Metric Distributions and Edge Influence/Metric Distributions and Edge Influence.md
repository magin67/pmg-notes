---
title: Metric Distributions and Edge Influence
date: 2026-11-03
updated: 2026-11-03
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 6
translation_key: metric-distributions-navigation
order: 0
tags:
  - resistances
  - variations
  - reconstruction
description: "From coupling influence on the value of a form to metric distributions, path intersections, and higher grades."
---

[[ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/Метрические распределения и влияние связей|Русский]]


Change one conductance and compare the values of a fixed form before and after the change. In grade one, the relative-sensitivity coefficients of existing edges form the metric distribution $D_L$; their sum equals the original value of the form. On a tree, the support of the distribution of the inner product of two vectors specified by vertex pairs selects the common segment of their paths.

In higher grades, the distribution is indexed by edge sets. The field of individual-edge influences is obtained by summing contributions of sets and does not in general determine them in reverse. The series follows this passage from the intersection of two paths to the norms of triangle boundaries and exterior objects of any grade.

The primary home of this series is [[en/Resistance Geometry and Duality/Resistance Geometry and Duality|Resistance Geometry and Duality]]. A secondary entry point is [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]: the influence field connects the distribution to changes of metric.

## Available notes

1. [[Edge Influence and Metric Distribution]]. Adding conductance, finite influence, the passage to relative sensitivity, and the derivation of $D_L$. The distinction between a coefficient sum and the metric evaluation of the output form.

2. [[Path Intersection as an Influence Field on a Tree]]. The common segment as the exact support of existing-edge influence; directions, conductances, and independent finite probes.

3. [[The Influence Field on Graphs with Cycles]]. Distribution through two flows, signed cancellation, a cross-edge with zero influence, and network refinement.

4. [[Metric Distribution in Higher Grades]]. The norm of a triangle boundary, distribution over edge pairs, sums giving individual-edge influences, and the general rule for grade $k$.

The series is available in Russian and English: four substantive notes, this navigator, and 12 figures in each language.

## Prerequisites

The prerequisites are [[Laplacian - graph, electrical network and quadratic form]], [[Basic Objects and Operations of Polyform Algebra]], and [[Laplacian Exponential]]. The mechanism of changing one exponential factor is described in [[One Changing Edge]]. Triangle boundaries use [[Metric of Higher-Grade Objects]].

## Main distinctions

Finite influence depends on the amount of added conductance. A grade-one coefficient of $D_L$ expresses sensitivity to a relative change of an existing edge. Adding an absent coupling is allowed, but its influence is not determined by that coupling's zero coefficient in the initial distribution.

In grade $k$, the distribution is indexed by sets of $k$ edges; its coefficients sum to the value of the form. The relative-sensitivity coefficient of one edge is obtained by summing over all sets containing it. These edge coefficients therefore sum to $kN_L(f)$; at $k=1$ they coincide with the coefficients of the distribution itself. Pair contributions are not mixed second derivatives.

The input form is fixed in each comparison. All independent probes use the same initial metric. Accumulating changes defines a different procedure. Finite increments generally do not add; in higher grades, this failure already occurs on a tree.

Historically, the subject arose from path intersections and polyform transformations. This series studies one metric distribution; its definition is not identified with spanning-tree averaging or with a distribution over forests of complementary grade.

## Results and origins

| Result | Source or derivation | Role in PMG | Status |
|---|---|---|---|
| Finite influence of one coupling | Exponential factor and normalization in Edge Influence and Metric Distribution; the matrix formula for one variation | The initial procedure for measuring influence | Proved; no novelty claim |
| Grade-one coefficients of $D_L$ | Relative sensitivity; electrical energy and its polarization | Assembling metric contributions into a form | Definition and derivation from known identities |
| Grade-one coefficient sum equals the value of the form | Homogeneity of degree $-1$ and Euler's identity | Justification of the distribution's normalization | Proved |
| Path intersection as the support of influence | Orthogonality of the edge basis of a tree and the relative-sensitivity formula | Signed selection of the common segment with edge resistances | Proved in the tree note; no novelty claim |
| Two flows on a graph with cycles | The energy identity of a resistive network and its polarization | Signs of contributions, zero response, and consistency under refinement | Classical basis; examples checked exactly |
| Distribution in higher grades | Exterior powers of the metric and the Cauchy-Binet formula; Stanley, Theorem 9.4 | Edge sets in place of individual edges; preservation of grade | Definition and derivation from a classical identity |
| Edge sums in higher grades | The Parseval identity for contractions and variation of the normalized potential | Exact influence of one coupling; sum $kN_L(f)$ | Proved; no novelty claim |

Detailed proofs and references to classical sources are given in [[Edge Influence and Metric Distribution]], [[Path Intersection as an Influence Field on a Tree]], [[The Influence Field on Graphs with Cycles]], and [[Metric Distribution in Higher Grades]].
