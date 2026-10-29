"""Draw two cospectral-graph figures using independently checked exact data."""
import argparse
from figure_language import prepare_figure, output_directory
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from verify_cospectral import check, RAW, NORMS

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
args = parser.parse_args()
data = check()
out = output_directory(args.lang)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "PMG-cospectral"})
INK, BLUE, TEAL, ORANGE, GREY = "#19354a", "#216b9f", "#25857e", "#bb4e28", "#8e9ca5"


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


def graph(ax, case, mode, norm):
    coords = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    edge_labels = {(0, 1): (0, 1.15), (2, 3): (0, -1.15),
                   (0, 3): (-1.13, 0), (1, 2): (1.13, 0),
                   (0, 2): (-.43, .43), (1, 3): (.43, .43)}
    for i, j, weight in case["edges"]:
        p, q = coords[i], coords[j]
        ax.plot([p[0], q[0]], [p[1], q[1]], color="#b1bcc4", lw=1.5+float(weight)*.6, zorder=1)
        ax.text(*edge_labels[(i, j)], str(weight), ha="center", va="center", color=INK,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2}, zorder=3)
    for i, ((x, y), component) in enumerate(zip(coords, mode)):
        color = BLUE if component > 0 else ORANGE if component < 0 else GREY
        ax.scatter(x, y, s=580, color=color, edgecolor="white", lw=1.5, zorder=4)
        ax.text(x, y, str(i+1), ha="center", va="center", color="white", weight="bold", zorder=5)
        label = "0" if not component else (("-" if component < 0 else "+") +
                (r"1/\sqrt{2}" if norm == 2 else r"1/2"))
        ax.text(x, y+(.38 if y > 0 else -.38), "$"+label+"$",
                ha="center", va="center", color=color, fontsize=14)
    ax.set(xlim=(-1.7, 1.7), ylim=(-1.65, 1.65), aspect="equal")
    ax.axis("off")


fig = plt.figure(figsize=(12.2, 7.4), facecolor="white")
fig.text(.045, .94, "Один спектр, разные собственные направления", fontsize=21, weight="bold", color=INK)
fig.text(.045, .875, r"Два взвешенных графа: спектр $0,\,4,\,4,\,8$; показана мода с $\lambda=8$",
         fontsize=14, color=INK)
for index, case in enumerate(data["cases"]):
    center = [.27, .74][index]
    graph(fig.add_axes([center-.20, .30, .40, .49]), case, RAW[index], NORMS[index])
    fig.text(center, .805, [r"$G_1$: полный граф, $c_{12}=3$, остальные $c=1$",
                           r"$G_2$: $K_{2,2}$, все четыре $c=2$"][index],
             ha="center", fontsize=13, color=INK)
    fig.text(center, .255, [r"$z_1=(1,-1,0,0)/\sqrt{2}$",
                           r"$z_2=(1,1,-1,-1)/2$"][index],
             ha="center", fontsize=16, color=INK)
    fig.text(center, .19, [r"$\mathbf{E}^{(1)}_8=z_1z_1^{\mathsf{T}}$",
                          r"$\mathbf{E}^{(2)}_8=z_2z_2^{\mathsf{T}}$"][index],
             ha="center", fontsize=16, color=INK)
fig.text(.5, .106, r"Для обоих графов: $\mathbf{L}=4\mathbf{J}+4\mathbf{E}_8$,  $\mathbf{E}_4=\mathbf{J}-\mathbf{E}_8$",
         ha="center", fontsize=15, color=INK)
fig.text(.045, .038, "Числа у рёбер — проводимости; у вершин — компоненты нормированной моды. Пересечения рёбер не являются вершинами.",
         fontsize=10, color=INK)
save(fig, "Изоспектральные графы и собственные направления",
     "Два неизоморфных взвешенных графа со спектром 0,4,4,8. G1 — полный граф K4 с проводимостью ребра 12 равной 3 и остальными равными 1; G2 — K2,2 с долями {1,2},{3,4} и всеми проводимостями 2. Моды собственного числа 8: z1=(1,-1,0,0)/sqrt(2) и z2=(1,1,-1,-1)/2. Синий цвет означает положительную компоненту, оранжевый отрицательную, серый нулевую. Проекторы E8 различаются, хотя их ранги и спектры лапласианов совпадают.")

fig = plt.figure(figsize=(12.2, 7.3), facecolor="white")
fig.text(.045, .94, "Резистенсы зависят от положения собственных подпространств", fontsize=18, weight="bold", color=INK)
fig.text(.045, .87, r"$R_{ij}=\|\mathbf{E}_4(e_j-e_i)\|_0^2/4+\|\mathbf{E}_8(e_j-e_i)\|_0^2/8$",
         fontsize=17, color=INK)
for panel, pair in enumerate(["12", "13"]):
    ax = fig.add_axes([.09+panel*.47, .26, .37, .47])
    for index, case in enumerate(data["cases"]):
        bottom = 0.
        for contribution, color in zip(case["contributions"][pair], [TEAL, ORANGE]):
            value = float(contribution)
            ax.bar(index, value, bottom=bottom, width=.53, color=color, edgecolor="white", linewidth=1.3)
            if contribution:
                ax.text(index, bottom+value/2, str(contribution), ha="center", va="center",
                        color="white", fontsize=13, weight="bold")
            bottom += value
        ax.text(index, bottom+.018, str(case["R"][pair]), ha="center", color=INK, fontsize=15, weight="bold")
    ax.set(xlim=(-.6, 1.6), ylim=(0, .58), xticks=[0, 1], xticklabels=[r"$G_1$", r"$G_2$"])
    ax.set_title(r"$R_{"+pair+"}$", color=INK, fontsize=18, pad=12)
    ax.set_yticks([0, .125, .25, .375, .5], ["0", "1/8", "1/4", "3/8", "1/2"])
    ax.grid(axis="y", alpha=.17)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(colors=INK)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(color=TEAL, label=r"Вклад подпространства $\lambda=4$"),
                    Patch(color=ORANGE, label=r"Вклад направления $\lambda=8$")],
           loc="lower center", bbox_to_anchor=(.5, .135), ncol=2, frameon=False, fontsize=12)
fig.text(.5, .085, r"В обоих графах $\sum_{i<j}R_{ij}=\mathrm{Kf}=5/2$, но отдельные резистенсы различаются.",
         ha="center", color=INK, fontsize=13)
fig.text(.045, .028, "Высоты столбцов и долей получены точным вычислением проекторов и псевдообратных матриц.", fontsize=10, color=INK)
save(fig, "Одинаковый спектр и разные резистенсы",
     "Для графа G1 резистенс R12=1/4 целиком создаётся модой 8, а для G2 R12=1/2 целиком создаётся подпространством 4. Для пары 13 вклады подпространств 4 и 8 равны 3/8 и 1/16 у G1, 1/4 и 1/8 у G2: суммы 7/16 и 3/8. Индекс Кирхгофа обоих графов равен 5/2. Все величины вычислены в точной рациональной арифметике.")
