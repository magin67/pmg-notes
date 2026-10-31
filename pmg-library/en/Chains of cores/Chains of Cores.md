---
title: "Chains of Cores"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: core-chains-series-navigation
order: 0
description: "Reading routes, applicability conditions, proofs, examples, and sources for chains of cores."
---

Russian version: [[ru/Цепи из ядер/Цепи из ядер|Цепи из ядер]].

This series explains how cores, seams, and the gluing scheme determine the characteristics of an assembled graph. Its main positive result concerns admissible open chains of cycles: with fixed ordered core and seam sizes, changing the configuration preserves the cycle matroid, ordinary forest coefficients, spanning-tree count, and resistance radius. Reordering seams, changing the scheme, or changing the last correspondence at closure requires separate analysis.

The five notes form a complete introductory reading route. This navigator collects their connections, applicability conditions, and the origins of the results. Full spectral classification of chains remains a continuation.

## Reading route

1. [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. Definitions of cores and schemes, seam vertex correspondences, and counting shared edges once. Input, output, and active boundaries; transfer of the full forest passport. The initial example of two assemblies of three hexagons.
2. [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. A plane embedding and a common dual multigraph for fixed ordered data. The passage to the cycle matroid, ordinary forests, and the radius; an independent check of the example and the difference between rooted forests.
3. [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]]. A dual determinant indexed by the cores, a two-step recurrence, continuants, and matchings. Homogeneous normalization, Chebyshev polynomials, chain reversal, and dependence on seam order.
4. [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores|Limits of Invariance - Branching, Disconnected Seams, and Other Cores]]. The theorem for a fixed tree of cycles; the difference between a path and a star. Disconnected seams, seam pairs in tetrahedra and cubes, and gluing prisms along lateral faces. A counterexample with equal spanning-tree counts but different radii.
5. [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain - Rings and the Möbius Effect]]. Exact ordinary and twisted closures of a square strip; their spanning-tree counts and radii. Strips of even cycles, a hexagonal ring around a hole, and the separate model of closing prisms along their bases.

For particular tasks, a shorter route is possible:

- **Establish invariance:** [[en/Chains of cores/Cores, Seams, and Admissible Chains#Admissible open chains of cycles|check admissibility]] → [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#From the dual graph to the cycle matroid|construct the common matroid]] → [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores#Which data are being compared|identify which change of construction is being compared]].
- **Compute the spanning-tree count:** [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#The spanning-tree count as a dual determinant|the dual determinant]] → [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#Recurrence in the number of cores|the recurrence]]. For a closed strip, continue to the [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect#The final seam of a square strip|definition of the final seam]] and the relevant model in that note.
- **Assemble using boundary data:** [[en/Chains of cores/Cores, Seams, and Admissible Chains#Accounting for shared edges when gluing|distribute shared edges]] → [[en/Chains of cores/Cores, Seams, and Admissible Chains#Transferring the full forest passport|transfer the passport to the new boundary]] → for closure, [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect#Edge accounting and retaining the initial boundary|retain the start until the final identification]].

## Conventions and background results

> [!info] Common construction data
> Write $N$ for the number of cores and $n$ for the vertex count of the assembled graph. The auxiliary path or tree on cores is a separate graph.
>
> The size $s_i$ of a connected seam counts **vertices** of $P_{s_i}$; the number of shared edges is $s_i-1$. A one-vertex seam has $s_i=1$, and an edge seam has $s_i=2$. The vertex correspondence is part of the data.
>
> In the basic model all edges are unit edges. Shared edges are identified, and their conductances are not added. Before applying formulas for disjoint edge sets, assign duplicate copies explicitly to the parts.
>
> The resistance radius is $\rho=R_{\mathrm{sph}}^2$ and the resistance diameter is $D_{\mathrm{res}}=4\rho$. Drawings of constructions are not resistance embeddings.

The polynomial notations serve different tasks. The ordinary forest polynomial $F_G(t)=\sum_g f_g(G)t^g$ counts forests without roots. The Laplacian polynomial $P_G(t)=\det(I+t\mathbf L_G)$ contains rooted forest coefficients; the characteristic polynomial uses $\xi$. The spanning-tree polynomial $\mathcal T_N$ depends on construction parameters and, on admissible integer data, gives one number $\tau(G)$. These distinctions are discussed in [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#Distinguishing the polynomials|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]].

Three groups of published background results are used:

- [[en/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges|The Cycle Matroid and Exterior Products of Edges]], [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]], [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|Resistance Radius - Forest Formula and Matroid Invariance]], and [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]]: matroid parameters and the conditions of gluing laws.
- [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States - What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]], and [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]: full passports, compatibility, and internal components. Spanning-tree and electrical data are separated in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]], and spectral data in [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]].
- [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]], and [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]]: rooted forests, modes, and Chebyshev polynomials. The spectrum of the auxiliary path on cores does not replace the spectrum of the whole graph.

The necessary definitions and main transitions are recalled in the notes themselves. Current normalizations are specified in [[en/Foundations/Core specification|Core specification]] and [[en/Foundations/PMG terminology|PMG terminology]].

## Applicability conditions

In the table, “configuration” means seam positions and vertex correspondences with the explicitly stated data fixed. Shared edges are counted once in every row.

| Model or change | What must be fixed and checked | What is established |
| --- | --- | --- |
| Admissible open chain of cycles | Ordered $m_i,s_i$; proper induced paths; disjoint seams within each core; no nonadjacent contacts or closure | The cycle matroid, $F_G(t)$, $\tau$, and $\rho$ are preserved. Rooted coefficients and the spectrum need not be preserved. |
| Admissible tree of cycles | The tree on cores itself, $m_i,s_{ij}$; pairwise vertex-disjoint seams within each core; no other contacts | The same matroid mechanism applies; a dual determinant indexed by the tree gives the spanning-tree count. |
| Reordering seams or replacing a path by a star | Admissibility of each assembly must be checked again | An arbitrary permutation or scheme change may alter $\tau$. Simultaneously reversing core and seam lists preserves the spanning-tree polynomial. |
| Sequential one-vertex gluings | Any fixed connected cores; each step intersects the assembled part in exactly one vertex | Direct sum of matroids: $\tau$ multiplies and $\rho$ adds. Both attachment positions and the assembly scheme may change in this model. |
| Disconnected seams or cores other than cycles | Full core graphs, actual intersections, seam pairs, and vertex correspondences | Sizes do not imply general invariance. Counterexamples are given, together with a positive result for open $K_4$ chains with disjoint edge seams. |
| Square strip, $N\ge3$ | Two rows, unit transverse edges, and the ordinary or reversed endpoint correspondence at the final seam | Both $\tau$ and $\rho$ formulas are proved; Möbius closure increases $\tau$ by $2N$ and decreases $\rho$. |
| Strip of even $C_m$, $m\ge4$, $N\ge3$ | Opposite edge seams; two equal longitudinal paths; distinct internal path vertices | The formula for $\tau$ and difference $N(m-2)$ are proved. For $m>4$, example radii are computed on the full graphs; no general radius-change law is proved here. |
| Prisms $C_m\square K_2$ closed along bases | $N,m\ge3$; aligned layers; a final cyclic shift $r\in\mathbb Z_m$ | The formula for $\tau_r$ and inequality $\tau_r>\tau_0$ for $r\ne0$ are proved. Shifts $r$ and $m-r$ are isomorphic. Universal monotonicity of the radius in the shift is not established. |

> [!note] What these results do not imply
> Agreement of one spanning-tree count does not guarantee agreement of radii. Symmetry of an individual seam does not establish equivalence of input-output pairs. Leaving sufficient hypotheses does not mean that every invariant must change.
>
> The plane hexagonal ring around a hole has longitudinal paths of lengths $1$ and $3$; a strip with opposite seams has lengths $2$ and $2$. Comparing these constructions changes seam positions, while comparing ordinary and twisted closures of **one** strip changes the last seam.

## Origins and status of the results

In this table, “deduction” means that a proof based on the named results is supplied in the series. It is not a claim of priority in the literature. Precise references and conditions also accompany the statements in the individual notes.

| Result | Source or derivation | Role in PMG | Novelty-claim status |
| --- | --- | --- | --- |
| Transfer of the full forest passport | Mannens–Nederlof [1, §4.3, Definition 4.14, Lemmas 4.17, 4.18, 4.21]; polynomial pairing and removal of marks | Explicit assignment of shared edges and active-boundary transfer retaining internal components | Adaptation of established operations; no priority claimed |
| Common dual multigraph and matroid invariance | Classical plane duality [2]; the observation of Chen–Mohar [3, after Lemma 3.1]; a proof for connected seams and a fixed tree of cycles | Precise sufficient conditions for preserving ordinary forest parameters | Application and extension of the mechanism to the specified model; priority not established |
| Preservation of the resistance radius | Richman–Shokrieh–Wu [4, Theorem C / 5.7] and the passage to the radius in the note on its forest formula | The quadratic normalization $\rho$; distinguishing matroid invariance from equality of $\tau$ alone | Consequence of established identities in the PMG normalization |
| Spanning-tree determinant and recurrence | The matrix-tree theorem; Chen–Mohar [3, Lemma 3.1] for a shared edge; dual-edge multiplicities for a path seam | Computation indexed by cores and dependence on seam order | An established recurrence and its derivation for the extended model |
| Matchings, normalization, and Chebyshev polynomials | Tridiagonal determinant expansion; standard DLMF identities [5] | Distinguishing the construction polynomial, ordinary forests, and the spectrum | Standard algebraic constructions; no priority claimed |
| Spanning-tree and resistance parameters of square closures | Azimi–Farrokhi [6, §§4–5]; a spectral derivation is supplied in the series | Passage from periodic to antiperiodic modes and radius normalization | Established families and adaptation of resistance characteristics |
| Elongated strips and shifted prism bases | Replacement of series edges with its determinant factor; cycle modes and the matrix-tree theorem | Formulas for precisely specified closure models | Proved deductions; no independent priority claimed |
| Graph pairs and counterexamples | Explicit assemblies, structural nonisomorphism certificates, and independent exact computations | Checking normalizations and demonstrating the limits of assertions | Computational examples and counterexamples; no priority claimed |

External foundations:

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [§4.3](https://arxiv.org/html/2307.01046#S4.SS3): forest tables and boundary operations.
2. J. Erickson. *Tree-Cotree Decompositions*. [Cycle-cut duality and complementary spanning-tree correspondence](https://jeffe.cs.illinois.edu/teaching/comptop/2023/notes/10-planar-tree-cotree.html).
3. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3).
4. H. Richman, F. Shokrieh, C. Wu. *Counting two-forests and random cut size via potential theory*. [Theorem C / 5.7](https://arxiv.org/html/2308.03859v1).
5. NIST DLMF. [§18.9(i)](https://dlmf.nist.gov/18.9.i), [18.5.1](https://dlmf.nist.gov/18.5.E1), [18.9.21](https://dlmf.nist.gov/18.9.E21): recurrences, trigonometric representation, and the Chebyshev derivative.
6. A. Azimi, M. Farrokhi D. G. *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*. [§§4–5; Theorem 4.2, Corollaries 4.6–4.7 and 5.3–5.4](https://arxiv.org/html/2306.10497v1).

## Reproducibility and continuation

Translation of the texts and figure labels, formula consistency, bilingual links, and rendered pages are documented in the [English translation review](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/REVIEW_EN.md).

The five notes passed the [general review of the Russian series](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/REVIEW_RU.md). The [verification programs, exact results, and construction of 15 figures](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md) are available with the library. Example data retain cores, seams, vertex correspondences, and final edge sets.

Spanning-tree counts are compared with direct determinants of the assembled graph Laplacians. Radii are checked by independent formulas in rational arithmetic. Forest states and matroid correspondences use exhaustive enumeration of small graphs; the computational scope for larger constructions is specified separately. These calculations supplement proofs rather than replace them.

In particular, the two nonisomorphic chains of three hexagons have $\tau=204$ and $\rho=43595/41616$, equal ordinary forest coefficients, and different rooted coefficients. This example connects the matroid part with the future “Spectra of Isomers” direction.

The full spectral automaton with boundary transfer, isomer classification, and decoding questions remain for continuation. Their development will require consistent boundary-edge orientations and the variable $\xi$. Injectivity of a full state does not imply injectivity of one coordinate, and finite code enumeration does not prove a general conjecture. Composite cores made from rings of hexagons also remain a research problem; the results of this series do not provide their general classification.
