"""Draw three SVG figures for four-point forest-state reduction.

Run: python checks/boundary/draw_reduction.py
Uses the existing Drawing primitives and independently checked matrix data.
"""
from draw_forest_states import Drawing, INK, MUTED, TEAL, BLUE, GOLD, PURPLE, LIGHT
from verify_reduction import LABELS, H


def partitions_gallery():
    d = Drawing('Пятнадцать состояний четырёхточечной границы',
                'Все разбиения a,b,c,d в фиксированном циклическом порядке. '
                'Ранги распределены как 1,6,7,1. Единственное пересекающееся разбиение ac|bd '
                'выделено розовым. Цветные области являются блоками, а не рёбрами; '
                'в точке пересечения блоков вершины нет.',
                804, 'Циклический порядок a, b, c, d. Области обозначают блоки, а не рёбра графа.')
    labels = LABELS[:13] + [LABELS[14], LABELS[13]]
    for i, state in enumerate(labels):
        x, y = 20 + (i % 5) * 188, 106 + (i // 5) * 214
        cx = x + 86
        d.box(x, y, 174, 200, '#fff0f3' if state == 'ac|bd' else LIGHT)
        d.text(cx, y + 29, state, 18, anchor='middle', weight='700')
        pts = {'a': (cx-43,y+73), 'b': (cx+43,y+73),
               'c': (cx+43,y+141), 'd': (cx-43,y+141)}
        for block, color in zip(state.split('|'), ['#b8ded8','#c5d9f3','#f1d9af','#e0ccec']):
            ps = [pts[v] for v in block]
            if len(ps) >= 3:
                coords = ' '.join(f'{a},{b}' for a,b in ps)
                d.parts.append(f'<polygon points="{coords}" fill="{color}" stroke="{color}" stroke-width="20" stroke-linejoin="round"/>')
            elif len(ps) == 2:
                if state == 'ac|bd' and block == 'bd':
                    d.line(ps[0],ps[1],'#fff0f3',31)
                d.line(ps[0],ps[1],color,23)
            else:
                d.circle(*ps[0],13,fill=color,stroke=color)
        for label, (px,py) in pts.items():
            d.circle(px,py,5)
            d.text(px,py-15 if label in 'ab' else py+25,label,16,anchor='middle')
        d.text(cx,y+188,'исключаем, r = 2' if state == 'ac|bd' else f'r = {4-len(state.split("|"))}',
               15,PURPLE if state == 'ac|bd' else MUTED,'middle')
    d.text(480,776,'15 исходных состояний → 14 координат класса паспорта',24,anchor='middle')
    return d.save('Пятнадцать состояний четырёхточечной границы')


def matrix_blocks():
    d = Drawing('Сокращённая матрица: леса и остовные блоки',
                'Матрица совместимости четырнадцати непересекающихся состояний в порядке заметки. '
                'Синим выделены единицы при сумме рангов 3, зелёным единицы при меньшей сумме. '
                'При большей сумме рангов все элементы равны нулю. Размеры групп 1,6,6,1; '
                'побочные блоки 1,A,A transpose,1 невырождены. det A=8, det C=-64.',
                734, 'Порядок состояний соответствует формуле (4). Цветная клетка = 1; белая = 0.')
    ox,oy,cell = 101,168,31
    ranks = [0]+[1]*6+[2]*6+[3]
    for i,row in enumerate(H):
        for j,v in enumerate(row):
            fill = BLUE if v and ranks[i]+ranks[j]==3 else TEAL if v else 'white'
            d.parts.append(f'<rect x="{ox+j*cell}" y="{oy+i*cell}" width="{cell}" height="{cell}" fill="{fill}" stroke="#d7e0e8" stroke-width="0.7"/>')
    for start,size,r in [(0,1,0),(1,6,1),(7,6,2),(13,1,3)]:
        center = (start+size/2)*cell
        d.text(ox+center,oy-25,str(r),19,anchor='middle',weight='700')
        d.text(ox-22,oy+center+6,str(r),19,anchor='middle',weight='700')
    for b in [0,1,7,13,14]:
        d.line((ox+b*cell,oy),(ox+b*cell,oy+14*cell),INK,1.7)
        d.line((ox,oy+b*cell),(ox+14*cell,oy+b*cell),INK,1.7)
    d.text(ox,123,'Ранг столбца',18,MUTED)
    d.text(34,151,'Ранг',16,MUTED)
    d.text(34,173,'строки',16,MUTED)
    x=575
    d.box(x,168,357,124)
    d.text(x+20,203,'r + s < 3: лесные блоки',20,TEAL,weight='700')
    d.text(x+20,236,'Возможны несвязные леса.',17,MUTED)
    d.text(x+20,269,'Имеются и единицы, и нули.',17,MUTED)
    d.box(x,312,357,124)
    d.text(x+20,347,'r + s = 3: остовные блоки',20,BLUE,weight='700')
    d.text(x+20,380,'Совместимость означает',17,MUTED)
    d.text(x+20,413,'соединение всей границы.',17,MUTED)
    d.box(x,456,357,96)
    d.text(x+20,491,'r + s > 3: только нули',20,weight='700')
    d.text(x+20,524,'Новый цикл неизбежен.',17,MUTED)
    d.text(480,651,'det A = 8;  det сокращённой матрицы = −64 ≠ 0',24,anchor='middle')
    d.text(480,696,'Для k вершин побочная блочная диагональ задаётся условием r + s = k − 1.',18,MUTED,'middle')
    return d.save('Сокращённая лесная матрица и остовные блоки')


def crossing_example():
    d = Drawing('Сокращение пересекающегося состояния',
                'Граф G имеет четыре граничные вершины и единичные рёбра ac,bd; пересечение не является вершиной. '
                'Партнёр J добавляет только ab. Имена границы согласованы, общих рёбер нет. '
                'Сочленение является путём c-a-b-d, с лесным полиномом (1+t)^3. '
                'Удаление состояния ac|bd теряет t^2+t^3, тогда как линейная замена сохраняет полный ответ.',
                687, 'B = {a, b, c, d}; все веса равны 1. Отождествление по именам, общих рёбер нет.')
    d.box(24,109,430,281)
    d.text(239,145,'G: рёбра ac, bd',23,anchor='middle',weight='700')
    ps={'a':(126,207),'b':(352,207),'c':(352,309),'d':(126,309)}
    d.line(ps['a'],ps['c'],TEAL)
    d.line(ps['b'],ps['d'],LIGHT,11)
    d.line(ps['b'],ps['d'],TEAL)
    for label,p in ps.items():
        d.node(*p,'',boundary=True)
        d.text(p[0],p[1]-22 if label in 'ab' else p[1]+32,label,19,anchor='middle')
    d.text(239,372,'Здесь нет общей вершины рёбер.',17,MUTED,'middle')
    d.box(482,109,454,281)
    d.text(709,145,'G # J: путь c–a–b–d',23,anchor='middle',weight='700')
    p2=[(529,258),(649,258),(769,258),(889,258)]
    for i in range(3):
        d.line(p2[i],p2[i+1],BLUE if i==1 else TEAL)
    for label,p in zip('cabd',p2):
        d.node(*p,label,boundary=True)
    d.text(709,308,'Синее ребро ab добавляет J.',18,BLUE,'middle')
    d.text(709,362,'F(t) = (1 + t)³',25,anchor='middle')
    d.box(24,414,912,181)
    d.text(480,453,'Вклад t² · s(ac|bd) переносится в семь координат:',22,anchor='middle')
    d.text(480,492,'+t²:  abc|d,  abd|c,  acd|b,  a|bcd',23,TEAL,'middle')
    d.text(480,531,'−t²:  ab|cd,  ad|bc,  abcd',23,PURPLE,'middle')
    d.text(480,573,'Это линейные координаты, а не веса отдельных состояний.',19,MUTED,'middle')
    d.text(480,644,'Если просто удалить ac|bd, получится 1 + 3t + 2t² вместо (1 + t)³.',21,anchor='middle')
    return d.save('Сокращение пересекающегося состояния без потери лесов')


if __name__ == '__main__':
    for draw in [partitions_gallery,matrix_blocks,crossing_example]:
        print(draw())
