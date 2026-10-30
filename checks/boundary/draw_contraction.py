"""Draw three native SVG figures for the boundary contraction note.

Run from the repository root: python checks/boundary/draw_contraction.py
Uses the drawing primitives of the first note; no third-party packages.
"""

from draw_forest_states import Drawing, INK, MUTED, TEAL, GOLD, PURPLE


def curve(d, path, color=TEAL, width=4):
    d.parts.append(f'<path d="{path}" fill="none" stroke="{color}" '
                   f'stroke-width="{width}" stroke-linecap="round"/>')


def between_blocks():
    d = Drawing('Цикл между двумя стягиваемыми блоками',
                'Исходный лес содержит ac и bd. Золотой пунктир ab и cd задаёт два блока отождествления. '
                'После стягивания выбранные рёбра образуют параллельную пару между h1 и h2, то есть цикл.',
                490, 'π = ac|bd;  σ = ab|cd.  Отдельные блоки проходят проверку, вся система - нет.')
    d.box(24, 108, 408, 280)
    d.box(528, 108, 408, 280)
    d.text(228, 148, 'Лес и пары отождествления', 21, anchor='middle', weight='700')
    d.line((128, 218), (128, 327))
    d.line((328, 218), (328, 327))
    d.line((128, 218), (328, 218), GOLD, dashed=True)
    d.line((128, 327), (328, 327), GOLD, dashed=True)
    for label, x, y in [('a', 128, 218), ('b', 328, 218), ('c', 128, 327), ('d', 328, 327)]:
        d.node(x, y, label if y == 218 else '')
        if y == 327:
            d.text(x, y + 30, label, 18, anchor='middle')
    d.text(480, 270, '→', 42, MUTED, 'middle')
    d.text(732, 148, 'После отождествления', 21, anchor='middle', weight='700')
    curve(d, 'M 630 272 Q 732 178 834 272')
    curve(d, 'M 630 272 Q 732 366 834 272')
    d.node(630, 272, 'h₁', boundary=True)
    d.node(834, 272, 'h₂', boundary=True)
    d.text(732, 209, 'ac', 18, TEAL, 'middle')
    d.text(732, 347, 'bd', 18, TEAL, 'middle')
    d.text(630, 307, '{a, b}', 17, MUTED, 'middle')
    d.text(834, 307, '{c, d}', 17, MUTED, 'middle')
    d.text(480, 429, 'r(π) + r(σ) = 2 + 2 > 3 = r(π ∨ σ)', 25, PURPLE, 'middle')
    d.text(480, 468, 'Пунктир задаёт отождествления и не является ребром исходного графа.', 18, MUTED, 'middle')
    return d.save('Цикл между двумя стягиваемыми блоками')


def path_contractions():
    d = Drawing('Три стягивания границы пути P₅',
                'Путь a-b-c-d-e имеет границу a,c,e и единичные веса. После a=c получаются связь h-b веса 2 '
                'и путь h-d-e; после a=e получается цикл C4; после a=c=e получаются связи h-b и h-d веса 2. '
                'Полиномы соответственно (1+2t)(1+t)^2, (1+t)^4-t^4 и (1+2t)^2.',
                645, 'B = {a, c, e}; исходные проводимости равны 1. Граничные вершины отмечены золотом.')
    d.forest(120, 151, 720, 15)
    for i in range(3):
        d.box(24 + i * 312, 210, 288, 348)
    d.text(168, 250, 'a = c', 24, anchor='middle', weight='700')
    d.text(480, 250, 'a = e', 24, anchor='middle', weight='700')
    d.text(792, 250, 'a = c = e', 24, anchor='middle', weight='700')
    # First quotient: double edge h-b, and path h-d-e.
    ps = {'b': (68, 374), 'h': (135, 374), 'd': (202, 374), 'e': (269, 374)}
    for a, b in [('b', 'h'), ('h', 'd'), ('d', 'e')]:
        d.line(ps[a], ps[b])
    for label, p in ps.items():
        d.node(*p, label, boundary=label in 'he')
    for x, label in [(101, '2'), (168, '1'), (235, '1')]:
        d.text(x, 407, label, 18, MUTED, 'middle')
    d.text(168, 292, 'h = {a, c}', 18, MUTED, 'middle')
    # Second quotient: four-cycle h-b-c-d-h.
    ps = {'h': (410, 330), 'b': (550, 330), 'c': (550, 425), 'd': (410, 425)}
    for a, b in [('h', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'h')]:
        d.line(ps[a], ps[b])
    for label, p in ps.items():
        d.node(*p, label if p[1] == 330 else '', boundary=label in 'hc')
        if p[1] == 425:
            d.text(p[0], p[1] + 29, label, 18, anchor='middle')
    d.text(480, 385, 'C₄', 23, MUTED, 'middle')
    d.text(480, 292, 'h = {a, e}', 18, MUTED, 'middle')
    # Third quotient: two doubled spokes, drawn as weighted edges.
    ps = {'b': (702, 374), 'h': (792, 374), 'd': (882, 374)}
    d.line(ps['b'], ps['h'])
    d.line(ps['h'], ps['d'])
    for label, p in ps.items():
        d.node(*p, label, boundary=label == 'h')
    for x in [747, 837]:
        d.text(x, 407, '2', 18, MUTED, 'middle')
    d.text(792, 292, 'h = {a, c, e}', 18, MUTED, 'middle')
    for x, f, top in [(168, '(1 + 2t)(1 + t)²', 'степень 3;  τ = 2'),
                       (480, '(1 + t)⁴ − t⁴', 'степень 3;  τ = 4'),
                       (792, '(1 + 2t)²', 'степень 2;  τ = 4')]:
        d.text(x, 492, f, 23, anchor='middle')
        d.text(x, 533, top, 19, TEAL, 'middle')
    d.text(480, 600, 'Два параллельных единичных ребра заменены связью проводимости 2.', 19, MUTED, 'middle')
    d.text(480, 631, 'Полиномы учитывают все остовные леса, включая внутренние компоненты.', 18, MUTED, 'middle')
    return d.save('Три стягивания трёхточечной границы P5')


def loops_and_parallel_edges():
    d = Drawing('Петля и параллельные рёбра после стягивания',
                'Треугольник с проводимостями ab=2, ac=3, bc=5. После a=b ребро ab становится петлёй веса 2, '
                'а ac,bc становятся параллельными рёбрами весов 3 и 5. Петля исключается из лесов. '
                'Параллельные рёбра можно заменить одним весом 8; лесной полином равен 1+8t.',
                505, 'Отождествляем a и b в h; метки и веса рёбер сначала сохраняются.')
    for x in [24, 349, 674]:
        d.box(x, 111, 262, 290)
    for x, title in [(155, 'Исходный граф'), (480, 'Перенос рёбер'), (805, 'Сумма весов')]:
        d.text(x, 151, title, 21, anchor='middle', weight='700')
    a, b, c = (89, 235), (221, 235), (155, 343)
    for p, q in [(a,b),(a,c),(b,c)]:
        d.line(p, q)
    for label,p in [('a',a),('b',b),('c',c)]:
        d.node(*p, label if label != 'c' else '', boundary=label in 'ab')
    d.text(155, 372, 'c', 18, anchor='middle')
    d.text(155, 225, '2', 19, MUTED, 'middle')
    d.text(100, 307, '3', 19, MUTED, 'middle')
    d.text(210, 307, '5', 19, MUTED, 'middle')
    for x in [318, 643]:
        d.text(x, 287, '→', 35, MUTED, 'middle')
    curve(d, 'M 412 283 Q 480 196 548 283')
    curve(d, 'M 412 283 Q 480 370 548 283')
    curve(d, 'M 412 283 C 357 280 363 207 412 226 C 442 239 425 266 412 283', MUTED, 2.5)
    d.node(412, 283, '', boundary=True)
    d.text(412, 315, 'h', 18, anchor='middle')
    d.node(548, 283, 'c')
    d.text(480, 230, '3', 19, TEAL, 'middle')
    d.text(480, 347, '5', 19, TEAL, 'middle')
    d.text(379, 207, '2', 18, MUTED, 'middle')
    d.line((376, 230), (395, 250), PURPLE, 2.5)
    d.line((395, 230), (376, 250), PURPLE, 2.5)
    d.text(480, 381, 'петля в лес не входит', 17, PURPLE, 'middle')
    d.line((733, 283), (877, 283))
    d.node(733, 283, 'h', boundary=True)
    d.node(877, 283, 'c')
    d.text(805, 264, '3 + 5 = 8', 20, TEAL, 'middle')
    d.text(805, 344, 'F(t) = 1 + 8t', 23, anchor='middle')
    d.text(480, 445, 'Из параллельной пары можно выбрать не более одного ребра.', 21, anchor='middle')
    d.text(480, 481, 'Член 15t² означал бы цикл из двух рёбер и поэтому исключается.', 19, MUTED, 'middle')
    return d.save('Петля и параллельные рёбра после стягивания')


if __name__ == '__main__':
    for draw in [between_blocks, path_contractions, loops_and_parallel_edges]:
        print(draw())
