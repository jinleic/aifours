"""Symbolic-structure analysis of a 2q+1 solution (base resolutions JSON).
Classifies every block of S0, B1, B2 by G-orbit type:
  AAB_ij(w): G-orbit of {0_i, 1_i, w_j};  AAA_j; INF_within_j; INF_cross(chi);
and records, for B bases, the multiplier a in Q with B ∩ O = Z_q·(a·T), and for
S0 the translate class.  Output JSON (stdout summary)."""
import json
import sys
from collections import Counter, defaultdict


def main():
    q = int(sys.argv[1]); path = sys.argv[2]
    res = json.load(open(path))
    inf = 2 * q
    Q = sorted({(x * x) % q for x in range(1, q)})
    Qs = set(Q)
    chi = lambda x: 0 if x % q == 0 else (1 if x % q in Qs else -1)
    inv = lambda x: pow(x, q - 2, q)

    def pt(p):
        return ("inf", None) if p == inf else (p // q, p % q)

    def classify(b):
        pts = [pt(p) for p in b]
        if any(p[0] == "inf" for p in pts):
            fin = [p for p in pts if p[0] != "inf"]
            (i, x), (j, y) = fin
            if i == j:
                return ("INF_within", i), None
            d = (y - x) % q if i == 0 else (x - y) % q  # copy1 minus copy0
            return ("INF_cross", chi(d)), d
        layers = Counter(p[0] for p in pts)
        if len(layers) == 1:
            return ("AAA", pts[0][0]), None
        i = [l for l, c in layers.items() if c == 2][0]
        j = 1 - i
        (_, x), (_, y) = [p for p in pts if p[0] == i]
        (_, z) = [p for p in pts if p[0] == j][0]
        # normalize: map {x,y} -> {0,1} with multiplier in Q
        for (u, v) in ((x, y), (y, x)):
            a = (v - u) % q
            if a in Qs:
                w = ((z - u) * inv(a)) % q
                return ("AAB", i, j), (w, a, u)
        raise AssertionError
    out = {}
    for name, classes in zip(["S0", "B1", "B2"], res):
        blocks = [tuple(b) for C in classes for b in C]
        types = Counter()
        aab = defaultdict(set)
        cross = []
        for b in blocks:
            t, extra = classify(b)
            types[t] += 1
            if t[0] == "AAB":
                w, a, u = extra
                aab[(t[1], t[2], w)].add(a)
            if t[0] == "INF_cross":
                cross.append(extra)
        out[name] = {"types": {str(k): v for k, v in types.items()},
                     "AAB_orbits": sorted([(i, j, w, sorted(s)[:3], len(s)) for (i, j, w), s in aab.items()]),
                     "inf_cross_diffs": sorted(set(cross))[:5]}
    print(json.dumps({"q": q, "Q": Q}, separators=(",", ":")))
    for name in out:
        o = out[name]
        print(name, o["types"])
        ws01 = sorted(w for (i, j, w, _, _) in o["AAB_orbits"] if (i, j) == (0, 1))
        ws10 = sorted(w for (i, j, w, _, _) in o["AAB_orbits"] if (i, j) == (1, 0))
        print("  AAB01 w:", ws01)
        print("  AAB10 w:", ws10)
        if name != "S0":
            mult = {(i, j, w): s for (i, j, w, s, n) in o["AAB_orbits"]}
            print("  multipliers (first):", [(k, v[0]) for k, v in sorted(mult.items())][:12])
            print("  inf cross diffs:", o["inf_cross_diffs"])


if __name__ == "__main__":
    main()
