"""Reproduce the bilingual SVG figures: python draw_editorial_figures.py --root ."""
from pathlib import Path
from itertools import combinations
import argparse, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Polygon

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.fonttype':'none','svg.hashsalt':'pmg-symmetric-2026-11-08','mathtext.fontset':'dejavusans','figure.facecolor':'white','savefig.facecolor':'white'})
BLUE='#276b9c';ORANGE='#bc641b';TEAL='#147b66';RED='#b9413c';INK='#263d4c';GRAY='#aebbc4';PALE='#edf3f7'
PREFIX={'ru':'pmg-library/ru/Алгебра и комбинаторика полиформ/Симметрические полиформы/images','en':'pmg-library/en/Polyform Algebra and Combinatorics/Symmetric polyforms/images'}
NAMES={
'route':('Путь от разбиений к лесным коэффициентам','From Partitions to Forest Coefficients'),
'types':('Разбиение и грейды его блоков','A Partition and Its Block Grades'),
'orbit':('Три разбиения и двадцать четыре перестановки','Three Partitions and Twenty-Four Permutations'),
'merge':('Суммы форм на пяти вершинах','Sums of Forms on Five Vertices'),
'products':('Три случая произведения границ','Three Cases of Boundary Multiplication'),
'trees':('Три леса для одного разбиения','Three Forests for One Partition'),
'cycle':('От полного графа к четырёхциклу','From the Complete Graph to the Four-Cycle'),
'roots':('Добавление и удаление корней','Adding and Deleting Roots'),
'fifty':('Пятьдесят лесов с двумя заданными корнями','Fifty Forests with Two Prescribed Roots')}
def tr(l,a,b):return a if l=='ru' else b
def txt(ax,x,y,s,size=16,color=INK,**kw):return ax.text(x,y,s,ha=kw.pop('ha','center'),va=kw.pop('va','center'),fontsize=size,color=color,**kw)
def canvas(w=12,h=4,x=(0,12),y=(0,4)):
    f,ax=plt.subplots(figsize=(w,h));ax.set_xlim(*x);ax.set_ylim(*y);ax.axis('off');ax.set_aspect('equal');f.subplots_adjust(left=.025,right=.975,bottom=.04,top=.96);return f,ax
def edge(ax,p,q,col=BLUE,lw=2.8,ls='-'):ax.plot([p[0],q[0]],[p[1],q[1]],color=col,lw=lw,ls=ls,zorder=2)
def node(ax,p,label,col=BLUE,root=False,r=.14):
    ax.add_patch(Circle(p,r,ec=col,fc='white',lw=2,zorder=4));txt(ax,*p,label,14,col,zorder=5)
    if root:ax.add_patch(Circle(p,r+.055,ec=col,fc='none',lw=1.6,zorder=4))
def arrow(ax,p,q):ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=27,lw=2.5,color=ORANGE,zorder=3))
def box(ax,x,y,w,h,col=BLUE,alpha=.07):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05,rounding_size=0.12',fc=col,ec=col,lw=1.5,alpha=alpha,zorder=0))
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05,rounding_size=0.12',fc='none',ec=col,lw=1.1,zorder=0))
def row(ax,blocks,x,y,step=.5):
    for i,b in enumerate(blocks):
        col=[BLUE,ORANGE,TEAL][i%3];w=len(b)*step
        box(ax,x-step*.36,y-.24,w-step*.28,.48,col)
        for j,v in enumerate(b):node(ax,(x+j*step,y),v,col,r=.135)
        x+=w+.20
def graph(ax,pos,edges,col=BLUE,roots=(),faint=()):
    for u,v in faint:edge(ax,pos[u],pos[v],GRAY,1.2,'--')
    for u,v in edges:edge(ax,pos[u],pos[v],col)
    for v,p in pos.items():node(ax,p,v,ORANGE if v in roots else col,root=v in roots)
def square(cx,cy,s=.58):return dict(zip('abcd',[(cx-s,cy+s),(cx+s,cy+s),(cx+s,cy-s),(cx-s,cy-s)]))

def route(l):
    f,ax=canvas(11,6,x=(0,11),y=(0,6))
    labels=([('Разбиение вершин','Какие вершины входят в каждый блок?'),('Симметрическая сумма','Все разбиения одного типа, каждое один раз'),('Главная полиформа','Один нетривиальный блок в каждом слагаемом'),('Произведения и полный граф','Правило умножения и лесное разложение'),('Лесные коэффициенты','Корни, группы компонент и многочлены Абеля')] if l=='ru' else [('A partition of vertices','Which vertices belong to each block?'),('A symmetric sum','All partitions of one type, each counted once'),('A principal polyform','One nontrivial block in each term'),('Products and the complete graph','Multiplication and the forest expansion'),('Forest coefficients','Roots, groups of components, and Abel polynomials')])
    for i,(title,sub) in enumerate(labels):
        y=5.1-i*1.12;box(ax,.7,y-.30,9.6,.79,[BLUE,TEAL,BLUE,TEAL,BLUE][i]);txt(ax,5.5,y+.17,title,17,weight='bold');txt(ax,5.5,y-.12,sub,14)
        if i<4:arrow(ax,(5.5,y-.40),(5.5,y-.71))
    return f
def types(l):
    f,ax=canvas(11,4,x=(0,11),y=(0,4))
    txt(ax,5.5,3.65,tr(l,'Одно разбиение шести вершин','One partition of six vertices'),19,weight='bold')
    for x,b in [(1,'abc'),(5.2,'de'),(8.7,'f')]:
        w=len(b)*.65;box(ax,x-.35,2.1,w+.25,.8,[BLUE,ORANGE,TEAL][['abc','de','f'].index(b)])
        for j,v in enumerate(b):node(ax,(x+j*.65,2.5),v,[BLUE,ORANGE,TEAL][['abc','de','f'].index(b)])
        cx=x+(len(b)-1)*.325
        txt(ax,cx,1.6,tr(l,'Размер блока: ','Block size: ')+str(len(b)),15)
        txt(ax,cx,1.1,tr(l,'Грейд: ','Grade: ')+str(len(b)-1),16,weight='bold')
    txt(ax,5.5,.35,r'$[3,2,1]\ \longrightarrow\ [2,1,0],\qquad k=3,\ m=3,\ r=2,\ \ell=1$',17)
    return f
def orbit(l):
    f,ax=canvas(12,4.5,x=(0,12),y=(0,4.5))
    txt(ax,6,4.13,tr(l,'24 перестановки дают 3 разбиения','24 permutations produce 3 partitions'),19,weight='bold')
    for x,blocks in zip([.55,4.55,8.55],[['ab','cd'],['ac','bd'],['ad','bc']]):
        row(ax,blocks,x,2.9,.58);txt(ax,x+1.05,1.95,r'$2!\cdot2!\cdot2!=8$',18)
    txt(ax,6,1.0,tr(l,'Внутри каждой пары: 2 порядка. Порядок двух пар: ещё 2.','Two orders inside each pair; two more orders for the pair of blocks.'),15)
    txt(ax,6,.43,r'$24=3\cdot8\qquad\quad \sum_{\sigma\in S_4}\sigma[(ab)(cd)]^2=8E_4[1,1]$',18)
    return f
def merge(l):
    f,ax=canvas(12,8.5,x=(0,12),y=(0,8.5))
    txt(ax,6,8.13,r'$E_5[2,1]=3E_5[3,0]$',25,weight='bold')
    txt(ax,2.5,7.49,tr(l,'10 разбиений: тройка + пара','10 partitions: triple + pair'),15,weight='bold')
    txt(ax,9.1,7.49,tr(l,'5 разбиений: четвёрка + вершина','5 partitions: quadruple + singleton'),15,weight='bold')
    for i,pair in enumerate(combinations('abcde',2)):
        pair=''.join(pair);other=''.join(v for v in 'abcde' if v not in pair);row(ax,[other,pair],.8,6.9-i*.61,.55)
    for i,v in enumerate('abcde'):
        row(ax,[''.join(x for x in 'abcde' if x!=v),v],7.5,6.6-i*1.22,.55)
    txt(ax,5.9,3.9,'= 3 ×',24)
    txt(ax,6,.42,tr(l,'Сравниваются суммы форм всех строк. Коэффициенты: 1 слева, 3 справа.','Compare the sums of all row forms. Coefficients: 1 on the left, 3 on the right.'),14)
    return f
def products(l):
    f,ax=canvas(13,5,x=(0,13),y=(0,5))
    titles=tr(l,['Нет общих вершин','Одна общая вершина','Две общие вершины'],['No shared vertices','One shared vertex','Two shared vertices'])
    for x,s in zip([2.1,6.5,10.9],titles):txt(ax,x,4.55,s,17,weight='bold')
    p=square(2.1,2.85,.7)
    edge(ax,p['a'],p['b'],BLUE);edge(ax,p['c'],p['d'],ORANGE)
    for v,z in p.items():node(ax,z,v,BLUE if v in 'ab' else ORANGE)
    p={'a':(5.7,2.5),'b':(6.5,3.45),'c':(7.3,2.5)}
    edge(ax,p['a'],p['b'],BLUE);edge(ax,p['b'],p['c'],ORANGE)
    for v,z in p.items():node(ax,z,v,TEAL if v=='b' else BLUE,root=v=='b')
    p=square(10.9,2.85,.7)
    for block,col in [('abc',BLUE),('bcd',ORANGE)]:
        ax.add_patch(Polygon([p[v] for v in block],fc=col,alpha=.12,zorder=0))
        for u,v in zip(block,block[1:]+block[:1]):edge(ax,p[u],p[v],col)
    edge(ax,p['b'],p['c'],TEAL,4.5)
    for v,z in p.items():node(ax,z,v,TEAL if v in 'bc' else BLUE,root=v in 'bc')
    for x,s in zip([2.1,6.5,10.9],[r'$[(ab)]^2[(cd)]^2$',r'$[(ab)]^2[(bc)]^2$',r'$[(abc)]^2[(bcd)]^2$']):txt(ax,x,1.45,s,17)
    for x,s in zip([2.1,6.5,10.9],[r'$=[(ab)(cd)]^2$',r'$=[(abc)]^2$',r'$=0$']):txt(ax,x,.82,s,20)
    return f
def trees(l):
    f,ax=canvas(12,4.5,x=(0,12),y=(0,4.5))
    txt(ax,6,4.12,tr(l,'Одно разбиение abc | de, три различных леса','One partition abc | de, three different forests'),19,weight='bold')
    choices=[[('a','b'),('a','c')],[('a','b'),('b','c')],[('a','c'),('b','c')]]
    for cx,ee in zip([2,6,10],choices):
        pos={'a':(cx,3.25),'b':(cx-.7,2.18),'c':(cx+.7,2.18),'d':(cx-.6,1.2),'e':(cx+.6,1.2)}
        graph(ax,{v:pos[v] for v in 'abc'},ee,BLUE);graph(ax,{v:pos[v] for v in 'de'},[('d','e')],ORANGE)
    txt(ax,6,.37,tr(l,'Каждый лес даёт форму ','Each forest gives the form ')+r'$[(abc)(de)]^2$',18)
    return f
def cycle(l):
    f,ax=canvas(13,8,x=(0,13),y=(0,8))
    cyc=[('a','b'),('b','c'),('c','d'),('d','a')];diags=[('a','c'),('b','d')]
    p=square(4,6.55,.65);graph(ax,p,cyc)
    for u,v in diags:edge(ax,p[u],p[v],RED,2.3,'--')
    p=square(9,6.55,.65);graph(ax,p,cyc)
    txt(ax,4,7.58,r'$K_4$',22);txt(ax,9,7.58,r'$C_4$',22);arrow(ax,(5.15,6.55),(7.75,6.55))
    txt(ax,6.5,5.37,tr(l,'4 остовных дерева: удалить одно ребро цикла','4 spanning trees: delete one cycle edge'),17,weight='bold')
    for i,x in enumerate([2,5,8,11]):graph(ax,square(x,4.15,.55),[e for j,e in enumerate(cyc) if i!=j],faint=[cyc[i]])
    txt(ax,6.5,2.92,tr(l,'6 двухрёберных лесов: выбрать два ребра','6 two-edge forests: choose two edges'),17,weight='bold')
    for x,ee in zip([1.1,3.25,5.4,7.55,9.7,11.85],combinations(cyc,2)):
        graph(ax,square(x,1.7,.43),ee,faint=[e for e in cyc if e not in ee])
    txt(ax,6.5,.52,r'$(M_{C_4})_2=E_4[2]+[(ab)(cd)]^2+[(ad)(bc)]^2$',19)
    return f
def roots(l):
    f,ax=canvas(13,5.5,x=(0,13),y=(0,5.5))
    titles=tr(l,['Два блока','Добавить корень к каждому','Удалить добавленные корни'],['Two blocks','Add a root to each block','Delete the added roots'])
    for cx,title in zip([2,6.5,11],titles):txt(ax,cx,5.1,title,16,weight='bold')
    for cx in [2,6.5,11]:
        box(ax,cx-1.25,1.95,2.5,2.15,BLUE);box(ax,cx-.6,.7,1.2,.7,ORANGE)
    p={'a':(1.2,3.3),'b':(2,2.5),'c':(2.8,3.3),'d':(2,1.05)}
    for v,z in p.items():node(ax,z,v,ORANGE if v=='d' else BLUE)
    p={'a':(5.7,2.5),'b':(6.5,2.5),'c':(7.3,2.5),'d':(6.1,1.05),'ρ₁':(6.5,3.55),'ρ₂':(6.85,1.05)}
    graph(ax,{v:p[v] for v in ['a','b','c','ρ₁']},[('ρ₁','a'),('ρ₁','c'),('a','b')],roots=['ρ₁'])
    graph(ax,{v:p[v] for v in ['d','ρ₂']},[('ρ₂','d')],ORANGE,roots=['ρ₂'])
    p={'a':(10.2,3.3),'b':(11,2.5),'c':(11.8,3.3),'d':(11,1.05)}
    graph(ax,{v:p[v] for v in 'abc'},[('a','b')],roots=['a','c']);graph(ax,{'d':p['d']},[],ORANGE,roots=['d'])
    arrow(ax,(3.45,2.8),(4.95,2.8));arrow(ax,(7.95,2.8),(9.45,2.8))
    txt(ax,2,.23,r'$k=4,\ m=2$',16);txt(ax,6.5,.23,tr(l,'Корни ρ₁, ρ₂ закреплены за блоками','Roots ρ₁, ρ₂ belong to their blocks'),13);txt(ax,11,.23,r'$r=3,\ m=2$',16)
    return f
def fifty(l):
    f,ax=canvas(12,4.8,x=(0,12),y=(0,4.8))
    txt(ax,6,4.48,tr(l,'3 обычные вершины и 2 заданных корня','3 ordinary vertices and 2 prescribed roots'),19,weight='bold')
    for cx,title in [(3,tr(l,'Один корень изолирован','One root is isolated')),(9,tr(l,'Оба корня заняты','Both roots are occupied'))]:txt(ax,cx,3.85,title,17)
    for cx,left in [(3,True),(9,False)]:
        p={'a':(cx-1,2.1),'b':(cx,1.6),'c':(cx+1,2.1),'ρ₁':(cx-1,2.95),'ρ₂':(cx+1,2.95)}
        ee=[('ρ₁','a'),('a','b'),('b','c')] if left else [('ρ₁','a'),('ρ₁','b'),('ρ₂','c')]
        graph(ax,p,ee,roots=['ρ₁','ρ₂'])
        txt(ax,cx,.9,r'$2\cdot\mathrm{St}(3,1)=32$' if left else r'$2!\cdot\mathrm{St}(3,2)=18$',20)
    txt(ax,6,.23,r'$A_3(2)=32+18=50$',21,weight='bold')
    return f

BUILDERS=[route,types,orbit,merge,products,trees,cycle,roots,fifty]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path('.'));ap.add_argument('--preview',type=Path);args=ap.parse_args()
    for lang in ['ru','en']:
        for fn in BUILDERS:
            f=fn(lang);dest=args.root/PREFIX[lang]/(NAMES[fn.__name__][lang=='en']+'.svg');dest.parent.mkdir(parents=True,exist_ok=True)
            f.savefig(dest,metadata={'Date':None,'Description':NAMES[fn.__name__][lang=='en']})
            if args.preview:
                args.preview.mkdir(parents=True,exist_ok=True);f.savefig(args.preview/(lang+'-'+fn.__name__+'.png'),dpi=100)
            plt.close(f)
    print('Generated 18 SVG files: nine figures in both languages.')
if __name__=='__main__':main()
