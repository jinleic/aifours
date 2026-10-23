"""Cyclotomic-class statistics of 2q+1 packages (pattern data for an ansatz).

For each base and each two-copy orbit AAB_ij(w) it uses, record the classes of
w, w−1 (index 2 and 6 cyclotomy w.r.t. a fixed primitive root), of the
multiplier a (B bases) or of the translate b (S), and of y = a·w.
Usage: cyclo_stats.py q base_resolutions.json
"""
import json
import sys
from collections import Counter



def prim_root(q):
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in {p for p in range(2, q) if (q - 1) % p == 0 and all(p % r for r in range(2, int(p ** 0.5) + 1))}):
            return g


def main():
    q = int(sys.argv[1]); res = json.load(open(sys.argv[2]))
    g = prim_root(q)
    dlog = {pow(g, k, q): k for k in range(q - 1)}
    cls = lambda x, e: None if x % q == 0 else dlog[x % q] % e
    Qs = {x for x in dlog if dlog[x] % 2 == 0}
    inv = lambda x: pow(x, q - 2, q)
    inf = 2 * q
    def pt(p): return ("inf", None) if p == inf else (p // q, p % q)
    summary = {}
    for name, classes in zip(["S0", "B1", "B2"], res):
        blocks = {tuple(b) for C in classes for b in C}
        recs = []
        for b in blocks:
            pts = [pt(p) for p in b]
            if any(p[0] == "inf" for p in pts):
                continue
            layers = Counter(p[0] for p in pts)
            if len(layers) != 2:
                continue
            i = [l for l, c in layers.items() if c == 2][0]
            (_, x), (_, y2) = [p for p in pts if p[0] == i]
            (_, z) = [p for p in pts if p[0] != i][0]
            for (u, vv) in ((x, y2), (y2, x)):
                a = (vv - u) % q
                if a in Qs:
                    w = ((z - u) * inv(a)) % q
                    recs.append((i, w, a, u))
                    break
        # one record per orbit: canonical representative = minimal (a, u) for B (translation orbit -> fixed a)
        orb = {}
        for i, w, a, u in recs:
            key = (i, w)
            orb.setdefault(key, set()).add(a)
        rows = []
        for (i, w), aset in sorted(orb.items()):
            if name == "S0":
                rows.append((i, w, cls(w, 2), cls(w - 1, 2), cls(w, 6), cls(w - 1, 6)))
            else:
                assert len(aset) == 1
                a = next(iter(aset))
                rows.append((i, w, cls(w, 2), cls(w - 1, 2), cls(w, 6), cls(w - 1, 6), cls(a, 6), cls(a * w, 6)))
        summary[name] = rows
        c2 = Counter((r[0], r[2], r[3]) for r in rows)
        print(name, "orbits", len(rows), "by (copy-with-pair, chi(w) class, chi(w-1) class):", dict(sorted(c2.items(), key=str)))
        if name != "S0":
            c6 = Counter((r[0], r[6]) for r in rows)
            print("   multiplier a index-6 class by type:", dict(sorted(c6.items(), key=str)))
    json.dump({"q": q, "g": g, "rows": summary}, open(sys.argv[2].replace(".json", f".cyclo.json"), "w"))


if __name__ == "__main__":
    main()
