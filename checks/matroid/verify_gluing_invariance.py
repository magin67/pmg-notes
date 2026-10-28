"""Exact checks for gluing, Whitney twists and boundary-dependent forests.

Run: python checks/matroid/verify_gluing_invariance.py
Only the standard library and the adjacent exact-matrix helpers are used.
Subset masks keep individual edge identities, including parallel edges.
"""

from fractions import Fraction as Q
from itertools import product

from verify_forest_power_sums import determinant, multiply, newton, normalized
from verify_resistance_radius import geometry, minor


def records(graph):
    n, edges = graph
    result = {}
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        weight, grade = Q(1), 0
        for k, (a, b, c) in enumerate(edges):
            if not (mask >> k) & 1:
                continue
            ra, rb = root(a), root(b)
            if ra == rb:
                break
            parent[ra] = rb
            weight *= c
            grade += 1
        else:
            result[mask] = (grade, tuple(root(v) for v in range(n)), weight)
    return result


def states(graph, boundary):
    n, _ = graph
    a, b = boundary
    connected, separated = [Q(0)] * n, [Q(0)] * n
    for grade, labels, weight in records(graph).values():
        target = connected if labels[a] == labels[b] else separated
        target[grade] += weight
    return connected, separated


def statistics(graph):
    n, edges = graph
    rec = records(graph)
    f = [sum(w for g, _, w in rec.values() if g == grade) for grade in range(n)]
    tau = f[-1]
    assert tau > 0
    trees = {mask: w for mask, (g, _, w) in rec.items() if g == n - 1}
    eta = [sum(w for mask, w in trees.items() if (mask >> k) & 1) / tau
           for k in range(len(edges))]
    l, gr, r, rho = geometry(n, edges)
    assert determinant(minor(l, {0})) == tau
    assert eta == [c * r[a][b] for a, b, c in edges]
    h = [sum(p ** q / edge[2] for p, edge in zip(eta, edges)) for q in range(1, 5)]
    assert rho == f[-2] / (3 * tau) - h[1] / 12
    tr_gr = sum(gr[i][i] for i in range(n))
    kf = sum(r[i][j] for i in range(n) for j in range(i + 1, n))
    assert kf == n * tr_gr
    return dict(masks=set(rec), f=f, tau=tau, eta=eta, h=h, rho=rho, r=r,
                powers=newton(normalized(f), 4), tr_gr=tr_gr, kf=kf,
                tr_l2=sum(l[i][j] * l[j][i] for i in range(n) for j in range(n)))


def glue(left, right, pairs):
    """Identify vertices only; edges remain distinct and retain their weights."""
    n, le = left
    m, re = right
    mapping = {b: a for a, b in pairs}
    assert len(mapping) == len(pairs) == len({a for a, _ in pairs})
    size = n
    for b in range(m):
        if b not in mapping:
            mapping[b] = size
            size += 1
    return size, le + [(mapping[a], mapping[b], c) for a, b, c in re]


def graph(n, pairs, weights=None):
    weights = [1] * len(pairs) if weights is None else weights
    return n, [(a, b, Q(c)) for (a, b), c in zip(pairs, weights)]


def check_two(left, right):
    a, b = 0, left[0] - 1
    c, d = 0, right[0] - 1
    normal = statistics(glue(left, right, [(a, c), (b, d)]))
    twisted = statistics(glue(left, right, [(a, d), (b, c)]))
    for key in ("masks", "f", "tau", "eta", "h", "rho", "powers"):
        assert normal[key] == twisted[key], key
    ca, sa = states(left, (a, b))
    cb, sb = states(right, (c, d))
    terms = [multiply(ca, sb), multiply(sa, cb), multiply(sa, sb)]
    predicted = [sum(values) for values in zip(*terms)]
    assert predicted[-1] == 0
    assert normal["f"] == predicted[:-1]
    ls, rs = statistics(left), statistics(right)
    assert normal["tau"] == ls["tau"] * sb[-2] + sa[-2] * rs["tau"]
    assert normal["tau"] == ls["tau"] * rs["tau"] * (ls["r"][a][b] + rs["r"][c][d])


def check_one(left, right):
    first = statistics(glue(left, right, [(0, 0)]))
    moved = statistics(glue(left, right, [(left[0] - 1, right[0] - 1)]))
    for key in ("masks", "f", "eta", "h", "rho", "powers"):
        assert first[key] == moved[key], key
    ls, rs = statistics(left), statistics(right)
    assert first["f"] == multiply(ls["f"], rs["f"])
    assert normalized(first["f"]) == multiply(normalized(ls["f"]), normalized(rs["f"]))
    assert first["tau"] == ls["tau"] * rs["tau"]
    assert first["rho"] == ls["rho"] + rs["rho"]
    assert first["h"] == [a + b for a, b in zip(ls["h"], rs["h"])]
    assert first["powers"] == [a + b for a, b in zip(ls["powers"], rs["powers"])]


def illustrated_examples():
    # a=0, b=1, x=2, y=3, p=4, q=5; the order is the edge identity.
    straight = graph(6, [(0, 2), (2, 1), (0, 4), (0, 3), (3, 1), (0, 5)])
    twist = graph(6, [(0, 2), (2, 1), (0, 4), (1, 3), (3, 0), (1, 5)])
    ss, st = statistics(straight), statistics(twist)
    assert ss["masks"] == st["masks"]
    assert ss["f"] == st["f"] == [1, 6, 15, 20, 14, 4]
    assert ss["h"][1] == st["h"][1] == Q(17, 4)
    assert ss["rho"] == st["rho"] == Q(13, 16)
    assert (ss["r"][4][5], st["r"][4][5]) == (2, 3)
    assert (ss["kf"], st["kf"]) == (20, 21)
    assert (ss["tr_l2"], st["tr_l2"]) == (42, 40)
    assert (ss["tr_gr"], st["tr_gr"]) == (Q(10, 3), Q(7, 2))
    distributions = []
    for example in (straight, twist):
        by_type = {}
        for grade, labels, weight in records(example).values():
            if grade == 4:
                sizes = tuple(sorted(labels.count(label) for label in set(labels)))
                by_type[sizes] = by_type.get(sizes, Q(0)) + weight
        distributions.append([by_type[key] for key in ((1, 5), (2, 4), (3, 3))])
    assert distributions == [[11, 2, 1], [10, 2, 2]]

    p3 = graph(3, [(0, 1), (1, 2)])
    p4 = graph(4, [(0, 1), (1, 2), (2, 3)])
    cycle = statistics(glue(p3, p4, [(0, 0), (2, 3)]))
    tailed = statistics(glue(p3, p4, [(0, 0), (2, 2)]))
    assert cycle["f"] == [1, 5, 10, 10, 5]
    assert tailed["f"] == [1, 5, 10, 10, 4]
    assert (cycle["rho"], tailed["rho"]) == (Q(2, 5), Q(9, 16))
    assert states(p4, (0, 3))[0] == [0, 0, 0, 1]
    assert states(p4, (0, 2))[0] == [0, 0, 1, 1]

    # Two triangles, three different policies for their marked edge ab.
    boundary_edges = [(0, 2), (2, 1), (0, 3), (3, 1)]
    assert [statistics(graph(4, boundary_edges + [(0, 1)] * k))["tau"]
            for k in (0, 1, 2)] == [4, 8, 12]
    print("Illustrations: Whitney rho=13/16, Kf=20/21; boundary choice tau=5/4,")
    print("rho=2/5 or 9/16; shared-edge policies tau=4/8/12.")


def main():
    pieces = [
        graph(2, [(0, 1)], [Q(1, 2)]),
        graph(2, [(0, 1), (0, 1)], [1, 3]),
        graph(3, [(0, 1), (1, 2), (2, 0)], [1, 2, 3]),
        graph(4, [(0, 1), (1, 2), (2, 3)], [Q(1, 3), 2, 5]),
        graph(4, [(0, 1), (0, 2), (0, 3)], [1, Q(3, 2), 7]),
        graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)], [2, 3, 5, 7]),
        graph(4, [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)], [1, 2, 3, 5, 7]),
    ]
    for left, right in product(pieces, repeat=2):
        check_one(left, right)
        check_two(left, right)
    illustrated_examples()
    print("OK: 49 one-point comparisons and 49 Whitney-twist comparisons.")
    print("All independent edge sets, weighted forest polynomials, boundary states,")
    print("tree marginals, power sums, H_1..H_4 and independent matrix radii agree.")


if __name__ == "__main__":
    main()
