---
title: Reconstructing Couplings with a Prescribed Neighbor Structure
date: 2026-11-13
updated: 2026-11-13
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-reconstruction-with-neighbor-constraints
lang: en
order: 4
description: "The inverse problem on a spatial grid: admissible coupling changes, criteria for distinguishability and stability, a regularized algorithm, and a model example with 16 electrodes."
---

Surface measurements determine the electrical response of a medium, but do not necessarily determine its internal structure. One additional condition can prescribe the neighbor structure: each point of the computational grid is connected only to its nearest neighbors, while the strengths of these couplings are unknown. Is this restriction sufficient? What further assumptions are needed, and how can they enter an algorithm?

The variation formula in [[Resistance Variations in Graphs and Continuous Media]] maps changes in internal couplings to changes in measurements. Constructing the inverse map requires choosing the admissible changes in the medium. Below, this choice is expressed through parameters, a sensitivity matrix, and a minimization problem. A numerical example shows why a small number of unknowns alone does not ensure reliable reconstruction.

## What must be specified before reconstruction

Consider a finite three-dimensional grid with spacing $h$. Each interior vertex has six neighbors, two along each coordinate axis. Let $E$ be the set of allowed edges and $c_e$ their conductances. All couplings between nonadjacent vertices are identically zero.

Before solving the inverse problem, specify:

- the geometry of the computational domain and electrode positions;
- conditions on the outer surface, including the lateral and bottom boundaries;
- the electrode model and, if needed, contact resistances;
- a background medium $c^0$ at which fields and sensitivity are computed;
- which quantities may change and within what limits.

For soil, a finite grid truncates a continuous half-space. The domain size and the treatment of its exterior must be checked separately. Otherwise, truncation error may be interpreted as heterogeneity.

Let $F(c)$ be the calculated measurements and $y$ the observed values. In the main derivation, the components of $F$ are effective resistances $R_{ab}$ between accessible vertices. Formulas for four-electrode measurements $T_{ab,mn}$ are given below. The pairwise potential coefficients $Z$ of a continuous medium, defined in [[What Electrometry Measures]], require their corresponding forward model: they cannot be substituted for the effective resistances of a finite graph.

## Why the inverse formula for the full matrix is insufficient

If resistances between all graph vertices, including internal vertices, are known, the full Laplacian can be reconstructed. In particular, its differential is related to that of the full resistance matrix:

$$
d\mathbf L=\frac12\mathbf L(d\mathbf R)\mathbf L
$$

If a complete table of effective resistances is known only between electrodes, inversion gives the effective Laplacian on the electrodes, obtained by eliminating internal vertices. Its couplings generally connect distant electrodes as well. They do not coincide with the local grid couplings inside the medium.

It is therefore invalid to reconstruct this Laplacian and then simply set couplings between nonadjacent vertices to zero. That would change the electrical response. The neighbor structure must enter the forward model and the inverse algorithm from the start.

The general problem with variable and fixed couplings is discussed in [[Variations with Conductance Constraints]]. In electrometry, the essential additional feature is that variable couplings lie inside the medium, whereas observed pairs lie on the electrodes.

## The sensitivity matrix of allowed couplings

Let $q$ denote a measured electrode pair, and let $u_q$ be the potentials throughout the background network under unit current through that pair. For an allowed edge $e=(i,j)$, set

$$
S_{qe}=\bigl(u_q(i)-u_q(j)\bigr)^2
$$

The matrix $\mathbf S$ has one row per measurement and one column per variable coupling. In PMG notation, its entry is the squared resistance inner product of the measured pair and the internal edge.

> [!info] Changes in couplings and measurements
> **Proposition.** For a connected network with positive conductances and fixed geometry,
>
> $$
> \boxed{d r=-\mathbf S\,dc}
> \tag{1}
> $$
>
> Here $r=F(c)$ is the set of measured resistances. For a small finite change, the equality becomes the approximation $\Delta r\approx-\mathbf S\Delta c$.

> [!note]- Derivation of the sensitivity formula
> **Proof.** A variation of the coupling $e=(i,j)$ gives $d\mathbf L=dc_e\,\mathbf b_e\mathbf b_e^{\mathsf T}$, where $\mathbf b_e=\mathbf e_i-\mathbf e_j$. The identity $d\mathbf{Gr}=-\mathbf{Gr}(d\mathbf L)\mathbf{Gr}$ implies $dR_q=-dc_e(\mathbf b_e^{\mathsf T}u_q)^2$. Summing over variable edges gives (1). A detailed comparison with continuum fields is given in [[Resistance Variations in Graphs and Continuous Media]]. $\square$

If some allowed couplings are known and remain constant, their columns are omitted. Forbidden couplings never enter the list of unknowns. The neighbor restriction is thus satisfied at every computational step.

For a four-electrode experiment $q=(ab,mn)$, the square is replaced by a product of two potential drops:

$$
S_{qe}=\bigl(u_{ab}(i)-u_{ab}(j)\bigr)
\bigl(u_{mn}(i)-u_{mn}(j)\bigr)
$$

Then $dT=-\mathbf S\,dc$; entries of $\mathbf S$ can now have either sign. All subsequent steps remain applicable. Internal fields are computed in the chosen model of the medium: electrode measurements alone do not provide them.

## Which assumptions reduce uncertainty

The neighbor restriction still leaves many unknowns. A $4\times4\times4$ grid has $64$ vertices and $144$ edges. Even if all $\binom{16}{2}=120$ effective resistances between the top electrodes are known, the sensitivity matrix has size $120\times144$. There are therefore at least $24$ independent directions of coupling change for which the linear approximation gives zero change in all data.

The complete $R$ table is a more favorable starting point. Experiments using four distinct electrodes within this grid yield at most $104$ independent linear combinations, as shown in [[What Electrometry Measures]]. The nullspace describes first-order ambiguity; the set of exact nonlinear solutions requires separate analysis.

Additional assumptions have different meanings:

| Assumption about the medium | How it enters the calculation | Additional specification |
| --- | --- | --- |
| Changes occur only in a known region | Keep only that region's couplings as unknowns | Location of the changing region |
| The medium consists of prescribed layers or blocks | Express couplings through shared parameters | Geometry of the layers or blocks |
| Conductivity is scalar and isotropic | Compute couplings from cell values of $\sigma$ | The rule mapping $\sigma$ to edges |
| Changes are smooth | Penalize differences between neighbors | The preferred degree of smoothing |
| Heterogeneities are few | Use a sparse representation or an $\ell_1$ penalty | A preference for few changes |

The first three rows define an admissible class of media. The last two usually express a preference within that class. A penalty does not make the preferred model the only medium consistent with the measurements.

### From cell conductivity to coupling strengths

Six neighbors do not by themselves imply isotropy. Varying each coupling independently permits different conductivities in different directions. For a scalar conductivity model, the couplings must be tied to a shared set of values $\sigma_i$.

For example, on an orthogonal grid of equal cells, assume piecewise constant conductivity and current passing successively through two half-cells. The conductance between their centers is

$$
c_{ij}=h\,\frac{2\sigma_i\sigma_j}{\sigma_i+\sigma_j}
$$

The factor $h$ is the ratio of face area $h^2$ to distance $h$. The harmonic mean follows by adding the resistances of the two half-cells. This is one specific discretization; other geometries or electrode models may require a different rule.

Denote independent parameters by $\theta$ and write $c=c(\theta)$. They may be layer conductivities, cell values, or coefficients of prescribed spatial functions. Below, $F(\theta)$ means $F(c(\theta))$. Introduce the matrices

$$
\mathbf H=\frac{\partial c}{\partial\theta},
\qquad
\boxed{\mathbf A=\frac{\partial F}{\partial\theta}=-\mathbf S\mathbf H}
\tag{2}
$$

The matrix $\mathbf H$ expresses assumptions about the medium; $\mathbf S$ expresses electrical sensitivity. Their product shows which changes in the chosen parameters the measurements distinguish. For example, four prescribed horizontal layers express all $144$ couplings through four conductivities. This reduces the number of unknowns, but it remains necessary to check whether measurements distinguish these four parameters.

## Uniqueness and stability

If different admissible changes in the medium produce identical measurement changes, they cannot be distinguished. The sensitivity matrix tests this to first order.

Suppose there are $p$ independent parameters, the background value is in the interior of the admissible set, and the forward model is smooth.

> [!info] Criterion for first-order distinguishability
> **Proposition.** Parameter changes are uniquely determined by their first-order response if and only if
>
> $$
> \ker\mathbf A=\{0\},
> \qquad \operatorname{rank}\mathbf A=p
> $$
>
> For an arbitrary linear space $U$ of admissible coupling changes, the same criterion reads $\ker\mathbf S\cap U=\{0\}$. Full column rank of $\mathbf A$ is also sufficient for local uniqueness of nonlinear reconstruction near the background medium.

> [!note]- Proof of the criterion
> **Proof.** Two changes have the same first-order response if and only if their difference belongs to the nullspace of the sensitivity matrix. For the nonlinear statement, choose $p$ rows of $\mathbf A$ forming a nonsingular square matrix. The corresponding $p$ components of $F$ have a local inverse by the inverse function theorem. Thus the full set of measurements also distinguishes parameters locally. $\square$

The Jacobian nullspace as a criterion for solvability of the linearized problem is discussed by **Boyer, Garzella, and Guevara Vasquez [1, §5.2, Lemma 5.4 and the following text]**. Here this standard criterion is applied to the chosen parameterization and available measurements. It does not imply global uniqueness. With deficient rank, changes may still be distinguished at higher orders, but stable linear inversion is unavailable.

### A weak response can be lost in measurement errors

If a substantial change in the medium produces a response smaller than instrument error, reconstruction will be unreliable even when uniqueness formally holds. The size of the response matters as well as its being nonzero.

First express parameters in specified physical scales. For independent errors, divide each data discrepancy by the standard deviation $s_q$ of that measurement. Less reliable values then receive lower weight. In matrix notation, $\mathbf W$ is diagonal with $W_{qq}=1/s_q^2$. For correlated errors, use the inverse of the positive-definite covariance matrix. With parameters already scaled, analyze

$$
\widetilde{\mathbf A}=\mathbf W^{1/2}\mathbf A
$$

If its smallest singular value is $\gamma>0$, a data error of linear norm at most $\varepsilon$ after this scaling can produce a linearized parameter error of up to $\varepsilon/\gamma$. A small positive $\gamma$ means poor stability despite the absence of exact linear ambiguity.

These are modes of **sensitivity to parameters of the medium**. The resistance-matrix spectrum discussed in [[Properties of Resistances in a Continuous Medium]] answers a different question. A small number of prominent modes in the resistance matrix does not establish that the same number of medium parameters can be reconstructed reliably.

> [!info] Practical meaning of approximate uniqueness
> **Definition.** For a model class $\Theta$ and tolerance $\varepsilon$, consider the set
>
> $$
> \mathcal C_\varepsilon=
> \{\theta\in\Theta:\|\mathbf W^{1/2}(F(\theta)-y)\|_2\le\varepsilon\}
> $$
>
> Reconstruction is unique to accuracy $\delta$ if this set is nonempty and any two of its elements differ by at most $\delta$ in a specified linear norm of the parameters.

This criterion concerns the entire admissible class. Singular values provide a local estimate, but do not rule out distant alternative solutions. Active parameter constraints further restrict admissible directions; this must be considered separately from checking the full Jacobian.

## Reconstruction algorithm

The residual is the discrepancy between calculated and observed values: $F(\theta)-y$. The algorithm reduces this discrepancy while respecting the chosen constraints. It can also favor models close to a reference background or varying smoothly in space.

Introduce reference parameters $\theta_{\mathrm{ref}}$ and a linear operator $\mathbf Q$. With $\mathbf Q=\mathbf I$, the penalty keeps the solution near the reference medium. If rows of $\mathbf Q$ compute differences between neighboring parameters, the penalty smooths deviations from that medium.

The first term measures agreement with the data; the second measures departure from the chosen preference:

$$
\boxed{
\min_{\theta\in\Theta}\Phi(\theta),\qquad
\Phi(\theta)=\frac12\|\mathbf W^{1/2}(F(\theta)-y)\|_2^2+
\frac\lambda2\|\mathbf Q(\theta-\theta_{\mathrm{ref}})\|_2^2
}
\tag{3}
$$

The parameter $\lambda\ge0$ sets the strength of that preference. The constraints $\Theta$ may include positivity, admissible intervals, and known values. Fixed parameters are most conveniently removed from the unknowns.

The computational sequence is as follows.

1. **Set the initial medium.** Choose $\theta$, construct only allowed couplings $c(\theta)$, and assemble the Laplacian. A positive lower bound on conductances preserves connectedness on a connected grid.
2. **Solve the forward problems.** Compute potentials and predicted measurements $F(\theta)$ for the current experiments. Fixing one vertex potential to zero removes the arbitrary additive constant.
3. **Compute sensitivity.** Assemble $\mathbf S$, then $\mathbf A=-\mathbf S\mathbf H$. Examine small singular values with measurement errors taken into account.
4. **Find an admissible step.** Linearize $F$ and solve a least-squares problem with the same constraints and penalty.
5. **Check the step in the nonlinear model.** Recompute measurements. If the objective decrease does not agree with the prediction, shorten the step or reduce the region in which the linearization is used. Update sensitivity after accepting the step.
6. **Assess the result.** Compare the residual with the error level and examine parameter changes, the effect of the starting medium, and regularization. A small residual alone does not mean that the internal structure has been recovered.

> [!note]- Computing one step
> At the current residual $f=F(\theta)-y$, one possible step $d$ is defined by
>
> $$
> \min_{\theta+d\in\Theta}
> \left\{
> \frac12\|\mathbf W^{1/2}(f+\mathbf A d)\|_2^2+
> \frac\lambda2\|\mathbf Q(\theta+d-\theta_{\mathrm{ref}})\|_2^2+
> \frac\mu2\|d\|_2^2
> \right\}
> $$
>
> Here $\mu\ge0$ limits step size; it is a numerical parameter distinct from the preference for a medium specified by $\lambda$. Interval constraints give a convex feasible set for the step. For $\mu>0$, the quadratic problem has a unique solution. For $\mu=0$ and $\lambda>0$, strict convexity is equivalent to $\ker\mathbf A\cap\ker\mathbf Q=\{0\}$. These statements follow from positivity of the quadratic part and concern the step, not the global minimum of nonlinear problem (3).

The general procedure corresponds to [[An Algorithm for Variations with Conductance Constraints]].

Choose penalty strength using error estimates and stability checks, rather than a desired image of the medium. When the model is consistent with the data, there is no reason to drive the residual far below the noise level. A persistently excessive residual also calls for reconsidering geometry, electrodes, and the model class itself.

## A model example with sixteen electrodes

Take a finite $4\times4\times4$ network with spacing $h=1$. Electrodes occupy all $16$ vertices of the top level. There are no couplings outside the network: lateral and bottom surfaces are insulating. This is a specifically defined network, not a numerical approximation of an infinite half-space with verified truncation accuracy.

Assign one conductivity $\theta_k$ to each of the four levels. Horizontal couplings equal $\theta_k$; vertical couplings equal the harmonic mean of adjacent level conductivities. The background is $(1,1,1,1)$, and the prescribed test medium is

$$
\theta_*=(1;\ 1.15;\ 0.85;\ 1.10)
$$

![[images/Medium model on a grid.svg]]

*The model network: 64 vertices, 144 allowed couplings, and 16 electrodes on the top face. In the layered description, all coupling strengths are expressed through four parameters.*

This computational experiment has access to the complete table of $120$ effective resistances $R$ between top vertices. It is calculated from the model; it is neither $120$ independent combinations of four-electrode readings $T$ nor the field estimates of $Z$ in [[Properties of Resistances in a Continuous Medium]].

An independent normal error with standard deviation $0.001R_q^0$ is added to each calculated value, where $R_q^0$ is the resistance of the homogeneous background. All scenarios use the same noise realization, with random seed `1304`. Conductivity bounds are $0.5\le\theta_k\le1.5$.

### Exact data are recovered; noise substantially changes the answer

The layered assumption has already achieved a specific reduction: $144$ free couplings have become four unknown parameters. For exact data, the algorithm starting from a homogeneous state recovered them with maximum absolute error below $10^{-7}$.

Next, test the stability of this result. Three formulations are compared for noisy data:

- free reconstruction of four parameters with $\lambda=0$;
- reconstruction of three parameters with the bottom-layer value $\theta_4=1.10$ **specified independently**;
- reconstruction of four parameters with a penalty toward the homogeneous background: $\mathbf Q=\mathbf I$, $\lambda=1$ in (3), and $W_{qq}=(0.001R_q^0)^{-2}$.

The second case uses additional knowledge of the bottom layer. In the third, $\lambda=1$ is chosen to illustrate the penalty's effect; no optimality is claimed.

| Case | $\theta_1$ | $\theta_2$ | $\theta_3$ | $\theta_4$ | Residual, % |
| --- | ---: | ---: | ---: | ---: | ---: |
| Prescribed medium, exact data | 1.0000 | 1.1500 | 0.8500 | 1.1000 | 0 |
| Reconstruction from exact data | 1.0000 | 1.1500 | 0.8500 | 1.1000 | below $10^{-10}$ |
| Noise, four unknowns | 1.0003 | 1.1462 | 0.7978 | 1.5000 | 0.09828 |
| Noise, known bottom layer | 1.0016 | 1.1278 | 0.9256 | 1.1000 | 0.09845 |
| Noise, penalty toward background | 1.0008 | 1.1402 | 0.8364 | 1.3615 | 0.09832 |

The residual is calculated relative to the data used in each row:

$$
100\sqrt{\frac1{120}\sum_q
\left(\frac{F_q(\theta)-y_q}{R_q^0}\right)^2}
$$

The root-mean-square added noise under the same normalization is $0.10067\%$. In the case with four unknowns, the bottom layer reaches the upper bound $1.5$. The bound stops the parameter from changing further, but does not confirm its physical correctness.

![[images/Layer reconstruction under different assumptions.svg]]

*One noisy dataset and three different assumptions. All results have similar residuals. Knowing the bottom layer reduces uncertainty, but errors in other layers remain. The chosen penalty also does not eliminate the bottom-layer error.*

### Sensitivity explains the result

At the homogeneous background, the singular values of the relative sensitivity matrix $\operatorname{diag}(1/R_q^0)\mathbf A$ are approximately

$$
8.9362;\quad 0.45043;\quad 0.022028;\quad 0.00098330
$$

All four are positive, but the ratio of largest to smallest is about $9088$. Scaling by noise standard deviations multiplies all values by another factor of $1000$, leaving their ratio unchanged. For three unknowns with the bottom layer fixed at $\theta_4=1.10$, the ratio is about $446$: here sensitivity is computed at the initial medium $(1;1;1;1.10)$ with the same data weights.

Independent knowledge of the bottom layer thus substantially improves conditioning. Errors in the remaining parameters nevertheless persist, as the table shows.

The four parameters are locally distinguishable in the exact model, yet some combinations produce a very weak surface response. Deep-layer conductivities can largely compensate for one another. The count $120$ alone does not characterize the quality of reconstruction of four unknowns.

> [!example] What the computation establishes
> For this network and this noise realization, different conductivity sets describe the measurements with almost identical residuals. A known layer value and a penalty change the selected answer, but do not make the remaining parameters exact. This demonstrates sensitivity to assumptions; it is not a statistical error assessment of a field method.

Analytical derivatives were separately checked against central finite differences of forward calculations: the maximum absolute discrepancy is below $10^{-8}$ for both the four parameters and all $144$ individual couplings. Data generation and reconstruction use the same forward model. The experiment therefore does not test discretization error, electrode error, or mismatch between real soil and the chosen layers.

## Choosing measurements after choosing the model

The minimum-measurement question becomes definite once the medium parameters and admissible reconstruction error are specified. For a chosen experiment set $M$, take the corresponding Jacobian rows $\mathbf A_M$ and their error covariance.

Regular first-order reconstruction of $p$ free parameters requires at least $p$ independent scalar data. This is not sufficient: rows may have nearly identical sensitivities. With independent errors, adding informative experiments increases $\mathbf A_M^{\mathsf T}\mathbf W_M\mathbf A_M$, but need not substantially improve its weakest direction.

A practical procedure is to choose an initial experiment set, compute its sensitivity, and add available measurements that better distinguish weakly observed parameter changes. One criterion is increasing the smallest singular value after consistent scaling. The check should be repeated for several admissible media, since sensitivity depends on the medium itself.

There is therefore no universal answer such as a fixed number of measurements being sufficient for five modes. The parameters or combinations to be recovered, and the required accuracy, must be specified. Preserving the spectral representation of the observed matrix and reconstructing internal couplings are related but different requirements.

## Status and further checks

The connection to PMG lies in expressing sensitivity through squared inner products and explicitly restricting admissible coupling changes. The algorithm uses established methods of regularized nonlinear fitting.

The distinguishability criterion is proved to first order; full rank is sufficient for local nonlinear uniqueness. The model experiment shows how constraints affect the result and its stability. Global uniqueness and accuracy for real soil require separate verification.

Practical continuation requires error estimates for real measurements, a consistent electrode model, and tests of several physically admissible descriptions of the medium. The result should include both a fitted conductivity and a description of changes that the data still cannot distinguish.

## Reproducibility

The accompanying calculation uses `scipy.optimize.least_squares` with method `trf`, an analytical Jacobian, and interval bounds. The penalty is added as extra residual components. The method controls the region allowed for a step and seeks a local minimum [2]; this does not certify global optimality.

- [Model experiment program](<data/Reconstruction on a grid.py>) generates data, solves four reconstruction problems, checks derivatives, and plots the figures. Requires Python 3, NumPy, SciPy, and Matplotlib.
- [Model measurements](<data/Model measurements.csv>) contain electrode-pair coordinates, background, exact, and noisy resistances, and error standard deviations. Electrodes are labeled `a` through `p`.
- [Reconstruction results](<data/Reconstruction results.json>) contain parameters, residuals, singular values, verification results, and computational library versions.

These files concern the synthetic example. The real measurements examined in [[Properties of Resistances in a Continuous Medium]] are not used in this calculation.

## Sources

1. Boyer J., Garzella J. J., Guevara Vasquez F. *On the Solvability of the Discrete Conductivity and Schrödinger Inverse Problems*. SIAM Journal on Applied Mathematics, 2016, 76(3), 1053-1075. [DOI: 10.1137/15M1043479](https://doi.org/10.1137/15M1043479). [Open preprint](https://www2.math.utah.edu/~fguevara/pubs/Boyer_2015_SDC.pdf), §5.2-5.3: linear sensitivity, the Jacobian-nullspace criterion, and iterative reconstruction.
2. SciPy. [`scipy.optimize.least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html): constrained nonlinear least squares, method `trf`, and the analytical Jacobian.
