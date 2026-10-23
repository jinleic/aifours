"""Exact rational reconstruction of the genus-2 solution space from saved per-prime RREFs.
Stability check: reconstruction with the first m primes must agree with all primes."""
import glob
import json
import sys
from fractions import Fraction

import numpy as np

from g2_exact import crt_pair, ratrec


def load():
    data = []
    okeys = None
    for f in sorted(glob.glob("../evidence/rref/rref_*.npz")):
        z = np.load(f, allow_pickle=False)
        p = int(f.split("_")[-1].split(".")[0])
        okeys_f = json.loads(str(z["okeys"]))
        okeys = okeys or okeys_f
        assert okeys_f == okeys
        data.append((p, list(z["piv"]), z["R"], bool(z["cons"][0])))
    return data, okeys


def reconstruct(data, nv):
    piv0 = data[0][1]
    assert all(d[1] == piv0 for d in data), "pivot structure differs"
    free = [c for c in range(nv) if c not in set(piv0)]

    def rec(colfun):
        vals, mod = None, 1
        for (p, piv, R, cons) in data:
            v = [int(z) for z in colfun(R, p)]
            if vals is None:
                vals, mod = v, p
            else:
                vals = [crt_pair(a, mod, z, p)[0] for a, z in zip(vals, v)]
                mod *= p
        return [ratrec(v, mod) for v in vals]

    part = rec(lambda R, p: R[:, nv] % p)
    nulls = {f: rec(lambda R, p, f=f: (-R[:, f]) % p) for f in free}
    return piv0, free, part, nulls


if __name__ == "__main__":
    data, okeys = load()
    nv = len(okeys)
    print("primes:", [d[0] for d in data])
    res = []
    for m in (len(data) - 2, len(data)):
        piv, free, part, nulls = reconstruct(data[:m], nv)
        fails = sum(q is None for q in part) + sum(q is None for v in nulls.values() for q in v)
        res.append((piv, free, part, nulls, fails))
        print(f"m={m}: failures={fails}")
    stable = res[0][2] == res[1][2] and all(res[0][3][f] == res[1][3][f] for f in res[1][1])
    print("stable between", len(data) - 2, "and", len(data), "primes:", stable)
    piv, free, part, nulls, fails = res[1]
    dens = sorted({q.denominator for q in part if q is not None} | {q.denominator for v in nulls.values() for q in v if q})
    print("free columns:", free, "keys:", [okeys[f] for f in free])
    print("denominators:", dens[:20], "max |num| bits:",
          max(abs(q.numerator).bit_length() for q in part + [q for v in nulls.values() for q in v] if q is not None))
    out = {"primes": [d[0] for d in data], "stable": stable, "failures": fails, "keys": okeys,
           "pivots": [int(c) for c in piv], "free": [int(f) for f in free],
           "particular": {int(piv[i]): [part[i].numerator, part[i].denominator] for i in range(len(piv))},
           "null": {int(f): {int(piv[i]): [nulls[f][i].numerator, nulls[f][i].denominator] for i in range(len(piv))}
                    for f in free}}
    json.dump(out, open("../evidence/g2_solution_space.json", "w"))
