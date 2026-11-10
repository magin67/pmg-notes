# PythonExamples checks

Install polyform_algebra using the shared setup note. For the fragment checker, use the exact revision pinned in the Combinatorial Potentials notebook. Each notebook sets up its own package revision. Run from the repository root:

```bash
python checks/pythonexamples/verify_examples.py
python checks/pythonexamples/generate_figures.py
python checks/pythonexamples/build_notebooks.py
python checks/pythonexamples/build_symbolic_notebooks.py
python checks/pythonexamples/execute_notebooks.py
```

Figure generation requires matplotlib. Notebook generation and execution require nbformat, nbclient, nbconvert, ipykernel, and a Python 3 Jupyter kernel using the selected environment. Install these development tools with pip if necessary.

The notebook generator reads the weighted-chain, Spaces, Metric Parameters, Structural Identities, Symmetric Polyforms, and Combinatorial Potentials example notes. The explanations and computation cells come from those notes. The generator adds package setup to the notebooks and an editable graph drawing to the weighted-chain notebook. The executor starts a fresh kernel for each language, checks for error outputs, saves computed results, and exports HTML previews under this directory. Inspect those previews after regeneration. A local execution is not a hosted Colab test.

The fragment checker executes each note in a separate namespace and checks key results. Package-level introductory tests independently check conductance matrices, currents, spanning-tree weights, areas, variations, and deletion. They complement the notes' own assertions.

The symbolic notebook creates letter-named elements before constructing forms. It demonstrates merging, disjoint components, vanishing cycle products, grade-grouped exponentials, and exact rational weights. Its display adapter formats computed forms without performing algebra. Numeric vertex identifiers are not used in public examples.

The Spaces examples check exact potentials, nonorthogonal coordinates, the midpoint form, and the boundary operator. They also check Dirichlet extension, deletion, contraction, one-vertex gluing, and Kron reduction for a path, a star, and both parts of a bipartite graph.

The Metric Parameters notebooks pin an exact package commit. Their installer checks the distribution's recorded source URL, since the v0.9.0 tag and the development revision report the same version. The calculations check both sphere centers, degree potential, subset volume, centralities, compactness, vertex removal, and norms in the original graph metric.

The Structural Identities notebooks check both sides of each identity, report a nonzero coefficient after a deliberate perturbation, and check exact rank, supports, and the spanning coefficient after rewriting a grove polyform.

The Symmetric Polyforms notebooks compare both sides coefficient by coefficient, beginning with the five-vertex identity. They check type counts, principal-form coefficients, products, the complete-graph and cycle exponentials, and the falling-factorial expansion of Abel polynomials.

The Combinatorial Potentials notebooks compare exact counts with enumeration, partition-form equality, contraction, r-Stirling numbers, and finite differences.
