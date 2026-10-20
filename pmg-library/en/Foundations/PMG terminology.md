---
title: PMG Terminology
date: 2026-10-09
updated: 2026-10-20
revision: 8
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-terminology
lang: en
description: "Terminology of the PMG core and published series: objects, forms, metrics, collections, partitions, symmetric polyforms, and combinatorial potentials; Russian equivalents."
order: 2
---

This glossary records the terminology of the [[Core specification|core specification]], the [[PMG Introductory Series|introductory series]], and the published thematic series. Each entry gives the English term, its Russian equivalent, and a brief definition. Applicability conditions and fundamental identities of the core are specified in the core specification; definitions of extensions, proofs, and examples appear in the linked notes.

## Scope and terminology status

The main model is a finite connected undirected graph without loops, with positive conductances on existing edges. The algebraic definitions do not require a graph. The disconnected case is addressed in the specification.

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
| Skew-symmetric form | Антисимметричная форма | Qualified | A form $F$ satisfying $F^{\mathsf T}=-F$. Its evaluation under a symmetric metric is zero. |
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
| External combinatorial potential | Внешний комбинаторный потенциал | PMG | $e_n(\mathbf x)=\binom{n}{w(\mathbf x)}s_2(\mathbf x)$ for $w(\mathbf x)\leqslant n$: choosing a subset of the prescribed size and a partition of that subset of the prescribed type. The indexed function $e_n$ differs from the unit form $e$. [[Combinatorial Potentials in Symmetric Polyforms]]. |
| Forest coefficients | Лесные коэффициенты | PMG | The numbers $\operatorname{St}(k,m)$ count forests on $k$ labelled ordinary vertices and $m$ added unlabelled roots: each component has exactly one root, and no root is isolated. Here $m$ belongs to the auxiliary construction, rather than counting all components of the original graph on $n$ vertices. These numbers differ from $\tau(G)$ and ordinary Stirling numbers $S(k,m)$. [[Forest Coefficients and Abel Polynomials]]. |
| $r$-Stirling numbers of the second kind | $r$-числа Стирлинга второго рода | Standard | $\left\{\begin{smallmatrix}N\\K\end{smallmatrix}\right\}_r$ counts partitions of $N$ elements into $K$ nonempty blocks with $r$ specified distinct elements in different blocks. Here $N,K$ are full sizes; the shifted notation $c_r(w,m)$ means $N=w+r$, $K=m+r$. [[Falling Factorials, Rooted Forests, and Stirling Numbers]]. |

For $\mathbf x=[x_i]$ with positive integer parts, $w=w(\mathbf x)$, and multiplicity collection $\boldsymbol\mu=[\mu_j]_{j\in J}$, the formula is

$$
s_2(\mathbf x)=\frac{w!}{[x_i!]!\,[\mu_j!]!}
$$

A combinatorial potential counts partitions and uses no metric. The polyform potential $u_M(f)=\tau(Mf)$ is defined in a different sense, through the metric polyform. When applying $s_2$, specify whether its argument lists vertex-block sizes or parts of an auxiliary partition. For example, $\#E_5[2,1]=s_2([3,2])=10$, whereas the coefficient in $E_5[2,1]=3E_5[3]$ is $s_2([2,1])=3$. The corresponding forest count in $K_5$ is $30$.

The relation between forest coefficients and $r$-Stirling numbers is used here for specific PMG counts. A general classification of Stirling-number families belongs to a separate project on combinatorics and partition algebra.

## Graphs, couplings, and matrix representations

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Coupling coefficient | Коэффициент связи | PMG | The pair coefficient $c_{ij}$. In the main model it is symmetric and nonnegative. |
| Edge conductance | Проводимость ребра | Standard | The electrical interpretation of a positive coefficient $c_{ij}$. “Conductivity” is not used here. |
| Edge weight | Вес ребра | Standard | A general name for a numerical edge parameter. In this model the weight represents conductance, not length. |
| Weighted degree | Взвешенная степень вершины | Standard | The sum $d_i=\sum_jc_{ij}$. |
| Edge resistance | Собственное сопротивление ребра | Standard | The quantity $r_{ij}=1/c_{ij}$ for an existing edge. It may differ from the effective resistance of the same pair. |
| Graph Laplacian matrix | Матрица лапласиана | Standard | The matrix $\mathbf L$ with diagonal entries $d_i$ and off-diagonal entries $-c_{ij}$. |
| Laplacian polyform | Полиформа лапласиана | PMG | The grade-$1$ form $L=\sum_{i<j}c_{ij}[a_{ij}]^2$. |
| Reduced Laplacian | Редуцированный лапласиан | Standard | The matrix obtained by deleting the row and column of the same vertex from $\mathbf L$. |
| Green matrix | Матрица Грина | Qualified | The matrix $\mathbf{Gr}=\mathbf L^+$. For a connected graph, it inverts the Laplacian on the zero-sum subspace and vanishes on constant columns. It is the Gram matrix of vectors from the vertices to the centroid: $\mathbf{Gr}_{ij}=(b-a_i)\cdot(b-a_j)$, where $b=n^{-1}\sum_i a_i$. |
| Resistance matrix | Резистивная матрица | Standard | The matrix $\mathbf R=(R_{ij})$ of pairwise effective resistances. |
| Distance operator | Дистанционный оператор | Qualified | The linear operator $\mathcal D(A)_{ij}=A_{ii}+A_{jj}-2A_{ij}$. Applied to a Gram matrix, it gives squared distances. |
| Centering matrix; centering projector | Центрирующий проектор | Standard | The matrix $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$. |
| Centroid | Центроид | Standard | The equal-weight mean of the points: $n^{-1}\sum_i a_i$. |
| Centering | Центрирование | Standard | Choosing the centroid as the origin in a Euclidean realization, so position vectors sum to zero. This introduces no new linear relation between formal basis vertices. |

When representations occur together, the polyform retains an ordinary letter and the matrix is bold: $L$ and $\mathbf L$. Where the matrix representation is unambiguous, the introductory notes may use ordinary letters $L,G,R$.

## Resistance geometry and metric evaluation

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Effective resistance | Эффективное сопротивление | Standard | The quantity $R_{ij}$ determined by the entire network and the vertex pair. In the resistance realization it is the squared Euclidean distance. |
| Resistance distance | Резистивное расстояние | Standard | Effective resistance $R_{ij}$ viewed as a metric on vertices. It does not mean $\sqrt{R_{ij}}$. |
| Resistance inner product | Резистивная метрика на векторах | Qualified | The inner product $u\cdot v=\mathbf u^{\mathsf T}\mathbf{Gr}\mathbf v$ on $W$. Unlike the preceding entry, this refers to a bilinear metric. |
| Resistance simplex | Резистивный симплекс | Qualified | A Euclidean simplex whose squared pairwise distances are $R_{ij}$. Its dimension in the main model is $n-1$. |
| Gram matrix | Матрица Грама; грамиан | Standard | The matrix $\mathbf G=(g_{ij})$ of pairwise inner products of selected elements: $g_{ij}=a_i\cdot a_j$. With several sets, specify arguments or meaningful subscripts. For local vertices, $\mathbf G=-\mathbf R/2$. |
| Mixed Gram determinant | Смешанный определитель Грама | Standard | The determinant of $(u_r\cdot v_s)$ for two ordered collections of equal size. |
| Induced inner product | Индуцированное скалярное произведение | Standard | The extension of the metric to $\Lambda^kW$ through mixed Gram determinants and bilinearity. |
| Norm of an exterior element; quadratic norm | Норма внешнего объекта; квадратичная норма | PMG | The number $X^2=X\cdot X$. In the resistance metric it is also called the resistance norm. For a decomposable boundary object, it is the squared volume of a parallelotope. |
| Linear norm | Линейная норма | PMG | The quantity $\|X\|=\sqrt{X^2}$ for $X^2\ge0$. On a positive definite space, it agrees with the usual Euclidean norm. |
| Metric evaluation of a form | Численная метрическая оценка формы | PMG | The linear evaluation $[X,Y]\mapsto X\cdot Y$ on forms on boundaries of a fixed grade. |

> [!info] Object, form, and number
> The notations $X$, $[X]^2$, and $X^2$ are distinct: they denote an exterior object, a formal quadratic form, and a numerical norm, respectively. The exterior product of an object with itself is written explicitly as $X\wedge X$.

The norm of a simplex boundary is the squared volume of a parallelotope, while its linear norm is the volume itself. The squared volume of the $k$-dimensional simplex is the norm of its boundary divided by $(k!)^2$. The metric on boundaries does not automatically define the norm of a formal point or simplex outside $\Lambda^kW$.

## Metric polyforms, forests, and the spanning-tree coefficient

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Metric polyform | Метрическая полиформа | PMG | The exponential $M_G=\exp L$ in the algebra of forms. It is not the matrix exponential $\exp\mathbf L$. |
| Edge form; pair form | Форма связи | PMG | The quadratic form $[a_{ij}]^2$. Its weighted contribution to the Laplacian is $c_{ij}[a_{ij}]^2$. |
| Edge factor | Фактор-форма связи | PMG | The multiplier $e+c_{ij}[a_{ij}]^2$ in the factorization of $M_G$. “Фактор-форма” is the shortened Russian name. |
| Spanning tree | Остовное дерево | Standard | A connected acyclic subgraph containing every vertex of the original graph. |
| Spanning forest | Остовный лес | Qualified | In this series, any acyclic subgraph containing every vertex, including isolated ones. Maximality of the edge set is not required. |
| Spanning 2-forest | Остовный 2-лес | Standard | A spanning forest with exactly two components. |
| Separating spanning 2-forest | Разделяющий остовный 2-лес | Qualified | A spanning 2-forest in which two specified vertices lie in different components. |
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

## Potentials, norms, and variations

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Electrical potential | Электрический потенциал вершины | Standard | The value $\varphi_i$ in a solution of the network equations for specified input, subject to the freedom to choose a reference potential. |
| Polyform potential | Потенциал формы | PMG | The quantity $u_M(f)=\tau(Mf)$ for fixed $M$. It is not the electrical potential at a vertex. |
| Normalized polyform potential | Нормированный потенциал | PMG | The ratio $u_M(f)/u_M(e)=\tau(Mf)/\tau(M)$ when $\tau(M)\ne0$. |
| PMG form norm | Норма формы в PMG | PMG | An acceptable name for the normalized potential. For a general form this is a linear evaluation, not a norm in the usual sense. |
| Metric identity | Метрическое тождество | PMG | The equality between the normalized potential of $[X,Y]$ and the induced inner product $X\cdot Y$. |
| Conductance variation | Вариация проводимости | Standard | A change $c_{ij}\mapsto c_{ij}+t$. The main graph model requires nonnegative final conductance. |
| Algebraic Laplacian variation | Алгебраическая вариация лапласиана | PMG | An update $t[v]^2$ for arbitrary $v\in W$. In general it changes several pair coefficients. |
| Joint conductance variation | Совместная вариация связей | Qualified | Simultaneous changes in conductances of several vertex pairs; their interaction is determined by the Gram matrix of the corresponding vectors. |

For a quadratic form $[X]^2$, the normalized potential is $\|X\|^2$, not $\|X\|$. For a mixed form it can be negative even when the metric is positive definite. This does not mean that the exterior object has a negative norm.

In PMG, “norm” without the qualifier “linear” means the quadratic norm $X^2=X\cdot X$. The notation $\|X\|$ is reserved for the linear norm. The norm of a form is defined through the normalized potential; the evaluation of a product of forms generally differs from the product of their evaluations.

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
| “Form commutator” | Skew-symmetric difference $[X,Y]-[Y,X]$ | The historical PMG name differs from the operator commutator $AB-BA$. The core requires no special name for this difference. |

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
| Sphere element | Элемент сферы | A normalized element $S=h+\rho z/2$; for $\rho>0$, the local points on the sphere satisfy $x\cdot S=0$, its local center is $h$, and its norm is $S^2=\rho$. [[Nonlocal Elements, Spheres, and Their Centers#A sphere as an orthogonality condition]]. |
| Distinguished null vector | Выделенный нуль-вектор | A nonzero element $z$ with $z^2=0$ that specifies the normalization of local points. It is not the zero element of the space. [[The Null Vector, Isotropic Representation, and the Boundary]]. |
| Isotropic element | Изотропный элемент | A nonzero linear element $u$ with zero norm $u\cdot u=0$, regardless of affine weight. Local elements are isotropic; the null vector $z$ is isotropic but not local, since its weight is $0$. [[The Null Vector, Isotropic Representation, and the Boundary]]. |
| Metric square | Метрический квадрат | A previous explanatory name for the norm $Y^2=Y\cdot Y$. The current text uses “norm”. It may be negative in an indefinite metric and differs from the form $[Y]^2$. |
| Orbital relative to the chosen extended basis | Орбиталь относительно расширенного базиса | The bi-coordinate along $z$ in the specified extended basis. It differs from the di-coordinate $Y\cdot z$. [[Projections, Bi-coordinates, and Di-coordinates#Coordinates in the isotropic extension]]. |
| Sub-basis | Суб-базис | A selected subset of a full basis that generates its own subspace. An object outside that subspace has no expansion in the sub-basis, although its di-coordinates relative to these elements are defined. [[Projections, Bi-coordinates, and Di-coordinates#The linear midpoint and its local center]]. |
| Resistance radius | Резистивный радиус | The squared linear circumradius of the basis: $\rho=R_{\mathrm{sph}}^2$. A PMG definition. [[Vertex Contraction and Graph Gluing#Resistance radius is additive]]. |
| Resistance diameter | Резистивный диаметр | $D_{\mathrm{res}}=4\rho=(2R_{\mathrm{sph}})^2$. The squared linear diameter of the circumsphere; generally different from the maximum pairwise effective resistance. [[Vertex Contraction and Graph Gluing#Resistance radius is additive]]. |
| Influence matrix | Матрица влияния | The matrix $\mathbf B$ extending values from selected to internal vertices. Its rows give the bi-coordinates of the projections of internal vertices. [[Selected Vertices and the Dirichlet Problem]]. |
| Fundamental matrix | Фундаментальная матрица | $\mathbf{Fm}=\mathbf A^{-1}$, where $\mathbf A$ is the internal Laplacian block. For a connected graph, it is also the Gram matrix of residual vectors; for a disconnected graph, the metric statement applies component by component. Invertibility requires every component to contain a selected vertex. [[Selected Vertices and the Dirichlet Problem]]. |
| Response matrix | Матрица отклика | The matrix $\boldsymbol\Lambda$ mapping prescribed values at selected vertices to the response after solving the internal equations. It equals the Laplacian of the induced graph. [[Vertex Elimination and Induced Couplings]]. |
| Common spanning-tree parameter of the two parts | Общий остовной параметр двух долей | The locally introduced normalization $J(G)$ of the spanning-tree coefficient of a bipartite graph. It can be computed through either part while retaining its original degrees. [[Couplings Within One Part of a Bipartite Graph]]. |

For other extensions, including KVP/KVPOU, dual polyforms, toponomes, metric-value decompositions, and interval forms, definitions and translations are added as the corresponding public sections are prepared. The following restrictions remain:

- “Cocenter” is not used as a synonym for centroid or as the name of a separate geometric center without a definition.
- No translation of “внешнее деление” is fixed until the operation is formally compared with standard operations of exterior algebra.
- “Duality” and “metric-value decomposition” require a definition of the particular construction; their meaning does not follow from the name alone.

## Usage rules and revision history

The first use of a PMG-specific term should include a definition or a precise link to one. Sharing a name with a term from another field does not replace a definition. Where needed, English text uses the qualifiers “polyform in PMG”, “polyform potential”, and “PMG form norm”.

Within a derivation, distinguish the graph $G$, a Gram matrix $\mathbf G$, and the Green matrix $\mathbf{Gr}$, formal forms from their numerical evaluations, and matrix multiplication from the polyform product. Renaming a mathematical object should include an explicit correspondence with the earlier name.

| Revision | Date | Content |
|---|---|---|
| 8 | 2026-10-20 | Added collections, partitions, structural identities, SPF types, representation sizes, and combinatorial potentials. Distinguished metric potential, symmetric-sum size, and forest count; clarified indices of forest coefficients and $r$-Stirling numbers. Aligned exterior-product notation and project scope. Aligned with Russian glossary revision 7. |
| 7 | 2026-10-16 | Replaced the Green-matrix notation $\mathbf G$ with $\mathbf{Gr}=\mathbf L^+$; reserved $\mathbf G$ for Gram matrices with entries $g_{ij}$. Discontinued $\mathbf B$ for the local-vertex Gram matrix and distinguished $\mathbf G$, $\mathbf G_z$, and bi-coordinate matrices $\mathbf B$. Aligned with Russian glossary revision 6. |
| 6 | 2026-10-15 | Added the sphere element and links to the properties of nonlocal elements, completing alignment with Russian glossary revision 5. |
| 5 | 2026-10-15 | Replaced metric mass with resistance radius and explicitly defined resistance diameter. |
| 4 | 2026-10-15 | Established the PMG convention for quadratic and linear norms; clarified locality and isotropy. |
| 3 | 2026-10-15 | Simplified isotropic-model notation: local points, nonlocal elements, and local centers. Updated section links. |
| 2 | 2026-10-14 | Added terms from the published spaces series and links to their definitions. Clarified resistance terminology, bi-coordinates and di-coordinates, metric square, and norm. This English version follows Russian revision 2. |
| 1 | 2026-10-09 | First public core glossary, aligned with core specification revision 2 and the introductory series. Clarifies the levels of objects and evaluations, the spanning-tree coefficient, edge factors, and earlier names. This English version follows Russian revision 1. |

Internal glossary version 1.1 of 2026-09-21 was used as source material. Its information about extensions remains relevant to their later preparation, but does not automatically form part of the current core terminology. Earlier revisions are records of changes, not parallel terminology standards.




