#!/usr/bin/env python3
"""README E10: definition-first checkers (standard library only) for the Construction 2.3 ingredients.

fg FG.json      1-FG(3, (K1, K), 16) of type 4^4 (Tan–Zhou lines 248–255): G partitions the 16
                points into 4 groups of 4; every pair lies in exactly one member of G ∪ B; every
                3-subset lies in exactly one member of G ∪ B ∪ T; |B| = 4 for B in B, |T| = 5 for T in T.
fdh CERT        FDGDD(3, 4, 5{8}) = FDH(5, 8, 4, 3) (lines 241–247): 5 groups of 8 partitioning the 40
                points; blocks are 4-subsets meeting every group at most once; every 3-subset
                meeting three groups lies in exactly one block; at EVERY point x the listed classes
                partition the derived design {B ∖ {x} : x ∈ B}, and each class is a parallel class of
                X ∖ (G_x ∪ G') for one group G' ≠ G_x (a Kirkman frame KF(8^4)).
Prints PASS/FAIL with the first failure; exit 0 on PASS, 1 on FAIL."""
import itertools
import json
import sys


class Fail(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Fail(msg)


def check_fg(path):
    d = json.load(open(path))
    G = [tuple(sorted(g)) for g in d["groups"]]
    B = [tuple(sorted(b)) for b in d["B"]]
    T = [tuple(sorted(t)) for t in d["T"]]
    pts = list(range(16))
    need(sorted(p for g in G for p in g) == pts and len(G) == 4 and all(len(g) == 4 for g in G),
         "GROUPS: not a partition of the 16 points into 4 groups of 4")
    need(all(len(b) == 4 for b in B), "B: a block of size != 4")
    need(all(len(t) == 5 for t in T), "T: a block of size != 5")
    need(all(len(set(m)) == len(m) and all(0 <= p < 16 for p in m) for m in G + B + T), "FORMAT: bad block")
    for pr in itertools.combinations(pts, 2):
        c = sum(1 for m in G + B if set(pr) <= set(m))
        need(c == 1, f"STEINER2: pair {pr} lies in {c} members of G ∪ B")
    for tr in itertools.combinations(pts, 3):
        c = sum(1 for m in G + B + T if set(tr) <= set(m))
        need(c == 1, f"STEINER3: triple {tr} lies in {c} members of G ∪ B ∪ T")
    return f"PASS 1-FG(3,({{4}},{{5}}),16) of type 4^4: |B|={len(B)} |T|={len(T)}"


def read_fdh(path):
    L = [l.split("#")[0].strip() for l in open(path)]
    L = [l for l in L if l]
    need(L[0] == "FDH 5 8", "HEADER: expected 'FDH 5 8'")
    need(L[1] == "GROUPS", "FORMAT: GROUPS")
    groups = [tuple(int(z) for z in L[2 + i].split()) for i in range(5)]
    need(L[7] == "BLOCKS", "FORMAT: BLOCKS")
    k = 8
    blocks = []
    while k < len(L) and not L[k].startswith("POINT"):
        blocks.append(tuple(int(z) for z in L[k].split()))
        k += 1
    col = {}
    cur = None
    while k < len(L):
        t = L[k].split()
        if t[0] == "POINT":
            cur = int(t[1])
            need(cur not in col, f"FORMAT: POINT {cur} twice")
            col[cur] = []
        elif t[0] == "CLASS":
            need(int(t[1]) == len(col[cur]), f"FORMAT: class id out of order at POINT {cur}")
            col[cur].append([])
        else:
            col[cur][-1].append(tuple(int(z) for z in t))
        k += 1
    return groups, blocks, col


def check_fdh(path):
    groups, blocks, col = read_fdh(path)
    pts = list(range(40))
    need(sorted(p for g in groups for p in g) == pts and all(len(g) == 8 for g in groups),
         "GROUPS: not a partition of 40 points into 5 groups of 8")
    gof = {p: i for i, g in enumerate(groups) for p in g}
    need(len(set(map(lambda b: tuple(sorted(b)), blocks))) == len(blocks), "BLOCK: repeated block")
    for b in blocks:
        need(len(b) == 4 and len(set(b)) == 4 and all(0 <= p < 40 for p in b), f"BLOCK: bad block {b}")
        need(len({gof[p] for p in b}) == 4, f"BLOCK: {b} meets a group twice")
    cover = {}
    for b in blocks:
        for t in itertools.combinations(sorted(b), 3):
            cover[t] = cover.get(t, 0) + 1
    universe = [t for t in itertools.combinations(pts, 3) if len({gof[p] for p in t}) == 3]
    need(all(cover.get(t, 0) == 1 for t in universe) and len(cover) == len(universe),
         "COVERAGE: some transverse triple is not in exactly one block")
    need(sorted(col) == pts, "COMPLETENESS: POINT sections missing")
    for x in pts:
        der = sorted(tuple(sorted(p for p in b if p != x)) for b in blocks if x in b)
        listed = sorted(tuple(sorted(t)) for C in col[x] for t in C)
        need(listed == der, f"FRAME: POINT {x}: classes do not partition the derived design")
        miss = []
        for C in col[x]:
            need(C, f"FRAME: POINT {x}: empty class")
            ps = [p for t in C for p in t]
            need(len(ps) == len(set(ps)), f"FRAME: POINT {x}: class not a partial parallel class")
            gs = {gof[p] for p in ps}
            need(gof[x] not in gs, f"FRAME: POINT {x}: class meets the group of x")
            need(len(gs) == 3, f"FRAME: POINT {x}: class does not miss exactly one other group")
            gm = ({0, 1, 2, 3, 4} - gs - {gof[x]}).pop()
            need(set(ps) == {p for p in pts if gof[p] not in (gof[x], gm)},
                 f"FRAME: POINT {x}: class is not a parallel class of X minus two groups")
            miss.append(gm)
    return f"PASS FDH(5,8,4,3): {len(blocks)} blocks, Kirkman frames at all 40 points"


def main():
    kind, path = sys.argv[1], sys.argv[2]
    try:
        print({"fg": check_fg, "fdh": check_fdh}[kind](path))
        return 0
    except Fail as e:
        print("FAIL", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
