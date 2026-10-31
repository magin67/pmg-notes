---
title: "Closing a Chain: Rings and the Möbius Effect"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: closing-a-chain-rings-and-the-mobius-effect
order: 5
description: "Ordinary and M\u00f6bius closures of square and even-cycle strips, hexagonal rings, and shifted prism bases."
---

Russian version: [[ru/Цепи из ядер/Замыкание цепи - кольцо и эффект Мёбиуса|Замыкание цепи: кольцо и эффект Мёбиуса]].

The final seam changes the global assembly conditions. One open square strip gives two different graphs depending on which endpoints of its end edges are identified. In this model, twisting increases the spanning-tree count and decreases the resistance radius. Both statements have exact formulas and proofs; extending them to other cores requires separate analysis.

The invariance conditions for an open chain are given in [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]] and [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. Closure leaves those conditions: the last core comes into contact with the first. We begin with squares, then consider opposite edges of even cycles and distinguish such a strip from a plane ring of hexagons. Finally, we compare edge closure with a shift of an entire prism base.

> [!note] Origins of the results
> Circular and Möbius ladders are classical graph families. The spanning-tree count of a circular ladder is given by [Azimi–Farrokhi, Theorem 4.2](https://arxiv.org/html/2306.10497v1#S4); resistance characteristics of circular and Möbius ladders are treated in §§4–5 of the same work. Below we give spectral proofs and convert the results to the PMG normalization. Formulas for elongated strips follow by replacing paths with conductances, and the prism formula by decomposition into transverse modes. Computational examples are identified separately; no priority is claimed for these constructions or deductions.

## The final seam of a square strip

All original edges have unit conductance. Shared edges remain unit edges after identification. Write $N$ for the number of cores and $n$ for the vertex count of the final graph. We use the convention

$$
\rho=R_{\mathrm{sph}}^2,\qquad D_{\mathrm{res}}=4\rho
$$

The drawings show graph constructions, not resistance embeddings.

> [!info] An open strip and two closures
> **Definition.** Let $N\ge3$. The open strip $O_N$ consists of squares
>
> $$
> K_i=C(a_i,a_{i+1},b_{i+1},b_i),\qquad 0\le i<N
> $$
>
> Its vertices $a_i,b_i$, $0\le i\le N$, are distinct. Adjacent squares share edge $a_ib_i$, counted once. The initial boundary is $B_0=(a_0,b_0)$ and the final boundary is $B_N=(a_N,b_N)$.
>
> **Ordinary closure** identifies $a_N\sim a_0$ and $b_N\sim b_0$; **twisted closure**, or Möbius closure, identifies $a_N\sim b_0$ and $b_N\sim a_0$. In both cases, $a_Nb_N$ and $a_0b_0$ become one edge.

![Two exact endpoint correspondences for the end edges of a square strip](Two%20Closures%20of%20a%20Square%20Strip.svg)

**One open construction, two correspondences.** Arrows along the end seams specify how their endpoints are matched. After identification, one unit seam edge remains. “Cylinder” and “Möbius” describe the boundary correspondence; the listed identifications suffice to specify the graph.

Denote the results by $G_{\text{c}}(N)$ and $G_{\text{m}}(N)$. They can be specified without taking a quotient: use vertices $a_i,b_i$, $0\le i<N$, all edges $a_ib_i$, and edges $a_ia_{i+1},b_ib_{i+1}$ for $0\le i<N-1$. The two remaining edges are

$$
\begin{aligned}
E_{\text{last},\text{c}}&=\{a_{N-1}a_0,\ b_{N-1}b_0\},\\
E_{\text{last},\text{m}}&=\{a_{N-1}b_0,\ b_{N-1}a_0\}
\end{aligned}
\tag{1}
$$

This describes edges of the result; adding them to $O_N$ without identifying its vertices would produce a different graph. In ordinary closure the longitudinal edges form two $N$-cycles; in twisted closure they form one $2N$-cycle. The edges $a_ib_i$ remain in both cases.

Both graphs are simple and connected, with $n=2N$, $|E|=3N$, and degree $3$ at every vertex. The restriction $N\ge3$ matters: smaller values produce coincident longitudinal edges, requiring a separate choice between a simple graph and a multigraph. The cycle rank of a closed strip is $N+1$, whereas the open strip has rank $N$. Thus the earlier model with one independent cycle per core and a size-$N$ determinant does not automatically extend to a ring.

## Edge accounting and retaining the initial boundary

> [!info] The Laplacian after identification
> **Lemma 1.** Remove one copy of the future shared edge from $O_N$, say $a_Nb_N$, and denote the resulting graph by $H_N$. Let $q$ be the chosen map of vertices to identification classes, and set $C_{vx}=1$ if $q(v)=x$ and $0$ otherwise. Then
>
> $$
> \boxed{\mathbf L_{G}=\mathbf C^{\mathsf T}\mathbf L_{H_N}\mathbf C}
> \tag{2}
> $$
>
> Using $O_N$ instead of $H_N$ would give conductance $2$ on the final seam.

> [!note]- Proof of Lemma 1
> **Proof.** The column $\mathbf C\mathbf x$ assigns an old-vertex potential constant on each class. Hence the energy $\sum_{uv\in E(H_N)}(x_{q(u)}-x_{q(v)})^2$ is the quadratic form of the right-hand side of (2). For $N\ge3$, edges of $H_N$ map bijectively to edges of the result, without loops. If $a_Nb_N$ is retained, its contribution coincides with that of $a_0b_0$ and adds another unit of conductance. $\square$

The lemma directly applies the energy definition in [[en/Introduction/Laplacian - graph, electrical network and quadratic form|Laplacian - graph, electrical network and quadratic form]]. It also explains why a gluing formula for disjoint edge sets cannot be applied to two copies of a shared seam without correction.

Sequential assembly must retain $B_0$ from the start. After a core is attached, the active boundary is $B_0\cup B_i$; previous output vertices that are no longer needed become internal. Before closure, retain all four names $a_0,b_0,a_N,b_N$ and their joint forest states. A passport on the current output edge alone is insufficient: it has forgotten connectivity with the start of the strip.

For $H_N$, the final operation is a [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|boundary contraction test]] with one of the partitions

$$
\sigma_{\text{c}}=a_0a_N\mid b_0b_N,\qquad
\sigma_{\text{m}}=a_0b_N\mid b_0a_N
$$

The vertical bar separates partition blocks. If $\mathcal F^{H_N,B}_\pi(t)$ is the state polynomial on $B=B_0\cup B_N$, the test rule gives

$$
F_G(t)=\sum_\pi C(\pi,\sigma)\mathcal F^{H_N,B}_\pi(t),\qquad
\tau(G)=[t^{2N-1}]F_G(t)
\tag{3}
$$

Here $C(\pi,\sigma)=1$ if $r(\pi\vee\sigma)=r(\pi)+r(\sigma)$ and $0$ otherwise; $r(\pi)=4-b(\pi)$, where $b(\pi)$ is the number of blocks and $\pi\vee\sigma$ their common coarsening. The condition selects forests that do not acquire a cycle under identification. The duplicate end edge must be excluded before forming the passport for the last step. Data transfer is described by the [[en/Chains of cores/Cores, Seams, and Admissible Chains#Transferring the full forest passport|active-boundary transfer rule]]. Spectral data require a separate [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|spectral passport]].

## Periodic and antiperiodic modes

We need the Chebyshev polynomials $T_k$ and $U_k$ of the first and second kinds. Their normalizations are $T_0=U_0=1$, $T_1(z)=z$, and $U_1(z)=2z$, with the common recurrence $p_{k+1}(z)=2zp_k(z)-p_{k-1}(z)$. Here $z$ is the Chebyshev argument; it is distinct from the spectral variable $\xi$ in $\det(\xi I-\mathbf L)$.

> [!info] A product with a boundary phase
> **Lemma 2.** For an integer $N\ge1$ and real $\varphi$,
>
> $$
> \prod_{j=0}^{N-1}\left(2z-2\cos\frac{2\pi j+\varphi}{N}\right)
> =2\bigl(T_N(z)-\cos\varphi\bigr)
> \tag{4}
> $$

This follows from the classical identity $T_N(\cos\theta)=\cos(N\theta)$ ([DLMF, 18.5.1](https://dlmf.nist.gov/18.5.E1)). Its relation to path and cycle operators is discussed in [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]].

> [!note]- Proof of Lemma 2
> **Proof.** For $\varphi\notin\pi\mathbb Z$, the indicated $N$ cosines are distinct roots of $T_N(z)-\cos\varphi$. Both sides have leading coefficient $2^N$. The remaining values of $\varphi$, including those with repeated roots, follow by continuity of the coefficients. $\square$

> [!info] Spanning-tree counts of the two square strips
> **Theorem 1.** For $N\ge3$,
>
> $$
> \boxed{\tau_{\text{c}}=N\bigl(T_N(2)-1\bigr)},\qquad
> \boxed{\tau_{\text{m}}=N\bigl(T_N(2)+1\bigr)}
> \tag{5}
> $$
>
> Consequently, $\tau_{\text{m}}-\tau_{\text{c}}=2N>0$. In particular, the two closed graphs are nonisomorphic and have different cycle matroids.

The circular-ladder formula is equivalent to [Azimi–Farrokhi, Theorem 4.2](https://arxiv.org/html/2306.10497v1#S4): in their notation, $a_{N+1}+a_N=2T_N(2)$. Here both formulas follow from one boundary-condition calculation.

> [!note]- Proof of Theorem 1
> **Proof.** The permutation $a_i\leftrightarrow b_i$ is an automorphism of both graphs. The function space splits into the symmetric sector $f(a_i)=f(b_i)$ and the antisymmetric sector $f(a_i)=-f(b_i)$, each of dimension $N$.
>
> In the symmetric sector, crossing the final seam preserves the sign. The operator is the Laplacian of $C_N$, with eigenvalues
>
> $$
> \lambda_j^{+}=2-2\cos\frac{2\pi j}{N},\qquad 0\le j<N
> $$
>
> In the antisymmetric sector, the transverse edge adds $2$. For ordinary closure, the function is periodic; for twisted closure, it changes sign after a full circuit. Thus, respectively,
>
> $$
> \lambda_{j,\text{c}}^{-}=4-2\cos\frac{2\pi j}{N},\qquad
> \lambda_{j,\text{m}}^{-}=4-2\cos\frac{(2j+1)\pi}{N}
> $$
>
> These modes can be obtained by substituting $f(a_i)=e^{\mathrm i\theta i}$, $f(b_i)=\pm e^{\mathrm i\theta i}$ with $e^{\mathrm iN\theta}=1$ or $-1$. Complex notation is used for the calculation; the Laplacian remains real symmetric.
>
> The only zero occurs at $j=0$ in the symmetric sector. The product of that sector's other eigenvalues is $N^2$, since $\tau(C_N)=N$. The product in the antisymmetric sector is $2(T_N(2)-1)$ or $2(T_N(2)+1)$ by (4). The matrix-tree theorem divides the full nonzero product by the vertex count $2N$, yielding (5). Different values of $\tau$ exclude both graph isomorphism and cycle matroid isomorphism. $\square$

The cycle spectrum and mode normalizations appear in [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]]. Here the calculation concerns the entire graph on $2N$ vertices; the auxiliary core scheme does not replace it.

## Radius of a square strip

> [!info] Twisting decreases the radius in the square model
> **Theorem 2.** For $N\ge3$,
>
> $$
> \begin{aligned}
> \rho_{\text{c}}&=\frac{N^2-1}{24N}
> +\frac{U_{N-1}(2)}{4(T_N(2)-1)},\\
> \rho_{\text{m}}&=\frac{N^2-1}{24N}
> +\frac{U_{N-1}(2)}{4(T_N(2)+1)}
> \end{aligned}
> \tag{6}
> $$
>
> In particular,
>
> $$
> \boxed{\rho_{\text{c}}-\rho_{\text{m}}
> =\frac{U_{N-1}(2)}{2(T_N(2)^2-1)}>0}
> \tag{7}
> $$

This converts known ladder resistance characteristics to the $\rho$ normalization; see [Azimi–Farrokhi, Corollaries 4.6–4.7 and 5.3–5.4](https://arxiv.org/html/2306.10497v1#S5). For these vertex-transitive graphs, $\rho=\operatorname{Kf}/(2N)^2$, where $\operatorname{Kf}$ is the Kirchhoff index. An independent spectral derivation follows.

> [!note]- Proof of Theorem 2
> **Proof.** The ordinary ladder is vertex-transitive under shifts along the rows and their interchange. In the twisted ladder, the longitudinal $2N$-cycle has order $a_0,\ldots,a_{N-1},b_0,\ldots,b_{N-1}$, and transverse edges join opposite vertices. Rotations of this cycle act transitively and preserve all edges.
>
> Hence the diagonal entries of $\mathbf{Gr}=\mathbf L^+$ are equal. In the centered resistance embedding, the vertices are equidistant from the centroid, which is therefore the circumcenter. Consequently,
>
> $$
> \rho=\frac{\operatorname{tr}\mathbf{Gr}}{2N}
> =\frac1{2N}\sum_{\lambda>0}\frac1\lambda
> $$
>
> The symmetric-sector sum is $(N^2-1)/12$. For example, logarithmic differentiation of $(T_N(z)-1)/(z-1)$ at $z=1$ gives this: $T_N'(1)=N^2$, $T_N''(1)=N^2(N^2-1)/3$, and the sum is $T_N''(1)/(4T_N'(1))$.
>
> Differentiating (4) with respect to $z$ gives
>
> $$
> \sum_{j=0}^{N-1}\frac1{2z-2\cos((2\pi j+\varphi)/N)}
> =\frac{NU_{N-1}(z)}{2(T_N(z)-\cos\varphi)}
> $$
>
> Here $T_N'(z)=NU_{N-1}(z)$ is used ([DLMF, 18.9.21](https://dlmf.nist.gov/18.9.E21)). Substituting $z=2$ and $\varphi=0$ or $\pi$, then dividing the two-sector sum by $2N$, gives (6). Subtraction gives (7); at $z=2$, $T_N(2)>1$ and $U_{N-1}(2)>0$. $\square$

The equality $\rho=\operatorname{tr}\mathbf{Gr}/n$ here relies on all vertices being equidistant from the centroid. For a general graph, the circumcenter may differ, as explained in [[en/Metric parameters/Resistance Radius and Diameter of a Graph|Resistance Radius and Diameter of a Graph]].

> [!example] Four square cores
> Both assemblies have $8$ vertices and $12$ edges. The ordinary one is the cube graph. Direct rational calculations give
>
> $$
> \tau_{\text{c}}=384,\quad \tau_{\text{m}}=392,\qquad
> \rho_{\text{c}}=\frac{29}{96},\quad \rho_{\text{m}}=\frac{67}{224}
> $$

## Strips of even cycles

> [!info] An elongated strip
> **Definition.** Let the core be $C_m$ with even $m\ge4$, and let the input and output seams be opposite edges. Put $\ell=(m-2)/2$. Between successive transverse edges are two paths, each containing $\ell$ unit edges. The internal vertices of all these paths are distinct. Close the strip of $N\ge3$ cores using the same two correspondences between the endpoints of the end seams.

Here $\ell$ denotes the length of a **longitudinal path**, not the number of seam edges: each seam still consists of one edge. The final graph has $n=2N\ell=N(m-2)$ vertices and $|E|=N(2\ell+1)=N(m-1)$ edges. Opposite seams are essential; an even core size alone does not imply the next formula.

![Replacing the two longitudinal paths of a hexagonal core by equivalent conductances](An%20Even%20Cycle%20and%20Reduction%20of%20Longitudinal%20Paths.svg)

**Example $m=6$, $\ell=2$.** Both transverse edges retain conductance $1$; each two-edge path is replaced by a connection of conductance $1/2$. This is an electrical reduction eliminating internal vertices, not another graph on the same vertex set.

> [!info] Spanning-tree counts of elongated strips
> **Theorem 3.** For the specified model,
>
> $$
> \begin{aligned}
> \tau_{\text{c}}&=N\ell\bigl(T_N(\ell+1)-1\bigr),\\
> \tau_{\text{m}}&=N\ell\bigl(T_N(\ell+1)+1\bigr)
> \end{aligned}
> \tag{8}
> $$
>
> Consequently,
>
> $$
> \Delta\tau=\tau_{\text{m}}-\tau_{\text{c}}=2N\ell=N(m-2),\qquad
> \frac{\Delta\tau}{\tau_{\text{c}}}=\frac{2}{T_N(m/2)-1}
> \tag{9}
> $$

The formula adapts the ladder calculation through the standard replacement of series edges, retaining the determinant factor from elimination of internal vertices. For the reduced weighted network, the spanning-tree coefficient is used: the sum of products of conductances over spanning trees. For the original unit network, it is the ordinary spanning-tree count. The general distinction between electrical response and the full spanning-tree scale is discussed in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]].

> [!note]- Proof of Theorem 3
> **Proof.** Replace each of the $2N$ longitudinal paths by a connection of conductance $c=1/\ell$. Restoring the paths multiplies the spanning-tree coefficient by $\ell^{2N}$. Indeed, in a spanning tree of the expanded graph, each such path is either included in full or has exactly one edge omitted. Omitting two edges would isolate an internal segment. Fully included paths and selected transverse edges form a spanning tree of the reduced graph. For each unselected path, there are $\ell$ choices of the omitted edge. Summing over reduced-graph trees therefore gives a factor $\ell^{2N}$ with weight $1/\ell$ on each selected longitudinal connection.
>
> In the symmetric sector of the reduced Laplacian, the eigenvalues are $c(2-2\cos(2\pi j/N))$. Their nonzero product is $c^{N-1}N^2$. The antisymmetric eigenvalues have the form
>
> $$
> 2c\left(\ell+1-\cos\frac{2\pi j+\varphi}{N}\right),
> \qquad \varphi=0\ \text{or}\ \pi
> $$
>
> By (4), their product is $2c^N(T_N(\ell+1)-\cos\varphi)$. The matrix-tree theorem gives $Nc^{2N-1}(T_N(\ell+1)-\cos\varphi)$ for the reduced network. Multiplication by $\ell^{2N}$ gives (8); subtraction and division give (9). $\square$

For fixed $m$, the absolute difference grows linearly with $N$, while the relative difference tends to zero exponentially: for $z=m/2>1$, one has $T_N(z)=(\lambda^N+\lambda^{-N})/2$, where $\lambda=z+\sqrt{z^2-1}>1$.

> [!note] The radius requires all vertices
> Reduction preserves resistances between retained vertices but removes internal path vertices. Thus the radius of the reduced network cannot replace the radius of the whole strip. Theorem 2 concerns $m=4$; for $m>4$, the values below are separate exact computations on the full graph.

| $N$ | $m$ | $\tau_{\text{c}}$ | $\tau_{\text{m}}$ | $\rho_{\text{c}}$ | $\rho_{\text{m}}$ |
|---:|---:|---:|---:|---:|---:|
| $4$ | $4$ | $384$ | $392$ | $29/96$ | $67/224$ |
| $6$ | $4$ | $8100$ | $8112$ | $31/80$ | $725/1872$ |
| $6$ | $6$ | $235200$ | $235224$ | $1339547/1411200$ | $99229/104544$ |

For six hexagons, the relative increase in $\tau$ is $24/235200=1/9800$, approximately $0.0102\%$. The radius decrease in this row is checked independently of the spanning-tree formula.

## A hexagonal ring and a cylindrical strip

Six regular hexagonal cells surrounding an empty cell form a different ring. In each core, the two paths between seams have lengths $1$ along the inner boundary and $3$ along the outer boundary. In a cylindrical strip of hexagons joined along opposite edges, the lengths are $2$ and $2$.

Both ordinary closures can be specified on vertices $u_i,v_i,x_i,y_i$, $i\in\mathbb Z_6$, with transverse edges $u_iv_i$. For the plane ring, the longitudinal paths are

$$
u_i\!\longleftrightarrow u_{i+1},\qquad
v_i\!\longleftrightarrow x_i\!\longleftrightarrow y_i\!\longleftrightarrow v_{i+1}
$$

For the cylindrical strip, they are

$$
u_i\!\longleftrightarrow x_i\!\longleftrightarrow u_{i+1},\qquad
v_i\!\longleftrightarrow y_i\!\longleftrightarrow v_{i+1}
$$

Each arrow in these expressions denotes one undirected unit edge. The lists exhaust the edge sets; each six-cycle consists of the two indicated paths and two consecutive transverse edges. In the twisted version of the second construction, only the last paths end at $v_0$ and $u_0$, respectively.

![A plane ring of six hexagons and a cylindrical strip with opposite seams](A%20Hexagonal%20Ring%20and%20a%20Closed%20Strip.svg)

**The configuration of each core differs.** Transverse seams are highlighted and the last seam is red. The ordinary cylindrical strip also admits a plane drawing. “Plane” in the name of the first construction describes the particular ring of cells, not a criterion for invariance.

| Construction | $\tau$ | $\rho$ |
|---|---:|---:|
| Ring around an empty cell | $176400$ | $4745753/4233600$ |
| Ordinary closure of the strip | $235200$ | $1339547/1411200$ |
| Twisted closure of the same strip | $235224$ | $99229/104544$ |

All three graphs have $n=24$ and $|E|=30$. The values are computed directly from the Laplacians. The difference between the first two rows comes from seam positions within cores; the final twist is measured by comparing the second and third rows. Different values of $\tau$ already prove that all three graphs are pairwise nonisomorphic. This comparison is related to the distinction between configuration and scheme in [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores|Limits of Invariance - Branching, Disconnected Seams, and Other Cores]].

## Shifting the base when closing a chain of prisms

This is a separate model: the seam is an entire base cycle. Take $N\ge3$ cores $C_m\square K_2$, $m\ge3$, successively glued along bases. The open construction has $N+1$ layers $v_{i,j}$, $0\le i\le N$, $j\in\mathbb Z_m$. Each layer has edges $v_{i,j}v_{i,j+1}$, and adjacent layers are joined by $v_{i,j}v_{i+1,j}$.

Close the chain by $v_{N,j}\sim v_{0,j+r}$, where $r\in\mathbb Z_m$. The two copies of each edge of the end bases are identified. The result has $n=Nm$ vertices and $|E|=2Nm$ edges. Described on layers $0,\ldots,N-1$, its last longitudinal transition is

$$
v_{N-1,j}v_{0,j+r}
\tag{10}
$$

![Zero and unit shifts when square bases are identified](Shifting%20the%20Final%20Prism%20Base.svg)

**A square-base example.** Arrows denote vertex correspondences, not additional graph edges. The shift $r=1$ maps $j$ to $j+1$ modulo $4$. This permutation of an entire base differs from interchanging the two endpoints of an edge seam.

> [!info] Spanning-tree count for a cyclic base shift
> **Proposition 1.** In the specified model,
>
> $$
> \boxed{\tau_r=\frac Nm\prod_{j=1}^{m-1}
> 2\left[T_N\!\left(2-\cos\frac{2\pi j}{m}\right)
> -\cos\frac{2\pi rj}{m}\right]}
> \tag{11}
> $$
>
> Every nonzero $r\in\mathbb Z_m$ satisfies $\tau_r>\tau_0$. Shifts $r$ and $m-r$ give isomorphic graphs.

This follows from cycle modes, the matrix-tree theorem, and identity (4), applied to the explicitly specified final transition (10).

> [!note]- Proof of Proposition 1
> **Proof.** The transverse mode $e^{2\pi\mathrm i j k/m}$ has phase $\theta_j=2\pi j/m$. After a full longitudinal circuit, its multiplier is $e^{\mathrm i r\theta_j}$. The graph eigenvalues are therefore
>
> $$
> \lambda_{j,k}=4-2\cos\theta_j
> -2\cos\frac{2\pi k+r\theta_j}{N},\qquad
> 0\le j<m,\quad 0\le k<N
> $$
>
> For $j=0$, this is the Laplacian of $C_N$, with one zero and nonzero product $N^2$. For $j\ne0$, set $z_j=2-\cos\theta_j>1$. The product over $k$ is $2(T_N(z_j)-\cos(r\theta_j))$ by (4). Dividing the full product by $Nm$ gives (11).
>
> All factors are positive. Replacing $r=0$ by any $r$ cannot decrease them, because $\cos(r\theta_j)\le1$. For nonzero $r$, the factor at $j=1$ strictly increases. An isomorphism from shift $r$ to shift $m-r$ is given by $j\mapsto-j$ in every layer. $\square$

For four cubical cores ($N=m=4$), direct calculations give:

| Final base shift | $\tau$ | $\rho$ |
|---|---:|---:|
| $r=0$ | $42467328$ | $103/384$ |
| $r=1$ | $43507216$ | $28133/105536$ |
| $r=2$ | $44255232$ | $713/2688$ |

Proposition 1 compares $\tau_r$ with $\tau_0$; it does not assert pairwise distinction of all other shifts. The tabulated radii are computed on the full graphs. The table implies no universal monotonicity of the radius with twist angle for an arbitrary core. Even if the angle $2\pi/m$ is small, $r=1$ changes the discrete correspondence of every base vertex.

## Checks and applicability conditions

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_closures.py) and [exact data](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/closure-results.json) record the open graphs, local core vertices, last correspondence, duplicate edges to remove, maps of all vertices to the closed graph, and its final edges. They check $37$ closed graphs: $24$ strips with $3\le N\le6$, $m\in\{4,6,8\}$, and both closures; the hexagonal ring; and $12$ prism closures with different shifts.

For each assembly, the checks cover connectivity, sizes, preservation of core images, and every pairwise intersection. The Laplacian from the final edge set is compared with (2), including the correction for all duplicate final-seam edges. Its minor gives the spanning-tree count. The radius is computed independently from the energy of the diagonal of the inverse grounded Laplacian and through a separately constructed Green matrix and circumcenter equidistance equations, using exact rational arithmetic. The energy is additionally checked for every reference vertex.

For strips, the Chebyshev formulas are compared with direct determinants; the symmetric and antisymmetric blocks and the determinant factor from eliminating internal vertices are checked separately. Boundary rule (3) is checked by full forest enumeration for square strips with $N=3,4$. An explicit correspondence identifies the ring with an independent assembly on the hexagonal lattice. For prisms, product (11) is evaluated exactly through the cyclic-shift matrix, without approximate trigonometric values; the isomorphism between shifts $r$ and $m-r$ is checked by an explicit vertex permutation. See the [reproduction and drawing instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md).

General assertions are proved in the text; finite checks confirm constructions and examples. Increased $\tau$ and decreased $\rho$ under Möbius closure are proved together here for the square strip. For even cycles joined along opposite edges, the formula for $\tau$ is proved; for a cyclic prism-base shift, comparison with the zero shift is proved. These conditions cannot be replaced by a general statement that “twisting improves connectivity.”

## Sources and connections

1. A. Azimi, M. Farrokhi D. G. *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*. [§§4–5; Theorem 4.2 and Corollaries 4.6–4.7, 5.3–5.4](https://arxiv.org/html/2306.10497v1). Classical ladders and their spanning-tree and resistance parameters.
2. NIST DLMF. [18.5.1](https://dlmf.nist.gov/18.5.E1), [18.9(i)](https://dlmf.nist.gov/18.9.i), [18.9.21](https://dlmf.nist.gov/18.9.E21). Trigonometric representation, recurrences, and the derivative of Chebyshev polynomials.

Seam construction: [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. The open-chain recurrence: [[en/Chains of cores/Spanning-Tree Polynomials of Chains - Determinant and Recurrence|Spanning-Tree Polynomials of Chains - Determinant and Recurrence]]. Limits of invariance: [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores|Limits of Invariance - Branching, Disconnected Seams, and Other Cores]]. Boundary identification: [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test|Vertex Contraction as a Boundary Test]]. Spectral foundations: [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]].

Reading routes, applicability conditions, and the origins of results: [[en/Chains of cores/Chains of Cores|Chains of Cores navigator]].
