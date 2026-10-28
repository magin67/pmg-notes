# Checks for Matroid Parameters and Forest Characteristics

[Русская версия](README.md)

The scripts accompany the seven notes of the series in Russian and English. They use exact rational arithmetic with Python's fractions.Fraction; the Python 3.10 or newer standard library is sufficient. Run them from the repository root without the -O flag, which disables assert checks.

## Coverage

| Script | Coverage | Independent comparisons |
| --- | --- | --- |
| verify_cycle_matroid.py | 6 graphs, 84 forests | Independence axioms; forests and exterior coordinates through minors; the matrix Greenian and centered 2-forests; edge probabilities; rooted polynomials. |
| verify_forest_coefficients.py | 70 graphs, 215 edge recursions | Forest enumeration, products of cofactors of induced blocks, and deletion-contraction; grade and corank order; ordinary and rooted Greenian polynomials of $K_4$. |
| verify_forest_power_sums.py | 46 connected graphs, powers through 8 | Formal logarithm and Newton identities; inverse recovery; matrix traces; scaling and one-point gluing. |
| verify_forest_scales.py | 50 graphs, 146 corank levels | Ordinary and rooted forests, admissible extensions; principal minors; inequalities, scaling, and gluing. |
| verify_edge_resistances.py | 53 graphs, 200 edges, 84 ordered tree pairs and triples | Tree enumeration, spanning-tree polynomial derivatives, the Green matrix, and resistances; interpretation of $H_q$ through intersections. |
| verify_resistance_radius.py | 54 graphs, 215 reference-vertex choices | Independent geometric construction of the circumsphere, the forest formula, and the edge correction; scales and gluing. |
| verify_gluing_invariance.py | 49 one-point comparisons and 49 Whitney twists | Forests and boundary states; preservation and change of parameters under different gluings; shared-edge examples. |

The 70-graph set includes all 64 subgraphs of $K_4$ whose six edges have conductances $1,2,3,5,7,11$, including empty and disconnected subgraphs. The other six cases are unit-weight $K_4$ and $C_4$, a triangle with weights $1,2,3$, a path with weights $1,1/2,3$, a three-vertex graph with a parallel-edge pair, and a three-vertex path with a loop. Parallel-edge labels are kept separate, and isolated vertices are retained. Deleting a bridge checks the rank change in the reversed recurrence.

## Running the checks

~~~bash
python checks/matroid/verify_cycle_matroid.py
python checks/matroid/verify_forest_coefficients.py
python checks/matroid/verify_forest_power_sums.py
python checks/matroid/verify_forest_scales.py
python checks/matroid/verify_edge_resistances.py
python checks/matroid/verify_resistance_radius.py
python checks/matroid/verify_gluing_invariance.py
~~~

Keep all files together. Shared forest enumeration, polynomial, and matrix routines are in verify_forest_power_sums.py; the other checks import them directly or through neighboring scripts. The coefficient check also imports the component routine from verify_cycle_matroid.py. Imported files need not be run separately: each main scenario is protected by an if __name__ == "__main__" guard.

## Figures

draw_series_figures.py produces nine SVGs for notes 1-5, draw_radius_figures.py produces three for the radius note, and draw_gluing_figures.py produces three for the concluding note. The separate translate_figures_en.py script translates all 15 checked Russian SVGs, preserving graph geometry, colors, and numerical labels. It translates visible labels, titles, and accessible descriptions.

~~~bash
python checks/matroid/draw_series_figures.py
python checks/matroid/draw_radius_figures.py
python checks/matroid/draw_gluing_figures.py
python checks/matroid/translate_figures_en.py
~~~

Drawing programs are independent of the numerical checks. The finished SVGs are stored alongside the notes and need not be regenerated to read the library. To update only the English figures from the saved Russian originals, run just the final command.

Checks of finite sets of examples supplement the mathematical proofs in the notes; they are not proofs of general statements.
