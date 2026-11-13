---
title: Resistance Variations in Graphs and Continuous Media
date: 2026-11-13
updated: 2026-11-13
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-variations-in-graphs-and-continuous-media
lang: en
order: 3
description: "Connecting PMG variation formulas with continuum sensitivity: potential drops and gradients, local heterogeneity, the effective electrode Laplacian, and quadric connectivity."
---

In a graph, changing one coupling affects resistances through squared inner products. In a continuous medium, the effect of a local conductivity change is expressed through electric fields. How are these formulas related? Can the inverse PMG formula, quadric connectivity, be used to recover changes within the medium?

Graph sensitivity is determined by the potential drop on the changing coupling; continuum sensitivity is determined by the field in the changing volume. Both formulas follow from the same rule for differentiating an inverse operator. Given the complete effective-resistance table between electrodes, the inverse formula determines an equivalent network on those electrodes. Recovering internal couplings additionally requires specifying the structure of the medium.

The symbols $T$, $R$, and $Z$ retain their meanings from [[What Electrometry Measures]]: $T$ is four-electrode transfer resistance, $R$ is effective resistance between two network terminals, and $Z$ is a pairwise potential coefficient of the continuous medium. [[Properties of Resistances in a Continuous Medium]] poses the sufficient-measurement problem. This note examines the mechanism of sensitivity.

## A coupling variation as a change in field energy

The initial graph is finite, connected, and undirected. Conductances $c_{kl}$ are nonnegative; the small changes considered preserve connectedness. Write $\mathbf L$ for the Laplacian matrix and $\mathbf{Gr}=\mathbf L^+$ for the Green matrix. The symbol $d$ denotes a differential; $\Delta$ denotes a finite increment. An equality of differentials gives only the first-order part of a finite change.

Let $\mathbf e_a$ have value one at $a$ and zero elsewhere. Introduce the current vector $\mathbf b_{ab}=\mathbf e_a-\mathbf e_b$. For unit current through $a,b$, the centered potentials are $\mathbf u_{ab}=\mathbf{Gr}\mathbf b_{ab}$. Then

$$
T_{ab,mn}=\mathbf b_{mn}^{\mathsf T}\mathbf{Gr}\mathbf b_{ab},
\qquad R_{ab}=T_{ab,ab}
$$

The sign of $\mathbf b_{ab}$ is opposite to the coordinates of $(ab)=b-a$. In an inner product of two pairs, the two signs cancel.

> [!info] Common basis of the variation formulas
> **Proposition.** On the space of zero-sum vectors,
>
> $$
> \boxed{d\mathbf{Gr}=-\mathbf{Gr}(d\mathbf L)\mathbf{Gr}}
> $$
>
> Consequently, for fixed current and sensing pairs,
>
> $$
> dT_{ab,mn}=-\mathbf u_{mn}^{\mathsf T}(d\mathbf L)\mathbf u_{ab}
> $$

This is the differential of matrix inversion. Its connection with polyform variations is developed in [[One Changing Edge]] and [[One Resistance and Quadric Connectivity]].

> [!note]- Derivation through the inverse operator
> **Proof.** For a fixed vertex set, $\mathbf L\mathbf{Gr}=\mathbf J$, where $\mathbf J=\mathbf I-\mathbf1\mathbf1^{\mathsf T}/n$ is fixed. Differentiating and multiplying on the left by $\mathbf{Gr}$ gives the first identity, since all variations preserve zero row sums. Multiplication by the current vectors gives the second. $\square$

When conductances change,

$$
d\mathbf L=\sum_{k<l}dc_{kl}\,\mathbf b_{kl}\mathbf b_{kl}^{\mathsf T}
$$

Therefore,

$$
dT_{ab,mn}=-\sum_{k<l}dc_{kl}
\bigl(u_{ab}(k)-u_{ab}(l)\bigr)
\bigl(u_{mn}(k)-u_{mn}(l)\bigr)
$$

For each changing coupling, the potential drops from two current experiments are multiplied. When the pairs coincide, this becomes the square of one drop:

$$
\frac{\partial R_{ab}}{\partial c_{kl}}
=-\bigl(u_{ab}(k)-u_{ab}(l)\bigr)^2
=-\bigl((ab)\cdot(kl)\bigr)^2
$$

This gives the resistance inner product an electrical interpretation. If current through $a,b$ produces no voltage across $k,l$, the derivative of $R_{ab}$ with respect to that conductance is zero. A larger drop means greater sensitivity to an absolute conductance change.

## From edge drops to continuum gradients

For a precise comparison with a finite graph, consider a connected bounded conducting body $\Omega$ with a sufficiently regular boundary. The medium is isotropic; conductivity $\sigma(x)$ is bounded above and bounded away from zero. Disjoint electrodes of finite area lie on the surface. They are perfect conductors, so each electrode is equipotential. The rest of the surface is insulated. Geometry is fixed and the model has no contact resistance.

Total electrode currents are prescribed and sum to zero. This model gives finite voltages and resistances. The indices $a,b,m,n$ label electrodes. The function $u_{ab}(x)$ is the potential in the initial medium when unit current enters through $a$ and leaves through $b$.

> [!info] Sensitivity of a four-electrode measurement
> **Proposition.** With fixed currents and a conductivity variation $d\sigma(x)$,
>
> $$
> \boxed{
> dT_{ab,mn}=-\int_\Omega d\sigma(x)\,
> \nabla u_{ab}(x)\cdot\nabla u_{mn}(x)\,dx
> }
> \tag{1}
> $$
>
> When the current and sensing pairs coincide,
>
> $$
> dR_{ab}=-\int_\Omega d\sigma(x)\,|\nabla u_{ab}(x)|^2\,dx
> $$

The product of gradients is a standard sensitivity kernel in electrometry. For continuous current distributions and a unit homogeneous background, it appears, for example, in **Bisch, Hirvensalo, and Hyvönen [1], equation (2.3)**. The same variational argument is given below for the stated electrode model and an arbitrary positive background.

> [!note]- Derivation from the conductivity equation
> **Proof.** For a test function $v$ constant on each electrode, the weak equation is
>
> $$
> \int_\Omega\sigma\nabla u_{ab}\cdot\nabla v\,dx=v_a-v_b
> $$
>
> Here $v_i$ is its value on electrode $i$. Differentiating at fixed currents gives
>
> $$
> \int_\Omega\sigma\nabla(du_{ab})\cdot\nabla v\,dx
> =-\int_\Omega d\sigma\,\nabla u_{ab}\cdot\nabla v\,dx
> $$
>
> Take $v=u_{mn}$. By the weak equation for $u_{mn}$, the left side is $(du_{ab})_m-(du_{ab})_n=dT_{ab,mn}$, giving (1). When $m=a$, $n=b$, the two fields coincide. $\square$

In a graph, one coupling contributes $c_{kl}(u_k-u_l)(v_k-v_l)$ to the bilinear energy. In the medium, a volume contributes $\sigma\nabla u\cdot\nabla v\,dx$. In both cases the coefficient of this energy is differentiated. The integral formula is therefore the continuum counterpart of the graph variation.

Passing to a spatial grid does not mean setting $c=\sigma$. For example, a conducting element of length $\ell$ and cross-sectional area $A$ has conductance $c=\sigma A/\ell$. These geometric factors reconcile the edge sum with the integral.

If $d\sigma\ge0$, effective resistance does not increase to first order. For transfer resistance $T$, the sign depends on the relative directions of the two fields. The gradient inner product belongs to ordinary physical space, whereas $(ab)\cdot(kl)$ uses the graph's resistance metric.

## A local heterogeneity and the potential coefficient

Suppose the conductivity change is supported in a small region $V$ around an interior point $x_0$. If the background gradients vary little across $V$, equation (1) gives

$$
dT_{ab,mn}\approx-q\,
\nabla u_{ab}(x_0)\cdot\nabla u_{mn}(x_0),
\qquad q=\int_V d\sigma(x)\,dx
$$

Two different assumptions are used: the differential describes a weak conductivity change, while replacing the integral by a value at $x_0$ uses the small size of the region. Small size alone does not make an arbitrary conductivity contrast weak.

The coefficient $Z_{an}$ uses a different setting: a half-space, point sources, and current return and zero potential at infinity. Let $u_a(x)$ and $u_n(x)$ be the background potentials of unit sources at $a,n$. For a bounded perturbation supported away from the electrodes, the same reciprocity argument gives

$$
dZ_{an}=-\int_\Omega d\sigma(x)\,
\nabla u_a(x)\cdot\nabla u_n(x)\,dx
$$

For a homogeneous three-dimensional half-space with a flat surface and conductivity $\sigma_0$,

$$
u_a(x)=\frac1{2\pi\sigma_0|x-a|}
$$

Thus a small region gives the explicit geometric expression

$$
\boxed{
dZ_{an}\approx-\frac{q}{4\pi^2\sigma_0^2}
\frac{(x_0-a)\cdot(x_0-n)}{|x_0-a|^3|x_0-n|^3}
}
$$

This substitutes the half-space potential into the variation formula; it is not a separate sensitivity law. The numerator is the ordinary inner product of two spatial vectors. Its sign can change, so a positive conductivity change need not decrease every potential coefficient $Z_{an}$.

A single graph coupling selects one direction of potential drop. An isotropic conductivity change in a volume affects all spatial directions: $|\nabla u|^2$ is the sum of squared coordinate derivatives. A point approximation to a volume heterogeneity should therefore not automatically be identified with changing one graph edge.

## What remains after internal vertices are eliminated

Start with a network in which the internal change is easy to see.

Four vertices $a,b,c,d$ are accessible. Internal vertex $p$ is joined to $a,b$, and internal vertex $q$ to $c,d$. These four conductances are $1$. A bridge between $p,q$ has conductance $t>0$.

![[images/Internal coupling and electrode response.svg]]

*Left: the original network with two internal vertices. Right: its equivalent graph on four electrodes at $t=1$. Edge labels give conductances. Both graphs have the same effective resistances between electrodes.*

The original graph is a tree. Resistance between two vertices is therefore the sum of individual edge resistances along the connecting path:

$$
R_{ab}=R_{cd}=2,
\qquad R_{ac}=R_{ad}=R_{bc}=R_{bd}=2+\frac1t
$$

For current between $a,b$, the bridge carries no current, so changing $t$ does not affect $R_{ab}$. For current between $a,c$, the entire unit current crosses the bridge. Its voltage is $1/t$, and the derivative of $R_{ac}$ is $-1/t^2$. This directly applies the squared inner product.

The network on the right reproduces every resistance between electrodes, although it has no internal vertices $p,q$. To find its couplings and how they change with the bridge, internal potentials must be expressed through electrode potentials.

### The general elimination formula

In general, let $B$ be the accessible electrode vertices and $I$ the internal vertices. Internal currents are zero. For prescribed electrode potentials $\mathbf U$, the Dirichlet problem determines the internal potentials:

$$
\mathbf u_I=\mathbf B\mathbf U,
\qquad \mathbf B=-\mathbf L_{II}^{-1}\mathbf L_{IB}
$$

The influence matrix $\mathbf B$ and its geometric meaning are discussed in [[Selected Vertices and the Dirichlet Problem]]. Write the full extension of the potentials as

$$
\mathbf u=\mathbf P\mathbf U,
\qquad \mathbf P=\begin{pmatrix}\mathbf I_B\\\mathbf B\end{pmatrix}
$$

> [!info] Effective Laplacian on the electrodes
> **Definition.** The matrix taking electrode potentials to total currents is
>
> $$
> \mathbf L_{\partial}
> =\mathbf L_{BB}-\mathbf L_{BI}\mathbf L_{II}^{-1}\mathbf L_{IB}
> =\mathbf P^{\mathsf T}\mathbf L\mathbf P
> $$
>
> This is the Laplacian of an equivalent graph on $B$. Its couplings $c^\partial_{ij}=-(L_{\partial})_{ij}$ reproduce the original graph's electrical response at the accessible vertices.

This elimination is called Kron reduction. Preservation of effective resistances and variations of the Kron-reduced Laplacian are treated by **Dörfler and Bullo [2], Theorems III.8 and III.14**, in the open version of their paper.

> [!info] How an internal variation appears at the electrodes
> **Proposition.** For fixed sets $B,I$,
>
> $$
> \boxed{d\mathbf L_{\partial}=\mathbf P^{\mathsf T}(d\mathbf L)\mathbf P}
> \tag{2}
> $$
>
> In particular, changing one internal coupling $k,l$ gives
>
> $$
> d\mathbf L_{\partial}=dc_{kl}\,\mathbf w\mathbf w^{\mathsf T},
> \qquad \mathbf w=\mathbf P^{\mathsf T}\mathbf b_{kl}
> $$

> [!note]- Why the derivative of the extension drops out
> **Proof.** Both $\mathbf L$ and $\mathbf P$ vary in $\mathbf L_{\partial}=\mathbf P^{\mathsf T}\mathbf L\mathbf P$. However, the rows of $d\mathbf P$ on $B$ vanish, and the rows of $\mathbf L\mathbf P$ on $I$ vanish by the internal Kirchhoff equations. Thus both terms involving $d\mathbf P$ disappear. Substituting $d\mathbf L=dc_{kl}\mathbf b_{kl}\mathbf b_{kl}^{\mathsf T}$ gives the second formula. $\square$

The vector $\mathbf w$ usually has nonzero values at several electrodes. One internal coupling therefore changes several effective couplings at once. Its location is not retained as one distinguished edge of the equivalent graph.

## Quadric connectivity on the electrodes

Let $\mathbf R_{\partial}$ be the complete matrix of effective resistances between accessible vertices. It agrees with the corresponding table in the original graph. The usual PMG transformations apply to the equivalent network:

$$
\mathbf{Gr}_{\partial}
=-\frac12\mathbf J_B\mathbf R_{\partial}\mathbf J_B,
\qquad \mathbf L_{\partial}=\mathbf{Gr}_{\partial}^{+}
$$

Here $\mathbf J_B$ centers values on $B$. Differentiating the inverse gives

> [!info] Inverse variation of effective resistances
> **Proposition.** For a connected equivalent network,
>
> $$
> \boxed{
> d\mathbf L_{\partial}
> =\frac12\mathbf L_{\partial}(d\mathbf R_{\partial})\mathbf L_{\partial}
> }
> \tag{3}
> $$
>
> Varying one independent symmetric coordinate $R_{kl}=R_{lk}$ while fixing all others gives
>
> $$
> \frac{\partial(L_{\partial})_{ij}}{\partial R_{kl}}
> =\frac12\bigl((L_{\partial})_{ik}(L_{\partial})_{jl}
> +(L_{\partial})_{il}(L_{\partial})_{jk}\bigr)
> $$
>
> The right side is the quadric connectivity of the equivalent graph. The derivative of $c^\partial_{ij}$ has the opposite sign.

The proof and the mutual inverse property of the pairwise response matrices are given in [[One Resistance and Quadric Connectivity#Two matrices on the full set of pairs|the note on quadric connectivity]]. The same result is applied here to the graph on electrodes. Formula (3) determines its effective Laplacian. The internal Laplacian of the original network has more coordinates and is not directly recovered by this formula.

The independent pair coordinates in this formula are algebraic coordinates. Changing one resistance while fixing all others need not be realizable by an admissible change of a particular medium. For an actual perturbation, the full consistent matrix $d\mathbf R_{\partial}$ must be substituted.

A continuous medium with finite electrodes has the same kind of finite electrical response. In the stated electrode model, $\mathbf L_{\partial}$ maps electrode potentials to total currents. Symmetry, zero row sums, and Laplacian sign conditions follow from reciprocity, current conservation, and the maximum principle. Formula (3) therefore applies to this matrix as well, provided the complete table of corresponding effective resistances is available.

> [!note] Data required by the inverse formula
> Formula (3) uses $\mathbf R_{\partial}$, not the coefficient table $\mathbf Z$ or the matrix of $1/Z_{ij}^2$. Measurements on four distinct terminals alone may fail to determine all of $\mathbf R_{\partial}$; the ambiguity is described in [[What Electrometry Measures]]. An inversion formula cannot replace missing data.

## A second expression through continuum fields

The same variation of $\mathbf L_{\partial}$ can be computed directly from the conductivity change. This requires fields with prescribed electrode potentials.

Let $h_i(x)$ solve the initial problem with value $1$ on electrode $i$ and $0$ on all other electrodes; the boundary outside the electrodes is insulated. For arbitrary potentials $U_i$, the internal field is $u(x)=\sum_i U_i h_i(x)$. The functions $h_i$ play the role of columns of the extension matrix $\mathbf P$.

> [!info] Variation of the effective Laplacian through local conductivity
> **Proposition.** For finite perfectly conducting electrodes,
>
> $$
> (L_{\partial})_{ij}
> =\int_\Omega\sigma\,\nabla h_i\cdot\nabla h_j\,dx
> $$
>
> $$
> \boxed{
> d(L_{\partial})_{ij}
> =\int_\Omega d\sigma\,\nabla h_i\cdot\nabla h_j\,dx
> }
> \tag{4}
> $$

> [!note]- Derivation from energy at prescribed potentials
> **Proof.** Substituting $u=\sum_i U_i h_i$ into the energy gives $\mathbf U^{\mathsf T}\mathbf L_{\partial}\mathbf U=\int_\Omega\sigma|\nabla u|^2\,dx$. Polarization gives the first identity. Differentiation also produces integrals involving $dh_i$ and $dh_j$. These variations vanish on all electrodes. By the weak equations for the background fields $h_i,h_j$, both extra integrals vanish, leaving (4). $\square$

Thus (2) and (4) express the same construction: an internal energy change is transferred to the accessible electrodes through extension of potentials. A graph uses the matrix $\mathbf P$; a medium uses the functions $h_i$.

The sign difference from (1) comes from the prescribed data. At fixed currents, the inverse electrical response is differentiated, producing a minus sign. At fixed potentials, the energy operator itself is differentiated, giving a positive sign. Individual off-diagonal entries can still change in either direction because $\nabla h_i\cdot\nabla h_j$ need not have one sign throughout the medium.

Formulas (3) and (4) must give the same effective-Laplacian variation. The first computes it from resistance changes; the second from conductivity changes and background fields. This connects quadric connectivity with the continuum problem. Equation (4) is a direct sensitivity to $\sigma$, not an inverse formula that recovers $d\sigma$.

## Example - changes of effective couplings

For the illustrated network with bridge conductance $t$, eliminating $p,q$ gives

$$
c^\partial_{ab}=c^\partial_{cd}=\frac{t+2}{4(t+1)},
\qquad
c^\partial_{ac}=c^\partial_{ad}=c^\partial_{bc}=c^\partial_{bd}
=\frac{t}{4(t+1)}
$$

The values and derivatives at $t=1$ are:

| Pairs | $R$ | $dR/dt$ | $c^\partial$ | $dc^\partial/dt$ |
| --- | ---: | ---: | ---: | ---: |
| $ab,cd$ | $2$ | $0$ | $3/8$ | $-1/16$ |
| $ac,ad,bc,bd$ | $3$ | $-1$ | $1/8$ | $1/16$ |

Strengthening the internal bridge weakens the effective couplings $ab,cd$, although their effective resistances remain unchanged. The other effective couplings strengthen and their resistances decrease. There is no contradiction: several couplings of the equivalent graph change together.

> [!example] One variation computed in two ways
> In electrode order $a,b,c,d$, set $\mathbf v=(1,1,-1,-1)^{\mathsf T}$ at $t=1$. Extension of potentials gives $\mathbf w=\mathbf v/4$, so (2) yields
>
> $$
> d\mathbf L_{\partial}=\frac{dt}{16}\,\mathbf v\mathbf v^{\mathsf T}
> $$
>
> Substituting the resistance derivatives from the table into the quadric-connectivity formula (3) gives the same matrix.

The example was checked in exact symbolic arithmetic. Resistances were independently computed by solving the grounded Kirchhoff system, and the effective Laplacian by eliminating internal vertices. Direct derivatives, formulas (2)-(3), and mutual inversion of the full pairwise sensitivity matrices were compared.

The [verification script](<data/Verify variations.py>) and [value table](<data/Internal coupling variations.csv>) are attached. The script requires Python with SymPy. This is a model example, not an analysis of field measurements.

## What is required to recover the medium

The complete effective-resistance table determines $\mathbf L_{\partial}$ but does not select an internal realization. In the example, the same table is realized by a tree with internal vertices and by a complete graph on the electrodes alone. If the original network is known to have the illustrated structure, with its four outer conductances equal to $1$, one resistance determines the internal bridge:

$$
t=\frac1{R_{ac}-2},\qquad R_{ac}>2
$$

Knowing the structure reduced the problem to one unknown. Without that knowledge, the same table allows another internal realization.

A continuous medium requires an analogous specification: which distributions $\sigma(x)$ are admissible, and which changes must be distinguished? For prescribed regions or basis functions $\psi_\alpha$, one may write

$$
d\sigma(x)=\sum_\alpha d\theta_\alpha\,\psi_\alpha(x)
$$

Let $p$ index the chosen four-electrode experiments, $u_p$ be the field of the current pair, and $v_p$ the field of unit current through the sensing pair. Equation (1) then gives

$$
d\mathbf T=\mathbf K\,d\boldsymbol\theta,
\qquad
K_{p\alpha}=-\int_\Omega\psi_\alpha\,
\nabla u_p\cdot\nabla v_p\,dx
$$

The matrix $\mathbf K$ depends on the background medium, electrode geometry, and chosen parameters. Together with measurement errors, it determines whether parameter changes can be distinguished. Quadric connectivity transforms the full electrical response into effective couplings but does not replace analysis of $\mathbf K$.

Choosing a sufficient measurement set can therefore have a specific goal: preserve sensitivity to admissible changes in the medium. The spectral representation of the pairwise table and sensitivity to parameters answer different questions. [[Reconstructing Couplings with a Prescribed Neighbor Structure]] specifies admissible changes on a spatial grid, builds an algorithm, and examines its stability. The number of modes of the transformed table alone does not determine the number of distinguishable heterogeneities.

## Sources and status of results

- [[What Electrometry Measures]] - the distinction between $T$, $R$, and $Z$, and measurement limitations.
- [[One Changing Edge]] - direct resistance variation through an inner product.
- [[One Resistance and Quadric Connectivity]] - inverse variation and the precise scope of mutual inversion of pair matrices.
- [[Selected Vertices and the Dirichlet Problem]] - extension of potentials and the influence matrix.
- **[1]** Bisch J., Hirvensalo M., Hyvönen N. *Continuity of the Linearized Forward Map of Electrical Impedance Tomography from Square-Integrable Perturbations to Hilbert-Schmidt Operators*. [Open version, arXiv:2409.10671](https://arxiv.org/abs/2409.10671), 2024, §2, equation (2.3).
- **[2]** Dörfler F., Bullo F. *Kron Reduction of Graphs With Applications to Electrical Networks*. IEEE Transactions on Circuits and Systems I, 60(1), 2013, 150-163. [DOI](https://doi.org/10.1109/TCSI.2012.2215780), [open text](https://motion.me.ucsb.edu/pdf/2011d-db.pdf). Section III.C: resistances; III.D: sensitivity of the reduction.

Inverse-operator variations, integral sensitivity kernels, and Kron reduction are known constructions. They are related here to PMG variation formulas and quadric connectivity. Derivations use the stated models, and the example is verified in exact arithmetic.
