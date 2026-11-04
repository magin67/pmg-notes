"""Exact checks for the PMG note 'Нормы лапласианов подграфов'.

Run from any directory: python checks/metric-parameters/verify_subgraph_norms.py
Requires SymPy. Enumerating trees independently checks the matrix calculations.
"""
from itertools import combinations
import sympy as sp


def laplacian(n, edges):
    result = sp.zeros(n)
    for a, b, weight in edges:
        v = sp.zeros(n, 1)
        v[a], v[b] = -1, 1
        result += sp.Rational(weight) * v * v.T
    return result


def components(n, edges):
    parent = list(range(n))

    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a

    for a, b, *_ in edges:
        a, b = root(a), root(b)
        if a != b:
            parent[a] = b
    return len({root(a) for a in range(n)})


def tree_list(n, edges):
    result = []
    for selected in combinations(edges, n - 1):
        if components(n, selected) == 1:
            result.append((selected, sp.prod(sp.Rational(e[2]) for e in selected)))
    return result


def data(n, edges):
    L = laplacian(n, edges)
    Gr = (L + sp.ones(n) / n).inv() - sp.ones(n) / n
    R = sp.Matrix(n, n, lambda i, j: Gr[i, i] + Gr[j, j] - 2 * Gr[i, j])
    trees = tree_list(n, edges)
    tau = sum(weight for _, weight in trees)
    assert tau == L[:n - 1, :n - 1].det()
    return L, Gr, R, trees, tau


def internal(edges, vertices):
    return [e for e in edges if e[0] in vertices and e[1] in vertices]


def norm(edges, R, vertices):
    return sum(weight * R[a, b] for a, b, weight in internal(edges, vertices))


def check_subsets(name, n, edges):
    L, Gr, R, trees, tau = data(n, edges)
    total = 0
    t = sp.symbols("t")
    for k in range(1, n + 1):
        for vertices in combinations(range(n), k):
            inside = internal(edges, vertices)
            score = norm(edges, R, vertices)
            LS = laplacian(n, inside)
            expected = sum(weight * len(internal(tree, vertices)) for tree, weight in trees) / tau
            assert score == expected == sp.trace(LS * Gr), (name, vertices)
            local_components = components(n, inside) - (n - k)
            assert 0 <= score <= k - local_components
            if len(edges) == n - 1:
                assert score == len(inside) == k - local_components
            if k <= 3:
                varied = L + t * LS
                coeff = varied[:n - 1, :n - 1].det()
                assert sp.diff(coeff, t).subs(t, 0) / tau == score
            if k == 3:
                a, b, c = vertices
                boundary = R[a, b] * R[a, c] - ((R[a, b] + R[a, c] - R[b, c]) / 2)**2
                local_tau = L[a, b] * L[a, c] + L[a, b] * L[b, c] + L[a, c] * L[b, c]
                p_connected = sum(weight for tree, weight in trees
                                  if len(internal(tree, vertices)) == 2) / tau
                assert local_tau * boundary == p_connected
            total += 1
    assert norm(edges, R, range(n)) == n - 1
    # Fixed metric: subset scores split into two internal sums and the cross sum.
    left = set(range(n // 2))
    right = set(range(n)) - left
    cross = sum(w * R[a, b] for a, b, w in edges if (a in left) != (b in left))
    assert norm(edges, R, left) + norm(edges, R, right) + cross == n - 1
    print(name, "subsets:", total)
    return L, Gr, R, trees, tau, total


def check_kron(n, edges):
    L, Gr, R, _, _ = data(n, edges)
    old = list(range(n - 1))
    q = L[n - 1, n - 1]
    reduced = L.extract(old, old) - L.extract(old, [n - 1]) * L.extract([n - 1], old) / q
    m = n - 1
    J = sp.eye(m) - sp.ones(m) / m
    Gr_old = -J * R.extract(old, old) * J / 2
    reconstructed = (Gr_old + sp.ones(m) / m).inv() - sp.ones(m) / m
    assert reduced == reconstructed
    for k in range(1, n):
        for vertices in combinations(old, k):
            before = sum(-reduced[i, j] * R[i, j] for i, j in combinations(vertices, 2))
            after = sum(-L[i, j] * R[i, j] for i, j in combinations(vertices, 2))
            difference = sum(L[i, n - 1] * L[j, n - 1] * R[i, j]
                             for i, j in combinations(vertices, 2)) / q
            assert before - after == difference >= 0


def check_greenian():
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    L, Gr, R, _, tau = data(4, edges)
    signed_edges = [(i, j, -Gr[i, j]) for i, j in combinations(range(4), 2) if Gr[i, j] != 0]
    signed_trees = tree_list(4, signed_edges)
    sigma = sum(weight for _, weight in signed_trees)
    assert sigma == Gr[:3, :3].det() == 1 / (16 * tau)
    exact = {
        (0, 1): (1, sp.Rational(-5, 8)),
        (0, 3): (0, sp.Rational(5, 4)),
        (0, 1, 2): (2, sp.Rational(5, 4)),
        (0, 1, 3): (1, sp.Rational(7, 4)),
        (0, 1, 2, 3): (3, 3),
    }
    t = sp.symbols("t")
    for vertices, expected in exact.items():
        GS = laplacian(4, internal(signed_edges, vertices))
        green_score = sum(w * (L[a, a] + L[b, b] - 2 * L[a, b])
                          for a, b, w in internal(signed_edges, vertices))
        signed_mean = sum(weight * len(internal(tree, vertices))
                          for tree, weight in signed_trees) / sigma
        determinant = (Gr + t * GS)[:3, :3].det()
        derivative = sp.diff(determinant, t).subs(t, 0) / sigma
        assert green_score == sp.trace(GS * L) == signed_mean == derivative
        assert (norm(edges, R, vertices), green_score) == expected
    print("Greenian: signed tree means, cofactor derivatives and five table rows verified")


def main():
    cases = {
        "triangle": (3, [(0, 1, 1), (1, 2, 1), (0, 2, 1)]),
        "square": (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)]),
        "path5": (5, [(i, i + 1, 1) for i in range(4)]),
        "weighted_tree": (5, [(0, 1, 2), (1, 2, 3), (1, 3, 5), (3, 4, 7)]),
        "bowtie": (5, [(0, 1, 1), (0, 2, 1), (1, 2, 1),
                       (0, 3, 1), (0, 4, 1), (3, 4, 1)]),
        "weighted_K4": (4, [(0, 1, 2), (0, 2, 3), (0, 3, 1),
                            (1, 2, 4), (1, 3, 2), (2, 3, 5)]),
        "hidden_star": (4, [(0, 3, 3), (1, 3, 3), (2, 3, 3)]),
        "two_triangles_bridge": (6, [(0, 1, 1), (0, 2, 1), (1, 2, 1),
                                    (3, 4, 1), (3, 5, 1), (4, 5, 1), (2, 3, 1)]),
    }
    stored = {}
    count = 0
    for name, (n, edges) in cases.items():
        stored[name] = check_subsets(name, n, edges)
        count += stored[name][-1]
        if n >= 3:
            check_kron(n, edges)

    edges = cases["path5"][1]
    R = stored["path5"][2]
    for vertices, expected in [((0, 1, 2), (2, 1)),
                               ((0, 1, 3), (1, 2)),
                               ((0, 2, 4), (0, 4))]:
        a, b, c = vertices
        boundary = R[a, b] * R[a, c] - ((R[a, b] + R[a, c] - R[b, c]) / 2)**2
        assert (norm(edges, R, vertices), boundary) == expected
    assert norm(edges, R, (0, 1, 3, 4)) == 2

    edges = cases["bowtie"][1]
    R = stored["bowtie"][2]
    scores = [norm(edges, R, vertices) for vertices in combinations(range(5), 3)]
    assert scores.count(2) == 2
    assert scores.count(sp.Rational(4, 3)) == 4
    assert scores.count(sp.Rational(2, 3)) == 4

    edges = cases["square"][1]
    R = stored["square"][2]
    assert norm(edges, R, (0, 1)) == sp.Rational(3, 4)
    assert norm(edges, R, (0, 2)) == 0
    assert all(norm(edges, R, v) == sp.Rational(3, 2) for v in combinations(range(4), 3))

    edges = cases["two_triangles_bridge"][1]
    R = stored["two_triangles_bridge"][2]
    pairs = list(combinations(range(6), 2))
    assert max(pairs, key=lambda v: norm(edges, R, v)) == (2, 3)
    best = max(norm(edges, R, v) for v in combinations(range(6), 3))
    assert best == 2
    assert all(norm(edges, R, (2, 3, x)) == sp.Rational(5, 3) for x in [0, 1, 4, 5])

    assert stored["triangle"][2] == stored["hidden_star"][2][:3, :3]
    assert norm(cases["hidden_star"][1], stored["hidden_star"][2], (0, 1, 2)) == 0
    # Deleting equal-norm groups in a path can leave a tree or a disconnected forest.
    path7 = [(i, i + 1, 1) for i in range(6)]
    for deleted, expected_trees in [({0, 1, 2}, 1), ({2, 3, 4}, 0)]:
        remaining = sorted(set(range(7)) - deleted)
        index = {v: i for i, v in enumerate(remaining)}
        remaining_edges = [(index[a], index[b], w) for a, b, w in path7
                           if a in index and b in index]
        assert len(tree_list(4, remaining_edges)) == expected_trees

    check_greenian()
    print("PASS:", count, "nonempty subsets; all note tables and Kron identities verified")


if __name__ == "__main__":
    main()

