# English translation review: the graph-weaving supplements

Date: 2026-11-02. Russian source baseline: `de095da6c5d85b69fda32820df1355c7d26cbd66` on `v5`.

## Scope and navigation

**Weaving Graphs: Plug, Socket, and Recurrence** and **The Laplacian Exponential in Graph Weaving** are translated in full into `pmg-library/en/Graph Transformations and Gluing/Chains of cores`, with eight translated SVG figures. The source pages receive reciprocal language links; their mathematical text is unchanged. Translation keys match, and `translated_revision` records Russian revisions 4 and 3, including the new links.

The complete series now has seven substantive notes, one navigator, and 23 distinct figures per language. The weaving notes occupy its first two reading positions. The original five English notes retain their text; their display order is aligned with the Russian route. Both navigators and English references from **Spectra of Isomers** are updated. The Russian navigator's obsolete description of spectral transfer and decoding as future work is reconciled with the completed companion series.

The indexes and map now record 17 bilingual series and 123 substantive notes in each language. Mathematical definitions in the core specification and terminology are unchanged.

## Mathematical parity

`verify_weaving_translation.py` checks all 55 display formulas in order, all 362 inline formulas, every numerical datum in the body and tables, and the sequence of 30 callouts including 12 collapsed proofs. It checks 46 internal links, seven explicit heading references, both language pairs, eight image paths, Markdown table structure, and the unique order 0 through 7 of the English series.

The only TeX substitutions translate words: graph label `Б` to `B`, `квадраты` to `squares`, `- лес` to `is a forest`, and `закрыта` to `closed`. No coefficient, exponent, matrix entry, equation number, sign, or normalization changes.

Preserved restrictions include the fixed correspondence of ordered contacts, separate runner edges, six vertices and five edges in a hexagonal path runner, and the factors involving the runner's spanning-tree coefficient. Two spanning coordinates, two ordinary-forest coordinates, five rooted coordinates, and the full component-size state retain their different meanings.

A repeated embedded factor and a power of a growth operator remain distinct from a power on a fixed vertex set and from a matrix exponential. The full size state has unbounded indices; the limitation on scalar recurrences retains its stated polynomial-coefficient scope. Closure requires retaining the initial boundary. Sufficiency of five rooted coordinates relies on the separate boundary-change theorem and implies neither minimality nor completeness of the scalar spectrum. The grade-three toponome difference remains a finite computation for the specified pair. No planarity or scientific priority is asserted.

## Exact checks repeated

Both existing mathematical programs were run again without modification. Their saved exact-result JSON files remain unchanged.

- `verify_weaving.py`: 42 pairs of direct Laplacian minors; independent enumeration of 5254 edge subsets on 21 graphs; all 2736 attachments from 38 connected labeled four-vertex runners, 36 input/output pair choices, and two correspondences. Variable and periodic path checks also passed.
- `verify_weaving_exponential.py`: 12 direct graph comparisons; 136470 edge subsets; 22110 second-grade coefficients; 54 general-path column checks; 216 three-step hexagonal choices; the explicit square rule and five shift-factor steps; all 131072 edge subsets of the original labeled isomer pair. Rooted coordinates were checked by four polynomial determinants, Jacobi's identity, and a signed off-diagonal cofactor at `t=1` for each of the twelve graphs.

These computations test implementations and finite examples; neither they nor translation parity replace the general proofs.

## Figures and rendered pages

The eight SVGs have English visible labels, titles, descriptions, and Markdown captions: 85 translated strings in the shared dictionary. Graph geometry, contact markings, mathematical labels, and numerical values are preserved. Longer labels may use a smaller font to remain within the original width. All eight figures were rendered and inspected visually; no clipped or overlapping labels were found.

The Quartz output was inspected for all 21 affected mathematical or navigation pages. Checks passed for 2670 rendered math expressions, 1045 local article links, 284 anchor references, 40 image placements, and 57 tables. No KaTeX errors or raw wiki-link markers remain. Table widths are consistent, and both new language pairs link in both directions.

No Quartz configuration, theme, dependency, or deployment setting changes are included. The existing optional Excalidraw-plugin warning does not prevent the build.

## Reproduction

```text
python checks/core-chains/verify_weaving.py
python checks/core-chains/verify_weaving_exponential.py
python checks/core-chains/translate_figures.py
python checks/core-chains/verify_weaving_translation.py
python checks/isomer-spectra/verify_translation.py
```

The exponential check requires SymPy. The translation checker uses only the standard library. Fitting the eight new SVG translations uses Pillow and Matplotlib; the earlier fifteen translations retain their behavior. See the [verification guide](README.md) and [figure dictionary](figure-translations-en.json).
