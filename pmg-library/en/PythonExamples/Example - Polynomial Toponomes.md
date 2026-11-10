---
title: "Example: Polynomial Toponomes"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-polynomial-toponomes
lang: en
description: "Five exact checks for normalizations, forest coefficients, the Kirchhoff index, and realizability."
order: 13
---

Five examples compare vector and vertex normalizations, compute the Kirchhoff index, and check examples of factorization and realizability. The series notes give the general proofs.

[[ru/PythonExamples/Пример - Полиномиальные топономы|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 3ae0e82](https://github.com/magin67/polyform_algebra/commit/3ae0e82e30c547e7980f1890bf1f62f5308b4a75).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/polynomial-toponomes.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/polynomial-toponomes.ipynb)

## Two normalizations of a path

Enumerate the forests of the unit-conductance path $P_6$. Two forests of type $(3,1)$ and one of type $(2^2)$ give $a_{4,2}=3$. Their root weights are $8$, $8$, and $9$, giving $b_{4,2}=25$. In each normalization, build the full toponome, the two-variable polynomial, and its specialization at $u=1$.

[[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Vector and Vertex Normalizations of Toponomes#The path on six vertices|Related section of the note]].

```python
from fractions import Fraction
from itertools import combinations
from math import comb, prod

from sympy import Matrix, Poly, expand, eye, symbols

from polyform_algebra.core import Network, green, laplacian, network, resistance, spanning_tree_weight
from polyform_algebra.toponomes import (
    coefficient_table, forest_toponome, laplacian_polynomial, partition_product,
    rooted_forest_weight, vertex_toponome,
)

t, u = symbols("t u")


def graph(labels, edges, conductance=1):
    return network(tuple(labels), tuple((a, b, conductance) for a, b in edges))


def polynomial(toponome):
    return sum(weight * t**k * u**r for (k, r), weight in coefficient_table(toponome).items())


def vertex_polynomial(net):
    return polynomial(vertex_toponome(forest_toponome(net)))


def from_coefficients(coefficients):
    return sum(value * t**k for k, value in enumerate(coefficients))


P6 = graph("abcdef", ("ab", "bc", "cd", "de", "ef"))
forest_types = forest_toponome(P6)
rooted_types = vertex_toponome(forest_types)
vector_table = coefficient_table(forest_types)
rooted_table = coefficient_table(rooted_types)
assert forest_types[(3, 1)] == 2 and forest_types[(2, 2)] == 1
assert rooted_types[(3, 1)] == 16 and rooted_types[(2, 2)] == 9
assert vector_table[4, 2] == 3 and rooted_table[4, 2] == 25
print("P₆ cell (4, 2): 3 forests, 25 rooted forests")

part_variables = symbols("x1:6")
full_vector = sum(
    value * prod(part_variables[j - 1] for j in kind)
    for kind, value in forest_types.items()
)
full_vertex = full_vector.subs({x: (j + 1) * x for j, x in enumerate(part_variables, 1)})
substitution = {x: t**j * u for j, x in enumerate(part_variables, 1)}
F6, V6 = map(polynomial, (forest_types, rooted_types))
assert expand(full_vector.subs(substitution)) == F6
assert expand(full_vertex.subs(substitution)) == V6
assert Poly(F6.subs(u, 1), t) == Poly((1 + t)**5, t)
assert V6.subs(u, 1) == from_coefficients((1, 10, 36, 56, 35, 6))
assert F6.subs({t: 1, u: 1}) == 32 and V6.subs({t: 1, u: 1}) == 144
print("P₆ totals: F(1,1) = 32, P(1,1) = 144")
```

## Prescribed roots and the Laplacian polynomial

For the cycle $C_4$, compare the vertex coefficients with $\det(I+tL)$ and the sums of principal minors. For prescribed roots $a,c$, enumerate two-edge forests and independently compute the minor of the original Laplacian. For a graph with two edges and an isolated vertex, check the degree $n-c$.

[[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial#A complete example: the cycle on four vertices|Related section of the note]].

```python
C4 = graph("abcd", ("ab", "bc", "cd", "da"))
L = Matrix(laplacian(C4).value.values)
expected = (1, 8, 20, 16)
assert polynomial(forest_toponome(C4)).subs(u, 1) == from_coefficients((1, 4, 6, 4))
assert vertex_polynomial(C4).subs(u, 1) == from_coefficients(expected)
assert laplacian_polynomial(C4) == expected
assert expand((eye(4) + t * L).det()) == from_coefficients(expected)
for k, coefficient in enumerate(expected):
    minors = [L.extract(indices, indices).det() for indices in combinations(range(4), k)]
    assert sum(minors) == coefficient
print("P(C₄) coefficients:", expected)

roots = {"a", "c"}
rooted_count = 0
for edges in combinations(C4.edges, 2):
    forest = Network(C4.context, edges)
    if all(len(roots.intersection(block)) == 1 for block in forest.components):
        rooted_count += 1
assert rooted_count == rooted_forest_weight(C4, ("a", "c")) == 4
print("Prescribed roots a, c:", rooted_count)

disconnected = network(tuple("abcde"), (("a", "b", 2), ("c", "d", 3)))
assert laplacian_polynomial(disconnected) == (1, 10, 24)
assert vertex_polynomial(disconnected).subs(u, 1) == from_coefficients((1, 10, 24))
assert len(laplacian_polynomial(disconnected)) - 1 == 5 - len(disconnected.components) == 2
```

## Forest coefficients and the Kirchhoff index

Sum the exact effective resistances over vertex pairs of the four-vertex path, star, and cycle. Compare each sum with the ratio $p_{n-2}/\tau$. For the triangle with conductances $1,2,3$, compare $R_{ab}$ with the weight of forests separating $a$ and $b$ divided by the spanning-tree weight. For $C_4$, also check the sum of squares of the reciprocal nonzero eigenvalues using the trace of $G^2$.

[[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Coefficients and Kirchhoff Indices#A path and a star on four vertices|Related section of the note]].

```python
P4 = graph("abcd", ("ab", "bc", "cd"))
star = graph("abcd", ("ab", "ac", "ad"))
assert polynomial(forest_toponome(P4)).subs(u, 1) == polynomial(forest_toponome(star)).subs(u, 1)


def kirchhoff_check(net, expected_index):
    labels = net.context.labels
    pairs = tuple(combinations(labels, 2))
    coefficients = laplacian_polynomial(net)
    tau = spanning_tree_weight(net).value
    p_previous, p_leading = coefficients[-2:]
    assert p_leading == len(labels) * tau
    forest_ratio = p_previous / tau
    pair_sum = sum(resistance(net, pairs=pairs).value.values)
    assert forest_ratio == pair_sum == expected_index
    return pair_sum


indices = tuple(kirchhoff_check(net, expected) for net, expected in (
    (P4, 10), (star, 9), (C4, 5),
))
print("Kirchhoff indices (P₄, star, C₄):", ", ".join(map(str, indices)))

triangle = network(tuple("abc"), (("a", "b", 1), ("a", "c", 2), ("b", "c", 3)))
separating_weight = rooted_forest_weight(triangle, ("a", "b"))
tau = spanning_tree_weight(triangle).value
R_ab = resistance(triangle, pairs=(("a", "b"),)).value.values[0]
assert separating_weight == 5 and tau == 11
assert R_ab == separating_weight / tau == Fraction(5, 11)
print("Weighted triangle: R_ab = 5/11")

p1, p2, p3 = laplacian_polynomial(C4)[1:]
reciprocal_square_sum = (p2 / p3)**2 - 2 * (p1 / p3)
G = Matrix(green(C4).value.values)
assert (G**2).trace() == reciprocal_square_sum == Fraction(9, 16)
```

## Products and factorization

Compare ordinary multiplication for two disjoint edges with the partial-matching product. The falling-power substitution gives a polynomial representation of the second product. At $u=1$, the connected path gains factors. In vertex normalization also check $P_{C_6}(t)=P_{K_3}(t)P_{K_{1,3}}(t)$.

[[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Reducibility of Toponomes#What changes after passing to one variable|Related section of the note]].

```python
P3 = graph("abc", ("ab", "bc"))
two_edges = graph("abcd", ("ab", "cd"))
edge = graph("ab", ("ab",))
assert polynomial(forest_toponome(P3)).subs(u, 1) == expand((1 + t)**2)
assert vertex_polynomial(P3).subs(u, 1) == expand((1 + t) * (1 + 3*t))

edge_types = forest_toponome(edge)
ordinary = polynomial(forest_toponome(two_edges))
matched = partition_product(edge_types, edge_types)
assert ordinary == expand(polynomial(edge_types)**2)
assert polynomial(matched) - ordinary == t**2 * u


def falling_image(toponome):
    return expand(sum(
        coefficient * t**k * prod(u - j for j in range(r))
        for (k, r), coefficient in coefficient_table(toponome).items()
    ))


assert falling_image(forest_toponome(two_edges)) == expand(1 + 2*t*u + t**2*u*(u - 1))
assert falling_image(matched) == expand(falling_image(edge_types)**2)
print("Two edges: ordinary (1 + tu)²; falling-power image 1 + 2tu + t²u(u − 1)")

C6 = graph("abcdef", ("ab", "bc", "cd", "de", "ef", "fa"))
K3 = graph("abc", ("ab", "ac", "bc"))
cycle_polynomial, triangle_polynomial, star_polynomial = (
    from_coefficients(laplacian_polynomial(net)) for net in (C6, K3, star)
)
assert len(C6.components) == 1
assert cycle_polynomial == expand(triangle_polynomial * star_polynomial)
print("One variable: P(C₆) = P(K₃) P(K₁,₃)")
```

## Checking graph realizability

The formal table $A_*$ has the right column sums, but $a_{2,1}=1$ violates the lower bound $M-q=2$. Also enumerate every three-edge graph on six letter-named vertices. Any three-edge graph can be brought to this size by removing or adding isolated vertices. For a positive example in vertex normalization, a triangle with conductances $1/3$ realizes $(1+t)^2$.

[[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Graph Realizability of Toponomes#A nonrealizable triangle with valid column sums|Related section of the note]].

```python
candidate = 1 + 3*t*u + t**2*u + 2*t**2*u**2 + t**3*u
assert candidate.subs(u, 1) == expand((1 + t)**3)
assert candidate.coeff(t**2*u) == 1 < 3 - 1

# Three edges can meet at most six vertices. Including isolated vertices
# lets the search on this one vertex set cover every three-edge graph.
labels = "abcdef"
three_edges = tuple(combinations(combinations(labels, 2), 3))
assert len(three_edges) == comb(15, 3) == 455
assert all(polynomial(forest_toponome(graph(labels, edges))) != candidate for edges in three_edges)
print("A*: no match among 455 labeled three-edge graphs")

weighted_K3 = graph("abc", ("ab", "ac", "bc"), Fraction(1, 3))
assert laplacian_polynomial(weighted_K3) == (1, 2, 1)
assert vertex_polynomial(weighted_K3).subs(u, 1) == expand((1 + t)**2)
print("Triangle with conductance 1/3: P(t) = (1 + t)²")
```
