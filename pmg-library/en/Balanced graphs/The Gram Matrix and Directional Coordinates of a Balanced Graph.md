---
title: The Gram Matrix and Directional Coordinates of a Balanced Graph
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: gram-matrix-and-directional-coordinates-of-balanced-graphs
order: 8
description: The canonical vertex Gram matrix, source and receiver roles, and directional bi-coordinates and di-coordinates for a balanced graph.
source_revision: 2
---

One-way resistances determine the bilinear metric on vertex differences. Pairings of the vertices themselves require an extension. We construct a zero-diagonal Gram matrix that preserves directional vector pairings and becomes symmetric for an undirected graph. We then distinguish source and receiver roles and express pairings through bi-coordinates and di-coordinates.

The graph is connected, balanced, and loopless, on $n\ge2$ vertices, with nonnegative arc weights. The weight $f_{ij}$ refers to $i\to j$: rows represent sources and columns receivers. We use [[One-Way Resistance and Hitting Times]] and [[Resistance Geometry and Circulation]].

## From the vector metric to a vertex Gram matrix

Let $h=n^{-1}\sum_i a_i$ be the centroid, and $x_i=a_i-h$ the zero-affine-weight vectors. For

$$
\mathbf{Gr}=\mathbf L^+,
\qquad
\mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

we have $\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J$; both matrices have zero row and column sums. The chosen argument order for the metric potential gives

$$
\beta(u,v)=P_M([u,v])=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u,
\qquad
\beta(x_i,x_j)=\mathrm{Gr}_{ji}
$$

The Gram matrix of centered vectors is therefore $\mathbf{Gr}^{\mathsf T}$. This transpose follows from argument order, not from reversing the graph's arcs.

Set

$$
q_i=\mathrm{Gr}_{ii}=x_i^2,
\qquad
\bar q=\frac1n\sum_iq_i
$$

The value $q_i$ is the squared distance from a vertex to the centroid in the symmetric metric. It is not the norm of the vertex itself. One-way resistances determine these values without further data:

$$
r_{ij}=q_j-\mathrm{Gr}_{ij},
\qquad
q_i=\frac1n\sum_k r_{ki}
$$

## The canonical Gram matrix of local vertices

> [!info] The canonical Gram matrix of local vertices
> **Definition.** Extend the pairing from differences to the vertex space by requiring
>
> $$
> a_i^2=0,
> \qquad
> a_i\cdot h=h\cdot a_i
> $$

The first condition makes the vertices local in the later isotropic extension. The second requires equal pairings with the centroid in both roles, without requiring the whole Gram matrix to be symmetric.

> [!info] Vertex Gram matrix
> **Theorem.** This extension is unique. Its matrix $\mathbf G=(g_{ij})$ is
>
> $$
> \boxed{g_{ij}=a_i\cdot a_j
> =\mathrm{Gr}_{ji}-\frac{q_i+q_j}{2}
> =-r_{ji}+\frac{q_i-q_j}{2}}
> \tag{1}
> $$

> [!note]- Existence and uniqueness
> **Proof.** Matrix (1) has zero diagonal and satisfies
>
> $$
> \mathbf J\mathbf G\mathbf J=\mathbf{Gr}^{\mathsf T},
> \qquad
> \mathbf G\mathbf1=\mathbf G^{\mathsf T}\mathbf1
> $$
>
> It therefore preserves every zero-sum vector pairing and satisfies the centroid condition.
>
> If two extensions agree on these vectors, their matrix difference has the form $\mathbf1\mathbf u^{\mathsf T}+\mathbf v\mathbf1^{\mathsf T}$. Zero diagonal gives $\mathbf v=-\mathbf u$. Equality of row and column sums then requires every component of $\mathbf u$ to be equal, making the matrix difference zero. $\square$

Canonical here means unique under the stated centroid condition. Zero diagonal alone is insufficient: adding $\mathbf t\mathbf1^{\mathsf T}-\mathbf1\mathbf t^{\mathsf T}$ changes neither the diagonal nor pairings of differences. Condition (1) removes that freedom.

The linear centroid's own norm and its vertex pairings are

$$
h^2=-\bar q,
\qquad
a_i\cdot h=h\cdot a_i=-\frac{q_i+\bar q}{2}
$$

A negative norm for $h$ is allowed: a linear combination of local vertices need not be local. This distinction is discussed in [[Nonlocal Elements, Spheres, and Their Centers]].

## Resistance, circulation, and the symmetric case

Equation (1) retains the familiar norm-of-a-difference formula:

$$
\boxed{(a_i-a_j)^2
=a_i^2+a_j^2-a_i\cdot a_j-a_j\cdot a_i
=r_{ij}+r_{ji}=R_{ij}}
\tag{2}
$$

Pair resistances determine the symmetric Gram part, and circulation determines the skew part:

$$
g_{ij}+g_{ji}=-R_{ij},
\qquad
g_{ij}-g_{ji}=\mathrm{Gr}_{ji}-\mathrm{Gr}_{ij}
$$

If $\gamma(u,v)=(\beta(u,v)-\beta(v,u))/2$, then

$$
g_{ij}=-\frac{R_{ij}}2+\gamma(x_i,x_j)
$$

In [[The Circulation Form|circulation-form notation]], the second term is $P_M(w(h,a_i,a_j))/2$. The centroid is allowed because the form's arguments are point differences.

> [!info] Resistance, circulation, and the symmetric case
> **Corollary.** For this canonical Gram matrix,
>
> $$
> \mathbf G=\mathbf G^{\mathsf T}
> \quad\Longleftrightarrow\quad
> \mathbf L=\mathbf L^{\mathsf T}
> $$
>
> The skew parts of $\mathbf G$ and $\mathbf{Gr}^{\mathsf T}$ agree, while pseudoinversion preserves symmetry in both directions. An undirected graph therefore has exactly the familiar $\mathbf G=-\mathbf R/2$.
>
> The matrix $\mathbf r$ is not redefined. Even for an undirected graph, $r_{ij}$ may differ from $r_{ji}$ because $q_i,q_j$ differ. The correction in (1) separates unequal centroid positions from pairing asymmetry.

## Sources and receivers

Each vertex has two roles: sending and receiving couplings. To record them, use two copies of the vertex space, $V_{\mathrm{out}}$ and $V_{\mathrm{in}}$, with bases $a_i^{\mathrm{out}}$ and $a_i^{\mathrm{in}}$.

> [!info] Sources and receivers
> **Definition.** Write the directional pairing in source-receiver order:
>
> $$
> a_i^{\mathrm{out}}\cdot a_j^{\mathrm{in}}=g_{ij}
> $$

The shorthand $a_i\cdot a_j$ means this role order. The value $g_{ij}$ describes a metric pairing in the whole graph, not the weight $f_{ij}$ of one arc.

The natural identification of the copies preserves vertex labels and linear-combination coefficients. Under it, a difference norm is

$$
(a_i-a_j)^2
=(a_i^{\mathrm{out}}-a_j^{\mathrm{out}})
\cdot(a_i^{\mathrm{in}}-a_j^{\mathrm{in}})
$$

No pairing of two sources or two receivers is separately introduced. The existing nonsymmetric bilinear form on one space is expressed using two consistently identified role spaces.

## Bi-coordinates and di-coordinates

As in [[Projections, Bi-coordinates, and Di-coordinates]], bi-coordinates are expansion coefficients. For specified representatives,

$$
X_{\mathrm{out}}=\sum_i b^i_{\mathrm{out}}(X)a_i^{\mathrm{out}},
\qquad
Y_{\mathrm{in}}=\sum_j b^j_{\mathrm{in}}(Y)a_j^{\mathrm{in}}
$$

each expansion is unique. Superscripts on $b^i$ index the coefficients.

> [!info] Bi-coordinates and di-coordinates
> **Definition.** Outgoing and incoming di-coordinates are pairings with the opposite-role basis:
>
> $$
> d_j^{\mathrm{out}}(X)=X_{\mathrm{out}}\cdot a_j^{\mathrm{in}},
> \qquad
> d_i^{\mathrm{in}}(Y)=a_i^{\mathrm{out}}\cdot Y_{\mathrm{in}}
> $$

For coordinate columns, this means

$$
\mathbf d_{\mathrm{out}}(X)=\mathbf G^{\mathsf T}\mathbf b_{\mathrm{out}}(X),
\qquad
\mathbf d_{\mathrm{in}}(Y)=\mathbf G\mathbf b_{\mathrm{in}}(Y)
$$

> [!info] Bi-coordinates and di-coordinates
> **Corollary.** The pairing has two equal coordinate contractions:
>
> $$
> \boxed{X_{\mathrm{out}}\cdot Y_{\mathrm{in}}
> =\mathbf b_{\mathrm{out}}(X)^{\mathsf T}\mathbf d_{\mathrm{in}}(Y)
> =\mathbf d_{\mathrm{out}}(X)^{\mathsf T}\mathbf b_{\mathrm{in}}(Y)}
> \tag{3}
> $$
>
> Both equal $\mathbf b_{\mathrm{out}}(X)^{\mathsf T}\mathbf G\mathbf b_{\mathrm{in}}(Y)$. Moving the conversion from bi- to di-coordinates to the other factor does not change the value. Exchanging the objects' roles, giving $Y_{\mathrm{out}}\cdot X_{\mathrm{in}}$, may change it.
>
> Two role spaces do not by themselves give one fixed linear representative two different expansions. Different bi-coordinate sets arise, for example, when one functional is represented through outgoing and incoming pairings. This is how the sphere is constructed in [[The Isotropic Space and Sphere of a Balanced Graph]].

## An example with unequal directional pairings

Take the unit cycle $a\to b\to c\to a$ and add a unit undirected coupling $ab$, meaning two opposite arcs. After combining weights,

$$
f_{ab}=2,\qquad f_{ba}=f_{bc}=f_{ca}=1
$$

Other weights are zero. Incoming and outgoing weighted degrees at the vertices are $2,2,1$.

![[A Balanced Graph with Different Sphere Coordinates.svg]]

*Arrows show directions and numbers show weights. The two arcs between $a,b$ have unequal weights; arcs through $c$ maintain balance.*

Direct calculation gives

$$
\mathbf L=\begin{pmatrix}2&-2&0\\-1&2&-1\\-1&0&1\end{pmatrix},
\qquad
\mathbf{Gr}=\frac1{18}
\begin{pmatrix}4&1&-5\\-2&4&-2\\-2&-5&7\end{pmatrix}
$$

Consequently,

$$
\mathbf r=\frac16\begin{pmatrix}0&1&4\\2&0&3\\2&3&0\end{pmatrix},
\qquad
\mathbf G=\frac1{12}\begin{pmatrix}0&-4&-5\\-2&0&-7\\-7&-5&0\end{pmatrix}
$$

In particular,

$$
a_{\mathrm{out}}\cdot b_{\mathrm{in}}=-\frac13,
\qquad
b_{\mathrm{out}}\cdot a_{\mathrm{in}}=-\frac16,
\qquad
(a-b)^2=\frac12
$$

The outgoing di-coordinates of $a$ form column $(0,-1/3,-5/12)^{\mathsf T}$; the incoming di-coordinates of $b$ form $(-1/3,0,-5/12)^{\mathsf T}$. Contracting either with the appropriate unit bi-coordinate column in (3) gives the same $-1/3$.

The same graph is used to compute the sphere and recover the Laplacian in [[The Isotropic Space and Sphere of a Balanced Graph]].

## Sources and status

Nonsymmetric bilinear pairings through a generalized inverse Laplacian, and the freedom to add row and column terms, are discussed in [1, §§8,12]. Source [2] studies the directed resistance matrix with entries $q_i+q_j-2\mathrm{Gr}_{ij}$; in our notation it equals $-2\mathbf G^{\mathsf T}$ and differs from $\mathbf r$.

The centroid normalization and its uniqueness, coordinate formulas, and connection to the PMG potential are proved here. Source and receiver terminology specifies argument roles. The note also draws on the author's PMG research.

Exact rational checks compared difference pairings with reduced-Laplacian inverses, verified the centroid condition, and checked the example by direct matrix computation.

1. Doyle, P. G.; Steiner, J. [Commuting time geometry of ergodic Markov chains](https://arxiv.org/html/1107.2612v2). arXiv:1107.2612, version 2, 2017, §§8,12.
2. Balaji, R.; Bapat, R. B.; Goel, S. [Resistance matrices of balanced directed graphs](https://arxiv.org/abs/1906.01165). *Linear and Multilinear Algebra*, 70 (2022), 787-808. [DOI](https://doi.org/10.1080/03081087.2020.1748850).
