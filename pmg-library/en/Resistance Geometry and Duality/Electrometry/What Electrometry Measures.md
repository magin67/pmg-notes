---
title: What Electrometry Measures
date: 2026-11-13
updated: 2026-11-13
revision: 2
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-measurements-and-pairwise-data
lang: en
order: 1
description: "Four-electrode measurements as inner products. Ambiguity of pairwise resistance recovery, remote electrodes, the compensation triangle, and error over a finite survey area."
---

In electrometry, current is passed through two electrodes while voltage is measured between two others. Repeating the experiment at different electrode positions provides data about a conducting medium. The inverse problem is to recover its internal state from these surface measurements.

Before solving the inverse problem, it is necessary to establish what has actually been measured. One experiment gives the response of one electrode pair to current through another. In the resistance geometry of a graph, this is the inner product of two vectors. Pairwise resistances are related to these responses, but recovering them requires additional conditions.

The series uses three quantities with the dimensions of resistance. Their distinction matters from the outset:

| Symbol | Meaning |
| --- | --- |
| $T$ | Voltage between the sensing electrodes divided by the current through the source pair |
| $R$ | Effective resistance between two network terminals |
| $Z$ | Potential due to a unit source, with current return and zero reference potential at infinity |

The instrument directly supplies $T$. Its relation to $R$ in a network model and to $Z$ in a continuous medium is established below.

The measurements are stationary and the medium is linear and reciprocal. The finite network model is connected and has nonnegative conductances. The voltmeter is ideal: no current flows through its inputs. The four electrodes in the measurements considered here are pairwise distinct. Sections using ordinary distances additionally assume a homogeneous isotropic half-space with a flat surface and point electrodes.

## Four electrodes and one measurement

Let current $I>0$ enter the medium through electrode $a$ and leave through $b$. Electrodes $m,n$ measure the potential difference. Their reading depends on the conductivity throughout the medium and on the positions of all four electrodes.

![[images/Four-electrode measurement.svg]]

*Current pair $a,b$ and sensing pair $m,n$. The source and voltmeter are schematic; $\sigma(x)$ is the conductivity of the medium at $x$.*

> [!info] Transfer resistance
> **Definition.** For the stated current direction, set
>
> $$
> T_{ab,mn}=\frac{\varphi_m-\varphi_n}{I}
> $$
>
> Here $\varphi_m,\varphi_n$ are the electrode potentials. The quantity $T_{ab,mn}$ has the dimensions of resistance and is called the transfer resistance.

Dividing by the actual current allows experiments with different currents to be compared. Exchanging $m,n$ reverses the sign of $T$. A negative value means that the measured voltage has the opposite sign for the chosen current direction.

In the finite network model, write $\mathbf L$ for the Laplacian and $\mathbf{Gr}=\mathbf L^+$ for the Green matrix. Let $\mathbf e_i$ have value one at $i$ and zero elsewhere. Then

$$
\mathbf L\boldsymbol\varphi=I(\mathbf e_a-\mathbf e_b)
$$

Solving with the Green matrix gives

$$
T_{ab,mn}=(\mathbf e_m-\mathbf e_n)^{\mathsf T}\mathbf{Gr}(\mathbf e_a-\mathbf e_b)
$$

Under the convention $(ab)=b-a$, $(mn)=n-m$, both differences in the last formula have signs opposite to the coordinates of these vectors. The two signs cancel, so

$$
T_{ab,mn}=(ab)\cdot(mn)
$$

This is the resistance inner product, not the inner product of electrode directions in ordinary physical space. The correspondence is explained in [[Inner Product of Graph Vectors]].

## Six resistances and two independent responses

In a finite network, $R_{ij}$ denotes the effective resistance between terminals $i,j$. It depends on the whole network, including its internal nodes. The polarization identity in [[Inner Product of Graph Vectors#The four-resistance formula|the note on inner products]] gives

> [!info] The four-resistance formula
> **Proposition.** With the chosen measurement orientation,
>
> $$
> \boxed{T_{ab,mn}=\frac{R_{an}+R_{bm}-R_{am}-R_{bn}}2}
> \tag{1}
> $$

The formula is exact for a linear symmetric resistive network; its edge conductances need not be equal.

> [!note]- Derivation through the Green matrix
> **Proof.** Use $R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}$. The diagonal terms on the right of (1) cancel, leaving
>
> $$
> \frac{R_{an}+R_{bm}-R_{am}-R_{bn}}2
> =\mathrm{Gr}_{am}-\mathrm{Gr}_{bm}-\mathrm{Gr}_{an}+\mathrm{Gr}_{bn}
> $$
>
> This is the transfer resistance obtained above. $\square$

Four points have six pairwise values:

$$
R_{ab},\ R_{am},\ R_{an},\ R_{bm},\ R_{bn},\ R_{mn}
$$

There are three ways to partition the points into two disjoint pairs. By reciprocity and sign reversal when a pair is reversed, all experiments reduce to three quantities:

$$
T_{ab,mn},\qquad T_{am,bn},\qquad T_{an,bm}
$$

They satisfy the four-point identity:

$$
T_{ab,mn}-T_{am,bn}+T_{an,bm}=0
$$

Thus there are only two independent linear data values. The third experiment can check measurement consistency but adds no third independent combination of resistances. Six unknown pairwise values cannot be recovered from two numbers without additional conditions.

## Why a larger grid does not remove the ambiguity

It might seem that adding electrodes would supply the missing information. However, all four-point measurements are insensitive to certain changes of the pairwise table.

Assign an arbitrary number $\varepsilon_i$ to each electrode $i$. Change only the values for distinct pairs:

$$
R'_{ij}=R_{ij}+\varepsilon_i+\varepsilon_j\quad(i\ne j),
\qquad R'_{ii}=0
$$

The added terms cancel in every measurement:

$$
2(T'_{ab,mn}-T_{ab,mn})=(\varepsilon_n-\varepsilon_m)+(\varepsilon_m-\varepsilon_n)=0
$$

Even adding the same constant to all off-diagonal $R_{ij}$ goes undetected. The more general transformation above has one free parameter per electrode.

> [!info] Ambiguity of four-point data
> **Theorem.** Let two real symmetric pairwise tables with zero diagonal be given on $N\ge4$ electrodes. All combinations (1) on four pairwise distinct electrodes agree if and only if
>
> $$
> R'_{ij}-R_{ij}=\varepsilon_i+\varepsilon_j\qquad(i\ne j)
> $$
>
> The full measurement operator therefore has rank $N(N-3)/2$, and the undetermined part of the table has dimension $N$.

This is a result about the linear operator on pairwise data. Its formulation and proof using KVP appear in [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis#What four-point combinations retain|the note on KVP applications]]. A short self-contained proof follows.

> [!note]- Proof that this is the entire ambiguity
> **Proof.** Preservation of the measurements under the stated additions has already been checked. For the converse, let $A$ be the difference between the tables. Vanishing four-point combinations mean that the pair sums agree for all three pairings of every quadruple.
>
> Choose electrodes numbered $1,2,3$ and set
>
> $$
> \varepsilon_1=\frac{A_{12}+A_{13}-A_{23}}2,
> \qquad \varepsilon_i=A_{1i}-\varepsilon_1\quad(i\ne1)
> $$
>
> Substitution gives $A_{ij}=\varepsilon_i+\varepsilon_j$ on pairs among $1,2,3$. For $i\ge4$, equality of pair sums on $1,2,3,i$ gives
>
> $$
> A_{2i}=A_{1i}+A_{23}-A_{13}=\varepsilon_2+\varepsilon_i
> $$
>
> Similarly, $A_{3i}=\varepsilon_3+\varepsilon_i$. For distinct $i,j\ge4$, use the quadruple $1,2,i,j$:
>
> $$
> A_{ij}+A_{12}=A_{1i}+A_{2j}
> $$
>
> Hence $A_{ij}=\varepsilon_i+\varepsilon_j$ for every pair. The table determines these parameters uniquely, so the kernel has dimension $N$. Out of $\binom N2$ pair coordinates, the measurements retain $\binom N2-N=N(N-3)/2$ independent combinations. $\square$

A grid of $16$ electrodes has $120$ pair coordinates, but all four-electrode experiments on that same grid provide only $16(16-3)/2=104$ independent linear combinations. The remaining $16$ degrees of freedom of an arbitrary table are not determined by these experiments. Additional constraints on the medium may reduce this ambiguity.

> [!note]- Connection with KVP decomposition
> In [[KVP Decomposition of Pair Characteristics|KVP terminology]], the undetermined part is $K\oplus V$, while the full measurement set determines the P-component. An incomplete set of experiments may leave more ambiguity. The main conclusion requires only the cancellation of vertex additions shown above.

This ambiguity also occurs in physical resistor networks. Connect each terminal to the original network through an additional series resistor of resistance $\varepsilon_i>0$. Pairwise effective resistances increase by $\varepsilon_i+\varepsilon_j$, while measurements on four distinct terminals remain unchanged. This exact contact model is discussed in [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis#An exact model of contact corrections|the note on KVP applications]].

> [!note] What cannot be recovered
> The theorem concerns recovery of an arbitrary pairwise table from these measurements alone. A model of the medium or known values of other characteristics can reduce the ambiguity. Locating electrodes within the survey area does not itself prevent recovery when additional information is available.
>
> The requirement of four distinct electrodes matters: formally $T_{ab,ab}=R_{ab}$, but this measurement is outside the set considered here.

## A pairwise characteristic of a continuous medium

The transition to field measurements requires distinguishing two meanings of a pairwise quantity. A graph resistance $R_{ij}$ is the effective resistance between two terminals. Moving the auxiliary electrodes far away in a four-electrode experiment isolates a different quantity: the potential at one point due to unit current at another, relative to a remote zero potential.

> [!info] Pairwise potential coefficient
> **Definition.** Let $Z_{ij}$ denote the potential at $j$ due to a unit current source at $i$, with current return at infinity and potential tending to zero at infinity. A model in which this response is defined is assumed. In a reciprocal medium, $Z_{ij}=Z_{ji}$.

For a homogeneous isotropic half-space with a flat surface,

$$
Z_{ij}=\frac{\rho}{2\pi d_{ij}},\qquad i\ne j
$$

Here $d_{ij}$ is the ordinary distance between surface points, and $\rho=1/\sigma$ is the resistivity of the medium. In this note, $\rho$ does not denote the graph resistance radius. The potential formula and its four-electrode application are given in the [GPG teaching material](https://alainplattner.net/gpg/content/DC_resistivity/DC_basic_principles_current_voltage_halfspace.html) and its [section on survey arrays](https://alainplattner.net/gpg/content/DC_resistivity/DC_surveys.html).

The potential due to the source pair $a,b$ is the difference of their contributions. Therefore,

$$
T_{ab,mn}=Z_{am}-Z_{bm}-Z_{an}+Z_{bn}
$$

In a homogeneous medium, changing the array geometry changes this value even when conductivity is unchanged. Differences between measured values alone do not establish heterogeneity.

For finite electrodes in a linear model with a reference terminal, self-coefficients $Z_{ii}$ can also be defined. The effective resistance is then

$$
R_{ij}=Z_{ii}+Z_{jj}-2Z_{ij}
$$

Substitution into (1) cancels the self-coefficients and gives the same formula for $T$. The self-potential of an ideal point source in a three-dimensional half-space is singular. Without a separate electrode model, this relation therefore cannot give a finite $R_{ij}$ between two point sources.

The $1/d$ law here applies to $Z_{ij}$. The notation $R_{ij}$ remains reserved for the effective resistances of [[Effective Resistance and Graph Geometry|graph resistance geometry]]. The quantities $R$, $Z$, and $T$ are measured in ohms but have different definitions. Resistivity $\rho$ is measured in ohm-meters.

## Why two electrodes are moved away

Let $a,n$ remain in the survey area while current electrode $b$ and sensing electrode $m$ are moved outside it. To estimate positive $Z_{an}$, reverse the order of the sensing electrodes:

$$
\widehat Z_{an}:=T_{ab,nm}=\frac{\varphi_n-\varphi_m}{I}=-T_{ab,mn}
$$

Then

$$
\widehat Z_{an}=Z_{an}+Z_{bm}-Z_{am}-Z_{bn}
$$

The hat denotes an estimate obtained from a measurement. If the remote contributions are small or cancel, $\widehat Z_{an}$ approximates $Z_{an}$. This is a *pole-pole* array: one current and one sensing electrode are active locally, while the other two approximate remote reference electrodes. Finite remote distances and actual electrode coordinates are discussed in the [RES2DINV manual, section 7.3](https://help.seequent.com/ResXDinv/en-GB/Content/Resources/DownloadableAssets/Res2DInv_Manual.pdf).

This procedure uses additional information about the medium and its remote contributions. Simply adding two unknown electrodes to a finite grid does not remove the measurement kernel described above. Vertex additions to $Z$ also cancel in four-point combinations; the condition at infinity or a compensation model selects a particular pairwise representation.

In the homogeneous half-space, the relative error of this estimate is

> [!info] Error due to finite remote distances
> **Proposition.** For four distinct surface point electrodes in a homogeneous isotropic half-space,
>
> $$
> \boxed{\varepsilon=\frac{\widehat Z_{an}-Z_{an}}{Z_{an}}
> =d_{an}\left(\frac1{d_{bm}}-\frac1{d_{am}}-\frac1{d_{bn}}\right)}
> \tag{2}
> $$

> [!note]- Derivation of the error
> **Proof.** The formula for $\widehat Z_{an}$ gives
>
> $$
> \widehat Z_{an}-Z_{an}=\frac{\rho}{2\pi}\left(\frac1{d_{bm}}-\frac1{d_{am}}-\frac1{d_{bn}}\right)
> $$
>
> Dividing by $Z_{an}=\rho/(2\pi d_{an})$ gives (2). $\square$

In this model the relative error depends only on array geometry. Large distances reduce individual remote contributions. Another option is to arrange for their cancellation.

## The compensation triangle

Let $O$ be the center of a small survey area. When calculating distances to the remote electrodes, replace $a,n$ by the center:

$$
d_{am}\approx d_{Om},\qquad d_{bn}\approx d_{Ob}
$$

This approximation applies only to the remote distances. The active electrodes remain distinct; their separation $d_{an}$ is not set to zero.

The remote correction vanishes in this approximation when

$$
\boxed{\frac1{d_{bm}}=\frac1{d_{Om}}+\frac1{d_{Ob}}}
$$

The vertices $O,b,m$ form a triangle. Writing its side lengths as $x=d_{Ob}$, $y=d_{Om}$, $z=d_{bm}$ gives $z=xy/(x+y)$. The lengths must also satisfy the usual triangle inequalities.

The simplest choice puts both remote electrodes at equal distances from the center:

$$
d_{Ob}=d_{Om}=D,\qquad d_{bm}=\frac D2
$$

The angle between the directions to $b,m$ is then

$$
\boxed{\theta=2\arcsin\frac14\approx28.955^\circ}
$$

![[images/Compensation triangle.svg]]

*Central approximation: both remote electrodes are at distance $D$ from the survey center and at distance $D/2$ from each other. The active electrodes $a,n$ lie near $O$ and are replaced by the center only for calculating the remote contributions.*

The same angle appears in **Robain et al. (1999), section 3.1, equation (16)**: $\sin(\theta/2)=1/4$. They consider symmetric pseudo-pole arrays and cancellation of the leading geometric error term. Their practical discussion uses an angle of about $30^\circ$. This known geometry is expressed here using $O,b,m$. “Compensation triangle” is a descriptive label, not a claim of an established term or a new construction.

> [!note]- Derivation of the angle
> **Proof.** The angle bisector at $O$ divides the isosceles triangle into two right triangles. Half the base is $D/4$ and the hypotenuse is $D$. Thus $\sin(\theta/2)=1/4$. $\square$

For a fixed pair $a,n$, exact compensation in the homogeneous model requires $1/d_{bm}=1/d_{am}+1/d_{bn}$. The triangle with vertex $O$ satisfies this condition in the central approximation. As the active electrodes move across the area, the residual correction changes.

## Error over a finite survey area

Suppose the entire area lies within a circle of radius $h$ centered at $O$, and the remote electrodes follow the isosceles arrangement with $D>h$. Write $d=d_{an}$ for the active separation; then $d\le2h$.

> [!info] Upper bound on the residual error
> **Proposition.** In a homogeneous half-space, for any distinct $a,n$ in this area,
>
> $$
> \boxed{|\varepsilon|\le\frac{2hd}{D(D-h)}\le\frac{4h^2}{D(D-h)}}
> \tag{3}
> $$
>
> This is a sufficient upper bound, not a claim that it is attained by this arrangement.

> [!note]- Proof of the bound
> **Proof.** The triangle inequality gives $D-h\le d_{am},d_{bn}\le D+h$. Hence
>
> $$
> \left|\frac1{d_{am}}-\frac1D\right|\le\frac{h}{D(D-h)}
> $$
>
> The same bound holds for $d_{bn}$. Since $d_{bm}=D/2$, the bracket in (2) equals
>
> $$
> \frac2D-\frac1{d_{am}}-\frac1{d_{bn}}
> $$
>
> Its absolute value is at most $2h/[D(D-h)]$. Multiplication by $d$ and the inequality $d\le2h$ give (3). $\square$

For $D\gg h$, the upper bound on relative error is of order $(h/D)^2$. For example, at $D=20h$ it is at most $4/(20\cdot19)\approx1.053\%$. If the survey area has radius $5$ m, this means $100$ m from its center to each remote electrode and $50$ m between the remote electrodes.

The bound assumes exact placement and a homogeneous medium. Positioning errors, uneven terrain, and heterogeneous conductivity add further deviations. In a heterogeneous medium, equality of reciprocal distances does not by itself guarantee $Z_{bm}=Z_{am}+Z_{bn}$.

## Established results and the remaining inverse problem

A four-electrode measurement gives an inner product in the network resistance model. The full collection of such measurements on distinct terminals determines a pairwise table only up to vertex additions. This is an exact algebraic result, independent of instrument quality.

Remote electrodes allow additional conditions on distant contributions to be used. For a homogeneous half-space, the note gives an exact error formula, a known triangular compensation arrangement, and a bound on the residual over a finite survey area. These results do not establish the accuracy of the same compensation in an arbitrary heterogeneous medium.

The resulting table can now be studied: which values are linked by geometry, and can the measurement set be reduced? These questions are addressed in [[Properties of Resistances in a Continuous Medium]].

Recovering internal conductivity requires another transition. Its basis is developed in [[Resistance Variations in Graphs and Continuous Media]], while admissible changes and an algorithm are discussed in [[Reconstructing Couplings with a Prescribed Neighbor Structure]].

## Programming example

A calculation with `polyform_algebra` is provided in [[en/PythonExamples/Example - Electrometry#What four electrodes determine|the Electrometry example]]. It is part of the series notebook with input data and checks.

## Sources and connections

- [[Inner Product of Graph Vectors]] - polarization of resistances, reciprocity, and the four-point identity.
- [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]] - the four-point measurement kernel, observability of P, and the exact series-contact model.
- [[Effective Resistance and Graph Geometry]] - graph resistance and its metric meaning.
- Robain H., Albouy Y., Dabas M., Descloitres M., Camerlynck C., Mechler P., Tabbagh A. **The location of infinite electrodes in pole-pole electrical surveys: consequences for 2D imaging.** *Journal of Applied Geophysics*, 41(4), 1999, 313-333. [DOI](https://doi.org/10.1016/S0926-9851(99)00010-5), [full text in the IRD archive](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_7/b_fdi_55-56/010023106.pdf). Section 3.1, equation (16): the symmetric arrangement with angle $28.96^\circ$.
- **Geophysics for Practicing Geoscientists:** [Currents and voltages in a uniform earth](https://alainplattner.net/gpg/content/DC_resistivity/DC_basic_principles_current_voltage_halfspace.html), [Surveys](https://alainplattner.net/gpg/content/DC_resistivity/DC_surveys.html) - point-source potential and the four-electrode formula for a homogeneous half-space.
- **RES2DINV manual, 2025**, [section 7.3: Remote electrodes of the pole-pole and pole-dipole arrays](https://help.seequent.com/ResXDinv/en-GB/Content/Resources/DownloadableAssets/Res2DInv_Manual.pdf) - finite remote-electrode positions and geometric factors.

The algebraic part agrees with the KVP series. Bound (3) is derived here from the triangle inequality; the source of the triangular arrangement is identified alongside its description.
