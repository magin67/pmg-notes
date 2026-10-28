---
title: Greenian Coefficients and Vertex Variations
date: 2026-10-28
updated: 2026-10-28
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
translation_key: dual-polyform-coefficients-vertex-variations
lang: en
order: 5
description: "Canonical vector coefficients, resistances in the polar expression, original forest weights, and changes in the spanning coefficient under vertex deletion and addition."
---

The canonical vector representation of the Greenian has coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$. These are the negative inner products of centroid vectors in the original resistance geometry. For variations, it is convenient to pass from them to resistances and positive forest weights of the original graph. Each such transition changes the expression while preserving the form and its entire exponential.

We start with the canonical vector coefficients and recovery of resistances. We then prove the polar representation formulas, derive the transition to original forest weights, and show how these determine the spanning coefficient after removing or attaching a vertex. All graph statements concern connected undirected graphs with positive conductances on their existing edges.

The Greenian $\mathrm{Gr}$ and the Laplacian $L$ are grade-one vector forms. Below, the Greenian is written on dual arguments as $Q_1$; the grades $Q_k$ belong to its boundary exponential $D=\exp Q_1$. The centered identification gives $\mathcal C(Q_1)=\mathrm{Gr}$ and $\mathcal C(D)=\exp(\mathrm{Gr})$.

## The basic normalization of duality

Let the direct vertices of $\mathcal V=\{a_1,\ldots,a_n\}$ form a basis of a space $V$, with $n\ge2$, and let $W$ be the space of affine vectors of dimension $d=n-1$. Set

$$
M=\exp L=\sum_{j=0}^{d}M_j,\qquad M_0=e,\qquad M_d\ne0
$$

In the [[Laplacian and Greenian - Mutual Duality of Exponentials#Definition of polyform duality|definition of duality]], the reference for deletion is the top component of the metric polyform itself:

$$
\boxed{M_d/Q_k=M_{d-k},\qquad D=\sum_{k=0}^{d}Q_k}
\tag{1}
$$

Hence $Q_0=e$. For a symmetric nondegenerate Laplacian, the [[The Exterior Exponential and Representations of the Greenian#The dual exponential of a nondegenerate symmetric form|exponential duality theorem]] gives

$$
D=\exp Q_1,\qquad Q_k=\frac{Q_1^k}{k!}
$$

For fixed vertex forms

$$
T=[(a_1\ldots a_n)]^2,\qquad
T^\vee=[a_1\cdots a_{n-1}]^2,\qquad T/T^\vee=e
$$

the graph satisfies

$$
M_d=\tau(G)T,\qquad Q_d=\frac1{\tau(G)}T^\vee
$$

The arguments of $T$ are direct, while those of $T^\vee$ are dual. The top coefficients are reciprocals. Unnormalized forest sums are denoted separately: $\widetilde Q_k=\tau Q_k$, $\widetilde D=\tau D$. Throughout this note, $Q_k,D$ without a tilde have the basic normalization $Q_0=e$.

## Canonical vector coefficients

Write vertex differences as $a_{ij}=a_j-a_i=(a_i a_j)$. When passing between direct and dual spaces, we explicitly specify the meaning of the arguments.

As proved in [[The Canonical Vector Representation of the Greenian]],

$$
Q_1=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

The arguments here are dual. Vector forms constitute a basis, so $\gamma_{ij}$ are uniquely determined. They may have either sign; the expansion of higher grades through vector factors uses signed forests with these weights.

From the coefficients $\gamma$, recover the Green matrix and resistances:

$$
\mathrm{Gr}_{ij}=-\gamma_{ij}\ (i\ne j),\qquad
\mathrm{Gr}_{ii}=\sum_{j\ne i}\gamma_{ij},\qquad
R_{ij}=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}+2\gamma_{ij}
$$

Thus a pair's resistance is not its vector coefficient. The inverse transition uses sums $R_i=\sum_jR_{ij}$ and means $\bar R_i=R_i/n$, $\bar R=n^{-2}\sum_iR_i$:

$$
\gamma_{ij}=\frac12(R_{ij}-\bar R_i-\bar R_j+\bar R)
$$

A direct comparison of the vector expressions is:

| Form | Coefficient of $[a_{ij}]^2$ | Interpretation |
|---|---|---|
| $L$ on direct arguments | $c_{ij}$ | Conductance |
| $Q_1$ on dual arguments | $\gamma_{ij}$ | Negative centroid inner product |

Spanning-tree variations benefit from knowing $R_{ij}$ and the forest weights of the original graph. These are conveniently extracted from the alternative polar and cut expressions examined below. This does not replace the canonical vector representation with another definition of the dual form.

## The polar basis as an alternative representation

On the dual side, the symbols $a_i$ denote classes of coordinate functionals on $W$. Their sole linear relation is

$$
a_1+\cdots+a_n=0
$$

These are dual deletion elements; the direct vertices remain independent.

**Definition.** The polar form of a pair of distinct dual elements is

$$
\{a_i,a_j\}=[a_i,a_j]+[a_j,a_i]
$$

We consider symmetric grade-one forms, that is, elements of $\operatorname{Sym}^2(W^*)$.

**Theorem.** The forms $\{a_i,a_j\}$, $i<j$, form a basis of $\operatorname{Sym}^2(W^*)$. Thus every symmetric grade-one form has a unique representation

$$
\boxed{S=\sum_{i<j}q_{ij}\{a_i,a_j\}}
\tag{2}
$$

**Proof.** Polarizing the dual relation gives

$$
0=\left\{a_i,\sum_j a_j\right\}
=2[a_i]^2+\sum_{j\ne i}\{a_i,a_j\}
$$

Consequently,

$$
[a_i]^2=-\frac12\sum_{j\ne i}\{a_i,a_j\}
$$

Every quadratic term is expressible through polar terms. Since the dual vertices generate $W^*$, the polar forms span the entire space of symmetric forms. Their number equals its dimension:

$$
\binom n2=\frac{d(d+1)}2
$$

Thus they form a basis. $\square$

The polar expression is also unique for fixed vertices. Unlike the main vector basis, it is used here to extract resistances directly. No reference vertex needs to be selected.

### Extracting an individual coefficient

When extracting a coefficient, $a_{ij}$ denotes a direct vector. Its action on the dual elements is

$$
a_{ij}/a_\ell=\delta_{j\ell}-\delta_{i\ell}
$$

Deleting a polar form from $[a_{ij}]^2$ gives zero for all pairs except $\{i,j\}$, which gives $-2e$. Thus, for (2),

$$
\boxed{[a_{ij}]^2/S=-2q_{ij}e}
\tag{3}
$$

This also directly proves linear independence of the polar forms: a zero form has zero coefficients for every pair.

## Resistances in the polar representation

For a direct grade-one form $F$, define the normalized potential

$$
P_M(F)=\frac{\tau(M_{d-1}F)}{\tau(G)}
$$

Here $\tau$ in the numerator extracts the coefficient of $T$. This agrees with the definition $P_M(F)=\tau(MF)/\tau(M)$: only $M_{d-1}F$ contributes to the top grade.

**Lemma.** For any direct grade-one form $F$,

$$
F/Q_1=P_M(F)e
$$

**Proof.** It suffices to check the equality on basis forms $[u_i,u_j]$ in a direct basis $u_1,\ldots,u_d$ and its dual basis. By (1), $M_{d-1}=M_d/Q_1$. Multiplying this form by $[u_i,u_j]$ leaves only the term in which precisely $u_i$ and $u_j$ were deleted from the two arguments of the top form. The signs of deletion and the subsequent exterior multiplication cancel across the two arguments. We obtain

$$
M_{d-1}F=(F/Q_1)M_d
$$

Comparing coefficients of $T$ and dividing by $\tau(G)$ completes the proof. $\square$

The resistance of a pair is defined by the norm of the direct vector:

$$
R_{ij}=P_M([a_{ij}]^2)
$$

The lemma and (3) yield the polar representation.

**Theorem.** The polar expression for the first dual form is

$$
\boxed{
Q_1=-\frac12\sum_{i<j}R_{ij}\{a_i,a_j\}
}
\tag{4}
$$

Its coefficients are unique and determine every pairwise resistance. In particular, negative polar coefficients are compatible with positivity of the resistance metric: polar basis forms are not themselves positive quadratic forms.

The transition between vector and polar expressions gives two ways to read the data of a single dual form:

| Representation of $Q_1$ | Grade-one forms | Coefficients |
|---|---|---|
| Canonical vector | $[a_{ij}]^2$ | $\gamma_{ij}=-\mathrm{Gr}_{ij}$ |
| Polar | $\{a_i,a_j\}$ | $-R_{ij}/2$ |

For multiplication in the exponential, we use vector factors and boundary rules. The polar expression makes an individual pair's resistance directly accessible through deletion (3).

Multiplying all conductances by $s>0$ divides resistances and $Q_1$ by $s$, and divides $Q_k$ by $s^k$.

### Recovering the graph

The polar coefficients give the matrix $\mathbf R=(R_{ij})$ with zero diagonal. By [[Laplacian, Green Matrix, and Effective Resistance Matrix#Reconstructing the Green matrix|double centering]],

$$
\mathbf{Gr}=-\frac12\mathbf J\mathbf R\mathbf J,\qquad
\mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T},\qquad
\mathbf L=\mathbf{Gr}^+
$$

Thus $Q_1$ determines the Laplacian, conductances, $\tau(G)$, and the entire exponential $D$. Higher-grade coefficients are not independently selectable parameters.

An arbitrary collection of positive pair values need not be the resistance matrix of a graph with nonnegative conductances. The canonical nature of the polar basis is an algebraic statement; the graph interpretation assumes that the form comes from the Laplacian under consideration.

## What resistance measures under a coupling variation

Suppose conductance $t\ge0$ is added to pair $i,j$, including a pair with no original edge. The polyform Laplacian becomes

$$
L(t)=L+t[a_{ij}]^2
$$

The added form has square zero, so

$$
\exp L(t)=M\bigl(e+t[a_{ij}]^2\bigr)
$$

Extracting the top coefficient and using the lemma gives

$$
\boxed{\tau(G+t\,ij)=\tau(G)(1+tR_{ij})}
\tag{5}
$$

Consequently,

$$
\frac{\partial\log\tau}{\partial c_{ij}}=R_{ij}
$$

For an absent coupling, the derivative is taken from the right. Resistance is the relative sensitivity of the spanning coefficient to added conductance between the given pair.

If a spanning tree is sampled with probability proportional to its product of conductances, then for an existing edge,

$$
\Pr\{\{i,j\}\text{ belongs to the spanning tree}\}=c_{ij}R_{ij}
$$

Indeed, multiplying the derivative $\partial\tau/\partial c_{ij}$ by $c_{ij}$ gives the total weight of trees containing that edge. Hence $R_{ij}\le1/c_{ij}$, with equality for a bridge. In general, a pair's resistance accounts for the whole graph and is not the reciprocal conductance of a single selected coupling.

## From the polar basis to cut forms

For a nonempty proper block $A$, set $a_A=\sum_{a_i\in A}a_i$. Since $a_{A^c}=-a_A$,

$$
\boxed{
[a_A]^2=-\frac12
\sum_{\substack{a_i\in A\\a_j\in A^c}}\{a_i,a_j\}
}
\tag{6}
$$

Each pair crossing the partition is counted once. The formula follows from $\{a_A,a_{A^c}\}=-2[a_A]^2$.

In the [[Cuts and Forest Grades of the Greenian Exponential#Representing the Greenian through cuts|forest representation]],

$$
Q_1=\sum_{A\mid A^c}\widehat\mu_A[a_A]^2,\qquad
\widehat\mu_A=\frac{\tau(G[A])\tau(G[A^c])}{\tau(G)}
$$

The partitions are unordered. Substituting (6) and comparing the unique polar coefficients with (4) gives

$$
\boxed{
R_{ij}=
\sum_{\substack{A\mid A^c\\i,j\text{ in different blocks}}}\widehat\mu_A
=\frac1{\tau(G)}
\sum_{\substack{F\text{ a spanning 2-forest}\\i,j\text{ in different components}}}w(F)
}
\tag{7}
$$

Thus a pair's resistance collects the normalized weights of all two-component forests separating it. The polar coefficient is $-R_{ij}/2$; the vector coefficient $\gamma_{ij}$ is obtained from all resistances by double centering. The forest weight of a single cut concerns trees within its blocks; it differs from the total conductance of crossing edges.

### Why cut coefficients may change under rewriting

For the unit $K_4$, we have $\tau=16$. The forest expression is

$$
Q_1=\frac1{16}\left(
3\sum_{v\in\{a,b,c,d\}}[v]^2
+[a+b]^2+[a+c]^2+[a+d]^2
\right)
$$

By the cut identity, this form equals

$$
Q_1=\frac14\bigl([a]^2+[b]^2+[c]^2+[d]^2\bigr)
=-\frac14\sum_{i<j}\{a_i,a_j\}
$$

The coefficient of $[a]^2$ changes from $3/16$ to $4/16$, while the polar coefficients remain $-1/4$. They give $R_{ij}=1/2$ for every pair.

The canonical vector coefficients are $\gamma_{ij}=1/16$ for every pair. Rewriting the cut sum does not change them.

In (7), the forest weights for pair $a,b$ give $(3+3+1+1)/16=1/2$. Two contributions separate a single vertex; two correspond to partitions into pairs. The reduced cut coefficients must no longer be read as original forest weights.

## Higher grades and forest weights

The algebraic generation of higher grades and their basis coefficients as minors are proved in the [[The Exterior Exponential and Representations of the Greenian#Higher-grade coefficients are minors|exterior-power formula]]. The vector exponential uses signed forests with weights $\gamma_{ij}$. For variations of the original graph, we now pass to a different expansion, over its forests with positive weights:

$$
Q_k=\sum_{\pi\in\Pi_{k+1}(\mathcal V)}\widehat\mu_\pi\Phi_\pi,\qquad
\widehat\mu_\pi=\frac{\mu_\pi}{\tau(G)},\qquad
\mu_\pi=\prod_{C\in\pi}\tau(G[C])
\tag{8}
$$

Here $\Phi_\pi$ is the form of the product of dual sums of all but one block. The omitted block does not affect the form. We set $\tau$ equal to $1$ for a one-vertex graph and to $0$ for a disconnected graph.

Each partition of $\mathcal V$ is counted once. The weight $\mu_\pi$ is uniquely determined by the partition and graph; coefficients in an arbitrary reduced expansion of the same form may differ.

At $k=0$, the sole partition has weight $\tau$, so $Q_0=e$. At $k=d$, the sole empty forest has weight $1$, so $Q_d=T^\vee/\tau$. The normalized weights $\widehat\mu_\pi$ are generally not probabilities: their sum need not equal $1$.

## Vertex deletion

For the partition $\{a_i\}\mid(\mathcal V\setminus\{a_i\})$, the forest weight is

$$
\mu_{\{a_i\}\mid \mathcal V\setminus\{a_i\}}=\tau(G-a_i)
$$

Thus, in the forest expression for $Q_1$, the coefficient of this partition is

$$
\boxed{
\widehat\mu_{\{a_i\}\mid \mathcal V\setminus\{a_i\}}
=\frac{\tau(G-a_i)}{\tau(G)}
}
\tag{9}
$$

This coefficient is read specifically in representation (8), not as the coefficient of $[a_i]^2$ in any equal sum.

More generally, for a nonempty proper vertex set $S$, take the partition $\pi_S$ into singletons from $S$ and the remaining block $\mathcal V\setminus S$. Then in grade $|S|$,

$$
\Phi_{\pi_S}=\left[\prod_{a_i\in S}a_i\right]^2,\qquad
\mu_{\pi_S}=\tau(G-S),\qquad
\widehat\mu_{\pi_S}=\frac{\tau(G-S)}{\tau(G)}
$$

If the remaining graph is disconnected, this weight is zero. For a weighted graph, the ratio has units of conductance to the power $-|S|$.

### Connection with leaf probability

Let $d_i=\sum_jc_{ij}$, and let $p_{i,1}$ be the probability that $a_i$ is a leaf in a random spanning tree. Extending a spanning tree of $G-a_i$ by one edge incident to $a_i$ gives

$$
p_{i,1}=d_i\frac{\tau(G-a_i)}{\tau(G)}
$$

This relates the forest coefficient of the dual form to a probabilistic vertex characteristic. A detailed comparison of two deletion operations appears in [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius]].

Here $G-S$ means deleting vertices together with incident edges and recalculating the metric. Schur-complement elimination preserves resistances between the remaining points and is a different operation. Exterior deletion from $T$ likewise does not mean deleting a graph vertex.

## Adding a vertex and the contribution of every grade

Attach a new vertex $p$ to the old vertices $a_i$ by conductances $t_i\ge0$. The old conductances remain unchanged. Denote the resulting graph by $G+p$ and set

$$
\mathbf t=(t_1,\ldots,t_n)^{\mathsf T},\qquad
t(C)=\sum_{a_i\in C}t_i
$$

If all $t_i=0$, the graph $G+p$ is disconnected and its spanning coefficient is zero.

**Theorem.** For any $t_i\ge0$,

$$
\boxed{
\tau(G+p)=
\sum_{\pi}\mu_\pi\prod_{C\in\pi}t(C)
}
\tag{10}
$$

The sum runs over all partitions of the original vertices into nonempty blocks; $\mu_\pi$ is defined in (8).

**Proof.** Removing $p$ from a spanning tree of the new graph leaves a spanning forest of the original graph. Each forest component was joined to $p$ by exactly one edge: no edge would violate connectedness, and two edges would create a cycle.

Conversely, choose a spanning forest and attach each component to $p$ by one edge. This gives a spanning tree. The sum of conductances of the ways to attach component $C$ is $t(C)$; choices for different components are independent. Grouping forests by partition gives (10). $\square$

Denote the homogeneous part of degree $k+1$ in the new conductances by

$$
B_{k+1}(\mathbf t)=
\sum_{\pi\in\Pi_{k+1}(\mathcal V)}\mu_\pi\prod_{C\in\pi}t(C)
$$

Then

$$
\boxed{
\tau(G+p)=\sum_{k=0}^{d}B_{k+1}(\mathbf t)
=\tau(G)\sum_{k=0}^{d}
\sum_{\pi\in\Pi_{k+1}(\mathcal V)}
\widehat\mu_\pi\prod_{C\in\pi}t(C)
}
\tag{11}
$$

The forest representation of $Q_k$ gives the part of degree $k+1$. It counts new spanning trees in which vertex $p$ has degree $k+1$.

| Dual grade | Forest of the original graph | Attachment of the new vertex |
|---:|---|---|
| $Q_0=e$ | One spanning tree | One edge; $p$ becomes a leaf |
| $Q_1$ | Two components | Two edges, one to each component |
| $Q_k$ | $k+1$ components | $k+1$ edges |
| $Q_d=T^\vee/\tau$ | All vertices isolated | A star centered at $p$ |

### Factorization and a determinant check

In the space with the added direct vertex,

$$
L_p=\sum_i t_i[(a_i p)]^2,\qquad
M_{G+p}=M\exp L_p
=M\prod_i\bigl(e+t_i[(a_i p)]^2\bigr)
$$

The top grade of the new space is $n$. Obtaining it from the old direct grade $M_{d-k}$ requires selecting $k+1$ new edges. This agrees with the table and with the complementary dual grade $Q_k$.

Removing a factor from an arbitrary factorization of $D$ does not by itself define vertex deletion. The graph operation here is defined by changing the Laplacian and passing to a space of dimension one greater.

Kirchhoff's theorem gives an independent matrix expression. Deleting the row and column of the new vertex from the Laplacian of $G+p$ leaves $\mathbf L+\operatorname{diag}(t_1,\ldots,t_n)$, so

$$
\boxed{\tau(G+p)=\det\bigl(\mathbf L+\operatorname{diag}(\mathbf t)\bigr)}
\tag{12}
$$

Thus (10) is a forest expansion of the determinant. When all $t_i$ are equal, the factor $\prod_Ct(C)$ contains the product of component sizes: this is the rooted normalization discussed in [[Forest Coefficients and the Laplacian Polynomial]] and in classical matrix-forest theory [1, 2].

### Calculating directly from the canonical form

For $\sigma=\sum_i t_i>0$, set

$$
\mathbf K_{\mathbf t}
=\operatorname{diag}(\mathbf t)
-\frac{\mathbf t\mathbf t^{\mathsf T}}{\sigma}
$$

This is the Laplacian of additional undirected couplings of conductance $t_it_j/\sigma$ between the old vertices. Eliminating $p$ by a Schur complement leaves the Laplacian $\mathbf L+\mathbf K_{\mathbf t}$.

**Corollary.** We have

$$
\boxed{
\frac{\tau(G+p)}{\tau(G)}
=\sigma\det\bigl(\mathbf I_n+\mathbf{Gr}\mathbf K_{\mathbf t}\bigr)
}
\tag{13}
$$

**Proof.** Take the cofactor of the Laplacian of $G+p$ corresponding to an old vertex. The Schur complement with respect to the new vertex's diagonal entry $\sigma$ gives

$$
\tau(G+p)=\sigma\,\tau(\mathbf L+\mathbf K_{\mathbf t})
$$

Here $\tau$ applied to a Laplacian denotes its common cofactor. On the space of zero-sum columns, the ratio of the determinants of $\mathbf L+\mathbf K_{\mathbf t}$ and $\mathbf L$ equals the determinant of $\mathbf I+\mathbf{Gr}\mathbf K_{\mathbf t}$. Both Laplacians have the same constant null vector, and their determinants on this space equal $n$ times their spanning coefficients. Thus the factors $n$ cancel. On constant columns, $\mathbf I_n+\mathbf{Gr}\mathbf K_{\mathbf t}$ acts as the identity, giving (13). $\square$

The matrix $\mathbf{Gr}$ is assembled directly from the canonical vector coefficients $\gamma_{ij}$; it can also be recovered from the resistances of the polar expression (4). Thus (13) calculates the variation without choosing a forest expansion. Formulas (10) and (13) express the same result in two ways: the first exposes forest components, while the second uses canonical metric data.

## Attachment examples

### A leaf and two attachment sites

If the only nonzero conductance is $t_a=t$, then

$$
\tau(G+p)=t\,\tau(G)
$$

Only the contribution from $Q_0$ survives: the new vertex becomes a leaf.

If attachment is possible only at two distinct vertices $a,b$, then $Q_0$ and $Q_1$ contribute. By (7) and (10),

$$
\boxed{
\tau(G+p)=\tau(G)\bigl(t_a+t_b+t_at_bR_{ab}\bigr)
}
\tag{14}
$$

For the unit path $a-b-c-d$, we have $\tau=1$ and $R_{ad}=3$. Attaching a new vertex to both ends by unit couplings closes a cycle on five vertices:

$$
\tau(C_5)=1+1+3=5
$$

For the path with conductances $c_{ab}=2$, $c_{bc}=3$, and $c_{cd}=5$, we have $\tau=30$ and $R_{ac}=1/2+1/3=5/6$. With $t_a=1$ and $t_c=2$, we obtain

$$
\tau(G+p)=30\left(1+2+2\cdot\frac56\right)=140
$$

### A weighted triangle: every grade contributes

Let $c_{ab}=2$, $c_{bc}=3$, and $c_{ac}=5$. Then $\tau=31$, and

$$
Q_1=\frac1{279}\bigl(14[(ab)]^2+5[(ac)]^2+11[(bc)]^2\bigr)
$$

For the attachment calculation, use the equivalent cut expression:

$$
Q_1=\frac{3[a]^2+5[b]^2+2[c]^2}{31},\qquad
Q_2=\frac{[ab]^2}{31}
$$

The polar representation is specified by the resistances

$$
R_{ab}=\frac8{31},\qquad
R_{ac}=\frac5{31},\qquad
R_{bc}=\frac7{31}
$$

The spanning coefficient after attaching $p$ has three homogeneous parts:

$$
\begin{aligned}
B_1&=31(t_a+t_b+t_c)\\
B_2&=2(t_a+t_b)t_c+3(t_b+t_c)t_a+5(t_a+t_c)t_b\\
B_3&=t_at_bt_c
\end{aligned}
$$

For $(t_a,t_b,t_c)=(7,11,13)$,

$$
B_1=961,\qquad B_2=2072,\qquad B_3=1001,\qquad
\tau(G+p)=4034
$$

An independent check using (12) gives

$$
\det
\begin{pmatrix}
14&-2&-5\\
-2&16&-3\\
-5&-3&21
\end{pmatrix}
=4034
$$

The three parts correspond to spanning trees of the new graph in which the degree of $p$ is $1,2,3$, respectively. Dividing them by $4034$ gives the probabilities of these events.

## Status of results and scope

The polar basis and uniqueness of its coefficients are proved for an arbitrary symmetric form on a dual space whose only vertex relation is the zero sum. Identifying the coefficients with resistances uses the metric polyform of a connected undirected graph. Vertex variations assume positive original conductances and nonnegative new conductances.

The forest and determinant methods belong to classical Kirchhoff theory and its extensions. The all-minors Laplacian theorem is proved combinatorially in [1]; the matrix theorem on rooted forests and the corresponding principal minors are discussed in [2]. Here the required formulas are proved directly and compared with canonical vector coefficients, resistances in the polar expression, and PMG grades.

Additional independent checks were performed in exact rational arithmetic on six graphs: an edge of conductance $2$, unit and weighted paths $P_4$, a triangle with conductances $2,3,5$, and unit $C_4$ and $K_4$. The polar form calculated through the Green matrix was compared with enumeration of two-component forests. Exterior powers and deletion from $M_d$ were checked in every grade. For 64 nonempty proper sets of deleted vertices, forest weights were compared with spanning coefficients of induced graphs. In 27 vertex-attachment checks, the forest formula (10), determinant (12), enumeration of new spanning trees by the new vertex's degree, and, for $\sigma>0$, formula (13) all agreed. The coupling variation (5) was also checked. These finite checks supplement the general proofs above.

The balanced directed extension requires ordered bilinear forms and separate agreement on indices of one-sided resistances. It is not included in the symmetric statements of this note.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/dual/verify_variations.py) reproduces these calculations without external libraries. From the repository root:

    python checks/dual/verify_variations.py

## References

1. Chaiken S. *A Combinatorial Proof of the All Minors Matrix Tree Theorem*. SIAM Journal on Algebraic Discrete Methods, 3(3), 1982, 319-329. [DOI: 10.1137/0603033](https://doi.org/10.1137/0603033).
2. Chebotarev P., Shamis E. *Matrix-Forest Theorems*. [arXiv:math/0602575v2](https://arxiv.org/abs/math/0602575v2), 2023 version of a manuscript from 1994–1997. Theorem 5 and Appendix Lemma 3: rooted forests and principal minors.

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
