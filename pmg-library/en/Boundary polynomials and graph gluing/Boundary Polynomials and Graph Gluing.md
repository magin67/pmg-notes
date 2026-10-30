---
title: "Boundary Polynomials and Graph Gluing"
date: 2026-10-30
updated: 2026-10-30
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: boundary-polynomials-series-navigation
order: 0
description: "Reading routes through six notes: the full forest passport, contraction tests, gluing, groves, Catalan reduction, and separate spectral boundary data. Includes a map of sources and result status."
---

What information about a component must be retained to compute properties of the whole graph after another component is attached? This series answers the question for the **full forest polynomial**, extracts the spanning-tree problem, and then turns to the **Laplacian characteristic polynomial**.

A forest polynomial alone does not show which boundary vertices a chosen forest connects. A spectrum alone does not show the position of the boundary relative to the eigenspaces. A component is therefore replaced by boundary data whose contents depend on the quantity to be computed. Sufficiency of a passport means obtaining the answer for every admissible partner, with the boundary correspondence and edge-counting rule specified in advance.

The main subject is the full forest passport, including forests with components that **do not meet the boundary**. It extends the published [[en/Structural identities/Structural Identities and Graph Gluing|spanning-tree gluing through groves]] and prepares calculations on chains of cores. Ordinary forest and spectral passports have different coordinates and different gluing laws.

## Contents and reading order

| Order | Note | What it establishes |
| ---: | --- | --- |
| 1 | [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component\|Boundary Forest States: What to Retain from a Component]] | Boundary partitions and the polynomial of each state; internal components and groves. The path $P_5$ shows what is lost when states are summed. |
| 2 | [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test\|Vertex Contraction as a Boundary Test]] | The acyclicity criterion and the quotient graph's polynomial. The polyform map is distinguished from the test; loops, parallel edges, and determinant normalization are examined. |
| 3 | [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data\|Gluing Components by Pairing Boundary Data]] | The bilinear law for the full forest polynomial and the passport of the result. States are distinguished from test responses, with two- and three-point examples. |
| 4 | [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry\|The Spanning-Tree Layer and Boundary Resistance Geometry]] | Grove extraction, spanning-tree pairing, the boundary Gram matrix, and the Schur complement. The capabilities and limits of electrical response are established. |
| 5 | [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction\|The Four-Point Passport and State Reduction]] | Reduction from 15 states to 14 coordinates, the distinction between the forest radical and the structural identity, and the general Catalan rank. Minimality concerns linear passports. |
| 6 | [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data\|From the Forest Passport to Spectral Boundary Data]] | A separate two-point passport of minors and a cofactor, Jacobi's identity, and spectral gluing rules. Input and output boundaries for future chains are introduced. |

The table gives a sequential reading order. For a particular task, choose one of these routes:

- **Compute the full forest polynomial:** [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]] → [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]] → [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]. To reduce the retained data, continue to [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]].
- **Connect gluing with electrical networks:** [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#Internal components and groves|the definition of groves]] → [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]. Then [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction#Why this is not the tetrahedron identity|the comparison of two kernels]] explains why spanning-tree relations cannot be transferred to the full passport.
- **Prepare spectral calculations on chains:** [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]] and [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] → [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]]. For comparison with the ordinary forest law, use [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]].

## Which data solve which problem

For a marked boundary $B$, a forest $H$ defines a partition $\pi_B(H)$: two boundary vertices belong to the same block if they are connected in $H$. The full passport coordinates are

$$
\mathcal F_\pi(t)=
\sum_{H:\,\pi_B(H)=\pi}w(H)t^{|E(H)|},\qquad
F_G(t)=\sum_{\pi\in\Pi(B)}\mathcal F_\pi(t)
$$

The sum includes all spanning forests, $w(H)$ is the product of the selected edge conductances, and $\Pi(B)$ is the set of boundary partitions. The boundary vertex names and the component's vertex count are retained alongside the polynomial vector. The latter is needed, in particular, to extract groves; it cannot always be recovered from the polynomials.

The matrix $\mathbf C_B$ marks partition pairs for which joining the corresponding forests creates no cycle. If $\mathbf f_i$ are the passports of two components with disjoint edges, and $\mathbf u_i$ their responses to all contractions, then

$$
\mathbf u_i=\mathbf C_B\mathbf f_i,\qquad
F_{G_1\#_B G_2}(t)=
\mathbf f_1(t)^{\mathsf T}\mathbf C_B\mathbf f_2(t)
$$

Both formulas are proved in [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]]. The exponent of $t$ counts edges, so there is no additional corank factor. A compressed passport preserves every response of this pairing but need not recover every original polynomial $\mathcal F_\pi$.

| Problem | Sufficient data | Essential limitation |
| --- | --- | --- |
| Full forest polynomial of a gluing | All $\mathcal F_\pi(t)$, or coordinates of their class modulo the radical of $\mathbf C_B$ | Free states and actual partition forms satisfy different relations. Reduction is minimal among universal linear passports with a bilinear law. |
| Spanning-tree coefficient of a gluing | Grove weights; for connected parts, also $\tau$ and a boundary resistance Gram matrix in a matched basis | A grove is a forest whose every component meets the boundary. Spanning-tree data do not retain lower forest layers with internal components. |
| Characteristic polynomial under two-point gluing | Five polynomials $A,B,C,D,E$ of the spectral pencil $\xi I-\mathbf L$ | They satisfy $AE=BC-D^2$. Sufficiency is established for a fixed marked pair; moving the active boundary requires a separate transformation. |

These are three computational problems. Electrical response and the spanning-tree scale give a compact description of spanning-tree gluing. The full forest polynomial requires all forest layers, while the characteristic polynomial requires data on rooted weights and on the position of the boundary relative to the eigenspaces.

## Prerequisites and assumptions

The main model is a finite undirected graph with positive conductances and a nonempty marked boundary. Each gluing specifies a boundary-vertex correspondence; internal vertices of the parts are not identified. Parallel edges are distinct instances. If an edge belongs to both original parts but must be counted once in the result, a separately stated rule applies.

Combinatorial forest laws and polynomial spectral laws do not require connectivity. Resistance formulas with invertible Gram matrices are stated for connected parts. Loops produced by contraction belong to no forest; in the incidence-based Laplacian used here, loops contribute zero.

Planarity is not required for the universal forest pairing or for choosing noncrossing partitions as its coordinates. **Circular planarity**, with all boundary vertices on the outer face in a specified order, is required by the theorem used to reconstruct individual grove weights from electrical response. These assumptions are discussed in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry#Limits of reconstruction|the reconstruction limits]].

Useful supporting texts:

- [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients: Grade, Components, and Corank]] and [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]: ordinary coefficients $f_g$, rooted coefficients $p_g$, and the choice of variable degree.
- [[en/Spaces/Vertex Contraction and Graph Gluing|Vertex Contraction and Graph Gluing]], [[en/Structural identities/Partition Forms and the Tetrahedron Identity|Partition Forms and the Tetrahedron Identity]], and [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]]: maps of spaces, structural relations, and the established spanning-tree pairing.
- [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]]: why the boundary choice is part of the data.
- [[en/Foundations/Core specification|Core Specification of PMG]] and [[en/Foundations/PMG terminology|PMG Terminology]]: current notation for forms, the Laplacian, the Greenian, and resistance Gram matrices.

## Provenance and status of the results

Having a proof and having scientific priority are different properties. In the table, “derived in the series” means that the passage from the named foundations to the result is given. It does not assert that the result is absent from other authors' work. Precise references and proofs also appear beside the statements in the substantive notes.

| Result | External source or derivation | Role in PMG | Status of the novelty claim |
| --- | --- | --- | --- |
| Forest states, compatibility, and combination of tables | Mannens–Nederlof [1, Definitions 4.3–4.5, 4.14; Lemma 4.21] | The vector of weighted generating polynomials is called the full forest passport; internal components are retained | Adaptation of an established construction |
| Contraction as a test and passage to test responses | Component counting and a forest bijection in [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test\|Vertex Contraction as a Boundary Test]]; Burgos treats singular forest splittings [3, §§4–5] | The quotient map, the test in the original space, and the variable degree are coordinated | Direct derivation; no independent priority claim |
| Groves, spanning-tree pairing, and electrical data | Kenyon–Wilson [2, Theorem 1.1, §§2.1–2.3, Appendix A]; Schur complements and resistances in Dörfler–Bullo [4] | The spanning-tree layer is connected to the full passport; scale and reconstruction conditions are specified | Established results in PMG notation |
| Spanning-tree law using the determinant of a sum of Gram matrices | Derived from electrical determinant identities and the Schur complement in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry\|The Spanning-Tree Layer and Boundary Resistance Geometry]] | The spanning-tree coefficient formula is distinguished from the metric of the result; basis normalization is specified | Consequence of established identities; no priority claim |
| Four-point reduction and the distinction between two kernels | Explicit forest-matrix calculation in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction\|The Four-Point Passport and State Reduction]]; the compared spanning-tree relation appears in Kenyon–Wilson [2, Lemma 2.3] | The forest relation mixes ranks, whereas the structural identity preserves grade | Calculation and PMG interpretation; no novelty claim |
| Exact Catalan rank | The upper bound of Mannens–Nederlof [1, Theorem 4.2] and the nondegenerate spanning-tree pairing of Kenyon–Wilson [2, §§2.1–2.2]; the series connects them through block antidiagonals | A basis and coordinate count for the full forest pairing on any boundary | Proved consequence of two results; priority for this combination has not been established |
| Minimality of a linear passport | The standard bilinear-form rank bound, applied in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction#In what sense the coordinate count is minimal\|In what sense the coordinate count is minimal]] | The class of passports in which the minimum is attained is specified precisely | A linear-algebra consequence |
| Spectral passport and its gluing law | The classical Desnanot–Jacobi identity [5] and the Schur complement; laws for a shared pair and a shared edge are derived in [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data\|From the Forest Passport to Spectral Boundary Data]] | A separate problem with variable $\xi$, five related coordinates, and explicit counting of shared elements | Application of classical constructions; no independent priority claim |

In particular, the exact rank

$$
\operatorname{rank}\mathbf C_B=
\mathrm{Cat}_{|B|}=\frac{1}{|B|+1}\binom{2|B|}{|B|}
$$

over $\mathbb Q$ or $\mathbb R$ has a general proof in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction#The general Catalan rank|The general Catalan rank]]. The values $2,5,14,42$ for boundary sizes $2,3,4,5$ are computational illustrations. Neither agreement with the dimension of the partition-form space nor these finite checks alone proves the theorem or identifies the two spaces.

The path, star, crossing matching, and electrically indistinguishable components serve as concrete calculations and counterexamples to reconstruction from incomplete data. No priority is claimed for these examples.

## Checks and continuation

The six Russian notes underwent a [joint review (in Russian)](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/REVIEW_RU.md). Their English versions were checked against that edition, including formulas, references, and figure labels. The series contains 21 distinct figures in each language; [six verification programs and SVG reproduction instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) are available. Exact arithmetic compares the formulas with direct enumeration of forests, determinants, cofactors, and ranks. These checks supplement the proofs.

In [[ru/Карта библиотеки PMG|the library roadmap (Russian)]], the series follows [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|the general spectral series]] and precedes “Chains of Cores.” It also continues [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|matroid parameters and forest characteristics]].

For chains, the next step is transforming the passport when the active boundary moves from a core's input to its output. Seam rules, shared edges, and closure must be specified before calculation; closure of a particular transfer automaton on the chosen coordinates needs a separate derivation. The automaton itself and classification of isomers are outside this series. “Spectra of Isomers” and “Spectra of Bipartite Graphs and Mutual Projections” remain separate directions.

## External sources

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [Section 4, especially §§4.2–4.3](https://arxiv.org/html/2307.01046#S4.SS2).
2. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. [Theorem 1.1, §§2.1–2.3, and Appendix A](https://arxiv.org/html/math/0608422v4). In §2.1, the authors ground nonsingularity of the spanning-tree matrix in the meander determinant of Di Francesco–Golinelli–Guitter.
3. J. M. Burgos. *Singularities in Negami’s splitting formula for the Tutte polynomial*. [Section 4, Theorem 4.2; Section 5](https://arxiv.org/html/1605.05499#S4).
4. F. Dörfler, F. Bullo. *Kron Reduction of Graphs with Applications to Electrical Networks*. [§2.1; §3.3, Theorem 11, equation (24)](https://arxiv.org/html/1102.2950).
5. M. Fulmek. *Viewing determinants as nonintersecting lattice paths yields classical determinantal identities bijectively*. [Proposition 2, equation (8), §5.1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p21/pdf/).

[[ru/Граничные полиномы и сочленение графов/Граничные полиномы и сочленение графов|Русский]]
