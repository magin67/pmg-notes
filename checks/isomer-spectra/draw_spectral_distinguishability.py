"""Three native SVG figures, with graph incidence checked independently."""
from pathlib import Path
import json
from draw_three_hexagons import SVG, INK, MUTED, BLUE, RED, GREEN
from draw_slr_code import draw_chain, geometry
from verify_slr_code import graph

DATA = json.loads(Path(__file__).with_name('spectral-distinguishability-results.json').read_text(encoding='utf-8'))


def checked_chain(s, u, box, highlight=False):
    pts, cores, edges, boundary = geometry(u)
    g, expected_cores, expected_boundary, _ = graph(u)
    assert cores == expected_cores and boundary == expected_boundary
    assert edges == {tuple(sorted(e)) for e in g.edges}
    assert min(abs(a-b) for i,a in pts.items() for j,b in pts.items() if i<j) > 1e-6
    p, centers = draw_chain(s, u, box)
    if highlight:
        seams = {tuple(sorted(set(a)&set(b))) for a,b in zip(cores,cores[1:])}
        for a,b in edges:
            if g.degree(a)==g.degree(b)==3 and (a,b) not in seams:
                s.line(p[a],p[b],RED,5)
        for v in g:
            if g.degree(v)==3:
                k=sum(g.degree(w)==3 for w in g[v])
                s.circle(p[v],7,RED if k==3 else 'white',RED,2.5)
    return g


def neighboring_turns():
    s=SVG(1200,640,'Шестой момент и соседние повороты',
          'SLL и SLR имеют по четыре ядра и два изгиба. У SLL одна пара LL, у SLR одинаковых соседних поворотов нет. Разность шестых моментов равна 6.')
    for x,u,h in [(20,'LL',1),(620,'LR',0)]:
        s.panel(x,20,560,520)
        s.text(x+280,64,'S'+u,30,anchor='middle',weight='bold')
        g=checked_chain(s,u,(x+55,90,450,290),True)
        assert sum(g.degree(v)==3 and all(g.degree(w)==3 for w in g[v]) for v in g)==h
        s.text(x+280,420,f'N = 4;   b = 2;   h = {h}',25,anchor='middle')
        row=next(r for r in DATA['short_catalog'] if r['code']=='S'+u)
        s.text(x+280,463,'s6 = '+str(row['traces'][5]),23,anchor='middle')
        s.text(x+280,505,'p6 = '+('1 882 609' if h else '1 882 610'),23,anchor='middle')
    s.text(600,585,'Одинаковое число изгибов; разное соседство поворотов',25,anchor='middle',weight='bold')
    s.text(600,622,'Δs6 = 6;   Δp6 = −1',24,RED,anchor='middle')
    s.save('Шестой момент и соседние повороты.svg')


def initial_coefficients():
    s=SVG(1200,930,'Совпадающие начала корневых полиномов',
          'Пара SSSL и SSLS различается в p8; пара SLSLL и SLLSR различается в p10. Предшествующие коэффициенты каждой пары совпадают.')
    for y,ua,ub,grade,b,h in [(20,'SSL','SLS',8,1,0),(480,'LSLL','LLSR',10,3,1)]:
        ex=DATA['examples']['S'+ua+' / S'+ub]
        assert not ex['isomorphic'] and ex['first_different_grade']==grade
        for x,u in [(20,ua),(620,ub)]:
            s.panel(x,y,560,330)
            s.text(x+280,y+38,'S'+u,28,anchor='middle',weight='bold')
            checked_chain(s,u,(x+35,y+60,490,210))
            s.text(x+280,y+309,f'N = {len(u)+2};   b = {b};   h = {h}',22,anchor='middle')
        s.text(100,y+374,'p0 = 1',19,MUTED)
        for j in range(1,grade+1):
            x=245+(j-1)*65
            s.parts.append(f'<rect x="{x}" y="{y+347}" width="55" height="38" rx="6" fill="{RED if j==grade else "#dce4ed"}"/>')
            s.text(x+27,y+373,'p'+str(j),19,'white' if j==grade else INK,'middle')
        s.text(600,y+423,f'p1, …, p{grade-1} совпадают; первая разность в p{grade}',22,anchor='middle')
    s.save('Совпадающие начала корневых полиномов.svg')


def data_levels():
    s=SVG(1200,550,'Данные для различения SLR-цепочек',
          'Полный отмеченный граничный вектор декодируется для любой длины. Различимость по полиному и по одному значению подтверждена до 18 ядер; общие утверждения остаются гипотезами.')
    cards=[(20,'Пять граничных чисел','z = (a, b, c, d, e)',GREEN,
            ['Ориентированное слово','с выбранной границей'],['Декодирование доказано','для любой длины']),
           (420,'Полный полином','χ(ξ)',BLUE,
            ['Класс графа','без граничных отметок'],['Проверено до 18 ядер','Общий случай: гипотеза 1']),
           (820,'Одно значение','P(1) = χ(−1)',BLUE,
            ['Класс графа','при известном N'],['Проверено до 18 ядер','Общий случай: гипотеза 2'])]
    for x,title,formula,color,meaning,status in cards:
        s.panel(x,20,360,385)
        s.text(x+180,65,title,24,anchor='middle',weight='bold')
        s.text(x+180,127,formula,26,color,'middle')
        for i,line in enumerate(meaning):s.text(x+180,187+i*32,line,21,anchor='middle')
        s.line((x+25,253),(x+335,253),'#dce4ed',2)
        for i,line in enumerate(status):s.text(x+180,300+i*35,line,20,color,'middle')
    s.text(600,453,'Отмеченное слово и неотмеченный класс графа - разные задачи',23,anchor='middle',weight='bold')
    s.text(600,500,'Доказательство для пяти чисел не доказывает инъективности одного числа',22,MUTED,'middle')
    s.save('Данные для различения SLR-цепочек.svg')


if __name__=='__main__':
    neighboring_turns();initial_coefficients();data_levels()
    print('PASS: three SVG figures and six independent graph-incidence checks')
