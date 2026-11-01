"""Reproduce four boundary-transfer diagrams with the standard-library SVG helper."""
from draw_three_hexagons import SVG, ring, reflect, INK, MUTED, RED, BLUE, GREEN, FILLS


def vertex(s, pt, label, color=INK, offset=(0, -15)):
    s.circle(pt, 7, 'white', color, 3)
    s.text(pt[0]+offset[0], pt[1]+offset[1], label, 21, color, 'middle')


def flow():
    s = SVG(1200, 460, 'Смена активной спектральной границы',
        'Старый фрагмент G соединяется с ядром K только через a,b. Его внутренность заменяется блоком S и множителем E. Пять новых миноров вычисляются на выходе c,d.')
    for x, width in [(20,355),(420,355),(820,360)]:
        s.panel(x,20,width,420)
    s.text(197,57,'1. Присоединить ядро',23,anchor='middle',weight='bold')
    s.polygon([(55,136),(140,110),(182,168),(182,271),(140,310),(55,286)],FILLS[0])
    s.polygon([(182,168),(300,139),(337,216),(300,300),(182,271)],FILLS[2])
    s.text(107,222,'G',32,anchor='middle',weight='bold')
    s.text(266,222,'K',32,anchor='middle',weight='bold')
    s.line((182,168),(182,271),RED,5)
    vertex(s,(182,168),'a',RED)
    vertex(s,(182,271),'b',RED,(0,29))
    vertex(s,(300,139),'c',BLUE)
    vertex(s,(300,300),'d',BLUE,(0,29))
    s.text(197,370,'Общие вершины: только a, b',19,MUTED,'middle')
    s.text(197,404,'Активная пара: (a, b)',21,RED,'middle')
    s.arrow((385,230),(410,230))
    s.text(597,57,'2. Исключить внутренность G',21,anchor='middle',weight='bold')
    s.polygon([(480,168),(692,139),(730,216),(692,300),(480,271)],FILLS[2])
    s.line((480,168),(480,271),RED,5)
    vertex(s,(480,168),'a',RED)
    vertex(s,(480,271),'b',RED,(0,29))
    vertex(s,(692,139),'c',BLUE)
    vertex(s,(692,300),'d',BLUE,(0,29))
    s.text(590,204,'S на входе',24,RED,'middle')
    s.text(590,246,'K связывает пары',19,MUTED,'middle')
    s.text(597,370,'Сохранить множитель E',22,GREEN,'middle', 'bold')
    s.text(597,404,'H = W + U S Uᵀ',23,anchor='middle')
    s.arrow((785,230),(810,230))
    s.text(1000,57,'3. Вычислить новый паспорт',21,anchor='middle',weight='bold')
    s.line((940,150),(1060,150),BLUE,5)
    vertex(s,(940,150),'c',BLUE)
    vertex(s,(1060,150),'d',BLUE)
    s.text(1000,226,'(A′, B′, C′, D′, E′)',27,anchor='middle',weight='bold')
    s.text(1000,278,'s′ = T s',30,GREEN,'middle')
    s.text(1000,370,'Пять полиномов',22,anchor='middle')
    s.text(1000,404,'Активная пара: (c, d)',21,BLUE,'middle')
    s.save('Смена активной спектральной границы.svg')


def exits():
    s = SVG(1170, 430, 'Три выходных шва шестиугольника',
        'Красный вход упорядочен от 0 к 1. Синие выходы упорядочены от 2 к 3, от 3 к 4 и от 4 к 5. Стрелки обозначают порядок пары, а не ориентацию графа.')
    for x,j in [(20,2),(410,3),(800,4)]:
        s.panel(x,15,350,395)
        cx,cy,r = x+175,212,100
        p=ring(cx,cy,r)
        s.text(cx,57,f'Выход ({j}, {j+1})',25,anchor='middle',weight='bold')
        s.polygon(list(p.values()),FILLS[1])
        for i in range(6):
            s.line(p[i],p[(i+1)%6],RED if i==0 else BLUE if i==j else MUTED,
                6 if i in [0,j] else 3)
        # Place order arrows just inside their edges.
        for i,color in [(0,RED),(j,BLUE)]:
            aa=tuple(cx+(p[i][0]-cx)*.76 if q==0 else cy+(p[i][1]-cy)*.76 for q in [0,1])
            bb=tuple(cx+(p[i+1][0]-cx)*.76 if q==0 else cy+(p[i+1][1]-cy)*.76 for q in [0,1])
            s.arrow(aa,bb)
        for i,pt in p.items():
            s.circle(pt,6,'white',INK)
            s.text(cx+(pt[0]-cx)*1.22,cy+(pt[1]-cy)*1.22+7,str(i),22,anchor='middle')
        s.text(cx,380,f'T{str(j).translate(str.maketrans("234","₂₃₄"))}',29,BLUE,'middle','bold')
    s.save('Три выходных шва шестиугольника.svg')


def two_hexagons(s,cx,cy,r,j):
    p=ring(cx,cy,r)
    old=[0,1,9,8,7,6]
    for k,v in enumerate(old[2:],2):
        p[v]=reflect(p[k],p[0],p[1])
    cores=[old,list(range(6))]
    for i,core in enumerate(cores):
        s.polygon([p[v] for v in core],FILLS[i])
    edges={tuple(sorted((a,b))) for c in cores for a,b in zip(c,c[1:]+c[:1])}
    assert len(edges)==11 and len(p)==10
    for a,b in edges:
        s.line(p[a],p[b])
    s.line(p[0],p[1],RED,5)
    s.line(p[j],p[j+1],BLUE,6)
    for i,pt in p.items():
        s.circle(pt,5,'white',BLUE if i in [j,j+1] else INK)
        if i == 0:
            s.text(pt[0]-11,pt[1]+26,'0',19,anchor='middle')
        elif i == 1:
            s.text(pt[0]+8,pt[1]-10,'1',19,anchor='middle')
        elif i<6:
            s.text(cx+(pt[0]-cx)*1.27,cy+(pt[1]-cy)*1.27+6,str(i),19,anchor='middle')


def memory():
    s=SVG(1180,520,'Спектральная память двух шестиугольников',
        'Два одинаковых графа из двух шестиугольников имеют P(1)=28435, но разные отмеченные выходы. Добавление третьего шестиугольника даёт изомер Б со значением 2504096 или А со значением 2518737.')
    for y,j,label,value,coords in [(20,2,'Б','2 504 096','(12331, 12694, 4763, 4707)'),
                                    (270,3,'А','2 518 737','(12694, 12694, 4884, 4828)')]:
        s.panel(20,y,1140,230)
        two_hexagons(s,138,y+112,54,j)
        s.text(425,y+44,f'Выход ({j}, {j+1})',24,BLUE,'middle','bold')
        s.text(425,y+91,'P(1) = 28 435',26,anchor='middle',weight='bold')
        s.text(425,y+135,'Остальные координаты z:',19,MUTED,'middle')
        s.text(425,y+172,coords,19,anchor='middle')
        s.arrow((660,y+116),(803,y+116))
        s.text(732,y+88,'+ C₆',25,anchor='middle')
        s.text(732,y+151,'по выходу',18,MUTED,'middle')
        s.text(980,y+72,f'Три ядра · изомер {label}',24,anchor='middle',weight='bold')
        s.text(980,y+127,'P(1) = '+value,28,GREEN,'middle','bold')
        s.text(980,y+175,'Та же завершающая строка',18,MUTED,'middle')
    s.save('Спектральная память двух шестиугольников.svg')


def singular():
    s=SVG(1180,440,'Перенос при нулевом внутреннем миноре',
        'Путь a-u-b соединяется с путём a-c-d-b в цикл C5. Вход a,b не является ребром. При xi=2 старый внутренний минор нулевой, но оба полиномиальных паспорта определены.')
    s.panel(20,20,480,400)
    s.panel(540,20,620,400)
    p={'a':(125,135),'u':(90,262),'b':(260,340),'c':(285,106),'d':(383,230)}
    for a,b in [('a','u'),('u','b')]:
        s.line(p[a],p[b],RED,5)
    for a,b in [('a','c'),('c','d'),('d','b')]:
        s.line(p[a],p[b],BLUE,5)
    for label,pt in p.items():
        vertex(s,pt,label,RED if label in ['a','b','u'] else BLUE)
    s.text(260,57,'Два пути образуют C₅',25,anchor='middle',weight='bold')
    s.text(227,216,'G',30,RED,'middle')
    s.text(330,198,'K',30,BLUE,'middle')
    s.text(260,390,'Вход (a, b) · выход (c, d)',22,anchor='middle')
    s.arrow((510,230),(530,230))
    s.text(850,69,'ξ = 2 · E(2) = 0',29,anchor='middle',weight='bold')
    s.text(850,127,'Старое: (−2, −1, −1, 1, 0)',27,RED,'middle')
    s.text(850,186,'T(2)',27,anchor='middle')
    s.arrow((850,205),(850,244))
    s.text(850,287,'Новое: (2, 1, 1, 1, 0)',27,BLUE,'middle')
    s.text(850,352,'Полиномиальный перенос без деления на E',21,GREEN,'middle')
    s.text(850,389,'Прямые миноры дают тот же результат',21,MUTED,'middle')
    s.save('Перенос при нулевом внутреннем миноре.svg')


if __name__=='__main__':
    flow()
    exits()
    memory()
    singular()
