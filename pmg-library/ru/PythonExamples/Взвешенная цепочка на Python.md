---
title: "Взвешенная цепочка на Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-weighted-chain
lang: ru
description: "Лапласиан, сопротивления, токи и мощность цепочки с проводимостями 1 и 2."
order: 2
---

Пример воспроизводит цепочку $1-2-3$ с проводимостями $c_{12}=1$, $c_{23}=2$ из заметок [[Лапласиан - граф, электрическая сеть и квадратичная форма]] и [[Эффективное сопротивление и геометрия графа#Пример: цепочка из трёх вершин|Эффективное сопротивление и геометрия графа]]. Сопротивления вычисляются через метрическую полиформу; уравнения токов дают независимую проверку.

[[en/PythonExamples/Weighted Chain in Python|English]] · [[ru/PythonExamples/PythonExamples|Программные примеры]]

## Код и запуск

[Полная программа](https://github.com/magin67/polyform_algebra/blob/b5a4ccfd0207ef6250a97417834ff67b4d94482d/examples/introductory/note01_weighted_chain.py) и [тесты](https://github.com/magin67/polyform_algebra/blob/b5a4ccfd0207ef6250a97417834ff67b4d94482d/tests/introductory/test_weighted_chain.py) закреплены на ревизии `b5a4ccf`. Установка описана в [[Установка библиотеки и запуск примеров]]. Для этого примера нужна именно эта ревизия: в прежней `76c433d` файла цепочки ещё нет. В отдельной копии для примеров выполните `git fetch origin` и `git checkout b5a4ccfd0207ef6250a97417834ff67b4d94482d`.

Из корня репозитория с Python выбранного окружения:

```powershell
python -m examples.introductory.note01_weighted_chain
python -m pytest tests/introductory/test_weighted_chain.py -q
```

В Windows можно заменить `python` на `.\.venv\Scripts\python.exe`, в Linux/macOS - на `.venv/bin/python`. В Colab сначала выполните установку с клонированием исходников из общей инструкции, затем:

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "examples.introductory.note01_weighted_chain"],
    check=True,
)
```

Для собственных вычислений достаточно установки пакета и следующего фрагмента; клонирование требуется для готовых программ и тестов.

## От графа к метрической полиформе

Вес ребра означает проводимость. Сопротивления рёбер равны обратным величинам: $1$ и $1/2$. Прямого ребра $13$ нет.

```python
import networkx as nx
from polyform_algebra import Polyform, quForm

# Edge weights are conductances.
graph = nx.Graph()
graph.add_weighted_edges_from([(1, 2, 1), (2, 3, 2)])
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()

print("tau =", metric.potential(quForm.one()))
for i, j in [(1, 2), (2, 3), (1, 3)]:
    form = quForm([(points[i], points[j])])
    print(f"R{i}{j} =", metric.norm(form))
```

Форма $f_{ij}=[a_j-a_i]^2$ задаёт квадратичную форму ребра. Нильпотентность рёберных форм даёт

$$
L=f_{12}+2f_{23},\qquad
M=\exp L=(e+f_{12})(e+2f_{23})
$$
В программе это экспонента в алгебре форм, а не матричная экспонента. Величина `potential(quForm.one())` даёт остовной коэффициент, а `norm(form)` - нормированную метрическую оценку.

| Величина | Результат | Объяснение |
|---|---:|---|
| $\tau$ | $2$ | Единственное остовное дерево имеет вес $1\cdot2$ |
| $R_{12}$ | $1$ | Сопротивление первого ребра |
| $R_{23}$ | $1/2$ | Сопротивление второго ребра |
| $R_{13}$ | $3/2$ | Сумма последовательных сопротивлений |

Наличие сопротивления $R_{13}$ не означает наличие ребра $13$. В резистивном евклидовом представлении это квадрат расстояния; само расстояние равно $\sqrt{3/2}$.

## Матрица, токи и мощность

Метод `to_matrix()` возвращает матрицу и соответствие точек индексам. В порядке вершин $1,2,3$:

$$
\mathbf L=
\begin{pmatrix}
1&-1&0\\
-1&3&-2\\
0&-2&2
\end{pmatrix}
$$
Воспроизведём опыт первой заметки: вводим 2 А в вершину 1, выводим 2 А через вершину 3 и выбираем $\varphi_3=0$.

```python
import numpy as np

matrix, index = laplacian.to_matrix()
# Reorder rows and columns explicitly as vertices 1, 2, 3.
order = [index[points[label]] for label in (1, 2, 3)]
matrix = matrix[np.ix_(order, order)]
# Ground vertex 3 and inject 2 A at vertex 1.
current = np.array([2.0, 0.0, -2.0])
potential = np.append(np.linalg.solve(matrix[:2, :2], current[:2]), 0.0)
print("potentials =", potential)
print("power =", potential @ matrix @ potential)
```

Получаем

$$
\varphi=(3,1,0)^{\mathsf T},\qquad
I_{12}=I_{23}=2,\qquad
\mathcal Q=1(3-1)^2+2(1-0)^2=6
$$
Баланс мощности также даёт $\varphi^{\mathsf T}J=6$ и $I^2R_{13}=4\cdot3/2=6$. При проводимостях в сименсах потенциалы измеряются в вольтах, мощность - в ваттах. Численный решатель NumPy используется только в примере; общий интерфейс решения сети в библиотеку не добавляется.

## Проверки

Три математических теста проверяют матрицу и сопротивления, остовной коэффициент и разложение экспоненты, уравнения токов и три способа вычисления мощности. Независимый эталон строит лапласиан явно, без преобразования полиформ: его минор даёт $\tau$, а три решения с единичным током проверяют все пары сопротивлений. Общие проверки примеров дополнительно проверяют запуск модуля и отсутствие вывода при импорте.

**Статус: непосредственно вычислено.** На Python 3.12 прошли все 228 тестов проекта. Облачный запуск в Google Colab отдельно не проверялся. Вычисления используют существующую квадратичную алгебру и не расширяют её модель.
