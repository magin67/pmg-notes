"""Exact independent checks for the PMG forest formula for resistance radius.

Run: python checks/matroid/verify_resistance_radius.py
Only the standard library and the adjacent exact-matrix module are required.
Enumerated rooted forests, minors, Green matrices and inverse resistance
matrices are compared. Finite checks are not substitutes for the proofs.
"""

from fractions import Fraction as Q
from itertools import combinations
from math import prod

from verify_forest_power_sums import determinant, greenian, inverse, laplacian


def components(n, edges):
    neighbours = [set() for _ in range(n)]
    for a, b, _ in edges:
        neighbours[a].add(b)
        neighbours[b].add(a)
    unseen, groups = set(range(n)), []
    while unseen:
        start = min(unseen)
        group, todo = {start}, [start]
        unseen.remove(start)
        while todo:
            for b in neighbours[todo.pop()]:
                if b in unseen:
                    unseen.remove(b)
                    group.add(b)
                    todo.append(b)
        groups.append(group)
    return groups


def forests(n, edges):
    """Connectivity enumeration; edge IDs are kept even when endpoints agree."""
    for mask in range(1 << len(edges)):
        selected = [edge for i, edge in enumerate(edges) if (mask >> i) & 1]
        groups = components(n, selected)
        if len(selected) != n - len(groups):
            continue
        labels = [next(j for j, group in enumerate(groups) if v in group) for v in range(n)]
        yield selected, labels, prod((c for _, _, c in selected), start=Q(1))


def minor(matrix, removed):
    keep = [i for i in range(len(matrix)) if i not in removed]
    return [[matrix[i][j] for j in keep] for i in keep]


def geometry(n, edges):
    l = laplacian(n, edges)
    gr = greenian(l)
    r = [[gr[i][i] + gr[j][j] - 2 * gr[i][j] for j in range(n)] for i in range(n)]
    inv_r = inverse(r)
    rho = 1 / (2 * sum(sum(row) for row in inv_r))
    return l, gr, r, rho


def check_graph(n, edges):
    records = list(forests(n, edges))
    coefficients = [sum((w for selected, _, w in records if len(selected) == g), Q(0))
                    for g in range(n)]
    tau = coefficients[-1]
    assert tau > 0
    two = [(selected, labels, w) for selected, labels, w in records if len(selected) == n - 2]
    three = [(selected, labels, w) for selected, labels, w in records if len(selected) == n - 3]
    l, gr, r, rho = geometry(n, edges)
    xi = coefficients[-2] / tau
    h2 = sum(c * r[a][b] ** 2 for a, b, c in edges)
    assert rho == xi / 3 - h2 / 12 > 0
    assert h2 < 4 * xi

    for q in range(n):
        keep = [i for i in range(n) if i != q]
        a = minor(l, {q})
        assert determinant(a) == tau
        gram = inverse(a)
        rs = [r[i][q] for i in range(n)]
        z2 = [sum((w for _, labels, w in two if labels[i] != labels[q]), Q(0))
              for i in range(n)]
        assert z2 == [tau * value for value in rs]
        for i in keep:
            assert determinant(minor(l, {q, i})) == z2[i]
            for j in keep:
                assert gram[keep.index(i)][keep.index(j)] == (rs[i] + rs[j] - r[i][j]) / 2
        removal_sum = Q(0)
        for i, j, c in edges:
            z3 = sum((w for _, labels, w in three
                      if len({labels[i], labels[j], labels[q]}) == 3), Q(0))
            gij = (rs[i] + rs[j] - r[i][j]) / 2
            assert z3 / tau == rs[i] * rs[j] - gij ** 2
            if q not in (i, j):
                assert determinant(minor(l, {q, i, j})) == z3
            else:
                assert z3 == 0
            removal_sum += c * z3
        assert coefficients[-2] == sum(z2) - removal_sum

        # Check the per-forest Euler count, without any determinant identity.
        vertex_count, edge_count = Q(0), Q(0)
        for selected, labels, weight in two:
            b = {i for i in range(n) if labels[i] != labels[q]}
            b_edges = sum(u in b and v in b for u, v, _ in selected)
            assert len(b) - b_edges == 1
            vertex_count += len(b) * weight
            edge_count += b_edges * weight
        assert vertex_count == sum(z2) and edge_count == removal_sum

        energy = sum(c * (rs[i] - rs[j]) ** 2 for i, j, c in edges)
        assert energy == 4 * rho
        incident_sum = [sum(c * r[i][j] for i, j, c in edges if v in (i, j))
                        for v in range(n)]
        lr = [sum(l[i][j] * rs[j] for j in range(n)) for i in range(n)]
        assert all(incident_sum[i] == 2 - lr[i] for i in keep)
        mixed = sum(c * r[i][j] * (rs[i] + rs[j]) for i, j, c in edges)
        assert mixed == 2 * sum(rs) - energy

        # Independent cofactor extraction of the rank-one potential in exp(Gr).
        mean = sum(rs) / n
        centered = [value - mean for value in rs]
        shifted = [[gr[i][j] + centered[i] * centered[j] for j in range(n)] for i in range(n)]
        potential = determinant(minor(shifted, {q})) / determinant(minor(gr, {q})) - 1
        assert potential == energy

    sigma = Q(3, 2)
    scaled = [(a, b, c * sigma) for a, b, c in edges]
    assert geometry(n, scaled)[3] == rho / sigma
    joined = edges + [(0, n, Q(2))]
    assert geometry(n + 1, joined)[3] == rho + Q(1, 8)
    merged = {}
    for a, b, c in edges:
        key = tuple(sorted((a, b)))
        merged[key] = merged.get(key, Q(0)) + c
    assert geometry(n, [(a, b, c) for (a, b), c in merged.items()])[3] == rho
    return xi, h2, rho


def cycle(n, weights=None):
    weights = weights if weights is not None else [Q(1)] * n
    return [(i, (i + 1) % n, Q(weights[i])) for i in range(n)]


def main():
    cases = {
        "edge2": (2, [(0, 1, Q(2))]),
        "parallel12": (2, [(0, 1, Q(1)), (0, 1, Q(2))]),
        "tree123": (4, [(i, i + 1, Q(i + 1)) for i in range(3)]),
        "P4": (4, [(i, i + 1, Q(1)) for i in range(3)]),
        "star4": (4, [(0, i, Q(1)) for i in range(1, 4)]),
        "C3": (3, cycle(3)),
        "C4": (4, cycle(4)),
        "C5": (5, cycle(5)),
        "C6": (6, cycle(6)),
        "weighted_C4": (4, cycle(4, [Q(1, 2), 2, 3, 5])),
        "K4": (4, [(i, j, Q(1)) for i, j in combinations(range(4), 2)]),
        "K5": (5, [(i, j, Q(1)) for i, j in combinations(range(5), 2)]),
        "triangle123": (3, [(0, 1, Q(1)), (0, 2, Q(2)), (1, 2, Q(3))]),
        "asymmetric5": (5, [(0, 1, Q(1, 3)), (1, 2, Q(2)), (2, 3, Q(3)),
                             (3, 4, Q(5)), (4, 0, Q(7)), (1, 4, Q(1, 2))]),
        "parallel_path": (3, [(0, 1, Q(1))] * 3 + [(1, 2, Q(1))] * 3),
    }
    weighted_k4 = [(i, j, Q(c)) for (i, j), c in
                   zip(combinations(range(4), 2), (1, 2, 3, 5, 7, 11))]
    for mask in range(64):
        edges = [e for i, e in enumerate(weighted_k4) if (mask >> i) & 1]
        if len(components(4, edges)) == 1:
            cases[f"K4_subset_{mask}"] = (4, edges)
    left = cases["triangle123"][1]
    mapping = [0, 3, 4]
    joined = left + [(mapping[i], mapping[j], c) for i, j, c in cycle(3)]
    cases["two_triangles"] = (5, joined)
    results = {name: check_graph(n, edges) for name, (n, edges) in cases.items()}
    assert len(results) == 54

    assert results["P4"] == results["star4"] == (Q(3), Q(3), Q(3, 4))
    assert results["C4"] == (Q(3, 2), Q(9, 4), Q(5, 16))
    assert results["K4"] == (Q(15, 16), Q(3, 2), Q(3, 16))
    assert results["triangle123"] == (Q(6, 11), Q(84, 121), Q(15, 121))
    assert results["tree123"][2] == Q(11, 24)
    assert results["edge2"][2] == Q(1, 8)
    assert results["parallel12"][2] == Q(1, 12)
    assert results["two_triangles"] == tuple(a + b for a, b in
                                            zip(results["triangle123"], results["C3"]))
    for n in range(3, 7):
        assert results[f"C{n}"][2] == Q(n * n - 1, 12 * n)
    for n in (4, 5):
        assert results[f"K{n}"] == (Q((n - 1) * (n + 6), 2 * n * n),
                                   Q(2 * (n - 1), n), Q(n - 1, n * n))
    print(f"OK: {len(cases)} connected graphs; {sum(n for n, _ in cases.values())} root choices.")
    print("Rooted forest sums, minors, Euler counts, both proof cancellations,")
    print("inverse-R radius, energy, Greenian potentials, scaling and gluing agree.")


if __name__ == "__main__":
    main()
