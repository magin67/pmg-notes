"""Rebuild the three SVG illustrations of the concluding matroid note.

Run: python checks/matroid/draw_gluing_figures.py
Only the standard library and the adjacent Drawing helper are required.
Layouts display graph incidence, not resistance lengths.
"""

from draw_series_figures import Drawing, BLUE, TEAL, GOLD, INK, MUTED


def whitney():
    d = Drawing("Переворот Уитни: один матроид, разная геометрия",
                "Две части являются двухрёберными путями с листом при первом конце. "
                "При прямой склейке листья присоединены к одной вершине C4, при перевороте "
                "к противоположным. Имена рёбер сохраняются. Радиус 13/16 в обоих случаях, "
                "индекс Кирхгофа равен 20 и 21.", 590,
                "Пары граничных вершин фиксированы; меняется только соответствие двух концов.")
    for offset, flipped in ((0, False), (468, True)):
        d.box(24 + offset, 102, 444, 402)
        center = 246 + offset
        d.text(center, 137, "С переворотом" if flipped else "Прямая склейка", 23,
               anchor="middle", weight="700")
        points = {"a": (150 + offset, 250), "b": (350 + offset, 250),
                  "x": (250 + offset, 182), "y": (250 + offset, 335),
                  "p": (70 + offset, 178),
                  "q": ((430 if flipped else 70) + offset, 335)}
        edges = [("a", "x"), ("x", "b"), ("a", "p"),
                 ("b", "y") if flipped else ("a", "y"),
                 ("y", "a") if flipped else ("y", "b"),
                 ("b", "q") if flipped else ("a", "q")]
        shifts = [(0, -11), (0, -11), (-10, 2), (0, 22), (0, 22),
                  (12 if flipped else -12, 7)]
        for i, ((a, b), (dx, dy)) in enumerate(zip(edges, shifts)):
            color = BLUE if i < 3 else TEAL
            d.line(points[a], points[b], color)
            d.text((points[a][0] + points[b][0]) / 2 + dx,
                   (points[a][1] + points[b][1]) / 2 + dy,
                   "ℓ" + "₁₂₃₄₅₆"[i], 20, color, "middle", halo=True)
        offsets = {"a": (-20, 4), "b": (20, 4), "x": (0, -16),
                   "y": (0, 27), "p": (-10, -15), "q": (0, 27)}
        for v, point in points.items():
            d.node(point, v, offsets[v], root=v in ("a", "b"))
        d.text(center, 404, "τ = 4;   ρ = 13/16", 24, anchor="middle", weight="700")
        d.text(center, 443, "R_pq = 3" if flipped else "R_pq = 2", 23, anchor="middle")
        d.text(center, 481, "Kf = 21" if flipped else "Kf = 20", 23, anchor="middle")
    d.text(480, 540, "Цикл: {ℓ₁, ℓ₂, ℓ₄, ℓ₅}. Мосты: ℓ₃, ℓ₆.", 23, anchor="middle")
    d.text(315, 574, "Первая часть", 18, BLUE, "middle")
    d.text(645, 574, "Вторая часть", 18, TEAL, "middle")
    return d.save("Переворот Уитни - один матроид и разная геометрия")


def changed_boundary():
    d = Drawing("Другой выбор границы меняет матроид результата",
                "Один путь P4 с двумя разметками границы. При добавлении пути из двух рёбер "
                "между концами P4 получается C5; при добавлении между вершинами на расстоянии "
                "двух рёбер получается C4 с листом. Остовные числа 5 и 4, радиусы 2/5 и 9/16.",
                660, "Золотые окружности отмечают выбранные вершины; все проводимости равны 1.")
    for offset, short in ((0, False), (468, True)):
        d.box(24 + offset, 102, 444, 530)
        center = 246 + offset
        d.text(center, 140, "Пара на расстоянии 2" if short else "Оба конца пути P₄", 23,
               anchor="middle", weight="700")
        top = [(70 + offset + 110 * i, 210) for i in range(4)]
        for i in range(3):
            d.line(top[i], top[i+1], TEAL)
        for i, point in enumerate(top):
            d.node(point, "v" + "₀₁₂₃"[i], (0, -22), root=i in (0, 2 if short else 3))
        d.text(center, 264, "Тот же P₄, другая разметка", 18, MUTED, "middle")
        d.text(center, 312, "Присоединяем путь P₃", 21, BLUE, "middle")
        lower = [(70 + offset + 110 * i, 398) for i in range(4)]
        for i in range(3):
            d.line(lower[i], lower[i+1], TEAL)
        end = 2 if short else 3
        x = ((lower[0][0] + lower[end][0]) / 2, 510)
        d.line(lower[0], x, BLUE)
        d.line(x, lower[end], BLUE)
        for i, point in enumerate(lower):
            d.node(point, "v" + "₀₁₂₃"[i], (0, -22), root=i in (0, end))
        d.node(x, "x", (0, 27))
        d.text(center, 572, "C₄ с листом" if short else "Цикл C₅", 23,
               anchor="middle", weight="700")
        d.text(center, 611, "τ = 4;   ρ = 9/16" if short else "τ = 5;   ρ = 2/5",
               23, anchor="middle")
    return d.save("Выбор границы - цикл и цикл с листом")


def shared_edge():
    d = Drawing("Общее ребро: три разных закона склейки",
                "Два единичных треугольника склеиваются по вершинам a,b. Две копии ребра ab "
                "сохраняются параллельно, отождествляются в одно единичное ребро или обе "
                "удаляются. Соответствующие остовные числа равны 12, 8 и 4.", 475,
                "Два единичных треугольника; правило для копий ребра ab задаётся отдельно.")
    titles = ["Сохранить обе копии", "Одно ребро c = 1", "Удалить обе копии"]
    for i, (copies, tau) in enumerate(((2, 12), (1, 8), (0, 4))):
        left, center = 24 + 312 * i, 168 + 312 * i
        d.box(left, 101, 288, 314)
        d.text(center, 137, titles[i], 20, anchor="middle", weight="700")
        a, b = (center - 88, 261), (center + 88, 261)
        x, y = (center, 182), (center, 342)
        for u, v, color in ((a, x, BLUE), (x, b, BLUE), (a, y, TEAL), (y, b, TEAL)):
            d.line(u, v, color)
        if copies == 2:
            for bend, color, label_y in ((219, BLUE, 236), (303, TEAL, 299)):
                d.parts.append(f'<path d="M {a[0]} {a[1]} Q {center} {bend} {b[0]} {b[1]}" '
                               f'fill="none" stroke="{color}" stroke-width="4"/>')
                d.text(center, label_y, "1", 19, color, "middle", halo=True)
        elif copies == 1:
            d.line(a, b, GOLD)
            d.text(center, 249, "1", 19, GOLD, "middle", halo=True)
        for name, point in (("a", a), ("b", b), ("x", x), ("y", y)):
            offset = (-21, 6) if name == "a" else ((21, 6) if name == "b" else (0, -16 if name == "x" else 25))
            d.node(point, name, offset, root=name in ("a", "b"))
        d.text(center, 396, "τ = " + str(tau), 25, anchor="middle", weight="700")
    d.text(480, 452, "Две параллельные копии можно заменить одним ребром c = 2.", 20,
           anchor="middle", color=MUTED)
    return d.save("Общее ребро - три разных закона склейки")


if __name__ == "__main__":
    for function in (whitney, changed_boundary, shared_edge):
        print(function())
