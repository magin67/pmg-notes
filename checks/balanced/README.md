# Проверки примеров серии «Балансовые графы» / Balanced Graphs examples

`verify_examples.py` использует точную арифметику SymPy. Он независимо вычисляет гринианы и главные миноры, перечисляет ориентированные леса и деревья, проверяет средние степени, координаты сферы, вариацию одной дуги на 12 взвешенных балграфах и числа циклов перестановок при 2–7 вершинах. Дополнительные проверки относятся к новым примерам свёрток, проекций, балансировки и геометрии рисунков. Это воспроизводимые проверки конечных примеров, а не доказательство общих утверждений и не архив всех ранее проведённых экспериментов.

`verify_examples.py` uses exact SymPy arithmetic to independently compute Green matrices and principal minors, enumerate directed forests and trees, and check mean degrees, sphere coordinates, single-arc variations on 12 weighted balanced graphs, and permutation cycle counts for 2–7 vertices. Additional checks cover the new contraction, projection, balancing, and figure examples. These are reproducible finite checks, not proofs of general statements or an archive of every earlier experiment.

```sh
python -m pip install sympy
python checks/balanced/verify_examples.py
```

`generate_figures.py` строит девять новых пар SVG и исправленную пару рисунков взвешенного треугольника; сторонние библиотеки не нужны. По умолчанию пишет в корень репозитория. Для отдельного каталога укажите `--root PATH`.

`generate_figures.py` reproduces the nine new SVG pairs and the repaired weighted-triangle pair using only the Python standard library. It writes to the repository root by default; use `--root PATH` for a separate output directory.

```sh
python checks/balanced/generate_figures.py --root preview-output
```
