---
title: "Programming Examples"
date: 2026-10-29
updated: 2026-11-11
revision: 22
translated_revision: 22
status: draft
text_prepared_by: ChatGPT
translation_key: programming-examples
lang: en
description: "Reproducible PMG calculations with the Polyform Algebra Python library."
order: 0
folder_order: 70
---

This section connects the mathematical PMG notes with executable examples from `polyform_algebra`. Each companion note states the problem, maps notation to code, gives expected results, and describes independent checks.

[[ru/PythonExamples/PythonExamples|Русский]]

## Library navigation

[[en/Getting Started and Foundations/Getting Started and Foundations|Getting Started and Foundations]] · [[en/Thematic Index|Thematic Index]].

## Getting started

[[Installing the Library and Running Examples]]: local installation, library use, running programs and tests, and working in Google Colab.

## First examples

[[Example - Weighted Chain]] starts with a graph and its conductances: the Laplacian, exponential, resistances, currents, and power. This is the recommended first calculation.

[[Example - Unit Triangle Geometry]] demonstrates edge inner products, quadratic boundary norm, and area, with Gram-matrix and coordinate checks.

[[Example - Triangle Coupling Variations]] reproduces the strengthening of one and two couplings of a unit triangle from [[Variation of a Single Edge]] and [[Varying several couplings together]]. Edge factors update the metric polyform; formulas and direct matrix calculations check the results.

Prerequisites: [[en/Getting Started and Foundations/Introduction/PMG Introductory Series|PMG Introductory Series]], particularly [[Basic Objects and Operations of Polyform Algebra]] and [[Laplacian Exponential]].

[[Example - Path P5 and Cycle C4 Exponentials]] covers exponential grades, forest weights, spanning-tree coefficients, and resistances of the path and cycle.

[[Example - Deleting an Edge and a Bridge]] compares cycle-edge and bridge deletion: resistance changes, preservation of isolated vertices, and unavailable global normalization after disconnection.

## Spaces

[[en/PythonExamples/Example - Subspaces and Graph Transformations|Subspaces and Graph Transformations]] - potentials, bi- and di-coordinates, Dirichlet extension, contraction, and elimination. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/spaces.ipynb).

## Metric Parameters of Graphs

[[en/PythonExamples/Example - Metric Parameters of Graphs|Metric Parameters in Python]]. Eight calculations from the notes in this series. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/metric-parameters.ipynb).

## Structural Identities

[[en/PythonExamples/Example - Checking Structural Identities|Structural Identities in Python]]. Five exact checks from the notes in this series. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/structural-identities.ipynb).

## Symmetric Polyforms

[[en/PythonExamples/Example - Checking Symmetric Polyform Identities|Checking symmetric polyform identities]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symmetric-polyforms.ipynb).

## Combinatorial Potentials

[[en/PythonExamples/Example - Combinatorial Potentials|Combinatorial Potentials]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/combinatorial-potentials.ipynb).

## Partition Toponomes

[[en/PythonExamples/Example - Partition Toponomes|Partition Toponomes]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/partition-toponomes.ipynb).

## Polynomial Toponomes

[[en/PythonExamples/Example - Polynomial Toponomes|Polynomial Toponomes]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/polynomial-toponomes.ipynb).

## Balanced Graphs

[[en/PythonExamples/Example - Balanced Graphs|Balanced Graphs]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/balanced-graphs.ipynb).

## KVP Decomposition

[[en/PythonExamples/Example - KVP Decomposition|KVP Decomposition]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/kvp-decomposition.ipynb).

## Greenian and Polyform Duality

[[en/PythonExamples/Example - Greenian and Polyform Duality|Greenian and Polyform Duality]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/greenian-duality.ipynb).

## Matroid Parameters and Forest Characteristics of Graphs

[[en/PythonExamples/Example - Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/matroid-forest-characteristics.ipynb).

## Boundary Data and Chains of Cores

[[en/PythonExamples/Example - Boundary Data and Chains of Cores|Boundary Data and Chains of Cores]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/boundary-data-core-chains.ipynb).

## How an example is organized

Problem and diagram → mathematical objects → calculation with `polyform_algebra` → expected results → independent check. Run each note’s fragments in order. NumPy and direct enumeration are used where they provide a separate way to check the answer.

## Version and ready-to-run notebooks

The introductory and Spaces examples use the `v0.9.0` tag. Later notebooks install the package commits pinned in their examples.

The weighted-chain notebook includes explanations, formulas, a diagram, and saved results:

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb)

A calculation for one case does not prove a general formula. Program capabilities should be distinguished from the general model in the [[Core specification|PMG specification]].


## Symbolic calculations

[[Example - Path P5 and Cycle C4 Exponentials|Path and cycle exponentials]]: named vertices, products of forms, and the full grade decomposition of the exponential. A separate notebook displays the polyforms themselves; numerical evaluations are kept in a final section.

[Open the symbolic notebook in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symbolic-polyforms.ipynb)
