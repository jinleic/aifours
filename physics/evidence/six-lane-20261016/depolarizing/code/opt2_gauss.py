"""Grid-initialized + L-BFGS optimization of mod-k rank-2 Gaussian-limit codes (float64 exploration).

python opt2_gauss.py --eta 0.735 --K 220 --D 320 --iters 40 --tag g2
"""
from __future__ import annotations

import argparse
import json
import math
import time

import torch

from gauss import GaussChannel, coherent_info_modular

torch.set_default_dtype(torch.float64)


def comb(K, k, residues, mu, w):
    n = torch.arange(K + 1, dtype=torch.float64)
    env = torch.exp(-(n - mu) ** 2 / (4 * w * w))
    out = []
    for r in residues:
        v = torch.where((n.long() % k) == r, env, torch.zeros_like(env))
        out.append(v / v.norm())
    return out


NONNEG = False   # set by --nonneg: amplitudes |v| (needed by the positive-recursion certificate)
FIXQ = None      # set by --fixq: fixed weights (theta ignored)


def ic_of(ch, vs, theta, K, k, residues):
    n = torch.arange(K + 1)
    psis = []
    for v, r in zip(vs, residues):
        m = ((n % k) == r).to(v.dtype)
        u = (torch.abs(v) if NONNEG else v) * m
        psis.append(u / torch.linalg.vector_norm(u))
    qs = torch.softmax(theta, 0) if FIXQ is None else torch.tensor(FIXQ)
    ic, _, _, w = coherent_info_modular(ch, psis, list(qs), residues, k)
    return ic


def _theta0(q, r):
    """log-weights: first codeword q, the remaining r-1 share 1-q equally."""
    return torch.log(torch.tensor([q] + [(1 - q) / (r - 1)] * (r - 1)))


def run(eta, K, D, k, residues, iters, mus, ws, qs_grid, init=None, log=None):
    ch = GaussChannel(eta, K, D)
    r = len(residues)
    if init is None:
        best = None
        for mu in mus:
            for w in ws:
                ps = comb(K, k, residues, mu, w)
                for q in qs_grid:
                    th = _theta0(q, r)
                    with torch.no_grad():
                        ic = ic_of(ch, ps, th, K, k, residues).item()
                    if best is None or ic > best[0]:
                        best = (ic, mu, w, q)
        ic0, mu, w, q = best
        vs = [p.clone().requires_grad_(True) for p in comb(K, k, residues, mu, w)]
        theta = _theta0(q, r).requires_grad_(True)
        start = {"mu": mu, "w": w, "q": q, "ic0": ic0}
    else:
        vs = [v.clone().detach().requires_grad_(True) for v in init[0]]
        theta = init[1].clone().detach().requires_grad_(True)
        with torch.no_grad():
            ic0 = ic_of(ch, vs, theta, K, k, residues).item()
        start = {"init": True, "ic0": ic0}
    scale = 1.0 / max(abs(ic0), 1e-13)
    opt = torch.optim.LBFGS(vs + [theta], lr=1, max_iter=25, history_size=100, line_search_fn="strong_wolfe",
                            tolerance_grad=1e-300, tolerance_change=1e-300)
    rec = {"ic": ic0, "state": ([v.detach().clone() for v in vs], theta.detach().clone())}

    def closure():
        opt.zero_grad()
        ic = ic_of(ch, vs, theta, K, k, residues)
        if ic.item() > rec["ic"]:
            rec["ic"] = ic.item()
            rec["state"] = ([v.detach().clone() for v in vs], theta.detach().clone())
        loss = -ic * scale
        loss.backward()
        return loss

    t0 = time.time()
    for it in range(iters):
        try:
            opt.step(closure)
        except Exception as e:  # eigh failures etc.
            print("step failed", e)
            break
        if log:
            print(f"eta={eta} it={it} ic={rec['ic']:.6e} t={time.time()-t0:.0f}s", flush=True)
    return rec, start


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--eta", type=float, required=True)
    ap.add_argument("--K", type=int, default=220)
    ap.add_argument("--D", type=int, default=320)
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--res", default="0,1")
    ap.add_argument("--iters", type=int, default=30)
    ap.add_argument("--mus", default="10,15,20,30,40,56,70,90")
    ap.add_argument("--ws", default="3,5,6,8,10,13,16,20,30")
    ap.add_argument("--qs", default="0.4,0.45,0.5")
    ap.add_argument("--init", default=None)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--nonneg", action="store_true")
    ap.add_argument("--fixq", default=None, help="comma list of fixed weights, e.g. 0.5,0.5")
    a = ap.parse_args()
    NONNEG = a.nonneg
    FIXQ = None if a.fixq is None else [float(x) for x in a.fixq.split(",")]
    res = [int(x) for x in a.res.split(",")]
    init = None
    if a.init:
        st = torch.load(a.init)
        vs = st["vs"]
        if a.K + 1 > len(vs[0]):
            vs = [torch.nn.functional.pad(v, (0, a.K + 1 - len(v))) for v in vs]
        else:
            vs = [v[: a.K + 1] for v in vs]
        if NONNEG:
            vs = [torch.clamp(v, min=0.0) for v in vs]
        init = (vs, st["theta"])
    rec, start = run(a.eta, a.K, a.D, a.k, res, a.iters, [float(x) for x in a.mus.split(",")],
                     [float(x) for x in a.ws.split(",")], [float(x) for x in a.qs.split(",")], init, log=True)
    out = f"../evidence/gauss/{a.tag}_k{a.k}_r{''.join(map(str,res))}_eta{a.eta:.7f}.pt"
    save_vs = [torch.abs(v) for v in rec["state"][0]] if NONNEG else rec["state"][0]
    torch.save({"vs": save_vs, "theta": rec["state"][1], "eta": a.eta, "ic": rec["ic"], "k": a.k,
                "res": res, "K": a.K, "D": a.D, "start": start, "nonneg": NONNEG, "fixq": FIXQ}, out)
    q = torch.softmax(rec["state"][1], 0).tolist() if FIXQ is None else FIXQ
    n = torch.arange(a.K + 1, dtype=torch.float64)
    means = []
    for v, r in zip(rec["state"][0], res):
        u = (torch.abs(v) if NONNEG else v) * ((n.long() % a.k) == r)
        u = u / u.norm()
        means.append(float((n * u * u).sum()))
    print(json.dumps({"eta": a.eta, "p": 0.75 * (1 - a.eta), "ic": rec["ic"], "q": q, "mean_n": means,
                      "start": start, "file": out}))
