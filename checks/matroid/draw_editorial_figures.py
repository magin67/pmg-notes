"""Two bilingual diagrams for the matroid series; run from any directory.

Uses only the Python standard library. All edges in these examples have unit
conductance. The small enumeration below checks the numbers shown in the SVGs.
"""
from pathlib import Path
from html import escape
from itertools import combinations
import os

ROOT = Path(__file__).resolve().parents[2]
if os.name == 'nt' and not str(ROOT).startswith('\\\\?\\'):
    ROOT = Path('\\\\?\\' + str(ROOT))
DIRS = {
    'ru': ROOT / 'pmg-library/ru/Инварианты, разложения и спектры/Матроидные параметры и лесные характеристики графов/images',
    'en': ROOT / 'pmg-library/en/Invariants, Decompositions, and Spectra/Matroid parameters and forest characteristics of graphs/images',
}
BLUE, GREEN, PURPLE, GRAY = '#2563a8', '#287a62', '#8a43a3', '#526078'

def forest_counts(n, edges):
    counts = [0] * n
    for k in range(min(n - 1, len(edges)) + 1):
        for chosen in combinations(range(len(edges)), k):
            parent = list(range(n))
            def find(a):
                while parent[a] != a:
                    a = parent[a]
                return a
            for i in chosen:
                a, b = map(find, edges[i])
                if a == b:
                    break
                parent[a] = b
            else:
                counts[k] += 1
    return counts

def verify_examples():
    triangle = forest_counts(3, [(0, 1), (0, 2), (1, 2)])
    deleted = forest_counts(3, [(0, 2), (1, 2)])
    contracted = forest_counts(2, [(0, 1), (0, 1)])
    assert triangle == [1, 3, 3] and deleted == [1, 2, 1] and contracted == [1, 2]
    assert triangle == [deleted[k] + (contracted[k-1] if k else 0) for k in range(3)]
    h1 = [(0, 1)] * 4 + [(1, 2), (2, 0)]
    h2 = [(0, 1)] * 3 + [(1, 2)] * 3
    assert forest_counts(3, h1) == forest_counts(3, h2) == [1, 6, 9]
    assert sorted([4, 1, 1]) != sorted([3, 3])

def text(x, y, value, size=21, weight=400, fill='#1d2939', anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>'

def edge(a, b, color=GRAY, bend=0):
    x, y = a; u, v = b
    dx, dy = u-x, v-y
    length = (dx*dx+dy*dy)**0.5
    mx, my = (x+u)/2-bend*dy/length, (y+v)/2+bend*dx/length
    return f'<path d="M{x},{y} Q{mx:.2f},{my:.2f} {u},{v}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round"/>'

def vertex(x, y, name, ox=0, oy=32):
    return f'<circle cx="{x}" cy="{y}" r="8" fill="white" stroke="#1d2939" stroke-width="2.5"/>' + text(x+ox, y+oy, name, 23, 600)

def panel(x, width, height=350):
    return f'<rect x="{x}" y="77" width="{width}" height="{height}" rx="15" fill="#f5f7fb" stroke="#d9e1ec"/>'

def svg(title, desc, body, height):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="{height}" viewBox="0 0 1080 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect width="1080" height="{height}" fill="white"/>
<g font-family="Arial, DejaVu Sans, sans-serif">{text(540,40,title,27,600)}{body}</g>
</svg>
'''

def deletion(lang):
    ru = lang == 'ru'
    title = 'Удаление и стягивание ребра треугольника' if ru else 'Deleting and contracting a triangle edge'
    labels = ['Исходный граф G', 'Удаление G ∖ ℓ', 'Стягивание G / ℓ'] if ru else ['Original graph G', 'Deletion G ∖ ℓ', 'Contraction G / ℓ']
    body = ''
    for x, label in zip([25, 375, 725], labels):
        body += panel(x, 330, 347) + text(x+165,112,label,23,600)
    a,b,c=(90,285),(290,285),(190,163)
    body += edge(a,b,PURPLE)+edge(a,c,BLUE)+edge(b,c,GREEN)
    body += vertex(*a,'a',oy=32)+vertex(*b,'b',oy=32)+vertex(*c,'c',oy=-18)
    body += text(190,276,'ℓ = ab',21,600,PURPLE)
    body += text(190,363,'1 + 3t + 3t²',26,600)+text(190,398,'7 лесов' if ru else '7 forests',20)
    a,b,c=(440,285),(640,285),(540,163)
    body += edge(a,c,BLUE)+edge(b,c,GREEN)
    body += vertex(*a,'a',oy=32)+vertex(*b,'b',oy=32)+vertex(*c,'c',oy=-18)
    body += text(540,363,'1 + 2t + t²',26,600)+text(540,398,'4 леса без ℓ' if ru else '4 forests without ℓ',20)
    a,c=(800,285),(980,163)
    body += edge(a,c,BLUE,-44)+edge(a,c,GREEN,44)
    body += vertex(*a,'a = b',oy=32)+vertex(*c,'c',oy=-18)
    body += text(890,363,'1 + 2t',26,600)+text(890,398,'3 леса после стягивания' if ru else '3 forests after contraction',20)
    body += '<text x="540" y="468" text-anchor="middle" font-size="27" font-weight="600" fill="#1d2939">F<tspan baseline-shift="sub" font-size="18">G</tspan><tspan baseline-shift="baseline">(t) = F</tspan><tspan baseline-shift="sub" font-size="18">G ∖ ℓ</tspan><tspan baseline-shift="baseline">(t) + t F</tspan><tspan baseline-shift="sub" font-size="18">G / ℓ</tspan><tspan baseline-shift="baseline">(t)</tspan></text>'
    body += text(540,510,'Выбрать оба параллельных ребра нельзя: получится цикл.' if ru else 'Selecting both parallel edges creates a cycle.',22)
    body += text(540,544,'Все проводимости равны 1; множитель t возвращает выбранное ребро ℓ.' if ru else 'All conductances are 1; the factor t restores the selected edge ℓ.',20)
    return svg(title, 'Леса разбиты по наличию выделенного ребра; после его стягивания два ребра остаются отдельными.' if ru else 'Forests are partitioned by presence of the selected edge; contraction retains two distinct parallel edges.', body, 570)

def same_polynomial(lang):
    ru = lang == 'ru'
    title = 'Одинаковый лесной полином, разные матроиды' if ru else 'Equal forest polynomials, different matroids'
    body = panel(25,500,355)+panel(555,500,355)
    body += text(275,115,'H₁',26,600)+text(805,115,'H₂',26,600)
    a,b,c=(135,212),(415,212),(275,325)
    for bend in [-100,-34,34,100]: body += edge(a,b,BLUE,bend)
    body += edge(a,c,GREEN)+edge(b,c,GREEN)
    body += vertex(*a,'a',ox=-23,oy=6)+vertex(*b,'b',ox=23,oy=6)+vertex(*c,'c',oy=30)
    body += text(275,151,'4',22,600,BLUE)+text(181,283,'1',22,600,GREEN)+text(369,283,'1',22,600,GREEN)
    a,b,c=(655,300),(805,164),(955,300)
    for bend in [-55,0,55]:
        body += edge(a,b,BLUE,bend)+edge(b,c,PURPLE,bend)
    body += vertex(*a,'a',oy=32)+vertex(*b,'b',oy=-19)+vertex(*c,'c',oy=32)
    body += text(694,220,'3',22,600,BLUE)+text(916,220,'3',22,600,PURPLE)
    body += text(275,404,'Параллельные классы: 4, 1, 1' if ru else 'Parallel classes: 4, 1, 1',22,600)
    body += text(805,404,'Параллельные классы: 3, 3' if ru else 'Parallel classes: 3, 3',22,600)
    body += text(540,474,'F(t) = 1 + 6t + 9t²;   Φ(u) = 1 + 2u/3 + u²/9',27,600)
    body += text(540,517,'Все рёбра единичные. Числа показывают размеры классов, а не веса рёбер.' if ru else 'All edges have unit weight. Numbers show class sizes, not edge weights.',20)
    body += text(540,555,'Совпадают суммы по мощностям; не совпадает структура зависимостей.' if ru else 'The totals by size agree; the dependence structures differ.',22)
    return svg(title, 'У первого графа четыре параллельных ребра ab и по одному ac и bc; у второго по три ab и bc. Оба имеют шесть рёбер и девять остовных деревьев.' if ru else 'The first graph has four parallel ab edges and one each of ac and bc; the second has three each of ab and bc. Both have six edges and nine spanning trees.', body, 585)

def main():
    verify_examples()
    for lang, directory in DIRS.items():
        directory.mkdir(parents=True, exist_ok=True)
        files = [('Удаление и стягивание ребра треугольника.svg' if lang=='ru' else 'Deleting and Contracting a Triangle Edge.svg', deletion(lang)),
                 ('Одинаковый лесной полином и разные матроиды.svg' if lang=='ru' else 'Equal Forest Polynomials and Different Matroids.svg', same_polynomial(lang))]
        for name, content in files:
            (directory/name).write_text(content, encoding='utf-8', newline='\n')
    print('OK: triangle deletion/contraction, both parallel-class examples; four SVGs written.')

if __name__ == '__main__':
    main()
