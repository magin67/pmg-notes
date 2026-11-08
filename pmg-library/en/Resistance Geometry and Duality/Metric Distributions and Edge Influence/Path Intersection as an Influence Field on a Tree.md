---
title: Path Intersection as an Influence Field on a Tree
date: 2026-11-03
updated: 2026-11-08
revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 5
translation_key: metric-distributions-tree-path-influence
order: 2
description: "The common segment of two paths as the exact support of existing-edge influence on their inner product: directions, resistances, and finite changes."
---

[[ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/Пересечение путей как поле влияния на дереве|Русский]]


On a tree there is a unique path between any two vertices. For two vectors specified by vertex pairs, the metric distribution selects the edges shared by their paths. Changing precisely these existing edges affects the inner product. Directions determine the sign of influence, and conductances determine the size of each contribution.

We use the operator from [[Edge Influence and Metric Distribution]]. The graph here is a finite undirected tree with positive conductances. The vectors and measured form remain fixed in every probe.

We first vary only existing-edge conductances while keeping the tree connected. Adding a new coupling can create a cycle; that different case is discussed at the end of the note.

## The common segment of two paths

Take the path $a-b-c-d-e$ with unit conductances and the vectors

$$
v=(ad),\qquad u=(be),\qquad f=\frac12\{v,u\}
$$

The vector $(ad)=d-a$ is directed from $a$ to $d$. The polar form is defined by $\{v,u\}=[v,u]+[u,v]$, so half of it has metric evaluation $N_L(f)=v\cdot u$.

The paths $a-b-c-d$ and $b-c-d-e$ share the segment $b-c-d$. Both traverse it from $b$ to $d$. The distribution and its coefficient sum are

$$
D_L(f)=[(bc)]^2+[(cd)]^2,\qquad N_L(f)=v\cdot u=2
$$

![The common segment, opposite directions, and one shared vertex](<images/Path Directions on a Tree.svg>)

*Each diagram shows the same unit path. Arrows above it indicate the selected paths; thick edges mark their intersection. The sign belongs to the distribution coefficients, not to the graph conductances.*

Reverse the second vector, replacing $u=(be)$ by $u=(eb)$. The common segment remains, but the paths now traverse it in opposite directions:

$$
D_L\left(\frac12\{(ad),(eb)\}\right)=-[(bc)]^2-[(cd)]^2,\qquad (ad)\cdot(eb)=-2
$$

For vectors $(ac)$ and $(ce)$, the paths share only vertex $c$. They have no common edges, so both the distribution and the inner product are zero. The same holds if the paths do not meet at all.

## Why only common edges remain

Give each edge $\ell$ an arbitrary auxiliary orientation and the corresponding vector $a_\ell$. Denote its conductance by $c_\ell>0$, its own resistance by $r_\ell=1/c_\ell$, and its edge form by $q_\ell=[a_\ell]^2$. Then

$$
L=\sum_\ell c_\ell q_\ell
$$

The letter $\ell$ indexes an edge; the symbol $e$ remains reserved for the unit form of PMG.

> [!info] The edge basis of a tree
> **Lemma.** The edge vectors of a tree form an orthogonal basis of the affine-vector space in the resistance metric:
>
> $$
> a_\ell\cdot a_k=\begin{cases}1/c_\ell,&\ell=k\\0,&\ell\ne k\end{cases}
> $$
>
> In particular, the effective resistance between an edge's endpoints equals its own resistance: $R_\ell=r_\ell$.

This is a property of the resistance metric, not of the angles between lines in the drawing. Its electrical basis is the unique path and the absence of current in side branches. The classical resistance formula for a tree is given by Ghosh, Boyd, and Saberi, [Minimizing Effective Resistance of a Graph](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf), Section 2.3.

> [!note]- Proof using edge coordinates
> **Proof.** Delete the coordinate of one reference vertex. Let the columns of the square matrix $\mathbf B$ be the remaining coordinates of the edge vectors, and let $\mathbf C=\operatorname{diag}(c_\ell)$. For a tree, $\mathbf B$ is invertible: the edges are independent and span all vertex differences. The reduced Laplacian is $\widehat{\mathbf L}=\mathbf B\mathbf C\mathbf B^{\mathsf T}$. Hence the Gram matrix of the edge vectors is
>
> $$
> \mathbf B^{\mathsf T}\widehat{\mathbf L}^{-1}\mathbf B=\mathbf C^{-1}
> $$
>
> This is the required diagonal matrix. The inner-product formula using the inverse reduced Laplacian is equivalent to the metric in [[Inner Product of Graph Vectors]]. $\square$

Expand the selected vectors in this basis:

$$
v=\sum_\ell x_\ell a_\ell,\qquad u=\sum_\ell y_\ell a_\ell
$$

For a vector specified by two vertices, $x_\ell$ is $1$ if the path traverses the edge in its auxiliary orientation, $-1$ if it traverses it against that orientation, and $0$ if it does not use the edge. The expansion is obtained by adding vertex differences along the path; intermediate vertices cancel. The same rule holds for $y_\ell$.

The lemma gives

$$
v\cdot a_\ell=\frac{x_\ell}{c_\ell},\qquad
u\cdot a_\ell=\frac{y_\ell}{c_\ell}
$$

Substitute these expressions into the coefficient formula in the [[Edge Influence and Metric Distribution#The metric distribution operator|definition of metric distribution]]:

$$
m_\ell(f)=c_\ell(v\cdot a_\ell)(u\cdot a_\ell)=\frac{x_\ell y_\ell}{c_\ell}
$$

> [!info] Intersection as the support of the distribution
> **Theorem.** For two vectors specified by vertex pairs on a tree,
>
> $$
> \boxed{D_L(f)=\sum_\ell\frac{x_\ell y_\ell}{c_\ell}q_\ell},\qquad
> \boxed{v\cdot u=\sum_\ell\frac{x_\ell y_\ell}{c_\ell}}
> \tag{1}
> $$
>
> The nonzero coefficients occur exactly on the common path edges. A coefficient is $+r_\ell$ when the directions agree and $-r_\ell$ when they are opposite.

> [!note]- Proof of the intersection formula
> **Proof.** The coefficient formula has already been obtained from orthogonality. If either path does not use an edge, the product $x_\ell y_\ell$ is zero. On a shared edge it is $1$ or $-1$. Expanding the inner product in the orthogonal basis gives the second equality in (1). The common part of two simple paths in a tree is connected: whenever two vertices belong to both paths, both contain the unique path between them. Thus a nonempty edge intersection is a single path, and the relative direction is constant throughout that segment. $\square$

The inner product is therefore the sum of the resistances along the common segment, with one overall sign. If this sum is called the resistance length of the path, it must be distinguished from the linear norm $\sqrt{v^2}$: in PMG, the norm $v^2=v\cdot v$ itself is quadratic. With unit conductances, the resistance sum equals the number of edges.

Reversing one of the **selected paths** changes the sign of the result; reversing both preserves it. Reversing an **auxiliary edge orientation** simultaneously negates $a_\ell,x_\ell,y_\ell$. The product $x_\ell y_\ell$ and the form $q_\ell$ are unchanged. These two operations on directions have different meanings.

### A tree with a side branch

Add an edge $cz$ from the path $a-b-c-d-e$ to a new vertex $z$. All conductances are $1$. For $v=(ad)$ and $u=(be)$, the paths still share exactly $bc,cd$. Branch $cz$ belongs to neither path, so $m_{cz}=0$. Changing its positive conductance leaves $v\cdot u=2$ unchanged.

![A Side Branch and Shared Edges](<images/A Side Branch and Shared Edges.svg>)

*Orange edges contribute $1$ each; all other edges contribute zero. Drawing angles show the tree structure, not angles in resistance geometry.*

## Unequal conductances

Keep $v=(ad)$ and $u=(be)$, and assign conductances

$$
c_{ab}=3,\qquad c_{bc}=2,\qquad c_{cd}=\frac12,\qquad c_{de}=4
$$

![Conductances and contributions along the common segment](<images/Conductances and Path Intersection.svg>)

*The upper path shows the conductances of the initial tree. Below it, only the shared edges remain, labeled by distribution coefficients. A thicker edge indicates a larger coefficient magnitude, not a larger conductance.*

Choose auxiliary orientations from left to right:

| Edge | $c_\ell$ | $x_\ell$ | $y_\ell$ | $m_\ell=x_\ell y_\ell/c_\ell$ |
|---|---:|---:|---:|---:|
| $ab$ | $3$ | $1$ | $0$ | $0$ |
| $bc$ | $2$ | $1$ | $1$ | $1/2$ |
| $cd$ | $1/2$ | $1$ | $1$ | $2$ |
| $de$ | $4$ | $0$ | $1$ | $0$ |

We obtain

$$
D_L(f)=\frac12[(bc)]^2+2[(cd)]^2,\qquad N_L(f)=\frac12+2=\frac52
$$

The paths and the support of their intersection are unchanged. The metric contributions have changed: edge $cd$ conducts less well and has greater resistance, so its contribution is larger. Conductances outside the common segment do not affect this inner product.

By the [[Edge Influence and Metric Distribution#Value of the output form|output evaluation formula]], this example gives

$$
N_L(D_L(f))=\sum_\ell\frac{x_\ell y_\ell}{c_\ell^2}=\frac14+4=\frac{17}4
$$

In the unit example, this evaluation equaled the original $N_L(f)$ because every edge had norm $1$.

## Detecting the intersection by edge probes

Now test each existing edge in turn, returning to the initial tree every time. Under the change $c_\ell\mapsto c_\ell+t$, with $t>-c_\ell$, the paths and their coordinates remain unchanged. Only one term in the sum (1) changes:

$$
\begin{aligned}
\Delta_\ell(t;f)&=x_\ell y_\ell\left(\frac1{c_\ell+t}-\frac1{c_\ell}\right)\\
&=-\frac{t\,x_\ell y_\ell}{c_\ell(c_\ell+t)}
\end{aligned}
\tag{2}
$$

The inequality is strict: deleting an edge disconnects the tree and leaves the connected-metric setting considered here.

> [!info] The influence field on a tree
> **Corollary.** For any nonzero admissible change of an existing edge, the finite influence on $f=\{v,u\}/2$ is nonzero if and only if the edge belongs to both paths. For the same relative change $t=\varepsilon c_\ell$, $\varepsilon>-1$,
>
> $$
> \boxed{\Delta_\ell(\varepsilon c_\ell;f)=-\frac{\varepsilon}{1+\varepsilon}m_\ell(f)}
> \tag{3}
> $$

Formulas (2)-(3) follow directly from (1) and agree with the general finite-influence formula, since on a tree $R_\ell=1/c_\ell$.

In our weighted example, double each conductance independently, taking $\varepsilon=1$. Then $\Delta_\ell=-m_\ell/2$:

| Probe | New value $N'(f)$ | Finite influence |
|---|---:|---:|
| $c_{ab}:3\to6$ | $5/2$ | $0$ |
| $c_{bc}:2\to4$ | $9/4$ | $-1/4$ |
| $c_{cd}:1/2\to1$ | $3/2$ | $-1$ |
| $c_{de}:4\to8$ | $5/2$ | $0$ |

![Independent edge strengthening and the change in the inner product](<images/Edge Probes on a Tree.svg>)

*In each row only the highlighted conductance is doubled. On the right are the new inner product and its difference from the initial $5/2$. Probes outside the intersection give zero; within the common segment, the less conductive edge produces the larger response to equal relative strengthening.*

The common segment is selected because **among existing edges, only its edges affect this form at all**, rather than because they have the "strongest" influence. Within that segment, magnitudes are compared under a specified change rule. The magnitude of relative sensitivity is $1/c_\ell$; the derivative with respect to absolute conductance has magnitude $1/c_\ell^2$.

For oppositely directed paths, $m_\ell<0$. Strengthening a common edge then gives positive $\Delta_\ell$: the negative inner product moves toward zero. The geometric segment stays the same while its resistance length decreases.

On a tree the formula also separates by edges under simultaneous changes: $N_{L'}(f)=\sum_\ell x_\ell y_\ell/(c_\ell+t_\ell)$, provided all final conductances are positive. For this inner product of grade one, the finite influences of different existing edges add. Such separation generally fails on graphs with cycles; for [[Metric Distribution in Higher Grades#Which pairs are selected on a tree|higher grades]], it can fail even on a tree.

## What the distribution retains and the limits of this picture

The output form retains the common segment, the paths' relative direction, and the resistances of its edges. It does not recover the original paths outside their intersection or distinguish simultaneous reversal of both vectors. For $u=v$, it distributes the effective resistance along the unique path:

$$
D_L([v]^2)=\sum_{\ell\in P_v}\frac1{c_\ell}q_\ell,\qquad
v^2=\sum_{\ell\in P_v}\frac1{c_\ell}
$$

The exact-support statement concerns **changes to existing edges of the tree**. Adding a coupling between previously nonadjacent vertices creates a cycle and may affect even the inner product of disjoint paths. For example, on the unit path $a-b-c-d$, take $v=(ab)$ and $u=(cd)$. Initially $N_L(f)=0$ and $D_L(f)=0$. After adding coupling $ad$ with conductance $t>0$, the general formula gives

$$
N_{L+t[(ad)]^2}(f)=-\frac{t}{1+3t}
$$

Thus a zero distribution over existing edges does not mean insensitivity to new couplings. Distributions over alternative routes and cancellation of signed contributions are discussed in [[The Influence Field on Graphs with Cycles]].

The formulas follow from the classical resistance metric of a tree and the definition of $D_L$. Examples were checked in exact rational arithmetic: unique-path coordinates were compared with independent Laplacian inversion, forest-based resistance calculations, and direct calculations on changed graphs. Code and results are available in the [series checks](https://github.com/magin67/pmg-notes/tree/v5/checks/metric-distributions).

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distributions and Edge Influence|Back to Metric Distributions and Edge Influence]].
