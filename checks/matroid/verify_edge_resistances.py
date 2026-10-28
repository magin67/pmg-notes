"""Exact checks for the PMG note on edge resistances and random trees.

Run from the repository root:
    python checks/matroid/verify_edge_resistances.py

Only the Python standard library is required. Tree enumeration by connectivity,
grounded cofactors, and the Green matrix are independent calculation routes.
Finite checks supplement the proofs; they do not replace them.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import prod

from verify_forest_power_sums import determinant, greenian, inverse, laplacian


ORDER = 5


def connected(n, edges):
    neighbours = [set() for _ in range(n)]
    for a, b, _ in edges:
        neighbours[a].add(b)
        neighbours[b].add(a)
    seen, stack = {0}, [0]
    while stack:
        for b in neighbours[stack.pop()]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == n


def tree_records(n, edges):
    """A connected subset with n-1 edges is a tree; edge IDs stay distinct."""
    for selected in combinations(range(len(edges)), n - 1):
        chosen = [edges[i] for i in selected]
        if connected(n, chosen):
            yield frozenset(selected), prod((c for _, _, c in chosen), start=Q(1))


def tree_statistics(n, edges):
    records = list(tree_records(n, edges))
    tau = sum((w for _, w in records), Q(0))
    assert tau > 0
    inclusion = [sum((w for selected, w in records if i in selected), Q(0)) / tau
                 for i in range(len(edges))]
    return tau, inclusion, records


def cofactor(n, edges, root=0):
    matrix = laplacian(n, edges)
    keep = [i for i in range(n) if i != root]
    return determinant([[matrix[i][j] for j in keep] for i in keep])


def contract(n, edges, index):
    """Identify the endpoints, delete the contracted edge, and omit loops."""
    a, b, _ = edges[index]
    representatives = [a if v == b else v for v in range(n)]
    labels = {v: i for i, v in enumerate(sorted(set(representatives)))}
    mapped = [labels[v] for v in representatives]
    remaining = [(mapped[u], mapped[v], c) for i, (u, v, c) in enumerate(edges)
                 if i != index and mapped[u] != mapped[v]]
    return n - 1, remaining


def edge_resistances(n, edges):
    gr = greenian(laplacian(n, edges))
    return [gr[a][a] + gr[b][b] - 2 * gr[a][b] for a, b, _ in edges]


def family(edges, inclusion):
    return [sum((eta ** q / c for (_, _, c), eta in zip(edges, inclusion)), Q(0))
            for q in range(1, ORDER + 1)]


def intersection_mean(edges, records, q):
    tau = sum(w for _, w in records)
    expectation = Q(0)
    for chosen in product(records, repeat=q):
        common = set(chosen[0][0]).intersection(*(selected for selected, _ in chosen[1:]))
        value = sum((1 / edges[i][2] for i in common), Q(0))
        expectation += value * prod(w for _, w in chosen) / tau ** q
    return expectation


def check_graph(n, edges):
    tau, eta, records = tree_statistics(n, edges)
    resistance = edge_resistances(n, edges)
    assert eta == [c * r for (_, _, c), r in zip(edges, resistance)]
    assert sum(eta) == n - 1
    assert all(0 < p <= 1 for p in eta)

    matrix = laplacian(n, edges)
    for root in range(n):
        keep = [v for v in range(n) if v != root]
        grounded = [[matrix[i][j] for j in keep] for i in keep]
        assert determinant(grounded) == tau
        inv = inverse(grounded)
        for (a, b, _), r in zip(edges, resistance):
            vector = [Q(v == b) - Q(v == a) for v in keep]
            energy = sum(vector[i] * inv[i][j] * vector[j]
                         for i in range(n - 1) for j in range(n - 1))
            assert energy == r

    bridge_sum = Q(0)
    for index, (_, _, c) in enumerate(edges):
        deleted = edges[:index] + edges[index + 1:]
        deleted_tau = cofactor(n, deleted)
        contracted_n, contracted_edges = contract(n, edges, index)
        contracted_tau = cofactor(contracted_n, contracted_edges)
        assert tau == deleted_tau + c * contracted_tau
        assert eta[index] == c * contracted_tau / tau == 1 - deleted_tau / tau
        assert resistance[index] == contracted_tau / tau
        is_bridge = not connected(n, deleted)
        assert (eta[index] == 1) == is_bridge
        if is_bridge:
            bridge_sum += 1 / c

    h = family(edges, eta)
    assert h[0] == sum(resistance)
    assert all(a >= b >= bridge_sum for a, b in zip(h, h[1:]))
    nonbridge = [p for p in eta if p < 1]
    if nonbridge:
        assert all(a > b for a, b in zip(h, h[1:]))
        for q, value in enumerate(h, 1):
            assert 0 < value - bridge_sum <= max(nonbridge) ** (q - 1) * (h[0] - bridge_sum)
    else:
        assert h == [bridge_sum] * ORDER

    sigma = Q(3, 2)
    scaled = [(a, b, sigma * c) for a, b, c in edges]
    scaled_tau, scaled_eta, _ = tree_statistics(n, scaled)
    assert scaled_tau == sigma ** (n - 1) * tau
    assert scaled_eta == eta
    assert edge_resistances(n, scaled) == [r / sigma for r in resistance]
    assert family(scaled, scaled_eta) == [value / sigma for value in h]

    # One-point attachment of a new edge, checked by enumeration and matrices.
    joined = edges + [(0, n, Q(2))]
    joined_tau, joined_eta, _ = tree_statistics(n + 1, joined)
    assert joined_tau == 2 * tau
    assert joined_eta == eta + [Q(1)]
    assert edge_resistances(n + 1, joined) == resistance + [Q(1, 2)]
    assert family(joined, joined_eta) == [value + Q(1, 2) for value in h]

    # Aggregating parallel conductors preserves the matrix and H2.
    aggregated = {}
    for a, b, c in edges:
        pair = tuple(sorted((a, b)))
        aggregated[pair] = aggregated.get(pair, Q(0)) + c
    merged = [(a, b, c) for (a, b), c in aggregated.items()]
    _, merged_eta, _ = tree_statistics(n, merged)
    assert laplacian(n, merged) == matrix
    assert family(merged, merged_eta)[1] == h[1]
    return tau, eta, resistance, h, records


def cycle(n, weights=None):
    conductances = weights if weights is not None else [Q(1)] * n
    return [(i, (i + 1) % n, Q(conductances[i])) for i in range(n)]


def main():
    cases = {
        "edge": (2, [(0, 1, Q(1))]),
        "parallel12": (2, [(0, 1, Q(1)), (0, 1, Q(2))]),
        "merged3": (2, [(0, 1, Q(3))]),
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
        "triangle123": (3, [(0, 1, Q(1)), (0, 2, Q(2)), (1, 2, Q(3))]),
    }
    weighted_k4 = [(a, b, Q(c)) for (a, b), c in
                   zip(combinations(range(4), 2), (1, 2, 3, 5, 7, 11))]
    for mask in range(64):
        edges = [edge for i, edge in enumerate(weighted_k4) if (mask >> i) & 1]
        if connected(4, edges):
            cases[f"K4_subset_{mask}"] = (4, edges)
    results = {name: check_graph(n, edges) for name, (n, edges) in cases.items()}
    assert len(results) == 52

    assert results["triangle123"][:4] == (
        Q(11), [Q(5, 11), Q(8, 11), Q(9, 11)],
        [Q(5, 11), Q(4, 11), Q(3, 11)],
        [Q(12, 11), Q(84, 121), Q(624, 1331), Q(4860, 14641), Q(39192, 161051)],
    )
    assert results["parallel12"][3][:3] == [Q(2, 3), Q(1, 3), Q(5, 27)]
    assert results["merged3"][3] == [Q(1, 3)] * ORDER
    assert results["tree123"][3] == [Q(11, 6)] * ORDER
    assert results["path4"][3] == results["star4"][3] == [Q(3)] * ORDER
    assert results["C4"][3][1] == Q(9, 4)
    assert results["K4"][3][1] == Q(3, 2)
    for n in (3, 4, 5):
        assert results[f"C{n}"][1] == [Q(n - 1, n)] * n
        assert results[f"C{n}"][3] == [n * Q(n - 1, n) ** q for q in range(1, ORDER + 1)]
    assert results["K4"][3] == [6 * Q(1, 2) ** q for q in range(1, ORDER + 1)]

    # Direct averaging over ordered tuples, without inclusion probabilities.
    intersection_tuples = 0
    for name in ("triangle123", "C3", "parallel12"):
        _, edges = cases[name]
        _, _, _, h, records = results[name]
        for q in (2, 3):
            assert intersection_mean(edges, records, q) == h[q - 1]
            intersection_tuples += len(records) ** q

    # Glue two cyclic parts, not just a pendant bridge, at vertex 0.
    left = cases["triangle123"][1]
    right = cycle(3)
    mapping = [0, 3, 4]
    joined = left + [(mapping[a], mapping[b], c) for a, b, c in right]
    joined_result = check_graph(5, joined)
    left_result, right_result = results["triangle123"], results["C3"]
    assert joined_result[0] == left_result[0] * right_result[0]
    assert joined_result[1] == left_result[1] + right_result[1]
    assert joined_result[2] == left_result[2] + right_result[2]
    assert joined_result[3] == [a + b for a, b in zip(left_result[3], right_result[3])]
    joint_probabilities = {selected: w / joined_result[0] for selected, w in joined_result[4]}
    for t1, w1 in left_result[4]:
        for t2, w2 in right_result[4]:
            union = t1 | frozenset(i + len(left) for i in t2)
            assert joint_probabilities[union] == w1 / left_result[0] * w2 / right_result[0]

    edge_count = sum(len(edges) for _, edges in cases.values()) + len(joined)
    print(f"OK: {len(cases) + 1} connected test graphs; {edge_count} edge instances.")
    print(f"Direct intersection averages: {intersection_tuples} ordered pairs/triples.")
    print("Enumeration, all grounded roots, Green matrices, deletion/contraction,")
    print("Foster, bridges, H1-H5, scaling, one-point gluing, and parallel aggregation agree.")


if __name__ == "__main__":
    main()
