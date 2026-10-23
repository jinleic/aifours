#!/usr/bin/env python3
"""[extend_p1q: generalization of extend_p1.py to q symbols with N = 3q+1, the P1 analogue
being (4,4,3,...,3,2); for q=6 identical behaviour. Written separately so that extend_p1.py,
which the running A3 batch calls, stays unchanged.]
Amendment A3: finer split of an A2 skeleton case whose special columns are all
P1 = (4,4,3,3,3,2). Enumerates every placement of the special columns' two size-4 blocks
(A, B) and the size-2 block (P), i.e. the 'full skeleton', subject only to necessary
conditions, then deduplicates up to isomorphism.

Necessary conditions used (all from validity, see README A3):
  * blocks of one column are disjoint; |A|=|B|=4, |P|=2;
  * two rows already agreeing (sharing a P0 quad or an earlier special block) are never put
    in a common block;
  * row budget: |T(r)| + w(r) <= 2 and >= 2 - L, w(r) = sum over special columns of e,
    e = +1 (A or B), 0 (triple), -1 (P); pruned with the bound that each remaining column
    changes w by at most +1 / at least -1.
Symmetry reduction during search (orbit representatives under row permutations that fix the
P0 skeleton and all choices made so far): within each class of rows with identical history,
only lowest-index rows are chosen. Both orders of the two size-4 blocks are enumerated. Final
deduplication by networkx isomorphism of colored incidence graphs (covers Aut of the P0
skeleton, swapping A/B, and permuting identical special columns).
Usage (research venv): extend_p1.py SPEC_JSON OUT_JSON
"""
import itertools
import json
import os
import sys

import networkx as nx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from encode_skel import rows_of  # noqa: E402



def main():
    spec = json.load(open(sys.argv[1]))
    c0, L, special = spec["c0"], spec["L"], spec["special"]
    N = spec.get("N", 19)
    q = (N - 1) // 3
    P1 = [4, 4] + [3] * (q - 3) + [2]
    assert all(list(p) == P1 for p in special)
    ns = len(special)
    m = int(sys.argv[3]) if len(sys.argv) > 3 else ns  # number of special columns to fix
    assert 1 <= m <= ns
    N = spec.get("N", 19)
    rows = rows_of(c0, spec["skeleton"], N)
    T = [len(t) for t in rows]
    agree0 = set()
    for v in range(c0):
        members = [r for r in range(N) if v in rows[r]]
        for a, b in itertools.combinations(members, 2):
            agree0.add((a, b))
    results = []

    def choose(avail_sorted, k, hist, agree):
        """k-subsets of avail rows, pairwise not agreeing, taking a prefix of each class of
        rows with identical history (orbit representatives)."""
        cls = {}
        for r in avail_sorted:
            cls.setdefault(hist[r], []).append(r)
        order = sorted(cls.values(), key=lambda rs: rs[0])

        def rec(ci, need, chosen):
            if need == 0:
                yield tuple(sorted(chosen))
                return
            if ci == len(order):
                return
            rs = order[ci]
            for take in range(min(need, len(rs)), -1, -1):
                pick = rs[:take]
                ok = all((min(a, b), max(a, b)) not in agree for a, b in itertools.combinations(pick, 2))
                ok = ok and all((min(a, b), max(a, b)) not in agree for a in pick for b in chosen)
                if ok:
                    yield from rec(ci + 1, need - take, chosen + pick)

        yield from rec(0, k, [])

    def budget_ok(w, cols_left):
        for r in range(N):
            if T[r] + w[r] - cols_left > 2:
                return False
            if T[r] + w[r] + cols_left < 2 - L:
                return False
        return True

    def col(ci, w, agree, hist, placed):
        if ci == m:
            if budget_ok(w, ns - m):
                results.append([[list(b) for b in p] for p in placed])
            return
        left = ns - ci - 1
        allr = list(range(N))
        candA = [r for r in allr if T[r] + w[r] + 1 - left <= 2]
        for A in choose(candA, 4, hist, agree):
            hA = list(hist)
            for r in A:
                hA[r] = hist[r] + ("A%d" % ci,)
            agA = set(agree) | {(a, b) for a, b in itertools.combinations(A, 2)}
            candB = [r for r in candA if r not in A]
            for B in choose(candB, 4, hA, agA):
                hB = list(hA)
                for r in B:
                    hB[r] = hA[r] + ("B%d" % ci,)
                agB = agA | {(a, b) for a, b in itertools.combinations(B, 2)}
                candP = [r for r in allr if r not in A and r not in B and T[r] + w[r] - 1 + left >= 2 - L]
                for P in choose(candP, 2, hB, agB):
                    w2 = list(w)
                    for r in A + B:
                        w2[r] += 1
                    for r in P:
                        w2[r] -= 1
                    if not budget_ok(w2, left):
                        continue
                    hP = list(hB)
                    for r in P:
                        hP[r] = hB[r] + ("P%d" % ci,)
                    for r in allr:
                        if r not in A and r not in B and r not in P:
                            hP[r] = hP[r] + ("T%d" % ci,)
                    agP = agB | {(min(P), max(P))}
                    col(ci + 1, w2, agP, tuple(hP), placed + [(A, B, P)])

    hist0 = tuple((rows[r],) for r in range(N))
    col(0, [0] * N, agree0, hist0, [])
    reps = {}
    nm = lambda a, b: a["kind"] == b["kind"]  # noqa: E731
    for pl in results:
        G = nx.Graph()
        for v in range(c0):
            G.add_node(("q", v), kind="P0quad")
        for r in range(N):
            G.add_node(("r", r), kind="row")
            for v in rows[r]:
                G.add_edge(("r", r), ("q", v))
        for ci, (A, B, P) in enumerate(pl):
            G.add_node(("c", ci), kind="P1col")
            for name, blk in (("A", A), ("B", B), ("P", P)):
                G.add_node((name, ci), kind="pair" if name == "P" else "squad")
                G.add_edge((name, ci), ("c", ci))
                for r in blk:
                    G.add_edge(("r", r), (name, ci))
        key = nx.weisfeiler_lehman_graph_hash(G, node_attr="kind", iterations=4)
        bucket = reps.setdefault(key, [])
        if any(nx.is_isomorphic(G, H, node_match=nm) for H, _ in bucket):
            continue
        bucket.append((G, pl))
    full = [pl for b in reps.values() for _, pl in b]
    json.dump({"source": os.path.basename(sys.argv[1]), "raw": len(results), "num_full": len(full),
               "full": full}, open(sys.argv[2], "w"))
    print(json.dumps({"source": os.path.basename(sys.argv[1]), "raw": len(results), "num_full": len(full)}))


if __name__ == "__main__":
    main()
