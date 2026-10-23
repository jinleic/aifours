#!/usr/bin/env python3
"""sun5_second_checker_v1: second independently written exact checker for the
Sun disjoint-coset k = 5 finite pattern bridge (Core(5) certificates).

Mathematical sources (read in full; the only sources of the predicates below):
  proof-v4.md             3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516
  rules-v1.md             cb86c16836d929a21256c34f0a87a5fc71788b970a6e1052751a69d637d1390f
  rules-v1-erratum-v3.md  1b3e126e1c398a71401b4c7e13cbc19c276befe095bb1c0043450c3cd425e8ed
  README.md               6bff400c970958dd2c1077d76fb284a6869351702aeff286f48471d23945a75e
  README-addendum-v4.md   2995d392d4489b66a4dc0170f0910ea210237a4ebbd823dc0adcb29934170953
Written without reading any earlier checker, engine, producer or control
implementation.  Standard library only; exact int and fractions.Fraction; no
asserts (python -O cannot change behaviour); no subprocesses, network or
helpers.  The only files read are the input, this source (self-hash) and the
written outputs (read-back); the cancel file is only tested for existence; the
only files written are three new files in a new output directory.

Meaning of a PASS (status PASS_MODULO_WRITTEN_SD): the pinned extract contains
one record per S5-orbit of the labelled universe (alpha: E(K5) -> {1,2,3},
E2, E3 in {0..4, none}); the record orbits are pairwise disjoint and their union
is exactly the universe; every non-SURVIVE certificate is re-verified exactly;
the SURVIVE records cover exactly the S5-orbit of the pattern S-D of proof-v4
section 6.  The exclusion of S-D is written mathematics (proof-v4 sections 5-6)
and is NOT checked here; it is accounted separately as WRITTEN_SD.

Usage:
  sun5_second_checker_v1.py --input PATH --expected-sha256 HEX
      --output-dir NEW_DIR --deadline-epoch INT [--cancel-file PATH]
Exit status: 0 PASS (published, COMPLETE.json pass_valid true); 1 FAIL;
2 INCOMPLETE_DEADLINE; 3 INCOMPLETE_CANCELLED; 4 INCOMPLETE_ERROR;
5 INPUT_PIN_MISMATCH; 6 usage error or existing output directory (nothing
verified); 7 publication failure (no valid result).
"""

import hashlib
import json
import math
import os
import re
import signal
import sys
import time
import traceback
from array import array
from fractions import Fraction
from itertools import combinations, product

CHECKER_ID = "sun5_second_checker_v1"

# ---------------------------------------------------------------------------
# Labelled universe (rules-v1 section 0 and L0.3; proof-v4 section 4)
# ---------------------------------------------------------------------------
NV = 5
VERTICES = tuple(range(NV))
# Key digit order of the extract.  Cited decoding: engine-v1-run1/survivors.json
# maps "1122333333/10" to alpha 01,02,03,04,12,13,14,23,24,34 and E2=1, E3=0.
EDGES = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4))
NE = len(EDGES)
EDGE_MASK_ALL = (1 << NE) - 1
EDGE_ID = {}
for _k, (_i, _j) in enumerate(EDGES):
    EDGE_ID[(_i, _j)] = _k
    EDGE_ID[(_j, _i)] = _k
ALPHA_VALUES = (1, 2, 3)                 # L0.3 in Core(5): alpha_ij in {1, 2, 3}
N_COLOURINGS = len(ALPHA_VALUES) ** NE   # all maps E(K5) -> {1, 2, 3}
MARKER_SYMBOLS = "-01234"                # marker index 0 = none, index 1 + v = vertex v
N_MARKERS = len(MARKER_SYMBOLS)          # E2 and E3 each range over {none} u V
N_MARKER_PAIRS = N_MARKERS * N_MARKERS
N_LABELLED = N_COLOURINGS * N_MARKER_PAIRS
GROUP_ORDER = math.factorial(NV)         # |S5|

# proof-v4 section 6: the written-excluded pattern S-D, in the labelling of the text.
SD_ALPHA = {(0, 1): 1, (0, 2): 1, (0, 3): 2, (0, 4): 2,
            (1, 2): 3, (1, 3): 3, (1, 4): 3, (2, 3): 3, (2, 4): 3, (3, 4): 3}
SD_E2 = 1
SD_E3 = 0
# proof-v4 section 4 states the stabiliser of S-D is {id, (3 4)} (orbit of 60).
SD_STABILISER_TEXT = frozenset([(0, 1, 2, 3, 4), (0, 1, 2, 4, 3)])

ST_PASS_SD = "PASS_MODULO_WRITTEN_SD"
ST_PASS_ALL = "PASS_ALL_CERTIFIED"
ST_FAIL = "FAIL"
ST_DEADLINE = "INCOMPLETE_DEADLINE"
ST_CANCEL = "INCOMPLETE_CANCELLED"
ST_ERROR = "INCOMPLETE_ERROR"
ST_PIN = "INPUT_PIN_MISMATCH"
EXIT_CODE = {ST_PASS_SD: 0, ST_PASS_ALL: 0, ST_FAIL: 1, ST_DEADLINE: 2,
             ST_CANCEL: 3, ST_ERROR: 4, ST_PIN: 5}
EXIT_USAGE = 6
EXIT_PUBLICATION = 7

R_VERIFIED = "VERIFIED"
R_FAILED = "FAILED"
R_UNVERIFIED = "UNVERIFIED"
R_WRITTEN_SD = "WRITTEN_SD"
RECORD_STATUSES = (R_VERIFIED, R_FAILED, R_UNVERIFIED, R_WRITTEN_SD)

MAX_LISTED_FAILURES = 2000
MAX_MISSING_EXAMPLES = 20


class InternalError(Exception):
    """A self-check of this program failed; the run can only end INCOMPLETE_ERROR."""


class Stop(Exception):
    """Deadline, cancel file or signal observed; the run can never PASS."""

    def __init__(self, status, detail):
        Exception.__init__(self, detail)
        self.status = status
        self.detail = detail


class Guard(object):
    """Fail-closed stop conditions polled during every long phase."""

    def __init__(self, deadline_epoch, cancel_file):
        self.deadline_epoch = deadline_epoch
        self.cancel_file = cancel_file
        self.signal_seen = None

    def on_signal(self, signum, frame):
        self.signal_seen = signum

    def condition(self):
        """None, or [status, detail] of the first stop condition present now."""
        if self.signal_seen is not None:
            return [ST_CANCEL, "signal %d observed" % self.signal_seen]
        if self.cancel_file is not None and os.path.lexists(self.cancel_file):
            return [ST_CANCEL, "cancel file present"]
        if time.time() >= self.deadline_epoch:
            return [ST_DEADLINE, "deadline reached"]
        return None

    def poll(self, where):
        c = self.condition()
        if c is not None:
            raise Stop(c[0], "%s at %s" % (c[1], where))


# ---------------------------------------------------------------------------
# Strict byte-level parser (scalar schema: see 02-scalar-schema-v1.md)
# ---------------------------------------------------------------------------
KEY_RE = re.compile(rb"([123]{10})/([-0-4])([-0-4])")
RULE_NAMES = {b"T": "T", b"K": "K", b"PB": "PB", b"N2": "N2", b"FH2": "FH2",
              b"SURVIVE": "SURVIVE"}
_V = rb"([0-4])"
_N = rb"(0|[1-9][0-9]{0,5})"
_VS_RE = re.compile(rb"\[" + _V + rb",\[([0-4](?:,[0-4]){1,3})\],\"" + _N +
                    rb"(?:/([1-9][0-9]{0,5}))?\"\]")
WITNESS_RE = {
    "T": re.compile(rb"\[\[" + _V + rb"," + _V + rb"," + _V + rb"\]," + _N + rb"," + _N + rb"\]"),
    "K": _VS_RE,
    "PB": _VS_RE,
    "N2": re.compile(rb"\[\]"),
    "FH2": re.compile(rb"\[\[" + _V + rb"," + _V + rb"\],\[([0-4](?:,[0-4]){0,2})\]," +
                      _N + rb"," + _N + rb"\]"),
    "SURVIVE": re.compile(rb"-"),
}


def strictly_increasing(seq):
    return all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))


def parse_key(raw):
    """KEY = ten alpha digits (edge order EDGES) '/' E2 E3; '-' = no such vertex."""
    m = KEY_RE.fullmatch(raw)
    if m is None:
        return None
    digits = tuple(c - 48 for c in m.group(1))
    m2i = MARKER_SYMBOLS.index(chr(m.group(2)[0]))
    m3i = MARKER_SYMBOLS.index(chr(m.group(3)[0]))
    al = [[0] * NV for _ in VERTICES]
    a1 = 0
    a2 = 0
    for k, (i, j) in enumerate(EDGES):
        d = digits[k]
        al[i][j] = d
        al[j][i] = d
        if d == 1:
            a1 |= 1 << k
        elif d == 2:
            a2 |= 1 << k
    e2 = None if m2i == 0 else m2i - 1
    e3 = None if m3i == 0 else m3i - 1
    return {"al": al, "a1": a1, "a2": a2, "m2i": m2i, "m3i": m3i, "e2": e2, "e3": e3}


def parse_witness(rule, raw):
    """Return (witness, None) or (None, reason).  Grammar per rule, no json module."""
    m = WITNESS_RE[rule].fullmatch(raw)
    if m is None:
        return None, "PARSE_WITNESS_SYNTAX"
    g = m.groups()
    if rule == "T":
        tri = (int(g[0]), int(g[1]), int(g[2]))
        if not strictly_increasing(tri):
            return None, "PARSE_INDEX_ORDER"
        return (tri, int(g[3]), int(g[4])), None
    if rule == "K" or rule == "PB":
        v = int(g[0])
        s = tuple(int(c) for c in g[1].split(b","))
        if not strictly_increasing(s):
            return None, "PARSE_INDEX_ORDER"
        if v in s:
            return None, "PARSE_VERTEX_IN_SET"
        num = int(g[2])
        if g[3] is None:
            den = 1
        else:
            den = int(g[3])
            if den <= 1 or math.gcd(num, den) != 1:
                return None, "PARSE_NONCANONICAL_RATIONAL"
        return (v, s, Fraction(num, den)), None
    if rule == "FH2":
        a = int(g[0])
        b = int(g[1])
        v2 = tuple(int(c) for c in g[2].split(b","))
        if not a < b or not strictly_increasing(v2):
            return None, "PARSE_INDEX_ORDER"
        if a in v2 or b in v2:
            return None, "PARSE_VERTEX_IN_SET"
        return ((a, b), v2, int(g[3]), int(g[4])), None
    return (), None  # N2 '[]' and SURVIVE '-'


def escape_field(raw):
    out = []
    for c in raw:
        if 0x20 <= c <= 0x7e and c != 0x5c:
            out.append(chr(c))
        else:
            out.append("\\x%02x" % c)
    return "".join(out)


class Rec(object):
    __slots__ = ("line", "raw_key", "raw_rule", "key", "rule", "w", "status",
                 "reasons", "detail", "orbit", "stab")

    def __init__(self, line, raw_key, raw_rule):
        self.line = line
        self.raw_key = raw_key
        self.raw_rule = raw_rule
        self.key = None
        self.rule = None
        self.w = None
        self.status = R_UNVERIFIED
        self.reasons = []
        self.detail = None
        self.orbit = 0
        self.stab = 0

    def fail(self, reason):
        if reason not in self.reasons:
            self.reasons.append(reason)
        self.status = R_FAILED


def parse_file(state, data, guard):
    """Account for every byte: file-level defects plus one Rec per line."""
    if len(data) == 0:
        state.file_reasons.append("FILE_EMPTY")
        return
    bad = [i for i, c in enumerate(data) if not (c == 0x09 or c == 0x0a or 0x20 <= c <= 0x7e)]
    if bad:
        state.file_reasons.append("FILE_FORBIDDEN_BYTE:count=%d,first_offset=%d" % (len(bad), bad[0]))
    pieces = data.split(b"\n")
    truncated = data[-1:] != b"\n"
    if truncated:
        state.file_reasons.append("FILE_NO_FINAL_NEWLINE")
    else:
        pieces.pop()  # the empty string after the final newline
    state.structure["input_lines"] = len(pieces)
    first_line_of_key = {}
    for n, line in enumerate(pieces):
        if (n & 255) == 0:
            guard.poll("parse")
        fields = line.split(b"\t")
        rec = Rec(n + 1, fields[0], fields[1] if len(fields) > 1 else b"")
        state.recs.append(rec)
        if truncated and n == len(pieces) - 1:
            rec.fail("PARSE_TRUNCATED_FINAL_LINE")
        if line == b"":
            rec.fail("PARSE_EMPTY_LINE")
            continue
        if len(fields) != 3:
            rec.fail("PARSE_FIELD_COUNT")
            continue
        key = parse_key(fields[0])
        if key is None:
            rec.fail("PARSE_KEY")
        else:
            rec.key = key
            if fields[0] in first_line_of_key:
                rec.fail("PARSE_DUPLICATE_KEY:first_line=%d" % first_line_of_key[fields[0]])
            else:
                first_line_of_key[fields[0]] = rec.line
        rule = RULE_NAMES.get(fields[1])
        if rule is None:
            rec.fail("PARSE_UNKNOWN_RULE")
            continue
        rec.rule = rule
        w, why = parse_witness(rule, fields[2])
        if why is not None:
            rec.fail(why)
        else:
            rec.w = w


# ---------------------------------------------------------------------------
# S5 by generator closure, induced action on edge-colour masks and markers
# ---------------------------------------------------------------------------
def build_group():
    """Closure of {(0 1), (0 1 2 3 4)} under composition.  In a finite group the
    closure under multiplication by generators is the generated subgroup; 120
    distinct bijections of a 5-set is all of S5."""
    identity = tuple(VERTICES)
    generators = ((1, 0, 2, 3, 4), (1, 2, 3, 4, 0))
    seen = set([identity])
    elements = [identity]
    frontier = [identity]
    while frontier:
        nxt = []
        for g in frontier:
            for s in generators:
                h = tuple(s[g[i]] for i in VERTICES)  # h = s o g
                if h not in seen:
                    seen.add(h)
                    elements.append(h)
                    nxt.append(h)
        frontier = nxt
    ok = len(elements) == GROUP_ORDER and all(sorted(p) == list(VERTICES) for p in elements)
    return elements, ok


def edge_permutation(p):
    """Edge k = {i, j} goes to edge {p(i), p(j)}: (p.alpha)(p(i), p(j)) = alpha(i, j)."""
    return tuple(EDGE_ID[(p[i], p[j])] for (i, j) in EDGES)


def mask_table(ep):
    table = array("H", [0]) * (1 << NE)
    for mask in range(1 << NE):
        image = 0
        for k in range(NE):
            if (mask >> k) & 1:
                image |= 1 << ep[k]
        table[mask] = image
    return table


def marker_map(p):
    """Marker index 0 (none) is fixed; index 1 + v goes to 1 + p(v)."""
    return (0,) + tuple(1 + p[v] for v in VERTICES)


def build_universe(guard):
    """All colourings c: E -> {1,2,3} as disjoint mask pairs (A1, A2) = (c^-1(1),
    c^-1(2)): A1 runs over every subset of E and A2 over every subset of E \\ A1.
    Returns the direct-address rank table, the rank-ordered list, and whether
    every colouring appeared exactly once with the definitional count 3^10."""
    rank = array("i", [-1]) * (1 << (2 * NE))
    colourings = []
    repeated = False
    for a1 in range(1 << NE):
        if (a1 & 63) == 0:
            guard.poll("universe")
        rest = EDGE_MASK_ALL ^ a1
        a2 = rest
        while True:
            slot = (a2 << NE) | a1
            if rank[slot] != -1:
                repeated = True
            else:
                rank[slot] = len(colourings)
                colourings.append((a1, a2))
            if a2 == 0:
                break
            a2 = (a2 - 1) & rest
    ok = (not repeated) and len(colourings) == N_COLOURINGS
    return rank, colourings, ok


def dense_index(rnk, m2i, m3i):
    return (rnk * N_MARKERS + m2i) * N_MARKERS + m3i


def orbit_of(a1, a2, m2i, m3i, acts, rank):
    """Forward orbit {g.x : g in S5} as dense indices, stabiliser size and the
    number of images outside the universe (must be 0)."""
    images = set()
    stab = 0
    outside = 0
    for table, mmap in acts:
        b1 = table[a1]
        b2 = table[a2]
        r = rank[(b2 << NE) | b1]
        if r < 0:
            outside += 1
            continue
        n2 = mmap[m2i]
        n3 = mmap[m3i]
        images.add(dense_index(r, n2, n3))
        if b1 == a1 and b2 == a2 and n2 == m2i and n3 == m3i:
            stab += 1
    return images, stab, outside


def decode_index(idx, colourings):
    rnk, rem = divmod(idx, N_MARKER_PAIRS)
    m2i, m3i = divmod(rem, N_MARKERS)
    a1, a2 = colourings[rnk]
    digits = []
    for k in range(NE):
        digits.append("1" if (a1 >> k) & 1 else ("2" if (a2 >> k) & 1 else "3"))
    return "".join(digits) + "/" + MARKER_SYMBOLS[m2i] + MARKER_SYMBOLS[m3i]


def burnside_orbit_count(elements):
    """(1/|S5|) sum_g |Fix(g)| with |Fix(g)| = 3^(edge cycles) * (1 + fixed vertices)^2."""
    total = 0
    for p in elements:
        ep = edge_permutation(p)
        seen = [False] * NE
        cycles = 0
        for k in range(NE):
            if not seen[k]:
                cycles += 1
                j = k
                while not seen[j]:
                    seen[j] = True
                    j = ep[j]
        fixed = sum(1 for v in VERTICES if p[v] == v)
        total += (len(ALPHA_VALUES) ** cycles) * (1 + fixed) ** 2
    return total


# ---------------------------------------------------------------------------
# Rule predicates (exact; r enters only through the marker status)
# ---------------------------------------------------------------------------
def gcd_alpha_r(alpha, z, e2, e3):
    """gcd(alpha, r_z) for alpha in {1,2,3}: equals alpha iff alpha | r_z, i.e. iff
    (alpha = 2 and z = E2) or (alpha = 3 and z = E3); otherwise 1 (rules-v1 L1,
    erratum v3 E5).  Valid for every pairwise-coprime r with this marker status."""
    if alpha == 2 and z == e2:
        return 2
    if alpha == 3 and z == e3:
        return 3
    return 1


def lcm(x, y):
    return x * y // math.gcd(x, y)


def tau_min(al, e2, e3, x, y, z):
    """Least tau with (T1) in Core(5) form: alpha_xy | r_z tau for each edge."""
    q1 = al[x][y] // gcd_alpha_r(al[x][y], z, e2, e3)
    q2 = al[x][z] // gcd_alpha_r(al[x][z], y, e2, e3)
    q3 = al[y][z] // gcd_alpha_r(al[y][z], x, e2, e3)
    return lcm(lcm(q1, q2), q3)


def tau_max(al, x, y, z):
    """Largest tau with (T2) at all three apexes: smallest vertex product."""
    return min(al[x][y] * al[x][z], al[y][x] * al[y][z], al[z][x] * al[z][y])


def check_t(key, w):
    (a, b, c), s_min, s_max = w
    al, e2, e3 = key["al"], key["e2"], key["e3"]
    t_min = tau_min(al, e2, e3, a, b, c)
    t_max = tau_max(al, a, b, c)
    reasons = []
    if t_min != s_min:
        reasons.append("T_SERIALIZED_TAU_MIN_MISMATCH")
    if t_max != s_max:
        reasons.append("T_SERIALIZED_TAU_MAX_MISMATCH")
    if not t_min > t_max:
        reasons.append("T_NOT_KILLING")
    return reasons, {"tau_min": t_min, "tau_max": t_max}


def check_k(key, w):
    v, s, q = w
    al, e2, e3 = key["al"], key["e2"], key["e3"]
    reasons = []
    for i, j in combinations(s, 2):
        # K1 at tau_min (rules-v1 L3 K1, L8 M1): tau_min(v,i,j) = alpha_vi alpha_vj.
        if tau_min(al, e2, e3, v, i, j) != al[v][i] * al[v][j]:
            reasons.append("K_LINK_ABSENT:%d%d" % (i, j))
    total = sum(al[i][v] for i in s)
    if total < 4:  # L3 in Core(5): the pair condition forces sum alpha_iv <= 3
        reasons.append("K_SUM_BELOW_4")
    if Fraction(total, 4) != q:
        reasons.append("K_SERIALIZED_SUM_MISMATCH")
    return reasons, {"sum_over_4": str(Fraction(total, 4))}


def pb_value(al, e2, e3, v, s):
    """Left side of (P5) at |X_j cap X_k| = hi_jk, in units of |G| (rules-v1 L4)."""
    x = {}
    for j in s:
        x[j] = Fraction(al[v][j], 4)  # (P1) |X_j| = alpha_vj |G| / 4
    value = Fraction(0)
    for j in s:
        value += 1 - x[j]
    his = {}
    for j, k in combinations(s, 2):
        u = Fraction(1, 4 * gcd_alpha_r(al[j][k], v, e2, e3))  # (P2) unit
        low = min(x[j], x[k])
        hi = (low // u) * u  # largest multiple of u <= min(|X_j|, |X_k|)
        if hi == low:
            # (P4): equality would force X_j <= X_k (or the reverse, or both);
            # K2 for U_vU_j <= U_vU_k requires alpha_vj + alpha_jk <= 3.
            if x[j] < x[k]:
                barred = al[v][j] + al[j][k] >= 4
            elif x[k] < x[j]:
                barred = al[v][k] + al[j][k] >= 4
            else:
                barred = (al[v][j] + al[j][k] >= 4) or (al[v][k] + al[j][k] >= 4)
            if barred:
                hi = hi - u
        his["%d%d" % (j, k)] = str(hi)
        value -= 1 - x[j] - x[k] + hi
    return value, his


def check_pb(key, w):
    v, s, q = w
    value, his = pb_value(key["al"], key["e2"], key["e3"], v, s)
    reasons = []
    if not value >= 1:
        reasons.append("PB_NOT_KILLING")
    if value != q:
        reasons.append("PB_SERIALIZED_VALUE_MISMATCH")
    return reasons, {"value": str(value), "hi": his}


def check_n2(key, w):
    al = key["al"]
    if all(al[i][j] == 2 for (i, j) in EDGES):
        return [], None
    return ["N2_NOT_ALL_TWO"], None


def p_adic(n, p):
    if n <= 0:
        raise InternalError("valuation of a non-positive integer")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def lambda_exponents(l, t, m, e2, e3):
    """(v2, v3) of lambda_l = 4 r_l t_l / m (rules-v1 L6 F1), as the supremum over
    every admissible r with this marker status: v2(r_l) = 0 unless l = E2, where
    it is any value >= 1 (None = unbounded); likewise v3 with E3.  Primes >= 5
    are never common to two lambdas (t <= 4, r pairwise coprime)."""
    base2 = 2 + p_adic(t, 2) - p_adic(m, 2)
    base3 = p_adic(t, 3)
    if base2 < 0:
        raise InternalError("negative 2-adic exponent")
    return (None if l == e2 else base2), (None if l == e3 else base3)


def min_exponent(x, y):
    if x is None and y is None:
        raise InternalError("two marker vertices for one prime")
    if x is None:
        return y
    if y is None:
        return x
    return x if x < y else y


def lambda_gcd_sup(l, tl, k, tk, m, e2, e3):
    l2, l3 = lambda_exponents(l, tl, m, e2, e3)
    k2, k3 = lambda_exponents(k, tk, m, e2, e3)
    return (2 ** min_exponent(l2, k2)) * (3 ** min_exponent(l3, k3))


def fh2_rejected(asg, al, e2, e3, m):
    """asg[l] = (t_l, met-coset bitmask).  Rejected iff (F3) fails at a vertex with
    t = 1, or some coset with s >= 2 members has every pairwise gcd < s (F2)."""
    for i in VERTICES:
        if asg[i][0] == 1:  # U_i inside H
            for l in VERTICES:
                # (F3): alpha_il / 4 <= t_l / m
                if l != i and al[i][l] * m > 4 * asg[l][0]:
                    return True
    for c in range(m):
        members = [l for l in VERTICES if (asg[l][1] >> c) & 1]
        s = len(members)
        if s >= 2:
            if all(lambda_gcd_sup(l, asg[l][0], k, asg[k][0], m, e2, e3) < s
                   for l, k in combinations(members, 2)):
                return True
    return False


def subsets_of_size(m, t):
    return tuple(sum(1 << c for c in comb) for comb in combinations(range(m), t))


def fh2_options(a, b, v2set, m, t_v2):
    opts = []
    for l in VERTICES:
        if l == a:
            opts.append(((1, 1),))  # t_a = 1; its coset labelled 0 (only symmetry used)
        elif l == b:
            opts.append(tuple((1, s) for s in subsets_of_size(m, 1)))
        elif l in v2set:
            opts.append(tuple((t_v2, s) for s in subsets_of_size(m, t_v2)))
        else:
            opts.append(tuple((t, s) for t in range(1, m + 1) for s in subsets_of_size(m, t)))
    return opts


def fh2_case(al, e2, e3, a, b, v2set, m, t_v2, guard):
    count = 0
    survivors = 0
    first = None
    for asg in product(*fh2_options(a, b, v2set, m, t_v2)):
        count += 1
        if (count & 511) == 0:
            guard.poll("FH2")
        if not fh2_rejected(asg, al, e2, e3, m):
            survivors += 1
            if first is None:
                first = [[t, [c for c in range(m) if (s >> c) & 1]] for (t, s) in asg]
    return count, survivors, first


def check_fh2(key, w, guard):
    (a, b), v2_ser, n_i, n_ii = w
    al, e2, e3 = key["al"], key["e2"], key["e3"]
    reasons = []
    if al[a][b] != 1:
        reasons.append("FH2_ALPHA_AB_NOT_1")
    v2 = tuple(v for v in VERTICES if v != a and v != b and al[v][a] == 2 and al[v][b] == 2)
    if not v2:
        reasons.append("FH2_V2_EMPTY")
    if v2 != v2_ser:
        reasons.append("FH2_V2_MISMATCH")
    if reasons:
        return reasons, {"v2": list(v2)}
    # rules-v1 L7 H2, the SAME pair (a, b) in both alternatives:
    c1, s1, x1 = fh2_case(al, e2, e3, a, b, v2, 4, 2, guard)  # (i)  [G:W] = 4, t_v = 2
    c2, s2, x2 = fh2_case(al, e2, e3, a, b, v2, 2, 1, guard)  # (ii) [G:W] = 2, t_v = 1
    if s1:
        reasons.append("FH2_CASE_I_NOT_REFUTED")
    if s2:
        reasons.append("FH2_CASE_II_NOT_REFUTED")
    if c1 != n_i:
        reasons.append("FH2_COUNT_I_MISMATCH")
    if c2 != n_ii:
        reasons.append("FH2_COUNT_II_MISMATCH")
    return reasons, {"v2": list(v2), "count_i": c1, "survivors_i": s1, "example_i": x1,
                     "count_ii": c2, "survivors_ii": s2, "example_ii": x2}


# ---------------------------------------------------------------------------
# Run state, phases, decision
# ---------------------------------------------------------------------------
class State(object):
    def __init__(self):
        self.recs = []
        self.file_reasons = []
        self.structure = {}
        self.coverage = {}
        self.labelled = {}
        self.phases = []
        self.input_sha = None
        self.input_bytes = None
        self.self_sha = None
        self.pin_mismatch = False
        self.stop = None
        self.error = None
        self.complete = False


def phase(state, name):
    state.phases.append([name, time.time()])
    sys.stderr.write("%s %s phase %s\n" % (CHECKER_ID, time.strftime("%Y-%m-%dT%H:%M:%S%z"), name))
    sys.stderr.flush()


def run(state, args, guard):
    phase(state, "read")
    with open(os.path.abspath(__file__), "rb") as fh:
        state.self_sha = hashlib.sha256(fh.read()).hexdigest()
    with open(args["input"], "rb") as fh:
        data = fh.read()
    state.input_bytes = len(data)
    state.input_sha = hashlib.sha256(data).hexdigest()
    if state.input_sha != args["expected_sha256"]:
        state.pin_mismatch = True
        return
    guard.poll("after-read")

    phase(state, "parse")
    parse_file(state, data, guard)

    phase(state, "group")
    elements, group_ok = build_group()
    state.structure["group_closure_order"] = len(elements)
    if not group_ok:
        raise InternalError("generator closure is not S5")
    acts = []
    for p in elements:
        guard.poll("tables")
        acts.append((mask_table(edge_permutation(p)), marker_map(p)))

    phase(state, "universe")
    rank, colourings, universe_ok = build_universe(guard)
    state.structure["colourings"] = len(colourings)
    state.structure["labelled_universe"] = len(colourings) * N_MARKER_PAIRS
    if not universe_ok:
        raise InternalError("colouring enumeration is not a bijection onto 3^10 colourings")

    phase(state, "sd-orbit")
    sd_a1 = 0
    sd_a2 = 0
    for k, e in enumerate(EDGES):
        if SD_ALPHA[e] == 1:
            sd_a1 |= 1 << k
        elif SD_ALPHA[e] == 2:
            sd_a2 |= 1 << k
    sd_orbit, sd_stab, sd_out = orbit_of(sd_a1, sd_a2, 1 + SD_E2, 1 + SD_E3, acts, rank)
    sd_stab_elems = set()
    for p, (table, mmap) in zip(elements, acts):
        if (table[sd_a1] == sd_a1 and table[sd_a2] == sd_a2 and
                mmap[1 + SD_E2] == 1 + SD_E2 and mmap[1 + SD_E3] == 1 + SD_E3):
            sd_stab_elems.add(p)
    state.structure["sd_orbit_size"] = len(sd_orbit)
    state.structure["sd_stabiliser"] = sorted([list(p) for p in sd_stab_elems])
    if sd_out != 0 or len(sd_orbit) * sd_stab != GROUP_ORDER:
        raise InternalError("S-D orbit computation inconsistent")
    if frozenset(sd_stab_elems) != SD_STABILISER_TEXT:
        raise InternalError("S-D stabiliser differs from proof-v4 section 4 statement")

    phase(state, "coverage")
    owner = array("i", [-1]) * N_LABELLED
    overlap_events = 0
    images_total = 0
    for pos, rec in enumerate(state.recs):
        if (pos & 63) == 0:
            guard.poll("coverage")
        if rec.key is None:
            continue
        key = rec.key
        images, stab, outside = orbit_of(key["a1"], key["a2"], key["m2i"], key["m3i"], acts, rank)
        rec.orbit = len(images)
        rec.stab = stab
        if outside != 0 or len(images) * stab != GROUP_ORDER:
            raise InternalError("orbit-stabiliser inconsistency at line %d" % rec.line)
        images_total += len(images)
        for idx in images:
            o = owner[idx]
            if o == -1:
                owner[idx] = pos
            elif o != pos:
                overlap_events += 1
                rec.fail("ORBIT_OVERLAP:line=%d" % state.recs[o].line)
                state.recs[o].fail("ORBIT_OVERLAPPED:line=%d" % rec.line)
        if rec.rule == "SURVIVE" and rec.w is not None:
            if images == sd_orbit:
                rec.status = R_WRITTEN_SD if rec.status != R_FAILED else R_FAILED
            else:
                rec.fail("SURVIVOR_NOT_SD")
    missing = owner.count(-1)
    state.coverage = {"owned": N_LABELLED - missing, "missing": missing,
                      "overlap_events": overlap_events, "orbit_images_total": images_total}
    if missing:
        state.file_reasons.append("UNIVERSE_MISSING:count=%d" % missing)
        examples = []
        for idx in range(N_LABELLED):
            if owner[idx] == -1:
                examples.append(decode_index(idx, colourings))
                if len(examples) >= MAX_MISSING_EXAMPLES:
                    break
        state.coverage["missing_examples"] = examples
    if overlap_events:
        state.file_reasons.append("ORBIT_OVERLAP_EVENTS:count=%d" % overlap_events)

    phase(state, "witnesses")
    for pos, rec in enumerate(state.recs):
        if (pos & 63) == 0:
            guard.poll("witnesses")
        if rec.key is None or rec.w is None or rec.rule == "SURVIVE":
            continue
        if rec.rule == "T":
            reasons, detail = check_t(rec.key, rec.w)
        elif rec.rule == "K":
            reasons, detail = check_k(rec.key, rec.w)
        elif rec.rule == "PB":
            reasons, detail = check_pb(rec.key, rec.w)
        elif rec.rule == "N2":
            reasons, detail = check_n2(rec.key, rec.w)
        elif rec.rule == "FH2":
            reasons, detail = check_fh2(rec.key, rec.w, guard)
        else:
            raise InternalError("unreachable rule %r" % rec.rule)
        rec.detail = detail
        for r in reasons:
            rec.fail(r)
        if not reasons and rec.status == R_UNVERIFIED:
            rec.status = R_VERIFIED

    phase(state, "burnside")
    total_fix = burnside_orbit_count(elements)
    state.structure["burnside_sum_fix"] = total_fix
    if total_fix % GROUP_ORDER != 0:
        raise InternalError("Burnside sum not divisible by |S5|")
    state.structure["burnside_orbits"] = total_fix // GROUP_ORDER
    if missing == 0 and overlap_events == 0:
        keyed = sum(1 for rec in state.recs if rec.key is not None)
        if keyed != total_fix // GROUP_ORDER:
            raise InternalError("exact partition but record count differs from Burnside count")

    phase(state, "labelled-accounting")
    by_status = dict((s, 0) for s in RECORD_STATUSES)
    by_status["MISSING"] = 0
    by_rule = {}
    for idx in range(N_LABELLED):
        if (idx & 65535) == 0:
            guard.poll("labelled-accounting")
        o = owner[idx]
        if o == -1:
            by_status["MISSING"] += 1
            continue
        rec = state.recs[o]
        by_status[rec.status] += 1
        rk = "%s/%s" % (rec.rule, rec.status)
        by_rule[rk] = by_rule.get(rk, 0) + 1
    state.labelled = {"by_status": by_status, "by_rule_status": by_rule}
    state.complete = True


def decide(state):
    if state.pin_mismatch:
        return ST_PIN
    if state.error is not None:
        return ST_ERROR
    if state.file_reasons or any(rec.status == R_FAILED for rec in state.recs):
        return ST_FAIL
    if state.stop is not None:
        return state.stop[0]
    if not state.complete or any(rec.status == R_UNVERIFIED for rec in state.recs):
        return ST_ERROR
    if any(rec.status == R_WRITTEN_SD for rec in state.recs):
        return ST_PASS_SD
    return ST_PASS_ALL


# ---------------------------------------------------------------------------
# Publication (exclusive create, fsync, read-back, COMPLETE marker last)
# ---------------------------------------------------------------------------
def write_exclusive(path, payload):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    try:
        view = memoryview(payload)
        off = 0
        while off < len(payload):
            n = os.write(fd, view[off:])
            if n <= 0:
                raise OSError("short write to %s" % path)
            off += n
        os.fsync(fd)
    finally:
        os.close(fd)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != payload:
        raise OSError("read-back mismatch for %s" % path)
    return hashlib.sha256(payload).hexdigest()


def render_records(state):
    out = ["# %s records: line\tkey\trule\tstatus\torbit\tstabiliser\treasons\n" % CHECKER_ID]
    for rec in state.recs:
        out.append("%d\t%s\t%s\t%s\t%d\t%d\t%s\n" % (
            rec.line, escape_field(rec.raw_key), escape_field(rec.raw_rule), rec.status,
            rec.orbit, rec.stab, ";".join(rec.reasons) if rec.reasons else "-"))
    return "".join(out).encode("ascii")


def record_counts(state):
    by_status = dict((s, 0) for s in RECORD_STATUSES)
    by_rule = {}
    for rec in state.recs:
        by_status[rec.status] += 1
        rk = "%s/%s" % (rec.rule, rec.status)
        by_rule[rk] = by_rule.get(rk, 0) + 1
    return {"total": len(state.recs), "by_status": by_status, "by_rule_status": by_rule}


def publish(state, status, args, started, guard):
    outdir = args["output_dir"]
    failures = []
    for rec in state.recs:
        if rec.status == R_FAILED and len(failures) < MAX_LISTED_FAILURES:
            failures.append({"line": rec.line, "key": escape_field(rec.raw_key),
                             "rule": escape_field(rec.raw_rule), "reasons": rec.reasons,
                             "detail": rec.detail})
    try:
        records_sha = write_exclusive(os.path.join(outdir, "records.tsv"), render_records(state))
        result = {
            "checker": {"id": CHECKER_ID, "source_sha256": state.self_sha,
                        "python": sys.version, "implementation": sys.implementation.name,
                        "optimize_flag": sys.flags.optimize, "argv": sys.argv},
            "input": {"path": args["input"], "expected_sha256": args["expected_sha256"],
                      "observed_sha256": state.input_sha, "bytes": state.input_bytes},
            "status": status,
            "pass_requires": "COMPLETE.json binding this file's sha256 with pass_valid true",
            "sd_scope": "S-D orbit accounted as WRITTEN_SD: excluded by proof-v4 sections 5-6, not checked by this program",
            "stop": state.stop,
            "error": state.error,
            "file_reasons": state.file_reasons,
            "structure": state.structure,
            "coverage": state.coverage,
            "records": record_counts(state),
            "labelled": state.labelled,
            "failures_listed": failures,
            "failures_listed_cap": MAX_LISTED_FAILURES,
            "records_tsv_sha256": records_sha,
            "phases": state.phases,
            "started_epoch": started,
            "deadline_epoch": args["deadline_epoch"],
            "cancel_file": args["cancel_file"],
        }
        payload = (json.dumps(result, indent=1, sort_keys=True) + "\n").encode("ascii")
        result_sha = write_exclusive(os.path.join(outdir, "RESULT.json"), payload)
        late = guard.condition()  # signal/cancel/deadline after the status was decided
        finished = time.time()
        pass_valid = (status in (ST_PASS_SD, ST_PASS_ALL) and late is None and
                      finished < args["deadline_epoch"])
        complete = {"status": status, "pass_valid": pass_valid, "result_json_sha256": result_sha,
                    "records_tsv_sha256": records_sha, "finished_epoch": finished,
                    "deadline_epoch": args["deadline_epoch"], "late_stop_condition": late}
        write_exclusive(os.path.join(outdir, "COMPLETE.json"),
                        (json.dumps(complete, indent=1, sort_keys=True) + "\n").encode("ascii"))
    except Exception as exc:  # any publication defect: no COMPLETE marker, never PASS
        sys.stderr.write("%s publication failed: %r\n" % (CHECKER_ID, exc))
        return EXIT_PUBLICATION
    if status in (ST_PASS_SD, ST_PASS_ALL) and not pass_valid:
        return EXIT_CODE[late[0]] if late is not None else EXIT_CODE[ST_DEADLINE]
    return EXIT_CODE[status]


# ---------------------------------------------------------------------------
# Command line
# ---------------------------------------------------------------------------
HEX64_RE = re.compile(r"[0-9a-f]{64}")
OPTIONS = ("--input", "--expected-sha256", "--output-dir", "--deadline-epoch", "--cancel-file")
REQUIRED = ("--input", "--expected-sha256", "--output-dir", "--deadline-epoch")


def parse_args(argv):
    if len(argv) % 2 != 0:
        return None
    seen = {}
    for i in range(0, len(argv), 2):
        opt, val = argv[i], argv[i + 1]
        if opt not in OPTIONS or opt in seen:
            return None
        seen[opt] = val
    if any(opt not in seen for opt in REQUIRED):
        return None
    if HEX64_RE.fullmatch(seen["--expected-sha256"]) is None:
        return None
    if re.fullmatch(r"[1-9][0-9]{0,11}", seen["--deadline-epoch"]) is None:
        return None
    return {"input": seen["--input"], "expected_sha256": seen["--expected-sha256"],
            "output_dir": seen["--output-dir"], "deadline_epoch": int(seen["--deadline-epoch"]),
            "cancel_file": seen.get("--cancel-file")}


def main(argv):
    args = parse_args(argv)
    if args is None:
        sys.stderr.write(__doc__ or "usage: see the source header\n")
        return EXIT_USAGE
    guard = Guard(args["deadline_epoch"], args["cancel_file"])
    signal.signal(signal.SIGTERM, guard.on_signal)
    signal.signal(signal.SIGINT, guard.on_signal)
    started = time.time()
    try:
        os.mkdir(args["output_dir"], 0o755)
    except FileExistsError:
        sys.stderr.write("%s refusing existing output directory %s\n" % (CHECKER_ID, args["output_dir"]))
        return EXIT_USAGE
    except OSError as exc:
        sys.stderr.write("%s cannot create output directory: %r\n" % (CHECKER_ID, exc))
        return EXIT_PUBLICATION
    state = State()
    try:
        run(state, args, guard)
    except Stop as stop:
        state.stop = [stop.status, stop.detail]
    except Exception:
        state.error = traceback.format_exc()[-4000:]
    status = decide(state)
    if status in (ST_PASS_SD, ST_PASS_ALL):
        try:
            guard.poll("pre-publication")
        except Stop as stop:
            state.stop = [stop.status, stop.detail]
            status = stop.status
    phase(state, "publish")
    return publish(state, status, args, started, guard)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
