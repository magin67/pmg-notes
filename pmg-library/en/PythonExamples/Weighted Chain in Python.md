---
title: "Weighted Chain in Python"
date: 2026-10-29
updated: 2026-11-09
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: python-weighted-chain
lang: en
description: "Laplacian, resistances, currents, and power of a path with conductances 1 and 2."
order: 2
---

This example reproduces the path $1-2-3$ with conductances $c_{12}=1$, $c_{23}=2$ from [[Laplacian - graph, electrical network and quadratic form]] and [[Effective Resistance and Graph Geometry#Example: a three-vertex path|Effective Resistance and Graph Geometry]]. Resistances are evaluated through the metric polyform; current equations provide an independent check.

[[ru/PythonExamples/Взвешенная цепочка на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


This example was checked with `polyform_algebra 0.9.0`. Environment setup: [[Installing the Library and Running Examples]]. Run the Python cells in order.

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb)

![[images/Weighted chain.svg]]

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
matrix = np.asarray(matrix[np.ix_(order, order)], dtype=float)
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
Power balance also gives $\varphi^{\mathsf T}J=6$ and $I^2R_{13}=4\cdot3/2=6$. With conductances in siemens, potentials are in volts and power in watts. The package supplies the matrix; NumPy solves the current equations. Below, this matrix is compared with an independent reference built directly from the conductances.

## Checks

Three mathematical tests check the matrix and resistances, spanning-tree coefficient and exponential factorization, current equations, and three ways of computing power. The independent reference constructs the Laplacian explicitly without converting polyforms: its cofactor gives $\tau$, while three unit-current solves check all pair resistances. General example checks also verify module execution and silent imports.



```python
from math import isclose

reference = np.array([[1., -1., 0.], [-1., 3., -2.], [0., -2., 2.]])
assert np.allclose(matrix, reference)
assert np.allclose(reference @ potential, current)
assert np.allclose(potential, [3., 1., 0.])
assert isclose(float(metric.potential(quForm.one())), 2.)
assert isclose(float(metric.norm(quForm([(points[1], points[3])]))), 1.5)
assert isclose(float(potential @ reference @ potential), 6.)
```


## Try changing the input

Change the second conductance from 2 to 4. Obtain $R_{13}=5/4$ and power 5 for the same current of 2 A.

These numerical checks concern this example and do not replace a general proof.
