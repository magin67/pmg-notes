---
title: The Isotropic Space and Sphere of a Balanced Graph
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isotropic-space-and-sphere-of-balanced-graphs
order: 9
description: The bordered isotropic Gram matrix, recovery of the Laplacian, two directional sphere representatives, one resistance radius, and spanning-tree degree formulas.
source_revision: 3
---

Extending a balanced graph's Gram matrix by a null vector preserves the main undirected construction. Inversion recovers the original Laplacian, two sets of sphere coordinates, and one resistance radius. Incoming and outgoing coordinates are expressed through mean vertex degrees in two families of directed spanning trees.

Consider a connected loopless balanced graph on $n\ge2$ vertices with nonnegative arc weights. Use the canonical Gram matrix from [[The Gram Matrix and Directional Coordinates of a Balanced Graph]]:

$$
\mathbf{Gr}=\mathbf L^+,
\qquad
q_i=\mathrm{Gr}_{ii},
\qquad
g_{ij}=\mathrm{Gr}_{ji}-\frac{q_i+q_j}{2}
$$

Pairings are written in source-receiver order. The matrix $\mathbf G$ is fixed by equal vertex-centroid pairings in the two roles; all parameters below refer to this choice.

## The null vector and affine weight

**Definition.** Add an independent element $z$ and prescribe

$$
z^2=0,
\qquad
a_i^{\mathrm{out}}\cdot z_{\mathrm{in}}
=z_{\mathrm{out}}\cdot a_i^{\mathrm{in}}=1
$$

In the corresponding bases $(a_1,\ldots,a_n,z)$, the extended Gram matrix is

$$
\boxed{\mathbf G_z=
\begin{pmatrix}\mathbf G&\mathbf1\\\mathbf1^{\mathsf T}&0\end{pmatrix}}
\tag{1}
$$

For $X=\sum_i x_i a_i+\lambda z$,

$$
X_{\mathrm{out}}\cdot z_{\mathrm{in}}
=z_{\mathrm{out}}\cdot X_{\mathrm{in}}
=\varepsilon(X)=\sum_i x_i
$$

Thus $z$ represents affine weight from either side. The border entries $1$ normalize that weight; $z^2=0$ alone would not determine vertex pairings. The null vector is nonzero, but its norm and affine weight are zero.

Under the natural identification of role copies, an element's norm is $X^2=X_{\mathrm{out}}\cdot X_{\mathrm{in}}$. Local elements satisfy $\varepsilon(X)=1$ and $X^2=0$, as in [[The Null Vector, Isotropic Representation, and the Boundary]].

### Where balance is used

Let $\mathbf K$ be the upper-left block of the inverse of (1). Multiplying in both orders requires

$$
\mathbf K\mathbf1=0,
\qquad
\mathbf1^{\mathsf T}\mathbf K=0
$$

Consequently, a unit border on both sides can recover the original Laplacian only if it is balanced. For our Gram matrix, recovery indeed holds, as the next theorem shows.

## Inverting the Gram matrix

Let $\mathbf q$ be the column of $q_i$, with mean $\bar q=n^{-1}\operatorname{tr}\mathbf{Gr}$.

> [!info] Laplacian, sphere coordinates, and radius
> **Theorem.** The matrix $\mathbf G_z$ is invertible, with
>
> $$
> \boxed{\mathbf G_z^{-1}=
> \begin{pmatrix}
> \mathbf L^{\mathsf T}&\mathbf b_{\mathrm{in}}\\
> \mathbf b_{\mathrm{out}}^{\mathsf T}&\rho
> \end{pmatrix}}
> \tag{2}
> $$
>
> where
>
> $$
> \mathbf b_{\mathrm{in}}=\frac1n\mathbf1+\frac12\mathbf L^{\mathsf T}\mathbf q,
> \qquad
> \mathbf b_{\mathrm{out}}=\frac1n\mathbf1+\frac12\mathbf L\mathbf q
> \tag{3}
> $$
>
> $$
> \boxed{\rho=\bar q+\frac14\mathbf q^{\mathsf T}\mathbf L\mathbf q>0}
> \tag{4}
> $$

> [!proof]- Verification of the inverse
> **Proof.** From $\mathbf{Gr}\mathbf L=\mathbf L\mathbf{Gr}=\mathbf J$ and zero row and column sums,
>
> $$
> \mathbf G\mathbf L^{\mathsf T}
> =\mathbf I-\mathbf1\mathbf b_{\mathrm{out}}^{\mathsf T},
> \qquad
> \mathbf L^{\mathsf T}\mathbf G
> =\mathbf I-\mathbf b_{\mathrm{in}}\mathbf1^{\mathsf T}
> $$
>
> Substituting (3) into $\mathbf G$ gives
>
> $$
> \mathbf G\mathbf b_{\mathrm{in}}=-\rho\mathbf1,
> \qquad
> \mathbf b_{\mathrm{out}}^{\mathsf T}\mathbf G=-\rho\mathbf1^{\mathsf T},
> \qquad
> \mathbf1^{\mathsf T}\mathbf b_{\mathrm{in}}
> =\mathbf1^{\mathsf T}\mathbf b_{\mathrm{out}}=1
> $$
>
> These identities verify both matrix products in (2). Positivity follows from $\bar q>0$ and
>
> $$
> \mathbf q^{\mathsf T}\mathbf L\mathbf q
> =\mathbf q^{\mathsf T}\frac{\mathbf L+\mathbf L^{\mathsf T}}2\mathbf q\ge0
> $$
>
> The symmetric part of a balanced Laplacian is an undirected graph Laplacian. $\square$

The original Laplacian is recovered exactly: transpose the upper block according to our convention. In particular, the original arc weight is $f_{ij}=-(\mathbf G_z^{-1})_{ji}$ for $i\ne j$. Exchanging these indices does not reverse the arcs.

**Definition.** The corner entry $\rho$ in (2) is the balanced graph's resistance radius. We retain the PMG quadratic normalization; the corresponding linear quantity is $\sqrt\rho$. This extends the inverse-Gram definition in [[Resistance Radius of a Set - Gram Matrix and Volume]], rather than defining the parameter through an additional geometric model.

## One sphere and two metric representatives

Define the functional extracting the null-vector coefficient:

$$
\ell\left(\sum_i x_i a_i+\lambda z\right)=\lambda
$$

It differs from affine weight: $\ell(a_i)=0$, $\ell(z)=1$. Its dual-basis coordinate column is $\boldsymbol\ell=(0,\ldots,0,1)^{\mathsf T}$.

**Definition.** The basis sphere is specified by $\ell(X)=0$ on local elements. Its incoming and outgoing metric representatives satisfy

$$
X_{\mathrm{out}}\cdot S_{\mathrm{in}}=\ell(X),
\qquad
S_{\mathrm{out}}\cdot X_{\mathrm{in}}=\ell(X)
\quad\text{for all }X
\tag{5}
$$

This is one functional represented in two ways through a nonsymmetric pairing. Equation (2) gives

$$
S_{\mathrm{in}}=\sum_i b^i_{\mathrm{in}}a_i^{\mathrm{in}}+\rho z_{\mathrm{in}},
\qquad
S_{\mathrm{out}}=\sum_i b^i_{\mathrm{out}}a_i^{\mathrm{out}}+\rho z_{\mathrm{out}}
\tag{6}
$$

Their di-coordinates both equal $\boldsymbol\ell$. Their bi-coordinates are obtained through $\mathbf G_z^{-1}$ and $\mathbf G_z^{-\mathsf T}$, respectively. Each role has a unique expansion.

In particular,

$$
a_i^{\mathrm{out}}\cdot S_{\mathrm{in}}=0,
\qquad
S_{\mathrm{out}}\cdot a_i^{\mathrm{in}}=0
$$

$$
z_{\mathrm{out}}\cdot S_{\mathrm{in}}
=S_{\mathrm{out}}\cdot z_{\mathrm{in}}=1
$$

This supplies an analogue of an orthocenter understood as an object orthogonal to all basis vertices; in the nonsymmetric case its representative's role must be specified. We call it the basis sphere. Orthogonality in this extended space does not mean intersection of Euclidean simplex altitudes.

**Corollary.** There is one radius:

$$
\boxed{S_{\mathrm{out}}\cdot S_{\mathrm{in}}=\rho}
\tag{7}
$$

Substituting (6) in the first argument kills all vertex terms by orthogonality, while $\rho z_{\mathrm{out}}$ contributes $\rho$. Under the natural role identification, also $S_{\mathrm{out}}^2=S_{\mathrm{in}}^2=\rho$: by (5), each norm is its representative's $z$ coefficient.

The two sets of vertex coordinates coincide exactly when

$$
(\mathbf L-\mathbf L^{\mathsf T})\mathbf q=0
$$

This holds for undirected graphs and for constant $q_i$, as in a uniform directed cycle. Agreement of sphere coordinates alone is therefore not a graph-symmetry criterion.

### Local centers and geometric interpretation

The isotropic correction from [[Nonlocal Elements, Spheres, and Their Centers]] still applies:

$$
p_{\mathrm{out}}=S_{\mathrm{out}}-\frac\rho2z_{\mathrm{out}},
\qquad
p_{\mathrm{in}}=S_{\mathrm{in}}-\frac\rho2z_{\mathrm{in}}
$$

After identifying the role copies, each element has weight $1$ and norm zero. They are the local centers of the corresponding metric representatives; their coordinates generally differ.

In the symmetric case they agree with the local representation of the ordinary circumcenter, and $\rho$ is its squared Euclidean circumradius. For a general balanced graph, the symmetric pairing part supplies a separate Euclidean interpretation. Its center and squared radius cannot automatically be identified with (3), (4). The algebraic definition of $\rho$ is retained.

## Sphere coordinates and spanning-tree degrees

An incoming arborescence is directed toward its root: each nonroot vertex has one outgoing arc leading eventually to the root. An outgoing arborescence is directed away from its root: each nonroot vertex has one incoming arc and is reachable from the root.

A tree's weight is the product of its arc weights. In each family, choose the root uniformly and then choose a tree with probability proportional to its weight. Balance makes the total weight at each root equal to $\tau$; for outgoing trees, apply the matrix-tree theorem to $\mathbf L^{\mathsf T}$. The total weight of either family is $n\tau$.

Let $\deg_T(i)$ count all tree arcs incident to $i$, regardless of direction. This is an ordinary tree degree: arc weights affect sampling probabilities, not the degree count itself.

> [!info] Mean degrees and bi-coordinates
> **Theorem.** Under these distributions,
>
> $$
> \boxed{b^i_{\mathrm{in}}=1-\frac12\mathbb E\deg_{T_{\mathrm{in}}}(i),
> \qquad
> b^i_{\mathrm{out}}=1-\frac12\mathbb E\deg_{T_{\mathrm{out}}}(i)}
> \tag{8}
> $$

> [!proof]- Derivation using arc-inclusion probabilities
> **Proof.** Let $\mathcal T_{\mathrm{in}}$ sum incoming-tree weights over all roots. For a row Laplacian, the matrix-tree theorem and determinant formula give
>
> $$
> \mathcal T_{\mathrm{in}}=\det(\mathbf L+\mathbf\Pi),
> \qquad
> \mathbf\Pi=\frac1n\mathbf1\mathbf1^{\mathsf T}
> $$
>
> At a balanced matrix, $\mathcal T_{\mathrm{in}}=n\tau$ and $(\mathbf L+\mathbf\Pi)^{-1}=\mathbf{Gr}+\mathbf\Pi$. For coordinate columns $\boldsymbol\delta_i$, one has $\partial\mathbf L/\partial f_{ij}=\boldsymbol\delta_i(\boldsymbol\delta_i-\boldsymbol\delta_j)^{\mathsf T}$. Therefore
>
> $$
> \Pr\{i\to j\in T_{\mathrm{in}}\}
> =f_{ij}\frac{\partial\log\mathcal T_{\mathrm{in}}}{\partial f_{ij}}
> =f_{ij}(\mathrm{Gr}_{ii}-\mathrm{Gr}_{ji})
> $$
>
> Differentiate the tree polynomial for an arbitrary row Laplacian, then evaluate at the balanced matrix. An intermediate single-arc change need not preserve balance.
>
> The mean outgoing degree of a vertex in an incoming tree is $1-1/n$: it is one unless that vertex is the root. From $\mathbf{Gr}\mathbf L=\mathbf J$, incoming-arc probabilities sum to $1-1/n-(\mathbf L^{\mathsf T}\mathbf q)_i$. Hence
>
> $$
> \mathbb E\deg_{T_{\mathrm{in}}}(i)
> =2-\frac2n-(\mathbf L^{\mathsf T}\mathbf q)_i
> $$
>
> Substituting (3) gives the first formula in (8). Reversing all arcs replaces $\mathbf L$ by $\mathbf L^{\mathsf T}$ and incoming trees by outgoing trees, while preserving the Green diagonal. This proves the second formula. $\square$

Every tree has total degree $2(n-1)$, so (8) directly explains why both coordinate sums equal $1$. A coordinate is positive, zero, or negative according as the mean degree is less than, equal to, or greater than two. Negative bi-coordinates are allowed.

For an undirected graph, forgetting the root gives the usual weighted spanning-tree distribution in both cases. The formula reduces to $b^i=1-\mathbb E\deg_T(i)/2$; its connection with resistance curvature is discussed in [2]. The directional formulas (8) are derived separately here.

## Example: two coordinate systems and one radius

Continue the [[The Gram Matrix and Directional Coordinates of a Balanced Graph#An example with unequal directional pairings|cycle example with an added bidirectional coupling]]. Its matrices $\mathbf L,\mathbf{Gr},\mathbf G$ are already known. Direct inversion gives

$$
\mathbf G_z^{-1}=
\begin{pmatrix}
2&-1&-1&1/4\\
-2&2&0&1/3\\
0&-1&1&5/12\\
1/3&1/4&5/12&41/144
\end{pmatrix}
$$

Thus

$$
\mathbf b_{\mathrm{out}}=\frac1{12}\begin{pmatrix}4\\3\\5\end{pmatrix},
\qquad
\mathbf b_{\mathrm{in}}=\frac1{12}\begin{pmatrix}3\\4\\5\end{pmatrix},
\qquad
\rho=\frac{41}{144}
$$

For each orientation there are four arborescences on the weighted arcs, with total weight $6=3\tau$, where $\tau=2$. Independent enumeration gives:

| Vertex | $\mathbb E\deg_{T_{\mathrm{out}}}$ | $b^i_{\mathrm{out}}$ | $\mathbb E\deg_{T_{\mathrm{in}}}$ | $b^i_{\mathrm{in}}$ |
| --- | --- | --- | --- | --- |
| $a$ | $4/3$ | $1/3$ | $3/2$ | $1/4$ |
| $b$ | $3/2$ | $1/4$ | $4/3$ | $1/3$ |
| $c$ | $7/6$ | $5/12$ | $7/6$ | $5/12$ |

Orthogonality to sources selects the incoming column; orthogonality to receivers selects the outgoing row. Both representatives have norm $41/144$.

For comparison, the symmetric pair-resistance geometry has circumcenter coordinates $(2/7,2/7,3/7)$ and squared Euclidean radius $2/7$. This illustrates the distinction above; $\rho$ remains the corner entry of $\mathbf G_z^{-1}$.

## Scope and status

The unit border connects a common affine weight with balance. An unbalanced Laplacian has different left and right kernels, so recovering it requires another border or prior balancing. Outgoing-weight scaling is treated in [[Balancing a Directed Graph by Spanning-Tree Potentials]]. Disconnected balanced graphs are treated componentwise: one border does not remove every degenerate direction.

Inversion of bordered balanced matrices using a pseudoinverse appears in [1, Lemma 4, equation (34)]. Here the formulas for the canonical local Gram matrix are proved, giving two sphere representatives and their directed-tree coordinates. Resistance radius is defined algebraically with the symmetric PMG normalization retained. The note also draws on the author's PMG research.

Exact rational checks inverted the Gram matrix independently of (2)-(4) and enumerated arborescences to obtain mean degrees and arc probabilities independently of (8). Sphere pairings, isotropic corrections, and the symmetric limit were also checked.

1. Balaji, R.; Bapat, R. B.; Goel, S. [Resistance matrices of balanced directed graphs](https://arxiv.org/abs/1906.01165). *Linear and Multilinear Algebra*, 70 (2022), 787-808; Lemma 4 in the [preprint](https://arxiv.org/pdf/1906.01165).
2. Devriendt, K. [Graphs with Nonnegative Resistance Curvature](https://doi.org/10.1007/s00026-025-00774-x). *Annals of Combinatorics*, 30 (2026), 415-438; the definition of resistance curvature and proof of Theorem 3.8.
