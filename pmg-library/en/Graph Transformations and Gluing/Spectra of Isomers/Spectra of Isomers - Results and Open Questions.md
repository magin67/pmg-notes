---
title: 'Spectra of Isomers: Results and Open Questions'
date: '2026-11-02'
updated: 2026-11-02
revision: 3
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-results-and-open-questions
order: 0
description: 'Results and navigation: spectral differences, transfer and reconstruction of SLR chains, weaving, periodicity, proved results, and open questions.'
tags:
- spectra
- boundary-data
- forests-and-spanning-trees
- reconstruction
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Спектры изомеров - результаты и открытые вопросы|Спектры изомеров: результаты и открытые вопросы]].

Seam positions between identical cores can change a graph's spectrum while preserving its cycle matroid, ordinary forest coefficients, spanning-tree count, and resistance radius. The series “Spectra of Isomers” follows this distinction from two chains of three hexagons to general spectral transfer, exact reconstruction from boundary data, and recurrences for periodic chains.

Nine substantive notes and this concluding navigator form the current bilingual series. A [series-wide review (in Russian)](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/REVIEW_RU.md) repeated the exact checks and corrected discrepancies. Open questions are listed separately. The English edition preserves the formulas, numerical data, and stated status of each result; its checks are documented in the [English translation review](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/REVIEW_EN.md).

> [!note] The main result in plain language
> Identical hexagonal cores can be joined in different sequences of straight continuations and turns. Their spanning-tree count remains unchanged, while their spectrum may change. The spectrum already determines the number of turns and the number of adjacent turns in the same direction.
>
> Retaining data at two ordered contacts at the end of the chain allows recovery of the entire turn sequence and length. Five exact integers suffice, as do three exactly specified rational numbers of a particular boundary response. Recovery from a single characteristic polynomial or a single number remains conjectural for arbitrary length. With measurement errors, distant differences may become very hard to detect.

## Objects and scope of the statements

The main class consists of finite open chains of cycles $C_6$ with unit conductances. Adjacent cores share exactly one edge, counted once. The input and output seams of an intermediate core have no common vertices; nonadjacent cores do not intersect. There are no other identifications. No planarity, planar layout, or absence of overlaps in a drawing is required: the construction is defined as an abstract graph.

For the number of cores $N\ge2$, the number of vertices $n$, and the internal word $u$, the conventions are

$$
n=4N+2,\qquad |E(G)|=5N+1,\qquad w=Su,\qquad |u|=N-2
$$

The initial S in the full code $w$ is a marker. Internal letters select the output seam: S is the opposite edge, and L and R are the two side outputs. For reconstruction, the ordered terminal pair is chosen on the free edge of the last core opposite its input seam, under the agreed orientation convention. A single hexagon is treated as a separate initial case.

Let $\bar u$ exchange L and R, and let $u^{\leftarrow}$ reverse letter order. The proved classification is

$$
G(Su)\cong G(Sv)
\quad\Longleftrightarrow\quad
v\in\{u,\bar u,u^{\leftarrow},\overline{u^{\leftarrow}}\}
$$

Reflected and reversed descriptions of the same graph are not counted as different isomers. The classification applies to the specified class of open chains; its proof is in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]. Spatial illustrations of constant turns and the correspondence between the code and assembly from paths are discussed in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]].

One result has a wider scope. In [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], closure of five coordinates is proved for attachment of an arbitrary core at exactly two input vertices, with a new output pair in that core and no other contacts. The output may intersect the input. The decoding theorems and scalar conjectures do not have this generality: they use the specific SLR transitions.

## How the data and problems are related

![Connections between configurations, boundary data, spectra, and reconstruction](Connections%20between%20Results%20in%20Spectra%20of%20Isomers.svg)

The spectral passport supports two directions: computing the polynomial of the whole graph and retaining marked data for subsequent attachment or reconstruction. A periodic code turns a sequence of transitions into a power of one matrix. In the diagram, the two-way connection between five integer coordinates and three rational data values holds on reachable states of the chosen class. Scalar inverse problems are marked as conjectures.

Let $\mathbf L_G$ be the Laplacian matrix. The characteristic and rooted polynomials satisfy

$$
\chi_G(\xi)=\det(\xi\mathbf I_n-\mathbf L_G),\qquad
P_G(t)=\det(\mathbf I_n+t\mathbf L_G)
$$

$$
\chi_G(\xi)=\xi^nP_G(-1/\xi),\qquad
P_G(1)=(-1)^n\chi_G(-1)=\chi_G(-1)
$$

The first equality is understood as a polynomial identity, including $\xi=0$; the last uses evenness of $n$. The coefficient $p_j$ of $P_G(t)=\sum_jp_jt^j$ counts spanning forests with $j$ edges and a chosen root in every component. The ordinary forest polynomial $F_G(t)$ counts the same forests without choosing roots. These polynomials are not interchangeable.

The five polynomial passport coordinates are denoted by $(A,B,C,D,E)$. The first is $\chi_G$; the others are principal minors and a mixed cofactor of the pencil $\xi\mathbf I_n-\mathbf L_G$. Deleting rows and columns does not entail recomputing vertex degrees. Jacobi's identity gives

$$
AE-BC+D^2=0
$$

Thus the five coordinates are not claimed to be algebraically independent. Their sufficiency for linear transfer also does not establish minimality among all possible encodings.

> [!info] Three different inverse problems
> **Established status.** The full marked boundary vector at $\xi=-1$ recovers the oriented word and its length: this is proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]. Equivalent recovery from three exact rational data values is proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]].
>
> Recovery of the unmarked class from $\chi_G$ and from a single value $P_G(1)$ are separate problems. The general statements are formulated as conjectures in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]].

In the positive forest normalization, the full vector is $\mathbf Z=(a,b,c,d,e)^{\mathsf T}=(A,-B,-C,-D,E)^{\mathsf T}|_{\xi=-1}$. For the terminal pair $\mathcal B=(x,y)$, the three rational data values form the symmetric matrix

$$
\mathbf K_{\mathcal B}
=\bigl((\mathbf I_n+\mathbf L_G)^{-1}\bigr)_{\mathcal B\mathcal B}
=\frac1a\begin{pmatrix}b&d\\d&c\end{pmatrix}
$$

This is a block of the inverse matrix $\mathbf I_n+\mathbf L_G$. Under the convention $\mathbf M_G(\xi)=\xi\mathbf I_n-\mathbf L_G$, the resolvent block at $\xi=-1$ is $-\mathbf K_{\mathcal B}$. The matrix $\mathbf K_{\mathcal B}^{-1}$ is the shifted boundary response. Primitivity of the reachable integer vector recovers the scale lost by division by $a$. Neither $N$ nor $P_G(1)$ needs to be known in advance. Exact rationals may have large denominators; three numbers do not mean a bounded amount of information or a fixed measurement precision.

The response can be obtained by processing dynamics on the original graph: two initial excitations, one at each contact, give four time records, and reciprocity makes the two cross-records equal. Three integrals specify the matrix; minimality of the data count is not claimed. An auxiliary electrical model with a separate unit resistor between every vertex and a common ground realizes the same matrix $\mathbf I_n+\mathbf L_G$. This is one interpretation of the spectral shift; it imposes no minimum-neighbor condition on the original vertices. Ordinary resistance between the endpoints of the chosen free terminal edge depends only on $N$ and does not distinguish the turn order. The electrical, dynamic, and probabilistic interpretations are reconciled in [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]].

## Summary of results

“Proved” below refers to a general statement under the assumptions of its note. Finite calculations additionally check implementations; they do not replace proofs for all lengths.

| Result and scope | Status | Where to read |
|---|---|---|
| The specified pair of three-hexagon chains has the same matroid parameters but different spectra; $\chi_{\mathrm A}-\chi_{\text{B}}=\xi^2(\xi^2-5\xi+5)^4$ | Formula proved; polynomials independently checked by rooted forests | [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons\|Two Isomers of Three Hexagons]] |
| Five polynomial coordinates are closed under the stated two-vertex attachment and change of active pair | Proved for an arbitrary attached core under the theorem's assumptions | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary\|Spectral Transfer to a New Boundary]] |
| Every SLR word defines an admissible chain; isomorphism is equivalent to membership in one orbit of four symmetries | Proved for all lengths in the main class | [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains\|SLR Codes of Hexagonal Chains]] |
| The local S/L difference has rank 2; mixed differences obey recurrences depending on the orientation convention | Proved matrix identities | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains\|Spectral Differences of SLR Chains]] |
| The spectrum recovers the number of bends and the number of adjacent LL or RR pairs | Proved through the fourth and sixth moments | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] |
| Any fixed number of leading rooted coefficients is insufficient for all sufficiently long chains | Proved for each fixed number of coefficients | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] |
| The full marked vector of five integers determines the oriented code and length; a terminating reachability criterion exists | Proved for every finite length | [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State\|Rooted Forests and Decoding the Boundary State]] |
| Three exact rational entries of $\mathbf K_{\mathcal B}$ determine the same code and length | Sufficiency proved; minimality of three data values not established | [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response\|Reconstructing a Chain from Its Boundary Response]] |
| No uniform positive absolute response accuracy suffices for all lengths; for bounded $N$, a sufficient error bound exists | Both statements proved; no optimality claimed | [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response\|Reconstructing a Chain from Its Boundary Response]] |
| A fixed marked runner gives a constant SLR turn; minimal homogeneous orders are 4 for S and 5 for L, R | Proved over $\mathbb Q(\xi)$ for the specified families | [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns\|Weaving SLR Chains and Constant Turns]] |
| Transfer for every period has multiplier 1 and a reciprocal quartet; for LR, SL, LLS the minimal homogeneous order is 5 | General structure proved; minimality established for the three named periods | [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra\|Periodic SLR Chains: Recurrences and Spectra]] |
| Phases $(LLS)^m$ and $(LSL)^m$ have different finite spectra at $m\ge1$, but the same limiting growth of rooted forest counts per core | Proved for all $m$ in the specified families | [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra\|Periodic SLR Chains: Recurrences and Spectra]] |
| Across all 16,150,725 unmarked classes with $2\le N\le18$, the values $P_G(1)$ are distinct | Exhaustive exact computational check of this range | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] |
| The characteristic polynomial determines the unmarked class at every length | Working Conjecture 1 | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] |
| A single value $P_G(1)$ determines the unmarked class for every fixed known $N$ | Working Conjecture 2, which is stronger | [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] |

The conjecture about $P_G(1)$ at fixed $N$ does not include recovery of an unknown $N$ from one number. Separation between size ranges is also checked in the finite catalog, but no general result across sizes follows. Likewise, neither conjecture asserts determination of an SLR chain by its spectrum among all graphs.

## Weaving, the exponential, and periodic transfer

Attaching a path $P_6$ with six vertices and five edges to an existing edge adds the next hexagon. The ordered plug specifies the input contact matching, while the socket choice specifies S, L, or R. Repeating a single marked runner realizes a constant turn; repeating a composite runner realizes a periodic word.

The foundations of this description are in the “Chains of Cores” series: [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]] and [[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving|The Laplacian Exponential in Graph Weaving]]. These two notes belong to the neighboring series and support the spectral continuation.

In the polyform exponential, a new attachment multiplies the previous expression by a factor embedded into new vertices. In reduced boundary coordinates, the same process is described by a growth operator. The Laplacian form $L$, its matrix $\mathbf L$, the exterior exponential $\exp L$, and the transfer matrix must be distinguished. A power of the transfer matrix is neither a power of the Laplacian nor a single unchanged factor in a fixed vertex space.

For a period $v=\beta_1\cdots\beta_p$ and the family with internal word $v^m$,

$$
\mathbf V_v=\mathbf U_{\beta_p}\cdots\mathbf U_{\beta_1},\qquad
\chi_{G_m^{(v)}}(\xi)=\mathbf r\mathbf V_v^{\,m}\boldsymbol s_1
$$

Here $N=pm+2$: the two end cores are counted separately. For runners starting directly from an edge, $N=pm$, and the initial conditions differ. The Cayley–Hamilton theorem gives a recurrence in the number of periods. Its minimal order depends on the period itself, the end conditions, and the specialization of $\xi$.

Cyclically shifting the period letters preserves the characteristic polynomial of $\mathbf V_v$ but may change the polynomial of the finite graph. Transfer multipliers describe growth in $m$; Laplacian eigenvalues are the roots of $\chi_G(\xi)$ in $\xi$. Exact examples for LR, SL, and LLS illustrate this distinction in [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra|Periodic SLR Chains: Recurrences and Spectra]].

## Contents and reading routes

| Note | Main problem |
|---|---|
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons\|Two Isomers of Three Hexagons]] | An exact pair of graphs, two polynomials, and a compact difference |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary\|Spectral Transfer to a New Boundary]] | Sufficient data for attachment and a change of active pair |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains\|SLR Codes of Hexagonal Chains]] | Orientations, symmetries, and graph classification |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains\|Spectral Differences of SLR Chains]] | Changing one or several seams and the first sensitive coefficients |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State\|Rooted Forests and Decoding the Boundary State]] | Forest meanings of the coordinates, the inverse algorithm, and reachability |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response\|Reconstructing a Chain from Its Boundary Response]] | Three rational data values, interpretations, and stability |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns\|Weaving SLR Chains and Constant Turns]] | A fixed runner and recurrences for constant families |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] | Partial recovery, a finite catalog, and scalar conjectures |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra\|Periodic SLR Chains: Recurrences and Spectra]] | The period matrix, phase, ends, and rooted-forest asymptotics |

For a first introduction, read [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]] and the plain-language result section in [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]]. They show which differences arise and which data recover them.

For spectral calculation, follow [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]] → [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] → [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]]. For repeated constructions, continue through [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]] to [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra|Periodic SLR Chains: Recurrences and Spectra]].

For the inverse problem, follow [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] → [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]] → [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response|Reconstructing a Chain from Its Boundary Response]]. The passage to unmarked scalar data is studied in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]].

## Foundations and provenance of the results

The mathematical foundations are determinants and minors, the Schur complement, matrix-forest identities, Newton's identities, and the classical transfer-matrix method. The series applies them to explicitly specified seams, orientations, and end conditions. A separate proof or a polyform expression does not establish scientific priority.

| Result | Source or derivation | Role in PMG | Novelty status |
|---|---|---|---|
| Forest meaning of the determinant and cofactors of $\mathbf I+\mathbf L$ | Chebotarev–Shamis Theorems 5–6; attribution in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State\|Rooted Forests and Decoding the Boundary State]] | Meaning of five integer coordinates and their spectral connection | Classical identities |
| Five coordinates and transfer to a new pair | Jacobi, Schur complement, and a separate determinant derivation in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary\|Spectral Transfer to a New Boundary]] | A closed rule for sequential assembly | Derivation provided; priority not established |
| Ternary code and chain symmetries | Classical description of hexagonal chains by Milosavljević–Stevanović; classification and Burnside's lemma in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains\|SLR Codes of Hexagonal Chains]] | Agreement between oriented words and unmarked graphs | Classical encoding; priority of the specialization not established |
| Decoding, the primitive scale, and stability bounds | Specific proofs for SLR transitions in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State\|Rooted Forests and Decoding the Boundary State]] and [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response\|Reconstructing a Chain from Its Boundary Response]] | The inverse problem and its quantitative limitations | Proved in the series; scientific priority not established |
| Probabilistic interpretation of the response | Avena–Gaudillière stopped walks and root law, Lemma 3.3 and Theorem 3.4; comparison in [[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response\|Reconstructing a Chain from Its Boundary Response]] | Equivalent specifications of the three data values | Adaptation of classical results |
| Scalar recurrences, generating functions, and growth | Cayley–Hamilton and the transfer method; specific coefficients and certificates in [[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra\|Periodic SLR Chains: Recurrences and Spectra]] | Fast computation for repeated constructions | Classical method; priority of the particular formulas not established |
| Moment formulas and the distinguishability catalog | Moment method, Newton's identities, and exact enumeration in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains\|Spectral Distinguishability of SLR Chains]] | Partial recovery and finite-range tests of conjectures | Specific derivations and calculations; priority not established |

Precise references and comparisons of assumptions appear alongside the results in the linked notes. General transfer theory, such as Molinari's work on determinants of block tridiagonal matrices, is not claimed as a source of specific SLR coefficients or a proof of their injectivity.

## Open questions

**Full scalar distinguishability.** Prove or refute the two conjectures in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]]. Word comparisons must account for reflection and reversal. Recovery of an unknown length from $P_G(1)$ should be posed separately from the conjecture for fixed $N$.

**Stability and practical reconstruction.** Find sharper bounds on response separation for bounded core counts, study error accumulation in the inverse algorithm, and investigate measurement choices. The theorem on exact rational data does not provide stable recovery from measurements of fixed precision. Applying a dynamic or electrical scheme in an experiment requires its own error model.

**Arbitrary periods and end conditions.** Determine when the homogeneous order is below five, which special $\xi$ lower it, and when different periods or phases have identical finite spectra. The reciprocal structure of the period matrix is proved; classification of all scalar recurrences remains a problem.

**Other cores and larger boundaries.** Determine which families combine closed transfer with an injective decoder, and which data are needed for boundaries of three or more vertices. Sufficiency of a fixed-boundary passport, closure under boundary transfer, and minimality of the number of coordinates require separate statements.

**Closures and infinite chains.** A ring requires retaining the initial boundary and explicitly specifying the final contact matching. An infinite model requires a definition of the operator, boundary conditions, and the meaning of the limit. Growth of rooted forest counts in finite graphs does not replace a theory of spectral bands of an infinite chain.

These directions continue the research. Completing the current collection records the results presented and their limits, without presuming solutions to these problems.

## Reproducibility and the place of the series in the library

The [verification directory](https://github.com/magin67/pmg-notes/tree/v5/checks/isomer-spectra) contains programs, exact data, and figure sources. The [reproduction guide](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) separates direct determinants, forest enumerations, symbolic identities, decoder checks, and the large catalog of classes.

In particular, the [distinguishability catalog](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/slr-distinguishability-catalog.json) records $2\le N\le18$ and 16,150,725 classes without collisions of $P_G(1)$. The [periodic checks](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/periodic-slr-results.json) contain 35 polynomial comparisons for chains with end cores and 28 for runners starting from an edge. These counts refer to different checks and cannot be added into a count of proved cases of general injectivity.

This navigator brings together published proofs and computational results; it adds no new enumerations or theorems.

The primary section is [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]: the series sits alongside “Chains of Cores” and boundary polynomials. An additional entry point is [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]], through spectral invariants and configuration recovery.

Required foundations: [[en/Graph Transformations and Gluing/Chains of cores/Chains of Cores|Chains of Cores]] specifies admissibility and matroid invariance; [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]] separates a fixed-pair passport from transfer; [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]] distinguishes spectra, projectors, and operators; [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] reconciles forest normalizations. General entry point: [[en/Thematic Index|Thematic Index]].
