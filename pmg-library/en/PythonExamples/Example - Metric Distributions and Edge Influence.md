---
title: "Example: Metric Distributions and Edge Influence"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-metric-distributions
lang: en
description: "Four exact calculations. Check the effect of a new coupling, path overlap in a weighted tree, a signed field on a cycle, and the distinction between edge marginals and pair coefficients in grade two."
order: 22
---

Four exact calculations. Check the effect of a new coupling, path overlap in a weighted tree, a signed field on a cycle, and the distinction between edge marginals and pair coefficients in grade two.

[[ru/PythonExamples/Пример - Метрические распределения и влияние связей|Русский]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra ebd699c](https://github.com/magin67/polyform_algebra/commit/ebd699c4d68d711f8adda77494d272789dafb306).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/metric-distributions.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/metric-distributions.ipynb)

## Adding a coupling to a path

Add $ac$ to the path $a-b-c$ and verify the change in effective resistance. Compare the contribution of the coupling before and after adding it.

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Edge Influence and Metric Distribution#Adding a coupling to a path|Related section of the note]].

```python
from fractions import Fraction as Q

from sympy import zeros

from polyform_algebra.core import (
    Boundary, form_exp, laplacian_form, network, potential, resistance,
    spanning_tree_weight, square,
)
from polyform_algebra.metric_distributions import metric_distribution, pair_blade
from polyform_algebra.variations import vary_conductances


def unit_graph(labels, pairs):
    return network(tuple(labels), [(a, b, 1) for a, b in pairs])


def vector(graph, pair):
    return pair_blade(graph, (pair,))


def edge_coefficients(distribution, left, right=None):
    return {subset[0]: value for subset, value in distribution.coefficients(left, right).items()}


path = unit_graph("abc", (("a", "b"), ("b", "c")))
ac = ("a", "c")
direction = vector(path, ac)
before = metric_distribution(path)
assert before.evaluate(direction) == 2
assert edge_coefficients(before, direction) == {("a", "b"): 1, ("b", "c"): 1}
assert ac not in edge_coefficients(before, direction)

triangle = vary_conductances(path, {ac: 1})
after = metric_distribution(triangle)
assert after.evaluate(direction) == resistance(triangle, pairs=(ac,)).value.values[0] == Q(2, 3)
assert after.evaluate(direction) - before.evaluate(direction) == -Q(4, 3)
assert edge_coefficients(after, direction) == {("a", "b"): Q(1, 9), ac: Q(4, 9), ("b", "c"): Q(1, 9)}
assert sum(edge_coefficients(after, direction).values()) == after.evaluate(direction)
print("Added ac: resistance 2 to 2/3; triangle coefficients 1/9, 4/9, 1/9")
```

## Path overlap in a weighted tree

Check the support and sign of the mixed distribution for paths $ad$ and $be$ in a weighted chain. Double each conductance separately and verify the finite changes.

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Path Intersection as an Influence Field on a Tree#Unequal conductances|Related section of the note]].

```python
weighted_path = network(tuple("abcde"), [
    ("a", "b", 3), ("b", "c", 2), ("c", "d", Q(1, 2)), ("d", "e", 4),
])
first, second = (vector(weighted_path, pair) for pair in (("a", "d"), ("b", "e")))
distribution = metric_distribution(weighted_path)
coefficients = edge_coefficients(distribution, first, second)
assert tuple(coefficients.values()) == (0, Q(1, 2), 2, 0)
initial = distribution.evaluate(first, second)
assert initial == sum(coefficients.values()) == Q(5, 2)
assert edge_coefficients(distribution, -first, second) == {pair: -value for pair, value in coefficients.items()}
changes = []
for a, b, conductance in weighted_path.edges:
    updated = vary_conductances(weighted_path, {(a, b): conductance})
    changes.append(metric_distribution(updated).evaluate(first, second) - initial)
assert changes == [0, -Q(1, 4), -1, 0]
print("Weighted path overlap: bc and cd; value =", initial)
print("Separate doubling effects:", tuple(map(str, changes)))
```

## A signed field and a balanced cross-edge

The mixed form for the diagonals of a square evaluates to zero and has four nonzero edge contributions. Check them with finite probes. Adding the cross-edge $bd$ leaves $R_{ac}$ unchanged.

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/The Influence Field on Graphs with Cycles#Square with a zero inner product and a nonzero field|Related section of the note]].

```python
cycle = unit_graph("abcd", (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")))
left, right = (vector(cycle, pair) for pair in (("a", "c"), ("b", "d")))
distribution = metric_distribution(cycle)
mixed = edge_coefficients(distribution, left, right)
assert mixed == {("a", "b"): -Q(1, 4), ("a", "d"): Q(1, 4),
                 ("b", "c"): Q(1, 4), ("c", "d"): -Q(1, 4)}
assert sum(mixed.values()) == distribution.evaluate(left, right) == 0
for pair, coefficient in mixed.items():
    altered = vary_conductances(cycle, {pair: 1})
    pair_resistance = distribution.evaluate(vector(cycle, pair))
    assert metric_distribution(altered).evaluate(left, right) == -coefficient/(1+pair_resistance)

for conductance in (Q(1, 3), Q(1), Q(7)):
    bridge = vary_conductances(cycle, {("b", "d"): conductance})
    bridge_data = metric_distribution(bridge)
    assert bridge_data.evaluate(left) == 1
    assert edge_coefficients(bridge_data, left)[("b", "d")] == 0
print("Square mixed field: two +1/4 and two -1/4; balanced cross-edge contributes zero")
```

## Pair contributions in grade two

Compare two forms on a square with equal edge marginals and different pair coefficients and output forms. Check all single-edge probes, including deletion. On a path, compare doubling two conductances together with the separate changes. Check the evaluations against the normalized spanning-tree potential.

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distribution in Higher Grades#Computation and checks|Related section of the note]].

```python
def triangle_blade(graph, labels):
    a, b, c = labels
    return pair_blade(graph, ((a, b), (a, c)))


def quadratic_sum(data, blades):
    return sum(data.evaluate(blade) for blade in blades)


def pair_field(data, blades):
    terms = [data.coefficients(blade) for blade in blades]
    return {subset: sum(term[subset] for term in terms) for subset in data.functionals}


def edge_marginals(field):
    result = {}
    for subset, value in field.items():
        for pair in subset:
            result[pair] = result.get(pair, 0) + value
    return result


def output_tensor(data, field):
    return sum((value * data.blades[subset] * data.blades[subset].T
                for subset, value in field.items()), zeros(data.metric.rows))


def forest_value(graph, triangles):
    indices = {label: i for i, label in enumerate(graph.context.labels)}
    forms = [square(Boundary(graph.context, tuple(indices[label] for label in triangle))).value
             for triangle in triangles]
    form = sum(forms[1:], forms[0])
    exponential = form_exp(laplacian_form(graph).value).value
    return potential(exponential, form).value / spanning_tree_weight(graph).value


data = metric_distribution(cycle, grade=2)
triangle_groups = (("abc", "acd"), ("abd", "bcd"))
forms = [tuple(triangle_blade(cycle, labels) for labels in group) for group in triangle_groups]
fields = [pair_field(data, blades) for blades in forms]
assert sum(data.functionals.values(), zeros(3)) == data.metric
for field, blades, triangles in zip(fields, forms, triangle_groups, strict=True):
    assert sum(field.values()) == quadratic_sum(data, blades) == forest_value(cycle, triangles) == 1
    assert edge_marginals(field) == {(a, b): Q(1, 2) for a, b, _ in cycle.edges}
edge_pair = (("a", "b"), ("b", "c"))
assert [field[edge_pair] for field in fields] == [Q(1, 4), Q(1, 8)]
assert output_tensor(data, fields[0]) != output_tensor(data, fields[1])

for a, b, _ in cycle.edges:
    for increment in (Q(1), Q(-1, 2), Q(1, 3), Q(-1)):
        updated = vary_conductances(cycle, {(a, b): increment})
        updated_data = metric_distribution(updated, grade=2)
        expected = 1 - increment*Q(1, 2)/(1+increment*Q(3, 4))
        for blades, triangles in zip(forms, triangle_groups, strict=True):
            assert quadratic_sum(updated_data, blades) == forest_value(updated, triangles) == expected

changes = ({}, {("a", "b"): 1}, {("b", "c"): 1}, {("a", "b"): 1, ("b", "c"): 1})
values = []
for change in changes:
    updated = vary_conductances(path, change)
    blade = triangle_blade(updated, "abc")
    value = metric_distribution(updated, grade=2).evaluate(blade)
    assert value == forest_value(updated, ("abc",))
    values.append(value)
assert values == [1, Q(1, 2), Q(1, 2), Q(1, 4)]
assert values[1] + values[2] - values[0] == 0
print("Grade two: same edge marginals; pair coefficients 1/4 and 1/8")
print("Joint doubling on a path: 1/4; adding the separate increments would give 0")
```
