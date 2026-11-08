"""Draw five bilingual editorial diagrams; extend the shared translation catalogue.

Run this script, then translate_figures.py. Only the Python standard library is
needed for drawing; the existing translator handles any optional font fitting.
"""
from pathlib import Path
from math import cos,sin,pi,sqrt
import json
from draw_admissible_chains import SVG,INK,MUTED,BLUE,RED,PURPLE,FILLS

GREEN='#138570'
HERE=Path(__file__).resolve().parent
CATALOG=HERE/'figure-translations-en.json'
data=json.loads(CATALOG.read_text(encoding='utf-8'))

class Figure(SVG):
    def __init__(self,w,h,title,description):
        self.words={title[0]:title[1],description[0]:description[1]}
        super().__init__(w,h,title[0],description[0])
    def text(self,x,y,t,*args,**kwargs):
        if isinstance(t,tuple):self.words[t[0]]=t[1];t=t[0]
        super().text(x,y,t,*args,**kwargs)
    def save_pair(self,ru,en):
        self.save(ru+'.svg')
        data[ru+'.svg']={'file':en+'.svg','text':self.words,'fit_text':False}

def routes():
    s=Figure(1180,510,('Два маршрута по цепям из ядер','Two routes through chains of cores'),('Основная линия: ядра, инвариантность, остовная рекурсия, ограничения, замыкание. Дополнительная: плетение и полный топоном.','Main track: cores, invariance, spanning-tree recurrence, limits, closure. Further track: weaving and the full toponome.'))
    s.text(30,43,('Основной маршрут: конструкция и её параметры','Main route: the construction and its parameters'),27,weight='bold')
    labels=[(('Ядра','Cores'),('и швы','and seams')),(('Матроидная','Matroid'),('инвариантность','invariance')),(('Остовной','Spanning-tree'),('определитель','determinant')),(('Границы','Limits of'),('инвариантности','invariance')),(('Замыкание','Closing'),('цепи','a chain'))]
    for k,(a,b) in enumerate(labels):
        x=30+230*k;s.panel(x,75,195,118)
        s.text(x+97,118,a,21,anchor='middle',weight='bold');s.text(x+97,153,b,20,anchor='middle')
        if k<4:s.arrow((x+201,134),(x+224,134),BLUE,3)
    s.text(30,236,('От условий допустимости к результату и его ограничениям','From admissibility to the result and its limitations'),21,MUTED)
    s.text(30,300,('Продолжение: вычисление повторяемым шагом','Further route: computation by repeating a step'),27,weight='bold')
    for x,a,b in [(30,('Плетение графов','Graph weaving'),('Бегунок и два остовных состояния','A runner and two spanning states')),(650,('Экспонента и топономы','The exponential and toponomes'),('Размеры компонент и их оценки','Component sizes and their evaluations'))]:
        s.panel(x,330,495,110);s.text(x+247,370,a,23,anchor='middle',weight='bold');s.text(x+247,411,b,20,anchor='middle')
    s.arrow((545,384),(630,384),PURPLE,4)
    s.text(30,484,('Плетение можно читать первым; полный топоном требует лесных состояний.','Weaving can be read first; the full toponome requires forest states.'),20,MUTED)
    s.save_pair('Два маршрута по цепям из ядер','Two routes through chains of cores')

def forgetting():
    s=Figure(1120,450,('Один лес при смене границы','One forest as the boundary changes'),('В лесу квадрата выбрано только ребро ab. После снятия отметок a и b эта компонента остаётся внутренней; выходные вершины c и d разделены.','Only edge ab is selected in a square forest. Removing the marks at a and b leaves that component internal; output vertices c and d remain separated.'))
    for x,active,title,state in [(25,'abcd',('До снятия отметок','Before removing marks'),'D = {a, b, c, d}'),(625,'cd',('После снятия отметок','After removing marks'),'C = {c, d}')]:
        s.panel(x,20,465,360);s.text(x+24,59,title,24,weight='bold')
        ps={'a':(x+115,130),'b':(x+115,260),'c':(x+340,130),'d':(x+340,260)}
        for a,b in [('a','c'),('b','d'),('c','d')]:s.line(ps[a],ps[b],'#cad7e5',2,'6 7')
        s.line(ps['a'],ps['b'],GREEN,6)
        for name,p in ps.items():
            if name in active:s.circle(p,11,'white',BLUE,3)
            s.circle(p,4,GREEN if name in 'ab' else INK)
            s.text(p[0]+(-24 if name in 'ab' else 20),p[1]+7,name,22)
        s.text(x+232,310,state,21,anchor='middle')
        s.text(x+232,349,'{a, b} | {c} | {d}' if x==25 else '{c} | {d}',23,anchor='middle',weight='bold')
    s.arrow((510,198),(605,198),BLUE,4)
    s.text(560,236,('вес t','weight t'),18,anchor='middle')
    s.text(560,420,('Ребро ab остаётся. Исчезают только две граничные отметки.','Edge ab remains. Only two boundary marks are removed.'),23,anchor='middle')
    s.save_pair('Один лес при смене границы','One forest as the boundary changes')

def square_step():
    s=Figure(1120,770,('Первый шаг топонома квадрата','The first square toponome step'),('Начальное ребро ab выбрано. Без новых рёбер старая компонента закрывается. Любые два новых ребра дают дерево на четырёх вершинах, объясняя коэффициент три.','The initial edge ab is selected. With no new edges, the old component closes. Any two new edges yield a tree on four vertices, explaining the coefficient three.'))
    s.text(30,42,('Начальное состояние tC₂: ребро ab уже выбрано','Initial state tC₂: edge ab is already selected'),26,weight='bold')
    edges=[('a','c'),('b','d'),('c','d')]
    panels=[(25,75,(),('Нет новых рёбер','No new edges'),'t z₂ D₁,₁'),(585,75,(0,1),('Две продольные связи','Two longitudinal edges'),'t³ C₄'),(25,385,(0,2),('Верхняя связь и перекладина','Upper edge and rung'),'t³ C₄'),(585,385,(1,2),('Нижняя связь и перекладина','Lower edge and rung'),'t³ C₄')]
    for x,y,selected,title,result in panels:
        s.panel(x,y,510,285);s.text(x+20,y+35,title,21,weight='bold')
        ps={'a':(x+110,y+90),'b':(x+110,y+195),'c':(x+365,y+90),'d':(x+365,y+195)}
        s.line(ps['a'],ps['b'],GREEN,6)
        for k,(a,b) in enumerate(edges):s.line(ps[a],ps[b],BLUE if k in selected else '#cbd6e3',5 if k in selected else 2,'' if k in selected else '6 7')
        for name,p in ps.items():
            s.circle(p,5);s.text(p[0]+(-23 if name in 'ab' else 18),p[1]+6,{'a':'a','b':'b','c':'a′','d':'b′'}[name],22)
        s.text(x+255,y+254,result,25,anchor='middle',weight='bold',color=PURPLE)
    s.text(560,714,('Три выбора пары новых рёбер дают вклад 3t³C₄.','Three choices of two new edges contribute 3t³C₄.'),24,anchor='middle',weight='bold')
    s.text(560,748,('Все три новых ребра вместе с ab образовали бы цикл.','All three new edges together with ab would form a cycle.'),20,anchor='middle',color=MUTED)
    s.save_pair('Первый шаг топонома квадрата','The first square toponome step')

def primal_dual():
    s=Figure(1160,480,('От цепочки к двойственному графу','From a chain to its dual graph'),('Два шва пересечены двойственными рёбрами f1f2 и f2f3. Внешнее ребро пересечено связью f1 с внешней гранью. Показана часть двойственного графа.','Two seams are crossed by dual edges f1f2 and f2f3. An external edge is crossed by a connection from f1 to the outer face. Only part of the dual graph is shown.'))
    s.text(30,42,('Каждое ребро связывает две соседние грани','Each edge links its two incident faces'),26,weight='bold')
    centers=[(165+sqrt(3)*100*k,250) for k in range(3)]
    for k,(cx,cy) in enumerate(centers):
        ps=[(cx+100*cos(pi/6+i*pi/3),cy+100*sin(pi/6+i*pi/3)) for i in range(6)]
        s.polygon(ps,FILLS[k])
        for a,b in zip(ps,ps[1:]+ps[:1]):s.line(a,b,MUTED,3)
        for p in ps:s.circle(p,4)
    for a,b in zip(centers,centers[1:]):s.line(a,b,PURPLE,4,'8 5')
    outer=(340,92);cross=(165+sqrt(3)*25,175)
    s.line(centers[0],cross,PURPLE,4,'8 5');s.line(cross,outer,PURPLE,4,'8 5')
    for k,p in enumerate(centers,1):s.circle(p,17,'white',PURPLE,3);s.text(p[0],p[1]+7,'f'+str(k),20,PURPLE,anchor='middle')
    s.circle(outer,20,'white',PURPLE,3);s.text(outer[0],outer[1]+7,'f∞',21,PURPLE,anchor='middle')
    s.text(365,98,('внешняя грань','outer face'),19,MUTED)
    s.text(695,160,('Шов между ядрами:','A seam between cores:'),22,weight='bold')
    s.text(695,198,'f₁ — f₂  /  f₂ — f₃',25,PURPLE)
    s.text(695,260,('Ребро внешнего контура:','An outer boundary edge:'),22,weight='bold')
    s.text(695,298,'f₁ — f∞',25,PURPLE)
    s.text(580,405,('Показаны 3 из 16 двойственных рёбер.','3 of the 16 dual edges are shown.'),23,anchor='middle',weight='bold')
    s.text(580,446,('В полном графе к f∞ ведут 5, 4 и 5 рёбер от трёх ядер.','In the full graph, the three cores have 5, 4 and 5 edges to f∞.'),21,anchor='middle')
    s.save_pair('От цепочки к двойственному графу','From a chain to its dual graph')

def prisms():
    s=Figure(1180,970,('Боковые грани призм и соответствия вершин','Prism side faces and vertex correspondences'),('В среднем ядре C6 на K2 выделены вход F0 и выход F2 либо F3. Ниже показаны два отождествления F0 внешнего ядра с F2 среднего: без сдвига и со сдвигом на одну вершину.','The middle core C6 Cartesian K2 has input F0 and output F2 or F3 highlighted. Below, F0 of an outer core is identified with F2 of the middle core, either directly or shifted by one vertex.'))
    s.text(30,42,('1. Выбрать две боковые грани среднего ядра','1. Choose two lateral faces of the middle core'),26,weight='bold')
    for x,j in [(25,2),(615,3)]:
        s.panel(x,65,540,420);cx=x+270;cy=195
        s.text(cx,104,'F₀  +  '+('F₂' if j==2 else 'F₃'),25,anchor='middle',weight='bold')
        ps={i:(cx+140*cos(-pi/3+i*pi/3),cy+55*sin(-pi/3+i*pi/3)) for i in range(6)}
        ps.update({i+6:(ps[i][0]+55,ps[i][1]+150) for i in range(6)})
        faces=[[0,1,7,6],[j,j+1,j+7,j+6]]
        for face,fill in zip(faces,['#ffe0e7','#dcecff']):s.polygon([ps[k] for k in face],fill)
        for i in range(6):
            for a,b in [(i,(i+1)%6),(i+6,(i+1)%6+6),(i,i+6)]:s.line(ps[a],ps[b],MUTED,2)
        for face,col in zip(faces,[RED,BLUE]):
            for a,b in zip(face,face[1:]+face[:1]):s.line(ps[a],ps[b],col,4)
        for i,p in ps.items():
            s.circle(p,5,'white',INK,2)
            dx=(p[0]-cx)/140;dy=-16 if i<6 else 25
            s.text(p[0]+14*dx,p[1]+dy,str(i),19,anchor='middle')
        s.text(cx,454,'F₀ = (0, 1, 7, 6);  '+('F₂ = (2, 3, 9, 8)' if j==2 else 'F₃ = (3, 4, 10, 9)'),20,anchor='middle')
    s.text(30,535,('2. Задать соответствие F₀ → F₂','2. Specify the correspondence F₀ → F₂'),26,weight='bold')
    for x,r in [(25,0),(615,1)]:
        s.panel(x,562,540,320)
        s.text(x+270,600,'r = '+str(r),25,anchor='middle',weight='bold')
        s.text(x+135,635,('Внешнее ядро','Outer core'),19,anchor='middle');s.text(x+405,635,('Среднее ядро','Middle core'),19,anchor='middle')
        left=[0,1,7,6];right=[2,3,9,8]
        for k in range(4):
            yy=670+52*k;target=670+52*((k+r)%4)
            s.arrow((x+153,yy),(x+386,target),PURPLE,2.5)
        for side,values in [(135,left),(405,right)]:
            for k,v in enumerate(values):
                p=(x+side,670+52*k);s.circle(p,16,'white',INK,2);s.text(p[0],p[1]+6,str(v),20,anchor='middle')
    s.text(590,922,('r = 0: типы рёбер сохраняются; r = 1: основания и продольные рёбра меняются местами.','r = 0 preserves edge types; r = 1 exchanges base edges and longitudinal edges.'),21,anchor='middle')
    s.text(590,958,('Стрелки задают отождествление вершин, а не новые рёбра.','Arrows specify vertex identifications, not new edges.'),20,anchor='middle',color=MUTED)
    s.save_pair('Боковые грани призм и соответствия вершин','Prism side faces and vertex correspondences')

if __name__=='__main__':
    routes();forgetting();square_step();primal_dual();prisms()
    CATALOG.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Generated five editorial diagrams and their translation entries.')
