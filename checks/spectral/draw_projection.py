"""Draw two projection figures from independently verified rational data."""
import argparse
from figure_language import prepare_figure, output_directory
from pathlib import Path
from fractions import Fraction as F
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from verify_projection import check, family_edges, spectral, MU, MU_STAR, PAIRS

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
args = parser.parse_args()
data = check()
out = output_directory(args.lang)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "PMG-spectral-projection"})
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


def graph(ax, edges, title, size=12):
    coords = {0: (-1, 1), 1: (1, 1), 2: (1, -1), 3: (-1, -1)}
    labels = {(0, 1): (0, 1.23), (2, 3): (0, -1.23),
              (0, 3): (-1.32, 0), (1, 2): (1.32, 0),
              (0, 2): (-.43, .43), (1, 3): (.43, .43)}
    for i, j, weight in edges:
        if not weight:
            continue
        pair = tuple(sorted((i, j)))
        p, q = coords[i], coords[j]
        color = ORANGE if weight < 0 else BLUE
        ax.plot([p[0], q[0]], [p[1], q[1]], color=color,
                lw=2.3, ls="--" if weight < 0 else "-", zorder=1)
        ax.text(*labels[pair], str(weight), color=color, ha="center", va="center",
                fontsize=size, zorder=3,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for vertex, (x, y) in coords.items():
        ax.scatter(x, y, s=340, color=INK, edgecolor="white", lw=1, zorder=4)
        ax.text(x, y, str(vertex+1), color="white", ha="center", va="center", fontsize=11, zorder=5)
    ax.set(xlim=(-1.75, 1.75), ylim=(-1.55, 1.55), aspect="equal")
    ax.axis("off")
    ax.set_title(title, color=INK, fontsize=15, pad=10)


def matrix_table(ax, entries, mixed=False):
    ax.axis("off")
    table = ax.table(cellText=entries, cellLoc="center", loc="center", bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor("white")
        cell.set_linewidth(2)
        cell.set_facecolor("#e3eef6" if i == j else "#f2f4f5")
        cell.set_text_props(color=INK)
        if mixed and (i, j) in [(0, 1), (1, 0)]:
            cell.set_facecolor("#f9d9bf")
            cell.set_text_props(color=ORANGE, weight="bold")


fig = plt.figure(figsize=(13.3, 8.4), facecolor="white")
fig.text(.045, .94, "От удаления смешанных мод к ближайшему графу", fontsize=21, weight="bold", color=INK)
fig.text(.045, .881, "Один базис, две разные задачи приближения", fontsize=15, color=INK)
hat, star = spectral(MU), spectral(MU_STAR)
graphs = [family_edges(-4), [(i, j, -hat[i][j]) for i, j in PAIRS],
          [(i, j, -star[i][j]) for i, j in PAIRS]]
titles = ["Исходный граф", "Диагональная проекция", "Проекция на конус"]
centers = [.17, .50, .83]
for c, edges, title in zip(centers, graphs, titles):
    graph(fig.add_axes([c-.145, .49, .29, .31]), edges, title)
for x in [.335, .665]:
    fig.text(x, .63, "→", fontsize=28, color=GREY, ha="center")
fig.text(.5, .43, "Матрицы на H в фиксированном базисе", fontsize=14, color=INK, ha="center")
matrices = [[["10", "−4", "0"], ["−4", "4", "0"], ["0", "0", "4"]],
            [["10", "0", "0"], ["0", "4", "0"], ["0", "0", "4"]],
            [["554/57", "0", "0"], ["0", "244/57", "0"], ["0", "0", "248/57"]]]
for k, (c, entries) in enumerate(zip(centers, matrices)):
    matrix_table(fig.add_axes([c-.115, .225, .23, .16]), entries, mixed=k == 0)
for c, text in zip(centers, [r"Спектр на $H$: 2, 4, 12",
                             r"$\|\mathbf{L}-\widehat{\mathbf{L}}\|_F^2=32$",
                             r"$\|\mathbf{L}-\mathbf{L}_*\|_F^2=1840/57$"]):
    fig.text(c, .16, text, ha="center", fontsize=14, color=INK)
fig.text(.045, .088, "Квадрат ошибки: 32 от удаления смешанных коэффициентов и ещё 16/57 от исправления знаков.", fontsize=12, color=INK)
fig.text(.045, .040, "Числа у связей — проводимости; оранжевый пунктир показывает недопустимые отрицательные значения.", fontsize=11, color=INK)
save(fig, "Диагональная проекция и ближайший граф на четырёх вершинах",
     "Исходный цикл 1–2–3–4–1 имеет проводимости 1 и дополнительное ребро 1–3 проводимости 5. Его матрица на H: [[10,−4,0],[−4,4,0],[0,0,4]]. У диагональной проекции связи 1–2 и 3–4 имеют коэффициент −1/5. Проекция на графовый конус имеет диагональ (554,244,248)/57, проводимости w14=w23=124/57, w13=184/57, w24=91/57 и w12=w34=0. Квадраты ошибок относительно исходного оператора: 32 и 1840/57.")

fig = plt.figure(figsize=(13.0, 8.2), facecolor="white")
fig.text(.045, .94, "Разные графы с одной спектральной проекцией", fontsize=21, weight="bold", color=INK)
fig.text(.045, .88, r"Семейство со смешанным коэффициентом $r$:  $-4\leq r\leq-2/3$", fontsize=15, color=INK)
graph(fig.add_axes([.035, .54, .27, .25]), family_edges(-4), r"$r=-4$", size=11)
graph(fig.add_axes([.035, .17, .27, .25]), family_edges(-2), r"$r=-2$", size=11)
fig.text(.17, .492, r"$\tau=24,\quad \mathrm{Kf}=10/3$", ha="center", color=INK, fontsize=13)
fig.text(.17, .122, r"$\tau=36,\quad \mathrm{Kf}=23/9$", ha="center", color=INK, fontsize=13)
for start in [(.30, .65), (.30, .30)]:
    arrow = FancyArrowPatch(start, (.40, .48), transform=fig.transFigure,
                            arrowstyle="-|>", mutation_scale=14, color=GREY, lw=1.8)
    fig.add_artist(arrow)
fig.text(.435, .55, "Одна\nдиагональ", ha="center", va="center", color=INK, fontsize=15)
fig.text(.435, .46, "(10, 4, 4)", ha="center", va="center", color=BLUE, fontsize=18,
         bbox={"facecolor": "#e3eef6", "edgecolor": "none", "boxstyle": "round,pad=.5"})
fig.text(.435, .35, "После исправления знаков:\nодна ближайшая\nточка конуса", ha="center", va="center", color=INK, fontsize=11)
ax = fig.add_axes([.61, .25, .35, .51])
rs = [-4+(F(10, 3)*i/200) for i in range(201)]
r13 = [F(2, 5)*(26+4*r)/(40-r*r) for r in rs]
r24 = [F(2, 5)*(44-4*r)/(40-r*r) for r in rs]
ax.plot(list(map(float, rs)), list(map(float, r13)), lw=2.7, color=BLUE, label=r"$R_{13}$")
ax.plot(list(map(float, rs)), list(map(float, r24)), lw=2.7, color=TEAL, label=r"$R_{24}$")
for case in [data["polyform_cases"][0], data["polyform_cases"][2]]:
    r = float(F(case["r"]))
    for index, color in [(1, BLUE), (4, TEAL)]:
        ax.scatter(r, float(F(case["R"][index])), s=65, color=color, edgecolor="white", zorder=3)
ax.set(xlim=(-4.12, -.55), ylim=(0, 1.1), xlabel=r"$r$", ylabel="Резистенс")
ax.set_xticks([-4, -3, -2, -2/3], ["−4", "−3", "−2", "−2/3"])
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["bottom", "left"]].set_color(GREY)
ax.tick_params(colors=INK)
ax.grid(color="#e2e8eb", lw=.7)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right", fontsize=14)
ax.set_title("Резистенсы исходных графов", color=INK, fontsize=14, pad=12)
fig.text(.61, .16, "Точки на кривых: r = −4 и r = −2.", fontsize=12, color=INK)
fig.text(.045, .045, "Отброшенный коэффициент меняет рёбра, лесные коэффициенты и резистивную геометрию.", fontsize=12, color=INK)
save(fig, "Разные графы с одной спектральной проекцией",
     "Графы при r=−4 и r=−2 имеют общую диагональ (10,4,4) и одну ближайшую точку спектрального конуса. Первый имеет остовной коэффициент 24, индекс Кирхгофа 10/3 и R13=1/6, R24=1; второй — 36, 23/9 и R13=1/5, R24=26/45. Справа показаны проверенные функции R13=(2/5)(26+4r)/(40−r²) и R24=(2/5)(44−4r)/(40−r²) на отрезке [−4,−2/3].")
