"""Does F_S / prod rho(k_i,k_j) depend on k at N = 4 (system (2), P = D_t + D_x^3)?"""
import sys, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr

Dx, Dy, Dt = H.DX, H.DY, H.DT
P = Dt + Dx**3
Bs = [H.bpoly(P), H.bpoly(Dy * P)]


def coeffs(ks, ls, a, b):
    waves = [(k, l, -k**3) for k, l in zip(ks, ls)]
    F, G = H.two_function_solution(Bs, waves, a, b)
    out = []
    for S in range(1 << len(ks)):
        idx = [i for i in range(len(ks)) if S >> i & 1]
        rho = Fr(1)
        for i, j in itertools.combinations(idx, 2):
            rho *= (ks[i] - ks[j]) / (ks[i] + ks[j])
        out.append((F[S] / rho, G[S] / rho))
    return out


ls = [Fr(1), Fr(3), Fr(7), Fr(12)]
a = [Fr(2), Fr(-1), Fr(5), Fr(3)]
b = [Fr(1), Fr(4), Fr(-2), Fr(7)]
c1 = coeffs([Fr(1), Fr(2), Fr(5), Fr(11)], ls, a, b)
c2 = coeffs([Fr(3), Fr(-7), Fr(4), Fr(9, 2)], ls, a, b)
for S in range(16):
    print(f"{S:04b}", c1[S] == c2[S], c1[S][0])
