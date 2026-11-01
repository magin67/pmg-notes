"""Six SVG figures; exact numerical data come from the verification JSON.

Matplotlib draws the scientific plots; all other elements are native SVG.
"""
from pathlib import Path
from fractions import Fraction as F
from math import cos, sin, pi, exp
from io import StringIO
import json
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from draw_three_hexagons import SVG, INK, MUTED, RED, BLUE, GREEN, FILLS
from draw_slr_code import geometry

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'boundary-response-results.json').read_text(encoding='utf-8'))


def ground(s,p):
    x,y=p
    s.line((x,y-12),(x,y),MUTED,2)
    for k,w in enumerate((22,15,7)):
        s.line((x-w/2,y+5*k),(x+w/2,y+5*k),MUTED,2)


def electrical():
    s=SVG(1200,650,'Два опыта с заземлённой цепочкой',
          'В каждой вершине, включая x и y, есть единичная проводимость к общей земле. '
          'Первый опыт с токами (1,0) даёт напряжения (r,h); второй с токами (0,1) даёт (h,s).')
    s.text(600,42,'Вспомогательная сеть G*: по резистору к общей точке',27,anchor='middle',weight='bold')
    s.panel(20,75,520,495)
    s.text(280,112,'Один C₆ для иллюстрации',23,anchor='middle',weight='bold')
    cx,cy,R=255,315,110
    p=[(cx+R*cos(-pi/6+i*pi/3),cy+R*sin(-pi/6+i*pi/3)) for i in range(6)]
    s.polygon(p,FILLS[1])
    for i in range(6):s.line(p[i],p[(i+1)%6],INK,3)
    for i,(x,y) in enumerate(p):
        theta=-pi/6+i*pi/3
        end=(cx+1.72*R*cos(theta),cy+1.72*R*sin(theta))
        s.line((x,y),end,MUTED,2)
        # A finite resistor, not a direct wire from the vertex to ground.
        mid=((x+end[0])/2,(y+end[1])/2)
        normal=(-sin(theta),cos(theta))
        along=(cos(theta),sin(theta))
        rect=[(mid[0]+a*along[0]+b*normal[0],mid[1]+a*along[1]+b*normal[1])
              for a,b in ((-11,-5),(11,-5),(11,5),(-11,5))]
        s.polygon(rect,'white')
        for a,b in zip(rect,rect[1:]+rect[:1]):s.line(a,b,BLUE,2)
        s.text(mid[0]+12,mid[1]-6,'1',18,BLUE)
        ground(s,(end[0],end[1]+12))
        s.circle((x,y),7 if i in (0,1) else 5,'white' if i in (0,1) else INK,BLUE if i in (0,1) else INK,3)
    s.text(p[0][0]-19,p[0][1]-16,'x',24,BLUE,weight='bold')
    s.text(p[1][0]-19,p[1][1]+30,'y',24,BLUE,weight='bold')
    s.text(cx,cy+5,'C₆',27,anchor='middle')
    s.text(280,550,'Все рёбра графа также имеют вес 1',19,MUTED,'middle')
    for y,title,inputs,outputs in [
        (75,'Опыт 1: ток подан в x','jₓ = 1,  jᵧ = 0','vₓ = r,  vᵧ = h'),
        (290,'Опыт 2: ток подан в y','jₓ = 0,  jᵧ = 1','vₓ = h,  vᵧ = s')]:
        s.panel(575,y,605,185)
        s.text(877,y+42,title,24,anchor='middle',weight='bold')
        s.text(625,y+99,inputs,25,BLUE)
        s.arrow((890,y+90),(940,y+90))
        s.text(962,y+99,outputs.split(',')[0],24,GREEN)
        s.text(962,y+139,outputs.split(',')[1].strip(),24,GREEN)
    s.text(877,530,'Нулевой ток не означает нулевое напряжение',20,RED,'middle')
    s.text(600,615,'Два опыта · четыре показания: r, h, h, s · общая точка * является добавленной',23,anchor='middle')
    s.save('Два опыта с заземлённой цепочкой.svg')


def embed_plot(s,fig,x,y,w,h):
    stream=StringIO();fig.savefig(stream,format='svg',metadata={'Date':None});plt.close(fig)
    root=ET.fromstring(stream.getvalue())
    for key,value in [('x',x),('y',y),('width',w),('height',h)]:root.set(key,str(value))
    s.parts.append('\n'.join(line.rstrip() for line in ET.tostring(root,encoding='unicode').splitlines()))


def dynamic_response():
    s=SVG(1200,820,'Динамический отклик исходной цепочки',
          'Одинаковые единичные теплоёмкости в вершинах и теплопроводности рёбер. '
          'Нет новых рёбер и внешнего теплообмена. На примере C6 показаны точные функции '
          'собственного и перекрёстного откликов; взвешенные интегралы равны 9/20 и 7/40.')
    s.text(600,42,'Исходный граф · распространение тепла без новых рёбер',27,anchor='middle',weight='bold')
    s.panel(20,75,350,470)
    s.text(195,115,'Один C₆: пример',25,anchor='middle',weight='bold')
    p=[(180+95*cos(-pi/6+i*pi/3),255+95*sin(-pi/6+i*pi/3)) for i in range(6)]
    s.polygon(p,FILLS[1])
    for i in range(6):s.line(p[i],p[(i+1)%6],MUTED,3)
    for i,q in enumerate(p):s.circle(q,7 if i<2 else 5,'white' if i<2 else INK,BLUE if i==0 else GREEN if i==1 else INK,3)
    s.text(p[0][0]+18,p[0][1]+7,'x',25,BLUE)
    s.text(p[1][0]+18,p[1][1]+7,'y',25,GREEN)
    s.text(195,391,'У x и y по два соседа',21,anchor='middle')
    s.text(195,437,'Импульс в x: Fₓₓ, Fᵧₓ',21,BLUE,'middle')
    s.text(195,477,'Импульс в y: Fₓᵧ, Fᵧᵧ',21,GREEN,'middle')
    s.text(195,516,'Записываем обе температуры',18,MUTED,'middle')
    data=DATA['original_graph_models']['C6_heat']
    ts=[i/80 for i in range(481)]
    values=lambda key:[sum(float(c)*exp(-rate*t) for c,rate in zip(data[key],data['decay_rates']))/data['normalization'] for t in ts]
    with plt.rc_context({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none','svg.hashsalt':'pmg-dynamic-response'}):
        fig,ax=plt.subplots(figsize=(7.9,4.7),layout='constrained')
        ax.plot(ts,values('self_coefficients'),color=BLUE,lw=2.5,label='Собственный Fₓₓ = Fᵧᵧ')
        ax.plot(ts,values('cross_coefficients'),color=GREEN,lw=2.5,label='Перекрёстный Fₓᵧ = Fᵧₓ')
        ax.set_xlabel('Время t');ax.set_ylabel('Температура')
        ax.set_xlim(0,6);ax.set_ylim(0,1.02);ax.grid(alpha=.2);ax.legend(fontsize=12)
        ax.spines[['top','right']].set_visible(False)
        embed_plot(s,fig,390,75,790,470)
    s.panel(20,572,1160,218)
    s.text(600,610,'Обработка записи: умножить на e⁻ᵗ и проинтегрировать',25,anchor='middle',weight='bold')
    r,h=data['weighted_integrals']
    s.text(330,660,f'Для C₆: r = s = {r}',27,BLUE,'middle')
    s.text(875,660,f'h = {h}',27,GREEN,'middle')
    s.text(600,706,'В общем случае четыре интеграла: r, h, h, s',23,anchor='middle')
    s.text(600,753,'Вес e⁻ᵗ применяется к данным; физической утечки во внешнюю среду нет',21,MUTED,'middle')
    s.save('Динамический отклик исходной цепочки.svg')


def ordinary_resistance():
    s=SVG(1200,780,'Одинаковое конечное сопротивление',
          'Исходные цепочки SS и SL из трёх ядер имеют одинаковое сопротивление на '
          'каноническом конечном ребре: 169/204. Префикс заменяется его сопротивлением '
          'R предыдущего шага; две ветви имеют сопротивления 1 и 4+R.')
    s.text(600,42,'Обычный стационарный опыт на выбранном конечном ребре',26,anchor='middle',weight='bold')
    for x,u,name in [(20,'S','SS'),(620,'L','SL')]:
        s.panel(x,75,560,320)
        s.text(x+45,119,name,28,BLUE if name=='SS' else RED,weight='bold')
        ending_chain(s,u,(x+100,143,360,155),name=='SL')
        R=DATA['original_graph_models']['examples'][name]['resistance']
        s.text(x+280,363,'Rₓᵧ = '+R,27,anchor='middle',weight='bold')
    s.text(600,441,'В обоих графах доступны только x и y; дополнительных рёбер нет',22,MUTED,'middle')
    left,right=(340,560),(860,560)
    s.line(left,right,BLUE,4)
    for pt in (left,right):s.circle(pt,7,'white',GREEN,3)
    s.text(310,567,'x',24,GREEN);s.text(880,567,'y',24,GREEN)
    s.text(600,541,'Выбранное ребро: 1',22,BLUE,'middle')
    s.line(left,(340,655),MUTED,3);s.line((340,655),(860,655),MUTED,3);s.line((860,655),right,MUTED,3)
    s.text(600,638,'Оставшийся путь: 4 + Rₙ₋₁',24,anchor='middle')
    s.text(600,731,'Параллельные ветви дают Rₙ = (4 + Rₙ₋₁) / (5 + Rₙ₋₁)',26,anchor='middle',weight='bold')
    s.save('Одинаковое конечное сопротивление.svg')


def probability():
    s=SVG(1200,610,'Два вероятностных прочтения отклика',
          'Совместный закон корней: вероятности исходов 11,10,01,00 равны k,r-k,s-k,1-r-s+k. '
          'В блуждании по единичным рёбрам остановка имеет интенсивность 1; при степени 2 каждый из двух переходов и остановка имеет вероятность 1/3.')
    s.panel(20,20,550,560);s.panel(600,20,580,560)
    s.text(295,66,'Случайный корневой лес',27,anchor='middle',weight='bold')
    s.text(295,101,'Два признака: является ли контакт корнем?',19,MUTED,'middle')
    for y,bits,label in [(167,(1,1),'k'),(252,(1,0),'r − k'),(337,(0,1),'s − k'),(422,(0,0),'1 − r − s + k')]:
        for x,bit,name in [(115,bits[0],'x'),(220,bits[1],'y')]:
            s.circle((x,y),17,GREEN if bit else 'white',GREEN if bit else MUTED,3)
            s.text(x,y+7,name,21,'white' if bit else INK,'middle')
        s.text(310,y+7,label,25,BLUE)
    s.text(295,505,'Заполненный кружок: выбранный корень',19,MUTED,'middle')
    s.text(295,547,'k = rs − h²  ⇒  h = √(rs − k) > 0',24,anchor='middle')
    s.text(890,66,'Блуждание с остановкой',27,anchor='middle',weight='bold')
    s.text(890,101,'Пример: вершина степени 2',20,MUTED,'middle')
    center=(890,246)
    for end in [(720,200),(1060,200)]:
        s.line(center,end,MUTED,3)
        s.circle(end,15,'white',MUTED,3)
        mid=((center[0]+end[0])/2,(center[1]+end[1])/2)
        s.arrow((mid[0]+(20 if end[0]<890 else -20),mid[1]+5),
                (mid[0]-(20 if end[0]<890 else -20),mid[1]-5))
        s.text(mid[0],mid[1]-29,'1/3',23,BLUE,'middle')
    s.circle(center,19,BLUE)
    s.text(890,253,'v',23,'white','middle')
    s.arrow((890,277),(890,349))
    s.text(922,319,'1/3',23,RED)
    s.circle((890,378),21,RED)
    s.text(890,385,'■',19,'white','middle')
    s.text(890,433,'Остановиться здесь',22,RED,'middle')
    s.text(890,500,'Kᵢⱼ = вероятность остановки в j',23,anchor='middle')
    s.text(890,537,'при старте из i, где i, j ∈ {x, y}',22,anchor='middle')
    s.save('Два вероятностных прочтения отклика.svg')


def ending_chain(s,u,rect,bend=False):
    points,cores,edges,active=geometry(u)
    centers=[sum(points[i] for i in c)/6 for c in cores]
    direction=centers[-1]-centers[-2]
    rotation=direction.conjugate()/abs(direction)
    points={i:z*rotation for i,z in points.items()}
    xmin,xmax=min(z.real for z in points.values()),max(z.real for z in points.values())
    ymin,ymax=min(z.imag for z in points.values()),max(z.imag for z in points.values())
    x,y,w,h=rect;scale=min(w/(xmax-xmin),h/(ymax-ymin))
    p={i:(x+w/2+(z.real-(xmin+xmax)/2)*scale,
          y+h/2-(z.imag-(ymin+ymax)/2)*scale) for i,z in points.items()}
    for j,c in enumerate(cores):s.polygon([p[i] for i in c], '#ffe5eb' if bend and j==1 else FILLS[2])
    for a,b in sorted(edges):s.line(p[a],p[b],MUTED,2)
    for j in range(len(cores)-1):
        a,b=sorted(set(cores[j])&set(cores[j+1]));s.line(p[a],p[b],BLUE,3)
    for i,q in p.items():s.circle(q,3,INK)
    a,b=active;s.line(p[a],p[b],GREEN,6)
    for i,name in zip(active,('x','y')):
        s.circle(p[i],5,'white',GREEN,2)
        s.text(p[i][0]+15,p[i][1]+6,name,20,GREEN)
    if bend:
        center=tuple(sum(p[i][j] for i in cores[1])/6 for j in (0,1))
        s.text(center[0],center[1]+6,'L',20,RED,'middle',weight='bold')


def attenuation():
    s=SVG(1200,1020,'Удалённый изгиб и точность отклика',
          'Две цепочки из семи ядер: SSSSSS и SLSSSS. Измерения на правом конце. '
          'Логарифмический график точных расстояний отклика для N от 3 до 14 и доказанной верхней границы.')
    s.text(600,40,'Один удалённый изгиб · измерения на правом конце',27,anchor='middle',weight='bold')
    s.text(36,112,'SSSSSS',22,BLUE,weight='bold')
    ending_chain(s,'S'*5,(225,72,820,105))
    s.text(36,258,'SLSSSS',22,RED,weight='bold')
    ending_chain(s,'L'+'S'*4,(225,200,820,145),True)
    s.text(600,381,'Общий прямой конец всё сильнее скрывает левую часть',23,MUTED,'middle')
    with plt.rc_context({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none','svg.hashsalt':'pmg-boundary-response'}):
        fig,ax=plt.subplots(figsize=(11.3,5.6),layout='constrained')
        rows=DATA['hidden_bend'];xs=[row['N'] for row in rows]
        ax.semilogy(xs,[float(F(row['entry_distance'])) for row in rows],'o-',color=BLUE,lw=2,
                    label='Точное расстояние откликов')
        ax.semilogy(xs,[float(F(row['upper_bound'])) for row in rows],'--',color=RED,lw=2,
                    label='Доказанная верхняя граница')
        ax.set_xlabel('Число шестиугольников N')
        ax.set_ylabel('Максимум |ΔKᵢⱼ|')
        ax.set_xticks(xs);ax.set_yticks([10.**(-k) for k in (4,8,12,16,20,24)])
        ax.grid(True,which='major',alpha=.25);ax.legend(loc='upper right',fontsize=13)
        ax.spines[['top','right']].set_visible(False)
        stream=StringIO();fig.savefig(stream,format='svg',metadata={'Date':None});plt.close(fig)
    root=ET.fromstring(stream.getvalue())
    root.set('x','35');root.set('y','415');root.set('width','1130');root.set('height','560')
    s.parts.append('\n'.join(line.rstrip() for line in ET.tostring(root,encoding='unicode').splitlines()))
    s.text(600,1000,'Точки вычислены рационально; десятичная шкала используется только на рисунке',18,MUTED,'middle')
    s.save('Удалённый изгиб и точность отклика.svg')


def outcomes():
    s=SVG(1200,670,'Результаты восстановления с погрешностью',
          'При известном ограничении N<=7 полный каталог содержит 365 отмеченных состояний. '
          'Округление отклика SLR до 14 знаков даёт единственного кандидата. Среднее откликов '
          'SSSSSS и SLSSSS допускает оба кода. Неопределённый сектор интервального алгоритма не доказывает неоднозначность.')
    s.text(600,43,'Что означает результат проверки неточных данных',28,anchor='middle',weight='bold')
    headers=['Один кандидат','Два кандидата','Нет заключения']
    colors=[GREEN,RED,BLUE]
    rows=[
        ['Полный поиск при N ≤ 7','Отклик SLR округлён','до 14 знаков после запятой','ε = 5 · 10⁻¹⁵','Совместим только SLR'],
        ['Полный поиск при N ≤ 7','Середина двух откликов','Радиус: половина расстояния','ε ≈ 1,23 · 10⁻¹¹','Совместимы SSSSSS и SLSSSS'],
        ['Интервальное снятие шагов','Интервал пересёк порог','или знак делителя не установлен','Проверка остановилась','Число кандидатов неизвестно']]
    for x,title,color,body in zip((20,415,810),headers,colors,rows):
        s.panel(x,80,370,515)
        s.text(x+185,125,title,27,color,'middle',weight='bold')
        s.text(x+185,174,body[0],18,MUTED,'middle')
        y=255
        for line in body[1:4]:
            s.text(x+185,y,line,19,anchor='middle');y+=43
        s.arrow((x+185,389),(x+185,436))
        if title=='Два кандидата':
            s.text(x+185,479,'SSSSSS  или  SLSSSS',22,color,'middle',weight='bold')
            s.text(x+185,526,'Доказана неоднозначность',19,color,'middle')
        elif title=='Один кандидат':
            s.text(x+185,479,'SLR',30,color,'middle',weight='bold')
            s.text(x+185,526,'Единственность в каталоге',19,color,'middle')
        else:
            s.text(x+185,479,'Нужна более точная проверка',18,color,'middle',weight='bold')
            s.text(x+185,526,'Неоднозначность не доказана',18,color,'middle')
    s.text(600,639,'Каждый найденный кандидат проверяется по исходным измерительным интервалам',22,anchor='middle')
    s.save('Результаты восстановления с погрешностью.svg')


if __name__=='__main__':
    dynamic_response();ordinary_resistance();electrical();probability();attenuation();outcomes()
    print('Wrote six boundary-response SVG figures')
