---
title: Spectral Transfer to a New Boundary
date: '2026-11-02'
updated: 2026-11-08
revision: 2
translated_revision: 6
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-boundary-transfer
order: 2
description: Five polynomial boundary coordinates and a closed transfer rule when a core is attached at two vertices and the active boundary changes.
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Спектральный перенос при смене границы|Спектральный перенос при смене границы]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

In [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]], moving the second seam changed the characteristic polynomial while preserving the matroid parameters. To compute longer chains, we must transfer the data to a new output seam after each core is attached.

The five-polynomial passport and its gluing rule on a **fixed** pair are defined and proved in [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]]. Here we prove closure of these coordinates when the pair **changes**. The essential conditions are that the new core meets the old fragment only at the input pair and that the new boundary lies in the attached core.

We begin with the data to retain and the data required from a core. We then derive the general rule and apply it to the three output-edge positions of a hexagon. This also gives a sequential calculation of the previously studied isomer pair.

> [!note] Origins of the result
> We use classical determinant properties, the Schur complement, and Jacobi's identity for minors. The closure proof and specific transfer formulas are given below in PMG notation. Their presence does not establish scientific priority. Connections with classical transfer methods and precise external references appear in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#Connection with classical methods|Connection with classical methods]].

## Old fragment, new core, and new boundary

We consider finite undirected graphs with positive conductances. Connectivity is not required for the determinant identities. Write $N$ for the number of cores and $n$ for the total number of vertices. We use the ordinary Laplacian matrix $\mathbf L_G$ and the spectral pencil

$$
\mathbf M_G(\xi)=\xi\mathbf I_n-\mathbf L_G
$$

The matrix, its operator on the vertex coordinate space, and the Laplacian form are distinguished as in [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]].

> [!info] One assembly step
> **Definition.** Let the old fragment $G$ have ordered active boundary $\mathcal B=(a,b)$. The core $K$ has marked input $(a,b)$ and output $\mathcal C=(c,d)$, where $c\ne d$.
>
> Only the input vertices are identified: $V(G)\cap V(K)=\{a,b\}$. The pair $\mathcal C$ belongs to $V(K)$ and may overlap the input pair. There are no other identifications. Subsequent attachment is allowed only through the new active pair.
>
> Denote the result by $H=G\cup_{\mathcal B}K$. If there is a shared edge $ab$ of conductance $\omega$, it is counted once in $H$. Its boundary Laplacian is
>
> $$
> \mathbf L_{\cap}=\omega
> \begin{pmatrix}1&-1\\-1&1\end{pmatrix}
> $$
>
> If no edge copies are shared, set $\mathbf L_{\cap}=0$: separate edges $ab$ from the two components are then retained as parallel edges.

The requirement of exactly two shared vertices excludes connections between the new core and already eliminated vertices of the old fragment. For an edge-glued chain, this is precisely what allows us to forget the internal structure of the accumulated graph.

![Old fragment, core attachment, and change of the active pair](images/Changing%20the%20Active%20Spectral%20Boundary.svg)

**What passes from step to step.** The interior of the old fragment is eliminated, but its determinant factor is retained. The core connects the input pair to the output pair. Once the five new coordinates have been computed, the passport on $(c,d)$ is stored; the old pair is no longer active.

## Five coordinates and their meaning

Recall the definitions from [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data#Five polynomials of a marked pair|Five polynomials of a marked pair]]. For $J=V(G)\setminus\{a,b\}$, set

$$
\begin{aligned}
s_G^{a,b}&=(A,B,C,D,E)^{\mathsf T},\\
A&=\det\mathbf M_G,\\
B&=\det(\mathbf M_G)_{\widehat a},\qquad
C=\det(\mathbf M_G)_{\widehat b},\\
D&=(\operatorname{adj}\mathbf M_G)_{ab},\\
E&=\det(\mathbf M_G)_{JJ}
\end{aligned}
\tag{1}
$$

Principal minors delete rows and columns **without recalculating the degrees of the remaining vertices**. The coordinate $D$ is an adjugate entry with its cofactor sign, not an unsigned minor. The empty determinant is $1$.

When $E\ne0$, the old interior is represented by the Schur complement

$$
\mathbf S_G=\frac1E
\begin{pmatrix}C&-D\\-D&B\end{pmatrix},
\qquad AE=BC-D^2
\tag{2}
$$

Hence $E\det\mathbf S_G=A$. The factor $E$ itself must also be retained: the rational matrix $\mathbf S_G$ alone does not contain the entire determinant of the old fragment.

These five polynomials are not five independent variables, nor do they represent five disjoint classes of ordinary forests. Their sufficiency for transfer does not imply that the coordinate count is minimal. If four polynomials $B,C,D,E$ are stored, $A$ can be recovered by exact division in (2), but this representation gives no substitution formula at zeros of $E$.

## What data are required from a core

Fix an order of the core vertices beginning with $a,b$. Let $\mathbf U$ embed the two input coordinates into $\mathbb R^{V(K)}$: its columns are the coordinate vectors of vertices $a,b$. Define

$$
\mathbf W_K(\xi)=\mathbf M_K(\xi)
-\xi\mathbf U\mathbf U^{\mathsf T}
+\mathbf U\mathbf L_{\cap}\mathbf U^{\mathsf T}
\tag{3}
$$

After eliminating $J$, the remaining matrix on the core vertices is

$$
\mathbf H_K=\mathbf W_K+\mathbf U\mathbf S_G\mathbf U^{\mathsf T}
\tag{4}
$$

The correction $-\xi\mathbf U\mathbf U^{\mathsf T}$ removes the double counting of the two shared vertices. The correction $+\mathbf U\mathbf L_{\cap}\mathbf U^{\mathsf T}$ removes the double counting of the shared edge in the Laplacian. The signs follow from $\mathbf M=\xi\mathbf I-\mathbf L$.

Thus one transition can be constructed from the core matrix, the locations and orders of both pairs, and the shared-edge rule. After preprocessing, the core can be replaced by its transfer matrix. **Two core passports computed separately at the input and output do not, in general, replace these data.** A single hexagon below demonstrates this.

## Why transfer closes on five coordinates

Replace the old Schur complement by an independent symmetric block

$$
\mathbf X=\begin{pmatrix}u&v\\v&w\end{pmatrix},
\qquad
\mathbf H_K(\mathbf X)=\mathbf W_K+\mathbf U\mathbf X\mathbf U^{\mathsf T}
\tag{5}
$$

For any symmetric matrix on $V(K)$, let $\Phi_1,\ldots,\Phi_5$ denote the same five operations as in (1), now relative to the output pair $(c,d)$: the determinant, two principal minors, an adjugate entry, and the principal minor deleting both vertices. Set $F_i(u,v,w)=\Phi_i(\mathbf H_K(\mathbf X))$.

> [!info] Five expressions suffice for each new minor
> **Lemma.** For each $i=1,\ldots,5$, there are polynomials $\alpha_i,\beta_i,\gamma_i,\delta_i,\varepsilon_i$ in $\xi$, depending only on the marked core and the seam rule, such that
>
> $$
> \begin{aligned}
> F_i={}&\alpha_i(uw-v^2)+\beta_i u+\gamma_i w+{}\\
> &+\delta_i v+\varepsilon_i
> \end{aligned}
> \tag{6}
> $$

> [!note]- Proof of the five-expression lemma
> **Proof.** The variables $u,v,w$ occur only in the two input rows and two input columns. Each determinant term selects one entry from each row and column, so its degree in these variables is at most two.
>
> If both input rows and both input columns are retained, the only quadratic contributions are $\alpha_i uw$ and $-\alpha_i v^2$: they differ by a transposition of the two input columns. If any of these rows or columns is deleted, there are no quadratic contributions. The remaining terms are linear or constant. Multiplication by the cofactor sign for $\Phi_4$ preserves this form. This also covers overlap between the input and output pairs. $\square$

> [!info] Polynomial transfer to a new pair
> **Theorem.** Under the conditions of one assembly step, the entire passport on the new boundary is linear in the old passport:
>
> $$
> \boxed{s_H^{c,d}=\mathbf T_{K;\mathcal B\to\mathcal C}(\xi)s_G^{a,b}}
> \tag{7}
> $$
>
> Row $i$ of the transfer matrix is
>
> $$
> (\alpha_i,\gamma_i,\beta_i,-\delta_i,\varepsilon_i)
> \tag{8}
> $$
>
> The formula holds for every $\xi$, including zeros of the old internal minor $E$. It requires neither planarity, a cyclic core, nor disjoint input and output pairs.

> [!note]- Proof of the transfer theorem
> **Proof.** Place the old internal vertices $J$ before the vertices of $K$. For $E\ne0$, block elimination gives (4). The block $J$ is unchanged in each of the five new determinants or cofactors. The new coordinate is therefore $E F_i(\mathbf S_G)$. In a cofactor with output indices, shifting both indices by $|J|$ leaves the sign unchanged.
>
> Substitute $u=C/E$, $w=B/E$, and $v=-D/E$ into (6) and use (2):
>
> $$
> \begin{aligned}
> E F_i(\mathbf S_G)
> &={}\alpha_i\frac{BC-D^2}{E}+\beta_i C+\gamma_i B-{}\\
> &\qquad-\delta_i D+\varepsilon_i E\\
> &={}\alpha_i A+\gamma_i B+\beta_i C-{}\\
> &\qquad-\delta_i D+\varepsilon_i E
> \end{aligned}
> $$
>
> This is (7)-(8). All new coordinates and the right-hand side are polynomial in $\xi$. The polynomial $E$ has leading coefficient $1$ and is not identically zero. Equality away from its finite set of zeros therefore extends to every $\xi$. $\square$

Closure has now been established by a separate proof. It means that, for a specified core and new pair, no additional coordinates depending on the size of the accumulated fragment are needed. The theorem does not assert that five coordinates suffice for a larger boundary or for new connections to forgotten vertices.

### Obtaining the matrix without guessing formulas

Each operation $F_i$ requires just five substitutions:

$$
\begin{aligned}
q_0&=F_i(0,0,0),&q_a&=F_i(1,0,0),\\
q_b&=F_i(0,0,1),&q_{ab}&=F_i(1,0,1),\\
q_v&=F_i(0,1,0)
\end{aligned}
$$

Equation (6) gives the exact formulas

$$
\begin{aligned}
\varepsilon_i&=q_0,\\
\beta_i&=q_a-q_0,\qquad \gamma_i=q_b-q_0,\\
\alpha_i&=q_{ab}-q_a-q_b+q_0,\\
\delta_i&=q_v-q_0+\alpha_i
\end{aligned}
\tag{9}
$$

These substitutions use formal entries of the block $\mathbf X$, not conductances of a new physical graph. Formulas (3), (5), (8), and (9) completely determine the transfer matrix for any specified core satisfying the theorem's conditions.

## Three outputs of a unit hexagon

Take $K=C(0,1,2,3,4,5)$. Identify the input $(0,1)$ with the old pair $(a,b)$ **in the same order**: $0\mapsto a$, $1\mapsto b$. Count the shared edge $01$ of conductance $1$ once. Choose output $(j,j+1)$, where $j=2,3,4$, and denote the corresponding transfer by $\mathbf T_j$.

![Three output edges with a fixed order of the input pair](images/Three%20Output%20Seams%20of%20a%20Hexagon.svg)

**The pair order is part of the data.** Arrows specify the order of the seam endpoints; the graph remains undirected. Each of the three output edges is disjoint from the input. Every individual cycle edge has the same spectral passport, but its position relative to the input differs.

For $y=\xi-2$, matrix (5) takes a particularly simple form:

$$
\mathbf H_K(\mathbf X)=
\begin{pmatrix}
u-1&v&0&0&0&1\\
v&w-1&1&0&0&0\\
0&1&y&1&0&0\\
0&0&1&y&1&0\\
0&0&0&1&y&1\\
1&0&0&0&1&y
\end{pmatrix}
\tag{10}
$$

The old shared edge is already included in $\mathbf S_G$. Its entry is therefore $v$, not $v+1$. The input diagonals decrease by $1$: each endpoint gains one new edge of the path $1-2-3-4-5-0$.

We give all transitions as compact recurrences. Set

$$
m=y^2-1,\qquad \ell=y^3-2y,\qquad k=y^4-3y^2+1
\tag{11}
$$

These are determinants of tridiagonal blocks of lengths $2,3,4$, with diagonal $y$ and neighboring entries $1$. For the old passport, define

$$
\Phi=ymA-(y+1)m(B+C)+(y+1)(m+y)E
$$

The first coordinate is the same for every output:

$$
\boxed{A'=kA-(k+\ell)(B+C)+2D+(k+2\ell+m)E}
\tag{12}
$$

It depends on the core attachment, not on the choice of the new marking. All three cases also satisfy $D'=D-E'$.

> [!info] Output $(2,3)$
> **Proposition.** The remaining coordinates of transfer $\mathbf T_2$ are
>
> $$
> \begin{aligned}
> B'&=\ell A-(\ell+m)B-\ell C+(\ell+m)E,\\
> C'&=\Phi-B,\\
> E'&=mA-(m+y)B-mC+(m+y)E,\\
> D'&=D-E'
> \end{aligned}
> \tag{13}
> $$

> [!info] Output $(3,4)$
> **Proposition.** The remaining coordinates of transfer $\mathbf T_3$ are
>
> $$
> \begin{aligned}
> B'&=\Phi-B,\qquad C'=\Phi-C,\\
> E'&=y^2A-y(y+1)(B+C)+(y+1)^2E,\\
> D'&=D-E'
> \end{aligned}
> \tag{14}
> $$

> [!note]- Derivation of the hexagon recurrences
> **Proof.** For outputs $(2,3)$ and $(3,4)$, apply the five operations $\Phi_i$ to matrix (10), expand the determinants in $u,v,w$, and use (8). In both cases the first row is $(k,-k-\ell,-k-\ell,2,k+2\ell+m)$. The other rows give (13), (14). All coefficients can be obtained by the five substitutions in (9), without rational elimination. The verification program independently compares each determinant expansion with the stated recurrences. $\square$

Let $\mathbf J$ interchange the second and third passport coordinates:

$$
\mathbf J(A,B,C,D,E)^{\mathsf T}=(A,C,B,D,E)^{\mathsf T}
$$

The cycle reflection interchanging $0,1$ takes output $(2,3)$ to $(5,4)$, and $(3,4)$ to $(4,3)$. Hence

$$
\mathbf T_4=\mathbf J\mathbf T_2\mathbf J,
\qquad \mathbf J\mathbf T_3\mathbf J=\mathbf T_3
\tag{15}
$$

Thus (12)-(15) specify all three polynomial matrices. Their expanded coefficients are retained in the [exact data](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/boundary-transfer-results.json).

Under the alternative convention identifying local input $(0,1)$ with old pair $(b,a)$, the transition becomes $\mathbf T_j\mathbf J$. Reversing only the output pair gives $\mathbf J\mathbf T_j$. These are different operations; conjugation $\mathbf J\mathbf T_j\mathbf J$ changes both orders. Transfer formulas cannot be compared without specifying these conventions.

## One graph, two passports, different continuations

The initial state of a single $C_6$ on edge $(0,1)$ is

$$
\begin{aligned}
A_1&=\xi(\xi-4)(\xi-3)^2(\xi-1)^2,\\
B_1=C_1&=(\xi-3)(\xi-2)(\xi-1)(\xi^2-4\xi+1),\\
D_1&=-(\xi-3)(\xi-1)(\xi^2-4\xi+2),\\
E_1&=(\xi^2-5\xi+5)(\xi^2-3\xi+1)
\end{aligned}
\tag{16}
$$

For a chain of $N\ge2$ cores assembled by these rules, sequential computation takes the form

$$
\begin{aligned}
s_N&=\mathbf T_{j_N}\cdots\mathbf T_{j_2}s_1,\\
\chi_G&=\mathbf e_1^{\mathsf T}s_N
=\mathbf r\mathbf T_{j_{N-1}}\cdots\mathbf T_{j_2}s_1
\end{aligned}
$$

Here $j_i$ specifies the output of core $i$, $\mathbf e_1=(1,0,0,0,0)^{\mathsf T}$, and $\mathbf r$ is the common first row (12). For $N=2$, the product between $\mathbf r$ and $s_1$ is empty. The output choice of the final core does not affect the polynomial of the graph already assembled. State subscripts count cores, not vertices.

The passports $\mathbf T_3s_1$ and $\mathbf T_2s_1$ belong to the same two-hexagon graph but to different output edges. Their first coordinates agree; the full vectors differ.

![The same polynomial for two cores and different results after attaching a third](images/Spectral%20Memory%20of%20Two%20Hexagons.svg)

**The difference is retained at the boundary until the next attachment.** The figure uses the numerical check $P_G(1)$, where $P_G(t)=\det(\mathbf I+t\mathbf L_G)$ is the rooted polynomial, not the ordinary forest polynomial. Equal values for two cores become different values for three after the same attachment rule is applied at the marked output.

> [!info] From a boundary difference to a spectral difference
> **Proposition.** Let $\mathbf r$ be the common first row of $\mathbf T_j$ in (12), and let
>
> $$
> \begin{aligned}
> q(\xi)&=\chi_{C_5}(\xi)=\xi(\xi^2-5\xi+5)^2,\\
> \mathbf v&=(0,\xi-2,0,-1,1)^{\mathsf T}
> \end{aligned}
> $$
>
> Then
>
> $$
> (\mathbf T_3-\mathbf T_2)s_1=-q\mathbf v,
> \qquad \mathbf r\mathbf v=-q
> \tag{17}
> $$
>
> Consequently, for the pair from [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]],
>
> $$
> \chi_{\mathrm A}-\chi_{\text{B}}
> =\mathbf r(\mathbf T_3-\mathbf T_2)s_1=q^2
> \tag{18}
> $$

> [!note]- Derivation of the boundary difference
> **Proof.** Substitute $B_1=C_1$ into the difference between (14) and (13). For $h=A_1-\xi B_1+\xi E_1$, we obtain $(0,yh,0,-h,h)^{\mathsf T}$. Expressions (16) give $h=-\xi(\xi^2-5\xi+5)^2=-q$. Substitution of $\mathbf v$ into row (12) gives $-y(k+\ell)-2+k+2\ell+m=-q$. This proves (17); multiplication by $\mathbf r$ gives (18). $\square$

This example also shows why two separate passports of the core itself are insufficient: the cycle $C_6$ has the same passport on every ordered edge, but $\mathbf T_2\ne\mathbf T_3$. The missing information is precisely the relative position of input and output. The transfer theorem uses the whole marked core when constructing the matrix; thereafter, the accumulated old graph is represented by only five coordinates.

### Check at $\xi=-1$

For a hexagonal chain, $n=4N+2$ is even. Set

$$
\mathbf R=\operatorname{diag}(1,-1,-1,-1,1),
\qquad z=\mathbf R s(-1)
$$

The first coordinate $z$ then equals $P_G(1)$, since $P_G(1)=(-1)^n\chi_G(-1)$. The initial state and two transfer results are

$$
\begin{aligned}
z_1&=\mathbf R s_1(-1)=(320,144,144,56,55)^{\mathsf T},\\
z_2^{(2)}&=(28435,12331,12694,4763,4707)^{\mathsf T},\\
z_2^{(3)}&=(28435,12694,12694,4884,4828)^{\mathsf T}
\end{aligned}
\tag{19}
$$

Here the superscript denotes the output position and the subscript the number of cores. The numerical transitions are $\mathbf R\mathbf T_j(-1)\mathbf R$. The common final row is

$$
(55,34,34,-2,21)
$$

> [!example] One numerical step
> Applied to the initial vector $z_1$ in (19), the common first row gives
>
> $$
> \begin{aligned}
> P_{G_2}(1)&=55\cdot320+34\cdot144+34\cdot144\\
> &\quad-2\cdot56+21\cdot55=28435
> \end{aligned}
> $$
>
> This is the first coordinate of both two-core states. The output choice already affects the boundary coordinates; the first coordinate differs after the next attachment.

Applying the same row to the two states in (19) gives $2504096$ and $2518737$, respectively, with difference $14641$. The negative entry $-2$ again shows why these coordinates cannot be interpreted as five disjoint forest classes whose counts are simply added.

Evaluation at $\xi=-1$ serves here as an exact check. It neither replaces polynomial transfer nor proves recovery of an arbitrary chain from one number.

## Transfer at a zero of the internal minor

Take the old path $G=a-u-b$ with active pair $(a,b)$. Attach the path $K=a-c-d-b$ with no shared edges, and transfer the boundary to $(c,d)$. The result is the cycle $C_5$.

![Transfer between two pairs when the internal minor is zero](images/Transfer%20with%20a%20Zero%20Interior%20Minor.svg)

**Rational elimination has a pole; polynomial transfer remains defined.** For the old path, $E=\xi-2$. At $\xi=2$, the formula expressing $\mathbf S_G$ through $1/E$ cannot be used. Yet all five new coordinates are obtained from (7).

> [!example] Exact substitution at a singular point
> **Computed directly.** For the specified graphs,
>
> $$
> \begin{aligned}
> s_G^{a,b}(2)&=(-2,-1,-1,1,0)^{\mathsf T},\\
> s_{C_5}^{c,d}(2)&=(2,1,1,1,0)^{\mathsf T}
> \end{aligned}
> \tag{20}
> $$
>
> The transfer formula and direct minors of the full Laplacian give the same result. Zeros of $E$ require neither discarding eigenvalues nor replacing a matrix by its pseudoinverse.

## Connection with classical methods

The Schur complement eliminates internal variables from a block linear system. Its electrical application to Laplacians is described, for example, by Dörfler and Bullo [1, §II.A, equations (1)-(2)] and presented in [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]. Here we eliminate a block of the spectral pencil: its dependence on $\xi$ is retained together with the determinant factor.

Transfer calculations of determinants are also classical. Molinari [2] expresses a block-tridiagonal determinant through the corresponding transfer matrix or a block of it. Here the specific coordinates differ: they are minors on the active pair. Polynomial closure follows from determinant multilinearity and Jacobi's identity, not from a special property of the ordinary forest passport.

In PMG language, the result extends spectral boundary data and the connection between the characteristic polynomial and rooted grades. The transfer matrix itself acts on a vector of polynomials. Its product must not be identified with a product of Laplacian forms or with addition of Greenians.

## Checks, established result, and continuation

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_boundary_transfer.py) builds matrices from edges, extracts the coefficients in (6), and independently compares transferred passports with direct determinants and cofactors of the result. It checks:

- overlapping and disjoint inputs and outputs, including retention and reversal of the old pair;
- one shared edge copy and separate parallel edges, with integer and rational conductances;
- disconnected graphs, isolated vertices, and cofactor signs after vertex permutations;
- the point $E=0$, all five polynomial coordinates of short hexagonal chains, and exact numerical states of longer chains;
- recurrences (12)-(15), formulas (17)-(20), and both full polynomials of the published three-hexagon pair.

The scope of the finite checks and reproduction commands are given in the [calculation documentation](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md). They confirm the implementation and examples; the general closure proof is contained in (5)-(8).

**Established:** for the specified two-vertex attachment, five spectral coordinates close under a change of active pair, and the transition matrix is determined by the marked core and seam rule. All three explicit hexagon transitions have been obtained with a fixed endpoint order.

Configuration coding, reflection and reversal, and classification of abstract open hexagonal chains are presented in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]. Further questions concern spectral differences of transition sequences and reconstruction. Injectivity of the full boundary state, of the characteristic polynomial, and of one numerical value are distinct. Transfer closure alone proves none of them; minimality of the five coordinates is not established here either.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

## Sources and connections

1. F. Dörfler, F. Bullo. *Kron Reduction of Graphs with Applications to Electrical Networks*. [arXiv:1102.2950, §II.A, equations (1)-(2)](https://arxiv.org/html/1102.2950#S2.SS1). The electrical Schur complement; the five-coordinate spectral transfer is derived in this note.
2. L. G. Molinari. *Determinants of Block Tridiagonal Matrices*. Linear Algebra and its Applications **429** (2008), 2221-2226. [arXiv:0712.0681](https://arxiv.org/abs/0712.0681), [DOI: 10.1016/j.laa.2008.06.015](https://doi.org/10.1016/j.laa.2008.06.015). Classical transfer computation of determinants; not the source of this note's specific passport or output-seam numbering.

Supporting notes: [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]], [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]], [[en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]].
