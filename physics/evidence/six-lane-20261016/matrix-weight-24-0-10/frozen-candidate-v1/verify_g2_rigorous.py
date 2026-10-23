"""Deterministic exact verification of the genus-2 MacWilliams identities for a candidate table, coefficient by
coefficient, for EVERY pair type tau' (all 20475 types, no S3-representative shortcut, no saved system matrices).

For each prime p we compute, with int64 arithmetic and reduction after every step (all intermediate values
< 2^36, no overflow),
   F(tau') = sum_tau f(tau) K(tau -> tau') mod p,   K(tau->tau') = [z^tau'] prod_c (T_c . z)^{n_c(tau)},
and compare with 2^48 f(tau') (full transform T) and, separately, F1 with 2^24 f(tau') (partial transform T1).
Height bounds (integers): sum_tau f(tau) = 2^48 and |K| <= 16^24 = 2^96 (row abs-sums of T are <= 16), so
|F - 2^48 f| < 2^145; for T1 (row abs-sums <= 4): |F1 - 2^24 f| < 2^97. If the residuals vanish modulo primes
whose product exceeds 2^146 (resp. 2^98), the integer residuals are exactly zero.
Usage: verify_g2_rigorous.py candidate.json PRIME [PRIME ...]   -> one JSON receipt per prime
"""
import json
import sys
import time

import numpy as np

from genus2 import brute_T, transform_row, types

T1 = np.array([[1, 0, 3, 0, 0], [0, 1, 0, 1, 2], [1, 0, -1, 0, 0], [0, 1, 0, 1, -2], [0, 1, 0, -1, 0]],
              dtype=np.int64)
N = 24


def per_type(counts):
    f = {}
    for (a, b, c, d) in types(N):
        key = json.dumps([sorted([a, b, c]), d])
        v = counts.get(key, 0)
        if v:
            f[(a, b, c, d)] = v
    return f


if __name__ == "__main__":
    cand = json.load(open(sys.argv[1]))
    if "entries" in cand:   # full AMH-indexed table [i,j,t,p,lambda] -> type (n0x,nx0,nxx,nxy)=(j-t,i-t,p,t-p)
        f = {}
        for i, j, t, p, v in cand["entries"]:
            if int(v):
                f[(j - t, i - t, p, t - p)] = int(v)
    else:
        f = per_type({k: int(v) for k, v in cand["counts"].items()})
    assert sum(f.values()) == 2 ** 48 and min(f.values()) > 0, "height bound needs total pair count 2^48, f > 0"
    T = brute_T()
    assert np.abs(T).sum(axis=1).max() <= 16 and np.abs(T1).sum(axis=1).max() <= 4
    for p in [int(a) for a in sys.argv[2:]]:
        t0 = time.time()
        acc = np.zeros((N + 1,) * 4, dtype=np.int64)
        acc1 = np.zeros((N + 1,) * 4, dtype=np.int64)
        target = np.zeros((N + 1,) * 4, dtype=np.int64)
        for tau, v in f.items():
            vp = v % p
            acc = (acc + vp * transform_row(tau, N, T, mod=p)) % p
            acc1 = (acc1 + vp * transform_row(tau, N, T1, mod=p)) % p
            target[tau] = vp
        ok_full = ok_part = True
        bad_full = bad_part = 0
        c48, c24 = pow(2, 48, p), pow(2, 24, p)
        for tau in types(N):
            if acc[tau] != (c48 * target[tau]) % p:
                ok_full = False
                bad_full += 1
            if acc1[tau] != (c24 * target[tau]) % p:
                ok_part = False
                bad_part += 1
        rec = {"prime": p, "rows_checked": len(types(N)), "full_transform_all_rows_vanish": ok_full,
               "partial_transform_all_rows_vanish": ok_part, "bad_full": bad_full, "bad_partial": bad_part,
               "seconds": round(time.time() - t0, 1)}
        print(json.dumps(rec), flush=True)
