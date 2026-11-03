"""Four vector illustrations using values from the exact cycle audit."""
from fractions import Fraction as Q
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[2]
out = root / 'pmg-library/ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/images'
preview = root.parent / 'path-polyform-research/cycle-preview'
preview.mkdir(parents=True, exist_ok=True)
data = json.loads(Path(__file__).with_name('cycle-results.json').read_text())['cases']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14, 'svg.fonttype': 'none'})
blue, orange, purple, gray = '#246585', '#bf651f', '#8a3c88', '#657587'
triangle = {'a': (-1, -.55), 'b': (0, 1.2), 'c': (1, -.55)}
square = {'a': (-1, 1), 'b': (1, 1), 'c': (1, -1), 'd': (-1, -1)}
diamond = {'a': (-1, 0), 'b': (0, 1.2), 'c': (1, 0), 'd': (0, -1.2)}


def network(ax, case, pos, mode='m', label_prefix=False):
    for row in case['edges']:
        i, j = row['edge']
        p, q = pos[i], pos[j]
        m = Q(row['m'])
        current = Q(row['Iu'] if mode == 'Iu' else row['Iv'])
        color = blue if mode in ('Iv', 'both') else orange if mode == 'Iu' else (
            orange if m > 0 else purple if m < 0 else gray)
        if mode in ('Iv', 'Iu', 'both'):
            start, end = (p, q) if current >= 0 else (q, p)
            ax.annotate('', xy=end, xytext=start,
                        arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.6,
                                    'shrinkA': 13, 'shrinkB': 13, 'mutation_scale': 16}, zorder=1)
        else:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=color,
                    lw=3.3 if m else 2, ls='-' if m else '--', zorder=1)
        midpoint = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        length = math.hypot(*midpoint)
        offset = (.30 * midpoint[0] / length, .30 * midpoint[1] / length) if length > .01 else (.08, .08)
        xy = (midpoint[0] + offset[0], midpoint[1] + offset[1])
        if mode == 'both':
            label = 'I = ' + str(abs(current)) + '\nm = ' + row['m']
        elif mode in ('Iv', 'Iu'):
            label = str(abs(current))
        else:
            label = ('m = ' if label_prefix else '') + ('+' if m > 0 and case['value'] == '0' else '') + row['m']
        ax.text(*xy, label, ha='center', va='center', fontsize=14, color=color,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2.5}, zorder=4)
    for name, p in pos.items():
        ax.scatter(*p, s=550, facecolor='white', edgecolor=gray, zorder=5)
        ax.text(*p, name, ha='center', va='center', fontsize=16, zorder=6)
    ax.set(xlim=(-1.9, 1.9), ylim=(-1.8, 1.8), aspect='equal')
    ax.axis('off')


def save(fig, name, desc):
    fig.savefig(out / (name + '.svg'), bbox_inches='tight', metadata={'Title': name, 'Description': desc})
    fig.savefig(preview / (name + '.png'), bbox_inches='tight', dpi=155)
    plt.close(fig)


fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.8))
for ax, key, title in zip(axes, ('triangle', 'reinforced_triangle'),
                          ('Все проводимости равны 1', 'Проводимость ac равна 2')):
    network(ax, data[key], triangle, mode='both')
    ax.set_title(title, fontsize=16, pad=12)
    ax.text(0, -1.5, r'$N([(ac)]^2)=' + data[key]['value'] + '$', ha='center', fontsize=19)
fig.suptitle('Два маршрута для единичного тока a → c', fontsize=18, y=.98)
fig.subplots_adjust(top=.77, bottom=.02, left=.02, right=.98, wspace=.12)
save(fig, 'Два маршрута в треугольнике',
     'Слева токи 1/3, 1/3 и 2/3, вклады 1/9, 1/9 и 4/9. Справа после увеличения c_ac до 2 токи 1/5, 1/5 и 4/5, вклады 1/25, 1/25 и 8/25. Норма меняется с 2/3 до 2/5.')

fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.4))
for ax, mode, title in zip(axes, ('Iv', 'Iu', 'm'), ('Поток для v = (ac)', 'Поток для u = (bd)', 'Коэффициенты смешанной формы')):
    network(ax, data['square_mixed'], square, mode=mode)
    ax.set_title(title, fontsize=14, pad=12)
axes[2].text(0, -1.65, 'Сумма = 0; поле ненулевое', ha='center', fontsize=13)
fig.suptitle('Знак зависит от взаимных направлений токов', fontsize=18, y=.98)
fig.subplots_adjust(top=.77, bottom=.03, left=.01, right=.99, wspace=.02)
save(fig, 'Два потока и знаки на квадрате',
     'Поток a-c и поток b-d имеют на сторонах модули 1/2. На ab и cd направления противоположны и вклад -1/4; на bc и ad совпадают и вклад +1/4. Сумма нулевая, распределение ненулевое.')

fig, ax = plt.subplots(figsize=(6.4, 4.9))
network(ax, data['balanced_bridge'], square, label_prefix=True)
ax.set_title('Распределение нормы (ac)²', fontsize=18, pad=18)
ax.text(0, -1.67, 'Все c = 1;   R(ac) = 1;   I(bd) = 0', ha='center', fontsize=14)
fig.subplots_adjust(top=.84, bottom=.02, left=.02, right=.98)
save(fig, 'Нулевое влияние перемычки',
     'Квадрат с единичной диагональной связью bd. В опыте a-c вершины b и d равнопотенциальны: вклад существующей перемычки равен нулю, а вклады четырёх сторон равны 1/4.')

fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.1))
network(axes[0], data['triangle'], triangle)
network(axes[1], data['subdivision'], diamond)
axes[0].set_title('Ребро ac: сопротивление 1', fontsize=15, pad=12)
axes[1].set_title('Два участка: 1/2 + 1/2', fontsize=15, pad=12)
for ax in axes:
    ax.text(0, -1.68, 'Сумма коэффициентов = 2/3', ha='center', fontsize=14)
fig.suptitle('Старая метрика сохраняется; вклад делится', fontsize=18, y=.98)
fig.text(.5, .88, 'На рёбрах указаны коэффициенты распределения для [(ac)]²', ha='center', fontsize=13, color=gray)
fig.subplots_adjust(top=.75, bottom=.02, left=.02, right=.98, wspace=.12)
save(fig, 'Детализация ребра и распределение',
     'Единичный треугольник и его детализация новой вершиной d на связи ac. Старый вклад ac 4/9 делится на ad 2/9 и cd 2/9; вклады ab и bc остаются 1/9. Резистенс ac остаётся 2/3.')
