"""Three reproducible editorial figures; translations share data and geometry.

Run verify_editorial_examples.py first, then this script and draw_english.py.
"""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from draw_three_hexagons import SVG,OUT,INK,MUTED,RED,BLUE,GREEN
from draw_slr_code import draw_chain,geometry

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'editorial-examples-results.json').read_text(encoding='utf-8'))
LABELS={}
def tr(ru,en):LABELS[ru]=en;return ru
def register(source,target):
    path=HERE/'figure-labels-en.json';entries=json.loads(path.read_text(encoding='utf-8'))
    root=ET.parse(OUT/source).getroot()
    needed={v for e in root.iter() for v in [e.text,e.tail] if v and re.search('[А-Яа-яЁё]',v)}
    assert needed<=set(LABELS),(source,needed-set(LABELS))
    entry={'source':source,'target':target,'labels':{v:LABELS[v] for v in sorted(needed)}}
    entries=[e for e in entries if e['source']!=source]+[entry]
    path.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def spectra():
    title=tr('Два графа - два лапласовских спектра','Two graphs, two Laplacian spectra')
    desc=tr('По 14 собственных значений на одной шкале. Общий нуль выделен кольцом; положительные значения вычислены приближённо.','Fourteen eigenvalues per graph on a shared scale. A ring marks the shared zero; positive values are approximated.')
    with plt.rc_context({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'none','svg.hashsalt':'isomer-spectra-editorial'}):
        fig,ax=plt.subplots(figsize=(12,4.8));fig.patch.set_facecolor('white');ax.set_facecolor('#f7f9fc')
        for key,y,color in [('A',1,BLUE),('B',0,RED)]:
            values=DATA['spectra_for_plot'][key]
            ax.hlines(y,0,5.3,color='#dce4ed',linewidth=1)
            ax.scatter(values,[y]*14,marker='|',s=500,linewidth=2.8,color=color,zorder=3)
            ax.scatter([0],[y],s=130,facecolors='white',edgecolors=INK,linewidths=2,zorder=4)
        ax.set_yticks([1,0],[tr('А: прямая цепь','A: straight chain'),tr('Б: смещённый шов','B: shifted seam')])
        ax.set_xlim(-.08,5.35);ax.set_ylim(-.5,1.5);ax.set_xticks(range(6));ax.grid(axis='x',color='#dce4ed');ax.set_axisbelow(True)
        ax.set_xlabel(tr('Собственное значение λ','Eigenvalue λ'),labelpad=12)
        ax.set_title(title,loc='left',pad=22,fontsize=22)
        for side in ['top','right','left']:ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#aab7c6');ax.tick_params(axis='y',length=0,pad=12)
        fig.text(.5,.055,tr('Общий нуль; 13 положительных значений в каждой строке','A shared zero; 13 positive values in each row'),ha='center',fontsize=15,color=MUTED)
        fig.subplots_adjust(left=.23,right=.97,top=.77,bottom=.27)
        fig.savefig(OUT/'Два лапласовских спектра.svg',metadata={'Date':None,'Title':title,'Description':desc})
        plt.close(fig)
    register('Два лапласовских спектра.svg','Two Laplacian Spectra.svg')

def square():
    s=SVG(1200,890,tr('Квадрат смешанной разности','The mixed-difference square'),tr('Независимые S/L-выборы в двух позициях дают четыре цепочки. Знаки: плюс, минус, минус, плюс.','Independent S/L choices at two positions give four chains. The signs are plus, minus, minus, plus.'))
    s.text(600,40,tr('Две позиции - четыре независимых выбора','Two positions, four independent choices'),27,anchor='middle',weight='bold')
    for u,x,y in [('SS',30,75),('SL',670,75),('LS',30,470),('LL',670,470)]:
        plus=u in ['SS','LL'];s.panel(x,y,500,310)
        s.text(x+250,y+40,('+' if plus else '−')+' χ(S'+u+')',29,GREEN if plus else RED,'middle','bold')
        draw_chain(s,u,(x+45,y+65,410,155))
        s.text(x+250,y+275,'P(1) = '+format(DATA['square_values']['S'+u],',').replace(',',' '),22,anchor='middle')
    for y in [230,625]:
        s.arrow((550,y),(650,y));s.text(600,y-22,'u₂',18,MUTED,'middle')
    for x in [280,920]:
        s.arrow((x,400),(x,455));s.text(x+28,435,'u₁',18,MUTED)
    s.text(600,827,'χ(SSS) − χ(SSL) − χ(SLS) + χ(SLL)',25,anchor='middle',weight='bold')
    s.text(600,864,tr('При ξ = −1: −102 487','At ξ = −1: −102 487'),23,BLUE,'middle')
    s.save('Квадрат смешанной разности.svg');register('Квадрат смешанной разности.svg','Mixed Difference Square.svg')

def closeup():
    s=SVG(1200,690,tr('Постоянный поворот крупным планом','A close-up of a constant turn'),tr('Три соседних ядра и два непересекающихся шва среднего ядра. Вход 01 выделен красным, выход 23 синим.','Three adjacent cores and the two disjoint seams of the middle core. Input 01 is red; output 23 is blue.'))
    s.text(600,42,tr('Правило L видно на трёх соседних ядрах','Rule L on three adjacent cores'),28,anchor='middle',weight='bold')
    s.panel(25,72,720,545);s.panel(775,72,400,545)
    p,centers=draw_chain(s,'L',(70,115,620,410))
    # Distinguish core names from the local vertex numbers below.
    for k in range(1,4):
        s.parts=[part.replace('>'+str(k)+'</text>', '>K'+str(k)+'</text>') for part in s.parts]
    points,cores,edges,active=geometry('L');middle=cores[1]
    for pair,color in [((middle[0],middle[1]),RED),((middle[2],middle[3]),BLUE)]:
        s.line(p[pair[0]],p[pair[1]],color,7)
        for v in pair:s.circle(p[v],7,'white',color,2.5)
    cx,cy=centers[1]
    # Local vertex labels are placed slightly inside the middle face.
    for local,v in enumerate(middle):
        x,y=p[v];s.text(cx+.77*(x-cx),cy+.77*(y-cy)+6,str(local),21,INK,'middle','bold')
    s.text(385,583,tr('Цифры у вершин - локальные номера среднего ядра','Vertex labels are local to the middle core'),19,MUTED,'middle')
    s.text(975,132,tr('Вход','Input'),25,RED,'middle','bold')
    s.text(975,177,'(0, 1) = (b, a)',26,RED,'middle')
    s.text(975,252,tr('Выход L','Output L'),25,BLUE,'middle','bold')
    s.text(975,297,'(2, 3)',28,BLUE,'middle')
    s.text(975,380,tr('Следующий шаг','Next step'),24,anchor='middle',weight='bold')
    s.text(975,421,tr('Новый вход снова обращает','The new input again reverses'),20,MUTED,'middle')
    s.text(975,450,tr('порядок активных контактов','the active contact order'),20,MUTED,'middle')
    s.text(975,524,tr('Тот же выход L','The same output L'),24,GREEN,'middle')
    s.text(600,660,tr('Пространственное положение меняется; правило соединения остаётся тем же','Spatial positions may change; the joining rule stays the same'),23,anchor='middle')
    s.save('Постоянный поворот крупным планом.svg');register('Постоянный поворот крупным планом.svg','Constant Turn Close Up.svg')

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    spectra();square();closeup()
    print('Created three diagrams and their English label mappings.')
