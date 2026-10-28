"""Exact checks for the PMG note 'Forest resistance scales'.

Run from the repository root:
    python checks/matroid/verify_forest_scales.py

The companion module provides rational matrix operations and an independent
edge-subset enumeration. This file enumerates extension conductances directly.
Only the Python standard library is used. Finite checks are not general proofs.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import comb, prod

from verify_forest_power_sums import (
    determinant_polynomial,
    forest_coefficients,
    greenian,
    laplacian,
    multiply,
    normalized,
)


def forest_records(n, edges):
    """Enumerate forests by grade and their admissible extension weights."""
    for grade in range(n):
        for selected in combinations(range(len(edges)), grade):
            parent = list(range(n))

            def root(a):
                while a != parent[a]:
                    a = parent[a]
                return a

            weight = Q(1)
            for index in selected:
                a, b, c = edges[index]
                ra, rb = root(a), root(b)
                if ra == rb:
                    break
                parent[ra] = rb
                weight *= c
            else:
                components = [root(a) for a in range(n)]
                sizes = Counter(components)
                root_choices = prod(sizes.values())
                extension = Q(0)
                rooted_extension = Q(0)
                for a, b, c in edges:
                    ra, rb = components[a], components[b]
                    if ra != rb:
                        extension += c
                        rooted_extension += c * (Q(1, sizes[ra]) + Q(1, sizes[rb]))
                yield grade, weight, root_choices, extension, rooted_extension


def scales(coefficients):
    """Ratios indexed by corank, starting at k=1."""
    d = len(coefficients) - 1
    return [coefficients[d - k] / coefficients[d - k + 1]
            for k in range(1, d + 1)]


def check_graph(n, edges):
    d = n - 1
    f, rooted = forest_coefficients(n, edges)
    records = list(forest_records(n, edges))
    ordinary_sum = [Q(0)] * n
    rooted_sum = [Q(0)] * n
    extension_sum = [Q(0)] * n
    rooted_extension_sum = [Q(0)] * n
    for g, w, roots, a, ar in records:
        ordinary_sum[g] += w
        rooted_sum[g] += w * roots
        extension_sum[g] += w * a
        rooted_extension_sum[g] += w * roots * ar
        if g < d:
            assert a > 0 and ar > 0
    assert ordinary_sum == f and rooted_sum == rooted

    xi, xi_root = scales(f), scales(rooted)
    total_c = sum(c for _, _, c in edges)
    for k in range(1, n):
        g = d - k
        assert extension_sum[g] == (n - k) * f[g + 1]
        assert rooted_extension_sum[g] == (n - k) * rooted[g + 1]
        assert xi[k - 1] == (n - k) / (extension_sum[g] / f[g])
        assert xi_root[k - 1] == (n - k) / (rooted_extension_sum[g] / rooted[g])
        assert xi[k - 1] >= Q(n - k) / total_c
    assert xi[-1] == 1 / total_c
    assert xi_root[-1] == 1 / (2 * total_c)

    # Verify the normalization and the stronger weighted coefficient inequality.
    assert normalized(f) == [prod(xi[:k]) for k in range(n)]
    assert f[-1] == 1 / prod(xi)
    number_of_edges = len(edges)
    for g in range(1, d):
        factor = Q((g + 1) * (number_of_edges - g + 1),
                   g * (number_of_edges - g))
        assert f[g] ** 2 >= factor * f[g - 1] * f[g + 1]
    assert all(a > b > 0 for a, b in zip(xi, xi[1:]))

    matrix = laplacian(n, edges)
    gr = greenian(matrix)
    p_gr = determinant_polynomial(gr)
    assert determinant_polynomial(matrix) == rooted
    assert p_gr == [x / (n * f[-1]) for x in reversed(rooted)]
    assert [p_gr[k] / p_gr[k - 1] for k in range(1, n)] == xi_root
    assert xi_root[0] == sum(gr[i][i] for i in range(n))

    sigma = Q(3, 2)
    scaled_edges = [(a, b, sigma * c) for a, b, c in edges]
    scaled_f, scaled_rooted = forest_coefficients(n, scaled_edges)
    assert scales(scaled_f) == [x / sigma for x in xi]
    assert scales(scaled_rooted) == [x / sigma for x in xi_root]

    # One-point attachment of an edge of conductance 2.
    glued_f, _ = forest_coefficients(n + 1, edges + [(0, n, Q(2))])
    glued_alpha = multiply(normalized(f), [Q(1), Q(1, 2)])
    assert normalized(glued_f) == glued_alpha
    assert scales(glued_f) == [glued_alpha[k] / glued_alpha[k - 1]
                              for k in range(1, n + 1)]
    assert scales(glued_f)[0] == xi[0] + Q(1, 2)
    return f, xi, xi_root, records, gr


def cycle(n, conductances=None):
    weights = conductances if conductances is not None else [Q(1)] * n
    return [(i, (i + 1) % n, Q(weights[i])) for i in range(n)]


def main():
    cases = {
        "edge": (2, [(0, 1, Q(1))]),
        "parallel_edges": (2, [(0, 1, Q(2)), (0, 1, Q(3))]),
        "tree123": (4, [(i, i + 1, Q(i + 1)) for i in range(3)]),
        "path4": (4, [(i, i + 1, Q(1)) for i in range(3)]),
        "star4": (4, [(0, i, Q(1)) for i in range(1, 4)]),
        "C3": (3, cycle(3)),
        "C4": (4, cycle(4)),
        "C5": (5, cycle(5)),
        "weighted_C4": (4, cycle(4, [Q(1, 2), 2, 3, 5])),
        "K4": (4, [(a, b, Q(1)) for a, b in combinations(range(4), 2)]),
        "parallel_path": (3, [(0, 1, Q(1))] * 3 + [(1, 2, Q(1))] * 3),
        "asymmetric5": (5, [(0, 1, Q(1, 3)), (1, 2, Q(2)), (2, 3, Q(3)),
                             (3, 4, Q(5)), (4, 0, Q(7)), (1, 4, Q(1, 2))]),
    }
    weighted_k4 = [(a, b, Q(c)) for (a, b), c in
                   zip(combinations(range(4), 2), (1, 2, 3, 5, 7, 11))]
    for mask in range(64):
        edges = [edge for i, edge in enumerate(weighted_k4) if (mask >> i) & 1]
        if forest_coefficients(4, edges)[0][-1] > 0:
            cases[f"K4_subset_{mask}"] = (4, edges)
    results = {name: check_graph(n, edges) for name, (n, edges) in cases.items()}
    assert len(results) == 50

    assert results["tree123"][0] == [1, 6, 11, 6]
    assert results["tree123"][1] == [Q(11, 6), Q(6, 11), Q(1, 6)]
    assert results["C3"][1] == [1, Q(1, 3)]
    assert results["K4"][1] == [Q(15, 16), Q(2, 5), Q(1, 6)]
    assert results["K4"][2] == [Q(3, 4), Q(1, 4), Q(1, 12)]
    assert results["path4"][1] == results["star4"][1] == [3, 1, Q(1, 3)]
    assert results["path4"][2][0] == Q(5, 2)
    assert results["star4"][2][0] == Q(9, 4)
    assert -results["path4"][4][0][1] == Q(-1, 8)

    # Check tree formulas for unequal conductances without using alpha.
    q_values = [Q(1), Q(1, 2), Q(1, 3)]
    elementary = [sum(prod(q_values[i] for i in subset)
                      for subset in combinations(range(3), k)) for k in range(4)]
    assert results["tree123"][1] == [elementary[k] / elementary[k - 1]
                                    for k in range(1, 4)]
    for n in (3, 4, 5):
        assert results[f"C{n}"][0] == [Q(comb(n, g)) for g in range(n)]
        assert results[f"C{n}"][1] == [Q(n - k, k + 1) for k in range(1, n)]
    assert results["path4"][1] == [Q(4 - k, k) for k in range(1, 4)]

    # The two kinds of average in the K4 example are distinct.
    two_forests = [r for r in results["K4"][3] if r[0] == 2]
    assert Counter(r[3] for r in two_forests) == {Q(3): 12, Q(4): 3}
    expected_a = sum(w * a for _, w, _, a, _ in two_forests) / 15
    expected_inverse = sum(w / a for _, w, _, a, _ in two_forests) / 15
    assert expected_a == Q(16, 5)
    assert 1 / expected_a == Q(5, 16)
    assert expected_inverse == Q(19, 60)
    assert all(ar == 4 for _, _, _, _, ar in two_forests)

    # Two two-edge trees: xi2 is defined in both parts, but is not additive.
    part_f, _ = forest_coefficients(3, [(0, 1, Q(1)), (1, 2, Q(1))])
    joined_f, _ = forest_coefficients(5, [(0, 1, Q(1)), (1, 2, Q(1)),
                                        (0, 3, Q(1)), (3, 4, Q(1))])
    assert scales(part_f)[1] == Q(1, 2)
    assert scales(joined_f)[1] == Q(3, 2) != 2 * scales(part_f)[1]
    assert normalized(joined_f) == multiply(normalized(part_f), normalized(part_f))

    levels = sum(n - 1 for n, _ in cases.values())
    print(f"OK: {len(cases)} connected test graphs; {levels} corank levels.")
    print("Both extension identities, rooted matrix coefficients, weighted inequalities,")
    print("scaling, one-point attachment, and all displayed examples agree exactly.")


if __name__ == "__main__":
    main()
