---
title: "Gluing and the Limits of Matroid Invariance"
date: 2026-10-28
updated: 2026-10-28
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: gluings-and-limits-of-matroid-invariance
lang: en
description: "One-point gluing laws, the Whitney twist, and changes of the chosen boundary. Two forest states, the roles of the Laplacian and Greenian, exact examples, and the transition to chains of cores."
order: 7
---

Matroid parameters separate properties of the parts of a graph from the way those parts are arranged when glued together. For one-point attachment this independence is complete: cycles remain within individual parts. With several shared vertices, cycles can pass through both parts, and one must keep track of how forests connect the boundary.

This question motivated the series in [[The Cycle Matroid and Exterior Products of Edges]]. We can now state gluing laws for the parameters constructed so far and distinguish precisely between two operations: interchanging two already chosen boundary vertices and choosing a different pair of vertices. The first preserves the cycle matroid; the second can change it.

## Assumptions and parameters

We consider finite connected undirected loopless graphs, each with at least two vertices. Conductances $c_\ell$ are positive. Parallel edges retain separate labels. When weighted matroids are compared, the edge correspondence must preserve their conductances.

For a graph on $n$ vertices, put $d=n-1$. The quantity $f_g$ is the sum of weights of ordinary spanning forests with $g$ edges; all isolated vertices are included, and no roots are chosen. Corank $k$ means $d-k$ edges and $k+1$ components. We use

$$
\tau=f_d,\qquad
F_G(t)=\sum_{g=0}^d f_g t^g,\qquad
\alpha_k=\frac{f_{d-k}}\tau,\qquad
\Phi_G(u)=\sum_{k=0}^d\alpha_k u^k
$$

Forest power-sum parameters and resistance scales are defined by

$$
\log\Phi_G(u)=\sum_{m\ge1}(-1)^{m-1}\frac{s_m^{\mathrm{for}}}m u^m,
\qquad
\xi_k=\frac{\alpha_k}{\alpha_{k-1}},\quad 1\le k\le d
$$

The edge family and resistance radius are

$$
\eta_\ell=c_\ell R_\ell,\qquad
H_q=\sum_\ell\frac{\eta_\ell^q}{c_\ell},\quad q\ge1,
\qquad
\rho=\frac13\xi_1-\frac1{12}H_2
\tag{1}
$$

Here $q$ is an integer, $R_\ell$ is the effective resistance between the endpoints of an existing edge, and $\rho=R_{\mathrm{sph}}^2$. Definitions and proofs are given in [[The Normalized Forest Polynomial and Power-Sum Parameters]], [[Forest Resistance Scales]], [[Edge Resistances and Random Spanning Trees]], and [[Resistance Radius - Forest Formula and Matroid Invariance]].

## What a prescribed gluing means

Start with two disjoint parts $G_1,G_2$, choose vertex sets of the same size in them, and specify a bijection between those sets. Identify only corresponding vertices. After this,

$$
V(G_1)\cap V(G_2)=U,\qquad
E(G)=E(G_1)\sqcup E(G_2)
\tag{2}
$$

There are no other shared vertices or additional identifications. Each edge retains its membership in a part and its weight. If two edges acquire the same endpoints, they remain parallel for now. This is the prescribed decomposition used in the [[Structural Identities and Graph Gluing#Gluing and a prescribed decomposition|polyform description of gluing]].

Conditions (2) are essential. Gluing along a shared edge subgraph while identifying its edges is a different operation; it is treated separately below.

## One-point gluing and the direct sum of matroids

Let $U=\{a\}$ and $G=G_1\vee G_2$.

**Proposition.** An edge set $I\subseteq E(G)$ is a forest if and only if both $I\cap E(G_i)$ are forests. Consequently, the cycle matroid of $G$ is the direct sum of the cycle matroids of the parts.

**Proof.** A cycle within a part remains a cycle in the whole graph. Conversely, a simple cycle cannot pass through both parts: to return, it would have to visit the sole shared vertex twice. Thus every cycle is contained in one part. This proves the independence criterion that defines the direct sum of matroids. $\square$

An ordinary forest of the resulting graph splits uniquely into two forests, its weight is the product of their weights, and their edge counts add. Therefore

$$
F_{G_1\vee G_2}(t)=F_{G_1}(t)F_{G_2}(t),\qquad
\tau(G_1\vee G_2)=\tau(G_1)\tau(G_2)
\tag{3}
$$

Since $d=d_1+d_2$, the same law holds in normalized corank notation:

$$
\Phi_{G_1\vee G_2}(u)=\Phi_{G_1}(u)\Phi_{G_2}(u)
\tag{4}
$$

### Summary of the laws

In the table, subscripts $1,2$ refer to the parts. Coefficients outside their allowed ranges are taken to be zero.

| Characteristic | Law under one-point gluing | Reason |
| --- | --- | --- |
| $\tau$ | $\tau=\tau_1\tau_2$ | A pair of trees of the parts gives a tree of the result |
| $F_G$, $\Phi_G$ | Product of polynomials | Weight-preserving bijection of forests |
| $f_g$ | $f_g=\sum_{a+b=g}f_{1,a}f_{2,b}$ | Edge counts add |
| $\alpha_k$ | $\alpha_k=\sum_{a+b=k}\alpha_{1,a}\alpha_{2,b}$ | Coranks add |
| $s_m^{\mathrm{for}}$ | $s_m^{\mathrm{for}}=s_{1,m}^{\mathrm{for}}+s_{2,m}^{\mathrm{for}}$ | Logarithm of the product in (4) |
| $\eta_\ell$, $R_\ell$ within a part | Unchanged | Independent choices of trees in the parts |
| $H_q$ | $H_q=H_{1,q}+H_{2,q}$ | Edge probabilities are preserved |
| $\xi_1$ | $\xi_1=\xi_{1,1}+\xi_{2,1}$ | Coefficient of $u$ in (4) |
| $\xi_k$, $k>1$ | Ratio of two convolutions, generally not a sum | Definition of adjacent-coefficient ratios |
| $\rho$ | $\rho=\rho_1+\rho_2$ | Formula (1) and its two additive terms |

For the higher scales, the exact expression is

$$
\xi_k(G_1\vee G_2)=
\frac{\sum_{a+b=k}\alpha_a(G_1)\alpha_b(G_2)}
{\sum_{a+b=k-1}\alpha_a(G_1)\alpha_b(G_2)}
$$

Matroid invariance of all these scalars was established independently of these laws. It does not turn a convolution into a sum or prove additivity by itself.

**Corollary.** If fixed parts are attached successively at exactly one vertex, every matroid parameter of the result is independent of the choice of attachment vertices. The pattern of these successive attachments can also be changed, provided each attachment remains a one-point attachment and creates no additional contacts. The resulting matroid is always the direct sum of the same matroids of the parts.

This statement does not require the parts to be identical or cyclic. At the same time, distances between vertices in different parts, centroidal characteristics, and spectra can depend on the assembly.

## Two-point gluing and the Whitney twist

Choose distinct vertices $a_1,b_1$ in $G_1$ and $a_2,b_2$ in $G_2$. Compare the two results:

$$
\begin{aligned}
G_{\parallel}:&\quad a_1\sim a_2,\quad b_1\sim b_2\\
G_{\times}:&\quad a_1\sim b_2,\quad b_1\sim a_2
\end{aligned}
\tag{5}
$$

The boundary pairs, the parts themselves, edge labels, and conductances remain fixed. The second assembly is called a *Whitney twist*, a classical operation associated with graph 2-isomorphism [1]. The following direct proof suffices here; the general classification theorem is not needed.

**Theorem.** The identity correspondence of edge labels in (5) preserves every cycle as an edge set. Thus $G_{\parallel}$ and $G_{\times}$ have the same weighted cycle matroid.

**Proof.** A simple cycle either lies wholly in one part or uses both parts. In the first case its edge set is unchanged. In the second, it splits into a path from $a_1$ to $b_1$ in the first part and a path from $a_2$ to $b_2$ in the second. The interiors of these paths are vertex-disjoint. After the endpoints are interchanged, the second path is traversed in reverse, and the same edges again form a simple cycle.

The twist is reversible, so the cycle correspondence works in both directions. Minimal dependent sets, and hence all independent sets, coincide. Weights are preserved along with edge labels. $\square$

The quantities $f_g$, $\tau$, $\Phi_G$, $s_m^{\mathrm{for}}$, $\xi_k$, all corresponding $\eta_\ell,R_\ell$, the family $H_q$, and the radius $\rho$ are preserved. These are equalities between two ways of gluing. They do not assert that the parameters of the glued graph are sums of the parameters of its parts.

### One matroid with different vertex geometry

Take the path $a_1-x-b_1$ with a leaf $p$ attached to $a_1$ as the first part. Take the path $a_2-y-b_2$ with a leaf $q$ attached to $a_2$ as the second. All six conductances equal $1$.

In the straight gluing, both leaves attach to the same vertex of the cycle $C_4$. After the twist, they attach to opposite vertices. The graphs are nonisomorphic: the first has a vertex of degree $4$, whereas the maximum degree of the second is $3$.

![[Whitney Twist - One Matroid and Different Geometry.svg]]

**Reading the figure.** Color identifies the original part; each label $\ell_i$ is preserved by the twist. The sole simple cycle in both graphs consists of $\ell_1,\ell_2,\ell_4,\ell_5$; $\ell_3,\ell_6$ are bridges. The attachment point of the leaf $q$ and the endpoint correspondence for edges of the second part change.

For both graphs, direct calculation gives

$$
F_G(t)=\bigl((1+t)^4-t^4\bigr)(1+t)^2
=1+6t+15t^2+20t^3+14t^4+4t^5
$$

$$
\tau=4,\qquad \xi_1=\frac72,\qquad H_2=\frac{17}4,
\qquad \rho=\frac{13}{16}
$$

Their vertex characteristics, however, differ:

| Characteristic | $G_{\parallel}$ | $G_{\times}$ |
| --- | --- | --- |
| $R_{pq}$ | $2$ | $3$ |
| $\mathrm{Kf}=\sum_{i<j}R_{ij}$ | $20$ | $21$ |
| $\operatorname{tr}\mathbf{Gr}=\mathrm{Kf}/6$ | $10/3$ | $7/2$ |
| $\operatorname{tr}(\mathbf L^2)$ | $42$ | $40$ |
| 2-forests by component type $(1+5,2+4,3+3)$ | $(11,2,1)$ | $(10,2,2)$ |

The first row follows from the two pendant edges in series and, in the second graph, resistance $1$ between opposite vertices of $C_4$. For the trace of the squared Laplacian, the identity $\operatorname{tr}(\mathbf L^2)=\sum_i\deg(i)^2+2|E|$ for a simple unit-weight graph suffices. The different traces prove that the Laplacian spectra differ. The values of $\mathrm{Kf}$ are obtained by summing pairwise resistances and are independently checked using $\mathbf L^+$.

The 2-forest counts come from direct enumeration. Their sum is $f_4=14$ in both cases, but the distributions by component size differ. Thus matroid invariance of the total forest sum does not extend to the full partition toponome. Summing over all choices of one root per component would multiply each forest weight by the product of its component sizes and give a different sum.

## Why changing the chosen pair is a different operation

The twist (5) preserves the chosen pair in each part. It does not permit replacing that pair by an arbitrary different pair.

Keep the parts $G_1=P_3$ and $G_2=P_4$ fixed, with all conductances equal to one. Mark both endpoints in $P_3$. In $P_4$, compare marking both endpoints with marking two vertices at distance two edges.

![[Boundary Choice - Cycle and Cycle with a Leaf.svg]]

**One part, two boundaries.** The top row shows two markings of the same path $P_4$; gold circles mark the chosen vertices. Below, the same two-edge path $P_3$ is attached to them. The results are $C_5$ and $C_4$ with one pendant edge.

| Result | $\tau$ | $\xi_1$ | $H_2$ | $\rho$ |
| --- | --- | --- | --- | --- |
| $C_5$ | $5$ | $2$ | $16/5$ | $2/5$ |
| $C_4$ with a leaf | $4$ | $5/2$ | $13/4$ | $9/16$ |

Both assemblies have five vertices and five edges. The parts, their matroids, and all their forest parameters are identical, but the resulting parameters differ. Already $\tau=5$ and $\tau=4$ rule out a matroid isomorphism. The sole cycle has five edges in the first graph and four in the second.

This also shows that the one-point laws fail: $\tau(P_3)\tau(P_4)=1$, whereas $\rho(P_3)+\rho(P_4)=1/2+3/4=5/4$. Neither value is the corresponding parameter of either two-point gluing.

## Two boundary states of an ordinary forest

The difference comes from the missing boundary marking. For a graph $X$ with distinguished vertices $a,b$, divide its ordinary forests into two classes:

$$
\begin{aligned}
F_X^{\mathrm{con}}(t)&=\sum_{\substack{F\text{ a forest in }X\\a,b\text{ connected in }F}}w(F)t^{|E(F)|}\\
F_X^{\mathrm{sep}}(t)&=\sum_{\substack{F\text{ a forest in }X\\a,b\text{ separated in }F}}w(F)t^{|E(F)|}
\end{aligned}
$$

Then $F_X=F_X^{\mathrm{con}}+F_X^{\mathrm{sep}}$. Other forest components, including those containing neither $a$ nor $b$, are allowed. No roots are chosen. The notation refers to the chosen pair, although that pair is omitted from the subscript.

For two parts satisfying (2) with exactly two shared vertices, compatibility is as follows:

| State in the first part | Second part: separated | Second part: connected |
| --- | --- | --- |
| Separated | Forest; boundary remains separated | Forest; boundary is connected |
| Connected | Forest; boundary is connected | Cycle; contribution excluded |

**Proposition.** In the grade variable $t$,

$$
\boxed{\begin{aligned}
F_G&=F_1^{\mathrm{sep}}F_2^{\mathrm{sep}}+F_1^{\mathrm{con}}F_2^{\mathrm{sep}}+F_1^{\mathrm{sep}}F_2^{\mathrm{con}}\\
&=F_1F_2-F_1^{\mathrm{con}}F_2^{\mathrm{con}}
\end{aligned}}
\tag{6}
$$

**Proof.** Restrictions of a forest of the result to the parts are forests. Conversely, the union of two forests creates a cycle exactly when both contain a path between the boundary vertices. The two paths then form a cycle; every cycle using both parts has precisely this form. In all other cases the union is acyclic. Edge counts add, weights multiply, and restriction to the parts is the inverse map. This proves (6) monomial by monomial. $\square$

There is no correction for the number of identified vertices in (6), because the exponent of $t$ counts edges. When passing to corank, one must account for $d=d_1+d_2-1$. Substituting the one-point law (4) here would be an error.

In the $P_4$ example, the full polynomial is the same: $F_{P_4}=(1+t)^3$. But for the two endpoints,

$$
F_{P_4}^{\mathrm{con}}=t^3
$$

whereas for vertices at distance two edges,

$$
F_{P_4}^{\mathrm{con}}=t^2(1+t)
$$

For $P_3$ with its endpoints marked, $F_{P_3}=(1+t)^2$ and $F_{P_3}^{\mathrm{con}}=t^2$. Thus (6) gives, respectively,

$$
F_{C_5}=(1+t)^5-t^5,
\qquad
F_{C_4\text{ with a leaf}}=(1+t)^5-t^4(1+t)
$$

This displays exactly the information lost by the full scalar forest polynomial of a part.

### The spanning-tree layer and boundary resistance

Let $\psi_X(a,b)$ be the sum of weights of ordinary 2-forests separating the chosen vertices. The [[Resistance Radius - Forest Formula and Matroid Invariance#Auxiliary forest sums with prescribed roots|formula for forests with prescribed roots]] gives

$$
\psi_X(a,b)=\tau_X R_{ab}^{X}
$$

Under two-point gluing, a tree of the result comes from a tree of one part and a separating 2-forest of the other. Hence

$$
\boxed{
\tau(G)=\tau_1\psi_2+\psi_1\tau_2
=\tau_1\tau_2\bigl(R_{a_1b_1}^{G_1}+R_{a_2b_2}^{G_2}\bigr)
}
\tag{7}
$$

This is also the highest nonzero coefficient of (6): the product of two spanning trees is excluded because it creates a cycle. In the $P_3,P_4$ example, the resistance of the first pair is $2$ and that of the second is $3$ or $2$. This gives $\tau=2+3=5$ or $\tau=2+2=4$.

The resistances in (7) concern distinguished vertex pairs in the original parts. Those pairs need not be edges; their resistances are not characteristics of the unmarked cycle matroid of a part. The spanning-tree layer (7) alone is insufficient to compute all of $F_G$.

## The Laplacian, the Greenian, and preserved scalars

After substituting common vertex names, the separate ownership of edges in (2) gives

$$
L_G=L_1+L_2,\qquad
M_G=\exp L_G=M_1M_2
\tag{8}
$$

This is an equality of full polyforms, valid for gluing at several points as well. The product retains vertex information; an edge set that forms a cycle gives a zero exterior product. This is why (8) is compatible with subtracting the incompatible class in the scalar formula (6). Multiplication of polyforms does not imply multiplication of scalar forest polynomials once boundary data have been discarded.

The other side of the duality is determined by the matrix $\mathbf{Gr}_G=\mathbf L_G^+$ and the exponential $N_G=\exp(\mathrm{Gr}_G)$. Taking a pseudoinverse is not linear; in general, (8) yields neither a sum of the Greenians of the parts nor a product of their exponentials. The centroid of the whole graph is also used, rather than two separate centroids.

[[The Greenian Metric and Potentials]] establishes the reciprocal metric evaluations

$$
P_M([u,v])=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v,
\qquad
P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v
$$

Ordinary forest coefficients have representations on both sides: in the vector forest expansion of $M$ and in the cut expansion of the dual grades of $N$. But preserving the sum of weights does not mean preserving the partition forms themselves or the entire vertex metric. Canonical Greenian forests with signed weights must also be distinguished from the original ordinary forests; this distinction is explained in the [[Forest Coefficients - Grade, Components, and Corank#Forest weights on both sides of duality|comparison of forest representations]].

The twist example displays both sides at once: the matroid coefficients and $\rho$ agree, whereas $\operatorname{tr}(\mathbf L^2)$ and $\operatorname{tr}\mathbf{Gr}$ differ. Thus Laplacian spectral parameters and reciprocal Greenian spectral parameters do not become matroid invariants by duality. The special combination defining the radius is matroid-invariant because of the separate forest formula (1).

## A shared seam and parallel conductors

If two cores have chosen seam edges, one must specify what happens to those edges. The distinction already matters for two unit-weight triangles.

![[Shared Edge - Three Different Gluing Laws.svg]]

**Three different graphs.** Vertices $a,b$ are identified in all three cases. On the left, both copies of $ab$ remain as parallel conductors; in the middle, they are identified as one edge of conductance $1$; on the right, both copies are deleted. The other four edges are the same.

| Operation on the copies of $ab$ | What remains at the seam | $\tau$ |
| --- | --- | --- |
| Keep both | Two parallel edges of conductance $1$ | $12$ |
| Identify as one unit-weight edge | One edge of conductance $1$ | $8$ |
| Delete both after identifying the vertices | No edge $ab$; $C_4$ remains | $4$ |

The first row satisfies (2), and (7) gives $3\cdot3\cdot(2/3+2/3)=12$. The other rows can be checked by counting trees: without the edge $ab$, the cycle has four trees; each tree containing $ab$ is completed by independently choosing one of two edges at each of the two remaining vertices. Thus a single edge $ab$ of conductance $c$ gives $\tau=4+4c$.

Combining two parallel unit conductors into one of conductance $2$ preserves the first network, its Laplacian, and the value $\tau=12$. It does not give the second row. The number of matroid elements changes, as explained in the [[Edge Resistances and Random Spanning Trees#Parallel conductors and the edge representation|discussion of the edge representation]].

Formulas (6)-(8) concern the first row of the table. The other two operations require recalculation: their edge sets differ. The term “two-point gluing” alone does not specify how seam edges are handled.

## What is needed for chains of cores

For successive one-point attachments, the invariance problem is already settled by the direct sum of matroids. With shared edges, long seams, or several contacts, one must separately prove preservation of the cycle matroid or compute the change in the parameters of interest.

Passing to chains of cores requires specifying:

- which vertices and edges are identified, which remain parallel, and which are deleted;
- the input and output boundaries of each core, their intersection, and whether additional contacts occur;
- the correspondence of edges and their weights when assemblies are compared;
- a justification that all cycles are preserved, rather than merely equality of a few numerical characteristics.

For a larger boundary, the two states in (6) do not suffice. A forest partitions the boundary vertices by its components. The full forest polynomial must also account for components that do not meet the boundary. For the spanning layer, *groves* arise naturally: spanning forests in which every component contains a boundary vertex. These objects and their boundary partitions are used in electrical network theory [2]. Their polyform encoding and the general gluing law form a separate continuation.

When an open chain is closed, the entire contact pattern must be checked again. Interchanging the endpoints of the final seam need not be a twist of the form (5): the two proposed parts may already meet at other vertices. In that case the proof using two boundary paths does not apply. A local change in a drawing is not synonymous with a matroid-preserving operation.

## Status of the results and verification

The direct sum under one-point gluing and the Whitney twist are classical matroid constructions. Here their proofs are given at the level of cycles, and consequences for PMG parameters are derived. The two-state formula (6) and its spanning-tree layer (7) are proved by a weight-preserving bijection. The examples involving leaves, boundary choices, and a shared edge are computed exactly; they do not replace general proofs.

The [exact verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/verify_gluing_invariance.py) performs 49 comparisons of one-point assemblies and 49 comparisons involving a Whitney twist. Each comparison checks the entire family of independent sets of labeled edges, followed by weighted coefficients, edge probabilities, four power-sum parameters, and $H_1,\ldots,H_4$. For two-point gluings it also checks boundary states and formulas (6)-(7). The radius is independently computed from the resistance matrix. The test set includes fractional weights and parallel edges; all numerical data in the three figures are checked separately.

Run from the repository root:

    python checks/matroid/verify_gluing_invariance.py

The three figures originate from the [SVG drawing script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/draw_gluing_figures.py); their English labels are reproduced by the [translation script](https://github.com/magin67/pmg-notes/blob/v5/checks/matroid/translate_figures_en.py). The figures show adjacency and the membership of edges in the parts; geometric lengths do not depict the resistance metric.

A weight-preserving matroid correspondence provides a general sufficient criterion for preservation of the scalars studied here. The converse is false: equality of several parameters, or even of the entire scalar forest polynomial, does not prove a matroid isomorphism; a counterexample appears in the [[The Normalized Forest Polynomial and Power-Sum Parameters#What can be recovered and what remains undetermined?|section on completeness of the forest family]]. Computation under gluing requires a separate composition law.

A full classification of gluings along arbitrary seams, boundary polyforms, and isomers of chains of cores is not claimed to be complete here. All results concern undirected graphs with positive conductances; no extension to balanced graphs is made.

## References and connections

1. Whitney H. *2-Isomorphic Graphs*. American Journal of Mathematics **55** (1933), 245-254. [DOI: 10.2307/2371127](https://doi.org/10.2307/2371127). The classical source on graph 2-isomorphism; the twist used here is proved directly in the text.
2. Kenyon R. W., Wilson D. B. *Boundary Partitions in Trees and Dimers*. Transactions of the American Mathematical Society **363** (2011), 1325-1364. [arXiv:math/0608422](https://arxiv.org/abs/math/0608422), [DOI: 10.1090/S0002-9947-2010-04964-5](https://doi.org/10.1090/S0002-9947-2010-04964-5). Groves and boundary partitions; this paper treats circular planar networks. Formulas (6)-(7) above are proved without a planarity assumption.
3. [[Vertex Contraction and Graph Gluing]]: geometric operations, one-point gluing, and additivity of the radius.
4. [[Structural Identities and Graph Gluing]]: prescribed decomposition, boundary data, and spanning-tree pairing.
5. [[The Greenian Metric and Potentials]] and [[Resistance Radius - Forest Formula and Matroid Invariance]]: reciprocal metric evaluations and the matroid formula for the radius.

Series navigator: [[en/Matroid parameters and forest characteristics of graphs/Matroid Parameters and Forest Characteristics of Graphs|Matroid Parameters and Forest Characteristics of Graphs]].

Russian edition: [[ru/Матроидные параметры и лесные характеристики графов/Сочленения и границы матроидной инвариантности|Русская версия]].
