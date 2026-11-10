---
title: "Example: Checking Structural Identities"
date: 2026-11-10
updated: 2026-11-10
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-structural-identities
lang: en
description: "Exact checks of form equality, rank, supports, and graph gluing."
order: 9
---

Five calculations accompany the five notes. Check equality of both sides, find independent relations, and examine how rewriting a form affects a graph-gluing calculation.

[[ru/PythonExamples/Пример - Проверка структурных тождеств|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 73ac82d](https://github.com/magin67/polyform_algebra/commit/73ac82d5c16afbfd47285436e1b6f37d5a68f8af).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/structural-identities.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/structural-identities.ipynb)

## The tetrahedron identity

On vertices $a,b,c,d$, sum the three pair-partition forms on the left and the four triple forms on the right. The function `q` squares the exterior product of the listed block boundaries. Omitted vertices are singletons. The string `"ab"` here denotes a block of two letter-named vertices.

$$
q_{ab|cd}+q_{ac|bd}+q_{ad|bc}
=q_{abc}+q_{abd}+q_{acd}+q_{bcd}
$$

The check compares all formal coefficients in one context. Then increase the coefficient of $q_{abc}$ on the right by one. The comparison should detect the error, and the difference should have a nonzero coefficient. The printed blades $a\wedge b$ belong to the exterior power of the formal vertex space.

[[en/Polyform Algebra and Combinatorics/Structural identities/Partition Forms and the Tetrahedron Identity#The tetrahedron identity|Related section of the note]].

```python
from itertools import combinations

from sympy import Matrix, zeros
from polyform_algebra.core import (
    Context, equivalent, form_coefficients, form_exp, form_product, grade_part,
    network, partition_form, spanning_coefficient, spanning_tree_weight,
)

def q(context, *blocks):
    return partition_form(context, tuple(tuple(block) for block in blocks)).value

def tetrahedron(context, vertices):
    a, b, c, d = vertices
    left = q(context, (a, b), (c, d)) + q(context, (a, c), (b, d)) + q(context, (a, d), (b, c))
    right = q(context, (a, b, c)) + q(context, (a, b, d)) + q(context, (a, c, d)) + q(context, (b, c, d))
    return left, right

four = Context(tuple("abcd"))
left, right = tetrahedron(four, four.labels)
assert equivalent(left, right).value
assert form_coefficients(left - right).value == ()

perturbed = right + q(four, "abc")
assert not equivalent(left, perturbed).value
(i, j), coefficient = form_coefficients(left - perturbed).value[0]
blades = tuple(" ∧ ".join(four.labels[position] for position in blade) for blade in (i, j))
print("Tetrahedron identity:", equivalent(left, right).value)
print("First coefficient of left - perturbed right:", blades, "→", coefficient)
```

## Transfer and multiplication

Transfer the identity to the context $a,b,c,d,e,f$ and multiply both sides by the separate pair form $ef$. Check the second equality after enlarging the fourth block to $def$, as in equation (5) of the note.

On five vertices also check $E_5[2,1]=3E_5[3,0]$. On the left each triple has a complementary pair, and on the right each quadruple gives one partition. Count every partition once. This calculation connects structural identities to symmetric sums.

[[en/Polyform Algebra and Combinatorics/Structural identities/Constructing Structural Identities#Two examples on six vertices|Related section of the note]].

```python
six = Context(tuple("abcdef"))
left, right = tetrahedron(six, "abcd")
extra_pair = q(six, "ef")
lifted_left = form_product(left, extra_pair).value
lifted_right = form_product(right, extra_pair).value
assert equivalent(lifted_left, lifted_right).value

enlarged_left = q(six, "abc", "def")
enlarged_right = (
    q(six, "ab", "cdef") + q(six, "ac", "bdef") + q(six, "bc", "adef")
    - q(six, "bcdef") - q(six, "acdef") - q(six, "abdef")
)
assert equivalent(enlarged_left, enlarged_right).value
print("With the extra pair ef:", equivalent(lifted_left, lifted_right).value)
print("With the larger block def:", equivalent(enlarged_left, enlarged_right).value)

five = Context(tuple("abcde"))
triple_pair = [
    q(five, triple, tuple(v for v in five.labels if v not in triple))
    for triple in combinations(five.labels, 3)
]
quadruple = [q(five, block) for block in combinations(five.labels, 4)]
E_21 = sum(triple_pair[1:], triple_pair[0])
E_30 = sum(quadruple[1:], quadruple[0])
assert equivalent(E_21, 3 * E_30).value
print("E5[2,1] = 3 E5[3,0]:", equivalent(E_21, 3 * E_30).value)
```

## Rank and kernel on four vertices

Put the six noncrossing partition forms first and $q_{ac|bd}$ last. Each row corresponds to a pair of basis blades. Expand each form once and use exact row reduction. The first six columns are pivots, so the rank is $6$ and the kernel is one-dimensional. Its vector with last coordinate $1$ expresses the crossing partition in the basis.

[[en/Polyform Algebra and Combinatorics/Structural identities/Basis and Dimension of the Space of Partition Forms#Four vertices: a basis and an explicit check|Related section of the note]].

```python
def coefficient_matrix(forms):
    columns = [dict(form_coefficients(form).value) for form in forms]
    pairs = sorted(set().union(*columns))
    return Matrix([[column.get(pair, 0) for column in columns] for pair in pairs])

basis = [
    q(four, "bcd"), q(four, "acd"), q(four, "abd"), q(four, "abc"),
    q(four, "ab", "cd"), q(four, "ad", "bc"),
]
crossing = q(four, "ac", "bd")
matrix = coefficient_matrix(basis + [crossing])
reduced, pivots = matrix.rref()
relation = Matrix([-reduced[row, 6] for row in range(6)] + [1])
assert pivots == tuple(range(6))
assert tuple(relation) == (-1, -1, -1, -1, 1, 1, 1)
assert matrix * relation == zeros(matrix.rows, 1)
print("Rank:", len(pivots), "| Nullity:", matrix.cols - len(pivots))
print("Relation coefficients:", tuple(relation))
```

## Change of basis in graph gluing

Glue the paths $a-c-b-d$ and $b-a-d-c$ with unit conductances. Their union is $K_4$. Rewrite grade two of $P_1$ using the tetrahedron identity to eliminate $q_{ac|bd}$. First compare the grade-two forms, then both products with $P_2$. The four contributions $1,7,7,1$ give $\tau(K_4)=16$. Check the spanning-tree weight separately from the full graph's Laplacian.

[[en/Polyform Algebra and Combinatorics/Structural identities/Structural Identities and Graph Gluing#Four shared vertices and the tetrahedron identity|Related section of the note]].

```python
P1 = form_exp(q(four, "ac") + q(four, "bc") + q(four, "bd")).value
P2 = form_exp(q(four, "ab") + q(four, "ad") + q(four, "cd")).value
before = grade_part(P1, 2).value
after = (
    2 * q(four, "bcd") + q(four, "acd") + q(four, "abd") + 2 * q(four, "abc")
    - q(four, "ab", "cd") - q(four, "ad", "bc")
)
assert equivalent(before, after).value
rewritten_P1 = P1 - before + after
original_product = form_product(P1, P2).value
rewritten_product = form_product(rewritten_P1, P2).value
assert equivalent(original_product, rewritten_product).value

contributions = tuple(
    spanning_coefficient(form_product(grade_part(P1, k).value, grade_part(P2, 3 - k).value).value).value
    for k in range(4)
)
complete = network(four.labels, tuple((a, b, 1) for a, b in combinations(four.labels, 2)))
assert contributions == (1, 7, 7, 1)
assert spanning_coefficient(rewritten_product).value == spanning_tree_weight(complete).value == 16
print("Grade contributions:", tuple(map(int, contributions)), "| tau(K4) =", sum(contributions))
```

## Supports on five vertices

There are five four-vertex subsets on five vertices. Check both sides of the tetrahedron identity on each subset, leaving the fifth vertex a singleton. Each relation has its own crossing partition, which is absent from the other four. Check this using coefficients of the partition symbols before expansion.

Then compare with the kernel of the expanded coefficient matrix of all $25$ grade-two forms. Its rank is $20$, so the five independent relations account for the whole kernel in this example.

[[en/Polyform Algebra and Combinatorics/Structural identities/Supports of Structural Identities#Four vertices: one relation|Related section of the note]].

```python
supports = tuple(combinations(five.labels, 4))
all_forms = [q(five, triple) for triple in combinations(five.labels, 3)]
relations = []
crossing_terms = []
for a, b, c, d in supports:
    left, right = tetrahedron(five, (a, b, c, d))
    assert equivalent(left, right).value
    relations.append(dict((left - right).terms))
    crossing = q(five, (a, c), (b, d))
    crossing_terms.append(crossing.terms[0][0])
    all_forms.extend((q(five, (a, b), (c, d)), crossing, q(five, (a, d), (b, c))))

# These are coefficients of partition symbols before exterior expansion.
# Each relation has its own crossing partition, so the five relations are independent.
for row, relation in enumerate(relations):
    assert [relation.get(term, 0) for term in crossing_terms] == [int(row == i) for i in range(5)]
matrix = coefficient_matrix(all_forms)
rank = matrix.rank()
assert matrix.cols == 25 and rank == 20 and matrix.cols - rank == len(supports)
print("Four-vertex supports:", ", ".join("".join(support) for support in supports))
print("Forms:", matrix.cols, "| Rank:", rank, "| Independent relations:", matrix.cols - rank)
```
