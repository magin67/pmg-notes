---
title: "Programming Examples"
date: 2026-10-29
updated: 2026-11-10
revision: 10
translated_revision: 10
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

## How an example is organized

Problem and diagram → mathematical objects → calculation with `polyform_algebra` → expected results → independent check. Run each note’s fragments in order. NumPy and direct enumeration are used where they provide a separate way to check the answer.

## Version and ready-to-run notebooks

All examples in this section were checked with `polyform_algebra 0.9.0` on Python 3.12. The shared guide covers installation; version information is updated together with checks of both language editions.

The weighted-chain notebook includes explanations, formulas, a diagram, and saved results:

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb)

The other examples currently provide executable fragments in the notes. A calculation for one case does not prove a general formula. Program capabilities should be distinguished from the general model in the [[Core specification|PMG specification]].


## Symbolic calculations

[[Example - Path P5 and Cycle C4 Exponentials|Path and cycle exponentials]]: named vertices, products of forms, and the full grade decomposition of the exponential. A separate notebook displays the polyforms themselves; numerical evaluations are kept in a final section.

[Open the symbolic notebook in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symbolic-polyforms.ipynb)
