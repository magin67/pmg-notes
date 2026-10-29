---
title: "Programming Examples"
date: 2026-10-29
updated: 2026-10-29
revision: 2
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: programming-examples
lang: en
description: "Reproducible PMG calculations with the Polyform Algebra Python library."
order: 0
---

This section connects the mathematical PMG notes with executable examples from `polyform_algebra`. Each companion note states the problem, maps notation to code, gives expected results, and describes independent checks.

[[ru/PythonExamples/PythonExamples|Русский]]

## Getting started

[[Installing the Library and Running Examples]]: local installation, library use, running programs and tests, and working in Google Colab.

## First examples

[[Triangle Coupling Variations in Python]] reproduces the strengthening of one and two couplings of a unit triangle from [[Variation of a Single Edge]] and [[Varying several couplings together]]. Edge factors update the metric polyform; formulas and direct matrix calculations check the results.

Prerequisites: [[PMG Introductory Series]], particularly [[Basic Objects and Operations of Polyform Algebra]] and [[Laplacian Exponential]].

## Code and reproducibility

The complete code lives in the [Python library repository](https://github.com/magin67/polyform_algebra). Notes link to a specific tested revision rather than a moving branch. Updating an example requires checking its results again and updating both language versions together.

These calculations use the supported quadratic subalgebra. The presence of more general forms in the [[Core specification|specification]] does not imply that they have already been implemented.

## Section status

The series lives in the `ru/PythonExamples` and `en/PythonExamples` folders of the PMG library. Russian and English versions are maintained together. The initial numerical examples were checked on Python 3.12. A computation for a particular case does not replace a general proof.
