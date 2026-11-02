---
title: Reconstructing a Chain from Its Boundary Response
date: '2026-11-02'
updated: '2026-11-02'
revision: 1
translated_revision: 5
status: draft
text_prepared_by: ChatGPT
lang: en
translation_key: isomer-spectra-boundary-response
order: 6
description: 'Exact recovery from three rational boundary responses: dynamic, electrical, and probabilistic interpretations, error bounds, and limits of
  stability.'
---

Russian version: [[ru/Преобразования и сочленения графов/Спектры изомеров/Восстановление цепочки по граничному отклику|Восстановление цепочки по граничному отклику]].

Results, their status, and reading routes: [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectra of Isomers - Results and Open Questions|Spectra of Isomers: Results and Open Questions]].

Imagine a chain of identical hexagonal cores. Each core consists of six vertices joined in a cycle by six edges. Adjacent cores share one edge; within the chain, assembly can continue straight, turn left, or turn right. The number of cores and the order of turns are unknown. Which data at two marked vertices at one end suffice to recover this configuration?

Recovery from five integers at the spectral specialization $\xi=-1$ was proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]. Here we show that these integers can be recovered from three rational entries of the matrix $(\mathbf I+\mathbf L_G)^{-1}$ on the marked pair. These are data of the original graph. They can be obtained from a dynamic response on that graph; a separate electrical realization requires an auxiliary graph. We explicitly distinguish these ways of obtaining the data and their limitations.

## The results in plain language

> [!info] What three exact boundary numbers determine
> **Exact reconstruction.** Suppose it is known in advance that the graph is assembled, under the rules below, from hexagonal cores with unit edge weights. Choose an ordered pair of vertices on the free edge of the last core opposite its input seam.
>
> The two self-responses and one mutual spectral response of this pair give three numbers. **If known exactly, they uniquely determine the number of cores and the entire sequence of turns in the chain.** These numbers are defined below; the chain length need not be known in advance.
>
> This is a theorem about the information contained in a specified passport. Obtaining that passport from physical measurements requires specifying a process and experimental conditions. A single ordinary resistance between these vertices does not determine the turns of the chain.

One way to obtain the required numbers without adding edges is to observe heat diffusion. Suppose every vertex has unit heat capacity, every edge has unit thermal conductance, and there is no heat exchange with the environment. In the first experiment, inject one unit of heat at one marked vertex; in the second, inject it at the other. In each experiment, record the temperatures of **both** vertices over time. This gives four curves; the two cross-response curves coincide by reciprocity. Weighted integration then gives the three numbers in the theorem. These are two experiments with time records, not two individual readings.

The presence of three data values has nothing to do with requiring three neighbors. Both chosen terminal vertices in this graph have degree $2$. Equality of the cross-responses follows from symmetry of the Laplacian matrix of an undirected graph; geometric symmetry of the chain is not required.

> [!info] What changes in the presence of errors
> **Accuracy matters increasingly as reconstruction reaches farther into the chain.** A long common end of two chains increasingly hides differences in their distant parts. For example, for two chains of seven hexagons—one straight and one with a single distant bend—all three spectral response numbers differ by at most approximately $2{,}46\cdot10^{-11}$ under the chosen normalization.
>
> Thus no fixed accuracy for these three numbers guarantees recovery of chains of every length. If the number of hexagons is bounded, however, a positive, albeit very conservative, error tolerance can be given.

There is also a probabilistic interpretation. Partition the graph into a random forest and choose one root in each component; all such **forests with chosen roots** are equally likely. The exact joint distribution of the two indicators “the first contact is a root” and “the second contact is a root” also determines the entire chain. Estimating these probabilities from a sample raises the accuracy question again.

The result provides identification within a known class of constructions from exactly specified data. Three rational numbers may have large denominators; having few coordinates does not make them easy to measure. A practical problem with noise additionally requires a size bound, an error model, and a check of how many constructions are compatible with the observations. The stability estimates below concern the three numbers $\mathbf K_B$, rather than optimal use of the entire time record.

## The chain model and the boundary location

We use the abstract open chains of [[en/Graph Transformations and Gluing/Chains of cores/Cores, Seams, and Admissible Chains|Cores, Seams, and Admissible Chains]] and [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]]. The cores $C_6$ form a path, joined along edges. The two seams of an intermediate core have no common vertices; nonadjacent cores do not intersect. There are no additional identifications or closure. All conductances are one, and each shared edge is counted once. For $N$ cores, the number of vertices is $n=4N+2$.

For $N\ge2$, the full code is written as $w=Su$, where $u$ contains $N-2$ letters. The initial $S$ is a marker. For an ordered active pair $(x,y)$, the new core is numbered cyclically so that $(0,1)=(y,x)$; the outputs $L,S,R$ are numbered $(2,3),(3,4),(4,5)$. On the last core, the boundary $B=(x,y)$ is the free edge opposite the input seam, with its endpoints ordered by rule $S$. A single $C_6$ is treated separately: its boundary is a chosen ordered edge.

This is specifically a **marked ordered boundary**. Exchanging the contacts corresponds to reflecting the code; moving them to the other end requires reversing the chain. If an unmarked graph class is required, apply the four word symmetries described in [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]] after decoding.

## Two boundary response matrices

Let $\mathbf L_G$ be the Laplacian matrix in the vertex basis. Set $\mathbf H=\mathbf I_n+\mathbf L_G$, and let $I=V(G)\setminus B$ denote the internal vertices. The matrix $\mathbf H$ is positive definite.

This shift arises from the spectral and forest problem: at $\xi=-1$, the determinant and consistently signed minors become positive integer counts of rooted forests. An inverse algorithm has already been proved for their transfer rule. Passing to a block of the inverse matrix asks whether recovery remains possible after normalizing these integer data. The auxiliary electrical network appears only as one realization of the resulting operator.

> [!info] Boundary data at a unit spectral shift
> **Definition.** The normalized spectral boundary passport and its inverse matrix are
>
> $$
> \mathbf K_B=(\mathbf H^{-1})_{BB},\qquad
> \boldsymbol\Lambda_B^{(1)}=\mathbf K_B^{-1}
> \tag{1}
> $$
>
> Equivalently, the second matrix is the Schur complement:
>
> $$
> \boldsymbol\Lambda_B^{(1)}=
> \mathbf H_{BB}-\mathbf H_{BI}\mathbf H_{II}^{-1}\mathbf H_{IB}
> \tag{2}
> $$

The superscript $(1)$ specifies the coefficient $1$ of $\mathbf I$ in the matrix $\mathbf L_G+\mathbf I$. The definition uses the original graph $G$; it requires no added vertices or edges. The relation of these data to dynamics, ordinary resistance, and an auxiliary electrical network is discussed below.

Introduce integer coordinates, retaining the notation of [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]]:

$$
\begin{aligned}
a&=\det\mathbf H=P_G(1)\\
b&=\det\mathbf H_{\widehat x},\qquad
c=\det\mathbf H_{\widehat y}\\
d&=(\operatorname{adj}\mathbf H)_{xy},\qquad
e=\det\mathbf H_{\widehat{\{x,y\}}}
\end{aligned}
\tag{3}
$$

A hat denotes deletion of rows and columns without recomputing degrees. Here $e$ is a numerical coordinate, not the unit form of polyform algebra. Jacobi's identity $ae=bc-d^2$ gives

$$
\boxed{
\mathbf K_B=\frac1a\begin{pmatrix}b&d\\d&c\end{pmatrix},\qquad
\boldsymbol\Lambda_B^{(1)}=\frac1e\begin{pmatrix}c&-d\\-d&b\end{pmatrix}
}
\tag{4}
$$

Under the spectral convention $\mathbf M_G(\xi)=\xi\mathbf I-\mathbf L_G$, we have $\mathbf M_G(-1)=-\mathbf H$. Thus the spectral Schur complement at $\xi=-1$ is $-\boldsymbol\Lambda_B^{(1)}$, while the corresponding resolvent block is $-\mathbf K_B$. Since $n$ is even, $P_G(1)=\chi_G(-1)$; the general rule is $P_G(1)=(-1)^n\chi_G(-1)$. The matrix $\mathbf H^{-1}$ also differs from the Greenian $\mathbf{Gr}=\mathbf L_G^+$.

## Why normalization retains the chain

Denote the three entries specifying the symmetric response matrix by

$$
r=K_{xx}=b/a,\qquad s=K_{yy}=c/a,\qquad h=K_{xy}=d/a
$$

They recover the fourth ratio

$$
k=\det\mathbf K_B=rs-h^2=e/a
\tag{5}
$$

Dividing an integer vector by its first coordinate usually loses its scale. For our states, the scale is determined by the coordinates being collectively coprime.

> [!info] Primitivity of the states
> **Lemma.** Every reachable state $\mathbf z=(a,b,c,d,e)^{\mathsf T}$ is primitive: the greatest common divisor of its five coordinates is $1$.

> [!note]- Proof of primitivity
> **Proof.** The initial vector of a single hexagon is
>
> $$
> \mathbf z_0=(320,144,144,56,55)^{\mathsf T}
> \tag{6}
> $$
>
> Its coordinates are collectively coprime. The integer matrices $\mathbf N_S,\mathbf N_L,\mathbf N_R$ in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]] have determinants $1$ and integer inverses. Multiplication by such a matrix preserves the common divisor of the coordinates in both directions. Every reachable state is obtained from (6) by a finite product of these matrices. $\square$

Let $\operatorname{den}(q)$ denote the positive denominator of a reduced rational fraction. From exact $r,s,h$, compute $k$ and then

$$
D=\operatorname{lcm}\bigl(
\operatorname{den}(r),\operatorname{den}(s),
\operatorname{den}(h),\operatorname{den}(k)\bigr)
\tag{7}
$$

> [!info] Recovery from three exact numbers
> **Theorem.** Within the chosen class of marked chains, the matrix $\mathbf K_B$, or equivalently $\boldsymbol\Lambda_B^{(1)}$, uniquely determines the full oriented SLR code and the number of cores $N$. Moreover,
>
> $$
> \boxed{D=a,\qquad \mathbf z=D(1,r,s,h,rs-h^2)^{\mathsf T}}
> \tag{8}
> $$
>
> Neither $a=P_G(1)$ nor $N$ needs to be known in advance. This establishes sufficiency of three rational data values; their minimality is not proved here.

> [!note]- Proof of recovery of the scale and code
> **Proof.** The denominators of the ratios $b/a,c/a,d/a,e/a$ divide $a$, so $D$ divides $a$. If $D<a$, integrality of $Db/a,Dc/a,Dd/a,De/a$ implies that the integer $a/D>1$ divides all five coordinates. This contradicts primitivity. Hence $D=a$, and (8) recovers the original vector.
>
> The decoding theorem of [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]] uniquely recovers the operation word from the full integer vector. For the full code $Su$, its state is $\mathbf z(uS)$: the terminal operation $S$ adds the last core and fixes the free boundary. After decoding, remove this terminal $S$ and add the initial marker $S$. The number of cores is the number of recovered operations plus $1$. Vector (6) is recognized separately as $N=1$. Invertibility in (1) proves the same statement for $\boldsymbol\Lambda_B^{(1)}$. $\square$

Formula (7) must be applied to **four** ratios, including the computed determinant $k$. For example, for a single $C_6$,

$$
r=s=\frac9{20},\qquad h=\frac7{40},\qquad k=\frac{11}{64}
$$

The least common multiple of the three original denominators is $40$, but including $k$ makes it $320$. This recovers (6).

### An example with four cores

Take the exact response

$$
\mathbf K_B=\frac1{220480560}
\begin{pmatrix}
98399833&37829429\\
37829429&98367457
\end{pmatrix}
\tag{9}
$$

Formulas (5)–(8) recover the vector

$$
\mathbf z=(220480560,98399833,98367457,37829429,37410444)^{\mathsf T}
$$

The inverse algorithm removes the operations $S,R,L$ and then reaches $\mathbf z_0$. The forward operation word is $LRS$, the full code is $SLR$, the number of cores is $N=4$, and the number of vertices is $n=18$. The integer states at each step are given in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State#Example: recovering the code SLR|Example: recovering the code SLR]].

For an arbitrary rational matrix, formula (8) gives only a candidate. The full recognition algorithm must be run: check admissibility of the intermediate states, arrival at exactly $\mathbf z_0$, and the terminal convention $uS$. Positive definiteness, primitivity, and Jacobi's identity alone do not guarantee that the candidate comes from a chain. Even successful recognition establishes compatibility with our model, not that an unknown network outside the specified class has the same construction.

## Obtaining the data from dynamics on the original graph

The required numbers can be obtained without additional connections if a known diffusion process is available on the original graph. Consider an idealized thermal model: the heat capacity of every vertex and the thermal conductance of every edge equal $1$ in consistent units, with no external heat exchange. Before each experiment, all temperatures relative to a common baseline are zero. At time $t=0$, one unit of heat is injected at vertex $j$. In this section, $t$ denotes time.

Let $\mathbf e_j$ be the unit coordinate column. The temperature vector satisfies

$$
\frac{d\mathbf u^{(j)}}{dt}=-\mathbf L_G\mathbf u^{(j)},\qquad
\mathbf u^{(j)}(0)=\mathbf e_j,\qquad
\mathbf u^{(j)}(t)=e^{-t\mathbf L_G}\mathbf e_j
$$

Write $F_{ij}(t)=(e^{-t\mathbf L_G})_{ij}$ for the temperature at $i$ after a unit impulse at $j$. This is the ideal impulse response of the linear model, not a claim that an instantaneous impulse can be produced in any physical object.

> [!info] Two dynamic experiments provide the required passport
> **Proposition.** For $i,j\in B$, the weighted integrals of the temperature responses are
>
> $$
> \boxed{K_{ij}=\int_0^\infty e^{-t}F_{ij}(t)\,dt}
> $$
>
> In particular, $r$ is obtained from $F_{xx}$, $s$ from $F_{yy}$, and $h$ from $F_{xy}=F_{yx}$. The factor $e^{-t}$ is introduced when processing the time record; it does not represent physical removal of heat from the vertices.

> [!note]- Proof of the dynamic response formula
> **Proof.** The symmetric matrix $\mathbf L_G$ is positive semidefinite. All eigenvalues of $\mathbf I+\mathbf L_G$ are positive, so
>
> $$
> \begin{aligned}
> \int_0^\infty e^{-t}e^{-t\mathbf L_G}\,dt
> &=\int_0^\infty e^{-t(\mathbf I+\mathbf L_G)}\,dt\\
> &=(\mathbf I+\mathbf L_G)^{-1}
> \end{aligned}
> $$
>
> The final equality follows by integrating the derivative of the matrix exponential; its limit at infinity is zero. Taking the block $BB$ gives (1). Symmetry of $\mathbf L_G$ implies symmetry of $e^{-t\mathbf L_G}$ and equality of the cross-responses. $\square$

| Experiment | Record at $x$ | Record at $y$ | After weighted integration |
| --- | --- | --- | --- |
| Impulse at $x$ | $F_{xx}(t)$ | $F_{yx}(t)$ | $r,h$ |
| Impulse at $y$ | $F_{xy}(t)$ | $F_{yy}(t)$ | $h,s$ |

Thus there are two experiments with two time records in each. Of the four records, one duplicates another by reciprocity. Geometric symmetry of the graph is unnecessary; in special symmetric cases, the self-responses may also coincide. Theorem (8) establishes sufficiency of three passport entries, not minimality of the number of physical measurements.

![Two heat impulses and processing of time records without adding edges](Dynamic%20Response%20of%20the%20Original%20Chain.svg)

**The graph is unchanged; a process on it is observed.** For a single $C_6$, the figure shows a self-response, a cross-response, and their weighted integrals. The curve formulas and integral values are checked exactly; the curves are drawn on a numerical scale. For a general chain, both experiments are needed because $F_{xx}$ and $F_{yy}$ may differ.

### A finite recording duration

The matrix $e^{-t\mathbf L_G}$ is nonnegative and has row sums $1$: it is also the transition probability matrix of the walk with generator $-\mathbf L_G$. Hence $0\le F_{ij}(t)\le1$, and the integral tail satisfies

$$
0\le K_{ij}-\int_0^T e^{-t}F_{ij}(t)\,dt\le e^{-T}
$$

If the absolute recording error is at most $\eta$ throughout $[0,T]$, the error in the weighted integral computed from that record is at most

$$
\varepsilon\le\eta(1-e^{-T})+e^{-T}
$$

Numerical integration error must be added separately. This is a sufficient bound for propagation of errors into the three numbers $\mathbf K_B$, not an optimal bound for reconstruction directly from complete time curves.

The assumptions of the dynamic model matter. With heat capacities $C_v$, the equation is $\mathbf C\dot{\mathbf u}=-\mathbf L_G\mathbf u$, where $\mathbf C=\operatorname{diag}(C_v)$; unknown or unequal heat capacities change the data and require separate analysis. A purely resistive network without energy storage has no such temperature process. Computing $\mathbf K_B$ from an already known matrix $\mathbf L_G$ produces a passport for comparing graphs, but is not a measurement of an unknown chain.

## Why ordinary terminal resistance does not distinguish turns

Now regard the original graph as an ordinary resistor network: every edge has resistance $1$, and no connections are added. Only the contacts $x,y$ on the chosen free terminal edge are accessible. Inject current at $x$ and withdraw it at $y$. All steady relations between current and voltage difference on this pair are determined by a single effective resistance.

> [!info] Terminal resistance depends only on the number of cores
> **Proposition.** For every admissible chain of $N$ cores, the resistance between the endpoints of the chosen free terminal edge is the number $R_N$ defined recursively by
>
> $$
> \boxed{R_1=\frac56,\qquad
> R_N=\frac{4+R_{N-1}}{5+R_{N-1}},\quad N\ge2}
> $$
>
> The order of the letters $L,S,R$ does not affect this resistance. The statement concerns this choice of pair, not all pairwise resistances in the graph.

> [!note]- Proof of the resistance recurrence
> **Proof.** We prove a stronger statement: any free edge of the last core other than the input edge may be chosen. For a single $C_6$, a unit edge is in parallel with a path of resistance $5$, so $R_1=5/6$.
>
> The preceding part of the chain meets the last core only at the two endpoints of the input seam. Replace this entire part, including the shared edge, by its equivalent resistance $R_{N-1}$. The shared edge is not added a second time. In the last core, the chosen output edge of resistance $1$ is in parallel with a path consisting of four unit edges and the resistance $R_{N-1}$. Therefore,
>
> $$
> R_N=1\mathbin{\|}(4+R_{N-1})
> =\frac{4+R_{N-1}}{5+R_{N-1}}
> $$
>
> Here $a\mathbin{\|}b=ab/(a+b)$ denotes the resistance of parallel branches. The position of the input edge on the remaining path does not change the sum of series resistances. Induction applies to every admissible choice of active seams. $\square$

The first values are

$$
R_1=\frac56,\quad R_2=\frac{29}{35},\quad
R_3=\frac{169}{204},\quad R_4=\frac{985}{1189},\quad
R_5=\frac{5741}{6930}
$$

![Straight and bent chains have the same terminal-edge resistance](Equal%20Terminal%20Resistance.svg)

**A steady experiment on this pair loses the positions of the turns.** The straight chain $SS$ and the bent chain $SL$, each with three cores, have resistance $169/204$. Their spectral responses $\mathbf K_B$ differ. The lower diagram shows the series and parallel connections used in the proof.

The ordinary two-point Dirichlet-to-Neumann operator of the original network is

$$
\boldsymbol\Lambda_B^{(0)}=
\frac1{R_N}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
$$

It has rank $1$ and determines only potential differences. Repeating steady experiments with different current magnitudes at the same contacts adds no information about the turns. Dynamic experiments use additional data: the time dependence of the response.

## An auxiliary electrical realization

The matrix $\mathbf I+\mathbf L_G$ can be realized by a separate resistor network. Construct an **auxiliary graph $G^*$**: add one common vertex $*$, and connect every vertex of the original graph $G$ to it by a separate edge of conductance $1$, that is, through a separate resistor of resistance $1$ in the chosen units. This applies to all internal vertices and both contacts.

Fix the potential of $*$ at zero. The potentials of the original vertices are not fixed: resistors lie between them and $*$. Connecting every vertex directly to ground by ideal wires would give a different circuit with zero voltages. Deleting the row and column of $*$ from the Laplacian of $G^*$ gives $\mathbf I+\mathbf L_G$. With external currents only at $x,y$ and their return through $*$,

$$
\mathbf H\mathbf v=\mathbf j,\qquad
\mathbf j_I=0,\qquad
\mathbf v_B=\mathbf K_B\mathbf j_B
\tag{10}
$$

The two experiments $\mathbf j_B=(1,0)^{\mathsf T}$ and $\mathbf j_B=(0,1)^{\mathsf T}$ give the two columns of $\mathbf K_B$. In each experiment, two voltages relative to $*$ are measured. Two of the four readings are equal by electrical reciprocity, so the matrix is specified by $r,s,h$. The contact with no external current remains connected to the network and to its resistor leading to $*$; its potential is **not fixed at zero**. Alternatively, prescribe two basis voltage vectors and measure the currents to obtain the columns of $\boldsymbol\Lambda_B^{(1)}$.

![A network with unit shunts to ground and two boundary experiments](Two%20Experiments%20with%20a%20Grounded%20Chain.svg)

**The auxiliary circuit: two experiments, four readings, three matrix entries.** The figure shows one core of the original graph and added resistors at all its vertices. Every ground symbol denotes the same common vertex $*$. This circuit realizes the required operator but changes the original electrical network.

The additional resistors must be built into the model device in advance. Such individual connections to every internal vertex cannot be made through only two contacts of an already assembled unknown chain. This realization is therefore not a two-electrode method for examining an ordinary chain. It is introduced after the spectral definition (1) as a physical interpretation, rather than as the starting problem of the investigation. Increasing vertex degrees in $G^*$ is not a condition of the reconstruction theorem for $G$.

This setting concerns the discrete Schrödinger operator $\mathbf L+\mathbf I$ and standard Schur reduction. Inverse problems for graph conductances and diagonal potentials are studied, for example, in [3]. Here the unknown is the assembly order within a fixed discrete family; theorem (8) is proved by the specific SLR decoder, not by applying general claims from [3]. The original unit conductances, unit shunts, and measurement scale are assumed known.

## Probabilistic interpretations

### Random roots

Choose uniformly from all spanning rooted forests. An unrooted forest with components $T$ receives total weight $\prod_T\#T$, since that is its number of root choices. Uniform choice of forests **without** roots would therefore define a different model.

The matrix-forest theorems [1] and the determinantal law of the root set [2, Theorem 3.4] give

$$
\begin{aligned}
r&=\Pr(x\text{ is a root})\\
s&=\Pr(y\text{ is a root})\\
h&=\Pr(\text{the component of }x\text{ is rooted at }y)\\
k&=\Pr(x,y\text{ are both roots})=rs-h^2
\end{aligned}
\tag{11}
$$

In the third event, $x,y$ belong to the same component. For the root indicators $X_x,X_y$, we obtain the negative covariance

$$
\operatorname{Cov}(X_x,X_y)=-h^2
\tag{12}
$$

> [!info] Recovery from the joint law of two roots
> **Corollary.** The exact joint distribution of the ordered pair $(X_x,X_y)$ determines the marked chain. Three probabilities $p_x=\Pr(X_x=1)$, $p_y=\Pr(X_y=1)$, and $p_{xy}=\Pr(X_x=X_y=1)$ suffice:
>
> $$
> r=p_x,\qquad s=p_y,\qquad h=\sqrt{p_xp_y-p_{xy}}
> \tag{13}
> $$

> [!note]- Proof of the probabilistic corollary
> **Proof.** Equations (11) follow from the forest interpretations of $a,b,c,d,e$ after division by the total number $a$ of rooted forests. Jacobi's identity gives (12). The graph is connected, so $h>0$: there is a spanning tree rooted at $y$ and containing $x$. Thus the positive square root in (13) is uniquely selected. For data from our model it is rational and recovers $\mathbf K_B$; then apply (8). $\square$

It suffices to know the joint law of two indicators, without observing the roots throughout the graph. A finite sample, however, estimates this law with error; the theorem about exact probabilities alone gives no bound on the required sample size.

### A walk stopped at a random time

Consider a continuous-time Markov walk: along each incident edge, the particle jumps at rate $1$. Its generator is $-\mathbf L_G$, and the total rate of leaving a vertex is its degree. Independently choose a stopping time $T$ with exponential distribution of rate $1$. Then

$$
\mathbf W_{ij}=\Pr_i(X_T=j),\qquad
\mathbf W=\int_0^\infty e^{-t}e^{-t\mathbf L_G}\,dt
=(\mathbf I+\mathbf L_G)^{-1}
\tag{14}
$$

This is the standard representation of the resolvent by a stopped process; see [2, Lemma 3.3]. In the notation of [2], $L$ denotes the generator, corresponding here to $-\mathbf L_G$.

An equivalent discrete rule is: at vertex $v$, stop with probability $1/(\deg(v)+1)$ or move to each neighbor with the same probability. These probabilities sum to $1$. This is not a walk with the same total departure rate at every vertex.

The block $\mathbf W_{BB}$ equals $\mathbf K_B$. Starting at $x$ or $y$, one needs the probabilities of final stopping at $x$ and $y$; these give the same three numbers. Each full row of $\mathbf W$ sums to $1$, but a row of the boundary block usually sums to less than $1$: the process may stop at an internal vertex.

![Root probabilities and a stopped walk give the same matrix](Two%20Probabilistic%20Interpretations%20of%20the%20Response.svg)

**The same data have two probabilistic meanings.** The left panel shows the four joint outcomes of the two root indicators. The right panel shows one step at a vertex of degree $2$: two moves and stopping are equally likely. The equivalence concerns the probabilities in (11) and (14), not an identification of individual forests with trajectories.

## Why distant differences become hard to detect

Set $p=(r,s,h,k)$. The invariant region from [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]] is

$$
\mathcal D=
\left[\frac{43}{100},\frac9{20}\right]^2
\times\left[\frac{83}{500},\frac7{40}\right]
\times\left[\frac4{25},\frac9{50}\right]
\tag{15}
$$

All reachable normalized states lie in $\mathcal D$. For $\alpha\in\{S,L,R\}$, define the normalized transition

$$
\Phi_\alpha(p)=
\frac{(\mathbf N_\alpha(1,p)^{\mathsf T})_{2:5}}
{(\mathbf N_\alpha(1,p)^{\mathsf T})_1}
\tag{16}
$$

The denominator is common to all three matrices:

$$
D_\alpha(p)=55+34r+34s-2h+21k,\qquad
\frac{349}{4}\le D_\alpha(p)\le\frac{11131}{125}
\tag{17}
$$

Here $D_\alpha(p)$ is the normalized growth factor, while $D$ in (7) is the integer scale; these are different quantities.

> [!info] Contraction of normalized states
> **Lemma.** For any $p,q\in\mathcal D$, in the maximum norm on coordinates,
>
> $$
> \begin{aligned}
> \|\Phi_S(p)-\Phi_S(q)\|_\infty
> &\le\frac3{100}\|p-q\|_\infty\\
> \|\Phi_\alpha(p)-\Phi_\alpha(q)\|_\infty
> &\le\frac3{20}\|p-q\|_\infty,
> \qquad \alpha\in\{L,R\}
> \end{aligned}
> \tag{18}
> $$
>
> The constants are sufficient bounds; no optimality is claimed.

> [!note]- An exact contraction certificate
> **Proof.** For row $i=2,\ldots,5$, write $A_i(p)=(\mathbf N_\alpha(1,p)^{\mathsf T})_i$. The derivative of a ratio is
>
> $$
> \partial_{p_j}\frac{A_i(p)}{D_\alpha(p)}=
> \frac{N_{\alpha,i,j+1}D_\alpha(p)-N_{\alpha,1,j+1}A_i(p)}{D_\alpha(p)^2}
> $$
>
> The numerator is affine in $p$. Its absolute value is maximized at one of the $16$ vertices of the box; the denominator is bounded below by $(349/4)^2$. Summing these exact upper bounds over the four columns gives the following bounds for the sums of absolute derivatives in each Jacobian row. Every entry in the table is divided by the common denominator $15225125$.
>
> | Transition | Row $r$ | Row $s$ | Row $h$ | Row $k$ |
> | --- | ---: | ---: | ---: | ---: |
> | $S$ | $449256$ | $449256$ | $368668$ | $219456$ |
> | $L$ | $2272204$ | $449256$ | $1036928$ | $864528$ |
> | $R$ | $449256$ | $2272204$ | $1036928$ | $864528$ |
>
> The row maxima are less than $3/100$ and $3/20$, respectively. The region $\mathcal D$ is convex; integrating the derivative along the segment from $p$ to $q$ proves (18). This is a certificate over the entire region, not a check of finitely many chains. $\square$

If the same sequence of $j$ operations is attached to two different initial parts, this bound reduces the distance between their normalized states by at least a factor of $(20/3)^j$. For a common straight continuation, the stronger factor $(3/100)^j$ applies.

### A straight chain and a single distant bend

Let $j\ge1$. Compare the full codes

$$
w_A=S^{j+1},\qquad w_B=SLS^{j-1},\qquad N=j+2
\tag{19}
$$

The first graph has no bends; the second has one bend near the end opposite the measurements. The graphs are nonisomorphic. The working states $\mathbf z(S)$ and $\mathbf z(L)$ have normalized distance $3/235$; both are acted on by $\Phi_S^j$, including the terminal operation selecting the marked last core. From (18),

$$
0<\max_{i,l\in B}|K_{A,il}-K_{B,il}|
\le\frac3{235}\left(\frac3{100}\right)^j
\tag{20}
$$

Strict positivity follows from the exact reconstruction theorem. Meanwhile, the right-hand side tends to zero.

> [!info] No uniform positive error tolerance for all lengths
> **Theorem.** There is no number $\varepsilon>0$ such that measuring all three entries of $\mathbf K_B$ with absolute error at most $\varepsilon$ guarantees unique recovery of every admissible chain of arbitrary length. This remains true even when comparing pairs with the same number of cores.

> [!note]- Proof of instability for unbounded length
> **Proof.** Given $\varepsilon>0$, choose $j$ so that the right-hand side of (20) is at most $2\varepsilon$. The mean of the two exact responses is at distance at most $\varepsilon$ from each in the coordinatewise norm. Thus the same observation with this error bound is compatible with two different chains. $\square$

![A distant bend and decreasing response differences as the common end grows](A%20Distant%20Bend%20and%20Response%20Accuracy.svg)

**A common continuation weakens the visible difference.** The upper diagram shows two chains of seven cores, with measurements at the right end. The plot shows response distances for the family (19); its points are computed as exact rational numbers, and the logarithmic scale is used only for display. The upper line is the proved bound (20).

| Number of cores $N$ | Maximum difference between the three entries, approximately |
| ---: | ---: |
| $3$ | $1{,}9289\cdot10^{-4}$ |
| $5$ | $6{,}1120\cdot10^{-8}$ |
| $7$ | $2{,}4588\cdot10^{-11}$ |
| $10$ | $2{,}2741\cdot10^{-16}$ |
| $14$ | $4{,}6367\cdot10^{-23}$ |

For example, at $N=3$, the exact distance is $38018321/197098726461$. All other fractions are recorded in the verification file. A small distance means that measurement and recovery are difficult, not that the spectral passports coincide.

### Matrix inversion itself is stable

On $\mathcal D$, Gershgorin's circles bound the eigenvalues of the symmetric matrix $\mathbf K_B$:

$$
\frac{51}{200}\le\lambda_{\min}(\mathbf K_B)
\le\lambda_{\max}(\mathbf K_B)\le\frac58
$$

Consequently,

$$
\kappa_2(\mathbf K_B)=\kappa_2(\boldsymbol\Lambda_B^{(1)})
\le\frac{125}{51}<2{,}451
\tag{21}
$$

Thus the loss of stability is caused by repeated inverse transfer, not by poor conditioning of a matrix of size $2\times2$. If $\boldsymbol\Lambda_B^{(1)}$ is measured with operator-norm error at most $\eta<8/5$, the standard identity for a difference of inverses gives

$$
\|\Delta\mathbf K_B\|_2\le\frac{25\eta}{64-40\eta}
\tag{22}
$$

## Guarantees under error bounds

### One inverse step

For a reachable noninitial state, the signs of $r-4/9,s-4/9$ determine the last operation:

| Operation | Sign of $r-4/9$ | Sign of $s-4/9$ |
| --- | --- | --- |
| $L$ | $-$ | $+$ |
| $S$ | $+$ | $+$ |
| $R$ | $+$ | $-$ |

The exact sector inequality margins and (17) give

$$
\min\{|r-4/9|,|s-4/9|\}\ge\delta_0,
\qquad \delta_0=\frac{71}{44524}
\tag{23}
$$

The initial state has $r=s=9/20$. All noninitial states satisfy $r,s\le9/20-\mu$, where

$$
\mu=\frac{615}{178096},\qquad \delta_0<\mu/2
$$

Thus the threshold $9/20-\mu/2$ first separates the initial state, and the threshold $4/9$ then identifies the sector. Errors in both diagonal coordinates strictly below $\delta_0$ allow these decisions for the current reachable state.

To verify (23), it suffices to use the lower margin $639/500$ for the absolute values of $9b'-4a',9c'-4a'$ divided by the old $a$, and the upper bound $a'/a$ from (17). The margin from $9/20$ is obtained similarly from $123/400$; both underlying inequalities are proved in [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]].

This guarantees **one** step. After applying $\mathbf N_\alpha^{-1}$ and normalizing again, the error may increase substantially. For a full marked graph, the first operation removed is always $S$: it completes the graph and selects the free boundary, rather than describing the unknown last internal turn.

### A known upper bound on the number of cores

> [!info] Sufficient accuracy when $N\le M$
> **Theorem.** Suppose the number of cores is known not to exceed $M\ge1$. Set
>
> $$
> A_M=\left\lceil320\left(\frac{11131}{125}\right)^{M-1}\right\rceil
> \tag{24}
> $$
>
> Any two distinct admissible marked states with $N\le M$ differ in at least one entry of $\mathbf K_B$ by at least $1/A_M^2$. Thus, under a coordinatewise absolute error
>
> $$
> \boxed{\varepsilon<\frac1{2A_M^2}}
> \tag{25}
> $$
>
> at most one such chain is compatible with the observation. If the data come from a chain in this class with the stated error, a compatible chain exists and is uniquely recovered.

> [!note]- Proof of the bound for bounded size
> **Proof.** Reaching the full state of a graph with $N$ cores takes $N-1$ transitions. By (17), $a\le A_M$. The denominators of the reduced fractions $b/a,c/a,d/a$ do not exceed $A_M$. Two distinct rationals with denominators at most $A_M$ differ by at least $1/A_M^2$. By theorem (8), different marked states differ in at least one of the three entries. If two such responses belonged to the same observation interval of radius $\varepsilon$, their distance would be at most $2\varepsilon$, contradicting (25). $\square$

The bound is very crude. For example, it permits recovery of the unique rational with a bounded denominator in each measurement interval, followed by (8) and the integer decoder. The number of arithmetic steps in the decoder is linear in word length, but integer sizes and required precision grow; no constant computational cost is claimed.

### Interval decoding and candidate verification

If (25) is unavailable, one can work with intervals for $r,s,h$. These give an interval for $k=rs-h^2$. Next, check whether stopping at the initial state is possible; if it is excluded and both diagonal intervals lie strictly on the required sides of $4/9$, the next operation is determined. Apply the integer inverse matrix to the interval vector $(1,r,s,h,k)$; division by its first coordinate is allowed only if its entire interval is proved positive.

Intervals usually widen because simple interval arithmetic loses dependencies between coordinates. Crossing a threshold, or failing to determine the denominator's sign, means that this verification method can no longer conclude. It **does not prove** that two compatible chains exist.

With known $M$, one can also enumerate all codes and test their exact responses against the original measurement box. This is a finite procedure with a completeness guarantee, but the number of candidates grows exponentially. Any candidate produced by the inverse algorithm should be checked against the original data, not merely the widened intermediate intervals.

![Three distinct outcomes when boundary data are inexact](Reconstruction%20with%20Inexact%20Data.svg)

**Uniqueness, ambiguity, and lack of a conclusion are different.** A single exact candidate after an exhaustive search up to the specified $M$ establishes uniqueness within that catalog. Two exact candidates prove ambiguity of the observation. Stopping the interval algorithm merely shows that the verification performed was insufficient.

Two reproducible examples for $N\le7$:

- Rounding the three entries in (9) to $14$ decimal places and allowing error at most $1/(2\cdot10^{14})$ leaves exactly the code $SLR$ in the complete catalog.
- For the codes $SSSSSS$ and $SLSSSS$, take the mean of the exact responses. With an error radius equal to half their distance, exactly these two codes remain in the same catalog. The exact radius is $121361886767503/9871437903919791971525040$, approximately $1{,}23\cdot10^{-11}$.

The catalog contains $365=1+\sum_{m=0}^{5}3^m$ marked states, including a single $C_6$. This is not the number of graph isomorphism classes. If no candidate fits, the observation is incompatible with the combined assumptions on model, size, and error bound; this alone does not identify which assumption fails.

## Exact checks and the status of the results

The [verification program](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/verify_boundary_response.py) uses integer and rational arithmetic. The [results](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/boundary-response-results.json) record complete fractions, example matrices, certificates, and counts.

- **General certificates:** all rational derivative bounds at the $16$ vertices of $\mathcal D$, sector margins, separation of the initial state, and eigenvalue and conditioning bounds.
- **Independent models:** for $14$ graphs, the matrices are constructed directly from edge lists. Solutions of the two electrical experiments, the Schur complement, the stopping-probability matrix, and the transfer result are compared. Forests for $C_6,S,SS,SL$ are enumerated afresh; $133184$ edge subsets are considered in total, including cyclic subsets, which are discarded.
- **Ordinary resistance of the original graph:** for a single $C_6$ and all $40$ codes with $2\le N\le5$, nodal equations are solved directly without additional edges. The checks cover the recurrence $R_N$, the two-point operator of rank $1$, and degree $2$ of both terminal contacts.
- **Dynamics on the original graph:** for a single $C_6$, the initial condition, the differential equation for the full matrix $e^{-t\mathbf L_G}$, and the self-response and cross-response integrals $9/20,7/40$ are checked exactly. For $14$ graphs, rational partial sums of the heat-resolvent expansion and bounds on their remainder are checked separately; no approximate integration is used in these checks.
- **Reconstruction:** all $9841=\sum_{m=0}^{8}3^m$ full states with $2\le N\le10$, together with a single $C_6$, are checked. Both the three response entries and the joint law of root indicators recover the primitive vector and code. There are no response collisions.
- **Stability:** the family (19) for $3\le N\le14$, all pairwise distances in catalogs up to $N=7$, and both examples of measurement intervals are computed exactly. A conservative interval prototype is tested on a known chain: the true intermediate state remains inside every computed interval.

The [reproduction commands](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/README.md) and [program for the six figures](https://github.com/magin67/pmg-notes/blob/v5/checks/isomer-spectra/draw_boundary_response.py) are in the same directory. Decimal numbers, plotted exponential values, and logarithms are used only for illustration. Finite enumerations check the implementation; theorems for arbitrary length follow from primitivity, the proved decoder, and bounds (18), (20), and (25). The ordinary resistance recurrence is proved by series and parallel reduction; the dynamic representation follows from a matrix integral.

| Statement | Status |
| --- | --- |
| Three exact entries of $\mathbf K_B$ determine the marked chain | Proved for the chosen class |
| These entries can be obtained from dynamics on the original graph | Proved for the specified model with unit heat capacities and thermal conductances |
| Ordinary resistance of the chosen terminal edge determines the turns | No: proved to depend only on $N$ |
| The exact joint law of two root indicators determines the same chain | Proved corollary |
| No uniform positive error tolerance works for all lengths | Proved by an explicit family |
| A positive sufficient accuracy exists under the bound $N\le M$ | A crude bound is proved |
| Better error bounds and an efficient reconstruction algorithm with noise | Remain research problems |
| Minimality of three data values; other cores, seams, weights, and closures | Not established here |
| Recovery from a single $P_G(1)$ or a single $\chi_G$ | Remains a separate open question |

The response matrix retains the boundary marking and additional information absent from a single spectral polynomial. The identification proved here therefore does not automatically solve recognition of a graph from its spectrum. Nor does it establish the practical accuracy of a particular measurement apparatus. Optimal use of complete time records, unknown heat capacities, and other physical models remain separate problems.

## Sources and related notes

1. P. Chebotarev, E. Shamis. *Matrix-Forest Theorems*. Manuscript, 1994–1997, [arXiv:math/0602575](https://arxiv.org/abs/math/0602575), Theorems 5–6. Forest interpretations of the determinant and cofactors of $\mathbf I+\mathbf L$.
2. L. Avena, A. Gaudillière. *Random spanning forests, Markov matrix spectra and well distributed points*. [arXiv:1310.1723v4](https://arxiv.org/abs/1310.1723v4), 2016, Lemma 3.3 and Theorem 3.4. Stopped walks and the determinantal law of roots; the generator has the opposite sign to the positive Laplacian used here.
3. J. Boyer, J. J. Garzella, F. Guevara Vasquez. *On the solvability of the discrete conductivity and Schrödinger inverse problems*. [arXiv:1510.02848](https://arxiv.org/abs/1510.02848), 2015. Context for inverse boundary problems for a Laplacian with a diagonal perturbation; their assumptions and unknowns differ from our chain assembly problem.

Matrix-forest identities, the integral representation of the resolvent through the matrix exponential, probabilistic representations, the Schur complement, and matrix inversion estimates are classical tools. The probabilistic version of the dynamic integral appears in [2, Lemma 3.3]; a direct matrix derivation is also given here. The specific conclusions of this note concern the chosen SLR transitions: recovery of the integer scale, application of the decoder to the response, and quantitative attenuation of distant differences. The ordinary terminal resistance recurrence follows from standard circuit rules. Having a proof in the library does not by itself establish scientific priority.

Foundations: [[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State|Rooted Forests and Decoding the Boundary State]], [[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains|SLR Codes of Hexagonal Chains]], [[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary|Spectral Transfer to a New Boundary]], [[en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data|From the Forest Passport to Spectral Boundary Data]]. Thematic entry points: [[en/Graph Transformations and Gluing/Graph Transformations and Gluing|Graph Transformations and Gluing]]; [[en/Invariants, Decompositions, and Spectra/Invariants, Decompositions, and Spectra|Invariants, Decompositions, and Spectra]].
