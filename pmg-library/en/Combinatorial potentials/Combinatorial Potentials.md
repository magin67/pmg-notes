---
title: Combinatorial Potentials
date: 2026-10-20
updated: 2026-10-24
revision: 2
source_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: combinatorial-potentials-series-navigation
lang: en
description: "Potentials of the first and second kinds, ordinary and cyclic partitions, SPF and forest counts, Cayley's formula, and Stirling numbers."
order: 0
---

This series explains how component sizes determine the counts of concrete partitions and graph constructions. Its central concept is the **combinatorial potential of the second kind**: the number of partitions of a given set into unordered blocks of prescribed sizes. This count is then applied to symmetric polyforms and compared with the number of forests. A separate note counts ways to join prescribed components into a tree. The relation between forest coefficients and $r$-Stirling numbers is explained through rooted forests. The final note introduces the potential of the first kind: the number of cyclic partitions of a prescribed type, connecting the series to permutation digraphs.

## Main results

**The potential of a prescribed type.** Let the numerical collection $\mathbf x=[x_1,\ldots,x_m]$ consist of positive integers and have weight $w$. If $\boldsymbol\mu$ is the collection of positive multiplicities of its distinct values, then

$$
\boxed{s_2(\mathbf x)=\frac{w!}{[x_i!]!\,[\mu_j!]!}}
$$

The formula follows by successively removing repetitions within blocks and between blocks of equal size. Examples with two pairs, a triple and a singleton, and two triples and a pair appear in [[Partitions and the Combinatorial Potential of the Second Kind]].

**The potential of a cycle type.** Giving each block a cyclic order changes the number of objects to

$$
\boxed{s_1(\mathbf x)=s_2(\mathbf x)\prod_i(x_i-1)!=\frac{w!}{\mathbf x!\,[\mu_j!]!}}
$$

The definition, a figure showing both orientations of a 3-cycle, and the derivation appear in [[Cyclic Partitions and the Combinatorial Potential of the First Kind]]. Summing over all types of weight $w$ gives $w!$; summing over types with a fixed number of cycles gives the unsigned Stirling numbers of the first kind. Excluding parts of size $1$ gives permutations without fixed points.

**Different SPF counts.** For positive grades $\boldsymbol k=[k_1,\ldots,k_r]$ and $\ell$ singleton blocks, the block sizes are $[k_i+1,1^\ell]$. The potential of this collection counts terms in the standard representation of $E_n$; the potential $s_2(\boldsymbol k)$ enters the fundamental theorem coefficient. Choosing trees within already fixed blocks introduces another factor, $t(\boldsymbol k)$. These distinctions are illustrated with type $[2,1]$ in [[Combinatorial Potentials in Symmetric Polyforms]].

| What is counted for type $[2,1]$ | Value |
| --- | ---: |
| Partitions of three auxiliary labels into sizes $[2,1]$ | $s_2([2,1])=3$ |
| Partitions of five original vertices into sizes $[3,2]$ | $\#E_5[2,1]=10$ |
| Complete-graph forests on these five vertices with those component sizes | $10\cdot3=30$ |

**Joining prescribed components.** If a fixed forest has $m\geqslant2$ components of sizes $\mathbf x=[x_1,\ldots,x_m]$ and $n=w(\mathbf x)$ vertices, its number of completions to a tree in the complete graph is

$$
\boxed{T(\mathbf x)=\mathbf x!\,n^{m-2}}
$$

For $m=1$, the forest is already a tree and its completion is unique. The Prüfer-code proof, all eight completions for sizes $[2,1,1]$, and the passage to a weighted graph are given in [[Cayley's Theorem and Joining Prescribed Components]]. In this problem, the blocks and their internal trees are already fixed.

**Forest coefficients and $r$-Stirling numbers.** For $1\leqslant m\leqslant k$, deleting ordinary leaves to encode a forest gives the bijection

$$
\operatorname{St}(k,m)=\left\{\begin{matrix}2k\\k+m\end{matrix}\right\}_{k+1}
$$

The right side counts partitions of $2k$ elements into $k+m$ blocks with $k+1$ distinguished elements in different blocks. The graph meaning of this identity, the role of isolated roots, and two counts of the number $91$ are explained in [[Falling Factorials, Rooted Forests, and Stirling Numbers]].

## Reading order

1. **[[Partitions and the Combinatorial Potential of the Second Kind]].** Collections and multiplicities, integer and set partitions, the product of a collection, the derivation of $s_2$, and relations to Stirling and Bell numbers.
2. **[[Combinatorial Potentials in Symmetric Polyforms]].** Types by edges, zero components, representation size, choosing subsets, forest counts, and the fundamental identity coefficient. Figures accompany the main examples.
3. **[[Cayley's Theorem and Joining Prescribed Components]].** Joining fixed blocks, the weighted Cayley formula, component contraction, refinement by Prüfer code type, and a brief passage to polyforms.
4. **[[Falling Factorials, Rooted Forests, and Stirling Numbers]].** Star and general rooted forests, leaf-deletion codes, inclusion-exclusion, $r$-Stirling numbers, and shifted expansions.

5. **[[Cyclic Partitions and the Combinatorial Potential of the First Kind]].** Cyclic orders within blocks, the relation between $s_1$ and $s_2$, sums over types, Stirling numbers of the first kind, and excluding fixed points.

The first-kind note can be read immediately after the definition of the second kind; its graph application appears in [[Permutation Digraphs and Cycle Combinatorics]].

The combinatorial route passes through the notes on partitions, joining components, and [[Falling Factorials, Rooted Forests, and Stirling Numbers|rooted forests and Stirling numbers]]; their main proofs do not require polyforms. For the passage to PMG, read the SPF potential note alongside [[Symmetric Polyforms - Types and Normalizations|types and normalisations]] and the [[Fundamental Theorem of Symmetric Polyforms|fundamental theorem]]. A further application to rooted forests, Abel polynomials, and finite differences appears in [[Forest Coefficients and Abel Polynomials]].

## Notation and scope

The size of a collection is $\#\mathbf x$, its weight is $w(\mathbf x)$, and the product of its elements is $\mathbf x!$. The notation $[x_i!]$ defines the collection of factorials, and $[x_i!]!$ its product. Repetitions are retained. The full number of partition components is $m$; in SPF types, $r$ counts nontrivial components and $\ell=m-r$ counts singletons.

Block sizes and boundary grades differ by one. A component's edge count equals its grade in a forest; this equality does not apply in the presence of cycles. Representation size, forest count, and form-identity coefficient have different definitions.

Notation and links are consistent with the [[Symmetric Polyforms]] series. The potential of the first kind counts cyclic partitions; the algebra of open paths and marked components remains a further combinatorial topic. The formulas in this series are proved under their stated conditions; enumeration of small examples provides additional checks.

