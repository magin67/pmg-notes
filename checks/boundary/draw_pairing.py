"""Three SVG figures for boundary pairing; Python standard library only.

Run: python checks/boundary/draw_pairing.py
The drawing primitives and colors are shared with the first note.
"""
from draw_forest_states import Drawing, INK, MUTED, TEAL, BLUE, GOLD, PURPLE


def curve(d, path, color, width=4):
    d.parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}"/>')


def two_paths():
    d = Drawing('Два пути и двухточечное спаривание',
                'Единичные пути a-x-b и a-y-b соединяются по одноимённым a,b; внутренние x,y различны. '
                'Получается цикл a-x-b-y-a. Только совместный выбор обоих путей целиком создаёт цикл. '
                'Полином равен (1+t)^4-t^4.',
                596, 'Общая граница B = {a, b}; все рёбра имеют разные метки и единичные веса.')
    for x, w in [(24,260),(350,260),(676,260)]:
        d.box(x,110,w,294)
    for cx, title in [(154,'Часть G₁'),(480,'Часть G₂'),(806,'Сочленение')]:
        d.text(cx,150,title,23,anchor='middle',weight='700')
    for cx, internal, color in [(154,'x',TEAL),(480,'y',BLUE)]:
        pts = [(cx-87,245),(cx,245),(cx+87,245)]
        d.line(pts[0],pts[1],color)
        d.line(pts[1],pts[2],color)
        for label,p in zip(['a',internal,'b'],pts):
            d.node(*p,label,boundary=label in 'ab')
        d.text(cx,331,'D = 1 + 2t',22,anchor='middle')
        d.text(cx,372,'S = t²',22,color,anchor='middle')
    d.text(317,253,'+',36,MUTED,'middle')
    d.text(643,253,'→',36,MUTED,'middle')
    a,x,b,y=(714,260),(806,205),(898,260),(806,315)
    d.line(a,x,TEAL); d.line(x,b,TEAL)
    d.line(a,y,BLUE); d.line(y,b,BLUE)
    for label,p in [('a',a),('x',x),('b',b)]:
        d.node(*p,label,boundary=label in 'ab')
    d.node(*y,'')
    d.text(y[0],y[1]+29,'y',18,anchor='middle')
    d.text(806,380,'Полный набор - цикл',18,PURPLE,'middle')
    d.text(480,454,'D₁D₂ + D₁S₂ + S₁D₂ = F₁F₂ − S₁S₂',26,anchor='middle')
    d.text(480,506,'F(t) = (1 + t)⁴ − t⁴ = 1 + 4t + 6t² + 4t³',25,anchor='middle')
    d.text(480,558,'Из 16 подмножеств рёбер допустимы 15; исключён только набор всех рёбер.',18,MUTED,'middle')
    return d.save('Два пути и двухточечное спаривание')


def compatibility_table():
    labels=['x|y|z','xy|z','xz|y','x|yz','xyz']
    C=[[1,1,1,1,1],[1,0,1,1,0],[1,1,0,1,0],[1,1,1,0,0],[1,0,0,0,0]]
    d=Drawing('Совместимость пяти трёхточечных состояний',
              'Матрица в порядке x|y|z, xy|z, xz|y, x|yz, xyz. Строки: 11111, 10110, 11010, '
              '11100, 10000. Единица означает лес, ноль означает цикл. Разные парные состояния '
              'совместимы; одинаковые парные состояния создают цикл.',
              622,'B = {x, y, z}; порядок строк и столбцов совпадает с порядком координат паспорта.')
    x0,y0,w,h=290,165,116,62
    for j,label in enumerate(labels):
        d.text(x0+(j+.5)*w,142,label,22,anchor='middle',weight='700')
    for i,label in enumerate(labels):
        d.text(255,y0+i*h+40,label,22,anchor='end',weight='700')
        for j,value in enumerate(C[i]):
            x,y=x0+j*w,y0+i*h
            d.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{("#d9eee8" if value else "#f2e8f5")}" stroke="white" stroke-width="3"/>')
            d.text(x+w/2,y+41,value,27,TEAL if value else PURPLE,'middle',weight='700')
    d.text(480,522,'1: объединение остаётся лесом;  0: объединение создаёт цикл',21,anchor='middle')
    d.text(480,567,'Разные парные связи дают дерево на границе; повторная связь даёт цикл.',18,MUTED,'middle')
    d.text(480,603,'Полностью соединённое состояние xyz совместимо только с x|y|z.',18,MUTED,'middle')
    return d.save('Совместимость пяти трёхточечных состояний')


def seam_edges():
    d=Drawing('Различимые копии и одно общее ребро',
              'Слева после отождествления a,b сохранены две единичные копии ребра: зелёная e1 и синяя e2. '
              'Их лесной полином 1+2t, обе сразу выбрать нельзя. Справа оставлено одно общее единичное ребро e, '
              'его полином 1+t. Суммирование параллельных весов дало бы ребро веса 2, а не 1.',
              488,'Соответствие вершин одинаково: a ↔ a, b ↔ b. Меняется правило учёта рёбер.')
    d.box(24,110,444,275);d.box(492,110,444,275)
    d.text(246,151,'Две разные метки',23,anchor='middle',weight='700')
    d.text(714,151,'Одна общая метка',23,anchor='middle',weight='700')
    curve(d,'M 112 253 Q 246 150 380 253',TEAL)
    curve(d,'M 112 253 Q 246 356 380 253',BLUE)
    for label,x in [('a',112),('b',380)]:
        d.node(x,253,label,boundary=True)
    d.text(246,186,'e₁: 1',19,TEAL,'middle')
    d.text(246,327,'e₂: 1',19,BLUE,'middle')
    d.text(246,369,'F(t) = 1 + 2t',24,anchor='middle')
    d.line((580,253),(848,253),TEAL)
    for label,x in [('a',580),('b',848)]:
        d.node(x,253,label,boundary=True)
    d.text(714,232,'e: 1',19,TEAL,'middle')
    d.text(714,369,'F(t) = 1 + t',24,anchor='middle')
    d.text(480,427,'Сумма проводимостей параллельных копий равна 2.',21,anchor='middle')
    d.text(480,466,'Для одного общего ребра его метку заранее назначают ровно одной части.',18,MUTED,'middle')
    return d.save('Различимые копии и одно общее ребро')


if __name__=='__main__':
    for draw in [two_paths,compatibility_table,seam_edges]:
        print(draw())
