"""Exact checks for cycle matroids and the two forest representations.

Run: python checks/matroid/verify_cycle_matroid.py
Only the standard library and the adjacent verify_forest_power_sums.py are used.
Enumeration, exterior coordinates, matrix inversion and centered 2-forest sums
are separate routes. Finite checks do not replace the proofs in the note.
"""

from fractions import Fraction as Q
from itertools import combinations

from verify_forest_power_sums import (
    determinant, determinant_polynomial, forest_coefficients,
    greenian, laplacian,
)


def components(n, edges):
    """Connected components, including isolated vertices; cycles are allowed."""
    parent = list(range(n))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for a, b, _ in edges:
        parent[root(a)] = root(b)
    blocks = {}
    for v in range(n):
        blocks.setdefault(root(v), []).append(v)
    return list(blocks.values())


def forests(n, edges):
    """Yield (edge mask, component blocks, weight) for ordinary forests."""
    for mask in range(1 << len(edges)):
        selected = [edge for i, edge in enumerate(edges) if mask >> i & 1]
        blocks = components(n, selected)
        if len(selected) != n - len(blocks):
            continue
        weight = Q(1)
        for _, _, conductance in selected:
            weight *= conductance
        yield mask, blocks, weight


def exterior_nonzero(n, edges, mask):
    """Exterior coordinates are all maximal minors of the incidence columns."""
    selected = [edge for i, edge in enumerate(edges) if mask >> i & 1]
    grade = len(selected)
    if grade > n:
        return False
    columns = [[Q(v == b) - Q(v == a) for v in range(n)]
               for a, b, _ in selected]
    return any(determinant([[column[v] for column in columns] for v in rows])
               for rows in combinations(range(n), grade))


def check_graph(n, edges):
    records = list(forests(n, edges))
    independent = {mask for mask, _, _ in records}
    assert 0 in independent
    for mask in range(1 << len(edges)):
        assert exterior_nonzero(n, edges, mask) == (mask in independent)
    for smaller in independent:
        # Deletion of each individual element implies full heredity.
        assert all(smaller ^ (1 << i) in independent
                   for i in range(len(edges)) if smaller >> i & 1)
        for larger in independent:
            if smaller.bit_count() < larger.bit_count():
                assert any(smaller | (1 << i) in independent
                           for i in range(len(edges))
                           if larger >> i & 1 and not smaller >> i & 1)

    f, rooted = forest_coefficients(n, edges)
    assert [sum(w for mask, _, w in records if mask.bit_count() == g)
            for g in range(n)] == f
    tau = f[-1]
    assert tau > 0
    matrix = laplacian(n, edges)
    gr = greenian(matrix)
    forest_gr = [[Q(0) for _ in range(n)] for _ in range(n)]
    for _, blocks, weight in records:
        if len(blocks) == 2:
            block = blocks[0]
            centered = [Q(v in block) - Q(len(block), n) for v in range(n)]
            for i in range(n):
                for j in range(n):
                    forest_gr[i][j] += weight * centered[i] * centered[j] / tau
    assert forest_gr == gr

    for e, (a, b, c) in enumerate(edges):
        probability = sum(w for mask, blocks, w in records
                          if len(blocks) == 1 and mask >> e & 1) / tau
        resistance = gr[a][a] + gr[b][b] - 2 * gr[a][b]
        assert probability == c * resistance

    canonical = [(i, j, -gr[i][j]) for i, j in combinations(range(n), 2)]
    _, rooted_gr = forest_coefficients(n, canonical)
    assert determinant_polynomial(matrix) == rooted
    assert determinant_polynomial(gr) == rooted_gr
    assert rooted_gr == [x / (n * tau) for x in reversed(rooted)]
    return len(records)


def main():
    cases = {
        "P4": (4, [(i, i + 1, Q(1)) for i in range(3)]),
        "star": (4, [(0, i, Q(1)) for i in range(1, 4)]),
        "C4": (4, [(i, (i + 1) % 4, Q(1)) for i in range(4)]),
        "K4": (4, [(a, b, Q(1)) for a, b in combinations(range(4), 2)]),
        "triangle_123": (3, [(0, 1, Q(1)), (0, 2, Q(2)), (1, 2, Q(3))]),
        "path_fractional": (4, [(0, 1, Q(1)), (1, 2, Q(1, 2)), (2, 3, Q(3))]),
    }
    count = sum(check_graph(n, edges) for n, edges in cases.values())
    print(f"OK: {len(cases)} graphs; {count} forests; matroid axioms and exterior minors.")
    print("OK: centered 2-forest Green matrices, edge probabilities and rooted reversal.")


if __name__ == "__main__":
    main()
