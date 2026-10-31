"""Exact rational checks for the constrained search note (standard library).

Independent forest enumeration checks the adjugate formula. Multiaffinity of
tree/forest polynomials yields exact derivatives without finite differences.
The general CAD algorithm is not implemented by this example checker.
"""

from fractions import Fraction as Q
from itertools import combinations
import json

from verify_single_edge import determinant, inverse, forest_sums
from verify_one_greenian_coefficient import laplacian, principal, centered_inverse
from verify_one_resistance import resistance
from verify_constrained_couplings import vector, construct, V, FIXED, Z, target


def bilinear(a, matrix, b):
    return sum(a[i]*matrix[i][j]*b[j] for i in range(len(a)) for j in range(len(b)))


def adjugate(matrix):
    n = len(matrix)
    return [[(-1)**(i+j) * determinant([
        [matrix[r][c] for c in range(n) if c != i]
        for r in range(n) if r != j]) for j in range(n)] for i in range(n)]


def check_graph(n, weights):
    weights = {e: Q(c) for e, c in weights.items()}
    matrix = principal(laplacian(n, weights))
    tau = determinant(matrix)
    adj = adjugate(matrix)
    tree_sum, forests = forest_sums(n, weights)
    assert tau == tree_sum > 0
    ri = resistance(centered_inverse(laplacian(n, weights)))
    pairs = list(combinations(range(n), 2))
    inv = inverse(matrix)
    for pair in pairs:
        v = vector(n, pair)[:-1]
        f = bilinear(v, adj, v)
        assert f == forests[pair]
        assert f/tau == ri[pair[0]][pair[1]] == bilinear(v, inv, v)
    derivatives = 0
    for edge in weights:
        incremented = dict(weights)
        incremented[edge] += 1
        tau_next, f_next = forest_sums(n, incremented)
        tau_d = tau_next-tau
        for pair in pairs:
            f_d = f_next[pair]-forests[pair]
            derivative = (f_d*tau-forests[pair]*tau_d)/(tau*tau)
            transfer = bilinear(vector(n, edge)[:-1], inv, vector(n, pair)[:-1])
            assert derivative == -transfer*transfer
            derivatives += 1
    # Verify the common polynomial denominator of a nonzero weighted residual.
    desired = {pair: Q(i+2, i+3) for i, pair in enumerate(pairs)}
    w = {pair: Q(i+1, i+2) for i, pair in enumerate(pairs)}
    h = sum(w[pair]*(forests[pair]-desired[pair]*tau)**2 for pair in pairs)
    psi = sum(w[pair]*(ri[pair[0]][pair[1]]-desired[pair])**2 for pair in pairs)/2
    assert h == 2*psi*tau*tau
    for eta in (psi/2, psi, psi+1):
        assert (h <= 2*eta*tau*tau) == (psi <= eta)
    return len(pairs), derivatives


def check_path():
    for x in (Q(1, 10), Q(1, 2), Q(1), Q(2), Q(3), Q(1000)):
        matrix = principal(laplacian(3, {(0, 1): Q(1), (1, 2): x}))
        v = vector(3, (0, 2))[:-1]
        tau = determinant(matrix)
        f = bilinear(v, adjugate(matrix), v)
        assert tau == x and f == x+1
        assert f-tau == 1  # Target 1 is impossible at every finite x.
        assert (f-2*tau == 0) == (x == 1)
        psi = (f/tau-1)**2/2
        assert psi == 1/(2*x*x)
        if x <= 2:
            # Certificate on 0 < x <= 2: Psi-1/8 = (2-x)(2+x)/(8x^2).
            assert psi-Q(1, 8) == (2-x)*(2+x)/(8*x*x) >= 0
    for eta in (Q(1), Q(1, 2), Q(1, 100), Q(1, 10000)):
        # Explicit finite witness for every positive rational objective level.
        x = max(Q(1), 1/eta)
        assert 1/(2*x*x) <= eta
    disconnected = principal(laplacian(3, {(0, 1): Q(1)}))
    assert determinant(disconnected) == 0
    # Clearing denominators without tau > 0 can admit a disconnected graph:
    # on four vertices with only edge 12, every 3-by-3 cofactor vanishes.
    bad = principal(laplacian(4, {(0, 1): Q(1)}))
    assert determinant(bad) == 0 and adjugate(bad) == [[0]*3 for _ in range(3)]


def check_prism():
    results = []
    for k, g in ((Q(21, 20), Q(2)), (Q(9, 8), Q(7))):
        weights = construct(k, g)
        assert min(weights.values()) >= 0
        assert all(weights.get(e, 0) == 0 for e in Z)
        assert all(weights[e] == 1 for e in FIXED)
        ri = resistance(centered_inverse(laplacian(6, weights)))
        assert [[ri[i][j] for j in range(3)] for i in range(3)] == target(k)
        results.append({"k": str(k), "conductances": [str(weights[e]) for e in V]})
    assert construct(Q(9, 8), Q(7))[(3, 4)] == 0
    # For k = 2, target boundary conductance 12 is zero, below the fixed 1.
    k = Q(2)
    assert 15*(2-k)/(4*k*(4-k)) == 0
    return results


def main():
    graphs = [
        (2, {(0, 1): Q(3, 2)}),
        (3, {(0, 1): Q(2), (0, 2): Q(1, 3), (1, 2): Q(4, 5)}),
        (4, {(0, 1): Q(1), (1, 2): Q(2), (2, 3): Q(3)}),
        (4, {(0, 1): Q(1), (1, 2): Q(2), (2, 3): Q(3), (0, 3): Q(4)}),
        (6, construct(Q(9, 8), Q(7)))
    ]
    counts = [check_graph(n, weights) for n, weights in graphs]
    check_path()
    witnesses = check_prism()
    print(json.dumps(dict(graphs=len(graphs), forest_pair_checks=sum(c[0] for c in counts),
        exact_derivative_checks=sum(c[1] for c in counts), prism_witnesses=witnesses), indent=2))


if __name__ == "__main__":
    main()
