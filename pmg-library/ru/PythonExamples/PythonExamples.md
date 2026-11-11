---
title: "Программные примеры"
date: 2026-10-29
updated: 2026-11-11
revision: 22
status: draft
text_prepared_by: ChatGPT
translation_key: programming-examples
lang: ru
description: "Воспроизводимые вычисления PMG с Python-библиотекой Алгебра полиформ."
order: 0
folder_order: 70
---

Раздел связывает математические заметки PMG с исполняемыми примерами библиотеки `polyform_algebra`. Каждый материал содержит исходную задачу, соответствие обозначений коду, ожидаемые результаты и независимые проверки.

[[en/PythonExamples/PythonExamples|English]]

## Навигация по библиотеке

[[ru/Начало работы и основания/Начало работы и основания|Начало работы и основания]] · [[ru/Тематический указатель|Тематический указатель]].

## Начало работы

[[Установка библиотеки и запуск примеров]]: установка на компьютере, использование библиотеки, запуск программ и тестов, работа в Google Colab.

## Первые примеры

[[Пример - Взвешенная цепочка]] начинает с задания графа и проводимостей: лапласиан, экспонента, сопротивления, токи и мощность. Это рекомендуемый первый вычислительный пример.

[[Пример - Геометрия единичного треугольника]] показывает скалярные произведения рёбер, квадратичную норму границы и площадь; результаты проверяются по грамиану и явным координатам.

[[Пример - Вариации связей треугольника]] воспроизводит усиление одной и двух связей единичного треугольника из заметок [[Вариация одной связи]] и [[Совместная вариация нескольких связей]]. Метрическая полиформа обновляется рёберными факторами; результаты сверяются с формулами и прямым матричным расчётом.

Предпосылки: [[ru/Начало работы и основания/Введение/Вводная серия PMG|Вводная серия PMG]], в особенности [[Основные объекты и операции алгебры полиформ]] и [[Экспонента лапласиана]].

[[Пример - Экспоненты пути P5 и цикла C4]] разбирает грейды экспоненты, лесные веса, остовные коэффициенты и сопротивления пути и цикла.

[[Пример - Удаление ребра и моста]] сопоставляет удаление ребра цикла и моста: изменение сопротивлений, сохранение изолированных вершин и невозможность глобальной нормировки при потере связности.

## Пространства

[[ru/PythonExamples/Пример - Подпространства и преобразования графов|Подпространства и преобразования графов]] - потенциалы, би- и ди-координаты, задача Дирихле, стягивание и исключение вершин. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/spaces.ipynb).

## Метрические параметры графов

[[ru/PythonExamples/Пример - Метрические параметры графов|Метрические параметры графов на Python]]. Восемь расчётов по заметкам серии. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/metric-parameters.ipynb).

## Структурные тождества

[[ru/PythonExamples/Пример - Проверка структурных тождеств|Структурные тождества на Python]]. Пять точных проверок по заметкам серии. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/structural-identities.ipynb).

## Симметрические полиформы

[[ru/PythonExamples/Пример - Проверка тождеств симметрических полиформ|Проверка тождеств симметрических полиформ]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/symmetric-polyforms.ipynb).

## Комбинаторные потенциалы

[[ru/PythonExamples/Пример - Комбинаторные потенциалы|Комбинаторные потенциалы]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/combinatorial-potentials.ipynb).

## Топономы разбиений

[[ru/PythonExamples/Пример - Топономы разбиений|Топономы разбиений]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/partition-toponomes.ipynb).

## Полиномиальные топономы

[[ru/PythonExamples/Пример - Полиномиальные топономы|Полиномиальные топономы]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/polynomial-toponomes.ipynb).

## Балансовые графы

[[ru/PythonExamples/Пример - Балансовые графы|Балансовые графы]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/balanced-graphs.ipynb).

## KVP-разложение

[[ru/PythonExamples/Пример - KVP-разложение|KVP-разложение]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/kvp-decomposition.ipynb).

## Гриниан и дуальность полиформ

[[ru/PythonExamples/Пример - Гриниан и дуальность полиформ|Гриниан и дуальность полиформ]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/greenian-duality.ipynb).

## Матроидные параметры и лесные характеристики графов

[[ru/PythonExamples/Пример - Матроидные параметры и лесные характеристики графов|Матроидные параметры и лесные характеристики графов]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/matroid-forest-characteristics.ipynb).

## Граничные данные и цепочки ядер

[[ru/PythonExamples/Пример - Граничные данные и цепочки ядер|Граничные данные и цепочки ядер]]. [Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/boundary-data-core-chains.ipynb).

## Как устроен пример

Задача и рисунок → математические объекты → вычисление через `polyform_algebra` → ожидаемые результаты → независимая проверка. Фрагменты одной заметки выполняются по порядку. NumPy и прямой подсчёт используются там, где они помогают проверить ответ другим способом.

## Версия и готовые блокноты

Для вводных примеров и серии «Пространства» используется тег `v0.9.0`. Блокноты следующих серий устанавливают закреплённые коммиты пакета, указанные в примерах.

Для взвешенной цепочки подготовлен блокнот с текстом, формулами, рисунком и результатами:

[Открыть в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/weighted-chain.ipynb) · [Скачать блокнот](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/ru/PythonExamples/notebooks/weighted-chain.ipynb)

Вычисление частного случая не заменяет доказательства общей формулы. Возможности программы следует отличать от общей модели [[Спецификация ядра PMG|спецификации PMG]].


## Символьные вычисления

[[Пример - Экспоненты пути P5 и цикла C4|Экспоненты пути и цикла]]: буквенные вершины, произведения форм, полное разложение экспоненты по грейдам. В отдельном блокноте видны сами полиформы; численные оценки вынесены в заключительный раздел.

[Открыть символьный блокнот в Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/ru/PythonExamples/notebooks/symbolic-polyforms.ipynb)
