---
title: SLR Codes of Hexagonal Chains
date: '2026-11-02'
updated: 2026-11-08
revision: 2
translated_revision: 7
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-slr-code
order: 3
description: 'SLR codes for abstract hexagonal chains: seam orientations, reflection, chain reversal, and classification up to graph isomorphism.'
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/SLR-код гексагональных цепочек|SLR-код гексагональных цепочек]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

Closure of five spectral coordinates and transitions for the three output edges of a hexagon were proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]]. We now describe an entire chain configuration and distinguish a change of graph from a change in how it is read.

An SLR code retains the sequence of straight continuations and turns. Reflection interchanges left and right turns; chain reversal changes both their order and their signs. The characteristic polynomial is preserved, but the passport at a chosen end of the chain may change.

> [!note] Origins and scope of the result
> Ternary encoding of hexagonal chains is classical: Milosavljević and Stevanović [1, §2, Definition 1 and Figure 2] use $F,R,L$ and conventional end symbols. Here $F$ is replaced by $S$, and the end marker and seam vertex correspondences are specified explicitly. The proofs below concern the stated abstract open chain. Class counting uses the classical Burnside lemma; neither the encoding nor its presentation in PMG notation is claimed to be scientifically new.

## The chains being encoded

We use admissibility from [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]]. Every core is $C_6$, and every seam is a single edge. In each internal core, the input and output edges are vertex-disjoint. Nonadjacent cores do not intersect; there is no closure or other identification. All conductances equal $1$, and shared edges are counted once.

Write $N$ for the number of cores and $n$ for the number of vertices of the resulting graph. Such a chain has

$$
n=4N+2,\qquad |E(G)|=5N+1
\tag{1}
$$

Each new core adds four vertices and five edges. The graph is connected, and its cycle rank is $N$.

For $N=1$, there is a single graph $C_6$, treated separately. From now on, $N\ge2$.

### Endpoint order and the three letters

Choose a traversal direction and an ordered attachment edge on the first core. Orient the traversals of subsequent cores so that each shared edge is traversed in opposite directions. In the figures, all cycles are then traversed clockwise.

> [!info] The letter of an internal core
> **Definition.** Let the active pair of the old fragment be $(a,b)$. Number the new core as $C(0,1,2,3,4,5)$ and attach it by
>
> $$
> 0\mapsto b,\qquad 1\mapsto a
> \tag{2}
> $$
>
> Choose its output pair in cycle traversal order:
>
> $$
> L:(2,3),\qquad S:(3,4),\qquad R:(4,5)
> \tag{3}
> $$
>
> These are all edges vertex-disjoint from the input $01$. In a development by regular hexagons, successive center-to-center directions turn by $+\pi/3$, $0$, and $-\pi/3$, respectively.

![Reversed input endpoint order and the three output seams](images/SLR%20Letters%20and%20Seam%20Endpoint%20Order.svg)

**A letter belongs to an internal core.** The red seam is the input; the blue seam is the output. Center-to-center arrows explain the letters; the graph itself remains undirected. Reversing the order in (2) gives “left” and “right” the same meaning at every step.

> [!info] Full code and turn word
> **Definition.** For a chain $K_1,\ldots,K_N$, set
>
> $$
> w=S u,\qquad u=\alpha_2\cdots\alpha_{N-1},
> \qquad \alpha_i\in\{S,L,R\}
> \tag{4}
> $$
>
> The initial $S$ is a conventional marker for the first connection between cores. It does not represent a turn within $K_1$. Thus
>
> $$
> |w|=N-1,\qquad |u|=N-2
> $$
>
> The final core has no output used in assembly, so it receives no separate turn letter.

For example, $S$ encodes two cores; $SS$ encodes three cores with a straight continuation; $SL$ and $SR$ encode three cores with one bend. Up to vertex relabeling and reflection, the pair in [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]] corresponds to $SS$ and $SL$.

## A word specifies an abstract graph

The construction from a code requires no coordinates. Start with $C_6$ and a chosen edge. Read $u$ from left to right, attaching a new core by (2), creating four new vertices, and choosing an output by (3) at each step. After all letters have been read, attach the final core. Its free edges are not used for further assembly.

> [!info] Every word gives an admissible construction
> **Proposition.** Every $u\in\{S,L,R\}^{N-2}$ specifies an admissible abstract chain, unique up to isomorphism for fixed initial markings. Every chain in the stated class arises this way.

> [!note]- Validity and completeness of the construction
> **Proof.** The output of a new core is disjoint from its input. Both output vertices are therefore created at the current step and belong to no earlier core. Identifying the next cycle only along this output creates no nonadjacent contact. This proves admissibility by induction.
>
> Conversely, choose an initial end and a traversal direction of the first cycle of a given chain. The shared seam uniquely extends the consistent traversal to the neighboring core. Relabel its input as $01$; its admissible output occupies exactly one position in (3). This recovers all letters. Renaming the four new vertices does not change the graph. $\square$

Abstract admissibility differs from realization by regular hexagons in a common plane. For example, $SLLLL$ has six cores: in a regular development, the final core touches the first, but this additional identification **is not part** of the code. The abstract graph still has $26$ vertices and $31$ edges. Merging vertices that coincide in the drawing would change the problem.

This does not prevent a plane embedding of the abstract graph with deformed faces: each new core can be attached in the outer face. Requiring regular cells of a fixed hexagonal lattice is an additional geometric condition.

## Reflection and reversal of the chain

Introduce the letter substitution

$$
\bar S=S,\qquad \bar L=R,\qquad \bar R=L
$$

For $u=\alpha_2\cdots\alpha_{N-1}$, write $u^{\leftarrow}=\alpha_{N-1}\cdots\alpha_2$ for the word in reverse order.

> [!info] Two code symmetries
> **Proposition.** Reflection and reading from the opposite end change the code according to
>
> $$
> \begin{aligned}
> \mu(Su)&=S\bar u,\\
> \iota(Su)&=S\overline{u^{\leftarrow}}
> \end{aligned}
> \tag{5}
> $$
>
> Both operations preserve the unmarked abstract graph. They are commuting involutions, and their composition gives
>
> $$
> \mu\iota(Su)=Su^{\leftarrow}
> \tag{6}
> $$

> [!note]- Why reversal changes both the order and the letters
> **Proof.** Reflection reverses the traversal direction of each cycle. Restoring the adopted input numbering changes local indices by $i\mapsto1-i\pmod6$. Output $(2,3)$ becomes $(5,4)$, that is, output $R$ with reversed order; the opposite output remains opposite. Reflection therefore replaces every $L$ by $R$ and conversely.
>
> When the chain is read from its other end, input and output exchange roles in every internal core. If the old output starts at $j$, the new cycle numbering starts there; the old input then occupies position $6-j$. Thus $2\leftrightarrow4$, while $3$ is preserved. The cores are also read in reverse order. This gives the second formula in (5). The initial marker $S$ is written anew and is not part of the reversed turn word.
>
> Applying reflection twice or reversal twice restores the code. Letterwise substitution commutes with reversal of their order, giving (6). $\square$

![Four representations of one chain under reflection and reversal](images/Reflection%20and%20Reversal%20of%20an%20SLR%20Code.svg)

**Four representations of one graph.** For $w=SLS$, the results are $SLS$, $SRS$, $SSR$, and $SSL$. The starting end and traversal direction change, but suitable relabeling makes the vertex and edge sets coincide. Some of these four representations coincide for symmetric words.

Simply reversing the letters of $u\mapsto u^{\leftarrow}$ also preserves the graph class, but under our convention it describes the composition of reflection and chain reversal, not merely reading from the other end. The entire string $w$, including its initial marker, must not be reversed.

## Which words specify the same graph

Preservation of the graph under (5) alone is insufficient for classification: other coincidences must be excluded. We can do this by recovering the cores from the graph itself.

> [!info] Cores are recognizable as six-edge cycles
> **Lemma.** Every simple cycle of length $6$ in a chain of the stated class is an original core. More generally, each simple cycle is the boundary of a consecutive segment of $k$ cores and has length $4k+2$.

> [!note]- Recovering the cores without a prescribed decomposition
> **Proof.** The original $N$ cycles are linearly independent in the cycle space over $\mathbb F_2$: each has edges belonging to no other core. The dimension of this space is the cycle rank $N$, so the cores form a basis.
>
> Any simple cycle is the symmetric difference of some set of cores. A nonconsecutive set splits into disjoint segments and produces a disconnected edge set, so it cannot be a simple cycle. For a consecutive segment, shared edges cancel. Attaching each next core replaces one boundary-cycle edge by a five-edge path with new internal vertices. The result is one simple cycle of length $6+4(k-1)=4k+2$. Length $6$ is possible only for $k=1$. $\square$

> [!info] Classification of open hexagonal chains
> **Theorem.** For two codes with the same number of cores,
>
> $$
> \boxed{
> G(Su)\cong G(Sv)
> \ \Longleftrightarrow\
> v\in\{u,\bar u,u^{\leftarrow},\overline{u^{\leftarrow}}\}}
> \tag{7}
> $$
>
> The isomorphism need not preserve the initial end, traversal direction, vertex labels, or output marking.

> [!note]- Proof that the four symmetries are complete
> **Proof.** Sufficiency follows from (5)-(6). For necessity, apply the lemma: any graph isomorphism maps cores to cores. Two cores are adjacent exactly when they share an edge, so their path is also recovered. An isomorphism either preserves or reverses its order.
>
> Fix one of these two possibilities. The image of the first seam is already known. An isomorphism of the first cycle has two possible correspondences between the seam endpoints. Once the correspondence is chosen, the map of the entire cycle is unique. On the next cycle, the images of two adjacent vertices are already specified, so its map is also unique; continue inductively.
>
> Thus only the choice of path end and the order of the first seam's endpoints remain. They give exactly the operations on the right-hand side of (7), with possible coincident results for symmetric words. There are no other identifications of codes. $\square$

The theorem concerns precisely open chains of $C_6$ with disjoint edge seams and no additional contacts. It does not classify arbitrary cores, branching assemblies, or closed constructions from [[en/Graph Transformations and Gluing/Chains of cores/Closing a Chain - Rings and the Möbius Effect|Closing a Chain: Rings and the Möbius Effect]].

### A representative and the number of classes

For enumeration, fix the order $S<L<R$ and select the lexicographically least of the four words in (7). This gives a canonical representative of a graph class. Such canonicalization uses the code itself, not the computed spectrum.

Let $m=N-2$ be the number of turn letters. By Burnside's lemma [2, Theorem 3.33], the number of orbits is the mean number of fixed words of the four operations. Here the counts are

| Operation on $u$ | Number of fixed words |
|---|---:|
| Identity | $3^m$ |
| Interchanging every $L\leftrightarrow R$ | $1$ |
| Reversing the order without interchanging letters | $3^{\lceil m/2\rceil}$ |
| Reversing the order and interchanging letters | $3^{\lfloor m/2\rfloor}$ |

For the last operation, each mirrored pair of positions is determined by one letter, and the middle letter of an odd-length word must be $S$. Hence

$$
\boxed{
c_N=\frac{3^{N-2}+1+
3^{\lceil(N-2)/2\rceil}+3^{\lfloor(N-2)/2\rfloor}}4
}
\qquad(N\ge2)
\tag{8}
$$

This counts graph classes under (7), not distinct spectra.

| $N$ | $n$ | Words $u$ | Graph classes |
|---:|---:|---:|---:|
| 2 | 10 | 1 | 1 |
| 3 | 14 | 3 | 2 |
| 4 | 18 | 9 | 4 |
| 5 | 22 | 27 | 10 |
| 6 | 26 | 81 | 25 |
| 7 | 30 | 243 | 70 |
| 8 | 34 | 729 | 196 |

![Four nonisomorphic graphs made from four hexagons](images/Four%20Classes%20of%20Four%20Hexagons.svg)

**Four classes for $N=4$.** In the adopted order, their representatives are $SSS$, $SSL$, $SLL$, and $SLR$. All have the same matroid parameters by [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]]. Their nonisomorphism follows from (7), not from the appearance of the drawings.

## Letter codes and spectral matrices

The passport notation is retained:

$$
s=(A,B,C,D,E)^{\mathsf T},\qquad
A=\chi_G(\xi)=\det(\xi\mathbf I_n-\mathbf L_G)
$$

The other four coordinates are principal minors, a signed adjugate entry, and the internal minor on the active pair; their precise definitions are given in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#Five coordinates and their meaning|Five coordinates and their meaning]]. Interchanging the pair endpoints acts by

$$
\mathbf J(A,B,C,D,E)^{\mathsf T}
=(A,C,B,D,E)^{\mathsf T}
$$

The published matrices $\mathbf T_2,\mathbf T_3,\mathbf T_4$ use the identification $(0,1)=(a,b)$. Under convention (2), the old passport is first permuted, so the letter matrices are

$$
\boxed{
\mathbf U_L=\mathbf T_2\mathbf J,\qquad
\mathbf U_S=\mathbf T_3\mathbf J,\qquad
\mathbf U_R=\mathbf T_4\mathbf J
}
\tag{9}
$$

This changes the input order; it is not a new closure proof. Multiplication by $\mathbf J$ **on the right** is essential; conjugation $\mathbf J\mathbf T_j\mathbf J$ would also change the output order.

Let $s_1$ be the passport of a single $C_6$ from [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#One graph, two passports, different continuations|One graph, two passports, different continuations]], and let $\mathbf e_1=(1,0,0,0,0)^{\mathsf T}$. After attaching the final core, conventionally mark its edge opposite the input. The full passport and characteristic polynomial are then

$$
\begin{aligned}
s_w&=\mathbf U_S\mathbf U_{\alpha_{N-1}}\cdots
\mathbf U_{\alpha_2}s_1,\\
\chi_w&=\mathbf e_1^{\mathsf T}s_w
\end{aligned}
\tag{10}
$$

The leftmost $\mathbf U_S$ is the final attachment. The initial symbol $S$ in $w=Su$ is a marker, not an additional initial transition before reading $u$. For $u=\varnothing$, formula (10) gives the two-core graph.

For a four-core example, the three descriptions correspond as follows:

| Description | Word | Meaning |
|---|---|---|
| Full code | $SLR$ | The initial marker and two internal turns |
| Internal word | $u=LR$ | Outputs of the second and third cores |
| Operation word starting from one core | $LRS$ | Two turns and the terminal attachment |

Matrices act from right to left: $s_{SLR}=\mathbf U_S\mathbf U_R\mathbf U_Ls_1$. Reading letters from left to right therefore agrees with writing matrix factors in reverse order.

> [!example] An orientation error becomes visible with four cores
> **Computed directly.** For the rooted polynomial $P_G(t)=\det(\mathbf I_n+t\mathbf L_G)$,
>
> $$
> P_{SLL}(1)=220348791,\qquad
> P_{SLR}(1)=220480560
> \tag{11}
> $$
>
> If the input endpoint order is preserved when constructing $SLL$, instead of using (2), the resulting graph is isomorphic to $SLR$. Three cores do not yet reveal this error: the initial passport is symmetric in $B,C$.

### What reflection does to the passport

The relations $\mathbf T_4=\mathbf J\mathbf T_2\mathbf J$ and $\mathbf J\mathbf T_3\mathbf J=\mathbf T_3$ imply

$$
\mathbf U_{\bar\alpha}=\mathbf J\mathbf U_\alpha\mathbf J,
\qquad \mathbf J s_1=s_1
\tag{12}
$$

> [!info] The spectral action of reflection
> **Proposition.** For the complete terminal marking in (10),
>
> $$
> s_{\mu(w)}=\mathbf J s_w,\qquad
> \chi_{\mu(w)}=\chi_w
> \tag{13}
> $$

> [!note]- Derivation of the reflection action
> **Proof.** Substitute (12) into product (10). Between neighboring factors, the pairs $\mathbf J^2=\mathbf I$ cancel; the initial state is preserved, and $\mathbf U_S$ commutes with $\mathbf J$. One left factor $\mathbf J$ remains. It does not change the first coordinate. $\square$

### Reversal takes us to the other end

Graph isomorphism under reversal implies

$$
\chi_{\iota(w)}=\chi_w
\tag{14}
$$

This is equality of polynomials, not the assertion $s_{\iota(w)}=s_w$ or $s_{\iota(w)}=\mathbf J s_w$. The terminal marking of the reversed code lies at the other end of the original graph. Reversing letter order in the matrix product also does not mean inverting the matrices themselves.

![One graph with different spectral passports at its two ends](images/Two%20Ends%20of%20One%20SLR%20Chain.svg)

**One graph, different marked boundaries.** The codes $SLS$ and $SSR=\iota(SLS)$ describe the same four-core graph. In the figure's construction, its right terminal pair is $(15,16)$ and its left pair $(3,4)$. Direct minors on these pairs differ.

For an exact numerical check, set $\mathbf R=\operatorname{diag}(1,-1,-1,-1,1)$ and $z_w=\mathbf R s_w(-1)$. Since $n=4N+2$ is even, the first coordinate is $P_G(1)=(-1)^n\chi_G(-1)$.

| Coordinate $z$ | $SLS$: right end | $SSR$: left end |
|---|---:|---:|
| $A(-1)$ | 221771751 | 221771751 |
| $-B(-1)$ | 98986375 | 98976277 |
| $-C(-1)$ | 98986738 | 98943538 |
| $-D(-1)$ | 38074862 | 38051101 |
| $E(-1)$ | 37645206 | 37629575 |

The vectors neither coincide nor differ merely by interchanging their second and third coordinates. This is a concrete example of the full state's dependence on boundary marking while the graph spectrum remains unchanged.

## Checks and limits of the conclusion

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_slr_code.py) constructs graphs directly from cycles and vertex identifications, without using spectral matrices to construct edges. It performs the following exact checks:

- for all $364$ words with $2\le N\le7$, it finds every six-edge cycle and recovers the original cores;
- it independently groups graphs by isomorphism; the resulting classes agree exactly with the orbits in (7), not merely in their number;
- it verifies isomorphisms of the reflected and reversed graphs for each word: $728$ correspondences in total, checking every edge;
- for all $121$ words with $2\le N\le6$, it compares the full Laplacian characteristic polynomial with (10); for all $13$ words with $N\le4$, it compares all five polynomial coordinates;
- it symbolically verifies (12), (13), polynomial equality under reversal on the stated finite set, numerical examples (11), the passports at both ends, and the error caused by preserving input order;
- it additionally enumerates orbits through $N=10$ and compares their number with (8).

Graph isomorphism is checked without using spectral equality as a criterion. The main computations use integers and exact polynomials. The [results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/slr-code-results.json) and [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) accompany the drawing scripts.

The validity of the code, the two symmetry rules, and completeness of classification (7) are proved **within the specified class of abstract open chains**. Formula (8) counts their graph isomorphism classes. Neither its proof nor the finite spectral checks establish injectivity of “code → full boundary passport,” “graph class → characteristic polynomial,” or “graph class → $P_G(1)$.” These three problems also differ in which markings and symmetries must be retained. The first problem, for the adopted terminal marking, is solved separately in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]; the two scalar conjectures are stated in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains|Spectral Distinguishability of SLR Chains]].

Changes to one or several seam positions are considered in [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains|Spectral Differences of SLR Chains]], using the alphabet, matrix product order, and code symmetries adopted here.

Fixed and periodic words as repetitions of a marked runner are considered in [[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns|Weaving SLR Chains and Constant Turns]]: a constant turn is defined without requiring a regular planar layout, and spectral data are computed by powers of the transfer matrix.

Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].

## Sources and connections

1. N. Milosavljević, D. Stevanović. *Detour Index of Hexagonal Chains*. MATCH Communications in Mathematical and in Computer Chemistry **72** (2014), 137-152. [§2, Definition 1 and Figure 2, pp. 139-140](https://match.pmf.kg.ac.rs/electronic_versions/Match72/n1/match72n1_137-152.pdf#page=3). The classical ternary description of internal core positions; spectral passports are not the subject of that article.
2. C. McMullen. *Sets, Groups and Knots. Course Notes*, Math 101, Harvard University. [Theorem 3.33, p. 49](https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/101/course/course.pdf#page=49). Burnside's lemma for orbit counting; the table of fixed SLR words and formula (8) follow by direct application.

Supporting notes: [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]], [[en/Graph Transformations and Gluing/Chains of cores/Why Chain Configuration Preserves Matroid Parameters|Why Chain Configuration Preserves Matroid Parameters]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons|Two Isomers of Three Hexagons]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]].
