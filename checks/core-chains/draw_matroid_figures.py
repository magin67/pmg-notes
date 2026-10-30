"""Generate editable SVG figures for the configuration-invariance note."""
from math import hypot

from draw_admissible_chains import SVG, INK, MUTED, BLUE, PURPLE, FILLS, draw_pair
from verify_admissible_chains import hex_pair, validate


def bundle(s, a, b, count, color):
    dx, dy = b[0]-a[0], b[1]-a[1]
    length = hypot(dx, dy)
    for k in range(count):
        offset = (k-(count-1)/2)*35
        control = ((a[0]+b[0])/2-offset*dy/length,
                   (a[1]+b[1])/2+offset*dx/length)
        s.parts.append(f'<path d="M {a[0]} {a[1]} Q {control[0]:.2f} {control[1]:.2f} {b[0]} {b[1]}" '
                       f'fill="none" stroke="{color}" stroke-width="2.5"/>')


def main():
    s = SVG(1180,520,'Общий двойственный мультиграф трёх шестиугольников',
            'Вершины f1, f2, f3 отвечают граням ядер; f∞ отвечает внешней грани. '
            'Между соседними ядрами по одному ребру; к внешней грани ведут пучки из 5, 4 и 5 отдельных рёбер.')
    s.text(590,45,'Двойственный граф обеих конфигураций',27,anchor='middle',weight='bold')
    outer = (590,125)
    faces = [(175,365),(590,365),(1005,365)]
    for point, count in zip(faces,[5,4,5]):
        bundle(s,outer,point,count,MUTED)
    for a,b in zip(faces,faces[1:]):
        s.line(a,b,BLUE,4)
        s.text((a[0]+b[0])/2,344,'1 общее ребро',20,BLUE,anchor='middle')
    for x,y,label in [(300,220,'5 рёбер'),(665,245,'4 ребра'),(880,220,'5 рёбер')]:
        s.text(x,y,label,22,anchor='middle',weight='bold')
    for i,p in enumerate(faces,1):
        s.circle(p,30,FILLS[i-1],INK,2)
        s.text(p[0],p[1]+8,'f'+str(i),24,anchor='middle')
        s.text(p[0],426,'Грань ядра K'+str(i),20,anchor='middle')
    s.circle(outer,30,'white',INK,2)
    s.text(outer[0],outer[1]+7,'f∞',24,anchor='middle')
    s.text(590,82,'Внешняя грань',20,MUTED,anchor='middle')
    s.text(590,479,'Параллельные линии - отдельные рёбра; всего 4 вершины и 16 рёбер',21,anchor='middle')
    s.save('Общий двойственный мультиграф цепочек.svg')

    s = SVG(1240,750,'Неизоморфность двух цепочек по вершинам степени три',
            'У каждой цепочки четыре вершины степени 3. В конфигурации А они индуцируют два раздельных ребра 01 и 34; '
            'в конфигурации Б - путь 0-1-2-3 из трёх рёбер. Это препятствует изоморфизму графов.')
    for x,start,name in [(20,3,'А. Противоположные швы'),(630,2,'Б. Швы через одно ребро')]:
        s.panel(x,20,590,675)
        s.text(x+24,62,name,24,weight='bold')
        ps = draw_pair(s,x+295,270,66,start,arrows=False)
        cores,joins = hex_pair(start)
        vertices,edges = validate(cores,joins)
        selected = sorted(v for v in vertices if sum(v in e for e in edges) == 3)
        for v in selected:
            s.circle(ps[v],7,PURPLE,'white',1.5)
        induced = [e for e in edges if set(e) <= set(selected)]
        s.text(x+295,462,'Выделены четыре вершины степени 3',20,PURPLE,anchor='middle')
        s.arrow((x+295,484),(x+295,524),MUTED,2)
        s.text(x+295,558,'Индуцированный подграф',21,anchor='middle')
        small = {v:(x+130+110*i,600) for i,v in enumerate(selected)}
        for a,b in induced:
            s.line(small[a],small[b],PURPLE,4)
        for v,p in small.items():
            s.circle(p,18,'white',PURPLE,2)
            s.text(p[0],p[1]+7,str(v),21,PURPLE,anchor='middle')
        s.text(x+295,660,'2 раздельных ребра' if start == 3 else 'Путь из 3 рёбер',23,anchor='middle',weight='bold')
    s.text(620,732,'Изоморфизм сохраняет степени вершин и рёбра индуцированного подграфа',22,anchor='middle')
    s.save('Неизоморфность двух шестиугольных цепочек.svg')


if __name__ == '__main__':
    main()
