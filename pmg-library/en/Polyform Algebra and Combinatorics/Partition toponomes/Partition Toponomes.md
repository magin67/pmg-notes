---
title: Partition Toponomes
date: 2026-10-22
updated: 2026-11-11
revision: 7
source_revision: 9
status: draft
text_prepared_by: ChatGPT
translation_key: partition-toponomes-series-navigation
lang: en
description: "Reducing a chosen polyform representation to partition types, dependence on structural identities, the second-kind algebra, graph interpretations, and coefficient triangles."
order: 0
tags:
  - partitions
  - forests-and-spanning-trees
  - reconstruction
aliases:
  - "en/Partition toponomes/Partition Toponomes"
  - "en/Partition toponomes/index"
---

This series introduces a **partition toponome**: a linear combination of types obtained from a chosen representation of a polyform as a sum of partition forms. Vertex labels are forgotten, and coefficients of identical types are collected. The series then defines multiplication of types, examines its graph interpretations, and develops a further reduction to coefficient tables.

The central question is what data each passage retains and on which objects it is defined. Types can be written as partitions or as monomials of a polynomial in several variables: these notations are equivalent. Grouping distinct types and applying structural identities require separate consideration.

## Place in the library

Primary section: [[en/Polyform Algebra and Combinatorics/Polyform Algebra and Combinatorics|Polyform Algebra and Combinatorics]].

Secondary thematic entries:

- [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]]: distinguishing graphs by coefficient tables.

[[en/Navigation/Thematic Index#Search by tags|Search by tags]] · [[en/Navigation/Thematic Index|Thematic Index]].

## Reading order

1. **[[From Polyforms to Partitions]].** How do we obtain a type and collect contributions of equal types?
2. **[[Toponomes and Structural Identities]].** Why can equality of polyforms fail after passage to types?
3. **[[The Second-Kind Algebra on Partitions]].** How do we multiply types and obtain their coefficients?
4. **[[Graph Colorings and Partition Products]].** How do graph colorings realize matchings of parts?
5. **[[Partition Products and Boundary Forms]].** How do we realize a matching by gluing while retaining the original vertices?
6. **[[Coefficient Tables of Toponomes]].** What does a table reveal, and which differences does it hide?

An introduction to reduction can follow [[From Polyforms to Partitions]] → [[Toponomes and Structural Identities]] → [[Coefficient Tables of Toponomes]]; the section on table multiplication relies on the algebra. The algebraic route through [[The Second-Kind Algebra on Partitions]] and [[Graph Colorings and Partition Products]] does not require a PMG metric.

## Prerequisites and notation

Reduction requires [[Partition Forms and the Tetrahedron Identity|partition forms]] and the [[Laplacian Exponential|Laplacian exponential]]. The coefficients of powers connect to the [[Partitions and the Combinatorial Potential of the Second Kind|potential of the second kind]]. General conventions are recorded in the [[Core specification|specification]] and [[PMG terminology|terminology]].

For a positive type $\lambda=(k_1,\ldots,k_r)$, write $k=w(\lambda)$ and $r=\#\lambda$. The full number of components is $m=n-k$, and the number of singleton vertices is $\ell=n-k-r$. Retain the original vertex count $n$ separately. The multiplicity notation $(1^2)$ differs from the product power $(1)^2$; the empty type $1$ corresponds to the unit form $e$. The notation $[x_i]!$ retains its meaning as the product of a collection.

## Which data are retained

![An expansion, types, a table, and column sums](images/From%20an%20Expansion%20to%20a%20Table.svg)

*Figure 1. Each arrow to the right groups data. Passage to types forgets labels and individual contributions; passage to a cell forgets individual component sizes; summing a column forgets the number of nontrivial components. The vertex count $n$ is retained separately. Encoding a type as a monomial is reversible.*

The main chain uses one fixed initial expansion. Replacing it by a structural identity is a separate operation that may change the toponome. In particular, a graph forest toponome is defined by expanding the factors of its exponential.

## Three different products

| Objects and operation | What happens to the components | Example |
| --- | --- | --- |
| Ordinary multiplication of particular forms | Shared vertices determine the result | $[(ab)]^2[(bc)]^2=[(abc)]^2$ |
| The type product $*$ | All partial matchings are summed | $(1)*(1)=(1^2)+(2)$ |
| Ordinary multiplication of type monomials | Lists of parts are joined without matchings | $x_1x_1=x_1^2$ |

Thus the same disjoint union of graphs has different descriptions for two constructions. Forests are chosen independently and give ordinary multiplication of type polynomials. Color classes in different graphs may share a color and merge, so their type sums multiply under $*$. In the symmetric-function representation, this latter product also becomes ordinary multiplication, but the variables and their correspondence with types are different.

## Programming companion

[[en/PythonExamples/Example - Partition Toponomes|Partition Toponomes]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/partition-toponomes.ipynb).

## Main results

**The toponome of a chosen representation.** For an expression $\mathcal E=\sum_\pi c_\pi q_\pi$ on a fixed set of $n$ vertices, where $q_\pi$ is a partition form,

$$
T_{\mathcal E}=\sum_\pi c_\pi\lambda(\pi)
$$

Here $\lambda(\pi)$ is the collection of positive boundary grades of the blocks. In the expansion of the Laplacian exponential, a type coefficient counts spanning forests of that type for unit edge weights; for a weighted graph, it is the sum of products of their edge weights. The full example of a path on five vertices appears in [[From Polyforms to Partitions]].

**Dependence on representation.** The identity $E_4[1,1]=E_4[2,0]$ relates equal polyforms, but the displayed expressions give different toponomes, $3(1^2)$ and $4(2)$. Reduction is defined linearly on formal sums of partitions. It descends to polyforms independently of their representation if and only if it sends every structural relation to zero. The criterion and the example of grade two of the $K_4$ exponential are developed in [[Toponomes and Structural Identities]].

**The second-kind algebra.** The product $*$ sums partial matchings of occurrences of parts in two factors. Each part belongs to at most one pair; matched parts add, and unmatched parts remain unchanged. This is a commutative associative algebra with unit $1$, also admitting a representation by symmetric functions. In particular,

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

## Scope and further directions

The continuation [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Polynomial Toponomes|Polynomial Toponomes]] treats coefficients as graph parameters. [[Vector and Vertex Normalizations of Toponomes]] compares the original and rooted weights, while [[Reducibility of Toponomes]] explains why factorization depends on the chosen product.

Equal numerical evaluations do not imply equal toponomes. Weighted coefficients retain sums of products of weights; they describe more than the unweighted graph structure.

The [[en/Navigation/Library Map|library map]] retains research directions: refinements of graph invariants, multicomponent gluings, the distinction between a spectrum and a full spectral representation, and toponomes of the Greenian exponential after duality is introduced. Reduction of a polyform by another polyform and the spanning-tree operator form a separate direction.
