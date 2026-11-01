"""Four reproducible SLR illustrations; only the Python standard library is used."""
from math import cos, sin, pi, sqrt
from draw_three_hexagons import SVG, INK, MUTED, RED, BLUE, GREEN, FILLS

EXIT={'L':2,'S':3,'R':4}


def geometry(u):
    points={i:complex(cos(pi/6-i*pi/3),sin(pi/6-i*pi/3)) for i in range(6)}
    cores=[list(range(6))];active=(0,1);n=6
    for letter in u+'S':
        a,b=active;p0,p1=points[b],points[a]
        center=(p0+p1)/2-1j*(p1-p0)*sqrt(3)/2
        v=p0-center;core=[b,a]+list(range(n,n+4));n+=4
        for i in range(2,6):
            points[core[i]]=center+v*complex(cos(-i*pi/3),sin(-i*pi/3))
        cores.append(core);j=EXIT[letter];active=(core[j],core[j+1])
    edges={tuple(sorted((a,b))) for c in cores for a,b in zip(c,c[1:]+c[:1])}
    assert len(points)==4*len(cores)+2 and len(edges)==5*len(cores)+1
    return points,cores,edges,active


def draw_chain(s,u,rect,ends=False):
    points,cores,edges,active=geometry(u)
    x,y,w,h=rect
    xmin,xmax=min(z.real for z in points.values()),max(z.real for z in points.values())
    ymin,ymax=min(z.imag for z in points.values()),max(z.imag for z in points.values())
    scale=min(w/(xmax-xmin),h/(ymax-ymin))
    p={i:(x+w/2+(z.real-(xmin+xmax)/2)*scale,y+h/2-(z.imag-(ymin+ymax)/2)*scale)
        for i,z in points.items()}
    for k,c in enumerate(cores):
        s.polygon([p[i] for i in c],FILLS[k%3])
    for a,b in sorted(edges):s.line(p[a],p[b],MUTED,2.5)
    for k in range(len(cores)-1):
        seam=set(cores[k])&set(cores[k+1]);assert len(seam)==2
        a,b=sorted(seam);s.line(p[a],p[b],BLUE,4)
    for i,pt in p.items():s.circle(pt,3.3,INK)
    centers=[]
    for k,c in enumerate(cores):
        cx,cy=(sum(p[i][q] for i in c)/6 for q in [0,1]);centers.append((cx,cy))
        s.text(cx,cy+6,str(k+1),20,MUTED,'middle')
    if ends:
        for pair,color in [((3,4),RED),(active,GREEN)]:
            s.line(p[pair[0]],p[pair[1]],color,7)
            for i in pair:
                s.circle(p[i],7,'white',color,3)
                s.text(p[i][0]+(-23 if color==RED else 24),p[i][1]+7,str(i),22,color,'middle')
    return p,centers


def local_letters():
    s=SVG(1200,490,'Буквы SLR и порядок концов шва',
        'Все циклы обходятся по часовой стрелке. Новое ядро получает 0=b, 1=a. Выход 23 даёт левый поворот L, 34 — прямое продолжение S, 45 — правый поворот R.')
    for x,letter,j in [(20,'L',2),(420,'S',3),(820,'R',4)]:
        s.panel(x,20,360,450);cx,cy=x+190,242;r=95
        p={i:(cx+r*cos(7*pi/6-i*pi/3),cy-r*sin(7*pi/6-i*pi/3)) for i in range(6)}
        s.text(x+180,61,f'{letter} · выход ({j}, {j+1})',25,anchor='middle',weight='bold')
        s.polygon(list(p.values()),FILLS[1])
        for i in range(6):s.line(p[i],p[(i+1)%6],RED if i==0 else BLUE if i==j else MUTED,5 if i in [0,j] else 3)
        for i,pt in p.items():
            s.circle(pt,5,'white',INK)
            dx,dy=pt[0]-cx,pt[1]-cy
            label='0 = b' if i==0 else '1 = a' if i==1 else str(i)
            s.text(cx+1.34*dx,cy+1.24*dy+6,label,20,RED if i in [0,1] else INK,'middle')
        s.arrow((cx-51,cy),(cx-5,cy))
        mid=((p[j][0]+p[j+1][0])/2,(p[j][1]+p[j+1][1])/2)
        s.arrow((cx,cy),(cx+.68*(mid[0]-cx),cy+.68*(mid[1]-cy)))
        s.text(x+180,389,'0 → b, 1 → a',24,RED,'middle')
        s.text(x+180,434,{'L':'поворот влево','S':'прямое продолжение','R':'поворот вправо'}[letter],21,BLUE,'middle')
    s.save('Буквы SLR и порядок концов шва.svg')


def symmetry_orbit():
    s=SVG(1200,780,'Отражение и обращение SLR-кода',
        'Четыре записи одного абстрактного графа: SLS, SRS, SSR, SSL. Горизонтальная операция — отражение, вертикальная — обращение цепи. Цифры указывают выбранный порядок ядер.')
    for x,y,u,label in [(20,20,'LS','w = SLS'),(650,20,'RS','μ(w) = SRS'),
                          (20,430,'SR','ι(w) = SSR'),(650,430,'SL','μι(w) = SSL')]:
        s.panel(x,y,530,330)
        s.text(x+265,y+40,label,27,anchor='middle',weight='bold')
        draw_chain(s,u,(x+55,y+75,420,210))
        s.text(x+265,y+308,'чтение: 1 → 2 → 3 → 4',19,MUTED,'middle')
    for y in [180,590]:
        s.arrow((565,y),(635,y));s.text(600,y-20,'μ',27,BLUE,'middle')
    for x in [285,915]:
        s.arrow((x,363),(x,416));s.text(x+23,398,'ι',27,RED)
    s.save('Отражение и обращение SLR-кода.svg')


def four_classes():
    s=SVG(1200,700,'Четыре класса четырёх шестиугольников',
        'Канонические представители SSS, SSL, SLL, SLR при порядке S<L<R. Это четыре разных класса графов, а не четыре записи одного графа.')
    for x,y,u in [(20,20,'SS'),(620,20,'SL'),(20,365,'LL'),(620,365,'LR')]:
        s.panel(x,y,560,315)
        s.text(x+280,y+43,'S'+u,29,anchor='middle',weight='bold')
        draw_chain(s,u,(x+50,y+70,460,210))
    s.save('Четыре класса четырёх шестиугольников.svg')


def boundary_ends():
    s=SVG(1200,680,'Два конца одной SLR-цепи',
        'Один граф SLS, прочитанный с другого конца как SSR. Конечные пары 3,4 и 15,16 имеют разные нормированные спектральные паспорта, хотя первая координата P(1)=221771751 одинакова.')
    s.text(600,40,'Один граф · два выбора конечной границы',27,anchor='middle',weight='bold')
    draw_chain(s,'LS',(260,80,680,260),ends=True)
    s.text(600,388,'Общее значение P(1) = 221 771 751',27,anchor='middle',weight='bold')
    for x,title,color,rows in [(20,'SSR · левая пара (3, 4)',RED,
        ['−B = 98 976 277;  −C = 98 943 538','−D = 38 051 101;  E = 37 629 575']),
        (620,'SLS · правая пара (15, 16)',GREEN,
        ['−B = 98 986 375;  −C = 98 986 738','−D = 38 074 862;  E = 37 645 206'])]:
        s.panel(x,423,560,177)
        s.text(x+280,464,title,23,color,'middle','bold')
        for i,row in enumerate(rows):s.text(x+280,511+40*i,row,21,anchor='middle')
    s.text(600,645,'Все координаты взяты при ξ = −1; перестановки B и C недостаточно',22,MUTED,'middle')
    s.save('Два конца одной SLR-цепи.svg')


if __name__=='__main__':
    local_letters();symmetry_orbit();four_classes();boundary_ends()
