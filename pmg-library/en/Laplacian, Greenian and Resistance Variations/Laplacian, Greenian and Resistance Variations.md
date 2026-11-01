---
title: Laplacian, Greenian and Resistance Variations
date: 2026-11-01
updated: 2026-11-01
revision: 1
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: laplacian-greenian-resistance-variations-series-navigation
order: 0
description: 'Reading order for eight notes: direct and inverse variations, exterior exponential factors, quadric connectivity, prescribed resistances, and conductance constraints. Main formulas, applicability, and provenance.'
translated_revision: 2
---

[[ru/Вариации лапласиана, гриниана и резистенсов/Вариации лапласиана, гриниана и резистенсов|Русский]]

This series describes direct and inverse variations on graphs: changes in couplings and the resulting changes in the spanning-tree coefficient, Greenian, and resistances; recovery of conductances from prescribed Greenian or resistance variations; and preservation of zero couplings and nonnegativity when only a restricted set of changes is permitted.

Eight notes lead from simple examples to joint variations and constrained algorithms. Their common algebraic basis is the addition of vector factors to the exterior exponentials of the Laplacian and Greenian. Finite formulas account for the new normalization; matrix inversion supplies an independent check.

## Contents and reading order

| Order | Note | Contents and example |
| ---: | --- | --- |
| 1 | [[One Changing Edge]] | The spanning-tree coefficient, resistances, and a squared inner product. Strengthening one edge of a triangle; removing a bridge. |
| 2 | [[Two Edges and Joint Variation]] | Interaction of two couplings, mixed terms, and multiple factors. Two changing sides of a triangle. |
| 3 | [[One Greenian Coefficient]] | Inverse variation: the spanning-tree coefficient and conductances under one vector contribution. A four-vertex path. |
| 4 | [[Joint Variation of Greenian Coefficients]] | Two contributions, the interaction matrix, and dependent directions. Greenian coefficients of a triangle. |
| 5 | [[One Resistance and Quadric Connectivity]] | Changing one resistance while preserving the others; quadric connectivity and inverse sensitivity matrices. A triangle. |
| 6 | [[Joint Variation of Resistances]] | Two resistances and general increments on a vertex set; solving the finite matrix equation and locating the update. |
| 7 | [[Variations with Conductance Constraints]] | Sets $P,Z,V$, preservation of zero couplings, and the region of nonnegative solutions. A triangular prism. |
| 8 | [[An Algorithm for Variations with Conductance Constraints]] | Numerical search, exact existence checks, global approximation, and an unattainable infimum. A path and a prism. |

For a sequential introduction, follow the table. For direct variations alone, [[One Changing Edge]] and [[Two Edges and Joint Variation]] suffice. The main route for recovering a graph from prescribed resistances passes through [[One Greenian Coefficient]], [[Joint Variation of Greenian Coefficients]], and [[One Resistance and Quadric Connectivity]] to [[Joint Variation of Resistances]]. Problems with forbidden couplings conclude with [[Variations with Conductance Constraints]] and [[An Algorithm for Variations with Conductance Constraints]].

Foundations of the factor derivation are collected in [[Laplacian Exponential]], [[The Canonical Vector Representation of the Greenian]], [[The Greenian Metric and Potentials]], and [[Laplacian and Greenian - Mutual Duality of Exponentials]]. Current conventions are given by [[Core specification]] and [[PMG terminology]].

## Common data and normalizations

The original graph is undirected, its set of $n\ge2$ vertices is fixed, and conductances are nonnegative. Positive-conductance edges form a connected graph. The notation $\tau$ denotes the spanning-tree coefficient, the sum of spanning-tree weights; for unit weights, it is the spanning-tree count.

The forms $L$ and $\mathrm{Gr}$ differ from their coefficient matrices $\mathbf L$ and $\mathbf{Gr}$. In the direct centered representation,

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,
\qquad a_{ij}=a_j-a_i
$$

For $i\ne j$, we have $c_{ij}=-L_{ij}$ and $\gamma_{ij}=-\mathrm{Gr}_{ij}$. Coefficients $\gamma_{ij}$ may have either sign. Matrices $\mathbf L$ and $\mathbf{Gr}$ are mutual inverses on $\mathbf1^\perp$ and annihilate the constant column. Write $\mathbf J=\mathbf I-\mathbf1\mathbf1^{\mathsf T}/n$.

> [!info] Two exterior exponentials
> Set $M=\exp L$, $N=\exp(\mathrm{Gr})$, $T_n=[(a_1\ldots a_n)]^2$. Then
>
> $$
> M_{n-1}=\tau T_n,\qquad
> N_{n-1}=\sigma T_n,\qquad
> \sigma=\frac1{n^2\tau}
> $$
>
> Multiplication here is the exterior multiplication of forms. Mutual duality of exponentials through exterior contraction is not multiplicative inversion. The reference form $T_n$ is the same before and after a variation.

A prime denotes a final value, $\Delta$ a finite increment, and $d$ a differential. All unprimed data in variation formulas refer to the original state.

## Main results

### One edge and one Greenian coefficient

Changing $c_{kl}$ by $t$ adds the factor $e+t[a_{kl}]^2$ to $M$. Set $g_{ij,kl}=a_{ij}\cdot_M a_{kl}$, with the inner product taken in the original resistance metric.

> [!info] Direct variation
> If connectedness is preserved,
>
> $$
> \tau'=\tau(1+tR_{kl}),\qquad
> \Delta R_{ij}=-\frac{t\,g_{ij,kl}^2}{1+tR_{kl}}
> $$
>
> In the differential limit, $\partial R_{ij}/\partial c_{kl}=-g_{ij,kl}^2$. The formula for $\tau'$ remains valid when a bridge is removed; the resistance formula requires a nonzero denominator.

The proof through grades and normalization appears in [[One Changing Edge]]. In the inverse direction, prescribe $\mathrm{Gr}'=\mathrm{Gr}+t[u]^2$ with vector $u$ fixed. Its coordinate column $\mathbf u$ has zero sum. Set

$$
q=\mathbf u^{\mathsf T}\mathbf L\mathbf u,\qquad
\mathbf b=\mathbf L\mathbf u
$$

> [!info] Inverse variation
> For $1+tq\ne0$,
>
> $$
> \tau'=\frac{\tau}{1+tq},\qquad
> \Delta c_{ij}=\frac{t\,b_i b_j}{1+tq},\quad i<j
> $$
>
> For $u=a_{kl}$, we have $b_i=L_{il}-L_{ik}$. The numerator therefore contains the product $(L_{ik}-L_{il})(L_{jk}-L_{jl})$.

This is [[One Greenian Coefficient#Two formulas for one coefficient|the variation of one fixed vector contribution]]. For $u=a_{kl}$, one canonical coefficient $\gamma_{kl}$ changes; for arbitrary $u$, several canonical coefficients may change. Condition $1+tq>0$ preserves positive definiteness of the Greenian; signs of the recovered conductances are checked separately.

### Two factors and several directions

The product of two factors contains a mixed term:

$$
(e+sp)(e+tr)=e+sp+tr+stpr,
\qquad p=[u]^2,\quad r=[v]^2
$$

The squares of $p^2$ and $r^2$ vanish. Their product $pr$ is generally nonzero and gives the Gram determinant of two directions.

> [!info] The joint spanning-tree multiplier
> For two changing couplings $u,v$, set $g_M=u\cdot_Mv$, $R_u=u\cdot_Mu$, $R_v=v\cdot_Mv$. Then
>
> $$
> \frac{\tau'}\tau
> =(1+sR_u)(1+tR_v)-stg_M^2
> $$
>
> For two Greenian contributions, set $q_u=\mathbf u^{\mathsf T}\mathbf L\mathbf u$, $q_v=\mathbf v^{\mathsf T}\mathbf L\mathbf v$, $g_N=\mathbf u^{\mathsf T}\mathbf L\mathbf v$. With a nonzero denominator,
>
> $$
> \frac{\tau'}\tau
> =\frac1{(1+sq_u)(1+tq_v)-stg_N^2}
> $$

Explicit resistance and conductance responses are given in [[Two Edges and Joint Variation]] and [[Joint Variation of Greenian Coefficients]], respectively. For $m$ directions, form $\mathbf U=(\mathbf u_1,\ldots,\mathbf u_m)$ and $\mathbf D=\operatorname{diag}(t_1,\ldots,t_m)$. Both spanning-tree formulas generalize:

$$
\begin{aligned}
\Delta\mathbf L=\mathbf U\mathbf D\mathbf U^{\mathsf T}
&:\quad \frac{\tau'}\tau=\det(\mathbf I_m+\mathbf D\mathbf G_M),\\
\Delta\mathbf{Gr}=\mathbf U\mathbf D\mathbf U^{\mathsf T}
&:\quad \frac{\tau'}\tau=\frac1{\det(\mathbf I_m+\mathbf D\mathbf G_N)}
\end{aligned}
$$

Here $\mathbf G_M=\mathbf U^{\mathsf T}\mathbf{Gr}\mathbf U$, $\mathbf G_N=\mathbf U^{\mathsf T}\mathbf L\mathbf U$; for conductance variations, the columns of $\mathbf U$ are vectors of the selected pairs. The second formula requires a nonzero determinant. Dependent directions are allowed. The joint response accounts for mixed terms, whereas sequential calculation uses updated data and requires nondegenerate intermediate states.

### Prescribed resistances and the finite matrix equation

With fixed vertices, the transformation from resistances to the Greenian is exactly linear:

$$
\Delta\mathbf{Gr}=-\frac12\mathbf J(\Delta\mathbf R)\mathbf J
$$

Changing only $R_{kl}=R_{lk}$ by $\rho$ is represented by two vector contributions. For centroid $h=n^{-1}\sum_i a_i$ and $p_i=a_i-h$,

$$
\Delta\mathrm{Gr}
=\frac\rho4[p_k-p_l]^2-\frac\rho4[p_k+p_l]^2
$$

Substitution into the two-factor formulas gives [[One Resistance and Quadric Connectivity#Explicit finite formulas|changes in the spanning-tree coefficient and all couplings while preserving the other resistances]]. Several independent increments add in $\Delta\mathbf{Gr}$; the responding Laplacian depends on them nonlinearly.

> [!info] Solving the finite equation
> Let $\Delta\mathbf R$ be symmetric with zero diagonal. For a nondegenerate new Greenian,
>
> $$
> \Delta\mathbf L=\frac12\mathbf L'\Delta\mathbf R\mathbf L
> $$
>
> The equation has the explicit solution
>
> $$
> \begin{gathered}
> \mathbf L'=\mathbf L\left(\mathbf I_n-\frac12\Delta\mathbf R\mathbf L\right)^{-1},\\
> \tau'=\frac{\tau}{\det\left(\mathbf I_n-\frac12\Delta\mathbf R\mathbf L\right)}
> \end{gathered}
> $$

If increments are prescribed only within $S$ and all other resistances are preserved, [[Joint Variation of Resistances#Changes on a prescribed vertex set|the reduced calculation]] uses a matrix of size $\lvert S\rvert$ and the original block $\mathbf L_{SS}$. The conductance update is supported on pairs of vertices in $S$ and its original neighbors. This location alone ensures neither the required conductance signs nor preservation of zero couplings.

### Quadric connectivity and inverse sensitivities

> [!info] Two differential transformations
> **Definition.** In the normalization used here, quadric connectivity is
>
> $$
> Lq^{ij,kl}=\frac12\bigl(L_{ik}L_{jl}+L_{il}L_{jk}\bigr)
> $$
>
> On the full set of unordered pairs, set $\mathbf{Lq}=(Lq^{ij,kl})$, $\mathbf S=(g_{ij,kl}^2)$. Then
>
> $$
> \begin{gathered}
> d\boldsymbol R=-\mathbf S\,d\boldsymbol c,\qquad
> d\boldsymbol c=-\mathbf{Lq}\,d\boldsymbol R,\\
> \mathbf S\mathbf{Lq}=\mathbf{Lq}\mathbf S=\mathbf I
> \end{gathered}
> $$

Here $\boldsymbol R$ and $\boldsymbol c$ are columns of independent pair coordinates $i<j$, including pairs whose original conductance is zero. At such points, derivatives are taken in the space of nondegenerate centered forms; admissibility of a direction for nonnegative conductances is checked separately. For the Laplacian matrix, the sign is positive: $d\mathbf L=\mathbf L(d\mathbf R)\mathbf L/2$; the conductance sign changes because $c_{ij}=-L_{ij}$.

The definition, symmetries, and inverse-identity proof are given in [[One Resistance and Quadric Connectivity]]. If only existing edges are retained, the corresponding principal submatrices are generally no longer mutual inverses; the required transformation contains a Schur complement.

### Conductance constraints and the algorithm

In [[Variations with Conductance Constraints]], vertices $P$ specify controlled resistances, pairs $Z$ mandatory zero couplings, and pairs $V$ permitted variable conductances. Sets $Z$ and $V$ are disjoint; the other conductances are fixed. Resistances outside the controlled pairs may change. The freedom needed to meet the constraints therefore comes from the problem formulation itself; locality of a full resistance variation is not guaranteed here.

For a unit triangular prism with fixed edges of the $P$ face and six variable couplings, the target is $R_{12}=8k/15$, $R_{13}=R_{23}=8/15$. The exact region of finite nonnegative solutions is

$$
\frac14\le k<\frac{31-\sqrt{481}}8
$$

If all six variable conductances must be strictly positive, the left endpoint is excluded as well. The construction and boundaries are proved in [[Variations with Conductance Constraints#Which changes the prism permits|the prism analysis]].

> [!info] What the general algorithm provides
> For prescribed $P,Z,V$, first check the available connected structure and necessary conditions on target resistances. Numerical search then uses rows of $\mathbf S$ for controlled pairs within $P$ and columns for couplings in $V$, conductance bounds, and a finite-step check.
>
> For rational or exactly specified real algebraic data, existence reduces to polynomial equalities and inequalities with the essential condition $\tau>0$. Quantifier elimination can decide existence, construct a solution, or determine the global error infimum and whether it is attained.

[[An Algorithm for Variations with Conductance Constraints]] distinguishes an exact solution, a numerical candidate, proved impossibility, and global approximation. Termination of numerical iterations does not prove absence of a solution; stationarity does not prove a minimum. If finite conductances do not attain the infimum, the algorithmic aim is to obtain approximations within a prescribed tolerance in error value. The general exact algorithm may be computationally expensive; the published examples implement numerical search, not a universal quantifier-elimination solver.

## Applicability conditions

> [!note] Separate checks
> - **Nondegeneracy:** denominators and determinants used for inversion are nonzero.
> - **Positive definiteness:** the new form is positive on $\mathbf1^\perp$. For several directions, a positive determinant is insufficient.
> - **Graph signs:** all recovered $c'_{ij}$ are nonnegative.
> - **Prescribed constraints:** forbidden and fixed couplings are preserved, and variable bounds are respected.
>
> At degeneracy, the factor product and its grades remain defined, but normalized inverse formulas may cease to apply. The pseudoinverse of a degenerate form does not replace a solution of the original problem with prescribed finite resistances.

Changing a coefficient at a fixed vector is not a change of the vector itself. Resistance between vertices accounts for the entire network and generally differs from the reciprocal conductance of a single edge. Preserving the entire resistance matrix uniquely determines the recovered Laplacian, whereas prescribing resistances only on $P$ may allow multiple solutions.

## Provenance and status of the results

This table distinguishes established matrix identities, their PMG expressions, and derivations developed in detail in the series. An independent proof or computational check does not establish scientific priority.

| Result | Source or derivation | Role in PMG | Status of a novelty claim |
| --- | --- | --- | --- |
| Inversion under one or several vector contributions | Sherman-Morrison and Woodbury identities; references in [[Further Reading for the PMG Introductory Series]] | Derivation through factors, potentials, and changing normalization | Established matrix result |
| Reciprocal spanning-tree multipliers for the Laplacian and Greenian | [[Laplacian and Greenian - Mutual Duality of Exponentials]]; factor derivations in [[Joint Variation of Greenian Coefficients]] | Agreement of top grades with fixed $T_n$ | PMG presentation; no priority claimed |
| Finite recovery from resistances | Double centering and inversion; derivation in [[Joint Variation of Resistances]] | Passage from independent resistances to vector factors and conductances | Derivation from classical methods |
| Quadric connectivity and inverse sensitivity matrices | Direct proof in [[One Resistance and Quadric Connectivity]] | Differential relation between full pair coordinates | PMG term; no priority claimed for the identity |
| Boundary constraints and the prism region | Kron reduction and calculation in [[Variations with Conductance Constraints]] | The $P,Z,V$ formulation and an exact example of a solution region | Reduction is established; no priority claimed for the calculation |
| Search and rigorous certificates | Gauss-Newton, backtracking, and quantifier elimination; sources and application in [[An Algorithm for Variations with Conductance Constraints]] | Distinguishing numerical search, existence, minimum, and infimum | Application of established algorithmic tools |

## Reproducible checks

The series checks compare factor expansions by grade, exterior contraction and normalizations, direct matrix inversion, enumeration of trees and separating forests, and recovery of resistances and conductances. Examples include a weighted edge, a triangle, a four-vertex path, a cycle, and a prism; dependent directions, negative Greenian coefficients, and degeneracy are covered.

Each note links to its verification script. The [cross-series consistency check](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_series_consistency.py) additionally takes 17 finite variations through “conductances - Greenian coefficients - resistances - recovered conductances” in exact rational arithmetic. Run from the repository root:

    python checks/variations/verify_series_consistency.py

The [numerical constrained-search example](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/constrained_search.py) uses NumPy. Its result is a numerical candidate; exact checks and proofs have a separate status.
