---
title: Variation of a Single Edge
date: 2026-10-04
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: single-edge-variation
lang: en
description: How changing the conductance of a single edge changes the Laplacian, Green matrix, effective resistances, spanning-tree weight, and spanning 2-forest weights of a graph.
---

So far, the graph has been treated as a fixed object. The conductances $c_{ij}$ determined the Laplacian, the Green matrix determined the inverse metric structure, and effective resistances played the role of squared distances between vertices.

We now change only one edge and trace how this local change propagates through the entire network.

Physically, the problem is simple. Suppose the conductance between vertices $k$ and $l$ changes: for example, the conductor becomes thicker, or an additional parallel channel is added. Locally only one connection changes, but effective resistances between many other pairs of vertices may change as well.

This perturbation turns out to have a particularly simple structure. The change in the Laplacian has rank one, the change in the inverse metric can be computed exactly, and the sensitivity of any effective resistance is determined by the square of a single inner product of graph vectors.

## Problem setup

Consider a connected undirected graph with nonnegative conductances $c_{ij}=c_{ji}$.

Choose a pair of vertices $k,l$ and change only its conductance:
$$
c'_{kl}=c_{kl}+\delta
\tag{1}
$$
All other conductances remain unchanged.

We assume
$$
c_{kl}+\delta\geq0
$$
The sign of $\delta$ determines the type of change:

- $\delta>0$ - the edge is strengthened;
- $-c_{kl}<\delta<0$ - the edge is weakened;
- $\delta=-c_{kl}$ - an existing edge is removed;
- if $c_{kl}=0$ and $\delta>0$, a new edge is added between the vertices.

For formulas involving the Green matrix, we additionally require the graph to remain connected after the change.

## Change in the Laplacian

As in [[Inner Product of Graph Vectors]], write
$$
\mathbf e_{kl}=\mathbf e_l-\mathbf e_k
$$
The contribution of a single edge with conductance $c_{kl}$ to the Laplacian is
$$
c_{kl}\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}
$$
Therefore changing one conductance gives
$$
\boxed{
L'=L+\delta\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}
}
\tag{2}
$$
The matrix
$$
\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}
$$
has rank one. Thus a local variation of one edge is a **rank-one perturbation** of the Laplacian.

This is the first reason why the problem admits an exact solution.

## Change in the Green matrix

The Laplacian of a connected graph is singular in the direction $\mathbf 1$, but invertible on the centered subspace
$$
H=\{x:\mathbf 1^{\mathsf T}x=0\}
$$
On this subspace, the Green matrix $G=L^+$ acts as the ordinary inverse of $L$.

Since $\mathbf e_{kl}\in H$, the Sherman-Morrison formula can be applied to (2). We obtain
$$
\boxed{
G'
=
G-
\frac{\delta}
{1+\delta R_{kl}}
G\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}G
}
\tag{3}
$$
Here we used
$$
\mathbf e_{kl}^{\mathsf T}G\mathbf e_{kl}=R_{kl}
$$
Formula (3) is exact: no smallness assumption on $\delta$ is required.

The vector $G\mathbf e_{kl}$ has a direct electrical meaning. It is the centered potential vector produced by a unit external current applied between vertices $k$ and $l$.

Thus the change in the entire Green matrix is built from a single potential profile. Although the global metric structure of the graph changes, the matrix correction still has rank one.

> [!note] When the denominator vanishes
> In the physically admissible range, the denominator $1+\delta R_{kl}$ remains positive as long as the modified graph stays connected.
>
> A special case occurs when a bridge is removed. Then the graph splits into components, the Green matrix of a connected graph no longer describes the whole network as one finite metric system, and the denominator in (3) becomes zero.

## Change in an arbitrary effective resistance

For another pair of vertices $i,j$, the effective resistance is
$$
R_{ij}=\mathbf e_{ij}^{\mathsf T}G\mathbf e_{ij}
$$
After the variation,
$$
R'_{ij}=\mathbf e_{ij}^{\mathsf T}G'\mathbf e_{ij}
$$
Substituting (3), we get
$$
R'_{ij}
=
R_{ij}
-
\frac{\delta}{1+\delta R_{kl}}
\left(
\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}
\right)^2
$$
But
$$
\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}
=
\langle a_{ij},a_{kl}\rangle
$$
where $a_{ij}=a_j-a_i$ and $a_{kl}=a_l-a_k$ are graph vectors in resistance geometry.

Therefore
$$
\boxed{
R'_{ij}
=
R_{ij}
-
\frac{\delta}{1+\delta R_{kl}}
\langle a_{ij},a_{kl}\rangle^2
}
\tag{4}
$$
Equivalently, in finite-variation form,
$$
\boxed{
\Delta R_{ij}
=
-
\frac{\delta}{1+\delta R_{kl}}
\langle a_{ij},a_{kl}\rangle^2
}
\tag{5}
$$
This is the main formula of the note.

From [[Inner Product of Graph Vectors]],
$$
\langle a_{ij},a_{kl}\rangle
=
\frac12
\left(
R_{il}+R_{jk}-R_{ik}-R_{jl}
\right)
$$
Hence (5) can be written entirely in terms of effective resistances:
$$
\boxed{
\Delta R_{ij}
=
-
\frac{\delta}
{4(1+\delta R_{kl})}
\left(
R_{il}+R_{jk}-R_{ik}-R_{jl}
\right)^2
}
\tag{6}
$$

> [!remark] Geometric meaning
> The effect of varying the edge $(kl)$ on the distance between $i$ and $j$ is determined not by the ordinary proximity of these pairs in a drawing of the graph, but by their inner product in resistance geometry.
>
> If
> $$
> \langle a_{ij},a_{kl}\rangle=0
> $$
> then changing the edge $(kl)$ does not change $R_{ij}$ at all for any admissible finite $\delta$. In resistance geometry, the corresponding directions are orthogonal.

## Electrical interpretation of the mixed factor

The inner product $\langle a_{ij},a_{kl}\rangle$ already has an electrical interpretation.

If a unit external current is applied between $k$ and $l$, the resulting potential difference between $i$ and $j$ is
$$
\varphi_j-\varphi_i
=
\langle a_{ij},a_{kl}\rangle
$$
By reciprocity, the measurement pair and the current pair may be interchanged.

Thus formula (5) says that the change in effective resistance is determined by the square of the **transfer voltage** between two pairs of vertices.

If this voltage is zero, changing the conductance $(kl)$ does not affect the measurement between $i$ and $j$.

## Infinitesimal variation

Now let $\delta$ be small and divide (5) by $\delta$.

As $\delta\to0$,
$$
\frac1{1+\delta R_{kl}}\longrightarrow1
$$
Therefore
$$
\boxed{
\frac{\partial R_{ij}}{\partial c_{kl}}
=
-\langle a_{ij},a_{kl}\rangle^2
}
\tag{7}
$$
This is the local sensitivity matrix of the resistance metric with respect to conductance changes.

The right-hand side is always nonpositive:
$$
\frac{\partial R_{ij}}{\partial c_{kl}}\leq0
$$
Therefore strengthening any edge cannot increase any effective resistance.

This is the local differential form of Rayleigh monotonicity.

> [!info] What sensitivity measures
> Formula (7) is especially transparent in geometric form. The sensitivity of one metric quantity to one edge equals minus the square of the inner product of the corresponding graph vectors.
>
> The sign is known in advance, while the magnitude of the effect is completely determined by the relative position of the two directions in resistance geometry.

## Special case: the endpoints of the varied edge

Set $(ij)=(kl)$. Then
$$
\langle a_{kl},a_{kl}\rangle=R_{kl}
$$
From (4),
$$
R'_{kl}
=
R_{kl}
-
\frac{\delta R_{kl}^2}{1+\delta R_{kl}}
$$
After simplification,
$$
\boxed{
R'_{kl}
=
\frac{R_{kl}}{1+\delta R_{kl}}
}
\tag{8}
$$
For the derivative,
$$
\boxed{
\frac{\partial R_{kl}}{\partial c_{kl}}
=-R_{kl}^2
}
\tag{9}
$$
Formula (8) has a simple electrical meaning. The rest of the network between $k$ and $l$ already has some effective conductance. When $\delta>0$, adding conductance between the same two vertices acts as adding another channel in parallel.

## What happens to the spanning-tree weight

Changing one edge affects not only the metric but also the combinatorics of the graph.

Let $\tau$ be the spanning-tree weight: in the weighted case, the sum of the weights of all spanning trees, where the weight of a tree is the product of the conductances of its edges.

By Kirchhoff's matrix-tree theorem, $\tau$ equals the determinant of any reduced Laplacian. After the variation, this reduced Laplacian receives the same rank-one perturbation as $L$. The determinant formula for a rank-one perturbation gives
$$
\boxed{
\tau'
=
\tau(1+\delta R_{kl})
}
\tag{10}
$$
This formula is again exact.

Therefore
$$
\Delta\tau
=
\delta\tau R_{kl}
$$
and
$$
\boxed{
\frac{\partial\tau}{\partial c_{kl}}
=
\tau R_{kl}
}
\tag{11}
$$
For the logarithm of the spanning-tree weight, we obtain the particularly compact identity
$$
\boxed{
\frac{\partial\log\tau}{\partial c_{kl}}
=
R_{kl}
}
\tag{12}
$$
Thus effective resistance measures not only metric distance between vertices but also the relative sensitivity of the spanning-tree weight to strengthening the corresponding edge.

## Probability of an edge in a random spanning tree

Choose a spanning tree at random with probability proportional to the product of the conductances of its edges.

If the edge $(kl)$ already exists and $c_{kl}>0$, then
$$
\frac{c_{kl}}{\tau}
\frac{\partial\tau}{\partial c_{kl}}
$$
is the total probability of all spanning trees containing this edge.

Using (11),
$$
\boxed{
\Pr((kl)\in T)=c_{kl}R_{kl}
}
\tag{13}
$$
This quantity lies between $0$ and $1$.

Formula (10) therefore has a probabilistic interpretation: the sensitivity of the spanning-tree weight to an edge change is determined by how essential that edge is for a random spanning tree.

## Weakening and removing an edge

When the edge is weakened, $\delta<0$. As long as the graph remains connected,
$$
1+\delta R_{kl}>0
$$
and (5) gives
$$
\Delta R_{ij}\geq0
$$
Thus weakening an edge increases effective resistances or leaves them unchanged.

Now remove an existing edge completely:
$$
\delta=-c_{kl}
$$
Then
$$
\boxed{
\tau'
=
\tau(1-c_{kl}R_{kl})
}
\tag{14}
$$
Using (13),
$$
1-c_{kl}R_{kl}
=
1-\Pr((kl)\in T)
$$
If the edge is not a bridge, at least one spanning tree does not contain it, so
$$
c_{kl}R_{kl}<1
$$
and removing the edge preserves connectivity.

If the edge is a bridge, it belongs to every spanning tree:
$$
\Pr((kl)\in T)=1
$$
Therefore
$$
\boxed{c_{kl}R_{kl}=1}
\tag{15}
$$
and after removal
$$
\tau'=0
$$
At the same time, the denominator in formulas (3)-(8) becomes zero. This is not an algebraic accident: the graph actually becomes disconnected.

> [!remark] Three interpretations of the same variation
> For a positively weighted connected graph, the following statements for an edge $(kl)$ are equivalent:
>
> - $(kl)$ is a bridge;
> - the edge belongs to every spanning tree;
> - $c_{kl}R_{kl}=1$.
>
> The same property is expressed topologically, probabilistically, and metrically.

## Return to the Gram determinant

In the previous note [[From Lengths to Areas and Volumes]], the Gram determinant of two vectors was
$$
\det\operatorname{Gram}(a_{ij},a_{kl})
=
R_{ij}R_{kl}
-
\langle a_{ij},a_{kl}\rangle^2
\tag{16}
$$
Let us see how this quantity appears in the variation problem.

Define $m_{ij}=\tau R_{ij}$ as the weighted sum of spanning 2-forests separating vertices $i$ and $j$.

Using (4) and (10) together,
$$
\begin{aligned}
m'_{ij}
&=\tau'R'_{ij}=\\
&=\tau(1+\delta R_{kl})
\left(
R_{ij}
-
\frac{\delta}{1+\delta R_{kl}}
\langle a_{ij},a_{kl}\rangle^2
\right)
\end{aligned}
$$
After simplification,
$$
m'_{ij}-m_{ij}
=
\delta\tau
\left(
R_{ij}R_{kl}
-
\langle a_{ij},a_{kl}\rangle^2
\right)
$$
Therefore
$$
\boxed{
\Delta m_{ij}
=
\delta\tau\,
\det\operatorname{Gram}(a_{ij},a_{kl})
}
\tag{17}
$$
But the Gram determinant of two vectors is the squared area of the parallelogram they span:
$$
\det\operatorname{Gram}(a_{ij},a_{kl})=S_{\parallel}^2
$$
Hence
$$
\boxed{
\Delta m_{ij}
=
\delta\tau S_{\parallel}^2
}
\tag{18}
$$
Here the variation problem directly continues the geometry of the previous note.

For effective resistance, the change was determined by the square of the inner product of two directions. For the unnormalized two-forest weight, the full Gram determinant appears, that is, the squared area.

This is the first point where higher-order geometric quantities appear not as an additional construction but directly as coefficients of graph variation.

## Example: strengthening one edge of a triangle

Consider $K_3$ with unit conductances:
$$
c_{12}=c_{13}=c_{23}=1
$$
For every pair,
$$
R_{12}=R_{13}=R_{23}=\frac23
$$
and the spanning-tree weight is
$$
\tau=3
$$
Strengthen edge $(12)$ by one:
$$
\delta=1,
\qquad
c'_{12}=2
$$
For the varied pair itself, (8) gives
$$
R'_{12}
=
\frac{2/3}{1+2/3}
=
\frac25
$$
Now consider the resistance between vertices $1$ and $3$. From the inner-product formula,
$$
\langle a_{13},a_{12}\rangle
=
\frac13
$$
Therefore
$$
R'_{13}
=
\frac23
-
\frac{1}{1+2/3}\frac19
=
\frac35
$$
The spanning-tree weight changes according to (10):
$$
\tau'
=
3\left(1+\frac23\right)
=5
$$
This can be checked directly. After strengthening edge $(12)$, the two spanning trees containing it have weight $2$, while the third has weight $1$:
$$
2+2+1=5
$$
Before the change, the probability that edge $(12)$ belonged to the random spanning tree was
$$
c_{12}R_{12}=\frac23
$$
After strengthening,
$$
c'_{12}R'_{12}
=
2\cdot\frac25
=
\frac45
$$
The strengthened edge has become much more likely to appear in a random spanning tree.

## What is not covered in this note

The formulas above concern a change in only one edge.

If several conductances change simultaneously, each of them changes the same Green matrix, so their effects cannot in general be treated as independent. Instead of a rank-one perturbation, one obtains a higher-rank perturbation, and the natural objects become matrices of mutual inner products and their determinants. This is the subject of [[Joint Variation of Several Edges]].

A separate inverse problem starts from variations of effective resistances and asks how conductances change or can be reconstructed from them. It uses the same transition
$$
L\longleftrightarrow G\longleftrightarrow R
$$
but has a different formulation and will be treated separately.

## Summary

Changing one conductance,
$$
c_{kl}\longmapsto c_{kl}+\delta
$$
produces a rank-one change in the Laplacian,
$$
L'=L+\delta\mathbf e_{kl}\mathbf e_{kl}^{\mathsf T}
$$
From this follow two main exact formulas:
$$
\boxed{
R'_{ij}
=
R_{ij}
-
\frac{\delta}{1+\delta R_{kl}}
\langle a_{ij},a_{kl}\rangle^2
}
$$
and
$$
\boxed{
\tau'=\tau(1+\delta R_{kl})
}
$$
In infinitesimal form, the first becomes
$$
\boxed{
\frac{\partial R_{ij}}{\partial c_{kl}}
=
-\langle a_{ij},a_{kl}\rangle^2
}
$$
Thus a local change in one edge is controlled by the geometry of graph vectors. The inner product determines the sensitivity of resistance distance, effective resistance determines the sensitivity of the spanning-tree weight, and the Gram determinant determines the variation of the two-forest weight.

The same variation appears simultaneously in three languages: electrical networks, metric geometry, and spanning-tree combinatorics.

## Classical results used in this note

- the Sherman-Morrison formula for a rank-one update of an inverse matrix;
- Rayleigh monotonicity for electrical networks;
- Kirchhoff's matrix-tree theorem;
- the identity $\Pr(e\in T)=c_eR_e$ for weighted random spanning trees;
- the spanning-forest interpretation of $\tau R_{ij}$.
