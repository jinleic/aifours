"""EXPLORATION ONLY (float64, not a certificate): search for non-classical pairs (Psi1, Psi2) completing two classical
AG(2,7) squares L3(i,j) = j + s3 i, L4(i,j) = j + s4 i to a set of 4 MOQLS(7) (standard form, row 0 = |j>).

Allowed coordinates at (i,j), i != 0: F_7 \\ {j, j + s3 i, j + s4 i} (rules #2/#3 w.r.t. row 0 and the classical squares).
Residual = sum over lines of the 4-net (rows, cols, L3-lines, L4-lines) of ||Gram_s - I||^2 for s = 1, 2
         + ||(G1 o G2) - I||^2 over all 49 cells (tensor-product orthonormality).
Random restarts (seeded); converged solutions are classified by numerical ray counts (|<u,v>| > 1 - 1e-6).

python -B explore_two_quantum.py --s4 2 --restarts 20 --seed 0 --out ../evidence/explore_s4_2.json
"""
from __future__ import annotations

import argparse
import json
import time

import torch

torch.set_default_dtype(torch.float64)
P = 7


def build(s3, s4):
    mask = torch.zeros(P, P, P)        # mask[i, j, k] = 1 if coord k allowed at cell (i, j)
    for i in range(1, P):
        for j in range(P):
            for k in range(P):
                if k not in (j, (j + s3 * i) % P, (j + s4 * i) % P):
                    mask[i, j, k] = 1
    lines = []
    for i in range(P):
        lines.append([(i, j) for j in range(P)])
    for j in range(P):
        lines.append([(i, j) for i in range(P)])
    for s in (s3, s4):
        for b in range(P):
            lines.append([(i, (b + s * i) % P) for i in range(P)])
    return mask, lines


def vectors(params, mask):
    re, im = params
    v = torch.complex(re * mask, im * mask)
    v = v / torch.linalg.vector_norm(v, dim=-1, keepdim=True).clamp_min(1e-300)
    row0 = torch.zeros(P, P, dtype=v.dtype)
    row0[torch.arange(P), torch.arange(P)] = 1
    v = torch.cat([row0.unsqueeze(0), v[1:]], 0)
    return v                                 # (P, P, P): cell (i,j) -> vector


def residual(V1, V2, lines):
    r = 0.0
    eye = torch.eye(P, dtype=V1.dtype)
    for V in (V1, V2):
        for L in lines:
            idx_i = torch.tensor([c[0] for c in L])
            idx_j = torch.tensor([c[1] for c in L])
            M = V[idx_i, idx_j]                 # (7, 7)
            G = M.conj() @ M.T
            r = r + (G - eye).abs().pow(2).sum()
    A = V1.reshape(P * P, P)
    B = V2.reshape(P * P, P)
    G1 = A.conj() @ A.T
    G2 = B.conj() @ B.T
    r = r + (G1 * G2 - torch.eye(P * P, dtype=G1.dtype)).abs().pow(2).sum()
    return r


def rays(V, tol=1e-6):
    A = V.reshape(P * P, P)
    G = (A.conj() @ A.T).abs()
    reps = []
    for c in range(P * P):
        if not any(G[c, r] > 1 - tol for r in reps):
            reps.append(c)
    return len(reps)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--s3", type=int, default=1)
    ap.add_argument("--s4", type=int, required=True)
    ap.add_argument("--restarts", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--iters", type=int, default=60)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    mask, lines = build(a.s3, a.s4)
    g = torch.Generator().manual_seed(a.seed)
    out = {"s3": a.s3, "s4": a.s4, "seed": a.seed, "runs": []}
    for rr in range(a.restarts):
        t0 = time.time()
        params = [torch.randn(P, P, P, generator=g).requires_grad_(True) for _ in range(4)]
        opt = torch.optim.LBFGS(params, lr=1, max_iter=50, history_size=50, line_search_fn="strong_wolfe",
                                tolerance_grad=1e-14, tolerance_change=1e-16)

        def closure():
            opt.zero_grad()
            V1 = vectors(params[0:2], mask)
            V2 = vectors(params[2:4], mask)
            loss = residual(V1, V2, lines)
            loss.backward()
            return loss
        last = None
        for _ in range(a.iters):
            last = opt.step(closure).item()
            if last < 1e-24:
                break
        with torch.no_grad():
            V1 = vectors(params[0:2], mask)
            V2 = vectors(params[2:4], mask)
            res = residual(V1, V2, lines).item()
            rec = {"restart": rr, "residual": res, "rays1": rays(V1), "rays2": rays(V2),
                   "max_weight1": int(((V1[1:].abs() > 1e-6).sum(-1)).max()),
                   "max_weight2": int(((V2[1:].abs() > 1e-6).sum(-1)).max()), "secs": round(time.time() - t0, 1)}
        out["runs"].append(rec)
        print(json.dumps(rec), flush=True)
    sol = [r for r in out["runs"] if r["residual"] < 1e-16]
    out["solutions"] = len(sol)
    out["nonclassical_solutions"] = sum(1 for r in sol if r["rays1"] > 7 or r["rays2"] > 7)
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("s3", "s4", "solutions", "nonclassical_solutions")}))


if __name__ == "__main__":
    main()
