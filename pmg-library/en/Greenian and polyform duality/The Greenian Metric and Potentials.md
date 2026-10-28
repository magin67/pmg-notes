---
title: The Greenian Metric and Potentials
date: 2026-10-28
updated: 2026-10-28
revision: 2
translated_revision: 3
status: draft
text_prepared_by: ChatGPT
translation_key: greenian-metric-and-potentials
lang: en
description: "Form potentials in the Greenian exponential: the Laplacian as a metric, cut weights, energy of vertex differences, higher-grade determinants, and exact examples."
order: 7
---

[[ru/Гриниан и дуальность полиформ/Метрика и потенциалы гриниана|Русский]]

The Laplacian exponential defines the resistance metric with the Green matrix. In the Greenian exponential, the matrices exchange roles: its normalized potentials are determined by the original Laplacian. Thus Greenian coefficients may have either sign, while norms of nonzero exterior objects remain positive.

For the vector form of $a_{ij}=a_j-a_i=(a_i a_j)$, the normalized potential is $d_i+d_j+2c_{ij}$, where $d_i$ is the sum of conductances incident to vertex $i$. The coupling $c_{ij}$ does indeed enter this value with a total factor of $4$. Below we explain this factor, connect potentials with cuts, and give a formula for arbitrary grade.

## The Greenian exponential and the potential of a form

Let $G$ be a connected undirected graph on $n\ge2$ vertices. Existing edges have positive conductances; $c_{ij}=c_{ji}=0$ for an absent coupling, and $c_{ii}=0$. Write

$$
d_i=\sum_j c_{ij},\qquad
L_{ii}=d_i,\qquad L_{ij}=-c_{ij}\quad(i\ne j),\qquad
\mathbf{Gr}=\mathbf L^+
$$

We work in the space of direct vectors

$$
W=\left\{\sum_i u_i a_i:\ \sum_i u_i=0\right\},\qquad
h=\frac1n\sum_i a_i
$$

Here $a_i$ are independent vertices of the direct space. For the centered vectors $p_i=a_i-h$, we have $\sum_i p_i=0$. Denote dual elements by $a_i^\vee$. The dual representation is transferred to the direct space by $\mathcal C:a_i^\vee\mapsto p_i=a_i-h$, whose meaning is established in [[The Exterior Exponential and Representations of the Greenian]]. All potentials in this note are calculated after this transfer.

The vector forms and their exponentials are

$$
L=\sum_{i<j}c_{ij}[a_{ij}]^2,\qquad
\mathrm{Gr}=\sum_{i<j}\gamma_{ij}[a_{ij}]^2,\qquad
\gamma_{ij}=-\mathrm{Gr}_{ij},\qquad
M=\exp L,\qquad N=\exp(\mathrm{Gr})
$$

For the Greenian,

$$
N=\sum_{k=0}^{n-1}N_k,\qquad
N_k=\frac{\mathrm{Gr}^k}{k!},\qquad N_0=e
$$

Set $T=[(a_1\ldots a_n)]^2$. The functional $\tau$ extracts the coefficient of this top form. By the [[The Canonical Vector Representation of the Greenian|formula for the Greenian's top coefficient]],

$$
N_{n-1}=\sigma T,\qquad
\sigma=\tau(N)=\frac{1}{n^2\tau(G)}>0
$$

**Definition.** The potential of a form $f$ in the Greenian exponential and its normalized value are

$$
u_N(f)=\tau(Nf),\qquad
P_N(f)=\frac{u_N(f)}{u_N(e)}=\frac{\tau(Nf)}{\sigma}
\tag{1}
$$

If $f$ has grade $k$, only $N_{n-1-k}f$ contributes to the numerator. In particular, $P_N(e)=1$. In PMG terminology, the normalized potential is called the norm of the form; for $f=[X]^2$, it is the quadratic norm of the argument $X$.

The coefficient $\gamma_{ij}$ in the Greenian expression must be distinguished from the value $P_N([a_{ij}]^2)$. A coefficient specifies the exponential, whereas a potential is obtained by multiplying the exponential by a given form and extracting the top coefficient. These are different operations.

## The Laplacian as the metric of the Greenian exponential

For $u=\sum_i u_i a_i\in W$, denote its coefficient column by $\mathbf u$; its coordinates sum to zero.

**Theorem.** For $u,v\in W$, the normalized potential of the bilinear form is

$$
\boxed{P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v}
\tag{2}
$$

This is a positive definite inner product on $W$. Denote it by $u\cdot_N v$. For simple exterior objects $X=u_1\cdots u_k$ and $Y=v_1\cdots v_k$, we have

$$
\boxed{
P_N([X,Y])
=\det\bigl(u_\alpha\cdot_N v_\beta\bigr)_{\alpha,\beta=1}^k
=\det(U^{\mathsf T}\mathbf L V)
}
\tag{3}
$$

Here $U,V$ contain the full $n$-coordinate columns of the factors. For $k=0$, the determinant equals $1$. The formula extends bilinearly to arbitrary objects of the same grade.

**Proof.** Choose an auxiliary orthonormal basis of the hyperplane $\mathbf1^\perp$ in the ordinary coordinate space $\mathbb R^n$, and collect its columns in the matrix $E$. This is auxiliary coordinate orthonormality, not the PMG metric being defined.

The Greenian coefficient matrix in this basis is $A=E^{\mathsf T}\mathbf{Gr}E$. It is positive definite, and $A^{-1}=E^{\mathsf T}\mathbf L E$, since $\mathbf{Gr}$ and $\mathbf L$ are mutual inverses on $\mathbf1^\perp$.

Apply the [[Laplacian Exponential#A general lemma on the top-grade coefficient|determinant lemma for the exterior exponential]] to the matrix $A$. The normalized potential equals the determinant of inner products with matrix $A^{-1}$. Passing to full coordinates gives (2) and (3). Changing the reference top form multiplies the numerator and denominator of (1) by the same coefficient and leaves their ratio unchanged.

Positive definiteness of $\mathbf L$ on $\mathbf1^\perp$ implies positive definiteness of all its exterior powers: in an eigenbasis, their diagonal entries are products of positive eigenvalues. Thus $P_N([X]^2)>0$ for every nonzero exterior object $X$, including nonsimple objects. $\square$

In particular,

$$
P_N([u]^2)=\mathbf u^{\mathsf T}\mathbf L\mathbf u
=\sum_{i<j}c_{ij}(u_i-u_j)^2
\tag{4}
$$

Formula (4) is the usual quadratic energy form of a graph. Its connection with cuts and electrical dissipation is standard [1]. The PMG result is that this form arises precisely as the normalized potential in $\exp(\mathrm{Gr})$.

For an arbitrary collection of vertex values $\varphi_i$, set

$$
v_\varphi=\sum_i\varphi_i p_i,\qquad
\mathcal E(\varphi)=\sum_{i<j}c_{ij}(\varphi_i-\varphi_j)^2
$$

Then $P_N([v_\varphi]^2)=\mathcal E(\varphi)$. Adding a common constant to all $\varphi_i$ changes neither the vector nor the energy. Electrically, $\mathcal E$ is the dissipated power at specified voltages; each undirected edge is counted once, so there is no factor of $1/2$. The potential of a form $u_N(f)$ and the electrical potential of a vertex $\varphi_i$ remain distinct concepts.

## Centered vertices, cuts, and differences

### Potentials of centered vertices

Since $\mathbf L\mathbf1=0$, (2) gives

$$
P_N([p_i,p_j])=L_{ij},\qquad
P_N([p_i]^2)=d_i,\qquad
P_N([p_i,p_j])=-c_{ij}\quad(i\ne j)
\tag{5}
$$

Thus, in the Greenian metric, centroid vectors have norms equal to weighted vertex degrees. Their pairwise inner products are the negatives of the original conductances. In the [[The Canonical Vector Representation of the Greenian#Coefficients and centroid geometry|original resistance metric]], the same vectors have inner products $\mathrm{Gr}_{ij}$. The metric matters here.

Formulas (5) concern the vectors $p_i=a_i-h$, not the independent direct vertices $a_i$, which lie outside $W$.

### The potential of a cut form

For a vertex set $A$, define the centered sum

$$
s_A=\sum_{i\in A}p_i,\qquad s_{A^c}=-s_A
$$

For disjoint sets $A,B$, denote their total connecting conductance by

$$
c(A,B)=\sum_{i\in A,\ j\in B}c_{ij}
$$

**Corollary.** The norm of the centered-sum form equals the weight of the corresponding cut:

$$
\boxed{P_N([s_A]^2)=c(A,A^c)}
\tag{6}
$$

For disjoint $A,B$, also

$$
P_N([s_A,s_B])=-c(A,B)
$$

**Proof.** The vector $s_A$ is represented by the indicator of $A$ with its mean subtracted. Centering preserves coordinate differences. In (4), the indicator difference has absolute value $1$ exactly on cut edges; all other terms vanish. The mixed formula follows from $\mathbf1_A^{\mathsf T}\mathbf L\mathbf1_B$; for disjoint sets, only off-diagonal entries $-c_{ij}$ contribute. $\square$

For $A=\varnothing$ or $A=V(G)$, the vector and potential are zero. For a nonempty proper $A$, the value is positive by connectedness.

Potential (6) must be distinguished from the coefficient of the cut form in the [[Cuts and Forest Grades of the Greenian Exponential|forest representation of the Greenian itself]]. After centered transfer, this representation is

$$
\mathrm{Gr}=\sum_{\{A,A^c\}}\widehat\mu_A[s_A]^2,\qquad
\widehat\mu_A=\frac{\tau(G[A])\tau(G[A^c])}{\tau(G)}
$$

Each unordered cut is counted once; the spanning-tree sum is zero for a disconnected induced subgraph and one for a single vertex. The coefficient $\widehat\mu_A$ counts the normalized total weight of two-component spanning forests with the specified components. The value $P_N([s_A]^2)$ measures the weight of edges crossing the cut. For example, in the unit $K_4$, with $A=\{a,b\}$, the coefficient is $1/16$, while the normalized potential is $4$.

### Why the internal coupling receives a factor of four

Let $V(G)=A\sqcup B\sqcup C$. Substituting values $+1$ on $A$, $-1$ on $B$, and $0$ on $C$ into (4) gives

$$
P_N([s_A-s_B]^2)=4c(A,B)+c(A,C)+c(B,C)
\tag{7}
$$

On edges between $A$ and $B$, the value difference is $2$, whose square gives $4$. On edges from these sets to $C$, the squared difference is $1$. Within each set, the difference is zero.

For the vector $a_{ij}=p_j-p_i$, this means

$$
\boxed{
P_N([a_{ij}]^2)=d_i+d_j+2c_{ij}
=4c_{ij}+\sum_{\ell\ne i,j}(c_{i\ell}+c_{j\ell})
}
\tag{8}
$$

Thus $c_{ij}$ already occurs once in $d_i$ and once in $d_j$, and appears twice more through the mixed term. This is not repeated counting of one contribution: the full coefficient is the square of the difference $1-(-1)$ across this coupling.

For the sum of two centered vertices, by contrast,

$$
P_N([p_i+p_j]^2)=d_i+d_j-2c_{ij}
=c(\{i,j\},V(G)\setminus\{i,j\})
$$

The sum assigns equal values to the two vertices and selects their common cut. The difference assigns opposite values and additionally counts the internal coupling with a factor of $4$. The vector norm (8) depends only on couplings incident to its endpoints, although the Greenian's own coefficients $\gamma_{ij}$ depend on the entire graph.

## Resistance and free interior vertices

The two exponentials give different metric evaluations of the same vector. For the column $\mathbf w=\mathbf e_j-\mathbf e_i$, where $\mathbf e_i$ are standard coordinate columns, we have

$$
P_M([a_{ij}]^2)=R_{ij}=\mathbf w^{\mathsf T}\mathbf{Gr}\mathbf w,\qquad
P_N([a_{ij}]^2)=\mathbf w^{\mathsf T}\mathbf L\mathbf w
$$

The resistance $R_{ij}$ equals dissipation under a unit current between the endpoints. The value $P_N([a_{ij}]^2)$ equals dissipation with specified values $-1,+1$ at the endpoints and $0$ at every other vertex. In this problem, the other vertices are fixed, not free.

**Theorem.** If only $\varphi_i=-1$ and $\varphi_j=1$ are prescribed and the other values are free, then

$$
\min_{\varphi_i=-1,\ \varphi_j=1}\mathcal E(\varphi)=\frac4{R_{ij}},\qquad
P_N([a_{ij}]^2)R_{ij}\ge4
\tag{9}
$$

Equality in the second relation holds if and only if $\mathbf w$ is an eigenvector of $\mathbf L$.

**Proof.** Set

$$
\psi=\frac2{R_{ij}}\mathbf{Gr}\mathbf w+t\mathbf1
$$

The difference $\psi_j-\psi_i$ is $2$, so a common constant $t$ can enforce both boundary values. Moreover,

$$
\mathbf L\psi=\frac2{R_{ij}}\mathbf w,\qquad
\mathcal E(\psi)=\frac4{R_{ij}}
$$

At every interior vertex, $\mathbf L\psi$ is zero: this is the harmonic extension of the boundary values. Any other admissible assignment is $\psi+\eta$, where $\eta_i=\eta_j=0$. The mixed term $\eta^{\mathsf T}\mathbf L\psi$ vanishes, so

$$
\mathcal E(\psi+\eta)=\mathcal E(\psi)+\mathcal E(\eta)\ge\mathcal E(\psi)
$$

Substitution of the admissible assignment $\varphi=\mathbf w$ gives the inequality. For the equality condition, apply Cauchy–Schwarz on $\mathbf1^\perp$ to $\mathbf L^{1/2}\mathbf w$ and $\mathbf L^{-1/2}\mathbf w$. Their inner product is $\mathbf w^{\mathsf T}\mathbf w=2$. Equality holds precisely when these columns are linearly dependent, that is, when $\mathbf L\mathbf w$ is proportional to $\mathbf w$. $\square$

The minimization is the classical Dirichlet principle for an electrical network [2]. In (9), the factor $4$ comes from the prescribed difference $2$. For difference $1$, the minimum is the effective conductance $1/R_{ij}$. Thus $P_N([a_{ij}]^2)/4$ generally differs from effective conductance: fixing additional vertices may increase dissipation.

![[Prescribed-values-and-Greenian-energy.svg]]

In the figure, all three edges of the path $a-b-c-d$ have unit conductance. For the difference $b-a$, the specified assignment is $(-1,1,0,0)$, with energy $4+1=5$. For the sum $p_a+p_b$, the assignment $(1,1,0,0)$ may be used: its energy is $1$, concentrated on the cut $ab\mid cd$. If only $a=-1$ and $b=1$ are fixed, the free vertices take values $c=d=1$, and the minimum is $4=4/R_{ab}$. Here $R_{ab}=1$.

## Potentials of higher grades

### A boundary on three vertices

Since $(abc)=(ab)(ac)$, formula (3) gives

$$
P_N([(abc)]^2)
=\det\begin{pmatrix}
d_a+d_b+2c_{ab} & d_a+c_{ab}+c_{ac}-c_{bc}\\
d_a+c_{ab}+c_{ac}-c_{bc} & d_a+d_c+2c_{ac}
\end{pmatrix}
\tag{10}
$$

In other words,

$$
P_N([(abc)]^2)
=(d_a+d_b+2c_{ab})(d_a+d_c+2c_{ac})
-(d_a+c_{ab}+c_{ac}-c_{bc})^2
$$

The degrees $d_a,d_b,d_c$ include couplings to vertices outside the triple. Thus the potential is not determined solely by the induced triangle. Choosing another reference vertex in the boundary factorization changes the vector pair by a transformation of determinant $\pm1$, leaving the result unchanged.

### Expansion through original edges

**Theorem.** Choose an arbitrary orientation of the edges of the original undirected graph. Let $B$ be the matrix of coordinates of their vectors: the column for edge $e=(i,j)$ is $\mathbf e_j-\mathbf e_i$. For $X=u_1\cdots u_k$ and the column matrix $U$,

$$
\boxed{
P_N([X]^2)
=\sum_{\substack{S\subseteq E(G)\\\#S=k}}
\left(\prod_{e\in S}c_e\right)\det(U^{\mathsf T}B_S)^2
}
\tag{11}
$$

Here $B_S$ contains the selected columns, and $c_e$ is the conductance of an original edge.

**Proof.** With $C=\operatorname{diag}(c_e)$, we have $\mathbf L=BCB^{\mathsf T}$. Substitute this decomposition into $\det(U^{\mathsf T}\mathbf L U)$ and apply Cauchy–Binet. Selecting $k$ columns gives the product of their conductances and two identical determinants $\det(U^{\mathsf T}B_S)$. This yields (11). $\square$

Every term in (11) is nonnegative. Reversing an edge's chosen orientation changes the sign of one column, which disappears when the determinant is squared. If $S$ contains a cycle, the columns of $B_S$ are dependent and its contribution vanishes. Thus the sum may run over spanning forests with $k$ edges, including isolated vertices; some of these forests may also contribute zero.

For a boundary on vertices, the matrices $U$ and $B_S$ are integer matrices, so the numerical factors multiplying products of conductances are squares of integer determinants. There is no factor $1/k!$ in (11): each edge set is already counted once.

Formula (11) calculates the potential of a **specified form** through the original positive conductances. It differs both from the expansion of grade $N_k$ using signed coefficients $\gamma_{ij}$ and from the representation of the complementary dual grade through forests of the original graph.

### Where the path coefficients come from

Consider the path $a-b-c-d$ with conductances $p,q,r$ on successive edges. For $X=(abc)$, take columns $U=((ab),(ac))$. Coordinate pairwise products with the three edges give

$$
U^{\mathsf T}B=
\begin{pmatrix}2&-1&0\\1&1&-1\end{pmatrix}
$$

These are auxiliary coordinate products used in (11), not inner products of the PMG metric.

| Selected edges | Product of conductances | Squared determinant | Contribution |
|---|---|---|---|
| $ab,bc$ | $pq$ | $9$ | $9pq$ |
| $ab,cd$ | $pr$ | $4$ | $4pr$ |
| $bc,cd$ | $qr$ | $1$ | $qr$ |

Thus

$$
\boxed{P_N([(abc)]^2)=9pq+4pr+qr}
\tag{12}
$$

The coefficients $9,4,1$ express the pairing of the chosen boundary with pairs of edges. They are not an additional grade normalization.

## Examples and the top form

### A path on four vertices

For the unit path, $\tau(G)=1$ and $\sigma=1/16$. For the path with conductances $(p,q,r)=(2,3,5)$, we have $\tau(G)=30$ and $\sigma=1/480$. With letter indices, write $a_{ab}=b-a$, and similarly for other pairs. The table gives **normalized** potentials; multiply by the corresponding $\sigma$ to obtain unnormalized potentials.

| Form $f$ | $P_N(f)$, unit path | $P_N(f)$, weights $2,3,5$ |
|---|---|---|
| $[a_{ab}]^2$ | $5$ | $11$ |
| $[a_{ac}]^2$ | $3$ | $10$ |
| $[a_{ad}]^2$ | $2$ | $7$ |
| $[a_{bc}]^2$ | $6$ | $19$ |
| $[a_{bd}]^2$ | $3$ | $10$ |
| $[a_{cd}]^2$ | $5$ | $23$ |
| $[(abc)]^2$ | $14$ | $109$ |
| $[(abd)]^2$ | $6$ | $61$ |
| $[(acd)]^2$ | $6$ | $61$ |
| $[(bcd)]^2$ | $14$ | $181$ |
| $T=[(abcd)]^2$ | $16$ | $480$ |

For example, for the unit path, $u_N([a_{ab}]^2)=5/16$ and $u_N([(abc)]^2)=7/8$. For cut forms,

$$
P_N([s_{\{a,b\}}]^2)=q,\qquad
P_N([s_{\{a,c\}}]^2)=p+q+r
$$

The second sum corresponds to the cut crossing all three edges.

### A triangle

Let $p=c_{ab}$, $q=c_{ac}$, and $r=c_{bc}$. Then

$$
\begin{aligned}
P_N([a_{ab}]^2)&=4p+q+r\\
P_N([a_{ac}]^2)&=p+4q+r\\
P_N([a_{bc}]^2)&=p+q+4r\\
P_N([(abc)]^2)&=9(pq+pr+qr)
\end{aligned}
$$

The last form is the top form. For the unit triangle, vector norms are $6$, and the top boundary norm is $27$. For $(p,q,r)=(2,3,5)$, the values are $16,19,25$ and $279$, respectively.

### The complete graph

For $K_n$ with uniform conductance $c>0$, we have

$$
\mathbf L=nc\left(I-\frac1n\mathbf1\mathbf1^{\mathsf T}\right),\qquad
P_N([p_i]^2)=(n-1)c,\qquad
P_N([a_{ij}]^2)=2nc
$$

A cut with $m$ vertices on one side has potential $m(n-m)c$. For a boundary of grade $k$ on any $k+1$ distinct vertices,

$$
\boxed{P_N([(a_{i_0}\ldots a_{i_k})]^2)=(k+1)(nc)^k}
\tag{13}
$$

Indeed, take differences with a common initial vertex. Their coordinate matrix satisfies $U^{\mathsf T}U=I_k+\mathbf1\mathbf1^{\mathsf T}$, whose determinant is $k+1$. On $W$, the Laplacian acts by multiplication by $nc$, and (3) gives (13). For $K_4$ with $c=1$, the values by grade are $1,8,48,256$.

### Normalization of the top potential

For any graph under consideration, the positive grades of $N$ vanish when multiplied by $T$. Thus $NT=T$, and

$$
u_N(T)=1,\qquad
\boxed{P_N(T)=\frac1\sigma=n^2\tau(G)}
\tag{14}
$$

This agrees with the Greenian's own top grade $N_{n-1}=T/(n^2\tau(G))$. The coefficient of the top form and its normalized potential are reciprocals. For a tree with unit conductances, they are $1/n^2$ and $n^2$, respectively; no change to the adopted normalization is needed.

## Status of results and verification

Identities (2)–(14) are proved for a connected undirected graph with positive conductances. Positivity of quadratic-form potentials follows from positive definiteness of the Laplacian on $W$; negative coefficients $\gamma_{ij}$ do not contradict it. Mixed forms may have negative potentials, as already shown by $P_N([p_i,p_j])=-c_{ij}$.

The examples are also checked by an [exact-arithmetic script](https://github.com/magin67/pmg-notes/blob/v5/checks/dual/verify_potentials.py). It constructs $N$ as a product of vector factors with coefficients $-\mathrm{Gr}_{ij}$, extracts potentials by exterior multiplication, and compares them with determinants of the original Laplacian. The Cauchy–Binet formula, cut weights, and the minimum with free interior vertices are checked separately. The checks cover nine graphs, including a weighted path, triangle, cycle, star, complete graph, and a weighted graph on five vertices. These computational checks supplement the proofs above.

Boundary potentials may be used in reductions of Greenian toponomes. Choosing indexing forests and subsequently evaluating their forms remain different operations. Extending these energy and positivity formulas to balanced directed graphs requires separate consideration; no such extension is asserted here.

## Sources and connections

1. Batson J., Spielman D. A., Srivastava N., Teng S.-H. [Spectral Sparsification of Graphs: Theory and Algorithms](https://www.cs.yale.edu/homes/spielman/PAPERS/CACMsparse.pdf). *Communications of the ACM*, 56(8), 2013, pp. 87–94, §2.2. DOI: [10.1145/2492007.2492029](https://doi.org/10.1145/2492007.2492029). The Laplacian quadratic form, its electrical interpretation, and evaluation of a cut indicator.
2. Doyle P. G., Snell J. L. [Random Walks and Electric Networks](https://math.dartmouth.edu/~doyle/docs/walks/walks.pdf). Mathematical Association of America, 1984; free author version dated 5 July 2006, §1.3.5, Exercise 1.3.11. The minimum-dissipation principle and its formulation for prescribed boundary voltages.

The algebraic definition of potential and the determinant lemma appear in [[Laplacian Exponential]]. The coefficients $\gamma_{ij}$ and their geometric meaning are discussed in [[The Canonical Vector Representation of the Greenian]], the forest expression for cuts in [[Cuts and Forest Grades of the Greenian Exponential]], and specific exponentials in [[Greenian Exponentials of Standard Graphs]].

Series contents and reading routes: [[en/Greenian and polyform duality/Greenian and Polyform Duality|Greenian and Polyform Duality]].
