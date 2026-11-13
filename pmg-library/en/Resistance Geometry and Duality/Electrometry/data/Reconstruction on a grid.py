"""Model experiment for "Reconstructing Couplings with a Prescribed Neighbor Structure".

Python 3, NumPy, SciPy, Matplotlib. Run: python "Reconstruction on a grid.py"
Saves CSV and JSON beside this script, and figures in the sibling images folder.
All quantities are dimensionless; this is a synthetic finite network, not field data.
"""
from pathlib import Path
from itertools import product, combinations
import argparse
import csv
import json
import numpy as np
import scipy
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import least_squares
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMAGES = HERE.parent / "images"
IMAGES.mkdir(exist_ok=True)
N = 4
XYZ = np.array(list(product(range(N), repeat=3)))
INDEX = {tuple(p): k for k, p in enumerate(XYZ)}
EDGES = []
for i, point in enumerate(XYZ):
    for direction in range(3):
        other = point.copy()
        other[direction] += 1
        if other[direction] < N:
            EDGES.append((i, INDEX[tuple(other)]))
EDGES = np.array(EDGES)
TOP = np.flatnonzero(XYZ[:, 2] == 0)
PAIRS = np.array(list(combinations(TOP, 2)))
INC = np.zeros((len(XYZ), len(EDGES)))
for k, (i, j) in enumerate(EDGES):
    INC[i, k], INC[j, k] = 1.0, -1.0
CURRENT = np.zeros((len(XYZ), len(PAIRS)))
for k, (i, j) in enumerate(PAIRS):
    CURRENT[i, k], CURRENT[j, k] = 1.0, -1.0
# Removing one row fixes a zero potential without changing resistances.
INC, CURRENT = INC[:-1], CURRENT[:-1]


def network(conductance):
    laplacian = (INC * conductance) @ INC.T
    potentials = cho_solve(cho_factor(laplacian, lower=True), CURRENT)
    resistance = np.sum(CURRENT * potentials, axis=0)
    sensitivity = (INC.T @ potentials).T ** 2
    return resistance, sensitivity


def layer_map(theta):
    """Horizontal couplings equal theta[z]; vertical couplings use the harmonic mean."""
    conductance = np.empty(len(EDGES))
    derivative = np.zeros((len(EDGES), N))
    for k, (i, j) in enumerate(EDGES):
        z, w = XYZ[i, 2], XYZ[j, 2]
        if z == w:
            conductance[k], derivative[k, z] = theta[z], 1.0
        else:
            total = theta[z] + theta[w]
            conductance[k] = 2 * theta[z] * theta[w] / total
            derivative[k, z] = 2 * theta[w] ** 2 / total ** 2
            derivative[k, w] = 2 * theta[z] ** 2 / total ** 2
    return conductance, derivative


def forward(theta):
    conductance, derivative = layer_map(theta)
    resistance, sensitivity = network(conductance)
    return resistance, -sensitivity @ derivative


def fit(observed, scale, fixed_bottom=None, regularization=0.0):
    n = N if fixed_bottom is None else N - 1

    def full_theta(x):
        return x if fixed_bottom is None else np.r_[x, fixed_bottom]

    def residual(x):
        data = (forward(full_theta(x))[0] - observed) / scale
        return np.r_[data, np.sqrt(regularization) * (x - 1)]

    def jacobian(x):
        data = forward(full_theta(x))[1][:, :n] / scale[:, None]
        return np.vstack([data, np.sqrt(regularization) * np.eye(n)])

    result = least_squares(residual, np.ones(n), jac=jacobian, bounds=(0.5, 1.5),
                           method="trf", ftol=1e-12, xtol=1e-12, gtol=1e-12,
                           max_nfev=500)
    assert result.success, result.message
    return full_theta(result.x), result


def main(preview_dir=None):
    baseline = np.ones(N)
    truth = np.array([1.0, 1.15, 0.85, 1.1])
    r0, jac0 = forward(baseline)
    rtrue, jac_true = forward(truth)
    eta = 0.001
    noise = eta * r0 * np.random.default_rng(1304).normal(size=len(PAIRS))
    observed = rtrue + noise
    normalized_jac = jac0 / r0[:, None]
    singular = np.linalg.svd(normalized_jac, compute_uv=False)
    known_bottom_reference = np.r_[np.ones(N - 1), truth[3]]
    jac_three = forward(known_bottom_reference)[1][:, :3] / r0[:, None]
    singular_three = np.linalg.svd(jac_three, compute_uv=False)
    free_singular = np.linalg.svd(network(np.ones(len(EDGES)))[1], compute_uv=False)

    step = 1e-5
    finite_difference = np.column_stack([
        (forward(truth + step * np.eye(N)[k])[0] -
         forward(truth - step * np.eye(N)[k])[0]) / (2 * step)
        for k in range(N)])
    jac_error = float(np.max(np.abs(finite_difference - jac_true)))
    assert jac_error < 1e-8
    # Independently check derivatives of all 144 individual couplings using the definition of R.
    base_c = layer_map(truth)[0]
    _, sensitivity = network(base_c)
    free_diff = np.column_stack([
        (network(base_c + step * np.eye(len(EDGES))[k])[0] -
         network(base_c - step * np.eye(len(EDGES))[k])[0]) / (2 * step)
        for k in range(len(EDGES))])
    free_error = float(np.max(np.abs(free_diff + sensitivity)))
    assert free_error < 1e-8

    scenarios = [
        ("exact_four", "Exact data, 4 parameters", rtrue, r0, None, 0.0),
        ("noisy_four", "Noise, 4 parameters", observed, eta * r0, None, 0.0),
        ("known_bottom", "Noise, known bottom layer", observed, eta * r0, truth[3], 0.0),
        ("prior_four", "Noise, penalty toward background", observed, eta * r0, None, 1.0),
    ]
    fits = {}
    for key, label, data, scale, bottom, alpha in scenarios:
        theta, result = fit(data, scale, bottom, alpha)
        relative_residual = (forward(theta)[0] - data) / r0
        fits[key] = {"label": label, "theta": theta.tolist(),
                     "rms_percent": float(np.sqrt(np.mean(relative_residual ** 2)) * 100),
                     "evaluations": result.nfev, "lambda": alpha,
                     "bottom_fixed": bottom is not None}
    assert np.max(np.abs(np.array(fits["exact_four"]["theta"]) - truth)) < 1e-7

    summary = {
        "grid": [N, N, N], "vertices": len(XYZ), "edges": len(EDGES),
        "electrodes": len(TOP), "observations": len(PAIRS), "seed": 1304,
        "noise_sd_relative_to_background": eta,
        "noise_rms_percent": float(np.sqrt(np.mean((noise / r0) ** 2)) * 100),
        "bounds": [0.5, 1.5], "truth": truth.tolist(),
        "relative_jacobian_singular_values": singular.tolist(),
        "condition_four": float(singular[0] / singular[-1]),
        "condition_three": float(singular_three[0] / singular_three[-1]),
        "known_bottom_reference": known_bottom_reference.tolist(),
        "free_rank_at_absolute_threshold_1e-10": int(np.sum(free_singular > 1e-10)),
        "free_smallest_singular_value": float(free_singular[-1]),
        "layer_jacobian_max_absolute_error": jac_error,
        "edge_jacobian_max_absolute_error": free_error,
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__}, "fits": fits,
    }
    (HERE / "Reconstruction results.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (HERE / "Model measurements.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["electrode_a", "electrode_b", "x_a", "y_a", "x_b", "y_b",
                         "R_background", "R_true", "R_observed", "noise_sd"])
        labels = {node: chr(ord("a") + k) for k, node in enumerate(TOP)}
        for k, (a, b) in enumerate(PAIRS):
            writer.writerow([labels[a], labels[b], *XYZ[a, :2], *XYZ[b, :2],
                             r0[k], rtrue[k], observed[k], eta * r0[k]])

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "svg.fonttype": "none", "axes.spines.top": False,
                         "axes.spines.right": False})
    colors = ["#1565a6", "#3892b5", "#d18a24", "#a8483a"]
    fig = plt.figure(figsize=(9, 5.4), layout="constrained")
    ax = fig.add_subplot(111, projection="3d")
    for i, j in EDGES:
        ax.plot(*XYZ[[i, j]].T, color="#8995a2", alpha=0.5, linewidth=0.8)
    for z in range(N):
        points = XYZ[XYZ[:, 2] == z]
        ax.scatter(*points.T, color=colors[z], s=42 if z == 0 else 15,
                   depthshade=False, label=f"Layer {z + 1}, θ{z + 1} = {truth[z]:.2f}")
    ax.set(xlabel="x", ylabel="y", zlabel="Depth z", xticks=range(N),
           yticks=range(N), zticks=range(N), zlim=(3.2, -0.2))
    ax.set_box_aspect((1, 1, 0.8))
    ax.view_init(elev=23, azim=-57)
    ax.set_title("Finite 4 × 4 × 4 network\n16 electrodes on the top face", pad=12)
    ax.legend(loc="center left", bbox_to_anchor=(1.16, 0.5), frameon=False)
    fig.savefig(IMAGES / "Medium model on a grid.svg", bbox_inches="tight")
    if preview_dir is not None:
        fig.savefig(preview_dir / "grid-preview.png", dpi=140, bbox_inches="tight")
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5), sharex=True, sharey=True,
                             layout="constrained")
    captions = ["4 unknown layers", "Known bottom layer", "Penalty toward background, λ = 1"]
    for ax, key, caption in zip(axes, ["noisy_four", "known_bottom", "prior_four"], captions):
        ax.plot(truth, range(1, N + 1), "o-", color="#27394b", label="Prescribed medium")
        ax.plot(fits[key]["theta"], range(1, N + 1), "s--", color="#bd5b24", label="Reconstruction")
        ax.set(title=caption, xlabel="Conductivity θ", xlim=(0.45, 1.55),
               ylim=(4.3, 0.7), yticks=range(1, N + 1))
        ax.grid(alpha=0.2)
    axes[0].set_ylabel("Layer number from the surface")
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    fig.suptitle("The same 120 measurements with 0.1% noise", fontsize=13)
    fig.savefig(IMAGES / "Layer reconstruction under different assumptions.svg")
    if preview_dir is not None:
        fig.savefig(preview_dir / "figure-preview.png", dpi=140)
    plt.close(fig)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path, help="Folder for optional PNG previews")
    args = parser.parse_args()
    if args.preview_dir is not None:
        args.preview_dir.mkdir(parents=True, exist_ok=True)
    main(args.preview_dir)
