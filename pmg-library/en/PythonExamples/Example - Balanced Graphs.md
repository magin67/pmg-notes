---
title: "Example: Balanced Graphs"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-balanced-graphs
lang: en
description: "Twelve exact calculations for outgoing Laplacians, directional metrics, and forests."
order: 14
---

Twelve calculations use the outgoing Laplacian convention. Bilinear forms are checked through coefficient matrices and minors.

[[ru/PythonExamples/Пример - Балансовые графы|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 94f2e3b](https://github.com/magin67/polyform_algebra/commit/94f2e3bd98d999eb3af6b62b9bbfa764bccb36ee).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/balanced-graphs.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/balanced-graphs.ipynb)

## Tree potentials of a triangle

Combine opposite directed cycles with weights $p=2$ and $q=1$. Check balance and compare each principal cofactor with $p^2+pq+q^2$.

[[en/Directed Graphs and Extensions/Balanced graphs/Balanced Graphs and Spanning-Tree Potentials#A triangle with both cycle directions|Related section of the note]].

```python
from itertools import combinations, permutations
from math import prod

from sympy import Matrix, Rational, diag, expand, eye, ones, symbols, zeros

from polyform_algebra.directed import DirectedNetwork


def cycle(labels, weight=1):
    return tuple((a, b, weight) for a, b in zip(labels, labels[1:] + labels[:1]))


labels = tuple("abc")
forward, backward = cycle(labels), cycle(tuple(reversed(labels)))
unit = DirectedNetwork(labels, forward)
reverse = DirectedNetwork(labels, backward)
triangle = DirectedNetwork(labels, cycle(labels, 2) + backward)
assert triangle.laplacian() == 2 * unit.laplacian() + reverse.laplacian()
assert ones(1, 3) * triangle.laplacian() == zeros(1, 3)
assert triangle.tree_potentials() == (2**2 + 2 * 1 + 1**2,) * 3
print("Tree potentials for p = 2, q = 1:", triangle.tree_potentials())
```

## Centered representations of the Laplacian

Represent bilinear terms by outer products of coefficient columns. Using $c$ or the centroid as reference gives the same outgoing Laplacian.

[[en/Directed Graphs and Extensions/Balanced graphs/The Bilinear Laplacian of a Balanced Graph#One directed 3-cycle in different representations|Related section of the note]].

```python
vertices = [eye(3)[:, i] for i in range(3)]
L = unit.laplacian()
J = eye(3) - ones(3) / 3
for reference in (vertices[2], ones(3, 1) / 3):
    centered = [vertex - reference for vertex in vertices]
    terms = [centered[i] * (vertices[i] - vertices[(i + 1) % 3]).T for i in range(3)]
    assert sum(terms, zeros(3)) == L
assert J * L * J == L
assert L[:2, :2] == Matrix([[1, -1], [0, 1]])
print("Both centered coefficient matrices equal L")
```

## Grade two of the cycle exponential

For each reference, sum products of the left and right determinants for pairs of arc terms. Compare grade two with the minor in the basis $a-c,b-c$.

[[en/Directed Graphs and Extensions/Balanced graphs/The Laplacian Exponential of a Balanced Graph#Example: the unit directed 3-cycle|Related section of the note]].

```python
def exterior_minor_sum(terms, grade):
    return sum(
        Matrix.hstack(*(left for left, _ in chosen)).det()
        * Matrix.hstack(*(right for _, right in chosen)).det()
        for chosen in combinations(terms, grade)
    )


for reference in (vertices[2], ones(3, 1) / 3):
    terms = [
        ((vertices[i] - reference)[:2, :], (vertices[i] - vertices[(i + 1) % 3])[:2, :])
        for i in range(3)
    ]
    assert exterior_minor_sum(terms, 2) == L[:2, :2].det() == unit.tree_potentials()[2] == 1
print("The grade-two coefficient of the unit cycle is 1")
```

## The circulation form

Compare the difference of the reverse and forward Laplacians with the skew form on $b-a,c-a$.

[[en/Directed Graphs and Extensions/Balanced graphs/The Circulation Form#How circulation appears in a directed 3-cycle|Related section of the note]].

```python
ab, ac = vertices[1] - vertices[0], vertices[2] - vertices[0]
circulation = ab * ac.T - ac * ab.T
assert reverse.laplacian() - L == circulation
symmetric_triangle = sum(
    ((vertices[i] - vertices[j]) * (vertices[i] - vertices[j]).T
     for i, j in combinations(range(3), 2)), zeros(3)
)
assert 2 * L == symmetric_triangle - circulation
print("Circulation sign and symmetric part verified")
```

## Adding the reverse directed cycle

Add the reverse cycle with weight $t$. Compute a symbolic cofactor and compare it with tree potentials at several exact weights.

[[en/Directed Graphs and Extensions/Balanced graphs/Balanced Variations#Adding a directed cycle|Related section of the note]].

```python
t = symbols("t")
variation = L + t * reverse.laplacian()
assert expand(variation[:2, :2].det()) == 1 + t + t**2
for weight in (0, Rational(1, 2), 1, 2):
    varied = DirectedNetwork(labels, forward + cycle(tuple(reversed(labels)), weight))
    assert varied.tree_potentials() == (1 + weight + weight**2,) * 3
print("Adding the reverse cycle: tau(t) = 1 + t + t²")
```

## One-way resistances and hitting times

Add a bidirectional coupling $ab$ to the unit cycle. Compute one-way resistances and solve the hitting-time systems with a fixed target.

[[en/Directed Graphs and Extensions/Balanced graphs/One-Way Resistance and Hitting Times#Markov interpretation|Related section of the note]].

```python
extra = DirectedNetwork(labels, forward + (("a", "b", 1), ("b", "a", 1)))
L_extra = extra.laplacian()
r = extra.one_way_resistances()
assert r == Matrix([[0, 1, 4], [2, 0, 3], [2, 3, 0]]) / 6
hitting = zeros(3)
for target in range(3):
    keep = [i for i in range(3) if i != target]
    solution = L_extra.extract(keep, keep).inv() * ones(2, 1)
    for index, value in zip(keep, solution):
        hitting[index, target] = value
assert hitting == 3 * r
print("One-way resistances a→b and b→a:", r[0, 1], r[1, 0])
```

## Three-vertex resistance

Build the bilinear metric on two differences. Compare its determinant with that of the symmetric part plus the circulation contribution.

[[en/Directed Graphs and Extensions/Balanced graphs/Resistance Geometry and Circulation#Three-vertex resistance|Related section of the note]].

```python
Gr = extra.centered_greenian()
beta = Matrix.hstack(ab, ac).T * Gr.T * Matrix.hstack(ab, ac)
g = (beta + beta.T) / 2
chi = beta[0, 1] - beta[1, 0]
assert chi == r[0, 1] + r[1, 2] + r[2, 0] - r[0, 2] - r[2, 1] - r[1, 0]
assert beta.det() == g.det() + chi**2 / 4 == 1 / L_extra[:2, :2].det()
assert beta[0, 0] == r[0, 1] + r[1, 0]
print("Triangle potential and squared circulation:", beta.det(), chi**2)
```

## Directional pairings

Compute the local vertex Gram matrix and check two directional pairings. Evaluate a pairing of differences through incoming and outgoing di-coordinates.

[[en/Directed Graphs and Extensions/Balanced graphs/The Gram Matrix and Directional Coordinates of a Balanced Graph#An example with unequal directional pairings|Related section of the note]].

```python
G = extra.vertex_gram()
assert G == Matrix([[0, -4, -5], [-2, 0, -7], [-7, -5, 0]]) / 12
assert J * G * J == Gr.T and G * ones(3, 1) == G.T * ones(3, 1)
u, v = vertices[0] - vertices[2], vertices[1] - vertices[2]
assert ((G.T * u).T * v)[0] == (u.T * (G * v))[0] == (u.T * G * v)[0]
assert G[0, 1] == -Rational(1, 3) and G[1, 0] == -Rational(1, 6)
print("Directional pairings a→b and b→a:", G[0, 1], G[1, 0])
```

## Two coordinate systems of the sphere

Invert the Gram matrix extended by the null vector. Compare the incoming and outgoing center coordinates and the common quadratic radius.

[[en/Directed Graphs and Extensions/Balanced graphs/The Isotropic Space and Sphere of a Balanced Graph#Example: two coordinate systems and one radius|Related section of the note]].

```python
one = ones(3, 1)
extended = G.row_join(one).col_join(one.T.row_join(zeros(1)))
inverse = extended.inv()
diagonal = Gr.diagonal().T
b_in = one / 3 + L_extra.T * diagonal / 2
b_out = one / 3 + L_extra * diagonal / 2
rho = sum(diagonal) / 3 + (diagonal.T * L_extra * diagonal)[0] / 4
assert inverse[:3, :3] == L_extra.T
assert inverse[:3, 3] == b_in == Matrix([3, 4, 5]) / 12
assert inverse[3, :3].T == b_out == Matrix([4, 3, 5]) / 12
assert inverse[3, 3] == rho == Rational(41, 144)
print("Sphere: incoming", tuple(b_in), "outgoing", tuple(b_out), "rho =", rho)
```

## Balancing three participants

Use the three tree potentials to scale the rows. Check balance and equality of the new potentials.

[[en/Directed Graphs and Extensions/Balanced graphs/Balancing a Directed Graph by Spanning-Tree Potentials#A three-participant example|Related section of the note]].

```python
ratings = DirectedNetwork(labels, (("a", "b", 1), ("a", "c", 2), ("b", "a", 2),
                                    ("b", "c", 1), ("c", "a", 1), ("c", "b", 1)))
assert ratings.tree_potentials() == (5, 4, 7)
balanced, factors = ratings.balance()
assert factors == tuple(Rational(i, 16) for i in (15, 12, 21))
assert balanced.laplacian() == diag(*factors) * ratings.laplacian()
assert ones(1, 3) * balanced.laplacian() == zeros(1, 3)
assert balanced.tree_potentials() == (Rational(315, 64),) * 3
print("Balancing multipliers:", factors)
```

## The toponome of a directed cycle

Enumerate the rooted forests of the directed four-cycle by type. Divide by component sizes for vector normalization and compare the vertex polynomial with the determinant.

[[en/Directed Graphs and Extensions/Balanced graphs/Toponomes of Balanced Graphs and Directed Forests#Unit directed 3- and 4-cycles|Related section of the note]].

```python
four = tuple("abcd")
directed_square = DirectedNetwork(four, cycle(four))
rooted = directed_square.forest_toponome()
assert rooted == {(): 1, (1,): 4, (2,): 4, (1, 1): 2, (3,): 4}
vector = {kind: weight / Rational(prod(grade + 1 for grade in kind))
          for kind, weight in rooted.items()}
assert vector == {(): 1, (1,): 2, (2,): Rational(4, 3), (1, 1): Rational(1, 2), (3,): 1}
polynomial = sum(weight * t**sum(kind) for kind, weight in rooted.items())
assert expand((eye(4) + t * directed_square.laplacian()).det()) == polynomial
print("Directed C₄ vertex polynomial:", polynomial)
```

## Permutations without loops

Enumerate permutations of four letters with no fixed points and compare their counts by type with the first-kind potential.

[[en/Directed Graphs and Extensions/Balanced graphs/Permutation Digraphs and Cycle Combinatorics#Graph type and its probability|Related section of the note]].

```python
from collections import Counter
from polyform_algebra.combinatorics import first_kind_potential


def cycle_type(images):
    successors = dict(zip(four, images))
    remaining = set(four)
    lengths = []
    while remaining:
        vertex = min(remaining)
        length = 0
        while vertex in remaining:
            remaining.remove(vertex)
            vertex = successors[vertex]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


derangements = Counter(cycle_type(images) for images in permutations(four)
                       if all(a != b for a, b in zip(four, images)))
assert derangements == {(4,): 6, (2, 2): 3}
assert all(count == first_kind_potential(kind) for kind, count in derangements.items())
print("Four vertices without loops: six 4-cycles and three pairs of 2-cycles")
```
