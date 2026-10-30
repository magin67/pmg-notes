"""Four native SVG figures for the spectral boundary note; stdlib only."""
from draw_forest_states import Drawing, INK, MUTED, TEAL, GOLD, BLUE, PURPLE
from verify_spectral_boundary import passport, poly, combine


def graph(d, points, edges, boundary=('a', 'b'), color=TEAL):
    for u, v in edges:
        d.line(points[u], points[v], color)
    for label, point in points.items():
        d.node(*point, label, boundary=label in boundary)


def same_passport():
    d = Drawing('Один лесной паспорт, разные спектры',
                'Путь abcd и звезда с центром b. В обоих графах упорядоченная граница a,b, все проводимости единичные. Лесные полиномы состояний совпадают, характеристические полиномы различаются.',
                505, 'Граница (a, b) выделена золотым; все проводимости равны 1.')
    d.box(24, 103, 446, 262)
    d.box(490, 103, 446, 262)
    d.text(245, 139, 'Путь P₄', 23, anchor='middle', weight='700')
    d.text(714, 139, 'Звезда K₁,₃', 23, anchor='middle', weight='700')
    graph(d, {'a': (75, 235), 'b': (185, 235), 'c': (295, 235), 'd': (405, 235)}, [('a', 'b'), ('b', 'c'), ('c', 'd')])
    graph(d, {'a': (555, 235), 'b': (685, 235), 'c': (835, 190), 'd': (835, 295)}, [('a', 'b'), ('b', 'c'), ('b', 'd')])
    d.text(245, 337, 'χ(ξ) = ξ(ξ − 2)(ξ² − 4ξ + 2)', 20, anchor='middle')
    d.text(714, 337, 'χ(ξ) = ξ(ξ − 1)²(ξ − 4)', 20, anchor='middle')
    d.text(480, 408, 'В обоих случаях:  ℱa|b(t) = (1 + t)²;   ℱab(t) = t(1 + t)²', 22, anchor='middle')
    d.text(480, 451, 'Два ребра в лесе: f₂ = 3, но корневые коэффициенты p₂ равны 10 и 9.', 19, MUTED, 'middle')
    d.text(480, 484, 'Паспорт по связности границы не сохраняет все размеры компонент.', 19, MUTED, 'middle')
    return d.save('Одинаковый лесной паспорт и разные спектры')


def two_paths():
    state = passport(tuple('aub'), (('a', 'u', 1), ('u', 'b', 1)))
    assert combine(state, state)[0] == poly(0, -16, 20, -8, 1)
    d = Drawing('Два пути сочленяются в цикл C₄',
                'Пути a-u-b и a-v-b с единичными проводимостями и общей границей a,b. После отождествления a с a и b с b получается цикл a-u-b-v-a. Общих рёбер нет. В каждой граничной диагонали лишний член xi вычитается один раз.',
                529, 'Отождествляются a ↔ a и b ↔ b; внутренние вершины u, v различны.')
    for x, width in ((24, 258), (306, 258), (608, 328)):
        d.box(x, 101, width, 274)
    d.text(153, 133, 'G₁', 23, BLUE, 'middle', '700')
    d.text(435, 133, 'G₂', 23, TEAL, 'middle', '700')
    d.text(772, 133, 'Результат', 23, anchor='middle', weight='700')
    graph(d, {'a': (65, 295), 'u': (153, 199), 'b': (241, 295)}, [('a', 'u'), ('u', 'b')], color=BLUE)
    graph(d, {'a': (347, 295), 'v': (435, 199), 'b': (523, 295)}, [('a', 'v'), ('v', 'b')])
    d.text(586, 252, '→', 31, anchor='middle')
    points = {'a': (657, 260), 'u': (772, 185), 'b': (887, 260), 'v': (772, 343)}
    d.line(points['a'], points['u'], BLUE)
    d.line(points['u'], points['b'], BLUE)
    graph(d, points, [('a', 'v'), ('v', 'b')])
    d.text(480, 414, 'S = S₁ + S₂ − ξI₂;     E = E₁E₂', 24, anchor='middle')
    d.text(480, 459, 'χC₄(ξ) = ξ(ξ − 2)²(ξ − 4)', 25, anchor='middle', weight='700')
    d.text(480, 504, 'При ξ = 2 рациональные Sᵢ не определены; полиномиальный закон остаётся верен.', 18, MUTED, 'middle')
    return d.save('Спектральное сочленение двух путей')


def shared_edge():
    d = Drawing('Одно общее ребро или две его копии',
                'Два единичных треугольника a-u-b-a и a-v-b-a сочленяются по a,b. Слева общий экземпляр ab оставлен один раз, всего пять рёбер. Справа два различных экземпляра ab оставлены параллельно, всего шесть рёбер. Пересечений рёбер вне вершин нет.',
                555, 'Исходные компоненты: треугольники a-u-b-a и a-v-b-a; все веса равны 1.')
    for x in (24, 492):
        d.box(x, 104, 444, 351)
    for cx, doubled in ((246, False), (714, True)):
        d.text(cx, 140, 'Общее ab: один экземпляр' if not doubled else 'Разные ab: две копии', 21, anchor='middle', weight='700')
        points = {'a': (cx-142, 285), 'u': (cx, 210), 'b': (cx+142, 285), 'v': (cx, 370)}
        for u, v in [('a', 'u'), ('u', 'b'), ('b', 'v'), ('v', 'a')]:
            d.line(points[u], points[v], BLUE if 'u' in (u, v) else TEAL)
        if doubled:
            for shift in (-33, 33):
                d.parts.append(f'<path d="M {cx-142} 285 Q {cx} {285+shift} {cx+142} 285" fill="none" stroke="{PURPLE}" stroke-width="4"/>')
        else:
            d.line(points['a'], points['b'], PURPLE)
        for name, point in points.items():
            d.node(*point, name, boundary=name in ('a', 'b'))
        d.text(cx, 416, '5 рёбер;  χ = ξ(ξ − 2)(ξ − 4)²' if not doubled else '6 рёбер;  χ = ξ(ξ − 2)(ξ − 4)(ξ − 6)', 18, anchor='middle')
    d.text(480, 492, 'Для одного общего ребра: L = L₁ + L₂ − Lₑ', 23, anchor='middle')
    d.text(480, 532, 'Если ab принадлежит только одной компоненте, применяем закон без общей копии.', 18, MUTED, 'middle')
    return d.save('Общее ребро и параллельные копии')


def input_output():
    d = Drawing('Вход и выход присоединяемого ядра',
                'Слева собранный фрагмент с выходом a,b, справа новое ядро со входом a,b и выходом c,d. Входная и выходная пары ядра не пересекаются. Ребро ab принадлежит только левому фрагменту, cd только ядру. После сочленения активная граница меняется с a,b на c,d; это требует отдельного преобразования миноров.',
                555, 'Порядок пар фиксирован: вход (a, b), выход (c, d). Схема задаёт инцидентность.')
    d.box(28, 103, 379, 310)
    d.box(427, 103, 505, 310)
    d.text(216, 139, 'Собранный фрагмент', 22, BLUE, 'middle', '700')
    d.text(681, 139, 'Новое ядро', 22, TEAL, 'middle', '700')
    pts = {'a': (417, 210), 'b': (417, 350), 'c': (825, 210), 'd': (825, 350), 'u': (170, 280), 'v': (620, 180), 'w': (620, 380)}
    for edge in [('u', 'a'), ('u', 'b'), ('a', 'b')]:
        d.line(pts[edge[0]], pts[edge[1]], BLUE)
    for edge in [('a', 'v'), ('v', 'c'), ('b', 'w'), ('w', 'd'), ('c', 'd')]:
        d.line(pts[edge[0]], pts[edge[1]], TEAL)
    for name, point in pts.items():
        d.node(*point, '' if name in ('b', 'd') else name, boundary=name in 'abcd')
        if name in ('b', 'd'):
            d.text(point[0]+22, point[1]+6, name, 18)
    d.text(417, 447, 'Старая граница (a, b)', 19, anchor='middle')
    d.text(797, 447, 'Новая граница (c, d)', 19, anchor='middle')
    d.text(480, 491, 'Общее ребро ab учитывается один раз: его владелец - левый фрагмент.', 19, MUTED, 'middle')
    d.text(480, 532, 'Сочленить на (a, b) и перенести паспорт на (c, d) - две разные операции.', 19, anchor='middle')
    return d.save('Входная и выходная спектральная граница')


if __name__ == '__main__':
    for draw in (same_passport, two_paths, shared_edge, input_output):
        print(draw().name)
