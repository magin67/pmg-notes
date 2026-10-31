---
title: PMG Terminology
date: 2026-10-09
updated: 2026-10-30
revision: 16
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-terminology
lang: en
description: "Terminology of the PMG core and published series: polyforms and metrics, forest and spectral parameters, boundary states and passports, groves and electrical response; Russian equivalents and usage conditions."
order: 2
---

This glossary records the terminology of the [[Core specification|core specification]], the [[PMG Introductory Series|introductory series]], and the published thematic series. Each entry gives the English term, its Russian equivalent, and a brief definition. Applicability conditions and fundamental identities of the core are specified in the core specification; definitions of extensions, proofs, and examples appear in the linked notes.

Russian version: [[ru/Основания/Терминология PMG|Терминология PMG]].

## Scope and terminology status

The main model is a finite connected undirected graph without loops, with positive conductances on existing edges. The algebraic definitions do not require a graph. The disconnected case is addressed in the specification. Terms for the balanced model appear in [[PMG terminology#Balanced graphs and directional metrics|Balanced graphs and directional metrics]]; symmetric formulas do not automatically extend to that model.

The tables use three status labels:

- **Standard:** the term has its usual mathematical meaning in the stated field.
- **Qualified:** the term is established, but the object, convention, or normalization requires clarification here.
- **PMG:** a term or specialized usage adopted in the project.

Terminology status does not describe the proof status of a claim. English names for PMG-specific constructions are editorial recommendations, not claims of established usage.

The project name remains **Polyform Metric Geometry (PMG)**.

## Collections and partitions

These conventions are used in the [[Partitions and the Combinatorial Potential of the Second Kind|combinatorial series]]; the compact notation for operations is recorded in the [[Core specification#Collections in combinatorial formulas|specification]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Numerical collection; multiset | Числовой набор | Qualified | A finite multiset $\mathbf x=[x_1,\ldots,x_m]$: order is immaterial, and repetitions are retained. The collection is bold, its elements are not. |
| Size; cardinality | Размер набора; мощность | Standard | $\#X$ counts the elements of a finite set or the occurrences in a collection. For $\mathbf x=[x_1,\ldots,x_m]$, one has $\#\mathbf x=m$. The term “length of a collection” is not used. |
| Weight of a numerical collection | Вес числового набора | Qualified | $w(\mathbf x)=x_1+\cdots+x_m$. Distinct from collection size and from the affine weight of an element of $V$. |
| Product of a collection | Произведение набора | PMG | $\mathbf x!=[x_i]!=x_1\cdots x_m$; the empty product equals $1$. Its argument is a collection, whereas $n!$ is the ordinary factorial of a number. The notation $[x_i!]!$ denotes the product of element factorials, not the factorial of their product. |
| Multiplicity of a value | Кратность значения | Standard | $\mu_j=\#\{i:x_i=j\}$ for each distinct value $j$ in the collection. The collection $\boldsymbol\mu=[\mu_j]_{j\in J}$ is indexed by the set $J$ of distinct values; equal multiplicities are retained. |
| Integer partition | Разбиение числа | Standard | A numerical collection of positive integers with prescribed weight $w$. Its elements are called parts. |
| Set partition; block; partition component | Разбиение множества; блок; компонента разбиения | Standard | A collection of nonempty pairwise disjoint subsets whose union is the original set. Blocks are unordered; their number is denoted by $m$. |
| Numerical type of a partition; block-size type | Числовой тип разбиения | Qualified | The collection of block sizes $[\#B_1,\ldots,\#B_m]$. Its size is the component count, and its weight is the size of the original set. Distinct from the grade type of a partition form. |

The notation $[x_i!]$ first constructs a new collection using the same indices as $[x_i]$, retaining every occurrence; the outer sign in $[x_i!]!$ then specifies its product. Numbers, collections, simplices, and forms are distinguished by their argument types, rather than by square brackets alone.

## Points, vectors, and exterior objects

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Basis vertex | Базовая вершина | PMG | An element $a_i$ of the fixed linearly independent basis of the formal space $V$. |
| Point | Точка | Qualified | An element $x=\sum_i x_i a_i$ with $\sum_i x_i=1$. Not every point is a basis vertex. |
| Affine weight | Аффинный вес | PMG | The value of the linear functional $\varepsilon(x)=\sum_i x_i$. It is neither an edge weight nor a physical mass. |
| Affine vector | Аффинный вектор | Qualified | An element $u\in W=\ker\varepsilon$. Within the core, “vector” may be used for brevity. |
| Vertex-pair vector | Вектор пары вершин | Qualified | The difference $a_{ij}=a_j-a_i=(ij)$. It is defined even without an edge; reversing the order changes its sign. |
| Space of affine vectors | Пространство аффинных векторов | Qualified | The $(n-1)$-dimensional subspace $W\subset V$ consisting of combinations with zero coefficient sum. |
| Exterior product; wedge product | Внешнее произведение | Standard | The product $XY$ in the exterior algebra, usually denoted by $X\wedge Y$. Exchanging homogeneous objects introduces a sign depending on their grades. |
| Exterior-algebra element | Внешний объект | Qualified | An element of $\Lambda^kV$ or $\Lambda^kW$. It may be a linear combination of exterior products. |
| Decomposable exterior element | Простой внешний объект | Standard | An object expressible as one exterior product. The Russian adjective “простой” means decomposable here. |
| Grade | Грейд | Qualified | The exterior degree $k$ of an object in $\Lambda^kV$. For a form, it is the common grade of its arguments. |
| Simplex | Симплекс | Qualified | The formal expression $[a_1\ldots a_k]=a_1\cdots a_k$. Its grade is $k$; the geometric dimension of a nondegenerate simplex is $k-1$. |
| Orientation | Ориентация | Standard | A choice of sign for an exterior object specified by the order of its generators. Exchanging two generators changes the sign. |

In the algebraic construction, $a_i$ does not denote a centered position vector of a Euclidean realization. Formal vertices are linearly independent; centered position vectors sum to zero.

## Boundaries and the boundary operator

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Boundary operator | Граничный оператор | Qualified | The linear operator $\partial$, with $\partial a_i=1$, $\partial1=0$, and the usual alternating vertex-deletion formula. This convention includes the scalar grade. |
| Simplex boundary | Граница симплекса | Qualified | The object $(a_1\ldots a_k)=\partial[a_1\ldots a_k]$, of grade $k-1$ when nonzero. |
| Boundary | Граница | Qualified | Any object in the image of $\partial$ in this algebra. In grade $k$, the space of boundaries is $\Lambda^kW$. |
| Space of boundaries | Пространство границ | Qualified | The space $\Lambda^kW$ in a fixed grade; it also equals the kernel of $\partial$ in that grade. Equality of kernel and image refers to this construction. |
| Boundary merging rule | Правило слияния | PMG | The product of simplex boundaries with exactly one shared basis vertex gives the boundary of the combined simplex, with the appropriate orientation sign. |
| Vanishing rule | Правило обнуления | PMG | The product of simplex boundaries with at least two shared basis vertices is zero. |

The merging and vanishing rules apply to simplex boundaries on basis vertices. For arbitrary linear combinations, the product is evaluated by bilinearity.

> [!note] Two meanings of “boundary”
> An algebraic boundary is an image of $\partial$. In a Dirichlet problem, “boundary vertices” means a selected vertex set on which values are prescribed. These are different notions. When both occur, use “algebraic boundary” and “boundary vertex set” or “selected vertex set” explicitly.

## Forms and polyforms

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Formal form | Форма | PMG | A formal symbol $[X,Y]$ subject to bilinearity, or a linear combination of such symbols of one grade. |
| Formal bilinear form | Билинейная форма в алгебре PMG | Qualified | The symbol $[X,Y]$ is bilinear in its exterior arguments. It is neither a number nor an already specified numerical bilinear function on $V$. |
| Quadratic form | Квадратичная форма | Qualified | The formal object $[X]^2=[X,X]$. Its numerical evaluation is defined separately. |
| Transpose of a form | Транспонирование формы | Qualified | The operation $[X,Y]^{\mathsf T}=[Y,X]$, extended linearly. |
| Polar form | Полярная форма | Qualified | The unnormalized sum $\{X,Y\}=[X,Y]+[Y,X]$. The definition includes no factor of $1/2$. |
| Skew-symmetric form | Антисимметричная форма | Qualified | A form $F$ satisfying $F^{\mathsf T}=-F$. Its evaluation under a symmetric metric is zero. A directional evaluation for a balanced graph can be nonzero. |
| Polyform in PMG | Полиформа | PMG | A finite linear combination of forms, possibly of different grades. After definition, “polyform” may be used. |
| Homogeneous polyform | Однородная полиформа | Qualified | A polyform of one grade. |
| Grade component | Грейд-компонента | Qualified | A homogeneous component $P_k$ of a specified polyform. “Грейд-полиформа” is an acceptable Russian synonym. |
| Polyform product | Произведение форм | PMG | The operation $[X,Y][A,B]=[XA,YB]$. It is commutative and differs from matrix multiplication. |
| Unit form | Единичная форма | PMG | The grade-$0$ form $e=[1,1]$, the identity for the product of forms. |
| Form on boundaries | Форма на границах | PMG | A form with arguments in $\Lambda^kW$. These forms constitute the subalgebra on which the core's metric evaluation is defined. |
| Nilpotency | Нильпотентность | Standard | A positive power of an element being zero. For example, $([v]^2)^2=0$ for a vector $v$, although the form of a nonzero vector is itself nonzero. |

In the electrical part of the introductory series, “the quadratic form of the Laplacian” also denotes the numerical function $\varphi\mapsto\varphi^{\mathsf T}\mathbf L\varphi$. When it appears alongside the formal polyform $L$, the representation must be specified.

## Structural identities and symmetric polyforms

Definitions follow [[Partition Forms and the Tetrahedron Identity]] and [[Symmetric Polyforms - Types and Normalizations]]. They belong to the formal algebra and require no choice of metric.

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Partition form | Форма разбиения | PMG | For a partition $\pi$ into blocks $B_1,\ldots,B_m$, this is $q_\pi=[(B_1)\cdots(B_m)]^2$. Its grade is $n-m$, where $n$ is the vertex count. A singleton block contributes the unit factor. |
| Structural identity | Структурное тождество | PMG | A linear relation between partition forms on a fixed vertex set that holds in the formal algebra. A numerical equality in one chosen metric does not by itself constitute such an identity. |
| Full type of a partition form | Полный тип формы разбиения | PMG | The collection of block-boundary grades $\lambda=[\#B_1-1,\ldots,\#B_m-1]$. With $r$ positive parts and $\ell$ zero parts, $m=r+\ell=n-k$, where $k$ is the sum of the parts. Zeros may be omitted for fixed $n$. A type refers to a partition and to a chosen representation of a sum. |
| Symmetric polyform; SPF | Симметрическая полиформа; СПФ | PMG | A polyform invariant under all permutations of a specified set of basis vertices. Vertex symmetry differs from symmetry of a form in its two arguments. |
| Symmetric sum of a given type | Симметрическая сумма заданного типа | PMG | $E_n[\lambda]$ is the sum of $q_\pi$ over all partitions of a specified set of $n$ vertices with full type $\lambda$. Each partition occurs once with coefficient $1$. |
| Principal symmetric polyform; principal SPF | Главная симметрическая полиформа; ГСПФ | PMG | $E_n[k]$ for $1\leqslant k\leqslant n-1$: the sum over one block of $k+1$ vertices, with all other blocks singletons. Grade $0$ is defined separately: $E_n[0^n]=e$. |
| Size of a polyform representation; representation size | Размер представления полиформы | PMG | The number of terms in a chosen expression as a sum of forms with coefficients. In the basic normalization, $\#E_n[\lambda]$ counts the indexing partitions. It is neither a vector-space dimension nor an invariant of the polyform. |

In a forest, the connected components determine the partition blocks. A component with $b$ vertices has $b-1$ edges, so its edge count equals its boundary grade. Several trees on the same block give the same partition form. Symmetric-sum size and forest count are therefore computed separately; see [[Combinatorial Potentials in Symmetric Polyforms]].

## Combinatorial potentials and forest coefficients

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Combinatorial potential of the second kind | Комбинаторный потенциал второго рода | PMG | $s_2(\mathbf x)$ counts partitions of a set of $w(\mathbf x)$ distinguishable elements into unordered blocks with positive sizes $\mathbf x$. This is the PMG name for that combinatorial number. [[Partitions and the Combinatorial Potential of the Second Kind]]. |
| Combinatorial potential of the first kind | Комбинаторный потенциал первого рода | PMG | $s_1(\mathbf k)=\frac{n!}{\prod_{j\ge1}j^{\mu_j}\mu_j!}$ counts permutations of $n=w(\mathbf k)$ distinguishable elements with cycle-length collection $\mathbf k$; $\mu_j$ is the multiplicity of length $j$. Distinct from the forest parameter $s_1^{\mathrm{for}}$. [[Cyclic Partitions and the Combinatorial Potential of the First Kind]]. |
| Potential of a mixed path-and-cycle state | Потенциал смешанного состояния из путей и циклов | PMG | $u(\lambda_k)=\frac{k!}{\prod_{j\ge1}j^{c_j}c_j!p_j!}$, where $c_j,p_j$ count cycles and nonempty directed paths with $j$ links, and $k=\sum_j j(c_j+p_j)$. Counts partitions of $k$ distinct link labels into cyclically and linearly ordered blocks, not graphs on a fixed vertex set. Isolated vertices are omitted from the reduced type. [[The Potential of Path-and-Cycle States]]. |
| External combinatorial potential | Внешний комбинаторный потенциал | PMG | $e_n(\mathbf x)=\binom{n}{w(\mathbf x)}s_2(\mathbf x)$ for $w(\mathbf x)\leqslant n$: choosing a subset of the prescribed size and a partition of that subset of the prescribed type. The indexed function $e_n$ differs from the unit form $e$. [[Combinatorial Potentials in Symmetric Polyforms]]. |
| Combinatorial forest coefficients $\operatorname{St}(k,m)$ | Комбинаторные лесные коэффициенты $\operatorname{St}(k,m)$ | PMG | The numbers $\operatorname{St}(k,m)$ count forests on $k$ labelled ordinary vertices and $m$ added unlabelled roots: each component has exactly one root, and no root is isolated. Here $m$ belongs to the auxiliary construction, rather than counting all components of the original graph on $n$ vertices. These numbers differ from $\tau(G)$ and ordinary Stirling numbers $S(k,m)$. [[Forest Coefficients and Abel Polynomials]]. |
| $r$-Stirling numbers of the second kind | $r$-числа Стирлинга второго рода | Standard | $\left\{\begin{smallmatrix}N\\K\end{smallmatrix}\right\}_r$ counts partitions of $N$ elements into $K$ nonempty blocks with $r$ specified distinct elements in different blocks. Here $N,K$ are full sizes; the shifted notation $c_r(w,m)$ means $N=w+r$, $K=m+r$. [[Falling Factorials, Rooted Forests, and Stirling Numbers]]. |

For $\mathbf x=[x_i]$ with positive integer parts, $w=w(\mathbf x)$, and multiplicity collection $\boldsymbol\mu=[\mu_j]_{j\in J}$, the formula is

$$
s_2(\mathbf x)=\frac{w!}{[x_i!]!\,[\mu_j!]!}
$$

A combinatorial potential counts partitions and uses no metric. The polyform potential $u_M(f)=\tau(Mf)$ is defined in a different sense, through the metric polyform. When applying $s_2$, specify whether its argument lists vertex-block sizes or parts of an auxiliary partition. For example, $\#E_5[2,1]=s_2([3,2])=10$, whereas the coefficient in $E_5[2,1]=3E_5[3]$ is $s_2([2,1])=3$. The corresponding forest count in $K_5$ is $30$.

The relation between forest coefficients and $r$-Stirling numbers is used here for specific PMG counts. A general classification of Stirling-number families belongs to a separate project on combinatorics and partition algebra.

## Partition toponomes and operations on types

Definitions and the scope of the operations are given in the [[en/Partition toponomes/Partition Toponomes|Partition Toponomes]] series. The names of PMG-specific constructions refer to the objects below; they do not define a general name for every reduction of a polyform.

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Positive type of a partition form | Положительный тип формы разбиения | PMG | The full type with zero parts omitted: $\lambda=(k_1,\ldots,k_r)$, $k_i\geqslant1$. For $k=w(\lambda)$ and known $n$, recover $m=n-k$ and $\ell=n-k-r$. The empty type is denoted by $1$ and corresponds to the unit form $e$. [[From Polyforms to Partitions]]. |
| Partition toponome; toponome of a chosen representation | Топоном разбиений; топоном выбранного представления | PMG | For an expression $\mathcal E=\sum_\pi c_\pi q_\pi$, this is $T_{\mathcal E}=\sum_\pi c_\pi\lambda(\pi)$. Vertex labels are forgotten, and contributions of identical positive types are collected. Structural identities need not be preserved; the toponome is not declared invariant under arbitrary changes of expression for the same polyform. [[Toponomes and Structural Identities]]. |
| Partial matching of components | Частичное сопоставление компонент | Standard | A set of pairs of occurrences of parts from two factors, with each occurrence belonging to at most one pair. Equal parts are temporarily distinguished; a coefficient counts matchings producing the same resulting type. [[The Second-Kind Algebra on Partitions]]. |
| The second-kind algebra on partitions | Алгебра второго рода на разбиениях | PMG | The real algebra of finite linear combinations of integer partitions with product $*$: matched parts add, unmatched parts remain unchanged, and all partial matchings are summed. The unit is the empty type $1$. “Second-kind” refers to the algebra; $(1)^k=\sum_{\lambda\vdash k}s_2(\lambda)\lambda$. It is isomorphic to the standard algebra of symmetric functions in the augmented monomial basis. |
| Color class | Цветовой класс | Standard | The set of vertices of one color in a proper coloring; it is an independent block. The weight type of color classes records the sums of vertex weights in each block. The sum of these types differs from the spanning-forest toponome. [[Graph Colorings and Partition Products]]. |
| Sum of partial gluings at chosen roots | Сумма частичных склеек по выбранным корням | PMG | A boundary realization of $*$: a root is chosen in advance in each nontrivial component, and the roots of each matched pair are identified without adding an edge. The sum ranges over matchings, not root choices. Each component belongs to at most one pair. [[Partition Products and Boundary Forms]]. |
| Coefficient table of a toponome | Коэффициентная таблица топонома | PMG | $\mathcal A_{\mathcal E}=(a_{k,r})$, where $a_{k,r}$ sums coefficients of types of weight $k$ with $r$ positive parts. Individual types within one cell are lost. Graph comparisons retain the vertex count $n$ separately; the data $(n,\mathcal A_G)$ do not in general determine a graph up to isomorphism. [[Coefficient Tables of Toponomes]]. |
| Coefficient triangle | Коэффициентный треугольник | PMG | A table layout with weight $k$ indexing columns and the number $r$ of nontrivial components indexing rows. For nonempty types on $n$ vertices, $r\leqslant k\leqslant n-r$; admissible row lengths decrease by two. The unit term is treated separately, and zero cells are left blank. A particular graph may fill only some admissible cells. |
| Vector normalization of a forest toponome | Векторная нормировка лесного топонома | PMG | Retains the weight $w(F)$ of each forest in the fixed forest representation. Collecting all types of the same grade gives $F_G(t)=\sum_g f_g t^g$. [[Vector and Vertex Normalizations of Toponomes]]. |
| Vertex, or rooted, normalization of a forest toponome | Вершинная, или корневая, нормировка лесного топонома | PMG | Multiplies $w(F)$ by $\prod_{C\in\pi(F)}\#C$, the number of choices of one root in each component. For type $\lambda=(k_i)$ this factor is written $h(\lambda)=\prod_i(k_i+1)$; the type function $h(\lambda)$ differs from the centroid $h$. [[Vector and Vertex Normalizations of Toponomes]]. |
| Laplacian polynomial | Лапласовский полином | Qualified | $P_G(t)=\det(I+t\mathbf L)=\sum_g p_g t^g$ in ascending-grade notation. Distinct from the ordinary forest polynomial $F_G$ and the characteristic polynomial $\chi_{\mathbf L}(x)=x^nP_G(-1/x)$. Its coefficients $p_g$ are rooted coefficients. [[Forest Coefficients and the Laplacian Polynomial]]. |

In this series, standalone types use parentheses: $(1^2)=(1,1)$, whereas $(1)^2=(1)*(1)$ denotes a product. Square brackets for collections and SPF notation $E_n[\lambda]$ are retained. Numerical parts of a type differ from vertex labels in boundary notation such as $(ab)$.

The correspondence $\lambda=(k_1,\ldots,k_r)\leftrightarrow x_{k_1}\cdots x_{k_r}$ preserves the type and gives two notations for the same data. Ordinary multiplication of these monomials concatenates lists of parts and differs from $*$. Under disjoint union of graphs, spanning-forest toponomes multiply by the ordinary polynomial product, while sums of color-class types multiply by $*$.

For a graph toponome, the expansion of the factors of the Laplacian exponential is fixed. With unit weights, coefficients count forests; with numerical weights, they sum products of edge weights. The rooted normalization is defined above. For an undirected graph with positive conductances, $P_G(t)=\prod_j(1+t\lambda_j)$, where $\lambda_j$ are the nonzero eigenvalues of $\mathbf L$. In this normalization, $(n,P_G)$ determines the Laplacian spectrum with multiplicities; neither the spectrum nor the polynomial specifies eigenvectors. See [[Forest Coefficients and the Laplacian Polynomial]]. Formal factorization parameters of $F_G$ or $\Phi_G$ do not automatically have this spectral meaning. Reduction by types is not identified with reduction of one polyform by another.

## Graphs, couplings, and matrix representations

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Coupling coefficient | Коэффициент связи | PMG | The pair coefficient $c_{ij}=\sum_{\ell:\,\ell=\{i,j\}}c_\ell$. In the main model it is symmetric and nonnegative. Summing parallel conductors preserves the Laplacian and metric, but changes the matroid ground set. |
| Edge conductance | Проводимость ребра | Standard | The positive weight $c_\ell$ of an individual conductor; it equals $c_{ij}$ when the pair has a single edge. Conductivity is not used in this sense. |
| Edge weight | Вес ребра | Standard | A general name for a numerical edge parameter. In this model the weight represents conductance, not length. |
| Weighted degree | Взвешенная степень вершины | Standard | The sum $d_i=\sum_jc_{ij}$. |
| Conductor resistance; resistance of an individual conductor | Собственное сопротивление ребра | Standard | The value $1/c_\ell$ for an individual conductor. It can differ from the effective resistance between its endpoints, $R_\ell=R_{ij}$. An aggregated coupling has conductor resistance $1/c_{ij}$. The notation $r_{ij}$ is reserved for one-way resistance. |
| Graph Laplacian matrix | Матрица лапласиана | Standard | In the symmetric model, $\mathbf L$ has diagonal entries $d_i$ and off-diagonal entries $-c_{ij}$. A digraph uses the outgoing convention $L_{ii}=\sum_jf_{ij}$, $L_{ij}=-f_{ij}$ for $i\ne j$. |
| Laplacian; Laplacian polyform | Лапласиан; полиформа лапласиана | PMG | The grade-one form with the Laplacian matrix as its coefficients. For an undirected graph, $L=\sum_{i<j}c_{ij}[a_{ij}]^2$; a balanced graph admits a nonsymmetric bilinear representation on boundaries. |
| Reduced Laplacian | Редуцированный лапласиан | Standard | The matrix obtained by deleting the row and column of the same vertex from $\mathbf L$. |
| Green matrix | Матрица Грина | Qualified | $\mathbf{Gr}=\mathbf L^+$. For a connected balanced graph, it inverts the Laplacian on the zero-sum subspace and vanishes on constant columns. With source-receiver pairing, the Gram matrix of centered vectors is $\mathbf{Gr}^{\mathsf T}$; in the symmetric case this equals $\mathbf{Gr}$. |
| Resistance matrix | Резистивная матрица | Qualified | The symmetric matrix $\mathbf R=(R_{ij})$ of pair resistances. For a balanced graph, $R_{ij}=r_{ij}+r_{ji}$; distinguish it from the one-way resistance matrix $\mathbf r$. |
| Distance operator | Дистанционный оператор | Qualified | The linear operator $\mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}$ on symmetric matrices. Applied to a symmetric Gram matrix, it gives squared distances. A nonsymmetric Gram matrix uses $A_{ij}+A_{ji}$ instead of $2A_{ij}$. |
| Centering matrix; centering projector | Центрирующий проектор | Standard | The matrix $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$. |
| Centroid | Центроид | Standard | The equal-weight mean of the points: $n^{-1}\sum_i a_i$. |
| Centering | Центрирование | Standard | Choosing the centroid as the origin in a Euclidean realization, so position vectors sum to zero. This introduces no new linear relation between formal basis vertices. |

When representations occur together, the polyform retains an ordinary letter and the matrix is bold: $L$ and $\mathbf L$. Scalar matrix entries are not bold: $L_{ij}$, $\mathrm{Gr}_{ij}$. Where the matrix representation is unambiguous, the introductory notes may use ordinary letters $L,G,R$.

## The Greenian and mutual duality

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Grade-one vector form | Векторная форма первого грейда | PMG | In the symmetric case, a sum of quadratic forms of vectors in $W$: $\sum c_\ell[u_\ell]^2$. The Laplacian and the Greenian have canonical representations through $[a_{ij}]^2$. Coefficients may have either sign. |
| Boundary polyform | Граничная полиформа | PMG | A polyform whose form arguments belong to exterior powers of the vector space $W$. Laplacian and Greenian exponentials are of this type; higher grades contain exterior products of several vectors. |
| Greenian | Гриниан | PMG | The grade-one form $\mathrm{Gr}=\sum_{i,j}\mathrm{Gr}_{ij}[a_i-h,a_j-h]$ with Green matrix $\mathbf{Gr}=\mathbf L^+$. In the symmetric case, $\mathrm{Gr}=-\sum_{i<j}\mathrm{Gr}_{ij}[a_{ij}]^2$. Formerly called the Green polyform; distinct from a Gram matrix $\mathbf G$. |
| Dual representation of the Greenian | Дуальное представление гриниана | PMG | The form $Q_1$ on $W^*$ satisfying $\mathcal C(Q_1)=\mathrm{Gr}$ for $\mathcal C:a_i^\vee\mapsto p_i=a_i-h$. Its exponential $D=\exp Q_1$ has grade-zero term $e$. The dual elements satisfy $\sum_i a_i^\vee=0$; they are distinct from the independent direct vertices $a_i$. In a section confined to one space, the mark $\vee$ may be omitted by explicit convention. |
| Mutually dual exponentials | Взаимно-дуальные экспоненты | PMG | For nondegenerate symmetric first grades: $M_d/Q_k=M_{d-k}$ and $Q_d/M_k=Q_{d-k}$ in paired direct and dual spaces. The slash means exterior contraction. This is a relation, not a separate type of polyform or multiplicative inversion. |
| Greenian exponential in the direct space | Экспонента гриниана в прямом пространстве | PMG | $N=\mathcal C(D)=\exp(\mathrm{Gr})$. With the same top-grade form $T_n$, $\tau(N)=1/(n^2\tau(G))$ for a connected undirected graph with positive conductances. It is not the multiplicative inverse of $M=\exp L$. |
| Exterior contraction in both arguments of a form | Внешнее удаление в обоих аргументах формы | Qualified | The linear operation $/$ between paired direct and dual sides, used in $M_d/Q_k=M_{d-k}$. Distinct from polyform multiplication, matrix pseudoinversion, and division of numbers. [[Laplacian and Greenian - Mutual Duality of Exponentials]]. |

Conventions and proofs appear in [[Laplacian and Greenian - Mutual Duality of Exponentials]] and [[The Canonical Vector Representation of the Greenian]]. In that series, the former name “dual polyform” for $D$ is replaced by “the Greenian exponential in its dual representation”. The relational phrase “a polyform dual to a given one” retains its precise meaning. The symmetric quadratic case is distinguished from the general bilinear case of balanced graphs.

For $u,v\in W$ in the direct space, the normalized potentials are $P_M([u,v])=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v$ and $P_N([u,v])=\mathbf u^{\mathsf T}\mathbf L\mathbf v$, where $P_N(f)=\tau(Nf)/\tau(N)$. The norm of a form depends on the chosen exponential; the metrics extend to higher grades through Gram determinants and bilinearity. [[The Greenian Metric and Potentials]].

## Spectral representations and projections

These definitions concern real symmetric Laplacians of undirected graphs. Eigenvectors are normalized in the auxiliary coordinate inner product $\langle\mathbf v,\mathbf w\rangle_0=\mathbf v^{\mathsf T}\mathbf w$ on $H=\mathbf1^\perp$; it differs from the resistance inner product with matrix $\mathbf{Gr}$. Definitions, proofs, and classical sources appear in [[en/Spectra and diagonalization in polyform algebra/Spectra and Diagonalization in Polyform Algebra|Spectra and Diagonalization in Polyform Algebra]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Eigenmode | Собственная мода | Standard | An eigenvector together with its eigenvalue and an explicitly chosen normalization. For a connected graph the constant mode has eigenvalue $0$, and the remaining modes lie in $H$. With multiplicities, individual modes are not canonical. |
| Eigenspace | Собственное подпространство | Standard | $H_\lambda=\ker(\mathbf L-\lambda I)$; for a symmetric operator its dimension is the eigenvalue multiplicity. |
| Spectral projector | Спектральный проектор | Standard | The coordinate-orthogonal projector $\mathbf E_\lambda$ onto $H_\lambda$. Independent of the orthonormal basis chosen within the eigenspace. Distinguish it from the form representing the projector: operator composition and form multiplication are different. |
| Full spectral representation | Полное спектральное представление | Qualified | Eigenvalues and spectral projectors in fixed vertex coordinates. Reconstructs the matrix, unlike the spectrum as a multiset of numbers. For a graph, it reconstructs total pair conductances. |
| Simultaneous orthogonal diagonalization | Совместная ортогональная диагонализация | Standard | A common orthonormal eigenbasis of a family of real symmetric operators; exists exactly when they commute pairwise. Their eigenvalues may differ. |
| Diagonal form of an eigendirection | Диагональная форма собственного направления | Qualified | The weighted form $\ell_\alpha=\lambda_\alpha[u_\alpha]^2$, where $u_\alpha=\sum_i u_{\alpha i}a_i$. Has grade $1$ and satisfies $\ell_\alpha^2=0$. |
| Diagonal representation of an exterior exponential | Диагональное представление внешней экспоненты | Qualified | The factorization $M(t)=\prod_\alpha(e+t\ell_\alpha)$ and grades $M_g=e_g(\ell_1,\ldots,\ell_d)$. Applies to the exponential of a symmetric first grade; does not assert simultaneous diagonalization of arbitrary higher grades. |
| Elementary symmetric polynomial | Элементарный симметрический полином | Standard | $e_g$ is the sum of products over all sets of $g$ distinct arguments. It can be evaluated in the commutative algebra of forms, where $e_0=e$; for numbers, $e_0=1$. Distinguish it from the external combinatorial potential $e_n(\mathbf x)$. |
| Coordinate evaluation of a form | Координатная оценка формы | Qualified | $\operatorname{ev}_0([X,Y])=\langle X,Y\rangle_0$, extending the inner product by Gram determinants. Linear but not an algebra homomorphism; $\operatorname{ev}_0(M_g)=p_g$. Differs from the resistance evaluation $P_M$. |
| Exterior power of an operator | Внешняя степень оператора | Standard | $\Lambda^g\mathbf A$ acts on an exterior product by applying $\mathbf A$ to every factor; eigenvalues multiply. The correspondence $M_g\leftrightarrow\Lambda^g(\mathbf L\vert_H)$ uses the coordinate metric. |
| Additive action on an exterior power | Аддитивное действие на внешней степени | Standard | The sum of the operator's actions on one exterior factor, leaving the others unchanged. Eigenvalues add. Differs from the exterior power of an operator and from the matrix exponential. |
| Laplacian spectral cone of a fixed basis | Лапласовский спектральный конус фиксированного базиса | Qualified | $\mathcal K_U$ consists of coefficients $\boldsymbol\mu$ for which $\mathbf U\operatorname{diag}(0,\boldsymbol\mu)\mathbf U^{\mathsf T}$ has nonpositive off-diagonal entries. The basis is coordinate-orthonormal and its first mode is constant. Coefficients are tied to directions; positive semidefiniteness alone is insufficient. |
| Diagonal projection in a fixed basis | Диагональная проекция в фиксированном базисе | Standard | The Frobenius projection $\Pi_U$ that removes an operator's off-diagonal entries in the selected basis. The retained evaluations $\mathbf u_k^{\mathsf T}\mathbf L\mathbf u_k$ need not be eigenvalues of the original operator. |
| Block spectral projection | Блочная спектральная проекция | Standard | $\Pi_{\mathrm{blk}}(\mathbf L)=\sum_\lambda\mathbf F_\lambda\mathbf L\mathbf F_\lambda$, where $\mathbf F_\lambda$ are the reference operator's projectors. Retains entire eigenspace blocks and is independent of the bases chosen within them. |
| Projection onto the graph spectral cone | Проекция на графовый спектральный конус | Qualified | The nearest admissible matrix of the fixed basis in the Frobenius norm. Corresponds to Euclidean projection of its coefficients onto $\mathcal K_U$; generally nonlinear and distinct from unconstrained diagonal projection. |

Symmetry of the polynomial $e_g$ in eigendirections does not imply invariance of a polyform under all vertex permutations. SPF retains its definition from the structural and symmetric series. With multiplicities, individual forms $\ell_\alpha$ depend on the basis, whereas complete grades and eigenspace forms do not.

Reversal of dual grade order means taking complementary sets of eigendirections, passing to the dual space, and normalizing by $\Delta=\prod_\alpha\lambda_\alpha=n\tau$ for a connected graph. It is not a simple permutation of grades. Disconnectedness, nonsymmetric balanced operators, and graph signs after projection require separate qualifications. Projection in operator space differs from resistance projection of PMG vectors. Conventions are collected in [[Core specification#Spectral representation in the symmetric case|the spectral section of the specification]].

## Resistance geometry and metric evaluation

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Effective resistance | Эффективное сопротивление | Standard | The quantity $R_{ij}$ determined by the entire network and the vertex pair. In the resistance realization it is the squared Euclidean distance. |
| Resistance distance | Резистивное расстояние | Standard | Effective resistance $R_{ij}$ viewed as a metric on vertices. It does not mean $\sqrt{R_{ij}}$. |
| Resistance inner product | Резистивная метрика на векторах | Qualified | In the symmetric model, the inner product $u\cdot v=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v$ on $W$. The balanced extension distinguishes the full pairing $\beta$ from its symmetric part $g$. |
| Resistance simplex | Резистивный симплекс | Qualified | A Euclidean simplex whose squared pairwise distances are $R_{ij}$. Its dimension in the main model is $n-1$. |
| Gram matrix | Матрица Грама; грамиан | Qualified | The matrix $\mathbf G=(g_{ij})$ of pairings of selected elements: $g_{ij}=a_i\cdot a_j$. The balanced model uses role order $a_i^{\mathrm{out}}\cdot a_j^{\mathrm{in}}$. For local vertices, $\mathbf G=-\mathbf R/2$ in the symmetric case; in general, $(\mathbf G+\mathbf G^{\mathsf T})/2=-\mathbf R/2$. |
| Mixed Gram determinant | Смешанный определитель Грама | Standard | The determinant of $(u_r\cdot v_s)$ for two ordered collections of equal size. |
| Induced inner product | Индуцированное скалярное произведение | Standard | The extension of the metric to $\Lambda^kW$ through mixed Gram determinants and bilinearity. |
| Norm of an exterior element; quadratic norm | Норма внешнего объекта; квадратичная норма | PMG | The number $X^2=X\cdot X$. In the resistance metric it is also called the resistance norm. For a decomposable boundary object in a symmetric metric, it is the squared volume of a parallelotope; in the balanced model the full potential may contain a circulation contribution. |
| Linear norm | Линейная норма | PMG | The quantity $\|X\|=\sqrt{X^2}$ for $X^2\ge0$. On a positive definite space, it agrees with the usual Euclidean norm. |
| Metric evaluation of a form | Численная метрическая оценка формы | PMG | The linear evaluation $[X,Y]\mapsto X\cdot Y$ on forms on boundaries of a fixed grade. |

> [!info] Object, form, and number
> The notations $X$, $[X]^2$, and $X^2$ are distinct: they denote an exterior object, a formal quadratic form, and a numerical norm, respectively. The exterior product of an object with itself is written explicitly as $X\wedge X$.

In a symmetric metric, the norm of a simplex boundary is the squared volume of a parallelotope, while its linear norm is the volume itself. The squared volume of the $k$-dimensional simplex is the norm of its boundary divided by $(k!)^2$. The metric on boundaries does not automatically define the norm of a formal point or simplex outside $\Lambda^kW$.

## Metric polyforms, forests, and the spanning-tree coefficient

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Metric polyform | Метрическая полиформа | PMG | The exponential $M_G=\exp L$ in the algebra of forms. It is not the matrix exponential $\exp\mathbf L$. |
| Edge form; pair form | Форма связи | PMG | The quadratic form $[a_{ij}]^2$. Its weighted contribution to the Laplacian is $c_{ij}[a_{ij}]^2$. |
| Edge factor | Фактор-форма связи | PMG | The multiplier $e+c_{ij}[a_{ij}]^2$ in the factorization of $M_G$. “Фактор-форма” is the shortened Russian name. |
| Spanning tree | Остовное дерево | Standard | A connected acyclic subgraph containing every vertex of the original graph. |
| Spanning forest | Остовный лес | Qualified | In this series, any acyclic subgraph containing every vertex, including isolated ones. Maximality of the edge set is not required. |
| Spanning 2-forest | Остовный 2-лес | Standard | A spanning forest with exactly two components. |
| Separating spanning 2-forest | Разделяющий остовной 2-лес | Qualified | A spanning 2-forest in which two specified vertices lie in different components. |
| Forest weight; tree weight | Вес леса или дерева | Standard | The product of the conductances of the selected edges. The empty product is $1$. |
| Forest expansion | Лесное разложение | Qualified | An expression for $M_k$ as a sum of weighted forms of forests with $k$ edges. Each such forest has $n-k$ components. |
| Spanning-tree form | Остовная форма | PMG | The fixed form $T_n=[(a_1\ldots a_n)]^2$ of grade $n-1$. |
| Top-grade form | Предельная форма | PMG | In the core, another name for $T_n$. No limiting process is involved; “limit form” is not used. |
| Top-grade component | Предельная компонента | Qualified | For a connected graph's metric polyform, $M_{n-1}=\tau(G)T_n$. It must be distinguished from the form $T_n$ itself. |
| Next-to-top-grade component | Допредельная компонента | PMG | For a connected graph's metric polyform, $M_{n-2}$, containing forms of spanning 2-forests. |
| Weighted spanning-tree sum; spanning-tree coefficient | Остовной коэффициент графа | Qualified | The sum $\tau(G)$ of spanning-tree weights. For unit conductances, it is the spanning-tree count. |
| Top-coefficient functional | Функционал извлечения остовного коэффициента | PMG | The linear functional $\tau(P)$ extracting the coefficient of the fixed $T_n$ from a polyform on boundaries. For general $P$, it need not be a sum of tree weights. |

For a disconnected graph, the highest nonzero grade of $M_G$ is $n-c$, where $c$ is the number of connected components. “Highest nonzero component” does not mean replacing the fixed $T_n$ by a different form: $\tau(M_G)=0$ still holds when $c>1$.

The sum of forest weights refers to a specified forest expansion. Because forms satisfy linear relations, an arbitrary expression for the same object may have a different coefficient sum.

## Matroids and forest parameters

> [!info] Matroids and forest parameters
> **Definition.** A finite matroid is a pair $(E,\mathcal I)$, where $E$ is a finite ground set and $\mathcal I$ is a family of independent subsets satisfying three axioms:
>
> 1. $\varnothing\in\mathcal I$.
> 2. If $I\in\mathcal I$ and $J\subseteq I$, then $J\in\mathcal I$.
> 3. If $I,J\in\mathcal I$ and $\#I<\#J$, there is $e\in J\setminus I$ such that $I\cup\{e\}\in\mathcal I$.

The third condition is the augmentation axiom. For a graph, the elements are individual edges and the independent sets are forests. See [[The Cycle Matroid and Exterior Products of Edges]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Cycle matroid of a graph | Цикловой матроид графа | Standard | $M(G)=(E,\mathcal I)$, whose independent sets are edge sets without cycles. Their exterior products are nonzero. Isolated vertices are not matroid elements. Loops are dependent, and parallel edges form a two-element circuit. |
| Matroid basis | Базис матроида | Standard | An inclusion-maximal independent set. In a connected graph, a spanning tree; in a disconnected graph, a spanning tree in each component. All bases have size $r(E)$. |
| Matroid circuit | Цикл матроида | Standard | An inclusion-minimal dependent set. In a cycle matroid, a graph cycle, including a loop or a pair of parallel edges when the model permits them. |
| Matroid rank and subset rank | Ранг матроида и ранг подмножества | Standard | $r(S)=\max\{\#I:I\subseteq S,\ I\in\mathcal I\}$; the matroid rank is $r=r(E)$. For a graph, $r=n-\kappa(G)$, where $\kappa(G)$ is the number of connected components; isolated vertices are included in both $n$ and $\kappa(G)$. |
| Forest corank | Когрейд леса | Qualified | $k=r-g$, where $g=\#E(F)$. A forest on all $n$ vertices has $m=n-g$ components, so $k=m-\kappa(G)$. For a connected graph, $r=d=n-1$ and $m=k+1$. |
| Weight-preserving matroid isomorphism | Изоморфизм матроидов с сохранением весов | Standard | A bijection of ground sets preserving independent subsets in both directions and the weights of corresponding elements. For electrical parameters, the conductances $c_\ell$ are preserved. |
| Matroid parameter; matroid invariance | Матроидный параметр; матроидная инвариантность | Qualified | A graph characteristic determined by its cycle matroid, with element weights included in the weighted case. A scalar is preserved by the relevant isomorphism; an edge-indexed family is transported by its bijection. This property implies neither additivity nor completeness of an invariant system. |

In the following definitions, $G$ is an undirected loopless graph with positive individual edge conductances, $w(F)=\prod_{\ell\in E(F)}c_\ell$, and $\pi(F)$ partitions all vertices into forest components. The normalized families $\alpha_k$, $s_m^{\mathrm{for}}$, $\xi_k$, as well as random spanning trees and $H_q$, additionally require connectedness, $n\ge2$, and $d=n-1$. Definitions of ordinary and rooted sums: [[Forest Coefficients - Grade, Components, and Corank]], [[Forest Coefficients and the Laplacian Polynomial]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Ordinary forest coefficients of a graph | Обычные лесные коэффициенты графа | Qualified | $f_g(G)=\sum_{F:\,\#E(F)=g}w(F)$ over spanning forests without chosen roots. All vertices, including isolated ones, are retained. $f_0=1$; for a connected graph, $f_d=\tau(G)$. These matroid coefficients differ from $\operatorname{St}(k,m)$. |
| Rooted forest coefficients of a graph | Корневые лесные коэффициенты графа | Qualified | $p_g(G)=\sum_{F:\,\#E(F)=g}w(F)\prod_{C\in\pi(F)}\#C$. One root is chosen in each component. These are the coefficients of $P_G(t)=\det(I+t\mathbf L)$; for a connected graph, $p_d=n\tau(G)$. Not matroid invariants in general. |
| Ordinary forest polynomial | Обычный лесной полином | Qualified | $F_G(t)=\sum_{g=0}^{r}f_g(G)t^g$. Collects ordinary spanning forests by grade and differs from the rooted polynomial $P_G$. |
| Reversed forest polynomial | Обращённый лесной полином | Qualified | $\mathscr F_G(u)=u^rF_G(u^{-1})=\sum_{k=0}^{r}f_{r-k}u^k$, the corank-indexed form. The variables $t,u$ differ from the type variables $x_i$. |
| Normalized forest coefficients and polynomial | Нормированные лесные коэффициенты и полином | PMG | For a connected graph, $\alpha_k=f_{d-k}/\tau$, $\Phi_G(u)=\mathscr F_G(u)/\tau=\sum_{k=0}^{d}\alpha_k u^k$, and $\alpha_0=1$. In the fixed cut-based forest representation of $Q_k$, the coefficient sum is $\alpha_k$. |
| Forest power-sum parameters | Лесные степенные параметры | PMG | $s_m^{\mathrm{for}}$ are defined by the formal series $\log\Phi_G(u)=\sum_{m\ge1}(-1)^{m-1}s_m^{\mathrm{for}}u^m/m$. Equality with spectral power sums is not assumed. [[The Normalized Forest Polynomial and Power-Sum Parameters]]. |
| Forest resistance scale | Лесной резистивный масштаб | PMG | $\xi_k=f_{d-k}/f_{d-k+1}=\alpha_k/\alpha_{k-1}$, $1\le k\le d$. Has resistance dimension, but is not defined as the resistance of a chosen vertex pair. [[Forest Resistance Scales]]. |
| Edge effective resistance | Эффективный резистенс ребра | Qualified | $R_\ell=R_{ij}$ for an existing edge $\ell=\{i,j\}$, accounting for the entire network. Distinct from $1/c_\ell$. The edge-indexed family is matroidal when conductances are preserved; this does not recover resistances of arbitrary vertex pairs. |
| Edge inclusion probability | Вероятность включения ребра | Standard | $\eta_\ell=\Pr(\ell\in T)=c_\ell R_\ell=c_\ell\,\partial\log\tau/\partial c_\ell$ under $\Pr(T)=w(T)/\tau$. Individual parallel edges retain their identities. [[Edge Resistances and Random Spanning Trees]]. |
| Edge resistance parameters | Рёберные резистивные параметры | PMG | $H_q=\sum_{\ell\in E}\eta_\ell^q/c_\ell$, $q=1,2,\ldots$. The expected sum of conductor resistances of edges in the intersection of $q$ independent random spanning trees. In particular, $H_2=\sum_\ell c_\ell R_\ell^2$. [[Edge Resistances and Random Spanning Trees]]. |

If conductance has dimension $C$, then $[f_g]=[p_g]=C^g$, $[\alpha_k]=C^{-k}$, $[s_m^{\mathrm{for}}]=C^{-m}$, $[\xi_k]=[R_\ell]=[H_q]=C^{-1}$, while $\eta_\ell$ is dimensionless.

Matroid invariance of $f_g$ does not imply matroid invariance of the rooted coefficients $p_g$ or the full component-size toponome. The coefficient sum of the fixed cut-based representation of $Q_k$ is also distinct from the canonical forest sum of the Greenian with weights $\gamma_{ij}=-\mathrm{Gr}_{ij}$. Spectral coefficients and ordinary forest coefficients are distinguished.

Under one-vertex gluing of connected graphs with disjoint edge sets, $\tau$, $F_G$, and $\Phi_G$ multiply, $\alpha_k$ convolve, and $s_m^{\mathrm{for}}$, $H_q$, and $\rho$ add. Additivity is not asserted for $\xi_k$ with $k>1$. These laws are proved separately from invariance in [[Gluing and the Limits of Matroid Invariance]]. Aggregating parallel conductors preserves $H_2$, but not the entire family $H_q$. Agreement of several invariants does not prove matroid isomorphism. Statements in this section do not extend automatically to balanced graphs.

## Boundary states and passports

This section covers terminology from the completed [[en/Boundary polynomials and graph gluing/Boundary Polynomials and Graph Gluing|Boundary Polynomials and Graph Gluing]] series. The governing formulas and conditions are collected in the [[en/Foundations/Core specification#Boundary passports and graph gluing|specification]]. “Passport” is the PMG name for a collection of data; terminology status does not imply novelty of a mathematical result. The notes and navigator identify the origins of theorems and of the derivations given in the series.

### Forest data and their reduction

Here $B$ is a nonempty set of marked vertices, $k=\#B$, and $n=\#V(G)$. Forests contain all vertices; neither connectivity nor planarity of the graph is assumed. Individual edge weights are positive. Definitions: [[en/Boundary polynomials and graph gluing/Boundary Forest States - What to Retain from a Component]], [[en/Boundary polynomials and graph gluing/Vertex Contraction as a Boundary Test]], [[en/Boundary polynomials and graph gluing/Gluing Components by Pairing Boundary Data]], [[en/Boundary polynomials and graph gluing/The Four-Point Passport and State Reduction]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Marked boundary | Отмеченная граница | Qualified | A set $B\subseteq V(G)$ with fixed names and a fixed gluing correspondence. It is not an algebraic boundary $\partial X$. For a spectral pair, the order $\mathcal B=(a,b)$ matters. |
| Component to be glued; constituent graph | Компонента сочленения | Qualified | A part of the construction, not necessarily a connected component of a graph. Its internal vertices are distinct from those of other parts. |
| Boundary forest state | Граничное лесное состояние | Qualified | The connectivity partition $\pi_B(H)$ of the boundary in a spanning forest $H$. It does not select a unique forest: different forests can induce the same state. |
| Internal forest component | Внутренняя компонента леса | Qualified | A component that does not meet $B$. A forest with $g$ edges in state $\pi$ has $n-g-b(\pi)$ such components. |
| Boundary-state polynomial | Полином граничного состояния | Qualified | $\mathcal F^{G,B}_\pi(t)=\sum_{\pi_B(H)=\pi}w(H)t^{\#E(H)}$. Includes forests with internal components; the degree of $t$ counts selected edges. |
| Full boundary forest passport | Полный граничный лесной паспорт | PMG | The vector $\mathbf f_G(t)=(\mathcal F^{G,B}_\pi(t))_\pi$. Boundary names, their correspondence, and the total vertex count are retained separately. The sum of coordinates is $F_G(t)$ and loses the distribution over states. |
| Free boundary-state space | Свободное пространство граничных состояний | Qualified | $\mathscr S_B=\bigoplus_{\pi\in\Pi(B)}\mathbb R s_\pi$; the symbols $s_\pi$ are independent. Their images $q_\pi$ in the algebra of forms may satisfy structural identities. |
| Boundary partition rank; join of partitions | Ранг граничного разбиения; соединение разбиений | Standard | $r(\pi)=k-b(\pi)$, where $b(\pi)$ is the number of blocks. $\pi\vee\sigma$ is the least common coarsening. This rank is not the grade of an arbitrary forest in state $\pi$. |
| Forest compatibility; compatibility matrix | Лесная совместимость; матрица совместимости | Qualified | $C(\pi,\sigma)=1$ when $r(\pi\vee\sigma)=r(\pi)+r(\sigma)$ and $0$ otherwise; $\mathbf C_B=(C(\pi,\sigma))$. The condition means that gluing creates no new cycle. |
| Boundary contraction test; test response | Граничный тест стягивания; тестовый отклик | Qualified | $U_G(\sigma;t)=F_{G/\sigma}(t)$, $\mathbf u_G=\mathbf C_B\mathbf f_G$. Selects forests that remain acyclic after identifying vertices in the blocks of $\sigma$. It is not an electrical response. |
| Forest boundary pairing | Лесное граничное спаривание | Qualified | The algebraic bilinear form $\mathbf x^{\mathsf T}\mathbf C_B\mathbf y$ on formal states. It is not the resistance inner product. |
| Radical of the forest pairing | Радикал лесного спаривания | Standard | $\mathscr R_B=\ker\mathbf C_B$. Vectors whose pairing with every state is zero; not the kernel of the map to partition forms. |
| Reduced linear forest passport | Сокращённый линейный лесной паспорт | PMG | A class in $\mathscr H_B=\mathscr S_B/\mathscr R_B$, taken coefficientwise in $t$ for polynomials. The dimension $\mathrm{Cat}_k$ is minimal for a universal linear passport with a fixed bilinear law. Coordinates may be signed. |
| Noncrossing boundary basis | Непересекающийся граничный базис | Qualified | Classes of noncrossing partitions in a chosen cyclic order on $B$. This is a coordinate choice for the forest quotient, not a graph-planarity assumption or an identification with a basis of actual polyforms. |

### Groves and electrical data

Groves are defined without a planarity assumption. The resistance Gram matrix and the electrical correspondences below require a connected graph with positive conductances; $I=V(G)\setminus B$. Definitions, external foundations, and reconstruction limits: [[en/Boundary polynomials and graph gluing/The Spanning-Tree Layer and Boundary Resistance Geometry]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Grove | Роща | Standard | A spanning forest every component of which contains at least one boundary vertex. A forest with an internal component is not a grove. |
| Grove weight of a state; grove layer | Вес рощ состояния; слой рощ | Qualified | $g^{G,B}_\pi=[t^{n-b(\pi)}]\mathcal F^{G,B}_\pi(t)$. The extraction degree depends on the state; it does not define a single common grade for the whole vector. |
| Spanning-tree boundary pairing | Остовное граничное спаривание | Qualified | Restriction of the forest rule to pairs with $\pi\vee\sigma=\{B\}$ and $r(\pi)+r(\sigma)=k-1$. Counts spanning trees of the result using grove weights of the parts. |
| Fully separated grove scale | Масштаб полностью разделённой рощи | Qualified | $\delta_B(G)=g^{G,B}_{b_0\mid\cdots\mid b_{k-1}}=\det\mathbf L_{II}$. Recovers the scale lost in eliminating the interior; the empty determinant is $1$. |
| Boundary response matrix; Dirichlet-to-Neumann operator | Граничная матрица отклика; оператор Дирихле–Неймана | Standard | $\boldsymbol\Lambda_B=\mathbf L_{BB}-\mathbf L_{BI}\mathbf L_{II}^{-1}\mathbf L_{IB}$. Maps boundary potentials to currents entering the network; it is the Laplacian of the effective network after eliminating internal vertices. |
| Boundary resistance Gram matrix | Граничный резистивный грамиан | Qualified | $\mathbf G_B=\mathbf D^{\mathsf T}\mathbf{Gr}_G\mathbf D$, where the columns of $\mathbf D$ are unit differences $b_i-b_0$. Inverse of the reduced response matrix; depends on the chosen basis. |
| Circular planarity | Круговая планарность | Standard | Embeddability of a network in a disk with boundary vertices on its boundary in the prescribed cyclic order. A condition in results recovering individual normalized grove weights from the electrical response. |

### Spectral boundary data

Here the pencil is $\mathbf M_G(\xi)=\xi I-\mathbf L_G$ and the ordered pair is $\mathcal B=(a,b)$. Connectivity is required for the electrical interpretation at $\xi=0$, but not for the determinant identities. Definitions and formulas: [[en/Boundary polynomials and graph gluing/From the Forest Passport to Spectral Boundary Data]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Spectral boundary passport of a pair | Спектральный граничный паспорт пары | PMG | Five polynomials $(A,B,C,D,E)$: the pencil determinant, two principal minors each deleting one boundary vertex, an off-diagonal adjugate entry, and the internal principal minor. These are not five ordinary forest states. |
| Spectral Schur complement | Спектральное дополнение Шура | Qualified | $\mathbf S_G(\xi)=E^{-1}\left(\begin{smallmatrix}C&-D\\-D&B\end{smallmatrix}\right)$ when $E\ne0$. Depends on the spectral parameter; for a connected graph, $\mathbf S_G(0)=-\boldsymbol\Lambda_{\mathcal B}$. |
| Jacobi identity for the passport | Тождество Якоби для паспорта | Standard | $AE=BC-D^2$. A polynomial determinant identity also valid at zeros of $E$; it rules out algebraic independence of the five coordinates. |
| Input and output boundaries; active boundary | Входная и выходная граница; активная граница | Qualified | Marked sets and their correspondences at successive chain-assembly steps. Moving to a new active boundary requires a separate transfer rule; closure of a five-coordinate automaton does not follow from a passport for a fixed pair. |

## Potentials, norms, and variations

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Electrical potential | Электрический потенциал вершины | Standard | The value $\varphi_i$ in a solution of the network equations for specified input, subject to the freedom to choose a reference potential. |
| Polyform potential | Потенциал формы | PMG | The quantity $u_M(f)=\tau(Mf)$ for fixed $M$. It is not the electrical potential at a vertex. |
| Normalized polyform potential | Нормированный потенциал | PMG | $P_M(f)=u_M(f)/u_M(e)=\tau(Mf)/\tau(M)$ when $\tau(M)\ne0$. The same definition applies in the symmetric and balanced models. |
| PMG form norm | Норма формы в PMG | PMG | An acceptable name for the normalized potential. For a general form this is a linear evaluation, not a norm in the usual sense. |
| Metric identity | Метрическое тождество | PMG | For $M=M_G=\exp L$ in the symmetric model, the normalized potential of $[X,Y]$ equals the induced inner product $X\cdot Y$. The balanced model uses the full pairing $\beta$ and its determinant extension, rather than only the symmetric part $g$. |
| Conductance variation | Вариация проводимости | Standard | A change $c_{ij}\mapsto c_{ij}+t$. The main graph model requires nonnegative final conductance. |
| Algebraic Laplacian variation | Алгебраическая вариация лапласиана | PMG | In the symmetric model, an elementary update $t[v]^2$ with $v\in W$; in the balanced model, $t[u,v]$ with $u,v\in W$. It generally changes several couplings; weight admissibility is checked separately. |
| Joint conductance variation | Совместная вариация связей | Qualified | Simultaneous changes in conductances of several vertex pairs; their interaction is determined by the Gram matrix of the corresponding vectors. |

In the symmetric resistance model, for a quadratic form $[X]^2$ the normalized potential is $\|X\|^2$, not $\|X\|$. For a mixed form it can be negative even when the metric is positive definite. This does not mean that the exterior object has a negative norm.

In PMG, “norm” without the qualifier “linear” means the quadratic norm $X^2=X\cdot X$. The notation $\|X\|$ is reserved for the linear norm. The norm of a form is defined through the normalized potential; the evaluation of a product of forms generally differs from the product of their evaluations.

## Balanced graphs and directional metrics

This section concerns loopless balanced digraphs with nonnegative arc weights. Connectedness is assumed when potentials are normalized and a metric is used. Conventions are collected in the [[Core specification#The balanced extension|balanced extension of the specification]]; proofs are in [[en/Balanced graphs/Balanced Graphs|Balanced Graphs]].

| English term | Russian equivalent | Status | Meaning and convention |
| --- | --- | --- | --- |
| Balanced digraph; balanced graph | Балансовый граф; балграф | Standard; PMG abbreviation | A weighted digraph whose incoming and outgoing weight sums agree at every vertex. Its outgoing Laplacian satisfies $\mathbf L\mathbf1=0$ and $\mathbf1^{\mathsf T}\mathbf L=0$. |
| 2-balanced graph | 2-балграф | PMG | An optional name for a symmetric graph as a sum of weighted directed 2-cycles. The existence of this decomposition does not mean that every decomposition uses only 2-cycles. |
| Arc weight | Вес дуги | Standard | $f_{ij}\ge0$ for arc $i\to j$; $L_{ij}=-f_{ij}$ for $i\ne j$. It is not the directional pairing of the vertices. |
| Spanning in-arborescence | Остовное ордерево к корню | Standard | A directed spanning tree in which every nonroot vertex has exactly one outgoing arc and its directed path leads to the root. |
| Rooted spanning-tree potential | Остовной потенциал вершины | Qualified | $\tau_i=\det\mathbf L_{\widehat i,\widehat i}$, the sum of weights of arborescences toward root $i$. Its column satisfies $\mathbf L^{\mathsf T}\boldsymbol\tau=0$. Distinct from electrical potential $\varphi_i$. |
| Common spanning-tree coefficient | Общий остовной коэффициент балграфа | Qualified | The common value $\tau_i=\tau>0$ in a connected balanced graph. One fixed root is counted; the sum over all roots is $n\tau$. [[Balanced Graphs and Spanning-Tree Potentials]]. |
| Canonical centered representation | Каноническое центрированное представление | PMG | $L=\sum_{i,j}L_{ij}[a_i-h,a_j-h]$ with centroid $h$. The coefficient matrix is normalized by zero row and column sums. It is not a canonical cycle decomposition. [[The Bilinear Laplacian of a Balanced Graph]]. |
| Directional pairing; bilinear pairing | Направленное сопряжение; направленное скалярное произведение | Qualified | $\beta(u,v)=P_M([u,v])=\mathbf v^{\mathsf T}\mathbf{Gr}\mathbf u$. The first argument is a source, $\mathrm{out}$; the second a receiver, $\mathrm{in}$. In general it is not a symmetric inner product. |
| Symmetric part of the metric | Симметричная часть метрики | Qualified | $g(u,v)=(\beta(u,v)+\beta(v,u))/2$. Positive definite on $W$, it gives Euclidean distances with squares $R_{ij}$. It does not determine the entire bilinear metric. |
| Circulation form | Форма циркуляции | PMG | $\omega(u,v)=[u,v]-[v,u]$ for affine vectors. A skew-symmetric formal form of PMG grade one. It can be considered without a graph. [[The Circulation Form]]. |
| Triangular circulation form | Треугольная форма циркуляции | PMG | $w(abc)=\omega(b-a,c-a)$. In the adopted orientation, $w(abc)=L_{acb}-L_{abc}$ for unit directed cycles. It is their difference, not a full cycle Laplacian. |
| Circulation potential; circulation norm | Циркуляционный потенциал; циркуляционная норма | PMG | $\chi_{ijk}=P_M(w(a_i a_j a_k))$. The difference of one-way resistance sums along the two orientations. It can have either sign; norm means the normalized form potential. |
| One-way resistance | Односторонний резистенс | PMG | $r_{ij}=P_M([a_j-h,a_j-a_i])=\mathrm{Gr}_{jj}-\mathrm{Gr}_{ij}$. Defined for every pair, it can be asymmetric even in an undirected graph. [[One-Way Resistance and Hitting Times]]. |
| Two-way resistance | Двусторонний резистенс | Qualified | $R_{ij}=r_{ij}+r_{ji}$. It agrees with undirected resistance in the symmetric case. |
| One-way resistance matrix | Матрица односторонних резистенсов | PMG | $\mathbf r=(r_{ij})$. It determines $\mathbf{Gr}=-\mathbf J\mathbf r$ and the original $\mathbf L=\mathbf{Gr}^{+}$. The symmetric $\mathbf R=\mathbf r+\mathbf r^{\mathsf T}$ is generally insufficient. |
| Mean hitting-time matrix | Матрица средних времён достижения | Standard | $\mathbf H=(H_{ij})$ in the chosen Markov model. For the continuous-time walk with generator $-\mathbf L$ on a connected balanced graph, $H_{ij}=nr_{ij}$. This interprets resistances; changing the process normalization changes the formula. |
| Outgoing and incoming bi-coordinates | Исходящие и входящие би-координаты | PMG | Expansion coefficients of a specified representative in the $\mathrm{out}$ or $\mathrm{in}$ role basis. Each expansion is unique. Two representatives of one functional may have different coordinates. |
| Outgoing and incoming di-coordinates | Исходящие и входящие ди-координаты | PMG | Pairings with the opposite-role basis: $\mathbf d_{\mathrm{out}}=\mathbf G^{\mathsf T}\mathbf b_{\mathrm{out}}$, $\mathbf d_{\mathrm{in}}=\mathbf G\mathbf b_{\mathrm{in}}$. [[The Gram Matrix and Directional Coordinates of a Balanced Graph]]. |
| Directional projections | Направленные проекции | PMG | Projections imposing orthogonality in the first or second argument of $\beta$. On line $ab$, their coefficients of $b$ are $\beta(a_i-a,b-a)/R_{ab}$ and $\beta(b-a,a_i-a)/R_{ab}$. [[Balanced Variations#One-way variation and loss of balance]]. |
| Metric representatives of the sphere | Метрические представители сферы | PMG | $S_{\mathrm{out}}$ and $S_{\mathrm{in}}$ represent one functional by pairing from different sides. Their bi-coordinates may differ, but $S_{\mathrm{out}}\cdot S_{\mathrm{in}}=\rho$. [[The Isotropic Space and Sphere of a Balanced Graph]]. |
| Balanced variation | Балансовая вариация | Qualified | A Laplacian update with zero row and column sums; nonnegative final weights are checked separately. Its elementary form is $t[u,v]$ with $u,v\in W$. [[Balanced Variations]]. |
| Single-arc variation | Односторонняя вариация дуги | Qualified | A weight change for one arc $a\to b$, $\Delta\mathbf L=t\mathbf e_a(\mathbf e_a-\mathbf e_b)^{\mathsf T}$. For $a\ne b$ and $t\ne0$, it breaks the original balanced graph's balance. |

Indices $i\to j$ in $r_{ij}$ specify the direction of a pair, whereas $\mathrm{out}/\mathrm{in}$ specify argument roles in the pairing; these are different conventions. The normalized potential $P_M(F)=\tau(MF)/\tau(M)$ is the common algebraic basis of resistance and circulation quantities. Rooted potentials $\tau_i$ and electrical potentials $\varphi_i$ are defined separately.

## KVP and KVPOU structural decompositions

The object being decomposed is an explicitly chosen real pair-data table on a fixed set of $n\ge3$ elements. Its diagonal is zero, and all component formulas refer to $i\ne j$. An absent coupling is represented by zero; an unknown value is not replaced by zero. Positivity, connectedness, and a metric are not required for the linear decomposition. Definitions and proofs: [[KVP Decomposition of Pair Characteristics]], [[Oriented Extensions of KVP - Circulation and Imbalance]].

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| KVP decomposition | KVP-разложение | PMG | The unique decomposition of a symmetric table as $A=A_K+A_V+A_P$. The constant K component gives the overall level, V reproduces deviations of row sums, and P has zero row sums. |
| K component | K-компонента | PMG | $(A_K)_{ij}=\mu$, where $\mu=\binom{n}{2}^{-1}\sum_{i<j}A_{ij}$. The average includes all distinct pairs, including zero entries. |
| V component | V-компонента | PMG | $(A_V)_{ij}=(v_i+v_j)/(n-2)$, where $v_i=\sum_{j\ne i}A_{ij}-(n-1)\mu$ and $\sum_i v_i=0$. |
| P component | P-компонента | PMG | $A_P=A-A_K-A_V$, the symmetric residual satisfying $\sum_{j\ne i}(A_P)_{ij}=0$. |
| Component sector and projector | Сектор и проектор компоненты | Qualified | A sector is the linear subspace of tables of a specified kind; $\Pi_X$ extracts $A_X$. For KVP, $\Pi_X^2=\Pi_X$, $\Pi_X\Pi_Y=0$ for $X\ne Y$, and the projectors sum to the identity. |
| KVPOU decomposition | KVPOU-разложение | PMG | For a directed table $C$, its symmetric part $S=(C+C^{\mathsf T})/2$ has a KVP decomposition, and its skew part $H=(C-C^{\mathsf T})/2$ splits into O and U. Thus $C=C_K+C_V+C_P+C_O+C_U$. |
| U component; vertex imbalance | U-компонента; вершинный дисбаланс | PMG | $(C_U)_{ij}=(u_i-u_j)/n$, where $u=H\mathbf1=(C\mathbf1-C^{\mathsf T}\mathbf1)/2$. This skew vertex part reproduces the imbalance of outgoing and incoming sums. For a balanced table, $U=0$. |
| O component; circulation component | O-компонента; циркуляционная компонента | PMG | $C_O=H-C_U$, $C_O^{\mathsf T}=-C_O$, $C_O\mathbf1=0$. A circulation table with zero row and column sums. |
| Coefficient orthogonality | Коэффициентная ортогональность | Qualified | Orthogonality of sectors under $\langle C,D\rangle_0=\tfrac12\sum_{i\ne j}C_{ij}D_{ij}$. On symmetric tables this is $\sum_{i<j}C_{ij}D_{ij}$. Distinct from the metric pairing of PMG elements. |

Components of couplings, the Green matrix, and resistances belong to different input tables. When applying the decomposition to $\mathbf{Gr}$, its off-diagonal part is treated as a pair table separately from the diagonal. The existence of a KVPOU decomposition does not itself define a resistance metric for an arbitrary unbalanced digraph. See [[KVP Decomposition of the Green Matrix and Resistances]].

## Earlier names and ambiguous usages

The following table also records earlier Russian usage, so that older research notes can be read consistently with the public core.

| Earlier or ambiguous name | Recommended expression | Reason for clarification |
|---|---|---|
| “Metric mass” | Resistance radius for $R_{\mathrm{sph}}^2$; resistance diameter for $4R_{\mathrm{sph}}^2$ | The earlier name is replaced with geometric terminology that explicitly distinguishes the normalizations. |
| “2-вектор” | Vertex-pair vector, $a_{ij}=a_j-a_i$ | In English, 2-vector normally means an object of exterior grade $2$, whereas $a_{ij}$ has grade $1$. “Two-point vector” is acceptable when explicitly defined. |
| “Order” without specifying the object | Grade | A simplex and its boundary differ in grade by one. |
| “Кратность” of a linear element | Affine weight | The coefficient-sum functional need not take integer values. |
| “Остовное число” for a weighted graph | Spanning-tree coefficient | A weighted sum need not be an integer. “Spanning-tree count” is appropriate when counting trees. |
| “Резистенс” | Resistance; effective resistance in the electrical interpretation | The Russian geometric term is retained in public graph descriptions. English uses “resistance”, with “effective resistance” where needed for interpretation and comparison with external sources. |
| “Матрица резистенсов” | Resistance matrix; «резистивная матрица» | Consistent naming with the introductory series. |
| “Двухлес” | Spanning 2-forest | The full name specifies that all vertices are included and there are two components. |
| “Связь-форма” | Specify $[a_{ij}]^2$, $c_{ij}[a_{ij}]^2$, or $e+c_{ij}[a_{ij}]^2$ | A pair form, a Laplacian contribution, and an exponential factor are different objects. |
| “Squared norm” for $X\cdot X$ | Norm or quadratic norm; also resistance norm in the resistance metric | In PMG, the norm is $X\cdot X$ itself; its square root for nonnegative norm is the linear norm. The formal form $[X]^2$ differs from its numerical evaluation. |
| “Potential of an object” | “Potential of the form $f$” or “combinatorial potential of the collection $\mathbf x$”, as appropriate | For $u_M(f)$, specify the form and metric; for $s_2(\mathbf x)$ or $e_n(\mathbf x)$, specify the collection and counted partitions. |
| “Independent components” in a product of boundaries | Product of component boundaries | Separate factors do not by themselves imply metric orthogonality or statistical independence. |
| “Form commutator” | Skew-symmetric difference $[X,Y]-[Y,X]$; for affine vectors, the circulation form $\omega(u,v)$ | The historical PMG name differs from the operator commutator $AB-BA$. The adopted circulation normalization contains no factor $1/2$. |
| “Graph boundary” without qualification | Marked set $B$ or algebraic boundary $\partial X$ | A vertex set differs from an exterior-algebra object. |
| “Boundary response” without qualification | Forest test response $\mathbf u_G$ or electrical matrix $\boldsymbol\Lambda_B$ | Forest selection and the relation between potentials and currents are different constructions. |
| “Dual boundary basis” | A basis dual with respect to a specified nondegenerate pairing | Coordinate duality for the forest pairing is not Laplacian-Greenian duality. |
| “Boundary passport” without qualification | Full forest, reduced linear, spanning-tree electrical data, or spectral passport | Sufficiency depends on the target characteristic and gluing rules; these data are not interchangeable. |

## Terminology of extensions

The following definitions are used in the published series “Spaces and Subspaces in PMG”. They extend the glossary; the required core definitions remain in the [[Core specification|specification]]. Conditions and examples are given in the linked notes.

| Term | Russian equivalent | Meaning and source |
| --- | --- | --- |
| Frame of an object | Фрейм объекта | A representation of an object as a linear combination of selected elements, including the elements and coefficients. The set may be dependent; different frames may represent one object. [[Projections, Bi-coordinates, and Di-coordinates#Bi-coordinates and frames]]. |
| Bi-coordinates | Би-координаты | Coefficients of the unique expansion of an object in a chosen basis of the corresponding linear space. A point basis is not required; barycentric coordinates of points are a special case. [[Projections, Bi-coordinates, and Di-coordinates#Bi-coordinates and frames]]. |
| Bi-coordinate matrix | Матрица би-координат | The matrix $\mathbf B$ of expansion coefficients of selected objects in a specified basis. Its definition must state whether the coordinates of each object occupy a row or a column. The influence matrix is a particular case. |
| Extended isotropic Gram matrix | Расширенный изотропный грамиан | The matrix $\mathbf G_z=G(a_1,\ldots,a_n,z)$ for local vertices and the null vector. With $z$ last, its blocks are $\left(\begin{smallmatrix}\mathbf G&\mathbf1\\\mathbf1^{\mathsf T}&0\end{smallmatrix}\right)$. [[The Null Vector, Isotropic Representation, and the Boundary#The vertex Gram matrix and the extended Gram matrix]]. |
| Di-coordinates | Ди-координаты | Inner products of an object with the elements of the chosen basis. When the metric on its subspace is nondegenerate, these are also the coefficients of the projection in the reciprocal basis. [[Projections, Bi-coordinates, and Di-coordinates#Di-coordinates: inner products]]. |
| Reciprocal basis | Взаимный базис | A basis of the same subspace whose inner products with the original basis elements are $1$ for matching indices and $0$ otherwise. It exists when the metric on the subspace is nondegenerate. [[Projections, Bi-coordinates, and Di-coordinates#The reciprocal basis]]. |
| Laplacian of a frame | Лапласиан фрейма | The difference part of the form decomposition for a fixed frame: $L_q=\sum_{i<j}q^iq^j[a_j-a_i]^2$. It may change with the frame and is not determined by the object $q$ alone. [[Projections, Bi-coordinates, and Di-coordinates#The difference part and the Laplacian of a frame]]. |
| Local element; local point | Локальный элемент; локальная точка | An element of unit affine weight and zero norm: $x\cdot z=1$, $x^2=0$. It represents a point in the isotropic model. [[The Null Vector, Isotropic Representation, and the Boundary#Local points]]. |
| Nonlocal element of unit weight | Нелокальный элемент единичного веса | An element $p$ with $p\cdot z=1$ and $p^2\ne0$. A PMG term in the isotropic model. [[Nonlocal Elements, Spheres, and Their Centers#Decomposing an element into its center and norm]]. |
| Local center | Локальный центр | The point $\pi(p)=p-p^2z/2$ for $p\cdot z=1$. Selecting the center is a nonlinear correction along $z$. [[Nonlocal Elements, Spheres, and Their Centers#Decomposing an element into its center and norm]]. |
| Sphere element | Элемент сферы | In the symmetric isotropic space, $S=O+\rho z/2$, where $O=\pi(S)$ is the local sphere center; $x\cdot S=0$ specifies its local points and $S^2=\rho$. The center $O$ is not identified with the centroid $h$. [[Nonlocal Elements, Spheres, and Their Centers#A sphere as an orthogonality condition]]. In a balanced graph, one sphere functional has two metric representatives. [[The Isotropic Space and Sphere of a Balanced Graph]]. |
| Distinguished null vector | Выделенный нуль-вектор | A nonzero element $z$ with $z^2=0$ that specifies the normalization of local points. It is not the zero element of the space. [[The Null Vector, Isotropic Representation, and the Boundary]]. |
| Isotropic element | Изотропный элемент | A nonzero linear element $u$ with zero norm $u\cdot u=0$, regardless of affine weight. Local elements are isotropic; the null vector $z$ is isotropic but not local, since its weight is $0$. [[The Null Vector, Isotropic Representation, and the Boundary]]. |
| Metric square | Метрический квадрат | A previous explanatory name for the norm $Y^2=Y\cdot Y$. The current text uses “norm”. It may be negative in an indefinite metric and differs from the form $[Y]^2$. |
| Orbital relative to the chosen extended basis | Орбиталь относительно расширенного базиса | The bi-coordinate along $z$ in the specified extended basis. It differs from the di-coordinate $Y\cdot z$. [[Projections, Bi-coordinates, and Di-coordinates#Coordinates in the isotropic extension]]. |
| Sub-basis | Суб-базис | A selected subset of a full basis that generates its own subspace. An object outside that subspace has no expansion in the sub-basis, although its di-coordinates relative to these elements are defined. [[Projections, Bi-coordinates, and Di-coordinates#The linear midpoint and its local center]]. |
| Resistance radius | Резистивный радиус | For a connected undirected graph, $\rho=R_{\mathrm{sph}}^2$ is the squared Euclidean circumradius of the resistance simplex. The forest formula is $\rho=\xi_1/3-H_2/12$. [[Resistance Radius - Forest Formula and Matroid Invariance]]. In the isotropic representation, $\rho=(\mathbf G_z^{-1})_{n+1,n+1}$; this algebraic normalization extends to balanced graphs, where it can differ from the squared radius of the Euclidean realization of the symmetric metric part. [[The Isotropic Space and Sphere of a Balanced Graph]]. |
| Resistance diameter | Резистивный диаметр | $D_{\mathrm{res}}=4\rho$. In the symmetric case it is the squared linear diameter of the circumsphere. The balanced model retains the algebraic normalization through $\rho$; generally different from the maximum pairwise resistance. [[Vertex Contraction and Graph Gluing#Resistance radius is additive]]. |
| Influence matrix | Матрица влияния | The matrix $\mathbf B$ of coefficients extending values from selected to internal vertices. Its rows give the bi-coordinates of projections. For a balanced graph, specify whether $\mathbf L$ or $\mathbf L^{\mathsf T}$ is used. [[Selected Vertices and the Dirichlet Problem]]. |
| Fundamental matrix | Фундаментальная матрица | $\mathbf{Fm}=\mathbf A^{-1}$, where $\mathbf A$ is the internal Laplacian block. For a connected undirected graph, it is also the Gram matrix of residual vectors; for a disconnected graph, the metric statement applies component by component. Invertibility requires every component to contain a selected vertex. [[Selected Vertices and the Dirichlet Problem]]. |
| Response matrix | Матрица отклика | The matrix $\boldsymbol\Lambda$ mapping prescribed boundary potentials to currents after solving the internal equations. The Laplacian of the effective network obtained by eliminating internal vertices, not merely of the subgraph on the remaining vertices. [[Vertex Elimination and Induced Couplings]]; [[en/Foundations/PMG terminology#Groves and electrical data|precise boundary conventions]]. |
| Common spanning-tree parameter of the two parts | Общий остовной параметр двух долей | The locally introduced normalization $J(G)$ of the spanning-tree coefficient of a bipartite graph. It can be computed through either part while retaining its original degrees. [[Couplings Within One Part of a Bipartite Graph]]. |

For extensions not yet developed here, including metric-value decompositions and interval forms, definitions and translations are added as the corresponding public sections are prepared. Published KVP/KVPOU definitions are given above. The following restrictions remain:

- “Cocenter” is not used as a synonym for centroid or as the name of a separate geometric center without a definition.
- For the linear operation $/$ in exponential duality, the terms exterior contraction and «внешнее удаление» are fixed. The historical expression «внешнее деление» without a definition does not automatically denote this operation; a different construction requires a separate comparison.
- “Duality” and “metric-value decomposition” require a definition of the particular construction; their meaning does not follow from the name alone.

## Usage rules and revision history

Russian texts use «остовной» in «остовной лес», «остовной 2-лес», and «остовной коэффициент»; the neuter form is «остовное дерево».

The first use of a PMG-specific term should include a definition or a precise link to one. Sharing a name with a term from another field does not replace a definition. Where needed, English text uses the qualifiers “polyform in PMG”, “polyform potential”, and “PMG form norm”.

Within a derivation, distinguish the graph $G$, a Gram matrix $\mathbf G$, and the Green matrix $\mathbf{Gr}$, formal forms from their numerical evaluations, and matrix multiplication from the polyform product. Renaming a mathematical object should include an explicit correspondence with the earlier name.

| Revision | Date | Content |
|---|---|---|
| 16 | 2026-10-30 | Replaced the internal series code in the revision history with its descriptive title. Definitions and terminology conventions are unchanged. Aligned with Russian revision 16. |
| 15 | 2026-10-30 | Added terminology of the completed “Boundary Polynomials and Graph Gluing” series: marked boundaries, full and reduced forest passports, tests, pairing radicals, groves, and electrical and spectral data. Distinguished states from forms, the two responses, minimality, and coordinate independence; clarified the effective network after vertex elimination. Aligned with Russian revision 15. |
| 14 | 2026-10-30 | Added terminology from the completed spectral series: modes, eigenspaces, projectors, diagonal forms and elementary symmetric grade polynomials, exterior powers, cones, and projections. Distinguished coordinate and resistance evaluations, polynomial symmetry and SPF invariance, and complementary dual directions. Aligned with Russian revision 14. |
| 13 | 2026-10-28 | Added matroid definitions, forest and edge parameter families, both toponome normalizations, first-kind and mixed-state potentials, and KVP/KVPOU. Aligned duality, conductor and edge effective resistance, and radius; removed stale qualifications. Aligned with Russian revision 13. |
| 12 | 2026-10-28 | Distinguished direct vertices from dual classes in the Greenian entry; aligned with Russian glossary revision 12 and linked the English series. |
| 11 | 2026-10-27 | Established the Laplacian-Greenian pair, vector first grades and boundary exponentials; distinguished the Green matrix, Greenian, dual representation, and mutual exponential duality. Aligned with Russian glossary revision 11. |
| 10 | 2026-10-25 | Added balanced graphs, rooted potentials, directional pairing, resistances, circulation, coordinates, and sphere representatives. Reserved $r_{ij}$ for one-way resistance; clarified symmetric formulas, Gram matrices, higher-grade norms, and radius. Aligned with Russian glossary revision 10. |
| 9 | 2026-10-22 | Added terminology for partition toponomes: positive type, the toponome of a chosen representation, the second-kind algebra, partial matchings and gluings, color classes, coefficient tables, and triangles. Distinguished polynomial notation, type multiplication, and ordinary polyform multiplication; clarified weight data and representation dependence. Aligned with Russian glossary revision 9, including the Russian adjective «остовной». |
| 8 | 2026-10-20 | Added collections, partitions, structural identities, SPF types, representation sizes, and combinatorial potentials. Distinguished metric potential, symmetric-sum size, and forest count; clarified indices of forest coefficients and $r$-Stirling numbers. Aligned exterior-product notation and project scope. Aligned with Russian glossary revision 7. |
| 7 | 2026-10-16 | Replaced the Green-matrix notation $\mathbf G$ with $\mathbf{Gr}=\mathbf L^+$; reserved $\mathbf G$ for Gram matrices with entries $g_{ij}$. Discontinued $\mathbf B$ for the local-vertex Gram matrix and distinguished $\mathbf G$, $\mathbf G_z$, and bi-coordinate matrices $\mathbf B$. Aligned with Russian glossary revision 6. |
| 6 | 2026-10-15 | Added the sphere element and links to the properties of nonlocal elements, completing alignment with Russian glossary revision 5. |
| 5 | 2026-10-15 | Replaced metric mass with resistance radius and explicitly defined resistance diameter. |
| 4 | 2026-10-15 | Established the PMG convention for quadratic and linear norms; clarified locality and isotropy. |
| 3 | 2026-10-15 | Simplified isotropic-model notation: local points, nonlocal elements, and local centers. Updated section links. |
| 2 | 2026-10-14 | Added terms from the published spaces series and links to their definitions. Clarified resistance terminology, bi-coordinates and di-coordinates, metric square, and norm. This English version follows Russian revision 2. |
| 1 | 2026-10-09 | First public core glossary, aligned with core specification revision 2 and the introductory series. Clarifies the levels of objects and evaluations, the spanning-tree coefficient, edge factors, and earlier names. This English version follows Russian revision 1. |

Internal glossary version 1.1 of 2026-09-21 was used as source material. Its information about extensions remains relevant to their later preparation, but does not automatically form part of the current core terminology. Earlier revisions are records of changes, not parallel terminology standards.
