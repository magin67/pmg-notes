---
title: Laplacian Exponential
date: 2026-10-06
updated: 2026-11-06
revision: 9
translated_revision: 9
source_revision: 8
status: draft
text_prepared_by: ChatGPT
translation_key: laplacian-exponential
lang: en
description: The exponential in the algebra of forms, its forest grade components, and the spanning-tree coefficient. A general proof relating normalized potential to the resistance metric.
order: "10"
aliases:
  - "en/Introduction/Laplacian Exponential"
---

In [[Basic Objects and Operations of Polyform Algebra]], a product of edge forms vanishes whenever the selected edges contain a cycle. We want one polyform that collects all remaining edge sets, counting each exactly once. For sets of $k$ edges, $L^k/k!$ does this: a set occurs in $L^k$ in $k!$ orders. Summing over $k$ gives the Laplacian exponential.

We examine its forest components, then show how extracting the top-grade coefficient recovers the familiar resistances, areas, and volumes.

## The exponential in the algebra of forms

Let $G$ be a connected undirected graph on vertices $a_1,\ldots,a_n$, $n\ge2$, with positive conductances on its existing edges. The space of affine vectors $W$ has dimension $n-1$. The Laplacian polyform is

$$
L=\sum_{\{i,j\}\in E}c_{ij}[a_{ij}]^2,\qquad a_{ij}=a_j-a_i
$$

All products of forms use the [[Basic Objects and Operations of Polyform Algebra#Polyforms and the product of forms|definition of the product of forms]]:

$$
[X,Y][A,B]=[XA,YB]
$$

The identity of this algebra is denoted by $e=[1,1]$. For every vector $v$, we have $([v]^2)^2=0$. Also, $L^n=0$, since a product of $n$ forms of grade one on $W$ has zero exterior arguments.

> [!info] The metric polyform
> **Definition.** The metric polyform of a graph is the exponential of its Laplacian in the algebra of forms:
>
> $$
> M=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!}
> =e+L+\frac{L^2}{2!}+\cdots+\frac{L^{n-1}}{(n-1)!}
> \tag{1}
> $$
>
> Here $L^0=e$, and all powers use the product of forms. The graph is fixed within each argument, so we write $M$ without a graph subscript; after a graph change we write $M'$.

The Laplacian matrix is denoted by $\mathbf L$. The matrix exponential $\exp\mathbf L$ uses a different multiplication and does not equal (1). Nilpotence of the polyform $L$ does not imply nilpotence of the matrix $\mathbf L$.

Commutativity of forms and the identity $([a_{ij}]^2)^2=0$ give the factorization

$$
M=\prod_{\{i,j\}\in E}\bigl(e+c_{ij}[a_{ij}]^2\bigr)
\tag{2}
$$

The factor $e+c_{ij}[a_{ij}]^2$ is called the edge factor. In the expansion of (2), each coupling is either selected once or omitted.

### Example: a weighted triangle

Let $c_{12}=\alpha$, $c_{23}=\beta$, and $c_{13}=\gamma$. Here and below, abbreviate the boundaries as $(12)=(a_1a_2)$ and $(123)=(a_1a_2a_3)$.

$$
M=(e+\alpha[(12)]^2)(e+\beta[(23)]^2)(e+\gamma[(13)]^2)
$$

Selecting one coupling gives its form weighted by its conductance. Any two couplings form a tree on three vertices, so their product gives $[(123)]^2$. Selecting all three gives zero because the cycle vectors are dependent. Thus

$$
\begin{aligned}
M={}&e+\alpha[(12)]^2+\beta[(23)]^2+\gamma[(13)]^2+\\
&+(\alpha\beta+\alpha\gamma+\beta\gamma)[(123)]^2
\end{aligned}
$$

The three spanning trees have weights $\alpha\beta$, $\alpha\gamma$, and $\beta\gamma$. Their forms coincide, so their weights add. The general forest expansion below works in the same way: any edge set may be selected, but a cycle makes its product vanish.

## Grade components and spanning forests

The grade decomposition of the exponential is

$$
M=\sum_{k=0}^{n-1}M_k,\qquad M_0=e,\qquad M_k=\frac{L^k}{k!}
\tag{3}
$$

A spanning forest contains every vertex of the original graph and has no cycles. Isolated vertices count as components. Maximality is not required: the empty edge set, for example, also defines a spanning forest.

For an edge subset $F$, fix an arbitrary order and orientations. Denote the exterior product of its vectors and the product of its coupling strengths by

$$
B_F=\bigwedge_{\{i,j\}\in F}a_{ij},\qquad
w(F)=\prod_{\{i,j\}\in F}c_{ij}
$$

The sign of $B_F$ depends on these choices, but the form $[B_F]^2$ does not. For the empty set, $B_F=1$ and $w(F)=1$.

> [!info] The forest expansion
> **Theorem.** The grade component of the exponential is
>
> $$
> M_k=\sum_{\substack{F\subseteq E\text{ is a forest}\\|F|=k}}w(F)[B_F]^2
> \tag{4}
> $$
>
> The forest contains all vertices of the original graph, including isolated vertices, and has $n-k$ components.

In the expansion of (2), each edge set occurs once. A cycle makes the exterior product of its edge vectors zero, while the vectors of a forest are independent. This proves (4). In the power expression (3), each set of $k$ distinct edges occurs in $k!$ orders, explaining the division by $k!$.

For a tree, the product of its edge vectors is the boundary on its vertices, up to sign. For a forest, it is the product of the boundaries of its components. An isolated vertex contributes the factor $\partial a_i=1$.

Denote the sum of weights of forests of a given size by

$$
s_k(G)=\sum_{\substack{F\subseteq E\text{ is a forest}\\|F|=k}}w(F)
$$

With unit conductances, this is the number of forests with $k$ edges. The quantity $s_k$ refers to the specific forest expansion (4). Forest forms may satisfy linear relations, so the sum of coefficients after an arbitrary rewriting of $M_k$ need not equal $s_k$.

## Example: a path on five vertices

Continue with a graph that also has forests with several nontrivial components.

```mermaid
graph LR
    a1((1)) --- a2((2))
    a2 --- a3((3))
    a3 --- a4((4))
    a4 --- a5((5))
```

> [!example] Grades of the exponential for the path $P_5$
> With unit conductances,
>
> $$
> M=(e+[(12)]^2)(e+[(23)]^2)(e+[(34)]^2)(e+[(45)]^2)
> $$
>
> The components in (3) are
>
> $$
> M_0=e,\qquad
> M_1=[(12)]^2+[(23)]^2+[(34)]^2+[(45)]^2
> $$
>
> $$
> \begin{aligned}
> M_2={}&[(123)]^2+[(234)]^2+[(345)]^2+\\
> &+[(12)(34)]^2+[(12)(45)]^2+[(23)(45)]^2
> \end{aligned}
> $$
>
> $$
> M_3=[(1234)]^2+[(2345)]^2+[(123)(45)]^2+[(12)(345)]^2
> $$
>
> $$
> M_4=[(12345)]^2
> $$
>
> Every edge subset of a path is a forest, so $(s_0,s_1,s_2,s_3,s_4)=(1,4,6,4,1)$. All six forests in $M_2$ have three components. For example, $(123)$ describes a tree on three vertices and two isolated vertices, while $(12)(34)$ describes two edges and the isolated vertex $5$.

## The spanning-tree form and top-grade coefficient

> [!info] The spanning-tree form
> **Definition.** On a fixed vertex set, define
>
> $$
> T_n=[(a_1\ldots a_n)]^2
> $$
>
> This is the spanning-tree form of grade $n-1$. In the project's terminology, it is also called the top-grade form.

Forests with $n-1$ edges are spanning trees, and the quadratic form of each is $T_n$. Thus (4) gives

$$
M_{n-1}=\tau(G)T_n,\qquad
\tau(G)=\sum_{T\text{ is a spanning tree}}\prod_{e\in T}c_e
\tag{5}
$$

The number $\tau(G)$ is called the spanning-tree coefficient; with unit conductances, it is the number of spanning trees. The component $M_{n-1}$ is the top-grade component, while $M_{n-2}$ is the component immediately below it and collects spanning 2-forests.

For a connected graph, $\tau(G)>0$. Hence $L^{n-1}\ne0$, $L^n=0$, and the highest nonzero grade of the exponential is $n-1$. By the matrix-tree theorem, the same $\tau(G)$ equals the determinant of any reduced Laplacian matrix.

> [!example] The four-cycle $C_4$
> For unit-conductance edges $12,23,34,41$,
>
> $$
> M=(e+[(12)]^2)(e+[(23)]^2)(e+[(34)]^2)(e+[(41)]^2)
> $$
>
> The components of grades zero and one are $M_0=e$ and $M_1=L$. At grade two,
>
> $$
> \begin{aligned}
> M_2={}&[(123)]^2+[(234)]^2+[(134)]^2+[(124)]^2+\\
> &+[(12)(34)]^2+[(23)(41)]^2
> \end{aligned}
> $$
>
> Any three edges form a spanning tree, so
>
> $$
> M_3=4[(1234)]^2,\qquad \tau(C_4)=4,\qquad M_4=0
> $$
>
> The vanishing fourth grade corresponds to the dependence $(12)+(23)+(34)+(41)=0$.

| Graph | Forest weight sums $s_k$ | Top grade | Spanning-tree coefficient |
|---|---|---:|---:|
| $P_5$ with unit conductances | $1,4,6,4,1$ | 4 | 1 |
| $C_4$ with unit conductances | $1,4,6,4$ | 3 | 4 |

## The potential of a form

The space $W$ has dimension $n-1$. Any two nonzero exterior products of $n-1$ vectors are therefore proportional: they belong to the one-dimensional space $\Lambda^{n-1}W$. Forms on boundaries of this grade also form a one-dimensional space, so each is a number times $T_n$.

For a polyform $P$, denote this number by $\tau(P)$:

$$
P_{n-1}=\tau(P)T_n
$$

For example, if $P_{n-1}=7T_n$, then $\tau(P)=7$; if the component of grade $n-1$ is absent, then $\tau(P)=0$. In particular, $\tau(M)=\tau(G)$. The fixed form $T_n$ is retained when passing to another polyform.

> [!info] Potential and normalized potential
> **Definition.** For a form $f$ on boundaries, its polyform potential and normalized potential are
>
> $$
> u_M(f)=\tau(Mf),\qquad
> \frac{u_M(f)}{u_M(e)}=\frac{\tau(Mf)}{\tau(M)}
> \tag{6}
> $$

The polyform potential $u_M(f)$ is not the electrical potential $\varphi_i$ at a vertex. The former is determined by the form $f$ and the metric polyform $M$; the latter arises when solving the network equations with prescribed currents or potential values.

For a homogeneous form of grade $k$, $0\le k\le n-1$, only the complementary grade of the exponential contributes to (6):

$$
u_M(f)=\tau(M_{n-1-k}f)
$$

In the project, the normalized potential is also called the PMG norm of the form. For an arbitrary form, this is not a norm in the usual sense: the evaluation is linear and may have either sign. For a quadratic form, it will equal the quadratic norm of its argument.

Consider the meaning of the potential for a single pair form $f=[a_{ij}]^2$. Only $M_{n-2}$, the sum of spanning 2-forest forms, completes it to the top grade. If $i,j$ lie in the same forest component, their difference is a linear combination of that component's edge vectors, so its exterior product with them is zero. If the vertices lie in different components, adding the pair $ij$ joins them into a spanning tree, whose form is $T_n$.

Extracting the top-grade coefficient therefore retains exactly the weights of forests separating $i$ and $j$. Their sum $m_{ij}$ was introduced in the [[Variation of a Single Edge#Weights of separating spanning forests|forest formula for resistance]]. Thus

$$
u_M([a_{ij}]^2)=m_{ij},\qquad
\frac{u_M([a_{ij}]^2)}{\tau(M)}=\frac{m_{ij}}{\tau(G)}=R_{ij}
$$

The normalized potential recovers resistance before we invoke the general theorem for higher-grade metrics.

### Example: normalization on a unit-conductance triangle

For unit-conductance $K_3$ with vertices $a,b,c$, set $p=[(ab)]^2$. The expansion already computed is

$$
M=e+[(ab)]^2+[(bc)]^2+[(ac)]^2+3T_3,\qquad T_3=[(abc)]^2
$$

Thus $\tau(M)=3$. After multiplication by $p$, only $Lp$ contributes to the top grade. The term $p^2$ vanishes, while the other two terms each give $T_3$:

$$
Lp=[(bc)]^2[(ab)]^2+[(ac)]^2[(ab)]^2=2T_3
$$

Consequently,

$$
u_M(p)=\tau(Mp)=2,\qquad
\frac{\tau(Mp)}{\tau(M)}=\frac23=R_{ab}
$$

The number $2$ is the potential of the form; dividing by $3$ gives the resistance. We can now state this rule for boundaries of any grade.

## Agreement with the resistance metric

> [!info] The metric identity
> **Theorem.** For any boundaries $X,Y\in\Lambda^kW$, $0\le k\le n-1$,
>
> $$
> \frac{\tau(M[X,Y])}{\tau(M)}=X\cdot Y,\qquad
> \frac{\tau(M[X]^2)}{\tau(M)}=X^2
> \tag{7}
> $$
>
> The right-hand sides use the induced metric from [[Metric of Higher-Grade Objects]]; $X^2=X\cdot X$ is a number, while $[X]^2$ is a formal object.


This result does not define the evaluation of forms of elements or arbitrary simplices outside the boundary subalgebra.

The general justification uses the determinant lemma below. Its proof can be skipped on a first reading: the triangle already illustrates the normalization, and formula (7) gives the calculation rule.

## A general lemma on the top-grade coefficient

> [!info] The determinant lemma
> **Lemma.** Let $b_1,\ldots,b_d$ be a basis of a vector space, let $A$ be a symmetric invertible matrix, and set
>
> $$
> L_A=\sum_{p,q=1}^d A_{pq}[b_p,b_q],\qquad
> T=[b_1 \cdots b_d]^2
> $$
>
> Let $\tau_b$ denote the coefficient of $T$. For decomposable objects $X=u_1 \cdots u_k$, $Y=v_1 \cdots v_k$, let $U,V$ contain the coordinate columns of their factors in the basis $b$. Then
>
> $$
> \tau_b(\exp L_A)=\det A,\qquad
> \frac{\tau_b(\exp L_A[X,Y])}{\det A}
> =\det(U^{\mathsf T}A^{-1}V)
> \tag{8}
> $$
>
> The formula includes $k=0$ with $X=Y=1$ and the empty determinant equal to one. It extends to general structures of the same grade by bilinearity.

> [!note]- Proof of the lemma
> **Proof.** For any matrix $C$, set $L_C=\sum C_{pq}[b_p,b_q]$. At the top grade, expanding the product gives
>
> $$
> \frac{L_C^d}{d!}=(\det C)T
> $$
>
> Nonzero terms use each basis element exactly once in each argument. The signs of their permutations give the determinant signs, and the $d!$ orders of the factors cancel the denominator. Thus $\tau_b(\exp L_C)=\det C$, without requiring $C$ to be symmetric.
>
> Introduce variables $t_1,\ldots,t_k$ and $D=\operatorname{diag}(t_1,\ldots,t_k)$. Since $[u_i,v_i]^2=[u_i\wedge u_i,v_i\wedge v_i]=0$, commutativity of forms gives
>
> $$
> \exp\left(L_A+\sum_{i=1}^k t_i[u_i,v_i]\right)
> =\exp L_A\prod_{i=1}^k(e+t_i[u_i,v_i])
> $$
>
> After applying $\tau_b$, the coefficient of $t_1\cdots t_k$ is $\tau_b(\exp L_A[X,Y])$.
>
> The coefficient matrix of the polyform in the exponential on the left is $A+UDV^{\mathsf T}$. By the top-grade formula just proved and the matrix determinant lemma,
>
> $$
> \tau_b\left(\exp\left(L_A+\sum_i t_i[u_i,v_i]\right)\right)
> =\det A\det(I_k+DV^{\mathsf T}A^{-1}U)
> $$
>
> The coefficient of $t_1\cdots t_k$ on the right is $\det A\det(V^{\mathsf T}A^{-1}U)$. Since $A$ is symmetric, the last determinant equals $\det(U^{\mathsf T}A^{-1}V)$. Comparing coefficients proves (8). Decomposable exterior structures span each grade, so bilinear extension covers all $X,Y$. $\square$

> [!note]- Applying the lemma to the resistance metric
> **Proof.** Choose $d=n-1$ and the basis $b_i=a_i-a_n$ of $W$. In this basis, the coefficient matrix of the polyform $L$ is the reduced Laplacian $A=\mathbf L_0$, obtained by deleting the row and column of vertex $n$.
>
> The boundary and the basis volume are related by
>
> $$
> b_1 \cdots b_{n-1}=(-1)^{n-1}(a_1\ldots a_n)
> $$
>
> Hence $T=T_n$ and $\tau_b=\tau$: the orientation sign disappears in the quadratic form. The matrix $A$ is positive definite, and the [[From Lengths to Areas and Volumes|Gram matrix relative to the reference vertex]] shows that the matrix of inner products of the $b_i$ is $A^{-1}$.
>
> For decomposable $X,Y$, the right-hand side of (8) is the mixed Gram determinant. For linear combinations, both sides of (7) extend bilinearly. Thus the theorem applies to nondecomposable exterior structures as well as to products of edge vectors. $\square$

## Adding and deleting an edge

Let $p=[a_{ij}]^2$, and change the conductance of the pair $ij$ by $t$. An absent coupling has conductance $0$; the graph interpretation requires $c_{ij}+t\ge0$. Then $L'=L+tp$, $M'=\exp L'$, and

$$
\boxed{M'=M(e+tp)}
$$

For $t=c>0$, this adds conductance $c$, including strengthening an existing coupling. For $t=-c_{ij}$, the existing edge is deleted entirely:

$$
\boxed{M'=M(e-c_{ij}p)}
$$

> [!note]- Proof
> **Proof.** Since $p^2=0$, we have $\exp(tp)=e+tp$ and
>
> $$
> (e+cp)(e-cp)=e
> $$
>
> Commutativity of forms gives $\exp(L+tp)=\exp L\exp(tp)$. When the edge is deleted, the multiplier $e-c_{ij}p$ turns its edge factor into the identity. $\square$

If a set $S$ of existing edges is deleted, also denote the exponential of the remaining graph by $M'$. Then

$$
M'=M\prod_{\{i,j\}\in S}\bigl(e-c_{ij}[a_{ij}]^2\bigr)
$$

The order of deletion does not affect the result. These algebraic equalities remain valid if connectivity is lost: the exponential in that case is described under [[#Disconnected graphs]].

### The inverse exponential

Invertibility of every edge factor makes the whole exponential invertible:

$$
\boxed{
M^{-1}=\exp(-L)
=\prod_{\{i,j\}\in E}\bigl(e-c_{ij}[a_{ij}]^2\bigr)
}
$$

> [!note]- Proof
> **Proof.** Multiplication by (2) pairs each edge factor with its inverse; every pair gives $e$. The product of the factors with minus signs equals $\exp(-L)$ because forms commute. $\square$

Writing $M_k=L^k/k!$, inversion changes the signs of precisely the odd grades:

$$
M^{-1}=\sum_{k=0}^{n-1}(-1)^kM_k,\qquad M_0=e
$$

All sums are finite. Invertibility here refers to the polyform product and requires neither graph connectivity nor invertibility of the Laplacian matrix. The inverse exponential of the complement is used in the [[Symmetric Polyforms of the Complete Graph#Deleting edges from the complete graph|representation by deleting edges from the complete graph]].

## Disconnected graphs

Definitions (1)-(4) also apply to disconnected graphs. If a graph has $c$ components, including isolated vertices, the rank of its edge-vector system is $r=n-c$. Let $\deg M$ denote the highest nonzero grade of $M$. With positive coupling strengths on existing edges,

$$
\deg M=\operatorname{rank}\mathbf L=r,\qquad L^r\ne0,\qquad L^{r+1}=0
$$

The top-grade component is the quadratic form of the product of the boundaries of all components, multiplied by the product of their spanning-tree coefficients. An isolated vertex contributes boundary $1$ and coefficient $1$.

> [!example] Two disconnected edges
> For unit-conductance edges $12$ and $34$,
>
> $$
> M=e+[(12)]^2+[(34)]^2+[(12)(34)]^2
> $$
>
> The top grade is $4-2=2$. The top-grade component contains one form whose argument is the product of two component boundaries.

The number of components is $c=n-\deg M$, rather than the number of terms in the top-grade component. With no edges, $L=0$, $M=e$, and $L^0=e$ is the only nonzero power. For a disconnected graph, the coefficient of the fixed form $T_n$ is zero; the normalization described above is not applied to it.

## Algebraic variation and edge addition

For any affine vector $v$, the identity $([v]^2)^2=0$ gives

$$
\exp(L+t[v]^2)=M(e+t[v]^2)
$$

By (6) and (7),

$$
\frac{\tau(\exp(L+t[v]^2))}{\tau(M)}=1+t\,v^2
\tag{9}
$$

For $v=a_{ij}$, this changes the conductance of the pair $ij$ by $t$, provided the new conductances are admissible. For an arbitrary $v=\sum_i v_i a_i$ with $\sum_i v_i=0$, it is an algebraic variation with matrix perturbation $t\mathbf v\mathbf v^{\mathsf T}$.

For example, if $v=a_1+a_2-2a_3$ and $t>0$, the off-diagonal entry of the perturbation in position $12$ is positive. In the Laplacian representation, this decreases $c_{12}$ by $t$, rather than adding a single conductor. Admissibility of all new conductances must be checked separately; identity (9) does not depend on it.

For $p=[a_{ij}]^2$ and $M'=M(e+tp)$, linearity of top-grade coefficient extraction also gives

$$
u_{M'}(f)=u_M(f)+t\,u_M(pf)
$$

This holds for any form or polyform $f$ on boundaries. Deleting an existing edge of conductance $c$ gives

$$
u_{M'}(f)=u_M(f)-c\,u_M(pf)
$$

Indeed, $\tau(M'f)=\tau(Mf)+t\tau(Mpf)$. Setting $f=e$ recovers the change in the spanning-tree coefficient from [[Variation of a Single Edge]]. The formula for unnormalized potentials remains valid when a bridge is deleted; normalization by $\tau(M')$ requires the modified graph to be connected.

Similarly, lemma (8) allows arbitrary vectors $u_i,v_i$ in $W$. Its determinant formula is algebraic and does not require each direction to correspond to an edge.

## Computing potentials and norms

> [!example] The endpoints of the path $P_5$
> Here $M$ is the exponential of the unit-conductance path $P_5$. After multiplication by $[(15)]^2$, each of the four terms of $M_3$ gives $T_5$: the added edge joins the two components of the corresponding forest. Therefore,
>
> $$
> u_M([(15)]^2)=4,\qquad
> (15)^2=\frac41=4
> $$
>
> The normalization uses $\tau(P_5)=1$. Independently, the resistance between the endpoints is the sum of four unit resistances.

> [!example] Adjacent vertices of the cycle $C_4$
> Here $M$ is the exponential of the unit-conductance cycle $C_4$. Of the six terms of $M_2$, three give zero when multiplied by $[(12)]^2$. The nonzero contributions correspond to the edge sets $\{23,34\}$, $\{34,41\}$, $\{23,41\}$. Each becomes a spanning tree after adding $12$. Hence
>
> $$
> u_M([(12)]^2)=3,\qquad
> (12)^2=\frac34
> $$
>
> The potential is $3$, and the normalized potential is $3/4$, since $\tau(C_4)=4$. An electrical check uses parallel paths with resistances $1$ and $3$: $R_{12}=1\cdot3/(1+3)=3/4$.

## Connections with geometry and further reading

The forest expansion describes the coefficients of the exponential, while theorem (7) relates extraction of its top-grade coefficient to the induced metric. At grade one, it recovers effective resistances and inner products; at higher grades, it gives mixed Gram determinants and squared volumes.

In [[Further Reading for the PMG Introductory Series|the reading recommendations]], source [3] covers the matrix-tree theorem, [5] the matrix determinant lemma, and [7] and [8] exterior algebra and the Cauchy-Binet formula. The metric identity in the adopted algebra of forms is proved by lemma (8) and its application to the reduced Laplacian.
