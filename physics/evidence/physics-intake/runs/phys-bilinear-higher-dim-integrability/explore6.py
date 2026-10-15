import sys, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/scratch/ai4s-runs/phys-bilinear-higher-dim-integrability")
import explore2 as E2
import hirota_ns as H

Dx, Dy, Dt = H.DX, H.DY, H.DT
cases = {
    "Dt+Dx^5 (F/G patterns)": Dt + Dx**5,
    "Dt+Dx^5+Dx^2": Dt + Dx**5 + Dx**2,
    "Dt+Dx^5+Dx^4": Dt + Dx**5 + Dx**4,
    "Dt+Dx^4+Dx^3": Dt + Dx**4 + Dx**3,
    "Dt+Dx^4": Dt + Dx**4,
    "Dt+Dx^6": Dt + Dx**6,
    "Dt+Dx^7+Dx^2": Dt + Dx**7 + Dx**2,
    "Dt+Dx^3+Dx^2+Dx": Dt + Dx**3 + Dx**2 + Dx,
    "Dt+Dx^2+Dx": Dt + Dx**2 + Dx,
}
for name, P in cases.items():
    for Mn, M in (("(1)", Dx), ("(2)", Dy)):
        fails = []
        for pat in itertools.product("FG", repeat=3):
            r = [E2.test_system(P, M, 3, s, pat) for s in (1, 2, 3)]
            if any(x != "PASS" for x in r):
                fails.append("".join(pat) + ":" + "/".join(sorted(set(r))))
        print(f"{name:26s} {Mn} failing patterns: {fails if fails else 'none'}")
