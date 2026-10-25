# Checks for “KVP Decomposition and Oriented Extensions”

[Русский](README.md) · English

This directory contains one reproducible script, [verify.py](verify.py), for the [nine notes in the series](../../pmg-library/en/KVP%20decomposition/KVP%20Decomposition%20and%20Oriented%20Extensions.md).

Python 3.9 or later is required; no third-party packages are needed. All numerical comparisons are exact, using fractions.Fraction. The script neither accesses the network nor modifies files.

## Running the checks

Download the whole repository, for example the v5 branch archive, or use an existing local copy. From the repository root, run:

    python checks/kvp/verify.py

On Windows, use py -3 instead of python if needed; on Linux or macOS, use python3. Data paths are resolved relative to the script, so running it by absolute path works from any directory.

Expected output:

    PASS symmetric
    PASS oriented
    PASS distance
    PASS green
    PASS applications
    PASS metrics
    PASS potential
    PASS forests
    All 8 check groups passed.

To display intermediate exact results:

    python checks/kvp/verify.py --verbose

To run one group:

    python checks/kvp/verify.py --only green --verbose

A mismatch prints FAIL and the error location, and returns a nonzero exit code. The checks use assert, so -O and PYTHONOPTIMIZE are not allowed: the script detects disabled assertions and refuses to run.

## What is checked

| Group | Notes | Checks and independent calculations |
| --- | --- | --- |
| symmetric | KVP definition and simple graphs | Nine unit-weight and weighted examples, sums of squares, and orthogonality; complete graphs, stars, and cycles for n from 3 to 12 |
| oriented | Oriented extensions | Five examples, numeric tables read directly from Markdown; projectors, orthogonality, and a triangular basis on all coordinate tables for n from 3 to 6; the sign of the circulation form |
| distance | The distance operator | All coordinate matrices for n from 3 to 6: double centering, sector action, U-V mixing, and both inverse rules |
| green | The Green matrix and resistances | Five examples and 40 additional symmetric and balanced graphs for n from 3 to 7; components and Green-matrix recovery; independent grounded-system solutions for columns of r. In the new regular example, R is additionally checked using ordinary unit currents between every pair |
| applications | Applications | Four electrical networks, including eight-node networks with contacts; responses from Kirchhoff-system solutions; the interaction table; ranks of four-point measurements for n from 4 to 8 |
| metrics | Metric parameters | Four unit-weight and two weighted examples; radius and center from a system using R; direct tree enumeration; derivatives from interpolation of the spanning-tree polynomial, independently of the trace formula. Additionally, 15 symmetric graphs for n from 3 to 7 and 12 balanced graphs for n from 3 to 6 |
| potential | The second-order potential | Every quadratic-form coefficient for n from 3 to 7, the tetrahedron identity, and the sum of four-point responses; examples, 15 additional symmetric graphs and 15 balanced graphs; Gram determinants and independent principal minors |
| forests | Forest toponomes | Forest enumeration and sums of principal minors, pure and mixed coefficients, graphs with spanning-tree coefficients 398 and 394, eight signed tables for n from 3 to 6; reproduction of the published rank witnesses in grades 2-4 |

Additional graphs are specified in the code with fixed random seeds: 25102026, 251020262 for potential checks, and 251020269 for forest checks. Symmetric graphs have positive connected support; balanced graphs are built by adding directed cycles. The signed forest examples require neither positivity nor connectedness.

## Data and limits of verification

The common script reads two parts of the original Russian public series:

- numeric tables of the [oriented examples](../../pmg-library/ru/KVP-разложение/Ориентированные%20расширения%20KVP%20-%20циркуляция%20и%20дисбаланс.md);
- [integer P-toponome rank witnesses](../../pmg-library/ru/KVP-разложение/Проверка%20рангов%20P-топономов.json).

The English notes retain the same numeric tables. An [English-labeled copy of the rank data](../../pmg-library/en/KVP%20decomposition/P%20toponome%20rank%20verification.json) contains identical matrices, type orders, coefficient vectors, and ranks.

All other input graphs and expected values are specified directly in the script. For the published witnesses, forests are enumerated anew, every coefficient vector is compared, and ranks are recomputed. The balance identity is not used to obtain these vectors.

A successful run confirms the described finite computations. General statements are justified in the notes; the script does not prove the rank conjecture at arbitrary grade. It also does not test electrometry on experimental data or implement incomplete-data or weighted statistical estimation.
