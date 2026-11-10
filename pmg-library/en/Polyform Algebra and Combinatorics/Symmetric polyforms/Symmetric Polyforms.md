---
title: Symmetric Polyforms
date: 2026-10-20
updated: 2026-11-10
revision: 5
source_revision: 7
status: draft
text_prepared_by: ChatGPT
translation_key: symmetric-polyforms-series-navigation
lang: en
description: "The fundamental theorem of SPFs as the main result of the series: exact normalization, proof, product rules, the complete-graph exponential, and Abel polynomials."
order: 0
tags:
  - partitions
  - forests-and-spanning-trees
aliases:
  - "en/Symmetric polyforms/Symmetric Polyforms"
  - "en/Symmetric polyforms/index"
---

What happens to a sum of forms when all vertices are relabelled? This series studies sums preserved by every permutation. Its main theorem replaces a symmetric sum of any admissible type by a numerical multiple of the principal polyform of the same grade. This simplifies multiplication and the counting of forest contributions.

## Place in the library

Primary section: [[en/Polyform Algebra and Combinatorics/Polyform Algebra and Combinatorics|Polyform Algebra and Combinatorics]].

[[en/Cross-cutting Tags|Cross-cutting Tags]] · [[en/Thematic Index|Thematic Index]].

## Prerequisites

The prerequisites are [[Basic Objects and Operations of Polyform Algebra|boundaries, grades, and multiplication of forms]], together with [[Partition Forms and the Tetrahedron Identity|partition forms and the tetrahedron identity]]. The proof of the noncrossing basis is not required for the main route.

Graph applications use the [[Laplacian Exponential|Laplacian exponential]]. Partition counts are explained by the [[Partitions and the Combinatorial Potential of the Second Kind|combinatorial potential of the second kind]]; its [[Combinatorial Potentials in Symmetric Polyforms|application to SPFs]] can be read alongside this series.

## Reading order

1. **[[Symmetric Polyforms - Types and Normalizations|Types and normalizations]].** How is a type obtained from a partition, and how is each term counted once? Figures explain blocks, grades, and repetition under permutations.
2. **[[Fundamental Theorem of Symmetric Polyforms]].** Why are symmetric sums of different types but the same grade proportional? A five-vertex example precedes the general formula and proof.
3. **[[Products and Powers of Symmetric Polyforms]].** How are SPFs multiplied? Three cases of block intersection lead to a four-vertex calculation and a polynomial in one generator.
4. **[[Symmetric Polyforms of the Complete Graph]].** How are partitions related to forests? Three trees for one block, a table for $K_5$, and obtaining $C_4$ by deleting diagonals.
5. **[[Forest Coefficients and Abel Polynomials]].** What do the resulting numbers count? Adding and deleting roots connects them to groups of components and Abel polynomials.

The notes on types and the fundamental theorem suffice for the main result. The graph route continues through products and the complete graph; the combinatorial route continues through forest coefficients.

![From Partitions to Forest Coefficients](<images/From Partitions to Forest Coefficients.svg>)

The route shows how the topics depend on one another. The main algebraic result precedes graph applications and numerical counting.

## Main result: the fundamental theorem of SPFs

At each grade, symmetric polyforms on boundaries form a single direction: every one is a multiple of the principal polyform $E_n[k]$. For example,

$$
E_5[2,1]=3E_5[3]
$$

The left side sums the forms of ten partitions into a triple and a pair; the right side contains five partitions into a quadruple and a singleton, each with coefficient $3$. This is an equality of forms, so the numbers of terms may differ.

The [[Fundamental Theorem of Symmetric Polyforms#Statement and scope|general formula]] gives the coefficient for every admissible type. The main proof uses a quadratic zero-sum identity and block merging; the idea of this proof is due to Dmitry Malyugin, with the exposition prepared by ChatGPT.

## Consequences and applications

The [[Products and Powers of Symmetric Polyforms#A single generator|SPF algebra]] is described by polynomials with the rule $t^n=0$. For the complete graph, this yields a [[Symmetric Polyforms of the Complete Graph#The Laplacian and exponential of the complete graph|short exponential expansion]], whose top grade gives Cayley's formula. Comparison with the forest expansion leads to [[Forest Coefficients and Abel Polynomials#The expansion of Abel polynomials|Abel polynomials]]. The general count of ways to join prescribed components is given in a [[Cayley's Theorem and Joining Prescribed Components|separate combinatorial note]].

## Programming companion

[[en/PythonExamples/Example - Checking Symmetric Polyform Identities|Checking symmetric polyform identities]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symmetric-polyforms.ipynb).

## Status and scope of the series

The identities of forms are proved before a metric is chosen; computations on small examples supplement the proofs. Representation size, coefficient sum, and metric evaluation are distinct. Notation follows the [[Core specification|core specification]] and [[PMG terminology|terminology]].

The main proof works with partition forms. [[Fundamental Theorem of Symmetric Polyforms#Correspondence with classical representation theory|Representation theory]] explains the extension to all forms on boundaries and belongs to the additional route. Cayley's formula, Abel polynomials, and their connection with Stirling numbers are classical results; the notes identify their sources and the passage to PMG notation.

Full symmetry means all permutations of the specified vertex set. The complete-graph formulas concern unit or equal conductances. Symmetries of an arbitrary graph, toponomes, and duality of exponentials require their own setups and do not follow automatically from this series.
