"""Three SVG figures for the spanning layer and boundary resistance note.

Run: python checks/boundary/draw_spanning_geometry.py
Only the standard library and the first note's drawing primitives are required.
"""
from draw_forest_states import Drawing, MUTED, TEAL, BLUE, GOLD, PURPLE


def elimination_scale():
    d=Drawing('Граничный отклик P₅ и остовной масштаб',
              'Исходный единичный путь a-b-c-d-e имеет границу a,c,e, остовной коэффициент 1 '
              'и вес полностью разделённых рощ 4. После исключения b,d остаётся путь a-c-e '
              'с проводимостями 1/2 и 1/2 и остовным коэффициентом 1/4. '
              'Граничные резистенсы 2,2,4 сохраняются; масштаб 4 восстанавливает исходное число 1.',
              632,'Граница B = {a, c, e}; все исходные проводимости равны 1.')
    d.box(24,109,912,171)
    d.text(480,147,'Исходный путь: n = 5,  τ = 1',22,anchor='middle',weight='700')
    d.forest(100,215,760,15)
    d.text(480,258,'δ = 4: четыре рощи состояния a|c|e',20,TEAL,'middle')
    d.text(480,326,'↓',42,MUTED,'middle')
    d.text(525,315,'исключаем внутренние b, d',19,MUTED)
    d.box(24,350,912,171)
    d.text(480,389,'Эффективный путь на границе: n = 3,  τ = 1/4',22,anchor='middle',weight='700')
    ps=[(140,457),(480,457),(820,457)]
    d.line(ps[0],ps[1]);d.line(ps[1],ps[2])
    for label,p in zip('ace',ps):
        d.node(*p,label,boundary=True)
    for x in [310,650]:
        d.text(x,444,'1/2',20,TEAL,'middle')
    d.parts.append(f'<text x="480" y="500" font-size="20" fill="{MUTED}" text-anchor="middle">R<tspan baseline-shift="sub" font-size="14">ac</tspan> = 2;  R<tspan baseline-shift="sub" font-size="14">ce</tspan> = 2;  R<tspan baseline-shift="sub" font-size="14">ae</tspan> = 4 в обоих графах</text>')
    d.text(480,565,'τ(исходного графа) = δ · τ(эффективного графа) = 4 · 1/4 = 1',23,anchor='middle')
    d.text(480,608,'Исключение сохраняет граничную метрику, но требует отдельного остовного масштаба.',18,MUTED,'middle')
    return d.save('Граничный отклик P5 и остовной масштаб')


def two_paths():
    d=Drawing('Два P₅ и остовное сочленение',
              'Два единичных пути a-b1-c-d1-e и a-b2-c-d2-e отождествлены по a,c,e. '
              'Зелёные рёбра принадлежат первой части, синие второй. '
              'Получаются два четырёхцикла с общей вершиной c. Каждый даёт четыре дерева, всего 16. '
              'Грамиан результата равен половине грамиана одной части, а для остовного коэффициента берётся определитель суммы.',
              644,'Общая граница B = {a, c, e}; внутренние вершины различны, общих рёбер нет.')
    d.text(280,123,'G₁: a–b₁–c–d₁–e',22,TEAL,'middle')
    d.text(680,123,'G₂: a–b₂–c–d₂–e',22,BLUE,'middle')
    a,c,e=(120,270),(480,270),(840,270)
    for b,dd,color in [((300,187),(660,187),TEAL),((300,353),(660,353),BLUE)]:
        for p,q in [(a,b),(b,c),(c,dd),(dd,e)]:
            d.line(p,q,color)
    for label,p in [('a',a),('c',c),('e',e)]:
        d.node(*p,label,boundary=True)
    for label,p in [('b₁',(300,187)),('d₁',(660,187))]:
        d.node(*p,label)
    for label,p in [('b₂',(300,353)),('d₂',(660,353))]:
        d.node(*p,'')
        d.text(p[0],p[1]+30,label,18,anchor='middle')
    d.text(300,280,'C₄',23,MUTED,'middle')
    d.text(660,280,'C₄',23,MUTED,'middle')
    d.box(24,414,912,152)
    d.text(480,450,'По графу: 4 · 4 = 16 деревьев',23,anchor='middle')
    d.text(480,489,'По рощам: 1 · 4 + 4 · 1 + 2 · 2 + 2 · 2 = 16',23,anchor='middle')
    d.text(480,534,'По грамианам: τ₁τ₂ det(G₁ + G₂) = det(2G₁) = 16',23,anchor='middle')
    d.text(480,610,'Грамиан самого сочленения: G = G₁/2.  Все граничные резистенсы вдвое меньше.',19,PURPLE,'middle')
    return d.save('Два P5 и остовное сочленение')


def same_response():
    d=Drawing('Одинаковый отклик и разные лесные паспорта',
              'В обоих графах граница a,b, внутренние листья x,y присоединены к a, ребро ab единичное. '
              'В первом графе веса ax,ay равны 1,1; во втором 2,1/2. '
              'В обоих случаях tau=delta=R_ab=1 и совпадают все веса рощ. '
              'Полиномы разделённого состояния равны (1+t)^2 и (1+2t)(1+t/2), поэтому полные паспорта различаются.',
              646,'B = {a, b}; оба графа имеют четыре вершины и одну и ту же топологию.')
    for i,title in enumerate(['Граф A','Граф B']):
        x=24+468*i;cx=x+222
        d.box(x,108,444,377)
        d.text(cx,149,title,24,anchor='middle',weight='700')
        a,b,u,v=(x+211,274),(x+370,274),(x+78,215),(x+78,346)
        for p,q in [(a,b),(a,u),(a,v)]:
            d.line(p,q)
        for label,p in [('a',a),('b',b),('x',u)]:
            d.node(*p,label,boundary=label in 'ab')
        d.node(*v,'')
        d.text(v[0],v[1]+28,'y',18,anchor='middle')
        d.text(x+145,224,'1' if i==0 else '2',20,TEAL,'middle')
        d.text(x+145,340,'1' if i==0 else '1/2',20,TEAL,'middle')
        d.text(x+290,258,'1',20,TEAL,'middle')
        expression='(1 + t)²' if i==0 else '(1 + 2t)(1 + t/2)'
        d.parts.append(f'<text x="{cx}" y="416" font-size="22" fill="#203444" text-anchor="middle">F<tspan baseline-shift="sub" font-size="16">a|b</tspan>(t) = {expression}</text>')
        d.parts.append(f'<text x="{cx}" y="459" font-size="22" fill="#203444" text-anchor="middle">F<tspan baseline-shift="sub" font-size="16">ab</tspan>(t) = t · F<tspan baseline-shift="sub" font-size="16">a|b</tspan>(t)</text>')
    d.text(480,530,'В обоих графах резистенс между a и b равен 1;  τ = δ = 1',23,anchor='middle')
    d.text(480,570,'Все веса рощ совпадают; младшие лесные коэффициенты различны.',21,PURPLE,'middle')
    d.text(480,616,'Лист без выбранного ребра становится внутренней компонентой и не входит в рощу.',18,MUTED,'middle')
    return d.save('Одинаковый отклик и разные лесные паспорта')


if __name__=='__main__':
    for draw in [elimination_scale,two_paths,same_response]:
        print(draw())
