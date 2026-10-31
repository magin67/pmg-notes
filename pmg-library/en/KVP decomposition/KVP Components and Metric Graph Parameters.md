---
title: KVP Components and Metric Graph Parameters
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-components-and-graph-metric-parameters
lang: en
order: 7
description: "What KVP adds to metric parameters: which components centralities see, the role of P in the radius, mixed contributions to center displacement, spanning-tree sensitivities, and compactness. A separate extension of Foster's identity to balanced graphs."
---

Resistance radius, the Kirchhoff index, centralities, and the spanning-tree coefficient are already defined in [[Metric Parameters of Graphs]]. Here KVP is used to study which parts of pair data these parameters retain, which differences between graphs they miss, and how they depend on components acting together.

The main results concern three questions. The Kirchhoff index and centroid centralities use only part of the KVP resistance data. The radius additionally depends on the position of the sphere center, and P can change it while K and V remain fixed. The spanning-tree coefficient connects conductance components with resistance components through derivatives and Foster's identity.

A scalar parameter has no automatic rule $f(C)=f(C_K)+f(C_V)+f(C_P)$. Individual components generally have coefficients of both signs and are not separate graphs with positive metrics. Each type of contribution is therefore defined explicitly below.

## Scope and notation

Until the section on balanced graphs, consider a connected loopless undirected graph on $n\ge3$ vertices. Its conductance table C is symmetric, with $c_{ij}\ge0$ and $c_{ii}=0$. Zero entries for absent couplings participate in the decomposition on the same footing as other pairs.

Use the matrices

$$
L=\operatorname{diag}(C\mathbf1)-C,
\qquad
\mathrm{Gr}=L^+,
\qquad
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

The Green matrix inverts L on $H=\mathbf1^\perp$; $L\mathrm{Gr}=\mathrm{Gr}L=J$. The symmetric resistances are

$$
R_{ij}=q_i+q_j-2\mathrm{Gr}_{ij},
\qquad q_i=\mathrm{Gr}_{ii},
\qquad t=\operatorname{tr}\mathrm{Gr}
$$

G remains reserved for Gram matrices. In this note, R does not denote the one-way resistance table r.

Decompose the two pair tables separately:

$$
C=C_K+C_V+C_P,
\qquad
R=R_K+R_V+R_P
$$

For couplings, set $N=\binom n2$, $W=\sum_{i<j}c_{ij}$, and

$$
\mu=\frac WN,
\qquad
v_i=\sum_jc_{ij}-(n-1)\mu
$$

For resistances, use a different vertex vector:

$$
\operatorname{Kf}=\sum_{i<j}R_{ij}=nt,
\qquad
s_i=\sum_jR_{ij},
\qquad
w_i=s_i-\frac{2\operatorname{Kf}}n
$$

Then $\sum_i v_i=\sum_i w_i=0$, and for $i\ne j$,

$$
(C_V)_{ij}=\frac{v_i+v_j}{n-2},
\qquad
(R_V)_{ij}=\frac{w_i+w_j}{n-2}
$$

These are parameters of different tables. Their connection passes through nonlinear Laplacian inversion, as shown in [[KVP Decomposition of the Green Matrix and Resistances]].

## Which components the Kirchhoff index and centralities see

The previously proved formulas $s_i=nq_i+t$ and $\operatorname{Kf}=nt$ give

$$
\boxed{
\operatorname{Kf}=N\mu_R,
\qquad
q_i=\frac{\operatorname{Kf}}{n^2}+\frac{w_i}{n}
}
\tag{1}
$$

Here $\mu_R$ is the constant coefficient of $R_K$.

In [[Centroid, Spanning-Tree, and Eigenvector Centralities]], centroid centrality is defined through normalized values $1/q_i$. Consequently:

- The Kirchhoff index is determined by $R_K$ alone.
- Centroid centrality values are determined by $R_K$ and $R_V$.
- Ranking vertices by proximity to the centroid is determined by the order of $w_i$: smaller $w_i$ means greater centrality.
- Changing only $R_P$, provided the resulting table remains the resistance table of an admissible graph, changes neither the Kirchhoff index nor these centralities.

These statements concern components of R. They do not imply that the parameters are independent of $C_P$. The conductance component $C_P$ can affect all components of R through inversion of L.

Spanning-tree centrality has a different dependence. It is determined by the mean vertex degree in a random weighted spanning tree:

$$
\delta_i=\sum_jc_{ij}R_{ij},
\qquad
C_i^{\mathrm{tree}}=\frac{\delta_i}{2(n-1)}
$$

Here direct and inverse pair data are multiplied. Constancy of centroid centralities as described above therefore does not guarantee constancy of spanning-tree centralities.

## Radius: overall level and center displacement

Let $x_i$ be the vertices of a Euclidean realization of the resistance simplex, $h=n^{-1}\sum_i x_i$ its centroid, and p the center of its circumsphere. Denote the center's bi-coordinates by $\boldsymbol\alpha$:

$$
p=\sum_i\alpha_i x_i,
\qquad
\mathbf1^{\mathsf T}\boldsymbol\alpha=1
$$

The resistance radius $\rho=(p-x_i)^2$ is quadratic; the linear radius is $\sqrt\rho$. The formulas from [[Centroid, Spanning-Tree, and Eigenvector Centralities#Expected spanning-tree degree and circumcenter coordinates|the connection between the center and spanning-tree degrees]] are

$$
\boldsymbol\alpha=\frac1n\mathbf1+\frac12L\mathbf q,
\qquad
\alpha_i=1-\frac{\delta_i}{2},
\qquad
\rho=\frac{t}{n}+\frac14\mathbf q^{\mathsf T}L\mathbf q
$$

Here $\mathbf q=(q_i)$ is the Green diagonal. Substituting (1) and using $L\mathbf1=0$ gives

$$
\boxed{
\begin{aligned}
\boldsymbol\alpha-\frac1n\mathbf1&=\frac1{2n}L\mathbf w\\
\rho&=\underbrace{\frac{\operatorname{Kf}}{n^2}}_{\rho_0}+\frac1{4n^2}\mathbf w^{\mathsf T}L\mathbf w
\end{aligned}
}
\tag{2}
$$

This rewrites known metric formulas to isolate the role of $R_V$. That component determines w, while the Laplacian L specifies how the corresponding displacement is measured.

> [!info] Radius: overall level and center displacement
> **Corollary.** For a connected undirected graph,
>
> $$
> \boxed{
> \rho\ge\rho_0,
> \qquad
> \rho=\rho_0
> \ \Longleftrightarrow\ R_V=0
> \ \Longleftrightarrow\ p=h
> }
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** L is positive definite on H. Hence $\mathbf w^{\mathsf T}L\mathbf w=0$ is equivalent to $\mathbf w=0$. This is equivalent to $R_V=0$, and the first formula in (2) then gives $\boldsymbol\alpha=\mathbf1/n$. $\square$

The P-component of R does not appear explicitly in (2), but it contributes to recovering L. Thus when $R_V$ is nonzero, the same vertex vector w can correspond to different center displacements and radii.

## Example: identical resistance K and V, different radii

On four vertices, specify two tables:

$$
R^{(0)}=\frac12
\begin{pmatrix}
0&4&4&5\\
4&0&3&4\\
4&3&0&4\\
5&4&4&0
\end{pmatrix},
\qquad
R^{(1)}=\frac14
\begin{pmatrix}
0&6&9&11\\
6&0&7&9\\
9&7&0&6\\
11&9&6&0
\end{pmatrix}
$$

Both have $\mu_R=2$, and their V-coefficients on pairs $ab,ac,ad,bc,bd,cd$ are

$$
R_V:\quad\left(0,0,\frac12,-\frac12,0,0\right)
$$

Only their P-components differ:

$$
R_P^{(0)}=0,
\qquad
R_P^{(1)}:\quad\frac14(-2,1,1,1,1,-2)
$$

Both tables are realized by connected graphs with positive conductances. This is checked by recovering $\mathrm{Gr}=-JRJ/2$, $L=\mathrm{Gr}^+$, and $c_{ij}=-L_{ij}$ for $i\ne j$:

| Pair | $c_{ij}^{(0)}$ | $c_{ij}^{(1)}$ |
| --- | ---: | ---: |
| $ab$ | $1/4$ | $26/51$ |
| $ac$ | $1/4$ | $8/51$ |
| $ad$ | $3/20$ | $4/51$ |
| $bc$ | $5/12$ | $16/51$ |
| $bd$ | $1/4$ | $8/51$ |
| $cd$ | $1/4$ | $26/51$ |

![[Same resistance K and V - different radii.svg]]

*The two positive coupling networks from the table. Vertex positions are schematic and do not form a resistance embedding. The graphs have identical K- and V-components of R and identical centroid centralities, but different P-components of R, sphere-center coordinates, and radii.*

In both cases,

$$
\operatorname{Kf}=12,
\qquad
\mathbf q=\frac18(7,5,5,7)^{\mathsf T},
\qquad
\mathbf C^{\mathrm{cent}}=\frac1{24}(5,7,7,5)^{\mathsf T}
$$

Other parameters nevertheless differ:

| Parameter | Graph 0 | Graph 1 |
| --- | --- | --- |
| Center bi-coordinates $\boldsymbol\alpha$ | $(5,3,3,5)/16$ | $(2,1,1,2)/6$ |
| $\rho_0$ | $3/4$ | $3/4$ |
| $(p-h)^2=\rho-\rho_0$ | $1/64$ | $1/48$ |
| $\rho$ | $49/64$ | $37/48$ |
| Spanning-tree coefficient $\tau$ | $4/15$ | $16/51$ |

Thus the K- and V-components of resistance do not determine the radius or sphere center. The example also distinguishes centroid and spanning-tree centralities: $\mathbf q$ is the same, whereas $\delta_i=2(1-\alpha_i)$ changes.

## Decomposing the radius at a fixed graph metric

Set $L_X=\mathscr L(C_X)$, where $X\in\{K,V,P\}$. Using $L=L_K+L_V+L_P$, decompose the second term of (2).

> [!info] Decomposing the radius at a fixed graph metric
> **Definition.** With w computed for the full original graph, define
>
> $$
> \rho_X=\frac1{4n^2}\mathbf w^{\mathsf T}L_X\mathbf w
> =\frac1{4n^2}\sum_{i<j}(C_X)_{ij}(w_i-w_j)^2
> $$

Then

$$
\boxed{\rho=\rho_0+\rho_K+\rho_V+\rho_P}
\tag{4}
$$

Here $\rho_X$ is the contribution to the evaluation of center displacement defined above, not the radius of graph $C_X$ and not the derivative of the radius along that component. The vector w already depends on all couplings through the Green matrix.

Explicit formulas are useful for computing the contributions:

$$
\rho_K=\frac{\mu}{4n}\sum_iw_i^2,
\qquad
\rho_V=\frac1{4n(n-2)}\sum_i v_iw_i^2,
\qquad
\rho_P=-\frac1{2n^2}\sum_{i<j}(C_P)_{ij}w_iw_j
\tag{5}
$$

> [!note]- Derivation
> **Derivation.** On H, the matrix $L_K$ equals $n\mu I_H$. For $\sum_iw_i=0$, direct summation gives
>
> $$
> \mathbf w^{\mathsf T}L_V\mathbf w
> =\frac{n}{n-2}\sum_i v_iw_i^2
> $$
>
> Finally, $L_P=-C_P$ because $C_P$ has zero row sums. Substituting into the definition of $\rho_X$ gives (5). $\square$

The K-contribution is nonnegative. The V- and P-contributions may have either sign; their total together with the K-contribution is nonnegative. For unit-weight graphs on five vertices:

| Graph | $\operatorname{Kf}$ | $\rho_0$ | $\rho_K$ | $\rho_V$ | $\rho_P$ | $\rho$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Complete graph $K_5$ | $4$ | $4/25$ | $0$ | $0$ | $0$ | $4/25$ |
| Cycle $C_5$ | $10$ | $2/5$ | $0$ | $0$ | $0$ | $2/5$ |
| Star $K_{1,4}$ | $16$ | $16/25$ | $18/125$ | $27/125$ | $0$ | $1$ |
| Path $P_5$ | $20$ | $4/5$ | $7/25$ | $-1/25$ | $-1/25$ | $1$ |

Equality of the star and path radii follows from tree invariance, discussed in [[Density, Compactness, and Tree Invariance]]. KVP shows how the constituents of that common value differ. The cycle has nonzero P-components in both couplings and resistances, but $R_V=0$, so its center coincides with its centroid and every $\rho_X$ is zero.

## Center bi-coordinates and mixed metric contributions

The first formula in (2) gives another useful collection of contributions:

$$
\mathbf a_X=\frac1{2n}L_X\mathbf w,
\qquad
\boldsymbol\alpha=\frac1n\mathbf1+\mathbf a_K+\mathbf a_V+\mathbf a_P
\tag{6}
$$

Each column $\mathbf a_X$ has zero sum and represents an affine vector from the centroid. This is a decomposition of bi-coordinates induced by coupling components at fixed w. A vertex column itself has no separate P-sector: all three contributions belong to the same space H.

Let $z_X=\sum_i(\mathbf a_X)_i x_i$ be the corresponding geometric vectors. Then

$$
p-h=z_K+z_V+z_P,
\qquad
z_X\cdot z_Y=\mathbf a_X^{\mathsf T}\mathrm{Gr}\mathbf a_Y
$$

Coefficient orthogonality of $C_K,C_V,C_P$ does not imply metric orthogonality of $z_K,z_V,z_P$. Therefore

$$
\boxed{
\rho-\rho_0
=\sum_X z_X^2+2\sum_{X<Y}z_X\cdot z_Y
}
\tag{7}
$$

The sum over $X<Y$ runs over the three distinct pairs of sectors. These are actual mixed metric terms.

For the path $P_5$, the matrix of these inner products in K, V, P order is

$$
\bigl(z_X\cdot z_Y\bigr)_{X,Y}
=\frac1{225}
\begin{pmatrix}
90&-12&-15\\
-12&2&1\\
-15&1&5
\end{pmatrix}
$$

The diagonal entries sum to $97/225$, whereas all entries sum to $45/225=1/5=\rho-\rho_0$. Mixed products account for the difference. Incorrectly transferring coefficient orthogonality to the metric would give a different radius.

The connection with (4) is

$$
\rho_X=\sum_Y z_X\cdot z_Y
$$

Indeed, $\sum_Y\mathbf a_Y=L\mathbf w/(2n)$ and $\mathrm{Gr}L\mathbf w=\mathbf w$. Thus the rows of the displayed matrix sum to $7/25,-1/25,-1/25$. Negative $\rho_V,\rho_P$ are compatible with nonnegative norms $z_V^2,z_P^2$: they include mixed products.

## The spanning-tree coefficient and matching Foster contributions

The weighted spanning-tree coefficient $\tau$ is a homogeneous polynomial of degree $n-1$ in the couplings. Under decomposition of C, it contains mixed products of components. To study them, introduce

$$
\Theta(\kappa,\nu,\pi)
=\frac1n\det\nolimits_H(\kappa L_K+\nu L_V+\pi L_P),
\qquad
\Theta(1,1,1)=\tau
$$

The determinant is taken in an orthonormal basis of H. The full polynomial and its mixed coefficients belong to the study of exponentials and toponomes. Here we consider derivatives at the original point.

> [!info] The spanning-tree coefficient and matching Foster contributions
> **Definition.** Set
>
> $$
> F_X=\left.\frac{\partial\log\Theta}{\partial x_X}\right|_{(1,1,1)},
> \qquad (x_K,x_V,x_P)=(\kappa,\nu,\pi)
> $$

> [!info] The spanning-tree coefficient and matching Foster contributions
> **Theorem.** These sensitivities admit a representation pairing matching components:
>
> $$
> \boxed{
> F_X=\operatorname{tr}(\mathrm{Gr}L_X)
> =\langle C_X,R\rangle_0
> =\langle C_X,R_X\rangle_0,
> \qquad
> F_K+F_V+F_P=n-1
> }
> \tag{8}
> $$
>
> Here $\langle A,B\rangle_0=\sum_{i<j}A_{ij}B_{ij}$.

> [!note]- Proof
> **Proof.** The derivative of the log determinant on H is $\operatorname{tr}(\mathrm{Gr}L_X)$. Since
>
> $$
> L_X=\sum_{i<j}(C_X)_{ij}
> (\mathbf e_i-\mathbf e_j)(\mathbf e_i-\mathbf e_j)^{\mathsf T}
> $$
>
> the trace equals $\sum_{i<j}(C_X)_{ij}R_{ij}$. Orthogonality of the pair sectors retains only $R_X$. The traces sum to $\operatorname{tr}(\mathrm{Gr}L)=\operatorname{tr}J=n-1$. $\square$

Consequently,

$$
F_K=\mu\operatorname{Kf},
\qquad
F_V=\frac1{n-2}\sum_i v_iw_i,
\qquad
F_P=\sum_{i<j}(C_P)_{ij}(R_P)_{ij}
\tag{9}
$$

This pairs direct and inverse pair structures. Mixed contractions of different sectors vanish in the sum over all pairs, but R itself already depends nonlinearly on every component of C.

| Unit-weight graph | $F_K$ | $F_V$ | $F_P$ | Sum |
| --- | ---: | ---: | ---: | ---: |
| $K_5$ | $4$ | $0$ | $0$ | $4$ |
| $C_5$ | $5$ | $0$ | $-1$ | $4$ |
| $K_{1,4}$ | $32/5$ | $-12/5$ | $0$ | $4$ |
| $P_5$ | $8$ | $-4/3$ | $-8/3$ | $4$ |

For an existing edge, $c_{ij}R_{ij}$ is its inclusion probability in a weighted random spanning tree, as used in [[Centroid, Spanning-Tree, and Eigenvector Centralities]]. Individual terms $(C_X)_{ij}R_{ij}$ and sums $F_X$, however, are not probabilities. They may be negative and include pairs with no original coupling.

The derivatives are defined near the original L, which is positive definite on H. The change $C+\varepsilon C_X$ need not preserve nonnegativity of all couplings. Physical admissibility of a variation must be checked separately; in general, $F_X$ is the derivative of the spanning-tree polynomial in the chosen algebraic direction.

## Consequences for compactness

[[Density, Compactness, and Tree Invariance]] defines compactness based on the Kirchhoff index, with mean weighted degree $\bar d=(n-1)\mu$, by

$$
\eta_K=\frac{(n-1)^2}{\bar d\operatorname{Kf}}
$$

Formula (9) gives its KVP representation:

$$
\boxed{
\eta_K=\frac{n-1}{F_K},
\qquad
\eta_K^{-1}-1=-\frac{F_V+F_P}{n-1}
}
\tag{10}
$$

> [!info] Consequences for compactness
> **Corollary.** In the symmetric model, $F_K\ge n-1$ and $F_V+F_P\le0$. Equality holds exactly for the complete graph with equal conductances.

> [!note]- Proof
> **Proof.** For the positive Laplacian eigenvalues $\lambda_2,\ldots,\lambda_n$, Cauchy's inequality gives
>
> $$
> \left(\sum_{k=2}^n\lambda_k\right)
> \left(\sum_{k=2}^n\lambda_k^{-1}\right)\ge(n-1)^2
> $$
>
> The left side is $(n-1)\mu\operatorname{Kf}=(n-1)F_K$. Equality requires all nonzero eigenvalues to be equal, that is, $L=\lambda J$. This is the Laplacian of a complete graph with constant conductance $\lambda/n$. $\square$

Thus the total compactness deficit relative to the reference can be expressed through matching V- and P-contractions. These are not two nonnegative shares: it is the combined quantity $-(F_V+F_P)$ that is nonnegative.

For radius-based compactness from the same series, the factorization remains

$$
\eta_\rho=\eta_K\frac{\rho_0}{\rho}
$$

In KVP terms, the additional factor equals 1 exactly when $R_V=0$. With nonzero resistance V, it accounts for displacement of the sphere center, which also depends on the other graph data.

## What remains valid for balanced graphs

Now let C be the arc table of a connected balanced graph with nonnegative weights. Balance does not imply regularity: $C_U=0$, but $C_V$ may be nonzero. We have $C=C_K+C_V+C_P+C_O$ and still $L\mathrm{Gr}=\mathrm{Gr}L=J$.

For the common spanning-tree coefficient of one fixed root, set $F_X=\operatorname{tr}(\mathrm{Gr}L_X)$, $X\in\{K,V,P,O\}$. These are derivatives of the logarithm of the corresponding four-parameter spanning-tree polynomial. From the definition of one-way resistance,

$$
r_{ij}=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}
$$

we obtain

$$
F_X=\sum_{i\ne j}(C_X)_{ij}
(\mathrm{Gr}_{ii}-\mathrm{Gr}_{ji})
=\sum_{i\ne j}(C_X)_{ij}r_{ji}
$$

The reversed index order is essential. With $\langle A,B\rangle_0=\frac12\sum_{i\ne j}A_{ij}B_{ij}$ for oriented tables, KVPOU orthogonality gives

$$
\boxed{
F_X=\langle C_X,R_X\rangle_0\quad(X=K,V,P),
\qquad
F_O=-2\langle C_O,r_O\rangle_0
}
\tag{11}
$$

Here $R=r+r^{\mathsf T}$, and $r_O$ is the circulation component of r. Its U-component does not contribute to the contractions because C has no U-component. As before,

$$
F_K+F_V+F_P+F_O=n-1
$$

For the unit directed 3-cycle, $\mu_C=1/2$ and all $R_{ij}=1$ for $i\ne j$, so

$$
F_K=\frac32,
\qquad F_V=F_P=0,
\qquad F_O=\frac12
$$

The sum is 2. The symmetric table R does not contain all information needed for this contraction: the O-contribution is required. This also shows that the symmetric inequality $F_K\ge n-1$ does not extend to balanced graphs.

Radius formulas (2)-(7) above use a symmetric metric and a symmetric Laplacian. In a general balanced graph, the Euclidean geometry of R describes only the symmetric part of the pairing, whereas canonical center coordinates and the PMG radius require the full bilinear Gram matrix. These distinctions are discussed in [[The Gram Matrix and Directional Coordinates of a Balanced Graph]] and [[The Isotropic Space and Sphere of a Balanced Graph]]. Substituting nonsymmetric L into symmetric formulas is not a proved extension. This note makes no metric claims for arbitrary unbalanced digraphs.

## Status of results and connections with the rest of the series

The underlying metric parameter formulas come from [[Metric Parameters of Graphs]]. Their KVP consequences, matching contractions, mixed products, and balanced formula (11) are justified here.

Numerical results were checked using exact rational arithmetic. The radius and bi-coordinates were independently recovered from $R\boldsymbol\alpha=2\rho\mathbf1$, $\mathbf1^{\mathsf T}\boldsymbol\alpha=1$. For the four unit-weight and two weighted examples, spanning-tree coefficients and mean spanning-tree degrees were also found by enumerating trees. Derivatives of the spanning-tree polynomial were checked from its values without using the trace formula. The general formulas were additionally checked on 15 symmetric graphs with 3-7 vertices and 12 balanced graphs with 3-6 vertices.

Here KVP distinguishes the information retained by a parameter, provides computable sensitivities, and gives specific decompositions at fixed data of the entire graph. It does not turn a nonlinear parameter into a sum of values on three separate positive graphs.

[[The Second-Order Symmetric Potential and KVP Decomposition]] proves the sector decomposition of the quadratic potential and its relation to the tetrahedron identity. The joint spanning-tree polynomial and other forest coefficients are developed in [[Forest Toponomes of KVP Components]]. Their mixed dependencies must be distinguished from coefficient orthogonality and from Foster's identity.

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.
