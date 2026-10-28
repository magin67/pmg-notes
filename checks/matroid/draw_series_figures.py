"""Rebuild the nine SVG illustrations of the Russian matroid series.

Run from the repository root: python checks/matroid/draw_series_figures.py
Only the standard library and the companion exact-matrix helper are used.
SVG text stays editable. Node positions show incidence, not resistance lengths.
"""

from fractions import Fraction as Q
from html import escape
from itertools import combinations
from pathlib import Path
import re

from verify_forest_power_sums import greenian, laplacian


OUT = Path(__file__).resolve().parents[2] / "pmg-library/ru/Матроидные параметры и лесные характеристики графов"
INK, MUTED = "#203444", "#566b7b"
BLUE, TEAL, GOLD, RED = "#2767ad", "#167f77", "#b97716", "#b54e45"
GHOST, LIGHT = "#c8d1d9", "#f3f6f9"


class Drawing:
    def __init__(self, title, description, height, subtitle=None):
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">',
            f"<title id=\"title\">{escape(title)}</title>",
            f"<desc id=\"desc\">{escape(description)}</desc>",
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="context-stroke" stroke-width="1.8"/></marker></defs>',
            f'<rect width="960" height="{height}" fill="white"/>',
            '<g font-family="DejaVu Sans, Arial, sans-serif">',
        ]
        self.text(30, 39, title, 27, weight="700")
        if subtitle:
            self.text(30, 72, subtitle, 18, color=MUTED)

    def text(self, x, y, value, size=20, color=INK, anchor="start", weight="400", halo=False):
        halo_style = ' stroke="white" stroke-width="7" stroke-linejoin="round" paint-order="stroke fill"' if halo else ""
        rendered = re.sub(r'([A-Za-zη])_([a-z]+)',
                          r'\1<tspan baseline-shift="sub" font-size="70%">\2</tspan>', escape(str(value)))
        self.parts.append(f'<text id="text{len(self.parts)}" x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}"{halo_style}>{rendered}</text>')

    def box(self, x, y, w, h, fill=LIGHT, stroke="none", radius=12):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def line(self, p, q, color=BLUE, width=4, dashed=False, arrow=False):
        x1, y1 = p
        x2, y2 = q
        if arrow:
            length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
            x2 -= 13 * (x2 - x1) / length
            y2 -= 13 * (y2 - y1) / length
        dash = ' stroke-dasharray="7 7"' if dashed else ""
        marker = ' marker-end="url(#arrow)"' if arrow else ""
        self.parts.append(f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash}{marker}/>')

    def node(self, p, label=None, offset=(0, -18), color=INK, fill="white", root=False, size=7, label_size=19):
        x, y = p
        if root:
            self.parts.append(f'<circle cx="{x}" cy="{y}" r="{size + 6}" fill="white" stroke="{GOLD}" stroke-width="2.8"/>')
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="{fill}" stroke="{color}" stroke-width="2.5"/>')
        if label:
            self.text(x + offset[0], y + offset[1], label, label_size, anchor="middle", halo=True)

    def graph(self, points, edges, selected=None, color=BLUE, labels=True, offsets=None, roots=(), node_colors=None):
        selected = set(edges if selected is None else selected)
        for edge in edges:
            if edge not in selected:
                self.line(points[edge[0]], points[edge[1]], GHOST, 2, dashed=True)
        for a, b in edges:
            if (a, b) in selected:
                self.line(points[a], points[b], color, 4)
        for v, p in points.items():
            self.node(p, v if labels else None, (offsets or {}).get(v, (0, -17)),
                      root=v in roots, color=(node_colors or {}).get(v, INK))

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / (name + ".svg")
        path.write_text("\n".join(self.parts + ["</g>", "</svg>"]) + "\n")
        return path


def triangle(cx, top, radius=85, height=125):
    return {"a": (cx, top), "b": (cx - radius, top + height), "c": (cx + radius, top + height)}


TRI = [("a", "b"), ("a", "c"), ("b", "c")]
TRI_OFFSETS = {"a": (0, -18), "b": (-17, 22), "c": (17, 22)}
SQUARE_EDGES = [("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")]
SQUARE_OFFSETS = {"a": (-16, -16), "b": (16, -16), "c": (16, 25), "d": (-16, 25)}


def square(x, y, size):
    return {"a": (x, y), "b": (x + size, y), "c": (x + size, y + size), "d": (x, y + size)}


def independence():
    d = Drawing("Лес и цикл: независимость рёберных векторов",
                "Два ребра треугольника образуют лес; все три ребра дают зависимость и нулевое внешнее произведение.",
                430, "Ориентация задаёт знаки векторов; независимость набора рёбер от неё не зависит.")
    for x, title in ((24, "Два ребра: лес"), (492, "Три ребра: цикл")):
        d.box(x, 96, 444, 307)
        d.text(x + 222, 130, title, 22, anchor="middle", weight="700")
    for cx, cyclic in ((246, False), (714, True)):
        p = triangle(cx, 175, 120, 120)
        d.line(p["c"], p["a"], RED if cyclic else GHOST, 4 if cyclic else 2, dashed=not cyclic, arrow=cyclic)
        d.line(p["a"], p["b"], RED if cyclic else TEAL, arrow=True)
        d.line(p["b"], p["c"], RED if cyclic else TEAL, arrow=True)
        for v, point in p.items():
            d.node(point, v, TRI_OFFSETS[v])
        d.text(cx, 351, "(ab) + (bc) + (ca) = 0" if cyclic else "(ab)(bc) = (abc) ≠ 0", 22, anchor="middle")
        if cyclic:
            d.text(cx, 384, "(ab)(bc)(ca) = 0", 22, color=RED, anchor="middle")
    return d.save("Лес и цикл - внешние произведения")


def path_star():
    d = Drawing("Один матроид, разная вершинная геометрия",
                "Путь P4 и звезда K1,3 с тремя именованными рёбрами. Соответствие имён сохраняет все независимые наборы, но суммы попарных резистенсов равны 10 и 9.",
                420, "Все проводимости равны 1. Одинаковый цвет и имя показывают соответствие рёбер.")
    d.box(24, 95, 444, 296)
    d.box(492, 95, 444, 296)
    d.text(246, 132, "Путь P₄", 23, anchor="middle", weight="700")
    d.text(714, 132, "Звезда K₁,₃", 23, anchor="middle", weight="700")
    path = {"a": (81, 226), "b": (191, 226), "c": (301, 226), "d": (411, 226)}
    star = {"a": (714, 225), "b": (594, 181), "c": (834, 181), "d": (714, 307)}
    for i, ((a, b), (u, v), color) in enumerate(zip(
            [("a", "b"), ("b", "c"), ("c", "d")],
            [("a", "b"), ("a", "c"), ("a", "d")], (BLUE, TEAL, GOLD)), 1):
        d.line(path[a], path[b], color)
        d.line(star[u], star[v], color)
        d.text((path[a][0] + path[b][0]) / 2, 259, "ℓ" + "₁₂₃"[i-1], 20, color, "middle")
        sx = (star[u][0] + star[v][0]) / 2
        sy = (star[u][1] + star[v][1]) / 2
        d.text(sx + (24 if i == 3 else 0), sy + (0 if i == 3 else 23), "ℓ" + "₁₂₃"[i-1], 20, color, "middle", halo=True)
    for v, p in path.items():
        d.node(p, v)
    for v, p in star.items():
        d.node(p, v, (0, 27) if v == "d" else (0, -18))
    d.text(246, 309, "Любой набор из {ℓ₁, ℓ₂, ℓ₃} независим", 18, anchor="middle")
    d.text(246, 366, "Kf = 10", 24, anchor="middle", weight="700")
    d.text(714, 366, "Kf = 9", 24, anchor="middle", weight="700")
    return d.save("Матроид пути и звезды - соответствие рёбер")


def laplacian_greenian():
    gr = greenian(laplacian(4, [(0, 1, Q(1)), (1, 2, Q(1)), (2, 3, Q(1))]))
    gamma = {(chr(97 + i), chr(97 + j)): -gr[i][j] for i, j in combinations(range(4), 2)}
    assert list(gamma.values()) == [Q(-1, 8), Q(3, 8), Q(5, 8), Q(1, 8), Q(3, 8), Q(-1, 8)]
    assert gr[0][0] + gr[3][3] - 2 * gr[0][3] == 3
    d = Drawing("Проводимости, коэффициенты гриниана и резистенсы",
                "Слева единичный путь abcd. Справа канонические связи гриниана: ab и cd имеют вес минус 1/8, ac и bd — 3/8, ad — 5/8, bc — 1/8. Резистенс ad равен 3.",
                590, "Сплошные связи: положительные коэффициенты. Красный пунктир: отрицательные.")
    d.box(24, 96, 444, 374)
    d.box(492, 96, 444, 374)
    d.text(246, 133, "L: проводимости cᵢⱼ", 22, anchor="middle", weight="700")
    d.text(714, 133, "Gr: коэффициенты γᵢⱼ", 22, anchor="middle", weight="700")
    p = square(112, 192, 252)
    d.graph(p, [("a", "b"), ("b", "c"), ("c", "d")], offsets=SQUARE_OFFSETS)
    for x, y in ((238, 180), (387, 323), (238, 432)):
        d.text(x, y, "1", 21, anchor="middle", halo=True)
    q = square(580, 192, 252)
    positions = {("a", "b"): (706, 180), ("a", "c"): (666, 270), ("a", "d"): (549, 324),
                 ("b", "c"): (864, 324), ("b", "d"): (749, 270), ("c", "d"): (706, 432)}
    for (a, b), value in gamma.items():
        d.line(q[a], q[b], RED if value < 0 else BLUE, 3.4, dashed=value < 0)
    for pair, value in gamma.items():
        x, y = positions[pair]
        d.text(x, y, str(value).replace("-", "−"), 21, RED if value < 0 else BLUE, "middle", halo=True)
    for v, point in q.items():
        d.node(point, v, SQUARE_OFFSETS[v])
    d.text(480, 510, "Rᵢⱼ = Grᵢᵢ + Grⱼⱼ − 2 Grᵢⱼ", 25, anchor="middle")
    d.text(480, 550, "R_ab = R_bc = R_cd = 1;    R_ad = 3", 22, anchor="middle")
    return d.save("Путь P4 - лапласиан и знаковые связи гриниана")


def grades():
    d = Drawing("Грейд, компоненты и когрейд одного леса",
                "В цикле C4 показано по одному лесу грейдов 0,1,2,3. Числа компонент равны 4,3,2,1, когрейды — 3,2,1,0. Во всех рисунках сохранены четыре вершины.",
                440, "Четыре леса в C₄. Пунктир: рёбра исходного графа, не вошедшие в выбранный лес.")
    for g in range(4):
        x = 24 + g * 234
        d.box(x, 100, 210, 288)
        d.text(x + 105, 137, f"g = {g}", 24, anchor="middle", weight="700")
        p = square(x + 53, 185, 104)
        d.graph(p, SQUARE_EDGES, SQUARE_EDGES[:g], TEAL, offsets=SQUARE_OFFSETS)
        d.text(x + 105, 343, f"m = {4-g},   k = {3-g}", 22, anchor="middle")
    d.text(480, 414, "n = 4,   d = 3;     g + m = n,     g + k = d", 21, anchor="middle")
    return d.save("Три индекса лесов цикла C4")


def roots():
    d = Drawing("Один лес: вклад без корней и с выбором корней",
                "Два леса на четырёх вершинах: путь на трёх вершинах и изолированная вершина имеют 3 выбора корней; два отдельных ребра имеют 4. Все варианты корней перечислены.",
                570, "Единичный K₄, грейд g = 2. Золотое кольцо отмечает выбранный корень компоненты.")
    for x, label in ((24, "Компоненты 3 + 1"), (492, "Компоненты 2 + 2")):
        d.box(x, 98, 444, 440)
        d.text(x + 222, 136, label, 23, anchor="middle", weight="700")
    p = {"a": (100, 208), "b": (240, 208), "c": (380, 208), "d": (240, 285)}
    d.graph(p, [("a", "b"), ("b", "c")])
    q = {"a": (610, 203), "b": (810, 203), "c": (610, 285), "d": (810, 285)}
    d.graph(q, [("a", "b"), ("c", "d")], color=TEAL)
    d.text(246, 339, "3 выбора корней", 22, anchor="middle")
    d.text(714, 339, "4 выбора корней", 22, anchor="middle")
    for i, root in enumerate("abc"):
        cx = 99 + i * 145
        small = {"a": (cx - 40, 391), "b": (cx, 391), "c": (cx + 40, 391), "d": (cx, 445)}
        d.graph(small, [("a", "b"), ("b", "c")], labels=False, roots=(root, "d"))
    for i, (r1, r2) in enumerate((("a", "c"), ("a", "d"), ("b", "c"), ("b", "d"))):
        cx = 552 + i * 108
        small = {"a": (cx - 27, 391), "b": (cx + 27, 391), "c": (cx - 27, 445), "d": (cx + 27, 445)}
        d.graph(small, [("a", "b"), ("c", "d")], color=TEAL, labels=False, roots=(r1, r2))
    d.text(246, 510, "Вклад в f₂: 1;   в p₂: 3", 22, anchor="middle", weight="700")
    d.text(714, 510, "Вклад в f₂: 1;   в p₂: 4", 22, anchor="middle", weight="700")
    return d.save("Обычные и корневые леса - два типа компонент")


def gluing():
    d = Drawing("Одноточечное сочленение: лес выбирается по частям",
                "Лес первого треугольника содержит два ребра, лес второго — одно. После отождествления выбранных вершин их объединение остаётся лесом. Грейды и когрейды складываются.",
                685, "Показан один выбор пары лесов. Пунктир сохраняет видимость остальных рёбер частей.")
    d.text(240, 111, "G₁:  g₁ = 2,  k₁ = 0", 22, anchor="middle", weight="700")
    d.text(720, 111, "G₂:  g₂ = 1,  k₂ = 1", 22, anchor="middle", weight="700")
    left = {"p₁": (240, 167), "a": (120, 282), "b": (360, 282)}
    right = {"p₂": (720, 167), "c": (600, 282), "d": (840, 282)}
    d.graph(left, [("p₁", "a"), ("a", "b"), ("b", "p₁")], [("p₁", "a"), ("a", "b")])
    d.graph(right, [("p₂", "c"), ("c", "d"), ("d", "p₂")], [("p₂", "c")], TEAL)
    d.text(480, 335, "Отождествляем p₁ и p₂", 21, anchor="middle")
    d.line((480, 351), (480, 400), MUTED, 2.4, arrow=True)
    p = {"p": (480, 499), "a": (280, 423), "b": (280, 575), "c": (680, 423), "d": (680, 575)}
    for a, b in [("b", "p"), ("c", "d"), ("d", "p")]:
        d.line(p[a], p[b], GHOST, 2, dashed=True)
    for a, b in [("p", "a"), ("a", "b")]:
        d.line(p[a], p[b], BLUE)
    d.line(p["p"], p["c"], TEAL)
    for v, point in p.items():
        d.node(point, v, (0, 28) if v == "p" else (-20 if v in "ab" else 20, 5))
    d.text(480, 630, "G = G₁ ∨ G₂:   g = 3,   k = 1", 23, anchor="middle", weight="700")
    d.text(480, 665, "F = F₁ ∪ F₂;   g = g₁ + g₂;   k = k₁ + k₂", 21, anchor="middle")
    return d.save("Леса при одноточечном сочленении")


def extensions():
    d = Drawing("Какие рёбра можно добавить к лесу?",
                "В единичном K4 у леса типа 3+1 три допустимых ребра, у типа 2+2 четыре. Всего таких лесов соответственно 12 и 3, среднее A равно 16/5.",
                615, "Синий: рёбра леса. Золотой пунктир: допустимое добавление. Серый пунктир: возник бы цикл.")
    for x, title in ((24, "Компоненты 3 + 1"), (492, "Компоненты 2 + 2")):
        d.box(x, 98, 444, 401)
        d.text(x + 222, 136, title, 22, anchor="middle", weight="700")
    all_edges = list(combinations("abcd", 2))
    for x, selected, groups in (
            (120, {("a", "b"), ("b", "c")}, {"a": 0, "b": 0, "c": 0, "d": 1}),
            (588, {("a", "b"), ("c", "d")}, {"a": 0, "b": 0, "c": 1, "d": 1})):
        p = square(x, 193, 236)
        allowed = [e for e in all_edges if groups[e[0]] != groups[e[1]]]
        for a, b in all_edges:
            if (a, b) not in selected:
                d.line(p[a], p[b], GOLD if (a, b) in allowed else GHOST, 3.3 if (a, b) in allowed else 2, dashed=True)
        for a, b in selected:
            d.line(p[a], p[b], BLUE, 5)
        for v, point in p.items():
            d.node(point, v, SQUARE_OFFSETS[v], BLUE if groups[v] == 0 else TEAL,
                   "#e9f1fb" if groups[v] == 0 else "#e4f4ef", size=10)
        d.text(x + 118, 480, f"A(F) = {len(allowed)}", 23, anchor="middle", weight="700")
    d.text(246, 529, "12 лесов этого типа", 21, anchor="middle")
    d.text(714, 529, "3 леса этого типа", 21, anchor="middle")
    d.text(480, 575, "E₁ A = (12 · 3 + 3 · 4) / 15 = 16/5;     ξ₁ = 15/16", 22, anchor="middle")
    return d.save("Допустимые расширения двухлесов K4")


TREE_EDGES = [TRI[:2], [TRI[0], TRI[2]], TRI[1:]]
TREE_WEIGHTS = [Q(2), Q(3), Q(6)]
CONDUCTANCE = dict(zip(TRI, (Q(1), Q(2), Q(3))))


def random_trees():
    assert [sum(w for t, w in zip(TREE_EDGES, TREE_WEIGHTS) if e in t) / 11 for e in TRI] == [Q(5, 11), Q(8, 11), Q(9, 11)]
    d = Drawing("Взвешенный треугольник и его три остовных дерева",
                "Проводимости ab, ac, bc равны 1,2,3. Три дерева имеют веса 2,3,6 и вероятности 2/11,3/11,6/11. Суммирование даёт вероятности включения рёбер 5/11,8/11,9/11.",
                625, "Остовной вес τ = 2 + 3 + 6 = 11. Вероятность дерева равна его весу, делённому на τ.")
    p = triangle(180, 132, 100, 140)
    d.graph(p, TRI, offsets=TRI_OFFSETS)
    for x, y, value in ((111, 194, "c_ab = 1"), (247, 194, "c_ac = 2"), (180, 260, "c_bc = 3")):
        d.text(x, y, value, 18, anchor="middle", halo=True)
    for y, value in ((155, "η_ab = 2/11 + 3/11 = 5/11"),
                     (215, "η_ac = 2/11 + 6/11 = 8/11"),
                     (275, "η_bc = 3/11 + 6/11 = 9/11")):
        d.text(390, y, value, 25)
    for i, (edges, weight) in enumerate(zip(TREE_EDGES, TREE_WEIGHTS)):
        x, cx = 24 + 312 * i, 168 + 312 * i
        d.box(x, 335, 288, 262)
        d.text(cx, 370, "T" + "₁₂₃"[i], 23, anchor="middle", weight="700")
        p = triangle(cx, 413, 80, 105)
        d.graph(p, TRI, edges, TEAL, offsets=TRI_OFFSETS)
        d.text(cx, 575, f"w = {weight};   p = {weight}/11", 22, anchor="middle", weight="700")
    return d.save("Три случайных дерева взвешенного треугольника")


def intersections():
    d = Drawing("Пересечение двух независимо выбранных деревьев",
                "Девять упорядоченных пар трёх деревьев треугольника. В ячейке показаны общие рёбра и сумма их собственных сопротивлений. Среднее с весами произведений вероятностей равно 84/121.",
                800, "Строка: первое дерево. Столбец: второе дерево. Каждая ячейка имеет вероятность pᵢ pⱼ.")
    probs = [w / 11 for w in TREE_WEIGHTS]
    h2 = Q(0)
    for j, weight in enumerate(TREE_WEIGHTS):
        cx = 330 + 234 * j
        d.text(cx, 123, "T" + "₁₂₃"[j], 23, anchor="middle", weight="700")
        d.text(cx, 154, f"p = {weight}/11", 20, anchor="middle")
    for i, weight in enumerate(TREE_WEIGHTS):
        y = 180 + 173 * i
        d.text(95, y + 72, "T" + "₁₂₃"[i], 23, anchor="middle", weight="700")
        d.text(95, y + 105, f"p = {weight}/11", 20, anchor="middle")
        for j in range(3):
            cx = 330 + 234 * j
            d.box(cx - 108, y, 216, 162, LIGHT if i == j else "#fafcfd", "#dce3e9")
            common = set(TREE_EDGES[i]) & set(TREE_EDGES[j])
            value = sum((1 / CONDUCTANCE[e] for e in common), Q(0))
            h2 += probs[i] * probs[j] * value
            p = triangle(cx, y + 36, 50, 63)
            d.graph(p, TRI, common, TEAL, labels=False)
            d.text(cx, y + 143, f"Σ 1/c = {value}", 21, anchor="middle")
    assert h2 == Q(84, 121)
    d.text(480, 745, "H₂ = Σᵢⱼ pᵢ pⱼ · (сумма в ячейке) = 84/121", 25, anchor="middle", weight="700")
    d.text(480, 780, "Серый пунктир: рёбра, не вошедшие в пересечение.", 19, color=MUTED, anchor="middle")
    return d.save("Пересечения деревьев и параметр H2")


def main():
    for draw in (independence, path_star, laplacian_greenian, grades, roots,
                 gluing, extensions, random_trees, intersections):
        print(draw().name)


if __name__ == "__main__":
    main()
