"""Exact shunt checks and a reproducible noise experiment for the PMG note.

Install the same package revision as the Electrometry examples:
python -m pip install 'https://github.com/magin67/polyform_algebra/archive/63d342437b0d5973f38befc5183d7f4ea9ecf6f0.zip'
Dependencies: SymPy, NumPy, Matplotlib. Run from any directory.
Results are written next to this script; figures go to ../images.
All resistances are in ohms, conductances in siemens, and currents in amperes.
"""

from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np
import sympy as sp
from polyform_algebra.core import green, kron_reduce, laplacian, network, resistance
from polyform_algebra.variations import vary_conductances

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT.parent / "images"
ELECTRODES = tuple("abmn")
LABELS = tuple("abmnpq")
EDGES = [("a", "p", 1), ("m", "p", 1), ("p", "q", 1),
         ("b", "q", 1), ("n", "q", 1)]


def vector(labels, pair):
    a, b = pair
    return sp.Matrix([int(v == a) - int(v == b) for v in labels])


def direct_green(labels, edges):
    """Independent centered inverse, without using the package update formula."""
    L = sp.zeros(len(labels))
    for a, b, c in edges:
        v = vector(labels, (a, b))
        L += sp.Rational(c) * v * v.T
    J0 = sp.ones(len(labels)) / len(labels)
    return (L + J0).inv() - J0


def transfer(G, labels, current=("a", "b"), sense=("m", "n")):
    return (vector(labels, sense).T * G * vector(labels, current))[0]


def estimate_two(T0, T1, T2, t1, t2):
    d1, d2 = T0 - T1, T0 - T2
    R = (d1 / t1 - d2 / t2) / (d2 - d1)
    A = d1 * (1 + t1 * R) / t1
    return R, A


def checks():
    net = network(LABELS, EDGES)
    G = sp.Matrix(green(net).value.values)
    assert G == direct_green(LABELS, EDGES)
    T0 = transfer(G, LABELS)
    R = sp.Matrix(resistance(net).value.values)
    assert T0 == 1 and R[0, 1] == 3 and R[0, 2] == 2

    # Every electrode pair, two finite conductances, and reversed orientations.
    for pair in combinations(ELECTRODES, 2):
        b = vector(LABELS, pair)
        Rpq = (b.T * G * b)[0]
        A = transfer(G, LABELS, pair, ("a", "b")) * transfer(G, LABELS, pair)
        for t in (Q(1, 4), Q(2, 3)):
            exact = direct_green(LABELS, EDGES + [(*pair, t)])
            package = sp.Matrix(green(vary_conductances(net, {pair: t})).value.values)
            assert exact == package
            assert transfer(exact, LABELS) == T0 - t * A / (1 + t * Rpq)
            assert transfer(exact, LABELS, sense=("n", "m")) == -transfer(exact, LABELS)

    t = sp.Rational(1, 3)
    Tcurrent = transfer(direct_green(LABELS, EDGES + [("a", "b", t)]), LABELS)
    recovered = (T0 / Tcurrent - 1) / t
    assert Tcurrent == sp.Rational(1, 2) and recovered == 3

    t1, t2 = sp.Rational(1, 4), sp.Rational(1, 2)
    T1 = transfer(direct_green(LABELS, EDGES + [("a", "m", t1)]), LABELS)
    T2 = transfer(direct_green(LABELS, EDGES + [("a", "m", t2)]), LABELS)
    assert (T1, T2) == (sp.Rational(7, 6), sp.Rational(5, 4))
    assert estimate_two(T0, T1, T2, t1, t2) == (2, -1)
    A0, R0, x1, x2 = sp.symbols("A R t_1 t_2", nonzero=True)
    eR, eA = estimate_two(0, -x1*A0/(1+x1*R0), -x2*A0/(1+x2*R0), x1, x2)
    assert sp.simplify(eR - R0) == 0 and sp.simplify(eA - A0) == 0

    # Coupled shunts: the off-diagonal Gram entry is nonzero.
    pairs = [("a", "m"), ("b", "m")]
    B = sp.Matrix.hstack(*(vector(LABELS, p) for p in pairs))
    D = sp.diag(t1, t2)
    K = B.T * G * B
    assert K == sp.Matrix([[2, 1], [1, 3]])
    joint = G - G * B * (sp.eye(2) + D*K).inv() * D * B.T * G
    assert joint == direct_green(LABELS, EDGES + [("a", "m", t1), ("b", "m", t2)])
    assert transfer(joint, LABELS) == sp.Rational(10, 29)
    separate_sum = T1 + transfer(direct_green(LABELS, EDGES + [("b", "m", t2)]), LABELS) - T0
    assert separate_sum == sp.Rational(11, 30)
    # Include a cycle and a zero conductance in the general matrix formula.
    Bcycle = sp.Matrix.hstack(*(vector(LABELS, p) for p in [("a", "m"), ("m", "b"), ("a", "b")]))
    for d in (sp.diag(t1, t2, t1), sp.diag(t1, 0, t2)):
        updated = G - G*Bcycle*(sp.eye(3)+d*Bcycle.T*G*Bcycle).inv()*d*Bcycle.T*G
        extra = [(a, b, d[i, i]) for i, (a, b) in enumerate([("a", "m"), ("m", "b"), ("a", "b")])]
        assert updated == direct_green(LABELS, EDGES + extra)

    # Adding an external shunt commutes with eliminating internal vertices.
    reduced = kron_reduce(net, ELECTRODES).value.network
    Lboundary = sp.Matrix(laplacian(reduced).value.values)
    bb = vector(ELECTRODES, ("a", "m"))
    reduced_shunt = kron_reduce(vary_conductances(net, {("a", "m"): Q(1, 4)}), ELECTRODES).value.network
    assert sp.Matrix(laplacian(reduced_shunt).value.values) == Lboundary + t1*bb*bb.T

    # Explicit series contacts: a-c, b-d, m-e, n-f, then the unchanged medium.
    contacts = {"a": Q(1, 5), "b": Q(3, 10), "m": Q(2, 5), "n": Q(1, 10)}
    interfaces = dict(zip(ELECTRODES, "cdef"))
    contact_labels = tuple("abmncdefpq")
    contact_edges = [(interfaces.get(a, a), interfaces.get(b, b), c) for a, b, c in EDGES]
    contact_edges += [(a, interfaces[a], 1/r) for a, r in contacts.items()]
    contact_net = network(contact_labels, contact_edges)
    Gcontact = direct_green(contact_labels, contact_edges)
    assert Gcontact == sp.Matrix(green(contact_net).value.values)
    Tc0 = transfer(Gcontact, contact_labels)
    Tc = transfer(direct_green(contact_labels, contact_edges + [("a", "b", t)]), contact_labels)
    Rcontact = (Tc0/Tc - 1)/t
    assert Tc0 == T0 and Tc == sp.Rational(6, 13) and Rcontact == sp.Rational(7, 2)
    assert Rcontact == R[0, 1] + contacts["a"] + contacts["b"]

    # Symmetric star: all equal pair shunts leave disjoint readings invisible.
    alpha, u = sp.symbols("alpha t", positive=True)
    J = sp.eye(4) - sp.ones(4)/4
    Gstar = alpha*J
    all_equal = alpha*J/(1+4*alpha*u)
    assert transfer(Gstar, ELECTRODES) == transfer(all_equal, ELECTRODES) == 0
    b = vector(ELECTRODES, ("a", "m"))
    Gcross = Gstar - u*(Gstar*b)*(b.T*Gstar)/(1+u*(b.T*Gstar*b)[0])
    assert sp.simplify(transfer(Gcross, ELECTRODES) - alpha**2*u/(1+2*alpha*u)) == 0
    star_labels = tuple("abmnh")
    star_edges = [(a, "h", 1) for a in ELECTRODES]
    assert transfer(direct_green(star_labels, star_edges + [(a, b, Q(1, 4)) for a, b in combinations(ELECTRODES, 2)]), star_labels) == 0
    return {"T0": str(T0), "R_ab": str(recovered), "T_ab_shunt": str(Tcurrent),
            "T_am_shunts": [str(T1), str(T2)], "R_am": "2", "product_A": "-1",
            "two_shunts": "10/29", "sum_of_separate_responses": "11/30",
            "contact_T0": str(Tc0), "contact_T_shunt": str(Tc), "contact_R_ab": str(Rcontact),
            "exact_checks": "passed"}


def noise_experiment():
    rng = np.random.default_rng(20261115)
    trials, sigma, T0, R = 10000, 0.001, 1.0, 3.0
    levels = np.array([0.01, 0.1, 1/3, 1.0, 10.0])
    # Same noisy baseline reused across shunt levels: estimates are correlated.
    baseline = T0 + rng.normal(0, sigma, trials)
    rows = []
    for t in levels:
        true_T = T0/(1+t*R)
        measured = true_T + rng.normal(0, sigma, trials)
        estimate = (baseline/measured - 1)/t
        rel = (estimate-R)/R
        # First-order standard uncertainty for independent errors in T0 and T(t).
        linear_sd = sigma/(t*R*true_T)*np.sqrt(1+(T0/true_T)**2)
        rows.append({"t_S": float(t), "tR": float(t*R), "T_ohm": float(true_T),
                     "linear_sd_percent": float(100*linear_sd),
                     "sample_sd_percent": float(100*np.std(rel, ddof=1)),
                     "median_bias_percent": float(100*np.median(rel)),
                     "negative_estimates": int(np.sum(estimate < 0))})
    return {"seed": 20261115, "trials": trials, "sigma_T_ohm": sigma,
            "T0_ohm": T0, "R_ohm": R, "rows": rows}


def figures(noise):
    IMAGES.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(9, 5))
    positions = {"a": (0, 2), "p": (2, 2), "q": (4, 2), "b": (6, 2), "m": (2, 0), "n": (4, 0)}
    for a, b, _ in EDGES:
        x1, y1 = positions[a]; x2, y2 = positions[b]
        ax.plot([x1, x2], [y1, y2], color="#43667a", lw=2, zorder=1)
        x, y = (x1+x2)/2, (y1+y2)/2
        ax.add_patch(Rectangle((x-.23, y-.17), .46, .34, fc="white", ec="#43667a", zorder=2))
        ax.text(x, y, "1", ha="center", va="center", zorder=3)
    ax.plot([0, 0, 6, 6], [2, 3.45, 3.45, 2], color="#bb5a23", lw=2)
    ax.add_patch(Rectangle((2.5, 3.25), 1, .4, fc="white", ec="#bb5a23", zorder=3))
    ax.text(3, 3.45, "1/t", ha="center", va="center", color="#9c4719", zorder=4)
    ax.text(3, 3.95, "Внешний шунт между a и b", ha="center", color="#9c4719")
    for name, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), .14, fc="white", ec="#253c4a", lw=1.7, zorder=4))
        dx, dy = {"p": (-.28, .32), "q": (.28, .32),
                  "m": (-.3, -.05), "n": (.3, -.05)}.get(name, (0, -.36))
        ax.text(x+dx, y+dy, name, ha="center", va="center", fontsize=13)
    ax.annotate("", xy=(-.18, 2), xytext=(-1, 2), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.text(-.65, 2.23, "I", ha="center")
    ax.annotate("", xy=(7, 2), xytext=(6.18, 2), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.text(6.65, 2.23, "I", ha="center")
    ax.plot([2, 2, 4, 4], [0, -.8, -.8, 0], ls=":", color="#777777")
    ax.add_patch(Circle((3, -.8), .22, fc="white", ec="#777777", zorder=3))
    ax.text(3, -.8, "V", ha="center", va="center", zorder=4)
    ax.text(3, -1.38, "В прямоугольниках - сопротивления, Ом; t - проводимость, См", ha="center", fontsize=10)
    ax.set(xlim=(-1.2, 7.2), ylim=(-1.6, 4.25), aspect="equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(IMAGES / "Сеть с управляемым шунтом.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.7))
    x = np.geomspace(.02, 50, 300)
    sigma = noise["sigma_T_ohm"]/noise["T0_ohm"]
    y = 100*sigma*(1+x)/x*np.sqrt(1+(1+x)**2)
    ax.loglog(x, y, color="#20618c", label="Линейная оценка погрешности")
    ax.scatter([r["tR"] for r in noise["rows"]], [r["sample_sd_percent"] for r in noise["rows"]], color="#bb5a23", label="10 000 опытов с шумом", zorder=4)
    ax.set(xlabel="Безразмерная проводимость tR", ylabel="Стандартное отклонение оценки R, %",
           title="Слабый и сильный шунты ухудшают точность в этой модели")
    ax.grid(True, which="both", alpha=.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(IMAGES / "Погрешность восстановления при шунтировании.svg")
    plt.close(fig)


if __name__ == "__main__":
    result = {"package_revision": "63d342437b0d5973f38befc5183d7f4ea9ecf6f0",
              "exact": checks(), "noise": noise_experiment()}
    figures(result["noise"])
    path = ROOT / "Результаты шунтирования.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
