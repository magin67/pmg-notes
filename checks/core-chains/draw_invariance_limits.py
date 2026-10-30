"""Draw labelled constructions from the checked records; editable SVG."""
from pathlib import Path
import json

from draw_admissible_chains import SVG, INK, MUTED, RED, BLUE, PURPLE, FILLS, ring, reflect
from verify_admissible_chains import edge


def fit(points,x,y,w,h):
    x0=min(p[0] for p in points.values());x1=max(p[0] for p in points.values())
    y0=min(p[1] for p in points.values());y1=max(p[1] for p in points.values())
    scale=min(w/(x1-x0),h/(y1-y0))
    return {v:(x+w/2+(p[0]-(x0+x1)/2)*scale,y+h/2+(p[1]-(y0+y1)/2)*scale) for v,p in points.items()}


def hex_positions(rec):
    ps=ring(0,0,100)
    for seam in rec['attachments']:
        parent=rec['core_vertex_maps'][seam['parent']]
        child=rec['core_vertex_maps'][seam['child']]
        j=seam['parent_local'][0]
        a,b=ps[parent[j]],ps[parent[(j+1)%6]]
        for k,v in enumerate(child):
            p=reflect(ps[parent[(j+k)%6]],a,b)
            if v in ps:assert sum((p[i]-ps[v][i])**2 for i in (0,1))<1e-12
            ps[v]=p
    return ps


def draw_hex_tree(s,rec,x,y,w,h):
    ps=fit(hex_positions(rec),x,y,w,h)
    for i,core in enumerate(rec['core_vertex_maps']):
        s.polygon([ps[v] for v in core],FILLS[i%3])
        cx=sum(ps[v][0] for v in core)/6;cy=sum(ps[v][1] for v in core)/6
        s.text(cx,cy+7,'K'+str(i+1),23,anchor='middle',weight='bold')
    for a,b in rec['edges']:s.line(ps[a],ps[b],MUTED,2.5)
    for seam in rec['attachments']:
        for a,b in seam['common_edges']:s.line(ps[a],ps[b],BLUE,6)
    for p in ps.values():s.circle(p,3.3)


def numbered_graph(s,ps,es,first=(),second=(),radius=5):
    first=set(first);second=set(second)
    for a,b in es:
        color=RED if edge(a,b) in first else BLUE if edge(a,b) in second else MUTED
        s.line(ps[a],ps[b],color,5 if color in (RED,BLUE) else 2.5)
    for v,p in ps.items():
        s.circle(p,radius,'white',INK,1.8)
        s.text(p[0]+10,p[1]-10,str(v),20)


def main():
    data=json.loads(Path(__file__).with_name('invariance-limits-results.json').read_text(encoding='utf-8'))
    records={r['name']:r for r in data['graphs']}
    s=SVG(1280,650,'Путь и звезда из четырёх шестиугольников',
          'Одни и те же четыре циклических ядра и три однорёберных шва. Схема пути даёт 1189 деревьев, схема звезды 1188; точные радиусы также различны.')
    s.text(640,44,'Четыре C₆: положение швов или изменение схемы?',27,anchor='middle',weight='bold')
    for x,name,label in [(20,'hex4_path','Путь P₄'),(660,'hex4_star','Звезда K₁,₃')]:
        rec=records[name];s.panel(x,75,600,505)
        s.text(x+300,115,label,26,anchor='middle',weight='bold')
        draw_hex_tree(s,rec,x+35,145,530,290)
        s.text(x+300,488,'τ = '+str(rec['tau']),27,anchor='middle',weight='bold')
        s.text(x+300,536,'ρ = '+rec['rho'],23,anchor='middle')
    s.text(640,611,'В обоих графах: 18 вершин, 21 ребро; синим выделены общие рёбра',22,anchor='middle')
    s.save('Путь и звезда из четырёх циклов.svg')

    s=SVG(1180,530,'Два расположения несвязных швов',
          'Среднее ядро C12. Вход 01 и 45 одинаков. Выход в А равен 23 и 67, в Б равен 67 и 10-11. Вход и выход не пересекаются по вершинам.')
    s.text(590,42,'Одинаковые несвязные швы, разное взаимное расположение',26,anchor='middle',weight='bold')
    for x,label,out in [(20,'А',[2,3,6,7]),(610,'Б',[6,7,10,11])]:
        s.panel(x,70,550,405);cx=x+275;cy=276
        s.text(cx,106,'Конфигурация '+label,25,anchor='middle',weight='bold')
        ps=ring(cx,cy,125,12)
        first={edge(0,1),edge(4,5)};second={edge(*out[:2]),edge(*out[2:])}
        for i in range(12):
            e=edge(i,(i+1)%12);color=RED if e in first else BLUE if e in second else MUTED
            s.line(ps[e[0]],ps[e[1]],color,6 if color in (RED,BLUE) else 2.5)
        for i,p in ps.items():
            s.circle(p,4)
            s.text(cx+(p[0]-cx)*1.20,cy+(p[1]-cy)*1.20+7,str(i),20,anchor='middle')
        s.text(cx,457,'Выход: ('+', '.join(map(str,out))+')',21,BLUE,anchor='middle')
    s.text(590,510,'Вход в обеих конфигурациях: (0, 1, 4, 5)',22,RED,anchor='middle')
    s.save('Два несвязных шва в цикле.svg')

    s=SVG(1260,650,'Три пары непересекающихся рёбер куба',
          'Первый шов 01. Второй равен 23, 67 или 26. Индуцированные подграфы на концах швов имеют вид C4, 2K2 и P4, поэтому пары неэквивалентны.')
    s.text(630,43,'Куб: отдельные рёбра эквивалентны, пары швов различаются',26,anchor='middle',weight='bold')
    local={0:(65,210),1:(215,210),2:(215,340),3:(65,340),4:(120,140),5:(270,140),6:(270,270),7:(120,270)}
    for col,(name,out,label) in enumerate([('same_face',[2,3],'C₄'),('opposite',[6,7],'2K₂'),('skew',[2,6],'P₄')]):
        x=20+420*col;s.panel(x,75,400,530)
        s.text(x+200,111,'Швы 01 и '+''.join(map(str,out)),24,anchor='middle',weight='bold')
        ps={v:(x+p[0],p[1]) for v,p in local.items()}
        rec=records['cube_'+name]
        numbered_graph(s,ps,rec['templates'][0]['edges'],[edge(0,1)],[edge(*out)])
        s.text(x+200,395,'Подграф на концах швов',20,anchor='middle')
        if name=='same_face':small={0:(120,440),1:(280,440),2:(280,510),3:(120,510)}
        elif name=='opposite':small={0:(120,440),1:(280,440),6:(120,510),7:(280,510)}
        else:small={v:(70+85*i,475) for i,v in enumerate([0,1,2,6])}
        small={v:(x+p[0],p[1]) for v,p in small.items()}
        for a,b in rec['middle_boundary_induced_edges']:s.line(small[a],small[b],PURPLE,3)
        for v,p in small.items():
            s.circle(p,16,'white',PURPLE,2);s.text(p[0],p[1]+6,str(v),18,PURPLE,anchor='middle')
        s.text(x+200,553,label,25,PURPLE,anchor='middle',weight='bold')
        s.text(x+200,588,'τ = '+str(rec['tau']),23,anchor='middle')
    s.text(630,634,'Каждая сборка содержит три куба: 20 вершин и 34 ребра',22,anchor='middle')
    s.save('Пары рёберных швов куба.svg')

    s=SVG(1240,565,'Одинаковое остовное число и разные резистивные радиусы',
          'Граф А: C4 и C3 с общей вершиной 0. Граф Б: K2,3 с висячим ребром 05. Оба имеют шесть вершин, семь рёбер и 12 деревьев. Радиусы 77/144 и 7/12 различны.')
    s.text(620,43,'Одного остовного числа недостаточно для определения радиуса',26,anchor='middle',weight='bold')
    for x,key,title,local in [
        (20,'equal_tau_A','А. Два цикла в общей вершине',{0:(270,265),1:(100,265),2:(100,135),3:(270,135),4:(430,200),5:(430,340)}),
        (640,'equal_tau_B','Б. K₂,₃ и висячее ребро',{0:(130,235),1:(430,235),2:(280,135),3:(280,235),4:(280,340),5:(40,235)})]:
        rec=records[key];s.panel(x,75,580,425)
        s.text(x+290,112,title,23,anchor='middle',weight='bold')
        ps={v:(x+p[0],p[1]+25) for v,p in local.items()}
        numbered_graph(s,ps,rec['edges'],radius=6)
        s.text(x+290,417,'τ = '+str(rec['tau']),27,anchor='middle',weight='bold')
        s.text(x+290,466,'ρ = '+rec['rho'],27,PURPLE,anchor='middle',weight='bold')
    s.text(620,540,'В обоих графах: n = 6, |E| = 7; висячая вершина есть только в Б',22,anchor='middle')
    s.save('Одинаковое остовное число и разные радиусы.svg')


if __name__=='__main__':
    main()
