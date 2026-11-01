"""Four native SVG figures for the exponential-weaving note; stdlib only."""
from pathlib import Path
import json
from draw_admissible_chains import SVG, INK, MUTED, BLUE, PURPLE, RED

GREEN='#16816c'
DATA=json.loads(Path(__file__).with_name('weaving-exponential-results.json').read_text(encoding='utf-8'))


def path(s,points,color=GREEN,width=5):
    for a,b in zip(points,points[1:]): s.line(a,b,color,width)
    for p in points: s.circle(p,6,color)


def contact(s,p,label,dx=0,dy=-20):
    s.circle(p,12,'white',BLUE,3)
    s.circle(p,5,BLUE)
    s.text(p[0]+dx,p[1]+dy,label,21,BLUE,anchor='middle')


def shift():
    s=SVG(1160,565,'Сдвиг и фактор экспоненты лестницы',
          'Старая квадратная лестница сдвигает индексы. Три новых ребра пути добавляются слева; старое входное ребро сохраняется в одном экземпляре.')
    for x in (20,405,790): s.panel(x,20,350,375)
    for x,title in [(40,'1. Лестница G₁'),(425,'2. Сдвиг S'),(810,'3. Умножение на Φ')]:s.text(x,60,title,23,weight='bold')
    for x,start,new in [(90,0,False),(475,1,False),(860,0,True)]:
        if new:
            points={(i,j):(x+100*i,140+145*j) for i in range(3) for j in range(2)}
            for i in (1,2):s.line(points[i,0],points[i,1],MUTED,4)
            for j in (0,1):s.line(points[1,j],points[2,j],MUTED,4)
            for a,b in [((0,0),(0,1)),((0,0),(1,0)),((0,1),(1,1))]:s.line(points[a],points[b],BLUE,6)
        else:
            points={(i,j):(x+170*i,140+145*j) for i in range(2) for j in range(2)}
            for i in (0,1):s.line(points[i,0],points[i,1],MUTED,4)
            for j in (0,1):s.line(points[0,j],points[1,j],MUTED,4)
        for (i,j),p in points.items():
            s.circle(p,6)
            label=('a' if j==0 else 'b')+str(i+start)
            s.text(p[0],p[1]+(-20 if j==0 else 33),label,21,anchor='middle')
    s.text(40,366,'M₁',24,weight='bold')
    s.text(425,366,'S(M₁)',24,weight='bold')
    s.text(810,366,'M₂ = Φ · S(M₁)',24,weight='bold')
    s.arrow((370,210),(398,210),BLUE)
    s.arrow((755,210),(783,210),BLUE)
    s.panel(20,420,1120,125)
    s.text(45,462,'Φ: новая перекладина и две продольные связи',25,BLUE,weight='bold')
    s.text(45,507,'Серые рёбра уже присутствуют. Повторяется деталь с новыми именами вершин.',21,MUTED)
    s.save('Сдвиг и фактор экспоненты лестницы.svg')


def sizes():
    s=SVG(1120,610,'Размеры активных компонент леса',
          'Состояние C5 содержит одно активное дерево на пяти вершинах. Состояние D3,2 содержит два активных дерева. В обоих примерах закрытое дерево на трёх вершинах даёт z3.')
    for x in (20,570):s.panel(x,20,530,465)
    s.text(42,60,'Оба контакта в одном дереве',23,weight='bold')
    s.text(592,60,'Контакты в разных деревьях',23,weight='bold')
    pts=[(105,140),(210,105),(315,140),(315,250),(105,250)]
    path(s,pts)
    contact(s,pts[0],'a',-30,7);contact(s,pts[-1],'b',-30,7)
    s.text(420,200,'C₅',29,GREEN,anchor='middle',weight='bold')
    p=[(655,140),(760,105),(865,140)]
    path(s,p);contact(s,p[0],'a',-30,7)
    p=[(655,250),(865,250)]
    path(s,p,PURPLE);contact(s,p[0],'b',-30,7)
    s.text(1000,205,'D₃,₂',29,GREEN,anchor='middle',weight='bold')
    for x,state in [(105,'z₃ C₅'),(655,'z₃ D₃,₂')]:
        path(s,[(x,355),(x+105,325),(x+210,355)],RED)
        s.text(x+105,397,'Закрытая компонента: z₃',20,RED,anchor='middle')
        s.text(x+105,453,state,26,anchor='middle',weight='bold')
    s.panel(20,510,1080,80)
    s.text(42,559,'При продолжении меняются только компоненты с отмеченными контактами.',22,MUTED)
    s.save('Размеры активных компонент леса.svg')


def reductions():
    s=SVG(1120,640,'От размеров компонент к двум и пяти координатам',
          'Полное граничное состояние хранит C_s и D_r,s с неограниченными размерами. Обычная оценка даёт две координаты, корневая оценка — пять определительных комбинаций.')
    s.panel(275,20,570,160)
    s.text(560,65,'Размеры граничных компонент',25,anchor='middle',weight='bold')
    s.text(560,111,'Cₛ и Dᵣ,ₛ',29,GREEN,anchor='middle',weight='bold')
    s.text(560,150,'Закрытые компоненты: множители zₛ',21,anchor='middle')
    s.arrow((405,180),(285,280),BLUE)
    s.arrow((715,180),(835,280),PURPLE)
    s.text(315,227,'zₛ = 1',23,BLUE,anchor='middle')
    s.text(805,227,'zₛ = s',23,PURPLE,anchor='middle')
    s.panel(20,290,520,255);s.panel(570,290,530,255)
    s.text(280,335,'Обычные леса',26,BLUE,anchor='middle',weight='bold')
    s.text(835,335,'Корневые леса',26,PURPLE,anchor='middle',weight='bold')
    s.text(280,389,'Контакты соединены / разделены',22,anchor='middle')
    s.text(835,389,'Свободные и закреплённые корни',22,anchor='middle')
    s.text(280,447,'Две полиномиальные координаты',22,anchor='middle',weight='bold')
    s.text(835,447,'Пять комбинаций A₊, B₊, C₊, D₊, E₊',22,anchor='middle',weight='bold')
    s.text(280,502,'Сумма: F(t)',24,BLUE,anchor='middle')
    s.text(835,502,'A₊ = P(t) = det(I + tL)',24,PURPLE,anchor='middle')
    s.text(560,595,'Обе оценки теряют часть распределения лесов по размерам компонент.',22,MUTED,anchor='middle')
    s.save('От размеров компонент к двум и пяти координатам.svg')


def difference():
    s=SVG(1160,600,'Третий грейд топономов двух изомеров',
          'Три типа лесов с тремя рёбрами. Разность чисел А минус Б равна минус один, плюс два, минус один. Корневые веса 4, 6, 8 обращают её в нуль.')
    counts=DATA['toponomes']['hex_grade_three_counts']
    for x in (20,405,790):s.panel(x,20,350,395)
    titles=['Тип (3)','Тип (2,1)','Тип (1,1,1)']
    for k,x in enumerate((20,405,790)):
        s.text(x+175,65,titles[k],26,anchor='middle',weight='bold')
        a,b=counts[k]['A'],counts[k]['B']
        s.text(x+175,292,f'А: {a}     Б: {b}',24,anchor='middle')
        s.text(x+175,338,f'Разность: {a-b:+d}',24,RED,anchor='middle',weight='bold')
        s.text(x+175,385,f'Корневой вес: {[4,6,8][k]}',22,anchor='middle')
    path(s,[(75,155),(150,120),(225,155),(300,120)])
    s.text(195,220,'Показан один из видов дерева',17,MUTED,anchor='middle')
    path(s,[(460,135),(550,100),(640,135)])
    path(s,[(500,205),(680,205)],PURPLE)
    for y,col in [(115,GREEN),(165,PURPLE),(215,BLUE)]:path(s,[(860,y),(1070,y)],col)
    s.panel(20,440,1120,140)
    s.text(580,482,'Разность топономов: −x₃ + 2x₂x₁ − x₁³',28,anchor='middle',weight='bold')
    s.text(580,528,'Корневая оценка: −4 + 2 · 6 − 8 = 0',25,PURPLE,anchor='middle')
    s.text(580,561,'Всего 14 вершин; изолированные вершины на схемах не показаны.',18,MUTED,anchor='middle')
    s.save('Третий грейд топономов двух изомеров.svg')


if __name__=='__main__':
    shift();sizes();reductions();difference()
    print('Generated four SVG figures.')
