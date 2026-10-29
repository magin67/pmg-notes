"""Reproduce the first spectral note's figures after exact verification.

Requires Matplotlib. SVGs are written beside the note in the selected language. Optional PNG
previews are written only when --preview-dir is supplied.
"""
import argparse
from figure_language import prepare_figure, output_directory
from math import cos, sin, pi, sqrt
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from verify_diagonal import check

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir", type=Path)
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
args = parser.parse_args()
data = check()
root = Path(__file__).resolve().parents[2]
out = output_directory(args.lang)
out.mkdir(parents=True, exist_ok=True)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":12,
                     "svg.fonttype":"none", "svg.hashsalt":"PMG-spectral-P3",
                     "axes.spines.top":False, "axes.spines.right":False})
BLUE, ORANGE, INK, GREY = "#216b9f", "#bb4e28", "#19354a", "#7a8993"
LIGHT, BORDER = "#edf4f8", "#bdcbd5"


def save(fig, name, description):
    name, description = prepare_figure(fig, name, description, args.lang)
    target = out / (name+".svg")
    fig.savefig(target, metadata={"Date":None, "Description":description})
    svg = target.read_text(encoding="utf-8")
    start = svg.index(">",svg.index("<svg"))+1
    svg = svg[:start]+f"\n<title>{escape(name)}</title>\n<desc>{escape(description)}</desc>"+svg[start:]
    svg = "\n".join(line.rstrip() for line in svg.splitlines())+"\n"
    with target.open("w",encoding="utf-8",newline="\n") as stream:
        stream.write(svg)
    if args.preview_dir:
        fig.savefig(args.preview_dir/(name+".png"),dpi=140)
    plt.close(fig)
    print(target.name)


fig, ax = plt.subplots(figsize=(11.4,6.3),facecolor="white")
fig.subplots_adjust(left=.055,right=.96,top=.78,bottom=.16)
ax.set(xlim=(-1.25,7.25),ylim=(-.55,3.2)); ax.axis("off")
fig.text(.055,.93,"Путь P₃: собственные направления",fontsize=21,weight="bold",color=INK)
fig.text(.055,.86,"Единичные проводимости. Координатная ортонормировка.",color=INK)
ax.text(1.5,3.03,"Значения на вершинах",ha="center",color=INK,weight="bold")
ax.text(5.0,3.03,r"$\mathbf{L}$",ha="center",fontsize=19,color=INK)
ax.text(6.6,3.03,r"$\mathbf{Gr}$",ha="center",fontsize=19,color=INK)
modes = [(0,[1,1,1],3,["+1/√3"]*3,"0","0")]
for i,(q,s,l) in enumerate(zip(data["raw_modes"],data["squared_lengths"],data["eigenvalues"]),1):
    labels = [["+1/√2","0","−1/√2"],["+1/√6","−2/√6","+1/√6"]][i-1]
    modes.append((i,q,s,labels,l,"1" if l=="1" else "1/3"))
for row,(i,q,s,labels,lam,inv) in enumerate(modes):
    y = 2.45-row*1.23
    ax.text(-.95,y,rf"$\mathbf{{u}}_{i}$",fontsize=21,va="center",color=INK)
    ax.plot([0,1.5,3],[y]*3,color=BORDER,lw=3,zorder=1)
    for j,(v,label) in enumerate(zip(q,labels)):
        col = BLUE if v>0 else ORANGE if v<0 else GREY
        ax.scatter(j*1.5,y,s=560,color=col,edgecolor="white",linewidth=1.6,zorder=2)
        ax.text(j*1.5,y,str(j+1),ha="center",va="center",color="white",fontsize=12,zorder=3)
        ax.text(j*1.5,y-.39,label,ha="center",color=INK,fontsize=14)
    ax.text(5,y,lam,ha="center",va="center",color=BLUE,fontsize=21)
    ax.text(6.6,y,inv,ha="center",va="center",color=ORANGE,fontsize=21)
ax.plot([-1.15,7.05],[1.76,1.76],color=BORDER,lw=1,ls="--")
fig.text(.055,.055,"Сверху: постоянная мода вне H.  Снизу: две моды H, общие для L и Gr.",color=INK,fontsize=12)
save(fig,"Собственные моды пути P3",
     "Компоненты трёх ортонормированных мод: (1,1,1)/√3, (1,0,-1)/√2, (1,-2,1)/√6. Множители L: 0,1,3; Gr: 0,1,1/3.")

fig,ax=plt.subplots(figsize=(11.4,7.0),facecolor="white")
fig.subplots_adjust(left=.035,right=.965,top=.79,bottom=.14)
ax.set(xlim=(0,12),ylim=(.35,5.4)); ax.axis("off")
fig.text(.055,.935,"Дуальность: дополнительные наборы направлений",fontsize=19,weight="bold",color=INK)
fig.text(.055,.867,r"$A=[u_1]^2,\ B=[u_2]^2,\quad A^\vee=[u^1]^2,\ B^\vee=[u^2]^2,\quad\Delta=3$",fontsize=16,color=INK)
ax.text(2.35,5.12,r"$M=\exp L$",ha="center",fontsize=19,color=BLUE)
ax.text(9.55,5.12,r"$D=\exp Q_1$",ha="center",fontsize=19,color=ORANGE)
ax.text(2.35,4.88,"Слагаемые прямых грейдов",ha="center",fontsize=10,color=GREY)
ax.text(9.55,4.88,"Слагаемые дуальных грейдов",ha="center",fontsize=10,color=GREY)
rows=[("M_0","e",r"\varnothing\ \longrightarrow\ \{1,2\}",r"\frac{1}{3} A^\vee B^\vee","Q_2"),
      ("M_1","A",r"\{1\}\ \longrightarrow\ \{2\}",r"\frac{1}{3} B^\vee","Q_1"),
      ("M_1","3B",r"\{2\}\ \longrightarrow\ \{1\}",r"A^\vee","Q_1"),
      ("M_2","3AB",r"\{1,2\}\ \longrightarrow\ \varnothing","e","Q_0")]
for row,(left,term,sets,dual,right) in enumerate(rows):
    y=4.35-row*1.05
    ax.add_patch(FancyBboxPatch((.35,y-.37),3.7,.75,boxstyle="round,pad=0.08",facecolor=LIGHT,edgecolor="none"))
    ax.add_patch(FancyBboxPatch((8.0,y-.37),3.7,.75,boxstyle="round,pad=0.08",facecolor="#fbf0ea",edgecolor="none"))
    ax.text(.58,y,rf"${left}$",ha="left",va="center",fontsize=15,color=BLUE)
    ax.text(2.5,y,rf"${term}$",ha="center",va="center",fontsize=24,color=INK)
    ax.text(9.45,y,rf"${dual}$",ha="center",va="center",fontsize=23,color=INK)
    ax.text(11.5,y,rf"${right}$",ha="right",va="center",fontsize=15,color=ORANGE)
    ax.add_patch(FancyArrowPatch((4.25,y-.04),(7.8,y-.04),arrowstyle="-|>",mutation_scale=15,color=GREY,lw=1.6))
    ax.text(6.0,y+.19,rf"${sets}$",ha="center",va="bottom",fontsize=13,color=INK)
    ax.text(6.0,y-.3,"коэффициент / 3",ha="center",va="center",fontsize=11,color=GREY)
fig.text(.055,.066,"Грейды 0 ↔ 2. В грейде 1 также берётся дополнительное направление.",fontsize=13,color=INK)
save(fig,"Дополнительные грейды пути P3",
     "Четыре соответствия: e переходит в A∨B∨/3; A в B∨/3; 3B в A∨; 3AB в e. Каждый коэффициент делится на 3, набор направлений заменяется дополнительным.")

fig,ax=plt.subplots(figsize=(8.1,7.7),facecolor="white")
fig.subplots_adjust(left=.17,right=.94,top=.82,bottom=.23)
angles=[2*pi*i/600 for i in range(601)]
a=[cos(t) for t in angles]
ax.plot(a,[sqrt(3)*sin(t) for t in angles],color=BLUE,lw=2.6,label=r"$P_M([w]^2)=a^2+b^2/3=1$")
ax.plot(a,[sin(t)/sqrt(3) for t in angles],color=ORANGE,lw=2.6,label=r"$P_N([w]^2)=a^2+3b^2=1$")
ax.plot(a,[sin(t) for t in angles],color=GREY,ls="--",lw=1.6,label=r"$\langle w,w\rangle_0=a^2+b^2=1$")
ax.axhline(0,color=BORDER,lw=.8); ax.axvline(0,color=BORDER,lw=.8)
ax.set_aspect("equal"); ax.set(xlim=(-1.45,1.45),ylim=(-1.95,1.95))
ax.set_xlabel(r"$a$ - коэффициент при $u_1$",color=INK)
ax.set_ylabel(r"$b$ - коэффициент при $u_2$",color=INK)
ax.grid(alpha=.17)
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.17),frameon=False,fontsize=12)
fig.text(.07,.936,"Две метрики в одном базисе",fontsize=21,weight="bold",color=INK)
fig.text(.07,.875,r"$w=a u_1+b u_2$"+". Единичные уровни квадратичных норм.",fontsize=13,color=INK)
save(fig,"Две метрики в базисе пути P3",
     "Эллипсы a²+b²/3=1 и a²+3b²=1 в коэффициентах вектора w=a u1+b u2; для сравнения окружность a²+b²=1. Оси совпадают, коэффициенты по u2 взаимно обратны.")
