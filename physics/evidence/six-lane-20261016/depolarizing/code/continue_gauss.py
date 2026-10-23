"""Warm-started continuation in eta for modular single-mode codes (float64 exploration).

python continue_gauss.py --init ../evidence/gauss/m3_r01_eta0750.pt --etas 0.745,0.74,... --iters 8 --tag m3r01
Writes one .pt per eta and appends JSON lines to ../evidence/gauss/<tag>_continuation.jsonl
"""
from __future__ import annotations

import argparse
import json
import time

import torch

from opt_gauss import optimize

torch.set_default_dtype(torch.float64)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--init", required=True)
    ap.add_argument("--etas", required=True)
    ap.add_argument("--iters", type=int, default=8)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--K", type=int, default=None)
    ap.add_argument("--D", type=int, default=None)
    a = ap.parse_args()
    st = torch.load(a.init)
    k, res = st["k"], st["res"]
    K = a.K or st["K"]
    D = a.D or st["D"]
    vs = st["vs"]
    if K + 1 > len(vs[0]):
        vs = [torch.nn.functional.pad(v, (0, K + 1 - len(v))) for v in vs]
    init = (vs, st["theta"])
    log = open(f"../evidence/gauss/{a.tag}_continuation.jsonl", "a")
    for eta in [float(x) for x in a.etas.split(",")]:
        t0 = time.time()
        best = optimize(eta, K, D, k, res, None, a.iters, init=init, verbose=False)
        rec = {"eta": eta, "p": 0.75 * (1 - eta), "ic": best[0], "k": k, "res": res, "K": K, "D": D,
               "q": torch.softmax(best[1][1], 0).tolist(), "secs": round(time.time() - t0, 1)}
        print(json.dumps(rec), flush=True)
        log.write(json.dumps(rec) + "\n")
        log.flush()
        torch.save({"vs": best[1][0], "theta": best[1][1], "eta": eta, "ic": best[0], "k": k, "res": res,
                    "K": K, "D": D}, f"../evidence/gauss/{a.tag}_eta{eta:.7f}.pt")
        init = best[1]
