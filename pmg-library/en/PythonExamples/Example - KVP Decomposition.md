---
title: "Example: KVP Decomposition"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-kvp-decomposition
lang: en
description: "Nine exact calculations for KVP and KVPOU, from pair tables to forest toponomes."
order: 15
---

Nine calculations check pair-table decompositions, the distance transformation, metric parameters, and signed forest toponomes.

[[ru/PythonExamples/Пример - KVP-разложение|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra efb5bdb](https://github.com/magin67/polyform_algebra/commit/efb5bdb8bb68b7fe975141ef21b1a9cbcdfec5f2).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/kvp-decomposition.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/kvp-decomposition.ipynb)

## Decomposing the path

Build K, V, and P for the four-vertex path. Check reconstruction, zero residual row sums, and coefficient orthogonality.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/KVP Decomposition of Pair Characteristics#A path on four vertices|Related section of the note]].

```python
from itertools import combinations

from sympy import Matrix, Rational, expand, eye, ones, symbols, zeros

from polyform_algebra.core import (
    circumsphere, form_exp, green, laplacian_form, network,
    partition_form, potential, resistance, spanning_tree_weight,
)
from polyform_algebra.kvp import decompose, distance_table, pair_laplacian, signed_forest_toponome
from polyform_algebra.toponomes import vertex_toponome

labels = tuple("abcd")
pairs = tuple(combinations(range(4), 2))


def pair_values(table):
    return tuple(table[i, j] for i, j in pairs)


def graph(edges):
    return network(labels, tuple((a, b, weight) for (a, b), weight in edges))


def couplings(net):
    table = zeros(len(net.context.labels))
    for a, b, weight in net.edges:
        i, j = map(net.context.labels.index, (a, b))
        table[i, j] = table[j, i] = weight
    return table


path = graph((("ab", 1), ("bc", 1), ("cd", 1)))
C = couplings(path)
parts = decompose(C)
assert parts.K + parts.V + parts.P == C
assert parts.P * ones(4, 1) == zeros(4, 1)
assert pair_values(parts.P) == tuple(Rational(x, 2) for x in (1, -1, 0, 0, -1, 1))
assert all(sum(a.multiply_elementwise(b)) == 0 for a, b in combinations((parts.K, parts.V, parts.P), 2))
print("P₄ pair residual:", pair_values(parts.P))
```

## A star, a cycle, and a weighted graph

Check that P vanishes for the star and V vanishes for the cycle. For the weighted example, verify P on every pair and cancellation on the absent edge.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/KVP on Simple and Weighted Graphs#A graph with unequal weights|Related section of the note]].

```python
star = graph((("ab", 1), ("ac", 1), ("ad", 1)))
cycle = graph((("ab", 1), ("bc", 1), ("cd", 1), ("ad", 1)))
weighted = graph((("ab", 4), ("ac", 2), ("bc", 1), ("bd", 3), ("cd", 2)))
assert decompose(couplings(star)).P == zeros(4)
assert decompose(couplings(cycle)).V == zeros(4)
weighted_parts = decompose(couplings(weighted))
assert pair_values(weighted_parts.P) == tuple(Rational(x, 2) for x in (2, 1, -3, -3, 1, 2))
assert weighted_parts.K[0, 3] + weighted_parts.V[0, 3] + weighted_parts.P[0, 3] == 0
print("Weighted P component:", pair_values(weighted_parts.P))
```

## One arc and five components

Check all five components for a single arc and an isolated vertex. The O residual forms a triangular circulation in the pair table.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/Oriented Extensions of KVP - Circulation and Imbalance#Directed graph examples|Related section of the note]].

```python
arc = Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
oriented = decompose(arc)
assert oriented.K + oriented.V + oriented.P + oriented.O + oriented.U == arc
assert oriented.P == zeros(3)
assert oriented.O == Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]]) / 6
assert oriented.U[0, 1] == Rational(1, 3)
assert oriented.O * ones(3, 1) == zeros(3, 1)
print("One arc: O_ab =", oriented.O[0, 1], "| U_ab =", oriented.U[0, 1])
```

## The distance operator

Apply the distance operator to Laplacians of a path, directed cycle, and single arc. Check the balanced multipliers and the contribution of U to V without balance.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/The Distance Operator and KVP Decomposition#Example: a path on four vertices|Related section of the note]].

```python
Q = distance_table(pair_laplacian(C))
assert Q == 8 * parts.K + 4 * parts.V + 2 * parts.P
assert pair_values(Q) == (5, 3, 2, 6, 3, 5)
cycle_arcs = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
cycle_parts = decompose(cycle_arcs)
assert cycle_parts.U == zeros(3)
assert distance_table(pair_laplacian(cycle_arcs)) == 6 * cycle_parts.K + 2 * cycle_parts.O
one_arc_image = decompose(distance_table(pair_laplacian(arc)))
assert one_arc_image.V == 3 * oriented.V + Matrix([[0, 0, 1], [0, 0, -1], [1, -1, 0]]) / 2
print("Distance image of P₄:", pair_values(Q))
```

## From the Green matrix to resistances

Build the pair table from off-diagonal Green matrix entries. Compare its components with the resistance decomposition and check the Kirchhoff index.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/KVP Decomposition of the Green Matrix and Resistances#Symmetric resistances: mean, vertex contribution, and residual|Related section of the note]].

```python
Gr = Matrix(green(path).value.values)
gamma = Matrix(4, 4, lambda i, j: -Gr[i, j] if i != j else 0)
R = Matrix(resistance(path).value.values)
g_parts, r_parts = decompose(gamma), decompose(R)
assert pair_laplacian(gamma) == Gr and distance_table(Gr) == R
assert (r_parts.K, r_parts.V, r_parts.P) == (8 * g_parts.K, 4 * g_parts.V, 2 * g_parts.P)
assert sum(pair_values(R)) == 4 * Gr.trace() == 10
print("Green table to resistance: multipliers 8, 4, 2; Kf = 10")
```

## Contacts and a conductance change

Add four contact resistances to the cycle and calculate resistances between external terminals. Then change an internal conductance separately and check the change in P.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/Applications of KVP Decomposition - Electrometry and Pair Data Analysis#A computed example: contacts and a conductance change|Related section of the note]].

```python
base = Matrix(resistance(cycle).value.values)
terminals = tuple("xyzw")
contacts = tuple(Rational(i, 4) for i in range(1, 5))
extended = network(labels + terminals, cycle.edges + tuple(
    (a, terminal, 1 / contact) for a, terminal, contact in zip(labels, terminals, contacts)
))
terminal_pairs = tuple((terminals[i], terminals[j]) for i, j in pairs)
values = resistance(extended, pairs=terminal_pairs).value.values
terminal_table = zeros(4)
for (i, j), value in zip(pairs, values):
    terminal_table[i, j] = terminal_table[j, i] = value
assert all(terminal_table[i, j] == base[i, j] + contacts[i] + contacts[j] for i, j in pairs)
assert decompose(terminal_table).P == decompose(base).P
changed = graph((("ab", 2), ("bc", 1), ("cd", 1), ("ad", 1)))
delta_P = decompose(Matrix(resistance(changed).value.values) - base).P
assert pair_values(delta_P) == tuple(Rational(x, 84) for x in (-5, -2, 7, 7, -2, -5))
print("Contacts preserve P. Internal change:", pair_values(delta_P))
```

## Equal K and V with different radii

Compare K, V, and P of the resistance tables of the two graphs. Compute their radii and spanning-tree coefficients.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/KVP Components and Metric Graph Parameters#Example: identical resistance K and V, different radii|Related section of the note]].

```python
weights = (
    (Rational(1, 4), Rational(1, 4), Rational(3, 20), Rational(5, 12), Rational(1, 4), Rational(1, 4)),
    tuple(Rational(x, 51) for x in (26, 8, 4, 16, 8, 26)),
)
graphs = [graph((labels[i] + labels[j], w) for (i, j), w in zip(pairs, row)) for row in weights]
first, second = [decompose(Matrix(resistance(net).value.values)) for net in graphs]
assert first.K == second.K and first.V == second.V and first.P != second.P
spheres = [circumsphere(net).value for net in graphs]
radii = tuple(sphere.resistance_radius for sphere in spheres)
assert radii == (Rational(49, 64), Rational(37, 48))
assert tuple(spanning_tree_weight(net).value for net in graphs) == (Rational(4, 15), Rational(16, 51))
print("Same resistance K and V, radii:", ", ".join(map(str, radii)))
```

## The second-order symmetric potential

Compute the potentials of all four triples on the path with conductances 1, 2, and 3. Compare their normalized sum with the quadratic formula in K, V, and P.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/The Second-Order Symmetric Potential and KVP Decomposition#Examples on four vertices|Related section of the note]].

```python
weighted_path = graph((("ab", 1), ("bc", 2), ("cd", 3)))
metric = form_exp(laplacian_form(weighted_path).value).value
triples = combinations(labels, 3)
raw_potentials = [
    potential(metric, partition_form(weighted_path.context, (triple,)).value).value
    for triple in triples
]
tau = spanning_tree_weight(weighted_path).value
assert tau == 6
assert tuple(value / tau for value in raw_potentials) == tuple(
    Rational(x, 6) for x in (3, 5, 3, 1)
)
resistance_parts = decompose(Matrix(resistance(weighted_path).value.values))
norms = [sum(component[i, j] ** 2 for i, j in pairs)
         for component in (resistance_parts.K, resistance_parts.V, resistance_parts.P)]
assert norms[0] / 2 - norms[1] / 2 - norms[2] == sum(raw_potentials) / tau == 2
assert sum(raw_potentials) == 12
print("Weighted path: nu₂ = 2, U₂ = 12")
```

## The forest toponome of the P component

Enumerate forests with signed weights for the P component of the five-vertex path. Check cancellation of type (2,1), root weighting, and agreement with the determinant.

[[en/Invariants, Decompositions, and Spectra/KVP decomposition/Forest Toponomes of KVP Components#Example: the P-component of a five-vertex path|Related section of the note]].

```python
C5 = zeros(5)
for i in range(4):
    C5[i, i + 1] = C5[i + 1, i] = 1
components = decompose(C5)
forest_types = signed_forest_toponome(components.P)
assert forest_types == {
    (): 1, (2,): -2, (1, 1): 1, (3,): Rational(-2, 27), (4,): Rational(1, 9),
}
t = symbols("t")
rooted = sum(value * t ** sum(kind) for kind, value in vertex_toponome(forest_types).items())
assert rooted == 1 - 2 * t**2 - Rational(8, 27) * t**3 + Rational(5, 9) * t**4
assert rooted == expand((eye(5) + t * pair_laplacian(components.P)).det())
full_types = signed_forest_toponome(C5)
for kind in ((2,), (1, 1)):
    assert sum(signed_forest_toponome(part).get(kind, 0)
               for part in (components.K, components.V, components.P)) == full_types[kind] == 3
print("Signed P₅ forest type (2,1) cancels; rooted polynomial agrees with determinant")
```
