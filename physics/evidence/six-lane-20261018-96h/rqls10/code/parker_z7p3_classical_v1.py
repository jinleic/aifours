#!/usr/bin/env python3
"""parker_z7p3_classical_v1: find classical Z_7 + 3 orthogonal Latin squares of order 10 (exact control data).

Both squares X in {A, B} have rows/cols/symbols Z_7 u {I0,I1,I2} (encoded 7,8,9), are invariant under
(i, j, s) -> (i+1, j+1, s+1) on finite parts, and are given by data (Dinf, beta, gamma, delta, corner):
  X(i, i+d) = i + beta[d] (d in Dfin),  X(i, i+d_c) = I_c,  X(I_a, j) = j + gamma[a],  X(i, I_b) = i + delta[b],
  X(I_a, I_b) = corner[a][b].
Orthogonality is checked on the full 10x10 arrays. Standard library only; deterministic enumeration order;
stops at the first MAX_HITS pairs or the 300 s self budget. Output JSON (exclusive create) = argv[1].
"""
import itertools, json, sys, time
T0 = time.monotonic(); BUDGET = 290.0; MAX_HITS = 5
N = 7; INF = [7, 8, 9]

def build(Dinf, beta, gamma, delta, corner):
    X = [[None] * 10 for _ in range(10)]
    for i in range(N):
        for d in range(N):
            j = (i + d) % N
            if d in Dinf:
                X[i][j] = INF[Dinf.index(d)]
            else:
                X[i][j] = (i + beta[d]) % N
    for a in range(3):
        for j in range(N):
            X[INF[a]][j] = (j + gamma[a]) % N
    for b in range(3):
        for i in range(N):
            X[i][INF[b]] = (i + delta[b]) % N
    for a in range(3):
        for b in range(3):
            X[INF[a]][INF[b]] = corner[a][b]
    return X

def latin(X):
    full = list(range(10))
    return all(sorted(r) == full for r in X) and all(sorted(X[i][j] for i in range(10)) == full for j in range(10))

def orth(X, Y):
    return len({(X[i][j], Y[i][j]) for i in range(10) for j in range(10)}) == 100

def betas(Dfin):
    out = []
    for vals in itertools.permutations(range(N), len(Dfin)):
        if len({(v - d) % N for v, d in zip(vals, Dfin)}) == len(Dfin):
            out.append(dict(zip(Dfin, vals)))
    return out

cornerA = [[INF[(a + b) % 3] for b in range(3)] for a in range(3)]
cornerB = [[INF[(a + 2 * b) % 3] for b in range(3)] for a in range(3)]
hits = []
tried = 0
for DA in itertools.combinations(range(N), 3):
    if DA[0] != 0:
        continue                      # translation normalisation of A's inf diagonals: 0 in DA
    rest = [d for d in range(N) if d not in DA]
    for DB in itertools.combinations(rest, 3):
        d0 = [d for d in rest if d not in DB][0]
        DAfin = sorted(set(DB) | {d0}); DBfin = sorted(set(DA) | {d0})
        BA = betas(DAfin); BB = betas(DBfin)
        for bA in BA:
            GA = sorted(set(range(N)) - {(bA[d] - d) % N for d in DAfin})
            DeA = sorted(set(range(N)) - {bA[d] for d in DAfin})
            for bB in BB:
                tried += 1
                if (tried & 1023) == 0 and time.monotonic() - T0 > BUDGET:
                    break
                e0 = (bB[d0] - bA[d0]) % N
                GB = sorted(set(range(N)) - {(bB[d] - d) % N for d in DBfin})
                DeB = sorted(set(range(N)) - {bB[d] for d in DBfin})
                for sg in itertools.permutations(GB):
                    dg = {(sg[k] - GA[k]) % N for k in range(3)}
                    if len(dg) < 3 or e0 in dg:
                        continue
                    for sd in itertools.permutations(DeB):
                        dd = {(sd[k] - DeA[k]) % N for k in range(3)}
                        if len(dd) < 3 or (dd & dg) or e0 in dd:
                            continue
                        A = build(list(DA), bA, GA, DeA, cornerA)
                        B = build(list(DB), bB, list(sg), list(sd), cornerB)
                        ok = latin(A) and latin(B) and orth(A, B)
                        if ok:
                            hits.append({"A": {"Dinf": list(DA), "beta": {str(k): v for k, v in bA.items()}, "gamma": GA, "delta": DeA, "corner": cornerA},
                                         "B": {"Dinf": list(DB), "beta": {str(k): v for k, v in bB.items()}, "gamma": list(sg), "delta": list(sd), "corner": cornerB},
                                         "A_array": A, "B_array": B})
                        if len(hits) >= MAX_HITS:
                            break
                    if len(hits) >= MAX_HITS:
                        break
                if len(hits) >= MAX_HITS:
                    break
            if len(hits) >= MAX_HITS or time.monotonic() - T0 > BUDGET:
                break
        if len(hits) >= MAX_HITS or time.monotonic() - T0 > BUDGET:
            break
    if len(hits) >= MAX_HITS or time.monotonic() - T0 > BUDGET:
        break
out = {"probe": "parker_z7p3_classical_v1", "hits": len(hits), "pairs": hits, "tried_beta_pairs": tried,
       "elapsed_s": round(time.monotonic() - T0, 3), "stop": "MAX_HITS" if len(hits) >= MAX_HITS else ("BUDGET" if time.monotonic() - T0 > BUDGET else "EXHAUSTED")}
with open(sys.argv[1], "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "pairs"}))
sys.exit(0 if hits else 1)
