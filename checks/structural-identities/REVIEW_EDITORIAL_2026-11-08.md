# Structural identities: bilingual editorial pass

Updated the five notes and both series navigators, preserving the reading order, existing heading anchors, mathematical scope, source attribution, and proof callouts.

- Partition forms: diagram of all seven partitions; numerical evaluation before the parallelepiped construction; replacement of the small raster illustration with a labeled vector diagram.
- Constructing identities: operations before type notation; diagrams for joining blocks and expanding four vertices to four blocks; explicit coefficient counts 2 and 6.
- Basis and dimension: early seven-to-six example; crossing and pairing diagrams; comparison of dimensions 3, 3, 9, and 6; general proofs and generating-series derivations after the main explanation.
- Graph gluing: early cycle and grove examples, including the excluded empty forest; highlighted eliminated and negative coordinates in the K4 table; updated links to the published full forest-pairing construction.
- Supports: early comparison of singleton transfer with multiplication; support diagrams; a sum of two four-vertex relations with five-vertex support; examples before the general decomposition theorem.
- Navigators: prerequisites and reading routes before compact result summaries. Descriptive links replace positional references. English revisions track the updated Russian revisions.

Added 11 vector illustrations in each language. The existing K4 illustration is retained, as are the old raster assets for link compatibility. `draw_editorial_figures.py` reproduces the SVGs using Matplotlib; use `--root <repository-root>` and optionally `--preview <directory>`.

Validation before publication:

- YAML, revision correspondence, order, UTF-8/LF, unique headings, existing heading anchors, all 161 internal links, and all 24 image references checked.
- All 38 proof callouts retained. Display formulas in the five note pairs agree in order after normalization of translated text. Original display formulas are retained, apart from moving the redundant rank equality to the section defining its map; the navigator no longer duplicates general formulas.
- All inline and display mathematics checked with the repository's Quartz KaTeX plugin; no rendering errors.
- Both language sets of figures inspected visually; labels, supports, edge colors, and the parallelepiped projection checked.
- `verify_editorial_examples.py` passes exact SymPy and combinatorial checks: tetrahedron identity, rank 6 and rank 3 of the pair-form subfamily, pairing determinant 8, five-vertex support of a sum, six support-count table rows, transfer rank 30, full kernel dimension 40, product extension rank 31, weighted cycle, K4 count 16, and its signed coordinate transformation. These finite checks do not replace the stated general proofs.

No changes to the mathematical foundations, site configuration, unrelated notes, or local Obsidian repository.
