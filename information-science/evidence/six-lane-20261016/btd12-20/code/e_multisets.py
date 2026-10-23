#!/usr/bin/env python3
"""e_multisets.py -- enumerate multisets of e7 / e8 tetrads (README 1.4(a), structure route; exploratory).

e7: the 7 complements of the lines of the Fano plane on points 0..6 (lines 012 034 056 135 146 236 245).
e8: the 14 affine planes of AG(3,2) on points 0..7 (point = 3-bit vector; plane = {x : <a,x> = b}, a != 0).
A multiset is a vector m of multiplicities (one per tetrad) with total r in [1, 12]; it is kept when every point
has degree sum_{T ni p} m_T in {0, 2, 4, 6}.  Multisets are reduced modulo the full automorphism group of the tetrad
set (all point permutations mapping the tetrad set to itself, found by brute force): the first member of each orbit
met by the search marks its whole orbit as seen, and the orbit's lexicographically smallest member is recorded.
Writes OUT.json (exclusive): group orders, tetrads, and the canonical multisets with their degrees.
Usage: e_multisets.py OUT.json     (stdlib only)
"""
import itertools
import json
import sys

FANO = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5)]


def e7_tetrads():
    return [tuple(sorted(set(range(7)) - set(L))) for L in FANO]


def e8_tetrads():
    out = []
    for a in range(1, 8):
        for b in (0, 1):
            out.append(tuple(x for x in range(8) if bin(a & x).count("1") % 2 == b))
    return out


def group_on_tetrads(npts, tets):
    idx = {frozenset(t): i for i, t in enumerate(tets)}
    perms = []
    for p in itertools.permutations(range(npts)):
        img = []
        for t in tets:
            q = frozenset(p[x] for x in t)
            if q not in idx:
                break
            img.append(idx[q])
        else:
            perms.append(tuple(img))
    return perms


def enumerate_multisets(npts, tets, G):
    nt = len(tets)
    inc = [[1 if p in t else 0 for p in range(npts)] for t in tets]
    res = {}
    seen = set()
    m = [0] * nt
    deg = [0] * npts

    def rec(t, total):
        if t == nt:
            if total >= 1 and all(d in (0, 2, 4, 6) for d in deg):
                cur = tuple(m)
                if cur not in seen:
                    orbit = {tuple(m[g[s]] for s in range(nt)) for g in G}
                    seen.update(orbit)
                    res[min(orbit)] = None
            return
        mult = 0
        while True:
            rec(t + 1, total + mult)
            if total + mult + 1 > 12 or any(deg[p] + inc[t][p] > 6 for p in range(npts)):
                break
            mult += 1
            m[t] = mult
            for p in range(npts):
                deg[p] += inc[t][p]
        for p in range(npts):
            deg[p] -= inc[t][p] * mult
        m[t] = 0

    rec(0, 0)
    out = []
    for key in sorted(res):
        d = [sum(key[s] * inc[s][p] for s in range(nt)) for p in range(npts)]
        out.append({"mult": list(key), "rows": sum(key), "degrees": d, "support": sum(1 for x in d if x)})
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    data = {}
    for name, npts, tets in (("e7", 7, e7_tetrads()), ("e8", 8, e8_tetrads())):
        G = group_on_tetrads(npts, tets)
        # G acts on multiplicity vectors by m -> (m[g[0]], ..., m[g[nt-1]]); it is a group, so the minimum over the
        # orbit is a canonical form.
        ms = enumerate_multisets(npts, tets, G)
        data[name] = {"points": npts, "tetrads": [list(t) for t in tets], "group_order": len(G), "multisets": ms}
        print(name, "group", len(G), "canonical multisets", len(ms), file=sys.stderr)
    with open(argv[1], "x") as f:
        json.dump(data, f)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
