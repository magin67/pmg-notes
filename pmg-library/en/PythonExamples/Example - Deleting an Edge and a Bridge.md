---
title: "Example: Deleting an Edge and a Bridge"
date: 2026-10-29
updated: 2026-11-10
revision: 4
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: python-edge-deletion
lang: en
description: "Deleting a cycle edge and a bridge, preserving vertices, and limits of metric-polyform normalization."
order: 6
aliases:
  - "en/PythonExamples/Deleting an Edge and a Bridge in Python"
---

This example illustrates the deletion rule in [[Laplacian Exponential#Adding and deleting an edge|Laplacian Exponential]]. It deletes edge $ab$ of the unit cycle $C_4$, then considers deleting the bridge $bc$ of conductance 2 in the path $a-b-c$ with conductances $c_{ab}=1$ and $c_{bc}=2$. The second graph becomes disconnected.

[[ru/PythonExamples/Пример - Удаление ребра и моста|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


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

# Delete edge ab of the unit cycle C4.
graph = nx.cycle_graph(list("abcd"))
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points["a"], points["b"])])
updated = metric * (Polyform.one() - p)
print("cycle tau =", updated.potential(quForm.one()))
print("cycle R_ab =", updated.norm(p))

# Delete the bridge of conductance 2, retaining isolated vertex c.
graph = nx.Graph()
graph.add_weighted_edges_from([("a", "b", 1), ("b", "c", 2)])
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points["b"], points["c"])])
updated = metric * (Polyform.one() - 2*p)
print("bridge tau =", updated.potential(quForm.one()))
print("remaining exponential =", updated)
f_ac = quForm([(points["a"], points["c"])])
print("unnormalized potential =", updated.potential(f_ac))
try:
    updated.norm(f_ac)
except ValueError as error:
    # Expected: normalization on the full disconnected graph is undefined.
    print(error)
```

## Deleting a cycle edge

Deleting $ab$ leaves the path $a-d-c-b$. It retains all four vertices and remains connected.

| Quantity | Before | After |
|---|---:|---:|
| Spanning-tree coefficient | 4 | 1 |
| Resistance $R_{ab}$ | $3/4$ | 3 |
| Highest exponential grade | 3 | 3 |

The identity $\tau'=4(1-3/4)=1$ agrees with the unique remaining spanning tree. Vertices a and b now have three unit resistances in series.

## Deleting a bridge

In the path $a-b-c$ with $c_{ab}=1$, $c_{bc}=2$, delete edge $bc$. Vertex c becomes isolated but remains in the fixed vertex set:

$$
M=(e+f_{ab})(e+2f_{bc}),\qquad
M'=M(e-2f_{bc})=e+f_{ab}
$$

$$
\tau(M')=0,\qquad u_{M'}(f_{ac})=1
$$
Before deletion, $\tau=2$ and $R_{bc}=1/2$, so $\tau'=2(1-2\cdot1/2)=0$. The highest nonzero grade falls from 2 to 1. The coefficient 1 of the remaining form $f_{ab}$ is not the spanning-tree coefficient on three vertices: that coefficient is still extracted at $T_3=[(abc)]^2$ and is zero.

The potential $u_{M'}(f_{ac})=1$ remains meaningful: the added form connects the components into a spanning tree. Normalization by $\tau(M')=0$ is impossible. The `norm` method raises `ValueError` rather than returning zero or a finite resistance between components. In the full program's output, `None` means the normalized value is not computed.

Within component $\{a,b\}$, the physical resistance is 1. However, the global polyform of the disconnected graph cannot normalize even this pair. Construct a separate component metric to compute it. The original isolated vertex must not silently disappear from the global context.

## Checks and status

Six mathematical checks compare factor deletion with a complete rebuild from the remaining graph, check edge restoration, matrices and their cofactors, a current solve for the connected case, and rejection of disconnected normalization. They also check the linear update of unnormalized potentials, $u_{M'}(f)=u_M(f)-c_{ij}u_M(pf)$.



This is a limitation of global normalization by `Polyform.norm`. The network interface `polyform_algebra.core.resistance` also handles disconnected networks: resistances within components are finite, while cross-component values are represented by `INFINITY` in exact mode. These answers belong to different operations.

## Try changing the input

Reduce the bridge conductance from 2 to 1 instead of deleting it. Check $	au=1$ and $R_{ac}=2$.

These numerical checks concern this example and do not replace a general proof.
