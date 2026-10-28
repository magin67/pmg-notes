---
title: "The Cycle Matroid and Exterior Products of Edges"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: cycle-matroid-and-exterior-products-of-edges
lang: en
description: "Matroid parameters as a tool for studying invariants of gluing. Edge independence, forest sums and their representations in the Laplacian and Greenian exponentials; limits of matroid invariance."
order: 1
---

Gluing the same graph pieces in different ways can change vertex distances, degrees, and positions in resistance geometry. Some numerical characteristics nevertheless remain unchanged. To explain such coincidences, we must determine what information about the graph suffices to compute each characteristic.

The cycle matroid retains the dependence structure of the edges: which sets are forests and which contain cycles. A graph transformation that preserves this structure and the weights of corresponding edges preserves every parameter determined by the weighted cycle matroid. This provides a general method for proving invariance and distinguishing it from specific gluing laws.

In PMG, this object is already present in the exterior-product rules: independent edge sets correspond to nonzero products of their vectors, while cycles give zero products. Matroid theory names this familiar structure. A general definition is given below; no prior knowledge of matroid theory is required.

Forest data are considered on both sides: in the Laplacian exponential and in the Greenian exponential. Their duality transfers representations and computations, but does not by itself make every coefficient or metric parameter a matroid invariant.

## From gluing to the question of invariants

[[Vertex Contraction and Graph Gluing]] proves two different laws for connected graphs glued at exactly one vertex:

$$
\begin{aligned}
\tau(G_1\vee G_2)&=\tau(G_1)\tau(G_2)\\
\rho(G_1\vee G_2)&=\rho(G_1)+\rho(G_2)
\end{aligned}
$$

Here $\tau$ is the spanning-tree coefficient and $\rho=R_{\mathrm{sph}}^2$ is the quadratic resistance radius in the current normalization. The pieces have disjoint edge sets; $\vee$ identifies one chosen vertex of each piece and preserves conductances.

These formulas show that the result does not depend on which vertices of the given pieces are identified. They also raise two separate questions:

1. **Invariance:** which transformations of the edge structure preserve the parameter?
2. **Gluing law:** how is the parameter of the combined graph computed from data of its pieces?

The matroid answers the first question once the parameter has been proved to depend only on the matroid. The second requires a separate derivation: $\tau$ multiplies, whereas $\rho$ adds. Neither property follows from the other.

The practical aim of the series is to identify families of such parameters, give methods for computing them, and then apply them to graph gluings and chains of cores. For a particular family of gluings, preservation of the cycle matroid must first be checked. Agreement of several computed numbers is insufficient.

## Edges as vectors

Let $G=(\mathcal V,E)$ be a finite undirected graph without loops or parallel edges, with $\mathcal V=\{a_1,\ldots,a_n\}$ and $n\ge2$. Sections on the metric and Greenian additionally assume connectedness and positive conductances $c_\ell$ on existing edges. All conductances in unweighted examples equal $1$.

We fix this particular edge set. If an electrical network is specified by separate parallel conductors, merging them into one coupling with their total conductance preserves the Laplacian but changes the ground set of the matroid. Such a merger is not a matroid isomorphism.

The direct vertices $a_i$ form a linearly independent basis of $V$. The space of affine vectors is

$$
W=\left\{\sum_i u_i a_i:\sum_i u_i=0\right\},\qquad \dim W=n-1
$$

Choose an orientation of each edge $\ell=\{i,j\}$ and associate the vector

$$
v_\ell=a_j-a_i=a_{ij}
$$

Orientation is only a notational choice: reversing it multiplies the vector by $-1$ without changing linear independence. For an edge set $S=\{\ell_1,\ldots,\ell_g\}$, put

$$
B_S=v_{\ell_1}\cdots v_{\ell_g}\in\Lambda^gW
$$

Juxtaposition of vectors denotes the exterior product. Order and orientation may change the sign of $B_S$, but not the condition $B_S\ne0$ or the quadratic form $[B_S]^2$. For the empty set, $B_\varnothing=1$ and $[B_\varnothing]^2=e$.

These constructions use only [[Basic Objects and Operations of Polyform Algebra|exterior algebra and forms]]. No resistance metric is needed yet.

## Independence, forests, and cycles

**Theorem.** For an edge set $S\subseteq E$, the following conditions are equivalent:

$$
\boxed{
\begin{gathered}
S\text{ is a forest}
\\
\Longleftrightarrow\quad\{v_\ell:\ell\in S\}\text{ are linearly independent}
\\
\Longleftrightarrow\quad B_S\ne0
\end{gathered}
}
$$

A forest here is a subgraph on the entire set $\mathcal V$, including isolated vertices. Maximality under inclusion is not required.

**Proof.** If $S$ contains a cycle, orient it consistently. For its vertices $a_{i_1},\ldots,a_{i_m}$,

$$
(a_{i_2}-a_{i_1})+(a_{i_3}-a_{i_2})+\cdots+(a_{i_1}-a_{i_m})=0
$$

Other choices of orientation change only the coefficient signs. This is a nontrivial linear dependence, so the exterior product of all vectors in the set vanishes.

Now suppose $S$ is a nonempty forest and

$$
\sum_{\ell\in S}\beta_\ell v_\ell=0
$$

Choose a leaf in a nontrivial component. Its basis vertex appears in exactly one edge vector, so the coefficient of that edge is zero. Delete the edge and repeat. Every coefficient is zero. The empty set is independent by definition.

The equivalence between linear independence and a nonzero exterior product is a standard property of exterior algebra. $\square$

For example,

$$
(ab)(bc)=(abc)\ne0,\qquad
(ab)(bc)(ca)=0
$$

![[Forest and Cycle - Exterior Products.svg]]

**Forest and cycle.** On the left, $ab,bc$ are selected; on the right, $ca$ is added. Around a closed traversal the edge vectors sum to zero, so their exterior product also vanishes. The gray dashed edge on the left belongs to the original triangle but is not selected. Arrows indicate the chosen orientation, not a directed graph.

For a tree, the product of its edge vectors equals the simplex boundary on its vertices up to sign. For a forest, it is the product of the component boundaries; an isolated vertex contributes $1$.

## What is a matroid?

**Definition.** A finite **matroid** $\mathsf M=(E,\mathcal I)$ consists of a finite ground set $E$ and a family $\mathcal I$ of its subsets, called independent sets. This family satisfies three conditions:

1. **The empty set is independent:** $\varnothing\in\mathcal I$.
2. **Heredity:** if $I\in\mathcal I$ and $J\subseteq I$, then $J\in\mathcal I$.
3. **Augmentation:** if $I,J\in\mathcal I$ and $\#I<\#J$, there is an element $\ell\in J\setminus I$ such that $I\cup\{\ell\}\in\mathcal I$.

Subsets outside $\mathcal I$ are dependent. Thus a matroid specifies a consistent independence rule; neither graph vertices nor vector coordinates enter its general definition. This is the standard definition from matroid theory [1].

**Example.** Associate vectors $v_\ell$ with the elements of $E$. Declare a set independent when its corresponding vectors are linearly independent. This gives the **linear matroid** of the vector system: the first two conditions are immediate, and the third follows by comparing dimensions. If every vector in a larger independent set $J$ lay in the span of a smaller set $I$, then $\#J\le\#I$, contrary to the hypothesis.

Linear and cycle matroids are examples of the general construction. The definition itself requires neither vector nor graph representability.

## The cycle matroid

**Definition.** The cycle matroid $\mathsf M(G)$ has ground set $E$. Its independent sets are the edge sets that form forests. By the theorem above, these are exactly the independent sets of the linear matroid of $\{v_\ell\}_{\ell\in E}$, and therefore satisfy all three defining conditions.

The notation $\mathsf M(G)$ is distinct from the polyform $M=\exp L$.

Four concepts suffice for what follows.

| Concept | Graph interpretation | Vector-system interpretation |
| --- | --- | --- |
| Independent set | Any forest | A linearly independent set |
| Basis | An inclusion-maximal forest | A maximal independent set of edge vectors |
| Circuit | The edge set of a simple cycle | A minimal dependent set |
| Rank of a set $S$ | Maximum number of edges in a forest contained in $S$ | Dimension of $\operatorname{span}\{v_\ell:\ell\in S\}$ |

A matroid circuit means a minimal dependence; it does not mean a graph path or a chain of glued cores.

If $\kappa(S)$ is the number of components of $(\mathcal V,S)$, including isolated vertices, then

$$
r(S)=n-\kappa(S),\qquad r(E)=n-\kappa(G)
$$

Indeed, a maximal forest in each component is a spanning tree and has one fewer edge than vertices. Thus a connected graph has rank $d=n-1$, and its bases are spanning trees. In a disconnected graph, a basis consists of a spanning tree in each component.

A forest $F$ with $g$ edges has $n-g$ components. Define its **corank** as the number of edges missing from full rank:

$$
k=r(E)-g=\kappa(F)-\kappa(G)
$$

For a connected original graph,

$$
k=d-g=\kappa(F)-1
$$

Thus the component count and corank differ by one only when the original graph is connected. The matroid does not record added isolated vertices: they change neither $E$ nor its independent subsets.

**Definition.** An isomorphism of cycle matroids is a bijection $\psi:E(G)\to E(H)$ such that $S$ is a forest if and only if $\psi(S)$ is a forest. In the weighted setting, additionally require

$$
c_{\psi(\ell)}=c_\ell
$$

Such a bijection preserves bases, cycles, and the ranks of all sets. It need not arise from a bijection between graph vertices.

## What is a matroid parameter?

**Definition.** A numerical or polynomial graph characteristic $P$ is a **matroid parameter** on a specified class of graphs if it is determined by the cycle matroid. Equivalently, isomorphic cycle matroids have equal values of $P$. For weighted graphs, conductances of corresponding edges must be preserved:

$$
\mathsf M(G)\simeq\mathsf M(H),\qquad
c'_{\psi(\ell)}=c_\ell
\quad\Longrightarrow\quad
P(G,c)=P(H,c')
$$

Here $\psi$ is the isomorphism, and $c,c'$ are the conductances of the two graphs. In the unweighted case they all equal $1$. For example, rank and the number of independent sets of each size are matroid parameters directly from the definition; the corresponding claims for weighted forest sums and metric characteristics require justification.

For a family indexed by individual edges, values are preserved under the same correspondence: $P_{\psi(\ell)}(H,c')=P_\ell(G,c)$. This is the meaning of matroid invariance for edge resistances proved below. It supplies no correspondence between all vertex pairs.

The graph class is part of the statement. Ordinary forest coefficients are defined even for disconnected graphs, whereas normalization by $\tau$ and the resistance radius in this series concern connected graphs on $n\ge2$ vertices. Adding isolated vertices preserves the matroid but leaves this metric class. Matroid invariance alone also specifies neither addition nor multiplication under gluing.

## Trees, cycles, and complete graphs

**Tree.** Every subset of its edges is independent. All trees with $m$ edges therefore have the same cycle matroid up to edge relabeling. Its only basis is the entire set $E$. A weighted isomorphism must also match equal conductances.

**Cycle $C_m$, $m\ge3$.** Every proper edge subset is independent, and the full set is dependent. The rank is $m-1$; bases are obtained by deleting one edge.

These two cases are uniform matroids: the independent sets of $U_{r,m}$ are exactly the sets of size at most $r$. A tree gives $U_{m,m}$, and a cycle gives $U_{m-1,m}$.

**Complete graph $K_n$, $n\ge4$.** Its rank is $n-1$, but size alone no longer determines independence. In $K_4$, $\{ab,bc,ca\}$ is dependent and $\{ab,bc,cd\}$ is independent, although both have three edges. Thus the matroid of $K_n$ is not uniform for $n\ge4$. The small cases $K_2$ and $K_3=C_3$ belong to the two examples above.

## Forest coefficients in the Laplacian exponential

Return to a connected graph with positive conductances. Put $d=n-1$ and

$$
L=\sum_{\ell\in E}c_\ell[v_\ell]^2,\qquad
M=\exp L=\sum_{g=0}^{d}M_g
$$

Nilpotence $([v_\ell]^2)^2=0$ and commutativity of the form product give

$$
M=\prod_{\ell\in E}\bigl(e+c_\ell[v_\ell]^2\bigr)
$$

Expanding selects one term from each factor. Sets containing a cycle vanish, so

$$
M_g=\sum_{\substack{F\subseteq E\text{ a forest}\\\#F=g}}
w(F)[B_F]^2,\qquad
w(F)=\prod_{\ell\in F}c_\ell
$$

This is the [[Laplacian Exponential|forest expansion of the exponential]] viewed through the matroid: nonzero products are indexed by independent edge sets.

Use the notation of [[Forest Coefficients and the Laplacian Polynomial]]:

$$
\boxed{
f_g(G)=\sum_{\substack{F\subseteq E\text{ a forest}\\\#F=g}}w(F),\qquad
F_G(t)=\sum_{g=0}^{d}f_g(G)t^g
}
$$

Here $f_0=1$ and $f_d=\tau$. These are weight sums of ordinary spanning forests without chosen roots.

**Corollary.** Every $f_g$, the polynomial $F_G$, and the spanning-tree coefficient $\tau$ are determined by the weighted cycle matroid.

**Proof.** A matroid isomorphism matches independent sets of the same size, and weight preservation preserves each product $w(F)$. $\square$

The sum $f_g$ refers specifically to the edge-factor expansion. Forms of different forests may be linearly dependent, so summing coefficients in an arbitrary other expression for $M_g$ need not give $f_g$. This distinction is explained in [[Partition Forms and the Tetrahedron Identity]] and [[From Polyforms to Partitions]].

Matroid invariance of $f_g$ does not imply invariance of the distribution of these forests by component sizes. Such a distribution uses additional vertex data.

## The same original forests in the Greenian exponential

Matroid parameters are not exclusive to the Laplacian. Its advantage is that the original edges and their conductances occur directly in the vector factors. Duality transfers the same forest weights to another representation.

For a fixed vertex set, the full Greenian recovers the Laplacian: $\mathbf{Gr}^+=\mathbf L$. Thus both full forms contain information about the entire weighted graph, not just its matroid. Matroid invariance is a property of the particular characteristic extracted, rather than a consequence of choosing one of these forms.

Recall the current notation:

$$
\mathbf{Gr}=\mathbf L^+,\qquad
D=\exp Q_1=\sum_{k=0}^{d}Q_k,\qquad Q_0=e
$$

Here $Q_1$ is the dual representation of the Greenian. The dual elements $a_i^\vee\in W^*$ satisfy $\sum_i a_i^\vee=0$. Under the centered identification,

$$
\mathcal C(a_i^\vee)=a_i-h,\qquad
h=\frac1n\sum_i a_i,\qquad
\mathcal C(Q_1)=\mathrm{Gr},\qquad
N=\mathcal C(D)=\exp(\mathrm{Gr})
$$

The direct vertices $a_i$ remain independent. The zero-sum relation concerns the dual elements or the centered vectors.

Let a forest $F$ have components $C_1,\ldots,C_{k+1}$, and set $a_C^\vee=\sum_{a_i\in C}a_i^\vee$. Its associated dual form is

$$
\Phi_{\pi(F)}=[a_{C_1}^\vee\cdots a_{C_k}^\vee]^2
$$

One block is omitted. Changing the omitted block or ordering the others changes the exterior argument only by a sign, so the form is well defined. For $k=0$, it equals $e$.

By the [[Cuts and Forest Grades of the Greenian Exponential#The forest formula for grades of the Greenian exponential|forest formula for dual grades]],

$$
\boxed{
Q_k=\frac1\tau
\sum_{\substack{F\subseteq E\text{ a forest}\\\#F=d-k}}
w(F)\Phi_{\pi(F)}
}
$$

Thus a single original forest with $g$ edges contributes to the direct grade $M_g$ and the dual grade $Q_{d-g}$. Its form and overall weight normalization change.

| Original forest data | In $M_g$ | In $Q_k$, where $k=d-g$ |
| --- | --- | --- |
| Edge count | $g$ | The same forest with $d-k$ edges |
| Component count | $n-g$ | $k+1$ |
| Form | Product of direct component boundaries | Form on the exterior product of dual block sums |
| Term weight | $w(F)$ | $w(F)/\tau$ |
| Weight sum in this representation | $f_g$ | $f_{d-k}/\tau$ |

This is why normalized forest parameters naturally relate to the Greenian: ratios of forest coefficients to $\tau$ already occur in its cut expression. Multiplying every conductance by $s>0$ multiplies $f_{d-k}/\tau$ by $s^{-k}$, just as for the grade $Q_k$ of the Greenian exponential. These coefficients have the dimensions of resistance to the $k$th power.

**Representation caveat.** The last row refers to the specified cut expansion. It is not the coefficient sum of every expression for $Q_k$. In the [[Cuts and Forest Grades of the Greenian Exponential#Uniqueness of the form and nonuniqueness of its expansion|$K_4$ example]], a structural identity changes this sum without changing the form.

If $T_n=[(a_1\ldots a_n)]^2$, mutual duality reads

$$
M_d=\tau T_n,\qquad
M_d/Q_k=M_{d-k},\qquad
Q_d/M_g=Q_{d-g}
$$

Here $/$ denotes exterior deletion, not numerical division or multiplication by an inverse polyform. The definition and proof appear in [[Laplacian and Greenian - Mutual Duality of Exponentials]].

The top coefficient depends on the chosen reference form. With $T_n^\vee=[a_1^\vee\cdots a_{n-1}^\vee]^2$,

$$
Q_d=\frac1\tau T_n^\vee,\qquad
N_d=\frac1{n^2\tau}T_n
$$

The factor $n^{-2}$ arises from the centered transfer $\mathcal C(T_n^\vee)=T_n/n^2$. Hence the coefficient $1/\tau$ in the dual vertex expression cannot be carried unchanged to the canonical boundary expression $N$.

## Canonical Greenian forests and their parameters

The Greenian also has a canonical vector expression in the direct space:

$$
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

It gives a second forest expansion:

$$
\begin{aligned}
N&=\prod_{i<j}\bigl(e+\gamma_{ij}[a_{ij}]^2\bigr)\\
&=\sum_{F\in\mathcal F(K_n)}
\left(\prod_{ij\in E(F)}\gamma_{ij}\right)[B_F]^2
\end{aligned}
$$

The sum runs over spanning forests of the complete set of pairs; zero coefficients remove absent couplings. The weight $\gamma_{ij}$ can have either sign and may be nonzero for a pair that is not an edge of the original graph.

This distinction already appears for the unit path on four vertices:

![[Path P4 - Laplacian and Signed Greenian Connections.svg]]

**Original and Greenian couplings.** The left panel shows conductances of the path $a-b-c-d$; the right shows the coefficients $\gamma_{ij}=-\mathrm{Gr}_{ij}$ in its canonical Greenian expression. The couplings $ac,ad,bd$ appear only on the right; the coefficients at $ab,cd$ equal $-1/8$. Yet edge resistances are positive and equal $1$, while $R_{ad}=3$. Thus $c_{ij}$, $\gamma_{ij}$, and $R_{ij}$ have different values and meanings. The layout is schematic: segment lengths do not represent $\sqrt{R_{ij}}$.

Forests in this expansion consist of Greenian couplings. They must not be identified with the original forests in the cut formula for $Q_k$: their weights and indexing differ. In one case, grade $k$ uses $k$ Greenian couplings; in the other, it uses $d-k$ original edges.

[[Toponomes of the Greenian Exponential and Dual Pairs]] defines the canonical forest polynomial $F_{\mathrm{Gr}}(t)=\sum_k f_{\mathrm{Gr},k}t^k$. Already its first coefficient is

$$
f_{\mathrm{Gr},1}=\sum_{i<j}\gamma_{ij}
=\frac12\operatorname{tr}\mathbf{Gr}
=\frac{Kf(G)}{2n},\qquad
Kf(G)=\sum_{i<j}R_{ij}
$$

It uses resistances between all pairs of vertices. In general, it is not an invariant of the original cycle matroid.

The two **rooted** forest polynomials satisfy exact coefficient reversal:

$$
P_L(t)=\det(\mathbf I+t\mathbf L),\qquad
P_{\mathrm{Gr}}(t)=\det(\mathbf I+t\mathbf{Gr})
$$

$$
P_{\mathrm{Gr}}(t)=\frac{t^d}{n\tau}P_L(1/t)
$$

The last expression is a polynomial identity after expansion. It follows from reciprocal nonzero spectra and $\prod_{i=1}^{d}\mu_i=n\tau$, where $\mu_i$ are the nonzero eigenvalues of $\mathbf L$. The forest interpretation of root weights and the proof appear in the [[Toponomes of the Greenian Exponential and Dual Pairs#The dual pair and reversal of spectral coefficients|section on spectral reversal]].

In a rooted polynomial, each forest weight is additionally multiplied by the product of its component sizes. These polynomials therefore differ from $F_G$ and $F_{\mathrm{Gr}}$. Spectral reversal does not imply $F_{\mathrm{Gr}}(t)=t^dF_G(1/t)/\tau$.

The two sides also differ in their normalized potentials. For affine vectors $u,v$ with coordinate columns $\mathbf u,\mathbf v$,

$$
P_M([u,v])=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v,\qquad
P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v
$$

The first formula gives the original resistance metric; the second gives the dual energy evaluation. The definition of $P$ and derivation of the second formula appear in [[The Greenian Metric and Potentials]]. Neither makes the evaluation of arbitrarily chosen vertex vectors a matroid parameter without further justification.

## Edge resistance as a link between the two sides

Quantities computed directly from the Green matrix can also be matroid parameters. What matters is how the argument is chosen and how the result relates to edge data.

Let $\ell=\{i,j\}$ be an **existing edge**. Write $R_\ell=R_{ij}$ for the effective resistance between its endpoints. It may differ from the conductor resistance $1/c_\ell$.

**Proposition.** For a connected graph with positive conductances,

$$
\boxed{
R_\ell=\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}
=\frac{\partial\log\tau}{\partial c_\ell}
}
$$

**Proof.** By the [[Variation of a Single Edge|conductance variation formula]],

$$
\tau(G;c_\ell+\delta)=\tau(G;c_\ell)(1+\delta R_\ell)
$$

Differentiation with respect to $\delta$ at zero proves the claim. $\square$

The spanning-tree polynomial is determined by matroid bases. Its derivative with respect to the variable of a matched edge, and hence $R_\ell$, is therefore preserved by a conductance-preserving isomorphism. If a spanning tree is sampled with probability proportional to its weight, then

$$
\eta_\ell=c_\ell R_\ell
=\frac{\sum_{T\ni\ell}w(T)}{\tau}
=\mathbb P(\ell\in T)
$$

The middle equality follows directly by differentiating the tree-weight sum. One quantity has three representations: a derivative of the spanning-tree polynomial, a Greenian evaluation, and an edge-inclusion probability.

For an arbitrary vertex pair, a matroid isomorphism supplies no corresponding pair: it matches edges. Thus the conclusion does not automatically extend to the entire matrix $\mathbf R$ or its vertex sums.

## One matroid, different vertex geometry

Consider the unit path $P_4$ with edges $ab,bc,cd$ and the unit star $K_{1,3}$ with edges $ab,ac,ad$. Both can be formed by gluing three separate edges at one vertex at each step.

Both matroids are free on three elements: every edge subset is independent. Their matroid isomorphism is therefore proved independently of the numerical coincidences below.

![[Path and Star Matroid - Edge Correspondence.svg]]

**Edge correspondence.** The labels $\ell_1,\ell_2,\ell_3$ specify a bijection: $ab\mapsto ab$, $bc\mapsto ac$, $cd\mapsto ad$. Every subset remains a forest. The vertex structure changes, so the sums of all pairwise resistances are $10$ and $9$, as computed below. This does not affect edge resistances: they equal $1$ in both unit trees.

| Characteristic | Path $P_4$ | Star $K_{1,3}$ |
| --- | --- | --- |
| Vertex degrees | $2,2,1,1$ | $3,1,1,1$ |
| Ordinary forest polynomial $F_G(t)$ | $1+3t+3t^2+t^3$ | $1+3t+3t^2+t^3$ |
| Two-edge forests: component sizes $3+1$ | $2$ | $3$ |
| Two-edge forests: component sizes $2+2$ | $1$ | $0$ |
| Rooted polynomial $P_L(t)$ | $1+6t+10t^2+4t^3$ | $1+6t+9t^2+4t^3$ |
| Kirchhoff index $Kf(G)$ | $10$ | $9$ |
| Canonical coefficient $f_{\mathrm{Gr},1}=Kf(G)/8$ | $5/4$ | $9/8$ |
| Weight sum of original 2-forests in the cut expression for $Q_1$: $f_2/\tau$ | $3$ | $3$ |
| Edge resistances | All equal $1$ | All equal $1$ |
| Resistance radius $\rho$ | $3/4$ | $3/4$ |

Ordinary forest coefficients count arbitrary subsets of three edges. For the rooted coefficient of grade two, the path gives $2\cdot3+1\cdot4=10$ and the star gives $3\cdot3=9$: the factors $3$ and $4$ count choices of roots in the components.

In a unit tree, effective resistance equals the number of edges in the unique path. The pair sum is $3\cdot1+2\cdot2+1\cdot3=10$ for $P_4$ and $3\cdot1+3\cdot2=9$ for the star. Both radii equal $3/4$ by the independently proved [[Vertex Contraction and Graph Gluing#Resistance radius is additive|tree-radius formula]].

The distinction is therefore not between “combinatorial Laplacian parameters” and “metric Greenian parameters”. Both objects have characteristics preserved by the matroid and characteristics using additional vertex information. In particular, the two different coefficient sums for $Q_1$ and its centered image must not be confused.

## What is preserved under one-point gluing?

Let $G=G_1\vee G_2$ under the assumptions in [[#From gluing to the question of invariants]]. A simple cycle cannot pass through both pieces, since it would have to revisit their only shared vertex. Hence $F\subseteq E(G)$ is a forest if and only if both $F\cap E(G_1)$ and $F\cap E(G_2)$ are forests.

This says that $\mathsf M(G)$ is the direct sum of the two matroids: independent sets are chosen independently in the pieces. Changing the vertices used for gluing does not change this condition. This explains why all weighted matroid parameters are preserved when such attachment points change.

The bijection between pairs of forests and multiplication of their weights separately give

$$
F_{G_1\vee G_2}(t)=F_{G_1}(t)F_{G_2}(t)
$$

Comparing leading coefficients proves multiplicativity of $\tau$. Additivity of $\rho$ has its own geometric proof in [[Vertex Contraction and Graph Gluing]]; it does not follow from the definition of matroid invariance alone.

With two or more shared vertices, cycles using edges of both pieces may occur. The argument above then no longer applies. For chains of cores, the gluing operation must be specified, the cycle correspondence checked, and shared vertices distinguished from identified shared edges.

## Polyform duality and matroid duality

Exterior duality $M_d/Q_k=M_{d-k}$ concerns forms on dual spaces. In the cut expression for $Q_k$, it uses the same independent sets of the original matroid, but of complementary size and with normalization $1/\tau$.

Matroids have a different duality operation: the bases of $\mathsf M(G)^*$ are the complements in $E$ of the bases of $\mathsf M(G)$. Its rank is therefore $\#E-d$, whereas the top grade of $D$ is $d$.

These constructions should not be identified. In particular, canonical Greenian couplings are not, by definition, elements of the dual matroid of the original graph. A connection with matroid duality requires a separate formulation and is not used in this note's proofs.

## Status of the results and continuation

The equivalence of forest and linear independence and the definitions of the cycle matroid, bases, and circuits belong to classical theory [1]. They are derived here in PMG exterior-algebra notation. The classical theory of graphs with identical cycle structure goes back to Whitney's work on 2-isomorphism [2]; its full transformation theorem is not needed for the proofs given here.

The note proves matroid invariance of ordinary forest coefficients and edge resistances, the direct-sum structure of one-point gluing, and the product law for forest polynomials. Dual forest formulas, spectral reversal, and metric identities are used with explicit links to their proofs in the library. The path and star are computed directly; equality of their radii does not replace a proof of matroid invariance of the radius for general graphs.

Six graphs were additionally checked in exact rational arithmetic: unit $P_4$, $K_{1,3}$, $C_4$, $K_4$, a triangle with conductances $1,2,3$, and a path with successive conductances $1,1/2,3$. The Greenian was obtained independently by matrix inversion on the zero-sum subspace and by summing original 2-forests after centering their block sums. Edge probabilities were checked against spanning-tree enumeration; rooted coefficients of both vector expressions were checked against spectral reversal. These checks supplement general proofs and verify normalizations.

The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_cycle_matroid.py) also compares acyclicity of every edge set with a nonzero exterior product computed from coordinate-matrix minors, and checks the independence axioms. It uses exact matrix routines from the adjacent verify_forest_power_sums.py; both files require only the Python standard library. Run from the repository root:

    python checks/matroid/verify_cycle_matroid.py

Forest-coefficient indexing, computation, and gluing convolutions are developed in [[Forest Coefficients - Grade, Components, and Corank]].

The families are developed separately in [[The Normalized Forest Polynomial and Power-Sum Parameters]], [[Forest Resistance Scales]], [[Edge Resistances and Random Spanning Trees]], and [[Resistance Radius - Forest Formula and Matroid Invariance]]. Their gluing laws and limitations are collected in [[Gluing and the Limits of Matroid Invariance]]. Formal factorization parameters of the ordinary forest polynomial are not identified with the spectrum of $\mathbf L$ or $\mathbf{Gr}$.

The graph-metric claims here concern connected undirected graphs with positive conductances. Extension to balanced graphs requires separate justification.

## References

1. Tutte W. T. *Lectures on Matroids*. Journal of Research of the National Bureau of Standards, Section B, 69B (1965), 1-47. [DOI: 10.6028/jres.069B.001](https://doi.org/10.6028/jres.069B.001). Classical exposition of matroids and their connection with graphs.
2. Whitney H. *2-Isomorphic Graphs*. American Journal of Mathematics, 55 (1933), 245-254. [DOI: 10.2307/2371127](https://doi.org/10.2307/2371127). The original source for graph 2-isomorphism.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Цикловой матроид и внешние произведения рёбер|Русская версия]].
