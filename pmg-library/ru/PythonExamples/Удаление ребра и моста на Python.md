---
title: "Удаление ребра и моста на Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-edge-deletion
lang: ru
description: "Удаление ребра цикла и моста, сохранение вершин и границы нормировки метрической полиформы."
order: 6
---

Пример иллюстрирует правило удаления связи из [[Экспонента лапласиана#Добавление и удаление ребра|Экспоненты лапласиана]]. Рассматриваются два случая: удаление ребра $12$ из единичного $C_4$ и удаление моста $23$ проводимости 2 из цепочки с проводимостями 1 и 2. Во втором случае граф становится несвязным.

[[en/PythonExamples/Deleting an Edge and a Bridge in Python|English]] · [[ru/PythonExamples/PythonExamples|Программные примеры]]

## Код и запуск

[Программа](https://github.com/magin67/polyform_algebra/blob/d4c82cf51b2a049ca00f09d1ae752c9d23648f7a/examples/introductory/note10_edge_deletion.py) и [тесты](https://github.com/magin67/polyform_algebra/blob/d4c82cf51b2a049ca00f09d1ae752c9d23648f7a/tests/introductory/test_edge_deletion.py) закреплены на ревизии `d4c82cf`. Следуйте [[Установка библиотеки и запуск примеров|общей инструкции]]. В отдельной копии примеров используйте `git fetch origin` и `git checkout d4c82cf51b2a049ca00f09d1ae752c9d23648f7a`.

Из корня репозитория с Python выбранного окружения:

```powershell
python -m examples.introductory.note10_edge_deletion
python -m pytest tests/introductory/test_edge_deletion.py -q
```

В Windows можно заменить `python` на `.\.venv\Scripts\python.exe`, в Linux/macOS - на `.venv/bin/python`. В Colab после установки с клонированием исходников:

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "examples.introductory.note10_edge_deletion"],
    check=True,
)
```

## Правило удаления

Удаляется существующее ребро целиком, поэтому из его проводимости вычитается именно $c_{ij}$:

$$
p=[a_j-a_i]^2,\qquad M' = M(e-c_{ij}p),\qquad
\tau(M')=\tau(M)(1-c_{ij}R_{ij})
$$
В формуле остовного коэффициента $R_{ij}$ относится к исходной связной сети. Отрицательный коэффициент в факторе удаления допустим в алгебре; итоговая проводимость удаляемого ребра равна нулю. Это не добавление ребра с отрицательной проводимостью.

Из $p^2=0$ следует $(e+cp)(e-cp)=e$. Поэтому повторное добавление удалённой проводимости восстанавливает исходную экспоненту, в том числе после удаления моста.

## Исполняемый фрагмент

```python
import networkx as nx
from polyform_algebra import Polyform, quForm

# Delete edge 12 of the unit cycle C4.
graph = nx.cycle_graph(range(1, 5))
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points[1], points[2])])
updated = metric * (Polyform.one() - p)
print("cycle tau =", updated.potential(quForm.one()))
print("cycle R12 =", updated.norm(p))

# Delete the bridge of conductance 2, retaining isolated vertex 3.
graph = nx.Graph()
graph.add_weighted_edges_from([(1, 2, 1), (2, 3, 2)])
laplacian, points = Polyform.from_networkx(graph, return_points="dict")
metric = laplacian.exp()
p = quForm([(points[2], points[3])])
updated = metric * (Polyform.one() - 2*p)
print("bridge tau =", updated.potential(quForm.one()))
print("remaining exponential =", updated)
f13 = quForm([(points[1], points[3])])
print("unnormalized potential =", updated.potential(f13))
try:
    updated.norm(f13)
except ValueError as error:
    # Expected: normalization on the full disconnected graph is undefined.
    print(error)
```

## Удаление ребра цикла

После удаления $12$ остаётся путь $1-4-3-2$. Он содержит все четыре вершины и остаётся связным.

| Величина | До удаления | После удаления |
|---|---:|---:|
| Остовной коэффициент | 4 | 1 |
| Сопротивление $R_{12}$ | $3/4$ | 3 |
| Старший грейд экспоненты | 3 | 3 |

Равенство $\tau'=4(1-3/4)=1$ согласуется с единственным оставшимся остовным деревом. Между вершинами 1 и 2 теперь последовательно соединены три единичных сопротивления.

## Удаление моста

В цепочке $1-2-3$ с $c_{12}=1$, $c_{23}=2$ удаляется ребро $23$. Вершина 3 становится изолированной, но остаётся частью фиксированного набора вершин:

$$
M=(e+f_{12})(e+2f_{23}),\qquad
M'=M(e-2f_{23})=e+f_{12}
$$

$$
\tau(M')=0,\qquad u_{M'}(f_{13})=1
$$
До удаления $\tau=2$ и $R_{23}=1/2$, поэтому $\tau'=2(1-2\cdot1/2)=0$. Старший ненулевой грейд понижается с 2 до 1. Коэффициент 1 при оставшейся форме $f_{12}$ нельзя принимать за остовной коэффициент на трёх вершинах: он по-прежнему извлекается при $T_3=[(123)]^2$ и равен нулю.

Потенциал $u_{M'}(f_{13})=1$ сохраняет смысл: добавленная форма соединяет компоненты в остов. Но нормировка на $\tau(M')=0$ невозможна. Метод `norm` выдаёт `ValueError`, а не нулевое или конечное сопротивление между компонентами. В выводе полной программы `None` означает, что нормированная величина не вычисляется.

Внутри компоненты $\{1,2\}$ сопротивление физически равно 1. Однако глобальная полиформа несвязного графа не поддерживает нормировку даже для этой пары. Для такого расчёта нужно отдельно построить метрику компоненты. Исходную изолированную вершину нельзя незаметно исключать из глобального контекста.

## Проверки и статус

Шесть математических проверок сравнивают факторное удаление с полным пересчётом по оставшемуся графу, проверяют восстановление ребра, матрицы и их миноры, токовый расчёт для связного случая и отказ нормировки для несвязного. Проверяется также линейное обновление ненормированного потенциала $u_{M'}(f)=u_M(f)-c_{ij}u_M(pf)$.

**Статус: непосредственно вычислено.** Все 254 теста прошли на Python 3.12, включая запуск и импорт примера. Код заметки выполнен локально; облачный сеанс Google Colab отдельно не проверялся. Ядро библиотеки не изменялось.
