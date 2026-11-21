---
title: The Arc Form and the One-Way Resistance Form
date: 2026-11-21
updated: 2026-11-21
revision: 1
translated_revision: 7
status: published
text_prepared_by: ChatGPT
lang: en
translation_key: directed-arc-form-and-one-way-resistance
order: 3
description: Two explicit multiplications on a unit directed three-cycle distinguish the arc form from the centroid form that measures one-way resistance.
---

For an undirected edge the form $[(ab)]^2$ has two uses. Multiplied by the edge weight, it contributes to the Laplacian. Multiplied by the metric polyform, it gives the pair resistance after extracting the normalized spanning-tree coefficient. What does the same calculation give for the arc $a\to b$?

Consider a connected balanced graph, in which the total outgoing and incoming weights agree at each vertex. [[en/Directed Graphs/Digraph Polyforms/Digraph Polyforms|Digraph Polyforms]]

In the unit cycle $a\to b\to c\to a$, one spanning tree of weight 1 leads to each root. All three rooted potentials are 1, so both forms can be tested on the same metric with unit normalization. Multiplication by a vertex form extracts each rooted potential. [[en/Directed Graphs/Digraph Polyforms/Computing a Rooted Spanning-Tree Potential from a Digraph Polyform|Computing a Rooted Spanning-Tree Potential from a Digraph Polyform]]

## The polyform of the directed cycle

Our vector convention is $(ab)=b-a$ and $(ba)=a-b$. A row of the outgoing Laplacian specifies the tail. The unit arc $a\to b$ places $+1$ on the diagonal of row $a$ and $-1$ in column $b$. Its form is

$$
H_{a\to b}=[a,a-b]=[a,(ba)]
$$

The first argument is a vertex. For an undirected edge both arguments are vertex differences. Bilinearity combines two opposite unit arcs into that edge.

$$
[a,(ba)]+[b,(ab)]=[b-a,b-a]=[(ab)]^2
$$

Forms multiply by taking exterior products in both arguments, $[x,y][u,v]=[x\wedge u,y\wedge v]$. The square of an individual arc form vanishes. Hence the Laplacian exponential in the polyform algebra factors as follows, with $e$ denoting the unit.

$$
\begin{aligned}
L&=[a,(ba)]+[b,(cb)]+[c,(ac)]\\
M=\exp L&=(e+[a,(ba)])(e+[b,(cb)])(e+[c,(ac)])
\end{aligned}
$$

The product of the first two arc forms is $[a\wedge b,(abc)]$ because $(a-b)\wedge(b-c)=(abc)$. The other two pairs give $[b\wedge c,(abc)]$ and $[c\wedge a,(abc)]$. Their three left arguments sum to $(abc)=a\wedge b+b\wedge c+c\wedge a$. The product of all three arcs vanishes because the right arguments $a-b,b-c,c-a$ sum to zero. Thus the entire metric polyform is

$$
\boxed{M=e+[a,(ba)]+[b,(cb)]+[c,(ac)]+[(abc)]^2}
$$

Each grade-two term comes from a tree. The path $a\to b\to c$ leads to $c$, and the other pairs lead to $a$ and $b$. In a general digraph, a repeated tail kills a product on the left and a directed cycle kills it on the right. Every surviving path therefore ends at a root. The converse and an unbalanced example follow from the forest expansion. [[en/Directed Graphs/Digraph Polyforms/How Arcs Form the Polyform of a Digraph#Which sets of arcs survive|Which sets of arcs survive]]

## Multiplication by the arc form

Multiply $M$ by $[a,(ba)]$. The unit gives the arc form itself. Two products survive in grade 2.

$$
\begin{aligned}
[a,(ba)][b,(cb)]&=[a\wedge b,(abc)]\\
[c,(ac)][a,(ba)]&=[c\wedge a,(abc)]
\end{aligned}
$$

Grade 3 vanishes since $(abc)\wedge(ba)=0$. For the reverse arc $[b,(ab)]$, only its product with $[c,(ac)]$ survives in grade 2. The right argument of $[a,(ba)]$ is proportional to $(ab)$, and $[b,(cb)]$ repeats $b$ on the left. The two full products are

$$
\begin{aligned}
M[a,(ba)]&=[a,(ba)]+[a\wedge b+c\wedge a,(abc)]\\
M[b,(ab)]&=[b,(ab)]+[b\wedge c,(abc)]
\end{aligned}
$$

Can the first line provide a single coefficient of $[(abc)]^2$? That would require $a\wedge b+c\wedge a$ to be proportional to $(abc)$. Its $b\wedge c$ coefficient is zero, whereas the coefficient in $(abc)$ is one.

The same line gives **three root coefficients**. For root $a$, multiply grade 2 by $[a]^2$ and extract the coefficient of $[a\wedge b\wedge c]^2$. Both left terms contain $a$ and vanish. At $b$ and $c$ one term of coefficient 1 survives. The forward arc gives $(0,1,1)$ and the reverse arc $(1,0,0)$. These are the changes in rooted potentials when one unit is added to the respective arc weight. With arc form $H$, the new polyform is $M(e+H)$ and the increment is $MH$. Summing the two grade-two components gives $[(abc)]^2$ with coefficient 1. How is that value shared between the directions?

## Multiplication by the one-way resistance form

We can measure any ordered pair, including a pair with no direct arc. The right argument points from the starting vertex to the target. The left argument points from the centroid of **all vertices** to that same target. For $a\to b$ on three vertices it is the average of $b-a,b-b,b-c$. In terms of the vertices the two forms are [[en/Directed Graphs/Balanced graphs/One-Way Resistance and Hitting Times#The one-way resistance form|The one-way resistance form]]

$$
\Phi_{ab}=\tfrac13[(ab)+(cb),(ab)],\qquad
\Phi_{ba}=\tfrac13[(ba)+(ca),(ba)]
$$

> [!info] Numerical evaluation
> **Definition.** For a connected balanced graph the one-way resistance is $r_{ij}=P_M(\Phi_{ij})=\tau(M\Phi_{ij})/\tau(M)$. Here $\tau$ extracts the coefficient of the top boundary form of grade $n-1$. Multiplying that form by a root form carries it to grade $n$ with the same coefficient. In this cycle the top boundary form is $[(abc)]^2$ and $\tau(M)=1$.

Only $b\to c$ and $c\to a$ contribute to grade 2 of $M\Phi_{ab}$. On the right, $(cb)\wedge(ab)=(abc)$ and $(ac)\wedge(ab)=-(abc)$. The surviving left arguments therefore combine to $b-c$ before wedging with the centroid vector. Both signs reverse for $\Phi_{ba}$. Hence

$$
\begin{aligned}
(M\Phi_{ab})_2
 &=\tfrac13[(b-c)\wedge((ab)+(cb)),(abc)]
 =\tfrac13[(abc)]^2\\
(M\Phi_{ba})_2
 &=\tfrac13[(c-b)\wedge((ba)+(ca)),(abc)]
 =\tfrac23[(abc)]^2
\end{aligned}
$$

In the first line $(cb)\wedge(cb)=0$, leaving one copy of $(abc)$. In the second, $(bc)\wedge(ba)$ and $(bc)\wedge(ca)$ both equal $(abc)$. Thus the unit directed three-cycle has $r_{ab}=1/3$ and $r_{ba}=2/3$.

A continuous-time walk gives an independent check. With unit arc rates, reaching $b$ from $a$ takes one transition and reaching $a$ from $b$ takes two. Each holding time has mean 1. Dividing the two mean hitting times by the three vertices gives the same values. [[en/Directed Graphs/Balanced graphs/One-Way Resistance and Hitting Times#Markov interpretation|Markov interpretation]]

## Why the Laplacian uses reversed indices

Write $a_i$ for the vertices of a loopless graph, $f_{ij}\ge0$ for the weight of $i\to j$ and $h$ for the centroid of all vertices. Since $\Phi_{ij}=[a_j-h,a_j-a_i]$, each arc satisfies

$$
H_{i\to j}=[a_i,a_i-a_j]
=\Phi_{ji}+[h,a_i-a_j]
$$

> [!info] Index order in the Laplacian
> **Proposition.** For a balanced graph,
>
> $$
> L=\sum_{i\ne j}f_{ij}\Phi_{ji}
> $$
>
> The tail of $i\to j$ becomes the target index of the measurement form $\Phi_{ji}$.

> [!note]- Proof
> **Proof.** Multiply the arc identity by $f_{ij}$ and sum. The correction is $[h,\sum_{i\ne j}f_{ij}(a_i-a_j)]$. Each vertex coefficient on the right is its outgoing weight minus its incoming weight. Under balance all these coefficients vanish. $\square$

In the unit cycle $L=\Phi_{ba}+\Phi_{cb}+\Phi_{ac}$. To change a single weight use $H_{i\to j}$, which changes only row $i$. For an unbalanced graph the total correction involving $h$ remains. [[en/Directed Graphs/Balanced graphs/The Bilinear Laplacian of a Balanced Graph#Balance and a common reference element|Balance and a common reference element]]

Evaluating $L$ itself checks the index order. For a connected balanced graph on $n\ge2$ vertices, $M_k=L^k/k!$ gives $(ML)_{n-1}=(n-1)M_{n-1}$. Dividing by the common spanning-tree coefficient yields

$$
\sum_{i\ne j}f_{ij}\,r_{ji}=n-1
$$

On our cycle this is $3\cdot(2/3)=2$. Using the forward indices would give $3\cdot(1/3)=1$, while $[(abc)]^2$ has coefficient 2 in $ML$.

## The undirected edge

For any vertex pair, bilinearity gives

$$
\Phi_{ij}+\Phi_{ji}=[a_j-a_i]^2=H_{i\to j}+H_{j\to i}
$$

The centroid cancels in the sum. On a connected balanced graph the same linear functional $P_M$ evaluates both forms. Thus $r_{ij}+r_{ji}=P_M([a_j-a_i]^2)=R_{ij}$, the symmetric pair resistance. Opposite arcs of equal weight contribute that weight times the same quadratic form to the Laplacian.

For a graph consisting of a single undirected edge $ab$ of weight $w>0$, $M=e+w[(ab)]^2$ and $\Phi_{ab}=\Phi_{ba}=\tfrac12[(ab)]^2$. Each direction gives $1/(2w)$ and their sum is $1/w$. On the directed three-cycle the pair resistance is $1/3+2/3=1$.

In $H_{i\to j}$ the tail selects the Laplacian row to change. In $\Phi_{ij}$ the target selects the centroid vector for evaluation. For balanced graphs the identity $L=\sum_{i\ne j}f_{ij}\Phi_{ji}$ connects the two choices. Unequal rooted potentials require an explicit normalization. [[en/Directed Graphs/Digraph Polyforms/How to Normalize One-Way Resistance in an Unbalanced Digraph|How to Normalize One-Way Resistance in an Unbalanced Digraph]]

[[ru/Направленные графы/Полиформы орграфов/Форма дуги и форма одностороннего резистенса|Русский]]
