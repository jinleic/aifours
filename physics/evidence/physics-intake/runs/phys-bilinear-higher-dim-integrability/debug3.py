import sys, random, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
import mpmath as mp
from fractions import Fraction as Fr

mp.mp.dps = 60
Dx, Dy, Dt = H.DX, H.DY, H.DT
P = Dt + Dx**3
Bp, Bq = H.bpoly(P), H.bpoly(Dx * P)
rng = random.Random(1)
ws, a, b = [], [], []
for i in range(3):
    k = Fr(rng.randint(1, 29), rng.randint(3, 11)) * rng.choice((1, -1))
    w = -k**3
    ws.append((k, Fr(0), w))
    a.append(Fr(rng.randint(1, 19), rng.randint(1, 7)) * rng.choice((1, -1)))
    b.append(Fr(rng.randint(1, 19), rng.randint(1, 7)) * rng.choice((1, -1)))
print(ws, a, b)
F, G = H.two_function_solution([Bp, Bq], ws, a, b)
res = H.residuals([Bp, Bq], ws, F, G)
print("exact nonzero:", len(res))
# same in mpmath
mws = [tuple(mp.mpf(c.numerator) / c.denominator for c in w) for w in ws]
ma = [mp.mpf(c.numerator) / c.denominator for c in a]
mb = [mp.mpf(c.numerator) / c.denominator for c in b]
mBp = {k: mp.mpf(v.numerator) / v.denominator for k, v in Bp.items()}
mBq = {k: mp.mpf(v.numerator) / v.denominator for k, v in Bq.items()}
mF, mG = H.two_function_solution([mBp, mBq], mws, ma, mb)
for S in range(8):
    print(S, float(F[S]), mp.nstr(mF[S], 15), float(G[S]), mp.nstr(mG[S], 15))
