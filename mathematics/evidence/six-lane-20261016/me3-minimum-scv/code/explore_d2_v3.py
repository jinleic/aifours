"""EXPLORATORY v3 (float64; not a certificate). Overflow-free epsilon form of S on the D2 family, regional minima.

1 + S = 2 (eps - B0)(eps - B2) / (eps - B1)^2, eps = e^{-r phi}, B_k = Re[(1 - i r) e^{-i phi} zeta^{k+1}],
zeta = 1/(1 + r w - i w)   (identical to the c-form after dividing all moments by e^{r phi}).
Regions are scanned on log grids in r and w and on phi in [0, theta1(r)] plus a tau-grid (phi = w tau) for small w.
Also: the D1 slice near phi = 0 and phi = 2 pi^- (wrap-around), and the boundary phi = theta1(r) family.
argv[1] = run directory; writes explore3.json (exclusive create).
"""
import sys
import json
import time
import math
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import numpy as np  # noqa: E402

RUN = sys.argv[1]
t0 = time.time()


def S_eps(r, w, phi):
    r = np.asarray(r, dtype=float)
    z = 1.0 / (1 + r * w - 1j * w)
    base = (1 - 1j * r) * np.exp(-1j * phi)
    eps = np.exp(-r * phi)
    B0 = np.real(base * z)
    B1 = np.real(base * z ** 2)
    B2 = np.real(base * z ** 3)
    return 2 * (eps - B0) * (eps - B2) / (eps - B1) ** 2 - 1


def theta1(r):
    if r == 0:
        return 2 * math.pi
    lo, hi = math.pi, 2 * math.pi
    g = lambda u: math.cos(u) - r * math.sin(u) - math.exp(-r * u)  # noqa: E731
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo


out = {}
# regional minima
rs_all = np.concatenate([[0.0], np.exp(np.linspace(math.log(1e-6), math.log(1e6), 400))])
ws_all = np.exp(np.linspace(math.log(1e-6), math.log(1e6), 400))
records = []
for r in rs_all:
    th = theta1(float(r))
    ph = np.concatenate([np.linspace(0, th, 800), th - np.exp(np.linspace(math.log(1e-12), math.log(min(1.0, th)), 200))])
    ph = ph[(ph >= 0) & (ph <= th)]
    for w in ws_all:
        # tau grid for small w: phi = w*tau
        tau = np.exp(np.linspace(math.log(1e-3), math.log(1e4), 300))
        ph2 = w * tau
        ph2 = ph2[ph2 <= th]
        P = np.concatenate([ph, ph2])
        with np.errstate(all="ignore"):
            s = S_eps(r, w, P)
        good = np.isfinite(s)
        k = int(np.argmin(np.where(good, s, np.inf)))
        records.append((float(r), float(w), float(s[k]), float(P[k])))
arr = np.array(records)


def regmin(mask):
    if not mask.any():
        return None
    sub = arr[mask]
    i = int(np.argmin(sub[:, 2]))
    return {"S": float(sub[i, 2]), "r": float(sub[i, 0]), "w": float(sub[i, 1]), "phi": float(sub[i, 3])}


R = arr[:, 0]
W = arr[:, 1]
reg = {}
for Wb in [1.5, 2, 3, 5, 10, 30, 100]:
    reg[f"w>={Wb}"] = regmin(W >= Wb)
for wb in [0.5, 0.4, 0.3, 0.2, 0.1, 0.03, 0.01, 1e-3]:
    reg[f"w<={wb}"] = regmin(W <= wb)
for Rb in [0.2, 0.3, 0.5, 1, 2, 4, 10, 100]:
    reg[f"r>={Rb}"] = regmin(R >= Rb)
    reg[f"r>={Rb},w>=0.3"] = regmin((R >= Rb) & (W >= 0.3))
reg["r<=0.3,0.3<=w<=3"] = regmin((R <= 0.3) & (W >= 0.3) & (W <= 3))
out["regional_minima"] = reg
# boundary family phi = theta1(r)
bnd = []
for r in [1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 0.03, 0.1, 0.3, 1, 3, 10, 100, 1e4]:
    th = theta1(r)
    ws = np.exp(np.linspace(math.log(1e-4), math.log(1e4), 4000))
    with np.errstate(all="ignore"):
        s = S_eps(r, ws, th)
    k = int(np.nanargmin(s))
    bnd.append({"r": r, "theta1": th, "min_S_on_boundary": float(s[k]), "w": float(ws[k])})
out["boundary_phi_eq_theta1"] = bnd
# D1 slice near phi=0 from both sides
d1 = []
for ph0 in [-0.3, -0.1, -0.03, -0.01, 0.0, 0.01, 0.03, 0.1]:
    ws = np.exp(np.linspace(math.log(1e-3), math.log(1e3), 20000))
    s = S_eps(0.0, ws, ph0)
    k = int(np.argmin(s))
    d1.append({"phi": ph0, "min_S": float(s[k]), "w": float(ws[k])})
out["D1_near_phi0"] = d1
out["elapsed"] = round(time.time() - t0, 2)
with lane_guard.xopen(RUN + "/explore3.json") as fh:
    json.dump(out, fh, indent=1)
for k, v in reg.items():
    print(k, v)
for b in bnd:
    print("bnd", b)
for d in d1:
    print("d1", d)
print("elapsed", out["elapsed"])
