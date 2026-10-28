---
title: "The Normalized Forest Polynomial and Power-Sum Parameters"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: normalized-forest-polynomial-and-power-sum-parameters
lang: en
description: "Normalized forest coefficients, the formal logarithm, and Newton identities. Matroid invariance and additivity of power-sum parameters under one-point gluing, distinction from Greenian spectral parameters, and limits of matroid recovery."
order: 3
---

Forest polynomials multiply under one-point gluing. To compare different assemblies of a graph, it is useful to have parameters that add: each piece's contribution can then be computed separately, and the attachment vertices do not affect the result. The logarithm of the normalized forest polynomial provides such a family.

[[Forest Coefficients - Grade, Components, and Corank|The note on forest coefficients]] constructs generating functions by grade and corank and proves their gluing laws. Here we introduce normalized coefficients and power-sum parameters, derive a recurrence for computing them, and compare them with spectral parameters of the Laplacian and Greenian. Factorization will be a consequence of the definition, not a required computational step.

## Normalized coefficients and the additivity problem

Let $G=(\mathcal V,E)$ be a finite connected undirected loopless graph on $n\ge2$ vertices with positive conductances $c_\ell$. Put $d=n-1$. Parallel edges, if present, retain separate labels when discussing the cycle matroid; two such edges form a cycle. The metric matrix uses their total conductance.

Write $f_g(G)$ for the weight sum of all ordinary spanning forests with $g$ edges:

$$
f_g(G)=\sum_{\substack{F\text{ a forest in }G\\\#E(F)=g}}w(F),\qquad
w(F)=\prod_{\ell\in E(F)}c_\ell
$$

A forest contains all vertices, including isolated ones; no roots are chosen in its components. Connectedness gives $f_d=\tau>0$, $f_0=1$, and a forest with $d-k$ edges has $k+1$ components. Use the polynomials already introduced:

$$
F_G(t)=\sum_{g=0}^d f_g t^g,\qquad
\mathscr F_G(u)=u^d F_G(u^{-1})
$$

**Definition.** The normalized forest coefficients and normalized forest polynomial are

$$
\boxed{
\alpha_k(G)=\frac{f_{d-k}(G)}{\tau(G)},\qquad
\Phi_G(u)=\frac{\mathscr F_G(u)}{\tau(G)}
=\sum_{k=0}^d\alpha_k(G)u^k
}
\tag{1}
$$

Thus $\alpha_0=1$ and $\alpha_d=1/\tau$. All $\alpha_k$ for $0\le k\le d$ are positive: deleting $k$ edges of any spanning tree gives at least one forest of the required corank. In recurrences, set $\alpha_k=0$ for $k>d$.

The coefficient $\alpha_k$ also has a polyform interpretation. In the fixed cut representation

$$
Q_k=\frac1\tau\sum_{\substack{F\text{ a forest in }G\\\#E(F)=d-k}}
w(F)\Phi_{\pi(F)}
$$

it is the sum of term weights. Here $\pi(F)$ is the component partition and $\Phi_{\pi(F)}$ is the form on the product of dual block sums. Its definition and the proof of the expansion appear in the [[Cuts and Forest Grades of the Greenian Exponential#The forest formula for grades of the Greenian exponential|forest formula for Greenian grades]]. The polynomial $\Phi_G(u)$ and cut form $\Phi_\pi$ are distinguished by their argument and subscript.

Under one-point gluing $G=G_1\vee G_2$, the normalized coefficients satisfy convolution:

$$
\alpha_k(G)=\sum_{a+b=k}\alpha_a(G_1)\alpha_b(G_2)
$$

In particular,

$$
\alpha_1(G)=\alpha_1(G_1)+\alpha_1(G_2)
$$

$$
\alpha_2(G)=\alpha_2(G_1)+\alpha_1(G_1)\alpha_1(G_2)+\alpha_2(G_2)
$$

A mixed term already appears in the second coefficient. Obtaining an additive family therefore requires transforming the entire sequence $\alpha_k$.

## Power-sum parameters through the formal logarithm

The polynomial $\Phi_G$ has constant coefficient $1$, so its logarithm is defined in the ring of formal power series:

$$
\log\Phi_G(u)=\sum_{q\ge1}\frac{(-1)^{q-1}}q\bigl(\Phi_G(u)-1\bigr)^q
$$

This is an algebraic definition: only finitely many terms $q\le m$ are needed to compute the coefficient at $u^m$. No numerical value of $u$, convergence domain, or branch of the complex logarithm is required.

**Definition.** The forest power-sum parameters $s_m^{\mathrm{for}}(G)$ are specified by

$$
\boxed{
\log\Phi_G(u)=\sum_{m\ge1}(-1)^{m-1}
\frac{s_m^{\mathrm{for}}(G)}m u^m
}
\tag{2}
$$

The superscript $\mathrm{for}$ refers to ordinary forest coefficients of the original graph and distinguishes this family from spectral power sums. The letter $p$ is retained for the rooted coefficients used in [[Forest Coefficients and the Laplacian Polynomial]].

The parameters are defined for every integer $m\ge1$, including $m>d$. The finite degree of $\Phi_G$ does not make its logarithm a polynomial.

## Newton identities and computation without factorization

**Proposition.** For every $m\ge1$, the following recurrence holds:

$$
\boxed{
m\alpha_m=\sum_{j=1}^m(-1)^{j-1}\alpha_{m-j}s_j^{\mathrm{for}}
}
\tag{3}
$$

**Proof.** Formal differentiation of (2) gives

$$
\Phi_G'(u)=\Phi_G(u)
\sum_{j\ge1}(-1)^{j-1}s_j^{\mathrm{for}}u^{j-1}
$$

The coefficient at $u^{m-1}$ is $m\alpha_m$ on the left and the convolution in (3) on the right. $\square$

These are the classical Newton identities for elementary symmetric functions and power sums, applied to the coefficients (1). They are not specific to graphs. The graph information lies in the $\alpha_k$ themselves.

The first values are

$$
\begin{aligned}
s_1^{\mathrm{for}}&=\alpha_1\\
s_2^{\mathrm{for}}&=\alpha_1^2-2\alpha_2\\
s_3^{\mathrm{for}}&=\alpha_1^3-3\alpha_1\alpha_2+3\alpha_3\\
s_4^{\mathrm{for}}&=\alpha_1^4-4\alpha_1^2\alpha_2+2\alpha_2^2
+4\alpha_1\alpha_3-4\alpha_4
\end{aligned}
\tag{4}
$$

In practice, compute $f_g$ by one of the [[Forest Coefficients - Grade, Components, and Corank|forest-coefficient methods]], divide the reversed sequence by $\tau$, and apply (3) successively. Polynomial roots need not be found.

For $m>d$, the same recurrence takes the form

$$
s_m^{\mathrm{for}}=\sum_{k=1}^d(-1)^{k-1}\alpha_k s_{m-k}^{\mathrm{for}}
\tag{5}
$$

Thus finitely many coefficients determine the infinite sequence.

### Recovering the original coefficients

If $d$ is known, the first $d$ parameters $s_1^{\mathrm{for}},\ldots,s_d^{\mathrm{for}}$ successively recover $\alpha_1,\ldots,\alpha_d$ using (3), starting from $\alpha_0=1$. Then

$$
\tau=\frac1{\alpha_d},\qquad
f_{d-k}=\frac{\alpha_k}{\alpha_d},\qquad 0\le k\le d
\tag{6}
$$

Passing to power-sum parameters loses no information about the full one-variable forest polynomial. Its advantage is the gluing law, rather than additional graph data.

## Factorization parameters and dimensions

Since $\deg\Phi_G=d$ and $\Phi_G(0)=1$, over the complex numbers one can write

$$
\boxed{
\Phi_G(u)=\prod_{\nu=1}^d(1+\zeta_\nu u),\qquad
s_m^{\mathrm{for}}=\sum_{\nu=1}^d\zeta_\nu^m
}
\tag{7}
$$

The second equality follows by taking the formal logarithm of the product. The coefficient $\alpha_k$ is the elementary symmetric function of degree $k$ in $\zeta_1,\ldots,\zeta_d$.

Here the $\zeta_\nu$ are nonzero factorization parameters, specified with multiplicities and without an ordering. The roots in the variable $u$ are $-1/\zeta_\nu$, not the $\zeta_\nu$ themselves. The notation $x_i$ remains reserved for partition-toponome variables.

Real coefficients imply conjugate pairing of nonreal parameters and real values of every $s_m^{\mathrm{for}}$. They do not imply that every $\zeta_\nu$ is real or that every power sum is positive. A real $\zeta_\nu$ must be positive: a negative value would give a positive root $u$, impossible for a polynomial with positive coefficients. However, the parameters need not all be real.

Writing $C$ for the dimension of conductance gives

$$
[\alpha_k]=C^{-k},\qquad
[u]=C,\qquad
[\zeta_\nu]=C^{-1},\qquad
[s_m^{\mathrm{for}}]=C^{-m}
\tag{8}
$$

Square brackets in (8) denote dimensions, not PMG forms. The polynomial $\Phi_G(u)$ is dimensionless. Having resistance dimension does not by itself make $\zeta_\nu$ the effective resistance of a vertex pair.

If $\sigma G$ multiplies all conductances by a dimensionless number $\sigma>0$, then

$$
\Phi_{\sigma G}(u)=\Phi_G(u/\sigma),\qquad
\alpha_k(\sigma G)=\sigma^{-k}\alpha_k(G),\qquad
s_m^{\mathrm{for}}(\sigma G)=\sigma^{-m}s_m^{\mathrm{for}}(G)
\tag{9}
$$

The corresponding unordered collection of factorization parameters is $\{\zeta_\nu/\sigma\}$.

## Matroid invariance and additivity

These properties have different grounds and require separate proofs.

**Matroid-invariance proposition.** An isomorphism of cycle matroids preserving the conductance of each corresponding edge preserves $\Phi_G$, all $\alpha_k$, and all $s_m^{\mathrm{for}}$.

**Proof.** The isomorphism preserves rank $d$, independent sets of each size, and products of their weights. It therefore preserves $f_g$, including $f_d=\tau$. Apply (1) and (2). $\square$

**Additivity proposition.** Let connected graphs $G_1,G_2$ have disjoint edge sets and be glued at exactly one vertex, preserving conductances and making no further identifications. Then for every $m\ge1$,

$$
\boxed{
s_m^{\mathrm{for}}(G_1\vee G_2)
=s_m^{\mathrm{for}}(G_1)+s_m^{\mathrm{for}}(G_2)
}
\tag{10}
$$

**Proof.** Every forest of the glued graph splits uniquely into forests of the pieces. A cycle cannot traverse both pieces when they meet only at one vertex. Consider this decomposition for two triangles:

![[Forests under One-Point Gluing.svg]]

**Choosing in each piece.** Solid edges form $F_1$ and $F_2$; dashed edges show the remaining original edges. Identifying $p_1,p_2$ creates no cycle. The illustrated choice has $g_1=2$, $g_2=1$, and total $g=3$; with $d_1=d_2=2$, this gives $k_1=0$, $k_2=1$, $k=1$. The isolated vertex $d$ is retained.

Every pair of forests behaves this way: grades and coranks add, and weights multiply. Hence

$$
\mathscr F_{G_1\vee G_2}=\mathscr F_{G_1}\mathscr F_{G_2},\qquad
\tau(G_1\vee G_2)=\tau(G_1)\tau(G_2)
$$

Division gives $\Phi_{G_1\vee G_2}=\Phi_{G_1}\Phi_{G_2}$. The formal logarithm of a product of series with constant coefficient $1$ is the sum of their logarithms. This can be checked by differentiation: derivatives agree and constant coefficients are zero. Comparing coefficients using (2) completes the proof. $\square$

For repeated one-point gluing, apply the formula successively. This explains the purpose of the power-sum family: for given pieces, their contribution to each $s_m^{\mathrm{for}}$ does not depend on the attachment vertices. In matroid language, this is additivity under direct sums.

Identifying several vertices or a shared edge subgraph requires a new law for forest states. Matroid invariance alone does not extend (10) to those operations.

## The forest family and the Laplacian-Greenian spectral pair

Let $\lambda_1,\ldots,\lambda_d>0$ be the nonzero eigenvalues of the Laplacian matrix $\mathbf L$. The Green matrix $\mathbf{Gr}=\mathbf L^+$ has nonzero eigenvalues $\lambda_1^{-1},\ldots,\lambda_d^{-1}$.

For the rooted forest polynomials,

$$
P_L(t)=\det(\mathbf I+t\mathbf L)=\prod_{\nu=1}^d(1+\lambda_\nu t)
$$

$$
P_{\mathrm{Gr}}(u)=\det(\mathbf I+u\mathbf{Gr})
=\prod_{\nu=1}^d\left(1+\frac u{\lambda_\nu}\right)
=\frac{u^d}{n\tau}P_L(u^{-1})
\tag{11}
$$

The normalization $n\tau=\prod_\nu\lambda_\nu$ and the forest meaning of the coefficients are explained in [[Forest Coefficients and the Laplacian Polynomial]] and [[Toponomes of the Greenian Exponential and Dual Pairs]]. The coefficient at $t^g$ in $P_L$ is

$$
p_{L,g}=\sum_{\substack{F\text{ a forest in }G\\\#E(F)=g}}
w(F)\prod_{B\in\pi(F)}\#B
$$

The factor $\prod_B\#B$ counts choices of one root in each component. It distinguishes $p_{L,g}$ from $f_g$. On the Greenian side, the coefficient at $u^k$ in (11) is $p_{L,d-k}/(n\tau)$, whereas in $\Phi_G$ it is $f_{d-k}/\tau$.

Formal logarithms of determinants give two spectral families:

$$
\log P_L(t)=\sum_{m\ge1}(-1)^{m-1}
\frac{\operatorname{tr}(\mathbf L^m)}m t^m
$$

$$
\log P_{\mathrm{Gr}}(u)=\sum_{m\ge1}(-1)^{m-1}
\frac{\operatorname{tr}(\mathbf{Gr}^m)}m u^m
\tag{12}
$$

Here

$$
\operatorname{tr}(\mathbf L^m)=\sum_\nu\lambda_\nu^m,\qquad
\operatorname{tr}(\mathbf{Gr}^m)=\sum_\nu\lambda_\nu^{-m}>0
$$

Thus exact spectral duality consists of reciprocating the nonzero eigenvalues. The forest parameters $s_m^{\mathrm{for}}$ and traces $\operatorname{tr}(\mathbf{Gr}^m)$ have the same dimension $C^{-m}$ but come from different polynomials and generally differ.

### The canonical forest polynomial of the Greenian

The Greenian exponential also has a canonical edge expansion with weights $\gamma_{ij}=-\mathrm{Gr}_{ij}$ on the complete set of vertex pairs. Its ordinary forest polynomial is

$$
F_{\mathrm{Gr}}(u)=\sum_{k=0}^d
\left(\sum_{\substack{F\text{ a forest on vertex pairs}\\\#E(F)=k}}
\prod_{ij\in E(F)}\gamma_{ij}\right)u^k
$$

The weights $\gamma_{ij}$ may have either sign. This is a third reduction: it uses $k$ Greenian couplings rather than $d-k$ original edges. The comparison is:

| Polynomial | Forests being summed | Coefficient at $u^k$ |
| --- | --- | --- |
| $\Phi_G(u)$ | Ordinary original forests of corank $k$ | $f_{d-k}/\tau$ |
| $F_{\mathrm{Gr}}(u)$ | Ordinary forests of $k$ couplings with weights $\gamma_{ij}$ | Sum of products of $\gamma_{ij}$ |
| $P_{\mathrm{Gr}}(u)$ | Rooted Greenian forests; equivalently, rooted original forests of corank $k$ | $p_{L,d-k}/(n\tau)$ |

Since $F_{\mathrm{Gr}}(0)=1$, its formal logarithm also defines power sums of its own factorization parameters. This implies neither equality with $s_m^{\mathrm{for}}$ nor equality with the traces (12). Even the first coefficients differ:

$$
[u]\Phi_G=\frac{f_{d-1}}\tau,\qquad
[u]F_{\mathrm{Gr}}=\frac12\operatorname{tr}\mathbf{Gr},\qquad
[u]P_{\mathrm{Gr}}=\operatorname{tr}\mathbf{Gr}
$$

The symbol $[u]$ here means extraction of the coefficient at $u$. The canonical formula is proved in the [[Toponomes of the Greenian Exponential and Dual Pairs#The full toponome and the meaning of its coefficients|description of canonical coefficients]].

### Why the polyform logarithm does not replace the scalar logarithm

In polyform algebra,

$$
D(u)=\sum_{k=0}^d u^kQ_k=\exp(uQ_1),\qquad
\log D(u)=uQ_1
$$

This does not mean that $\log\Phi_G(u)$ contains only the first power of $u$. Passing from a fixed forest representation of $Q_k$ to its weight sum is not an algebra homomorphism. In particular, it need not preserve products or commute with logarithms. Without a fixed representation, the coefficient sum does not even define a linear functional on forms: structural identities relate different expansions.

The simplest example is a graph with one edge of conductance $c$. It has $d=1$, $Q_1^2=0$, and

$$
D(u)=e+uQ_1,\qquad \log D(u)=uQ_1
$$

But the scalar sum is $\Phi_G(u)=1+u/c$, so

$$
\log\Phi_G(u)=\sum_{m\ge1}(-1)^{m-1}\frac{u^m}{m c^m}
$$

In the polyform product, repeating a direction makes the term vanish. Ordinary multiplication of the numbers $1/c$ has no such rule. Dependence of reductions on representation is discussed in [[Toponomes and Structural Identities]] and the [[Forest Coefficients - Grade, Components, and Corank#Dependence of the sum on the representation|section on weight sums]].

## Examples

### Weighted tree

Every edge set of a tree $T$ is independent. Therefore

$$
\Phi_T(u)=\prod_{\ell\in E(T)}\left(1+\frac u{c_\ell}\right),\qquad
\boxed{s_m^{\mathrm{for}}(T)=\sum_{\ell\in E(T)}c_\ell^{-m}}
\tag{13}
$$

In this case the parameters $\zeta_\nu$ really are individual edge resistances. They also equal the effective resistances between those endpoints, since a tree has no alternative path. For general graphs, this interpretation of (7) is not established and, as the triangle shows, is impossible as a family of positive edge resistances.

For three edges with conductances $1,2,3$,

$$
\Phi_T(u)=(1+u)\left(1+\frac u2\right)\left(1+\frac u3\right)
=1+\frac{11}6u+u^2+\frac16u^3
$$

$$
s_1^{\mathrm{for}}=\frac{11}6,\qquad
s_2^{\mathrm{for}}=\frac{49}{36},\qquad
s_3^{\mathrm{for}}=\frac{251}{216}
$$

Permuting these conductances or changing the tree's shape leaves the forest family unchanged. The spectral family may change. For example, for the unit path $P_4$ and unit star $K_{1,3}$,

$$
\Phi_{P_4}(u)=\Phi_{K_{1,3}}(u)=(1+u)^3,\qquad
s_m^{\mathrm{for}}=3\quad(m\ge1)
$$

But

$$
\operatorname{tr}\mathbf{Gr}_{P_4}=\frac52,\qquad
\operatorname{tr}\mathbf{Gr}_{K_{1,3}}=\frac94
$$

These values equal $Kf/n$: the sums of pairwise resistances are $10$ and $9$, respectively. See the [[The Cycle Matroid and Exterior Products of Edges#One matroid, different vertex geometry|example of two trees with one matroid]] for the calculation. It shows that Greenian spectral parameters are not generally matroid invariants. Even the first trace fails the law (10): the sum of Greenian traces of three separate unit edges is $3/2$, whereas gluing gives $5/2$ or $9/4$.

### Unit triangle

For the triangle, $f_0=1$, $f_1=3$, $f_2=\tau=3$, hence

$$
\Phi_{K_3}(u)=1+u+\frac13u^2,\qquad
\zeta_{1,2}=\frac12\left(1\pm\frac{i}{\sqrt3}\right)
$$

Both parameters are nonreal. Equations (4), (5) give the sequence in the table. For comparison, $\mathbf L$ has nonzero eigenvalues $3,3$, so

$$
P_{\mathrm{Gr}}(u)=\left(1+\frac u3\right)^2,\qquad
\operatorname{tr}(\mathbf{Gr}^m)=\frac2{3^m}
$$

| $m$ | $s_m^{\mathrm{for}}(K_3)$ | $\operatorname{tr}(\mathbf{Gr}^m)$ |
| ---: | ---: | ---: |
| $1$ | $1$ | $2/3$ |
| $2$ | $1/3$ | $2/9$ |
| $3$ | $0$ | $2/27$ |
| $4$ | $-1/9$ | $2/81$ |

Thus forest power-sum parameters are not generally moments of positive resistances or a positive spectrum. The negative value of $s_4^{\mathrm{for}}$ is consistent with positivity of every $\alpha_k$.

The third polynomial also differs. Here $\mathbf{Gr}=\frac13(\mathbf I-\mathbf1\mathbf1^{\mathsf T}/3)$ and $\gamma_{ij}=1/9$ for each pair. Direct forest counting gives

$$
F_{\mathrm{Gr}}(u)=1+\frac13u+\frac1{27}u^2
$$

### Complete graph on four vertices

The [[Forest Coefficients - Grade, Components, and Corank|complete-graph forest count]] gives $f_0=1$, $f_1=6$, $f_2=15$, $f_3=\tau=16$. Consequently,

$$
\Phi_{K_4}(u)=1+\frac{15}{16}u+\frac38u^2+\frac1{16}u^3
$$

$$
s_1^{\mathrm{for}}=\frac{15}{16},\qquad
s_2^{\mathrm{for}}=\frac{33}{256},\qquad
s_3^{\mathrm{for}}=-\frac{177}{4096}
$$

Unlike the triangle, a negative parameter appears already at $m=3$. The spectral values are $\operatorname{tr}(\mathbf{Gr}^m)=3/4^m$ and remain positive.

## What can be recovered and what remains undetermined?

For known rank $d$, the power-sum family recovers every ordinary forest coefficient through (6). However, the forest polynomial stores only the total weights of independent sets of each size. It does not store the sets themselves and is not a complete matroid invariant.

**Definition.** A matroid element is a loop if its singleton is dependent. Two distinct nonloop elements are parallel if their pair is a minimal dependent set. Maximal groups of pairwise parallel elements are parallel classes; a single nonloop element also forms a class if it has no parallel elements. In a cycle matroid, nonloop edges with the same endpoints form such a class: each pair is a cycle of length $2$.

This distinguishes matroids without spectral computation. Consider two multigraphs $H_1,H_2$ on $a,b,c$, with all edge conductances equal to one:

- the first has four parallel edges $ab$, one $bc$, and one $ca$;
- the second has three parallel edges $ab$, three $bc$, and no $ca$.

Parallel edges are separate matroid elements here. Both graphs have $f_1=6$, and their spanning-tree counts are

$$
\tau(H_1)=4\cdot1+4\cdot1+1\cdot1=9,\qquad
\tau(H_2)=3\cdot3=9
$$

Thus both have

$$
\Phi(u)=1+\frac23u+\frac19u^2=\left(1+\frac u3\right)^2
$$

and identical values $s_m^{\mathrm{for}}=2/3^m$ for every $m\ge1$. Yet the first matroid has a four-element parallel class, while the maximal parallel classes of the second have three elements. Matroid isomorphism preserves this distinction. Thus even equality of the entire power-sum family does not prove isomorphism; equality of a few parameters is still less conclusive.

### Passing to neighboring forest ratios

Another normalization uses adjacent coefficients:

$$
\xi_k=\frac{f_{d-k}}{f_{d-k+1}}=\frac{\alpha_k}{\alpha_{k-1}},
\qquad 1\le k\le d
$$

All $\xi_k$ are positive and have dimension $C^{-1}$, whereas $s_m^{\mathrm{for}}$ has dimension $C^{-m}$ and may be negative. Only the first parameters agree:

$$
\xi_1=s_1^{\mathrm{for}},\qquad
\alpha_k=\xi_1\xi_2\cdots\xi_k
$$

For $k>1$, the ratios $\xi_k$ must not be identified with the power-sum parameters. Their probabilistic interpretations, normalizations, ordering, and behavior under gluing are studied in [[Forest Resistance Scales]].

## Status of the results and verification

Definition through a formal logarithm, the Newton identities, and the description through factorization parameters belong to the classical algebra of symmetric functions. Their derivations are given here in forest-series notation. Matroid invariance is proved by preservation of independent sets and weights; additivity is proved separately for the specified one-point gluing.

Spectral reversal uses the normalization of the published Greenian series. Ordinary, rooted, and canonical forest sums remain distinct after taking logarithms. An exponential polyform expression does not imply an exponential expression for its scalar sum.

The tree, triangle, $K_4$, and multigraph-pair examples are computed directly. Exact rational checks cover these examples and all 38 connected subgraphs of $K_4$ with fixed edge conductances $1,2,3,5,7,11$, for 46 test graphs in total. Forest coefficients are obtained by directly enumerating edge sets. Power-sum parameters through order $8$ are checked by Newton recurrence and an independent expansion of the formal series $\log(1+v)$.

Additional comparisons use powers of edge resistances for trees and powers of $\mathbf L^+$ computed from the Laplacian for the spectral family. Rooted coefficients are checked against principal minors. Checks also cover spectral reversal, recovery of original coefficients, scaling, and additivity when one edge is attached. The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_forest_power_sums.py) uses only the Python standard library. Run:

    python checks/matroid/verify_forest_power_sums.py

Finite computations supplement rather than replace the general proofs.

No general positive metric interpretation of higher $s_m^{\mathrm{for}}$ is asserted: the negative examples rule it out without further conditions. Possible interpretations for special graph classes require separate results. All metric and dual comparisons concern connected undirected graphs with positive original conductances; no extension to balanced graphs is made.

## Sources and connections

1. Brent R. P. *On computing factors of cyclotomic polynomials*. Report TR-CS-92-13, Australian National University, September 1992. [Author's text, Section 1.4, formulas (13), (14)](https://maths-people.anu.edu.au/~brent/pd/rpb135.pdf). Newton identities and the formal exponential relation between coefficients and power sums; only this general algebraic machinery is used.
2. [[Forest Coefficients - Grade, Components, and Corank]]: original forest sums, index reversal, coefficient computation, and the gluing product.
3. [[Laplacian and Greenian - Mutual Duality of Exponentials]] and [[Cuts and Forest Grades of the Greenian Exponential]]: polyform duality and normalized coefficients on the $Q_k$ side.
4. [[Toponomes of the Greenian Exponential and Dual Pairs]]: canonical and rooted Greenian polynomials, normalizations, and spectral reversal.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Нормированный лесной полином и степенные параметры|Русская версия]].
