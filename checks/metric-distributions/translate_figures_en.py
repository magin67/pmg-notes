"""Translate the 12 SVG figures without changing geometry or numerical data."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'pmg-library/ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/images'
DESTINATION = ROOT / 'pmg-library/en/Resistance Geometry and Duality/Metric Distributions and Edge Influence/images'
NAMES = {
    'Добавление связи к цепочке': 'Adding a Coupling to a Path',
    'Поле влияния на треугольнике': 'Influence Field on a Triangle',
    'Направления путей на дереве': 'Path Directions on a Tree',
    'Проводимости и пересечение путей': 'Conductances and Path Intersection',
    'Пробы связей на дереве': 'Edge Probes on a Tree',
    'Два маршрута в треугольнике': 'Two Routes in a Triangle',
    'Два потока и знаки на квадрате': 'Two Flows and Signs on a Square',
    'Нулевое влияние перемычки': 'Zero Influence of a Cross-Edge',
    'Детализация ребра и распределение': 'Edge Subdivision and Distribution',
    'Парные вклады треугольника на дереве': 'Triangle Pair Contributions on a Tree',
    'Пары и влияние связей на квадрате': 'Pairs and Edge Influence on a Square',
    'Пробы нормы треугольника на квадрате': 'Triangle Norm Probes on a Square',
}
TEXT = {
    **NAMES,
    'нет связи': 'no edge',
    'Исходная цепочка': 'Initial path',
    'Добавлена связь ac проводимости 1': 'Edge ac added with conductance 1',
    'Одна форма в двух метриках': 'One form in two metrics',
    'Три независимые пробы для f = [(ac)]²': 'Three independent probes for f = [(ac)]²',
    'Исходный граф в каждой пробе: единичный треугольник, N(f) = 2/3': 'Each probe starts from a unit triangle, N(f) = 2/3',
    'Совпадающие направления на общем участке': 'Matching directions on the common segment',
    'Вклады: +1 на bc, +1 на cd;   N(f) = 2': 'Contributions: +1 on bc, +1 on cd;   N(f) = 2',
    'Обращён только второй путь': 'Only the second path is reversed',
    'Вклады: −1 на bc, −1 на cd;   N(f) = −2': 'Contributions: −1 on bc, −1 on cd;   N(f) = −2',
    'Одна общая вершина, общих рёбер нет': 'One shared vertex, no shared edges',
    'Все рёберные вклады равны нулю;   N(f) = 0': 'All edge contributions are zero;   N(f) = 0',
    'Исходное дерево: проводимости c': 'Initial tree: conductances c',
    'Распределение: коэффициенты m': 'Distribution: coefficients m',
    'Каждая проба начинается с исходного дерева': 'Each probe starts from the initial tree',
    'Исходно N(f) = 5/2; в каждой пробе удвоена одна проводимость': 'Initially N(f) = 5/2; each probe doubles one conductance',
    'Все проводимости равны 1': 'All conductances are 1',
    'Проводимость ac равна 2': 'Conductance of ac is 2',
    'Два маршрута для единичного тока a → c': 'Two routes for a unit current a → c',
    'Поток для v = (ac)': 'Flow for v = (ac)',
    'Поток для u = (bd)': 'Flow for u = (bd)',
    'Сумма = 0; поле ненулевое': 'Sum = 0; nonzero field',
    'Коэффициенты смешанной формы': 'Mixed-form coefficients',
    'Знак зависит от взаимных направлений токов': 'The sign depends on relative current directions',
    'Все c = 1;   R(ac) = 1;   I(bd) = 0': 'All c = 1;   R(ac) = 1;   I(bd) = 0',
    'Распределение нормы (ac)²': 'Distribution of norm (ac)²',
    'Сумма коэффициентов = 2/3': 'Coefficient sum = 2/3',
    'Ребро ac: сопротивление 1': 'Edge ac: resistance 1',
    'Два участка: 1/2 + 1/2': 'Two segments: 1/2 + 1/2',
    'Старая метрика сохраняется; вклад делится': 'The old metric is preserved; the contribution splits',
    'На рёбрах указаны коэффициенты распределения для [(ac)]²': 'Edges show distribution coefficients for [(ac)]²',
    'Вклад = 1/2': 'Contribution = 1/2',
    'Вклад = 1/3': 'Contribution = 1/3',
    'Вклад = 1/6': 'Contribution = 1/6',
    'Удалены ha, hb': 'Delete ha, hb',
    'Удалены ha, hc': 'Delete ha, hc',
    'Удалены hb, hc': 'Delete hb, hc',
    'Норма (abc)² = 1/2 + 1/3 + 1/6 = 1': 'Norm (abc)² = 1/2 + 1/3 + 1/6 = 1',
    'Сумма = 1/2': 'Sum = 1/2',
    'Сумма = 1': 'Sum = 1',
    'Вклады пар m': 'Pair contributions m',
    'Влияния связей A': 'Edge influences A',
    'Исходный квадрат': 'Initial square',
    'Изменение: -3/14': 'Change: -3/14',
    'Изменение: -1/14': 'Change: -1/14',
    'Удвоена связь ab': 'Double edge ab',
    'Удвоена связь cd': 'Double edge cd',
    'Две независимые пробы нормы треугольника': 'Two independent probes of the triangle norm',
    'Цепочка a-b-c с единичными проводимостями и треугольник после добавления единичной связи ac. Значение формы меняется с 2 до 2/3.':
        'The path a-b-c with unit conductances and the triangle after adding a unit coupling ac. The value of the form changes from 2 to 2/3.',
    'Каждая проводимость отдельно увеличивается с 1 до 2. Новые значения формы: 3/5, 3/5, 2/5; влияния: -1/15, -1/15, -4/15; коэффициенты: 1/9, 1/9, 4/9.':
        'Each conductance is independently increased from 1 to 2. New form values: 3/5, 3/5, 2/5; influences: -1/15, -1/15, -4/15; coefficients: 1/9, 1/9, 4/9.',
    'Три пары путей единичной цепочки: одинаковое направление на b-c-d, противоположное направление на том же участке и встреча только в вершине c. Значения формы равны 2, -2 и 0.':
        'Three path pairs on a unit path: matching directions on b-c-d, opposite directions on the same segment, and contact only at vertex c. The form values are 2, -2, and 0.',
    'У цепочки проводимости 3, 2, 1/2 и 4. Для путей a-d и b-e коэффициенты распределения равны 0, 1/2, 2 и 0; их сумма 5/2.':
        'The path has conductances 3, 2, 1/2, and 4. For paths a-d and b-e, distribution coefficients are 0, 1/2, 2, and 0; their sum is 5/2.',
    'Четыре независимых удвоения проводимости. Для ab и de влияние нулевое; для bc оно равно -1/4, для cd равно -1. Новые значения формы 5/2, 9/4, 3/2 и 5/2.':
        'Four independent conductance doublings. The influence is zero for ab and de, -1/4 for bc, and -1 for cd. New form values are 5/2, 9/4, 3/2, and 5/2.',
    'Слева токи 1/3, 1/3 и 2/3, вклады 1/9, 1/9 и 4/9. Справа после увеличения c_ac до 2 токи 1/5, 1/5 и 4/5, вклады 1/25, 1/25 и 8/25. Норма меняется с 2/3 до 2/5.':
        'Left: currents 1/3, 1/3, and 2/3; contributions 1/9, 1/9, and 4/9. Right, after increasing c_ac to 2: currents 1/5, 1/5, and 4/5; contributions 1/25, 1/25, and 8/25. The norm changes from 2/3 to 2/5.',
    'Поток a-c и поток b-d имеют на сторонах модули 1/2. На ab и cd направления противоположны и вклад -1/4; на bc и ad совпадают и вклад +1/4. Сумма нулевая, распределение ненулевое.':
        'Flows a-c and b-d have magnitude 1/2 on every side. On ab and cd their directions are opposite, giving -1/4; on bc and ad they agree, giving +1/4. The sum is zero but the distribution is nonzero.',
    'Квадрат с единичной диагональной связью bd. В опыте a-c вершины b и d равнопотенциальны: вклад существующей перемычки равен нулю, а вклады четырёх сторон равны 1/4.':
        'A square with a unit diagonal coupling bd. In experiment a-c, vertices b and d have equal potentials: the existing cross-edge contributes zero, and each of the four sides contributes 1/4.',
    'Единичный треугольник и его детализация новой вершиной d на связи ac. Старый вклад ac 4/9 делится на ad 2/9 и cd 2/9; вклады ab и bc остаются 1/9. Резистенс ac остаётся 2/3.':
        'A unit triangle and its subdivision by a new vertex d on ac. The old ac contribution 4/9 splits into ad 2/9 and cd 2/9; ab and bc retain contributions of 1/9. Effective resistance ac remains 2/3.',
    'Дерево с центром h и листьями a,b,c,d; проводимости ha=1,hb=2,hc=3,hd=1. Удаляемые пары ha,hb; ha,hc; hb,hc имеют вклады 1/2,1/3,1/6. Цвет контура вершины отмечает её компоненту после удаления.':
        'A tree with center h and leaves a,b,c,d; conductances ha=1,hb=2,hc=3,hd=1. Deleted pairs ha,hb; ha,hc; hb,hc contribute 1/2,1/3,1/6. Vertex outline colors mark components after deletion.',
    'Для X=(abc) на единичном квадрате парные вклады: ab,bc=1/4; ab,cd=ab,ad=bc,cd=bc,ad=1/16; cd,ad=0. Рёберные суммы A_ab=A_bc=3/8, A_cd=A_ad=1/8. Сумма пар 1/2, сумма влияний 1.':
        'For X=(abc) on a unit square, pair contributions are ab,bc=1/4; ab,cd=ab,ad=bc,cd=bc,ad=1/16; cd,ad=0. Edge sums are A_ab=A_bc=3/8 and A_cd=A_ad=1/8. Pair sum 1/2; influence sum 1.',
    'Исходная норма границы (abc) на единичном квадрате равна 1/2. Независимое удвоение ab даёт 2/7 и изменение -3/14; независимое удвоение cd даёт 3/7 и изменение -1/14. Подписи рёбер обозначают проводимости.':
        'The initial norm of boundary (abc) on a unit square is 1/2. Independently doubling ab gives 2/7 and a change of -3/14; independently doubling cd gives 3/7 and a change of -1/14. Edge labels denote conductances.',
}


def main():
    for prefix, uri in [
        ('', 'http://www.w3.org/2000/svg'),
        ('xlink', 'http://www.w3.org/1999/xlink'),
        ('dc', 'http://purl.org/dc/elements/1.1/'),
        ('cc', 'http://creativecommons.org/ns#'),
        ('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
    ]:
        ET.register_namespace(prefix, uri)
    DESTINATION.mkdir(parents=True, exist_ok=True)
    changed = 0
    for old, new in NAMES.items():
        tree = ET.parse(SOURCE / (old+'.svg'))
        for node in tree.getroot().iter():
            if node.text and re.search('[А-Яа-яЁё]', node.text):
                assert node.text in TEXT, (old, node.text)
                node.text = TEXT[node.text]
                changed += 1
        result = ET.tostring(tree.getroot(), encoding='unicode')
        assert not re.search('[А-Яа-яЁё]', result), old
        (DESTINATION/(new+'.svg')).write_text(result+'\n', encoding='utf-8', newline='\n')
    print(f'Translated {len(NAMES)} figures and {changed} text nodes; geometry unchanged.')


if __name__ == '__main__':
    main()
