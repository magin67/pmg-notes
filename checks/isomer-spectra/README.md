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
