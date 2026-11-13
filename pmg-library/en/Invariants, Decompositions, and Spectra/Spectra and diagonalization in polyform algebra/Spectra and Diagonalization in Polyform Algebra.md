---
title: "Spectra and Diagonalization in Polyform Algebra"
date: 2026-10-30
updated: 2026-11-11
revision: 7
translated_revision: 8
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: spectra-and-diagonalization-series-navigation
order: 0
description: "Six notes on eigendirections, diagonal polyforms and duality, spectra of paths and cycles, Chebyshev transformations, the spectral cone, and information lost under projection."
tags:
  - spectra
  - reconstruction
aliases:
  - "en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra"
  - "en/Spectra and diagonalization in polyform algebra/index"
---

[[ru/Инварианты, разложения и спектры/Спектры и диагонализация в алгебре полиформ/Спектры и диагонализация в алгебре полиформ|Русский]]

Scalar invariants and forest polynomials allow graphs to be compared, but do not retain all information about their eigendirections. This series introduces the **full spectral representation**: eigenvalues together with projectors in vertex coordinates. It reconstructs the Laplacian and Greenian, their exterior exponentials, and pairwise resistances.

In the language of PMG, the diagonal expression makes grades elementary symmetric polynomials in the forms of eigendirections. Duality relates complementary sets of these directions and reverses the order of grades. Paths, cycles, and small weighted graphs show which information is retained in numerical coefficients and which is lost on passing to a spectrum or a projection.

## Place in the library

Primary section: [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

Secondary thematic entries:

- [[en/Resistance Geometry and Duality/Resistance Geometry and Duality|Resistance Geometry and Duality]]: the distinction between coordinate and resistance metrics.

[[en/Getting Started and Foundations/Navigation/Thematic Index#Search by tags|Search by tags]] · [[en/Getting Started and Foundations/Navigation/Thematic Index|Thematic Index]].

## Contents and reading order

| Order | Note | Main question and examples |
| ---: | --- | --- |
| 1 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality\|Diagonal Representation of Polyforms and Duality]] | What is diagonalized, and in which metric? How do exterior exponentials factor, and how are complementary grades reversed? All forms and both metric evaluations on the path $P_3$. |
| 2 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms\|Eigenspaces, Projectors, and Reconstruction of Polyforms]] | How do we account for multiplicities and reconstruct the operator independently of basis choices within eigenspaces? The cycle $C_4$ and a cospectral weighted pair with different forest polynomials and resistances. |
| 3 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles\|Eigenmodes of Paths and Cycles]] | How can eigenvalues, eigenvectors, and projectors be written explicitly for entire families? Examples $P_6$, $C_6$, and $C_5$, with modal contributions to resistances. |
| 4 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle\|Chebyshev Transformations of the Laplacian - From Path to Cycle]] | How does a polynomial in the Laplacian preserve directions while changing the spectrum? The transition from a path to a cycle, folding a doubled cycle, and classification of the Chebyshev orbit. |
| 5 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis\|The Spectral Cone of a Fixed Basis]] | Which coefficient sets in a prescribed basis are realized by graph Laplacians? Sign constraints, the geometry of the cone for $P_3$, and the distinction between the Chebyshev orbit and the full cone. |
| 6 | [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Projection onto a Fixed Spectral Basis and Loss of Information\|Projection onto a Fixed Spectral Basis and Loss of Information]] | What does diagonal or block projection discard, and when is projection onto the graph cone required? A family of different graphs with the same projection, and the failure of projection to commute with inversion. |

The table gives a sequential reading order. For a specific task, a shorter route may be useful:

- **Understand diagonal grades and duality:** [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], followed by grouping repeated modes in [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]].
- **Work with paths and cycles:** [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]], followed by [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]] and [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]].
- **Compare graphs using incomplete data:** the [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms#Cospectral graphs with different forest polynomials|cospectral pair]], followed by [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Projection onto a Fixed Spectral Basis and Loss of Information|Projection onto a Fixed Spectral Basis and Loss of Information]].

## Prerequisites and assumptions

Algebraic prerequisites are [[en/Getting Started and Foundations/Introduction/Basic Objects and Operations of Polyform Algebra|Basic Objects and Operations of Polyform Algebra]], [[en/Getting Started and Foundations/Introduction/Laplacian Exponential|Laplacian Exponential]], and [[en/Resistance Geometry and Duality/Greenian and polyform duality/The Exterior Exponential and Representations of the Greenian|The Exterior Exponential and Representations of the Greenian]]. Duality is introduced in [[en/Resistance Geometry and Duality/Greenian and polyform duality/Laplacian and Greenian - Mutual Duality of Exponentials|Laplacian and Greenian - Mutual Duality of Exponentials]], while ordinary and rooted forest sums are distinguished in [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]] and [[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]]. Current definitions are fixed in [[en/Getting Started and Foundations/Foundations/Core specification|Core Specification]] and [[en/Getting Started and Foundations/Foundations/PMG terminology|Terminology]].

The main model is a finite connected undirected graph without loops on $n\ge2$ vertices, with positive conductances on its existing edges. Set $d=n-1$. Diagonalization takes place on $H=\mathbf1^\perp$ in the auxiliary coordinate inner product $\langle\mathbf v,\mathbf w\rangle_0=\mathbf v^{\mathsf T}\mathbf w$. The resistance inner product of the corresponding affine vectors $v,w\in W$ is $\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf w$; this is a different metric.

Disconnected graphs are treated separately: zero modes remain on $H$, and formulas dividing by the product of all $d$ eigenvalues do not apply. Nonsymmetric balanced-graph Laplacians require a separate treatment.

## Main connections

**From eigendirections to forms.** Let $\mathbf u_\alpha$ be a coordinate-orthonormal eigenbasis of $H$, with $u_\alpha=\sum_i u_{\alpha i}a_i$. Then

$$
\mathbf L\mathbf u_\alpha=\lambda_\alpha\mathbf u_\alpha,\qquad
\mathbf{Gr}\mathbf u_\alpha=\lambda_\alpha^{-1}\mathbf u_\alpha,\qquad
L=\sum_\alpha\ell_\alpha,\qquad
\ell_\alpha=\lambda_\alpha[u_\alpha]^2
$$

Since $\ell_\alpha^2=0$,

$$
M(t)=\exp(tL)=\prod_\alpha(e+t\ell_\alpha),\qquad
M_g=e_g(\ell_1,\ldots,\ell_d)
$$

Here $e_g$ is the elementary symmetric polynomial evaluated in the commutative algebra of forms. This is the exterior exponential; its grades correspond to exterior powers of the operator, not to the matrix exponential. With multiplicities, eigenspaces and projectors are the objects independent of the basis choice.

**Complementary grades and duality.** For the algebraic dual basis $u^\alpha\in W^*$, set $Q_1=\sum_\alpha\lambda_\alpha^{-1}[u^\alpha]^2$ and $D(t)=\exp(tQ_1)$. If $M_g,Q_g$ are the grades of $M(1),D(1)$, then

$$
M_d/Q_g=M_{d-g},\qquad Q_d/M_g=Q_{d-g},\qquad
\Delta=\prod_\alpha\lambda_\alpha=n\tau(G)
$$

The symbol $/$ denotes exterior contraction. Under the centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$, where $h=n^{-1}\sum_i a_i$, we have $\mathcal C(Q_1)=\mathrm{Gr}$ and $N=\mathcal C(D(1))=\exp(\mathrm{Gr})$. The top-grade normalizations are $M_d=\tau T_n$ and $N_d=T_n/(n^2\tau)$, where $T_n=[(a_1\ldots a_n)]^2$. This identification is not the resistance Riesz identification.

The common parameter $t$ merely records the grades of the two original polyforms. When conductances are multiplied by $s>0$, the mutually dual pair is $M(s)$ and $D(s^{-1})$. Details and proofs are given in the [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter and scaling convention]].

**Scalar data and limits of reconstruction.** Eigenvalues with multiplicities determine the rooted coefficients

$$
P_G(t)=\det(I+t\mathbf L)=\sum_{g=0}^d p_g t^g,\qquad
\tau=\frac{p_d}{n},\qquad
\operatorname{Kf}(G)=n\frac{p_{d-1}}{p_d}
$$

Reconstructing the operator itself, the conductances, and individual resistances also requires projectors in vertex coordinates. In the [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms#Cospectral graphs with different forest polynomials|four-vertex example]], the spectrum $0,4,4,8$ and all $p_g$ coincide, but the ordinary forest coefficients $f_2$ are $25$ and $24$, and the resistances $R_{12}$ are $1/4$ and $1/2$.

**Graph realizability and projection.** Positive eigenvalues and zero row sums are insufficient: the reconstructed matrix must satisfy $L_{ij}\le0$ for $i\ne j$. These inequalities define the [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|graph spectral cone]]. Unconstrained diagonal projection may leave this cone. Moreover, projection of the Greenian generally differs from the pseudoinverse of the projected Laplacian; both operations are examined in [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Projection onto a Fixed Spectral Basis and Loss of Information|Projection onto a Fixed Spectral Basis and Loss of Information]].

## Place of the series and continuations

The series forms a general spectral section following [[en/Resistance Geometry and Duality/Greenian and polyform duality/Greenian and Polyform Duality|the Greenian and duality]] and [[en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|matroid parameters and forest characteristics]]. It covers the part of “Spectra of Paths and Cycles” developed here; its place among the other research directions is recorded in the [[en/Getting Started and Foundations/Navigation/Library Map|project map]].

Published continuations are [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]], [[en/Graph Transformations and Gluing/Chains of cores/Chains of Cores|Chains of Cores]], and [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers]]. The first series introduces the full forest passport and separate boundary spectral data; the other two study gluing cores and distinguishing their isomers. Ordinary forest states must be distinguished from characteristic polynomials and their boundary data. The cospectral pair in the present series illustrates limits of reconstruction and does not replace the study of chains.

“Spectra of Bipartite Graphs and Mutual Projections” remains a separate research direction in the [[en/Getting Started and Foundations/Navigation/Library Map|library map]]. Its results are not assumed to have been established in these six notes.

## Programming companion

[[en/PythonExamples/Example - Spectra and Diagonalization in Polyform Algebra#Diagonalizing the path P3|Spectra and Diagonalization in Polyform Algebra]]. [Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/spectral-diagonalization.ipynb).

## Sources and reproducibility

The spectral theorem, spectral projectors, exterior powers, formulas for paths and cycles, Chebyshev polynomials, and orthogonal projections belong to classical theory. Precise references to external work and proofs are given in the relevant notes; the series reconciles these constructions with PMG forms, metrics, and normalizations.

The [series verification folder](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral) contains seven verification scripts and the figure-generation programs. They check independent edge and spectral decompositions, grades and dual contractions, forest coefficients, projectors, resistances, Chebyshev transformations, and projections onto the cone. The six notes contain 22 substantive figures. Finite computational checks confirm examples and do not replace general proofs.
