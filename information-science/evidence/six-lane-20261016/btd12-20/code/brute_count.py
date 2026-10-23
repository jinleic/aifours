#!/usr/bin/env python3
"""brute_count.py -- independent stdlib brute-force counter for tiny BTD parameters (lane btd12-15, README 1.6
encoding controls).  Shares no code with the CNF generators.

Counts the V x B matrices over {0,1,2} satisfying (D1)-(D4) and, separately, those that also satisfy (S0) (row 0 =
0^z 1^p1 2^p2) and (S1) (rows lexicographically nondecreasing top to bottom, columns lexicographically nondecreasing
left to right, compared top to bottom, with 0 < 1 < 2).
Method: all row vectors with the required composition are listed; matrices are built row by row with pairwise inner
products checked as rows are added and column partial sums bounded by K; at the leaves the column sums are checked
exactly and the symmetry conditions are evaluated directly from their definitions.
  mode all : enumerate every matrix (no symmetry used during the search) and report counts for none / S0 / S1;
  mode s1  : enumerate only matrices whose rows are nondecreasing and row 0 sorted (both necessary for S1), then test
             the column condition at the leaves; reports the S1 count only.
Usage: brute_count.py V B p1 p2 R K L MODE OUT.json      (OUT exclusive)
"""
import itertools
import json
import sys
import time


def rows_with_composition(B, p1, p2):
    out = []
    for nz in itertools.combinations(range(B), p1 + p2):
        for tw in itertools.combinations(nz, p2):
            r = [0] * B
            for j in nz:
                r[j] = 1
            for j in tw:
                r[j] = 2
            out.append(tuple(r))
    out.sort()
    return out


def main(argv):
    if len(argv) != 10:
        print(__doc__, file=sys.stderr)
        return 2
    V, B, p1, p2, R, K, L = (int(x) for x in argv[1:8])
    mode, out = argv[8], argv[9]
    assert R == p1 + 2 * p2 and mode in ("all", "s1")
    rows = rows_with_composition(B, p1, p2)
    z = B - p1 - p2
    row0 = tuple([0] * z + [1] * p1 + [2] * p2)
    dot = {}
    counts = {"none": 0, "S0": 0, "S1": 0}
    t0 = time.time()
    M = []
    colsum = [0] * B

    def leaf():
        if any(c != K for c in colsum):
            return
        counts["none"] += 1
        if M[0] == row0:
            counts["S0"] += 1
        rows_ok = all(M[i] <= M[i + 1] for i in range(V - 1))
        cols = [tuple(M[i][j] for i in range(V)) for j in range(B)]
        cols_ok = all(cols[j] <= cols[j + 1] for j in range(B - 1))
        if rows_ok and cols_ok:
            counts["S1"] += 1

    def rec(depth, start):
        if depth == V:
            leaf()
            return
        cand = rows if mode == "all" else ([row0] if depth == 0 else rows[start:])
        for idx, r in enumerate(cand):
            ok = True
            for prev in M:
                d = sum(x * y for x, y in zip(prev, r))
                if d != L:
                    ok = False
                    break
            if not ok:
                continue
            if any(colsum[j] + r[j] > K for j in range(B)):
                continue
            M.append(r)
            for j in range(B):
                colsum[j] += r[j]
            nxt = 0 if mode == "all" else (rows.index(r) if depth == 0 else start + idx)
            rec(depth + 1, nxt)
            for j in range(B):
                colsum[j] -= r[j]
            M.pop()

    rec(0, 0)
    res = {"program": "brute_count.py", "params": [V, B, p1, p2, R, K, L], "mode": mode,
           "row_vectors": len(rows), "seconds": round(time.time() - t0, 3)}
    if mode == "all":
        res.update({"count_no_symmetry": counts["none"], "count_S0": counts["S0"], "count_S1": counts["S1"]})
    else:
        res.update({"count_S1": counts["S1"]})
    with open(out, "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps(res))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
