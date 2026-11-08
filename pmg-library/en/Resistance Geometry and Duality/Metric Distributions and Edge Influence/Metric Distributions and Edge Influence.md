---
title: Metric Distributions and Edge Influence
date: 2026-11-03
updated: 2026-11-08
revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 7
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

1. **What does one coupling change?** [[Edge Influence and Metric Distribution]]: from a finite probe to sensitivity and the operator $D_L$.
2. **Why does a tree select path intersection?** [[Path Intersection as an Influence Field on a Tree]]: shared edges, directions, conductances, and side branches.
3. **What do cycles change?** [[The Influence Field on Graphs with Cycles]]: splitting flows, signed contributions, zero influence, and simultaneous changes.
4. **Why are edge pairs and sets needed?** [[Metric Distribution in Higher Grades]]: from a minimal grade-two example to the general definition.

The series is available in Russian and English: four substantive notes, this navigator, and 17 figures in each language.

## Prerequisites

The prerequisites are [[Laplacian - graph, electrical network and quadratic form]], [[Basic Objects and Operations of Polyform Algebra]], and [[Laplacian Exponential]]. The mechanism of changing one exponential factor is described in [[One Changing Edge]]. Triangle boundaries use [[Metric of Higher-Grade Objects]].

## Reading the notation

| Notation | Meaning |
|---|---|
| $N_L(f)$ | Numerical value of a fixed form $f$ in metric $L$ |
| $\Delta_\ell(t;f)$ | Finite change of that value when conductance $t$ is added to coupling $\ell$ |
| $m_J(f)$ | Contribution of a set $J$ of $k$ edges; at $k=1$, a single-edge contribution |
| $A_\ell(f)$ | Sensitivity to a relative conductance change: $-c_\ell\partial N_L(f)/\partial c_\ell$ |
| $D_{L,k}$ and $D_{L,k}(f)$ | The distribution operator and its assembled output form; in grade one, write $D_L$ |

The coefficients $m_J$ sum to $N_L(f)$, not to one. Mixed forms can have negative coefficients. Thus “distribution” here does not mean a probability distribution.

![From a Probe to a Distribution](<images/From a Probe to a Distribution.svg>)

*In grade one, an edge contribution equals its sensitivity. In higher grades, sensitivity is the sum of contributions of sets containing that edge.*

## Main distinctions

Finite influence depends on the amount of added conductance. A grade-one coefficient of $D_L$ expresses sensitivity to a relative change of an existing edge. Adding an absent coupling is allowed, but its influence is not determined by that coupling's zero coefficient in the initial distribution.

In grade $k$, the distribution is indexed by sets of $k$ edges; its coefficients sum to the value of the form. The relative-sensitivity coefficient of one edge is obtained by summing over all sets containing it. These edge coefficients therefore sum to $kN_L(f)$; at $k=1$ they coincide with the coefficients of the distribution itself. Pair contributions are not mixed second derivatives.

The input form is fixed in each comparison. All independent probes use the same initial metric. Accumulating changes defines a different procedure. Finite increments generally do not add; in higher grades, this failure already occurs on a tree.

Historically, the subject arose from path intersections and polyform transformations. This series studies one metric distribution; its definition is not identified with spanning-tree averaging or with a distribution over forests of complementary grade.

## Results and origins

The construction uses classical resistance metrics, inverse-matrix variations, and exterior algebra. These connections are expressed in PMG notation; no scientific priority is claimed.

> [!info]- Sources and status of the results
>
> | Result | Source or derivation | Role in PMG | Status |
> |---|---|---|---|
> | Finite influence of one coupling | Exponential factor and normalization in Edge Influence and Metric Distribution; the matrix formula for one variation | The initial procedure for measuring influence | Proved |
> | Grade-one coefficients of $D_L$ | Relative sensitivity; electrical energy and its polarization | Assembling metric contributions into a form | Definition and derivation from known identities |
> | Grade-one coefficient sum equals the value of the form | Homogeneity of degree $-1$ and Euler's identity | Justification of the contribution sum | Proved |
> | Path intersection as the support of influence | Orthogonality of the edge basis of a tree and the relative-sensitivity formula | Signed selection of the common segment with edge resistances | Proved in the tree note |
> | Two flows on a graph with cycles | The energy identity of a resistive network and its polarization | Signs of contributions, zero response, and consistency under refinement | Classical basis; examples checked exactly |
> | Distribution in higher grades | Exterior powers of the metric and the Cauchy-Binet formula; Stanley, Theorem 9.4 | Edge sets in place of individual edges; preservation of grade | Definition and derivation from a classical identity |
> | Edge sums in higher grades | The Parseval identity for contractions and variation of the normalized potential | Exact influence of one coupling; sum $kN_L(f)$ | Proved |

Detailed proofs and references to classical sources are given in [[Edge Influence and Metric Distribution]], [[Path Intersection as an Influence Field on a Tree]], [[The Influence Field on Graphs with Cycles]], and [[Metric Distribution in Higher Grades]].
