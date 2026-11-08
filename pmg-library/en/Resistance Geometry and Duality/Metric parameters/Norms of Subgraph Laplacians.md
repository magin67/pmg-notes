---
title: Norms of Subgraph Laplacians
date: 2026-11-04
updated: 2026-11-08
revision: 2
translated_revision: 2
status: draft
text_prepared_by: ChatGPT
translation_key: norms-of-subgraph-laplacians
lang: en
description: "The norm of an internal Laplacian in the metric of the whole graph: spanning-tree interpretation, trees and blocks, partitions, sensitivity, partial observations, and comparison with boundary and Greenian norms."
order: 8
---

For each group of vertices, we can select its internal couplings and evaluate their Laplacian in the metric of the whole graph. The result is dimensionless: the expected number of internal edges of the group in a random spanning tree. It allows groups to be compared, but differs from density, geometric volume, and criticality under deletion.

The underlying edge formula is proved in [[Edge Resistances and Random Spanning Trees]]. Here it is applied to subgraph Laplacians. The norm means the [[Laplacian Exponential#The potential of a form|normalized potential of a form]], rather than a matrix norm or the square root of a numerical evaluation.

The main route covers the norm in a fixed metric, its spanning-tree meaning, small examples, and partitions. The sections on observations, boundaries, the Greenian, and maximum-norm groups are applications that can be read separately.

## The internal Laplacian and a fixed metric

Let $G=(V,E)$ be a finite connected undirected loopless graph, with $n=|V|\ge2$. Existing couplings have positive conductances; absent couplings have $c_{ij}=0$. Parallel conductors are first combined by summing their conductances. Set

$$
a_{ij}=a_j-a_i,\qquad
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
M=\exp L,\qquad
\mathbf{Gr}=\mathbf L^+
$$

Throughout this note, resistances $R_{ij}=a_{ij}^2$ are computed in the metric of the original graph $G$, unless explicitly stated otherwise. For a form $F$, write its norm as

$$
N_L(F)=\frac{\tau(F\exp L)}{\tau(\exp L)}
$$

Here $\tau(F)$ extracts the coefficient of a fixed top form, and $\tau(G)=\tau(\exp L)$ is the graph's spanning-tree coefficient.

> [!info] The norm of the internal Laplacian
> **Definition.** For nonempty $S\subseteq V$, the internal Laplacian and its norm are
>
> $$
> L_S=\sum_{\substack{i<j\\i,j\in S}}c_{ij}[a_{ij}]^2,\qquad
> \boxed{\mu_G(S)=N_L(L_S)=
> \sum_{\substack{i<j\\i,j\in S}}c_{ij}R_{ij}}
> \tag{1}
> $$

This is the Laplacian of the induced subgraph $G[S]$, regarded as a form in the original space. Its matrix is extended by zeros outside $S$, and its diagonal includes only internal couplings. It differs from the principal submatrix $\mathbf L_{S,S}$, whose diagonal also retains couplings to external vertices.

> [!note]- Matrix verification
> **Proof.** The norm of a grade-one form with symmetric coefficient matrix $\mathbf A$ is $\operatorname{tr}(\mathbf A\mathbf{Gr})$. For the coordinate column $\mathbf b_{ij}$ of $a_{ij}$, we have $R_{ij}=\mathbf b_{ij}^{\mathsf T}\mathbf{Gr}\mathbf b_{ij}$. Substituting $\mathbf L_S=\sum_{i<j,\ i,j\in S}c_{ij}\mathbf b_{ij}\mathbf b_{ij}^{\mathsf T}$ gives
>
> $$
> \mu_G(S)=\operatorname{tr}(\mathbf L_S\mathbf{Gr})
> $$
>
> The product here is matrix multiplication, not the polyform product. $\square$

In (1), **the metric is not recomputed from the subgraph**. If a connected $G[S]$ is considered separately and its Laplacian is evaluated in its own metric, the result is always $|S|-1$. For disconnected $G[S]$, a single resistance metric on all its vertices is not defined in the sense of the PMG core; norm (1) in the connected larger graph remains defined.

The product $c_{ij}R_{ij}$ is dimensionless. Multiplying all conductances of the larger graph by $t>0$ divides resistances by $t$, leaving $\mu_G(S)$ unchanged. For a single vertex, $L_S=0$ and $\mu_G(S)=0$.

## Spanning-tree interpretation and bounds

Choose a random spanning tree $\mathcal T$ of the original graph with distribution

$$
\mathbb P(\mathcal T=T)=\frac{w(T)}{\tau(G)},\qquad
w(T)=\prod_{ij\in T}c_{ij}
$$

With unit conductances, all spanning trees are equally likely. Kirchhoff's formula gives $\mathbb P(ij\in\mathcal T)=c_{ij}R_{ij}$; see [[Edge Resistances and Random Spanning Trees#Kirchhoff's formula in three representations|three representations of the edge formula]] and [1, §13.5, Theorem 13.5.1].


### Counting across the triangle's three spanning trees

The unit triangle has three equally likely spanning trees. Edge $ab$ occurs in two of them. For $S=\{a,b\}$, the internal edge counts are $1,1,0$, so

$$
\mu_G(\{a,b\})=\frac{1+1+0}{3}=\frac23=c_{ab}R_{ab}
$$

For the entire triple, each spanning tree has two internal edges, giving norm $2$. The probability that the triple is internally connected in the tree is $1$. Expected edge count and connectivity probability are different quantities.

![Edge $ab$ occurs in the first two spanning trees and is absent from the third](<images/Three Spanning Trees of a Triangle.svg>)

*Edge $ab$ occurs in the first two spanning trees and is absent from the third. All three trees are equally likely. This computes the pair norm directly, without matrix inversion.*

> [!info] Internal edges of a random spanning tree
> **Corollary of Kirchhoff's formula.** Let $K_S$ count the edges of $\mathcal T$ with both endpoints in $S$, and let $\kappa(\mathcal T[S])$ count the components of the induced forest, including isolated vertices. Then
>
> $$
> \boxed{\mu_G(S)=\mathbb E K_S
> =|S|-\mathbb E\,\kappa(\mathcal T[S])}
> \tag{2}
> $$
>
> In particular,
>
> $$
> 0\le\mu_G(S)\le |S|-\kappa(G[S])\le |S|-1
> \tag{3}
> $$

> [!note]- Proof
> **Proof.** The number $K_S$ is the sum of the inclusion indicators for internal edges. Linearity of expectation and the edge formula give (2). An induced subgraph of a tree is a forest, so $K_S=|S|-\kappa(\mathcal T[S])$. Each of its components lies within a component of $G[S]$, hence $\kappa(\mathcal T[S])\ge\kappa(G[S])$. $\square$

With positive conductances, $\mu_G(S)=0$ if and only if the group has no internal edges. The upper bound $|S|-1$ is attained if and only if **every** spanning tree connects $S$ by internal edges: every spanning tree has positive probability.

Thus, for a fixed group size, a larger norm means fewer components on average within a random spanning tree. This characterizes internal couplings in the context of the whole graph. It is neither the probability that the group is connected nor a direct measure of its number of edges.

Groups of different sizes can be compared using $\mu_G(S)/(|S|-1)$ for $|S|\ge2$, but this merely normalizes the upper bound. It does not remove all size effects: in a complete graph with equal conductances, $k=|S|$ gives $\mu_G(S)=k(k-1)/n$, and the normalized value is $k/n$.

## Trees, a cycle, and one-point gluing

### Trees

> [!info] In a tree, the norm counts internal edges
> **Corollary.** If the whole graph $G$ is a tree with arbitrary positive conductances, then
>
> $$
> \boxed{\mu_G(S)=|E(G[S])|=|S|-\kappa(G[S])}
> \tag{4}
> $$

> [!note]- Proof
> **Proof.** A tree has only one spanning tree: itself. Alternatively, $R_{ij}=1/c_{ij}$ for each of its edges, so every internal contribution in (1) equals one. $\square$

For four selected vertices:

| Component sizes in the induced subgraph | Number of components | Norm |
|---|---:|---:|
| $4$ | 1 | 3 |
| $3+1$ or $2+2$ | 2 | 2 |
| $2+1+1$ | 3 | 1 |
| $1+1+1+1$ | 4 | 0 |

These are possible types, not a claim that every type occurs in every tree. In the unit-conductance path with consecutive vertices $a,b,c,d,e$, the group $\{a,b,d,e\}$ consists of two separate edges and has norm $2$.

Every connected group of $k$ vertices in a tree has the maximum norm $k-1$. A maximum therefore neither guarantees density nor identifies a unique clustering structure.

### A triangle and a square

In a unit-conductance triangle, each edge contributes $2/3$. A pair has norm $2/3$, and the whole triangle has norm $2$.

In a unit-conductance cycle on four vertices, each edge contributes $3/4$. An adjacent pair has norm $3/4$, an opposite pair has norm $0$, every triple has norm $3/2$, and the whole cycle has norm $3$. In particular, the induced subgraph on a triple is connected, but some spanning trees connect its vertices through the fourth vertex.

### Two triangles with a common vertex

Let the graph consist of unit-conductance triangles $hab$ and $hcd$, glued only at $h$. Every edge retains resistance $2/3$. Each spanning tree contains two edges from each triangle.

![Three types of triples in two triangles with a common vertex](<images/Subgraph Laplacian Norms - triples in two triangles.svg>)

Selected vertices and their internal edges are blue. The three panels represent all types of triples; gray couplings remain in the larger graph and contribute to its metric.

| Type of triple | Example | Number of such triples | Norm |
|---|---|---:|---:|
| One of the original triangles | $\{h,a,b\}$ | 2 | $2$ |
| The common vertex and one vertex from each triangle | $\{h,a,c\}$ | 4 | $4/3$ |
| A triple without the common vertex | $\{a,b,c\}$ | 4 | $2/3$ |

Exactly the two original triples maximize the norm. They are biconnected blocks, not connected components: the whole graph is connected. These groups overlap at $h$ and do not partition the vertices.

The more general result is the local Foster formula: over the vertices and edges of an entire biconnected block, the sum of $c_{ij}R_{ij}$ equals its number of vertices minus one [2, Theorem 2.8]. The reason is that every spanning tree restricts to a tree on the block. Bridges satisfy the same law as two-vertex blocks. Attaining the upper bound does not itself mean that the selected group is one maximal block: a connected union of several entire blocks can attain it as well.

## Partitions and sensitivity of the spanning-tree coefficient

For disjoint $A,B$, define the contribution of couplings between them:

$$
\mu_G(A,B)=\sum_{i\in A,\ j\in B}c_{ij}R_{ij}
$$

Linearity gives

$$
\mu_G(A\cup B)=\mu_G(A)+\mu_G(B)+\mu_G(A,B)
$$

For a partition $V=S_1\sqcup\cdots\sqcup S_q$, we obtain

$$
\boxed{\sum_{\alpha=1}^q\mu_G(S_\alpha)
+\sum_{\alpha<\beta}\mu_G(S_\alpha,S_\beta)=n-1}
\tag{5}
$$

The right-hand side is the norm of the full Laplacian. The sum of within-group norms alone depends on the partition. If instead the edge set is partitioned into disjoint parts and every edge is counted exactly once, the sum of their norms is always $n-1$. In the two-triangle example, the sum $2+2=4$ is valid precisely because the edge sets are disjoint despite the shared vertex.

Now multiply the group's internal conductances by $1+t$, leaving all others unchanged, with $t>-1$. Denote the resulting graph by $G_t$.

> [!info] Relative sensitivity
> **Corollary of the edge variation formula.**
>
> $$
> \boxed{\left.\frac{d}{dt}\log\tau(G_t)\right|_{t=0}
> =\mu_G(S)}
> \tag{6}
> $$

> [!note]- Proof
> **Proof.** The [[Edge Resistances and Random Spanning Trees#Differentiating the spanning-tree polynomial|derivative formula]] gives $\partial\log\tau/\partial c_{ij}=R_{ij}$. The derivatives $dc_{ij}/dt$ equal $c_{ij}$ for internal couplings and zero otherwise. The chain rule gives (6). Equivalently, each spanning-tree weight is multiplied by $(1+t)^{K_S}$, and the derivative of the normalized spanning-tree sum equals $\mathbb E K_S$. $\square$

Weakening all internal conductances by a small fraction $\varepsilon$ decreases the spanning-tree coefficient by a relative fraction $\varepsilon\mu_G(S)+O(\varepsilon^2)$. This changes the weighted spanning-tree coefficient; the number of combinatorially possible spanning trees remains unchanged while weights stay positive.

### Why this is not criticality under vertex deletion

In the unit-conductance path on seven consecutively numbered vertices, the groups $\{1,2,3\}$ and $\{3,4,5\}$ have the same maximum norm $2$. Deleting the first leaves a connected path; deleting the second leaves two separate edges. The spanning-tree coefficients of the remaining graphs are $1$ and $0$, respectively.

Even a single vertex has zero internal norm, yet it may be an articulation point. Thus (6), which concerns changes to internal conductances, cannot be transferred to deletion of the group together with all incident couplings. These operations are also distinguished in [[Vertex Deletion - Spanning-Tree Coefficient and Resistance Radius]].

## What resistances on observed vertices determine

Suppose only a finite set $B$ is observed, while couplings and other vertices are unknown. All pairwise resistances on $B$ determine its metric, but generally do not determine the internal Laplacian of the original network.

For example, the same observed resistances $R_{ab}=R_{ac}=R_{bc}=2/3$ arise in two networks:

| Network | Couplings | Actual internal Laplacian norm of $abc$ |
|---|---|---:|
| Triangle | Three conductances of $1$ between observed vertices | $2$ |
| Star with hidden center $d$ | Conductances $ad,bd,cd$ are $3$ | $0$ |

![Both networks give resistance $2/3$ between observed vertices $a,b,c$](<images/A Triangle and a Hidden Center.svg>)

*Both networks give resistance $2/3$ between observed vertices $a,b,c$. All triangle edges are internal to the observed triple; every star edge leads to hidden vertex $d$. Thus the actual norms are $2$ and $0$, although the observed triple has the same metric.*

Nevertheless, these resistances uniquely determine an effective graph on $B$. For $m=|B|$, its matrices are recovered as

$$
\mathbf J_B=\mathbf I-\frac1m\mathbf1\mathbf1^{\mathsf T},\qquad
\mathbf{Gr}^{(B)}=-\frac12\mathbf J_B\mathbf R_B\mathbf J_B,\qquad
\mathbf L^{(B)}=(\mathbf{Gr}^{(B)})^+
\tag{7}
$$

This is the resistance description of [[Vertex Elimination and Induced Couplings|Kron reduction]]. Effective conductances incorporate paths through hidden vertices. Reconstruction from resistances and preservation of resistances under reduction are described in [3, Theorem III.8 and Lemma III.10].

The full effective Laplacian on $B$ has norm $m-1$. It does not reveal which part of its conductances came from direct couplings in the original network.

### Enlarging the observed set

Suppose an additional vertex $d\notin B$ is now observed, with the previous resistances unchanged. Write the conductances of the effective graphs on $B$ and $B\cup\{d\}$ as $c^{(B)}_{ij}$ and $c^{(B+d)}_{ij}$, respectively. Set

$$
q_d=\sum_{i\in B}c^{(B+d)}_{id}>0
$$

A one-step Schur complement gives [3, equation (16) and Lemma III.3]

$$
c^{(B)}_{ij}
=c^{(B+d)}_{ij}
+\frac{c^{(B+d)}_{id}c^{(B+d)}_{jd}}{q_d}
$$

> [!info] A fixed group's norm under enlarged observations
> **Corollary of Kron reduction.** For fixed $S\subseteq B$, the internal Laplacian norms in the two effective graphs satisfy
>
> $$
> \boxed{\mu_B(S)-\mu_{B+d}(S)
> =\frac1{q_d}
> \sum_{\substack{i<j\\i,j\in S}}
> c^{(B+d)}_{id}c^{(B+d)}_{jd}R_{ij}\ge0}
> \tag{8}
> $$

> [!note]- Proof
> **Proof.** Reduction preserves resistances. Multiply the conductance difference by $R_{ij}$ and sum over internal pairs of $S$. Every term is nonnegative. For distinct vertices, $R_{ij}>0$, so the decrease is strict if and only if $d$ is coupled to at least two vertices of $S$ in the new effective graph. $\square$

In the star example, revealing the center $d$ changes the triple's norm from $2$ to $0$. Its metric is unchanged, but the evaluated form changes. Eliminating $d$ again restores the previous norm $2$.

## Difference from the norm of a triple's boundary

For $S=\{a,b,c\}$, the form $[(abc)]^2$ has grade $2$, whereas $L_S$ has grade $1$. By the [[Metric of Higher-Grade Objects#Norm and volume|Gram determinant]], its norm is

$$
\nu_G(S)=N_L([(abc)]^2)
=R_{ab}R_{ac}
-\left(\frac{R_{ab}+R_{ac}-R_{bc}}2\right)^2
$$

It has the physical dimension of resistance squared and equals the squared area of the parallelogram on $(ab),(ac)$ in the resistance realization. Its definition requires no internal couplings.

For the unit-conductance path with edges $ab,bc,cd,de$:

| Triple | $\mu_G(S)$ | $\nu_G(S)$ |
|---|---:|---:|
| $\{a,b,c\}$ | $2$ | $1$ |
| $\{a,b,d\}$ | $1$ | $2$ |
| $\{a,c,e\}$ | $0$ | $4$ |

There is no direct monotone correspondence. There is, however, an exact relation. For the triple's internal spanning-tree coefficient

$$
t_S=c_{ab}c_{ac}+c_{ab}c_{bc}+c_{ac}c_{bc}
$$

we obtain

$$
\frac{L_S^2}{2}=t_S[(abc)]^2,\qquad
N_L\left(\frac{L_S^2}{2}\right)=t_S\nu_G(S)
\tag{9}
$$

The number $t_S\nu_G(S)$ is the probability that a random spanning tree connects the triple by internal edges. The first norm $\mu_G(S)$ is the expected number of these edges, not that probability.

> [!note]- Deriving the probabilistic interpretation
> **Proof.** The product of the forms of any two distinct sides of the triple is $[(abc)]^2$, while each vector form has zero self-product. This gives the first equality in (9). Multiplying the internal conductances by $1+s$ gives two expressions for the spanning-tree sum:
>
> $$
> \frac{\tau(G_s)}{\tau(G)}
> =\mathbb E(1+s)^{K_S}
> =1+s\mu_G(S)+s^2t_S\nu_G(S)
> $$
>
> Here we used commutativity of exponentials and $L_S^3=0$. Since $K_S$ takes only the values $0,1,2$, the coefficient of $s^2$ is $\mathbb P(K_S=2)$. This is a special case of the determinantal edge-inclusion formulas [5, Theorem 1.1]; the weighted version here is derived directly. $\square$

The norm of the product in (9) cannot be replaced by the product of norms: generally, $N_L(L_S^2)\ne N_L(L_S)^2$.

## Comparison with the internal part of the Greenian

In the [[The Canonical Vector Representation of the Greenian|canonical representation]], set

$$
\mathrm{Gr}_S=\sum_{\substack{i<j\\i,j\in S}}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij}
$$

These are the Greenian coefficients of the same whole graph. This is not a Greenian reconstructed from the isolated $G[S]$ or from the centered resistance matrix on $S$ alone.

Evaluate each partial form in the metric of its own full exponential. For $N=\exp(\mathrm{Gr})$, define $N_{\mathrm{Gr}}(F)=\tau(NF)/\tau(N)$. The [[The Greenian Metric and Potentials#The Laplacian as the metric of the Greenian exponential|Greenian metric identity]] gives

$$
\mu_{\mathrm{Gr}}(S)=N_{\mathrm{Gr}}(\mathrm{Gr}_S)
=\sum_{\substack{i<j\\i,j\in S}}
\gamma_{ij}(d_i+d_j+2c_{ij})
\tag{10}
$$

Here $d_i=\sum_{j\ne i}c_{ij}$ is the weighted degree in the original graph. The norm $\mu_{\mathrm{Gr}}(S)$ is also dimensionless. For the whole vertex set, both norms equal $n-1$, but on subsets even their signs may differ:

| Group in the unit-conductance path with edges $ab,bc,cd$ | $\mu_G(S)$ | $\mu_{\mathrm{Gr}}(S)$ |
|---|---:|---:|
| $\{a,b\}$ | $1$ | $-5/8$ |
| $\{a,d\}$ | $0$ | $5/4$ |
| $\{a,b,c\}$ | $2$ | $5/4$ |
| $\{a,b,d\}$ | $1$ | $7/4$ |
| $\{a,b,c,d\}$ | $3$ | $3$ |

For example, $\gamma_{ab}=-1/8$ and $d_a+d_b+2c_{ab}=5$. Negativity concerns evaluation of a form with a negative coefficient; the norms of nonzero vectors themselves in the metric of $N$ are positive.

The spanning-tree expansion for coefficients $\gamma_{ij}$ is signed, as shown in the [[The Canonical Vector Representation of the Greenian#Signed forest grades|Greenian forest expansion]]. The formula for the mean number of internal edges remains algebraically valid with weights $\prod_{ij\in T}\gamma_{ij}$, but with negative weights it is not a probabilistic expectation. If every $\gamma_{ij}\ge0$, the usual probabilistic interpretation applies to the Greenian graph, not to the original graph.

The relative-sensitivity interpretation always remains valid. For $\sigma(t)=\tau(\exp(\mathrm{Gr}+t\mathrm{Gr}_S))$, differentiation gives $\sigma'(0)/\sigma(0)=\mu_{\mathrm{Gr}}(S)$. This changes the Greenian's own internal coefficients, rather than the internal conductances of the original Laplacian.

The mixed evaluation $N_L(\mathrm{Gr}_S)$ concerns a different question and is not used in (10). In particular, $N_L(\mathrm{Gr})=\operatorname{tr}(\mathbf{Gr}^2)$ is not the Greenian norm in the metric of its own exponential.

## Finding a group of maximum norm

In a fixed graph, it suffices to compute the weights $w_{ij}=c_{ij}R_{ij}$ once. Finding a group of prescribed size $k$ then takes the form

$$
\max_{\substack{S\subseteq V\\|S|=k}}
\sum_{\substack{i<j\\i,j\in S}}w_{ij}
$$

This is a special case of the weighted densest subgraph problem with prescribed size [6]. For a pair, choose a maximum-weight edge; for small $k$, enumeration is feasible. Exact branch-and-bound methods discard extensions that cannot improve the current value. Greedy addition and vertex swaps are heuristics without a general guarantee of optimality.

Optimal groups of different sizes need not be nested. In two unit-conductance triangles joined by a bridge, the best pair consists of the bridge endpoints and has norm $1$. The best triples are the triangles themselves, with norm $2$; a triple containing both bridge endpoints has norm $5/3$.

In a tree, any connected group of the required size suffices. In any graph, attaining $k-1$ proves optimality. NP-hardness of the general problem with arbitrary weights [6] does not by itself establish NP-hardness for the special class $w_{ij}=c_{ij}R_{ij}$; no separate complexity claim for that class is made here.

## Sources, status, and verification

The main statements follow from established edge, spanning-tree, and determinantal formulas. Selecting the internal Laplacian as the evaluated form, comparing the two norms, and choosing the examples serve the exposition in PMG language; no claim of scientific novelty is made.

| Result | Basis | Role in this note |
|---|---|---|
| Spanning-tree interpretation and norm bounds | Kirchhoff's formula and forest edge counts | A group characteristic in a fixed metric |
| Trees and biconnected blocks | Uniqueness of the spanning tree; local Foster formula [2] | Exact extremal cases |
| Additivity and sensitivity | Linearity of the norm; derivative of the spanning-tree coefficient | Partitions and internal-coupling changes |
| Decrease under enlarged observations | Schur complement [3] | Distinguishing the metric from effective coefficients |
| Comparison with a triple's boundary | Gram determinant; second coefficient of the spanning-tree sum | Distinguishing grades and statistics |
| Comparison with the Greenian | The two metrics in the published series; signed forest sums | Limits of the probabilistic interpretation |

The [exact-arithmetic verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/metric-parameters/verify_subgraph_norms.py) compares matrix calculations through pseudoinversion with independent spanning-tree enumeration. It checks all subsets of selected small graphs, the example tables, cofactor variation, Kron reduction, the second grade of a triple, and the signed spanning-tree interpretation of the Greenian. These checks verify calculations but do not replace the proofs above.

### Beyond the finite model

Non-identifiability persists for infinite networks: an infinite ray of unit resistances can be attached at $a$ in each example without changing the measurements. However, the main theory of this note is finite-dimensional. For a general infinite network, the definition of resistance and the boundary condition at infinity must be fixed; free and wired conditions may differ [4, §2]. The finite expression $\sum c_{ij}R_{ij}$ does not require a formal exponential of the whole infinite graph.

### Sources

1. Spielman D. A. [Spectral and Algebraic Graph Theory](https://www.cs.yale.edu/homes/spielman/sagt/sagt.pdf). Author's version dated April 2, 2025, §13.5, Theorem 13.5.1: edge-inclusion probability in a random spanning tree.
2. Devriendt K. [Graphs with Nonnegative Resistance Curvature](https://doi.org/10.1007/s00026-025-00774-x). *Annals of Combinatorics*, 30 (2026), 415-438; Theorem 2.8: the local Foster formula.
3. Dörfler F., Bullo F. [Kron Reduction of Graphs with Applications to Electrical Networks](https://motion.me.ucsb.edu/pdf/2011d-db.pdf). Author's version; equation (16), Lemma III.3, Theorem III.8, and Lemma III.10: Schur complements, preservation and reconstruction of resistance data.
4. Weihrauch T., Bachmann S. [On the Probabilistic Representation of the Free Effective Resistance of Infinite Graphs](https://doi.org/10.1007/s10959-022-01218-5). *Journal of Theoretical Probability*, 36 (2023), 1956-1971; §2: free resistances of infinite networks.
5. Burton R., Pemantle R. [Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances](https://arxiv.org/html/math/0404048v1). *Annals of Probability*, 21 (1993), 1329-1371; Theorem 1.1: the determinantal formula for joint edge inclusion.
6. Borgwardt S., Schmiedl F. [Threshold-based preprocessing for approximating the weighted dense k-subgraph problem](https://doi.org/10.1016/j.ejor.2013.09.027). *European Journal of Operational Research* (2014): the weighted subgraph problem with prescribed size.

Further study of polyform functions, their series, and possible transforms is a separate topic. Here the exponential is used only to define the norm and finite variation identities.
