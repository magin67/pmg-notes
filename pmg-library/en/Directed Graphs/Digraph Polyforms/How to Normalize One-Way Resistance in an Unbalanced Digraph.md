---
title: How to Normalize One-Way Resistance in an Unbalanced Digraph
date: 2026-11-21
updated: 2026-11-21
revision: 1
translated_revision: 3
status: published
text_prepared_by: ChatGPT
lang: en
translation_key: one-way-resistance-normalization-digraph
order: 4
description: Normalization by total rooted potential, additivity for opposite directions and examples ranging from an undirected edge to a path with one sink.
---

When the rooted potentials are $5,4,7$, what divides the measurement for $(ab)$? This series takes **the sum of the measurement coefficients over all roots, divided by the sum of the rooted potentials**. Here the denominator is 16 for both directions and for the symmetric pair resistance.

## One rule for every pair

Take a loopless digraph on $n\ge2$ vertices $a_1,\ldots,a_n$ with nonnegative weights. Laplacian rows correspond to arc tails. Let $M=\exp L$ in the polyform algebra, with unit $e$. To measure the direction from $a_i$ to $a_j$, the left argument points from the centroid of all vertices to $a_j$, and the right argument from $a_i$ to $a_j$. [[en/Directed Graphs/Digraph Polyforms/The Arc Form and the One-Way Resistance Form#Multiplication by the one-way resistance form|Multiplication by the one-way resistance form]]

$$
\Phi_{ij}=\left[a_j-\frac{a_1+\cdots+a_n}{n},\,a_j-a_i\right]
$$

For each $a_k$ multiply $MF$ by $[a_k]^2$. Write $u_k(F)$ for the coefficient of $[a_1\wedge\cdots\wedge a_n]^2$ in the product. At $F=e$ we obtain $\tau_k=u_k(e)$, the total weight of spanning trees directed toward $a_k$. [[en/Directed Graphs/Digraph Polyforms/Computing a Rooted Spanning-Tree Potential from a Digraph Polyform|Computing a Rooted Spanning-Tree Potential from a Digraph Polyform]]

> [!info] Normalization by total spanning-tree potential
> **Definition.** For $S=\sum_{k=1}^n\tau_k>0$, define the normalized form potential and the one-way resistance of an ordered pair by
>
> $$
> P_M^\Sigma(F)=\frac{\sum_{k=1}^n u_k(F)}{S},
> \qquad r_{ij}=P_M^\Sigma(\Phi_{ij})
> $$
>
> Every root enters the numerator, including a root with $\tau_k=0$.

Add the coefficients first and divide once by $S$. Dividing each $u_k(F)$ by its own $\tau_k$ can be impossible even on a path with one sink. Equal root weights are a choice. Given that choice, $P_M^\Sigma(e)=1$ fixes the denominator. The rule applies precisely when some vertex is reachable from every vertex by positive-weight arcs, so at least one positive-weight spanning tree exists. Otherwise $S=0$ and the rule gives no numerical value. For example, in $b\leftarrow a\to c$ neither sink can leave itself.

## Why the two directions add

The symmetric pair resistance can be computed directly from the quadratic pair form. Put $R_{ij}=P_M^\Sigma([a_j-a_i]^2)$.

> [!info] Additivity
> **Proposition.** For every vertex pair with $S>0$, $r_{ij}+r_{ji}=R_{ij}$.

> [!note]- Proof
> **Proof.** Reversing the pair negates the right argument of $\Phi_{ij}$. On the left the difference of the two vectors from the same centroid is $a_j-a_i$. Thus $\Phi_{ij}+\Phi_{ji}=[a_j-a_i]^2$. Each root coefficient is linear in the measured form and $S$ depends only on the graph. Apply $P_M^\Sigma$ to the identity. $\square$

Additivity follows from using one linear functional for both directions and the symmetric pair. Equal weighting of roots is part of the definition.

## Computing the coefficients with minors

A simple form $F=[x,y]$ has matrix $\mathbf F=\mathbf x\mathbf y^{\mathsf T}$ in vertex coordinates. In $\mathbf L+t\mathbf F$ delete row and column $k$. One determinant supplies two numbers.

$$
\det\!\left((\mathbf L+t\mathbf F)_{\widehat k,\widehat k}\right)
=\tau_k+t\,u_k(F)
$$

Indeed, $F^2=0$, so $\exp(L+tF)=M(e+tF)$. Multiplication by $[a_k]^2$ extracts the principal minor omitting $k$. The constant term and the coefficient of $t$ correspond to the two terms of the polyform. Here $t$ serves only to extract a coefficient.

For a connected balanced graph the $\tau_k$ all equal $\tau$. For $F=\Phi_{ij}$ all $u_k(F)$ also agree. Both $\mathbf L$ and $\mathbf F$ have zero row and column sums, the former by balance and the latter because both arguments are zero-sum. All principal minors of order $n-1$ of $\mathbf L+t\mathbf F$ therefore agree. At rank $n-1$ each row and column of its adjugate is constant. At lower rank all those minors vanish. Compare the coefficients of $t$. The factor $n$ cancels between numerator and denominator and the result is the balanced normalization $u_k(\Phi_{ij})/\tau$.

## Two vertices and a unit cycle

**Two vertices.** Give $a\to b$ weight $p>0$ and $b\to a$ weight $q>0$. Then $\tau_a=q$ and $\tau_b=p$. The centroid is the midpoint, so $\Phi_{ab}=\Phi_{ba}=\tfrac12[(ab)]^2$. For both forms $u_a=u_b=1/2$, giving

$$
r_{ab}=r_{ba}=\frac{1}{p+q}
$$

At $p=q=w$ each direction gives $1/(2w)$ and the pair gives $1/w$. At $p=2$, $q=1$, both shares equal $1/3$. With two vertices the measurement forms already agree, even for unequal arc weights.

**Three vertices.** In the unit cycle $a\to b\to c\to a$ each root has one tree of weight 1, hence $S=3$. Direct multiplication gives $(M\Phi_{ab})_2=\tfrac13[(abc)]^2$ and $(M\Phi_{ba})_2=\tfrac23[(abc)]^2$. Each vertex form preserves the corresponding coefficient. [[en/Directed Graphs/Digraph Polyforms/The Arc Form and the One-Way Resistance Form#Multiplication by the one-way resistance form|Multiplication by the one-way resistance form]]

$$
r_{ab}=\frac{1/3+1/3+1/3}{3}=\frac13,
\qquad
r_{ba}=\frac{2/3+2/3+2/3}{3}=\frac23
$$

From $a$ to $b$ the walk makes one transition and from $b$ to $a$ it makes two. At unit rates each transition takes one unit of time on average. Dividing the mean times by three checks the result for this balanced graph. The two shares sum to $R_{ab}=1$. [[en/Directed Graphs/Balanced graphs/One-Way Resistance and Hitting Times#Markov interpretation|Markov interpretation]]

## Three distinct rooted potentials

![An unbalanced digraph on three vertices with arc weights](./images/weighted-unbalanced-digraph.svg)

*Fig. 1. In the running example $b\to a$ and $a\to c$ have weight 2 and the remaining four arcs have weight 1.*

In vertex order $a,b,c$ the Laplacian and its principal minors are

$$
\mathbf L=
\begin{pmatrix}3&-1&-2\\-2&3&-1\\-1&-1&2\end{pmatrix},
\qquad (\tau_a,\tau_b,\tau_c)=(5,4,7)
$$

For example, consider root $b$ when measuring $(ab)$. The left coordinate column of $\Phi_{ab}$ is $(-1,2,-1)^{\mathsf T}/3$ and the right column is $(-1,1,0)^{\mathsf T}$. Delete row and column $b$ to get

$$
\det\begin{pmatrix}3+t/3&-2\\-1+t/3&2\end{pmatrix}
=4+\frac{4t}{3}
$$

Thus $\tau_b=4$ and $u_b(\Phi_{ab})=4/3$. Repeat for all roots. In the last row measure the quadratic form $[(ab)]^2$ directly.

| Measured form | $u_a$ | $u_b$ | $u_c$ | Sum | Divided by $16$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $\Phi_{ab}$ | $1$ | $4/3$ | $5/3$ | $4$ | $1/4$ |
| $\Phi_{ba}$ | $1$ | $2/3$ | $4/3$ | $3$ | $3/16$ |
| $[(ab)]^2$ | $2$ | $2$ | $3$ | $7$ | $7/16$ |

Hence $r_{ab}=1/4$ and $r_{ba}=3/16$. The two directions add in every root column and after normalization. Their sum, $7/16$, agrees with the independent measurement of $[(ab)]^2$.

What if we used only the target's potential? For $(ab)$ we would get $(4/3)/4=1/3$ and for $(ba)$ we would get $1/5$. Their sum $8/15$ differs from $7/16$ because reversing direction changes the root used for the measurement.

## A directed path with a single sink

In the unit path $a\to b\to c\to d$ all three arcs form the only spanning tree and its root is $d$. Thus $(\tau_a,\tau_b,\tau_c,\tau_d)=(0,0,0,1)$ and $S=1$. The last column is the sum of the four coefficients.

| Direction | $u_a$ | $u_b$ | $u_c$ | $u_d$ | $r_{ij}$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $(bc)$ | $0$ | $-1/4$ | $0$ | $1/4$ | $0$ |
| $(cb)$ | $0$ | $1/4$ | $0$ | $3/4$ | $1$ |
| $(ad)$ | $3/4$ | $3/4$ | $3/4$ | $3/4$ | $3$ |
| $(da)$ | $1/4$ | $1/4$ | $1/4$ | $1/4$ | $1$ |

For $(bc)$ the contribution from root $b$ is $-1/4$ although $\tau_b=0$. It cancels the sink contribution and $r_{bc}=0$ for two distinct vertices. Keeping only the root of positive potential would miss this cancellation. The reverse value is $r_{cb}=1$, giving $R_{bc}=1$.

The endpoints give $r_{ad}=3$ and $r_{da}=1$. There is no path from $d$ to $a$, yet the latter measurement is finite. This normalization preserves additivity and extends the balanced formula. Strict positivity for distinct vertices and the hitting-time interpretation need additional hypotheses.

The arc $b\to c$ gives zero in one cell of the table. Recovering its weight from the entire table and the rooted potentials requires reconstructing the Laplacian rows. [[en/Directed Graphs/Digraph Polyforms/Can the One-Way Resistance Matrix Recover a Digraph|Can the One-Way Resistance Matrix Recover a Digraph?]]

[[ru/Направленные графы/Полиформы орграфов/Как нормировать односторонний резистенс в небалансовом орграфе|Русский]]
