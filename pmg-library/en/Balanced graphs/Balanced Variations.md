---
title: Balanced Variations
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: balanced-graph-variations
lang: en
description: 'Exact balanced variations: rank-one bilinear updates, exchanging recipients, adding a directed cycle, and inserting a vertex into an arc.'
order: 5
source_revision: 2
---

A local change to a balanced graph must preserve equality of incoming and outgoing weights at every vertex. Changing one directed arc breaks balance; coordinated changes to several arcs can have a particularly simple polyform expression.

Our basic tool is a variation $t[u,v]$ with affine vectors $u,v$. Its square vanishes, so the entire exponential changes by one multiplication by $e+t[u,v]$. Exchanging two recipients and inserting a vertex into an arc provide graph applications. Adding a directed cycle is another important balance-preserving operation.

## Conditions for preserving balance

Let $G$ be a loopless balanced graph on fixed vertices $a_1,\ldots,a_n$, $n\ge2$, with arc weights $f_{ij}\ge0$. Use the outgoing convention:

$$
L_{ii}=\sum_j f_{ij},\qquad L_{ij}=-f_{ij}\quad(i\ne j)
$$

Write $\mathbf L$ for the matrix and $L$ for its polyform. Weight changes $\delta f_{ij}$ preserve balance exactly when

$$
\sum_j\delta f_{ij}=\sum_j\delta f_{ji}\quad\text{for all }i
$$

In matrix form, this means

$$
\boxed{\Delta\mathbf L\,\mathbf1=0,\qquad
\mathbf1^{\mathsf T}\Delta\mathbf L=0}
\tag{1}
$$

A graph with nonnegative weights also requires $f_{ij}+\delta f_{ij}\ge0$. Algebraic balance alone does not ensure this inequality.

Let $V$ be the formal vertex space, $\varepsilon(a_i)=1$ its affine-weight functional, and $W=\ker\varepsilon$. As shown in [[The Bilinear Laplacian of a Balanced Graph]], every $[u,v]$ with $u,v\in W$ has zero row and column sums. Linear combinations automatically satisfy (1); conversely, every matrix with these zero sums has a representation by forms on $W$.

This describes all algebraic balanced variations on a fixed vertex set. Graph admissibility depends on the signs of the resulting weights.

## An elementary bilinear variation

Retain $[X,Y][U,V]=[XU,YV]$ and $e=[1,1]$. The exponential $M=\exp L$ uses polyform multiplication, as in [[The Laplacian Exponential of a Balanced Graph]], and differs from the matrix exponential.

> [!info] Exact variation formula
> **Theorem.** Let $u,v\in W$, $H=[u,v]$, and $L_t=L+tH$. For every $t\in\mathbb R$,
>
> $$
> \boxed{M(t)=\exp L_t=M(e+tH)=M+tMH}
> \tag{2}
> $$
>
> This is an algebraic identity. A graph interpretation requires nonnegative weights for $L_t$.

> [!note]- Proof
> **Proof.** Vector exterior self-products vanish, so $H^2=[u\wedge u,v\wedge v]=0$ and $\exp(tH)=e+tH$. Polyform multiplication is commutative and all series are finite, hence $\exp(L+tH)=(\exp L)(\exp tH)$. $\square$

Writing $M_k$ for grade $k$ gives

$$
M_k(t)=M_k+tM_{k-1}H,\qquad k\ge1
$$

Dependence on $t$ is exactly linear in every grade. For $u=v$, the variation is quadratic, $t[u]^2$. If $u=(ab)$, it adds the same weight $t$ to both $a\to b$ and $b\to a$.

## Change in the spanning-tree coefficient

On the fixed vertex set, define $T_n=[(a_1\ldots a_n)]^2$ and the linear functional $\tau(P)$ by $P_{n-1}=\tau(P)T_n$. For $M=\exp L$, the coefficient $\tau(M)=\tau(G)$ is the common principal minor of order $n-1$, or the sum of tree weights toward one fixed root. This is proved in [[The Laplacian Exponential of a Balanced Graph#The spanning-tree form and common coefficient|the spanning-tree form section]]. It vanishes when $G$ is disconnected.

Applying the functional to (2) gives

$$
\boxed{\tau(G_t)=\tau(G)+t\,\tau(M[u,v])}
\tag{3}
$$

In the notation of the [[Core specification#Potential and the metric identity|form potential]], put $u_M(H)=\tau(MH)$. This algebraically extends the definition to a balanced-graph exponential without yet assuming a metric interpretation. The coefficient of $t$ in (3) is $u_M(H)$, involving only $M_{n-2}$.

Equation (3) remains valid when $\tau(G)=0$. Division by the original coefficient requires it to be nonzero.

### A matrix check and argument order

Choose reference vertex $a_r$ and basis $b_i=a_i-a_r$, $i\ne r$. Let $\mathbf C=\mathbf L_{\widehat r,\widehat r}$ be the coefficient matrix in this basis, and let $\mathbf u,\mathbf v$ be the coordinate columns of $u,v$. Then

$$
\mathbf C_t=\mathbf C+t\mathbf u\mathbf v^{\mathsf T}
$$

If the original graph is connected, $\mathbf C$ is invertible and

$$
\boxed{\frac{\tau(G_t)}{\tau(G)}
=1+t\,\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u}
\tag{4}
$$

> [!note]- Independent determinant derivation
> **Proof.** Factor out $\mathbf C$ and put $\mathbf x=\mathbf C^{-1}\mathbf u$. In the column expansion of $\det(\mathbf I+t\mathbf x\mathbf v^{\mathsf T})$, selecting two or more update columns gives zero because they are proportional to $\mathbf x$. The constant term is $1$ and the linear terms sum to $t\sum_i v_i x_i$. Thus
>
> $$
> \det(\mathbf C+t\mathbf u\mathbf v^{\mathsf T})
> =\det\mathbf C\,(1+t\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u)
> $$
>
> Principal minors equal spanning-tree coefficients, giving (4). The updated matrix $\mathbf C_t$ may be singular. $\square$

Comparing (3) and (4) gives

$$
\frac{\tau(M[u,v])}{\tau(M)}=\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u
$$

The order $\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u$ matters: a nonsymmetric Laplacian does not permit replacing it by $\mathbf u^{\mathsf T}\mathbf C^{-1}\mathbf v$. The normalized potential therefore cannot be assumed to be a symmetric inner product. Its directional meaning is developed in [[One-Way Resistance and Hitting Times]], and its symmetric and circulation parts in [[Resistance Geometry and Circulation]].

For an admissible nonnegative graph $G_t$ with connected original $G$, the condition $1+t\mathbf v^{\mathsf T}\mathbf C^{-1}\mathbf u>0$ is equivalent to retaining connectedness. For $u=v=(ab)$, the factor becomes the familiar $1+tR_{ab}$ from [[Variation of a Single Edge]].

## Reassigning two couplings

Choose four distinct vertices $a,b,c,d$. Decrease weights of $a\to c$ and $b\to d$ by $t$, and increase those of $a\to d$ and $b\to c$ by $t$. Every incoming and outgoing total is preserved: the outgoing allocation changes at $a,b$, and the incoming allocation at $c,d$.

The full admissible interval depends on four weights:

$$
-\min(f_{ad},f_{bc})\le t\le\min(f_{ac},f_{bd})
$$

The unit contribution of $x\to y$ is $[x,x-y]$. Hence

$$
\begin{aligned}
\Delta L
&=t\bigl([a,a-d]+[b,b-c]-[a,a-c]-[b,b-d]\bigr)\\
&=t[a-b,c-d]=t[(ab),(cd)]
\end{aligned}
$$

One bilinear form therefore describes changes to four arcs, and

$$
M(t)=M\bigl(e+t[(ab),(cd)]\bigr)
$$

### Two directed 2-cycles become one directed 4-cycle

Start with unit 2-cycles $a\leftrightarrow c$ and $b\leftrightarrow d$, reassigning $a\to c$ and $b\to d$. At $t=1$, the result is the unit cycle $a\to d\to b\to c\to a$.

![[Reassigning Two Couplings.svg]]

*All arcs in the two endpoint diagrams have weight $1$. Orange arcs are reassigned; gray arcs are retained. Two separate 2-cycles become one 4-cycle. For $0<t<1$, old orange arcs have weight $1-t$ and new ones weight $t$; all incoming and outgoing totals remain $1$.*

The original exponential is

$$
M_0=\bigl(e+[(ac)]^2\bigr)\bigl(e+[(bd)]^2\bigr)
$$

Put $H=[(ab),(cd)]$. Then

$$
M(t)=M_0(e+tH),\qquad
(M_0)_2H=[(ac)(bd)(ab),(ac)(bd)(cd)]=T_4
$$

For the last equality, use $u=b-a$, $v=c-a$, $w=d-a$: both exterior arguments equal $uvw$. Consequently,

$$
\boxed{\tau(G_t)=t,\qquad 0\le t\le1}
\tag{5}
$$

Independently, consider trees toward $a$. Arcs $c\to a$ and $d\to b$ are forced. Choosing $b\to d$ would create a cycle, leaving $b\to c$ of weight $t$. For $t>0$, there is exactly one tree, $d\to b\to c\to a$, of weight $t$; it disappears at $t=0$.

The graph is disconnected at $t=0$ and connected for $t>0$; the highest nonzero exponential grade rises from $2$ to $3$. At the endpoints these are [[Balanced Graphs and Spanning-Tree Potentials#Degree-one balanced graphs and permutations|derangement digraphs]]. At intermediate values, $a,b$ each have two outgoing arcs, although outgoing weight stays $1$. In the gift model, the endpoint operation exchanges two donors' recipients.

## Adding a directed cycle

Let $C$ be a unit directed cycle of length $k\ge2$ on existing vertices, with Laplacian $L_C$. Adding weight $t$ to all its arcs preserves balance:

$$
L_t=L+tL_C,\qquad M(t)=M\exp(tL_C)
$$

For $t\ge0$, nonnegativity is automatic. For $t<0$, require $t\ge-\min_{(i\to j)\in C}f_{ij}$.

The vector space on the cycle's $k$ vertices has dimension $k-1$. Therefore $L_C^k=0$ and

$$
\boxed{\exp(tL_C)=\sum_{j=0}^{k-1}\frac{t^jL_C^j}{j!}}
\tag{6}
$$

Unlike a single bilinear form, a cycle Laplacian has a nonzero square when its length exceeds $2$. The components of $M(t)$ and its spanning-tree coefficient are polynomials in $t$ of degree at most $k-1$. For nonnegative original weights, the polynomial $\tau(G_t)$ has nonnegative coefficients, by its directed spanning-tree expansion.

### Directed 2- and 3-cycles

For a 2-cycle, $L_C=[(ab)]^2$, giving factor $e+t[(ab)]^2$.

For a unit 3-cycle on $a,b,c$, the [[The Laplacian Exponential of a Balanced Graph#Example: the unit directed 3-cycle|direct exponential calculation]] gives $L_C^2=2T_3$ and $L_C^3=0$. Hence

$$
\exp(tL_C)=e+tL_C+t^2T_3,\qquad T_3=[(abc)]^2
$$

For example, add a reverse cycle of weight $t\ge0$ to the unit cycle $a\to b\to c\to a$. Then

$$
L_t=L_{abc}+tL_{acb},\qquad
\boxed{\tau(G_t)=1+t+t^2}
\tag{7}
$$

For $t>0$, there are exactly three trees toward $a$: $b\to c\to a$ of weight $1$; arcs $b\to a$, $c\to a$ with product $t$; and $c\to b\to a$ of weight $t^2$. Their sum independently verifies (7). At $t=0$, only the first remains. At $t=1$, the graph is a symmetric triangle with coefficient $3$.

Thus the number of added cycles differs from the number of elementary bilinear factors. Even one cycle can produce several powers of the parameter.

## Inserting a vertex into a directed arc

Suppose $G$ contains $a\to c$ of weight $q>0$. Add a new vertex $b$ and replace the arc by $a\to b\to c$, assigning weight $q$ to both new arcs. No other arc meets $b$.

Vertices $a,c$ retain their incoming and outgoing totals. Both totals at $b$ are $q$, so the new graph $G'$ is balanced.

![[Inserting a Vertex into a Directed Arc.svg]]

*An arc $a\to c$ of weight $q$ is replaced by two successive arcs of the same weight. Vertex $b$ is new; the rest of the graph is retained. The Laplacian change is $-q[(ab),(bc)]$.*

To compare polyforms, embed the old space into the space containing $b$. Initially its Laplacian row and column are zero. The difference is

$$
\begin{aligned}
\Delta L
&=q\bigl([a,a-b]+[b,b-c]-[a,a-c]\bigr)\\
&=q[b-a,b-c]=-q[(ab),(bc)]
\end{aligned}
$$

Equation (2) gives the exact identity

$$
\boxed{M'=M\bigl(e-q[(ab),(bc)]\bigr)}
\tag{8}
$$

Multiplication now takes place on $n+1$ vertices. The original $M$ has no grade-$n$ component, so its spanning-tree coefficient relative to the new vertex set is zero. The old $\tau(G)$ is extracted from grade $n-1$ on the old set. Thus normalized formula (4) cannot be applied to (8) while retaining the old meaning of $\tau$.

### The spanning-tree coefficient after insertion

> [!info] Vertex insertion and trees
> **Theorem.** Replacing an arc of weight $q$ by two successive arcs of the same weight gives
>
> $$
> \boxed{\tau(G')=q\,\tau(G)}
> \tag{9}
> $$
>
> Each coefficient uses its own vertex set. Insertion into a unit arc preserves the coefficient.

> [!note]- Proof using directed trees
> **Proof.** Fix an old vertex as root $r$. For each original tree toward $r$, there are two cases.
>
> If it contains $a\to c$, replace that arc by $a\to b\to c$. The weight is multiplied by $q^2/q=q$.
>
> If it does not, add only $b\to c$. This attaches the new vertex and also multiplies the weight by $q$.
>
> The correspondence is reversible. Every new tree toward an old root must contain $b\to c$. If $a\to b$ is also present, contract the two-arc path to $a\to c$. Otherwise delete $b$ and its sole tree arc $b\to c$. Tree-weight sums therefore differ by factor $q$. Balance identifies each sum with its graph's common spanning-tree coefficient. $\square$

For a disconnected original graph, both sides of (9) vanish: insertion does not join components. Identity (8) also needs no connectedness.

### Check on a directed 2-cycle

The original $a\leftrightarrow c$ with weights $q$ has $\tau(G)=q$. Insertion produces $a\to b\to c\to a$ with weights $q$ and $\tau(G')=q^2$.

Check directly with $u=b-a$, $v=c-b$, so $c-a=u+v$ and $uv=(abc)$:

$$
M=e+q[u+v]^2,\qquad
M'=\bigl(e+q[u+v]^2\bigr)(e-q[u,v])
$$

The grade-two component is

$$
-q^2[(u+v)u,(u+v)v]
=-q^2[-uv,uv]=q^2[(abc)]^2
$$

This gives the same coefficient $q^2$. The negative sign of the variation form agrees with positive spanning-tree weights.

## Comparing the operations

Here $M$ is the original exponential. The first three rows retain the vertex set; the last enlarges it.

| Operation | Laplacian change | Variation factor | Incoming/outgoing weights and spanning-tree coefficient |
| --- | --- | --- | --- |
| Equal addition to opposite arcs | $t[(ab)]^2$ | $e+t[(ab)]^2$ | Both totals at $a,b$ increase by $t$; $\tau(G_t)$ is linear in $t$ |
| Reassigning two couplings | $t[(ab),(cd)]$ | $e+t[(ab),(cd)]$ | Every incoming and outgoing total is preserved; $\tau(G_t)$ is linear in $t$ |
| Adding a directed $k$-cycle | $tL_C$ | $\exp(tL_C)$, of degree $k-1$ in $t$ | Both totals at each cycle vertex increase by $t$; $\deg_t\tau(G_t)\le k-1$ |
| Inserting a vertex into an arc of weight $q$ | $-q[(ab),(bc)]$ | $e-q[(ab),(bc)]$ | Old totals are preserved; both new totals are $q$; $\tau(G')=q\tau(G)$ |

Preserving balance keeps the calculation within boundary forms. The variation determines the complexity of $\exp(\Delta L)$; extracting the top grade gives the spanning-tree change. When the vertex count changes, the space dimension and coefficient-extraction functional must be tracked separately.

Equation (3) gives the bilinear form potential an algebraic meaning as the coefficient of a change in $\tau$. Its relation to the metric, symmetry, and circulation is developed in [[One-Way Resistance and Hitting Times]] and [[Resistance Geometry and Circulation]].

## Sources and connections

The variation identities follow here from polyform multiplication. The matrix check uses the determinant expansion for a rank-one update. Exterior powers and minors of bilinear forms are treated in double-form theory [1, §2.1], without symmetry assumptions. The proof of (9) uses the directed matrix-tree theorem [2] under our Laplacian convention.

1. M. L. Labbi. [On some algebraic identities and the exterior product of double forms](https://arxiv.org/abs/1112.1346). *Archivum Mathematicum* **49** (2013), 241-271. [DOI: 10.5817/AM2013-4-241](https://doi.org/10.5817/AM2013-4-241). §1.1: double-form multiplication; §2.1: exterior powers and minors.
2. A. Postnikov, notes by A. Lin. [Lecture 29: Proof of Directed Matrix Tree Theorem based on induction](https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/4b3d3325c633bfb7fdea92ab6d6f6d1e_MIT18_212S19_lec29.pdf). *18.212 Algebraic Combinatorics*, 2019. The directed matrix-tree theorem.

Related library notes:

- [[Balanced Graphs and Spanning-Tree Potentials]]: balance, connectedness, rooted trees, and permutation digraphs.
- [[The Bilinear Laplacian of a Balanced Graph]]: affine-vector representations and reference vertices.
- [[The Laplacian Exponential of a Balanced Graph]]: the finite exponential, determinant coefficients, and directed forests.
- [[Variation of a Single Edge]]: symmetric variations, spanning-tree coefficients, and effective resistance.
- [[The Circulation Form]]: the skew-symmetric cycle part and its distinction from the full Laplacian.
