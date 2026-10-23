#!/usr/bin/env python3
"""redei_p5_exhaustive_v1: exact exhaustive check of Redei's direction bound in AG(2,5).

Claim checked: every 5-point subset of AG(2,5) = Z_5^2 that is not a line determines at least (5+3)/2 = 4 of the 6
directions. Also reports the full distribution (number of directions) and the counts for graphs of permutations.
Standard library only; self wall budget 300 s; writes one JSON file given as argv[1] (exclusive create).
"""
import itertools, json, sys, time, os

T0 = time.monotonic()
BUDGET = 300.0
P = 5
pts = [(x, y) for x in range(P) for y in range(P)]

def direction(p, q):
    dx = (q[0] - p[0]) % P
    dy = (q[1] - p[1]) % P
    if dx == 0:
        return "inf"
    inv = pow(dx, P - 2, P)
    return (dy * inv) % P          # slope in Z_5

def is_line(S):
    dirs = {direction(p, q) for p, q in itertools.combinations(S, 2)}
    return len(dirs) == 1

dist = {}
min_nonline = None
n_sets = n_lines = 0
graph_dist = {}
violations = []
for S in itertools.combinations(pts, 5):
    n_sets += 1
    if (n_sets & 4095) == 0 and time.monotonic() - T0 > BUDGET:
        print("BUDGET_STOP", file=sys.stderr)
        sys.exit(3)
    dirs = {direction(p, q) for p, q in itertools.combinations(S, 2)}
    k = len(dirs)
    line = (k == 1)
    n_lines += line
    dist[k] = dist.get(k, 0) + 1
    if not line:
        if min_nonline is None or k < min_nonline:
            min_nonline = k
        if k < 4:
            violations.append(S)
    xs = sorted(p[0] for p in S); ys = sorted(p[1] for p in S)
    if xs == list(range(P)) and ys == list(range(P)):
        graph_dist[k] = graph_dist.get(k, 0) + 1

out = {
    "probe": "redei_p5_exhaustive_v1",
    "subsets": n_sets,
    "expected_subsets": 53130,
    "lines": n_lines,
    "expected_lines": 30,
    "direction_count_distribution": {str(k): v for k, v in sorted(dist.items())},
    "min_directions_nonline": min_nonline,
    "violations_lt4": len(violations),
    "permutation_graphs_direction_distribution": {str(k): v for k, v in sorted(graph_dist.items())},
    "permutation_graphs_total": sum(graph_dist.values()),
    "claim_holds": (len(violations) == 0 and n_sets == 53130 and n_lines == 30),
    "elapsed_s": round(time.monotonic() - T0, 3),
}
with open(sys.argv[1], "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out))
sys.exit(0 if out["claim_holds"] else 1)
