---
title: "Example: Combinatorial Potentials"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-combinatorial-potentials
lang: en
description: "Six exact checks for partitions, forests, permutations, and directed states."
order: 11
---

Compute combinatorial potentials for prescribed types and check them by enumeration. The forest examples also use partition forms, contraction, and exact spanning-tree coefficients. These calculations verify selected examples. The series notes give the general proofs.

[[ru/PythonExamples/Пример - Комбинаторные потенциалы|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 990f446](https://github.com/magin67/polyform_algebra/commit/990f4462b17a1afaad25666220ffc1fbc2cd4d26).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/combinatorial-potentials.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/combinatorial-potentials.ipynb)

## Partitions and the second-kind potential

Enumerate the three partitions of $\{a,b,c,d\}$ into two pairs and compare the count with $s_2([2,2])$. For sets of up to five elements, check the formula for each type. Summing over all types gives the Bell number. Summing over types with a fixed block count gives the Stirling number of the second kind.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Partitions and the Combinatorial Potential of the Second Kind#One type and three partitions|Related section of the note]].

```python
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial, perm, prod

from sympy.functions.combinatorial.numbers import bell, stirling
from sympy.utilities.iterables import multiset_partitions

from polyform_algebra.combinatorics import (
    first_kind_potential, path_cycle_potential, second_kind_potential,
)


def block_sizes(blocks):
    return tuple(sorted((len(block) for block in blocks), reverse=True))


four = tuple("abcd")
pairs = [blocks for blocks in multiset_partitions(four, 2)
         if block_sizes(blocks) == (2, 2)]
assert len(pairs) == second_kind_potential((2, 2)) == 3
print("s₂([2,2]) =", len(pairs), "|", [" | ".join(map("".join, p)) for p in pairs])

for n in range(1, 6):
    labels = tuple("abcde"[:n])
    counts = Counter(block_sizes(blocks) for blocks in multiset_partitions(labels))
    assert all(count == second_kind_potential(sizes) for sizes, count in counts.items())
    assert sum(counts.values()) == bell(n)
    for m in range(1, n + 1):
        assert sum(count for sizes, count in counts.items() if len(sizes) == m) == stirling(n, m)
print("B₅ =", bell(5), "| S(5,2) =", stirling(5, 2))
```

## From partitions to forests on five vertices

The entries of type $[2,1]$ are grades. To count partitions of the vertices, use block sizes $[3,2]$. The potential $s_2([2,1])=3$ counts partitions of an auxiliary three-element set. On five vertices there are ten partitions and thirty forests. On the left, sum the products of edge forms for all these forests. On the right, sum the partition forms and multiply by $3$. Compare the coefficients exactly.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Combinatorial Potentials in Symmetric Polyforms#Why there are ten partitions but thirty forests|Related section of the note]].

```python
from functools import reduce

from polyform_algebra.core import (
    Context, Network, contract, equivalent, form_product, network,
    partition_form, spanning_tree_weight,
)


def partition(context, blocks=()):
    return partition_form(context, blocks).value


def complete_graph(labels):
    return network(labels, tuple((a, b, 1) for a, b in combinations(labels, 2)))


def product_of_edges(context, edges):
    return reduce(
        lambda form, edge: form_product(form, partition(context, (edge,))).value,
        edges, partition(context),
    )


five = tuple("abcde")
context = Context(five)
zero = 0 * partition(context)
type_partitions = [
    tuple(map(tuple, blocks)) for blocks in multiset_partitions(five, 2)
    if block_sizes(blocks) == (3, 2)
]
E5_21 = sum((partition(context, blocks) for blocks in type_partitions), start=zero)

forest_edges = []
for edges in combinations(combinations(five, 2), 3):
    forest = Network(context, tuple((a, b, 1) for a, b in edges))
    if block_sizes(forest.components) == (3, 2):
        forest_edges.append(edges)
forest_sum = sum((product_of_edges(context, edges) for edges in forest_edges), start=zero)

assert second_kind_potential((2, 1)) == 3
assert len(type_partitions) == second_kind_potential((3, 2)) == 10
assert len(forest_edges) == 3 * len(type_partitions) == 30
assert equivalent(forest_sum, 3 * E5_21).value
print("s₂([2,1]) = 3 | #E₅[2,1] = 10 | 30 forest terms = 3 E₅[2,1]")
```

## Joining prescribed components

Keep the prescribed edges $ab$ or $ab,cd$ and enumerate the pairs of new edges that complete the forest to a tree. Count adjacent and disjoint new-edge pairs separately. Compare the total with the Cayley–Moon formula and with the spanning-tree coefficient of the complete graph after contracting the prescribed blocks.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Cayley's Theorem and Joining Prescribed Components#Contraction to a weighted graph|Related section of the note]].

```python
def completions(labels, groups):
    complete = complete_graph(labels)
    contracted = contract(complete, groups).value.network
    sizes = tuple(map(len, groups.values()))
    expected = prod(sizes) * len(labels) ** (len(sizes) - 2)
    assert spanning_tree_weight(contracted).value == expected

    # In both examples each original component is a singleton or a fixed edge.
    prescribed = tuple(tuple(block) for block in groups.values() if len(block) == 2)
    candidates = [edge for edge in combinations(labels, 2) if edge not in prescribed]
    distribution = Counter()
    for added in combinations(candidates, len(sizes) - 1):
        tree = Network(complete.context, tuple((a, b, 1) for a, b in prescribed + added))
        if len(tree.components) == 1:
            new_edges = Network(complete.context, tuple((a, b, 1) for a, b in added))
            positive_grades = tuple(size - 1 for size in block_sizes(new_edges.components) if size > 1)
            distribution[positive_grades] += 1
    assert sum(distribution.values()) == expected
    return expected, (distribution[(2,)], distribution[(1, 1)])


assert completions(four, {"A": ("a", "b"), "B": ("c",), "C": ("d",)}) == (8, (6, 2))
assert completions(five, {"A": ("a", "b"), "B": ("c", "d"), "C": ("e",)}) == (20, (12, 8))
print("T([2,1,1]) = 6 + 2 = 8 | T([2,2,1]) = 12 + 8 = 20")
```

## Forest coefficients and Stirling numbers

For each $1\leqslant k\leqslant6$, compute $\operatorname{St}(k,m)$ in three ways. First sum over ordinary block sizes, using Cayley's factor for each block with its added root. Then build a row of $r$-Stirling numbers from $r=k+1$ separate markers, and separately compute a finite difference of the Abel polynomial. Display the rows for $k=3$ and $k=4$.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Falling Factorials, Rooted Forests, and Stirling Numbers#Why forest coefficients are r-Stirling numbers|Related section of the note]].

```python
def restricted_stirling(markers, positions):
    # Start with the markers in separate blocks. Each new position joins
    # one of the existing blocks or forms a new block of its own.
    row = {markers: 1}
    for _ in range(positions):
        next_row = Counter()
        for blocks, count in row.items():
            next_row[blocks] += blocks * count
            next_row[blocks + 1] += count
        row = next_row
    return row


for k in range(1, 7):
    labels = tuple("abcdef"[:k])
    types = {block_sizes(blocks) for blocks in multiset_partitions(labels)}
    row = restricted_stirling(markers=k + 1, positions=k - 1)
    coefficients = []
    for m in range(1, k + 1):
        by_type = sum(second_kind_potential(sizes) * prod((size + 1) ** (size - 1) for size in sizes)
                      for sizes in types if len(sizes) == m)
        difference = sum((-1) ** (m-i) * comb(m, i) * i * (i + k) ** (k - 1)
                         for i in range(m + 1))
        assert by_type == row[k + m]
        assert factorial(m) * by_type == difference
        coefficients.append(by_type)
    if k in (3, 4):
        print(f"St({k}, m) =", tuple(coefficients))
        assert tuple(coefficients) == {3: (16, 9, 1), 4: (125, 91, 18, 1)}[k]
```

## Cycles and the first-kind potential

Enumerate the permutations of four letters and group them by cycle lengths. Check the count against $s_1$ and against $s_2$ multiplied by the number of cyclic orders within the blocks. On five letters, count the permutations with no fixed points separately.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/Cyclic Partitions and the Combinatorial Potential of the First Kind#The potential of a cycle type|Related section of the note]].

```python
def cycle_type(labels, images):
    permutation = dict(zip(labels, images))
    remaining = set(labels)
    lengths = []
    while remaining:
        vertex = min(remaining)
        length = 0
        while vertex in remaining:
            remaining.remove(vertex)
            vertex = permutation[vertex]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


types4 = Counter(cycle_type(four, images) for images in permutations(four))
for sizes, count in sorted(types4.items(), reverse=True):
    assert count == first_kind_potential(sizes)
    assert count == second_kind_potential(sizes) * prod(factorial(size - 1) for size in sizes)
    print(f"s₁{list(sizes)} =", count)
assert sum(types4.values()) == factorial(len(four))

derangements5 = sum(all(a != b for a, b in zip(five, images)) for images in permutations(five))
assert derangements5 == first_kind_potential((5,)) + first_kind_potential((3, 2)) == 44
print("D₅ =", derangements5)
```

## Paths, cycles, and construction histories

First check seven small state types. For a two-cycle and a separate open arc, enumerate how the three arc labels can be assigned to components. Then on vertices $a,b,c$, enumerate directed two-arc paths and every order of adding their arcs. The checks distinguish the potential $u=2$, the graph count $N_3=6$, and the history count $H_3=12$.

[[en/Polyform Algebra and Combinatorics/Combinatorial potentials/The Potential of Path-and-Cycle States#Graphs on prescribed vertices and construction histories|Related section of the note]].

```python
examples = (
    ((1, 1), (), 1), ((1,), (1,), 2), ((2,), (), 1), ((), (2,), 2),
    ((), (1, 1), 1), ((2,), (1,), 3), ((1,), (2,), 6),
)
assert all(path_cycle_potential(cycles, paths) == count for cycles, paths, count in examples)
arc_labels = tuple("ijk")
mixed_arc_types = {
    (tuple(sorted(cycle)), path) for *cycle, path in permutations(arc_labels)
}
assert len(mixed_arc_types) == path_cycle_potential((2,), (1,)) == 3

vertices = tuple("abc")
directed_paths = {((a, b), (b, c)) for a, b, c in permutations(vertices)}
histories = {history for edges in directed_paths for history in permutations(edges)}
u = path_cycle_potential(path_lengths=(2,))
assert len(histories) == u * perm(len(vertices), 3) == 12
assert len(directed_paths) == len(histories) // factorial(2) == 6
print("u([2, open 1]) = 3 | two-arc path: u = 2, N₃ = 6, H₃ = 12")
```
