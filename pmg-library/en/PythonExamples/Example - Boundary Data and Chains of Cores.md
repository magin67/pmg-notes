---
title: "Example: Boundary Data and Chains of Cores"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-boundary-data-core-chains
lang: en
description: "Thirteen calculations show how boundary data determine properties of assembled graphs. The four-point pairing has rank 14, two chains of three hexagons each have 204 spanning trees, and the two square-strip closures have 75 and 81."
order: 18
---

Thirteen calculations show how boundary data determine properties of assembled graphs. The four-point pairing has rank 14, two chains of three hexagons each have 204 spanning trees, and the two square-strip closures have 75 and 81.

[[ru/PythonExamples/Пример - Граничные данные и цепочки ядер|Русский]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra a7fa4b5](https://github.com/magin67/polyform_algebra/commit/a7fa4b54aaa29f5c42213bf2e97f74f922da3ead).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/boundary-data-core-chains.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/boundary-data-core-chains.ipynb)

## Forest passport of a path

Compute the state polynomials of the path $a-b-c-d-e$ with boundary $a,c,e$. The state $ae|c$ is absent, and the other polynomials sum to the ordinary forest polynomial.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#The five polynomials of the path P5|Related section of the note]].

```python
from collections import Counter
from fractions import Fraction as Q
from itertools import product

from sympy import Matrix, Symbol, expand

from polyform_algebra.boundary_data import (
    forest_passport, join_forest_states, pair_forest_passports,
    pair_spectral_passports, spectral_pair_passport,
)
from polyform_algebra.core import circumsphere, contract, kron_reduce, laplacian, network, spanning_tree_weight
from polyform_algebra.core_chains import cycle_chain_tree_count
from polyform_algebra.matroid import forest_coefficients
from polyform_algebra.toponomes import forest_toponome, laplacian_polynomial, rooted_forest_weight


def unit_graph(labels, edges):
    return network(tuple(labels), [(a, b, 1) for a, b in edges])


def path_edges(labels):
    return tuple(zip(labels, labels[1:]))


def cycle_edges(labels):
    return (*path_edges(labels), (labels[-1], labels[0]))


def polynomial(coefficients, variable):
    return sum(value * variable**grade for grade, value in enumerate(coefficients))


def state(name):
    return tuple(tuple(block) for block in name.split("|"))


path = unit_graph("abcde", path_edges("abcde"))
boundary = tuple("ace")
passport = forest_passport(path, boundary)
assert passport == {
    state("a|c|e"): {0: 1, 1: 4, 2: 4},
    state("ac|e"): {2: 1, 3: 2},
    state("a|ce"): {2: 1, 3: 2},
    state("ace"): {4: 1},
}
assert tuple(sum(poly.get(k, 0) for poly in passport.values()) for k in range(5)) == forest_coefficients(path)
for blocks, coefficients in passport.items():
    print("P5 state", "|".join(map("".join, blocks)),
          polynomial(tuple(coefficients.get(k, 0) for k in range(5)), Symbol("t")))
```

## Three contractions

For each contraction, retain the compatible forest states and compare the resulting coefficients with a direct calculation on the quotient graph.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test#Example: three contractions of P5|Related section of the note]].

```python
for partition, expected in (
    ("ac|e", (1, 4, 5, 2)),
    ("ae|c", (1, 4, 6, 4)),
    ("ace", (1, 4, 4)),
):
    boundary_state = state(partition)
    quotient = contract(path, {"".join(block): block for block in (*boundary_state, ("b",), ("d",))}).value.network
    predicted = tuple(sum(poly.get(k, 0) for blocks, poly in passport.items()
                          if join_forest_states(boundary, blocks, boundary_state) is not None)
                      for k in range(len(quotient.context.labels)))
    assert predicted == forest_coefficients(quotient) == expected
    print("Contraction", partition, tuple(map(str, predicted)))
```

## Pairing forest passports

Glue two paths along $a,c,e$. Compare all state polynomials obtained by pairing compatible states with direct enumeration on the glued graph.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data#The bilinear law for the full forest polynomial|Related section of the note]].

```python
other_path = unit_graph("afcge", path_edges("afcge"))
joined = network(tuple("abcdefg"), path.edges + other_path.edges)
combined = pair_forest_passports(boundary, passport, forest_passport(other_path, boundary))
assert combined == forest_passport(joined, boundary)
assert combined[state("ace")][6] == 16
print("Paired passport:", len(combined), "states; spanning trees:", combined[state("ace")][6])
```

## Spanning trees and boundary response

For one path and for the glued pair, compare the spanning-tree cofactor with the product of the interior minor and a cofactor of the boundary response.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry#Two paths with a shared three-point boundary|Related section of the note]].

```python
for graph, expected in ((path, 1), (joined, 16)):
    response = Matrix(laplacian(kron_reduce(graph, boundary).value.network).value.values)
    interior_minor = rooted_forest_weight(graph, boundary)
    assert interior_minor == (4 if graph == path else 16)
    assert interior_minor * response[1:, 1:].det() == spanning_tree_weight(graph).value == expected
assert Matrix(laplacian(kron_reduce(path, boundary).value.network).value.values) == Matrix(
    [[Q(1, 2), Q(-1, 2), 0], [Q(-1, 2), 1, Q(-1, 2)], [0, Q(-1, 2), Q(1, 2)]]
)
print("Spanning-tree counts via boundary response: 1, 16")
```

## Rank of the four-point matrix

Build the compatibility matrix for all 15 partitions. Check the relation vector and the determinant of the minor for the first 14 states.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction#The reduced matrix and rank fourteen|Related section of the note]].

```python
four_boundary = tuple("abcd")
names = ("a|b|c|d", "ab|c|d", "ac|b|d", "ad|b|c", "a|bc|d", "a|bd|c", "a|b|cd",
         "abc|d", "abd|c", "acd|b", "a|bcd", "ab|cd", "ad|bc", "abcd", "ac|bd")
states = tuple(map(state, names))
pairing = Matrix([[int(join_forest_states(four_boundary, a, b) is not None)
                   for b in states] for a in states])
relation = Matrix([0] * 7 + [-1] * 4 + [1] * 4)
assert pairing * relation == Matrix.zeros(15, 1)
assert pairing.rank() == 14 and pairing[:14, :14].det() == -64
print("Four-point matrix: rank", pairing.rank(), "out of", pairing.rows)
```

## Spectral pairing

Glue two length-two paths at their endpoints. Compare all five polynomials with direct minors and check Jacobi's identity. The identity remains valid at $x=2$, where the interior minor vanishes.

[[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data#Gluing along two shared vertices|Related section of the note]].

```python
x = Symbol("x")
terminals = tuple("ab")
first = unit_graph("acb", path_edges("acb"))
second = unit_graph("adb", path_edges("adb"))
cycle = network(tuple("acbd"), first.edges + second.edges)
left, right = (spectral_pair_passport(graph, terminals, x) for graph in (first, second))
full, minor_a, minor_b, cross, interior = left
assert expand(full * interior - minor_a * minor_b + cross**2) == 0
paired = pair_spectral_passports(left, right, x)
assert paired == spectral_pair_passport(cycle, terminals, x)
assert paired[0] == x**4 - 8*x**3 + 20*x**2 - 16*x
assert paired[0].subs(x, 2) == 0 and interior.subs(x, 2) == 0
print("Spectral gluing:", paired[0])
```

## Spanning trees of a square ladder

Compare the recurrence $\tau_{k+2}=4\tau_{k+1}-\tau_k$ with direct tree cofactors of the ladders.

[[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence#Starting with a square ladder|Related section of the note]].

```python
def ladder(top, bottom):
    return unit_graph(top + bottom, (*path_edges(top), *path_edges(bottom), *zip(top, bottom)))


top, bottom = "abcdef", "uvwxyz"
ladders = [ladder(top[:n], bottom[:n]) for n in range(1, 7)]
direct = [spanning_tree_weight(graph).value for graph in ladders]
recurrence = [1, 4]
for _ in range(4):
    recurrence.append(4 * recurrence[-1] - recurrence[-2])
assert direct == recurrence == [1, 4, 15, 56, 209, 780]
print("Square ladder tree counts:", tuple(map(str, direct)))
```

## Transfer of ladder forest states

Compare the transfer of two polynomials for connected and disconnected contacts with the ladder passports. For a single square, also check the component-size toponome and the rooted polynomial.

[[en/Graph Transformations and Gluing/Chains of cores/The Laplacian Exponential in Graph Weaving#The ordinary forest polynomial and a second-order recurrence|Related section of the note]].

```python
t = Symbol("t")
forest_polynomials = [polynomial(forest_coefficients(graph), t) for graph in ladders[:4]]
assert [f.subs(t, 1) for f in forest_polynomials] == [2, 15, 112, 836]
h4, b4 = (1 + t)**2, t**2
transfer = Matrix([[t*h4 + (1-t)*b4, t*h4], [h4-b4, h4]])
predicted = Matrix([t, 1])
for index, graph in enumerate(ladders[:4]):
    active = (top[index], bottom[index])
    data = forest_passport(graph, active)
    observed = Matrix([sum(value*t**k for k, value in data[blocks].items())
                       for blocks in ((active,), tuple((v,) for v in active))])
    assert (observed - predicted).applyfunc(expand) == Matrix.zeros(2, 1)
    predicted = transfer * predicted
for f, g, h in zip(forest_polynomials, forest_polynomials[1:], forest_polynomials[2:]):
    assert expand(h - (1 + 3*t + 4*t**2)*g + t**2*(1+t)**2*f) == 0
assert forest_toponome(ladders[1]) == {(): 1, (1,): 4, (2,): 4, (1, 1): 2, (3,): 4}
assert laplacian_polynomial(ladders[1]) == (1, 8, 20, 16)
print("Square ladder forest counts:", tuple(f.subs(t, 1) for f in forest_polynomials))
```

## Two admissible chains

Build two chains with different seam placements. Count shared edges once. Check vertex, edge and spanning-tree counts and the resistance radius.

[[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains#Two assemblies of three hexagons|Related section of the note]].

```python
def chain_of_cycles(cores):
    labels = tuple(dict.fromkeys("".join(cores)))
    edges = sorted({tuple(sorted(edge)) for core in cores for edge in cycle_edges(core)})
    return unit_graph(labels, edges)


def hexagon_chain(second_seam):
    cores = ("abjihg", "abcdef", second_seam + "nmlk")
    first_seam = set("ab")
    assert set(cores[0]) & set(cores[1]) == first_seam
    assert set(cores[1]) & set(cores[2]) == set(second_seam)
    assert not set(cores[0]) & set(cores[2])
    graph = chain_of_cycles(cores)
    assert len(graph.context.labels) == 14 and len(graph.edges) == 16
    return graph


hexagons = (hexagon_chain("de"), hexagon_chain("cd"))
assert [spanning_tree_weight(graph).value for graph in hexagons] == [204, 204]
assert [circumsphere(graph).value.resistance_radius for graph in hexagons] == [Q(43595, 41616)] * 2
print("Three hexagons: 14 vertices, 16 edges, 204 trees in each assembly")
```

## Matroid and configuration

Compare the multiplicities of dual edges by face pair. The ordinary forest polynomials agree, and the rooted polynomials differ.

[[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#Two chains of three hexagons|Related section of the note]].

```python
def dual_edge_counts(cores):
    # Face A denotes the outer face; B, C, D are the three cycle cores.
    faces = {}
    for face, core in zip("BCD", cores, strict=True):
        for edge in cycle_edges(core):
            faces.setdefault(tuple(sorted(edge)), []).append(face)
    return Counter(tuple(sorted(pair if len(pair) == 2 else ["A", *pair])) for pair in faces.values())


dual_counts = [dual_edge_counts(("abjihg", "abcdef", seam + "nmlk")) for seam in ("de", "cd")]
assert dual_counts[0] == dual_counts[1] == {("A", "B"): 5, ("A", "C"): 4, ("A", "D"): 5,
                                           ("B", "C"): 1, ("C", "D"): 1}
ordinary = [forest_coefficients(graph) for graph in hexagons]
rooted = [laplacian_polynomial(graph) for graph in hexagons]
assert ordinary[0] == ordinary[1]
assert rooted[0] != rooted[1]
degree_three_edges = []
for graph in hexagons:
    degree_three = {v for v in graph.context.labels if sum(v in edge[:2] for edge in graph.edges) == 3}
    degree_three_edges.append(sum(a in degree_three and b in degree_three for a, b, _ in graph.edges))
assert degree_three_edges == [2, 3]
print("Hexagon configurations: same ordinary polynomial; degree-three edges:", *degree_three_edges)
```

## Determinant and continuant

Compare the continuant with the determinant of the dual minor and with direct spanning-tree cofactors of the assembled chains.

[[en/Graph Transformations and Gluing/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#Explicit assemblies and independent checks|Related section of the note]].

```python
for size in (4, 6):
    for count in range(1, 6):
        dual_minor = Matrix(count, count, lambda i, j: size if i == j else -int(abs(i-j) == 1))
        assert cycle_chain_tree_count([size] * count, [1] * (count-1)) == dual_minor.det()
assert cycle_chain_tree_count([4, 5, 6], [1, 2]) == cycle_chain_tree_count([6, 5, 4], [2, 1])
assert cycle_chain_tree_count([6, 6, 6], [1, 1]) == spanning_tree_weight(hexagons[0]).value
assert cycle_chain_tree_count([4] * 5, [1] * 4) == direct[-1]
print("Continuants agree with dual determinants and direct cofactors")
```

## Limits of the tree count

Check two graphs with 12 spanning trees. Their exact resistance radii differ.

[[en/Graph Transformations and Gluing/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores#An equal spanning-tree count does not determine the radius|Related section of the note]].

```python
square_triangle = chain_of_cycles(("abcd", "aef"))
bipartite_with_leaf = unit_graph("abcdef", (*product("ab", "cde"), ("a", "f")))
assert [spanning_tree_weight(graph).value for graph in (square_triangle, bipartite_with_leaf)] == [12, 12]
radii = [circumsphere(graph).value.resistance_radius for graph in (square_triangle, bipartite_with_leaf)]
assert radii == [Q(77, 144), Q(7, 12)]
print("Equal tree counts, different radii:", *radii)
```

## Two strip closures

Add the straight or twisted seam. Compare the tree counts and resistance radii of the cylindrical and Möbius strips.

[[en/Graph Transformations and Gluing/Chains of cores/Closing a Chain - Rings and the Möbius Effect#The final seam of a square strip|Related section of the note]].

```python
strip_top, strip_bottom = "abc", "uvw"
rungs_and_rails = (*path_edges(strip_top), *path_edges(strip_bottom), *zip(strip_top, strip_bottom))
cylinder = unit_graph(strip_top + strip_bottom, (*rungs_and_rails, ("c", "a"), ("w", "u")))
mobius = unit_graph(strip_top + strip_bottom, (*rungs_and_rails, ("c", "u"), ("w", "a")))
counts = [spanning_tree_weight(graph).value for graph in (cylinder, mobius)]
radii = [circumsphere(graph).value.resistance_radius for graph in (cylinder, mobius)]
assert counts == [75, 81] and counts[1] - counts[0] == 2 * 3
assert radii == [Q(47, 180), Q(1, 4)]
print("Cylindrical and Möbius closures:", *counts)
```
