#!/usr/bin/env python3
"""Generic CNF encoder for G-invariant symmetric weighing matrices (README 1.4).

Usage: python3 -B code/sw_cnf.py SPEC.json OUT.cnf [--s1] [--fix STRICT.sw] [--units UNITS.json]
Writes OUT.cnf and OUT.cnf.map.json (mode x).

Encoding (definition only, plus G-invariance by construction):
* cells {i,j}, i <= j (symmetry built in); G-orbits on cells with relative sign via union-find with parity; an orbit
  containing a cell and its negative is forced to 0 (no variables);
* orbit variables A (nonzero) and S (sign; true means value -1 on the orbit root); clause (A or not S);
* every row-orbit representative: exactly w nonzeros (truncated totalizer, both directions, cap w+1);
* every unordered row-pair-orbit representative {i,j}: P(o1,o2,t) <-> A_o1 & A_o2 & (S_o1 xor S_o2 = t) (full
  Tseitin); per column k the product W_ik W_jk is +1 (E) or -1 (D); #E = #D via two totalizers capped at w/2+1 with
  equal outputs 1..w/2 and output w/2+1 false (sound since #E + #D <= w);
* --s1: trace > 0 (number of +1 diagonal entries exceeds number of -1 diagonal entries), labelled variant S1;
* --fix FILE: unit clauses forcing every orbit to the value of the given strict matrix at its root (self-tests);
* --units FILE: JSON list of extra clauses over orbit literals {"cell":[i,j],"value":v} (case splits, labelled).
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402


class CNF:
    def __init__(self):
        self.nv = 0
        self.cls = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.cls.append(c)


def totalizer(cnf, inputs, cap):
    """Return outputs o[1..m] (list index t-1) with o_t <-> (#true inputs >= t), m = min(len(inputs), cap)."""
    if not inputs:
        return []
    layer = [[x] for x in inputs]
    while len(layer) > 1:
        nxt = []
        for k in range(0, len(layer) - 1, 2):
            a, b = layer[k], layer[k + 1]
            m = min(len(a) + len(b), cap)
            c = [cnf.new() for _ in range(m)]
            for i in range(len(a) + 1):
                for j in range(len(b) + 1):
                    if 1 <= i + j <= m:
                        cl = []
                        if i > 0:
                            cl.append(-a[i - 1])
                        if j > 0:
                            cl.append(-b[j - 1])
                        cl.append(c[i + j - 1])
                        cnf.add(cl)
                    if i + j < m:
                        cl = []
                        if i < len(a):
                            cl.append(a[i])
                        if j < len(b):
                            cl.append(b[j])
                        cl.append(-c[i + j])
                        cnf.add(cl)
            nxt.append(c)
        if len(layer) % 2 == 1:
            nxt.append(layer[-1])
        layer = nxt
    return layer[0]


def orbits(spec):
    n = spec["n"]
    cid = {}
    cells = []
    for i in range(n):
        for j in range(i, n):
            cid[(i, j)] = len(cells)
            cells.append((i, j))
    parent = list(range(len(cells)))
    par = [0] * len(cells)  # value(c) = (-1)^par[c] * value(parent[c])
    bad = set()

    def find(c):
        # path = [c, p1, ..., pk] with parent[pk] = root; par[x] is relative to parent[x].
        path = []
        while parent[c] != c:
            path.append(c)
            c = parent[c]
        root = c
        acc = 0
        for x in reversed(path):  # nearest-to-root first; par[x] still original when read
            acc ^= par[x]
            par[x] = acc  # now relative to root
            parent[x] = root
        return root

    def union(c1, c2, rel):  # value(c2) = (-1)^rel value(c1)
        r1, r2 = find(c1), find(c2)
        p1, p2 = par[c1] if c1 != r1 else 0, par[c2] if c2 != r2 else 0
        if r1 == r2:
            if (p1 ^ p2) != rel:
                bad.add(r1)
            return
        # value(c1) = (-1)^p1 v(r1); value(c2) = (-1)^p2 v(r2); want v(c2) = (-1)^rel v(c1)
        # => v(r2) = (-1)^(p2 ^ rel ^ p1) v(r1)
        parent[r2] = r1
        par[r2] = p1 ^ p2 ^ rel
        if r2 in bad:
            bad.add(r1)

    for g in spec["generators"]:
        p, s = g["perm"], g["sign"]
        for (i, j), c in cid.items():
            a, b = p[i], p[j]
            key = (a, b) if a <= b else (b, a)
            union(c, cid[key], 0 if s[i] * s[j] == 1 else 1)
    roots = {}
    for c in range(len(cells)):
        r = find(c)
        roots[c] = (r, par[c] if c != r else 0)
    zero_roots = set(find(b) for b in bad)
    return cells, cid, roots, zero_roots


def row_orbits(spec, pairs=False):
    n = spec["n"]
    gens = [g["perm"] for g in spec["generators"]]
    seen = set()
    reps = []
    items = [(i, j) for i in range(n) for j in range(i + 1, n)] if pairs else [(i,) for i in range(n)]
    for it in items:
        if it in seen:
            continue
        reps.append(it)
        stack = [it]
        seen.add(it)
        while stack:
            x = stack.pop()
            for p in gens:
                y = tuple(sorted(p[v] for v in x))
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return reps


def main():
    spec_path, out = sys.argv[1], sys.argv[2]
    opts = sys.argv[3:]
    spec_text = open(spec_path).read()
    spec = json.loads(spec_text)
    n, w = spec["n"], spec["w"]
    cells, cid, roots, zero_roots = orbits(spec)
    cnf = CNF()
    A, S = {}, {}
    for c in range(len(cells)):
        r = roots[c][0]
        if r in zero_roots or r in A:
            continue
        A[r] = cnf.new()
        S[r] = cnf.new()
        cnf.add([A[r], -S[r]])

    def cell(i, j):
        c = cid[(i, j) if i <= j else (j, i)]
        r, p = roots[c]
        if r in zero_roots:
            return None
        return r, p

    # rows
    row_reps = row_orbits(spec)
    for (i,) in row_reps:
        ins = []
        for j in range(n):
            x = cell(i, j)
            if x is not None:
                ins.append(A[x[0]])
        outs = totalizer(cnf, ins, w + 1)
        if len(outs) < w:
            cnf.add([])  # row cannot reach weight w
        else:
            cnf.add([outs[w - 1]])
            if len(outs) > w:
                cnf.add([-outs[w]])
    # pairs
    Pcache = {}

    def P(o1, o2, t):
        key = (min(o1, o2), max(o1, o2), t)
        if key in Pcache:
            return Pcache[key]
        v = cnf.new()
        a1, a2, s1, s2 = A[o1], A[o2], S[o1], S[o2]
        cnf.add([-v, a1])
        cnf.add([-v, a2])
        if t == 0:  # s1 == s2
            cnf.add([-v, -s1, s2])
            cnf.add([-v, s1, -s2])
            cnf.add([-a1, -a2, -s1, -s2, v])
            cnf.add([-a1, -a2, s1, s2, v])
        else:
            cnf.add([-v, s1, s2])
            cnf.add([-v, -s1, -s2])
            cnf.add([-a1, -a2, -s1, s2, v])
            cnf.add([-a1, -a2, s1, -s2, v])
        Pcache[key] = v
        return v

    pair_reps = row_orbits(spec, pairs=True)
    half = w // 2
    for (i, j) in pair_reps:
        E, D = [], []
        for k in range(n):
            x, y = cell(i, k), cell(j, k)
            if x is None or y is None:
                continue
            (o1, p1), (o2, p2) = x, y
            tau = p1 ^ p2
            if o1 == o2:
                (E if tau == 0 else D).append(A[o1])
            else:
                E.append(P(o1, o2, tau))
                D.append(P(o1, o2, 1 - tau))
        eo = totalizer(cnf, E, half + 1)
        do = totalizer(cnf, D, half + 1)
        for t in range(1, half + 1):
            le = eo[t - 1] if t <= len(eo) else None
            ld = do[t - 1] if t <= len(do) else None
            if le is None and ld is None:
                continue
            if le is None:
                cnf.add([-ld])
            elif ld is None:
                cnf.add([-le])
            else:
                cnf.add([-le, ld])
                cnf.add([le, -ld])
        if len(eo) > half:
            cnf.add([-eo[half]])
        if len(do) > half:
            cnf.add([-do[half]])
    labels = []
    if "--s1" in opts:
        labels.append("S1")
        pos, neg = [], []
        for i in range(n):
            x = cell(i, i)
            if x is None:
                continue
            o, p = x
            vp, vn = cnf.new(), cnf.new()
            # vp <-> A & (S xor p == 0); vn <-> A & (S xor p == 1)
            sl = S[o] if p == 0 else -S[o]  # sl true <-> value -1
            cnf.add([-vp, A[o]])
            cnf.add([-vp, -sl])
            cnf.add([-A[o], sl, vp])
            cnf.add([-vn, A[o]])
            cnf.add([-vn, sl])
            cnf.add([-A[o], -sl, vn])
            pos.append(vp)
            neg.append(vn)
        po = totalizer(cnf, pos, n)
        no = totalizer(cnf, neg, n)
        if not po:
            cnf.add([])
        else:
            cnf.add([po[0]])
            for t in range(1, len(no) + 1):
                if t + 1 <= len(po):
                    cnf.add([-no[t - 1], po[t]])
                else:
                    cnf.add([-no[t - 1]])
    if "--fix" in opts:
        fpath = opts[opts.index("--fix") + 1]
        labels.append("FIX:" + hashlib.sha256(open(fpath, "rb").read()).hexdigest())
        _, _, Wf = C.read_strict(fpath)
        for (i, j), c in cid.items():
            x = cell(i, j)
            v = Wf[i][j]
            if x is None:
                if v != 0:
                    cnf.add([])
                continue
            o, p = x
            if v == 0:
                cnf.add([-A[o]])
            else:
                cnf.add([A[o]])
                neg_root = (v == -1) ^ (p == 1)  # root value -1 ?
                cnf.add([S[o] if neg_root else -S[o]])
    if "--units" in opts:
        upath = opts[opts.index("--units") + 1]
        labels.append("UNITS:" + hashlib.sha256(open(upath, "rb").read()).hexdigest())
        for u in json.load(open(upath)):
            i, j = u["cell"]
            v = u["value"]
            x = cell(i, j)
            if x is None:
                if v != 0:
                    cnf.add([])
                continue
            o, p = x
            if v == 0:
                cnf.add([-A[o]])
            else:
                cnf.add([A[o]])
                neg_root = (v == -1) ^ (p == 1)
                cnf.add([S[o] if neg_root else -S[o]])
    text = f"p cnf {cnf.nv} {len(cnf.cls)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in cnf.cls)
    with open(out, "x") as f:
        f.write(text)
    cmap = {
        "spec": spec_path, "spec_sha256": hashlib.sha256(spec_text.encode()).hexdigest(), "n": n, "w": w,
        "labels": labels, "vars": cnf.nv, "clauses": len(cnf.cls),
        "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "cell_orbits_nonzero": len(A), "forced_zero_cells": sum(1 for c in range(len(cells))
                                                                   if roots[c][0] in zero_roots),
        "row_reps": len(row_reps), "pair_reps": len(pair_reps),
        "cells": {f"{i},{j}": (None if roots[cid[(i, j)]][0] in zero_roots else
                               [A[roots[cid[(i, j)]][0]], S[roots[cid[(i, j)]][0]], roots[cid[(i, j)]][1]])
                  for (i, j) in cells},
    }
    with open(out + ".map.json", "x") as f:
        json.dump(cmap, f)
        f.write("\n")
    print(json.dumps({k: cmap[k] for k in ("spec", "labels", "vars", "clauses", "cnf_sha256", "cell_orbits_nonzero",
                                           "forced_zero_cells", "row_reps", "pair_reps")}))


if __name__ == "__main__":
    main()
