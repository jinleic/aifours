#!/usr/bin/env python3
"""class_trade_search.py -- why the C2 mutation control uses a synthetic K_6 case (lane point-cyclic100).

For a certificate, tests whether the blocks of some 2 or 3 classes can be re-partitioned into the same number of
parallel classes in a different way (a "trade"; it would give a mutation that keeps the block set and every class
valid but can break only check C2). Exhaustive for every pair and every triple of classes:
  pairs: the conflict graph on the 2*(v/k) blocks (two blocks adjacent iff they share a point) is 2-colorable with
         the original colors; other re-partitions exist iff it has more than one connected component;
  triples: complete backtracking for a proper coloring with 3 colors (blocks through a common point get distinct
         colors) that is not a relabeling of the original one; no node limit.
Usage: class_trade_search.py CERT
"""
import itertools
import sys


def main(argv):
    lines = open(argv[1]).read().rstrip("\n").split("\n")[1:]
    byc = {}
    for line in lines:
        t = list(map(int, line.split()))
        byc.setdefault(t[0], []).append(tuple(t[1:]))
    cl = sorted(byc)
    split_pairs = 0
    for c1, c2 in itertools.combinations(cl, 2):
        blocks = byc[c1] + byc[c2]
        pt = {}
        for i, B in enumerate(blocks):
            for p in B:
                pt.setdefault(p, []).append(i)
        adj = {i: set() for i in range(len(blocks))}
        for lst in pt.values():
            for a in lst:
                adj[a].update(b for b in lst if b != a)
        seen, comps = set(), 0
        for i in range(len(blocks)):
            if i in seen:
                continue
            comps += 1
            st = [i]
            seen.add(i)
            while st:
                x = st.pop()
                for y in adj[x] - seen:
                    seen.add(y)
                    st.append(y)
        split_pairs += comps > 1
    print(f"pairs: {len(cl) * (len(cl) - 1) // 2} checked, {split_pairs} with a 2-class re-partition")

    total_nodes = 0
    found = 0
    for combo in itertools.combinations(cl, 3):
        blocks = [B for c in combo for B in byc[c]]
        orig = {B: k for k, c in enumerate(combo) for B in byc[c]}
        pt = {}
        for B in blocks:
            for p in B:
                pt.setdefault(p, []).append(B)
        nb = {B: {C for p in B for C in pt[p] if C != B} for B in blocks}
        order, seen = [], {blocks[0]}
        queue = [blocks[0]]
        while queue:
            B = queue.pop(0)
            order.append(B)
            for C in sorted(nb[B]):
                if C not in seen:
                    seen.add(C)
                    queue.append(C)
        color = {}
        hit = [False]
        nodes = [0]

        def rec(i):
            nodes[0] += 1
            if i == len(order):
                mp = {}
                for B in blocks:
                    if mp.setdefault(orig[B], color[B]) != color[B]:
                        hit[0] = True
                        return True
                return False
            B = order[i]
            for col in range(3):
                if i == 0 and col:
                    break
                if all(color.get(C) != col for C in nb[B]):
                    color[B] = col
                    if rec(i + 1):
                        return True
                    del color[B]
            return False

        rec(0)
        total_nodes += nodes[0]
        found += hit[0]
    print(f"triples: {len(cl) * (len(cl) - 1) * (len(cl) - 2) // 6} checked exhaustively "
          f"({total_nodes} search nodes), {found} with a 3-class re-partition")
    return 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    sys.exit(main(sys.argv))
