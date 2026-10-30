"""Generate the three C01 SVG figures with Python's standard library."""
from html import escape
from math import cos, sin, pi
from pathlib import Path

from verify_admissible_chains import cycle, hex_pair, validate, negative_cases

OUT = Path(__file__).resolve().parents[2] / 'pmg-library/ru/Цепи из ядер'
INK, MUTED, EDGE = '#172b43', '#52657a', '#52657a'
RED, BLUE, PURPLE = '#bc294b', '#196bb9', '#8953af'
FILLS = ['#fff0d7','#ddf4e9','#e2edff']


class SVG:
    def __init__(self,w,h,title,desc):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
                      f'<rect width="{w}" height="{h}" fill="white"/>',
                      '<g font-family="DejaVu Sans, Arial, sans-serif">']
    def text(self,x,y,t,size=20,color=INK,anchor='start',weight='normal'):
        self.parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(t)}</text>')
    def line(self,a,b,color=EDGE,width=3,dash=''):
        self.parts.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    def polygon(self,ps,fill):
        self.parts.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in ps)+f'" fill="{fill}"/>')
    def circle(self,p,r=5,fill=INK,stroke='none',width=2):
        self.parts.append(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
    def panel(self,x,y,w,h):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#f7f9fc" stroke="#dce4ed"/>')
    def arrow(self,a,b,color=INK,width=3):
        self.line(a,b,color,width)
        dx,dy = b[0]-a[0],b[1]-a[1]
        length = (dx*dx+dy*dy)**.5
        dx,dy = dx/length,dy/length
        self.polygon([b,(b[0]-12*dx+5*dy,b[1]-12*dy-5*dx),(b[0]-12*dx-5*dy,b[1]-12*dy+5*dx)],color)
    def save(self,name):
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/name).write_text('\n'.join(self.parts+['</g></svg>'])+'\n',encoding='utf-8')


def ring(cx,cy,r,n=6):
    return {i:(cx+r*cos(pi/3-i*2*pi/n),cy+r*sin(pi/3-i*2*pi/n)) for i in range(n)}


def reflect(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    t=((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)
    foot=(a[0]+t*dx,a[1]+t*dy)
    return 2*foot[0]-p[0],2*foot[1]-p[1]


def pair_positions(cx,cy,r,start):
    p=ring(cx,cy,r)
    for a,ids in [(0,[9,8,7,6]),(start,[13,12,11,10])]:
        for k,v in enumerate(ids,2):
            p[v]=reflect(p[(a+k)%6],p[a],p[(a+1)%6])
    return p


def draw_pair(s,cx,cy,r,start,labels=True,arrows=True):
    cores,joins=hex_pair(start)
    _,edges=validate(cores,joins)
    p=pair_positions(cx,cy,r,start)
    for i,core in enumerate(cores):
        s.polygon([p[v] for v in core],FILLS[i])
        center=tuple(sum(p[v][j] for v in core)/6 for j in [0,1])
        s.text(center[0],center[1]+7,'K'+str(i+1),23,anchor='middle',weight='bold')
    for a,b in edges:
        s.line(p[a],p[b])
    for sh,col in zip(joins,[RED,BLUE]):
        a,b=p[sh[0]],p[sh[1]]
        s.line(a,b,col,6)
        if arrows:
            q=lambda t:(a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]))
            s.arrow(q(.30),q(.72),col,3)
    for v,pt in p.items():
        s.circle(pt,4)
        if labels:
            if v<6:
                dx,dy=(pt[0]-cx)/r,(pt[1]-cy)/r
                s.text(pt[0]+15*dx,pt[1]+15*dy+5,str(v),17,anchor='middle')
            else:
                s.text(pt[0],pt[1]-10,str(v),15,anchor='middle')
    return p


def figures():
    s=SVG(1240,620,'Две сборки трёх шестиугольников','Два графа со швами 01 и 34 либо 01 и 23; одинаковая схема ядер P3, 14 вершин и 16 рёбер.')
    for x,start,name in [(20,3,'А. Противоположные швы'),(630,2,'Б. Швы через одно ребро')]:
        s.panel(x,20,590,580)
        s.text(x+24,60,name,24,weight='bold')
        draw_pair(s,x+295,280,70,start)
        s.text(x+295,465,f'Вход: (0, 1)     Выход: ({start}, {start+1})',19,anchor='middle')
        s.text(x+295,495,'Одинаковые номера отождествлены',17,MUTED,anchor='middle')
        yy=548
        for a,b in [(x+190,x+295),(x+295,x+400)]:
            s.line((a,yy),(b,yy),MUTED,2)
        for i,xx in enumerate([x+190,x+295,x+400],1):
            s.circle((xx,yy),17,'white',MUTED)
            s.text(xx,yy+6,str(i),18,anchor='middle')
        s.text(x+295,585,'Схема ядер: P₃;  s₁ = s₂ = 2',18,anchor='middle')
    s.save('Две сборки трёх шестиугольников.svg')

    s=SVG(1160,720,'Присоединение ядра и перенос активной границы','Общее ребро оставлено у старого фрагмента. Входные отметки снимаются после сборки, выход сохраняется. Вставка: изолированная входная вершина при шве на трёх вершинах.')
    for x,w in [(20,275),(325,275),(660,480)]:
        s.panel(x,20,w,330)
    s.text(40,60,'1. Собранная часть H',22,weight='bold')
    s.text(345,60,'2. Новый фрагмент K⁻',22,weight='bold')
    s.text(680,60,'3. После сочленения',22,weight='bold')
    old=[(65,140),(235,140),(235,260),(65,260)]
    s.polygon(old,FILLS[0])
    for a,b in zip(old,old[1:]+old[:1]):s.line(a,b)
    s.line(old[1],old[2],RED,6)
    for p in old:s.circle(p)
    s.text(245,136,'a',18,RED);s.text(245,279,'b',18,RED)
    s.text(155,310,'Активная граница B = {a, b}',17,anchor='middle')
    new=[(365,140),(555,140),(555,260),(365,260)]
    s.polygon(new,FILLS[2])
    for a,b in zip(new[:3],new[1:]):s.line(a,b)
    s.line(new[3],new[0],RED,2,'6 7')
    s.line(new[1],new[2],BLUE,6)
    for p in new:s.circle(p)
    for p,t,c in [(new[0],'a',RED),(new[3],'b',RED),(new[1],'c',BLUE),(new[2],'d',BLUE)]:s.text(p[0]-12,p[1]+(-13 if p[1]==140 else 24),t,18,c)
    s.text(463,310,'Копия ребра ab удалена',17,anchor='middle')
    s.arrow((605,200),(650,200),MUTED)
    final=[(720,140),(890,140),(1060,140),(1060,260),(890,260),(720,260)]
    s.polygon([final[k] for k in [0,1,4,5]],FILLS[0])
    s.polygon([final[k] for k in [1,2,3,4]],FILLS[2])
    for a,b in zip(final,final[1:]+final[:1]):s.line(a,b)
    s.line(final[1],final[4],EDGE,3)
    s.line(final[2],final[3],BLUE,6)
    for p in final:s.circle(p)
    s.text(878,126,'a',18,MUTED);s.text(878,285,'b',18,MUTED)
    s.text(1070,136,'c',18,BLUE);s.text(1070,279,'d',18,BLUE)
    s.text(900,310,'Новая активная граница C = {c, d}',17,anchor='middle')
    s.panel(20,380,1120,315)
    s.text(42,420,'Вставка: шов на трёх вершинах',23,weight='bold')
    p={'a':(110,470),'w':(110,540),'b':(110,610),'c':(230,470),'d':(290,540),'e':(230,610)}
    for a,b in [('a','c'),('c','d'),('d','e'),('e','b')]:s.line(p[a],p[b])
    s.line(p['a'],p['w'],RED,2,'6 7');s.line(p['w'],p['b'],RED,2,'6 7')
    s.circle(p['w'],16,'#ffe8ee')
    for v,pt in p.items():s.circle(pt);s.text(pt[0]+(12 if v in 'cde' else -19),pt[1]+6,v,18)
    s.text(360,482,'В K⁻ удалены рёбра aw и wb, но сохранены все 6 вершин.',21)
    s.text(360,526,'Вершина w изолирована в K⁻ и входит в его паспорт.',21)
    s.text(360,570,'В собранном графе она соединена рёбрами шва из H.',21)
    s.text(360,620,'Снять отметку границы ≠ удалить вершину.',22,weight='bold')
    s.text(50,670,'Пунктир: копии рёбер, исключённые из присоединяемого фрагмента.',17,MUTED)
    s.save('Присоединение ядра и перенос активной границы.svg')

    # The rejected models are the same explicitly checked models used by the verifier.
    assert len(negative_cases())==3
    s=SVG(1240,960,'Допустимая цепочка и нарушения условий','Допустимая цепочка; пересекающиеся швы; дополнительный контакт крайних ядер; несвязный шов из двух отдельных рёбер.')
    for x,y in [(20,20),(630,20),(20,490),(630,490)]:s.panel(x,y,590,450)
    s.text(44,60,'А. Допустимая цепочка',24,weight='bold')
    draw_pair(s,315,220,65,3,labels=False,arrows=False)
    s.text(315,392,'Швы не пересекаются по вершинам.',19,anchor='middle')
    s.text(315,425,'Несоседние ядра не имеют контактов.',19,anchor='middle')
    s.text(654,60,'Б. Два шва имеют общую вершину',24,weight='bold')
    p=ring(925,227,115)
    s.polygon(list(p.values()),FILLS[1])
    for a,b in cycle(list(range(6))):s.line(p[a],p[b])
    s.line(p[0],p[1],RED,6);s.line(p[1],p[2],BLUE,6)
    s.circle(p[1],15,'#ffe2e9',RED)
    for v,pt in p.items():s.circle(pt,4);s.text(pt[0]+(26 if v==1 else 15 if pt[0]>925 else -15),pt[1]+5,str(v),18,anchor='middle')
    s.text(925,392,'Показано среднее ядро: швы 01 и 12.',19,anchor='middle')
    s.text(925,425,'Вершина 1 принадлежит всем трём ядрам.',19,anchor='middle')
    s.text(44,530,'В. Дополнительный контакт',24,weight='bold')
    p=draw_pair(s,315,710,65,3,labels=False,arrows=False)
    a,b=p[7],p[12]
    top=min(a[1],b[1])-55
    s.parts.append(f'<path d="M {a[0]:.2f},{a[1]:.2f} C {a[0]:.2f},{top:.2f} {b[0]:.2f},{top:.2f} {b[0]:.2f},{b[1]:.2f}" fill="none" stroke="{PURPLE}" stroke-width="3" stroke-dasharray="7 6"/>')
    for pt,t in [(a,'7'),(b,'12')]:s.circle(pt,9,'white',PURPLE,3);s.text(pt[0]+(20 if t=='7' else -22),pt[1]+6,t,18,PURPLE,anchor='middle')
    s.text(315,865,'Дополнительно отождествить 7 и 12.',19,anchor='middle')
    s.text(315,902,'Тогда крайние ядра имеют общую вершину.',19,anchor='middle')
    s.text(654,530,'Г. Несвязный шов',24,weight='bold')
    for cx,ids in [(800,list(range(8))),(1050,[0,1,8,9,4,5,10,11])]:
        coords=ring(cx,705,90,8)
        pos={v:coords[i] for i,v in enumerate(ids)}
        s.polygon([pos[v] for v in ids],FILLS[0] if cx==800 else FILLS[2])
        for u,v in cycle(ids):s.line(pos[u],pos[v])
        for u,v in [(0,1),(4,5)]:s.line(pos[u],pos[v],RED,6)
        for v,pt in pos.items():
            s.circle(pt,4)
            if v in [0,1,4,5]:s.text(pt[0]+(16 if pt[0]>cx else -16),pt[1]+5,str(v),18,anchor='middle')
    s.text(925,843,'Одинаковые номера отождествляются.',19,anchor='middle')
    s.text(925,878,'Пересечение: два отдельных ребра 01 и 45.',19,anchor='middle')
    s.text(925,913,'Четыре общие вершины не образуют P₄.',19,anchor='middle')
    s.save('Допустимая цепочка и нарушения условий.svg')
    print('Generated 3 SVG figures.')


if __name__ == '__main__':
    figures()
