---
title: Varying several couplings together
date: 2026-10-05
revision: 1
source_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: joint-edge-variation
lang: en
description: How simultaneous changes in several conductances affect the Green matrix, effective resistances, and the spanning-tree coefficient, and why mixed variation coefficients are Gram determinants.
---

In [[Varying a single coupling]], changing one conductance produced a rank-one perturbation of the Laplacian. This made it possible to write exact formulas for the changes in the Green matrix, effective resistances, and the spanning-tree coefficient.

We now vary several couplings simultaneously.

A new effect appears. Each individual variation acts on the same metric structure of the graph, so the changes can no longer be treated as independent. Their interaction is controlled by pairwise inner products of the corresponding graph vectors, while higher-order mixed coefficients turn out to be Gram determinants.

Joint variations therefore produce the natural sequence
$$
\text{length}
\longrightarrow
\text{area}
\longrightarrow
\text{volume}
\longrightarrow
\text{higher-dimensional volume}
$$
which was studied geometrically in [[From lengths to areas and volumes]].

## Setup

Consider a connected undirected graph with nonnegative conductances.

Choose $m$ distinct pairs of vertices $e_1,\ldots,e_m$ and assign an arbitrary orientation to each pair. For $e_\alpha=(k_\alpha l_\alpha)$, let $b_\alpha=\mathbf e_{l_\alpha}-\mathbf e_{k_\alpha}$ be its coordinate vector. Change the corresponding conductances by $\delta_1,\ldots,\delta_m$ and collect the vectors and variations into
$$
B=
\begin{pmatrix}
b_1&\cdots&b_m
\end{pmatrix},
\qquad
\Delta=\operatorname{diag}(\delta_1,\ldots,\delta_m)
\tag{1}
$$
We assume that all conductances remain nonnegative after the change.

For formulas involving the new Green matrix, we additionally require the modified graph to remain connected. The formula for the spanning-tree coefficient remains meaningful even at the boundary where connectivity is lost.

Each varied coupling contributes $\delta_\alpha b_\alpha b_\alpha^{\mathsf T}$, so the joint change of the Laplacian is
$$
\boxed{
L'=L+B\Delta B^{\mathsf T}
}
\tag{2}
$$
The rank of the correction is at most $m$, and may be smaller if the selected vectors are linearly dependent.

For $m=1$, formula (2) reduces to the rank-one perturbation from the previous note.

## Gram matrix of the varied couplings

Let $G=L^+$ be the Green matrix of the original graph.

The main object of the joint variation is
$$
\boxed{
K=B^{\mathsf T}GB
}
\tag{3}
$$
> [!definition] Gram matrix of the varied couplings
> We will call the matrix $K$ in (3) the **Gram matrix of the varied couplings**. Its entries are the pairwise inner products of the selected graph vectors:
> $$
> K_{\alpha\beta}
> =b_\alpha^{\mathsf T}Gb_\beta
> =\langle a_{e_\alpha},a_{e_\beta}\rangle
> $$
> Thus, $K$ is the ordinary Gram matrix of the vectors $a_{e_1},\ldots,a_{e_m}$ in resistance geometry. It is not a new Green matrix and should not be confused with $G=L^+$.

Its diagonal entries are the effective resistances between the endpoints of the selected pairs: $K_{\alpha\alpha}=R_{e_\alpha}$.

Off the diagonal we find the familiar mixed quantities $K_{\alpha\beta}=\langle a_{e_\alpha},a_{e_\beta}\rangle$. Their electrical meaning was discussed in [[Transfer potential as an inner product]]: if a unit external current is passed between the endpoints of $e_\beta$, then $K_{\alpha\beta}$ is the resulting potential difference across $e_\alpha$, with the sign determined by the chosen orientations.

In electrical terminology, such a mixed quantity is called a **transfer resistance** or **transfer impedance**: it is the ratio of the potential difference measured across one pair of nodes to the current injected through another pair. In a purely resistive network with unit current, it is numerically equal to $K_{\alpha\beta}$.

The chosen orientations matter only for the signs of mixed inner products. Replacing $b_\alpha$ by $-b_\alpha$ changes the signs of the corresponding row and column of $K$ simultaneously. All final resistances, determinants, and probabilities remain unchanged.

## Two couplings first

Before turning to the general case, consider two varied couplings $e$ and $f$.

Write $R_e=\langle a_e,a_e\rangle$, $R_f=\langle a_f,a_f\rangle$, and $g_{ef}=\langle a_e,a_f\rangle$. Then
$$
K=
\begin{pmatrix}
R_e & g_{ef}\\
g_{ef} & R_f
\end{pmatrix},
\qquad
\Delta=
\begin{pmatrix}
\delta_e&0\\
0&\delta_f
\end{pmatrix}
\tag{4}
$$
For the spanning-tree coefficient we will derive the general formula $\tau'/\tau=\det(I+\Delta K)$. With two couplings it gives immediately
$$
\boxed{
\frac{\tau'}{\tau}
=
1+\delta_eR_e+\delta_fR_f+
\delta_e\delta_f
\left(
R_eR_f-g_{ef}^2
\right)
}
\tag{5}
$$
The first two linear terms are the familiar single-coupling contributions. The new mixed coefficient is
$$
R_eR_f-g_{ef}^2
=
\det K
\tag{6}
$$
This is the Gram determinant of the two graph vectors. Therefore
$$
\boxed{
R_eR_f-g_{ef}^2=S_{ef}^2
}
\tag{7}
$$
where $S_{ef}$ is the area of the parallelogram spanned by $a_e$ and $a_f$ in resistance geometry.

Thus, for the joint variation of two couplings, area appears directly as the coefficient of $\delta_e\delta_f$.

> [!remark] What the interaction means
> If the two changes acted independently while each kept the original metric fixed, one would naturally expect the product $(1+\delta_eR_e)(1+\delta_fR_f)$. The actual result differs by $\delta_e\delta_f g_{ef}^2$.
>
> The inner product $g_{ef}$ measures how much the first variation changes the metric effectiveness of the second.

## Sequential and simultaneous variation

The same result can be obtained sequentially.

First vary the coupling $e$. After this change, the effective resistance between the endpoints of $f$ becomes
$$
R_f^{(e)}
=
R_f-
\frac{\delta_e}{1+\delta_eR_e}g_{ef}^2
\tag{8}
$$
The first step multiplies the spanning-tree coefficient by $1+\delta_eR_e$, and the second by $1+\delta_fR_f^{(e)}$. Hence
$$
\frac{\tau_{e,f}}{\tau}
=
(1+\delta_eR_e)
\left(
1+\delta_fR_f^{(e)}
\right)
$$
Substituting (8), we obtain
$$
\begin{aligned}
\frac{\tau_{e,f}}{\tau}
&=
(1+\delta_eR_e)(1+\delta_fR_f)-
\delta_e\delta_f g_{ef}^2 =\\
&=
1+\delta_eR_e+\delta_fR_f+
\delta_e\delta_f
\left(
R_eR_f-g_{ef}^2
\right)
\end{aligned}
\tag{9}
$$
This is exactly the simultaneous-variation formula.

The order of the changes does not affect the final graph. The intermediate metric does depend on which coupling is varied first, and this change of metric is precisely what produces the mixed term.

## Change of the Green matrix

Return to $m$ varied couplings.

As in the previous note, work on the centered subspace $H=\{x:\mathbf1^{\mathsf T}x=0\}$. On this subspace the Green matrix $G=L^+$ acts as the ordinary inverse of $L$.

To invert a matrix after adding a correction of limited rank, one uses the **Woodbury matrix identity**. If $A$ and $C$ are invertible, then
$$
\boxed{
(A+UCV)^{-1}
=
A^{-1}-
A^{-1}U
\left(
C^{-1}+VA^{-1}U
\right)^{-1}
VA^{-1}
}
$$
Here $A$ is the original square matrix, while $UCV$ is the added correction, whose rank is at most the number of columns of $U$.

In our case on $H$, take $A=L$, $U=B$, $C=\Delta$, and $V=B^{\mathsf T}$. When $\Delta$ is invertible, Woodbury gives
$$
G'
=
G-
GB
\left(
\Delta^{-1}+K
\right)^{-1}
B^{\mathsf T}G
\tag{10}
$$

> [!definition] Sherman-Morrison formula
> If the correction has rank one, the Woodbury identity reduces to the **Sherman-Morrison formula**. For an invertible matrix $A$ and vectors $u,v$,
> $$
> (A+uv^{\mathsf T})^{-1}
> =
> A^{-1}-
> \frac{A^{-1}uv^{\mathsf T}A^{-1}}
> {1+v^{\mathsf T}A^{-1}u}
> $$
> This is the formula used in [[Varying a single coupling]], where the Laplacian perturbation had rank one.

Formula (10) is inconvenient when some variations are zero. Using $(\Delta^{-1}+K)^{-1}=(I+\Delta K)^{-1}\Delta$, we obtain a form that does not require $\Delta^{-1}$:
$$
\boxed{
G'
=
G-
GB(I+\Delta K)^{-1}\Delta B^{\mathsf T}G
}
\tag{11}
$$
Formula (11) remains valid when individual $\delta_\alpha$ vanish: the corresponding coupling simply does not change.

The invertibility of $I+\Delta K$ has a direct graph-theoretic meaning. For admissible nonnegative conductances, this matrix remains invertible as long as the modified graph stays connected.

## Change of an arbitrary effective resistance

Consider any pair of vertices $i,j$ and write $x=\mathbf e_{ij}$. Its effective resistance is $R_{ij}=x^{\mathsf T}Gx$.

Introduce
$$
\boxed{
q=B^{\mathsf T}Gx
}
\tag{12}
$$
Its components are $q_\alpha=\langle a_{ij},a_{e_\alpha}\rangle$. Thus, $q$ collects the inner products of the measured direction $a_{ij}$ with all varied directions.

Substituting (11) into $R'_{ij}=x^{\mathsf T}G'x$ gives
$$
\boxed{
R'_{ij}
=
R_{ij}-
q^{\mathsf T}
(I+\Delta K)^{-1}
\Delta q
}
\tag{13}
$$
This is an exact formula for the joint finite variation of an effective resistance.

If every $\delta_\alpha\ne0$, the same relation can be written as
$$
R'_{ij}
=
R_{ij}-
q^{\mathsf T}
\left(
\Delta^{-1}+K
\right)^{-1}
q
\tag{14}
$$
For $m=1$, $K=R_e$ and $q=\langle a_{ij},a_e\rangle$, so (13) reduces to the formula from [[Varying a single coupling]].

If all variations are nonnegative, $\delta_\alpha\geq0$, then the correction in (13) is nonnegative. Hence $R'_{ij}\leq R_{ij}$: simultaneously strengthening any set of couplings cannot increase an effective resistance. This is a finite multi-coupling form of Rayleigh monotonicity.

## Spanning-tree coefficient

Now consider the combinatorial side of the variation.

Let $L_0$ be any reduced Laplacian of the original connected graph. By Kirchhoff's matrix-tree theorem, $\tau=\det L_0$. After the variation,
$$
L'_0=L_0+B_0\Delta B_0^{\mathsf T}
$$
where $B_0$ is obtained from $B$ by deleting the same row used to form $L_0$.

We use another standard matrix identity, the **matrix determinant lemma**. For an invertible square matrix $A$ and compatible matrices $U,V$,
$$
\boxed{
\det(A+UV)
=
\det A\,
\det(I+VA^{-1}U)
}
$$
Thus, the determinant of a large modified matrix is reduced to a determinant whose size is controlled by the number of columns of $U$ and rows of $V$.

Applying the lemma to the reduced Laplacian gives
$$
\det L'_0
=
\det L_0\,
\det\left(
I+\Delta B_0^{\mathsf T}L_0^{-1}B_0
\right)
$$
The mixed inner products do not depend on the choice of reference potential, so $B_0^{\mathsf T}L_0^{-1}B_0=K$. Therefore
$$
\boxed{
\frac{\tau'}{\tau}
=
\det(I+\Delta K)
}
\tag{15}
$$
or equivalently
$$
\boxed{
\tau'=\tau\det(I+\Delta K)
}
\tag{16}
$$
For one coupling, $\det(I+\Delta K)=1+\delta R_e$, so (16) reproduces the previous result.

Unlike the formula for $G'$, equation (16) remains meaningful if deleting couplings disconnects the graph. In that case $\tau'=0$, and the determinant vanishes.

## Expanding the determinant by subsets of couplings

Formula (15) is especially important because it can be expanded in powers of the variations.

For a subset $S\subseteq\{1,\ldots,m\}$, let $K_S$ denote the principal submatrix of $K$ whose rows and columns are indexed by $S$. Then
$$
\boxed{
\det(I+\Delta K)
=
\sum_{S\subseteq\{1,\ldots,m\}}
\left(
\prod_{\alpha\in S}\delta_\alpha
\right)
\det K_S
}
\tag{17}
$$
with $\det K_\varnothing=1$.

The first terms are therefore
$$
\begin{aligned}
\frac{\tau'}{\tau}
&=
1+
\sum_\alpha\delta_\alpha K_{\alpha\alpha}+
\sum_{\alpha<\beta}
\delta_\alpha\delta_\beta
\det K_{\{\alpha,\beta\}}+
\cdots+\\
&\quad+
\left(
\prod_{\alpha=1}^m\delta_\alpha
\right)
\det K
\end{aligned}
\tag{18}
$$
Since $K_{\alpha\alpha}=R_{e_\alpha}$, the linear coefficients are squared lengths of the selected graph vectors.

For two couplings,
$$
\det K_{\{\alpha,\beta\}}
=
R_{e_\alpha}R_{e_\beta}-
\langle a_{e_\alpha},a_{e_\beta}\rangle^2
$$
is the squared area of the corresponding parallelogram.

For three couplings, $\det K_{\{\alpha,\beta,\gamma\}}$ is the squared volume of the parallelepiped spanned by the three graph vectors.

In general,
$$
\boxed{
\det K_S=V_S^2
}
\tag{19}
$$
where $V_S$ is the higher-dimensional volume of the parallelotope spanned by the vectors in $S$.

> [!info] Main geometric result
> The coefficients of the joint variation of the spanning-tree coefficient have a successive geometric meaning:
> - one varied vector gives a squared length;
> - two give a squared area;
> - three give a squared volume;
> - $k$ give a squared $k$-dimensional volume.
>
> Gram determinants therefore arise not as an additional geometric decoration, but as the actual coefficients of a multi-coupling variation of the graph.

## Mixed derivatives of the spanning-tree coefficient

Formula (17) also gives a differential form of the result.

Let $e_1,\ldots,e_k$ be distinct pairs. The coefficient of $\delta_1\cdots\delta_k$ is $\det K_S$. Hence
$$
\boxed{
\frac{1}{\tau}
\frac{\partial^k\tau}
{\partial c_{e_1}\cdots\partial c_{e_k}}
=
\det K_S
}
\tag{20}
$$
where $K_S$ is evaluated in the original metric.

For $k=1$, this gives $\tau^{-1}\partial\tau/\partial c_e=R_e$. For $k=2$,
$$
\boxed{
\frac1\tau
\frac{\partial^2\tau}
{\partial c_e\partial c_f}
=
R_eR_f-g_{ef}^2
=
\det K_{\{e,f\}}
}
\tag{21}
$$
Thus the sequence
$$
\text{first variation}
\longrightarrow
\text{length},
\qquad
\text{second mixed variation}
\longrightarrow
\text{area},
\qquad
\text{third mixed variation}
\longrightarrow
\text{volume}
$$
is an exact statement about the coefficients of the spanning-tree polynomial.

## Random spanning trees

The same formulas have a direct probabilistic interpretation.

Let $e_1,\ldots,e_k$ now be existing edges of the original graph with positive conductances. Choose a spanning tree at random, with probability proportional to the product of the conductances of its edges.

For one edge, $\Pr(e\in T)=c_eR_e$. For distinct edges,
$$
\boxed{
\Pr(e_1,\ldots,e_k\in T)
=
\left(
\prod_{\alpha=1}^k c_{e_\alpha}
\right)
\det K_S
}
\tag{22}
$$
> [!definition] Transfer current
> Fix oriented edges $e$ and $f$. Inject a unit current at one endpoint of $e$ and withdraw it at the other. The **transfer current** from $e$ to $f$ is the oriented current that then flows through the edge $f$.
>
> If $g(e,f)=\langle a_e,a_f\rangle$ is the induced potential difference across $f$, then Ohm's law gives $Y(e,f)=c_f g(e,f)$, where $c_f$ is the conductance of $f$. The matrix $Y$ is called the **transfer-current matrix**.

The **transfer-current theorem** states that for distinct edges $e_1,\ldots,e_k$, the probability that all of them belong to a random weighted spanning tree is the determinant of the corresponding submatrix of $Y$. In our notation,
$$
\det Y_S
=
\left(
\prod_{\alpha=1}^k c_{e_\alpha}
\right)
\det K_S
$$
which gives (22).

For two edges,
$$
\boxed{
\Pr(e,f\in T)
=
c_ec_f
\left(
R_eR_f-g_{ef}^2
\right)
}
\tag{23}
$$
while $\Pr(e\in T)\Pr(f\in T)=c_ec_fR_eR_f$. Therefore
$$
\boxed{
\Pr(e\in T)\Pr(f\in T)-
\Pr(e,f\in T)
=
c_ec_fg_{ef}^2
\geq0
}
\tag{24}
$$
Thus two distinct edges are negatively correlated in a random spanning tree: their joint probability does not exceed the product of their individual probabilities.

Geometrically, the size of this deviation is determined by the squared inner product of the corresponding graph vectors.

## Removing several couplings

Now let $S$ be a set of existing edges and remove all of them completely. For each $e\in S$, this means $\delta_e=-c_e$.

Collect their original conductances into $C_S=\operatorname{diag}(c_e:e\in S)$. Equation (15) then gives
$$
\boxed{
\frac{\tau(G\setminus S)}{\tau(G)}
=
\det(I-C_SK_S)
}
\tag{25}
$$
The left-hand side has a simple probabilistic meaning. Its numerator sums the weights of exactly those spanning trees of the original graph that use none of the edges in $S$. Therefore
$$
\boxed{
\frac{\tau(G\setminus S)}{\tau(G)}
=
\Pr(T\cap S=\varnothing)
}
\tag{26}
$$
Consequently, $\det(I-C_SK_S)=0$ if and only if deleting $S$ disconnects the graph.

> [!definition] Disconnecting set of edges
> A set of edges $S$ is **disconnecting** if $G\setminus S$ is disconnected. A nonempty disconnecting set that is minimal under inclusion is a **bond**, or minimal edge cut.

For a single edge, this criterion reduces to the bridge condition $c_eR_e=1$. Formula (25) is therefore the multi-edge extension of the one-edge criterion.

## Small joint variations and the logarithm of the spanning-tree coefficient

From the first derivative we already know $\partial\log\tau/\partial c_e=R_e$. Differentiating with respect to another conductance and using the single-coupling sensitivity formula gives
$$
\boxed{
\frac{\partial^2\log\tau}
{\partial c_e\partial c_f}
=-g_{ef}^2
}
\tag{27}
$$
In particular, $\partial^2\log\tau/\partial c_e^2=-R_e^2$.

Hence the Hessian is
$$
\nabla^2\log\tau
=
-\left(K_{ef}^2\right)_{e,f}
\tag{28}
$$
The entrywise square of a Gram matrix is positive semidefinite. Therefore $\nabla^2\log\tau\preceq0$.

In other words, $\log\tau$ is concave as a function of the conductances: along any linear variation of the conductances, its second derivative is nonpositive within the region of connected graphs with positive conductances.

This fact is useful, but here it is only a consequence of the main determinantal structure rather than a separate topic.

## Example: two couplings of a triangle

Consider again the complete graph $K_3$ with unit conductances $c_{12}=c_{13}=c_{23}=1$. Its spanning-tree coefficient is $\tau=3$, and all effective resistances are $R_{12}=R_{13}=R_{23}=2/3$.

Choose $e=(12)$ and $f=(13)$, both oriented away from vertex $1$. Their inner product is $g_{ef}=1/3$, so
$$
K=
\begin{pmatrix}
2/3&1/3\\
1/3&2/3
\end{pmatrix}
$$
Strengthen both couplings by one, $\delta_e=\delta_f=1$. Then
$$
\frac{\tau'}{\tau}
=
\det(I+K)
=
\det
\begin{pmatrix}
5/3&1/3\\
1/3&5/3
\end{pmatrix}
=
\frac83
$$
Therefore
$$
\boxed{\tau'=8}
\tag{29}
$$
This is easy to check directly. After the change, $c'_{12}=2$, $c'_{13}=2$, and $c'_{23}=1$. The three spanning trees have weights $4$, $2$, and $2$, whose sum is $8$.

Now compute the change sequentially. After strengthening only edge $(12)$, the previous note gives $\tau_e=5$. The effective resistance between the endpoints of the second coupling becomes
$$
R_f^{(e)}
=
\frac23-
\frac{1}{1+2/3}\frac19
=
\frac35
$$
so the second step gives $\tau_{e,f}=5(1+3/5)=8$.

The simultaneous and sequential calculations agree, but the second step uses the already modified resistance $R_f^{(e)}$.

For completeness, consider also the resistance between vertices $2$ and $3$. For $x=\mathbf e_{23}$, we have
$$
q=
\begin{pmatrix}
-1/3\\
1/3
\end{pmatrix}
$$
Equation (13) gives
$$
R'_{23}
=
\frac23-
q^{\mathsf T}(I+K)^{-1}q
=
\frac12
\tag{30}
$$
This can also be checked electrically: between vertices $2$ and $3$ there is a direct resistor of resistance $1$, in parallel with the path through vertex $1$, whose total resistance is $1/2+1/2=1$.

> [!example] What this example shows
> Even for a triangle, a joint variation does not reduce to two independent single-coupling formulas. The mixed term $\delta_e\delta_f(R_eR_f-g_{ef}^2)$ is already necessary to obtain the correct spanning-tree coefficient.
>
> Its coefficient is simultaneously a squared area and, after multiplication by the conductances, a joint spanning-tree probability.

## Connection with higher-order geometry

In [[From lengths to areas and volumes]], the Gram determinant was introduced as a geometric construction. Here it has appeared independently as a coefficient of a joint variation.

For a set of varied couplings $S$, the same quantity $\det K_S$ has three equivalent interpretations:

- geometrically, it is the squared higher-dimensional volume spanned by the graph vectors;
- variationally, it is the normalized mixed coefficient in the change of the spanning-tree coefficient;
- combinatorially, after multiplication by the conductances, it is the probability that all selected edges occur together in a random spanning tree.

This is precisely where it becomes natural to regard several graph vectors not merely as a list of independent directions, but as a single higher-order object.

In exterior algebra such an object is written $a_{e_1}\wedge\cdots\wedge a_{e_k}$, and its squared norm is
$$
\left\|
a_{e_1}\wedge\cdots\wedge a_{e_k}
\right\|^2
=
\det K_S
$$
The full algebraic meaning of this notation will be introduced in the following notes. Here it is enough to observe that multi-coupling variation itself leads naturally to higher-grade objects.

## What is not covered here

Only symmetric changes of conductances in an undirected graph have been considered here.

A directed variation of a symmetric network is interesting in its own right: a special asymmetric perturbation of the Laplacian can reproduce the field of potential differences generated by an external current source. That construction, however, requires distinguishing the symmetric and antisymmetric parts of the Laplacian and does not belong to the present multi-coupling Gram scheme.

We also do not consider the inverse problem $dR\longrightarrow dc$, that is, reconstructing conductance variations from changes in effective resistances. It will be treated separately in a note on inverse variation and electrometry.

Finally, this note does not develop the general theory of variations of arbitrary polyform potentials. The discussion is deliberately restricted to the Green matrix, effective resistances, and the spanning-tree coefficient in order to isolate the main geometric mechanism.

## Summary

A joint change of conductances
$$
L'=L+B\Delta B^{\mathsf T}
$$
is controlled by the Gram matrix of the selected graph vectors, $K=B^{\mathsf T}GB$.

It gives two main exact formulas:
$$
\boxed{
G'
=
G-
GB(I+\Delta K)^{-1}\Delta B^{\mathsf T}G
}
$$
and
$$
\boxed{
\frac{\tau'}{\tau}
=
\det(I+\Delta K)
}
$$
For an arbitrary pair of vertices,
$$
\boxed{
R'_{ij}
=
R_{ij}-
q^{\mathsf T}(I+\Delta K)^{-1}\Delta q,
\qquad
q=B^{\mathsf T}G\mathbf e_{ij}
}
$$
The main new effect compared with a single-coupling variation is contained in the expansion
$$
\det(I+\Delta K)
=
\sum_S
\left(
\prod_{\alpha\in S}\delta_\alpha
\right)
\det K_S
$$
The first-order coefficient is a squared length, the second-order coefficient a squared area, the third-order coefficient a squared volume, and the coefficient of general order the squared corresponding higher-dimensional volume.

Joint variations therefore produce the direct transition
$$
\boxed{
\text{coupling variations}
\longrightarrow
\text{Gram determinants}
\longrightarrow
\text{higher-grade objects}
}
$$
which leads directly toward the algebraic language of PMG.

## Classical results used in this note

- the Woodbury matrix identity for inverting a matrix after a correction of limited rank;
- the matrix determinant lemma for determinants after a correction of limited rank;
- Kirchhoff's matrix-tree theorem;
- Rayleigh monotonicity;
- Gram determinants and their interpretation as squared higher-dimensional volumes;
- the transfer-current theorem for joint edge probabilities in a random spanning tree.
