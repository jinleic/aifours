"""Exact rational parametrization of the n=24 genus-2 solution space by multi-prime RREF + CRT + rational
reconstruction.  Output: particular solution c and nullspace generators for the free orbit columns, as exact
fractions, such that every solution is x = c + sum_f s_f * v_f.  (Exactness of the final objects is then
re-verified independently by multi-prime evaluation of every equation with a bound-based CRT argument.)
"""
import json
import sys
from fractions import Fraction
from math import gcd, isqrt

import numpy as np

from g2_system import build_mod


def rref_mod(Mfull, b, p):
    A = np.concatenate([Mfull % p, (b % p)[:, None]], axis=1).astype(np.int64)
    m, ncol = A.shape
    nv = ncol - 1
    piv = []
    r = 0
    for c in range(nv):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - (col[nzr, None] * A[r][None, :]) % p) % p
        piv.append(c)
        r += 1
        if r == m:
            break
    consistent = not np.any(A[r:, nv] % p)
    return piv, A[:r], consistent


def ratrec(a, m):
    """Rational reconstruction of a mod m (Wang): returns Fraction or None."""
    a %= m
    bound = isqrt(m // 2)
    r0, r1 = m, a
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound or gcd(r1, abs(s1)) != 1:
        return None
    return Fraction(r1, s1)


def crt_pair(a1, m1, a2, m2):
    t = ((a2 - a1) * pow(m1, -1, m2)) % m2
    return a1 + m1 * t, m1 * m2


if __name__ == "__main__":
    primes = [int(p) for p in sys.argv[1:]] or [2147483647, 2147483629, 2147483587, 2147483579]
    data = []
    okeys = None
    for p in primes:
        Mfull, b, okeys_p, orbits = build_mod(p, log=lambda *a: None)
        okeys = okeys or okeys_p
        piv, R, cons = rref_mod(Mfull, b, p)
        data.append((p, piv, R, cons))
        print(json.dumps({"prime": p, "rank": len(piv), "consistent": bool(cons)}), flush=True)
    piv0 = data[0][1]
    assert all(d[1] == piv0 for d in data), "pivot structure differs across primes"
    nv = len(okeys)
    free = [c for c in range(nv) if c not in set(piv0)]
    # particular solution (free=0): x[piv[i]] = R[i, nv]; nullspace vector for free f: x[f]=1, x[piv[i]] = -R[i,f]
    def collect(colfun):
        vals, mod = None, 1
        for (p, piv, R, cons) in data:
            v = colfun(R, p)
            if vals is None:
                vals, mod = [int(z) for z in v], p
            else:
                vals = [crt_pair(a, mod, int(z), p)[0] for a, z in zip(vals, v)]
                mod *= p
        return vals, mod
    out = {"primes": primes, "free_columns": free, "free_keys": [okeys[f] for f in free],
           "pivot_columns": piv0, "keys": okeys}
    vals, mod = collect(lambda R, p: R[:, nv] % p)
    part = [ratrec(v, mod) for v in vals]
    out["particular"] = {str(piv0[i]): (None if q is None else [q.numerator, q.denominator]) for i, q in enumerate(part)}
    nulls = {}
    for f in free:
        vals, mod = collect(lambda R, p, f=f: (-R[:, f]) % p)
        rec = [ratrec(v, mod) for v in vals]
        nulls[str(f)] = {str(piv0[i]): (None if q is None else [q.numerator, q.denominator]) for i, q in enumerate(rec)}
    out["null"] = nulls
    nfail = sum(1 for v in out["particular"].values() if v is None) + sum(
        1 for d in nulls.values() for v in d.values() if v is None)
    out["reconstruction_failures"] = nfail
    print("reconstruction failures:", nfail)
    json.dump(out, open(f"../evidence/g2_exact_{len(primes)}primes.json", "w"))
