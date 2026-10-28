---
title: Laplacian and Greenian - Mutual Duality of Exponentials
date: 2026-10-28
updated: 2026-10-28
revision: 1
translated_revision: 8
status: draft
text_prepared_by: ChatGPT
translation_key: dual-polyform-definition-metric-recovery
lang: en
order: 1
description: "The Laplacian and Greenian as vector forms: boundary exponentials, mutual duality through exterior deletion, normalization, and a complete path example."
---

The Laplacian $L$ and the Greenian $\mathrm{Gr}$ are two grade-one forms related by inversion of their matrices on the space of affine vectors. In the symmetric case, both are **vector forms**: they admit representations as sums of quadratic forms of vertex differences. Their exterior exponentials are **boundary polyforms** with components of different grades.

Duality describes the relationship between these exponentials. To express it through exterior deletion, the Greenian is transferred to the dual space. Grade $k$ of one exponential then recovers the complementary grade $n-1-k$ of the other by acting on its top component. This relationship is mutual; “dual” is not the proper name of just one of the two polyforms.

The algebraic mechanism uses the standard interior product in exterior algebra and the duality of complementary exterior powers. Below, this machinery is expressed in PMG notation, the uniqueness of the dual representation is proved, and the unit path $a-b-c-d$ is worked out in full. The main working representation of the Greenian is a [[The Canonical Vector Representation of the Greenian|vector sum]] with coefficients $-\mathrm{Gr}_{ij}$; cut forms provide an equivalent expression and a compact check of deletion.

## Initial objects

Consider a connected undirected graph on $n\ge2$ vertices with positive conductances on its existing edges. Absent edges have zero conductance. All spaces are real.

The vertices $a_1,\ldots,a_n$ form a linearly independent basis of a space $V$. The affine-weight functional and the space of affine vectors are

$$
\varepsilon(a_i)=1,\qquad
W=\ker\varepsilon,\qquad d=\dim W=n-1
$$

Boundaries belong to the exterior algebra $\Lambda W$. In particular,

$$
a_{ij}=a_j-a_i=(a_i a_j),\qquad
\Omega=(a_1\ldots a_n)=\partial(a_1\cdots a_n),\qquad
T=[\Omega]^2
$$

Here $\Omega$ is a nonzero boundary of the highest grade $d$, and $T$ is the fixed top, or spanning, form. Permuting the vertices may change the sign of $\Omega$ but leaves $T$ unchanged.

We use formal forms $[X,Y]$, bilinear in their arguments, and the notation

$$
[X]^2=[X,X],\qquad
[X,Y][A,B]=[XA,YB],\qquad e=[1,1]
$$

Products within form arguments are exterior products. The form $[X]^2$ is distinct from the numerical norm $X\cdot X$ and from the exterior self-product $X\wedge X$. The definitions are collected in [[Basic Objects and Operations of Polyform Algebra]].

The Laplacian polyform and its exponential are

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
M=\exp L=\sum_{j=0}^{d}M_j,\qquad
M_j=\frac{L^j}{j!},\qquad M_0=e
\tag{1}
$$

Defining duality requires only $M_d\ne0$. The spanning-tree interpretation of this component's coefficient will be used after the definition.

### The Laplacian and the Greenian as vector forms

Let $\mathbf L$ be the Laplacian matrix and $\mathbf{Gr}=\mathbf L^+$ the Green matrix. We call the corresponding grade-one form the **Greenian**:

$$
\boxed{
\mathrm{Gr}=\sum_{i,j}\mathrm{Gr}_{ij}[a_i-h,a_j-h]
=-\sum_{i<j}\mathrm{Gr}_{ij}[a_{ij}]^2,
\qquad h=\frac1n\sum_i a_i
}
$$

The two expressions are equal because the Green matrix is symmetric and has zero row sums. Both $L$ and $\mathrm{Gr}$ belong to $\operatorname{Sym}^2(W)$; their coefficients are $c_{ij}$ and $\gamma_{ij}=-\mathrm{Gr}_{ij}$, respectively. The second coefficient system may contain both signs.

The Greenian must be distinguished from the Gram matrix $\mathbf G$ of an arbitrary collection of elements. The matrices of the two vector forms are mutual pseudoinverses:

$$
\mathbf{Gr}=\mathbf L^+,\qquad
\mathbf{Gr}^+=\mathbf L,\qquad
\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J,\qquad
\mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T}
$$

On $\mathbf1^\perp$, this is ordinary inversion. The product here is a matrix product, not a polyform product.

Each exponential is a product of factors of the form $e+c[a_{ij}]^2$. Thus grade $k$ contains quadratic forms of exterior products of $k$ vectors, belonging to $\Lambda^kW$. In this sense, the exponentials are boundary polyforms. The statement about a sum of quadratic forms of **vectors** concerns their first grade; grades $k>1$ contain exterior objects of higher degrees.

The Greenian can also be written using dual elements. For this purpose, we construct $W^*$ below; whenever both spaces occur in a formula, we denote a dual element by $a_i^\vee$ and a direct vertex by $a_i$. The centered identification $\mathcal C:a_i^\vee\mapsto p_i=a_i-h$ maps $W^*$ to $W$. The first dual grade $Q_1$ will be a representation of the Greenian in $W^*$:

$$
\mathcal C(Q_1)=\mathrm{Gr},\qquad
D=\exp Q_1,\qquad
\mathcal C(D)=\exp(\mathrm{Gr})
$$

These equalities are proved in the [[The Exterior Exponential and Representations of the Greenian#The centered image and the Greenian|theorem on the centered image]]. Distinguishing $Q_1$ from $\mathrm{Gr}$ preserves the meaning of their arguments: the former acts by deletion, while the latter is expressed on direct vectors. Below, “the dual representation of the Greenian” denotes precisely $Q_1$, and $Q_k$ denotes the grades of its exponential.

## The interior product and deletion notation

### Deletion from an exterior object

For a linear functional $\varphi\in V^*$, the standard **interior product**, or contraction, is defined by

$$
\iota_\varphi(v_1\cdots v_r)
=\sum_{\ell=1}^{r}(-1)^{\ell-1}\varphi(v_\ell)
v_1\cdots\widehat{v_\ell}\cdots v_r
\tag{2}
$$

The hat over a factor means that it is omitted. The operation extends linearly and vanishes on scalars. It is a standard operation of exterior algebra [1, Chapters 5–6]. Here a functional acts on an exterior object; the equivalent dual notation uses a vector acting on an exterior form.

Let $a_i^*$ be the coordinate functional: $a_i^*(a_j)=\delta_{ij}$. In PMG notation, set

$$
X/a_i:=\iota_{a_i^*}X
$$

The symbol $a_i$ to the right of the slash denotes the **dual deletion element** corresponding to the vertex. For example,

$$
abc/a=bc,\qquad
abc/b=-ac,\qquad
abc/c=ab
$$

If the corresponding vertex does not occur in an exterior basis product, the result is zero. Deletion is linear in both arguments: for example, $X/(a+b)=X/a+X/b$.

For a product of dual elements, we fix the order of action:

$$
X/(u_1\cdots u_k)
=\bigl(\cdots((X/u_1)/u_2)\cdots\bigr)/u_k
\tag{3}
$$

Interchanging adjacent dual elements changes the sign, while deleting the same element twice gives zero. Thus the deletion argument itself belongs to an exterior algebra. For $k>r$, deletion from an object of grade $r$ is zero.

The name “deletion” describes the action of (2) on basis products. The slash denotes this linear operation, not inversion of the exterior product.

### Why the dual vertices sum to zero

The sum of the coordinate functionals is the affine-weight functional:

$$
a_1^*+\cdots+a_n^*=\varepsilon
$$

Its interior product is the boundary operator. Therefore

$$
X/(a_1+\cdots+a_n)=\partial X
$$

For a boundary $X\in\Lambda W$, we have $\partial X=0$. Consequently, when acting on boundaries, the following dual relation holds:

$$
\boxed{a_1+\cdots+a_n\equiv0}
\tag{4}
$$

Equality (4) concerns the **dual deletion elements**. The original vertices in $V$ remain linearly independent.

The precise construction is

$$
V^*/\mathbb R\varepsilon\cong W^*
$$

Two functionals define the same dual element if their restrictions to $W$ coincide. Write this class explicitly as $a_i^\vee=a_i^*+\mathbb R\varepsilon$. Then

$$
\sum_i a_i^\vee=0,\qquad
p_i=a_i-h,\qquad
\sum_i p_i=0,\qquad
\mathcal C(a_i^\vee)=p_i
$$

In deletion formulas and sections devoted entirely to the dual side, we retain the short notation $a_i$ for $a_i^\vee$, including $a,b,c,d$ in examples. We use $\vee$ in formulas that pass between the spaces. The zero-sum relation does not apply to the original independent vertices.

### Deletion from a form

For direct objects $X,Y$ of the same grade and dual objects $A,B$ of the same grade, define

$$
[X,Y]/[A,B]=[X/A,Y/B]
\tag{5}
$$

The action extends bilinearly to forms and polyforms. It is the interior product in each of the two tensor arguments. Its standard formulation for double forms is given by Belkhirat and Labbi [2, §4 of the open preprint]; here we use the natural pairing of direct and dual spaces, without choosing a graph metric.

In particular,

$$
T/[A]^2=[\Omega/A]^2,\qquad T/e=T
$$

The coefficients of a dual form enter the result **linearly**:

$$
T/(cF)=c(T/F),\qquad
T/(F+H)=T/F+T/H
\tag{6}
$$

Thus a scalar factor to the right of the deletion sign is not inverted. Ordinary division of a form by a number, such as $F/\tau$, still means multiplying the form by $1/\tau$.

Forms on dual arguments multiply by the same exterior rule:

$$
[A,B][C,D]=[AC,BD]
$$

This product is commutative: interchanging the forms cancels the signs in the two arguments. It differs from the action (5), which lowers the grade of the direct form.

## Definition of polyform duality

**Definition.** The dual grade polyform $Q_k$ of a metric polyform $M$, relative to its nonzero top component $M_d$, is the form on $\Lambda^kW^*$ such that

$$
\boxed{M_d/Q_k=M_{d-k}},\qquad 0\le k\le d
\tag{7}
$$

The polyform dual to $M$ in the chosen normalization is defined by the sum

$$
D=\sum_{k=0}^{d}Q_k
$$

By linearity of deletion, its action recovers the entire metric polyform:

$$
\boxed{M_d/D=M}
\tag{8}
$$

In (7), a “form on $\Lambda^kW^*$” means an element of $\Lambda^kW^*\otimes\Lambda^kW^*$; the graph forms in this note are symmetric under interchange of the arguments.

### Existence and uniqueness

**Lemma (complementary exterior powers).** For nonzero $\Omega\in\Lambda^dW$, the map

$$
C_\Omega:\Lambda^kW^*\longrightarrow\Lambda^{d-k}W,\qquad
A\longmapsto\Omega/A
$$

is a linear isomorphism.

**Proof.** Choose a basis $u_1,\ldots,u_d$ of $W$ and the dual basis $u^1,\ldots,u^d$. Then $\Omega=\lambda u_1\cdots u_d$, with $\lambda\ne0$.

Deleting the basis product $u^{i_1}\cdots u^{i_k}$ leaves the product of those $u_j$ whose indices were not deleted, with coefficient $\lambda$ and the appropriate sign. Different sets of $k$ indices correspond to different complementary sets of $d-k$ indices. Thus a basis maps to a basis with nonzero coefficients. $\square$

**Theorem.** All forms $Q_k$ in (7) exist and are unique in the dual space subject to relation (4).

**Proof.** Applying $C_\Omega$ in both arguments and multiplying by the coefficient of $T$ in $M_d$ gives an isomorphism

$$
C_{M_d}:\Lambda^kW^*\otimes\Lambda^kW^*
\longrightarrow
\Lambda^{d-k}W\otimes\Lambda^{d-k}W,\qquad
F\longmapsto M_d/F
$$

Since $M_d$ is a nonzero scalar multiple of $T$, this map differs from the action of $T$ only by a nonzero factor. Hence every $M_{d-k}$ has a unique preimage. The map preserves symmetry under interchange of the arguments, so the preimage of a symmetric form is also symmetric. $\square$

The dual form itself is unique, but its expression as a sum of terms need not be. For example, different vertex sums may represent the same class under relation (4).

### Connection with classical exterior duality

Passing from grade $k$ to the complementary grade $d-k$ through a top exterior element is a standard algebraic construction. In mixed exterior algebra, the Poincaré map is defined by contraction with a normalized top element [3, §2, formula (6)]. For double forms, the connection between this action and the double Hodge operator is given in [2, Proposition 4.3, formula (15) of the open preprint].

In our notation, the domain and image are first distinguished as dual and direct spaces, and the top element describing deletion is the specific boundary $\Omega=(a_1\ldots a_n)$. The corresponding top component $M_d$ serves as the reference for defining duality. Thus definition (7) does not require an inner product or unit volume to be introduced in advance. Comparison with a metric Hodge operator requires the identification of the spaces and the normalization of the top element to be matched separately.

The application to PMG consists of choosing $M=\exp L$, using its top component $M_d$ as the reference, and interpreting the resulting dual grades. The interior product and the duality of complementary powers themselves are used in their standard sense.

## Normalization and grade zero

At $k=0$, definition (7) gives $M_d/Q_0=M_d$. Since the action is linear and $M_d\ne0$, we obtain

$$
\boxed{Q_0=e}
\tag{9}
$$

The unit is the basic normalization of both exponentials. It does not require the spanning-tree sum to be introduced first.

For a graph, the [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|forest expansion of the exponential]] gives

$$
M_d=\tau T,\qquad
\tau=\sum_{F\text{ a spanning tree}}\prod_{\{i,j\}\in F}c_{ij}>0
\tag{10}
$$

For unit conductances, $\tau$ is the number of spanning trees. In general, it is their total weight, or spanning coefficient. Therefore (7)–(8) become

$$
\boxed{(\tau T)/Q_k=M_{d-k},\qquad (\tau T)/D=M}
\tag{11}
$$

Set $T^\vee=[a_1^\vee\cdots a_{n-1}^\vee]^2$. This is a form on dual elements; any one vertex may be omitted, and $T/T^\vee=e$. At $k=d$, (7) gives

$$
Q_d=\frac1\tau T^\vee
$$

Thus the top coefficients of the direct and dual exponentials are reciprocals. The coefficient $1/\tau$ refers to the fixed vertex form $T^\vee$.

**Corollary.** The Greenian exponential in its dual representation $D$ retains all information about $M$, including the conductance scale.

**Proof.** The coefficient of $T^\vee$ in $Q_d$ determines $1/\tau$. Once $\tau$ is recovered, formula (11) recovers all direct grades. $\square$

### The Greenian exponential in its dual representation

In the symmetric case, the general result is

$$
Q_1=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij},\qquad D=\exp Q_1
$$

Here $Q_1$ is the dual representation of the Greenian; its differences consist of dual elements, while $\mathbf{Gr}=\mathbf L^+$ refers to the original graph. The canonical nature of the expression, the centroid interpretation of its coefficients, and the expansion of the exponential over signed forests are proved in [[The Canonical Vector Representation of the Greenian]]. Vector forms multiply by the rules for merging and annihilating boundaries.

On the dual side, the full boundary and the product of all but one vertex have different normalizations:

$$
\Theta=[(a_1^\vee\ldots a_n^\vee)]^2=n^2T^\vee,\qquad
Q_d=\frac1{n^2\tau}\Theta=\frac1\tau T^\vee
$$

The coefficient of $\Theta$ is the signed spanning-tree sum of the weights $\gamma_{ij}$. These dual arguments must be distinguished from the direct boundary defining $T$.

### Mutuality of duality

Duality between the exponentials of symmetric nondegenerate forms is mutual. In matched direct and dual bases, their first grades have coefficient matrices $\mathbf A$ and $\mathbf A^{-1}$. Inverting again returns $\mathbf A$. Thus the [[The Exterior Exponential and Representations of the Greenian#The dual exponential of a nondegenerate symmetric form|exponential duality theorem]], applied in both directions, gives

$$
\boxed{
M_d/Q_k=M_{d-k},\qquad
Q_d/M_k=Q_{d-k},\qquad 0\le k\le d
}
$$

In the second equality, direct elements act on dual ones through the natural identification $W^{**}=W$. In particular, $M_d/D=M$ and $Q_d/M=D$. This is mutual duality relative to their own top components, not invertibility under ordinary multiplication.

After transfer to the same centered space, the two exponentials multiply by the usual law:

$$
\exp L\,\exp(\mathrm{Gr})=\exp(L+\mathrm{Gr}),\qquad
(\exp L)^{-1}=\exp(-L)
$$

The matrix $\mathbf L\mathbf{Gr}=\mathbf J$ describes composition of linear operators. It does not give the exterior product of these exponentials.

### The auxiliary forest normalization

To write unnormalized forest sums, it is convenient to define separately

$$
\widetilde Q_k=\tau Q_k,\qquad
\widetilde D=\tau D,\qquad
T/\widetilde D=M
$$

This auxiliary polyform has $\widetilde Q_0=\tau e$ and $\widetilde Q_d=T^\vee$. Throughout the series, the symbols $Q_k,D$ without a tilde refer to the basic normalization $Q_0=e$; the tilde explicitly indicates the forest normalization. The change multiplies every grade by $\tau$, not just grade zero.

### Representations and normalizations at a glance

Write the centered Greenian exponential as $N=\mathcal C(D)=\exp(\mathrm{Gr})$. With $d=n-1$, we obtain:

| Object | Reference form or variable | Top term or coefficient |
| --- | --- | --- |
| $M=\exp L$ | Direct boundary $T=[(a_1\ldots a_n)]^2$ | $M_d=\tau T$ |
| $D=\exp Q_1$ | Dual vertex form $T^\vee$ | $Q_d=T^\vee/\tau$ |
| The same $D$ | Dual boundary $\Theta=n^2T^\vee$ | $Q_d=\Theta/(n^2\tau)$ |
| $N=\mathcal C(D)$ | Direct boundary $T$ | $N_d=T/(n^2\tau)$ |
| Full vector toponome of the Greenian | Monomial $x_d$ | Coefficient $1/(n^2\tau)$ |
| Rooted spectral specialization | Power $t^d$ | Coefficient $1/(n\tau)$ |

The rows for $D$ express the same top grade using different reference forms. The centered map satisfies $\mathcal C(\Theta)=T$ and $\mathcal C(T^\vee)=T/n^2$; the proof appears in the [[The Canonical Vector Representation of the Greenian#An independent matrix check|check of the top normalization]]. The last two rows concern [[Toponomes of the Greenian Exponential and Dual Pairs|reductions of the exponential]]: the additional factor $n$ comes from choosing a root in the single spanning component.

In all three exponentials $M,D,N$, grade zero is $e$. Their normalization must be distinguished from the explicitly marked forest expression $\widetilde D=\tau D$.

### A check on a single weighted edge

Let vertices $a,b$ be joined by an edge of conductance $c>0$. Then

$$
T=[(ab)]^2,\qquad M=e+cT,\qquad M_1=cT,\qquad \tau=c
$$

On the dual side, $a+b=0$ and $T/[a]^2=e$. Consequently,

$$
D=e+\frac1c[a]^2,\qquad
\widetilde D=ce+[a]^2
$$

Checking deletion gives

$$
(cT)/D=cT+e=M,\qquad T/\widetilde D=M
$$

Even with a unit in grade zero, the scale is retained: the top dual coefficient is $1/c$. The vector representation on the dual side is

$$
Q_1=\frac1{4c}[(ab)]^2=\frac1c[a]^2
$$

Here $(ab)=b-a=-2a$. Thus the factor $4$ is explained by the form argument.

## Full example: a path on four vertices

Consider the path $a-b-c-d$ with three unit conductances. Here $W$ has dimension $3$, the only spanning tree is the graph itself, and hence $\tau=1$ and $D=\widetilde D$.

### Direct grades of the exponential

We have

$$
L=[(ab)]^2+[(bc)]^2+[(cd)]^2,\qquad
T=[(abcd)]^2
$$

Expanding the product

$$
M=(e+[(ab)]^2)(e+[(bc)]^2)(e+[(cd)]^2)
$$

gives all direct grades:

$$
\begin{aligned}
M_0&=e\\
M_1&=[(ab)]^2+[(bc)]^2+[(cd)]^2\\
M_2&=[(abc)]^2+[(ab)(cd)]^2+[(bcd)]^2\\
M_3&=T
\end{aligned}
\tag{12}
$$

The three spanning 2-forests represented in $M_2$ have edges $ab,bc$; edges $ab,cd$; and edges $bc,cd$. Isolated vertices belong to the forest but contribute a factor of $1$ to the product of boundaries.

### The first dual grade

The canonical vector expression is

$$
\begin{aligned}
Q_1=\frac18\bigl(&-[(ab)]^2+3[(ac)]^2+5[(ad)]^2+{}\\
&+[(bc)]^2+3[(bd)]^2-[(cd)]^2\bigr)
\end{aligned}
$$

Its coefficients and products are calculated in detail in the [[The Canonical Vector Representation of the Greenian#Full example: a path on four vertices|vector calculation for the path]]. To check deletion directly, we use the equivalent cut expression.

The dual space satisfies

$$
a+b+c+d\equiv0
$$

Direct deletion from $\Omega=(abcd)$ gives

$$
\begin{aligned}
(abcd)/a&=-(bcd)\\
(abcd)/(a+b)&=(ab)(cd)\\
(abcd)/d&=(abc)
\end{aligned}
$$

The signs disappear in the quadratic forms, so

$$
\begin{aligned}
T/[a]^2&=[(bcd)]^2\\
T/[a+b]^2&=[(ab)(cd)]^2\\
T/[d]^2&=[(abc)]^2
\end{aligned}
\tag{13}
$$

Consequently, by definition (7),

$$
\boxed{Q_1=[a]^2+[a+b]^2+[d]^2},\qquad
T/Q_1=M_2
\tag{14}
$$

Each term corresponds to a partition of the vertices into two forest components: $\{a\}\mid\{b,c,d\}$, $\{a,b\}\mid\{c,d\}$, or $\{a,b,c\}\mid\{d\}$. The dual argument is the sum of the vertices in one part. Either part can be used: for example, $a+b\equiv-(c+d)$, and hence $[a+b]^2=[c+d]^2$.

For the middle term, the partition is $\{a,b\}\mid\{c,d\}$, the set of path edges crossing it consists of $bc$, and the corresponding spanning forest consists of $ab$ and $cd$. These three objects play different roles. The form $[a+b]^2$ represents the partition through its dual deletion element.

### The second dual grade

Each of the forms $[a]^2$, $[a+b]^2$, and $[d]^2$ has square zero. In the square of their sum, each pair of distinct factors occurs twice:

$$
\frac{Q_1^2}{2!}
=[a(a+b)]^2+[ad]^2+[(a+b)d]^2
$$

In the exterior algebra of dual elements,

$$
a(a+b)=ab,\qquad
(a+b)d=(-c-d)d=-cd
$$

Therefore

$$
\frac{Q_1^2}{2!}=[ab]^2+[ad]^2+[cd]^2
$$

Now check the action of this form independently:

$$
\begin{aligned}
T/[ab]^2&=[(cd)]^2\\
T/[ad]^2&=[(bc)]^2\\
T/[cd]^2&=[(ab)]^2
\end{aligned}
$$

The sum equals $M_1$ from (12). By uniqueness of the dual grade,

$$
\boxed{Q_2=\frac{Q_1^2}{2!}=[ab]^2+[ad]^2+[cd]^2},\qquad
T/Q_2=M_1
\tag{15}
$$

In particular, $[ab]^2$ here has a dual argument consisting of two vertices; parentheses $(ab)$ still denote a boundary.

### The third dual grade

In the cube of $Q_1$, only products of all three distinct terms survive. They occur in $3!$ orders, so

$$
\frac{Q_1^3}{3!}=[a(a+b)d]^2=[abd]^2
$$

Successive deletion gives

$$
(abcd)/(abd)=1,\qquad T/[abd]^2=e=M_0
$$

Consequently,

$$
\boxed{Q_3=\frac{Q_1^3}{3!}=[abd]^2}
\tag{16}
$$

All higher powers vanish because the dual space has dimension $3$.

### Comparing all grades

| Dual grade | Dual form | Recovered direct grade |
|---:|---|---|
| $0$ | $Q_0=e$ | $T/Q_0=M_3=T$ |
| $1$ | $Q_1=[a]^2+[a+b]^2+[d]^2$ | $T/Q_1=M_2$ |
| $2$ | $Q_2=[ab]^2+[ad]^2+[cd]^2$ | $T/Q_2=M_1$ |
| $3$ | $Q_3=[abd]^2$ | $T/Q_3=M_0=e$ |

Calculations (13)–(16) establish for this path that

$$
\boxed{
D=e+Q_1+\frac{Q_1^2}{2!}+\frac{Q_1^3}{3!}
=\exp Q_1,\qquad T/D=M
}
\tag{17}
$$

Equivalently,

$$
D=(e+[a]^2)(e+[a+b]^2)(e+[d]^2)
$$

The coefficients $1/2!$ and $1/3!$ were obtained by counting factor orders, and correspondence with the direct grades was checked by deletion from $T$. The general exponential formula for an arbitrary connected graph was not assumed in this calculation.

## What the dual representation retains

For fixed vertices, the highest dual grade determines $\tau$, after which formula (11) recovers all direct grades. Thus the Greenian exponential in its dual representation determines the whole of $M$, in particular $M_1=L$, and hence the graph conductances. Recovering $M$ also recovers its normalized potentials and resistance metric; their relationship is proved in the [[Laplacian Exponential#The potential of a form|definition of potential]] and the [[Laplacian Exponential#A general lemma on the top-grade coefficient|determinant lemma]].

The transition changes the exterior arguments: a direct object of grade $d-k$ is replaced by a dual object of grade $k$ whose deletion from the top element yields the original object. The correspondence of complementary grades is ensured by the isomorphism $C_{M_d}$.

Duality (7) must be distinguished from inversion in the polyform algebra: the inverse exponential satisfies $M\exp(-L)=e$, whereas the defining action here is $M_d/D=M$. The connection with matrix inversion is established by the exponential duality theorem; duality of graphs or matroids does not follow automatically. Sharing a vertex set is insufficient for two polyforms to be dual: equalities (7) are required.

This note proves the existence and uniqueness of the polyform dual to $M$, its normalization, and recovery of the original metric polyform. The Greenian exponential in its dual representation is calculated directly for a path on four vertices. The general forest formula for all dual grades and their representation through block sums are proved in [[Cuts and Forest Grades of the Greenian Exponential]]. The general exponential law and its connection with the Greenian are proved in [[The Exterior Exponential and Representations of the Greenian]]. The central comparison with the Laplacian, the centroid interpretation of coefficients, and signed spanning-tree sums are presented in [[The Canonical Vector Representation of the Greenian]]. The transition to polar and forest coefficients for variations is examined in [[Greenian Coefficients and Vertex Variations]]. The results here concern connected undirected graphs; the balanced extension requires separate treatment.

## References

1. Greub W. *Multilinear Algebra*. 2nd ed. Springer, 1978. [DOI: 10.1007/978-1-4613-9425-9](https://doi.org/10.1007/978-1-4613-9425-9). Chapters 5, “Exterior Algebra”, and 6, “Mixed Exterior Algebra”, present the classical machinery of exterior and mixed exterior algebra.
2. Belkhirat A., Labbi M. *On the composition and exterior products of double forms and p-pure manifolds*. Turkish Journal of Mathematics, 43(1) (2019), 539–560. [DOI: 10.3906/mat-1809-25](https://doi.org/10.3906/mat-1809-25). Open preprint: *Interactions between the composition and exterior products of double forms and applications*, [arXiv:1402.4072v1](https://arxiv.org/abs/1402.4072v1), 2014. References in the text to §4, Proposition 4.3, and formula (15) refer to this preprint version: the interior product in two arguments and its connection with the double Hodge operator.
3. Vanstone J. R. *The Poincaré Map in Mixed Exterior Algebra*. Canadian Mathematical Bulletin, 26(2) (1983), 129–136. [DOI: 10.4153/CMB-1983-021-2](https://doi.org/10.4153/CMB-1983-021-2); [open text](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CCF86BA5865EA358BE3C47E7D414065A/S0008439500062883a.pdf/the-poincare-map-in-mixed-exterior-algebra.pdf). §2, formula (6), p. 130: the Poincaré map through the interior product with a top element.

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
