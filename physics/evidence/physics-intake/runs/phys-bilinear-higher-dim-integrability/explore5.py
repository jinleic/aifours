"""Symbolic two-amplitude 3-soliton coefficients for (2): P = D_t + D_x^3, M = D_y (structure hunting)."""
import sys, time
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
import sympy as sp
from sympy.polys.fields import field
from sympy import QQ

Dx, Dy, Dt = H.DX, H.DY, H.DT
N = 3
names = []
for i in range(1, N + 1):
    names += [f"k{i}", f"l{i}", f"a{i}", f"b{i}"]
K, *gens = field(",".join(names), QQ)
g = dict(zip(names, gens))
P = Dt + Dx**3
Bp, Bq = H.bpoly(P), H.bpoly(Dy * P)
ws = [(g[f"k{i}"], g[f"l{i}"], -g[f"k{i}"] ** 3) for i in range(1, N + 1)]
a = [g[f"a{i}"] for i in range(1, N + 1)]
b = [g[f"b{i}"] for i in range(1, N + 1)]
t0 = time.time()
F, G = H.two_function_solution([Bp, Bq], ws, a, b)
print("solved in", time.time() - t0)
t0 = time.time()
res = H.residuals([Bp, Bq], ws, F, G)
print("residual nonzero entries:", len(res), "time", time.time() - t0)
ks = [sp.Symbol(f"k{i}") for i in range(1, N + 1)]
for S in (3, 5, 6, 7):
    fs = sp.factor(sp.sympify(str(F[S].as_expr())))
    gs = sp.factor(sp.sympify(str(G[S].as_expr())))
    print(f"F[{S:03b}] =", fs)
    print(f"G[{S:03b}] =", gs)
