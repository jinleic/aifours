"""Exact checks of the genus-2 (pair) MacWilliams identities for a candidate table.

(a) Polynomial identity test, independent of the transform-row code: with
    W(z) = sum_tau f(tau) z00^n00 z0x^n0x zx0^nx0 zxx^nxx zxy^nxy  (exact big integers),
    check W(T z) = 2^48 W(z) (full transform) and W(T1 z) = 2^24 W(z) (partial transform in u) at random integer
    points z (Schwartz-Zippel; degree 24, points drawn from [-10^6, 10^6]^5).
(b) Rigorous modular check of every S3-orbit equation of the full transform using the saved system matrices
    modulo 8 primes (product > 2^247); with |residual| < 2^156 this proves the integer residuals vanish.
"""
import glob
import json
import random
import sys

import numpy as np

from genus2 import brute_T

T1 = [[1, 0, 3, 0, 0], [0, 1, 0, 1, 2], [1, 0, -1, 0, 0], [0, 1, 0, 1, -2], [0, 1, 0, -1, 0]]


def per_type_counts(counts, n=24):
    f = {}
    for a in range(n + 1):
        for b in range(n + 1 - a):
            for cc in range(n + 1 - a - b):
                for d in range(n + 1 - a - b - cc):
                    key = json.dumps([sorted([a, b, cc]), d])
                    if key in counts and counts[key] != 0:
                        f[(a, b, cc, d)] = counts[key]
    return f


def W_eval(f, z, n=24):
    z00, z0x, zx0, zxx, zxy = z
    tot = 0
    for (n0x, nx0, nxx, nxy), v in f.items():
        n00 = n - n0x - nx0 - nxx - nxy
        tot += v * z00 ** n00 * z0x ** n0x * zx0 ** nx0 * zxx ** nxx * zxy ** nxy
    return tot


def matvec(M, z):
    return [sum(int(M[r][c]) * z[c] for c in range(5)) for r in range(5)]


if __name__ == "__main__":
    cand = json.load(open(sys.argv[1]))
    counts = {k: int(v) for k, v in cand["counts"].items()}
    f = per_type_counts(counts)
    T = brute_T().tolist()
    rng = random.Random(20261016)
    res = {"poly_full": [], "poly_partial": []}
    for _ in range(8):
        z = [rng.randint(-10 ** 6, 10 ** 6) for _ in range(5)]
        lhs = W_eval(f, matvec(T, z))
        rhs = 2 ** 48 * W_eval(f, z)
        res["poly_full"].append(lhs == rhs)
        lhs1 = W_eval(f, matvec(T1, z))
        rhs1 = 2 ** 24 * W_eval(f, z)
        res["poly_partial"].append(lhs1 == rhs1)
    print("polynomial identity W(Tz)=2^48 W(z) at 8 random points:", res["poly_full"])
    print("polynomial identity W(T1z)=2^24 W(z) at 8 random points:", res["poly_partial"])
    # (b) modular rigorous check against the saved orbit-row systems
    keys_sorted = json.loads(str(np.load(sorted(glob.glob("../evidence/rref/rref_*.npz"))[0])["okeys"]))
    xv = [counts.get(json.dumps(k), 0) for k in keys_sorted]
    mod_ok = []
    prod = 1
    for fn in sorted(glob.glob("../evidence/rref/system_*.npz")):
        p = int(fn.split("_")[-1].split(".")[0])
        z = np.load(fn)
        M, b = z["M"], z["b"]
        r = (M.astype(object).dot(np.array(xv, dtype=object)) - b.astype(object)) % p
        mod_ok.append(bool(not any(int(v) for v in r)))
        prod *= p
    res["modular_all_rows"] = mod_ok
    res["prime_product_bits"] = prod.bit_length()
    print("orbit-row equations vanish modulo each prime:", mod_ok, " product bits:", prod.bit_length())
    res["ALL_PASS"] = all(res["poly_full"]) and all(res["poly_partial"]) and all(mod_ok) and prod.bit_length() > 157
    print("GENUS-2 IDENTITIES:", "PASS" if res["ALL_PASS"] else "FAIL")
    json.dump(res, open(sys.argv[1].replace(".json", "_g2check.json"), "w"), indent=1)
