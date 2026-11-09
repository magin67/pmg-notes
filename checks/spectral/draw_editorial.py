"""Four explanatory spectral figures, in Russian and English.

Run from any directory: python checks/spectral/draw_editorial.py --lang ru
The diagrams use the same coordinate metric as the spectral notes.
"""
import argparse
from pathlib import Path
from xml.sax.saxutils import escape
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, FancyBboxPatch

parser = argparse.ArgumentParser()
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
parser.add_argument("--preview-dir", type=Path)
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[2]
folder = (
    "ru/Инварианты, разложения и спектры/Спектры и диагонализация в алгебре полиформ"
    if args.lang == "ru" else
    "en/Invariants, Decompositions, and Spectra/Spectra and diagonalization in polyform algebra"
)
out = ROOT/"pmg-library"/folder/"images"
# Windows publication paths can exceed MAX_PATH.
if str(out).startswith("\\\\?\\") is False and out.drive:
    out = Path("\\\\?\\"+str(out))
out.mkdir(parents=True, exist_ok=True)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans", "svg.fonttype": "none",
                     "svg.hashsalt": "PMG-spectral-editorial-2026-11"})
INK, BLUE, TEAL, ORANGE, GREY = "#19354a", "#216b9f", "#25857e", "#bb4e28", "#9caab4"
PALETTE = [BLUE, ORANGE, TEAL, "#76599a", "#917028", "#416d75"]
def tr(ru, en):
    return ru if args.lang == "ru" else en

def save(fig, ru, en, description):
    name = tr(ru, en)
    fig.patch.set_facecolor("white")
    path = out/(name+".svg")
    fig.savefig(path, metadata={"Date": None, "Description": description})
    svg = path.read_text(encoding="utf-8")
    start = svg.index(">", svg.index("<svg"))+1
    svg = svg[:start]+f"\n<title>{escape(name)}</title>\n<desc>{escape(description)}</desc>"+svg[start:]
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(line.rstrip() for line in svg.splitlines())+"\n")
    if args.preview_dir:
        fig.savefig(args.preview_dir/(name+".png"), dpi=120)
    plt.close(fig)
    print(path.name)

def arrow(fig, p, q, color=GREY):
    fig.add_artist(FancyArrowPatch(p, q, transform=fig.transFigure,
                                  arrowstyle="-|>", mutation_scale=22,
                                  linewidth=1.8, color=color))

# 1. Ghost endpoint values explain the half-step shift.
fig, axes = plt.subplots(2, 1, figsize=(11, 7.1), sharex=True)
fig.subplots_adjust(left=.10, right=.96, top=.86, bottom=.17, hspace=.48)
fig.suptitle(tr("Почему косинус сдвинут на половину шага",
                "Why the cosine starts half a step earlier"),
             fontsize=18, color=INK, y=.97)
fig.text(.5, .915, tr("Путь P₆: отражаются значения, граф не продолжается",
                       "Path P₆: extend the values, not the graph"),
         ha="center", color=INK, fontsize=12)
for k, ax in enumerate(axes, 1):
    r = np.arange(8)
    values = np.sqrt(2/6)*np.cos(np.pi*k*(r-.5)/6)
    assert abs(values[0]-values[1]) < 1e-12
    assert abs(values[6]-values[7]) < 1e-12
    assert abs(np.dot(values[1:7], values[1:7])-1) < 1e-12
    x = np.linspace(0, 7, 300)
    ax.axhline(0, color="#d4dce2", lw=1)
    ax.axvspan(0, .5, color="#f3f5f7")
    ax.axvspan(6.5, 7, color="#f3f5f7")
    ax.plot(x, np.sqrt(2/6)*np.cos(np.pi*k*(x-.5)/6), color=BLUE, lw=2)
    ax.scatter(r[1:7], values[1:7], c=BLUE, s=65, zorder=3)
    ax.scatter(r[[0,7]], values[[0,7]], edgecolor=ORANGE,
               facecolor="white", s=85, linewidths=2, zorder=4)
    for boundary in (.5,6.5): ax.axvline(boundary, color=ORANGE, ls="--", lw=1.3)
    ax.text(.5, .67, r"$f_0=f_1$", color=ORANGE, ha="center", fontsize=13)
    ax.text(6.5, .67, r"$f_7=f_6$", color=ORANGE, ha="center", fontsize=13)
    ax.set(xlim=(-.25,7.25), ylim=(-.72,.82), yticks=[-.5,0,.5])
    ax.set_ylabel(r"$u_"+str(k)+r"(r)$", fontsize=14)
    ax.set_title(r"$k="+str(k)+r"$", color=INK, loc="left", fontsize=13)
    ax.spines[["top","right"]].set_visible(False)
axes[-1].set_xticks(range(8))
axes[-1].set_xlabel(tr("Позиция r; вершины пути имеют номера 1,…,6",
                       "Position r; path vertices are numbered 1,…,6"), labelpad=10)
fig.text(.5, .04, r"$u_k(r)=\sqrt{2/6}\,\cos\!\left(\pi k(r-1/2)/6\right)$",
         ha="center", color=INK, fontsize=16)
save(fig, "Косинусная мода пути и отражение на концах",
     "A cosine path mode reflected at the endpoints",
     tr("Две нормированные моды P6 и равные значения по обе стороны зеркал в позициях 1/2 и 13/2.",
        "Two normalized P6 modes with equal values on either side of mirrors at positions 1/2 and 13/2."))

# 2. Fold the step graphs on 12 positions. Independent matrix construction
# checks the quotient weights rather than summing the two reflected edges.
def representative(j, n=6):
    j %= 2*n
    return min(j,2*n-1-j)
def folded_matrix(m, n=6):
    result=np.zeros((n,n),dtype=int)
    for i in range(n):
        result[i,i]=2
        for j in (i+m,i-m): result[i,representative(j,n)]-=1
    return result
base=folded_matrix(1)
assert np.array_equal(folded_matrix(3),base@(base-3*np.eye(6,dtype=int))@(base-3*np.eye(6,dtype=int)))
expected_edges={1:{(i,i+1) for i in range(5)},3:{(0,2),(2,5),(3,5),(0,3),(1,4)}}
fig=plt.figure(figsize=(12,9.5))
fig.suptitle(tr("Свёртка: каждая отражённая пара становится вершиной",
                "Folding: each reflected pair becomes one vertex"),
             fontsize=17, y=.98, color=INK)
fig.text(.5,.932, tr("Одинаковые цвета обозначают одну пару; подпись: позиция j → новая вершина",
                     "Matching colors identify a pair; label: position j → new vertex"),
         ha="center", fontsize=12, color=INK)
fig.text(.5,.887, "0,11 → 1     1,10 → 2     2,9 → 3     3,8 → 4     4,7 → 5     5,6 → 6",
         ha="center", fontsize=12, color=INK)
for row,m in enumerate((1,3)):
    bottom=.49 if row==0 else .10
    ax=fig.add_axes([.04,bottom,.43,.35])
    bx=fig.add_axes([.60,bottom,.35,.35])
    theta=np.pi/2-2*np.pi*(np.arange(12)+.5)/12
    coords=np.column_stack([np.cos(theta),np.sin(theta)])
    for i in range(12):
        j=(i+m)%12
        internal=representative(i)==representative(j)
        ax.plot(coords[[i,j],0],coords[[i,j],1],
                color=GREY if internal else "#8297a6", lw=1.5,
                ls="--" if internal else "-", zorder=1)
    for j,(x,y) in enumerate(coords):
        label=representative(j)+1
        ax.scatter(x,y,s=155,color=PALETTE[label-1],zorder=3,edgecolors="white")
        ax.text(1.27*x,1.27*y,f"{j} → {label}",ha="center",va="center",
                fontsize=11,color=INK)
    ax.set(xlim=(-1.62,1.62),ylim=(-1.35,1.35),aspect="equal")
    ax.axis("off")
    ax.set_title(f"m = {m}",fontsize=15,color=INK,pad=9)
    mat=folded_matrix(m)
    edges={(i,j) for i in range(6) for j in range(i+1,6) if mat[i,j]<0}
    assert edges==expected_edges[m]
    assert np.array_equal(mat,mat.T)
    assert all(mat[i,j]==-1 for i,j in edges)
    if m==1:
        pos={i:np.array([i,0.]) for i in range(6)}
        bx.set(xlim=(-.6,5.6),ylim=(-1.5,1.5))
    else:
        pos={0:np.array([0.,1.]),2:np.array([1.7,1.]),5:np.array([1.7,-1.]),
             3:np.array([0.,-1.]),1:np.array([3.4,1.]),4:np.array([3.4,-1.])}
        bx.set(xlim=(-.6,4.),ylim=(-1.7,1.7))
    for i,j in edges:bx.plot(*np.array([pos[i],pos[j]]).T,color=BLUE,lw=2.5,zorder=1)
    for i,(x,y) in pos.items():
        bx.scatter(x,y,s=330,color=PALETTE[i],edgecolors="white",zorder=3)
        bx.text(x,y,str(i+1),ha="center",va="center",color="white",fontsize=12,zorder=4)
    bx.set_aspect("equal");bx.axis("off")
    bx.set_title(r"$P_6$" if m==1 else r"$C_4\ \sqcup\ P_2$",fontsize=17,color=INK,pad=10)
    arrow(fig,(.49,bottom+.17),(.58,bottom+.17),BLUE)
fig.text(.5,.04,tr("Переходы считаются из одной вершины пары. Каждое итоговое ребро имеет проводимость 1.",
                   "Count transitions from one vertex of each pair. Every resulting edge has conductance 1."),
         ha="center",fontsize=12,color=INK)
save(fig,"Свёртка удвоенного цикла для P6","Folding the doubled cycle for P6",
     tr("Свёртка шагов 1 и 3 на двенадцати позициях даёт P6 и C4 вместе с P2. Отражённые пары явно подписаны.",
        "Folding steps 1 and 3 on twelve positions gives P6 and C4 together with P2. Reflection pairs are explicitly labeled."))

# 3. Compare three projections in the reference C4 basis.
def matrix(fig, rect, entries, mode):
    ax=fig.add_axes(rect);ax.axis("off")
    table=ax.table(cellText=entries,cellLoc="center",bbox=[0,0,1,1])
    table.auto_set_font_size(False);table.set_fontsize(14)
    for (i,j),cell in table.get_celld().items():
        cell.set_edgecolor("white");cell.set_linewidth(2)
        color="#edf2f5"
        if i==j:color="#d7e8f3" if mode!="cone" else "#d2e9e4"
        if (i,j) in [(0,1),(1,0)]:color="#f4dccc" if mode=="source" else "#f1f1f1"
        cell.set_facecolor(color);cell.get_text().set_color(INK)
    ax.add_patch(Rectangle((0,1/3),2/3,2/3,transform=ax.transAxes,
                          fill=False,edgecolor=TEAL,lw=2.5,clip_on=False))
    return ax
fig=plt.figure(figsize=(11,8.2))
fig.suptitle(tr("Что сохраняют три проекции","What the three projections retain"),
             fontsize=19,y=.97,color=INK)
fig.text(.5,.91,tr("Первые две моды принадлежат одному подпространству опорного цикла C₄",
                   "The first two modes share one eigenspace of the reference cycle C₄"),
         ha="center",fontsize=12,color=INK)
source=[["10","−4","0"],["−4","4","0"],["0","0","4"]]
matrix(fig,[.07,.40,.25,.20],source,"source")
fig.text(.195,.65,tr("Исходная матрица S","Original matrix S"),ha="center",fontsize=15,color=INK)
fig.text(.195,.32,tr("Контур: двумерный блок","Outline: two-dimensional block"),
         ha="center",fontsize=11,color=TEAL)
for y,mode,entries,title,subtitle in [
    (.68,"source",source,tr("Блочная проекция","Block projection"),tr("Смешивание внутри блока сохранено","Mixing within the block is retained")),
    (.39,"diagonal",[["10","0","0"],["0","4","0"],["0","0","4"]],tr("Диагональная проекция","Diagonal projection"),tr("Смешанные коэффициенты удалены","Mixed coefficients are removed")),
    (.10,"cone",[["554/57","0","0"],["0","244/57","0"],["0","0","248/57"]],tr("Проекция на конус","Projection onto the cone"),tr("Диагональ изменена ради графовых знаков","The diagonal is changed to satisfy graph signs"))
]:
    matrix(fig,[.63,y,.28,.16],entries,mode)
    fig.text(.77,y+.19,title,ha="center",fontsize=14,color=INK)
    fig.text(.77,y-.033,subtitle,ha="center",fontsize=10.5,color=INK)
    arrow(fig,(.36,.50),(.58,y+.08),TEAL if mode=="source" else GREY)
save(fig,"Три проекции в одном базисе","Three projections in one basis",
     tr("Для одного графа показаны исходная матрица, сохранение целого блока, удаление смешанных коэффициентов и исправление диагонали до спектрального конуса.",
        "One graph is represented by its original matrix, its retained full block, its diagonal projection, and its diagonal corrected to the spectral cone."))

# 4. Noncommutation of grade construction and diagonal projection.
fig=plt.figure(figsize=(12,7.3))
fig.suptitle(tr("Порядок операций меняет второй грейд",
                "The order of operations changes grade two"),
             fontsize=19,color=INK,y=.97)
fig.text(.5,.89,tr("Сравниваем только коэффициент при форме [u₁u₂]²",
                   "Compare only the coefficient of the form [u₁u₂]²"),
         ha="center",fontsize=14,color=INK)
def box(rect,text,color="#e8f0f6",size=16):
    x,y,w,h=rect
    fig.add_artist(FancyBboxPatch((x,y),w,h,transform=fig.transFigure,
                   boxstyle="round,pad=0.012",facecolor=color,edgecolor="none"))
    fig.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size,color=INK)
box((.04,.39,.18,.20),r"$S_{11}=10$"+"\n"+r"$S_{22}=4$"+"\n"+r"$S_{12}=S_{21}=r$",size=14)
box((.37,.63,.23,.15),r"$10\cdot4-r^2$",size=19)
box((.76,.63,.19,.15),r"$40-r^2$",color="#d4e9e4",size=19)
box((.37,.20,.23,.15),r"$S_{11}=10,\ S_{22}=4$"+"\n"+r"$S_{12}=S_{21}=0$",size=14)
box((.76,.20,.19,.15),r"$40$",color="#f4ddce",size=19)
arrow(fig,(.24,.55),(.34,.705),BLUE)
arrow(fig,(.24,.43),(.34,.275),BLUE)
arrow(fig,(.63,.705),(.73,.705),BLUE)
arrow(fig,(.63,.275),(.73,.275),BLUE)
fig.text(.47,.82,tr("Построить M₂","Build M₂"),ha="center",fontsize=14,color=INK)
fig.text(.855,.82,tr("Спроецировать M₂","Project M₂"),ha="center",fontsize=14,color=INK)
fig.text(.47,.39,tr("Спроецировать L","Project L"),ha="center",fontsize=14,color=INK)
fig.text(.855,.39,tr("Построить M̂₂","Build M̂₂"),ha="center",fontsize=14,color=INK)
fig.text(.855,.54,r"$r=-4:\quad24\ne40$",ha="center",fontsize=18,color=ORANGE)
fig.text(.5,.08,tr("Готовый минор сохраняет r². Удаление r до построения минора теряет этот вклад.",
                   "The completed minor retains r². Removing r first loses that contribution."),
         ha="center",fontsize=12,color=INK)
assert 10*4-(-4)**2==24
save(fig,"Проекция грейда и грейд проекции","Projection of a grade and grade of a projection",
     tr("Два порядка операций дают коэффициенты 40-r² и 40 при форме второго грейда. При r=-4 они равны 24 и 40.",
        "Two orders of operations give coefficients 40-r² and 40 in a grade-two form. At r=-4 they are 24 and 40."))
