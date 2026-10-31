---
title: "Resistance Radius: Forest Formula and Matroid Invariance"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: resistance-radius-forest-formula-and-matroid-invariance
lang: en
description: "The circumradius through the 2-forest coefficient and edge resistances. A weighted proof of the forest formula, reciprocal roles of the Laplacian and Greenian, matroid invariance, gluing, and exact geometric examples."
order: 6
---

The circumsphere radius is defined by the full resistance geometry of a graph. Nevertheless, two scalar matroid characteristics suffice to compute it: the first forest scale and the second edge parameter. This explains how the radius can remain unchanged while vertex geometry changes.

[[Forest Resistance Scales]] introduces $\xi_1=f_{n-2}/\tau$, and [[Edge Resistances and Random Spanning Trees]] introduces $H_2=\sum_\ell c_\ell R_\ell^2$. Here we prove

$$
\boxed{
\rho=\frac13\xi_1-\frac1{12}H_2
=\frac13\frac{f_{n-2}}{\tau}
-\frac1{12}\sum_{\ell\in E}c_\ell R_\ell^2
}
\tag{1}
$$

The forest identity underlying (1) is due to Richman, Shokrieh, and Wu [1, Theorem C / 5.7]; weighted expressions also appear in [2, Section 3.1]. A complete derivation is given below using edge conductances and the current PMG normalization $\rho=R_{\mathrm{sph}}^2$.

## Graph, sphere, and normalization

Let $G=(\mathcal V,E)$ be a finite connected undirected loopless graph on $n\ge2$ vertices. Parallel edges are allowed and retain separate labels. Their conductances satisfy $c_\ell>0$. Each undirected edge occurs once in every edge sum.

Write $f_g$ for the weighted sum of ordinary spanning forests with $g$ edges, including all isolated vertices. No roots are chosen. With $d=n-1$, we have $\tau=f_d>0$, and $f_{n-2}=f_{d-1}$ counts weighted two-component forests. Thus $\xi_1$ is indexed by corank $1$, not component count $2$.

The Green and resistance matrices satisfy

$$
\mathbf{Gr}=\mathbf L^+,\qquad
R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
\tag{2}
$$

For an existing edge $\ell=\{i,j\}$, set $R_\ell=R_{ij}$. The quantity $\eta_\ell=c_\ell R_\ell$ is its inclusion probability in a weighted random spanning tree.

Let $A_i$ be vertices of a Euclidean realization corresponding to the PMG vertices $a_i$. Then

$$
(A_i-A_j)^2=R_{ij},\qquad
\|A_i-A_j\|=\sqrt{R_{ij}}
$$

A superscript $2$ denotes a quadratic norm, while $\|\cdot\|$ denotes the linear norm. The simplex has dimension $n-1$. Write $O$ for its circumcenter and $h=n^{-1}\sum_i A_i$ for its centroid. They generally differ.

$$
\rho=(A_i-O)^2=R_{\mathrm{sph}}^2,\qquad
D_{\mathrm{res}}=4\rho
$$

This is the normalization of [[Resistance Radius and Diameter of a Graph]]. The parameter $\rho$ has resistance dimension; it is neither a linear radius nor the maximum pairwise resistance. “Mass” is not used as its current name.

![[Weighted Triangle - Resistance Circumcircle.svg]]

**From graph to geometry.** For a triangle with conductances $c_{ab}=1$, $c_{ac}=2$, $c_{bc}=3$, the resistances are $R_{ab}=5/11$, $R_{ac}=4/11$, $R_{bc}=3/11$. The left panel is the network diagram; the right is its exact Euclidean realization, with side lengths equal to the square roots of these values. All vertices lie on a circle with $\rho=15/121$. The circumcenter $O$ and centroid $h$ are marked separately.

## The radius as Laplacian energy

Fix a reference vertex $q$ and introduce the column

$$
\mathbf r=(r_i)_{i\in\mathcal V},\qquad r_i=R_{iq},\qquad r_q=0
$$

Deleting row and column $q$ from the Laplacian gives the positive definite matrix $\mathbf A=\mathbf L_{\widehat q,\widehat q}$ with determinant $\tau$. Let $\widehat{\mathbf r}$ be $\mathbf r$ with entry $q$ removed.

For the vectors $u_i=A_i-A_q$, $i\ne q$, the reference Gram matrix is

$$
\mathbf G_q=(g_{ij})_{i,j\ne q}=\mathbf A^{-1},\qquad
g_{ij}=\frac{r_i+r_j-R_{ij}}2
$$

The first equality follows by solving the grounded Laplacian system: column $g_{\cdot j}$ gives the potentials for current $\mathbf e_j-\mathbf e_q$ and zero potential at $q$. The second is polarization of the norm of $u_i-u_j$. The connection between the grounded system and $\mathbf{Gr}$ is proved in the [[Edge Resistances and Random Spanning Trees#Differentiating a Laplacian cofactor|Laplacian-cofactor derivation]].

> [!info] The radius as Laplacian energy
> **Lemma.** For any choice of $q$,
>
> $$
> \boxed{
> \rho=\frac14\widehat{\mathbf r}^{\mathsf T}\mathbf A\widehat{\mathbf r}
> =\frac14\mathbf r^{\mathsf T}\mathbf L\mathbf r
> =\frac14\sum_{\ell=\{i,j\}}c_\ell(r_i-r_j)^2
> }
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** Put $y=O-A_q$. Equal distances from the center to $A_i$ and $A_q$ mean
>
> $$
> (u_i-y)^2=y^2,\qquad 2u_i\cdot y=u_i^2=r_i
> $$
>
> Write $y=\sum_{i\ne q}\beta_i u_i$. Then $2\mathbf G_q\boldsymbol\beta=\widehat{\mathbf r}$ and
>
> $$
> \rho=y^2=\boldsymbol\beta^{\mathsf T}\mathbf G_q\boldsymbol\beta
> =\frac14\widehat{\mathbf r}^{\mathsf T}\mathbf G_q^{-1}\widehat{\mathbf r}
> $$
>
> Substituting $\mathbf G_q^{-1}=\mathbf A$ gives the first equality in (3). The second uses $r_q=0$, and the third is the usual expansion of the Laplacian quadratic form. $\square$

The column $\mathbf r$ depends on $q$, but its energy always equals $4\rho$. For $n\ge2$ it is nonconstant, hence $\rho>0$.

## Reciprocal roles of the Laplacian and Greenian

[[The Greenian Metric and Potentials]] establishes two evaluations for affine vectors $u,v$ with coordinate columns $\mathbf u,\mathbf v$:

$$
M=\exp L,\qquad N=\exp(\mathrm{Gr})
$$

$$
P_M([u,v])=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v,\qquad
P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v
$$

The first gives the original resistance metric; the second gives the energy metric of the Greenian exponential. The Greenian's own coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$ replace neither evaluation.

In the direct PMG space, put $p_i=a_i-h$, where now $h=n^{-1}\sum_i a_i$ is the corresponding centroid element. For the chosen reference $q$, define

$$
v_q=\sum_i R_{iq}p_i
$$

Its full coordinate column is $\mathbf r-\bar r\mathbf1$, where $\bar r=n^{-1}\sum_i r_i$. Since $\mathbf L\mathbf1=0$, (3) gives

$$
\boxed{P_N([v_q]^2)=\mathbf r^{\mathsf T}\mathbf L\mathbf r=4\rho}
\tag{4}
$$

Thus $R_{iq}$ comes from the metric of the Laplacian exponential, while its centered combination is evaluated by a potential of the Greenian exponential. The vector $v_q$ is not identified with the geometric vector $O-A_q$: equality (4) uses a different metric evaluation.

Equality (4) alone does not establish matroid invariance: $v_q$ uses vertex data and changes with the graph. The next step expresses the same energy through ordinary forests and original-edge characteristics.

## Auxiliary forest sums with prescribed roots

For fixed vertices, introduce two auxiliary sums:

- $Z_{i\mid q}$: the weight sum of 2-forests in which $i,q$ lie in different components;
- $Z_{i\mid j\mid q}$: the weight sum of 3-forests in which $i,j,q$ lie in three different components.

These forests have a prescribed root set: each component contains exactly one of the listed roots. Other root choices are not summed. If two listed roots coincide, the corresponding sum is defined to be zero.

For a nonempty root set $S$, the determinant of $\mathbf L_{\mathcal V\setminus S,\mathcal V\setminus S}$ is the weight sum of forests with exactly one root from $S$ in each component. This is a special case of the matrix-forest formula in [[Forest Coefficients and the Laplacian Polynomial]].

A short derivation clarifies the weights. After deleting root coordinates, expand the determinant of $\sum c_\ell\mathbf b_\ell\mathbf b_\ell^{\mathsf T}$ by Cauchy-Binet. A cycle gives dependent columns; a component without a root gives dependent rows. The remaining edge sets are forests with one root in each component. The coordinate-matrix determinant is $\pm1$, as seen by successively deleting leaves. The contribution is therefore exactly $\prod_{\ell\in F}c_\ell$. For the empty matrix, set $\det=1$.

> [!info] Auxiliary forest sums with prescribed roots
> **Lemma.** For fixed $q$,
>
> $$
> \boxed{
> \frac{Z_{i\mid q}}{\tau}=r_i,\qquad
> \frac{Z_{i\mid j\mid q}}{\tau}=r_i r_j-g_{ij}^2
> }
> \tag{5}
> $$
>
> To include $i=q$ or $j=q$, extend the scalar notation by $g_{iq}=g_{qi}=0$.

> [!note]- Proof
> **Proof.** Apply the identity for complementary principal minors of an inverse matrix to $\mathbf A^{-1}=\mathbf G_q$. For $i\ne q$ and for distinct $i,j\ne q$, respectively,
>
> $$
> \frac{\det\mathbf A_{\widehat i,\widehat i}}{\det\mathbf A}=g_{ii}=r_i
> $$
>
> $$
> \frac{\det\mathbf A_{\widehat{\{i,j\}},\widehat{\{i,j\}}}}{\det\mathbf A}
> =\det\begin{pmatrix}g_{ii}&g_{ij}\\g_{ij}&g_{jj}\end{pmatrix}
> =r_i r_j-g_{ij}^2
> $$
>
> Submatrix indices retain the vertex labels. Numerators are the stated forest sums, and denominators are $\tau$. When roots coincide, both sides of the corresponding equality vanish by convention. $\square$

## Why each ordinary 2-forest is counted once

> [!info] Why each ordinary 2-forest is counted once
> **Lemma.** For any reference vertex $q$,
>
> $$
> \boxed{
> f_{n-2}=\sum_i Z_{i\mid q}
> -\sum_{\ell=\{i,j\}}c_\ell Z_{i\mid j\mid q}
> }
> \tag{6}
> $$

> [!note]- Proof
> **Proof.** Fix an ordinary 2-forest $F$ with components $A,B$, where $q\in A$. In the first sum it occurs once for each $i\in B$, contributing $|B|w(F)$ in total.
>
> The second sum counts pairs consisting of a 3-forest with roots $i,j,q$ and an edge $\ell=\{i,j\}$. Adding $\ell$ joins the two components without $q$ and gives a 2-forest $F$. The pair weight is $c_\ell w(F\setminus\{\ell\})=w(F)$.
>
> Conversely, for a fixed $F$, such a representation is obtained by deleting any edge of the tree $F[B]$. There are $|B|-1$ choices. Edges of component $A$ do not give the required representation: after deletion, $q$ remains in the same component as one endpoint. The difference of contributions is therefore
>
> $$
> \bigl(|B|-(|B|-1)\bigr)w(F)=w(F)
> $$
>
> Summing over all 2-forests proves (6). Distinct labels on parallel edges preserve this bijection and the weight equality. $\square$

![[Two-Forest - Counting Vertices and Deleted Edges.svg]]

**Three choices minus two choices.** The upper drawing shows a fixed 2-forest: $q$ lies in component $A$, and $B$ is the path $b-c-d$. The first sum in (6) chooses one of the three vertices of $B$. The second deletes one of its two edges; the endpoints and $q$ become three prescribed roots. Restoring the deleted edge gives the original forest with weight $w(F)$ in either case. The remainder is $(3-2)w(F)=w(F)$.

## Derivation of the main formula

Divide (6) by $\tau$ and substitute (5):

$$
\xi_1=\sum_i r_i+\sum_{\ell=\{i,j\}}c_\ell(g_{ij}^2-r_i r_j)
\tag{7}
$$

Introduce the energy notation

$$
\mathcal E_q=\mathbf r^{\mathsf T}\mathbf L\mathbf r
=\sum_{\ell=\{i,j\}}c_\ell(r_i-r_j)^2=4\rho
$$

**First transformation.** From $g_{ij}=(r_i+r_j-R_{ij})/2$,

$$
g_{ij}^2-r_i r_j
=\frac14(r_i-r_j)^2
-\frac12R_{ij}(r_i+r_j)
+\frac14R_{ij}^2
$$

Consequently,

$$
\xi_1=\sum_i r_i+\frac14\mathcal E_q+\frac14H_2
-\frac12\sum_{\ell=\{i,j\}}c_\ell R_{ij}(r_i+r_j)
$$

**Second transformation.** Let $d_i=\sum_{\ell\ni i}c_\ell$ be the total conductance at vertex $i$. The diagonal equality $(\mathbf A\mathbf G_q)_{ii}=1$ for $i\ne q$ gives

$$
\sum_{\ell=\{i,j\}\ni i}c_\ell g_{ij}=d_i r_i-1
$$

Therefore

$$
\sum_{\ell=\{i,j\}\ni i}c_\ell R_{ij}
=d_i r_i+\sum_{\ell=\{i,j\}\ni i}c_\ell r_j
-2(d_i r_i-1)
=2-(\mathbf L\mathbf r)_i
$$

Multiply by $r_i$ and sum over $i$. The component $r_q$ is zero, and each edge contributes twice, with factors $r_i,r_j$. This gives

$$
\sum_{\ell=\{i,j\}}c_\ell R_{ij}(r_i+r_j)
=2\sum_i r_i-\mathcal E_q
$$

After substitution into (7), the sums $\sum_i r_i$ cancel:

$$
\xi_1=\frac34\mathcal E_q+\frac14H_2
=3\rho+\frac14H_2
$$

This proves (1). Every step uses positive conductances directly, without extending the unit-weight case by analogy. When $n=2$, the 3-forest sums vanish and the remaining identities still hold.

## Matroid invariance and its limits

> [!info] Matroid invariance and its limits
> **Theorem.** The resistance radius $\rho$ is an invariant of the weighted cycle matroid.

> [!note]- Proof
> **Proof.** A matroid isomorphism preserving corresponding conductances preserves the basis-weight sum $\tau$ and the weight sum of independent sets of corank $1$, namely $f_{n-2}$. It also preserves the inclusion probabilities $\eta_\ell$ of matched edges in a weighted random basis. Hence it preserves
>
> $$
> \xi_1=\frac{f_{n-2}}{\tau},\qquad
> H_2=\sum_\ell\frac{\eta_\ell^2}{c_\ell}
> $$
>
> Formula (1) therefore preserves $\rho$. $\square$

Matroid invariance concerns the scalar $\rho$. An edge isomorphism does not match all vertex pairs; it does not imply preservation of the entire matrix $\mathbf R$, the coordinates of $O$, its distance from the centroid, or the shape of the resistance simplex. The path and star in the [[The Cycle Matroid and Exterior Products of Edges#One matroid, different vertex geometry|two-tree comparison]] have the same radius but different vertex characteristics.

The converse also fails: equal radii, like equality of several other scalars, do not by themselves prove matroid isomorphism.

## Scaling and one-point gluing

Multiplying every conductance by $\sigma>0$ divides both $\xi_1,H_2$ by $\sigma$. Thus

$$
\rho(\sigma G)=\sigma^{-1}\rho(G),\qquad
R_{\mathrm{sph}}(\sigma G)=\sigma^{-1/2}R_{\mathrm{sph}}(G)
$$

Every term of (1) has dimension $C^{-1}$, where $C$ is conductance dimension.

**Gluing corollary.** If connected graphs $G_1,G_2$ have disjoint edge sets and are glued at exactly one vertex, retaining conductances, then

$$
\boxed{\rho(G_1\vee G_2)=\rho(G_1)+\rho(G_2)}
\tag{8}
$$

> [!note]- Proof
> **Proof.** The product of normalized forest polynomials gives $\xi_1(G_1\vee G_2)=\xi_1(G_1)+\xi_1(G_2)$. Preservation of edge probabilities in the pieces gives the same law for $H_2$. Substitute both sums into (1). $\square$

This is a separate derivation using the laws of this particular gluing. It agrees with the geometric proof in the [[Vertex Contraction and Graph Gluing#Resistance radius is additive|section on radius additivity]]. Formula (8) does not automatically extend to gluing at several vertices or along a shared edge subgraph.

Merging parallel conductors also preserves $\rho$, since it leaves $\mathbf L$ and the metric unchanged. This agrees with (1). An ordinary forest can use at most one edge from a parallel class, so the sum of its possible edge weights is the total conductance; every $f_g$ is preserved. Preservation of $H_2$ under the same operation is proved in the [[Edge Resistances and Random Spanning Trees#Parallel conductors and the edge representation|discussion of parallel conductors]]. The matroid ground set nevertheless changes.

## Examples and independent computation

### Weighted tree

For a tree, the two quantities agree:

$$
\xi_1(T)=H_2(T)=\sum_{\ell\in E(T)}\frac1{c_\ell}
$$

Therefore

$$
\boxed{\rho(T)=\frac14\sum_{\ell\in E(T)}\frac1{c_\ell}}
$$

For one edge of conductance $c$, the resistance simplex is a segment of length $1/\sqrt c$, whose squared radius is $1/(4c)$. This directly checks the factor $1/4$. Every unit tree on $n$ vertices has $\rho=(n-1)/4$.

### Cycle and complete graph

For a unit cycle $C_n$, $n\ge3$, one has $\xi_1=(n-1)/2$ and $H_2=(n-1)^2/n$. Hence

$$
\rho(C_n)=\frac{n^2-1}{12n}
$$

For a unit complete graph $K_n$, $n\ge2$, the forest and edge values are

$$
\xi_1=\frac{(n-1)(n+6)}{2n^2},\qquad
H_2=\frac{2(n-1)}n,\qquad
\rho(K_n)=\frac{n-1}{n^2}
$$

The last formula can first be obtained from regular-simplex geometry: all $R_{ij}=2/n$, the center equals the centroid, and $n\rho=n^{-1}\sum_{i<j}R_{ij}$. Formula (1) then recovers the displayed expression for $\xi_1$. With common conductance $c$, the radii in both families are divided by $c$.

### Triangle with conductances 1, 2, 3

Continue the [[Edge Resistances and Random Spanning Trees#Examples|weighted-triangle example]]. We have

$$
\tau=11,\qquad f_1=1+2+3=6,\qquad
\xi_1=\frac6{11},\qquad H_2=\frac{84}{121}
$$

Substitution into (1) gives

$$
\rho=\frac2{11}-\frac7{121}=\frac{15}{121}
$$

For an independent geometric check, take the realization

$$
A=(0,0),\qquad
B=\left(\sqrt{\frac5{11}},0\right),\qquad
C=\left(\frac3{\sqrt{55}},\frac1{\sqrt5}\right)
$$

The squared side lengths are $5/11,4/11,3/11$. Equal-distance conditions give

$$
O=\left(\frac{\sqrt{55}}{22},\frac{\sqrt5}{22}\right),\qquad
h=\left(\frac8{3\sqrt{55}},\frac1{3\sqrt5}\right)
$$

Thus $(O-A)^2=(55+5)/22^2=15/121$, with $O\ne h$. This realization is used in the circumcircle figure.

### Comparing the two contributions

| Graph | $\xi_1$ | $H_2$ | $\rho$ |
| --- | --- | --- | --- |
| Unit $P_4$ and $K_{1,3}$ | $3$ | $3$ | $3/4$ |
| Unit $C_4$ | $3/2$ | $9/4$ | $5/16$ |
| Unit $K_4$ | $15/16$ | $3/2$ | $3/16$ |
| Triangle with conductances $1,2,3$ | $6/11$ | $84/121$ | $15/121$ |

![[Forest Contribution and Edge Correction to the Radius.svg]]

**Two contributions and the result.** The full bar has length $\xi_1/3$. The red hatched part has length $H_2/12$ and is subtracted; the remaining green part equals $\rho$. Every row uses the same scale. This depicts the exact difference, not a decomposition of the sphere into geometric pieces.

## Original sources and conversion of weights

In [1], the forest identity uses tree and 2-forest counts and a scalar $\gamma(G)$. Its energy definition and (3) give $\gamma(G)=\rho$ in our quadratic normalization. Here $\gamma(G)$ is distinct from the canonical Greenian coefficients $\gamma_{ij}$.

In [2, Section 3.1], edge weights are conductor resistances, and forest weight is a product over edges outside the forest. Conversion to conductances uses

$$
\prod_{\ell\notin F}\frac1{c_\ell}
=\left(\prod_{\ell\in E}\frac1{c_\ell}\right)
\prod_{\ell\in F}c_\ell
$$

The common factor cancels in the ratio of the 2-forest and spanning-tree sums. In the edge term of formula (11) of [2], the ratio of spanning-tree polynomials after edge contraction becomes $\eta_\ell$, so that term is $\eta_\ell^2/c_\ell=c_\ell R_\ell^2$. These are exactly our $\xi_1,H_2$.

Under this conversion, resistances of loops created by contracting a parallel edge remain in the product over edges outside the tree. Loops do not appear in our product of conductances over tree edges. They cannot be discarded from the complementary-edge product without accounting for this factor.

Passing to diameter normalization multiplies the entire formula by $4$:

$$
D_{\mathrm{res}}=\frac43\xi_1-\frac13H_2
$$

This expression must not be confused with the formula for $\rho$. The proof above fixes the normalization geometrically before using the forest identity.

## Status of the results and verification

The Richman-Shokrieh-Wu forest identity, the matrix-forest formula, and the complementary-minor identity are external results. Here the derivation is reproduced for positive conductances, connected with the adopted potentials of $M,N$, and used to establish matroid invariance and the stated radius transformation laws. The original forest identity is not attributed to PMG.

Exact rational checks on 54 connected graphs with 215 choices of reference vertex compare direct enumeration of forests with prescribed roots, principal minors, both transformations in the proof, energy (3), extraction of the Greenian-exponential potential, and the independent computation

$$
\rho=\frac1{2\,\mathbf1^{\mathsf T}\mathbf R^{-1}\mathbf1}
$$

The last formula is proved in the [[Resistance Radius and Diameter of a Graph#Computation from the resistance matrix|matrix computation of the radius]]. Separate checks cover every reference vertex, scaling, one-point gluing, and parallel-conductor merging. The [exact-arithmetic script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_resistance_radius.py) uses only the Python standard library and adjacent helper modules. Run from the repository root:

    python checks/matroid/verify_resistance_radius.py

The three SVG figures originate from the [drawing script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/draw_radius_figures.py); their English labels are reproduced by the [translation script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/translate_figures_en.py). Finite checks and figures supplement the proofs.

Results concern connected undirected graphs with positive conductances. No extension to the balanced model is made here. One-point gluing laws, the Whitney twist, and dependence on the chosen boundary are studied in [[Gluing and the Limits of Matroid Invariance]]. General boundary gluings and applications to chains of cores form a separate continuation.

## References and connections

1. Richman H., Shokrieh F., Wu C. *Counting two-forests and random cut size via potential theory*. [arXiv:2308.03859](https://arxiv.org/abs/2308.03859), 2023. Theorem C / 5.7, Propositions 3.4 and 5.6: the identity for 2-forest sums and resistances.
2. Richman H., Shokrieh F., Wu C. *On determinants of resistance matrices*. [arXiv:2606.21902](https://arxiv.org/abs/2606.21902), 2026; [DOI: 10.1016/j.laa.2026.10.003](https://doi.org/10.1016/j.laa.2026.10.003). Section 3.1, formulas (11)-(12): the weighted expression using conductor resistances.
3. [[Resistance Radius and Diameter of a Graph]] and [[Vertex Contraction and Graph Gluing]]: the sphere definition, normalization, and geometric gluing law.
4. [[The Greenian Metric and Potentials]]: reciprocal metric roles of the Laplacian and Greenian.
5. [[Forest Resistance Scales]] and [[Edge Resistances and Random Spanning Trees]]: the two matroid families entering the radius formula.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Резистивный радиус - лесная формула и матроидная инвариантность|Русская версия]].
