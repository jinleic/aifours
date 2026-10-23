"""Cutting-plane LP with Zhang-Yeung instances on (A+Z,B+Z,C+Z,D+Z), A,B,C,D,Z disjoint (valid for all
entropic vectors; conditioning on Z is valid because ZY holds for each conditional distribution and the
expression is balanced).  BCDRV form:
 -2H(A)-2H(B)-H(C)+3H(AB)+3H(AC)+H(AD)+3H(BC)+H(BD)-H(CD)-4H(ABC)-H(ABD) >= 0.
Exploratory float LP (replay target: BCDRV ZY(R^-) = 1212/181).
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entropy_lp
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks

N = 10
ZY_TERMS = (("A", -2), ("B", -2), ("C", -1), ("AB", 3), ("AC", 3), ("AD", 1), ("BC", 3), ("BD", 1), ("CD", -1), ("ABC", -4), ("ABD", -1))

def zy_row(a, b, c, d):
    sets = dict(A=a, B=b, C=c, D=d)
    r = {}
    for key, cf in ZY_TERMS:
        m = 0
        for ch in key: m |= sets[ch]
        r[m] = r.get(m, 0) + cf
    return {k: v for k, v in r.items() if v}

def scan(hfull, tol, keep_top):
    best = []; total = 6 ** N; chunk = 6 ** 8
    for start in range(0, total, chunk):
        k = np.arange(start, min(total, start + chunk), dtype=np.int64)
        R = [np.zeros_like(k) for _ in range(5)]
        t = k.copy()
        for i in range(N):
            dd = t % 6; t //= 6; bit = 1 << i
            for r in range(5): R[r] |= np.where(dd == r + 1, bit, 0)
        A, B, C, D, Z = R
        m = (A > 0) & (B > 0) & (C > 0) & (D > 0) & (A < B)
        A, B, C, D = A[m] | Z[m], B[m] | Z[m], C[m] | Z[m], D[m] | Z[m]
        H = lambda x: hfull[x]
        v = (-2 * H(A) - 2 * H(B) - H(C) + 3 * H(A | B) + 3 * H(A | C) + H(A | D) + 3 * H(B | C) + H(B | D) - H(C | D) - 4 * H(A | B | C) - H(A | B | D))
        sel = np.nonzero(v < -tol)[0]
        for i in sel:
            best.append((float(v[i]), int(A[i]), int(B[i]), int(C[i]), int(D[i])))
        if len(best) > 20 * keep_top:
            best.sort(); best = best[:keep_top]
    best.sort()
    return best[:keep_top]

def run(edges, max_rounds=60, per_round=300, tol=1e-9, log=None):
    nbm = nbmasks(edges); extra = []; seen = set(); hist = []
    for rnd in range(max_rounds):
        o = entropy_lp.solve(nbm, extra_ge=extra)
        hfull = np.concatenate([[0.0], o["x"]])
        viol = scan(hfull, tol, per_round)
        added = 0
        for v, a, b, c, d in viol:
            key = (a, b, c, d)
            if key in seen: continue
            seen.add(key); extra.append(zy_row(*key)); added += 1
        hist.append(dict(round=rnd, value=o["value"], min_viol=(viol[0][0] if viol else 0.0), added=added, total=len(extra)))
        if log: print(json.dumps(hist[-1]), file=log, flush=True)
        if added == 0: break
    return o, sorted(seen), hist

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    o, keys, hist = run(R_MINUS_EDGES if which == "Rminus" else R_EDGES, log=sys.stdout)
    json.dump(dict(graph=which, value=o["value"], status=o["status"], zy_instances=keys, history=hist),
              open(os.path.join(os.path.dirname(__file__), "..", "evidence", f"zy-cond-cg-{which}.json"), "w"))
