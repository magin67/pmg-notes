---
title: "Forest Coefficients: Grade, Components, and Corank"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: forest-coefficients-grade-components-and-corank
lang: en
description: "Three indices for forest coefficients, generating functions by grade and corank, Laplacian and Greenian representations, computation through partitions and deletion-contraction, and a specialization of the Tutte polynomial."
order: 2
---

Forest coefficients collect the weights of independent edge sets of a given size. They are determined by the weighted cycle matroid and turn the dependence structure into computable graph characteristics. This passage and its connection with gluing invariants are introduced in [[The Cycle Matroid and Exterior Products of Edges]].

Here we reconcile three ways of indexing the same forests: edge count, component count, and corank. We then construct two generating functions, compare them with the Laplacian and Greenian exponentials, and give methods for computing their coefficients. The main methods are summation over vertex partitions and deletion-contraction; unit weights give a forest specialization of the Tutte polynomial.

Ordinary forest sums, rooted sums, and canonical Greenian forest sums remain distinct throughout. Their relationships do not allow one to replace another in computations.

## Which forests are counted?

Let $G=(\mathcal V,E)$ be a finite undirected graph on $n\ge1$ vertices. Existing edges have positive conductances $c_\ell$. The main model is a simple graph; recursions allow separately labeled parallel edges and loops arising from contraction.

**Definition.** A spanning forest is an acyclic subgraph on the entire vertex set $\mathcal V$. Isolated vertices are included. Maximality under inclusion is not required, and no roots are chosen in its components.

In a multigraph, a loop is a cycle of length $1$, and two parallel edges form a cycle of length $2$. Thus a forest contains no loops and cannot contain two edges with the same endpoints. This convention agrees with linear dependence of the corresponding edge vectors.

The weight of a forest is

$$
w(F)=\prod_{\ell\in E(F)}c_\ell
$$

For the empty edge set, $w(F)=1$. Its subgraph contains all $n$ isolated vertices.

**Definition.** The forest coefficient of grade $g$ is

$$
\boxed{
f_g(G)=\sum_{\substack{F\text{ a spanning forest of }G\\\#E(F)=g}}w(F)
}
\tag{1}
$$

This continues the notation of [[Forest Coefficients and the Laplacian Polynomial]]. With unit conductances, $f_g$ counts forests with $g$ edges.

Let $\kappa(G)$ be the number of components of the original graph, including isolated vertices, and put

$$
r=n-\kappa(G)
$$

This is the rank of the cycle matroid and the maximum number of edges in a forest. Set $f_g=0$ for $g<0$ or $g>r$. Always $f_0=1$.

If the graph components are $G_1,\ldots,G_{\kappa(G)}$, then

$$
f_r(G)=\prod_{j=1}^{\kappa(G)}\tau(G_j)
$$

Here $\tau$ is the spanning-tree coefficient; for one vertex, set $\tau=1$. Positive conductances imply $f_r>0$. For a connected graph, write $d=n-1=r$, so $f_d=\tau(G)$. For a disconnected graph, $\tau(G)=0$ even though its leading forest coefficient $f_r$ is positive.

A matroid isomorphism preserving independent sets and their weights preserves every $f_g$. Adding an isolated vertex also leaves these coefficients unchanged: edge sets and their weights remain the same.

## Grade, component count, and corank

Let a forest $F$ have $g$ edges and $m$ components. Each component has one fewer edge than vertices, so

$$
g=n-m
$$

**Definition.** The corank of a forest relative to the original graph is

$$
k=r-g=m-\kappa(G)
$$

It is the number of edges missing from a basis of the cycle matroid. For a connected original graph,

$$
\boxed{g=n-m,\qquad k=d-g=m-1}
\tag{2}
$$

In the figure, edge count increases from left to right, while component count and corank decrease:

![[Three Forest Indices of Cycle C4.svg]]

**Three indices.** The original cycle $C_4$ has rank $d=3$. One forest of each grade is shown, not every forest of the graph. All four vertices remain even when $g=0$; at $g=2$, the selected forest is a three-vertex path and one isolated vertex. Thus all four cases satisfy $m=4-g$ and $k=3-g$.

The different indices describe the same sum:

| Forests specified by | Index | Total weight |
| --- | --- | --- |
| Edge count | $g$ | $f_g$ |
| Component count | $m$ | $f_{n-m}$ |
| Corank | $k$ | $f_{r-k}$; if connected, $f_{d-k}$ |

In a connected graph, a tree has corank $0$, a spanning 2-forest has corank $1$, and the empty edge set has corank $d$. Hence the coefficient of two-component forests is $f_{n-2}=f_{d-1}$.

When another notation indexes by component count, the spanning-tree coefficient occupies position $1$. When indexed by corank, it occupies position $0$. This series retains $f_g$ as the primary notation: other indices are substituted into it, without redefining $\tau$.

For a disconnected graph, a maximal forest has $\kappa(G)$ components and corank $0$. The formula $k=m-1$ does not apply. Recovering a forest's component count from its grade requires knowing $n$; the matroid itself does not record isolated vertices.

## Two generating functions

**Definition.** The generating function by grade and its reversal by corank are

$$
F_G(t)=\sum_{g=0}^{r}f_g(G)t^g
$$

$$
\boxed{
\mathscr F_G(u)=u^rF_G(u^{-1})
=\sum_{k=0}^{r}f_{r-k}(G)u^k
}
\tag{3}
$$

The right-hand side of (3) is a polynomial; its value at $u=0$ is taken after expansion. The inverse transformation is $F_G(t)=t^r\mathscr F_G(t^{-1})$.

These are the same coefficients written in opposite directions. For $F_G$, the constant coefficient is $1$ and the leading coefficient is $f_r$; for $\mathscr F_G$, they are $f_r$ and $1$. In the connected case, $f_r=\tau$.

For example, for a connected graph the first terms in the reversed expression are

$$
\mathscr F_G(u)=\tau+f_{d-1}u+f_{d-2}u^2+\cdots+u^d
$$

The exponent of $u$ records the component count minus one. The total number of forests of a unit-weight graph is $F_G(1)=\mathscr F_G(1)$; for arbitrary weights, this is the total forest weight in the chosen conductance unit.

### Dimensions and scaling

Writing $C$ for the dimension of conductance,

$$
[f_g]=C^g,\qquad [t]=C^{-1},\qquad [u]=C
$$

With this dimensional interpretation, $F_G(t)$ is dimensionless and every term of $\mathscr F_G(u)$ has dimension $C^r$. Square brackets here denote the dimension of a quantity, not a PMG form.

Let $sG$ mean that every conductance is multiplied by a dimensionless factor $s>0$. The weight definition gives

$$
f_g(sG)=s^g f_g(G),\qquad
F_{sG}(t)=F_G(st),\qquad
\mathscr F_{sG}(u)=s^r\mathscr F_G(u/s)
$$

Both generating functions can also be treated as purely formal polynomials. The dimensional interpretation explains why the meaning of the variable changes when passing from grade to corank.

## Forest weights on both sides of duality

In this section the graph is connected, $n\ge2$, and $d=n-1$. Direct vertices $a_i$ are independent, $a_{ij}=a_j-a_i$, and $B_F$ is the exterior product of the forest's edge vectors. Orientations and order do not affect $[B_F]^2$.

For the Laplacian,

$$
L=\sum_{\ell=\{i,j\}\in E}c_\ell[a_{ij}]^2,\qquad
M=\exp L=\sum_{g=0}^{d}M_g
$$

By the [[Laplacian Exponential|forest expansion of the exponential]],

$$
M_g=\sum_{\substack{F\text{ a forest}\\\#E(F)=g}}w(F)[B_F]^2
$$

Thus $f_g$ is the weight sum in this particular edge representation of $M_g$.

On the other side, use the dual Greenian representation $Q_1$ and

$$
D=\exp Q_1=\sum_{k=0}^{d}Q_k,\qquad Q_0=e,\qquad
\mathbf{Gr}=\mathbf L^+
$$

For the partition $\pi=\{C_1,\ldots,C_{k+1}\}$ into forest components, put

$$
a_C^\vee=\sum_{a_i\in C}a_i^\vee,\qquad
\Phi_\pi=[a_{C_1}^\vee\cdots a_{C_k}^\vee]^2
$$

The dual elements satisfy $\sum_i a_i^\vee=0$. One block is omitted from the product; changing that block or ordering the others does not change the quadratic form. For $k=0$, one gets $\Phi_\pi=e$.

The [[Cuts and Forest Grades of the Greenian Exponential#The forest formula for grades of the Greenian exponential|forest formula]] gives

$$
Q_k=\frac1\tau\sum_{\substack{F\text{ a forest}\\\#E(F)=d-k}}w(F)\Phi_{\pi(F)}
\tag{4}
$$

Hence the sum of term weights in (4) is $f_{d-k}/\tau$. The same original forest contributes to $M_g$ and $Q_{d-g}$: its form and normalization change, while its original edge set remains unchanged.

| Representation | Form grade | Original forest edges | Sum of term weights |
| --- | ---: | ---: | --- |
| Edge expansion of $M_g$ | $g$ | $g$ | $f_g$ |
| Cut expansion of $Q_k$ | $k$ | $d-k$ | $f_{d-k}/\tau$ |
| Auxiliary forest expression $\widetilde Q_k=\tau Q_k$ | $k$ | $d-k$ | $f_{d-k}$ |

In particular, $\mathscr F_G(u)/\tau$ collects by dual grade the original forest-weight sums in (4). Its coefficient at $u^k$ has dimension $C^{-k}$ and scales by $s^{-k}$ when conductances are scaled, just as $Q_k$ does.

### Dependence of the sum on the representation

Forms of different partitions may be linearly dependent. Hence “replace every form by $1$ and sum the coefficients” is not a general linear functional on the space of polyforms.

The values $f_g$ and $f_{d-k}/\tau$ are read from the specified forest expansions. Applying a structural identity before summing can change the result. A concrete example appears in the [[Cuts and Forest Grades of the Greenian Exponential#Uniqueness of the form and nonuniqueness of its expansion|section on nonuniqueness of expansions]]; the same limitation applies on the direct side.

### The canonical vector representation of the Greenian

Set $h=n^{-1}\sum_i a_i$ and $\mathcal C(a_i^\vee)=a_i-h$. Then

$$
N=\mathcal C(D)=\exp(\mathrm{Gr}),\qquad
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

The canonical forest polynomial $F_{\mathrm{Gr}}$ is obtained from forests of couplings with weights $\gamma_{ij}$ on the complete set of pairs. These weights can have either sign. Grade $k$ uses $k$ Greenian couplings, whereas (4) uses $d-k$ original edges.

Thus $F_{\mathrm{Gr}}(u)$ and $\mathscr F_G(u)/\tau$ refer to different forest representations. They are not equal in general. Their difference will be computed directly for $K_4$.

The top-form normalizations also differ. With

$$
T_n=[(a_1\ldots a_n)]^2,\qquad
T_n^\vee=[a_1^\vee\cdots a_{n-1}^\vee]^2
$$

one has $Q_d=T_n^\vee/\tau$, but $N_d=T_n/(n^2\tau)$. The factor $n^{-2}$ comes from $\mathcal C(T_n^\vee)=T_n/n^2$. See the [[Laplacian and Greenian - Mutual Duality of Exponentials#Representations and normalizations at a glance|normalization summary]] for the derivation.

## Computation through vertex partitions

Direct enumeration selects sets of $g$ edges, checks for cycles, and sums conductance products. Another method fixes the components of the prospective forest first.

Let $\Pi_m(\mathcal V)$ be the set of unordered partitions of $\mathcal V$ into $m$ nonempty blocks. For a block $B$, let $G[B]$ be the induced graph with the original conductances of its internal edges. Adopt

$$
\tau(G[B])=1\quad\text{if }\#B=1,\qquad
\tau(G[B])=0\quad\text{if }G[B]\text{ is disconnected}
$$

**Theorem.** For $0\le g\le r$,

$$
\boxed{
f_g(G)=\sum_{\pi\in\Pi_{n-g}(\mathcal V)}
\prod_{B\in\pi}\tau(G[B])
}
\tag{5}
$$

**Proof.** Fix a partition $\pi$. A forest with these components is obtained by choosing a spanning tree independently inside each block. The total weight of forests with this partition is therefore the product of the block spanning-tree coefficients. Every forest has a unique component partition, so summing over partitions counts it once. $\square$

There is no factor $(n-g)!$ in (5): blocks are unordered. The same grouping in (4) yields the cut representation of the Greenian through products of $\tau(G[B])$, proved in the [[Cuts and Forest Grades of the Greenian Exponential#Combining forests with identical components|formula for a prescribed partition]].

Each $\tau(G[B])$ can be computed as a Laplacian cofactor of the **induced graph**. Its diagonal must be recalculated using only edges inside $B$. It is not simply a principal submatrix of the original $\mathbf L$, whose diagonal still includes couplings to outside vertices.

Formula (5) reduces the problem to determinants and a sum over partitions. There may be many partitions; the passage to determinants alone gives no general fast algorithm for all $f_g$.

## Edge deletion and contraction

Deleting $\ell$ retains all vertices and other edges. Contracting an edge with distinct endpoints identifies those endpoints, deletes the edge itself, and retains all other edge labels and conductances. Parallel edges and loops in intermediate graphs follow the conventions in [[#Which forests are counted?]].

**Theorem.** For a nonloop edge $\ell$,

$$
\boxed{
F_G(t)=F_{G\setminus\ell}(t)+c_\ell t\,F_{G/\ell}(t)
}
\tag{6}
$$

Accordingly,

$$
f_g(G)=f_g(G\setminus\ell)+c_\ell f_{g-1}(G/\ell)
\tag{7}
$$

**Proof.** Forests not containing $\ell$ are forests of $G\setminus\ell$ with the same weights and edge counts. Contracting $\ell$ gives a bijection between forests of $G$ containing $\ell$ and forests of $G/\ell$. The inverse operation splits the contracted vertex and restores $\ell$; a cycle exists before this operation if and only if it exists afterwards. The edge count decreases by one, and the weight is divided by $c_\ell$. This gives the two terms in (6); coefficient comparison gives (7). $\square$

A loop belongs to no forest, so for a loop $F_G=F_{G\setminus\ell}$. The initial condition for an edgeless graph is $F_G=1$, regardless of the number of isolated vertices.

If $\ell$ is a bridge, no cycle uses it. Independent sets of the remaining edges are the same after deletion and contraction, hence

$$
F_{G\setminus\ell}=F_{G/\ell},\qquad
F_G(t)=(1+c_\ell t)F_{G/\ell}(t)
$$

Connectedness of the original graph is not required in (6)-(7). This matters for recursive computation: deleting a bridge increases the component count.

### Recursion in corank notation

For a nonloop edge, $r(G/\ell)=r(G)-1$. Deletion preserves rank unless the edge is a bridge, in which case rank decreases by one. Substitution of these ranks into (3) and (6) gives

$$
\mathscr F_G(u)=
\begin{cases}
\mathscr F_{G\setminus\ell}(u),&\ell\text{ a loop}\\
(u+c_\ell)\mathscr F_{G/\ell}(u),&\ell\text{ a bridge}\\
\mathscr F_{G\setminus\ell}(u)+c_\ell\mathscr F_{G/\ell}(u),
&\text{otherwise}
\end{cases}
\tag{8}
$$

For a bridge, the extra factor $u$ in the deletion term comes precisely from the rank change. Thus one cannot reverse every polynomial in (6) using the same exponent.

## Connection with the Tutte polynomial

In this section all original conductances equal $1$. Write $\mathsf M(G)$ for the cycle matroid, $r(A)$ for the rank of an edge set $A$, and $r$ for the full rank.

In the modern rank definition, the Tutte polynomial is [2, p. 12]

$$
T_{\mathsf M(G)}(x,y)
=\sum_{A\subseteq E}(x-1)^{r-r(A)}(y-1)^{\#A-r(A)}
$$

The notation $T_{\mathsf M(G)}$ is distinct from the full toponome $T_G(\mathbf x)$. The Tutte polynomial and its recursion are classical; Tutte's original paper [1, pp. 85-90] defines it through spanning-tree activities.

**Theorem.** For a unit-weight graph, including a disconnected one,

$$
\boxed{
\mathscr F_G(u)=T_{\mathsf M(G)}(1+u,1)
}
\tag{9}
$$

**Proof.** At $y=1$, every term with $\#A-r(A)>0$ vanishes. Exactly the independent sets, or forests, remain. For them, $r(A)=\#A$, and the remaining exponent of $u$ is $r-\#A$, the corank. The sum agrees with (3). The zeroth power $(y-1)^0$ is the constant polynomial $1$, so substitution is unambiguous. $\square$

With direct indexing, the same relationship reads

$$
F_G(t)=t^rT_{\mathsf M(G)}(1+t^{-1},1)
$$

Again this is understood after polynomial expansion. In particular, $T_{\mathsf M(G)}(2,1)$ counts all forests and $T_{\mathsf M(G)}(1,1)$ counts bases. For a connected graph the latter equals $\tau$.

For arbitrary conductances, the sums (1) retain products of specific edge weights. The ordinary unweighted Tutte polynomial does not contain those weights, so (9) cannot be applied unchanged. The weighted forest functions are already defined in (1) and (3); formulas (5)-(8) suffice to compute them.

## Why the determinant counts different coefficients

For a forest with components $B\in\pi(F)$, the number of ways to choose one root in each component is $\prod_{B\in\pi(F)}\#B$. Hence the rooted coefficient is

$$
p_g(G)=\sum_{\substack{F\text{ a forest}\\\#E(F)=g}}
w(F)\prod_{B\in\pi(F)}\#B
$$

Directly listing roots shows the source of this extra factor:

![[Ordinary and Rooted Forests - Two Component Types.svg]]

**An ordinary forest and choices of roots.** Both illustrated forests of unit $K_4$ have two edges and contribute $1$ each to $f_2$. For type $3+1$, the three-vertex component has three possible roots, while the isolated vertex is already its component's root. For type $2+2$, there are $2\cdot2=4$ choices. These extra choices give contributions $3$ and $4$ to $p_2$. The smaller drawings below list all choices for each of the two fixed forests.

By the [[Forest Coefficients and the Laplacian Polynomial#Summing minors and the Laplacian polynomial|matrix-forest formula]],

$$
P_L(t)=\det(\mathbf I+t\mathbf L)=\sum_{g=0}^{r}p_g(G)t^g
$$

This is the polynomial $P_G$ in that note; the subscript $L$ allows comparison with the Greenian. Summing principal minors of grade $g$ gives $p_g$, not $f_g$.

For a connected graph, $p_d=n\tau=n f_d$, since each spanning tree has $n$ possible roots. At intermediate grades the multiplier can depend on component type. For a two-component forest, for example, it is $m(n-m)$, where $m$ is one component's size. Thus $f_{d-1}$ alone generally does not determine $p_{d-1}$.

The full toponome retains the distribution of forest weights by component type and allows both specializations. The ordinary one-variable forest polynomial already combines different types of the same grade. Invariance of this sum does not imply invariance of each type; see the [[The Cycle Matroid and Exterior Products of Edges#One matroid, different vertex geometry|path-and-star comparison]].

For the following comparison with the Greenian, assume the graph is connected, $n\ge2$, $d=n-1$, and $\tau>0$. The rooted sums of its canonical signed forests satisfy

$$
P_{\mathrm{Gr}}(u)=\det(\mathbf I+u\mathbf{Gr}),\qquad
P_{\mathrm{Gr}}(u)=\frac{u^d}{n\tau}P_L(u^{-1})
\tag{10}
$$

The proof using reciprocal nonzero spectra appears in [[Toponomes of the Greenian Exponential and Dual Pairs#The dual pair and reversal of spectral coefficients|spectral reversal]]. Here $u$ has the dimension of conductance.

Sequence reversal thus occurs in two distinct formulas: (3) reverses ordinary forest coefficients of the original graph, while (10) relates rooted coefficients of the Laplacian and Greenian with normalization $n\tau$. These operations must not be confused.

## Full example: unit K4

Take vertices $a,b,c,d$ and all six edges of conductance $1$. The graph has rank $3$.

There is one empty edge set and six single-edge sets. Every pair of distinct edges is a forest, so $f_2=\binom62=15$. Of the $\binom63=20$ triples, four are triangles. The remaining sixteen are spanning trees; hence $\tau=f_3=16$.

| Edges $g$ | Components $m$ | Corank $k=3-g$ | $f_g$ | Weight sum in the cut expression for $Q_k$ |
| ---: | ---: | ---: | ---: | ---: |
| $0$ | $4$ | $3$ | $1$ | $1/16$ |
| $1$ | $3$ | $2$ | $6$ | $3/8$ |
| $2$ | $2$ | $1$ | $15$ | $15/16$ |
| $3$ | $1$ | $0$ | $16$ | $1$ |

This gives

$$
F_{K_4}(t)=1+6t+15t^2+16t^3
$$

$$
\mathscr F_{K_4}(u)=16+15u+6u^2+u^3
$$

### Check by grouping components

A two-edge forest has component type $3+1$ or $2+2$. In the first case, there are four choices of isolated vertex and three trees on the remaining triple. In the second, there are three partitions into pairs, with a unique tree inside each pair.

| Component sizes | Partitions | Forests per partition | Total forests | Root choices per forest | Rooted contribution |
| --- | ---: | ---: | ---: | ---: | ---: |
| $3+1$ | $4$ | $3$ | $12$ | $3$ | $36$ |
| $2+2$ | $3$ | $1$ | $3$ | $4$ | $12$ |

Formula (5) gives $f_2=12+3=15$, whereas rooted counting gives $p_2=36+12=48$. At the other grades, $p_0=1$, $p_1=2\cdot6=12$, and $p_3=4\cdot16=64$. Therefore

$$
P_L(t)=1+12t+48t^2+64t^3=(1+4t)^3
$$

An independent matrix check uses $\mathbf L=4\mathbf J$, where $\mathbf J=\mathbf I-\mathbf1\mathbf1^{\mathsf T}/4$: its nonzero eigenvalues are $4,4,4$.

### Two forest polynomials on the Greenian side

The same matrix gives $\mathbf{Gr}=\mathbf J/4$. Thus $\gamma_{ij}=1/16$ for all six pairs. Substitution of these weights gives the canonical Greenian forest polynomial:

$$
F_{\mathrm{Gr}}(u)=1+\frac38u+\frac{15}{256}u^2+\frac1{256}u^3
$$

Weight sums of original forests in the cut expression give a different polynomial:

$$
\frac{\mathscr F_{K_4}(u)}{\tau}
=1+\frac{15}{16}u+\frac38u^2+\frac1{16}u^3
$$

In particular, the first canonical coefficient is $3/8$, whereas the weight sum in the cut representation of $Q_1$ is $15/16$. These are different reductions of representations of the same exponential after centered identification, not two computations of the same coefficient sum.

The rooted Greenian polynomial is

$$
P_{\mathrm{Gr}}(u)=\left(1+\frac u4\right)^3
=1+\frac34u+\frac3{16}u^2+\frac1{64}u^3
$$

It satisfies (10) with $n\tau=64$. Thus the three sums on the Greenian side have different coefficients and consistent normalizations.

## A weighted tree and triangle

### Tree

Every edge subset of a tree $T$ is a forest. Each edge can be selected independently of the others, so

$$
F_T(t)=\prod_{\ell\in E(T)}(1+c_\ell t),\qquad
\mathscr F_T(u)=\prod_{\ell\in E(T)}(u+c_\ell)
\tag{11}
$$

The constant coefficient of the second function is $\tau(T)=\prod_\ell c_\ell$.

For example, for a path with successive conductances $1,2,3$,

$$
F_T(t)=1+6t+11t^2+6t^3,\qquad
\mathscr F_T(u)=6+11u+6u^2+u^3
$$

Any other tree with these three conductances gives the same polynomials. Edge placement affects vertex geometry, but not this count of independent sets.

### A triangle and parallel edges after contraction

Let edges $ab,ac,bc$ have conductances $c_1,c_2,c_3$. All sets of zero, one, or two edges are independent; the triple forms a cycle. Therefore

$$
\tau=c_1c_2+c_1c_3+c_2c_3
$$

$$
F_G(t)=1+(c_1+c_2+c_3)t+\tau t^2,\qquad
\mathscr F_G(u)=\tau+(c_1+c_2+c_3)u+u^2
$$

Delete or contract $ab$. Deletion leaves a tree with weights $c_2,c_3$; contraction leaves two parallel edges with those weights. Hence

$$
F_{G\setminus ab}(t)=(1+c_2t)(1+c_3t),\qquad
F_{G/ab}(t)=1+(c_2+c_3)t
$$

The second polynomial has no term $c_2c_3t^2$: two parallel edges together form a cycle. Substitution into (6) recovers the computed $F_G$.

For $c_1=1,c_2=2,c_3=3$, a direct numerical check gives

$$
F_G(t)=(1+5t+6t^2)+t(1+5t)=1+6t+11t^2
$$

$$
\mathscr F_G(u)=(6+5u+u^2)+(5+u)=11+6u+u^2
$$

The deleted edge is not a bridge, so the second line uses the third branch of (8).

## Gluing and coefficient convolution

Let connected graphs $G_1,G_2$ have disjoint edge sets and be glued at exactly one vertex. Conductances are retained and no further identifications made. Write $G=G_1\vee G_2$ for the result and $d_1,d_2$ for the ranks of the pieces. Then $d=d_1+d_2$.

As proved in the [[The Cycle Matroid and Exterior Products of Edges#What is preserved under one-point gluing?|matroid description of gluing]], each forest of the result splits uniquely into forests of the pieces. Their grades add and their weights multiply. Hence

$$
F_G(t)=F_{G_1}(t)F_{G_2}(t),\qquad
\boxed{f_g(G)=\sum_{i+j=g}f_i(G_1)f_j(G_2)}
\tag{12}
$$

Coranks also add:

$$
(d_1-i)+(d_2-j)=d-(i+j)
$$

Consequently,

$$
\mathscr F_G(u)=\mathscr F_{G_1}(u)\mathscr F_{G_2}(u)
$$

$$
f_{d-k}(G)=\sum_{a+b=k}f_{d_1-a}(G_1)f_{d_2-b}(G_2)
\tag{13}
$$

For $k=0$, one gets $\tau(G)=\tau(G_1)\tau(G_2)$. For $k=1$, division by this product gives

$$
\frac{f_{d-1}(G)}{\tau(G)}
=\frac{f_{d_1-1}(G_1)}{\tau(G_1)}
+\frac{f_{d_2-1}(G_2)}{\tau(G_2)}
\tag{14}
$$

This is a specific additive normalized parameter. Its additivity follows from convolution, whereas its matroid invariance follows from the dependence of numerator and denominator on the weighted matroid.

For $k=2$, (13) also includes the product of two corank-$1$ coefficients. Higher ratios $f_{d-k}/\tau$ therefore do not generally add. Their transformation requires separate analysis.

## Passing to the normalized forest polynomial

For a connected graph, define

$$
\boxed{
\Phi_G(u)=\frac{\mathscr F_G(u)}{\tau(G)}
=\sum_{k=0}^{d}\frac{f_{d-k}(G)}{\tau(G)}u^k
}
\tag{15}
$$

It has $\Phi_G(0)=1$ and leading coefficient $1/\tau$. It generates the weight sums in the cut representation of $Q_k$; in general, it differs from the canonical $F_{\mathrm{Gr}}$.

Under one-point gluing,

$$
\Phi_{G_1\vee G_2}(u)=\Phi_{G_1}(u)\Phi_{G_2}(u)
$$

For a tree, (11) gives

$$
\Phi_T(u)=\prod_{\ell\in E(T)}\left(1+\frac{u}{c_\ell}\right)
$$

These identities are used to study [[The Normalized Forest Polynomial and Power-Sum Parameters|normalized coefficients, power-sum parameters, and their gluing laws]]. Factorization of a general $\Phi_G$ alone does not connect its parameters with the spectrum of $\mathbf L$ or $\mathbf{Gr}$; the spectral formula (10) concerns the different, rooted coefficients.

## Status of the results and verification

Matroid invariance of ordinary forest coefficients and the forest representations of exponentials are used in the current normalization of the published notes. The note proves partition grouping, deletion-contraction and its corank version, the Tutte specialization, and convolution under one-point gluing. These are classical combinatorial constructions reconciled with PMG notation, not claimed as new results in general matroid theory.

The $K_4$, tree, and triangle examples are computed directly. Rooted polynomials of $K_4$ are independently checked using $\mathbf L=4\mathbf J$ and $\mathbf{Gr}=\mathbf J/4$.

Exact rational arithmetic additionally checks 70 graphs, including all 64 subgraphs of $K_4$ with fixed edge conductances $1,2,3,5,7,11$, the examples, and cases with parallel edges and loops. Direct forest enumeration agrees with sums of cofactor products over partitions and with recursive computation. There are 215 edge-recursion checks in direct and reversed notation, including rank changes after bridge deletion. Canonical ordinary and rooted Greenian coefficients of $K_4$ are also checked by enumerating forests with weights $1/16$. These finite checks supplement the general proofs.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_forest_coefficients.py) preserves these scenarios and uses helpers from verify_cycle_matroid.py and verify_forest_power_sums.py. Only the Python standard library is required. Run from the repository root:

    python checks/matroid/verify_forest_coefficients.py

Metric duality in this note is used only for connected undirected graphs with positive conductances. Forest functions of rank $r$ are defined for disconnected graphs, but normalization by the global $\tau$ is not applied. Extension to balanced graphs requires separate justification.

## References

1. Tutte W. T. *A Contribution to the Theory of Chromatic Polynomials*. Canadian Journal of Mathematics, 6 (1954), 80-91. [DOI: 10.4153/CJM-1954-010-9](https://doi.org/10.4153/CJM-1954-010-9). Pages 85-90: the two-variable polynomial through tree activities, deletion-contraction, and the product under one-point gluing.
2. Fink A. *LTCC Enumerative Combinatorics. Notes 6: Deletion-contraction*. Fall 2015. [Author's notes, p. 12](https://maths.qmul.ac.uk/~fink/enumcombi/notes06.pdf). The rank definition of the matroid Tutte polynomial and its specializations.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Лесные коэффициенты - грейд, компоненты и когрейд|Русская версия]].
