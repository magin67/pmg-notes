"""Reproducible bilingual SVG figures for the KVP editorial revision.

Run with --root PATH pointing to a repository checkout (or a staging root).
All figures are written to the corresponding series/images directories.
"""
from pathlib import Path
import argparse, html, math, re

DIRS={'ru':'pmg-library/ru/Инварианты, разложения и спектры/KVP-разложение',
      'en':'pmg-library/en/Invariants, Decompositions, and Spectra/KVP decomposition'}
NAMES={
 'routes':('Маршруты серии KVP','Routes through the KVP series'),
 'transforms':('Переходы между связями и резистенсами','Transformations from couplings to resistances'),
 'directed':('Три таблицы резистенсов балграфа','Three resistance tables of a balanced graph'),
 'radius':('Центр сферы и центроид в KVP','Circumcenter and centroid in KVP'),
 'mixed':('Смешанные векторы KVP для пути P5','Mixed KVP vectors for the path P5'),
 'triangle':('Площадь треугольника и потенциал второго порядка','Triangle area and the second-order potential'),
 'tetra':('Путь P4 и резистивный тетраэдр','The path P4 and its resistance tetrahedron'),
 'forests':('Одинаковые чистые топономы и разные смешанные вклады','Equal pure toponomes and different mixed contributions')}
C={'ink':'#20344a','blue':'#28638c','orange':'#b45920','green':'#178071','gray':'#9ba8b5','purple':'#7e549b'}
def tr(lang,ru,en):return ru if lang=='ru' else en
class SVG:
    def __init__(self,title,lang,height=610):
        self.height=height
        self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(title)}</title>',f'<desc id="desc">{html.escape(tr(lang,"Математический смысл и точные данные приведены в подписи к рисунку.","The caption provides the mathematical interpretation and exact data."))}</desc>','<defs>']
        for name,col in C.items():self.items.append(f'<marker id="{name}" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L14 7 L0 14 Z" fill="{col}"/></marker>')
        self.items+=['</defs>',f'<rect width="1120" height="{height}" rx="12" fill="white"/>','<g font-family="Arial, DejaVu Sans, sans-serif">']
        self.text(560,42,title,25,bold=True)
    def text(self,x,y,t,size=22,color='ink',bold=False,anchor='middle',halo=False):
        content=re.sub(r'([A-Za-zα-ωΑ-Ω])_([A-Za-z]+)',r'\1<tspan baseline-shift="sub" font-size="70%">\2</tspan>',html.escape(str(t)))
        self.items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{C[color]}" text-anchor="{anchor}"'+(' font-weight="bold"' if bold else '')+(' paint-order="stroke" stroke="white" stroke-width="5" stroke-linejoin="round"' if halo else '')+'>'+content+'</text>')
    def line(self,a,b,color='blue',width=3,arrow=False,dash=False):
        self.items.append(f'<path d="M{a[0]:.2f} {a[1]:.2f} L{b[0]:.2f} {b[1]:.2f}" fill="none" stroke="{C[color]}" stroke-width="{width}"'+(f' marker-end="url(#{color})"' if arrow else '')+(' stroke-dasharray="8 6"' if dash else '')+'/>')
    def panel(self,x,y,w,h,title=None):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f7f9fc" stroke="#dce4ec"/>')
        if title:self.text(x+w/2,y+34,title,22,bold=True)
    def circle(self,p,r,color='gray',fill='none',width=2):
        self.items.append(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r:.2f}" fill="{fill}" stroke="{C[color]}" stroke-width="{width}"/>')
    def vertex(self,p,label):
        self.circle(p,20,'blue','white');self.text(p[0],p[1]+7,label,23)
    def point(self,p,label,offset=(0,-15),color='ink'):
        self.circle(p,5,color,C[color]);self.text(p[0]+offset[0],p[1]+offset[1],label,23,color,bold=True,halo=True)
    def polygon(self,pts,fill='#e2eff9'):
        self.items.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{fill}"/>')
    def edge(self,a,b,value,color=None,dash=None,labeloffset=(0,-12),width=3):
        color=color or ('orange' if str(value).startswith('−') else 'blue')
        dash=(color=='orange') if dash is None else dash
        self.line(a,b,color,width,dash=dash)
        if value is not None:self.text((a[0]+b[0])/2+labeloffset[0],(a[1]+b[1])/2+labeloffset[1],value,21,color,halo=True)
    def save(self,p):
        p.parent.mkdir(parents=True,exist_ok=True);p.write_text('\n'.join(self.items+['</g></svg>'])+'\n',encoding='utf-8')

def routes(lang):
    s=SVG(tr(lang,'Выберите маршрут после определения KVP','Choose a route after the KVP definition'),lang,650)
    s.panel(380,80,360,100);s.text(560,120,'1',27,'blue',True);s.text(560,153,tr(lang,'Определение и компоненты','Definition and components'))
    xs=[20,295,570,845]
    labels=[('2',tr(lang,'Графовые примеры','Graph examples')),('3',tr(lang,'Направленные данные','Directed data')),('4 → 5',tr(lang,'Переходы и резистенсы','Transforms and resistances')),('9',tr(lang,'Леса и топономы','Forests and toponomes'))]
    s.line((560,180),(560,220));s.line((145,220),(970,220))
    for x,(n,t) in zip(xs,labels):
        s.line((x+125,220),(x+125,254),arrow=True)
        s.panel(x,260,250,105);s.text(x+125,301,n,27,'blue',True);s.text(x+125,337,t,19)
    for x,n,t in [(295,'6',tr(lang,'Электрометрия','Electrometry')),(570,'7 → 8',tr(lang,'Параметры и потенциалы','Parameters and potentials'))]:
        s.panel(x,465,250,100);s.text(x+125,505,n,27,'blue',True);s.text(x+125,540,t,19)
    s.line((695,365),(695,459),arrow=True)
    s.line((680,400),(420,400));s.line((680,365),(680,400));s.line((420,400),(420,459),arrow=True)
    s.text(560,610,tr(lang,'Пример взаимодействий в заметке 6: достаточно маршрута 1 → 6.','For the interaction example in note 6, the route 1 → 6 is sufficient.'),20)
    return s

def transforms(lang):
    s=SVG(tr(lang,'Два пути от лапласиана к парным данным','Two routes from the Laplacian to pair data'),lang,690)
    boxes=[(30,110,220,'C',tr(lang,'Связи; диагональ 0','Couplings; diagonal 0')),(420,110,220,'L = ℒ(C)',tr(lang,'Матрица лапласиана','Laplacian matrix')),(850,110,240,'Gr = L⁺',tr(lang,'Матрица Грина','Green matrix')),(420,350,220,'Q = D(L)',tr(lang,'Диагональ 0','Diagonal 0')),(850,350,240,'R = D(Gr)',tr(lang,'Резистенсы; диагональ 0','Resistances; diagonal 0'))]
    for x,y,w,title,sub in boxes:s.panel(x,y,w,110);s.text(x+w/2,y+44,title,27,bold=True);s.text(x+w/2,y+82,sub,18)
    s.line((255,165),(414,165),arrow=True);s.text(334,140,tr(lang,'Линейно','Linear'),19)
    s.line((646,165),(844,165),'orange',arrow=True);s.text(745,130,tr(lang,'Обращение на H','Inversion on H'),18,'orange');s.text(745,194,tr(lang,'Нелинейно','Nonlinear'),18,'orange')
    for x in [530,970]:s.line((x,225),(x,344),arrow=True);s.text(x+30,288,'D',24,anchor='start')
    s.text(560,80,tr(lang,'Связный ненаправленный граф; H = 1⊥','Connected undirected graph; H = 1⊥'),20)
    s.panel(30,520,1060,130)
    s.text(560,559,tr(lang,'Парные коэффициенты Грина: γᵢⱼ = −Grᵢⱼ (i ≠ j), γᵢᵢ = 0','Green pair coefficients: γᵢⱼ = −Grᵢⱼ (i ≠ j), γᵢᵢ = 0'),22)
    s.text(560,597,'γ  ⟷  Gr = ℒ(γ)',27,bold=True)
    s.text(560,629,tr(lang,'Этот переход линейный; KVP применяется к γ.','This transformation is linear; KVP is applied to γ.'),20)
    return s

def directed(lang):
    s=SVG(tr(lang,'Односторонняя, сбалансированная и симметричная таблицы','One-way, balanced, and symmetric tables'),lang,590)
    labels=[('r','K + V + P + O + U',tr(lang,'Односторонняя','One-way')),('r̃ = ½ D(Gr)','K + V + P + O',tr(lang,'Сбалансированная','Balanced')),('R = r + rᵀ','2K + 2V + 2P',tr(lang,'Симметричная','Symmetric'))]
    for x,(title,components,kind) in zip([30,410,790],labels):
        s.panel(x,130,300,160);s.text(x+150,169,title,26,bold=True);s.text(x+150,210,kind,21);s.text(x+150,258,components,22,'blue')
    s.line((336,211),(404,211),arrow=True);s.text(370,115,'−r_U',23)
    s.line((716,211),(784,211),arrow=True);s.text(750,110,tr(lang,'+ трансп.','+ transpose'),17)
    s.line((180,296),(180,370));s.line((180,370),(940,370));s.line((940,370),(940,297),arrow=True)
    s.text(560,359,'r + rᵀ',23,halo=True)
    s.text(560,425,tr(lang,'K, V, P, O, U в панелях - компоненты исходной таблицы r.','K, V, P, O, U in the panels are components of the original table r.'),20)
    s.text(560,465,tr(lang,'Удаление U сохраняет O; симметризация удаляет O и U.','Removing U preserves O; symmetrization removes O and U.'),22)
    s.text(560,507,'(r_U)ᵢⱼ = (qⱼ − qᵢ)/2',25,'orange',True)
    s.text(560,550,tr(lang,'Для резистенсов балграфа V определяет U: переход r ↔ r̃ обратим.','For balanced-graph resistances, V determines U: r ↔ r̃ is invertible.'),20)
    return s

def radius(lang):
    s=SVG(tr(lang,'Радиус и смещение центра','Radius and center displacement'),lang,620)
    s.panel(20,80,620,500);s.panel(665,80,435,500)
    scale=180
    proj=lambda x,y:(120+scale*x,410-scale*y)
    a,b,c=proj(0,0),proj(2,0),proj(0,1);p=proj(1,.5);h=proj(2/3,1/3)
    s.circle(p,scale*math.sqrt(5)/2,'blue',width=2)
    s.polygon([a,b,c]);
    for u,v in [(a,b),(a,c),(b,c)]:s.line(u,v,'gray',2)
    for v in [a,b,c]:s.line(p,v,'blue',2,dash=True)
    s.line(h,p,'orange',4,arrow=True)
    for v,name,off in [(a,'a',(0,27)),(b,'b',(0,27)),(c,'c',(-20,-10))]:s.point(v,name,off)
    s.point(h,'h',(-18,23),'orange');s.point(p,'p',(15,-12),'blue')
    s.text(415,352,'√ρ',24,'blue',halo=True)
    s.text(330,547,tr(lang,'Резистенсы: 4, 1, 5','Resistances: 4, 1, 5'),22)
    s.text(882,126,tr(lang,'Точные координаты','Exact coordinates'),23,bold=True)
    for y,t in [(178,'h = (2/3, 1/3)'),(222,'p = (1, 1/2)'),(294,'ρ₀ = 10/9'),(338,'(p − h)² = 5/36'),(405,'ρ = 10/9 + 5/36 = 5/4')]:s.text(882,y,t,24)
    s.text(882,480,tr(lang,'ρ₀: среднее квадратов','ρ₀: mean squared'),21)
    s.text(882,512,tr(lang,'расстояний до h','distance to h'),21)
    return s

def mixed(lang):
    s=SVG(tr(lang,'Метрические вклады не ортогональны','Metric contributions are not orthogonal'),lang,530)
    s.panel(20,80,690,390);s.panel(735,80,365,390)
    # Exact coordinates in units sqrt(10)/150; an isometry and common scale.
    h=(100,260);a=(640,260);b=(568,224);p=(478,314)
    for u,v,col in [(h,a,'blue'),(a,b,'orange'),(b,p,'purple')]:s.line(u,v,col,4,True)
    s.line(h,p,'green',3,True,dash=True)
    s.point(h,'h',(-20,-18));s.point(p,'p',(20,28),'green')
    s.text(340,239,'z_K',25,'blue',True,halo=True);s.text(620,210,'z_V',25,'orange',True,halo=True);s.text(551,304,'z_P',25,'purple',True,halo=True)
    s.text(285,322,'p − h',24,'green',True,halo=True)
    s.text(365,399,'z_K + z_V + z_P = p − h',25,bold=True)
    s.text(917,126,tr(lang,'Путь P₅','Path P₅'),24,bold=True)
    for y,t in [(191,'Σ z_X² = 97/225'),(250,'2Σ z_X·z_Y = −52/225'),(321,'(p − h)² = 45/225'),(361,'= 1/5')]:s.text(917,y,t,22)
    s.text(917,423,tr(lang,'Во второй сумме X < Y','The second sum uses X < Y'),18)
    s.text(560,510,tr(lang,'Точная плоская реализация трёх векторов; см. координаты в подписи.','Exact planar realization of three vectors; see the caption for coordinates.'),20)
    return s

def triangle(lang):
    s=SVG(tr(lang,'От площади треугольника к потенциалу','From triangle area to potential'),lang,560)
    s.panel(20,80,610,430);s.panel(655,80,445,430)
    a,b,c,d=(90,390),(310,390),(310,170),(530,170)
    s.polygon([a,b,c]);s.line(b,d,'gray',2,dash=True);s.line(d,c,'gray',2,dash=True)
    s.line(a,b,'blue',4,True);s.line(a,c,'orange',4,True);s.line(b,c,'gray',2)
    for p,t,off in [(a,'a',(-22,20)),(b,'b',(18,25)),(c,'c',(0,-18))]:s.point(p,t,off)
    s.text(180,424,'(ab)',23,'blue');s.text(175,267,'(ac)',23,'orange',halo=True)
    s.text(248,335,'A = 1/2',22,halo=True);s.text(412,274,tr(lang,'Площадь 1','Area 1'),21)
    s.text(877,130,tr(lang,'Грамиан двух векторов','Gram matrix of two vectors'),22,bold=True)
    s.text(797,215,'G =',27)
    for x,y,t in [(870,192,'1'),(935,192,'1'),(870,235,'1'),(935,235,'2')]:s.text(x,y,t,27)
    for x in [835,970]:
        s.line((x,164),(x,249),'ink',2)
        for y in [164,249]:s.line((x,y),(x+(10 if x==835 else -10),y),'ink',2)
    s.text(877,285,'det G = 2 − 1 = 1',25)
    s.text(877,355,'h_abc = 4A² = 1',27,'blue',True)
    s.text(877,437,'R_ab = R_bc = 1; R_ac = 2',21)
    s.text(560,545,tr(lang,'Квадрат площади параллелограмма равен норме границы тройки.','The squared parallelogram area equals the quadratic norm of the triple boundary.'),19)
    return s

def tetra(lang):
    s=SVG(tr(lang,'Схема пути и резистивное вложение','Path diagram and resistance embedding'),lang,660)
    s.panel(20,80,420,460,tr(lang,'Граф P₄','Graph P₄'));s.panel(460,80,640,460,tr(lang,'Резистивный тетраэдр','Resistance tetrahedron'))
    ps={'a':(70,240),'b':(175,240),'c':(280,240),'d':(385,240)}
    for a,b in [('a','b'),('b','c'),('c','d')]:s.edge(ps[a],ps[b],'1')
    for name,p in ps.items():s.vertex(p,name)
    s.text(230,342,tr(lang,'Все проводимости равны 1','All conductances equal 1'),21)
    s.text(230,389,tr(lang,'Положение на схеме','Diagram positions'),21)
    s.text(230,422,tr(lang,'не задаёт расстояния','do not specify distances'),21)
    ps={'a':(540,430),'b':(825,430),'c':(1010,310),'d':(850,170)}
    for a,b,col in [('a','b','blue'),('c','d','blue'),('a','c','orange'),('b','d','orange'),('a','d','green'),('b','c','green')]:s.line(ps[a],ps[b],col,3)
    for name,p in ps.items():s.vertex(p,name)
    s.text(780,500,tr(lang,'Три шага пути ортогональны в 3D','The three path steps are orthogonal in 3D'),20)
    s.text(560,585,'(ab)·(cd) = 0;   (ac)·(bd) = 1;   (ad)·(bc) = 1',25)
    s.text(560,628,'H₄ = 1 + 4 + 3 − (0 + 1 + 1) = 6',27,'blue',True)
    return s

def forests(lang):
    s=SVG(tr(lang,'Чистые компоненты и их совместное действие','Pure components and their combined effect'),lang,690)
    es=[ [('a','b','−1'),('a','d','−1'),('b','c','+1'),('c','d','+1')],
         [('a','b','+1'),('c','d','+1'),('a','c','−1'),('b','d','−1')],
         [('a','b','−1'),('c','d','−1'),('a','c','+1'),('b','d','+1')]]
    for j,(title,edges) in enumerate(zip([tr(lang,'Общая V','Common V'),'P₊','P₋ = −P₊'],es)):
        x=20+j*370;s.panel(x,85,340,400,title)
        p={'a':(x+65,185),'b':(x+275,185),'c':(x+275,375),'d':(x+65,375)}
        for a,b,val in edges:
            off=(0,-12) if a+b in ['ab','cd'] else (-27,0) if a+b=='ad' else (27,0) if a+b=='bc' else (-12,-17) if a+b=='ac' else (-12,20)
            s.edge(p[a],p[b],val,labeloffset=off)
        for name,point in p.items():s.vertex(point,name)
        s.text(x+170,454,'K: 3' if j==0 else ('τ(C₊) = 398' if j==1 else 'τ(C₋) = 394'),24,bold=True)
    s.text(560,540,'T(P₊) = T(P₋) = 1 − 4x₂ + 2x₁²',26)
    s.text(560,589,tr(lang,'Смешанный вклад: +2ν²π или −2ν²π','Mixed contribution: +2ν²π or −2ν²π'),25,'orange',True)
    s.text(560,642,tr(lang,'Знак P меняется; имена вершин и V остаются фиксированными.','The sign of P changes; vertex labels and V remain fixed.'),21)
    return s

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);args=parser.parse_args()
    root=Path('\\\\?\\'+str(args.root.resolve())) if __import__('os').name=='nt' else args.root
    for key in NAMES:
        for lang in DIRS:
            name=NAMES[key][0 if lang=='ru' else 1]
            globals()[key](lang).save(root/DIRS[lang]/'images'/(name+'.svg'))
    print('Generated 16 bilingual SVG files.')
if __name__=='__main__':main()
