---
title: Applications of KVP Decomposition - Electrometry and Pair Data Analysis
date: 2026-10-26
updated: 2026-10-26
revision: 1
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: kvp-applications-electrometry-and-pairwise-data
lang: en
order: 6
description: "Possible uses of KVP: four-electrode measurements and observability of P, series contact resistances, interaction networks, monitoring, and directed flows. Proved properties and limits of applied interpretations."
---

KVP decomposition is useful when an observed quantity belongs to a pair of objects and its change may reflect an overall level, properties of individual objects, or pair structure itself. Four-point combinations are especially relevant to electrometry: in a symmetric resistance model, they express transfer resistances and depend only on the P-component of pair resistances.

This note develops two models in detail: a small electrical network and an interaction table for four participants. Their properties are proved and checked by direct computation. These illustrate possible uses; they are not tests of KVP on field or organizational data. Detecting heterogeneities in a conducting medium and interpreting real interactions require additional models and validation.

Components are defined in [[KVP Decomposition of Pair Characteristics]], oriented extensions in [[Oriented Extensions of KVP - Circulation and Imbalance]], and passage from couplings to metric data in [[KVP Decomposition of the Green Matrix and Resistances]].

## Mathematical basis: the residual of an additive model

Let $A$ be a real symmetric table on a fixed set of $n\ge4$ objects, with $A_{ii}=0$. All pairs are observed and receive equal weight in the decomposition. Write

$$
N=\binom n2,\qquad
\mu=\frac1N\sum_{i<j}A_{ij},\qquad
d_i=\sum_jA_{ij}
$$

Introduce vertex parameters

$$
\alpha_i=\frac{d_i-(n-1)\mu}{n-2},
\qquad \sum_i\alpha_i=0
$$

**Definition.** In this notation, KVP decomposition is

$$
\boxed{A_{ij}=\mu+\alpha_i+\alpha_j+P_{ij}\quad(i\ne j)}
\tag{1}
$$

All three component diagonals are zero; $P$ is symmetric and satisfies $\sum_jP_{ij}=0$. Here $A_K$ has constant off-diagonal entries $\mu$, $A_V$ has entries $\alpha_i+\alpha_j$, and $P=A_P$.

The sum of K and V is the unique best additive approximation in the problem

$$
\min_{m,\,\sum_i b_i=0}
\sum_{i<j}\bigl(A_{ij}-m-b_i-b_j\bigr)^2
$$

This follows from coefficient orthogonality proved in [[KVP Decomposition of Pair Characteristics]]. The inner product is $\langle A,B\rangle_0=\sum_{i<j}A_{ij}B_{ij}$; it is not the PMG metric inner product.

**Corollary.** If the observations change according to

$$
A'_{ij}=A_{ij}+\varepsilon_i+\varepsilon_j\quad(i\ne j),
\qquad A'_{ii}=0
$$

then

$$
\boxed{\Pi_P A'=\Pi_P A}
\tag{2}
$$

Indeed, this addition lies entirely in $K\oplus V$. With $\bar\varepsilon=n^{-1}\sum_i\varepsilon_i$, its K-contribution is $2\bar\varepsilon$, and its V-contribution is $(\varepsilon_i-\bar\varepsilon)+(\varepsilon_j-\bar\varepsilon)$.

The interpretation of $\varepsilon_i$ depends on the problem: an instrument correction, individual activity, or some other additive effect. The decomposition itself does not identify the cause. In particular, it does not prove that V is error and P is useful signal.

**Remark.** P-projection is not ordinary double centering. For a zero-diagonal correction $B_{ij}=\varepsilon_i+\varepsilon_j$ with $i\ne j$, and $J=I-\mathbf1\mathbf1^{\mathsf T}/n$,

$$
\Pi_P B=0,\qquad
JBJ=-2J\operatorname{diag}(\boldsymbol\varepsilon)J
$$

The second expression is generally nonzero, as follows from $B=\boldsymbol\varepsilon\mathbf1^{\mathsf T}+\mathbf1\boldsymbol\varepsilon^{\mathsf T}-2\operatorname{diag}(\boldsymbol\varepsilon)$. Thus passing from a resistance table to a centered Gram matrix does not itself remove these corrections. The distinction between the operators is explained in [[The Distance Operator and KVP Decomposition]].

## What four-point combinations retain

**Definition.** For four pairwise distinct indices, set

$$
\mathcal T_{ab,mn}(A)
=\frac12(A_{an}+A_{bm}-A_{am}-A_{bn})
\tag{3}
$$

Each vertex parameter occurs with opposite signs, so

$$
\mathcal T_{ab,mn}(A)=\mathcal T_{ab,mn}(A_P)
$$

**Theorem.** The complete collection of combinations (3) uniquely determines the P-component. Two symmetric pair tables give the same combinations if and only if their difference has the form $\varepsilon_i+\varepsilon_j$ for $i\ne j$.

**Proof.** It suffices to characterize tables A for which all combinations vanish. For such tables, the sums over the three pair partitions of any four elements coincide. Set

$$
b_1=\frac{A_{12}+A_{13}-A_{23}}2,
\qquad b_i=A_{1i}-b_1\quad(i\ne1)
$$

For pairs among $1,2,3$, we obtain $A_{ij}=b_i+b_j$ directly. For $i\ge4$, equality of sums on the four elements $1,2,3,i$ gives

$$
A_{2i}=A_{1i}+A_{23}-A_{13}=b_2+b_i,
\qquad
A_{3i}=A_{1i}+A_{23}-A_{12}=b_3+b_i
$$

Finally, for distinct $i,j\ge4$, the equality $A_{ij}+A_{12}=A_{1i}+A_{2j}$ gives $A_{ij}=b_i+b_j$. Thus the kernel of the collection (3) is exactly $K\oplus V$. The reverse inclusion follows from cancellation of vertex terms. $\square$

The number of independent linear data of this kind is therefore

$$
\dim\mathcal P_n=\frac{n(n-3)}2
$$

For four objects, two independent combinations of the six pair quantities remain. The three ways of assigning four indices to two pairs satisfy

$$
\mathcal T_{ab,cd}-\mathcal T_{ac,bd}+\mathcal T_{ad,bc}=0
\tag{4}
$$

This is a result about algebraic observability: without additional assumptions, these data cannot recover K and V. Representation through P organizes the available information but does not increase the number of independent measurements.

## Electrometry: from currents and voltages to P

Consider a finite connected network of ordinary resistors with symmetric nonnegative conductances. Let $L$ be its Laplacian and $\mathrm{Gr}=L^+$. In this section, $R$ is the table of **symmetric pair resistances**, not the one-way resistance table $r$.

Inject current $I\ne0$ at terminal $a$ and extract it at $b$. The electrical potentials $\boldsymbol\varphi$ satisfy

$$
L\boldsymbol\varphi=I(\mathbf e_a-\mathbf e_b)
$$

Assume an ideal voltmeter between $m$ and $n$, drawing no current. **Definition.** The transfer resistance of this configuration is

$$
T_{ab,mn}=\frac{\varphi_m-\varphi_n}{I}
$$

Using the Green-matrix solution,

$$
\begin{aligned}
T_{ab,mn}
&=(\mathbf e_m-\mathbf e_n)^{\mathsf T}
\mathrm{Gr}(\mathbf e_a-\mathbf e_b)\\
&=\frac12(R_{an}+R_{bm}-R_{am}-R_{bn})
\end{aligned}
\tag{5}
$$

The sign depends on the order of the current pair and of the measured voltage difference. Transfer resistance may be negative; this does not mean a negative resistance of an individual resistor.

For four distinct terminals, (3) and (5) give

$$
\boxed{T_{ab,mn}=\mathcal T_{ab,mn}(R_P)}
\tag{6}
$$

Thus P has a direct measurement interpretation in this model. Measurements with shared current and voltage terminals generally retain K- and V-contributions as well.

If the network has internal nodes, decompose the resistance table of the **chosen terminal set**. One may compute resistances in the full network and select the required pairs, or eliminate internal vertices while preserving the boundary response, as in [[Vertex Elimination and Induced Couplings]]. The number of KVP objects is then the number of selected terminals. This is not a decomposition of the table of all internal couplings.

The measurements $T_{ab,mn}$ have four indices. They cannot directly be declared a pair table $R_{ij}$: operator (5) specifies their relation to R. The complete collection of admissible measurements recovers P; for an incomplete collection, the rank of the corresponding linear system must be checked.

## An exact model of contact corrections

Choose nodes $x_i$ of a network. Attach a separate terminal $a_i$ to each node through a single series resistor of resistance $\varepsilon_i>0$. The terminals $a_i$ are leaves of the extended network. Let $R^0_{ij}$ denote the resistance between $x_i,x_j$ in the original network and $R^{\mathrm{term}}_{ij}$ that between the new terminals.

**Proposition.** For distinct terminals,

$$
\boxed{R^{\mathrm{term}}_{ij}=R^0_{ij}+\varepsilon_i+\varepsilon_j}
\tag{7}
$$

**Proof.** Under unit current from $a_i$ to $a_j$, both corresponding contact resistors carry current 1. No current flows through the other leaf resistors. The internal network receives the same current pair $x_i,x_j$, so the total voltage drop is $\varepsilon_i+R^0_{ij}+\varepsilon_j$. $\square$

Formula (2) gives the exact invariance

$$
\Pi_P R^{\mathrm{term}}=\Pi_P R^0
$$

Transfer resistances also coincide for four distinct terminals. Physically, the voltage contacts have no voltage drop because they carry no current; drops at the current contacts do not enter the measured difference. The formula uses the actual current I, rather than assuming that current stays unchanged under fixed source voltage.

This explains one possible benefit of KVP: pair data can be compared independently of series contact resistances **within this model**. If only four-electrode measurements are available, this cancellation has already occurred in the data; subsequently recovering P does not remove that error a second time.

A real electrode of finite size may change the current distribution in the medium. Its effect need not reduce to a single series resistor. The distinction between that circuit and a distributed-contact model is discussed in detail by [Cheng et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4816634/); [Hua et al.](https://pubmed.ncbi.nlm.nih.gov/8375870/) study edge and shunting effects. These electrode-model studies support the need to choose a physical model; they are not validations of KVP.

## A computed example: contacts and a conductance change

Take the cycle $a-b-c-d-a$ with unit conductances. Compare it with two changes: adding series contacts and increasing the conductance of $ab$ from 1 to 2.

![[Electrometry example for KVP.svg]]

*Left: the original unit cycle. Center: leaf terminals are attached to its four nodes through resistors of resistance $1/4,1/2,3/4,1$; KVP is applied to the table on the four external terminals. Right: the internal conductance $ab$ is changed, with no contacts present. Numbers in the center panel are contact resistances; the 2 on the right is a coupling conductance.*

All quantities below use consistent arbitrary units. For the original cycle,

$$
R^0=\frac14
\begin{pmatrix}
0&3&4&3\\
3&0&3&4\\
4&3&0&3\\
3&4&3&0
\end{pmatrix}
$$

Its K-component has entries $5/6$, and V is zero. In pair order $ab,ac,ad,bc,bd,cd$, the P-component is

$$
R_P^0:\quad\frac1{12}(-1,2,-1,-1,2,-1)
$$

Even the uniform cycle has $R_P^0\ne0$. Thus nonzero P alone does not indicate a conductance anomaly.

### Adding contacts

Set $\boldsymbol\varepsilon=(1/4,1/2,3/4,1)$. Between the external terminals of the extended network,

$$
R^{\mathrm{term}}=\frac12
\begin{pmatrix}
0&3&4&4\\
3&0&4&5\\
4&4&0&5\\
4&5&5&0
\end{pmatrix}
$$

The mean resistance has increased from $5/6$ to $25/12$, and a V-component has appeared. But $R_P^{\mathrm{term}}=R_P^0$, as predicted by (7).

### Changing an internal coupling

With conductance $c_{ab}=2$ and all other cycle conductances equal to 1, the resistance table is

$$
R^1=\frac17
\begin{pmatrix}
0&3&6&5\\
3&0&5&6\\
6&5&0&5\\
5&6&5&0
\end{pmatrix}
$$

In the same pair order,

$$
R_P^1:\quad\frac17(-1,1,0,0,1,-1),
\qquad
\Delta P=\Pi_P(R^1-R^0)
=\frac1{84}(-5,-2,7,7,-2,-5)
$$

P has now changed. The full table of four-electrode responses with fixed pair order contains the following three values; two are independent by (4).

| Configuration: current pair, voltage pair | Original cycle | Cycle with contacts | $c_{ab}=2$ | $c_{ab}=2$ with the same contacts |
| --- | ---: | ---: | ---: | ---: |
| $ab,cd$ | $-1/4$ | $-1/4$ | $-1/7$ | $-1/7$ |
| $ac,bd$ | $0$ | $0$ | $1/7$ | $1/7$ |
| $ad,bc$ | $1/4$ | $1/4$ | $2/7$ | $2/7$ |

The contact changes did not affect these measurements; the chosen internal conductance change did. This is a directly computed result for four specified networks. It does not establish that every internal change will be detected or that its location can be uniquely recovered.

To detect a deviation from a known background, a natural object is $\Delta P=\Pi_P(R-R^0)$ with the terminals fixed. Sensitivity must still be checked: part of a real change may lie in $K\oplus V$ and disappear from four-electrode data. Terminal and boundary geometry enters the choice of $R^0$; P does not remove it automatically.

## An interaction network: vertex activity and an individual pair

Consider an illustrative table of counts of joint interactions over the same time interval. Each event belongs to an unordered pair; self-interactions are excluded. The vertices are $a$ for Anna, $b$ for Boris, $c$ for Vera, and $d$ for Gleb. The data are invented for this example.

Initially each pair has 10 interactions: $A^0_{ij}=10$ for $i\ne j$. Only K is present.

Now consider two changes:

1. Anna has 4 additional interactions with each of the other three participants. The increment $E^{(a)}$ equals 4 on pairs involving a and zero elsewhere.
2. Vera and Gleb carry out joint work that adds 6 events only to pair $cd$. Denote this increment by $E^{(cd)}$.

![[Vertex and pair changes in KVP interactions.svg]]

*The panels show increments to the common initial table, in which every pair had value 10. Left: three equal increases incident to one vertex form a purely additive vertex correction. Right: one pair changes. Its P-projection also has coefficients on other pairs, as required by the zero-row-sum conditions.*

The first increment has the form $\varepsilon_i+\varepsilon_j$ with $\boldsymbol\varepsilon=(4,0,0,0)$, so $\Pi_P E^{(a)}=0$. Its K-contribution is 2, and its V-contribution is 2 on pairs involving a and $-2$ on the others. Increased individual activity changes both K and V: the informal phrase “vertex change” does not mean a pure V-component.

The increment to a single pair has all three components nonzero:

| Pair | $E^{(a)}_{ij}$ | $E^{(cd)}_{ij}$ | $(E^{(cd)}_K)_{ij}$ | $(E^{(cd)}_V)_{ij}$ | $(E^{(cd)}_P)_{ij}$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $ab$ | $4$ | $0$ | $1$ | $-3$ | $2$ |
| $ac$ | $4$ | $0$ | $1$ | $0$ | $-1$ |
| $ad$ | $4$ | $0$ | $1$ | $0$ | $-1$ |
| $bc$ | $0$ | $0$ | $1$ | $0$ | $-1$ |
| $bd$ | $0$ | $0$ | $1$ | $0$ | $-1$ |
| $cd$ | $0$ | $6$ | $1$ | $3$ | $2$ |

After both changes, the observed table is

$$
A^2=A^0+E^{(a)}+E^{(cd)}
=\begin{pmatrix}
0&14&14&14\\
14&0&10&10\\
14&10&0&16\\
14&10&16&0
\end{pmatrix}
$$

Its mean is 13, and its P-component coincides with $E^{(cd)}_P$. Adding Anna's vertex activity did not change this residual.

However, the positive value $(E^{(cd)}_P)_{ab}=2$ does not mean that Anna and Boris had two hidden interactions. Pair $ab$ did not change at all in passing from $A^0+E^{(a)}$ to $A^2$. P describes deviation from a newly fitted additive model; its coefficients are linked by the zero-row-sum conditions. An individual P-coefficient therefore cannot be read as an independent count of actual events.

In practice, this representation allows residual pair structure to be compared while individual activity changes. It is not a ready-made method of community detection, employee evaluation, or causal explanation of interactions. A model of expected couplings proportional to $d_i d_j$ also differs from the additive model (1).

## Monitoring and measures of change

For two tables on the same object set, put $\Delta A=A^{(1)}-A^{(0)}$. Linearity gives

$$
\Delta A_X=A_X^{(1)}-A_X^{(0)},
\qquad X\in\{K,V,P\}
$$

Changes in the mean level, vertex heterogeneity, and residual structure can be monitored separately. For quantitative comparison, define the coefficient sums of squares

$$
E_X=\sum_{i<j}(\Delta A_X)_{ij}^2,
\qquad
E=\sum_{i<j}(\Delta A_{ij})^2
$$

Orthogonality gives the exact equality $E=E_K+E_V+E_P$. For $E>0$, the ratios $E_X/E$ give the shares of change under the chosen coefficient inner product.

For the two increments in the example,

| Change | $E_K$ | $E_V$ | $E_P$ | $E$ |
| --- | ---: | ---: | ---: | ---: |
| 4 added to every pair involving Anna | $24$ | $24$ | $0$ | $48$ |
| 6 added only to the Vera-Gleb pair | $6$ | $18$ | $12$ | $36$ |

Even a change in a single pair does not belong entirely to P: here the ratio $E_P/E$ is $1/3$. The measure characterizes the chosen projection, not the probability of a pair-specific cause or the proportion of correctly detected signal.

Under overall rescaling $A\mapsto\lambda A$, all components are multiplied by $\lambda$. Time intervals, units, and counting rules must therefore be consistent. Adding a vertex changes pair space and the projectors themselves; old and new components cannot directly be compared as outputs of the same decomposition.

For an interaction network, decomposition of the original coupling table C must also be distinguished from decomposition of its resistance table R. The former describes direct interactions; the latter describes accessibility geometry through the entire network. The nonlinear transition between them is discussed in [[KVP Decomposition of the Green Matrix and Resistances]].

## Directed flows: where O and U are needed

If data are directional, such as amounts of a resource transferred $F_{ij}$, they should be decomposed as an oriented table. Incoming and outgoing sums must use the same units and time interval:

$$
d_i^{out}=\sum_jF_{ij},\qquad
d_i^{in}=\sum_jF_{ji},\qquad
\delta_i=d_i^{out}-d_i^{in}
$$

In KVPOU decomposition,

$$
(F_U)_{ij}=\frac{\delta_i-\delta_j}{2n},
\qquad
F_O=\frac{F-F^{\mathsf T}}2-F_U
$$

U encodes vertex imbalances; O has zero row sums and extracts the circulation part of the skew-symmetric data. K, V, and P describe the symmetric part of the flow: the overall level, heterogeneity of mean incoming and outgoing activity, and residual pair structure.

For example, comparing periods may reveal changes in the imbalance of individual nodes while circulation remains almost unchanged, or vice versa. If the original flow table is balanced, U vanishes; V may remain.

This is a linear description of the table. O may have negative coefficients and nonzero entries on absent arcs, so it cannot automatically be interpreted as a collection of actually traversed routes. Decomposing O into particular cycles requires a choice of representation and is generally nonunique. These limitations and examples are discussed in [[Oriented Extensions of KVP - Circulation and Imbalance]].

## Requirements for working with real data

Applied use requires three parts of the problem to be fixed.

1. **What constitutes a pair observation.** It may be a coupling, resistance, joint event, or directed flow. Matrices on different objects and with different normalizations answer different questions.
2. **Which model K and V remove.** Formula (2) concerns additive corrections at the two endpoints of a pair. It does not remove arbitrary errors, multiplicative effects, or changes in measurement geometry.
3. **What the residual is compared with.** A background, repeated measurements, or a statistical model is needed. P has no universal threshold above which a coefficient becomes an anomaly.

A missing observation must not be replaced by zero without a substantive reason. Incomplete pair data or unequal measurement precision lead to a separate weighted estimation problem; standard projectors for a complete table with equal observation weights do not automatically solve it.

For an incomplete set of four-electrode measurements $y_\omega$, one may formulate

$$
\min_{P\in\mathcal P_n}
\sum_{\omega\in\Omega}w_\omega
\bigl(\mathcal T_\omega(P)-y_\omega\bigr)^2,
\qquad w_\omega>0
$$

Here $\omega$ specifies the ordered current and voltage pairs. Uniqueness depends on the rank of the chosen observation operator; stability also depends on its conditioning and error properties. This is a problem for further work, not a reconstruction of field data performed in this note.

For electrometry, a useful next experiment would compare a homogeneous medium with specified heterogeneities under one electrode geometry, then add contact changes and noise separately. It should test which heterogeneities P distinguishes and how stably. One cannot assume in advance that extracting P improves sensitivity: together with unwanted corrections, it removes all changes in $K\oplus V$.

## Status of results and validation

Invariance (2), the kernel description for four-point measurements, electrical formula (5), and the series-contact model (7) are proved. Electrical examples were checked in exact rational arithmetic in two ways: through the Green matrix and by independently solving grounded Kirchhoff systems for specified currents. For networks with contacts, the systems had eight nodes, while KVP was computed on the table of four external terminals.

The interaction tables and sums of squares were also checked by direct decomposition. The rank of the complete four-point combination operator was additionally checked for $n=4,5,6,7,8$; this is a computational check of a consequence of the proved theorem.

The possibility of using KVP as an exact representation of additive and residual pair effects is justified. The examples do not establish effectiveness in detecting geological heterogeneities, statistical significance of coefficients, or advantages over other models.

The reading order and main results are collected in [[KVP Decomposition and Oriented Extensions]]. [Reproducible computational checks](https://github.com/magin67/pmg-notes/blob/v5/checks/kvp/README.en.md) use exact rational arithmetic and include instructions for running them.

## Sources and connections

- [[KVP Decomposition of Pair Characteristics]]: definitions, projectors, coefficient orthogonality, and counterparts of the decomposition.
- [[KVP Decomposition of the Green Matrix and Resistances]]: distinctions between components of couplings, the Green matrix, symmetric resistances, and one-way resistances.
- [[Vertex Elimination and Induced Couplings]]: passage to a chosen terminal set while preserving network response.
- Cheng K.-S., Isaacson D., Newell J. C., Gisser D. G. *Electrode Models for Electric Current Computed Tomography*. IEEE Transactions on Biomedical Engineering, 1989, 36(9), 918-924. [Open text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4816634/), [DOI: 10.1109/10.35300](https://doi.org/10.1109/10.35300). Comparison of series circuits and distributed electrode models.
- Hua P., Woo E. J., Webster J. G., Tompkins W. J. *Finite element modeling of electrode-skin contact impedance in electrical impedance tomography*. IEEE Transactions on Biomedical Engineering, 1993, 40(4), 335-343. [Abstract](https://pubmed.ncbi.nlm.nih.gov/8375870/), [DOI: 10.1109/10.222326](https://doi.org/10.1109/10.222326). Effects of finite electrode size, shunting, and edge effects.
