---
title: Greenian and Polyform Duality
date: 2026-10-28
updated: 2026-10-28
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: greenian-and-polyform-duality-series-navigation
order: 0
description: "The Laplacian and Greenian, mutual duality of exterior exponentials, vector and cut representations, signed forests, potentials, symmetric identities, and toponomes."
---

This series connects the **Laplacian** $L$ and the **Greenian** $\mathrm{Gr}$: two grade-one vector forms whose matrices are mutual pseudoinverses. Their exterior exponentials are boundary polyforms. Duality describes the mutual relationship between these exponentials through deletion from the top form and passage to a complementary grade.

The main working expression for the Greenian uses forms of vectors $a_{ij}=a_j-a_i$. Thus multiplication and forest expansion follow the same rules as for the Laplacian, while coefficients acquire a different meaning and may have either sign. Polar and cut expressions provide additional methods of calculation and interpretation.

Nine notes provide a route from definitions to toponomes. The graph model throughout the series is a connected undirected graph on $n\ge2$ vertices with positive conductances on existing edges. The general algebraic part of the exterior exponential requires no graph; the assumptions of each broader statement are specified separately.

## Contents and reading order

| Order | Note | Main question |
| ---: | --- | --- |
| 1 | [[Laplacian and Greenian - Mutual Duality of Exponentials]] | How is deletion defined, how are complementary grades recovered, and how are normalizations matched? |
| 2 | [[The Canonical Vector Representation of the Greenian]] | Why are vector coefficients unique and equal to $-\mathrm{Gr}_{ij}$, and how do signed spanning-tree sums arise? |
| 3 | [[Cuts and Forest Grades of the Greenian Exponential]] | How do partitions and original graph forests define block-sum forms and every dual grade? |
| 4 | [[The Exterior Exponential and Representations of the Greenian]] | Where do $1/k!$, factorization, and minors come from, and how does the dual form become the Greenian? |
| 5 | [[Greenian Coefficients and Vertex Variations]] | What do polar and forest coefficients mean, and how does the spanning-tree sum change when vertices are removed or attached? |
| 6 | [[Greenian Exponentials of Standard Graphs]] | How are all grades calculated for complete graphs, stars, cycles, weighted paths, and more complex examples? |
| 7 | [[The Greenian Metric and Potentials]] | How does the original Laplacian determine potentials in the Greenian metric, and how does a potential differ from a coefficient? |
| 8 | [[Symmetric Identities of the Greenian]] | What does centering preserve, and which evaluations respect boundary identities? |
| 9 | [[Toponomes of the Greenian Exponential and Dual Pairs]] | How are signed forest sums reduced, the two normalizations distinguished, and spectral polynomials compared? |

## Main results

**Canonical vector coefficients.** In the direct space of differences,

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij},\qquad
\mathbf{Gr}=\mathbf L^+
$$

The Green matrix is the Gram matrix of centroid vectors in the original resistance metric. Thus $\gamma_{ij}=-(a_i-h)\cdot(a_j-h)$, where $h=n^{-1}\sum_i a_i$. Coefficients $\gamma_{ij}$ may be positive, negative, or zero, including for pairs with no original graph edge.

**The ordinary exterior exponential.** Set $d=n-1$, $M=\exp L$, and $N=\exp(\mathrm{Gr})$. Vector factorization gives

$$
N=\prod_{i<j}\left(e+\gamma_{ij}[a_{ij}]^2\right),\qquad
N_k=\frac{\mathrm{Gr}^k}{k!}
$$

Repetitions and cycles vanish; the remaining products correspond to forests of Greenian couplings. A forest's weight is the product of its coefficients. Grouping by vertex partitions expresses coefficients through spanning-tree sums on blocks. Formulas for every grade and examples with negative contributions appear in [[Greenian Exponentials of Standard Graphs]].

**Mutual duality.** Let $a_i^\vee$ denote classes of coordinate functionals in $W^*$, and $p_i=a_i-h$ the direct centered vectors. Under the identification

$$
\mathcal C(a_i^\vee)=p_i,\qquad
\mathcal C(Q_1)=\mathrm{Gr},\qquad
D=\exp Q_1,\qquad N=\mathcal C(D)
$$

the exponentials satisfy

$$
M_d/Q_k=M_{d-k},\qquad
Q_d/M_k=Q_{d-k},\qquad 0\le k\le d
$$

The slash denotes linear exterior deletion. The forms initially lie in paired spaces; $\mathcal C$ allows their expressions on direct vectors to be compared.

**Potentials and variations.** The polar expression for $Q_1$ uses resistances of the original graph. The cut forest expression connects coefficients with spanning-tree sums of induced subgraphs and attachment of a new vertex. After centered transfer, the normalized potential in $N$ is given by the Laplacian:

$$
P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v
$$

Here $\mathbf u,\mathbf v$ are coordinate columns of direct vectors with zero sum. Higher simple forms use determinants of such pairwise values. A form's coefficient, its potential, and its contribution to a chosen forest sum are different quantities.

**Identities and toponomes.** Centering preserves boundaries and their identities. Component types define the full multivariate toponome of the canonical forest representation. After rooted specialization,

$$
P_L(t)=\det(\mathbf I+t\mathbf L),\qquad
P_{\mathrm{Gr}}(t)=\det(\mathbf I+t\mathbf{Gr})
$$

and

$$
P_{\mathrm{Gr}}(t)=\frac{t^d}{n\tau}P_L(1/t)
$$

The last expression is a polynomial identity after expanding the right-hand side; its value at $t=0$ is $1$. It relates rooted sums of complementary grades. It does not imply a general reversal of individual coefficients of the full toponome.

## Representations and normalizations

In the table, $T=[(a_1\ldots a_n)]^2$ is built on direct vertices, $T^\vee=[a_1^\vee\cdots a_{n-1}^\vee]^2$ on dual elements, and $\Theta=[(a_1^\vee\ldots a_n^\vee)]^2=n^2T^\vee$. The symbol $\tau$ denotes the spanning-tree sum of the original graph.

| Exponential | Argument space | Top grade |
| --- | --- | --- |
| $M=\exp L$ | Direct vectors | $\tau T$ |
| $D=\exp Q_1$ | Dual elements | $T^\vee/\tau=\Theta/(n^2\tau)$ |
| $N=\exp(\mathrm{Gr})=\mathcal C(D)$ | Direct vectors | $T/(n^2\tau)$ |

The grade-zero term of every exponential is $e$. Under $\mathcal C$, we have $\mathcal C(\Theta)=T$ and $\mathcal C(T^\vee)=T/n^2$. Thus the coefficients $1/\tau$ and $1/(n^2\tau)$ refer to different reference forms of the same result.

In the full vector toponome of the Greenian, the coefficient of $x_d$ is $1/(n^2\tau)$. Rooted specialization adds $n$ root choices and gives the coefficient $1/(n\tau)$ of $t^d$. The auxiliary forest expression $\widetilde D=\tau D$ is marked by a tilde and has grade-zero term $\tau e$.

## Routes by task

- **Definition and algebra.** [[Laplacian and Greenian - Mutual Duality of Exponentials]], followed by [[The Canonical Vector Representation of the Greenian]] and [[The Exterior Exponential and Representations of the Greenian]]. Prerequisites: [[Basic Objects and Operations of Polyform Algebra]] and [[Laplacian Exponential]]. General matroid theory is not required.
- **Coefficients, cuts, and graph changes.** After the canonical expression, proceed to [[Cuts and Forest Grades of the Greenian Exponential]] and [[Greenian Coefficients and Vertex Variations]]. Retain the specific vertex blocks and distinguish original forests from edges crossing a cut.
- **Examples and metric meaning.** [[Greenian Exponentials of Standard Graphs]], followed by [[The Greenian Metric and Potentials]]. For matrix transformations, see [[Laplacian, Green Matrix, and Effective Resistance Matrix]]; for the centroid interpretation, see [[KVP Decomposition and Oriented Extensions]].
- **Symmetric identities and toponomes.** [[Symmetric Identities of the Greenian]], followed by [[Toponomes of the Greenian Exponential and Dual Pairs]]. Prerequisites are collected in [[en/Partition toponomes/Partition Toponomes|Partition Toponomes]] and [[en/Polynomial toponomes/Polynomial Toponomes|Polynomial Toponomes]]. For the general role of identities, see the [[en/Symmetric polyforms/Symmetric Polyforms|Symmetric Polyforms]] series.

## Distinctions to retain while reading

Formulas involving both spaces use $a_i$ and $a_i^\vee$; sections devoted solely to the dual side may omit $\vee$ by explicit convention. The zero-sum relation concerns $a_i^\vee$ or $p_i$, not the original independent vertices.

The labeled partition $abc\mid d$, its positive type $(2)$, and the monomial $x_2$ represent different levels of data. The number $2$ in the type and variable index is the boundary grade of a three-vertex component. The original vertex count $n$ is retained separately. The full reduction fixes a chosen forest representation, since identities may relate forms of different types.

The vector expansion of $N_k$ uses $k$-edge forests of Greenian couplings. The cut expression for the same grade uses $(d-k)$-edge forests of the original graph. The indexing forest's type in the second expression does not automatically become the type of the boundary form.

After transfer to one space, the exterior product of the exponentials is $\exp L\,\exp(\mathrm{Gr})=\exp(L+\mathrm{Gr})$. The multiplicative inverse of $\exp L$ is $\exp(-L)$. The matrix equality $\mathbf L\mathbf{Gr}=\mathbf J$, exterior deletion, and graph or matroid duality concern other operations and relationships.

## Reproducible checks

All programs use the Python standard library and exact rational arithmetic. From the repository root, run:

    python checks/dual/verify_vector.py
    python checks/dual/verify_exponential.py
    python checks/dual/verify_variations.py
    python checks/dual/verify_typical.py
    python checks/dual/verify_potentials.py
    python checks/dual/verify_symmetry.py
    python checks/dual/verify_toponomes.py

The [check descriptions and script dependencies](https://github.com/magin67/pmg-notes/blob/v5/checks/dual/README.en.md) specify the scope of each suite. They compare exterior products, minors, forest enumerations, spanning coefficients, and rooted polynomials. Finite checks supplement the proofs in the notes.

## Scope of the series and further directions

For the full toponome, a question remains: what additional data allow the Greenian toponome to be recovered from the Laplacian toponome without recovering the labeled matrix? The spectral formula is proved, but combines types within a grade.

A directed extension requires bilinear forms, argument order, and directions to be aligned with the [[en/Balanced graphs/Balanced Graphs|Balanced Graphs]] series. Symmetric formulas do not transfer automatically. A separate topic is the polyform of the isotropic Gram matrix, its top and next-to-top components, and its connection with sphere geometry.

The general theory of cuts goes beyond the cut representation used here. These directions remain recorded in the [[ru/Карта библиотеки PMG#Отложенные вопросы и продолжения|project map (in Russian)]]. The English series follows the checked [[ru/Гриниан и дуальность полиформ/Гриниан и дуальность полиформ|Russian edition]]. Current definitions and notation are collected in [[Core specification|Core Specification of PMG]] and [[PMG terminology|PMG Terminology]].
