"""Reproducible period diagrams and a growth plot, with incidence checks."""
from pathlib import Path
import json
from draw_three_hexagons import SVG, INK, MUTED, BLUE, RED, GREEN, OUT
from draw_slr_code import draw_chain, geometry
from verify_slr_code import graph

DATA = json.loads(Path(__file__).with_name('periodic-slr-results.json').read_text(encoding='utf-8'))


def checked_chain(s, u, rect):
    pts, cores, edges, boundary = geometry(u)
    g, expected_cores, expected_boundary, _ = graph(u)
    assert cores == expected_cores and boundary == expected_boundary
    assert edges == {tuple(sorted(e)) for e in g.edges}
    assert min(abs(a-b) for i,a in pts.items() for j,b in pts.items() if i<j) > 1e-6
    return draw_chain(s, u, rect)


def ends():
    s=SVG(1200,770,'Два соглашения о периоде',
          'Для периода LR и двух повторений внутреннее слово LRLR даёт шесть ядер. Четыре бегунка LRLR от стартового ребра дают четыре ядра с внутренним словом RL.')
    s.text(600,43,'Один период LR · два повторения · разные концы',27,anchor='middle',weight='bold')
    for y,u,title,runners,count in [
        (65,'LRLR','Периодическое внутреннее слово','S | LR | LR | S',6),
        (415,'RL','Бегунки от стартового ребра','LR | LR',4)]:
        s.panel(20,y,1160,325)
        s.text(48,y+42,title,26,weight='bold')
        checked_chain(s,u,(50,y+70,700,210))
        s.text(960,y+105,'Выходы бегунков',20,MUTED,'middle')
        s.text(960,y+146,runners,27,BLUE,'middle','bold')
        s.text(960,y+198,'u = '+u,25,anchor='middle')
        s.text(960,y+247,f'N = {count};  n = {4*count+2}',25,anchor='middle')
        s.text(390,y+306,'Синие рёбра - швы; цифры - номера ядер',18,MUTED,'middle')
    s.save('Два соглашения о периоде.svg')


def phases():
    s=SVG(1200,630,'Три фазы периода LLS',
          'Внутренние слова LLS, LSL, SLL при одном повторении задают пять ядер. LLS и SLL изоморфны; LSL имеет другой спектр. Матрицы всех трёх периодов подобны.')
    s.text(600,42,'Один период · три начала · два класса графов',27,anchor='middle',weight='bold')
    for x,u,h in [(20,'LLS',1),(420,'LSL',0),(820,'SLL',1)]:
        s.panel(x,65,360,465)
        s.text(x+180,107,'u = '+u,29,anchor='middle',weight='bold')
        checked_chain(s,u,(x+28,140,304,235))
        s.text(x+180,414,f'N = 5;  h = {h}',23,anchor='middle')
        value=DATA['phases'][u]['P1_sequence'][1]
        s.text(x+180,459,'P(1) =',20,MUTED,'middle')
        s.text(x+180,494,f'{value:,}'.replace(',',' '),24,RED if u=='LSL' else BLUE,'middle','bold')
    s.text(600,575,'LLS и SLL: обращение цепи сохраняет спектр',23,BLUE,'middle')
    s.text(600,611,'LLS и LSL: Δp6 = −1 при любом числе повторений m ≥ 1',23,RED,'middle')
    s.save('Три фазы периода LLS.svg')


def growth():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    words=['LR','LLS','SL']
    vals=[float(DATA['periods'][w]['at_minus_one']['growth_per_core']) for w in words]
    with plt.rc_context({'font.family':'DejaVu Sans','font.size':15,'svg.fonttype':'path','svg.hashsalt':'periodic-slr'}):
        fig,ax=plt.subplots(figsize=(11.8,4.7))
        fig.patch.set_facecolor('white');ax.set_facecolor('#f7f9fc')
        for i,(w,value,color) in enumerate(zip(words,vals,[BLUE,GREEN,RED])):
            ax.plot(value,2-i,'o',color=color,markersize=11)
            ax.annotate(f'{value:.6f}'.replace('.',','),(value,2-i),xytext=(0,15),
                        textcoords='offset points',ha='center',color=color,fontsize=16)
        ax.set_yticks([2,1,0],words);ax.set_ylim(-.5,2.6)
        ax.set_xlim(88.0,88.35);ax.set_xticks([88.0,88.05,88.1,88.15,88.2,88.25,88.3,88.35])
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'{x:.2f}'.replace('.',',')))
        ax.grid(axis='x',color='#dce4ed');ax.set_axisbelow(True)
        for side in ['top','right','left']:ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#aab7c6');ax.tick_params(axis='y',length=0,pad=12)
        ax.set_xlabel('Предельный рост числа корневых лесов на одно ядро',labelpad=17)
        ax.set_title('Период влияет на скорость роста',fontsize=20,loc='left',pad=24)
        fig.text(.5,.035,'Для LLS сравнение учитывает три ядра за период; для LR и SL - два.',
                 ha='center',fontsize=13,color=MUTED)
        fig.subplots_adjust(left=.10,right=.97,top=.80,bottom=.25)
        fig.savefig(OUT/'Рост корневых лесов периодических цепочек.svg',metadata={
            'Date':None,
            'Title':'Рост корневых лесов периодических цепочек',
            'Description':'Точный предел P(1) в степени 1/N: LR 88,047425; LLS 88,200892; SL 88,305091. Показаны округлённые значения.'})
        plt.close(fig)
    output=OUT/'Рост корневых лесов периодических цепочек.svg'
    output.write_text('\n'.join(line.rstrip() for line in output.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')


if __name__=='__main__':
    ends();phases();growth()
    print('PASS: three figures, five graph-incidence checks, growth from exact results')
