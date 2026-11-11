---
title: Edge Influence and Metric Distribution
date: 2026-11-03
updated: 2026-11-11
revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 6
translation_key: metric-distributions-edge-influence
order: 1
description: "From adding a coupling and the finite change in a form's value to a sensitivity field and the metric distribution operator D_L."
---

[[ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/Влияние связей и метрическое распределение|Русский]]


Adding a coupling changes the graph metric and hence the values of measured forms. Fix a form of grade one, change one conductance, and subtract the original value from the new one. Repeating this probe for different couplings, always from the same initial graph, gives their influence field on the form. From this field we derive a metric distribution: sensitivity coefficients of existing edges whose sum equals the original value of the form.

## Adding a coupling to a path

See [[en/PythonExamples/Example - Metric Distributions and Edge Influence#Adding a coupling to a path|the notebook calculation]].

Take the path $a-b-c$ with conductances $c_{ab}=c_{bc}=1$. We measure the form $f=[(ac)]^2$. Its value is the effective resistance between $a$ and $c$:

$$
N(f)=R_{ac}=2
$$

Add a direct coupling $ac$ of conductance $t\ge0$. The original path has resistance $2$ and conductance $1/2$. The new coupling is in parallel with this path, so

$$
N_t(f)=\frac1{1/2+t}=\frac2{1+2t}
$$

The influence of the added coupling is the difference

$$
\Delta_{ac}(t;f)=N_t(f)-N(f)=-\frac{4t}{1+2t}
$$

At $t=1$ we obtain a unit triangle: the value changes from $2$ to $2/3$, and the influence is $-4/3$.

![Adding a coupling to a path and changing the effective resistance](<images/Adding a Coupling to a Path.svg>)

*On the left, coupling $ac$ is absent; the dashed line marks where it will be added. On the right, conductance $1$ has been added. The form $[(ac)]^2$ is unchanged; its metric evaluation changes. Edge labels indicate conductances.*

A coupling can also be added between vertices that are already joined by an edge. This increases the existing conductance. In both cases we compare the values of one fixed form in two metrics.

The absent coupling $ac$ has zero coefficient in the distribution over existing edges. This example already shows that adding it still affects the metric. Below we distinguish adding a new coupling from changing an existing one relatively.

## The form and the initial metric

Let the graph be finite, connected, and undirected. Its vertices are fixed, $a_{ij}=a_j-a_i$, $q_{ij}=[a_{ij}]^2$, and conductances $c_{ij}$ are nonnegative. Edges with $c_{ij}>0$ are called existing edges. Write

$$
L=\sum_{i<j}c_{ij}q_{ij},\qquad M=\exp L
$$

The value of a form $f$ on boundaries is given by the normalized potential

$$
N_L(f)=\frac{\tau(Mf)}{\tau(M)}
$$

Here $\tau(P)$ extracts the coefficient of the fixed full form $T_n=[(a_1\ldots a_n)]^2$, and $\tau(M)>0$ is the spanning-tree coefficient of the initial graph. Definitions and the metric identity are given in [[Laplacian Exponential]].

In this note the input form has grade one. For vectors $v,u$ in the space of affine vectors,

$$
N_L([v]^2)=v^2,\qquad
N_L\left(\frac12\{v,u\}\right)=v\cdot u
$$

where $\{v,u\}=[v,u]+[u,v]$. Under the PMG convention, the norm $v^2=v\cdot v$ is a quadratic quantity, with no square root taken. The notation $[v]^2$ denotes a formal form. All its arguments and coefficients remain fixed as the metric changes.

Below, $N(f)$ without a subscript refers to the initial $L$; a prime denotes the changed metric.

## The finite influence of one coupling

Choose a pair $kl$, set $p=q_{kl}$, and add conductance $t$:

$$
L'=L+tp
$$

Addition has $t\ge0$. The same formula describes weakening when $t<0$, provided $c_{kl}+t\ge0$ and the new graph remains connected. The effective resistance $R_{kl}=N(p)$ is evaluated in the initial metric; it is defined even if coupling $kl$ is initially absent.

The quadratic edge form satisfies $p^2=0$, so

$$
M'=M(e+tp)
$$

where $e=[1,1]$ is the unit form. Both the potential of the measured form and the normalizing spanning-tree coefficient change.

> [!info] Influence of added conductance
> **Definition and formula.** The finite influence of changing coupling $kl$ on a form $f$ is
>
> $$
> \Delta_{kl}(t;f)=N_{L+tp}(f)-N_L(f)
> $$
>
> Provided connectedness is preserved,
>
> $$
> \boxed{
> \Delta_{kl}(t;f)=
> \frac{t}{1+tR_{kl}}\bigl(N(fp)-R_{kl}N(f)\bigr).
> }
> \tag{1}
> $$

The exponential factor and the change in the spanning-tree coefficient are discussed in [[One Changing Edge]]. Formula (1) applies that mechanism to the value of a fixed form.

> [!note]- Derivation with normalization
> **Proof.** Linearity of $\tau$ gives
>
> $$
> \tau(M'f)=\tau(Mf)+t\tau(Mfp),\qquad
> \tau(M')=\tau(M)(1+tR_{kl})
> $$
>
> Hence
>
> $$
> N'(f)=\frac{N(f)+tN(fp)}{1+tR_{kl}}
> $$
>
> Subtracting $N(f)$ gives (1). The condition $1+tR_{kl}>0$ makes division valid; with nonnegative final conductances it is equivalent to preserving connectedness. $\square$

In the opening example, $f=p=[(ac)]^2$, so $fp=0$ and $R_{ac}=N(f)=2$. Formula (1) returns $-4t/(1+2t)$.

We interpret the family of numbers $\Delta_{kl}(t;f)$, under a specified rule for choosing $t$, as the field of finite coupling influence on the form. **Every probe starts from the same initial graph.** Accumulating additions changes the metric and defines a different procedure. The size of $t$ is also part of the comparison: equal absolute and equal relative conductance increments generally give different fields.

## From finite influence to distribution coefficients

For an existing edge $c_{kl}>0$, consider the relative change

$$
c'_{kl}=(1+\varepsilon)c_{kl},\qquad t=\varepsilon c_{kl}
$$

For small $\varepsilon$, the first derivative determines the influence. Choose the coefficient's sign so that a decrease in the norm of a quadratic form when an edge is strengthened corresponds to a positive contribution.

> [!info] Metric distribution coefficient
> **Definition.** For an existing edge, set
>
> $$
> \boxed{
> m_{kl}(f)=
> -\left.\frac{d}{d\varepsilon}N_{L+\varepsilon c_{kl}p}(f)\right|_{\varepsilon=0}
> =-c_{kl}\frac{\partial N_L(f)}{\partial c_{kl}}.
> }
> \tag{2}
> $$
>
> By (1),
>
> $$
> m_{kl}(f)=c_{kl}\bigl(R_{kl}N(f)-N(fp)\bigr)
> \tag{3}
> $$

Thus $m_{kl}$ measures sensitivity to a relative conductance change. It is the coefficient of an infinitesimal change, rather than the finite difference caused by adding one unit of conductance.

Its relation to finite influence is exact:

$$
\boxed{
\Delta_{kl}(t;f)=-\frac{t}{c_{kl}(1+tR_{kl})}m_{kl}(f).
}
\tag{4}
$$

Conversely, for a nonzero admissible $t$, the coefficient can be recovered from one finite probe:

$$
m_{kl}(f)=-\frac{c_{kl}(1+tR_{kl})}{t}\Delta_{kl}(t;f)
$$

Here $R_{kl}$ is the effective resistance in the full network, generally different from the edge's own resistance $1/c_{kl}$. Formula (4) also shows that a zero coefficient is equivalent to zero influence under every admissible change of this coupling alone.

For example, on a unit triangle with $f=[(ac)]^2$, we will obtain $m_{ac}=4/9$. Increase the conductance of $ac$ by $1\%$, so $\varepsilon=0.01$. To first order, the value of the form decreases by $\varepsilon m_{ac}=1/225$. The exact decrease from (4) is $2/453$. The minus sign in the definition of $m$ represents a decrease in the norm under strengthening by a positive coefficient. The relative change is that of **conductance**; the change in $N_L(f)$ is measured in its original units.

### Absent couplings

Addition can be tested between any vertices. A relative change of a zero conductance, however, does not create a coupling. The metric distribution is therefore indexed by existing edges; when $c_{kl}=0$, we set $m_{kl}=0$.

This does not mean that a new coupling has no influence. On the initial path $a-b-c$, the coefficient of the absent edge $ac$ is zero, but adding it changes $R_{ac}$. Such a probe uses (1) directly, without division by $c_{kl}$. The field of possible additions and the distribution over existing edges have different index sets.

## The metric distribution operator

For the inner-product form $f=\{v,u\}/2$, expression (3) simplifies. The exterior metric identity gives

$$
N(fp)=(va_{kl})\cdot(ua_{kl})
=(v\cdot u)R_{kl}-(v\cdot a_{kl})(u\cdot a_{kl})
$$

This is the determinant of pairwise inner products from [[Metric of Higher-Grade Objects]]. Substitution leaves

$$
\boxed{m_{kl}(f)=c_{kl}(v\cdot a_{kl})(u\cdot a_{kl}).}
\tag{5}
$$

> [!info] Assembling coefficients into a form
> **Definition.** The metric distribution operator in grade one is
>
> $$
> \boxed{D_L(f)=\sum_{k<l}m_{kl}(f)[a_{kl}]^2.}
> \tag{6}
> $$
>
> Coefficients are evaluated in the initial metric $L$. The definition extends linearly to arbitrary forms of grade one.

The subscript $L$ distinguishes this operator from the notation $D=\exp Q_1$ used for the dual representation of the Greenian exponential. In this series, $D_L$ denotes the metric distribution.

For a square $f=[v]^2$, the coefficients are nonnegative: $m_{kl}=c_{kl}(v\cdot a_{kl})^2$. For a mixed form, either sign is possible. Reversing an auxiliary edge orientation changes the signs of both inner-product factors and leaves the coefficient and output form unchanged.

The definition is independent of a decomposition of the input $f$ into squares or mixed forms: formula (3) is linear in the form itself. The output edge forms are normalized by the fixed vertex differences $a_l-a_k$.

Compare the three levels:

| Quantity | Meaning |
|---|---|
| $\Delta_{kl}(t;f)$ | Result of a finite probe with prescribed $t$ |
| $m_{kl}(f)$ | Sensitivity coefficient for a relative conductance change |
| $D_L(f)$ | Form assembled from contributions and edge forms $[a_{kl}]^2$ |

The coefficient sum equals $N_L(f)$, not one. For the unit triangle and input $[(ac)]^2$, below we obtain $\sum m_{kl}=2/3$, but $N_L(D_L(f))=4/9$: evaluating the output form additionally multiplies each coefficient by the effective resistance of the corresponding vertex pair. These are different operations.

## Why the coefficients sum to the value of the form

> [!info] Sum of metric contributions
> **Theorem.** For every fixed form of grade one on affine vectors,
>
> $$
> \boxed{\sum_{k<l}m_{kl}(f)=N_L(f).}
> \tag{7}
> $$

> [!note]- Proof by scaling all conductances
> **Proof.** Multiplying every conductance by $\alpha>0$ multiplies the spanning-tree coefficient by $\alpha^{n-1}$. The potential of a grade-one form uses component $M_{n-2}$, so its numerator gains the factor $\alpha^{n-2}$. Hence
>
> $$
> N_{\alpha L}(f)=\alpha^{-1}N_L(f)
> $$
>
> Differentiating at $\alpha=1$ gives
>
> $$
> \sum_{k<l}c_{kl}\frac{\partial N_L(f)}{\partial c_{kl}}=-N_L(f)
> $$
>
> By definition (2), this is (7). It suffices to sum over existing edges. $\square$

The chosen normalization of influence therefore also decomposes the metric quantity. For $f=[v]^2$, this is a nonnegative distribution of the norm; for $f=\{v,u\}/2$, it is a signed distribution of the inner product.

## Three independent probes on a triangle

Take a unit triangle and again measure $f=[(ac)]^2$. Initially $N(f)=2/3$; the effective resistance between the endpoints of any edge is also $2/3$. In each probe, increase one conductance from $1$ to $2$ and leave the others unchanged.

![Independent probes of the triangle edges](<images/Influence Field on a Triangle.svg>)

*Each diagram is obtained from the same initial unit triangle. Color marks the single strengthened edge. Below each diagram are the new value of the form, the finite influence, and the metric distribution coefficient.*

| Changed edge | New value $N'(f)$ | Influence $\Delta_{kl}(1;f)$ | Coefficient $m_{kl}(f)$ |
|---|---:|---:|---:|
| $ab$ | $3/5$ | $-1/15$ | $1/9$ |
| $bc$ | $3/5$ | $-1/15$ | $1/9$ |
| $ac$ | $2/5$ | $-4/15$ | $4/9$ |

By (4), here $\Delta_{kl}(1;f)=-3m_{kl}/5$. We obtain

$$
D_L([(ac)]^2)=\frac19[(ab)]^2+\frac19[(bc)]^2+\frac49[(ac)]^2
$$

The coefficients sum to $2/3$, as predicted by (7). The finite influences sum to $-2/5$, which is not the original value of the form. Nor does their sum describe strengthening all edges at once: independent finite changes generally cannot be added.

### Value of the output form

The sum of coefficients differs from the metric evaluation of the assembled result:

$$
N_L(D_L(f))=\sum_{k<l}m_{kl}(f)R_{kl}
$$

On the unit triangle this is $\frac23\cdot\frac23=4/9$, whereas the coefficient sum is $2/3$. The operator retains the original number as the sum of metric contributions; its definition does not require $N_L(D_L(f))=N_L(f)$.

## Computation and origin of the formulas

The probing procedure explains what the coefficients mean. Computing the entire distribution does not require rebuilding the graph for each edge. Formula (5) uses inner products of the input vectors with the edges. They can be obtained from the Green matrix, or by solving one Laplacian system for a square and two for a mixed form. Formula (4) then gives the finite influence of a selected coupling if its initial effective resistance is known.

For $[v]^2$, the coefficients $c_{kl}(v\cdot a_{kl})^2$ have the classical electrical interpretation of edge energy contributions for a prescribed vector of external currents. Conductance derivatives follow from differentiating the inverse matrix; the method and electrical interpretation are described by Ghosh, Boyd, and Saberi, [Minimizing Effective Resistance of a Graph](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf), Sections 2.9 and 3.2. The sum formula is also Euler's identity for a homogeneous function of degree $-1$.

The polyform derivation through $M(e+tp)$ connects these known results to potential normalization and the assembly of a sensitivity field into the form $D_L(f)$.

The numerical examples were checked in exact rational arithmetic. Independent comparisons used inversion of the reduced Laplacian, enumeration of spanning trees and separating forests, and finite probes for squares and mixed forms. Reproducible calculations are available in the [checks for this note](https://github.com/magin67/pmg-notes/tree/v5/checks/metric-distributions).

Application to the common segment of two paths: [[Path Intersection as an Influence Field on a Tree]].

Reading route and scope: [[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distributions and Edge Influence|Metric Distributions and Edge Influence]].
