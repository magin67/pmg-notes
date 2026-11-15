---
title: Controlled Shunting and Resistance Reconstruction
date: 2026-11-15
updated: 2026-11-15
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-controlled-shunting
lang: en
order: 5
description: "How a known external shunt reveals a resistance through changes in a four-electrode response: single and multiple shunts, contacts, degenerate configurations, and measurement errors."
---

[[ru/Резистивная геометрия и дуальность/Электрометрия/Управляемое шунтирование и восстановление сопротивлений|Русский]]

Ordinary measurements on four distinct electrodes do not determine the entire resistance table. [[What Electrometry Measures]] identifies the vertex additions that remain invisible. Additional information can be obtained by connecting a known external coupling between experiments while keeping the medium and its contacts unchanged.

The simplest case is a shunt across the current electrodes. Some of the current flows through the shunt, reducing the voltage across the other pair. The amount of this reduction determines the original resistance of the current pair. For an arbitrary pair and for multiple shunts, the same principle is expressed by finite coupling-variation formulas.

## What changes in the experiment

Let current $I$ enter through electrode $a$ and leave through $b$, with voltage measured between $m$ and $n$. The measured quantity is

$$
T_{ab,mn}=\frac{\varphi_m-\varphi_n}{I}
$$

The electrodes $a,b,m,n$ are pairwise distinct. An external resistor of conductance $t>0$ connects selected accessible terminals $p,q$; its resistance is $1/t$. Conductances are measured in siemens, and $T$ and resistances $R$ in ohms. The product $tR$ is dimensionless.

> [!info] Experimental assumptions
> Measurements are made at steady state in a linear, reciprocal, connected network with nonnegative conductances. Geometry, internal conductivity, and contacts remain unchanged between experiments. The voltmeter input current is taken to be zero. The total source current entering the combined medium-and-shunt system is known.

The source current divides between the medium and the shunt. If instead the current through the medium alone is kept constant, shunting the current pair will not produce the attenuation described below. If the total current varies slightly, each voltage must be divided by the current measured in its own experiment.

After internal nodes are eliminated, the medium together with its contacts defines an effective electrode Laplacian $\mathbf L_\partial$. Its centered Green matrix is $\mathbf{Gr}=\mathbf L_\partial^+$. For a continuous medium, a model of finite electrodes is required, with finite terminal resistances and the same type of linear reciprocal response. The singular self-potential of an ideal point source is not used here.

Let $\mathbf e_i$ be the column with a 1 at position $i$ and zeros elsewhere. For a pair, put $\mathbf b_{ij}=\mathbf e_i-\mathbf e_j$. Then

$$
R_{ij}=\mathbf b_{ij}^{\mathsf T}\mathbf{Gr}\mathbf b_{ij},
\qquad
T_{ab,mn}=\mathbf b_{mn}^{\mathsf T}\mathbf{Gr}\mathbf b_{ab}
$$

In PMG notation, $T_{ab,mn}=(ab)\cdot(mn)$. The current column has the opposite orientation to the vector $(ab)=b-a$; reversing both arguments preserves their inner product. Coincident pairs are allowed in the formulas: $T_{ab,ab}=R_{ab}$, although the experiment measures voltage across a separate pair.

## A shunt across the current electrodes

Connect the shunt across $a,b$. Write the unshunted response as $T_0=T_{ab,mn}$ and the response after connection as $T(t)$. All unprimed resistances refer to the original network.

> [!info] Reconstruction with one shunt
> **Proposition.** Shunting the current pair gives
>
> $$
> T(t)=\frac{T_0}{1+tR_{ab}}
> $$
>
> If $T_0\ne0$, the original resistance is determined using one nonzero conductance:
>
> $$
> \boxed{R_{ab}=\frac1t\left(\frac{T_0}{T(t)}-1\right)}
> $$

This determination of resistance from a voltage ratio is described in E. N. Kapitanov's patent [RU2664633C2](https://patents.google.com/patent/RU2664633C2/ru), in the explanation of Fig. 3. The derivation below applies to an arbitrary linear resistive medium; no priority is claimed for the measurement principle.

> [!note]- Proof by current division
> **Proof.** Let $I_{\mathrm{med}}$ be the current through the original medium. The voltage across the current terminals is $R_{ab}I_{\mathrm{med}}$, so the shunt current is $tR_{ab}I_{\mathrm{med}}$. Kirchhoff's law gives
>
> $$
> I=I_{\mathrm{med}}(1+tR_{ab})
> $$
>
> In the linear medium, the measured voltage is $T_0I_{\mathrm{med}}$. Division by the total current $I$ gives the response formula; solving it for $R_{ab}$ gives the reconstruction formula. $\square$

For negative $T_0$, the voltage magnitude decreases while its sign is preserved. If $T_0=0$, this configuration provides no resistance information: the zero response remains zero. By reciprocity, the analogous formula holds when the voltage pair is shunted and determines $R_{mn}$.

## A shunt across an arbitrary pair

The pair $p,q$ may now differ from both the current pair and the voltage pair. The shunt changes the current distribution, so the response may either decrease or increase.

> [!info] Exact single-shunt formula
> **Proposition.** Adding conductance $t\ge0$ between $p,q$ gives
>
> $$
> \boxed{
> T'_{ab,mn}=T_{ab,mn}-\frac{t}{1+tR_{pq}}\,T_{pq,ab}T_{pq,mn}
> }
> $$
>
> Every quantity on the right is evaluated in the original network. The formula is exact for finite $t$ and does not require a small shunt conductance.

This is an application of the established inverse formula for a rank-one update; its resistance version is developed in [[One Changing Edge]]. The internal structure of the medium affects the original $R$ and $T$, but not the form of the identity.

> [!note]- Derivation from the Laplacian update
> **Proof.** Put $\mathbf b=\mathbf b_{pq}$. The external coupling adds $t\mathbf b\mathbf b^{\mathsf T}$ to the electrode Laplacian. On the space of currents with zero sum, the Laplacian is invertible and
>
> $$
> \mathbf{Gr}'=\mathbf{Gr}-\frac{t}{1+tR_{pq}}
> (\mathbf{Gr}\mathbf b)(\mathbf b^{\mathsf T}\mathbf{Gr})
> $$
>
> Both sides annihilate the constant column. Multiplication on the left by $\mathbf b_{mn}^{\mathsf T}$ and on the right by $\mathbf b_{ab}$ gives the response formula. The denominator is positive for $t\ge0$. $\square$

For reconstruction, introduce the abbreviations

$$
R=R_{pq},\qquad A=T_{pq,ab}T_{pq,mn},\qquad
\Delta(t)=T_0-T(t)=\frac{tA}{1+tR}
$$

> [!info] Reconstruction from two conductances
> **Corollary.** Suppose $A\ne0$ and $t_1,t_2>0$ are distinct. Write $\Delta_i=T_0-T(t_i)$. Then
>
> $$
> \boxed{R=\frac{\Delta_1/t_1-\Delta_2/t_2}{\Delta_2-\Delta_1}},
> \qquad
> A=\frac{\Delta_1}{t_1}(1+t_1R)
> $$
>
> Three experiments are required: the baseline and two experiments with different shunts. These data determine the product $A$, but not its two factors separately.

> [!note]- Proof
> **Proof.** The equality $\Delta_i(1+t_iR)=t_iA$ implies $A=\Delta_i/t_i+R\Delta_i$. Equating the two expressions gives the formula for $R$. Moreover,
>
> $$
> \Delta_2-\Delta_1=\frac{A(t_2-t_1)}{(1+t_1R)(1+t_2R)}\ne0
> $$
>
> Thus the inversion is valid. Back-substitution determines $A$. $\square$

The shunt is invisible to the selected response if $A=0$. One of the two original current experiments then produces no potential difference between $p$ and $q$. In particular, if $T_{pq,ab}=0$, no current flows through the shunt in the driving experiment. A different shunt pair or current-and-voltage configuration is needed. When $A\ne0$, a shunt can produce a nonzero response even from a baseline $T_0=0$.

## Multiple shunts and their interaction

Choose $s$ electrode pairs. Let $\mathbf B$ contain their current columns, and let $\mathbf D=\operatorname{diag}(t_1,\ldots,t_s)$ contain their nonnegative conductances. Here $\mathbf B$ is the incidence matrix of the selected external couplings. Then

$$
\mathbf L'_\partial=\mathbf L_\partial+\mathbf B\mathbf D\mathbf B^{\mathsf T},
\qquad
\mathbf G=\mathbf B^{\mathsf T}\mathbf{Gr}\mathbf B
$$

The matrix $\mathbf G$ is the Gram matrix of the shunted segments. Its diagonal entries are the resistances of the selected pairs; its off-diagonal entries are transfer resistances between them.

> [!info] Response to a network of external shunts
> **Proposition.** Let $\mathbf I_s$ be the identity matrix of order $s$. Then
>
> $$
> \boxed{\mathbf{Gr}'=\mathbf{Gr}-
> \mathbf{Gr}\mathbf B(\mathbf I_s+\mathbf D\mathbf G)^{-1}
> \mathbf D\mathbf B^{\mathsf T}\mathbf{Gr}}
> $$
>
> This matrix determines all new transfer resistances. The formula permits zero conductances and linearly dependent columns of $\mathbf B$, including cycles of external couplings.

Derivations using the Woodbury formula and factors of the Laplacian exponential are given in [[Two Edges and Joint Variation#Dependent directions and a compact matrix form|the note on joint coupling variations]]. For external shunts, the result applies after internal nodes are eliminated: the shunts change only the electrode block of the Laplacian, so the same matrix $\mathbf B\mathbf D\mathbf B^{\mathsf T}$ is added to the result of elimination. Elimination is defined in [[Resistance Variations in Graphs and Continuous Media#What remains after internal vertices are eliminated]].

The off-diagonal entries of $\mathbf G$ account for shunt interactions. When shunts are connected sequentially, the second acts on an already modified network. Adding two changes that were each calculated from the original network is generally incorrect.

### Why shunting every pair may not help

Consider four electrodes $a,b,m,n$ connected to a single internal node through identical resistances $\alpha>0$. This is a star. When current is applied through $a,b$, the other two electrodes have the same potential, so $T_{ab,mn}=0$ for every $\alpha$.

> [!example] Symmetry preserves invisibility
> If identical shunts of conductance $t$ are connected across all six electrode pairs, every response on four distinct electrodes remains zero. In contrast, a single shunt across $a,m$ gives
>
> $$
> T_{ab,mn}(t)=\frac{\alpha^2t}{1+2\alpha t}>0
> $$

> [!note]- Verification of the example
> Put $\mathbf J=\mathbf I_4-\mathbf1\mathbf1^{\mathsf T}/4$. The original star has $\mathbf{Gr}=\alpha\mathbf J$. Equal shunts across every pair add $4t\mathbf J$ to the Laplacian, so
>
> $$
> \mathbf{Gr}'=\frac{\alpha}{1+4\alpha t}\mathbf J
> $$
>
> The current columns of disjoint pairs are orthogonal, giving zero response. For a single shunt across $a,m$, we have $R_{am}=2\alpha$, $T_{am,ab}=\alpha$, and $T_{am,mn}=-\alpha$. Substitution into the single-shunt formula gives the stated nonzero response.

Thus shunt placement matters, not just the number of shunts. For specified unknown parameters, responses from several configurations can be combined, and the rank and conditioning of their Jacobian checked, as in [[Reconstructing Couplings with a Prescribed Neighbor Structure#Uniqueness and stability|constrained reconstruction]]. No fixed configuration is claimed here to suffice for every medium.

## A computational example with internal nodes

Take electrodes $a,b,m,n$ and internal nodes $p,q$. Each of the five couplings $ap,mp,pq,bq,nq$ has resistance $1$ ohm. Current is applied through $a,b$ and voltage is measured between $m,n$.

![A network with two internal nodes and an external shunt](<images/Network with a controlled shunt.svg>)

*The rectangles show resistances in ohms. The total source current $I$ divides between the upper shunt and the original network. The voltmeter measures the potential difference between $m,n$.*

Without a shunt, current follows the path $a-p-q-b$. No current flows in the voltmeter branches, so

$$
T_0=1\ \Omega,\qquad R_{ab}=3\ \Omega,\qquad R_{am}=2\ \Omega
$$

| Connected shunts | Conductances, S | Response $T_{ab,mn}$, ohms |
| --- | --- | --- |
| None | $0$ | $1$ |
| $ab$ | $1/3$ | $1/2$ |
| $am$ | $1/4$ | $7/6$ |
| $am$ | $1/2$ | $5/4$ |
| $am$ and $bm$ simultaneously | $1/4$ and $1/2$ | $10/29$ |

The first two rows recover $R_{ab}=3$ ohms. The two experiments with a shunt across $am$ give $\Delta_1=-1/6$ ohm and $\Delta_2=-1/4$ ohm. The two-conductance formula returns $R_{am}=2$ ohms and $A=-1$ ohm$^2$. The increase in response under shunting is not a sign error.

For the two selected pairs in the last row, the Gram matrix is

$$
\mathbf G=\begin{pmatrix}2&1\\1&3\end{pmatrix}\ \Omega
$$

The shunts interact. Adding the changes from two separate experiments would give a final response of $11/30$ ohm instead of $10/29$ ohm.

### Adding contact resistances

Insert a series contact resistance between each accessible terminal and the original network. For $a,b,m,n$, take these resistances to be $0.2$, $0.3$, $0.4$, and $0.1$ ohm, respectively. This is an explicitly chosen contact model, not a general assertion about all electrodes.

The baseline four-electrode response remains $1$ ohm. However, the resistance between the accessible terminals $a,b$ is now

$$
R_{ab}^{\mathrm{term}}=3+0.2+0.3=3.5\ \Omega
$$

With a shunt across $ab$ of conductance $1/3$ S, the response is $T=6/13$ ohm. The reconstruction formula returns $3.5$ ohms. Thus the shunt reveals information hidden in the original four-electrode experiment, but the recovered quantity includes contacts. Their contribution can be subtracted only if it is known or determined under additional assumptions. The exact series-contact model is also discussed in [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis#An exact model of contact corrections]].

## Errors and the choice of conductance

For an arbitrary shunt with $tR\ll1$, the change is approximately $tA$: dependence on $R$ appears only at the next order. For $tR\gg1$, the response is close to the limit $T_0-A/R$, and two large conductances may produce almost identical results. In either case, a formally unique reconstruction may be unstable.

For the current pair, a weak shunt requires subtracting nearly equal numbers in $T_0/T(t)-1$. A strong shunt makes $T(t)$ small and amplifies absolute voltage errors. The practical choice depends on the error model, permissible currents, and the accuracy of the shunt itself.

In the example above, independent Gaussian noise with a standard deviation of $0.001$ ohm is added to each measured $T$. The error in the baseline $T_0$ is shared by estimates using different shunts within one set of experiments. Shunt conductance is assumed to be known exactly. For each conductance, 10,000 reconstructions of $R_{ab}=3$ ohms are performed.

![Reconstruction error for different shunt conductances](<images/Reconstruction error under shunting.svg>)

*The curve is the linearized standard-deviation estimate; the points come from noise simulations. The result assumes a constant absolute error in $T$ and does not establish a universally optimal value of $tR$.*

For example, at $t=0.01$ S, the sample standard deviation of the estimate, relative to the true $R$, is about $5\%$; at $t=1/3$ S it is about $0.44\%$; and at $t=10$ S it is about $3.2\%$. These numbers describe the spread of individual reconstructions, not the error of the average over 10,000 trials.

Several values of $t$ allow the rational dependence $T(t)=T_0-tA/(1+tR)$ to be checked. With noisy data, it is preferable to fit the responses themselves while accounting for their errors. The formally linear expression $t/\Delta(t)=1/A+tR/A$ amplifies errors when $\Delta$ is small; ordinary linear regression without appropriate weights does not account for this. If one common baseline experiment is used, errors in all differences $\Delta_i$ are correlated.

Repeating the baseline measurement after disconnecting the shunt helps detect changes in the medium or contacts. Agreement with the formula checks the consistency of the chosen model within measurement accuracy, but does not prove its uniqueness.

## What can and cannot be reconstructed

Shunting introduces a known change in the external network. It therefore does not contradict the theorem on incomplete four-point data: that theorem concerns measurements of one unchanged network. The new formulation compares several networks related by known additions to the Laplacian.

> [!info] The limit of external interventions
> **Proposition.** If two media together with their contacts have the same complete electrode matrix $\mathbf L_\partial$, any identical external shunt networks preserve their indistinguishability under electrode measurements.

> [!note]- Proof
> **Proof.** After connection, both cases have the same matrix $\mathbf L_\partial+\mathbf B\mathbf D\mathbf B^{\mathsf T}$. Hence their solutions for any prescribed electrode currents and all measured potential differences coincide. $\square$

Controlled shunts can therefore supplement an incomplete set of baseline measurements. They provide no information beyond the complete electrode response and do not by themselves determine the internal conductivity distribution. The recovered resistance $R_{pq}$ is also not the pairwise coefficient $Z_{pq}$ of a point-source continuum model; the distinction between these quantities remains.

An open practical problem is to choose a small number of shunts, their conductances, and current-and-voltage pairs so that the required parameters are distinguishable with acceptable accuracy. The unknown parameters and the contact and error models must be specified in advance. This note does not establish a validated field reconstruction method.

## Reproducibility and sources

The [verification script](<data/Verify shunting.py>) uses the same pinned revision of `polyform_algebra` as the [[en/PythonExamples/Example - Electrometry|series programming examples]]. It checks single and simultaneous shunts, reconstruction from two conductances, elimination of internal nodes, series contacts, and the symmetric star. The formulas are compared with independent direct inversion of the modified Laplacian in SymPy. Exact checks use rational arithmetic; the statistical experiment has a fixed random seed. The script produces both figures and the [results table](<data/Shunting results.json>).

All numerical data in this note are synthetic. The computation illustrates the proved formulas and their stability under the chosen error model; it does not replace an experiment with soil.

- Kapitanov E. N. **Device for measuring electrical impedance in body parts.** Patent [RU2664633C2](https://patents.google.com/patent/RU2664633C2/ru), published August 21, 2018. The explanation of Fig. 3 gives $R=R_{\mathrm{sh}}(U/U_{\mathrm{sh}}-1)$: a known shunt and a voltage ratio. Separating the contact contribution in the patent relies on its own model and does not automatically extend to an arbitrary medium.
- [[One Changing Edge]]: the exact finite variation for one added coupling.
- [[Two Edges and Joint Variation]]: interacting changes, exponential factors, and the matrix formula for several couplings.
- [[Resistance Variations in Graphs and Continuous Media]]: electrode response after eliminating internal vertices.
- [[Reconstructing Couplings with a Prescribed Neighbor Structure]]: parameter distinguishability and limitations of the inverse problem.

The note applies established finite-variation formulas and an established measurement principle to electrometry in PMG. The two-conductance reconstruction, examples, and limitations are derived explicitly; no scientific priority is claimed for these consequences.

Reading order and connections to the other notes: [[en/Resistance Geometry and Duality/Electrometry/Electrometry|Electrometry]].
