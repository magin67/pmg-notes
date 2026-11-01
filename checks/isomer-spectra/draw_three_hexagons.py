"""Reproduce the note's SVG figures with Python's standard library."""
from html import escape
from math import cos, sin, pi
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / 'pmg-library/ru/Инварианты, разложения и спектры/Спектры изомеров'
INK, MUTED, EDGE = '#172b43', '#52657a', '#52657a'
RED, BLUE, GREEN = '#bc294b', '#196bb9', '#15815b'
FILLS = ['#fff0d7', '#ddf4e9', '#e2edff']


class SVG:
    def __init__(self, w, h, title, desc):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
                      f'<rect width="{w}" height="{h}" fill="white"/>',
                      '<g font-family="DejaVu Sans, Arial, sans-serif">']

    def text(self, x, y, t, size=20, color=INK, anchor='start', weight='normal'):
        self.parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(t)}</text>')

    def line(self, a, b, color=EDGE, width=3):
        self.parts.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>')

    def polygon(self, ps, fill):
        self.parts.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x, y in ps)+f'" fill="{fill}"/>')

    def circle(self, p, r=5, fill=INK, stroke='none', width=2):
        self.parts.append(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')

    def panel(self, x, y, w, h):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#f7f9fc" stroke="#dce4ed"/>')

    def arrow(self, a, b):
        self.line(a, b, INK, 3)
        dx, dy = b[0]-a[0], b[1]-a[1]
        length = (dx*dx+dy*dy)**.5
        dx, dy = dx/length, dy/length
        self.polygon([b, (b[0]-12*dx+5*dy, b[1]-12*dy-5*dx),
                         (b[0]-12*dx-5*dy, b[1]-12*dy+5*dx)], INK)

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT/name).write_text('\n'.join(self.parts+['</g></svg>'])+'\n', encoding='utf-8')


def ring(cx, cy, r):
    return {i: (cx+r*cos(pi/3-i*pi/3), cy+r*sin(pi/3-i*pi/3)) for i in range(6)}


def reflect(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    t = ((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)
    return 2*(a[0]+t*dx)-p[0], 2*(a[1]+t*dy)-p[1]


def pair_positions(cx, cy, r, start):
    p = ring(cx, cy, r)
    for a, ids in [(0, [9, 8, 7, 6]), (start, [13, 12, 11, 10])]:
        for k, v in enumerate(ids, 2):
            p[v] = reflect(p[(a+k) % 6], p[a], p[(a+1) % 6])
    return p


def draw_pair(s, cx, cy, r, start):
    cores = [[0, 1, 9, 8, 7, 6], [0, 1, 2, 3, 4, 5],
             [start, start+1, 13, 12, 11, 10]]
    p = pair_positions(cx, cy, r, start)
    edges = {tuple(sorted((a, b))) for c in cores for a, b in zip(c, c[1:]+c[:1])}
    assert len(edges) == 16 and len(p) == 14
    centers = []
    for i, c in enumerate(cores):
        s.polygon([p[v] for v in c], FILLS[i])
        center = tuple(sum(p[v][j] for v in c)/6 for j in [0, 1])
        centers.append(center)
        s.text(center[0], center[1]+7, 'K'+str(i+1), 24, anchor='middle', weight='bold')
    for a, b in sorted(edges):
        s.line(p[a], p[b])
    for (a, b), color in [((0, 1), RED), ((start, start+1), BLUE)]:
        s.line(p[a], p[b], color, 6)
    seam = {0, 1, start, start+1}
    for v, pt in p.items():
        s.circle(pt, 7 if v in seam else 4.5, 'white' if v in seam else INK, INK)
        center = centers[1] if v < 6 else centers[0 if v < 10 else 2]
        dx, dy = (pt[0]-center[0])/r, (pt[1]-center[1])/r
        s.text(pt[0]+19*dx, pt[1]+19*dy+6, str(v), 18, anchor='middle')


def seams():
    s = SVG(1160, 650, 'Два изомера трёх шестиугольников',
            'В А швы среднего ядра 01 и 34, в Б — 01 и 23. На вершинах степени три получаются два отдельных ребра и путь.')
    for x, label, start in [(20, 'А · противоположные швы', 3), (600, 'Б · смещённый шов', 2)]:
        s.panel(x, 18, 540, 614)
        s.text(x+25, 55, label, 25, weight='bold')
        draw_pair(s, x+270+(24 if start == 2 else 0), 275, 68, start)
        s.text(x+270, 451, 'Подграф на вершинах степени 3', 20, MUTED, 'middle')
        xs = [x+100, x+205, x+335, x+440]
        ids = [0, 1, 3, 4] if start == 3 else [0, 1, 2, 3]
        for i in [0, 2]:
            s.line((xs[i], 507), (xs[i+1], 507), RED if i == 0 else BLUE, 5)
        if start == 2:
            s.line((xs[1], 507), (xs[2], 507), EDGE, 4)
        for xx, v in zip(xs, ids):
            s.circle((xx, 507), 7, 'white', INK)
            s.text(xx, 541, str(v), 20, anchor='middle')
        s.text(x+270, 594, '2 ребра' if start == 3 else '3 ребра', 24, anchor='middle', weight='bold')
    s.save('Швы и вершины степени три.svg')


def forest_weights():
    s = SVG(1200, 550, 'Корневые веса четырёхрёберных лесов',
            'Пять типов размеров компонент: 5; 4,2; 3,3; 3,2,2; 2,2,2,2. Их корневые веса равны 5,8,9,12,16. Зелёным отмечен один пример выбора корней.')
    s.text(600, 38, 'Четыре ребра · пять типов размеров компонент', 25, anchor='middle', weight='bold')
    shapes = [(5,), (4, 2), (3, 3), (3, 2, 2), (2, 2, 2, 2)]
    counts_a, counts_b = [56, 314, 133, 888, 429], [60, 317, 128, 880, 435]
    weights = [5, 8, 9, 12, 16]
    for i, shape in enumerate(shapes):
        x, cx = 20+236*i, 130+236*i
        s.panel(x, 65, 220, 412)
        s.text(cx, 103, ' + '.join(map(str, shape)), 25, anchor='middle', weight='bold')
        for j, size in enumerate(shape):
            yy = 154+j*45
            points = [(cx+(k-(size-1)/2)*36, yy) for k in range(size)]
            for a, b in zip(points, points[1:]):
                s.line(a, b)
            for k, pt in enumerate(points):
                s.circle(pt, 7 if k == 0 else 5, GREEN if k == 0 else 'white', GREEN if k == 0 else INK)
        expr = ' × '.join(map(str, shape))
        s.text(cx, 345, expr + (f' = {weights[i]}' if len(shape) > 1 else ' выборов'), 20, GREEN, 'middle', 'bold')
        s.text(cx, 391, f'А: {counts_a[i]} лесов', 21, anchor='middle')
        s.text(cx, 432, f'Б: {counts_b[i]} лесов', 21, anchor='middle')
    s.circle((65, 514), 7, GREEN)
    s.text(85, 521, 'Один выбор корней; изолированные вершины не показаны', 21, MUTED)
    s.save('Корневые веса четырёхрёберных лесов.svg')


def reduced_ring(s, cx, cy, start, label):
    p = ring(cx, cy, 95)
    s.polygon(list(p.values()), '#edf5f4')
    seam = {0, 1, start, start+1}
    for i in range(6):
        a, b = p[i], p[(i+1) % 6]
        color = RED if i == 0 else BLUE if i == start else EDGE
        s.line(a, b, color, 5 if i in [0, start] else 3)
        mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
        s.text(mx+(mx-cx)*.23, my+(my-cy)*.23+6,
               'w' if i in [0, start] else '1', 22, color, 'middle')
    for i, pt in p.items():
        s.circle(pt, 17, 'white', INK)
        s.text(pt[0], pt[1]+7, 'd' if i in seam else 'y', 23, anchor='middle')
        # Vertex indices are placed toward the face, away from edge labels.
        s.text(cx+(pt[0]-cx)*.68, cy+(pt[1]-cy)*.68+5, str(i), 16, MUTED, 'middle')
    s.text(cx, cy+163, label, 24, anchor='middle', weight='bold')


def elimination():
    s = SVG(1160, 680, 'Исключение крайних ядер',
            'Четыре внутренние вершины крайнего шестиугольника исключаются. На концах шва остаётся диагональ d и внедиагональный элемент w. Два положения второго шва задают разные сокращённые матрицы.')
    s.text(35, 40, 'Один крайний блок: дополнение Шура', 25, weight='bold')
    s.panel(20, 62, 1120, 211)
    pts = [(65, 205), (130, 129), (215, 108), (300, 108), (385, 129), (450, 205)]
    for a, b in zip(pts, pts[1:]):
        s.line(a, b)
    s.line(pts[0], pts[-1], RED, 5)
    for i, pt in enumerate(pts):
        s.circle(pt, 6, 'white', INK)
        s.text(pt[0], pt[1]-18, 'y − 1' if i in [0, 5] else 'y', 20, anchor='middle')
    s.text(257, 246, 'шов: элемент 1', 20, RED, 'middle')
    s.text(257, 169, 'T₄ · определитель k', 20, MUTED, 'middle')
    s.arrow((499, 172), (622, 172))
    s.text(560, 150, 'исключить', 18, MUTED, 'middle')
    s.line((709, 172), (1007, 172), RED, 5)
    for xx in [709, 1007]:
        s.circle((xx, 172), 8, 'white', INK)
        s.text(xx, 144, 'd', 27, anchor='middle')
    s.text(858, 161, 'w = 1 + 1/k', 23, RED, 'middle')
    s.text(858, 225, 'd = y − 1 − ℓ/k', 23, anchor='middle')
    s.text(35, 315, 'После двух исключений: χ = k² det H', 25, weight='bold')
    s.panel(20, 337, 540, 319)
    s.panel(600, 337, 540, 319)
    reduced_ring(s, 290, 469, 3, 'А · HА')
    reduced_ring(s, 870, 469, 2, 'Б · HБ')
    s.save('Исключение крайних ядер.svg')


if __name__ == '__main__':
    seams()
    forest_weights()
    elimination()
    print('Generated three SVG figures.')
