---
title: Electrometry
date: 2026-11-13
updated: 2026-11-13
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: electrometry-series-navigation
lang: en
order: 0
description: "Four notes connecting field measurements with resistance geometry: measured quantities, the geometry of pairwise data, sensitivity of the medium, and reconstruction under prescribed constraints."
tags:
  - resistances
  - variations
  - reconstruction
  - spectra
---

Electrometry investigates a conducting medium through currents and voltages at its surface. For PMG, it connects the resistance geometry of a graph to actual measurements: what an inner product means, how an internal coupling affects electrode response, and what is required for the inverse step.

Four notes lead from the measurement configuration to a reconstruction algorithm. The series contains exact results, analysis of real pairwise data, and computational examples. There is no complete, validated method of soil reconstruction yet; the scope of each result is stated in its note.

## Contents and reading order

| Order | Note | Main question |
| ---: | --- | --- |
| 1 | [[What Electrometry Measures]] | What does a four-electrode experiment determine, what remains undetermined, and how do remote electrodes help? |
| 2 | [[Properties of Resistances in a Continuous Medium]] | How does measurement-patch geometry appear in pairwise values, and can fewer measurements suffice? |
| 3 | [[Resistance Variations in Graphs and Continuous Media]] | How do squared inner products relate to electric fields and quadric connectivity? |
| 4 | [[Reconstructing Couplings with a Prescribed Neighbor Structure]] | Which assumptions permit reconstruction of internal couplings, and how can stability be checked? |

For a first reading, follow the table order. The main connection to PMG variation formulas is developed in [[Resistance Variations in Graphs and Continuous Media]]. The formulation and example of a computational algorithm are collected in [[Reconstructing Couplings with a Prescribed Neighbor Structure]].

## What the series establishes

**Which data are available.** An instrument reading $T$, a network effective resistance $R$, and a pairwise potential coefficient $Z$ have different definitions. For 16 electrodes, the complete pairwise table contains 120 values, whereas experiments on four distinct electrodes within the same grid determine only 104 independent linear combinations of an arbitrary table. Remote electrodes permit estimation of $Z$ using additional assumptions about distant contributions.

**How data geometry differs from information about the medium.** In a homogeneous half-space, $Z$ is inversely proportional to distance. After entrywise transformation $1/Z^2$ and double centering, a planar configuration is described by two geometric modes. Heterogeneity and errors can affect every mode. For the real $4\times4$ patch, the grid reconstructed from two modes has a root-mean-square deviation of about $0.23$ grid spacings after alignment.

**How PMG variation formulas connect to fields.** A squared potential drop on an edge corresponds to a squared potential gradient within the medium. Inverting the complete effective-resistance table determines an equivalent network on the electrodes. Choosing an internal realization of that network requires additional information.

**How assumptions enter the calculation.** The neighbor structure specifies allowed couplings; layers and known regions reduce the number of parameters; regularization expresses preferences among admissible models. In the model $4\times4\times4$ network, a layered description reduces 144 unknown couplings to four parameters. The example shows both successful reconstruction from exact data and sensitivity to noise.

## Origin and status of results

| Result | Source or derivation | Role in PMG | Novelty status |
| --- | --- | --- | --- |
| Ambiguity of four-point data | Polarization and KVP; proof in [[What Electrometry Measures]] | Separates observable combinations from vertex additions | Algebraic result; no priority claimed |
| Triangular compensation of distant contributions | Robain et al., 1999; residual estimate derived in [[What Electrometry Measures]] | Connects the measurement configuration to the pairwise coefficient | Known geometry; no priority claimed for the estimate |
| Two geometric modes | Distance-matrix theory; references and verification in [[Properties of Resistances in a Continuous Medium]] | Explains a simple representation of a homogeneous table | Application of an established construction |
| Variations of fields and effective couplings | Inverse-operator differentiation and Kron reduction; derivations in [[Resistance Variations in Graphs and Continuous Media]] | Relates medium sensitivity to quadric connectivity | Established constructions in PMG notation |
| Reconstruction on a prescribed grid | Jacobian and regularized least squares; [[Reconstructing Couplings with a Prescribed Neighbor Structure]] | Incorporates admissible coupling changes | Application of established methods; model verification |

## Open questions

- How can errors in real pairwise measurements, including remote-electrode effects, be estimated?
- Which spectral features are robust to those errors and related to heterogeneity?
- Which medium parameters can be distinguished on the chosen patch, and to what accuracy?
- How can a smaller measurement set preserve the required information about the data or medium parameters?

These questions are related but require different validation criteria. Exact reproduction of a measured table alone does not confirm the reconstructed internal structure.

## Related material

- [[Effective Resistance and Graph Geometry]] and [[Inner Product of Graph Vectors]]: resistances and the four-resistance formula.
- [[Applications of KVP Decomposition - Electrometry and Pair Data Analysis]]: undetermined vertex additions.
- [[Selected Vertices and the Dirichlet Problem]] and [[One Resistance and Quadric Connectivity]]: electrical response on selected vertices and inverse variations.
- [[Variations with Conductance Constraints]] and [[An Algorithm for Variations with Conductance Constraints]]: the general reconstruction problem with forbidden and fixed couplings.

Real pairwise data accompany [[Properties of Resistances in a Continuous Medium]]. Scripts and tables for the model examples are provided in [[Resistance Variations in Graphs and Continuous Media]] and [[Reconstructing Couplings with a Prescribed Neighbor Structure]].
