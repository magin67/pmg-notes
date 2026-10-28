"""Reproduce the 15 English SVG figures from the checked Russian originals.

Run from any directory with Python 3.10 or newer. Only the standard library is
needed. Coordinates, graph topology, colors, and mathematical data are retained;
titles, accessible descriptions, and visible prose labels are translated.
"""

from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as ET


FIGURES = {
    "Лес и цикл - внешние произведения.svg": "Forest and Cycle - Exterior Products.svg",
    "Матроид пути и звезды - соответствие рёбер.svg": "Path and Star Matroid - Edge Correspondence.svg",
    "Путь P4 - лапласиан и знаковые связи гриниана.svg": "Path P4 - Laplacian and Signed Greenian Connections.svg",
    "Три индекса лесов цикла C4.svg": "Three Forest Indices of Cycle C4.svg",
    "Обычные и корневые леса - два типа компонент.svg": "Ordinary and Rooted Forests - Two Component Types.svg",
    "Леса при одноточечном сочленении.svg": "Forests under One-Point Gluing.svg",
    "Допустимые расширения двухлесов K4.svg": "Admissible Extensions of K4 Two-Forests.svg",
    "Три случайных дерева взвешенного треугольника.svg": "Three Random Trees of a Weighted Triangle.svg",
    "Пересечения деревьев и параметр H2.svg": "Tree Intersections and Parameter H2.svg",
    "Взвешенный треугольник - резистивная окружность.svg": "Weighted Triangle - Resistance Circumcircle.svg",
    "Двухлес - подсчёт по вершинам и удалённым рёбрам.svg": "Two-Forest - Counting Vertices and Deleted Edges.svg",
    "Лесной вклад и рёберная поправка к радиусу.svg": "Forest Contribution and Edge Correction to the Radius.svg",
    "Переворот Уитни - один матроид и разная геометрия.svg": "Whitney Twist - One Matroid and Different Geometry.svg",
    "Выбор границы - цикл и цикл с листом.svg": "Boundary Choice - Cycle and Cycle with a Leaf.svg",
    "Общее ребро - три разных закона склейки.svg": "Shared Edge - Three Different Gluing Laws.svg",
}

LABELS = {
    "Пересечение двух независимо выбранных деревьев": "Intersection of two independently sampled trees",
    "Девять упорядоченных пар трёх деревьев треугольника. В ячейке показаны общие рёбра и сумма их собственных сопротивлений. Среднее с весами произведений вероятностей равно 84/121.": "Nine ordered pairs of the triangle's three trees. Each cell shows common edges and the sum of their conductor resistances. The average weighted by products of tree probabilities is 84/121.",
    "Строка: первое дерево. Столбец: второе дерево. Каждая ячейка имеет вероятность pᵢ pⱼ.": "Row: first tree. Column: second tree. Each cell has probability pᵢ pⱼ.",
    "H₂ = Σᵢⱼ pᵢ pⱼ · (сумма в ячейке) = 84/121": "H₂ = Σᵢⱼ pᵢ pⱼ · (cell sum) = 84/121",
    "Серый пунктир: рёбра, не вошедшие в пересечение.": "Gray dashes: edges outside the intersection.",
    "Какие рёбра можно добавить к лесу?": "Which edges can be added to a forest?",
    "В единичном K4 у леса типа 3+1 три допустимых ребра, у типа 2+2 четыре. Всего таких лесов соответственно 12 и 3, среднее A равно 16/5.": "In unit-weight K4, a forest of type 3+1 has three admissible edges; type 2+2 has four. There are 12 and 3 such forests, respectively, and the mean of A is 16/5.",
    "Синий: рёбра леса. Золотой пунктир: допустимое добавление. Серый пунктир: возник бы цикл.": "Blue: forest edges. Gold dashes: admissible additions. Gray dashes: a cycle would form.",
    "Компоненты 3 + 1": "Components 3 + 1",
    "Компоненты 2 + 2": "Components 2 + 2",
    "12 лесов этого типа": "12 forests of this type",
    "3 леса этого типа": "3 forests of this type",
    "Грейд, компоненты и когрейд одного леса": "Grade, components, and corank of a forest",
    "В цикле C4 показано по одному лесу грейдов 0,1,2,3. Числа компонент равны 4,3,2,1, когрейды — 3,2,1,0. Во всех рисунках сохранены четыре вершины.": "Cycle C4 is shown with one forest at each grade 0,1,2,3. Component counts are 4,3,2,1 and coranks are 3,2,1,0. All four vertices are retained in every drawing.",
    "Четыре леса в C₄. Пунктир: рёбра исходного графа, не вошедшие в выбранный лес.": "Four forests in C₄. Dashes: original edges outside the chosen forest.",
    "Взвешенный треугольник и его три остовных дерева": "A weighted triangle and its three spanning trees",
    "Проводимости ab, ac, bc равны 1,2,3. Три дерева имеют веса 2,3,6 и вероятности 2/11,3/11,6/11. Суммирование даёт вероятности включения рёбер 5/11,8/11,9/11.": "Conductances ab, ac, bc are 1,2,3. The three trees have weights 2,3,6 and probabilities 2/11,3/11,6/11. Summing gives edge inclusion probabilities 5/11,8/11,9/11.",
    "Остовной вес τ = 2 + 3 + 6 = 11. Вероятность дерева равна его весу, делённому на τ.": "Spanning-tree weight τ = 2 + 3 + 6 = 11. Each tree has probability equal to its weight divided by τ.",
    "Общее ребро: три разных закона склейки": "A shared edge: three different gluing laws",
    "Два единичных треугольника склеиваются по вершинам a,b. Две копии ребра ab сохраняются параллельно, отождествляются в одно единичное ребро или обе удаляются. Соответствующие остовные числа равны 12, 8 и 4.": "Two unit-weight triangles are glued at vertices a,b. Both copies of edge ab are kept in parallel, identified as one unit-weight edge, or deleted. The corresponding spanning-tree counts are 12, 8, and 4.",
    "Два единичных треугольника; правило для копий ребра ab задаётся отдельно.": "Two unit-weight triangles; the rule for copies of edge ab is specified separately.",
    "Сохранить обе копии": "Keep both copies",
    "Одно ребро c = 1": "One edge, c = 1",
    "Удалить обе копии": "Delete both copies",
    "Две параллельные копии можно заменить одним ребром c = 2.": "Two parallel copies can be replaced by one edge with c = 2.",
    "Один лес: вклад без корней и с выбором корней": "One forest: unrooted and rooted contributions",
    "Два леса на четырёх вершинах: путь на трёх вершинах и изолированная вершина имеют 3 выбора корней; два отдельных ребра имеют 4. Все варианты корней перечислены.": "Two forests on four vertices: a three-vertex path and an isolated vertex have 3 root choices; two disjoint edges have 4. All root choices are shown.",
    "Единичный K₄, грейд g = 2. Золотое кольцо отмечает выбранный корень компоненты.": "Unit-weight K₄, grade g = 2. A gold ring marks the chosen root of a component.",
    "3 выбора корней": "3 root choices",
    "4 выбора корней": "4 root choices",
    "Вклад в f₂: 1;   в p₂: 3": "Contribution to f₂: 1;   to p₂: 3",
    "Вклад в f₂: 1;   в p₂: 4": "Contribution to f₂: 1;   to p₂: 4",
    "Один матроид, разная вершинная геометрия": "One matroid, different vertex geometry",
    "Путь P4 и звезда K1,3 с тремя именованными рёбрами. Соответствие имён сохраняет все независимые наборы, но суммы попарных резистенсов равны 10 и 9.": "Path P4 and star K1,3 with three labeled edges. The label correspondence preserves every independent set, but the sums of pairwise resistances are 10 and 9.",
    "Все проводимости равны 1. Одинаковый цвет и имя показывают соответствие рёбер.": "All conductances equal 1. Matching colors and labels show the edge correspondence.",
    "Путь P₄": "Path P₄",
    "Звезда K₁,₃": "Star K₁,₃",
    "Любой набор из {ℓ₁, ℓ₂, ℓ₃} независим": "Every subset of {ℓ₁, ℓ₂, ℓ₃} is independent",
    "Проводимости, коэффициенты гриниана и резистенсы": "Conductances, Greenian coefficients, and resistances",
    "Слева единичный путь abcd. Справа канонические связи гриниана: ab и cd имеют вес минус 1/8, ac и bd — 3/8, ad — 5/8, bc — 1/8. Резистенс ad равен 3.": "Left: the unit-weight path abcd. Right: canonical Greenian connections, with weights minus 1/8 for ab and cd, 3/8 for ac and bd, 5/8 for ad, and 1/8 for bc. Resistance ad is 3.",
    "Сплошные связи: положительные коэффициенты. Красный пунктир: отрицательные.": "Solid connections: positive coefficients. Red dashes: negative coefficients.",
    "L: проводимости cᵢⱼ": "L: conductances cᵢⱼ",
    "Gr: коэффициенты γᵢⱼ": "Gr: coefficients γᵢⱼ",
    "От проводимостей к описанной окружности": "From conductances to the circumcircle",
    "Слева сеть с проводимостями 1,2,3. Справа точная евклидова реализация: квадраты сторон 5/11,4/11,3/11, квадрат радиуса 15/121. Центр O отличается от центроида h.": "Left: a network with conductances 1,2,3. Right: an exact Euclidean realization, with squared side lengths 5/11,4/11,3/11 and squared radius 15/121. The center O differs from the centroid h.",
    "Сеть показана схематически. Евклидова реализация справа сохраняет длины √R.": "The network is schematic. The Euclidean realization on the right preserves lengths √R.",
    "Проводимости рёбер": "Edge conductances",
    "Резистивная геометрия": "Resistance geometry",
    "Лесной вклад, рёберная поправка и радиус": "Forest contribution, edge correction, and radius",
    "Столбцы показывают ξ1/3, из которого вычитается H2/12. Для единичного дерева на 4 вершинах, C4, K4 и треугольника с проводимостями 1,2,3 остаются радиусы 3/4,5/16,3/16,15/121.": "Bars show ξ1/3, from which H2/12 is subtracted. For a unit-weight tree on 4 vertices, C4, K4, and a triangle with conductances 1,2,3, the remaining radii are 3/4,5/16,3/16,15/121.",
    "Полный столбец: ξ₁/3. Штрихованная часть вычитается; остаётся ρ.": "Full bar: ξ₁/3. Subtract the hatched part; ρ remains.",
    "Радиус ρ": "Radius ρ",
    "Вычитаем H₂/12": "Subtract H₂/12",
    "P₄ и K₁,₃": "P₄ and K₁,₃",
    "Треугольник": "Triangle",
    "Одноточечное сочленение: лес выбирается по частям": "One-point gluing: choose a forest in each part",
    "Лес первого треугольника содержит два ребра, лес второго — одно. После отождествления выбранных вершин их объединение остаётся лесом. Грейды и когрейды складываются.": "The forest of the first triangle has two edges; that of the second has one. After the chosen vertices are identified, their union is still a forest. Grades and coranks add.",
    "Показан один выбор пары лесов. Пунктир сохраняет видимость остальных рёбер частей.": "One choice of a forest pair is shown. Dashes show the remaining edges of the parts.",
    "Отождествляем p₁ и p₂": "Identify p₁ and p₂",
    "Другой выбор границы меняет матроид результата": "Changing the boundary changes the resulting matroid",
    "Один путь P4 с двумя разметками границы. При добавлении пути из двух рёбер между концами P4 получается C5; при добавлении между вершинами на расстоянии двух рёбер получается C4 с листом. Остовные числа 5 и 4, радиусы 2/5 и 9/16.": "One path P4 with two boundary markings. Adding a two-edge path between its endpoints gives C5; adding it between vertices at distance two edges gives C4 with a leaf. Spanning-tree counts are 5 and 4, radii 2/5 and 9/16.",
    "Золотые окружности отмечают выбранные вершины; все проводимости равны 1.": "Gold circles mark the chosen vertices; all conductances equal 1.",
    "Оба конца пути P₄": "Both endpoints of P₄",
    "Тот же P₄, другая разметка": "Same P₄, different marking",
    "Присоединяем путь P₃": "Attach path P₃",
    "Цикл C₅": "Cycle C₅",
    "Пара на расстоянии 2": "Pair at distance 2",
    "C₄ с листом": "C₄ with a leaf",
    "Лес и цикл: независимость рёберных векторов": "Forest and cycle: independence of edge vectors",
    "Два ребра треугольника образуют лес; все три ребра дают зависимость и нулевое внешнее произведение.": "Two edges of a triangle form a forest; all three edges give a dependence and a zero exterior product.",
    "Ориентация задаёт знаки векторов; независимость набора рёбер от неё не зависит.": "Orientation sets the signs of vectors; edge-set independence does not depend on it.",
    "Два ребра: лес": "Two edges: forest",
    "Три ребра: цикл": "Three edges: cycle",
    "Почему каждый двухлес учитывается ровно один раз": "Why each 2-forest is counted exactly once",
    "Фиксированный двухлес с компонентами A={q,a} и B={b,c,d}. В B можно выбрать 3 вершины или удалить 2 ребра. При восстановлении веса разность вкладов равна (3-2)w(F)=w(F).": "A fixed 2-forest with components A={q,a} and B={b,c,d}. In B one can choose 3 vertices or delete 2 edges. After restoring weights, the difference of contributions is (3-2)w(F)=w(F).",
    "Фиксируем q в A. Все показанные выборы возвращают один и тот же лес F.": "Fix q in A. All choices shown recover the same forest F.",
    "Компонента A": "Component A",
    "Компонента B": "Component B",
    "Сумма по вершинам: три выбора": "Vertex sum: three choices",
    "Сумма по рёбрам: два удаления": "Edge sum: two deletions",
    "Удалено bc": "Delete bc",
    "Удалено cd": "Delete cd",
    "Переворот Уитни: один матроид, разная геометрия": "Whitney twist: one matroid, different geometry",
    "Две части являются двухрёберными путями с листом при первом конце. При прямой склейке листья присоединены к одной вершине C4, при перевороте к противоположным. Имена рёбер сохраняются. Радиус 13/16 в обоих случаях, индекс Кирхгофа равен 20 и 21.": "The two parts are two-edge paths, each with a leaf at its first endpoint. Straight gluing attaches both leaves to one vertex of C4; a twist attaches them to opposite vertices. Edge labels are preserved. Both radii are 13/16, but the Kirchhoff indices are 20 and 21.",
    "Пары граничных вершин фиксированы; меняется только соответствие двух концов.": "Boundary pairs stay fixed; only the correspondence of the two endpoints changes.",
    "Прямая склейка": "Straight gluing",
    "С переворотом": "With a twist",
    "Цикл: {ℓ₁, ℓ₂, ℓ₄, ℓ₅}. Мосты: ℓ₃, ℓ₆.": "Cycle: {ℓ₁, ℓ₂, ℓ₄, ℓ₅}. Bridges: ℓ₃, ℓ₆.",
    "Первая часть": "First part",
    "Вторая часть": "Second part",
}


def main():
    repo = Path(__file__).resolve().parents[2]
    source = repo / "pmg-library/ru/Матроидные параметры и лесные характеристики графов"
    target = repo / "pmg-library/en/Matroid parameters and forest characteristics of graphs"
    target.mkdir(parents=True, exist_ok=True)
    used = set()
    for original, translated in FIGURES.items():
        svg = (source / original).read_text()
        for old, new in LABELS.items():
            escaped = escape(old, quote=False)
            if escaped in svg:
                svg = svg.replace(escaped, escape(new, quote=False))
                used.add(old)
        assert not re.search("[А-Яа-яЁё]", svg), original
        ET.fromstring(svg)
        (target / translated).write_text(svg)
    assert used == set(LABELS), f"Unused translations: {set(LABELS) - used}"
    print(f"Translated {len(FIGURES)} SVG figures; geometry and numeric labels preserved.")


if __name__ == "__main__":
    main()
