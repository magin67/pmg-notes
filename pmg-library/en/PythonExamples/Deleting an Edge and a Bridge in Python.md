---
title: "Deleting an Edge and a Bridge in Python"
date: 2026-10-29
updated: 2026-11-09
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: python-edge-deletion
lang: en
description: "Deleting a cycle edge and a bridge, preserving vertices, and limits of metric-polyform normalization."
order: 6
---

This example illustrates the deletion rule in [[Laplacian Exponential#Adding and deleting an edge|Laplacian Exponential]]. It deletes edge $12$ of the unit cycle $C_4$, then considers deleting the bridge $23$ of conductance 2 in a path with conductances 1 and 2. The second graph becomes disconnected.

[[ru/PythonExamples/Удаление ребра и моста на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


This example was checked with `polyform_algebra 0.9.0`. Environment setup: [[Installing the Library and Running Examples]]. Run the Python cells in order.

![[images/Deleting an edge and a bridge.svg]]

## Deletion rule

The existing edge is removed completely, so its conductance is reduced by exactly $c_{ij}$:

$$
p=[a_j-a_i]^2,\qquad M' = M(e-c_{ij}p),\qquad
\tau(M')=\tau(M)(1-c_{ij}R_{ij})
$$
In the tree-coefficient formula, $R_{ij}$ refers to the original connected network. The negative coefficient in the deletion factor is valid in the algebra; the final edge conductance is zero. This does not add an edge of negative conductance.

Since $p^2=0$, we have $(e+cp)(e-cp)=e$. Adding the removed conductance back therefore restores the original exponential, even after bridge deletion.

## Executable fragment

```python
import networkx as nx
from polyform_algebra import Polyform, quForm

# Delete edge 12 of the unit cycle C4.
graph = nx.cycle_graph(range(1, 5))
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points[1], points[2])])
updated = metric * (Polyform.one() - p)
print("cycle tau =", updated.potential(quForm.one()))
print("cycle R12 =", updated.norm(p))

# Delete the bridge of conductance 2, retaining isolated vertex 3.
graph = nx.Graph()
graph.add_weighted_edges_from([(1, 2, 1), (2, 3, 2)])
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points[2], points[3])])
updated = metric * (Polyform.one() - 2*p)
print("bridge tau =", updated.potential(quForm.one()))
print("remaining exponential =", updated)
f13 = quForm([(points[1], points[3])])
print("unnormalized potential =", updated.potential(f13))
try:
    updated.norm(f13)
except ValueError as error:
    # Expected: normalization on the full disconnected graph is undefined.
    print(error)
```

## Deleting a cycle edge

Deleting $12$ leaves the path $1-4-3-2$. It retains all four vertices and remains connected.

| Quantity | Before | After |
|---|---:|---:|
| Spanning-tree coefficient | 4 | 1 |
| Resistance $R_{12}$ | $3/4$ | 3 |
| Highest exponential grade | 3 | 3 |

The identity $\tau'=4(1-3/4)=1$ agrees with the unique remaining spanning tree. Vertices 1 and 2 now have three unit resistances in series.

## Deleting a bridge

In the path $1-2-3$ with $c_{12}=1$, $c_{23}=2$, delete edge $23$. Vertex 3 becomes isolated but remains in the fixed vertex set:

$$
M=(e+f_{12})(e+2f_{23}),\qquad
M'=M(e-2f_{23})=e+f_{12}
$$

$$
\tau(M')=0,\qquad u_{M'}(f_{13})=1
$$
Before deletion, $\tau=2$ and $R_{23}=1/2$, so $\tau'=2(1-2\cdot1/2)=0$. The highest nonzero grade falls from 2 to 1. The coefficient 1 of the remaining form $f_{12}$ is not the spanning-tree coefficient on three vertices: that coefficient is still extracted at $T_3=[(123)]^2$ and is zero.

The potential $u_{M'}(f_{13})=1$ remains meaningful: the added form connects the components into a spanning tree. Normalization by $\tau(M')=0$ is impossible. The `norm` method raises `ValueError` rather than returning zero or a finite resistance between components. In the full program's output, `None` means the normalized value is not computed.

Within component $\{1,2\}$, the physical resistance is 1. However, the global polyform of the disconnected graph cannot normalize even this pair. Construct a separate component metric to compute it. The original isolated vertex must not silently disappear from the global context.

## Checks and status

Six mathematical checks compare factor deletion with a complete rebuild from the remaining graph, check edge restoration, matrices and their cofactors, a current solve for the connected case, and rejection of disconnected normalization. They also check the linear update of unnormalized potentials, $u_{M'}(f)=u_M(f)-c_{ij}u_M(pf)$.



This is a limitation of global normalization by `Polyform.norm`. The network interface `polyform_algebra.core.resistance` also handles disconnected networks: resistances within components are finite, while cross-component values are represented by `INFINITY` in exact mode. These answers belong to different operations.

## Try changing the input

Reduce the bridge conductance from 2 to 1 instead of deleting it. Check $	au=1$ and $R_{13}=2$.

These numerical checks concern this example and do not replace a general proof.
