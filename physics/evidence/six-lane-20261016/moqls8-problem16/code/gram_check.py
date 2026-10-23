"""Direct evaluator of the Gram-pattern conditions G1-G4 (+P4) of gram_a.py, independent of any CNF, plus exact Gram
patterns of genuine configurations used as positive controls:
  - order 8: the Theorem-6 pair over Z2 x Z4 (Psi^(f), Phi^(u)) as two "quantum" squares;
  - order 7: the Corollary-7 pair (Psi^(f0), classical slope-4 square) as two "quantum" squares.
python -B gram_check.py --emit 8 --out pairs8.json   (writes {"1": [[p,q],...], "2": [...]})
python -B gram_check.py --check pairs8.json --order 8 [--p4 1]
"""
from __future__ import annotations

import argparse
import itertools
import json


def lines_rc(N):
    return [[(i, j) for j in range(N)] for i in range(N)] + [[(i, j) for i in range(N)] for j in range(N)]


def evaluate(N, G, p4=()):
    """G: {s: set of frozenset({p,q})} nonzero overlaps. Returns list of violations (rows/columns only)."""
    cells = [(i, j) for i in range(N) for j in range(N)]
    bad = []

    def g(s, p, q):
        return p == q or frozenset((p, q)) in G[s]
    for s in G:
        for e in G[s]:
            p, q = tuple(e)
            if p[0] == q[0] or p[1] == q[1]:
                bad.append("G1 %s %s %s" % (s, p, q))
    for s, u in itertools.combinations(sorted(G), 2):
        for e in G[s] & G[u]:
            bad.append("G2 %s %s %s" % (s, u, tuple(e)))
    L = lines_rc(N)
    for s in G:
        for l1, l2 in itertools.combinations(L, 2):
            M = [[g(s, a, b) for b in l2] for a in l1]
            if not all(any(row) for row in M) or not all(any(M[k][r] for k in range(N)) for r in range(N)):
                bad.append("G3 empty %s" % s)
            for r1, r2 in itertools.combinations(range(N), 2):
                if sum(M[r1][k] and M[r2][k] for k in range(N)) == 1 or \
                        sum(M[k][r1] and M[k][r2] for k in range(N)) == 1:
                    bad.append("G3 one %s" % s)
        for l in L:
            rest = [c for c in cells if c not in set(l)]
            for p, q in itertools.combinations(rest, 2):
                I = sum(g(s, a, p) and g(s, a, q) for a in l)
                if I == 1 and not g(s, p, q):
                    bad.append("G4 one %s %s %s" % (s, p, q))
                if I == 0 and g(s, p, q):
                    bad.append("G4 zero %s %s %s" % (s, p, q))
    for s in G:                                  # G5 same ray
        for l in L:
            ls = set(l)
            for q in cells:
                if q in ls:
                    continue
                sup = [a for a in l if g(s, a, q)]
                if len(sup) == 1:
                    a = sup[0]
                    for p in cells:
                        if p not in (q, a) and g(s, p, q) != g(s, p, a):
                            bad.append("G5 %s %s %s %s" % (s, q, a, p))
    for s in p4:
        if not any(sum(g(s, (0, j), p) for j in range(N)) >= 3 for p in cells if p[0] != 0):
            bad.append("P4 %s" % s)
    return bad


def pairs8():
    dec = lambda e: (e >> 2, e & 3)
    enc = lambda a, b: ((a % 2) << 2) | (b % 4)
    add = lambda x, y: enc(dec(x)[0] + dec(y)[0], dec(x)[1] + dec(y)[1])
    mul = lambda x, y: enc(dec(x)[0] * dec(y)[0], dec(x)[1] * dec(y)[1])
    f = [0, 2, 4, 6, 1, 7, 5, 3]
    u = enc(1, 1)

    def chi(x):
        a, b = dec(x)
        re, im = [(1, 0), (0, 1), (-1, 0), (0, -1)][b]
        return (-re, -im) if a else (re, im)
    vec = {(i, j): [chi(add(mul(i, f[x]), mul(j, x))) for x in range(8)] for i in range(8) for j in range(8)}

    def nz(v, w):
        re = sum(p[0] * q[0] + p[1] * q[1] for p, q in zip(v, w))
        im = sum(p[0] * q[1] - p[1] * q[0] for p, q in zip(v, w))
        return (re, im) != (0, 0)
    cells = list(vec)
    g1 = [[p, q] for p, q in itertools.combinations(sorted(cells), 2) if nz(vec[p], vec[q])]
    phi = {c: add(mul(u, c[0]), c[1]) for c in cells}
    g2 = [[p, q] for p, q in itertools.combinations(sorted(cells), 2) if phi[p] == phi[q]]
    return {"1": g1, "2": g2}


def pairs7():
    H = {1, 2, 4}
    f = [x if x in H else 0 for x in range(7)]
    perm = lambda seq: sorted(v % 7 for v in seq) == list(range(7))
    M = [m for m in range(7) if perm([f[x] - m * x for x in range(7)])]
    f0 = [(f[x] - M[0] * x) % 7 for x in range(7)]
    sl = (M[1] - M[0]) % 7
    e = {(i, j): [(i * f0[x] + j * x) % 7 for x in range(7)] for i in range(7) for j in range(7)}
    cells = sorted(e)
    g1 = [[p, q] for p, q in itertools.combinations(cells, 2) if not perm([e[q][x] - e[p][x] for x in range(7)])]
    g2 = [[p, q] for p, q in itertools.combinations(cells, 2) if (p[1] + sl * p[0]) % 7 == (q[1] + sl * q[0]) % 7]
    return {"1": g1, "2": g2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", type=int, choices=[7, 8])
    ap.add_argument("--out")
    ap.add_argument("--check")
    ap.add_argument("--order", type=int)
    ap.add_argument("--p4", default="")
    a = ap.parse_args()
    if a.emit:
        d = pairs8() if a.emit == 8 else pairs7()
        with open(a.out, "x") as fh:
            json.dump(d, fh)
        print(json.dumps({k: len(v) for k, v in d.items()}))
        return
    d = json.load(open(a.check))
    G = {int(k): {frozenset((tuple(p), tuple(q))) for p, q in v} for k, v in d.items()}
    bad = evaluate(a.order, G, tuple(int(ch) for ch in a.p4))
    print(json.dumps({"violations": len(bad), "first": bad[:5]}))
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
