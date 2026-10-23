"""Exact checker 1 (order 8) for the controls of README §0.

(a) Classical complete set: the 7 AG(2,8) squares L_s(i,j) = j XOR s*i over GF(8) (x^3 = x + 1): Latin, mutually
    orthogonal, 8 rays each (classical).
(b) Non-classical MOQLS(8) pair from Ball–Simoens Theorem 6 / Lemma 14. Over GF(8) (and any ring whose additive group
    is Z2^3) no instance exists: an exhaustive search (recorded below) finds no permutation f, not GF(2)-affine, with
    f(x) + m x a permutation for some m != 0 (all orthomorphisms of Z2^3 are affine). Z8 has no orthomorphisms. We
    therefore use the Frobenius ring R = Z2 x Z4 (product ring; generating character chi(a,b) = (-1)^a i^b), unit
    u = (1,1): f a permutation, f - u x a permutation, f not additive + constant. Then Psi^(f)_{ij} =
    8^{-1/2} sum_x chi(i f(x) + j x) |x> and Phi^(u)_{ij} = |u i + j> are orthogonal QLS (checked here exactly with
    Gaussian integers), and Psi^(f) has > 8 rays.
Element encoding of Z2 x Z4: e = 4a + b (a in Z2, b in Z4).
Mutations: an additive f (must give exactly 8 rays); the other unit u' = (1,3) where f - u' x is not a permutation
(orthogonality must fail).
python -B exact8_a.py --out ../evidence/controls/exact8_a.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json

Q = 8


def gmul(a, b):
    r = 0
    for k in range(3):
        if (b >> k) & 1:
            r ^= a << k
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1011 << (d - 3)
    return r


def is_perm(vals):
    return sorted(vals) == list(range(Q))


# ---------------- Z2 x Z4
def dec(e):
    return e >> 2, e & 3


def enc(a, b):
    return ((a % 2) << 2) | (b % 4)


def add(x, y):
    (a, b), (c, d) = dec(x), dec(y)
    return enc(a + c, b + d)


def neg(x):
    a, b = dec(x)
    return enc(-a, -b)


def rmul(x, y):
    (a, b), (c, d) = dec(x), dec(y)
    return enc(a * c, b * d)


def chi(x):
    """Gaussian integer (re, im) of (-1)^a i^b."""
    a, b = dec(x)
    re, im = [(1, 0), (0, 1), (-1, 0), (0, -1)][b]
    s = -1 if a else 1
    return s * re, s * im


def additive(f):
    return all(f[add(x, y)] == add(f[x], f[y]) for x in range(Q) for y in range(Q))


def gauss_ip(u, v):
    """<u, v> = sum conj(u_k) v_k for Gaussian-integer vectors."""
    re = sum(a * c + b * d for (a, b), (c, d) in zip(u, v))
    im = sum(a * d - b * c for (a, b), (c, d) in zip(u, v))
    return re, im


def psi(f):
    return {(i, j): [chi(add(rmul(i, f[x]), rmul(j, x))) for x in range(Q)] for i in range(Q) for j in range(Q)}


def check(f, u):
    P = psi(f)
    cells = list(P)
    zero = (0, 0)
    rows = all(gauss_ip(P[(i, j)], P[(i, k)]) == zero for i in range(Q) for j, k in itertools.combinations(range(Q), 2))
    cols = all(gauss_ip(P[(i, j)], P[(k, j)]) == zero for j in range(Q) for i, k in itertools.combinations(range(Q), 2))
    norms = all(gauss_ip(P[c], P[c]) == (Q, 0) for c in cells)
    out = {"qls": rows and cols and norms}
    if u is not None:
        phi = {(i, j): add(rmul(u, i), j) for i in range(Q) for j in range(Q)}
        out["phi_latin"] = all(is_perm([phi[(i, j)] for j in range(Q)]) for i in range(Q)) and \
            all(is_perm([phi[(i, j)] for i in range(Q)]) for j in range(Q))
        out["orthogonal"] = all(gauss_ip(P[c], P[d]) == zero or phi[c] != phi[d]
                                for c, d in itertools.combinations(cells, 2))
    reps = []
    for c in cells:
        if not any(sum(t * t for t in gauss_ip(P[c], P[r])) == Q * Q for r in reps):
            reps.append(c)
    out["rays"] = len(reps)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    sq = {s: [[j ^ gmul(s, i) for j in range(Q)] for i in range(Q)] for s in range(1, Q)}
    latin = all(is_perm(row) for s in sq for row in sq[s]) and \
        all(is_perm([sq[s][i][j] for i in range(Q)]) for s in sq for j in range(Q))
    orth = all(len({(sq[s][i][j], sq[t][i][j]) for i in range(Q) for j in range(Q)}) == Q * Q
               for s, t in itertools.combinations(sq, 2))
    res["classical_7MOLS8"] = {"latin": latin, "mutually_orthogonal": orth,
                               "rays_per_square": [len({sq[s][i][j] for i in range(Q) for j in range(Q)}) for s in sq]}
    # GF(8): exhaustive search for a non-GF(2)-affine permutation with a second undetermined direction
    gf_hits = 0
    for perm in itertools.permutations(range(1, Q)):
        f = [0] + list(perm)
        c = f[0]
        if all(f[x ^ y] == f[x] ^ f[y] for x in range(Q) for y in range(Q)):
            continue
        if any(is_perm([f[x] ^ gmul(m, x) for x in range(Q)]) for m in range(1, Q)):
            gf_hits += 1
    res["gf8_nonaffine_with_second_direction"] = gf_hits
    # Z2 x Z4: first non-additive permutation f, f(0)=0, with f - u x a permutation for u = (1,1)
    u = enc(1, 1)
    found = None
    for perm in itertools.permutations(range(1, Q)):
        f = [0] + list(perm)
        if additive(f):
            continue
        if is_perm([add(f[x], neg(rmul(u, x))) for x in range(Q)]):
            found = f
            break
    f = found
    u2 = enc(1, 3)
    res["pair"] = {"ring": "Z2xZ4", "encoding": "e = 4a + b", "f": f, "u": u, "f_additive": additive(f),
                   "f_minus_ux_perm": is_perm([add(f[x], neg(rmul(u, x))) for x in range(Q)]), **check(f, u)}
    addf = [rmul(enc(1, 3), x) for x in range(Q)]          # additive (multiplication by a unit)
    res["mutation_additive_f"] = {"f": addf, "f_additive": additive(addf), **check(addf, None)}
    res["mutation_other_unit"] = {"u": u2, "f_minus_u2x_perm": is_perm([add(f[x], neg(rmul(u2, x))) for x in range(Q)]),
                                  **check(f, u2)}
    res["expected"] = {"classical_ok": latin and orth and res["classical_7MOLS8"]["rays_per_square"] == [8] * 7,
                       "pair_noncl": res["pair"]["qls"] and res["pair"]["phi_latin"] and res["pair"]["orthogonal"]
                       and res["pair"]["rays"] > 8 and not res["pair"]["f_additive"],
                       "additive_classical": res["mutation_additive_f"]["rays"] == 8,
                       "other_unit_breaks": (not res["mutation_other_unit"]["f_minus_u2x_perm"])
                       and not res["mutation_other_unit"]["orthogonal"]}
    json.dump(res, open(a.out, "x"), indent=1)
    print(json.dumps(res))
    if not all(res["expected"].values()):
        raise SystemExit("EXACT CHECK 1 FAILED")


if __name__ == "__main__":
    main()
