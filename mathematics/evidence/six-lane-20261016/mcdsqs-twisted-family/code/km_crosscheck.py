#!/usr/bin/env python3
"""Independent cross-check of Kramer–Mesner (un)satisfiability (standard library only; no code
shared with mcdsqs_lib.py): canonical orbit forms over the explicit group {x -> m*x+b}, rows
from orbit sizes, and exhaustive exact-cover enumeration (Algorithm X).
Usage: km_crosscheck.py V GEN [MAXSOL]   -> prints #columns, #valid rows, #solutions (capped)."""
import sys
from itertools import combinations


def main():
    v, gen = int(sys.argv[1]), int(sys.argv[2])
    maxsol = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
    mults, x = [1], gen % v
    while x != 1:
        mults.append(x)
        x = x * gen % v
    G = [(m, b) for m in mults for b in range(v)]

    def canon(s):
        return min(tuple(sorted((m * p + b) % v for p in s)) for m, b in G)

    def orbit(s):
        return {tuple(sorted((m * p + b) % v for p in s)) for m, b in G}

    tsize = {}
    for t in combinations(range(v), 3):
        c = canon(t)
        if c not in tsize:
            tsize[c] = len(orbit(c))
    assert sum(tsize.values()) == v * (v - 1) * (v - 2) // 6
    rows, seen = [], set()
    for rest in combinations(range(1, v), 3):
        q = (0,) + rest
        c = canon(q)
        if c in seen:
            continue
        seen.add(c)
        osz = len(orbit(c))
        cnt = {}
        for t in combinations(c, 3):
            ct = canon(t)
            cnt[ct] = cnt.get(ct, 0) + 1
        if all(osz * k == tsize[ct] for ct, k in cnt.items()):
            rows.append((c, frozenset(cnt)))
    cols = set(tsize)
    # Algorithm X
    bycol = {c: [i for i, (_, s) in enumerate(rows) if c in s] for c in cols}
    sols = []

    def search(active, chosen):
        if len(sols) >= maxsol:
            return
        if not active:
            sols.append(list(chosen))
            return
        c = min(active, key=lambda c: sum(1 for i in bycol[c] if rows[i][1] <= active))
        for i in bycol[c]:
            s = rows[i][1]
            if s <= active:
                chosen.append(i)
                search(active - s, chosen)
                chosen.pop()

    search(frozenset(cols), [])
    print(f"v={v} gen={gen} |G|={len(G)} columns={len(cols)} valid_rows={len(rows)} "
          f"solutions={len(sols)}{' (capped)' if len(sols) >= maxsol else ' (exhaustive)'}")


if __name__ == "__main__":
    main()
