---
title: Resistance Geometry and Circulation
date: 2026-10-24
updated: 2026-10-25
revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: resistance-geometry-and-circulation
lang: en
description: Euclidean pair geometry, circulation as nonreciprocal response, and a three-vertex resistance formula combining area and circulation.
order: 7
source_revision: 5
---

Pair resistance in a balanced graph retains the geometric meaning of squared distance. These distances describe only the symmetric part of its bilinear response. A circulation form's normalized potential supplies an additional oriented quantity. In a Markov model it compares traversal times; electrically it compares responses after exchanging excitation and measurement. On three vertices, both contributions enter a formula extending the expression for area in terms of side lengths.

Use the definitions from [[One-Way Resistance and Hitting Times]]: $M=\exp L$, $P_M(F)=\tau(MF)/\tau(M)$, and $r_{ij}=P_M([a_j-h,a_j-a_i])$, where $h=n^{-1}\sum_i a_i$. The graph is connected, balanced, loopless, and nonnegatively weighted. These are algebraic definitions; geometric, Markov, and electrical interpretations follow.

## The bilinear potential and its two parts

For affine vectors $u,v\in W$, set $\beta(u,v)=P_M([u,v])$. With argument roles explicit,

$$
\beta(u,v)=u^{\mathrm{out}}\cdot v^{\mathrm{in}}
=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u,
\qquad \mathbf{Gr}=\mathbf L^+
$$

Here $u$ is the source and $v$ the receiver. Exchanging roles gives $\beta(v,u)=v^{\mathrm{out}}\cdot u^{\mathrm{in}}$. The corresponding spaces and coordinates are described in [[The Gram Matrix and Directional Coordinates of a Balanced Graph#Sources and receivers|the directional pairing note]]. Below we use the shorter $\beta(u,v)$.

In general, $\beta$ is nonsymmetric. Separate its symmetric and skew-symmetric parts:

$$
g(u,v)=\frac{\beta(u,v)+\beta(v,u)}2,\qquad
\gamma(u,v)=\frac{\beta(u,v)-\beta(v,u)}2
\tag{1}
$$

Here $g$ is a numerical inner product on $W$, and $\gamma$ a numerical skew-symmetric bilinear form. They differ from the formal forms $[u,v]$ and $\omega(u,v)=[u,v]-[v,u]$.

For $u=a_j-a_i$, $v=a_k-a_i$,

$$
R_{ij}=g(u,u),\qquad
\chi_{ijk}=P_M(w(a_i a_j a_k))=2\gamma(u,v)
$$

The circulation norm therefore compares two directional pairings:

$$
\chi_{ijk}=u^{\mathrm{out}}\cdot v^{\mathrm{in}}
-v^{\mathrm{out}}\cdot u^{\mathrm{in}}
$$

This exchanges the source and receiver roles of two vectors. By contrast, evaluating the same pairing through one argument's bi-coordinates and the other's di-coordinates preserves its value.

The split (1) serves interpretation. Exponential calculations can still use bilinear forms directly, without splitting the Laplacian into two types of terms.

## The Euclidean part of the metric

> [!info] Positivity of the symmetric part
> **Theorem.** For a connected balanced graph with nonnegative weights, $g$ is positive definite on $W$. Its vertices therefore have an $(n-1)$-dimensional Euclidean realization with
>
> $$
> \boxed{|a_j-a_i|_g^2=R_{ij}=r_{ij}+r_{ji}}
> \tag{2}
> $$
>
> Linear distance in this realization is $\sqrt{R_{ij}}$.

> [!note]- Proof
> **Proof.** Set $\mathbf S=(\mathbf L+\mathbf L^{\mathsf T})/2$. Balance makes this the Laplacian of a connected undirected graph with conductances $(f_{ij}+f_{ji})/2$, hence positive definite on zero-sum columns.
>
> For a nonzero column $\mathbf u$ in that subspace, put $\mathbf y=\mathbf{Gr}\mathbf u$. Then $\mathbf L\mathbf y=\mathbf u$, $\mathbf y\ne0$, and
>
> $$
> g(u,u)=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf u
> =(\mathbf L\mathbf y)^{\mathsf T}\mathbf y
> =\mathbf y^{\mathsf T}\mathbf S\mathbf y>0
> $$
>
> An orthonormal basis for $g$ gives a Euclidean realization of $W$. The vectors $a_i-h$ sum to zero, and their pairwise differences give (2). $\square$

Ordinary distance geometry thus survives directed couplings. For the continuous-time walk with generator $-\mathbf L$, the identity $H_{ij}=nr_{ij}$ interprets $nR_{ij}$ as the mean time to reach $j$ from $i$ and return. Euclidean geometry of such times for nonreversible chains is studied in [1].

Generally, $g$ differs from the resistance metric of $\mathbf S$: inversion and symmetrization do not commute. Directionality affects distances even though distances themselves are symmetric.

### Example: the unit directed 3-cycle

In $a\to b\to c\to a$, all arc weights are $1$. The formula $r_{ij}=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}$ gives, in order $a,b,c$,

$$
\mathbf r=\frac13
\begin{pmatrix}
0&1&2\\
2&0&1\\
1&2&0
\end{pmatrix},\qquad
R_{ab}=R_{bc}=R_{ca}=1,\qquad
\chi_{abc}=1-2=-1
$$

![[Geometry of a Unit Directed 3-Cycle.svg]]

*Left: the original unit-weight cycle. Right: its resistance geometry, an equilateral triangle of side $1$. One-way resistances sum to $1$ along the forward traversal and $2$ along the reverse; their difference $\chi_{abc}=-1$ is invisible in the side lengths. Corresponding mean traversal times are $3$ and $6$.*

An undirected triangle with conductance $2/3$ on each edge has the same pair resistances $1$, but zero circulation norms. Equal pairwise distances therefore do not determine the full metric evaluation of a balanced graph's bilinear forms.

## What circulation measures

For three vertices, we defined

$$
\chi_{ijk}=r_{ij}+r_{jk}+r_{ki}-r_{ik}-r_{kj}-r_{ji}
$$

This is the normalized potential of the grade-one form $w(a_i a_j a_k)$. Its sign compares one-way resistance sums in the two orientations; its magnitude measures their difference. In the Markov interpretation, $n\chi_{ijk}$ is the difference between mean sequential target-traversal times. A single difference $r_{ij}-r_{ji}$ also includes different centroid positions and is not a pure circulation measure.

> [!info] What circulation measures
> **Proposition.** The following conditions are equivalent: every $\chi_{ijk}$ vanishes; $\beta$ is symmetric; $\mathbf L$ is symmetric. In the Markov interpretation, these are also equivalent to reversibility of the walk with generator $-\mathbf L$.

> [!note]- Why all triples are needed
> **Proof.** Fix $a_n$. The forms $w(a_n a_i a_j)$ encode skew pairs of the basis vectors $a_i-a_n$. Vanishing of their potentials is equivalent to $\gamma=0$ on all of $W$. Then $\mathbf{Gr}$ is symmetric on zero-sum columns and, since it annihilates constants, on the full coordinate space. Its pseudoinverse $\mathbf L$ is also symmetric. The reverse implications follow from the same identities. For stationary probabilities $\pi_i=1/n$, detailed balance $\pi_if_{ij}=\pi_jf_{ji}$ is equivalent to $f_{ij}=f_{ji}$. $\square$

One vanishing $\chi_{ijk}$ permits cancellation and does not imply symmetry of the whole graph. The all-triples condition agrees with the cyclic reversibility criterion in [1, §12].

### Why its magnitude can increase or decrease

Give $a\to b\to c\to a$ weight $p$ and the opposite arcs weight $q$, where $p,q\ge0$ and $p+q>0$. Direct computation gives

$$
\tau=p^2+pq+q^2,\qquad
R_{ab}=R_{bc}=R_{ca}=\frac{p+q}{\tau},\qquad
\boxed{\chi_{abc}=\frac{q-p}{\tau}}
\tag{3}
$$

> [!note]- Check using the reduced Laplacian
> **Proof.** In basis $a-c,b-c$, the Laplacian coefficient matrix and inverse are
>
> $$
> \mathbf C=
> \begin{pmatrix}p+q&-p\\-q&p+q\end{pmatrix},\qquad
> \mathbf C^{-1}=\frac1{p^2+pq+q^2}
> \begin{pmatrix}p+q&p\\q&p+q\end{pmatrix}
> $$
>
> Use $\beta(u,v)=\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u$. For $u=b-a$, $v=c-a$, this gives $\beta(u,u)=\beta(v,v)=(p+q)/\tau$, $\beta(u,v)=q/\tau$, and $\beta(v,u)=p/\tau$. Cyclic symmetry makes all pair resistances equal; subtracting the mixed values gives (3). $\square$

At fixed outgoing weight $p+q=1$:

| Forward weight $p$ | Reverse weight $q$ | Each pair's total resistance | Circulation norm $\chi_{abc}$ |
| --- | --- | --- | --- |
| $1/2$ | $1/2$ | $4/3$ | $0$ |
| $3/4$ | $1/4$ | $16/13$ | $-8/13$ |
| $1$ | $0$ | $1$ | $-1$ |

Within this family, strengthening the preferred direction increases circulation magnitude. Its absolute value also depends on weight scale: multiplying all weights by $c>0$ divides $r$, $R$, and $\chi$ by $c$. Doubling a pure cycle's weights reduces $|\chi|$ from $1$ to $1/2$ without changing its orientation.

The ratio $\chi_{abc}/R_{ab}=(q-p)/(p+q)$ separates directional bias from scale in this family. A general balanced graph has no such local formula in two arc weights: its circulation potential depends on the entire graph. It also differs from stationary flow, here $(p-q)/3$ along each side.

### Circulation and two projections onto a line

The circulation potential also has a geometric interpretation through [[Balanced Variations#One-way variation and loss of balance|directional projections]]. Put $v=b-a$ and $w_i=a_i-a$. The coefficients of $b$ in the outgoing and incoming projections of vertex $a_i$ onto line $ab$ are

$$
\theta_i^{\mathrm{out}}=\frac{\beta(w_i,v)}{R_{ab}},\qquad
\theta_i^{\mathrm{in}}=\frac{\beta(v,w_i)}{R_{ab}}
$$

By definition, $\chi_{abi}=\beta(v,w_i)-\beta(w_i,v)$, so

$$
\boxed{\theta_i^{\mathrm{in}}-\theta_i^{\mathrm{out}}
=\frac{\chi_{abi}}{R_{ab}}}
$$

Thus the sign of the circulation potential gives the order of the two projections along $a\to b$, while its ratio to $R_{ab}$ gives the difference of their coefficients. Zero circulation for this triple means that these two projections coincide. For example, in the unit cycle $a\to b\to c\to a$, we have $\theta_c^{\mathrm{out}}=1$, $\theta_c^{\mathrm{in}}=0$, and $\chi_{abc}/R_{ab}=-1$.

## Electrical interpretation: reciprocity of responses

Consider the linear nodal law

$$
\mathbf I=\mathbf L\boldsymbol\varphi
$$

External currents sum to zero, and potentials are defined up to a constant. For excitation column $\mathbf u$, choose $\boldsymbol\varphi=\mathbf{Gr}\mathbf u$. Measurement coefficients $\mathbf v$ give

$$
\boxed{\mathbf v^{\mathsf T}\boldsymbol\varphi=\beta(u,v)}
\tag{4}
$$

In this experiment, $\mathrm{out}$ denotes current excitation $u$, and $\mathrm{in}$ the response measurement $v$. For $u=b-a$, current $+1$ enters at $b$ and $-1$ at $a$. For $v=d-c$, the measured voltage is $\varphi_d-\varphi_c$.

- If $u=v$, the result is two-terminal resistance $R_{ab}$. Reversing both excitation and measurement signs preserves it.
- Exchanging excitation and measurement gives $\beta(v,u)$. The difference between experiments is $P_M(\omega(u,v))$.
- For $u=b-a$, $v=c-a$, this difference is $\chi_{abc}$.

![[Circulation and Response Reciprocity.svg]]

*Both experiments use the same network. First, current enters at $b$ and leaves at $a$, while voltage is measured between $c$ and $a$. The second experiment exchanges the roles of $b,c$. The difference of the measured responses equals $\chi_{abc}$.*

Ordinary resistor networks satisfy reciprocity because their Laplacians are symmetric. A nonsymmetric nodal law requires nonreciprocal elements or controlled sources. Electrical models of nonreversible Markov chains with additional elements appear in [2]; their specific circuits must be matched to the chosen nodal law.

Thus $\chi$ has an operational interpretation as **nonreciprocity of transfer response**. Excitation and measurement are exchanged; ordinary resistance of one pair remains unchanged when current is reversed.

To compare with rooted potentials after adding an arc $a\to b$, prescribe the current column $\mathbf d=\mathbf e_a-\mathbf e_b$. The original network and the network with all arcs reversed give, respectively,

$$
\begin{aligned}
\boldsymbol\varphi&=\mathbf{Gr}\mathbf d,&
\frac{\varphi_a-\varphi_i}{R_{ab}}&=\theta_i^{\mathrm{in}}\\
\mathbf y&=\mathbf{Gr}^{\mathsf T}\mathbf d,&
\frac{y_a-y_i}{R_{ab}}&=\theta_i^{\mathrm{out}}
\end{aligned}
$$

Thus normalized differences of the perturbed digraph's rooted potentials reproduce voltages for the transpose of the original Laplacian. When $\mathbf L=\mathbf L^{\mathsf T}$, both responses coincide. For a general balanced graph, their difference agrees with the two [[Selected Vertices and the Dirichlet Problem#Two Dirichlet problems in a balanced graph|Dirichlet problems]] and the formula involving $\chi$ above.

## Three-vertex resistance

For three distinct basis vertices, define

$$
R_{abc}=P_M([(abc)]^2)
$$

This is the normalized potential of the quadratic form of a grade-two boundary. For an undirected graph it is the square of twice the triangle's area. A balanced graph adds a circulation contribution.

> [!info] Generalized three-vertex formula
> **Theorem.** Let $A_{abc}$ be the triangle's area in Euclidean metric $g$. Then
>
> $$
> \boxed{R_{abc}=4A_{abc}^2+\frac{\chi_{abc}^2}{4}}
> \tag{5}
> $$
>
> Equivalently, in pair resistances,
>
> $$
> \boxed{4R_{abc}
> =(R_{ab}+R_{bc}+R_{ca})^2
> -2(R_{ab}^2+R_{bc}^2+R_{ca}^2)+\chi_{abc}^2}
> \tag{6}
> $$

> [!note]- Proof through form multiplication
> **Proof.** Put $u=b-a$, $v=c-a$, so $(abc)=uv$. The determinant expansion for two bilinear variations gives
>
> $$
> P_M([uv]^2)=
> \det\begin{pmatrix}\beta(u,u)&\beta(u,v)\\\beta(v,u)&\beta(v,v)\end{pmatrix}
> $$
>
> Indeed, in $\exp(L+s[u]^2+t[v]^2)=M(e+s[u]^2)(e+t[v]^2)$, extracting the spanning-tree coefficient and then the coefficient of $st$ gives $\tau(M[uv]^2)$. Computing through the reduced Laplacian instead gives $\tau(M)$ times the two-excitation determinant, whose $st$ coefficient is the displayed determinant.
>
> Using $\beta(u,v)=g(u,v)+\gamma(u,v)$ gives
>
> $$
> P_M([uv]^2)=g(u,u)g(v,v)-g(u,v)^2+\gamma(u,v)^2
> $$
>
> The Gram determinant $g(u,u)g(v,v)-g(u,v)^2$ equals $4A_{abc}^2$. Also, $2\gamma(u,v)=\chi_{abc}$ and $2g(u,v)=R_{ab}+R_{ac}-R_{bc}$. Substitution proves (5) and (6). $\square$

The result can be computed directly from one-way resistances:

$$
\begin{aligned}
\beta(b-a,c-a)&=r_{ab}+r_{ca}-r_{cb}\\
\beta(c-a,b-a)&=r_{ac}+r_{ba}-r_{bc}\\
R_{abc}&=R_{ab}R_{ac}-\beta(b-a,c-a)\beta(c-a,b-a)
\end{aligned}
$$

For the unit directed 3-cycle, all $R_{ij}=1$ and $\chi_{abc}=-1$, hence

$$
R_{abc}=\frac34+\frac14=1
$$

This independently agrees with $M=e+L+[(abc)]^2$ and $\tau(M)=1$: the top coefficient of $M[(abc)]^2$ is $1$. An undirected triangle with the same pair resistances has $\chi_{abc}=0$, giving $R_{abc}=3/4$.

> [!info] Three-vertex resistance
> **Corollary.** With circulation present, the potential of $[(abc)]^2$ is not just the Euclidean boundary norm induced by $g$. It evaluates the full bilinear response. It can be measured as the determinant of the two-experiment response matrix in (4): two independent current excitations and two measurements give a matrix with determinant $R_{abc}$. Reversing every arc changes the sign of $\chi$, while preserving $\chi^2/4$.
>
> Decomposable objects of arbitrary grade obey the analogous determinant rule:
>
> $$
> P_M([u_1\cdots u_k,v_1\cdots v_k])
> =\det\bigl(\beta(u_i,v_j)\bigr)_{i,j=1}^k
> $$
>
> It follows by comparing coefficients of $k$ bilinear variations, as in the proof of (5). The one-way resistance matrix therefore determines these potentials too: for zero-sum coordinate columns,
>
> $$
> \beta(u,v)=-\mathbf v^{\mathsf T}\mathbf r\mathbf u
> $$
>
> Detailed higher-grade geometry remains a separate subject. Already the three-vertex case shows why it cannot automatically be identified with the exterior extension of the symmetric metric $g$ alone.

## Sources and connections

The geometric and determinant identities are proved above. Three-vertex resistance formulas were also checked directly by multiplying the exterior exponential and $[(abc)]^2$ on rational weighted balanced graphs, independently of area calculations from pairwise distances.

1. P. G. Doyle, J. Steiner. [Commuting time geometry of ergodic Markov chains](https://arxiv.org/abs/1107.2612). Version 2, 2017. Commute-time geometry for general ergodic chains; §12: circulation sums and reversibility.
2. M. Balázs, Á. Folly. [An Electric Network for Nonreversible Markov Chains](https://arxiv.org/abs/1405.7660). *The American Mathematical Monthly* **123** (2016), 657-682. [DOI: 10.4169/amer.math.monthly.123.7.657](https://doi.org/10.4169/amer.math.monthly.123.7.657). An electrical model with additional elements for nonreversible chains.

Related notes: [[One-Way Resistance and Hitting Times]], [[The Circulation Form]], [[From Lengths to Areas and Volumes]], [[Balanced Variations]], [[The Gram Matrix and Directional Coordinates of a Balanced Graph]], [[The Isotropic Space and Sphere of a Balanced Graph]].

