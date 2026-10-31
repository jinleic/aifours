#!/usr/bin/env python3
"""Reviewer-written control for the classical no-OLS(6) import and for the
P-completion search routine used in proof-independent-controls-v1.py.

Searches for an orthogonal array OA(n^2,4,n,2) (equivalently a pair of
orthogonal Latin squares of order n) with the same row-by-row MRV
backtracking as the review's P-completion routine, plus two standard
symmetry reductions: the row a=0 is (0,b,b,b) and the column b=0 has c=a.

    python3 -B proof-ols6-control-v1.py <new-output.json>
"""
import json
import os
import sys
import time


def oa_exists(n, node_cap=None):
    used = [set() for _ in range(6)]  # (a,c),(a,d),(b,c),(b,d),(c,d) at indices 1..5
    words = []
    rows = [(a, b) for a in range(n) for b in range(n)]
    nodes = [0]
    capped = [False]

    def add(a, b, c, d):
        for pi, key in ((1, (a, c)), (2, (a, d)), (3, (b, c)), (4, (b, d)), (5, (c, d))):
            used[pi].add(key)
        words.append((a, b, c, d))

    def remove(a, b, c, d):
        for pi, key in ((1, (a, c)), (2, (a, d)), (3, (b, c)), (4, (b, d)), (5, (c, d))):
            used[pi].discard(key)
        words.pop()

    def options(a, b):
        res = []
        for c in range(n):
            if (a, c) in used[1] or (b, c) in used[3]:
                continue
            if b == 0 and c != a:  # reduced first column of the first square
                continue
            for d in range(n):
                if (a, d) in used[2] or (b, d) in used[4] or (c, d) in used[5]:
                    continue
                res.append((c, d))
        return res

    # fixed first row: (0,b,b,b)
    for b in range(n):
        add(0, b, b, b)
    remaining = [(a, b) for (a, b) in rows if a != 0]

    def rec(remaining):
        nodes[0] += 1
        if node_cap and nodes[0] > node_cap:
            capped[0] = True
            return False
        if not remaining:
            return True
        best, bestopts = None, None
        for r in remaining:
            o = options(*r)
            if not o:
                return False
            if best is None or len(o) < len(bestopts):
                best, bestopts = r, o
        rem2 = [r for r in remaining if r != best]
        a, b = best
        for (c, d) in bestopts:
            add(a, b, c, d)
            if rec(rem2):
                return True
            remove(a, b, c, d)
        return False

    ok = rec(remaining)
    return ok, nodes[0], capped[0], (list(words) if ok else None)


def main():
    if len(sys.argv) != 2 or os.path.exists(sys.argv[1]):
        print(__doc__)
        sys.exit(2)
    rep = {}
    for n in (3, 4, 5, 6, 7):
        t = time.time()
        ok, nodes, capped, w = oa_exists(n)
        rep[f"order_{n}"] = {"OA_exists": ok, "nodes": nodes, "capped": capped, "seconds": round(time.time() - t, 2)}
        if ok:
            # verify the witness is pairwise pair-distinct
            pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            good = all(len(set((x[i], x[j]) for x in w)) == n * n for (i, j) in pairs)
            rep[f"order_{n}"]["witness_pair_injective"] = good
            rep[f"order_{n}"]["witness"] = w
        print(n, rep[f"order_{n}"]["OA_exists"], nodes, flush=True)
    with open(sys.argv[1], "x") as f:
        json.dump(rep, f, indent=1)
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "witness"} for k, v in rep.items()}, indent=1))


if __name__ == "__main__":
    main()
