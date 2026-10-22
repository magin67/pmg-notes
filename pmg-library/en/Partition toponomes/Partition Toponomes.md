---
title: Partition Toponomes
date: 2026-10-22
updated: 2026-10-22
revision: 2
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: partition-toponomes-series-navigation
lang: en
description: "Reducing a chosen polyform representation to partition types, dependence on structural identities, the second-kind algebra, graph interpretations, and coefficient triangles."
order: 0
---

This series introduces a **partition toponome**: a linear combination of types obtained from a chosen representation of a polyform as a sum of partition forms. Vertex labels are forgotten, and coefficients of identical types are collected. The series then defines multiplication of types, examines its graph interpretations, and develops a further reduction to coefficient tables.

The central question is what data each passage retains and on which objects it is defined. Types can be written as partitions or as monomials of a polynomial in several variables: these notations are equivalent. Grouping distinct types and applying structural identities require separate consideration.

## Main results

**The toponome of a chosen representation.** For an expression $\mathcal E=\sum_\pi c_\pi q_\pi$ on a fixed set of $n$ vertices, where $q_\pi$ is a partition form,

$$
T_{\mathcal E}=\sum_\pi c_\pi\lambda(\pi)
$$

Here $\lambda(\pi)$ is the collection of positive boundary grades of the blocks. In the expansion of the Laplacian exponential, a type coefficient counts spanning forests of that type for unit edge weights; for a weighted graph, it is the sum of products of their edge weights. The full example of a path on five vertices appears in [[From Polyforms to Partitions]].

**Dependence on representation.** The identity $E_4[1,1]=E_4[2,0]$ relates equal polyforms, but the displayed expressions give different toponomes, $3(1^2)$ and $4(2)$. Reduction is defined linearly on formal sums of partitions. It descends to polyforms independently of their representation if and only if it sends every structural relation to zero. The criterion and the example of grade two of the $K_4$ exponential are developed in [[Toponomes and Structural Identities]].

**The second-kind algebra.** The product $*$ sums partial matchings of occurrences of parts in two factors. Each part belongs to at most one pair; matched parts add, and unmatched parts remain unchanged. This is a commutative associative algebra with unit $1$, isomorphic to the algebra of symmetric functions in the augmented monomial basis. In particular,

$$
(1^2)*(1^2)=(1^4)+4(2,1^2)+2(2^2)
$$

For every integer $k\geqslant0$,

$$
(1)^k=\sum_{\lambda\vdash k}s_2(\lambda)\lambda
$$

The coefficients in the second formula are combinatorial potentials of the second kind. The general rule, proofs, and computational procedures appear in [[The Second-Kind Algebra on Partitions]]. The designation “second-kind” refers to the algebra and is used as a PMG term.

Two realizations of this product differ in the meanings of parts and in their graph operations:

| Realization | Meaning of a part | Operation realizing the product $*$ |
| --- | --- | --- |
| [[Graph Colorings and Partition Products\|Color classes]] | The weight of a class; for unit weights, its vertex count | The sum of color-class types of a disjoint union of graphs |
| [[Partition Products and Boundary Forms\|Boundary forms]] | Boundary grade; for a tree, its edge count | A sum of partial pairwise gluings of components at roots chosen in advance |

The second model does not sum over root choices. Ordinary multiplication of particular polyforms is determined by their already specified shared vertices and is not generally described by $*$.

**Coefficient triangles and limits on distinguishing graphs.** Grouping types of weight $k$ with the same number $r$ of positive parts gives the table

$$
a_{k,r}=\sum_{\substack{w(\lambda)=k\\\#\lambda=r}}c_\lambda
$$

For nonempty types on $n$ vertices, the admissible indices satisfy $r\leqslant k\leqslant n-r$. Thus, with $k$ indexing columns and $r$ indexing rows, each successive row loses one position at either end. The unit term is treated separately, and zero cells are left blank. [[Coefficient Tables of Toponomes]] displays the triangle for the path $P_6$, proves equality of the normalized path and cycle triangles with an example on eleven vertices, derives the induced product of tables, and gives two nonisomorphic trees on ten vertices with the same table. Their full toponomes differ; the counterexample concerns the data $(n,\mathcal A_G)$, not every possible refinement of the invariant.

## Reading order

1. **[[From Polyforms to Partitions]].** Full and positive types, coefficients, all grade components of the $P_5$ exponential, polynomials in several variables, and retained data.
2. **[[Toponomes and Structural Identities]].** The tetrahedron identity, two representations of grade two of the $K_4$ exponential, and a criterion for representation-independent reduction.
3. **[[The Second-Kind Algebra on Partitions]].** Partial matchings, one-part multiplication, recursive computation, powers of $(1)$, and symmetric functions.
4. **[[Graph Colorings and Partition Products]].** The vertex interpretation, seven color-class partitions of two edges, and the chromatic symmetric function.
5. **[[Partition Products and Boundary Forms]].** The boundary interpretation, seven gluings of two pairs of connections, the role of chosen roots, and the limits of the model.
6. **[[Coefficient Tables of Toponomes]].** Two indices, triangular layout, normalized path and cycle triangles, multiplication, retained information, and a counterexample to reconstructing every graph.

An introduction to reduction can follow [[From Polyforms to Partitions]] → [[Toponomes and Structural Identities]] → [[Coefficient Tables of Toponomes]]; the section on table multiplication relies on the algebra. The algebraic route through [[The Second-Kind Algebra on Partitions]] and [[Graph Colorings and Partition Products]] does not require a PMG metric.

## Prerequisites and notation

Reduction requires [[Partition Forms and the Tetrahedron Identity|partition forms]] and the [[Laplacian Exponential|Laplacian exponential]]. The coefficients of powers connect to the [[Partitions and the Combinatorial Potential of the Second Kind|potential of the second kind]]. General conventions are recorded in the [[Core specification|specification]] and [[PMG terminology|terminology]].

For a positive type $\lambda=(k_1,\ldots,k_r)$, write $k=w(\lambda)$ and $r=\#\lambda$. The full number of components is $m=n-k$, and the number of singleton vertices is $\ell=n-k-r$. Retain the original vertex count $n$ separately. The multiplicity notation $(1^2)$ differs from the product power $(1)^2$; the empty type $1$ corresponds to the unit form $e$. The notation $[x_i]!$ retains its meaning as the product of a collection.

## Scope and further directions

The term “partition toponome” is defined for a specific reduction of a chosen representation. Equal numerical evaluations of distinct types do not imply equal toponomes. Weighted coefficients retain aggregated weight data, so the result cannot be described solely as a collection of topological properties.

The [[Карта библиотеки PMG|PMG library map (in Russian)]] records further directions: component and root weights, the passage to $\det(I+t\mathbf L)$, the distinction between a spectrum and a full spectral representation, toponomes of dual polyforms after duality is introduced, multicomponent gluings, and refinements of graph invariants. Reduction of a polyform by another polyform and the spanning-tree operator remain a separate direction.

