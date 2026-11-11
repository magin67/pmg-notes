---
title: "Example: Laplacian, Greenian and Resistance Variations"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-network-variations
lang: en
description: "Eight exact calculations. Check direct conductance changes, network recovery from Greenian and resistance variations, and the feasibility of prescribed resistances with fixed conductances in a prism."
order: 20
---

Eight exact calculations. Check direct conductance changes, network recovery from Greenian and resistance variations, and the feasibility of prescribed resistances with fixed conductances in a prism.

[[ru/PythonExamples/Пример - Вариации лапласиана, гриниана и резистенсов|Русский]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 63d3424](https://github.com/magin67/polyform_algebra/commit/63d342437b0d5973f38befc5183d7f4ea9ecf6f0).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/network-variations.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/network-variations.ipynb)

## Strengthening one edge

Strengthen edge $ab$ of the unit triangle. Check the spanning-tree weight and resistance against direct calculations. Separately remove a bridge of a path.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/One Changing Edge#Example - strengthening one edge of a triangle|Related section of the note]].

```python
from fractions import Fraction as Q
from itertools import combinations

from sympy import Matrix, diag, eye

from polyform_algebra.core import (
    DomainError, InvalidInput, green, kron_reduce, laplacian, network,
    network_from_resistance, resistance, spanning_tree_weight,
)
from polyform_algebra.variations import (
    conductance_greenian_update, resistance_constraint_polynomials,
    vary_conductances, vary_greenian_coefficients, vary_resistances,
)


def unit_graph(labels, pairs):
    return network(tuple(labels), [(a, b, 1) for a, b in pairs])


def edge_weights(graph):
    return {(a, b): c for a, b, c in graph.edges}


def tree_weight(graph):
    return spanning_tree_weight(graph).value


def green_matrix(graph):
    return Matrix(green(graph).value.values)


def resistance_matrix(graph):
    return Matrix(resistance(graph).value.values)


triangle = unit_graph("abc", combinations("abc", 2))
edge = ("a", "b")
change = Q(1)
updated_triangle = vary_conductances(triangle, {edge: change})
green_updated, ratio = conductance_greenian_update(triangle, {edge: change})
old_r = resistance_matrix(triangle)
new_r = resistance_matrix(updated_triangle)
assert ratio == 1 + change * old_r[0, 1] == Q(5, 3)
assert green_updated == green_matrix(updated_triangle)
assert new_r[0, 1] == old_r[0, 1] / ratio == Q(2, 5)
assert tree_weight(updated_triangle) == ratio * tree_weight(triangle) == 5

path3 = unit_graph("abc", (("a", "b"), ("b", "c")))
assert len(vary_conductances(path3, {edge: -1}).components) == 2
try:
    conductance_greenian_update(path3, {edge: -1})
except DomainError:
    print("Single edge: R(a,b) =", new_r[0, 1], "; removing a bridge disconnects the path")
else:
    raise AssertionError("a disconnected output has no connected update")
```

## Changing two conductances together

Strengthen two triangle edges and check the mixed term in the spanning-tree normalization. On a path, check a joint change with a disconnected intermediate graph.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Two Edges and Joint Variation#Example - strengthening two edges of a triangle|Related section of the note]].

```python
# The final graph is connected even though deleting ab first breaks the path.
changes = {("a", "b"): 1, ("a", "c"): 1}
directions = Matrix([[1, 1], [-1, 0], [0, -1]])
combined = vary_conductances(triangle, changes)
updated_green, ratio = conductance_greenian_update(triangle, changes)
gram = directions.T * green_matrix(triangle) * directions
assert updated_green == green_matrix(combined)
assert ratio == 1 + gram.trace() + gram.det() == Q(8, 3)
assert tree_weight(combined) == 8 and resistance_matrix(combined)[0, 1] == Q(3, 8)

changes = {("a", "b"): -1, ("a", "c"): 2}
joint_graph = vary_conductances(path3, changes)
joint_green, factor = conductance_greenian_update(path3, changes)
gram = directions.T * green_matrix(path3) * directions
first, second = changes.values()
expected = 1 + first*gram[0, 0] + second*gram[1, 1] + first*second*gram.det()
assert joint_green == green_matrix(joint_graph)
assert factor == expected == tree_weight(joint_graph) / tree_weight(path3) == 2
print("Joint edge variation: triangle tree weight =", tree_weight(combined), "; path ratio =", factor)
```

## One Greenian coefficient

Change $\gamma_{ab}$ on a four-vertex path. Compare the recovered conductances and spanning-tree weight with the exact values in the note.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/One Greenian Coefficient#Example - one Greenian coefficient of a path|Related section of the note]].

```python
path4 = unit_graph("abcd", (("a", "b"), ("b", "c"), ("c", "d")))
delta = Q(1, 5)
result = vary_greenian_coefficients(path4, {edge: delta})
direction = Matrix([1, -1, 0, 0])
original_green = green_matrix(path4)
factor = 1 + delta * (direction.T * Matrix(laplacian(path4).value.values) * direction)[0]
assert -original_green[0, 1] == -Q(1, 8)
assert -green_matrix(result)[0, 1] == Q(3, 40)
assert edge_weights(result) == {("a", "b"): Q(2, 5), ("a", "c"): Q(1, 5),
                                ("b", "c"): Q(7, 10), ("c", "d"): 1}
assert factor == 2 and tree_weight(result) == Q(1, 2)
print("One Greenian coefficient:", -original_green[0, 1], "to", -green_matrix(result)[0, 1])
```

## Two Greenian coefficients

Increase two Greenian coefficients of a triangle by $1/3$. Compare the prescribed matrix with the Greenian of the recovered graph and check the spanning-tree normalization.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Joint Variation of Greenian Coefficients#Example - two Greenian coefficients of a triangle|Related section of the note]].

```python
lap = Matrix(laplacian(triangle).value.values)
gamma = {("a", "b"): Q(1, 3), ("a", "c"): Q(1, 3)}
increments = diag(*gamma.values())
joint = vary_greenian_coefficients(triangle, gamma)
expected_green = green_matrix(triangle) + directions * increments * directions.T
factor = (eye(2) + increments * directions.T * lap * directions).det()
assert green_matrix(joint) == expected_green
assert tree_weight(joint) * factor == tree_weight(triangle)
assert factor == 8 and tree_weight(joint) == Q(3, 8)
assert edge_weights(joint) == {("a", "b"): Q(1, 4), ("a", "c"): Q(1, 4), ("b", "c"): Q(5, 8)}
print("Joint Greenian variation: determinant factor =", factor)
```

## One resistance and quadric connectivity

Change only $R_{ab}$ and verify that the other resistances are preserved. Check the two inverse sensitivity matrices of the original triangle.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/One Resistance and Quadric Connectivity#Example - only one side resistance changes|Related section of the note]].

```python
one = vary_resistances(triangle, {edge: Q(1, 3)})
original_r = resistance_matrix(triangle)
one_r = resistance_matrix(one)
assert one_r - original_r == Matrix([[0, Q(1, 3), 0], [Q(1, 3), 0, 0], [0, 0, 0]])
assert tree_weight(triangle) / tree_weight(one) == Q(5, 4)

# The differential matrices are indexed by the same ordered list of vertex pairs.
pairs = list(combinations(range(3), 2))
incidence = Matrix.hstack(directions, Matrix([0, 1, -1]))
transfer = (incidence.T * green_matrix(triangle) * incidence).applyfunc(lambda value: value**2)
quadric = Matrix([[(lap[i, k]*lap[j, l] + lap[i, l]*lap[j, k])/2 for k, l in pairs]
                  for i, j in pairs])
assert transfer == Matrix([[4, 1, 1], [1, 4, 1], [1, 1, 4]]) / 9
assert transfer * quadric == eye(3)
print("One resistance: R(a,b) =", one_r[0, 1], "; quadric matrices are inverse")
```

## Two resistances

Compare simultaneous and sequential recovery. For a larger change, verify that the simultaneous result is admissible and that both intermediate states are singular.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Joint Variation of Resistances#An example with two resistances|Related section of the note]].

```python
deltas = {("a", "b"): Q(1, 3), ("a", "c"): Q(1, 3)}
result = vary_resistances(triangle, deltas)
sequential = vary_resistances(one, {("a", "c"): Q(1, 3)})
assert edge_weights(result) == edge_weights(sequential) == {
    ("a", "b"): Q(3, 5), ("a", "c"): Q(3, 5), ("b", "c"): Q(6, 5),
}
assert tree_weight(result) == Q(9, 5)
valid_joint = vary_resistances(triangle, {("a", "b"): 2, ("a", "c"): 2})
assert len(valid_joint.components) == 1
for pair in deltas:
    try:
        vary_resistances(triangle, {pair: 2})
    except InvalidInput:
        pass
    else:
        raise AssertionError("the intermediate metric is singular")
print("Joint resistance variation: tree weight =", tree_weight(result))
```

## A feasible change of the prism

Keep the boundary triangle and the forbidden pairs fixed. Check the exact boundary resistances and compare them with the result of eliminating the interior vertices.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Variations with Conductance Constraints#The prism example|Related section of the note]].

```python
boundary = tuple("abc")
fixed = tuple(combinations(boundary, 2))
variable = (("d", "e"), ("d", "f"), ("e", "f"), ("a", "d"), ("b", "e"), ("c", "f"))
prism = unit_graph("abcdef", (*fixed, *variable))


def target(k):
    r = Q(8, 15)
    return {("a", "b"): k*r, ("a", "c"): r, ("b", "c"): r}


def witness(k, g):
    a = (4*k*k - 31*k + 30) / (4*k*(4-k))
    b = (4*k - 1) / (4*(4-k))
    nu = g*b / (g-3*b)
    x = g*(a*g - b*(2*a+b)) / ((g-2*a-b)*(g-3*b))
    return (x, nu, nu, g, g, g)


def apply_witness(weights):
    return vary_conductances(prism, {pair: value-1 for pair, value in zip(variable, weights, strict=True)})


k = Q(9, 8)
values = witness(k, Q(7))
altered = apply_witness(values)
actual = edge_weights(altered)
assert values == (0, Q(7, 20), Q(7, 20), 7, 7, 7)
assert all(actual[pair] == 1 for pair in fixed)
assert set(actual) <= set(fixed + variable) and all(value >= 0 for value in actual.values())
assert resistance(altered, pairs=tuple(fixed)).value.values == tuple(target(k).values())
reduced = kron_reduce(altered, boundary).value.network
assert resistance(reduced, pairs=tuple(fixed)).value.values == tuple(target(k).values())
assert tree_weight(altered) == Q(7203, 4)
print("Constrained prism: c(de) =", values[0], "; tree weight =", tree_weight(altered))
```

## Exact constraint certificates

Clear the denominators using the spanning-tree polynomial and check two exact solutions. For $k=2$, the required reduced conductance of $ab$ is zero while its direct conductance is already one.

[[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/An Algorithm for Variations with Conductance Constraints#Returning to the prism and verification|Related section of the note]].

```python
variables, tree, residuals = resistance_constraint_polynomials(prism, variable, target(k))
for stretch, g in ((Q(9, 8), Q(7)), (Q(21, 20), Q(2))):
    active = witness(stretch, g)
    exact_graph = apply_witness(active)
    assignment = dict(zip(variables, active, strict=True))
    tree_at_witness = tree.subs(assignment)
    assert min(active) >= 0 and tree_at_witness == tree_weight(exact_graph) > 0
    # Residuals above use target(k). Substitute the new target without
    # rebuilding the three separating-forest numerators.
    for original, new, residual in zip(target(k).values(), target(stretch).values(), residuals, strict=True):
        assert residual.subs(assignment) + (original-new)*tree_at_witness == 0

# k = 2 would require zero reduced conductance ab, below its fixed direct value.
stretch = Q(2)
r_ab, r_ac, r_bc = target(stretch).values()
target_matrix = [[0, r_ab, r_ac], [r_ab, 0, r_bc], [r_ac, r_bc, 0]]
target_graph = network_from_resistance(target_matrix, boundary).value
assert edge_weights(target_graph).get(("a", "b"), 0) == 0
assert edge_weights(prism)[("a", "b")] == 1
print("Polynomial constraints: two exact witnesses; k = 2 violates the fixed edge bound")
```
