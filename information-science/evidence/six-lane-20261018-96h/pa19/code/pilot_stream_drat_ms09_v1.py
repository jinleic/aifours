#!/usr/bin/env python3
"""PA19 96h P-STREAM runner v1, multiset ms09: pilot_file_drat_v27.py (d9a1d5b3...) + the P-STREAM transport
(parent request 2026-10-19 04:5x; design notes/p-stream-design-v1.md and review/p-stream-design-v1.json):
  S1 No proof byte is ever written to disk.  kissat writes its proof into an owned FIFO; the ProofBuffer collector
     thread retains it in RAM (immutable FEED_BLOCK blocks) under the HARD byte cap and measures bytes and SHA-256
     at the producer; after the reap the blocks are frozen (tuple) and re-hashed by an independent second pass.
  S2 Two pinned checkers consume the SAME frozen buffer through stdin, sequentially (one native child at a time):
     A = the lane copy LANE/code/vendor/drat-trim (111b0405...), B = the provenanced parent build
     moqls7-parent-proofcheck-v1/drat-trim (a46c0c71...; receipt parent-result.json 200d307d...; source
     d834b649...).  argv [DRAT_X, CNF, -i, -t CHECK_SECONDS]: no proof path, so drat-trim reads the proof from
     stdin and '-i' forces binary mode.  An owned Feeder thread writes the blocks into the checker's stdin pipe,
     hashing/counting exactly the bytes os.write() accepted; the runner's read end is closed right after Popen
     and the write end is closed exactly once.  Each checker binary is re-hashed when its child is prepared.
  S3 Checker stdout+stderr pass the capture filter: raw bytes and SHA-256 are measured in-stream; ONLY lines
     that fullmatch the drat-trim duplicate-literal line (drat-trim.c:1162) are dropped, counted by phase and
     bytes; every other byte is the retained (capped) log.
  S4 Per checker: feed mode plain, fed bytes/SHA-256 == the collector measurement, 'read N bytes' == fed bytes,
     the stdin line, the parse header, exactly ['s VERIFIED'] rc0, no forbidden pattern, filter accounting,
     settled; the buffer is re-hashed after the checks; then the unchanged terminal gate and commit boundary.
     A later checker is skipped once an earlier one has a defect (the item is UNKNOWN either way).
  S5 RSS: the retained buffer bytes are charged to the lane RSS trip: child RSS + max(runner RSS, retained).
  S6 Controls C1-C7 for both checkers plus C7b (missing CNF + held feed: EPIPE liveness) = 14 children;
     CHECK_SECONDS 600 per checker; ITEMS = [] (controls-only qualification); production items only by a
     later item-only delta with its own parent GO bound to the then-current frontier.
PA19 96h pilot runner v14 = v13 + fixes for Codex r6 (review/codex-pilot-v13-r6/result.json a79577ae...;
R5#2-#4 resolved there):
  r6#1 the settle-all pass iterates OWNED by index entirely inside its retry guard (no unguarded snapshot
       allocation) and is a module function settle_all(), also used by main's closeout.
  r6#2 an unstarted capture reader is an explicit settlement failure (streams closed, sink finished,
       UNSETTLED + latch); settle-all stops retrying bookkeeping for a REAPED child after 20 failures and
       records it UNSETTLED with the latch held; an unreaped child is always retried.
PA19 96h pilot runner v13 notes follow (= v12 + fixes for the Codex r5 cleanup findings, review/codex-pilot-v12-r5/result.json
545eb709...; R4#2-#5 resolved there):
  r5#1 settle-all sets the emergency stop WITHOUT polling and retries settle() inside a protected loop.
  r5#2 single SIGTERM: the timestamp is computed before send_signal and the delivery marker is stored
       immediately after it returns, with no fallible call in between (term() and reap_robust()).
  r5#3 an existing quarantine receipt counts as published only if it parses and names this pid; a partial
       artifact is preserved and reported as a publication failure.
  r5#4 receipt publication is bounded (20 attempts); after the child is reaped the reaper returns and a
       missing/failed receipt is carried into settlement as UNSETTLED with the latch held.
PA19 96h pilot runner v12 notes follow (= v11 + fixes for Codex r4, review/codex-pilot-v11-r4/result.json 92eb788e...):
  r4#1 cleanup: emergency stop state is set before any fallible logging; Child.term marks delivery only
       after send_signal returns (undelivered SIGTERM is retried); reap_robust protects its whole retry
       path (including back-off), polls instead of blocking so a pending quarantine receipt is retried
       until written, and never returns before the retained Popen is reaped; run_child's settle-all
       requests termination for any child it must settle after an escape.
  r4#2 resource classifier also matches drat-trim 'failed to reallocate' (unit-stack realloc failure).
  r4#3 the new-file census is collected BEFORE final admission; cancel/latch/frozen-deadline are rechecked
       immediately before Popen with no blocking work in between.
  r4#4 cwd preparation is inside run_child's cleanup guard (a pre-created proof sink is always finished).
  r4#5 each child gets a private TMPDIR (its own cwd); the census covers only the run output tree.
PA19 96h pilot runner v11 notes follow (= v10 with the new-file census scoped to the run output tree and LANE/tmp, so
unrelated lane writes such as checkpoints cannot cause a false latch; v10 was never frozen or sent).
PA19 96h pilot runner v10 notes follow.  v1-v9 are preserved and were never run.  Review history:
  v3 parent NO-GO; v5 Codex r1, v8 Codex r2, v9 Codex r3 (review/codex-pilot-v9-r3/result.json 749f0d5e...)
  all needs-rework.  r3 resolved R2#1,#3,#5,#6.  v10 changes by r3 finding:
  r3#1 ownership is pre-allocated (Child appended to OWNED before Popen) and one exception-resistant
       reap loop (single SIGTERM, bounded wait, quarantine receipt at the 60 s transition, wait())
       retries on any exception and never unwinds before the child is reaped.
  r3#2 the signal handler is lock-free: it only stamps a scalar cancel order with next(ORDER); no Event.
  r3#3 native memory diagnostics (MEMOUT, MEMORY ALLOCATION ERROR, out-of-memory) in any child
       output latch a memory-resource stop (EXIT_SAFETY_STOP), in controls and items.
  r3#4/#5 kissat process/output behaviour: upstream rel-4.0.4 source evidence
       (evidence/kissat-source-evidence-v2.json d4495a3f...) shows popen only for compressed suffixes,
       fopen-in-place for other paths, no other outputs without -o; runtime defence in depth: the proof
       FIFO must still be the same FIFO inode after exit, the per-child cwd must still be empty, and a
       lane new-file census around each kissat child must show only the expected outputs.
  r3#6 the full serial settlement tail (TERM_WAIT + 2*STREAM_JOIN + SINK_UNBLOCK + 30 = 220 s) is
       reserved in every child cutoff; child deadlines are frozen as min(start+wall+GRACE, abs_end-tail).
  r3#7 every retained JSON is bounded: strings and lists are truncated with digests, serialized size is
       capped at RECORD_MAX and RECORD_ALLOW is the product of a fixed record count and RECORD_MAX.
  r3#8 controls require a COMPLETED checker outcome (exactly 's VERIFIED' rc0 or 's NOT VERIFIED' rc1,
       no resource diagnostics) in addition to their intended reason.
  r3#9 closeout: blocking metadata first, then an explicit closeout boundary next(ORDER); a cancel
       stamped before it is reflected in the code and summary and can never yield exit 0.

NOT TO BE RUN without the item-specific parent GO whose JSON names this file's SHA-256.

Scope (frozen): controls only (ITEMS = []): C1-C7 and C7b through the P-STREAM transport for both pinned
checkers.  Production items of multiset ms09 are added only by a later item-only delta with its own parent GO:
  encode_skel_b.build_partbatch over a pinned placement-list interval.
Per item: CNF built in memory by the vendored unchanged encoder, frozen digest required, written by exclusive
creation and re-hashed (the only retained input); kissat -q -f --seed=1 --time=300 CNF PROOF_FIFO (owned RAM
collector, HARD cap, nothing on disk); then, only on a settled self-exit rc20 's UNSATISFIABLE' with a complete
buffer, checker A and then checker B with the frozen buffer on stdin; CNF and buffer re-hashed.
No deletion/overwrite, no SIGKILL, no subprocess timeout, no ulimit; lane FIFOs are new and never
removed.  The only signal ever sent is ONE SIGTERM to an UNREAPED owned Popen child, then a bounded
60 s wait; a survivor gets a quarantine receipt, no further signal, LATCH, and the runner keeps waiting.
"""
import errno
import hashlib
import importlib.util
import itertools
import json
import os
import re
import signal
import stat
import subprocess
import sys
import threading
import time
from datetime import datetime

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
KISSAT = ("/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat", "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848")
DRAT_OLD = (OLD + "/tools/drat-trim/drat-trim", "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4")
DRAT = LANE + "/code/vendor/drat-trim"
DRAT_PROV = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/drat-trim",
             "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37")
DRAT_PROV_RECEIPT = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/"
                     "parent-result.json", "200d307dd52ab4d6559ff89d5faa6c3859e256bbd20c6d1fb439d237b9af3bfe")
DRAT_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
CHECKERS = (("A", DRAT, DRAT_OLD[1]), ("B", DRAT_PROV[0], DRAT_PROV[1]))  # S2: sequential, same frozen buffer
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
REGISTRY = (LANE + "/evidence/inherited-stop-registry-v1.json", "ee370929f20ffe514e71bce6961e31ed32faaf243e0433d9268179956a0e9873")
LAUNCH_CONTRACT = (RUN + "/control/launch-contract-tightening-v1.json", "8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20")
BINARY_IMPORTS = (LANE + "/evidence/probes/binary-process-imports-v1.json", "c822c4f07974b3f107c18c91bd910a972aa6ddee025e8087c256917492b7cffc")
KISSAT_SOURCE = (LANE + "/evidence/kissat-source-evidence-v2.json", "d4495a3f0d526604e586b11cbd2b1ed717e2872419e31536848bd2000f51a7a7")
MONITOR = RUN + "/control/resource-observer-live-v3.jsonl"
OBSERVER_SOURCE_SHA = "fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196"
OBSERVER_CWD = RUN
SAMPLE_SCOPE = "metadata only; not scientific checkpoint or launch admission"
OLD_LIVE_MARKERS = {  # inherited registry v1 live cycle2-root markers: must stay byte-identical and complete
    "STOP-m2skel7": "06359a697a2029fc599f176944f8ec11d5403739e9a12e96e8a098edca561974",
    "STOP-m2skel8": "294e4946af9b8d84d556aeef37eed717aa69c5502f016f1c609a34374c7b5b86",
    "STOP-m2skel9": "52c9581db260d317bf0fbfe440fbb8acc9e54fd0f46a55ce63be80196c8a0152",
    "STOP-m2partbatch5": "117fc85ffa66c20f31271cfde01fa82bcbae18f12599752bb7057ea8deea750c",
    "STOP-hard10": "300493c629141543b71db391f98f8d2098618d1cee57c84d68be106874411287",
    "STOP-m2r10": "300493c629141543b71db391f98f8d2098618d1cee57c84d68be106874411287",
    "STOP-hard12": "94b56f04b59849923b41db6929760de00a33c12f077983faa2670a2080015bb2",
    "STOP-m2r12": "94b56f04b59849923b41db6929760de00a33c12f077983faa2670a2080015bb2",
    "STOP-K1": "b05f12b9587bb89a8b30d3d040074e1958463109d866bddeb96527d79c9716bf",
}
P0 = [4, 3, 3, 3, 3, 3]
ITEMS = []  # P-STREAM v1: controls-only qualification; production items only by a later item-only delta
SOLVER_SECONDS = 300
CHECK_SECONDS = 600                   # per checker, two per item (measured max 0.598 s per proof MB)
GRACE = 60
TERM_WAIT = 60
STREAM_JOIN = 60
SINK_UNBLOCK = 10
SETTLE_TAIL = TERM_WAIT + STREAM_JOIN + SINK_UNBLOCK + STREAM_JOIN + 30   # 220 s serial settlement bound
PROOF_CAP = 629_145_600              # HARD: the RAM buffer never retains more than this (never written to disk)
CONTROL_PROOF_CAP = 8 * 1024 * 1024  # HARD RAM cap for control proofs
LOG_CAP = 16 * 1024 * 1024           # HARD per captured stdout+stderr stream
RECORD_MAX = 512 * 1024              # HARD per retained JSON record (bounded() + size check)
STR_MAX = 1000
LIST_MAX = 40
ITEM_RECORDS = 11                     # 3 children x (launch, settle, quarantine) + item record + spare
CONTROL_RECORDS = 14 * 3 + 2          # 14 children x (launch, settle, quarantine) + controls.json + spare
RUN_RECORDS = 3                       # launch-record, summary, spare
CNF_ITEM_MAX = max((it["cnf"][1] for it in ITEMS), default=0)
ITEM_RESERVE = CNF_ITEM_MAX + (1 + len(CHECKERS)) * LOG_CAP + ITEM_RECORDS * RECORD_MAX  # S1: no proof bytes on disk
CONTROL_CHILDREN = 14                 # C1 kissat+A+B, C2 A+B, C3 A+B, C4 A+B, C5 kissat, C6 kissat, C7 kissat, C7b A+B
CONTROL_CNF_ALLOW = 1024 * 1024       # six PHP CNFs, each < 64 KiB
CONTROL_RESERVE = CONTROL_CHILDREN * LOG_CAP + CONTROL_CNF_ALLOW + CONTROL_RECORDS * RECORD_MAX  # S1: RAM proofs only
RUN_RESERVE = RUN_RECORDS * RECORD_MAX
FREE_FLOOR = 12_000_000_000
FRESH_BASE = 12_200_000_000
LANE_RSS_TRIP = 6 * 1024 ** 3
CONTROL_CHILD_WALL = 60
CONTROLS_WORST_SECONDS = CONTROL_CHILDREN * (CONTROL_CHILD_WALL + GRACE + SETTLE_TAIL + 30)
ITEM_WORST_SECONDS = (30 + (SOLVER_SECONDS + GRACE + SETTLE_TAIL) + 30
                      + len(CHECKERS) * (CHECK_SECONDS + GRACE + SETTLE_TAIL + 30))
MAX_CHUNK = 10800
SETTLE = 120
MARGIN = 60
OWNED_SETTLED_BY = datetime.fromisoformat("2026-10-22T21:56:33-07:00").timestamp()
CHILD_ENV = dict(os.environ, TMPDIR=LANE + "/tmp", PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1",
                 OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
EXIT_PLAN_COMPLETE = 0      # every planned item has a terminal record (UNSAT or UNKNOWN); NOT a science verdict
EXIT_SAT_CANDIDATE = 10
EXIT_CONTROLS_FAILED = 20
EXIT_ADMISSION_REFUSED = 30
EXIT_CANCELLED = 40
EXIT_SAFETY_STOP = 50
EXIT_EXCEPTION = 60
EXIT_PRESTART_REFUSED = 70
NONLATCHING_TRIPS = {"proof_cap", "owner_cancel_sigterm"}
RESOURCE_DIAG = re.compile(r"(?i)(memout|memory allocation error|out of memory|out-of-memory|failed to reallocate|reallocation failed)")
FEED_BLOCK = 1 << 20                  # S1: RAM block size and collector read size
WRITE_SLICE = 1 << 16                 # S2: feeder os.write slice
HOLD_SECONDS = 30                     # S6: a C7b held feed waits at most this long for the checker reap
SUFFIX = b"x"                         # S6: C3 trailing byte appended in transit
STDIN_LINE = "c reading proof from stdin"
DUP_LINE = re.compile(rb"\rc WARNING: detected and deleted duplicate literal (-?[1-9][0-9]*) at position ([1-9][0-9]*) "
                      rb"of proof line ([1-9][0-9]*)\n")
PARSE_LINE = re.compile(rb"\rc parsing input formula with ([0-9]+) variables and ([0-9]+) clauses\n")
PENDING_MAX = 1 << 16                 # S3: no duplicate-literal line is this long; longer pending bytes are kept

ORDER = itertools.count(1)
LATCH = []          # persistent safety/unsettled reasons; non-empty refuses every later child
OWNED = []          # every Child (pre-allocated before Popen), for the computed settlement summary
LIVE_BUFFERS = []   # S5: every ProofBuffer; the unreleased ones are charged to the lane RSS trip
STATE = {"seq": 0, "out": None, "abs_end": None, "chunk_end": None, "remaining_reserve": 0,
         "cancel_order": None, "run_record": None, "go": None, "runner_sha": None}


def on_term(signum, frame):
    """r3#2: lock-free; only stamps a scalar order once."""
    if STATE["cancel_order"] is None:
        STATE["cancel_order"] = next(ORDER)


def cancelled():
    return STATE["cancel_order"] is not None


def latch(reason):
    LATCH.append(str(reason)[:STR_MAX])


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True,
                          check=True, stdin=subprocess.DEVNULL).stdout.strip()


def bounded(x):
    """r3#7: bound strings/lists recursively, replacing removed text by its SHA-256."""
    if isinstance(x, str):
        if len(x) <= STR_MAX:
            return x
        return x[:STR_MAX] + "...[truncated %d chars sha256 %s]" % (len(x), hashlib.sha256(x.encode()).hexdigest())
    if isinstance(x, (list, tuple)):
        y = [bounded(v) for v in x[:LIST_MAX]]
        if len(x) > LIST_MAX:
            y.append("...[%d more items]" % (len(x) - LIST_MAX))
        return y
    if isinstance(x, dict):
        return {str(k)[:200]: bounded(v) for k, v in x.items()}
    return x


def serialize(obj):
    data = json.dumps(bounded(obj), indent=1, sort_keys=True).encode()
    if len(data) > RECORD_MAX:
        raise RuntimeError("record exceeds RECORD_MAX (%d bytes)" % len(data))
    return data


def write_x(path, obj):
    data = serialize(obj)
    with open(path, "xb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    return hashlib.sha256(data).hexdigest()


def write_bytes_x(path, data):
    with open(path, "xb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    return hashlib.sha256(data).hexdigest(), len(data)


def sha_file(path):
    st = os.lstat(path)
    if not stat.S_ISREG(st.st_mode):
        raise RuntimeError("not a regular file: " + path)
    h = hashlib.sha256()
    n = 0
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def read_pinned(path, expect):
    st = os.lstat(path)
    if not stat.S_ISREG(st.st_mode):
        raise RuntimeError("not a regular file: " + path)
    with open(path, "rb") as f:
        raw = f.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != expect:
        raise RuntimeError(f"pin mismatch {path}: {got} != {expect}")
    return raw


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def ps_table():
    """Process table rows (pid, ppid, pgid, rss_kib); raises on failure (callers latch)."""
    out = subprocess.run(["/bin/ps", "-A", "-o", "pid=,ppid=,pgid=,rss="], capture_output=True, text=True,
                         stdin=subprocess.DEVNULL)
    if out.returncode != 0:
        raise RuntimeError("ps -A failed rc %d" % out.returncode)
    rows = []
    for ln in out.stdout.splitlines():
        parts = ln.split()
        if len(parts) != 4 or not all(p.isdigit() for p in parts):
            raise RuntimeError("malformed ps row %r" % ln)
        rows.append(tuple(int(p) for p in parts))
    if not rows:
        raise RuntimeError("empty ps table")
    return rows


def identity_checked(pid, runner_pid):
    """Start identity; must parse and show ppid==runner and pgid==pid (own session)."""
    out = subprocess.run(["/bin/ps", "-o", "pid=,ppid=,pgid=,lstart=,comm=", "-p", str(pid)],
                         capture_output=True, text=True, stdin=subprocess.DEVNULL)
    line = out.stdout.strip()
    parts = line.split()
    if out.returncode != 0 or len(parts) < 8 or not all(p.isdigit() for p in parts[:3]):
        raise RuntimeError("unavailable/malformed start identity %r" % line)
    if int(parts[0]) != pid or int(parts[1]) != runner_pid or int(parts[2]) != pid:
        raise RuntimeError("start identity mismatch %r" % line)
    return line


def lane_files():
    """r3#4/#5: (path -> (inode, size)) for every non-directory entry under the run output tree and
    LANE/tmp (the trees a misbehaving child could reach through its paths/cwd; symlinks not followed)."""
    snap = {}
    for root in (STATE["out"],):  # r4#5: private per-child TMPDIR lives inside the run tree
        for dp, dns, fns in os.walk(root, followlinks=False):
            for n in fns:
                p = os.path.join(dp, n)
                st = os.lstat(p)
                snap[p] = (st.st_ino, st.st_size)
    return snap


def registry_refusals():
    """Fail-closed STOP registry: new-round STOP*/HALT*/SAT-CANDIDATE* markers in LANE/control or
    RUN/control; any change, loss or addition in the inherited old cycle2-root STOP/HALT set."""
    why = []
    for d in (LANE + "/control", RUN + "/control"):
        for name in sorted(os.listdir(d)):
            if re.match(r"(?i)^(stop|halt|sat-candidate)", name) or "HALT" in name:
                why.append("new-round marker " + os.path.join(d, name))
    c2 = OLD + "/cycle2"
    present = sorted(n for n in os.listdir(c2) if re.match(r"^(STOP|HALT)", n) or "HALT" in n)
    if present != sorted(OLD_LIVE_MARKERS):
        why.append("inherited cycle2 marker set changed: " + json.dumps(present))
    for name, h in OLD_LIVE_MARKERS.items():
        try:
            if sha_file(os.path.join(c2, name))[0] != h:
                why.append("inherited marker changed: " + name)
        except Exception as exc:
            why.append(f"inherited marker unreadable: {name}: {exc!r}")
    try:
        if sha_file(REGISTRY[0])[0] != REGISTRY[1]:
            why.append("lane registry changed")
        if sha_file(LAUNCH_CONTRACT[0])[0] != LAUNCH_CONTRACT[1]:
            why.append("launch contract changed")
    except Exception as exc:
        why.append("registry/contract unreadable: %r" % exc)
    return why


def _aware(s):
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("naive timestamp")
    return dt


def _int(x, lo=None):
    if not isinstance(x, int) or isinstance(x, bool) or (lo is not None and x < lo):
        raise ValueError("bad integer %r" % (x,))
    return x


def stability_refusals(projected):
    """resource-stability-addendum v1 rule over the v2-pinned v3 monitor; strict schema."""
    st = os.lstat(MONITOR)
    if not stat.S_ISREG(st.st_mode):
        return ["monitor is not a regular file"]
    with open(MONITOR, "rb") as f:
        raw = f.read()
    complete = raw.split(b"\n")[:-1]  # last element: b"" after a final newline, or an ignored partial line
    rows = []
    for i, ln in enumerate(complete):
        try:
            o = json.loads(ln)
            if not isinstance(o, dict):
                raise ValueError("not an object")
            if "event" in o:
                if not (i == 0 and set(o) == {"event", "at", "pid", "pgid", "cwd", "source_sha256"}
                        and o["event"] == "observer_start" and o["source_sha256"] == OBSERVER_SOURCE_SHA
                        and o["cwd"] == OBSERVER_CWD):
                    return ["monitor event line %d is not the allowed first observer_start: %r" % (i, ln[:160])]
                _aware(o["at"])
                _int(o["pid"], 1)
                _int(o["pgid"], 1)
                continue
            if set(o) != {"t", "free", "floor_bytes", "scope"} or o["floor_bytes"] != 12_000_000_000 \
                    or o["scope"] != SAMPLE_SCOPE:
                raise ValueError("sample schema/fixed values")
            _int(o["floor_bytes"], 0)
            rows.append((_aware(o["t"]).timestamp(), _int(o["free"], 0)))
        except Exception as exc:
            return ["malformed monitor line %d: %r (%r)" % (i, ln[:160], exc)]
    if not rows:
        return ["no monitor samples"]
    for a, b in zip(rows, rows[1:]):
        if not b[0] > a[0]:
            return ["monitor timestamps not strictly increasing"]
    why = []
    now = time.time()
    t_last, free_last = rows[-1]
    if not (0 <= now - t_last <= 30):
        why.append(f"monitor last sample age {now - t_last:.1f}s outside [0,30]")
    win = [r for r in rows if now - 300 <= r[0] <= now]
    if len(win) < 25:
        why.append(f"only {len(win)} samples in [now-300, now]")
    elif win[-1][0] - win[0][0] < 280:
        why.append(f"window span {win[-1][0] - win[0][0]:.1f}s < 280 s")
    if free_last < 13_500_000_000 + projected:
        why.append(f"last free {free_last} < 13.5e9 + projected {projected}")
    allowed = max(300_000_000, (free_last - 13_500_000_000) // 12)
    peak, drop = None, 0
    for _, fr in win:
        peak = fr if peak is None else max(peak, fr)
        drop = max(drop, peak - fr)
    if drop > allowed:
        why.append(f"peak-to-later drop {drop} > allowed {allowed}")
    return why


def full_admission(projected, child_deadline):
    """Blocking part of admission (registry, monitor, statvfs, fit). Returns refusal reasons."""
    why = []
    try:
        why += registry_refusals()
        why += stability_refusals(projected)
        fb = free_bytes()
        if fb < FRESH_BASE + projected:
            why.append(f"fresh free {fb} < 12.2e9 + {projected}")
        if fb - STATE["remaining_reserve"] < FREE_FLOOR:
            why.append(f"free {fb} - remaining reservations {STATE['remaining_reserve']} < 12e9")
    except Exception as exc:
        why.append("admission exception %r" % exc)
    if child_deadline + SETTLE_TAIL > STATE["abs_end"] or child_deadline + SETTLE_TAIL + MARGIN > STATE["chunk_end"] \
            or child_deadline + SETTLE_TAIL > OWNED_SETTLED_BY - 180:
        why.append("per-child chunk fit / absolute end (with full settlement tail)")
    return why


def buffer_charge():
    """S5: bytes retained by unreleased proof buffers, charged in full to the lane RSS trip."""
    return sum(b.retained for b in list(LIVE_BUFFERS) if not b.released)


class ProofBuffer:
    """S1: owned FIFO reader retaining the proof in RAM only (immutable FEED_BLOCK blocks) with a HARD byte cap;
    bytes and SHA-256 are measured as they arrive from the producer; nothing is written to disk."""

    def __init__(self, fifo_path, cap):
        if os.path.lexists(fifo_path):
            raise RuntimeError("proof fifo path exists")
        os.mkfifo(fifo_path, 0o600)
        self.fifo_ino = os.lstat(fifo_path).st_ino
        self.fifo_path, self.cap = fifo_path, cap
        self.blocks = []
        self.sha = hashlib.sha256()
        self.retained = self.received = self.discarded = 0
        self.over_cap = self.connected = self.eof = self.released = False
        self.error = None
        self.unblocked_by_runner = False
        self.finished = None
        LIVE_BUFFERS.append(self)
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def _run(self):
        acc = bytearray()
        try:
            fd = os.open(self.fifo_path, os.O_RDONLY)  # blocks until a writer opens the FIFO
            self.connected = True
            try:
                while True:
                    b = os.read(fd, FEED_BLOCK)
                    if not b:
                        self.eof = True
                        break
                    self.received += len(b)
                    if not self.over_cap and self.retained + len(b) <= self.cap:
                        acc += b
                        self.sha.update(b)
                        self.retained += len(b)
                        while len(acc) >= FEED_BLOCK:       # exact FEED_BLOCK blocks; the tail stays in acc
                            self.blocks.append(bytes(acc[:FEED_BLOCK]))
                            del acc[:FEED_BLOCK]
                    else:
                        self.over_cap = True       # never retain beyond the cap; drain so the producer can exit
                        self.discarded += len(b)
            finally:
                os.close(fd)
        except Exception as exc:
            self.error = repr(exc)
        finally:
            try:
                if acc:
                    self.blocks.append(bytes(acc))
            except Exception as exc:
                self.error = (self.error or "") + " tail:" + repr(exc)

    def digest(self):
        """Independent second pass over the retained RAM blocks."""
        h = hashlib.sha256()
        n = 0
        for b in self.blocks:
            h.update(b)
            n += len(b)
        return [h.hexdigest(), n]

    def finish(self):
        """After the producer is reaped: unblock a never-connected reader, bounded join; latches on an
        unsettled thread, collector I/O error, re-hash failure or a replaced FIFO; freezes the blocks."""
        if self.finished is not None:
            return self.finished
        deadline = time.time() + SINK_UNBLOCK
        while self.thread.is_alive() and not self.connected and time.time() < deadline:
            try:
                fd = os.open(self.fifo_path, os.O_WRONLY | os.O_NONBLOCK)
                self.unblocked_by_runner = True
                os.close(fd)
                break
            except OSError as exc:
                if exc.errno != errno.ENXIO:
                    self.error = (self.error or "") + " unblock:" + repr(exc)
                    break
                time.sleep(0.05)
        self.thread.join(STREAM_JOIN)
        alive = self.thread.is_alive()
        rec = {"fifo": self.fifo_path, "storage": "RAM only", "cap": self.cap, "connected": self.connected,
               "eof": self.eof, "received": self.received, "retained": self.retained, "discarded": self.discarded,
               "over_cap": self.over_cap, "error": self.error, "unblocked_by_runner": self.unblocked_by_runner,
               "thread_alive_after_join": alive, "sha256_of_retained": self.sha.hexdigest()}
        try:
            st = os.lstat(self.fifo_path)
            rec["fifo_same_inode_still_fifo"] = bool(stat.S_ISFIFO(st.st_mode) and st.st_ino == self.fifo_ino)
        except Exception as exc:
            rec["fifo_same_inode_still_fifo"] = False
            rec["fifo_check_error"] = repr(exc)
        if not rec["fifo_same_inode_still_fifo"]:
            latch("proof FIFO replaced or missing: " + self.fifo_path)
        if alive:
            latch("proof collector thread unsettled: " + self.fifo_path)
        else:
            try:
                self.blocks = tuple(self.blocks)    # frozen: the feeders share it read-only
                rec["blocks"] = len(self.blocks)
                rec["buffer_rehash"] = self.digest()
            except Exception as exc:
                rec["buffer_rehash_error"] = repr(exc)
                latch("proof buffer re-hash failed %r" % exc)
        if self.error:
            latch("proof collector I/O error %s" % self.error)
        rec["sink_settled"] = (not alive and self.error is None and "buffer_rehash" in rec
                               and rec["fifo_same_inode_still_fifo"])
        self.finished = rec
        return rec

    def release(self):
        """Drop the RAM blocks (after the last feed, or when the item ends); the charge falls to zero."""
        self.released = True
        self.blocks = ()


class Feeder:
    """S2: owned writer of a frozen RAM proof buffer into ONE checker's stdin pipe; hashes/counts exactly the
    bytes os.write() accepted.  Modes: plain; suffix (C3: SUFFIX after the proof); hold (C7b: the first write
    waits until the checker was reaped).  The runner's read end is closed right after Popen (close_read);
    the write end is closed exactly once: by the thread, or by abandon() when the thread never started."""

    def __init__(self, blocks, mode="plain"):
        if mode not in ("plain", "suffix", "hold"):
            raise RuntimeError("unknown feed mode %r" % (mode,))
        if not isinstance(blocks, tuple):
            raise RuntimeError("proof buffer not frozen")
        self.blocks, self.mode = blocks, mode
        self.expected = sum(len(b) for b in blocks)
        self.sha = hashlib.sha256()
        self.fed = self.proof_fed = 0
        self.delivery_error = self.exception = self.close_error = None
        self.hold = threading.Event()
        self.hold_released_by_event = None
        self.started = False
        self.finished = None
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.rfd, self.wfd = os.pipe()             # non-inheritable: only the checker's dup2'd stdin holds rfd

    def plan(self):
        return {"mode": self.mode, "buffer_bytes": self.expected, "blocks": len(self.blocks)}

    def close_read(self):
        fd, self.rfd = self.rfd, None
        if fd is not None:
            os.close(fd)

    def start(self):
        self.thread.start()
        self.started = True

    def abandon(self):
        """Never-started feeder: close whichever pipe ends are still open."""
        for name in ("rfd", "wfd"):
            fd = getattr(self, name)
            setattr(self, name, None)
            if fd is not None:
                try:
                    os.close(fd)
                except OSError as exc:
                    self.close_error = repr(exc)

    def _deliver(self, data):
        mv, off = memoryview(data), 0
        while off < len(mv):
            try:
                n = os.write(self.wfd, mv[off:off + WRITE_SLICE])
            except OSError as exc:
                self.delivery_error = "%s after %d fed bytes" % (
                    "EPIPE" if isinstance(exc, BrokenPipeError) else repr(exc), self.fed)
                return off, False
            self.sha.update(mv[off:off + n])
            off += n
            self.fed += n
        return off, True

    def _run(self):
        try:
            if self.mode == "hold":
                self.hold_released_by_event = self.hold.wait(HOLD_SECONDS)
            ok = True
            for b in self.blocks:
                k, ok = self._deliver(b)
                self.proof_fed += k
                if not ok:
                    break
            if ok and self.mode == "suffix":
                self._deliver(SUFFIX)
        except Exception as exc:
            self.exception = repr(exc)
        finally:
            fd, self.wfd = self.wfd, None
            if fd is not None:
                try:
                    os.close(fd)                   # EOF for the checker
                except OSError as exc:
                    self.close_error = repr(exc)

    def finish(self, timeout):
        """After the checker is reaped: release a held feed, bounded join, record; drops the shared blocks."""
        if self.finished is not None:
            return self.finished
        if self.started:
            self.hold.set()
            self.thread.join(timeout)
        alive = self.started and self.thread.is_alive()
        self.finished = {"mode": self.mode, "started": self.started, "buffer_bytes": self.expected,
                         "fed_bytes": self.fed, "fed_sha256": self.sha.hexdigest(), "proof_bytes_fed": self.proof_fed,
                         "undelivered_proof_bytes": self.expected - self.proof_fed,
                         "delivery_error": self.delivery_error, "exception": self.exception,
                         "close_error": self.close_error, "hold_released_by_event": self.hold_released_by_event,
                         "thread_alive_after_join": alive}
        if not alive:
            self.blocks = ()
        return self.finished


def new_filter():
    """S3: per-checker capture-filter state."""
    return {"raw_sha": hashlib.sha256(), "raw_bytes": 0, "raw_eof": False, "pending": b"", "header_clauses": None,
            "dup_low": 0, "dup_high": 0, "dup_bytes": 0, "tail": 0}


class Child:
    """One owned native child: pre-allocated ownership, own session, HARD capped capture, records."""

    def __init__(self, argv, label, wall, reserve, inputs, sink, cwd, feeder=None):
        STATE["seq"] += 1
        self.seq = STATE["seq"]
        self.argv, self.label, self.sink_obj, self.cwd = argv, label, sink, cwd
        self.feeder = feeder                       # S2: owned stdin feeder (checker children only)
        self.filt = None if feeder is None else new_filter()  # S3
        base = os.path.join(STATE["out"], "children", "%02d-%s" % (self.seq, label))
        self.out_path, self.launch_path, self.settle_path = base + ".out", base + ".launch.json", base + ".settle.json"
        self.quarantine_path = base + ".QUARANTINE.json"
        self.captured, self.over_cap, self.reader_error = 0, False, None
        self.term_sent_at, self.stop, self.reader, self.settled_rec = None, None, None, None
        self.identity_at_start, self.descendants = None, []
        self.inputs, self.reserve = inputs, reserve
        self.proc, self.pid, self.pgid, self.started = None, None, None, None
        self.quarantined, self.refused = False, None
        self.quarantine_receipt_state = "none"
        self.lane_before = None
        self.capture = open(self.out_path, "xb")  # outputs prepared BEFORE admission and spawn
        child_env = dict(CHILD_ENV, TMPDIR=cwd)   # r4#5: private TMPDIR inside the run tree
        if sink is not None:
            self.lane_before = lane_files()        # r4#3: blocking census BEFORE final admission
        now = time.time()
        self.deadline = min(now + wall + GRACE, STATE["abs_end"] - SETTLE_TAIL)
        why = full_admission(reserve, self.deadline)
        if why:
            self.capture.close()
            self.refused = why
            return
        OWNED.append(self)  # r3#1: ownership exists before the process does
        # r4#3: final non-blocking checks, immediately followed by Popen.
        if LATCH or cancelled() or time.time() + wall > self.deadline:
            OWNED.remove(self)
            self.capture.close()
            self.refused = ["final pre-spawn check: latch=%r cancel=%r deadline_close=%r"
                            % (bool(LATCH), cancelled(), time.time() + wall > self.deadline)]
            return
        self.proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL if feeder is None else feeder.rfd,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     start_new_session=True, close_fds=True, cwd=cwd, env=child_env)
        try:
            if feeder is not None:
                feeder.close_read()                # S2: from here only the checker holds the read end
            self.pid = self.pgid = self.proc.pid
            self.started = time.time()
            self.identity_at_start = identity_checked(self.pid, os.getpid())
            write_x(self.launch_path, {"seq": self.seq, "label": label, "runner_pid": os.getpid(), "pid": self.pid,
                                       "pgid": self.pgid, "identity": self.identity_at_start, "argv": argv,
                                       "cwd": cwd, "start_epoch": self.started,
                                       "absolute_deadline_epoch": self.deadline, "capture": self.out_path,
                                       "capture_cap": LOG_CAP, "retained_reservation_bytes": reserve,
                                       "inputs": inputs, "run_launch_record": STATE["run_record"],
                                       "go": STATE["go"], "runner_sha256": STATE["runner_sha"],
                                       "binaries": {"kissat": KISSAT, "checkers": CHECKERS},
                                       "stdin_feed": None if feeder is None else feeder.plan()})
            print("CHILD_LAUNCH", self.launch_path, flush=True)
            self.reader = threading.Thread(target=self._read, daemon=True)
            self.reader.start()
            if feeder is not None:
                feeder.start()
        except BaseException as exc:
            if self.stop is None:
                self.stop = "registration_failure"   # r4#1: emergency stop state before fallible logging
            try:
                latch("post-Popen registration failure %r" % (exc,))
            except BaseException:
                pass
            self.reap_robust()
            raise

    def _keep(self, b):
        room = LOG_CAP - self.captured
        if room > 0:
            self.capture.write(b[:room])
        self.captured += len(b)
        if self.captured > LOG_CAP:
            self.over_cap = True

    def _read(self):
        """Capped capture.  S3: for a checker child the raw stream is hashed/counted in-stream and ONLY lines
        that fullmatch DUP_LINE are dropped (counted by phase and bytes); every other byte is kept."""
        f = self.filt
        try:
            while True:
                b = self.proc.stdout.read1(65536)
                if not b:
                    if f is not None:
                        f["raw_eof"] = True
                    break
                if f is None:
                    self._keep(b)
                    continue
                f["raw_sha"].update(b)
                f["raw_bytes"] += len(b)
                parts = (f["pending"] + b).split(b"\n")
                f["pending"] = parts.pop()
                for ln in parts:
                    ln += b"\n"
                    m = DUP_LINE.fullmatch(ln)
                    if m is None:
                        hm = PARSE_LINE.fullmatch(ln)
                        if hm is not None and f["header_clauses"] is None:
                            f["header_clauses"] = int(hm.group(2))
                        self._keep(ln)
                        continue
                    f["dup_bytes"] += len(ln)
                    if f["header_clauses"] is not None and int(m.group(3)) <= f["header_clauses"]:
                        f["dup_low"] += 1
                    else:
                        f["dup_high"] += 1
                if len(f["pending"]) > PENDING_MAX:
                    self._keep(f["pending"])
                    f["pending"] = b""
            if f is not None and f["pending"]:
                f["tail"] = len(f["pending"])
                self._keep(f["pending"])
                f["pending"] = b""
        except Exception as exc:
            self.reader_error = repr(exc)
        finally:
            try:
                self.capture.flush()
                os.fsync(self.capture.fileno())
                self.capture.close()
                self.proc.stdout.close()
            except Exception as exc:
                self.reader_error = (self.reader_error or "") + " close:" + repr(exc)

    def alive(self):
        return self.proc.poll() is None

    def term(self, reason):
        if self.term_sent_at is None and self.proc.returncode is None:
            if self.stop is None:
                self.stop = reason
            ts = time.time()                        # r5#2: computed before delivery
            self.proc.send_signal(signal.SIGTERM)   # Popen polls first; never signals a reaped PID
            self.term_sent_at = ts                  # stored immediately after send_signal returns

    def reap_robust(self):
        """r3#1/r4#1: exception-resistant reap state machine.  The whole retry path is protected; it
        polls (never blocks) so a pending quarantine receipt keeps being retried; a SIGTERM is (re)tried
        only while undelivered and only if termination was requested; it returns only after the retained
        Popen is reaped."""
        attempts = 0
        while True:
            try:
                if self.stop is not None and self.term_sent_at is None and self.proc.returncode is None:
                    ts = time.time()                       # r5#2
                    self.proc.send_signal(signal.SIGTERM)
                    self.term_sent_at = ts
                if self.term_sent_at is not None and not self.quarantined and self.proc.poll() is None \
                        and time.time() >= self.term_sent_at + TERM_WAIT:
                    self.quarantined = True
                    self.quarantine_receipt_state = "pending"
                    try:
                        latch("quarantine pid %d" % self.pid)
                    except BaseException:
                        pass
                if self.quarantine_receipt_state == "pending":
                    attempts += 1
                    try:
                        write_x(self.quarantine_path, {"pid": self.pid, "pgid": self.pgid, "argv": self.argv,
                                                       "epoch": time.time(), "note": "survived SIGTERM + 60 s; "
                                                       "no further signal; runner keeps waiting"})
                        self.quarantine_receipt_state = "written"
                    except FileExistsError:                # r5#3: validate, never assume
                        self.quarantine_receipt_state = "written" if self._receipt_valid() else "failed"
                    except BaseException:
                        if attempts >= 20:                 # r5#4: bounded publication attempts
                            self.quarantine_receipt_state = "failed"
                rc = self.proc.poll()
                if rc is not None:
                    return self.proc.wait()                # r5#4: reaped -> leave; receipt state is settled later
                time.sleep(0.1)
            except BaseException:
                try:
                    time.sleep(0.05)
                except BaseException:
                    pass

    def _receipt_valid(self):
        try:
            with open(self.quarantine_path, "rb") as f:
                d = json.loads(f.read())
            return isinstance(d, dict) and d.get("pid") == self.pid and "note" in d
        except BaseException:
            return False

    def census(self):
        """Other processes with ppid==child or pgid==child (excluding the child itself)."""
        rows = ps_table()
        found = [r for r in rows if r[0] != self.pid and (r[1] == self.pid or r[2] == self.pgid)]
        rss = sum(r[3] for r in rows if r[0] == self.pid or r in found) * 1024
        return found, rss

    def settle(self):
        """Always reaches wait(); settlement final only after streams, sink, FIFO/cwd/lane checks,
        hashes and the receipt; any failure clears 'settled' and latches."""
        if self.settled_rec is not None:
            return self.settled_rec
        problems = []
        rc = self.reap_robust()
        if self.quarantined and self.quarantine_receipt_state != "written":
            problems.append("quarantine receipt not published (%s)" % self.quarantine_receipt_state)
        stream_alive = None
        if self.reader is not None and self.reader.ident is not None:
            self.reader.join(STREAM_JOIN)
            stream_alive = self.reader.is_alive()
        else:
            problems.append("no started capture reader")  # r6#2: explicit settlement failure
            try:
                self.proc.stdout.close()
            except Exception as exc:
                problems.append("stdout close %r" % exc)
            try:
                self.capture.close()
            except Exception as exc:
                problems.append("capture close %r" % exc)
        feed_rec = filt_rec = None
        if self.feeder is not None:   # S2: the checker is reaped, so a held feed now meets a closed read end
            try:
                feed_rec = self.feeder.finish(STREAM_JOIN)
                if not feed_rec["started"] or feed_rec["thread_alive_after_join"]:
                    problems.append("stdin feeder not started or unsettled")
                if feed_rec["exception"] is not None or feed_rec["close_error"] is not None:
                    problems.append("stdin feeder exception/close error")
            except BaseException as exc:
                problems.append("feeder finish failed %r" % exc)
            if stream_alive is False:
                f = self.filt
                filt_rec = {"raw_bytes": f["raw_bytes"], "raw_sha256": f["raw_sha"].hexdigest(), "raw_eof": f["raw_eof"],
                            "header_clauses": f["header_clauses"], "dup_bytes_dropped": f["dup_bytes"],
                            "dup_lines_at_or_below_header_clauses": f["dup_low"],
                            "dup_lines_above_header_clauses": f["dup_high"], "kept_bytes": self.captured,
                            "unterminated_tail_bytes": f["tail"]}
        group_empty = None
        try:
            os.killpg(self.pgid, 0)
            group_empty = False
        except ProcessLookupError:
            group_empty = True
        except BaseException as exc:
            problems.append("killpg probe %r" % exc)
        try:
            after, _ = self.census()
            if after:
                problems.append("descendants after reap %r" % after)
        except BaseException as exc:
            problems.append("post-reap census failed %r" % exc)
        if self.descendants:
            problems.append("descendants seen during run %r" % self.descendants[:5])
        sink_rec = None
        if self.sink_obj is not None:
            try:
                sink_rec = self.sink_obj.finish()
                if not sink_rec["sink_settled"]:
                    problems.append("proof sink not settled")
            except BaseException as exc:
                problems.append("sink finish failed %r" % exc)
        try:
            if os.listdir(self.cwd):
                problems.append("child cwd not empty: %r" % os.listdir(self.cwd)[:10])
        except BaseException as exc:
            problems.append("cwd check failed %r" % exc)
        if self.lane_before is not None:
            try:
                expected = {self.out_path, self.launch_path, self.settle_path, self.quarantine_path}  # S1: no proof file
                now = lane_files()
                unexpected = [p for p, v in now.items()
                              if p not in expected and (p not in self.lane_before or self.lane_before[p] != v)]
                if unexpected:
                    problems.append("unexpected lane file changes %r" % unexpected[:10])
            except BaseException as exc:
                problems.append("lane census failed %r" % exc)
        diag = []
        out_sha = None
        if stream_alive is False:
            try:
                out_sha = sha_file(self.out_path)[0]
                with open(self.out_path, "rb") as f:
                    diag = sorted(set(m.group(0) for m in RESOURCE_DIAG.finditer(f.read().decode("utf-8", "replace"))))
            except BaseException as exc:
                problems.append("capture hash/scan failed %r" % exc)
        if diag:
            latch("native memory diagnostic in %s: %r" % (self.label, diag))  # r3#3
        rec = {"seq": self.seq, "label": self.label, "pid": self.pid, "pgid": self.pgid,
               "identity_at_start": self.identity_at_start, "argv": self.argv, "returncode": rc,
               "stop": self.stop or "self", "seconds": round(time.time() - self.started, 3),
               "captured_bytes": self.captured, "capture_over_cap": self.over_cap, "reader_error": self.reader_error,
               "stream_thread_alive_after_join": stream_alive, "group_empty_after_reap": group_empty,
               "quarantined": self.quarantined, "problems": problems, "resource_diagnostics": diag,
               "proof_sink": sink_rec, "stdin_feed": feed_rec, "stdout_filter": filt_rec,
               "launch_record": self.launch_path, "output_path": self.out_path,
               "output_sha256": out_sha, "settled": False}
        ok = (stream_alive is False and group_empty is True and not self.quarantined and not problems
              and self.reader_error is None and out_sha is not None)
        try:
            write_x(self.settle_path, dict(rec, settled=ok))
            rec["settled"] = ok
        except BaseException as exc:
            rec["settle_receipt_error"] = repr(exc)
        if not rec["settled"]:
            latch("child %d %s not settled" % (self.seq, self.label))
        self.settled_rec = rec
        return rec


def segments(path):
    with open(path, "rb") as f:
        txt = f.read().decode("utf-8", "replace")
    return [s for s in re.split(r"[\r\n]", txt) if s != ""]


def supervise(child, sink):
    """Monitor until exit or a single trip; any monitor exception is itself a trip."""
    me = os.getpid()
    last_rss = last_reg = 0.0
    peak = 0
    while child.alive():
        try:
            now = time.time()
            if cancelled():
                child.term("owner_cancel_sigterm")
            elif now > child.deadline:
                child.term("absolute_or_wall_deadline")
            elif sink is not None and sink.over_cap:
                child.term("proof_cap")
            elif sink is not None and sink.error:
                child.term("proof_sink_error")
            elif child.feeder is not None and child.feeder.exception is not None:
                child.term("feeder_exception")
            elif child.over_cap:
                child.term("capture_cap")
            elif free_bytes() < FREE_FLOOR:
                child.term("inflight_disk_floor")
            if child.term_sent_at is None and now - last_rss >= 1.0:
                last_rss = now
                found, rss = child.census()
                rows = ps_table()
                runner_rss = sum(r[3] for r in rows if r[0] == me) * 1024
                if found:
                    child.descendants.extend(found)
                    child.term("descendant_process")
                total = rss + max(runner_rss, buffer_charge())  # S5: the RAM proof buffer is charged in full
                peak = max(peak, total)
                if runner_rss == 0 or (rss == 0 and child.alive()):
                    child.term("rss_unreadable")
                elif total > LANE_RSS_TRIP:
                    child.term("lane_rss")
            if child.term_sent_at is None and now - last_reg >= 5.0:
                last_reg = now
                if registry_refusals():
                    child.term("stop_registry")
        except Exception as exc:
            child.term("monitor_exception:%r" % exc)
        if child.term_sent_at is not None:
            break
        time.sleep(0.25)
    if child.stop is not None and child.stop not in NONLATCHING_TRIPS:
        latch("trip %s on %s" % (child.stop, child.label))
    return child.stop, peak


def run_child(argv, label, wall, reserve, inputs, sink=None, feeder=None):
    """Prepared outputs -> admission -> spawn -> supervise -> settle.  Returns (rec|None, lines, refusal)."""
    ch = None
    try:
        cwd = os.path.join(STATE["out"], "cwd", "%02d-%s" % (STATE["seq"] + 1, label))
        os.makedirs(cwd)  # r4#4: inside the cleanup guard
        ch = Child(argv, label, wall, reserve, inputs, sink, cwd, feeder)
        if ch.refused:
            return None, [], ch.refused
        peak = None
        try:
            if cancelled():
                ch.term("owner_cancel_sigterm")
            _, peak = supervise(ch, sink)
        except BaseException as exc:
            latch("runner exception during supervision %r" % exc)
            ch.term("runner_exception")
        rec = ch.settle()
        rec["trip"] = ch.stop
        rec["peak_sampled_lane_rss_bytes"] = peak
        lines = segments(ch.out_path) if rec.get("stream_thread_alive_after_join") is False else []
        return rec, lines, []
    finally:
        settle_all()
        if sink is not None and (ch is None or ch.proc is None):
            sink.finish()  # never-spawned producer: unblock and join the reader
        if feeder is not None and not feeder.started:
            feeder.abandon()  # S2: never-spawned checker or never-started feeder: close both pipe ends


def settle_all():
    """r6#1/#2: index iteration entirely inside the retry guard; an unreaped child is retried forever
    (never abandoned); a reaped child whose settlement bookkeeping keeps failing is recorded UNSETTLED
    with the latch held after 20 attempts."""
    i = 0
    failures = 0
    while True:
        try:
            if i >= len(OWNED):
                return
            c = OWNED[i]
            if c.proc is not None and c.settled_rec is None:
                if c.stop is None:
                    c.stop = "runner_escape_cleanup"  # emergency stop without polling first
                try:
                    c.settle()
                except BaseException:
                    failures += 1
                    if c.proc.returncode is not None and failures >= 20:
                        c.settled_rec = {"seq": c.seq, "label": c.label, "pid": c.pid, "settled": False,
                                         "returncode": c.proc.returncode, "stop": c.stop,
                                         "note": "settlement bookkeeping failed after reap"}
                        LATCH.append("child settlement bookkeeping failed after reap")
                    continue
            i += 1
            failures = 0
        except BaseException:
            continue


def run_kissat(cnf_path, label, seconds, cap, reserve, inputs):
    """kissat -q -f --seed=1 --time=S CNF [PROOF_FIFO]; with a cap the proof goes ONLY to a RAM ProofBuffer (S1).
    Returns (rec|None, lines, refusal, buffer|None)."""
    argv = [KISSAT[0], "-q", "-f", "--seed=1", "--time=%d" % seconds, cnf_path]
    sink = None
    if cap is not None:
        fifo_dir = os.path.join(STATE["out"], "fifo")
        os.makedirs(fifo_dir, exist_ok=True)
        sink = ProofBuffer(os.path.join(fifo_dir, label + ".proof.fifo"), cap)
        argv.append(sink.fifo_path)
    rec, lines, refused = run_child(argv, label + ".kissat", seconds, reserve,
                                    dict(inputs, proof_storage=None if sink is None else "RAM only", proof_cap=cap),
                                    sink)
    return rec, lines, refused, sink


def run_check(cnf_path, buf, checker, label, seconds, reserve, inputs, mode="plain"):
    """S2: one pinned checker [DRAT_X, CNF, -i, -t S] with the frozen RAM buffer on stdin via an owned Feeder;
    the binary is re-hashed immediately before the spawn."""
    name, path, pin = checker
    if sha_file(path)[0] != pin:
        latch("checker %s binary pin mismatch at spawn" % name)
        raise RuntimeError("checker %s binary pin mismatch" % name)
    if buf.released:
        raise RuntimeError("proof buffer already released")
    feeder = Feeder(buf.blocks, mode)
    return run_child([path, cnf_path, "-i", "-t", str(seconds)], "%s.drat%s" % (label, name), seconds, reserve,
                     dict(inputs, cnf=cnf_path, checker=[name, path, pin], proof_source="RAM buffer on stdin",
                          feed_mode=mode), feeder=feeder)


def sink_complete(sink_rec):
    return (sink_rec is not None and sink_rec.get("sink_settled") and sink_rec["connected"] and sink_rec["eof"]
            and not sink_rec["over_cap"] and sink_rec["error"] is None and not sink_rec["unblocked_by_runner"]
            and sink_rec["discarded"] == 0 and sink_rec["received"] == sink_rec["retained"]
            and sink_rec.get("buffer_rehash") == [sink_rec["sha256_of_retained"], sink_rec["retained"]])


def status_lines(lines):
    return [s[:200] for s in lines if s.startswith("s ")][:8]


def checker_defects(name, cnf_expect, buf_sha, buf_bytes, drat_rec, drat_lines):
    """S4: per-checker P-STREAM qualification; every defect names the checker."""
    bad = []
    feed = drat_rec.get("stdin_feed") or {}
    filt = drat_rec.get("stdout_filter") or {}
    if drat_rec["returncode"] != 0 or drat_rec["stop"] != "self":
        bad.append("checker not self-exit rc0")
    if status_lines(drat_lines) != ["s VERIFIED"]:
        bad.append("checker status lines not exactly ['s VERIFIED']")
    v, c = cnf_expect[2].split()[2:4]
    if ("c parsing input formula with %s variables and %s clauses" % (v, c)) not in drat_lines:
        bad.append("checker parse header line missing/mismatched")
    if STDIN_LINE not in drat_lines:
        bad.append("checker did not report reading the proof from stdin")
    if feed.get("mode") != "plain":
        bad.append("feed mode is not plain")
    if feed.get("fed_bytes") != buf_bytes or feed.get("fed_sha256") != buf_sha or feed.get("proof_bytes_fed") != buf_bytes:
        bad.append("fed bytes/SHA-256 != collected proof buffer")
    if feed.get("started") is not True or feed.get("delivery_error") is not None or feed.get("exception") is not None \
            or feed.get("close_error") is not None or feed.get("thread_alive_after_join") is not False:
        bad.append("stdin feed incomplete, failed or unsettled")
    fb = feed.get("fed_bytes")
    if not isinstance(fb, int) or ("c finished parsing, read %d bytes from proof file" % fb) not in drat_lines:
        bad.append("checker-consumed proof bytes != fed bytes")
    if filt.get("raw_eof") is not True or not isinstance(filt.get("dup_bytes_dropped"), int) \
            or filt.get("raw_bytes") != drat_rec["captured_bytes"] + filt["dup_bytes_dropped"]:
        bad.append("checker output filter accounting mismatch")
    for pat in ("early EOF", "clauses less than expected", "trivial UNSAT", "ERROR", "MEMOUT",
                "wrong binary prefix", "no empty clause detected", "NOT VERIFIED", "TIMEOUT",
                "illegal literal", "error opening", "failed to reallocate"):
        if any(pat in s for s in drat_lines):
            bad.append("checker output contains %r" % pat)
    if not drat_rec["settled"] or drat_rec["capture_over_cap"]:
        bad.append("settlement/capture defect seq %s" % drat_rec["seq"])
    return ["checker %s: %s" % (name, b) for b in bad]


def qualify_stream(cnf_expect, solver_rec, kissat_lines, proof_cap, checks, cnf_post, buf_post):
    """S4: item-level qualification over the solver leg, the RAM buffer and every pinned checker in order;
    checks = [(name, drat_rec, drat_lines), ...].  UNSAT requires the empty list."""
    bad = []
    if solver_rec["returncode"] != 20 or solver_rec["stop"] != "self":
        bad.append("solver not self-exit rc20")
    if status_lines(kissat_lines) != ["s UNSATISFIABLE"]:
        bad.append("solver status lines not exactly ['s UNSATISFIABLE']")
    buf = solver_rec.get("proof_sink") or {}
    if not sink_complete(solver_rec.get("proof_sink")):
        bad.append("proof buffer incomplete/over cap/error")
    buf_sha, buf_bytes = buf.get("sha256_of_retained"), buf.get("retained")
    if not isinstance(buf_bytes, int) or buf_bytes <= 0 or buf_bytes > proof_cap:
        bad.append("proof size outside (0, cap]")
    if [c[0] for c in checks] != [c[0] for c in CHECKERS]:
        bad.append("not every pinned checker ran, in order")
    for name, rec, lines in checks:
        bad += checker_defects(name, cnf_expect, buf_sha, buf_bytes, rec, lines)
    if cnf_post != (cnf_expect[0], cnf_expect[1]):
        bad.append("CNF file digest/bytes != expected")
    if buf_post != [buf_sha, buf_bytes]:
        bad.append("proof buffer re-hash after the checks != collector measurement")
    if not solver_rec["settled"] or solver_rec["capture_over_cap"]:
        bad.append("settlement/capture defect seq %s" % solver_rec["seq"])
    return bad


def verify_sat(cnf_path, kissat_lines, label):
    """Two independent checks of a SAT model: clause satisfaction and both PA19 definitions."""
    lits = set()
    for s in kissat_lines:
        if s.startswith("v "):
            lits.update(int(x) for x in s[2:].split() if x != "0")
    sat_all = True
    with open(cnf_path, "rb") as f:
        for ln in f:
            if ln.startswith(b"p") or ln.startswith(b"c"):
                continue
            cl = [int(x) for x in ln.split()[:-1]]
            if not any(l in lits for l in cl):
                sat_all = False
                break
    A = [[None] * 8 for _ in range(19)]
    cells_ok = True
    for r in range(19):
        for c in range(8):
            ss = [s for s in range(6) if (1 + 48 * r + 6 * c + s) in lits]
            if len(ss) != 1:
                cells_ok = False
            else:
                A[r][c] = ss[0]
    rowpair_ok = cells_ok and all(sum(A[r][c] == A[q][c] for c in range(8)) <= 1
                                  for r in range(19) for q in range(r + 1, 19))
    colpair_ok = cells_ok and all(len({(A[r][c], A[r][d]) for r in range(19)}) == 19
                                  for c in range(8) for d in range(c + 1, 8))
    cand = os.path.join(STATE["out"], label + ".SAT-CANDIDATE.json")
    write_x(cand, {"host_clock": clock(), "array": A, "clauses_all_satisfied": sat_all,
                   "cells_exactly_one": cells_ok, "row_pair_agreements_le_1": rowpair_ok,
                   "column_pair_ordered_pairs_distinct": colpair_ok,
                   "status": "CANDIDATE_UNVERIFIED - notify parent immediately"})
    latch_path = os.path.join(LANE, "control", "SAT-CANDIDATE-" + label)
    write_bytes_x(latch_path, cand.encode())
    return {"candidate": cand, "latch": latch_path, "clauses_all_satisfied": sat_all, "cells": cells_ok,
            "rowpair": rowpair_ok, "colpair": colpair_ok}


def php_cnf(p, h):
    """Pigeonhole: p pigeons into h holes; UNSAT iff p > h."""
    var = lambda i, j: i * h + j + 1  # noqa: E731
    cl = [[var(i, j) for j in range(h)] for i in range(p)]
    for j in range(h):
        for i in range(p):
            for k in range(i + 1, p):
                cl.append([-var(i, j), -var(k, j)])
    return ("p cnf %d %d\n" % (p * h, len(cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cl)).encode()


def healthy(rec):
    """A control child must have exited by itself (rc>=0), with no trip, fully settled, no resource diag."""
    return rec is not None and rec["stop"] == "self" and rec["settled"] and not rec["capture_over_cap"] \
        and rec["returncode"] is not None and rec["returncode"] >= 0 and not rec["resource_diagnostics"]


def completed_checker(rec, lines, expect):
    """r3#8: a completed drat-trim outcome: exactly 's VERIFIED' rc0 or 's NOT VERIFIED' rc1, no
    MEMOUT/TIMEOUT/ERROR text, healthy settlement."""
    st = status_lines(lines)
    if not healthy(rec) or any(p in s for s in lines for p in ("MEMOUT", "TIMEOUT", "ERROR")):
        return False
    if expect == "VERIFIED":
        return st == ["s VERIFIED"] and rec["returncode"] == 0
    return st == ["s NOT VERIFIED"] and rec["returncode"] == 1


def controls():
    """S6: same-binary positive and intended-reason controls through the RAM/stdin transport for BOTH pinned
    checkers; stops at the first refused, unhealthy or not-as-intended control (later controls are not started)."""
    recs = {}
    d = os.path.join(STATE["out"], "controls")
    os.mkdir(d)
    per_child = LOG_CAP + 3 * RECORD_MAX

    def fail(name, why):
        recs[name] = dict(recs.get(name, {}), failed=why)
        return False, recs

    def both(tag, cnf_path, pins, buf, mode):
        out = []
        for chk in CHECKERS:
            dr, dl, rf = run_check(cnf_path, buf, chk, tag, CONTROL_CHILD_WALL, per_child, pins, mode)
            if dr is None:
                return out, "checker %s refused %r" % (chk[0], rf)
            out.append((chk[0], dr, dl))
        return out, None

    def view(checks):
        return {n: {"drat": r, "checker_status_lines": status_lines(l)} for n, r, l in checks}

    raw = php_cnf(6, 5)
    cnf = os.path.join(d, "php6x5.cnf")
    h, n = write_bytes_x(cnf, raw)
    exp = (h, n, raw.split(b"\n", 1)[0].decode())
    ks, kl, rf, b1 = run_kissat(cnf, "C1", CONTROL_CHILD_WALL, CONTROL_PROOF_CAP, per_child, {"cnf_pin": [h, n]})
    if ks is None:
        return fail("C1_positive_php6x5", "refused %r" % rf)
    recs["C1_positive_php6x5"] = {"kissat": ks}
    if not (healthy(ks) and sink_complete(ks["proof_sink"])):
        return fail("C1_positive_php6x5", "solver leg unhealthy or proof buffer incomplete")
    ph, pn = ks["proof_sink"]["sha256_of_retained"], ks["proof_sink"]["retained"]
    pins = {"cnf_pin": [h, n], "proof_pin": [ph, pn]}
    c1k, why = both("C1", cnf, pins, b1, "plain")
    if why:
        return fail("C1_positive_php6x5", why)
    c1 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c1k, sha_file(cnf), b1.digest())
    recs["C1_positive_php6x5"].update(intended="PASS through checker A and checker B", defects=c1, checkers=view(c1k))
    if c1 != [] or not all(completed_checker(r, l, "VERIFIED") for _, r, l in c1k):
        return fail("C1_positive_php6x5", "positive control did not pass")
    # C2 (deterministic): well-formed CNF, same header and clause count, first clause missing one literal.
    lines = raw.split(b"\n")
    first = lines[1].split()
    mutated = b"\n".join([lines[0], b" ".join(first[:-2] + first[-1:])] + lines[2:])
    cnf2 = os.path.join(d, "php6x5-one-literal-removed.cnf")
    h2, n2 = write_bytes_x(cnf2, mutated)
    c2k, why = both("C2", cnf2, {"cnf_pin": [h2, n2], "proof_pin": [ph, pn]}, b1, "plain")
    if why:
        return fail("C2_mutated_cnf_digest", why)
    c2 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c2k, sha_file(cnf2), b1.digest())
    recs["C2_mutated_cnf_digest"] = {"intended": "REJECT with 'CNF file digest/bytes != expected'; both checkers "
                                                 "completed", "defects": c2, "checkers": view(c2k)}
    if not (all(completed_checker(r, l, "VERIFIED") or completed_checker(r, l, "NOT VERIFIED") for _, r, l in c2k)
            and "CNF file digest/bytes != expected" in c2):
        return fail("C2_mutated_cnf_digest", "intended reason or completed checker missing")
    # C3: the valid proof + one trailing byte appended IN TRANSIT: completed 's VERIFIED' yet rejected.
    c3k, why = both("C3", cnf, pins, b1, "suffix")
    if why:
        return fail("C3_trailing_proof_byte", why)
    c3 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c3k, sha_file(cnf), b1.digest())
    recs["C3_trailing_proof_byte"] = {"intended": "per checker: completed 's VERIFIED' but REJECT: feed mode, fed != "
                                                  "buffer, consumed != fed and 'wrong binary prefix'",
                                      "defects": c3, "checkers": view(c3k)}
    for name, r, l in c3k:
        want = ["checker %s: %s" % (name, w) for w in ("feed mode is not plain",
                                                       "fed bytes/SHA-256 != collected proof buffer",
                                                       "checker-consumed proof bytes != fed bytes",
                                                       "checker output contains 'wrong binary prefix'")]
        if not (completed_checker(r, l, "VERIFIED") and all(w in c3 for w in want)
                and (r.get("stdin_feed") or {}).get("fed_bytes") == pn + len(SUFFIX)):
            return fail("C3_trailing_proof_byte", "intended reason or completed checker missing (%s)" % name)
    # C4: satisfiable PHP(5,5) with the PHP(6,5) proof: each checker completed 's NOT VERIFIED' rc1.
    raw4 = php_cnf(5, 5)
    cnf4 = os.path.join(d, "php5x5-sat.cnf")
    h4, n4 = write_bytes_x(cnf4, raw4)
    c4k, why = both("C4", cnf4, {"cnf_pin": [h4, n4], "proof_pin": [ph, pn]}, b1, "plain")
    if why:
        return fail("C4_sat_formula_foreign_proof", why)
    recs["C4_sat_formula_foreign_proof"] = {"intended": "each checker completed exactly ['s NOT VERIFIED'] rc1",
                                            "checkers": view(c4k)}
    if not all(completed_checker(r, l, "NOT VERIFIED") for _, r, l in c4k):
        return fail("C4_sat_formula_foreign_proof", "intended reason or completed checker missing")
    # C5: HARD RAM proof cap 4096 B on PHP(11,10): never retains beyond 4096, trip proof_cap, settled.
    raw5 = php_cnf(11, 10)
    cnf5 = os.path.join(d, "php11x10.cnf")
    h5, n5 = write_bytes_x(cnf5, raw5)
    ks5, kl5, rf, b5 = run_kissat(cnf5, "C5", CONTROL_CHILD_WALL, 4096, per_child, {"cnf_pin": [h5, n5]})
    if ks5 is None:
        return fail("C5_proof_hard_cap", "refused %r" % rf)
    b5.release()
    ps5 = ks5["proof_sink"] or {}
    recs["C5_proof_hard_cap"] = {"intended": "stop=proof_cap, buffer retained<=4096 B, settled, over_cap and joined",
                                 "kissat": ks5}
    if not (ks5["stop"] == "proof_cap" and ps5.get("retained", 4097) <= 4096 and ps5.get("over_cap")
            and ks5["settled"] and ps5.get("thread_alive_after_join") is False and not ks5["resource_diagnostics"]):
        return fail("C5_proof_hard_cap", "intended reason or settlement missing")
    # C6: kissat --time=1, no proof: clean self-exit without a verdict.
    raw6 = php_cnf(13, 12)
    cnf6 = os.path.join(d, "php13x12.cnf")
    h6, n6 = write_bytes_x(cnf6, raw6)
    ks6, kl6, rf, _ = run_kissat(cnf6, "C6", 1, None, per_child, {"cnf_pin": [h6, n6]})
    if ks6 is None:
        return fail("C6_native_time_limit", "refused %r" % rf)
    st6 = status_lines(kl6)
    recs["C6_native_time_limit"] = {"intended": "healthy self-exit, rc not 10/20, no SAT/UNSAT status line",
                                    "kissat": ks6, "status_lines": st6}
    if not (healthy(ks6) and ks6["returncode"] not in (10, 20)
            and not any(s in ("s SATISFIABLE", "s UNSATISFIABLE") for s in st6)):
        return fail("C6_native_time_limit", "intended reason or health missing")
    # C7: missing input with a RAM proof buffer: kissat self-exit rc>0 naming the path; the collector settles.
    absent = os.path.join(d, "absent.cnf")
    ks7, kl7, rf, b7 = run_kissat(absent, "C7", 10, CONTROL_PROOF_CAP, per_child, {"cnf_pin": None})
    if ks7 is None:
        return fail("C7_no_input_sink_liveness", "refused %r" % rf)
    b7.release()
    recs["C7_no_input_sink_liveness"] = {"intended": "healthy self-exit rc>0 not 10/20 mentioning absent.cnf; "
                                                     "collector joined", "kissat": ks7}
    if not (healthy(ks7) and ks7["returncode"] not in (0, 10, 20) and any("absent.cnf" in s for s in kl7)
            and ks7["proof_sink"]["thread_alive_after_join"] is False):
        return fail("C7_no_input_sink_liveness", "intended reason or settlement missing")
    # C7b: missing CNF for each checker with a HELD feed: the checker exits before reading stdin, the feeder
    # then meets a closed read end (EPIPE, 0 bytes fed), every thread settles, nothing hangs.
    absent2 = os.path.join(d, "absent-checker.cnf")
    c7k, why = both("C7b", absent2, {"cnf_pin": None, "proof_pin": [ph, pn]}, b1, "hold")
    b1.release()
    if why:
        return fail("C7b_checker_no_input_feed_liveness", why)
    recs["C7b_checker_no_input_feed_liveness"] = {"intended": "per checker: healthy self-exit rc not 0 naming "
                                                              "absent-checker.cnf; held feed EPIPE with 0 bytes fed; "
                                                              "feeder joined", "checkers": view(c7k)}
    for name, r, l in c7k:
        f7 = r.get("stdin_feed") or {}
        if not (healthy(r) and r["returncode"] != 0 and any("absent-checker.cnf" in s for s in l)
                and f7.get("fed_bytes") == 0 and str(f7.get("delivery_error")).startswith("EPIPE")
                and f7.get("hold_released_by_event") is True and f7.get("thread_alive_after_join") is False):
            return fail("C7b_checker_no_input_feed_liveness", "intended reason or settlement missing (%s)" % name)
    return True, recs


def terminal_gate():
    """Registry and disk evidence collected BEFORE the commit boundary; any failure latches."""
    why = []
    try:
        why += registry_refusals()
        if free_bytes() < FREE_FLOOR:
            why.append("free below in-flight floor at terminal gate")
    except Exception as exc:
        why.append("terminal gate exception %r" % exc)
    for w in why:
        latch("terminal gate: " + w)
    return why


def commit_record(path, rec_unknown, rec_unsat):
    """Explicit commit boundary.  Both serializations and the O_EXCL fd exist before the boundary; the
    boundary is one atomic next(ORDER); a cancel stamped before it (or any latch) forces UNKNOWN."""
    unknown_bytes = serialize(rec_unknown)
    unsat_bytes = None if rec_unsat is None else serialize(rec_unsat)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        boundary = next(ORDER)
        co = STATE["cancel_order"]
        chosen = unsat_bytes if (unsat_bytes is not None and not LATCH and (co is None or co > boundary)) else unknown_bytes
        view = memoryview(chosen)
        while view:
            k = os.write(fd, view)
            view = view[k:]
        os.fsync(fd)
    finally:
        os.close(fd)
    return {"boundary": boundary, "cancel_order": STATE["cancel_order"], "committed_unsat": chosen is unsat_bytes,
            "sha256": hashlib.sha256(chosen).hexdigest()}


def main():
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if len(sys.argv) != 4:
        print("usage: pilot_file_drat_v14.py GO.json GO_SHA256 OUT_DIR", flush=True)
        return EXIT_PRESTART_REFUSED
    go_path, go_sha, out_dir = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
    if not out_dir.startswith(LANE + "/evidence/pilot-v1/"):
        print("REFUSED: output outside LANE/evidence/pilot-v1/", flush=True)
        return EXIT_PRESTART_REFUSED
    self_sha = sha_file(os.path.abspath(__file__))[0]
    try:
        go = json.loads(read_pinned(go_path, go_sha))
        read_pinned(*BINARY_IMPORTS)
        read_pinned(*KISSAT_SOURCE)
    except Exception as exc:
        print("REFUSED: GO/evidence unreadable or pin mismatch %r" % exc, flush=True)
        return EXIT_PRESTART_REFUSED
    if go.get("runner_sha256") != self_sha or go.get("decision") != "GO" \
            or go.get("items") != [it["id"] for it in ITEMS]:
        print("REFUSED: GO record does not name this runner/items", flush=True)
        return EXIT_PRESTART_REFUSED
    t_start = time.time()
    abs_end = t_start + CONTROLS_WORST_SECONDS + len(ITEMS) * ITEM_WORST_SECONDS
    if abs_end + SETTLE + MARGIN > t_start + MAX_CHUNK or abs_end > OWNED_SETTLED_BY - 180:
        print("REFUSED: chunk-fit", flush=True)
        return EXIT_PRESTART_REFUSED
    os.mkdir(out_dir)
    os.mkdir(os.path.join(out_dir, "children"))
    os.mkdir(os.path.join(out_dir, "cwd"))
    STATE.update(out=out_dir, abs_end=abs_end, chunk_end=t_start + MAX_CHUNK,
                 remaining_reserve=RUN_RESERVE + CONTROL_RESERVE + len(ITEMS) * ITEM_RESERVE,
                 go={"path": go_path, "sha256": go_sha}, runner_sha=self_sha)
    launch = {
        "schema": "PA19-96H-PSTREAM-LAUNCH-v1", "host_clock": clock(), "owner": "ContinuePA19",
        "go": STATE["go"], "runner": {"path": os.path.abspath(__file__), "sha256": self_sha},
        "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "cwd": os.getcwd(), "argv": sys.argv,
        "python": sys.version, "binaries": {"kissat": KISSAT, "drat_trim_lane_copy": DRAT, "drat_trim_old": DRAT_OLD,
                                            "drat_trim_provenanced": DRAT_PROV, "provenance_receipt": DRAT_PROV_RECEIPT,
                                            "drat_trim_source_sha256": DRAT_SOURCE_SHA, "checkers_in_order": CHECKERS},
        "inputs": {"encoder": ENC, "skeleton": SKEL, "items": ITEMS, "registry": REGISTRY,
                   "launch_contract": LAUNCH_CONTRACT, "binary_imports": BINARY_IMPORTS,
                   "kissat_source_evidence": KISSAT_SOURCE, "monitor": MONITOR, "observer_source": OBSERVER_SOURCE_SHA},
        "absolute_end_epoch": abs_end, "max_chunk_end_epoch": t_start + MAX_CHUNK,
        "retained_output_reservation_bytes": STATE["remaining_reserve"],
        "reservation_breakdown": {"run_reserve": RUN_RESERVE, "control_reserve": CONTROL_RESERVE,
                                  "item_reserve_each": ITEM_RESERVE, "record_max": RECORD_MAX},
        "output_dir": out_dir, "children_dir": os.path.join(out_dir, "children"),
        "limits": {"solver_s": SOLVER_SECONDS, "check_s": CHECK_SECONDS, "grace_s": GRACE, "term_wait_s": TERM_WAIT,
                   "stream_join_s": STREAM_JOIN, "settle_tail_s": SETTLE_TAIL, "proof_cap_hard": PROOF_CAP,
                   "control_proof_cap_hard": CONTROL_PROOF_CAP, "log_cap_hard": LOG_CAP, "lane_rss_trip": LANE_RSS_TRIP,
                   "free_floor": FREE_FLOOR, "fresh_base": FRESH_BASE, "proof_storage": "RAM only; never written",
                   "feed_block": FEED_BLOCK, "write_slice": WRITE_SLICE, "hold_s": HOLD_SECONDS,
                   "rss_charge": "child RSS + max(runner RSS, retained proof buffer bytes)"},
        "exit_codes": {"0": "plan complete (each item terminal UNSAT/UNKNOWN); not a science verdict",
                       "10": "SAT candidate", "20": "controls failed", "30": "admission refused",
                       "40": "owner cancel", "50": "safety stop / latch / unsettled / memory diagnostic",
                       "60": "exception", "70": "prestart refused"},
    }
    run_record = os.path.join(out_dir, "launch-record.json")
    STATE["run_record"] = {"path": run_record, "sha256": write_x(run_record, launch)}
    print("LAUNCH_RECORD", run_record, flush=True)
    summary = {"schema": "PA19-96H-PSTREAM-SUMMARY-v1", "items": {}, "controls_ok": None, "stopped": None,
               "terminal_policy": "exit code reports runner execution only; per-item records carry the scientific "
                                  "status; an item counts only if qualify_stream (both pinned checkers on the same "
                                  "RAM buffer), the terminal gate and the commit boundary all pass; case closure is "
                                  "decided by the parent audit"}
    outcome = {"sat": False, "controls_failed": False, "refused": False, "exception": False, "complete": False}
    try:
        run_plan(summary, outcome)
    except BaseException as exc:
        outcome["exception"] = True
        summary["stopped"] = {"phase": "exception", "error": repr(exc)}
    finally:
        settle_all()
        code = final_code(summary, outcome)
    return code


def run_plan(summary, outcome):
    """The plan body; every early stop is a plain return with the outcome flags set."""
    out_dir = STATE["out"]
    if sha_file(DRAT_OLD[0])[0] != DRAT_OLD[1] or sha_file(KISSAT[0])[0] != KISSAT[1]:
        raise RuntimeError("binary pin mismatch")
    if sha_file(DRAT)[0] != DRAT_OLD[1] or os.lstat(DRAT).st_ino == os.lstat(DRAT_OLD[0]).st_ino:
        raise RuntimeError("vendored drat-trim mismatch or shared inode")
    prov = json.loads(read_pinned(*DRAT_PROV_RECEIPT)).get("drat_trim") or {}
    if prov.get("binary_sha256") != DRAT_PROV[1] or prov.get("source_sha256") != DRAT_SOURCE_SHA \
            or sha_file(DRAT_PROV[0])[0] != DRAT_PROV[1] \
            or os.lstat(DRAT_PROV[0]).st_ino in (os.lstat(DRAT).st_ino, os.lstat(DRAT_OLD[0]).st_ino):
        raise RuntimeError("provenanced drat-trim pin/receipt mismatch or shared inode")
    ok, recs = controls()
    summary["controls_ok"] = ok
    summary["controls_record_sha256"] = write_x(os.path.join(out_dir, "controls.json"), recs)
    STATE["remaining_reserve"] -= CONTROL_RESERVE
    if not ok:
        outcome["controls_failed"] = True
        summary["stopped"] = {"phase": "controls"}
        return
    read_pinned(ENC[0], ENC[1])
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
    E = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(E)
    D = json.loads(read_pinned(*SKEL))
    special = [p for p in D["profiles"] if list(p) != P0]
    for it in ITEMS:
        label = it["id"].replace(":", "_")
        rec = {"id": it["id"], "status": "UNKNOWN", "count_for_scientific_coverage": False,
               "host_clock_start": clock()}
        rec_path = os.path.join(out_dir, label + ".record.json")
        Ej = json.loads(read_pinned(*it["list"]))
        if not (Ej["num_placements"] == len(Ej["placements"]) == it["denominator"]):
            raise RuntimeError("list denominator mismatch " + it["id"])
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                   [Ej["placements"][i] for i in range(it["lo"], it["hi"] + 1)])
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = (hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode())
        if got != it["cnf"]:
            raise RuntimeError("CNF digest mismatch %r" % (got,))
        cnf_path = os.path.join(out_dir, label + ".cnf")
        write_bytes_x(cnf_path, cnf)
        del cnf
        if sha_file(cnf_path) != (it["cnf"][0], it["cnf"][1]):
            raise RuntimeError("CNF file re-hash mismatch")
        inputs = {"item": it["id"], "cnf_pin": [it["cnf"][0], it["cnf"][1]], "list_pin": it["list"][1],
                  "skeleton_pin": SKEL[1], "encoder_pin": ENC[1]}
        ks, kl, refused, buf = run_kissat(cnf_path, label, SOLVER_SECONDS, PROOF_CAP, LOG_CAP + 3 * RECORD_MAX, inputs)
        if ks is None:
            rec.update(reason="solver admission refused", refusal=refused, host_clock_end=clock())
            write_x(rec_path, rec)
            summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "solver admission refused"}
            summary["stopped"] = {"phase": "solver_admission", "item": it["id"], "why": refused}
            outcome["refused"] = True
            return
        rec["solver"] = ks
        rec["solver_status_lines"] = status_lines(kl)
        if ks["returncode"] == 10 and rec["solver_status_lines"] == ["s SATISFIABLE"] and ks["stop"] == "self" \
                and ks["settled"]:
            rec["status"] = "SAT_CANDIDATE"
            rec["sat"] = verify_sat(cnf_path, kl, label)
            rec["host_clock_end"] = clock()
            write_x(rec_path, rec)
            summary["items"][it["id"]] = {"status": "SAT_CANDIDATE", "sat": rec["sat"]}
            summary["stopped"] = {"phase": "sat_candidate", "item": it["id"]}
            outcome["sat"] = True
            return
        sink_ok = sink_complete(ks["proof_sink"])
        if sink_ok:
            rec["proof"] = {"sha256": ks["proof_sink"]["sha256_of_retained"], "bytes": ks["proof_sink"]["retained"],
                            "storage": "RAM only (P-STREAM); never written to disk"}
        if ks["returncode"] == 20 and ks["stop"] == "self" and ks["settled"] and sink_ok and not LATCH \
                and not cancelled():
            checks = []
            rec["checkers"] = {}
            for name, path, pin in CHECKERS:
                dr, dl, refused = run_check(cnf_path, buf, (name, path, pin), label, CHECK_SECONDS,
                                            LOG_CAP + 3 * RECORD_MAX,
                                            dict(inputs, proof_pin=[rec["proof"]["sha256"], rec["proof"]["bytes"]]))
                if dr is None:
                    rec.update(reason="checker %s admission refused" % name, refusal=refused, host_clock_end=clock())
                    write_x(rec_path, rec)
                    summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "checker %s admission refused" % name}
                    summary["stopped"] = {"phase": "checker_admission", "item": it["id"], "checker": name,
                                          "why": refused}
                    outcome["refused"] = True
                    return
                checks.append((name, dr, dl))
                rec["checkers"][name] = {"record": dr, "status_lines": status_lines(dl),
                                         "parse_lines": [s[:200] for s in dl if s.startswith("c parsing")
                                                         or s.startswith("c finished parsing") or s == STDIN_LINE][:6]}
                if checker_defects(name, it["cnf"], rec["proof"]["sha256"], rec["proof"]["bytes"], dr, dl) \
                        or LATCH or cancelled():
                    break  # S4: a later checker cannot rescue the item
            post_cnf, post_buf = sha_file(cnf_path), buf.digest()
            buf.release()
            rec["post_check_hashes"] = {"cnf": list(post_cnf), "proof_buffer": post_buf}
            rec["defects"] = qualify_stream(it["cnf"], ks, kl, PROOF_CAP, checks, post_cnf, post_buf)
            rec["host_clock_end"] = clock()
            rec["terminal_gate"] = terminal_gate()
            unsat = None
            if not rec["defects"] and not rec["terminal_gate"] and not LATCH:
                unsat = dict(rec, status="UNSAT", count_for_scientific_coverage=True,
                             commit="UNSAT chosen at an explicit commit boundary with no earlier cancel stamp or latch")
            commit = commit_record(rec_path, dict(rec, commit="UNKNOWN record"), unsat)
            rec["status"] = "UNSAT" if commit["committed_unsat"] else "UNKNOWN"
            summary.setdefault("commits", {})[it["id"]] = commit
        else:
            rec["reason"] = "no settled self-exit rc20 verdict with a complete proof buffer (or latch/cancel)"
            rec["host_clock_end"] = clock()
            write_x(rec_path, rec)
        buf.release()
        summary["items"][it["id"]] = {k: rec.get(k) for k in ("status", "defects", "terminal_gate", "reason", "proof")}
        STATE["remaining_reserve"] -= ITEM_RESERVE
        if LATCH or cancelled():
            summary["stopped"] = {"phase": "latch_or_cancel", "item": it["id"]}
            return
    outcome["complete"] = True


def final_code(summary, outcome):
    """r3#9: blocking metadata first, then an explicit closeout boundary, then the code."""
    out_dir = STATE["out"]
    try:
        host_end = clock()
    except BaseException as exc:
        host_end = "unavailable %r" % exc
    children = [c.settled_rec if c.settled_rec is not None else {"seq": c.seq, "label": c.label, "pid": c.pid,
                                                                   "settled": False, "note": "never settled"}
                for c in OWNED if c.proc is not None]
    all_settled = all(r.get("settled") for r in children)
    boundary = next(ORDER)
    co = STATE["cancel_order"]
    cancel_before = co is not None and co < boundary
    if outcome["sat"]:
        code = EXIT_SAT_CANDIDATE
    elif LATCH or not all_settled:
        code = EXIT_SAFETY_STOP
    elif outcome["exception"]:
        code = EXIT_EXCEPTION
    elif cancel_before:
        code = EXIT_CANCELLED
    elif outcome["controls_failed"]:
        code = EXIT_CONTROLS_FAILED
    elif outcome["refused"]:
        code = EXIT_ADMISSION_REFUSED
    elif outcome["complete"]:
        code = EXIT_PLAN_COMPLETE
    else:
        code = EXIT_EXCEPTION
    summary.update(exit_code=code, latch=list(LATCH), cancel_order=co, closeout_boundary=boundary,
                   cancel_before_closeout=cancel_before, host_clock_end=host_end,
                   children=[{k: r.get(k) for k in ("seq", "label", "pid", "returncode", "stop", "settled")}
                             for r in children],
                   all_children_settled=all_settled)
    try:
        write_x(os.path.join(out_dir, "summary.json"), summary)
    except BaseException as exc:
        print("SUMMARY WRITE FAILED %r" % exc, flush=True)
        code = EXIT_SAFETY_STOP
    print("SUMMARY", os.path.join(out_dir, "summary.json"), "exit", code, flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
