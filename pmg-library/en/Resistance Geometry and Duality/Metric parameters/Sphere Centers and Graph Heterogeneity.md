---
title: Sphere Centers and Graph Heterogeneity
date: 2026-11-03
updated: 2026-11-10
revision: 3
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: sphere-centres-and-graph-heterogeneity
order: 6
description: "Circumcenters of the simplices with Laplacian and Green Gram matrices: coordinates, bordering, degree diffusion, displacement from the centroid, and limits of interpretation through symmetry and bottlenecks."
---

A connected graph has two mutually inverse simplex geometries, with the Green matrix and the Laplacian as their Gram matrices. Their circumspheres generally have different centers and radii. In resistance geometry, the center coordinates are related to expected spanning-tree degrees; in Laplacian geometry, they are determined by the network's response to deviations of weighted degrees from their mean.

This note derives formulas for the second center, compares both centers' displacements from their centroids, and clarifies what these quantities measure. They characterize particular forms of heterogeneity, but provide neither a criterion for structural asymmetry nor a universal bottleneck measure.

Prerequisites: [[Laplacian, Green Matrix, and Effective Resistance Matrix|matrix conversions]], [[The Greenian Metric and Potentials|the Laplacian as the metric of the Greenian exponential]], and [[Centroid, Spanning-Tree, and Eigenvector Centralities|the decomposition of resistance radius through the centroid]].

Russian version: [[Центры сфер и неоднородность графа]].

Bi-coordinates $\alpha^i,\beta^i$ have upper indices. We use the upper/lower summation convention from [[Bi-coordinates and Di-coordinates|the coordinate note]].

## Two geometries of one graph

Consider a finite connected undirected loopless graph on $n\ge2$ vertices. Conductances $c_{ij}=c_{ji}$ are positive on existing edges and zero on absent ones. Write

$$
L_{ii}=d_i=\sum_jc_{ij},\qquad
L_{ij}=-c_{ij}\quad(i\ne j),\qquad
\mathbf{Gr}=\mathbf L^+
$$

The matrices $\mathbf L$ and $\mathbf{Gr}$ are positive definite on $\mathbf1^\perp$, have kernel $\operatorname{span}\{\mathbf1\}$, and satisfy

$$
\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J,\qquad
\mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

For a symmetric matrix $\mathbf A$, define

$$
\mathcal D(\mathbf A)_{ij}=A_{ii}+A_{jj}-2A_{ij}
$$

> [!info] Resistance and Laplacian simplices
> **Definition.** The resistance simplex is the Euclidean simplex whose centered position vectors have Gram matrix $\mathbf{Gr}$. The Laplacian simplex is the simplex with Gram matrix $\mathbf L$. Their squared-distance matrices are, respectively,
>
> $$
> \mathbf R=\mathcal D(\mathbf{Gr}),\qquad
> \mathbf Q=\mathcal D(\mathbf L)
> $$
>
> In particular, for $i\ne j$,
>
> $$
> Q_{ij}=d_i+d_j+2c_{ij}
> $$

Both simplices are nondegenerate in dimension $n-1$. A planar drawing of the original graph specifies neither geometry. In particular, $Q_{ij}$ is not the effective resistance in the original network.

In PMG these geometries already appear as the metrics of normalized potentials in $\exp L$ and $\exp(\mathrm{Gr})$: the first has matrix $\mathbf{Gr}$, the second $\mathbf L$. See the [[The Greenian Metric and Potentials#The Laplacian as the metric of the Greenian exponential|metric identity]] and the [[The Greenian Metric and Potentials#Centered vertices, cuts, and differences|potentials of centered vertices]]. The distance matrix $\mathbf Q$ here differs from the grade polyforms $Q_k$.

In the figure, one network with conductances $7,1,1$ defines two different triangles. Each geometry shows its centroid $h$ and circumcenter $O$. The symbols $\alpha$ and $\beta$ denote circumcenter bi-coordinates in the resistance and Laplacian geometries, respectively, and $\rho$ and $\sigma$ their squared radii; the values are calculated below. First distinguish the geometries themselves.

![[images/Centers of Two Simplices - Triangle 7 1 1.svg]]

*One network and its two simplex geometries. $O$ denotes the circumcenter and $h$ the centroid. The geometric panels use independent scales. The resistance center lies inside the triangle; the Laplacian center lies beyond side $12$.*

## The Laplacian circumcenter

Write $h_L$ for the centroid of the Laplacian simplex, $O_L$ for its circumcenter, and $\beta$ for the barycentric coordinates of $O_L$ in its vertices. These are unit-sum coordinates of an affine combination; they correspond to bi-coordinates in PMG terminology.

In this note, $\sigma$ denotes the square of the linear circumradius of the Laplacian simplex. This local notation differs from the symbol for the top coefficient $\tau(\exp(\mathrm{Gr}))$ in the [[The Greenian Metric and Potentials|note on Greenian potentials]].

> [!info] Center coordinates and radius
> **Proposition.** The center and squared radius are uniquely determined by
>
> $$
> \boxed{\mathbf Q\beta=2\sigma\mathbf1,\qquad
> \mathbf1^{\mathsf T}\beta=1}
> \tag{1}
> $$
>
> If
>
> $$
> \bar d=\frac1n\sum_i d_i,\qquad
> b=d-\bar d\mathbf1,\qquad
> u=\frac1n\mathbf1
> $$
>
> then
>
> $$
> \boxed{\mathbf L\beta=\frac12b,\qquad
> \beta=u+\frac12\mathbf{Gr}\,b}
> \tag{2}
> $$
>
> $$
> \boxed{\sigma=\bar d+\frac14b^{\mathsf T}\mathbf{Gr}\,b}
> \tag{3}
> $$

These formulas specialize the general simplex-center formulas to the Gram matrix $\mathbf L$. The general construction, including arbitrary simplices, is presented in [2, §2.4, Theorem 2 and formula (14)].

> [!note]- Derivation of the center formulas
> **Proof.** Choose the centroid as the origin. For the position vectors $y_i$, we have $y_i\cdot y_j=L_{ij}$ and $O_L=\beta^i y_i$. Equidistance means
>
> $$
> d_i-2(\mathbf L\beta)_i+\beta^{\mathsf T}\mathbf L\beta=\sigma
> $$
>
> Averaging over $i$ gives $\sigma=\bar d+\beta^{\mathsf T}\mathbf L\beta$; subtracting the mean gives the first equality in (2). Pseudoinversion and the unit-sum condition give the second. Therefore
>
> $$
> \beta^{\mathsf T}\mathbf L\beta
> =\frac14b^{\mathsf T}\mathbf{Gr}\,b
> $$
>
> This proves (3). Finally,
>
> $$
> \mathbf Q=d\mathbf1^{\mathsf T}+\mathbf1d^{\mathsf T}-2\mathbf L,\qquad
> d^{\mathsf T}\beta=\bar d+\frac12b^{\mathsf T}\mathbf{Gr}\,b
> $$
>
> Substitution gives (1). Conversely, applying $\mathbf J$ to (1) recovers $\mathbf L\beta=b/2$. The coordinate sum then determines $\beta$, and the equation determines $\sigma$. $\square$

For an affine column $q$, with $\mathbf1^{\mathsf T}q=1$, we also obtain

$$
\frac12q^{\mathsf T}\mathbf Qq
=\sigma-(q-\beta)^{\mathsf T}\mathbf L(q-\beta)
$$

Hence $\beta$ is the unique maximizer of this quadratic function on the unit-sum hyperplane. There is no constraint $q^i\ge0$. Adding that constraint defines a different optimization problem and may change the center.

## Comparison with the resistance circumcenter

As in [[Centroid, Spanning-Tree, and Eigenvector Centralities]], put $r_i=\mathrm{Gr}_{ii}$ and $r=(r_i)$. Write $h_R,O_R$ for the resistance centroid and circumcenter. From the [[Centroid, Spanning-Tree, and Eigenvector Centralities#Expected spanning-tree degree and circumcenter coordinates|resistance-center formulas]], we have

$$
\alpha=u+\frac12\mathbf Lr,\qquad
\Delta_R:=\|O_R-h_R\|^2=\frac14r^{\mathsf T}\mathbf Lr
$$

$$
\rho=\frac{\operatorname{tr}\mathbf{Gr}}n+\Delta_R
$$

| Characteristic | Resistance simplex | Laplacian simplex |
|---|---|---|
| Gram matrix of centered position vectors | $\mathbf{Gr}$ | $\mathbf L$ |
| Squared distances | $\mathbf R$ | $\mathbf Q$ |
| Center coordinates | $\alpha=u+\mathbf Lr/2$ | $\beta=u+\mathbf{Gr}b/2$ |
| Squared linear radius | $\rho$ | $\sigma$ |
| Center displacement | $\Delta_R=r^{\mathsf T}\mathbf Lr/4$ | $\Delta_L=b^{\mathsf T}\mathbf{Gr}b/4$ |
| Condition for coincidence with the centroid | $r$ is constant | $d$ is constant |

The resistance sums satisfy

$$
R_i=\sum_jR_{ij}=nr_i+\operatorname{tr}\mathbf{Gr}
$$

Thus $\Delta_R=0$ is equivalent to constant $R_i$. For unit-conductance graphs this is the known property of resistance regularity [4, Introduction and §2]. It differs from constant degree, which determines $\Delta_L=0$.

For the resistance center,

$$
\alpha^i=1-\frac12\sum_jc_{ij}R_{ij}
$$

In [3, definition (2) and Appendix B.3], these coordinates are studied as vertex resistance curvature. That result concerns the simplex with Gram matrix $\mathbf{Gr}$. Exchanging the matrices does not establish such an interpretation for $\beta$.

## Electrical response to degree heterogeneity

Since $\mathbf1^{\mathsf T}b=0$, the column $b$ is an admissible balanced distribution of external currents. The zero-mean solution is

$$
\varphi=\mathbf{Gr}\,b,\qquad
\mathbf L\varphi=b,\qquad
\mathbf1^{\mathsf T}\varphi=0
$$

Thus $\beta^i=1/n+\varphi_i/2$. Vertices whose degree exceeds the mean act as sources; those below the mean act as sinks. The values $\varphi_i$ account for the entire redistribution of currents, not just the degree of the vertex itself.

The power for numerical current values $b_i$ is

$$
\mathcal E=\sum_{i<j}c_{ij}(\varphi_i-\varphi_j)^2
=\varphi^{\mathsf T}\mathbf L\varphi
=b^{\mathsf T}\mathbf{Gr}\,b
$$

Each undirected edge is counted once. With physical units, choose a voltage scale $U_0$: the currents are $I=U_0b$, the voltages $U_0\varphi$, and the power $U_0^2\mathcal E$. The physical dimension of $\sigma$ itself is conductance, not power.

The electrical potential $\varphi_i$ and the normalized potential of a polyform are different concepts. Their relation to the quadratic energy form is discussed in the [[The Greenian Metric and Potentials#The Laplacian as the metric of the Greenian exponential|Greenian metric]].

## Center displacement and diffusion

In the following formulas, $\|\cdot\|$ is the ordinary linear Euclidean norm. Under the PMG convention, $\|O-h\|^2$ is the quadratic norm of the displacement vector.

> [!info] Geometric meaning of the radius correction
> **Corollary.** The squared distance between the circumcenter and the centroid is
>
> $$
> \boxed{
> \Delta_L:=\|O_L-h_L\|^2
> =\sigma-\bar d
> =\frac14b^{\mathsf T}\mathbf{Gr}\,b
> }
> \tag{4}
> $$
>
> In particular,
>
> $$
> O_L=h_L
> \quad\Longleftrightarrow\quad
> \beta=u
> \quad\Longleftrightarrow\quad
> d_1=\cdots=d_n
> $$

> [!note]- Proof
> **Proof.** In a centered realization, $\|O_L-h_L\|^2=\beta^{\mathsf T}\mathbf L\beta$. Formula (4) follows from (2)-(3). The matrix $\mathbf{Gr}$ is positive definite on $\mathbf1^\perp$, so $\Delta_L=0$ is equivalent to $b=0$. $\square$

The quantity $\sigma$ combines the mean degree and the center displacement. Thus equal values of $\sigma$ need not mean equal heterogeneity.

For a dynamic interpretation, start symmetric diffusion on the original network from the degree values:

$$
\dot x(t)=-\mathbf Lx(t),\qquad
x(0)=d,\qquad
x(t)\longrightarrow\bar d\mathbf1
$$

The Laplacian is unnormalized; equilibrium is constant across vertices.

> [!info] Integrated measures of degree equalization
> **Proposition.** For this diffusion,
>
> $$
> \boxed{
> \beta-u=\frac12\int_0^\infty
> \bigl(x(t)-\bar d\mathbf1\bigr)\,dt
> }
> \tag{5}
> $$
>
> $$
> \boxed{
> \Delta_L=\frac12\int_0^\infty
> \sum_i\bigl(x_i(t)-\bar d\bigr)^2\,dt
> }
> \tag{6}
> $$

> [!note]- Integrating the diffusion
> **Proof.** Put $y(t)=x(t)-\bar d\mathbf1=e^{-t\mathbf L}b$. All its spectral components decay, since $b\perp\mathbf1$. Hence
>
> $$
> \mathbf L\int_0^\infty y(t)\,dt
> =-\int_0^\infty\dot y(t)\,dt=b
> $$
>
> The integral has zero coordinate sum, so it equals $\mathbf{Gr}\,b$. This gives (5).
>
> Let $b_k$ be the coordinates of $b$ in an orthonormal Laplacian eigenbasis, and let $\lambda_k>0$, $k=2,\ldots,n$, be the nonzero eigenvalues. Then
>
> $$
> \int_0^\infty\sum_i y_i(t)^2\,dt
> =\sum_{k=2}^n\frac{b_k^2}{2\lambda_k}
> =\frac12b^{\mathsf T}\mathbf{Gr}\,b
> $$
>
> Comparing with (4) proves (6). $\square$

The center coordinates measure accumulated **signed** deviations from the mean. The displacement $\Delta_L$ measures persistent heterogeneity in aggregate: both the initial degree differences and the rate at which they equalize matter. Here $b_k$ are the coordinates of the degree deviations $b$ in an orthonormal eigenbasis of the Laplacian, and $\lambda_k$, $k=2,\ldots,n$, are its positive eigenvalues. The spectral expression is


$$
\Delta_L=\frac14\sum_{k=2}^n\frac{b_k^2}{\lambda_k}
$$

Slow components receive greater weight, but only if they occur in the initial distribution $b$. In particular, a regular graph starts at equilibrium and has $\Delta_L=0$, regardless of its other structural properties.

## Exact examples and negative coordinates

The vertices of $P_4$ are ordered $1-2-3-4$; in $K_{1,3}$, vertex $1$ is the hub. These graphs and $C_4$ have unit conductances. Triangle weights are listed in the order $(c_{12},c_{13},c_{23})$.

| Graph | $\beta$ | $\sigma$ | $\alpha$ | $\rho$ |
|---|---|---|---|---|
| $P_4$ | $(1,3,3,1)/8$ | $13/8$ | $(1,0,0,1)/2$ | $3/4$ |
| $K_{1,3}$ | $(7,3,3,3)/16$ | $27/16$ | $(-1,1,1,1)/2$ | $3/4$ |
| $C_4$ | $(1,1,1,1)/4$ | $2$ | $(1,1,1,1)/4$ | $5/16$ |
| Triangle $(1,2,3)$ | $(5,8,9)/22$ | $45/11$ | $(9,8,5)/22$ | $15/121$ |
| Triangle $(7,1,1)$ | $(2,2,-1)/3$ | $8$ | $(4,4,7)/15$ | $32/225$ |

The values were obtained in rational arithmetic by independently solving the equidistance systems: each Gram matrix was first converted to a squared-distance matrix, then a system of the form (1) was solved. The results were compared with the diagonal and pseudoinverse formulas; the bordered identity (8) was checked separately. [Exact-check and figure-reproduction script](https://github.com/magin67/pmg-notes/blob/v5/checks/metric-parameters/verify_sphere_centres.py).

For any unit-conductance cycle $C_n$, $n\ge3$, both coordinate vectors equal $u$, and $\sigma=2$. This follows from regularity and vertex transitivity. The path and star illustrate substantial differences between the coordinates of the two centers.

For the check triangle $(7,1,1)$,

$$
\mathbf L=
\begin{pmatrix}
8&-7&-1\\
-7&8&-1\\
-1&-1&2
\end{pmatrix},
\qquad
\mathbf Q=
\begin{pmatrix}
0&30&12\\
30&0&12\\
12&12&0
\end{pmatrix}
$$

Directly, $\mathbf Q(2,2,-1)^{\mathsf T}/3=16\mathbf1$, so $\sigma=8$. Here $\bar d=6$ and $\Delta_L=2$. In resistance geometry, $\Delta_R=2/225$.

Barycentric coordinates of a point within a simplex are nonnegative, but circumcenter coordinates may have either sign. A negative $\beta^3$ means that $O_L$ lies on the opposite side of the hyperplane of face $12$ from vertex $3$. This is ordinary circumsphere geometry, not a failure of connectedness or metric positivity. For the star, it is the resistance center that lies outside: $\alpha^1=-1/2$.

The [[en/PythonExamples/Example - Metric Parameters of Graphs#Centers of the two spheres|Python example]] reproduces this calculation.

## Coincident centers and structural symmetry

If the conductance-preserving automorphism group acts transitively on vertices, all $d_i$ are equal and all $\mathrm{Gr}_{ii}$ are equal. Both centers therefore coincide with their respective centroids.

Having some nontrivial automorphisms is insufficient: a star permits arbitrary permutations of its leaves, yet its centers do not coincide with its centroids. Vertex transitivity of the unweighted structure alone is also insufficient with arbitrary conductances.

The converse fails even for the simultaneous equality $\Delta_L=\Delta_R=0$.

> [!example] A fully asymmetric graph with two zero displacements
> In Brouwer's catalogue [5], graph P25.01 has strongly regular parameters $(25,12,5,6)$ and automorphism-group order $1$. Nevertheless,
>
> $$
> \beta=\alpha=\frac1{25}\mathbf1,\qquad
> \sigma=12,\qquad \rho=\frac2{25},\qquad
> \Delta_L=\Delta_R=0
> $$

> [!note]- Verification through the adjacency matrix
> **Proof.** Let $\mathbf A$ be the adjacency matrix of this graph and $\mathbf E=\mathbf1\mathbf1^{\mathsf T}$. Strong regularity means degree $12$, with $5$ common neighbors for adjacent vertices and $6$ for nonadjacent vertices. Hence
>
> $$
> \mathbf A^2=6\mathbf I-\mathbf A+6\mathbf E,\qquad
> \mathbf A\mathbf1=12\mathbf1
> $$
>
> For $\mathbf L=12\mathbf I-\mathbf A$, direct multiplication gives
>
> $$
> \mathbf{Gr}=\frac{13\mathbf I+\mathbf A-\mathbf E}{150},\qquad
> \mathbf L\mathbf{Gr}=\mathbf I-\frac1{25}\mathbf E,\qquad
> \mathbf{Gr}\mathbf1=0
> $$
>
> Thus $d_i=12$ and $\mathrm{Gr}_{ii}=2/25$ are constant. The conditions for coincident centers give all the stated values. The absence of nontrivial automorphisms is a catalogue property of the graph, not a consequence of these matrix identities. $\square$

This example rules out interpreting the displacements as exact measures of structural asymmetry. $\Delta_L$ detects degree heterogeneity through the network; $\Delta_R$ detects heterogeneity of the vertices' resistance positions. Vanishing values do not determine the automorphism group.

## Conductance scale and weak cuts

### Uniform scaling

Under $c_{ij}\mapsto a c_{ij}$, $a>0$, we have

$$
\mathbf L\mapsto a\mathbf L,\qquad
\mathbf{Gr}\mapsto a^{-1}\mathbf{Gr},\qquad
d\mapsto ad,\qquad b\mapsto ab
$$

Therefore

$$
\beta\mapsto\beta,\qquad
\sigma\mapsto a\sigma,\qquad
\Delta_L\mapsto a\Delta_L
$$

In resistance geometry, $\alpha$ is also preserved, while $\rho,\Delta_R$ are divided by $a$. Thus the coordinates are independent of the overall conductance scale. To compare displacements, one can use the dimensionless ratios $\Delta_L/\sigma$ and $\Delta_R/\rho$, both in $[0,1)$. The second already enters the [[Density, Compactness, and Tree Invariance#Bounds and decomposition of radius compactness|decomposition of radius compactness]].

### Conditional sensitivity to a bottleneck

Let $A$ be a nonempty proper subset of the vertices. Denote the total cut conductance and the imbalance of the prescribed currents in this part by

$$
C_{\partial A}=\sum_{\substack{i\in A\\j\notin A}}c_{ij},\qquad
B_A=\sum_{i\in A}b_i
$$

> [!info] A lower bound from a cut
> **Proposition.** For every such $A$,
>
> $$
> \boxed{\Delta_L\ge\frac{B_A^2}{4C_{\partial A}}}
> \tag{7}
> $$

> [!note]- Total current through the cut
> **Proof.** Summing $\mathbf L\varphi=b$ over $i\in A$ cancels internal-edge contributions and gives
>
> $$
> B_A=\sum_{\substack{i\in A\\j\notin A}}
> c_{ij}(\varphi_i-\varphi_j)
> $$
>
> By the Cauchy-Schwarz inequality,
>
> $$
> B_A^2\le C_{\partial A}
> \sum_{\substack{i\in A\\j\notin A}}
> c_{ij}(\varphi_i-\varphi_j)^2
> \le4C_{\partial A}\Delta_L
> $$
>
> Dividing by the positive cut conductance proves (7). $\square$

If the cut weakens while $B_A$ stays away from zero, the displacement grows without bound. However, $b$ itself depends on conductances, and the required imbalance may be absent.

For example, for the path $1-2-3$ with conductances $1,\varepsilon$, exact calculation gives

$$
\beta^2-\beta^3=\frac{2-\varepsilon}{6\varepsilon},\qquad
\Delta_L=\frac1{36}
\left((1-2\varepsilon)^2+\frac{(2-\varepsilon)^2}{\varepsilon}\right)
$$

As $\varepsilon\to0+$, $\Delta_L\sim1/(9\varepsilon)$. Here the weak edge must carry nonzero total current between the parts.

For a contrasting example, take the cycle $1-2-3-4-1$ and set

$$
c_{12}=c_{34}=1-\varepsilon,\qquad
c_{23}=c_{41}=\varepsilon,\qquad 0<\varepsilon<1
$$

All degrees equal $1$, so for every $\varepsilon$,

$$
\beta=\frac14\mathbf1,\qquad \sigma=1,\qquad \Delta_L=0
$$

Yet the conductance of the cut $\{1,2\}\mid\{3,4\}$ is $2\varepsilon$ and tends to zero. The vector $(1,1,-1,-1)^{\mathsf T}$ has eigenvalue $2\varepsilon$, but $b=0$ does not excite this slow component. Throughout this family, internal conductances change together with cross-cut conductances, preserving the degrees.

A weak bridge can remain invisible even when the internal conductances of the parts stay fixed.

> [!example] Weakening a bridge between fixed parts
> In the path $1-2-3-4$, assign conductances $1,\varepsilon,1$, where $\varepsilon>0$. For $A=\{1,2\}$, we have $B_A=0$. Independently solving the equidistance system gives
>
> $$
> \beta=\left(\frac14-\frac\varepsilon8,\,
> \frac14+\frac\varepsilon8,\,
> \frac14+\frac\varepsilon8,\,
> \frac14-\frac\varepsilon8\right)^{\mathsf T}
> $$
>
> $$
> \Delta_L=\frac{\varepsilon^2}{8},\qquad
> \sigma=1+\frac\varepsilon2+\frac{\varepsilon^2}{8}
> $$
>
> As $\varepsilon\to0+$, the graph approaches disconnection, but $\beta\to u$ and $\Delta_L\to0$. Unlike the regular-cycle example, the internal edges of the parts do not change.

Thus sensitivity to a weak cut is proved subject to a current imbalance. Universal bottleneck detection from $(\beta,\sigma)$ does not follow from the definition.

![Two weak connections give different displacement behavior](<images/Weak Edges and Degree Imbalance.svg>)

*Two weak connections give different displacement behavior. In the three-vertex path, current imbalance across the weak edge remains nonzero and $\Delta_L$ grows. In the symmetric four-vertex path, each half has zero net imbalance: the weak bridge carries no current for this distribution, and $\Delta_L$ decreases.*

## Further detail: duality and bordering

The following derivations supplement the geometric and electrical explanations: they relate vertices to normals, explain matrix bordering, and prove a special equality of displacements on trees.

### Mutually inverse simplices and normals

The construction of mutually inverse simplices and the relation between their vertices and face normals belong to Fiedler's theory; an exposition is given by Devriendt and Van Mieghem [1, §3.1, formulas (5)-(8)]. In our notation it takes the following form.

Let the columns of $\mathbf X$ be the centered position vectors of the resistance simplex, so that $\mathbf X^{\mathsf T}\mathbf X=\mathbf{Gr}$. Put $\mathbf Y=\mathbf X\mathbf L$. Then

$$
\mathbf Y^{\mathsf T}\mathbf Y=\mathbf L,\qquad
\mathbf X^{\mathsf T}\mathbf Y=\mathbf J
$$

Thus the columns $x_i,y_j$ satisfy $x_i\cdot y_j=\delta_{ij}-1/n$. For a fixed $j$, the inner product with $y_j$ is constant on the face opposite $x_j$. Hence $y_j$ points along its inward normal; similarly, $x_j$ supplies the normal to the opposite face of the second simplex.

This is a geometric duality. It does not mean that $\mathbf{Gr}$ must be the Laplacian of a network with positive conductances: its off-diagonal entries may have either sign.

### Meaning of the bordered Green matrix

> [!info] Bordered Green matrix
> **Proposition.** The following identity holds:
>
> $$
> \boxed{
> \begin{pmatrix}
> \sigma&\beta^{\mathsf T}\\
> \beta&\mathbf{Gr}
> \end{pmatrix}^{-1}
> =
> \begin{pmatrix}
> 0&\mathbf1^{\mathsf T}\\
> \mathbf1&-\mathbf Q/2
> \end{pmatrix}
> }
> \tag{8}
> $$

This is Fiedler's identity for the simplex with Gram matrix $\mathbf L$, after rescaling the bordering row and column; compare [2, §2.4, formula (14)]. It imposes no sign condition on the off-diagonal entries of $\mathbf{Gr}$.

> [!note]- Verification by block multiplication
> **Proof.** The equalities $\mathbf{Gr}\mathbf1=0$, $\mathbf1^{\mathsf T}\beta=1$, and $\mathbf Q\beta=2\sigma\mathbf1$ verify three blocks of the product. For the fourth, use
>
> $$
> \mathbf Q\mathbf{Gr}=\mathbf1d^{\mathsf T}\mathbf{Gr}-2\mathbf J,\qquad
> \beta^{\mathsf T}=\frac1n\mathbf1^{\mathsf T}
> +\frac12d^{\mathsf T}\mathbf{Gr}
> $$
>
> Then $\mathbf1\beta^{\mathsf T}-\mathbf Q\mathbf{Gr}/2=\mathbf I$. $\square$

Bordering adds the affine center and radius data to the singular matrix $\mathbf{Gr}$. The inverse contains squared pairwise distances and the unit affine-weight condition. It differs from the positive semidefinite Gram matrix of centered Euclidean position vectors: the bordered matrix is nonsingular and indefinite.

For the resistance simplex, similarly,

$$
\begin{pmatrix}
\rho&\alpha^{\mathsf T}\\
\alpha&\mathbf L
\end{pmatrix}^{-1}
=
\begin{pmatrix}
0&\mathbf1^{\mathsf T}\\
\mathbf1&-\mathbf R/2
\end{pmatrix}
$$

Here $\alpha$ is the resistance circumcenter's coordinate vector, and $\rho$ is the resistance radius in PMG's quadratic normalization.

### Equal displacements on unit-conductance trees

> [!info] The two displacements of a tree
> **Proposition.** If the graph is a tree with unit conductances, then
>
> $$
> \boxed{\Delta_L=\Delta_R}
> $$
>
> This is an equality of quadratic quantities at the chosen unit scale, not an identification of the two simplices.

> [!note]- Proof through distance sums
> **Proof.** Let $T_i=\sum_j\operatorname{dist}(i,j)$, and let $Kf=\sum_{i<j}R_{ij}$ be the Kirchhoff index. On a unit-conductance tree, $R_{ij}=\operatorname{dist}(i,j)$, so
>
> $$
> r=\frac1nT-\frac{Kf}{n^2}\mathbf1
> $$
>
> Counting branch sizes gives $\mathbf LT=-nb$, as proved in the [[Degree Potential and Centralities#Agreement with closeness on trees|tree theorem]]. Hence $\mathbf Lr=-b$, and
>
> $$
> b^{\mathsf T}\mathbf{Gr}\,b
> =r^{\mathsf T}\mathbf L\mathbf{Gr}\mathbf Lr
> =r^{\mathsf T}\mathbf Lr
> $$
>
> Dividing by $4$ proves equality of the displacements. $\square$

If every edge of the tree has the same conductance $c>0$, scaling gives $\Delta_L=c^2\Delta_R$. Equality is not asserted for arbitrary conductance distributions. The resistance displacement enters the [[Density, Compactness, and Tree Invariance#Bounds and decomposition of radius compactness|compactness factor]] as $\chi=1-\Delta_R/\rho$; the Laplacian displacement has a different physical dimension.

## Status of the results and continuation

| Result | Source or derivation | Role in the note |
|---|---|---|
| Mutually inverse simplices, vertices, and normals | Fiedler's theory as presented in [1, §3.1] | Geometric foundation |
| Center, radius, and bordering | General formulas in [2, §2.4], specialized to Gram matrix $\mathbf L$ with a direct proof | Definition and computation of $(\beta,\sigma)$ |
| Spanning-tree interpretation of the resistance center | [3] and the published centralities note | Distinguishing the two centers |
| Diffusion formulas and the cut bound | Derived here from $\mathbf L\varphi=b$ and spectral decomposition | Interpretation of heterogeneity and its limits |
| Zero displacements in an asymmetric graph | Graph from [5], exact matrix verification here | Counterexample to a structural-symmetry criterion |
| Equal displacements on unit-conductance trees | Derived from the Green diagonal and distance-sum formulas | Relation between the two geometries at a specified normalization |
| Small-graph table | Independent solution of equidistance systems | Verification of normalizations and signs |

A derivation in this note is not a claim of scientific novelty. The Laplacian circumcenter belongs to a known geometric construction; the electrical and diffusion interpretations clarify its meaning for the chosen degree distribution.

Using $\beta$ to rank vertices is discussed in [[Degree Potential and Centralities]]. That note gives a positive normalization, the link to generalized degree, and a comparison with eigenvector centrality; the geometric definition of the center is independent of the chosen ranking normalization.

## Sources

1. K. Devriendt, P. Van Mieghem. *The Simplex Geometry of Graphs*. [arXiv:1807.06475](https://arxiv.org/abs/1807.06475), version 2, §3.1: mutually inverse simplices and face normals.
2. K. Devriendt. *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*. [arXiv:2010.04521](https://arxiv.org/abs/2010.04521), version 2, §2.4, Theorem 2 and formula (14): Fiedler's identity and its extension to arbitrary simplices.
3. K. Devriendt, R. Lambiotte. *Discrete curvature on graphs from the effective resistance*. [arXiv:2201.06385](https://arxiv.org/abs/2201.06385), version 3, definition (2), Appendices B.3-B.4: resistance curvature, the circumcenter, and the variational characterization.
4. J. Zhou, Z. Wang, C. Bu. *On the resistance matrix of a graph*. Electronic Journal of Combinatorics 23(1), P1.41, 2016. [Full text](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p41/pdf/): resistance regularity.
5. A. E. Brouwer. [Paulus-Rozenfeld graphs](https://aeb.win.tue.nl/graphs/Paulus.html), entry P25.01; [adjacency matrix as neighbor lists](https://aeb.win.tue.nl/graphs/paulus/p25_01). Parameters $(25,12,5,6)$ and automorphism-group order $1$.
