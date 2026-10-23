"""Odd-coset duality bound tables (Proposition 6 of PROOF.md); exact integer optimization, single implementation.

For each remaining type (rank 2t, weight d) and even-coset data (z, c), m' = (3072 - 5d + 4z + 8c)/16.
Required: L_O/2 = 14 n28 + 10 n20 - 6 n12 - 2 n4 <= M(m'), where n28, n20 are forced by the odd-coset energy
1024 m' = 784 n28 + 400 n20 + 144 n12 + 16 n4 and n28+n20+n12+n4 = 256.
 kappa=0 (rank<=6): M(m') = max sum_{|S|=m'} |J| over J in 8Z^256, sum J^2 = 65536, J/8 mod 2 affine (3 cases).
 rank 8: J = eps*w, w in c0+16Z (c0 in {4,12}), twisted support signs balanced within 14.
Output: minimal a = n4+n12 compatible, per (z,c).  Writes evidence/oside-bounds.json.
"""
import json, os, sys

def M_kappa0(mp):
    best = 0
    for n3 in range(0, mp + 1):  # all-odd case: k=J/8 odd everywhere
        for n5 in range(0, mp + 1 - n3):
            n1 = mp - n3 - n5
            if n1 + 9 * n3 + 25 * n5 + (256 - mp) > 1024: break
            best = max(best, n1 + 3 * n3 + 5 * n5)
    for n2 in range(0, mp + 1):  # all-even case: J in 16Z, k'=J/16 in {1,2} on S
        n1 = mp - n2
        if n1 + 4 * n2 > 256: break
        best = max(best, 2 * (n1 + 2 * n2))
    for so in range(max(0, mp - 128), min(128, mp) + 1):  # balanced case
        se = mp - so
        for e2 in range(0, se + 1):
            for e4 in range(0, se - e2 + 1):
                rem = 1024 - (128 - so) - so - 4 * e2 - 16 * e4
                if rem < 0: break
                up3 = min(so, rem // 8); up5 = min(up3, (rem - 8 * up3) // 16)
                best = max(best, so + 2 * up3 + 2 * up5 + 2 * e2 + 4 * e4)
    return 8 * best

def M_rank8(mp, c0, maxdiff=14):
    vals = [w for w in range(-300, 301) if (w - c0) % 16 == 0]
    pos = sorted([(w * w, w) for w in vals if w > 0])[:3]
    neg = sorted([(w * w, -w) for w in vals if w < 0])[:3]
    offmin = min(w * w for w in vals)
    budget = 65536 - offmin * (256 - mp)
    def pareto(opts, cnt):
        res = {}
        for a in range(cnt + 1):
            for b in range(cnt + 1 - a):
                cc = cnt - a - b
                cost = a * opts[0][0] + b * opts[1][0] + cc * opts[2][0]
                gain = a * opts[0][1] + b * opts[1][1] + cc * opts[2][1]
                if res.get(cost, -1) < gain: res[cost] = gain
        par = []; bg = -1
        for cst, g in sorted(res.items()):
            if g > bg: par.append((cst, g)); bg = g
        return par
    best = -1
    for P in range(mp + 1):
        M = mp - P
        if abs(P - M) > maxdiff: continue
        pp, nn = pareto(pos, P), pareto(neg, M)
        j = len(nn) - 1
        for cst, g in pp:
            while j >= 0 and cst + nn[j][0] > budget: j -= 1
            if j < 0: break
            best = max(best, g + nn[j][1])
    return best

def table(rank, d, zmin, Mfun, zmax=24, cmax=24):
    rows = []
    for z in range(zmin, zmax + 1, 2):
        for c in range(0, cmax + 1):
            num = 3072 - 5 * d + 4 * z + 8 * c
            if num % 16: continue
            mp = num // 16; EO = 1024 * mp; Mv = Mfun(mp); best = None
            for n12 in range(0, 60):
                for n4 in range(0, 60):
                    t = EO - 102400 + 256 * n12 + 384 * n4
                    if t % 384: continue
                    n28 = t // 384; n20 = 256 - n12 - n4 - n28
                    if n28 < 0 or n20 < 0: continue
                    if 14 * n28 + 10 * n20 - 6 * n12 - 2 * n4 <= Mv:
                        if best is None or n12 + n4 < best[0]: best = (n12 + n4, n12, n4)
            rows.append(dict(z=z, c=c, mprime=mp, M=Mv, min_a=None if best is None else best[0],
                             witness_n12_n4=None if best is None else best[1:]))
    return rows

if __name__ == "__main__":
    out = {}
    cache = {}
    def M0(mp):
        if mp not in cache: cache[mp] = M_kappa0(mp)
        return cache[mp]
    for (r, d, zmin) in [(2, 192, 8), (4, 160, 8), (6, 112, 4), (6, 128, 8), (6, 144, 4)]:
        out[f"({r},{d})"] = table(r, d, zmin, M0)
    c8 = {}
    def M8(mp):
        if mp not in c8: c8[mp] = max(M_rank8(mp, 4), M_rank8(mp, 12))
        return c8[mp]
    for (d, zmin) in [(120, 10), (136, 12)]:
        out[f"(8,{d})"] = table(8, d, zmin, M8)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "oside-bounds.json")
    json.dump(dict(note="exploratory necessary-condition table; single implementation; see PROOF.md Prop. 6", tables=out),
              open(path, "w"), indent=0)
    for k, rows in out.items():
        print(k, [(r["z"], r["c"], r["min_a"]) for r in rows[:6]])
