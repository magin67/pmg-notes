---
title: "Геометрия единичного треугольника на Python"
date: 2026-10-29
updated: 2026-10-29
revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-unit-triangle-geometry
lang: ru
description: "Скалярные произведения, квадратичная норма границы и площадь резистивного треугольника K3."
order: 3
---

Пример воспроизводит резистивный треугольник $K_3$ из заметок [[От длин к площадям и объёмам]] и [[Метрика объектов высших грейдов]]. Все три проводимости равны единице. Это не треугольник с единичными геометрическими сторонами: сопротивления между вершинами равны $2/3$, а длины сторон резистивного треугольника равны $\sqrt{2/3}$.

[[en/PythonExamples/Unit Triangle Geometry in Python|English]] · [[ru/PythonExamples/PythonExamples|Программные примеры]]

## Код и запуск

[Программа](https://github.com/magin67/polyform_algebra/blob/a678839a1eb3aab467a1b043bd1d0b9c7b5716ad/examples/introductory/note05_triangle_geometry.py) и [тесты](https://github.com/magin67/polyform_algebra/blob/a678839a1eb3aab467a1b043bd1d0b9c7b5716ad/tests/introductory/test_triangle_geometry.py) проверены на ревизии `a678839`. Следуйте [[Установка библиотеки и запуск примеров|общей инструкции установки]]. В существующей отдельной копии примеров выполните `git fetch origin`, затем `git checkout a678839a1eb3aab467a1b043bd1d0b9c7b5716ad`: более ранние ревизии могут не содержать этот модуль.

Из корня репозитория с интерпретатором выбранного окружения:

```powershell
python -m examples.introductory.note05_triangle_geometry
python -m pytest tests/introductory/test_triangle_geometry.py -q
```

В Windows вместо `python` можно использовать `.\.venv\Scripts\python.exe`, в Linux/macOS - `.venv/bin/python`. Для Colab выберите установку с клонированием исходников из общей инструкции и выполните:

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "examples.introductory.note05_triangle_geometry"],
    check=True,
)
```

Следующий самостоятельный фрагмент можно выполнить в файле или ячейке после установки пакета:

```python
from math import sqrt
import numpy as np
from polyform_algebra import Point, quForm

a, b, c = Point.create_list(["1", "2", "3"])
f12 = quForm([(a, b)])
f13 = quForm([(a, c)])
f23 = quForm([(b, c)])
metric = (f12 + f13 + f23).exp()
u, v, w = b-a, c-a, c-b

# @ creates a scalar polyform; norm evaluates it in the graph metric.
uv = metric.norm(u @ v)
gram = np.array([
    [metric.norm(u @ u), uv],
    [metric.norm(v @ u), metric.norm(v @ v)],
])
# Use the quadratic boundary form directly; no higher-grade @ is required.
boundary_norm = metric.norm(quForm([(a, b, c)]))
area_squared = boundary_norm / 4
area = sqrt(area_squared)
print("u dot v =", uv)
print("u dot w =", metric.norm(u @ w))
print("Gram matrix =", gram)
print("Gram determinant =", np.linalg.det(gram))
print("boundary norm =", boundary_norm)
print("area squared =", area_squared)
print("area =", area)
```

## Скалярные произведения и ориентация

В коде $u=b-a$, $v=c-a$, $w=c-b=v-u$. Оператор `@` строит скалярную полиформу; численное значение получается после применения `metric.norm`. Для выбранных ориентаций

$$
u^2=v^2=w^2=\frac23,\qquad
u\cdot v=\frac13,\qquad
u\cdot w=-\frac13,\qquad
v\cdot w=\frac13
$$

$$
\mathbf G(u,v)=
\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\qquad
\det\mathbf G=\frac13
$$
Векторы $u,v$ выходят из общей вершины, угол между ними равен $60^\circ$. Векторы $u,w$ направлены последовательно вдоль двух сторон; угол между свободными векторами равен $120^\circ$, поэтому скалярное произведение отрицательно. При замене $u$ на $-u$ знак $u\cdot v$ меняется, а норма $u^2$ сохраняется.

## Граница и площадь

Граница треугольника имеет грейд 2. Её квадратичная форма записывается как `quForm([(a, b, c)])`. В принятом соглашении PMG норма является квадратичной величиной:

$$
X=(abc)=uv,\qquad X^2=\det\mathbf G=\frac13
$$

$$
\sqrt{X^2}=\frac1{\sqrt3},\qquad
S^2=\frac{X^2}{4}=\frac1{12},\qquad
S=\frac{\sqrt{X^2}}2=\frac{\sqrt3}{6}
$$
Линейная норма границы равна площади параллелограмма на $u,v$. Площадь треугольника вдвое меньше. Поэтому деление квадратичной нормы на 4 даёт квадрат площади, а не саму площадь.

| Величина | Точное значение |
|---|---:|
| Остовной коэффициент $\tau$ | $3$ |
| Квадрат длины каждой стороны | $2/3$ |
| Квадратичная норма границы $X^2$ | $1/3$ |
| Линейная норма границы | $1/\sqrt3$ |
| Квадрат площади $S^2$ | $1/12$ |
| Площадь $S$ | $\sqrt3/6\approx0.288675$ |

Для границы второго грейда здесь не используется `X @ X`: численная оценка поддерживаемой квадратичной формы доступна без поляризации высших грейдов.

## Почему нормы нельзя просто перемножить

Произведение $f_{12}f_{13}$ является квадратичной формой границы треугольника. Но метрическая оценка произведения не равна произведению оценок:

$$
P_M(f_{12}f_{13})=\frac13
\ne P_M(f_{12})P_M(f_{13})=\frac49
$$
Определитель Грама содержит вычитаемое слагаемое $(u\cdot v)^2=1/9$. Полная программа выводит оба результата как `product_form_norm` и `product_of_norms`.

## Независимые проверки

Тесты сравнивают результаты с обратным редуцированным лапласианом $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ и с явными координатами равностороннего треугольника со стороной $\sqrt{2/3}$. Площадь проверяется через определитель координат рёбер и формулу $S^2=3\ell^4/16$. Все шесть перестановок вершин сохраняют квадратичную норму границы и определитель Грама.

**Статус: непосредственно вычислено.** На Python 3.12 прошли 238 тестов проекта, включая восемь проверок этого примера и общие проверки запуска и импорта. Кодовые фрагменты заметки проверены локально; сеанс Google Colab отдельно не запускался. Ядро квадратичной алгебры не изменялось.
