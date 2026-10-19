---
title: Symmetric Polyforms
date: 2026-10-20
updated: 2026-10-20
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: symmetric-polyforms-series-navigation
lang: en
description: "The fundamental theorem of SPFs as the main result of the series: exact normalization, proof, product rules, the complete-graph exponential, and Abel polynomials."
order: 0
---

The main result of this series is the **fundamental theorem of symmetric polyforms**. It expresses a symmetric sum of partition forms of any admissible type through the principal polyform of the same grade and gives the exact coefficient of this conversion. Consequences include product and power rules, a compact representation of the exponential of the complete graph, and combinatorial identities related to Abel polynomials.

A symmetric polyform (SPF) is invariant under every permutation of the chosen vertex set. A principal symmetric polyform (principal SPF) of positive grade is a sum of partition forms with one nontrivial component. Symmetry under vertex permutations differs from symmetry of the arguments of a form and from commutativity of the product of forms.

## Main result: the fundamental theorem of SPFs

Fix $n\geqslant2$ independent basis vertices over $\mathbb R$. In the sum $E_n[\lambda]$, each partition into unordered blocks of the given type is counted once with coefficient $1$. The parts of the type are the grades of the block boundaries: a part $k_i$ corresponds to a block of $k_i+1$ vertices, and a zero to a singleton block.

Let $m\geqslant1$, $k_i\geqslant1$, $k=\sum_i k_i$, and $\ell=n-k-m\geqslant0$. Write $\mu_j$ for the number of parts equal to $j$. The principal SPF of the same grade is denoted by $E_n[k]=E_n[k,0^{\,n-k-1}]$.

> [!info] Fundamental theorem
> For every admissible type, the following identity of forms holds:
>
> $$
> \boxed{
> E_n[k_1,\ldots,k_m,0^\ell]
> =\frac{(n-k-1)!\,k!}
> {\ell!\displaystyle\prod_{i=1}^m k_i!\displaystyle\prod_{j\geqslant1}\mu_j!}
> E_n[k]
> }
> $$
>
> Grade zero is specified separately: $E_n[0^n]=e$. A type refers to the chosen representation; the identity relates representations of different types of the same polyform.

The full statement and proof are given in [[Fundamental Theorem of Symmetric Polyforms]]. The idea of the main proof is due to Dmitry Malugin; the exposition was prepared by ChatGPT. The proof has three steps:

1. A quadratic identity for arguments whose sum is zero.
2. Merging two blocks using $\partial^2=0$.
3. Successively merging all nontrivial blocks and counting multiplicities.

This is a general algebraic proof before a graph or metric is chosen. The [[Fundamental Theorem of Symmetric Polyforms#Examples and normalization checks|examples accompanying the theorem]] include expanded identities on five and six vertices. Comparing representation sizes or arbitrary coefficient sums does not suffice to prove an identity of forms.

## Consequences and applications

**One symmetric direction in each grade.** Every SPF on boundaries has a unique representation $P=c_0e+\sum_{k=1}^{n-1}c_kE_n[k]$. For the space of partition forms, this follows from the main theorem and averaging over permutations. The extension to all forms on boundaries is proved using classical representation theory in the [[Fundamental Theorem of Symmetric Polyforms#Correspondence with classical representation theory|section on the correspondence with the literature]]. The number of independent relations among symmetric sums of types is $p(n)-n$, where $p(n)$ counts partitions of the integer $n$.

**A simple product rule.** Let $1\leqslant p,q\leqslant n-1$. If $p+q\leqslant n-1$, then $E_n[p]E_n[q]=n\binom{p+q}{p}E_n[p+q]$; if $p+q\geqslant n$, the product is zero. The algebra of SPFs on boundaries is isomorphic to $\mathbb R[t]/(t^n)$ under $t\mapsto E_n[1]$. Proofs, powers, and factorial normalizations are collected in [[Products and Powers of Symmetric Polyforms]].

**The complete-graph exponential and Cayley's formula.** For $K_n$ with unit conductances, the Laplacian equals $E_n[1]$, and its polyform exponential is

$$
M_{K_n}=e+\sum_{k=1}^{n-1}n^{k-1}E_n[k]
$$

The top-grade coefficient gives $\tau(K_n)=n^{n-2}$. In [[Symmetric Polyforms of the Complete Graph]], this representation is compared with the expansion by forest type. The same note shows how to obtain the exponential of another graph by deleting edges from the complete graph, with a detailed example for $C_4$.

**The combinatorial meaning of forest coefficients.** Comparing the expansions yields the falling-factorial expansion of the Abel polynomial $A_k(x)=x(x+k)^{k-1}$, $k\geqslant1$. Its coefficients $\operatorname{St}(k,m)$ count rooted forests on $k$ labelled vertices together with a partition of their component set into $m$ nonempty groups. The bijection, the connection with Stirling numbers, and the exact correspondence with OEIS A360177 are given in [[Forest Coefficients and Abel Polynomials]].

## Reading order

1. **[[Symmetric Polyforms - Types and Normalizations|Symmetric Polyforms: Types and Normalizations]].** Definitions of SPFs and principal SPFs, zero components, representation size, repeated blocks, and symmetrization. This note fixes the normalization used throughout the series.

2. **[[Fundamental Theorem of Symmetric Polyforms]].** The main identity and its three-step proof, expanded examples, uniqueness of the principal representation, counting symmetric relations, and the precise connection with representation theory.

3. **[[Products and Powers of Symmetric Polyforms]].** The product rule for principal SPFs, powers and nilpotency, a single generator, and the special role of grade zero. Examples on four, five, and six vertices.

4. **[[Symmetric Polyforms of the Complete Graph]].** Two representations of the exponential, a derivation of Cayley's formula, counting forests of a given type, the $K_5$ example, and deleting diagonals to obtain $C_4$.

5. **[[Forest Coefficients and Abel Polynomials]].** Passing from SPF identities to numerical coefficients, rooted forests and grouping components, prescribed roots, finite differences, and correspondence with the literature.

To study the main result, read [[Symmetric Polyforms - Types and Normalizations|the note on types and normalizations]] and [[Fundamental Theorem of Symmetric Polyforms|the fundamental theorem]]. For the graph applications, continue with [[Products and Powers of Symmetric Polyforms|products and powers]] and [[Symmetric Polyforms of the Complete Graph|the complete graph]]. The combinatorial continuation is developed in [[Forest Coefficients and Abel Polynomials|the note on forest coefficients]].

## Prerequisites

The main proof requires [[Basic Objects and Operations of Polyform Algebra|boundaries, grades, bilinearity, and the product of forms]], together with the definition of a [[Partition Forms and the Tetrahedron Identity|partition form]]. The original normalization of $E_n[\lambda]$ is introduced in the [[Constructing Structural Identities#From local identities to symmetric sums|section on symmetric sums]] and restated in the note on types. The proof of the noncrossing basis from [[Structural Identities]] is not required for the main proof of the fundamental theorem of SPFs.

Graph applications use the [[Laplacian Exponential|Laplacian exponential and its forest expansion]]. Notation and terminology agree with the [[Core specification|core specification]] and [[PMG terminology|PMG terminology]]. Representation size, coefficient sum, and metric evaluation of a polyform are distinct quantities; the PMG norm is quadratic: $X^2=X\cdot X$.

## Status and scope of the series

All five notes are available in Russian and English; the overall review of content, translations, links, and formatting is complete. The formulas have general proofs or precise references to accessible sources. Computational checks provide additional verification of examples.

The main proof of the fundamental theorem works directly with partition forms. The independent explanation and extension to all forms on boundaries use irreducibility of the exterior powers of the standard representation of $S_n$ and Schur's lemma; references and the passage to PMG are given in the [[Fundamental Theorem of Symmetric Polyforms#Correspondence with classical representation theory|section on representation theory]].

The complete-graph formulas apply to unit or equal conductances with explicitly stated scaling. Invariance under automorphisms of an arbitrary graph and the role of SPFs in its exponential remain a separate research topic. Reductions, toponomes, the spanning-tree operator, and the dual polyform retain their own scope. The overview “Partitions and Combinatorial Coefficients” and the note “Polyform Algebra” are planned separately.
