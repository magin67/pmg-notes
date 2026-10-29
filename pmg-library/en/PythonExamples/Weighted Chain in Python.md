---
title: "Weighted Chain in Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
source_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-weighted-chain
lang: en
description: "Laplacian, resistances, currents, and power of a path with conductances 1 and 2."
order: 2
---

This example reproduces the path $1-2-3$ with conductances $c_{12}=1$, $c_{23}=2$ from [[Laplacian - graph, electrical network and quadratic form]] and [[Effective Resistance and Graph Geometry#Example: a three-vertex path|Effective Resistance and Graph Geometry]]. Resistances are evaluated through the metric polyform; current equations provide an independent check.

[[ru/PythonExamples/Взвешенная цепочка на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

## Code and execution

The [complete program](https://github.com/magin67/polyform_algebra/blob/b5a4ccfd0207ef6250a97417834ff67b4d94482d/examples/introductory/note01_weighted_chain.py) and [tests](https://github.com/magin67/polyform_algebra/blob/b5a4ccfd0207ef6250a97417834ff67b4d94482d/tests/introductory/test_weighted_chain.py) are pinned to revision `b5a4ccf`. See [[Installing the Library and Running Examples]] for setup. This example requires that revision: the earlier `76c433d` does not contain the chain module. In a separate examples checkout, run `git fetch origin` and `git checkout b5a4ccfd0207ef6250a97417834ff67b4d94482d`.

From the repository root, using the selected environment's Python:

```powershell
python -m examples.introductory.note01_weighted_chain
python -m pytest tests/introductory/test_weighted_chain.py -q
```

On Windows replace `python` with `.\.venv\Scripts\python.exe` if needed; on Linux/macOS use `.venv/bin/python`. In Colab, first follow the source-cloning route in the setup guide, then run:

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "examples.introductory.note01_weighted_chain"],
    check=True,
)
```

For your own calculations, installing the package and running the next fragment is sufficient; the complete programs and tests require the checkout.

## From graph to metric polyform

An edge weight is a conductance. Edge resistances are its reciprocal: $1$ and $1/2$. There is no direct edge $13$.

```python
import networkx as nx
from polyform_algebra import Polyform, quForm

# Edge weights are conductances.
graph = nx.Graph()
graph.add_weighted_edges_from([(1, 2, 1), (2, 3, 2)])
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()

print("tau =", metric.potential(quForm.one()))
for i, j in [(1, 2), (2, 3), (1, 3)]:
    form = quForm([(points[i], points[j])])
    print(f"R{i}{j} =", metric.norm(form))
```

The form $f_{ij}=[a_j-a_i]^2$ is the quadratic form of an edge. Nilpotence of edge forms gives

$$
L=f_{12}+2f_{23},\qquad
M=\exp L=(e+f_{12})(e+2f_{23})
$$
This is the exponential in the algebra of forms, not the matrix exponential. The value `potential(quForm.one())` gives the spanning-tree coefficient, while `norm(form)` gives the normalized metric evaluation.

| Quantity | Result | Explanation |
|---|---:|---|
| $\tau$ | $2$ | The unique spanning tree has weight $1\cdot2$ |
| $R_{12}$ | $1$ | Resistance of the first edge |
| $R_{23}$ | $1/2$ | Resistance of the second edge |
| $R_{13}$ | $3/2$ | Sum of series resistances |

The existence of $R_{13}$ does not imply an edge $13$. In the resistance embedding this is a squared distance; the distance itself is $\sqrt{3/2}$.

## Matrix, currents, and power

The `to_matrix()` method returns a matrix and a point-to-index mapping. In vertex order $1,2,3$:

$$
\mathbf L=
\begin{pmatrix}
1&-1&0\\
-1&3&-2\\
0&-2&2
\end{pmatrix}
$$
Reproduce the first note's experiment: inject 2 A at vertex 1, remove 2 A at vertex 3, and choose $\varphi_3=0$.

```python
import numpy as np

matrix, index = laplacian.to_matrix()
# Reorder rows and columns explicitly as vertices 1, 2, 3.
order = [index[points[label]] for label in (1, 2, 3)]
matrix = matrix[np.ix_(order, order)]
# Ground vertex 3 and inject 2 A at vertex 1.
current = np.array([2.0, 0.0, -2.0])
potential = np.append(np.linalg.solve(matrix[:2, :2], current[:2]), 0.0)
print("potentials =", potential)
print("power =", potential @ matrix @ potential)
```

The result is

$$
\varphi=(3,1,0)^{\mathsf T},\qquad
I_{12}=I_{23}=2,\qquad
\mathcal Q=1(3-1)^2+2(1-0)^2=6
$$
Power balance also gives $\varphi^{\mathsf T}J=6$ and $I^2R_{13}=4\cdot3/2=6$. With conductances in siemens, potentials are in volts and power in watts. The NumPy solver is used only in the example; no general network-solving API is added to the library.

## Checks

Three mathematical tests check the matrix and resistances, spanning-tree coefficient and exponential factorization, current equations, and three ways of computing power. The independent reference constructs the Laplacian explicitly without converting polyforms: its cofactor gives $\tau$, while three unit-current solves check all pair resistances. General example checks also verify module execution and silent imports.

**Status: computed directly.** All 228 project tests passed on Python 3.12. Execution in a hosted Google Colab session has not been separately checked. Calculations use the existing quadratic algebra without extending its model.
