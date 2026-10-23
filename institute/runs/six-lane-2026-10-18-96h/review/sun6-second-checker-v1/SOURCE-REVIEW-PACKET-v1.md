# Sun6 second independent checker v1: full-body source review packet

- Clock (/bin/date immediately before writing): 2026-10-19T17:37:42-0700
- Directory (snapshot root): `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun6-second-checker-v1`
- Status: SOURCE ONLY, NOT RUN. No execution, compilation, test or lint of anything in this directory; ast.parse only. No verification, novelty or theorem claim. The author does not accept its own work: parent source review + item GO + fresh stability gate + five-part release are required before any execution.
- Authority: source scope 6cc055bcd254dc4405b2876f67ae6d494534b844605dccb0f6c924662c49659a; fullgate ruling 4818f1ca96c99e012d758e165982ec0844228eae07ff3f38b95dc2b7a3a5eada; entry verdict efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29.

## 1. Independence statement

Written from the nine named Sun6 mathematical sources and the pinned untrusted DATA only (READLOG-v1.json lists every read with sha256). Not read: lane engine/checker code, the earlier independent checker and its diff, the parent derivation, parent auxiliary implementations, old controls, replay reports/receipts, review notes, Sun5 material. No import, copy or re-export of any project code; standard library only.

## 2. Files (sha256 at packet time; SHA256SUMS-v1.txt is authoritative)

| File | Bytes | SHA256 |
|---|---:|---|
| `CONTROLS-PLAN-v1.json` | 53057 | `42cd627528121b3a26ce886514b4cc24b0ec33ac83ee8f75fe11768b4563b01b` |
| `INPUT-PINS-v1.json` | 4864 | `aba3c1ea0c576cfda974d4520e8f6c32ff16d9e30cef3fcb924b6fbe7bc2a18e` |
| `MATH-BRIDGE-v1.md` | 15827 | `398eaa5631aa1783ba8c57ea82db7d0fa10ef3653a861d3806dbaf8885af9526` |
| `READLOG-v1.json` | 7752 | `761f4f0d1e03f4aa5201ab2b5d004c4ef76e15953292633cc8bf60ca96127854` |
| `RESOURCE-LIFECYCLE-PLAN-v1.json` | 6179 | `f5d1c13715bfb084b2093a78fb6ebc8edbd1128cfa2f392689102c66f00f1fec` |
| `SCOPE-DESIGN-v1.md` | 12759 | `8ae497b2b57a6a473799012f7d10bd6c4195faef463cb163dd3f07234ed46a40` |
| `checkpoints/checkpoint-001.md` | 1845 | `d0ab1574128ada05e28887539c2dcf8f9fe68d694811ab3135e82702c6c474bd` |
| `checkpoints/checkpoint-002.md` | 1298 | `abb2e8278aa077532c5ca481657f25f0581277567de0820f2d6f69dbf5792c0e` |
| `checkpoints/checkpoint-003.md` | 1778 | `1a6e33b0b868e66a4b413a0dd5a9729975606090740ec1efafc07d20241aae4f` |
| `code/sun6_second_checker_controls_v1.py` | 16801 | `ef47979132296fd5a4bfc45fe2c1d130e1b2fefd5d033b72404c71af2a0869d3` |
| `code/sun6_second_checker_v1.py` | 56971 | `1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f` |

## 3. What reviewers should attack (suggested)

1. Every predicate in sections 3-8 of MATH-BRIDGE-v1.md against rules-k6-v1/v2/v3, proof-k6-lemmas-v1, erratum-v3 (C1-C22) and CERT-FORMAT-k6-v3 sections 3 and 6 (K, RLP, Ppair/PB with C13 rounding and K2 decrement, FH5 domains/rejections/7 placements, N26 with C11/C14, RPLP ordered forced pairs, columns, objective).
2. Universe completeness: `enumeration_schedule`/`enumerate_leaves` test each of the 20 triangles exactly once and prune only at completed triangles; `lex_image_getters` implements (p.A)[p(i)][p(j)] = A[i][j]; `check_coverage` decides exact set equality with disjoint orbits.
3. Exactness for arbitrary cofactors: `gcd_alpha_r`, `allowed_masks` (maxgcd), `fh5_exponents`/`fgcd_value` with SAT = 64 (sections 2, 5, 7 of the bridge).
4. FH5 search soundness: monotonicity of both rejection conditions, incremental hereditary test (subsets containing the new vertex), exact accounting identity, no fixed vertex other than a.
5. Strict parsing and accounting: duplicate keys, floats, NaN, bools-as-ints, unknown/missing fields, truncation, empty lines, run.json float paths, dual key regex, rational regex.
6. Fail-closed lifecycle: latched Guard, StopRequested propagation, INCOMPLETE vs FAIL classification (`detected_failure` before the all-true conjunction), PASS downgrade before publication, O_EXCL report + seal, exit codes.
7. Controls (CONTROLS-PLAN-v1.json, 124 entries): whether each expectation is right, intended-reason (not incidental), and whether important defect classes are missing.
8. Resource plan realism (RESOURCE-LIFECYCLE-PLAN-v1.json); all figures are author estimates.

## 4. Known deliberate choices (not defects unless a reviewer shows otherwise)

- Format clauses enforced even where mathematics would allow slack (fail-closed): RLP y >= 0; PB requires lo <= hi on every pair of N.
- Not required: sortedness of S/V lists; reduced form of rationals (canonical decimal regex only; length <= 64).
- `code`, `pruned_nodes`, `seconds` and FH5 `counts` are parsed/type-checked but never decide anything.
- Dual checks are memoised by (q tuple, status tuple) only; RPLP "R" references reuse the same memo.
- run.json mismatches (leaves, orbits, rule counts, leafcodes sha, totals, dual count, decompressed sha) are FAIL, although run.json is untrusted: a certificate set inconsistent with its own summary is rejected.
- The controls harness is white-box (calls checker functions in-process on in-memory mutations); the CLI has no pin override.

## 5. Full body: `code/sun6_second_checker_v1.py`

```python
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
```

## 6. Full body: `code/sun6_second_checker_controls_v1.py`

```python
#!/usr/bin/env python3
"""Frozen-plan interpreter for the sun6-second-checker-v1 intended-reason controls.

NOT RUN. Execute only after parent source review and an item GO.  Standard library only.
Executes exactly the hashed checker bytes, reads the pinned inputs read-only, keeps every
mutation in memory, and writes only inside a new --out-dir (exclusive creation, no deletion).
Exit: 0 all controls MATCH; 1 some MISMATCH/ERROR; 2 stopped (deadline/signal); 3 setup rejected.
"""

import argparse
import copy
import gzip
import hashlib
import json
import os
import signal
import sys
import time
import types

CHECKER_SHA256 = "1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f"
PLAN_SHA256 = "42cd627528121b3a26ce886514b4cc24b0ec33ac83ee8f75fe11768b4563b01b"
HERE = os.path.dirname(os.path.abspath(__file__))


class SetupError(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_checker(path):
    with open(path, "rb") as f:
        data = f.read()
    if sha(data) != CHECKER_SHA256:
        raise SetupError("checker sha256 mismatch")
    mod = types.ModuleType("sun6_second_checker_v1")
    mod.__file__ = path
    exec(compile(data, path, "exec"), mod.__dict__)
    return mod


class Env:
    def __init__(self, ck, input_dir, deadline_ns, out_dir):
        self.ck = ck
        self.deadline_ns = deadline_ns
        self.out_dir = out_dir
        self.blobs = ck.read_inputs(input_dir)
        for name in ck.INPUT_NAMES:
            b = self.blobs.get(name)
            size, h = ck.INPUT_PINS[name]
            if type(b) is not bytes or len(b) != size or sha(b) != h:
                raise SetupError("input pin mismatch: " + name)
        self.plain = gzip.decompress(self.blobs["orbits.jsonl.gz"])
        if (len(self.plain), sha(self.plain)) != tuple(ck.ORBITS_PLAIN_PIN):
            raise SetupError("decompressed pin mismatch")
        self.records = ck.parse_orbit_lines(self.plain)
        self.duals = ck.parse_duals(self.blobs["rlp_duals.json"])
        self._leaves = {}

    def guard(self):
        return self.ck.Guard(self.deadline_ns)

    def leaves(self, tp):
        if tp not in self._leaves:
            self._leaves[tp] = self.ck.enumerate_leaves(self.ck.Status(tp), self.guard())[0]
        return self._leaves[tp]


def tp_of(x):
    return tuple(x)


def rationals(ck, strs):
    t = tuple(ck.parse_rational(s) for s in strs)
    if any(v is None for v in t):
        raise SetupError("non-rational string in plan")
    return t


def c_unit_tri(env, a, cid):
    ck = env.ck
    tmin, tmax = ck.tri_bounds(a["a_ij"], a["a_ik"], a["a_jk"], a["i"], a["j"], a["k"],
                               ck.Status(tp_of(a["type"])))
    return {"tau_min": tmin, "tau_max": tmax, "consistent": tmin <= tmax}


def c_unit_leaf(env, a, cid):
    ck = env.ck
    tp = tp_of(a["type"])
    out = {"t_consistent": ck.t_consistent(ck.matrix_from_code(a["code"]), ck.Status(tp))}
    if a.get("enumerate"):
        out["member"] = ck.lexkey_from_code(a["code"]) in env.leaves(tp)
    return out


def c_unit_stabilizer(env, a, cid):
    return {"size": len(env.ck.stabilizer(tp_of(a["type"])))}


def c_unit_orbit(env, a, cid):
    ck = env.ck
    getters = ck.lex_image_getters(ck.stabilizer(tp_of(a["type"])))
    return {"size": len(ck.orbit_of(ck.lexkey_from_code(a["rep"]), getters))}


def c_unit_placement(env, a, cid):
    r = env.ck.placement_reduction()
    return {"placements": r["placements"], "exactly_one": r["exactly_one"], "ok": r["ok"]}


def c_unit_dual(env, a, cid):
    ck = env.ck
    ctx = ck.RuleContext({}, env.guard())
    r = ck.dual_condition(tuple(a["q"]), tuple(tuple(s) for s in a["st5"]),
                          rationals(ck, a["y"]), ctx)
    return {"result": "VALID" if r is None else r[0]}


def c_unit_pbounds(env, a, cid):
    ck = env.ck
    lo, hi, u = ck.p_bounds(ck.matrix_from_code(a["rep"]), ck.Status(tp_of(a["type"])),
                            a["v"], a["j"], a["k"])
    return {"lo": str(lo), "hi": str(hi), "u": str(u)}


def c_unit_forced(env, a, cid):
    ck = env.ck
    A = ck.matrix_from_code(a["rep"])
    st = ck.Status(tp_of(a["type"]))
    N, st5, forced, amasks, _ylo, _yhi = ck.rplp_frame(A, st, a["v"])
    out = {"forced": sorted([N[x], N[y]] for (x, y) in forced), "admissible_A": len(amasks)}
    if "q" in a:
        ctx = ck.RuleContext({}, env.guard())
        allowed = set(ck.allowed_masks(tuple(a["q"]), st5, ctx))
        allowed.add(0)
        n = 0
        for am in amasks:
            sm = am
            while True:
                if sm in allowed:
                    n += 1
                if sm == 0:
                    break
                sm = (sm - 1) & am
        out["columns"] = n
    return out


def c_unit_fgcd(env, a, cid):
    ck = env.ck
    st = ck.Status(tp_of(a["type"]))
    ex = ck.fh5_exponents(st, a["x"], a["tx"], a["e5"])
    ey = ck.fh5_exponents(st, a["y"], a["ty"], a["e5"])
    return {"fgcd": ck.fgcd_value(ex, ey)}


def verify_outcome(env, tp, rep, rule, witness, duals):
    ck = env.ck
    ctx = ck.RuleContext(duals, env.guard())
    try:
        ck.verify_record(tp, rep, rule, witness, ctx)
        return {"status": "VERIFIED"}
    except ck.WitnessFail as exc:
        return {"status": "FAILED", "reason": exc.reason, "detail": exc.detail}


def c_record(env, a, cid):
    duals = {k: rationals(env.ck, ys) for k, ys in (a.get("duals") or {}).items()}
    return verify_outcome(env, tp_of(a["type"]), a["rep"], a["rule"], copy.deepcopy(a["witness"]),
                          duals)


def find_line(env, sel):
    tp = tp_of(sel["type"])
    hits = [r for r in env.records if r[1] == tp and r[2] == sel["rep"] and r[3] == sel["rule"]]
    if len(hits) != 1:
        raise SetupError("selector matched %d lines" % len(hits))
    return hits[0]


def nav(obj, path):
    for p in path:
        obj = obj[p]
    return obj


def c_record_data(env, a, cid):
    n, tp, rep, rule, wit = find_line(env, a["select"])
    w = copy.deepcopy(wit)
    duals = dict(env.duals)
    m = a["mutation"]
    op = m["op"]
    if op == "none":
        pass
    elif op == "duals_remove":
        if m["key"] not in duals:
            raise SetupError("dual key absent")
        del duals[m["key"]]
    elif op == "duals_replace":
        if m["key"] not in duals:
            raise SetupError("dual key absent")
        duals[m["key"]] = rationals(env.ck, m["y"])
    elif op == "witness_set":
        parent = nav(w, m["path"][:-1])
        idx = m["path"][-1]
        if type(parent) is not list or not 0 <= idx < len(parent):
            raise SetupError("bad witness path")
        parent[idx] = copy.deepcopy(m["value"])
    elif op == "witness_pop":
        lst = nav(w, m["path"])
        if type(lst) is not list or not lst:
            raise SetupError("bad witness path")
        lst.pop()
    elif op == "witness_swap":
        lst = nav(w, m["path"])
        lst[m["i"]], lst[m["j"]] = lst[m["j"]], lst[m["i"]]
    else:
        raise SetupError("unknown record_data op " + op)
    out = verify_outcome(env, tp, rep, rule, w, duals)
    out["line"] = n
    return out


def c_coverage(env, a, cid):
    ck = env.ck
    tp = tp_of(a["type"])
    items = [(r[0], ck.lexkey_from_code(r[2])) for r in env.records if r[1] == tp]
    m = a["mutation"]
    op = m["op"]
    if op == "none":
        pass
    elif op == "remove_rep":
        key = ck.lexkey_from_code(m["rep"])
        before = len(items)
        items = [it for it in items if it[1] != key]
        if len(items) != before - 1:
            raise SetupError("remove_rep did not remove exactly one line")
    elif op == "add_rep":
        items.append((10 ** 9, ck.lexkey_from_code(m["rep"])))
    elif op == "replace_rep":
        key = ck.lexkey_from_code(m["rep"])
        idx = [i for i, it in enumerate(items) if it[1] == key]
        if len(idx) != 1:
            raise SetupError("replace_rep selector")
        items[idx[0]] = (items[idx[0]][0], ck.lexkey_from_code(m["new_rep"]))
    else:
        raise SetupError("unknown coverage op " + op)
    cov = ck.check_coverage(items, env.leaves(tp), ck.lex_image_getters(ck.stabilizer(tp)),
                            env.guard())
    return {"clean": cov["clean"], "missing": cov["missing"], "missing_orbits": cov["missing_orbits"],
            "duplicates": len(cov["duplicate"]), "rep_not_leaf": len(cov["rep_not_leaf"]),
            "orbits_owned": cov["orbits_owned"], "covered": cov["covered"]}


def c_pipeline(env, a, cid):
    ck = env.ck
    blobs = dict(env.blobs)
    plain = env.plain
    m = a["mutation"]
    op = m["op"]
    plain_changed = False
    if op == "none":
        pass
    elif op == "flip_byte":
        b = bytearray(blobs[m["file"]])
        b[m["offset"]] ^= 0xFF
        blobs[m["file"]] = bytes(b)
    elif op == "append_bytes":
        blobs[m["file"]] = blobs[m["file"]] + m["text"].encode("ascii")
    elif op == "text_replace":
        old = m["old"].encode("ascii")
        b = blobs[m["file"]]
        if b.count(old) != 1:
            raise SetupError("text_replace anchor not unique")
        blobs[m["file"]] = b.replace(old, m["new"].encode("ascii"))
    elif op == "file_replace":
        blobs[m["file"]] = m["text"].encode("ascii")
    elif op == "plain_line_replace":
        lines = plain.split(b"\n")
        lines[m["line"] - 1] = m["text"].encode("ascii")
        plain = b"\n".join(lines)
        plain_changed = True
    elif op == "plain_strip_final_newline":
        if not plain.endswith(b"\n"):
            raise SetupError("no final newline to strip")
        plain = plain[:-1]
        plain_changed = True
    elif op == "plain_insert_empty_line":
        lines = plain.split(b"\n")
        lines.insert(m["after"], b"")
        plain = b"\n".join(lines)
        plain_changed = True
    else:
        raise SetupError("unknown pipeline op " + op)
    if plain_changed:
        blobs["orbits.jsonl.gz"] = gzip.compress(plain, compresslevel=9, mtime=0)
    rp = a["repin"]
    pins = None
    plain_pin = None
    if rp in ("all", "compressed_only"):
        pins = {n: (len(blobs[n]), sha(blobs[n])) for n in ck.INPUT_NAMES}
        if rp == "all":
            plain_pin = (len(plain), sha(plain))
    elif rp != "none":
        raise SetupError("unknown repin mode")
    g = a["guard"]
    mode = g["mode"]
    if mode == "far":
        guard = env.guard()
    elif mode == "past":
        guard = ck.Guard(0)
    elif mode == "cancel":
        guard = env.guard()
        guard.request_cancel("control")
    elif mode == "clock_after":
        calls = [0]
        limit = g["calls"]

        def clock():
            calls[0] += 1
            return 0 if calls[0] < limit else 2 ** 62

        guard = ck.Guard(10 ** 18, None, clock)
    else:
        raise SetupError("unknown guard mode")
    R = ck.run_check(blobs, guard, pins, plain_pin)
    W = R.get("witnesses") or {}
    return {"verdict": R["verdict"], "exit_code": R["exit_code"],
            "inputs_reject": (R["inputs"].get("reject") or {}).get("reason"),
            "parse_reject": ((R.get("parse") or {}).get("reject") or {}).get("reason"),
            "stop": R.get("stop"), "witnesses_verified": W.get("verified"),
            "witnesses_incomplete": W.get("incomplete")}


def c_publish(env, a, cid):
    ck = env.ck
    d = os.path.join(env.out_dir, "publish-" + cid)
    os.mkdir(d)
    pre = b"preexisting control bytes\n"
    rpath = os.path.join(d, "REPORT.json")
    spath = os.path.join(d, "REPORT.seal.json")
    if a["preexisting_report"]:
        ck.write_exclusive(rpath, pre)
    R = {"checker": ck.CHECKER_ID, "synthetic_control": cid, "verdict": a["verdict"],
         "exit_code": {"PASS": 0, "FAIL": 1, "INCOMPLETE": 2}[a["verdict"]]}
    guard = env.guard() if a["guard"] == "far" else ck.Guard(0)
    code = ck.publish(R, d, guard)
    out = {"exit_code": code, "seal": os.path.exists(spath)}
    with open(rpath, "rb") as f:
        body = f.read()
    if a["preexisting_report"]:
        out["preexisting_unchanged"] = (body == pre)
    else:
        out["report_verdict"] = json.loads(body.decode("ascii"))["verdict"]
        if out["seal"]:
            with open(spath, "rb") as f:
                seal = json.loads(f.read().decode("ascii"))
            out["seal_verdict"] = seal["verdict"]
            out["seal_hash_ok"] = (seal["report_sha256"] == sha(body))
    return out


RUNNERS = {"unit_tri": c_unit_tri, "unit_leaf": c_unit_leaf, "unit_stabilizer": c_unit_stabilizer,
           "unit_orbit": c_unit_orbit, "unit_placement": c_unit_placement, "unit_dual": c_unit_dual,
           "unit_pbounds": c_unit_pbounds, "unit_forced": c_unit_forced, "unit_fgcd": c_unit_fgcd,
           "record": c_record, "record_data": c_record_data, "coverage": c_coverage,
           "pipeline": c_pipeline, "publish": c_publish}


def write_result(out_dir, doc):
    body = (json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")
    path = os.path.join(out_dir, "CONTROLS-RESULT.json")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        view = memoryview(body)
        while len(view):
            n = os.write(fd, view)
            view = view[n:]
        os.fsync(fd)
    finally:
        os.close(fd)
    return sha(body)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="sun6-second-checker-v1-controls")
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--out-dir", required=True, help="must not exist; created exclusively")
    ap.add_argument("--deadline-epoch", required=True, type=int)
    ap.add_argument("--plan", default=os.path.join(os.path.dirname(HERE), "CONTROLS-PLAN-v1.json"))
    ap.add_argument("--checker", default=os.path.join(HERE, "sun6_second_checker_v1.py"))
    args = ap.parse_args(argv)
    flag = []

    def on_signal(signum, _frame):
        flag.append("signal-%d" % signum)

    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    try:
        os.mkdir(args.out_dir)
    except OSError as exc:
        sys.stderr.write("controls: out-dir not created exclusively: %s\n" % exc)
        return 3
    deadline_ns = args.deadline_epoch * 1000000000
    started = time.time_ns()
    doc = {"harness": "sun6-second-checker-v1-controls", "checker_sha256": CHECKER_SHA256,
           "plan_sha256": PLAN_SHA256, "started_ns": started, "python": sys.version}
    try:
        ck = load_checker(args.checker)
        with open(args.plan, "rb") as f:
            pb = f.read()
        if sha(pb) != PLAN_SHA256:
            raise SetupError("plan sha256 mismatch")
        plan = json.loads(pb.decode("ascii"))
        if plan["checker"]["sha256"] != CHECKER_SHA256:
            raise SetupError("plan names a different checker")
        env = Env(ck, args.input_dir, deadline_ns, args.out_dir)
    except Exception as exc:
        doc["setup_error"] = repr(exc)[:400]
        doc["exit_code"] = 3
        write_result(args.out_dir, doc)
        return 3
    results = []
    stopped = None
    for c in plan["controls"]:
        if stopped is None and flag:
            stopped = flag[0]
        if stopped is None and time.time_ns() >= deadline_ns:
            stopped = "DEADLINE"
        if stopped is not None:
            results.append({"id": c["id"], "status": "NOT_RUN", "reason": stopped})
            continue
        t0 = time.monotonic_ns()
        try:
            obs = RUNNERS[c["kind"]](env, c["args"], c["id"])
            match = all(k in obs and obs[k] == v for k, v in c["expect"].items())
            results.append({"id": c["id"], "kind": c["kind"],
                            "status": "MATCH" if match else "MISMATCH",
                            "expect": c["expect"], "observed": obs,
                            "elapsed_ns": time.monotonic_ns() - t0})
        except ck.StopRequested as exc:
            stopped = exc.reason
            results.append({"id": c["id"], "status": "STOPPED", "reason": exc.reason})
        except SetupError as exc:
            results.append({"id": c["id"], "status": "SETUP_ERROR", "detail": str(exc)[:300]})
        except Exception as exc:
            results.append({"id": c["id"], "status": "ERROR", "detail": repr(exc)[:300]})
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    doc["results"] = results
    doc["counts"] = counts
    doc["stopped"] = stopped
    doc["ended_ns"] = time.time_ns()
    if stopped is not None:
        code = 2
    elif counts.get("MATCH", 0) == len(plan["controls"]):
        code = 0
    else:
        code = 1
    doc["exit_code"] = code
    write_result(args.out_dir, doc)
    return code


if __name__ == "__main__":
    sys.exit(main())
```

## 7. Full body: `MATH-BRIDGE-v1.md`

# Sun6 second checker v1: mathematical bridge and every-rule source map

- Clock (/bin/date immediately before writing): 2026-10-19T17:35:10-0700
- Checker: `code/sun6_second_checker_v1.py`, sha256 `1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f` (not executed).
- Sources (read; hashes in READLOG-v1.json): README (R0, R1(6)), rules-k6-v1 (L0-L8), rules-k6-v2 (L9), rules-k6-v3 (L10-L12 + formats), proof-k6-lemmas-v1, rules-k6-erratum-v3 (C1-C22), CERT-FORMAT-k6-v3 (sections 0-4, 6), ACCEPTANCE-AMENDMENT-v1 (overlay), proof-k6-v3 (composition).
- Scope: this note states, for every predicate the checker decides, which written lemma turns it into "no configuration has this labelled pattern", and why the integer/rational decision is exact for EVERY admissible tau and EVERY pairwise-coprime cofactor vector with the given marker statuses. It does not re-prove the cited lemmas; they are imports (section 9). No new theorem, no novelty claim.

## 0. Notation used by the code

Vertices 0..5; `A[i][j]` = alpha_ij in {1,2,3,4} (L0.3: 1 <= alpha <= gcd - 1 = 4). A type is (e2, c2, e3). For a vertex z the code uses `r2(z)` in {0, 1, SAT} (v2(r_z) = 0; = 1 for E2 class 1; >= 2 for E2 class 2) and `r3(z)` in {0, SAT} (3 | r_z iff z = E3); SAT = 64. Sizes are in units of |G|.

## 1. Chain of the conclusion (what a PASS would mean)

1. R0 (README section 2): any counterexample in an arbitrary group gives one in a finite quotient with the same indices and disjointness.
2. Least-order frame (README section 2; C4, C15, C18): choose a finite counterexample G of minimal order; every proper subgroup satisfies Sun(6); Sun(k<=4) holds (Zhu Theorem 1.1, L0.6); Sun(5) holds (accepted import, section 9). By R1(6) G carries a Core5(6) configuration: indices 5r_i with pairwise coprime r_i and pairwise disjoint cosets.
3. Pattern: alpha_ij = [G:U_i cap U_j]/(5 r_i r_j) in {1..4}, plus markers E2 (with class), E3, E5 (any may coincide, C7).
4. Placement reduction (checker `placement_reduction`): all 13 x 7 = 91 placements of (E2 with class, E3) are mapped by some permutation in S6 onto exactly one of the 8 types. Relabelling vertices maps configurations to configurations, so every pattern is the image of a labelled pattern of one of the 8 types. E5 is not part of the type; see section 8.
5. Triangle rule T (section 2): a labelling with a T-failing triangle has no configuration. The checker enumerates EXACTLY the T-consistent labellings of each type (prunes only at completed triangles; every one of the 20 triangles is tested once; schedule self-checked).
6. Coverage (checker `check_coverage`): the stabiliser of the type (all p in S6 fixing e2 and e3 when present; sizes 720/120/24 asserted) maps the type to itself and preserves every rule; the union of the stabiliser orbits of the listed representatives must EQUAL the enumerated leaf set, orbits pairwise disjoint (no duplicate), every rep a leaf. Hence every T-consistent labelled pattern is the image of a listed rep.
7. Per-line rule checks (sections 3-7): each rep's witness, verified exactly, shows that rep admits no configuration in a least-order counterexample; relabelling transfers it to the whole orbit.
8. Hence no least-order Sun(6) counterexample carries Core5(6); by step 2 no least-order counterexample exists; so Sun(6) holds for all finite groups and, by R0, all groups (C18 form). The checker verifies steps 4-7 only.

## 2. Rule T (rules-k6-v1 L1; CERT-FORMAT 2) - `tri_bounds`, `t_consistent`, `triangle_tables`

- (T1) I_xy | L tau with L = 5 r_a r_b r_c (coprime r) gives alpha_xy | r_z tau, i.e. alpha_xy / gcd(alpha_xy, r_z) | tau. So tau is a multiple of tau_min = lcm of the three quotients.
- (T2)+(T3) give tau <= alpha_xy alpha_xz at each apex, so tau <= tau_max = min over the three vertices of the product of the two alphas there (= product of the two smallest).
- T-kill: tau_min > tau_max leaves no admissible tau (C9: "admissible" means satisfying these necessary constraints).
- Exactness for every cofactor: alpha in {1..4} has only primes 2, 3. gcd(alpha, r_z) = 2^min(v2(alpha), v2(r_z)) 3^min(v3(alpha), v3(r_z)). v2(r_z) is 0 unless z = E2 (exactly 1 for class 1, >= 2 for class 2) and v2(alpha) <= 2, so SAT = 64 gives the true value; v3(r_z) >= 1 iff z = E3 and v3(alpha) <= 1. This reproduces the L1 table for every instance (r_z = 1, prime powers, primes >= 7 included).

## 3. K (rules-k6-v1 L3, K1; CERT-FORMAT 3 "K", 6.7) - `verify_K`

- Predicate: S duplicate-free subset of N = V minus v; sum_(i in S) alpha_iv >= 5; for every pair {i,j} in S: tau_min(i,v,j) == alpha_iv alpha_vj.
- Bridge: for a T-consistent rep, tau_min <= tau <= tau_max <= alpha_iv alpha_vj (product at v), so the equality pins tau = alpha_iv alpha_vj for EVERY admissible tau (M1). By (T3) at apex i, |U_i(U_v cap U_j)| = tau/(5 alpha_vj) = alpha_iv/5 = |U_iU_v|, so L2 gives U_vU_i subset U_jU_i: the L3 pair condition. L3 then forces sum alpha_iv/5 <= 1 - 1/(5 r_v) < 1, i.e. sum <= 4, contradicting sum >= 5.
- Cofactors: only tau_min (section 2) and alphas are read. E5 irrelevant (C19). Imports: none beyond L0-L3.

## 4. P: Ppair and PB (rules-k6-v1 L4; C13; CERT-FORMAT 3, 6.7) - `p_bounds`, `verify_Ppair`, `verify_PB`

- X_j = U_vU_j, |X_j| = x_j = alpha_vj/5 (P1). |X_j cap X_k| is a union of (U_v, U_j cap U_k) double cosets (L0.5), each of size a multiple of 1/gcd(5 r_v, 5 r_j r_k alpha_jk) = 1/(5 gcd(r_v, alpha_jk)) =: u (L0.4; r_v coprime to r_j r_k). gcd(r_v, alpha_jk) is the section-2 value at z = v: exact for every instance.
- Lower bound (P3): U_v(U_j cap U_k) is inside the intersection and has size tau_vjk/(5 alpha_jk) >= tau_min/(5 alpha_jk) for every admissible tau (M1); also x_j + x_k - 1 and 0. lo = u ceil(Lb/u) is valid because the intersection is a multiple of u.
- Upper bound: min(x_j, x_k) rounded down to a multiple of u. If that equals min(x_j,x_k), equality would force X_j subset X_k (x_j < x_k), X_k subset X_j (x_k < x_j), or X_j = X_k (equal); by K2 (L3 at j with S = {v,k} using U_jU_v subset U_kU_v) X_j subset X_k needs alpha_vj + alpha_kj <= 4 (and symmetrically). When barred, the intersection is a strictly smaller multiple of u, so hi drops by u. The optional XE strengthening C21 is NOT used.
- Ppair: lo > hi leaves no value for |X_j cap X_k|.
- PB: union of Y_j = G minus X_j (j in S) avoids U_v (U_v subset every X_j), so its size is < 1; Bonferroni gives sum |Y_j| - sum |Y_j cap Y_k| <= |union| < 1 with |Y_j cap Y_k| = 1 - x_j - x_k + |X_j cap X_k| <= 1 - x_j - x_k + hi. So value >= 1 is impossible. The checker also enforces the format's precondition lo <= hi on every pair of N (if it failed, a Ppair would apply; enforcing it can only cause a fail-closed rejection).
- E5 irrelevant (alpha has no factor 5; C19).

## 5. RLP (rules-k6-v1 L7; rules-k6-v2 L9(b); C3, C10, C17; CERT-FORMAT 3 "RLP", 6.4) - `verify_RLP`, `check_q_dual`, `dual_condition`, `allowed_masks`

- Translate g_v = 1; D_j = U_v g_j U_j. (R1) D_j cap U_vU_j empty; (R2) |D_j| is a positive multiple of 1/gcd(5r_v,5r_j) = 1/5; so |D_j| = q_j/5 with 1 <= q_j <= 5 - alpha_vj, and d_j = |D_j|/|U_j| = q_j r_j. The true configuration has one such q (unknown), so EVERY q in the product is checked (itertools.product order, first neighbour slowest; key recomputed from (q, statuses)).
- Right U_v-cosets C partition G; mu(S) = mass of cosets with S_C = S (non-empty). Coverage sum_(S contains j) mu(S) = q_j/5; total <= 1 - |U_v| < 1 (U_v is in no D_j by R1).
- Support: by L9(b) (pieces in C, right-translated and inverted, are pairwise disjoint left cosets in U_v of indices d_l; Sun(|T|) in U_v for |T| <= 5) mu(S) > 0 only if every T subset of S, |T| >= 2, has a pair with gcd(d_x, d_y) >= |T| (|S| = 1 always allowed).
- maxgcd is the TRUE gcd for every instance: primes >= 5 cannot divide two d's (q <= 4, r's coprime); v2(gcd) = min(v2(q_x) + v2(r_x), v2(q_y) + v2(r_y)) with at most one E2; class 1 contributes exactly 1; for class 2, v2(r) >= 2 >= v2(q_partner), so the minimum is the partner's exponent, reproduced by SAT; likewise for 3 with E3 (v3(q) <= 1 <= v3(r_E3)). So the allowed family computed is exactly the family L9(b) permits, for every instance with the given markers (C5, C16 and proof-k6-lemmas-v1 section 1).
- Weak duality: if y >= 0, sum_(x in S) y_x <= 1 on EVERY allowed S, and sum (q_x/5) y_x >= 1, then total mass = sum_S mu(S) >= sum_S mu(S) sum_(x in S) y_x = sum_x y_x q_x/5 >= 1, contradiction. (With equality coverage y >= 0 is not mathematically needed; the checker enforces it because the format requires it - fail-closed.)
- Every used key is checked against all 31 non-empty subsets; results are memoised only by (q tuple, status tuple), which determine the check completely. Unused duals carry no weight and are counted.
- E5 irrelevant (C19). Imports: L0.6, Zhu (|T| = 3,4), Sun(5) (|T| = 5). Sun(6) never used (at most five pieces).

## 6. RPLP (rules-k6-v3 L12; proof-k6-lemmas-v1 section 4; CERT-FORMAT 3, 6.4, 6.5) - `rplp_frame`, `verify_RPLP`

- For each q (same enumeration as RLP): either ["R", key] whose key equals the recomputed key and whose dual passes section 5 (then that q is already impossible), or ["P", vec] with 30 exact rationals.
- Right U_v-cosets get types (A_C, S_C), A_C = {j : C subset Y_j}, S_C = {j : C subset D_j} subset A_C (R1). x(A,S) >= 0 masses on A non-empty; cosets with A empty lie in the intersection of the X_j and are excluded; total = |union Y_j| <= 1 - |U_v| < 1.
- Forced ORDERED pairs (w,j): tau_min(v,w,j) >= alpha_vw alpha_wj (product at w) pins tau = alpha_vw alpha_wj (T2 at w); (T3) at v gives |U_v(U_w cap U_j)| = alpha_vw/5 = |X_w|, so X_w subset X_j, Y_j subset Y_w: no coset has j in A and w not in A. Columns violating this have zero mass and are omitted; (w,j) and (j,w) are tested separately.
- Constraints: E1_j: sum_(S contains j) x = q_j/5; E2_j: sum_(A contains j) x = (5 - alpha_vj)/5; B_jk: ylo <= sum_(A contains j,k) x = |Y_j cap Y_k| <= yhi with ylo/yhi = 1 - (alpha_vj + alpha_vk)/5 + lo/hi from section 4 (valid for every admissible tau and instance).
- S must be empty, a singleton, or hereditary-allowed with maxgcd for this q (section 5).
- Weak duality: with a, b free and u, l >= 0, if every admitted column has coefficient sum_S a + sum_A b - sum_(p in A) u + sum_(p in A) l <= 1 and the objective sum a q/5 + sum b (5 - alpha)/5 - sum u yhi + sum l ylo >= 1, then sum x >= 1 for every feasible x, contradicting total < 1; an infeasible system is covered by the same check through Farkas (proof-k6-lemmas-v1 section 4).
- E5 irrelevant (C19). Imports as RLP.

## 7. FH5 (rules-k6-v1 L5, L6, L8; rules-k6-v2 L9(a); C2, C4, C6, C15, C16; CERT-FORMAT 3, 6.3) - `verify_FH5`, `fh5_search`

- Hypotheses checked: a != b, alpha_ab = 1, V recomputed as {v not in {a,b} : alpha_va = alpha_vb} equals the witness set (duplicate-free) and is non-empty.
- H5/L6: H := U_aU_b is a subgroup of index m = 5 containing U_a and U_b, and t_v = [U_v : U_v cap H] = alpha_va for v in V (t_v = 1, i.e. U_v subset H, when alpha_va = 1). H < G because [G:H] = 5.
- F1: g_lU_l meets exactly t_l left cosets of H (1 <= t_l <= 5). Cosets of H are labelled 0..4 up to relabelling; a meets one coset, fixed to 0 (only a is fixed, C6). Domains: b and V-vertices with alpha_va = 1: all 5 singletons; V-vertices with alpha_va = c > 1: all C(5,c) c-subsets; every other vertex: all 31 non-empty subsets with t = size.
- Rejection (both conditions are necessary in any configuration):
  - (F3) U_i subset H (t_i = 1) gives |U_iU_l| <= |HU_l| = t_l/5, i.e. alpha_il <= t_l.
  - (F2) with L9(a): the pieces of the cosets meeting a coset C of H, left-translated into H, are pairwise disjoint cosets of U_l cap H of index lambda_l = r_l t_l; every T subset of the members with |T| >= 2 needs a pair with gcd(lambda) >= |T|: Sun(2) = L0.6, Sun(3), Sun(4) = Zhu, Sun(5) = accepted import, Sun(6) = minimality of G applied to the proper subgroup H (THIS IS THE ONLY USE OF SUN(6), and it is valid only in the least-order frame of section 1).
- fgcd is the true gcd for every instance: t <= 5 so primes >= 7 cannot be common; class-1 E2 exact; class-2 E2 v2(r) >= 2 >= v2(t); E3 v3(r) >= 1 >= v3(t); E5 v5(r) >= 1 >= v5(t); SAT = 64 reproduces each minimum (C16; SAT5 >= 1 required and used).
- E5: the 7 placements None, 0..5 are all searched (E5 is not part of the type; an instance has at most one E5 vertex, possibly coinciding with E2/E3). [Observation, not used by the checker: since t_a = t_b = 1, a and b lie in distinct cosets (their lambdas are coprime), and a t = 5 vertex would meet both, needing gcd >= 2 with both; at most one of them can be E5, so no t = 5 vertex survives and E5 never changes an FH5 outcome here. The checker still runs all 7 placements as required.]
- Completeness: depth-first search over the full product of domains; a partial assignment is cut only when a rejection condition already holds, and both conditions persist under extension (F3 involves two assigned vertices; a failing subset T stays in the growing member set), so every completion is rejected. Exact accounting: (rejected-node weights = product of remaining domain sizes) + (complete assignments reached) must equal the domain product; any complete unrejected assignment is reported as FH5_SURVIVING_ASSIGNMENT. The engine's `counts` are informational only.

## 8. N26 (rules-k6-v3 L11; proof-k6-lemmas-v1 section 3; C11, C14, C19; CERT-FORMAT 3, 6.6) - `verify_N26`

- Predicate: v != E2; alpha_vj = 2 for all j != v; alpha_jk in {2,4} for all neighbour pairs; if v = E3: tau_max(j,k,l) < 3 tau_min(j,k,l) for every neighbour triple.
- Bridge: hypotheses (i)-(iii) are checked literally; (iv) gcd(r_v, tau_jkl) = 1: by C14 every admissible tau of a neighbour triangle is in {2,4,8,12,16} (a multiple of tau_min in {2,4} that is <= tau_max in {4,8,16}), so only 2 and 3 can divide it; r_v is odd (v != E2); if v != E3 then 3 does not divide r_v (covers r_v = 1, v = E5, primes >= 7, prime powers); if v = E3, tau_max < 3 tau_min leaves only tau in {tau_min, 2 tau_min}, powers of 2. Then L11 gives a contradiction.
- E5 irrelevant (covered by C14 consequence and C19).

## 9. Imports and dependencies stated literally

| Import | Where used by a certificate the checker accepts | Status |
|---|---|---|
| R0, R1(6), least-order frame | conclusion (section 1) | written, reviewed (README; C1, C12, C18); not checked by code |
| L0-L4, L6 (H5), L7 R1-R5', L9, L10-L12 written proofs | sections 2-8 | written, reviewed; imports |
| L0.6 (Sun(2)) | every hereditary test with |T| = 2 | classical |
| Zhu Theorem 1.1 (Sun(3), Sun(4)) | hereditary tests with |T| = 3, 4 | published import |
| Sun(5) in every group | hereditary tests with |T| = 5 (RLP/RPLP supports, FH5 cosets) and R1(6) p = 2 branch | accepted verdict 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 (sun-coset5 proof-v4 + erratum v3). That result is itself computer-assisted (including its S-D handling); THIS CHECKER DOES NOT re-verify or remove the Sun(5) computation; its second checker is a separate gate. |
| Sun(6) in proper subgroups | FH5 cosets with |T| = 6 only | valid only in the least-order counterexample frame (H < G) |

## 10. What the checker does NOT establish

- It does not verify the written lemmas, R0/R1(6), Zhu or Sun(5); it verifies that the pinned finite certificate set satisfies the written predicates exactly and covers the full labelled universe.
- It does not use the engine `code` field, run.json pruned_nodes/seconds or FH5 counts for any decision.
- A PASS is single-kernel CPython evidence with trusted OS/hardware; no Lean or formal kernel.
- No interface was found that could not be derived from the sources; no HOLD is raised at source level. The real-data outcome is unknown until an admitted run.

