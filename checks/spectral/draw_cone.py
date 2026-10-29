"""Draw the P3 spectral cone and reciprocal image after exact checks."""
import argparse
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from verify_cone import check

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
args = parser.parse_args()
data = check()
out = Path(__file__).resolve().parents[2]/"pmg-library/ru/Спектры и диагонализация в алгебре полиформ"
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "PMG-fixed-basis-cone"})
INK, BLUE, TEAL, ORANGE, GREY = "#19354a", "#216b9f", "#25857e", "#bb4e28", "#a8b5bf"
GREEN_FILL, ORANGE_FILL = "#cce9df", "#f9d9bf"


def save(fig, name, description):
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


def axes_style(ax, limit, x_label, y_label):
    ax.set(xlim=(0, limit), ylim=(0, limit), aspect="equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color(GREY)
    ax.set_xlabel(x_label, fontsize=16, color=INK, labelpad=8)
    ax.set_ylabel(y_label, fontsize=16, color=INK, labelpad=8)
    ax.tick_params(colors=INK)
    ax.grid(color="#e2e8eb", lw=.7, zorder=0)
    ax.set_axisbelow(True)


def graph(ax, edges, title):
    coords = {1: (-1, -.5), 2: (0, .8), 3: (1, -.5)}
    used = {v for pair in edges for v in pair}
    for i, j in edges:
        p, q = coords[i], coords[j]
        ax.plot([p[0], q[0]], [p[1], q[1]], color=BLUE, lw=3, zorder=1)
    for v, (x, y) in coords.items():
        ax.scatter(x, y, s=360, color=BLUE if v in used else GREY, zorder=2)
        ax.text(x, y, str(v), color="white", ha="center", va="center", fontsize=11, zorder=3)
    ax.set(xlim=(-1.35, 1.35), ylim=(-.85, 1.12), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12, color=INK, pad=0)


fig = plt.figure(figsize=(12.4, 8.1), facecolor="white")
fig.text(.055, .94, "Фиксированные моды пути — целый конус графов", fontsize=20, weight="bold", color=INK)
fig.text(.055, .875, r"$w_{12}=w_{23}=b/3,\qquad w_{13}=(3a-b)/6$", fontsize=19, color=INK)
ax = fig.add_axes([.075, .19, .55, .62])
limit = 4.4
axes_style(ax, limit, r"$a=\mu_1$", r"$b=\mu_2$")
ax.fill([0, limit/3, limit, limit], [0, limit, limit, 0], color="#e0edf7", zorder=1)
ax.plot([0, limit/3], [0, limit], color=BLUE, lw=2.5, zorder=2)
ax.plot([0, limit], [0, 0], color=TEAL, lw=3, zorder=2, clip_on=False)
ax.text(.25, 2.7, r"$b=3a$", rotation=71.565, fontsize=14, color=BLUE)
ax.text(2.9, .16, r"$b=0$", fontsize=14, color=TEAL)
ax.text(2.15, 2.1, "Взвешенные\nтреугольники", color=INK, fontsize=14, ha="center")
labels = {(0, 0): (18, 14, "(0, 0)"), (2, 0): (-18, 15, "E (2, 0)"),
          (1, 3): (10, 14, "P₃ (1, 3)"), (3, 3): (10, 10, "K₃ (3, 3)")}
for a, b in data["simple_points"]:
    ax.scatter(a, b, s=70, color=INK, edgecolor="white", zorder=4, clip_on=False)
    dx, dy, label = labels[(a, b)]
    ax.annotate(label, (a, b), xytext=(dx, dy), textcoords="offset points", fontsize=12, color=INK)
graph(fig.add_axes([.71, .61, .22, .17]), [(1, 2), (2, 3)], "P₃: связная граница")
graph(fig.add_axes([.71, .385, .22, .17]), [(1, 2), (2, 3), (1, 3)], "K₃: внутренняя точка")
graph(fig.add_axes([.71, .16, .22, .17]), [(1, 3)], "E: несвязная граница")
fig.text(.07, .075, r"$(a,b)=\frac{b}{3}(1,3)+\frac{3a-b}{6}(2,0)$", fontsize=19, color=INK)
fig.text(.07, .026, "Коэффициенты разложения по крайним лучам — проводимости рёбер.", fontsize=12, color=INK)
save(fig, "Конус базиса P3 и его графы",
     "Конус a≥0, 0≤b≤3a. Крайние лучи: единичный путь P3 с координатами (1,3) и ребро 1–3 с изолированной вершиной 2, точка (2,0). Четыре отмеченные точки соответствуют всем простым графам в фиксированном базисе. Полный граф K3 находится в точке (3,3).")

fig = plt.figure(figsize=(12.4, 7.9), facecolor="white")
fig.text(.055, .94, "Обращение собственных чисел меняет допустимую область", fontsize=19, weight="bold", color=INK)
fig.text(.5, .875, r"$(a,b)\longmapsto(\alpha,\beta)=(1/a,1/b)$", fontsize=20, color=INK, ha="center")
left = fig.add_axes([.075, .26, .375, .53])
right = fig.add_axes([.575, .26, .375, .53])
for ax, lim, x, y in [(left, 4.6, r"$a$", r"$b$"), (right, 1.6, r"$\alpha$", r"$\beta$")]:
    axes_style(ax, lim, x, y)
    ax.fill([0, lim/3, lim, lim], [0, lim, lim, lim/3], color=GREEN_FILL, zorder=1)
    ax.plot([0, lim/3], [0, lim], color=TEAL, lw=2, zorder=2)
    ax.plot([0, lim], [0, lim/3], color=TEAL, lw=2, zorder=2)
left.fill([0, 4.6, 4.6], [0, 0, 4.6/3], color=ORANGE_FILL, zorder=1)
right.fill([0, 0, 1.6/3], [0, 1.6, 1.6], color=ORANGE_FILL, zorder=1)
left.set_title("Исходный лапласиан", fontsize=15, color=INK, pad=12)
right.set_title("Его гриниан", fontsize=15, color=INK, pad=12)
left.text(.27, 3.0, r"$b=3a$", rotation=71.565, color=TEAL, fontsize=12)
left.text(2.5, 1.25, r"$b=a/3$", rotation=18.435, color=TEAL, fontsize=12)
right.text(.18, 1.17, r"$\beta=3\alpha$", rotation=71.565, color=TEAL, fontsize=12)
right.text(.88, .37, r"$\beta=\alpha/3$", rotation=18.435, color=TEAL, fontsize=12)
for ax, point, offset, label in [(left, (4, 1), (-70, -30), "(4, 1)"),
                                 (right, (.25, 1), (12, -12), "(1/4, 1)")]:
    ax.scatter(*point, s=75, color=ORANGE, edgecolor="white", zorder=4)
    ax.annotate(label, point, xytext=offset, textcoords="offset points", fontsize=13,
                color=INK, arrowprops={"arrowstyle": "-", "color": ORANGE})
fig.legend(handles=[Patch(facecolor=GREEN_FILL, label="Обе матрицы — графовые лапласианы"),
                    Patch(facecolor=ORANGE_FILL, label="Исходный граф допустим; у гриниана нарушены знаки")],
           loc="lower left", bbox_to_anchor=(.07, .10), frameon=False, fontsize=12)
fig.text(.075, .066, r"$(4,1):\quad w_{12}=w_{23}=1/3,\quad w_{13}=11/6,\quad \mathrm{Gr}_{13}=+1/24$", fontsize=14, color=INK)
fig.text(.075, .022, "Масштабы панелей различаются. Координатные оси не входят в область обращения.", fontsize=11, color=INK)
save(fig, "Обращение спектральных координат в базисе P3",
     "Слева связная часть конуса a>0, 0<b≤3a; справа её образ α>0, β≥α/3. Зелёные сектора a/3≤b≤3a и α/3≤β≤3α соответствуют графовым лапласианам и графовым гринианам одновременно. Оранжевый сектор b<a/3 переходит в β>3α, где гриниан не удовлетворяет знаковым условиям. Пример (4,1) переходит в (1/4,1) и даёт Gr13=1/24>0.")
