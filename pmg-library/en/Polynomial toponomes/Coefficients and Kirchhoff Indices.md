---
title: Coefficients and Kirchhoff Indices
date: 2026-10-23
updated: 2026-10-23
revision: 1
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: coefficients-and-kirchhoff-indices
lang: en
description: "The two highest vertex coefficients determine the Kirchhoff index; other coefficient ratios describe the reciprocal spectrum and the centroid contribution to the resistance radius."
order: 3
---

[[Forest Coefficients and the Laplacian Polynomial]] established that reducing the Laplacian exponential through partition types in vertex normalization gives the same polynomial as the determinant of $I+t\mathbf L$. We now use this correspondence to extract metric graph parameters from the coefficients.

**Main result: the sum of all pairwise resistances is determined by the two highest coefficients of the vertex toponome. Divide the next-to-leading coefficient by the leading coefficient and multiply by the vertex count.** The proof uses spanning 2-forests and requires no computation of Laplacian eigenvalues.

A path and a star will show how vertex normalization distinguishes graphs with identical vector polynomials. We then consider the other coefficient ratios and briefly relate the result to the centroid and circumsphere.

## Initial data

Let $G=(V,E)$ be a finite connected simple undirected graph on $n\geqslant2$ vertices. Existing edges have positive conductances $c_e$. We use the [[Vector and Vertex Normalizations of Toponomes#One-variable toponomes|one-variable toponomes]]

$$
F_G(t)=\sum_{k=0}^{n-1}f_kt^k,
\qquad
P_G(t)=\sum_{k=0}^{n-1}p_kt^k=\det(I+t\mathbf L)
$$

The Laplacian matrix is $\mathbf L$, and the Green matrix is $\mathbf{Gr}=\mathbf L^+$. Electrically, $R_{ij}$ is the effective resistance between vertices $i,j$. In resistance geometry, it is the norm of the affine vector $a_{ij}=a_j-a_i$. The PMG norm is quadratic: $a_{ij}^2=a_{ij}\cdot a_{ij}=R_{ij}$.

Let $\tau(G)>0$ be the spanning-tree coefficient, the sum of conductance products over spanning trees. By the [[Forest Coefficients and the Laplacian Polynomial#The highest coefficients of a connected graph|forest characterization of the highest coefficients]],

$$
f_{n-1}=\tau(G),
\qquad
p_{n-1}=n\tau(G)
$$

Write $\tau_{ij}^{(2)}$ for the total weight of spanning 2-forests separating distinct vertices $i,j$. Each such forest covers all of $V$ and has exactly two components: one contains $i$, and the other contains $j$.

Connectivity is essential. For a disconnected graph, $p_{n-1}=0$, and vertices in different components have no finite effective resistance. The ratios below do not apply to that case; each connected component can be considered separately.

## Resistance as a ratio of forest sums

> [!info] Resistance through separating 2-forests
> **Theorem.** The resistance between two vertices is the total weight of spanning 2-forests separating them, divided by the graph's spanning-tree coefficient:
>
> $$
> \boxed{R_{ij}=\frac{\tau_{ij}^{(2)}}{\tau(G)}}
> \tag{1}
> $$

For unit conductances, the numerator counts separating 2-forests and the denominator counts spanning trees. For arbitrary conductances, their weights are summed. The formula does not require an edge between $i$ and $j$.

> [!proof]- Proof by grounding and a principal minor
> **Proof.** Inject unit current at $i$, extract it at $j$, and set the potential of $j$ to zero. For $S=V\setminus\{j\}$, the remaining potentials satisfy
>
> $$
> \mathbf A\varphi_S=\mathbf e_i,
> \qquad \mathbf A=\mathbf L[S,S]
> $$
>
> The coordinates of $\mathbf A$ and the column $\mathbf e_i$ are indexed by vertices in $S$. The matrix $\mathbf A$ is invertible, and the potential difference $\varphi_i-\varphi_j=\varphi_i$ equals $R_{ij}$. Therefore
>
> $$
> R_{ij}=(\mathbf A^{-1})_{ii}
> =\frac{\det\mathbf L[V\setminus\{i,j\},V\setminus\{i,j\}]}{\det\mathbf L[V\setminus\{j\},V\setminus\{j\}]}
> $$
>
> By the [[Forest Coefficients and the Laplacian Polynomial#Prescribed roots and a principal minor|principal-minor theorem]], the denominator is $\tau(G)$: the root $j$ is prescribed, and the forest has one component. The numerator is $\tau_{ij}^{(2)}$: roots $i,j$ are prescribed, and each must lie in its own component. There are no additional root choices. This proves (1). For $n=2$, the numerator is an empty determinant, equal to $1$. $\square$

A principal minor thus acquires a metric meaning: after division by the spanning-tree coefficient, the weight of forests with two prescribed roots becomes the resistance between those roots.

## The Kirchhoff index from the two highest coefficients

**Definition.** The Kirchhoff index is the sum of resistances over unordered pairs of distinct vertices:

$$
Kf(G)=\sum_{i<j}R_{ij}
$$

For a fixed vertex count, a smaller index means a smaller average pairwise resistance. The average itself is $2Kf(G)/(n(n-1))$.

> [!info] Metric meaning of the coefficient ratio
> **Theorem.** The sum of all pairwise resistances of a connected graph equals the ratio of the next-to-leading vertex coefficient to the leading one, multiplied by the number of vertices:
>
> $$
> \boxed{
> Kf(G)=\frac{p_{n-2}}{\tau(G)}
> =n\,\frac{p_{n-2}}{p_{n-1}}
> }
> \tag{2}
> $$

> [!proof]- Why the product of component sizes appears
> **Proof.** Let a spanning 2-forest $F$ have component vertex sets $A_F,B_F$ and weight $w(F)$. It separates exactly $|A_F|\,|B_F|$ unordered vertex pairs. Hence
>
> $$
> \sum_{i<j}\tau_{ij}^{(2)}
> =\sum_{F\in\mathcal F_2^{\mathrm{comp}}(G)}|A_F|\,|B_F|\,w(F)
> =p_{n-2}
> $$
>
> Each forest occurs once in the right-hand sum; the two components are unordered. Sum (1) over pairs and then use $p_{n-1}=n\tau(G)$. This gives (2). $\square$

The same factor has two meanings. In [[Vector and Vertex Normalizations of Toponomes#Vertex weight and root choices|vertex normalization]], $|A_F|\,|B_F|$ counts ways to choose roots in the two components. In the Kirchhoff index, it counts vertex pairs separated by them. This is why total resistance corresponds specifically to the vertex coefficient $p_{n-2}$.

The vector coefficient $f_{n-2}$ sums 2-forest weights without accounting for component sizes. Substituting $f_{n-2}$ for $p_{n-2}$ in (2) is generally incorrect.

### Comparison with the spectrum and Green matrix

Let $\lambda_1,\ldots,\lambda_{n-1}>0$ be the nonzero eigenvalues of $\mathbf L$. From

$$
P_G(t)=\prod_{j=1}^{n-1}(1+t\lambda_j)
$$

we obtain

$$
p_{n-1}=\prod_j\lambda_j,
\qquad
p_{n-2}=\left(\prod_j\lambda_j\right)\sum_j\frac1{\lambda_j}
$$

Thus (2) agrees with the classical representations of the Kirchhoff index:

$$
\boxed{
\frac{p_{n-2}}{p_{n-1}}
=\sum_j\frac1{\lambda_j}
=\operatorname{tr}\mathbf{Gr}
=\frac{Kf(G)}n
}
\tag{3}
$$

The identity $Kf=n\operatorname{tr}\mathbf{Gr}$ is independently derived from the distance formula in the [[Centroid, Spanning-Tree, and Eigenvector Centralities#Total resistance to the centroid, the Kirchhoff index, and the radius|note on centralities]]. The forest derivation of (2) and the matrix derivation through the Green matrix therefore lead to the same parameter.

### Root sums and the two ends of the coefficient list

Let $t_1,\ldots,t_{n-1}$ be the roots of $P_G(t)$, counted with multiplicity. By the [[Forest Coefficients and the Laplacian Polynomial#Roots and factorization over the reals|relation between roots and spectrum]], $t_j=-1/\lambda_j$.

> [!info] Two sums involving toponome roots
> **Corollary.** For a connected graph, the negative sum of reciprocal roots of the vertex toponome equals the sum of weighted vertex degrees. The negative sum of the roots themselves equals the Kirchhoff index divided by the vertex count:
>
> $$
> \boxed{
> \begin{aligned}
> -\sum_j\frac1{t_j}&=p_1=\sum_i d_i\\
> -\sum_j t_j&=\frac{p_{n-2}}{p_{n-1}}=\frac{Kf(G)}n
> \end{aligned}
> }
> $$

**Proof.** The first identity follows from $\sum_j\lambda_j=\operatorname{tr}\mathbf L$. The second follows from (3), or from Vieta's formula for the root sum together with (2). $\square$

Thus the low-order coefficient $p_1$ describes total conductance, while the ratio of the two highest coefficients describes total resistance. For example, $P_{K_3}(t)=(1+3t)^2$ has two roots equal to $-1/3$: the negative sum of reciprocal roots is $6$, and the negative root sum is $2/3=Kf(K_3)/3$. Meanwhile, the roots of the characteristic polynomial sum to $6$; these are different polynomial conventions.

## A path and a star on four vertices

Consider the path $P_4$ with edges $ab,bc,cd$ and the star $K_{1,3}$ with edges $ab,ac,ad$, all of conductance $1$.

For both trees, every edge set is a forest, and there is a unique spanning tree. Therefore

$$
F_{P_4}(t)=F_{K_{1,3}}(t)=(1+t)^3,
\qquad \tau=1,
\qquad p_3=4
$$

A spanning 2-forest is obtained by deleting one edge. Vector normalization gives $f_2=3$ in both cases. The vertex coefficient depends on the sizes of the pieces into which the tree splits.

![Deleting each edge of a path and star: component-size products and the Kirchhoff index](Two-Forest%20Weights%20of%20the%20Path%20and%20Star.svg)

*Figure 1. Each edge of each tree is deleted in turn and shown dashed. Vertex colors identify the two components of the remaining forest. For the path, the component-size products are $3,4,3$; for the star, they are $3,3,3$. Their sums give $p_2$ and, since $\tau=1$, also the Kirchhoff index.*

| Graph | Partitions after edge deletion | Root weights | $p_2$ |
| --- | --- | --- | ---: |
| Path $P_4$ | $a\mid bcd$, $ab\mid cd$, $abc\mid d$ | $1\cdot3$, $2\cdot2$, $3\cdot1$ | $10$ |
| Star $K_{1,3}$ | $b\mid acd$, $c\mid abd$, $d\mid abc$ | $1\cdot3$, $1\cdot3$, $1\cdot3$ | $9$ |

The coefficient $p_1=6$ is the same: each of the three edges has two root choices. We obtain

$$
P_{P_4}(t)=1+6t+10t^2+4t^3,
\qquad
P_{K_{1,3}}(t)=1+6t+9t^2+4t^3
$$

By (2),

$$
Kf(P_4)=4\cdot\frac{10}{4}=10,
\qquad
Kf(K_{1,3})=4\cdot\frac94=9
$$

**Independent check.** In a unit-weight tree, resistance equals the number of edges in the unique path between the vertices. In $P_4$, three pairs have distance $1$, two have distance $2$, and one has distance $3$, giving $Kf=3+4+3=10$. In the star, three center–leaf pairs contribute $1$ each, and three leaf pairs contribute $2$ each, giving $Kf=3+6=9$.

Thus two trees with the same vector polynomial can have different Kirchhoff indices. Vertex normalization records component sizes, allowing the difference to appear in $p_2$.

### A check on the cycle

The [[Forest Coefficients and the Laplacian Polynomial#A complete example: the cycle on four vertices|unit-cycle example]] gave

$$
P_{C_4}(t)=1+8t+20t^2+16t^3
$$

Hence

$$
Kf(C_4)=4\cdot\frac{20}{16}=5
$$

An electrical calculation gives the same result. Adjacent vertices are joined by parallel paths of resistances $1$ and $3$, so their resistance is $3/4$. Opposite vertices are joined by two parallel paths of resistance $2$, so their resistance is $1$. There are four pairs of the first kind and two of the second:

$$
Kf(C_4)=4\cdot\frac34+2\cdot1=5
$$

### A weighted check

For the triangle with conductances $c_{ab}=1$, $c_{bc}=2$, and $c_{ca}=3$, we already found $P_G(t)=1+12t+33t^2$. Its spanning-tree coefficient is $\tau=11$, so $Kf=3\cdot12/33=12/11$. Independent parallel-branch calculations give

$$
R_{ab}=\frac5{11},\qquad
R_{bc}=\frac4{11},\qquad
R_{ca}=\frac3{11},\qquad
R_{ab}+R_{bc}+R_{ca}=\frac{12}{11}
$$

## Other coefficient ratios and the reciprocal spectrum

Reading coefficients from highest to lowest gives characteristics of the reciprocal eigenvalues. Set

$$
\sigma_r=\frac{p_{n-1-r}}{p_{n-1}},
\qquad 0\leqslant r\leqslant n-1,
\qquad \sigma_0=1
$$

Here $r$ records the decrease in grade from the highest one. This divides the already obtained vertex coefficients by their leading coefficient; the choice between vector and vertex normalization was made earlier.

> [!info] Coefficients and reciprocal eigenvalues
> **Theorem.** The vertex toponome coefficients, read from highest to lowest and divided by the leading coefficient, are the elementary symmetric functions of the reciprocals of the nonzero Laplacian eigenvalues:
>
> $$
> \boxed{
> \sigma_r=e_r\left(\lambda_1^{-1},\ldots,\lambda_{n-1}^{-1}\right)
> }
> \tag{4}
> $$

Here $e_r$ is the elementary symmetric function: the sum of products over all $r$-element sets of distinct arguments; $e_0=1$.

> [!proof]- Proof by complementary subsets
> **Proof.** The coefficient $p_{n-1-r}$ is the sum of products over all $(n-1-r)$-element sets of eigenvalues. Dividing by $p_{n-1}=\prod_j\lambda_j$ replaces each product by the product of reciprocal values in the complementary $r$-element set. Each such set occurs exactly once. This proves (4), including $r=0$ and $r=n-1$. $\square$

The forest interpretation is retained as well. Let $\mathcal F_{r+1}^{\mathrm{comp}}(G)$ contain spanning forests with $r+1$ components, let $w(F)$ be the product of edge conductances, and let $h(F)$ be the product of component sizes. Then

$$
\sigma_r=\frac1{n\tau(G)}
\sum_{F\in\mathcal F_{r+1}^{\mathrm{comp}}(G)}w(F)h(F)
$$

The same quantities thus describe rooted forests with a prescribed component count and symmetric functions of the reciprocal spectrum. For $r=1$, $\sigma_1=Kf/n$.

### Reciprocal spectral sums and higher indices

**Definition.** For an integer $m\geqslant1$, set

$$
S_m=\sum_{j=1}^{n-1}\lambda_j^{-m}
=\operatorname{tr}(\mathbf{Gr}^{\,m}),
\qquad
Kf_m=nS_m
$$

In this note, call $Kf_m$ the spectral Kirchhoff index of order $m$. The name and the factor $n$ specify the extension used here: $Kf_1=Kf$. When comparing other definitions of higher indices, their normalization must be checked. The power $\mathbf{Gr}^{\,m}$ uses matrix multiplication.

The functions $e_r$ and the power sums are related by Newton's identities. In particular,

$$
S_1=\sigma_1,
\qquad
S_2=\sigma_1^2-2\sigma_2
$$

The first identity was already used in (3). The second follows by expanding the square of the sum of reciprocal eigenvalues: products of two distinct values occur twice. Hence, for $n\geqslant3$,

$$
\boxed{
Kf_2=n\left[
\left(\frac{p_{n-2}}{p_{n-1}}\right)^2
-2\frac{p_{n-3}}{p_{n-1}}
\right]
}
\tag{5}
$$

The three highest coefficients suffice to compute this index. For arbitrary order, the recurrence is

$$
S_m=\sum_{r=1}^{m-1}(-1)^{r-1}\sigma_rS_{m-r}
+(-1)^{m-1}m\sigma_m
$$

Here $\sigma_r=0$ for $r>n-1$; for $m=1$, the sum is empty. In particular, for $n=2$, $S_2=\sigma_1^2$, with no reference to a coefficient having a negative index.

> [!proof]- Derivation of the recurrence
> **Proof.** Set $\mu_j=\lambda_j^{-1}$ and introduce the auxiliary polynomial $E(z)=\prod_j(1+z\mu_j)=\sum_r\sigma_rz^r$. Its logarithmic derivative, as a formal power series, is
>
> $$
> \frac{E'(z)}{E(z)}
> =\sum_j\frac{\mu_j}{1+z\mu_j}
> =\sum_{m\geqslant1}(-1)^{m-1}S_mz^{m-1}
> $$
>
> Multiplying by $E(z)$ and comparing coefficients of $z^{m-1}$ gives the stated recurrence. $\square$

**Remark.** For $m>1$, $Kf_m$ must not be identified with $\sum_{i<j}R_{ij}^m$. The ordinary index has both interpretations because the distance formula is summed linearly; raising individual resistances to powers is a different operation.

For example, for $C_4$, $\sigma_1=5/4$ and $\sigma_2=1/2$. Thus

$$
Kf_2(C_4)=4\left(\frac{25}{16}-1\right)=\frac94,
\qquad
\sum_{i<j}R_{ij}^2=4\cdot\frac9{16}+2=\frac{17}{4}
$$

The nonzero eigenvalues of $C_4$ are $2,2,4$, independently giving $S_2=1/4+1/4+1/16=9/16$ and $Kf_2=9/4$.

Multiplying every conductance by $\alpha>0$ multiplies $p_k$ by $\alpha^k$. Consequently, $\sigma_r$ scales by $\alpha^{-r}$ and $Kf_m$ by $\alpha^{-m}$. For the ordinary index, this agrees with reciprocal scaling of all resistances.

## Coefficients, the centroid, and the circumsphere

Let $a_1,\ldots,a_n$ be the vertices of a Euclidean realization of the resistance simplex, $b$ their centroid, and $O$ the circumcenter. Under our convention, the resistance radius $\rho=R_{\mathrm{sph}}^2$ and the norm $(O-b)^2$ are quadratic quantities.

The [[Centroid, Spanning-Tree, and Eigenvector Centralities#Total resistance to the centroid, the Kirchhoff index, and the radius|centroid relations]] give

$$
\sum_i(a_i-b)^2=\operatorname{tr}\mathbf{Gr}=\frac{Kf(G)}n,
\qquad
\rho=\frac{Kf(G)}{n^2}+(O-b)^2
$$

Substituting (2)–(3) yields the following interpretation of the coefficients.

> [!info] The centroid contribution to the resistance radius
> **Corollary.** The ratio of the next-to-leading vertex coefficient to the leading one equals the sum of resistances from the vertices to the centroid. Dividing it by the vertex count gives the average resistance to the centroid. The resistance radius of the circumsphere is obtained by adding the norm of its center's displacement:
>
> $$
> \boxed{
> \sum_i(a_i-b)^2=\frac{p_{n-2}}{p_{n-1}},
> \qquad
> \rho=\frac{p_{n-2}}{n\,p_{n-1}}+(O-b)^2
> }
> \tag{6}
> $$

In particular,

$$
\rho\geqslant\frac{p_{n-2}}{n\,p_{n-1}}
$$

Equality holds if and only if the circumcenter is the centroid. In general, the term $(O-b)^2$ remains in (6); this formula does not settle whether it can be recovered from polynomial data.

For the unit-weight $C_4$, vertex symmetry makes all diagonal entries of the Green matrix equal, so the centroid is equidistant from every vertex. Hence $O=b$ and

$$
\rho(C_4)=\frac{20}{4\cdot16}=\frac5{16}
$$

This concerns the circumsphere of the three-dimensional resistance simplex, not the circle on which a cycle is usually drawn.

## Results and checks

The two-forest formula (1) converts forest weights into individual resistances. Summing over pairs gives the main result (2): the two highest vertex coefficients determine the Kirchhoff index. Other coefficient ratios describe the reciprocal spectrum and allow successive computation of $Kf_m$.

The difference between the two normalizations appeared in trees with the same vector polynomial: root weights retain the component-size information needed for the Kirchhoff index. Formula (6) connects the same coefficient ratio to the centroid and resistance radius.

> [!example]- Independent computational checks
> All edge sets of $P_4$, $K_{1,3}$, $C_4$, and the triangle with conductances $1,2,3$ were enumerated. Forest coefficients and separating two-forest sums were compared with determinants expanded by permutations. Resistances were independently computed by solving unit-current equations with one grounded vertex, using exact rational arithmetic.
>
> The Green matrix was obtained independently as $(\mathbf L+\mathbf1\mathbf1^{\mathsf T}/n)^{-1}-\mathbf1\mathbf1^{\mathsf T}/n$. Traces of its powers through order five were compared with Newton's recurrence. The radius formula was checked by solving the circumcenter equations. The boundary case $n=2$ was checked on one edge of conductance $2$.

## Sources

- [[Vector and Vertex Normalizations of Toponomes]] — the passage from the exponential through partition types to the polynomial, root weights, and the distinction between normalizations.
- [[Forest Coefficients and the Laplacian Polynomial]] — principal minors with prescribed roots, forest coefficients, and the determinant representation.
- [[Effective Resistance and Graph Geometry]] — the Green matrix and the resistance simplex.
- [[Centroid, Spanning-Tree, and Eigenvector Centralities]] — the Kirchhoff index, centroid, and relation to the resistance radius.
- W. Barrett, E. J. Evans, A. E. Francis, M. Kempton, J. Sinkovic. [Spanning 2-Forests and Resistance Distance in 2-Connected Graphs](https://arxiv.org/abs/1901.00053), 2019. The forest interpretation of resistance for unit conductances. The weighted version (1) is proved above using principal minors.
- A. Ghosh, S. Boyd, A. Saberi. [Minimizing Effective Resistance of a Graph](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf). SIAM Review, 50(1), 37–66, 2008, Sections 2.3–2.5. Weighted graphs, total effective resistance, the Green matrix, and the spectral formula for the ordinary Kirchhoff index. Higher indices are defined separately in this note.
