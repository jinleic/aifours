#!/usr/bin/env python3
"""README E9b: coupled design/colouring model (the design is NOT fixed).

KM part: a pool P of KM rows (orbits of 4-sets under GROUP) = the union of the rows of several
recorded designs; variables y_r (r in P); every KM column covered by exactly one selected row.
Any exact cover from P is a GROUP-invariant CQS(g^4 : 0), in general different from every pooled
design (mixtures / trades between them).
Colouring part at x = 0: every 4-set through x of a pooled row gives a potential triple of D_x
(present iff its row is selected).  Triples are grouped in R-orbits, R = <pi1> (Stab(x) of the
A4 x coordinate groups used here); class orbits: hole-avoiding [1, 3, 3, 3, 3, 3] (R-fixed class
first), 16 non-avoiding orbits of size 3 (pi1 fixes no non-hole point, so no non-avoiding class is
pi1-invariant).  A present triple orbit gets exactly one placement, an absent one none; at most
one triple per (class orbit, point); strengthening S1/S2 and the profile are the copied
colour_model functions (valid for every CQS).  The anchored forcing of the fixed-design model is
replaced by sound lex symmetry breaking: for the anchor h (non-avoiding orbits) and for the least
non-hole point q0 (the full hole-avoiding orbits under a P-profile), the representative of each
orbit is its class with the least-index triple through h (resp. q0), and orbits are ordered by it.

build OUTDIR --group G --g 32 --pool S1.json:i[,S2.json:j...] [--profile P16] [--strengthen]
      [--symbreak]          writes OUTDIR/col.cnf and OUTDIR/summary.json (no solving)
decode OUTDIR LOG NEWDIR    rebuilds the model from OUTDIR/summary.json, checks the CNF sha256
                            and that the retained kissat model satisfies it, decodes design and
                            colouring, transports it by the group and writes a GCDCQS certificate.
"""
import lane_guard  # noqa: F401

import argparse
import collections
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import CNF, closure, comp, inverse, gcsts_params, parse_status, model_satisfies  # noqa: E402
from cqs_km import CQSKM  # noqa: E402
import colour_model as cm  # noqa: E402
import groups as grp  # noqa: E402
from pipeline import certificate_text, derived  # noqa: E402


def img(g, t):
    return tuple(sorted(g[p] for p in t))


def lex_break(cnf, orbits, choice, R, T0, ks):
    """For class orbits ks (trivial stabilizer): representative = class with the least-index triple of
    T0 (all triples of T0 share one point lying in every class of these orbits); orbits ordered."""
    ident = tuple(range(len(R[0])))
    where = {}
    for oi, (u, _) in enumerate(orbits):
        for h in R:
            where.setdefault(img(h, u), (oi, h))

    def z(k, c, t):
        if t not in where:
            return None
        oi, h = where[t]
        gneed = comp(inverse(h), c)
        lits = [v for v, kk, g in choice[oi] if kk == k and g == gneed]
        return lits[0] if lits else None

    nonid = [c for c in R if c != ident]
    n = 0
    for k in ks:
        for a, t in enumerate(T0):
            zt = z(k, ident, t)
            if zt is None:
                continue
            for c in nonid:
                for t2 in T0[:a]:
                    w = z(k, c, t2)
                    if w is not None:
                        cnf.add([-zt, -w])
                        n += 1
    for k, k2 in zip(ks, ks[1:]):
        for a, t in enumerate(T0):
            zt = z(k, ident, t)
            if zt is None:
                continue
            for t2 in T0[:a + 1]:
                w = z(k2, ident, t2)
                if w is not None:
                    cnf.add([-zt, -w])
                    n += 1
    return n


def build_model(a):
    v, g = 4 * a.g, a.g
    spec = grp.build(a.group, 4, g)
    gens, group_of = spec["gens"], spec["group_of"]
    R = closure(spec["res"]["C3"], v)
    r, s = gcsts_params(v - 1, g - 1)
    km = CQSKM(v, group_of, gens)
    pool = set()
    for item in a.pool.split(","):
        path, idx = item.rsplit(":", 1)
        src = json.load(open(path))
        assert src["group"] == a.group and src["g"] == g
        pool |= set(src["samples"][int(idx)]["rows"])
    pool = sorted(pool)
    lab2row = {km.rows[j][0]: j for j in pool}
    mask0 = (km.Q[:, 0] == 0) & km.q_valid
    labs0, quads0 = km.LQ[mask0], km.Q[mask0]
    T = {}
    for lab, q in zip(labs0.tolist(), quads0.tolist()):
        if lab in lab2row:
            T[tuple(q[1:])] = lab2row[lab]
    x, h = 0, 1
    hole = {q for q in range(v) if group_of[q] == 0 and q != 0}
    pts = [q for q in range(v) if q != 0]
    cnf = CNF()
    y = {j: cnf.var() for j in pool}
    bycol = collections.defaultdict(list)
    for j in pool:
        for c in km.rows[j][1]:
            bycol[c].append(y[j])
    assert sorted(bycol) == list(range(len(km.tcols))), "pool does not cover every KM column"
    for c in sorted(bycol):
        cnf.exactly_one(bycol[c])
    seen, orbits = set(), []
    for t in sorted(T):
        if t in seen:
            continue
        orb = {img(e, t) for e in R}
        assert all(T.get(u) == T[t] for u in orb), "R does not preserve a row's triples"
        seen |= orb
        orbits.append((t, [e for e in R if img(e, t) == t]))
    ident = tuple(range(v))
    triv = [ident]
    stabs = [list(R)] + [triv] * 5 + [triv] * 16
    flags = [True] * 6 + [False] * 16
    cosets = []
    for S in stabs:
        reps_, seen_c = [], set()
        for e in sorted(R):
            if e in seen_c:
                continue
            reps_.append(e)
            seen_c.update(comp(e, ss) for ss in S)
        cosets.append(reps_)
    choice, cover = [], collections.defaultdict(list)
    for t, stab in orbits:
        opts = []
        has_hole = bool(set(t) & hole)
        for k, S in enumerate(stabs):
            if flags[k] and has_hole:
                continue
            for e in cosets[k]:
                einv = inverse(e)
                if not all(comp(comp(einv, hh), e) in S for hh in stab):
                    continue
                blks = {img(comp(ss, einv), t) for ss in S}
                pc = collections.Counter(p for b in blks for p in b)
                if any(cnt > 1 for cnt in pc.values()):
                    continue
                var = cnf.var()
                opts.append((var, k, e))
                for p in pc:
                    cover[(k, p)].append(var)
        yr = y[T[t]]
        cnf.amo([o[0] for o in opts])
        cnf.add([-yr] + [o[0] for o in opts])
        for o in opts:
            cnf.add([-o[0], yr])
        choice.append(opts)
    for k in range(len(stabs)):
        for p in pts:
            cnf.amo(cover.get((k, p), []))
    if a.strengthen or a.profile:
        cov = cm.add_strengthening(cnf, cover, pts, hole, R, stabs, cosets, flags)
        if a.profile in ("P10", "P16"):
            cm.add_profile_p10(cnf, cover, pts, hole, R, stabs, cosets, flags, cov)
        elif a.profile:
            raise SystemExit("unsupported profile for the coupled model")
    nsb = 0
    if a.symbreak:
        assert a.profile in ("P10", "P16")
        Th = sorted(t for t in T if h in t)
        nsb += lex_break(cnf, orbits, choice, R, Th, list(range(6, 22)))
        q0 = min(p for p in pts if p not in hole)
        Tq = sorted(t for t in T if q0 in t and not set(t) & hole)
        nsb += lex_break(cnf, orbits, choice, R, Tq, list(range(1, 6)))
    meta = {"pool_rows": len(pool), "potential_triples": len(T), "triple_orbits": len(orbits),
            "vars": cnf.nv, "clauses": len(cnf.clauses), "symbreak_clauses": nsb, "r": r, "s": s}
    return cnf, meta, (km, pool, y, orbits, choice, cosets, stabs, R, spec, hole, pts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["build", "decode"])
    ap.add_argument("out")
    ap.add_argument("log", nargs="?")
    ap.add_argument("newdir", nargs="?")
    ap.add_argument("--group")
    ap.add_argument("--g", type=int, default=32)
    ap.add_argument("--pool")
    ap.add_argument("--profile", default=None)
    ap.add_argument("--strengthen", action="store_true")
    ap.add_argument("--symbreak", action="store_true")
    a = ap.parse_args()
    if a.mode == "build":
        fresh_dir(a.out)
        cnf, meta, _ = build_model(a)
        sha = cnf.write(os.path.join(a.out, "col.cnf"))
        meta.update({"args": vars(a), "cnf_sha256": sha})
        with xopen(os.path.join(a.out, "summary.json")) as fh:
            json.dump(meta, fh, indent=1)
        print(json.dumps(meta))
        return 0
    rec = json.load(open(os.path.join(a.out, "summary.json")))
    b = argparse.Namespace(**rec["args"])
    fresh_dir(a.newdir)
    cnf, meta, (km, pool, y, orbits, choice, cosets, stabs, R, spec, hole, pts) = build_model(b)
    p = os.path.join(a.newdir, "col_rebuilt.cnf")
    sha = cnf.write(p)
    assert sha == rec["cnf_sha256"], "rebuilt CNF differs"
    st, model = parse_status(open(a.log).read())
    assert st == "SAT" and model_satisfies(p, model)
    sel = [j for j in pool if y[j] in model]
    blocks = km.blocks_of(sel)
    v, g = 4 * b.g, b.g
    der = derived(blocks, 0)
    classes_d = {(k, i): set() for k in range(len(stabs)) for i in range(len(cosets[k]))}
    for (t, stab), opts in zip(orbits, choice):
        chosen = [o for o in opts if o[0] in model]
        assert len(chosen) <= 1
        if not chosen:
            continue
        _, k, e = chosen[0]
        for hh in R:
            xg = comp(hh, e)
            idx = next(i for i, c in enumerate(cosets[k]) if any(comp(c, ss) == xg for ss in stabs[k]))
            classes_d[(k, idx)].add(img(hh, t))
    classes = [sorted(vv) for _, vv in sorted(classes_d.items())]
    cm.verify_good_colouring(der, pts, sorted(hole), classes, meta["r"], meta["s"])
    G = closure(spec["gens"], v)
    col = {}
    for e in G:
        if e[0] not in col:
            col[e[0]] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in classes]
    assert sorted(col) == list(range(v))
    text = certificate_text(v, 4, g, meta["r"], meta["s"], spec["groups"], blocks, col,
                            f"gcDCQS({g}^4:0) candidate: coupled model (README E9b), group {b.group}, "
                            f"R=C3, pool {b.pool}, profile {b.profile}")
    cert = os.path.join(a.newdir, f"gcdcqs{g}_coupled.txt")
    with xopen(cert) as fh:
        fh.write(text)
    with xopen(os.path.join(a.newdir, "selected_rows.json")) as fh:
        json.dump({"group": b.group, "g": g, "samples": [{"sample": 0, "km_status": "COUPLED", "rows": sel}]}, fh)
    chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), cert], capture_output=True, text=True)
    print(cert, hashlib.sha256(text.encode()).hexdigest(), json.loads(chk.stdout)["result"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
