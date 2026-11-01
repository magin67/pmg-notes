"""Reproducible SVG figures for local and mixed SLR spectral differences."""
from math import cos, sin, pi
import json
from pathlib import Path
from draw_three_hexagons import SVG, INK, MUTED, RED, BLUE, GREEN, FILLS
from draw_slr_code import draw_chain, geometry

DATA=json.loads((Path(__file__).with_name('spectral-differences-results.json')).read_text(encoding='utf-8'))


def number(n):
    return f'{n:,}'.replace(',', ' ')


def changed_chain(s,u,rect,index):
    points,_=draw_chain(s,u,rect)
    _,cores,_,_=geometry(u)
    seam=set(cores[index+1])&set(cores[index+2])
    a,b=sorted(seam)
    s.line(points[a],points[b],RED,7)
    for v in (a,b): s.circle(points[v],5,'white',RED,2)


def one_seam():
    s=SVG(1200,820,'Один шов и две спектральные разности',
        'SS и SL различаются одним прямым продолжением или изгибом; SLL и SLR различаются направлением второго изгиба. Изменяемый шов красный; остальные синие.')
    for y,a,b,i,formula in [(20,'S','L',0,'χSS − χSL = q²'),
                            (410,'LL','LR',1,'χSLL − χSLR = −(ξ − 2)² q²')]:
        for x,u in [(20,a),(620,b)]:
            s.panel(x,y,560,350)
            s.text(x+280,y+39,'S'+u,28,anchor='middle',weight='bold')
            changed_chain(s,u,(x+60,y+65,440,205),i)
            value=DATA['P_at_one']['S'+u]
            s.text(x+280,y+310,'P(1) = '+number(value),23,MUTED,'middle')
        s.text(600,y+381,formula,26,BLUE,'middle','bold')
    s.save('Один шов и две спектральные разности.svg')


def two_combinations():
    s=SVG(1200,560,'Два сочетания в разности швов',
        'Префикс p даёт пятикоординатный паспорт. Матрица Q выделяет A−ξB+ξE и C−B. Правое продолжение даёт два коэффициента eta. Их скалярное произведение равно разности характеристических полиномов.')
    s.text(600,44,'Окружение фиксировано · меняется одна буква S ↔ L',28,anchor='middle',weight='bold')
    for x,w,title,lines in [(25,300,'Левый фрагмент p',['sₚ = M(p)s₁','Aₚ, Bₚ, Cₚ, Dₚ, Eₚ']),
                            (450,300,'Два сочетания',['Aₚ − ξBₚ + ξEₚ','Cₚ − Bₚ']),
                            (875,300,'Правый фрагмент v',['ℓᵥ = r M(v)','(η₁, η₂) = ℓᵥ P'])]:
        s.panel(x,115,w,198)
        s.text(x+w/2,158,title,24,anchor='middle',weight='bold')
        for i,line in enumerate(lines):s.text(x+w/2,218+49*i,line,24,BLUE if x==450 else MUTED,'middle')
    s.arrow((340,215),(432,215));s.text(384,192,'Q',28,BLUE,'middle')
    s.arrow((858,215),(767,215));s.text(812,192,'η',28,BLUE,'middle')
    s.arrow((600,332),(600,391))
    s.panel(120,413,960,105)
    s.text(600,456,'χ(SpSv) − χ(SpLv) = η₁(Aₚ − ξBₚ + ξEₚ) + η₂(Cₚ − Bₚ)',25,anchor='middle',weight='bold')
    s.text(600,493,'Два сочетания достаточны для этой разности; общий паспорт сохраняет пять координат',21,MUTED,'middle')
    s.save('Два сочетания в разности швов.svg')


def mixed():
    s=SVG(1200,820,'Две смешанные разности SLR',
        'Обе суммы начинаются с chi SSS минус chi SSL минус chi SLS. При обычных S/L выборах четвёртый член SLL; с дополнительной перестановкой границы SLR. При xi=-1 суммы равны -102487 и 29282.')
    s.text(600,40,'Три общих члена · два разных завершения суммы',27,anchor='middle',weight='bold')
    for x,u,sign in [(20,'SS','+'),(420,'SL','−'),(820,'LS','−')]:
        s.panel(x,70,360,290)
        s.text(x+180,109,sign+' χ(S'+u+')',27,anchor='middle',weight='bold')
        draw_chain(s,u,(x+40,135,280,145))
        s.text(x+180,330,'P(1) = '+number(DATA['P_at_one']['S'+u]),21,MUTED,'middle')
    for x in (300,900):s.arrow((600,378),(x,423))
    for x,u,title,color,total in [(20,'LL','Обычные выборы S/L',BLUE,-102487),
                                (620,'LR','С перестановкой границы',RED,29282)]:
        s.panel(x,440,560,355)
        s.text(x+280,477,title,25,color,'middle','bold')
        s.text(x+280,514,'+ χ(S'+u+')',26,anchor='middle',weight='bold')
        draw_chain(s,u,(x+75,530,410,156))
        s.text(x+280,726,'P(1) = '+number(DATA['P_at_one']['S'+u]),22,MUTED,'middle')
        s.text(x+280,770,'Сумма при ξ = −1: '+number(total),26,color,'middle','bold')
    assert DATA['P_at_one']['SSS']-DATA['P_at_one']['SSL']-DATA['P_at_one']['SLS']+DATA['P_at_one']['SLL']==-102487
    assert DATA['P_at_one']['SSS']-DATA['P_at_one']['SSL']-DATA['P_at_one']['SLS']+DATA['P_at_one']['SLR']==29282
    s.save('Две смешанные разности SLR.svg')


def bend_coefficient():
    s=SVG(1200,500,'Изгиб и четвёртый корневой коэффициент',
        'У промежуточного ядра концы двух швов имеют степень три. При противоположных швах S между ними нет дополнительного ребра. При L или R есть ровно одно такое ребро; число m33 равно N−1+b.')
    for x,letter,j in [(20,'L',2),(420,'S',3),(820,'R',4)]:
        s.panel(x,20,360,390);cx,cy=x+180,210;radius=87
        points={i:(cx+radius*cos(7*pi/6-i*pi/3),cy-radius*sin(7*pi/6-i*pi/3)) for i in range(6)}
        marked={0,1,j,j+1}
        s.text(cx,62,letter,30,anchor='middle',weight='bold')
        s.polygon(list(points.values()),FILLS[1])
        for i in range(6):
            k=(i+1)%6
            color=RED if i in (0,j) else BLUE if i in marked and k in marked else MUTED
            s.line(points[i],points[k],color,6 if color!=MUTED else 3)
        for i,p in points.items():
            s.circle(p,7,'white',RED if i in marked else MUTED,3)
            s.text(cx+1.3*(p[0]-cx),cy+1.28*(p[1]-cy)+7,'3' if i in marked else '2',23,RED if i in marked else MUTED,'middle')
        s.text(cx,369,'Добавочное ребро: '+('0' if letter=='S' else '1'),23,BLUE,'middle')
    s.text(600,451,'Красные рёбра — швы; синее — добавочное; числа у вершин — степени в цепочке',22,MUTED,'middle')
    s.text(320,486,'m₃₃ = N − 1 + b',25,anchor='middle',weight='bold')
    s.text(850,486,'tr(L⁴) = 648N − 228 + 4b',25,anchor='middle',weight='bold')
    s.save('Изгиб и четвёртый корневой коэффициент.svg')


if __name__=='__main__':
    one_seam();two_combinations();mixed();bend_coefficient()
