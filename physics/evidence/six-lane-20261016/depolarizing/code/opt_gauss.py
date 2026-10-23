"""Optimize modular rank-r single-mode codes for the emergent Gaussian channel (float64 exploration).

Usage: python opt_gauss.py --eta 0.73 --k 3 --res 0,1 --K 220 --D 320 --mu 56 --iters 200 --out file.pt
"""
from __future__ import annotations

import argparse
import json
import math
import time

import torch

from gauss import GaussChannel, coherent_info_modular

torch.set_default_dtype(torch.float64)


def init_vecs(K, k, residues, mu, width_scale=1.0, complex_=False, seed=0):
    g = torch.Generator().manual_seed(seed)
    vs = []
    n = torch.arange(K + 1, dtype=torch.float64)
    # sqrt-Poisson envelope (multi-component cat comb), optionally widened
    lp = n * math.log(mu) - mu - torch.lgamma(n + 1)
    lp = lp / width_scale ** 2 + (1 - 1 / width_scale ** 2) * (-(n - mu) ** 2 / (2 * mu))  # crude widening
    env = torch.exp(0.5 * (lp - lp.max()))
    for r in residues:
        v = torch.where((n.long() % k) == r, env, torch.zeros_like(env))
        v = v + 1e-6 * torch.randn(K + 1, generator=g) * ((n.long() % k) == r)
        if complex_:
            v = v.to(torch.complex128)
        vs.append(v)
    return vs


def build(params, K, k, residues):
    vs, theta = params
    n = torch.arange(K + 1)
    psis = []
    for v, r in zip(vs, residues):
        mask = ((n % k) == r).to(v.dtype)
        w = v * mask
        psis.append(w / torch.linalg.vector_norm(w))
    qs = torch.softmax(theta, dim=0)
    return psis, qs


def optimize(eta, K, D, k, residues, mu, iters, init=None, width_scale=1.0, complex_=False, verbose=True, seed=0,
             scale=1e6):
    ch = GaussChannel(eta, K, D)
    if init is None:
        vs = [v.clone().requires_grad_(True) for v in init_vecs(K, k, residues, mu, width_scale, complex_, seed)]
        theta = torch.zeros(len(residues), requires_grad=True)
    else:
        vs = [v.clone().detach().requires_grad_(True) for v in init[0]]
        theta = init[1].clone().detach().requires_grad_(True)
    params = vs + [theta]
    opt = torch.optim.LBFGS(params, lr=1, max_iter=20, history_size=50, line_search_fn="strong_wolfe",
                            tolerance_grad=1e-30, tolerance_change=1e-30)
    best = [-1e9, None]

    def closure():
        opt.zero_grad()
        psis, qs = build((vs, theta), K, k, residues)
        ic, _, _, _ = coherent_info_modular(ch, psis, list(qs), residues, k)
        loss = -ic * scale
        loss.backward()
        if ic.item() > best[0]:
            best[0] = ic.item()
            best[1] = ([v.detach().clone() for v in vs], theta.detach().clone())
        return loss

    t0 = time.time()
    for it in range(iters):
        opt.step(closure)
        if verbose and (it % 5 == 0 or it == iters - 1):
            print(f"eta={eta:.7f} it={it} best_ic={best[0]:.6e} t={time.time()-t0:.1f}s", flush=True)
    return best


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--eta", type=float, required=True)
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--res", type=str, default="0,1")
    ap.add_argument("--K", type=int, default=220)
    ap.add_argument("--D", type=int, default=320)
    ap.add_argument("--mu", type=float, default=56.0)
    ap.add_argument("--iters", type=int, default=30)
    ap.add_argument("--width", type=float, default=1.0)
    ap.add_argument("--complex", action="store_true")
    ap.add_argument("--init", type=str, default=None)
    ap.add_argument("--out", type=str, default=None)
    a = ap.parse_args()
    residues = [int(x) for x in a.res.split(",")]
    init = torch.load(a.init) if a.init else None
    if init is not None:
        init = (init["vs"], init["theta"])
    best = optimize(a.eta, a.K, a.D, a.k, residues, a.mu, a.iters, init, a.width, a.complex)
    p = 0.75 * (1 - a.eta)
    print(json.dumps({"eta": a.eta, "p": p, "best_ic": best[0], "k": a.k, "res": residues, "K": a.K, "D": a.D}))
    if a.out:
        torch.save({"vs": best[1][0], "theta": best[1][1], "eta": a.eta, "ic": best[0], "k": a.k,
                    "res": residues, "K": a.K, "D": a.D}, a.out)
