"""Global nonlinear-code search under the frozen max_v obligation (binary, biased columns).

A binary FD-consistent code C on R^- with N words in which every column has at most m ones.
Translation by a fixed vector is an automorphism of the confusion graph, so WLOG every column's
minority symbol is 1.  Such a code gives gn(R^-) >= log2 N / h2(m/N) by an elementary type-class
bridge:
  - take C^n restricted to sequences using each codeword exactly n/N times;
  - its size is >= N^n/(n+1)^N, and every vertex alphabet has size <= C(n, n m_v/N) <= 2^{n h2(m/N)}.
  - Exact comparison: ratio > 20/3  <=>  (m^m (N-m)^(N-m))^20 > N^(17N).
Candidate windows are the (N,m) with 20/3 < log2 N/h2(m/N) <= 1847/276.  Pairs above 1847/276 are
impossible by Gurpinar's theorem; they serve as NEGATIVE controls, and the solver must never return
FEASIBLE there.  Positive control: (64,32), realised by three disjoint triangles.
CP-SAT, 3 workers, time limit per pair.  UNKNOWN is not UNSAT.
"""
import sys, os, json, math, time
from ortools.sat.python import cp_model
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
NBM = nbmasks(R_MINUS_EDGES)
D = [d for d in range(1, 1024) if any((d >> v) & 1 and not (d & NBM[v]) for v in range(10))]
h2 = lambda p: 0.0 if p <= 0 or p >= 1 else -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def exact_beats(N, m):   # (m^m (N-m)^(N-m))^20 > N^(17N)
    return (m ** m * (N - m) ** (N - m)) ** 20 > N ** (17 * N)

def fd_ok(code):
    for v in range(10):
        seen = {}
        for x in code:
            if seen.setdefault(x & NBM[v], (x >> v) & 1) != (x >> v) & 1: return False
    return True

def run(N, m, tlim, seed=0):
    mdl = cp_model.CpModel(); x = [mdl.NewBoolVar(f"x{w}") for w in range(1024)]
    Dset = set(D)
    for w in range(1024):
        for d in D:
            w2 = w ^ d
            if w2 > w: mdl.AddBoolOr([x[w].Not(), x[w2].Not()])
    mdl.Add(sum(x) == N)
    for v in range(10):
        mdl.Add(sum(x[w] for w in range(1024) if (w >> v) & 1) <= m)
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = tlim
    s.parameters.num_workers = 3; s.parameters.random_seed = seed
    t0 = time.time(); st = s.Solve(mdl)
    rec = dict(N=N, m=m, ratio=math.log2(N) / h2(m / N), exact_beats_20_3=exact_beats(N, m),
               status=s.StatusName(st), wall=round(time.time() - t0, 1))
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        code = [w for w in range(1024) if s.Value(x[w])]
        rec.update(code=code, fd_ok=fd_ok(code), col_ones=[sum((w >> v) & 1 for w in code) for v in range(10)])
    return rec

if __name__ == "__main__":
    tlim = float(sys.argv[1]) if len(sys.argv) > 1 else 120
    lo, hi = 20 / 3, 1847 / 276
    cands = [(N, m) for N in range(2, 104) for m in range(1, N // 2 + 1) if lo < math.log2(N) / h2(m / N) <= hi]
    controls = [(64, 32, "positive"), (88, 34, "negative: ratio 6.711 > 1847/276"), (41, 9, "negative")]
    out = os.path.join(os.path.dirname(__file__), "..", "evidence", "biased-binary-search.jsonl")
    with open(out, "a") as fh:
        fh.write(json.dumps(dict(meta=True, D_size=len(D), tlim=tlim, n_candidates=len(cands))) + "\n")
        for N, m, kind in controls:
            r = run(N, m, tlim); r["control"] = kind; fh.write(json.dumps(r) + "\n"); fh.flush()
            print(json.dumps({k: v for k, v in r.items() if k != "code"}), flush=True)
        for N, m in sorted(cands, key=lambda t: t[0]):
            r = run(N, m, tlim); fh.write(json.dumps(r) + "\n"); fh.flush()
            print(json.dumps({k: v for k, v in r.items() if k != "code"}), flush=True)
