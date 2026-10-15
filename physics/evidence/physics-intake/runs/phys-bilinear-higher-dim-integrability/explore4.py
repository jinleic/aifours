import sys, random
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/scratch/ai4s-runs/phys-bilinear-higher-dim-integrability")
import explore1 as E1
import hirota_ns as H

Dx, Dy, Dt = H.DX, H.DY, H.DT
tests = [
    ("D_x(D_t+D_x^5+D_x^3)", Dx * (Dt + Dx**5 + Dx**3), {5: 1, 3: 1}, False),
    ("D_x(D_t+D_x^5+D_x^3+D_x)", Dx * (Dt + Dx**5 + Dx**3 + Dx), {5: 1, 3: 1, 1: 1}, False),
    ("D_x(D_t+D_x^5+2D_x^3)", Dx * (Dt + Dx**5 + 2 * Dx**3), {5: 1, 3: 2}, False),
    ("D_y(D_t+D_x^5+D_x^3)", Dy * (Dt + Dx**5 + Dx**3), {5: 1, 3: 1}, True),
    ("D_x(D_t+D_x^7+D_x^5)", Dx * (Dt + Dx**7 + Dx**5), {7: 1, 5: 1}, False),
]
for name, B, pc, wy in tests:
    for seed in (3, 4, 5):
        res = E1.single_test(B, pc, 3, seed=seed, with_y=wy)
        print(f"{name:28s} seed={seed} nonzero={len(res)}")
