#!/usr/bin/env python3
"""Independent cross-check for dmorbit_dfs_v1 (lane cfr33/cfr27, worker InfoCFR27Lift, README section 5.1(a)).

Usage: dmorbit_xcheck_v1.py SPEC.json [MAXSOL]
Different algorithm from the C solver: (1) the group is closed here from the spec generators (own code);
(2) EVERY G-orbit of normalised columns (entry 0 = 0) is materialised as a set by brute force over Z_n^(k-1);
(3) solutions are exact covers of the items (row pair, value) over ALL row pairs (not only representatives), using
whole orbits as options, with the zero column forced if the spec has a zero orbit and the multiset of orbit sizes
required to equal the spec's; search = choose the uncovered item with fewest compatible orbits (Knuth's MRV).
Counts sets of orbits (each solution once). Prints 'XCHECK COUNT <c>' and a sha256 of the sorted solution list,
where a solution is written as the sorted list of its orbits' lexicographically minimal normalised columns.
Pure Python; intended for n <= 21 (n = 25/27 orbit materialisation is slow).
"""
import hashlib, itertools, json, sys
from collections import Counter


def main():
    spec = json.load(open(sys.argv[1]))
    maxsol = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    n, k = spec["n"], spec["k"]
    gens = [(g[0] % n, tuple(g[1])) for g in spec["gens"]]
    # group closure: element = (mu, perm) acting on column c by (s c)_i = mu * c_{perm^-1(i)}
    def act(g, c):
        mu, p = g
        out = [0] * k
        for i in range(k):
            out[p[i]] = (mu * c[i]) % n   # row i's entry moves to row p[i]
        base = out[0]
        return tuple((x - base) % n for x in out)
    ident = (1, tuple(range(k)))
    G = {ident}
    frontier = [ident]
    def mul(a, b):  # a after b
        return ((a[0] * b[0]) % n, tuple(a[1][b[1][i]] for i in range(k)))
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mul(g, x)
                if y not in G:
                    G.add(y)
                    new.append(y)
        frontier = new
    G = sorted(G)
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    pidx = {p: t for t, p in enumerate(pairs)}
    # all orbits of normalised columns
    seen = set()
    orbits = []
    for tail in itertools.product(range(n), repeat=k - 1):
        c = (0,) + tail
        if c in seen:
            continue
        orb = frozenset(act(g, c) for g in G)
        seen |= orb
        cols = sorted(orb)
        # coverage over ALL pairs; reject orbits with an internal repeat
        items = []
        ok = True
        for (i, j) in pairs:
            vals = [(col[i] - col[j]) % n for col in cols]
            if len(set(vals)) != len(vals):
                ok = False
                break
            items.extend((pidx[(i, j)], v) for v in vals)
        if ok:
            orbits.append((cols[0], len(cols), frozenset(items)))
    want = Counter()
    zero_needed = False
    for o in spec["orbits"]:
        # orbit size = |G| / |stab|: recompute stabiliser order from the spec's stabiliser generators
        S = {ident}
        fr = [ident]
        sg = [(g[0] % n, tuple(g[1])) for g in o.get("stab", [])]
        while fr:
            nw = []
            for x in fr:
                for g in sg:
                    y = mul(g, x)
                    if y not in S:
                        S.add(y)
                        nw.append(y)
            fr = nw
        size = len(G) // len(S)
        if o.get("zero"):
            zero_needed = True
        else:
            want[size] += o["count"]
    zero_col = tuple([0] * k)
    zero_orbit = [ob for ob in orbits if ob[0] == zero_col]
    items_all = [(t, v) for t in range(len(pairs)) for v in range(n)]
    sols = []
    covered0 = set()
    chosen0 = []
    if zero_needed:
        assert len(zero_orbit) == 1 and zero_orbit[0][1] == 1
        covered0 = set(zero_orbit[0][2])
        chosen0 = [zero_orbit[0][0]]
    cand = [ob for ob in orbits if ob[0] != zero_col and ob[1] in want]
    by_item = {it: [] for it in items_all}
    for idx, ob in enumerate(cand):
        for it in ob[2]:
            by_item[it].append(idx)
    sys.setrecursionlimit(10000)

    def rec(covered, chosen, need):
        if len(sols) >= maxsol:
            return
        if len(covered) == len(items_all):
            if sum(need.values()) == 0:
                sols.append(tuple(sorted(chosen)))
            return
        best, bestl = None, None
        for it in items_all:
            if it in covered:
                continue
            l = [i for i in by_item[it] if need[cand[i][1]] > 0 and not (cand[i][2] & covered)]
            if best is None or len(l) < len(bestl):
                best, bestl = it, l
                if not l:
                    return
        for i in bestl:
            ob = cand[i]
            need[ob[1]] -= 1
            rec(covered | ob[2], chosen + [ob[0]], need)
            need[ob[1]] += 1

    rec(frozenset(covered0), chosen0, Counter(want))
    text = "\n".join(" ".join(",".join(map(str, c)) for c in s) for s in sorted(sols))
    print("XCHECK group_order %d orbits_valid %d candidates %d" % (len(G), len(orbits), len(cand)))
    print("XCHECK COUNT %d%s sha256 %s" % (len(sols), " (capped)" if len(sols) >= maxsol else "", hashlib.sha256(text.encode()).hexdigest()))


if __name__ == "__main__":
    main()
