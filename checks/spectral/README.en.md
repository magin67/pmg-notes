# Spectral series checks

[Русский](README.md)

These programs reproduce the mathematical checks and all 18 figures in the six-note series **Spectra and Diagonalization in Polyform Algebra**.

Python 3.10 or later is required. Run commands from the repository root. Do not use -O: verification relies on assert. Verification scripts print JSON and do not write files.

All seven draw_*.py programs accept --lang en for English figures and --lang ru for Russian figures (the default). Mathematical data and checks are shared; figure_labels_en.json supplies English labels, titles, and descriptions. Translation is applied before rendering, so mathematical labels are laid out normally rather than edited in the resulting SVG.

SVGs are saved beside the notes in the selected language. The optional --preview-dir PATH saves PNGs for visual inspection. Figure generation requires Matplotlib and runs the corresponding mathematical checks first. Approximate coordinates are used for curves and layout; mathematical parameters and labels are checked as described below.

## Diagonal representation and duality on P3

    python checks/spectral/verify_diagonal.py
    python checks/spectral/draw_diagonal.py --lang en --preview-dir previews

Verification needs no external packages. It uses shared operations from checks/dual/verify_vector.py and checks/dual/exterior_checks.py.

Unnormalized integer eigenvectors allow normalized tensors to be checked exactly: their quadratic forms are divided by coordinate squared lengths 2 and 6. Independent comparisons cover:

- the edge-built Laplacian, spectral decomposition, and pseudoinverse;
- all grades of the edge and spectral exterior exponentials;
- both directions of exterior contraction in consistent direct and dual bases;
- centered transfer of the dual exponential and the normalizations of T3 and the top grades;
- coordinate, resistance, and energy evaluations;
- principal minors and direct enumeration of ordinary and rooted forests;
- pairwise resistances and the Kirchhoff index.

This is an exact check of a particular example, not a computational proof of the general statements. The drawing program produces three figures.

## Eigenspaces and projectors on C4

    python checks/spectral/verify_projectors.py
    python checks/spectral/draw_projectors.py --lang en

Verification uses only the standard library and shared operations from verify_diagonal.py and checks/dual. The drawing program produces three figures.

Exact comparisons cover two orthonormal bases of the eigenvalue-2 eigenspace, polynomial formulas for projectors, all six forms selecting directions, and the corresponding operators on exterior powers. Exponential grades are compared with an independent expansion over cycle edges. Further checks cover dual contractions for every grade and every set of direction counts, the centered identification, T4 normalizations, rooted and ordinary forest coefficients, both metric evaluations, resistances, and changes in individual modal contributions under basis rotation.

## A cospectral weighted pair on four vertices

    python checks/spectral/verify_cospectral.py
    python checks/spectral/draw_cospectral.py --lang en

Verification uses only the standard library and shared operations from neighboring checks. The drawing program produces two figures.

Laplacians are constructed from edges independently of the projectors and common eigenbasis. Checks cover the spectrum 0,4,4,8, the difference between projectors, Green matrices, all grades of the direct and transferred dual exponentials, characteristic polynomials, top-grade normalizations, and every pairwise resistance with its eigenspace contributions. Ordinary and rooted coefficients are independently obtained by forest enumeration.

For both graphs, both dual contractions are checked in every grade at conductance scale factors 1/2, 1, 2, and 3. The dual first grade is compared with an independently inverted reduced matrix. A separate check confirms that scaling direct and dual coefficients by the same factor breaks reciprocity.

## Path and cycle modes: P6, C6, and C5

    python checks/spectral/verify_path_cycle.py
    python checks/spectral/draw_path_cycle.py --lang en

Verification requires SymPy and NumPy. The drawing program produces four figures.

For the three main examples, projectors are computed exactly by polynomial interpolation in the edge-built Laplacian. Checks cover orthogonality, ranks, completeness, and spectral reconstruction of the Laplacian and Greenian. Trigonometric components are evaluated numerically and compared with exact projectors to an error below 10⁻¹².

Rooted polynomials are independently obtained from the determinant, the spectral product, and direct forest enumeration. Further checks cover ordinary forest coefficients, reversal of coefficients for the Greenian, spanning-tree counts, and top-grade normalizations. For C6, the second-grade formula is checked as an equality of polyforms, including nilpotence of the forms of paired eigenspaces. All pairwise resistances and the eigenspace contributions stated in the note are compared exactly; Kirchhoff indices are checked by summation and through the Greenian trace.

Additional numerical checks cover 45 graphs: paths P2–P24 and cycles C3–C24. They compare orthonormality, eigenvector equations, the spectral Greenian formula with independent matrix inversion, and electrical resistance formulas. The absolute error tolerance is 10⁻¹¹. This is a finite set of examples; the general statements are proved in the note.

## Chebyshev transformations of a path

    python checks/spectral/verify_chebyshev.py
    python checks/spectral/draw_chebyshev.py --lang en

Verification requires SymPy. The drawing program produces two figures.

For P2–P18, 374 matrices are compared: steps from 0 to 2n+1 are computed by polynomial recurrence and independently by folding the step graph on 2n vertices. Checks cover signs, conductances, components, classification by the greatest common divisor, zero modes, reflection, and periodicity. An additional 49 pairs of composed transformations are checked on P6.

For the transition from P6 to C6, exact checks cover relabeling, merging of the original path projectors, the Greenian, and each mode's contribution to R16. The exterior exponential is compared in three representations: by edges, through the first grade, and by eigenspace forms. Checks cover every grade of M and N, reversal of scalar coefficients, both dual contractions, and top-grade normalizations 6T6 and T6/216. For the disconnected step m=3, the spectrum, rank 4, and vanishing fifth grade are checked.

## The spectral cone of the fixed P3 basis

    python checks/spectral/verify_cone.py
    python checks/spectral/draw_cone.py --lang en

Verification uses the standard library and shared operations from earlier checks. The drawing program produces two figures.

Equality of spectral and edge matrices is checked through the two coefficient matrices; sign conditions are tested at 697 rational points. Checks cover 432 cases of inversion of positive coordinates and 83 nonnegative matrices in the fixed basis for the reverse passage from the Perron spectracone. Enumeration of all eight simple labeled graphs on three vertices identifies exactly four diagonal in the chosen basis.

At eight cone points, including the zero and disconnected cases, exterior exponentials from modes and edges, ordinary and rooted forest coefficients, and top grades are compared exactly. Six connected examples additionally check matrix inversion, direct and dual contractions, the centered identification, both metric evaluations, resistances, and the Kirchhoff index. Separate checks cover the Green matrix at (4,1), a commutation example with a repeated eigenvalue, and six steps of the P3 Chebyshev orbit. Finite checks verify examples and figures; the general statements are proved in the note.

## Projection onto a fixed basis and loss of information

    python checks/spectral/verify_projection.py
    python checks/spectral/draw_projection.py --lang en

Verification uses the standard library and existing polyform-algebra operations. The drawing program produces two figures.

For the C4 basis with rotated modes, exact checks cover spectral and edge expressions, diagonal and block projections, negative edge coefficients in the unconstrained projection, coordinates of the nearest graph in the cone, and decomposition of the squared error. Optimality of the nearest point is confirmed by its equality to the projection onto the violated half-space and satisfaction of the remaining constraints.

The checks include 21 rational points of the family with common diagonal (10,4,4). For five admissible graphs and the unconstrained projection, all grades are compared through exterior powers, matrix minors, and independent edge expansions. Checks cover ordinary and rooted forest coefficients, both dual contractions, the centered identification, top-grade normalizations, metric evaluations, the Greenian, resistances, and the Kirchhoff index. Projection of each already formed grade is compared with the corresponding grade of the exponential of the projection.

Enumeration of all 64 simple labeled graphs on four vertices checks trace preservation, idempotence, orthogonal error decomposition, inequalities for rooted coefficients, and the exact error expression through the second coefficient. For the 38 connected graphs, additional checks cover positivity of the diagonal evaluations and the inequality for the diagonal of the inverse matrix. The single-edge example on three vertices checks the possible rank increase after projection. These finite checks verify examples; the general statements are justified in the note.
