---
title: "Chebyshev Transformations of the Laplacian: From Path to Cycle"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: chebyshev-transformations-of-the-laplacian
order: 4
description: "Chebyshev polynomials of the path Laplacian, the transition to a cycle, folding a doubled cycle, and classification of the orbit. Eigenprojectors, polyforms, and duality."
---

[[ru/Спектры и диагонализация в алгебре полиформ/Чебышёвские преобразования лапласиана - от пути к циклу|Русский]]

Eigendirections can be preserved while changing the multipliers along them. For a path, transformations that multiply the spectral angle are especially natural: doubling turns the path into a relabeled cycle, while other integer multipliers give paths, cycles, or several components. The coefficients of diagonal polyforms and the resistance geometry change along with them.

[[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]] derives eigenbases for both families. Here we establish the graph meaning of polynomial transformations and carry them into exterior exponential factorizations. We use classical Chebyshev formulas and quotient matrices of equitable partitions; the specific classification of the orbit is derived in the text.

## A polynomial in an operator and a fixed metric

Let $\mathbf L$ be the ordinary symmetric Laplacian of a connected undirected graph. Fix the coordinate inner product $\langle\mathbf z,\mathbf y\rangle_0=\mathbf z^{\mathsf T}\mathbf y$. Let $\mathbf u_0=\mathbf1/\sqrt n,\mathbf u_1,\ldots,\mathbf u_d$, $d=n-1$, be an orthonormal eigenbasis, and put $H=\mathbf1^\perp$. Identify columns in $H$ with vectors of $W$ by $u=\sum_i u(i)a_i$.

For a real polynomial $f(\xi)=\sum_{r=0}^s c_r\xi^r$, define

$$
f(\mathbf L)=\sum_{r=0}^s c_r\mathbf L^r
$$

Powers here mean matrix composition. If $\mathbf L\mathbf u_k=\lambda_k\mathbf u_k$, then

$$
f(\mathbf L)\mathbf u_k=f(\lambda_k)\mathbf u_k
$$

> [!note]- Proof
> **Proof.** Induction gives $\mathbf L^r\mathbf u_k=\lambda_k^r\mathbf u_k$. A linear combination of these identities proves the assertion. $\square$

Thus the original eigenbasis remains an eigenbasis. If several values $f(\lambda_k)$ coincide, the corresponding eigenspace is the sum of the original eigenspaces, and its projector is the sum of their projectors. This is standard spectral calculus for a symmetric matrix, consistent with simultaneous diagonalization [Brouwer–Haemers, §2.1](https://aeb.win.tue.nl/2WF02/spectra.pdf#page=31).

The condition $f(0)=0$ preserves the constant zero mode. Nonnegativity of $f(\lambda_k)$ ensures positive semidefiniteness, but a graph Laplacian also needs nonpositive off-diagonal entries. For example, $\mathbf L_{P_n}^2$ has entry $(1,3)$ equal to $1$ for $n\ge3$, so it is not a graph Laplacian with nonnegative conductances.

The coordinate inner product stays fixed throughout the transformation. The resistance metric determined by the new Greenian may change. This distinction is established in [[en/Foundations/Core specification|Core specification]] and [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]].

## Polynomials that multiply the spectral angle

The classical formula $T_m(\cos\theta)=\cos(m\theta)$ for Chebyshev polynomials of the first kind appears in [DLMF, formula 18.5.1](https://dlmf.nist.gov/18.5.E1). Apply it to the Laplacian variable $\xi=2-2\cos\theta$.

> [!info] Polynomials that multiply the spectral angle
> **Definition.** For an integer $m\ge0$, put
>
> $$
> \Phi_m(\xi)=2-2T_m\left(1-\frac\xi2\right)
> $$

Then

$$
\boxed{\Phi_m(2-2\cos\theta)=2-2\cos(m\theta)}
$$

The first polynomials are

$$
\Phi_0(\xi)=0,\qquad \Phi_1(\xi)=\xi,\qquad
\Phi_2(\xi)=\xi(4-\xi),\qquad
\Phi_3(\xi)=\xi(\xi-3)^2
$$

The Chebyshev three-term recurrence ([DLMF, §18.9(i), Table 18.9.1](https://dlmf.nist.gov/18.9.i)) gives

$$
\Phi_{m+1}(\xi)=2\xi+(2-\xi)\Phi_m(\xi)-\Phi_{m-1}(\xi)
$$

Successive angle multiplications give the composition

$$
\Phi_p(\Phi_q(\xi))=\Phi_{pq}(\xi)=\Phi_q(\Phi_p(\xi))
$$

This is a polynomial identity: trigonometric substitution proves it on the entire interval $[0,4]$, hence it holds for every $\xi$. In particular,

$$
\Phi_{2m}(\xi)=\Phi_m(\xi)\bigl(4-\Phi_m(\xi)\bigr)
$$

The variable $\xi$ is the argument of a spectral polynomial, not a vertex variable in a toponome.

## The Chebyshev orbit of a path

Let $P_n$ have unit conductances, with $n\ge2$. Its eigenvalues and normalized nonzero modes are

$$
\lambda_k=2-2\cos\frac{\pi k}{n},\qquad
u_k(i)=\sqrt{\frac2n}\cos\frac{\pi k(i-1/2)}n,\qquad 1\le k<n
$$

The constant mode corresponds to $\lambda_0=0$. Derivation and normalization appear in [[en/Spectra and diagonalization in polyform algebra/Eigenmodes of Paths and Cycles|Eigenmodes of Paths and Cycles]]; an external account of path and cycle formulas is [Perera–Mizoguchi](https://arxiv.org/abs/1210.7253).

Write

$$
\mathbf L^{(m)}=\Phi_m(\mathbf L_{P_n}),\qquad
\mu_k^{(m)}=2-2\cos\frac{\pi mk}{n}
$$

Call the family $\{\mathbf L^{(m)}\}_{m\ge0}$ the **Chebyshev orbit of the path**. The name is used here for this particular matrix family. The superscript $(m)$ distinguishes the transformation index from a polyform grade.

All matrices in the orbit are diagonal in the path basis and satisfy

$$
\mathbf L^{(m)}\mathbf u_k=\mu_k^{(m)}\mathbf u_k,\qquad
\mathbf L^{(m+2n)}=\mathbf L^{(m)},\qquad
\mathbf L^{(2n-m)}=\mathbf L^{(m)}
$$

The last equalities follow from periodicity and evenness of cosine on each basis vector. It therefore suffices to consider $0\le m\le n$. The values $\mu_k^{(m)}$ are nonnegative; we will prove the graph sign conditions through an explicit adjacency rule.

## Angle doubling turns a path into a cycle

> [!info] Angle doubling turns a path into a cycle
> **Theorem.** For $n\ge3$, the matrix
>
> $$
> \boxed{\mathbf L^{(2)}=4\mathbf L_{P_n}-\mathbf L_{P_n}^{\,2}}
> $$
>
> is the Laplacian of a simple cycle with edges
>
> $$
> \{1,2\},\quad \{n-1,n\},\quad \{i,i+2\}\ (1\le i\le n-2)
> $$

> [!note]- Proof
> **Proof.** For adjacent path vertices $i,j$, $(\mathbf L^2)_{ij}=-(\deg i+\deg j)$. Thus $4\mathbf L-\mathbf L^2$ retains the two end edges with coefficient $-1$, while all other adjacent-pair coefficients vanish. At distance $2$, the entry of $\mathbf L^2$ is $1$, giving a new edge with coefficient $-1$. All remaining off-diagonal entries vanish.
>
> Row sums are zero, and each vertex of the resulting graph has degree $2$. The graph is connected: starting at $1$, visit even vertices in increasing order and then odd vertices in decreasing order, returning to $1$. It is a cycle, and its Laplacian diagonal entries are $2$. $\square$

For $n=6$, the traversal is

$$
1\longrightarrow2\longrightarrow4\longrightarrow6\longrightarrow5\longrightarrow3\longrightarrow1
$$

If the columns of the permutation matrix $\mathbf P$ list the vertices in this order, then $\mathbf P^{\mathsf T}\mathbf L^{(2)}\mathbf P=\mathbf L_{C_6}$ for standard cyclic labeling. Thus the statement concerns the matrix itself, not merely its spectrum.

![[Chebyshev Transition from P6 to a Cycle.svg]]

*Figure 1. Left: the original path. Right: the resulting cycle with the original vertex labels. The two end edges are retained, and pairs at distance two become adjacent. The table shows how eigenvalues change in the fixed path basis and gives the reciprocal nonzero eigenvalues of the new Greenian.*

In the path basis, the transformed values for $k=1,\ldots,5$ occur in the order $1,3,4,3,1$. The new cycle projectors are therefore

$$
\mathbf E_{1}^{\mathrm{new}}=\mathbf E_1^P+\mathbf E_5^P,\qquad
\mathbf E_{3}^{\mathrm{new}}=\mathbf E_2^P+\mathbf E_4^P,\qquad
\mathbf E_{4}^{\mathrm{new}}=\mathbf E_3^P
$$

Indices on the left denote eigenvalues; indices on the right denote path modes. A sine-cosine basis for the standard labeling of $C_6$ is obtained after permuting vertices and choosing a basis in each two-dimensional eigenspace.

## Folding the doubled cycle

For general $m$, use indices $j\in\mathbb Z/(2n)$ and the reflection $j\mapsto-j-1$. It fixes no vertex, so every reflection orbit contains two vertices. Let $\pi_n(j)$ be the unique orbit representative among $0,\ldots,n-1$. Representative $i$ corresponds to vertex $i+1$ of the original path.

On the doubled cycle, introduce the step operator

$$
(\mathbf K_m F)(j)=2F(j)-F(j+m)-F(j-m)
$$

For $1\le m<n$, this is the ordinary Laplacian of the graph with steps $\pm m$. The subspace of functions $F(j)=f(\pi_n(j))$, constant on reflection orbits, is invariant. Restriction to it is given by

$$
(\mathbf A_m f)(i)=2f(i)-f(\pi_n(i+m))-f(\pi_n(i-m))
$$

This is the quotient matrix of an equitable partition into reflected vertex pairs. Equitability means that the total transition coefficient from a vertex in one class to another class is independent of the selected vertex in the first class. Here reflection, which permutes neighbors, ensures this property. The general quotient construction and lifting of eigenvectors are given by [Brouwer–Haemers, §2.3, Lemma 2.3.1](https://aeb.win.tue.nl/2WF02/spectra.pdf#page=34). All classes have the same size, so the normalized lift $F(j)=f(\pi_n(j))/\sqrt2$ preserves the coordinate inner product and the quotient matrix is symmetric.

> [!info] Folding the doubled cycle
> **Lemma.** $\mathbf A_m=\mathbf L^{(m)}$.

> [!note]- Proof
> **Proof.** Extend a path cosine mode to $2n$ indices:
>
> $$
> F_k(j)=\cos\left(\left(j+\frac12\right)\theta_k\right),\qquad
> \theta_k=\frac{\pi k}{n}
> $$
>
> It has period $2n$ and is reflection-invariant. The cosine sum formula gives
>
> $$
> F_k(j+m)+F_k(j-m)=2\cos(m\theta_k)F_k(j)
> $$
>
> Thus $\mathbf A_m$ acts on the complete path basis with multipliers $2-2\cos(m\theta_k)=\mu_k^{(m)}$. They agree with those of $\mathbf L^{(m)}$, proving matrix equality. $\square$

The adjacency formula also checks the signs: every transition to another orbit gives a negative off-diagonal entry. If $\pi_n(i\pm m)=i$, that term reduces the diagonal; no loop appears in the Laplacian. For $1\le m<n$, the two neighbors cannot coincide: equality modulo the period would require $2m\equiv0\pmod{2n}$, and equality through reflection would require the impossible congruence $2i\equiv-1\pmod{2n}$. Every nonzero conductance is therefore $1$.

## Which graphs occur in the orbit

> [!info] Which graphs occur in the orbit
> **Theorem.** Let $1\le m<n$, and let $\Gamma_m$ be the graph with Laplacian $\mathbf L^{(m)}$.
>
> If $m$ is odd and $q=\gcd(m,n)$, then
>
> $$
> \Gamma_m\simeq P_{n/q}\;\sqcup\;\frac{q-1}{2}C_{2n/q}
> $$
>
> If $m=2r$ is even and $q=\gcd(r,n)$, then
>
> $$
> \Gamma_m\simeq qC_{n/q}
> $$
>
> A number preceding a graph symbol denotes the number of disjoint copies, and $\sqcup$ denotes disjoint union.

> [!note]- Proof
> **Proof.** Step $m$ splits $\mathbb Z/(2n)$ into $s=\gcd(m,2n)$ cycles of length $2n/s$. Their components are indexed by residues modulo $s$, and reflection acts on them as $a\mapsto-a-1$.
>
> For odd $m$, $s=q$ is also odd. The congruence $2a\equiv-1\pmod q$ has exactly one solution. The corresponding cycle is invariant under reflection; reflection fixes none of its vertices, and folding gives a path on $n/q$ vertices. The remaining $q-1$ cycles are paired, each pair giving one cycle of the original length $2n/q$.
>
> For even $m=2r$, $s=2q$. The congruence $2a\equiv-1\pmod{2q}$ has no solution, so all components are paired. The result is $q$ cycles of length $n/q$. For $m<n$, this length is at least $3$. $\square$

Connectedness is therefore equivalent to $\gcd(m,n)=1$ for odd $m$ and $\gcd(m/2,n)=1$ for even $m$. Connected graphs in this range are relabeled copies of $P_n$ or $C_n$.

The extreme values require separate treatment. At $m=0$ the matrix is zero. At $m=n$, the steps $+n$ and $-n$ coincide, and after folding,

$$
(\mathbf L^{(n)}f)(i)=2f(i)-2f(n-1-i)
$$

This gives edges of conductance $2$ between mirror vertices. For odd $n$, the central vertex is isolated. This is a weighted graph, not a simple graph with unit conductances.

![[Graphs in the Chebyshev Orbit of P6.svg]]

*Figure 2. Steps $m=1,\ldots,5$ and the extreme step $m=6$ for $P_6$. Original vertex labels are preserved. At $m=3$ the result is $P_2$ and $C_4$; at $m=4$, two triangles. In both cases the Laplacian has rank $4$ and is singular on the five-dimensional space $H$. More components mean a higher multiplicity of the zero eigenvalue. Labels 2 on the last diagram denote conductances.*

## Transforming diagonal polyforms

Put $A_k=[u_k]^2$ for the nonzero modes of the original path. At step $m$, the forms $A_k$ are preserved and their coefficients change:

$$
L^{(m)}=\sum_{k=1}^{d}\mu_k^{(m)}A_k,\qquad
M^{(m)}(t)=\exp(tL^{(m)})=\prod_{k=1}^{d}\bigl(e+t\mu_k^{(m)}A_k\bigr)
$$

In particular, grade $g$ is the elementary symmetric polynomial

$$
M_g^{(m)}=e_g\bigl(\mu_1^{(m)}A_1,\ldots,\mu_d^{(m)}A_d\bigr)
$$

This applies the factorization from [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]] and shows how eigenvalue changes propagate through all grades. Form multiplication here is exterior multiplication. Substituting $\Phi_m(L)$ with this product does not define $L^{(m)}$: for example, the exterior form $L^2$ has grade $2$, whereas the matrix $\mathbf L^2$ still represents an operator on the original space.

For the transition $P_6\to\Gamma_2$,

$$
M^{(2)}(t)=(e+tA_1)(e+3tA_2)(e+4tA_3)(e+3tA_4)(e+tA_5)
$$

The original path eigendirections provide a basis for this entire expression. Repeated eigenvalues allow factors to be grouped by eigenspaces, as in [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]].

## The Greenian, complementary grades, and new zero modes

First suppose $\Gamma_m$ is connected. Every $\mu_k^{(m)}$, $1\le k\le d$, is then positive, and

$$
\mathbf{Gr}^{(m)}=\sum_{k=1}^{d}\frac{\mathbf u_k\mathbf u_k^{\mathsf T}}{\mu_k^{(m)}},\qquad
\mathrm{Gr}^{(m)}=\sum_{k=1}^{d}\frac{A_k}{\mu_k^{(m)}}
$$

In the algebraically dual basis $u^1,\ldots,u^d$, put $A_k^\vee=[u^k]^2$. Then

$$
D^{(m)}(t)=\exp(tQ_1^{(m)})=
\prod_{k=1}^{d}\left(e+\frac{tA_k^\vee}{\mu_k^{(m)}}\right)
$$

The centered identification $\mathcal C:a_i^\vee\mapsto a_i-h$, $h=n^{-1}\sum_i a_i$, sends $A_k^\vee$ to $A_k$ and $D^{(m)}(t)$ to $\exp(t\mathrm{Gr}^{(m)})$. It uses the fixed coordinate metric; resistance pairing changes with $\mathbf{Gr}^{(m)}$.

Here $t$ is the grade parameter of the dual pair at $t=1$. Multiplying conductances by $s>0$ gives the pair $M^{(m)}(s)$, $D^{(m)}(s^{-1})$; see the [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality#The grade parameter and rescaling a dual pair|parameter convention]].

For a set $I\subseteq\{1,\ldots,d\}$ and its complement $I^c$,

$$
\prod_{k\in I}\frac1{\mu_k^{(m)}}=
\frac{\prod_{k\in I^c}\mu_k^{(m)}}{\Delta_m},\qquad
\Delta_m=\prod_{k=1}^{d}\mu_k^{(m)}=n\tau(\Gamma_m)
$$

Duality therefore still reverses complementary grades: $M_d^{(m)}/Q_g^{(m)}=M_{d-g}^{(m)}$. The coefficients and the normalizing factor $\Delta_m$ change.

For $P_6$, $\Delta_1=6$; for $\Gamma_2\simeq C_6$, $\Delta_2=36$. With $N^{(m)}=\exp(\mathrm{Gr}^{(m)})$, the top grades are consequently

$$
M_5^{(1)}=T_6,\qquad M_5^{(2)}=6T_6,\qquad
N_5^{(1)}=\frac{T_6}{36},\qquad N_5^{(2)}=\frac{T_6}{216}
$$

The effective resistance between fixed vertices also changes. For the pair $1,6$, it was $5$ on the path; after transformation it is

$$
R_{16}^{(2)}=\frac{2+\sqrt3}{3}+\frac16+\frac{2-\sqrt3}{3}=\frac32
$$

The three summands correspond to the original path modes $k=1,3,5$. In the new cycle, vertices $1$ and $6$ are opposite, independently giving resistance $3/2$.

If $\Gamma_m$ is disconnected, some $\mu_k^{(m)}$ vanish. The matrix pseudoinverse remains defined:

$$
\mathbf{Gr}^{(m)}=
\sum_{k:\,\mu_k^{(m)}>0}\frac{\mathbf u_k\mathbf u_k^{\mathsf T}}{\mu_k^{(m)}}
$$

It no longer induces a nondegenerate metric on all of $H$. Put $r_m=\operatorname{rank}\mathbf L^{(m)}$. The Laplacian and Greenian exterior exponentials have nonzero grades only up to $r_m$. Inversion and duality can be considered on $H_m^+=\operatorname{im}\mathbf L^{(m)}$ and its algebraic dual, complementing sets within the $r_m$ positive modes. The connected-case formulas with $d=n-1$ and $\Delta_m=n\tau$ do not apply.

For example, at $n=6$, $m=3$, the transformed values for $k=0,\ldots,5$ are $0,2,4,2,0,2$. Two zero modes correspond to the two components $P_2\sqcup C_4$, and the highest nonzero grade is $4$. A difference of vertices in distinct components does not belong to $H_m^+$; its finite pseudoinverse evaluation is not the electrical resistance between disconnected components.

## Scope and sources

The Chebyshev orbit is a special finite family in a fixed eigenbasis. It does not describe every graph Laplacian diagonal in that basis. For example, $\mathbf L_{K_n}=n\mathbf I-\mathbf1\mathbf1^{\mathsf T}$ is diagonal in any orthonormal basis containing the constant mode; for $n\ge4$, the complete graph is absent from this orbit. Conditions for the entire set of admissible Laplacians are studied in [[en/Spectra and diagonalization in polyform algebra/The Spectral Cone of a Fixed Basis|The Spectral Cone of a Fixed Basis]].

Polynomial spectral calculus, Chebyshev identities, and equitable partitions are classical. The orbit classification is derived here from the step graph on $2n$ vertices and the reflection action; no claim of novelty is made. The polyform expression uses established PMG definitions and normalizations.

Independent computation compares the matrix polynomial recurrence with folding the step graph: 374 matrices were checked for $P_2,\ldots,P_{18}$ and steps $0\le m\le2n+1$, including components, conductances, periodicity, and reflection. For $P_6$, additional checks cover 49 composition pairs, projectors, the Greenian, grades and coefficients, duality of the connected transformation, top-grade normalizations, and effective resistance. These finite checks control formulas and figures; general statements are justified in the text.

- [A. E. Brouwer, W. H. Haemers. Spectra of Graphs, authors' text](https://aeb.win.tue.nl/2WF02/spectra.pdf): §2.1 - simultaneous diagonalization; §2.3 and Lemma 2.3.1 - quotient matrices of equitable partitions. [Book page and corrections](https://homepages.cwi.nl/~aeb/math/ipm/).
- [NIST DLMF, §18.5](https://dlmf.nist.gov/18.5), formula 18.5.1, and [§18.9(i)](https://dlmf.nist.gov/18.9.i), Table 18.9.1: the trigonometric formula and Chebyshev recurrence. The polynomials $\Phi_m$ follow by the variable substitution specified in the text.
- [K. K. K. R. Perera, Y. Mizoguchi. Bipartition of graphs based on the normalized cut and spectral methods](https://arxiv.org/html/1210.7253v2#S4.SS1), § 4.1, Propositions 4.4(2) and 4.8(2): spectra and eigenvectors of the ordinary cycle and path Laplacians, respectively.
- [[en/Foundations/Core specification|Core specification]], [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], and [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]]: spaces, exterior exponentials, and dual normalizations.
- [Checks and figure reproduction](https://github.com/magin67/pmg-notes/tree/v5/checks/spectral): computations for the Chebyshev orbit.

Navigator: [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].
