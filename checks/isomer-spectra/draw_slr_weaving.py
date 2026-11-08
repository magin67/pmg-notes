"""Native SVG illustrations; spatial coordinates are for drawings only."""
from pathlib import Path
from math import cos, sin, pi, atan2
import sys
import json
import numpy as np
import networkx as nx

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'checks/core-chains'))
from draw_admissible_chains import SVG as BaseSVG, INK, MUTED, BLUE, PURPLE, RED
import verify_slr_code as slr

OUT = ROOT/'pmg-library/ru/Преобразования и сочленения графов/Спектры изомеров/images'
GREEN = '#16816c'
COLORS = {'S': BLUE, 'L': GREEN, 'R': PURPLE}
DATA = json.loads(Path(__file__).with_name('slr-weaving-results.json').read_text(encoding='utf-8'))
HEX = np.array([(cos(pi/3-i*pi/3), sin(pi/3-i*pi/3), 0.) for i in range(6)])


class SVG(BaseSVG):
    def save(self, name):
        (OUT/name).write_text('\n'.join(self.parts+['</g></svg>'])+'\n', encoding='utf-8')


def fit(points, box):
    x, y, w, h = box
    lo = np.min(list(points.values()), axis=0)
    hi = np.max(list(points.values()), axis=0)
    scale = min(w/max(hi[0]-lo[0], .01), h/max(hi[1]-lo[1], .01))
    center = (hi+lo)/2
    return {i: (x+w/2+(p[0]-center[0])*scale, y+h/2-(p[1]-center[1])*scale)
            for i, p in points.items()}


def planar(u):
    graph, cores, boundary, edges = slr.graph(u)
    positions = {i: HEX[i, :2] for i in range(6)}
    src = HEX[1, :2]-HEX[0, :2]
    for core in cores[1:]:
        target = positions[core[1]]-positions[core[0]]
        angle = atan2(target[1], target[0])-atan2(src[1], src[0])
        R = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
        shift = positions[core[0]]-R@HEX[0, :2]
        positions.update({v: R@HEX[i, :2]+shift for i, v in enumerate(core)})
    return graph, cores, boundary, positions


def draw_graph(s, graph, cores, positions, box, label=True, depths=None):
    p = fit(positions, box)
    seams = {tuple(sorted(e)) for core1, core2 in zip(cores, cores[1:])
             for e in [tuple(set(core1)&set(core2))]}
    edges = list(graph.edges)
    if depths is not None:
        edges.sort(key=lambda e: (depths[e[0]]+depths[e[1]])/2)
    for a, b in edges:
        seam = tuple(sorted((a,b))) in seams
        s.line(p[a], p[b], 'white', 8)
        s.line(p[a], p[b], BLUE if seam else MUTED, 4 if seam else 2.5)
    for v in graph:
        s.circle(p[v], 3.5, INK)
    if label:
        for i, core in enumerate(cores):
            if label is not True and i+1 not in label:
                continue
            x = sum(p[v][0] for v in core)/6
            y = sum(p[v][1] for v in core)/6
            s.circle((x,y), 12, 'white')
            s.text(x,y+6,str(i+1),16,INK,anchor='middle',weight='bold')
    return p


def runners():
    s = SVG(1160,480,'Три SLR-бегунка','Один путь из пяти рёбер, вилка (1,0), три различных упорядоченных выхода. Входное ребро пунктиром уже принадлежит старому графу.')
    for panel,c in enumerate('LSR'):
        x=20+385*panel
        s.panel(x,20,365,350)
        s.text(x+22,58,{'L':'L: розетка (2, 3)','S':'S: розетка (3, 4)','R':'R: розетка (4, 5)'}[c],23,COLORS[c],weight='bold')
        p = fit({i: HEX[i,:2] for i in range(6)},(x+82,103,205,175))
        for a,b in zip([1,2,3,4,5],[2,3,4,5,0]):s.line(p[a],p[b],BLUE,4)
        s.line(p[0],p[1],MUTED,3,'7 6')
        j=slr.EXIT[c]
        s.line(p[j],p[j+1],COLORS[c],7)
        aa=np.array(p[j]);bb=np.array(p[j+1])
        s.arrow(aa*.72+bb*.28,aa*.28+bb*.72,'white',2)
        center=np.mean(list(p.values()),axis=0)
        for i in range(6):
            s.circle(p[i],8,'white',BLUE if i in [0,1] else INK,2)
            delta=np.array(p[i])-center
            delta=delta/np.linalg.norm(delta)*24
            s.text(p[i][0]+delta[0],p[i][1]+delta[1]+7,str(i),21,anchor='middle')
        s.text(x+182,333,'Вилка (1, 0):  1 → a,  0 → b',19,anchor='middle')
    s.text(40,414,'Пять рёбер добавляются. Старое ребро ab замыкает новый C6.',23,weight='bold')
    s.text(40,451,'Четыре новые вершины на каждом шаге; порядок контактов входит в правило.',21,MUTED)
    s.save('Три SLR-бегунка.svg')


def spatial_L(N):
    # A spatial P6 runner repeats under a screw motion. Its six-vertex cycles
    # need not be regular polygons: only graph incidence enters the theorem.
    def helix(u, radius):
        return np.array([1.3*u, radius*cos(1.1*u), radius*sin(1.1*u)])
    positions={0:helix(0,.85),1:helix(0,1.55)}
    graph=nx.Graph([(0,1)]);cores=[];boundary=(0,1)
    for step in range(1,N+1):
        a,b=boundary;n=len(graph)
        core=[b,a,n,n+1,n+2,n+3]
        positions.update({n:helix(step,.85),n+1:helix(step,1.55),
                          n+2:helix(step-1/3,1.55),n+3:helix(step-2/3,1.55)})
        graph.add_edges_from(zip(core,core[1:]+core[:1]));cores.append(core)
        boundary=(n,n+1)
    assert nx.is_isomorphic(graph,slr.graph('L'*(N-2))[0])
    projection={i:np.array([p[0]+.65*p[2], .8*p[1]+.6*p[2]]) for i,p in positions.items()}
    depths={i:float(-.52*p[0]-.6*p[1]+.8*p[2]) for i,p in positions.items()}
    return graph,cores,projection,depths


def families():
    s=SVG(1160,770,'Прямая цепочка, зигзаг и спираль','Верхние схемы показывают прямой и чередующийся код. Нижняя показывает пространственное расположение десяти циклов с постоянной буквой L; пересечения проекции не являются вершинами.')
    for x,u,title in [(20,'SS','Прямое продолжение: SSS'),(590,'LRLR','Чередование: SLRLR')]:
        s.panel(x,20,550,290);s.text(x+22,60,title,23,weight='bold')
        g,cores,_,p=planar(u)
        draw_graph(s,g,cores,p,(x+35,92,480,170))
    s.panel(20,335,1120,335)
    s.text(42,375,'Постоянный L: пространственная цепочка из 10 ядер',25,GREEN,weight='bold')
    g,cores,p,depths=spatial_L(10)
    draw_graph(s,g,cores,p,(62,410,1035,205),label={1,4,7,10},depths=depths)
    s.text(42,647,'В каждом ядре одно и то же положение швов; общие рёбра выделены синим.',21,MUTED)
    s.text(40,710,'Плоскость не фиксирована. Координаты нужны рисунку, а не спектральному переносу.',22,weight='bold')
    s.text(40,748,'Поворот SLR задаёт локальное соединение; пространственная форма выбирается отдельно.',20,MUTED)
    s.save('Прямая цепочка зигзаг и спираль.svg')


def matching():
    s=SVG(1160,540,'Соответствие контактов и SLR-поворот','Фиксированный боковой выход при разных соответствиях вилки и розетки даёт SLL и SLR. Остовное число одинаково, корневые определители различны.')
    for x,u,title,sub,col in [(20,'LL','1 → a,  0 → b','Постоянный поворот: SLL',GREEN),
                              (590,'LR','0 → a,  1 → b','Чередование, с точностью до отражения: SLR',PURPLE)]:
        s.panel(x,20,550,420)
        s.text(x+22,65,title,28,col,weight='bold')
        s.text(x+22,105,sub,19,weight='bold')
        g,cores,_,p=planar(u)
        draw_graph(s,g,cores,p,(x+75,140,400,210))
        val=DATA['contact_order_counterexample_N4']['S'+u+'_P1']
        s.text(x+275,400,'P(1) = '+str(val),25,col,anchor='middle',weight='bold')
    s.text(40,482,'Одинаковый путь и боковой выход; разные правила отождествления контактов.',22,weight='bold')
    s.text(40,519,'У обоих графов 4 ядра, 18 вершин, 21 ребро и τ = 1189.',21,MUTED)
    s.save('Соответствие контактов и SLR-поворот.svg')


def blocks():
    s=SVG(1160,550,'Периодический SLR-бегунок','Две последовательно присоединённые копии P6 объединяются в один бегунок с двумя входами и двумя выходами. Перенос за период LR равен U_R U_L.')
    s.panel(20,20,490,340);s.text(42,60,'Два пути как одна деталь',24,weight='bold')
    # Two steps with outputs L,R; first completed cycle has output (2,3).
    positions={i:HEX[i,:2] for i in range(6)}
    core0=list(range(6));core1=[3,2,6,7,8,9]
    src=HEX[1,:2]-HEX[0,:2];target=positions[2]-positions[3]
    angle=atan2(target[1],target[0])-atan2(src[1],src[0])
    R=np.array([[cos(angle),-sin(angle)],[sin(angle),cos(angle)]])
    shift=positions[3]-R@HEX[0,:2]
    positions.update({v:R@HEX[i,:2]+shift for i,v in enumerate(core1)})
    g=nx.Graph();g.add_edges_from(zip(core0,core0[1:]+core0[:1]));g.add_edges_from(zip(core1,core1[1:]+core1[:1]))
    g.remove_edge(0,1)
    p=draw_graph(s,g,[core0,core1],positions,(105,108,300,170),label=False)
    s.line(p[0],p[1],MUTED,3,'7 6')
    for pair,col,label in [((1,0),BLUE,'P'),((8,9),GREEN,'Q')]:
        for v in pair:s.circle(p[v],8,'white',col,3)
        mid=(np.array(p[pair[0]])+np.array(p[pair[1]]))/2
        s.text(mid[0]+(28 if label=='P' else -45),mid[1]+5,label,23,col,weight='bold')
    s.text(42,325,'10 вершин, 10 рёбер; пунктир не входит в K.',19,MUTED)
    s.panel(535,20,605,340);s.text(560,60,'Порядок матриц за период LR',24,weight='bold')
    for x,label in [(600,'s0'),(815,'s1'),(1060,'s2')]:s.text(x,175,label,29,anchor='middle',weight='bold')
    s.arrow((635,165),(780,165),GREEN);s.text(707,137,'U_L',24,GREEN,anchor='middle')
    s.arrow((850,165),(1020,165),PURPLE);s.text(935,137,'U_R',24,PURPLE,anchor='middle')
    s.text(838,262,'V_LR = U_R U_L',31,BLUE,anchor='middle',weight='bold')
    s.text(838,320,'Первым действует правый множитель.',20,MUTED,anchor='middle')
    for i in range(4):
        x=90+i*265;s.panel(x,395,185,65);s.text(x+92,438,'блок LR',23,BLUE,anchor='middle',weight='bold')
        if i<3:s.arrow((x+195,427),(x+250,427),MUTED)
    s.text(40,512,'Один составной бегунок добавляет два ядра. После m блоков: s(2m) = (U_R U_L)^m s0.',22,weight='bold')
    s.save('Периодический SLR-бегунок.svg')


if __name__=='__main__':
    runners();families();matching();blocks()
    print('Saved four SVG figures; the spatial graph has the asserted SLR incidence.')
