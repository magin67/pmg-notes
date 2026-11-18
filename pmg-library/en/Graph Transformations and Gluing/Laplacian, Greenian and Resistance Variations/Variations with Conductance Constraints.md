---
title: Variations with Conductance Constraints
date: 2026-10-31
updated: 2026-11-18
revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: variations-constrained-couplings
lang: en
description: 'The prism and the problem with sets P, Z, and V: prescribed resistances, preserved zero couplings, nonnegative conductances, and boundaries of solution existence.'
order: 7
translated_revision: 9
aliases:
  - "en/Laplacian, Greenian and Resistance Variations/Variations with Conductance Constraints"
---

[[ru/Преобразования и сочленения графов/Вариации лапласиана, гриниана и резистенсов/Вариации при ограничениях на связи|Русский]]

In [[Joint Variation of Resistances]], the entire new resistance matrix was prescribed. This uniquely determined the Laplacian but could introduce previously absent couplings or negative conductances.

We now prescribe resistances only between vertices of a set $P$. Some couplings must remain zero; the others may change only on a specified set $V$, while remaining nonnegative. Resistances outside $P$ result from the solution and are not fixed in advance. Relaxing the resistance conditions in this way creates freedom to satisfy conductance constraints.

## The prism example

See [[en/PythonExamples/Example - Laplacian, Greenian and Resistance Variations#A feasible change of the prism|the notebook calculation]].

In this example, $P$ is a vertex set, whereas $V$ and $Z$ are sets of vertex pairs. Colored edges may vary and grey edges are fixed; absent forbidden pairs are listed separately.

Consider a triangular prism with faces $abc$ and $def$ and connecting edges $ad,be,cf$. Initially, all nine conductances equal $1$.

Choose $P=\{a,b,c\}$. Keep the three conductances of this face equal to one. The following may change:

$$
V=\{de,df,ef,ad,be,cf\}
$$

All absent couplings must remain zero:

$$
Z=\{ae,af,bd,bf,cd,ce\}
$$

The original resistances on $P$ are

$$
R_{ab}=R_{ac}=R_{bc}=\frac8{15}
$$

Increase only $R_{ab}$ to $3/5$, that is, by a factor of $9/8$, keeping $R_{ac}=R_{bc}=8/15$.

![Two states of the prism graph with fixed outer face abc and variable couplings to inner face def](<images/Prism with Conductance Constraints.svg>)

*The prism is drawn in the plane: the outer triangle $abc$ corresponds to $P$. Its gray edges are fixed; colored edges belong to $V$. Numbers denote conductances. The dashed edge on the right is the permitted coupling $de$ whose conductance has become zero; pairs in $Z$ are not drawn.*

> [!example] An exact solution with nonnegative conductances
> One solution is
>
> $$
> \boxed{\begin{gathered}
> c'_{ad}=c'_{be}=c'_{cf}=7,\\
> c'_{de}=0,\qquad c'_{df}=c'_{ef}=\frac7{20}
> \end{gathered}}
> \tag{1}
> $$
>
> It gives
>
> $$
> R'_{ab}=\frac35,\qquad R'_{ac}=R'_{bc}=\frac8{15}
> $$
>
> Couplings on $Z$ remain zero, conductances on face $P$ remain one, and the graph is connected. Setting $de$ to zero is permitted: this pair belongs to $V$.

To check this, eliminate the internal vertices $d,e,f$ while preserving resistances on $P$. Initially, the resulting triangle has conductances $5/4$. For (1), its conductances are

$$
q'_{ab}=\frac{70}{69},\qquad q'_{ac}=q'_{bc}=\frac{30}{23}
$$

The spanning-tree coefficient of this triangle is $100/23$. Thus

$$
R'_{ab}=\frac{60/23}{100/23}=\frac35,\qquad
R'_{ac}=R'_{bc}=\frac{70/69+30/23}{100/23}=\frac8{15}
$$

Conductances $q'_{ij}$ belong to the graph after internal-vertex elimination, not to the original couplings $c'_{ij}=1$ on face $P$. The elimination formula and general derivation are given below.

If instead $R_{ab}$ is required to double while the same two other resistances are preserved, there is no solution with nonnegative conductances. Free couplings therefore do not make every resistance change admissible.

![The Prism and Its Boundary Triangle](<images/The Prism and Its Boundary Triangle.svg>)

*Eliminating vertices $d,e,f$ produces another graph on $P$. Its conductance $q_{ab}$ is the fixed $c_{ab}=1$ plus an induced contribution; this is not a change of the original edge $ab$.*

## Formulating the problem with P, Z, and V

Let $\Omega$ be a fixed vertex set, $\mathcal E$ the set of all unordered pairs, and $c_e^0\ge0$ the original conductances of an undirected graph. Positive-conductance edges form a connected graph. Specify:

| Data | Requirement |
|---|---|
| $P\subseteq\Omega$, $\lvert P\rvert\ge2$ | Resistances between all distinct vertices of $P$ must equal the prescribed $R^*_{ab}$ |
| $Z\subseteq\mathcal E$ | These pair conductances are zero and must remain zero |
| $V\subseteq\mathcal E\setminus Z$ | These pair conductances may change |
| Pairs outside $Z\cup V$ | Conductances retain their original values |

To preserve resistances, choose $R^*_{ab}=R^0_{ab}$. To change them, prescribe other values. The input is assumed consistent: $c_e^0=0$ for $e\in Z$. Forced removal of an originally nonzero edge is a separate fixed change and must be included explicitly in the problem.

The target table $\mathbf R_P^*$ is symmetric with zero diagonal. Its realizability in the graph class must be checked.

Denote the new conductances on $V$ by $x_e$, and the corresponding pair vectors by $\mathbf a_e=\mathbf e_j-\mathbf e_i$. Then

$$
\begin{aligned}
\mathbf L(\boldsymbol x)&=\mathbf L_{\mathrm{fix}}
+\sum_{e\in V}x_e\mathbf a_e\mathbf a_e^{\mathsf T},\\
\mathbf L_{\mathrm{fix}}&=\sum_{e\notin V}c_e^0\mathbf a_e\mathbf a_e^{\mathsf T}
\end{aligned}
\tag{2}
$$

> [!info] The exact constrained problem
> **Definition.** Find finite numbers $x_e$ satisfying
>
> $$
> \boxed{\begin{gathered}
> x_e\ge0\quad(e\in V),\\
> \mathbf L(\boldsymbol x)|_{\mathbf1^\perp}\succ0,\\
> R_{ab}(\boldsymbol x)=R^*_{ab}\quad(a<b,\ a,b\in P)
> \end{gathered}}
> \tag{3}
> $$
>
> Formula (2) already preserves all zeros on $Z$ and all fixed couplings. Positive definiteness on $\mathbf1^\perp$ means that the graph is connected.

The requirement $x_e\ge0$ allows some permitted couplings to be removed. If all conductances on $V$ must be positive, replace it by $x_e>0$. Strict positivity and nonnegativity define different solution regions; example (1) lies on the boundary of the latter.

If $P=\Omega$, the full resistance matrix is specified and the solution is unique or nonexistent: it remains to check constraints on the Laplacian recovered by [[Joint Variation of Resistances#Solving the matrix equation|the prescribed-resistance inversion formula]]. For a proper subset $P$, there may be multiple solutions.

## Eliminating internal vertices

Set $I=\Omega\setminus P$. For a connected graph with nonnegative conductances, matrix $\mathbf L_{II}$ is positive definite. Eliminating internal potentials gives the response matrix

$$
\boxed{\mathbf\Lambda_P(\boldsymbol x)
=\mathbf L_{PP}-\mathbf L_{PI}\mathbf L_{II}^{-1}\mathbf L_{IP}}
\tag{4}
$$

For empty $I$, set $\mathbf\Lambda_P=\mathbf L$. This is the Laplacian of a graph on $P$ preserving every resistance between its vertices. A proof through potential elimination and polyform factorization is given in [[Vertex Elimination and Induced Couplings#Response at the selected vertices|the note on vertex elimination]]. Classically, this is Kron reduction; resistance preservation is stated by Dörfler and Bullo in [Theorem 3.9, item 1](https://arxiv.org/pdf/1102.2950#page=19).

Let $m=|P|$, $\mathbf J_P=\mathbf I_m-\mathbf1\mathbf1^{\mathsf T}/m$. The target resistance table gives

$$
\mathbf\Gamma^*=-\frac12\mathbf J_P\mathbf R_P^*\mathbf J_P
$$

If $\mathbf\Gamma^*$ is positive definite on $\mathbf1_P^\perp$, define $\mathbf\Lambda^*=(\mathbf\Gamma^*)^+$: inversion on the zero-sum space, with zero action on the constant column. Here $\mathbf\Gamma^*$ is the target Greenian on $P$; it generally differs from the principal block of the full Greenian.

> [!info] The equivalent boundary equation
> **Proposition.** Under these conditions, the resistance equalities in (3) are equivalent to
>
> $$
> \boxed{\mathbf\Lambda_P(\boldsymbol x)=\mathbf\Lambda^*}
> \tag{5}
> $$
>
> If $\mathbf\Gamma^*$ is not positive definite on $\mathbf1_P^\perp$, or if $\mathbf\Lambda^*$ has a positive off-diagonal entry, there is no exact solution in the graph class considered.

> [!note]- Proof of the boundary formulation
> **Proof.** By (4), the full and reduced graphs have the same resistances on $P$. On the fixed set $P$, double centering uniquely transforms their complete resistance table into a centered Greenian; inversion on $\mathbf1_P^\perp$ uniquely recovers the Laplacian. This proves equivalence of (3) and (5). Reduction of a graph with nonnegative conductances again gives nonnegative conductances, yielding the necessary sign conditions. $\square$

These target-matrix checks are necessary but insufficient for specified $Z$ and $V$: an admissible graph on $P$ may not be realizable by the permitted internal network.

There is a stronger simple check. Suppose some direct couplings between vertices of $P$ are fixed. Eliminating internal vertices adds nonnegative induced conductances to them. Therefore

$$
-\Lambda^*_{ab}\ge c^0_{ab}
\quad\text{for fixed pairs }ab\subset P
\tag{6}
$$

This also follows by splitting the network into the fixed couplings within $P$ and the remaining network: the former do not enter blocks $\mathbf L_{PI}$ and $\mathbf L_{II}$ and are added directly to its response.

## Which changes the prism permits

Return to the prism and prescribe

$$
R^*_{ab}=k\frac8{15},\qquad
R^*_{ac}=R^*_{bc}=\frac8{15},\qquad k>0
$$

### The target triangle on P

For $0<k<4$, inversion of the target resistance table gives

$$
q^*_{ab}=\frac{15(2-k)}{4k(4-k)},\qquad
q^*_{ac}=q^*_{bc}=\frac{15}{4(4-k)}
\tag{7}
$$

> [!note]- Deriving the target-triangle conductances
> **Proof.** For a triangle with resistances $r_{ab},r_{ac},r_{bc}$, set
>
> $$
> \begin{aligned}
> D={}&2(r_{ab}r_{ac}+r_{ab}r_{bc}+r_{ac}r_{bc})\\
> &-r_{ab}^2-r_{ac}^2-r_{bc}^2
> \end{aligned}
> $$
>
> Solving the three equalities $r_{ij}=(q_{ik}+q_{jk})/\tau$ gives $q_{ij}=2(r_{ik}+r_{jk}-r_{ij})/D$. For $r_{ab}=kr$, $r_{ac}=r_{bc}=r$, we have $D=r^2k(4-k)$. Substitution of $r=8/15$ gives (7). Positive definiteness of the target Greenian is equivalent to $0<k<4$. $\square$

Doubling, $k=2$, requires $q^*_{ab}=0$. But the fixed coupling $c_{ab}=1$ already contributes $1$, and the internal network can add only a nonnegative contribution. Condition (6) fails. The target triangle itself is admissible at $k=2$; the impossibility comes from the prism constraints.

The internal network must supplement the unit couplings to reach (7). Denote the required induced conductances by

$$
\begin{aligned}
\alpha&=q^*_{ab}-1=\frac{4k^2-31k+30}{4k(4-k)},\\
\beta&=q^*_{ac}-1=q^*_{bc}-1=\frac{4k-1}{4(4-k)}
\end{aligned}
\tag{8}
$$

Conditions $\alpha,\beta\ge0$ give a candidate solution region. Attainability of one endpoint needs a separate check.

> [!info] The exact solution region for the prism
> **Theorem.** With fixed unit couplings $ab,ac,bc$ and the specified set $V$, a finite connected solution with nonnegative conductances exists exactly when
>
> $$
> \boxed{\begin{gathered}
> \frac14\le k<k_{\max},\\
> k_{\max}=\frac{31-\sqrt{481}}8\approx1{,}13354
> \end{gathered}}
> \tag{9}
> $$
>
> If all six conductances on $V$ must be strictly positive, the left inequality is strict as well. For an increase of the original resistance, the region is $1\le k<k_{\max}$.

![The Prism Feasibility Interval](<images/The Prism Feasibility Interval.svg>)

*The lower endpoint is included for nonnegative conductances. No finite network attains the upper endpoint. Requiring every variable conductance to be positive excludes both endpoints.*

### Constructing the conductances

The following construction gives an explicit recipe within the feasible interval. On a first reading, proceed to [[#Why the upper endpoint is unattainable|the unattainable upper endpoint]], then return to the conductance calculation.

Let $\alpha>0$, $\beta\ge0$ be given by (8). Choose all three connecting conductances equal to $g$ and set

$$
\begin{aligned}
c_{ad}=c_{be}=c_{cf}&=g,\\
c_{df}=c_{ef}&=\frac{g\beta}{g-3\beta},\\
c_{de}&=\frac{g\,[\alpha g-\beta(2\alpha+\beta)]}{(g-2\alpha-\beta)(g-3\beta)}
\end{aligned}
\tag{10}
$$

It suffices to choose

$$
g>\max\left\{2\alpha+\beta,\ 3\beta,\ \frac{\beta(2\alpha+\beta)}{\alpha}\right\}
\tag{11}
$$

Then for $\beta>0$, all six conductances are positive. At $\beta=0$, we get $c_{df}=c_{ef}=0$ and $c_{de}=g\alpha/(g-2\alpha)>0$, while connectedness is preserved through the fixed face and the three connecting edges.

> [!note]- Proof of the construction and numerical example
> **Proof.** Let $\mathbf H$ be the Laplacian of triangle $def$ in order $d,e,f$. With equal connecting conductances, its contribution to the response on $P$ is
>
> $$
> \mathbf C=g\mathbf I_3-g^2(g\mathbf I_3+\mathbf H)^{-1}
> $$
>
> The required triangle with conductances $\alpha,\beta,\beta$ has eigenvalues $2\alpha+\beta$ and $3\beta$ in directions $(1,-1,0)$ and $(1,1,-2)$. If an eigenvalue of $\mathbf H$ is $h$, the corresponding eigenvalue of $\mathbf C$ is $gh/(g+h)$. Thus the required values of $\mathbf H$ are
>
> $$
> \mu=\frac{g(2\alpha+\beta)}{g-2\alpha-\beta},\qquad
> 3\nu=\frac{3g\beta}{g-3\beta}
> $$
>
> For conductances $c_{de}=(\mu-\nu)/2$, $c_{df}=c_{ef}=\nu$, this gives (10). Condition (11) ensures the required signs.
>
> At $k=1$, we have $\alpha=\beta=1/4$; choosing $g=1$ recovers all original conductances $1$. At $k=9/8$, we have $\alpha=1/69$, $\beta=7/23$. Choosing $g=7$ gives $\mu=\nu=7/20$ and precisely (1). Here the last inequality in (11) is replaced by equality: conductance $de$ is zero. Any $g>7$ in (10) gives the same resistances with strictly positive conductances. $\square$

### Why the upper endpoint is unattainable

At the upper endpoint, the induced contribution between $a$ and $b$ must be zero, while those between $a,c$ and $b,c$ must be positive. In the prism’s finite internal network, the latter two connections also provide a path between $a$ and $b$. Its induced contribution is positive, so the required zero is impossible. The boundary can be approached but not attained with finite conductances.

> [!note]- Proof that the solution region is exact
> **Proof.** From (8) and $0<k<4$: $\beta\ge0$ requires $k\ge1/4$, and $\alpha\ge0$ requires $k\le k_{\max}$. For $1/4\le k<k_{\max}$, construction (10)-(11) gives a solution. At $k=1/4$, we have $\alpha=6$, $\beta=0$; for example, take $g=24$, $c_{de}=12$, $c_{df}=c_{ef}=0$.
>
> It remains to exclude $k=k_{\max}$, where $\alpha=0$, $\beta>0$. Suppose such a solution exists. Write $g_1=c_{ad}$, $g_2=c_{be}$, $g_3=c_{cf}$, and $x=c_{de}$, $y=c_{df}$, $z=c_{ef}$. The two positive induced contributions $ac$ and $bc$ require $g_1,g_2,g_3>0$. Set $\mathbf M=\operatorname{diag}(g_1,g_2,g_3)+\mathbf H$. For the induced conductance $ab$, the Schur complement formula gives
>
> $$
> \alpha=\frac{g_1g_2}{\det\mathbf M}
> \bigl[x(g_3+y+z)+yz\bigr]
> $$
>
> With nonnegative conductances, equality $\alpha=0$ forces $x=0$ and $yz=0$. But with $x=0$, positive contributions $ac$ and $bc$ require $y>0$ and $z>0$, respectively. This is a contradiction.
>
> If all six conductances are strictly positive, all three induced conductances are positive. Thus $\beta=0$ at the left endpoint is also impossible. Within the open interval, (11) ensures strict positivity. $\square$

Admissibility of the target resistance table, necessary sign bounds, and realization in the specified structure are therefore distinct. For this prism, the conditions are fully resolved; for a general graph, check (6) alone is insufficient.

## Finite variations of permitted couplings only

The constraints can be expressed directly using the variation formulas already obtained. Let $t_e=x_e-c_e^0$ for $e\in V$, let matrix $\mathbf U$ consist of columns $\mathbf a_e$, and set

$$
\mathbf D=\operatorname{diag}(t_e),\qquad
\mathbf G=\mathbf U^{\mathsf T}\mathbf{Gr}^0\mathbf U
$$

Here $\mathbf G$ is the Gram matrix of the permitted edges in the original resistance metric. For a pair $a,b\in P$, set

$$
\mathbf z_{ab}=\mathbf U^{\mathsf T}\mathbf{Gr}^0\mathbf a_{ab}
$$

From [[Two Edges and Joint Variation#Dependent directions and a compact matrix form|the joint variation of couplings]],

$$
\begin{gathered}
\Phi=\det(\mathbf I+\mathbf D\mathbf G),\qquad
\mathbf K=(\mathbf I+\mathbf D\mathbf G)^{-1}\mathbf D,\\
R_{ab}(\boldsymbol x)=R^0_{ab}-\mathbf z_{ab}^{\mathsf T}\mathbf K\mathbf z_{ab},\\
\tau(\boldsymbol x)=\tau^0\Phi
\end{gathered}
\tag{12}
$$

> [!info] The finite system with conductance constraints
> **Corollary.** Problem (3) is equivalent to
>
> $$
> \boxed{\begin{gathered}
> t_e\ge-c_e^0\quad(e\in V),\qquad \Phi>0,\\
> \mathbf z_{ab}^{\mathsf T}\mathbf K\mathbf z_{ab}
> =R^0_{ab}-R^*_{ab},\\
> a<b,\quad a,b\in P
> \end{gathered}}
> \tag{13}
> $$
>
> Matrix $\mathbf K$ depends on the unknown $t_e$, so the resistance equalities in (13) are generally nonlinear. There are no variables on $Z$: the parameterization itself preserves zero couplings.

> [!note]- Proof of the finite system
> **Proof.** The Laplacian change is $\sum_{e\in V}t_e[a_e]^2$, and its exterior exponential is multiplied by $\prod_{e\in V}(e+t_e[a_e]^2)$. Formulas (12) follow from expanding these factors and normalizing potentials, as proved in the cited note. Substitution of the target resistances gives (13).
>
> Under $t_e\ge-c_e^0$, all graph conductances are nonnegative. In this class, connectedness is equivalent to positivity of the spanning-tree coefficient: at least one spanning tree must have positive weight. Since $\tau^0>0$, this is equivalent to $\Phi>0$. Thus the determinant sign is sufficient here specifically in conjunction with nonnegative conductances. $\square$

The formulas allow dependent edge directions and zero increments. They do not require inversion of $\mathbf D$ or $\mathbf G$.

## First order and the possibility of compensation

At the current graph state, the resistance differential on $P$ is

$$
d\boldsymbol R_P=-\mathbf S_{P,V}\,d\boldsymbol c_V,
\qquad
(\mathbf S_{P,V})_{ab,e}=(a_{ab}\cdot_M a_e)^2
\tag{14}
$$

Rows are indexed by all vertex pairs in $P$, and columns by permitted pairs $V$. This is a rectangular part of [[One Resistance and Quadric Connectivity#Two matrices on the full set of pairs|the direct response matrix]].

To preserve resistances, an admissible direction must lie in the kernel of $\mathbf S_{P,V}$. For a prescribed first-order increment, solve linear system (14). If a current conductance is zero, a direction admissible for a positive step must also satisfy $dc_e\ge0$. These are first-order conditions; finite changes are checked using (3), (5), or (13).

For the original unit prism, in row order $ab,ac,bc$ and column order $de,df,ef,ad,be,cf$,

$$
\mathbf S_{P,V}=\frac1{225}
\begin{pmatrix}
4&1&1&9&9&0\\
1&4&1&9&0&9\\
1&1&4&0&9&9
\end{pmatrix}
$$

The first three columns form a nonsingular matrix. Hence, in a sufficiently small neighborhood of the original state, any three small resistance changes on $P$ can be realized by changing couplings of the second face, while keeping the connecting conductances equal to $1$. This is a local consequence of the inverse function theorem; the original conductances are strictly positive, and a sufficiently small neighborhood preserves their signs. It does not extend to arbitrary finite changes, as the impossibility of doubling shows.

### Why simply removing unwanted couplings does not work

If the full resistance matrix is prescribed first and the Laplacian is recovered, couplings on $Z$ may appear. Setting them to zero afterwards is itself a conductance variation and generally changes resistances on $P$. Preserving those resistances requires jointly changing permitted couplings and checking the full equality (5) or (13).

The new formulation does not retain [[Joint Variation of Resistances#Which couplings can change|the locality obtained when all other resistances are preserved]]: there, every resistance increment outside the prescribed block was zero. Here they are free. For example, on the path $a-b-c-d-e-f$ with $P=\{a,b\}$, conductance $ef$ can change while $R_{ab}$ is preserved, even though both its endpoints lie outside $P$ and its neighbors.

## When no exact solution exists

Let $\mathcal A$ be the set of finite conductances satisfying the conductance and connectedness constraints of (3), without the resistance equalities. For positive weights $w_{ab}$, define

$$
\Psi(\boldsymbol x)=\frac12\sum_{\substack{a<b\\a,b\in P}}
w_{ab}\bigl(R_{ab}(\boldsymbol x)-R^*_{ab}\bigr)^2
\tag{15}
$$

An exact solution is a point $\boldsymbol x\in\mathcal A$ with $\Psi(\boldsymbol x)=0$. The approximation problem seeks the infimum of this function and checks whether finite admissible conductances attain it. Deviations are measured in resistances; minimizing response-matrix error would be a different problem.

> [!info] Zero limiting error does not imply existence of a solution
> **Corollary of the prism example.** At $k=k_{\max}$, there is no exact finite solution, but
>
> $$
> \inf_{\boldsymbol x\in\mathcal A}\Psi(\boldsymbol x)=0
> $$
>
> Indeed, choose $k_j\uparrow k_{\max}$ and construct exact solutions for $k_j$ using (10)-(11). Their resistances tend to the target values, while the connecting conductances required by this construction grow without bound.

Small numerical error alone therefore does not prove existence of an exact finite solution. If an application imposes upper conductance limits, include them in $\mathcal A$ from the outset. Together with the bound $\lambda_2(\mathbf L)\ge\varepsilon>0$, they make the feasible region compact; on a nonempty such region, the continuous function (15) attains its minimum. These bounds are additional problem data.

## Verification and further calculation

For the general problem, first check consistency of the sets and target resistance table, then response constraints such as (6). If these do not rule out a solution, solve system (5) or (13) with nonnegative conductances. In general, existence does not follow from the number of free couplings or the rank of a linearization at one point.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_constrained_couplings.py) uses exact rational arithmetic. For the prism, it compares full inversion, internal-vertex elimination, spanning-tree and forest sums, finite variation formulas, and the sensitivity matrix. It checks example (1), family (10), the left endpoint, approach to the upper boundary, preservation of all zero and fixed couplings, and the distinction between local conditions and finite realizability.

From the repository root:

    python checks/variations/verify_constrained_couplings.py

Kron reduction, preservation of boundary resistances, and signs of induced couplings are classical results. The formulation with $P,Z,V$, calculation of the prism solution region, and its agreement with variation formulas are presented here with explicit justifications. The general algorithm for finding exact solutions and best approximations is given in [[An Algorithm for Variations with Conductance Constraints]].

Reading order and summary of results: [[en/Graph Transformations and Gluing/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
