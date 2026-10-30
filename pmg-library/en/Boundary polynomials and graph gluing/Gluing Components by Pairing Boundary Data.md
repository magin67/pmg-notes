---
title: "Gluing Components by Pairing Boundary Data"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 8
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: gluing-components-as-boundary-pairing
order: 3
description: "Forest compatibility and the bilinear gluing law. State coordinates, contraction responses, nondegenerate quotients, two- and three-point examples, and shared-edge conventions."
---

The full boundary forest passport records how a forest connects marked vertices, including contributions from components disjoint from the boundary. We now establish its sufficiency for gluing: the forest polynomial of the combined graph is computed from two passports and a universal compatibility matrix. Once the passports have been constructed, the internal structure of the parts is no longer needed.

The passport is defined in [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]]. [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]] derives the linear response to a fixed identification scheme. In gluing, the other side is also given by state polynomials, making the law bilinear.

> [!info] Provenance of the results
> **From the literature.** The forest compatibility matrix and the combination of state tables appear in [Mannens–Nederlof, §§4.2–4.3](https://arxiv.org/html/2307.01046#S4.SS2).
>
> **Derivations and exposition here.** The established combination rule is written for weighted generating polynomials and proved by a bijection. Passing from states to test responses is linear algebra for this matrix; the rules for shared edges and the examples specify its conditions of use.
> “Derived here” identifies where a proof is given; no claim of scientific priority is made.

## Which parts are joined, and how

Let $G_1,G_2$ be finite undirected graphs with positive conductances and marked boundaries of $k\ge1$ vertices. The parts need not be connected. First choose a bijection between the boundaries; after renaming, corresponding vertices have identical names and form the set $B$.

Fix the gluing conditions as follows:

$$
V(G_1)\cap V(G_2)=B,\qquad
E(G_1)\cap E(G_2)=\varnothing
$$

Internal vertices of the parts are distinct. Edges have separate labels, retain their conductances, and are counted once each. If two edges acquire identical endpoints after identification, they remain distinguishable parallel edges. Loops belong to no forest. Write the operation as $G=G_1\#_B G_2$; its vertex count is $n=n_1+n_2-k$.

The edge condition allows two distinct copies of the same boundary pair. It does not identify these copies as one edge: that operation requires a separate choice of edge set, discussed below.

For a spanning forest $H$, write its weight and induced boundary partition as $w(H)=\prod_{e\in E(H)}c_e$ and $\pi_B(H)$. Recall the state polynomial and passport column:

$$
\mathcal F^{G_i,B}_\pi(t)
=\sum_{\substack{H\text{ a spanning forest of }G_i\\\pi_B(H)=\pi}}
w(H)t^{|E(H)|},\qquad
\mathbf f_i(t)=\bigl(\mathcal F^{G_i,B}_\pi(t)\bigr)_{\pi\in\Pi(B)}
$$

All vertices belong to the forest, including isolated vertices. Components with no boundary vertices are not excluded. The sum of the coordinates is $F_{G_i}(t)$.

## Compatibility of two forest states

Let $b(\pi)$ be the number of blocks and $r(\pi)=k-b(\pi)$. The join $\pi\vee\sigma$ is the least common coarsening: it connects vertices through sequences of steps within blocks of $\pi$ or $\sigma$.

**Definition.** Partitions $\pi,\sigma$ are compatible if

$$
r(\pi\vee\sigma)=r(\pi)+r(\sigma)
$$

The forest compatibility matrix has entries

$$
\boxed{
(\mathbf C_B)_{\pi\sigma}=C(\pi,\sigma)=
\begin{cases}
1,&r(\pi\vee\sigma)=r(\pi)+r(\sigma)\\
0,&\text{otherwise}
\end{cases}}
\tag{1}
$$

It is symmetric and depends only on the boundary and the ordering of partitions. This is the *forest compatibility* matrix of [1, Definitions 4.3–4.5].

**Lemma.** For forests $H_i\subseteq G_i$ with states $\pi,\sigma$, the union $H_1\cup H_2$ is a forest if and only if $C(\pi,\sigma)=1$.

**Proof.** Let $g_i$ be the number of edges of $H_i$ and $k_{0,i}$ the number of its components containing no boundary vertex. Then

$$
g_1=n_1-k_{0,1}-b(\pi),\qquad
g_2=n_2-k_{0,2}-b(\sigma)
$$

Internal components remain unchanged in the union, while components meeting $B$ join according to $\pi\vee\sigma$. The number of independent cycles in the union is

$$
\begin{aligned}
(g_1+g_2)-n+k_{0,1}+k_{0,2}+b(\pi\vee\sigma)
&=k-b(\pi)-b(\sigma)+b(\pi\vee\sigma)\\
&=r(\pi)+r(\sigma)-r(\pi\vee\sigma)
\end{aligned}
$$

It is zero exactly under condition (1). The count also applies to distinguishable parallel edges. $\square$

This is the same as [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test#When the image of a forest remains a forest|the contraction criterion]]. Here, however, both sides are forests of graph parts. The internal-component counts cancel in the cycle test while their contributions remain in the state polynomials.

## The bilinear law for the full forest polynomial

**An established law in polynomial form.** The combination of tables over compatible partitions appears in [the proof of Lemma 4.21 of Mannens–Nederlof](https://arxiv.org/html/2307.01046#S4.SS3). Formulas (2)–(3) below use the same rule with weights and powers of $t$.

**Theorem.** Under the gluing rules fixed above,

$$
\boxed{
\begin{aligned}
F_{G_1\#_B G_2}(t)
&=\sum_{\pi,\sigma\in\Pi(B)}
\mathcal F^{G_1,B}_\pi(t)C(\pi,\sigma)\mathcal F^{G_2,B}_\sigma(t)
\\
&=\mathbf f_1(t)^{\mathsf T}\mathbf C_B\mathbf f_2(t)
\end{aligned}
}
\tag{2}
$$

**Proof.** Edge labels uniquely split every forest of the resulting graph into forests of the two parts. Conversely, a pair of forests has an admissible union exactly under the condition of the lemma. Weights multiply and edge counts add:

$$
w(H_1\cup H_2)=w(H_1)w(H_2),\qquad
t^{|E(H_1\cup H_2)|}=t^{g_1}t^{g_2}
$$

Summing first over forest pairs with fixed states and then over states gives (2). $\square$

There is no additional power of $t$. Identifying boundary vertices decreases the vertex count but not the number of selected edges. In particular, the constant term of (2) is $1$: the empty forests of the two parts are compatible.

To compare with the corank convention, suppose the parts are connected and set $d_i=n_i-1$, $d=n-1=d_1+d_2-(k-1)$. If $\widehat{\mathbf f}_i(u)=u^{d_i}\mathbf f_i(u^{-1})$, then

$$
u^dF_G(u^{-1})
=u^{-(k-1)}\widehat{\mathbf f}_1(u)^{\mathsf T}\mathbf C_B\widehat{\mathbf f}_2(u)
$$

This is where the corank factor appears. It comes from inverting the variable with different top degrees and does not carry over to (2).

### The passport of the result

If the same marked boundary $B$ is retained after gluing, we can compute every state of the result as well as $F_G$:

$$
\boxed{
\mathcal F^{G,B}_\theta(t)
=\sum_{\substack{\pi,\sigma\in\Pi(B)\\\pi\vee\sigma=\theta}}
C(\pi,\sigma)\mathcal F^{G_1,B}_\pi(t)\mathcal F^{G_2,B}_\sigma(t)
}
\tag{3}
$$

The proof is the same: an admissible union has boundary partition $\pi\vee\sigma$. Its number of internal components is $k_{0,1}+k_{0,2}$. The full passport therefore supports further gluing. If several parts share one boundary, have pairwise distinct internal vertices, and have disjoint edge labels, successive application of (3) is independent of parenthesization: it enumerates the same forests of the combined graph.

Changing or reducing the retained boundary requires a separate transformation of states. Formula (3) alone does not define an arbitrary input and output interface for a chain.

## States and test responses

**A linear-algebra consequence.** This section's formulas follow from the compatibility matrix and the proved contraction rule. Inverting a nondegenerate pairing is a general linear-algebra procedure; here we specify its meaning for forest data.

On the free space $\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R s_\pi$, define the bilinear form

$$
\mathcal C_B(s_\pi,s_\sigma)=C(\pi,\sigma)
$$

Extending it coefficientwise to $\mathscr S_B[t]$ gives (2). This is an **algebraic pairing of states**, not a resistance inner product. It is not determined by the Laplacian of a particular component and need not be positive definite.

For each contraction scheme $\sigma$, we know the response

$$
U_i(\sigma;t)=F_{G_i/\sigma}(t)
=\sum_\pi C(\pi,\sigma)\mathcal F^{G_i,B}_\pi(t)
$$

Collect these polynomials into a column $\mathbf u_i$ in the same partition order. Symmetry gives

$$
\boxed{\mathbf u_i=\mathbf C_B\mathbf f_i}
\tag{4}
$$

The coordinate $\mathcal F_\pi$ counts forests of one exact state; $U(\sigma;t)$ sums all states compatible with the test. These are different data even though their index sets coincide.

If $\mathbf C_B$ is nonsingular, (4) implies

$$
\boxed{F_{G_1\#_B G_2}(t)
=\mathbf u_1(t)^{\mathsf T}\mathbf C_B^{-1}\mathbf u_2(t)}
\tag{5}
$$

The inverse matrix comes from changing coordinates. Substituting $\mathbf u_i$ for $\mathbf f_i$ in (2) without this change would give a different quantity.

### Where inversion is allowed

Singularity is also a known issue for the forest specialization of the Tutte polynomial: Burgos [2, §4, Theorem 4.2; §5] uses an equation for a generalized inverse. His variable and normalization differ from ours; we work directly with the compatibility matrix.

For an arbitrary boundary, the full matrix is not assumed invertible. The natural nondegenerate space for the scalar pairing is the quotient

$$
\mathscr R_B=\{x:\mathcal C_B(x,y)=0\text{ for all }y\}
=\ker\mathbf C_B,\qquad
\mathscr H_B=\mathscr S_B/\mathscr R_B
$$

The pairing is well-defined on classes: adding an element of $\mathscr R_B$ changes no result in (2). It is nondegenerate on the quotient by definition of the radical. Choosing a basis $b_1,\ldots,b_m$ there gives a nonsingular matrix $K_{ij}=\mathcal C_B(b_i,b_j)$ and a formula of the form (5), with $\mathbf K^{-1}$, for responses to this basis. The explicit four-point reduction, the general Catalan rank, and minimality among linear passports are proved in [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]].

The dual basis with respect to this pairing is

$$
b^j=\sum_\ell(\mathbf K^{-1})_{\ell j}b_\ell,\qquad
\mathcal C_B(b_i,b^j)=\delta_i^j
$$

This is coordinate duality. It is not Laplacian–Greenian duality and does not automatically transfer structural polyform identities to free forest states. The quotient preserves the scalar pairing (2); no reconstruction of all original coordinates from it is asserted.

## Two boundary vertices

Let $B=\{a,b\}$, with state order $a|b,ab$. Denote the separated-state and connected-state polynomials by $D_i,S_i$. Then

$$
\mathbf C_2=
\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
\det\mathbf C_2=-1,\qquad
\mathbf C_2^{-1}=
\begin{pmatrix}0&1\\1&-1\end{pmatrix}
$$

Only the pair of connected states is forbidden: two paths between $a,b$ create a cycle. Formula (2) becomes

$$
F_G=D_1D_2+D_1S_2+S_1D_2
=F_{G_1}F_{G_2}-S_1S_2
\tag{6}
$$

This is the previously published [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#Two boundary states of an ordinary forest|two-state formula]], now a special case of the full passport.

The responses are $U_i(a|b)=F_{G_i}$ and $U_i(ab)=D_i$. Thus (5) gives the equivalent expression

$$
F_G=F_{G_1}U_2(ab)+U_1(ab)F_{G_2}-U_1(ab)U_2(ab)
$$

Even on this boundary, the pairing is not positive definite: for $v=s_{a|b}-2s_{ab}$, we have $\mathcal C_B(v,v)=-3$. Negative entries of the inverse matrix are not negative conductances; they arise when states are recovered from overlapping test sums.

### Two paths form a cycle

Take unit-weight paths $a-x-b$ and $a-y-b$ with common boundary $\{a,b\}$ and distinct internal vertices $x,y$. Their edges are distinct. Each path has

$$
D=1+2t,\qquad S=t^2,\qquad F=(1+t)^2
$$

The result is the cycle $a-x-b-y-a$. By (6),

$$
F_{C_4}(t)=(1+t)^4-t^4=1+4t+6t^2+4t^3
$$

The unique pair selecting both complete paths is subtracted. The constant term of $D_1D_2$ includes two isolated internal vertices $x,y$; excluding forests that are not groves would lose this contribution and other lower coefficients.

![[Two paths and two-point pairing.svg]]

**The forest polynomial of a cycle.** Green and blue edges belong to different parts; gold circles mark the shared boundary. Only the simultaneous selection of all four edges is forbidden. The drawing specifies the graphs and boundary correspondence, not resistance distances.

## Three boundary vertices

For $B=\{x,y,z\}$, fix the order

$$
\pi_0=x|y|z,\quad
\pi_1=xy|z,\quad
\pi_2=xz|y,\quad
\pi_3=x|yz,\quad
\pi_4=xyz
$$

The discrete state is compatible with every state. Among the three states containing one pair, distinct states are compatible and identical states are not. The fully connected state is compatible only with the discrete state. Hence

$$
\mathbf C_3=
\begin{pmatrix}
1&1&1&1&1\\
1&0&1&1&0\\
1&1&0&1&0\\
1&1&1&0&0\\
1&0&0&0&0
\end{pmatrix},\qquad
\det\mathbf C_3=-2
$$

![[Compatibility of five three-point states.svg]]

**Compatibility table.** An entry is $1$ if the pair of states produces a forest and $0$ if it creates a cycle. Color repeats the numerical information. The table applies to all graphs with this boundary; the parts need not be planar.

Write one passport's coordinates as $f_j=\mathcal F_{\pi_j}$ and its responses as $u_j=U(\pi_j;t)$. Then

$$
\begin{aligned}
u_0&=f_0+f_1+f_2+f_3+f_4\\
u_1&=f_0+f_2+f_3,&u_2&=f_0+f_1+f_3\\
u_3&=f_0+f_1+f_2,&u_4&=f_0
\end{aligned}
$$

Nonsingularity allows all five polynomials to be recovered:

$$
\begin{aligned}
f_0&=u_4\\
f_1&=\tfrac12(-u_1+u_2+u_3-u_4)\\
f_2&=\tfrac12(u_1-u_2+u_3-u_4)\\
f_3&=\tfrac12(u_1+u_2-u_3-u_4)\\
f_4&=u_0-\tfrac12(u_1+u_2+u_3-u_4)
\end{aligned}
$$

In this order, therefore,

$$
\mathbf C_3^{-1}=\frac12
\begin{pmatrix}
0&0&0&0&2\\
0&-1&1&1&-1\\
0&1&-1&1&-1\\
0&1&1&-1&-1\\
2&-1&-1&-1&1
\end{pmatrix}
$$

The recovery formulas verify the inverse matrix directly, not just its determinant. For two three-point passports, both expressions now apply: $\mathbf f_1^{\mathsf T}\mathbf C_3\mathbf f_2$ and $\mathbf u_1^{\mathsf T}\mathbf C_3^{-1}\mathbf u_2$.

### One partner and two markings of a path

Use [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component#One forest polynomial, different gluing results|the example showing dependence on the boundary choice]]: the paths

$$
X:\ x-b-y-d-z,\qquad
X':\ x-b-z-d-y
$$

have unit conductances and boundary $B=\{x,y,z\}$. Their partner $J$ has one unit edge $xy$ and the isolated boundary vertex $z$. Vertices with the same name are identified; there are no shared edges.

Set $A=(1+2t)^2$ and $Q=t^2(1+2t)$. In the fixed state order,

$$
\mathbf f_X=(A,Q,0,Q,t^4)^{\mathsf T},\qquad
\mathbf f_{X'}=(A,0,Q,Q,t^4)^{\mathsf T},\qquad
\mathbf f_J=(1,t,0,0,0)^{\mathsf T}
$$

The zero coordinates differ: $xz|y$ is impossible for $X$, and $xy|z$ for $X'$. Since the partner has only two nonzero states, (2) reduces to

$$
F_{X\#J}=F_X+tU_X(xy|z;t),\qquad
F_{X'\#J}=F_{X'}+tU_{X'}(xy|z;t)
$$

The row $\pi_1$ of $\mathbf C_3$ gives

$$
U_X(xy|z;t)=A+Q,\qquad
U_{X'}(xy|z;t)=A+2Q
$$

Although $F_X=F_{X'}=(1+t)^4$, the results differ:

$$
\begin{aligned}
F_{X\#J}(t)&=1+5t+10t^2+9t^3+3t^4\\
F_{X'\#J}(t)&=1+5t+10t^2+10t^3+5t^4
\end{aligned}
$$

Their difference is $tQ=t^3+2t^4$. It gives exactly the contribution of the boundary state whose role changed when the marking was permuted.

![[One partner and two markings of a path.svg]]

**The same graphs, evaluated by pairing.** The figure from the forest-state note shows a triangle with a tail and the cycle $C_5$. Here their polynomials are obtained from passports; directly excluding the unique cycle in each graph gives an independent check.

### The boundary correspondence is part of the data

If $\beta:B_2\to B_1$ is the chosen bijection, it carries $\sigma$ to $\beta(\sigma)$. Let $\mathbf P_\beta$ transfer the coordinate column accordingly. Before renaming to a common set, we have

$$
F_{G_1\#_\beta G_2}
=\mathbf f_1^{\mathsf T}\mathbf C_{B_1}\mathbf P_\beta\mathbf f_2
$$

Simultaneously permuting the names on both boundaries preserves compatibility: $\mathbf P^{\mathsf T}\mathbf C_B\mathbf P=\mathbf C_B$. Permuting only one side changes the contact correspondence and can change the result, as in the path example. Numbering coordinates alone does not specify the bijection.

## If the parts are intended to share an edge

Suppose each part consists of one edge between boundary vertices $a,b$, with conductances $p$ and $q$. Under our rule, both distinct labels are retained. Their passports are $(1,pt)$ and $(1,qt)$, so

$$
F_{G_1\#_B G_2}(t)=1+(p+q)t
$$

The term $pq\,t^2$ is excluded: selecting both parallel edges forms a cycle. They may be replaced by one connection of conductance $p+q$ while preserving the weighted forest polynomial. This does not identify the two copies as one edge of conductance $p$ or $q$.

![[Distinct copies and one shared edge.svg]]

**Two different seam rules.** With unit conductances, retaining both copies gives $1+2t$, while retaining one shared unit edge gives $1+t$. In the first case, the parallel copies may be combined into conductance $2$; in the second, the single label is counted once.

If a graph has a genuinely shared edge $e$ of conductance $c$, one way to apply (2) is to assign it to one part in advance and delete the second copy. Passports are then built for this new distribution of edges. For example, use $G_1\#_B(G_2\setminus e)$ if the edge is retained in $G_1$. Assign each of several shared edges to exactly one part. One cannot divide the completed formula (2) by $1+ct$: selecting an edge depends on the pre-existing connectivity of its endpoints. Further seam conventions are discussed in [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#A shared seam and parallel conductors|the comparison of gluing rules]].

## Connection with the product of polyforms

After matching names, embed both parts in one vertex space. For disjoint edge labels,

$$
L_G=L_1+L_2,\qquad
\exp(tL_G)=\exp(tL_1)\exp(tL_2)
$$

This is a product in the polyform algebra, not a matrix exponential. In the labeled forest expansion, the product of two forest forms vanishes exactly when a cycle appears. It therefore performs the same selection as (1).

However, after structural identities are imposed, summing the coefficients of a chosen forest expansion does not automatically define a linear evaluation of the polyform itself. Formula (2) is proved on free states and requires no such passage. The map $s_\pi\mapsto q_\pi$, where $q_\pi$ is a partition form, and the quotient by $\ker\mathbf C_B$ are different constructions; equal coordinate counts do not identify them.

Adding Laplacians likewise does not mean adding the Greenians of the parts: taking a pseudoinverse is not linear. Neither $\mathbf C_B$ nor $\mathbf C_B^{-1}$ is a Green matrix or a resistance Gram matrix.

## The spanning-tree layer and further reduction

The resulting graph has $n=n_1+n_2-k$ vertices, so its spanning-tree coefficient is $[t^{n-1}]F_G(t)$. If an admissible union is a tree, its original forests have no internal components and $\pi\vee\sigma=\{B\}$. On this layer, (2) therefore becomes [[en/Structural identities/Structural Identities and Graph Gluing#The spanning-tree coefficient after gluing|the previously published grove pairing]]. A grove is a spanning forest whose every component meets the boundary.

[[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]] expresses the spanning-tree pairing through resistance Gram matrices and a Schur complement, specifying its conditions and the limits of reconstruction from electrical response. The full forest polynomial also retains all lower degrees, including forests with internal components. [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]] constructs reduced linear coordinates and distinguishes the forest radical from the structural kernel of partition forms. [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]] separates ordinary forest passports from spectral passports using graphs with identical ordinary passports and different characteristic polynomials, and derives a separate gluing law for the spectral problem.

## Status of the results and checks

Criterion (1), law (2), and the result-passport formula (3) are proved for the stated class of weighted graphs without connectivity or planarity assumptions. The response formula (5) requires a nonsingular matrix: this is established explicitly for two and three vertices, while a suitable quotient space is defined in general. Its general dimension and a concrete basis are not computed here.

The [exact verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_pairing.py) compares the pairing formula with direct enumeration of forests in the combined graph, including every resulting state. Compatibility matrices are checked through independence of the edges of partition representatives; inverse matrices and the passage to responses are checked using rational arithmetic. Separate checks cover the examples, boundary permutations, internal components, loops, parallel and shared edges, and successive gluing of three parts. [Instructions for running the checks and reproducing the figures](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) accompany the script. Finite checks supplement the general proofs.

## Sources and connections

1. I. Mannens, J. Nederlof. *A Fine-Grained Classification of the Complexity of Evaluating the Tutte Polynomial on Integer Points Parameterized by Treewidth and Cutwidth*. [arXiv:2307.01046, §4.2, Definitions 4.3–4.5; §4.3, Definition 4.14 and the proof of Lemma 4.21](https://arxiv.org/html/2307.01046#S4.SS2). The forest compatibility matrix, state tables, and their combination rule. Formulas (2)–(3) are a polynomial version of this rule, justified here by a weight-preserving bijection.
2. J. M. Burgos. *Singularities in Negami's splitting formula for the Tutte polynomial*. Discrete Applied Mathematics, 237 (2018), 65–74. [arXiv:1605.05499, §4, Theorem 4.2; §5](https://arxiv.org/html/1605.05499#S4). The forest specialization $y=1$ requires separate treatment of singular matrices. The source uses a different variable and normalization; its general splitting formula cannot be mechanically transferred to (2) or inverted in the singular case.
3. R. W. Kenyon, D. B. Wilson. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society, 363 (2011), 1325–1364. [arXiv:math/0608422, §§1.1, 2.1–2.2](https://arxiv.org/html/math/0608422v4#S2). Groves and the spanning-tree pairing of boundary partitions. Electrical results for circular planar networks must be used with their hypotheses; the full forest-law proofs above require no planarity.

Supporting PMG notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]], [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]], [[en/Structural identities/Structural Identities and Graph Gluing|Structural Identities and Graph Gluing]], [[en/Introduction/Laplacian Exponential|Laplacian Exponential]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/Сочленение компонент как спаривание граничных данных|Русский]]
