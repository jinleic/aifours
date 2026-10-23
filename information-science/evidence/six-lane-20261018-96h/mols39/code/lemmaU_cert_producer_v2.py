#!/usr/bin/env python3
"""lemmaU_cert_producer_v2.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only).

Successor of lemmaU_cert_producer_v1.py (sha256 52b8218e8a3f5fccc719d8c2b1c17a886f0cdaee67bebebe54f2a3f4dd00b8eb,
never executed). Contract: evidence/lemmaU-certificate-format-v2.md, sections 1, 2, 3 and 5A. Run only through
code/go_entry_producer_v2.py, which pins this file, verifies the job root and makes it the working directory.
Changes from v1 (review ea5f29a7..., findings M3, M5, m1):
  - raw grammar G1, exactly as the accepted checker parses it (M5);
  - finite positive budget 0 < S <= 280, cooperative deadline checks in every substantial loop, a deadline check
    before each publication step; work limits k <= 12, n <= 120, dim <= 8; input cap 1 MiB (M3);
  - every failure path, including I/O errors and unexpected exceptions, ends in a structured status and exit code
    (m1);
  - fixed outputs cert.json and result.json in the working directory, exclusive create, result.json last.
Method (unchanged from v1): build the J fibre-sum equations over the U gauged unknowns; run Gauss-Jordan elimination
over F_3, tracking every working row as a combination of the original equations; take the nullspace basis from the
free columns; test all 3^dim points for the rainbow property, recording the smallest failing fibre of every
non-rainbow point. Internal self-checks (not a substitute for the independent checker): the basis solves every
equation; every witness row recomputed from its combination reproduces the reduced row and the pivot pattern; and
alpha_hat and minus_alpha_hat are listed rainbow points."""
import sys, os, json, time, math, hashlib

FORMAT = "lemmaU-cert-v1"
RAW_CAP = 1 << 20
CERT_CAP = 8 << 20
MAX_BUDGET_S = 280.0
DEFAULT_BUDGET_S = 240.0
MAX_K, MAX_N, MAX_DIM = 12, 120, 8
EXIT = {"OK": 0, "BAD_INPUT": 2, "INPUT_PIN_MISMATCH": 2, "IO_ERROR": 2, "NOT_DM": 3, "FIBRE_SIZE": 3,
        "SELF_CHECK": 4, "INTERNAL_ERROR": 4, "BUDGET_EXCEEDED": 5, "WORK_LIMIT": 6}
RESULT_KEYS = ("status", "reason", "n", "q", "k", "U", "J", "rank", "dim", "rainbow_count", "alpha_hat_idx",
               "minus_alpha_hat_idx", "cert_sha256", "anchor_sha256", "producer_sha256", "wall_s")
FLAGS = ("--anchor", "--anchor-sha256", "--budget-s")


class Stop(Exception):
    def __init__(self, status, reason):
        super().__init__(reason)
        self.status, self.reason = status, reason


class Budget:
    def __init__(self, t0, seconds):
        self.deadline = t0 + seconds

    def tick(self):
        if time.monotonic() > self.deadline:
            raise Stop("BUDGET_EXCEEDED", "self budget exceeded")


def parse_args(argv):
    got = {}
    if len(argv) % 2:
        raise Stop("BAD_INPUT", "arguments must be --flag value pairs")
    for i in range(0, len(argv), 2):
        flag, value = argv[i], argv[i + 1]
        if flag not in FLAGS:
            raise Stop("BAD_INPUT", "unknown flag")
        if flag in got:
            raise Stop("BAD_INPUT", "repeated flag")
        got[flag] = value
    for flag in ("--anchor", "--anchor-sha256"):
        if flag not in got:
            raise Stop("BAD_INPUT", "missing " + flag)
    budget_s = DEFAULT_BUDGET_S
    if "--budget-s" in got:
        try:
            budget_s = float(got["--budget-s"])
        except ValueError:
            raise Stop("BAD_INPUT", "--budget-s is not a number") from None
    if not (math.isfinite(budget_s) and 0.0 < budget_s <= MAX_BUDGET_S):
        raise Stop("BAD_INPUT", "--budget-s must be finite with 0 < S <= 280")
    return got["--anchor"], got["--anchor-sha256"], budget_s


def parse_g1(raw, budget):
    """Grammar G1 (format v2 section 1); returns the list of rows of Python ints."""
    lines = raw.split(b"\n")
    if lines[-1] == b"":
        lines.pop()
    rows = []
    for line in lines:
        budget.tick()
        tokens = line.split()
        if not tokens:
            raise Stop("BAD_INPUT", "G1: a line has no token")
        row = []
        for tok in tokens:
            digits = tok[1:] if tok[:1] in (b"+", b"-") else tok
            if not digits.isdigit():
                raise Stop("BAD_INPUT", "G1: a token is not a decimal integer")
            try:
                row.append(int(tok))
            except ValueError:
                raise Stop("BAD_INPUT", "G1: integer too long") from None
        rows.append(row)
    return rows


def write_new(name, data):
    """Exclusive create of a plain file name in the working directory (the verified job root)."""
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        view = memoryview(data)
        while view:
            written = os.write(fd, view)
            view = view[written:]
    finally:
        os.close(fd)


def produce(anchor_path, anchor_pin, budget, summary):
    try:
        with open(anchor_path, "rb") as fh:
            raw = fh.read(RAW_CAP + 1)
    except OSError as exc:
        raise Stop("IO_ERROR", "cannot read anchor: " + type(exc).__name__) from None
    if len(raw) > RAW_CAP:
        raise Stop("BAD_INPUT", "anchor exceeds 1 MiB")
    h = hashlib.sha256(raw).hexdigest()
    summary["anchor_sha256"] = h
    if h != anchor_pin:
        raise Stop("INPUT_PIN_MISMATCH", "anchor sha256 differs from --anchor-sha256")
    rows = parse_g1(raw, budget)
    k = len(rows)
    n = len(rows[0]) if rows else 0
    if k < 2 or n < 3 or any(len(r) != n for r in rows):
        raise Stop("BAD_INPUT", "anchor must have k >= 2 rows of one length n >= 3")
    if k > MAX_K or n > MAX_N:
        raise Stop("WORK_LIMIT", "k or n beyond the work limits")
    q = n // 3
    if n % 3 != 0 or q % 3 == 0:
        raise Stop("BAD_INPUT", "n must be 3q with q % 3 != 0")
    summary.update({"n": n, "q": q, "k": k})
    D = [[v % n for v in r] for r in rows]
    for x in range(k):
        for y in range(x + 1, k):
            budget.tick()
            if len({(D[x][c] - D[y][c]) % n for c in range(n)}) != n:
                raise Stop("NOT_DM", "rows %d, %d: differences are not a bijection" % (x, y))
    E = [[(D[x][c] - D[0][c]) % n for c in range(n)] for x in range(k)]
    Bq = [[v % q for v in r] for r in E]
    T3 = [[v % 3 for v in r] for r in E]
    pairs = [(x, y) for x in range(k) for y in range(x + 1, k)]
    U = (k - 1) * (n - 1)
    J = len(pairs) * q
    summary.update({"U": U, "J": J})

    def var(x, c):
        return None if (x == 0 or c == 0) else (x - 1) * (n - 1) + (c - 1)

    fibres = []
    for (x, y) in pairs:
        budget.tick()
        buckets = [[] for _ in range(q)]
        for c in range(n):
            buckets[(Bq[x][c] - Bq[y][c]) % q].append(c)
        for t in range(q):
            if len(buckets[t]) != 3:
                raise Stop("FIBRE_SIZE", "pair (%d,%d) fibre %d has %d columns" % (x, y, t, len(buckets[t])))
            fibres.append((x, y, buckets[t]))
    eqs = []
    for (x, y, cols) in fibres:
        budget.tick()
        e = [0] * U
        for c in cols:
            vx, vy = var(x, c), var(y, c)
            if vx is not None:
                e[vx] = (e[vx] + 1) % 3
            if vy is not None:
                e[vy] = (e[vy] + 2) % 3
        eqs.append(e)
    # Gauss-Jordan over F_3 with combination tracking
    work = [list(e) for e in eqs]
    combs = [{j: 1} for j in range(J)]
    pivots = []
    r = 0
    for col in range(U):
        budget.tick()
        if r == J:
            break
        piv = None
        for i in range(r, J):
            if work[i][col]:
                piv = i
                break
        if piv is None:
            continue
        work[r], work[piv] = work[piv], work[r]
        combs[r], combs[piv] = combs[piv], combs[r]
        if work[r][col] == 2:                        # 2 * 2 = 4 = 1 (mod 3)
            work[r] = [(v * 2) % 3 for v in work[r]]
            combs[r] = {j: (cf * 2) % 3 for j, cf in combs[r].items()}
        wr, cr = work[r], combs[r]
        for i in range(J):
            if (i & 63) == 0:
                budget.tick()
            if i != r and work[i][col]:
                f = work[i][col]
                work[i] = [(vi - f * vr) % 3 for vi, vr in zip(work[i], wr)]
                ci = combs[i]
                for j, cf in cr.items():
                    nv = (ci.get(j, 0) - f * cf) % 3
                    if nv:
                        ci[j] = nv
                    else:
                        ci.pop(j, None)
        pivots.append(col)
        r += 1
    rank = r
    pivset = set(pivots)
    free = [col for col in range(U) if col not in pivset]
    dim = U - rank
    if len(free) != dim:
        raise Stop("SELF_CHECK", "free column count mismatch")
    summary.update({"rank": rank, "dim": dim})
    if dim > MAX_DIM:
        raise Stop("WORK_LIMIT", "dim beyond the work limit")
    basis = []
    for fcol in free:
        budget.tick()
        b = [0] * U
        b[fcol] = 1
        for i, p in enumerate(pivots):
            b[p] = (-work[i][fcol]) % 3
        basis.append(b)
    for b in basis:
        for j, e in enumerate(eqs):
            if (j & 63) == 0:
                budget.tick()
            if sum(ev * bv for ev, bv in zip(e, b)) % 3:
                raise Stop("SELF_CHECK", "a basis vector fails an equation")
    witness = []
    for i in range(rank):
        budget.tick()
        R = [0] * U
        for j, cf in combs[i].items():
            ej = eqs[j]
            R = [(rv + cf * ev) % 3 for rv, ev in zip(R, ej)]
        if R != work[i]:
            raise Stop("SELF_CHECK", "combination does not reproduce reduced row %d" % i)
        for m, p in enumerate(pivots):
            if R[p] != (1 if m == i else 0):
                raise Stop("SELF_CHECK", "pivot pattern broken in row %d" % i)
        witness.append({"pivot": pivots[i], "combination": [[j, cf] for j, cf in sorted(combs[i].items()) if cf % 3]})
    fib_idx = [(x, y, [(var(x, c), var(y, c)) for c in cols]) for (x, y, cols) in fibres]

    def first_bad_fibre(A):
        for j, (x, y, cv) in enumerate(fib_idx):
            vals = set()
            for (vx, vy) in cv:
                ax = 0 if vx is None else A[vx]
                ay = 0 if vy is None else A[vy]
                vals.add((ax - ay) % 3)
            if len(vals) != 3:
                return j
        return None

    def point(z):
        A = [0] * U
        for zr, b in zip(z, basis):
            if zr:
                A = [(av + zr * bv) % 3 for av, bv in zip(A, b)]
        return A

    rainbow, failures = [], []
    for idx in range(3 ** dim):
        budget.tick()
        z, rem = [], idx
        for _ in range(dim):
            z.append(rem % 3)
            rem //= 3
        z.reverse()                                  # z[0] most significant
        j = first_bad_fibre(point(z))
        if j is None:
            rainbow.append(idx)
        else:
            failures.append([idx, j])
    ah = [0] * U
    for x in range(1, k):
        for c in range(1, n):
            ah[var(x, c)] = (T3[x][c] - T3[x][0]) % 3
    mah = [(3 - v) % 3 for v in ah]

    def index_of(vec):
        z = [vec[f] for f in free]
        if point(z) != vec:
            return None
        idx = 0
        for zr in z:
            idx = idx * 3 + zr
        return idx

    budget.tick()
    ia, ima = index_of(ah), index_of(mah)
    if ia is None or ima is None or ia not in rainbow or ima not in rainbow:
        raise Stop("SELF_CHECK", "alpha_hat or minus_alpha_hat is not a listed rainbow point")
    summary.update({"rainbow_count": len(rainbow), "alpha_hat_idx": ia, "minus_alpha_hat_idx": ima})
    own_sha = summary["producer_sha256"]
    cert = {"format": FORMAT, "anchor_sha256": h, "n": n, "q": q, "k": k, "U": U, "J": J, "dim": dim,
            "basis": basis, "free_columns": free, "rank_witness": witness, "rainbow": rainbow,
            "failures": failures, "producer": {"name": "lemmaU_cert_producer_v2.py", "sha256": own_sha or ""}}
    budget.tick()
    data = (json.dumps(cert, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    if len(data) > CERT_CAP:
        raise Stop("WORK_LIMIT", "certificate exceeds 8 MiB")
    budget.tick()                                    # deadline check before publication
    try:
        write_new("cert.json", data)
    except OSError as exc:
        raise Stop("IO_ERROR", "cannot write cert.json: " + type(exc).__name__) from None
    summary["cert_sha256"] = hashlib.sha256(data).hexdigest()


def main(argv):
    t0 = time.monotonic()
    summary = {key: None for key in RESULT_KEYS}
    try:
        with open(os.path.abspath(__file__), "rb") as fh:
            summary["producer_sha256"] = hashlib.sha256(fh.read()).hexdigest()   # informational only
    except (OSError, NameError):
        summary["producer_sha256"] = None
    status, reason = "OK", None
    try:
        anchor_path, anchor_pin, budget_s = parse_args(argv)
        budget = Budget(t0, budget_s)
        produce(anchor_path, anchor_pin, budget, summary)
        budget.tick()                                # deadline check before reporting OK
    except Stop as s:
        status, reason = s.status, s.reason
    except MemoryError:
        status, reason = "INTERNAL_ERROR", "MemoryError"
    except Exception as exc:
        status, reason = "INTERNAL_ERROR", type(exc).__name__
    summary["status"], summary["reason"] = status, reason
    summary["wall_s"] = round(time.monotonic() - t0, 3)
    line = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    try:
        write_new("result.json", (line + "\n").encode("ascii"))
    except OSError as exc:
        summary["status"], summary["reason"] = "IO_ERROR", "cannot write result.json: " + type(exc).__name__
        line = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    try:
        print(line, flush=True)
    except OSError:
        return EXIT["IO_ERROR"]
    return EXIT[summary["status"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
