#!/usr/bin/env python3
"""bridge_verifier_v1 -- parent finite-bridge verifier for the sun-core5 Core(5) certificate artifact.

Self-contained, standard library only, deterministic, one process.  It imports nothing from the lane
(the engine file is only hashed) and nothing from other parent scripts.

Binding:   extract sha256  e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2
           engine  sha256  65ce5a00cdd513ef55533b3507a8e8a37dcc88e9d389a541978a0f23cb952eb1
Semantics: rules-v1 L1-L8 as re-derived by the parent (identical to the Claude written-proof review,
           section 3): sizes in units of |G|, everything recomputed from (alpha, E2, E3) only.

Usage: python3 bridge_verifier_v1.py OUTDIR EXTRACT_TSV ENGINE_PY RUN_JSON SURVIVORS_JSON CERTS_TSV_GZ
Writes OUTDIR/RESULT.json (exclusive create).  Exit status 0 iff verdict PASS.

Checks (all errors are collected; nothing stops at the first failure):
 (1) independent canonical keys of all 3^10*6^2 = 2,125,764 raw triples; exact set equality with the records
 (2) every serialized witness checked against its own decoded pattern (bounds, totals, V2, counts), no
     first-firing assumption; plus an independent decision of every pattern by the parent's own rules
 (3) strict parsing: malformed records, duplicate / missing / extra keys, invalid vertices, witness shapes,
     inconsistent metadata (run.json, survivors.json, gzip provenance); shown by mutation fixtures
 (4) hashes of this source and of every input in RESULT.json
"""
import gzip
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from math import gcd

EXPECTED_EXTRACT_SHA = "e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2"
EXPECTED_ENGINE_SHA = "65ce5a00cdd513ef55533b3507a8e8a37dcc88e9d389a541978a0f23cb952eb1"
SD_CODE = "1122333333/10"  # proof-v1.md lines 25-28: a01=a02=1, a03=a04=2, other six = 3; E2=1, E3=0
RULES = ("T", "K", "Ppair", "PB", "N2", "FH1", "FH2", "SURVIVE")
CODE_RE = re.compile(r"\A[123]{10}/[0-4-]{2}\Z")
INF = 10 ** 6

EDGES = list(combinations(range(5), 2))  # edge order of the 10-digit code
EIDX = {e: t for t, e in enumerate(EDGES)}
PERMS = list(permutations(range(5)))
MARK = (None, 0, 1, 2, 3, 4)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def lcm(a, b):
    return a * b // gcd(a, b)


def vp(x, p):
    c = 0
    while x % p == 0:
        x //= p
        c += 1
    return c


def ceil_to(x, u):
    q = x / u
    return (-((-q.numerator) // q.denominator)) * u


def floor_to(x, u):
    q = x / u
    return (q.numerator // q.denominator) * u


def is_int(x):
    return type(x) is int


def mch(m):
    return "-" if m is None else str(m)


# ------------------------------------------------------------------ canonical keys
def perm_src(pi):
    src = [None] * 10
    for t, (i, j) in enumerate(EDGES):
        a, b = pi[i], pi[j]
        src[EIDX[(min(a, b), max(a, b))]] = t
    return tuple(src)


PSRC = [(pi, perm_src(pi)) for pi in PERMS]


def inv_perm(pi):
    r = [0] * 5
    for i, j in enumerate(pi):
        r[j] = i
    return tuple(r)


def decode(code):
    a, b = code.split("/")
    f = lambda ch: None if ch == "-" else int(ch)
    return tuple(int(c) for c in a), f(b[0]), f(b[1])


class Universe:
    """Input-independent: canonical code of every raw triple, orbit sizes, own decision of every orbit."""

    def __init__(self):
        t0 = time.time()
        assign = {}
        stabs = {}
        for al in product((1, 2, 3), repeat=10):
            if al in assign:
                continue  # al is the lexicographic minimum of its orbit (lex iteration order)
            st = []
            for pi, src in PSRC:
                b = tuple(al[src[s]] for s in range(10))  # relabelling i -> pi[i]
                if b == al:
                    st.append(pi)
                if b not in assign:
                    assign[b] = (al, inv_perm(pi))
            stabs[al] = st
        self.n_alpha_orbits = len(stabs)
        self.orbit_size = Counter()
        for beta, (rep, sig) in assign.items():
            for e2 in MARK:
                for e3 in MARK:
                    f2 = None if e2 is None else sig[e2]
                    f3 = None if e3 is None else sig[e3]
                    best = min(((9 if f2 is None else tau[f2]), (9 if f3 is None else tau[f3])) for tau in stabs[rep])
                    code = "".join(map(str, rep)) + "/" + "".join("-" if x == 9 else str(x) for x in best)
                    self.orbit_size[code] += 1
        self.raw_triples = sum(self.orbit_size.values())
        self.codes = frozenset(self.orbit_size)
        self.seconds_keys = round(time.time() - t0, 2)
        # own decision of every orbit (no record consulted)
        t1 = time.time()
        self.fcache = {}
        self.decision = {}
        for code in sorted(self.codes):
            p = Pat(code, self)
            h = p.hits_basic()
            fired = sorted(r for r, v in h.items() if v)
            if not fired and p.fh2_any():
                fired = ["FH2"]
            self.decision[code] = fired
        self.own_unkilled = sorted(c for c, f in self.decision.items() if not f)
        self.seconds_decide = round(time.time() - t1, 2)


# ------------------------------------------------------------------ rules (parent re-derivation)
class Pat:
    def __init__(s, code, U=None):
        s.code = code
        al, s.e2, s.e3 = decode(code)
        s.al = {}
        for t, (i, j) in enumerate(EDGES):
            s.al[(i, j)] = al[t]
            s.al[(j, i)] = al[t]
        s.alpha = al
        s.U = U
        s._tm = {}
        s._pb = {}

    def a(s, i, j):
        return s.al[(i, j)]

    def gam(s, opp, a):  # gamma_e: gcd(r_opp, alpha_e) for alpha in {1,2,3}
        if a == 2 and opp == s.e2:
            return 2
        if a == 3 and opp == s.e3:
            return 3
        return 1

    def tmin(s, x, y, z):
        k = frozenset((x, y, z))
        if k not in s._tm:
            t = 1
            for p, q, o in ((x, y, z), (x, z, y), (y, z, x)):
                a = s.a(p, q)
                t = lcm(t, a // s.gam(o, a))
            s._tm[k] = t
        return s._tm[k]

    def tmax(s, x, y, z):
        A, B, C = s.a(x, y), s.a(x, z), s.a(y, z)
        return min(A * B, A * C, B * C)

    def link(s, v, i, j):
        return s.tmin(v, i, j) == s.a(v, i) * s.a(v, j)

    def K2_allowed(s, v, j, k):
        return s.a(v, j) + s.a(k, j) <= 3

    def pbounds(s, v, j, k):
        key = (v, j, k)
        if key in s._pb:
            return s._pb[key]
        xj, xk = Fr(s.a(v, j), 4), Fr(s.a(v, k), 4)
        u = Fr(1, 4 * s.gam(v, s.a(j, k)))
        lo = ceil_to(max(Fr(s.tmin(v, j, k), 4 * s.a(j, k)), xj + xk - 1, Fr(0)), u)
        m = min(xj, xk)
        hi = floor_to(m, u)
        assert hi == m  # x is a multiple of u in Core(5)
        if xj < xk:
            ok = s.K2_allowed(v, j, k)
        elif xk < xj:
            ok = s.K2_allowed(v, k, j)
        else:
            ok = s.K2_allowed(v, j, k) and s.K2_allowed(v, k, j)
        if not ok:
            hi -= u
        s._pb[key] = (lo, hi, u)
        return s._pb[key]

    def PB_val(s, v, S):
        val = sum(1 - Fr(s.a(v, j), 4) for j in S)
        for j, k in combinations(S, 2):
            val -= 1 - Fr(s.a(v, j), 4) - Fr(s.a(v, k), 4) + s.pbounds(v, j, k)[1]
        return val

    def V2_of(s, x, y):
        return [v for v in range(5) if v not in (x, y) and s.a(v, x) == 2 and s.a(v, y) == 2]

    def lamv(s, l, t, m):  # dominating representative: E2/E3 valuations saturated
        a2 = 2 + (INF if l == s.e2 else 0) + vp(t, 2) - vp(m, 2)
        a3 = (INF if l == s.e3 else 0) + vp(t, 3)
        return a2, a3

    def glam(s, x, tx, y, ty, m):
        ax, ay = s.lamv(x, tx, m), s.lamv(y, ty, m)
        e, f = min(ax[0], ay[0]), min(ax[1], ay[1])
        assert e < INF and f < INF
        return 2 ** e * 3 ** f

    def fibre(s, m, inside, fixed):
        """Full enumeration (no symmetry reduction). Returns (admissible_found, examined)."""
        key = (s.code, m, tuple(inside), tuple(sorted(fixed.items())))
        cache = s.U.fcache if s.U is not None else {}
        if key in cache:
            return cache[key]
        opts = {}
        for l in range(5):
            ts = [1] if l in inside else ([fixed[l]] if l in fixed else list(range(1, m + 1)))
            opts[l] = [(t, frozenset(M)) for t in ts for M in combinations(range(m), t)]
        ex = 0
        found = False
        for combo in product(*[opts[l] for l in range(5)]):
            ex += 1
            bad = False
            for l in range(5):  # F3 at every t = 1 vertex
                if combo[l][0] == 1:
                    for l2 in range(5):
                        if l2 != l and s.a(l, l2) * m > 4 * combo[l2][0]:
                            bad = True
                            break
                if bad:
                    break
            if bad:
                continue
            for c in range(m):  # F2: some pair with gcd >= s in every coset with s >= 2
                S = [l for l in range(5) if c in combo[l][1]]
                if len(S) >= 2 and not any(s.glam(x, combo[x][0], y, combo[y][0], m) >= len(S)
                                           for x, y in combinations(S, 2)):
                    bad = True
                    break
            if not bad:
                found = True
                break
        cache[key] = (found, ex)
        return found, ex

    def fh2_cases(s, x, y):
        V2 = s.V2_of(x, y)
        f4, ex4 = s.fibre(4, [x, y], {v: 2 for v in V2})
        f2, ex2 = s.fibre(2, [x, y] + V2, {})
        return V2, (not f4), (not f2), ex4, ex2

    def fh2_any(s):
        for x, y in combinations(range(5), 2):
            if s.a(x, y) == 1 and s.V2_of(x, y):
                _, r1, r2, _, _ = s.fh2_cases(x, y)
                if r1 and r2:
                    return True
        return False

    def hits_basic(s):
        oth = lambda v: [w for w in range(5) if w != v]
        h = {"T": any(s.tmin(*t) > s.tmax(*t) for t in combinations(range(5), 3)),
             "K": any(all(s.link(v, i, j) for i, j in combinations(S, 2)) and sum(s.a(i, v) for i in S) >= 4
                      for v in range(5) for r in (2, 3, 4) for S in combinations(oth(v), r)),
             "Ppair": any(s.pbounds(v, j, k)[0] > s.pbounds(v, j, k)[1]
                          for v in range(5) for j, k in combinations(oth(v), 2)),
             "PB": any(s.PB_val(v, S) >= 1 for v in range(5) for r in (2, 3, 4) for S in combinations(oth(v), r)),
             "N2": all(x == 2 for x in s.alpha)}
        return h


# ------------------------------------------------------------------ strict verification
def sorted_distinct_vertices(L, lo_len, hi_len):
    return (type(L) is list and lo_len <= len(L) <= hi_len and all(is_int(x) for x in L)
            and all(0 <= x <= 4 for x in L) and all(L[i] < L[i + 1] for i in range(len(L) - 1)))


def fr_str_ok(x):
    return type(x) is str and re.fullmatch(r"-?[0-9]+(/[0-9]+)?", x) is not None


def verify(inp, U):
    """inp: dict of bytes: extract, engine, run, survivors, gz.  Returns (errors, stats)."""
    E = []
    err = lambda cat, *d: E.append([cat] + [str(x) for x in d])
    ex_b = inp["extract"]
    # ---- bindings and provenance
    if sha(ex_b) != EXPECTED_EXTRACT_SHA:
        err("bind-extract-sha", sha(ex_b))
    if sha(inp["engine"]) != EXPECTED_ENGINE_SHA:
        err("bind-engine-sha", sha(inp["engine"]))
    try:
        if gzip.decompress(inp["gz"]) != ex_b:
            err("gz-provenance", "decompressed gzip != extract")
    except Exception as e:  # noqa: BLE001
        err("gz-provenance", repr(e))
    # ---- parse
    recs = {}
    order = []
    try:
        txt = ex_b.decode("utf-8", errors="strict")
    except UnicodeDecodeError as e:
        err("malformed-encoding", repr(e))
        txt = ""
    if not txt.endswith("\n"):
        err("malformed-eof", "no final newline")
    if "\r" in txt:
        err("malformed-line", "carriage return present")
    body = txt[:-1] if txt.endswith("\n") else txt
    for ln_no, ln in enumerate(body.split("\n"), 1):
        f = ln.split("\t")
        if len(f) != 3:
            err("malformed-line", ln_no, len(f))
            continue
        code, rule, wjs = f
        if CODE_RE.match(code) is None:
            err("bad-code", ln_no, code)
            continue
        if rule not in RULES:
            err("bad-rule", ln_no, rule)
            continue
        if code in recs:
            err("duplicate-key", ln_no, code)
            continue
        if rule == "SURVIVE":
            if wjs != "-":
                err("bad-witness-shape", ln_no, "SURVIVE witness must be '-'")
                continue
            w = None
        else:
            try:
                w = json.loads(wjs)
            except Exception:  # noqa: BLE001
                err("bad-witness-json", ln_no, wjs)
                continue
            if json.dumps(w, separators=(",", ":")) != wjs:
                err("bad-witness-json", ln_no, "non-canonical serialization")
                continue
            if type(w) is not list:
                err("bad-witness-shape", ln_no, "not a list")
                continue
        recs[code] = (rule, w, ln_no)
        order.append(code)
    # ---- (1) key set equality and orbit coverage
    keys = set(recs)
    missing = sorted(U.codes - keys)
    extra = sorted(keys - U.codes)
    for c in missing:
        err("missing-key", c)
    for c in extra:
        err("extra-key", c)
    okey = lambda c: (c[:10], 5 if c[11] == "-" else int(c[11]), 5 if c[12] == "-" else int(c[12]))
    if order != sorted(order, key=okey):
        err("record-order", "records not in the engine's documented key order (alpha, E2, E3; none = 5)")
    # ---- (2) witnesses against their own decoded patterns
    rule_count = Counter()
    labelled = Counter()
    fh2_log = []
    for code in order:
        if code in extra:
            continue
        rule, w, ln_no = recs[code]
        p = Pat(code, U)
        rule_count[rule] += 1
        labelled[rule] += U.orbit_size[code]
        if rule == "SURVIVE":
            if code != SD_CODE:
                err("survivor-not-SD", code)
            continue
        if rule == "T":
            if not (len(w) == 3 and type(w[0]) is list and len(w[0]) == 3 and all(is_int(x) for x in w[0])
                    and is_int(w[1]) and is_int(w[2])):
                err("bad-witness-shape", code, w)
                continue
            if not sorted_distinct_vertices(w[0], 3, 3):
                err("invalid-vertex", code, w)
                continue
            tri, tm, tM = w
            if p.tmin(*tri) != tm or p.tmax(*tri) != tM:
                err("witness-T-bounds", code, w, p.tmin(*tri), p.tmax(*tri))
            if not p.tmin(*tri) > p.tmax(*tri):
                err("witness-T-nokill", code, w)
        elif rule == "K":
            if not (len(w) == 3 and is_int(w[0]) and type(w[1]) is list and fr_str_ok(w[2])):
                err("bad-witness-shape", code, w)
                continue
            v, S, sstr = w
            if not (0 <= v <= 4 and sorted_distinct_vertices(S, 2, 4) and v not in S):
                err("invalid-vertex", code, w)
                continue
            if not all(p.link(v, i, j) for i, j in combinations(S, 2)):
                err("witness-K-link", code, w)
            tot = Fr(sum(p.a(i, v) for i in S), 4)
            if str(tot) != sstr:
                err("witness-K-total", code, w, tot)
            if tot < 1:
                err("witness-K-nokill", code, w)
        elif rule == "PB":
            if not (len(w) == 3 and is_int(w[0]) and type(w[1]) is list and fr_str_ok(w[2])):
                err("bad-witness-shape", code, w)
                continue
            v, S, vstr = w
            if not (0 <= v <= 4 and sorted_distinct_vertices(S, 2, 4) and v not in S):
                err("invalid-vertex", code, w)
                continue
            val = p.PB_val(v, S)
            if str(val) != vstr:
                err("witness-PB-total", code, w, val)
            if val < 1:
                err("witness-PB-nokill", code, w)
        elif rule == "Ppair":
            if not (len(w) == 4 and is_int(w[0]) and type(w[1]) is list and fr_str_ok(w[2]) and fr_str_ok(w[3])):
                err("bad-witness-shape", code, w)
                continue
            v, jk, los, his = w
            if not (0 <= v <= 4 and sorted_distinct_vertices(jk, 2, 2) and v not in jk):
                err("invalid-vertex", code, w)
                continue
            lo, hi, _ = p.pbounds(v, *jk)
            if str(lo) != los or str(hi) != his:
                err("witness-Ppair-bounds", code, w, lo, hi)
            if not lo > hi:
                err("witness-Ppair-nokill", code, w)
        elif rule == "N2":
            if w != []:
                err("bad-witness-shape", code, w)
                continue
            if not all(x == 2 for x in p.alpha):
                err("witness-N2", code)
        elif rule == "FH1":
            if not (len(w) == 3 and type(w[0]) is list and is_int(w[1]) and is_int(w[2])):
                err("bad-witness-shape", code, w)
                continue
            tri, a, exn = w
            if not sorted_distinct_vertices(tri, 3, 3):
                err("invalid-vertex", code, w)
                continue
            if not (all(p.a(i, j) == 1 for i, j in combinations(tri, 2)) and a == 4):
                err("witness-FH1-source", code, w)
                continue
            found, ex = p.fibre(4, list(tri), {})
            if found:
                err("witness-FH1-admissible", code, w)
            if exn * 4 != ex:
                err("witness-FH1-count", code, w, ex)
        elif rule == "FH2":
            if not (len(w) == 4 and type(w[0]) is list and type(w[1]) is list and is_int(w[2]) and is_int(w[3])):
                err("bad-witness-shape", code, w)
                continue
            xy, V2, e4, e2 = w
            if not (sorted_distinct_vertices(xy, 2, 2) and sorted_distinct_vertices(V2, 1, 3)
                    and not set(V2) & set(xy)):
                err("invalid-vertex", code, w)
                continue
            x, y = xy
            if p.a(x, y) != 1:
                err("witness-FH2-alpha", code, w)
                continue
            myV2, r1, r2, ex4, ex2 = p.fh2_cases(x, y)
            if myV2 != V2:
                err("witness-FH2-V2", code, w, myV2)
                continue
            if not r1:
                err("witness-FH2-case-i-admissible", code, w)
            if not r2:
                err("witness-FH2-case-ii-admissible", code, w)
            # recorded counts = exhaustive search space with one inside vertex pinned to coset 0
            if not (e4 * 4 == ex4 and e2 * 2 == ex2):
                err("witness-FH2-counts", code, w, ex4, ex2)
            fh2_log.append([code, xy, V2, r1, r2, ex4, ex2, e4, e2])
        # own decision must contain the recorded rule (no first-firing assumption)
        if rule != "SURVIVE" and code in U.decision and rule not in U.decision[code]:
            err("own-decision-mismatch", code, rule, U.decision[code])
    survivors = sorted(c for c in order if c in recs and recs[c][0] == "SURVIVE")
    if survivors != [SD_CODE]:
        err("survivor-set", survivors)
    # independent decision: every orbit except S-D must be killed by the parent's own rules
    for c in U.own_unkilled:
        if c != SD_CODE:
            err("own-unkilled", c)
    if SD_CODE not in U.own_unkilled:
        err("own-SD-killed", SD_CODE)
    # ---- metadata: run.json
    try:
        run = json.loads(inp["run"])
    except Exception as e:  # noqa: BLE001
        run = {}
        err("meta-run-json", repr(e))
    if run.get("engine") != "core5_engine_v1" or run.get("engine_sha256") != EXPECTED_ENGINE_SHA:
        err("meta-run-engine", run.get("engine"), run.get("engine_sha256"))
    if run.get("certificates_tsv_sha256_uncompressed") != sha(ex_b):
        err("meta-run-certsha", run.get("certificates_tsv_sha256_uncompressed"))
    if run.get("core5_patterns") != len(recs) or run.get("core5_patterns") != len(U.codes):
        err("meta-run-patterns", run.get("core5_patterns"), len(recs))
    n_alpha = len({c.split("/")[0] for c in recs})
    if run.get("core5_alpha_classes") != n_alpha or n_alpha != U.n_alpha_orbits:
        err("meta-run-alpha", run.get("core5_alpha_classes"), n_alpha)
    if run.get("core5_rule_counts") != dict(rule_count):
        err("meta-run-counts", run.get("core5_rule_counts"), dict(rule_count))
    if run.get("core5_survivors") != rule_count.get("SURVIVE", 0):
        err("meta-run-survivors", run.get("core5_survivors"))
    if run.get("core5_flagged_new_unreviewed") != {"N2": rule_count.get("N2", 0), "FH2": rule_count.get("FH2", 0)}:
        err("meta-run-flagged", run.get("core5_flagged_new_unreviewed"))
    # ---- metadata: survivors.json
    try:
        sv = json.loads(inp["survivors"])
    except Exception as e:  # noqa: BLE001
        sv = None
        err("meta-survivors-json", repr(e))
    if type(sv) is not list or [d.get("code") if type(d) is dict else None for d in sv] != survivors:
        err("meta-survivors-set", sv if type(sv) is not list else [d.get("code") if type(d) is dict else d for d in sv])
    else:
        for d in sv:
            al, e2, e3 = decode(d["code"])
            if set(d) != {"code", "alpha", "E2", "E3", "n_representative"}:
                err("meta-survivors-fields", d["code"], sorted(d))
                continue
            if d["alpha"] != {f"{i}{j}": al[t] for t, (i, j) in enumerate(EDGES)}:
                err("meta-survivors-alpha", d["code"])
            if d["E2"] != e2 or d["E3"] != e3:
                err("meta-survivors-markers", d["code"], d["E2"], d["E3"])
            nr = d["n_representative"]
            ok = type(nr) is list and len(nr) == 5 and all(is_int(x) and x > 0 and x % 4 == 0 for x in nr)
            if ok:
                r = [x // 4 for x in nr]
                ok = all(gcd(r[i], r[j]) == 1 for i, j in combinations(range(5), 2))
                ok = ok and all((r[i] % 2 == 0) == (i == e2) and (r[i] % 3 == 0) == (i == e3) for i in range(5))
            if not ok:
                err("meta-survivors-n", d["code"], nr)
    stats = {"records": len(recs), "rule_counts": dict(rule_count), "labelled_counts": dict(labelled),
             "labelled_total": sum(labelled.values()), "missing": len(missing), "extra": len(extra),
             "fh2": fh2_log}
    return E, stats


# ------------------------------------------------------------------ mutation fixtures
def fixtures(pristine, U):
    ex = pristine["extract"].decode()
    lines = ex[:-1].split("\n")
    idx = {ln.split("\t")[0]: n for n, ln in enumerate(lines)}

    def first(rule):
        return next(n for n, ln in enumerate(lines) if ln.split("\t")[1] == rule)

    def with_lines(L, tail="\n"):
        d = dict(pristine)
        d["extract"] = ("\n".join(L) + tail).encode()
        return d

    def sub(n, new):
        L = list(lines)
        L[n] = new
        return L

    def fields(n):
        return lines[n].split("\t")

    F = []
    nT, nK, nPB, nN2, nFH2 = first("T"), first("K"), first("PB"), first("N2"), first("FH2")
    nSD = idx[SD_CODE]
    # malformed records
    F.append(("M01", "line with two fields", with_lines(sub(nT, "\t".join(fields(nT)[:2]))), "malformed-line"))
    F.append(("M02", "line with four fields", with_lines(sub(nT, lines[nT] + "\tX")), "malformed-line"))
    F.append(("M03", "alpha digit 4 in code", with_lines(sub(nT, "4" + lines[nT][1:])), "bad-code"))
    F.append(("M04", "code without slash", with_lines(sub(nT, lines[nT].replace("/", "", 1))), "bad-code"))
    F.append(("M05", "marker 5 in code", with_lines(sub(nT, lines[nT][:11] + "5" + lines[nT][12:])), "bad-code"))
    F.append(("M06", "unknown rule name", with_lines(sub(nT, "\t".join([fields(nT)[0], "X", fields(nT)[2]]))),
              "bad-rule"))
    F.append(("M07", "CRLF line ending", with_lines(sub(nT, lines[nT] + "\r")), "malformed-line"))
    F.append(("M08", "empty line inside", with_lines(lines[:5] + [""] + lines[5:]), "malformed-line"))
    F.append(("M09", "missing final newline", with_lines(lines, tail=""), "malformed-eof"))
    # duplicate / missing / extra keys
    F.append(("M10", "duplicated record", with_lines(lines[:nT + 1] + [lines[nT]] + lines[nT + 1:]), "duplicate-key"))
    F.append(("M11", "deleted record", with_lines(lines[:nT] + lines[nT + 1:]), "missing-key"))
    # extra: a non-canonical relabelling of an existing pattern (same orbit) added
    code0 = fields(nN2)[0]
    cands = [c for c in (code0[:11] + "44", code0[:11] + "34", code0[:11] + "43") if c not in idx and c not in U.codes]
    F.append(("M12", "extra non-canonical key", with_lines(lines + ["\t".join([cands[0], "SURVIVE", "-"])]),
              "extra-key"))
    # replace a canonical code by a non-canonical member of the same orbit (missing + extra)
    cT, rT, wT = fields(nT)
    alT, e2T, e3T = decode(cT)
    alt = None
    for pi, src in PSRC:
        b = tuple(alT[src[s]] for s in range(10))
        c2 = "".join(map(str, b)) + "/" + mch(None if e2T is None else pi[e2T]) + mch(None if e3T is None else pi[e3T])
        if c2 != cT:
            alt = c2
            break
    F.append(("M13", "canonical key replaced by equivalent non-canonical key",
              with_lines(sub(nT, "\t".join([alt, rT, wT]))), "extra-key"))
    # invalid vertices / witness shapes / JSON
    F.append(("M14", "T triangle uses vertex 5", with_lines(sub(nT, "\t".join([cT, "T", "[[0,1,5],2,1]"]))),
              "invalid-vertex"))
    cK, rK, wK = fields(nK)
    wk = json.loads(wK)
    F.append(("M15", "K vertex 7", with_lines(sub(nK, "\t".join([cK, "K", json.dumps([7] + wk[1:], separators=(",", ":"))]))),
              "invalid-vertex"))
    F.append(("M16", "K set contains its own vertex", with_lines(sub(nK, "\t".join(
        [cK, "K", json.dumps([wk[0], sorted(set(wk[1]) | {wk[0]}), wk[2]], separators=(",", ":"))]))), "invalid-vertex"))
    F.append(("M17", "T witness missing a field", with_lines(sub(nT, "\t".join([cT, "T", json.dumps(json.loads(wT)[:2], separators=(",", ":"))]))),
              "bad-witness-shape"))
    F.append(("M18", "N2 witness with extra payload", with_lines(sub(nN2, "\t".join([code0, "N2", "[1]"]))),
              "bad-witness-shape"))
    wt = json.loads(wT)
    F.append(("M19", "T bound typed as string", with_lines(sub(nT, "\t".join([cT, "T", json.dumps([wt[0], str(wt[1]), wt[2]], separators=(",", ":"))]))),
              "bad-witness-shape"))
    F.append(("M20", "T bound typed as boolean", with_lines(sub(nT, "\t".join([cT, "T", json.dumps([wt[0], True, wt[2]], separators=(",", ":"))]))),
              "bad-witness-shape"))
    F.append(("M21", "non-canonical JSON spacing", with_lines(sub(nT, "\t".join([cT, "T", json.dumps(wt)]))),
              "bad-witness-json"))
    F.append(("M22", "T triangle with repeated vertex", with_lines(sub(nT, "\t".join([cT, "T", json.dumps([[0, 0, 1], wt[1], wt[2]], separators=(",", ":"))]))),
              "invalid-vertex"))
    F.append(("M23", "rule label K on a T-shaped witness", with_lines(sub(nT, "\t".join([cT, "K", wT]))),
              "bad-witness-shape"))
    # recorded bounds / totals / V2 / counts
    F.append(("M24", "T recorded tau_min off by one", with_lines(sub(nT, "\t".join([cT, "T", json.dumps([wt[0], wt[1] + 1, wt[2]], separators=(",", ":"))]))),
              "witness-T-bounds"))
    F.append(("M25", "T recorded tau_max off by one", with_lines(sub(nT, "\t".join([cT, "T", json.dumps([wt[0], wt[1], wt[2] + 1], separators=(",", ":"))]))),
              "witness-T-bounds"))
    # T witness pointing to a triangle that is not killed (true bounds recorded)
    nT2 = cT2 = tri_ok = pT = None
    for n, ln in enumerate(lines):
        c, r, _ = ln.split("\t")
        if r == "T":
            pp = Pat(c)
            tt = [t for t in combinations(range(5), 3) if pp.tmin(*t) <= pp.tmax(*t)]
            if tt:
                nT2, cT2, tri_ok, pT = n, c, tt[0], pp
                break
    F.append(("M26", "T witness on an unkilled triangle with its true bounds", with_lines(sub(nT2, "\t".join(
        [cT2, "T", json.dumps([list(tri_ok), pT.tmin(*tri_ok), pT.tmax(*tri_ok)], separators=(",", ":"))]))),
              "witness-T-nokill"))
    F.append(("M27", "K recorded total altered", with_lines(sub(nK, "\t".join([cK, "K", json.dumps([wk[0], wk[1], "5/4" if wk[2] != "5/4" else "3/2"], separators=(",", ":"))]))),
              "witness-K-total"))
    # K with an unlinked pair, recorded total consistent
    kfix = None
    for n, ln in enumerate(lines):
        c, r, w_ = ln.split("\t")
        pp = Pat(c)
        for v in range(5):
            oth = [x for x in range(5) if x != v]
            for S in combinations(oth, 2):
                if not pp.link(v, *S) and sum(pp.a(i, v) for i in S) >= 4:
                    kfix = (n, c, v, list(S), str(Fr(sum(pp.a(i, v) for i in S), 4)))
                    break
            if kfix:
                break
        if kfix:
            break
    n_, c_, v_, S_, t_ = kfix
    F.append(("M28", "K witness with an unlinked pair (true total recorded)", with_lines(sub(n_, "\t".join(
        [c_, "K", json.dumps([v_, S_, t_], separators=(",", ":"))]))), "witness-K-link"))
    cP, rP, wP = fields(nPB)
    wp = json.loads(wP)
    F.append(("M29", "PB recorded total altered", with_lines(sub(nPB, "\t".join([cP, "PB", json.dumps([wp[0], wp[1], "2"], separators=(",", ":"))]))),
              "witness-PB-total"))
    pP = Pat(cP)
    pbfix = None
    for v in range(5):
        oth = [x for x in range(5) if x != v]
        for r in (2, 3, 4):
            for S in combinations(oth, r):
                if pP.PB_val(v, S) < 1:
                    pbfix = (v, list(S), str(pP.PB_val(v, S)))
                    break
            if pbfix:
                break
        if pbfix:
            break
    F.append(("M30", "PB witness at a vertex/set where Bonferroni does not fail (true value recorded)",
              with_lines(sub(nPB, "\t".join([cP, "PB", json.dumps(list(pbfix), separators=(",", ":"))]))),
              "witness-PB-nokill"))
    cF, rF, wF = fields(nFH2)
    wf = json.loads(wF)
    F.append(("M31", "FH2 recorded V2 shortened", with_lines(sub(nFH2, "\t".join([cF, "FH2", json.dumps([wf[0], wf[1][:-1], wf[2], wf[3]], separators=(",", ":"))]))),
              "witness-FH2-V2"))
    F.append(("M32", "FH2 recorded count altered", with_lines(sub(nFH2, "\t".join([cF, "FH2", json.dumps([wf[0], wf[1], wf[2] - 1, wf[3]], separators=(",", ":"))]))),
              "witness-FH2-counts"))
    # FH2 on a pair whose alpha is not 1
    pF = Pat(cF)
    bad_pair = next([x, y] for x, y in combinations(range(5), 2) if pF.a(x, y) != 1)
    bad_V2 = [v for v in range(5) if v not in bad_pair][:1]
    F.append(("M33", "FH2 pair with alpha != 1", with_lines(sub(nFH2, "\t".join([cF, "FH2", json.dumps([bad_pair, bad_V2, wf[2], wf[3]], separators=(",", ":"))]))),
              "witness-FH2-alpha"))
    # one-case-only FH2 certificate (exactly one H2 alternative refuted) must be rejected
    onecase = None
    for n, ln in enumerate(lines):
        c, r, _ = ln.split("\t")
        pp = Pat(c, U)
        for x, y in combinations(range(5), 2):
            if pp.a(x, y) == 1 and pp.V2_of(x, y):
                V2, r1, r2, ex4, ex2 = pp.fh2_cases(x, y)
                if r1 != r2:
                    onecase = (n, c, [x, y], V2, ex4 // 4, ex2 // 2, r1, r2)
                    break
        if onecase:
            break
    n_, c_, xy_, V2_, e4_, e2_, r1_, r2_ = onecase
    F.append(("M34", f"one-case-only FH2 certificate ({'case ii' if r2_ else 'case i'} refuted only) at {c_}",
              with_lines(sub(n_, "\t".join([c_, "FH2", json.dumps([xy_, V2_, e4_, e2_], separators=(",", ":"))]))),
              "witness-FH2-case-i-admissible" if not r1_ else "witness-FH2-case-ii-admissible"))
    # survivors
    F.append(("M35", "killable pattern relabelled SURVIVE", with_lines(sub(nT, "\t".join([cT, "SURVIVE", "-"]))),
              "survivor-not-SD"))
    F.append(("M36", "S-D record given a forged T certificate", with_lines(sub(nSD, "\t".join(
        [SD_CODE, "T", json.dumps([[0, 1, 2], 1, 1], separators=(",", ":"))]))), "witness-T-nokill"))
    F.append(("M37", "S-D record forged as N2", with_lines(sub(nSD, "\t".join([SD_CODE, "N2", "[]"]))), "witness-N2"))
    # metadata
    run = json.loads(pristine["run"])
    r2 = dict(run)
    r2["core5_rule_counts"] = dict(run["core5_rule_counts"], T=run["core5_rule_counts"]["T"] + 1)
    d = dict(pristine)
    d["run"] = json.dumps(r2).encode()
    F.append(("M38", "run.json rule counts inconsistent", d, "meta-run-counts"))
    r3 = dict(run)
    r3["engine_sha256"] = "0" * 64
    d = dict(pristine)
    d["run"] = json.dumps(r3).encode()
    F.append(("M39", "run.json engine sha altered", d, "meta-run-engine"))
    r4 = dict(run)
    r4["certificates_tsv_sha256_uncompressed"] = "f" * 64
    d = dict(pristine)
    d["run"] = json.dumps(r4).encode()
    F.append(("M40", "run.json certificate sha altered", d, "meta-run-certsha"))
    sv = json.loads(pristine["survivors"])
    s2 = [dict(sv[0], E2=2)]
    d = dict(pristine)
    d["survivors"] = json.dumps(s2).encode()
    F.append(("M41", "survivors.json marker altered", d, "meta-survivors-markers"))
    s3 = [dict(sv[0], n_representative=[1620, 448, 44, 52, 66])]
    d = dict(pristine)
    d["survivors"] = json.dumps(s3).encode()
    F.append(("M42", "survivors.json representative indices inconsistent", d, "meta-survivors-n"))
    d = dict(pristine)
    d["survivors"] = b"[]"
    F.append(("M43", "survivors.json empty", d, "meta-survivors-set"))
    d = dict(pristine)
    d["engine"] = pristine["engine"] + b"\n"
    F.append(("M44", "engine bytes altered", d, "bind-engine-sha"))
    d = dict(pristine)
    d["gz"] = gzip.compress(pristine["extract"].replace(b"\tT\t", b"\tK\t", 1), mtime=0)
    F.append(("M45", "gzip artifact differs from extract", d, "gz-provenance"))
    F.append(("M46", "records out of sorted order", with_lines([lines[1], lines[0]] + lines[2:]), "record-order"))
    return F


def main():
    outdir = sys.argv[1]
    paths = dict(zip(("extract", "engine", "run", "survivors", "gz"), sys.argv[2:7]))
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        me = sha(f.read())
    inp = {}
    for k, pth in paths.items():
        with open(pth, "rb") as f:
            inp[k] = f.read()
    U = Universe()
    errors, stats = verify(inp, U)
    fx = []
    for fid, desc, mutated, expect in fixtures(inp, U):
        e2, _ = verify(mutated, U)
        cats = sorted({e[0] for e in e2})
        fx.append({"id": fid, "mutation": desc, "expected_category": expect, "observed_categories": cats,
                   "rejected": bool(e2), "rejected_for_expected_reason": expect in cats})
    fixtures_ok = all(f["rejected"] and f["rejected_for_expected_reason"] for f in fx)
    verdict = "PASS" if (not errors and fixtures_ok) else "FAIL"
    R = {
        "verifier": "bridge_verifier_v1", "verifier_sha256": me, "python": sys.version,
        "binding": {"extract_sha256_expected": EXPECTED_EXTRACT_SHA, "engine_sha256_expected": EXPECTED_ENGINE_SHA},
        "inputs": {k: {"path": os.path.abspath(p), "sha256": sha(inp[k]), "bytes": len(inp[k])} for k, p in paths.items()},
        "universe": {"raw_triples": U.raw_triples, "alpha_orbits": U.n_alpha_orbits, "orbits": len(U.codes),
                     "seconds_keys": U.seconds_keys, "seconds_own_decision": U.seconds_decide},
        "own_decision": {"unkilled_orbits": U.own_unkilled,
                         "hitset_histogram": dict(Counter("+".join(v) if v else "NONE" for v in U.decision.values()))},
        "pristine_errors": errors, "stats": stats,
        "fixtures": fx, "fixtures_all_rejected_for_expected_reason": fixtures_ok,
        "verdict": verdict, "seconds": round(time.time() - t0, 2),
    }
    with open(os.path.join(outdir, "RESULT.json"), "x") as f:
        json.dump(R, f, indent=1, default=str)
    print(json.dumps({"verdict": verdict, "pristine_errors": len(errors), "records": stats["records"],
                      "rule_counts": stats["rule_counts"], "labelled_counts": stats["labelled_counts"],
                      "labelled_total": stats["labelled_total"], "own_unkilled": U.own_unkilled,
                      "fixtures": [(f["id"], f["rejected_for_expected_reason"]) for f in fx],
                      "verifier_sha256": me, "seconds": R["seconds"]}))
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
