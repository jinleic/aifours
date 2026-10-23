"""Resolution of a given STS with a prescribed cyclic class symmetry, via SAT.

Given blocks (3-tuples) of an STS on n points, a permutation r preserving the
block set, and class-orbit sizes d_1..d_K (each d_k divides ord(r), sum = (n-1)/2),
find a resolution in which r maps class r^s C_k to r^(s+1) C_k and
r^(d_k) C_k = C_k.  A block orbit of size e may enter class orbit k only if
d_k | e; offset s in Z_{d_k} means block b lies in r^s C_k.
"""
from __future__ import annotations

import collections

from lkts_core import perm_order
from satlib import CNF, solve


def block_orbits(blocks, r):
    bset = {tuple(sorted(b)) for b in blocks}
    seen = set()
    orbits = []
    for b in sorted(bset):
        if b in seen:
            continue
        orb = []
        x = b
        while x not in seen:
            seen.add(x)
            orb.append(x)
            x = tuple(sorted(r[p] for p in x))
            if x not in bset:
                raise ValueError("r does not preserve the block set")
        orbits.append(orb)  # orb[j] = r^j b
    return orbits


def build(blocks, n, r, sizes):
    m = perm_order(r)
    assert all(m % d == 0 for d in sizes)
    assert sum(sizes) == (n - 1) // 2
    orbits = block_orbits(blocks, r)
    cnf = CNF()
    choice = []  # per orbit: list of (var, k, s)
    cover = collections.defaultdict(list)  # (k, p) -> vars
    for W in orbits:
        e = len(W)
        opts = []
        for k, d in enumerate(sizes):
            if e % d:
                continue
            for s in range(d):
                # blocks r^j b in C_k  <=>  j + s ≡ 0 (mod d)
                pts = collections.Counter()
                for j in range(e):
                    if (j + s) % d == 0:
                        for p in W[j]:
                            pts[p] += 1
                if any(c > 1 for c in pts.values()):
                    continue
                v = cnf.var()
                opts.append((v, k, s))
                for p in pts:
                    cover[(k, p)].append(v)
        if not opts:
            cnf.add([])
        cnf.exactly_one([o[0] for o in opts])
        choice.append(opts)
    for k in range(len(sizes)):
        for p in range(n):
            lits = cover.get((k, p), [])
            if not lits:
                cnf.add([])
            else:
                cnf.exactly_one(lits)
    return cnf, orbits, choice


def decode(model, orbits, choice, sizes, r):
    """Return list of classes (each a list of blocks)."""
    classes = []
    index = {}
    for k, d in enumerate(sizes):
        for s in range(d):
            index[(k, s)] = len(classes)
            classes.append([])
    for W, opts in zip(orbits, choice):
        sel = [o for o in opts if o[0] in model]
        assert len(sel) == 1
        _, k, s = sel[0]
        d = sizes[k]
        for j, b in enumerate(W):
            classes[index[(k, (j + s) % d)]].append(b)
    return classes


def resolve_symmetric(blocks, n, r, sizes, path, solver="kissat", timeout=300, seed=None, log=None):
    cnf, orbits, choice = build(blocks, n, r, sizes)
    sha = cnf.write(path)
    st, model, dt = solve(path, solver, timeout=timeout, seed=seed, log=log)
    classes = decode(model, orbits, choice, sizes, r) if st == "SAT" else None
    return {"status": st, "seconds": dt, "cnf_sha256": sha, "vars": cnf.nv,
            "clauses": len(cnf.clauses), "block_orbits": len(orbits)}, classes


def check_resolution(blocks, n, classes):
    bset = {tuple(sorted(b)) for b in blocks}
    allc = [tuple(sorted(b)) for C in classes for b in C]
    assert len(allc) == len(bset) == len(set(allc)) and set(allc) == bset
    for C in classes:
        pts = [p for b in C for p in b]
        assert sorted(pts) == list(range(n)), "class is not a partition"
    return True


def build_group(blocks, n, R, stabs):
    """Abelian class symmetry group R (list of perms, includes identity).
    stabs[k] = list of perms: stabilizer subgroup R_k of class-orbit rep C_k.
    Classes are g C_k for cosets g R_k; sum_k |R:R_k| must equal (n-1)/2."""
    from lkts_core import compose, inverse
    Rset = set(R)
    ident = tuple(range(n))
    assert ident in Rset
    for a in R:
        for b in R:
            assert compose(a, b) == compose(b, a), "R must be abelian"
    stabs = [set(s) for s in stabs]
    cosets = []
    for S in stabs:
        reps, seen = [], set()
        for g in R:
            if g in seen:
                continue
            reps.append(g)
            seen.update(compose(g, s) for s in S)
        cosets.append(reps)
    assert sum(len(c) for c in cosets) == (n - 1) // 2, [len(c) for c in cosets]
    bset = {tuple(sorted(b)) for b in blocks}
    img = lambda g, b: tuple(sorted(g[p] for p in b))
    seen, orbits = set(), []
    for b in sorted(bset):
        if b in seen:
            continue
        orb = {img(g, b) for g in R}
        assert orb <= bset, "R does not preserve blocks"
        seen |= orb
        stab = {g for g in R if img(g, b) == b}
        orbits.append((b, stab))
    cnf = CNF()
    choice = []
    cover = collections.defaultdict(list)
    for b, stab in orbits:
        opts = []
        for k, S in enumerate(stabs):
            if not stab <= S:
                continue
            for g in cosets[k]:
                ginv = inverse(g)
                hs = {compose(s, ginv) for s in S}
                blks = {img(h, b) for h in hs}
                pts = collections.Counter(p for x in blks for p in x)
                if any(c > 1 for c in pts.values()):
                    continue
                v = cnf.var()
                opts.append((v, k, g))
                for p in pts:
                    cover[(k, p)].append(v)
        if not opts:
            cnf.add([])
        else:
            cnf.exactly_one([o[0] for o in opts])
        choice.append(opts)
    for k in range(len(stabs)):
        for p in range(n):
            lits = cover.get((k, p), [])
            if not lits:
                cnf.add([])
            else:
                cnf.exactly_one(lits)
    return cnf, orbits, choice, cosets, stabs


def decode_group(model, orbits, choice, cosets, stabs, R):
    from lkts_core import compose
    img = lambda g, b: tuple(sorted(g[p] for p in b))
    # class id = (k, coset rep index); find coset of element x in R/R_k
    def coset_index(k, x):
        for idx, g in enumerate(cosets[k]):
            if any(compose(g, s) == x for s in stabs[k]):
                return idx
        raise AssertionError
    classes = {}
    for (b, stab), opts in zip(orbits, choice):
        sel = [o for o in opts if o[0] in model]
        assert len(sel) == 1
        _, k, g = sel[0]
        for h in R:
            blk = img(h, b)
            cid = (k, coset_index(k, compose(h, g)))
            classes.setdefault(cid, set()).add(blk)
    return [sorted(v) for _, v in sorted(classes.items(), key=lambda kv: (kv[0][0], kv[0][1]))]


def resolve_group(blocks, n, R, stabs, path, solver="kissat", timeout=300, seed=None, log=None):
    cnf, orbits, choice, cosets, st_ = build_group(blocks, n, R, stabs)
    sha = cnf.write(path)
    st, model, dt = solve(path, solver, timeout=timeout, seed=seed, log=log)
    classes = decode_group(model, orbits, choice, cosets, st_, R) if st == "SAT" else None
    return {"status": st, "seconds": dt, "cnf_sha256": sha, "vars": cnf.nv,
            "clauses": len(cnf.clauses), "block_orbits": len(orbits)}, classes
