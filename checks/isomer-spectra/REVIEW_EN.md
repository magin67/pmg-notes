# English edition review: Spectra of Isomers

Date: 2026-11-02. Russian source baseline: `099c4ffdd85948a4f2263308afb2d17fd6872898`.

The English collection contains nine substantive notes, the concluding navigator, and 35 SVG figures in `pmg-library/en/Graph Transformations and Gluing/Spectra of Isomers`. It follows the [reviewed Russian series](REVIEW_RU.md), including the corrections to reflection/reversal conventions, the sign of the resolvent, and the limits of the reconstruction claims.

## Translation scope

1. Two Isomers of Three Hexagons.
2. Spectral Transfer to a New Boundary.
3. SLR Codes of Hexagonal Chains.
4. Spectral Differences of SLR Chains.
5. Rooted Forests and Decoding the Boundary State.
6. Reconstructing a Chain from Its Boundary Response.
7. Weaving SLR Chains and Constant Turns.
8. Spectral Distinguishability of SLR Chains.
9. Periodic SLR Chains: Recurrences and Spectra.

The navigator, **Spectra of Isomers: Results and Open Questions**, preserves the connection diagram, summary of results, attribution table, reading routes, and open questions. Every page has a reciprocal Russian/English link and the same `translation_key` as its counterpart. `translated_revision` records the current Russian revision.

The two supporting notes on graph weaving and the Laplacian exponential belong to **Chains of Cores**. They are outside this translation request and remain explicitly labeled “in Russian” wherever linked. The adjacent navigator now distinguishes these supplements from its five bilingual introductory notes and links to the completed spectral continuation.

## Mathematical parity and result status

The automated comparison passes for:

- 288 display formulas, in their original order;
- 1,789 inline formulas, allowing grammatical reordering within prose;
- all numerical table entries;
- the sequence and folding state of 127 result, proof, and explanatory callouts;
- all ten language pairs, 234 English-page wiki links, 16 explicit section links, and 35 image references.

The permitted TeX changes are purely linguistic: the Russian graph label `Б` becomes `B`, equation tags `12а` and `12б` become `12a` and `12b`, and words inside `\text{...}` are translated. No polynomial coefficient, matrix entry, rational value, inequality, exponent, or sign is changed.

The English text retains the distinctions between:

- the number of cores and the number of vertices;
- ordinary and rooted forest polynomials and the characteristic polynomial;
- the Laplacian form, its matrix, and its operator;
- a fixed-boundary passport and transfer to a new boundary;
- graph isomorphism, matroid equivalence, and cospectrality;
- injectivity of the full marked state, of a characteristic polynomial, and of a single numerical value.

In particular, decoding from the full state and reconstruction from three exact rational response entries remain proved for the stated class. No minimality of those three entries is asserted. Scalar distinguishability at arbitrary length remains conjectural. The catalog of 16,150,725 unmarked classes up to 18 cores remains a finite computational result. No planarity requirement is introduced. Period-phase similarity is distinguished from equality of finite spectra. Exact reconstruction is distinguished from stability under measurement errors and from practical identification outside the specified graph class.

The dynamic interpretation uses the original graph. The network with one unit resistor from each vertex to a common ground is explicitly auxiliary. Two experiments yield four records or readings, with the cross-responses equal by reciprocity; geometric symmetry and three neighbors per vertex are not required.

## Figures and shared exact checks

All 35 figures have English captions, visible labels, titles, and accessible descriptions. The 327 translated source strings are stored in `figure-labels-en.json`. `draw_english.py` preserves all graph and diagram geometry in 34 SVGs, adjusting text sizes where necessary. The remaining periodic-growth plot is redrawn from the same result file, including its English plot labels and decimal formatting. Every figure was rendered and visually inspected for clipping and overlap.

The existing mathematical verification programs and twelve exact-result files used by the series and its weaving foundations are unchanged. The first-pair calculation was run again:

```text
PASS: both determinants, 131072 edge subsets, radii, forest types, traces, and symbolic Schur proof.
```

This independently checks both characteristic polynomials and rooted forest enumerations. The broader mathematical audit, including the large catalog, is recorded in `REVIEW_RU.md`; the translation task did not rerun that entire catalog or claim a new proof from translation parity.

Reproduce the translation checks with:

```text
python checks/isomer-spectra/verify_translation.py
python checks/isomer-spectra/draw_english.py
python checks/isomer-spectra/verify_three_hexagons.py
```

See [README.md](README.md) for all mathematical verification commands and dependencies.

## Navigation and rendered-site checks

Both home pages, both thematic indexes, the primary **Graph Transformations and Gluing** section, the secondary **Invariants, Decompositions, and Spectra** entry, and the neighboring series navigator are updated. English foundational links now lead to the English proofs. The library map is revision 69; its remaining outdated placement row is corrected. The synchronized core specification and terminology revisions are 18 and 19 respectively; their mathematical definitions are unchanged.

The current totals are **17 bilingual series, 123 substantive Russian notes, and 121 substantive English notes**. The difference consists of the two untranslated weaving supplements, not missing pages of this series.

The local Quartz build passes. Inspection of all 20 Russian and English pages confirms:

- 2,077 English math expressions rendered without KaTeX errors;
- 688 local article links and 260 section-anchor references resolve;
- all 70 image occurrences resolve;
- all ten language pairs link in both directions;
- ten former Russian page addresses and the former folder address still redirect.

The English drawing filenames avoid punctuation that Quartz encodes inconsistently in image links. Existing Russian aliases and assets remain intact. No Quartz configuration, theme, or dependency changes are included.
