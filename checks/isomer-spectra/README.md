# Exact checks for “Spectra of Isomers”

The Russian note is `pmg-library/ru/Инварианты, разложения и спектры/Спектры изомеров/Два изомера трёх шестиугольников.md`.
The input consists solely of the explicitly listed cycles, with shared edges counted once.

## Reproduction

Python 3.10+ and SymPy are required for the exact checks. Verified with Python 3.12.1 and SymPy 1.14.0.

```text
python -m pip install sympy==1.14.0
python checks/isomer-spectra/verify_three_hexagons.py
python checks/isomer-spectra/draw_three_hexagons.py
```

The drawing script uses only the Python standard library. The scripts resolve their output locations relative to their own files and may be invoked from any working directory using the appropriate paths.

The verification prints:

```text
PASS: both determinants, 131072 edge subsets, radii, forest types, traces, and symbolic Schur proof.
```

## Independent methods

1. Construct each 14-by-14 Laplacian from the edge set and compute the symbolic determinant of `xi*I-L` by exact domain elimination. Compare it with SymPy's characteristic polynomial and with `det(I+t*L)`.
2. Enumerate all 65,536 edge subsets of each graph, rejecting cycles by union-find. For each spanning forest record its edge count, its ordinary weight 1, and its rooted weight (the product of component sizes, including isolated vertices). This calculation does not use a determinant, transfer rule, or conjectured difference formula. Compare every coefficient.
3. Count four-edge forests by their component sizes. Verify the fourth spectral moment independently through degree products along edges and through matrix powers.
4. Check the spanning-tree cofactor and the PMG resistance radius using the reduced-Laplacian energy and the inverse resistance matrix. Compute the Kirchhoff index directly from pairwise resistances.
5. Symbolically verify the four-vertex Schur block, its endpoint inverse entries, both reduced six-vertex determinants with independent variables, their squared difference, the continuant identity, and the recovery of each complete characteristic polynomial.
6. Check the factorization of the difference as the square of the Laplacian characteristic polynomial of `C5`, the greatest common divisor `xi`, and the `P7` characteristic factor of the straight chain.

All mathematical checks use integers, rational numbers, or exact polynomial expressions. Floating-point coordinates occur only in the illustrations.

## Outputs and scope

- `three-hexagons-results.json`: complete edge lists and Laplacians; characteristic polynomials and factorizations; ordinary and rooted forest coefficients; four-edge component counts; radius, spanning-tree count, Kirchhoff index, and spectral moments.
- Three SVG files beside the Russian note: seam geometry and the degree-three induced subgraphs; rooted forest weights; Schur elimination and reduced matrices.

The two graphs have `tau=204`, `rho=43595/41616`, and equal ordinary forest polynomials. Their characteristic difference is `xi^2*(xi^2-5*xi+5)^4`; the first rooted difference is `p4(A)-p4(B)=1`.

The determinant identity in the note is proved algebraically. Exhaustive forest enumeration independently checks this particular pair. Neither calculation asserts transfer closure, injectivity for longer chains, or scientific priority.

## Transfer to a new boundary

The second Russian note is `pmg-library/ru/Инварианты, разложения и спектры/Спектры изомеров/Спектральный перенос при смене границы.md`.

```text
python checks/isomer-spectra/verify_boundary_transfer.py
python checks/isomer-spectra/draw_boundary_transfer.py
```

The drawing script imports the standard-library SVG helper from `draw_three_hexagons.py`; keep the scripts together. It creates four SVG files beside the second note: the transfer mechanism, three ordered exits of a hexagon, different continuations of the same two-hexagon graph, and a transfer at a zero of the old interior minor.

The verification derives each transfer row by symbolic determinant expansion in a symmetric two-by-two input block. It also recovers every coefficient from five exact evaluations of that block. Independently, it builds the complete glued graph and compares all five direct determinants/cofactors with the transferred state:

- 64 overlapping-boundary cases: every pair of simple graphs on three vertices, including disconnected graphs and isolated vertices;
- 64 disjoint-boundary cases: each old three-vertex graph combined with a four-vertex kernel containing a fixed path and any subset of its three remaining edges;
- 32 weighted cases: rational conductances, either one shared edge or separate parallel copies, and four choices of output pair, including the input pair in both orders;
- the same 32 weighted results with a nontrivial permutation of all vertices, checking cofactor signs;
- the exact singular example `E_old(2)=0`, joining two paths to `C5`;
- all five polynomial coordinates for the 13 words of length 0, 1, or 2 over the exits 2, 3, 4 (one to three hexagons);
- 15 direct integer checks: five specified longer words at `xi=-1,0,2`, up to eight hexagons (34 vertices).

The script verifies the compact recurrences, reflection identities, initial state, state-difference identity, and both complete characteristic polynomials against the independently generated `three-hexagons-results.json`. It also verifies the rooted specialization and its terminal row through the exact transfer matrices.

The output `boundary-transfer-results.json` records all three polynomial transfer matrices, the initial state, their normalized specialization at `xi=-1`, both two-hexagon states, and the test counts. The input convention is `(0,1)=(a,b)`, the output is `(j,j+1)`, and a shared unit edge is counted once. Reversing only the input changes `T_j` to `T_j J`, not to `J T_j J`.

Closure for every two-vertex attachment satisfying the note's conditions is proved algebraically in the note. These finite checks validate formulas and implementation; they do not prove minimality or injectivity of the state, characteristic polynomial, or one numerical value.

## SLR codes, reflection, and reversal

The third Russian note is `pmg-library/ru/Инварианты, разложения и спектры/Спектры изомеров/SLR-код гексагональных цепочек.md`.

```text
python -m pip install sympy==1.14.0 networkx==3.6.1
python checks/isomer-spectra/verify_slr_code.py
python checks/isomer-spectra/draw_slr_code.py
```

The code is `w=S u`, where the first `S` is a marker and `len(u)=N-2`. The builder identifies the new local `(0,1)` with the old `(b,a)`, assigns four new vertex IDs, and uses exits 2, 3, or 4 for `L`, `S`, or `R`. A final attachment completes the graph; its opposite free edge is selected only to define the final passport. No geometric coordinate is used to identify graph vertices.

The test constructs all 364 words for two to seven cores. A bounded DFS on the adjacency lists recovers all six-edge cycles independently of the supplied core list. Exact graph isomorphism partitions the graphs without consulting their code or spectra; a Weisfeiler-Lehman hash is used only to reduce candidate comparisons, and every accepted match is checked by graph isomorphism. The resulting partition is compared with the complete four-element code orbits. Reflection and reversal are also checked by 728 explicit bijections with equality of all mapped edge sets.

The 121 words through six cores are checked against complete exact Laplacian characteristic polynomials. All five direct polynomial minors/cofactors are checked for the 13 words through four cores. The test verifies the symbolic transfer reflection identity, code symmetry, the input-order error at `SLL`, and the two different terminal passports of `SLS` and `SSR`, including both boundaries in one labelled graph. It also checks the exact center displacement in the regular development of `SLLLL`: this development has an extra contact that is excluded from the abstract model. Code orbits are additionally enumerated through ten cores and compared with the Burnside formula.

`slr-code-results.json` contains the finite-check counts, example values and full edge sets, terminal states, and explicit isomorphisms for the four words in the `SLS` orbit. Four SVG files illustrate local turns and seam order, a symmetry orbit, the four classes with four cores, and different passports at opposite ends. The drawing script uses only the standard-library helper and does not require NetworkX or SymPy.

The note proves the graph classification only for abstract open chains of hexagons with disjoint edge seams and no other identifications. It does not establish injectivity of the spectral state, the characteristic polynomial, or its value at `xi=-1`.

## Спектральные разности SLR-цепочек

Из корня репозитория:

```console
python checks/isomer-spectra/verify_spectral_differences.py
python checks/isomer-spectra/draw_spectral_differences.py
```

Проверено на Python 3.12.1, SymPy 1.14.0 и NetworkX 3.6.1. Расчёт использует
только точные целые числа и полиномы; программа рисунков использует стандартную
библиотеку Python и сохранённые результаты.

- Независимые полные характеристические полиномы: все 121 слово при 2 ≤ N ≤ 6.
- Все 426 однобуквенных замен и 64 смешанные разности по двум выбранным позициям
  на этом наборе; фиксированные промежутки сохраняются в произведении матриц.
- Прямые спектральные моменты и число рёбер между вершинами степени 3:
  все 364 слова при 2 ≤ N ≤ 7. Для 121 полинома проверены тождества Ньютона
  и общий младший коэффициент −nτ.
- Две разные рекурсии: обычные S/L-замены и замены с дополнительной
  перестановкой границы. Прямые знакопеременные суммы проверены до r=4,
  полиномиальные последовательности до r=8; общие матричные тождества проверены
  символьно. Конечные проверки не подменяют доказательств в заметке.
- Факторизации примеров, отсутствие универсальной делимости на χ(C5)²,
  одна телескопическая разность с заменой всех букв.

`spectral-differences-results.json` сохраняет матрицы разности, факторизации,
коэффициенты, значения при ξ=−1, списки рёбер примеров и счётчики проверок.
Числа на рисунках берутся из этого файла. Полные спектральные паспорта,
характеристические полиномы и одно числовое значение не смешиваются как
критерии восстановления.

## Корневые леса и декодирование граничного состояния

Из корня репозитория:

```console
python -B checks/isomer-spectra/verify_decoding.py
python -B checks/isomer-spectra/draw_decoding.py
```

Используются Python 3.12, SymPy 1.14.0 и NetworkX 3.6.1 из предыдущих проверок.
Нужны соседние файлы `verify_slr_code.py`, `verify_boundary_transfer.py` и
`boundary-transfer-results.json`; рисунки используют стандартные SVG-помощники
из `draw_three_hexagons.py` и `draw_slr_code.py`.

`verify_decoding.py` специализирует полиномиальные переходы при ξ=-1 с поправкой
знаков R=diag(1,-1,-1,-1,1). Проверяются определители 1, целочисленные обратные
матрицы, квадратичное тождество Якоби, точные рациональные запасы всех неравенств
на 16 вершинах нормированного прямоугольника и строгие знаки трёх секторов.
Аффинность проверяемых неравенств делает эти сертификаты проверкой общей леммы.

Независимо строятся 14 полных паспортов I+L: один C6 и все 13 слов поворотов
длины 0–2. Для C6 и кодов S, SS, SL отдельно перебираются 133184 подмножества
рёбер (включая отброшенные циклические); корни считаются по размерам компонент.
Все пять координат сопоставляются с прямыми минорами и переносом.

Декодируются все 88573 слова операций длины 0–10. Проверяются отсутствие
совпадений, остановка на начальном состоянии, отказ для 2z0, пример SLR и
конечное соглашение: полный код Su имеет слово операций uS, поэтому после
декодирования удаляется конечное S и добавляется начальный маркер S.

`decoding-results.json` содержит рациональные сертификаты, матрицы и их
обратные, точные состояния, лесные подсчёты и счётчики. Три SVG иллюстрируют
лесной смысл координат, разделение секторов и обратный расчёт для SLR.
Числовые подписи берутся из результатов проверки; только размещение точек
и вершин рисунков использует приближённые координаты.

Инъективность полного отмеченного состояния для любой длины доказана в тексте
через инвариантную область и обратные переходы. Конечный перебор проверяет
реализацию. Инъективность одного характеристического полинома или значения
P(1), минимальность линейного состояния и другие классы цепочек не заявляются.

## Восстановление цепочки по граничному отклику

Из корня репозитория:

```console
python -B checks/isomer-spectra/verify_boundary_response.py
python -B checks/isomer-spectra/draw_boundary_response.py
```

Проверка использует Python 3.12, SymPy 1.14.0 и NetworkX 3.6.1; научные графики
в программе рисунков построены Matplotlib 3.8.2. Остальные элементы рисунков -
обычный SVG. Нужны соседние проверочные программы и файлы результатов из
раздела о корневом декодировании.

- Точные сертификаты сжатия нормированных переходов на всём четырёхмерном
  прямоугольнике: аффинные числители производных проверяются в его 16 вершинах,
  знаменатели ограничиваются снизу. Проверяются также запасы секторных
  неравенств, отделение начального состояния и обусловленность матрицы отклика.
- Независимые электрические уравнения, дополнения Шура и вероятности остановки
  строятся из рёбер для 14 графов. Для C6, S, SS, SL заново перебираются все
  133184 подмножества рёбер, включая отброшенные циклические, и считаются корни.
- Для 9841 полного отмеченного состояния (2 ≤ N ≤ 10), а также отдельного C6
  восстанавливаются примитивный целый вектор и полный код из трёх рациональных
  элементов отклика и из совместного распределения двух корневых индикаторов.
  При восстановлении масштаба учитывается знаменатель det K, а не только
  знаменатели трёх непосредственно заданных элементов.
- Для прямой цепочки и одного удалённого изгиба точно вычислены расстояния
  откликов при 3 ≤ N ≤ 14 и проверена общая верхняя оценка. Полный каталог
  при N ≤ 7 содержит 365 отмеченных состояний; сохранены минимальные расстояния,
  пример единственного кандидата и пример двух совместимых неизоморфных цепей.
- Интервальный прототип отслеживает гарантированное включение истинного
  промежуточного состояния и корректность снятых букв. Он прекращает проверку,
  если нельзя исключить начальное состояние, выбрать сектор или доказать
  положительность делителя. Такая остановка не доказывает неоднозначности.

`boundary-response-results.json` содержит все точные дроби, матрицы примеров,
сертификаты, каталожные проверки и трассы интервального прототипа. Шесть SVG
показывают динамический отклик исходного графа, одинаковое конечное
сопротивление, вспомогательные электрические опыты, два вероятностных прочтения,
ослабление удалённого изгиба и разные исходы восстановления с погрешностью. Приближённые
числа используются только для подписей и графического изображения.

Редакция 2 отличает исходный граф от вспомогательного графа с общей вершиной.
Число трёх элементов симметричного паспорта не связано с минимальной степенью 3.
Дополнительные проверки `original_graph_models` работают на исходном графе:

- Для C6 и всех 40 полных кодов при 2 ≤ N ≤ 5 непосредственно решаются узловые
  уравнения. Проверяются степень 2 обоих контактов, обычный двухточечный отклик
  ранга 1 и рекурсия R_N=(4+R_(N-1))/(5+R_(N-1)), R_1=5/6.
- Для C6 точная матрица тепловой эволюции проверяется по начальному условию и
  дифференциальному уравнению. Взвешенные интегралы собственных и перекрёстных
  температур равны 9/20 и 7/40.
- Для 14 графов U=I-L/3 является стохастической матрицей. Проверяются 32 члена
  точного ряда (1/4) sum_(k≥0) (3U/4)^k = (I+L)^(-1), получаемого интегрированием
  равномеризованной тепловой полугруппы, и покоординатная граница остатка (3/4)^32.
  Это рациональные сертификаты, а не приближённая квадратура временных кривых.

Динамическая интерпретация требует известных единичных теплоёмкостей и
теплопроводностей. Вес exp(-t) вводится при обработке записей; новых рёбер и
физической утечки нет. В заметке отдельно оценены хвост конечной записи и
ошибка интегрируемых данных. Эти оценки относятся к извлечению K, а не к
оптимальному декодированию непосредственно по полным временным кривым.

Точные теоремы относятся к принятому классу открытых цепей C6 с единичными
весами и канонической упорядоченной конечной границей. Сжатие даёт отсутствие
общей положительной точности для всех длин; при N ≤ M приведена грубая
положительная оценка. Минимальность данных, оптимальная устойчивость,
произвольные сети и инъективность одного спектрального полинома не заявляются.

## SLR-плетение и постоянный поворот

Заметка: `Плетение SLR-цепочек и постоянный поворот.md` в русской серии
«Спектры изомеров». Планарность и геометрические координаты не входят
в математическую модель. Бегунок P6 имеет шесть вершин и пять рёбер;
его вилка (1,0) и розетки L=(2,3), S=(3,4), R=(4,5) упорядочены.

```text
python -B checks/isomer-spectra/verify_slr_weaving.py
python -B checks/isomer-spectra/draw_slr_weaving.py
```

Для проверок нужны SymPy и NetworkX; для рисунков также NumPy.
Все математические проверки целочисленные или полиномиальные:

- три перехода независимо получены из определителей пути без входного ребра;
- все 121 SLR-слов с 2–6 ядрами сопоставлены с построением из путей,
  включая упорядоченную конечную границу;
- 14 графов с другим фиксированным соответствием входа проверяют чередование L/R;
- 18 полных характеристических полиномов постоянных S- и L-семейств
  с 0–8 ядрами проверены непосредственно по спискам рёбер;
- 8 полных полиномиальных паспортов, 18 определителей I+L и 18 остовных
  кофакторов независимо проверяют перенос и числовые таблицы;
- характеристические полиномы матриц, коэффициенты a,b, постоянный остаток,
  рекурсии и ненулевые миноры Ганкеля проверены точно;
- 8 отмеченных отражений и 5 определителей для повторяемого блока LR
  проверяют симметрию и порядок произведения матриц.

`slr-weaving-results.json` содержит коэффициенты, полные четыре начальных
полинома каждого семейства, целые последовательности и сертификаты
минимальных порядков 4 и 5. Минимальность относится к однородным скалярным
рекурсиям с коэффициентами, не зависящими от числа ядер.

Четыре SVG показывают три размеченных бегунка, прямую цепочку и зигзаг
вместе с пространственной спиралью, два соответствия контактов и составной
периодический бегунок. Спираль построена из того же абстрактного графа:
новый путь расположен между последовательными парами контактов винтовой
линии. Равенство геометрических длин рёбер и плоскость ячеек не предполагаются;
проводимости остаются единичными. Численные координаты используются только
для рисунка, его графовая изоморфность проверяется отдельно.

## Спектральная различимость SLR-цепочек

Заметка: `Спектральная различимость SLR-цепочек.md` в русской серии
«Спектры изомеров». Доказательства для всех длин отделены от конечного
каталога и двух гипотез инъективности.

```text
python -B checks/isomer-spectra/verify_spectral_distinguishability.py
python -B checks/isomer-spectra/catalog_spectral_values.py --max-n 18
python -B checks/isomer-spectra/draw_spectral_distinguishability.py
```

Для независимых проверок нужны SymPy и NetworkX. Большой перебор использует
только стандартную библиотеку Python и целые числа произвольной длины.
В памяти хранится словарь точных значений для одного размера: при N=18
это 10 764 961 записей. Для сокращённого запуска можно указать `--max-n 12`;
он перезапишет файл каталога результатом меньшего диапазона.

- Для всех 1093 ориентированных слов при 2 ≤ N ≤ 8 непосредственно из
  графов вычисляются следы L^1,...,L^8, степени вершин, типы рёбер и сумма
  квадратов сумм соседних степеней. Проверяются общие формулы до s6.
- Быстрые целочисленные переходы на том же наборе сверяются с исходными
  полиномиальными переходами при ξ=-1.
- Для всех 42 классов при 2 ≤ N ≤ 6 вычисляются полные характеристические
  полиномы по лапласианам. Для них и 36 графов с 7-18 ядрами независимо
  вычисляются 78 определителей I+L.
- Примеры проверяются по точным полиномиальным разностям, их степеням
  и графовой изоморфности. Сохраняются полные полиномы и списки рёбер.
- `verify_distinguishability_proofs.py` проверяет символьную арифметику
  доказательств, связь p6 с h и достаточную оценку принципа Дирихле
  для k=10, N=152. Общий подсчёт приведён в тексте, а не заменён примером.
- Большой каталог содержит 16 150 725 представителей доказанных орбит
  при 2 ≤ N ≤ 18. Он сверяет числа классов с формулой Бёрнсайда,
  сравнивает полные целые значения P(1), записывает все совпадения,
  минимумы и максимумы, а также проверяет разделение диапазонов разных N.

`spectral-distinguishability-results.json` содержит независимые проверки,
`slr-distinguishability-catalog.json` - агрегаты полного перебора.
Отсутствие совпадений P(1) доказывает отсутствие совпадений полиномов
на проверенном конечном наборе, но не инъективность для всех длин.
Скалярные гипотезы относятся к неотмеченным графам; теорема декодирования
пяти координат относится к ориентированному отмеченному состоянию.

Три SVG показывают вклад соседних одинаковых поворотов, пары с совпадающими
начальными коэффициентами и различие трёх задач восстановления. Для всех
шести изображённых графов списки рёбер сверяются с построением из циклов;
отсутствие совпадающих координат разных вершин проверяется отдельно.

## Периодические SLR-цепочки

Заметка: `Периодические SLR-цепочки - рекурсии и спектры.md`.
Основное семейство имеет внутреннее слово v^m, N=|v|m+2 ядра
и перенос r V^m s1. Повторение бегунка от ребра имеет N=|v|m
и другие начальные условия. Рассмотрены LR, SL, LLS и все их фазы.

```text
python -B checks/isomer-spectra/verify_periodic_slr.py
python -B checks/isomer-spectra/draw_periodic_slr.py
```

Для проверок нужны SymPy и NetworkX; для графика роста также Matplotlib.
`periodic-slr-results.json` сохраняет коэффициенты, полные полиномы,
целые последовательности, правые части для разных концов и фаз,
определители Ганкеля и производящие функции.

- Полиномиально проверяются сохранение AE-BC+D², единичные определители
  трёх переходов и взаимно обратные характеристические полиномы периодов.
- Коэффициенты в переменной x=ξ-2 независимо переписаны из текста и
  сверяются с вычисленными следами и постоянными правыми частями.
- Непосредственно из лапласианов вычисляются 35 полных полиномов
  цепочек с двумя крайними ядрами (семь фаз, 0≤m≤4, до N=14, n=58)
  и 28 полиномов для бегунков от ребра (0≤m≤3). Этот счёт включает
  повторения одного графа при разных фазах и общие начальные графы.
- Проверяются сопряжение фаз, первые различающиеся коэффициенты,
  графовая изоморфность и сертификаты минимальности пятого порядка.
- Пять точных тождеств r V^j (V-I)^3 s1=0 при ξ=2, j=0,...,4,
  вместе с Кэли-Гамильтоном доказывают специальные формулы для всех m.
- Производящие функции проверяются по целым последовательностям;
  взаимная простота числителя и знаменателя подтверждена точно.
  Показатели роста заданы алгебраическими выражениями, десятичная
  запись используется только для таблицы и рисунка.

Три SVG показывают два соглашения о крайних ядрах, три фазы LLS
и рост корневых лесов на одно ядро. Для всех пяти нарисованных графов
инцидентность сверяется с независимым построением. Геометрические
координаты не входят в определение цепочек; требования планарности нет.

## Итоговый навигатор

`Спектры изомеров - результаты и открытые вопросы.md` сводит девять
содержательных заметок, статусы результатов, атрибуцию и маршруты чтения.
Новых математических вычислений навигатор не добавляет. Схема связей
воспроизводится средствами стандартной библиотеки Python:

```text
python -B checks/isomer-spectra/draw_series_overview.py
```

Стрелки показывают связи задач и данных. Эквивалентность полного целого
вектора и трёх точных рациональных данных относится к достижимым состояниям
принятого класса SLR-цепочек. Скалярные обратные задачи помечены гипотезами.
