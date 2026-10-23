#!/usr/bin/env python3
"""Sun(6) Core5(6) second independent certificate checker, version 1.

Written only from the Sun(6) mathematical texts (README R0/R1(6); rules-k6-v1, -v2, -v3;
proof-k6-lemmas-v1; cumulative erratum rules-k6-erratum-v3 items C1-C22; CERT-FORMAT-k6-v3
sections 0-4 and 6; ACCEPTANCE-AMENDMENT-v1 overlay) and the pinned untrusted engine output.
No engine source, no earlier checker source and no old control source was read.

Standard library only. Every mathematical decision uses exact int or fractions.Fraction.
The engine `code` field is parsed but never used: orbits are identified by (type, rep).

Exit codes: 0 PASS (sealed), 1 FAIL, 2 INCOMPLETE (deadline/cancel/late), 3 INPUT REJECTED,
4 PUBLICATION FAILURE, 5 INTERNAL ERROR.  Only exit 0 together with a verified seal file
whose verdict is PASS constitutes a PASS.
"""

import argparse
import gzip
import hashlib
import itertools
import json
import math
import operator
import os
import re
import signal
import sys
import time
import zlib
from fractions import Fraction
from math import gcd

CHECKER_ID = "sun6-second-checker-v1"

# ---------------------------------------------------------------------------
# Input pins (entry verdict efe1d849..., parent input pins MANIFEST-v1).
# ---------------------------------------------------------------------------
INPUT_NAMES = ("run.json", "orbits.jsonl.gz", "rlp_duals.json", "survivors.json")
INPUT_PINS = {
    "run.json": (2853, "6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754"),
    "orbits.jsonl.gz": (407387, "a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49"),
    "rlp_duals.json": (106879, "bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef"),
    "survivors.json": (2, "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"),
}
ORBITS_PLAIN_PIN = (6337747, "f4f69363a1a602ec56f3a957566e566d2f03f988792a8d04565d2cce31976579")

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_INCOMPLETE = 2
EXIT_INPUT_REJECTED = 3
EXIT_PUBLICATION = 4
EXIT_INTERNAL = 5

# ---------------------------------------------------------------------------
# Combinatorial constants.
# ---------------------------------------------------------------------------
SAT = 64                      # saturation exponent (>= every threshold in CERT-FORMAT 3/6)
ALPHAS = (1, 2, 3, 4)         # L0.3 in Core5(6)
VERTICES = tuple(range(6))
COSETS = tuple(range(5))      # m = 5 left cosets of H in FH5
TYPES = ((None, 0, None), (None, 0, 0), (0, 1, None), (0, 1, 0), (0, 1, 1),
         (0, 2, None), (0, 2, 0), (0, 2, 1))
EDGE_ORDER_E = tuple((i, j) for j in range(6) for i in range(j))
if EDGE_ORDER_E != ((0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4),
                    (3, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)):
    raise RuntimeError("edge order E construction")
E_INDEX = {p: n for n, p in enumerate(EDGE_ORDER_E)}
LEX_PAIRS = tuple((i, j) for i in range(6) for j in range(i + 1, 6))
LEX_INDEX = {p: n for n, p in enumerate(LEX_PAIRS)}
TRIANGLES = tuple(itertools.combinations(range(6), 3))
FIVE_PAIRS = tuple(itertools.combinations(range(5), 2))   # lexicographic pair order of N positions
RULE_NAMES = ("K", "RLP", "PB", "Ppair", "FH5", "N26", "RPLP", "SURVIVE")
RAT_RE = re.compile(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?")
KEY_RE = re.compile(r"[1-4](,[1-4]){4}\|[0-2][01](;[0-2][01]){4}")
CODE_RE = re.compile(r"[1-4]{15}")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
RAT_MAX_LEN = 64
FAIL_DETAIL_CAP = 400
GUARD_STRIDE = 2048
E5_PLACEMENTS = (None, 0, 1, 2, 3, 4, 5)


def type_key(tp):
    """run.json string form of a type, e.g. "(None, 0, None)"."""
    return "(" + ", ".join("None" if x is None else str(x) for x in tp) + ")"


def expected_stabilizer_size(tp):
    e2, _c2, e3 = tp
    fixed = set(x for x in (e2, e3) if x is not None)
    return math.factorial(6 - len(fixed))


# ---------------------------------------------------------------------------
# Exceptions and lifecycle guard.
# ---------------------------------------------------------------------------
class InputRejected(Exception):
    def __init__(self, reason, detail=""):
        Exception.__init__(self, reason, detail)
        self.reason = reason
        self.detail = str(detail)[:300]


class WitnessFail(Exception):
    def __init__(self, reason, detail=""):
        Exception.__init__(self, reason, detail)
        self.reason = reason
        self.detail = str(detail)[:300]


class StopRequested(Exception):
    def __init__(self, reason):
        Exception.__init__(self, reason)
        self.reason = reason


class Guard:
    """Latched stop: deadline (absolute ns), cancel file, or an external flag (signals)."""

    def __init__(self, deadline_ns, cancel_file=None, clock_ns=time.time_ns):
        if type(deadline_ns) is not int:
            raise TypeError("deadline_ns must be int")
        self.deadline_ns = deadline_ns
        self.cancel_file = cancel_file
        self.clock_ns = clock_ns
        self.flag = None
        self.triggered = None
        self.checks = 0

    def request_cancel(self, why):
        if self.flag is None:
            self.flag = str(why)

    def state(self):
        if self.triggered is None:
            if self.flag is not None:
                self.triggered = "CANCELLED:" + self.flag
            elif self.cancel_file is not None and os.path.lexists(self.cancel_file):
                self.triggered = "CANCELLED:cancel-file"
            elif self.clock_ns() >= self.deadline_ns:
                self.triggered = "DEADLINE"
        return self.triggered

    def check(self):
        self.checks += 1
        if self.state() is not None:
            raise StopRequested(self.triggered)


# ---------------------------------------------------------------------------
# Strict parsing helpers.
# ---------------------------------------------------------------------------
class FloatToken:
    """A JSON float, admitted only at informational run.json `seconds` paths."""
    __slots__ = ("text",)

    def __init__(self, text):
        self.text = text


def _reject_float(text):
    raise InputRejected("FLOAT_REJECTED", text[:40])


def _reject_constant(text):
    raise InputRejected("CONSTANT_REJECTED", text)


def _pairs_no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise InputRejected("DUPLICATE_KEY", k[:80])
        out[k] = v
    return out


def strict_json(raw, allow_float=False, what="json"):
    if type(raw) is not bytes:
        raise InputRejected("NOT_BYTES", what)
    if not raw.isascii():
        raise InputRejected("NOT_ASCII", what)
    if b"\r" in raw:
        raise InputRejected("CR_PRESENT", what)
    try:
        return json.loads(raw.decode("ascii"), object_pairs_hook=_pairs_no_duplicates,
                          parse_float=(FloatToken if allow_float else _reject_float),
                          parse_constant=_reject_constant)
    except InputRejected:
        raise
    except (ValueError, RecursionError) as exc:
        raise InputRejected("JSON_ERROR", "%s: %s" % (what, str(exc)[:200]))


def parse_rational(s):
    """Exact rational from a canonical decimal string; None if not admissible."""
    if type(s) is not str or len(s) > RAT_MAX_LEN or RAT_RE.fullmatch(s) is None:
        return None
    if "/" in s:
        num, den = s.split("/")
        return Fraction(int(num), int(den))
    return Fraction(int(s))


def is_vertex(x):
    return type(x) is int and 0 <= x <= 5


def sha256_hex(b):
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------------------
# Marker statuses (CERT-FORMAT 0-1; rules-k6-v1 0; erratum C5, C7, C16).
# ---------------------------------------------------------------------------
class Status:
    """Marker statuses of a type: E2 vertex and class, E3 vertex (E5 handled only in FH5)."""
    __slots__ = ("e2", "c2", "e3")

    def __init__(self, tp):
        self.e2, self.c2, self.e3 = tp

    def is_e2(self, z):
        return self.e2 is not None and z == self.e2

    def is_e3(self, z):
        return self.e3 is not None and z == self.e3

    def r2(self, z):
        """Exponent used for v2(r_z): 0 (odd), 1 (class 1, exact), SAT (class 2, v2 >= 2)."""
        if self.is_e2(z):
            return 1 if self.c2 == 1 else SAT
        return 0

    def r3(self, z):
        """Exponent used for v3(r_z): SAT for E3 (v3 >= 1), else 0."""
        return SAT if self.is_e3(z) else 0

    def class_digit(self, z):
        return self.c2 if self.is_e2(z) else 0

    def e3_flag(self, z):
        return 1 if self.is_e3(z) else 0


def v_p(n, p):
    if type(n) is not int or n <= 0:
        raise ValueError("v_p of non-positive int")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def lcm(a, b):
    return a // gcd(a, b) * b


def gcd_alpha_r(alpha, st, z):
    """gcd(alpha, r_z) for alpha in 1..4: only primes 2, 3 can divide alpha."""
    return 2 ** min(v_p(alpha, 2), st.r2(z)) * 3 ** min(v_p(alpha, 3), st.r3(z))


def tri_bounds(a_ij, a_ik, a_jk, i, j, k, st):
    """(tau_min, tau_max) of triangle {i,j,k} (rules-k6-v1 L1; CERT-FORMAT 2)."""
    t1 = a_ij // gcd_alpha_r(a_ij, st, k)     # edge ij, opposite vertex k
    t2 = a_ik // gcd_alpha_r(a_ik, st, j)     # edge ik, opposite vertex j
    t3 = a_jk // gcd_alpha_r(a_jk, st, i)     # edge jk, opposite vertex i
    tmin = lcm(lcm(t1, t2), t3)
    tmax = min(a_ij * a_ik, a_ij * a_jk, a_ik * a_jk)   # products at i, j, k
    return tmin, tmax


def tau_min_max(A, st, x, y, z):
    i, j, k = sorted((x, y, z))
    return tri_bounds(A[i][j], A[i][k], A[j][k], i, j, k, st)


def t_consistent(A, st):
    for (i, j, k) in TRIANGLES:
        tmin, tmax = tri_bounds(A[i][j], A[i][k], A[j][k], i, j, k, st)
        if tmin > tmax:
            return False
    return True


def matrix_from_code(code):
    """Symmetric 6x6 alpha matrix from a 15-character E-order string over 1..4."""
    A = [[0] * 6 for _ in range(6)]
    for ch, (i, j) in zip(code, EDGE_ORDER_E):
        a = ord(ch) - 48
        A[i][j] = a
        A[j][i] = a
    return A


def lexkey_from_code(code):
    return "".join(code[E_INDEX[p]] for p in LEX_PAIRS)


def code_from_lexkey(key):
    return "".join(key[LEX_INDEX[p]] for p in EDGE_ORDER_E)


# ---------------------------------------------------------------------------
# Universe: T-consistent labelled leaves, vertex-incremental in descending order.
# ---------------------------------------------------------------------------
def triangle_tables(st):
    tables = {}
    for (i, j, k) in TRIANGLES:
        ok = set()
        for a in ALPHAS:
            for b in ALPHAS:
                for c in ALPHAS:
                    tmin, tmax = tri_bounds(a, b, c, i, j, k, st)
                    if tmin <= tmax:
                        ok.add((a, b, c))
        tables[(i, j, k)] = frozenset(ok)
    return tables


def enumeration_schedule():
    """15 edge steps; each triangle is tested exactly once, when its last edge is set."""
    order = (5, 4, 3, 2, 1, 0)
    steps = []
    tested = []
    for idx in range(1, 6):
        k = order[idx]
        placed = order[:idx]
        for pos in range(idx):
            m = placed[pos]
            tris = []
            for m2 in placed[:pos]:
                tri = tuple(sorted((k, m, m2)))
                tris.append(tri)
                tested.append(tri)
            steps.append((k, m, tuple(tris)))
    if len(steps) != 15 or sorted(tested) != sorted(TRIANGLES):
        raise RuntimeError("enumeration schedule does not test each triangle exactly once")
    if sorted(tuple(sorted((k, m))) for (k, m, _t) in steps) != sorted(LEX_PAIRS):
        raise RuntimeError("enumeration schedule does not set each edge exactly once")
    return tuple(steps)


def enumerate_leaves(st, guard):
    """Set of lex keys of all T-consistent labellings for the marker statuses st."""
    tables = triangle_tables(st)
    steps = enumeration_schedule()
    A = [[0] * 6 for _ in range(6)]
    leaves = set()
    nodes = [0]

    def rec(s):
        if s == 15:
            leaves.add("".join(chr(48 + A[i][j]) for (i, j) in LEX_PAIRS))
            return
        k, m, tris = steps[s]
        for a in ALPHAS:
            nodes[0] += 1
            if nodes[0] % GUARD_STRIDE == 0:
                guard.check()
            A[k][m] = a
            A[m][k] = a
            good = True
            for (i, j, l) in tris:
                if (A[i][j], A[i][l], A[j][l]) not in tables[(i, j, l)]:
                    good = False
                    break
            if good:
                rec(s + 1)
        A[k][m] = 0
        A[m][k] = 0

    rec(0)
    return leaves, nodes[0]


def stabilizer(tp):
    e2, _c2, e3 = tp
    return [p for p in itertools.permutations(range(6))
            if (e2 is None or p[e2] == e2) and (e3 is None or p[e3] == e3)]


def lex_image_getters(perms):
    """For each p: lex key of p.A, where (p.A)[p(i)][p(j)] = A[i][j]."""
    getters = []
    for p in perms:
        pinv = [0] * 6
        for i in range(6):
            pinv[p[i]] = i
        src = []
        for (i, j) in LEX_PAIRS:
            a, b = pinv[i], pinv[j]
            if a > b:
                a, b = b, a
            src.append(LEX_INDEX[(a, b)])
        getters.append(operator.itemgetter(*src))
    return getters


def orbit_of(key, getters):
    return {"".join(g(key)) for g in getters}


def missing_orbit_count(missing, getters, guard):
    left = set(missing)
    n = 0
    while left:
        guard.check()
        k = next(iter(left))
        left -= orbit_of(k, getters)
        n += 1
    return n


def check_coverage(items, leaves, getters, guard):
    """items: list of (lineno, lexkey). Exact disjoint-orbit cover of `leaves`."""
    owner = {}
    out = {"rep_not_leaf": [], "image_not_leaf": [], "duplicate": [], "orbits_owned": 0}
    for (lineno, key) in items:
        guard.check()
        if key not in leaves:
            out["rep_not_leaf"].append(lineno)
            continue
        imgs = orbit_of(key, getters)
        if any(im not in leaves for im in imgs):
            out["image_not_leaf"].append(lineno)
            continue
        clash = sorted(set(owner[im] for im in imgs if im in owner))
        if clash:
            out["duplicate"].append([lineno, clash[0]])
            continue
        for im in imgs:
            owner[im] = lineno
        out["orbits_owned"] += 1
    covered = set(owner)
    missing = leaves - covered
    out["covered"] = len(covered)
    out["missing"] = len(missing)
    out["missing_orbits"] = missing_orbit_count(missing, getters, guard)
    out["missing_examples"] = sorted(code_from_lexkey(k) for k in missing)[:20]
    out["set_equal"] = (covered == leaves)
    out["clean"] = (out["set_equal"] and not out["rep_not_leaf"] and not out["image_not_leaf"]
                    and not out["duplicate"])
    return out


def placement_reduction():
    """Every placement of (E2 with class, E3) maps onto exactly one of the 8 types under S6."""
    placements = []
    for e2 in [None] + [(x, c) for x in range(6) for c in (1, 2)]:
        for e3 in [None] + list(range(6)):
            placements.append((e2, e3))
    exactly_one = 0
    bad = []
    perms = list(itertools.permutations(range(6)))
    for (e2, e3) in placements:
        reached = set()
        for p in perms:
            img_e2 = None if e2 is None else (p[e2[0]], e2[1])
            img_e3 = None if e3 is None else p[e3]
            for tp in TYPES:
                t_e2 = None if tp[0] is None else (tp[0], tp[1])
                if img_e2 == t_e2 and img_e3 == tp[2]:
                    reached.add(tp)
        if len(reached) == 1:
            exactly_one += 1
        else:
            bad.append([str(e2), str(e3), len(reached)])
    return {"placements": len(placements), "exactly_one": exactly_one, "bad": bad[:20],
            "ok": len(placements) == 91 and exactly_one == 91}


# ---------------------------------------------------------------------------
# Shared rule context.
# ---------------------------------------------------------------------------
class RuleContext:
    def __init__(self, duals, guard):
        self.duals = duals                 # key -> tuple of 5 Fractions
        self.guard = guard
        self.dual_cache = {}               # (q, st5) -> None (valid) or (reason, detail)
        self.allowed_cache = {}            # (q, st5) -> tuple of allowed non-empty masks
        self.used_keys = set()
        self.fg_cache = {}                 # (type, e5) -> FH5 fgcd table
        self.stats = {"rlp_q_checks": 0, "rplp_R_refs": 0, "rplp_P_vectors": 0,
                      "rplp_columns_checked": 0, "fh5_placements": 0, "fh5_nodes": 0,
                      "fh5_domain_total": 0, "fh5_pruned_weight": 0}


def neighbours(st, v):
    N = tuple(j for j in range(6) if j != v)
    st5 = tuple((st.class_digit(j), st.e3_flag(j)) for j in N)
    return N, st5


def dual_key(q, st5):
    return ",".join(str(x) for x in q) + "|" + ";".join("%d%d" % (d, f) for (d, f) in st5)


def mask_members(mask):
    return tuple(x for x in range(5) if (mask >> x) & 1)


def hereditary_ok(members, pairval):
    """Every T subset of members with |T| >= 2 has a pair with pairval >= |T| (rules-k6-v2 L9)."""
    n = len(members)
    for size in range(2, n + 1):
        for T in itertools.combinations(members, size):
            if not any(pairval(x, y) >= size for (x, y) in itertools.combinations(T, 2)):
                return False
    return True


def allowed_masks(q, st5, ctx):
    """Non-empty supports S (bitmasks over N positions) allowed with maxgcd (CERT-FORMAT 3 RLP)."""
    ck = (q, st5)
    hit = ctx.allowed_cache.get(ck)
    if hit is not None:
        return hit
    e2 = [v_p(q[x], 2) + (0, 1, SAT)[st5[x][0]] for x in range(5)]
    e3 = [v_p(q[x], 3) + (SAT if st5[x][1] else 0) for x in range(5)]

    def maxgcd(x, y):
        return 2 ** min(e2[x], e2[y]) * 3 ** min(e3[x], e3[y])

    out = []
    for mask in range(1, 32):
        mem = mask_members(mask)
        if len(mem) == 1 or hereditary_ok(mem, maxgcd):
            out.append(mask)
    res = tuple(out)
    ctx.allowed_cache[ck] = res
    return res


def dual_condition(q, st5, y, ctx):
    """None if y certifies LPmin(q) >= 1 (CERT-FORMAT 3 RLP), else (reason, detail)."""
    for x in range(5):
        if y[x] < 0:
            return ("NEGATIVE", "position %d" % x)
    for mask in allowed_masks(q, st5, ctx):
        if sum((y[x] for x in mask_members(mask)), Fraction(0)) > 1:
            return ("PACKING", "support %s" % list(mask_members(mask)))
    if sum((Fraction(q[x], 5) * y[x] for x in range(5)), Fraction(0)) < 1:
        return ("OBJECTIVE", "")
    return None


def check_q_dual(q, st5, ctx, prefix):
    ck = (q, st5)
    if ck in ctx.dual_cache:
        res = ctx.dual_cache[ck]
    else:
        key = dual_key(q, st5)
        y = ctx.duals.get(key)
        if y is None:
            res = ("KEY_MISSING", key)
        else:
            ctx.used_keys.add(key)
            res = dual_condition(q, st5, y, ctx)
        ctx.dual_cache[ck] = res
    if res is not None:
        raise WitnessFail(prefix + "_" + res[0], "q=%s %s" % (list(q), res[1]))


def q_vectors(A, v, N):
    return list(itertools.product(*[range(1, 6 - A[v][j]) for j in N]))


# ---------------------------------------------------------------------------
# K (rules-k6-v1 L3 with K1; CERT-FORMAT 3 "K").
# ---------------------------------------------------------------------------
def verify_K(A, st, w):
    if type(w) is not list or len(w) != 2:
        raise WitnessFail("K_SHAPE", "witness")
    v, S = w
    if not is_vertex(v) or type(S) is not list:
        raise WitnessFail("K_SHAPE", "v/S")
    if any(not is_vertex(i) or i == v for i in S) or len(set(S)) != len(S):
        raise WitnessFail("K_SHAPE", "S not a duplicate-free subset of N")
    if sum(A[i][v] for i in S) < 5:
        raise WitnessFail("K_SUM", "sum=%d" % sum(A[i][v] for i in S))
    for (i, j) in itertools.combinations(S, 2):
        tmin, _tmax = tau_min_max(A, st, i, v, j)
        if tmin != A[i][v] * A[v][j]:
            raise WitnessFail("K_LINK", "pair %d,%d tau_min=%d" % (i, j, tmin))
    return {"v": v, "S": sorted(S)}


# ---------------------------------------------------------------------------
# RLP (rules-k6-v1 L7 + rules-k6-v2 L9; CERT-FORMAT 3 "RLP", 6.4).
# ---------------------------------------------------------------------------
def verify_RLP(A, st, w, ctx):
    if type(w) is not list or len(w) != 1 or not is_vertex(w[0]):
        raise WitnessFail("RLP_SHAPE", "witness")
    v = w[0]
    N, st5 = neighbours(st, v)
    n = 0
    for q in q_vectors(A, v, N):
        ctx.stats["rlp_q_checks"] += 1
        check_q_dual(q, st5, ctx, "RLP")
        n += 1
    return {"v": v, "q_checked": n}


# ---------------------------------------------------------------------------
# P (rules-k6-v1 L4; erratum C13; CERT-FORMAT 3 "PB"/"Ppair", 6.7).
# ---------------------------------------------------------------------------
def p_bounds(A, st, v, j, k):
    xj = Fraction(A[v][j], 5)
    xk = Fraction(A[v][k], 5)
    ajk = A[j][k]
    u = Fraction(1, 5 * gcd_alpha_r(ajk, st, v))
    tmin, _tmax = tau_min_max(A, st, v, j, k)
    lb = max(Fraction(tmin, 5 * ajk), xj + xk - 1, Fraction(0))
    lo = u * math.ceil(lb / u)
    mn = min(xj, xk)
    hi = u * math.floor(mn / u)
    if hi == mn:
        j_in_k_ok = A[v][j] + ajk <= 4      # K2 for X_j subset X_k
        k_in_j_ok = A[v][k] + ajk <= 4      # K2 for X_k subset X_j
        if xj < xk:
            barred = not j_in_k_ok
        elif xk < xj:
            barred = not k_in_j_ok
        else:
            barred = not (j_in_k_ok and k_in_j_ok)
        if barred:
            hi = hi - u
    return lo, hi, u


def verify_Ppair(A, st, w):
    if type(w) is not list or len(w) != 2 or not is_vertex(w[0]) or type(w[1]) is not list \
            or len(w[1]) != 2:
        raise WitnessFail("PPAIR_SHAPE", "witness")
    v = w[0]
    j, k = w[1]
    if not is_vertex(j) or not is_vertex(k) or j == k or j == v or k == v:
        raise WitnessFail("PPAIR_SHAPE", "pair")
    lo, hi, _u = p_bounds(A, st, v, j, k)
    if not lo > hi:
        raise WitnessFail("PPAIR_NOT_KILL", "lo=%s hi=%s" % (lo, hi))
    return {"v": v, "pair": [j, k]}


def verify_PB(A, st, w):
    if type(w) is not list or len(w) != 2 or not is_vertex(w[0]) or type(w[1]) is not list:
        raise WitnessFail("PB_SHAPE", "witness")
    v, S = w
    if any(not is_vertex(i) or i == v for i in S) or len(set(S)) != len(S):
        raise WitnessFail("PB_SHAPE", "S not a duplicate-free subset of N")
    N = [j for j in range(6) if j != v]
    hi = {}
    for (j, k) in itertools.combinations(N, 2):
        lo_jk, hi_jk, _u = p_bounds(A, st, v, j, k)
        if lo_jk > hi_jk:
            raise WitnessFail("PB_PAIR_LO_GT_HI", "pair %d,%d" % (j, k))
        hi[(j, k)] = hi_jk
    Ss = sorted(S)
    x = {j: Fraction(A[v][j], 5) for j in N}
    total = sum((1 - x[j] for j in Ss), Fraction(0))
    total -= sum((1 - x[j] - x[k] + hi[(j, k)] for (j, k) in itertools.combinations(Ss, 2)),
                 Fraction(0))
    if total < 1:
        raise WitnessFail("PB_BOUND", "value=%s" % total)
    return {"v": v, "S": Ss}


# ---------------------------------------------------------------------------
# N26 (rules-k6-v3 L11; proof-k6-lemmas-v1 3; erratum C11, C14; CERT-FORMAT 6.6).
# ---------------------------------------------------------------------------
def verify_N26(A, st, w):
    if type(w) is not list or len(w) != 1 or not is_vertex(w[0]):
        raise WitnessFail("N26_SHAPE", "witness")
    v = w[0]
    if st.is_e2(v):
        raise WitnessFail("N26_V_IS_E2", "v=%d" % v)
    N = [j for j in range(6) if j != v]
    if any(A[v][j] != 2 for j in N):
        raise WitnessFail("N26_STAR", "v=%d" % v)
    if any(A[j][k] not in (2, 4) for (j, k) in itertools.combinations(N, 2)):
        raise WitnessFail("N26_NEIGHBOUR_ALPHA", "v=%d" % v)
    if st.is_e3(v):
        for (j, k, l) in itertools.combinations(N, 3):
            tmin, tmax = tau_min_max(A, st, j, k, l)
            if not tmax < 3 * tmin:
                raise WitnessFail("N26_E3_TEST", "triple %d,%d,%d" % (j, k, l))
    return {"v": v}


# ---------------------------------------------------------------------------
# FH5 (rules-k6-v1 L5, L6, L8; rules-k6-v2 L9(a); erratum C4, C6, C15, C16;
# CERT-FORMAT 3 "FH5", 6.3).  Sun(6) in H is used only for |T| = 6 and only
# inside a least-order counterexample (H = U_a U_b has index 5, so H < G).
# ---------------------------------------------------------------------------
def fh5_exponents(st, l, t, e5):
    """(v2, v3, v5) exponents used for lambda_l = r_l t_l (saturated, C5/C16)."""
    b2 = 0
    if st.is_e2(l):
        b2 = 1 if st.c2 == 1 else SAT
    b3 = SAT if st.is_e3(l) else 0
    b5 = SAT if (e5 is not None and l == e5) else 0
    return (v_p(t, 2) + b2, v_p(t, 3) + b3, v_p(t, 5) + b5)


def fgcd_value(ex, ey):
    return 2 ** min(ex[0], ey[0]) * 3 ** min(ex[1], ey[1]) * 5 ** min(ex[2], ey[2])


def fgcd_table(st, e5):
    ex = {(l, t): fh5_exponents(st, l, t, e5) for l in range(6) for t in range(1, 6)}
    fg = {}
    for (l, t) in ex:
        for (l2, t2) in ex:
            if l != l2:
                fg[(l, t, l2, t2)] = fgcd_value(ex[(l, t)], ex[(l2, t2)])
    return fg


def fh5_domains(A, a, b, V):
    """Coset-set choices (mask over cosets 0..4, t) per vertex; only a is fixed (C6)."""
    dom = {a: ((1, 1),)}
    dom[b] = tuple((1 << c, 1) for c in COSETS)
    for v in V:
        c = A[v][a]
        if c == 1:
            dom[v] = tuple((1 << x, 1) for x in COSETS)
        else:
            dom[v] = tuple((sum(1 << x for x in comb), c)
                           for comb in itertools.combinations(COSETS, c))
    for l in range(6):
        if l not in dom:
            dom[l] = tuple((m, bin(m).count("1")) for m in range(1, 32))
    return dom


def fh5_search(A, a, b, V, fg, guard):
    """Exhaustive search with safe monotone pruning; returns accounting and any survivor."""
    free = [l for l in range(6) if l != a and l != b and l not in V]
    order = [a, b] + sorted(V) + sorted(free)
    dom = fh5_domains(A, a, b, V)
    sizes = [len(dom[l]) for l in order]
    suffix = [1] * 7
    for d in range(5, -1, -1):
        suffix[d] = suffix[d + 1] * sizes[d]
    t_of = [0] * 6
    mask_of = [0] * 6
    members = [[] for _ in COSETS]
    acct = {"nodes": 0, "pruned_weight": 0, "complete": 0}
    found = []

    def rejected(l):
        t = t_of[l]
        m = mask_of[l]
        for i in range(6):
            if i == l:
                continue
            ti = t_of[i]
            if ti == 0:
                continue
            if t == 1 and A[l][i] > ti:        # (F3): U_l inside H
                return True
            if ti == 1 and A[i][l] > t:        # (F3): U_i inside H
                return True
        for c in COSETS:
            if not (m >> c) & 1:
                continue
            M = members[c]
            for size in range(1, len(M) + 1):
                k = size + 1
                for R in itertools.combinations(M, size):
                    T = R + (l,)
                    if not any(fg[(x, t_of[x], y, t_of[y])] >= k
                               for (x, y) in itertools.combinations(T, 2)):
                        return True            # (F2) hereditary Sun(|T|) fails in coset c
        return False

    def rec(d):
        if d == 6:
            acct["complete"] += 1
            found.append([[l, list(mask_members(mask_of[l])), t_of[l]] for l in range(6)])
            return True
        l = order[d]
        for (m, t) in dom[l]:
            acct["nodes"] += 1
            if acct["nodes"] % GUARD_STRIDE == 0:
                guard.check()
            t_of[l] = t
            mask_of[l] = m
            if rejected(l):
                acct["pruned_weight"] += suffix[d + 1]
                t_of[l] = 0
                mask_of[l] = 0
                continue
            for c in COSETS:
                if (m >> c) & 1:
                    members[c].append(l)
            hit = rec(d + 1)
            for c in COSETS:
                if (m >> c) & 1:
                    members[c].pop()
            t_of[l] = 0
            mask_of[l] = 0
            if hit:
                return True
        return False

    rec(0)
    return {"domain": suffix[0], "nodes": acct["nodes"], "pruned_weight": acct["pruned_weight"],
            "complete": acct["complete"], "survivor": (found[0] if found else None)}


def verify_FH5(A, st, w, ctx, tp):
    if type(w) is not list or len(w) != 3:
        raise WitnessFail("FH5_SHAPE", "witness")
    ab, Vw, counts = w
    if type(ab) is not list or len(ab) != 2 or not all(is_vertex(x) for x in ab):
        raise WitnessFail("FH5_SHAPE", "[a,b]")
    a, b = ab
    if a == b:
        raise WitnessFail("FH5_SHAPE", "a == b")
    if type(Vw) is not list or any(not is_vertex(x) for x in Vw) or len(set(Vw)) != len(Vw):
        raise WitnessFail("FH5_SHAPE", "V")
    if type(counts) is not list or len(counts) != 7 or \
            any(type(c) is not int or c < 0 for c in counts):
        raise WitnessFail("FH5_SHAPE", "counts")
    if A[a][b] != 1:
        raise WitnessFail("FH5_AB_NOT_ONE", "alpha_ab=%d" % A[a][b])
    V = sorted(v for v in range(6) if v != a and v != b and A[v][a] == A[v][b])
    if set(Vw) != set(V):
        raise WitnessFail("FH5_V_MISMATCH", "witness %s recomputed %s" % (sorted(Vw), V))
    if not V:
        raise WitnessFail("FH5_V_EMPTY", "")
    per = []
    for e5 in E5_PLACEMENTS:
        fk = (tp, e5)
        fg = ctx.fg_cache.get(fk)
        if fg is None:
            fg = fgcd_table(st, e5)
            ctx.fg_cache[fk] = fg
        res = fh5_search(A, a, b, V, fg, ctx.guard)
        ctx.stats["fh5_placements"] += 1
        ctx.stats["fh5_nodes"] += res["nodes"]
        ctx.stats["fh5_domain_total"] += res["domain"]
        if res["survivor"] is not None:
            raise WitnessFail("FH5_SURVIVING_ASSIGNMENT",
                              "e5=%s assignment=%s" % (e5, res["survivor"]))
        if res["complete"] != 0 or res["pruned_weight"] != res["domain"]:
            raise WitnessFail("FH5_ACCOUNTING", "e5=%s %s/%s" % (e5, res["pruned_weight"],
                                                                 res["domain"]))
        ctx.stats["fh5_pruned_weight"] += res["pruned_weight"]
        per.append([("None" if e5 is None else e5), res["domain"], res["nodes"]])
    return {"ab": [a, b], "V": V, "placements": per}


# ---------------------------------------------------------------------------
# RPLP (rules-k6-v3 L12; proof-k6-lemmas-v1 4; CERT-FORMAT 3 "RPLP", 6.4, 6.5).
# ---------------------------------------------------------------------------
def rplp_frame(A, st, v):
    """Forced ordered pairs (positions), admissible A-masks, and ylo/yhi per pair."""
    N, st5 = neighbours(st, v)
    forced = []
    for x in range(5):
        for y in range(5):
            if x == y:
                continue
            wv, jv = N[x], N[y]
            tmin, _tmax = tau_min_max(A, st, v, wv, jv)
            if tmin >= A[v][wv] * A[wv][jv]:      # product taken at w (ordered)
                forced.append((x, y))
    amasks = [am for am in range(1, 32)
              if not any(((am >> y) & 1) and not ((am >> x) & 1) for (x, y) in forced)]
    ylo = []
    yhi = []
    for (x, y) in FIVE_PAIRS:
        lo, hi, _u = p_bounds(A, st, v, N[x], N[y])
        base = 1 - Fraction(A[v][N[x]] + A[v][N[y]], 5)
        ylo.append(base + lo)
        yhi.append(base + hi)
    return N, st5, forced, amasks, ylo, yhi


def verify_RPLP(A, st, w, ctx):
    if type(w) is not list or len(w) != 2 or not is_vertex(w[0]) or type(w[1]) is not list:
        raise WitnessFail("RPLP_SHAPE", "witness")
    v, certs = w
    N, st5, forced, amasks, ylo, yhi = rplp_frame(A, st, v)
    qs = q_vectors(A, v, N)
    if len(certs) != len(qs):
        raise WitnessFail("RPLP_CERT_COUNT", "%d != %d" % (len(certs), len(qs)))
    pairs_in = {am: tuple(pi for pi, (x, y) in enumerate(FIVE_PAIRS)
                          if (am >> x) & 1 and (am >> y) & 1) for am in amasks}
    nR = 0
    nP = 0
    for idx, q in enumerate(qs):
        e = certs[idx]
        if type(e) is not list or len(e) != 2 or type(e[0]) is not str:
            raise WitnessFail("RPLP_ENTRY_SHAPE", "entry %d" % idx)
        if e[0] == "R":
            if type(e[1]) is not str or e[1] != dual_key(q, st5):
                raise WitnessFail("RPLP_R_KEY_MISMATCH", "entry %d q=%s" % (idx, list(q)))
            check_q_dual(q, st5, ctx, "RPLP_R")
            ctx.stats["rplp_R_refs"] += 1
            nR += 1
        elif e[0] == "P":
            vec = e[1]
            if type(vec) is not list or len(vec) != 30:
                raise WitnessFail("RPLP_ENTRY_SHAPE", "entry %d vector" % idx)
            vals = [parse_rational(s) for s in vec]
            if any(r is None for r in vals):
                raise WitnessFail("RPLP_BAD_RATIONAL", "entry %d" % idx)
            av, bv, uv, lv = vals[0:5], vals[5:10], vals[10:20], vals[20:30]
            if any(r < 0 for r in uv) or any(r < 0 for r in lv):
                raise WitnessFail("RPLP_P_NEGATIVE", "entry %d" % idx)
            allowed = set(allowed_masks(q, st5, ctx))
            allowed.add(0)
            for am in amasks:
                base = sum((bv[x] for x in mask_members(am)), Fraction(0))
                base -= sum((uv[pi] - lv[pi] for pi in pairs_in[am]), Fraction(0))
                sm = am
                while True:
                    if sm in allowed:
                        ctx.stats["rplp_columns_checked"] += 1
                        coef = base + sum((av[x] for x in mask_members(sm)), Fraction(0))
                        if coef > 1:
                            raise WitnessFail("RPLP_P_COLUMN", "entry %d A=%s S=%s" % (
                                idx, [N[x] for x in mask_members(am)],
                                [N[x] for x in mask_members(sm)]))
                    if sm == 0:
                        break
                    sm = (sm - 1) & am
            obj = sum((av[x] * Fraction(q[x], 5) for x in range(5)), Fraction(0))
            obj += sum((bv[x] * Fraction(5 - A[v][N[x]], 5) for x in range(5)), Fraction(0))
            obj -= sum((uv[pi] * yhi[pi] for pi in range(10)), Fraction(0))
            obj += sum((lv[pi] * ylo[pi] for pi in range(10)), Fraction(0))
            if obj < 1:
                raise WitnessFail("RPLP_P_OBJECTIVE", "entry %d value=%s" % (idx, obj))
            ctx.stats["rplp_P_vectors"] += 1
            nP += 1
        else:
            raise WitnessFail("RPLP_ENTRY_SHAPE", "entry %d tag" % idx)
    return {"v": v, "q": len(qs), "R": nR, "P": nP}


# ---------------------------------------------------------------------------
# One certificate line.
# ---------------------------------------------------------------------------
def verify_record(tp, rep, rule, witness, ctx):
    """Verify one (type, rep, rule, witness); returns info or raises WitnessFail/StopRequested."""
    if tp not in TYPES:
        raise WitnessFail("BAD_TYPE", str(tp))
    if type(rep) is not str or CODE_RE.fullmatch(rep) is None:
        raise WitnessFail("BAD_REP", str(rep)[:40])
    st = Status(tp)
    A = matrix_from_code(rep)
    if not t_consistent(A, st):
        raise WitnessFail("REP_NOT_T_CONSISTENT", rep)
    if rule == "K":
        return verify_K(A, st, witness)
    if rule == "RLP":
        return verify_RLP(A, st, witness, ctx)
    if rule == "PB":
        return verify_PB(A, st, witness)
    if rule == "Ppair":
        return verify_Ppair(A, st, witness)
    if rule == "FH5":
        return verify_FH5(A, st, witness, ctx, tp)
    if rule == "N26":
        return verify_N26(A, st, witness)
    if rule == "RPLP":
        return verify_RPLP(A, st, witness, ctx)
    if rule == "SURVIVE":
        raise WitnessFail("SURVIVE_LINE", rep)
    raise WitnessFail("BAD_RULE", str(rule)[:20])


# ---------------------------------------------------------------------------
# Input parsing (CERT-FORMAT 6.2; overlay item 1: `code` opaque).
# ---------------------------------------------------------------------------
LINE_KEYS = frozenset(("type", "code", "rep", "rule", "witness"))
LINE_KEYS_SURVIVE = frozenset(("type", "code", "rep", "rule"))
RUN_TOP_KEYS = frozenset(("engine", "sha256", "imports_v2_sha256", "python", "platform", "summary",
                          "total_orbits", "total_survivors", "orbits_jsonl_sha256_uncompressed",
                          "rlp_dual_entries", "seconds"))
RUN_TYPE_KEYS = frozenset(("leaves_labelled", "pruned_nodes", "orbits", "leafcodes_sha256",
                           "orbit_rule_counts", "seconds"))


def parse_type_field(x, n):
    if type(x) is not list or len(x) != 3:
        raise InputRejected("BAD_TYPE_FIELD", "line %d" % n)
    e2, c2, e3 = x
    if not (e2 is None or type(e2) is int) or type(c2) is not int or \
            not (e3 is None or type(e3) is int):
        raise InputRejected("BAD_TYPE_FIELD", "line %d" % n)
    tp = (e2, c2, e3)
    if tp not in TYPES:
        raise InputRejected("BAD_TYPE_FIELD", "line %d %s" % (n, str(tp)))
    return tp


def parse_orbit_lines(plain):
    if type(plain) is not bytes or not plain.isascii():
        raise InputRejected("NOT_ASCII", "orbits.jsonl")
    if b"\r" in plain:
        raise InputRejected("CR_PRESENT", "orbits.jsonl")
    if not plain.endswith(b"\n"):
        raise InputRejected("TRUNCATED_STREAM", "missing final newline")
    body = plain[:-1]
    if not body:
        raise InputRejected("EMPTY_STREAM", "orbits.jsonl")
    records = []
    for n, raw in enumerate(body.split(b"\n"), start=1):
        if not raw:
            raise InputRejected("EMPTY_LINE", "line %d" % n)
        obj = strict_json(raw, what="line %d" % n)
        if type(obj) is not dict:
            raise InputRejected("LINE_NOT_OBJECT", "line %d" % n)
        rule = obj.get("rule")
        if type(rule) is not str or rule not in RULE_NAMES:
            raise InputRejected("BAD_RULE", "line %d" % n)
        expect = LINE_KEYS_SURVIVE if rule == "SURVIVE" else LINE_KEYS
        if frozenset(obj) != expect:
            raise InputRejected("FIELDS", "line %d: %s" % (n, sorted(set(obj) ^ set(expect))))
        tp = parse_type_field(obj["type"], n)
        code = obj["code"]
        if type(code) is not str or CODE_RE.fullmatch(code) is None:
            raise InputRejected("BAD_CODE", "line %d" % n)
        rep = obj["rep"]
        if type(rep) is not str or CODE_RE.fullmatch(rep) is None:
            raise InputRejected("BAD_REP", "line %d" % n)
        records.append((n, tp, rep, rule, obj.get("witness")))
    return records


def parse_duals(raw):
    obj = strict_json(raw, what="rlp_duals.json")
    if type(obj) is not dict:
        raise InputRejected("BAD_DUALS", "top level")
    duals = {}
    for key, val in obj.items():
        if KEY_RE.fullmatch(key) is None:
            raise InputRejected("BAD_DUALS", "key %s" % key[:60])
        if type(val) is not dict or frozenset(val) != frozenset(("value", "y")):
            raise InputRejected("BAD_DUALS", "fields of %s" % key)
        y = val["y"]
        if type(y) is not list or len(y) != 5:
            raise InputRejected("BAD_DUALS", "y shape of %s" % key)
        ys = tuple(parse_rational(s) for s in y)
        if any(r is None for r in ys) or parse_rational(val["value"]) is None:
            raise InputRejected("BAD_DUALS", "rational in %s" % key)
        duals[key] = ys
    return duals


def _is_seconds(x):
    return type(x) is FloatToken or (type(x) is int and x >= 0)


def _nonneg_int(x):
    return type(x) is int and x >= 0


def parse_runjson(raw):
    obj = strict_json(raw, allow_float=True, what="run.json")
    if type(obj) is not dict or frozenset(obj) != RUN_TOP_KEYS:
        raise InputRejected("BAD_RUNJSON", "top-level fields")
    for k in ("engine", "sha256", "imports_v2_sha256", "python", "platform"):
        if type(obj[k]) is not str:
            raise InputRejected("BAD_RUNJSON", k)
    for k in ("total_orbits", "total_survivors", "rlp_dual_entries"):
        if not _nonneg_int(obj[k]):
            raise InputRejected("BAD_RUNJSON", k)
    osha = obj["orbits_jsonl_sha256_uncompressed"]
    if type(osha) is not str or HEX64_RE.fullmatch(osha) is None:
        raise InputRejected("BAD_RUNJSON", "orbits_jsonl_sha256_uncompressed")
    if not _is_seconds(obj["seconds"]):
        raise InputRejected("BAD_RUNJSON", "seconds")
    summ = obj["summary"]
    if type(summ) is not dict or frozenset(summ) != frozenset(type_key(tp) for tp in TYPES):
        raise InputRejected("BAD_RUNJSON", "summary keys")
    per = {}
    for tp in TYPES:
        s = summ[type_key(tp)]
        if type(s) is not dict or frozenset(s) != RUN_TYPE_KEYS:
            raise InputRejected("BAD_RUNJSON", "summary fields %s" % type_key(tp))
        for k in ("leaves_labelled", "pruned_nodes", "orbits"):
            if not _nonneg_int(s[k]):
                raise InputRejected("BAD_RUNJSON", "%s %s" % (type_key(tp), k))
        if type(s["leafcodes_sha256"]) is not str or HEX64_RE.fullmatch(s["leafcodes_sha256"]) is None:
            raise InputRejected("BAD_RUNJSON", "%s leafcodes_sha256" % type_key(tp))
        if not _is_seconds(s["seconds"]):
            raise InputRejected("BAD_RUNJSON", "%s seconds" % type_key(tp))
        rc = s["orbit_rule_counts"]
        if type(rc) is not dict or any(k not in RULE_NAMES or not _nonneg_int(c) for k, c in rc.items()):
            raise InputRejected("BAD_RUNJSON", "%s orbit_rule_counts" % type_key(tp))
        per[tp] = {"leaves": s["leaves_labelled"], "orbits": s["orbits"],
                   "sha": s["leafcodes_sha256"], "rule_counts": dict(rc)}
    glob = {"total_orbits": obj["total_orbits"], "total_survivors": obj["total_survivors"],
            "orbits_sha": osha, "rlp_dual_entries": obj["rlp_dual_entries"]}
    return glob, per


def parse_survivors(raw):
    obj = strict_json(raw, what="survivors.json")
    if type(obj) is not list:
        raise InputRejected("BAD_SURVIVORS", "not a list")
    return obj


# ---------------------------------------------------------------------------
# Pipeline.
# ---------------------------------------------------------------------------
def run_check(blobs, guard, pins=None, plain_pin=None):
    """Complete fail-closed replay. Returns the report dict (with gate and verdict)."""
    pins = INPUT_PINS if pins is None else pins
    plain_pin = ORBITS_PLAIN_PIN if plain_pin is None else plain_pin
    R = {"checker": CHECKER_ID,
         "inputs": {"ok": False, "files": {}, "reject": None},
         "parse": {"ok": False, "reject": None},
         "placements": None,
         "runjson_global": None,
         "universe": {"complete": False, "types": {}},
         "witnesses": None,
         "rules": None}
    # Stage 1: byte pins.
    try:
        for name in INPUT_NAMES:
            b = blobs.get(name)
            if type(b) is not bytes:
                raise InputRejected("INPUT_MISSING", name)
            size, sha = pins[name]
            h = sha256_hex(b)
            R["inputs"]["files"][name] = {"bytes": len(b), "sha256": h}
            if len(b) != size:
                raise InputRejected("PIN_SIZE_MISMATCH", name)
            if h != sha:
                raise InputRejected("PIN_SHA_MISMATCH", name)
        try:
            plain = gzip.decompress(blobs["orbits.jsonl.gz"])
        except (OSError, EOFError, ValueError, zlib.error) as exc:
            raise InputRejected("DECOMPRESS_ERROR", str(exc)[:200])
        ph = sha256_hex(plain)
        R["inputs"]["orbits_plain"] = {"bytes": len(plain), "sha256": ph}
        if len(plain) != plain_pin[0] or ph != plain_pin[1]:
            raise InputRejected("PLAIN_PIN_MISMATCH", "orbits.jsonl")
        R["inputs"]["ok"] = True
    except InputRejected as exc:
        R["inputs"]["reject"] = {"reason": exc.reason, "detail": exc.detail}
        return finish(R, guard)
    # Stage 2: strict parse.
    try:
        records = parse_orbit_lines(plain)
        duals = parse_duals(blobs["rlp_duals.json"])
        rj_glob, rj_types = parse_runjson(blobs["run.json"])
        survivors = parse_survivors(blobs["survivors.json"])
    except InputRejected as exc:
        R["parse"]["reject"] = {"reason": exc.reason, "detail": exc.detail}
        return finish(R, guard)
    rule_counts = {}
    for rec in records:
        rule_counts[rec[3]] = rule_counts.get(rec[3], 0) + 1
    R["parse"] = {"ok": True, "reject": None, "lines": len(records), "dual_entries": len(duals),
                  "survivors": len(survivors), "rules": rule_counts}
    R["runjson_global"] = {
        "total_orbits": rj_glob["total_orbits"] == len(records),
        "total_survivors": rj_glob["total_survivors"] == len(survivors)
        and rj_glob["total_survivors"] == rule_counts.get("SURVIVE", 0),
        "orbits_sha": rj_glob["orbits_sha"] == ph,
        "rlp_dual_entries": rj_glob["rlp_dual_entries"] == len(duals)}
    stop = None
    # Stage 3: marker placements.
    try:
        guard.check()
        R["placements"] = placement_reduction()
    except StopRequested as exc:
        stop = exc.reason
    # Stage 4: universe and exact orbit coverage.
    by_type = {tp: [] for tp in TYPES}
    for rec in records:
        by_type[rec[1]].append(rec)
    if stop is None:
        try:
            for tp in TYPES:
                guard.check()
                st = Status(tp)
                perms = stabilizer(tp)
                getters = lex_image_getters(perms)
                leaves, nodes = enumerate_leaves(st, guard)
                items = [(rec[0], lexkey_from_code(rec[2])) for rec in by_type[tp]]
                cov = check_coverage(items, leaves, getters, guard)
                cov["rep_not_leaf"] = cov["rep_not_leaf"][:50]
                cov["image_not_leaf"] = cov["image_not_leaf"][:50]
                cov["duplicate"] = cov["duplicate"][:50]
                leafsha = sha256_hex(("\n".join(sorted(code_from_lexkey(k) for k in leaves))
                                      + "\n").encode("ascii"))
                rc = {}
                for rec in by_type[tp]:
                    rc[rec[3]] = rc.get(rec[3], 0) + 1
                exp = rj_types[tp]
                R["universe"]["types"][type_key(tp)] = {
                    "stabilizer_size": len(perms),
                    "stabilizer_expected": expected_stabilizer_size(tp),
                    "enumeration_nodes": nodes,
                    "leaves": len(leaves),
                    "lines": len(items),
                    "leafcodes_sha256": leafsha,
                    "coverage": cov,
                    "runjson": {"leaves_labelled": exp["leaves"] == len(leaves),
                                "orbits": exp["orbits"] == len(items)
                                and cov["orbits_owned"] == len(items),
                                "orbit_rule_counts": exp["rule_counts"] == rc,
                                "leafcodes_sha256": exp["sha"] == leafsha}}
                del leaves
            R["universe"]["complete"] = True
        except StopRequested as exc:
            stop = exc.reason
    # Stage 5: every witness line.
    ctx = RuleContext(duals, guard)
    W = {"total": len(records), "verified": 0, "failed": 0, "incomplete": 0, "by_rule": {},
         "failures": [], "first_incomplete_line": None}
    for rec in records:
        n, tp, rep, rule, wit = rec
        br = W["by_rule"].setdefault(rule, {"verified": 0, "failed": 0, "incomplete": 0})
        if stop is None:
            try:
                guard.check()
            except StopRequested as exc:
                stop = exc.reason
        if stop is not None:
            W["incomplete"] += 1
            br["incomplete"] += 1
            if W["first_incomplete_line"] is None:
                W["first_incomplete_line"] = n
            continue
        try:
            verify_record(tp, rep, rule, wit, ctx)
            W["verified"] += 1
            br["verified"] += 1
        except WitnessFail as exc:
            W["failed"] += 1
            br["failed"] += 1
            if len(W["failures"]) < FAIL_DETAIL_CAP:
                W["failures"].append([n, type_key(tp), rep, rule, exc.reason, exc.detail])
        except StopRequested as exc:
            stop = exc.reason
            W["incomplete"] += 1
            br["incomplete"] += 1
            if W["first_incomplete_line"] is None:
                W["first_incomplete_line"] = n
        except Exception as exc:          # defect in this checker: fail closed, never PASS
            W["failed"] += 1
            br["failed"] += 1
            if len(W["failures"]) < FAIL_DETAIL_CAP:
                W["failures"].append([n, type_key(tp), rep, rule, "INTERNAL_ERROR", repr(exc)[:200]])
    R["witnesses"] = W
    stats = dict(ctx.stats)
    stats["rlp_used_keys"] = len(ctx.used_keys)
    stats["rlp_unused_keys"] = len(set(duals) - ctx.used_keys)
    stats["dual_cache_entries"] = len(ctx.dual_cache)
    R["rules"] = stats
    R["stop"] = stop
    return finish(R, guard)


def compute_gate(R, guard):
    g = {}
    g["inputs_ok"] = R["inputs"].get("ok") is True
    P = R.get("parse") or {}
    g["parse_ok"] = P.get("ok") is True
    pl = R.get("placements")
    g["placements_ok"] = bool(pl) and pl.get("ok") is True
    rg = R.get("runjson_global")
    g["runjson_global_ok"] = bool(rg) and all(v is True for v in rg.values())
    U = R.get("universe") or {}
    T = U.get("types") or {}
    g["universe_complete"] = U.get("complete") is True and len(T) == 8 and \
        set(T) == set(type_key(tp) for tp in TYPES)
    g["coverage_clean_all"] = g["universe_complete"] and all(t["coverage"]["clean"] is True
                                                             for t in T.values())
    g["stabilizers_ok"] = g["universe_complete"] and all(
        t["stabilizer_size"] == t["stabilizer_expected"] for t in T.values())
    g["runjson_types_ok"] = g["universe_complete"] and all(
        all(v is True for v in t["runjson"].values()) for t in T.values())
    W = R.get("witnesses") or {}
    total = W.get("total", -1)
    g["lines_accounted"] = type(total) is int and total >= 0 and \
        W.get("verified", 0) + W.get("failed", 0) + W.get("incomplete", 0) == total
    g["all_verified"] = g["parse_ok"] and total == P.get("lines", -2) and total > 0 and \
        W.get("verified") == total
    g["failed_zero"] = W.get("failed", 1) == 0
    g["incomplete_zero"] = W.get("incomplete", 1) == 0
    g["survivors_empty"] = P.get("survivors", 1) == 0
    g["no_survive_lines"] = g["parse_ok"] and (P.get("rules") or {}).get("SURVIVE", 0) == 0
    g["no_stop"] = R.get("stop") is None
    g["guard_clear"] = guard.state() is None
    return g


def detected_failure(R, g):
    if not g["inputs_ok"] or not g["parse_ok"]:
        return True
    if R.get("placements") is not None and not g["placements_ok"]:
        return True
    if R.get("runjson_global") is not None and not g["runjson_global_ok"]:
        return True
    for t in (R.get("universe") or {}).get("types", {}).values():
        if t["coverage"]["clean"] is not True or t["stabilizer_size"] != t["stabilizer_expected"] \
                or not all(v is True for v in t["runjson"].values()):
            return True
    W = R.get("witnesses") or {}
    if W.get("failed", 0) != 0:
        return True
    P = R.get("parse") or {}
    if P.get("survivors", 0) != 0 or (P.get("rules") or {}).get("SURVIVE", 0) != 0:
        return True
    return False


def finish(R, guard):
    g = compute_gate(R, guard)
    R["gate"] = g
    R["guard"] = {"triggered": guard.triggered, "checks": guard.checks,
                  "deadline_ns": guard.deadline_ns}
    if detected_failure(R, g):
        R["verdict"] = "FAIL"
        R["exit_code"] = EXIT_INPUT_REJECTED if not (g["inputs_ok"] and g["parse_ok"]) else EXIT_FAIL
    elif all(v is True for v in g.values()):
        R["verdict"] = "PASS"
        R["exit_code"] = EXIT_PASS
    else:
        R["verdict"] = "INCOMPLETE"
        R["exit_code"] = EXIT_INCOMPLETE
    return R


# ---------------------------------------------------------------------------
# Publication: exclusive report, read-back, guard re-check, exclusive seal.
# ---------------------------------------------------------------------------
def write_exclusive(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        view = memoryview(data)
        while len(view):
            n = os.write(fd, view)
            view = view[n:]
        os.fsync(fd)
    finally:
        os.close(fd)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise OSError("read-back mismatch: %s" % path)


def publish(R, out_dir, guard):
    """Returns the process exit code. PASS only with a verified seal and a clear guard."""
    verdict = R.get("verdict")
    code = R.get("exit_code")
    if verdict not in ("PASS", "FAIL", "INCOMPLETE") or type(code) is not int:
        return EXIT_INTERNAL
    if verdict == "PASS" and guard.state() is not None:
        # Stop arrived after the gate but before publication: downgrade, never publish PASS.
        R["verdict"] = verdict = "INCOMPLETE"
        R["exit_code"] = code = EXIT_INCOMPLETE
        R["stop_before_publication"] = guard.triggered
    R["pass_requires_verified_seal"] = True
    body = (json.dumps(R, sort_keys=True, indent=1, ensure_ascii=True) + "\n").encode("ascii")
    try:
        write_exclusive(os.path.join(out_dir, "REPORT.json"), body)
    except OSError as exc:
        sys.stderr.write("%s: report publication failed: %s\n" % (CHECKER_ID, exc))
        return EXIT_PUBLICATION
    if verdict == "PASS" and guard.state() is not None:
        sys.stderr.write("%s: stop (%s) before seal; PASS not sealed\n" % (CHECKER_ID,
                                                                         guard.triggered))
        return EXIT_INCOMPLETE
    seal = {"checker": CHECKER_ID, "report_sha256": sha256_hex(body), "report_bytes": len(body),
            "verdict": verdict, "exit_code": code, "sealed_at_ns": time.time_ns()}
    seal_body = (json.dumps(seal, sort_keys=True, indent=1) + "\n").encode("ascii")
    try:
        write_exclusive(os.path.join(out_dir, "REPORT.seal.json"), seal_body)
    except OSError as exc:
        sys.stderr.write("%s: seal publication failed: %s\n" % (CHECKER_ID, exc))
        return EXIT_PUBLICATION
    return code


def read_inputs(input_dir, pins=None):
    pins = INPUT_PINS if pins is None else pins
    blobs = {}
    for name in INPUT_NAMES:
        try:
            with open(os.path.join(input_dir, name), "rb") as f:
                blobs[name] = f.read(pins[name][0] + 1)
        except OSError:
            blobs[name] = None
    return blobs


def main(argv=None):
    ap = argparse.ArgumentParser(prog=CHECKER_ID,
                                 description="Second independent Sun(6) Core5(6) certificate checker")
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--out-dir", required=True, help="must not exist; created exclusively")
    ap.add_argument("--deadline-epoch", required=True, type=int,
                    help="absolute wall-clock deadline, integer UNIX seconds")
    ap.add_argument("--cancel-file", default=None)
    args = ap.parse_args(argv)
    guard = Guard(args.deadline_epoch * 1000000000, args.cancel_file)

    def on_signal(signum, _frame):
        guard.request_cancel("signal-%d" % signum)

    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    started_ns = time.time_ns()
    mono0 = time.monotonic_ns()
    try:
        os.mkdir(args.out_dir)
    except OSError as exc:
        sys.stderr.write("%s: out-dir not created exclusively: %s\n" % (CHECKER_ID, exc))
        return EXIT_PUBLICATION
    try:
        with open(os.path.abspath(__file__), "rb") as f:
            source_sha = sha256_hex(f.read())
        blobs = read_inputs(args.input_dir)
        R = run_check(blobs, guard)
        R["run"] = {"source_sha256": source_sha, "python": sys.version, "platform": sys.platform,
                    "pid": os.getpid(), "pgid": os.getpgrp(), "cwd": os.getcwd(),
                    "argv": list(sys.argv), "started_ns": started_ns, "ended_ns": time.time_ns(),
                    "monotonic_elapsed_ns": time.monotonic_ns() - mono0}
    except Exception as exc:              # never PASS on an internal error
        sys.stderr.write("%s: internal error: %r\n" % (CHECKER_ID, exc))
        return EXIT_INTERNAL
    return publish(R, args.out_dir, guard)


if __name__ == "__main__":
    sys.exit(main())
