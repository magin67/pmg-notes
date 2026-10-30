---
title: "From the Forest Passport to Spectral Boundary Data"
date: 2026-10-30
updated: 2026-10-30
revision: 1
translated_revision: 4
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: boundary-polynomials-spectral-data
order: 6
description: "A separate two-point spectral passport of five related minors and cofactors. Jacobi’s identity, gluing with shared vertices and edges, and input and output boundaries for chains."
---

[[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data|Gluing Components by Pairing Boundary Data]] reconstructs the full forest polynomial of a gluing from boundary partitions. [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]] establishes how many linear coordinates suffice. We now change the quantity to be computed: the goal is the Laplacian characteristic polynomial. In general, the retained forest states do not suffice for it.

For a two-point boundary, a new passport can be formed from five polynomials: the determinant of the spectral pencil, three principal minors, and one cofactor. They satisfy Jacobi's identity. We derive their gluing law, then specify the setting for chains with input and output boundaries.

**Provenance of the results.** Jacobi's identity and elimination of internal variables by a Schur complement are classical matrix constructions. Here they are applied to the spectral pencil used in PMG and to specified gluing rules. The particular formulas and examples are derived in the text; this does not assert scientific priority. Transfer matrices for particular chain families remain a subject for the next stage.

## Two forest states do not determine the spectral polynomial

As in [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], use the spectral variable $\xi$:

$$
\begin{aligned}
\chi_G(\xi)&=\det(\xi I-\mathbf L_G)
=\xi^nP_G(-1/\xi)\\
P_G(t)&=\det(I+t\mathbf L_G)
=\sum_g p_g t^g
\end{aligned}
\tag{1}
$$

The last expression for $\chi_G$ is a polynomial identity, including at $\xi=0$. The coefficient $p_g$ counts rooted forests: each ordinary forest weight is additionally multiplied by the product of its component sizes. This is the matrix-forest formula, presented with sources in [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]]. The ordinary coefficient $f_g$ has no such factor.

**An example computed here.** Take two trees with vertex names $a,b,c,d$: the path with edges $ab,bc,cd$ and the star with edges $ab,bc,bd$. All conductances are $1$; both have the ordered boundary $(a,b)$. We are comparing separate components with identical boundary labels.

![[The same forest passport and different spectra.svg]]

In each tree, the unique path between $a$ and $b$ is the edge $ab$. Selecting it gives state $ab$; omitting it gives $a|b$. The other two edges are chosen independently, so the **full ordinary forest passports coincide**:

$$
\mathcal F_{a|b}(t)=(1+t)^2,\qquad
\mathcal F_{ab}(t)=t(1+t)^2
\tag{2}
$$

Direct determinant calculation nevertheless gives

$$
\begin{aligned}
\chi_{P_4}(\xi)&=\xi(\xi-2)(\xi^2-4\xi+2)\\
\chi_{K_{1,3}}(\xi)&=\xi(\xi-1)^2(\xi-4)
\end{aligned}
\tag{3}
$$

The difference is also visible in two-edge forests. For the path, component sizes give factors $3,4,3$, while the star gives $3,3,3$. Thus the ordinary coefficient is $f_2=3$ in both cases, but the rooted coefficient $p_2$ is $10$ and $9$, respectively.

Even a full two-point ordinary passport therefore does not determine $\chi_G$. Reducing its coordinate count cannot recover information already lost in (2).

## Five polynomials of a marked pair

Let $G$ be a finite undirected graph with positive conductances, and let $\mathcal B=(a,b)$ be an ordered pair of distinct vertices. Call the vertices outside $\mathcal B$ internal and denote their set by $J$. Connectivity is not required for the algebraic formulas. Parallel edges contribute with their conductances; a loop has zero incidence vector and contributes nothing to the Laplacian used here.

Set $\mathbf M_G(\xi)=\xi I-\mathbf L_G$. A hat denotes deletion of a row and column. **Define the spectral boundary passport** by

$$
\begin{aligned}
A&=\det\mathbf M_G=\chi_G(\xi)\\
B&=\det(\mathbf M_G)_{\widehat a},\qquad
C=\det(\mathbf M_G)_{\widehat b}\\
D&=(\operatorname{adj}\mathbf M_G)_{ab}\\
E&=\det(\mathbf M_G)_{\widehat{\{a,b\}}}
=\det(\mathbf M_G)_{JJ}
\end{aligned}
\tag{4}
$$

The empty determinant is $1$. The letters $B,C$ denote polynomials, while the boundary is written $\mathcal B$. The degrees of $A,B,C,E$ are $n,n-1,n-1,n-2$, respectively; the degree of $D$ is at most $n-2$.

Here $\operatorname{adj}$ is the adjugate, the transpose of the cofactor matrix. If $a,b$ have indices $i,j$ in the vertex order, then $D$ is obtained by deleting row $j$ and column $i$ and multiplying the determinant by $(-1)^{i+j}$. Symmetry of $\mathbf M_G$ makes the two reciprocal cofactors equal. Interchanging boundary names $a\leftrightarrow b$ swaps $B,C$ and preserves $A,D,E$.

**Deleting a row and column does not mean deleting a graph vertex and recalculating degrees.** For example, for the path $a-u-b$,

$$
B=(\xi-2)(\xi-1)-1=\xi^2-3\xi+1
$$

The remaining diagonal entry at $u$ retains its original degree $2$. The graph $G-a$, consisting of a single edge, has a different characteristic polynomial: $\xi(\xi-2)$.

Passport (4) is a choice of determinant coordinates. Its components are not sums of ordinary forests over five partitions: a pair of vertices has only two partitions.

## The Schur complement and Jacobi's identity

Order $a,b$ first, followed by the internal vertices. For $E(\xi)\ne0$, eliminating internal coordinates gives a symmetric matrix of size $2$:

$$
\mathbf S_G(\xi)
=\mathbf M_{\mathcal B\mathcal B}
-\mathbf M_{\mathcal B J}\mathbf M_{JJ}^{-1}
\mathbf M_{J\mathcal B}
\tag{5}
$$

This is the ordinary Schur complement. Its application to the static Laplacian and the Dirichlet-to-Neumann operator is discussed in [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]; the external foundation for the electrical interpretation is Dörfler–Bullo [2, §II.A, equations (1)–(2)]. Formula (5) applies the same operation to the pencil depending on $\xi$.

Determinant-preserving block elimination gives $A=E\det\mathbf S_G$. Applying it to the principal minors and evaluating the off-diagonal cofactor yields

$$
\boxed{
\mathbf S_G=\frac1E
\begin{pmatrix}C&-D\\-D&B\end{pmatrix},\qquad
A=E\det\mathbf S_G
}
\tag{6}
$$

**The classical Jacobi identity.** The coordinates (4) satisfy

$$
\boxed{AE=BC-D^2}
\tag{7}
$$

This is the symmetric case of the Desnanot–Jacobi identity for minors underlying Dodgson condensation; see Fulmek [1, Proposition 2, equation (8), §5.1] for a modern proof. In our notation, (7) follows directly from the determinant of (6). The proof first holds for $E\ne0$, then for every $\xi$: both sides of (7) are polynomials, and $E$ is a nonzero monic polynomial. $\square$

The five polynomials are therefore **not algebraically independent**. Given the full polynomials $B,C,D,E$ of a realizable passport, $A$ is recovered by exact division of $BC-D^2$ by $E$. Retaining $A$ keeps the gluing law polynomial, without division, and allows it to be used at zeros of $E$. No minimality of five coordinates among all possible spectral passports is proved here.

There is also a resolvent connection. For $A(\xi)\ne0$,

$$
\begin{aligned}
\bigl((\xi I-\mathbf L_G)^{-1}\bigr)_{\mathcal B\mathcal B}
&=\frac1A\begin{pmatrix}B&D\\D&C\end{pmatrix}\\
&=\sum_\lambda\frac{(\mathbf E_\lambda)_{\mathcal B\mathcal B}}{\xi-\lambda}
\end{aligned}
\tag{8}
$$

Here $\mathbf E_\lambda$ is the orthogonal projector onto an eigenspace in $\mathbb R^V$. The notation agrees with [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]], but the sum in (8) runs over **all distinct eigenvalues, including $0$**: this is the resolvent on the full vertex space. For a connected graph, $\mathbf E_0=\mathbf1\mathbf1^{\mathsf T}/n$; for a disconnected graph, it projects onto the entire $\ker\mathbf L_G$. The nonbold letter $E$ still denotes the internal minor in (4).

Boundary data thus depend on the position of the marked pair relative to the eigenspaces. The spectrum alone specifies the denominators in (8), but not all numerators.

Even for the same path $a-u-b$, changing the boundary changes the passport: $(a,b)$ gives $E=\xi-2$, whereas $(a,u)$ gives $E=\xi-1$, with the same $A=\xi(\xi-1)(\xi-3)$.

## Gluing along two shared vertices

First fix a construction with no shared edges. Components $G_1,G_2$ have the common boundary $\mathcal B=(a,b)$ and disjoint internal sets $J_1,J_2$. Only boundary vertices with the same name are identified. Each edge instance belongs to exactly one component; two distinct edges $ab$, if present, remain parallel edges.

Let $G=G_1\cup_{\mathcal B}G_2$. After embedding matrices in the common vertex space,

$$
\mathbf L_G=\mathbf L_1+\mathbf L_2,\qquad
\mathbf M_G=\mathbf M_1+\mathbf M_2-\xi\mathbf I_{\mathcal B}
\tag{9}
$$

Here $\mathbf I_{\mathcal B}$ is diagonal with ones only at $a,b$. It is needed because the sum of the two pencils gives these vertices two copies of $\xi$. The matrices indexed by $1,2$ in (9) are extended by zero outside their components.

The internal block of the result is block diagonal. Thus

$$
E_G=E_1E_2,\qquad
\mathbf S_G=\mathbf S_1+\mathbf S_2-\xi I_2
\tag{10}
$$

**Derivation for the specified gluing.** Write

$$
\begin{aligned}
U&=B_1E_2+E_1B_2\\
V&=C_1E_2+E_1C_2\\
W&=D_1E_2+E_1D_2,\qquad Z=E_1E_2\\
Q&=A_1E_2+E_1A_2+B_1C_2+C_1B_2-2D_1D_2
\end{aligned}
\tag{11}
$$

Then the entire passport of the result on the same boundary is

$$
\boxed{
\begin{aligned}
A_G&=Q-\xi(U+V)+\xi^2 Z\\
B_G&=U-\xi Z,\qquad C_G=V-\xi Z\\
D_G&=W,\qquad E_G=Z
\end{aligned}
}
\tag{12}
$$

**Proof.** The equalities for $B_G,C_G,D_G$ follow by substituting (6) into (10). For the first equality, expand the determinant of $\mathbf S_1+\mathbf S_2-\xi I_2$ and multiply by $E_1E_2$. Terms involving only one component reduce by (7) to $A_1E_2$ and $E_1A_2$; mixed terms give $B_1C_2+C_1B_2-2D_1D_2$. The diagonal correction gives the remaining terms. The resulting expressions are polynomial and therefore hold also when $E_1E_2=0$. $\square$

Formula (12) is derived here from the classical Schur complement and (7), rather than borrowed as an ordinary forest-state formula. It is bilinear in the two five-component vectors over the polynomial ring in $\xi$. For a fixed partner, it is a linear transformation of the passport. Sufficiency concerns the marked pair and the stated gluing rules; planarity is not required.

### Two paths give a cycle

Take $G_1=a-u-b$ and $G_2=a-v-b$ with unit conductances. They share boundary $(a,b)$, have distinct $u,v$, and share no edges. In both cases,

$$
\begin{aligned}
A_i&=\xi(\xi-1)(\xi-3)\\
B_i&=C_i=\xi^2-3\xi+1,\qquad D_i=1\\
E_i&=\xi-2
\end{aligned}
$$

![[Spectral gluing of two paths.svg]]

Formula (12) gives

$$
\chi_{C_4}(\xi)=\xi(\xi-2)^2(\xi-4)
\tag{13}
$$

At $\xi=2$, both $E_i$ vanish, so the rational expression (6) cannot be evaluated there. Formula (12) remains valid: $B_i=C_i=-1$ and $D_i=1$, so the only surviving terms in $A_G$ give $2-2=0$. Eliminating internal vertices has not lost the characteristic-polynomial root.

## When the components contain the same edge

Now change the rule: an edge $ab$ of conductance $w$ is included in both original components but must remain **one** edge of the same conductance in the result. The shared subgraph consists of $a,b$ and this edge. Its boundary Laplacian is

$$
\mathbf L_e=w\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
$$

Then $\mathbf L_G=\mathbf L_1+\mathbf L_2-\mathbf L_e$, so

$$
\mathbf S_G=\mathbf S_1+\mathbf S_2-\xi I_2+\mathbf L_e
\tag{14}
$$

Expanding this determinant with the same notation (11) gives

$$
\boxed{
\begin{aligned}
A_G&=Q+(w-\xi)(U+V)-\\
&\quad-2wW+(\xi^2-2w\xi)Z\\
B_G&=U+(w-\xi)Z,\qquad C_G=V+(w-\xi)Z\\
D_G&=W+wZ,\qquad E_G=Z
\end{aligned}
}
\tag{15}
$$

This correction for the specified counting rule is also derived from the Schur complement. At $w=0$, it reduces to (12). Another way to obtain the same graph is to assign the shared edge to one component beforehand, recompute the other component's passport without that edge, and apply (12). Removing an edge instance from the construction while retaining the old component passport is invalid.

![[A shared edge and parallel copies.svg]]

For example, two unit-weight triangles $a-u-b-a$ and $a-v-b-a$ have the same marked pair $(a,b)$. If $ab$ is retained once, the resulting graph has five edges:

$$
\chi_G(\xi)=\xi(\xi-2)(\xi-4)^2
$$

If the two instances of $ab$ are instead distinct parallel edges, the result has six edges counted with multiplicity:

$$
\chi_{G_{\parallel}}(\xi)=\xi(\xi-2)(\xi-4)(\xi-6)
$$

Both answers are correct for their constructions. The drawing and the ownership rule for the shared edge specify which one is required.

## What remains of the electrical response

For a connected graph with nonempty boundary, $(\mathbf L_G)_{JJ}$ is nonsingular; for $J=\varnothing$, use the empty-determinant convention. Substituting $\xi=0$ into (5) gives

$$
\mathbf S_G(0)=-\boldsymbol\Lambda_G,\qquad
E(0)=(-1)^{|J|}\det(\mathbf L_G)_{JJ}
\tag{16}
$$

Here $\boldsymbol\Lambda_G$ is the Dirichlet-to-Neumann operator from [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]]. The sign comes from choosing $\mathbf M_G=\xi I-\mathbf L_G$. At $\xi=0$, (10) becomes the established addition rule for electrical responses of components with disjoint edges. For a shared edge, (14) gives $\boldsymbol\Lambda_G=\boldsymbol\Lambda_1+\boldsymbol\Lambda_2-\mathbf L_e$.

But $\mathbf S_G(0)$ does not determine the rational matrix $\mathbf S_G(\xi)$ for every $\xi$, just as the number $E(0)$ does not determine the polynomial $E$. Static electrical response must therefore be distinguished from the spectral passport. Addition of pencils and their Schur complements is also neither addition of Greenians nor a resistance inner product.

## Input and output boundaries of a chain

Successively attaching cores requires two ordered pairs on each core: an input $\mathcal B_{\mathrm{in}}$ and an output $\mathcal B_{\mathrm{out}}$. The output of the assembled fragment is identified with the input of the new core by a specified correspondence. The new core's output then becomes the active boundary.

![[Spectral input and output boundaries.svg]]

Before calculation, specify the vertex order in both pairs, any overlap between them inside the core, and the shared-edge counting rule. In the illustrated scheme, the two pairs inside the core are disjoint, the shared edge belongs to one fragment, and each shared vertex is counted once after gluing.

Formulas (12) and (15) retain the previous active pair $(a,b)$. Moving the boundary to other vertices is a separate operation: it requires the locations of the input and output in the attached core and a corresponding transformation of minors. It cannot be obtained merely by renaming the old $B,C$.

For a specified family of cores, this setting prepares a transfer method. This note establishes passport sufficiency for gluing at a fixed two-point boundary. Concrete transitions between different inputs and outputs, closure on five coordinates, a transfer automaton, and classification of isomers require separate treatment.

## Status of the results and checks

| Result | Foundation and role in the exposition |
|---|---|
| Relation of $\chi_G$ to rooted coefficients | The established matrix-forest formula, applied in PMG notation |
| $AE=BC-D^2$ | The classical Jacobi identity [1], with a short proof in our coordinates |
| Schur complement and electrical value at $\xi=0$ | Standard variable elimination; electrical interpretation in [2] |
| Formulas (12), (15) | Direct derivations from these matrix identities for explicitly specified gluing; no independent priority claim |
| Examples and reconstruction limits | Calculations checked here, distinguishing ordinary, electrical, and spectral passports |

The formulas are proved above. The [verification script](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/verify_spectral_boundary.py) separately computes pencil determinants and cofactors in exact rational polynomial arithmetic. For 80 components, it checks Jacobi's identity and agreement of $\chi_G$ with independent enumeration of rooted forests. For 528 gluings with disjoint edges and 48 with a shared weighted edge, all five coordinates are compared with direct minors of the result.

Further checks cover the coinciding forest passports of the path and star, dependence on boundary choice, the distinction between a principal minor and the polynomial of a vertex-deleted graph, zeros of $E_i$, parallel edges, loops, isolated internal vertices, 24 vertex orders, associativity of successive gluing on one boundary, and the resolvent expansion including the zero projector for connected and disconnected graphs. Finite checks illustrate the proved formulas but do not replace proofs. [Instructions for running the checks and reproducing the figures](https://github.com/magin67/pmg-notes/blob/v5/checks/boundary/README_EN.md) accompany the script.

We have completed the passage from “which forests connect the boundary?” to “which spectral pencil is visible at the boundary?” Both problems use boundary data and gluing laws, but retain different information about a component.

## Sources and connections

1. M. Fulmek. *Viewing determinants as nonintersecting lattice paths yields classical determinantal identities bijectively*. The Electronic Journal of Combinatorics, 19(3) (2012), P21. [Equation (8), Remark 1, and §5.1](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p21/pdf/). The Desnanot–Jacobi identity and its combinatorial proof; not the source of our passport's particular notation.
2. F. Dörfler, F. Bullo. *Kron Reduction of Graphs with Applications to Electrical Networks*. [arXiv:1102.2950, §II.A, equations (1)–(2)](https://arxiv.org/html/1102.2950#S2.SS1). Elimination of internal potentials and the electrical Schur complement; spectral formulas (12), (15) are derived in this note.

Related notes: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component|Boundary Forest States: What to Retain from a Component]], [[en/Polynomial toponomes/Forest Coefficients and the Laplacian Polynomial|Forest Coefficients and the Laplacian Polynomial]], [[en/Spectra and diagonalization in polyform algebra/Diagonal Representation of Polyforms and Duality|Diagonal Representation of Polyforms and Duality]], [[en/Spectra and diagonalization in polyform algebra/Eigenspaces, Projectors, and Reconstruction of Polyforms|Eigenspaces, Projectors, and Reconstruction of Polyforms]], [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry|The Spanning-Tree Layer and Boundary Resistance Geometry]], [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction|The Four-Point Passport and State Reduction]].

Series navigator: [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]].

[[ru/Граничные полиномы и сочленение графов/От лесного паспорта к спектральным граничным данным|Русский]]
