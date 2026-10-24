---
title: One-Way Resistance and Hitting Times
date: 2026-10-24
updated: 2026-10-24
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: one-way-resistance-and-hitting-times
lang: en
description: One-way resistance defined by a form potential, its matrix properties and relation to pair resistance and circulation, followed by the first-hitting-time interpretation.
order: 6
source_revision: 3
---

A balanced graph's metric can begin with a form that distinguishes the initial and target vertices. Its normalized potential gives the one-way resistance $r_{ij}$. Opposite values sum to the pair resistance; differences between sums around opposite triangular traversals give circulation potentials. These definitions and properties belong to the algebra of forms and matrices. Geometry, electrical networks, and Markov chains provide interpretations; the definitions themselves require no time variable.

The algebraic foundation is [[Balanced Variations]]: a bilinear form potential is computed using the inverse reduced Laplacian. Here we introduce its directional meaning. Geometric and electrical interpretations, together with three-vertex resistance, are treated in [[Resistance Geometry and Circulation]].

## The one-way resistance form

Let $G$ be a connected loopless balanced graph on $n\ge2$ vertices, with weights $f_{ij}\ge0$. Use the outgoing Laplacian:

$$
d_i=\sum_jf_{ij},\qquad L_{ii}=d_i,\qquad L_{ij}=-f_{ij}\quad(i\ne j)
$$

Balance means $\mathbf L\mathbf1=0$ and $\mathbf1^{\mathsf T}\mathbf L=0$. Under these conditions, connectedness is equivalent to strong connectedness. The polyform $M=\exp L$ has positive spanning-tree coefficient $\tau(M)=\tau(G)$. The exponential uses polyform multiplication, as in [[The Laplacian Exponential of a Balanced Graph]].

Abbreviate the normalized potential by

$$
P_M(F)=\frac{\tau(MF)}{\tau(M)}
$$

This is the potential ratio in the [[Core specification#Potential and the metric identity|PMG specification]]. For a general form it may have either sign. The unnormalized potential is $u_M(F)=\tau(M)P_M(F)$.

Choose the centroid $h$ and centered vectors $x_i$:

$$
h=\frac1n\sum_{k=1}^n a_k,\qquad x_i=a_i-h,\qquad \sum_i x_i=0
$$

> [!info] One-way resistance
> **Definition.** For an ordered vertex pair, set
>
> $$
> \Phi_{ij}=[a_j-h,a_j-a_i]=[x_j,x_j-x_i],\qquad
> \boxed{r_{ij}=P_M(\Phi_{ij})}
> \tag{1}
> $$
>
> “One-way resistance” here means precisely normalization (1). The indices specify direction from $i$ to $j$; the form's first argument refers to the target vertex.

The form is defined for every pair, whether or not an arc exists. It vanishes for $i=j$. The centroid choice is essential: replacing $h$ arbitrarily changes individual $r_{ij}$. The centroid gives a canonical choice treating all vertices equally.

### Computation using the Green matrix

Set $\mathbf{Gr}=\mathbf L^+$. For a connected balanced graph it inverts $\mathbf L$ on zero-sum columns and annihilates constant columns:

$$
\mathbf L\mathbf{Gr}=\mathbf{Gr}\mathbf L=\mathbf J,
\qquad \mathbf J=\mathbf I-\frac1n\mathbf1\mathbf1^{\mathsf T},
\qquad \mathbf{Gr}\mathbf1=0,\quad\mathbf1^{\mathsf T}\mathbf{Gr}=0
$$

The [[Balanced Variations#A matrix check and argument order|determinant formula for the potential]] gives, for affine vectors with coordinate columns $\mathbf u,\mathbf v$,

$$
P_M([u,v])=u^{\mathrm{out}}\cdot v^{\mathrm{in}}
=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u
$$

The pairing's first argument has the source role ($\mathrm{out}$), and its second the receiver role ($\mathrm{in}$). These roles and their coordinates are defined in [[The Gram Matrix and Directional Coordinates of a Balanced Graph#Sources and receivers|the directional pairing section]]. Argument order matters. Substituting $u=x_j$, $v=x_j-x_i$ gives

$$
\boxed{r_{ij}=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}}
\tag{2}
$$

With roles explicit, the same definition is

$$
r_{ij}=x_j^{\mathrm{out}}\cdot
\bigl(x_j^{\mathrm{in}}-x_i^{\mathrm{in}}\bigr)
$$

The pair direction $i\to j$ and the roles of the form arguments are different conventions: the first argument here is the vector to target $j$ in the source role. One-way resistance direction therefore cannot be inferred merely from vertex order in a pairing.

> [!note]- From the reduced Laplacian to the Green matrix
> **Proof.** Use basis $b_k=a_k-a_n$, $k<n$, and the matrix $\mathbf B$ of its coordinate columns. Then $\mathbf L=\mathbf B\mathbf C\mathbf B^{\mathsf T}$, where $\mathbf C=\mathbf L_{\widehat n,\widehat n}$. Write $\mathbf u=\mathbf B\widehat{\mathbf u}$ and $\mathbf v=\mathbf B\widehat{\mathbf v}$. For $\boldsymbol\varphi=\mathbf{Gr}\mathbf u$, the equation $\mathbf L\boldsymbol\varphi=\mathbf u$ gives $\mathbf C\mathbf B^{\mathsf T}\boldsymbol\varphi=\widehat{\mathbf u}$. Hence
>
> $$
> \mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u
> =\widehat{\mathbf v}^{\mathsf T}\mathbf C^{-1}\widehat{\mathbf u}
> $$
>
> The right side is the normalized potential from [[Balanced Variations]]. $\square$

## Pair resistance and circulation

Bilinearity gives the form identity

$$
\Phi_{ij}+\Phi_{ji}=[x_j-x_i]^2=[(a_i a_j)]^2
$$

The resistance norm of a pair vector is therefore

$$
\boxed{R_{ij}=P_M([(a_i a_j)]^2)=r_{ij}+r_{ji}}
\tag{3}
$$

The total resistance is symmetric in the vertices. Its Euclidean realization with side length $\sqrt{R_{ij}}$ is justified in [[Resistance Geometry and Circulation#The Euclidean part of the metric|the geometry section]].

For three vertices, write $w_{ijk}=w(a_i a_j a_k)$ as in [[The Circulation Form]]. Expansion gives another identity:

$$
w_{ijk}
=\Phi_{ij}+\Phi_{jk}+\Phi_{ki}-\Phi_{ik}-\Phi_{kj}-\Phi_{ji}
$$

Define the **circulation norm**, the normalized circulation-form potential, by $\chi_{ijk}=P_M(w_{ijk})$. Then

$$
\boxed{\chi_{ijk}=r_{ij}+r_{jk}+r_{ki}-r_{ik}-r_{kj}-r_{ji}}
\tag{4}
$$

It compares sums of one-way resistances along the two orientations of a closed traversal. This is a signed form norm in the PMG convention, without a nonnegativity requirement. Reversing vertex order reverses its sign. The corresponding arcs need not exist: forms are defined for all pairs and triples.

## The one-way resistance matrix

Write $\mathbf r=(r_{ij})$, $q_i=\mathrm{Gr}_{ii}$, and $\mathbf q=(q_1,\ldots,q_n)^{\mathsf T}$. Equation (2) gives

$$
\mathbf r=\mathbf1\mathbf q^{\mathsf T}-\mathbf{Gr},\qquad
\mathbf L\mathbf r=-\mathbf J
$$

Each column can therefore be computed directly from a reduced Laplacian:

$$
\boxed{\mathbf L_{\widehat j,\widehat j}\,\mathbf r_{\widehat j,j}=\frac1n\mathbf1},
\qquad r_{jj}=0
\tag{5}
$$

Row and column $j$ are deleted. The factor $1/n$ follows algebraically from the centroid normalization of $\mathbf J$.

The main properties of $\mathbf r$ are:

- $r_{ii}=0$ and $r_{ij}>0$ for $i\ne j$.
- The directed triangle inequality holds: $r_{ik}\le r_{ij}+r_{jk}$.
- Row sums agree, while column sums generally differ:

$$
\sum_jr_{ij}=\operatorname{tr}\mathbf{Gr},\qquad
\sum_ir_{ij}=nq_j
$$

Thus $\mathbf r$ is neither skew-symmetric nor generally symmetric. It is itself balanced only when all $q_i$ agree. Adding opposite directed triangle inequalities gives the triangle inequality for $R$.

> [!note]- Algebraic positivity and the triangle inequality
> **Proof.** If $y_j=0$ and $(\mathbf L\mathbf y)_i\ge0$ for $i\ne j$, then $y_i\ge0$. Otherwise, at a negative minimum, every $f_{ik}(y_i-y_k)$ is nonpositive. Their nonnegative sum forces every outgoing neighbor to share the minimum. Strong connectedness propagates it to $j$, contradicting $y_j=0$.
>
> Applying this argument to (5) gives $r_{ij}\ge0$. A zero value for $i\ne j$ would give $(\mathbf L\mathbf r_{\cdot j})_i\le0$, contradicting the right side $1/n>0$.
>
> For fixed $j,k$, set $y_i=r_{ij}+r_{jk}-r_{ik}$. Then $y_j=0$ and $\mathbf L\mathbf y=\mathbf e_k-\mathbf e_j$, where $\mathbf e_k$ is coordinate column $k$. Away from $j$, the right side is nonnegative, hence $y_i\ge0$, proving the triangle inequality. The sum formulas follow from (2) and the zero sums of $\mathbf{Gr}$. $\square$

The full one-way resistance matrix determines the original balanced graph, including directions and weight scale:

$$
\boxed{\mathbf{Gr}=-\mathbf J\mathbf r},\qquad
\mathbf L=\mathbf{Gr}^{+}
\tag{6}
$$

It is therefore another representation of the same algebraic data. Pairwise sums alone generally lose directional information.

## Why an undirected graph can have unequal one-way resistances

Put $q_i=P_M([a_i-h]^2)=\mathrm{Gr}_{ii}$. In an undirected graph, $\mathbf{Gr}$ is symmetric and

$$
r_{ij}=\frac{R_{ij}+q_j-q_i}{2},\qquad
r_{ji}=\frac{R_{ij}+q_i-q_j}{2}
\tag{7}
$$

In resistance geometry, $q_i$ is the squared distance from vertex $i$ to the centroid. Different positions relative to that centroid divide the total resistance into unequal shares.

Symmetry of the potential means $P_M([u,v])=P_M([v,u])$. But $\Phi_{ij}$ and $\Phi_{ji}$ are not obtained merely by exchanging arguments: reversing the pair also changes the target's centered vector. Equation (7) therefore does not contradict metric symmetry.

### Example: a three-vertex path

Take the undirected path with unit edges $ab$ and $bc$. In the order $a,b,c$, pseudoinversion and (2) give

$$
\mathbf{Gr}=\frac19
\begin{pmatrix}
5&-1&-4\\
-1&2&-1\\
-4&-1&5
\end{pmatrix},\qquad
\mathbf r=\frac13
\begin{pmatrix}
0&1&3\\
2&0&2\\
3&1&0
\end{pmatrix}
$$

Thus $r_{ab}=1/3$, $r_{ba}=2/3$, while $R_{ab}=1$. For the triple,

$$
\chi_{abc}=\frac{1+2+3-3-1-2}{3}=0
$$

Every undirected graph satisfies $r_{ij}-r_{ji}=q_j-q_i$. These differences cancel around a closed traversal. **One-way resistance can be asymmetric without circulation; circulation is detected by comparing closed sums.**

## Comparison with another directed definition

Balaji, Bapat, and Goel [3, Definition 1] define directed resistance as $\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}$. To retain our rule of adding two directions, denote half their quantity by

$$
\widetilde r_{ij}=\frac{\mathrm{Gr}_{ii}+\mathrm{Gr}_{jj}-2\mathrm{Gr}_{ij}}2
=r_{ij}+\frac{q_i-q_j}{2}
\tag{8}
$$

Then $R_{ij}=\widetilde r_{ij}+\widetilde r_{ji}$. In an undirected graph, both shares equal $R_{ij}/2$. In a general balanced graph,

$$
\widetilde r_{ij}-\widetilde r_{ji}=\mathrm{Gr}_{ji}-\mathrm{Gr}_{ij},
\qquad
\sum_j\widetilde r_{ij}=\sum_j\widetilde r_{ji}
=\frac{nq_i+\operatorname{tr}\mathbf{Gr}}2
$$

The matrix $\widetilde{\mathbf r}$ is balanced, and its asymmetry isolates the skew-symmetric Green part. Our $r$ is directly defined by the single form $\Phi_{ij}$ tied to the centroid and target.

The correction in (8) cancels on every closed traversal. Replacing $r$ by $\widetilde r$ therefore preserves both (3) and (4). These are two consistent allocations of total resistance between directions; circulation is independent of that choice. Neither share means that ordinary two-terminal resistance changes when current is reversed.

The [[The Gram Matrix and Directional Coordinates of a Balanced Graph#The canonical Gram matrix of local vertices|canonical Gram matrix]] relates both definitions to vertex pairings. For $g_{ij}=a_i^{\mathrm{out}}\cdot a_j^{\mathrm{in}}=\mathrm{Gr}_{ji}-(q_i+q_j)/2$,

$$
\begin{aligned}
r_{ij}&=-g_{ji}+\frac{q_j-q_i}{2}\\
\widetilde r_{ij}&=-g_{ji}=-a_j^{\mathrm{out}}\cdot a_i^{\mathrm{in}}
\end{aligned}
$$

The indices $ji$ follow from pairing order. The expression for $r_{ij}$ also retains the centroid-position correction. These identities do not alter definitions (1) and (8).

## Markov interpretation

Now interpret $f_{ij}$ as transition rates and consider the continuous-time walk with generator $-\mathbf L$. At $i$, it waits an exponential time of mean $1/d_i$, then selects $k$ with probability $f_{ik}/d_i$. Balance makes the stationary distribution uniform, with probabilities $1/n$.

**Definition.** Let $H_{ij}$ be the mean first hitting time of $j$ starting at $i$. Set $H_{jj}=0$; return time after leaving $j$ is a different quantity. Call $\mathbf H=(H_{ij})$ the **mean first hitting-time matrix**. It refers to the specified random process.

For fixed target $j$, conditioning on the first transition gives [1, Theorem 2.3]

$$
H_{ij}=\frac1{d_i}+\sum_k\frac{f_{ik}}{d_i}H_{kj}\quad(i\ne j),
\qquad H_{jj}=0
$$

The entire column is therefore obtained from one linear system:

$$
\boxed{\mathbf L_{\widehat j,\widehat j}\,\mathbf H_{\widehat j,j}=\mathbf1}
\tag{9}
$$

The target's row and column are deleted, and the right side is a column of $n-1$ ones. The reduced Laplacian is invertible, so the solution is unique. Repeating for every target computes $\mathbf H$ directly from graph weights.

> [!info] Potential and mean hitting time
> **Theorem.** For this continuous-time walk,
>
> $$
> \boxed{H_{ij}=nr_{ij}=nP_M(\Phi_{ij})}
> \tag{10}
> $$
>
> A form whose normalized potential equals $H_{ij}$ itself is therefore
>
> $$
> n\Phi_{ij}=\sum_{k=1}^n[a_j-a_k,a_j-a_i]
> $$

> [!note]- Proof
> **Proof.** Multiplying system (5) for $\mathbf r_{\widehat j,j}$ by $n$ gives (9). Both have unique solutions and zero diagonal entries, hence $H_{ij}=nr_{ij}$. Linearity of the potential and $n(a_j-h)=\sum_k(a_j-a_k)$ yield the expression using $n\Phi_{ij}$. $\square$

Resistance was defined and computed before the process was introduced. Equation (10) gives its probabilistic meaning for these rates. The factor $n$ relates normalizations; dividing a time matrix by $n$ is not the definition of resistance. The algebraic construction itself contains no time.

**Remark.** The number of transitions before hitting a target differs from continuous time. For its expectation, the right side of (9) becomes $\mathbf d_{\widehat j}$. These two models must not be mixed.

In the same interpretation,

$$
nR_{ij}=H_{ij}+H_{ji},\qquad
n\chi_{ijk}=H_{ij}+H_{jk}+H_{ki}-H_{ik}-H_{kj}-H_{ji}
$$

The first quantity is the mean time to reach $j$ from $i$ and then return. The second compares sequential target traversals $i\to j\to k\to i$ and $i\to k\to j\to i$. Each stage ends on first reaching its next target; intermediate visits to other vertices are allowed. Cyclic sums and nonreversibility are studied in [2, §12].

For the path example, $r_{ab}=1/3$ and $r_{ba}=2/3$ correspond to $H_{ab}=1$ and $H_{ba}=2$. The unequal times interpret the resistance asymmetry already computed algebraically.

## Sources and connections

The potential formulas are derived in PMG algebra. The time relation follows independently from the hitting-time system. Rational weighted examples also checked the potential of $\Phi_{ij}$ through the exterior exponential, the hitting-time solution, and cyclic identities. These computations supplement the proofs.

1. N. Berestycki, P. Sousi. [Applied Probability](https://www.statslab.cam.ac.uk/~ps422/notes-new2015.pdf), 2015. §2.2, Theorem 2.3: continuous-time hitting equations; Remark 2.4: the distinction from transition counts.
2. P. G. Doyle, J. Steiner. [Commuting time geometry of ergodic Markov chains](https://arxiv.org/abs/1107.2612). Version 2, 2017. Euclidean commute-time geometry; §12: cyclic sums and reversibility.
3. R. Balaji, R. B. Bapat, S. Goel. [Resistance matrices of balanced directed graphs](https://arxiv.org/abs/1906.01165). *Linear and Multilinear Algebra* **70** (2022), 787-808. [DOI: 10.1080/03081087.2020.1748850](https://doi.org/10.1080/03081087.2020.1748850). An alternative directed resistance definition with a normalization different from (1).

Related notes: [[Balanced Variations]], [[The Circulation Form]], [[Resistance Geometry and Circulation]], [[The Gram Matrix and Directional Coordinates of a Balanced Graph]].
