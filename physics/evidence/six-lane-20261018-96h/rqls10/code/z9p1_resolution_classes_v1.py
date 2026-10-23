#!/usr/bin/env python3
"""z9p1_resolution_classes_v1: exact stdlib count of the Z_9 + 1 resolution squares used by the proposed R9 stage of
code/rqls_assay_v9.py (functions z9_all_betas / z9_canon / z9_config copied verbatim from that file, sha256
e907968609f9e90c1c25891068227f3117a7ec44691338494b5d99cd772164db): betas on D_fin = {1..8} with beta, beta - id
injective (D_inf = {0}); classes under symbol translation, multipliers u in Z_9^* and transposition. Also: each beta
gives a Latin square (re-checked on the full 10 x 10 array), and the classes containing the 40 known classical
resolutions of evidence/z9p1_classical_search_v1.result.json. Standard library; budget 60 s; output JSON (exclusive).
Usage: z9p1_resolution_classes_v1.py Z9_JSON OUT.json
"""
import json, sys, time

T0 = time.monotonic()


def z9_all_betas():
    """every beta on D_fin = {1..8} with beta and beta - id injective (Z_9 + 1 squares with D_inf = {0})."""
    out, vals, usedv, usedw = [], [None] * 8, set(), set()

    def rec(k):
        if k == 8:
            out.append(tuple(vals))
            return
        d = k + 1
        for x in range(9):
            w = (x - d) % 9
            if x in usedv or w in usedw:
                continue
            usedv.add(x)
            usedw.add(w)
            vals[k] = x
            rec(k + 1)
            usedv.discard(x)
            usedw.discard(w)
    rec(0)
    return out


def z9_canon(bt):
    """canonical form of beta (tuple over d = 1..8) under symbol translation beta + c, multipliers
    beta'(u d) = u beta(d) (u in Z_9^*) and transposition beta^T(d) = d + beta(-d)."""
    best = None
    for tr in (False, True):
        b0 = {d: bt[d - 1] for d in range(1, 9)}
        if tr:
            b0 = {d: (d + b0[(-d) % 9]) % 9 for d in range(1, 9)}
        for u in (1, 2, 4, 5, 7, 8):
            bu = {(u * d) % 9: (u * b0[d]) % 9 for d in range(1, 9)}
            for c in range(9):
                key = tuple((bu[d] + c) % 9 for d in range(1, 9))
                if best is None or key < best:
                    best = key
    return best


def z9_config(bt):
    beta = {d: bt[d - 1] for d in range(1, 9)}
    gam = sorted(set(range(9)) - {(beta[d] - d) % 9 for d in range(1, 9)})
    dlt = sorted(set(range(9)) - set(beta.values()))
    return beta, gam, dlt


def square(beta, gam, dlt):
    X = [[None] * 10 for _ in range(10)]
    for i in range(9):
        for d in range(9):
            X[i][(i + d) % 9] = 9 if d == 0 else (i + beta[d]) % 9
    for j in range(9):
        X[9][j] = (j + gam[0]) % 9
    for i in range(9):
        X[i][9] = (i + dlt[0]) % 9
    X[9][9] = 9
    return X


def latin(X):
    f = list(range(10))
    return all(sorted(r) == f for r in X) and all(sorted(X[i][j] for i in range(10)) == f for j in range(10))


allb = z9_all_betas()
bad = 0
for bt in allb:
    beta, gam, dlt = z9_config(bt)
    if len(gam) != 1 or len(dlt) != 1 or not latin(square(beta, gam, dlt)):
        bad += 1
canon = {}
for bt in allb:
    canon.setdefault(z9_canon(bt), []).append(bt)
z9 = json.load(open(sys.argv[1]))
known = set()
for hit in z9["first_hits"]:
    bA = {int(k): int(v) for k, v in hit["betaA"].items()}
    bB = {int(k): int(v) for k, v in hit["betaB"].items()}
    e9 = int(hit["e"])
    known.add(z9_canon(tuple(bA[d] for d in range(1, 9))))
    known.add(z9_canon(tuple(bB[(d + e9) % 9] for d in range(1, 9))))
sizes = sorted(len(v) for v in canon.values())
out = {"probe": "z9p1_resolution_classes_v1", "betas": len(allb), "non_latin_or_bad": bad, "classes": len(canon),
       "class_size_histogram": {str(s): sizes.count(s) for s in sorted(set(sizes))},
       "known_classical_classes": len(known), "known_in_enumeration": len(known & set(canon)),
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(sys.argv[2], "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out))
