---
title: "Matroid Parameters and Forest Characteristics of Graphs"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: matroid-parameters-and-forest-characteristics-series-navigation
order: 0
description: "Seven notes on the cycle matroid, forest coefficients, the Laplacian and Greenian, resistance scales, edge characteristics, the radius, and the limits of invariance under gluing."
---

When the same graph parts are glued together, some characteristics are preserved even though vertex distances and positions change. This series explains which of these invariances follow from the **cycle matroid**: the edge independence structure in which precisely the forests are independent. It then provides ways to compute the corresponding parameters and derives their gluing laws separately.

In PMG, the starting connection is algebraic: edges correspond to vectors, forests to nonzero exterior products, and cycles make those products vanish. Forest sums occur in the Laplacian exponential and, after passing to the complementary grade, in the cut representation of the Greenian exponential. Matroid parameters are therefore considered on both sides of the duality.

The seven notes constitute direction **C02** of the [[ru/Карта библиотеки PMG|project map (in Russian)]]. The series prepares the study of boundary data and chains of cores; a prior course in general matroid theory is not required.

## Contents and reading order

| Order | Note | Definitions and main result |
| ---: | --- | --- |
| 1 | [[The Cycle Matroid and Exterior Products of Edges]] | What a matroid and a matroid parameter are; why forest independence and linear independence agree; what is preserved and what is forgotten. |
| 2 | [[Forest Coefficients - Grade, Components, and Corank]] | Ordinary forests and three indices; computation through partitions and deletion-contraction; distinction from rooted sums. |
| 3 | [[The Normalized Forest Polynomial and Power-Sum Parameters]] | Coefficients $\alpha_k$, the polynomial $\Phi_G$, and parameters $s_m^{\mathrm{for}}$; computation by Newton identities and additivity. |
| 4 | [[Forest Resistance Scales]] | Ratios $\xi_k$, their dimensions, ordering, and probabilistic meaning; comparison with the rooted model. |
| 5 | [[Edge Resistances and Random Spanning Trees]] | Probabilities $\eta_\ell=c_\ell R_\ell$, derivatives of the spanning-tree polynomial, and the family $H_q$. |
| 6 | [[Resistance Radius - Forest Formula and Matroid Invariance]] | Geometric definition $\rho=R_{\mathrm{sph}}^2$, original source, and proof of $\rho=\xi_1/3-H_2/12$. |
| 7 | [[Gluing and the Limits of Matroid Invariance]] | One-point gluing, the Whitney twist, boundary choice, and two forest states; conditions for preserving parameters. |

For a first reading, follow the order in the table. If you already have a specific question, a shorter route is possible:

- **Understand invariance under gluing:** the [[The Cycle Matroid and Exterior Products of Edges#What is a matroid?|definition of a matroid]], the [[The Cycle Matroid and Exterior Products of Edges#What is a matroid parameter?|definition of a matroid parameter]], then [[Gluing and the Limits of Matroid Invariance]].
- **Compute forest characteristics:** [[Forest Coefficients - Grade, Components, and Corank]], followed by [[The Normalized Forest Polynomial and Power-Sum Parameters]] and [[Forest Resistance Scales]].
- **Recover the radius from forest and edge data:** the definitions of $\xi_1$ in the [[Forest Resistance Scales#Definition and assumptions|note on scales]] and $H_q$ in [[Edge Resistances and Random Spanning Trees]], followed by [[Resistance Radius - Forest Formula and Matroid Invariance]].

## Prerequisites and assumptions

The algebraic part requires [[Basic Objects and Operations of Polyform Algebra]] and [[Laplacian Exponential]]. The dual language is introduced in [[Laplacian and Greenian - Mutual Duality of Exponentials]] and [[Cuts and Forest Grades of the Greenian Exponential]]. The full Greenian reading route is given in the [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]] navigator.

The main metric model is a finite connected undirected loopless graph on $n\ge2$ vertices with positive conductances $c_\ell$. Parallel edges, when allowed, retain separate labels. A weighted matroid isomorphism preserves the conductances of corresponding edges. Forest functions are also defined for disconnected graphs; deletion and contraction account for loops, parallel edges, and isolated vertices.

Current notation is fixed in [[Core specification]] and [[PMG terminology]]. The Green matrix is denoted by $\mathbf{Gr}=\mathbf L^+$, the Gramian by $\mathbf G$, and the centroid by $h$. The resistance radius is quadratic: $\rho=R_{\mathrm{sph}}^2$, with $D_{\mathrm{res}}=4\rho$. The former term “mass” is not used as current terminology.

## Forest indices and two representations

An ordinary spanning forest contains all vertices, including isolated ones, and has no chosen roots. If $g$ is its number of edges, $m$ its number of components, and $r=n-\kappa(G)$ the rank of the original graph, then

$$
m=n-g,\qquad k=r-g=m-\kappa(G)
$$

For a connected graph, $r=d=n-1$ and $m=k+1$. The sum of weights of grade-$g$ forests is

$$
f_g=\sum_{\substack{F\text{ a forest}\\\#E(F)=g}}\prod_{\ell\in E(F)}c_\ell
$$

For a connected graph, $\tau=f_d$ and $\alpha_k=f_{d-k}/\tau$. The same original forest occurs in two expansions:

| Representation | Grade of the form | Number of original edges | Sum of term weights |
| --- | ---: | ---: | --- |
| Edge expansion of $M=\exp L$ | $g$ | $g$ | $f_g$ |
| Cut expansion of $D=\exp Q_1$ | $k$ | $d-k$ | $\alpha_k=f_{d-k}/\tau$ |

Here $Q_1$ is the dual representation of the Greenian. The centered identification $\mathcal C(a_i^\vee)=a_i-h$ takes $D$ to $\exp(\mathrm{Gr})$. The table lists sums in specific forest representations, not values of a universal linear functional on polyforms.

The canonical vector expansion of the Greenian itself uses different connections, with coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$. They can have either sign and occur at pairs with no original edge. Its ordinary forest polynomial $F_{\mathrm{Gr}}$ generally differs from the normalized original polynomial $\Phi_G$.

Rooted forests give another pair:

$$
P_L(t)=\det(\mathbf I+t\mathbf L),\qquad
P_{\mathrm{Gr}}(u)=\det(\mathbf I+u\mathbf{Gr})
=\frac{u^d}{n\tau}P_L(u^{-1})
$$

The last equality is understood as a polynomial identity after expanding the right-hand side. Each original forest coefficient is additionally multiplied here by the product of its component sizes, that is, by the number of root choices. Reversal of this sequence differs from the passage $f_g\mapsto f_{d-k}/\tau$.

## Parameter families and the gluing law

The normalized polynomial and its formal logarithm define

$$
\Phi_G(u)=\sum_{k=0}^d\alpha_k u^k,\qquad
\log\Phi_G(u)=\sum_{m\ge1}(-1)^{m-1}\frac{s_m^{\mathrm{for}}}m u^m
$$

Adjacent-coefficient ratios and the edge family are defined by

$$
\xi_k=\frac{\alpha_k}{\alpha_{k-1}},\quad 1\le k\le d,\qquad
H_q=\sum_{\ell\in E}\frac{\eta_\ell^q}{c_\ell},\quad q=1,2,\ldots,
\qquad \eta_\ell=c_\ell R_\ell
$$

$R_\ell$ is the effective resistance between the endpoints of an existing edge, and $\eta_\ell$ is its inclusion probability in a random spanning tree sampled with probabilities proportional to products of conductances. All listed parameters are matroid-invariant under the stated assumptions. Their transformation under gluing is a separate result.

In the following table, the parts have exactly one common vertex and disjoint edge sets; conductances are preserved.

| Quantities | Under $G=G_1\vee G_2$ |
| --- | --- |
| $F_G$, $\Phi_G$, $\tau$ | Values for the parts multiply. |
| $f_g$, $\alpha_k$ | Coefficient sequences are convolved. |
| $s_m^{\mathrm{for}}$, $H_q$, $\xi_1$, $\rho$ | Values for the parts add. |
| $\xi_k$ for $k>1$ | Ratios of two convolutions; no general additivity. |

Forest power-sum parameters can be negative and are not spectral sums by definition. The scales $\xi_k$ are positive and ordered; their geometric realization for higher $k$ remains a separate problem. The spectral parameters $\operatorname{tr}(\mathbf L^m)$ and $\operatorname{tr}(\mathbf{Gr}^m)$ belong to the rooted pair and are generally not determined by the original matroid.

## What the matroid preserves and what the parameters do not determine

![[Path and Star Matroid - Edge Correspondence.svg]]

**The same independence, different vertex geometry.** Every edge set of the unit-weight path $P_4$ and star $K_{1,3}$ is a forest. All ordinary forest coefficients and matroid parameters therefore agree, including $\rho=3/4$. But the sums of resistances over all vertex pairs are $10$ and $9$. The computation and comparison of Laplacians and Greenians are given in the [[The Cycle Matroid and Exterior Products of Edges#One matroid, different vertex geometry|path and star example]].

Equality of forest polynomials does not recover the matroid either: the polynomial records total weights by cardinality, not the independent sets themselves. A counterexample with different parallel classes appears in the [[The Normalized Forest Polynomial and Power-Sum Parameters#What can be recovered and what remains undetermined?|section on the limits of recovery]]. The full partition toponome, in turn, contains additional component-size data and is generally not matroid-invariant.

For two-point gluing, one must distinguish a twist of an already chosen boundary, which preserves the matroid, from a choice of a different boundary pair, which can change it. Identifying edges of a shared seam also requires a separate law. Examples and exact conditions are collected in [[Gluing and the Limits of Matroid Invariance]].

## Status and reproducible checks

Definitions, proofs, and computed examples are distinguished in every note. Classical results are accompanied by their original sources; in particular, log-concavity is used as an external theorem, while the forest formula for the radius is given with a proof and a conversion to the PMG normalization. Finite checks control calculations and normalizations but do not replace general proofs.

A verification script is provided for each of the seven notes. The scripts use exact rational arithmetic and the Python standard library. [Check descriptions, dependencies, and commands](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/README.en.md) are available in the public repository. Figures are stored alongside the notes; drawing programs and the English-label translation script are also available in the checks directory.

## Continuation to boundary data and chains of cores

The series develops scalar parameters through gluing laws and the minimal two-point boundary description. A general boundary requires partitions of its vertices, the corresponding forest states, boundary polyforms, and groves. These form a separate continuation, after which direction **C01, “Chains of Cores,”** can use the parameters developed here to compare chain isomers and establish the limits of invariance.

Higher forest scales do not yet have a general geometric realization. Formulas for undirected graphs are not automatically extended to balanced graphs.

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Матроидные параметры и лесные характеристики графов|Русская версия]].
