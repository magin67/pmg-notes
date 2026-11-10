---
title: "Example: Subspaces and Graph Transformations"
date: 2026-11-10
updated: 2026-11-10
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-spaces
lang: en
description: "Exact calculations for subspaces, the Dirichlet problem, and graph transformations."
order: 7
---

Two paths, a star, and a bipartite graph illustrate the Spaces series. We begin with the subspace metric, coordinates, and the form of a midpoint, then compare graph operations.

[[ru/PythonExamples/Пример - Подпространства и преобразования графов|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom with version 0.9.0. See [[Installing the Library and Running Examples]].

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/spaces.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/spaces.ipynb)

## The metric on a selected subspace

Take the path $a-b-c$ with unit conductances and vectors $u=b-a$, $v=c-b$. The vertices $a,c$ give the direction $c-a=u+v$. Compute the squared norms of this vector and the boundary $(abc)$ using normalized potentials of the metric polyform. The Green matrix provides a separate check.

[[en/Resistance Geometry and Duality/Spaces/Basis#A direct calculation on the path|Related section of the note]].

```python
from fractions import Fraction as Q
from sympy import Matrix
from polyform_algebra.core import (
    INFINITY, Atom, Boundary, Context, boundary, contract, coordinates,
    dirichlet, equivalent, evaluate_form, form_exp, gram, induced_subgraph,
    kron_reduce, laplacian, laplacian_form, network, polar_form, potential,
    resistance, spanning_coefficient, spanning_tree_weight, square, wedge,
)

def difference(net, start, end):
    return coordinates(net.context, {
        label: int(label == end) - int(label == start)
        for label in net.context.labels
    })

unit_path = network(("a", "b", "c"), (("a", "b", 1), ("b", "c", 1)))
u = difference(unit_path, "a", "b")
v = difference(unit_path, "b", "c")
assert gram(unit_path, (u, v)).value.values == ((1, 0), (0, 1))

metric = form_exp(laplacian_form(unit_path).value).value
a_index, b_index, c_index = (unit_path.context.labels.index(label) for label in ("a", "b", "c"))
edge_form = square(Boundary(unit_path.context, (a_index, c_index))).value
triangle_form = square(Boundary(unit_path.context, (a_index, b_index, c_index))).value
tau = spanning_coefficient(metric).value
line_norm = potential(metric, edge_form).value / tau
boundary_norm = potential(metric, triangle_form).value / tau
assert tau == 1
assert line_norm == evaluate_form(unit_path, edge_form).value == 2
assert boundary_norm == evaluate_form(unit_path, triangle_form).value == 1
print("R_ac =", line_norm, "| (abc)^2 =", boundary_norm)
```

## Bi-coordinates and di-coordinates

On the same path, $u,v$ are orthogonal unit vectors. Use the basis $h_1=u$, $h_2=u+v$ and the object $v$. Its bi-coordinates $\mathbf b$ give the expansion coefficients, while its di-coordinates $\mathbf d$ are inner products with the basis vectors. The package computes the Gram matrix and the di-coordinates, and SymPy solves $\mathbf G\mathbf b=\mathbf d$.

[[en/Resistance Geometry and Duality/Spaces/Bi-coordinates and Di-coordinates#An example with a nonorthogonal basis|Related section of the note]].

```python
basis = (u, u + v)
G = Matrix(gram(unit_path, basis).value.values)
di = Matrix(gram(unit_path, basis, (v,)).value.values)
bi = G.LUsolve(di)
reciprocal = (u - v, v)

assert tuple(bi) == (-1, 1) and tuple(di) == (0, 1)
assert bi[0] * basis[0] + bi[1] * basis[1] == v
assert gram(unit_path, basis, reciprocal).value.values == ((1, 0), (0, 1))
print("G =", G.tolist(), "| b =", tuple(bi), "| d =", tuple(di))
```

## The form of a midpoint

Let $q=(a+c)/2$. The package computes the polar form $\{q,q\}=2[q]^2$. Compare its half with the atomic part minus the difference part. The check compares formal coefficients before a metric is chosen.

$$
[q]^2=\frac12[a]^2+\frac12[c]^2-\frac14[(ac)]^2
$$

[[en/Resistance Geometry and Duality/Spaces/Decomposing a Form into Atomic and Difference Parts#Decomposing a form using frame elements and their differences|Related section of the note]].

```python
context = unit_path.context
a = Atom(context, a_index)
c = Atom(context, c_index)
q = (a.as_exterior() + c.as_exterior()) * Q(1, 2)
midpoint_square = polar_form(q, q).value * Q(1, 2)
atomic = (square(a).value + square(c).value) * Q(1, 2)
difference_part = edge_form * Q(1, 4)
assert equivalent(midpoint_square, atomic - difference_part).value
print("[q]^2 = ([a]^2 + [c]^2)/2 - [(ac)]^2/4")
```

## Boundary and affine weight

Assign affine weights $\epsilon(a)=\epsilon(b)=1$, $\epsilon(z)=0$. The Leibniz rule gives $\partial z=0$ and $\partial(az)=z$. Here the context specifies the affine weight. The relation $z^2=0$ in the isotropic metric requires a separately specified inner product.

[[en/Resistance Geometry and Duality/Spaces/The Null Vector, Isotropic Representation, and the Boundary|Note on the null vector]].

```python
affine_context = Context(("a", "b", "z"), epsilon=(1, 1, 0))
a = Atom(affine_context, affine_context.labels.index("a"))
z = Atom(affine_context, affine_context.labels.index("z"))
az = wedge(a, z).value

assert not boundary(z).value.coefficients
assert boundary(az).value == z.as_exterior()
assert not boundary(boundary(az).value).value.coefficients
print("∂z = 0; ∂(az) = z")
```

## The Dirichlet problem on a weighted path

On the path $a-x-y-b$ with conductances $2,1,3$, prescribe $f_a=0$, $f_b=11$. The matrix $\mathbf B$ shows how the prescribed values determine $f_x,f_y$. Check the solution with the internal current equations and sum the energy over the edges.

[[en/Resistance Geometry and Duality/Spaces/Selected Vertices and the Dirichlet Problem#Matrix notation for computation|Related section of the note]].

```python
path = network(("a", "x", "y", "b"), (("a", "x", 2), ("x", "y", 1), ("y", "b", 3)))
selected = ("a", "b")
solution = dirichlet(path, selected).value
values = solution.extend({"a": 0, "b": 11}).value
f = dict(zip(path.context.labels, values.values))
energy = sum(c * (f[u] - f[v])**2 for u, v, c in path.edges)
net_currents = Matrix(laplacian(path).value.values) * Matrix(values.values)

assert solution.I == ("x", "y")
assert solution.B.values == ((Q(8, 11), Q(3, 11)), (Q(2, 11), Q(9, 11)))
assert f == {"a": 0, "x": 3, "y": 9, "b": 11}
assert tuple(net_currents) == (-6, 0, 0, 6)
assert energy == 66
print("B =", [[str(value) for value in row] for row in solution.B.values])
print("f:", ", ".join(f"{label}={value}" for label, value in f.items()))
print("Energy =", energy)
```

## Deletion, contraction, and elimination

Keep $a,b$ on the same path and compare three operations. Deleting $x,y$ disconnects the path. Contraction identifies $x$ with $a$ and $y$ with $b$. Kron reduction preserves the resistance between $a,b$.

| Operation | Conductance of $ab$ | Resistance $R_{ab}$ |
| --- | ---: | ---: |
| Deletion | No edge | $\infty$ |
| Contraction | $1$ | $1$ |
| Elimination | $6/11$ | $11/6$ |

Contraction can also glue separate edges $ab$ and $cd$ at a shared vertex $s$. For conductances $2$ and $3$, the new path has spanning-tree weight $6$ and endpoint resistance $1/2+1/3=5/6$.

[[en/Resistance Geometry and Duality/Spaces/Vertex Contraction and Graph Gluing#Gluing at a single vertex|Related section of the note]].

```python
deleted = induced_subgraph(path, selected).value
contracted = contract(path, {"a": ("a", "x"), "b": ("y", "b")}).value.network
reduced = kron_reduce(path, selected).value.network

def pair_resistance(net, start, end):
    return resistance(net, pairs=((start, end),)).value.values[0]

assert deleted.edges == () and pair_resistance(deleted, "a", "b") == INFINITY
assert contracted.edges == (("a", "b", 1),)
assert reduced.edges == (("a", "b", Q(6, 11)),)
assert pair_resistance(contracted, "a", "b") == 1
assert pair_resistance(reduced, "a", "b") == pair_resistance(path, "a", "b") == Q(11, 6)
print("R_ab:", {
    "deletion": "∞",
    "contraction": str(pair_resistance(contracted, "a", "b")),
    "elimination": str(pair_resistance(reduced, "a", "b")),
})

separate = network(("a", "b", "c", "d"), (("a", "b", 2), ("c", "d", 3)))
glued = contract(separate, {"a": ("a",), "s": ("b", "c"), "d": ("d",)}).value.network
assert spanning_tree_weight(glued).value == 6
assert pair_resistance(glued, "a", "d") == Q(5, 6)
print("a–s–d: tau =", spanning_tree_weight(glued).value, "| R_ad =", pair_resistance(glued, "a", "d"))
```

## Eliminating the center of a star

Eliminate the center $x$ of a star with leaves $a,b,c$ and unit conductances. This gives a triangle with induced conductance $1/3$ on each edge. Check that the resistance of each leaf pair stays at $2$ and that the triangle has spanning-tree weight $1/3$.

[[en/Resistance Geometry and Duality/Spaces/Vertex Elimination and Induced Couplings#A star becomes a triangle|Related section of the note]].

```python
leaves = ("a", "b", "c")
star = network(leaves + ("x",), tuple((leaf, "x", 1) for leaf in leaves))
triangle = kron_reduce(star, leaves).value.network

assert triangle.edges == (("a", "b", Q(1, 3)), ("a", "c", Q(1, 3)), ("b", "c", Q(1, 3)))
for start, end, _ in triangle.edges:
    assert pair_resistance(star, start, end) == pair_resistance(triangle, start, end) == 2
assert spanning_tree_weight(triangle).value == Q(1, 3)
print(", ".join(f"c_{u}{v}={weight}" for u, v, weight in triangle.edges), "| R_ab = 2")
```

## Both parts of a bipartite graph

Use this participation table for employees $a,b$ and documents $x,y$.

| Employee | $x$ | $y$ |
| --- | ---: | ---: |
| $a$ | $1$ | $1$ |
| $b$ | $2$ | $0$ |

A zero denotes an absent edge. Keeping the employees gives conductance $c_{ab}=2/3$. Keeping the documents gives $c_{xy}=1/2$. Each elimination preserves the resistances within the selected part.

[[en/Resistance Geometry and Duality/Spaces/Couplings Within One Part of a Bipartite Graph#Two induced graphs|Related section of the note]].

```python
people = ("a", "b")
documents = ("x", "y")
participation = network(people + documents, (("a", "x", 1), ("a", "y", 1), ("b", "x", 2)))
people_graph = kron_reduce(participation, people).value.network
document_graph = kron_reduce(participation, documents).value.network

assert people_graph.edges == (("a", "b", Q(2, 3)),)
assert document_graph.edges == (("x", "y", Q(1, 2)),)
assert pair_resistance(people_graph, "a", "b") == pair_resistance(participation, "a", "b") == Q(3, 2)
assert pair_resistance(document_graph, "x", "y") == pair_resistance(participation, "x", "y") == 2
print("c_ab =", people_graph.edges[0][2], "| c_xy =", document_graph.edges[0][2])
```
