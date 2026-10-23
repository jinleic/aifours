"""Maximum winning set for the guessing game on G with alphabet {0,1} (CP-SAT; exploratory).

C subset {0,1}^10 is winning iff no x != y in C have x+y in S, S = {z: exists v in supp z with
N(v) cap supp z empty}.  gn(G,2) = log2 max|C|.  Beating 20/3 at q=2 needs |C| >= 102.
Symmetry breaking: translation invariance lets us assume 0 in C.  A found code is re-verified by brute
force (every pair) in verify_code().
Usage: python mis_q2.py [Rminus|R] [timeout_s] [target_lb]
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks

def forbidden_diffs(nbm, n=10):
    S = []
    for z in range(1, 1 << n):
        for v in range(n):
            if (z >> v) & 1 and (nbm[v] & z) == 0:
                S.append(z); break
    return S

def verify_code(code, nbm, n=10):
    """Brute-force decoding check: each player v guesses x_v from x_{N(v)} via a lookup built from C."""
    table = {}
    for x in code:
        for v in range(n):
            key = (v, x & nbm[v])
            b = (x >> v) & 1
            if table.setdefault(key, b) != b:
                return False
    return True

def solve(edges, timeout, lb=None, workers=3):
    from ortools.sat.python import cp_model
    nbm = nbmasks(edges); S = forbidden_diffs(nbm)
    m = cp_model.CpModel()
    x = [m.NewBoolVar(f"x{i}") for i in range(1024)]
    seen = set()
    for a in range(1024):
        for z in S:
            b = a ^ z
            if a < b:
                m.AddBoolOr([x[a].Not(), x[b].Not()])
    m.Add(x[0] == 1)
    if lb: m.Add(sum(x) >= lb)
    m.Maximize(sum(x))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = timeout; s.parameters.num_search_workers = workers
    t0 = time.time(); st = s.Solve(m)
    code = [i for i in range(1024) if s.Value(x[i])] if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    return dict(status=s.StatusName(st), best=len(code), bound=s.BestObjectiveBound(), wall=round(time.time() - t0, 1),
                forbidden_diffs=len(S), code_verified=verify_code(code, nbm) if code else None, code=code)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    T = float(sys.argv[2]) if len(sys.argv) > 2 else 300
    lb = int(sys.argv[3]) if len(sys.argv) > 3 else None
    out = solve(R_MINUS_EDGES if which == "Rminus" else R_EDGES, T, lb)
    out["graph"] = which
    print(json.dumps(out))
