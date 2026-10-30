"""Draw five native SVG figures using only the standard library.

Run from the repository root: python checks/boundary/draw_forest_states.py
Coordinates depict graph incidence, not resistance distances.
"""

from html import escape
from pathlib import Path
from verify_forest_states import forests, state_name

OUT = Path(__file__).resolve().parents[2] / 'pmg-library/ru/Граничные полиномы и сочленение графов'
INK, MUTED, TEAL, GOLD = '#203444', '#566b7b', '#167f77', '#b97716'
PURPLE, BLUE, GHOST, LIGHT = '#9464af', '#2767ad', '#c8d1d9', '#f3f6f9'
EDGES = [(a, b, 1) for a, b in zip('abcde', 'bcde')]
RECORDS = {sum(1 << i for i in f['selected']): f for f in forests('abcde', EDGES, 'ace')}


class Drawing:
    def __init__(self, title, desc, height, subtitle):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title>',
                      f'<desc id="desc">{escape(desc)}</desc>',
                      f'<rect width="960" height="{height}" fill="white"/>',
                      '<g font-family="DejaVu Sans, Arial, sans-serif">']
        self.text(28, 40, title, 27, weight='700')
        self.text(28, 73, subtitle, 17, MUTED)

    def text(self, x, y, text, size=19, color=INK, anchor='start', weight='400'):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(str(text))}</text>')

    def box(self, x, y, w, h, fill=LIGHT):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>')

    def line(self, a, b, color=TEAL, width=4, dashed=False):
        dash = ' stroke-dasharray="5 6"' if dashed else ''
        self.parts.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash}/>')

    def circle(self, x, y, radius, fill='white', stroke=INK, width=2):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')

    def node(self, x, y, label, boundary=False, internal=False, size=7, label_size=18):
        if boundary:
            self.circle(x, y, size + 6, stroke=GOLD, width=2.6)
        if internal:
            self.circle(x, y, size + 6, fill='#f2e8fa', stroke=PURPLE)
        self.circle(x, y, size, fill=PURPLE if internal else 'white', width=2)
        self.text(x, y - 20, label, label_size, anchor='middle')

    def forest(self, x, y, width, mask, labels='abcde', small=False):
        record = RECORDS[mask]
        internal = set().union(*record['internal']) if record['internal'] else set()
        pts = [(x + i * width / 4, y) for i in range(5)]
        for i in range(4):
            present = bool(mask & (1 << i))
            self.line(pts[i], pts[i + 1], TEAL if present else GHOST, 3.5 if present else 1.5, not present)
        for i, (px, py) in enumerate(pts):
            self.node(px, py, labels[i], boundary=i in (0, 2, 4), internal='abcde'[i] in internal,
                      size=5 if small else 7, label_size=15 if small else 18)
        return pts

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / (name + '.svg')
        path.write_text('\n'.join(self.parts + ['</g>', '</svg>']) + '\n', encoding='utf-8')
        return path


def graph_boundary():
    d = Drawing('Путь P₅ с трёхточечной границей',
                'Путь a-b-c-d-e с единичными проводимостями. Граница состоит из a,c,e; b,d являются внутренними вершинами.',
                320, 'B = {a, c, e}; все проводимости равны 1.')
    d.forest(95, 171, 770, 15)
    for i in range(4):
        d.text(95 + (i + .5) * 770 / 4, 157, '1', 18, MUTED, 'middle')
    d.text(480, 247, 'Золотые окружности: граница. Внутренние вершины: b, d.', 20, anchor='middle')
    d.text(480, 286, 'Каждый остовной лес сохраняет все пять вершин.', 19, MUTED, 'middle')
    return d.save('Путь P5 с трёхточечной границей')


def five_partitions():
    d = Drawing('Пять разбиений границы {a, c, e}',
                'Пять формальных состояний: ace, ac|e, ae|c, a|ce, a|c|e. Цветные области обозначают блоки, а не рёбра. Состояние ae|c на пути P5 невозможно.',
                426, 'Расположение трёх вершин одинаково; меняется только разбиение на блоки.')
    for i, state in enumerate(['ace', 'ac|e', 'ae|c', 'a|ce', 'a|c|e']):
        x, cx = 20 + 186 * i, 106 + 186 * i
        d.box(x, 106, 176, 253)
        d.text(cx, 140, state, 23, anchor='middle', weight='700')
        points = {'a': (cx - 42, 269), 'c': (cx, 207), 'e': (cx + 42, 269)}
        for block, color in zip(state.split('|'), ['#cbe7e0', '#d9e5f8', '#f3dfb9']):
            ps = [points[v] for v in block]
            if len(ps) == 3:
                coords = ' '.join(f'{a},{b}' for a, b in ps)
                d.parts.append(f'<polygon points="{coords}" fill="{color}" stroke="{color}" stroke-width="25" stroke-linejoin="round"/>')
            elif len(ps) == 2:
                d.line(ps[0], ps[1], color, 35)
            else:
                d.circle(*ps[0], 18, fill=color, stroke=color)
        for label, p in points.items():
            d.node(*p, label, size=5)
        d.text(cx, 333, 'на P₅ невозможно' if state == 'ae|c' else f"блоков: {len(state.split('|'))}", 16,
               PURPLE if state == 'ae|c' else MUTED, 'middle')
    d.text(480, 398, 'Цветные области - блоки разбиения; они не изображают рёбра графа.', 19, MUTED, 'middle')
    return d.save('Пять разбиений трёхточечной границы')


def three_forests():
    d = Drawing('Три леса одного состояния ac|e',
                'Рёбра ab,bc обязательны. Справа выбран пустой набор, cd или de. Первый лес имеет внутреннюю компоненту d и даёт t^2; два других являются рощами и дают по t^3.',
                455, 'Во всех трёх лесах a соединена с c, а e принадлежит другой компоненте.')
    for i, mask in enumerate([3, 7, 11]):
        x, cx = 24 + 312 * i, 168 + 312 * i
        r = RECORDS[mask]
        assert state_name(r['state']) == 'ac|e'
        d.box(x, 108, 288, 257)
        d.text(cx, 146, ['Выбраны ab, bc', 'Добавлено cd', 'Добавлено de'][i], 21, anchor='middle', weight='700')
        d.forest(x + 30, 220, 228, mask)
        d.text(cx, 279, 'вклад: t²' if i == 0 else 'вклад: t³', 23, anchor='middle')
        d.text(cx, 318, 'внутренняя компонента {d}' if i == 0 else 'роща: внутренних компонент нет', 15,
               PURPLE if i == 0 else TEAL, 'middle')
        d.text(cx, 347, 'k₀ = 1' if i == 0 else 'k₀ = 0', 17, MUTED, 'middle')
    d.text(480, 406, 'Полином состояния: t² + t³ + t³ = t²(1 + 2t).', 23, anchor='middle')
    d.text(480, 439, 'Фиолетовый цвет: внутренняя компонента. Пунктир: невыбранное ребро.', 17, MUTED, 'middle')
    return d.save('Три леса одного граничного состояния')


def nine_forests():
    d = Drawing('Девять лесов состояния a|c|e',
                'Сетка трёх выборов слева: пустой набор, ab, bc; и трёх справа: пустой набор, cd, de. Получаются один лес с нулём рёбер, четыре с одним и четыре с двумя. Последние четыре являются рощами.',
                800, 'Строки: выбор на a-b-c. Столбцы: выбор на c-d-e. Все веса равны 1.')
    right_names, left_names = ['ничего', 'cd', 'de'], ['ничего', 'ab', 'bc']
    for j in range(3):
        d.text(286 + 260 * j, 130, right_names[j], 21, anchor='middle', weight='700')
    for i, left in enumerate([0, 1, 2]):
        d.text(76, 233 + 180 * i, left_names[i], 20, anchor='middle', weight='700')
        for j, right in enumerate([0, 4, 8]):
            x, y, mask = 162 + 260 * j, 155 + 180 * i, left | right
            r = RECORDS[mask]
            assert state_name(r['state']) == 'a|c|e'
            d.box(x, y, 248, 157)
            d.forest(x + 28, y + 63, 192, mask, small=True)
            monomial = ['1', 't', 't²'][r['g']]
            d.text(x + 124, y + 105, f"вклад: {monomial};  k₀ = {len(r['internal'])}", 18, anchor='middle')
            d.text(x + 124, y + 136, 'роща' if not r['internal'] else 'есть внутренняя компонента', 15,
                   TEAL if not r['internal'] else PURPLE, 'middle')
    d.text(480, 730, '(1 + 2t)(1 + 2t) = 1 + 4t + 4t²', 25, anchor='middle')
    d.text(480, 772, 'Фиолетовый цвет: внутренняя компонента. Пунктир: невыбранное ребро.', 17, MUTED, 'middle')
    return d.save('Девять лесов раздельной границы')


def same_partner():
    d = Drawing('Один партнёр и две разметки пути',
                'Партнёр J содержит единичное ребро xy и изолированную граничную вершину z. При присоединении к пути x-b-y-d-z возникает треугольник с хвостом, а к x-b-z-d-y - цикл C5. Общих рёбер нет; имена x,y,z отождествляются.',
                766, 'B = {x, y, z}; отождествляются одноимённые вершины, каждое ребро учитывается один раз.')
    d.text(230, 143, 'Партнёр J:', 21, BLUE)
    d.line((420, 150), (535, 150), BLUE)
    for v, x in zip('xyz', [420, 535, 710]):
        d.node(x, 150, v, boundary=True)
    d.text(477, 180, '1', 17, BLUE, 'middle')
    for i, labels in enumerate(['xbydz', 'xbzdy']):
        x, cx = 24 + 468 * i, 246 + 468 * i
        d.box(x, 208, 444, 483)
        d.text(cx, 246, 'Часть X' if i == 0 else 'Часть X′', 24, anchor='middle', weight='700')
        d.forest(x + 42, 316, 360, 15, labels=labels)
        d.text(cx, 367, 'F(t) = (1 + t)⁴', 23, anchor='middle')
        d.text(cx, 415, 'После присоединения J', 19, BLUE, 'middle')
        points = [(x + 42 + j * 90, 485) for j in range(5)]
        endpoint = 2 if i == 0 else 4
        a, b = points[0], points[endpoint]
        d.parts.append(f'<path d="M {a[0]} {a[1]} Q {(a[0] + b[0]) / 2} 617 {b[0]} {b[1]}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
        d.forest(x + 42, 485, 360, 15, labels=labels)
        d.text(cx, 597, 'Треугольник с хвостом' if i == 0 else 'Цикл C₅', 22, anchor='middle', weight='700')
        d.text(cx, 635, '1 + 5t + 10t² + 9t³ + 3t⁴' if i == 0 else '1 + 5t + 10t² + 10t³ + 5t⁴', 21, anchor='middle')
        d.text(cx, 672, 'τ = 3' if i == 0 else 'τ = 5', 22, TEAL, 'middle')
    d.text(480, 737, 'Одинаковые лесные полиномы частей дают разные полиномы сочленений.', 20, MUTED, 'middle')
    return d.save('Один партнёр и две разметки пути')


if __name__ == '__main__':
    for draw in [graph_boundary, five_partitions, three_forests, nine_forests, same_partner]:
        print(draw())
