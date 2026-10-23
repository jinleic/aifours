#!/usr/bin/env python3
"""rqls10-maximal numeric STRUCTURE probe v1. Float arithmetic, standard library only.

NOT A CERTIFICATE. The output is a reconstruction lead at most. A numeric miss is UNKNOWN; it does not exclude
anything, restricted or unrestricted.

Frozen objectives. All run in one process under one self-budget. Each sub-run has a fixed time slice, in this
order:

W  Weyl-Heisenberg orbit ansatz (representation-v1, R4 open sub-case).
   q0 in C^d; X|t>=|t+1>, Z|t>=w^t|t>, w = exp(2 pi i/d).
   f_W(q0) = sum over M in {X^a, Z^a, X^a Z^(lam a) : a = 1..d-1} of |<q0, M q0>|^2.
   f_W = 0 means q_(row b, col a) = X^a Z^b q0 is a 1-RQLS(d) with B(b,a) = b - lam*a mod d.
   Runs:
   - W5 control: d=5, lam=1. Solutions are known to exist (WH MUB vectors).
   - W10: d=10, lam in (1,3,7,9).

G  General quantum mate of a fixed Latin square B (order n).
   Unit vectors q_p, p in cells. f_G = sum over lines L of (||S_L||_F^2 - n), with S_L = sum_{p in L} q_p q_p^*.
   Lines are rows, columns and B-classes. f_G = 0 iff every line is an orthonormal basis.
   Runs:
   - G8  control: B(i,j) = i XOR j, n=8. Source Example 2.4 and classical mates exist.
   - G6  calibration: B = Cay(Z6). No 1-RQLS(6) exists (Ball-Simoens, as cited by Zhang-Cao).
   - G10 target: B = Cay(Z10), B(i,j) = (i+j) mod 10. No classical mate exists, so any solution would be
     non-classical.

Thresholds (frozen):
- W candidate: f_W < 1e-20.
- G candidate: max over lines of max |G_L - I| entry < 1e-9.
- Parallel-ray test for diagnostics: |<q_p,q_p'>| > 1 - 1e-6.

Self-budget: 290 s wall total (time.monotonic). Disk guard every 5 s: statvfs free >= 12e9 bytes, else stop
with reason DISK_FLOOR. Output: one JSON result file, created exclusively, < 1 MiB.
"""
import cmath
import json
import math
import operator
import os
import random
import sys
import time

FROZEN = {
    "version": "numeric_structure_probe_v1",
    "budget_total_s": 290.0,
    "disk_floor_bytes": 12_000_000_000,
    "disk_check_period_s": 5.0,
    "seed_base": 20261018,
    "W_slices_s": {"W5": 6.0, "W10": 44.0},
    "W_lams_10": [1, 3, 7, 9],
    "W_max_iter_per_start": 3000,
    "W_candidate_f": 1e-20,
    "G_slices_s": {"G8": 40.0, "G6": 20.0, "G10": 170.0},
    "G10_start_slice_s": 56.0,
    "G_candidate_maxdev": 1e-9,
    "parallel_tol": 1e-6,
    "eta0": 0.05,
}

T0 = time.monotonic()
LANE_PROBES = os.path.dirname(os.path.abspath(__file__))
_last_disk = [-1e9]
STOP = {"reason": None}


def free_bytes():
    st = os.statvfs(LANE_PROBES)
    return st.f_bavail * st.f_frsize


def guard():
    """Return False if the run must stop (budget or disk)."""
    now = time.monotonic()
    if now - T0 > FROZEN["budget_total_s"]:
        STOP["reason"] = STOP["reason"] or "BUDGET"
        return False
    if now - _last_disk[0] >= FROZEN["disk_check_period_s"]:
        _last_disk[0] = now
        fb = free_bytes()
        if fb < FROZEN["disk_floor_bytes"]:
            STOP["reason"] = "DISK_FLOOR free=%d" % fb
            return False
    return STOP["reason"] is None


def cdot(x, y):
    """<x,y> = sum conj(x_k) y_k"""
    return sum(map(operator.mul, (z.conjugate() for z in x), y))


def normalize(x):
    s = math.sqrt(sum((z.real * z.real + z.imag * z.imag) for z in x))
    return [z / s for z in x]


def rand_unit(rng, d):
    return normalize([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(d)])


# ---------------- W: Weyl-Heisenberg orbit ansatz ----------------

def wh_ops(d, lam):
    w = [cmath.exp(2j * math.pi * k / d) for k in range(d)]
    ops = []  # (apply, apply_adjoint)
    for a in range(1, d):
        # X^a: (X^a q)(t) = q(t-a); adjoint X^{-a}
        ops.append((lambda q, a=a: [q[(t - a) % d] for t in range(d)],
                    lambda q, a=a: [q[(t + a) % d] for t in range(d)]))
    for b in range(1, d):
        ops.append((lambda q, b=b: [w[(b * t) % d] * q[t] for t in range(d)],
                    lambda q, b=b: [w[(-b * t) % d] * q[t] for t in range(d)]))
    for a in range(1, d):
        la = lam * a
        # M = X^a Z^{la}: (M q)(t) = w^{la (t-a)} q(t-a); M^* q (t) = w^{-la t} q(t+a)
        ops.append((lambda q, a=a, la=la: [w[(la * (t - a)) % d] * q[(t - a) % d] for t in range(d)],
                    lambda q, a=a, la=la: [w[(-la * t) % d] * q[(t + a) % d] for t in range(d)]))
    return ops


def wh_f_grad(q, ops):
    d = len(q)
    f = 0.0
    g = [0j] * d
    for ap, adj in ops:
        mq = ap(q)
        c = cdot(q, mq)
        f += c.real * c.real + c.imag * c.imag
        mtq = adj(q)
        cc = c.conjugate()
        g = [gi + cc * x + c * y for gi, x, y in zip(g, mq, mtq)]
    return f, g


def wh_run(d, lam, rng, deadline):
    ops = wh_ops(d, lam)
    best = None
    starts = 0
    while time.monotonic() < deadline and guard():
        starts += 1
        q = rand_unit(rng, d)
        eta = FROZEN["eta0"]
        f, g = wh_f_grad(q, ops)
        it = 0
        while it < FROZEN["W_max_iter_per_start"] and f > 1e-26:
            if (it & 63) == 0 and (time.monotonic() >= deadline or not guard()):
                break
            pr = cdot(q, g)
            gt = [gi - qi * pr for gi, qi in zip(g, q)]
            qn = normalize([qi - eta * gi for qi, gi in zip(q, gt)])
            fn, gn = wh_f_grad(qn, ops)
            if fn <= f:
                q, f, g = qn, fn, gn
                eta = min(eta * 1.2, 2.0)
            else:
                eta *= 0.5
                if eta < 1e-14:
                    break
            it += 1
        rec = {"start": starts, "f": f, "iters": it}
        if best is None or f < best["f"]:
            best = dict(rec)
            best["q0"] = [[z.real, z.imag] for z in q]
    return best, starts


def wh_config_vectors(q0, d, lam):
    """cell (row b, col a) -> X^a Z^b q0; B(b,a) = (b - lam a) mod d."""
    w = [cmath.exp(2j * math.pi * k / d) for k in range(d)]
    vecs = {}
    for b in range(d):
        zq = [w[(b * t) % d] * q0[t] for t in range(d)]
        for a in range(d):
            vecs[(b, a)] = [zq[(t - a) % d] for t in range(d)]
    Bsq = [[(b - lam * a) % d for a in range(d)] for b in range(d)]
    return vecs, Bsq


# ---------------- G: general quantum mate of fixed B ----------------

def lines_of(B):
    n = len(B)
    L = []
    for i in range(n):
        L.append([(i, j) for j in range(n)])
    for j in range(n):
        L.append([(i, j) for i in range(n)])
    for s in range(n):
        L.append([(i, j) for i in range(n) for j in range(n) if B[i][j] == s])
    for l in L:
        assert len(l) == n
    return L


def g_f_grad(Q, L, n):
    f = 0.0
    grad = {p: [0j] * n for p in Q}
    for line in L:
        S = [[0j] * n for _ in range(n)]
        for p in line:
            qv = Q[p]
            cv = [z.conjugate() for z in qv]
            for a in range(n):
                x = qv[a]
                S[a] = [r + x * c for r, c in zip(S[a], cv)]
        f += sum((z.real * z.real + z.imag * z.imag) for row in S for z in row) - n
        for p in line:
            qv = Q[p]
            gp = grad[p]
            grad[p] = [gi + sum(map(operator.mul, row, qv)) for gi, row in zip(gp, S)]
    return f, grad


def g_maxdev(Q, L):
    m = 0.0
    for line in L:
        for x in range(len(line)):
            for y in range(x, len(line)):
                c = cdot(Q[line[x]], Q[line[y]])
                if x == y:
                    c -= 1.0
                m = max(m, abs(c))
    return m


def ray_stats(Q, tol):
    cells = sorted(Q)
    parent = {p: p for p in cells}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    maxov = 0.0
    for x in range(len(cells)):
        for y in range(x + 1, len(cells)):
            ov = abs(cdot(Q[cells[x]], Q[cells[y]]))
            if ov > maxov:
                maxov = ov
            if ov > 1 - tol:
                parent[find(cells[x])] = find(cells[y])
    roots = {find(p) for p in cells}
    return {"distinct_rays": len(roots), "max_offcell_overlap": maxov}


def g_run(B, rng, deadline, label):
    n = len(B)
    L = lines_of(B)
    Q = {(i, j): rand_unit(rng, n) for i in range(n) for j in range(n)}
    eta = FROZEN["eta0"]
    f, grad = g_f_grad(Q, L, n)
    hist = [(0, f)]
    it = 0
    while f > 1e-26:
        if (it & 15) == 0 and (time.monotonic() >= deadline or not guard()):
            break
        newQ = {}
        for p, qv in Q.items():
            gp = grad[p]
            pr = cdot(qv, gp)
            newQ[p] = normalize([qi - eta * (gi - qi * pr) for qi, gi in zip(qv, gp)])
        fn, gn = g_f_grad(newQ, L, n)
        if fn <= f:
            Q, f, grad = newQ, fn, gn
            eta = min(eta * 1.1, 1.0)
        else:
            eta *= 0.5
            if eta < 1e-14:
                break
        it += 1
        if it in (10, 30, 100, 300, 1000, 3000, 10000) or (it % 2000 == 0):
            hist.append((it, f))
    hist.append((it, f))
    md = g_maxdev(Q, L)
    out = {"label": label, "n": n, "iters": it, "f": f, "maxdev": md, "eta_final": eta, "hist": hist,
           "candidate": md < FROZEN["G_candidate_maxdev"]}
    out.update(ray_stats(Q, FROZEN["parallel_tol"]))
    if out["candidate"]:
        out["vectors"] = {"%d,%d" % p: [[z.real, z.imag] for z in Q[p]] for p in sorted(Q)}
    return out


def main(out_path):
    if os.path.exists(out_path):
        print("REFUSE: output exists", out_path)
        return 2
    res = {"frozen": FROZEN, "python": sys.version, "argv": sys.argv, "runs": [], "frontier": []}
    fb0 = free_bytes()
    res["free_bytes_start"] = fb0
    if fb0 < FROZEN["disk_floor_bytes"]:
        res["stop_reason"] = "NOT_STARTED_DISK free=%d" % fb0
    else:
        # W5 control
        t = time.monotonic()
        rng = random.Random(FROZEN["seed_base"] + 1)
        best, starts = wh_run(5, 1, rng, t + FROZEN["W_slices_s"]["W5"])
        res["runs"].append({"label": "W5_lam1_control", "starts": starts, "best_f": best["f"] if best else None,
                            "candidate": bool(best and best["f"] < FROZEN["W_candidate_f"]),
                            "elapsed_s": time.monotonic() - t})
        # W10
        per = FROZEN["W_slices_s"]["W10"] / len(FROZEN["W_lams_10"])
        for k, lam in enumerate(FROZEN["W_lams_10"]):
            if not guard():
                res["frontier"].append("W10_lam%d not run" % lam)
                continue
            t = time.monotonic()
            rng = random.Random(FROZEN["seed_base"] + 10 + k)
            best, starts = wh_run(10, lam, rng, t + per)
            rec = {"label": "W10_lam%d" % lam, "starts": starts, "best_f": best["f"] if best else None,
                   "best_iters": best["iters"] if best else None, "elapsed_s": time.monotonic() - t}
            rec["candidate"] = bool(best and best["f"] < FROZEN["W_candidate_f"])
            if best and rec["candidate"]:
                q0 = [complex(a, b) for a, b in best["q0"]]
                vecs, Bsq = wh_config_vectors(q0, 10, lam)
                Lw = lines_of(Bsq)
                rec["config_maxdev"] = g_maxdev(vecs, Lw)
                rec.update(ray_stats(vecs, FROZEN["parallel_tol"]))
                rec["q0"] = best["q0"]
            res["runs"].append(rec)
        # G runs
        Bxor = [[i ^ j for j in range(8)] for i in range(8)]
        Bz6 = [[(i + j) % 6 for j in range(6)] for i in range(6)]
        Bz10 = [[(i + j) % 10 for j in range(10)] for i in range(10)]
        for label, B, slice_s, seed in (("G8_xor_control", Bxor, FROZEN["G_slices_s"]["G8"], 101),
                                        ("G6_cayZ6_calibration", Bz6, FROZEN["G_slices_s"]["G6"], 102)):
            if not guard():
                res["frontier"].append(label + " not run")
                continue
            t = time.monotonic()
            rng = random.Random(FROZEN["seed_base"] + seed)
            r = g_run(B, rng, t + slice_s, label)
            r["elapsed_s"] = time.monotonic() - t
            res["runs"].append(r)
        t10 = time.monotonic()
        k = 0
        while guard() and time.monotonic() - t10 < FROZEN["G_slices_s"]["G10"] - 5.0:
            k += 1
            t = time.monotonic()
            dl = min(t + FROZEN["G10_start_slice_s"], t10 + FROZEN["G_slices_s"]["G10"])
            rng = random.Random(FROZEN["seed_base"] + 1000 + k)
            r = g_run(Bz10, rng, dl, "G10_cayZ10_start%d" % k)
            r["elapsed_s"] = time.monotonic() - t
            res["runs"].append(r)
        res["stop_reason"] = STOP["reason"] or "COMPLETED_ALL_SLICES"
    res["elapsed_total_s"] = time.monotonic() - T0
    res["free_bytes_end"] = free_bytes()
    with open(out_path, "x") as fh:
        json.dump(res, fh, indent=1)
    print("WROTE", out_path, "stop_reason", res["stop_reason"], "elapsed", round(res["elapsed_total_s"], 1))
    for r in res["runs"]:
        print(r.get("label"), {k: r.get(k) for k in ("best_f", "f", "maxdev", "candidate", "starts", "iters",
                                                      "distinct_rays", "max_offcell_overlap", "elapsed_s")})
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
