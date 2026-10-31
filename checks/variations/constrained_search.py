"""Small NumPy demonstration of constrained conductance search.

Vertices are zero based. All pairs outside fixed and variable stay zero.
The inner convex quadratic is solved by enumerating active bounds, so this
implementation is intended only for a few variables. No return status proves
infeasibility or global optimality. Run this file for path and prism examples.
"""

from itertools import product
import json

import numpy as np


def incidence(n, edges):
    result = np.zeros((n - 1, len(edges)))
    for column, (i, j) in enumerate(edges):
        if i < n - 1:
            result[i, column] = -1
        if j < n - 1:
            result[j, column] = 1
    return result


def bound_quadratic(hessian, rhs, lower, upper):
    """Find a KKT point of a strictly convex small bound quadratic."""
    choices = [(-1, 0, 1) if np.isfinite(u) else (-1, 0) for u in upper]
    for state in product(*choices):
        state = np.array(state)
        free = state == 0
        fixed = ~free
        step = np.zeros(len(rhs))
        step[state == -1] = lower[state == -1]
        step[state == 1] = upper[state == 1]
        if free.any():
            step[free] = np.linalg.solve(hessian[np.ix_(free, free)],
                rhs[free] - hessian[np.ix_(free, fixed)] @ step[fixed])
        if np.any(step < lower - 1e-12) or np.any(step > upper + 1e-12):
            continue
        gradient = hessian @ step - rhs
        tolerance = 1e-12 * (1 + np.max(np.abs(rhs)))
        if np.any(gradient[state == -1] < -tolerance):
            continue
        if np.any(gradient[state == 1] > tolerance):
            continue
        return np.clip(step, lower, upper)
    raise ArithmeticError("Inner quadratic did not meet the KKT tolerance")


def search(n, fixed, variable, pairs, target, initial, *, lower=None,
           upper=None, weights=None, damping=1e-5, residual_tol=1e-10,
           stationarity_tol=1e-12, max_iterations=400):
    """Return a numerical candidate; retain zeros and check connectivity.

    Fixed weights and variable edges must be disjoint, undirected pairs with
    i < j. Equal bounds should be moved to fixed before calling this function.
    Targets refer only to pairs, not to the full resistance matrix.
    """
    variable, pairs = list(variable), list(pairs)
    m = len(variable)
    if not m:
        raise ValueError("Evaluate a graph with no variables directly")
    all_edges = list(fixed) + variable
    if (len(set(all_edges)) != len(all_edges) or
            any(not (0 <= i < j < n) for i, j in all_edges + pairs)):
        raise ValueError("Use disjoint, unique, ordered vertex pairs")
    fixed_weights = np.array(list(fixed.values()), dtype=float)
    if np.any(fixed_weights < 0) or not np.all(np.isfinite(fixed_weights)):
        raise ValueError("Fixed conductances must be finite and nonnegative")
    x = np.array(initial, dtype=float)
    lo = np.zeros(m) if lower is None else np.array(lower, dtype=float)
    hi = np.full(m, np.inf) if upper is None else np.array(upper, dtype=float)
    target = np.array(target, dtype=float)
    w = np.ones(len(pairs)) if weights is None else np.array(weights, dtype=float)
    if (x.shape != (m,) or lo.shape != (m,) or hi.shape != (m,) or
            target.shape != (len(pairs),) or w.shape != target.shape):
        raise ValueError("Incorrect input dimensions")
    if (not np.all(np.isfinite(x)) or not np.all(np.isfinite(lo)) or
            np.any(np.isnan(hi)) or np.any(lo < 0) or np.any(lo >= hi) or
            np.any(x < lo) or np.any(x > hi) or np.any(w <= 0) or
            not np.all(np.isfinite(w)) or not np.all(np.isfinite(target)) or
            damping <= 0):
        raise ValueError("Invalid bounds, starting point, weights, or damping")
    b_fixed = incidence(n, list(fixed))
    b_var = incidence(n, variable)
    b_pairs = incidence(n, pairs)
    a_fixed = (b_fixed * fixed_weights) @ b_fixed.T

    def evaluate(point):
        matrix = a_fixed + (b_var * point) @ b_var.T
        # A numerical positive-definiteness check, not an exact certificate.
        chol = np.linalg.cholesky(matrix)
        potentials = np.linalg.solve(chol.T, np.linalg.solve(chol, b_pairs))
        resistances = np.sum(b_pairs * potentials, axis=0)
        sensitivity = (b_var.T @ potentials).T ** 2
        residual = resistances - target
        objective = 0.5 * np.dot(w * residual, residual)
        return objective, residual, sensitivity, resistances

    current = evaluate(x)
    history = [float(current[0])]
    status = "iteration_limit"
    for _ in range(max_iterations):
        objective, residual, sensitivity, resistances = current
        if np.max(np.abs(residual)) <= residual_tol:
            status = "residual_tolerance"
            break
        gradient = -sensitivity.T @ (w * residual)
        projected = x - np.clip(x - gradient, lo, hi)
        if np.max(np.abs(projected)) <= stationarity_tol:
            status = "stationarity_tolerance"
            break
        hessian = sensitivity.T @ (w[:, None] * sensitivity) + damping*np.eye(m)
        try:
            step = bound_quadratic(hessian, -gradient, lo-x, hi-x)
        except ArithmeticError:
            status = "inner_accuracy_limit"
            break
        slope = float(gradient @ step)
        if slope >= 0:
            status = "non_descent_numerical_step"
            break
        alpha = 1.0
        for _ in range(60):
            trial = np.clip(x + alpha*step, lo, hi)
            try:
                values = evaluate(trial)
            except np.linalg.LinAlgError:
                alpha *= 0.5
                continue
            if np.isfinite(values[0]) and values[0] <= objective + 1e-4*alpha*slope:
                x, current = trial, values
                history.append(float(current[0]))
                break
            alpha *= 0.5
        else:
            status = "line_search_accuracy_limit"
            break
    # Always recompute and report the final actual graph, even at iteration limit.
    objective, residual, _, resistances = evaluate(x)
    return dict(status=status, conductances=x.tolist(),
                resistances=resistances.tolist(), error=float(objective),
                max_residual=float(np.max(np.abs(residual))),
                accepted_steps=len(history)-1, history=history)


def main():
    exact = search(3, {(0, 1): 1}, [(1, 2)], [(0, 2)], [2], [0.5])
    bounded = search(3, {(0, 1): 1}, [(1, 2)], [(0, 2)], [1], [0.5], upper=[2])
    prism_v = [(3, 4), (3, 5), (4, 5), (0, 3), (1, 4), (2, 5)]
    prism = search(6, {(0, 1): 1, (0, 2): 1, (1, 2): 1}, prism_v,
                   [(0, 1), (0, 2), (1, 2)], [14/25, 8/15, 8/15], [1]*6)
    assert exact["status"] == "residual_tolerance"
    assert abs(exact["conductances"][0]-1) < 1e-9
    assert bounded["status"] == "stationarity_tolerance"
    assert bounded["conductances"] == [2.0]
    assert abs(bounded["error"]-0.125) < 1e-12
    assert prism["status"] == "residual_tolerance"
    assert min(prism["conductances"]) >= 0
    for result in (exact, bounded, prism):
        assert all(b <= a for a, b in zip(result["history"], result["history"][1:]))
    # Validate the returned prism through a separate centered inverse.
    lap = np.zeros((6, 6))
    for (i, j), c in list({(0, 1): 1, (0, 2): 1, (1, 2): 1}.items()) + list(zip(prism_v, prism["conductances"])):
        lap[i, i] += c
        lap[j, j] += c
        lap[i, j] -= c
        lap[j, i] -= c
    gr = np.linalg.inv(lap + np.ones((6, 6))/6) - np.ones((6, 6))/6
    recovered = np.diag(gr)[:, None] + np.diag(gr)[None, :] - 2*gr
    assert np.max(np.abs(recovered[[0, 0, 1], [1, 2, 2]] - [14/25, 8/15, 8/15])) < 1e-10
    output = {name: {k: v for k, v in result.items() if k != "history"}
              for name, result in (("path_exact", exact), ("path_bounded", bounded), ("prism", prism))}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
