"""Draw the C4 projector figures after exact rational verification.

Requires Matplotlib. SVGs are saved beside the Russian note. Optional PNG
previews are written to --preview-dir. No network access is used.
"""
import argparse
from figure_language import prepare_figure, output_directory
from fractions import Fraction as F
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from verify_projectors import check

parser = argparse.ArgumentParser()
parser.add_argument("--preview-dir",type=Path)
parser.add_argument("--lang", choices=("ru", "en"), default="ru")
args = parser.parse_args()
data = check()
out = output_directory(args.lang)
if args.preview_dir:
    args.preview_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.fonttype":"none",
                     "svg.hashsalt":"PMG-spectral-C4","axes.spines.top":False,"axes.spines.right":False})
BLUE,ORANGE,TEAL,GREY,INK = "#216b9f","#bb4e28","#25857e","#7a8993","#19354a"
PALE,BORDER = "#edf4f8","#bdcbd5"


def save(fig,name,description):
    name, description = prepare_figure(fig, name, description, args.lang)
    path = out/(name+".svg")
    fig.savefig(path,metadata={"Date":None,"Description":description})
    svg = path.read_text(encoding="utf-8")
    start = svg.index(">",svg.index("<svg"))+1
    svg = svg[:start]+f"\n<title>{escape(name)}</title>\n<desc>{escape(description)}</desc>"+svg[start:]
    with path.open("w",encoding="utf-8",newline="\n") as f:
        f.write("\n".join(line.rstrip() for line in svg.splitlines())+"\n")
    if args.preview_dir:
        fig.savefig(args.preview_dir/(name+".png"),dpi=140)
    plt.close(fig)
    print(path.name)


def mode_graph(ax,raw,norm,title):
    coords=[(-1,1),(1,1),(1,-1),(-1,-1)]
    for i,j in [(0,1),(1,2),(2,3),(3,0)]:
        ax.plot([coords[i][0],coords[j][0]],[coords[i][1],coords[j][1]],color=BORDER,lw=2.5,zorder=1)
    for i,((x,y),v) in enumerate(zip(coords,raw)):
        color=BLUE if v>0 else ORANGE if v<0 else GREY
        ax.scatter(x,y,s=490,color=color,edgecolor="white",linewidth=1.4,zorder=2)
        ax.text(x,y,str(i+1),ha="center",va="center",color="white",fontsize=11,zorder=3)
        label="0" if not v else ("+" if v>0 else "−")+("1/√2" if norm==2 else "1/2")
        ax.text(x,y+(0.48 if y>0 else -0.48),label,ha="center",va="center",fontsize=12,color=INK)
    ax.set(xlim=(-1.65,1.65),ylim=(-1.82,1.85),aspect="equal")
    ax.axis("off"); ax.set_title(title,fontsize=19,color=INK,pad=5)


fig=plt.figure(figsize=(11.8,8.4),facecolor="white")
gs=fig.add_gridspec(2,3,width_ratios=[1,1,1.35],left=.05,right=.96,top=.79,bottom=.15,wspace=.34,hspace=.36)
for col in range(2):
    mode_graph(fig.add_subplot(gs[0,col]),data["raw_modes"][col],data["squared_lengths"][col],[r"$\mathbf{u}$",r"$\mathbf{v}$"][col])
    mode_graph(fig.add_subplot(gs[1,col]),data["rotated_modes"][col],data["rotated_squared_lengths"][col],[r"$\widetilde{\mathbf{u}}$",r"$\widetilde{\mathbf{v}}$"][col])
ax=fig.add_subplot(gs[:,2])
matrix=[[float(F(v)) for v in row] for row in data["E2"]]
cmap=LinearSegmentedColormap.from_list("signed",["#f4d9cb","#ffffff","#bdd9ec"])
ax.imshow(matrix,cmap=cmap,vmin=-.5,vmax=.5)
ax.set_xticks(range(4),labels=range(1,5)); ax.set_yticks(range(4),labels=range(1,5))
ax.tick_params(length=0)
for i,row in enumerate(data["E2"]):
    for j,v in enumerate(row):
        ax.text(j,i,v.replace("-","−"),ha="center",va="center",fontsize=15,color=INK)
for spine in ax.spines.values(): spine.set_visible(False)
ax.set_title("Общий проектор "+r"$\mathbf{E}_2$",fontsize=17,pad=22,color=INK)
ax.set_xlabel(r"$\mathbf{E}_2^2=\mathbf{E}_2,\quad\mathrm{rank}\,\mathbf{E}_2=2$",fontsize=14,labelpad=25,color=INK)
fig.text(.05,.945,"Цикл C₄: разные моды, одно подпространство",fontsize=21,weight="bold",color=INK)
fig.text(.05,.884,"Собственное число 2. Сверху исходный базис, снизу поворот на 45°.",fontsize=13,color=INK)
fig.text(.05,.073,r"$\mathbf{u}\mathbf{u}^{\mathsf{T}}+\mathbf{v}\mathbf{v}^{\mathsf{T}}"
         r"=\widetilde{\mathbf{u}}\widetilde{\mathbf{u}}^{\mathsf{T}}+\widetilde{\mathbf{v}}\widetilde{\mathbf{v}}^{\mathsf{T}}=\mathbf{E}_2$",fontsize=19,color=INK)
save(fig,"Два базиса и общий проектор цикла C4",
     "Два базиса H2: (1,0,-1,0)/√2 и (0,1,0,-1)/√2; (1,1,-1,-1)/2 и (-1,1,1,-1)/2. Их суммы матриц ранга один дают одинаковый проектор E2 ранга 2.")

fig=plt.figure(figsize=(12.4,7.4),facecolor="white")
ax=fig.add_axes([.03,.20,.94,.57]); ax.set(xlim=(-.6,14.5),ylim=(-.5,4.0)); ax.axis("off")
colors={0:"#f0f2f4",1:"#e3eff8",2:"#e0f2ee",3:"#fae5d9"}
left={(0,0):r"e",(1,0):r"2S_{2,1}",(2,0):r"4S_{2,2}",
      (0,1):r"4S_{4,1}",(1,1):r"8S_{2,1}S_{4,1}",(2,1):r"16S_{2,2}S_{4,1}"}
right={(0,0):r"e",(1,0):r"\frac{1}{2}S_{2,1}^{\vee}",(2,0):r"\frac{1}{4}S_{2,2}^{\vee}",
       (0,1):r"\frac{1}{4}S_{4,1}^{\vee}",(1,1):r"\frac{1}{8}S_{2,1}^{\vee}S_{4,1}^{\vee}",
       (2,1):r"\frac{1}{16}S_{2,2}^{\vee}S_{4,1}^{\vee}"}
for side,offset,forms in [("M",0,left),("D",7.7,right)]:
    ax.text(offset+2.7,3.65,r"$M=\exp L$" if side=="M" else r"$D=\exp Q_1$",ha="center",fontsize=20,color=INK)
    for k in range(3):
        ax.text(offset+1.85*k+.85,-.27,str(k),ha="center",fontsize=13,color=INK)
    ax.text(offset+2.7,-.58,r"$k_2$"+" - число направлений из H₂",ha="center",fontsize=12,color=INK)
    for l in range(2):
        ax.text(offset-.22,1.4*l+.7,str(l),ha="center",va="center",fontsize=13,color=INK)
    ax.text(offset-.22,3.02,r"$k_4$",ha="center",va="center",fontsize=13,color=INK)
    for (k,l),term in forms.items():
        x,y=offset+1.85*k,1.4*l
        g=k+l
        color=colors[g if side=="M" else 3-g]
        ax.add_patch(FancyBboxPatch((x,y),1.7,1.23,boxstyle="round,pad=0.04",facecolor=color,edgecolor="white"))
        ax.text(x+.85,y+.70,"$"+term+"$",ha="center",va="center",fontsize=14.5,color=INK)
        ax.text(x+.85,y+.17,f"грейд {g}",ha="center",fontsize=10,color=GREY)
ax.add_patch(FancyArrowPatch((5.65,1.32),(7.32,1.32),arrowstyle="-|>",mutation_scale=19,lw=1.8,color=GREY))
ax.text(6.48,1.77,"дополнение",ha="center",fontsize=10,color=INK)
ax.text(6.48,.82,"коэффициент / 16",ha="center",fontsize=9.5,color=GREY)
fig.text(.05,.94,"Грейды C₄: выбор и дополнение направлений",fontsize=21,weight="bold",color=INK)
fig.text(.05,.865,r"$m_2=2,\quad m_4=1,\qquad (k_2,k_4)\longmapsto(2-k_2,1-k_4),\qquad\Delta=16$",fontsize=17,color=INK)
fig.text(.05,.106,"Одинаковый цвет связывает дополнительные грейды. Соответствующие ячейки\nзанимают противоположные позиции в двух сетках.",fontsize=12,color=INK)
fig.text(.05,.037,r"$S_{2,1}=A+B,\quad S_{2,2}=AB,\quad S_{4,1}=C$",fontsize=16,color=INK)
save(fig,"Грейды и дополнение направлений цикла C4",
     "Две сетки 3 на 2 показывают вклады собственных подпространств в M и D. Координаты k2=0,1,2 и k4=0,1. Дополнение отражает обе координаты и делит коэффициент прямой формы на 16.")

fig,(ax,bx)=plt.subplots(1,2,figsize=(11.7,6.2),facecolor="white",gridspec_kw={"width_ratios":[1.05,1]})
fig.subplots_adjust(left=.08,right=.97,top=.72,bottom=.28,wspace=.36)
res=[[float(F(v)) for v in row] for row in data["resistance_contributions"]]
for i,row in enumerate(res):
    y=1-i
    ax.barh(y,row[0],height=.38,color=BLUE,label="H₂" if i==0 else None)
    ax.barh(y,row[1],left=row[0],height=.38,color=ORANGE,label="H₄" if i==0 else None)
    ax.text(row[0]/2,y,data["resistance_contributions"][i][0],ha="center",va="center",color="white",fontsize=15)
    if row[1]: ax.text(row[0]+row[1]/2,y,"1/4",ha="center",va="center",color="white",fontsize=14)
    ax.text(sum(row)+.035,y,"3/4" if i==0 else "1",va="center",color=INK,fontsize=16,weight="bold")
ax.set_yticks([1,0],labels=["Пара 1,2","Пара 1,3"])
ax.set(xlim=(0,1.18),ylim=(-.55,1.55),xlabel="Вклад в резистенс")
ax.set_title("Вклады подпространств",fontsize=16,pad=19,color=INK)
ax.spines['left'].set_visible(False); ax.tick_params(axis="y",length=0)
ax.legend(loc="upper left",bbox_to_anchor=(0,-.24),ncol=2,frameon=False)
modal=[[float(F(v)) for v in row] for row in data["mode_contributions"]]
for i,row in enumerate(modal):
    y=1-i
    bx.barh(y,row[0],height=.38,color=TEAL)
    bx.barh(y,row[1],left=row[0],height=.38,color="#73b9b3")
    if row[0]: bx.text(row[0]/2,y,"1/4",ha="center",va="center",color="white",fontsize=15)
    bx.text(row[0]+row[1]/2,y,"1/4" if i==0 else "1/2",ha="center",va="center",color=INK,fontsize=15)
    bx.text(.525,y,"= 1/2",va="center",color=INK,fontsize=15,weight="bold")
bx.set_yticks([1,0],labels=[r"$u,\ v$",r"$\widetilde u,\ \widetilde v$"])
bx.set(xlim=(0,.69),ylim=(-.55,1.55),xlabel="Вклад отдельных мод H₂ в R₁₂")
bx.set_title("Два базиса одного H₂",fontsize=16,pad=19,color=INK)
bx.spines['left'].set_visible(False); bx.tick_params(axis="y",length=0)
bx.text(0,-1.13,"Тёмный: первая мода. Светлый: вторая.",fontsize=10,color=GREY)
fig.text(.05,.94,"Резистенсы C₄: вклады подпространств и мод",fontsize=20,weight="bold",color=INK)
fig.text(.05,.855,"Отдельные моды меняют вклады при повороте базиса. Их сумма сохраняется.",fontsize=12,color=INK)
fig.text(.05,.045,"У противоположных вершин вклад H₄ равен нулю: компоненты моды w совпадают.",fontsize=12,color=INK)
save(fig,"Спектральные вклады в резистенсы цикла C4",
     "Резистенс соседних вершин 3/4=1/2+1/4, противоположных 1=1+0 по подпространствам H2 и H4. Вклад H2 в R12 разбивается на 1/4+1/4 в исходном базисе и 0+1/2 после поворота.")
