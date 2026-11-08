"""Reproduce the bilingual vector figures: python draw_editorial_figures.py --root ."""
from pathlib import Path
import argparse, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.fonttype':'none','svg.hashsalt':'pmg-structural-2026-11-08','mathtext.fontset':'dejavusans','figure.facecolor':'white','savefig.facecolor':'white'})
BLUE='#276b9c';ORANGE='#d17a29';TEAL='#1e8a72';RED='#bd4d43';INK='#263d4c';GRAY='#aebbc4';PALE='#edf3f7'
PREFIX={'ru':'pmg-library/ru/Алгебра и комбинаторика полиформ/Структурные тождества/images','en':'pmg-library/en/Polyform Algebra and Combinatorics/Structural identities/images'}
NAMES={
'seven':('Семь разбиений в тождестве тетраэдра','Seven Partitions in the Tetrahedron Identity'),
'box':('Тетраэдр и три площади параллелепипеда','A Tetrahedron and Three Parallelepiped Areas'),
'merge':('Присоединение пары к разбиению','Joining a Pair to a Partition'),
'blocks':('От четырёх вершин к четырём блокам','From Four Vertices to Four Blocks'),
'crossing':('Пересекающиеся и непересекающиеся разбиения','Crossing and Noncrossing Partitions'),
'pairing':('Спаривание разбиений - дерево или цикл','Pairing Partitions - A Tree or a Cycle'),
'cycle':('Сочленение двух путей в цикл','Gluing Two Paths into a Cycle'),
'groves':('Рощи пути с внутренней вершиной','Groves of a Path with an Internal Vertex'),
'support':('Носители разбиений и тождества','Supports of Partitions and an Identity'),
 'transfer':('Перенос и умножение тождества','Transferring and Multiplying an Identity'),
'support_sum':('Носитель суммы двух отношений','Support of a Sum of Two Relations')}
def tr(l,a,b):return a if l=='ru' else b
def text(ax,x,y,s,size=15,color=INK,**kw):return ax.text(x,y,s,ha=kw.pop('ha','center'),va=kw.pop('va','center'),fontsize=size,color=color,**kw)
def edge(ax,p,q,color=BLUE,lw=2.8,ls='-',label=None,offset=(0,.13)):
 ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=lw,ls=ls,zorder=2)
 if label:
  x,y=(np.array(p)+np.array(q))/2+np.array(offset);text(ax,x,y,label,14,bbox={'fc':'white','ec':'none','pad':1.5})
def node(ax,p,name,color=BLUE,fill='white',r=.105):
 ax.add_patch(Circle(p,r,ec=color,fc=fill,lw=2,zorder=4));text(ax,*p,name,16,color if fill=='white' else 'white',zorder=5)
def arrow(ax,p,q,color=ORANGE):ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=24,lw=2.5,color=color,zorder=3))
def setup(ax,x=(-1.4,1.4),y=(-1.38,1.5)):
 ax.set_aspect('equal');ax.set_xlim(*x);ax.set_ylim(*y);ax.axis('off')
def canvas(n=1,w=12,h=4):
 f,aa=plt.subplots(1,n,figsize=(w,h),squeeze=False)
 for a in aa.flat:setup(a)
 f.subplots_adjust(left=.025,right=.975,top=.88,bottom=.12,wspace=.2)
 return f,list(aa.flat)
def title(ax,s):ax.set_title(s,fontsize=16,color=INK,fontweight='bold',pad=10)
def positions(names):
 if names=='abcd':return dict(zip(names,[(-.7,.7),(.7,.7),(.7,-.7),(-.7,-.7)]))
 return {v:np.array((math.cos(t),math.sin(t)))*.85 for v,t in zip(names,np.linspace(math.pi*.65,math.pi*.65-2*math.pi,len(names),endpoint=False))}
def partition(ax,blocks,names='abcd',support=False):
 pos=positions(names);ax.add_patch(Circle((0,0),.99,ec=GRAY,fc='none',lw=1,ls='--',zorder=0))
 for i,b in enumerate(blocks):
  col=[BLUE,ORANGE,TEAL,RED][i%4]
  if len(b)>2:ax.add_patch(Polygon([pos[v] for v in b],fc=col,alpha=.10,ec='none',zorder=0))
  for u,v in zip(b,b[1:]):edge(ax,pos[u],pos[v],col)
  for v in b:
   if support and len(b)>1:ax.add_patch(Circle(pos[v],.19,fc=TEAL,ec='none',alpha=.20,zorder=1))
   node(ax,pos[v],v,color=TEAL if support and len(b)>1 else GRAY if support else col)
 return pos

def seven(l):
 f=plt.figure(figsize=(13,7.5));gs=f.add_gridspec(2,8,left=.03,right=.97,top=.90,bottom=.06,hspace=.55,wspace=.3)
 entries=[(['ab','cd'],0,1),(['ac','bd'],0,3),(['ad','bc'],0,5),(['a','bcd'],1,0),(['b','acd'],1,2),(['c','abd'],1,4),(['d','abc'],1,6)]
 for b,row,col in entries:
  ax=f.add_subplot(gs[row,col:col+2]);setup(ax);partition(ax,b);text(ax,0,-1.25,' | '.join(b),16)
 f.text(.5,.96,tr(l,'Сумма трёх форм разбиений на пары','Sum of three pair-partition forms'),ha='center',color=INK,fontsize=17,weight='bold')
 f.text(.5,.485,tr(l,'равна сумме четырёх форм «тройка + вершина»','equals the sum of four “triple + singleton” forms'),ha='center',color=INK,fontsize=17,weight='bold')
 return f

def crossing(l):
 f,aa=canvas(3)
 for ax,b,cap in zip(aa,[['ab','cd'],['ac','bd'],['ad','bc']],[tr(l,'Непересекающееся','Noncrossing'),tr(l,'Пересекающееся','Crossing'),tr(l,'Непересекающееся','Noncrossing')]):
  partition(ax,b);title(ax,cap);text(ax,0,-1.22,' | '.join(b),17)
 return f

def merge(l):
 f,aa=canvas(2,w=11,h=4.4)
 for j,ax in enumerate(aa):
  p=partition(ax,['ab','cd'] if j==0 else ['abc','d']);edge(ax,p['a'],p['c'],RED,lw=3.5,ls='--');text(ax,-.2,.12,'ac',14,RED,bbox={'fc':'white','ec':'none','pad':1})
  title(ax,tr(l,'Разные блоки → один блок','Different blocks → one block') if j==0 else tr(l,'Один блок → нулевое произведение','Same block → zero product'))
  text(ax,0,-1.25,r'$q_{ab|cd}[(ac)]^2=q_{abcd}$' if j==0 else r'$q_{abc|d}[(ac)]^2=0$',16)
 return f

def blocks(l):
 f,aa=canvas(2,w=12,h=4.7)
 p=partition(aa[0],['abc','d']);title(aa[0],tr(l,'Один из семи членов','One of the seven terms'));text(aa[0],0,-1.25,r'$q_{abc|d}$',18)
 ax=aa[1];p=positions('abcdef')
 for block,col in [('abc',BLUE),('def',ORANGE)]:
  ax.add_patch(Polygon([p[v] for v in block],fc=col,alpha=.12,ec=col))
  for v in block:node(ax,p[v],v,color=col)
 for u,v in [('d','e'),('d','f')]:edge(ax,p[u],p[v],RED,ls='--')
 title(ax,tr(l,'Блок D = {d, e, f}','Block D = {d, e, f}'));text(ax,0,-1.25,r'$q_{abc|def}$',18)
 f.text(.5,.52,r'$\times\,[(de)]^2[(df)]^2$',ha='center',color=RED,fontsize=16)
 f.text(.5,.10,tr(l,'A = {a}, B = {b}, C = {c}; одна операция для всех слагаемых','A = {a}, B = {b}, C = {c}; the same operation for every term'),ha='center',color=INK,fontsize=14)
 f.subplots_adjust(wspace=.65,bottom=.19)
 return f

def pairing(l):
 f,aa=canvas(2,w=11,h=4.5);p=positions('abcd')
 for j,ax in enumerate(aa):
  for u,v in ([('a','b'),('c','d')] if j==0 else [('a','b'),('b','c')]):edge(ax,p[u],p[v])
  edge(ax,p['a'],p['c'],ORANGE,ls='--')
  for v in p:node(ax,p[v],v)
  title(ax,tr(l,'Дерево: коэффициент 1','Tree: coefficient 1') if j==0 else tr(l,'Цикл и отдельная вершина: 0','Cycle and an isolated vertex: 0'))
  text(ax,0,-1.12,'ab | cd  +  ac | b | d' if j==0 else 'abc | d  +  ac | b | d',15)
 f.text(.5,.035,tr(l,'Синие рёбра — первое разбиение; оранжевое — второе','Blue edges: first partition; orange edge: second partition'),ha='center',fontsize=14,color=INK)
 return f

def cycle(l):
 f,aa=canvas(3,w=13,h=4.2)
 for ax,mid,labels,col in [(aa[0],'x',[r'$\alpha$',r'$\beta$'],BLUE),(aa[1],'y',[r'$\gamma$',r'$\delta$'],ORANGE)]:
  p={'a':(-1,0),mid:(0,.5),'b':(1,0)}
  for i,(u,v) in enumerate([('a',mid),(mid,'b')]):edge(ax,p[u],p[v],col,label=labels[i])
  for v in p:node(ax,p[v],v,fill=BLUE if v in 'ab' else 'white')
  title(ax,r'$G_1$' if mid=='x' else r'$G_2$');text(ax,0,-.7,'a – '+mid+' – b',15)
 ax=aa[2];p={'a':(-1,0),'x':(0,.8),'b':(1,0),'y':(0,-.8)}
 for u,v,col,lab,dy in [('a','x',BLUE,r'$\alpha$',.16),('x','b',BLUE,r'$\beta$',.16),('a','y',ORANGE,r'$\gamma$',-.17),('y','b',ORANGE,r'$\delta$',-.17)]:edge(ax,p[u],p[v],col,label=lab,offset=(0,dy))
 for v in p:node(ax,p[v],v,fill=BLUE if v in 'ab' else 'white')
 title(ax,tr(l,'После отождествления a, b','After identifying a, b'))
 f.text(.5,.035,tr(l,'Синие вершины: S = {a, b}. Белые вершины: внутренние.','Blue vertices: S = {a, b}. White vertices: internal.'),ha='center',fontsize=14,color=INK)
 return f

def groves(l):
 f,aa=canvas(4,w=14,h=3.9);p={'a':(-1,0),'x':(0,.55),'b':(1,0)}
 for j,ax in enumerate(aa):
  for k,(u,v) in enumerate([('a','x'),('x','b')]):
   present=j==0 or j==k+1
   edge(ax,p[u],p[v],BLUE if present else GRAY,lw=2.8 if present else 1.1,ls='-' if present else ':',label=([r'$\alpha$',r'$\beta$'][k] if present else None))
  for v in p:node(ax,p[v],v,color=RED if j==3 and v=='x' else BLUE,fill=BLUE if v in 'ab' else 'white')
  title(ax,tr(l,'Роща','Grove') if j<3 else tr(l,'Не роща','Not a grove'))
  text(ax,0,-.65,['ab','a | b','a | b',tr(l,'{x} ∩ S = ∅','{x} ∩ S = ∅')][j],15,RED if j==3 else INK)
  text(ax,0,-1.1,[r'$\alpha\beta$',r'$\alpha$',r'$\beta$',tr(l,'Исключён','Excluded')][j],16)
 return f

def support(l):
 f,aa=canvas(3,w=12,h=4.2)
 for ax,blocks,cap in zip(aa,[['ab','cd','e'],['abc','d','e'],['a','b','c','d','e']],['ab | cd | e','abc | d | e',r'$R_{abcd}$']):
  p=partition(ax,blocks,names='abcde',support=True);title(ax,cap)
  if cap.startswith('$'):
   for v in 'abcd':
    ax.add_patch(Circle(p[v],.21,fc=TEAL,ec=TEAL,alpha=.22,zorder=1));node(ax,p[v],v,color=TEAL)
  text(ax,0,-1.23,'U = {a, b, c, d}' if cap!='abc | d | e' else 'U = {a, b, c}',14,TEAL)
 return f

def support_nodes(ax,active,names='abcdef'):
 p=positions(names)
 for v in names:
  if v in active:ax.add_patch(Circle(p[v],.2,fc=TEAL,ec='none',alpha=.2))
  node(ax,p[v],v,color=TEAL if v in active else GRAY)
 return p

def transfer(l):
 f,aa=canvas(3,w=13,h=4.4)
 for ax,active,cap,grade in zip(aa,['abcd','abcd','abcdef'],[tr(l,'Исходное отношение','Original relation'),tr(l,'Добавить одиночные e, f','Adjoin singleton e, f'),tr(l,'Умножить на [(ef)]²','Multiply by [(ef)]²')],[2,2,3]):
  p=support_nodes(ax,active);title(ax,cap)
  if grade==3:edge(ax,p['e'],p['f'],ORANGE,lw=3)
  text(ax,0,-1.2,f'r = {grade},  |U| = {len(active)}',16)
 f.text(.5,.035,tr(l,'Зелёным выделен носитель; серые вершины в него не входят.','Green highlights the support; gray vertices are outside it.'),ha='center',fontsize=14,color=INK)
 return f

def support_sum(l):
 f,aa=canvas(3,w=12,h=4)
 for ax,active,cap in zip(aa,['abcd','abce','abcde'],[r'$R_{abcd}$',r'$R_{abce}$',r'$R_{abcd}+R_{abce}$']):
  support_nodes(ax,active,'abcde');title(ax,cap);text(ax,0,-1.22,f'r = 2,  |U| = {len(active)}',16)
 f.text(.343,.5,'+',fontsize=23,color=INK);f.text(.665,.5,'=',fontsize=23,color=INK)
 return f

def box(l):
 f=plt.figure(figsize=(13,5.7));ax=f.add_axes([.02,.12,.53,.77]);setup(ax,(-1,3.6),(-.5,3.3))
 p=np.array([2.1,0]);q=np.array([.65,.9]);r=np.array([-.25,2.1]);zero=np.zeros(2)
 ps={'a':zero,'d₁':p,'c₁':q,'a₁':r,'b':p+q,'c':q+r,'d':p+r,'b₁':p+q+r}
 coords={tuple(v):k for k,v in ps.items()}
 for v in list(ps.values()):
  for u in [p,q,r]:
   other=v+u
   name=next((k for k,w in ps.items() if np.allclose(w,other)),None)
   if name:edge(ax,v,other,GRAY,lw=1.3,ls='--')
 for pairs,col in [([('a','b'),('c','d')],BLUE),([('a','c'),('b','d')],ORANGE),([('a','d'),('b','c')],TEAL)]:
  for a,b in pairs:edge(ax,ps[a],ps[b],col,lw=2.8)
 offsets={'a':(-.12,-.2),'b':(.16,.05),'c':(-.15,.12),'d':(.12,.15),'a₁':(-.18,0),'b₁':(.13,.15),'c₁':(-.16,-.16),'d₁':(.15,-.16)}
 for k,v in ps.items():
  ax.add_patch(Circle(v,.035,fc=INK));text(ax,*(v+offsets[k]),k,15)
 title(ax,tr(l,'Тетраэдр в параллелепипеде','Tetrahedron in a parallelepiped'))
 for j,(u,v,label,caption,col) in enumerate([(p,q,r'$F_1$','p, q',BLUE),(q,r,r'$F_2$','q, r',ORANGE),(p,r,r'$F_3$','p, r',TEAL)]):
  a=f.add_axes([.59,.69-j*.27,.36,.23]);setup(a,(-1,3.4),(-.6,3.2));verts=[zero,u,u+v,v];a.add_patch(Polygon(verts,fc=col,ec=col,alpha=.22,lw=2));center=(u+v)/2;text(a,*center,label,17,color=col);text(a,3.2,1.0,caption,14,ha='left')
 f.text(.76,.96,tr(l,'Три площади граней','Three face areas'),ha='center',color=INK,fontsize=16,weight='bold')
 return f

BUILDERS=[seven,box,merge,blocks,crossing,pairing,cycle,groves,support,transfer,support_sum]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path('.'));ap.add_argument('--preview',type=Path);args=ap.parse_args()
 for lang in ['ru','en']:
  for fn in BUILDERS:
   f=fn(lang);dest=args.root/PREFIX[lang]/(NAMES[fn.__name__][lang=='en']+'.svg');dest.parent.mkdir(parents=True,exist_ok=True);f.savefig(dest,metadata={'Date':None,'Description':NAMES[fn.__name__][lang=='en']});dest.write_text(dest.read_text(encoding='utf8'),encoding='utf8',newline='\n')
   if args.preview:
    args.preview.mkdir(parents=True,exist_ok=True);f.savefig(args.preview/(lang+'-'+fn.__name__+'.png'),dpi=110)
   plt.close(f)
 print('Generated 22 SVG files (11 figures in two languages).')
if __name__=='__main__':main()
