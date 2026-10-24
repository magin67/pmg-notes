---
title: Balancing a Directed Graph by Spanning-Tree Potentials
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: directed-graph-balancing-by-spanning-tree-potentials
order: 10
description: 'Positive scaling of outgoing couplings by spanning-tree potentials: uniqueness, computation, applications, and comparison with additive balancing.'
source_revision: 1
---

In a general digraph, a vertex's incoming and outgoing weights can differ. Can this imbalance be removed while preserving existing arcs and each source's allocation proportions? For a strongly connected digraph, yes: multiply all outgoing couplings of each vertex by its spanning-tree potential. Once the overall scale is fixed, this method is unique.

This gives the potentials from [[Balanced Graphs and Spanning-Tree Potentials]] an applied meaning and converts a digraph into a balanced graph with a PMG bilinear metric. Balancing changes weights; it does not merely rewrite the original Laplacian.

## The problem and the direction of scaling

Let $\mathbf F=(f_{ij})$ contain nonnegative weights on $n\ge2$ vertices, with $f_{ii}=0$. The first index is the **source**, the second the **receiver**: $f_{ij}$ weights $i\to j$. Set

$$
d_i^{\mathrm{out}}=\sum_j f_{ij},\qquad
d_i^{\mathrm{in}}=\sum_j f_{ji},\qquad
\mathbf L=\operatorname{diag}(d^{\mathrm{out}})-\mathbf F
$$

Always $\mathbf L\mathbf1=0$. Until the limitations section, assume that the positive-arc graph is strongly connected.

Seek positive multipliers $\sigma_i$, common to all couplings from one source:

$$
f_{ij}^{\mathrm{bal}}=\sigma_i f_{ij},\qquad
\mathbf F_{\mathrm{bal}}=\mathbf D_\sigma\mathbf F,
\qquad
\mathbf D_\sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n)
$$

Left multiplication scales rows. Right multiplication would scale by receivers, defining a different problem.

Balance at vertex $i$ requires

$$
\sigma_i d_i^{\mathrm{out}}=\sum_j\sigma_j f_{ji}
$$

Thus the problem reduces to one equation:

$$
\boxed{\mathbf L^{\mathsf T}\sigma=0}
\tag{1}
$$

## Balancing multipliers and spanning-tree potentials

The original digraph's spanning-tree potentials are

$$
\tau_i=\det\mathbf L_{\widehat i,\widehat i},\qquad
T=\sum_i\tau_i
$$

By the directed matrix-tree theorem, $\tau_i$ sums weights of spanning trees toward $i$. Strong connectedness gives $\tau_i>0$. Also $\tau^{\mathsf T}\mathbf L=0$, proved using the adjugate in [[Balanced Graphs and Spanning-Tree Potentials]].

The common scale of a solution to (1) is free. Normalize the mean multiplier to one:

$$
\boxed{\sigma_i=\frac{n\tau_i}{T},\qquad
\sum_i\sigma_i=n}
\tag{2}
$$

Here $\tau_i$ are the minors themselves and $\sigma_i$ the normalized balancing multipliers. This distinction preserves the definition of a spanning-tree potential.

> [!info] Balancing through spanning-tree potentials
> **Theorem.** For a strongly connected digraph with nonnegative weights, $\mathbf F_{\mathrm{bal}}=\mathbf D_\sigma\mathbf F$, with $\sigma$ from (2), is balanced. Its Laplacian is
>
> $$
> \boxed{\mathbf L_{\mathrm{bal}}=\mathbf D_\sigma\mathbf L}
> \tag{3}
> $$
>
> Among positive scalings of outgoing couplings, this is the unique solution with $\sum_i\sigma_i=n$.

> [!note]- Proof
> **Proof.** The scaled outgoing weight is $\sigma_i d_i^{\mathrm{out}}$, so the Laplacian transforms as (3). Its row and column sums vanish:
>
> $$
> \mathbf L_{\mathrm{bal}}\mathbf1=\mathbf D_\sigma\mathbf L\mathbf1=0,
> \qquad
> \mathbf1^{\mathsf T}\mathbf L_{\mathrm{bal}}=\sigma^{\mathsf T}\mathbf L=0
> $$
>
> This is balance. Positive multipliers preserve weight signs and the arc set.
>
> If another positive scaling $\mathbf D_v\mathbf F$ is balanced, then $v^{\mathsf T}\mathbf L=0$. Strong connectedness gives rank $n-1$, so the left kernel is one-dimensional and $v$ is proportional to $\tau$. Normalization fixes the proportionality factor uniquely. $\square$

Diagonal balancing via the directed matrix-tree theorem also appears in network systems theory [1, §4.1]. That source uses the transposed Laplacian convention, placing the diagonal multiplier on the right.

## What is preserved and the sense of projection

Scaling preserves existing arcs, their directions, and strong connectedness. Two positive couplings from one source satisfy

$$
\frac{f_{ij}^{\mathrm{bal}}}{f_{ik}^{\mathrm{bal}}}
=\frac{f_{ij}}{f_{ik}}
$$

The relative outgoing-allocation matrix is also preserved:

$$
p_{ij}=\frac{f_{ij}}{d_i^{\mathrm{out}}}
=\frac{f_{ij}^{\mathrm{bal}}}{d_i^{\mathrm{bal}}},
\qquad
d_i^{\mathrm{bal}}=\sigma_i d_i^{\mathrm{out}}
\tag{4}
$$

Absolute weights, their total sum, spanning-tree potentials, and metric parameters generally change. The condition $\sum_i\sigma_i=n$ fixes the mean multiplier, not total flow. If an application requires the original total weight, multiply the result by the ratio of the old total to the new one; that is another choice of common scale.

Write $\mathcal B(\mathbf F)=\mathbf F_{\mathrm{bal}}$ for normalized balancing.

> [!info] Idempotence
> **Corollary.** On strongly connected digraphs,
>
> $$
> \mathcal B(\mathcal B(\mathbf F))=\mathcal B(\mathbf F)
> $$
>
> If the original graph is balanced, $\mathcal B(\mathbf F)=\mathbf F$.

> [!note]- Proof
> **Proof.** A connected balanced graph has equal spanning-tree potentials, so its normalized multipliers are all $1$. The first application produces precisely such a graph. $\square$

In this sense, $\mathcal B$ is a **nonlinear projection onto balanced graphs**. Preserving outgoing proportions distinguishes it. No minimal-change assertion in a matrix metric is included.

The output $\mathbf F_{\mathrm{bal}}$ alone does not recover the original graph. Retaining the multipliers makes the transformation reversible:

$$
\boxed{\mathbf F=\mathbf D_\sigma^{-1}\mathbf F_{\mathrm{bal}}}
$$

The pair $(\mathbf F_{\mathrm{bal}},\sigma)$ separates a balanced matrix from individual source scales.

## How spanning-tree potentials become equal

For any positive vector $v$, principal minors of $\mathbf D_v\mathbf L$ satisfy

$$
\tau_i(\mathbf D_v\mathbf F)
=\tau_i(\mathbf F)\prod_{k\ne i}v_k
\tag{5}
$$

All rows except the deleted row $i$ are scaled in the minor. Equivalently, each tree toward $i$ uses exactly one outgoing arc from every nonroot vertex and none from the root.

With $v=\sigma$, equation (2) gives

$$
\tau_i(\mathbf F_{\mathrm{bal}})
=\frac{T}{n}\prod_k\sigma_k
=\left(\frac nT\right)^{n-1}\prod_k\tau_k
$$

The right side is independent of the root. Scaling therefore directly equalizes all spanning-tree potentials.

Conversely, starting from a balanced graph and multiplying outgoing couplings at $i$ by $v_i>0$ makes the new potentials proportional to $1/v_i$. Balancing multipliers compensate for these changes up to a common scale.

## A three-participant example

Suppose each matrix row contains one participant's ratings of the others:

$$
\mathbf F=
\begin{pmatrix}
0&1&2\\
2&0&1\\
1&1&0
\end{pmatrix},\qquad
\mathbf L=
\begin{pmatrix}
3&-1&-2\\
-2&3&-1\\
-1&-1&2
\end{pmatrix}
$$

Outgoing sums are $(3,3,2)$, incoming sums $(3,2,3)$, so the graph is unbalanced. Principal minors give

$$
(\tau_a,\tau_b,\tau_c)=(5,4,7),\qquad
\sigma=\frac3{16}(5,4,7)^{\mathsf T}
$$

Scaling rows yields

$$
\mathbf F_{\mathrm{bal}}=\frac3{16}
\begin{pmatrix}
0&5&10\\
8&0&4\\
7&7&0
\end{pmatrix}
$$

The displayed integer matrix precedes the common factor $3/16$; its row and column sums both equal $(15,12,14)$. For the normalized matrix:

| Vertex | Outgoing weight $d_i^{\mathrm{out}}$ | Incoming weight $d_i^{\mathrm{in}}$ | Multiplier $\sigma_i$ | Balanced weight $d_i^{\mathrm{bal}}$ |
| --- | ---: | ---: | ---: | ---: |
| $a$ | $3$ | $3$ | $15/16$ | $45/16$ |
| $b$ | $3$ | $2$ | $12/16$ | $36/16$ |
| $c$ | $2$ | $3$ | $21/16$ | $42/16$ |

The new spanning-tree potentials all equal $315/64$. Any principal cofactor verifies this; all three were checked independently in this example.

Vertex $c$ has the largest multiplier, whereas $a$ has the largest balanced weight. These are different quantities: $\sigma_i$ scales the source's ratings, while $d_i^{\mathrm{bal}}$ is the resulting weighted incoming total, equal to its outgoing total.

Balancing specifies a model for reconciling ratings. Equal input and output alone do not establish a fair ranking; interpretation depends on the original weights' meaning.

## Computing the balancing

Computing $n$ determinants is unnecessary. Solve

$$
\mathbf L^{\mathsf T}\sigma=0,\qquad
\mathbf1^{\mathsf T}\sigma=n
$$

In practice, replace one row of the first equation by the normalization. An equivalent square system is

$$
\left(\mathbf L^{\mathsf T}+\frac{\mathbf1\mathbf1^{\mathsf T}}n\right)\sigma=\mathbf1
\tag{6}
$$

Its matrix is nonsingular. Left multiplication of (6) by $\mathbf1^{\mathsf T}$ yields normalization, leaving (1); uniqueness follows from the theorem.

The computational steps are:

1. Check strong connectedness of positive arcs and construct $\mathbf L$.
2. Solve the normalized system for $\sigma$.
3. Multiply row $i$ of $\mathbf F$ by $\sigma_i$.
4. Check multiplier positivity and equality of incoming and outgoing sums within numerical precision.

For large sparse matrices, replacing one normalization row avoids forming the dense addition in (6). A nearly disconnected graph can give an ill-conditioned system; negative roundoff-sized values must be distinguished from absence of a positive solution.

## Flow-allocation interpretations

In a distribution network, $f_{ij}$ may describe transfer intensity from $i$ to $j$. The multiplier $\sigma_i$ changes the source's overall scale while preserving recipient shares. Equation (1) means no accumulation at internal vertices of the resulting network. If original weights represent real deliveries with external inflow, outflow, or storage, their imbalance has a meaning of its own; eliminating it changes the model.

For a continuous-time Markov interpretation, set $\mathbf Q=-\mathbf L$. Then

$$
\pi_i=\frac{\sigma_i}{n}
$$

is stationary, since $\pi^{\mathsf T}\mathbf Q=0$ and $\sum_i\pi_i=1$. The matrix $\mathbf F_{\mathrm{bal}}/n$ gives the original chain's stationary flows $\pi_i f_{ij}$. If $-\mathbf L_{\mathrm{bal}}$ instead generates a new chain, its stationary distribution is uniform. The change preserves next-vertex probabilities (4) but changes exit rates.

For the discrete chain with $\mathbf P=(p_{ij})$ from (4), stationary probabilities are different:

$$
\nu_i=\frac{\sigma_i d_i^{\mathrm{out}}}
{\sum_k\sigma_k d_k^{\mathrm{out}}}
\tag{7}
$$

The balance equation gives $\sum_i\nu_i p_{ij}=\nu_j$. If the original weights are row-normalized, $d_i^{\mathrm{out}}=1$, then $\nu_i=\sigma_i/n$. Generally, a balancing multiplier differs from a discrete-chain stationary weight. These interpretations are unnecessary for defining balancing, whose basis is equation (1).

## Why additive balancing gives a different result

Another natural problem allows additive corrections to all matrix entries and minimizes their squared sum. Let $\delta_i=d_i^{\mathrm{out}}-d_i^{\mathrm{in}}$, so $\sum_i\delta_i=0$. Then

$$
\psi_i=\frac{\delta_i}{2n},\qquad
A_{ij}=\psi_i-\psi_j,\qquad
\mathbf F_{\mathrm{add}}=\mathbf F-\mathbf A
$$

gives an additive decomposition into a balanced part and a gradient correction.

> [!note]- Orthogonality of the additive decomposition
> **Proof.** The imbalance at row $i$ of $\mathbf A$ is
>
> $$
> \sum_j(A_{ij}-A_{ji})=2n\psi_i=\delta_i
> $$
>
> Hence $\mathbf F_{\mathrm{add}}$ is balanced. For any balanced matrix $\mathbf X$, the Frobenius inner product satisfies
>
> $$
> \langle\mathbf A,\mathbf X\rangle_F
> =\sum_i\psi_i\left(\sum_jX_{ij}-\sum_jX_{ji}\right)=0
> $$
>
> Thus $\mathbf F_{\mathrm{add}}$ is the orthogonal projection onto the vector space of balanced real matrices. $\square$

This projection may create new arcs and negative weights, and change source proportions. No sign or support constraints have been imposed; including them would define a different minimization problem.

Multiplicative balancing solves the original problem of preserving positive arcs and outgoing proportions. It is distinct from this additive orthogonal projection.

## When positive balancing is impossible

For a connected digraph, strong connectedness is necessary: positive scaling preserves all arcs, while a connected balanced graph is strongly connected. A connected graph with arcs between different strongly connected components therefore cannot be balanced this way while retaining every positive arc.

With one closed strongly connected component, spanning-tree potentials are positive inside it and zero outside. Scaling by these potentials removes outgoing arcs of all other vertices. With several closed components, every principal minor of order $n-1$ vanishes, so (2) is unavailable.

If a disconnected graph has strongly connected weak components, balance each separately, choosing their common scales independently. Balancing strong components separately when arcs run between them is insufficient: the intercomponent imbalance remains.

## Connection with the metric and further work

After balancing, $\mathbf L_{\mathrm{bal}}$ has zero row and column sums. It admits [[The Bilinear Laplacian of a Balanced Graph|boundary-form representations]], [[One-Way Resistance and Hitting Times|one-way resistances]], and the [[The Isotropic Space and Sphere of a Balanced Graph|balanced isotropic construction]]. The resulting parameters belong to the balanced graph; assigning them to the original digraph needs a separate definition.

Another transformation is resistance symmetrization using $R_{ij}=r_{ij}+r_{ji}$. It preserves pair resistances and removes the metric's circulation part, but may require negative coupling weights. This is a separate question from balancing by spanning-tree potentials.

## Status and sources

The main construction is the known diagonal balancing through the Laplacian kernel and directed matrix-tree theorem [1]. Here we give its proof, normalization, projection properties, transformation of tree potentials, and comparison with additive balancing. The applied presentation also draws on the author's PMG research.

The example was checked with exact rational arithmetic. Multipliers were obtained independently from principal minors and the normalized linear system; row sums, column sums, and tree potentials were recomputed after scaling. Repeated balancing, recovery of the original matrix, and (7) were also checked.

1. Van der Schaft, A. J. [Modeling of Physical Network Systems](https://arxiv.org/abs/1510.04984). Preprint, 2015. [§4.1](https://arxiv.org/html/1510.04984v1#S4.SS1): balancing via spanning trees; §4.3: network consensus applications.

The directed matrix-tree theorem and balance criterion are proved in [[Balanced Graphs and Spanning-Tree Potentials]].
