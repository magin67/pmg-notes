# Editorial revision: Metric Parameters of Graphs

Scope: all eight notes and the navigation page, in Russian and English. The note names, addresses, series order, mathematical results, and open research questions are retained.

- Small examples now accompany the definitions. Added complete calculations for the center of a three-vertex path, a compactness reference with fixed total conductance, the triangle's spanning-tree polynomial, and degree potential.
- The three centralities are introduced and compared before the polyform and spanning-2-forest derivations. The proof of the radius change under metric-preserving removal is located in the vertex-removal note, with a link from the centrality note.
- The sphere-center note begins with its geometric picture, followed by the electrical and diffusion interpretations. Duality and bordering are collected afterward. The subgraph note separates its main route from applications and the infinite-network continuation.
- Bi-coordinate indices, upper/lower contractions, and use of the distinguished null-vector symbol are consistent with the coordinate series. The triangle-with-tail example states explicitly that vertex c supplies current and the triangle edges carry none.
- Added 11 explanatory SVG figures per language; updated both ranking-disagreement figures and the Russian fan-graph label. Existing useful figures remain.

Prepublication verification:

- Checked YAML, translation revisions, all 18 series pages, 320 wiki links, and 34 image references. All original heading anchors are retained.
- Compared the Russian and English display formulas in order. Rendered all 4,626 math expressions with the site's Quartz LaTeX plugin: no errors.
- Inspected all new Russian and English figures, including arrows, labels, units, and correspondence to the text.
- Exact example checks pass. Existing degree-potential, sphere-center, and subgraph-norm checks pass; the latter checks 208 nonempty subsets and Kron identities.

From the repository root:

```sh
python checks/metric-parameters/verify_editorial_examples.py
python checks/metric-parameters/verify_degree_potential.py
python checks/metric-parameters/verify_sphere_centres.py
python checks/metric-parameters/verify_subgraph_norms.py
python checks/metric-parameters/draw_editorial_figures.py --root . --preview work/metric-figures
```

The figure generator requires Matplotlib and NumPy; the exact checks require SymPy. The new generator writes 24 SVGs: 22 new illustrations and the two updated ranking plots. Publication and live-page checks follow the atomic commit; this report records the checks performed before publication.
