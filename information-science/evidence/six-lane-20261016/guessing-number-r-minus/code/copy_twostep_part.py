"""Two-step copy chains (exploratory): step 1 fixed (best single copy), step 2 enumerated."""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_explore import run, Z0
from graphs import R_MINUS_EDGES, nbmasks
part, nparts, first = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
FIRST = {"A": ([9], [0, 1, 2, 4, 5, 6, 7, 8]), "B": ([2], [0, 1, 4, 5, 6, 7, 8, 9]), "C": ([3], [0, 1, 4, 5, 6, 7, 8, 9])}[first]
pool = [2, 9, 3, 7, 10]  # diamond 3,10,4,8 and the first copy (index 10)
nbm = nbmasks(R_MINUS_EDGES)
def det(x, Y):  # is base var x determined by base set Y via FD closure? (copies treated as free)
    T = set(v for v in Y if v < 10); ch = True
    while ch:
        ch = False
        for v in range(10):
            if v not in T and all(((nbm[v] >> u) & 1) == 0 or u in T for u in range(10)):
                T.add(v); ch = True
    return x < 10 and x in T
cfgs = []
for X in pool:
    rest = [d for d in pool if d != X]
    for r in range(1, len(rest) + 1):
        for W in itertools.combinations(rest, r):
            Y = sorted(Z0 + list(W))
            if det(X, Y): continue
            cfgs.append(([X], Y))
out = os.path.join(os.path.dirname(__file__), "..", "evidence", f"copy-twostep-{first}.part{part}.jsonl")
with open(out, "a") as fh:
    for i, step2 in enumerate(cfgs):
        if i % nparts != part: continue
        res = run([FIRST, step2]); fh.write(json.dumps(res) + "\n"); fh.flush()
