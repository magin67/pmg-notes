from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
BLUE='#176b9b';ORANGE='#b65422';GRAY='#44536a'
NAMES={'chain':('Взвешенная цепочка','Weighted chain'),'triangle':('Векторы резистивного треугольника','Vectors of the resistance triangle'),'variation':('Усиление связей треугольника','Strengthening triangle couplings'),'forests':('Путь и цикл в лесном разложении','Path and cycle in the forest expansion'),'deletion':('Удаление ребра и моста','Deleting an edge and a bridge')}
def node(ax,x,y,label):
 if isinstance(label,int):label="abcde"[label-1]
 ax.plot(x,y,'o',ms=19,color='white',markeredgecolor=GRAY,markeredgewidth=2,zorder=5)
 ax.text(x,y,str(label),ha='center',va='center',fontsize=11,zorder=6)
def edge(ax,a,b,label=None,dashed=False):
 ax.plot([a[0],b[0]],[a[1],b[1]],color=ORANGE if dashed else BLUE,lw=2.6,ls='--' if dashed else '-')
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.13,label,ha='center',va='bottom',bbox={'facecolor':'white','edgecolor':'none','pad':1})
def finish(ax):ax.axis('off');ax.set_aspect('equal')
def graph(ax,pos,edges,title):
 for a,b,w in edges:edge(ax,pos[a],pos[b],str(w) if w else None)
 for a,(x,y) in pos.items():node(ax,x,y,a)
 ax.set_title(title,pad=18);ax.margins(.25);finish(ax)
def make(key,ru):
 if key=='chain':
  fig,ax=plt.subplots(figsize=(9,3.3));p={1:(0,0),2:(2,0),3:(4,0)}
  graph(ax,p,[(1,2,'c₁₂ = 1 S'),(2,3,'c₂₃ = 2 S')], 'Цепочка: проводимости, ток и потенциалы' if ru else 'Chain: conductances, current, and potentials')
  for x,v in [(0,3),(2,1),(4,0)]:ax.text(x,-.38,f'φ = {v} V',ha='center')
  for x in [.5,2.5]:ax.annotate('',(x+1,.65),(x,.65),arrowprops={'arrowstyle':'-|>','mutation_scale':24,'color':ORANGE,'lw':2});ax.text(x+.5,.8,'I = 2 A',ha='center')
  ax.set(xlim=(-.5,4.5),ylim=(-.75,1.25))
 elif key=='triangle':
  fig,axs=plt.subplots(1,2,figsize=(10,4.3));h=np.sqrt(3)/2
  for ax in axs:finish(ax);ax.set(xlim=(-.25,1.3),ylim=(-.2,1.25))
  p={'a':(0,0),'b':(1,0),'c':(.5,h)}
  for a,b in [('a','b'),('a','c'),('b','c')]:
   x,y=p[a],p[b];axs[0].annotate('',y,x,arrowprops={'arrowstyle':'-|>','mutation_scale':24,'color':BLUE,'lw':2.4})
  for a,(x,y) in p.items():node(axs[0],x,y,a)
  axs[0].text(.5,-.15,'u = b − a',ha='center');axs[0].text(-.02,.45,'v',ha='center');axs[0].text(.9,.45,'w',ha='center')
  axs[0].set_title('Резистивный треугольник' if ru else 'Resistance triangle')
  axs[0].text(.5,1.1,'u² = v² = w² = 2/3',ha='center')
  ax=axs[1];o=(.7,.15)
  for end,label,off in [((1.2,.15),'u',(.95,.02)),((.45,.15+h/2),'w',(.36,.6))]:
   ax.annotate('',end,o,arrowprops={'arrowstyle':'-|>','mutation_scale':24,'color':BLUE,'lw':2.4});ax.text(*off,label)
  ax.text(.75,.48,'120°',ha='center');ax.text(.7,-.12,'u · w = −1/3',ha='center');ax.set_title('Свободные векторы' if ru else 'Free vectors')
 elif key=='variation':
  fig,axs=plt.subplots(1,3,figsize=(11,3.5));p={1:(0,0),2:(1.6,0),3:(.8,1.3)}
  for ax,weights,tau,title in zip(axs,[(1,1,1),(2,1,1),(2,2,1)],[3,5,8],['Исходный граф','Одна связь','Две связи'] if ru else ['Original graph','One coupling','Two couplings']):
   graph(ax,p,[(1,2,weights[0]),(1,3,weights[1]),(2,3,weights[2])],title)
   ax.text(.8,-.45,f'τ = {tau}',ha='center');ax.set_ylim(-.6,1.7)
 elif key=='forests':
  fig,axs=plt.subplots(1,2,figsize=(10,3.5));p={i:(i-1,0) for i in range(1,6)}
  graph(axs[0],p,[(i,i+1,None) for i in range(1,5)],'P₅: τ = 1');axs[0].text(2,-.6,'sₖ: 1, 4, 6, 4, 1',ha='center');axs[0].set_ylim(-1,1)
  p={1:(0,0),2:(1.4,0),3:(1.4,1.4),4:(0,1.4)}
  graph(axs[1],p,[(1,2,None),(2,3,None),(3,4,None),(4,1,None)],'C₄: τ = 4');axs[1].text(.7,-.55,'sₖ: 1, 4, 6, 4, 0',ha='center')
 elif key=='deletion':
  fig,axs=plt.subplots(1,2,figsize=(10,4));p={1:(0,0),2:(1.5,0),3:(1.5,1.5),4:(0,1.5)}
  graph(axs[0],p,[(1,4,None),(4,3,None),(3,2,None)],'Ребро цикла удалено' if ru else 'Cycle edge deleted');edge(axs[0],p[1],p[2],dashed=True)
  axs[0].text(.75,-.6,'τ = 1, R₁₂ = 3',ha='center')
  p={1:(0,.6),2:(1.5,.6),3:(3,.6)}
  graph(axs[1],p,[(1,2,'c = 1')],'Мост удалён' if ru else 'Bridge deleted');edge(axs[1],p[2],p[3],dashed=True)
  axs[1].text(1.5,-.2,'τ = 0',ha='center');axs[1].text(1.5,-.65,'Нет глобальной нормировки' if ru else 'No global normalization',ha='center',fontsize=12);axs[1].set_ylim(-1,1.8)
 fig.tight_layout(pad=1.6);return fig
if __name__=='__main__':
 for lang in ('ru','en'):
  out=ROOT/'pmg-library'/lang/'PythonExamples/images';out.mkdir(parents=True,exist_ok=True)
  preview=ROOT/'checks/pythonexamples/previews';preview.mkdir(exist_ok=True)
  for key,names in NAMES.items():
   fig=make(key,lang=='ru');fig.savefig(out/(names[lang=='en']+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Date':None});fig.savefig(preview/f'{key}-{lang}.png',dpi=110,bbox_inches='tight');plt.close(fig)
 print('Generated 10 bilingual SVG diagrams.')
