# Exact checks for Greenian and Polyform Duality

[Русская версия](README.md)

Python 3.10 or later is required; no external packages are needed. All calculations use `fractions.Fraction`. The checks print JSON to standard output, do not modify notes, and do not save results to files.

From the repository root:

    python checks/dual/verify_vector.py
    python checks/dual/verify_exponential.py
    python checks/dual/verify_variations.py
    python checks/dual/verify_typical.py
    python checks/dual/verify_potentials.py
    python checks/dual/verify_symmetry.py
    python checks/dual/verify_toponomes.py

Each script may also be run by its absolute path from another working directory. Keep the neighboring files in this folder: the additional checks use operations from `verify_vector.py` and `exterior_checks.py`. Do not use Python's `-O` option: the checks rely on `assert`.

| Script | Independent comparisons | Scope |
| --- | --- | --- |
| [verify_vector.py](verify_vector.py) | Vector factors, signed forests, minors of the inverse reduced Laplacian, original forest sums, and both directions of dual deletion | 9 graphs on 2–6 vertices |
| [verify_exponential.py](verify_exponential.py) | Exterior powers and all minors, factorization, complementary grades, centered image | 29 matrices of orders 1–5; 15 nonsingular symmetric duality cases; 3 graph examples |
| [verify_variations.py](verify_variations.py) | Polar form, original forests, vertex deletion, vertex attachment, determinant, and direct enumeration of new trees | 6 graphs; 64 deleted sets; 27 attachments |
| [verify_typical.py](verify_typical.py) | All exterior grades, minors, block cofactors, partition sums, and rooted sums | 9 graphs on 4–10 vertices, including Petersen; also complete graphs and stars on 2–8 vertices |
| [verify_potentials.py](verify_potentials.py) | Potentials from form multiplication, Laplacian determinants, Cauchy–Binet, and the minimum with free interior vertices | 9 graphs; also complete graphs |
| [verify_symmetry.py](verify_symmetry.py) | Identities for subset sums of squared elements and tetrahedron identities in the zero-sum space | 154 tensor equalities on 2–8 elements |
| [verify_toponomes.py](verify_toponomes.py) | Full toponomes from forest enumeration, two specializations, independent principal minors, spectral reversal, and complementary original forests | Unit and weighted P4 paths, K4, C5, a star, and a nonuniformly weighted graph on five vertices |

Exterior products are calculated from permutation signs of basis indices, minors by Gaussian elimination in rational arithmetic, and forest sums by separate enumeration or cofactors on specified blocks. The shared helper `exterior_checks.py` contains coordinate deletion and independent checks of forest minors.

The graph suites partly overlap. Exit code zero means that all checks in the script passed. The standard-graph suite, particularly Petersen, takes substantially longer than the others. These calculations verify finite collections of examples; general proofs are provided in the notes.
