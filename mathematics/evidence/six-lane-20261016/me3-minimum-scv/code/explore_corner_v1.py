"""EXPLORATORY (mpmath, points only): margins of the corner-series quantities.

Psi = Phi/(w |xi|^2) and Ig = Im g / w computed directly from W (no series) at points, for s in a grid, and
(delta, w) in [0, 0.3] x (0, 0.2]; reports max_s Psi, min_s Ig per (delta, w), and the global worst.
argv[1] = run directory; writes corner.json (exclusive create).
"""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
mp.mp.dps = 40
kap = mp.mpf(50) / 61


def W(s, xi):
    N1 = kap * s * s - 2 * s * (1 - s) + 2 * (1 - s) ** 2
    zz = 1 / (1 + xi)
    return zz * (kap * s * s / N1 + zz * (-2 * s * (1 - s) / N1 + zz * 2 * (1 - s) ** 2 / N1))


rows = []
worst_psi = (-mp.inf, None)
worst_ig = (mp.inf, None)
for di in range(0, 31):
    d = mp.mpf(di) / 100
    for wi in range(1, 21):
        w = mp.mpf(wi) / 100
        xi = d - 1j * w
        mpsi, mig = -mp.inf, mp.inf
        for si in range(0, 201):
            s = mp.mpf(si) / 200
            g = mp.log(W(s, xi))   # principal log; near 1 here
            psi = (w * g.real + d * g.imag) / (w * (d * d + w * w))
            ig = g.imag / w
            if psi > mpsi:
                mpsi, sp = psi, s
            if ig < mig:
                mig = ig
        rows.append({"delta": float(d), "w": float(w), "max_psi": float(mpsi), "s_at": float(sp), "min_ig": float(mig)})
        if mpsi > worst_psi[0]:
            worst_psi = (mpsi, (float(d), float(w), float(sp)))
        if mig < worst_ig[0]:
            worst_ig = (mig, (float(d), float(w)))
out = {"worst_psi": [float(worst_psi[0]), worst_psi[1]], "worst_ig": [float(worst_ig[0]), worst_ig[1]], "rows": rows}
with lane_guard.xopen(RUN + "/corner.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("worst_psi", "worst_ig")}))
bad = [r for r in rows if r["max_psi"] > -0.005]
print("near-zero or positive psi rows:", len(bad), bad[:20])
