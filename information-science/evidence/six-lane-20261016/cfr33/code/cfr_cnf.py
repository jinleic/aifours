#!/usr/bin/env python3
"""CNF encoder for CFR(r,n) in normal form with optional multiplier / row-permutation relations (lane cfr33).

Usage: cfr_cnf.py SPEC.json OUT_PREFIX
Writes OUT_PREFIX.cnf (DIMACS) and OUT_PREFIX.map.json (mode 'x'; never overwrites).

Model (notes/facts-v1.md E1/E2/E3). Unknown position maps f_1..f_{r-1} of Z_n with f_j(0) = 0 (f_0 = id is implicit).
  X(j,x,v) <-> f_j(x) = v, for x != 0, v not in {0, x}.
  Each f_j is a bijection, f_j - id is a bijection, and for j < l, f_j - f_l is a bijection, with
  Y(j,l,x,d) <-> f_j(x) - f_l(x) = d (d != 0), defined by table clauses (both directions) + at-most-one.
SPEC keys:
  n, r                      : parameters (r >= 2).
  relations (optional)      : list of {"mu": unit mod n, "sigma": [sigma(1), ..., sigma(r-1)]} meaning
                              f_j(mu x) = mu f_{sigma(j)}(x) for all x, j.  Implemented by identifying variables
                              (union-find over X and Y keys); the restricted model is exactly the set of CFR normal
                              forms satisfying all relations.  {} / [] = unrestricted.
  units (optional)          : list of [j, x, v] forced true (planted controls).
  row_order_sb (optional)   : true -> f_1(1) < f_2(1) < ... < f_{r-1}(1) (integers 1..n-1).  Only allowed when every
                              relation has sigma = identity (then row permutations preserve the model).
Clauses are generated over keys, mapped to representative variables, literal-deduplicated; tautologies dropped.
"""
import hashlib, json, sys
from math import gcd


def main():
    spec_path, out = sys.argv[1], sys.argv[2]
    spec_bytes = open(spec_path, "rb").read()
    spec = json.loads(spec_bytes)
    n, r = int(spec["n"]), int(spec["r"])
    rels = spec.get("relations") or []
    m = r - 1
    J = list(range(1, m + 1))
    for rel in rels:
        assert gcd(int(rel["mu"]) % n, n) == 1, "mu must be a unit"
        assert sorted(rel["sigma"]) == J, "sigma must be a permutation of 1..r-1"
    parent = {}

    def find(k):
        root = k
        while parent.get(root, root) != root:
            root = parent[root]
        while parent.get(k, k) != root:
            nxt = parent[k]
            parent[k] = root
            k = nxt
        return root

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

    Xkeys = [(1, j, x, v) for j in J for x in range(1, n) for v in range(1, n) if v != x]
    Ykeys = [(2, j, l, x, d) for j in J for l in J if j < l for x in range(1, n) for d in range(1, n)]
    for rel in rels:
        mu = int(rel["mu"]) % n
        sg = {j: int(rel["sigma"][j - 1]) for j in J}
        for (_, j, x, v) in Xkeys:
            union((1, j, mu * x % n, mu * v % n), (1, sg[j], x, v))
        for (_, j, l, x, d) in Ykeys:
            a, b = sg[j], sg[l]
            if a < b:
                union((2, j, l, mu * x % n, mu * d % n), (2, a, b, x, d))
            else:
                union((2, j, l, mu * x % n, mu * d % n), (2, b, a, x, (-d) % n))
    var = {}
    nv = 0
    for k in Xkeys + Ykeys:
        rk = find(k)
        if rk not in var:
            nv += 1
            var[rk] = nv

    def X(j, x, v):
        return var[find((1, j, x % n, v % n))]

    def Y(j, l, x, d):
        return var[find((2, j, l, x % n, d % n))]

    clauses = set()
    stats = {"tautologies_dropped": 0}

    def add(lits):
        s = set(lits)
        if any(-a in s for a in s):
            stats["tautologies_dropped"] += 1
            return
        clauses.add(tuple(sorted(s, key=lambda z: (abs(z), z))))

    def exactly_one(lits):
        add(lits)
        for a in range(len(lits)):
            for b in range(a + 1, len(lits)):
                add([-lits[a], -lits[b]])

    def dom(x, v):
        return v % n != 0 and v % n != x % n

    for j in J:
        for x in range(1, n):
            exactly_one([X(j, x, v) for v in range(1, n) if v != x])
        for v in range(1, n):
            exactly_one([X(j, x, v) for x in range(1, n) if x != v])
        for d in range(1, n):
            exactly_one([X(j, x, x + d) for x in range(1, n) if (x + d) % n != 0])
    for j in J:
        for l in J:
            if not j < l:
                continue
            for x in range(1, n):
                for u in range(1, n):
                    if u == x:
                        continue
                    if dom(x, u):
                        add([-X(j, x, u), -X(l, x, u)])
                    for w in range(1, n):
                        if w == x or w == u:
                            continue
                        add([-X(j, x, u), -X(l, x, w), Y(j, l, x, u - w)])
                ys = [Y(j, l, x, d) for d in range(1, n)]
                exactly_one(ys)
                for d in range(1, n):
                    for u in range(1, n):
                        if u == x:
                            continue
                        w = (u - d) % n
                        if dom(x, w):
                            add([-Y(j, l, x, d), -X(j, x, u), X(l, x, w)])
                        else:
                            add([-Y(j, l, x, d), -X(j, x, u)])
                    for w in range(1, n):
                        if w == x:
                            continue
                        u = (w + d) % n
                        if dom(x, u):
                            add([-Y(j, l, x, d), -X(l, x, w), X(j, x, u)])
                        else:
                            add([-Y(j, l, x, d), -X(l, x, w)])
            for d in range(1, n):
                exactly_one([Y(j, l, x, d) for x in range(1, n)])
    for (j, x, v) in spec.get("units") or []:
        assert dom(x, v)
        add([X(j, x, v)])
    if spec.get("row_order_sb"):
        assert all(rel["sigma"] == J for rel in rels), "row_order_sb needs sigma = id in every relation"
        for j in J[:-1]:
            for a in range(2, n):
                for b in range(2, n):
                    if a >= b:
                        add([-X(j, 1, a), -X(j + 1, 1, b)])
    cl = sorted(clauses)
    lines = ["p cnf %d %d" % (nv, len(cl))] + [" ".join(map(str, c)) + " 0" for c in cl]
    text = "\n".join(lines) + "\n"
    with open(out + ".cnf", "x") as fh:
        fh.write(text)
    xmap = [[j, x, v, X(j, x, v)] for (_, j, x, v) in Xkeys]
    info = {"spec_sha256": hashlib.sha256(spec_bytes).hexdigest(), "spec": spec,
            "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(), "vars": nv, "clauses": len(cl),
            "x_vars_distinct": len({e[3] for e in xmap}), "stats": stats, "xmap": xmap,
            "encoder": "cfr_cnf.py v1"}
    with open(out + ".map.json", "x") as fh:
        json.dump(info, fh)
    print(json.dumps({k: info[k] for k in ("spec_sha256", "cnf_sha256", "vars", "clauses", "x_vars_distinct", "stats")}))


if __name__ == "__main__":
    main()
