"""Rebuild three SVG figures for the PMG resistance-radius note.

Run: python checks/matroid/draw_radius_figures.py
Uses only the standard library and the adjacent SVG drawing helper.
The circle figure uses an exact Euclidean construction (rounded only in SVG).
"""

from fractions import Fraction as Q
from math import sqrt

from draw_series_figures import Drawing, BLUE, TEAL, GOLD, RED, INK, MUTED, GHOST, LIGHT


def resistance_circle():
    a = (0., 0.)
    b = (sqrt(5 / 11), 0.)
    c = (3 / sqrt(55), 1 / sqrt(5))
    center = (sqrt(55) / 22, sqrt(5) / 22)
    centroid = (8 / (3 * sqrt(55)), 1 / (3 * sqrt(5)))
    rho = Q(15, 121)
    dist2 = lambda u, v: sum((x - y) ** 2 for x, y in zip(u, v))
    for u, v, expected in ((a, b, Q(5, 11)), (a, c, Q(4, 11)), (b, c, Q(3, 11))):
        assert abs(dist2(u, v) - expected) < 1e-14
    assert all(abs(dist2(v, center) - rho) < 1e-14 for v in (a, b, c))
    assert all(abs(centroid[i] - (a[i] + b[i] + c[i]) / 3) < 1e-14 for i in (0, 1))

    d = Drawing("От проводимостей к описанной окружности",
                "Слева сеть с проводимостями 1,2,3. Справа точная евклидова реализация: квадраты сторон 5/11,4/11,3/11, квадрат радиуса 15/121. Центр O отличается от центроида h.",
                590, "Сеть показана схематически. Евклидова реализация справа сохраняет длины √R.")
    d.box(24, 96, 444, 374)
    d.box(492, 96, 444, 374)
    d.text(246, 130, "Проводимости рёбер", 23, anchor="middle", weight="700")
    d.text(714, 130, "Резистивная геометрия", 23, anchor="middle", weight="700")
    points = {"a": (246, 182), "b": (96, 376), "c": (396, 376)}
    d.graph(points, [("a", "b"), ("a", "c"), ("b", "c")],
            offsets={"a": (0, -18), "b": (-17, 25), "c": (17, 25)})
    for x, y, value in ((151, 270, "c_ab = 1"), (341, 270, "c_ac = 2"), (246, 365, "c_bc = 3")):
        d.text(x, y, value, 21, anchor="middle", halo=True)

    origin, scale = (714, 320), 420
    def position(v):
        return (origin[0] + scale * (v[0] - center[0]),
                origin[1] - scale * (v[1] - center[1]))
    radius = scale * sqrt(float(rho))
    d.parts.append(f'<circle cx="{origin[0]}" cy="{origin[1]}" r="{radius:.8f}" fill="white" stroke="{BLUE}" stroke-width="2.6"/>')
    euclidean = dict(zip(("A", "B", "C"), map(position, (a, b, c))))
    d.graph(euclidean, [("A", "B"), ("A", "C"), ("B", "C")], color=TEAL,
            offsets={"A": (-16, 24), "B": (16, 24), "C": (0, -17)})
    d.line(origin, euclidean["C"], RED, 2.2, dashed=True)
    d.text(735, 232, "R_sph", 20, RED, halo=True)
    d.node(origin, "O", (-22, 25), color=RED, fill=RED, size=4.5)
    hx, hy = position(centroid)
    d.parts.append(f'<path d="M {hx} {hy-5} L {hx+5} {hy} L {hx} {hy+5} L {hx-5} {hy} Z" fill="{TEAL}"/>')
    d.line((hx + 8, hy - 3), (hx + 35, hy - 13), TEAL, 1.3)
    d.text(hx + 40, hy - 10, "h", 21, TEAL)
    d.text(246, 512, "R_ab = 5/11,   R_ac = 4/11", 21, anchor="middle")
    d.text(246, 548, "R_bc = 3/11", 21, anchor="middle")
    d.text(714, 512, "ρ = 15/121", 25, anchor="middle", weight="700")
    d.text(714, 548, "R_sph = √15 / 11;   O ≠ h", 21, anchor="middle")
    return d.save("Взвешенный треугольник - резистивная окружность")


def euler_count():
    d = Drawing("Почему каждый двухлес учитывается ровно один раз",
                "Фиксированный двухлес с компонентами A={q,a} и B={b,c,d}. В B можно выбрать 3 вершины или удалить 2 ребра. При восстановлении веса разность вкладов равна (3-2)w(F)=w(F).",
                670, "Фиксируем q в A. Все показанные выборы возвращают один и тот же лес F.")
    d.box(30, 102, 330, 145)
    d.box(390, 102, 540, 145)
    d.text(195, 135, "Компонента A", 21, anchor="middle", weight="700")
    d.text(660, 135, "Компонента B", 21, anchor="middle", weight="700")
    d.graph({"q": (105, 201), "a": (285, 201)}, [("q", "a")], roots=("q",))
    d.graph({"b": (480, 201), "c": (660, 201), "d": (840, 201)},
            [("b", "c"), ("c", "d")], color=TEAL)

    d.text(30, 292, "Сумма по вершинам: три выбора", 22, weight="700")
    d.text(930, 292, "+3 w(F)", 24, BLUE, "end", weight="700")
    for i, root in enumerate(("b", "c", "d")):
        cx = 165 + i * 315
        pts = {"b": (cx - 75, 360), "c": (cx, 360), "d": (cx + 75, 360)}
        d.graph(pts, [("b", "c"), ("c", "d")], color=TEAL, roots=(root,))

    d.text(30, 439, "Сумма по рёбрам: два удаления", 22, weight="700")
    d.text(930, 439, "−2 w(F)", 24, RED, "end", weight="700")
    for cx, removed in ((285, ("b", "c")), (675, ("c", "d"))):
        pts = {"b": (cx - 90, 510), "c": (cx, 510), "d": (cx + 90, 510)}
        for e in (("b", "c"), ("c", "d")):
            d.line(pts[e[0]], pts[e[1]], RED if e == removed else TEAL,
                   3 if e == removed else 4, dashed=e == removed)
        for v, p in pts.items():
            d.node(p, v, (0, -21), root=v in removed)
        d.text(cx, 560, "Удалено " + "".join(removed), 20, anchor="middle")
    d.text(480, 630, "(3 − 2) w(F) = w(F)", 28, anchor="middle", weight="700")
    return d.save("Двухлес - подсчёт по вершинам и удалённым рёбрам")


def contributions():
    d = Drawing("Лесной вклад, рёберная поправка и радиус",
                "Столбцы показывают ξ1/3, из которого вычитается H2/12. Для единичного дерева на 4 вершинах, C4, K4 и треугольника с проводимостями 1,2,3 остаются радиусы 3/4,5/16,3/16,15/121.",
                610, "Полный столбец: ξ₁/3. Штрихованная часть вычитается; остаётся ρ.")
    d.parts.append(f'<defs><pattern id="subtract" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#f7dfdb"/><path d="M -2 2 L 2 -2 M 0 8 L 8 0 M 6 10 L 10 6" stroke="{RED}" stroke-width="1.1"/></pattern></defs>')
    d.box(30, 94, 25, 19, TEAL, radius=0)
    d.text(67, 111, "Радиус ρ", 19)
    d.box(300, 94, 25, 19, "url(#subtract)", radius=0)
    d.text(337, 111, "Вычитаем H₂/12", 19)
    start, scale = 250, 650
    for value in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        x = start + scale * float(value)
        d.line((x, 165), (x, 550), "#e0e6eb", 1)
        d.text(x, 153, str(value), 18, MUTED, "middle")
    data = [("P₄ и K₁,₃", Q(3), Q(3), Q(3, 4)),
            ("C₄", Q(3, 2), Q(9, 4), Q(5, 16)),
            ("K₄", Q(15, 16), Q(3, 2), Q(3, 16)),
            ("Треугольник", Q(6, 11), Q(84, 121), Q(15, 121))]
    for i, (label, xi, h2, rho) in enumerate(data):
        left, right = xi / 3, h2 / 12
        assert left - right == rho
        y = 180 + i * 110
        d.text(30, y + 23, label, 23, weight="700")
        if i == 3:
            d.text(30, y + 49, "c = 1, 2, 3", 18, MUTED)
        else:
            d.text(30, y + 49, "c = 1", 18, MUTED)
        d.box(start, y, scale * float(rho), 32, TEAL, radius=0)
        d.box(start + scale * float(rho), y, scale * float(right), 32, "url(#subtract)", radius=0)
        d.box(start, y, scale * float(left), 32, "none", INK, radius=0)
        d.text(start, y + 65, f"ξ₁/3 = {left};   H₂/12 = {right};   ρ = {rho}", 20)
    return d.save("Лесной вклад и рёберная поправка к радиусу")


if __name__ == "__main__":
    for drawing in (resistance_circle, euler_count, contributions):
        print(drawing().name)
