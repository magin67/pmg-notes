"""Generate bilingual, repository-native SVG illustrations for Balanced Graphs."""
from pathlib import Path
import argparse,math,html,re

FIGS={
 'route':('Маршруты серии о балграфах','Routes through Balanced Graphs'),
 'circulation':('Диагональ в циркуляции и лапласиане','A Diagonal in Circulation and the Laplacian'),
 'oneway':('Односторонние резистенсы и циркуляция','One-Way Resistances and Circulation'),
 'projections':('Три проекции вершины орцикла','Three Projections of a Cycle Vertex'),
 'sphere':('Сфера балграфа и три положения центров','The Balanced Sphere and Three Center Positions'),
 'trees':('Деревья к корню и от корня','Trees toward and away from a Root'),
 'balance':('Балансировка исходящих весов','Balancing Outgoing Weights'),
 'mixed':('Смешанный лес двух орциклов','A Mixed Forest of Two Directed Cycles'),
 'factors':('Два графа перестановок на общих вершинах','Two Permutation Digraphs on Shared Vertices'),
 'repair':('Балграф с различными координатами сферы','A Balanced Graph with Different Sphere Coordinates')
}
DIRS={'ru':'pmg-library/ru/Направленные графы и расширения/Балансовые графы','en':'pmg-library/en/Directed Graphs and Extensions/Balanced graphs'}
C={'ink':'#20344a','blue':'#28638c','orange':'#b45920','green':'#178071','gray':'#9ba8b5','purple':'#7e549b'}
def tr(lang,ru,en):return ru if lang=='ru' else en
class SVG:
    def __init__(self,title,height=520):
        self.h=height;self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(title)}. See the accompanying caption for the mathematical interpretation.</desc>','<defs>']
        for name,color in C.items():self.items.append(f'<marker id="{name}" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L14 7 L0 14 Z" fill="{color}"/></marker>')
        self.items+=['</defs>',f'<rect width="1120" height="{height}" rx="12" fill="white"/>','<g font-family="Arial, DejaVu Sans, sans-serif">']
        self.text(560,42,title,size=25,bold=True)
    def text(self,x,y,value,size=21,color='ink',bold=False,anchor='middle',halo=False):
        value=re.sub(r'([A-Za-zα-ωΑ-Ω])_([a-z]+)',r'\1<tspan baseline-shift="sub" font-size="70%">\2</tspan>',html.escape(str(value)))
        self.items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{C.get(color,color)}" text-anchor="{anchor}"'+(' font-weight="bold"' if bold else '')+(' paint-order="stroke" stroke="white" stroke-width="4" stroke-linejoin="round"' if halo else '')+'>'+value+'</text>')
    def line(self,a,b,color='ink',dash=False,arrow=False,width=3):
        self.items.append(f'<path d="M{a[0]:.2f} {a[1]:.2f} L{b[0]:.2f} {b[1]:.2f}" fill="none" stroke="{C[color]}" stroke-width="{width}"'+(' stroke-dasharray="7 5"' if dash else '')+(f' marker-end="url(#{color})"' if arrow else '')+'/>')
    def panel(self,x,y,w,h,title=None):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f7f9fc" stroke="#dce4ec"/>')
        if title:self.text(x+w/2,y+32,title,size=22,bold=True)
    def dot(self,pos,label,root=False,color='ink',r=23):
        self.items.append(f'<circle cx="{pos[0]:.2f}" cy="{pos[1]:.2f}" r="{r}" fill="'+('#fff1c2' if root else 'white')+f'" stroke="{C[color]}" stroke-width="2.3"/>')
        self.text(pos[0],pos[1]+7,label,size=24,color=color)
    def point(self,pos,color='blue',r=6):
        self.items.append(f'<circle cx="{pos[0]:.2f}" cy="{pos[1]:.2f}" r="{r}" fill="{C[color]}"/>')
    def arc(self,a,b,weight=None,color='blue',curve=0,dash=False):
        dx,dy=b[0]-a[0],b[1]-a[1];d=math.hypot(dx,dy);ux,uy=dx/d,dy/d;nx,ny=-uy,ux
        # Every tip lies beyond the painted vertex disk.
        start=(a[0]+31*ux+curve*.15*nx,a[1]+31*uy+curve*.15*ny)
        end=(b[0]-31*ux+curve*.15*nx,b[1]-31*uy+curve*.15*ny)
        control=((a[0]+b[0])/2+curve*nx,(a[1]+b[1])/2+curve*ny)
        self.items.append(f'<path d="M{start[0]:.2f} {start[1]:.2f} Q{control[0]:.2f} {control[1]:.2f} {end[0]:.2f} {end[1]:.2f}" fill="none" stroke="{C[color]}" stroke-width="3" marker-end="url(#{color})"'+(' stroke-dasharray="7 5"' if dash else '')+'/>')
        if weight is not None:
            offset=curve*.65+17
            self.text((a[0]+b[0])/2+offset*nx,(a[1]+b[1])/2+offset*ny+6,weight,size=20,color=color,halo=True)
    def graph(self,pos,edges,roots=()):
        for edge in edges:
            a,b,*opts=edge;kw=opts[0] if opts else {};self.arc(pos[a],pos[b],**kw)
        for a,p in pos.items():self.dot(p,a,root=a in roots)
    def save(self,path):
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text('\n'.join(self.items+['</g></svg>'])+'\n',encoding='utf-8')

def route(lang):
    s=SVG(tr(lang,'Как читать серию о балграфах','Reading the balanced-graph series'),620)
    boxes=[(20,90,240,100,['1',tr(lang,'Баланс и деревья','Balance and trees')]),(300,90,240,100,['2–3',tr(lang,'Формы и экспонента','Forms and exponential')]),(580,90,240,100,['4',tr(lang,'Форма циркуляции','Circulation form')]),(860,90,240,100,['5',tr(lang,'Основные вариации','Basic variations')]),(20,300,240,100,['10',tr(lang,'Балансировка','Balancing')]),(300,300,240,100,['11',tr(lang,'Леса и топономы','Forests and toponomes')]),(580,300,240,100,['6–9',tr(lang,'Метрика и сфера','Metric and sphere')]),(860,300,240,100,['5',tr(lang,'Одна дуга и проекции','One arc and projections')]),(20,480,240,100,['12',tr(lang,'Перестановки','Permutations')])]
    for x,y,w,h,lines in boxes:
        s.panel(x,y,w,h);s.text(x+w/2,y+35,lines[0],bold=True,color='blue');s.text(x+w/2,y+70,lines[1],size=19)
    for x in [260,540,820]:s.line((x+3,140),(x+34,140),arrow=True)
    s.line((140,190),(140,295),arrow=True)
    s.line((140,240),(280,240),color='gray');s.line((280,240),(280,530),color='gray');s.line((280,530),(264,530),color='gray',arrow=True)
    s.line((420,190),(420,295),arrow=True)
    s.line((980,190),(705,295),arrow=True)
    s.line((825,350),(855,350),arrow=True)
    s.text(700,490,tr(lang,'К метрическому продолжению вариаций','Return to the metric continuation of variations'),size=20)
    s.text(700,523,tr(lang,'возвращаемся после определения сопряжения.','after the directional pairing has been defined.'),size=20)
    return s

def circulation(lang):
    s=SVG(tr(lang,'Что происходит с диагональю','What happens to the diagonal'),550)
    for j,title in enumerate(['L(abc)','L(acd)','L(abc) + L(acd)']):
        x=20+j*370;s.panel(x,75,340,370,title)
        p={'a':(x+70,165),'b':(x+270,165),'c':(x+270,365),'d':(x+70,365)}
        arcs=[('a','b'),('b','c'),('c','a')] if j==0 else [('a','c'),('c','d'),('d','a')] if j==1 else [('a','b'),('b','c'),('c','d'),('d','a'),('a','c'),('c','a')]
        edges=[(a,b,{'color':'orange' if {a,b}=={'a','c'} else 'blue','curve':22 if j==2 and {a,b}=={'a','c'} else 0}) for a,b in arcs]
        s.graph(p,edges)
    s.text(560,485,'w(abc) + w(acd) = w(abcd)',bold=True,color='blue')
    s.text(560,522,'L(abc) + L(acd) = L(abcd) + [(ac)]²',bold=True,color='orange')
    return s

def oneway(lang):
    s=SVG(tr(lang,'Одна пара не определяет циркуляцию','One pair does not determine circulation'),650)
    s.panel(20,80,530,520,tr(lang,'Единичный направленный цикл','Unit directed cycle'))
    s.panel(570,80,530,520,tr(lang,'Ненаправленный путь','Undirected path'))
    p={'a':(280,170),'b':(130,355),'c':(430,355)}
    s.graph(p,[(a,b,{'weight':1}) for a,b in [('a','b'),('b','c'),('c','a')]])
    p={'a':(660,270),'b':(835,270),'c':(1010,270)}
    for a,b in [('a','b'),('b','c')]:s.line(p[a],p[b],color='blue');s.text((p[a][0]+p[b][0])/2,245,'1')
    for a,v in p.items():s.dot(v,a)
    for x in [285,835]:
        s.text(x,430,'r_ab = 1/3;  r_ba = 2/3',bold=True);s.text(x,465,'R_ab = r_ab + r_ba = 1')
    s.text(285,515,'abc: 1;  acb: 2');s.text(835,515,'abc: 2;  acb: 2')
    s.text(285,562,'χ_abc = −1',color='orange',bold=True);s.text(835,562,'χ_abc = 0',color='green',bold=True)
    s.text(560,631,tr(lang,'Внизу сравниваются суммы r вдоль двух замкнутых обходов.','The bottom rows compare sums of r along the two closed traversals.'),size=20)
    return s

def projections(lang):
    s=SVG(tr(lang,'Две направленные проекции и евклидова','Two directional projections and the Euclidean one'),500)
    titles=[tr(lang,'Входящая','Incoming'),tr(lang,'Исходящая','Outgoing'),tr(lang,'Симметричная метрика g','Symmetric metric g')]
    colors=['orange','green','purple']
    for j in range(3):
        x=20+370*j;s.panel(x,80,340,370,titles[j]);p={'a':(x+55,340),'b':(x+285,340),'c':(x+170,340-230*math.sqrt(3)/2)}
        for a,b in [('a','b'),('b','c'),('c','a')]:s.line(p[a],p[b],color='gray',width=2)
        foot=p['a'] if j==0 else p['b'] if j==1 else(x+170,340)
        ca=p['c'];dx,dy=foot[0]-ca[0],foot[1]-ca[1];d=math.hypot(dx,dy)
        start=(ca[0]+30*dx/d,ca[1]+30*dy/d);end=(foot[0]-28*dx/d,foot[1]-28*dy/d) if j<2 else foot
        s.line(start,end,color=colors[j],dash=True,arrow=True)
        for a,v in p.items():s.dot(v,a)
        if j==2:
            s.point(foot,'purple');s.line((foot[0],324),(foot[0]+16,324),color='purple',width=2);s.line((foot[0]+16,324),(foot[0]+16,340),color='purple',width=2)
        s.text(x+170,405,['θ_in = 0: a','θ_out = 1: b','θ_g = 1/2'][j],color=colors[j],bold=True)
    s.text(560,482,'θ_g = (θ_out + θ_in)/2;   θ_in − θ_out = χ_abc / R_ab = −1',size=21)
    return s

def sphere(lang):
    s=SVG(tr(lang,'Одна окружность и три положения центров','One circle and three center positions'),710)
    s.panel(20,80,520,500,tr(lang,'Евклидова реализация','Euclidean realization'))
    s.panel(580,80,520,500,tr(lang,'Увеличенный фрагмент','Enlarged view'))
    v={'a':(0,0),'b':(math.sqrt(.5),0),'c':(math.sqrt(.5)/2,math.sqrt(7/8))}
    bary={'out':(1/3,1/4,5/12),'in':(1/4,1/3,5/12),'g':(2/7,2/7,3/7)}
    ctr={key:tuple(sum(co[i]*list(v.values())[i][axis] for i in range(3)) for axis in (0,1)) for key,co in bary.items()}
    draw=lambda p:(150+330*p[0],450-330*p[1]);gc=draw(ctr['g']);radius=330*math.sqrt(2/7)
    s.items.append(f'<circle cx="{gc[0]:.3f}" cy="{gc[1]:.3f}" r="{radius:.3f}" fill="none" stroke="#7e549b" stroke-width="2.5"/>')
    for a,b in [('a','b'),('b','c'),('c','a')]:s.line(draw(v[a]),draw(v[b]),color='gray',width=2)
    for name,p in v.items():
        pp=draw(p);s.point(pp,'ink',5);s.text(pp[0]+(-18 if name=='a' else 18),pp[1]+(7 if name=='c' else 25),name,size=23)
    for key,col in [('out','orange'),('in','green'),('g','purple')]:s.point(draw(ctr[key]),col,4)
    s.items.append(f'<circle cx="{gc[0]:.3f}" cy="{gc[1]:.3f}" r="25" fill="none" stroke="#9ba8b5" stroke-dasharray="5 4"/>')
    s.line((gc[0]+25,gc[1]),(600,290),color='gray',dash=True)
    for key,col in [('out','orange'),('in','green'),('g','purple')]:
        p=(840+3300*(ctr[key][0]-ctr['g'][0]),280-3300*(ctr[key][1]-ctr['g'][1]))
        s.point(p,col,7);s.text(p[0],p[1]+(-22 if key=='g' else 35),'p_'+key,color=col,bold=True)
    s.text(280,535,'R_g² = 2/7',bold=True,color='purple')
    s.text(840,430,tr(lang,'Только p_g - центр окружности','Only p_g is the circle center'),size=21,bold=True,color='purple')
    s.text(840,474,'ρ = 41/144 ≠ R_g²',size=23,bold=True)
    s.text(560,624,'p_out: (4, 3, 5)/12;    p_in: (3, 4, 5)/12;    p_g: (2, 2, 3)/7',size=22)
    s.text(560,666,tr(lang,'Внизу указаны вершинные коэффициенты; направление z на рисунке исключено.','The bottom row gives vertex coefficients; the z direction is removed in the drawing.'),size=19)
    return s

def trees(lang):
    s=SVG(tr(lang,'Остовные деревья с одним корнем a','Spanning trees with the same root a'),490)
    for j,title in enumerate([tr(lang,'К корню','Toward the root'),tr(lang,'От корня','Away from the root')]):
        x=20+560*j;s.panel(x,80,520,355,title)
        p={'a':(x+260,160),'b':(x+100,340),'c':(x+420,340)}
        edges=[('b','a',{'weight':1}),('c','a',{'weight':1})] if j==0 else [('a','b',{'weight':2,'color':'orange'}),('b','c',{'weight':1,'color':'orange'})]
        s.graph(p,edges,roots=['a']);s.text(x+260,405,tr(lang,'Вес дерева = ','Tree weight = ')+str(j+1),bold=True)
    s.text(560,470,tr(lang,'Показано по одному дереву из двух взвешенных семейств.','One tree from each of the two weighted families is shown.'),size=21)
    return s

def balance(lang):
    s=SVG(tr(lang,'Масштабирование всех дуг одного источника','Scaling every arc from the same source'),680)
    arcs=[('a','b',1),('a','c',2),('b','a',2),('b','c',1),('c','a',1),('c','b',1)];cols={'a':'blue','b':'orange','c':'green'};fac={'a':15,'b':12,'c':21}
    for j,title in enumerate([tr(lang,'До балансировки','Before balancing'),tr(lang,'После балансировки','After balancing')]):
        x=20+560*j;s.panel(x,80,520,500,title);p={'a':(x+260,180),'b':(x+105,385),'c':(x+415,385)}
        s.graph(p,[(a,b,{'weight':str(w) if j==0 else f'{w*fac[a]}/16','color':cols[a],'curve':38}) for a,b,w in arcs])
        if j==0:
            s.text(x+260,475,tr(lang,'Выход: (3, 3, 2)','Outgoing: (3, 3, 2)'));s.text(x+260,515,tr(lang,'Вход: (3, 2, 3)','Incoming: (3, 2, 3)'))
        else:
            s.text(x+260,475,tr(lang,'Выход = вход','Outgoing = incoming'),bold=True);s.text(x+260,515,'(45, 36, 42)/16')
    s.text(560,620,'σ_a = 15/16;    σ_b = 12/16;    σ_c = 21/16',bold=True)
    s.text(560,660,tr(lang,'Цвет дуги указывает её источник и общий множитель.','Arc color identifies its source and common multiplier.'),size=20)
    return s

def mixed(lang):
    s=SVG(tr(lang,'Смешанный лес двух противоположных орциклов','A mixed forest from opposite directed cycles'),500)
    for j,title in enumerate(['C₊: a → b','C₋: c → b',tr(lang,'Лес типа (2)','A forest of type (2)')]):
        x=20+j*370;s.panel(x,80,340,350,title);p={'a':(x+65,170),'b':(x+275,170),'c':(x+275,350),'d':(x+65,350)}
        cyc=[('a','b'),('b','c'),('c','d'),('d','a')] if j==0 else [('b','a'),('c','b'),('d','c'),('a','d')]
        if j<2:
            edges=[(a,b,{'color':'blue' if j==0 and (a,b)==('a','b') else 'orange' if j==1 and(a,b)==('c','b') else 'gray'}) for a,b in cyc]
        else:edges=[('a','b',{'color':'blue'}),('c','b',{'color':'orange'})]
        s.graph(p,edges,roots=['b','d'] if j==2 else [])
    s.text(560,475,tr(lang,'Один смешанный лес: тройка с корнем b и одиночная вершина d.','One mixed forest: a triple rooted at b and singleton d.'),size=22)
    return s

def factors(lang):
    s=SVG(tr(lang,'Разложение по дугам на общей системе вершин','An arc decomposition on the same vertex set'),490)
    for j,title in enumerate([tr(lang,'Степень d = 2','Degree d = 2'),tr(lang,'Первый 1-фактор','First 1-factor'),tr(lang,'Второй 1-фактор','Second 1-factor')]):
        x=20+j*370;s.panel(x,80,340,350,title);p={'a':(x+170,165),'b':(x+60,350),'c':(x+280,350)}
        blue=[('a','b'),('b','c'),('c','a')];orange=[('b','a'),('c','b'),('a','c')]
        edges=[]
        if j!=2:edges += [(a,b,{'color':'blue','curve':28 if j==0 else 0}) for a,b in blue]
        if j!=1:edges += [(a,b,{'color':'orange','curve':28 if j==0 else 0}) for a,b in orange]
        s.graph(p,edges)
    s.text(560,472,tr(lang,'Все дуги имеют вес 1. Каждый фактор содержит все три вершины.','All arcs have weight 1. Each factor contains all three vertices.'),size=22)
    return s

def repair(lang):
    s=SVG(tr(lang,'3-орцикл и двусторонняя связь ab','A directed 3-cycle and a two-way coupling ab'),510)
    p={'a':(125,170),'b':(430,170),'c':(280,410)}
    s.graph(p,[('a','b',{'weight':2,'curve':-75}),('b','a',{'weight':1,'curve':-60}),('b','c',{'weight':1}),('c','a',{'weight':1})])
    s.panel(580,90,510,360,tr(lang,'Баланс каждой вершины','Balance at every vertex'))
    for x,label in zip([655,805,975],[tr(lang,'Вершина','Vertex'),tr(lang,'Выход','Out'),tr(lang,'Вход','In')]):s.text(x,180,label,bold=True,size=21)
    for y,a,w in zip([245,310,375],['a','b','c'],[2,2,1]):
        for x,value in zip([655,805,975],[a,w,w]):s.text(x,y,value,size=25)
    s.text(560,486,tr(lang,'Дуги через c компенсируют разные веса встречных дуг между a и b.','Arcs through c balance the unequal opposite weights between a and b.'),size=21)
    return s

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);args=parser.parse_args()
    root=Path('\\\\?\\'+str(args.root.resolve())) if __import__('os').name=='nt' else args.root.resolve()
    for lang in ['ru','en']:
        for key in FIGS:
            svg=globals()[key](lang);svg.save(root/DIRS[lang]/'images'/(FIGS[key][lang=='en']+'.svg'))
    print('Generated 9 new figure pairs and repaired the weighted-triangle pair.')
if __name__=='__main__':main()
