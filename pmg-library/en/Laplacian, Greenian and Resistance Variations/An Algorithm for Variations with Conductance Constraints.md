---
title: An Algorithm for Variations with Conductance Constraints
date: 2026-10-31
updated: 2026-11-01
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: variations-constrained-algorithm
lang: en
description: Finding nonnegative conductances for prescribed P, Z, and V, proving impossibility of an exact solution, and determining a best approximation or an unattainable limit.
order: 8
translated_revision: 4
---

[[ru/Вариации лапласиана, гриниана и резистенсов/Алгоритм вариаций при ограничениях на связи|Русский]]

[[Variations with Conductance Constraints]] introduced three sets: vertices $P$ whose pairwise resistances are controlled; pairs $Z$ whose couplings remain zero; and pairs $V$ whose conductances may change. We now construct a calculation algorithm.

We first examine an example where one formula reveals every outcome. Then we derive a numerical search step from the matrix of squared inner products. Finally, we reduce existence and global approximation to exact polynomial problems. The last method gives a general criterion but may require substantially more computation.

## Three outcomes on a simple path

Take the path $1-2-3$. Conductance $12$ is fixed at $1$, conductance $23$ equals $x\ge0$, and coupling $13$ is forbidden:

$$
P=\{1,3\},\qquad Z=\{13\},\qquad V=\{23\}
$$

![A path with fixed conductance 1 and variable conductance x](<images/Constrained Search on a Path.svg>)

Connectedness requires $x>0$. The two edges are in series, so

$$
R_{13}(x)=1+\frac1x
\tag{1}
$$

**An exact solution.** For a prescribed $R^*_{13}=r>1$,

$$
x=\frac1{r-1}
$$

For example, $r=2$ gives $x=1$.

**An unattainable limit.** If $r=1$, there is no finite solution. With unit weight, the error is

$$
\Psi(x)=\frac12\bigl(R_{13}(x)-1\bigr)^2=\frac1{2x^2}
$$

It tends to zero as $x\to\infty$, but no finite conductance gives zero error. Nor is there a best finite approximation: every value found can be improved.

**An attained best approximation.** If the problem additionally imposes $x\le2$, the minimum is attained:

$$
x=2,\qquad R_{13}=\frac32,\qquad \min\Psi=\frac18
$$

This is a problem with an upper bound. Such a bound cannot be introduced merely for computational convenience and the result declared a solution of the original unbounded problem.

## Data and the feasible region

The vertex set $\Omega$ is fixed; $n=\lvert\Omega\rvert$. All conductances are finite. Assume $2\le\lvert P\rvert\le n$ and $Z\cap V=\varnothing$. Conductances on $Z$ are zero; on other pairs outside $V$, they are fixed and nonnegative. Denote the corresponding matrix by $\mathbf L_{\mathrm{fix}}$.

Variables $x_e$ are **final conductances**, not increments. Without additional bounds, use $\ell_e=0$, $u_e=+\infty$. Lower bounds $\ell_e$ are finite; upper bounds $u_e$ may be finite or equal to $+\infty$. Always require $0\le\ell_e\le u_e$. Pairs with $\ell_e=u_e$ can be moved immediately to the fixed part.

> [!info] Feasible conductances and error
> **Definition.** For $e=ij$, set $\mathbf a_e=\mathbf e_j-\mathbf e_i$ and
>
> $$
> \mathbf L(\boldsymbol x)=\mathbf L_{\mathrm{fix}}+\sum_{e\in V}x_e\mathbf a_e\mathbf a_e^{\mathsf T}
> $$
>
> The feasible region $\mathcal A$ consists of tuples satisfying
>
> $$
> \ell_e\le x_e\le u_e\quad(e\in V),\qquad
> \mathbf L(\boldsymbol x)|_{\mathbf1^\perp}\succ0
> \tag{2}
> $$
>
> For target resistances $r^*_{ab}=R^*_{ab}$ and positive weights $w_{ab}$, define
>
> $$
> \Psi(\boldsymbol x)=\frac12
> \sum_{\substack{a<b\\a,b\in P}}
> w_{ab}\bigl(R_{ab}(\boldsymbol x)-r^*_{ab}\bigr)^2
> \tag{3}
> $$
>
> An exact solution satisfies $\Psi=0$. A global best approximation, if it exists, attains $\inf_{\mathcal A}\Psi$.

Zero couplings are preserved by the expression $\mathbf L(\boldsymbol x)$ itself: there are no variables on $Z$. Nonnegativity allows some permitted couplings to become zero, but positive-conductance edges must form a connected graph. Resistances outside the controlled pairs may change.

If only some pairs in $P$ are controlled, retain only the corresponding rows and summands below. The full target-matrix check in the next section then becomes a feasible-completion problem; checking an arbitrarily filled-in table is invalid.

## Checks before iteration

### Does any feasible graph exist?

Construct the graph containing fixed positive couplings and every pair $e\in V$ for which $u_e>0$.

> [!info] Checking whether the feasible region is nonempty
> **Proposition.** For consistent bounds $\ell_e,u_e$, the region $\mathcal A$ is nonempty if and only if this graph is connected.

> [!note]- Proof of the connectedness check
> **Proof.** No feasible conductance can create an edge outside the constructed graph, so its disconnectedness rules out a solution. If it is connected, each available pair can be assigned a finite positive conductance within its bounds. The resulting positive subgraph is connected, so (2) holds. $\square$

This checks existence of a feasible graph before considering target resistances. It also supplies a starting point for the search. If the original conductances already satisfy the bounds, starting with them is convenient.

### Are the target resistances compatible with the constraints?

For a complete table on $P$, check symmetry and a zero diagonal. Set $p=\lvert P\rvert$ and

$$
\mathbf J_P=\mathbf I_p-\frac1p\mathbf1\mathbf1^{\mathsf T},\qquad
\mathbf\Gamma^*=-\frac12\mathbf J_P\mathbf R^*_P\mathbf J_P
$$

An exact solution requires $\mathbf\Gamma^*$ to be positive definite on $\mathbf1_P^\perp$. The target response is then defined:

$$
\mathbf\Lambda^*=(\mathbf\Gamma^*)^+
$$

As proved in [[Variations with Conductance Constraints#Eliminating internal vertices|the boundary formulation]], its off-diagonal entries must also be nonpositive, and

$$
-\Lambda^*_{ab}\ge c^{\mathrm{fix}}_{ab},\qquad a\ne b,\quad a,b\in P
\tag{4}
$$

Here $c^{\mathrm{fix}}_{ab}$ is the fixed direct conductance between these vertices, or zero when no such fixed coupling exists. Failure of any condition excludes an **exact** realization. The approximation problem (3) remains meaningful.

Monotonicity gives further simple bounds. If all $u_e$ are finite, the connected graph at $\boldsymbol x=\boldsymbol u$ gives lower bounds for every resistance. If the graph at $\boldsymbol x=\boldsymbol\ell$ is connected, it gives upper bounds:

$$
R_{ab}(\boldsymbol u)\le R_{ab}(\boldsymbol x)
\le R_{ab}(\boldsymbol\ell)
\tag{5}
$$

Use each side only when its own condition holds. Monotonicity follows from the single-edge variation formula: increasing a conductance cannot increase any resistance.

Passing these checks does not yet prove that an exact solution exists. If $P=\Omega$, however, the entire resistance matrix uniquely determines the Laplacian: recover it and check all couplings, bounds, and connectedness.

## Computing resistances and their sensitivities

Fix a reference vertex $s\in\Omega$. Delete its row and column from $\mathbf L$ and call the resulting matrix $\mathbf A$. The vector $\mathbf v_{ab}$ is obtained by deleting the same coordinate from $\mathbf a_{ab}$.

For each controlled pair $q=ab$, solve

$$
\mathbf A\boldsymbol h_q=\mathbf v_q,\qquad
R_q=\mathbf v_q^{\mathsf T}\boldsymbol h_q
\tag{6}
$$

Matrix $\mathbf A$ is positive definite exactly when the graph is connected. Its factorization serves all right-hand sides; computing the full Greenian is optional.

For the current exterior exponential $M=\exp L(\boldsymbol x)$, [[One Changing Edge#Sensitivity and resistance preservation|the single-edge sensitivity formula]] gives

$$
\frac{\partial R_q}{\partial x_e}=-S_{q,e},\qquad
S_{q,e}=(\mathbf v_e^{\mathsf T}\boldsymbol h_q)^2
=(a_q\cdot_M a_e)^2
\tag{7}
$$

The inner product is taken in the **current** resistance metric. Rows of $\mathbf S$ correspond to controlled pairs, and columns to permitted couplings.

Denote the error vector by $\boldsymbol f=\boldsymbol R_P-\boldsymbol r^*$ and the weight matrix by $\mathbf W=\operatorname{diag}(w_q)$. Then

$$
\nabla\Psi=-\mathbf S^{\mathsf T}\mathbf W\boldsymbol f
\tag{8}
$$

The rank of $\mathbf S$ describes first-order possibilities at this point. Rank deficiency does not prove global impossibility, and a small gradient does not prove a global minimum.

## A practical search step

Linearization says that after changing conductances by $\boldsymbol d$, the error is approximately $\boldsymbol f-\mathbf S\boldsymbol d$. Seek a step that reduces this quantity while respecting conductance bounds.

> [!info] A step respecting conductance constraints
> **Algorithm definition.** Choose $\mu>0$ and solve the convex quadratic problem
>
> $$
> \boxed{\begin{aligned}
> \min_{\boldsymbol d}\quad&
> \frac12\|\mathbf W^{1/2}(\boldsymbol f-\mathbf S\boldsymbol d)\|_2^2
> +\frac\mu2\|\boldsymbol d\|_2^2\\
> \text{subject to}\quad&
> \boldsymbol\ell-\boldsymbol x\le\boldsymbol d
> \le\boldsymbol u-\boldsymbol x
> \end{aligned}}
> \tag{9}
> $$
>
> Here $\|\cdot\|_2$ is the ordinary Euclidean linear norm of a coordinate vector. The term with $\mu$ limits the step size and makes the step unique, including when columns of $\mathbf S$ are dependent.

This is a constrained damped Gauss-Newton step. In particular, (9) can be solved as a bounded linear least-squares problem with matrix and right-hand side

$$
\begin{pmatrix}\mathbf W^{1/2}\mathbf S\\\sqrt\mu\mathbf I\end{pmatrix},
\qquad
\begin{pmatrix}\mathbf W^{1/2}\boldsymbol f\\\boldsymbol0\end{pmatrix}
$$

Such an interface is provided, for example, by [scipy.optimize.lsq_linear](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.lsq_linear.html). Convexity applies to step (9); the full problem (3) is generally nonlinear and nonconvex.

### Accepting a finite step

A full step may be too large for the linearization. Test $\alpha=1,1/2,1/4,\ldots$ in order and choose the first for which the graph at $\boldsymbol x+\alpha\boldsymbol d$ is connected and

$$
\Psi(\boldsymbol x+\alpha\boldsymbol d)
\le\Psi(\boldsymbol x)
+\omega\alpha\,\nabla\Psi^{\mathsf T}\boldsymbol d,
\qquad 0<\omega<1
\tag{10}
$$

After accepting the step, recalculate resistances and $\mathbf S$. Formulas based on the previous state are no longer used as current data.

> [!info] What one step guarantees
> **Proposition.** If $\boldsymbol x\in\mathcal A$ and the exact solution of (9) gives $\boldsymbol d\ne0$, then
>
> $$
> \nabla\Psi^{\mathsf T}\boldsymbol d\le-\mu\|\boldsymbol d\|_2^2<0
> $$
>
> A sufficiently small positive step therefore preserves feasibility and satisfies (10). In exact arithmetic, step selection terminates and decreases $\Psi$.

> [!note]- Proof of error decrease
> **Proof.** The zero step is feasible in (9). Applying the optimality condition at its minimum to the zero step gives
>
> $$
> \nabla\Psi^{\mathsf T}\boldsymbol d
> \le-\boldsymbol d^{\mathsf T}
> (\mathbf S^{\mathsf T}\mathbf W\mathbf S+\mu\mathbf I)
> \boldsymbol d
> $$
>
> This proves strict descent in direction $\boldsymbol d$. Conductance bounds are preserved for $0\le\alpha\le1$ by convexity of the coordinate box. Positive definiteness of $\mathbf A$ is preserved in a sufficiently small neighborhood of the current point. Finally, differentiability of $\Psi$ and $\omega<1$ ensure (10) for sufficiently small $\alpha>0$. $\square$

This justifies a single step, not convergence to a global minimum. At $\boldsymbol d=0$, only stationarity conditions accounting for bounds hold. By themselves, they prove neither a local nor a global minimum. With rounding, monitor the accuracy of solving (9), residual size, connectedness, and actual error decrease separately.

The substitution $x_e=\exp\theta_e$ is inconvenient here: it excludes zero conductances that may be part of an exact solution. Setting small couplings to zero afterwards also requires checking the resistances again.

## A rigorous existence check

Numerical search supplies a useful candidate, but failure does not mean that no solution exists. For a rigorous answer, use spanning-tree and forest coefficients.

Let

$$
\tau(\boldsymbol x)=\det\mathbf A(\boldsymbol x),\qquad
F_q(\boldsymbol x)=
\mathbf v_q^{\mathsf T}\operatorname{adj}(\mathbf A(\boldsymbol x))\mathbf v_q
\tag{11}
$$

Here $\operatorname{adj}$ is the adjugate matrix formed from cofactors. Both expressions are polynomials in the conductances. Combinatorially, $\tau$ is the weighted spanning-tree sum, and $F_{ab}$ is the weighted sum of spanning 2-forests separating $a$ and $b$. These are the same spanning-tree and forest sums obtained from exponential grades in the derivation of conductance variation formulas.

> [!info] A polynomial criterion for exact realization
> **Proposition.** A nonnegative exact solution exists if and only if the following system is feasible:
>
> $$
> \boxed{\begin{gathered}
> \ell_e\le x_e\le u_e\quad(e\in V),\qquad \tau(\boldsymbol x)>0,\\
> F_q(\boldsymbol x)-r^*_q\tau(\boldsymbol x)=0
> \quad\text{for all controlled pairs }q
> \end{gathered}}
> \tag{12}
> $$
>
> For $u_e=+\infty$, omit the corresponding upper inequality. The condition $\tau>0$ is essential: without it, the polynomial equalities may admit disconnected graphs.

> [!note]- Proof of the polynomial criterion
> **Proof.** With nonnegative conductances, $\tau>0$ is equivalent to connectedness. In that case, $\mathbf A^{-1}=\operatorname{adj}(\mathbf A)/\tau$, and (6) gives
>
> $$
> R_q(\boldsymbol x)=\frac{F_q(\boldsymbol x)}{\tau(\boldsymbol x)}
> $$
>
> Thus $R_q=r^*_q$ is equivalent to the corresponding equality in (12). The remaining conditions describe precisely the feasible region. $\square$

For the path in the opening example, $\tau=x$, $F_{13}=x+1$. At $r=2$, equation (12) is $1-x=0$; at $r=1$, it becomes $1=0$. This provides an exact impossibility proof independent of the behavior of iterations.

### Solving the polynomial problem

If the input numbers are rational or exactly represented real algebraic numbers, (12) is a finite system of polynomial equalities and inequalities. Real quantifier-elimination algorithms, such as cylindrical algebraic decomposition (CAD), apply. Their foundations and complexity are discussed in [S. Basu's survey, § 2.1](https://www.math.purdue.edu/~sbasu/raag_survey2011_final-sep4-2014.pdf#page=5).

In practical terms, the conductance space is partitioned into regions where the input polynomials have constant signs. One checks whether a region satisfies every condition in (12); a feasible point is extracted from a nonempty such region. Conductances of an exact solution may be algebraic rather than rational.

This is therefore a finite general algorithm for deciding existence and constructing a solution. Its computational cost may be very high; for many variables, numerical search is usually attempted first. If the exact calculation has not finished, the answer remains **undetermined**, even if several numerical runs fail to find a solution. Approximate measurements require a separately chosen model of input accuracy.

## Global approximation and an unattainable limit

The same polynomial representation can check the quality of a candidate. Set

$$
H(\boldsymbol x)=\sum_q w_q
\bigl(F_q(\boldsymbol x)-r^*_q\tau(\boldsymbol x)\bigr)^2
$$

Then on $\mathcal A$,

$$
\Psi(\boldsymbol x)=\frac{H(\boldsymbol x)}{2\tau(\boldsymbol x)^2}
\tag{13}
$$

> [!info] Checking an attainable error level
> **Definition.** For $\eta\ge0$, let $T(\eta)$ assert the existence of conductances satisfying
>
> $$
> \begin{gathered}
> \boldsymbol\ell\le\boldsymbol x\le\boldsymbol u,\qquad \tau(\boldsymbol x)>0,\\
> H(\boldsymbol x)\le2\eta\tau(\boldsymbol x)^2
> \end{gathered}
> \tag{14}
> $$
>
> This is equivalent to existence of a feasible graph with $\Psi\le\eta$.

Eliminating variables $x_e$ from (14) gives an exact description of the feasible values of $\eta$. For nonempty $\mathcal A$, it has one of two forms:

$$
[\eta_*,+\infty)\qquad\text{or}\qquad(\eta_*,+\infty),
\qquad \eta_* = \inf_{\mathcal A}\Psi
\tag{15}
$$

In the first case, the minimum is attained: substitute $\eta=\eta_*$ into (14) and find the conductances. In the second case, there is no best finite approximation. For any prescribed $\varepsilon>0$, solve (14) at $\eta=\eta_*+\varepsilon$ to obtain conductances whose error is at most $\varepsilon$ above the infimum.

For rational or algebraic data, including weights, the boundary $\eta_*$ is also real algebraic and admits an exact representation. This follows from quantifier elimination for (14). The ray forms in (15) already follow from the definition of infimum and monotonicity of $T(\eta)$ in $\eta$.

In particular, $\eta_*=0$ alone does not establish exact realizability: the left endpoint must belong to the ray. For the path with target resistance $1$, we obtain $(0,+\infty)$; adding the bound $x\le2$ gives $[1/8,+\infty)$.

### Checking an existing candidate

Suppose a feasible candidate $\widehat{\boldsymbol x}$ has been checked exactly and $U=\Psi(\widehat{\boldsymbol x})$. It is unnecessary to compute the entire ray (15) at once. It suffices to check whether any feasible tuple satisfies

$$
H(\boldsymbol x)<2(U-\varepsilon)\tau(\boldsymbol x)^2
\tag{16}
$$

If none does, the candidate lies at most $\varepsilon$ above the global infimum. For $\varepsilon=0$, this certifies a global minimum. Such an exact check requires exact specifications of the candidate and parameters; a rounded printout of a numerical answer is not a certificate.

### When attainment is guaranteed

> [!info] A sufficient condition for a best approximation to exist
> **Proposition.** If all $u_e$ are finite and the graph at $\boldsymbol x=\boldsymbol\ell$ is connected, then (3) attains a global minimum on the entire prescribed conductance box.

> [!note]- Proof of attainment
> **Proof.** Every conductance increase preserves connectedness of the graph at $\boldsymbol\ell$. Thus the entire closed bounded box is feasible, and its matrices $\mathbf A$ are uniformly positive definite. Resistances and $\Psi$ are continuous on this compact set and attain a minimum. $\square$

If the graph at the lower bounds is disconnected, this sufficient condition does not apply, but a minimum may still exist. The path with $0<x\le2$ above is such an example. Upper bounds alone, without connectedness control, do not make $\mathcal A$ closed.

## Calculation workflow

1. **Specify the model.** Fix $P,Z,V$, the other conductances, target resistances, weights, and the bounds actually imposed by the problem. Check consistency.
2. **Check the permitted structure.** Connectedness of the available edges decides whether $\mathcal A\ne\varnothing$. If the region is empty, there is neither an exact solution nor a feasible approximation.
3. **Apply simple obstructions.** Target-response conditions and bounds (5) may immediately prove that no exact solution exists. Continue with approximation if required.
4. **Find a numerical candidate.** Repeat (6)-(10), checking actual resistances, bounds, and connectedness. Stop at the required error, stationarity, or exhaustion of the computational budget.
5. **Certify the required result.** For a candidate with exact rational or algebraic coordinates, check (12) in exact arithmetic; otherwise, solve the existence problem (12). For global approximation, use (14)-(16). Numerical search and exact verification serve different purposes.
6. **Report the result and its status.** Give conductances, actual resistances, error, and the justification for the conclusion.

| Calculation result | What has been established |
|---|---|
| Exact conductances satisfy (12) | A nonnegative exact solution exists |
| A necessary condition is contradicted or (12) is proved infeasible | No exact solution exists |
| A small numerical residual is found | A numerical candidate has the stated error |
| Iteration stops with a nonzero residual | A candidate exists; impossibility of an exact solution is not proved |
| The candidate is feasible and (16) is proved infeasible | A global approximation is obtained within $\varepsilon$ in the value of (3) |
| The left endpoint in (15) is excluded | The minimum is not attained; approximations to the infimum can be sought |

Multiple starting points may improve the numerical result but do not themselves give a global certificate. An additional objective, such as minimizing the change from original conductances among exact solutions, should be posed separately: adding it to (3) would change the original problem.

## Returning to the prism and verification

In [[Variations with Conductance Constraints#The prism example|the prism example]], the target is $R_{12}=8k/15$ with $R_{13}=R_{23}=8/15$. Its known exact solution region tests the statuses of the general algorithm:

- at $k=9/8$, there is a solution $c_{45}=0$, $c_{46}=c_{56}=7/20$, $c_{14}=c_{25}=c_{36}=7$;
- at $k=2$, condition (4) fails, so no exact solution exists;
- at $k=(31-\sqrt{481})/8$, no exact finite solution exists, but the error infimum is zero.

The numerical procedure (9)-(10) is also checked for the feasible target $k=21/20$, starting with all nine conductances equal to $1$. In the reported run, six accepted steps reduced the maximum absolute error of the three resistances below $10^{-11}$. All computed conductances are positive; verification by full centered inversion gives the same resistances.

Existence of an exact solution for this target is independently confirmed by [[Variations with Conductance Constraints#Constructing the conductances|the rational conductance family for the prism]]. For example,

$$
c_{45}=\frac6{35},\qquad c_{46}=c_{56}=\frac{16}{35},\qquad
c_{14}=c_{25}=c_{36}=2
$$

gives exactly $R_{12}=14/25$, $R_{13}=R_{23}=8/15$. The numerical method finds a different conductance tuple: the solution is not unique. Success in this calculation is not used as proof of general convergence.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_constrained_algorithm.py) compares the adjugate matrix, independent enumeration of trees and 2-forests, resistances, and sensitivities in exact rational arithmetic. It uses one edge, a triangle, a four-vertex path, a cycle, and the prism. The three outcomes of the opening example and the polynomial error representation are checked separately.

The [numerical algorithm example](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/constrained_search.py) uses NumPy and solves small instances of (9) by enumerating active bounds. This is a demonstration for a few variables; larger problems require a specialized solver. It returns a numerical candidate and error history but does not declare infeasibility. CAD and a general global solver are not implemented in these scripts.

The [cross-series consistency check](https://github.com/magin67/pmg-notes/blob/v5/checks/variations/verify_series_consistency.py) takes 17 finite variations on a weighted edge, triangle, path, and cycle through conductances, canonical Greenian coefficients, and resistances, and back to conductances. Exact rational arithmetic compares spanning-tree coefficients, top-grade normalizations, the matrix-equation solution, and mutually inverse differential-transition matrices. These calculations check consistency on examples and do not replace general proofs.

From the repository root:

    python checks/variations/verify_constrained_algorithm.py
    python checks/variations/constrained_search.py
    python checks/variations/verify_series_consistency.py

Sensitivity formulas and forest ratios rely on [[One Changing Edge]], and the restriction of variable conductances on [[Variations with Conductance Constraints]]. Gauss-Newton, backtracking, and quantifier elimination are established algorithmic tools. This note applies them to specified $P,Z,V$ while explicitly distinguishing a numerical result, exact existence, a global minimum, and an unattainable limit; no scientific priority is claimed.

Reading order and summary of results: [[en/Laplacian, Greenian and Resistance Variations/Laplacian, Greenian and Resistance Variations|Laplacian, Greenian and Resistance Variations]].
