"""Cutting-plane LP with Ingleton instances on disjoint (A,B,C,D) (exploratory, HiGHS float).

Ing(A,B,C,D) = -h(A)-h(B)+h(AB)+h(AC)+h(AD)+h(BC)+h(BD)-h(CD)-h(ABC)-h(ABD) >= 0
(holds for linear rank functions; NOT valid for all entropic vectors).  Separation scans all 5^10
assignments of the 10 variables to {none,A,B,C,D} with A,B nonempty and C,D nonempty.
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entropy_lp
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks

N = 10
def all_quads():
    k = np.arange(5 ** N, dtype=np.int64)
    A = np.zeros_like(k); B = np.zeros_like(k); C = np.zeros_like(k); D = np.zeros_like(k)
    t = k.copy()
    for i in range(N):
        d = t % 5; t //= 5
        bit = 1 << i
        A |= np.where(d == 1, bit, 0); B |= np.where(d == 2, bit, 0)
        C |= np.where(d == 3, bit, 0); D |= np.where(d == 4, bit, 0)
    keep = (A > 0) & (B > 0) & (C > 0) & (D > 0) & (A < B) & (C < D)  # symmetry A<->B, C<->D
    return A[keep], B[keep], C[keep], D[keep]

def ing_values(hfull, A, B, C, D):
    H = lambda m: hfull[m]
    return (-H(A) - H(B) + H(A | B) + H(A | C) + H(A | D) + H(B | C) + H(B | D) - H(C | D) - H(A | B | C) - H(A | B | D))

def ing_row(a, b, c, d):
    r = {}
    for m, cf in ((a, -1), (b, -1), (a | b, 1), (a | c, 1), (a | d, 1), (b | c, 1), (b | d, 1), (c | d, -1), (a | b | c, -1), (a | b | d, -1)):
        if m: r[m] = r.get(m, 0) + cf
    return {k: v for k, v in r.items() if v}

def run(edges, max_rounds=200, per_round=300, tol=1e-9, log=None):
    nbm = nbmasks(edges)
    A, B, C, D = all_quads()
    extra = []; seen = set(); hist = []
    for rnd in range(max_rounds):
        o = entropy_lp.solve(nbm, extra_ge=extra)
        hfull = np.concatenate([[0.0], o["x"]])
        vals = ing_values(hfull, A, B, C, D)
        order = np.argsort(vals)[: per_round * 4]
        added = 0
        for i in order:
            if vals[i] >= -tol: break
            key = (int(A[i]), int(B[i]), int(C[i]), int(D[i]))
            if key in seen: continue
            seen.add(key); extra.append(ing_row(*key)); added += 1
            if added >= per_round: break
        hist.append(dict(round=rnd, value=o["value"], min_ing=float(vals.min()), added=added, total_ing=len(extra)))
        if log: print(json.dumps(hist[-1]), file=log, flush=True)
        if added == 0:
            break
    return o, extra, sorted(seen), hist

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    o, extra, keys, hist = run(R_MINUS_EDGES if which == "Rminus" else R_EDGES, log=sys.stdout)
    json.dump(dict(graph=which, value=o["value"], status=o["status"], ingleton_instances=keys, history=hist),
              open(os.path.join(os.path.dirname(__file__), "..", "evidence", f"ingleton-cg-{which}.json"), "w"))
