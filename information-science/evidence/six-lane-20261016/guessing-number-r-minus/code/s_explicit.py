"""Make the compensation term S of the diamond (3,10;4,8) certificate explicit and evaluate Ing + 3S.

Certificate (evidence/certs/diamond_3_10_4_8.json; exact Fractions):
    h(V) = sum_v u_v h(v) - sum_k y_k g_k(h) - (1/3) Ing(h) - sum_e z_e f_e(h)
for every set function h, where the g_k are elemental Shannon rows (>= 0 on polymatroids), Ing is the
diamond row I(U;V|ZP)+I(U;V|ZQ)+I(P;Q|Z)-I(U;V|Z), and the f_e are FD rows (= 0 on codes).  On codes,
    (2/3) sum_v h(v) - h(V) = S(h) + Ing(h)/3,  S = sum_k y_k g_k  (u_v = 2/3).
Hence gn > 20/3 needs codes with Ing + 3S < 0 (together with an alphabet-balancing construction).

This script:
 1. verifies the identity coefficient-wise in Fractions and lists S as named conditional informations;
 2. evaluates every S term, Ing and the identity on two exact codes:
    - the BCDRV cover code (positive control: S = Ing = 0), with entropies from GF(2) ranks;
    - the 625-word fan code from verify_fan_code.py, with entropies from exact counts as floats.
"""
import sys, os, json, math, itertools
from fractions import Fraction as F
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
W = ["00000", "00110", "10010", "11110", "10001"]          # same data as verify_fan_code.py
FANS = [(1, 2, 3, 4, 5), (1, 2, 7, 6, 5), (8, 10, 4, 3, 9), (8, 10, 7, 6, 9)]
def build(words):
    code = set()
    for choice in itertools.product(range(len(words)), repeat=4):
        sym = {v: [] for v in range(1, 11)}
        for f, c in zip(FANS, choice):
            for pos, v in enumerate(f): sym[v].append(words[c][pos])
        code.add(tuple("".join(sym[v]) for v in range(1, 11)))
    return sorted(code)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
cert = json.load(open(os.path.join(ROOT, "evidence", "certs", "diamond_3_10_4_8.json")))
FULL = 1023
def m(*vs): return sum(1 << (v - 1) for v in vs)
Z = m(1, 2, 5, 6, 7, 9); U, V, P, Q = m(3), m(10), m(4), m(8)
ING = Counter()
for a, b, c in ((U, V, P), (U, V, Q), (P, Q, 0)):
    for k, x in ((Z | a | c, 1), (Z | b | c, 1), (Z | a | b | c, -1), (Z | c, -1)): ING[k] += x
for k, x in ((Z | U, -1), (Z | V, -1), (Z | U | V, 1), (Z, 1)): ING[k] += x
ING = {k: x for k, x in ING.items() if x and k}

def name(row):
    r = {int(k): v for k, v in row.items()}
    if len(r) == 2 and FULL in r:
        i = (FULL ^ [k for k in r if k != FULL][0]).bit_length()
        return f"H({i}|rest)"
    pos = [k for k, v in r.items() if v > 0]; neg = [k for k, v in r.items() if v < 0]
    big = max(neg); K = min(neg) if len(neg) == 2 else 0
    i, j = [(p ^ K).bit_length() for p in pos]
    Ks = ",".join(str(t + 1) for t in range(10) if K >> t & 1)
    return f"I({i};{j}|{Ks})"

rows = []
ing_y = None
for g in cert["ge"]:
    r = {int(k): v for k, v in g["row"].items()}
    if r == ING: ing_y = F(g["y"]); continue
    rows.append((r, F(g["y"]), name(g["row"])))
assert ing_y == F(1, 3), ing_y
# identity check (coefficient-wise): h(V) - sum u h(v) + sum y g + (1/3) Ing + sum z f == 0 ?
acc = Counter(); acc[FULL] += 1
for v in range(10): acc[1 << v] -= F(cert["u"][v])
for r, y, _ in rows:
    for k, x in r.items(): acc[k] += y * x
for k, x in ING.items(): acc[k] += ing_y * x
for e in cert["eq"]:
    for k, x in e["row"].items(): acc[int(k)] += F(e["z"]) * x
residual = {k: x for k, x in acc.items() if x}
assert not residual, residual
assert all(F(t) == F(2, 3) for t in cert["u"])

def h_from_counts(code):
    n = len(code); h = np.zeros(1024)
    for S in range(1, 1024):
        idx = [t for t in range(10) if S >> t & 1]
        c = Counter(tuple(x[t] for t in idx) for x in code)
        h[S] = math.log2(n) - sum(k * math.log2(k) for k in c.values()) / n
    return h

def h_cover():
    tri = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
    cols = [(v, t) for v in range(1, 11) for t, T in enumerate(tri) if v in T]
    G = np.zeros((20, 30), dtype=np.uint8)
    for t, (a, b, c) in enumerate(tri):
        for r, pat in enumerate(((1, 0, 1), (0, 1, 1))):
            for v, bit in zip((a, b, c), pat):
                G[2 * t + r, cols.index((v, t))] = bit
    def rank(M):
        M = M.copy(); r = 0
        for c in range(M.shape[1]):
            piv = next((i for i in range(r, M.shape[0]) if M[i, c]), None)
            if piv is None: continue
            M[[r, piv]] = M[[piv, r]]
            for i in range(M.shape[0]):
                if i != r and M[i, c]: M[i] ^= M[r]
            r += 1
        return r
    h = np.zeros(1024)
    for S in range(1, 1024):
        sel = [k for k, (v, t) in enumerate(cols) if S >> (v - 1) & 1]
        h[S] = rank(G[:, sel])
    return h

def evaluate(h):
    val = lambda r: sum(x * h[k] for k, x in r.items() if k)
    terms = sorted(((float(y) * val(r), nm, float(y), val(r)) for r, y, nm in rows), reverse=True)
    S = sum(t[0] for t in terms); Ing = val(ING)
    lhs = (2 / 3) * sum(h[1 << v] for v in range(10)) - h[FULL]
    return dict(hV=h[FULL], sum_hv=sum(h[1 << v] for v in range(10)), S=S, Ing=Ing, Ing_plus_3S=Ing + 3 * S,
                identity_residual=lhs - (S + Ing / 3),
                top_terms=[dict(term=nm, y=str(F(y).limit_denominator(1000)), value=v, weighted=w) for w, nm, y, v in terms[:25] if w > 1e-12],
                n_positive_terms=sum(1 for t in terms if t[0] > 1e-12))

out = dict(certificate="evidence/certs/diamond_3_10_4_8.json", identity_exact=True, n_S_rows=len(rows),
           S_rows=[dict(term=nm, y=str(y)) for r, y, nm in rows])
out["cover_code"] = evaluate(h_cover())
out["fan_code"] = evaluate(h_from_counts(build(W)))
json.dump(out, open(os.path.join(ROOT, "evidence", "S-explicit-diamond-3-10-4-8.json"), "w"), indent=1)
for k in ("cover_code", "fan_code"):
    e = out[k]
    print(k, {a: round(b, 6) for a, b in e.items() if isinstance(b, float)}, "positive S terms:", e["n_positive_terms"])
    for t in e["top_terms"][:12]: print("   ", t["term"], "y=", t["y"], "value=", round(t["value"], 5), "weighted=", round(t["weighted"], 5))
