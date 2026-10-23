#!/usr/bin/env python3
"""t2_sat.py -- representation R1c (README Section 2.2): CNF encoding of the T2 type of GENERAL-REDUCTION.md for
v = 4q, q odd, q = 1 (mod 12) (t = q, K = {1^((q-1)/12)}), for kissat; and the decoder of a model into a PC-SEED.

CRT coordinates: x in Z_v <-> (x mod 4, x mod q) ("height", "residue"). With A = (q-1)/4 X blocks and C = (q-1)/12 Y
blocks:
  xb(r,b)   residue r (1..q-1) lies in X block b (0..A-1)                 exactly one b per r, exactly 4 r per b
  xh(r,h)   residue r has height h (0..3)                                 exactly one h per r
  ys(j,h,s) Y block j (0..C-1) has its height-h point at residue s        exactly one s per (j,h)
  same(r1,r2), hd(r1,r2,d) (r1 < r2): same X block; h(r2) - h(r1) = d (mod 4)
  cx(class,r): the unordered X pair {r, r+e} covers the +-class;  yd(j,h1,h2,e): s(j,h2) - s(j,h1) = e.
Difference classes: (delta, e) ~ (-delta, -e), canonical e in 1..(q-1)/2, delta in Z_4 (2(q-1) classes). Every class is
covered exactly once (the X candidates and the Y candidates of the class); yd(.,.,.,0) is forbidden (short difference).
This is exactly (R1) (residue partition by construction of xb), (R2) for k = 1 (one point per height) and (D)
(GENERAL-REDUCTION.md Section 4; with the residue condition, an X pair never has a difference in H = <q>).
Normalizations (each preserves the existence of a solution, proof in README 2.2):
  N1 within each X block the smallest residue has height 0 (translate the block by a multiple of q);
  N2 X blocks ordered by their smallest residues (relabel blocks);
  N3 every Y block has its height-0 point at residue 0 (translate the block by a multiple of 4);
  N4 Y blocks ordered by the residue of their height-1 point, strictly increasing (relabel Y blocks).
Usage:  t2_sat.py encode q OUT.cnf      (writes the CNF and OUT.cnf.map.json; refuses to overwrite)
        t2_sat.py decode q OUT.cnf MODEL.txt SEED_OUT   (MODEL.txt = solver stdout with 'v' lines)
"""
import json
import os
import sys


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, *lits):
        self.clauses.append(lits)

    def exactly_one(self, lits):
        self.add(*lits)
        self.at_most_one(lits)

    def at_most_one(self, lits):
        lits = list(lits)
        if len(lits) <= 5:
            for i in range(len(lits)):
                for j in range(i + 1, len(lits)):
                    self.add(-lits[i], -lits[j])
            return
        # sequential counter (Sinz)
        s = [self.var() for _ in range(len(lits) - 1)]
        self.add(-lits[0], s[0])
        for i in range(1, len(lits) - 1):
            self.add(-lits[i], s[i])
            self.add(-s[i - 1], s[i])
            self.add(-lits[i], -s[i - 1])
        self.add(-lits[-1], -s[-1])

    def at_most_k(self, lits, k):
        """Sinz sequential counter: s[i][c] (c = 1..k) is implied by 'at least c of lits[0..i] are true'."""
        n = len(lits)
        s = [[self.var() for _ in range(k + 1)] for _ in range(n)]   # index c = 1..k used
        self.add(-lits[0], s[0][1])
        for c in range(2, k + 1):
            self.add(-s[0][c])
        for i in range(1, n):
            x = lits[i]
            self.add(-x, s[i][1])
            self.add(-s[i - 1][1], s[i][1])
            for c in range(2, k + 1):
                self.add(-x, -s[i - 1][c - 1], s[i][c])
                self.add(-s[i - 1][c], s[i][c])
            self.add(-x, -s[i - 1][k])


def encode(q):
    assert q % 2 == 1 and q % 12 == 1
    A, C = (q - 1) // 4, (q - 1) // 12
    f = CNF()
    xb = {(r, b): f.var() for r in range(1, q) for b in range(A)}
    xh = {(r, h): f.var() for r in range(1, q) for h in range(4)}
    ys = {(j, h, s): f.var() for j in range(C) for h in range(4) for s in range(q)}
    for r in range(1, q):
        f.exactly_one([xb[r, b] for b in range(A)])
        f.exactly_one([xh[r, h] for h in range(4)])
    for b in range(A):
        # at most 4 residues per block; with exactly one block per residue and 4A = q - 1 residues this is exactly 4
        f.at_most_k([xb[r, b] for r in range(1, q)], 4)
    for j in range(C):
        for h in range(4):
            f.exactly_one([ys[j, h, s] for s in range(q)])
    same, hd = {}, {}
    for r1 in range(1, q):
        for r2 in range(r1 + 1, q):
            sv = f.var()
            same[r1, r2] = sv
            for b in range(A):
                f.add(-sv, -xb[r1, b], xb[r2, b])
                f.add(-sv, xb[r1, b], -xb[r2, b])
                f.add(sv, -xb[r1, b], -xb[r2, b])
            for d in range(4):
                hv = f.var()
                hd[r1, r2, d] = hv
                for h in range(4):
                    f.add(-xh[r1, h], -xh[r2, (h + d) % 4], hv)
                    f.add(-hv, -xh[r1, h], xh[r2, (h + d) % 4])
    yd = {}
    for j in range(C):
        for h1 in range(4):
            for h2 in range(h1 + 1, 4):
                for e in range(q):
                    yv = f.var()
                    yd[j, h1, h2, e] = yv
                    for s in range(q):
                        f.add(-ys[j, h1, s], -ys[j, h2, (s + e) % q], yv)
                        f.add(-yv, -ys[j, h1, s], ys[j, h2, (s + e) % q])
                f.add(-yd[j, h1, h2, 0])
    # classes
    for delta in range(4):
        for e in range(1, (q - 1) // 2 + 1):
            cands = []
            for r in range(1, q):
                r2 = (r + e) % q
                if r2 == 0:
                    continue
                # unordered pair {r, r2} with h(r2) - h(r) = delta
                if r < r2:
                    a, b_, dd = r, r2, delta
                else:
                    a, b_, dd = r2, r, (-delta) % 4
                cv = f.var()
                f.add(-cv, same[a, b_])
                f.add(-cv, hd[a, b_, dd])
                f.add(cv, -same[a, b_], -hd[a, b_, dd])
                cands.append(cv)
            for j in range(C):
                for h1 in range(4):
                    for h2 in range(h1 + 1, 4):
                        dh = h2 - h1
                        if dh % 4 == delta:
                            cands.append(yd[j, h1, h2, e])
                        if (-dh) % 4 == delta:
                            cands.append(yd[j, h1, h2, (-e) % q])
            f.exactly_one(cands)
    # normalizations
    seen = {}
    for b in range(A):
        for r in range(1, q):
            sv = f.var()
            seen[r, b] = sv
            prev = seen.get((r - 1, b))
            f.add(-xb[r, b], sv)
            if prev:
                f.add(-prev, sv)
                f.add(-sv, prev, xb[r, b])
            else:
                f.add(-sv, xb[r, b])
            # N1: first residue of block b has height 0
            if prev:
                f.add(-xb[r, b], prev, xh[r, 0])
            else:
                f.add(-xb[r, b], xh[r, 0])
    for b in range(A - 1):                       # N2
        for r in range(1, q):
            prev = seen.get((r - 1, b))
            if prev:
                f.add(-xb[r, b + 1], prev)
            else:
                f.add(-xb[r, b + 1])
    for j in range(C):                           # N3
        f.add(ys[j, 0, 0])
    for j in range(C - 1):                       # N4
        for s in range(q):
            f.add(-ys[j + 1, 1, s], *[ys[j, 1, s2] for s2 in range(s)]) if s > 0 else f.add(-ys[j + 1, 1, 0])
    return f, {"q": q, "A": A, "C": C,
               "xb": {f"{r},{b}": v for (r, b), v in xb.items()},
               "xh": {f"{r},{h}": v for (r, h), v in xh.items()},
               "ys": {f"{j},{h},{s}": v for (j, h, s), v in ys.items()}}


def crt(h, r, q):
    for x in range(4 * q):
        if x % 4 == h and x % q == r:
            return x
    raise ValueError


def main(argv):
    if len(argv) >= 4 and argv[1] == "encode":
        q, out = int(argv[2]), argv[3]
        if os.path.exists(out) or os.path.exists(out + ".map.json"):
            raise SystemExit("refusing to overwrite")
        f, mp = encode(q)
        with open(out, "x") as fh:
            fh.write(f"p cnf {f.nv} {len(f.clauses)}\n")
            for c in f.clauses:
                fh.write(" ".join(map(str, c)) + " 0\n")
        with open(out + ".map.json", "x") as fh:
            json.dump(mp, fh)
        print(f"q={q} vars={f.nv} clauses={len(f.clauses)}")
        return 0
    if len(argv) == 6 and argv[1] == "decode":
        q, cnf, model, seed_out = int(argv[2]), argv[3], argv[4], argv[5]
        mp = json.load(open(cnf + ".map.json"))
        true = set()
        for line in open(model):
            if line.startswith("v "):
                true |= {int(x) for x in line.split()[1:] if int(x) > 0}
        A, C = mp["A"], mp["C"]
        blocks = [[] for _ in range(A)]
        height = {}
        for key, v in mp["xh"].items():
            if v in true:
                r, h = map(int, key.split(","))
                height[r] = h
        for key, v in mp["xb"].items():
            if v in true:
                r, b = map(int, key.split(","))
                blocks[b].append(crt(height[r], r, q))
        ypts = [[None] * 4 for _ in range(C)]
        for key, v in mp["ys"].items():
            if v in true:
                j, h, s = map(int, key.split(","))
                ypts[j][h] = crt(h, s, q)
        lines = [f"PC-SEED {4 * q}", f"SHORT {q}"]
        lines += ["X " + " ".join(map(str, sorted(B))) for B in sorted(sorted(B) for B in blocks)]
        for Y in sorted(sorted(Y) for Y in ypts):
            lines += ["GROUP 1", "Y " + " ".join(map(str, Y))]
        if os.path.exists(seed_out):
            raise SystemExit("refusing to overwrite")
        with open(seed_out, "x") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"wrote {seed_out}")
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
