"""Cutting-plane LP with conditional Ingleton instances Ing(A+Z,B+Z,C+Z,D+Z), A,B,C,D,Z disjoint (6^10 scan).

Valid for linear rank functions (contraction by Z); NOT valid for general entropic vectors.
Exploratory float LP; instances recorded for later conditional-validity analysis.
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entropy_lp
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks
from ingleton_cg import ing_row

N = 10
def scan(hfull, tol, keep_top):
    best = []
    total = 6 ** N; chunk = 6 ** 8
    for start in range(0, total, chunk):
        k = np.arange(start, min(total, start + chunk), dtype=np.int64)
        A = np.zeros_like(k); B = np.zeros_like(k); C = np.zeros_like(k); D = np.zeros_like(k); Z = np.zeros_like(k)
        t = k.copy()
        for i in range(N):
            d = t % 6; t //= 6; bit = 1 << i
            A |= np.where(d == 1, bit, 0); B |= np.where(d == 2, bit, 0); C |= np.where(d == 3, bit, 0)
            D |= np.where(d == 4, bit, 0); Z |= np.where(d == 5, bit, 0)
        m = (A > 0) & (B > 0) & (C > 0) & (D > 0) & (A < B) & (C < D)
        A, B, C, D, Z = A[m] | Z[m], B[m] | Z[m], C[m] | Z[m], D[m] | Z[m], Z[m]
        H = lambda x: hfull[x]
        v = (-H(A) - H(B) + H(A | B) + H(A | C) + H(A | D) + H(B | C) + H(B | D) - H(C | D) - H(A | B | C) - H(A | B | D))
        sel = np.nonzero(v < -tol)[0]
        for i in sel:
            best.append((float(v[i]), int(A[i]), int(B[i]), int(C[i]), int(D[i])))
        if len(best) > 20 * keep_top:
            best.sort(); best = best[:keep_top]
    best.sort()
    return best[:keep_top]

def run(edges, max_rounds=100, per_round=400, tol=1e-9, log=None):
    nbm = nbmasks(edges); extra = []; seen = set(); hist = []
    for rnd in range(max_rounds):
        o = entropy_lp.solve(nbm, extra_ge=extra)
        hfull = np.concatenate([[0.0], o["x"]])
        viol = scan(hfull, tol, per_round)
        added = 0
        for v, a, b, c, d in viol:
            key = (a, b, c, d)
            if key in seen: continue
            seen.add(key); extra.append(ing_row(*key)); added += 1
        hist.append(dict(round=rnd, value=o["value"], min_ing=(viol[0][0] if viol else 0.0), added=added, total=len(extra)))
        if log: print(json.dumps(hist[-1]), file=log, flush=True)
        if added == 0: break
    return o, sorted(seen), hist

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    o, keys, hist = run(R_MINUS_EDGES if which == "Rminus" else R_EDGES, log=sys.stdout)
    json.dump(dict(graph=which, value=o["value"], status=o["status"], instances=keys, history=hist),
              open(os.path.join(os.path.dirname(__file__), "..", "evidence", f"ingleton-cond-cg-{which}.json"), "w"))
