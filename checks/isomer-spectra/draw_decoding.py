"""Three reproducible SVG figures; exact numerical labels come from the audit."""
from itertools import product
from math import cos, sin, pi
from pathlib import Path
import json
from draw_three_hexagons import SVG, INK, MUTED, RED, BLUE, GREEN
from draw_slr_code import draw_chain, geometry

DATA=json.loads(Path(__file__).with_name('decoding-results.json').read_text(encoding='utf-8'))


def rect(s,x,y,w,h,fill,stroke='none'):
    s.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>')


def forests():
    s=SVG(1200,790,'Пять корневых координат',
          'По одному корневому лесу на C6 для каждого из пяти условий. Зелёные вершины являются корнями; красное кольцо отмечает x, синее y. Пунктир показывает невыбранные рёбра цикла. Классы лесов пересекаются.')
    s.text(600,38,'Корни леса и отметки границы',28,anchor='middle',weight='bold')
    examples=[('a','Все корневые леса',20,65,[(0,1),(1,2),(3,4)],{1,3,5},['Один корень','в каждой компоненте']),
              ('b','x является корнем',420,65,[(0,1),(1,2),(3,4)],{0,3,5},['Корень компоненты x','обязательно равен x']),
              ('c','y является корнем',820,65,[(0,1),(1,2),(3,4)],{1,3,5},['Корень компоненты y','обязательно равен y']),
              ('d','x и y в одном дереве',220,405,[(0,1),(1,2),(3,4)],{1,3,5},['Общая компонента','укоренена в y']),
              ('e','Два предписанных корня',620,405,[(1,2),(2,3),(4,5)],{0,1,4},['x и y являются корнями','разных компонент'])]
    for key,title,x,y,edges,roots,lines in examples:
        s.panel(x,y,360,315)
        s.text(x+180,y+32,f'{key} · {title}',21,anchor='middle',weight='bold')
        cx,cy=x+180,y+149
        pts={i:(cx+68*cos(5*pi/6-i*pi/3),cy-68*sin(5*pi/6-i*pi/3)) for i in range(6)}
        selected={frozenset(e) for e in edges}
        for i in range(6):
            a,b=pts[i],pts[(i+1)%6]
            if frozenset((i,(i+1)%6)) in selected:s.line(a,b,INK,4)
            else:s.parts.append(f'<path d="M {a[0]} {a[1]} L {b[0]} {b[1]}" stroke="#c8d2dd" stroke-width="2" stroke-dasharray="5 6"/>')
        for i,p in pts.items():
            if i in (0,1):s.circle(p,12,'white',RED if i==0 else BLUE,3)
            s.circle(p,6,GREEN if i in roots else 'white',INK,1.5)
        for i,label,color in [(0,'x',RED),(1,'y',BLUE)]:
            p=pts[i];s.text(p[0]+(-19 if i==0 else 19),p[1]-14,label,23,color,'middle','bold')
        for j,line in enumerate(lines):s.text(x+180,y+263+27*j,line,20,MUTED,'middle')
    s.circle((264,764),7,GREEN);s.text(282,771,'корень',20)
    s.circle((444,764),11,'white',RED,3);s.text(464,771,'отметка x',20)
    s.circle((670,764),11,'white',BLUE,3);s.text(690,771,'отметка y',20)
    s.text(1020,771,'классы пересекаются',19,MUTED,'middle')
    s.save('Пять корневых координат.svg')


def sectors():
    s=SVG(1200,710,'Три сектора декодирования',
          'Проекция инвариантной области на b/a,c/a. Пороги 4/9 разделяют L: минус плюс, S: плюс плюс, R: плюс минус. Нижний левый сектор невозможен для потомков. Начальное состояние лежит на верхнем правом углу и проверяется отдельно.')
    s.text(600,38,'Последний переход определяется двумя знаками',28,anchor='middle',weight='bold')
    x0,y0,size=105,105,480
    def xy(r,t):return (x0+(r-.43)/.02*size,y0+size-(t-.43)/.02*size)
    xp,yp=xy(4/9,4/9)
    rect(s,x0,y0,xp-x0,yp-y0,'#fce4e9')
    rect(s,xp,y0,x0+size-xp,yp-y0,'#def3e8')
    rect(s,xp,yp,x0+size-xp,y0+size-yp,'#e2edff')
    rect(s,x0,yp,xp-x0,y0+size-yp,'#f0f2f5')
    rect(s,x0,y0,size,size,'none',MUTED)
    s.line((xp,y0),(xp,y0+size),MUTED,2)
    s.line((x0,yp),(x0+size,yp),MUTED,2)
    s.text(x0+100,y0+70,'L  (−,+)',26,RED,'middle','bold')
    s.text(xp+66,y0+40,'S  (+,+)',23,GREEN,'middle','bold')
    s.text(xp+66,yp+190,'R  (+,−)',23,BLUE,'middle','bold')
    s.text(x0+170,yp+155,'(−,−)',27,MUTED,'middle')
    s.text(x0+170,yp+190,'нет непустых потомков',21,MUTED,'middle')
    for value,label in [(.43,'43/100'),(4/9,'4/9'),(.45,'9/20')]:
        x,y=xy(value,value)
        s.text(x,y0+size+33,label,21,MUTED,'middle')
        s.text(x0-15,y+7,label,21,MUTED,'end')
    s.text(x0+size+38,y0+size+5,'b/a',24,anchor='middle')
    s.text(x0,y0-24,'c/a',24,anchor='middle')
    colors={'S':GREEN,'L':RED,'R':BLUE}
    seed=(320,144,144,56,55)
    def step(c,z):return tuple(sum(v*w for v,w in zip(row,z)) for row in DATA['matrices'][c])
    for length in range(1,4):
        for word in product('SLR',repeat=length):
            z=seed
            for c in word:z=step(c,z)
            s.circle(xy(z[1]/z[0],z[2]/z[0]),4,colors[word[-1]],'white',.8)
    seed_pt=xy(seed[1]/seed[0],seed[2]/seed[0]);s.circle(seed_pt,7,'white',INK,3)
    s.line((seed_pt[0]+9,seed_pt[1]),(685,105),INK,2)
    s.text(707,111,'z₀: сначала проверка остановки',22,weight='bold')
    s.panel(685,160,480,340)
    lines=[('U = 9b − 4a',28,INK),('V = 9c − 4a',28,INK),
           ('L: снять Nₗ',25,RED),('S: снять Nₛ',25,GREEN),('R: снять Nᵣ',25,BLUE),
           ('После выбора применить обратную матрицу',20,MUTED)]
    for i,(line,fs,color) in enumerate(lines):s.text(925,205+i*49,line,fs,color,'middle')
    s.text(925,554,'Точки: слова операций длины 1–3',22,MUTED,'middle')
    s.text(925,588,'Цветные области показывают знаки,',21,MUTED,'middle')
    s.text(925,617,'а не все достижимые состояния',21,MUTED,'middle')
    s.text(600,678,'Пороги точные; размещение точек на рисунке приближённое',22,MUTED,'middle')
    s.save('Три сектора декодирования.svg')


def backwards():
    s=SVG(1200,920,'Обратное чтение SLR',
          'Полный код SLR имеет четыре ядра и слово операций LRS. Декодирование снимает S, затем R, затем L и достигает начального состояния. Последнее S относится к конечной отметке, начальное S в полном коде является маркером.')
    s.text(600,38,'Код цепочки SLR · слово операций LRS',28,anchor='middle',weight='bold')
    points,_=draw_chain(s,'LR',(55,85,510,180))
    _,_,_,active=geometry('LR')
    s.line(points[active[0]],points[active[1]],GREEN,7)
    for v,label in zip(active,('x','y')):
        px,py=points[v]
        s.text(px+20,py+7,label,22,GREEN,'middle','bold')
    s.text(320,295,'Зелёное ребро: конечная упорядоченная граница',20,MUTED,'middle')
    for i,line in enumerate(['u = LR;  N = 4','ZSLR = Nₛ Nᵣ Nₗ z₀','P(1) = 220 480 560']):
        s.text(890,130+i*57,line,27,BLUE if i==2 else INK,'middle','bold')
    rows=list(reversed(DATA['example']))
    boxes=[(20,340),(650,340),(650,620),(20,620)]
    for i,(row,(x,y)) in enumerate(zip(rows,boxes)):
        s.panel(x,y,530,220)
        label='z('+row['word']+')' if row['word'] else 'z₀ · остановка'
        s.text(x+265,y+38,label,26,anchor='middle',weight='bold')
        a,b,c,d,e=row['state']
        s.text(x+265,y+85,f'a = {a:,}'.replace(',',' '),24,BLUE,'middle')
        s.text(x+265,y+124,f'b = {b:,};  c = {c:,}'.replace(',',' '),22,anchor='middle')
        s.text(x+265,y+159,f'd = {d:,};  e = {e:,}'.replace(',',' '),22,anchor='middle')
        if row['word']:
            u,v=row['U'],row['V']
            s.text(x+265,y+196,f'U = {u:,};  V = {v:,}'.replace(',',' '),21,MUTED,'middle')
        else:s.text(x+265,y+196,'Не снимать ещё одну букву S',21,RED,'middle')
    s.arrow((565,449),(635,449));s.text(600,425,'S⁻¹',26,GREEN,'middle')
    s.arrow((915,572),(915,608));s.text(957,598,'R⁻¹',26,BLUE,'middle')
    s.arrow((635,729),(565,729));s.text(600,705,'L⁻¹',26,RED,'middle')
    s.text(600,887,'Восстановлено LRS → удалить конечное S → LR → добавить маркер S → SLR',23,anchor='middle')
    s.save('Обратное чтение SLR.svg')


if __name__=='__main__':
    forests();sectors();backwards()
    print('Wrote 3 decoding figures')
