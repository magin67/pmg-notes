---
title: Reducibility of Toponomes
date: 2026-10-23
updated: 2026-10-23
revision: 1
source_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: reducibility-of-toponomes
lang: en
description: "Factorization of full, two-variable, and one-variable toponomes: ordinary multiplication, the second-kind product, graph components, and irreducibility proofs."
order: 4
---

The Laplacian exponential has a factor representation in the polyform algebra. The one-variable vertex toponome also factors, with factors related to the eigenvalues of the Laplacian matrix. Between these constructions lie the full partition toponome and its coefficient triangle. How does factorization behave at these levels?

**Under ordinary multiplication, the full and two-variable toponomes of a connected graph are irreducible. For an arbitrary graph, their irreducible factors correspond to components with edges. Under the second-kind product, the forest toponome of any graph with edges is irreducible both at the positive-type level and after grouping into a coefficient table; connectivity is not required.** Passing to one variable can create new factors. These statements are proved below for positive conductances and compared in simple examples.

## Objects and the meaning of reducibility

Let $G$ be a finite simple undirected graph with positive conductances on existing edges. Connectivity will be specified separately. Throughout, fix the [[From Polyforms to Partitions#The Laplacian exponential and forest coefficients|canonical forest expansion of the exponential]]: a type coefficient is the sum of the weights of spanning forests of that type.

A positive type $\lambda=(k_1,\ldots,k_r)$ records the edge counts of the nontrivial forest components; singleton vertices are omitted. Write

$$
x_\lambda=\prod_{i=1}^r x_{k_i},
\qquad
h(\lambda)=\prod_{i=1}^r(k_i+1)
$$

For the empty type, both products are $1$. By the [[Vector and Vertex Normalizations of Toponomes|normalization definitions]], the full toponomes are

$$
\begin{aligned}
T_G^{\mathrm{vec}}(\mathbf x)&=\sum_\lambda c_G(\lambda)x_\lambda=T_G(\mathbf x)\\
T_G^{\mathrm{vert}}(\mathbf x)&=\sum_\lambda c_G(\lambda)h(\lambda)x_\lambda
\end{aligned}
$$

The two-variable toponomes are obtained by substituting $x_j=t^ju$ in the corresponding normalization:

$$
\begin{aligned}
F_G(t,u)&=1+\sum_{k,r}a_{k,r}t^ku^r\\
P_G(t,u)&=1+\sum_{k,r}b_{k,r}t^ku^r
\end{aligned}
$$

Here $k$ is the grade and $r$ the number of nontrivial components. The coefficients form a [[Coefficient Tables of Toponomes|triangle]]; the unit term is treated separately. Setting $u=1$ gives $F_G(t)$ and $P_G(t)$.

> [!info] Objects and the meaning of reducibility
> **Definition.** A nonzero nonconstant polynomial over a field $\mathbb K$ is reducible if it is the product of two nonconstant polynomials over the same field. Otherwise it is irreducible. For full and two-variable toponomes below, $\mathbb K=\mathbb R$ or $\mathbb C$; in the one-variable case, the field is specified explicitly. Irreducibility over $\mathbb C$ means absolute irreducibility for a polynomial with real coefficients.

Besides ordinary monomial multiplication, we use the product $*$ of the [[The Second-Kind Algebra on Partitions|second-kind algebra]]. It sums partial matchings of parts. For example,

$$
(1)*(1)=(1^2)+(2),
\qquad
x_1*x_1=x_1^2+x_2
$$

This algebra consists of finite sums of types; irreducibility is defined relative to $*$, and its units are the nonzero constants. Statements about two-variable and one-variable polynomials concern ordinary multiplication. The [[Coefficient Tables of Toponomes#Multiplication of tables|second-kind product induced on tables]] is considered separately below through a falling-power representation.

## Two products of cells

A pair $(k,r)$ specifies a cell of the coefficient triangle: $k$ connections and $r$ nontrivial components. It is not a numerical partition type. For example, cell $(3,1)$ corresponds to forests with one nontrivial component of three connections, whereas positive type $(3,1)$ describes two nontrivial components, with three and one connections.

Let $u_{k,r}$ denote the table with a one in cell $(k,r)$ and zeros elsewhere. The unit $u_{0,0}$ corresponds to the empty forest. To distinguish the two table products, denote coordinatewise addition of pairs by $\circ$:

$$
\boxed{u_{k,r}\circ u_{l,s}=u_{k+l,r+s}}
$$

Extend the rule bilinearly to linear combinations. Under $u_{k,r}\leftrightarrow t^ku^r$, it becomes ordinary monomial multiplication. Thus $\circ$ and ordinary multiplication of two-variable polynomials are two notations for the same operation.

> [!info] Two products of cells
> **Lemma.** The $\circ$-product of the coefficient tables of two graphs is the table of their disjoint union.

> [!note]- Proof
> **Proof.** Each forest of the union is uniquely assembled from forests of the two original graphs. Edge counts and nontrivial component counts add, while weights multiply. The bilinear expansion of $\circ$ enumerates all such pairs. The same holds in vertex normalization, since root weights of independent components also multiply. $\square$

The second-kind table product [[Coefficient Tables of Toponomes#Multiplication of tables|additionally enumerates component matchings]] and reduces the component count at every gluing. The difference already appears for two unit cells:

$$
\begin{aligned}
u_{1,1}\circ u_{1,1}&=u_{2,2}\\
u_{1,1}*u_{1,1}&=u_{2,2}+u_{2,1}
\end{aligned}
$$

The first rule leaves the two components separate. The second includes both the separate case and the case in which they are joined. Factorization statements must specify the product concerned.

## Why exponential factors do not become type factors

In the polyform algebra,

$$
\exp L=\prod_{\{i,j\}\in E}\bigl(e+c_{ij}[a_{ij}]^2\bigr)
$$

Multiplication of forms uses the specific vertices shared by the edges. Passing to types loses this information: two edges always give the same factor types $(1),(1)$, regardless of their relative position.

For the unit-weight path $P_3$ and two independent unit-weight edges, respectively,

$$
T_{P_3}=1+2(1)+(2),
\qquad
T_{2K_2}=1+2(1)+(1^2)
$$

However, the product of the reduced factor forms is

$$
\bigl(1+(1)\bigr)*\bigl(1+(1)\bigr)
=1+2(1)+(1^2)+(2)
$$

It contains both possibilities: keeping the edges separate and gluing them into one component. The first possibility is absent from the path, and the second from the independent pair. Thus reduction of a forest representation to types does not preserve multiplication of specific polyforms. The geometric meaning of the sum of possibilities is discussed in [[Partition Products and Boundary Forms]].

The factors themselves also have different meanings. The factor form of a connection is invertible:

$$
\bigl(e+c[a]^2\bigr)^{-1}=e-c[a]^2
$$

This follows from $([a]^2)^2=0$. Consequently, the factor representation of the exponential is not a factorization into irreducible nonunits in the polynomial-theoretic sense; the exponential itself is invertible as well. See the [[Laplacian Exponential#The inverse exponential|inverse exponential]].

## The full toponome under ordinary multiplication

> [!info] Irreducibility of the full toponome
> **Theorem.** The full toponome of a connected graph with at least one edge is irreducible under ordinary polynomial multiplication. This holds in both normalizations over $\mathbb R$ and $\mathbb C$.

> [!note]- Proof using the highest variable
> **Proof.** Let the graph have $n\geqslant2$ vertices. Forests of grade $n-1$ are spanning trees and have the unique positive type $(n-1)$. Therefore
>
> $$
> T_G^{\mathrm{vec}}(\mathbf x)=\tau(G)x_{n-1}+R_{\mathrm{vec}}(x_1,\ldots,x_{n-2})
> $$
>
> $$
> T_G^{\mathrm{vert}}(\mathbf x)=n\tau(G)x_{n-1}+R_{\mathrm{vert}}(x_1,\ldots,x_{n-2})
> $$
>
> Here $\tau(G)>0$ is the sum of spanning-tree weights. The variable $x_{n-1}$ cannot occur in any other term: its weight is already the maximum grade.
>
> For either polynomial, consider a factorization $T=AB$. By degree in $x_{n-1}$, one factor, say $A$, is independent of that variable. Comparing coefficients of $x_{n-1}$ shows that $A$ divides the nonzero constant $\tau(G)$ or $n\tau(G)$. Thus $A$ is a nonzero constant. For $n=2$, the remainder is $1$, and the argument still applies. $\square$

> [!info] The full toponome under ordinary multiplication
> **Corollary.** Under ordinary multiplication, the irreducible factorization of the full toponome of an arbitrary graph is given by its connected components with edges:
>
> $$
> T_G^{\mathrm{vec}}=\prod_{i=1}^r T_{G_i}^{\mathrm{vec}},
> \qquad
> T_G^{\mathrm{vert}}=\prod_{i=1}^r T_{G_i}^{\mathrm{vert}}
> $$

> [!note]- Proof
> **Proof.** Forests in independent components are chosen independently, and their weights and root weights multiply. Hence the [[Vector and Vertex Normalizations of Toponomes#Disjoint union and multiplication|product lemma]] applies. Each resulting factor is irreducible by the theorem. $\square$

After normalizing the factors' constant terms to $1$, the factorization is unique up to order. It recovers the component toponomes, but does not claim to recover the graphs themselves up to isomorphism. Isolated vertices contribute factors of $1$ and are not detected separately.

## The two-variable toponome and the coefficient triangle

Grouping types into cells $(k,r)$ loses some information. Nevertheless, it retains the decisive feature for factorization: all forests of the highest grade of a connected graph have exactly one nontrivial component.

> [!info] Irreducibility of the two-variable toponome
> **Theorem.** The vector and vertex two-variable toponomes of a connected graph with at least one edge are irreducible over $\mathbb R$ and $\mathbb C$. Thus passing from the full toponome of a connected graph to its coefficient triangle preserves irreducibility.

> [!note]- Proof using the leading coefficient
> **Proof.** Denote either polynomial by $Q(t,u)$. For a connected graph on $n\geqslant2$ vertices,
>
> $$
> Q(t,0)=Q(0,u)=1,
> \qquad
> [t^{n-1}]Q(t,u)=\gamma u
> $$
>
> Here $\gamma=\tau(G)$ in vector normalization and $\gamma=n\tau(G)$ in vertex normalization. In both cases, $\gamma>0$.
>
> Suppose $Q=AB$ with both factors nonconstant. Since $Q(0,u)=1$, a factor depending only on $u$ must be constant. Thus both factors have positive degree in $t$.
>
> The equality
>
> $$
> A(t,0)B(t,0)=1
> $$
>
> implies that $A(t,0)$ and $B(t,0)$ are constant in $t$. Therefore the leading coefficients of $A$ and $B$ in $t$ are divisible by $u$. Their product, which is the leading coefficient of $Q$, is divisible by $u^2$. But $\gamma u$ is not divisible by $u^2$, a contradiction. $\square$

**Remark on Eisenstein's criterion.** The polynomial reversed in $t$, namely $t^{n-1}Q(1/t,u)$, has leading coefficient $1$. All other coefficients are divisible by $u$, while its constant term in $t$, $\gamma u$, is not divisible by $u^2$. Thus Eisenstein's criterion applies in $\mathbb K[u][t]$ with prime element $u$ [2]. The proof above presents the same argument directly for $Q$.

> [!info] The two-variable toponome and the coefficient triangle
> **Corollary.** The two-variable toponomes of an arbitrary graph factor as
>
> $$
> F_G(t,u)=\prod_{i=1}^r F_{G_i}(t,u),
> \qquad
> P_G(t,u)=\prod_{i=1}^r P_{G_i}(t,u)
> $$
>
> Here $G_1,\ldots,G_r$ are all components containing edges; each factor is irreducible. Consequently, for $r=1$ the polynomial is irreducible, for $r\geqslant2$ it is reducible, and for $r=0$ it is $1$. The number of irreducible factors, counted with multiplicity, is $r$.
>
> This follows from the independent-component lemma and the theorem just proved. Isolated vertices do not affect the polynomial: a graph with one nontrivial component and several isolated vertices also has an irreducible 2-toponome.

**The unit term is essential.** The triangle displays coefficients of nonempty forests. If only the corresponding sum $Q-1$ is considered, it has a common factor $tu$. The theorem concerns the full polynomial $Q$, including the empty forest's contribution $1$. Dividing triangle rows by additional coefficients likewise produces a different object outside the statement's scope.

### Example: two disjoint three-edge paths

The path $P_4$ has four vertices and three connections. For unit conductances, its vector toponome in cell notation is

$$
\mathcal A_{P_4}=u_{0,0}+3u_{1,1}+2u_{2,1}+u_{3,1}+u_{2,2}
$$

Among two-edge choices, two adjacent choices give one nontrivial component, and the choice of the two end edges gives two. The polynomial expression is

$$
F_{P_4}(t,u)=1+(3t+2t^2+t^3)u+t^2u^2
$$

By the lemma, $\mathcal A_{P_4\sqcup P_4}=\mathcal A_{P_4}\circ\mathcal A_{P_4}$. In polynomial notation,

$$
\begin{aligned}
F_{P_4\sqcup P_4}(t,u)={}&1+(6t+4t^2+2t^3)u+\\
&+(11t^2+12t^3+10t^4+4t^5+t^6)u^2+\\
&+(6t^3+4t^4+2t^5)u^3+t^4u^4
\end{aligned}
$$

For example, the coefficient $11$ of $t^2u^2$ consists of $9=3\cdot3$ pairs choosing one connection in each path, plus two choices of both end connections in one path while the other is empty.

The toponome of one path is irreducible under ordinary multiplication. The union's toponome is reducible and has two identical irreducible factors. This factorization is relative to $\circ$, not to the second-kind product.

**Independent check.** The coefficients of the expanded square were compared with direct enumeration of all $64$ subsets of the union's six edges. All subsets are forests; the edge and nontrivial component counts were computed separately for each. The tables agreed, and the coefficient sum is $64=2^6$.

## Irreducibility in the second-kind algebra

We now retain every positive type separately but change the product to $*$. In this algebra, independent graph components no longer give factors of the graph's forest toponome.

### Free generators and the highest variable

Denote one-part types by $\xi_j=(j)$. Under the [[The Second-Kind Algebra on Partitions#Realization by ordinary multiplication of symmetric functions|isomorphism with symmetric functions]], they correspond to power sums. These freely generate the algebra over a field of characteristic zero [1, Theorem 2.6.4]. Hence

$$
(\mathcal A,*)\simeq\mathbb K[\xi_1,\xi_2,\ldots]
$$

On the right, ordinary multiplication represents $*$; it is not multiplication of the monomials $x_\lambda$. For example,

$$
\begin{aligned}
(1^2)&=\xi_1^2-\xi_2\\
(2,1)&=\xi_2\xi_1-\xi_3\\
(1^3)&=\xi_1^3-3\xi_1\xi_2+2\xi_3
\end{aligned}
$$

Freeness can also be seen directly from the matching rule. In a product of one-part types, the term without mergers is the original type with coefficient $1$, while all other terms have fewer parts. For each fixed weight, the change between products of $\xi_j$ and basis types is triangular with diagonal entries $1$. It is therefore invertible: the generators span the entire algebra and satisfy no polynomial relations.

> [!info] Free generators and the highest variable
> **Lemma.** When a type of weight $d$ is expressed in the free generators, $\xi_d$ occurs linearly with a nonzero coefficient depending only on the number of parts. For $\lambda=(a_1,\ldots,a_r)$ and $d=a_1+\cdots+a_r$,
>
> $$
> \boxed{\lambda=(-1)^{r-1}(r-1)!\,\xi_d+H_\lambda(\xi_1,\ldots,\xi_{d-1})}
> $$

> [!note]- Proof by recursion on the number of parts
> **Proof.** The weight of $\xi_j$ is $j$. Thus, in an expression of weight $d$, $\xi_d$ can occur only as a single linear term. For one part, the type is $\xi_d$, with coefficient $1$.
>
> Let $r\geqslant2$ and $\mu=(a_1,\ldots,a_{r-1})$. The one-part multiplication rule gives
>
> $$
> \mu*(a_r)=\lambda+\sum_{i=1}^{r-1}\mu_i
> $$
>
> Here $\mu_i$ is obtained from $\mu$ by replacing $a_i$ with $a_i+a_r$. Both factors on the left have positive weight less than $d$ and are expressed through $\xi_1,\ldots,\xi_{d-1}$. Thus the coefficient of $\xi_d$ on the left is zero. Each type $\mu_i$ has $r-1$ parts and weight $d$.
>
> Inductively, the coefficient depends only on the part count and satisfies
>
> $$
> \alpha_1=1,\qquad \alpha_r=-(r-1)\alpha_{r-1}
> $$
>
> Hence $\alpha_r=(-1)^{r-1}(r-1)!$. $\square$

### The theorem for a forest toponome

> [!info] Irreducibility under the second-kind product
> **Theorem.** The forest toponome of a graph with positive conductances and at least one edge is irreducible in the second-kind algebra over $\mathbb R$ and $\mathbb C$. The graph need not be connected. The statement also holds after vertex weighting of the positive-type coefficients.

> [!note]- Proof using the unique type of highest grade
> **Proof.** Let $G_1,\ldots,G_r$ be the components with edges, $n_i$ the vertex count of $G_i$, and $\tau(G_i)>0$ its total spanning-tree weight. Set
>
> $$
> d=\sum_{i=1}^r(n_i-1),\qquad \tau=\prod_{i=1}^r\tau(G_i)
> $$
>
> A forest of maximum grade $d$ contains one spanning tree in each $G_i$. Its positive type is unique:
>
> $$
> \lambda_{\max}=(n_1-1,\ldots,n_r-1)
> $$
>
> Its coefficient is $\tau$. Every other type has weight less than $d$ and contains no $\xi_d$ when expressed in the generators. The lemma gives
>
> $$
> T_G=\tau(-1)^{r-1}(r-1)!\,\xi_d+H_G(\xi_1,\ldots,\xi_{d-1})
> $$
>
> The coefficient of $\xi_d$ is a nonzero constant. A polynomial linear in an independent variable with such a coefficient is irreducible: in any factorization, one factor is independent of $\xi_d$ and must divide that constant. Introducing higher-weight generators creates no new factorizations, since degrees in each additional variable add under multiplication.
>
> In vertex normalization, the coefficient of the highest type is additionally multiplied by $\prod_i n_i$, so it remains nonzero. The same argument applies. $\square$

For example, for two independent unit-weight edges, the ordinary polynomial and the expression in free generators are

$$
T_{2K_2}(\mathbf x)=(1+x_1)^2,
\qquad
T_{2K_2}=1+2\xi_1+\xi_1^2-\xi_2
$$

The first is reducible under ordinary multiplication, and the second is irreducible relative to $*$. These are two algebraic structures on the same coefficient space.

**Scope.** The theorem concerns canonical forest toponomes and does not assert irreducibility of all elements of $\mathcal A$. For example, $1+2(1)+(1^2)+(2)$ was already expressed above as $\bigl(1+(1)\bigr)^{*2}$. The essential graph-toponome property is a unique type of highest weight with nonzero coefficient. No truncation by vertex count or completion by formal infinite series is introduced: those constructions change questions of invertibility and factorization.

## Irreducibility of the table under the second-kind product

Grouping positive types into cells $(k,r)$ respects $*$, but that fact alone does not transfer irreducibility: a homomorphism can create new factorizations. We give a separate proof for the coefficient table.

Consider the algebra $\mathcal B$ of finite linear combinations of $u_{0,0}$ and $u_{k,r}$ with $1\leqslant r\leqslant k$, over $\mathbb K=\mathbb R$ or $\mathbb C$. The vertex count is not fixed, and tables are not truncated.

### Representation by falling powers

Introduce falling powers [6]:

$$
u^{\underline 0}=1,
\qquad
u^{\underline r}=u(u-1)\cdots(u-r+1)
$$

> [!info] Representation by falling powers
> **Lemma.** Assigning $t^ku^{\underline r}$ to a cell with $k$ connections and $r$ nontrivial components turns the second-kind product into ordinary polynomial multiplication. The map
>
> $$
> \Psi_*:\mathcal B\longrightarrow\mathbb K[t,u],
> \qquad
> \Psi_*(u_{k,r})=t^ku^{\underline r}
> $$
>
> preserves the unit and multiplication and is injective.

> [!note]- Proof of the representation
> **Proof.** Falling powers satisfy
>
> $$
> u^{\underline r}u^{\underline s}
> =\sum_{h=0}^{\min(r,s)}\binom rh\binom sh h!\,u^{\underline{r+s-h}}
> $$
>
> For an integer $u=N\geqslant r+s$, the left side counts pairs of ordered selections from $N$ elements: $r$ distinct elements in the first and $s$ in the second. If exactly $h$ elements are shared, select $h$ positions in each selection and a bijection between them. The resulting $r+s-h$ position classes can be filled with distinct elements in $N^{\underline{r+s-h}}$ ways. This gives the right side. Equality for infinitely many $N$ proves the polynomial identity.
>
> After multiplication by $t^{k+l}$, this is the [[Coefficient Tables of Toponomes#Multiplication of tables|cell-product rule]]. Thus $\Psi_*$ preserves multiplication and the unit. For fixed $k$, the polynomials $u^{\underline r}$ are linearly independent: they have distinct degrees $r$ and leading coefficient $1$. Different $k$ are distinguished by their powers of $t$, proving injectivity. $\square$

The units of $\mathcal B$ are exactly the nonzero constants: under the embedding into $\mathbb K[t,u]$, an invertible element must map to a nonzero constant. Hence irreducibility of the image in the full ring $\mathbb K[t,u]$ implies irreducibility of the original table under $*$.

### The theorem for a coefficient table

> [!info] Irreducibility of a table under the second-kind product
> **Theorem.** The coefficient table of the canonical forest toponome of any graph with positive conductances and at least one edge is irreducible under the induced second-kind product. This holds in both normalizations over $\mathbb R$ and $\mathbb C$, regardless of connectivity.

> [!note]- Proof using the leading coefficient
> **Proof.** Denote the coefficients in either normalization by $q_{k,r}$, so the table's image is
>
> $$
> \widehat Q_G(t,u)=1+\sum_{k\geqslant1}\sum_{r=1}^k q_{k,r}t^ku^{\underline r}
> $$
>
> Let $G_1,\ldots,G_q$ be the components with edges, and $n_i$ the vertex count of $G_i$. The highest grade is $d=\sum_i(n_i-1)$, and every forest of this grade contains one spanning tree in each $G_i$. Thus
>
> $$
> \widehat Q_G(t,0)=\widehat Q_G(0,u)=1,
> \qquad
> [t^d]\widehat Q_G(t,u)=\gamma u^{\underline q}
> $$
>
> In vector normalization, $\gamma=\prod_i\tau(G_i)$; in vertex normalization, $\gamma=\prod_i n_i\tau(G_i)$. In both cases, $\gamma>0$. For $q\geqslant1$, the leading coefficient has a simple zero at $u=0$:
>
> $$
> u^{\underline q}=u\prod_{j=1}^{q-1}(u-j),
> \qquad
> [u]u^{\underline q}=(-1)^{q-1}(q-1)!\ne0
> $$
>
> If $\widehat Q_G=AB$ with both factors nonconstant, then $\widehat Q_G(0,u)=1$ forces both to have positive degree in $t$. The equality $A(t,0)B(t,0)=1$ forces their leading coefficients in $t$ to be divisible by $u$. The leading coefficient of their product is then divisible by $u^2$, contradicting the simple zero of $\gamma u^{\underline q}$.
>
> Hence $\widehat Q_G$ is irreducible in $\mathbb K[t,u]$, and the table is irreducible in $\mathcal B$ by the lemma. $\square$

**Example: two independent edges.** For the unit-weight graph $2K_2$, the vector table is

$$
\mathcal A_{2K_2}=u_{0,0}+2u_{1,1}+u_{2,2}
$$

Its two representations give

$$
\begin{aligned}
F_{2K_2}(t,u)&=1+2tu+t^2u^2=(1+tu)^2\\
\widehat F_{2K_2}(t,u)&=1+2tu+t^2u(u-1)
\end{aligned}
$$

The first polynomial represents $\circ$ and is reducible. The second represents $*$ and is irreducible; its leading coefficient in $t$, $u(u-1)$, is divisible by $u$ but not by $u^2$. Thus the same table has different reducibility status under the two multiplication rules.

An edgeless graph has the unit table. Isolated vertices change neither the table nor the result. The statement concerns the full table with its unit term; additional triangle-row normalizations are outside its scope.

## What changes after passing to one variable

The substitution $u=1$ groups forests of the same grade with different nontrivial component counts. The condition underlying the two-variable theorem disappears: the leading coefficient $\gamma u$ becomes the number $\gamma$.

For the unit-weight path $P_3$,

$$
\begin{aligned}
F_{P_3}(t,u)&=1+2tu+t^2u\\
P_{P_3}(t,u)&=1+4tu+3t^2u
\end{aligned}
$$

Both polynomials are irreducible. After the substitution,

$$
F_{P_3}(t,1)=(1+t)^2,
\qquad
P_{P_3}(t,1)=(1+t)(1+3t)
$$

Thus, under ordinary multiplication, passing from the full toponome to two variables preserves irreducibility for a connected graph, while further reduction may create new factors.

For the vertex toponome there is a stronger [[Forest Coefficients and the Laplacian Polynomial#Roots and factorization over the reals|spectral result]]. If $c$ is the total number of connected components, including isolated vertices, and $\lambda_1,\ldots,\lambda_{n-c}$ are the nonzero Laplacian eigenvalues, then

$$
P_G(t)=\det(I+t\mathbf L)=\prod_{j=1}^{n-c}(1+\lambda_jt)
$$

All $\lambda_j$ are positive. Thus, for $n-c\geqslant2$, $P_G(t)$ is reducible over $\mathbb R$ and splits completely into linear factors. This need not hold over $\mathbb Q$: for the path with conductances $1,2$, the polynomial $1+6t+6t^2$ has discriminant $12$ and is irreducible over $\mathbb Q$.

Vector normalization does not guarantee reducibility over the reals. For the unit-weight triangle, $F_{K_3}(t)=1+3t+3t^2$ has discriminant $-3$ and is irreducible over $\mathbb R$. Over $\mathbb C$, every one-variable polynomial of degree at least $2$ is reducible. A one-variable statement must therefore specify both the normalization and the coefficient field.

## Comparison of results

Let $G$ have at least one edge, and let $r$ be the number of components with edges. Rows concerning one-variable polynomials assume degree at least $2$.

| Object and product | Result |
| --- | --- |
| Full toponome, ordinary product, both normalizations | Exactly $r$ irreducible factors over $\mathbb R$ and $\mathbb C$, with multiplicities: the toponomes of nontrivial components |
| Two-variable toponome, ordinary product, both normalizations | The same factorization by nontrivial components |
| Full forest toponome, second-kind product, both normalizations | Irreducible over $\mathbb R$ and $\mathbb C$ regardless of connectivity |
| Coefficient table, induced second-kind product, both normalizations | Irreducible over $\mathbb R$ and $\mathbb C$ regardless of connectivity |
| One-variable vertex toponome | Splits into real linear factors; may be irreducible over $\mathbb Q$ |
| One-variable vector toponome | Either case is possible over $\mathbb R$; reducible over $\mathbb C$ |

Factorization of full and two-variable toponomes describes component toponomes but does not solve graph reconstruction. In one variable, even a product representation by toponomes of other graphs does not prove disconnectedness: see the $C_6$ example in [[Forest Coefficients and the Laplacian Polynomial#Factorization does not determine components]].

Irreducibility alone does not guarantee that a formal toponome comes from a graph. The note on [[Graph Realizability of Toponomes#What reducibility conditions provide|graph realizability]] gives a triangle that passes both irreducibility tests but requires an impossible number of adjacent edge pairs.

## Status and independent checks

Irreducibility of full and two-variable toponomes, factorization by components, and irreducibility of the full toponome and coefficient table under $*$ have been proved under the stated assumptions. These conclusions concern the fixed forest representation; they do not remove the [[Toponomes and Structural Identities|representation dependence of reduction for an arbitrary polyform]].

In addition, spanning forests were enumerated directly from the definition for all $1099$ simple labeled graphs on $1\leqslant n\leqslant5$ vertices. For graphs with edges, the unique highest-grade type and the coefficient of the highest free generator were checked; for connected graphs, the hypotheses of the two-variable proof were checked in both normalizations. This checks structural conditions and does not replace the general proof with algorithmic factorization.

The passage to free generators was independently checked for all $29$ positive types of weight at most $6$: sums over distinct indices were compared with power-sum expressions in six variables. Example formulas were obtained by direct forest enumeration.

For the falling-power table representation, the product identity was separately checked for $0\leqslant r,s\leqslant6$, as was the image of every cell product with grades at most $6$. Direct forest enumeration for all $1099$ simple labeled graphs on $1\leqslant n\leqslant5$ vertices confirmed the hypotheses of the new proof in both normalizations; weighted examples were also checked. These computations verify the proof's conditions and the displayed polynomials, rather than replacing the general argument.

## Sources and connections

This note is based on the author's research within PMG. Its toponome statements are derived here from the forest expansion and the two multiplication rules; external sources supply standard algebraic tools.

1. Alistair Savage. [Symmetric Functions](https://alistairsavage.ca/symfunc/notes/Savage-SymmetricFunctions.pdf), §2.6, Theorem 2.6.4: power sums as algebraically independent generators of the symmetric-function algebra over $\mathbb Q$.
2. Mathlib. [Eisenstein polynomials](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Eisenstein/Basic.html): Eisenstein's criterion for a primitive polynomial relative to a prime ideal.
3. [[The Second-Kind Algebra on Partitions]] — type products, one-part multiplication, and the isomorphism with symmetric functions.
4. [[Vector and Vertex Normalizations of Toponomes]] — reduction definitions and products for independent graphs.
5. [[Forest Coefficients and the Laplacian Polynomial]] — the determinant, spectral factorization, and limitations of one-variable conclusions.
6. NIST Digital Library of Mathematical Functions. [§26.1, Alternative Notations](https://dlmf.nist.gov/26.1#E1): the definition of a falling power. Its product identity and application to tables are proved in the text.
