"""Float64 finite-M evaluation of a saved Gaussian-limit code at a given eta (exploration only)."""
import argparse, json, time
import numpy as np, torch
from finite import finite_ic

ap = argparse.ArgumentParser()
ap.add_argument("code"); ap.add_argument("--eta", type=float, required=True)
ap.add_argument("--Ms", required=True); ap.add_argument("--D", type=int, required=True)
ap.add_argument("--q", default=None); ap.add_argument("--zero_below", type=float, default=0.0)
a = ap.parse_args()
st = torch.load(a.code); K = st["K"]; n = np.arange(K + 1)
cs = []
for v, r in zip(st["vs"], st["res"]):
    w = v.numpy() * ((n % st["k"]) == r); w = w / np.linalg.norm(w)
    w[np.abs(w) < a.zero_below] = 0.0
    cs.append(w / np.linalg.norm(w))
q = [float(x) for x in a.q.split(",")] if a.q else torch.softmax(st["theta"], 0).tolist()
for M in [int(x) for x in a.Ms.split(",")]:
    t0 = time.time()
    f, res, dr = finite_ic(M, a.eta, cs, q, D=min(a.D, M), k=st["k"], residues=st["res"], ptail=1e-15, pitail=1e-17)
    print(json.dumps({"code": a.code, "eta": a.eta, "M": M, "D": a.D, "q": q, "Ic": f, "sectors": len(res),
                      "maxflag": max(max(r.flag) for r in res), "secs": round(time.time() - t0, 1)}), flush=True)
