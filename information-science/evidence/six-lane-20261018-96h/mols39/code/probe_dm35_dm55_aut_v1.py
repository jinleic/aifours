#!/usr/bin/env python3
"""probe_dm35_dm55_aut_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; <=280 s).
Positive representation anchors (not new results):
 * DM35: the (35,7;1) difference matrix of Miller-Valkov-Abel, Symmetry 18 (2026) 269, Example 3, transcribed from
   the pinned PDF text (pdftotext -layout) — D1 (7x17), D2 = D1 with rows 1<->2, 3<->4, 5<->6 interchanged, D3 (7x1).
 * DM55: Sage DM_55_7_1 (Handbook III.3.72) re-typed from the pinned Sage source (only re-hashed here).
For each: DM check over Z_n (all 21 row pairs), row bijectivity, and the full untwisted automorphism group
{(mu, pi) : mu unit, pi in S_7} of the column set acting (a) exactly on vectors and (b) modulo constants; group
order, element cycle types and multipliers. Also writes nothing; prints one JSON object.
Args: pdf_text_path pdf_text_sha sage_path sage_sha"""
import sys, json, hashlib, itertools, time
from math import gcd
T0 = time.monotonic()
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
pinned(sys.argv[1], sys.argv[2]); pinned(sys.argv[3], sys.argv[4])
D1 = [[0]*17,
      [4,21,3,20,2,19,1,18,0,17,34,16,33,15,32,14,31],
      [5,23,6,24,7,25,8,26,9,27,10,28,11,29,12,30,13],
      [19,34,15,1,13,33,18,12,27,8,29,6,26,25,5,20,0],
      [3,23,7,21,9,24,4,10,30,14,28,16,31,32,17,2,22],
      [23,7,33,32,13,21,9,28,29,2,0,16,5,24,25,17,12],
      [20,1,10,11,30,22,34,15,14,6,8,27,3,19,18,26,31]]
D3 = [0,22,22,11,11,4,4]
swap = [0,2,1,4,3,6,5]
D2 = [D1[swap[i]] for i in range(7)]
DM35 = [D1[i] + D2[i] + [D3[i]] for i in range(7)]
M55 = [[1,7,14,19,28,33,40,46,50],[2,13,25,38,52,12,20,32,45],[39,6,8,26,24,51,11,34,37],
       [54,48,41,36,27,22,15,9,5],[53,42,30,17,3,43,35,23,10],[16,49,47,29,31,4,44,21,18]]
Mb = [[0]*7]
for R in zip(*M55):
    R = list(R)
    for c in range(6):
        sh = R[-c:] + R[:-c] if c else R[:]
        Mb.append(sh + [0])
DM55 = [[col[i] for col in Mb] for i in range(7)]
def analyse(name, rows, n):
    k = len(rows); cols = [tuple(rows[i][c] % n for i in range(k)) for c in range(n)]
    res = {"name": name, "n": n, "k": k, "ncols": len(cols), "distinct_cols": len(set(cols))}
    res["dm_ok"] = all(len({(rows[i][c] - rows[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
    res["row_bijective"] = [len(set(r)) == n for r in rows]
    S = set(cols)
    def norm(c): return tuple((x - c[0]) % n for x in c)
    Sn = set(norm(c) for c in cols)
    units = [u for u in range(1, n) if gcd(u, n) == 1]
    ex = []; mc = []
    for mu in units:
        for perm in itertools.permutations(range(k)):
            pinv = [0] * k
            for x in range(k): pinv[perm[x]] = x
            imgs = [tuple((mu * c[pinv[x]]) % n for x in range(k)) for c in cols]
            if all(v in S for v in imgs): ex.append((mu, perm))
            if all(norm(v) in Sn for v in imgs): mc.append((mu, perm))
    def ctype(perm):
        seen = [False] * k; t = []
        for i in range(k):
            if not seen[i]:
                L = 0; j = i
                while not seen[j]: seen[j] = True; j = perm[j]; L += 1
                t.append(L)
        return "".join(map(str, sorted(t, reverse=True)))
    res["aut_exact_order"] = len(ex); res["aut_modconst_order"] = len(mc)
    res["aut_exact"] = [[mu, list(p), ctype(p)] for mu, p in ex]
    res["aut_modconst"] = [[mu, list(p), ctype(p)] for mu, p in mc]
    return res
out = {"status": "OK", "results": [analyse("DM35_Sym2026_Ex3", DM35, 35), analyse("Sage_DM_55_7_1", DM55, 55)],
       "dm35_rows": DM35, "dm55_rows": DM55}
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
