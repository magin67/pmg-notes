"""Reproduce the four SVG figures for the standard dual examples.
Run from any directory: python checks/dual/draw_typical.py
Uses only the Python standard library and verify_typical.py.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import cos, sin, pi
from html import escape
from verify_typical import matrix_data

DEST=Path(__file__).resolve().parents[2]/'pmg-library/ru/Дуальная полиформа'
BLUE='#176c9e'; RED='#b13a32'; INK='#263443'; GREY='#6a7684'
class SVG:
 def __init__(self,w,h,title,desc):
  self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
   f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
   f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
   '<g font-family="DejaVu Sans, Arial, sans-serif" fill="'+INK+'">']
 def text(self,x,y,t,size=18,color=INK,weight='normal',anchor='middle'):
  self.items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" fill="{color}" font-weight="{weight}">{escape(str(t))}</text>')
 def line(self,x1,y1,x2,y2,color=GREY,width=2,dash=False):
  extra=' stroke-dasharray="8 5"' if dash else ''
  self.items.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{width:.2f}"{extra}/>')
 def circle(self,x,y,label,r=16):
  self.items.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="1.8"/>')
  self.text(x,y+5,label,15)
 def rect(self,x,y,w,h,fill,stroke='#fff'):
  self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>')
 def graph(self,points,edges,dual=False,labels=False,r=16,label_positions=None,width_override=None):
  biggest=max((abs(c) for i,j,c in edges),default=1)
  texts=[]
  for i,j,c in edges:
   if not c: continue
   x1,y1=points[i];x2,y2=points[j]
   color=(BLUE if c>0 else RED) if dual else GREY
   width=width_override if width_override is not None else (1.5+2.4*float(abs(c)/biggest) if dual else 2.3)
   self.line(x1,y1,x2,y2,color,width,dual and c<0)
   if labels:
    t=.36 if abs(x2-x1)>50 and abs(y2-y1)>50 else .5
    x=x1+(x2-x1)*t;y=y1+(y2-y1)*t
    dx=x2-x1;dy=y2-y1;length=(dx*dx+dy*dy)**.5
    x+=12*dy/length;y-=12*dx/length
    if label_positions and (i,j) in label_positions:x,y=label_positions[i,j]
    value=str(c)
    texts.append((x,y,value,color))
  for x,y,value,color in texts:
   self.rect(x-7*len(value)/2-4,y-17,7*len(value)+8,22,'#fff')
   self.text(x,y,value,15,color)
  for i,(x,y) in enumerate(points):self.circle(x,y,i+1,r)
 def save(self,name):
  DEST.mkdir(parents=True,exist_ok=True)
  (DEST/name).write_text('\n'.join(self.items+['</g></svg>']))

def shift(points,cx,cy):return [(x+cx,y+cy) for x,y in points]
def ring(n,cx,cy,r):return [(cx+r*cos(-pi/2+2*pi*i/n),cy+r*sin(-pi/2+2*pi*i/n)) for i in range(n)]
def data(n,edges):return matrix_data(n,edges)[2]
def legend(s,x,y):
 s.line(x,y-5,x+34,y-5,BLUE,3);s.text(x+46,y,'положительная',15,anchor='start')
 s.line(x+220,y-5,x+254,y-5,RED,3,True);s.text(x+266,y,'отрицательная',15,anchor='start')

def simple():
 s=SVG(900,850,'Звезда и полный граф без ребра: прямые и дуальные связи','В двух строках сопоставлены исходные графы и все положительные дуальные веса. Вершины обозначены числами.')
 s.text(450,35,'ИЗМЕНЕНИЕ ВЕСОВ И НАБОРА СВЯЗЕЙ',21,weight='bold')
 s.text(220,80,'Исходный граф · веса 1',19);s.text(670,80,'Дуальные связи · точные веса',19)
 star=[(0,0),(-125,-90),(125,-90),(0,130)]
 E=[(0,i,1) for i in range(1,4)]
 s.text(450,120,'Звезда K₁,₃ · вершина 1 в центре',18)
 s.graph(shift(star,220,245),E)
 s.graph(shift(star,670,245),data(4,E),True,True,label_positions={(0,1):(610,212),(0,2):(730,212),(0,3):(670,309),(1,2):(670,142),(1,3):(574,281),(2,3):(766,281)})
 s.text(450,420,'Между листьями возникают связи веса 5/16',17,BLUE)
 sq=[(-110,-100),(110,-100),(110,100),(-110,100)]
 E=[(i,j,1) for i,j in combinations(range(4),2) if (i,j)!=(0,1)]
 s.text(450,485,'K₄ без ребра 12',18)
 s.graph(shift(sq,220,640),E)
 s.graph(shift(sq,670,640),data(4,E),True,True)
 s.text(450,805,'Отсутствующей исходной связи 12 соответствует дуальный вес 3/16',17,BLUE)
 s.save('Дуальные связи звезды и неполного графа.svg')

def cycles():
 s=SVG(1020,790,'Дуальные связи циклов C4, C5 и C6','Сверху исходные циклы, снизу их дуальные системы. Положительные связи синие сплошные, отрицательные красные штриховые, нулевые отсутствуют.')
 s.text(510,34,'ЦИКЛЫ: ПОЛОЖИТЕЛЬНЫЕ, НУЛЕВЫЕ И ОТРИЦАТЕЛЬНЫЕ ВЕСА',20,weight='bold')
 for n,cx in [(4,170),(5,510),(6,850)]:
  s.text(cx,80,'C'+str(n),23,weight='bold')
  E=[(i,(i+1)%n,1) for i in range(n)]
  s.graph(ring(n,cx,225,105),E)
  s.graph(ring(n,cx,525,105),data(n,E),True)
 s.text(510,385,'Дуальные связи',20,weight='bold')
 for cx,lines in [(170,['Расстояние 1: 1/16','Расстояние 2: 3/16']),
                  (510,['Расстояние 1: 0','Расстояние 2: 1/5']),
                  (850,['Расстояние 1: −5/72','Расстояние 2: 13/72','Расстояние 3: 19/72'])]:
  for k,t in enumerate(lines):s.text(cx,674+23*k,t,16,RED if '−' in t else INK)
 legend(s,275,770)
 s.save('Дуальные связи циклов.svg')

def wikipedia():
 s=SVG(960,555,'Граф из статьи о матрице Кирхгофа и его дуальные веса','Исходный граф на шести вершинах и таблица точных числителей 198 gamma. Десять пар имеют положительные веса, пять отрицательные.')
 s.text(480,35,'НЕОДНОРОДНЫЙ ГРАФ НА ШЕСТИ ВЕРШИНАХ',21,weight='bold')
 s.text(220,90,'Исходные связи · веса 1',19);s.text(710,90,'Числители 198 γᵢⱼ',19)
 E=[(0,1,1),(0,4,1),(1,2,1),(1,4,1),(2,3,1),(3,4,1),(3,5,1)]
 pts=shift([(-135,-50),(-30,-120),(100,-120),(100,30),(-30,30),(100,155)],210,265)
 s.graph(pts,E)
 pairs=data(6,E); weights={(i,j):int(c*198) for i,j,c in pairs}
 x0,y0,step=535,150,55
 for i in range(6):
  s.text(x0+i*step+step/2,y0-15,i+1,16)
  s.text(x0-20,y0+i*step+step/2+6,i+1,16)
  for j in range(6):
   if i==j: fill='#f0f2f5';value='·';col=GREY
   else:
    c=weights[tuple(sorted((i,j)))]
    fill='#e5f1f8' if c>0 else '#fbe9e6';value=str(c);col=BLUE if c>0 else RED
   s.rect(x0+j*step,y0+i*step,step,step,fill)
   s.text(x0+j*step+step/2,y0+i*step+step/2+6,value,17,col)
 s.text(220,490,'7 исходных рёбер · τ = 11',17)
 s.text(700,510,'10 положительных и 5 отрицательных пар',16)
 s.save('Дуальные связи графа из Википедии.svg')

def petersen():
 s=SVG(1110,510,'Граф Петерсена и два класса дуальных связей','Слева исходный граф, в центре его 15 отрицательных дуальных связей веса минус 3/100, справа 30 положительных связей веса 7/100.')
 s.text(555,35,'ПЕТЕРСЕН: ДВА КЛАССА ДУАЛЬНЫХ ВЕСОВ',22,weight='bold')
 E=[(i,(i+1)%5,1) for i in range(5)]+[(i,i+5,1) for i in range(5)]+[(i+5,(i+2)%5+5,1) for i in range(5)]
 ps=data(10,E)
 for cx,title,edges,dual in [(185,'Исходный граф',E,False),(555,'Отрицательные связи',[e for e in ps if e[2]<0],True),(925,'Положительные связи',[e for e in ps if e[2]>0],True)]:
  s.text(cx,90,title,19,weight='bold')
  pts=ring(5,cx,265,132)+ring(5,cx,265,57)
  s.graph(pts,edges,dual,r=14,width_override=(1.6 if cx==925 else 2.5))
 s.text(185,445,'15 рёбер · вес 1',18)
 s.text(555,445,'15 пар · вес −3/100',18,RED)
 s.text(925,445,'30 пар · вес 7/100',18,BLUE)
 s.text(555,488,'Две правые панели вместе задают первую дуальную форму',17)
 s.save('Дуальные связи графа Петерсена.svg')

if __name__=='__main__':
 simple();cycles();wikipedia();petersen()
 print('Written 4 SVG figures to',DEST)
