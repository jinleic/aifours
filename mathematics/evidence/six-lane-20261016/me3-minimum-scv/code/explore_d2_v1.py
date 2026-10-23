"""EXPLORATORY (float64 numpy; not a certificate). Landscape of S = SCV on the D2 extreme-ray family.

Parametrization (real pole 1, pair -(1+delta) +- i omega, r = delta/omega, phi = omega*tau):
  c = (1 - i r) e^{(r - i) phi},  zeta = 1/(1 + omega (r - i)),  A_k = Re[c zeta^{k+1}],
  m_k = k! (1 - A_k),  1 + S = 2 (1-A0)(1-A2)/(1-A1)^2.
Feasibility: phi in [0, theta1(r)], theta1 = root of e^{r u}(cos u - r sin u) = 1 on (pi, 2 pi).
Reports: D1 (r=0) minimum and argmin; sublevel sets {S < T} for several T with their r/omega/phi extents; sign of
dS/dr (central differences at fixed omega, phi) on those sets; tail samples.
argv[1] = run directory; writes explore.json (exclusive create).
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


def S_of(r, w, phi):
    c = (1 - 1j * r) * np.exp((r - 1j) * phi)
    z = 1.0 / (1 + w * (r - 1j))
    A0 = np.real(c * z)
    A1 = np.real(c * z ** 2)
    A2 = np.real(c * z ** 3)
    return 2 * (1 - A0) * (1 - A2) / (1 - A1) ** 2 - 1, (1 - A0), (1 - A1), (1 - A2)


def theta1(r):
    if r == 0:
        return 2 * math.pi
    lo, hi = math.pi, 2 * math.pi
    g = lambda u: math.exp(r * u) * (math.cos(u) - r * math.sin(u)) - 1  # noqa: E731
    # g(pi) = -e^{r pi} - 1 < 0, g(2pi) = e^{2 pi r} - 1 > 0, g increasing on (pi, 2pi)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo


out = {}
# D1 landscape
ws = np.linspace(0.02, 6.0, 1200)
ph = np.linspace(0, 2 * math.pi, 2400, endpoint=False)
W, P = np.meshgrid(ws, ph, indexing="ij")
S0 = S_of(0.0, W, P)[0]
i, j = np.unravel_index(np.argmin(S0), S0.shape)
out["D1_grid_min"] = {"S": float(S0[i, j]), "omega": float(ws[i]), "phi": float(ph[j])}
# refine with Newton-free local grid
w0, p0 = ws[i], ph[j]
for scale in [0.01, 0.001, 0.0001, 0.00001, 0.000001]:
    wl = np.linspace(w0 - 5 * scale, w0 + 5 * scale, 201)
    pl = np.linspace(p0 - 5 * scale, p0 + 5 * scale, 201)
    WW, PP = np.meshgrid(wl, pl, indexing="ij")
    SS = S_of(0.0, WW, PP)[0]
    a, b = np.unravel_index(np.argmin(SS), SS.shape)
    w0, p0 = wl[a], pl[b]
out["D1_refined_min"] = {"S": float(S_of(0.0, w0, p0)[0]), "omega": float(w0), "phi": float(p0),
                         "1/S": float(1 / S_of(0.0, w0, p0)[0])}
vmin = float(S_of(0.0, w0, p0)[0])
# D1 min over phi as function of omega
prof = []
for wv in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0, 1.036, 1.1, 1.3, 1.6, 2.0, 3.0, 5.0, 10.0, 30.0, 100.0]:
    pp = np.linspace(0, 2 * math.pi, 20000, endpoint=False)
    s = S_of(0.0, wv, pp)[0]
    k = int(np.argmin(s))
    prof.append({"omega": wv, "min_S": float(s[k]), "phi": float(pp[k])})
out["D1_profile_min_over_phi"] = prof

# D2 grid: r log-ish, omega log, phi feasible
rs = np.concatenate([[1e-4, 1e-3, 3e-3], np.linspace(0.01, 0.2, 20), np.linspace(0.25, 2, 15), [3, 5, 10, 30, 100]])
wsg = np.exp(np.linspace(math.log(0.01), math.log(200), 160))
prof2 = []
setinfo = {T: {"count": 0, "r_max": 0.0, "w_min": 1e9, "w_max": 0.0, "phi_min": 1e9, "phi_max": 0.0,
               "dSdr_min": 1e9, "dSdr_neg_count": 0, "neg_examples": []} for T in (0.21, 0.22, 0.24, 0.25, 0.27, 0.3)}
global_min = (10.0, None)
for r in rs:
    th = theta1(float(r))
    pp = np.linspace(0, th, 1500)
    for wv in wsg:
        s, m0, m1, m2 = S_of(float(r), float(wv), pp)
        if np.any(m0 <= 0) or np.any(m1 <= 0):
            prof2.append({"r": float(r), "omega": float(wv), "WARN_nonpositive_moment": True})
        k = int(np.argmin(s))
        if s[k] < global_min[0]:
            global_min = (float(s[k]), {"r": float(r), "omega": float(wv), "phi": float(pp[k])})
        h = 1e-6 * max(1.0, r)
        if r > h:
            dS = (S_of(r + h, float(wv), pp)[0] - S_of(r - h, float(wv), pp)[0]) / (2 * h)
        else:
            dS = (S_of(r + h, float(wv), pp)[0] - S_of(r, float(wv), pp)[0]) / h
        for T, inf in setinfo.items():
            mask = s < T
            if np.any(mask):
                inf["count"] += int(mask.sum())
                inf["r_max"] = max(inf["r_max"], float(r))
                inf["w_min"] = min(inf["w_min"], float(wv))
                inf["w_max"] = max(inf["w_max"], float(wv))
                inf["phi_min"] = min(inf["phi_min"], float(pp[mask].min()))
                inf["phi_max"] = max(inf["phi_max"], float(pp[mask].max()))
                dm = dS[mask]
                inf["dSdr_min"] = min(inf["dSdr_min"], float(dm.min()))
                negs = np.where(dm <= 0)[0]
                inf["dSdr_neg_count"] += int(len(negs))
                if len(negs) and len(inf["neg_examples"]) < 8:
                    q = negs[0]
                    inf["neg_examples"].append({"r": float(r), "omega": float(wv), "phi": float(pp[mask][q]),
                                                "S": float(s[mask][q]), "dSdr": float(dm[q])})
out["D2_global_grid_min"] = {"S": global_min[0], "at": global_min[1]}
out["sublevel_sets"] = {str(T): v for T, v in setinfo.items()}
# tails: min over phi of S at extreme parameters
tails = []
for r in [0.0, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
    th = theta1(r)
    pp = np.linspace(0, th, 20001)
    for wv in [1e-4, 1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1e3, 1e4]:
        with np.errstate(all="ignore"):
            s = S_of(r, wv, pp)[0]
        good = np.isfinite(s)
        tails.append({"r": r, "omega": wv, "min_S": float(s[good].min()) if good.any() else None,
                      "phi_at_min": float(pp[good][np.argmin(s[good])]) if good.any() else None,
                      "theta1": th})
out["tails"] = tails
out["theta1_samples"] = {str(r): theta1(r) for r in [0, 1e-3, 0.01, 0.1, 0.5, 1, 2, 5, 10, 100]}
out["vmin_D1"] = vmin
out["elapsed"] = round(time.time() - t0, 2)
with lane_guard.xopen(RUN + "/explore.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("D1_refined_min", "D2_global_grid_min", "elapsed")}, indent=1))
for T, v in out["sublevel_sets"].items():
    print(T, {k: v[k] for k in v if k != "neg_examples"}, v["neg_examples"][:3])
