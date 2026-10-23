#!/usr/bin/env python3
"""z9p1_classical_search_v1: exhaustive search for orthogonal Latin squares of order 10 that are both Z_9 + 1
invariant (automorphism i -> i+1 on Z_9 rows/columns/symbols fixing one point), up to translation normalisations.

Data per square X: inf diagonal d_X; beta_X on the other 8 diagonals (injective, beta_X - id injective);
gamma_X = Z_9 minus (beta_X - id)(Dfin), delta_X = Z_9 minus beta_X(Dfin). X(i, i+d) = i + beta_X[d], X(i, i+d_X) = inf,
X(inf, j) = j + gamma_X, X(i, inf) = i + delta_X, X(inf, inf) = inf.
Orthogonality of (A, B) with d_A = 0 (column translation), d_B = e != 0: the 7 differences beta_B[d] - beta_A[d]
(d not in {0, e}) together with gamma_B - gamma_A and delta_B - delta_A are the 9 distinct residues (the remaining
pair orbits are matched automatically). Normalisations: symbol translations of A and of B shift all differences
uniformly, so beta_A[e] = 0 and the first common diagonal of B is fixed to 0 w.l.o.g. Each hit is re-checked on the
full 10x10 arrays. Standard library; self budget 280 s; output JSON (exclusive) argv[1].
"""
import json, sys, time
T0 = time.monotonic(); BUDGET = 280.0
N = 9
hits, nodes, stop = [], 0, "EXHAUSTED"


def build(d_inf, beta, gamma, delta):
    X = [[None] * 10 for _ in range(10)]
    for i in range(N):
        for d in range(N):
            X[i][(i + d) % N] = 9 if d == d_inf else (i + beta[d]) % N
    for j in range(N):
        X[9][j] = (j + gamma) % N
    for i in range(N):
        X[i][9] = (i + delta) % N
    X[9][9] = 9
    return X


def latin(X):
    f = list(range(10))
    return all(sorted(r) == f for r in X) and all(sorted(X[i][j] for i in range(10)) == f for j in range(10))


def betas(dfin, fixed=None):
    """all beta on dfin with beta and beta - id injective; optional fixed (d, value)."""
    out = []
    order = list(dfin)
    vals = [None] * len(order)
    usedv, usedw = set(), set()

    def rec(k):
        if k == len(order):
            out.append(dict(zip(order, vals)))
            return
        d = order[k]
        cand = [fixed[1]] if (fixed and fixed[0] == d) else range(N)
        for x in cand:
            w = (x - d) % N
            if x in usedv or w in usedw:
                continue
            usedv.add(x); usedw.add(w); vals[k] = x
            rec(k + 1)
            usedv.discard(x); usedw.discard(w)
    rec(0)
    return out


for e in range(1, N):
    if time.monotonic() - T0 > BUDGET:
        stop = "BUDGET"
        break
    dA = [d for d in range(N) if d != 0]
    dB = [d for d in range(N) if d != e]
    common = [d for d in range(N) if d not in (0, e)]
    BA = betas(dA, fixed=(e, 0))
    BB = betas(dB, fixed=(common[0], 0))
    for ba in BA:
        if time.monotonic() - T0 > BUDGET:
            stop = "BUDGET"
            break
        gA = (set(range(N)) - {(ba[d] - d) % N for d in dA}).pop()
        dlA = (set(range(N)) - set(ba.values())).pop()
        for bb in BB:
            nodes += 1
            diffs = {(bb[d] - ba[d]) % N for d in common}
            if len(diffs) < 7:
                continue
            gB = (set(range(N)) - {(bb[d] - d) % N for d in dB}).pop()
            dlB = (set(range(N)) - set(bb.values())).pop()
            diffs |= {(gB - gA) % N, (dlB - dlA) % N}
            if len(diffs) == 9:
                A = build(0, ba, gA, dlA)
                B = build(e, bb, gB, dlB)
                ok = latin(A) and latin(B) and len({(A[i][j], B[i][j]) for i in range(10) for j in range(10)}) == 100
                hits.append({"e": e, "betaA": {str(k): v for k, v in ba.items()}, "betaB": {str(k): v for k, v in bb.items()},
                             "gammaA": gA, "deltaA": dlA, "gammaB": gB, "deltaB": dlB, "verified_full": ok})
                if len(hits) >= 20:
                    break
        if len(hits) >= 20:
            stop = "MAX_HITS"
            break
    if stop in ("BUDGET", "MAX_HITS"):
        break
out = {"probe": "z9p1_classical_search_v1", "hits": len(hits), "first_hits": hits[:20], "pairs_examined": nodes, "stop": stop,
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(sys.argv[1], "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("hits", "pairs_examined", "stop", "elapsed_s")}))
