"""Draw two figures from the exact Chebyshev-orbit checks.

Requires SymPy and Matplotlib. SVGs go beside the Russian note; optional PNGs
are saved to --preview-dir. Mathematical data are checked before rendering.
"""
import argparse
from figure_language import prepare_figure, output_directory
from pathlib import Path
from math import cos, sin, pi
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from verify_chebyshev import check

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
args = parser.parse_args()
data = check()
out = output_directory(args.lang)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "PMG-Chebyshev-orbit"})
INK, BLUE, TEAL, ORANGE, GREY = "#19354a", "#216b9f", "#25857e", "#bb4e28", "#a8b5bf"


def save(fig, name, description):
    name, description = prepare_figure(fig, name, description, args.lang)
    path = out/(name+".svg")
    fig.savefig(path, metadata={"Date": None, "Description": description})
    svg = path.read_text(encoding="utf-8")
    start = svg.index(">", svg.index("<svg"))+1
    svg = svg[:start]+f"\n<title>{escape(name)}</title>\n<desc>{escape(description)}</desc>"+svg[start:]
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(line.rstrip() for line in svg.splitlines())+"\n")
    if args.preview_dir:
        fig.savefig(args.preview_dir/(name+".png"), dpi=140)
    plt.close(fig)
    print(path.name)


def circle(order, center=(0, 0), radius=1):
    return {vertex: (center[0]+radius*cos(pi/2-2*pi*k/len(order)),
                     center[1]+radius*sin(pi/2-2*pi*k/len(order)))
            for k, vertex in enumerate(order)}


def graph(ax, entry, coords, highlight=False):
    part_color = {vertex: [BLUE, TEAL, ORANGE][i] for i, part in enumerate(entry["components"]) for vertex in part}
    for i, j, weight in entry["edges"]:
        a, b = coords[i], coords[j]
        color = (ORANGE if abs(i-j) == 1 else BLUE) if highlight else part_color[i]
        if highlight and entry["m"] == 1 and (i, j) not in [(1, 2), (5, 6)]:
            color = GREY
        ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=3.3 if weight == 2 else 2.8, zorder=1)
        if weight != 1:
            ax.text((a[0]+b[0])/2+.14, (a[1]+b[1])/2, str(weight), color=color,
                    fontsize=14, ha="left", va="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for vertex, (x, y) in coords.items():
        ax.scatter(x, y, s=440, color=INK if highlight else part_color[vertex],
                   edgecolor="white", linewidth=1.2, zorder=2)
        ax.text(x, y, str(vertex), color="white", fontsize=11, ha="center", va="center", zorder=3)
    ax.axis("off")


fig = plt.figure(figsize=(12.4, 8.6), facecolor="white")
left = fig.add_axes([.055, .61, .40, .22])
graph(left, data["P6"][1], {i+1: (i, 0) for i in range(6)}, True)
left.set(xlim=(-.35, 5.35), ylim=(-.65, .65))
left.set_title("Путь P₆", fontsize=18, color=INK, pad=1)
right = fig.add_axes([.64, .575, .29, .27])
graph(right, data["P6"][2], circle([1, 2, 4, 6, 5, 3]), True)
right.set(xlim=(-1.4, 1.4), ylim=(-1.3, 1.3), aspect="equal")
right.set_title("Цикл с исходными номерами", fontsize=15, color=INK, pad=1)
fig.text(.49, .73, r"$\Phi_2$", fontsize=23, color=INK, ha="center")
fig.text(.49, .68, "⟶", fontsize=28, color=INK, ha="center")
fig.text(.055, .55, "Оранжевые рёбра сохраняются. Синие соединяют вершины на расстоянии два в пути.", fontsize=11.5, color=INK)

ax = fig.add_axes([.09, .13, .82, .36])
ax.axis("off")
old = ["0", r"$2-\sqrt{3}$", "1", "2", "3", r"$2+\sqrt{3}$"]
new = ["0", "1", "3", "4", "3", "1"]
green = ["0", "1", "1/3", "1/4", "1/3", "1"]
rows = [[str(k), old[k], new[k], green[k]] for k in range(6)]
table = ax.table(cellText=rows, colLabels=["Мода k", "Число пути", "Число после Φ₂", "Число гриниана"],
                 cellLoc="center", colLoc="center", loc="center", bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(14)
palette = {"0": "#f0f2f4", "1": "#e2eff8", "3": "#e1f1ed", "4": "#fae5da"}
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("white")
    cell.set_linewidth(2)
    cell.set_text_props(color=INK)
    if row == 0:
        cell.set_facecolor("#d3e0e8")
        cell.set_text_props(weight="bold", fontsize=12)
    else:
        cell.set_facecolor(palette[new[row-1]])
fig.text(.055, .944, "Удвоение спектрального угла: P₆ превращается в цикл", fontsize=20, weight="bold", color=INK)
fig.text(.055, .88, r"$\mathbf{L}^{(2)}=4\mathbf{L}_{P_6}-\mathbf{L}_{P_6}^{\,2},\qquad\Phi_2(\xi)=\xi(4-\xi)$", fontsize=20, color=INK)
fig.text(.055, .060, "Одинаковый цвет строк выделяет объединённое собственное подпространство.", fontsize=12, color=INK)
fig.text(.055, .024, "Базис пути сохраняется; меняются собственные числа и резистивная метрика.", fontsize=11, color=INK)
save(fig, "Чебышёвский переход от пути P6 к циклу",
     "Переход 4L−L² сохраняет рёбра 1–2 и 5–6 и добавляет 1–3, 2–4, 3–5, 4–6. Обход нового цикла: 1,2,4,6,5,3. В исходном базисе пути спектр меняется с 0,2−√3,1,2,3,2+√3 на 0,1,3,4,3,1; числа гриниана: 0,1,1/3,1/4,1/3,1.")

fig, axes = plt.subplots(2, 3, figsize=(13.6, 8.6), facecolor="white")
fig.subplots_adjust(left=.035, right=.965, top=.78, bottom=.18, wspace=.18, hspace=.54)
layouts = {
    1: {i+1: (-1.5+.6*i, 0) for i in range(6)},
    2: circle([1, 2, 4, 6, 5, 3], radius=.85),
    3: {1: (-1.35, .6), 3: (-.25, .6), 6: (-.25, -.6), 4: (-1.35, -.6), 2: (1.15, .6), 5: (1.15, -.6)},
    4: {**circle([1, 4, 5], (-.95, 0), .59), **circle([2, 3, 6], (.95, 0), .59)},
    5: {v: (-1.5+.6*i, 0) for i, v in enumerate([3, 5, 1, 6, 2, 4])},
    6: {1: (-1.2, .6), 6: (-1.2, -.6), 2: (0, .6), 5: (0, -.6), 3: (1.2, .6), 4: (1.2, -.6)}
}
titles = {1: r"$m=1:\quad P_6$", 2: r"$m=2:\quad C_6$", 3: r"$m=3:\quad P_2\sqcup C_4$",
          4: r"$m=4:\quad 2C_3$", 5: r"$m=5:\quad P_6$", 6: "$m=6$: рёбра проводимости 2"}
for m, ax in enumerate(axes.flat, 1):
    entry = data["P6"][m]
    graph(ax, entry, layouts[m])
    ax.set(xlim=(-1.95, 1.95), ylim=(-1.1, 1.1), aspect="equal")
    ax.set_title(titles[m], fontsize=17 if m < 6 else 13, color=INK, pad=13)
    c = entry["nullity"]
    ax.text(.5, -.12, f"Компонент: {c}    |    Нулевых мод: {c}    |    Ранг: {6-c}",
            transform=ax.transAxes, ha="center", fontsize=10, color=INK)
fig.text(.055, .94, "Чебышёвская орбита P₆: связность меняется, базис сохраняется", fontsize=20, weight="bold", color=INK)
fig.text(.055, .875, r"$\mathbf{L}^{(m)}=\Phi_m(\mathbf{L}_{P_6}),\qquad \mu_k^{(m)}=2-2\cos(\pi mk/6)$", fontsize=18, color=INK)
fig.text(.055, .085, "Цвет различает компоненты. Номера вершин сохранены; расположение выбрано для ясности рёбер.", fontsize=11, color=INK)
fig.text(.055, .035, "При m = 0 получаются шесть изолированных вершин. Далее орбита отражается и повторяется с периодом 12.", fontsize=11, color=INK)
save(fig, "Графы чебышёвской орбиты пути P6",
     "Шаги m=1..6 дают P6, C6, P2 плюс C4, два C3, перенумерованный P6 и три ребра проводимости 2. Число компонент и нулевых мод: 1,1,2,2,1,3. Нумерация вершин сохраняется, рёбра вычислены точно.")
