"""Parent beta capture-audit consumer v1: pure X1/X2/X3/X4/X6/X7 predicates. SOURCE ONLY, UNTESTED.

Implements audit_capture() of the frozen parent consumer contract
/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/beta-audit-consumer-contract-v1.json
(sha256 b26a98caba1fbf17de0376fde24905052b68ebc0d5f567cdebfac092a6cdfd96). X5 RESULT_SCHEMA belongs to audit_schema.
This module starts no processes and performs no application-file I/O; standard-library imports may read runtime files. Trusted Python/import state and -B remain parent launch preconditions. audit_capture()
returns causes only: no verdict, file write, process or /bin/date. Every byte it judges comes from the caller's
read_bytes(path, cap), called only at paths bound by the parent expectation.

    causes = audit_capture(expectation, observed, read_bytes)   # e.g. [] or ["X1 EXIT_MISMATCH"]

TRUSTED-PARENT ADAPTER PRECONDITION (enforced by the parent adapter before the call; never inferred here)
- The expectation is parent authority, never child self-report. PLAN: the plan v5 item and its exact GO. FIXTURE:
  the separately approved instrumented invocation. Its resolved_argv binds that actual command line, including
  --budget-s 2 versus 240; production B-BAD_PIN supplies only the compared status/schema/expected-exit oracle.
- The observation is parent-owned evidence. actual_exit is the parent-observed exit status of the nested science
  child (negative = signal), never a supervisor or driver exit. Capture records map the actual capture files with no
  ignored duplicate field. Census hits and unresolved identities go into settlement.unresolved; every stop signal
  goes into settlement.signals.
- Synthetic negatives: the parent first verifies its own immutable derivation manifest. The manifest preserves the
  genuine upstream receipt and actual exit and labels exactly the altered predicate input. The same function is then
  called; there is no synthetic bypass and no extra field. A synthetic exit (for example 120) is never measured exit
  evidence.
- A receipt match proves only that the bytes at receipt_path have the parent-bound digest, never runtime truth.
  Endedness comes only from settlement, never from a receipt label.
- read_bytes(path, cap) is the contract's descriptor-anchored, cap+1-bounded reader that retains actual identity
  evidence. Tests may use an explicitly labelled immutable snapshot callback, never presented as kernel evidence. It
  returns bytes of length <= cap or raises OSError/ValueError. Any other exception propagates, and the caller must
  treat an exception from audit_capture as a failed audit.
- [] only means that no owned cause fired. It is not a verdict, not X5 and not a canonical audit. No consumer,
  fixture or source PASS writes an audit, releases a reservation or admits a job. That needs the separate five-part
  parent transaction.

DETERMINISTIC RULES
- Strict types: bool is never int, counts are exact ints >= 0, hashes are 64 lowercase hex, paths are absolute and
  normalized (no empty, '.' or '..' component, no NUL), names are plain. An absent or malformed field fails the
  predicate that owns it. No default is substituted, and no JSON-typed input raises.
- Ownership: expected_exit/actual_exit -> X1. capture_paths and captures.stdout -> X2; captures.stderr -> X3.
  outputs, job_dir, artifacts and actual_artifact_names -> X4; X2 also locates result.json through outputs/job_dir.
  settlement -> X6. Top-level format/key sets and every remaining field -> X7.
- Each stream has at most one subcause. MISSING (record absent/null or present false) beats INCOMPLETE (present but
  not a verified complete capture), which beats the content cause. Content is judged only on a verified complete
  capture: stdout must equal the actual bytes of the bound result.json (its single canonical line is X5's), and
  stderr must be empty. An empty complete capture is not a missing capture.
- Cross-role path placement is parent authority; this predicate adds no uncontracted disjointness restriction.
- Reads happen only at bound paths, at most once per path per call, with one cap (READ_CAP), in evaluation order
  X2, X3, X4, X7 (artifact names and pin paths sorted).
"""
import hashlib
import math

EXPECTATION_FORMAT = "beta-parent-audit-expectation-v1"
OBSERVATION_FORMAT = "beta-parent-audit-observation-v1"
# Plan pinned by the consumer contract authority (ext-search-plan-v5.json); any other plan digest fails X7.
AUTHORITY_PLAN_SHA256 = "254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731"
MODES = ("PLAN", "FIXTURE")
RESULT_NAME = "result.json"
READ_CAP = 16 << 20  # successor4 v3 plan/source-pin/artifact cap, also applied to captures and the receipt
READ_FAILURES = (OSError, ValueError)  # defined read_bytes failures; every other exception propagates

X1 = "X1 EXIT_MISMATCH"
X2_MISSING = "X2 STDOUT_CAPTURE_MISSING"
X2_INCOMPLETE = "X2 STDOUT_CAPTURE_INCOMPLETE"
X2_NOT_EXACT = "X2 STDOUT_NOT_EXACT_RESULT_LINE"
X3_MISSING = "X3 STDERR_CAPTURE_MISSING"
X3_INCOMPLETE = "X3 STDERR_CAPTURE_INCOMPLETE"
X3_NONEMPTY = "X3 STDERR_NONEMPTY"
X4 = "X4 ARTIFACT_SET_OR_DIGEST"
X6 = "X6 UNSETTLED"
X7 = "X7 PROVENANCE"
# Contract cause order without X5 RESULT_SCHEMA, which audit_schema owns.
CAUSE_ORDER = (X1, X2_MISSING, X2_INCOMPLETE, X2_NOT_EXACT, X3_MISSING, X3_INCOMPLETE, X3_NONEMPTY, X4, X6, X7)

EXPECTATION_KEYS = frozenset((
    "format", "mode", "item", "plan_sha256", "expected_exit", "outputs", "job_dir", "capture_paths",
    "receipt_path", "receipt_sha256", "resolved_argv", "go_sha256", "source_pins", "input_pins", "date_start",
    "date_end"))
OBSERVATION_KEYS = frozenset((
    "format", "item", "plan_sha256", "mode", "actual_exit", "captures", "artifacts", "actual_artifact_names",
    "receipt", "settlement", "resolved_argv", "go_sha256", "source_pins", "input_pins", "date_start", "date_end"))
STREAM_KEYS = frozenset(("stdout", "stderr"))
CAPTURE_KEYS = frozenset(("present", "path", "sha256", "bytes_seen", "bytes_stored", "eof", "overflow", "error"))
ARTIFACT_KEYS = frozenset(("path", "sha256", "bytes", "ino", "nlink"))
RECEIPT_KEYS = frozenset(("path", "sha256"))
SETTLEMENT_KEYS = frozenset(("reaped", "group_empty", "census_complete", "unresolved", "signals"))
HEX_DIGITS = frozenset("0123456789abcdef")

_ABSENT = object()  # field unavailable: fails every check and never stands in for a value
_MISSING, _INCOMPLETE, _COMPLETE = "MISSING", "INCOMPLETE", "COMPLETE"


def audit_capture(expectation, observed, read_bytes):
    """Ordered unique X1/X2/X3/X4/X6/X7 causes; [] only when every owned predicate is established."""
    reader = _Reader(read_bytes)
    fired = set()
    if not _exit_matches(expectation, observed):
        fired.add(X1)
    state, stdout = _capture(expectation, observed, "stdout", reader)
    if state == _MISSING:
        fired.add(X2_MISSING)
    elif state == _INCOMPLETE:
        fired.add(X2_INCOMPLETE)
    else:
        result = _result_bytes(expectation, reader)
        if result is None or stdout != result:
            fired.add(X2_NOT_EXACT)
    state, stderr = _capture(expectation, observed, "stderr", reader)
    if state == _MISSING:
        fired.add(X3_MISSING)
    elif state == _INCOMPLETE:
        fired.add(X3_INCOMPLETE)
    elif len(stderr) != 0:
        fired.add(X3_NONEMPTY)
    if not _artifacts_ok(expectation, observed, reader):
        fired.add(X4)
    if not _settled(observed):
        fired.add(X6)
    if not _provenance_ok(expectation, observed, reader):
        fired.add(X7)
    return [cause for cause in CAUSE_ORDER if cause in fired]


class _Reader:
    """Calls read_bytes(path, READ_CAP) at most once per bound path; any failure yields None, never bytes."""

    def __init__(self, read_bytes):
        self._read_bytes = read_bytes if callable(read_bytes) else None
        self._cache = {}

    def read(self, path):
        if not _norm_abs(path):
            return None
        if path not in self._cache:
            data = None
            if self._read_bytes is not None:
                try:
                    data = self._read_bytes(path, READ_CAP)
                except READ_FAILURES:
                    data = None
                if type(data) is not bytes or len(data) > READ_CAP:
                    data = None
            self._cache[path] = data
        return self._cache[path]


def _get(record, key):
    """Field value, or _ABSENT when record is not an exact dict or lacks key."""
    if type(record) is dict and key in record:
        return record[key]
    return _ABSENT


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _hex64(value):
    return type(value) is str and len(value) == 64 and set(value) <= HEX_DIGITS


def _count(value):
    return type(value) is int and value >= 0


def _same_str(value, want):
    return type(value) is str and type(want) is str and value == want


def _norm_abs(path):
    """Absolute normalized path as in ext4_gate anchored_parent: leading '/', no '', '.', '..' component, no NUL."""
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        return False
    return all(part not in ("", ".", "..") for part in path.split("/")[1:])


def _plain_name(name):
    return type(name) is str and name not in ("", ".", "..") and "/" not in name and "\x00" not in name


def _names(value):
    """Exact nonempty list of distinct plain names, else None; no uncontracted count limit."""
    if type(value) is not list or len(value) == 0:
        return None
    if not all(_plain_name(name) for name in value) or len(set(value)) != len(value):
        return None
    return value


def _exact(left, right):
    """Iterative typed JSON equality with no depth cap; reject cycles but allow repeated acyclic aliases."""
    stack = [(left, right, False)]
    active = set()
    while stack:
        a, b, leave = stack.pop()
        pair = (id(a), id(b))
        if leave:
            active.remove(pair)
            continue
        if type(a) is not type(b):
            return False
        if type(a) in (dict, list):
            if pair in active:
                return False
            active.add(pair)
            stack.append((a, b, True))
            if type(a) is dict:
                if (len(a) != len(b) or any(type(k) is not str for k in b)
                        or any(type(k) is not str or k not in b for k in a)):
                    return False
                stack.extend((a[k], b[k], False) for k in a)
            else:
                if len(a) != len(b):
                    return False
                stack.extend((x, y, False) for x, y in zip(a, b))
        elif type(a) is float:
            if not math.isfinite(a) or not math.isfinite(b) or a != b:
                return False
        elif type(a) in (str, int, bool):
            if a != b:
                return False
        elif a is not None:
            return False
    return True

def _keys(record, keys):
    """Exact built-in JSON string keys on every schema boundary; str subclasses never alias authority."""
    return type(record) is dict and all(type(k) is str for k in record) and set(record) == set(keys)


def _bound_job_dir(expectation):
    job_dir = _get(expectation, "job_dir")
    return job_dir if _norm_abs(job_dir) else None


def _bound_capture_path(expectation, stream):
    """Declared capture path of stream, or None when the parent binding is unusable."""
    paths = _get(expectation, "capture_paths")
    if not _keys(paths, STREAM_KEYS):
        return None
    path = paths[stream]
    if not _norm_abs(path):
        return None
    return path


def _exit_matches(expectation, observed):
    want = _get(expectation, "expected_exit")
    got = _get(observed, "actual_exit")
    return type(want) is int and type(got) is int and got == want


def _capture(expectation, observed, stream, reader):
    """(MISSING, None), (INCOMPLETE, None) or (COMPLETE, verified actual capture bytes)."""
    captures = _get(observed, "captures")
    record = _get(captures, stream)
    if record is _ABSENT or record is None or (type(record) is dict and _get(record, "present") is False):
        return _MISSING, None
    if type(captures) is not dict or any(type(key) is not str or key not in STREAM_KEYS for key in captures):
        return _INCOMPLETE, None
    path = _bound_capture_path(expectation, stream)
    if path is None or not _keys(record, CAPTURE_KEYS) or record["present"] is not True:
        return _INCOMPLETE, None
    seen, stored, digest = record["bytes_seen"], record["bytes_stored"], record["sha256"]
    if (not _same_str(record["path"], path) or not _hex64(digest) or not _count(seen) or not _count(stored)
            or seen != stored or stored > READ_CAP or record["eof"] is not True
            or record["overflow"] is not False or record["error"] is not None):
        return _INCOMPLETE, None
    data = reader.read(path)
    if data is None or len(data) != stored or _sha256(data) != digest:
        return _INCOMPLETE, None
    return _COMPLETE, data


def _result_bytes(expectation, reader):
    """Actual bytes of the declared result.json at its bound path; None if undeclared, unbound or unreadable."""
    outputs = _names(_get(expectation, "outputs"))
    job_dir = _bound_job_dir(expectation)
    if outputs is None or job_dir is None or RESULT_NAME not in outputs:
        return None
    return reader.read(job_dir + "/" + RESULT_NAME)


def _artifacts_ok(expectation, observed, reader):
    outputs = _names(_get(expectation, "outputs"))
    job_dir = _bound_job_dir(expectation)
    artifacts = _get(observed, "artifacts")
    if outputs is None or job_dir is None or type(artifacts) is not dict:
        return False
    census = _names(_get(observed, "actual_artifact_names"))
    ok = (RESULT_NAME in outputs and census is not None and set(census) == set(outputs)
          and _keys(artifacts, outputs))
    for name in sorted(outputs):
        if not _artifact_ok(_get(artifacts, name), job_dir + "/" + name, reader):
            ok = False
    return ok


def _artifact_ok(record, path, reader):
    if not _keys(record, ARTIFACT_KEYS):
        return False
    size, digest, ino, nlink = record["bytes"], record["sha256"], record["ino"], record["nlink"]
    if (not _same_str(record["path"], path) or not _hex64(digest) or not _count(size) or size > READ_CAP
            or type(ino) is not int or ino <= 0 or type(nlink) is not int or nlink != 1):
        return False
    data = reader.read(path)
    return data is not None and len(data) == size and _sha256(data) == digest


def _settled(observed):
    settlement = _get(observed, "settlement")
    if not _keys(settlement, SETTLEMENT_KEYS):
        return False
    unresolved, signals = settlement["unresolved"], settlement["signals"]
    return (settlement["reaped"] is True and settlement["group_empty"] is True
            and settlement["census_complete"] is True and type(unresolved) is list and len(unresolved) == 0
            and type(signals) is list and len(signals) == 0)


def _provenance_ok(expectation, observed, reader):
    ok = _record_ok(expectation, EXPECTATION_KEYS, EXPECTATION_FORMAT)
    if not _record_ok(observed, OBSERVATION_KEYS, OBSERVATION_FORMAT):
        ok = False
    mode = _get(expectation, "mode")
    if type(mode) is not str or mode not in MODES or not _same_str(_get(observed, "mode"), mode):
        ok = False
    item = _get(expectation, "item")
    if type(item) is not str or not _same_str(_get(observed, "item"), item):
        ok = False
    plan = _get(expectation, "plan_sha256")
    if not _same_str(plan, AUTHORITY_PLAN_SHA256) or not _same_str(_get(observed, "plan_sha256"), plan):
        ok = False
    if not _receipt_ok(expectation, observed, reader):
        ok = False
    argv = _get(expectation, "resolved_argv")
    if (type(argv) is not list or not all(type(arg) is str for arg in argv)
            or not _exact(argv, _get(observed, "resolved_argv"))):
        ok = False
    go = _get(expectation, "go_sha256")
    if not _hex64(go) or not _same_str(_get(observed, "go_sha256"), go):
        ok = False
    for key in ("source_pins", "input_pins"):
        if not _pins_bound(_get(expectation, key), _get(observed, key), reader):
            ok = False
    for key in ("date_start", "date_end"):
        record = _get(expectation, key)
        if type(record) is not dict or len(record) == 0 or not _exact(record, _get(observed, key)):
            ok = False
    return ok


def _record_ok(record, keys, form):
    return _keys(record, keys) and _same_str(record["format"], form)


def _receipt_ok(expectation, observed, reader):
    path, digest = _get(expectation, "receipt_path"), _get(expectation, "receipt_sha256")
    if not _norm_abs(path) or not _hex64(digest):
        return False
    receipt = _get(observed, "receipt")
    ok = (_keys(receipt, RECEIPT_KEYS) and _same_str(receipt["path"], path)
          and _same_str(receipt["sha256"], digest))
    data = reader.read(path)
    return ok and data is not None and _sha256(data) == digest


def _pins_bound(pins, observed_pins, reader):
    if (type(pins) is not dict
            or not all(_norm_abs(path) and _hex64(digest) for path, digest in pins.items())):
        return False
    ok = _exact(pins, observed_pins)
    for path in sorted(pins):
        data = reader.read(path)
        if data is None or _sha256(data) != pins[path]:
            ok = False
    return ok
