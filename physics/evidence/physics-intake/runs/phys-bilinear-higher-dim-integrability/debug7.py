import sys, itertools, random
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/scratch/ai4s-runs/phys-bilinear-higher-dim-integrability")
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import explore3 as E3
import hirota_ns as H
import mpmath as mp
import sympy as sp

Dx, Dy, Dt = H.DX, H.DY, H.DT
P, M = Dt + Dx**2, Dx
rng = random.Random(1)
types = list("FFG")
Bp = E3.to_mp_poly(H.bpoly(P)); Bq = E3.to_mp_poly(H.bpoly(sp.expand(M * P)))
ws, a, b = [], [], []
for i in range(3):
    kq = sp.Rational(rng.randint(1, 29), rng.randint(3, 11)) * rng.choice((1, -1))
    k = mp.mpf(kq.p) / kq.q
    l = mp.mpf(0)
    w = E3.solve_w(P, kq, rng, sign=-1 if types[i] == "G" else 1)
    ws.append((k, l, w))
    ai = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
    bi = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
    if types[i] == "F": bi = mp.mpf(0)
    if types[i] == "G": ai = mp.mpf(0)
    a.append(ai); b.append(bi)
print([tuple(mp.nstr(c, 8) for c in w) for w in ws], [mp.nstr(x, 6) for x in a], [mp.nstr(x, 6) for x in b])
print("types of w:", [type(w[2]) for w in ws])
F, G = H.two_function_solution([Bp, Bq], ws, a, b)
kap = H._kappa_table(ws)
for n in itertools.product((0, 1, 2), repeat=3):
    vals = [H.coefficient(B, kap, F, G, n) for B in (Bp, Bq)]
    if any(abs(v) > 1e-40 for v in vals):
        print("nonzero", n, [mp.nstr(v, 5) for v in vals])
