#!/usr/bin/env python3
"""P0-quad skeleton split for the non-balanced multisets E1..E3c (Amendment A2).

For a multiset with c0 P0 columns and special (non-P0) columns X, row r lies in the quads of
a set T(r) of P0 columns. Facts (README A2): each P0 quad has 4 rows; two quads share <= 1
row; |T(r)| <= 2 - w(r) with w(r) = sum_{c in X} (n_{c,A[r][c]} - 3) >= wmin = sum_X min e;
rows with |T(r)| >= 3 have w(r) <= -1 so lie in a light block (size <= 2) of some special
column: their number is <= hmax = number of rows in light blocks of X.
Skeleton = hypergraph (simple graph of |T|=2 rows + hyperedges of size 3..tmax), private
rows (|T|=1) fill every P0 column to degree 4, the rest are rows with T empty. Enumerated
from geng graphs on c0 vertices (max degree 4) plus all hyperedge sets, deduplicated up to
isomorphism with networkx (colored incidence graphs).
Single special column (c0 = 7): exact feasibility filter: the special column's multiset of
e-values must be assignable to rows with 0 <= 2 - |T(r)| - e <= L (bipartite check).
Usage (research venv): gen_skel.py MULTISET_INDEX OUTDIR
"""
import itertools
import json
import os
import subprocess
import sys

import networkx as nx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import profiles  # noqa: E402

def feasible_single(types_sizes, evals, L, B):
    # rows sorted by |T|; e-values must satisfy B-|T|-L <= e <= B-|T| ; greedy matching on
    # intervals (each row is an interval of allowed e); classic interval assignment.
    rows = sorted(((B - t - L, B - t) for t in types_sizes), key=lambda iv: (iv[1], iv[0]))
    pool = sorted(evals)
    used = [False] * len(pool)
    for lo, hi in rows:
        pick = None
        for i, e in enumerate(pool):
            if not used[i] and lo <= e <= hi:
                pick = i
                break
        if pick is None:
            return False
        used[pick] = True
    return True


def main():
    mi, outdir = int(sys.argv[1]), sys.argv[2]
    N, k, q = (int(x) for x in sys.argv[3:6]) if len(sys.argv) >= 6 else (19, 8, 6)
    P0 = (4,) + (3,) * (q - 1)
    B = N - 1 - 2 * k  # row r meets 2k + |T(r)| + w(r) <= N-1 others
    assert sum(P0) == N and B >= 0
    P = profiles.enumerate_profiles(N, k, q)
    kmin = P["kappa_min"]
    ms = P["multisets"][mi]
    profs = [tuple(p) for p in ms["profiles"]]
    c0 = sum(1 for p in profs if p == P0)
    X = sorted([p for p in profs if p != P0],
               key=lambda p: (-(profiles.kappa(p) - kmin), [-x for x in p]))
    L = ms["zero_agreement_pairs"]
    wmin = sum(min(x - 3 for x in p) for p in X)
    tmax = min(c0, B - wmin)
    hmax = sum(sum(x for x in p if x <= 2) for p in X)
    evals = None
    if len(X) == 1:
        evals = [x - 3 for x in X[0] for _ in range(x)]
    graphs = subprocess.run(["/opt/homebrew/bin/geng", "-q", str(c0), "-D4"], capture_output=True,
                            text=True).stdout.split()
    reps = {}
    stats = {"graphs": len(graphs), "raw": 0, "after_rows": 0, "after_filter": 0}
    for g6 in graphs:
        G = nx.from_graph6_bytes(g6.encode())
        E = [tuple(sorted(e)) for e in G.edges()]
        deg0 = [G.degree(v) for v in range(c0)]
        covered = set(E)
        cands = []
        for s in range(3, tmax + 1):
            for S in itertools.combinations(range(c0), s):
                if all(deg0[v] < 4 for v in S) and not any(p in covered for p in itertools.combinations(S, 2)):
                    cands.append(S)

        def rec(start, chosen, deg, cov):
            yield list(chosen)
            if len(chosen) >= hmax:
                return
            for i in range(start, len(cands)):
                S = cands[i]
                if any(deg[v] >= 4 for v in S):
                    continue
                prs = list(itertools.combinations(S, 2))
                if any(p in cov for p in prs):
                    continue
                for v in S:
                    deg[v] += 1
                cov2 = cov | set(prs)
                chosen.append(S)
                yield from rec(i + 1, chosen, deg, cov2)
                chosen.pop()
                for v in S:
                    deg[v] -= 1

        for H in rec(0, [], deg0[:], set(covered)):
            stats["raw"] += 1
            deg = deg0[:]
            for S in H:
                for v in S:
                    deg[v] += 1
            priv = [4 - d for d in deg]
            nrows = len(E) + len(H) + sum(priv)
            empty = N - nrows
            if empty < 0:
                continue
            stats["after_rows"] += 1
            tsizes = [2] * len(E) + [len(S) for S in H] + [1] * sum(priv) + [0] * empty
            if evals is not None and not feasible_single(tsizes, evals, L, B):
                continue
            # leave lower bound: rows with |T| = t have l >= 2 - t - wmax(row); skip (SAT handles)
            stats["after_filter"] += 1
            Gi = nx.Graph()
            for v in range(c0):
                Gi.add_node(("v", v), kind="v")
            for j, e in enumerate(E):
                Gi.add_node(("e", j), kind="e2")
                Gi.add_edges_from((("e", j), ("v", v)) for v in e)
            for j, S in enumerate(H):
                Gi.add_node(("h", j), kind="h%d" % len(S))
                Gi.add_edges_from((("h", j), ("v", v)) for v in S)
            key = (len(E), tuple(sorted(len(S) for S in H)), tuple(sorted(deg)),
                   nx.weisfeiler_lehman_graph_hash(Gi, node_attr="kind", iterations=3))
            bucket = reps.setdefault(key, [])
            nm = lambda a, b: a["kind"] == b["kind"]  # noqa: E731
            if any(nx.is_isomorphic(Gi, R[0], node_match=nm) for R in bucket):
                continue
            bucket.append((Gi, {"edges": E, "hyper": [list(S) for S in H], "empty": empty}))
    skels = [d for b in reps.values() for _, d in b]
    os.makedirs(outdir, exist_ok=True)
    out = {"N": N, "k": k, "q": q, "multiset_index": mi, "profiles": [list(p) for p in profs], "c0": c0,
           "special": [list(p) for p in X], "L": L, "wmin": wmin, "tmax": tmax, "hmax": hmax,
           "stats": stats, "num_skeletons": len(skels), "skeletons": skels}
    json.dump(out, open(os.path.join(outdir, "skeletons-ms%02d.json" % mi), "w"))
    print(json.dumps({k: v for k, v in out.items() if k != "skeletons"}))


if __name__ == "__main__":
    main()
