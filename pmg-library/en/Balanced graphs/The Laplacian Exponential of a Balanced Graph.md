---
title: The Laplacian Exponential of a Balanced Graph
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: balanced-graph-laplacian-exponential
lang: en
description: 'The finite exterior exponential of a balanced Laplacian: bilinear factors, minors, directed forests, reference-point weights, and connections to double-form theory.'
order: 3
source_revision: 5
---

The representations in [[The Bilinear Laplacian of a Balanced Graph]] construct the Laplacian exponential in the same boundary-form algebra used for undirected graphs. Each individual bilinear term has square zero, so the exponential becomes a finite product of linear factors. Symmetry of the Laplacian is unnecessary.

Different representations yield one polyform while distributing it differently among terms. Arc expansions display directed forests; vertex expansions reduce the factor count. In a basis of pairs of boundaries, coefficients are minors of the reduced Laplacian, and the highest possible grade is determined by the common spanning-tree coefficient.

## Conventions and the finite exponential

Let $G$ be a loopless balanced graph on formal basis vertices $a_1,\ldots,a_n$, with $n\ge2$. Arc $i\to j$ has weight $f_{ij}\ge0$, and $f_{ii}=0$. The set $E(G)$ contains only positive-weight arcs. Use the outgoing Laplacian:

$$
L_{ii}=\sum_j f_{ij},\qquad L_{ij}=-f_{ij}\quad(i\ne j),\qquad
\mathbf L\mathbf1=0,\qquad \mathbf1^{\mathsf T}\mathbf L=0
$$

The matrix is $\mathbf L$, its entries $L_{ij}$, and the polyform $L$. The affine-vector space $W=\ker\varepsilon$ has dimension $n-1$. Both arguments of every Laplacian term under consideration belong to $W$.

Multiplication is $[X,Y][U,V]=[XU,YV]$. It is commutative because the two exterior signs cancel when factors are exchanged. The unit form is $e=[1,1]$.

> [!info] Laplacian exponential
> **Definition.** The exponential of the Laplacian polyform of a balanced graph is
>
> $$
> \boxed{M=\exp L=\sum_{k=0}^{n-1}\frac{L^k}{k!}},\qquad L^0=e
> \tag{1}
> $$
>
> Its grade components are $M_k=L^k/k!$.

The arguments in a product of $n$ grade-one forms would lie in $\Lambda^nW=0$, so $L^n=0$. Equation (1) is an exact finite expression, requiring no convergence argument.

This exponential uses the polyform product. The matrix exponential $\exp\mathbf L$, computed with ordinary matrix multiplication, is different. For example, $L^2$ has grade $2$, whereas $\mathbf L^2$ remains a matrix of the same size.

## Why these are called double forms

In exterior-algebra terminology, “double” refers to two exterior factors. Our notation corresponds to the tensor

$$
[X,Y]\ \longleftrightarrow\ X\otimes Y,\qquad
X,Y\in\Lambda^kW
$$

Each factor has its own grade. General double-form theory allows different grades, using $\Lambda^pW\otimes\Lambda^qW$. PMG uses the equal-grade subalgebra, called diagonal in the literature [1, §1.1; 2, Definition 2.1]:

$$
\bigoplus_{k=0}^{n-1}\Lambda^kW\otimes\Lambda^kW
$$

| PMG notation | Two exterior factors | Bigrade |
| --- | --- | --- |
| $[u,v]$ | $u\otimes v$ | $(1,1)$ |
| $[(abc),(abd)]$ | $(abc)\otimes(abd)$ | $(2,2)$ |
| $[u]^2=[u,u]$ | $u\otimes u$ | $(1,1)$ |

PMG grade $k$ thus corresponds to bigrade $(k,k)$. A quadratic form is also double, with equal factors. “Double” does not mean grade two, and “diagonal” here means equal grades, without requiring $X=Y$.

Multiplication acts separately in the two factors:

$$
(X\otimes Y)(U\otimes V)=(XU)\otimes(YV)
$$

This is exactly $[X,Y][U,V]=[XU,YV]$.

**Terminology.** In [2, §2], elements of $\Lambda^pW\otimes\Lambda^qW$ are called double exterior vectors; double exterior forms use $W^*$ instead. Precisely, our formal forms can be viewed as double forms on the dual space $W^*$. This correspondence needs no metric. The PMG term “form” retains the definition in [[Basic Objects and Operations of Polyform Algebra]].

### The exterior exponential in the literature

Belkhirat and Labbi [2, §5, Proposition 5.1] explicitly consider the exponential of a bilinear double form with this exterior product, without assuming symmetry. After an auxiliary metric is chosen, the exponential represents the extension of the corresponding linear operator to the exterior algebra. Equation (1) applies this general exterior-exponential construction to a Laplacian in $W\otimes W$.

## Factorization by bilinear terms

For $u,v\in W$, the form $H=[u,v]$ satisfies $H^2=[u\wedge u,v\wedge v]=0$, hence $\exp H=e+H$.

> [!info] A product of linear factors
> **Theorem.** If $L=\sum_{\alpha=1}^m H_\alpha$, where $H_\alpha=[u_\alpha,v_\alpha]$ and $u_\alpha,v_\alpha\in W$, then
>
> $$
> \boxed{M=\prod_{\alpha=1}^m(e+H_\alpha)}
> \tag{2}
> $$
>
> For each $k$,
>
> $$
> M_k=\sum_{\alpha_1<\cdots<\alpha_k}
> [u_{\alpha_1}\cdots u_{\alpha_k},v_{\alpha_1}\cdots v_{\alpha_k}]
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** In the expansion of $L^k$, repeated indices give zero because $H_\alpha^2=0$. Each set of $k$ distinct indices occurs in $k!$ orders. Commutativity makes these products equal, and $k!$ cancels the denominator in $M_k$. This gives (3); summing over $k$ gives (2). $\square$

A term of (3) is nonzero exactly when each of its two vector collections is linearly independent. Vanishing can therefore be checked separately in the two arguments. All results remain bilinear forms on boundaries of the appropriate grade.

### Grouping by vertices

For any point $h$ of affine weight $1$, set

$$
v_i=\sum_j f_{ij}(a_i-a_j)=\sum_j L_{ij}a_j,\qquad
H_i=[a_i-h,v_i]
$$

The representation $L=\sum_i H_i$ was proved in [[The Bilinear Laplacian of a Balanced Graph#Grouping by vertices|the bilinear Laplacian note]]. It gives

$$
M=\prod_{i=1}^n(e+[a_i-h,v_i])
$$

Choosing $h=a_r$ makes factor $r$ equal to $e$, so

$$
\boxed{M=\prod_{i\ne r}(e+[a_i-a_r,v_i])}
\tag{4}
$$

There are at most $n-1$ nontrivial factors, regardless of the arc count or cycle decomposition. For a connected balanced graph, $\operatorname{rank}\mathbf L=n-1$, so fewer grade-one bilinear terms cannot represent $L$.

Equation (4) reduces the factor count, but its full expansion can still be large. To compute one grade, choose only subsets of the required size; to obtain the top coefficient, a determinant is often preferable. The number of cycles alone does not determine computational effort: unlike a single $[u,v]$, the Laplacian of a whole cycle generally has a nonzero square.

## Grade components and minors

Choose reference vertex $a_n$ and basis $b_i=a_i-a_n$, $1\le i\le d=n-1$, of $W$. Then

$$
L=\sum_{i,j=1}^d C_{ij}[b_i,b_j],\qquad
\mathbf C=\mathbf L_{\widehat n,\widehat n}
$$

The matrix $\mathbf C$ deletes row and column $n$. For increasing indices $I=(i_1<\cdots<i_k)$, write $b_I=b_{i_1}\cdots b_{i_k}$; set $b_\varnothing=1$. The arguments are boundaries: $b_I=(a_n a_{i_1}\ldots a_{i_k})$. The two arguments may use different index sets.

> [!info] Coefficients of the exponential
> **Theorem.** For an arbitrary matrix $\mathbf C$, without assuming symmetry,
>
> $$
> \boxed{M_k=\sum_{\substack{I,J\subseteq\{1,\ldots,d\}\\|I|=|J|=k}}
> \det\mathbf C_{I,J}\,[b_I,b_J]}
> \tag{5}
> $$
>
> Indices within $I,J$ are increasing; the determinant of the empty matrix is $1$.

> [!note]- Proof of the minor formula
> **Proof.** Expand $L^k/k!$. A repeated left or right basis vector kills the term. Fix index sets $I,J$. Ordering the left argument by $I$ leaves all bijections from its indices to those of $J$. Permutation signs in the right argument produce $\det\mathbf C_{I,J}$. Each choice occurs in $k!$ factor orders, cancelling the denominator. $\square$

Equation (5) is the coordinate form of the known identity that the $k$th exterior power of a bilinear form, divided by $k!$, has order-$k$ minors as coefficients [1, §2.1, equation (16)]. The proof states this identity in PMG notation.

The forms $[b_I,b_J]$ form a basis in grade $k$, so these coefficients are unique. Principal minors multiply quadratic forms $[b_I]^2$; other minors multiply forms with different arguments. For a nonsymmetric Laplacian, the coefficients of $[b_I,b_J]$ and $[b_J,b_I]$ need not agree.

> [!info] Grade components and minors
> **Corollary.** The highest nonzero grade of the exponential equals $\operatorname{rank}\mathbf L$. Formula (5) is nonzero up to the largest order of a nonzero minor of $\mathbf C$, and the boundary representation gives equal ranks for $\mathbf C$ and $\mathbf L$. If there are $c$ weakly connected components, including isolated vertices, nonnegative weights give
>
> $$
> \deg M=\operatorname{rank}\mathbf L=n-c
> $$
>
> Each nontrivial component is strongly connected, as established in [[Balanced Graphs and Spanning-Tree Potentials]]. For an empty graph, $M=e$ and $\deg M=0$.

## Expansion over directed forests

To retain individual arcs, use

$$
L=\sum_{i\ne j}E_{ij}(h),\qquad
E_{ij}(h)=f_{ij}[a_i-h,a_i-a_j]
$$

This holds for a balanced graph and any unit-weight point $h$. An individual $E_{ij}(h)$ depends on $h$ and is not the Laplacian of the original arc alone. Their full sum nevertheless equals $L$, and

$$
M=\prod_{i\to j\in E(G)}(e+E_{ij}(h))
$$

> [!info] Expansion over directed forests
> **Definition.** A directed spanning forest toward roots includes all vertices; each component is a tree directed toward its root. Every nonroot vertex has one outgoing arc, and each root has none. An isolated vertex is its component's root.

For a forest $F$ with $k$ arcs, choose a common arc order and set

$$
w(F)=\prod_{i\to j\in F}f_{ij},\qquad
A_F(h)=\prod_{i\to j\in F}(a_i-h),\qquad
B_F=\prod_{i\to j\in F}(a_i-a_j)
$$

The same order is used in both exterior products. Changing it preserves $[A_F(h),B_F]$, since the two signs cancel. For the empty forest, $w(F)=1$ and $A_F(h)=B_F=1$.

> [!info] Forest expansion
> **Theorem.** Let $\mathcal F_k$ be all directed spanning forests toward roots with $k$ arcs. Then
>
> $$
> \boxed{M_k=\sum_{F\in\mathcal F_k}w(F)[A_F(h),B_F]}
> \tag{6}
> $$
>
> The formula holds for every unit-weight point $h$. Some choices of $h$ may make individual forest terms zero.

> [!note]- Proof
> **Proof.** Expand the arc product. Selecting two arcs from one vertex repeats $a_i-h$ in the left argument, giving zero. Selecting a directed cycle makes its right-argument vectors $a_i-a_j$ sum to zero, also killing the term.
>
> In a finite acyclic directed graph with outdegree at most $1$, each path ends at a vertex with no outgoing arc. A weakly connected component has a unique such root: both ends of each arc have the same terminal root. Each component is therefore a tree toward that root. The remaining arc sets are exactly $\mathcal F_k$, with the stated terms. $\square$

The right argument $B_F$ is, up to sign, the product of the component boundaries. The left argument depends on the selected sources and $h$. In general they differ, so a forest contributes a bilinear form rather than a quadratic one.

Minors and directed forests also appear in Abdesselam's Grassmann approach [3, §§2-3]. It uses $\exp(-\sum_{i,j}\bar\psi_i A_{ij}\psi_j)$ with two families of anticommuting variables; Berezin integration extracts determinant and minor coefficients. The matrix $\mathbf A$ need not be symmetric. That source uses column sums and trees directed away from roots; comparison with our convention requires transposition and reversal of arcs. The centered expansion (6) for arbitrary $h$ follows from the proof above.

### The centroid and a reference vertex

For $h=(a_1+\cdots+a_n)/n$, any collection of at most $n-1$ distinct vectors $a_i-h$ is independent. Indeed, in $\sum_{i\in I}t_i(a_i-h)=0$, the coefficient of an omitted vertex is $-\sum_{i\in I}t_i/n$. It forces the coefficient sum to vanish, and then every $t_i=0$. Each forest in $\mathcal F_k$ therefore gives a nonzero term in (6).

For $h=a_r$, exactly the terms containing an outgoing arc from $a_r$ vanish. The remaining sources give distinct members of the basis $a_i-a_r$, so their terms are nonzero. Thus only forests having $a_r$ as one of their roots remain.

These are two expansions of the same polyform. The centroid retains every root choice, while a reference vertex removes some terms and changes the forms of the others. Neither the number of terms nor the sum of their weights is invariant under arbitrary rewritings of $M_k$.

## The spanning-tree form and common coefficient

The space $\Lambda^{n-1}W$ is one-dimensional. Fix the spanning-tree form

$$
T_n=[(a_1\ldots a_n)]^2
$$

The product $b_1\cdots b_{n-1}$ differs from $(a_1\ldots a_n)$ only by a sign, which disappears in its quadratic form. Equation (5) gives

$$
M_{n-1}=\det\mathbf L_{\widehat n,\widehat n}\,T_n
$$

All order-$(n-1)$ principal minors of a balanced Laplacian agree. Calling their common value $\tau$ gives

$$
\boxed{M_{n-1}=\tau T_n,\qquad L^{n-1}=(n-1)!\,\tau T_n}
\tag{7}
$$

Connectedness and nonnegative weights imply $\tau>0$. By the directed matrix-tree theorem, it is the sum of weights of spanning trees toward any one fixed vertex. The proof and direction convention appear in [[Balanced Graphs and Spanning-Tree Potentials#The spanning-tree potential of a vertex|the spanning-tree potential note]].

### A tree's contribution for an arbitrary reference point

Express the point as an affine combination:

$$
h=\sum_{i=1}^n\alpha_i a_i,\qquad \sum_i\alpha_i=1
$$

The coefficients $\alpha_i$ may be negative.

> [!info] Root weight in the top grade
> **Lemma.** For a spanning tree $T$ directed toward $a_r$,
>
> $$
> \boxed{[A_T(h),B_T]=\alpha_r T_n}
> \tag{8}
> $$
>
> Its contribution to the forest expansion is therefore $\alpha_r w(T)T_n$.

> [!note]- Proof
> **Proof.** Order the nonroot vertices, put $u_i=a_i-a_r$, and denote their exterior product by $U$. Each $i\ne r$ has an arc $i\to p(i)$ to its parent. Its right-argument vector is $u_i-u_{p(i)}$, with $u_r=0$.
>
> Placing parents after descendants makes the change from $u_i$ to $u_i-u_{p(i)}$ triangular with unit diagonal. Any common reordering still has determinant $1$, so $B_T=U$.
>
> Now $h-a_r=\sum_{i\ne r}\alpha_i u_i$ and $a_i-h=u_i-(h-a_r)$. The change-of-basis matrix is $\mathbf I-\boldsymbol\alpha\mathbf1^{\mathsf T}$, where $\boldsymbol\alpha$ lists the coefficients with $i\ne r$. Its determinant is $1-\sum_{i\ne r}\alpha_i=\alpha_r$. Hence $A_T(h)=\alpha_r U$ and $[A_T(h),B_T]=\alpha_r[U]^2=\alpha_r T_n$. $\square$

At the centroid, each tree contributes $w(T)T_n/n$. Summing tree weights over all $n$ roots gives $n\tau$, leaving top coefficient $\tau$.

For $h=a_r$, trees toward other roots give zero, and each tree toward $a_r$ gives its full contribution $w(T)T_n$. Generally, (6) and (8) give the same result:

$$
M_{n-1}=\left(\sum_r\alpha_r\tau_r\right)T_n=\tau T_n
$$

The common coefficient $\tau$ refers to one fixed root. It is not the sum over all roots unless that sum is divided by $n$.

## Example: the unit directed 3-cycle

Consider $a\to b\to c\to a$ with unit weights. For $h=c$, set $u=a-c$, $v=b-c$. Then

$$
L=H_a+H_b,\qquad H_a=[u,u-v],\qquad H_b=[v,v]
$$

Both $H_a^2$ and $H_b^2$ vanish, while the mixed product is

$$
H_aH_b=[uv,(u-v)v]=[uv]^2=[(abc)]^2
$$

The final equality uses $uv=(cab)=(abc)$. Consequently,

$$
\boxed{M=(e+H_a)(e+H_b)=e+L+[(abc)]^2}
$$

This directly gives $L^2=2[(abc)]^2$, $L^3=0$, and $\tau=1$.

### The same calculation using the centroid

Let $h=(a+b+c)/3$, and let $E_{ab},E_{bc},E_{ca}$ be the centered arc forms. Then

$$
M=(e+E_{ab})(e+E_{bc})(e+E_{ca})
$$

Grade one equals $L$. Grade two contains three trees, while the product of all three arc forms vanishes.

![[Spanning Trees of a Directed 3-Cycle.svg]]

*Each root gives one tree: $b\to c\to a$, $c\to a\to b$, or $a\to b\to c$. The cycle arc leaving the chosen root is omitted. The three tree contributions depend on the reference point.*

| Root | Product of arc forms | Contribution for $h=(a+b+c)/3$ | Contribution for $h=c$ |
| --- | --- | --- | --- |
| $a$ | $E_{bc}(h)E_{ca}(h)$ | $T_3/3$ | $0$ |
| $b$ | $E_{ca}(h)E_{ab}(h)$ | $T_3/3$ | $0$ |
| $c$ | $E_{ab}(h)E_{bc}(h)$ | $T_3/3$ | $T_3$ |

Both cases give $M_2=T_3$. The centroid entry in the last row can also be checked directly: with $u=a-c$, $v=b-c$,

$$
a-h=\frac{2u-v}{3},\qquad b-h=\frac{2v-u}{3}
$$

Thus $(a-h)(b-h)=uv/3$, whereas $(a-b)(b-c)=(u-v)v=uv$. It follows that $E_{ab}(h)E_{bc}(h)=[uv/3,uv]=T_3/3$, independently of the general tree lemma.

### Two opposite directed 3-cycles

Give the forward cycle weight $p$ and the reverse cycle weight $q$, with $p,q\ge0$. In the same basis $u,v$ and with $h=c$,

$$
H_a=[u,(p+q)u-pv],\qquad
H_b=[v,-qu+(p+q)v]
$$

The exterior product of the right arguments is

$$
((p+q)u-pv)(-qu+(p+q)v)
=((p+q)^2-pq)uv
$$

Hence

$$
\boxed{M=e+L+(p^2+pq+q^2)T_3}
$$

This follows by multiplying forms. Independently, trees toward $c$ have arc sets $a\to b$, $b\to c$; $a\to c$, $b\to c$; and $b\to a$, $a\to c$, with weights $p^2,pq,q^2$. Setting $p=1,q=0$ recovers the unit cycle; $p=q=1$ gives the symmetric triangle with $\tau=3$.

## Returning to undirected graphs

In a 2-balanced graph, each opposite arc pair has common weight $c_{ij}=f_{ij}=f_{ji}$. For any $h$, its forms satisfy

$$
E_{ij}(h)+E_{ji}(h)=c_{ij}[(a_i a_j)]^2,\qquad
E_{ij}(h)E_{ji}(h)=0
$$

The second equality follows from dependence of the right arguments $a_i-a_j$ and $a_j-a_i$. The corresponding factors therefore combine:

$$
(e+E_{ij}(h))(e+E_{ji}(h))
=e+c_{ij}[(a_i a_j)]^2
$$

Combining every opposite pair recovers

$$
M=\prod_{\{i,j\}\in E(G)}(e+c_{ij}[(a_i a_j)]^2)
$$

Expanding gives the quadratic forms of undirected forests from [[Laplacian Exponential#Grade components and spanning forests|the symmetric Laplacian exponential]]. The directed forest construction agrees with the original PMG construction after opposite arcs are grouped.

## What the construction provides

Balance represents $L$ by forms on boundaries. Bilinearity and the commutative product ensure closure and finite exponential factorization. Minors provide coordinates; directed forests explain the arc expansion combinatorially. None requires an initial symmetric/skew-symmetric split.

Grouping forests by component sizes, reconciling normalizations with the symmetric case, and passing to the Laplacian polynomial are treated in [[Toponomes of Balanced Graphs and Directed Forests]]. Such grouping uses a fixed forest representation and does not define universal multiplication of numerical types.

The exterior exponential and its determinant coefficients are established algebraic constructions [1, 2]. Here they are applied to a balanced graph's boundary space and related to the affine reference point. A self-contained proof in PMG notation is not itself a claim of novelty.

[[The Circulation Form]] studies skew-symmetric boundary forms as independent PMG objects, including forms outside the nonnegative Laplacian class. Their potentials and metric evaluations are connected in [[One-Way Resistance and Hitting Times]] and [[Resistance Geometry and Circulation]], where the directed bilinear pairing is distinguished from its symmetric part.

## Sources and connections

The numbering below is used throughout. Section and proposition numbers for [2] refer to the linked preprint.

1. M. L. Labbi. [On some algebraic identities and the exterior product of double forms](https://arxiv.org/abs/1112.1346). *Archivum Mathematicum* **49** (2013), 241-271. [DOI: 10.5817/AM2013-4-241](https://doi.org/10.5817/AM2013-4-241). Double-form multiplication: §1.1; powers of arbitrary bilinear forms and determinants: §2.1, equation (16).
2. A. Belkhirat, M. L. Labbi. [Interactions between the composition and exterior products of double forms and applications](https://arxiv.org/abs/1402.4072). Preprint, 2014. Double forms and double exterior vectors: §2; the diagonal subalgebra: Definition 2.1; exterior exponentials and operator extensions: §5, Proposition 5.1. Journal version: [On the composition and exterior products of double forms and p-pure manifolds](https://journals.tubitak.gov.tr/math/vol43/iss1/44/), *Turkish Journal of Mathematics* **43** (2019), 539-560.
3. A. Abdesselam. [Grassmann-Berezin Calculus and Theorems of the Matrix-Tree Type](https://arxiv.org/abs/math/0306396). *Advances in Applied Mathematics* **33** (2004), 51-70. [DOI: 10.1016/j.aam.2003.07.002](https://doi.org/10.1016/j.aam.2003.07.002). Grassmann exponentials and minor extraction: §2, Proposition 5, equations (15)-(16); directed forests and the all-minors theorem: §3.
4. A. Postnikov, notes by A. Lin. [Lecture 29: Proof of Directed Matrix Tree Theorem based on induction](https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/4b3d3325c633bfb7fdea92ab6d6f6d1e_MIT18_212S19_lec29.pdf). *18.212 Algebraic Combinatorics*, 2019. The weighted directed matrix-tree theorem and the outgoing Laplacian convention.

Related library notes:

- [[The Bilinear Laplacian of a Balanced Graph]]: centering, arc and vertex representations, arbitrary reference points, and boundary products.
- [[Balanced Graphs and Spanning-Tree Potentials]]: connectedness, the directed matrix-tree theorem, and equal spanning-tree potentials.
- [[Basic Objects and Operations of Polyform Algebra]]: forms, grades, and multiplication.
- [[Laplacian Exponential]]: the symmetric case, forest forms, and the determinant lemma.
