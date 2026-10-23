"""CP-SAT model (OR-tools, lane-local venv) for a cyclic (v,k,1) difference family, t = (v-1)/(k(k-1)).

Variables: block i = {x[i][0] = 0 < x[i][1] < ... < x[i][k-1]} in Z_v.
Constraints: c = min(d, v-d) for every within-block difference d = x[i][l] - x[i][j] (l > j);
AllDifferent over all t*k(k-1)/2 classes (exactly (v-1)/2 values, so a permutation).
Symmetry breaking (normalisations every DF admits):
  - each block is the translate starting at its unique smallest circular gap: x[i][1] < every other
    gap (gaps are differences, hence distinct);
  - the block containing the class 1 is block 0 (so x[0][1] = 1);
  - blocks 1..t-1 sorted by their smallest gap: x[1][1] < x[2][1] < ... (smallest gaps are distinct).
usage: venv/bin/python cpsat_cdf.py v k seed seconds workers OUT_PREFIX
Writes OUT_PREFIX.sol in the strict certificate format if a solution is found; prints status JSON.
"""
import sys, json, time
from ortools.sat.python import cp_model

def main():
    v, k, seed, secs, workers, pre = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    t, n = (v - 1) // (k * (k - 1)), (v - 1) // 2
    m = cp_model.CpModel()
    x = [[m.NewIntVar(0, v - 1, f"x{i}_{j}") for j in range(k)] for i in range(t)]
    for i in range(t):
        m.Add(x[i][0] == 0)
        for j in range(k - 1): m.Add(x[i][j] < x[i][j + 1])
        for j in range(1, k - 1): m.Add(x[i][1] < x[i][j + 1] - x[i][j])
        m.Add(x[i][1] < v - x[i][k - 1])
    m.Add(x[0][1] == 1)
    for i in range(1, t - 1): m.Add(x[i][1] < x[i + 1][1])
    cl = []
    for i in range(t):
        for j in range(k):
            for l in range(j + 1, k):
                d = m.NewIntVar(1, v - 1, f"d{i}_{j}_{l}"); m.Add(d == x[i][l] - x[i][j])
                e = m.NewIntVar(1, v - 1, f"e{i}_{j}_{l}"); m.Add(e == v - d)
                c = m.NewIntVar(1, n, f"c{i}_{j}_{l}"); m.AddMinEquality(c, [d, e])
                cl.append(c)
    m.AddAllDifferent(cl)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = secs
    s.parameters.num_workers = workers
    s.parameters.random_seed = seed
    t0 = time.time()
    st = s.Solve(m)
    res = dict(v=v, k=k, t=t, seed=seed, workers=workers, status=s.StatusName(st), wall=round(time.time() - t0, 1),
               branches=s.NumBranches(), conflicts=s.NumConflicts())
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        blocks = [[s.Value(x[i][j]) for j in range(k)] for i in range(t)]
        with open(pre + ".sol", "w") as f:
            f.write(f"CDF {v} {k}\n")
            for B in blocks: f.write(" ".join(map(str, B)) + "\n")
        res["blocks"] = blocks
    print(json.dumps(res), flush=True)

if __name__ == "__main__":
    main()
