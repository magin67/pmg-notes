# Checks for boundary forest passports and spectral boundary data

[Русская инструкция](README.md).

These programs accompany the six notes of *Boundary Polynomials and Graph Gluing* in both languages. They require only Python 3.10 or later and its standard library. Run them from the repository root without `-O`, which disables the assertions used by the checks.

## Exact checks

```bash
python checks/boundary/verify_forest_states.py
python checks/boundary/verify_contraction.py
python checks/boundary/verify_pairing.py
python checks/boundary/verify_spanning_geometry.py
python checks/boundary/verify_reduction.py
python checks/boundary/verify_spectral_boundary.py
```

| Program | Independent comparisons |
| --- | --- |
| `verify_forest_states.py` | Enumerates distinguishable edge subsets, detects cycles, and extracts boundary partitions, internal components, and groves. Checks all 16 forests of P5, the two marked-path gluings, weighted and disconnected examples, isolated vertices, and parallel edges. |
| `verify_contraction.py` | Compares the partition-rank criterion, cycle detection in quotient graphs, and incidence rank after adding auxiliary trees. Checks quotient polynomials, Kirchhoff determinants, resistance Gram determinants, basis changes, and redundant identifications. Includes 3,284 contraction configurations, with 1,956 resistance-formula cases. |
| `verify_pairing.py` | Compares the full pairing and every resulting state with direct enumeration. Checks responses, inverse matrices for two and three boundary vertices, boundary permutations, shared-edge conventions, and successive gluing. Includes 781 graph-pair configurations and 255 pairs of state representatives. |
| `verify_spanning_geometry.py` | Compares grove enumeration, reduced Laplacian determinants, Schur complements, boundary resistance Gram matrices, and both spanning-tree gluing laws. Checks the metric of the result, normalization changes, and the reconstruction counterexamples. |
| `verify_reduction.py` | Checks forest compatibility independently through incidence rank, the four-point radical, reduced matrix, spanning-tree blocks, and reduced-coordinate and response pairings. Computes ranks 2, 5, 14, 42 for boundary sizes 2–5 and checks graph examples by direct contraction and gluing. |
| `verify_spectral_boundary.py` | Uses rational polynomial arithmetic to compare determinants, cofactors, Jacobi's identity, and rooted-forest enumeration for 80 components. Checks all five coordinates for 528 gluings with disjoint edges and 48 with a shared weighted edge, as well as vertex orders, singular internal minors, loops, isolated vertices, associativity, and the zero projector in the resolvent. |

The programs share helper functions in this directory. Keep the six verification files together. The Russian review report, [REVIEW_RU.md](REVIEW_RU.md), records the joint mathematical and editorial review on which the English translations are based.

These finite computations check examples and implementations of the formulas. They do not replace the general proofs, including the Catalan rank theorem or its cited external foundations.

## Reproducing the figures

The six drawing programs generate the 21 Russian SVG source figures:

```bash
python checks/boundary/draw_forest_states.py
python checks/boundary/draw_contraction.py
python checks/boundary/draw_pairing.py
python checks/boundary/draw_spanning_geometry.py
python checks/boundary/draw_reduction.py
python checks/boundary/draw_spectral_boundary.py
```

Then generate all 21 English figures:

```bash
python checks/boundary/draw_english.py
```

The English generator uses `figure_translations_en.json` to translate titles, accessible descriptions, visible labels, and text following subscript spans. It preserves all geometry, edge weights, partition labels, and nontext attributes. Missing or unused dictionary entries fail explicitly. No image-generation service or additional Python package is needed.

By default, figures are read from `pmg-library/ru/Граничные полиномы и сочленение графов` and English files are written to `pmg-library/en/Boundary polynomials and graph gluing`. Optional `--source` and `--destination` arguments select alternative library roots, for example for a separate review build.

## Translation verification

The English edition retains all 180 displayed equations across the six notes and navigator; only explanatory words within formulas are translated. Inline mathematical expressions, equation numbering, proof structure, applicability assumptions, and source attribution are checked against the reviewed Russian text. State and response coordinates remain distinct from actual partition forms and resistance Gram matrices; ordinary forest data remain distinct from spectral data.

All 21 English SVGs are rendered and visually checked. Reciprocal language links, translated section links, figure paths, navigator tables, and the complete website build are checked before publication.
