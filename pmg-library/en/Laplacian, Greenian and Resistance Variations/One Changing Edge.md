---
title: One Changing Edge
date: 2026-10-31
updated: 2026-11-01
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: variations-one-changing-edge
lang: en
description: From strengthening a triangle edge to exact variations of the spanning-tree coefficient and resistances. A derivation through one exterior Laplacian exponential factor, forest potentials, and their normalization.
order: 1
translated_revision: 5
---

[[ru/Вариации лапласиана, гриниана и резистенсов/Одна изменяемая связь|Русский]]

We change the conductance of one edge. How does the spanning-tree coefficient change? How do resistances between vertices change, including those between the endpoints of other edges? We begin with a direct calculation, then derive general formulas from one added factor of the Laplacian exponential.

## Example - strengthening one edge of a triangle

For a graph consisting of one edge of conductance $c>0$, the answer is simple: $\tau=c$, $R_{12}=1/c$. After changing the conductance by $t$, where $c+t>0$, we have $\tau'=c+t$, $R'_{12}=1/(c+t)$.

A triangle provides an alternative path. Take $c_{12}=c_{13}=c_{23}=1$ and increase only $c_{12}$ to $2$. Keep all vertices and the other two conductances fixed.

![The original unit triangle and the triangle after increasing the conductance of edge 12 to 2](<images/Strengthening One Edge of a Triangle.svg>)

*Numbers beside edges denote conductances. The strengthened edge is distinguished by color and thickness; vertex labels are unchanged.*

The original triangle has three spanning trees of weight $1$, so $\tau=3$. After the change, their weights are $2,2,1$, and $\tau'=5$.

Vertices $1$ and $2$ are joined by parallel paths with resistances $1/2$ and $2$. Between $1$ and $3$, the parallel paths have resistances $1$ and $3/2$. Hence

$$
R'_{12}=\frac{(1/2)\cdot2}{1/2+2}=\frac25,
\qquad
R'_{13}=R'_{23}=\frac{1\cdot(3/2)}{1+3/2}=\frac35
$$

| Quantity | Before | After | Increment |
|---|---:|---:|---:|
| $c_{12}$ | $1$ | $2$ | $1$ |
| $\tau$ | $3$ | $5$ | $2$ |
| $R_{12}$ | $2/3$ | $2/5$ | $-4/15$ |
| $R_{13},R_{23}$ | $2/3$ | $3/5$ | $-1/15$ |

One conductance changed, but all three resistances decreased. In particular, $R'_{12}=2/5$ differs from the resistance $1/c'_{12}=1/2$ of the strengthened edge itself: effective resistance accounts for the entire network.

> [!example] The same triangle under an arbitrary change
> If $c'_{12}=1+t$, $t\ge-1$, direct calculation gives
>
> $$
> \tau'=3+2t,\qquad
> R'_{12}=\frac2{3+2t},\qquad
> R'_{13}=R'_{23}=\frac{2+t}{3+2t}
> $$
>
> At $t=-1$, edge $12$ is removed: the remaining path $1-3-2$ has $\tau'=1$, $R'_{12}=2$, and $R'_{13}=R'_{23}=1$.

## Data needed for a general graph

Let the original graph be connected and undirected, with fixed vertices $a_1,\ldots,a_n$, $n\ge2$. All conductances are nonnegative. Connectedness and bridges are determined by edges of positive conductance; zero conductance means that the coupling is absent. We change only the coupling $kl$:

$$
c'_{kl}=c_{kl}+t,\qquad t\ge-c_{kl}
$$

A prime denotes the new value, and $\Delta$ the difference between the new and original values. The parameter $t$ is a finite increment; it need not be small. All unprimed quantities below refer to the original graph.

> [!info] Data for calculating the variation
> For the measured pair $ij$ and the varied pair $kl$, use the vectors $a_{ij}=a_j-a_i$, $a_{kl}=a_l-a_k$ and their inner product in the original resistance metric:
>
> $$
> g_{ij,kl}=a_{ij}\cdot a_{kl}
> =\frac{R_{il}+R_{jk}-R_{ik}-R_{jl}}2
> $$
>
> In particular, $a_{ij}^2=R_{ij}$ and $g_{kl,kl}=R_{kl}$. Reversing the orientation of one pair changes the sign of $g_{ij,kl}$ but preserves its square.

> [!info] Two working formulas
> Recall the response formulas that will be derived below from the exponential factor:
>
> $$
> \boxed{\Delta\tau=t\tau R_{kl}}
> \tag{1}
> $$
>
> $$
> \boxed{
> \Delta R_{ij}=-\frac{t}{1+tR_{kl}}\,g_{ij,kl}^{\,2}
> }
> \tag{2}
> $$

Formula (1) remains valid if connectedness is lost. Formula (2) requires $1+tR_{kl}>0$; for nonnegative final conductances, this is precisely the condition that connectedness be preserved. These results are known from [[Variation of a Single Edge|the matrix treatment of a single variation]]. Here we obtain them through products of forms, explicitly accounting for the changing normalization.

For the triangle in the example, $R_{12}=2/3$, $g_{12,12}=2/3$, $g_{13,12}=1/3$. At $t=1$, the formulas give

$$
\Delta\tau=1\cdot3\cdot\frac23=2,\qquad
\Delta R_{12}=-\frac{4/9}{5/3}=-\frac4{15},\qquad
\Delta R_{13}=-\frac{1/9}{5/3}=-\frac1{15}
$$

## Variation as adding a factor

The Laplacian polyform and its exterior exponential are

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,
\qquad
M=\exp L=\sum_{r=0}^{n-1}M_r,
\qquad M_r=\frac{L^r}{r!}
$$

Here $e=M_0$ is the unit form. Multiplication takes place in polyform algebra; the matrix exponential uses a different multiplication. The required rules and forest expansion are established in [[Laplacian Exponential]].

Set $p=[a_{kl}]^2$. Repeating a vector in an exterior product gives zero, so $p^2=0$. Quadratic forms commute.

> [!info] One additional factor
> **Proposition.** For any real $t$, the algebraic variation $L'=L+tp$ gives
>
> $$
> \boxed{M'=M(e+tp)}
> \tag{3}
> $$
>
> Grade by grade, with $1\le r\le n-1$,
>
> $$
> M'_0=e,\qquad
> M'_r=M_r+tM_{r-1}p
> $$
>
> A graph interpretation retains the condition $c_{kl}+t\ge0$.

> [!note]- Proof
> **Proof.** Commutativity gives $\exp(L+tp)=\exp L\,\exp(tp)$, while $p^2=0$ gives $\exp(tp)=e+tp$. Multiplication in $Mp$ raises the grade by one, yielding the formula for $M'_r$. $\square$

Adding a factor increases the coefficient of a fixed form, including when the edge is already present:

$$
(e+c_{kl}p)(e+tp)=e+(c_{kl}+t)p
$$

In particular, when the edge is removed with $t=-c_{kl}$, the two factors give $e$. This is an exact finite change, not a truncated expansion in a small parameter.

## Extracting the spanning-tree coefficient from the factor

We extract the coefficient using the same spanning-tree form $T_n=[(a_1\ldots a_n)]^2$ before and after the change. Recall the definitions in [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|the description of the top-grade coefficient]] and [[Laplacian Exponential#The potential of a form|the definition of a potential]].

> [!info] The top-grade coefficient and the potential of a form
> **Definition.** For a boundary polyform $P$, the functional $\tau(P)$ is defined by
>
> $$
> P_{n-1}=\tau(P)T_n
> $$
>
> The potential of a form $f$ relative to $M$ is $u_M(f)=\tau(Mf)$. For the metric polyform, $\tau(M)=\tau$ is the weighted spanning-tree sum, and $u_M(e)=\tau$.

The functional $\tau(P)$ is linear. Thus (3) immediately gives a general rule for any fixed form $f$:

> [!info] Linear variation of a potential
> **Lemma.** When one coupling changes,
>
> $$
> \boxed{u_{M'}(f)=u_M(f)+t\,u_M(fp)}
> \tag{4}
> $$

> [!note]- Proof
> **Proof.** Multiply (3) by $f$ and extract the top-grade coefficient: $\tau(M'f)=\tau(Mf)+t\tau(Mfp)$. This equality does not require the final graph to be connected. $\square$

By [[Laplacian Exponential#Agreement with the resistance metric|the metric identity]] for the original connected graph,

$$
u_M([a_{kl}]^2)=\tau R_{kl}
$$

> [!info] The spanning-tree coefficient after the change
> **Corollary.** For $t\ge-c_{kl}$,
>
> $$
> \boxed{\tau'=\tau(1+tR_{kl})}
> $$
>
> The final graph is connected if and only if $1+tR_{kl}>0$.

> [!note]- Proof
> **Proof.** Set $f=e$ in (4): $\tau'=\tau+t\,u_M(p)=\tau+t\tau R_{kl}$. This gives (1). For nonnegative conductances, positivity of $\tau'$ is equivalent to the existence of a spanning tree. Since the original $\tau>0$, this is equivalent to $1+tR_{kl}>0$. $\square$

## How normalization gives the resistance variation

For the measured pair $ij$, set $f=[a_{ij}]^2$ and write

$$
m_{ij}=u_M(f)=\tau R_{ij}
$$

The number $m_{ij}$ is the sum of the weights of spanning two-component forests separating $i$ and $j$. Indeed, in grade $M_{n-2}$, adding the vector $a_{ij}$ completes precisely those forests whose endpoints lie in different components to the spanning-tree form. Each such forest contributes coefficient $1$ to $T_n$; if the endpoints lie in the same component, the exterior product vanishes. The combinatorial correspondence is detailed in [[Variation of a Single Edge#Weights of separating spanning forests|the forest formula for resistance]].

The product of the measured and varied forms is

$$
fp=[a_{ij}a_{kl}]^2
$$

The brackets contain the exterior product of two vectors. Its norm is given by the Gram determinant:

$$
(a_{ij}a_{kl})^2
=R_{ij}R_{kl}-g_{ij,kl}^{\,2}
$$

The underlying construction is [[Metric of Higher-Grade Objects|the exterior extension of the resistance metric]].

> [!info] Variation of the unnormalized forest potential
> **Corollary.** Including when a bridge is removed,
>
> $$
> \boxed{
> m'_{ij}=m_{ij}+t\tau
> \bigl(R_{ij}R_{kl}-g_{ij,kl}^{\,2}\bigr)
> }
> \tag{5}
> $$

> [!note]- Proof
> **Proof.** The metric identity for the original graph gives $u_M(fp)=\tau(a_{ij}a_{kl})^2$. Substitute the Gram determinant into (4). For $n=2$, the two vectors are dependent, so $fp=0$ and the determinant also vanishes. Connectedness of the new graph was not used to calculate $m'_{ij}$. $\square$

Now assume that connectedness is preserved. The new resistance requires division by the **new** spanning-tree coefficient:

> [!info] Finite resistance variation
> **Corollary.** If $1+tR_{kl}>0$, then for every pair $ij$,
>
> $$
> \boxed{
> R'_{ij}=R_{ij}-\frac{t}{1+tR_{kl}}\,g_{ij,kl}^{\,2}
> }
> $$

> [!note]- Proof through normalization
> **Proof.** Divide (5) by $\tau'=\tau(1+tR_{kl})$:
>
> $$
> \begin{aligned}
> R'_{ij}
> &=\frac{R_{ij}+t(R_{ij}R_{kl}-g_{ij,kl}^{\,2})}{1+tR_{kl}}\\
> &=R_{ij}-\frac{t\,g_{ij,kl}^{\,2}}{1+tR_{kl}}
> \end{aligned}
> $$
>
> Subtracting $R_{ij}$ gives (2). $\square$

The polyform $M'$, each of its grades, and each fixed potential depend linearly on $t$. Resistance depends on it through a fractional-linear function: both the numerator $m'_{ij}$ and the denominator $\tau'$ change. For example, in the triangle, $m'_{12}=2$, $m'_{13}=m'_{23}=2+t$, and the common denominator is $3+2t$.

## Sensitivity and resistance preservation

> [!info] The differential limit
> **Corollary.** At the original connected state,
>
> $$
> \frac{\partial\tau}{\partial c_{kl}}=\tau R_{kl},\qquad
> \boxed{\frac{\partial R_{ij}}{\partial c_{kl}}=-g_{ij,kl}^{\,2}}
> $$
>
> At $c_{kl}=0$, the class of nonnegative conductances uses the right derivative.

> [!note]- Proof
> **Proof.** Divide (1) and (2) by $t$ and take the limit $t\to0$. For an existing edge, sufficiently small changes in either direction are admissible. $\square$

The denominator in (2) is positive. Strengthening a coupling therefore cannot increase resistances, and weakening it cannot decrease them. If $g_{ij,kl}=0$, the measured resistance is preserved under every admissible finite change of this coupling that preserves connectedness. For nonzero $t$, this condition is also necessary.

The inner product has an electrical meaning: with unit current entering at $l$ and leaving at $k$, it equals the potential difference $\varphi_j-\varphi_i$. Sensitivity is therefore minus the square of the transfer voltage. Electrical potentials $\varphi_i$ differ from the potential of a form $u_M(f)$.

For the endpoints of the varied edge, the formula simplifies to

$$
R'_{kl}=\frac{R_{kl}}{1+tR_{kl}},\qquad
\frac1{R'_{kl}}=\frac1{R_{kl}}+t
$$

## Edge removal and the boundary of applicability

To remove an existing edge with $c_{kl}>0$, set $t=-c_{kl}$ and obtain

$$
\tau'=\tau(1-c_{kl}R_{kl})
$$

> [!info] Removing a bridge
> **Corollary.** An edge $kl$ is a bridge if and only if $c_{kl}R_{kl}=1$. Removing it gives $\tau'=0$. If the edge is not a bridge, then $c_{kl}R_{kl}<1$, and the finite resistance formula remains applicable all the way to removal.

> [!note]- Proof
> **Proof.** Removing a bridge disconnects the graph, so $\tau'=0$. Removing a non-bridge leaves a spanning tree of positive weight, so $\tau'>0$. Substitute these two cases into the formula for $\tau'$. $\square$

Upon removal of a bridge, resistances between components cease to be finite; (2) cannot be extended to this boundary by division by zero. The polyform and unnormalized forest-potential formulas remain valid. The exterior exponential itself remains invertible as a polyform because its grade-zero term is $e$; this invertibility differs from nondegeneracy of the Laplacian on the zero-sum space.

## Independent verification and provenance of the formulas

The matrix description uses $\mathbf L$, $\mathbf{Gr}=\mathbf L^+$, and the coordinate column $\mathbf a_{kl}=\mathbf e_l-\mathbf e_k$. It provides an independent check of the factor derivation.

> [!note]- Verification by matrix inversion
> **Proof.** The Laplacian is invertible on $\mathbf1^\perp$. The update $t\mathbf a_{kl}\mathbf a_{kl}^{\mathsf T}$ has rank at most one. The determinant formula gives $\tau'/\tau=1+tR_{kl}$; the Sherman-Morrison formula, when its denominator is nonzero, gives
>
> $$
> \mathbf{Gr}'=\mathbf{Gr}
> -\frac{t}{1+tR_{kl}}
> \mathbf{Gr}\mathbf a_{kl}\mathbf a_{kl}^{\mathsf T}\mathbf{Gr}
> $$
>
> The determinant ratio on $\mathbf1^\perp$ equals the ratio of spanning-tree coefficients: the common factor $n$ cancels. Multiplying the Greenian identity by $\mathbf a_{ij}^{\mathsf T}$ on the left and $\mathbf a_{ij}$ on the right yields (2), since $\mathbf a_{ij}^{\mathsf T}\mathbf{Gr}\mathbf a_{kl}=g_{ij,kl}$. $\square$

The spanning-tree and resistance update formulas are instances of known rank-one perturbation identities. Their matrix treatment and references are given in [[Variation of a Single Edge]] and [[Further Reading for the PMG Introductory Series]]. Established properties of effective resistances and their dependence on conductances are also discussed by Ghosh, Boyd, and Saberi [1].

The derivation in this note connects these results with the factor $e+t[a_{kl}]^2$, linear changes of grades, and normalization of potentials. Providing this derivation does not establish scientific priority.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_single_edge.py) compares factor expansion in every grade, direct enumeration of trees and separating two-component forests, and matrix inversion. Checks use exact rational arithmetic on a weighted edge, unit and weighted triangles, the path $P_4$, and a weighted cycle $C_4$. They cover strengthening, weakening, adding a missing edge, and removal, including bridges. These checks supplement the proofs.

From the repository root:

    python checks/variations/verify_single_edge.py

Joint action of factors, mixed terms, and updating the metric during sequential changes are treated in [[Two Edges and Joint Variation]]. Matrix formulas are also given in [[Varying several couplings together]].

1. Ghosh A., Boyd S., Saberi A. *Minimizing Effective Resistance of a Graph*. SIAM Review, 50(1), 2008, 37-66. [Article](https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf), [DOI](https://doi.org/10.1137/050645452).

Reading order and summary of results: [[en/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
