"""Four native SVG illustrations for the graph-weaving note; stdlib only."""
from pathlib import Path
import json

from draw_admissible_chains import SVG, INK, MUTED, EDGE, RED, BLUE, PURPLE

DATA = json.loads(Path(__file__).with_name('weaving-results.json').read_text(encoding='utf-8'))
GREEN = '#16816c'


def graph(s, positions, edges, plug=(), socket=(), labels=None, color=EDGE):
    for u,v in edges:
        s.line(positions[u],positions[v],color,4)
    for v,xy in positions.items():
        s.circle(xy,5)
        if v in plug:
            s.circle(xy,10,'white',RED,3)
            s.circle(xy,4,RED)
        if v in socket:
            s.circle(xy,10,'white',BLUE,3)
            s.circle(xy,4,BLUE)
        if labels and v in labels:
            text,dx,dy,anchor = labels[v]
            s.text(xy[0]+dx,xy[1]+dy,text,19,anchor=anchor)


def ladder(s,x,y,steps,dx=115,dy=100):
    positions = {(i,j):(x+i*dx,y+j*dy) for i in range(steps+1) for j in range(2)}
    edges = [((i,0),(i,1)) for i in range(steps+1)]
    edges += [((i,j),(i+1,j)) for i in range(steps) for j in range(2)]
    graph(s,positions,edges,plug=[(0,0),(0,1)],socket=[(steps,0),(steps,1)])
    return positions


def construction():
    s=SVG(1160,690,'Вилка и розетка при плетении',
          'Начальное ребро, трёхрёберный путь с вилкой и розеткой, первый квадрат и три повторения того же пути.')
    for x,w in [(20,235),(280,370),(675,465)]:
        s.panel(x,20,w,320)
    s.text(40,57,'1. Начало G₀',24,weight='bold')
    graph(s,{0:(135,130),1:(135,255)},[(0,1)],socket=(0,1))
    s.text(160,137,'a',21);s.text(160,262,'b',21)
    s.text(40,310,'Розетка: (a, b)',20,BLUE)
    s.text(300,57,'2. Один бегунок K',24,weight='bold')
    pos={0:(345,130),1:(560,130),2:(560,255),3:(345,255)}
    labels={0:('p₀',-16,7,'end'),3:('p₁',-16,7,'end'),1:('q₀',17,7,'start'),2:('q₁',17,7,'start')}
    graph(s,pos,[(0,1),(1,2),(2,3)],plug=(0,3),socket=(1,2),labels=labels)
    s.text(340,102,'Вилка',19,RED);s.text(525,102,'Розетка',19,BLUE)
    s.text(300,310,'Три ребра; между p₀ и p₁ ребра нет',17)
    s.text(695,57,'3. Вставить вилку в розетку',23,weight='bold')
    pos=ladder(s,750,130,1,260,125)
    s.text(726,137,'a',20,anchor='end');s.text(726,262,'b',20,anchor='end')
    s.text(1033,137,'q₀',20);s.text(1033,262,'q₁',20)
    s.text(695,310,'G₁: старое ребро + новый путь',19)
    s.panel(20,365,1120,305)
    s.text(42,405,'Повторяем тот же шаг',25,weight='bold')
    ladder(s,115,460,3,155,115)
    s.text(720,470,'G₃: три квадрата',25,weight='bold')
    s.text(720,514,'8 вершин · 10 рёбер',21)
    s.text(720,554,'Новая розетка всегда справа',19,BLUE)
    s.text(42,637,'Цветные кольца отмечают контакты. Они не добавляют рёбер к графу.',19,MUTED)
    s.save('Вилка и розетка при плетении.svg')


def states():
    s=SVG(1120,640,'Два остовных состояния плетения',
          'Одна координата суммирует деревья, другая — двухкомпонентные леса, разделяющие отмеченные контакты. Для квадрата координаты равны 4 и 3.')
    s.panel(20,20,520,345);s.panel(560,20,540,345)
    s.text(42,60,'Контакты соединены',25,weight='bold')
    s.text(582,60,'Контакты разделены',25,weight='bold')
    for x,mode in [(110,'tree'),(660,'forest')]:
        p={0:(x,130),1:(x+230,130),2:(x+230,260),3:(x,260)}
        for u,v in [(0,1),(1,2),(2,3),(3,0)]:
            s.line(p[u],p[v],'#c8d3df',3,'6 7')
        if mode=='tree':
            for u,v in [(0,1),(1,2),(2,3)]:s.line(p[u],p[v],GREEN,5)
        else:
            s.line(p[0],p[1],GREEN,5);s.line(p[2],p[3],PURPLE,5)
        graph(s,p,[],socket=(1,2))
        s.text(x+255,137,'x',20);s.text(x+255,267,'y',20)
    s.text(42,330,'τ = 4 дерева; показано одно',21)
    s.text(582,330,'σ = 3 разделяющих леса; показан один',21)
    s.panel(20,390,1080,230)
    s.text(42,432,'Путь-бегунок обновляет оба числа',25,weight='bold')
    vals=[x['state'] for x in DATA['examples']['square_ladder']['history'][:4]]
    for i,(a,b) in enumerate(vals):
        x=115+i*272
        s.text(x,498,f'({a}, {b})',29,anchor='middle',weight='bold')
        s.text(x,533,['ребро','квадрат','два квадрата','три квадрата'][i],18,anchor='middle',color=MUTED)
        if i<3:s.arrow((x+65,488),(x+190,488),BLUE)
    s.text(42,587,'τ′ = 3τ + σ',22)
    s.text(580,587,'σ′ = 2τ + σ',22)
    s.save('Два остовных состояния плетения.svg')


def runners():
    s=SVG(1160,590,'Три бегунка и их рекурсии',
          'Два пути с собственным остовным числом 1 и граф K4 без входного ребра с собственным остовным числом 8. У всех отмечены входные и выходные контакты.')
    for x in [20,400,780]:s.panel(x,20,360,550)
    s.text(42,61,'Путь P₄',25,weight='bold')
    s.text(422,61,'Путь P₆',25,weight='bold')
    s.text(802,61,'K₄ без ребра 01',24,weight='bold')
    p={0:(80,160),1:(290,160),2:(290,285),3:(80,285)}
    graph(s,p,[(0,1),(1,2),(2,3)],plug=(0,3),socket=(1,2))
    p={0:(450,160),1:(565,160),2:(680,160),3:(680,285),4:(565,285),5:(450,285)}
    graph(s,p,[(i,i+1) for i in range(5)],plug=(0,5),socket=(2,3))
    p={0:(825,225),1:(1095,225),2:(960,135),3:(960,315)}
    graph(s,p,[(0,2),(0,3),(1,2),(1,3),(2,3)],plug=(0,1),socket=(2,3),
          labels={0:('0',-14,7,'end'),1:('1',14,7,'start'),2:('2',15,-12,'start'),3:('3',15,24,'start')})
    for x,lines in [(42,['κ = 1','α = 3,  β = 1,  γ = 1','τₖ₊₂ = 4τₖ₊₁ − τₖ','1, 4, 15, 56, …']),
                    (422,['κ = 1','α = 5,  β = 1,  γ = 1','τₖ₊₂ = 6τₖ₊₁ − τₖ','1, 6, 35, 204, …']),
                    (802,['κ = 8','α = 1,  β = 1/2,  γ = 0','τₖ₊₂ = 12τₖ₊₁','1, 16, 192, 2304, …'])]:
        for j,line in enumerate(lines):s.text(x,385+j*47,line,22 if j!=1 else 19,weight='bold' if j==2 else 'normal')
    s.save('Три бегунка и их рекурсии.svg')


def closure():
    s=SVG(1120,755,'Начало плетения и замыкание',
          'При замыкании нужно хранить начальные контакты. Прямое и перекрёстное соответствия крайних пар квадратной полосы дают разные замыкания.')
    s.panel(20,20,1080,310)
    s.text(42,62,'Открытая полоса: начало сохраняется до последнего шага',25,weight='bold')
    ladder(s,210,125,3,225,120)
    for x,y,t,anchor in [(185,132,'a₀','end'),(185,252,'b₀','end'),(910,132,'a₃','start'),(910,252,'b₃','start')]:
        s.text(x,y,t,22,anchor=anchor)
    s.text(210,296,'B₀: начальная пара',20,RED)
    s.text(680,296,'B₃: текущая розетка',20,BLUE)
    for x,twist in [(20,False),(570,True)]:
        s.panel(x,355,530,280)
        s.text(x+22,397,'Скрещённое соответствие' if twist else 'Прямое соответствие',23,weight='bold')
        left=[(x+95,460),(x+95,555)];right=[(x+415,460),(x+415,555)]
        for i in range(2):
            s.line(left[i],right[1-i] if twist else right[i],PURPLE,3,'8 7')
            s.circle(left[i],8,'white',RED,3);s.circle(right[i],8,'white',BLUE,3)
            s.text(x+72,left[i][1]+7,['a₀','b₀'][i],21,anchor='end')
            s.text(x+438,right[i][1]+7,['a₃','b₃'][i],21)
        s.text(x+22,610,'Мёбиусово замыкание' if twist else 'Цилиндрическое замыкание',21)
    s.text(42,680,'Пунктир обозначает отождествления, а не новые рёбра.',21,MUTED)
    s.text(42,719,'Для единичного общего ребра одну из двух крайних копий удаляют.',21,MUTED)
    s.save('Начало плетения и замыкание.svg')


if __name__=='__main__':
    construction();states();runners();closure()
    print('Generated four graph-weaving SVGs.')
