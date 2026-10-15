"""Sectors b_i = eps_i a_i for P = D_t + D_x^5 (and D_t + D_x^3): which pass the 3-soliton test?"""
import sys, itertools, random
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr

Dx, Dy, Dt = H.DX, H.DY, H.DT
for n in (3, 5, 7):
    P = Dt + Dx**n
    for mname, M in (("(1)", Dx), ("(2)", Dy)):
        Bs = [H.bpoly(P), H.bpoly(M * P)]
        passing = []
        for eps in itertools.product((1, -1), repeat=3):
            ok = True
            for seed in (1, 2):
                rng = random.Random(seed)
                ks = [[Fr(1), Fr(-5, 2), Fr(7, 3)], [Fr(2), Fr(3, 4), Fr(-9, 5)]][seed - 1]
                ls = [[Fr(1), Fr(3), Fr(7)], [Fr(2), Fr(5), Fr(-11, 3)]][seed - 1] if M == Dy else [Fr(0)] * 3
                a = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(3)]
                b = [e * x for e, x in zip(eps, a)]
                waves = [(k, l, -k**n) for k, l in zip(ks, ls)]
                F, G = H.two_function_solution(Bs, waves, a, b)
                if H.residuals(Bs, waves, F, G):
                    ok = False
            if ok:
                passing.append(eps)
        print(f"P=D_t+D_x^{n} {mname}: passing sectors b_i = eps_i a_i: {passing}")
