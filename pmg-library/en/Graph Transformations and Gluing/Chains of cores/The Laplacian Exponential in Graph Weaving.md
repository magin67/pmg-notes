---
title: "The Laplacian Exponential in Graph Weaving"
date: 2026-11-02
updated: 2026-11-08
revision: 2
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: laplacian-exponential-under-graph-weaving
order: 2
description: "The repeated runner factor and the exponential growth operator; toponome transfer by component sizes, a forest recurrence, and five rooted boundary coordinates."
---

Russian version: [[ru/Преобразования и сочленения графов/Цепи из ядер/Экспонента лапласиана при плетении графов|Экспонента лапласиана при плетении графов]].

In [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]], a fixed plug, socket, and contact correspondence specify a repeated graph-construction step. Two spanning states allow the tree count to be computed. Here we consider the full Laplacian exponential and its forest grades.

Each attachment multiplies the exponential by a copy of the runner's exponential. The form of the piece repeats, but its vertex labels change. For a square ladder, this gives an explicit power of one operator: a shift of labels followed by multiplication by a fixed factor. After passage to the toponome, the operator acts on the sizes of components meeting the socket. Ordinary forest evaluation reduces it to two coordinates, while rooted evaluation leads to five spectral coordinates.

> [!info] Meaning of the result
> Extending a ladder does not require expanding all forests afresh at every step. The runner's action on boundary data can be described once and then repeated. The full exponential retains vertices, the toponome retains component sizes, and the ordinary and rooted polynomials retain different sums of their contributions. The chosen data determine the size of the transfer state.

> [!note] Origins of the results
> Factorization is used in the sense of [[en/Getting Started and Foundations/Introduction/Laplacian Exponential|Laplacian Exponential]]. The boundary calculation applies classical transfer of connectivity tables; accounting for component sizes agrees with the $U$-polynomial and algorithms for graphs of bounded treewidth [1, 2]. Rooted determinants and cofactors rely on the matrix-forest theorems of Chebotarev and Shamis [3, Theorems 5 and 6]. Formulas for the particular runner, their derivations, and checks are given below; no scientific priority is claimed.

## What repeats under attachment

Graphs are finite and undirected, with positive edge conductances. The runner $K$ has an ordered plug $P=(p_0,p_1)$ and socket $Q=(q_0,q_1)$. The plug of a new copy is identified with the active pair of the old graph using a fixed correspondence. There are no other identifications. The socket lies in the new copy and may overlap the plug. Subsequent attachments use only the active pair.

Edges of different copies are counted separately. In an ordinary chain of cycles, a shared edge must occur once: the runner is therefore the cycle **with its input edge removed**, and the initial graph contains that edge. Squares use the three-edge path $P_4$; hexagons use the five-edge path $P_6$. Retaining the input edge in the runner would add a parallel connection.

Write $N$ for the number of attachments and $n_N$ for the vertex count of the result. Starting from an edge with runner $P_m$,

$$
n_N=2+N(m-2),\qquad |E(G_N)|=1+N(m-1).
$$

For $N\ge1$, this is the number of added cycles $C_m$; $G_0$ is the initial edge. The variable $t$ marks the grade. For the Laplacian form and its exponential, set

$$
L_G=\sum_{uv\in E(G)}c_{uv}[a_v-a_u]^2,
\qquad M_G(t)=\exp(tL_G).
$$

Powers use the product of forms, with identity $e$. The matrix exponential $\exp(t\mathbf L_G)$ is not considered here.

> [!info] The exponential of one step
> **Proposition.** Let $\iota$ and $\jmath$ embed the old graph and the new runner copy into the vertex space of the result $H$. Then
>
> $$
> \begin{aligned}
> M_H(t)&=\iota(M_G(t))\,\jmath(M_K(t)),\\
> M_K(t)&=\prod_{uv\in E(K)}\bigl(e+tc_{uv}[a_v-a_u]^2\bigr).
> \end{aligned}
> \tag{1}
> $$

> [!note]- Proof of the factor rule
> **Proof.** After embedding, $L_H=\iota(L_G)+\jmath(L_K)$. Forms commute, so the exponential of the sum is the product of the exponentials. For the coupling form $p=[a_v-a_u]^2$, we have $p^2=0$ and $\exp(tcp)=e+tcp$. This gives (1). Edge sets containing cycles vanish in the product expansion, while each forest contributes its weight. $\square$

The repeated factor has the same local form but different embeddings. On a single fixed vertex set, the ordinary power $M_K(t)^N=\exp(NtL_K)$ would multiply conductances by $N$. New vertices arise from the attachment rule, not from that power.

## The square ladder as a power of an operator

Denote the rung vertices by $a_i,b_i$, $i\ge0$, and define

$$
f_{uv}(t)=e+t[v-u]^2,\qquad R_i(t)=f_{a_i b_i}(t).
$$

In a ladder of $N$ squares, the rungs have indices $0,\ldots,N$, and longitudinal edges join consecutive indices. Hence

$$
M_{G_N}(t)=R_0(t)\prod_{i=0}^{N-1}
f_{a_i a_{i+1}}(t)f_{b_i b_{i+1}}(t)R_{i+1}(t).
\tag{2}
$$

To express repetition, work with forms each using finitely many vertices from the list $a_0,b_0,a_1,b_1,\ldots$. The shift $\mathcal S$ replaces $a_i,b_i$ by $a_{i+1},b_{i+1}$ and preserves sums and products. Set

$$
\Phi(t)=R_0(t)f_{a_0a_1}(t)f_{b_0b_1}(t),
\qquad \mathcal U_t(X)=\Phi(t)\mathcal S(X).
$$

The factor $\Phi$ is the exponential of the path $a_1-a_0-b_0-b_1$. Its plug is $(a_1,b_1)$, and its socket is $(a_0,b_0)$. Here growth is depicted toward decreasing indices; the shift makes room for the next copy.

![Shifting the old ladder and adding the runner's three new factors](images/Shift%20and%20Exponential%20Factor%20of%20a%20Ladder.svg)

In the figure, old edges after the shift are gray, and the three new edges are blue. The former rung becomes the input edge and is not added again.

> [!info] The growth operator
> **Proposition.** For all $N\ge0$,
>
> $$
> \boxed{M_{G_N}(t)=\mathcal U_t^{\,N}(R_0(t)).}
> \tag{3}
> $$
>
> The power in (3) means operator composition. If $M_{G_N}(t)=\sum_g t^gM_{N,g}$ and $\Phi(t)=\sum_{r=0}^3t^r\Phi_r$, then
>
> $$
> M_{N+1,g}=\sum_{r=0}^3\Phi_r\,\mathcal S(M_{N,g-r}),
> \tag{4}
> $$
>
> where components with negative indices are zero.

> [!note]- Proof of the operator expression
> **Proof.** At $N=0$, both sides equal $R_0$. The shift moves every rung of the old ladder to indices $1,\ldots,N+1$. Multiplication by $\Phi$ adds rung $0$ and two connections between indices $0$ and $1$. This gives exactly the edge set in (2) for $N+1$. Induction proves (3); comparing coefficients of $t^g$ gives (4). $\square$

For an arbitrary connected runner, (1) similarly gives a convolution of grades with $L_K^r/r!$, $0\le r\le |V(K)|-1$, after the appropriate embeddings. It describes the full polyform; finitely many summands in a single step do not by themselves bound the size of the entire state.

## From the exponential to a toponome with a marked boundary

Use the canonical expansion of the edge factors in (1). A forest $F$ has weight $w(F)=\prod_{e\in F}c_e$. All vertices, including isolated vertices, are retained. Introduce variables $z_s$ for component sizes and set $z_1=1$:

$$
\mathcal T_G(t,\mathbf z)
=\sum_{F\text{ is a forest}}w(F)t^{|E(F)|}
\prod_{C\in\operatorname{Comp}(F)}z_{|V(C)|}.
\tag{5}
$$

At $t=1$, with $z_s=x_{s-1}$ for $s\ge2$, this gives the toponome $T_G(\mathbf x)$ of [[en/Polyform Algebra and Combinatorics/Partition toponomes/From Polyforms to Partitions|From Polyforms to Partitions]]. The number of vertices is retained separately. The variable $t$ is redundant but useful for transfer: its exponent is the sum of the component grades.

For unit conductances, (5) follows from the forest specialization of the Noble–Welsh $U$-polynomial: in formula (3.2) of Merino–Noble [1], setting $y=1$ retains forests, after which the variable for a component of size $s$ is replaced by $t^{s-1}z_s$. This identifies a specialization of a known polynomial; it does not define a new independent invariant.

This reduction applies to the chosen forest expansion. As explained in [[en/Polyform Algebra and Combinatorics/Partition toponomes/Toponomes and Structural Identities|Toponomes and Structural Identities]], rewriting an equal polyform arbitrarily may change the toponome of the chosen representation. The product $*$ in [[en/Polyform Algebra and Combinatorics/Partition toponomes/The Second-Kind Algebra on Partitions|The Second-Kind Algebra on Partitions]] does not replace attachment either: it sums partial matchings, whereas here the plug, socket, and contact correspondence are fixed in advance.

Let the active pair be $(a,b)$. Call a forest component **active** if it contains at least one contact, and **closed** if it contains none. A closed component can no longer connect to future vertices.

> [!info] A state retaining component sizes
> **Definition.** Introduce independent formal symbols:
>
> - $\mathsf C_s$, $s\ge2$: both contacts lie in one component of $s$ vertices;
> - $\mathsf D_{r,s}$, $r,s\ge1$: the first contact lies in a component of size $r$, and the second in a different component of size $s$.
>
> The state $\mathcal H_{G;a,b}(t,\mathbf z)$ is obtained by summing these symbols with weight
>
> $$
> w(F)t^{|E(F)|}\prod_{C\text{ closed}}z_{|V(C)|}.
> $$
>
> These symbols are counting states, not forms in the polyform algebra.

![One or two active components and a forest component that is already closed](images/Sizes%20of%20Active%20Forest%20Components.svg)

Rings mark the contacts in the figure; for brevity, $t=1$. The size of the closed tree is already recorded by the coefficient $z_3$; sizes of active trees remain in the state indices and may increase as the graph is extended.

The completion operation $\ell$ closes the remaining components:

$$
\ell(\mathsf C_s)=z_s,\qquad
\ell(\mathsf D_{r,s})=z_rz_s,\qquad
\mathcal T_G=\ell(\mathcal H_{G;a,b}).
\tag{6}
$$

**Why the data suffice.** For each edge subset of the runner, check whether it creates a cycle together with the old connectivity between the contacts. The sizes of components being joined are added to the number of new vertices. Components that lose contact with the new socket are closed. The internal shapes of the old trees are not needed for these operations. Restricting attachment to the active pair is essential: new connections to forgotten vertices would require additional data.

## Explicit transfer of the full square-ladder toponome

Denote the new contacts by $a',b'$. The runner adds edges $aa'$, $bb'$, and $a'b'$. All three conductances are one. Transfer by $\mathcal V_t$ is linear over the polynomial ring in $t,z_2,z_3,\ldots$.

> [!info] Two families of transitions
> **Theorem.** The square runner acts by the formulas
>
> $$
> \begin{aligned}
> \mathcal V_t(\mathsf C_s)={}&z_s(\mathsf D_{1,1}+t\mathsf C_2)\\
> &+t(\mathsf D_{s+1,1}+\mathsf D_{1,s+1})\\
> &+3t^2\mathsf C_{s+2},
> \end{aligned}
> \tag{7}
> $$
>
> $$
> \begin{aligned}
> \mathcal V_t(\mathsf D_{r,s})={}&z_rz_s(\mathsf D_{1,1}+t\mathsf C_2)\\
> &+tz_s\mathsf D_{r+1,1}+tz_r\mathsf D_{1,s+1}\\
> &+t^2\mathsf D_{r+1,s+1}\\
> &+t^2(z_s\mathsf C_{r+2}+z_r\mathsf C_{s+2})\\
> &+t^3\mathsf C_{r+s+2}.
> \end{aligned}
> \tag{8}
> $$
>
> For the initial edge, $\mathcal H_0=\mathsf D_{1,1}+t\mathsf C_2$, so
>
> $$
> \boxed{\mathcal T_{G_N}(t,\mathbf z)
> =\ell\!\left(\mathcal V_t^{\,N}(\mathcal H_0)\right).}
> \tag{9}
> $$

> [!note]- Proof of component-size transfer
> **Proof.** Enumerate the eight subsets of the three new edges. In state $\mathsf C_s$, choosing no longitudinal edges closes the old component and gives the first line of (7), according to whether the new rung is chosen. One longitudinal edge without the rung gives the second line. Any two new edges connect both new contacts to the old component, giving $3t^2\mathsf C_{s+2}$. All three edges create a cycle and are excluded.
>
> In state $\mathsf D_{r,s}$, all eight subsets are allowed. With no longitudinal edges, both old components close. One longitudinal edge without the rung closes the opposite component. Two longitudinal edges preserve separation. The rung together with one longitudinal edge forms one active component and closes the other old component. All three edges join the old components through the two new vertices. These cases give the lines of (8). No forest is lost or counted twice. Formula (6) and induction give (9). $\square$

The same procedure defines one operator for any fixed runner and its marked pairs. Two families of symbols do not mean two numerical coordinates: the size indices are unbounded.

### The complete first step: from an edge to a square

Set $z_1=1$ and substitute the initial state $\mathcal H_0=\mathsf D_{1,1}+t\mathsf C_2$ into (7)-(8). Collecting identical states gives

$$
\begin{aligned}
\mathcal H_1={}&(1+tz_2)(\mathsf D_{1,1}+t\mathsf C_2)+{}\\
&+t(\mathsf D_{2,1}+\mathsf D_{1,2})+{}\\
&+t^2(\mathsf D_{2,2}+\mathsf D_{3,1}+\mathsf D_{1,3}+2\mathsf C_3)+{}\\
&+4t^3\mathsf C_4
\end{aligned}
$$

In the state $t\mathsf C_2$, the initial edge is selected. Adding no new edges closes the old component and contributes $tz_2\mathsf D_{1,1}$. Any two of the three new edges produce a tree on four vertices, giving $3t^3\mathsf C_4$. The fourth tree comes from $\mathsf D_{1,1}$ by selecting all three new edges. This explains the final coefficient $4$.

![A selected initial edge: closing a component and three ways to extend a tree](images/The%20first%20square%20toponome%20step.svg)

Applying completion (6) yields the full toponome of the square:

$$
\mathcal T_{C_4}(t,\mathbf z)=1+4tz_2+t^2(4z_3+2z_2^2)+4t^3z_4
$$

The coefficients can also be checked without transfer. A single edge can be chosen in four ways. Among the six pairs of edges, four pairs are adjacent and form a three-vertex component; two pairs are opposite and give two two-vertex components. Any three edges form a spanning tree.

Both evaluations are now visible in one example:

$$
\begin{aligned}
z_s=1:&\qquad F_{C_4}(t)=1+4t+6t^2+4t^3,\\
z_s=s:&\qquad P_{C_4}(t)=1+8t+20t^2+16t^3
\end{aligned}
$$

Under the rooted evaluation, a component with $s$ vertices has $s$ choices of root. Hence the coefficient of $t^2$ is $4\cdot3+2\cdot2^2=20$. These evaluations allow states to be reduced. Before turning to them, clarify the limitation for the full toponome.

### Limitation of a scalar recurrence

> [!info] A limitation on scalar recurrences
> **Proposition.** For a growing sequence of connected graphs with positive conductances and $n_N\to\infty$, the full toponomes cannot satisfy a fixed-order linear recurrence whose coefficients are independent of $N$ and polynomial in a finite set of variables $x_j$.

> [!note]- Proof of the limitation
> **Proof.** Finitely many recurrence coefficients and initial polynomials use a finite set of variables. Addition and ordinary multiplication do not create new variables. Yet $T_{G_N}$ contains the monomial $\tau(G_N)x_{n_N-1}$, where $\tau(G_N)>0$. As $n_N$ grows without bound, this contradicts the recurrence. $\square$

This limitation concerns the specified class of ordinary scalar recurrences. It does not exclude the operator formulas (7)-(9), index shifts, coefficients depending on $N$, or finite recurrences after specializing variables.

## The ordinary forest polynomial and a second-order recurrence

Set $z_s=1$. Component sizes can then be forgotten: two polynomials $f_N^{\mathrm c}(t)$ and $f_N^{\mathrm d}(t)$ remain, for forests with joined and separated contacts. They also account for closed components and differ from the spanning states $(\tau,\sigma)$ in [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]]. The ordinary forest polynomial is $F_N=f_N^{\mathrm c}+f_N^{\mathrm d}$.

Let the runner be a unit path $P_m$, $m\ge3$, with its plug at the endpoints and its socket on any one of its edges. Write

$$
h_m=(1+t)^{m-2},\qquad b_m=t^{m-2}.
$$

If the socket overlaps the plug, this weaving may violate the stronger condition on disjoint nonadjacent cores in [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. The following formula requires only the stated rule of attachment through the active pair.

> [!info] Transfer of ordinary forests
> **Theorem.** Under every such attachment,
>
> $$
> \begin{gathered}
> \begin{pmatrix}f_{N+1}^{\mathrm c}\\f_{N+1}^{\mathrm d}\end{pmatrix}
> =\mathbf W_m(t)
> \begin{pmatrix}f_N^{\mathrm c}\\f_N^{\mathrm d}\end{pmatrix},\\[4pt]
> \mathbf W_m(t)=
> \begin{pmatrix}
> th_m+(1-t)b_m&th_m\\
> h_m-b_m&h_m
> \end{pmatrix}.
> \end{gathered}
> \tag{10}
> $$
>
> For a chain starting from an edge, $f_0^{\mathrm c}=t$, $f_0^{\mathrm d}=1$. The socket position and an exchange of the two contacts do not change (10).

> [!note]- Proof of the two-coordinate matrix
> **Proof.** If the old contacts are separated, any subset of the path is allowed. The new contacts are joined exactly when the output edge is chosen. The sums of weights are $th_m$ and $h_m$, giving the second column.
>
> If the old contacts are joined, choosing all $m-1$ edges creates a cycle and is forbidden. With the output edge chosen, the joined states have total weight $th_m-t^{m-1}$. Without that edge, the new contacts are joined through the old forest exactly when all other edges are chosen; this adds $t^{m-2}$. This gives the first row of the first column. A separated output allows every subset of the remaining edges except the full set: $h_m-b_m$. The position of the output edge was never used. $\square$

The trace and determinant of the matrix are

$$
\begin{aligned}
a_m(t)&=(1+t)^{m-1}+(1-t)t^{m-2},\\
d_m(t)&=[t(1+t)]^{m-2}.
\end{aligned}
$$

> [!info] A recurrence for the full ordinary forest polynomial
> **Corollary.** For all $N\ge0$,
>
> $$
> \boxed{F_{N+2}=a_m(t)F_{N+1}-d_m(t)F_N,}
> \tag{11}
> $$
>
> $$
> F_0=1+t,\qquad F_1=(1+t)^m-t^m.
> $$

> [!note]- Proof of the forest recurrence
> **Proof.** Apply the Cayley–Hamilton identity to $\mathbf W_m$ and add the two coordinates. The initial values count edge subsets of an edge and of a cycle, excluding the full edge set of the cycle. $\square$

For the square, $a_4=1+3t+4t^2$, $d_4=t^2(1+t)^2$. For the hexagon, $a_6=1+5t+10t^2+10t^3+6t^4$, $d_6=t^4(1+t)^4$. For example,

$$
F_{G_2}^{\text{squares}}(t)
=1+7t+21t^2+35t^3+33t^4+15t^5.
$$

| Number of cycles $N$ | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| All forests of the square ladder, $F_N(1)$ | 2 | 15 | 112 | 836 |
| All forests of the hexagonal chain, $F_N(1)$ | 2 | 63 | 1984 | 62480 |
| Spanning-tree counts of the square ladder | 1 | 4 | 15 | 56 |
| Spanning-tree counts of the hexagonal chain | 1 | 6 | 35 | 204 |

The leading coefficients of $a_m$ and $d_m$ are $m$ and $1$, and their degrees are $m-2$ and $2m-4$. Extracting the leading terms of (11) gives $\tau_{N+2}=m\tau_{N+1}-\tau_N$. The ordinary forest recurrence remains valid when the output edge varies from step to step. This is a concrete realization of matroid invariance; it does not extend to rooted polynomials.

## Rooted weights and five boundary coordinates

Now replace $z_s$ by $s$. For each forest, set

$$
\omega(F)=w(F)t^{|E(F)|}\prod_{C\text{ closed}}|V(C)|.
$$

When the contacts are joined, write $s(F)$ for their component size and define

$$
c_0=\sum_{F:\,a\leftrightarrow b}\omega(F),\qquad
c_1=\sum_{F:\,a\leftrightarrow b}s(F)\omega(F).
$$

When the contacts are separated, let $r(F),s(F)$ be the component sizes of the first and second contacts. Set

$$
d_{ij}=\sum_{F:\,a\not\leftrightarrow b}
r(F)^i s(F)^j\omega(F),\qquad i,j\in\{0,1\}.
$$

This gives six sums. The following five combinations form the familiar determinantal passport for the positive pencil $\mathbf H_G(t)=\mathbf I_n+t\mathbf L_G$:

> [!info] The forest meaning of the five-minor passport
> **Theorem.** When rows and columns are deleted without recomputing vertex degrees,
>
> $$
> \begin{aligned}
> A_+&=\det\mathbf H_G=c_1+d_{11},\\
> B_+&=\det(\mathbf H_G)_{\widehat a}=c_0+d_{01},\\
> C_+&=\det(\mathbf H_G)_{\widehat b}=c_0+d_{10},\\
> D_+&=(\operatorname{adj}\mathbf H_G)_{ab}=c_0,\\
> E_+&=\det(\mathbf H_G)_{\widehat{a,b}}=d_{00}.
> \end{aligned}
> \tag{12}
> $$
>
> In particular, $A_+=P_G(t)$ and $A_+E_+=B_+C_+-D_+^2$. The five coordinates are not claimed to be algebraically independent or minimal.

> [!note]- Proof of the rooted interpretation
> **Proof.** The matrix-forest theorem [3, Theorem 5] counts forests with one chosen root in each component. In the active component of a joined state there are $s$ root choices; in two separated components there are $rs$. This gives $A_+$.
>
> The principal minor deleting $a$ counts forests in which the root of the component containing $a$ is forced to be $a$, while other roots are free. Thus the active-component weights are $1$ for a joined state and $s$ for a separated state. Deleting $b$ gives $1$ and $r$, respectively. Deleting both contacts requires them to be roots of distinct components, leaving $d_{00}$.
>
> All formulas for the principal minors can be obtained together from the identity
>
> $$
> \begin{aligned}
> &\det(\operatorname{diag}(y_v)+t\mathbf L_G)\\
> &\quad=\sum_F w(F)t^{|E(F)|}
> \prod_{C\in\operatorname{Comp}(F)}\left(\sum_{v\in C}y_v\right).
> \end{aligned}
> $$
>
> It follows from the matrix-tree theorem after adding an auxiliary vertex and connections of weight $y_v$: removing this vertex from a tree leaves each component with exactly one connection to it. Differentiating with respect to $y_a$, or to $y_a,y_b$, and then setting all $y_v=1$ gives the required minors.
>
> Finally, Theorem 6 of [3] expresses the cofactor through forests in which $a,b$ lie in the same tree rooted at one specified contact. Symmetry makes the sum independent of the index direction. The root of the active tree is already fixed, so $c_0$ remains. Jacobi's identity gives the final equality. $\square$

![Full boundary component sizes and two different specializations of transfer](images/From%20Component%20Sizes%20to%20Two%20and%20Five%20Coordinates.svg)

Ordinary evaluation forgets sizes. Rooted evaluation retains the five combinations (12), corresponding to free and forced roots. The full toponome itself cannot be recovered from these combinations.

**Why five coordinates are closed.** Their forest interpretation alone does not prove transfer to a new pair. For that, we apply the theorem in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#Why transfer closes on five coordinates|Spectral Transfer to a New Boundary]]. Its determinant argument also applies to $\mathbf I+t\mathbf L$: after elimination of the old interior, each new minor depends on the symmetric input block through $1,u,v,w,uw-v^2$. Retaining the interior determinant makes transfer linear in the five coordinates. A fixed marked runner therefore gives one polynomial matrix in $t$.

Thus (12) explains which combinations of forest component sizes are retained by this already-proved transfer. Repeating one runner gives a coordinate recurrence of order at most five by the Cayley–Hamilton theorem. The minimal order of a particular sequence may be lower.

To compare with the library's spectral convention, for $t\ne0$,

$$
\mathbf H_G(t)=-t\,\mathbf M_G(-1/t),\qquad
\mathbf M_G(\xi)=\xi\mathbf I_n-\mathbf L_G.
$$

Accordingly, $A_+(t)=(-t)^nA(-1/t)$, the coordinates $B_+,C_+,D_+$ acquire the factor $(-t)^{n-1}$, and $E_+$ acquires $(-t)^{n-2}$. These expressions extend polynomially to $t=0$. In particular, $P_G(1)=(-1)^n\chi_G(-1)$.

## Distinguishing isomers before rooted evaluation

Use exactly graphs A and B from [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]]. The notation $C(v_0,\ldots,v_5)$ includes the closing edge. The common cores are $C(0,1,9,8,7,6)$ and $C(0,1,2,3,4,5)$; the third core is $C(3,4,13,12,11,10)$ in A and $C(2,3,13,12,11,10)$ in B. Edges are united as sets. Both graphs have $n=14$ vertices and $16$ edges.

Exact enumeration shows that their full toponomes agree in grades $0,1,2$ and first differ in grade $3$.

| Positive type | Components containing edges | A | B | A minus B |
| --- | --- | --- | --- | --- |
| $(3)$ | One tree on four vertices | 34 | 35 | -1 |
| $(2,1)$ | A tree on three vertices and a separate edge | 236 | 234 | 2 |
| $(1,1,1)$ | Three separate edges | 290 | 291 | -1 |

All other vertices are isolated. Row $(3)$ combines all shapes of a tree on four vertices, including the path and the star.

![Three forest types distinguishing the isomers and cancellation of the difference under rooted weights](images/Grade%20Three%20of%20the%20Toponomes%20of%20Two%20Isomers.svg)

Hence, for the homogeneous part of total grade $3$,

$$
\left(T_{\mathrm A}-T_{\text{B}}\right)_{g=3}
=-x_3+2x_2x_1-x_1^3.
\tag{13}
$$

Under ordinary evaluation $x_j\mapsto t^j$, the difference is $(-1+2-1)t^3=0$. Rooted evaluation $x_j\mapsto(j+1)t^j$ also gives zero:

$$
\bigl(-4+2\cdot3\cdot2-2^3\bigr)t^3=0.
$$

The toponome distinguishes component-size distributions, but these two sums do not distinguish them. In grade four the rooted difference is already nonzero; the full result agrees with the proved formula in [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons#The first difference in rooted forests|Two Isomers of Three Hexagons]]:

$$
P_{\mathrm A}(t)-P_{\text{B}}(t)=t^4(1+5t+5t^2)^4.
$$

The statement about the first toponome difference and the table were obtained by exhaustive finite enumeration of this particular pair. They are not a general theorem about the first distinguishing grade of all chains. For the full exponential on labeled vertices, the question is different: its first grade already contains the Laplacian itself. Here we compare types after forgetting vertex labels.

## Exact checks and limits of the result

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_weaving_exponential.py) uses integers and exact symbolic arithmetic in SymPy. The [saved results](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/weaving-exponential-results.json) contain edge sets, boundaries, full toponomes, and five rooted polynomials. The [figure generator](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/draw_weaving_exponential.py) uses these results for numerical labels.

The checks cover:

- the square ladder and two configurations of the hexagonal chain at $N=0,1,2,3$: 12 graphs and exhaustive enumeration of 136470 edge subsets;
- agreement of the full boundary state with independent enumeration, and of its rooted evaluation with direct determinants; polynomials are compared for the four principal determinants, while the off-diagonal cofactor is checked using Jacobi's identity and a direct sign check at $t=1$;
- all 22110 coefficients of the second grade in the vertex basis for these graphs: products of edge forms agree with the corresponding Laplacian minors of size $2$;
- the explicit rules (7)-(8), the shift operator (3) through five squares, and recurrence (11);
- 54 checks of the columns of (10) for $3\le m\le8$ and every output edge; 216 variants of three $P_6$ steps with three internal sockets and both input-contact correspondences;
- additional enumeration of all $2\cdot2^{16}$ edge subsets of the original labeled pair A, B: it agrees with the runner calculation and confirms (13).

Jacobi's identity determines the square of the off-diagonal polynomial. Its sign is uniquely fixed by the direct cofactor at $t=1$, because the graphs considered are connected and this cofactor is positive. Thus the check is not limited to a single numerical value.

The general factor, operator, and forest formulas above have proofs. Enumerations check the implementations and specified examples. Finite-dimensional transfer is not proved for the full toponome; indeed, active component sizes in the state used here are unbounded. For rooted evaluation, sufficiency of five coordinates relies on a separate theorem on changing the boundary. It does not imply completeness of the spectrum as a graph invariant.

The connection to [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] is established in detail in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]]: the three sockets of the path $P_6$, contact order, reflection, and constant and periodic words. Repetition gives a power of the growth operator and exact spectral recurrences. No planarity is required; a spatial drawing of the chain does not change the attachment rule.

## Sources and connections

1. C. Merino, S. D. Noble. *The Equivalence of Two Graph Polynomials and a Symmetric Function*. [§3, formula (3.2)](https://arxiv.org/html/0805.4793v1#S3): expansion of the $U$-polynomial by component sizes.
2. S. D. Noble. *Evaluating a Weighted Graph Polynomial for Graphs of Bounded Tree-Width*. Electronic Journal of Combinatorics **16** (2009), R64. [Article and abstract](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r64). General algorithmic context for accounting for components; the specific formulas (7)-(11) are derived in this note.
3. P. Chebotarev, E. Shamis. *Matrix-Forest Theorems*. [“Matrix-Forest Theorems” section, Theorems 5 and 6](https://arxiv.org/html/math/0602575v2#S4): the determinant and cofactors as sums of rooted-forest weights.

Foundations: [[en/Getting Started and Foundations/Introduction/Laplacian Exponential|Laplacian Exponential]], [[en/Polyform Algebra and Combinatorics/Partition toponomes/From Polyforms to Partitions|From Polyforms to Partitions]], [[en/Polyform Algebra and Combinatorics/Polynomial toponomes/Vector and Vertex Normalizations of Toponomes|Vector and Vertex Normalizations of Toponomes]]. Construction: [[en/Graph Transformations and Gluing/Chains of cores/Weaving Graphs - Plug Socket and Recurrence|Weaving Graphs: Plug, Socket, and Recurrence]]. Boundary states: [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]]. Distinguishing isomers: [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]].
