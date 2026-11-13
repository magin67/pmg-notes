---
title: Properties of Resistances in a Continuous Medium
date: 2026-11-13
updated: 2026-11-13
revision: 2
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-continuous-medium-and-measurement-information
lang: en
order: 2
description: "Pairwise measurements on an electrode grid: a homogeneous medium, hidden geometry, spectral components, and measurement error. Formulating the choice of a sufficient measurement set."
---

A square survey area contains 16 electrodes, four in each row. A pairwise characteristic of the medium can be obtained for each pair, giving 120 values. Could fewer measurements suffice to recover the rest? The answer depends on what is known about the medium and on the required accuracy.

[[What Electrometry Measures]] distinguishes a graph resistance $R_{ij}$ from a pairwise potential coefficient $Z_{ij}$ of a continuous medium. This note concerns $Z_{ij}$: the potential at one surface point due to a unit current source at another, with current return and zero reference potential at infinity. A four-electrode array with two remote electrodes can approximately isolate this coefficient. The conditions and errors of that transition are described in the linked note.

The starting model is a homogeneous isotropic half-space with a flat surface and point electrodes, using exact values. Deviations from this model and measurement errors are then considered. The aim is to establish properties of the pairwise table and formulate the problem of reducing measurements.

## The electrode grid and its pairwise table

Choose $N$ distinct surface points. The medium is linear and reciprocal, so $Z_{ij}=Z_{ji}$. The number of unordered pairs is

$$
M=\binom N2=\frac{N(N-1)}2
$$

For $N=16$, this gives $M=120$. These are potential coefficients $Z$ estimated using remote electrodes and conditions on their distant contributions. The number $104$ in [[What Electrometry Measures]] concerns a different problem: independent combinations $T$ on four distinct electrodes within the grid itself.

Each of the $120$ values of $Z$ belongs to a different pair. Their independence depends on the chosen model of the medium.

The values form a symmetric matrix $\mathbf Z$. Its diagonal is not measured. Where a complete square matrix is needed to discuss rank, the convention $Z_{ii}=0$ is used below. This does not assert that a point source has zero self-potential: in this idealization its self-potential is singular.

Two questions must be kept separate. Matrix rank measures linear independence of rows or columns. The number of independent model parameters measures how freely the whole table can vary. A matrix can be nonsingular even when all its entries are determined by one unknown number.

## A homogeneous medium

In a homogeneous isotropic half-space, the pairwise coefficient is

$$
Z_{ij}=\frac{\kappa}{d_{ij}},\qquad
\kappa=\frac{\rho}{2\pi},\qquad i\ne j
$$

Here $d_{ij}$ is the ordinary electrode separation and $\rho$ is the resistivity of the medium. The physical meaning and connection with measured voltage are explained in [[What Electrometry Measures#A pairwise characteristic of a continuous medium|the section on the pairwise coefficient]].

If the electrode coordinates are known, only $\kappa$ remains unknown. One exact measurement determines it as $\kappa=Z_{ij}d_{ij}$, after which every other value can be calculated.

For example, let a square grid have spacing $h$ and nearest-neighbor coefficient $z=\kappa/h$. The coefficients at separations $\sqrt2h$ and $2h$ must then be $z/\sqrt2$ and $z/2$. These are consequences of one model, not additional independent parameters.

> [!info] Measurement count and parameter count
> **Proposition.** With known distances and a known homogeneous isotropic half-space, the entire pairwise table depends on one coefficient $\kappa$. More electrodes produce more pairs but do not increase the number of model parameters.

The remaining measurements are still useful in practice. They allow errors to be averaged and the homogeneity assumption to be checked. In particular, the products $Z_{ij}d_{ij}$ should agree within the permitted error. Systematic disagreement calls for checking both the medium model and the measurement array.

## Geometry hidden in the measurements

Recovering a grid whose coordinates are already known provides a check: how well does the pairwise table agree with the geometry of a homogeneous medium? The law $Z_{ij}=\kappa/d_{ij}$ gives distances up to one unknown scale. A configuration can be reconstructed from them and compared with the actual grid.

The calculation has three steps: transform $Z$ entrywise into squared distances, pass to vectors from the survey center, and spectrally decompose their Gram matrix. For positive $Z_{ij}$, define the first matrix as follows.

> [!info] Entrywise transformation
> **Definition.** Set
>
> $$
> D_{ij}=\frac1{Z_{ij}^{2}}\quad(i\ne j),\qquad D_{ii}=0
> $$
>
> Taking reciprocals and squaring are performed separately for each off-diagonal entry. This is neither matrix inversion nor the square of an inverse matrix.

In the homogeneous model,

$$
D_{ij}=\frac{d_{ij}^{2}}{\kappa^{2}}
$$

Thus $\mathbf D$ is a squared-distance matrix with a common scale factor. Its rank need not equal the dimension of the plane. Rank 2 appears after passing to inner products of vectors from the survey center.

This transition uses the [[Laplacian, Green Matrix, and Effective Resistance Matrix#The centering matrix|centering matrix]]:

$$
\mathbf J=\mathbf I-\frac1N\mathbf1\mathbf1^{\mathsf T}
$$

Here $\mathbf I$ is the identity and $\mathbf1$ contains $N$ ones. Multiplication by $\mathbf J$ subtracts the mean from each entry. Define

$$
\boxed{\mathbf G_d=-\frac12\mathbf J\mathbf D\mathbf J}
\tag{1}
$$

The subscript $d$ indicates transformed distance data. In the homogeneous model, $\mathbf G_d$ is the Gram matrix of the centered geometric configuration. It is not the Green matrix of the original conducting medium.

> [!info] Dimension of the geometric representation
> **Proposition.** For points on a plane in the homogeneous model, $\mathbf G_d$ is positive semidefinite and has rank at most 2. Its rank is 2 if the points are not collinear. The rank of $\mathbf D$ is at most 4.

This applies known properties of squared Euclidean distance matrices; see **Dokmanić et al. (2015), Theorem 1 and Algorithm 1**, in their [survey on distance matrices](https://arxiv.org/abs/1502.07541). A short derivation in the present notation follows.

> [!note]- Why centering leaves two modes
> **Proof.** Let $\mathbf x_i\in\mathbb R^2$ be the electrode coordinates and $\overline{\mathbf x}$ their mean. Introduce scaled, centered vectors
>
> $$
> \mathbf y_i=\frac{\mathbf x_i-\overline{\mathbf x}}{\kappa},\qquad
> \sum_i\mathbf y_i=0
> $$
>
> Let the rows of $\mathbf Y$ be $\mathbf y_i^{\mathsf T}$. The Gram matrix $\mathbf H=\mathbf Y\mathbf Y^{\mathsf T}$ is positive semidefinite, with rank equal to the dimension of the span of the vectors $\mathbf y_i$. For noncollinear points this dimension is 2.
>
> Let $\mathbf q$ contain the diagonal entries of $\mathbf H$. Expanding the squared distance gives
>
> $$
> D_{ij}=\|\mathbf y_i-\mathbf y_j\|^2
> =H_{ii}+H_{jj}-2H_{ij}
> $$
>
> $$
> \mathbf D=\mathbf q\mathbf1^{\mathsf T}+\mathbf1\mathbf q^{\mathsf T}-2\mathbf H
> $$
>
> Each of the first two terms has rank at most 1, so $\operatorname{rank}\mathbf D\le4$. Multiplication by $\mathbf J$ on both sides removes them. Since $\mathbf J\mathbf Y=\mathbf Y$, it follows that $\mathbf G_d=\mathbf H$. $\square$

Recovering geometry requires both the two nonzero eigenvalues and their eigenvectors. If $\lambda_1,\lambda_2>0$ and $u_1,u_2$ are normalized eigenvectors of $\mathbf G_d$, coordinates can be written as

$$
\mathbf y_i=\bigl(\sqrt{\lambda_1}\,u_{1i},\ \sqrt{\lambda_2}\,u_{2i}\bigr)
$$

This standard reconstruction from distances is called classical multidimensional scaling. Pairwise distances determine neither translation nor rotation or reflection. If $\kappa$ is unknown, the physical scale is also undetermined. When the two eigenvalues coincide, individual eigenvectors can be chosen differently, but the resulting configurations differ only by an orthogonal transformation.

There are two different counts here. With known coordinates, one coefficient $\kappa$ determines the homogeneous table. Two geometric modes arise because the electrodes lie in a plane. Each mode includes eigenvector values at all electrodes; these must also be recovered when the configuration is unknown. Two modes therefore do not imply that two measurements suffice.

## What heterogeneity changes

In a heterogeneous medium, electrode separation alone generally does not determine $Z_{ij}$. Two pairs with the same separation may lie above different regions and produce different values. The average decay law with distance may also change. For example, equal values at equal separations do not establish homogeneity with depth.

The entrywise transformation and centering can still be computed, but $\mathbf D$ need not represent squared Euclidean distances. Additional nonzero eigenvalues may appear in $\mathbf G_d$, including negative ones. A negative eigenvalue here indicates a failure of the transformed data to have a Euclidean representation; it does not mean negative ground conductivity.

For any symmetric zero-diagonal $\mathbf D$, double centering retains the inverse relation:

$$
D_{ij}=(G_d)_{ii}+(G_d)_{jj}-2(G_d)_{ij}
$$

Using the full spectral representation of $\mathbf G_d$, this becomes

$$
D_{ij}=\sum_\alpha\lambda_\alpha(u_{\alpha i}-u_{\alpha j})^2,
\qquad Z_{ij}=\frac1{\sqrt{D_{ij}}}\quad(i\ne j)
$$

The sum includes every nonzero mode with its sign; the eigenvectors are orthonormal in the ordinary coordinate inner product. If some modes are discarded, $D_{ij}>0$ must be checked again for every distinct pair, or recovery of positive $Z_{ij}$ is impossible. Eigenvalues alone do not determine the matrix: the eigendirections are also needed. This distinction is recorded in [[PMG terminology#Spectral representations and projections|the terminology of spectral representations]].

> [!example] Geometry of an actual survey area
> For a $4\times4$ patch from the author's measurements, $\mathbf D$ and $\mathbf G_d$ were constructed and the two largest positive eigenvalues and their eigenvectors retained. The recovered configuration was aligned with the original grid by translation, an orthogonal transformation, and one common scale. The root-mean-square position error was about $0.23$ grid spacings.

![[images/Grid from two principal modes.svg]]

*Blue points and lines show the original grid. Red crosses and lines show the configuration from two principal modes. Numbers identify electrodes. Position and common scale are aligned, but no arbitrary affine correction of shape is applied. The distortions show that the two principal modes themselves contain departures from the ideal homogeneous model.*

The [120 original pairs and electrode coordinates used in the figure](<data/Measurements on a 4 by 4 patch.csv>) are attached. Coordinates are in grid spacings, and $Z$ retains the units of the original records. The source file called these values $R$; the column has been renamed to match this series. They are treated as experimental estimates of potential coefficients, without assuming that finite remote-distance errors or instrument errors have been removed.

The example recovers recognizable geometry but does not establish an exact separation into “geometry in two modes and medium properties in the others.” Both medium properties and measurement errors can affect every mode. How many additional modes are needed for a chosen accuracy requires a separate check.

## Errors when taking reciprocals

Suppose the measured value is $Z_{ij}+\delta Z_{ij}$, with $|\delta Z_{ij}|\ll Z_{ij}$. Linearizing the transformation gives

$$
\delta D_{ij}\approx-\frac{2\,\delta Z_{ij}}{Z_{ij}^{3}},\qquad
\frac{\delta D_{ij}}{D_{ij}}\approx-2\frac{\delta Z_{ij}}{Z_{ij}}
$$

With approximately constant absolute error, smaller $Z_{ij}$ values have larger relative errors. Such values usually occur at larger separations. After reciprocation, distant pairs may substantially affect weak spectral components.

If the original relative error is constant instead, the relative error of $D_{ij}$ is only doubled to first order. Further growth with distance does not follow from the reciprocal transformation alone. Spectral analysis therefore needs an error model for the original measurements.

Errors need not be random. Inaccurate array geometry, finite remote-electrode positions, and common offsets can create coordinated deviations across several pairs. Averaging does not necessarily remove their cause.

Two qualifications follow. A nonzero eigenvalue does not establish a separate heterogeneity. A small eigenvalue does not establish that its mode is irrelevant: after transforming back, it may appreciably change some $Z_{ij}$.

## Choosing a sufficient measurement set

In the homogeneous model with known geometry, one exact pair value determines the common coefficient. For an arbitrary symmetric table, symmetry alone cannot recover a missing entry. Between these cases lie models with additional constraints on the medium or the structure of the pairwise data.

> [!info] Research problem
> For a given electrode grid, choose pairwise measurements that allow the complete table to be recovered to a specified accuracy under stated assumptions about the medium and measurement errors.

To make the problem definite, specify:

- **What is recovered:** the full table, its change from a known background, or selected medium parameters.
- **Which models are admissible:** which medium properties are known and which remain unknown.
- **How error is assessed:** in the original pair values, the transformed matrix, or the medium parameters. These criteria are not equivalent.
- **How measurement errors are handled:** which values and combinations can be considered reliable.

Two questions then arise: how many pairs to measure and which pairs to choose. Count alone is insufficient. Measurements may duplicate similar information or complement one another, and close eigenvalues of two matrices do not guarantee close entries.

Possible approaches include reference electrodes, combinations of separations and directions, selection by sensitivity to medium parameters, and sequential addition of measurements. Sufficiency must be tested within the chosen model. A limit on the number of modes does not by itself specify an array or a universal minimum measurement count.

A complete experimental data set can test a proposed scheme: hide some values, reconstruct using only the retained measurements, and compare with the hidden values. This checks reproduction of the data. Without an independent error estimate, it does not establish accuracy in recovering the true state of the medium.

The homogeneous model explains why a large pairwise table may have a simple description. Heterogeneity and errors complicate it. The relation between changes in pairwise characteristics and changes in the medium is derived in [[Resistance Variations in Graphs and Continuous Media]]. [[Reconstructing Couplings with a Prescribed Neighbor Structure]] uses this sensitivity to assess parameter identifiability and discuss measurement selection. A specific minimum set for real ground remains an open problem.

## Programming example

A calculation with `polyform_algebra` is provided in [[en/PythonExamples/Example - Electrometry#Geometry from real pairwise data|the Electrometry example]]. It is part of the series notebook with input data and checks.

## Sources and connections

- [[What Electrometry Measures]] - definitions of $T$, $R$, and $Z$, remote electrodes, and limits of the transition to potential coefficients.
- [[Laplacian, Green Matrix, and Effective Resistance Matrix]] - the distance operator and double centering, with conditions for applying them to a graph resistance matrix.
- [[PMG terminology#Spectral representations and projections|Spectral terminology]] - eigenmodes, eigenspaces, and full spectral representations.
- Dokmanić I., Parhizkar R., Ranieri J., Vetterli M. **Euclidean Distance Matrices: Essential Theory, Algorithms, and Applications.** *IEEE Signal Processing Magazine*, 32(6), 2015, 12-30. [DOI](https://doi.org/10.1109/MSP.2015.2398954), [open version](https://arxiv.org/abs/1502.07541). Theorem 1: the rank of a squared-distance matrix; Algorithm 1: coordinate recovery by double centering and spectral decomposition.

The geometric transformations are known results from distance-matrix theory. The figure uses the author's measurements. Choosing a sufficient measurement set is posed as an open problem with several possible refinements.
