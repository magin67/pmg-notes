"""Constructive SVG illustrations for ordinary and twisted closures."""
from math import cos, sin, pi, sqrt
from pathlib import Path
import json

from draw_admissible_chains import SVG, INK, MUTED, EDGE, RED, BLUE, PURPLE, FILLS
from verify_admissible_chains import edge, cycle

DATA = {r['name']: r for r in json.loads(Path(__file__).with_name('closure-results.json').read_text(encoding='utf-8'))['graphs']}
SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')


def label(letter, i):
    return letter+str(i).translate(SUB)


def draw_graph(s, positions, edges, seams=None):
    seams = seams or {}
    for a, b in edges:
        color = seams.get(edge(a,b), EDGE)
        s.line(positions[a], positions[b], color, 5 if color != EDGE else 2.6)
    for p in positions.values():
        s.circle(p, 4.5, 'white', INK, 1.6)


def two_closures():
    s=SVG(1260,570,'Два замыкания квадратной полосы','Одна полоса из четырёх квадратов; прямое и обратное соответствия крайних рёбер. Общие рёбра учитываются один раз.')
    s.text(630,35,'Последний шов: совпадение или обмен концов',28,anchor='middle',weight='bold')
    for panel,twist in enumerate((False,True)):
        x0=20+panel*630
        s.panel(x0,65,610,440)
        s.text(x0+305,102,'Скрученное замыкание' if twist else 'Обычное замыкание',24,anchor='middle',weight='bold')
        ps={}
        for i in range(5):
            ps[2*i]=(x0+75+115*i,180)
            ps[2*i+1]=(x0+75+115*i,335)
        for i in range(4):
            s.polygon([ps[2*i],ps[2*i+2],ps[2*i+3],ps[2*i+1]],FILLS[i%3])
            s.text(x0+132+115*i,265,label('K',i),22,anchor='middle',weight='bold')
        es={(2*i,2*i+1) for i in range(5)}|{(2*i+r,2*i+2+r) for i in range(4) for r in (0,1)}
        draw_graph(s,ps,es,{(0,1):RED,(8,9):RED})
        for i in range(5):
            s.text(ps[2*i][0],158,label('a',i),19,anchor='middle')
            s.text(ps[2*i+1][0],363,label('b',i),19,anchor='middle')
        s.arrow((x0+53,310),(x0+53,205),RED)
        s.arrow((x0+557,205 if twist else 310),(x0+557,310 if twist else 205),RED)
        s.text(x0+305,407,'a₄ ↔ b₀,   b₄ ↔ a₀' if twist else 'a₄ ↔ a₀,   b₄ ↔ b₀',24,RED,'middle','bold')
        rec=DATA[f'strip_N4_p1_q1_twist{int(twist)}']
        s.text(x0+305,456,f"После замыкания: τ = {rec['tau']},  ρ = {rec['rho']}",21,anchor='middle')
    s.text(630,545,'Два крайних красных ребра становятся одним единичным ребром',22,anchor='middle')
    s.save('Два замыкания квадратной полосы.svg')


def reduction():
    s=SVG(1200,530,'Чётный цикл и редукция продольных путей','Шестиугольное ядро с противоположными рёберными швами: два пути длины два заменяются проводимостями одна вторая.')
    s.text(600,36,'Шестиугольное ядро: пути длины 2 и их проводимости',27,anchor='middle',weight='bold')
    s.panel(20,65,510,390);s.panel(670,65,510,390)
    s.text(275,105,'Все шесть рёбер единичные',23,anchor='middle',weight='bold')
    s.text(925,105,'После исключения двух вершин',23,anchor='middle',weight='bold')
    ps={0:(115,220),1:(275,160),2:(435,220),3:(435,340),4:(275,400),5:(115,340)}
    s.polygon(list(ps.values()),FILLS[1]);draw_graph(s,ps,cycle(list(range(6))),{(0,5):RED,(2,3):BLUE})
    for v,txt,dx,dy in [(0,'aᵢ',-28,4),(5,'bᵢ',-28,4),(2,'aᵢ₊₁',36,4),(3,'bᵢ₊₁',36,4),(1,'xᵢ',0,-15),(4,'yᵢ',0,27)]:
        s.text(ps[v][0]+dx,ps[v][1]+dy,txt,21,anchor='middle')
    s.arrow((565,280),(635,280),PURPLE,4)
    ps2={0:(775,220),1:(1075,220),2:(1075,340),3:(775,340)}
    draw_graph(s,ps2,cycle([0,1,2,3]),{(0,3):RED,(1,2):BLUE})
    s.text(925,197,'c = 1/2',25,PURPLE,'middle','bold');s.text(925,379,'c = 1/2',25,PURPLE,'middle','bold')
    s.text(748,285,'1',22,RED,'middle');s.text(1102,285,'1',22,BLUE,'middle')
    s.text(600,496,'Восстановление двух путей даёт множитель 4 для остовного числа',22,anchor='middle')
    s.save('Чётный цикл и редукция продольных путей.svg')


def rings():
    s=SVG(1260,690,'Шестиугольное кольцо и замкнутая полоса','Два обычных замыкания шести циклов C6. Пути между швами имеют длины 1 и 3 либо 2 и 2. Последний шов красный.')
    s.text(630,35,'Одинаковые ядра, разное положение швов',28,anchor='middle',weight='bold')
    left=DATA['strip_N6_p1_q3_twist0'];right=DATA['strip_N6_p2_q2_twist0']
    for panel in range(2):s.panel(20+630*panel,65,610,565)
    s.text(325,105,'Кольцо вокруг пустой ячейки',24,anchor='middle',weight='bold')
    s.text(955,105,'Цилиндрическая полоса',24,anchor='middle',weight='bold')
    ps={i:(325+65*(x+y/2),315-65*sqrt(3)*y/2) for i,(x,y) in enumerate(left['lattice_coordinates'])}
    for i,core in enumerate(left['lattice_core_cycles']):
        s.polygon([ps[v] for v in core],FILLS[i%3])
        cx=sum(ps[v][0] for v in core)/6;cy=sum(ps[v][1] for v in core)/6
        s.text(cx,cy+6,label('K',i),18,anchor='middle',weight='bold')
    iso=left['strip_to_lattice']
    seams={edge(iso[2*i],iso[2*i+1]):RED if i==0 else BLUE for i in range(6)}
    draw_graph(s,ps,left['lattice_edges'],seams)
    s.text(325,319,'C₆',24,MUTED,'middle','bold')
    ps2={}
    for i,pair in enumerate(right['rail_paths']):
        for row,path in enumerate(pair):
            for k,v in enumerate(path):
                angle=-pi/2+(i+k/2)*pi/3
                rad=95 if row==0 else 190
                ps2[v]=(955+rad*cos(angle),315+rad*sin(angle))
    for i,core in enumerate(right['core_cycles']):
        s.polygon([ps2[v] for v in core],FILLS[i%3])
        angle=-pi/2+(i+.5)*pi/3
        s.text(955+143*cos(angle),321+143*sin(angle),label('K',i),18,anchor='middle',weight='bold')
    draw_graph(s,ps2,right['edges'],{(2*i,2*i+1):RED if i==0 else BLUE for i in range(6)})
    s.text(955,319,'C₁₂',24,MUTED,'middle','bold')
    for x,rec,lengths in [(325,left,'1 и 3'),(955,right,'2 и 2')]:
        s.text(x,532,'Длины путей: '+lengths,22,anchor='middle')
        s.text(x,572,'τ = '+str(rec['tau']),25,anchor='middle',weight='bold')
        s.text(x,609,'ρ = '+rec['rho'],21,PURPLE,'middle')
    s.text(630,669,'В обоих графах: 24 вершины, 30 рёбер; красным отмечен последний шов',22,anchor='middle')
    s.save('Шестиугольное кольцо и замкнутая полоса.svg')


def prism_shift():
    s=SVG(1260,590,'Сдвиг последнего основания призм','Соответствия двух квадратных границ при сдвигах ноль и один. Стрелки показывают отождествление, а не новые рёбра.')
    s.text(630,35,'Последнее основание: j переходит в j + r по модулю 4',27,anchor='middle',weight='bold')
    for panel,r in enumerate((0,1)):
        x0=20+630*panel;s.panel(x0,65,610,450)
        s.text(x0+305,102,'Нулевой сдвиг r = 0' if r==0 else 'Сдвиг r = 1',25,anchor='middle',weight='bold')
        s.text(x0+130,143,'Конец цепи',20,anchor='middle');s.text(x0+480,143,'Начало цепи',20,anchor='middle')
        for x,side in [(x0+130,-1),(x0+480,1)]:
            for j in range(3):s.line((x,185+75*j),(x,185+75*(j+1)),EDGE,3)
            s.parts.append(f'<path d="M{x},185 C{x+65*side},160 {x+65*side},435 {x},410" fill="none" stroke="{EDGE}" stroke-width="3"/>')
        for j in range(4):
            dest=(j+r)%4
            s.arrow((x0+145,185+75*j),(x0+465,185+75*dest),PURPLE,2.5)
        for x in [x0+130,x0+480]:
            for j in range(4):
                s.circle((x,185+75*j),15,'white',INK,1.7)
                s.text(x,192+75*j,str(j),19,anchor='middle')
        s.text(x0+305,478,'0→0, 1→1, 2→2, 3→3' if r==0 else '0→1, 1→2, 2→3, 3→0',23,PURPLE,'middle','bold')
    s.text(630,555,'Стрелки — соответствия; две копии каждого ребра основания сливаются в одну',21,anchor='middle')
    s.save('Сдвиг последнего основания призм.svg')


if __name__=='__main__':
    two_closures();reduction();rings();prism_shift()
    print('Created four closure diagrams.')
