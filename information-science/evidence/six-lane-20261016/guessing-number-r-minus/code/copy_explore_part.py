import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_explore import run, Z0, DIA
part, nparts = int(sys.argv[1]), int(sys.argv[2])
cfgs = []
for k in (1, 2):
    for X in itertools.combinations(DIA, k):
        rest = [d for d in DIA if d not in X]
        for r in range(len(rest) + 1):
            for W in itertools.combinations(rest, r):
                cfgs.append((list(X), sorted(Z0 + list(W))))
out = os.path.join(os.path.dirname(__file__), "..", "evidence", f"copy-explore-diamond.part{part}.jsonl")
with open(out, "a") as fh:
    for i, (X, Y) in enumerate(cfgs):
        if i % nparts != part: continue
        res = run([(X, Y)])
        fh.write(json.dumps(res) + "\n"); fh.flush()
