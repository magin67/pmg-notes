"""Draw four path/cycle figures from verified data. Requires Matplotlib.

Exact and numerical checks run before drawing. SVGs are written beside the
Russian note; optional PNG previews are saved to --preview-dir.
"""
import argparse
from pathlib import Path
from xml.sax.saxutils import escape
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from verify_path_cycle import check

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
args = parser.parse_args()
data = check()
out = Path(__file__).resolve().parents[2]/"pmg-library/ru/Спектры и диагонализация в алгебре полиформ"
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "PMG-path-cycle",
                     "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, TEAL, GREY, INK = "#216b9f", "#bb4e28", "#25857e", "#84919a", "#19354a"
BORDER = "#c6d1d8"


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


def component(value):
    return "0" if abs(value) < 1e-10 else f"{value:+.3f}".replace("-", "−")


def sign_color(value):
    return GREY if abs(value) < 1e-10 else BLUE if value > 0 else ORANGE


def sign_legend(fig, y):
    fig.text(.055, y, "●  положительная", color=BLUE, fontsize=11)
    fig.text(.275, y, "●  отрицательная", color=ORANGE, fontsize=11)
    fig.text(.50, y, "●  нулевая", color=GREY, fontsize=11)


# Path: the same six vertices in every row, including the constant mode.
fig = plt.figure(figsize=(12.5, 8.5), facecolor="white")
ax = fig.add_axes([.04, .15, .93, .65])
ax.set(xlim=(-1.1, 9.4), ylim=(-.65, 5.6))
ax.axis("off")
U = np.array(data["P6"]["modes"])
left = ["0", r"2-\sqrt{3}", "1", "2", "3", r"2+\sqrt{3}"]
right = ["0", r"2+\sqrt{3}", "1", r"1/2", r"1/3", r"2-\sqrt{3}"]
for k in range(6):
    y = 5-k
    ax.plot(range(6), [y]*6, color=BORDER, lw=2.6, zorder=1)
    ax.text(-.80, y, "$u_"+str(k)+"$", ha="center", va="center", fontsize=17, color=INK)
    for r, value in enumerate(U[:, k]):
        ax.scatter(r, y, s=440, color=sign_color(value), edgecolor="white", linewidth=1.2, zorder=2)
        ax.text(r, y, str(r+1), color="white", ha="center", va="center", fontsize=10, zorder=3)
        ax.text(r, y-.33, component(value), color=INK, ha="center", va="center", fontsize=11)
    for x, value in [(6.65, left[k]), (8.65, right[k])]:
        ax.text(x, y-.06, "$"+value+"$", color=INK, ha="center", va="center", fontsize=17)
ax.text(6.65, 5.57, r"$\mathbf{L}$", ha="center", color=INK, fontsize=19)
ax.text(8.65, 5.57, r"$\mathbf{Gr}$", ha="center", color=INK, fontsize=19)
ax.axvline(5.65, color=BORDER, lw=1)
fig.text(.055, .945, "Путь P₆: моды и два спектральных множителя", fontsize=21, weight="bold", color=INK)
fig.text(.055, .882, r"$u_k(r)=\sqrt{2/6}\,\cos\!\left(\pi k(r-1/2)/6\right)$"+"  при k > 0", fontsize=17, color=INK)
sign_legend(fig, .073)
fig.text(.055, .027, "Координатная норма каждой моды равна 1. Компоненты округлены до трёх знаков.", fontsize=11, color=INK)
save(fig, "Собственные моды пути P6",
     "Все шесть координатно нормированных мод P6. Положительные компоненты синие, отрицательные оранжевые, нулевые серые. Справа собственные числа L: 0, 2−√3, 1, 2, 3, 2+√3 и Gr: 0, 2+√3, 1, 1/2, 1/3, 2−√3.")


def cycle_panel(ax, values, title):
    n = len(values)
    angles = np.pi/2-2*np.pi*np.arange(n)/n
    xy = np.column_stack((np.cos(angles), np.sin(angles)))
    for i in range(n):
        j = (i+1) % n
        ax.plot(xy[[i, j], 0], xy[[i, j], 1], color=BORDER, lw=2.5, zorder=1)
    for i, ((x, y), value) in enumerate(zip(xy, values)):
        ax.scatter(x, y, s=460, color=sign_color(value), edgecolor="white", linewidth=1.3, zorder=2)
        ax.text(x, y, str(i+1), ha="center", va="center", fontsize=11, color="white", zorder=3)
        ax.text(1.70*x, 1.40*y, component(value), color=INK, fontsize=11,
                ha="center", va="center")
    ax.set(xlim=(-1.98, 1.98), ylim=(-1.56, 1.56), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=16, color=INK, pad=13)


fig, axes = plt.subplots(3, 2, figsize=(10.7, 12), facecolor="white")
fig.subplots_adjust(left=.055, right=.945, top=.835, bottom=.095, wspace=.20, hspace=.31)
U = np.array(data["C6"]["modes"])
indices = [0, 5, 1, 2, 3, 4]
titles = [r"$u_0:\quad \mathbf{L}:\,0,\ \mathbf{Gr}:\,0$", r"$w:\quad \mathbf{L}:\,4,\ \mathbf{Gr}:\,1/4$",
          r"$v_1^c:\quad \mathbf{L}:\,1,\ \mathbf{Gr}:\,1$", r"$v_1^s:\quad \mathbf{L}:\,1,\ \mathbf{Gr}:\,1$",
          r"$v_2^c:\quad \mathbf{L}:\,3,\ \mathbf{Gr}:\,1/3$", r"$v_2^s:\quad \mathbf{L}:\,3,\ \mathbf{Gr}:\,1/3$"]
for ax, index, title in zip(axes.flat, indices, titles):
    cycle_panel(ax, U[:, index], title)
fig.text(.055, .957, "Цикл C₆: две пары и две отдельные моды", fontsize=21, weight="bold", color=INK)
fig.text(.055, .914, "Для каждой моды указаны множители действия лапласиана и гриниана.", fontsize=12, color=INK)
fig.text(.055, .88, "Во втором ряду собственное число 1, в третьем - 3; каждый из этих рядов задаёт пару.", fontsize=11, color=INK)
sign_legend(fig, .043)
save(fig, "Вещественные моды цикла C6",
     "Полный вещественный базис C6: постоянная и чередующаяся моды, косинусно-синусные пары частот 1 и 2. Компоненты нормированы и округлены до трёх знаков. Для каждой моды указаны множители L и Gr.")

fig, axes = plt.subplots(2, 2, figsize=(10.7, 9.1), facecolor="white")
fig.subplots_adjust(left=.055, right=.945, top=.79, bottom=.14, wspace=.20, hspace=.33)
U = np.array(data["C5"]["modes"])
titles = [r"$v_1^c:\quad \mu_1=(5-\sqrt{5})/2$", r"$v_1^s:\quad \mu_1=(5-\sqrt{5})/2$",
          r"$v_2^c:\quad \mu_2=(5+\sqrt{5})/2$", r"$v_2^s:\quad \mu_2=(5+\sqrt{5})/2$"]
for ax, index, title in zip(axes.flat, range(1, 5), titles):
    cycle_panel(ax, U[:, index], title)
fig.text(.055, .948, "Цикл C₅: четыре моды в двух подпространствах", fontsize=20, weight="bold", color=INK)
fig.text(.055, .887, "В каждой паре лапласиан умножает на μₖ, а гриниан на 1/μₖ.", fontsize=13, color=INK)
fig.text(.055, .844, "Показаны ненулевые моды. Постоянная мода имеет компоненты 1/√5.", fontsize=12, color=INK)
sign_legend(fig, .078)
fig.text(.055, .025, "Чередующаяся последовательность не замыкается после пяти шагов: отдельной моды 4 нет.", fontsize=11, color=INK)
save(fig, "Парные моды нечётного цикла C5",
     "Две пары ненулевых мод C5 с числами (5−√5)/2 и (5+√5)/2. Косинусные и синусные компоненты нормированы и округлены до трёх знаков. Отдельной чередующейся моды нет.")


# Separate quantitative axes preserve the actual resistance contributions.
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 7.8), facecolor="white",
                            gridspec_kw={"width_ratios": [1, 1.25]})
fig.subplots_adjust(left=.075, right=.965, top=.76, bottom=.25, wspace=.35)
colors = [BLUE, TEAL, ORANGE]
path_rows = [[sp.sympify(row[k]) for k in (0, 2, 4)] for row in data["P6"]["resistance_contributions"]]
path_text = [[r"\frac{7+4\sqrt{3}}{3}", "1/3", r"\frac{7-4\sqrt{3}}{3}"], ["1/3"]*3]
for x, (row, labels) in enumerate(zip(path_rows, path_text)):
    bottom = 0
    for k, (value, label, color) in enumerate(zip(row, labels, colors)):
        height = float(value)
        ax.bar(x, height, bottom=bottom, width=.48, color=color,
               label=["мода k = 1", "мода k = 3", "мода k = 5"][k] if x == 0 else None)
        if x == 0 and k == 2:
            ax.annotate("$"+label+"$", xy=(x+.24, bottom+height/2), xytext=(.57, 5.05),
                        fontsize=13, color=ORANGE, ha="left", va="center",
                        arrowprops={"arrowstyle": "-", "color": ORANGE, "lw": 1.1})
        else:
            ax.text(x, bottom+height/2, "$"+label+"$", ha="center", va="center",
                    color="white", fontsize=14)
        bottom += height
    ax.text(x, bottom+.13, "$R="+str(int(round(bottom)))+"$", ha="center", fontsize=15, color=INK)
ax.set_xticks([0, 1], labels=["Пара 1,6", "Пара 3,4"])
ax.set(xlim=(-.55, 1.55), ylim=(0, 5.7), ylabel="Вклад в резистенс")
ax.set_title("Путь P₆", fontsize=18, color=INK, pad=15)
ax.legend(loc="upper left", bbox_to_anchor=(-.08, -.13), frameon=False, fontsize=10)
cycle_rows = [[sp.sympify(v) for v in row] for row in data["C6"]["resistance_contributions"]]
for x, row in enumerate(cycle_rows):
    bottom = 0
    for k, (value, color) in enumerate(zip(row, colors)):
        height = float(value)
        bx.bar(x, height, bottom=bottom, width=.48, color=color,
               label=["пара μ₁ = 1", "пара μ₂ = 3", "мода 4"][k] if x == 0 else None)
        if height:
            bx.text(x, bottom+height/2, "$"+sp.latex(value)+"$", ha="center", va="center", color="white", fontsize=15)
        bottom += height
    bx.text(x, bottom+.055, "$R="+sp.latex(sum(row))+"$", ha="center", fontsize=15, color=INK)
bx.set_xticks([0, 1, 2], labels=["Пара 1,2", "Пара 1,3", "Пара 1,4"])
bx.set(xlim=(-.55, 2.55), ylim=(0, 1.8), ylabel="Вклад в резистенс")
bx.set_title("Цикл C₆", fontsize=18, color=INK, pad=15)
bx.legend(loc="upper left", bbox_to_anchor=(-.04, -.13), frameon=False, fontsize=10)
for panel in (ax, bx):
    panel.set_axisbelow(True)
    panel.yaxis.grid(True, color="#e8eef2")
    panel.tick_params(axis="x", length=0, pad=9)
fig.text(.055, .944, "Какие моды соединяют выбранные вершины", fontsize=21, weight="bold", color=INK)
fig.text(.055, .872, "Высота каждого столбца равна сопротивлению. Цветные части показывают спектральные вклады.", fontsize=12, color=INK)
fig.text(.055, .035, "У P₆ моды k = 2 и 4 дают нулевые вклады в обе выбранные пары. Вертикальные шкалы различаются.", fontsize=11, color=INK)
save(fig, "Спектральные вклады в резистенсы P6 и C6",
     "P6: R16=(7+4√3)/3+1/3+(7−4√3)/3=5, R34=1/3+1/3+1/3=1. C6: R12=1/3+1/3+1/6=5/6; R13=1+1/3=4/3; R14=4/3+1/6=3/2. Высоты частей соответствуют точным значениям; шкалы панелей различаются.")
