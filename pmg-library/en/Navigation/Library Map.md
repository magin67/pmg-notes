---
title: Library Map
date: 2026-11-11
updated: 2026-11-11
revision: 1
status: published
text_prepared_by: ChatGPT
lang: en
translation_key: pmg-library-map
order: 0
description: "Research directions, published series, connections, and open questions."
---

This map brings together the published series, research directions, and planned continuations of PMG. It summarizes the current research plan and links to the notes that develop each topic. The detailed editorial chronology is recorded in the Russian map.

[[ru/Навигация/Карта библиотеки|Русский]] · [[en/Navigation/Navigation|Navigation]]

## How to use the map

The [[en/Navigation/Thematic Index|Thematic Index]] groups series by their main question and provides search by tags. Series navigators specify prerequisites and reading routes.

Research codes retain the Cyrillic letters used in the Russian map so that each direction has the same identifier in both languages. A direction can span several series, and a series can cover several directions. The codes support cross-references and discussion.

Preparation states describe the material available to readers.

- **Public foundation** means that the introductory series or reference documents cover the basic construction.
- **Published and checked** means that the relevant texts and their presentation have been reviewed.
- **Complete in its current scope** means that the agreed set of notes is available in both languages, with navigators and the checks specified for that series.
- **To review** means that sources, definitions, prerequisites, or the proposed scope require examination.
- **Planned** means that a continuation has been agreed, with its position or date still open.
- **To investigate** means that the construction, conditions, or applications require further research.

Each mathematical claim has its own status in the note where it appears. The library distinguishes proofs, direct calculations, checks on examples, and working conjectures. A completed series can contain open questions.

## Published series

The library contains 18 bilingual series with 131 substantive notes in each language. Navigators, reference documents, the introductory bibliography, and programming examples are counted separately.

| Series | Directions | Notes per language |
| --- | --- | ---: |
| [[en/Getting Started and Foundations/Introduction/PMG Introductory Series\|PMG Introductory Series]] | О01-О05 | 10 |
| [[en/Polyform Algebra and Combinatorics/Structural identities/Structural Identities\|Structural Identities]] | А02 | 5 |
| [[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Symmetric Polyforms\|Symmetric Polyforms]] | А01 | 5 |
| [[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Combinatorial Potentials\|Combinatorial Potentials]] | А07 | 6 |
| [[en/Polyform Algebra and Combinatorics/Partition toponomes/Partition Toponomes\|Partition Toponomes]] | А03 | 6 |
| [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Polynomial Toponomes\|Polynomial Toponomes]] | А03 | 5 |
| [[en/Resistance Geometry and Duality/Spaces/Spaces\|Spaces]] | Г01-Г02 | 9 |
| [[en/Resistance Geometry and Duality/Metric parameters/Metric Parameters of Graphs\|Metric Parameters of Graphs]] | Г03-Г04, С06 | 8 |
| [[en/Resistance Geometry and Duality/Greenian and polyform duality/Greenian and Polyform Duality\|Greenian and Polyform Duality]] | Д01-Д03 | 9 |
| [[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distributions and Edge Influence\|Metric Distributions and Edge Influence]] | А04, Д04 | 4 |
| [[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs\|Matroid Parameters and Forest Characteristics of Graphs]] | С02 | 7 |
| [[en/Invariants, Decompositions, and Spectra/KVP decomposition/KVP Decomposition and Oriented Extensions\|KVP Decomposition and Oriented Extensions]] | А05 | 9 |
| [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra\|Spectra and Diagonalization in Polyform Algebra]] | С03, С07 | 6 |
| [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations\|Laplacian, Greenian and Resistance Variations]] | О03, О05, Д02 | 8 |
| [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing\|Boundary Polynomials and Graph Gluing]] | С08 | 6 |
| [[en/Graph Transformations and Gluing/Chains of cores/Chains of Cores\|Chains of Cores]] | С01 | 7 |
| [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions\|Spectra of Isomers]] | С04 | 9 |
| [[en/Directed Graphs and Extensions/Balanced graphs/Balanced Graphs\|Balanced Graphs]] | А06 | 12 |

The [[en/Getting Started and Foundations/Foundations/Core specification|Core Specification]] and [[en/Getting Started and Foundations/Foundations/PMG terminology|PMG Terminology]] record the current definitions and conventions. The [[en/PythonExamples/PythonExamples|Programming Examples]] provide executable calculations and notebooks.

## Foundations

| Code | Direction | Scope and preparation state |
| --- | --- | --- |
| О01 | Basic polyform algebra | Points, affine vectors, simplices, boundaries, grades, forms, products, merging, and annihilation. The public foundation is available. A separate treatment of the algebra and its notation is planned. |
| О02 | Laplacian and metric polyform | Coupling forms, the Laplacian exponential, forest expansion, the top-grade component, and the spanning-tree coefficient. Public foundation. |
| О03 | Potentials, norms, and variations | Top-coefficient extraction, metric evaluation, direct and inverse variations, independent resistances, quadric connectivity, and conductance constraints. Public foundation and a completed eight-note variation series. |
| О04 | Resistance geometry and electrometry | Resistances, inner products, areas, volumes, electrical interpretation, and the original motivation for PMG. The foundation is available. Specialized applications require review. |
| О05 | Matrix representations and transformations | Laplacian, Green matrix, resistance matrix, distance operator, centering, and finite variation equations. The symmetric constructions are published. Other extensions require separate review. |

## Algebraic directions

| Code | Direction | Scope and preparation state |
| --- | --- | --- |
| А01 | Symmetric polyforms | Fundamental theorem, normalizations, products, powers, complete-graph exponential, forest coefficients, and Abel polynomials. Five bilingual notes. |
| А02 | Structural identities | Partition forms, noncrossing bases, Narayana and Catalan dimensions, the four-block identity, spanning-tree pairing, and support decomposition of relations. Five bilingual notes. |
| А03 | Partition reduction and polynomial toponomes | Toponomes of a chosen representation, the algebra of the second kind, coefficient tables, vector and vertex normalizations, forest coefficients, the Laplacian polynomial, Kirchhoff indices, factorization, and graph realizability. Two completed series of six and five notes. |
| А04 | Metric distributions and path intersections | The operator $D_L$, edge influence, the tree model, and higher grades. Covered jointly with Д04 by the four-note metric distribution series. |
| А05 | KVP and oriented extensions | Pair-data decompositions, projectors, KVPO/KVPOU, distance transformation, the Green matrix, resistances, metric parameters, potentials, and applications. Nine bilingual notes and exact checks. |
| А06 | Balanced graphs and directed-cycle polyforms | Balance, spanning-tree potentials, the bilinear Laplacian and exponential, circulation, directed geometry, the Gram matrix, spheres, in/out coordinates, balancing, directed forests, and permutation digraphs. Twelve bilingual notes. |
| А07 | Combinatorial potentials | Ordinary and cyclic partitions, potentials of the first and second kinds, path-cycle states, symmetric-polyform representations, forest counts, Cayley-Moon formulas, finite differences, and Stirling numbers. Six bilingual notes. |
| А08 | Permutations, invariants, and Galois theory | The action of $S_n$ on partition forms and structural relations, permutation cycles, and polynomial resolvents with a specified field and scalar realization. A research direction building on А01, А02, and А07. Its scope as a separate series is open. |

## Geometry and subspaces

| Code | Direction | Scope and preparation state |
| --- | --- | --- |
| Г01 | Basis subspaces and coordinates | Spaces and forms, projections, bi- and di-coordinates, contraction and gluing, the Dirichlet problem, vertex elimination, and induced couplings in a bipartite class. Nine bilingual notes in Spaces. |
| Г02 | The null vector and isotropic model | Affine weight, local and nonlocal elements, spheres and their centers, exterior products, and the boundary operator. The basic construction is published in Spaces. Sphere normals and constant-curvature geometry have separate continuations. |
| Г03 | Circumcenter and resistance radius | Center coordinates, radius, diameter, Gram matrix, volume, centroid decomposition, subsets, and graph changes. Published in Metric Parameters of Graphs. Multipoint forest and spanning-tree gluing laws appear in С08. |
| Г04 | Connectivity center | The Laplacian sphere center $(\beta,\sigma)$ and its relation to the resistance center, electrical and diffusion interpretations, degree potential, and vertex ranking. Covered by Sphere Centers and Graph Heterogeneity and Degree Potential and Centralities. The notes specify the conditions for weak-cut sensitivity and coincident centrality rankings. |
| Г05 | Interval forms | Intervals as quadratic forms, directed boundaries, intersections, and unbounded regions. Sources and the relation to reduction constructions require review. |

The terminology follows the current specification. In particular, the boundary of a Dirichlet problem and the boundary operator of the algebra have their own definitions. Comparisons with external coordinate terminology require checking those definitions.

## Cuts, duality, and distributions

| Code | Direction | Scope and preparation state |
| --- | --- | --- |
| Д01 | Cuts and cut forms | Vertex partitions, crossing edges, indexing forests, block-sum forms, and the cut representation of the Greenian. The algebraic construction and forest coefficients are published. A general theory of cuts has a separate scope. |
| Д02 | Greenian and polyform duality | Vector forms, boundary exponentials, mutual duality, signed coefficients, cut representations, normalizations, vertex variations, and form potentials. Nine bilingual notes, a navigator, and exact checks. |
| Д03 | Greenian toponomes and dual pairs | Grouping the canonical vector forest expansion by component types, comparison with Laplacian toponomes, and rooted spectral evaluations. The basic construction and spectral relation are proved. A general transformation of full toponomes remains open. |
| Д04 | Metric distributions and edge influence | Relative sensitivity, distribution of a form's value, and metric variations. Four bilingual notes jointly with А04 cover edge influence, trees, graphs with cycles, and higher grades. |

For a cut, the vertex partition, its crossing-edge set, and spanning two-component forests with those vertex sets carry different information. Each distribution specifies its input object, coefficients, their sum, and the metric evaluation. Comparisons of constructions must check these data and their normalizations.

## Graph structure, invariants, and spectra

| Code | Direction | Scope and preparation state |
| --- | --- | --- |
| С01 | Chains of cores | Admissible chains and seams, active-boundary transfer, matroid invariance, spanning-tree recurrences, limits of applicability, ordinary closure, twisted closure, and graph weaving. Seven bilingual notes. Open hexagonal-chain classification is developed in С04. Other cores and composite cores remain research topics. |
| С02 | Matroid parameters and forest characteristics | Cycle matroids, forest coefficients and duality, power-sum parameters, scales, edge characteristics, the resistance radius, and gluing laws. Seven bilingual notes and exact checks. |
| С03 | Spectra of paths and cycles | Explicit modes and projectors, common eigenbases, polynomial transformations, and the Chebyshev relation between paths and cycles. The principal treatment is included in С07. |
| С04 | Spectra of isomers | Spectral transfer, SLR classification, decoding the full marked boundary state, reconstruction from three exact rational data, stability, partial spectral reconstruction, and periodic LR, SL, and LLS chains. Nine bilingual notes. General scalar distinguishability remains a conjecture. |
| С05 | Bipartite spectra and mutual projections | Relations between the spectra of the original graph and the induced graphs, subspace angles, and the shared spanning-tree parameter. A deferred continuation of Г01 requiring review of its scope and normalizations. |
| С06 | Metric graph characteristics and centralities | Centroid, spanning-tree, and spectral centralities, degree potential, two simplex centers, density, compactness, tree invariance, and two forms of vertex removal. Covered by the eight-note metric series together with Г03 and Г04. |
| С07 | Spectra and diagonalization in polyform algebra | Space, metric, operators, eigenspaces, projectors, diagonal grades, duality, operator reconstruction, cones, projections, paths, and cycles. Six bilingual notes. |
| С08 | Boundary polynomials and graph gluing | Full boundary forest states, contraction tests, pairing, coordinate reduction, the spanning-tree layer, and a separate passage to spectral boundary data. Six bilingual notes with exact checks and source attribution. |
| С09 | Infinite lattices and limits of finite graphs | One-dimensional core chains, triangular, square, and hexagonal planar lattices, and three-dimensional models. Laplacians, Greenians, resistances, spectra, spanning-tree characteristics, finite fragments, and limits require comparison with classical theory. The possible PMG contribution and publication scope are open. |

## Connections between directions

The following relationships help locate prerequisites and continuations. Individual series navigators give the reading routes.

| Directions | Connection |
| --- | --- |
| О03, О05, Д02, Г01 | Variations connect exterior-exponential factors to exact matrix updates, independent resistances, and mutually inverse differential-response matrices on the complete set of vertex pairs. Partial resistance data with conductance constraints lead to a separate realizability problem. |
| А01, А02, А03 | Structural identities support symmetric forms and reduction to partitions. Particular results specify which identities they require. |
| А07, А01 | The second-kind potential counts partitions of a prescribed type. The combinatorial series explains forest coefficients through coding and a bijection with $r$-Stirling numbers. Cayley-Moon and Abel counting arguments also have independent combinatorial proofs. |
| А03, А04 | Partition and toponome reduction use type data. Metric distribution $D_L$ uses sensitivity in a fixed edge representation. A correspondence between these operations requires a separate construction. |
| А05, А06 | Balanced graphs, directed cycles, and circulation connect to KVP components. Their component interactions and duality are research continuations. |
| А03, А06 | The balanced series constructs directed forest toponomes and determinant vertex reduction. Multiplication of general reduced types, directed matroid inequalities, and realizability remain open. |
| Г01, Г02 | Affine-vector spaces, metric restriction, and the Dirichlet problem use the published core. The isotropic model supplies the geometry of local points and element centers where required. |
| Г02, Д01, Д02 | The Green matrix, exterior exponential, and inner product define the Greenian and mutual duality. Cut representations are derived within the duality series. |
| А03, Д02, Д03 | Canonical signed forest expansions admit grouping by component type. Rooted spectral polynomials have a proved dual relation. The full correspondence of types remains open. |
| А04, Д04, О03, О05 | In grade $k$, $D_L$ is a distribution on $k$-edge sets. Summing contributions over sets containing an edge gives its relative sensitivity. For $k>1$, these marginals generally lose information about the full distribution. |
| А04, Д01, Д04, Г05 | Historical spanning-tree averaging, complementary-grade forest distributions, and oriented interval intersections require comparison of their inputs and normalization with $D_L$. |
| Г03, С01, С02 | The matroid formula for the resistance radius, one-point gluing, and Whitney flips support invariance results for admissible chains. Boundary choices and chain closures require their stated conditions. |
| Г03, С06, О02, О03, Д01 | Potentials and Laplacian-exponential grades express radius, volume, vertex parameters, and spanning-tree ratios. С02 develops forest and matroid relations, С08 boundary laws, and С01 chain applications. |
| Г03, Г04, С06, Д02, А05 | Laplacian and Green Gram matrices define two simplex geometries. Degree potential relates the Laplacian center to vertex heterogeneity. The stated centrality coincidences on unit trees have explicit hypotheses. |
| А03, С03, С07, С04 | Diagonal grades, projectors, Chebyshev transformations, cones, and projection losses provide spectral foundations. Reconstruction from spectra has the limitations described in С07 and С04. |
| А02, С02, С07, С08, С01 | Boundary forest passports extend spanning-tree pairing through groves and support active-boundary transfer and closure. Ordinary forest states and spectral-pencil minors use distinct definitions. |
| С01, С04, С07, С08, С09 | Finite chains and periodic recurrences motivate lattice models. Higher-dimensional extensions require a cell, intercell couplings, boundary conditions, and a justified limiting process. |
| Г01, С05 | Mutual projections of bipartite classes relate to induced graphs and the shared spanning-tree parameter. Spectral objects, angles, and normalizations need further review. |

## Deferred questions and continuations

The current phase concerns the clarity and presentation of published material. Research continuations retain the preparation states listed below. A completed treatment can establish a starting point for a broader question.

| Question | Direction and remaining work | Preparation state |
| --- | --- | --- |
| Permutation-invariant KVP operators and quadratic forms | А05. Formulate scalar action on K, V, and P for pair tables, handle small $n$, and examine mixing between repeated components in arbitrary symmetric matrices. | Pair-table result to write up. Matrix extension to review. |
| Centroid representations and factorization of K and V | А05, О01. Derive expressions using centered vertices and products of quadratic-form exponentials, with their dependencies and normalizations. | Formulas to write up and check. |
| Coupling concentration and quadratic Laplacian moments | А05, С03, С05. Relate effective edge count, degree moments, component coefficient norms, and the Laplacian Frobenius norm. Check the metric meaning of each norm. | Identities to write up. Applied interpretation to review. |
| Resistance sensitivity along KVP directions | А05, Д02, С06. Derive Green-matrix and resistance derivatives along K, V, and P within the admissible conductance region, and compare them with the dual form. | Formulas to write up and review. |
| Covariance interpretations and graph comparison | А05. Specify a probability model, centering, normalization, correspondence between vertex sets, scale, and stability. | To investigate. |
| Higher potentials and exterior powers | А05, А01, А02. Study higher-order invariants, induced metrics, and mixed terms, including polyforms whose higher grades are independently specified. | To investigate. |
| P-toponome ranks and completeness of mixed data | А05, А03. Obtain reproducible exact ranks for grades five and higher and examine the general rank conjecture and the distinguishing power of joint KVP data. | General conjecture and distinguishability to investigate. |
| O and U in exponentials, toponomes, and duality | А05, А06, А03, Д02-Д03. Develop mixed coefficients involving O and suitable models for U in general digraphs. | Component extension to investigate. |
| KVP electrometry on real data | А05. Test noise, incomplete measurements, realistic electrodes, recovery of P, and the limits of the contact model against baseline processing. | Experimental effectiveness to investigate. |
| Component evaluations and spectral representations | А03, С07. Extend the published symmetric spectral foundation to independent higher grades, full-toponome transformations, and nonsymmetric balanced-graph spectra. | Basic treatments published. Extensions to investigate. |
| Multicomponent gluing | А03. Describe interactions where one component meets several components of another factor, including vertex data, coefficients, cycles, and associativity. | To investigate. |
| Historical transformations and interval forms | А04, Д01, Д04, Г05. Compare spanning-tree averaging, complementary-grade distributions, and oriented intersections with metric distributions. | Deferred. Series placement open. |
| Distinguishing graphs by toponomes and coefficient tables | А03, С04. Identify sufficient data for reconstruction within specified graph classes and examine richer data beyond grade and component-count tables. | To investigate. |
| Greenian toponomes and dual pairs | Д03. Extend the published canonical forest construction and rooted spectral relation to a general transformation of full toponomes. | Basic construction published and checked. General transformation open. |
| Polyform algebra and its notation | О01. Explain form multiplication, quadratic dependence, polarization, and the relation to double forms. Review proposed shorthand against existing simplex notation. | Planned. |
| A Fourier transform on polyforms | О01 with О02, О03, Д02. Define the function space, independent variables, exponential kernel, top-coefficient extraction, inversion, basis dependence, and action on mixed forms. Compare finite nilpotent-variable transforms and Hodge duality. | To investigate. |
| Partitions and combinatorial coefficients | А07, А01, А02, А03, А06. Ordinary and cyclic potentials and mixed path-cycle counting are available. General algebraic operations on labeled states have a separate continuation. | Basic treatment and first-kind potential published in both languages. |
| Permutations, invariants, and Galois theory | А08. Study the $S_n$ action on partition forms and structural relations, beginning with four vertices. A Galois correspondence would require a specified field, polynomial, and scalar realization. | To investigate. |
| Graph symmetry and symmetric parts of its exponential | А01, А02. Study full permutation symmetry, graph automorphisms, symmetric grades, and averaging operators beyond the complete-graph examples. | To investigate. |
| Spectral relations between bipartite classes | Г01, С05. Specify spectral objects, normalization, projection angles, and their relation to the shared spanning-tree parameter $J(G)$. | To review. |
| Balanced graphs and directed-cycle polyforms | А06, А03. The introductory construction, symmetric limit, and two forest normalizations are available. General reduction algebra, directed matroid inequalities, and KVP links have separate continuations. | Introductory series published in both languages. |
| Regular balanced graphs and component probabilities | А06, А07. Fix a model for loopless labeled digraphs of in/out degree $d\ge2$ and study counts, connected components, type distributions, and expected component sizes. | To investigate beyond the introductory series. |
| Partition algebra with labeled components | А07, О01. Define products of open paths and closed cycles, the unit, associativity, coefficients, and potential behavior. Compare existing path-cycle constructions. | Research deferred. |
| Resistance symmetrization of a balanced graph | А06, Г02. Reconstruct a symmetric Laplacian from $R_{ij}=r_{ij}+r_{ji}$, determine nonnegative-coupling conditions, and examine preserved metric parameters. | To investigate. |
| Refined directed-forest types | А06, А03. Determine the additional component data needed for toponome multiplication. | To investigate. |
| Circulation polyforms and electrodynamics | А06. Define a correspondence with electromagnetic fields and identify physical examples of pure-circulation polyforms. | To investigate. |
| Circulation, discrete connections, and holonomy | А06. Seek a precise interpretation of circulation norm through transport around a closed contour. | To investigate. Publication placement open. |
| Isotropic model and Minkowski space | Г02. Establish the mathematical correspondence and the additional assumptions required for a physical interpretation. | Planned. |
| Sphere normals and constant-curvature geometry | Г02. Examine how choices of normal and section affect the geometric model. | To review. |
| Metric polyform of the isotropic extension | Г02, Д02. Express metric evaluations involving point representatives and the null vector through a polyform. | To review. |
| Multipoint gluing and chains of cores | С08, С01, С04. The current boundary and chain constructions are available. Scalar spectral distinguishability, other cores, composite cores, and further closure problems retain their individual scope. | Boundary and chain series complete in their current scope. Continuations retained. |
| Infinite lattices and finite-graph limits | С09. Compare classical results, define valid limiting constructions, and identify the possible contribution of PMG in one, two, and three dimensions. | Scope and contribution to investigate. |
| Splitting a graph at vertices | А02. Define shared vertices, splitting into copies, edge assignment, choices, and nonuniqueness. | Planned. |
| Splitting a graph along edges | А02. Compare with vertex splitting and determine whether a separate treatment is needed. | To review. |
| Matroid parameters and forest characteristics | С02, С08, С01. Matroid determination and gluing laws are treated separately in the published scalar, boundary, and chain constructions. | С02 and its current boundary continuation complete in both languages. |
| Resistance radius after deleting a vertex and its edges | Г03, С06. Seek a compact expression in terms of a small set of original-graph vertex characteristics. The new-metric calculation and metric-preserving elimination are already described. | To review. Compact formula open. |

The corresponding series navigators link to the results underlying these questions. The [[ru/Навигация/Карта библиотеки#Отложенные вопросы и продолжения|detailed Russian register]] records the originating notes, external comparisons, and the history of each continuation.

## Editorial work and next steps

The current priority is the clarity of the published library. The editorial pass considers motivation, the order of definitions, intermediate steps, examples, notation, illustrations, and each note's prerequisites. Changes are coordinated between Russian and English and checked for formulas, links, images, and rendering.

The [[en/Navigation/Thematic Index|Thematic Index]] gives the current contents of all series. Detailed editorial decisions and the history of reviews are recorded in the [[ru/Навигация/Карта библиотеки#Редакционный проход|Russian editorial register]]. Research directions and open questions retain their stated mathematical status throughout this work.

## Updating the map

Keep direction codes stable when rearranging tables or changing publication order. Add new directions explicitly, and retain a link to the result when a deferred question has been addressed. Review the continuation register before selecting new research work.

When either language version changes, synchronize the directions, accepted decisions, series counts, and open questions. Reading routes and detailed prerequisites are maintained in series navigators. Increment the revision and update the date when the research plan changes.

## Revision history

- 11 November 2026. Created the English map of current directions, published series, connections, and continuations alongside the Navigation section. The [[ru/Навигация/Карта библиотеки#История изменений|Russian revision history]] records the preceding editorial development.
