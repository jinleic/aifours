"""Exact checker 2 (order 8), independent of exact8_a.py. Verifies the witness recorded by exact8_a.py:
ring Z2 x Z4 (element code e = 4a + b), f, unit u; Psi^(f)_{ij} = 8^{-1/2} sum_x chi(i f(x) + j x)|x>,
chi(a, b) = (-1)^a i^b; Phi^(u)_{ij} = |u i + j>. Exact integer Gram matrices (real and imaginary parts as int64
numpy arrays), orthogonality via the Hadamard product with Phi's Gram pattern, rays via union-find on |G|^2 = 64.
Also re-checks the mutations and the classical AG(2,8) complete set (GF(8) via exp/log tables).

python -B exact8_b.py --witness ../evidence/controls/exact8_a.json --out ../evidence/controls/exact8_b.json
"""
from __future__ import annotations

import argparse
import hashlib
import json

import numpy as np

ELEMS = [(a, b) for a in range(2) for b in range(4)]          # code e = 4a + b  <->  ELEMS[e]
CODE = {x: k for k, x in enumerate(ELEMS)}


def r_add(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 4)


def r_mul(x, y):
    return ((x[0] * y[0]) % 2, (x[1] * y[1]) % 4)


def r_sub(x, y):
    return ((x[0] - y[0]) % 2, (x[1] - y[1]) % 4)


def char_parts(x):
    # (-1)^a * i^b  ->  (re, im)
    sign = 1 - 2 * x[0]
    return {0: (sign, 0), 1: (0, sign), 2: (-sign, 0), 3: (0, -sign)}[x[1]]


CELLS = [(i, j) for i in ELEMS for j in ELEMS]


def analyse(fcodes, ucode):
    f = {ELEMS[k]: ELEMS[v] for k, v in enumerate(fcodes)}
    re = np.zeros((64, 8), dtype=np.int64)
    im = np.zeros((64, 8), dtype=np.int64)
    for r, (i, j) in enumerate(CELLS):
        for k, x in enumerate(ELEMS):
            re[r, k], im[r, k] = char_parts(r_add(r_mul(i, f[x]), r_mul(j, x)))
    g_re = re @ re.T + im @ im.T
    g_im = re @ im.T - im @ re.T
    mod2 = g_re * g_re + g_im * g_im
    eye = np.eye(64, dtype=bool)
    same_line = np.array([[c[0] == d[0] or c[1] == d[1] for d in CELLS] for c in CELLS])
    out = {"qls": bool(np.all(g_re[eye] == 8) and np.all(g_im[eye] == 0) and np.all(mod2[same_line & ~eye] == 0))}
    if ucode is not None:
        u = ELEMS[ucode]
        phi = [r_add(r_mul(u, i), j) for (i, j) in CELLS]
        same_phi = np.array([[phi[a] == phi[b] for b in range(64)] for a in range(64)])
        out["orthogonal"] = bool(not np.any((mod2 != 0) & same_phi & ~eye))
        out["phi_latin"] = all(len({phi[r] for r, c in enumerate(CELLS) if c[0] == i}) == 8 for i in ELEMS) and \
            all(len({phi[r] for r, c in enumerate(CELLS) if c[1] == j}) == 8 for j in ELEMS)
    parent = list(range(64))

    def find(z):
        while parent[z] != z:
            parent[z] = parent[parent[z]]
            z = parent[z]
        return z
    for a in range(64):
        for b in range(a + 1, 64):
            if mod2[a, b] == 64:
                parent[find(a)] = find(b)
    out["rays"] = len({find(z) for z in range(64)})
    return out


# GF(8) via exp/log tables (primitive element t, t^3 = t + 1)
EXP = [1]
for _ in range(6):
    v = EXP[-1] << 1
    EXP.append(v ^ 0b1011 if v & 0b1000 else v)
LOG = {v: k for k, v in enumerate(EXP)}


def gf_mul(a, b):
    return 0 if a == 0 or b == 0 else EXP[(LOG[a] + LOG[b]) % 7]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--witness", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    w = json.load(open(a.witness))
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "witness_sha256": hashlib.sha256(open(a.witness, "rb").read()).hexdigest()}
    f, u = w["pair"]["f"], w["pair"]["u"]
    fe = {ELEMS[k]: ELEMS[v] for k, v in enumerate(f)}
    additive = all(fe[r_add(x, y)] == r_add(fe[x], fe[y]) for x in ELEMS for y in ELEMS)
    perm = sorted(f) == list(range(8))
    minus = sorted(CODE[r_sub(fe[x], r_mul(ELEMS[u], x))] for x in ELEMS) == list(range(8))
    res["pair"] = {"f_permutation": perm, "f_additive": additive, "f_minus_ux_perm": minus, **analyse(f, u)}
    res["mutation_additive_f"] = analyse(w["mutation_additive_f"]["f"], None)
    res["mutation_other_unit"] = analyse(f, w["mutation_other_unit"]["u"])
    sq = np.array([[[j ^ gf_mul(s, i) for j in range(8)] for i in range(8)] for s in range(1, 8)])
    latin = all(len(set(sq[s, i, :])) == 8 and len(set(sq[s, :, i])) == 8 for s in range(7) for i in range(8))
    orth = all(len(set(zip(sq[s].ravel(), sq[t].ravel()))) == 64 for s in range(7) for t in range(s + 1, 7))
    res["classical_7MOLS8"] = {"latin": latin, "mutually_orthogonal": orth}
    res["expected"] = {"pair_noncl": perm and minus and not additive and res["pair"]["qls"]
                       and res["pair"]["orthogonal"] and res["pair"]["phi_latin"] and res["pair"]["rays"] > 8,
                       "additive_classical": res["mutation_additive_f"]["rays"] == 8,
                       "other_unit_breaks": not res["mutation_other_unit"]["orthogonal"],
                       "classical_ok": latin and orth}
    json.dump(res, open(a.out, "x"), indent=1)
    print(json.dumps(res))
    if not all(res["expected"].values()):
        raise SystemExit("EXACT CHECK 2 FAILED")


if __name__ == "__main__":
    main()
