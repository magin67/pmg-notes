"""Reproduce the bilingual editorial figures without network access."""
from pathlib import Path
import argparse,math,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none','svg.hashsalt':'pmg-metric-editorial-2026-11-08','axes.unicode_minus':False,'figure.facecolor':'white','savefig.facecolor':'white','mathtext.fontset':'dejavusans'})
BLUE='#236c9e'; ORANGE='#c06721'; TEAL='#158174'; RED='#b74938'; INK='#243c50'; GRAY='#a8b5c0'; LIGHT='#e9f2f8'
NAMES={
 'radius':('Радиус, диаметр и хорда','Radius, Diameter, and Chord'),
 'projection':('Проекция центра на сторону','Projecting the Center onto a Side'),
 'centralities':('Три центральности пути','Three Centralities of a Path'),
 'reference':('Граф и эталон компактности','A Graph and Its Compactness Reference'),
 'adding':('Добавление связи в двудольном графе','Adding an Edge to a Bipartite Graph'),
 'deletion':('Два вида удаления вершины','Two Types of Vertex Removal'),
 'trees':('Три остова треугольника','Three Spanning Trees of a Triangle'),
 'weak':('Слабые связи и дисбаланс степеней','Weak Edges and Degree Imbalance'),
 'potential':('Потенциал степеней на пути','Degree Potential on a Path'),
 'flow':('Равные потенциалы треугольника','Equal Potentials in a Triangle'),
 'hidden':('Треугольник и скрытый центр','A Triangle and a Hidden Center'),
 'ranking':('Потенциал степеней - расхождение ранжирований','Degree Potential - Ranking Disagreement')}
PREFIX={'ru':'pmg-library/ru/Резистивная геометрия и дуальность/Метрические параметры/images','en':'pmg-library/en/Resistance Geometry and Duality/Metric parameters/images'}

def tr(lang,a,b):return a if lang=='ru' else b
def canvas(n=1,width=10.8,height=3.8):
 f,axs=plt.subplots(1,n,figsize=(width,height),squeeze=False)
 for ax in axs.flat:ax.set_aspect('equal');ax.axis('off')
 return f,list(axs.flat)
def txt(ax,x,y,s,size=13,color=INK,**kw):return ax.text(x,y,s,fontsize=size,color=color,ha=kw.pop('ha','center'),va=kw.pop('va','center'),**kw)
def edge(ax,p,q,label=None,color=BLUE,lw=2,style='-',dy=.1):
 ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=lw,ls=style,zorder=1)
 if label is not None:
  m=(np.array(p)+q)/2;txt(ax,m[0],m[1]+dy,label,12,bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
def node(ax,p,label,color=BLUE,fill='white',r=.12):
 ax.add_patch(Circle(p,r,ec=color,fc=fill,lw=1.8,zorder=5));txt(ax,*p,label,13,color,zorder=6)
def arrow(ax,p,q,color=ORANGE,both=False,shrink=0):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle='<->' if both else '-|>',mutation_scale=18,linewidth=2,color=color,shrinkA=shrink,shrinkB=shrink,zorder=3))
def title(ax,s):ax.set_title(s,fontsize=15,fontweight='bold',color=INK,pad=12)
def limits(ax,x=(-1.45,1.45),y=(-1.1,1.4)):ax.set_xlim(*x);ax.set_ylim(*y)
def network(ax,pos,edges,labels=None,colors=None):
 for i,(u,v) in enumerate(edges):edge(ax,pos[u],pos[v],None if labels is None else labels[i])
 for v,p in pos.items():node(ax,p,v,**((colors or {}).get(v,{})))

def radius(lang):
 f,a=canvas(2,height=4.4);p={'a':(-.9,-.3),'b':(.9,-.3),'c':(0,1)}
 network(a[0],p,[('a','b'),('a','c'),('b','c')],['1','1','1']);title(a[0],tr(lang,'Исходная сеть','Original network'));limits(a[0])
 txt(a[0],0,-.85,r'$R_{ij}=2/3$')
 ax=a[1];ax.add_patch(Circle((0,0),1,ec=BLUE,fc='none',lw=1.6,ls='--'))
 pts=[(math.cos(t),math.sin(t)) for t in np.deg2rad([210,330,90])]
 for i in range(3):edge(ax,pts[i],pts[(i+1)%3],color=INK,lw=2)
 for p,l in zip(pts,'abc'):node(ax,p,l,r=.07)
 arrow(ax,(-1,0),(1,0),RED,True);arrow(ax,(0,0),pts[2],TEAL)
 node(ax,(0,0),'O',r=.07);txt(ax,.12,.55,r'$R_{\mathrm{sph}}$',12,color=TEAL,ha='left')
 txt(ax,0,-1.22,r'$R_{\mathrm{sph}}=\sqrt{2/9}$',12,color=TEAL)
 txt(ax,0,-.2,r'$2R_{\mathrm{sph}}=\sqrt{8/9}$',12,RED)
 txt(ax,0,-.72,r'$|ab|=\sqrt{2/3}$',12)
 title(ax,tr(lang,'Резистивный треугольник','Resistance triangle'));limits(ax,(-1.38,1.65),(-1.42,1.3))
 f.subplots_adjust(wspace=.24,top=.84,bottom=.12)
 return f

def projection(lang):
 f,aa=canvas(height=4.8,width=8);ax=aa[0];O=(0,0);H=(0,-.5);a=(-math.sqrt(3)/2,-.5);b=(math.sqrt(3)/2,-.5);c=(0,1)
 ax.add_patch(Circle(O,1,ec=GRAY,fc='none',lw=1.8,ls='--'))
 for p,q in [(a,b),(a,c),(b,c)]:edge(ax,p,q,color=INK,lw=1.5)
 arrow(ax,O,a,BLUE);arrow(ax,H,a,TEAL);arrow(ax,O,H,ORANGE)
 ax.plot([-.11,-.11,0],[-.5,-.39,-.39],color=GRAY,lw=1.5)
 for p,l in [(a,'a'),(b,'b'),(c,'c')]:node(ax,p,l,r=.06)
 ax.plot(*O,'o',color=BLUE);ax.plot(*H,'o',color=TEAL)
 txt(ax,.15,.1,r'$O_A$',14);txt(ax,.17,-.61,r'$O_C$',14)
 txt(ax,-.52,-.1,r'$R_A$',14,BLUE);txt(ax,-.45,-.65,r'$R_C$',14,TEAL);txt(ax,.1,-.27,r'$d$',14,ORANGE)
 txt(ax,0,-1.18,r'$R_A^2=R_C^2+d^2$',15)
 title(ax,tr(lang,'Центр поднабора как проекция','The subset center as a projection'));limits(ax,(-1.4,1.4),(-1.33,1.2));f.tight_layout()
 return f

def centralities(lang):
 f,aa=canvas(width=11.8,height=4.8);ax=aa[0]
 rows=[(tr(lang,'Центроидная','Centroid'),np.array([1,2,3,2,1])/9,TEAL),
       (tr(lang,'Остовная','Spanning-tree'),np.array([1,2,2,2,1])/8,ORANGE),
       (tr(lang,'Спектральная','Eigenvector'),np.array([1,np.sqrt(3),2,np.sqrt(3),1])/(4+2*np.sqrt(3)),BLUE)]
 for k,(name,v,color) in enumerate(rows):
  y=2.7-1.1*k;txt(ax,-.9,y,name,14,ha='right')
  for i in range(4):edge(ax,(i,y),(i+1,y),color=GRAY)
  for i,val in enumerate(v):node(ax,(i,y),str(i+1),color,fill=LIGHT,r=.15);txt(ax,i,y-.4,f'{100*val:.1f}%',13)
 limits(ax,(-2.5,4.5),(-.1,3.25));title(ax,tr(lang,'Путь P₅: одинаковый граф, разные оценки','Path P₅: one graph, different scores'));f.tight_layout()
 return f

def reference(lang):
 f,aa=canvas(2,height=3.8);p={'a':(-1,0),'b':(0,.85),'c':(1,0)}
 network(aa[0],p,[('a','b'),('b','c')],['1','1']);network(aa[1],p,[('a','b'),('b','c'),('a','c')],['2/3']*3)
 for ax in aa:limits(ax,y=(-.85,1.1));txt(ax,0,-.45,r'$n=3,\quad C=2$')
 title(aa[0],tr(lang,'Исследуемый путь','The path'));title(aa[1],tr(lang,'Полный эталон','Complete reference'))
 txt(aa[0],0,-.75,r'$\rho=1/2,\quad\eta_\rho=2/3$');txt(aa[1],0,-.75,r'$\rho_*=1/3$');f.tight_layout();return f

def adding(lang):
 f,aa=canvas(2,height=4.7,width=11.8);p={'a':(-.9,.6),'b':(-.9,-.6),'c':(.9,.95),'d':(.9,0),'e':(.9,-.95)}
 network(aa[0],p,[(u,v) for u in 'ab' for v in 'cde']);edge(aa[0],p['a'],p['b'],color=RED,lw=3)
 txt(aa[0],-1.22,0,r'$t$',15,RED);limits(aa[0],(-1.5,1.3),(-1.3,1.35));title(aa[0],tr(lang,'Новая связь внутри доли','New edge within one part'))
 txt(aa[0],0,-1.2,tr(lang,'Остальные проводимости: 1','Other conductances: 1'),12)
 ax=aa[1];ax.set_aspect('auto');limits(ax,(-.1,3.2),(-.2,3.2));title(ax,tr(lang,'Две причины изменения','Two sources of change'))
 txt(ax,1.2,2.9,tr(lang,'До','Before'),13);txt(ax,2.6,2.9,tr(lang,'После (t = 1)','After (t = 1)'),13)
 rows=[(r'$\rho$',r'$1/3$',r'$17/50$'),(r'$\rho_*$',r'$4/15$',r'$8/35$'),(r'$\eta_\rho$',r'$4/5$',r'$80/119$'),(r'$Kf$',r'$23/3$',r'$7$'),(r'$Kf_*$',r'$20/3$',r'$40/7$'),(r'$\eta_K$',r'$20/23$',r'$40/49$')]
 for i,(label,before,after) in enumerate(rows):
  y=2.45-.43*i;txt(ax,.15,y,label,15);txt(ax,1.2,y,before,15);txt(ax,2.6,y,after,15)
 f.subplots_adjust(wspace=.32,top=.83,bottom=.08);return f

def deletion(lang):
 f,aa=canvas(3,width=11.8,height=3.9);p={'a':(-.9,0),'b':(.9,0),'c':(0,1)}
 network(aa[0],p,[('a','b'),('a','c'),('b','c')],['1']*3)
 for ax,c in zip(aa[1:],['1','3/2']):network(ax,{k:p[k] for k in 'ab'},[('a','b')],[c])
 for ax in aa:limits(ax,(-1.2,1.2),(-.9,1.35))
 for ax,t in zip(aa,[tr(lang,'Исходный треугольник','Original triangle'),tr(lang,'Удаление c','Delete c'),tr(lang,'Исключение c','Eliminate c')]):title(ax,t)
 for ax,rs,rho in zip(aa,['2/3','1','2/3'],['2/9','1/4','1/6']):txt(ax,0,-.4,'$R_{ab}='+rs+'$');txt(ax,0,-.72,r'$\rho='+rho+'$')
 f.tight_layout(w_pad=1.3);return f

def trees(lang):
 f,aa=canvas(3,width=11.4,height=4);p={'a':(0,.8),'b':(-.8,-.35),'c':(.8,-.35)};all_edges=[('a','b'),('a','c'),('b','c')]
 for k,ax in enumerate(aa):
  chosen=[all_edges[i] for i in [[0,1],[0,2],[1,2]][k]]
  for u,v in all_edges:edge(ax,p[u],p[v],color=BLUE if (u,v) in chosen else GRAY,style='-' if (u,v) in chosen else '--',lw=2.5 if (u,v) in chosen else 1)
  for v,pos in p.items():node(ax,pos,v,ORANGE if v=='a' else BLUE,fill='#fff2e5' if v=='a' else 'white')
  limits(ax,(-1.15,1.15),(-1.2,1.1));title(ax,r'$P=1/3$')
  txt(ax,0,-.76,tr(lang,'Степень a: ','Degree of a: ')+str([2,1,1][k]),13)
  txt(ax,0,-1.08,tr(lang,'Ребро ab: ','Edge ab: ')+tr(lang,['есть','есть','нет'][k],['present','present','absent'][k]),12)
 f.tight_layout(w_pad=2);return f

def weak(lang):
 f,aa=canvas(2,width=11.6,height=4.4)
 for ax,n in zip(aa,[3,4]):
  xs=np.linspace(-1.25,1.25,n);ps=[(x,.25) for x in xs]
  weakidx=1
  for i in range(n-1):edge(ax,ps[i],ps[i+1],r'$\varepsilon$' if i==weakidx else '1',color=RED if i==weakidx else BLUE,dy=.2)
  for i,pos in enumerate(ps):node(ax,pos,str(i+1),fill=LIGHT,r=.12)
  if n==3:
   arrow(ax,(-1.1,-.02),(-.15,-.02));arrow(ax,(.15,-.02),(1.1,-.02));txt(ax,0,-.4,r'$B_{\{1,2\}}=(2-\varepsilon)/3$',13);txt(ax,0,-.82,r'$\Delta_L\sim1/(9\varepsilon)$',15)
  else:
   arrow(ax,(-.55,-.02),(-1.1,-.02));arrow(ax,(.55,-.02),(1.1,-.02));txt(ax,0,-.4,r'$B_{\{1,2\}}=0$',13);txt(ax,0,-.82,r'$\Delta_L=\varepsilon^2/8$',15)
  limits(ax,(-1.5,1.5),(-1.2,.95))
 title(aa[0],tr(lang,'Есть ток через слабое ребро','Current crosses the weak edge'));title(aa[1],tr(lang,'Через мост ток равен нулю','Zero current across the bridge'))
 f.text(.5,.05,r'$0<\varepsilon<1/2,\quad\varepsilon\to0^+$',ha='center',fontsize=13,color=INK);f.subplots_adjust(top=.79,bottom=.13,wspace=.25);return f

def potential(lang):
 f,aa=canvas(width=9.8,height=4.3);ax=aa[0];p={'a':(-1.5,.75),'b':(0,.75),'c':(1.5,.75)}
 network(ax,p,[('a','b'),('b','c')],['1','1'],{'b':{'color':ORANGE,'fill':'#fff2e5'}})
 arrow(ax,(-.15,.48),(-1.35,.48));arrow(ax,(.15,.48),(1.35,.48));txt(ax,-.75,.25,r'$1/3$',12);txt(ax,.75,.25,r'$1/3$',12)
 for y,label in [(0,r'$d=(1,2,1)$'),(-.35,r'$b=(-1,2,-1)/3$'),(-.7,r'$\varphi=(-1,2,-1)/9$'),(-1.05,r'$\beta=(5/18,4/9,5/18)$')]:txt(ax,0,y,label,14)
 limits(ax,(-2.4,2.4),(-1.3,1.2));title(ax,tr(lang,'От степеней к потенциалу','From degrees to potential'));f.tight_layout();return f

def flow(lang):
 f,aa=canvas(width=11,height=3.8);ax=aa[0];p={'a':(-2,.7),'b':(-2,-.7),'c':(-.9,0),'d':(.6,0),'e':(2.1,0)}
 network(ax,p,[('a','b'),('a','c'),('b','c'),('c','d'),('d','e')],colors={v:{'color':BLUE,'fill':LIGHT} for v in 'abc'})
 arrow(ax,(-.72,.25),(.42,.25));arrow(ax,(.78,.25),(1.92,.25));txt(ax,-.15,.48,'1',12);txt(ax,1.35,.48,'1',12)
 txt(ax,-2.8,0,r'$\varphi=3/5$',13);txt(ax,-.9,-.48,r'$b_c=1$',13,ORANGE);txt(ax,.6,-.48,r'$\varphi_d=-2/5$',13);txt(ax,2.1,-.48,r'$b_e=-1$',13,ORANGE)
 txt(ax,2.1,-.85,r'$\varphi_e=-7/5$',13);txt(ax,-2,-1.02,tr(lang,'Треугольник равнопотенциален','Equal potential in the triangle'),12)
 limits(ax,(-3.7,2.8),(-1.2,1.1));title(ax,tr(lang,'Треугольник с присоединённым путём','A triangle with an attached path'));f.tight_layout();return f

def hidden(lang):
 f,aa=canvas(2,width=10.5,height=4.4);p={'a':(0,1),'b':(-.9,-.45),'c':(.9,-.45)}
 network(aa[0],p,[('a','b'),('a','c'),('b','c')],['1']*3)
 p2={**p,'d':(0,.1)};network(aa[1],p2,[('a','d'),('b','d'),('c','d')],['3']*3,{'d':{'color':ORANGE,'fill':'#fff2e5'}})
 title(aa[0],tr(lang,'Связи между наблюдаемыми','Edges between observed vertices'));title(aa[1],tr(lang,'Связи через скрытый центр','Edges through a hidden center'))
 for ax,mu in zip(aa,[2,0]):limits(ax,(-1.35,1.35),(-1.2,1.3));txt(ax,0,-.85,r'$\mu_G(\{a,b,c\})='+str(mu)+'$',14)
 f.text(.5,.035,r'$R_{ab}=R_{ac}=R_{bc}=2/3$',ha='center',fontsize=14,color=INK);f.subplots_adjust(top=.84,bottom=.12,wspace=.3);return f

def ranking(lang):
 f,aa=plt.subplots(1,2,figsize=(11.2,4),gridspec_kw={'width_ratios':[1,1.65]});ax=aa[0];ax.set_aspect('equal');ax.axis('off')
 p={'a':(-1.5,0),'b':(-.5,0),'c':(1,0),'d':(.25,.9),'e':(.25,-.9)};es=[('a','b'),('b','c'),('b','d'),('b','e'),('c','d'),('c','e')]
 network(ax,p,es);limits(ax,(-1.8,1.3),(-1.2,1.2));title(ax,tr(lang,'Конечный граф: ε = 1','Final graph: ε = 1'))
 vals=[];xs=np.linspace(0,1,251);E={tuple(sorted(('abcde'.index(a),'abcde'.index(b)))) for a,b in es}
 for eps in xs:
  A=np.zeros((5,5))
  for i in range(5):
   for j in range(i+1,5):A[i,j]=A[j,i]=1 if (i,j) in E else 1-eps
  d=A.sum(1);L=np.diag(d)-A;beta=np.ones(5)/5+.5*np.linalg.pinv(L)@(d-d.mean());ev,V=np.linalg.eigh(A);v=V[:,-1];v=v/v.sum();vals.append((beta[1]-beta[2],2.5*(v[1]-v[2])))
 ax=aa[1];v=np.array(vals);ax.plot(xs,v[:,0],color=BLUE,lw=2,label=r'$\beta^b-\beta^c$');ax.plot(xs,v[:,1],color=ORANGE,lw=2,label=r'$(5/2)(v_b-v_c)$');root=(35-5*np.sqrt(17))/16
 ax.axhline(0,color=GRAY,lw=1);ax.axvline(root,color=GRAY,ls=':');ax.set_xlim(0,1);ax.grid(alpha=.15);ax.legend(frameon=False,fontsize=11);ax.set_xlabel(tr(lang,'ε: ослабление четырёх связей','ε: weakening four edges'),fontsize=12);ax.set_ylabel(tr(lang,'Разность оценок b и c','Score difference: b minus c'),fontsize=12);title(ax,tr(lang,'От K₅ к конечному графу','From K₅ to the final graph'));f.tight_layout();return f

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',default='.');ap.add_argument('--preview');args=ap.parse_args();root=Path(args.root);preview=Path(args.preview) if args.preview else None
 if preview:preview.mkdir(parents=True,exist_ok=True)
 results=[]
 for lang in ['ru','en']:
  dest=root/PREFIX[lang];dest.mkdir(parents=True,exist_ok=True)
  for key in NAMES:
   figure=globals()[key](lang);name=NAMES[key][lang=='en'];path=dest/(name+'.svg')
   figure.savefig(path,format='svg',metadata={'Date':None,'Creator':'PMG editorial figures'})
   path.write_text(path.read_text(encoding='utf8'),encoding='utf8',newline='\n')
   if preview:figure.savefig(preview/f'{lang}-{key}.png',dpi=120)
   plt.close(figure);results.append(str(path))
 print(json.dumps({'figures':len(results),'root':str(root)},ensure_ascii=True))

if __name__=='__main__':main()
