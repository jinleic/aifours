import sys, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
import mpmath as mp
from fractions import Fraction as Fr

mp.mp.dps = 60
Dx, Dy, Dt = H.DX, H.DY, H.DT
P = Dt + Dx**2
Bp, Bq = H.bpoly(P), H.bpoly(Dx * P)
k = [Fr(3, 2), Fr(-5, 7), Fr(2, 3)]
types = "FFG"
ws, a, b = [], [], []
for i, t in enumerate(types):
    w = -k[i] ** 2 if t == "F" else k[i] ** 2
    ws.append((k[i], Fr(0), w))
    a.append(Fr(2 + i) if t == "F" else Fr(0))
    b.append(Fr(0) if t == "F" else Fr(5 - i))
F, G = H.two_function_solution([Bp, Bq], ws, a, b)
res = H.residuals([Bp, Bq], ws, F, G)
print("exact residual entries:", res)
print("F", F)
print("G", G)
mws = [tuple(mp.mpf(c.numerator) / c.denominator for c in w) for w in ws]
ma = [mp.mpf(c.numerator) / c.denominator for c in a]
mb = [mp.mpf(c.numerator) / c.denominator for c in b]
cv = lambda B: {kk: mp.mpf(v.numerator) / v.denominator for kk, v in B.items()}
mF, mG = H.two_function_solution([cv(Bp), cv(Bq)], mws, ma, mb)
kap = H._kappa_table(mws)
for n in itertools.product((0, 1, 2), repeat=3):
    vals = [H.coefficient(cv(B), kap, mF, mG, n) for B in (Bp, Bq)]
    if any(abs(v) > 1e-40 for v in vals):
        print("float nonzero", n, [mp.nstr(v, 5) for v in vals])
