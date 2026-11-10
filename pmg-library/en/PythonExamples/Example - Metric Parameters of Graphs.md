---
title: "Example: Metric Parameters of Graphs"
date: 2026-11-10
updated: 2026-11-10
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-metric-parameters
lang: en
description: "Radii, centralities, compactness, vertex removal, and subgraph norms."
order: 8
---

Eight calculations accompany the eight notes in the Metric Parameters of Graphs series. Metric and spanning-tree quantities use rational arithmetic; eigenvector centrality uses a numerical method.

[[ru/PythonExamples/Пример - Метрические параметры графов|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the tested package revision with the exact operations used in this series. [polyform-algebra 14f137c](https://github.com/magin67/polyform_algebra/commit/14f137c0b4bf965392f47f877165f2f3b8168073).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/metric-parameters.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/metric-parameters.ipynb)

## Radius and diameter of a path and a star

Compare the path $a-b-c-d$ with the star centered at $a$, with unit conductances throughout. Exact arithmetic gives $\rho=3/4$ and $D_{\mathrm{res}}=4\rho=3$ for both trees. The maximum pairwise resistance is $3$ for the path and $2$ for the star. The centers have different bi-coordinates, with a negative coordinate at the hub of the star.

[[en/Resistance Geometry and Duality/Metric parameters/Resistance Radius and Diameter of a Graph#Simple examples|Related section of the note]].

```python
from fractions import Fraction as Q
from itertools import combinations
from math import isclose

from networkx import Graph
from polyform_algebra.core import (
    Network, circumsphere, degree_potential, evaluate_form, green, induced_subgraph,
    kron_reduce, laplacian, laplacian_circumsphere, laplacian_form, network,
    resistance, simplex_volume_squared, spanning_tree_weight,
)
from polyform_algebra.matrix.networkx import from_networkx

vertices = ("a", "b", "c", "d")
path = network(vertices, (("a", "b", 1), ("b", "c", 1), ("c", "d", 1)))
star = network(vertices, (("a", "b", 1), ("a", "c", 1), ("a", "d", 1)))
graphs = {"P4": path, "K1,3": star}

spheres = {name: circumsphere(graph).value for name, graph in graphs.items()}
assert spheres["P4"].center_coordinates.values == (Q(1, 2), 0, 0, Q(1, 2))
assert spheres["K1,3"].center_coordinates.values == (Q(-1, 2), Q(1, 2), Q(1, 2), Q(1, 2))
maximum_resistances = {}
for name, graph in graphs.items():
    sphere = spheres[name]
    rho = sphere.resistance_radius
    center = ", ".join(
        f"{vertex}={value}" for vertex, value in zip(vertices, sphere.center_coordinates.values)
    )
    maximum_resistances[name] = max(max(row) for row in resistance(graph).value.values)
    assert rho == Q(3, 4)
    print(f"{name}: rho={rho}, D_res={4 * rho}, max R={maximum_resistances[name]}")
    print(f"  center: {center}")
assert maximum_resistances == {"P4": 3, "K1,3": 2}
```

## Radius and volume of a subset

Take the unit complete graph $K_4$. Its resistance simplex is a regular tetrahedron. To compute the radius of the face $abc$ in the full graph's metric, eliminate $d$ by Kron reduction. For the squared area use the original graph and the selected vertices. The tetrahedron has $\rho=3/16$ and $V^2=1/576$, and the face has $\rho=1/6$ and $S^2=3/64$.

[[en/Resistance Geometry and Duality/Metric parameters/Resistance Radius of a Set - Gram Matrix and Volume#Examples and normalization checks|Related section of the note]].

```python
tetrahedron = network(vertices, tuple((i, j, 1) for i, j in combinations(vertices, 2)))
face = ("a", "b", "c")
face_network = kron_reduce(tetrahedron, face).value.network
tetrahedron_radius = circumsphere(tetrahedron).value.resistance_radius
face_radius = circumsphere(face_network).value.resistance_radius
volume_squared = simplex_volume_squared(tetrahedron, vertices).value
face_area_squared = simplex_volume_squared(tetrahedron, face).value
assert (tetrahedron_radius, volume_squared) == (Q(3, 16), Q(1, 576))
assert (face_radius, face_area_squared) == (Q(1, 6), Q(3, 64))
print(f"abcd: rho={tetrahedron_radius}, V²={volume_squared}")
print(f"abc: rho={face_radius}, area²={face_area_squared}")
```

## Three centralities

Compare centroid, spanning-tree, and eigenvector centralities on the same path and star. Centroid scores are proportional to the reciprocals of the diagonal entries of the Green matrix. Tree scores are proportional to expected tree degrees $\delta_i=2(1-\alpha^i)$. Compute these two columns exactly and use a numerical adjacency eigenvector for the spectral column. Each column sums to one.

[[en/Resistance Geometry and Duality/Metric parameters/Centroid, Spanning-Tree, and Eigenvector Centralities#The complete graph, a path, and a star|Related section of the note]].

```python
def centralities(graph, sphere):
    Gr = green(graph).value.values
    inverse_norms = tuple(1 / row[i] for i, row in enumerate(Gr))
    centroid = tuple(value / sum(inverse_norms) for value in inverse_norms)
    expected_degrees = tuple(2 * (1 - x) for x in sphere.center_coordinates.values)
    tree_scores = tuple(value / sum(expected_degrees) for value in expected_degrees)

    nx_graph = Graph()
    nx_graph.add_nodes_from(graph.context.labels)
    # Convert conductances at the boundary of the numerical spectral API.
    nx_graph.add_weighted_edges_from((a, b, float(c)) for a, b, c in graph.edges)
    matrix = from_networkx(nx_graph, vertices=graph.context.labels)
    numeric_tree = matrix.spanning_tree_centrality().scores.to_numpy()
    eigenvector = matrix.eigenvector_centrality().scores.to_numpy()
    assert all(isclose(float(x), y, abs_tol=1e-12) for x, y in zip(tree_scores, numeric_tree))
    assert sum(centroid) == sum(tree_scores) == 1
    assert isclose(sum(eigenvector), 1)
    return centroid, tree_scores, eigenvector

for name, graph in graphs.items():
    centroid, tree_scores, eigenvector = centralities(graph, spheres[name])
    if name == "P4":
        assert centroid == (Q(3, 20), Q(7, 20), Q(7, 20), Q(3, 20))
        assert tree_scores == (Q(1, 6), Q(1, 3), Q(1, 3), Q(1, 6))
    else:
        assert centroid == (Q(11, 20), Q(3, 20), Q(3, 20), Q(3, 20))
        assert tree_scores == (Q(1, 2), Q(1, 6), Q(1, 6), Q(1, 6))
    print(name, "  vertex   centroid   tree     eigenvector")
    for label, c, t, e in zip(vertices, centroid, tree_scores, eigenvector):
        print(f"     {label:>5} {str(c):>10} {str(t):>7} {e:>14.6f}")
```

## Two compactness measures

The path and star have the same number of vertices, total conductance, and resistance radius. Their radial compactness $\eta_\rho$ equals $1/2$. Kirchhoff compactness $\eta_K$ uses all pairwise resistances and gives $3/5$ for the path and $2/3$ for the star. Check that multiplying all conductances by $3$ preserves both dimensionless measures.

[[en/Resistance Geometry and Duality/Metric parameters/Density, Compactness, and Tree Invariance#Tree invariance|Related section of the note]].

```python
def compactness(graph, rho):
    R = resistance(graph).value.values
    n = len(graph.context.labels)
    mean_degree = 2 * sum(c for _, _, c in graph.edges) / n
    kirchhoff = sum(R[i][j] for i, j in combinations(range(n), 2))
    radial = Q((n - 1)**2, n**2) / (mean_degree * rho)
    by_kirchhoff = (n - 1)**2 / (mean_degree * kirchhoff)
    return radial, by_kirchhoff

assert compactness(path, spheres["P4"].resistance_radius) == (Q(1, 2), Q(3, 5))
assert compactness(star, spheres["K1,3"].resistance_radius) == (Q(1, 2), Q(2, 3))
for name, graph in graphs.items():
    radial, by_kirchhoff = compactness(graph, spheres[name].resistance_radius)
    scaled = network(vertices, tuple((a, b, 3 * c) for a, b, c in graph.edges))
    assert compactness(scaled, circumsphere(scaled).value.resistance_radius) == (radial, by_kirchhoff)
    print(f"{name}: eta_rho={radial}, eta_K={by_kirchhoff}")
```

## Two ways to remove a vertex

Keep vertices $a,b$ of the unit triangle. Deleting $c$ and its edges leaves the original edge of conductance $1$. Eliminating $c$ by Kron reduction gives conductance $3/2$ to preserve the original resistance. Compare radii and spanning-tree weights.

| Graph | $\tau$ | $\rho$ |
| --- | ---: | ---: |
| Original triangle | $3$ | $2/9$ |
| After deletion | $1$ | $1/4$ |
| After elimination | $3/2$ | $1/6$ |

[[en/Resistance Geometry and Duality/Metric parameters/Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius#Small examples|Related section of the note]].

```python
triangle = network(face, tuple((i, j, 1) for i, j in combinations(face, 2)))
remaining = ("a", "b")
deleted = induced_subgraph(triangle, remaining).value
eliminated = kron_reduce(triangle, remaining).value.network
variants = (("K3", triangle), ("Deletion", deleted), ("Elimination", eliminated))
tree_weights = tuple(spanning_tree_weight(graph).value for _, graph in variants)
radii = tuple(circumsphere(graph).value.resistance_radius for _, graph in variants)
assert tree_weights == (3, 1, Q(3, 2))
assert radii == (Q(2, 9), Q(1, 4), Q(1, 6))
assert tuple(value / tree_weights[0] for value in tree_weights[1:]) == (Q(1, 3), Q(1, 2))
assert tuple(value / radii[0] for value in radii[1:]) == (Q(9, 8), Q(3, 4))
for (label, _), tau, rho in zip(variants, tree_weights, radii):
    print(f"{label}: tau={tau}, rho={rho}")
```

## Centers of the two spheres

Use conductances $c_{ab}=7$ and $c_{ac}=c_{bc}=1$. Compare the center with bi-coordinates $\alpha$ in the resistance geometry with Gram matrix $\mathbf{Gr}$ and the center $\beta$ in the Laplacian geometry with Gram matrix $\mathbf L$. The coordinate of $\beta$ at $c$ is negative. Here $\rho$ and $\sigma$ are the squared radii in the two geometries.

[[en/Resistance Geometry and Duality/Metric parameters/Sphere Centers and Graph Heterogeneity#Exact examples and negative coordinates|Related section of the note]].

```python
weighted_triangle = network(face, (("a", "b", 7), ("a", "c", 1), ("b", "c", 1)))
resistance_sphere = circumsphere(weighted_triangle).value
laplacian_sphere = laplacian_circumsphere(weighted_triangle).value
alpha = resistance_sphere.center_coordinates.values
beta = laplacian_sphere.center_coordinates.values
assert alpha == (Q(4, 15), Q(4, 15), Q(7, 15))
assert resistance_sphere.resistance_radius == Q(32, 225)
assert beta == (Q(2, 3), Q(2, 3), Q(-1, 3))
assert laplacian_sphere.squared_radius == 8
print("alpha:", ", ".join(map(str, alpha)), "| rho =", resistance_sphere.resistance_radius)
print("beta: ", ", ".join(map(str, beta)), "| sigma =", laplacian_sphere.squared_radius)
```

## Degree potential on a path

Return to the unit path $a-b-c$. Its degrees are $(1,2,1)$, so the centered degree vector is $(-1,2,-1)/3$. Check that the potential $\varphi$ sums to zero and satisfies $\mathbf L\varphi=d-\bar d\mathbf1$. The middle vertex has the largest potential. Adding $\varphi/2$ to the uniform coordinates gives $\beta$.

[[en/Resistance Geometry and Duality/Metric parameters/Degree Potential and Centralities#A first calculation: a three-vertex path|Related section of the note]].

```python
short_path = network(face, (("a", "b", 1), ("b", "c", 1)))
phi = degree_potential(short_path).value.values
L = laplacian(short_path).value.values
degrees = tuple(row[i] for i, row in enumerate(L))
mean_degree = sum(degrees) / len(degrees)
source = tuple(value - mean_degree for value in degrees)
beta = laplacian_circumsphere(short_path).value.center_coordinates.values
assert sum(phi) == 0 and phi == (Q(-1, 9), Q(2, 9), Q(-1, 9))
assert tuple(sum(x * y for x, y in zip(row, phi)) for row in L) == source
assert beta == (Q(5, 18), Q(4, 9), Q(5, 18))
print("phi:", ", ".join(map(str, phi)))
print("beta:", ", ".join(map(str, beta)))
```

## Norm of the internal Laplacian

In the unit cycle $C_4$, compare an adjacent pair, an opposite pair, and a triple. For each group, build the form of its internal edges in the original context and evaluate it in the full cycle's metric. Check the result against the sum of $c_{ij}R_{ij}$ over the internal edges. The triple has norm $3/2$ in the full cycle and $2$ in the metric of its own induced graph.

[[en/Resistance Geometry and Duality/Metric parameters/Norms of Subgraph Laplacians#A triangle and a square|Related section of the note]].

```python
cycle = network(vertices, (("a", "b", 1), ("b", "c", 1), ("c", "d", 1), ("d", "a", 1)))

def internal_norm(graph, labels):
    # Keep the original vertex context so the form is evaluated in G.
    selected = set(labels)
    edges = tuple(edge for edge in graph.edges if edge[0] in selected and edge[1] in selected)
    internal = Network(graph.context, edges, graph.policy)
    value = evaluate_form(graph, laplacian_form(internal).value).value
    pairs = tuple((i, j) for i, j, _ in edges)
    pair_resistances = resistance(graph, pairs=pairs).value.values
    assert value == sum(edge[2] * r for edge, r in zip(edges, pair_resistances))
    return value

for selected, expected in (
    (("a", "b"), Q(3, 4)), (("a", "c"), 0), (face, Q(3, 2)), (vertices, 3),
):
    value = internal_norm(cycle, selected)
    assert value == expected
    print("".join(selected), ":", value)

induced = induced_subgraph(cycle, face).value
assert internal_norm(induced, face) == 2
print("abc evaluated in its own induced graph:", internal_norm(induced, face))
```
