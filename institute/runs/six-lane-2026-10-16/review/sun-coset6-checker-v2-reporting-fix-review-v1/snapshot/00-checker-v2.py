#!/usr/bin/env python3
"""
checker_v2.py -- independent checker for the engine-v3 Core5(6) certificate set
(sun-coset6 lane, six-lane run 2026-10-16).

v2 = checker_v1.py (sha256 5c25199b6de969c84c9521b9960a02d297d6cbacacea6c5e9e8f82695737874e) plus one
reporting fix from the final Codex composition review (sun-coset6-composition-final-v1-codex-v1.note.md,
MAJOR at lines 7-13): a witness skipped because the time budget ran out is now also recorded in the
global incomplete list, and PASS now also requires, from the per-rule tallies, verified == number of
lines, failed == 0 and incomplete == 0.  No check predicate changed.

Written ONLY from these texts; no engine or verifier source code was read:
  sun-coset6/CERT-FORMAT-k6-v1.md (primary specification), CERT-FORMAT-k6-v2.md, rules-k6-v1.md,
  rules-k6-v2.md, rules-k6-v3.md, proof-k6-lemmas-v1.md, rules-k6-erratum-v1.md,
  rules-k6-erratum-v2.md, README.md, and the review notes sun-coset6-rules-v1-codex-v1.note.md,
  sun-coset6-rules-v1-claude-v1.note.md, sun-coset6-rules-v3-delta-codex-v1.note.md,
  sun-coset6-rules-v3-delta-claude-v1.note.md (plus the parent's relayed checker obligations).

Python standard library only (no numpy), ONE process, exact integer / fractions.Fraction
arithmetic in every decision.

Usage:
  TMPDIR=<own tmp dir> python3 checker_v2.py --engine-dir DIR --out-json REPORT.json \
        --out-md REPORT.md --log RUNLOG.txt [--budget-seconds 3300]
Output files are created exclusively (open mode 'x'); the program never overwrites anything.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
import platform
import random
import re
import resource
import sys
import time
from fractions import Fraction
from math import gcd
from operator import itemgetter

SAT = 30
NV = 6
CODECH = "1234"
EDGES = [(i, j) for j in range(NV) for i in range(j)]
assert EDGES == [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                 (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
EIDX = {}
for _n, (_i, _j) in enumerate(EDGES):
    EIDX[(_i, _j)] = _n
    EIDX[(_j, _i)] = _n
TRIANGLES = list(itertools.combinations(range(NV), 3))
TYPES = [(None, 0, None), (None, 0, 0), (0, 1, None), (0, 1, 0), (0, 1, 1),
         (0, 2, None), (0, 2, 0), (0, 2, 1)]
RULES = ("K", "RLP", "PB", "Ppair", "FH5", "N26", "RPLP", "SURVIVE")
RAT_RE = re.compile(r"-?[0-9]+(/[0-9]+)?")
E5_PLACEMENTS = [None, 0, 1, 2, 3, 4, 5]
PAIRS5 = list(itertools.combinations(range(5), 2))      # lexicographic pairs of positions in N
FREE_DISK_FLOOR = 12200000000

SOURCES_USED = [
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/CERT-FORMAT-k6-v1.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-v1.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-v2.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-v3.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/proof-k6-lemmas-v1.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-erratum-v1.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/README.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/CERT-FORMAT-k6-v2.md",
    "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/rules-k6-erratum-v2.md",
    "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-rules-v1-codex-v1.note.md",
    "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-rules-v1-claude-v1.note.md",
    "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-rules-v3-delta-codex-v1.note.md",
    "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-rules-v3-delta-claude-v1.note.md",
]


class CertError(Exception):
    """A certificate (or input) failed a check.  Always fail closed."""


class Timeout(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise CertError(msg)


def is_int(x):
    return type(x) is int          # excludes bool


def tkey(typ):
    return str(tuple(typ))         # e.g. "(None, 0, None)", "(0, 2, 1)"


def bits(m):
    return [x for x in range(5) if (m >> x) & 1]


def popcount(m):
    return bin(m).count("1")


def submasks(m):
    """All submasks of m, from m down to 0 (inclusive)."""
    s = m
    while True:
        yield s
        if s == 0:
            return
        s = (s - 1) & m


def vp(n, p):
    need(is_int(n) and n >= 1, "vp of non-positive")
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def lcm(a, b):
    return a * b // gcd(a, b)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# --------------------------------------------------------------------------- markers / gcd table
def is_e2(z, typ):
    return typ[0] is not None and z == typ[0]


def is_e3(z, typ):
    return typ[2] is not None and z == typ[2]


def gtab(a, z, typ):
    """gcd(alpha, r_z) as in the CERT-FORMAT section 2 table (rules-k6-v1 L1)."""
    if a == 1:
        return 1
    if a == 2:
        return 2 if is_e2(z, typ) else 1
    if a == 3:
        return 3 if is_e3(z, typ) else 1
    if a == 4:
        if is_e2(z, typ):
            return 4 if typ[1] == 2 else 2
        return 1
    raise CertError("alpha out of range: %r" % (a,))


def parse_type(t):
    need(isinstance(t, list) and len(t) == 3, "type field malformed: %r" % (t,))
    e2, c2, e3 = t
    need(e2 is None or is_int(e2), "type e2 malformed: %r" % (t,))
    need(is_int(c2), "type c2 malformed: %r" % (t,))
    need(e3 is None or is_int(e3), "type e3 malformed: %r" % (t,))
    typ = (e2, c2, e3)
    need(typ in TYPES, "unknown type %r" % (t,))
    return typ


# --------------------------------------------------------------------------- codes
def parse_code(s):
    need(isinstance(s, str) and len(s) == 15 and all(ch in CODECH for ch in s), "bad code %r" % (s,))
    return s


def alpha_matrix(code):
    A = [[0] * NV for _ in range(NV)]
    for f, (i, j) in enumerate(EDGES):
        a = ord(code[f]) - 48
        A[i][j] = a
        A[j][i] = a
    return A


# --------------------------------------------------------------------------- rule T
def tau_min(A, typ, i, j, k):
    """lcm over the three edges e of alpha_e / gcd(alpha_e, r_opposite)."""
    t = 1
    for (x, y, z) in ((j, k, i), (i, k, j), (i, j, k)):
        a = A[x][y]
        g = gtab(a, z, typ)
        need(a % g == 0, "internal: gcd table")
        t = lcm(t, a // g)
    return t


def tau_max(A, i, j, k):
    """minimum over the three vertices of the product of the two alphas at that vertex."""
    return min(A[i][j] * A[i][k], A[j][i] * A[j][k], A[k][i] * A[k][j])


def tri_pass(A, typ, i, j, k):
    return tau_min(A, typ, i, j, k) <= tau_max(A, i, j, k)


def t_consistent(A, typ):
    return all(tri_pass(A, typ, i, j, k) for (i, j, k) in TRIANGLES)


def tri_table(typ, i, j, k):
    """tab[d_ij][d_ik][d_jk] = T passes on triangle (i,j,k) with alpha = d+1."""
    tab = [[[False] * 4 for _ in range(4)] for _ in range(4)]
    A = [[0] * NV for _ in range(NV)]
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                A[i][j] = A[j][i] = d1 + 1
                A[i][k] = A[k][i] = d2 + 1
                A[j][k] = A[k][j] = d3 + 1
                tab[d1][d2][d3] = tri_pass(A, typ, i, j, k)
    return tab


def enumerate_leaves(typ):
    """Primary enumeration: all T-consistent labellings of one type, sorted code strings.
    Vertex by vertex (= edge order E).  For vertex c every star (alpha_0c..alpha_{c-1}c) in
    {1..4}^c is considered; triangle {a,b,c} (a<b<c) is tested once its last edge (b,c) is
    assigned, which is the only pruning."""
    partials = list(CODECH)
    levels = [len(partials)]
    for c in range(2, NV):
        stars = ["".join(s) for s in itertools.product(CODECH, repeat=c)]   # increasing order
        pairs = []
        for a in range(c):
            for b in range(a + 1, c):
                tab = tri_table(typ, a, b, c)
                mk = {}
                for dab in range(4):
                    m = 0
                    for si, s in enumerate(stars):
                        if tab[dab][ord(s[a]) - 49][ord(s[b]) - 49]:
                            m |= 1 << si
                    mk[CODECH[dab]] = m
                pairs.append((EIDX[(a, b)], mk))
        full = (1 << len(stars)) - 1
        new = []
        app = new.append
        for p in partials:
            m = full
            for e, mk in pairs:
                m &= mk[p[e]]
                if not m:
                    break
            while m:
                low = m & -m
                app(p + stars[low.bit_length() - 1])
                m ^= low
        partials = new
        levels.append(len(partials))
    for x in range(1, len(partials)):
        need(partials[x - 1] < partials[x], "internal: enumeration not strictly increasing")
    return partials, levels


def enumerate_leaves_dfs(typ, deadline=None):
    """Second, structurally different enumeration: depth-first over the 15 edges in order E,
    each of 1..4 tried, each completed triangle tested with the scalar T function."""
    comp = [[] for _ in range(15)]
    for (a, b, c) in TRIANGLES:
        comp[EIDX[(b, c)]].append((a, b, c))
    A = [[0] * NV for _ in range(NV)]
    cur = [""] * 15
    out = []
    nodes = [0]

    def rec(f):
        if f == 15:
            out.append("".join(cur))
            return
        i, j = EDGES[f]
        for a in (1, 2, 3, 4):
            nodes[0] += 1
            if deadline is not None and nodes[0] % 200000 == 0 and time.time() > deadline:
                raise Timeout()
            A[i][j] = A[j][i] = a
            cur[f] = CODECH[a - 1]
            ok = True
            for (x, y, z) in comp[f]:
                if not tri_pass(A, typ, x, y, z):
                    ok = False
                    break
            if ok:
                rec(f + 1)
        A[i][j] = A[j][i] = 0

    try:
        rec(0)
    except Timeout:
        return None, nodes[0]
    return out, nodes[0]


def spot_check(typ, leafset, leaves, seed, n_random, n_leaf_samples):
    """Membership in the leaf set agrees with the scalar T test on random labellings and on all
    one-edge changes of sampled leaves."""
    rng = random.Random(seed)
    bad = 0
    pos = 0
    checked = 0
    for _ in range(n_random):
        s = "".join(rng.choice(CODECH) for _ in range(15))
        tc = t_consistent(alpha_matrix(s), typ)
        pos += tc
        bad += tc != (s in leafset)
        checked += 1
    for _ in range(n_leaf_samples):
        base = leaves[rng.randrange(len(leaves))]
        for f in range(15):
            for ch in CODECH:
                if ch == base[f]:
                    continue
                s = base[:f] + ch + base[f + 1:]
                tc = t_consistent(alpha_matrix(s), typ)
                pos += tc
                bad += tc != (s in leafset)
                checked += 1
    return {"checked": checked, "t_consistent_among_checked": pos, "disagreements": bad}


def leaf_hash(sorted_codes):
    """sha256 of the sorted code strings joined by newline, plus a final newline."""
    h = hashlib.sha256()
    CH = 65536
    for s in range(0, len(sorted_codes), CH):
        h.update(("\n".join(sorted_codes[s:s + CH]) + "\n").encode("ascii"))
    return h.hexdigest()


# --------------------------------------------------------------------------- types / orbits
def stabiliser(typ):
    fixed = [x for x in (typ[0], typ[2]) if x is not None]
    return [p for p in itertools.permutations(range(NV)) if all(p[x] == x for x in fixed)]


def _perm_placement(p, pl):
    e2, c2, e3 = pl
    return (None if e2 is None else p[e2], c2, None if e3 is None else p[e3])


def check_types_cover():
    """Every E2(class)/E3 placement maps to exactly one of the 8 types; stabilisers are as stated."""
    perms = list(itertools.permutations(range(NV)))
    pls = []
    for e2 in [None] + list(range(NV)):
        for c2 in ([0] if e2 is None else [1, 2]):
            for e3 in [None] + list(range(NV)):
                pls.append((e2, c2, e3))
    hits = {}
    for pl in pls:
        reach = set(_perm_placement(p, pl) for p in perms) & set(TYPES)
        need(len(reach) == 1, "placement %r reaches %d types" % (pl, len(reach)))
        t = reach.pop()
        hits[tkey(t)] = hits.get(tkey(t), 0) + 1
    sizes = {}
    for typ in TYPES:
        st = stabiliser(typ)
        need(set(st) == set(p for p in perms if _perm_placement(p, typ) == typ), "stabiliser mismatch")
        sset = set(st)
        for p in st:
            for r in st:
                need(tuple(p[r[x]] for x in range(NV)) in sset, "stabiliser not closed")
        sizes[tkey(typ)] = len(st)
    return {"placements": len(pls), "placements_per_type": hits, "stabiliser_sizes": sizes,
            "each_placement_maps_to_exactly_one_type": True}


def edge_src(p):
    """(p.alpha)[f] = alpha[src[f]], where (p.alpha)_{p(i)p(j)} = alpha_{ij}."""
    pinv = [0] * NV
    for i, pi in enumerate(p):
        pinv[pi] = i
    return [EIDX[(pinv[x], pinv[y])] for (x, y) in EDGES]


def act(p, code):
    src = edge_src(p)
    return "".join(code[s] for s in src)


def orbit_getters(perms):
    return [itemgetter(*edge_src(p)) for p in perms]


def check_orbit_coverage(typ, leafset, reps, codes=None):
    """Own orbits of the reps under the stabiliser must be pairwise disjoint, union = leaf set.
    Also (informational) whether the engine 'code' field lies in the orbit of rep / is its min."""
    getters = orbit_getters(stabiliser(typ))
    union = set()
    total = 0
    code_in = 0
    code_min = 0
    for n, r in enumerate(reps):
        o = {"".join(g(r)) for g in getters}
        total += len(o)
        union |= o
        if codes is not None:
            code_in += codes[n] in o
            code_min += codes[n] == min(o)
    res = {"lines": len(reps), "sum_orbit_sizes": total, "union_size": len(union),
           "duplicate_elements": total - len(union), "disjoint": total == len(union),
           "union_equals_leaves": union == leafset,
           "missing": len(leafset - union), "extra": len(union - leafset),
           "union_sha256": leaf_hash(sorted(union))}
    if codes is not None:
        res["code_field_in_stabiliser_orbit_of_rep"] = code_in
        res["code_field_equals_my_orbit_min"] = code_min
    res["ok"] = bool(res["disjoint"] and res["union_equals_leaves"])
    return res


def code_in_s6_orbit_sample(reps, codes, limit):
    """Informational: for up to `limit` lines, is the engine 'code' in the full S6 orbit of rep?"""
    getters = orbit_getters(list(itertools.permutations(range(NV))))
    n = min(limit, len(reps))
    hit = 0
    for x in range(n):
        o = {"".join(g(reps[x])) for g in getters}
        hit += codes[x] in o
    return {"sampled": n, "code_in_S6_orbit": hit}


# --------------------------------------------------------------------------- rationals / JSON
def parse_rat(s):
    need(isinstance(s, str) and RAT_RE.fullmatch(s) is not None, "bad rational %r" % (s,))
    try:
        return Fraction(s)
    except ZeroDivisionError:
        raise CertError("zero denominator %r" % (s,))


def _strict_pairs(pairs):
    d = {}
    for k, v in pairs:
        need(k not in d, "duplicate JSON key %r" % (k,))
        d[k] = v
    return d


def strict_loads(raw):
    """json.loads that rejects duplicate keys (fail closed)."""
    return json.loads(raw, object_pairs_hook=_strict_pairs)


# --------------------------------------------------------------------------- neighbours / q / supports
def nbrs(v):
    return [j for j in range(NV) if j != v]


def st_of(j, typ):
    return (typ[1] if is_e2(j, typ) else 0, 1 if is_e3(j, typ) else 0)


def rlp_key(q, sts):
    return ",".join(str(x) for x in q) + "|" + ";".join("%d%d" % s for s in sts)


def q_space(A, v):
    """Every q in prod_{j in N} {1..5-alpha_vj}, first neighbour slowest (itertools.product)."""
    return list(itertools.product(*[range(1, 6 - A[v][j]) for j in nbrs(v)]))


_ALLOWED = {}


def allowed_masks(q, sts):
    """All non-empty S (bitmask over positions 0..4 of N) that are allowed: |S| = 1, or every
    T subset of S with |T| >= 2 has a pair with maxgcd >= |T|.  All 31 subsets are tested."""
    ex = []
    for x in range(5):
        d, f = sts[x]
        need(d in (0, 1, 2) and f in (0, 1), "bad status")
        e2 = vp(q[x], 2) + (0 if d == 0 else (1 if d == 1 else SAT))
        e3 = vp(q[x], 3) + (SAT if f == 1 else 0)
        ex.append((e2, e3))
    ex = tuple(ex)
    if ex in _ALLOWED:
        return _ALLOWED[ex]

    def mg(x, y):
        return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1]))

    res = []
    for S in range(1, 32):
        if popcount(S) == 1:
            res.append(S)
            continue
        ok = True
        for T in submasks(S):
            tm = bits(T)
            if len(tm) < 2:
                continue
            if not any(mg(x, y) >= len(tm) for x, y in itertools.combinations(tm, 2)):
                ok = False
                break
        if ok:
            res.append(S)
    res = tuple(res)
    _ALLOWED[ex] = res
    return res


def check_rlp_dual(q, sts, entry, allowed=None):
    need(isinstance(entry, dict) and "y" in entry, "dual entry malformed")
    ys = entry["y"]
    need(isinstance(ys, list) and len(ys) == 5, "dual y must have 5 entries")
    y = [parse_rat(s) for s in ys]
    need(all(t >= 0 for t in y), "dual y has a negative entry")
    if allowed is None:
        allowed = allowed_masks(q, sts)
    for S in allowed:
        tot = sum((y[x] for x in bits(S)), Fraction(0))
        need(tot <= 1, "allowed S=%s has y-sum %s > 1" % (bits(S), tot))
    obj = sum((Fraction(q[x], 5) * y[x] for x in range(5)), Fraction(0))
    need(obj >= 1, "dual objective %s < 1" % (obj,))
    return obj


class RLPCache:
    """Caches RLP dual checks by their full input key "q|statuses" (the key fixes q and statuses)."""

    def __init__(self, duals):
        need(isinstance(duals, dict), "rlp_duals.json is not an object")
        self.duals = duals
        self.res = {}

    def check(self, q, sts):
        key = rlp_key(q, sts)
        if key not in self.res:
            if key not in self.duals:
                self.res[key] = (False, "missing dual for key %s" % key)
            else:
                try:
                    check_rlp_dual(q, sts, self.duals[key])
                    self.res[key] = (True, "")
                except CertError as e:
                    self.res[key] = (False, "key %s: %s" % (key, e))
        return self.res[key]


# --------------------------------------------------------------------------- rules
def _vertex(x):
    return is_int(x) and 0 <= x < NV


def _vertex_set(S, v, minlen):
    return (isinstance(S, list) and len(S) >= minlen and all(_vertex(i) and i != v for i in S)
            and len(set(S)) == len(S))


def check_K(A, typ, wit):
    need(isinstance(wit, list) and len(wit) == 2, "K witness shape")
    v, S = wit
    need(_vertex(v), "K: bad v")
    need(_vertex_set(S, v, 1), "K: bad S")
    need(sum(A[i][v] for i in S) >= 5, "K: sum of alpha_iv < 5")
    for i, j in itertools.combinations(S, 2):
        need(tau_min(A, typ, i, v, j) == A[i][v] * A[v][j], "K: pair (%d,%d) not linked at v=%d" % (i, j, v))
    return "ok"


def check_RLP(A, typ, wit, cache):
    need(isinstance(wit, list) and len(wit) == 1, "RLP witness shape")
    v = wit[0]
    need(_vertex(v), "RLP: bad v")
    sts = [st_of(j, typ) for j in nbrs(v)]
    nq = 0
    for q in q_space(A, v):
        ok, msg = cache.check(q, sts)
        need(ok, "RLP q=%s: %s" % (q, msg))
        nq += 1
    return "ok (%d q)" % nq


def lohi(A, typ, v, j, k):
    """lo/hi of |X_j cap X_k| at vertex v (units |G|), rounded on the grid of multiples of u:
    lo = u*ceil(L/u), hi = u*floor(min(x_j,x_k)/u), then the K2 containment decrement."""
    xj = Fraction(A[v][j], 5)
    xk = Fraction(A[v][k], 5)
    g = gtab(A[j][k], v, typ)
    u = Fraction(1, 5 * g)
    L = max(Fraction(tau_min(A, typ, v, j, k), 5 * A[j][k]), xj + xk - 1, Fraction(0))
    lo = u * math.ceil(L / u)
    m = min(xj, xk)
    hi = u * math.floor(m / u)
    if hi == m:
        allow_j_in_k = A[v][j] + A[k][j] <= 4     # K2 for X_j subset X_k
        allow_k_in_j = A[v][k] + A[j][k] <= 4     # K2 for X_k subset X_j
        if xj < xk:
            barred = not allow_j_in_k
        elif xk < xj:
            barred = not allow_k_in_j
        else:
            barred = not (allow_j_in_k and allow_k_in_j)
        if barred:
            hi = hi - u
    return lo, hi, u


def check_Ppair(A, typ, wit):
    need(isinstance(wit, list) and len(wit) == 2, "Ppair witness shape")
    v, pr = wit
    need(_vertex(v), "Ppair: bad v")
    need(_vertex_set(pr, v, 2) and len(pr) == 2, "Ppair: bad pair")
    lo, hi, u = lohi(A, typ, v, pr[0], pr[1])
    need(lo > hi, "Ppair: lo %s <= hi %s" % (lo, hi))
    return "ok"


def check_PB(A, typ, wit):
    need(isinstance(wit, list) and len(wit) == 2, "PB witness shape")
    v, S = wit
    need(_vertex(v), "PB: bad v")
    need(_vertex_set(S, v, 1), "PB: bad S")
    N = nbrs(v)
    H = {}
    for j, k in itertools.combinations(N, 2):
        lo, hi, u = lohi(A, typ, v, j, k)
        need(lo <= hi, "PB: pair (%d,%d) has lo > hi (Ppair applies instead)" % (j, k))
        H[(j, k)] = hi
        H[(k, j)] = hi
    x = {j: Fraction(A[v][j], 5) for j in N}
    lhs = sum((1 - x[j] for j in S), Fraction(0)) - sum(
        (1 - x[j] - x[k] + H[(j, k)] for j, k in itertools.combinations(S, 2)), Fraction(0))
    need(lhs >= 1, "PB: Bonferroni lhs %s < 1" % (lhs,))
    return "ok"


def check_N26(A, typ, wit):
    """Safe N2-6: v != E2; alpha_vj = 2; alpha_jk in {2,4}; for every neighbour triple and EVERY
    admissible tau (multiples of tau_min up to tau_max): no prime factor >= 5, and if v = E3 then
    3 does not divide tau; and (as instructed) tau_max < 3 tau_min on every triple when v = E3.
    The '3 | tau_min' alternative of the texts is never accepted."""
    need(isinstance(wit, list) and len(wit) == 1, "N26 witness shape")
    v = wit[0]
    need(_vertex(v), "N26: bad v")
    need(not is_e2(v, typ), "N26: v is E2")
    N = nbrs(v)
    need(all(A[v][j] == 2 for j in N), "N26: some alpha_vj != 2")
    need(all(A[j][k] in (2, 4) for j, k in itertools.combinations(N, 2)), "N26: some alpha_jk not in {2,4}")
    for (j, k, l) in itertools.combinations(N, 3):
        tm = tau_min(A, typ, j, k, l)
        tM = tau_max(A, j, k, l)
        need(tm <= tM, "N26: triple (%d,%d,%d) T-inconsistent" % (j, k, l))
        for tau in range(tm, tM + 1, tm):
            t = tau
            while t % 2 == 0:
                t //= 2
            while t % 3 == 0:
                t //= 3
            need(t == 1, "N26: admissible tau=%d on (%d,%d,%d) has a prime factor >= 5" % (tau, j, k, l))
            if is_e3(v, typ):
                need(tau % 3 != 0, "N26: v=E3 and admissible tau=%d on (%d,%d,%d) divisible by 3" % (tau, j, k, l))
        if is_e3(v, typ):
            need(tM < 3 * tm, "N26: v=E3 and tau_max %d >= 3*tau_min %d on (%d,%d,%d)" % (tM, tm, j, k, l))
    return "ok"


def forced_pairs(A, typ, v):
    """Ordered position pairs (w,j) of N with tau_min(v,w,j) >= alpha_vw * alpha_wj."""
    N = nbrs(v)
    return [(wx, jx) for wx in range(5) for jx in range(5)
            if wx != jx and tau_min(A, typ, v, N[wx], N[jx]) >= A[v][N[wx]] * A[N[wx]][N[jx]]]


def rplp_columns(A, typ, v, q, sts, forced=None, include_empty_S=True):
    """All (A,S): A non-empty subset of N closed under forced pairs (j in A => w in A);
    S subset of A that is empty, a singleton or hereditary-allowed (for this q)."""
    if forced is None:
        forced = forced_pairs(A, typ, v)
    allowed = set(allowed_masks(q, sts))
    cols = []
    for Am in range(1, 32):
        if any(((Am >> jx) & 1) and not ((Am >> wx) & 1) for (wx, jx) in forced):
            continue
        for Sm in submasks(Am):
            if (Sm == 0 and include_empty_S) or (Sm != 0 and Sm in allowed):
                cols.append((Am, Sm))
    return cols


def rplp_bounds(A, typ, v):
    N = nbrs(v)
    yhi, ylo = [], []
    for (x, y) in PAIRS5:
        lo, hi, u = lohi(A, typ, v, N[x], N[y])
        base = 1 - Fraction(A[v][N[x]] + A[v][N[y]], 5)
        yhi.append(base + hi)
        ylo.append(base + lo)
    return yhi, ylo


def check_rplp_vec(A, typ, v, q, vec, cols, yhi, ylo):
    need(isinstance(vec, list) and len(vec) == 30, "RPLP: P vector must have 30 entries")
    vals = [parse_rat(s) for s in vec]
    a, b, u, l = vals[0:5], vals[5:10], vals[10:20], vals[20:30]
    need(all(t >= 0 for t in u), "RPLP: negative u")
    need(all(t >= 0 for t in l), "RPLP: negative l")
    N = nbrs(v)
    for (Am, Sm) in cols:
        val = sum((a[x] for x in bits(Sm)), Fraction(0)) + sum((b[x] for x in bits(Am)), Fraction(0))
        for p, (x, y) in enumerate(PAIRS5):
            if (Am >> x) & 1 and (Am >> y) & 1:
                val += l[p] - u[p]
        need(val <= 1, "RPLP: column A=%s S=%s has value %s > 1" % (bits(Am), bits(Sm), val))
    obj = (sum((a[x] * Fraction(q[x], 5) for x in range(5)), Fraction(0))
           + sum((b[x] * Fraction(5 - A[v][N[x]], 5) for x in range(5)), Fraction(0))
           - sum((u[p] * yhi[p] for p in range(10)), Fraction(0))
           + sum((l[p] * ylo[p] for p in range(10)), Fraction(0)))
    need(obj >= 1, "RPLP: objective %s < 1" % (obj,))
    return obj


def check_RPLP(A, typ, wit, cache):
    need(isinstance(wit, list) and len(wit) == 2, "RPLP witness shape")
    v, certs = wit
    need(_vertex(v), "RPLP: bad v")
    N = nbrs(v)
    sts = [st_of(j, typ) for j in N]
    qs = q_space(A, v)
    need(isinstance(certs, list) and len(certs) == len(qs),
         "RPLP: %s certs for %d admissible q" % (len(certs) if isinstance(certs, list) else "?", len(qs)))
    forced = forced_pairs(A, typ, v)
    yhi, ylo = rplp_bounds(A, typ, v)
    nR = nP = 0
    for q, cert in zip(qs, certs):
        need(isinstance(cert, list) and len(cert) == 2 and cert[0] in ("R", "P"), "RPLP: malformed cert for q=%s" % (q,))
        if cert[0] == "R":
            key = rlp_key(q, sts)
            need(cert[1] == key, "RPLP: R key %r != expected %r" % (cert[1], key))
            ok, msg = cache.check(q, sts)
            need(ok, "RPLP q=%s: %s" % (q, msg))
            nR += 1
        else:
            cols = rplp_columns(A, typ, v, q, sts, forced)
            try:
                check_rplp_vec(A, typ, v, q, cert[1], cols, yhi, ylo)
            except CertError as e:
                raise CertError("q=%s: %s" % (q, e))
            nP += 1
    return "ok (R %d, P %d)" % (nR, nP)


# --------------------------------------------------------------------------- FH5
def fh5_V(A, a, b):
    return sorted(v for v in range(NV) if v != a and v != b and A[v][a] == A[v][b])


def check_FH5_witness(A, typ, wit):
    need(isinstance(wit, list) and len(wit) == 3, "FH5 witness shape")
    ab, V, counts = wit
    need(isinstance(ab, list) and len(ab) == 2 and all(_vertex(x) for x in ab) and ab[0] != ab[1], "FH5: bad [a,b]")
    a, b = ab
    need(A[a][b] == 1, "FH5: alpha_ab != 1")
    myV = fh5_V(A, a, b)
    need(len(myV) >= 1, "FH5: V empty")
    need(isinstance(V, list) and all(_vertex(x) for x in V) and len(set(V)) == len(V) and sorted(V) == myV,
         "FH5: witness V %r != computed V %r" % (V, myV))
    need(isinstance(counts, list) and len(counts) == 7 and all(is_int(c) and c >= 0 for c in counts),
         "FH5: counts malformed")
    return a, b, myV, counts


def fh5_domains(A, a, b, V):
    subsets = {t: [m for m in range(1, 32) if popcount(m) == t] for t in range(1, 6)}
    dom = {a: [(1, 1)]}
    dom[b] = [(1, 1 << c) for c in range(5)]
    for l in V:
        c = A[l][a]
        dom[l] = [(1, 1 << x) for x in range(5)] if c == 1 else [(c, m) for m in subsets[c]]
    for l in range(NV):
        if l not in dom:
            dom[l] = [(t, m) for t in range(1, 6) for m in subsets[t]]
    return dom


def fh5_lambda_exp(typ, l, t, e5):
    e2 = vp(t, 2) + ((1 if typ[1] == 1 else SAT) if is_e2(l, typ) else 0)
    e3 = vp(t, 3) + (SAT if is_e3(l, typ) else 0)
    e5x = vp(t, 5) + (SAT if (e5 is not None and l == e5) else 0)
    return e2, e3, e5x


def fh5_fgcd(typ, x, y, e5):
    e, f = fh5_lambda_exp(typ, x[0], x[1], e5), fh5_lambda_exp(typ, y[0], y[1], e5)
    return (2 ** min(e[0], f[0])) * (3 ** min(e[1], f[1])) * (5 ** min(e[2], f[2]))


def fh5_search(A, typ, a, b, V, deadline=None):
    """Exhaustive search over all FH5 assignments, all 7 E5 placements at once.
    A partial assignment is dropped for a placement only when it is already rejected there by
    (i) F3 between two assigned vertices or (ii) a failing subset T of an assigned coset member
    set; both persist under extension.  Status REFUTED / ACCEPTED / INCOMPLETE."""
    NP = len(E5_PLACEMENTS)
    FULL = (1 << NP) - 1
    others = [l for l in range(NV) if l != a and l != b and l not in V]
    order = [a, b] + list(V) + others
    dom = fh5_domains(A, a, b, V)
    space = 1
    for l in range(NV):
        space *= len(dom[l])
    fgc = {}

    def fg(x, y, pi):
        key = (x, y, pi)
        r = fgc.get(key)
        if r is None:
            r = fh5_fgcd(typ, x, y, E5_PLACEMENTS[pi])
            fgc[key] = r
        return r

    def coset_ok(M, new, pi):
        n = len(M)
        for tm in range(1, 1 << n):
            T = [M[i] for i in range(n) if (tm >> i) & 1]
            T.append(new)
            s = len(T)
            if not any(fg(T[i], T[j], pi) >= s for i in range(s) for j in range(i + 1, s)):
                return False
        return True

    members = [[] for _ in range(5)]
    assigned = []
    stats = {"nodes": 0}
    found = []

    def dfs(depth, alive):
        stats["nodes"] += 1
        if deadline is not None and stats["nodes"] % 2048 == 0 and time.time() > deadline:
            raise Timeout()
        if depth == NV:
            found.append(([(l, t, bits(m)) for (l, t, m) in assigned],
                          [E5_PLACEMENTS[i] for i in range(NP) if (alive >> i) & 1]))
            return True
        l = order[depth]
        for (t, m) in dom[l]:
            bad = False
            for (i, ti, mi) in assigned:
                if (ti == 1 and A[i][l] > t) or (t == 1 and A[l][i] > ti):
                    bad = True
                    break
            if bad:
                continue
            na = alive
            for pi in range(NP):
                if not (na >> pi) & 1:
                    continue
                for c in range(5):
                    if (m >> c) & 1 and members[c] and not coset_ok(members[c], (l, t), pi):
                        na &= ~(1 << pi)
                        break
            if na == 0:
                continue
            assigned.append((l, t, m))
            for c in range(5):
                if (m >> c) & 1:
                    members[c].append((l, t))
            r = dfs(depth + 1, na)
            for c in range(5):
                if (m >> c) & 1:
                    members[c].pop()
            assigned.pop()
            if r:
                return True
        return False

    try:
        acc = dfs(0, FULL)
    except Timeout:
        return {"status": "INCOMPLETE", "nodes": stats["nodes"], "space": space}
    if acc:
        return {"status": "ACCEPTED", "nodes": stats["nodes"], "space": space, "accepted": found[0]}
    return {"status": "REFUTED", "nodes": stats["nodes"], "space": space}


# --------------------------------------------------------------------------- input lines
def parse_line(raw):
    obj = strict_loads(raw)
    need(isinstance(obj, dict), "line is not an object")
    rule = obj.get("rule")
    need(isinstance(rule, str) and rule in RULES, "unknown rule %r" % (rule,))
    expected = {"type", "code", "rep", "rule"} | (set() if rule == "SURVIVE" else {"witness"})
    need(set(obj.keys()) == expected, "unexpected keys %r" % (sorted(obj.keys()),))
    typ = parse_type(obj["type"])
    rep = parse_code(obj["rep"])
    code = parse_code(obj["code"])
    return typ, rep, code, rule, obj.get("witness")


def check_rule(A, typ, rule, wit, cache, deadline=None):
    """Dispatch one line's certificate.  Raises CertError on failure.  FH5 runs the full search."""
    if rule == "SURVIVE":
        raise CertError("SURVIVE line (no certificate)")
    if rule == "K":
        return check_K(A, typ, wit), None
    if rule == "RLP":
        return check_RLP(A, typ, wit, cache), None
    if rule == "PB":
        return check_PB(A, typ, wit), None
    if rule == "Ppair":
        return check_Ppair(A, typ, wit), None
    if rule == "N26":
        return check_N26(A, typ, wit), None
    if rule == "RPLP":
        return check_RPLP(A, typ, wit, cache), None
    if rule == "FH5":
        a, b, V, counts = check_FH5_witness(A, typ, wit)
        r = fh5_search(A, typ, a, b, V, deadline)
        r["engine_counts_equal_full_space"] = all(c == r["space"] for c in counts)
        if r["status"] == "INCOMPLETE":
            return "INCOMPLETE", r
        need(r["status"] == "REFUTED", "FH5: accepted assignment %r" % (r.get("accepted"),))
        return "ok", r
    raise CertError("unknown rule %r" % (rule,))


def compare_type_summary(k, leaves_mine, hash_mine, orbit_lines, rule_counts_lines, eng):
    """Compare my numbers for one type with run.json summary[type]; returns failure strings."""
    out = []
    if not isinstance(eng, dict):
        return ["run.json has no summary for %s" % k]
    if eng.get("leaves_labelled") != leaves_mine:
        out.append("leaf count mismatch: mine %d, run.json %r" % (leaves_mine, eng.get("leaves_labelled")))
    if eng.get("leafcodes_sha256") != hash_mine:
        out.append("leaf hash mismatch: mine %s, run.json %r" % (hash_mine, eng.get("leafcodes_sha256")))
    if eng.get("orbits") != orbit_lines:
        out.append("orbit count mismatch: lines %d, run.json %r" % (orbit_lines, eng.get("orbits")))
    erc = eng.get("orbit_rule_counts")
    if not (isinstance(erc, dict) and {a: b for a, b in erc.items() if b} == rule_counts_lines):
        out.append("rule counts mismatch: lines %r, run.json %r" % (rule_counts_lines, erc))
    return out


def global_survive_check(rules_of_lines, survivors, run):
    """Any SURVIVE line, non-empty survivors.json or non-zero total_survivors => failure."""
    out = []
    ns = sum(1 for r in rules_of_lines if r == "SURVIVE")
    if ns:
        out.append("%d SURVIVE lines" % ns)
    if survivors not in ([], {}):
        out.append("survivors.json is not empty")
    if not isinstance(run, dict) or run.get("total_survivors") != 0:
        out.append("run.json total_survivors is not 0")
    return out


# --------------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine-dir", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--budget-seconds", type=int, default=3300)
    ap.add_argument("--spot-random", type=int, default=20000)
    ap.add_argument("--spot-leaves", type=int, default=300)
    args = ap.parse_args(argv)
    tmpdir = os.environ.get("TMPDIR", "")
    need(tmpdir != "" and os.path.isdir(tmpdir), "TMPDIR must be set to an existing own directory")
    import tempfile
    tempfile.tempdir = tmpdir
    st0 = os.statvfs("/Users/jinleic/repos/aifours")
    free0 = st0.f_bavail * st0.f_frsize
    if free0 < FREE_DISK_FLOOR:
        print("refusing to start: free disk %d < %d bytes" % (free0, FREE_DISK_FLOOR))
        return 2
    t0 = time.time()
    deadline = t0 + args.budget_seconds
    logf = open(args.log, "x")

    def log(msg):
        line = "%s %8.1fs %s" % (time.strftime("%H:%M:%S"), time.time() - t0, msg)
        logf.write(line + "\n")
        logf.flush()
        print(line, flush=True)

    rep = {"checker": {}, "inputs": {}, "sources_used_sha256": {}, "environment": {},
           "types_cover": None, "per_type": {}, "global": {}, "failures": [], "incomplete": []}
    me = os.path.abspath(__file__)
    rep["checker"] = {"path": me, "sha256": sha256_bytes(open(me, "rb").read())}
    rep["environment"] = {"python": sys.version, "platform": platform.platform(), "TMPDIR": tmpdir,
                          "processes": 1, "numpy": "not used", "budget_seconds": args.budget_seconds,
                          "free_bytes_at_start": free0, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    for p in SOURCES_USED:
        try:
            rep["sources_used_sha256"][p] = sha256_bytes(open(p, "rb").read())
        except OSError as e:
            rep["sources_used_sha256"][p] = "UNREADABLE: %s" % e

    def fail(where, msg):
        rep["failures"].append({"where": where, "msg": msg})

    # ---- inputs
    files = {}
    for name in ("run.json", "orbits.jsonl.gz", "rlp_duals.json", "survivors.json"):
        p = os.path.join(args.engine_dir, name)
        data = open(p, "rb").read()
        files[name] = data
        rep["inputs"][p] = {"sha256": sha256_bytes(data), "bytes": len(data)}
    man = os.path.join(os.path.dirname(os.path.abspath(args.engine_dir)), "engine-v3-run.sha256")
    if os.path.exists(man):
        mb = open(man, "rb").read()
        rep["inputs"][man] = {"sha256": sha256_bytes(mb), "bytes": len(mb)}
        mtxt = mb.decode("utf-8", "replace")
        rep["global"]["manifest_lists_input_hashes"] = {
            name: rep["inputs"][os.path.join(args.engine_dir, name)]["sha256"] in mtxt for name in files}

    def load_json(name):
        try:
            return strict_loads(files[name])
        except CertError as e:
            fail(name, "strict JSON parse: %s" % e)
            return json.loads(files[name])

    run = load_json("run.json")
    raw_orb = gzip.decompress(files["orbits.jsonl.gz"])
    rep["global"]["orbits_jsonl_uncompressed_sha256"] = sha256_bytes(raw_orb)
    rep["global"]["orbits_jsonl_uncompressed_sha256_matches_run_json"] = (
        isinstance(run, dict) and sha256_bytes(raw_orb) == run.get("orbits_jsonl_sha256_uncompressed"))
    duals = load_json("rlp_duals.json")
    survivors = load_json("survivors.json")
    log("inputs read and hashed")

    try:
        rep["types_cover"] = check_types_cover()
    except CertError as e:
        fail("types", str(e))
    summ = run.get("summary") if isinstance(run, dict) else None
    if not (isinstance(summ, dict) and set(summ.keys()) == set(tkey(t) for t in TYPES)):
        fail("run.json", "summary keys are not exactly the 8 types")
        summ = summ if isinstance(summ, dict) else {}

    # ---- parse all lines (fail closed on any malformed line)
    lines = []
    bad_lines = 0
    for n, raw in enumerate(raw_orb.split(b"\n")):
        if not raw.strip():
            continue
        try:
            typ, repc, code, rule, wit = parse_line(raw)
            lines.append((n, typ, repc, code, rule, wit))
        except (CertError, ValueError) as e:
            bad_lines += 1
            fail("line %d" % n, "parse: %s" % e)
    rep["global"]["lines_parsed"] = len(lines)
    rep["global"]["lines_malformed"] = bad_lines
    by_type = {tkey(t): [] for t in TYPES}
    for L in lines:
        by_type[tkey(L[1])].append(L)
    log("parsed %d lines (%d malformed)" % (len(lines), bad_lines))

    # ---- per type: enumeration x2, hash, spot check, orbit coverage
    for ti, t in enumerate(TYPES):
        k = tkey(t)
        pt = {}
        rep["per_type"][k] = pt
        if time.time() > deadline:
            rep["incomplete"].append({"where": k, "what": "enumeration/coverage not run before deadline"})
            pt["status"] = "INCOMPLETE"
            continue
        ts = time.time()
        leaves, levels = enumerate_leaves(t)
        pt["leaves_mine"] = len(leaves)
        pt["partial_counts_by_vertex_level"] = levels
        pt["hash_mine"] = leaf_hash(leaves)
        pt["enum_seconds"] = round(time.time() - ts, 2)
        ts = time.time()
        dfs, nodes = enumerate_leaves_dfs(t, deadline)
        if dfs is None:
            pt["dfs_crosscheck"] = "INCOMPLETE"
            rep["incomplete"].append({"where": k, "what": "edge-DFS cross-check enumeration"})
        else:
            pt["dfs_crosscheck"] = {"count": len(dfs), "nodes": nodes, "identical_to_primary": dfs == leaves}
            if dfs != leaves:
                fail(k, "edge-DFS enumeration differs from primary enumeration")
        del dfs
        pt["dfs_seconds"] = round(time.time() - ts, 2)
        leafset = set(leaves)
        ts = time.time()
        pt["spot_check"] = spot_check(t, leafset, leaves, 1000 + ti, args.spot_random, args.spot_leaves)
        if pt["spot_check"]["disagreements"]:
            fail(k, "spot check disagreements")
        pt["spot_seconds"] = round(time.time() - ts, 2)
        Ls = by_type[k]
        reps = [L[2] for L in Ls]
        codes = [L[3] for L in Ls]
        ts = time.time()
        cov = check_orbit_coverage(t, leafset, reps, codes)
        pt["orbit_coverage"] = cov
        if not cov["ok"]:
            fail(k, "orbit coverage failed: %s" % ({x: cov.get(x) for x in ("disjoint", "union_equals_leaves", "missing", "extra", "duplicate_elements")},))
        pt["code_field_S6_sample"] = code_in_s6_orbit_sample(reps, codes, 200)
        nonleaf = sum(1 for r in reps if r not in leafset)
        scalar_bad = sum(1 for r in reps if not t_consistent(alpha_matrix(r), t))
        pt["reps_not_in_leafset"] = nonleaf
        pt["reps_failing_scalar_T"] = scalar_bad
        if nonleaf or scalar_bad:
            fail(k, "%d reps not in my leaf set; %d fail the scalar T check" % (nonleaf, scalar_bad))
        pt["orbit_seconds"] = round(time.time() - ts, 2)
        rc = {}
        for L in Ls:
            rc[L[4]] = rc.get(L[4], 0) + 1
        pt["orbit_lines"] = len(Ls)
        pt["rule_counts_lines"] = rc
        eng = summ.get(k)
        pt["engine_summary"] = {x: eng.get(x) for x in ("leaves_labelled", "leafcodes_sha256", "orbits", "orbit_rule_counts")} if isinstance(eng, dict) else None
        cmpf = compare_type_summary(k, len(leaves), pt["hash_mine"], len(Ls), rc, eng)
        pt["summary_mismatches"] = cmpf
        pt["leaves_match"] = not any(x.startswith("leaf count") for x in cmpf)
        pt["hash_match"] = not any(x.startswith("leaf hash") for x in cmpf)
        pt["orbits_match"] = not any(x.startswith("orbit count") for x in cmpf)
        pt["rule_counts_match"] = not any(x.startswith("rule counts") for x in cmpf)
        for x in cmpf:
            fail(k, x)
        pt["rules"] = {r: {"lines": 0, "verified": 0, "failed": 0, "incomplete": 0} for r in RULES}
        del leaves, leafset
        log("type %s: leaves %d, hash_match %s, dfs %s, coverage %s" % (
            k, pt["leaves_mine"], pt["hash_match"],
            pt["dfs_crosscheck"] if pt["dfs_crosscheck"] == "INCOMPLETE" else pt["dfs_crosscheck"]["identical_to_primary"],
            cov["ok"]))

    # ---- rule certificates
    cache = None
    try:
        cache = RLPCache(duals)
    except CertError as e:
        fail("rlp_duals.json", str(e))
    fh5 = {"lines": 0, "nodes": 0, "max_seconds": 0.0, "engine_counts_equal_full_space": 0,
           "full_space_sum_per_placement": 0}
    qstats = {"RLP_q_vectors_checked": 0, "RPLP_R_entries": 0, "RPLP_P_entries": 0}
    for (n, t, repc, code, rule, wit) in lines:
        k = tkey(t)
        if "rules" not in rep["per_type"][k]:
            rep["per_type"][k]["rules"] = {r: {"lines": 0, "verified": 0, "failed": 0, "incomplete": 0} for r in RULES}
        rs = rep["per_type"][k]["rules"][rule]
        rs["lines"] += 1
        if time.time() > deadline:
            rs["incomplete"] += 1
            rep["incomplete"].append({"where": "line %d" % n, "what": "%s witness not checked before deadline" % rule})
            continue
        A = alpha_matrix(repc)
        try:
            need(cache is not None or rule not in ("RLP", "RPLP"), "no usable rlp_duals.json")
            ts = time.time()
            status, extra = check_rule(A, t, rule, wit, cache, deadline)
            if rule == "FH5":
                fh5["lines"] += 1
                fh5["nodes"] += extra["nodes"]
                fh5["max_seconds"] = max(fh5["max_seconds"], round(time.time() - ts, 3))
                fh5["full_space_sum_per_placement"] += extra["space"]
                fh5["engine_counts_equal_full_space"] += bool(extra.get("engine_counts_equal_full_space"))
            mq = re.fullmatch(r"ok \((\d+) q\)", status) if rule == "RLP" else None
            if mq:
                qstats["RLP_q_vectors_checked"] += int(mq.group(1))
            mr = re.fullmatch(r"ok \(R (\d+), P (\d+)\)", status) if rule == "RPLP" else None
            if mr:
                qstats["RPLP_R_entries"] += int(mr.group(1))
                qstats["RPLP_P_entries"] += int(mr.group(2))
            if status == "INCOMPLETE":
                rs["incomplete"] += 1
                rep["incomplete"].append({"where": "line %d" % n, "what": "%s search hit the budget" % rule})
            else:
                rs["verified"] += 1
        except CertError as e:
            rs["failed"] += 1
            fail("line %d %s %s %s" % (n, k, repc, rule), str(e))
    rep["global"]["fh5"] = fh5
    rep["global"]["q_statistics"] = qstats
    log("rule certificates done")

    # ---- global
    g = rep["global"]
    for x in global_survive_check([L[4] for L in lines], survivors, run):
        fail("global", x)
    g["survive_lines"] = sum(1 for L in lines if L[4] == "SURVIVE")
    g["survivors_json_empty"] = survivors in ([], {})
    g["total_lines"] = len(lines)
    g["total_orbits_engine"] = run.get("total_orbits") if isinstance(run, dict) else None
    g["total_orbits_match"] = g["total_orbits_engine"] == len(lines)
    if not g["total_orbits_match"]:
        fail("run.json", "total_orbits mismatch")
    g["rlp_dual_entries"] = len(duals) if isinstance(duals, dict) else None
    g["rlp_dual_entries_match_run_json"] = isinstance(run, dict) and g["rlp_dual_entries"] == run.get("rlp_dual_entries")
    if cache is not None:
        g["rlp_keys_checked"] = len(cache.res)
        g["rlp_keys_passed"] = sum(1 for v in cache.res.values() if v[0])
        g["rlp_keys_failed"] = sum(1 for v in cache.res.values() if not v[0])
        g["rlp_dual_entries_unused"] = len(set(duals) - set(cache.res))
    g["leaves_total_mine"] = sum(pt.get("leaves_mine", 0) for pt in rep["per_type"].values())
    per_rule = {}
    tot = {"lines": 0, "verified": 0, "failed": 0, "incomplete": 0}
    for pt in rep["per_type"].values():
        for r, rs in pt.get("rules", {}).items():
            pr = per_rule.setdefault(r, {"lines": 0, "verified": 0, "failed": 0, "incomplete": 0})
            for x in pr:
                pr[x] += rs[x]
                tot[x] += rs[x]
    g["per_rule"] = {r: v for r, v in per_rule.items() if v["lines"]}
    g["lines_totals"] = tot
    if tot["lines"] != len(lines) or tot["verified"] + tot["failed"] + tot["incomplete"] != len(lines):
        fail("global", "internal bookkeeping mismatch")
    rep["environment"]["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    rep["environment"]["max_rss_bytes_self"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rep["environment"]["elapsed_seconds"] = round(time.time() - t0, 1)
    pass_gate = {"verified_equals_total_lines": tot["verified"] == len(lines),
                 "failed_zero": tot["failed"] == 0, "incomplete_zero": tot["incomplete"] == 0}
    g["pass_gate"] = pass_gate
    if rep["failures"] or tot["failed"] != 0:
        verdict = "FAIL"
    elif rep["incomplete"] or not all(pass_gate.values()):
        verdict = "INCOMPLETE"
    else:
        verdict = "PASS"
    rep["verdict"] = verdict
    rep["failures_total"] = len(rep["failures"])
    rep["failures"] = rep["failures"][:200]
    with open(args.out_json, "x") as f:
        json.dump(rep, f, indent=1, default=str)
        f.write("\n")
    with open(args.out_md, "x") as f:
        f.write(render_md(rep))
    log("verdict %s; reports written" % verdict)
    logf.close()
    return 0 if verdict == "PASS" else 1


def render_md(rep):
    g = rep["global"]
    out = ["# Independent checker report (checker_v2, standard library, one process)\n"]
    out.append("- Verdict: **%s** (failures %d, incomplete parts %d)" % (
        rep["verdict"], rep["failures_total"], len(rep["incomplete"])))
    out.append("- Checker: `%s` sha256 `%s`" % (rep["checker"]["path"], rep["checker"]["sha256"]))
    out.append("- Elapsed: %s s (one process, no numpy)" % (rep["environment"]["elapsed_seconds"],))
    out.append("\n## Inputs (sha256)\n")
    for p, v in rep["inputs"].items():
        out.append("- `%s` %s (%d bytes)" % (p, v["sha256"], v["bytes"]))
    out.append("- orbits.jsonl (uncompressed) %s; equals run.json field: %s" % (
        g.get("orbits_jsonl_uncompressed_sha256"), g.get("orbits_jsonl_uncompressed_sha256_matches_run_json")))
    out.append("\n## Per type\n")
    out.append("| type | leaves (mine) | leaves (run.json) | hash match | edge-DFS = primary | orbit lines | orbits (run.json) | coverage ok | verified | failed | incomplete |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, pt in rep["per_type"].items():
        if "leaves_mine" not in pt:
            out.append("| `%s` | INCOMPLETE | | | | | | | | | |" % k)
            continue
        dc = pt["dfs_crosscheck"]
        dcs = dc["identical_to_primary"] if isinstance(dc, dict) else dc
        rules = pt.get("rules", {})
        ver = sum(r["verified"] for r in rules.values())
        fl = sum(r["failed"] for r in rules.values())
        inc = sum(r["incomplete"] for r in rules.values())
        es = pt.get("engine_summary") or {}
        out.append("| `%s` | %d | %s | %s | %s | %d | %s | %s | %d | %d | %d |" % (
            k, pt["leaves_mine"], es.get("leaves_labelled"), pt["hash_match"], dcs, pt["orbit_lines"],
            es.get("orbits"), pt["orbit_coverage"]["ok"], ver, fl, inc))
    out.append("\nEngine `code` field (informational; CERT-FORMAT says not to rely on it): lines whose `code` lies in the "
               "stabiliser orbit of `rep`, per type: %s; sampled lines whose `code` lies in the full S6 orbit of `rep`: %s." % (
                   {k: pt.get("orbit_coverage", {}).get("code_field_in_stabiliser_orbit_of_rep") for k, pt in rep["per_type"].items()},
                   {k: pt.get("code_field_S6_sample") for k, pt in rep["per_type"].items()}))
    out.append("\n## Per rule (all types)\n")
    out.append("| rule | lines | verified | failed | incomplete |")
    out.append("|---|---|---|---|---|")
    for r, v in g.get("per_rule", {}).items():
        out.append("| %s | %d | %d | %d | %d |" % (r, v["lines"], v["verified"], v["failed"], v["incomplete"]))
    out.append("\n## Global\n")
    for key in ("lines_parsed", "lines_malformed", "survive_lines", "survivors_json_empty", "total_orbits_match",
                "rlp_dual_entries", "rlp_keys_checked", "rlp_keys_passed", "rlp_keys_failed",
                "rlp_dual_entries_unused", "leaves_total_mine", "manifest_lists_input_hashes", "pass_gate"):
        out.append("- %s: %s" % (key, g.get(key)))
    out.append("- FH5: %s" % (g.get("fh5"),))
    out.append("- q statistics: %s" % (g.get("q_statistics"),))
    out.append("- types cover: %s" % (rep.get("types_cover"),))
    if rep["failures"]:
        out.append("\n## First failures\n")
        for f in rep["failures"][:30]:
            out.append("- %s: %s" % (f["where"], f["msg"]))
    if rep["incomplete"]:
        out.append("\n## Incomplete\n")
        for f in rep["incomplete"][:30]:
            out.append("- %s: %s" % (f["where"], f["what"]))
    out.append(STATIC_NOTES)
    out.append("")
    return "\n".join(out)


STATIC_NOTES = """
## Method (what a PASS means)

- **Types.** A placement is (E2 vertex or none, class c2 in {1,2}, E3 vertex or none): 1 + 6 + 6*2 + 6*2*6 = 91
  placements.  Coverage proof: no markers -> (None,0,None); only E3 at x -> any permutation with x->0 gives
  (None,0,0); only E2 at x with class c -> x->0 gives (0,c,None); E2 and E3 both at x -> x->0 gives (0,c,0);
  E2 at x, E3 at y != x -> x->0, y->1 gives (0,c,1).  Presence of each marker, the class and coincidence are
  S6-invariant, so the image type is unique.  Relabelling the six subgroups by a permutation maps a configuration
  to a configuration, so every pattern is equivalent to one with a type's placement.  The stabiliser of a type's
  placement is exactly {p : p(e2)=e2 if present, p(e3)=e3 if present} (E2 and E3 are different markers and are never
  exchanged); sizes 720, 120 (x5), 24 (x2).  `check_types_cover` re-verifies all of this by brute force over S6.
- **Universe.** Primary enumeration: vertex-by-vertex stars, every star in {1..4}^c tried, a triangle tested exactly
  when its last edge is assigned.  Cross-check: an edge-by-edge depth-first enumeration with the scalar T test
  (must give the identical sorted list), plus random and one-edge-neighbour spot checks.  The sorted list is hashed as
  specified and compared with run.json.
- **Orbits.** For each line the checker computes the full stabiliser orbit of `rep` itself; the orbits must be pairwise
  disjoint and their union must equal the leaf set exactly (set equality, not only counts/hash); `rep` must be a
  T-consistent leaf of the line's type.  Every rule is checked on `rep`; a certificate for `rep` transfers to its orbit
  because each rule is label-equivariant and the stabiliser fixes the markers.
- **Rules.** K, RLP (all 31 non-empty supports with every hereditary sub-test, exact Fractions, every admissible q,
  key recomputed), PB/Ppair (grid rounding lo = u*ceil(L/u), hi = u*floor(min/u) then the K2 decrement), FH5
  (exhaustive search over the whole assignment space for all 7 E5 placements; pruning only on rejections that persist),
  N26 (safe form: every admissible tau of every neighbour triple has no prime factor >= 5, and if v = E3 none is
  divisible by 3 and tau_max < 3 tau_min; the '3 | tau_min' alternative is never accepted), RPLP (columns rebuilt:
  every non-empty A closed under the ordered forced pairs, every S subset of A that is empty, a singleton or
  hereditary-allowed; per-q certificate count exact; R keys recomputed).  Any SURVIVE line, malformed line, unknown
  rule, duplicate JSON key, non-string rational or sign violation is a failure.

## Observations on the texts (no effect on this verdict unless stated)

1. CERT-FORMAT-k6-v1 N26 and rules-k6-v3 L11(4) allow '3 | tau_min' as an alternative; that direction is wrong
   (it forces 3 | tau).  Unreachable here because tau_min is a power of 2 under alpha_jk in {2,4}; fixed in
   CERT-FORMAT-k6-v2 / erratum v2 F1.  This checker uses the safe test.
2. CERT-FORMAT-k6-v1 PB wording ('ceil(...) rounded up to a multiple of u') is ambiguous; the integer-ceiling reading
   would be unsound.  This checker uses grid rounding (as in CERT-FORMAT-k6-v2 / erratum v2 F3).
3. The engine `code` field is not, in general, a labelling in the stabiliser orbit of `rep` (counts above); it is in
   the full S6 orbit on every sampled line, i.e. it appears to carry the markers elsewhere.  Coverage here is
   established from `rep` only, as CERT-FORMAT section 3 prescribes.
4. The PB precondition 'every pair has lo <= hi' is not needed for soundness (it is enforced anyway).
5. E5 enters only FH5; for K, P, RLP and RPLP E5-independence is a written argument (alpha, q <= 4 and the gcd
   table involve no factor 5).  For N26 this checker removes the dependence mechanically (prime-support test on
   every admissible tau).
6. What a PASS supports (wording from the delta reviews): no minimal-order Sun(6) counterexample carries a Core5(6)
   configuration, conditional on the written rule proofs, the imports (Zhu k <= 4, accepted Sun(5)), and R1(6).
   This report is a certificate check only; it makes no theorem or novelty claim.
"""


if __name__ == "__main__":
    sys.exit(main())
