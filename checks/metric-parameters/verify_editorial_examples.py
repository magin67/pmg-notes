"""Exact independent checks for the 2026-11-08 worked examples and figures.

Run from any directory: python checks/metric-parameters/verify_editorial_examples.py
Requires SymPy. No network or file writes.
"""
from itertools import combinations
import sympy as s

Q = s.Rational


def graph(n, edges):
    lap = s.zeros(n)
    for i, j, weight in edges:
        v = s.zeros(n, 1)
        v[i], v[j] = 1, -1
        lap += weight * v * v.T
    one = s.ones(n, 1)
    green = (lap + one * one.T / n).inv() - one * one.T / n
    resistance = s.Matrix(n, n, lambda i, j: green[i, i] + green[j, j] - 2 * green[i, j])
    v = resistance.inv() * one
    rho = 1 / (2 * sum(v))
    degree = lap.diagonal().T
    current = degree - sum(degree) / n * one
    potential = green * current
    beta = one / n + potential / 2
    kirchhoff = sum(resistance[i, j] for i, j in combinations(range(n), 2))
    total = sum(degree) / 2
    rho_ref = (n - 1) ** 2 / (2 * n * total)
    kf_ref = n * (n - 1) ** 2 / (2 * total)
    return lap, resistance, rho, v / sum(v), potential, beta, kirchhoff, rho_ref, kf_ref


p3 = graph(3, [(0, 1, 1), (1, 2, 1)])
assert p3[1] == s.Matrix([[0, 1, 2], [1, 0, 1], [2, 1, 0]])
assert p3[2] == Q(1, 2)
assert p3[3] == s.Matrix([Q(1, 2), 0, Q(1, 2)])
assert p3[4] == s.Matrix([-1, 2, -1]) / 9
assert p3[5] == s.Matrix([5, 8, 5]) / 18
reference = graph(3, [(i, j, Q(2, 3)) for i, j in combinations(range(3), 2)])
assert reference[2] == p3[7] == Q(1, 3)
assert reference[2] / p3[2] == Q(2, 3)

triangle = graph(3, [(0, 1, 1), (0, 2, 1), (1, 2, 1)])
deleted = graph(2, [(0, 1, 1)])
eliminated = graph(2, [(0, 1, Q(3, 2))])
assert [g[2] for g in [triangle, deleted, eliminated]] == [Q(2, 9), Q(1, 4), Q(1, 6)]
assert triangle[1][0, 1] == eliminated[1][0, 1] == Q(2, 3)
trees = list(combinations([(0, 1), (0, 2), (1, 2)], 2))
t = s.symbols('t')
polynomial = sum(t ** sum(0 in edge for edge in tree) for tree in trees) / 3
assert s.expand(polynomial) == (2*t + t*t) / 3
assert s.diff(polynomial, t).subs(t, 0) == Q(2, 3)
assert s.diff(polynomial, t).subs(t, 1) == Q(4, 3)
assert Q(sum((0, 1) in tree for tree in trees), len(trees)) == Q(2, 3)

edges = [(i, j, 1) for i in range(2) for j in range(2, 5)]
before, after = graph(5, edges), graph(5, edges + [(0, 1, 1)])
for g, expected in [(before, [Q(1, 3), Q(4, 15), Q(4, 5), Q(23, 3), Q(20, 3), Q(20, 23)]),
                    (after, [Q(17, 50), Q(8, 35), Q(80, 119), 7, Q(40, 7), Q(40, 49)])]:
    assert [g[2], g[7], g[7]/g[2], g[6], g[8], g[8]/g[6]] == expected

tail = graph(5, [(0, 1, 1), (0, 2, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)])
assert tail[4] == s.Matrix([3, 3, 3, -2, -7]) / 5
assert tail[5] == s.Matrix([1, 1, 1, 0, -1]) / 2
hidden = graph(4, [(i, 3, 3) for i in range(3)])
assert hidden[1][:3, :3] == triangle[1]
assert sum(1 * triangle[1][i,j] for i,j in combinations(range(3),2)) == 2
assert sum(-hidden[0][i,j] * hidden[1][i,j] for i,j in combinations(range(3),2)) == 0

print('PASS: radius, center, compactness references, vertex removal, tree polynomial, edge addition, degree potential, hidden-center metric.')
