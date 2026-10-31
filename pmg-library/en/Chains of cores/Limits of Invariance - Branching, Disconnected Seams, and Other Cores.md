---
title: "Limits of Invariance: Branching, Disconnected Seams, and Other Cores"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: limits-of-invariance-branching-seams-and-other-cores
order: 4
description: "Trees of cycles and the limits of invariance for disconnected seams, other cores, and changes of gluing scheme."
---

Russian version: [[ru/Цепи из ядер/Границы инвариантности - ветвление, несвязные швы и другие ядра|Границы инвариантности: ветвление, несвязные швы и другие ядра]].

Identical cores and identical seam sizes do not by themselves determine the parameters of an assembled graph. For an open chain of cycles, invariance has a specific mechanism: fixed ordered data determine one dual multigraph and one cycle matroid. When the construction changes, this mechanism must be checked again.

The proof in [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]] assumes connected seams, no additional contacts, and disjoint input and output seams. Here we first extend it to a fixed tree of cycles, then examine changes to the gluing scheme, disconnected seams, and replacement of cycles by other cores. The final identification of boundaries is considered separately in [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain - Rings and the Möbius Effect]].

> [!note] Origins and status of the results
> For polygon chains with single-edge gluings, independence of the spanning-tree count from seam placement and its explanation through dual graphs are given by [Chen–Mohar, §3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). The tree-of-cycles theorem below applies the same mechanism under explicit conditions. The radius consequence uses the [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|forest formula for the radius]], based on the identity of [Richman–Shokrieh–Wu, Theorem C / 5.7](https://arxiv.org/html/2308.03859v1). The other tables contain directly verified examples; the Cartesian-product formula follows from standard Laplacian spectral properties and the matrix-tree theorem. No priority is claimed for the examples or constructions.

## Which data are being compared

The assembled graphs are finite, connected, and have unit conductances. Shared edges are identified and retain unit conductance. Write $N$ for the number of cores and $n$ for the vertex count of the assembled graph. For a connected seam $P_s$, $s$ counts vertices and $s-1$ counts edges. Disconnected seams and cycle seams will be specified by separate vertex and edge lists.

The parameters being compared are the spanning-tree count $\tau$ and resistance radius

$$
\rho=R_{\mathrm{sph}}^2,\qquad D_{\mathrm{res}}=4\rho
$$

The normalization agrees with the [[en/Foundations/Core specification#Resistance radius and diameter|current radius convention]]. The geometric drawings below show graph constructions, not resistance embeddings.

> [!info] Three distinct changes to a construction
> **Configuration with a fixed scheme:** seam positions within cores or their vertex correspondences change, while the prescribed core adjacencies and parameters of each seam remain fixed.
>
> **Change of scheme:** the auxiliary graph whose vertices represent cores and whose edges represent prescribed gluings changes.
>
> **Change of model:** other seam types, intersecting seams, additional contacts, or other cores are allowed.

Leaving a theorem's hypotheses does not imply that every parameter must change. It means that the previous proof no longer guarantees preservation.

## What is preserved for a fixed tree of cycles

> [!info] Admissible tree of cycles
> **Definition.** Let $T$ be a specified tree on $N$ vertices representing cycles $K_i=C_{m_i}$. Each edge $ij\in E(T)$ prescribes gluing along a proper induced path $P_{s_{ij}}$, with an explicit vertex correspondence. Require that:
>
> - adjacent cores intersect in exactly the prescribed path;
> - cores not joined by an edge of $T$ have no common vertices;
> - all seams of a core are pairwise vertex-disjoint;
> - core images are retained, with no other identifications or edges.
>
> In particular, $1\le s_{ij}\le\min(m_i,m_j)-1$ and $\sum_{j:\,ij\in E(T)}s_{ij}\le m_i$. These inequalities do not replace checking the actual intersections.

The scheme $T$ is a tree **on cores**; the assembled graph contains cycles. For $T=P_N$, this is the model from the [[en/Chains of cores/Cores, Seams, and Admissible Chains#Admissible open chains of cycles|definition of an open chain]].

> [!info] Invariance for a fixed tree
> **Theorem 1.** For fixed $T$, core sizes $m_i$, and seam sizes $s_{ij}$, all admissible trees of cycles have isomorphic cycle matroids. Consequently, they have the same ordinary forest polynomial $F_G(t)$, spanning-tree count $\tau$, resistance radius $\rho$, and parameters defined through ordinary forest coefficients.
>
> Put $\ell_{ij}=s_{ij}-1$. The spanning-tree count is
>
> $$
> \boxed{\tau(G)=\det\mathbf M_T},\qquad
> (M_T)_{ij}=
> \begin{cases}
> m_i,&i=j,\\
> -\ell_{ij},&ij\in E(T),\\
> 0,&\text{otherwise}
> \end{cases}
> \tag{1}
> $$

> [!note]- Proof of Theorem 1
> **Proof.** Root $T$ and attach cores so that each parent precedes its children. The initial cycle bounds one face. The next core's seam lies on a free portion of its already embedded parent's outer boundary: previously used seams share no vertices with it. The new cycle can be placed outside in a narrow region around the seam path, or in a free outer sector at the common vertex for a one-vertex seam. Its direction can be changed by reflection. The other unused seams remain accessible from outside.
>
> This gives a plane embedding with one bounded face per core. Its dual multigraph $H$ has vertices $f_i$ for the cores and $f_\infty$ for the outer face. For $ij\in E(T)$ there are $\ell_{ij}$ edges between $f_i,f_j$, and there are
>
> $$
> b_i=m_i-\sum_{j:\,ij\in E(T)}\ell_{ij}
> $$
>
> edges between $f_i,f_\infty$. There are no other edges. Thus the abstract multigraph $H$ depends only on the fixed data. Deleting the outer vertex's row and column from its Laplacian gives $\mathbf M_T$.
>
> By complementary spanning-tree correspondence, an isomorphism of dual multigraphs induces an isomorphism of the primal cycle matroids. This is the same passage used in the [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#From the dual graph to the cycle matroid|proof for chains]]. The matrix-tree theorem gives (1); independent matroid sets give equality of ordinary forest coefficients, and the [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance|matroid formula for the radius]] gives equality of $\rho$. $\square$

For identical cycles and seams, the formula simplifies to $\mathbf M_T=mI-(s-1)\mathbf A_T$, where $\mathbf A_T$ is the adjacency matrix of the tree **on cores**. The theorem does not determine rooted forest coefficients or the spectrum of the whole assembled graph.

If all gluings are at one vertex, a more general positive result holds: arbitrary fixed connected cores may be attached sequentially, each intersecting the assembled graph in exactly one vertex. The resulting matroid is the direct sum of the constituent matroids; $\tau$ multiplies and $\rho$ adds. In this model, both attachment positions and the sequential assembly scheme can change, provided each step remains a one-vertex gluing; the cores need not be cycles. See the [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#One-point gluing and the direct sum of matroids|one-vertex gluing laws]].

## Replacing the path by a star

Take four copies of $C_6$ with single-edge seams. For the path, each next cycle is glued by its edge $01$ to edge $34$ of the preceding cycle. For the star, the three outer cycles are glued by their edges $01$ to edges $01,23,45$ of the central cycle. Local vertex labels in each core follow cyclic order; endpoint correspondences preserve the indicated order. New vertices of outer cores are distinct.

![Four hexagons with equal seams: a path and a star](A%20Path%20and%20a%20Star%20of%20Four%20Cycles.svg)

**The scheme changes, not the seam size.** Both graphs have $N=4$, $n=18$, and $|E|=21$; each gluing has two vertices and one shared edge. In the star, the three marked seams of the central core are pairwise disjoint. Both constructions satisfy the definition of an admissible tree of cycles, but their schemes differ.

| Core scheme | $\tau$ | $\rho$ |
|---|---:|---:|
| Path $P_4$ | $1189$ | $7514229/5654884$ |
| Star $K_{1,3}$ | $1188$ | $1931/1452$ |

> [!note]- Checking the spanning-tree counts of the path and star
> **Proof.** With $m=6$, $s=2$, the path determinant is $m^4-3m^2+1=1189$ by the [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence#The continuant and matchings of a path|continuant expansion]]. For the star, the determinant of $mI-\mathbf A_T$ allows only the empty matching and three individual edges, giving $m^4-3m^2=1188$. The extra path term corresponds to two disjoint scheme edges; the star has no such pair. Both values are independently checked using the original Laplacians. $\square$

The tabulated radii are also computed directly and independently. Different spanning-tree counts already prove nonisomorphism. There is no contradiction with Theorem 1, which keeps the tree $T$ itself fixed.

## A disconnected seam adds different cycles

> [!info] Increase in cycle rank
> **Lemma 1.** Suppose a new cycle $K$ intersects a connected assembled graph $H$ in exactly a nonempty forest $S$ with $k$ connected components. With shared edges counted once,
>
> $$
> \boxed{\beta(H\cup K)-\beta(H)=k},\qquad
> \beta(G)=|E(G)|-|V(G)|+1
> \tag{2}
> $$

> [!note]- Proof of Lemma 1
> **Proof.** Let $S$ have $v$ vertices and $e$ edges. Since it is a forest with $k$ components, $v-e=k$. A cycle of length $m$ adds $m-v$ vertices and $m-e$ edges; the union remains connected. The difference of the increments is $v-e=k$. $\square$

For a connected path, $k=1$, and each core adds one independent cycle. For a seam consisting of two separate edges, $k=2$, and two independent cycles are added. Three such cycle cores have rank $1+2+2=5$, so the model with one bounded face per core does not apply.

Consider three copies of $C_{12}$. Number the middle core's vertices $0,\ldots,11$ cyclically. Specify its input by the ordered list $U=(0,1,4,5)$: the induced seam consists of $01$ and $45$. Each outer core has the same local seam $U$.

The first outer core is glued to $U$ of the middle core. The second is glued by one of two correspondences:

$$
\begin{array}{c|rrrr}
\text{outer-core vertex}&0&1&4&5\\\hline
\text{A: middle-core vertex}&2&3&6&7\\
\text{B: middle-core vertex}&6&7&10&11
\end{array}
\tag{3}
$$

The remaining vertices of the outer cores are new and distinct. In both cases the middle core's input and output are vertex-disjoint. Individual seams are related by rotations of $C_{12}$; their relative placement changes.

![Two placements of equal disconnected seams on the middle dodecagon](Two%20Disconnected%20Seams%20in%20a%20Cycle.svg)

**The middle core of two assemblies.** Red marks input $01\cup45$ and blue marks the output. Vertex-list labels supplement the colors. The four shared vertices do not form $P_4$: the actual intersection contains exactly two nonadjacent edges.

> [!example] Seam size and type are preserved, but parameters change
> Both graphs have $n=28$, $|E|=32$, and $\beta=5$. Direct calculation gives different values:

| Configuration | $\tau$ | $\rho$ |
|---|---:|---:|
| A | $28160$ | $39255199/24780800$ |
| B | $26460$ | $100697/58800$ |

This is a counterexample to extending the connected-seam theorem to arbitrary disconnected intersections, even with identical cores and the same type of each seam. The number of shared vertices alone is insufficient.

The actual intersection must be checked against every edge. For example, identifying vertices $0,1,2,3$ of two cycles in the same order makes $01,12,23$ shared. Selecting only $01$ and $23$ in a drawing does not make the seam disconnected.

## Core symmetry and symmetry of a seam pair

> [!info] Equivalence of boundary data
> **Definition.** Two ordered pairs of input and output seams of one core are equivalent under automorphisms if a core automorphism sends the input to the specified input and the output to the specified output. If individual boundary vertex correspondences are fixed, the automorphism must respect those as well.

Transitivity on individual edges or faces does not imply transitivity on their ordered pairs. Compatible core automorphisms induce an isomorphism of assemblies. The absence of such an automorphism does not by itself prove that $\tau$ or $\rho$ differ; exact computations establishing differences are given below.

### Tetrahedra: two distinct restrictions

A tetrahedral core means the graph $K_4$ on local vertices $0,1,2,3$. Take three copies. Glue the first outer core by its edge $(0,1)$ to $(0,1)$ of the middle core. Glue the second by its $(0,1)$ either to $(2,3)$ or to $(0,2)$ of the middle core. Correspondences preserve the indicated pair order; all remaining vertices are new.

| Seams of the middle core | $n$ | Edge count | $\tau$ | $\rho$ |
|---|---:|---:|---:|---:|
| $01$ and $23$ | $8$ | $16$ | $2304$ | $91/288$ |
| $01$ and $02$ | $8$ | $16$ | $2240$ | $1831/5600$ |

In the second row, the seams intersect. Moreover, both outer cores share vertex $0$: the prescribed attachment sequence no longer describes all actual contacts. This comparison is therefore not a counterexample with the seam-disjointness condition retained.

> [!info] Chains of complete four-vertex cores
> **Proposition 1.** For a fixed number of cores, open chains of $K_4$ with vertex-disjoint edge seams in every internal core and no additional contacts are mutually isomorphic. Changing configuration here does not produce a nontrivial family of nonisomorphic graphs.

> [!note]- Proof of Proposition 1
> **Proof.** Every permutation of the four vertices is an automorphism of $K_4$. Once the input edge of an internal core is chosen, its only possible disjoint output edge joins the remaining two vertices. A prescribed input-endpoint correspondence and any output-endpoint correspondence together define a permutation of all four vertices, hence extend to a core automorphism. Choosing these automorphisms successively from the first core to the last gives a compatible isomorphism of the entire chain. $\square$

### Cubes: disjoint seams are no longer sufficient

Represent the cube as $C_4\square K_2$: base cycles $0123$ and $4567$ are joined by $04,15,26,37$. In each of three assemblies, the first seam of the middle cube is $01$, and the second is $23$, $67$, or $26$. Each outer core is glued by its edge $(0,1)$ to the corresponding ordered pair of the middle core; there are no other identifications.

![Three inequivalent pairs of disjoint cube edges](Pairs%20of%20Edge%20Seams%20of%20a%20Cube.svg)

**The graph itself distinguishes the pairs.** The four seam endpoints induce, respectively, $C_4$, two disjoint edges, and the path $P_4$. These subgraphs differ, so no cube automorphism relates the pairs. Spatial descriptions such as “parallel” or “skew” are unnecessary for this argument.

| Second seam | Subgraph induced by the seam endpoints | $\tau$ | $\rho$, rounded |
|---|---|---:|---:|
| $23$ | $C_4$ | $38395904$ | $0.658097293$ |
| $67$ | $2K_2$ | $38600704$ | $0.656434277$ |
| $26$ | $P_4$ | $38651904$ | $0.655146384$ |

All three graphs have $n=20$ and $|E|=34$. Adjacent cores share exactly one edge, and nonadjacent cores are disjoint. Values are computed in exact rational arithmetic; full fractions are retained in the verification data. Different spanning-tree counts prove that replacing cycle cores by cubes can destroy invariance even with disjoint edge seams.

## Prisms: face placement and vertex correspondence

Now let the core be $C_6\square K_2$. Label the first layer $0,\ldots,5$ and the second $6,\ldots,11$; longitudinal edges are $j(j+6)$. A lateral face has cyclic order

$$
F_j=(j,\ j+1,\ (j+1)+6,\ j+6)
$$

First-layer indices are taken modulo $6$, then $6$ is added for the second layer. The seam is an entire four-cycle $F_j$, not a path on four vertices.

Glue the first outer core by its face $F_0$ to the middle core's $F_0$, matching local labels. Glue the second outer core by its $F_0$ to $F_j$, where $j=2$ or $3$. Both face pairs are vertex-disjoint. Let $F_j[k]$ be vertex $k$ of the indicated cyclic list, $0\le k<4$. Specify the last correspondence by

$$
\varphi_r:F_0[k]\longmapsto F_j[(k+r)\bmod4],\qquad r=0\ \text{or}\ 1
\tag{4}
$$

The four shared edges of each face pair are counted once. For $r=0$, edge types are preserved: base edges and longitudinal edges. For $r=1$, the types are interchanged. This is a permutation of seam vertices; no drawing of a physical prism rotation is required to define the graph.

| Middle-core faces | Shift $r$ | $\tau$ | $\rho$, rounded |
|---|---:|---:|---:|
| $F_0,F_2$ | $0$ | $25708969440$ | $0.687521270$ |
| $F_0,F_3$ | $0$ | $25762140408$ | $0.686915467$ |
| $F_0,F_2$ | $1$ | $25999447104$ | $0.686020598$ |
| $F_0,F_3$ | $1$ | $26037789636$ | $0.685448723$ |

All cases have $n=28$ and $|E|=46$. Either the output face position or its vertex correspondence changes. A one-step shift around a lateral face does not extend to an automorphism of the entire $C_6\square K_2$: a base edge belongs to one four-cycle and a longitudinal edge to two. An automorphism preserves these counts. Thus symmetry of the seam itself is insufficient to establish invariance of the assembly.

### Why aligned layers detect a spectral difference

For $r=0$, the assembled graph is $H\square K_2$, where $H$ is an open chain of three hexagons with edge seams. The position of $F_j$ gives input edge $01$ and output edge $j(j+1)$ in each layer. For $j=2$ and $3$, the base graphs have the same cycle matroid and $\tau(H)=204$, but different Laplacian polynomials, as shown by the [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#Two chains of three hexagons|two hexagonal chains]].

> [!info] Spanning-tree count of a doubled graph
> **Lemma 2.** For a connected graph $H$ with unit conductances,
>
> $$
> \boxed{\tau(H\square K_2)=\frac{\tau(H)}2\det(\mathbf L_H+2I)}
> \tag{5}
> $$
>
> With $h=|V(H)|$, the additional factor is expressed through the Laplacian polynomial as $\det(\mathbf L_H+2I)=2^hP_H(1/2)$.

> [!note]- Proof of Lemma 2
> **Proof.** Numbering the first layer before the second gives the product Laplacian
>
> $$
> \mathbf L_{H\square K_2}=
> \begin{pmatrix}\mathbf L_H+I&-I\\-I&\mathbf L_H+I\end{pmatrix}
> $$
>
> It acts as $\mathbf L_H$ on vectors $(u,u)$ and as $\mathbf L_H+2I$ on $(u,-u)$. If the eigenvalues of $H$ are $0=\lambda_1,\lambda_2,\ldots,\lambda_h$, the nonzero eigenvalues of the product consist of $\lambda_2,\ldots,\lambda_h$ and all $\lambda_j+2$. By the matrix-tree theorem,
>
> $$
> \tau(H\square K_2)=\frac{1}{2h}
> \left(\prod_{j=2}^{h}\lambda_j\right)
> \left(\prod_{j=1}^{h}(\lambda_j+2)\right)
> =\frac{\tau(H)}2\det(\mathbf L_H+2I)
> $$
>
> The last equality uses $\prod_{j=2}^{h}\lambda_j=h\tau(H)$. Factoring $2$ from each row gives the expression through $P_H$. $\square$

For the two aligned assemblies, direct calculation gives

$$
\det(\mathbf L_{H_2}+2I)=252048720,\qquad
\det(\mathbf L_{H_3}+2I)=252570004
$$

Here $j$ denotes the selected output edge, not the vertex count. Multiplying each value by $204/2=102$ gives the corresponding row of the prism table. Equality of the ordinary forest polynomials of the bases does not preserve this factor: it depends on rooted forest coefficients. The two polynomials are defined in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]. For $r=1$, the construction does not use a decomposition into two aligned layers, and formula (5) does not automatically apply.

Cubes and prisms are themselves planar graphs. Differences in the tables should not be attributed to the spatial dimension of their usual drawings. The relevant data are the core graph, its boundary data, and the specific identifications.

## An equal spanning-tree count does not determine the radius

Consider two explicitly specified graphs on vertices $0,\ldots,5$. In graph A, $C(0,1,2,3)$ and $C(0,4,5)$ are glued at vertex $0$. In graph B, take $K_{2,3}$ with parts $\{0,1\}$ and $\{2,3,4\}$ and add the pendant edge $05$. Their complete edge sets are

$$
E_{\text{A}}=\{01,12,23,03,04,45,05\},\qquad
E_{\text{B}}=\{02,03,04,12,13,14,05\}
\tag{6}
$$

Here $ij$ denotes the undirected edge $\{i,j\}$.

![Two graphs with twelve spanning trees and different resistance radii](Equal%20Spanning-Tree%20Counts%20and%20Different%20Radii.svg)

**Equal sizes and spanning-tree counts.** Both graphs have $n=6$, $|E|=7$, and $\tau=12$. Only B has a pendant vertex, so the graphs are nonisomorphic independently of the radius calculation. This compares different collections of cores, rather than two configurations of one fixed system of identical cores.

> [!example] Counterexample to determining the radius from the spanning-tree count alone
>
> $$
> \tau_{\text{A}}=\tau_{\text{B}}=12,\qquad
> \rho_{\text{A}}=\frac{77}{144},\qquad
> \rho_{\text{B}}=\frac7{12}
> \tag{7}
> $$
>
> The radius difference is $7/144$. Thus equality of $\tau$ does not guarantee equality of $\rho$ among connected graphs.

> [!note]- Exact verification of the counterexample
> **Proof.** One-vertex gluing gives $\tau_{\text{A}}=4\cdot3=12$. The pendant edge of graph B belongs to every tree. Deleting row and column $0$ from the Laplacian of $K_{2,3}$ gives
>
> $$
> \det\begin{pmatrix}3&-1&-1&-1\\-1&2&0&0\\-1&0&2&0\\-1&0&0&2\end{pmatrix}
> =2^3\left(3-\frac32\right)=12
> $$
>
> Hence $\tau_{\text{B}}=12$. For the radius, use the independent [[en/Matroid parameters and forest characteristics of graphs/Resistance Radius - Forest Formula and Matroid Invariance#The radius as Laplacian energy|Laplacian energy formula]]. With reference vertex $q=0$, inverting the grounded Laplacians gives the columns $\mathbf d=(R_{10},\ldots,R_{50})$:
>
> $$
> \mathbf d_{\text{A}}=(3/4,1,3/4,2/3,2/3)^{\mathsf T},\qquad
> \mathbf d_{\text{B}}=(2/3,2/3,2/3,2/3,1)^{\mathsf T}
> $$
>
> Add $R_{00}=0$ and sum squared differences over the edges (6). This yields
>
> $$
> \rho_{\text{A}}=\frac14\left(\frac54+\frac89\right)=\frac{77}{144},\qquad
> \rho_{\text{B}}=\frac14\left(\frac43+1\right)=\frac7{12}
> $$
>
> The calculation uses the two original graphs without assuming joint preservation of the parameters. $\square$

The ordinary two-component forest counts are $30$ and $32$, respectively. This is another difference missed by the spanning-tree count alone. In [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]], joint preservation of forest parameters and the radius follows from cycle matroid isomorphism, not equality of a single invariant. Counterexample (7) does not itself resolve separate questions for every narrower model of identical cores.

## Data required for further assembly

The general conclusion for a core other than a cycle is that its internal scalars $\tau(K)$ and $\rho(K)$ do not replace data on the chosen boundary. Even identical copies of a core can have inequivalent input-output pairs. Sequential gluing requires boundary names, vertex correspondences, and forest connectivity information on those boundaries.

The [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|full forest passport]] stores this information. Its pairing is described in [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]], and changing the active boundary in the [[en/Chains of cores/Cores, Seams, and Admissible Chains#Transferring the full forest passport|passport transfer rule]]. For a shared edge or face, first distribute shared edges between the parts: for example, retain them in the assembled part and remove duplicate copies from the new core, retaining all boundary vertices. Otherwise the formula for disjoint edge sets counts a different network.

Spectral characteristics require a separate [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|spectral passport]]. Neither symmetry of one seam nor equality of individual-core parameters establishes a universal gluing law.

## Checks and scope

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_invariance_limits.py) and [exact results](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/invariance-limits-results.json) specify the local graphs of all cores, vertex correspondences, shared edges, all actual intersections, and final edge sets. They check $20$ explicitly defined graphs. The common vertex of nonadjacent tetrahedra in the second table row is recorded as an intentional violation of the original conditions; the other constructions have no accidental extra contacts.

For each graph, $\tau$ is computed from a minor of the original Laplacian. The radius is calculated by two independent methods in rational arithmetic: the energy of the diagonal of the inverse grounded Laplacian, and a separate construction of the centered Green matrix and resistance matrix followed by solving the circumcenter equidistance equations. The energy is additionally checked for every reference vertex. Decimal table entries are rounded; full fractions are available in the results.

For trees of cycles, the dual determinant and matroid duality rank identity are checked on selected edge sets; Theorem 1 proves the general result. Additional configurations of one tree cover a one-vertex seam, a multi-edge seam, and seam movement and reversal. For the cube, the orbits of disjoint edge pairs are checked. For prisms, the explicit Cartesian-product correspondence for aligned layers and formula (5) are checked. The two small graphs (6) are checked by full forest enumeration and a separate evaluation of the forest formula for the radius. See the [reproduction and drawing instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md).

Theorem 1 gives sufficient conditions for invariance. The counterexamples delimit particular extensions but do not establish that cycle cores are the only possible ones. Ordinary and twisted closures are treated in [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain - Rings and the Möbius Effect]], where the initial boundary must be retained and the last vertex correspondence specified exactly.

## Sources and connections

1. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). Polygon chains and the explanation of invariance through dual graphs.
2. H. Richman, F. Shokrieh, C. Wu. *Counting two-forests and random cut size via potential theory*. [Theorem C / 5.7](https://arxiv.org/html/2308.03859v1). The forest identity used in the matroid formula for the radius.

Construction and admissibility: [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. The matroid mechanism: [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. Spanning-tree determinants: [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]]. General gluing limitations: [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance|Gluing and the Limits of Matroid Invariance]].

Reading routes, applicability conditions, and the origins of results: [[en/Chains of cores/Chains of Cores|Chains of Cores navigator]].
