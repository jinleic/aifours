"""Colouring of an STS (triples) by PARTIAL parallel classes with a prescribed abelian
class-symmetry group R.

Adapted from ../../rdsqs52/code/symres.py (sha256 47ff365a…dc2): the point-cover
constraint "exactly one triple per (class, point)" of a resolution is replaced by "at most
one", and an R-invariant extra class (the class missing the anchor) is supported.

R: list of permutations (closed abelian group, identity included) preserving the triple set.
stabs[k]: subgroup R_k <= R (list of perms) = stabilizer of the k-th representative class
C_k; the classes of orbit k are c(C_k) for coset reps c of R/R_k.  A triple orbit may be
placed in class orbit k only if its stabilizer lies in R_k; its placement is a coset g, and
then C_k contains R_k g^{-1}(t).  Placements whose sub-orbit already repeats a point are
dropped.  Every triple orbit gets exactly one placement; every (k, point) is covered at most
once.  anchored(): lossless labelling by the R-orbits of the triples through an R-fixed anchor.
"""
from __future__ import annotations

import collections

from mcdsqs_lib import CNF, comp


def inverse(p):
    inv = [0] * len(p)
    for i, x in enumerate(p):
        inv[x] = i
    return tuple(inv)


def img(g, t):
    return tuple(sorted(g[p] for p in t))


def build(triples, points, R, stabs):
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
            cnf.amo(cover.get((k, p), []))
    return cnf, orbits, choice, cosets, stabs


def anchored(der, pts, R, anchor, extra_fixed):
    """Class structure forced by the anchor (Lemma B of the README): one class orbit per
    R-orbit of triples through `anchor` (stabilizer = anchored triple stabilizer, anchored
    triple forced at the identity coset), plus `extra_fixed` R-invariant classes (stabilizer R)
    for the classes missing the anchor."""
    seen, anchor_orbits = set(), []
    for t in sorted(t for t in der if anchor in t):
        if t in seen:
            continue
        seen |= {img(g, t) for g in R}
        anchor_orbits.append((t, [g for g in R if img(g, t) == t]))
    stabs = [s for _, s in anchor_orbits] + [list(R)] * extra_fixed
    cnf, orbits, choice, cosets, stb = build(der, pts, R, stabs)
    ident = tuple(range(len(R[0])))
    for i, (t, _) in enumerate(anchor_orbits):
        oi = next(j for j, (u, _) in enumerate(orbits) if u == t)
        forced = [o[0] for o in choice[oi] if o[1] == i and o[2] == ident]
        cnf.add([forced[0]] if forced else [])
    sizes = [len(R) // len(s) for s in stabs]
    return cnf, orbits, choice, cosets, stb, sizes


def decode(model, orbits, choice, cosets, stabs, R):
    classes = {(k, i): set() for k in range(len(stabs)) for i in range(len(cosets[k]))}
    for (t, stab), opts in zip(orbits, choice):
        sel = [o for o in opts if o[0] in model]
        assert len(sel) == 1
        _, k, g = sel[0]
        for h in R:
            x = comp(h, g)
            idx = next(i for i, c in enumerate(cosets[k]) if any(comp(c, s) == x for s in stabs[k]))
            classes[(k, idx)].add(img(h, t))
    return [sorted(v) for _, v in sorted(classes.items())]
