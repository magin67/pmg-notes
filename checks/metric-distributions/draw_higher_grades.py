"""Three SVG figures from the exact higher-grade results."""
from fractions import Fraction as Q
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

root = Path(__file__).resolve().parents[2]
out = root / 'pmg-library/ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/images'
preview = root.parent / 'path-polyform-research/higher-grade-preview'
preview.mkdir(parents=True, exist_ok=True)
data = json.loads(Path(__file__).with_name('higher-grade-results.json').read_text(encoding='utf8'))['examples']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'none'})
blue, orange, green, gray = '#246585','#bf651f','#347b65','#677587'
star = {'h':(0,0),'a':(-1,0),'b':(1,0),'c':(0,-1),'d':(0,1)}
square = {'a':(-1,1),'b':(1,1),'c':(1,-1),'d':(-1,-1)}


def save(fig, name, description):
    fig.savefig(out/(name+'.svg'),bbox_inches='tight',metadata={'Title':name,'Description':description})
    fig.savefig(preview/(name+'.png'),bbox_inches='tight',dpi=155)
    plt.close(fig)


def vertices(ax, positions, colors=None):
    colors = colors or {}
    for name, p in positions.items():
        color = colors.get(name, gray)
        ax.scatter(*p,s=600,facecolor='white',edgecolor=color,linewidths=1.8,zorder=4)
        ax.text(*p,name,ha='center',va='center',fontsize=18,color=color,zorder=5)


fig, axes = plt.subplots(1,3,figsize=(10.6,4.6))
case = data['weighted_star']
nonzero = [r for r in case['coefficients'] if Q(r['m'])]
for ax, row in zip(axes,nonzero):
    removed = set(row['edges'])
    attached = next(v for v in 'abc' if 'h'+v not in removed)
    colors = {'a':blue,'b':orange,'c':green}
    colors['h'] = colors['d'] = colors[attached]
    for edge in case['edges']:
        i,j = edge['edge']; p,q = star[i],star[j]
        cut = edge['edge'] in removed
        ax.plot([p[0],q[0]],[p[1],q[1]],color=orange if cut else gray,
                lw=2.5,ls='--' if cut else '-',zorder=1)
        x,y = (p[0]+q[0])/2,(p[1]+q[1])/2
        dx,dy = (.19,0) if x==0 else (0,.20)
        ax.text(x+dx,y+dy,edge['c'],ha='center',va='center',fontsize=16,color=gray)
    vertices(ax,star,colors)
    ax.set_title('Удалены '+', '.join(row['edges']),fontsize=16,pad=12)
    ax.text(0,-1.56,'Вклад = '+row['m'],ha='center',fontsize=19,color=blue)
    ax.set(xlim=(-1.45,1.45),ylim=(-1.75,1.45),aspect='equal');ax.axis('off')
fig.suptitle('Норма (abc)² = 1/2 + 1/3 + 1/6 = 1',fontsize=20,y=.98)
fig.subplots_adjust(top=.77,bottom=.02,left=.02,right=.98,wspace=.10)
save(fig,'Парные вклады треугольника на дереве',
     'Дерево с центром h и листьями a,b,c,d; проводимости ha=1,hb=2,hc=3,hd=1. Удаляемые пары ha,hb; ha,hc; hb,hc имеют вклады 1/2,1/3,1/6. Цвет контура вершины отмечает её компоненту после удаления.')


def square_graph(ax, labels, reinforced=None):
    for edge,label in labels.items():
        i,j = edge; p,q = square[i],square[j]
        marked = edge==reinforced
        ax.plot([p[0],q[0]],[p[1],q[1]],color=orange if marked else blue,
                lw=3.7 if marked else 2.6,zorder=1)
        x,y = (p[0]+q[0])/2,(p[1]+q[1])/2
        dx,dy = (.28*x,.28*y)
        ax.text(x+dx,y+dy,label,ha='center',va='center',fontsize=18,
                color=orange if marked else blue,
                bbox={'facecolor':'white','edgecolor':'none','pad':1},zorder=2)
    vertices(ax,square,{v:blue for v in 'abc'})
    ax.set(xlim=(-1.65,1.65),ylim=(-1.7,1.65),aspect='equal');ax.axis('off')


fig, axes = plt.subplots(1,2,figsize=(9.0,4.8),gridspec_kw={'width_ratios':[1.1,1]})
ax = axes[0]
edges = [row['edge'] for row in data['unit_square']['edges']]
coeff = {tuple(row['edges']):row['m'] for row in data['unit_square']['coefficients']}
for i,e in enumerate(edges):
    for j,f in enumerate(edges):
        valid = j>i
        label = coeff.get((e,f),'')
        face = '#d9e9ef' if valid and label!='0' else '#f1f3f5'
        if label=='1/4':face='#9fc5d4'
        ax.add_patch(Rectangle((j,i),1,1,facecolor=face,edgecolor='white',lw=2))
        ax.text(j+.5,i+.5,label if valid else '·',ha='center',va='center',fontsize=18,
                color='#263d48' if valid else '#a8b2bb')
ax.set(xlim=(0,4),ylim=(4,0),aspect='equal')
ax.set_xticks([i+.5 for i in range(4)],edges);ax.set_yticks([i+.5 for i in range(4)],edges)
ax.xaxis.tick_top();ax.tick_params(length=0,pad=7)
for sp in ax.spines.values():sp.set_visible(False)
ax.set_title('Вклады пар m',fontsize=18,pad=40)
ax.text(2,4.65,'Сумма = 1/2',ha='center',fontsize=18)
square_graph(axes[1],{r['edge']:r['A'] for r in data['unit_square']['edges']})
axes[1].set_title('Влияния связей A',fontsize=18,pad=24)
axes[1].text(0,-1.67,'Сумма = 1',ha='center',fontsize=18)
fig.subplots_adjust(top=.78,bottom=.15,left=.07,right=.98,wspace=.21)
save(fig,'Пары и влияние связей на квадрате',
     'Для X=(abc) на единичном квадрате парные вклады: ab,bc=1/4; ab,cd=ab,ad=bc,cd=bc,ad=1/16; cd,ad=0. Рёберные суммы A_ab=A_bc=3/8, A_cd=A_ad=1/8. Сумма пар 1/2, сумма влияний 1.')


fig, axes = plt.subplots(1,3,figsize=(10.6,4.8))
case = data['unit_square']
by_edge = {r['edge']:r for r in case['edges']}
for ax, edge in zip(axes,(None,'ab','cd')):
    labels = {r['edge']:('2' if r['edge']==edge else '1') for r in case['edges']}
    square_graph(ax,labels,edge)
    ax.set_title('Исходный квадрат' if edge is None else 'Удвоена связь '+edge,fontsize=16,pad=12)
    value = case['value'] if edge is None else by_edge[edge]['doubled_value']
    delta = '' if edge is None else '\nИзменение: '+by_edge[edge]['delta']
    ax.text(0,-1.65,'(abc)² = '+value+delta,ha='center',va='top',fontsize=17,linespacing=1.6)
fig.suptitle('Две независимые пробы нормы треугольника',fontsize=19,y=.98)
fig.subplots_adjust(top=.77,bottom=.15,left=.02,right=.98,wspace=.10)
save(fig,'Пробы нормы треугольника на квадрате',
     'Исходная норма границы (abc) на единичном квадрате равна 1/2. Независимое удвоение ab даёт 2/7 и изменение -3/14; независимое удвоение cd даёт 3/7 и изменение -1/14. Подписи рёбер обозначают проводимости.')
print(json.dumps({'svg_figures':3,'preview_directory':str(preview)},ensure_ascii=False))
