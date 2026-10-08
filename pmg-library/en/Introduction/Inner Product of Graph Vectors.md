---
title: Inner Product of Graph Vectors
date: 2026-10-03
updated: 2026-10-08
revision: 2
source_revision: 5
status: draft
text_prepared_by: ChatGPT
translation_key: inner-product-vectors
lang: en
description: Inner products of affine vectors through the Green matrix and four effective resistances. Electrical interpretation, reciprocity of measurements, and the four-point identity.
order: "3"
---

In [[Effective Resistance and Graph Geometry]], the vertices of a connected graph were represented by points in Euclidean space whose squared distances equal the effective resistances. The same construction determines inner products of affine vectors between vertices. Electrically, these express the potential difference across one pair of vertices when a unit current is passed through another pair.

We consider a finite connected undirected graph without loops, with positive conductances on its edges. Its Laplacian is denoted by $L$ and its Green matrix by $G=L^+$. For the points of the resistance representation, we retain the notation

$$
a_{ij}=a_j-a_i,\qquad \mathbf e_{ij}=\mathbf e_j-\mathbf e_i
$$

where $\mathbf e_i$ are the standard coordinate columns. The column $\mathbf e_{ij}$ records the coefficients of the affine vector $a_{ij}$ with respect to the vertices.

## Inner product through the Green matrix

Let $x_i$ denote the position vector of $a_i$ relative to the centroid. By construction of the resistance representation, $x_i\cdot x_j=G_{ij}$, so

$$
a_{ij}\cdot a_{kl}=(x_j-x_i)\cdot(x_l-x_k)=G_{jl}-G_{jk}-G_{il}+G_{ik}
$$

> [!info] Inner product
> **Lemma.** For any two pairs of vertices,
>
> $$
> a_{ij}\cdot a_{kl}=\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}
> \tag{1}
> $$
>
> This is the numerical inner product of affine vectors in the Euclidean resistance representation.

Some indices may coincide. In particular, when the two pairs coincide, (1) gives

$$
a_{ij}\cdot a_{ij}=\|a_{ij}\|^2=R_{ij}
$$

## The four-resistance formula

Effective resistances are expressed through the Green matrix as

$$
R_{pq}=G_{pp}+G_{qq}-2G_{pq}
$$

In the combination $R_{il}+R_{jk}-R_{ik}-R_{jl}$, the diagonal entries cancel, giving

$$
R_{il}+R_{jk}-R_{ik}-R_{jl}=2(G_{ik}+G_{jl}-G_{il}-G_{jk})
$$

> [!info] Polarization of resistances
> **Lemma.** The inner product can be recovered from four effective resistances:
>
> $$
> a_{ij}\cdot a_{kl}=\frac12(R_{il}+R_{jk}-R_{ik}-R_{jl})
> \tag{2}
> $$

This is the standard polarization identity for squared Euclidean distances. In an arbitrary coordinate system, the diagonal terms are the squared norms of the position vectors. Each appears with opposite signs and cancels. The result is therefore independent of the choice of origin, although the norms of the position vectors themselves change under translation.

> [!note] Orientation
> Reversing one vector changes the sign of the inner product:
>
> $$
> a_{ji}\cdot a_{kl}=-a_{ij}\cdot a_{kl}
> $$
>
> Reversing both vectors preserves its value. The resistance $R_{ij}$ is independent of orientation.

## Electrical interpretation

Inject a unit current at vertex $l$ and withdraw it at vertex $k$. The external-current column is then $J=\mathbf e_{kl}$. The centered solution of $L\varphi=J$ is

$$
\varphi=G\mathbf e_{kl}
$$

The potential difference across the measurement pair is

$$
\varphi_j-\varphi_i=\mathbf e_{ij}^{\mathsf T}\varphi=\mathbf e_{ij}^{\mathsf T}G\mathbf e_{kl}
$$

> [!info] Measuring an inner product
> **Lemma.** For a unit current injected at $l$ and withdrawn at $k$,
>
> $$
> \varphi_j-\varphi_i=a_{ij}\cdot a_{kl}
> \tag{3}
> $$
>
> For a current of magnitude $I$ in the same direction, the right-hand side is multiplied by $I$.

Interchanging the injection and withdrawal vertices changes the sign of the current column. The difference $\varphi_j-\varphi_i$ also changes sign. Adding a common constant to all potentials does not affect the measurement.

## Reciprocity of measurements

Symmetry of the Green matrix in (1) gives

$$
a_{ij}\cdot a_{kl}=a_{kl}\cdot a_{ij}
$$

This is the reciprocity principle for a linear resistive network. The voltage $\varphi_j-\varphi_i$ produced by unit injection at $l$ and withdrawal at $k$ equals the voltage $\psi_l-\psi_k$ produced by unit injection at $j$ and withdrawal at $i$. Interchanging the current and measurement pairs preserves the result when their orientations are retained.

## The four-point identity

> [!info] Four-point identity
> **Lemma.** For any four points and their affine differences $a_{ij}=a_j-a_i$,
>
> $$
> a_{ij}\cdot a_{kl}+a_{jk}\cdot a_{il}+a_{ik}\cdot a_{lj}=0
> \tag{4}
> $$
>
> The points need not be distinct. The equality holds for any choice of inner product.

For graph vertices, the identity can be derived through effective resistances.

> [!note]- Proof
> **Proof.** By (2),
>
> $$
> 2a_{ij}\cdot a_{kl}=R_{il}+R_{jk}-R_{ik}-R_{jl}
> $$
>
> $$
> 2a_{jk}\cdot a_{il}=R_{jl}+R_{ik}-R_{ij}-R_{kl}
> $$
>
> $$
> 2a_{ik}\cdot a_{lj}=R_{ij}+R_{kl}-R_{il}-R_{jk}
> $$
>
> All resistance terms cancel upon addition. For arbitrary points, the same argument applies to the squared distances $R_{pq}=\|a_q-a_p\|^2$, since the polarization formula (2) remains valid. $\square$

Equality (4) follows from the bilinearity and symmetry of the inner product and the relations between differences of four points. It does not depend on the graph structure or on particular resistance values. In the note on [[Basic Objects and Operations of Polyform Algebra|polyform algebra]], it will be written as an equality of polar forms that holds before a metric is chosen.

By (3), the same relation holds for three electrical measurements with the corresponding current and measurement pairs. Each of the three values equals minus the sum of the other two.

## Example: a triangle

Consider the complete graph $K_3$ with unit conductances on all edges.

> [!example] Resistances and inner products
> Between any pair of vertices, an edge of resistance $1$ is in parallel with a two-edge path of total resistance $2$. Hence
>
> $$
> R_{12}=R_{23}=R_{13}=\frac{1\cdot2}{1+2}=\frac23
> $$
>
> By (2),
>
> $$
> a_{12}\cdot a_{13}=\frac12(R_{13}+R_{21}-R_{11}-R_{23})=\frac13
> $$
>
> For the consecutively oriented vectors,
>
> $$
> a_{12}\cdot a_{23}=\frac12(R_{13}+R_{22}-R_{12}-R_{23})=-\frac13
> $$
>
> The squared norms of all three vectors are $2/3$. The resistance simplex is an equilateral triangle. The angle between $a_{12}$ and $a_{13}$ is $60^\circ$, while the angle between $a_{12}$ and $a_{23}$ is $120^\circ$.

> [!example] Independent calculation of potentials
> For this graph,
>
> $$
> L=\begin{pmatrix}
> 2&-1&-1\\
> -1&2&-1\\
> -1&-1&2
> \end{pmatrix}
> $$
>
> Inject a unit current at vertex $3$ and withdraw it at vertex $1$. The column $\varphi=(-1/3,0,1/3)^{\mathsf T}$ satisfies $L\varphi=(-1,0,1)^{\mathsf T}$ and $\sum_i\varphi_i=0$. Therefore,
>
> $$
> \varphi_2-\varphi_1=\frac13=a_{12}\cdot a_{13}
> $$
>
> For injection at $3$ and withdrawal at $2$, the centered potentials are $\psi=(0,-1/3,1/3)^{\mathsf T}$, giving
>
> $$
> \psi_2-\psi_1=-\frac13=a_{12}\cdot a_{23}
> $$
>
> Both measurements agree with (3), including the sign.

## Angles and further reading

For nonzero vectors, that is, when $i\ne j$ and $k\ne l$, the angle $\theta$ between them is determined by

$$
\cos\theta=\frac{a_{ij}\cdot a_{kl}}{\sqrt{R_{ij}R_{kl}}}
$$

A positive inner product means $0\le\theta<90^\circ$, a zero inner product means orthogonality, and a negative inner product means $90^\circ<\theta\le180^\circ$. Electrically, the sign determines the sign of the measured potential difference for the chosen orientations of the pairs.

The next note, [[Laplacian, Green Matrix, and Effective Resistance Matrix]], collects the forward and inverse transformations between $L$, $G$, and $R$. In [[From Lengths to Areas and Volumes]], inner products are used to compute Gram determinants, which express squared areas and volumes.

Sources on resistance geometry and electrical networks are listed in [[Further Reading for the PMG Introductory Series#Graphs, electric networks, and resistance geometry|the first section of the reading recommendations]].
