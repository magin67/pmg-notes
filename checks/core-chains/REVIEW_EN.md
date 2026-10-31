# English translation review: Chains of Cores

Date: 2026-10-31. Russian source baseline: `1972b217b2b79a38b5013eeb42f039bd1c1c7b4a` on `v5`, following the [general mathematical review](REVIEW_RU.md).

## Scope and synchronization

The five notes and their navigator have been translated in full into `pmg-library/en/Chains of cores`. Each English page shares its Russian counterpart's `translation_key` and records the corresponding Russian revision in `translated_revision`. Both versions link directly to one another. The two library indexes expose the complete route and the navigator in the other language.

Terminology follows the current English core specification (revision 15), PMG terminology (revision 16), and the published boundary, matroid, and spectral notes. The distinctions between cores and their auxiliary scheme, seam vertices and shared edges, ordinary and rooted forests, and full and reduced electrical data are retained. Statements, proofs, computational examples, and limitations have the same scope as in Russian. Internal series codes are absent from the public texts.

## Mathematical and editorial checks

| Page | Display-math blocks | Collapsible proofs | Figure placements |
| --- | ---: | ---: | ---: |
| Cores, Seams, and Admissible Chains | 11 | 4 | 3 |
| Why Chain Configuration Preserves Matroid Parameters | 17 | 6 | 2 |
| Spanning-Tree Polynomials of Chains: Determinant and Recurrence | 25 | 8 | 3 |
| Limits of Invariance: Branching, Disconnected Seams, and Other Cores | 16 | 6 | 4 |
| Closing a Chain: Rings and the Möbius Effect | 23 | 6 | 4 |
| Chains of Cores navigator | 0 | 0 | 0 |
| Total | 92 | 30 | 16 |

All 92 display-math blocks were compared with the Russian source. Only explanatory text and the labels A/B, c/m, and “last” were translated; expressions and equation numbers were retained. Inline formulas and numerical tables were compared as well. The two harmless differences in formula occurrence counts are an additional math-formatted degree 3 and replacement of a repeated S by “it” in a proof.

The graph definitions, numerical examples, verification programs, and exact result files retain the mathematical content checked in the Russian review. This translation does not introduce new numerical experiments or strengthen conclusions inferred from finite checks.

Source checks covered YAML, paired translation keys and revisions, heading and callout counts, proof markers, math delimiters, internal links and section anchors, and image paths. External references to Chen–Mohar, Richman–Shokrieh–Wu, Mannens–Nederlof, DLMF, Azimi–Farrokhi, and Erickson were checked at their cited addresses.

## Figures and rendered pages

The 15 distinct SVGs retain the original graph geometry, vertex labels, seam correspondences, and numerical values. Visible labels, panel names, titles, and accessibility descriptions are translated. Configuration letters agree with the English formulas. One dual figure is used in two notes, giving 16 placements.

Run `python checks/core-chains/translate_figures.py` to reproduce the English SVGs after generating the Russian originals. The explicit dictionary is [figure-translations-en.json](figure-translations-en.json). The program rejects missing or unused translations and any remaining Cyrillic text.

The unchanged Quartz build processed 262 Markdown files and emitted 902 files successfully. Browser checks covered all six English pages, all 30 proof toggles, all 16 image placements, all 15 SVG text bounds, table structure, and rendered internal links including section anchors. No KaTeX errors, overflowing display formulas at the checked desktop width, nested callouts, or broken content links were found. All SVGs and representative proof and navigator views were inspected visually.

The local preview intentionally blocked unrelated external browser resources; its graph-view network message is not a content-rendering failure. The existing optional Excalidraw-plugin warning and the archive's lack of Git metadata did not prevent the build. No Quartz configuration, theme, dependency, or deployment setting was changed.
