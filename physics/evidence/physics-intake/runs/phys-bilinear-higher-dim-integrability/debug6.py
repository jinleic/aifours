import sys, itertools, random
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/scratch/ai4s-runs/phys-bilinear-higher-dim-integrability")
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import explore3 as E3
import hirota_ns as H
import mpmath as mp
import sympy as sp

Dx, Dy, Dt = H.DX, H.DY, H.DT
P = Dt + Dx**2
rng = random.Random(1)
types = list("FFG")
for i in range(3):
    kq = sp.Rational(rng.randint(1, 29), rng.randint(3, 11)) * rng.choice((1, -1))
    w = E3.solve_w(P, kq, rng, sign=-1 if types[i] == "G" else 1)
    print(types[i], kq, w, "expected", (-kq**2 if types[i] == "F" else kq**2))
    rng.randint(1, 19); rng.randint(1, 7); rng.choice((1, -1)); rng.randint(1, 19); rng.randint(1, 7); rng.choice((1, -1))
