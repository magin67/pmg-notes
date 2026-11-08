---
title: The Influence Field on Graphs with Cycles
date: 2026-11-03
updated: 2026-11-08
revision: 2
status: draft
text_prepared_by: ChatGPT
lang: en
translated_revision: 5
translation_key: metric-distributions-cycle-influence
order: 3
description: "Distributions of norms and inner products on a triangle and a square: electrical flows, signs, finite probes, and a cross-edge with zero influence."
---

[[ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/Поле влияния на графах с циклами|Русский]]


On a tree, the influence field of two vectors specified by vertex pairs selects the common segment of their unique paths. On a graph with cycles, different paths can be chosen between vertices. The operator $D_L$ is still uniquely defined: its coefficients are evaluated in the metric of the entire network. We examine what replaces path intersection and how to interpret the result.

We use the definition in [[Edge Influence and Metric Distribution]] and the tree case in [[Path Intersection as an Influence Field on a Tree]]. All graphs are finite, connected, and undirected, with positive conductances on existing edges. The input form is fixed as the metric changes.

## From a unique path to electrical flow

Give edge $\ell$ an auxiliary orientation $i\to j$, and set $a_\ell=a_j-a_i$, $q_\ell=[a_\ell]^2$, and $r_\ell=1/c_\ell$. We measure $f=\{v,u\}/2$, where $\{v,u\}=[v,u]+[u,v]$ and $N_L(f)=v\cdot u$. Recall:

$$
D_L(f)=\sum_\ell m_\ell(f)q_\ell,\qquad
m_\ell(f)=c_\ell(v\cdot a_\ell)(u\cdot a_\ell)
$$

For $v=(st)$, consider an electrical experiment: a unit current enters at $s$ and leaves at $t$. Denote the edge current in the chosen orientation by $I_\ell(v)$. The network laws give

$$
I_\ell(v)=c_\ell(v\cdot a_\ell)
$$

On a tree these are the values $1,-1,0$ marking the unique path. On a cycle, current splits between routes. Its magnitude and direction depend on all conductances.

> [!info] Distribution through two flows
> **Proposition.** For two separate electrical experiments with vectors $v$ and $u$,
>
> $$
> \boxed{m_\ell(f)=r_\ell I_\ell(v)I_\ell(u)},\qquad
> \boxed{\sum_\ell m_\ell(f)=v\cdot u}
> \tag{1}
> $$
>
> For $u=v$, the contributions $r_\ell I_\ell(v)^2$ to the norm $v^2$ are nonnegative. For different vectors, the contribution's sign is determined by the relative directions of the two currents on the edge.

The energy identity and the electrical interpretation of effective resistance are classical; see Ghosh, Boyd, and Saberi, [Minimizing Effective Resistance of a Graph](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf), Sections 2.2 and 3.2. Here their polarization is expressed as a metric distribution in PMG.

> [!note]- Derivation using network potentials
> **Proof.** Let $\mathbf v$ be the coordinate column of $v=(st)$. It has $-1$ at $s$ and $+1$ at $t$. Electrical potentials therefore satisfy $\mathbf L\boldsymbol\varphi_v=-\mathbf v$. We may take $\boldsymbol\varphi_v=-\mathbf{Gr}\mathbf v$. By Ohm's law,
>
> $$
> I_\ell(v)=c_\ell(\varphi_{v,i}-\varphi_{v,j})=c_\ell(v\cdot a_\ell)
> $$
>
> Substitution into the definition gives the first formula in (1). The sum of products of potential drops is
>
> $$
> \sum_\ell r_\ell I_\ell(v)I_\ell(u)
> =\boldsymbol\varphi_v^{\mathsf T}\mathbf L\boldsymbol\varphi_u
> =\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u
> $$
>
> The last quantity is $v\cdot u$. $\square$

For the mixed form, an edge coefficient is nonzero if and only if both flows are nonzero on it. This retains the idea of shared edge participation, now for two electrical flows. No decomposition into selected simple paths is needed. Reversing an auxiliary edge orientation negates both currents and preserves the coefficient; reversing one input vector negates the whole distribution.

## Triangle and the contributions to effective resistance

On a unit triangle, take $v=(ac)$ and $f=[v]^2$. Between $a$ and $c$, the direct route has resistance $1$ and route $a-b-c$ has resistance $2$. They are in parallel, so the currents are $2/3$ and $1/3$, respectively.

![Currents and coefficients on unit and weighted triangles](<images/Two Routes in a Triangle.svg>)

*Arrows show current from $a$ to $c$. Each edge is labeled with its current $I$ and coefficient $m=rI^2$. On the left all conductances are one; on the right the conductance of $ac$ has increased to $2$, with the others unchanged. The right-hand distribution is recomputed in the changed metric.*

For the unit triangle,

$$
D_L([(ac)]^2)=\frac19q_{ab}+\frac19q_{bc}+\frac49q_{ac},\qquad R_{ac}=\frac23
$$

The direct route contributes $(2/3)^2\cdot1=4/9$, and the other route contributes $(1/3)^2\cdot2=2/9$. Their sum is $2/3$. Thus effective resistance is assembled from segment resistances multiplied by the squares of their currents. Simply adding the lengths of both routes would give a different number.

Increasing $c_{ac}$ to $2$ makes the direct edge's resistance $1/2$. Currents redistribute: $4/5$ along $ac$ and $1/5$ along each edge of the other route. For the new Laplacian $L'$,

$$
D_{L'}([(ac)]^2)=\frac1{25}q_{ab}+\frac1{25}q_{bc}+\frac8{25}q_{ac},\qquad R'_{ac}=\frac25
$$

Although the current through $ac$ has increased, its contribution to the norm has decreased from $4/9$ to $8/25$: the edge resistance has decreased as well. A distribution coefficient should not be identified with current magnitude. Strengthening one edge has also changed the coefficients of the other edges.

## Square with a zero inner product and a nonzero field

Let $a,b,c,d$ occur consecutively around a unit square. For $v=(ac)$, current splits equally between routes $a-b-c$ and $a-d-c$. Hence

$$
D_L([(ac)]^2)=\frac14(q_{ab}+q_{bc}+q_{cd}+q_{ad}),\qquad R_{ac}=1
$$

Now keep $v=(ac)$, take $u=(bd)$, and measure the mixed form $f=\{v,u\}/2$. The second flow also splits equally, but its directions relative to the first flow differ from edge to edge.

![Two flows on a square and the signs of their metric contributions](<images/Two Flows and Signs on a Square.svg>)

*The left and middle panels show two separate unit-current experiments: $a\to c$ and $b\to d$. Every edge current has magnitude $1/2$. The right panel shows products of the two currents and the resistance: matching directions give $+1/4$, opposite directions give $-1/4$. All conductances are positive and equal to $1$.*

Choose auxiliary orientations $a\to b$, $b\to c$, $c\to d$, and $a\to d$:

| Edge | $I_\ell(v)$ | $I_\ell(u)$ | $m_\ell(f)$ |
|---|---:|---:|---:|
| $ab$ | $1/2$ | $-1/2$ | $-1/4$ |
| $bc$ | $1/2$ | $1/2$ | $1/4$ |
| $cd$ | $-1/2$ | $1/2$ | $-1/4$ |
| $ad$ | $1/2$ | $1/2$ | $1/4$ |

We obtain

$$
D_L(f)=\frac14(-q_{ab}+q_{bc}-q_{cd}+q_{ad})\ne0,\qquad v\cdot u=0
$$

The inner product is zero because positive and negative contributions cancel. Every edge nevertheless influences the form. This differs substantially from the tree case: for two vectors specified by vertex pairs, the nonzero contributions along the common segment all have one sign, and a zero sum means there are no common edges.

## Checking by finite conductance changes

The coefficient $m_\ell=-c_\ell\partial N_L(f)/\partial c_\ell$ describes relative sensitivity. For a finite probe $c_\ell\mapsto(1+\varepsilon)c_\ell$, the [[Edge Influence and Metric Distribution#From finite influence to distribution coefficients|relation between finite influence and the distribution]] gives

$$
\boxed{\Delta_\ell(\varepsilon c_\ell;f)=-\frac{\varepsilon}{1+\varepsilon c_\ell R_\ell}m_\ell(f)}
\tag{2}
$$

Here $R_\ell$ is the effective resistance between the edge's endpoints in the full initial network; the final conductance must be nonnegative and the graph must remain connected. On a tree, $c_\ell R_\ell=1$. When an alternative route exists, $R_\ell<1/c_\ell$, so the factor in (2) differs from its tree value. It can also differ between edges of one graph.

### Mixed form: initial value zero

On the unit square, $R_\ell=3/4$ for every edge. Independently doubling a conductance gives $\Delta_\ell=-4m_\ell/7$. For the mixed form of the diagonal vectors, whose initial value is zero:

| Conductance doubled | New value $N'(f)=\Delta_\ell$ |
|---|---:|
| $ab$ or $cd$ | $1/7$ |
| $bc$ or $ad$ | $-1/7$ |

Each row denotes a separate probe from the initial square. Strengthening an edge with a negative coefficient increases the value of the form; strengthening one with a positive coefficient decreases it.

### Vector norm: initial value one

Now fix $f=[(ac)]^2$ with $N_L(f)=1$.

Finite effects of different edges generally interact. For example, on the square with $f=[(ac)]^2$, doubling either $ab$ or $bc$ separately gives a change of $-1/7$. After both are doubled simultaneously, the two route resistances are $1$ and $2$, and the new effective resistance is $2/3$. Adding the independent initial probes would incorrectly give $1-1/7-1/7=5/7$. Linear addition of first derivatives remains valid for an infinitesimal joint change.

![Independent and Simultaneous Changes](<images/Independent and Simultaneous Changes.svg>)

*Both separate probes start from the initial square. In the simultaneous change, both conductances are $2$, so the metric must be recomputed.*

## A cross-edge with no influence on the selected form

Add edge $bd$ of conductance $1$ to the unit square and again take $f=[(ac)]^2$. Vertices $b$ and $d$ have equal potentials in this experiment. The cross-edge carries zero current even though it exists and belongs to simple paths such as $a-b-d-c$.

![Zero contribution of a cross-edge between equal-potential vertices](<images/Zero Influence of a Cross-Edge.svg>)

*Edges are labeled with coefficients of the distribution of norm $(ac)^2$. The four sides contribute $1/4$ each, and cross-edge $bd$ contributes zero. The cross-edge is a solid grey line labeled $c=1$, $m=0$. Diagonal $ac$ is not an edge of the graph; it is the selected vector between vertices.*

The distribution over the sides and the value $R_{ac}=1$ are unchanged. Changing only the conductance of $bd$ also has no effect: symmetry keeps the potentials equal for any nonnegative conductance of this cross-edge. The conclusion can change for a different input form or after symmetry is broken.

Thus the support of $D_L$ does not recover the union of all possible simple paths. It shows the edges with nonzero electrical response for the given form. For $[v]^2$, zero contribution means zero current; for $\{v,u\}/2$, zero current in either experiment suffices.

## What changes when the network is refined

The distribution is tied to the existing edges. This can be seen without changing the metric on the old vertices. In a unit triangle, replace edge $ac$ of resistance $1$ by two series edges $ad,dc$, each of resistance $1/2$. The new vertex $d$ is joined by two edges of conductance $2$ each. Its degree in PMG terminology is the sum of conductances, hence $4$.

![Splitting an edge contribution by introducing an intermediate vertex](<images/Edge Subdivision and Distribution.svg>)

*On the left is a unit triangle; on the right is a network equivalent on the old vertices, with an intermediate vertex $d$. Edge labels show coefficients $m$. The old contribution $4/9$ of edge $ac$ splits into two contributions of $2/9$; the sum of all coefficients remains $2/3$.*

The input remains $[(ac)]^2$. Both new segments carry the same current, and their resistances add. Therefore

$$
D_{L'}([(ac)]^2)=\frac19q_{ab}+\frac19q_{bc}+\frac29q_{ad}+\frac29q_{cd}
$$

In general, splitting a resistance in series as $r=r_1+r_2$ divides its former contribution in proportions $r_1/r$ and $r_2/r$. This also holds for a mixed form on the old vertices: the current is the same along the series segments in each experiment, and $m_i=r_iI(v)I(u)$. Combining the labels recovers the former coefficient. The output forms themselves belong to different spaces because of the new vertex, so literal equality is not asserted.

If instead a conductance is split into parallel couplings with the same endpoints, $c=c_1+c_2$, their contributions split in proportions $c_1/c$ and $c_2/c$: the potential drops stay equal. Here the edge forms coincide, and adding them also recovers the original output form.

## Coefficient sum, output evaluation, and computation

Compare the contribution sum $\sum_\ell m_\ell(f)=N_L(f)$ with the [[Edge Influence and Metric Distribution#Value of the output form|output evaluation]] $N_L(D_L(f))=\sum_\ell m_\ell(f)R_\ell$:

| Graph and input form | Coefficient sum $N_L(f)$ | $N_L(D_L(f))$ |
|---|---:|---:|
| Unit triangle, $[(ac)]^2$ | $2/3$ | $4/9$ |
| Triangle with $c_{ac}=2$, $[(ac)]^2$ | $2/5$ | $22/125$ |
| Unit square, $[(ac)]^2$ | $1$ | $3/4$ |
| Unit square, $\{(ac),(bd)\}/2$ | $0$ | $0$ |
| Square with a unit cross-edge $bd$, $[(ac)]^2$ | $1$ | $5/8$ |
| Triangle after subdividing $ac$ in series, $[(ac)]^2$ | $2/3$ | $1/3$ |

Work through the second row. When $c_{ac}=2$, edge $ac$ has its own resistance $r_{ac}=1/2$, whereas its effective resistance in the full network is $R_{ac}=2/5$. The other two vertex pairs have $R_{ab}=R_{bc}=3/5$. Hence

$$
N_L(D_L([(ac)]^2))
=\frac1{25}\left(\frac35+\frac35\right)+\frac8{25}\frac25
=\frac{22}{125}
$$

This evaluation uses network resistances $R$, although the contributions $m$ themselves can be computed as $rI^2$ using the edges' own resistances.

In the mixed-form row both numbers are zero, but the output form is nonzero. One scalar evaluation is insufficient to recover the influence field.

The computational procedure still applies to cycles: solve one Laplacian system for $[v]^2$ or two for $\{v,u\}/2$, obtain the currents, and assemble $r_\ell I_\ell(v)I_\ell(u)$. No enumeration of paths or spanning trees is required. Finite probes additionally require the initial $R_\ell$ in (2). A new metric after a finite change gives a new field; the initial coefficients cannot automatically be carried over to it.

All numerical values were checked in exact rational arithmetic. Comparisons used reduced-Laplacian inversion, independent enumeration of spanning trees and separating forests, electrical calculations for two parallel routes, and direct finite probes. Edge subdivision was also checked for all mixed forms on the old vertices. The [reproducible checks](https://github.com/magin67/pmg-notes/tree/v5/checks/metric-distributions) include additional weighted examples. The formulas rest on classical resistive-network theory.

Distribution of a triangle's norm and the passage from pair contributions to individual-edge influences: [[Metric Distribution in Higher Grades]].

[[en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/Metric Distributions and Edge Influence|Back to Metric Distributions and Edge Influence]].
