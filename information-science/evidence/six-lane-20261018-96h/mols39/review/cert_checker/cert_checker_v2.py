#!/usr/bin/env python3
"""Independent checker for Lemma U certificates (format "lemmaU-cert-v1").
I/O-boundary successor v2, written only by ContinueCFR21: original independent mathematical
logic unchanged byte-for-byte (FORMAT_TAG through compute_facts). New read_capped_input
uses actual same-fd capped reads, O_NONBLOCK/O_NOFOLLOW, regular-file verification and
budget ticks. Error on oversized/growing/FIFO input is ERROR exit2, not a control rejection.
finish checks the deadline before/after publication; a late file is retained but stdout/exit
become ERROR and audit must reject any artifact/stdout mismatch. No snapshots are created.


Written from lemmaU-certificate-format-v1.md alone: checks 0-6 of its
section 4, run in that order (the first failing check is reported), and the
command-line interface of its section 5.  Python standard library only; one
process; no threads, subprocesses or network; exact integer arithmetic mod 3
and mod n.  The "producer" field of the certificate is type-checked only.

Usage:
    python3.14 -I -B cert_checker.py --anchor RAW --anchor-sha256 HEX
        --cert CERT_JSON --out OUT_JSON [--budget-s S]

Exit status: 0 VALID, 1 INVALID, 2 ERROR.
"""

import os
import stat
import hashlib
import json
import math
import sys
import time

FORMAT_TAG = "lemmaU-cert-v1"
CERT_KEYS = frozenset((
    "format", "anchor_sha256", "n", "q", "k", "U", "J", "dim", "basis",
    "free_columns", "rank_witness", "rainbow", "failures", "producer"))
RECORD_KEYS = frozenset(("pivot", "combination"))
PRODUCER_KEYS = frozenset(("name", "sha256"))
OUT_KEYS = (
    "verdict", "first_failed_check", "reason", "cert_sha256", "anchor_sha256",
    "n", "q", "k", "U", "J", "dim", "rank", "rainbow_count",
    "alpha_hat_listed", "minus_alpha_hat_listed", "rainbow_is_pm_alpha_hat",
    "wall_s")
FACT_KEYS = (
    "dim", "rank", "rainbow_count", "alpha_hat_listed",
    "minus_alpha_hat_listed", "rainbow_is_pm_alpha_hat")
EXIT_CODE = {"VALID": 0, "INVALID": 1, "ERROR": 2}
FLAGS = {
    "--anchor": "anchor", "--anchor-sha256": "anchor_sha256",
    "--cert": "cert", "--out": "out", "--budget-s": "budget_s"}
LOWER_HEX = frozenset("0123456789abcdef")
DEFAULT_BUDGET_S = 240.0


class UsageError(Exception):
    """Bad command line: verdict ERROR, exit 2."""


class CheckFailed(Exception):
    """Normative check number `check` failed: verdict INVALID, exit 1."""

    def __init__(self, check, reason):
        super().__init__(reason)
        self.check = check
        self.reason = reason


class BudgetExceeded(Exception):
    """Wall-clock budget exceeded: verdict ERROR, reason "budget", exit 2."""


class Budget:
    """Deadline on time.monotonic(); tick() is called inside the loops."""

    def __init__(self, t0, seconds):
        self.deadline = t0 + seconds

    def expired(self):
        return time.monotonic() > self.deadline

    def tick(self):
        if self.expired():
            raise BudgetExceeded()


def is_int(value):
    """A JSON integer; bool is rejected although it subclasses int."""
    return type(value) is int


def short(value):
    """Bounded repr for reason strings."""
    text = repr(value)
    return text if len(text) <= 80 else text[:77] + "..."


# ------------------------------------------------------------ check 0: format

def reject_constant(name):
    raise ValueError("non-finite constant " + name)


def unique_keys(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("duplicate key " + short(key))
        obj[key] = value
    return obj


def load_certificate(cert_bytes):
    """Check 0, first part: UTF-8 JSON without duplicate keys or NaN/Infinity."""
    try:
        text = cert_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise CheckFailed(0, "certificate is not valid UTF-8") from None
    try:
        return json.loads(text, object_pairs_hook=unique_keys,
                          parse_constant=reject_constant)
    except (ValueError, RecursionError) as exc:
        raise CheckFailed(0, "malformed JSON: " + short(str(exc))) from None


def check0_format(cert, budget):
    """Check 0: keys, types and ranges of section 3; header identities."""
    if type(cert) is not dict:
        raise CheckFailed(0, "top level is not a JSON object")
    missing = sorted(CERT_KEYS - set(cert))
    extra = sorted(set(cert) - CERT_KEYS)
    if missing:
        raise CheckFailed(0, "missing keys " + short(missing))
    if extra:
        raise CheckFailed(0, "extra keys " + short(extra))
    if type(cert["format"]) is not str or cert["format"] != FORMAT_TAG:
        raise CheckFailed(0, "format is not " + FORMAT_TAG)
    sha = cert["anchor_sha256"]
    if type(sha) is not str or len(sha) != 64 or not set(sha) <= LOWER_HEX:
        raise CheckFailed(0, "anchor_sha256 is not 64 lowercase hex digits")
    for key in ("n", "q", "k", "U", "J", "dim"):
        if not is_int(cert[key]):
            raise CheckFailed(0, key + " is not an integer")
    n, q, k = cert["n"], cert["q"], cert["k"]
    U, J, dim = cert["U"], cert["J"], cert["dim"]
    if n % 3 != 0 or q != n // 3:
        raise CheckFailed(0, "q != n/3")
    if q < 1 or q % 3 == 0:
        raise CheckFailed(0, "q = n/3 violates q >= 1 and q % 3 != 0")
    if k < 2:
        raise CheckFailed(0, "k < 2")
    if U != (k - 1) * (n - 1):
        raise CheckFailed(0, "U != (k-1)(n-1)")
    if J != q * (k * (k - 1) // 2):
        raise CheckFailed(0, "J != q*k*(k-1)/2")
    basis = cert["basis"]
    if type(basis) is not list or len(basis) != dim:
        raise CheckFailed(0, "basis is not a list of dim vectors")
    for i, vec in enumerate(basis):
        budget.tick()
        if type(vec) is not list or len(vec) != U:
            raise CheckFailed(0, "basis[%d] is not a list of U entries" % i)
        for a in vec:
            if not is_int(a) or a < 0 or a > 2:
                raise CheckFailed(0, "basis[%d] has an entry not in {0,1,2}" % i)
    free = cert["free_columns"]
    if type(free) is not list or len(free) != dim:
        raise CheckFailed(0, "free_columns is not a list of dim entries")
    for f in free:
        if not is_int(f) or f < 0 or f >= U:
            raise CheckFailed(0, "free_columns has an entry not in [0, U)")
    if len(set(free)) != dim:
        raise CheckFailed(0, "free_columns are not distinct")
    witness = cert["rank_witness"]
    if type(witness) is not list or len(witness) != U - dim:
        raise CheckFailed(0, "rank_witness is not a list of U - dim records")
    for i, rec in enumerate(witness):
        budget.tick()
        if type(rec) is not dict or set(rec) != RECORD_KEYS:
            raise CheckFailed(0, "rank_witness[%d] keys are not pivot, combination" % i)
        pivot = rec["pivot"]
        if not is_int(pivot) or pivot < 0 or pivot >= U:
            raise CheckFailed(0, "rank_witness[%d].pivot is not in [0, U)" % i)
        comb = rec["combination"]
        if type(comb) is not list:
            raise CheckFailed(0, "rank_witness[%d].combination is not a list" % i)
        last = -1
        for term in comb:
            if type(term) is not list or len(term) != 2:
                raise CheckFailed(0, "rank_witness[%d]: a term is not [j, coef]" % i)
            j, coef = term
            if not is_int(j) or j <= last or j >= J:
                raise CheckFailed(0, "rank_witness[%d]: j not strictly increasing in [0, J)" % i)
            if not is_int(coef) or coef not in (1, 2):
                raise CheckFailed(0, "rank_witness[%d]: coef not in {1,2}" % i)
            last = j
    total = 3 ** dim                    # dim = len(basis) <= U: bounded by the file
    rainbow = cert["rainbow"]
    if type(rainbow) is not list:
        raise CheckFailed(0, "rainbow is not a list")
    last = -1
    for idx in rainbow:
        budget.tick()
        if not is_int(idx) or idx <= last or idx >= total:
            raise CheckFailed(0, "rainbow is not strictly increasing in [0, 3^dim)")
        last = idx
    failures = cert["failures"]
    if type(failures) is not list:
        raise CheckFailed(0, "failures is not a list")
    last = -1
    for item in failures:
        budget.tick()
        if type(item) is not list or len(item) != 2:
            raise CheckFailed(0, "failures: an entry is not [idx, j]")
        idx, j = item
        if not is_int(idx) or idx <= last or idx >= total:
            raise CheckFailed(0, "failures: idx not strictly increasing in [0, 3^dim)")
        if not is_int(j) or j < 0 or j >= J:
            raise CheckFailed(0, "failures: j not in [0, J)")
        last = idx
    producer = cert["producer"]
    if type(producer) is not dict or set(producer) != PRODUCER_KEYS:
        raise CheckFailed(0, "producer keys are not name, sha256")
    if type(producer["name"]) is not str or type(producer["sha256"]) is not str:
        raise CheckFailed(0, "producer name or sha256 is not a string")
    return {"anchor_sha256": sha, "n": n, "q": q, "k": k, "U": U, "J": J,
            "basis": basis, "free": free, "witness": witness,
            "rainbow": rainbow, "failures": failures}


# ------------------------------------------------------------ check 1: anchor

def parse_anchor(raw_bytes, budget):
    """Section 1: non-empty lines of whitespace-separated decimal integers."""
    lines = raw_bytes.split(b"\n")
    if lines[-1] == b"":
        lines.pop()                     # terminator of the last line
    rows = []
    for number, line in enumerate(lines):
        budget.tick()
        tokens = line.split()           # ASCII whitespace (also drops a CR)
        if not tokens:
            raise CheckFailed(1, "anchor line %d is empty" % number)
        row = []
        for tok in tokens:
            digits = tok[1:] if tok[:1] in (b"+", b"-") else tok
            if not digits.isdigit():    # bytes.isdigit: ASCII 0-9 only, non-empty
                raise CheckFailed(1, "anchor line %d: token is not a decimal integer" % number)
            try:
                row.append(int(tok))
            except ValueError:
                raise CheckFailed(1, "anchor line %d: integer too long" % number) from None
        rows.append(row)
    return rows


def check1_anchor(raw_bytes, raw_sha, cli_sha, hdr, budget):
    """Check 1: anchor hash, shape, difference-matrix property, fibre sizes."""
    if raw_sha != cli_sha:
        raise CheckFailed(1, "sha256 of the anchor bytes != --anchor-sha256")
    if raw_sha != hdr["anchor_sha256"]:
        raise CheckFailed(1, "sha256 of the anchor bytes != certificate anchor_sha256")
    rows = parse_anchor(raw_bytes, budget)
    if len(rows) != hdr["k"]:
        raise CheckFailed(1, "anchor has %d rows, certificate k = %s"
                          % (len(rows), short(hdr["k"])))
    for x, row in enumerate(rows):
        if len(row) != hdr["n"]:
            raise CheckFailed(1, "anchor row %d has %d integers, certificate n = %s"
                              % (x, len(row), short(hdr["n"])))
    # Section 2 objects, computed from the raw file only.
    k = len(rows)
    n = len(rows[0])
    q = n // 3
    U = (k - 1) * (n - 1)
    pairs = [(x, y) for x in range(k) for y in range(x + 1, k)]
    J = len(pairs) * q
    if n % 3 != 0 or q != hdr["q"] or U != hdr["U"] or J != hdr["J"]:
        raise CheckFailed(1, "q, U or J of the anchor differ from the certificate")
    D = [[value % n for value in row] for row in rows]
    for x, y in pairs:
        budget.tick()
        if len({(D[x][c] - D[y][c]) % n for c in range(n)}) != n:
            raise CheckFailed(1, "D is not a difference matrix (rows %d, %d)" % (x, y))
    E = [[(D[x][c] - D[0][c]) % n for c in range(n)] for x in range(k)]
    B = [[E[x][c] % q for c in range(n)] for x in range(k)]
    T = [[E[x][c] % 3 for c in range(n)] for x in range(k)]
    fibres = []                         # fibres[p*q + t] = (x, y, columns)
    for p, (x, y) in enumerate(pairs):
        budget.tick()
        buckets = [[] for _ in range(q)]
        for c in range(n):
            buckets[(B[x][c] - B[y][c]) % q].append(c)
        for t in range(q):
            if len(buckets[t]) != 3:
                raise CheckFailed(1, "fibre (p=%d, t=%d) has %d columns, not 3"
                                  % (p, t, len(buckets[t])))
            fibres.append((x, y, buckets[t]))
    return {"n": n, "q": q, "k": k, "U": U, "J": J, "T": T, "fibres": fibres}


# ------------------------------------- section 2: indexing, equations, points

def var_index(n, x, c):
    """v(x, c) = (x-1)*(n-1) + (c-1) for x = 1..k-1 and c = 1..n-1."""
    return (x - 1) * (n - 1) + (c - 1)


def entry(A, n, x, c):
    """A[x][c] of a point A in F_3^U read as the k x n array with fixed zeros."""
    if x == 0 or c == 0:
        return 0
    return A[var_index(n, x, c)]


def build_equations(der):
    """e_j for j = 0..J-1 as sorted sparse lists of (v, w) with w in {1, 2}."""
    n = der["n"]
    equations = []
    for x, y, cols in der["fibres"]:
        e = {}
        for c in cols:
            if c >= 1:
                if x >= 1:
                    v = var_index(n, x, c)
                    e[v] = (e.get(v, 0) + 1) % 3
                v = var_index(n, y, c)
                e[v] = (e.get(v, 0) + 2) % 3
        equations.append(sorted((v, w) for v, w in e.items() if w != 0))
    return equations


def point(idx, basis, U):
    """point(z) = sum over r of z[r]*basis[r] (mod 3), z = the dim base-3
    digits of idx with z[0] most significant (idx(z) of section 2)."""
    dim = len(basis)
    z = [0] * dim
    rest = idx
    for r in range(dim - 1, -1, -1):
        z[r] = rest % 3
        rest //= 3
    A = [0] * U
    for r in range(dim):
        zr = z[r]
        if zr:
            A = [a + zr * b for a, b in zip(A, basis[r])]
    return [a % 3 for a in A]


def fibre_values(A, n, fibre):
    """The values (A[x][c] - A[y][c]) mod 3 over the columns of the fibre."""
    x, y, cols = fibre
    return [(entry(A, n, x, c) - entry(A, n, y, c)) % 3 for c in cols]


def pairwise_distinct(values):
    a, b, c = values
    return a != b and a != c and b != c


# --------------------------------------------------------- check 2: solutions

def check2_solutions(equations, basis, budget):
    """Check 2: e_j . basis[i] = 0 (mod 3) for every j and every i."""
    for i, b in enumerate(basis):
        budget.tick()
        for j, e in enumerate(equations):
            if sum(w * b[v] for v, w in e) % 3 != 0:
                raise CheckFailed(2, "e_%d . basis[%d] != 0 (mod 3)" % (j, i))


# ------------------------------------------------ check 3: free-column identity

def check3_identity(basis, free, budget):
    """Check 3: basis[i][free_columns[r]] == (1 if i == r else 0)."""
    for i, b in enumerate(basis):
        budget.tick()
        for r, f in enumerate(free):
            want = 1 if i == r else 0
            if b[f] != want:
                raise CheckFailed(3, "basis[%d][free_columns[%d]] != %d" % (i, r, want))


# ------------------------------------------------------ check 4: rank witness

def check4_rank(equations, witness, free, U, budget):
    """Check 4: distinct non-free pivots; R_i[pivot_i] = 1 and R_i[pivot_m] = 0
    for every other record m, with R_i = sum of coef * e_j (mod 3)."""
    pivots = [rec["pivot"] for rec in witness]
    if len(set(pivots)) != len(pivots):
        raise CheckFailed(4, "pivots are not pairwise distinct")
    free_set = set(free)
    for i, pivot in enumerate(pivots):
        if pivot in free_set:
            raise CheckFailed(4, "pivot of record %d is a free column" % i)
    for i, rec in enumerate(witness):
        budget.tick()
        R = [0] * U
        for j, coef in rec["combination"]:
            for v, w in equations[j]:
                R[v] = (R[v] + coef * w) % 3
        if R[pivots[i]] != 1:
            raise CheckFailed(4, "R_%d[pivot_%d] != 1" % (i, i))
        for m, pivot in enumerate(pivots):
            if m != i and R[pivot] != 0:
                raise CheckFailed(4, "R_%d[pivot_%d] != 0" % (i, m))


# ------------------------------------------------------ check 5: rainbow list

def check5_rainbow(rainbow, basis, der, budget):
    """Check 5: point(idx) is rainbow for every listed idx."""
    for idx in rainbow:
        budget.tick()
        A = point(idx, basis, der["U"])
        for j, fibre in enumerate(der["fibres"]):
            if not pairwise_distinct(fibre_values(A, der["n"], fibre)):
                raise CheckFailed(5, "listed point %d is not rainbow (fibre %d)" % (idx, j))


# ------------------------------------------- check 6: failures and coverage

def check6_coverage(rainbow, failures, basis, der, budget):
    """Check 6: rainbow and failure indices are disjoint and together exactly
    {0, ..., 3^dim - 1}; fibre j of point(idx) really fails for each failure."""
    total = 3 ** len(basis)
    failure_idx = [idx for idx, _ in failures]
    rainbow_set = set(rainbow)
    failure_set = set(failure_idx)
    if len(rainbow_set) != len(rainbow) or len(failure_set) != len(failure_idx):
        raise CheckFailed(6, "duplicate point index")
    if rainbow_set & failure_set:
        raise CheckFailed(6, "rainbow and failure indices are not disjoint")
    if len(rainbow) + len(failure_idx) != total:
        raise CheckFailed(6, "%d indices listed, 3^dim needed (dim = %d)"
                          % (len(rainbow) + len(failure_idx), len(basis)))
    budget.tick()
    if (rainbow_set | failure_set) != set(range(total)):
        raise CheckFailed(6, "indices are not exactly {0, ..., 3^dim - 1}")
    for idx, j in failures:
        budget.tick()
        A = point(idx, basis, der["U"])
        if pairwise_distinct(fibre_values(A, der["n"], der["fibres"][j])):
            raise CheckFailed(6, "failure [%d, %d]: the fibre carries three distinct values"
                              % (idx, j))


# ------------------------------------------------------------------- facts

def compute_facts(der, basis, rainbow, budget):
    """Facts of section 4 (reported only when VALID)."""
    n, k, U, T = der["n"], der["k"], der["U"], der["T"]
    alpha_hat = [0] * U
    for x in range(1, k):
        for c in range(1, n):
            alpha_hat[var_index(n, x, c)] = (T[x][c] - T[x][0]) % 3
    minus_alpha_hat = [(3 - a) % 3 for a in alpha_hat]
    plus_listed = False
    minus_listed = False
    for idx in rainbow:
        budget.tick()
        A = point(idx, basis, U)
        plus_listed = plus_listed or A == alpha_hat
        minus_listed = minus_listed or A == minus_alpha_hat
    dim = len(basis)
    count = len(rainbow)
    return {
        "dim": dim,
        "rank": U - dim,
        "rainbow_count": count,
        "alpha_hat_listed": plus_listed,
        "minus_alpha_hat_listed": minus_listed,
        "rainbow_is_pm_alpha_hat": (count == 2 and plus_listed and minus_listed
                                    and alpha_hat != minus_alpha_hat),
    }


# ---------------------------------------------------------------- interface

def parse_args(argv):
    """Section 5 command line; "--flag value" or "--flag=value"."""
    got = {}
    i = 0
    while i < len(argv):
        flag, sep, value = argv[i].partition("=")
        if flag not in FLAGS:
            raise UsageError("unknown argument " + short(argv[i]))
        if not sep:
            if i + 1 >= len(argv):
                raise UsageError("missing value for " + flag)
            i += 1
            value = argv[i]
        i += 1
        if FLAGS[flag] in got:
            raise UsageError("repeated " + flag)
        got[FLAGS[flag]] = value
    for flag in ("--anchor", "--anchor-sha256", "--cert", "--out"):
        if FLAGS[flag] not in got:
            raise UsageError("missing " + flag)
    budget_s = DEFAULT_BUDGET_S
    if "budget_s" in got:
        try:
            budget_s = float(got["budget_s"])
        except ValueError:
            raise UsageError("--budget-s is not a number") from None
        if not (math.isfinite(budget_s) and budget_s > 0):
            raise UsageError("--budget-s must be positive and finite")
    return got, budget_s


def null_result():
    return {key: None for key in OUT_KEYS}


def set_error(res, reason):
    res["verdict"] = "ERROR"
    res["first_failed_check"] = None
    res["reason"] = reason
    for key in FACT_KEYS:
        res[key] = None


def read_capped_input(path, cap, budget):
    """I/O boundary only: nonblocking open rejects FIFOs before any read; same-fd cap+1 read.
    Growth after fstat is bounded by bytes actually consumed, not pathname metadata.
    No snapshot or extra retained file is created. Errors are ERROR, never INVALID.
    """
    budget.tick()
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise OSError("input is not a regular file")
        if info.st_size > cap:
            raise OSError("input exceeds size cap")
        chunks = []
        total = 0
        while True:
            budget.tick()
            block = os.read(fd, min(65536, cap + 1 - total))
            budget.tick()
            if not block:
                break
            total += len(block)
            if total > cap:
                raise OSError("input grew beyond size cap")
            chunks.append(block)
        budget.tick()
        return b"".join(chunks)
    finally:
        os.close(fd)


def run_checks(args, budget_s, t0, res):
    """Read both inputs, then run checks 0-6 in order; the first failure wins."""
    budget = Budget(t0, budget_s)
    try:
        raw_bytes = read_capped_input(args["anchor"], 1 << 20, budget)
        res["anchor_sha256"] = hashlib.sha256(raw_bytes).hexdigest()
        cert_bytes = read_capped_input(args["cert"], 8 << 20, budget)
        res["cert_sha256"] = hashlib.sha256(cert_bytes).hexdigest()
    except BudgetExceeded:
        set_error(res, "budget")
        return
    except OSError as exc:
        set_error(res, "cannot read bounded input: " + type(exc).__name__)
        return
    try:
        cert = load_certificate(cert_bytes)                           # check 0
        hdr = check0_format(cert, budget)                             # check 0
        der = check1_anchor(raw_bytes, res["anchor_sha256"],
                            args["anchor_sha256"], hdr, budget)       # check 1
        for key in ("n", "q", "k", "U", "J"):
            res[key] = der[key]
        equations = build_equations(der)
        check2_solutions(equations, hdr["basis"], budget)             # check 2
        check3_identity(hdr["basis"], hdr["free"], budget)            # check 3
        check4_rank(equations, hdr["witness"], hdr["free"], der["U"],
                    budget)                                           # check 4
        check5_rainbow(hdr["rainbow"], hdr["basis"], der, budget)     # check 5
        check6_coverage(hdr["rainbow"], hdr["failures"], hdr["basis"], der,
                        budget)                                       # check 6
        facts = compute_facts(der, hdr["basis"], hdr["rainbow"], budget)
    except CheckFailed as exc:
        res["verdict"] = "INVALID"
        res["first_failed_check"] = exc.check
        res["reason"] = "check %d: %s" % (exc.check, exc.reason)
    except BudgetExceeded:
        set_error(res, "budget")
        return
    else:
        res["verdict"] = "VALID"
        res["first_failed_check"] = None
        res["reason"] = "checks 0-6 passed"
        res.update(facts)
    if budget.expired():                # never VALID (nor INVALID) past the budget
        set_error(res, "budget")


def finish(res, t0, out_file, deadline=None):
    """Write the object to OUT_JSON (when reserved) and print it as one line."""
    if res["verdict"] not in EXIT_CODE:
        set_error(res, "internal error: no verdict")
    if deadline is not None and time.monotonic() > deadline:
        set_error(res, "budget before publication")
    res["wall_s"] = round(time.monotonic() - t0, 3)
    line = json.dumps(res, separators=(",", ":"))
    if out_file is not None:
        try:
            out_file.write(line + "\n")
            out_file.close()
        except OSError as exc:
            set_error(res, "cannot write output file: " + type(exc).__name__)
            res["wall_s"] = round(time.monotonic() - t0, 3)
            line = json.dumps(res, separators=(",", ":"))
    if deadline is not None and time.monotonic() > deadline:
        # The exclusive artifact is preserved; stdout/exit become ERROR, so parent audit must reject.
        set_error(res, "budget after publication")
        res["wall_s"] = round(time.monotonic() - t0, 3)
        line = json.dumps(res, separators=(",", ":"))
    try:
        print(line, flush=True)
    except OSError:
        return EXIT_CODE["ERROR"]
    return EXIT_CODE[res["verdict"]]


def main(argv):
    t0 = time.monotonic()
    res = null_result()
    try:
        args, budget_s = parse_args(argv)
    except UsageError as exc:
        set_error(res, "bad arguments: " + str(exc))
        return finish(res, t0, None)
    try:
        out_file = open(args["out"], "x", encoding="utf-8")       # reserve OUT_JSON
    except FileExistsError:
        set_error(res, "output file already exists")
        return finish(res, t0, None)
    except OSError as exc:
        set_error(res, "cannot create output file: " + type(exc).__name__)
        return finish(res, t0, None)
    try:
        run_checks(args, budget_s, t0, res)
    except Exception as exc:            # checker defect or resource failure: never VALID
        set_error(res, "internal error: " + type(exc).__name__)
    return finish(res, t0, out_file, deadline=t0 + budget_s)


if __name__ == "__main__":
    try:
        STATUS = main(sys.argv[1:])
    except BaseException:               # last resort: never exit 0 or 1 by accident
        STATUS = EXIT_CODE["ERROR"]
    sys.exit(STATUS)
