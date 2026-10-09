---
title: PMG Terminology
date: 2026-10-09
updated: 2026-10-09
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: pmg-terminology
lang: en
description: "Terminology of the PMG core, Russian equivalents, and distinctions between formal objects, forms, and metric values."
order: 2
---

This glossary records the terminology of the [[Core specification|core specification]] and the [[PMG Introductory Series|introductory series]]. Each entry gives the English term, its Russian equivalent, and a brief definition. Applicability conditions and fundamental identities are specified in the core specification; proofs and examples appear in the introductory notes.

## Scope and terminology status

The main model is a finite connected undirected graph without loops, with positive conductances on existing edges. The algebraic definitions do not require a graph. The disconnected case is addressed in the specification.

The tables use three status labels:

- **Standard:** the term has its usual mathematical meaning in the stated field.
- **Qualified:** the term is established, but the object, convention, or normalization requires clarification here.
- **PMG:** a term or specialized usage adopted in the project.

Terminology status does not describe the proof status of a claim. English names for PMG-specific constructions are editorial recommendations, not claims of established usage.

The project name remains **Polyform Metric Geometry (PMG)**.

## Points, vectors, and exterior objects

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Basis vertex | Базовая вершина | PMG | An element $a_i$ of the fixed linearly independent basis of the formal space $V$. |
| Point | Точка | Qualified | An element $x=\sum_i x_i a_i$ with $\sum_i x_i=1$. Not every point is a basis vertex. |
| Affine weight | Аффинный вес | PMG | The value of the linear functional $\varepsilon(x)=\sum_i x_i$. It is neither an edge weight nor a physical mass. |
| Affine vector | Аффинный вектор | Qualified | An element $u\in W=\ker\varepsilon$. Within the core, “vector” may be used for brevity. |
| Vertex-pair vector | Вектор пары вершин | Qualified | The difference $a_{ij}=a_j-a_i=(ij)$. It is defined even without an edge; reversing the order changes its sign. |
| Space of affine vectors | Пространство аффинных векторов | Qualified | The $(n-1)$-dimensional subspace $W\subset V$ consisting of combinations with zero coefficient sum. |
| Exterior product; wedge product | Внешнее произведение | Standard | The operation $\wedge$ in the exterior algebra. Exchanging homogeneous objects introduces a sign depending on their grades. |
| Exterior-algebra element | Внешний объект | Qualified | An element of $\Lambda^kV$ or $\Lambda^kW$. It may be a linear combination of exterior products. |
| Decomposable exterior element | Простой внешний объект | Standard | An object expressible as one exterior product. The Russian adjective “простой” means decomposable here. |
| Grade | Грейд | Qualified | The exterior degree $k$ of an object in $\Lambda^kV$. For a form, it is the common grade of its arguments. |
| Simplex | Симплекс | Qualified | The formal expression $[a_1\ldots a_k]=a_1\wedge\cdots\wedge a_k$. Its grade is $k$; the geometric dimension of a nondegenerate simplex is $k-1$. |
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
| Polyform product | Произведение форм | PMG | The operation $[X,Y][A,B]=[X\wedge A,Y\wedge B]$. It is commutative and differs from matrix multiplication. |
| Unit form | Единичная форма | PMG | The grade-$0$ form $e=[1,1]$, the identity for the product of forms. |
| Form on boundaries | Форма на границах | PMG | A form with arguments in $\Lambda^kW$. These forms constitute the subalgebra on which the core's metric evaluation is defined. |
| Nilpotency | Нильпотентность | Standard | A positive power of an element being zero. For example, $([v]^2)^2=0$ for a vector $v$, although the form of a nonzero vector is itself nonzero. |

In the electrical part of the introductory series, “the quadratic form of the Laplacian” also denotes the numerical function $\varphi\mapsto\varphi^{\mathsf T}\mathbf L\varphi$. When it appears alongside the formal polyform $L$, the representation must be specified.

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
| Green matrix | Матрица Грина | Qualified | The matrix $\mathbf G=\mathbf L^+$. For a connected graph, it inverts the Laplacian on the zero-sum subspace and vanishes on constant columns. |
| Resistance matrix | Резистивная матрица | Standard | The matrix $\mathbf R=(R_{ij})$ of pairwise effective resistances. |
| Distance operator | Дистанционный оператор | Qualified | The linear operator $\mathcal D(B)_{ij}=B_{ii}+B_{jj}-2B_{ij}$. Applied to a Gram matrix, it gives squared distances. |
| Centering matrix; centering projector | Центрирующий проектор | Standard | The matrix $\mathbf J=I-\mathbf1\mathbf1^{\mathsf T}/n$. |
| Centroid | Центроид | Standard | The equal-weight mean of the points: $n^{-1}\sum_i a_i$. |
| Centering | Центрирование | Standard | Choosing the centroid as the origin in a Euclidean realization, so position vectors sum to zero. This introduces no new linear relation between formal basis vertices. |

When representations occur together, the polyform retains an ordinary letter and the matrix is bold: $L$ and $\mathbf L$. Where the matrix representation is unambiguous, the introductory notes may use ordinary letters $L,G,R$.

## Resistance geometry and metric evaluation

| English term | Russian equivalent | Status | Meaning and convention |
|---|---|---|---|
| Effective resistance | Эффективное сопротивление | Standard | The quantity $R_{ij}$ determined by the entire network and the vertex pair. In the resistance realization it is the squared Euclidean distance. |
| Resistance distance | Резистивное расстояние | Standard | Effective resistance $R_{ij}$ viewed as a metric on vertices. It does not mean $\sqrt{R_{ij}}$. |
| Resistance inner product | Резистивная метрика на векторах | Qualified | The inner product $u\cdot v=\mathbf u^{\mathsf T}\mathbf G\mathbf v$ on $W$. Unlike the preceding entry, this refers to a bilinear metric. |
| Resistance simplex | Резистивный симплекс | Qualified | A Euclidean simplex whose squared pairwise distances are $R_{ij}$. Its dimension in the main model is $n-1$. |
| Gram matrix | Матрица Грама; грамиан | Standard | The matrix of pairwise inner products of selected vectors. Not every Gram matrix is a Green matrix. |
| Mixed Gram determinant | Смешанный определитель Грама | Standard | The determinant of $(u_r\cdot v_s)$ for two ordered collections of equal size. |
| Induced inner product | Индуцированное скалярное произведение | Standard | The extension of the metric to $\Lambda^kW$ through mixed Gram determinants and bilinearity. |
| Squared norm of an exterior element | Квадрат нормы внешнего объекта | Standard | The number $X^2=X\cdot X=\lVert X\rVert^2$. For a decomposable object it is the squared volume of a parallelotope. |
| Metric evaluation of a form | Численная метрическая оценка формы | PMG | The linear evaluation $[X,Y]\mapsto X\cdot Y$ on forms on boundaries of a fixed grade. |

> [!info] Object, form, and number
> The notations $X$, $[X]^2$, and $X^2$ are distinct: they denote an exterior object, a formal quadratic form, and a numerical squared norm, respectively. The exterior product of an object with itself is written explicitly as $X\wedge X$.

The norm of a simplex boundary corresponds to the volume of a parallelotope. The squared volume of the $k$-dimensional simplex itself is the squared norm of its boundary divided by $(k!)^2$. The metric on boundaries does not automatically define the norm of a formal point or simplex outside $\Lambda^kW$.

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

In public notation, $\|X\|$ retains its usual Euclidean meaning. Use of the specialized term “form norm” should include its definition through the normalized potential. The numerical evaluation of a product of forms generally differs from the product of their evaluations.

## Earlier names and ambiguous usages

The following table also records earlier Russian usage, so that older research notes can be read consistently with the public core.

| Earlier or ambiguous name | Recommended expression | Reason for clarification |
|---|---|---|
| “2-вектор” | Vertex-pair vector, $a_{ij}=a_j-a_i$ | In English, 2-vector normally means an object of exterior grade $2$, whereas $a_{ij}$ has grade $1$. “Two-point vector” is acceptable when explicitly defined. |
| “Order” without specifying the object | Grade | A simplex and its boundary differ in grade by one. |
| “Кратность” of a linear element | Affine weight | The coefficient-sum functional need not take integer values. |
| “Остовное число” for a weighted graph | Spanning-tree coefficient | A weighted sum need not be an integer. “Spanning-tree count” is appropriate when counting trees. |
| “Резистенс” | Effective resistance | An abbreviated internal Russian term; public text preferably uses the full name. |
| “Матрица резистенсов” | Resistance matrix; «резистивная матрица» | Consistent naming with the introductory series. |
| “Двухлес” | Spanning 2-forest | The full name specifies that all vertices are included and there are two components. |
| “Связь-форма” | Specify $[a_{ij}]^2$, $c_{ij}[a_{ij}]^2$, or $e+c_{ij}[a_{ij}]^2$ | A pair form, a Laplacian contribution, and an exponential factor are different objects. |
| “Norm” without specifying the level | Euclidean norm of an object, squared norm, or normalized potential of a form | The quantities $\lVert X\rVert$, $\lVert X\rVert^2$, and a linear evaluation of a form must be distinguished. |
| “Potential of an object” | Potential of the form $f$ | The form being evaluated and the metric must be specified. |
| “Independent components” in a product of boundaries | Product of component boundaries | Separate factors do not by themselves imply metric orthogonality or statistical independence. |
| “Form commutator” | Skew-symmetric difference $[X,Y]-[Y,X]$ | The historical PMG name differs from the operator commutator $AB-BA$. The core requires no special name for this difference. |

## Terminology of extensions

The isotropic extension, the null vector, barycentric and metric dual coordinates, KVP/KVPOU, dual polyforms, toponomes, metric-value decompositions, and interval forms lie outside the current core specification. Their definitions and translations should be added to this glossary when the corresponding public sections are prepared.

Until then, the following restrictions apply:

- The “null vector” of the isotropic extension does not mean the zero element of a vector space.
- “Cocenter” is not used as a synonym for centroid or as the name of a separate geometric center without a definition.
- No translation of “внешнее деление” is fixed until the operation is formally compared with standard operations of exterior algebra.
- “Duality” and “metric-value decomposition” require a definition of the particular construction; their meaning does not follow from the name alone.

These are terminological restrictions, not definitions of the corresponding extensions.

## Usage rules and revision history

The first use of a PMG-specific term should include a definition or a precise link to one. Sharing a name with a term from another field does not replace a definition. Where needed, English text uses the qualifiers “polyform in PMG”, “polyform potential”, and “PMG form norm”.

Within a derivation, distinguish the graph $G$ from its Green matrix $\mathbf G$, formal forms from their numerical evaluations, and matrix multiplication from the polyform product. Renaming a mathematical object should include an explicit correspondence with the earlier name.

| Revision | Date | Content |
|---|---|---|
| 1 | 2026-10-09 | First public core glossary, aligned with core specification revision 2 and the introductory series. Clarifies the levels of objects and evaluations, the spanning-tree coefficient, edge factors, and earlier names. This English version follows Russian revision 1. |

Internal glossary version 1.1 of 2026-09-21 was used as source material. Its information about extensions remains relevant to their later preparation, but does not automatically form part of the current core terminology. Earlier revisions are records of changes, not parallel terminology standards.
