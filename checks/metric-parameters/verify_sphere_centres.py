"""Exact checks for 'Sphere centres and graph heterogeneity' (SymPy required).
Run: python checks/metric-parameters/verify_sphere_centres.py
Add --figure OUTPUT.svg to reproduce the illustration (Matplotlib required).
"""
import sys
import sympy as S

def laplacian(n, edges):
    L = S.zeros(n)
    for i, j, c in edges:
        L[i, i] += c
        L[j, j] += c
        L[i, j] -= c
        L[j, i] -= c
    return L

def distances(A):
    n = A.rows
    d = A.diagonal().T
    one = S.ones(n, 1)
    return d * one.T + one * d.T - 2 * A

def direct_centre(D):
    """Solve the distance equations, independently of the degree formulas."""
    n = D.rows
    one = S.ones(n, 1)
    system = D.row_join(-2 * one).col_join(one.T.row_join(S.zeros(1, 1)))
    result = system.inv() * S.Matrix([0] * n + [1])
    return result[:n, :], result[n]

def analyse(L):
    n = L.rows
    one = S.ones(n, 1)
    P = S.eye(n) - S.ones(n) / n
    Gr = (L + S.ones(n) / n).inv() - S.ones(n) / n
    assert L * Gr == P and Gr * one == S.zeros(n, 1)
    d = L.diagonal().T
    avg = sum(d) / n
    b = d - avg * one
    beta, sigma = direct_centre(distances(L))
    alpha, rho = direct_centre(distances(Gr))
    phi = Gr * b
    DeltaL = (b.T * phi)[0] / 4
    q = Gr.diagonal().T
    DeltaR = (q.T * L * q)[0] / 4
    assert beta == one / n + phi / 2
    assert S.simplify(sigma - avg - DeltaL) == 0
    assert alpha == one / n + L * q / 2
    assert S.simplify(rho - S.trace(Gr) / n - DeltaR) == 0
    border = S.Matrix([[sigma]]).row_join(beta.T).col_join(beta.row_join(Gr))
    inverse = S.zeros(1).row_join(one.T).col_join(one.row_join(-distances(L) / 2))
    assert border * inverse == S.eye(n + 1)
    return beta, sigma, alpha, rho, DeltaL, DeltaR

cases = {
    "P4": (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
    "K1,3": (4, [(0, 1, 1), (0, 2, 1), (0, 3, 1)]),
    "C4": (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]),
    "triangle 1,2,3": (3, [(0, 1, 1), (0, 2, 2), (1, 2, 3)]),
    "triangle 7,1,1": (3, [(0, 1, 7), (0, 2, 1), (1, 2, 1)]),
}
for name, (n, edges) in cases.items():
    beta, sigma, alpha, rho, dl, dr = analyse(laplacian(n, edges))
    print(name, "beta=", list(beta), "sigma=", sigma,
          "alpha=", list(alpha), "rho=", rho, "DeltaL=", dl, "DeltaR=", dr)

# Two symbolic weak-cut families.
eps = S.symbols("eps", positive=True)
L = laplacian(3, [(0, 1, 1), (1, 2, eps)])
n = 3
one = S.ones(n, 1)
Gr = (L + S.ones(n) / n).inv() - S.ones(n) / n
d = L.diagonal().T
b = d - sum(d) * one / n
phi = S.simplify(Gr * b)
dl = S.factor((b.T * phi)[0] / 4)
assert S.simplify((phi[1] - phi[2]) / 2 - (2 - eps) / (6 * eps)) == 0
assert S.simplify(dl - ((1 - 2*eps)**2 + (2-eps)**2/eps)/36) == 0
assert S.limit(eps * dl, eps, 0) == S.Rational(1, 9)
print("weak P3: DeltaL=", dl)
L4 = laplacian(4, [(0, 1, 1-eps), (1, 2, eps),
                   (2, 3, 1-eps), (3, 0, eps)])
assert L4.diagonal() == S.ones(1, 4)
assert distances(L4) * (S.ones(4, 1)/4) == 2*S.ones(4, 1)
assert L4 * S.Matrix([1, 1, -1, -1]) == 2*eps*S.Matrix([1, 1, -1, -1])
print("regular weak-cut C4: beta=1/4, sigma=1, DeltaL=0")

# Exact diffusion normalization on P3.
t = S.symbols("t", nonnegative=True)
L3 = laplacian(3, [(0, 1, 1), (1, 2, 1)])
b3 = S.Matrix([-S.Rational(1, 3), S.Rational(2, 3), -S.Rational(1, 3)])
y = S.exp(-3*t)*b3
assert S.diff(y, t) == -L3*y
assert S.integrate((y.T*y)[0], (t, 0, S.oo))/2 == S.Rational(1, 18)

# P25.01 adjacency list, from Brouwer's public catalogue:
# https://aeb.win.tue.nl/graphs/paulus/p25_01
rows = [
[1,2,3,4,5,6,7,8,9,10,11,12],
[0,2,3,4,5,6,13,14,15,16,17,18],
[0,1,3,4,5,6,19,20,21,22,23,24],
[0,1,2,7,8,9,13,14,15,19,20,21],
[0,1,2,7,10,11,13,16,17,19,22,23],
[0,1,2,8,10,12,14,16,18,20,22,24],
[0,1,2,9,11,12,15,17,18,21,23,24],
[0,3,4,8,9,10,13,15,18,22,23,24],
[0,3,5,7,9,11,14,16,17,21,22,24],
[0,3,6,7,8,12,16,17,18,19,20,23],
[0,4,5,7,11,12,13,14,18,20,21,23],
[0,4,6,8,10,12,14,15,17,19,21,22],
[0,5,6,9,10,11,13,15,16,19,20,24],
[1,3,4,7,10,12,15,16,17,20,21,24],
[1,3,5,8,10,11,15,16,18,19,21,23],
[1,3,6,7,11,12,13,14,18,19,22,24],
[1,4,5,8,9,12,13,14,17,19,23,24],
[1,4,6,8,9,11,13,16,18,20,21,22],
[1,5,6,7,9,10,14,15,17,20,22,23],
[2,3,4,9,11,12,14,15,16,20,22,23],
[2,3,5,9,10,12,13,17,18,19,21,22],
[2,3,6,8,10,11,13,14,17,20,23,24],
[2,4,5,7,8,11,15,17,18,19,20,24],
[2,4,6,7,9,10,14,16,18,19,21,24],
[2,5,6,7,8,12,13,15,16,21,22,23],
]
A = S.zeros(25)
for i, rr in enumerate(rows):
    for j in rr:
        A[i, j] = 1
E = S.ones(25)
assert A == A.T and A*A == 6*S.eye(25)-A+6*E
L = 12*S.eye(25)-A
Gr = (13*S.eye(25)+A-E)/150
assert L*Gr == S.eye(25)-E/25
assert Gr*S.ones(25, 1) == S.zeros(25, 1)
assert Gr.diagonal() == S.ones(1, 25)*S.Rational(2, 25)
print("P25.01: exact strongly-regular identity; both centre displacements vanish")
print("All exact checks passed.")

def draw_figure(filename):
    import os
    from pathlib import Path
    os.environ.setdefault("MPLCONFIGDIR", str(Path(filename).resolve().parent / "mplconfig"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle, Polygon
    import numpy as np
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":11,
                         "svg.fonttype":"none", "axes.titleweight":"bold"})
    fig, axes = plt.subplots(1, 3, figsize=(13.8, 5.2))
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")
    blue="#2166ac"; amber="#c87517"; ink="#334155"
    net=np.array([[-1.,0.],[1.,0.],[0.,1.6]])
    for i,j,w in [(0,1,7),(0,2,1),(1,2,1)]:
        axes[0].plot(net[[i,j],0],net[[i,j],1],color=ink,lw=1.3+w/3)
        mid=(net[i]+net[j])/2
        off=np.array([0.,-.14]) if w==7 else np.array([-.12 if i==0 else .12,0])
        axes[0].text(*(mid+off),str(w),ha="center",va="center",
                     bbox={"facecolor":"white","edgecolor":"none","pad":2})
    axes[0].scatter(net[:,0],net[:,1],s=340,facecolor="white",edgecolor=ink,lw=1.8,zorder=4)
    for i,p in enumerate(net): axes[0].text(*p,str(i+1),ha="center",va="center",zorder=5)
    axes[0].set_xlim(-1.6,1.6);axes[0].set_ylim(-.8,2.4)
    axes[0].set_title("Исходная сеть",pad=18)
    axes[0].text(.5,-.10,"Проводимости: 7, 1, 1",transform=axes[0].transAxes,ha="center")
    data=[
      (np.sqrt(2/15),np.sqrt(.5),np.array([4,4,7])/15,
       "Резистивный симплекс",r"$\alpha=(4,4,7)/15,\quad \rho=32/225$"),
      (np.sqrt(30),3/np.sqrt(2),np.array([2,2,-1])/3,
       "Лапласиановый симплекс",r"$\beta=(2,2,-1)/3,\quad \sigma=8$")]
    for ax,(base,height,coords,title,caption) in zip(axes[1:],data):
        pts=np.array([[-base/2,0],[base/2,0],[0,height]])
        centre=coords@pts; centroid=pts.mean(axis=0)
        radius=np.linalg.norm(pts[0]-centre)
        ax.add_patch(Circle(centre,radius,fill=False,color=blue,lw=1.4,ls=(0,(4,3))))
        ax.add_patch(Polygon(pts,closed=True,facecolor="#eef4f9",edgecolor=ink,lw=1.6))
        ax.plot([centroid[0],centre[0]],[centroid[1],centre[1]],color=amber,lw=2)
        ax.scatter(pts[:,0],pts[:,1],s=45,facecolor="white",edgecolor=ink,zorder=4)
        for i,p in enumerate(pts):
            off=np.array([-.07*radius if i==0 else .07*radius if i==1 else 0,
                          -.10*radius if i<2 else .12*radius])
            ax.text(*(p+off),str(i+1),ha="center",va="center")
        ax.scatter(*centroid,s=42,color=amber,zorder=5)
        ax.scatter(*centre,s=48,color=blue,marker="D",zorder=6)
        ax.text(centre[0]+.12*radius,centre[1],"O",color=blue,va="center")
        ax.text(centroid[0]+.12*radius,centroid[1],"h",color=amber,va="center")
        ax.set_xlim(centre[0]-1.28*radius,centre[0]+1.28*radius)
        ax.set_ylim(centre[1]-1.28*radius,centre[1]+1.28*radius)
        ax.set_title(title,pad=18)
        ax.text(.5,-.10,caption,transform=ax.transAxes,ha="center")
    fig.text(.5,.035,"O - центр описанной окружности; h - центроид. Масштабы геометрических панелей независимы.",
             ha="center",color=ink,fontsize=10)
    fig.subplots_adjust(left=.025,right=.985,bottom=.19,top=.86,wspace=.3)
    fig.savefig(filename,metadata={"Date":None},facecolor="white")
    fig.savefig(str(Path(filename).with_suffix(".png")),dpi=140,facecolor="white")
    plt.close(fig)

if "--figure" in sys.argv:
    draw_figure(sys.argv[sys.argv.index("--figure")+1])
