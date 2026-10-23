#!/usr/bin/env python3
"""moqls8 encoder binding v1 -- parent verification driver (see ../README.md). Single process, single thread.

  python -B bind.py --target K5 --out ../K5.bind.json --names-out ../K5.names.json.gz --solve
  python -B bind.py --target K4 --out ../K4.bind.json --names-out ../K4.names.json.gz --solve
  python -B bind.py --target K5 --flag-variant --base-json ../K5.bind.json --out ../K5.flagvariant.json --solve

Regeneration: the pinned encoder copy (code/gram_a.py or code/gram_a_r3.py, byte-identical to the snapshot) is imported
and ITS OWN main() is run with the argv recorded in the lane map JSON (only the --cnf/--map values are replaced by paths
in this directory); the module-level build() is wrapped so that the CNF object is captured and main() is stopped before
it opens any output file.  The DIMACS bytes are produced with main()'s two writer expressions
("p cnf %d %d\n" % (nv, C) and " ".join(map(str, cl)) + " 0\n") into SHA-256, never to disk.
Every clause is then classified through the encoder's name table into the families of
review/K4K5_ENCODING_SOUNDNESS.r2.md with semantic validation of each instance, compared as a multiset (per family,
name space, BLAKE2b-128 additive fingerprint + count) with an independently written generator of the declared families,
and evaluated under the canonical assignment of a classical AG(2,8) set of 5 MOLS(8) built and verified here.
--solve: kissat (native --time <= 600 s, stdin) on the C12 control instances only (base minus P4 at-least-one clauses
and minus the declared SB2 units, plus one unit per g variable fixing the classical Gram pattern); models are checked
against every clause of the instance here.  Nothing here claims or implies an exclusion of K4 or K5.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import resource
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.dirname(HERE)
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16"
DISK_FLOOR = 12_000_000_000
SOLVER_TIME = 600
TARGETS = {
    "K5": {"encoder": "gram_a.py", "stored": LANE + "/evidence/gram_dev_v1/GA5L_K5_sb2.cnf",
           "lane_map": LANE + "/evidence/gram_dev_v1/GA5L_K5_sb2.map.json",
           "declared_sha256": "6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b",
           "declared_where": "lane README section 8 (lines 180-182) and the lane map meta",
           "declared_vars": 509915, "declared_clauses": 5740230},
    "K4": {"encoder": "gram_a_r3.py", "stored": LANE + "/evidence/k4_w1_v1/GA3_K4w1.cnf",
           "lane_map": LANE + "/evidence/k4_w1_v1/GA3_K4w1.map.json",
           "declared_sha256": "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7",
           "declared_where": "lane map meta (README section 7 records the command line, not the SHA)",
           "declared_vars": 513184, "declared_clauses": 5833793},
}
FAMILIES = ["G2", "G3", "AND_DEF", "G4", "G5", "P4", "ROWLEX", "W1", "SB2"]
T0 = time.time()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def log(*a):
    print("[%s +%.0fs]" % (now(), time.time() - T0), *a, file=sys.stderr, flush=True)


def sha_file(path):
    h = hashlib.sha256()
    n = 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 22), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def check_disk():
    free = shutil.disk_usage(OUTDIR).free
    if free < DISK_FLOOR:
        raise SystemExit("disk floor: free %d < %d" % (free, DISK_FLOOR))
    return free


# ----------------------------------------------------------------------------------------------- geometry
N = 8


def set_order(n):
    global N, CELLS, LINEKEYS
    N = n
    CELLS = [(i, j) for i in range(N) for j in range(N)]
    LINEKEYS = [("R", r) for r in range(N)] + [("C", c) for c in range(N)]


set_order(8)


def collinear(p, q):
    return p != q and (p[0] == q[0] or p[1] == q[1])


def line_cells(lk):
    t, x = lk
    return [(x, j) for j in range(N)] if t == "R" else [(i, x) for i in range(N)]


def on_line(c, lk):
    return c[0] == lk[1] if lk[0] == "R" else c[1] == lk[1]


def lk_of(cells):
    if len(cells) < 2:
        return None
    if len({c[0] for c in cells}) == 1:
        return ("R", cells[0][0])
    if len({c[1] for c in cells}) == 1:
        return ("C", cells[0][1])
    return None


def gname(s, p, q):
    """Declared semantics of the primary variables: True on the diagonal, False on a common row/column."""
    if p == q:
        return True
    if collinear(p, q):
        return False
    a, b = (p, q) if p < q else (q, p)
    return ("g", s, a, b)


# ----------------------------------------------------------------------------------------------- regeneration
class _Captured(Exception):
    pass


def regenerate(encoder_path, argv):
    spec = importlib.util.spec_from_file_location("pinned_encoder", encoder_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    box = {}
    orig = mod.build

    def capture(*a, **k):
        f = orig(*a, **k)
        box.update(args=repr(a), kwargs=repr(k), f=f)
        raise _Captured

    mod.build = capture
    saved = sys.argv
    sys.argv = list(argv)
    try:
        mod.main()
    except _Captured:
        pass
    finally:
        sys.argv = saved
    if "f" not in box:
        raise RuntimeError("encoder main() returned without calling build()")
    return box


def dimacs_sha(f):
    h = hashlib.sha256()
    head = ("p cnf %d %d\n" % (f.nv, len(f.clauses))).encode()
    h.update(head)
    n = len(head)
    buf = []
    for cl in f.clauses:
        buf.append(" ".join(map(str, cl)) + " 0\n")
        if len(buf) == 65536:
            b = "".join(buf).encode()
            h.update(b)
            n += len(b)
            buf = []
    if buf:
        b = "".join(buf).encode()
        h.update(b)
        n += len(b)
    return h.hexdigest(), n


def fp_of(key):
    return int.from_bytes(hashlib.blake2b(repr(key).encode(), digest_size=16).digest(), "big")


class FP:
    MOD = 1 << 128

    def __init__(self):
        self.c = Counter()
        self.s = defaultdict(int)

    def add(self, fam, key):
        self.c[fam] += 1
        self.s[fam] = (self.s[fam] + fp_of(key)) % self.MOD

    def as_json(self):
        return {fam: {"count": self.c[fam], "fp": "%032x" % self.s[fam]} for fam in sorted(self.c)}


# ----------------------------------------------------------------------------------------------- declared spec
def declared_spec(target, flag_variant):
    rows = [("R", r) for r in range(N)]
    cols = [("C", c) for c in range(N)]
    if target == "K5":   # README section 8; soundness note sections 2-5 (K5 base)
        spec = dict(quantum=[1, 2, 3, 4, 5], g5=True, p4_squares=[1, 2, 3, 4, 5], p4_frames=[("R", 0)],
                    w3_style="row", rowlex=True, sb2="K5", weight1=None)
    else:                # README section 7; soundness note sections 2-5 (K4 weight-1 CNF)
        spec = dict(quantum=[1, 2, 3, 4, 5], g5=True, p4_squares=[1, 2, 3, 4], p4_frames=rows + cols,
                    w3_style="line", rowlex=False, sb2="K4", weight1=5)
    if flag_variant:
        spec.update(p4_squares=[], sb2=None)
    return spec


def declared_sb2_units(spec):
    """(sign, name) unit literals declared by the soundness note: K5 LF 45-48, K4 LF 52-55."""
    out = []
    if spec["sb2"] == "K5":
        free = list(range(1, N))
        parts = [free[:3]] + [[k] for k in free[3:]]
        for s, part in zip(spec["quantum"], parts):
            for k in range(1, N):
                out.append((k in part, gname(s, (0, k), (1, 0))))
    elif spec["sb2"] == "K4":
        t = spec["weight1"]
        for k in range(1, N):
            out.append((k == 1, gname(t, (0, k), (1, 0))))
        qs = [s for s in spec["quantum"] if s != t]
        for s, part in zip(qs, [[2, 3, 4], [5], [6], [7]]):
            for k in range(1, N):
                out.append((k in part, gname(s, (0, k), (1, 0))))
        for i in range(2, N):
            out.append((True, gname(t, (0, i), (i, 0))))
    return out


# ----------------------------------------------------------------------------------------------- expected generator
def expected_fingerprints(spec):
    """Independently written generator of the declared families in name space (encoder name conventions for the
    auxiliary variables; constants simplified as in the note: g(p,p) = True, g = False on a common row/column)."""
    fp = FP()
    defined = set()
    Q = spec["quantum"]

    def P(x):
        return x if isinstance(x, bool) else (True, x)

    def Nn(x):
        return (not x) if isinstance(x, bool) else (False, x)

    def add(fam, lits):
        out = []
        for l in lits:
            if l is True:
                return
            if l is False:
                continue
            out.append(l)
        if not out:
            raise ValueError("expected generator produced an empty clause in " + fam)
        fp.add(fam, tuple(sorted(out)))

    def AND(name, x, y):
        if x is False or y is False:
            return False
        if x is True:
            return y
        if y is True:
            return x
        if name not in defined:
            defined.add(name)
            add("AND_DEF", [(False, name), (True, x)])
            add("AND_DEF", [(False, name), (True, y)])
            add("AND_DEF", [(True, name), (False, x), (False, y)])
        return name

    def forbid_exactly_one(fam, terms):
        for k, t in enumerate(terms):
            if t is False:
                continue
            add(fam, [Nn(t)] + [P(m) for kk, m in enumerate(terms) if kk != k])

    lines = [line_cells(lk) for lk in LINEKEYS]
    for s, u in itertools.combinations(Q, 2):                       # G2 (Prop 1)
        for p, q in itertools.combinations(CELLS, 2):
            add("G2", [Nn(gname(s, p, q)), Nn(gname(u, p, q))])
    for s in Q:                                                     # G3 (unitary transition patterns)
        for l1, l2 in itertools.combinations(lines, 2):
            for a in l1:
                add("G3", [P(gname(s, a, b)) for b in l2])
            for b in l2:
                add("G3", [P(gname(s, a, b)) for a in l1])
            for x, y in itertools.combinations(l1, 2):
                forbid_exactly_one("G3", [AND(("b3", s, x, y, z), gname(s, x, z), gname(s, y, z)) for z in l2])
            for x, y in itertools.combinations(l2, 2):
                forbid_exactly_one("G3", [AND(("b3", s, x, y, z), gname(s, z, x), gname(s, z, y)) for z in l1])
    for s in Q:                                                     # G4 (Parseval)
        for l in lines:
            ls = set(l)
            rest = [c for c in CELLS if c not in ls]
            for p, q in itertools.combinations(rest, 2):
                gpq = gname(s, p, q)
                pp, qq = (p, q) if p < q else (q, p)
                cs = [AND(("c4", s, a, pp, qq), gname(s, a, p), gname(s, a, q)) for a in l]
                for k, ck in enumerate(cs):
                    if ck is False:
                        continue
                    add("G4", [Nn(ck)] + [P(m) for kk, m in enumerate(cs) if kk != k] + [P(gpq)])
                add("G4", [Nn(gpq)] + [P(m) for m in cs])
    if spec["g5"]:                                                  # G5 (same ray)
        for s in Q:
            for l in lines:
                ls = set(l)
                for q in CELLS:
                    if q in ls:
                        continue
                    ov = [gname(s, a, q) for a in l]
                    for k, a in enumerate(l):
                        if ov[k] is False:
                            continue
                        u = ("u5", s, l[0], l[1], q, a)
                        add("G5", [(False, u), P(ov[k])])
                        for kk in range(N):
                            if kk != k:
                                add("G5", [(False, u), Nn(ov[kk])])
                        add("G5", [(True, u), Nn(ov[k])] + [P(ov[kk]) for kk in range(N) if kk != k])
                        for p in CELLS:
                            if p == q or p == a:
                                continue
                            gpq, gpa = gname(s, p, q), gname(s, p, a)
                            add("G5", [(False, u), Nn(gpq), P(gpa)])
                            add("G5", [(False, u), Nn(gpa), P(gpq)])
    for s in spec["p4_squares"]:                                    # P4 (one-way weight >= 3 flags + at-least-one)
        for fk in spec["p4_frames"]:
            fl = line_cells(fk)
            flags = []
            for p in CELLS:
                if p in fl:
                    continue
                w = ("w3", s, fk[1], p) if spec["w3_style"] == "row" else ("w3", s, fl[0], fl[1], p)
                ov = [gname(s, a, p) for a in fl]
                for K in itertools.combinations(range(N), N - 2):
                    add("P4", [(False, w)] + [P(ov[k]) for k in K])
                flags.append((True, w))
            add("P4", flags)
    if spec["rowlex"]:                                              # ROWLEX (square 1, column 0, rows 2..N-1)
        s1 = spec["quantum"][0]
        for i in range(2, N - 1):
            A = [gname(s1, (0, k), (i, 0)) for k in range(N)]
            B = [gname(s1, (0, k), (i + 1, 0)) for k in range(N)]
            e_prev = True
            for k in range(N):
                add("ROWLEX", [Nn(e_prev), Nn(A[k]), P(B[k])])
                if k < N - 1:
                    e = ("lexeq", i, k)
                    if e_prev is not True:
                        add("ROWLEX", [(False, e), P(e_prev)])
                    add("ROWLEX", [(False, e), Nn(A[k]), P(B[k])])
                    add("ROWLEX", [(False, e), P(A[k]), Nn(B[k])])
                    add("ROWLEX", [(True, e), Nn(e_prev), P(A[k]), P(B[k])])
                    add("ROWLEX", [(True, e), Nn(e_prev), Nn(A[k]), Nn(B[k])])
                    e_prev = e
    if spec["weight1"]:                                             # weight1 (at most one row-0 overlap)
        t = spec["weight1"]
        for p in CELLS:
            if p[0] == 0:
                continue
            ov = [gname(t, (0, k), p) for k in range(N)]
            for k1, k2 in itertools.combinations(range(N), 2):
                add("W1", [Nn(ov[k1]), Nn(ov[k2])])
    for sign, nm in declared_sb2_units(spec):                       # SB2 units
        add("SB2", [P(nm) if sign else Nn(nm)])
    return fp


# ----------------------------------------------------------------------------------------------- classifier
def classify(f, spec, fp):
    """Classify every clause of the regenerated stream; validate each instance against the family's declared domain."""
    nv = f.nv
    names = [None] * (nv + 1)
    for nm, v in f.names.items():
        if not (1 <= v <= nv) or names[v] is not None:
            raise RuntimeError("name table is not a bijection onto 1..nv")
        names[v] = nm
    if any(names[v] is None for v in range(1, nv + 1)):
        raise RuntimeError("variable without a name")
    vid = f.names
    kind = [None] + [nm[0] for nm in names[1:]]
    err = Counter()
    err_ex = defaultdict(list)
    fam_c = Counter()
    sub_c = Counter()

    def bad(tag, cl):
        err[tag] += 1
        if len(err_ex[tag]) < 4:
            err_ex[tag].append([[l > 0, names[abs(l)]] for l in cl])

    # ---- variable-level checks (C2/C3)
    kinds_present = Counter(kind[1:])
    gcount = Counter()
    for v in range(1, nv + 1):
        nm = names[v]
        if nm[0] == "g":
            s, a, b = nm[1], nm[2], nm[3]
            if not (a < b) or a == b or collinear(a, b) or s not in spec["quantum"]:
                err["C2_bad_g_name"] += 1
            gcount[s] += 1
    npairs = sum(1 for p, q in itertools.combinations(CELLS, 2) if not collinear(p, q))
    g_complete = all(gcount[s] == npairs for s in spec["quantum"])
    missing_g = 0
    for s in spec["quantum"]:
        for p, q in itertools.combinations(CELLS, 2):
            if not collinear(p, q) and ("g", s, p, q) not in vid:
                missing_g += 1

    and_defs = {}          # AND var -> [posA, posB, rev]
    u5_state = {}          # u5 var -> [D1, D3, set(a' defined negative)]
    flags_oneway = defaultdict(list)   # w3 var -> list of frame-position bitmasks
    flag_alo = Counter()   # w3 var -> number of at-least-one clauses containing it positively
    p4_alo = []            # (clause index, s, frame)
    sb2_units = []         # (clause index, sign, name)
    lex_groups = defaultdict(list)     # i -> list of clauses as [(sign, ('A'|'B'|'e', k))]
    g2_pairs = Counter()
    w1_cells = Counter()
    g3_rows = Counter()

    def w3_frame(v):
        nm = names[v]
        if len(nm) == 4:
            s, r, p = nm[1], nm[2], nm[3]
            lk = ("R", r)
        else:
            s, f0, f1, p = nm[1], nm[2], nm[3], nm[4]
            lk = lk_of([f0, f1])
            if lk is None or line_cells(lk)[:2] != [f0, f1]:
                return None
        if on_line(p, lk):
            return None
        return s, lk, p

    def operands(v):
        nm = names[v]
        if nm[0] == "b3":
            s, x, y, z = nm[1:]
            if not (x < y and collinear(x, y)):
                return None
            o = (gname(s, x, z), gname(s, y, z))
        else:
            s, a, p, q = nm[1:]
            if not (p < q):
                return None
            o = (gname(s, a, p), gname(s, a, q))
        if any(isinstance(x, bool) for x in o):
            return None
        return (vid.get(o[0]), vid.get(o[1]))

    s1 = spec["quantum"][0]
    for idx, cl in enumerate(f.clauses):
        key = tuple(sorted((l > 0, names[abs(l)]) for l in cl))
        if not cl:
            bad("EMPTY", cl)
            fp.add("EMPTY", key)
            continue
        ks = {kind[abs(l)] for l in cl}
        fam = None
        sub = None
        if len(cl) == 1:
            l = cl[0]
            k0 = kind[abs(l)]
            if k0 == "g":
                fam, sub = "SB2", "unit"
                sb2_units.append((idx, l > 0, names[abs(l)]))
            elif k0 == "lexeq" and l > 0 and names[l][2] == 0 and spec["rowlex"]:
                fam, sub = "ROWLEX", "e0_unit"
                lex_groups[names[l][1]].append([(True, ("e", 0))])
            else:
                bad("UNMAPPED_unit", cl)
        elif "w3" in ks:
            ws = [l for l in cl if kind[abs(l)] == "w3"]
            if ks == {"w3"} and all(l > 0 for l in cl):
                infos = [w3_frame(l) for l in cl]
                if any(x is None for x in infos) or len({(x[0], x[1]) for x in infos}) != 1:
                    bad("P4_alo_mixed", cl)
                else:
                    s, lk = infos[0][0], infos[0][1]
                    ps = [x[2] for x in infos]
                    if len(set(ps)) != len(ps) or set(ps) != {c for c in CELLS if not on_line(c, lk)}:
                        bad("P4_alo_domain", cl)
                    else:
                        fam, sub = "P4", "alo"
                        p4_alo.append((idx, s, lk))
                        for l in cl:
                            flag_alo[l] += 1
            elif ks == {"w3", "g"} and len(ws) == 1 and ws[0] < 0 and all(l > 0 for l in cl if l != ws[0]):
                inf = w3_frame(-ws[0])
                ok = inf is not None
                if ok:
                    s, lk, p = inf
                    fcells = line_cells(lk)
                    mask = 0
                    for l in cl:
                        if l == ws[0]:
                            continue
                        nm = names[l]
                        if nm[1] != s or p not in (nm[2], nm[3]):
                            ok = False
                            break
                        a = nm[3] if nm[2] == p else nm[2]
                        if not on_line(a, lk):
                            ok = False
                            break
                        mask |= 1 << fcells.index(a)
                if ok:
                    fam, sub = "P4", "oneway"
                    flags_oneway[-ws[0]].append(mask)
                else:
                    bad("P4_oneway_domain", cl)
            else:
                bad("UNMAPPED_w3", cl)
        elif "lexeq" in ks:
            if not ks <= {"lexeq", "g"} or not spec["rowlex"]:
                bad("UNMAPPED_lexeq", cl)
            else:
                iset = {names[abs(l)][1] for l in cl if kind[abs(l)] == "lexeq"}
                ok = len(iset) == 1
                i = next(iter(iset))
                ok = ok and 2 <= i <= N - 2
                sym = []
                for l in cl:
                    nm = names[abs(l)]
                    if nm[0] == "lexeq":
                        if not (0 <= nm[2] <= N - 2):
                            ok = False
                        sym.append((l > 0, ("e", nm[2])))
                    else:
                        s, a, b = nm[1:]
                        if s != s1 or a[0] != 0 or b not in ((i, 0), (i + 1, 0)):
                            ok = False
                            break
                        sym.append((l > 0, ("A" if b == (i, 0) else "B", a[1])))
                if ok:
                    fam, sub = "ROWLEX", "chain"
                    lex_groups[i].append(sym)
                else:
                    bad("ROWLEX_domain", cl)
        elif "u5" in ks:
            us = [l for l in cl if kind[abs(l)] == "u5"]
            if not ks <= {"u5", "g"} or len(us) != 1:
                bad("UNMAPPED_u5", cl)
            else:
                u = us[0]
                nm = names[abs(u)]
                s, l0, l1, q, a = nm[1:]
                lk = lk_of([l0, l1])
                ok = lk is not None and line_cells(lk)[:2] == [l0, l1] and not on_line(q, lk) and on_line(a, lk) \
                    and not collinear(a, q)
                gl = []
                for l in cl:
                    if l == u:
                        continue
                    g = names[abs(l)]
                    if g[1] != s:
                        ok = False
                    gl.append((l > 0, g[2], g[3]))
                if ok:
                    lcells = line_cells(lk)
                    Aq = {b for b in lcells if b != a and not collinear(b, q)}
                    st = u5_state.setdefault(abs(u), [0, 0, set()])
                    pos = [x for x in gl if x[0]]
                    negs = [x for x in gl if not x[0]]
                    pair = lambda x: {x[1], x[2]}
                    if u < 0 and len(gl) == 1 and pos and pair(pos[0]) == {a, q}:
                        sub = "def_pos"
                        st[0] += 1
                    elif u > 0 and len(negs) == 1 and pair(negs[0]) == {a, q} and \
                            sorted(tuple(sorted(pair(x) - {q})) for x in pos) == sorted((b,) for b in Aq) and \
                            all(q in pair(x) for x in pos):
                        sub = "def_rev"
                        st[1] += 1
                    elif u < 0 and len(gl) == 1 and negs:
                        c, d = negs[0][1], negs[0][2]
                        if q in (c, d):
                            p = d if c == q else c
                            okn = p not in (q, a) and collinear(p, a) and not collinear(p, q)
                        elif a in (c, d):
                            p = d if c == a else c
                            okn = p not in (q, a) and collinear(p, q) and not collinear(p, a)
                        else:
                            okn = False
                        if okn:
                            sub = "neg"
                            if q in (c, d) and p in Aq:
                                st[2].add(p)
                        else:
                            ok = False
                    elif u < 0 and len(gl) == 2 and len(pos) == 1 and len(negs) == 1:
                        pn, pp = pair(negs[0]), pair(pos[0])
                        cand = pn & pp
                        okq = False
                        if len(cand) == 1:
                            p = next(iter(cand))
                            rest = sorted([tuple(pn - {p}), tuple(pp - {p})])
                            okq = p not in (q, a) and not collinear(p, q) and not collinear(p, a) and \
                                rest == sorted([(q,), (a,)])
                        if okq:
                            sub = "eq"
                        else:
                            ok = False
                    else:
                        ok = False
                if ok:
                    fam = "G5"
                else:
                    bad("G5_domain", cl)
        elif ks & {"b3", "c4"}:
            andl = [l for l in cl if kind[abs(l)] in ("b3", "c4")]
            gls = [l for l in cl if kind[abs(l)] == "g"]
            if "b3" in ks and "c4" in ks or not ks <= {"b3", "c4", "g"}:
                bad("UNMAPPED_and_mix", cl)
            elif len(andl) == 1 and ((len(cl) == 2 and andl[0] < 0 and gls[0] > 0) or
                                     (len(cl) == 3 and andl[0] > 0 and all(l < 0 for l in gls))):
                v = abs(andl[0])
                ops = operands(v)
                st = and_defs.setdefault(v, [0, 0, 0])
                if ops is None or None in ops:
                    bad("AND_def_operands", cl)
                elif len(cl) == 2 and gls[0] in ops:
                    fam, sub = "AND_DEF", kind[v]
                    st[ops.index(gls[0])] += 1
                elif len(cl) == 3 and sorted(-l for l in gls) == sorted(ops):
                    fam, sub = "AND_DEF", kind[v]
                    st[2] += 1
                else:
                    bad("AND_def_shape", cl)
            elif ks == {"b3"}:
                nms = [names[abs(l)] for l in cl]
                negc = sum(1 for l in cl if l < 0)
                sxy = {(nm[1], nm[2], nm[3]) for nm in nms}
                zs = [nm[4] for nm in nms]
                lk = lk_of(zs)
                ok = negc == 1 and len(sxy) == 1 and lk is not None and len(set(zs)) == len(zs)
                if ok:
                    s, x, y = next(iter(sxy))
                    exp = {z for z in line_cells(lk) if z not in (x, y) and not collinear(z, x) and not collinear(z, y)}
                    ok = collinear(x, y) and x < y and set(zs) == exp
                if ok:
                    fam, sub = "G3", "exactly_one_forbidden"
                else:
                    bad("G3_x1f_domain", cl)
            elif ks <= {"c4", "g"} and len(gls) <= 1:
                nms = [names[abs(l)] for l in andl]
                spq = {(nm[1], nm[3], nm[4]) for nm in nms}
                As = [nm[2] for nm in nms]
                lk = lk_of(As)
                ok = len(spq) == 1 and lk is not None and len(set(As)) == len(As)
                if ok:
                    s, p, q = next(iter(spq))
                    exp = {a for a in line_cells(lk) if not collinear(a, p) and not collinear(a, q)}
                    ok = not on_line(p, lk) and not on_line(q, lk) and set(As) == exp
                if ok:
                    negc = sum(1 for l in andl if l < 0)
                    if collinear(p, q):
                        ok = not gls and negc == 1
                        sub = "single_term_collinear"
                    elif gls:
                        gn = names[abs(gls[0])]
                        ok = gn == ("g", s, p, q)
                        if gls[0] > 0 and negc == 1:
                            sub = "single_term"
                        elif gls[0] < 0 and negc == 0:
                            sub = "zero"
                        else:
                            ok = False
                    else:
                        ok = False
                if ok:
                    fam = "G4"
                else:
                    bad("G4_domain", cl)
            else:
                bad("UNMAPPED_and", cl)
        elif ks == {"g"}:
            gl = [(l > 0,) + names[abs(l)][1:] for l in cl]
            if all(x[0] for x in gl):
                s = gl[0][1]
                common = {gl[0][2], gl[0][3]}
                for x in gl[1:]:
                    common &= {x[2], x[3]}
                ok = all(x[1] == s for x in gl) and len(common) == 1
                if ok:
                    c = next(iter(common))
                    others = [x[3] if x[2] == c else x[2] for x in gl]
                    lk = lk_of(others)
                    ok = lk is not None and not on_line(c, lk) and len(set(others)) == len(others) and \
                        set(others) == {y for y in line_cells(lk) if not collinear(c, y)}
                if ok:
                    fam, sub = "G3", "nonempty"
                    g3_rows[(s, c, lk)] += 1
                else:
                    bad("G3_nonempty_domain", cl)
            elif len(gl) == 2 and not gl[0][0] and not gl[1][0]:
                (_, s, a, b), (_, u, a2, b2) = gl
                if (a, b) == (a2, b2) and s != u:
                    fam, sub = "G2", "pair"
                    g2_pairs[(min(s, u), max(s, u))] += 1
                elif s == u and s == spec["weight1"]:
                    common = {a, b} & {a2, b2}
                    if len(common) == 1:
                        p = next(iter(common))
                        o1 = a if b == p else b
                        o2 = a2 if b2 == p else b2
                        if p[0] != 0 and o1[0] == 0 and o2[0] == 0 and o1 != o2:
                            fam, sub = "W1", "at_most_one"
                            w1_cells[p] += 1
                if fam is None:
                    bad("UNMAPPED_g_binary", cl)
            else:
                bad("UNMAPPED_g", cl)
        else:
            bad("UNMAPPED_kinds", cl)
        if fam is None:
            fp.add("UNMAPPED", key)
        else:
            fp.add(fam, key)
            fam_c[fam] += 1
            sub_c[fam + "/" + str(sub)] += 1
        if idx % 1000000 == 0:
            log("classified", idx)

    res = {"kinds_present": dict(kinds_present), "g_vars_per_square": {str(k): v for k, v in sorted(gcount.items())},
           "g_pairs_expected_per_square": npairs, "g_complete": g_complete, "g_missing": missing_g,
           "family_counts": dict(fam_c), "subfamily_counts": dict(sorted(sub_c.items()))}
    # ---- AND definitions complete and unique (full equivalence; memo keys consistent)
    and_vars = [v for v in range(1, nv + 1) if kind[v] in ("b3", "c4")]
    and_bad = [v for v in and_vars if and_defs.get(v) != [1, 1, 1]]
    res["and_vars"] = {"b3": sum(1 for v in and_vars if kind[v] == "b3"), "c4": sum(1 for v in and_vars if kind[v] == "c4"),
                       "not_exactly_one_definition_triple": len(and_bad),
                       "examples": [[names[v], and_defs.get(v)] for v in and_bad[:4]]}
    # ---- u5 definitions complete
    u5_vars = [v for v in range(1, nv + 1) if kind[v] == "u5"]
    u5_bad = []
    for v in u5_vars:
        st = u5_state.get(v)
        nm = names[v]
        s, l0, l1, q, a = nm[1:]
        Aq = {b for b in line_cells(lk_of([l0, l1])) if b != a and not collinear(b, q)}
        if st is None or st[0] != 1 or st[1] != 1 or st[2] != Aq:
            u5_bad.append(v)
    res["u5_vars"] = {"count": len(u5_vars), "incomplete_or_duplicated_definitions": len(u5_bad),
                      "examples": [names[v] for v in u5_bad[:4]]}
    # ---- P4
    w3_vars = [v for v in range(1, nv + 1) if kind[v] == "w3"]
    frames = Counter((s, lk) for _, s, lk in p4_alo)
    gadget_bad = []
    oneway_sizes = Counter()
    for v in w3_vars:
        inf = w3_frame(v)
        if inf is None:
            gadget_bad.append([names[v], "bad name/frame"])
            continue
        s, lk, p = inf
        fcells = line_cells(lk)
        const = [k for k, a in enumerate(fcells) if collinear(a, p)]
        masks = flags_oneway.get(v, [])
        oneway_sizes[len(masks)] += 1
        okg = len(const) == 1 and flag_alo[v] == 1
        if okg:
            j0 = const[0]
            for x in range(1 << N):
                if (x >> j0) & 1:
                    continue
                sat = all(x & m for m in masks)
                if sat != (bin(x).count("1") >= 3):
                    okg = False
                    break
        if not okg:
            gadget_bad.append([names[v], len(masks), flag_alo[v]])
    exp_frames = {(s, fk) for s in spec["p4_squares"] for fk in spec["p4_frames"]}
    res["p4"] = {"at_least_one_clauses": len(p4_alo),
                 "at_least_one_by_square_frame": sorted([[s, list(lk), c] for (s, lk), c in frames.items()]),
                 "declared_square_frames": len(exp_frames),
                 "square_frames_equal_declared": set(frames) == exp_frames and all(c == 1 for c in frames.values()),
                 "squares_with_alo": sorted({s for (s, lk) in frames}),
                 "frames_with_alo": sorted({lk for (s, lk) in frames}),
                 "w3_vars": len(w3_vars), "w3_flags_per_alo_clause": N * N - N,
                 "oneway_clauses_per_flag_histogram": {str(k): v for k, v in oneway_sizes.items()},
                 "gadget_exhaustive": {"flags_checked": len(w3_vars), "flags_failing": len(gadget_bad),
                                       "rule": "for every flag, every 0/1 pattern of its 7 non-constant frame overlaps: "
                                               "w=1 satisfies all its one-way clauses <=> weight >= 3",
                                       "examples": gadget_bad[:4]},
                 "alo_clause_indices": [i for i, _, _ in p4_alo]}
    # ---- ROWLEX semantics (exhaustive over A, B)
    lex = {"groups": sorted(lex_groups), "clauses_per_group": {str(i): len(c) for i, c in sorted(lex_groups.items())}}
    lex_fail = []
    for i, cls in sorted(lex_groups.items()):
        for xa in range(1 << (N - 1)):
            A = [False] + [bool((xa >> (k - 1)) & 1) for k in range(1, N)]
            for xb in range(1 << (N - 1)):
                B = [False] + [bool((xb >> (k - 1)) & 1) for k in range(1, N)]
                e = []
                eq = True
                for k in range(N - 1):
                    eq = eq and (A[k] == B[k])
                    e.append(eq)
                env = {"A": A, "B": B, "e": e}
                sat = all(any((env[t][k] if sg else not env[t][k]) for sg, (t, k) in c) for c in cls)
                if sat != (tuple(A) <= tuple(B)):
                    lex_fail.append([i, xa, xb])
                    break
            if lex_fail and lex_fail[-1][0] == i:
                break
    lex["exhaustive_rule"] = ("under the defining values of the lexeq chain, all ROWLEX clauses of pair (i, i+1) hold "
                              "<=> (g_1((0,k),(i,0)))_k <=lex (g_1((0,k),(i+1,0)))_k, k = 0 most significant")
    lex["failures"] = lex_fail
    lex["lexeq_vars"] = sum(1 for v in range(1, nv + 1) if kind[v] == "lexeq")
    res["rowlex"] = lex
    # ---- SB2 units vs declared
    actual_units = Counter((sg, nm) for _, sg, nm in sb2_units)
    decl = Counter(declared_sb2_units(spec))
    res["sb2"] = {"unit_clauses_on_g": len(sb2_units), "declared": len(decl),
                  "equal_to_declared": actual_units == decl,
                  "extra": [[sg, nm] for (sg, nm), c in (actual_units - decl).items()],
                  "missing": [[sg, nm] for (sg, nm), c in (decl - actual_units).items()],
                  "units": sorted([[sg, nm] for (sg, nm) in actual_units])}
    res["sb2_unit_index"] = [[i, sg, nm] for i, sg, nm in sb2_units]
    # ---- G2 / weight1 / G3 nonempty
    res["g2"] = {"square_pairs": sorted([[a, b, c] for (a, b), c in g2_pairs.items()]),
                 "all_10_pairs": len(g2_pairs) == len(list(itertools.combinations(spec["quantum"], 2))),
                 "per_pair_expected": npairs, "all_pairs_complete": all(c == npairs for c in g2_pairs.values())}
    off0 = [c for c in CELLS if c[0] != 0]
    res["weight1"] = {"cells_with_clauses": len(w1_cells), "off_row0_cells": len(off0),
                      "per_cell_counts": sorted(set(w1_cells.values())),
                      "expected_per_cell": (N - 1) * (N - 2) // 2,
                      "all_cells_complete": spec["weight1"] is not None and set(w1_cells) == set(off0) and
                      all(c == (N - 1) * (N - 2) // 2 for c in w1_cells.values())}
    res["g3_nonempty_multiplicity"] = sorted(set(g3_rows.values()))
    res["errors"] = dict(err)
    res["error_examples"] = {k: v for k, v in err_ex.items()}
    return res, names


# ----------------------------------------------------------------------------------------------- classical control
def gf8_mul():
    """GF(8) = GF(2)[x]/(x^3 + x + 1), elements as bit vectors (bit k = coefficient of x^k); field axioms checked."""
    def xtime(a):
        a <<= 1
        return a ^ 0b1011 if a & 0b1000 else a

    def mul(a, b):
        r, t = 0, a
        for k in range(3):
            if (b >> k) & 1:
                r ^= t
            t = xtime(t)
        return r

    E = range(8)
    for a in E:
        assert mul(a, 1) == a and mul(a, 0) == 0
        if a:
            assert sum(1 for b in E if mul(a, b) == 1) == 1
        for b in E:
            assert mul(a, b) == mul(b, a)
            for c in E:
                assert mul(mul(a, b), c) == mul(a, mul(b, c))
                assert mul(a, b ^ c) == mul(a, b) ^ mul(a, c)
    return mul


def classical_control(mode):
    """Five MOLS(8) from AG(2,8): L_m(i,j) = j + m*i (m in GF(8)*), cell (i,j) = point (x=i, y=j); normalised as the
    mode requires.  Returns (squares dict s -> {cell: symbol}, report)."""
    assert N == 8
    mul = gf8_mul()
    Ls = {m: {(i, j): j ^ mul(m, i) for i in range(8) for j in range(8)} for m in range(1, 8)}
    rep = {"field": "GF(8)=GF(2)[x]/(x^3+x+1); field axioms checked exhaustively"}
    lat = all(len({L[(i, j)] for j in range(8)}) == 8 and len({L[(j, i)] for j in range(8)}) == 8
              for L in Ls.values() for i in range(8))
    orth = all(len({(Ls[a][c], Ls[b][c]) for c in CELLS}) == 64 for a, b in itertools.combinations(Ls, 2))
    plane = True
    for p, q in itertools.combinations(CELLS, 2):
        n = (p[0] == q[0]) + (p[1] == q[1]) + sum(Ls[m][p] == Ls[m][q] for m in Ls)
        plane &= n == 1
    rep.update(all7_latin=lat, all21_pairs_orthogonal=orth, affine_plane_9_classes_every_pair_once=plane)
    if mode == "K5":
        slopes = {1: 1, 2: 4, 3: 5, 4: 6, 5: 7}
        perm = [0, 1, 7, 6, 5, 4, 3, 2]          # new row i <- old row perm[i]
    else:
        slopes = {1: 2, 2: 5, 3: 6, 4: 7, 5: 1}  # square 5 = L (weight-1 square), slope 1: L(i,0) = i
        perm = list(range(8))
    sq = {s: {(i, j): Ls[m][(perm[i], j)] for i in range(8) for j in range(8)} for s, m in slopes.items()}
    rep["slopes_by_square"] = slopes
    rep["row_permutation_new_from_old"] = perm
    # quantum view: Psi_s(p) = e_{L_s(p)}; exact integer checks
    vec = lambda x: tuple(1 if t == x else 0 for t in range(8))
    dot = lambda u, v: sum(a * b for a, b in zip(u, v))
    qls = True
    for s in sq:
        for lk in LINEKEYS:
            vs = [vec(sq[s][c]) for c in line_cells(lk)]
            qls &= all(dot(vs[a], vs[b]) == (1 if a == b else 0) for a in range(8) for b in range(8))
    mutual = True
    for s, u in itertools.combinations(sq, 2):
        tens = [tuple(x * y for x in vec(sq[s][c]) for y in vec(sq[u][c])) for c in CELLS]
        mutual &= all(dot(tens[a], tens[b]) == (1 if a == b else 0) for a in range(64) for b in range(64))
    std = all(sq[s][(0, j)] == j for s in sq for j in range(8))
    rep.update(qls_rows_cols_onb=qls, mutually_orthogonal_tensor_onb_all_10_pairs=mutual, row0_standard_form=std)
    gram = {s: {(p, q): dot(vec(sq[s][p]), vec(sq[s][q])) != 0 for p, q in itertools.combinations(CELLS, 2)} for s in sq}
    if mode == "K5":
        col = [sq[1][(i, 0)] for i in range(8)]
        vrows = [tuple(gram[1][((0, k), (i, 0))] for k in range(8)) for i in range(2, 8)]
        rep["square1_column0"] = col
        rep["rowlex_vectors_nondecreasing_rows2to7"] = all(vrows[t] <= vrows[t + 1] for t in range(5))
        rep["supports_at_10"] = {s: sorted(k for k in range(1, 8) if gram[s][((0, k), (1, 0))]) for s in sq}
    else:
        rep["L_column0"] = [sq[5][(i, 0)] for i in range(8)]
        rep["L_10_is_1_and_Li0_is_i"] = sq[5][(1, 0)] == 1 and all(sq[5][(i, 0)] == i for i in range(2, 8))
        rep["supports_at_10"] = {s: sorted(k for k in range(1, 8) if gram[s][((0, k), (1, 0))]) for s in sq}
    rep["squares"] = {s: [[sq[s][(i, j)] for j in range(8)] for i in range(8)] for s in sq}
    return gram, rep


def canonical_values(names, gram, spec):
    def G(s, p, q):
        if p == q:
            return True
        a, b = (p, q) if p < q else (q, p)
        return gram[s][(a, b)]

    val = bytearray(len(names))
    for v in range(1, len(names)):
        nm = names[v]
        k = nm[0]
        if k == "g":
            x = gram[nm[1]][(nm[2], nm[3])]
        elif k == "b3":
            s, x_, y_, z = nm[1:]
            x = G(s, x_, z) and G(s, y_, z)
        elif k == "c4":
            s, a, p, q = nm[1:]
            x = G(s, a, p) and G(s, a, q)
        elif k == "u5":
            s, l0, l1, q, a = nm[1:]
            x = G(s, a, q) and not any(G(s, b, q) for b in line_cells(lk_of([l0, l1])) if b != a)
        elif k == "w3":
            if len(nm) == 4:
                s, lk, p = nm[1], ("R", nm[2]), nm[3]
            else:
                s, lk, p = nm[1], lk_of([nm[2], nm[3]]), nm[4]
            x = sum(1 for a in line_cells(lk) if G(s, a, p)) >= 3
        elif k == "lexeq":
            i, kk = nm[1], nm[2]
            x = all(G(1, (0, t), (i, 0)) == G(1, (0, t), (i + 1, 0)) for t in range(kk + 1))
        else:
            raise RuntimeError("no canonical value for " + repr(nm))
        val[v] = 1 if x else 0
    return val


def evaluate(clauses, val, skip=frozenset()):
    bad = []
    for idx, cl in enumerate(clauses):
        if idx in skip:
            continue
        if not any((val[l] if l > 0 else not val[-l]) for l in cl):
            bad.append(idx)
    return bad


def kissat_meta():
    path = shutil.which("kissat")
    ver = subprocess.run([path, "--version"], capture_output=True, text=True).stdout.strip()
    return {"path": path, "realpath": os.path.realpath(path), "sha256": sha_file(os.path.realpath(path))[0], "version": ver}


def run_kissat(nv, clauses, drop, units, label):
    """Instance = clauses (except indices in drop) + unit clauses; bytes built in memory and piped to kissat."""
    check_disk()
    kept = len(clauses) - len(drop)
    chunks = [("p cnf %d %d\n" % (nv, kept + len(units))).encode()]
    buf = []
    for idx, cl in enumerate(clauses):
        if idx in drop:
            continue
        buf.append(" ".join(map(str, cl)) + " 0\n")
        if len(buf) == 65536:
            chunks.append("".join(buf).encode())
            buf = []
    buf += ["%d 0\n" % u for u in units]
    chunks.append("".join(buf).encode())
    data = b"".join(chunks)
    del chunks, buf
    inst_sha = hashlib.sha256(data).hexdigest()
    argv = [shutil.which("kissat"), "--time=%d" % SOLVER_TIME, "-q"]
    t = time.time()
    log("kissat", label, "bytes", len(data))
    p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errb = p.communicate(input=data)
    secs = time.time() - t
    del data
    out = out.decode()
    status = [ln for ln in out.splitlines() if ln.startswith("s ")]
    model = None
    check = None
    if p.returncode == 10:
        model = bytearray(nv + 1)
        seen = 0
        for ln in out.splitlines():
            if ln.startswith("v "):
                for tok in ln[2:].split():
                    x = int(tok)
                    if x == 0:
                        continue
                    model[abs(x)] = 1 if x > 0 else 0
                    seen += 1
        viol = 0
        for idx, cl in enumerate(clauses):
            if idx in drop:
                continue
            if not any((model[l] if l > 0 else not model[-l]) for l in cl):
                viol += 1
        uviol = sum(1 for u in units if not (model[u] if u > 0 else not model[-u]))
        check = {"model_literals": seen, "instance_clauses_violated_by_model": viol, "units_violated_by_model": uviol}
    return {"label": label, "argv": argv + ["<stdin>"], "instance_sha256": inst_sha, "instance_vars": nv,
            "instance_clauses": kept + len(units), "dropped_clauses": len(drop), "added_units": len(units),
            "returncode": p.returncode, "status_lines": status, "seconds": round(secs, 2),
            "stderr_tail": errb.decode()[-400:], "model_check": check}


def gadget_solver_tests(f, names, flags):
    """Tiny CNFs from the ACTUAL one-way clauses of a few flags: w=1 + all 7 non-constant overlaps fixed."""
    out = []
    want = set(flags)
    per = defaultdict(list)
    for cl in f.clauses:
        if len(cl) >= 2 and cl[0] < 0 and -cl[0] in want and names[-cl[0]][0] == "w3":
            if all(l > 0 and names[l][0] == "g" for l in cl[1:]):
                per[-cl[0]].append(cl)
    for w in flags:
        cls = per[w]
        ovs = sorted({l for cl in cls for l in cl[1:]})
        ren = {w: 1}
        for k, g in enumerate(ovs):
            ren[g] = k + 2
        for ones in (2, 3):
            units = [1] + [(k + 2) if k < ones else -(k + 2) for k in range(len(ovs))]
            body = ["p cnf %d %d\n" % (len(ovs) + 1, len(cls) + len(units))]
            for cl in cls:
                body.append(" ".join(str(ren[abs(l)] if l > 0 else -ren[abs(l)]) for l in cl) + " 0\n")
            body += ["%d 0\n" % u for u in units]
            data = "".join(body).encode()
            p = subprocess.Popen([shutil.which("kissat"), "--time=60", "-q"], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o, _ = p.communicate(input=data)
            out.append({"flag": names[w], "one_way_clauses": len(cls), "nonconstant_overlaps": len(ovs),
                        "nonzero_overlaps": ones, "returncode": p.returncode,
                        "status": [ln for ln in o.decode().splitlines() if ln.startswith("s ")],
                        "expected": 20 if ones == 2 else 10, "instance_sha256": hashlib.sha256(data).hexdigest()})
    return out


# ----------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", choices=["K5", "K4"], required=True)
    ap.add_argument("--flag-variant", action="store_true", help="encoder argv with --p4 none and without --sb2")
    ap.add_argument("--base-json", default=None, help="base result JSON for the family cross-comparison")
    ap.add_argument("--out", required=True)
    ap.add_argument("--names-out", default=None)
    ap.add_argument("--solve", action="store_true")
    a = ap.parse_args()
    check_disk()
    T = TARGETS[a.target]
    res = {"target": a.target, "flag_variant": a.flag_variant, "started": now(), "python": sys.version,
           "driver_sha256": sha_file(os.path.abspath(__file__))[0]}
    enc = os.path.join(HERE, T["encoder"])
    res["encoder"] = {"path": enc, "sha256": sha_file(enc)[0]}
    lane_map = json.load(open(T["lane_map"]))
    res["lane_map"] = {"path": T["lane_map"], "sha256": sha_file(T["lane_map"])[0], "meta": lane_map["meta"]}
    argv = list(lane_map["meta"]["argv"])
    tag = a.target + (".flagvariant" if a.flag_variant else "")
    if a.flag_variant:
        i = argv.index("--p4")
        argv[i + 1] = "none"
        argv.remove("--sb2")
    for opt, ext in (("--cnf", ".cnf"), ("--map", ".map.json")):
        i = argv.index(opt)
        argv[i + 1] = os.path.join(OUTDIR, "never-written." + tag + ext)
    res["encoder_argv_used"] = argv
    log("regenerating", tag)
    box = regenerate(enc, argv)
    f = box["f"]
    for opt in ("--cnf", "--map"):
        assert not os.path.exists(argv[argv.index(opt) + 1])
    res["build_call"] = {"args": box["args"], "kwargs": box["kwargs"]}
    log("built nv", f.nv, "clauses", len(f.clauses), "maxrss", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    sha, nbytes = dimacs_sha(f)
    res["regenerated"] = {"sha256": sha, "bytes": nbytes, "vars": f.nv, "clauses": len(f.clauses)}
    if not a.flag_variant:
        st_sha, st_bytes = sha_file(T["stored"])
        stt = os.stat(T["stored"])
        res["stored"] = {"path": T["stored"], "sha256": st_sha, "bytes": st_bytes,
                         "mtime": datetime.datetime.fromtimestamp(stt.st_mtime).astimezone().isoformat(timespec="seconds")}
        res["C1_byte_identity"] = {
            "regenerated_eq_declared": sha == T["declared_sha256"], "declared_where": T["declared_where"],
            "regenerated_eq_map_meta": sha == lane_map["meta"]["cnf_sha256"],
            "regenerated_eq_stored_file": sha == st_sha and nbytes == st_bytes,
            "header_eq_declared": [f.nv, len(f.clauses)] == [T["declared_vars"], T["declared_clauses"]],
            "encoder_sha_eq_map_meta": res["encoder"]["sha256"] == lane_map["meta"]["script_sha256"]}
        mine = {json.dumps(k): v for k, v in f.names.items() if isinstance(k, tuple) and k[0] in ("g",)
                or isinstance(k, tuple) and isinstance(k[0], str) and k[0].startswith("L")}
        res["map_vars_equal_lane_map"] = mine == lane_map["vars"]
        res["map_vars_count"] = len(mine)
    log("sha", sha, nbytes)
    spec = declared_spec(a.target, a.flag_variant)
    res["declared_spec"] = {k: (v if not isinstance(v, list) else [list(x) if isinstance(x, tuple) else x for x in v])
                            for k, v in spec.items()}
    fp_actual = FP()
    cres, names = classify(f, spec, fp_actual)
    res["classification"] = cres
    log("classified; errors", cres["errors"])
    if a.names_out:
        with open(a.names_out, "xb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as gz:
                gz.write(json.dumps([[v, names[v]] for v in range(1, f.nv + 1)]).encode())
        res["names_table"] = {"path": a.names_out, "sha256": sha_file(a.names_out)[0]}
    fp_exp = expected_fingerprints(spec)
    fa, fe = fp_actual.as_json(), fp_exp.as_json()
    res["family_fingerprints"] = {"actual": fa, "expected": fe,
                                  "equal_per_family": {k: fa.get(k) == fe.get(k) for k in sorted(set(fa) | set(fe))},
                                  "multiset_equal": fa == fe}
    log("fingerprints equal", fa == fe)
    if a.base_json:
        base = json.load(open(a.base_json))
        bfa = base["family_fingerprints"]["actual"]
        res["vs_base"] = {"base_json": a.base_json, "base_json_sha256": sha_file(a.base_json)[0],
                          "shared_families_equal": {k: fa.get(k) == bfa.get(k) for k in sorted(set(fa) | set(bfa))}}
    if a.target == "K5" and not a.flag_variant:
        chain = {1: (1, 2), 2: (1, 3), 3: (1, 4), 4: (1, 5), 5: (1, 6), 6: (1, 7), 7: (2, 2), 8: (2, 3)}
        declared = {1: [57, 106, 155, 204, 253, 302, 351], 2: [64, 113, 162, 211, 260, 309, 358],
                    3: [71, 120, 169, 218, 267, 316, 365], 4: [78, 127, 176, 225, 274, 323, 372],
                    5: [85, 134, 183, 232, 281, 330, 379], 6: [92, 141, 190, 239, 288, 337, 386],
                    7: [1625, 1674, 1723, 1772, 1821, 1870, 1919], 8: [1632, 1681, 1730, 1779, 1828, 1877, 1926]}
        got = {d: [f.names[("g", s, (0, k), (r, 0))] for k in range(1, 8)] for d, (s, r) in chain.items()}
        res["split_lists_V1_V8"] = {"semantics": "V_d = g_s((0,k),(r,0)), k = 1..7; (s, r) = " + json.dumps(chain),
                                    "ids_from_regenerated_name_table": got,
                                    "equal_to_README_8_8.1": got == declared,
                                    "all_le_nv": all(x <= f.nv for v in got.values() for x in v)}
    # ---- classical control (C12)
    gram, crep = classical_control(a.target)
    res["c12_classical_set"] = crep
    val = canonical_values(names, gram, spec)
    viol = evaluate(f.clauses, val)
    alo = set(cres["p4"]["alo_clause_indices"])
    unit_idx = {i: (sg, nm) for i, sg, nm in cres["sb2_unit_index"]}
    vdesc = Counter()
    vlist = []
    for i in viol:
        if i in alo:
            vdesc["P4_at_least_one"] += 1
        elif i in unit_idx:
            vdesc["SB2_unit"] += 1
            vlist.append(list(unit_idx[i]))
        else:
            vdesc["OTHER"] += 1
            vlist.append([[l > 0, names[abs(l)]] for l in f.clauses[i]])
    res["c12_canonical_assignment"] = {"violated_clauses": len(viol), "by_kind": dict(vdesc), "violated_non_p4": vlist}
    log("canonical violations", dict(vdesc))
    gvars = [v for v in range(1, f.nv + 1) if names[v][0] == "g"]
    gunits = [v if val[v] else -v for v in gvars]
    if a.solve:
        res["kissat"] = kissat_meta()
        runs = []
        if a.flag_variant:
            runs.append(run_kissat(f.nv, f.clauses, set(), gunits, tag + ":flag-variant+gram-units"))
        else:
            q_sb2 = set()
            q1_sb2 = set()
            for i, (sg, nm) in unit_idx.items():
                if a.target == "K5" or nm[1] != spec["weight1"]:
                    q_sb2.add(i)
                if nm[1] == spec["quantum"][0]:
                    q1_sb2.add(i)
            res["c12_variants"] = {
                "std": "base minus P4 at-least-one clauses (%d) minus SB2 Q-part units (%d; K5: all SB2 units, K4: squares "
                       "1-4 at (1,0), L-part kept) plus %d Gram units" % (len(alo), len(q_sb2), len(gunits)),
                "strong": "base minus P4 at-least-one clauses minus the SB2 units of square 1 only (%d) plus Gram units"
                          % len(q1_sb2),
                "mutation": "std instance with the unit of one g variable with value 1 negated; must be UNSAT"}
            runs.append(run_kissat(f.nv, f.clauses, alo | q_sb2, gunits, tag + ":std"))
            runs.append(run_kissat(f.nv, f.clauses, alo | q1_sb2, gunits, tag + ":strong"))
            one = next(v for v in gvars if val[v] and names[v][1] == 2)
            mut = [(-u if u == one else u) for u in gunits]
            r = run_kissat(f.nv, f.clauses, alo | q_sb2, mut, tag + ":mutation")
            r["mutated_variable"] = [one, names[one]]
            runs.append(r)
            w3s = [v for v in range(1, f.nv + 1) if names[v][0] == "w3"]
            res["p4_gadget_solver_tests"] = gadget_solver_tests(f, names, [w3s[0], w3s[len(w3s) // 2], w3s[-1]])
        res["solver_runs"] = runs
    ru = resource.getrusage(resource.RUSAGE_SELF)
    rc = resource.getrusage(resource.RUSAGE_CHILDREN)
    res["resources"] = {"self_maxrss_bytes": ru.ru_maxrss, "self_cpu_s": round(ru.ru_utime + ru.ru_stime, 1),
                        "children_maxrss_bytes": rc.ru_maxrss, "children_cpu_s": round(rc.ru_utime + rc.ru_stime, 1),
                        "wall_s": round(time.time() - T0, 1), "disk_free_end": shutil.disk_usage(OUTDIR).free}
    res["finished"] = now()
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1, default=list)
    log("done", a.out)


if __name__ == "__main__":
    main()
