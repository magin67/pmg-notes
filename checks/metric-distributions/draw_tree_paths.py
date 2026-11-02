"""Three explanatory SVG figures; finite values come from the exact audit."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[2]
out = root / 'pmg-library/ru/Резистивная геометрия и дуальность/Метрические распределения и влияние связей/images'
preview = root.parent / 'path-polyform-research/tree-path-preview'
preview.mkdir(parents=True, exist_ok=True)
data = json.loads(Path(__file__).with_name('tree-path-results.json').read_text())
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14, 'svg.fonttype': 'none'})
blue, orange, gray, pale = '#246585', '#bf651f', '#657587', '#d5dce1'
names = 'abcde'


def chain(ax, weights=None, shared=(), selected=None, output=False):
    for i in range(4):
        color = orange if i in shared or i == selected else gray
        width = 4.5 if i in shared or i == selected else 2
        if output and i not in shared:
            color, width = pale, 1
        if output and weights is not None and i in shared:
            width = 2 + 3 * float(Fraction(weights[i]))
        ax.plot([i, i + 1], [0, 0], color=color, lw=width, zorder=1,
                ls=':' if output and i not in shared else '-')
        if weights is not None:
            label = weights[i]
            ax.text(i + .5, -.38 if output else .26, str(label), ha='center',
                    color=color, fontsize=14)
    for i, name in enumerate(names):
        edgecolor = pale if output and i not in (1, 2, 3) else gray
        ax.scatter(i, 0, s=480, facecolor='white', edgecolor=edgecolor, zorder=3)
        ax.text(i, 0, name, ha='center', va='center', zorder=4, fontsize=15, color=edgecolor)
    ax.set_xlim(-.3, 4.3)
    ax.axis('off')


def arrow(ax, start, finish, y, label, color):
    ax.annotate('', xy=(finish, y), xytext=(start, y),
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.3, 'mutation_scale': 15})
    ax.text((start + finish) / 2, y + .12, label, ha='center', color=color, fontsize=14)


def save(fig, name, desc):
    fig.savefig(out / (name + '.svg'), bbox_inches='tight',
                metadata={'Title': name, 'Description': desc})
    fig.savefig(preview / (name + '.png'), bbox_inches='tight', dpi=150)
    plt.close(fig)


fig, axes = plt.subplots(3, 1, figsize=(9, 8.7))
cases = [
    ('Совпадающие направления на общем участке', (0, 3, 'v = (ad)'), (1, 4, 'u = (be)'), (1, 2),
     'Вклады: +1 на bc, +1 на cd;   N(f) = 2'),
    ('Обращён только второй путь', (0, 3, 'v = (ad)'), (4, 1, 'u = (eb)'), (1, 2),
     'Вклады: −1 на bc, −1 на cd;   N(f) = −2'),
    ('Одна общая вершина, общих рёбер нет', (0, 2, 'v = (ac)'), (2, 4, 'u = (ce)'), (),
     'Все рёберные вклады равны нулю;   N(f) = 0'),
]
for ax, (title, v, u, shared, result) in zip(axes, cases):
    chain(ax, shared=shared)
    arrow(ax, *v[:2], .72, v[2], blue)
    arrow(ax, *u[:2], 1.23, u[2], orange)
    ax.text(2, 1.88, title, ha='center', fontsize=16, weight='bold')
    ax.text(2, -.65, result, ha='center', fontsize=14)
    ax.set_ylim(-.82, 2.15)
fig.subplots_adjust(hspace=.27, left=.05, right=.95, top=.98, bottom=.02)
save(fig, 'Направления путей на дереве',
     'Три пары путей единичной цепочки: одинаковое направление на b-c-d, противоположное направление на том же участке и встреча только в вершине c. Значения формы равны 2, -2 и 0.')

fig, axes = plt.subplots(2, 1, figsize=(9, 5.6))
chain(axes[0], weights=[r['c'] for r in data['weighted_probes']], shared=(1, 2))
arrow(axes[0], 0, 3, .83, 'v = (ad)', blue)
arrow(axes[0], 1, 4, 1.32, 'u = (be)', orange)
axes[0].text(2, 1.95, 'Исходное дерево: проводимости c', ha='center', fontsize=16, weight='bold')
axes[0].set_ylim(-.4, 2.2)
chain(axes[1], weights=[r['m'] for r in data['weighted_probes']], shared=(1, 2), output=True)
axes[1].text(2, .65, 'Распределение: коэффициенты m', ha='center', fontsize=16, weight='bold')
axes[1].text(2, -.92, r'$D_L(f)=\frac{1}{2}[(bc)]^2+2[(cd)]^2,\qquad N(f)=\frac{5}{2}$',
             ha='center', fontsize=19)
axes[1].set_ylim(-1.25, .95)
fig.subplots_adjust(hspace=.27, left=.05, right=.95, top=.98, bottom=.03)
save(fig, 'Проводимости и пересечение путей',
     'У цепочки проводимости 3, 2, 1/2 и 4. Для путей a-d и b-e коэффициенты распределения равны 0, 1/2, 2 и 0; их сумма 5/2.')

fig, axes = plt.subplots(4, 1, figsize=(10, 7.3))
for i, (ax, row) in enumerate(zip(axes, data['weighted_probes'])):
    weights = [r['c'] for r in data['weighted_probes']]
    weights[i] = row['new_c']
    chain(ax, weights=weights, selected=i)
    ax.text(0, .77, row['edge'] + ': ' + row['c'] + ' → ' + row['new_c'],
            ha='left', color=orange, fontsize=15, weight='bold')
    ax.text(4.65, .16, r'$N^{\prime}(f)=' + row['new_value'] + '$', fontsize=17)
    ax.text(4.65, -.4, r'$\Delta=' + row['change'] + '$', fontsize=17,
            color=orange if row['change'] != '0' else gray)
    ax.set(xlim=(-.3, 6.5), ylim=(-.65, 1.1))
fig.suptitle('Каждая проба начинается с исходного дерева', fontsize=17, y=.99)
fig.text(.5, .93, 'Исходно N(f) = 5/2; в каждой пробе удвоена одна проводимость',
         ha='center', fontsize=13, color=gray)
fig.subplots_adjust(hspace=.3, left=.04, right=.97, top=.86, bottom=.02)
save(fig, 'Пробы связей на дереве',
     'Четыре независимых удвоения проводимости. Для ab и de влияние нулевое; для bc оно равно -1/4, для cd равно -1. Новые значения формы 5/2, 9/4, 3/2 и 5/2.')
