---
title: "Path P5 and Cycle C4 Exponentials in Python"
date: 2026-10-29
updated: 2026-11-09
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: python-path-cycle-exponentials
lang: en
description: "Forest grade components of the P5 and C4 exponentials, spanning-tree coefficients, and effective resistances."
order: 5
---

This example reproduces the path $P_5$ and four-cycle $C_4$ from [[Laplacian Exponential]]. All conductances equal one. The program prints each grade component of the exponential, the spanning-tree coefficient, unnormalized potentials, and all pair resistances.

[[ru/PythonExamples/Экспоненты пути P5 и цикла C4 на Python|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]


This example was checked with `polyform_algebra 0.9.0`. Environment setup: [[Installing the Library and Running Examples]]. Run the Python cells in order.

![[images/Path and cycle in the forest expansion.svg]]

## Construction and grade expansion

For unit conductances, use

$$
M=\exp L=\prod_{ij\in E}(e+f_{ij}),\qquad
f_{ij}=[a_j-a_i]^2,\qquad
M_k=\frac{L^k}{k!}
$$
This is the exponential in the algebra of forms, not the matrix exponential. An edge form is nilpotent, and the product of forms along a cycle vanishes. Grade $k$ therefore collects spanning forests with $k$ edges, including isolated vertices.

A standalone fragment after installing the package:

```python
import networkx as nx
from polyform_algebra import Polyform, quForm

for name, graph in [("P5", nx.path_graph(range(1, 6))),
                    ("C4", nx.cycle_graph(range(1, 5)))]:
    laplacian, points = Polyform.from_networkx(graph, return_points="dict")
    metric = laplacian.exp()
    print(name)
    for k in range(5):
        part = metric.extract_grade(k)
        # Valid for this retained forest representation, not an arbitrary rewrite.
        print(k, part, "forest weight sum =", sum(part.terms.values()))
    print("tau =", metric.potential(quForm.one()))
    pair = (1, 5) if name == "P5" else (1, 2)
    form = quForm([(points[pair[0]], points[pair[1]])])
    print("potential =", metric.potential(form))
    print("resistance =", metric.norm(form))
```

The method `extract_grade(k)` returns a polyform, not a number. In the printed notation, `f[1]` denotes the unit form $e$, while `f[(1, 2), (3, 4)]` denotes $[(12)(34)]^2$. Vertices are numbered from 1.

## Path P5

The path edges are $12,23,34,45$. Every subset is a forest, so the forest counts by grade are the binomial coefficients $\binom4k$:

| Grade $k$ | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Forest weight sum $s_k$ | 1 | 4 | 6 | 4 | 1 |
| Stored term count | 1 | 4 | 6 | 4 | 1 |

For example, the second and top grades are

$$
M_2=[(123)]^2+[(234)]^2+[(345)]^2+[(12)(34)]^2+[(12)(45)]^2+[(23)(45)]^2
$$

$$
M_4=[(12345)]^2,\qquad \tau(P_5)=1
$$
In $(123)$, vertices 4 and 5 remain isolated; their boundaries equal 1. The unique spanning tree is the whole path. Resistance between vertices $i<j$ is $j-i$, in particular $R_{15}=4$.

## Cycle C4

The cycle edges are $12,23,34,41$. Any three form a spanning tree, but all four form a cycle and their form product vanishes:

$$
M_2=[(123)]^2+[(234)]^2+[(134)]^2+[(124)]^2+[(12)(34)]^2+[(14)(23)]^2
$$

$$
M_3=4[(1234)]^2,\qquad M_4=0,\qquad \tau(C_4)=4
$$
| Grade $k$ | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Forest weight sum $s_k$ | 1 | 4 | 6 | 4 | 0 |
| Stored term count | 1 | 4 | 6 | 1 | 0 |

The four spanning trees yield the same form $[(1234)]^2$. Storage retains a single term with coefficient 4. The term count therefore differs from the forest count.

Here the coefficient sum corresponds to the retained forest expansion. After arbitrary rewriting using linear identities among polyforms, that sum need not retain its meaning as $s_k$. It is not a general way to recover forest weights from every representation.

## Potentials and resistances

The `potential` method extracts an unnormalized coefficient; `norm` divides it by the spanning-tree coefficient:

$$
u_M(f_{ij})=\tau(Mf_{ij}),\qquad
R_{ij}=\frac{u_M(f_{ij})}{\tau(M)}
$$
| Graph and pair | Potential | $\tau$ | Resistance |
|---|---:|---:|---:|
| $P_5$, endpoints 1 and 5 | 4 | 1 | 4 |
| $C_4$, neighbors 1 and 2 | 3 | 4 | $3/4$ |
| $C_4$, opposite vertices 1 and 3 | 4 | 4 | 1 |

For neighboring cycle vertices, paths of resistance 1 and 3 are in parallel, so $R_{12}=3/4$. Opposite vertices have two parallel paths of resistance 2, so $R_{13}=1$. For all pairs in $C_4$, $R_{ij}=d(4-d)/4$, where $d=j-i$ for $i<j$.

## Checks and status

Tests independently enumerate edge subsets, reject cycles, and construct forms from connected components. They check the grade components themselves, their forest weights, the identities $M_k=L^k/k!$, and exponential factorization. Separate numerical Laplacians provide cofactors for $\tau$ and unit-current solutions for every pair resistance.



## Try changing the input

Double one cycle conductance. The number of spanning trees remains 4, but their total weight becomes 7.

These numerical checks concern this example and do not replace a general proof.
