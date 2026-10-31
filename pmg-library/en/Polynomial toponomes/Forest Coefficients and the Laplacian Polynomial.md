---
title: Forest Coefficients and the Laplacian Polynomial
date: 2026-10-23
updated: 2026-10-23
revision: 1
source_revision: 8
status: draft
text_prepared_by: ChatGPT
translation_key: forest-coefficients-and-the-laplacian-polynomial
lang: en
description: "Forest interpretations of the coefficients, principal minors, the identity between exponential reduction and the Laplacian polynomial, roots, connected components, and Abel polynomials."
order: 2
---

There are two routes to a graph polynomial: through the Laplacian exponential in the polyform algebra, and through the characteristic polynomial of its matrix. The [[Vector and Vertex Normalizations of Toponomes|definitions of the two normalizations]] already give the first construction: the forest representation of $\exp L$ is reduced to the partition-type toponome $T_G(\mathbf x)$ and then to one-variable polynomials.

| Through the polyform algebra | Through the Laplacian matrix |
| --- | --- |
| Expand $\exp L$ into partition forms | Write the Laplacian matrix $\mathbf L$ |
| Pass to partition types to obtain $T_G(\mathbf x)$ | Construct $\det(I+t\mathbf L)$ |
| Apply the vertex substitution $x_j=(j+1)t^j$ to obtain $P_G(t)$ | Compute the coefficients as sums of principal minors |

**Main result: the one-variable vertex reduction of the Laplacian exponential gives the same polynomial as the determinant of $I+t\mathbf L$.** Equality of these independently defined constructions requires proof. The result is related to the standard characteristic polynomial by reversing the order of powers and alternating coefficient signs; this passage will be written out after the proof.

The connecting object is a spanning forest. A principal minor of the Laplacian counts forests with prescribed roots, and summing over root sets produces precisely the component-size factors introduced by vertex normalization. This correspondence will prove equality of the polynomials without diagonalizing the Laplacian and identify the graph parameters expressed by their coefficients.

## Coefficients as sums of forest weights

Let $G=(V,E)$ be a finite simple undirected graph on $n\geqslant2$ vertices. Existing edges have positive conductances $c_e$. Connectivity will be specified where needed.

Write $\mathcal F_k(G)$ for the set of spanning forests with $k$ edges. Each forest covers every vertex, including isolated ones, and has $n-k$ components. It need not be maximal. Its weight is

$$
w(F)=\prod_{e\in E(F)}c_e
$$

The empty edge set has weight $1$. If the component vertex sets are $B_1,\ldots,B_{n-k}$, set

$$
h(F)=\prod_{i=1}^{n-k}|B_i|
$$

This is the number of choices of one root vertex in each component; singleton components contribute a factor of $1$.

> [!info] Forest characterization of the coefficients
> The vector and vertex one-variable toponomes are
>
> $$
> F_G(t)=\sum_{k=0}^{n-1}f_kt^k,
> \qquad
> P_G(t)=\sum_{k=0}^{n-1}p_kt^k
> $$
>
> Their coefficients are
>
> $$
> \boxed{
> f_k=\sum_{F\in\mathcal F_k(G)}w(F),
> \qquad
> p_k=\sum_{F\in\mathcal F_k(G)}w(F)h(F)
> }
> \tag{1}
> $$

These formulas follow from the [[Vector and Vertex Normalizations of Toponomes#One-variable toponomes|normalization definitions]]: grouping forests first by type and then by grade is equivalent to summing directly over $\mathcal F_k(G)$. For unit conductances, $f_k$ counts unmarked forests, and $p_k$ counts forests with a chosen root in each component.

The vector sum refers to the fixed [[Laplacian Exponential#Grade components and spanning forests|forest expansion of the exponential]]. Summing the coefficients of an arbitrary equal representation of the polyform may give a different result. For the one-variable vertex evaluation, [[Vector and Vertex Normalizations of Toponomes#Compatibility with structural identities|representation independence]] has already been proved.

## Prescribed roots and a principal minor

> [!info] Prescribed roots and a principal minor
> **Definition.** Let $\varnothing\ne R\subseteq V$ be a prescribed root set. Write $\mathcal F_R(G)$ for the spanning forests in which each component contains exactly one vertex of $R$.

The roots of such a forest are already specified; no additional choices are made in the sum. Its component count is $|R|$, and its edge count is $n-|R|$. In particular, every isolated vertex of such a forest must belong to $R$.

Set $S=V\setminus R$. Write $\mathbf L[S,S]$ for the principal submatrix of the original Laplacian whose rows and columns are indexed by $S$.

> [!info] A principal minor and rooted forests
> **Theorem.** Delete from the Laplacian the rows and columns corresponding to a chosen nonempty set of root vertices. The determinant of the remaining matrix is the total weight of spanning forests in which each component contains exactly one chosen root.
>
> For unit conductances, this principal minor is the number of such forests. In our notation,
>
> $$
> \boxed{
> \det\mathbf L[S,S]=\sum_{F\in\mathcal F_R(G)}w(F),
> \qquad S=V\setminus R
> }
> \tag{2}
> $$
>
> When $R=V$, take $\det\mathbf L[\varnothing,\varnothing]=1$: the right-hand side contains the unique empty edge set, with every vertex a root.

**Remark.** Rows and columns of the matrix are deleted; all graph vertices remain in the forests being counted. The submatrix $\mathbf L[S,S]$ retains the original diagonal entries $d_i$. It is not the Laplacian of the graph obtained by deleting the vertices of $R$ and their incident edges: connections to roots still contribute to the degrees of the remaining vertices.

### Example with a fixed root set

Take the unit-weight cycle $C_4$ with edges $ab,bc,cd,da$. For $R=\{a,c\}$ and $S=\{b,d\}$,

$$
\mathbf L[S,S]=\begin{pmatrix}2&0\\0&2\end{pmatrix},
\qquad \det\mathbf L[S,S]=4
$$

Each nonroot vertex $b,d$ can select either of its two connections to the roots. This gives four admissible forests:

$$
\{ab,ad\},\quad \{ab,cd\},\quad \{bc,ad\},\quad \{bc,cd\}
$$

![Four admissible and two excluded forests of C4 with roots a and c](Prescribed%20Roots%20in%20C4.svg)

*Figure 1. The roots $a,c$ are circled. The four forests on the left have exactly one root in each component and contribute to the minor. The two on the right are excluded: the path $abc$ or $adc$ contains both roots, while the isolated vertex has no root. Solid lines denote selected forest edges; dashed lines denote the remaining edges of the original cycle.*

The induced graph on $\{b,d\}$ has no edges, so its own Laplacian would be zero. Retaining the diagonal entries equal to two in the principal minor is essential.

### Proof using the incidence matrix

Choose an arbitrary orientation for every edge. The incidence matrix $\mathbf B$ consists of the coordinate columns of the edge vectors: the column of $i\to j$ has $-1$ in row $i$, $1$ in row $j$, and zeros elsewhere. Let $\mathbf D_c=\operatorname{diag}(c_e)$. Then

$$
\mathbf L=\mathbf B\mathbf D_c\mathbf B^{\mathsf T}
$$

Orientations only specify the columns; reversing an orientation does not change the Laplacian.

> [!note]- Proof of the theorem
> **Proof.** Set $k=|S|$. By the Cauchy–Binet formula,
>
> $$
> \det\mathbf L[S,S]
> =\sum_{\substack{J\subseteq E\\|J|=k}}
> \det\bigl(\mathbf B[S,J]\bigr)^2\prod_{e\in J}c_e
> $$
>
> Here $\mathbf B[S,J]$ is a square incidence submatrix. We examine when its determinant is nonzero.
>
> If $J$ contains a cycle, the columns of its edges are already linearly dependent in the full incidence matrix. Restricting to selected rows preserves the dependence, so the corresponding determinant is zero.
>
> If $J$ is acyclic, it defines a spanning forest with $n-k=|R|$ components. If a component contains no root, all its vertices lie in $S$. The sum of the corresponding rows of $\mathbf B[S,J]$ is zero, so the determinant again vanishes. Since the numbers of roots and components are equal, a component with two or more roots also forces a component without a root.
>
> The remaining case has exactly one root in each component. After permuting rows and columns, the matrix splits into square blocks, each obtained from a tree incidence matrix by deleting its root row. Such a block has determinant $\pm1$. Indeed, a nontrivial tree has a leaf other than its root; expansion along that row deletes the leaf and its sole incident edge, giving a factor of $\pm1$ inductively. A singleton root gives an empty block with determinant $1$.
>
> Consequently,
>
> $$
> \det\bigl(\mathbf B[S,J]\bigr)^2=
> \begin{cases}
> 1,&(V,J)\in\mathcal F_R(G)\\
> 0,&\text{otherwise}
> \end{cases}
> $$
>
> Substitution into Cauchy–Binet gives (2). The case $S=\varnothing$ agrees with the empty-determinant and empty-product conventions. $\square$

For one root, (2) is Kirchhoff's theorem: the determinant of the reduced Laplacian equals the spanning-tree coefficient. For an arbitrary number of roots, it counts the corresponding forests.

## Summing minors and the Laplacian polynomial

By multilinearity of the determinant, every square matrix $\mathbf L$ satisfies

$$
\det(I+t\mathbf L)
=\sum_{S\subseteq V}t^{|S|}\det\mathbf L[S,S]
\tag{3}
$$

Indeed, in each column we select either the identity-matrix column or the column of $t\mathbf L$. If the latter is selected in positions $S$, expansion along the remaining identity columns leaves exactly the principal minor on $S$, multiplied by $t^{|S|}$.

For the Laplacian, the term $S=V$ vanishes because $\mathbf L\mathbf1=0$. Formula (2) applies to all remaining summands.

> [!info] The matrix-forest theorem
> **Theorem.** Reducing the Laplacian exponential through partition types to a one-variable toponome in vertex normalization gives the same polynomial as computing the determinant of $I+t\mathbf L$:
>
> $$
> \boxed{P_G(t)=\det(I+t\mathbf L)}
> \tag{4}
> $$
>
> In particular, for $0\leqslant k\leqslant n-1$,
>
> $$
> \boxed{
> p_k=\sum_{\substack{S\subseteq V\\|S|=k}}\det\mathbf L[S,S]
> }
> $$

> [!note]- How the component-size factor arises
> **Proof.** Fix a forest $F\in\mathcal F_k(G)$ with components $B_1,\ldots,B_{n-k}$. In the sum of order-$k$ minors, it is counted for every set $R=V\setminus S$ containing exactly one vertex of each component. There are $\prod_i|B_i|=h(F)$ such sets.
>
> In each corresponding minor, the forest has weight $w(F)$. Its total contribution is therefore $w(F)h(F)$. Summing over forests agrees with the definition of $p_k$ in (1), which together with (3) proves (4). $\square$

A spanning forest is thus the common object of the two constructions. In exponential reduction, its weight is multiplied by $h(F)$ by the vertex-normalization rule; in the determinant, the same factor counts the principal minors containing that forest. The results therefore agree coefficient by coefficient.

Formula (4) is the classical matrix-forest theorem. In the PMG exposition, it connects reduction of a polyform exponential to the polynomial of the Laplacian matrix. In particular, $P_G(1)=\det(I+\mathbf L)$ is the total weight of all rooted spanning forests.

The ordinary sum of principal minors gives $p_k$, not $f_k$. Relative to the vector coefficients, it contains an extra multiplicity $h(F)$ depending on the component sizes of each forest.

## Relation to the characteristic polynomial

Call $P_G(t)$ the **Laplacian polynomial** in our ascending-grade notation. The standard characteristic polynomial of the Laplacian matrix is defined differently:

$$
\chi_{\mathbf L}(x)=\det(xI-\mathbf L)
$$

For $x\ne0$, (4) gives

$$
\boxed{
\chi_{\mathbf L}(x)=x^nP_G(-1/x)
=\sum_{k=0}^{n-1}(-1)^kp_kx^{n-k}
}
\tag{5}
$$

The final expression is a polynomial, so equality extends to $x=0$. Passing between the two expressions reverses the order of powers and introduces alternating coefficient signs. The constant term of $P_G$ is $1$, whereas that of $\chi_{\mathbf L}$ is zero.

If $\lambda_1,\ldots,\lambda_{n-c}$ are the positive Laplacian eigenvalues, where $c$ is the number of graph components, then

$$
P_G(t)=\prod_{j=1}^{n-c}(1+t\lambda_j)
$$

Thus $p_k$ is the elementary symmetric function of degree $k$ in these values. This is a spectral interpretation of the forest coefficients already obtained; it was not used to prove (4). The number $n$ is retained separately: together with the degree of $P_G$, it determines the multiplicity of the zero eigenvalue. Hence, for known $n$, the one-variable vertex reduction of the exponential determines the entire Laplacian spectrum with multiplicities.

### Roots and factorization over the reals

> [!info] Roots of the vertex toponome
> **Corollary.** The roots of the one-variable vertex toponome are the negative reciprocals of the nonzero Laplacian eigenvalues, with multiplicities preserved. All roots are real and negative:
>
> $$
> t_j=-\lambda_j^{-1},\qquad j=1,\ldots,n-c
> $$

> [!note]- Proof
> **Proof.** Each factor $1+t\lambda_j$ vanishes at $t=-1/\lambda_j$. For an undirected graph with positive conductances, the nonzero Laplacian eigenvalues are positive. Zero eigenvalues contribute factors of $1$ and produce no roots of the toponome. $\square$

In particular, **the vertex toponome of a connected graph on $n>2$ vertices is reducible over $\mathbb R$ and splits completely into linear factors**. For an arbitrary graph, the condition is $n-c\geqslant2$. One edge together with isolated vertices gives a polynomial of degree $1$, regardless of the total vertex count.

The conclusion about real linear factors concerns vertex normalization over $\mathbb R$. Reducibility over $\mathbb Q$ is not guaranteed; in vector normalization, irreducibility is possible even over $\mathbb R$. Examples showing the roles of the field and normalization appear in the [[Reducibility of Toponomes#What changes after passing to one variable|discussion of one-variable factorization]].

By contrast, the full and two-variable toponomes of a connected graph are irreducible over $\mathbb C$ in both normalizations. [[Reducibility of Toponomes]] compares these statements and explains the role of substituting $u=1$.

If arbitrary positive conductances are allowed and the graph structure is not prescribed, negative real roots together with $P(0)=1$ are also sufficient. The proof and limitations of this conclusion appear in the [[Graph Realizability of Toponomes#A complete criterion for the weighted vertex polynomial|spectral criterion for graph realizability]].

### Factorization does not determine components

By the [[Vector and Vertex Normalizations of Toponomes#Disjoint union and multiplication|disjoint-union lemma]], independent graphs correspond to products of toponomes. The converse fails for a one-variable polynomial: writing it as a product of toponomes does not imply that the original graph is disconnected.

For the unit-weight cycle $C_6$, triangle $K_3$, and star $K_{1,3}$, direct determinant computation gives

$$
\begin{aligned}
P_{C_6}(t)&=(1+t)^2(1+3t)^2(1+4t)\\
P_{K_3}(t)&=(1+3t)^2\\
P_{K_{1,3}}(t)&=(1+t)^2(1+4t)
\end{aligned}
$$

Consequently,

$$
\boxed{P_{C_6}(t)=P_{K_3}(t)P_{K_{1,3}}(t)}
$$

Expansion gives $1+12t+54t^2+112t^3+105t^4+36t^5$. The left side represents a connected graph on six vertices; the right side is the toponome of a union on seven vertices. Their nonzero Laplacian spectra agree, but their zero multiplicities differ. Comparisons therefore retain the data $(n,P_G)$.

If we additionally require $n_G=n_H+n_K$ for two graphs with nonempty vertex sets, equality $P_G=P_HP_K$ is impossible for connected $G$: the degree on the left is $n_G-1$, while the degree on the right is at most $n_G-2$. This is a restriction on graph sizes, not a statement of algebraic irreducibility.

## The first coefficients

Write $C$ for the total conductance and $d_i$ for the weighted vertex degrees:

$$
C=\sum_{e\in E}c_e,
\qquad d_i=\sum_jc_{ij},
\qquad \sum_i d_i=2C
$$

### The empty forest and one connection

The empty forest is unique. All its components are singletons, so

$$
f_0=p_0=1
$$

Each edge gives a one-edge forest whose sole nontrivial component has size $2$. Hence

$$
\boxed{f_1=C,\qquad p_1=2C=\operatorname{tr}\mathbf L}
$$

### Sum of roots and sum of vertex degrees

> [!info] Sum of roots and sum of vertex degrees
> **Corollary.** The sum of the roots of the Laplacian characteristic polynomial, with multiplicities, equals the sum of weighted vertex degrees, or twice the total edge conductance:
>
> $$
> \sum_{j=1}^{n-c}\lambda_j
> =\operatorname{tr}\mathbf L
> =\sum_i d_i=2C=p_1
> $$
>
> This follows because the sum of eigenvalues equals the matrix trace. Zero eigenvalues do not change the sum. For unit conductances, it equals $2|E|$.
>
> For the roots $t_j=-1/\lambda_j$ of our toponome, the same statement becomes
>
> $$
> -\sum_{j=1}^{n-c}\frac1{t_j}=p_1
> $$
>
> The sum of the roots of $P_G$ themselves is determined by the opposite end of the coefficient list: for a connected graph it is $-p_{n-2}/p_{n-1}$. Its [[Coefficients and Kirchhoff Indices#Root sums and the two ends of the coefficient list|relation to the Kirchhoff index]] is considered separately. Thus “the sum of the roots of the Laplacian polynomial” requires specifying which polynomial convention is intended.

### Two connections

In a simple graph, any two distinct edges form a forest. Therefore

$$
\boxed{
f_2=\sum_{\{e,f\}\subseteq E}c_ec_f
=\frac12\left(C^2-\sum_{e\in E}c_e^2\right)
}
$$

The edge pair is unordered. For the vertex coefficient, their relative position matters:

| Edge pair | Nontrivial components | Root factor |
| --- | --- | ---: |
| One shared vertex | One three-vertex tree | $3$ |
| No shared vertices | Two two-vertex components | $4$ |

Let $A$ be the sum of conductance products over unordered pairs of adjacent edges. Each such pair has exactly one common vertex, so

$$
A=\frac12\sum_i\left(d_i^2-\sum_{e\ni i}c_e^2\right)
=\frac12\sum_i d_i^2-\sum_e c_e^2
$$

If every pair is initially assigned a factor of $4$, one copy of the weight must be subtracted for each adjacent pair. This gives

$$
\boxed{
p_2=4f_2-A
=\frac12\left(4C^2-\sum_i d_i^2-2\sum_e c_e^2\right)
}
\tag{6}
$$

The same formula follows independently from the sum of order-two principal minors:

$$
p_2=\sum_{i<j}(d_id_j-c_{ij}^2)
=\frac12\left((\operatorname{tr}\mathbf L)^2-\operatorname{tr}(\mathbf L^2)\right)
$$

The last expression uses matrix multiplication. Here $\operatorname{tr}(\mathbf L^2)=\sum_i d_i^2+2\sum_e c_e^2$.

For unit conductances, $C=|E|$ and $\sum_e c_e^2=|E|$. Thus $f_2=\binom{|E|}{2}$ is determined by the edge count, whereas $p_2$ also depends on the sum of squared vertex degrees. For $n=2$, take $f_2,p_2$ to be zero; the formulas give the same result.

## The highest coefficients of a connected graph

Throughout this section, $G$ is connected.

### Spanning trees

A forest with $n-1$ edges has one component and is therefore a spanning tree. Its root can be chosen in $n$ ways. Hence

$$
\boxed{f_{n-1}=\tau(G),\qquad p_{n-1}=n\tau(G)}
$$

Here $\tau(G)$ is the [[Laplacian Exponential#The spanning-tree form and top-grade coefficient|spanning-tree coefficient]], the sum of spanning-tree weights. For unit conductances, it is the number of spanning trees.

Vertex normalization also has a determinant explanation: there are $n$ principal minors of order $n-1$, each equal to $\tau(G)$ by Kirchhoff's theorem.

### Spanning 2-forests

Let $\mathcal F_2^{\mathrm{comp}}(G)$ denote the spanning forests with exactly two components. The superscript distinguishes component count from the index $k$ in $\mathcal F_k(G)$, which counts edges in this note. Every 2-forest has $n-2$ edges.

If its component vertex sets are $A_F,B_F$, then

$$
\boxed{
f_{n-2}=\sum_{F\in\mathcal F_2^{\mathrm{comp}}(G)}w(F),
\qquad
p_{n-2}=\sum_{F\in\mathcal F_2^{\mathrm{comp}}(G)}|A_F|\,|B_F|\,w(F)
}
\tag{7}
$$

The factor $|A_F|\,|B_F|$ has two equivalent meanings: the number of root choices in the two components, and the number of unordered vertex pairs separated by those components. The components themselves are unordered; there is no additional factor of $2$.

Let $\tau_{ij}^{(2)}$ be the total weight of spanning 2-forests separating vertices $i,j$. Interchanging the two finite sums in (7) gives

$$
\boxed{p_{n-2}=\sum_{i<j}\tau_{ij}^{(2)}}
$$

This formula relates a polynomial coefficient to pairwise vertex characteristics. Its resistance interpretation and the passage to the Kirchhoff index appear in the [[Coefficients and Kirchhoff Indices#The Kirchhoff index from the two highest coefficients|theorem on the ratio of the two highest coefficients]].

## Disconnected graphs and polynomial degrees

Let the components of the original graph be $G_1,\ldots,G_c$, of sizes $n_1,\ldots,n_c$. For a singleton vertex, set $\tau(G_i)=1$.

A forest has at most $n-c$ edges. Equality holds when a spanning tree is chosen within each component $G_i$. Positive conductances prevent cancellation of these contributions. Therefore

$$
\boxed{\deg F_G=\deg P_G=n-c}
$$

The leading coefficients are

$$
f_{n-c}=\prod_{i=1}^c\tau(G_i),
\qquad
p_{n-c}=\prod_{i=1}^c n_i\tau(G_i)
$$

For $c>1$, the coefficients of $t^{n-1}$ vanish. The highest nonzero coefficient concerns a forest with $c$ components, rather than a spanning tree of the entire graph. For an edgeless graph, both polynomials are $1$ and have degree $0$.

These equalities agree with the [[Laplacian Exponential#Disconnected graphs|highest nonzero grade of the exponential]]. Adding an isolated vertex increases both $n$ and $c$ by one and leaves the polynomials unchanged.

### The zero root and the number of components

> [!info] Component count from degree and roots
> **Corollary.** For known vertex count, the number of graph components is $n$ minus the degree of the toponome. In the characteristic polynomial, the same number is the multiplicity of the zero root:
>
> $$
> c=n-\deg P_G=\operatorname{ord}_{x=0}\chi_{\mathbf L}(x)
> $$

> [!note]- Proof
> **Proof.** The combinatorial count of the maximum grade above gives $\deg P_G=n-c$. Thus the lowest nonzero power of $x$ in (5) is $c$. $\square$

For $n\geqslant1$, zero has multiplicity $c-1$ in $\chi_{\mathbf L}(x)/x$. If the graph is connected, this polynomial has no zero root. In words, the number of components is one more than the multiplicity of zero after removing one obligatory factor of $x$. The toponome $P_G$ itself has no zero root, since $P_G(0)=1$.

These statements concern undirected graphs with positive conductances. Extending component statements to directed graphs requires separate definitions and results.

## Complete graphs and Abel polynomials

Reversing the direction of powers has a combinatorial meaning for any graph. A forest with $k$ edges has $m=n-k$ components, including singleton vertices. Thus the polynomial extension of $x^nP_G(1/x)$ is

$$
\boxed{
x^nP_G(1/x)=\det(xI+\mathbf L)
=\sum_{m=1}^{n}p_{n-m}x^m
}
$$

> [!info] Complete graphs and Abel polynomials
> **Proposition.** The coefficient of $x^m$ in this expression is the total weight of rooted spanning forests with $m$ components. For unit conductances, it counts such forests on the given set of labeled vertices. Each component has a chosen root; the components are unordered.

> [!note]- Proof
> **Proof.** The substitution sends $p_kt^k$ to $p_kx^{n-k}$. The forests and their root weights remain unchanged, but the exponent now counts components instead of edges. Equality with the determinant follows from (4) for $x\ne0$ and extends polynomially to $x=0$. $\square$

For the complete graph $K_n$ with unit conductances, $\mathbf L=nI-\mathbf1\mathbf1^{\mathsf T}$. This matrix vanishes on $\mathbf1$ and acts as multiplication by $n$ on $\mathbf1^\perp$. Consequently, for $n\geqslant1$,

$$
P_{K_n}(t)=(1+nt)^{n-1},
\qquad
\boxed{A_n(x)=x^nP_{K_n}(1/x)=x(x+n)^{n-1}}
$$

This is the [[Forest Coefficients and Abel Polynomials#The expansion of Abel polynomials|Abel polynomial in our normalization]]. It therefore records the same vertex coefficients of the complete graph, indexed instead by forest component count.

> [!info] Ordinary coefficients of an Abel polynomial
> **Theorem.** The coefficient of $x^m$ in $A_n(x)$ is the number of labeled rooted forests of $m$ trees on the given $n$ vertices:
>
> $$
> [x^m]A_n(x)=p_{n-m}(K_n)
> =\binom{n-1}{m-1}n^{n-m},\qquad 1\leqslant m\leqslant n
> $$

> [!note]- Proof
> **Proof.** Every forest on the given vertices is a subgraph of $K_n$, so the preceding proposition counts all of them. Expanding $x(x+n)^{n-1}$ gives the explicit formula. $\square$

For example,

$$
\begin{aligned}
P_{K_3}(t)&=1+6t+9t^2\\
A_3(x)&=x^3+6x^2+9x\\
P_{K_4}(t)&=1+12t+48t^2+64t^3\\
A_4(x)&=x^4+12x^3+48x^2+64x
\end{aligned}
$$

The numbers $[1,6,9]$ correspond to ascending powers of $t$ in $P_{K_3}$ and descending nonzero powers of $x$ in $A_3$. Their meanings are:

| Components $m$ | Edges $k$ | Forests without root choices | Root choices per forest | Coefficient |
| ---: | ---: | ---: | ---: | ---: |
| $3$ | $0$ | $1$ | $1$ | $1$ |
| $2$ | $1$ | $3$ | $2$ | $6$ |
| $1$ | $2$ | $3$ | $3$ | $9$ |

The zero root of $A_n$ is simple; the remaining $n-1$ roots equal $-n$. By comparison, the roots of $P_{K_n}$ equal $-1/n$, while the nonzero roots of $\chi_{\mathbf L}(x)=x(x-n)^{n-1}$ equal $n$. In general, $\det(xI+\mathbf L)=(-1)^n\chi_{\mathbf L}(-x)$, so the sum of the roots of this expression must not be identified with the positive sum of vertex degrees.

The expansion of $A_n$ in falling factorials and the corresponding forest coefficients $\operatorname{St}(n,m)$ are discussed in [[Forest Coefficients and Abel Polynomials]]. They differ from the ordinary coefficients $[x^m]A_n$: there, a forest additionally carries a grouping of its components.

## A complete example: the cycle on four vertices

Consider $C_4$ with edges $ab,bc,cd,da$ and unit conductances. Every edge subset except the full cycle is a forest.

![All groups of spanning forests of C4 and their contributions in both normalizations](Forest%20Coefficients%20of%20C4.svg)

*Figure 2. Fifteen of the sixteen edge sets are forests. Among two-edge sets, four adjacent pairs have root weight $3$, and two disjoint pairs have root weight $4$. Solid lines denote forest edges; dashed lines retain the positions of the remaining connections of the original cycle. The right columns show each group's total contributions to $f_k$ and $p_k$.*

| Edges $k$ | Forest form | Number of forests | Root weight per forest | Contribution to $f_k$ | Contribution to $p_k$ |
| ---: | --- | ---: | ---: | ---: | ---: |
| $0$ | Four singleton vertices | $1$ | $1$ | $1$ | $1$ |
| $1$ | One edge and two singleton vertices | $4$ | $2$ | $4$ | $8$ |
| $2$ | Two adjacent edges and a singleton vertex | $4$ | $3$ | $4$ | $12$ |
| $2$ | Two disjoint edges | $2$ | $4$ | $2$ | $8$ |
| $3$ | A spanning tree | $4$ | $4$ | $4$ | $16$ |

These forest groups give the partition toponome

$$
T_{C_4}(\mathbf x)=1+4x_1+(4x_2+2x_1^2)+4x_3
$$

In grade $2$, the four adjacent pairs have type $(2)$ and the two disjoint pairs have type $(1^2)$. The vector substitution $x_j=t^j$ gives

$$
\boxed{F_{C_4}(t)=1+4t+6t^2+4t^3}
$$

The vertex substitution $x_j=(j+1)t^j$ gives

$$
\boxed{P_{C_4}(t)=1+8t+20t^2+16t^3}
$$

In particular, $p_2=4\cdot3+2\cdot4=20$. Formula (6) independently computes it from degrees: $C=4$, $d_a=d_b=d_c=d_d=2$, and $\sum_e c_e^2=4$, so

$$
p_2=\frac12(64-16-8)=20
$$

All four three-edge forests are spanning trees, so $\tau(C_4)=4$ and $p_3=4\tau=16$.

### Checking the determinant

In vertex order $a,b,c,d$,

$$
I+t\mathbf L=
\begin{pmatrix}
1+2t&-t&0&-t\\
-t&1+2t&-t&0\\
0&-t&1+2t&-t\\
-t&0&-t&1+2t
\end{pmatrix}
$$

Direct determinant computation gives

$$
\begin{aligned}
\det(I+t\mathbf L)
&=(1+2t)^2\bigl((1+2t)^2-4t^2\bigr)\\
&=(1+2t)^2(1+4t)\\
&=1+8t+20t^2+16t^3
\end{aligned}
$$

This agrees with the polynomial obtained from the exponential through the partition toponome and the vertex substitution. By (5), the characteristic polynomial is

$$
\chi_{\mathbf L}(x)=x^4-8x^3+20x^2-16x
$$

The full four-edge set contains a cycle and gives the zero form in the [[Laplacian Exponential|Laplacian exponential]]. The forest polynomials have no degree-$4$ term; in the determinant it is $t^4\det\mathbf L=0$.

### A short weighted check

For a triangle with conductances $a,b,c>0$, every two-edge set is a spanning tree. Set $C=a+b+c$ and $\tau=ab+ac+bc$. Then

$$
F_G(t)=1+Ct+\tau t^2,
\qquad
P_G(t)=1+2Ct+3\tau t^2
$$

For $a=1$, $b=2$, and $c=3$,

$$
F_G(t)=1+6t+11t^2,
\qquad
P_G(t)=1+12t+33t^2
$$

Here $\tau=11$ is the sum of the weights of three spanning trees, not their number. This distinction applies to all coefficients of a weighted graph.

## Results and continuation

We have proved that two constructions coincide: reduction of the Laplacian exponential through partition types in vertex normalization, and the determinant of $I+t\mathbf L$. Formula (5) converts its coefficients into those of the standard characteristic polynomial of the Laplacian matrix.

The general formula (1) characterizes both normalizations through forests, while the principal-minor theorem (2) explains why the matrix polynomial corresponds specifically to vertex normalization. The first coefficients express total conductance and the distribution of vertex degrees; the highest coefficients express the spanning-tree coefficient and two-forest sums. Roots relate the polynomial to the nonzero Laplacian spectrum; its degree together with $n$ determines the component count. Indexing by component count gives the Abel polynomial for the complete graph.

> [!example]- Independent computational checks
> All edge sets of the unit-weight $C_4$ and the triangle with conductances $1,2,3$ were enumerated. Cyclic sets were excluded, and rooted coefficients were checked separately by enumerating vertex subsets with one root in each component. The resulting polynomials were compared with determinants expanded by permutations and with sums of principal minors. Formula (2) was also checked for every nonempty root set.
>
> Determinants were additionally expanded for $C_6$, $K_3$, $K_{1,3}$, and the path with conductances $1,2$. The identity $P_{C_6}=P_{K_3}P_{K_{1,3}}$ was checked. For $K_3,K_4$, coefficients were obtained independently by enumerating forests and root weights.
>
> The disconnected case was checked on two disjoint edges of conductances $2,3$ and one isolated vertex: $F_G(t)=1+5t+6t^2$, $P_G(t)=1+10t+24t^2$, $n=5$, $c=3$. The degree is $n-c=2$, and the leading coefficients are $6$ and $24$.

[[Coefficients and Kirchhoff Indices]] converts two-forest sums into resistances and derives $Kf(G)=n\,p_{n-2}/p_{n-1}$. Other coefficient ratios are interpreted through the reciprocal spectrum; the relation to the centroid and circumsphere is treated separately.

## Sources

- [[Vector and Vertex Normalizations of Toponomes]] — definitions of the two normalizations and the role of root weight.
- [[Laplacian Exponential]] — the forest expansion, spanning-tree coefficient, and highest grade of a disconnected graph.
- P. Chebotarev, E. Shamis. [Matrix-Forest Theorems](https://arxiv.org/abs/math/0602575), version v2, 2023: Theorem 5 on the total weight of rooted forests and Appendix Lemma 3 on principal minors. The polynomial version follows by scaling all conductances by $t$; a coefficientwise proof is given above.

- [[Forest Coefficients and Abel Polynomials]] — ordinary Abel coefficients, falling factorials, and the different objects counted.
- A. K. Kelmans. [On the Number of Trees of a Graph. I](https://www.mathnet.ru/at11531). Avtomatika i Telemekhanika, 26:12 (1965), 2194–2204 (in Russian).
- A. K. Kelmans. [On the Number of Trees of a Graph. II](https://www.mathnet.ru/at11014). Avtomatika i Telemekhanika, no. 2 (1966), 56–65 (in Russian). Both papers are classical studies of tree counts and related graph functions.
- R. P. Agaev, P. Yu. Chebotarev. [Laplacian Spectra of Digraphs and Their Applications](https://www.ipu.ru/node/1225). Avtomatika i Telemekhanika, no. 5 (2005), 47–62 (Russian edition). Historical and spectral context; the results of this note are stated for undirected graphs.
- K. Ch. Das. [The Laplacian Spectrum of a Graph](https://doi.org/10.1016/j.camwa.2004.05.005). Computers & Mathematics with Applications, 48 (2004), 715–724. Relations between spectra and graph parameters; the equality between the eigenvalue sum and the trace used here is proved directly.
- A. D. Sokal. [Total positivity of some polynomial matrices that enumerate labeled trees and forests, I. Forests of rooted labeled trees](https://arxiv.org/abs/2105.05583), formula (1.1). Classical enumeration of rooted forests by component count.

The forest characterization of the Laplacian polynomial is classical. In PMG, it is related to reduction of the polyform exponential and the two normalizations of its coefficients.
