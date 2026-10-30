"""Editable SVG diagrams for continuants and seam order; standard library."""
from pathlib import Path
import json

from draw_admissible_chains import SVG, INK, MUTED, BLUE, PURPLE
from verify_spanning_polynomials import matchings


def main():
    s=SVG(1080,650,'Паросочетания и остовной полином четырёх ядер',
          'Пять паросочетаний вспомогательного пути на четырёх ядрах: пустое, три одиночных ребра и пара первого с третьим. '
          'Каждое выбранное ребро даёт минус квадрат числа общих рёбер, непокрытая вершина даёт размер ядра.')
    s.text(540,42,'Пять паросочетаний пути на четырёх ядрах',27,anchor='middle',weight='bold')
    s.text(540,78,'Синим выделены рёбра паросочетания; круги обозначают ядра',21,MUTED,anchor='middle')
    terms={(): 'm₁m₂m₃m₄', (0,): '−ℓ₁²m₃m₄', (1,): '−ℓ₂²m₁m₄', (2,): '−ℓ₃²m₁m₂', (0,2): '+ℓ₁²ℓ₃²'}
    xs=[210,330,450,570]
    for row,es in enumerate(matchings(4)):
        y=145+95*row
        s.text(60,y+8,'∅' if not es else ', '.join(str(i+1) for i in es),24,anchor='middle')
        for i in range(3):
            selected=i in es
            s.line((xs[i],y),(xs[i+1],y),BLUE if selected else '#c5ced9',7 if selected else 2)
        covered={v for i in es for v in (i,i+1)}
        for i,x in enumerate(xs):
            s.circle((x,y),21,'#e2edff' if i in covered else 'white',BLUE if i in covered else MUTED,2)
            s.text(x,y+7,str(i+1),21,anchor='middle')
        s.text(700,y+9,terms[es],29,INK,weight='bold')
    s.text(540,619,'ℓᵢ = sᵢ − 1: число общих рёбер, а не число вершин шва',22,anchor='middle')
    s.save('Паросочетания и остовной полином.svg')

    records=json.loads(Path(__file__).with_name('spanning-polynomials-results.json').read_text(encoding='utf-8'))
    values={g['name']:g['tau'] for g in records['graphs']}
    s=SVG(1080,500,'Порядок швов меняет остовное число',
          'Вспомогательные пути четырёх восьмиугольных ядер. Порядки швов 1,2,3 и 1,3,2 дают 3776 деревьев; '
          'порядок 2,1,3 даёт 3780. Размеры швов считаются в вершинах; пунктир означает точечный контакт.')
    s.text(540,43,'Одинаковые ядра C₈, разные порядки швов',27,anchor='middle',weight='bold')
    s.text(540,78,'Вспомогательный путь: каждый круг обозначает целый цикл',21,MUTED,anchor='middle')
    xs=[115,315,515,715]
    for row,order in enumerate([(1,2,3),(2,1,3),(1,3,2)]):
        y=150+125*row
        for i,size in enumerate(order):
            s.line((xs[i],y),(xs[i+1],y),PURPLE if size==1 else MUTED,3,'7 6' if size==1 else '')
            s.text((xs[i]+xs[i+1])/2,y-18,'s = '+str(size),23,PURPLE if size==1 else INK,anchor='middle')
        for i,x in enumerate(xs):
            s.circle((x,y),25,'#fff0d7',INK,2)
            s.text(x,y+8,str(i+1),24,anchor='middle')
        tau=values['order_'+''.join(map(str,order))+'_r0']
        s.text(930,y+9,'τ = '+str(tau),29,PURPLE if row==1 else INK,anchor='middle',weight='bold')
    s.text(540,475,'Пунктир: шов из одной вершины; общее ребро отсутствует',22,anchor='middle')
    s.save('Порядок швов и остовное число.svg')


if __name__=='__main__':
    main()
