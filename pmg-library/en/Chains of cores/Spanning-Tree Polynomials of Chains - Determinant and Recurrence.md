---
title: "Spanning-Tree Polynomials of Chains: Determinant and Recurrence"
date: 2026-10-31
updated: 2026-10-31
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: spanning-tree-polynomials-of-chains
order: 3
description: "Dual determinants, continuants, matchings, Chebyshev polynomials, and the dependence of spanning-tree counts on seam order."
---

Russian version: [[ru/Цепи из ядер/Остовные полиномы цепочек - определитель и рекурсия|Остовные полиномы цепочек: определитель и рекурсия]].

The spanning-tree count of a chain can be computed from a matrix whose size is the number of cores. Its tridiagonal structure gives a two-step recurrence. The same matrix explains why seam positions within cores do not affect the result, whereas permuting seam lengths may change it.

The graph construction and shared-edge rules are specified in [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. The common dual multigraph and invariance of the cycle matroid for fixed ordered sizes are established in [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. Here we apply that construction to spanning-tree counts and relate the resulting polynomials to continuants and Chebyshev polynomials.

> [!note] Origins of the results
> The recurrence for polygon chains with one shared edge between adjacent cycles is given by [Chen–Mohar, §3, Lemma 3.1](https://arxiv.org/html/1907.08450v1#S3). The treatment of an arbitrary connected seam below follows from dual-edge multiplicities and the matrix-tree theorem. The continuant expansion and passage to Chebyshev polynomials are standard algebraic constructions; we use the recurrence in [DLMF, §18.9(i), Table 18.9.1](https://dlmf.nist.gov/18.9.i). Examples and normalizations are checked separately. No priority is claimed for these families.

## Model and parameters

Consider an admissible open chain of $N\ge1$ simple cycles $K_i=C_{m_i}$, $m_i\ge3$. Adjacent cores intersect in exactly a prescribed proper induced path $P_{s_i}$. Nonadjacent cores have no common vertices; the input and output seams of an internal core are vertex-disjoint. There are no additional identifications, edges, or closure.

> [!info] Seam vertices and shared edges
> The size $s_i$ counts **vertices** of the seam. Set
>
> $$
> \ell_i=s_i-1\quad(1\le i<N),\qquad \ell_0=\ell_N=0
> $$
>
> The number $\ell_i$ counts shared edges. All edges of the original chain have conductance $1$; a shared edge is identified and counted once. When $s_i=1$, the contact is at one vertex and $\ell_i=0$.

Admissible assembly requires

$$
1\le s_i\le\min(m_i,m_{i+1})-1,\qquad
s_{i-1}+s_i\le m_i\quad(2\le i<N)
$$

The intersections themselves must satisfy the definition; the inequalities alone are not enough. Write $n$ for the vertex count of the result; the auxiliary path on cores has $N$ vertices. The count in the [[en/Chains of cores/Cores, Seams, and Admissible Chains#Admissible open chains of cycles|definition of an admissible chain]] gives

$$
n=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}s_i,\qquad
|E(G)|=\sum_{i=1}^{N}m_i-\sum_{i=1}^{N-1}\ell_i
$$

Let $G_j$ consist of the first $j$ cores and let $\tau_j=\tau(G_j)$ for $j\ge1$. The value $\tau_0=1$ will be a formal initial condition; it introduces no additional graph into the model.

## The spanning-tree count as a dual determinant

In the [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#A plane embedding with one face per core|plane embedding of the chain]], each cycle bounds a separate face. Denote the vertices of the dual multigraph $H$ by $f_1,\ldots,f_N,f_\infty$, where $f_\infty$ represents the outer face. There are $\ell_i$ distinct edges between $f_i$ and $f_{i+1}$, and

$$
b_i=m_i-\ell_{i-1}-\ell_i
$$

edges between $f_i$ and $f_\infty$. There are no other edges. The full degree of $f_i$ is $m_i$, including its edges to the outer face. In particular, the reduced Laplacian diagonal is not the number of edges remaining after deletion of $f_\infty$.

> [!info] A determinant indexed by the cores
> **Theorem 1.** For an admissible open chain,
>
> $$
> \boxed{\tau_N=\det\mathbf M_N}
> \tag{1}
> $$
>
> Here $\mathbf M_N$ is the reduced Laplacian of $H$ with the row and column of $f_\infty$ deleted:
>
> $$
> \mathbf M_N=
> \begin{pmatrix}
> m_1&-\ell_1&0&\cdots&0\\
> -\ell_1&m_2&-\ell_2&\ddots&\vdots\\
> 0&-\ell_2&m_3&\ddots&0\\
> \vdots&\ddots&\ddots&\ddots&-\ell_{N-1}\\
> 0&\cdots&0&-\ell_{N-1}&m_N
> \end{pmatrix}
> $$
>
> For $N=1$, this is the matrix $(m_1)$; for $N=2$, it is the corresponding size-$2$ matrix.

> [!note]- Proof of Theorem 1
> **Proof.** The stated multiplicities give off-diagonal entries $-\ell_i$, while the full degrees give diagonal entries $m_i$. By the matrix-tree theorem, $\det\mathbf M_N=\tau(H)$. The complement of a spanning tree of a plane graph corresponds to a spanning tree of its dual, so $\tau(G)=\tau(H)$; the precise correspondence appears in the [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters#From the dual graph to the cycle matroid|proof of matroid invariance]]. This gives (1). $\square$

![The dual multigraph of three hexagons, including the outer vertex](The%20Common%20Dual%20Multigraph%20of%20the%20Chains.svg)

**Example of the dual graph.** For three hexagons and two shared edges, the full degrees of the internal dual vertices are $6$. The bundles to the outer vertex contain $5,4,5$ edges. After its row and column are deleted, the diagonal remains $(6,6,6)$ and neighboring entries are $-1$. Parallel edges are drawn separately; their unit conductances add in the Laplacian. This calculation in the dual graph does not change the rule that shared edges of the original chain are counted once.

## Recurrence in the number of cores

> [!info] Two-step spanning-tree recurrence
> **Corollary 1.** For $2\le j\le N$,
>
> $$
> \boxed{
> \tau_0=1,\qquad \tau_1=m_1,\qquad
> \tau_j=m_j\tau_{j-1}-\ell_{j-1}^{\,2}\tau_{j-2}
> }
> \tag{2}
> $$
>
> In terms of seam sizes, the subtracted multiplier is $(s_{j-1}-1)^2$.

For $s_i=2$, formula (2) is the recurrence of Chen–Mohar [1, Lemma 3.1]. For a multi-edge seam, the square $\ell_i^2$ comes from the two symmetric off-diagonal entries of the determinant.

> [!note]- Proof of the recurrence
> **Proof.** The matrix for the first $j$ cores has the same diagonal $m_1,\ldots,m_j$ and the first $j-1$ neighboring entries. The last core's output seam edges, if marked for later assembly, still belong to the outer boundary of this subchain. Thus its dual cofactor is indeed the leading principal block $\mathbf M_j$.
>
> Expand $\det\mathbf M_j$ along the last row. The diagonal term is $m_j\det\mathbf M_{j-1}$. In the minor for the entry $-\ell_{j-1}$, the last column has a single nonzero entry $-\ell_{j-1}$; its cofactor sign in the original last row is negative. The second contribution is $-\ell_{j-1}^2\det\mathbf M_{j-2}$. The empty determinant is $1$, giving the initial conditions and (2). $\square$

The first expressions are

$$
\begin{aligned}
\tau_2&=m_1m_2-\ell_1^2\\
\tau_3&=m_1m_2m_3-m_3\ell_1^2-m_1\ell_2^2
\end{aligned}
\tag{3}
$$

> [!example] Three hexagons and three octagons
> For $m_i=6$ and $s_i=2$, the recurrence gives
>
> $$
> \tau_1=6,\qquad \tau_2=36-1=35,\qquad \tau_3=6\cdot35-6=204
> $$
>
> For $m_i=8$ and $s_i=3$, we have $\ell_i=2$ and
>
> $$
> \tau_1=8,\qquad \tau_2=64-4=60,\qquad \tau_3=8\cdot60-4\cdot8=448
> $$
>
> Both sequences are independently checked against minors of the original graph Laplacians.

## The continuant and matchings of a path

> [!info] Spanning-tree polynomial in construction parameters
> **Definition.** For fixed $N$, call
>
> $$
> \mathcal T_N(m_1,\ldots,m_N;\ell_1,\ldots,\ell_{N-1})=\det\mathbf M_N
> $$
>
> the spanning-tree polynomial of the chain **in its construction parameters**. Its value on admissible integer data is $\tau_N$. Such a tridiagonal determinant with a two-step recurrence is a continuant; here the signs and squares of neighboring parameters are specified explicitly.

The formal polynomial is defined beyond the graph model. Arbitrary real arguments do not specify a chain of cycles. In particular, changing $m_i$ and $\ell_i$ in this polynomial does not mean changing the conductances of a fixed original graph.

> [!info] Matching of the auxiliary path
> **Definition.** A matching of $P_N$ is an edge set with no shared endpoints. The vertices of this path represent cores; its edge $(i,i+1)$ represents seam $i$. Write $\mathcal M(P_N)$ for all matchings, including the empty matching, and $V(Q)$ for the vertices covered by a matching $Q$.

> [!info] Continuant expansion
> **Lemma 1.** For formal parameters,
>
> $$
> \boxed{
> \mathcal T_N=
> \sum_{Q\in\mathcal M(P_N)}(-1)^{|Q|}
> \prod_{(i,i+1)\in Q}\ell_i^2
> \prod_{j\notin V(Q)}m_j
> }
> \tag{4}
> $$

This is the standard determinant expansion for a matrix whose graph of nonzero off-diagonal entries is a path; we give a direct proof.

> [!note]- Proof of Lemma 1
> **Proof.** A nonzero term of the determinant can use only diagonal entries and neighboring pairs of indices. A permutation cycle of length at least three would require a cycle in $P_N$, which is impossible. Thus only fixed points and disjoint transpositions of neighboring indices remain.
>
> The transpositions form a matching $Q$. Each contributes a minus sign and the product $(-\ell_i)(-\ell_i)=\ell_i^2$. An uncovered index contributes $m_j$. Summing over all such permutations gives (4). $\square$

![The five matchings of the path on four cores and their terms](Matchings%20and%20the%20Spanning-Tree%20Polynomial.svg)

**Five terms for four cores.** Highlighted edges belong to a matching of the auxiliary path. The possibilities are the empty set, three individual edges, and the pair consisting of the first and third edges. Adjacent seams cannot both belong to a matching because they share a core. Therefore

$$
\begin{aligned}
\mathcal T_4={}&m_1m_2m_3m_4-m_3m_4\ell_1^2-m_1m_4\ell_2^2-\\
&-m_1m_2\ell_3^2+\ell_1^2\ell_3^2
\end{aligned}
\tag{5}
$$

Each term in (4) has total degree $N$ in $m_i,\ell_i$. The alternating coefficients describe a determinant expansion; they are not counts of ordinary forests of the original chain.

## Reversing a chain and ordering its seams

> [!info] Reversal preserves the spanning-tree polynomial
> **Corollary 2.** The simultaneous replacement
>
> $$
> (m_1,\ldots,m_N;\ell_1,\ldots,\ell_{N-1})
> \longmapsto
> (m_N,\ldots,m_1;\ell_{N-1},\ldots,\ell_1)
> $$
>
> preserves $\mathcal T_N$. If core sizes differ, reversing only the seam list is not covered by this assertion.

> [!note]- Proof of Corollary 2
> **Proof.** Reversing the rows and columns of $\mathbf M_N$ gives the matrix of the reversed data. If $\mathbf J$ is the corresponding permutation matrix, its determinant is $\det(\mathbf J^{\mathsf T}\mathbf M_N\mathbf J)=\det\mathbf M_N$. $\square$

For four identical cores, formula (5) becomes

$$
\boxed{\tau_4=m^4-m^2(\ell_1^2+\ell_2^2+\ell_3^2)+\ell_1^2\ell_3^2}
\tag{6}
$$

The sum of squares is unchanged by permutation. The last product depends on which two seams occupy the ends.

| Seam lengths in vertices | Reverse order | Polynomial for identical cores | Value at $m=8$ |
|---|---|---|---:|
| $(1,2,3)$ | $(3,2,1)$ | $m^4-5m^2$ | $3776$ |
| $(2,1,3)$ | $(3,1,2)$ | $m^4-5m^2+4$ | $3780$ |
| $(1,3,2)$ | $(2,3,1)$ | $m^4-5m^2$ | $3776$ |

All these orders allow disjoint seams when $m\ge5$. If the one-vertex seam is at an end, the product in (6) is zero; if it is in the middle, the product is $1^2\cdot2^2=4$.

![Three seam orders on the auxiliary path of four octagonal cores](Seam%20Order%20and%20the%20Spanning-Tree%20Count.svg)

**Seam orders and determinant values.** Circles represent entire cores $C_8$. Lines specify the gluing scheme, including the one-vertex contact; the numbers above them are seam sizes in vertices. This is the auxiliary path, not the original graph or its dual. Moving the one-vertex seam changes the tree count from $3776$ to $3780$.

Here three classes of sequences up to reversal give only two polynomials. Counting orders does not count distinct polynomials, nonisomorphic graphs, or isomers with respect to a parameter pair. For three distinct seam sizes $a,b,c>1$ and four identical cores, the three order classes give three different polynomials: the three possible products of endpoint squares are positive and distinct.

For unequal core sizes, reordering seams may matter already at $N=3$. With $(m_1,m_2,m_3)=(3,5,6)$, formula (3) gives $87$ for $(s_1,s_2)=(1,2)$ and $84$ for $(2,1)$. Both assemblies are admissible. Reversing the first chain gives sizes $(6,5,3)$, seams $(2,1)$, and again the count $87$.

> [!info] Factorization at a one-vertex seam
> **Corollary 3.** If $s_i=1$, the spanning-tree count of the whole chain is the product of the counts of the subchains to the left and right of that seam.

> [!note]- Proof of factorization
> **Proof.** When $\ell_i=0$, the matrix $\mathbf M_N$ splits into two diagonal blocks. Its determinant is the product of their determinants. This agrees with the [[en/Matroid parameters and forest characteristics of graphs/Gluing and the Limits of Matroid Invariance#One-point gluing and the direct sum of matroids|one-vertex gluing rule]]: a tree of the union consists of a tree of each part. If every $s_i=1$, then $\tau_N=\prod_i m_i$. $\square$

## Identical cores and homogeneous normalization

Let $m_i=m$, $s_i=s$, and $\ell=s-1$. For fixed $N$, factor the common core size out of the determinant.

> [!info] Normalized spanning-tree polynomial
> **Definition.** Set
>
> $$
> x=\frac{s-1}{m}=\frac\ell m,\qquad
> D_N(x)=\frac{\mathcal T_N(m,\ldots,m;\ell,\ldots,\ell)}{m^N}
> \tag{7}
> $$
>
> For admissible integer data, $\tau_N=m^ND_N(x)$ is an exact equality, not a limiting formula. Formula (2) gives
>
> $$
> D_0=D_1=1,\qquad D_N=D_{N-1}-x^2D_{N-2}\quad(N\ge2)
> \tag{8}
> $$

Here $D_N$ is a scalar polynomial in the relative number of seam **edges**. It does not denote the Greenian exponential $D$ or the resistance diameter $D_{\mathrm{res}}$. If the fraction of seam vertices is $y=s/m$, then $x=y-1/m$; these parameters differ for finite $m$.

| Number of cores $N$ | $D_N(x)$ |
|---:|---|
| $0$ | $1$ |
| $1$ | $1$ |
| $2$ | $1-x^2$ |
| $3$ | $1-2x^2$ |
| $4$ | $1-3x^2+x^4$ |
| $5$ | $1-4x^2+3x^4$ |
| $6$ | $1-5x^2+6x^4-x^6$ |

> [!info] Coefficients of the normalized polynomial
> **Corollary 4.** For $N\ge0$,
>
> $$
> \boxed{D_N(x)=\sum_{k=0}^{\lfloor N/2\rfloor}(-1)^k\binom{N-k}{k}x^{2k}}
> \tag{9}
> $$
>
> The degree is $2\lfloor N/2\rfloor$. In particular, for odd $N$ it is one less than $N$.

> [!note]- Proof of the coefficient formula
> **Proof.** After division by $m^N$, each matching with $k$ edges in (4) contributes $(-1)^kx^{2k}$. If the selected edge indices are $i_1<\cdots<i_k$ and consecutive indices differ by at least $2$, the numbers $i_j-(j-1)$ form an arbitrary $k$-element subset of $\{1,\ldots,N-k\}$. There are $\binom{N-k}{k}$ such subsets. The leading coefficient is nonzero, giving the degree. $\square$

For $N\ge3$, there is an internal core, so $2s\le m$ and

$$
0\le x\le\frac{\lfloor m/2\rfloor-1}{m}<\frac12
$$

The admissible values for fixed $m$ are discrete. For $N=2$, there is no internal core and only $1\le s\le m-1$ is required, giving a wider range. For $N=1$, there are no seams and $D_1=1$ is independent of the formal variable $x$.

## Chebyshev polynomials and the auxiliary spectrum

Chebyshev polynomials of the **second kind** satisfy [DLMF, Table 18.9.1](https://dlmf.nist.gov/18.9.i):

$$
U_0(z)=1,\qquad U_1(z)=2z,\qquad
U_N(z)=2zU_{N-1}(z)-U_{N-2}(z)
$$

> [!info] Chebyshev form of the spanning-tree polynomial
> **Corollary 5.** For $x\ne0$,
>
> $$
> \boxed{D_N(x)=x^NU_N\!\left(\frac1{2x}\right)}
> \tag{10}
> $$
>
> After expansion, the right-hand side is a polynomial and extends to $x=0$, where $D_N(0)=1$. Equivalently, for $\ell\ne0$, one has $\tau_N=\ell^NU_N(m/(2\ell))$.

> [!note]- Proof of Corollary 5
> **Proof.** Multiply the recurrence for $U_N$ at $z=1/(2x)$ by $x^N$. This gives (8) and the initial values $1,1$, which uniquely determine the sequence. Formula (9) shows that the singularity at $x=0$ is removable. $\square$

To clarify the spectral meaning, let $\mathbf A_N$ be the adjacency matrix of the auxiliary path $P_N$ on cores. Then

$$
\mathbf M_N=mI-\ell\mathbf A_N,\qquad
D_N(x)=\det(I-x\mathbf A_N)
\tag{11}
$$

This is not the path Laplacian: $\mathbf A_N$ has zero diagonal, whereas the diagonal $m$ of $\mathbf M_N$ also accounts for edges to the outer dual vertex. The matrix $\mathbf M_N$ must not be identified with the Laplacian of the original graph on $n$ vertices.

The characteristic polynomial of the path adjacency matrix satisfies

$$
\chi_{\mathbf A_N}(\xi)=\det(\xi I-\mathbf A_N)=U_N(\xi/2),\qquad
D_N(x)=x^N\chi_{\mathbf A_N}(1/x)
\tag{12}
$$

For $x\ne0$, the second expression reverses a polynomial with the appropriate multiplier; it does not say $D_N(x)=\chi_{\mathbf A_N}(x)$. For example, $\chi_{\mathbf A_3}(\xi)=\xi^3-2\xi$, whereas $D_3(x)=1-2x^2$.

> [!info] Positivity of the normalized polynomial
> **Corollary 6.** The polynomial $D_N(x)$ is positive on $0\le x\le1/2$; for $N\ge2$, it is strictly decreasing on this interval. For $N\ge2$, its smallest positive root is $1/(2\cos(\pi/(N+1)))>1/2$.

> [!note]- Spectral formulas and proof of Corollary 6
> **Proof.** The determinants $\det(\xi I-\mathbf A_N)$ have initial values $1,\xi$ and recurrence $c_N=\xi c_{N-1}-c_{N-2}$. This is the recurrence for $U_N(\xi/2)$, proving the first formula in (12); the second follows by factoring $x$ from each row.
>
> The path eigenvectors have coordinates $v_i=\sin(\pi ji/(N+1))$, $1\le i\le N$. Substitution with $v_0=v_{N+1}=0$ gives eigenvalues $2\cos(\pi j/(N+1))$, $1\le j\le N$. They are distinct and exhaust the spectrum. Pairing opposite eigenvalues gives
>
> $$
> D_N(x)=\prod_{j=1}^{\lfloor N/2\rfloor}
> \left(1-4x^2\cos^2\frac{\pi j}{N+1}\right)
> $$
>
> For $N\ge2$, the smallest positive root is $1/(2\cos(\pi/(N+1)))>1/2$. Hence all factors are positive on $[0,1/2]$ and strictly decrease as $x$ increases within that interval. $\square$

Corollary 6 concerns the normalized spanning-tree count for fixed $N$. It gives no universal law for the radius or for closing a chain.

At the boundary of the common range, the recurrence $U_N(1)=2U_{N-1}(1)-U_{N-2}(1)$ gives $U_N(1)=N+1$, so

$$
D_N(1/2)=\frac{N+1}{2^N}
$$

For a finite homogeneous chain with $N\ge3$, $x=1/2$ is inadmissible. For fixed $N$, it can be approached as a limit, for example through even $m\to\infty$ with $s=m/2$. More generally, if $s(m)/m\to x$, then $\tau_N(m,s(m))/m^N\to D_N(x)$ by the exact normalization (7) and continuity of the polynomial.

The role of Chebyshev polynomials in transformations of the **Laplacian** is discussed separately in [[en/Spectra and diagonalization in polyform algebra/Chebyshev Transformations of the Laplacian - From Path to Cycle|Chebyshev Transformations of the Laplacian - From Path to Cycle]]. Here we use the **adjacency** matrix of the path on cores. The constructions share an algebraic tool but have different operators and graph interpretations.

## Distinguishing the polynomials

> [!info] Construction parameters, ordinary forests, and the spectrum
> **The spanning-tree polynomial $\mathcal T_N$** depends on core and seam sizes. On admissible integer data it gives one number, $\tau(G)$.
>
> **The ordinary forest polynomial** of a fixed graph is $F_G(t)=\sum_g f_g(G)t^g$: $f_g$ counts spanning forests with $g$ edges and no selected roots. For a connected graph, $f_{n-1}=\tau(G)$.
>
> **The Laplacian polynomial** $P_G(t)=\det(I+t\mathbf L_G)=\sum_g p_g(G)t^g$ has rooted forest coefficients. The Laplacian characteristic polynomial is $\chi_G(\xi)=\det(\xi I-\mathbf L_G)$, with $\chi_G(\xi)=\xi^nP_G(-1/\xi)$ as a polynomial identity.

Definitions and the relation between the two forest normalizations appear in [[en/Matroid parameters and forest characteristics of graphs/Forest Coefficients - Grade, Components, and Corank|Forest Coefficients - Grade, Components, and Corank]] and [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]. The alternating coefficients of $\mathcal T_N$ and $D_N$ do not replace $f_g$ or $p_g$. The spectrum of $\mathbf A_N$ in (12) concerns only the auxiliary path. Equality of spanning-tree counts proves neither equality of forest polynomials nor equality of radii; in [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]], those consequences follow from the stronger fact of cycle matroid isomorphism.

## Explicit assemblies and independent checks

Use the following exact numbering rule for the table below. The first core has cyclic order $0,\ldots,m_1-1$. To attach the second, take the first $s_1$ vertices of the first. At each later step, identify the input of the new core, in the same order, with the $s_{j-1}$ vertices of the preceding core immediately following its input seam. The new core's cyclic list starts with these shared vertices and is completed by $m_j-s_{j-1}$ new labels in increasing order.

Thus the input and output of an internal core occupy disjoint segments of its cyclic list. The final edge set is the union of the cyclic edges of all lists, counting coincidences once. This specifies cores, seams, vertex correspondences, and the graph independently of a drawing. Complete lists and edge sets are saved in the [exact results file](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/spanning-polynomials-results.json).

| Core sizes | Seams in vertices | $n$ | Edge count | $\tau$ |
|---|---|---:|---:|---:|
| $(6,6,6)$ | $(2,2)$ | $14$ | $16$ | $204$ |
| $(8,8,8)$ | $(3,3)$ | $18$ | $20$ | $448$ |
| $(3,4,5,6)$ | $(1,2,3)$ | $12$ | $15$ | $294$ |
| $(3,5,6)$ | $(1,2)$ | $11$ | $13$ | $87$ |
| $(3,5,6)$ | $(2,1)$ | $11$ | $13$ | $84$ |
| $(8,8,8,8)$ | $(1,2,3)$ | $26$ | $29$ | $3776$ |
| $(8,8,8,8)$ | $(2,1,3)$ | $26$ | $29$ | $3780$ |
| $(8,8,8,8)$ | $(1,3,2)$ | $26$ | $29$ | $3776$ |

Here $\tau$ is computed directly as a Laplacian minor of the **assembled original graph**. It is compared with the dual determinant, recurrence, and matching sum. For $N=3$, $m_i=6$, $s_i=2$, this rule places the middle core's output immediately after its input; the opposite-output variant is checked separately and also gives $204$.

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/verify_spanning_polynomials.py) checks $76$ configurations and $286$ subchain Laplacian minors in exact arithmetic. It checks connectivity, exact intersections and absence of additional contacts, vertex and edge counts, both correspondence directions, one-vertex and multi-edge seams, different core sizes, and the case $s_{i-1}+s_i=m_i$. All permutations of seam sizes $(1,2,3)$ and $(2,3,4)$ are checked for four octagons.

The algebraic part independently compares the permutation expansion of the determinant with (4) for $1\le N\le7$, and the coefficients from the recurrence, binomial formula, and transformed $U_N$ polynomials for $0\le N\le20$. It also checks characteristic determinants of the auxiliary path and the boundary value $x=1/2$. See the [reproduction and drawing instructions](https://github.com/magin67/pmg-notes/blob/v5/checks/core-chains/README.md).

The general formulas are proved in the text; finite computations check examples and implementation. Branching, disconnected seams, and cores other than cycles are treated in [[en/Chains of cores/Limits of Invariance - Branching, Disconnected Seams, and Other Cores|Limits of Invariance - Branching, Disconnected Seams, and Other Cores]], and ordinary and twisted closures in [[en/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain - Rings and the Möbius Effect]]. Matrix (1) does not transfer automatically to these models.

## Sources and connections

1. H. Chen, B. Mohar. *The sandpile group of a polygon flower*. [§3, Lemma 3.1 and the following paragraph](https://arxiv.org/html/1907.08450v1#S3). The spanning-tree recurrence for single-edge gluings and independence from seam placement for a fixed order of core sizes.
2. NIST Digital Library of Mathematical Functions. [§18.9(i), Table 18.9.1](https://dlmf.nist.gov/18.9.i). The Chebyshev recurrence used in (10).

Chain definitions: [[en/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. The dual graph and matroid consequences: [[en/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. Forest and spectral normalizations: [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]].

Reading routes, applicability conditions, and the origins of results: [[en/Chains of cores/Chains of Cores|Chains of Cores navigator]].
