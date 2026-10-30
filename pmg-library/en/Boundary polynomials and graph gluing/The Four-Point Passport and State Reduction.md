---
title: "The Four-Point Passport and State Reduction"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: four-point-passport-and-state-reduction
order: 5
description: "Fifteen four-point states reduced to fourteen linear coordinates; the forest radical versus the tetrahedron identity, the general Catalan rank, and precise linear minimality."
---

The full forest passport has one polynomial coordinate for each boundary partition. Yet different linear combinations of states can give the same result against every partner. Four boundary vertices are the first case where this reduces the coordinate count: fourteen suffice instead of fifteen. The reduction preserves the entire forest polynomial of a gluing, including contributions from internal components.

The starting point is [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|the full pairing law]]. Unlike [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|extraction of the spanning-tree layer]], this reduction discards no lower polynomial degrees. Comparison with [[en/Structural identities/Partition Forms and the Tetrahedron Identity|the tetrahedron identity]] explains why the same number $14$ occurs in two different spaces. We then prove the general Catalan rank, identifying the external results used.

> [!info] Provenance of the results
> **From the literature.** The matrix, reduction by its responses, and the Catalan upper bound appear in [Mannens–Nederlof, §§4.2–4.3](https://arxiv.org/html/2307.01046#S4.SS2); nondegeneracy of the spanning-tree pairing appears in [Kenyon–Wilson, §§2.1–2.2](https://arxiv.org/html/math/0608422v4#S2.SS1).
>
> **Derivations and interpretation here.** We give the four-point relation and matrix explicitly and derive the exact Catalan rank from the two external results. Comparing the forest radical with the structural kernel uses the language of PMG. Minimality follows from rank in an explicitly defined class of passports.
> “Derived here” identifies where a proof is given; no claim of scientific priority is made.

## Which information may be identified

Let $B$ be a marked boundary of $k\ge1$ vertices and $\Pi(B)$ its set of partitions. As in the full law, $r(\pi)=k-b(\pi)$, where $b(\pi)$ is the number of blocks, and $\pi\vee\sigma$ is the least common coarsening. In the free real space

$$
\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R s_\pi
$$

the symbols $s_\pi$ are independent. They represent states, not polyforms. The symmetric pairing matrix is defined by

$$
(\mathbf C_B)_{\pi\sigma}=C(\pi,\sigma)
=\begin{cases}
1,&r(\pi\vee\sigma)=r(\pi)+r(\sigma)\\
0,&\text{otherwise}
\end{cases}
$$

For a component $G$, write the full passport as $\mathbf f_G(t)=(\mathcal F^{G,B}_\pi(t))_\pi$. Here $\mathcal F_\pi$ sums the weights of all spanning forests of state $\pi$, and the degree of $t$ counts selected edges. With matching boundary names, distinct internal vertices, and disjoint edge-label sets,

$$
F_{G_1\#_B G_2}(t)=\mathbf f_1(t)^{\mathsf T}\mathbf C_B\mathbf f_2(t)
\tag{1}
$$

Parallel edges remain distinguishable, and loops belong to no forest. The parts need be neither connected nor planar. Formula (1) has no additional factor of $t$.

**Definition.** The radical of the forest pairing and its quotient space are

$$
\mathscr R_B=\ker\mathbf C_B,\qquad
\mathscr H_B=\mathscr S_B/\mathscr R_B
$$

Two formal vectors are equivalent if their difference pairs to zero with every state. The pairing on $\mathscr H_B$ is nondegenerate, and $\dim\mathscr H_B=\operatorname{rank}\mathbf C_B$. For polynomial vectors, the quotient is taken coefficientwise in $t$.

The radical concerns the **universal linear pairing**. It does not assert equalities among the original state polynomials or turn them into partition forms.

## The fifteen states of a four-point boundary

Fix $B=\{a,b,c,d\}$ and the cyclic order $a,b,c,d$. All partitions are distributed by rank as follows:

$$
\begin{array}{c|l|c}
r&\text{partitions}&\text{count}\\\hline
0&a|b|c|d&1\\
1&ab|c|d,\ ac|b|d,\ ad|b|c,\ a|bc|d,\ a|bd|c,\ a|b|cd&6\\
2&abc|d,\ abd|c,\ acd|b,\ a|bcd,\ ab|cd,\ ad|bc,\ ac|bd&7\\
3&abcd&1
\end{array}
$$

Two blocks cross in the cyclic order if four vertices belonging to them alternate. A partition is noncrossing if no such pair of blocks exists. The only crossing partition here is $\chi=ac|bd$; the other fourteen form the family $\mathrm{NC}_4$.

![[Fifteen states of a four-point boundary.svg]]

**States before reduction.** Every diagram uses the same vertex order. Colored regions represent partition blocks, not graph edges; the crossing of regions in $ac|bd$ creates no vertex. Choosing noncrossing partitions as coordinates does not impose planarity on the component.

## The unique forest relation

**An explicit computation for an established matrix.** Four- and five-point reductions are also used in the proof of Lemma 4.12 of [1]. Here we write the four-point relation in our notation and check it directly.

Introduce the following vector in the free space:

$$
\boxed{
\begin{aligned}
\eta={}&s_{abcd}+s_{ab|cd}+s_{ac|bd}+s_{ad|bc}-\\
&-s_{abc|d}-s_{abd|c}-s_{acd|b}-s_{a|bcd}
\end{aligned}
}
\tag{2}
$$

**Lemma.** The vector $\eta$ belongs to $\mathscr R_B$.

**Proof.** Check its pairing with a state $\sigma$ according to rank. If $r(\sigma)=0$, every term is compatible and the coefficient sum is $1+3-4=0$. If $r(\sigma)=1$, the state joins one vertex pair. It is compatible with two of the three partitions into two pairs and with two of the four partitions of type $3+1$. The fully connected state is incompatible, so the response is $2-2=0$. If $r(\sigma)\ge2$, its rank plus that of every term in (2) exceeds $3$, making compatibility impossible. $\square$

Consequently, in every forest pairing, the crossing state may be replaced by

$$
\boxed{
\begin{aligned}
s_{ac|bd}\equiv{}&
s_{abc|d}+s_{abd|c}+s_{acd|b}+s_{a|bcd}-\\
&-s_{ab|cd}-s_{ad|bc}-s_{abcd}
\end{aligned}
}
\tag{3}
$$

The symbol $\equiv$ means equality of classes in $\mathscr H_B$. It is neither an equality of graphs nor a rule allowing the state $ac|bd$ simply to be deleted.

## The reduced matrix and rank fourteen

List $\mathrm{NC}_4$ in the order

$$
\begin{aligned}
(&a|b|c|d;\\
&ab|c|d,\ ac|b|d,\ ad|b|c,\ a|bc|d,\ a|bd|c,\ a|b|cd;\\
&abc|d,\ abd|c,\ acd|b,\ a|bcd,\ ab|cd,\ ad|bc;\\
&abcd)
\end{aligned}
\tag{4}
$$

The principal submatrix $\widehat{\mathbf C}_4=\mathbf C_B[\mathrm{NC}_4,\mathrm{NC}_4]$ has the explicit block form

$$
\boxed{
\widehat{\mathbf C}_4=
\begin{pmatrix}
1&\mathbf 1^{\mathsf T}&\mathbf 1^{\mathsf T}&1\\
\mathbf 1&\mathbf J_6-\mathbf I_6&\mathbf A&\mathbf 0\\
\mathbf 1&\mathbf A^{\mathsf T}&\mathbf 0&\mathbf 0\\
1&\mathbf 0^{\mathsf T}&\mathbf 0^{\mathsf T}&0
\end{pmatrix}
}
\tag{5}
$$

Here $\mathbf 1$ is a column of six ones, $\mathbf J_6$ is the all-ones matrix, and the group sizes are $1,6,6,1$. The block between ranks $1$ and $2$ is

$$
\mathbf A=
\begin{pmatrix}
0&0&1&1&0&1\\
0&1&0&1&1&1\\
1&0&0&1&1&0\\
0&1&1&0&1&0\\
1&0&1&0&1&1\\
1&1&0&0&0&1
\end{pmatrix}
$$

Its entry is $1$ when the endpoints of the selected pair lie in different blocks of the selected rank-$2$ partition. Matrix (5) thus specifies all $196$ entries without listing fourteen lengthy rows.

Direct calculation gives $\det\mathbf A=8$. Expanding (5) along the last row and then along the column of the fully connected state yields

$$
\det\widehat{\mathbf C}_4=-(\det\mathbf A)^2=-64
$$

**Theorem.** The full $15\times15$ matrix $\mathbf C_B$ has rank $14$, and its radical is $\mathbb R\eta$.

**Proof.** Relation (2) gives the upper bound $14$. The nonzero minor (5) gives the lower bound $14$. The radical is therefore one-dimensional and generated by $\eta$. $\square$

![[The reduced forest matrix and spanning-tree blocks.svg]]

**The forest matrix contains the spanning-tree matrix on its block antidiagonal.** Filled cells equal $1$ and white cells equal $0$. When the rank sum is $3$, a compatible forest already connects the whole boundary; these blocks coincide with the spanning-tree pairing. Larger rank sums give zeros. This structure will be used in the general proof.

## State coordinates and responses after reduction

Let $f_\pi(t)=\mathcal F^{G,B}_\pi(t)$. Applying (3) to the formal vector $\sum_\pi f_\pi s_\pi$ gives fourteen coordinates:

$$
\widetilde f_\rho=
\begin{cases}
f_\rho,&r(\rho)=0\text{ or }1\\
f_\rho+f_\chi,&\rho\in\{abc|d,abd|c,acd|b,a|bcd\}\\
f_\rho-f_\chi,&\rho\in\{ab|cd,ad|bc,abcd\}
\end{cases}
\tag{6}
$$

Denote this constant linear transformation by $\widetilde{\mathbf f}=\mathbf K\mathbf f$. Appending $\chi$ last to the order (4) gives

$$
\mathbf K=(\mathbf I_{14}\mid\mathbf c),\qquad
\mathbf c=(0,0,0,0,0,0,0,1,1,1,1,-1,-1,-1)^{\mathsf T}
$$

Equality of state classes implies the factorization

$$
\mathbf C_B=\mathbf K^{\mathsf T}\widehat{\mathbf C}_4\mathbf K
$$

and the full gluing law becomes

$$
\boxed{
F_{G_1\#_B G_2}(t)
=\widetilde{\mathbf f}_1(t)^{\mathsf T}
\widehat{\mathbf C}_4\widetilde{\mathbf f}_2(t)
}
\tag{7}
$$

Reduced coordinates may have negative coefficients. They are not polynomials of individual forest events; they represent the class of the full passport.

For [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|contraction responses]], a different expression applies. Set

$$
u_\sigma(t)=F_{G/\sigma}(t),\qquad
\widehat{\mathbf u}(t)=(u_\sigma(t))_{\sigma\in\mathrm{NC}_4}
$$

Since $\mathbf u=\mathbf C_B\mathbf f$, we have

$$
\widehat{\mathbf u}=\widehat{\mathbf C}_4\widetilde{\mathbf f},\qquad
\widetilde{\mathbf f}=\widehat{\mathbf C}_4^{-1}\widehat{\mathbf u}
$$

Hence

$$
\boxed{
F_{G_1\#_B G_2}(t)
=\widehat{\mathbf u}_1(t)^{\mathsf T}
\widehat{\mathbf C}_4^{-1}\widehat{\mathbf u}_2(t)
}
\tag{8}
$$

Only the nonsingular matrix of size $14$ is inverted, not the full matrix of size $15$. The response to the omitted test is recovered by

$$
\begin{aligned}
u_{ac|bd}={}&u_{abc|d}+u_{abd|c}+u_{acd|b}+u_{a|bcd}-\\
&-u_{ab|cd}-u_{ad|bc}-u_{abcd}
\end{aligned}
\tag{9}
$$

Relation (9) holds for responses; no analogous identity holds for the original $f_\pi$. The inverse matrix in (8) defines dual coordinates for this algebraic pairing. It is not a resistance Gram matrix and does not express Laplacian–Greenian duality.

### An example with a crossing state

Take a graph $G$ on the boundary $B=\{a,b,c,d\}$ itself, with two unit edges $ac$ and $bd$. Its only nonzero coordinates are

$$
f_{a|b|c|d}=1,\qquad
f_{ac|b|d}=f_{a|bd|c}=t,\qquad
f_{ac|bd}=t^2
$$

After reduction, the four coordinates of type $3+1$ equal $t^2$, while those of $ab|cd$, $ad|bc$, and $abcd$ equal $-t^2$. Rank-$0$ and rank-$1$ coordinates remain unchanged. In particular, the formal combination $\sum_\pi\eta_\pi f_\pi=t^2\ne0$: the original coefficients do not satisfy the radical relation.

The partner $J$ has the same boundary, the single unit edge $ab$, and isolated vertices $c,d$. Boundaries are identified by name; there are no shared edges. The result is the path $c-a-b-d$, so

$$
F_{G\#_B J}(t)=(1+t)^3
$$

Formula (7) gives the same answer. Simply deleting $f_{ac|bd}$ without transforming the other coordinates would give $1+3t+2t^2$, losing $t^2+t^3$.

![[Reducing a crossing state without losing forests.svg]]

**Changing coordinates retains the contribution; deletion loses it.** The crossing of $ac$ and $bd$ in the left diagram is not a vertex. After adding $ab$, the graph is redrawn as an ordinary path. Negative reduced coordinates compensate for excess contributions; they do not represent negative edge weights.

## Why this is not the tetrahedron identity

**Comparison in the language of PMG.** We compare the forest pairing of [1] with the map to partition forms from [[en/Structural identities/Partition Forms and the Tetrahedron Identity|Partition Forms and the Tetrahedron Identity]]. The calculation below distinguishes their kernels; it interprets the two constructions within this series.

Now consider a different map: $\Phi(s_\pi)=q_\pi$, where $q_\pi=\prod_{A\in\pi}[(A)]^2$ is an actual partition form. For independent basis vertices, the structural identity is

$$
q_{ab|cd}+q_{ac|bd}+q_{ad|bc}
=q_{abc|d}+q_{abd|c}+q_{acd|b}+q_{a|bcd}
$$

Every term has grade $2$. Denote the corresponding formal difference by $\theta$. The same state combination is a known relation for the spanning-tree pairing in Kenyon–Wilson [2, §2.3, Lemma 2.3]. Here equality of actual forms rests on the cited PMG structural identity; the spanning-tree and full forest pairings are different. We then have

$$
\eta=\theta+s_{abcd},\qquad
\Phi(\theta)=0,\qquad
\Phi(\eta)=q_{abcd}\ne0
$$

Conversely, $\theta$ does not lie in the forest radical: pairing it with the fully separated test gives $3-4=-1$. Thus structural reduction cannot automatically be applied to an ordinary forest passport, nor can the forest relation be regarded as an equality of polyforms.

| Space | What is identified | Dimension for four vertices |
|---|---|---|
| $\mathscr S_B$ | Nothing: all state symbols are independent | $15$ |
| Form space $\mathcal P_4$ | Structural identities, including $\theta=0$ | $14$ |
| Forest space $\mathscr H_B$ | Zero responses to every partner, that is, $\eta=0$ | $14$ |

The dimension of $\mathcal P_4$ is proved in [[en/Structural identities/Basis and Dimension of the Space of Partition Forms|Basis and Dimension of the Space of Partition Forms]]. Equal dimensions do not identify the two kernels or make $s_\pi\mapsto q_\pi$ well-defined on the forest quotient.

### Coordinate groups do not define a canonical grading

Free states decompose by rank as $1+6+7+1$. Structural reduction preserves grade and gives $1+6+6+1$. The forest relation $\eta=0$ mixes ranks $2$ and $3$: the nonzero class of $s_{abcd}$ equals a combination of rank-$2$ classes.

Thus the original grading by $r(\pi)$ does not descend to $\mathscr H_B$. Basis (4) retains groups of sizes $1,6,6,1$, but these merely organize coordinates. They do not by themselves give a canonical decomposition into exterior powers or mutually dual symmetric forms.

The degree of $t$, which counts edges of the original forest, remains unchanged: reduction (6) acts coefficientwise. For example, a term $-t^2$ in the coordinate named $abcd$ does not assert the existence of a two-edge tree on four vertices.

## The general Catalan rank

Fix a cyclic order on an arbitrary boundary of $k$ vertices. The number of noncrossing partitions is the Catalan number

$$
\mathrm{Cat}_k=\frac1{k+1}\binom{2k}{k}
$$

**Theorem (a consequence of [1]–[2]).** Over $\mathbb R$, and also over $\mathbb Q$,

$$
\boxed{
\operatorname{rank}\mathbf C_B=\mathrm{Cat}_k
}
\tag{10}
$$

The classes of noncrossing partitions form a basis of $\mathscr H_B$, and the principal submatrix $\mathbf C_B[\mathrm{NC}_k,\mathrm{NC}_k]$ is nonsingular.

**External foundations.** Mannens–Nederlof [1, §4.2, Theorem 4.2] prove the upper bound $\operatorname{rank}\mathbf C_B\le\mathrm{Cat}_k$ for the forest compatibility matrix; their Definitions 4.3–4.5 agree with our setting. Kenyon–Wilson [2, §§2.1–2.2] use the nonsingular spanning-tree matrix on noncrossing partitions

$$
(\mathbf T_k)_{\pi\sigma}
=\begin{cases}
1,&\pi\vee\sigma=\{B\},\quad r(\pi)+r(\sigma)=k-1\\
0,&\text{otherwise}
\end{cases}
$$

Their notation is $\mathcal M_{\mathsf t}$. In §2.1, they justify nonsingularity via a limit of the meander matrix, citing equation (5.18) of Di Francesco–Golinelli–Guitter. Below, the two results yield the exact equality (10), not just a bound.

**Proof of the lower bound.** Set $\mathbf M=\mathbf C_B[\mathrm{NC}_k,\mathrm{NC}_k]$ and group rows and columns by partition rank.

1. If $r+s>k-1$, the block $\mathbf M_{r,s}$ is zero: the rank of the join cannot exceed $k-1$.
2. If $r+s=k-1$, compatibility is equivalent to full connectivity of the boundary. Thus $\mathbf M_{r,k-1-r}=(\mathbf T_k)_{r,k-1-r}$.
3. All other blocks of $\mathbf T_k$ are zero. Its nonsingularity implies that each block between complementary ranks is square and nonsingular.

Now list the column groups in reverse order. The matrix $\mathbf M$ becomes block upper triangular, with precisely the nonsingular blocks from step 3 on its diagonal. Consequently, $\det\mathbf M\ne0$ and

$$
\operatorname{rank}\mathbf C_B\ge|\mathrm{NC}_k|=\mathrm{Cat}_k
$$

Moreover, for the same index ordering, $\det\mathbf M=\det\mathbf T_k$: after the same permutation of column groups, both matrices have identical diagonal blocks. The upper bound of [1] completes the proof of (10). The independent classes $\mathrm{NC}_k$ have the dimension of the entire quotient, so they form a basis. $\square$

The exact equality is obtained here by combining two external results. It is proved, but priority for this deduction has not been established; the statement does not claim novelty relative to the entire literature. Graphs to which (10) is applied may be nonplanar: noncrossing partitions are chosen as coordinates of a universal matrix. Circular-planarity hypotheses in theorems reconstructing groves from electrical response are discussed separately in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]].

For any boundary, one may therefore retain $\mathrm{Cat}_k$ responses $F_{G/\sigma}(t)$ with $\sigma\in\mathrm{NC}_k$ and use $\mathbf M^{-1}$ in the analogue of (8). The cyclic order affects the coordinate choice, not the rank.

## In what sense the coordinate count is minimal

**A linear-algebra consequence.** The lower bound on the coordinate count follows from the rank of a bilinear form. The principle is standard; the precise class of allowed passports is essential to its application.

Specify that class as follows. A fixed linear map $\mathcal K_0:\mathscr S_B\to\mathbb R^m$ is applied coefficientwise to the polynomial vector, and gluing is recovered by a fixed bilinear pairing of the images. In matrix terms,

$$
\mathbf C_B=\mathbf K_0^{\mathsf T}\mathbf M_0\mathbf K_0
$$

for some matrix $\mathbf M_0$ of size $m$. Then

$$
\mathrm{Cat}_k=\operatorname{rank}\mathbf C_B
\le\operatorname{rank}\mathbf K_0\le m
$$

Conversely, quotienting by the radical and choosing the noncrossing basis achieves $m=\mathrm{Cat}_k$. Thus **this is the minimum number of polynomial coordinates in a universal linear passport with a bilinear gluing law**. Allowing linear transformations over $\mathbb R(t)$ gives the same bound from the rank over that field.

Formal partners introduce no artificial restriction here. For each partition $\pi$, take one unit-weight tree on each block, with no internal vertices, and call the resulting forest-graph $A_\pi$. Its full passport has leading term $t^{r(\pi)}s_\pi$, while the remaining terms correspond to strict refinements of $\pi$. The matrix of these passports is triangular with nonzero diagonal over $\mathbb R(t)$, so they span the entire formal space over this field. A universal bilinear formula for all graphs must also preserve their linear combinations.

This is not a lower bound for arbitrary nonlinear graph encodings, for packing several polynomials into one object, or for a restricted family of partners. Nor does it assert algebraic independence of passport coordinates for a particular graph class.

## Status of the results and checks

The four-point relation is proved by three cases of test rank, and rank $14$ by an explicit nonzero minor. State and response reductions follow from the matrix factorization. The distinction from the tetrahedron identity is established by checking both kernels. The general theorem (10) is proved using the stated external results; finite computations do not replace it.

Exact checks give

$$
\begin{array}{c|rrrrr}
k&1&2&3&4&5\\\hline
|\Pi(B)|&1&2&5&15&52\\
\operatorname{rank}\mathbf C_B&1&2&5&14&42
\end{array}
$$

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_reduction.py) uses rational arithmetic. It independently compares compatibility with incidence-matrix rank and checks the radical, reduced matrix, spanning-tree blocks, and both pairing methods. For graphs, responses are enumerated directly after contraction, and resulting polynomials after gluing. Checks also cover boundary permutations, internal components, loops, and parallel edges. [Instructions for the checks and figure reproduction](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) accompany it.

For the full forest-polynomial problem, states, tests, pairing, and its minimal linear reduction are now defined. [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]] constructs a different two-point passport from minors and cofactors of the spectral pencil, proving Jacobi's identity and gluing laws with shared vertices and edges counted explicitly. Ordinary forest coordinates cannot automatically be transferred to that problem.

## Sources and connections

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [arXiv:2307.01046, §4.2, Definitions 4.3–4.5, Theorem 4.2, and the proof of Lemma 4.12; §4.3, Definition 4.16](https://arxiv.org/html/2307.01046#S4.SS2). The forest compatibility matrix and the Catalan rank upper bound. Their matrix notation $F_k$ differs from our polynomial notation $F_G(t)$.
2. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325–1364. [arXiv:math/0608422v4, §§2.1–2.2, equations (5)–(6); §2.3, Lemma 2.3](https://arxiv.org/html/math/0608422v4#S2.SS1). The nonsingular spanning-tree matrix $\mathcal M_{\mathsf t}$ and its combinatorial rule; §2.1 identifies its nonsingularity basis in the meander determinant of Di Francesco–Golinelli–Guitter.

Supporting PMG notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]], [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]], [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]], [[en/Structural identities/Partition Forms and the Tetrahedron Identity|Partition Forms and the Tetrahedron Identity]], [[en/Structural identities/Basis and Dimension of the Space of Partition Forms|Basis and Dimension of the Space of Partition Forms]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/Четырёхточечный паспорт и сокращение числа состояний|Русский]]
