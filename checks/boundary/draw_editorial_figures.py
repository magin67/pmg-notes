"""Draw the bilingual editorial overview and star/K4 example (stdlib only).

Run from the repository root: python checks/boundary/draw_editorial_figures.py
Use --root for a separate output tree. Existing figures are left unchanged.
"""
from pathlib import Path
from html import escape
import argparse

PREFIX = {
    'ru': 'pmg-library/ru/Преобразования и сочленения графов/Граничные полиномы и сочленение графов/images',
    'en': 'pmg-library/en/Graph Transformations and Gluing/Boundary polynomials and graph gluing/images',
}
NAMES = {
    'overview': ('Какие данные сохраняет граничный паспорт', 'What boundary passports retain'),
    'star': ('Одинаковый отклик звезды и полного графа', 'The same response for a star and a complete graph'),
}
INK, MUTED, BLUE, GREEN, GOLD = '#20354b', '#53677a', '#2168a6', '#17826b', '#d69a20'


class SVG:
    def __init__(self, height, title, description):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{height}" viewBox="0 0 1100 {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
            '<defs><marker id="arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="10" markerHeight="10" orient="auto-start-reverse"><path d="M1 1 L11 6 L1 11 Z" fill="#53677a"/></marker></defs>',
            f'<rect width="1100" height="{height}" fill="white"/>',
            '<g font-family="DejaVu Sans, Arial, sans-serif">']

    def text(self,x,y,value,size=20,color=INK,anchor='start',bold=False):
        value=escape(value)
        for label,base,sub in [('fπ','f','π'),('gπ','g','π'),('δB','δ','B'),('g₁₂|₃₄','g','12|34')]:
            value=value.replace(label,f'{base}<tspan baseline-shift="sub" font-size="75%">{sub}</tspan>')
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{"bold" if bold else "normal"}">{value}</text>')

    def line(self,x1,y1,x2,y2,color=MUTED,width=3,arrow=False):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')

    def box(self,x,y,w,h,color='#eaf2f9'):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{color}" stroke="#ccd8e2"/>')

    def node(self,x,y,label,boundary=True):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="white" stroke="{GOLD if boundary else INK}" stroke-width="4"/>')
        self.text(x,y+6,label,18,anchor='middle',bold=True)

    def save(self,path):
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text('\n'.join(self.parts+['</g></svg>'])+'\n',encoding='utf-8')


def overview(lang):
    en=lang=='en'
    pick=lambda a,b:b if en else a
    title=pick('Что сохраняет граничный паспорт','What a boundary passport retains')
    s=SVG(750,title,pick('Из графа строятся отдельно полный лесной и спектральный паспорта. Из лесного паспорта выделяются рощи, затем электрический отклик и масштаб.','Build the full forest and spectral passports separately from the graph. Extract groves from the forest passport, then electrical response and scale.'))
    s.text(40,46,title,29,bold=True)
    s.text(40,80,pick('Выбор данных зависит от того, что нужно вычислить после сочленения.','The data to retain depend on what the gluing must compute.'),20,MUTED)
    s.box(315,108,470,74,'#f2f5f8')
    s.text(550,139,pick('Граф G с отмеченной границей','Graph G with a marked boundary'),22,anchor='middle',bold=True)
    s.text(550,165,pick('Имена границы и число вершин известны','Boundary labels and vertex count are known'),17,MUTED,anchor='middle')
    s.line(440,184,300,236,arrow=True);s.line(660,184,812,236,arrow=True)
    s.box(40,248,480,106)
    s.text(64,281,pick('Полный лесной паспорт','Full forest passport'),24,BLUE,bold=True)
    s.text(64,312,pick('Все полиномы состояний: fπ(t)','All state polynomials: fπ(t)'),21)
    s.text(64,338,pick('Включая внутренние компоненты леса','Including internal forest components'),18,MUTED)
    s.box(580,248,480,174,'#f1edf8')
    s.text(604,281,pick('Спектральный паспорт','Spectral passport'),24,'#705295',bold=True)
    s.text(604,312,pick('Для пары: A, B, C, D, E','For a pair: A, B, C, D, E'),21)
    s.text(604,343,'AE = BC − D²',23)
    s.text(604,376,pick('Считает характеристический полином','Computes the characteristic polynomial'),18,MUTED)
    s.text(604,404,pick('и сохраняет данные отмеченной пары','and retains data of the marked pair'),18,MUTED)
    s.line(280,358,280,414,arrow=True)
    s.text(305,391,pick('Коэффициент при tⁿ⁻ᵇ⁽π⁾','Coefficient of tⁿ⁻ᵇ⁽π⁾'),16,MUTED)
    s.box(40,426,480,100,'#eaf5ef')
    s.text(64,460,pick('Веса рощ: gπ','Grove weights: gπ'),24,GREEN,bold=True)
    s.text(64,493,pick('Каждая компонента встречает границу','Every component meets the boundary'),18,MUTED)
    s.line(280,530,280,586,arrow=True)
    s.text(305,563,pick('Для связной компоненты','For a connected component'),17,MUTED)
    s.box(40,598,480,100,'#fff7e6')
    s.text(64,634,pick('Электрический отклик Λ и масштаб δB','Electrical response Λ and scale δB'),21,bold=True)
    s.text(64,670,pick('Достаточны для остовного сочленения','Suffice for spanning-tree gluing'),18,MUTED)
    s.text(600,483,pick('Лесной паспорт не определяет','The forest passport does not'),20,bold=True)
    s.text(600,512,pick('спектральный паспорт в общем случае.','determine the spectral passport in general.'),19)
    s.text(600,565,pick('Обратное восстановление данных','Reconstructing data in the reverse'),19,MUTED)
    s.text(600,594,pick('электрической ветви ограничено:','direction on the electrical branch is limited:'),19,MUTED)
    s.text(600,623,pick('см. условия и контрпримеры в заметке 4.','see assumptions and examples in note 4.'),19,MUTED)
    return s


def star(lang):
    en=lang=='en'
    pick=lambda a,b:b if en else a
    s=SVG(720,pick('Один отклик не восстанавливает каждую рощу','One response does not recover every grove'),pick('Четырёхлучевая единичная звезда и полный граф на границе с проводимостями одна четверть имеют один электрический отклик, но разные веса рощи 12|34.','A four-leaf unit star and the complete boundary graph with conductances one quarter have the same response but different weights of the grove 12|34.'))
    s.text(40,45,pick('Один отклик не восстанавливает каждую рощу','One response does not recover every grove'),28,bold=True)
    s.text(40,80,pick('Золотые окружности: граница B = {1, 2, 3, 4}. Пересечение линий не создаёт вершину.','Gold circles: boundary B = {1, 2, 3, 4}. Crossing lines do not create a vertex.'),18,MUTED)
    for x in (40,580): s.box(x,105,480,405,'#f7f9fb')
    s.text(280,140,pick('Звезда: каждое ребро имеет вес 1','Star: every edge has weight 1'),20,anchor='middle',bold=True)
    s.text(820,140,pick('Эффективный K₄: каждое ребро 1/4','Effective K₄: every edge has weight 1/4'),20,anchor='middle',bold=True)
    left=[(155,200),(405,200),(405,410),(155,410)]
    right=[(695,200),(945,200),(945,410),(695,410)]
    for i,(x,y) in enumerate(left): s.line(x,y,280,305,BLUE if i<2 else GREEN,5)
    s.node(280,305,'h',False)
    for i in range(4):
        for j in range(i+1,4):
            s.line(*right[i],*right[j],BLUE if (i,j)==(0,1) else GREEN if (i,j)==(2,3) else '#becbd6',6 if (i,j) in ((0,1),(2,3)) else 2)
    for coords in (left,right):
        for i,(x,y) in enumerate(coords): s.node(x,y,str(i+1))
    s.text(280,465,pick('Две пары требуют общего центра h','Both pairs would need the center h'),19,anchor='middle')
    s.text(820,465,pick('Выбранные рёбра 12 и 34 не связаны','Selected edges 12 and 34 are disjoint'),19,anchor='middle')
    s.text(280,495,'g₁₂|₃₄ = 0,  δB = 4',23,anchor='middle',bold=True)
    s.text(820,495,'g₁₂|₃₄ = (1/4)² = 1/16,  δB = 1',23,anchor='middle',bold=True)
    s.box(40,536,1020,142,'#fff7e6')
    s.text(550,571,pick('Одинаковый электрический отклик: Λ = I₄ − (1/4) 11ᵀ','The same electrical response: Λ = I₄ − (1/4) 11ᵀ'),24,anchor='middle',bold=True)
    s.text(280,612,pick('Нормированный вес: g₁₂|₃₄ / δB = 0','Normalized weight: g₁₂|₃₄ / δB = 0'),20,anchor='middle')
    s.text(820,612,pick('Нормированный вес: g₁₂|₃₄ / δB = 1/16','Normalized weight: g₁₂|₃₄ / δB = 1/16'),20,anchor='middle')
    s.text(550,650,pick('K₄ планарен, но не допускает все четыре вершины на одной внешней грани.','K₄ is planar, but cannot place all four vertices on a single outer face.'),20,anchor='middle')
    return s


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args()
    for lang in ('ru','en'):
        for key,draw in (('overview',overview),('star',star)):
            path=args.root/PREFIX[lang]/(NAMES[key][lang=='en']+'.svg')
            draw(lang).save(path)
            print(path)


if __name__=='__main__':
    main()
