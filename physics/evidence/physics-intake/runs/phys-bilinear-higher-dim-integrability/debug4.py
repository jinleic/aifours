import sys, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/scratch/ai4s-runs/phys-bilinear-higher-dim-integrability")
import explore2 as E2
import explore3 as E3
import hirota_ns as H

Dx, Dy, Dt = H.DX, H.DY, H.DT
for P in (Dt + Dx**2, Dt + Dx**2 + Dx**3, Dt + Dx * Dt + Dx**3):
    for M in (Dx, Dy):
        for pat in itertools.product("FG", repeat=3):
            ex = [E2.test_system(P, M, 3, s, pat) for s in range(1, 6)]
            fl = [E3.run(P, M, 3, s, list(pat)).split("(")[0] for s in range(1, 6)]
            print(P, M, "".join(pat), "exact:", sorted(set(ex)), "float:", sorted(set(fl)))
