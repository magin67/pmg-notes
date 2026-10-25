---
title: KVP Decomposition and Oriented Extensions
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: kvp-decomposition-series-navigation
order: 0
description: "Nine notes on KVP, KVPO, and KVPOU: definitions, examples, the distance transformation, Green and resistance components, applications, metric parameters, the second-order potential, and forest toponomes."
---

This series explains the canonical decomposition of pair characteristics and its use in PMG. Linear subspaces and projectors are defined first, followed by graph, metric, and applied consequences. The decomposition always concerns a chosen table: couplings C, pair coefficients of the Green matrix, or resistances R and r.

The nine reviewed Russian notes form the current series; their English translations are collected here. KVP is the PMG name for a decomposition with known counterparts in Hoeffding-ANOVA theory, representations of the symmetric group, and the Johnson scheme. The established decomposition itself should be distinguished from the study of particular consequences for PMG.

## Components and classes of tables

For a symmetric table with $A_{ii}=0$ on $n\ge3$ elements, define

$$
\mu=\frac{\sum_{i<j}A_{ij}}{\binom n2},
\qquad
v_i=\sum_jA_{ij}-(n-1)\mu
$$

For $i\ne j$,

$$
A_{ij}=\mu+\frac{v_i+v_j}{n-2}+p_{ij},
\qquad
\sum_i v_i=0,
\qquad
\sum_jp_{ij}=0
$$

This is KVP decomposition: K specifies the overall level, V the vertex heterogeneity of row sums, and P the symmetric residual with zero row sums. For an oriented table, the skew-symmetric part is further split into O with zero row sums and U of the form $(u_i-u_j)/n$, where $u=(d^{out}-d^{in})/2$.

| Table being decomposed | Decomposition | Components necessarily absent |
| --- | --- | --- |
| Symmetric | KVP | O and U |
| Balanced oriented | KVPO | U |
| Arbitrary oriented | KVPOU | No restriction on which components may be nonzero |

Balance compares incoming and outgoing sums at each vertex. It does not imply regularity and does not eliminate V. Every pair of the specified set participates in the decomposition; a zero coupling and an unknown observation have different meanings.

## Contents and reading order

| Order | Note | Main contents |
| ---: | --- | --- |
| 1 | [[KVP Decomposition of Pair Characteristics]] | Definition, origins of the normalizations, projectors, uniqueness, dimensions, coefficient orthogonality, and known counterparts |
| 2 | [[KVP on Simple and Weighted Graphs]] | Complete graphs, stars, cycles, paths, disconnected and weighted examples; what components do and do not imply |
| 3 | [[Oriented Extensions of KVP - Circulation and Imbalance]] | O and U, KVPOU projectors, a triangular circulation basis, balance without regularity, and oriented examples |
| 4 | [[The Distance Operator and KVP Decomposition]] | Centered matrices and pair tables, inverse transformation, action on sectors, and U-V mixing without balance |
| 5 | [[KVP Decomposition of the Green Matrix and Resistances]] | Distinctions between components of C, the Green matrix, R, and r; recovery, circulation, and five examples of different component behavior |
| 6 | [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]] | Observability of P, series contacts, an electrical network, interactions, monitoring, and limitations of real measurements |
| 7 | [[KVP Components and Metric Graph Parameters]] | The Kirchhoff index, centralities, radius, mixed metric contributions, spanning-tree sensitivities, and Foster contractions |
| 8 | [[The Second-Order Symmetric Potential and KVP Decomposition]] | The potential's quadratic form, the SPF tetrahedron identity, bounds, examples, and the balanced-graph circulation correction |
| 9 | [[Forest Toponomes of KVP Components]] | Polyform factorization, pure and mixed forest coefficients, balance identities for P, ranks, and open questions |

## Main results

The linear and forest statements admit signed tables and do not require connectedness. The metric statements below assume a connected graph with nonnegative weights; in the oriented case, balance is also required. These metric formulas are not asserted for arbitrary unbalanced digraphs.

**A unique linear decomposition.** The KVP and KVPOU projectors are explicit. Their orthogonality concerns the coefficient inner product of tables. Individual components have signed coefficients; a nonzero P-component cannot be a table of nonnegative couplings.

**Exact transformations between representations.** The composition of the distance operator with Laplacian construction acts on the balanced pair sectors K, V, P, O with multipliers $2n,n,2,2$. The distance operator itself differs from this composition. Without balance, U also produces a V-contribution.

**Different components of couplings and resistances.** Laplacian inversion is nonlinear. [[KVP Decomposition of the Green Matrix and Resistances]] gives examples with $C_P=0$, $R_P\ne0$ and with $C_V=0$, $R_V\ne0$. One-way resistances r of a balanced graph may have all five components even though the original couplings have no U. Symmetric R loses circulation data.

**The measurement meaning of P.** The complete collection of four-point combinations determines P and cannot distinguish additions from $K\oplus V$. In the resistor model, these combinations are transfer resistances. Invariance under series contacts is proved for a leaf-electrode model; effectiveness on real electrometric data has not yet been established.

**Metric and quadratic consequences.** The Kirchhoff index uses only $R_K$; centroid centralities use $R_K$ and $R_V$. Radii can differ even when these components coincide. For the second-order potential,

$$
H_n(R)=\frac{n-2}{4}\|R_K\|_0^2
-\frac12\|R_V\|_0^2-\frac n4\|R_P\|_0^2
$$

Here $\|A\|_0^2=\sum_{i<j}A_{ij}^2$ is the coefficient sum of squares. For a symmetric graph, the normalized potential is $\nu_2=H_n(R)$; a balanced graph adds $n\|r_O\|_0^2$. The relation to the tetrahedron identity and the applicability conditions are proved in [[The Second-Order Symmetric Potential and KVP Decomposition]].

**Constraints and interactions of forest coefficients.** At grade two, scalar mixed KVP-coefficients vanish. For pure P, $A_{2,1^{k-2}}=-kA_{1^k}$ is proved. Higher grades contain mixed terms; three pure toponomes do not determine the full toponome or spanning-tree coefficient. Two positively weighted graphs with spanning-tree coefficients 398 and 394 demonstrate this.

## Reading routes and prerequisites

- **First introduction:** [[KVP Decomposition of Pair Characteristics]], then [[KVP on Simple and Weighted Graphs]]. Linear algebra and the notion of a coupling table suffice; the decomposition itself needs no metric.
- **Oriented data:** after the KVP definition, read [[Oriented Extensions of KVP - Circulation and Imbalance]]. Moving to directional geometry requires [[Balanced Graphs]] and [[KVP Decomposition of the Green Matrix and Resistances]].
- **Metric and potentials:** [[The Distance Operator and KVP Decomposition]], [[KVP Decomposition of the Green Matrix and Resistances]], then [[KVP Components and Metric Graph Parameters]] and [[The Second-Order Symmetric Potential and KVP Decomposition]]. Useful background includes [[Laplacian, Green Matrix, and Effective Resistance Matrix]], [[Metric Parameters of Graphs]], and [[Partition Forms and the Tetrahedron Identity]].
- **Applications:** the KVP definitions, then [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]]. The electrical part requires [[KVP Decomposition of the Green Matrix and Resistances]] first; the interaction example uses a pair table directly.
- **Forests and toponomes:** [[Forest Toponomes of KVP Components]] after the KVP definition and the basic constructions of [[Partition Toponomes]] and [[Polynomial Toponomes]]. The metric notes are not prerequisites for defining pure toponomes.

## Checks, boundaries, and further work

The [common verification script and running instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) are available in the public repository. They use exact rational arithmetic. Checks compare projectors on coordinate bases, grounded-system solutions, determinants, and forest enumeration; generators for additional graphs are fixed. The published P-toponome rank data are reproduced as well. Computations complement the general proofs.

Coefficient orthogonality must not be transferred to the PMG metric inner product. Linear decomposition does not automatically make inversion, radius, the spanning-tree coefficient, or the exponential additive. The polyform and matrix exponentials use different products; the forest toponome refers to a fixed representation.

The general conjecture on P-toponome ranks remains open; exact witnesses establish equality with the proved upper bound for grades 2-4. Further work on directed toponomes concerns types and interactions of O and U: the balanced-graph exponential has already been constructed. General invariant operators, centroid factorizations, coupling concentration, resistance sensitivities, higher potentials, and experimental electrometry are recorded in the [[Карта библиотеки PMG#Отложенные вопросы и продолжения|map of further topics (in Russian)]].

The main notation is recorded in [[Core specification]] and [[PMG terminology]]. The series and its navigator are available in Russian and English; corresponding notes share a translation key.
