"""Resolution of a design (triples) with a prescribed abelian class-symmetry group R.

R: list of permutations (closed abelian group, identity included) preserving the
triple set.  stabs[k]: subgroup R_k ≤ R (list of perms) = stabilizer of the k-th
representative class C_k; the classes are g(C_k) for coset reps g of R/R_k, so
sum_k |R:R_k| must equal the number of classes.  A triple orbit may contribute to
class orbit k only if its stabilizer lies in R_k; its placement is a coset g.
Optional: anchor point to fix class labels is not needed (orbits label classes).
"""
from __future__ import annotations

import collections

from rdsqs_lib import CNF, comp


def inverse(p):
    inv = [0] * len(p)
    for i, x in enumerate(p):
        inv[x] = i
    return tuple(inv)


def img(g, t):
    return tuple(sorted(g[p] for p in t))


def build(triples, points, R, stabs):
    Rset = set(R)
    stabs = [set(s) for s in stabs]
    cosets = []
    for S in stabs:
        reps, seen = [], set()
        for g in sorted(R):
            if g in seen:
                continue
            reps.append(g)
            seen.update(comp(g, s) for s in S)
        cosets.append(reps)
    tset = set(triples)
    seen, orbits = set(), []
    for t in sorted(tset):
        if t in seen:
            continue
        orb = {img(g, t) for g in R}
        assert orb <= tset, "R does not preserve the triples"
        seen |= orb
        stab = {g for g in R if img(g, t) == t}
        orbits.append((t, stab))
    cnf = CNF()
    choice = []
    cover = collections.defaultdict(list)
    for t, stab in orbits:
        opts = []
        for k, S in enumerate(stabs):
            if not stab <= S:
                continue
            for g in cosets[k]:
                ginv = inverse(g)
                blks = {img(comp(s, ginv), t) for s in S}
                pts = collections.Counter(p for b in blks for p in b)
                if any(c > 1 for c in pts.values()):
                    continue
                v = cnf.var()
                opts.append((v, k, g))
                for p in pts:
                    cover[(k, p)].append(v)
        cnf.exactly_one([o[0] for o in opts])
        choice.append(opts)
    for k in range(len(stabs)):
        for p in points:
            cnf.exactly_one(cover.get((k, p), []))
    return cnf, orbits, choice, cosets, stabs


def decode(model, orbits, choice, cosets, stabs, R):
    classes = {}
    for (t, stab), opts in zip(orbits, choice):
        sel = [o for o in opts if o[0] in model]
        assert len(sel) == 1
        _, k, g = sel[0]
        for h in R:
            x = comp(h, g)
            idx = next(i for i, c in enumerate(cosets[k]) if any(comp(c, s) == x for s in stabs[k]))
            classes.setdefault((k, idx), set()).add(img(h, t))
    return [sorted(v) for _, v in sorted(classes.items())]
