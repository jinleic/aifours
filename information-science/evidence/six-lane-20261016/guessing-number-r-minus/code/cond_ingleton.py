"""LP with conditional Ingleton instances that are VALID for exact guessing-game codes.

Ing(A,B,C,D) = I(A;B|C)+I(A;B|D)+I(C;D)-I(A;B) >= 0 holds for every discrete (entropic) distribution
whenever one of Boege's ten CI hypothesis sets holds (Boege arXiv:2204.03971v3, Thm; Studeny 2021;
in Boege's labels X=C, Y=D, Z=A, U=B).  For the uniform distribution on a winning set, the only CI
statements used are those FORCED by the functional dependencies:  I(P;Q|R)=0 if P or Q lies in cl(R),
cl = closure under 'v in cl(S) if N(v) subset S'.  Instances are Ing(A+Z,B+Z,C+Z,D+Z), A..D,Z disjoint.
Exploratory float LP; exact certification separately.
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entropy_lp
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks
from ingleton_cg import ing_row

N = 10
def closures(nbm, n=N):
    cl = np.zeros(1 << n, dtype=np.int64)
    for S in range(1 << n):
        T = S
        while True:
            T2 = T
            for v in range(n):
                if (nbm[v] & ~T2) == 0 and nbm[v] != 0:
                    T2 |= 1 << v
            if T2 == T: break
            T = T2
        cl[S] = T
    return cl

def make_valid(cl):
    def ci0(P, Q, R):  # FD-implied I(P;Q|R)=0  (vectorized on int arrays)
        c = cl[R]
        return ((P & ~c) == 0) | ((Q & ~c) == 0)
    def valid(A, B, C, D):
        s1 = ci0(A, B, 0 * A) | ci0(C, A, 0 * A) | ci0(D, A, 0 * A) | ci0(C, B, 0 * A) | ci0(D, B, 0 * A)
        s3 = ci0(C, A, D) | ci0(D, A, C) | ci0(C, B, D) | ci0(D, B, C)
        s4 = ci0(C, D, A | B)
        s5 = ci0(C, A, D | B) | ci0(D, A, C | B) | ci0(C, B, D | A) | ci0(D, B, C | A)
        cd0 = ci0(C, D, 0 * A)
        p21 = cd0 & (ci0(C, D, A) | ci0(C, D, B))
        p22 = (ci0(C, D, A) & (ci0(D, B, A) | ci0(C, B, A))) | (ci0(C, D, B) & (ci0(D, A, B) | ci0(C, A, B)))
        p23 = (ci0(C, A, B) & ci0(C, B, A)) | (ci0(D, A, B) & ci0(D, B, A))
        p24 = (ci0(C, A, B) & ci0(A, B, C)) | (ci0(D, A, B) & ci0(A, B, D)) | (ci0(C, B, A) & ci0(A, B, C)) | (ci0(D, B, A) & ci0(A, B, D))
        p25 = (ci0(C, A, B) & ci0(D, A, B)) | (ci0(C, B, A) & ci0(D, B, A))
        return s1 | s3 | s4 | s5 | p21 | p22 | p23 | p24 | p25
    return valid

def scan(hfull, valid, tol, keep_top, only_valid=True):
    best = []; total = 6 ** N; chunk = 6 ** 8; nviol_all = 0; nviol_valid = 0
    for start in range(0, total, chunk):
        k = np.arange(start, min(total, start + chunk), dtype=np.int64)
        A = np.zeros_like(k); B = np.zeros_like(k); C = np.zeros_like(k); D = np.zeros_like(k); Z = np.zeros_like(k)
        t = k.copy()
        for i in range(N):
            d = t % 6; t //= 6; bit = 1 << i
            A |= np.where(d == 1, bit, 0); B |= np.where(d == 2, bit, 0); C |= np.where(d == 3, bit, 0)
            D |= np.where(d == 4, bit, 0); Z |= np.where(d == 5, bit, 0)
        m = (A > 0) & (B > 0) & (C > 0) & (D > 0) & (A < B) & (C < D)
        A, B, C, D = A[m] | Z[m], B[m] | Z[m], C[m] | Z[m], D[m] | Z[m]
        H = lambda x: hfull[x]
        v = (-H(A) - H(B) + H(A | B) + H(A | C) + H(A | D) + H(B | C) + H(B | D) - H(C | D) - H(A | B | C) - H(A | B | D))
        neg = v < -tol
        nviol_all += int(neg.sum())
        if only_valid:
            ok = valid(A[neg], B[neg], C[neg], D[neg])
            idx = np.nonzero(neg)[0][ok]
        else:
            idx = np.nonzero(neg)[0]
        nviol_valid += len(idx)
        for i in idx:
            best.append((float(v[i]), int(A[i]), int(B[i]), int(C[i]), int(D[i])))
        if len(best) > 20 * keep_top:
            best.sort(); best = best[:keep_top]
    best.sort()
    return best[:keep_top], nviol_all, nviol_valid

def run(edges, max_rounds=200, per_round=400, tol=1e-9, log=None, only_valid=True):
    nbm = nbmasks(edges); cl = closures(nbm); valid = make_valid(cl)
    extra = []; seen = set(); hist = []
    for rnd in range(max_rounds):
        o = entropy_lp.solve(nbm, extra_ge=extra)
        hfull = np.concatenate([[0.0], o["x"]])
        viol, na, nv = scan(hfull, valid, tol, per_round, only_valid)
        added = 0
        for v, a, b, c, d in viol:
            key = (a, b, c, d)
            if key in seen: continue
            seen.add(key); extra.append(ing_row(*key)); added += 1
        hist.append(dict(round=rnd, value=o["value"], violated_all=na, violated_valid=nv, added=added, total=len(extra)))
        if log: print(json.dumps(hist[-1]), file=log, flush=True)
        if added == 0: break
    return o, sorted(seen), hist

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    o, keys, hist = run(R_MINUS_EDGES if which == "Rminus" else R_EDGES, log=sys.stdout)
    json.dump(dict(graph=which, value=o["value"], status=o["status"], valid_instances=keys, history=hist),
              open(os.path.join(os.path.dirname(__file__), "..", "evidence", f"cond-ingleton-valid-{which}.json"), "w"))
