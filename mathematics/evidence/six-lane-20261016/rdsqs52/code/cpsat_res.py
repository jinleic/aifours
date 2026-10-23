"""CP-SAT resolution with AllDifferent per point (colour[t] in 0..k-1), anchor triples fixed.
Usage: cpsat_res.py FILE.tri ANCHOR SECONDS WORKERS SEED -> prints status and writes FILE.cpsat.json"""
import sys, json, time
from ortools.sat.python import cp_model
path, anchor, secs, workers, seed = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
lines = open(path).read().split("\n")
v, m = map(int, lines[0].split())
T = [tuple(map(int, l.split())) for l in lines[1:1 + m]]
k = (v - 1) // 2
md = cp_model.CpModel()
col = [md.NewIntVar(0, k - 1, f"c{i}") for i in range(m)]
inc = {}
for i, t in enumerate(T):
    for p in t:
        inc.setdefault(p, []).append(i)
for p, ts in inc.items():
    md.AddAllDifferent([col[i] for i in ts])
anc = sorted([i for i, t in enumerate(T) if anchor in t], key=lambda i: T[i])
for c, i in enumerate(anc):
    md.Add(col[i] == c)
s = cp_model.CpSolver()
s.parameters.max_time_in_seconds = secs
s.parameters.num_workers = workers
s.parameters.random_seed = seed
t0 = time.time()
st = s.Solve(md)
name = s.StatusName(st)
out = {"file": path, "status": name, "seconds": round(time.time() - t0, 2), "workers": workers, "seed": seed}
if name in ("OPTIMAL", "FEASIBLE"):
    cols = [s.Value(c) for c in col]
    classes = [[] for _ in range(k)]
    for i, c in enumerate(cols):
        classes[c].append(T[i])
    ok = all(sorted(p for t in C for p in t) == sorted(range(v)) for C in classes)
    out["verified_partition"] = ok
    out["classes"] = classes
json.dump(out, open(path + ".cpsat.json", "w"))
print(name, out["seconds"], out.get("verified_partition"))
