"""Draw two vector figures from independently checked rational data."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[2]
out=root/'pmg-library/ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/images'
out.mkdir(parents=True,exist_ok=True)
preview=root.parent/'path-polyform-research/influence-preview'
preview.mkdir(parents=True,exist_ok=True)
data=json.loads(Path(__file__).with_name('influence-results.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
blue='#246585';orange='#bf651f';gray='#657587'
pos={'a':(0,0),'b':(1,1.05),'c':(2,0)}


def triangle(ax,weights,changed=None,candidate=False):
    for edge in ['ab','bc','ac']:
        p,q=[pos[x] for x in edge]
        color=orange if edge==changed else blue
        if edge=='ac' and candidate:
            ax.plot([p[0],q[0]],[p[1],q[1]],color=orange,lw=2,ls='--',zorder=1)
        elif weights.get(edge,0):
            ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=4 if edge==changed else 2.5,zorder=1)
        textpos={'ab':(.32,.65),'bc':(1.68,.65),'ac':(1,-.16)}[edge]
        label='нет связи' if edge=='ac' and candidate else str(weights.get(edge,''))
        if label:
            ax.text(*textpos,label,ha='center',va='center',color=color,
                    bbox={'facecolor':'white','edgecolor':'none','pad':2})
    for name,p in pos.items():
        ax.scatter(*p,s=550,facecolor='white',edgecolor=gray,zorder=3)
        ax.text(*p,name,ha='center',va='center',zorder=4,fontsize=14)
    ax.set(xlim=(-.4,2.4),ylim=(-.75,1.52),aspect='equal')
    ax.axis('off')


def save(fig,name,desc):
    fig.savefig(out/(name+'.svg'),bbox_inches='tight',metadata={'Title':name,'Description':desc})
    fig.savefig(preview/(name+'.png'),bbox_inches='tight',dpi=160)
    plt.close(fig)


fig,axes=plt.subplots(1,2,figsize=(10,4.3))
triangle(axes[0],{'ab':1,'bc':1},candidate=True)
triangle(axes[1],{'ab':1,'bc':1,'ac':1},changed='ac')
axes[0].set_title('Исходная цепочка',fontsize=14)
axes[1].set_title('Добавлена связь ac проводимости 1',fontsize=14)
axes[0].text(1,-.50,r'$N([(ac)]^2)=2$',ha='center',fontsize=16)
axes[1].text(1,-.50,r'$N^{\prime}([(ac)]^2)=2/3$',ha='center',fontsize=16)
fig.suptitle('Одна форма в двух метриках',fontsize=18)
fig.text(.5,.04,r'$N_t([(ac)]^2)=2/(1+2t),\qquad \Delta_{ac}(1)=-4/3$',ha='center',fontsize=14)
fig.subplots_adjust(top=.78,bottom=.18,wspace=.25)
save(fig,'Добавление связи к цепочке','Цепочка a-b-c с единичными проводимостями и треугольник после добавления единичной связи ac. Значение формы меняется с 2 до 2/3.')

fig,axes=plt.subplots(1,3,figsize=(12,4.7))
for ax,row in zip(axes,data['triangle_probes']):
    weights={'ab':1,'bc':1,'ac':1};weights[row['edge']]=2
    triangle(ax,weights,changed=row['edge'])
    ax.set_title(row['edge']+': 1 → 2',fontsize=15)
    labels=[r'$N^{\prime}(f)='+row['new_value']+'$',
            r'$\Delta(1;f)='+row['change']+'$',r'$m='+row['m']+'$']
    for y,t in zip([-.37,-.63,-.89],labels):
        ax.text(1,y,t,ha='center',fontsize=14)
    ax.set_ylim(-1.05,1.45)
fig.suptitle('Три независимые пробы для f = [(ac)]²',fontsize=18,y=.99)
fig.text(.5,.88,'Исходный граф в каждой пробе: единичный треугольник, N(f) = 2/3',ha='center',fontsize=13,color=gray)
fig.subplots_adjust(top=.79,bottom=.08,wspace=.12)
save(fig,'Поле влияния на треугольнике','Каждая проводимость отдельно увеличивается с 1 до 2. Новые значения формы: 3/5, 3/5, 2/5; влияния: -1/15, -1/15, -4/15; коэффициенты: 1/9, 1/9, 4/9.')
