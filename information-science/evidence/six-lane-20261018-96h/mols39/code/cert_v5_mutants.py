# PACKAGE v5 I/O repair: no informational __file__ read; wrapper-injected verified digest.
# After final stdout completion, late budget => exit5 with already emitted bytes preserved.
#!/usr/bin/env python3
"""CERTIFICATE PACKAGE v4: actual capped descriptor reads; budget before/after EACH retained publication.
Source-only. Scientific mutation definitions nc0..10 unchanged; parent review7b07cf45 findings2/3.
cert_v5_mutants.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only).

Preregistered negative and positive controls for the independent Lemma U certificate checker. Successor of
make_cert_mutants_v2.py (sha256 35d08e6e093febf0c298a2b6c5decee3ce149806b3a2eba388dc1549ff8e2f24, never executed).
Contract: evidence/lemmaU-certificate-format-v2.md, sections 1-3 and 5C. Run only through
code/cert_v5_entry_mutants.py, which pins this file, verifies the job root and makes it the working directory.
Imports neither the producer nor the checker.
Changes from v2 (review ea5f29a7..., findings m3, M3, M4, M5, m1):
  - new control nc10_basis_scale, aimed at check 3 (m3);
  - every output is a plain name created exclusively in the working directory; there is no --outdir argument (M4);
  - the anchor is parsed with grammar G1 (M5); the source certificate is parsed strictly (duplicate keys, NaN,
    Infinity and non-finite floats are rejected) and must be in canonical bytes;
  - finite positive budget 0 < S <= 280 with cooperative deadline checks and a check before publication (M3);
  - structured statuses for every failure, including I/O errors (m1);
  - the manifest records, per mutant, integer details that let the expectations program re-derive the exact
    mutation independently.
Mutants (S = source certificate). Intended verdict and first failing check of the accepted checker in brackets:
  nc0_identity            unchanged copy (same bytes)                                        [VALID]
  nc1_basis_flip          basis[0][p] += 1 (mod 3) with p = S.rank_witness[0].pivot           [INVALID 2]
  nc2_pivot_swap          swap the pivots of witness records 0 and 1                          [INVALID 4]
  nc3_rainbow_swap        r0 = S.rainbow[0] moves to failures as [r0, 0];
                          f0 = S.failures[0][0] moves to rainbow                              [INVALID 5]
  nc4_failure_delete      delete S.failures[0]                                                [INVALID 6]
  nc5_wrong_anchor_hash   anchor_sha256 := --other-sha256                                     [INVALID 1]
  nc6_failure_wrong_fibre first failure entry whose point has a passing fibre:
                          its fibre := the smallest passing fibre                             [INVALID 6]
  nc7_witness_coef        witness record 0, first combination term: coefficient c -> 3 - c   [INVALID 4]
  nc8_witness_drop        delete the last witness record                                      [INVALID 0]
  nc9_anchor_mutation     anchor_sha256 := --mut-anchor-sha256 (checked with that raw)        [INVALID 1]
  nc10_basis_scale        basis[0] := 2 * basis[0] (mod 3)                                    [INVALID 3]
CLI: --cert CERT --cert-sha256 HEX --anchor RAW --anchor-sha256 HEX --other-sha256 HEX --mut-anchor-sha256 HEX
     [--budget-s S]       ("--flag value" pairs only; each flag at most once)
Exit codes: 0 OK; 2 BAD_INPUT / INPUT_PIN_MISMATCH / IO_ERROR; 4 INTERNAL_ERROR; 5 BUDGET_EXCEEDED.
One JSON line is printed, and the same bytes plus a newline are written to result.json (last)."""
import sys, os, json, copy, math, time, hashlib, stat

RAW_CAP = 1 << 20
CERT_CAP = 8 << 20
MAX_BUDGET_S = 280.0
DEFAULT_BUDGET_S = 240.0
EXIT = {"OK": 0, "BAD_INPUT": 2, "INPUT_PIN_MISMATCH": 2, "IO_ERROR": 2, "INTERNAL_ERROR": 4, "BUDGET_EXCEEDED": 5}
FLAGS = ("--cert", "--cert-sha256", "--anchor", "--anchor-sha256", "--other-sha256", "--mut-anchor-sha256",
         "--budget-s")
RESULT_KEYS = ("status", "reason", "mutants", "manifest_sha256", "source_cert_sha256", "generator_sha256", "wall_s")
CERT_KEYS = frozenset(("format", "anchor_sha256", "n", "q", "k", "U", "J", "dim", "basis", "free_columns",
                       "rank_witness", "rainbow", "failures", "producer"))
INTENDED = (("nc0_identity", "VALID", None), ("nc1_basis_flip", "INVALID", 2), ("nc2_pivot_swap", "INVALID", 4),
            ("nc3_rainbow_swap", "INVALID", 5), ("nc4_failure_delete", "INVALID", 6),
            ("nc5_wrong_anchor_hash", "INVALID", 1), ("nc6_failure_wrong_fibre", "INVALID", 6),
            ("nc7_witness_coef", "INVALID", 4), ("nc8_witness_drop", "INVALID", 0),
            ("nc9_anchor_mutation", "INVALID", 1), ("nc10_basis_scale", "INVALID", 3))


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


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"


def strict_loads(data):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate key")
            out[key] = value
        return out

    def bad_constant(name):
        raise ValueError("non-finite constant")

    def finite_float(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError("non-finite float")
        return value

    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=bad_constant,
                      parse_float=finite_float)


def parse_g1(raw, budget):
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


def read_regular_capped(path, cap):
    """Actual descriptor-bound bytes; a FIFO never reaches a blocking read."""
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_size > cap:
            raise OSError("input kind or cap")
        chunks, total = [], 0
        while True:
            b = os.read(fd, min(65536, cap + 1 - total))
            if not b:
                break
            total += len(b)
            if total > cap:
                raise OSError("input grew past cap")
            chunks.append(b)
        return b"".join(chunks)
    finally:
        os.close(fd)


def read_capped(path, cap, what):
    try:
        data = read_regular_capped(path, cap)
    except OSError as exc:
        raise Stop("IO_ERROR", "cannot read %s: %s" % (what, type(exc).__name__)) from None
    if len(data) > cap:
        raise Stop("BAD_INPUT", what + " exceeds its size cap")
    return data


def write_new(name, data):
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        view = memoryview(data)
        while view:
            written = os.write(fd, view)
            view = view[written:]
    finally:
        os.close(fd)


def is_int(v):
    return type(v) is int


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
    for flag in FLAGS[:-1]:
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
    return got, budget_s


def generate(a, budget, summary):
    cb = read_capped(a["--cert"], CERT_CAP, "certificate")
    src_sha = hashlib.sha256(cb).hexdigest()
    if src_sha != a["--cert-sha256"]:
        raise Stop("INPUT_PIN_MISMATCH", "certificate sha256")
    summary["source_cert_sha256"] = src_sha
    rb = read_capped(a["--anchor"], RAW_CAP, "anchor")
    if hashlib.sha256(rb).hexdigest() != a["--anchor-sha256"]:
        raise Stop("INPUT_PIN_MISMATCH", "anchor sha256")
    try:
        S = strict_loads(cb)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Stop("BAD_INPUT", "certificate is not strict JSON") from None
    if type(S) is not dict or set(S) != CERT_KEYS:
        raise Stop("BAD_INPUT", "certificate keys")
    if dump(S).encode("ascii") != cb:
        raise Stop("BAD_INPUT", "certificate is not in canonical bytes")
    if S["anchor_sha256"] != a["--anchor-sha256"]:
        raise Stop("BAD_INPUT", "certificate is not for this anchor")
    n, q, k, U, J, dim = (S[key] for key in ("n", "q", "k", "U", "J", "dim"))
    if not all(is_int(v) for v in (n, q, k, U, J, dim)):
        raise Stop("BAD_INPUT", "certificate header types")
    basis, wit, rainbow, failures = S["basis"], S["rank_witness"], S["rainbow"], S["failures"]
    if (type(basis) is not list or len(basis) != dim or dim < 1 or type(wit) is not list or len(wit) < 2
            or type(rainbow) is not list or len(rainbow) < 1 or type(failures) is not list or len(failures) < 1):
        raise Stop("BAD_INPUT", "certificate too small for the controls")
    rows = parse_g1(rb, budget)
    if len(rows) != k or any(len(r) != n for r in rows) or n % 3 or q != n // 3:
        raise Stop("BAD_INPUT", "anchor shape differs from the certificate")
    E = [[(rows[x][c] - rows[0][c]) % n for c in range(n)] for x in range(k)]
    fibres = []
    for x in range(k):
        for y in range(x + 1, k):
            budget.tick()
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[((E[x][c] % q) - (E[y][c] % q)) % q].append(c)
            for t in range(q):
                if len(buckets[t]) != 3:
                    raise Stop("BAD_INPUT", "anchor fibre size is not 3")
                fibres.append((x, y, buckets[t]))
    if len(fibres) != J:
        raise Stop("BAD_INPUT", "fibre count differs from J")

    def var(x, c):
        return None if (x == 0 or c == 0) else (x - 1) * (n - 1) + (c - 1)

    def point(idx):
        z, rem = [], idx
        for _ in range(dim):
            z.append(rem % 3)
            rem //= 3
        z.reverse()
        A = [0] * U
        for zr, b in zip(z, basis):
            if zr:
                A = [(av + zr * bv) % 3 for av, bv in zip(A, b)]
        return A

    def fibre_ok(A, j):
        x, y, cols = fibres[j]
        vals = set()
        for c in cols:
            vx, vy = var(x, c), var(y, c)
            vals.add(((0 if vx is None else A[vx]) - (0 if vy is None else A[vy])) % 3)
        return len(vals) == 3

    muts, details = {}, {}
    muts["nc0_identity"] = copy.deepcopy(S)
    details["nc0_identity"] = {}
    m = copy.deepcopy(S)
    p0 = m["rank_witness"][0]["pivot"]
    old = m["basis"][0][p0]
    m["basis"][0][p0] = (old + 1) % 3
    muts["nc1_basis_flip"] = m
    details["nc1_basis_flip"] = {"vector": 0, "position": p0, "old": old, "new": (old + 1) % 3}
    m = copy.deepcopy(S)
    pa, pb = m["rank_witness"][0]["pivot"], m["rank_witness"][1]["pivot"]
    m["rank_witness"][0]["pivot"], m["rank_witness"][1]["pivot"] = pb, pa
    muts["nc2_pivot_swap"] = m
    details["nc2_pivot_swap"] = {"record_a": 0, "record_b": 1, "pivot_a": pa, "pivot_b": pb}
    m = copy.deepcopy(S)
    r0, (f0, jf0) = m["rainbow"][0], m["failures"][0]
    m["rainbow"] = sorted([i for i in m["rainbow"] if i != r0] + [f0])
    m["failures"] = sorted([e for e in m["failures"] if e[0] != f0] + [[r0, 0]], key=lambda e: e[0])
    muts["nc3_rainbow_swap"] = m
    details["nc3_rainbow_swap"] = {"rainbow_idx_moved": r0, "failure_idx_moved": f0,
                                   "failure_fibre_of_moved": jf0, "new_failure_fibre": 0}
    m = copy.deepcopy(S)
    di, dj = m["failures"].pop(0)
    muts["nc4_failure_delete"] = m
    details["nc4_failure_delete"] = {"deleted_idx": di, "deleted_fibre": dj}
    m = copy.deepcopy(S)
    m["anchor_sha256"] = a["--other-sha256"]
    muts["nc5_wrong_anchor_hash"] = m
    details["nc5_wrong_anchor_hash"] = {}
    m = copy.deepcopy(S)
    target = None
    for pos, (idx, j) in enumerate(m["failures"]):
        budget.tick()
        A = point(idx)
        if fibre_ok(A, j):
            raise Stop("BAD_INPUT", "source failure entry %d does not fail" % pos)
        for jj in range(J):
            if fibre_ok(A, jj):
                target = (pos, idx, j, jj)
                break
        if target:
            break
    if target is None:
        raise Stop("BAD_INPUT", "no failure entry whose point has a passing fibre")
    m["failures"][target[0]] = [target[1], target[3]]
    muts["nc6_failure_wrong_fibre"] = m
    details["nc6_failure_wrong_fibre"] = {"position": target[0], "idx": target[1], "old_fibre": target[2],
                                          "new_fibre": target[3]}
    m = copy.deepcopy(S)
    term = m["rank_witness"][0]["combination"][0]
    oc = term[1]
    term[1] = 3 - oc
    muts["nc7_witness_coef"] = m
    details["nc7_witness_coef"] = {"record": 0, "term": 0, "equation": term[0], "old_coef": oc, "new_coef": 3 - oc}
    m = copy.deepcopy(S)
    dropped = m["rank_witness"].pop()
    muts["nc8_witness_drop"] = m
    details["nc8_witness_drop"] = {"deleted_record": len(S["rank_witness"]) - 1, "deleted_pivot": dropped["pivot"]}
    m = copy.deepcopy(S)
    m["anchor_sha256"] = a["--mut-anchor-sha256"]
    muts["nc9_anchor_mutation"] = m
    details["nc9_anchor_mutation"] = {}
    m = copy.deepcopy(S)
    m["basis"][0] = [(2 * v) % 3 for v in m["basis"][0]]
    muts["nc10_basis_scale"] = m
    details["nc10_basis_scale"] = {"vector": 0, "factor": 2}
    blobs, entries = [], []
    for name, verdict, check in INTENDED:
        budget.tick()
        data = dump(muts[name]).encode("ascii")
        if len(data) > CERT_CAP:
            raise Stop("BAD_INPUT", "mutant exceeds the certificate cap")
        blobs.append((name + ".cert.json", data))
        entries.append({"item": name, "file": name + ".cert.json", "sha256": hashlib.sha256(data).hexdigest(),
                        "intended_verdict": verdict, "intended_first_failed_check": check,
                        "detail": details[name]})
    if blobs[0][1] != cb:
        raise Stop("INTERNAL_ERROR", "nc0 bytes differ from the source certificate")
    manifest = {"format": "lemmaU-cert-mutants-v2", "source_cert_sha256": src_sha,
                "anchor_sha256": a["--anchor-sha256"], "generator_sha256": summary["generator_sha256"] or "",
                "mutants": entries}
    mdata = dump(manifest).encode("ascii")
    budget.tick()                                    # deadline check before publication
    try:
        for name, data in blobs:
            budget.tick()
            write_new(name, data)
            budget.tick()
        budget.tick()
        write_new("manifest.json", mdata)
        budget.tick()
    except OSError as exc:
        raise Stop("IO_ERROR", "cannot write outputs: " + type(exc).__name__) from None
    summary["mutants"] = len(blobs)
    summary["manifest_sha256"] = hashlib.sha256(mdata).hexdigest()


def publication_line(summary, budget, t0):
    """Fail closed before/after a publication; never rewrite an existing artifact on late expiry.
    If expiry follows the last write, stdout/exit differ from the retained artifact and audit must reject.
    """
    if summary["status"] == "OK" and budget is not None:
        try:
            budget.tick()
        except Stop as exc:
            summary["status"], summary["reason"] = exc.status, exc.reason
            summary["wall_s"] = round(time.monotonic() - t0, 3)
    return json.dumps(summary, sort_keys=True, separators=(",", ":"))


def main(argv):
    t0 = time.monotonic()
    summary = {key: None for key in RESULT_KEYS}
    # Set by the GO entrypoint from the SAME source bytes it has already read, verified and executed.
    # Informational only; no pathname reopen/read occurs here (including before Budget construction).
    summary["generator_sha256"] = globals().get("VERIFIED_SOURCE_SHA256")
    status, reason = "OK", None
    budget = None
    try:
        a, budget_s = parse_args(argv)
        budget = Budget(t0, budget_s)
        generate(a, budget, summary)
        budget.tick()
    except Stop as s:
        status, reason = s.status, s.reason
    except MemoryError:
        status, reason = "INTERNAL_ERROR", "MemoryError"
    except Exception as exc:
        status, reason = "INTERNAL_ERROR", type(exc).__name__
    summary["status"], summary["reason"] = status, reason
    summary["wall_s"] = round(time.monotonic() - t0, 3)
    line = publication_line(summary, budget, t0)
    try:
        write_new("result.json", (line + "\n").encode("ascii"))
    except OSError as exc:
        summary["status"], summary["reason"] = "IO_ERROR", "cannot write result.json: " + type(exc).__name__
        line = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    line = publication_line(summary, budget, t0)
    try:
        print(line, flush=True)
    except OSError:
        return EXIT["IO_ERROR"]
    # Stdout is now immutable one-line evidence. Do not rewrite/reprint after a late flush.
    if budget is not None:
        try:
            budget.tick()
        except Stop:
            return EXIT["BUDGET_EXCEEDED"]
    return EXIT[summary["status"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
