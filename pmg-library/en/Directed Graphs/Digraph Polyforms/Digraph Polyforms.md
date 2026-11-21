---
title: Digraph Polyforms
date: 2026-11-21
updated: 2026-11-21
revision: 2
translated_revision: 11
status: published
text_prepared_by: ChatGPT
lang: en
translation_key: digraph-polyforms-series-navigation
order: 0
description: From the arc form and rooted forests to one-way resistance, reconstruction and measurements of higher-grade boundaries.
tags:
- directed-graphs
- resistances
- reconstruction
---

For an undirected edge, the same quadratic form contributes to the Laplacian and measures resistance. What changes when each arc has its own direction and weight? We build the polyform from the arcs, then use it to measure an ordered pair, two vectors and finally a boundary of any grade.

## From an arc to a boundary measurement

**1. [[en/Directed Graphs/Digraph Polyforms/How Arcs Form the Polyform of a Digraph|How Arcs Form the Polyform of a Digraph]]** Read the outgoing Laplacian from a weighted digraph. Its exponential retains precisely the forests whose arcs point toward their roots. All grades are computed for a three-vertex example.

**2. [[en/Directed Graphs/Digraph Polyforms/Computing a Rooted Spanning-Tree Potential from a Digraph Polyform|Computing a Rooted Spanning-Tree Potential from a Digraph Polyform]]** Multiplying by $[b]^2$ selects three trees rooted at $b$. Their total weight agrees with a principal minor. A directed path shows when a rooted potential vanishes.

**3. [[en/Directed Graphs/Digraph Polyforms/The Arc Form and the One-Way Resistance Form|The Arc Form and the One-Way Resistance Form]]** Two multiplications use the same metric on a unit directed three-cycle. The arc form gives the change in the rooted potentials when its weight increases. The measurement forms give one-way resistances $1/3$ and $2/3$.

**4. [[en/Directed Graphs/Digraph Polyforms/How to Normalize One-Way Resistance in an Unbalanced Digraph|How to Normalize One-Way Resistance in an Unbalanced Digraph]]** Sum the measurement coefficients over all roots. In the graph with rooted potentials $5,4,7$, the two directions give $1/4$ and $3/16$. The quadratic form of the pair gives their sum, $7/16$. On a directed path a one-way resistance can vanish.

**5. [[en/Directed Graphs/Digraph Polyforms/Can the One-Way Resistance Matrix Recover a Digraph|Can the One-Way Resistance Matrix Recover a Digraph?]]** The resistance table recovers the differences between Laplacian rows. The relative rooted potentials supply the missing row information, even for an arc along which the one-way resistance is zero.

**6. [[en/Directed Graphs/Digraph Polyforms/Computing the Directed Scalar Product of Two Vectors in a Digraph|Computing the Directed Scalar Product of Two Vectors in a Digraph]]** Evaluate the mixed form $[u,v]$ with the first vector as source and the second as receiver. In the running example, exchanging $(ab)$ and $(ac)$ changes $1/4$ to $1/8$. The difference measures circulation around the triangle.

**7. [[en/Directed Graphs/Digraph Polyforms/What Does the Product of Two Side Forms of a Triangle Measure|What Does the Product of Two Side Forms of a Triangle Measure?]]** Three products of side forms sum to the quadratic form of a triangular boundary. In a directed four-cycle the three starts contribute $1/4,1/4,1/2$. Their sum equals the Gram determinant of the directed scalar product.

**8. [[en/Directed Graphs/Digraph Polyforms/Computing the Norm of a Boundary of Any Grade in a Digraph|Computing the Norm of a Boundary of Any Grade in a Digraph]]** On $k+1$ vertices, products of consecutive pair forms give one term per starting vertex. After evaluation their sum is the Gram determinant. A tetrahedron in two cycles shows how a vertex outside the tetrahedron changes the individual contributions.

## Results of the series

| Notes | Basis for the calculation | What the polyform determines |
| --- | --- | --- |
| 1–2 | Forest expansion and directed matrix-tree theorem | Total spanning-tree weight at each root and the criterion for a zero potential |
| 3–4 | Centroid measurement form and normalization by total rooted potential | One-way resistances and their sum for opposite directions |
| 5–6 | Centering the resistance table and bilinearity | Laplacian row differences and the directed scalar product. The relative rooted potentials also recover the arc weights |
| 7–8 | Exterior algebra and a determinant coefficient | The full boundary norm in any grade and each starting-vertex contribution |

The notes prove these results for the stated normalization. Historical priority has not been assessed. It remains open how to distinguish the two orientations of a boundary of grade $k\ge2$ independently of its starting vertex.

Three conventions run through the series. Vertex $i$ in $i\to j$ specifies a Laplacian row. Tree arcs point toward the root. An arc form changes the graph, and the measurement form of an ordered pair evaluates a quantity on the graph already given.

For notation and the connected balanced case, see the [[en/Getting Started and Foundations/Foundations/Core specification#Polyforms of general digraphs|Polyforms of general digraphs]] and [[en/Directed Graphs/Balanced graphs/Balanced Graphs|Balanced Graphs]].

[[en/Directed Graphs/Directed Graphs|Directed Graphs]]

## Programming example

[[en/PythonExamples/Example - Digraph Polyforms|Five calculations with DirectedNetwork]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/digraph-polyforms.ipynb).

[[ru/Направленные графы/Полиформы орграфов/Полиформы орграфов|Русский]]
