---
title: 'Example: Digraph Polyforms'
date: 2026-11-21
updated: 2026-11-21
revision: 1
translated_revision: 1
status: published
text_prepared_by: ChatGPT
translation_key: python-digraph-polyforms
lang: en
description: Five exact calculations from the outgoing Laplacian to one-way resistance, reconstruction and boundary norms.
order: 24
---

The same arrow gives two different calculations. Increasing the weight of $a\to b$ changes the rooted potentials by $(0,2,1)$ per unit of added weight. Measuring that direction gives the number $1/4$. We compute both from the same graph, then use the resistance table to recover its arcs and measure a boundary.

[[ru/PythonExamples/Пример - Полиформы орграфов|Русский]] · [[en/PythonExamples/PythonExamples|Programming examples]]

Run the cells from top to bottom. The notebook installs the exact revision of the package. [polyform_algebra f84dc6a](https://github.com/magin67/polyform_algebra/commit/f84dc6abefcc6adaea313f97395eeb0587b337ea).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/digraph-polyforms.ipynb) · [Download the notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/digraph-polyforms.ipynb)

## 1. From arcs to the polyform

Specify six arcs. The pair $(b,a)$ denotes an arc from $b$ to $a$ and changes row $b$ of the Laplacian. At $b$ the outgoing weight is 3 and the incoming weight is 2.

![[en/Directed Graphs/Digraph Polyforms/images/weighted-unbalanced-digraph.svg|Six arcs on a, b and c; b to a and a to c have weight two]]

Write $M=\exp L$ grade by grade in vertex order $a,b,c$. Grade two has rows and columns in the order $a\wedge b,a\wedge c,b\wedge c$. In this basis the boundary $(abc)$ has coordinates $(1,-1,1)$.

[[en/Directed Graphs/Digraph Polyforms/How Arcs Form the Polyform of a Digraph|How Arcs Form the Polyform of a Digraph]] · [[en/Directed Graphs/Digraph Polyforms/Computing a Rooted Spanning-Tree Potential from a Digraph Polyform|Computing a Rooted Spanning-Tree Potential from a Digraph Polyform]]

```python
from itertools import combinations
from IPython.display import Math, display
from sympy import Matrix, Rational, eye, latex, ones, symbols, zeros
from polyform_algebra.core import DomainError
from polyform_algebra.directed import DirectedNetwork

a, b, c, d, e = tuple("abcde")
vertices = (a, b, c)
arcs = ((a, b, 1), (b, a, 2), (a, c, 2), (c, a, 1), (b, c, 1), (c, b, 1))
graph = DirectedNetwork(vertices, arcs)
L = graph.laplacian()
M2 = graph.polyform_grade(2)
boundary = Matrix([[1, -1, 1]])
assert graph.polyform_grade(0) == eye(1)
assert graph.polyform_grade(1) == L
assert graph.polyform_grade(3) == zeros(1)
assert M2 == M2[:, 0] * boundary
display(Math("L=" + latex(L) + r",\qquad M_2=" + latex(M2)))
# Present the left blade in cyclic order bc, ca, ab.
bc, ca, ab = M2[2, 0], -M2[1, 0], M2[0, 0]
display(Math(r"M=e+L+[" + rf"{bc}\,b\wedge c+{ca}\,c\wedge a+{ab}\,a\wedge b"
             + r",\,(abc)]"))
```

```python
# On three vertices two arcs form a tree if their tails differ and they do not form a cycle.
tree_weights = {v: [] for v in vertices}
for (i, j, w), (k, m, z) in combinations(arcs, 2):
    if i == k or (i, j) == (m, k):
        continue
    root, = set(vertices) - {i, k}
    tree_weights[root].append(w * z)
tau = graph.tree_potentials()
assert Matrix(tau).T * L == zeros(1, 3)
assert tuple(map(sum, tree_weights.values())) == (bc, ca, ab) == tau == (5, 4, 7)
for root in vertices:
    print(root, sorted(tree_weights[root]), "→", sum(tree_weights[root]))
```

## 2. Strengthening an arc and measuring a pair

In the arc form $H_{a\to b}=[a,a-b]$ the left argument is vertex $a$. In the measurement form $\Phi_{ab}=[b-h,b-a]$ it is the vector from the centroid of all vertices to $b$. Each method returns two coordinate columns $(x,y)$ in vertex order. The form has matrix $xy^{\mathsf T}$.

First add $t$ to the arc weight. Compute the principal minor for each root and independently compare its linear coefficient with the package result.

[[en/Directed Graphs/Digraph Polyforms/The Arc Form and the One-Way Resistance Form|The Arc Form and the One-Way Resistance Form]] · [[en/Directed Graphs/Digraph Polyforms/How to Normalize One-Way Resistance in an Unbalanced Digraph|How to Normalize One-Way Resistance in an Unbalanced Digraph]]

```python
t = symbols("t")
x, y = graph.arc_form(a, b)
changed = L + t * x * y.T
root_polynomials = tuple(changed.minor_submatrix(i, i).det().expand() for i in range(3))
increments = graph.root_coefficients(x, y)
assert increments == (0, 2, 1)
assert root_polynomials == tuple(old + t * inc for old, inc in zip(tau, increments))
display(Math(r"(\tau_a(t),\tau_b(t),\tau_c(t))=" + latex(root_polynomials)))
```

```python
# Keep the same graph and evaluate the two ordered pairs.
for start, target in [(a, b), (b, a)]:
    form = graph.measurement_form(start, target)
    u = graph.root_coefficients(*form)
    r = graph.normalized_potential(*form)
    assert r == sum(u) / sum(tau)
    print(f"{start} → {target}   u = {u}   r = {r}")

resistances = graph.one_way_resistances()
_, ab_vector = graph.measurement_form(a, b)
assert (resistances[0, 1], resistances[1, 0]) == (Rational(1, 4), Rational(3, 16))
pair = graph.normalized_potential(ab_vector, ab_vector)
assert resistances[0, 1] + resistances[1, 0] == pair == Rational(7, 16)
display(Math(r"r_{ab}+r_{ba}=" + latex(pair)))
```

## 3. Which roots enter the sum?

The only spanning tree of the unit path $a\to b\to c\to d$ points toward $d$. Print the contributions from **all** roots for both directions of its inner edge and both directions between its endpoints. For $(bc)$ the contributions from $b$ and $d$ cancel.

The fork $b\leftarrow a\to c$ has two sinks. Its polyform and cofactors exist, but $S=0$, so the normalized pair measurement is undefined.

[[en/Directed Graphs/Digraph Polyforms/Computing a Rooted Spanning-Tree Potential from a Digraph Polyform|Computing a Rooted Spanning-Tree Potential from a Digraph Polyform]] · [[en/Directed Graphs/Digraph Polyforms/How to Normalize One-Way Resistance in an Unbalanced Digraph|How to Normalize One-Way Resistance in an Unbalanced Digraph]]

```python
def unit_path(labels, closed=False):
    targets = labels[1:] + (labels[:1] if closed else ())
    return DirectedNetwork(labels, [(i, j, 1) for i, j in zip(labels, targets)])

chain = unit_path((a, b, c, d))
assert chain.tree_potentials() == (0, 0, 0, 1)
for i, j, expected in [(b, c, 0), (c, b, 1), (a, d, 3), (d, a, 1)]:
    form = chain.measurement_form(i, j)
    u = chain.root_coefficients(*form)
    value = chain.normalized_potential(*form)
    assert value == expected
    print(f"{i} → {j}   u = {u}   r = {value}")
fork = DirectedNetwork(vertices, ((a, b, 1), (a, c, 1)))
assert fork.tree_potentials() == (0, 0, 0)
try:
    fork.one_way_resistances()
except DomainError:
    print("S = 0  →  undefined")
else:
    raise AssertionError("S = 0")
```

## 4. Recovering the graph and measuring two vectors

From the table $\mathbf r$ compute $\mathbf K=(-\mathbf J\mathbf r)^+$, where $\mathbf J$ subtracts the mean. This recovers Laplacian row differences. The shares $\pi_i=\tau_i/S$ supply the common row correction. On **two** vertices, exchanging the root shares will recover opposite arcs from the same table.

The directed scalar product requires only the table. Its first argument $u$ goes on the right in $-\mathbf v^{\mathsf T}\mathbf r\mathbf u$.

[[en/Directed Graphs/Digraph Polyforms/Can the One-Way Resistance Matrix Recover a Digraph|Can the One-Way Resistance Matrix Recover a Digraph?]] · [[en/Directed Graphs/Digraph Polyforms/Computing the Directed Scalar Product of Two Vectors in a Digraph|Computing the Directed Scalar Product of Two Vectors in a Digraph]]

```python
J = eye(3) - ones(3) / 3
K = (-J * resistances).pinv()
pi = Matrix(tau) / sum(tau)
restored = DirectedNetwork.from_one_way_resistances(vertices, resistances, pi)
assert K == J * L
assert K - ones(3, 1) * pi.T * K == restored.laplacian() == L
assert restored.arcs == graph.arcs
display(Math(r"\mathbf r=" + latex(resistances) + r",\qquad\mathbf K=" + latex(K)))
display(Math(r"\mathbf L_{\rm recovered}=" + latex(restored.laplacian())))
same_table = [[0, 1], [1, 0]]
for shares in [(0, 1), (1, 0)]:
    candidate = DirectedNetwork.from_one_way_resistances((a, b), same_table, shares)
    assert candidate.one_way_resistances() == Matrix(same_table)
    print(shares, "→", candidate.arcs)
```

```python
_, u = graph.measurement_form(a, b)
_, v = graph.measurement_form(a, c)
for left, right, expected in [(u, v, Rational(1, 4)), (v, u, Rational(1, 8))]:
    value = graph.directed_scalar_product(left, right)
    assert value == -(right.T * resistances * left)[0] == graph.normalized_potential(left, right)
    assert value == expected
    print(value)
```

## 5. Measuring a boundary by starts and by its Gram matrix

Measure the triangle $(abc)$ and then the tetrahedron $(abcd)$ in a directed four-cycle. Insert an external vertex $e$ between $d$ and $a$ and measure the tetrahedron again. The vertex list selects the boundary. The centroid still uses the entire digraph.

![[en/Directed Graphs/Digraph Polyforms/images/tetrahedron-in-directed-cycles-en.svg|Tetrahedron abcd in two directed cycles, with e inserted on the return path]]

For each boundary the package computes the contribution from each start. Independently check the full norm with the Gram matrix assembled directly from the resistance table. The last calculation reverses the triangle orientation while keeping its start fixed.

[[en/Directed Graphs/Digraph Polyforms/What Does the Product of Two Side Forms of a Triangle Measure|What Does the Product of Two Side Forms of a Triangle Measure?]] · [[en/Directed Graphs/Digraph Polyforms/Computing the Norm of a Boundary of Any Grade in a Digraph|Computing the Norm of a Boundary of Any Grade in a Digraph]]

```python
square = unit_path((a, b, c, d), closed=True)
pentagon = unit_path((a, b, c, d, e), closed=True)
for net, boundary_labels, numerators in [
    (square, (a, b, c), (1, 1, 2)),
    (square, (a, b, c, d), (1, 1, 1, 1)),
    (pentagon, (a, b, c, d), (1, 1, 1, 2)),
]:
    start = boundary_labels[0]
    directions = Matrix.hstack(*(net.measurement_form(start, j)[1] for j in boundary_labels[1:]))
    gram = -directions.T * net.one_way_resistances().T * directions
    parts = net.boundary_contributions(boundary_labels)
    assert list(parts.values()) == [Rational(x, len(net.labels)) for x in numerators]
    assert sum(parts.values()) == net.boundary_norm(boundary_labels) == gram.det() == 1
    print(f"{''.join(net.labels)} / {''.join(boundary_labels)}   {parts}   det = {gram.det()}")
assert square.boundary_contributions((a, b, c))[a] == square.boundary_contributions((a, c, b))[a]
```

Check the contribution from start $c$ directly. Each rank-one perturbation enters a minor linearly, so the four evaluations below extract exactly the mixed coefficient.

```python
# Independent coefficient of t1*t2 from principal minors, for start c of (cab).
def root_total(matrix):
    return sum(matrix.minor_submatrix(i, i).det() for i in range(matrix.rows))

x1, y1 = square.measurement_form(c, a)
x2, y2 = square.measurement_form(a, b)
A = square.laplacian()
F1, F2 = x1 * y1.T, x2 * y2.T
mixed = root_total(A + F1 + F2) - root_total(A + F1) - root_total(A + F2) + root_total(A)
direct = mixed / root_total(A)
assert direct == square.boundary_contributions((c, a, b))[c] == Rational(1, 2)
display(Math(r"P_M^\Sigma(\Phi_{ca}\Phi_{ab})=" + latex(direct)))
```

Moving the start from $a$ to $c$ in the triangle changes its contribution from $1/4$ to $1/2$. Reversing orientation at fixed $a$ leaves its contribution equal to $1/4$. Inserting $e$ changes the tetrahedron’s shares while its full norm remains 1.
