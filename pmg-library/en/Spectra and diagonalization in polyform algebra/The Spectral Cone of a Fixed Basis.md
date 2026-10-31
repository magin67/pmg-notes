---
title: "The Spectral Cone of a Fixed Basis"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: spectral-cone-of-a-fixed-basis
order: 5
description: "Graph sign constraints in a fixed eigenbasis, the polyhedral spectral cone, simultaneous diagonalization, and the distinction between the Chebyshev orbit and the full cone."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Спектральный конус фиксированного базиса|Русский]]

A fixed eigenbasis allows an operator to vary through its diagonal coefficients. However, not every nonnegative coefficient tuple defines a graph Laplacian: after returning to vertex coordinates, some conductances may be negative. Admissible tuples form a convex polyhedral cone.

[[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]] constructs a special family of graphs sharing the path basis. Here we consider the entire set of admissible Laplacians in a chosen basis. The $P_3$ example reveals its full geometry, variation of polyforms, and the limits of interpreting the Greenian as a graph Laplacian.

## Fixed directions and conductance constraints

Let $n\ge2$ and $d=n-1$. Fix the coordinate inner product $\langle\mathbf z,\mathbf y\rangle_0=\mathbf z^{\mathsf T}\mathbf y$ and an orthonormal basis

$$
\mathbf U=(\mathbf u_0,\mathbf u_1,\ldots,\mathbf u_d),\qquad
\mathbf u_0=\frac{\mathbf1}{\sqrt n},\qquad H=\mathbf1^\perp
$$

For $\boldsymbol\mu=(\mu_1,\ldots,\mu_d)\in\mathbb R^d$, put

$$
\mathbf L(\boldsymbol\mu)=
\mathbf U\operatorname{diag}(0,\mu_1,\ldots,\mu_d)\mathbf U^{\mathsf T}
$$

The number $\mu_k$ belongs to the specific mode $\mathbf u_k$. Sorting the numbers without correspondingly permuting the modes changes the operator. Cone coordinates are therefore coefficients ordered relative to the basis, not the spectrum as a multiset.

The matrix $\mathbf L(\boldsymbol\mu)$ is symmetric and has zero row sums. For $i\ne j$, define the candidate conductance

$$
w_{ij}(\boldsymbol\mu)=-L_{ij}(\boldsymbol\mu)
=-\sum_{k=1}^d\mu_k u_k(i)u_k(j)
$$

> [!info] Fixed directions and conductance constraints
> **Definition.** The Laplacian spectral cone of the basis $\mathbf U$ is
>
> $$
> \boxed{\mathcal K_U=
> \{\boldsymbol\mu\in\mathbb R^d:\ w_{ij}(\boldsymbol\mu)\ge0\ \text{for all }i<j\}}
> $$

Its corresponding matrix cone is $\{\mathbf L(\boldsymbol\mu):\boldsymbol\mu\in\mathcal K_U\}$. The map between them is linear and one-to-one: $\mu_k=\mathbf u_k^{\mathsf T}\mathbf L\mathbf u_k$. Pairs with $w_{ij}>0$ are graph edges; $w_{ij}=0$ means the edge is absent.

> [!info] Fixed directions and conductance constraints
> **Lemma.** The sign constraints in the definition already imply $\mu_k\ge0$.

> [!note]- Proof
> **Proof.** Zero row sums give $L_{ii}=\sum_{j\ne i}w_{ij}$. Thus, for any $\mathbf z\in\mathbb R^n$,
>
> $$
> \mathbf z^{\mathsf T}\mathbf L\mathbf z
> =\sum_{i<j}w_{ij}(z_i-z_j)^2\ge0
> $$
>
> Substituting $\mathbf z=\mathbf u_k$ gives $\mu_k\ge0$. $\square$

Separate eigenvalue nonnegativity constraints may therefore be added, but are redundant. The converse fails: for example, the square of a path Laplacian is positive semidefinite with zero row sums, yet its entries between vertices at distance two are positive.

The coordinate inner product and basis remain fixed. For a connected graph, the PMG resistance inner product is determined by $\mathbf{Gr}=\mathbf L^+$ and depends on $\boldsymbol\mu$; these identifications are distinguished in [[en/Foundations/Core specification|Core specification]].

## Cone geometry and its boundary

> [!info] Cone geometry and its boundary
> **Proposition.** $\mathcal K_U$ is a closed convex polyhedral cone of full dimension $d$ containing no lines.

> [!note]- Proof
> **Proof.** Every $w_{ij}$ depends linearly on $\boldsymbol\mu$. The cone is therefore the intersection of finitely many closed homogeneous half-spaces. Nonnegativity of its coordinates shows that it can contain both $\boldsymbol\mu$ and $-\boldsymbol\mu$ only when $\boldsymbol\mu=0$.
>
> For full dimension, consider the complete graph with equal conductance $c>0$:
>
> $$
> \mathbf L_{K_n(c)}=c(n\mathbf I-\mathbf1\mathbf1^{\mathsf T}),\qquad
> \boldsymbol\mu=(nc,\ldots,nc)
> $$
>
> All inequalities $w_{ij}>0$ are strict here and remain strict in a neighborhood. Thus the cone has an interior point in $\mathbb R^d$. $\square$

Adding cone points adds the conductances of their graphs on the same vertex set. Multiplying by a positive number changes the overall conductance scale and preserves the edge set.

The interior is defined by $w_{ij}>0$ for every pair. If any conductance vanishes, the point lies on the boundary: the corresponding linear functional is not identically zero, since it is positive on the complete graph. Conditions $w_{ij}=0$ define faces; not every original inequality necessarily defines a distinct facet.

**Connectedness is determined by a different condition:**

$$
\boldsymbol\mu\in\mathcal K_U\text{ defines a connected graph}
\quad\Longleftrightarrow\quad \mu_k>0\ \text{for all }1\le k\le d
$$

Indeed, the energy formula shows that the Laplacian kernel consists of functions constant on each connected component. Its dimension equals the number of components. The constant mode is already included; additional components occur when additional $\mu_k$ vanish.

A connected graph with missing edges therefore lies on the cone boundary. The cone boundary and the set of disconnected graphs are different sets.

## A complete example: the eigenbasis of P3

Take the modes from [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]]:

$$
\mathbf u_1=\frac1{\sqrt2}(1,0,-1)^{\mathsf T},\qquad
\mathbf u_2=\frac1{\sqrt6}(1,-2,1)^{\mathsf T}
$$

Put $a=\mu_1$ and $b=\mu_2$. These are scalar parameters, not the formal vertices $a_i$. Direct substitution gives

$$
\mathbf L(a,b)=
\begin{pmatrix}
a/2+b/6&-b/3&-a/2+b/6\\
-b/3&2b/3&-b/3\\
-a/2+b/6&-b/3&a/2+b/6
\end{pmatrix}
$$

Hence

$$
w_{12}=w_{23}=\frac b3,\qquad
w_{13}=\frac{3a-b}{6},\qquad
\boxed{\mathcal K_U=\{(a,b):a\ge0,\ 0\le b\le3a\}}
$$

Let $E$ be the graph consisting of the unit edge $\{1,3\}$ and isolated vertex $2$. Its spectral point is $(2,0)$; the unit path $P_3$ has point $(1,3)$. Every cone point has a unique decomposition along these two rays:

$$
(a,b)=\frac b3(1,3)+\frac{3a-b}{6}(2,0)
$$

The decomposition coefficients are conductances directly: the first is assigned to both path edges, and the second to $\{1,3\}$. Thus both boundary rays are extreme.

On the ray $b=3a>0$, the graph is a connected path. On $b=0$, $a>0$, it has one edge and one isolated vertex. Inside the angle $0<b<3a$, all three conductances are positive and the graph is a weighted triangle.

A simple unweighted graph requires $w_{ij}\in\{0,1\}$. There are exactly four such graphs in this basis:

| Point $(a,b)$ | $w_{12}=w_{23}$ | $w_{13}$ | Graph |
|---|---:|---:|---|
| $(0,0)$ | $0$ | $0$ | Three isolated vertices |
| $(2,0)$ | $0$ | $1$ | $E$: edge $\{1,3\}$ and vertex $2$ |
| $(1,3)$ | $1$ | $0$ | Path $P_3$ |
| $(3,3)$ | $1$ | $1$ | Complete graph $K_3$ |

Vertex labels and the basis are fixed: the statement concerns specific labeled graphs.

![[The Cone of the P3 Basis and Its Graphs.svg]]

*Figure 1. The cone $0\le b\le3a$ in the coefficient plane of the two path modes. Its extreme rays are generated by $E$ and $P_3$. The path lies on the connected part of the boundary, while $K_3$ lies in the interior. Points corresponding to simple unweighted graphs are marked separately; intermediate points usually describe weighted graphs.*

## Polyforms and coefficients inside the cone

Let $u_k=\sum_i u_k(i)a_i\in W$ and $A_k=[u_k]^2$. The forms $A_k$ are fixed together with the basis. For any cone point,

$$
L(\boldsymbol\mu)=\sum_{k=1}^d\mu_k A_k,\qquad
M(t;\boldsymbol\mu)=\exp(tL)=\prod_{k=1}^d(e+t\mu_k A_k)
$$

Thus

$$
M_g(\boldsymbol\mu)=e_g(\mu_1A_1,\ldots,\mu_dA_d)
$$

These are elementary symmetric polynomials in the commutative algebra of forms. Coordinate evaluation of a basis form $[u_I]^2$ is $1$, so it sends $M_g$ to $e_g(\mu_1,\ldots,\mu_d)$, the rooted forest coefficient $p_g$. Ordinary forest coefficients $f_g$ have a different normalization and combinatorial meaning; see [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

For a connected cone point,

$$
\Delta=\prod_{k=1}^d\mu_k=n\tau,\qquad
\operatorname{tr}\mathbf{Gr}=\sum_{k=1}^d\frac1{\mu_k},\qquad
\operatorname{Kf}=n\sum_{k=1}^d\frac1{\mu_k}
$$

These are the classical spectral expressions for the spanning-tree coefficient and Kirchhoff index, consistent with the normalizations in [[en/Polynomial toponomes/Coefficients and Kirchhoff Indices|Coefficients and Kirchhoff Indices]]. For a weighted graph, $\tau$ is the sum of conductance products over spanning trees and need not be an integer.

In the $P_3$ example,

$$
\begin{aligned}
M(t;a,b)&=e+t(aA_1+bA_2)+t^2abA_1A_2\\
P(t)&=1+(a+b)t+ab\,t^2\\
F(t)&=1+\frac{a+b}{2}t+\frac{ab}{3}t^2
\end{aligned}
$$

Here $P$ is the rooted forest polynomial and $F$ the ordinary forest polynomial. The last formula can be checked directly: the conductances sum to $(a+b)/2$, and the products over the three possible trees sum to $ab/3$.

For $a,b>0$, $\tau=ab/3$ and $\operatorname{Kf}=3(a^{-1}+b^{-1})$. As $b\to0$ with fixed $a>0$, the spanning-tree coefficient tends to zero and the Greenian trace grows without bound. At the disconnected point itself, the pseudoinverse exists but is not the limit of these Greenians and does not induce a nondegenerate metric on all of $H$.

## Inverting eigenvalues and duality

At a connected cone point all $\mu_k>0$, so

$$
\mathbf{Gr}(\boldsymbol\mu)=\sum_{k=1}^d\mu_k^{-1}\mathbf u_k\mathbf u_k^{\mathsf T},\qquad
\mathrm{Gr}(\boldsymbol\mu)=\sum_{k=1}^d\mu_k^{-1}A_k
$$

In the algebraically dual basis $u^1,\ldots,u^d$, put $A_k^\vee=[u^k]^2$. Then

$$
D(t;\boldsymbol\mu)=\exp(tQ_1)=\prod_{k=1}^d(e+t\mu_k^{-1}A_k^\vee)
$$

The centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$, $h=n^{-1}\sum_i a_i$, sends $A_k^\vee$ to $A_k$ and $D(t)$ to $\exp(t\mathrm{Gr})$. It is determined by coordinate orthonormality, not the changing resistance metric.

The parameter $t$ marks the grade at a fixed cone point $\boldsymbol\mu$. The dual pair is taken at $t=1$; scaling conductances by a positive factor $s$ gives $M(s;\boldsymbol\mu)$ and $D(s^{-1};\boldsymbol\mu)$, according to the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter convention]].

Complementing eigendirection sets gives

$$
\prod_{k\in I}\mu_k^{-1}=\frac{\prod_{k\notin I}\mu_k}{\Delta},\qquad
M_d/Q_g=M_{d-g}
$$

This reversal of complementary grades is proved in [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]]. It holds regardless of the signs of the Greenian's off-diagonal entries.

For $P_3$, the dual expression is

$$
D(t;a,b)=e+t(a^{-1}A_1^\vee+b^{-1}A_2^\vee)+\frac{t^2}{ab}A_1^\vee A_2^\vee
$$

In particular, with $N=\exp(\mathrm{Gr})$ and $T_3=3A_1A_2$,

$$
M_2=\frac{ab}{3}T_3,\qquad N_2=\frac1{3ab}T_3
$$

However, $(a,b)\mapsto(a^{-1},b^{-1})$ need not preserve the Laplacian cone. Writing $\alpha=1/a$ and $\beta=1/b$, the image of the connected part of $\mathcal K_U$ is

$$
\{(\alpha,\beta):\alpha>0,\ \beta\ge\alpha/3\}
$$

For the Green matrix itself to be a graph Laplacian with nonnegative conductances, one also needs $\beta\le3\alpha$. In the original parameters this means

$$
\boxed{a>0,\qquad a/3\le b\le3a}
$$

**Example.** The point $(a,b)=(4,1)$ lies inside the cone and gives conductances

$$
w_{12}=w_{23}=\frac13,\qquad w_{13}=\frac{11}{6}
$$

Its Greenian has matrix

$$
\mathbf{Gr}(4,1)=\frac1{24}
\begin{pmatrix}
7&-8&1\\
-8&16&-8\\
1&-8&7
\end{pmatrix}
$$

The eigenvalues $1/4$ and $1$ are positive and row sums vanish, but $\mathrm{Gr}_{13}=1/24>0$. Interpreting this matrix as a Laplacian would therefore require negative conductance $-1/24$ between vertices $1$ and $3$.

The Greenian still correctly defines the original resistance metric: for example, $R_{13}=2/a=1/2$. The signs in its edge representation are discussed in [[en/Greenian and polyform duality/The Canonical Vector Representation of the Greenian|The Canonical Vector Representation of the Greenian]]. Here they appear as the reciprocal eigenvalue tuple leaving the Laplacian cone.

![[Inverting Spectral Coordinates in the P3 Basis.svg]]

*Figure 2. Left: the connected part of the original cone for $a,b>0$. Right: its image under $(a,b)\mapsto(1/a,1/b)$. The green region corresponds to cases where both matrices are graph Laplacians. The orange region contains admissible original graphs whose Greenians violate the Laplacian sign condition. The map $(4,1)\mapsto(1/4,1)$ is marked. Panel scales differ; coordinate axes are excluded from the inversion domain.*

## Connection with the Perron spectracone

Cones of diagonal coefficients for a fixed diagonalizing matrix have been studied previously. Johnson and Paparella define the **Perron spectracone**

$$
\mathcal C(\mathbf S)=
\{\boldsymbol\eta:\ \mathbf S\operatorname{diag}(\boldsymbol\eta)\mathbf S^{-1}\ge0\}
$$

The inequality means entrywise nonnegativity, not positive semidefiniteness. The definition and polyhedrality appear in [Johnson–Paparella, Definition 3.1 and Proposition 3.4](https://arxiv.org/pdf/1508.07400#page=4). For our orthogonal $\mathbf U$, its relationship with $\mathcal K_U$ can be stated exactly.

> [!info] Connection with the Perron spectracone
> **Proposition.** The Laplacian cone is a linear image of the Perron spectracone:
>
> $$
> \mathcal K_U=
> \{(\eta_0-\eta_1,\ldots,\eta_0-\eta_d):
> \boldsymbol\eta\in\mathcal C(\mathbf U)\}
> $$

> [!note]- Proof
> **Proof.** Let $\mathbf L=\mathbf L(\boldsymbol\mu)$ be an admissible Laplacian. Choose $s\ge\max_iL_{ii}$. Then
>
> $$
> \mathbf A=s\mathbf I-\mathbf L\ge0,\qquad
> \boldsymbol\eta=(s,s-\mu_1,\ldots,s-\mu_d)\in\mathcal C(\mathbf U)
> $$
>
> Indeed, the diagonal entries are nonnegative by the choice of $s$, and the off-diagonal entries are conductances. The differences $\eta_0-\eta_k$ recover $\mu_k$.
>
> Conversely, let $\mathbf A=\mathbf U\operatorname{diag}(\boldsymbol\eta)\mathbf U^{\mathsf T}\ge0$. The constant first mode gives $\mathbf A\mathbf1=\eta_0\mathbf1$. Thus $\mathbf L=\eta_0\mathbf I-\mathbf A$ is symmetric, has zero row sums and nonpositive off-diagonal entries. It is a Laplacian with eigenvalue coefficients $\eta_0-\eta_k$. $\square$

The terminology and general method thus connect to the existing theory of spectral cones. The displayed identity gives the specific transition to the Laplacian sign condition. In this section $\mathcal C(\mathbf U)$ denotes the cone from that work; $\mathcal C$ without a matrix argument above denotes the centered identification of PMG spaces.

## Simultaneous diagonalization and the Chebyshev orbit

If a symmetric operator $\mathbf L_0$ has simple spectrum and eigenbasis $\mathbf U$, then a symmetric matrix $\mathbf A$ is diagonal in that basis if and only if $\mathbf A\mathbf L_0=\mathbf L_0\mathbf A$. Indeed, commutation preserves every one-dimensional eigenspace of $\mathbf L_0$.

For repeated eigenvalues, the eigenspaces are preserved, but $\mathbf A$ need not be diagonal inside them in a prescribed basis. The existence of a common orthonormal basis for a commuting family of symmetric operators is classical [Brouwer–Haemers, Proposition 2.1.1](https://aeb.win.tue.nl/2WF02/spectra.pdf#page=31). It does not single out a unique basis inside a repeated eigenspace. For example, the Laplacian of $K_n$ is scalar on $H$ and commutes with every graph Laplacian on the same vertices.

The path orbit from [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]] consists of particular points $\mu_k=\Phi_m(\lambda_k)$ in its cone. For $P_3$ and $m=0,1,2,3$, they are

$$
(0,0),\quad(1,3),\quad(3,3),\quad(4,0)
$$

The points then repeat. The cone contains continuous conductance families. Even in this small example, the simple graph $E$ at $(2,0)$ is absent from the orbit, although it lies on the same ray as the orbit point $(4,0)$. Nevertheless, the conic hull of the $P_3$ orbit is the whole cone, because it contains both extreme rays. Equality of the conic hull and the cone does not mean equality of the original sets.

For $n\ge4$, $K_n$ belongs to the cone of every such basis and is absent from the path's Chebyshev orbit. Moreover, if a simple unweighted graph $G$ is diagonal in $\mathbf U$, its complement has Laplacian

$$
\mathbf L_{\overline G}=n\mathbf I-\mathbf1\mathbf1^{\mathsf T}-\mathbf L_G
$$

and coefficients $n-\mu_k$ in the same basis. This statement concerns the complement of a simple graph; subtracting arbitrary conductances from a complete graph requires a separate sign check.

The full cone describes admissible graphs with fixed modes. Approximating an arbitrary Laplacian by a point in this cone and the associated data loss are studied in [[en/Spectra and diagonalization in polyform algebra/Projection onto a Fixed Spectral Basis and Loss of Information|Projection onto a Fixed Spectral Basis and Loss of Information]].

## Status and sources

Cones associated with a fixed diagonalizing basis and simultaneous diagonalization belong to classical matrix theory. This note derives the Laplacian conditions, their relationship with the Perron spectracone, and the complete two-dimensional example. Diagonal forms, exterior exponentials, and complementary grades use current PMG normalizations; no novelty is claimed for the general cone construction.

The $P_3$ formulas were checked exactly: spectral and edge-built matrices, conductances, extreme rays and simple graphs, direct and dual grades, ordinary and rooted forest coefficients, the Greenian, and effective resistances. Coordinate inversion and the Perron spectracone connection were checked independently on rational examples. The figures use these verified formulas; finite computations do not replace the general proofs given above.

- [C. R. Johnson, P. Paparella. Perron Spectratopes and the Real Nonnegative Inverse Eigenvalue Problem](https://arxiv.org/abs/1508.07400): Definition 3.1 and Proposition 3.4 - the Perron spectracone and its polyhedrality. The Laplacian cone is related to it by the linear map proved above.
- [A. E. Brouwer, W. H. Haemers. Spectra of Graphs, authors' text](https://aeb.win.tue.nl/2WF02/spectra.pdf): §2.1, Proposition 2.1.1 - simultaneous diagonalization. [Book page and corrections](https://homepages.cwi.nl/~aeb/math/ipm/).
- [[en/Foundations/Core specification|Core specification]], [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], and [[en/Greenian and polyform duality/The Canonical Vector Representation of the Greenian|The Canonical Vector Representation of the Greenian]]: spaces, metric evaluations, exponentials, and signs of Greenian coefficients.
- [Checks and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral): computations for the spectral cone of the $P_3$ basis.

Navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
