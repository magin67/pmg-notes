---
title: "Forest Resistance Scales"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: forest-resistance-scales
lang: en
description: "Ratios of adjacent forest coefficients, their probabilistic meaning, dimensions, and ordering. Trees, cycles, one-point gluing, and rooted analogues on the Greenian side."
order: 4
---

Forest coefficients compare adjacent connectivity levels: forests with $k+1$ components and those with $k$ components. The ratio of their total weights has the dimension of resistance. It describes the possibility of joining the components of a random forest without creating a cycle.

[[The Normalized Forest Polynomial and Power-Sum Parameters]] constructs an additive power-sum family from the same coefficient sequence. Here we study neighboring ratios $\xi_k$. They are all positive and have the same dimension, but higher ratios are generally not additive. The main result is a probabilistic formula involving the total conductance of admissible added edges. Rooted coefficients give a different formula, which we relate to the Greenian.

## Definition and assumptions

Let $G=(\mathcal V,E)$ be a finite connected undirected loopless graph on $n\ge2$ vertices. Existing edges have positive conductances $c_\ell$. Parallel edges are allowed and are separate elements of the cycle matroid; their conductances add in the Laplacian matrix.

Write $d=n-1$. An ordinary spanning forest contains all vertices, including isolated ones, and no cycles. No roots are chosen in its components. Use the definitions from [[Forest Coefficients - Grade, Components, and Corank]]:

$$
f_g=\sum_{\substack{F\text{ a forest in }G\\\#E(F)=g}}w(F),\qquad
w(F)=\prod_{\ell\in E(F)}c_\ell,\qquad f_0=1,\quad f_d=\tau
$$

A forest of corank $k$ has $d-k$ edges and $k+1$ components. Its normalized coefficients are $\alpha_k=f_{d-k}/\tau$; in particular, $\alpha_0=1$.

**Definition.** The forest resistance scales are the ratios

$$
\boxed{
\xi_k(G)=\frac{f_{d-k}(G)}{f_{d-k+1}(G)}
=\frac{\alpha_k(G)}{\alpha_{k-1}(G)},\qquad 1\le k\le d
}
\tag{1}
$$

All coefficients in (1) are positive: deleting edges of a spanning tree gives forests of every grade from $0$ to $d$. Normalization by the global $\tau$ assumes connectedness; adding isolated vertices lies outside this note's assumptions.

The name “resistance scale” refers to the dimension and the probabilistic interpretation below. It does not assert that $\xi_k$ is the effective resistance between any canonically chosen vertices.

### Connection with the normalized polynomial

Successive use of (1) gives

$$
\alpha_k=\prod_{j=1}^k\xi_j,\qquad
\Phi_G(u)=1+\sum_{k=1}^d\left(\prod_{j=1}^k\xi_j\right)u^k
\tag{2}
$$

Thus, for known $d$, the entire scale sequence recovers the normalized forest polynomial, as well as

$$
\tau=\left(\prod_{j=1}^d\xi_j\right)^{-1},\qquad
f_{d-k}=\tau\prod_{j=1}^k\xi_j
$$

The empty product at $k=0$ is $1$. All information in the ordinary forest polynomial is retained, but the matroid itself cannot generally be recovered from it; an explicit counterexample appears in the [[The Normalized Forest Polynomial and Power-Sum Parameters#What can be recovered and what remains undetermined?|discussion of completeness of the forest family]].

The first scale agrees with the first forest power-sum parameter:

$$
\xi_1=s_1^{\mathrm{for}}=\frac{f_{n-2}}\tau
$$

For $k>1$, the ratios $\xi_k$ and parameters $s_k^{\mathrm{for}}$ have different definitions and dimensions.

## A random forest and admissible edge addition

Let $\mathcal F_k(G)$ denote the ordinary spanning forests of corank $k$. For fixed $1\le k\le d$, sample a forest from

$$
\Pr_k(F)=\frac{w(F)}{f_{d-k}},\qquad F\in\mathcal F_k(G)
\tag{3}
$$

For a given forest, put

$$
A(F)=\sum_{\substack{\ell=\{i,j\}\in E\\
i,j\text{ in different components of }F}}c_\ell
$$

This is the total conductance of original edges that can be added to $F$ without creating a cycle. Addition reduces the component count by one. Connectedness of $G$ and the presence of at least two components in $F$ ensure $A(F)>0$.

![[Admissible Extensions of K4 Two-Forests.svg]]

**Admissible additions.** In unit $K_4$, a 2-forest of type $3+1$ admits three edges to its isolated vertex; the unused edge within the three-vertex component would close a cycle. For type $2+2$, all four edges between components are admissible. There are $12$ and $3$ such forests, respectively, and all $15$ have weight $1$. Hence $\mathbb E_1 A=(12\cdot3+3\cdot4)/15=16/5$. The formula below gives $\xi_1=3/(16/5)=15/16$. Line crossings without a circle are not vertices.

**Proposition.** For distribution (3),

$$
\boxed{
\mathbb E_k A(F)=(n-k)\frac{f_{d-k+1}}{f_{d-k}},\qquad
\xi_k=\frac{n-k}{\mathbb E_k A(F)}
}
\tag{4}
$$

**Proof.** Consider pairs $(F,\ell)$ where $F\in\mathcal F_k(G)$ and $\ell$ joins two components of $F$. The pair weight is $w(F)c_\ell$. Summing first over forests gives

$$
\sum_{F\in\mathcal F_k(G)}w(F)A(F)
$$

On the other hand, $F'=F\cup\{\ell\}$ is a forest with $d-k+1=n-k$ edges, and the pair weight equals $w(F')$. Every such $F'$ arises in exactly $n-k$ ways, by deleting any one of its edges. Therefore

$$
\sum_{F\in\mathcal F_k(G)}w(F)A(F)=(n-k)f_{d-k+1}
$$

Division by $f_{d-k}$ proves both equalities in (4). $\square$

The formula relates one step of joining forest components to the mean total weight of admissible couplings. The number $n-k$ counts edges of the resulting forest, not admissible edges of each initial forest; the latter count may vary.

The expression takes the reciprocal of an expectation. In general, this is not the expectation of the reciprocal:

$$
\frac1{\mathbb E_k A(F)}\ne\mathbb E_k\frac1{A(F)}
$$

Moreover, $A(F)$ sums conductances between all distinct components. It does not define a two-terminal effective conductance between a prescribed vertex pair.

## Matroid invariance, dimensions, and extreme values

**Matroid invariance.** An isomorphism of cycle matroids preserving corresponding conductances preserves independent sets of each size and their weights. Hence it preserves numerator and denominator in (1), and therefore $\xi_k$. The weight condition is essential.

The probabilistic formula agrees with this description: an edge is admissible exactly when adding it preserves independence. Components are convenient for the graph interpretation, but the admissible extensions themselves are determined by the matroid.

**Dimensions and scaling.** If conductance has dimension $C$, then

$$
[f_g]=C^g,\qquad [A(F)]=C,\qquad [\xi_k]=C^{-1}
$$

Square brackets here denote dimensions, not PMG forms. Every $\xi_k$ has the dimension of effective resistance, a quadratic quantity in resistance geometry. The dimension of $s_m^{\mathrm{for}}$ is $C^{-m}$.

Multiplying all conductances by a dimensionless factor $\sigma>0$ gives

$$
\xi_k(\sigma G)=\sigma^{-1}\xi_k(G)
\tag{5}
$$

This follows from the degrees of numerator and denominator. The probabilistic explanation is the same: all forests of a fixed corank acquire a common weight factor, so distribution (3) is unchanged, while $A(F)$ is multiplied by $\sigma$.

**Extreme values.** Introduce the total conductance $S=\sum_{\ell\in E}c_\ell$. Then

$$
\boxed{
\xi_1=\frac{f_{n-2}}\tau,\qquad
\xi_d=\frac{f_0}{f_1}=\frac1S
}
\tag{6}
$$

At $k=d$, the forest has no edges and contains $n$ isolated vertices. Every edge is admissible, $A(F)=S$, and $n-k=1$, directly checking (4). Throughout the range, $A(F)\le S$, so also

$$
\xi_k\ge\frac{n-k}{S}
$$

## Ordering of scales and log-concavity

For positive conductances, forest coefficients satisfy

$$
f_g^2\ge f_{g-1}f_{g+1},\qquad 1\le g\le d-1
\tag{7}
$$

This applies the external theory of log-concavity of matroid independent sets. We do not prove the general theorem here, but use the result of Anari, Liu, Oveis Gharan, and Vinzant [1].

**Definition.** A nonnegative sequence $b_0,\ldots,b_N$ without internal zeros is **ultra-log-concave** if $b_g/\binom Ng$ is log-concave: the square of each interior term is at least the product of its neighbors. “Without internal zeros” means that no zero lies between positive terms. Forest coefficients are positive from $f_0$ through $f_d$ and zero above the rank.

A precise reference to the external result requires one more term. A nonnegative polynomial is **completely log-concave** if every sequence of directional derivatives in directions with nonnegative coordinates yields either the zero polynomial or a polynomial whose logarithm is concave on the positive orthant. The sequence may be empty. Here a directional derivative means $D_v=\sum_i v_i\partial/\partial z_i$, with $v_i\ge0$; this is Definition 1.3 of [1].

To justify the weighted specialization, let $N_E=\#E$. By Theorem 4.1 of the arXiv:1811.01600v1 version of [1], the polynomial

$$
\sum_{I\text{ independent}}
y^{N_E-\#I}\prod_{\ell\in I}z_\ell
$$

is completely log-concave. Lemma 2.2 preserves this property under $z_\ell=c_\ell z$. For the resulting bivariate polynomial, Proposition 5.1 gives ultra-log-concavity of the coefficients. In our notation,

$$
f_g^2\ge
\frac{(g+1)(N_E-g+1)}{g(N_E-g)}f_{g-1}f_{g+1},
\qquad 1\le g\le d-1
\tag{8}
$$

Here $N_E$ is the edge count, not the vertex count or rank $d$. Zero coefficients above the rank do not enter the stated range. Inequality (7) is a weaker consequence of (8).

**Corollary.** The scales are ordered:

$$
\boxed{\xi_1\ge\xi_2\ge\cdots\ge\xi_d>0}
\tag{9}
$$

**Proof.** For $g=d-k$,

$$
\frac{\xi_{k+1}}{\xi_k}
=\frac{f_{g-1}f_{g+1}}{f_g^2}\le1
$$

This proves (9). The stronger (8), together with positivity, even yields $\xi_{k+1}<\xi_k$ for $1\le k<d$. When $d=1$, there are no adjacent values to compare. $\square$

This ordering concerns different coranks of one fixed graph. It does not compare different graphs after edges are added. Nor does (7) follow from real-rootedness of $\Phi_G$: the unit triangle has nonreal roots, as shown in the [[The Normalized Forest Polynomial and Power-Sum Parameters#Unit triangle|triangle example]].

## Trees, cycles, and the complete graph

### Weighted tree

In a tree $T$, every set of deleted edges defines a forest. Put $q_\ell=1/c_\ell$, and let $e_k(q)$ be the elementary symmetric function of degree $k$ in these resistances, with $e_0(q)=1$. Then

$$
f_{d-k}(T)=\tau(T)e_k(q),\qquad
\boxed{\xi_k(T)=\frac{e_k(q)}{e_{k-1}(q)}}
\tag{10}
$$

Indeed, deleting a set $J$ of $k$ edges changes the tree weight to $\tau\prod_{\ell\in J}q_\ell$. Summing over $J$ gives (10).

If $T$ has $n$ vertices and every conductance equals $c$, then $e_k(q)=\binom{n-1}{k}c^{-k}$, so

$$
\xi_k(T)=\frac{n-k}{kc}
\tag{11}
$$

The same answer follows from (4): exactly the $k$ deleted edges are admissible, so $A(F)=kc$ for every forest of that corank. Different tree shapes give the same sequence for the same conductance collection.

### Cycle

For a cycle $C_n$ with common conductance $c$, every proper edge subset is a forest. Thus

$$
f_{d-k}(C_n)=\binom{n}{k+1}c^{n-1-k},\qquad
\boxed{\xi_k(C_n)=\frac{n-k}{(k+1)c}}
\tag{12}
$$

For $k\ge1$, exactly $k+1$ edges have been deleted, and each joins different components of the resulting forest. Hence $A(F)=(k+1)c$, and (4) again gives the same result.

Formulas (11), (12) compare trees and cycles with the same $n,c$. They do not replace a general law for changes of scales under arbitrary graph modification.

### Exact values

| Graph and conductances | $(f_0,f_1,\ldots,f_d)$ | $(\xi_1,\ldots,\xi_d)$ |
| --- | --- | --- |
| Tree with three edges of conductances $1,2,3$ | $(1,6,11,6)$ | $(11/6,6/11,1/6)$ |
| Unit triangle | $(1,3,3)$ | $(1,1/3)$ |
| Unit $K_4$ | $(1,6,15,16)$ | $(15/16,2/5,1/6)$ |

The $K_4$ coefficients are counted in [[Forest Coefficients - Grade, Components, and Corank]]. At corank $1$, there are 12 forests of component sizes $3+1$ and 3 of sizes $2+2$. In the first case $A(F)=3$; in the second $A(F)=4$. Hence

$$
\mathbb E_1 A(F)=\frac{12\cdot3+3\cdot4}{15}=\frac{16}5,\qquad
\xi_1(K_4)=\frac3{16/5}=\frac{15}{16}
$$

This is an independent check using admissible additions, not another division of forest coefficients. It also distinguishes the two averages:

$$
\frac1{\mathbb E_1 A(F)}=\frac5{16},\qquad
\mathbb E_1\frac1{A(F)}
=\frac{12/3+3/4}{15}=\frac{19}{60}
$$

## One-point gluing

Let $G=G_1\vee G_2$ identify exactly one vertex of two connected graphs with disjoint edge sets. Conductances are retained. Then $d=d_1+d_2$ and

$$
\Phi_G(u)=\Phi_{G_1}(u)\Phi_{G_2}(u)
$$

This follows from the unique decomposition of every forest into forests of the pieces, proved in the [[Forest Coefficients - Grade, Components, and Corank#Gluing and coefficient convolution|convolution formula]]. Setting $\alpha_i(G_j)=0$ outside $0\le i\le d_j$ gives

$$
\boxed{
\xi_k(G_1\vee G_2)=
\frac{\displaystyle\sum_{i+j=k}\alpha_i(G_1)\alpha_j(G_2)}
{\displaystyle\sum_{i+j=k-1}\alpha_i(G_1)\alpha_j(G_2)}
},\qquad 1\le k\le d
\tag{13}
$$

At $k=1$, the denominator is $1$, so

$$
\xi_1(G_1\vee G_2)=\xi_1(G_1)+\xi_1(G_2)
$$

This agrees with $\xi_1=s_1^{\mathrm{for}}$. For higher ratios, mixed terms in the numerator and denominator remain.

For example, every unit tree with two edges has $\Phi(u)=(1+u)^2$ and $\xi_2=1/2$. One-point gluing of two such trees produces a four-edge tree:

$$
\Phi_G(u)=(1+u)^4,\qquad
\xi_2(G)=\frac64=\frac32\ne\frac12+\frac12
$$

Thus matroid invariance of every $\xi_k$ does not imply additivity. Nevertheless, in successive one-point gluings of fixed pieces, the entire forest polynomial and hence the entire scale sequence are independent of the attachment vertices. Gluing at several vertices or along a shared edge subgraph does not satisfy (13) without separate justification.

## Scales and dual grades

In the edge expansion of the Laplacian exponential $M=\exp L$, the weight sum of grade $M_g$ is $f_g$. In the cut expansion of the Greenian exponential $D=\exp Q_1$, grade $Q_k$ uses original forests with $d-k$ edges:

$$
Q_k=\frac1\tau\sum_{F\in\mathcal F_k(G)}w(F)\Phi_{\pi(F)}
$$

Here $\Phi_{\pi(F)}$ is the form on the product of dual block sums defined in [[Cuts and Forest Grades of the Greenian Exponential]]. Its term-weight sum in this expression is $\alpha_k$.

Thus on the Greenian side, $\xi_k=\alpha_k/\alpha_{k-1}$ is a ratio of weight sums in neighboring dual grades. The original forests and their positive weights are retained in this passage. This explains why a parameter defined through Laplacian forests also has a dual representation.

These sums refer to the specified expression. They are not evaluations of a general linear functional on arbitrary form representations; see the [[The Normalized Forest Polynomial and Power-Sum Parameters#Why the polyform logarithm does not replace the scalar logarithm|discussion of scalar reduction]].

## Rooted ratios and the spectral Greenian polynomial

### Another positive sequence

For the component partition $\pi(F)$ of a forest, put

$$
\omega(F)=\prod_{B\in\pi(F)}\#B
$$

This counts choices of one root in each component; an isolated vertex contributes $1$. The forest still has $k+1$ components.

The rooted coefficients and determinant polynomials are

$$
p_{L,g}=\sum_{\substack{F\text{ a forest in }G\\\#E(F)=g}}w(F)\omega(F),\qquad
P_L(t)=\det(\mathbf I+t\mathbf L)=\sum_{g=0}^d p_{L,g}t^g
$$

$$
P_{\mathrm{Gr}}(u)=\det(\mathbf I+u\mathbf{Gr})
=\sum_{k=0}^d p_{\mathrm{Gr},k}u^k,\qquad
\mathbf{Gr}=\mathbf L^+
$$

By [[Toponomes of the Greenian Exponential and Dual Pairs|spectral coefficient reversal]],

$$
p_{\mathrm{Gr},k}=\frac{p_{L,d-k}}{n\tau}
$$

For comparison with (1), write

$$
\boxed{
\xi_k^{\mathrm{root}}=
\frac{p_{\mathrm{Gr},k}}{p_{\mathrm{Gr},k-1}}
=\frac{p_{L,d-k}}{p_{L,d-k+1}},\qquad 1\le k\le d
}
\tag{14}
$$

All these ratios are positive and have dimension $C^{-1}$, but the factors $\omega(F)$ distinguish them from $\xi_k$. For example,

$$
\xi_1^{\mathrm{root}}=\operatorname{tr}\mathbf{Gr}=\frac{Kf(G)}n,
\qquad
\xi_d^{\mathrm{root}}=\frac1{2S}
$$

Here $Kf(G)=\sum_{i<j}R_{ij}$; the last equality uses $p_{L,0}=1$ and $p_{L,1}=2S$. For the unit path $P_4$ and star $K_{1,3}$, the first ordinary scale is $3$, whereas the rooted ratio is $5/2$ and $9/4$, respectively. Thus the rooted family is not generally determined by the original cycle matroid.

### A rooted probabilistic formula

Sample $F\in\mathcal F_k(G)$ from a different distribution:

$$
\Pr_k^{\mathrm{root}}(F)=\frac{w(F)\omega(F)}{p_{L,d-k}}
$$

It can be obtained by sampling a rooted forest with weight $w(F)$ and then forgetting the roots. It is not distribution (3).

If an admissible edge $\ell$ has endpoints in different components $B_\ell,C_\ell$, define

$$
A_{\mathrm{root}}(F)=
\sum_{\ell\text{ admissible}}
c_\ell\left(\frac1{\#B_\ell}+\frac1{\#C_\ell}\right)
$$

**Proposition.** For the rooted distribution,

$$
\boxed{
\xi_k^{\mathrm{root}}=
\frac{n-k}{\mathbb E_k^{\mathrm{root}}A_{\mathrm{root}}(F)}
}
\tag{15}
$$

**Proof.** Let the component sizes be $b,c$. Before addition, these components admit $bc$ root choices; after merging, they admit $b+c$. Hence

$$
\frac{\omega(F\cup\{\ell\})}{\omega(F)}
=\frac{b+c}{bc}=\frac1b+\frac1c
$$

The pair weight therefore satisfies

$$
w(F)\omega(F)c_\ell
\left(\frac1b+\frac1c\right)
=w(F\cup\{\ell\})\omega(F\cup\{\ell\})
$$

As in the proof of (4), each resulting forest $F'$ has $n-k$ edges and is counted that many times. Thus

$$
\sum_{F\in\mathcal F_k(G)}w(F)\omega(F)A_{\mathrm{root}}(F)
=(n-k)p_{L,d-k+1}
$$

Division by $p_{L,d-k}$ gives (15). $\square$

Both the forest distribution and the added-edge weight have changed. Changing only one would not yield ratio (14).

### Comparison on the complete graph

For unit $K_4$, the rooted Greenian polynomial is $P_{\mathrm{Gr}}(u)=(1+u/4)^3$. Therefore

| $k$ | Ordinary scale $\xi_k$ | Rooted ratio $\xi_k^{\mathrm{root}}$ |
| ---: | ---: | ---: |
| $1$ | $15/16$ | $3/4$ |
| $2$ | $2/5$ | $1/4$ |
| $3$ | $1/6$ | $1/12$ |

The rooted formula at $k=1$ can be checked without a determinant. Type $3+1$ has three admissible edges and multiplier $1/3+1=4/3$; type $2+2$ has four admissible edges and multiplier $1/2+1/2=1$. Both give $A_{\mathrm{root}}(F)=4$. Hence for any distribution over these types, in particular the rooted one,

$$
\mathbb E_1^{\mathrm{root}}A_{\mathrm{root}}(F)=4,\qquad
\xi_1^{\mathrm{root}}=\frac34
$$

The ordinary expectation for this graph was $16/5$. The difference comes from the root choices and the component-merging rule.

## Canonical Greenian forests and signed weights

The centered identification $\mathcal C$ takes $D$ to $N=\mathcal C(D)=\exp(\mathrm{Gr})$. Its canonical vector expansion uses couplings with weights

$$
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

Forests of these couplings differ from original forests in the cut representation of $Q_k$. For the unit path $a-b-c-d$, a matrix calculation gives $\mathrm{Gr}_{ab}=1/8$, so $\gamma_{ab}=-1/8$. The corresponding one-edge forest has negative weight.

Consequently, dividing individual canonical forest weights by their sum does not generally define a probability distribution. Positive semidefiniteness of $\mathbf{Gr}$ does not make every $\gamma_{ij}$ nonnegative.

Formula (15) avoids this issue through exact spectral reversal: its positive distribution uses original rooted forests. It does not interpret signed canonical weights as probabilities. Nor is the ordinary canonical polynomial $F_{\mathrm{Gr}}$ replaced by the rooted $P_{\mathrm{Gr}}$; their distinction is explained in the [[The Normalized Forest Polynomial and Power-Sum Parameters#The canonical forest polynomial of the Greenian|comparison of three polynomials]].

## Geometric meaning and continuation

For $\xi_k$ we have proved positivity, resistance dimension, and an interpretation through admissible extensions of a random forest. These properties do not automatically construct a canonical point pair with resistance $\xi_k$, a form with this norm, or a sphere with this radius. For higher scales, such a geometric realization remains a separate problem and may depend on the graph class.

The first scale $\xi_1=s_1^{\mathrm{for}}$ enters the exact formula $\rho=\xi_1/3-H_2/12$, proved in [[Resistance Radius - Forest Formula and Matroid Invariance]]. Here $\rho=R_{\mathrm{sph}}^2$ and $H_2=\sum_\ell c_\ell R_\ell^2$ is an edge characteristic. Its probabilistic interpretation through random spanning trees and its connection with derivatives of the spanning-tree polynomial appear in [[Edge Resistances and Random Spanning Trees]].

## Status of the results and verification

The note proves probabilistic formulas (4), (15), matroid invariance of ordinary scales, scaling, extreme values, and the one-point gluing law (13). Tree and cycle formulas come from direct counting. The rooted relationship (14) uses the published spectral reversal for Laplacian and Greenian coefficients. Log-concavity is applied as an external theorem [1], from which scale ordering is derived here. General matroid-theoretic results are not claimed as new PMG results.

Exact rational computations cover 50 connected test graphs, including all 38 connected subgraphs of $K_4$ with edge conductances $1,2,3,5,7,11$, the examples, cycles, fractional weights, and parallel edges. At 146 corank levels, direct forest enumeration is compared with admissible-extension counting in the ordinary and rooted models. Rooted coefficients are also checked against principal minors of $\mathbf L$ and $\mathbf L^+$. Further checks cover scaling, one-point gluing, and coefficient inequalities. The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_forest_scales.py) uses helpers from the adjacent verify_forest_power_sums.py; both need only the Python standard library. Run from the repository root:

    python checks/matroid/verify_forest_scales.py

Finite checks supplement general proofs. The probability distributions in this note require positive original conductances. The metric and duality are used for connected undirected graphs; no extension to balanced graphs is made.

## References and connections

1. Anari N., Liu K., Oveis Gharan S., Vinzant C. *Log-concave polynomials III: Mason’s ultra-log-concavity conjecture for independent sets of matroids*. Proceedings of the American Mathematical Society, 152 (2024), 1969-1981. [DOI: 10.1090/proc/16724](https://doi.org/10.1090/proc/16724). In the [open arXiv:1811.01600v1 version](https://arxiv.org/abs/1811.01600v1), Theorem 4.1, Lemma 2.2, and Proposition 5.1 give the weighted specialization and inequality (8) used here.
2. [[Forest Coefficients - Grade, Components, and Corank]]: ordinary forest sums, indexing, computation methods, and gluing convolution.
3. [[The Normalized Forest Polynomial and Power-Sum Parameters]]: the additive family, distinct scalar reductions, and limits of matroid recovery.
4. [[Cuts and Forest Grades of the Greenian Exponential]] and [[Toponomes of the Greenian Exponential and Dual Pairs]]: two Greenian forest representations and exact reversal of rooted coefficients.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Лесные резистивные масштабы|Русская версия]].
