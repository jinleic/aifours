#!/usr/bin/env python3
"""gram_encB.py: independent Gram-support CNF encoder B (stdlib only). Lane moqls7-maximum.

Same mathematics as gram_enc.py (review/GRAM-ENCODING), written separately with different auxiliary structure:
for every square a, line l and unordered pair {p,q} of points off l, a 2-bit "at most one / at least one" summary
of the products m_r = g(p,r) g(q,r) (r on l) is built with a sequential counter:
   s1 (at least one product), s2 (at least two products);
   then: not s1 -> not g(p,q);  s1 and not s2 -> g(p,q)   (for collinear p,q: s1 -> s2).
Transition patterns (G3): for every ordered pair of lines (l1,l2) and point r on l1 off l2 the neighbour count on
l2 is summarised the same way (c1: >= 1, c2: >= 2); c1 is required, and (not c2) together with g(r,q) forbids every
other neighbour of q on l1. Heavy (G4): a sequential counter "at least 3" per (point, line).
Inputs as gram_enc.py. Usage: gram_encB.py --squares S [--net-L LJSON] [--heavy] [--sym] [--fix-json F] --out F.cnf
"""
import argparse
import itertools
import json

N = 7
PTS = [(r, c) for r in range(N) for c in range(N)]


class Builder:
    def __init__(self):
        self.n = 0
        self.clauses = []

    def var(self):
        self.n += 1
        return self.n

    def clause(self, *lits):
        self.clauses.append(lits)

    def dump(self, path):
        with open(path, "w") as f:
            f.write("p cnf %d %d\n" % (self.n, len(self.clauses)))
            for c in self.clauses:
                f.write(" ".join(map(str, c)) + " 0\n")


def counter2(B, items):
    """items: list of literals. Returns (s1, s2) with s1 <-> (>=1 true), s2 <-> (>=2 true), via a sequential
    counter (full equivalences)."""
    if not items:
        return None, None
    a1, a2 = items[0], None          # a1: >=1 among prefix, a2: >=2 among prefix (None = false)
    for x in items[1:]:
        n1, n2 = B.var(), B.var()
        # n1 <-> a1 or x
        B.clause(-n1, a1, x); B.clause(n1, -a1); B.clause(n1, -x)
        # n2 <-> a2 or (a1 and x)
        if a2 is None:
            B.clause(-n2, a1); B.clause(-n2, x); B.clause(n2, -a1, -x)
        else:
            B.clause(-n2, a2, a1); B.clause(-n2, a2, x); B.clause(n2, -a2); B.clause(n2, -a1, -x)
        a1, a2 = n1, n2
    return a1, a2


def counter_ge3(B, items):
    """Return literal t with t -> (>= 3 of items true) (one direction suffices for 'required' use)."""
    t = B.var()
    if len(items) < 3:
        B.clause(-t)
        return t
    # c[i][k]: among first i items at least k true (k = 1..3); one-directional (c -> condition) is enough
    prev = {1: None, 2: None, 3: None}
    for i, x in enumerate(items):
        cur = {}
        for k in (1, 2, 3):
            v = B.var()
            cur[k] = v
            # v -> prev[k] or (x and prev[k-1])
            lower = prev[k - 1] if k > 1 else "T"
            if prev[k] is None and lower == "T":
                B.clause(-v, x)
            elif prev[k] is None and lower is None:
                B.clause(-v)
            elif prev[k] is None:
                B.clause(-v, x); B.clause(-v, lower)
            elif lower == "T":
                B.clause(-v, prev[k], x)
            elif lower is None:
                B.clause(-v, prev[k])
            else:
                B.clause(-v, prev[k], x); B.clause(-v, prev[k], lower)
        prev = cur
    B.clause(-t, prev[3])
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--squares", type=int, default=3)
    ap.add_argument("--net-L", default=None)
    ap.add_argument("--heavy", action="store_true")
    ap.add_argument("--sym", action="store_true")
    ap.add_argument("--fix-json", default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    L = json.load(open(a.net_L)) if a.net_L else None
    lines = [[(r, c) for c in range(N)] for r in range(N)] + [[(r, c) for r in range(N)] for c in range(N)]
    if L is not None:
        lines += [[pt for pt in PTS if L[pt[0]][pt[1]] == s] for s in range(N)]
    same_line = set()
    for l in lines:
        for p in l:
            for q in l:
                if p != q:
                    same_line.add((p, q))
    B = Builder()
    sq = list(range(1, a.squares + 1))
    gv = {}
    for s in sq:
        for i, p in enumerate(PTS):
            for q in PTS[i + 1:]:
                if (p, q) not in same_line:
                    gv[(s, p, q)] = B.var()

    def g(s, p, q):
        if p > q:
            p, q = q, p
        return gv.get((s, p, q))
    prod = {}

    def m(s, p, q, r):
        x, y = g(s, p, r), g(s, q, r)
        if x is None or y is None:
            return None
        key = (s, min(p, q), max(p, q), r)
        if key not in prod:
            v = B.var()
            prod[key] = v
            B.clause(-v, x); B.clause(-v, y); B.clause(v, -x, -y)
        return prod[key]
    for s in sq:
        for l in lines:
            on = set(l)
            off = [p for p in PTS if p not in on]
            for i, p in enumerate(off):
                for q in off[i + 1:]:
                    items = [m(s, p, q, r) for r in l]
                    items = [x for x in items if x is not None]
                    s1, s2 = counter2(B, items)
                    gpq = g(s, p, q)
                    if s1 is None:
                        if gpq is not None:
                            B.clause(-gpq)
                        continue
                    if gpq is None:
                        B.clause(-s1, s2)              # never exactly one common neighbour
                    else:
                        B.clause(s1, -gpq)             # none -> orthogonal
                        if s2 is None:
                            B.clause(-s1, gpq)
                        else:
                            B.clause(-s1, s2, gpq)     # exactly one -> not orthogonal
        for l1 in lines:
            for l2 in lines:
                if l1 is l2:
                    continue
                o1, o2 = set(l1), set(l2)
                for r in l1:
                    if r in o2:
                        continue
                    nb = [(q, g(s, r, q)) for q in l2 if q not in o1 and g(s, r, q) is not None]
                    lits = [v for _, v in nb]
                    if not lits:
                        B.clause()
                        continue
                    c1, c2 = counter2(B, lits)
                    B.clause(c1)
                    for q, v in nb:
                        for r2 in l1:
                            if r2 == r or r2 in o2:
                                continue
                            w = g(s, r2, q)
                            if w is None:
                                continue
                            if c2 is None:
                                B.clause(-v, -w)
                            else:
                                B.clause(c2, -v, -w)
    for s, t in itertools.combinations(sq, 2):
        for (s0, p, q), v in list(gv.items()):
            if s0 == s:
                B.clause(-v, -gv[(t, p, q)])
    if a.heavy:
        for s in sq:
            for li, l in enumerate(lines):
                if a.sym and s == 1 and li == 0:
                    for r in [(0, 1), (0, 2), (0, 3)]:
                        B.clause(g(1, (1, 0), r))
                    continue
                on = set(l)
                opts = []
                for p in PTS:
                    if p in on:
                        continue
                    items = [g(s, p, r) for r in l if g(s, p, r) is not None]
                    opts.append(counter_ge3(B, items))
                B.clause(*opts)
    if a.fix_json:
        fix = json.load(open(a.fix_json))
        for s in sq:
            key = "g%d" % s
            if key not in fix:
                continue
            ones = set()
            for e in fix[key]:
                p, q = tuple(e[0]), tuple(e[1])
                ones.add((min(p, q), max(p, q)))
            for (s0, p, q), v in gv.items():
                if s0 == s:
                    B.clause(v if (p, q) in ones else -v)
    B.dump(a.out)
    print("vars", B.n, "clauses", len(B.clauses))


if __name__ == "__main__":
    main()
