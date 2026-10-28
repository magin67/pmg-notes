"""Reproduce the 70-graph / 215-edge checks of ordinary forest coefficients.

Run: python checks/matroid/verify_forest_coefficients.py
Only the standard library and the two adjacent helper scripts are required.
The three routes are edge-subset enumeration, induced-block cofactors, and
deletion-contraction recursion. Disconnected graphs, isolates, loops and
labelled parallel edges remain present throughout the calculation.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations

from verify_cycle_matroid import components
from verify_forest_power_sums import (
    determinant, determinant_polynomial, forest_coefficients, greenian, laplacian,
)


def trim(coefficients):
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(a, b):
    result = [Q(0)] * max(len(a), len(b))
    for terms in (a, b):
        for i, value in enumerate(terms):
            result[i] += value
    return trim(result)


def contract(n, edges, index):
    a, b, _ = edges[index]
    assert a != b
    representatives = [a if v == b else v for v in range(n)]
    labels = {v: i for i, v in enumerate(sorted(set(representatives)))}
    mapping = [labels[v] for v in representatives]
    return n - 1, tuple((mapping[u], mapping[v], c)
                        for i, (u, v, c) in enumerate(edges) if i != index)


@lru_cache(maxsize=None)
def recursive(n, edges):
    if not edges:
        return (Q(1),)
    a, b, c = edges[0]
    deleted = recursive(n, edges[1:])
    if a == b:
        return deleted
    contracted = recursive(*contract(n, edges, 0))
    return tuple(add(deleted, [Q(0)] + [c * x for x in contracted]))


def partitions(vertices):
    """Each unordered set partition exactly once."""
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for blocks in partitions(rest):
        yield ((first,),) + blocks
        for i, block in enumerate(blocks):
            yield blocks[:i] + ((first,) + block,) + blocks[i + 1:]


def induced_tau(block, edges):
    if len(block) == 1:
        return Q(1)
    labels = {v: i for i, v in enumerate(block)}
    induced = [(labels[a], labels[b], c) for a, b, c in edges
               if a in labels and b in labels]
    matrix = laplacian(len(block), induced)
    return determinant([row[1:] for row in matrix[1:]])


def partition_coefficients(n, edges):
    coefficients = [Q(0)] * n
    for blocks in partitions(list(range(n))):
        weight = Q(1)
        for block in blocks:
            weight *= induced_tau(block, edges)
        coefficients[n - len(blocks)] += weight
    return trim(coefficients)


def check_graph(n, edges):
    f, rooted = forest_coefficients(n, edges)
    f = trim(f)
    rank = n - len(components(n, edges))
    assert len(f) == rank + 1
    assert f == partition_coefficients(n, edges)
    assert f == list(recursive(n, tuple(edges)))
    assert trim(rooted) == determinant_polynomial(laplacian(n, edges))
    reverse = list(reversed(f))
    for i, (a, b, c) in enumerate(edges):
        deleted = edges[:i] + edges[i + 1:]
        f_deleted = trim(forest_coefficients(n, deleted)[0])
        if a == b:
            assert f == f_deleted
            assert reverse == list(reversed(f_deleted))
            continue
        nc, contracted = contract(n, edges, i)
        f_contracted = trim(forest_coefficients(nc, contracted)[0])
        assert len(f_contracted) == rank
        assert f == add(f_deleted, [Q(0)] + [c * x for x in f_contracted])
        reverse_deleted = list(reversed(f_deleted))
        reverse_contracted = list(reversed(f_contracted))
        rank_deleted = n - len(components(n, deleted))
        if rank_deleted == rank - 1:  # A bridge changes the reversal degree.
            assert f_deleted == f_contracted
            assert reverse == add([Q(0)] + reverse_contracted,
                                  [c * x for x in reverse_contracted])
        else:
            assert rank_deleted == rank
            assert reverse == add(reverse_deleted, [c * x for x in reverse_contracted])
    return len(edges)


def main():
    weighted_k4 = [(a, b, Q(c)) for (a, b), c in
                   zip(combinations(range(4), 2), (1, 2, 3, 5, 7, 11))]
    cases = [(4, [edge for i, edge in enumerate(weighted_k4) if mask >> i & 1])
             for mask in range(64)]
    complete = [(a, b, Q(1)) for a, b in combinations(range(4), 2)]
    cases += [
        (4, complete),
        (3, [(0, 1, Q(1)), (0, 2, Q(2)), (1, 2, Q(3))]),
        (4, [(0, 1, Q(1)), (1, 2, Q(1, 2)), (2, 3, Q(3))]),
        (4, [(i, (i + 1) % 4, Q(1)) for i in range(4)]),
        (3, [(0, 1, Q(1)), (0, 1, Q(2)), (1, 2, Q(3)), (2, 0, Q(5))]),
        (3, [(0, 0, Q(7)), (0, 1, Q(2)), (1, 2, Q(3))]),
    ]
    edge_checks = sum(check_graph(n, edges) for n, edges in cases)
    assert len(cases) == 70 and edge_checks == 215
    gr = greenian(laplacian(4, complete))
    canonical = [(a, b, -gr[a][b]) for a, b in combinations(range(4), 2)]
    assert all(c == Q(1, 16) for _, _, c in canonical)
    ordinary, rooted = forest_coefficients(4, canonical)
    assert ordinary == [1, Q(3, 8), Q(15, 256), Q(1, 256)]
    assert rooted == [1, Q(3, 4), Q(3, 16), Q(1, 64)]
    assert rooted == determinant_polynomial(gr)
    print(f"OK: {len(cases)} graphs; {edge_checks} edge recursions in grade and corank.")
    print("OK: enumeration, induced-block cofactors, recursive computation and K4 Greenian.")


if __name__ == "__main__":
    main()
