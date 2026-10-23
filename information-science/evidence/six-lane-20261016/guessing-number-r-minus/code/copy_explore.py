"""Explore single copy-lemma steps targeted at the diamond (3,10,4,8 | Z), with Aut(R^-) symmetry.
Exploratory float LPs; best configurations are re-solved and certified separately."""
import sys, os, json, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
from copy_lp import Model

def perm(cycles):
    p = list(range(10))
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]): p[a - 1] = b - 1
    return p
SIG = perm([(1, 8), (2, 10, 5, 9), (3, 7, 4, 6)]); TAU = perm([(2, 5), (3, 6), (4, 7)])
Z0 = [0, 1, 4, 5, 6, 8]; DIA = [2, 9, 3, 7]   # vertices 3,10,4,8

def run(copies, sym=True):
    m = Model(nbmasks(R_MINUS_EDGES))
    m.add_block(copies)
    t0 = time.time()
    st, val, nc, nr = m.solve(sym_perms=[SIG, TAU] if sym else [])
    return dict(copies=copies, status=st, value=val, cols=nc, rows=nr, wall=round(time.time() - t0, 1))

if __name__ == "__main__":
    out = []
    base = run([])
    print(json.dumps(base)); sys.stdout.flush(); out.append(base)
    cfgs = []
    for k in (1, 2):
        for X in itertools.combinations(DIA, k):
            rest = [d for d in DIA if d not in X]
            for r in range(len(rest) + 1):
                for W in itertools.combinations(rest, r):
                    cfgs.append((list(X), sorted(Z0 + list(W))))
    for X, Y in cfgs:
        res = run([(X, Y)])
        out.append(res); print(json.dumps(res)); sys.stdout.flush()
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "copy-explore-diamond.json"), "w"))
