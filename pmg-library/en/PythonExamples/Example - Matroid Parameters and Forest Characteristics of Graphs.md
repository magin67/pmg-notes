---
title: "Example: Matroid Parameters and Forest Characteristics of Graphs"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-matroid-forest-characteristics
lang: en
description: "Seven exact calculations for cycle matroids, forest polynomials, and resistance."
order: 17
---

Seven calculations check edge independence, forest coefficients, the resistance radius, and the Whitney twist.

[[ru/PythonExamples/Пример - Матроидные параметры и лесные характеристики графов|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 1487709](https://github.com/magin67/polyform_algebra/commit/148770970a5d0005c8e16b8eb63969d2afe3ca22).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/matroid-forest-characteristics.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/matroid-forest-characteristics.ipynb)

## The cycle matroid of a triangle

Enumerate the edge subsets of a triangle and test independence by exterior product. All seven proper subsets are independent, and the product of the three cycle edges vanishes.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/The Cycle Matroid and Exterior Products of Edges#Independence, forests, and cycles|Related section of the note]].

```python
from fractions import Fraction as Q
from functools import reduce
from itertools import combinations
from math import prod

from polyform_algebra.core import Boundary, Unit, circumsphere, contract, network, resistance, wedge
from polyform_algebra.matroid import (
    edge_forest_probabilities, forest_coefficients, forest_power_sums,
    forest_resistance_radius, forest_resistance_scales, normalized_forest_coefficients,
)
from polyform_algebra.toponomes import forest_toponome, laplacian_polynomial


def unit_network(labels, pairs):
    return network(tuple(labels), [(a, b, 1) for a, b in pairs])


def edge_product(net, pairs):
    positions = {label: i for i, label in enumerate(net.context.labels)}
    blades = (Boundary(net.context, (positions[a], positions[b])) for a, b in pairs)
    return reduce(lambda left, right: wedge(left, right).value, blades, Unit(net.context).as_exterior())


def subsets(items):
    return (part for size in range(len(items) + 1) for part in combinations(items, size))


triangle_edges = (("a", "b"), ("a", "c"), ("b", "c"))
triangle = unit_network("abc", triangle_edges)
triangle_forests = [part for part in subsets(triangle_edges) if edge_product(triangle, part).coefficients]
assert not edge_product(triangle, triangle_edges).coefficients
assert tuple(sum(len(part) == k for part in triangle_forests) for k in range(3)) == (1, 3, 3)
print("Independent edge sets:", len(triangle_forests))
```

## Ordinary and rooted forests of K4

Compare ordinary coefficients with rooted coefficients from $\det(I+tL)$. At four values of $t$, compare the ordinary polynomial with $t^3T_{K_4}(1+1/t,1)$ evaluated from the independent subsets.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank#Full example: unit K4|Related section of the note]].

```python
k4_edges = tuple(combinations("abcd", 2))
k4 = unit_network("abcd", k4_edges)
ordinary = forest_coefficients(k4)
rooted = laplacian_polynomial(k4)
assert ordinary == (1, 6, 15, 16)
assert rooted == (1, 12, 48, 64)

# At y=1 only the independent subsets survive in the Tutte rank sum.
# A subset of size k then contributes (x - 1) ** (3 - k).
independent = [part for part in subsets(k4_edges) if edge_product(k4, part).coefficients]
for t in (Q(1), Q(2), Q(1, 2), Q(-1)):
    tutte_value = sum((1 / t) ** (3 - len(part)) for part in independent)
    assert sum(value * t**k for k, value in enumerate(ordinary)) == t**3 * tutte_value
print("Ordinary K4:", tuple(map(str, ordinary)))
print("Rooted K4:", tuple(map(str, rooted)))
```

## Normalized polynomial and Newton sums

For a path with conductances $1,2,3$, compare the Newton sums with power sums of the reciprocal conductances. For the unit triangle, compute the first four sums without factoring the polynomial.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/The Normalized Forest Polynomial and Power-Sum Parameters#Examples|Related section of the note]].

```python
weighted_path = network(tuple("abcd"), [("a", "b", 1), ("b", "c", 2), ("c", "d", 3)])
normalized = normalized_forest_coefficients(weighted_path)
assert normalized == (1, Q(11, 6), 1, Q(1, 6))
path_powers = forest_power_sums(normalized, 4)
assert path_powers == tuple(sum(Q(1, c)**k for c in (1, 2, 3)) for k in range(1, 5))
triangle_powers = forest_power_sums(normalized_forest_coefficients(triangle), 4)
assert triangle_powers == (1, Q(1, 3), 0, Q(-1, 9))
print("Triangle Newton sums:", tuple(map(str, triangle_powers)))
```

## Forest resistance scales

The four-vertex path and star have the same ordinary scales and different first rooted scales. Check exact ratios of adjacent coefficients for the cycle and complete graph as well.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Forest Resistance Scales#Trees, cycles, and the complete graph|Related section of the note]].

```python
path = unit_network("abcd", (("a", "b"), ("b", "c"), ("c", "d")))
star = unit_network("abcd", (("a", "b"), ("a", "c"), ("a", "d")))
cycle = unit_network("abcd", (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")))
assert forest_resistance_scales(forest_coefficients(path)) == (3, 1, Q(1, 3))
assert forest_resistance_scales(forest_coefficients(star)) == (3, 1, Q(1, 3))
assert forest_resistance_scales(forest_coefficients(cycle)) == (Q(3, 2), Q(2, 3), Q(1, 4))
assert forest_resistance_scales(laplacian_polynomial(path))[0] == Q(5, 2)
assert forest_resistance_scales(laplacian_polynomial(star))[0] == Q(9, 4)
assert forest_resistance_scales(ordinary) == (Q(15, 16), Q(2, 5), Q(1, 6))
assert forest_resistance_scales(rooted) == (Q(3, 4), Q(1, 4), Q(1, 12))
print("First rooted scales (path, star):", Q(5, 2), Q(9, 4))
```

## Edge probabilities in a weighted triangle

Compare $c_eR_e$ with the probabilities obtained by enumerating the three spanning trees. Check their sum and the ordinary forest polynomial identity for deleting and contracting edge $ab$.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Edge Resistances and Random Spanning Trees#Examples|Related section of the note]].

```python
weighted_triangle = network(tuple("abc"), [("a", "b", 1), ("a", "c", 2), ("b", "c", 3)])
trees = tuple(combinations(weighted_triangle.edges, 2))
tree_weights = {tree: prod(edge[2] for edge in tree) for tree in trees}
total = sum(tree_weights.values())
by_enumeration = {
    edge[:2]: sum(weight for tree, weight in tree_weights.items() if edge in tree) / total
    for edge in weighted_triangle.edges
}
probabilities = edge_forest_probabilities(weighted_triangle)
assert probabilities == by_enumeration
assert tuple(probabilities.values()) == (Q(5, 11), Q(8, 11), Q(9, 11))
assert sum(probabilities.values()) == 2

without_ab = network(tuple("abc"), weighted_triangle.edges[1:])
contracted_ab = contract(weighted_triangle, {"ab": ("a", "b"), "c": ("c",)}).value.network
f_delete = forest_coefficients(without_ab)
f_contract = forest_coefficients(contracted_ab)
# The conductance of ab is 1, and including ab raises the grade by one.
assert forest_coefficients(weighted_triangle) == tuple(
    a + b for a, b in zip(f_delete, (0, *f_contract), strict=True)
)
print("Weighted triangle probabilities:", tuple(map(str, probabilities.values())))
```

## Radius of the resistance sphere

For six graphs, compare the exact values of $\rho=\xi/3-h_2/12$ with the squared circumradius computed from the resistance metric.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance#Examples and independent computation|Related section of the note]].

```python
examples = {
    "P4": (path, Q(3, 4)),
    "star": (star, Q(3, 4)),
    "weighted P4": (weighted_path, Q(11, 24)),
    "C4": (cycle, Q(5, 16)),
    "K4": (k4, Q(3, 16)),
    "weighted triangle": (weighted_triangle, Q(15, 121)),
}
for name, (graph, expected) in examples.items():
    forest_radius = forest_resistance_radius(graph)
    geometric_radius = circumsphere(graph).value.resistance_radius
    assert forest_radius == geometric_radius == expected
    print(name, "radius:", forest_radius)
```

## The Whitney twist

Compare independence for all 64 subsets of edge labels before and after twisting. The ordinary forest coefficients and radius are preserved. The coefficient of forests with block sizes $5$ and $1$ changes from $11$ to $10$, and $R(p,q)$ changes from $2$ to $3$.

[[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#Two-point gluing and the Whitney twist|Related section of the note]].

```python
straight_edges = (("a", "x"), ("x", "b"), ("a", "p"), ("a", "y"), ("y", "b"), ("a", "q"))
twisted_edges = (("a", "x"), ("x", "b"), ("a", "p"), ("b", "y"), ("y", "a"), ("b", "q"))
straight = unit_network("abxypq", straight_edges)
twisted = unit_network("abxypq", twisted_edges)
by_edge_label = tuple(subsets(tuple("ABCDEF")))
for chosen in by_edge_label:
    indices = tuple("ABCDEF".index(label) for label in chosen)
    first = edge_product(straight, (straight_edges[i] for i in indices))
    second = edge_product(twisted, (twisted_edges[i] for i in indices))
    assert bool(first.coefficients) == bool(second.coefficients)
assert forest_coefficients(straight) == forest_coefficients(twisted) == (1, 6, 15, 20, 14, 4)
assert forest_resistance_radius(straight) == forest_resistance_radius(twisted) == Q(13, 16)
assert forest_toponome(straight)[(4,)] == 11
assert forest_toponome(twisted)[(4,)] == 10
pair_values = tuple(resistance(graph, pairs=(("p", "q"),)).value.values[0]
                    for graph in (straight, twisted))
assert pair_values == (2, 3)
print("Whitney twist:", len(by_edge_label), "edge subsets checked; R(p,q) =", *pair_values)
```
