---
title: Further Reading for the PMG Introductory Series
date: 2026-10-07
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: introductory-reading
lang: en
description: Annotated reading recommendations on graphs, electric networks, resistance geometry, matrix perturbations, and exterior algebra for the PMG introductory series.
---

This list supplements the ten introductory notes. Sources are grouped into three themes; each entry identifies recommended sections, connections to the notes, and access options. All sources below are in English.

## Where to start

For a first reading, follow this route:

1. **The Laplacian and electric networks:** Spielman [3], Chapters 1, 11, and 12. Doyle and Snell [2] provide an introduction through currents and voltages.
2. **The geometry of effective resistance:** Devriendt [4], Section II. This requires inner products, Gram matrices, and the pseudoinverse.
3. **Coupling variations:** Petersen and Pedersen [5], the sections on determinants and matrix inversion. Derivations of the matrix identities are discussed in [6].
4. **Exterior products and spanning trees:** Vinberg [8], Chapter 8, and Spielman [3], Section 13.4. Prasolov [7] complements these with proofs and problems.

Diestel [1] provides a reference for graph terminology. Lyons and Peres [9] offer further reading on the relation between electric networks and random spanning trees.

## Graphs, electric networks, and resistance geometry

### [1] R. Diestel. Graph Theory

Fifth edition. Springer, 2017. Graduate Texts in Mathematics, 173.

[Publisher's page and preview](https://link.springer.com/book/10.1007/978-3-662-53622-3). The contents and front matter are openly available; the full book requires purchase or institutional access.

**Read:** Chapter 1, particularly Sections 1.3 on paths and cycles, 1.4 on connectivity, 1.5 on trees and forests, and 1.9 on linear algebra.

The book establishes the terminology of paths, cycles, trees, forests, and connected components. It supports the first note and the forest expansion of the Laplacian exponential. Resistance geometry requires the more specialised sources [2]-[4]. Prerequisites: elementary discrete mathematics.

### [2] P. G. Doyle, J. L. Snell. Random Walks and Electric Networks

Mathematical Association of America, 1984. Open electronic version dated 5 July 2006.

[Full text on the author's website, PDF](https://math.dartmouth.edu/~doyle/docs/walks/walks.pdf).

**Read:** Section 1 on finite networks, particularly 1.3 on general networks and 1.4 on Rayleigh's monotonicity law. Section numbers refer to the electronic version above.

Currents, voltages, conductances, and effective resistance are introduced through the connection between electric networks and random walks. The energy principle explains how changing one coupling affects the resistance of the network. This complements the notes on the Laplacian, effective resistance, and variation of a single edge. Prerequisites: basic linear algebra; the probabilistic parts require elementary probability.

### [3] D. A. Spielman. Spectral and Algebraic Graph Theory

Author's textbook draft, incomplete version dated 2 April 2025.

[Full text, PDF](https://www.cs.yale.edu/homes/spielman/sagt/sagt.pdf). The file is updated periodically; chapter numbers refer to the version checked.

**Read:** Section 1.2 on graph matrices; Chapter 11 on walks, springs, and resistor networks; Chapter 12 on effective resistance and Schur complements. For spanning trees, read Chapter 13, particularly Section 13.4 on the matrix-tree theorem.

A unified account connects the Laplacian quadratic form, electric currents, the pseudoinverse, effective resistance, and spanning trees. It supports the matrix-based part of the introduction and the combinatorial interpretation of the Laplacian exponential. Prerequisites: university-level linear algebra.

### [4] K. Devriendt. Effective resistance is more than distance: Laplacians, Simplices and the Schur complement

*Linear Algebra and its Applications*, 639 (2022), 24-49.

[Open text on arXiv](https://arxiv.org/abs/2010.04521) · [Journal DOI](https://doi.org/10.1016/j.laa.2022.01.002).

**Read:** Section II on graphs, Laplacians, and simplices, particularly II.2-II.4. Sections III and IV discuss the Schur complement and a geometric proof of the metric properties of resistance.

The paper explains the correspondence between a Laplacian and a geometric simplex, the role of the pseudoinverse as a Gram matrix, and the representation of effective resistances as squared Euclidean distances. It complements the notes on graph geometry and the relations between the Laplacian, Green matrix, and effective resistance matrix. Prerequisites: linear algebra and simplex geometry.

## Coupling variations

### [5] K. B. Petersen, M. S. Pedersen. The Matrix Cookbook

Technical University of Denmark. Version dated 15 November 2012.

[Publication page](https://www2.imm.dtu.dk/pubdb/pubs/3274-full.html) · [Full text, PDF](https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf).

**Read:** Section 1.2 on determinants; Sections 3.2.2 on the Woodbury identity, 3.2.3 on the Kailath variant, and 3.2.4 on the Sherman-Morrison formula.

A compact reference for matrix identities governing rank-one and higher-rank perturbations. It relates variations of one or several couplings to identities for inverses and determinants. Apply these formulas to an invertible reduced Laplacian or to its restriction to the zero-sum subspace, checking invertibility after the change. The handbook is intended for checking formulas rather than studying their proofs in sequence.

### [6] H. V. Henderson, S. R. Searle. On Deriving the Inverse of a Sum of Matrices

*SIAM Review*, 23(1) (1981), 53-60.

[Article page and DOI](https://doi.org/10.1137/1023004). The abstract and bibliographic information are open; the publisher's full text requires access.

**Read:** the entire paper for derivations of inversion identities beyond the reference formulas in [5].

The authors consider inverses of matrix sums, including perturbations of the form $A+UBV$, and compare different versions of the identities. This is an additional source for both notes on coupling variations. Prerequisites: block matrices and matrix multiplication.

## Exterior algebra and metric polyforms

### [7] V. V. Prasolov. Problems and Theorems in Linear Algebra

American Mathematical Society, 1994. Translations of Mathematical Monographs, 134.

[Full English text on a university website, PDF](https://staff.math.su.se/mleites/books/prasolov-1994-problems.pdf).

**Read:** Chapter I, Section 2 on minors and cofactors, including the Cauchy-Binet formula and Jacobi's identities for complementary minors; Chapter V, Sections 27 and 28 on multilinear maps, tensor products, and symmetric and skew-symmetric tensors. These section numbers refer to the 1994 English edition.

The book connects determinants, minors, and exterior powers. It supports proofs of metric formulas for higher grades and the extraction of the highest-grade coefficient in the Laplacian exponential. It also complements matrix transformations and joint variations. Prerequisites: basic linear algebra; the presentation emphasises proofs and problems.

### [8] E. B. Vinberg. A Course in Algebra

American Mathematical Society, 2003. Graduate Studies in Mathematics, 56.

[Publisher's page and DOI](https://doi.org/10.1090/gsm/056). The full book requires purchase or institutional access.

**Read:** Chapter 5 on vector spaces, particularly bilinear and quadratic functions and Euclidean spaces; Chapter 8 on tensor algebra, particularly tensor products, the tensor algebra, and the Grassmann algebra.

A systematic introduction to bilinear forms, tensor products, and exterior algebra. These topics provide the prerequisites for products of forms, grades, and the vanishing of exterior products of linearly dependent vectors. It complements the notes on the basic objects of polyform algebra and the metric of higher-grade objects. Prerequisites: elementary vector spaces; the necessary definitions are developed in the book.

### [9] R. Lyons, Y. Peres. Probability on Trees and Networks

Cambridge University Press, 2016. Author's electronic versions include corrections and updates.

[Book website and open full texts](https://rdlyons.pages.iu.edu/prbtree/).

**Read:** Chapter 2 on random walks and electric networks and Chapter 4 on uniform spanning trees. The remaining chapters are not required for the introductory series.

A more detailed treatment of electric networks and random spanning trees. Determinantal relations between edge-inclusion events connect tree combinatorics with electrical measurements. This is further reading after the notes on joint variation and the Laplacian exponential. Prerequisites: linear algebra and probability.

## Relation to the introductory notes

| Note | Sources | Main topic |
|---|---|---|
| [[Laplacian - graph, electrical network and quadratic form]] | [1], [2], [3] | Graph terminology, network laws, the Laplacian quadratic form |
| [[Effective Resistance and Graph Geometry]] | [2], [3], [4] | Effective resistance and its Euclidean representation |
| [[Inner Product of Graph Vectors]] | [3], [4], [8] | Inner products and Gram matrix geometry |
| [[Laplacian, Green Matrix, and Effective Resistance Matrix]] | [3], [4], [7] | Pseudoinverses, distance matrices, minors |
| [[From Lengths to Areas and Volumes]] | [7], [8] | Gram determinants and exterior powers |
| [[Variation of a Single Edge]] | [2], [5], [6] | Monotonicity, rank-one perturbations, matrix inversion |
| [[Varying several couplings together]] | [5], [6], [7], [9] | Matrix perturbations, determinants, relations between edge-inclusion events |
| [[Basic Objects and Operations of Polyform Algebra]] | [7], [8] | Tensor and exterior algebras, bilinear forms |
| [[Metric of Higher-Grade Objects]] | [7], [8] | Exterior powers and Gram determinants |
| [[Laplacian Exponential]] | [1], [3], [7], [9] | Forests, spanning trees, and determinantal coefficients |

> [!remark] Literature and PMG constructions
> These sources explain standard results about graphs, electric networks, matrices, and exterior algebra. Their expression in the language of boundaries and forms is given in the introductory notes. The metric polyform $M_G=\exp L$, the adopted definitions of potential and norm, and PMG notation require their own exposition and justification in the project materials.
>
> The exponential $\exp L$ in this construction uses the product of forms. Textbook sections on the matrix exponential concern a different operation.

Links and electronic-version information were checked on 7 October 2026. When citing files that are updated periodically, specify the date of the version used.
