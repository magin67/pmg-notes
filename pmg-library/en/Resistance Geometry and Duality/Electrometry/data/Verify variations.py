"""Example for "Resistance Variations in Graphs and Continuous Media".

Run: python "Verify variations.py"
Requires SymPy. All calculations use exact arithmetic.
Vertices a,b,c,d are accessible; p,q are internal. The conductance of pq varies.
"""
from itertools import combinations
import sympy as s

labels = ('a', 'b', 'c', 'd', 'p', 'q')
t = s.symbols('t', positive=True)
eye = s.eye(len(labels))


def vector(a, b):
    return eye[:, labels.index(a)] - eye[:, labels.index(b)]


L = s.zeros(len(labels))
for a, b, conductance in [('a', 'p', 1), ('b', 'p', 1),
                          ('c', 'q', 1), ('d', 'q', 1), ('p', 'q', t)]:
    v = vector(a, b)
    L += conductance * v * v.T

# Direct Kirchhoff solution: ground q and solve the remaining equations exactly.
R = s.zeros(4)
potentials = {}
for i, j in combinations(range(4), 2):
    current = vector(labels[i], labels[j])
    u = (L[:-1, :-1].inv() * current[:-1, :]).col_join(s.zeros(1, 1))
    potentials[i, j] = u
    R[i, j] = R[j, i] = s.simplify(u[i] - u[j])

# Independently compute the response by eliminating internal vertices.
B = s.simplify(-L[4:, 4:].inv() * L[4:, :4])
P = s.eye(4).col_join(B)
K = s.simplify(L[:4, :4] + L[:4, 4:] * B)
assert s.simplify(P.T * L * P - K) == s.zeros(4)
mean = s.ones(4) / 4
Gr = s.simplify((K + mean).inv() - mean)
R_from_K = s.Matrix(4, 4, lambda i, j: Gr[i, i] + Gr[j, j] - 2 * Gr[i, j])
assert s.simplify(R_from_K - R) == s.zeros(4)

# Forward sensitivity: the squared voltage across the internal connecting edge.
for (i, j), u in potentials.items():
    assert s.simplify(s.diff(R[i, j], t) + (u[4] - u[5]) ** 2) == 0

# Projection of the variation and inverse variation through resistances.
dL = s.diff(L, t)
dK = s.simplify(s.diff(K, t))
dR = s.simplify(s.diff(R, t))
assert s.simplify(dK - P.T * dL * P) == s.zeros(4)
assert s.simplify(dK - K * dR * K / 2) == s.zeros(4)
w = s.simplify(P.T * vector('p', 'q'))
assert s.simplify(dK - w * w.T) == s.zeros(4)

# Full pair matrices of quadric connectivity and forward response at t=1.
K0, G0 = K.subs(t, 1), Gr.subs(t, 1)
pairs = list(combinations(range(4), 2))
v = [s.eye(4)[:, i] - s.eye(4)[:, j] for i, j in pairs]
S = s.Matrix(len(pairs), len(pairs), lambda i, j: (v[i].T * G0 * v[j])[0] ** 2)
Lq = s.Matrix(len(pairs), len(pairs), lambda a, b:
              (K0[pairs[a][0], pairs[b][0]] * K0[pairs[a][1], pairs[b][1]]
               + K0[pairs[a][0], pairs[b][1]] * K0[pairs[a][1], pairs[b][0]]) / 2)
assert S * Lq == s.eye(len(pairs))
dr = s.Matrix([dR[i, j].subs(t, 1) for i, j in pairs])
dc = s.Matrix([-dK[i, j].subs(t, 1) for i, j in pairs])
assert dc == -Lq * dr

rows = []
for i, j in pairs:
    rows.append([labels[i] + labels[j], str(R[i, j].subs(t, 1)),
                 str(dR[i, j].subs(t, 1)), str(-K[i, j].subs(t, 1)),
                 str(-dK[i, j].subs(t, 1))])

if __name__ == '__main__':
    print('All exact checks passed.')
    print('Pair; R at t=1; dR/dt; effective c; dc/dt')
    for row in rows:
        print('; '.join(row))
    print('Effective Laplacian at t=1:')
    s.pprint(K0)
