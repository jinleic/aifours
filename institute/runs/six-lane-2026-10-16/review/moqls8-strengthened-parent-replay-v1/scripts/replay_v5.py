#!/usr/bin/env python3
"""Parent replay desk for the six MOQLS(8) P1 strengthened formulas (normal form r2, section 5), v5 transport.

Desk: institute/runs/six-lane-2026-10-16/review/moqls8-strengthened-parent-replay-v1 (parent-owned). Derived by
copying scripts/replay_v4.py (sha256 44b4f293...dc9d; v4 = v3 baa4a675...7565 + DIFF-replay_v3-to-v4.txt, which fixed
the Codex v3 findings 1-9). v5 adds the parent's long-job disk-stability rule for formula launches (read from the
parent disk monitor file) and the Codex v4 review fixes; the changes are in DIFF-replay_v4-to-v5.txt. Every v5 file
name has the 'v5-' prefix.

Transport: CNF bytes exist only in this process's memory and reach each child through its own anonymous pipe passed
as /dev/fd/N. Each writer thread hashes exactly the bytes it writes (measured feed). The DRAT proof goes solver ->
named FIFO -> parent relay thread -> anonymous pipe -> drat-trim stdin (-i). The relay hashes and counts the bytes
it reads from the FIFO (the proof stream) and, separately, the bytes os.write() delivered to the checker. At most
one CHUNK (1 MiB) is in flight. FIFO EOF is recorded only when read() returns b''. Delivery errors (e.g. EPIPE when
the checker closed its proof input), drain (read) errors and close errors are kept apart; after a delivery error
the relay keeps reading and hashing the FIFO to EOF so the solver never blocks. No CNF or proof bytes touch disk.

Proof-byte counter semantics (pinned parent drat-trim source d834b649...c2ee, review/moqls7-parent-proofcheck-tools-v1/
drat-trim.c): with -i (binary mode) S->nReads is incremented once per consumed proof byte (L987 in read_lit, L1115
for the 'a'/'d' marker byte); the parse loop reads until EOF and does not stop at the empty clause (L1107-1108 break
only on EOF at a marker position); a wrong binary prefix stops reading early (L1113, N < D); an EOF met at the start
of a literal adds one (L986-988, N = D + 1). So 'c finished parsing, read N bytes from proof file' with N == D (the
relay-delivered byte count) is an exact "consumed to EOF, well-formed" check. The suffix control shows that N counts
bytes delivered after the empty clause.

Process control: native limits (cadical -t 3600, drat-trim -t 7200) plus cooperative SIGTERM safety stops with a
bounded 120 s wait; never SIGKILL, never Popen.kill, never subprocess timeouts. The ps/lsof lane-scan helpers run in
their own session under monotonic deadlines (SIGTERM-only cleanup); in flight a scanner thread publishes readings and
a failed or stale lane reading, an unreadable own-child RSS, or any exception after a spawn is a safety stop
(SIGTERM own children, bounded reap, UNKNOWN, no further launch). A SIGTERM to the driver is latched and checked
before gate success and immediately before each spawn. A timeout, guard stop or deferral is never success.

Runs: a PRE-EXEC holds either only controls (selftest:NAME) or only formulas (formula:ID). A formula PRE-EXEC is
admitted only if all five v5 control receipts exist for THIS script sha and the pinned binaries with their
preregistered verdicts; this is validated at preexec and again in run before each launch. A formula launch also
needs the parent disk monitor to show stability (see GATE_RULE); an absent or stale monitor refuses formulas.
Usage (/usr/bin/python3 -I -B, environment TMPDIR=<desk>/tmp/):
  replay_v5.py preexec OUT [--worker-prefix N SHA] ITEM...    ITEM = selftest:NAME | formula:ID
  replay_v5.py run PREEXEC
  replay_v5.py assemble OUT PREEXEC...
"""
import ctypes
import datetime
import fcntl
import glob
import hashlib
import json
import os
import re
import selectors
import signal
import struct
import subprocess
import sys
import threading
import time
import traceback

ROOT = "/Users/jinleic/repos/aifours"
RUN = ROOT + "/institute/runs/six-lane-2026-10-16"
REVIEW = RUN + "/review"
LANE = ROOT + "/physics/evidence/six-lane-20261016/moqls8-problem16"
DESK = REVIEW + "/moqls8-strengthened-parent-replay-v1"
SCRIPT = os.path.realpath(__file__)
SCRIPT_REL = "scripts/replay_v5.py"
LABEL_PREFIX = "v5-"  # every v5 receipt/log/FIFO/TMPDIR name; v2, v3 and v4 names stay untouched
TMP = DESK + "/tmp"

CADICAL = "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical"
CADICAL_SHA = "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa"
DRAT = REVIEW + "/moqls7-parent-proofcheck-v1/drat-trim"
DRAT_RECEIPT = REVIEW + "/moqls7-parent-proofcheck-v1/parent-result.json"
DRAT_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"  # that desk's drat_trim.binary_sha256
DRAT_AFFIXES = ("a46c0c71", "8e37")
BIND_DIR = REVIEW + "/moqls8-one-p4-parent-binding-v1"
BIND_RESULT_AFFIXES = ("65311ab0", "28b0")
OLD_ENCODER_BINDING = REVIEW + "/moqls8-encoder-binding-v1/binding-result.v2.json"
OLD_ENCODER_BINDING_SHA = "dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112"
WORKER_RESULTS = LANE + "/evidence/n8_one_p4_template_runs_v1/RESULTS.jsonl"
WORKER_PREFIX = (16, "bcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19")
DELETIONS_REL = "evidence/UNIFIED_ONE_P4_DELETIONS_v1.json"
MANIFEST_REL = "evidence/n8_one_p4_templates_v1/MANIFEST.json"
RECIPE_REL = "evidence/n8_one_p4_templates_v1/BASE_RECIPE.json"
TABLE_REL = "review/K5_COLUMN0_TEMPLATE_COVER.r1.md"
MAP_REL = "evidence/gram_dev_v1/GA5L_K5_sb2.map.json"
PINS = {  # identical to the PINS dict of parent_binding_v1.py (checked at load time)
    DELETIONS_REL: "4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6",
    MANIFEST_REL: "355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74",
    RECIPE_REL: "264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18",
    TABLE_REL: "1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a",
    MAP_REL: "7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197",
    "code/gram_a.py": "bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a",
}
SOURCE_HEADER = b"p cnf 509915 5740230\n"
WEAK_HEADER = b"p cnf 509915 5740226\n"
LEAF_HEADER = b"p cnf 509915 5740268\n"
COUNTS = (5740230, 5740226, 4, 1576)  # source clauses, retained, deleted, deleted bytes
# --- strengthened formulas (normal form r2 section 5), bound beforehand in BINDING.json by scripts/bind_v1.py
V1_SCRIPT = REVIEW + "/moqls8-fone-parent-replay-v1/scripts/replay_v1.py"
V1_SCRIPT_SHA = "16cba374241636885d71f2e91dd3969d35779ccbe27eca4fc2bee3c8781f486d"
BINDING = DESK + "/BINDING.json"
BINDING_SHA = "5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c"
BIND_SCRIPT = DESK + "/scripts/bind_v1.py"
BIND_SCRIPT_SHA = "b010baa4dd5c7620f7c6215beeb052af80846bfd6c3ee0a80e8d8a235144786c"
V2_SCRIPT = DESK + "/scripts/replay_v2.py"
V2_SCRIPT_SHA = "dcedbe45c6a354c03b400539eda588c2dca65a40d1f7009a3c42faceb97aac82"
DIFF_V1_V2 = DESK + "/DIFF-replay_v1-to-v2.txt"
DIFF_V1_V2_SHA = "44b12b90c1ebcfb173cb502f7cff1e6f64f5217cdddad91e9cc59e48789de0ba"
V3_SCRIPT = DESK + "/scripts/replay_v3.py"
V3_SCRIPT_SHA = "baa4a675fc2634dc8dc96f53b9f6dd1b59af012b9fef23681af894904aa67565"
DIFF_V2_V3 = DESK + "/DIFF-replay_v2-to-v3.txt"
DIFF_V2_V3_SHA = "dc2a67ecf0aa5a9e7f19de0a145f04a60c3fd70325cbb61f7703d2d596aba8c8"
V4_SCRIPT = DESK + "/scripts/replay_v4.py"
V4_SCRIPT_SHA = "44b4f293b4a0eeb86cafce1afa9314e7e54592d60d95791dee4d58539c9bdc9d"
DIFF_V3_V4 = DESK + "/DIFF-replay_v3-to-v4.txt"
DIFF_V3_V4_SHA = "3e2625c591f17ec432512e4cb9f603901cf2ddea64399f7986348501f48acd53"
DIFF = DESK + "/DIFF-replay_v4-to-v5.txt"
NF_R2 = LANE + "/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md"
NF_R2_SHA = "8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f"
NF_CHECK = REVIEW + "/moqls8-p1-normalform-parent-v1/check_local_boolean_v1.py"
NF_CHECK_SHA = "abfa623afdd89def969ef48abc2c4a508a84e1f1488651243d023e7dd7762531"
NF_RESULT = REVIEW + "/moqls8-p1-normalform-parent-v1/RESULT.json"
NF_RESULT_SHA = "e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2"
WORKER_HASHES = LANE + "/evidence/P1_MONOMIAL_FORMULA_HASHES.r2.json"
WORKER_HASHES_SHA = "e04557a4ea83875caa265e9928b488386fe52c2f95306bd6078f7706265eb709"
TAIL_FP = {  # 126-clause M_s tail bytes sha256 (parent RESULT e075aff8 mononomial_clause_checks)
    2: "6fe525a9e6df69193b918d3f0ec29c841d0a66845ee58b3ca0690b9fe2988708",
    3: "e9f44b5f4c9ca4a4de152bcc47385283da7b66d074b10956a0fcdc7440b5ca7c",
    4: "900a6bc37239e6835f4190ccf42dfc4088dfd4a43dcc4aec522d9297da8e4dea",
    5: "233636b1002e5b9f877999d9cce0ab822b44c585edee70a9248f601652554cce",
}
FORMULAS = {  # id -> (source template, square s, bound strengthened sha256 = worker r2 hash)
    "P1-B1.M2": ("P1-B1", 2, "09a117b880a4715e068c33b7601b23b424b70218958675ed68b28f053fd050c0"),
    "P1-B2.M2": ("P1-B2", 2, "3f65ad964ea83c68f78d7a6a90a95820925c70636e610ec0f4e78541531e04b0"),
    "P1-B2.M4": ("P1-B2", 4, "61bddbe074e733a632b10fdac214d4bde1032cda4bdfcf563275d5a5f6fb4af0"),
    "P1-B3.M2": ("P1-B3", 2, "e4b55555bdeb9ba389cec74983576ee66939fe19210bb593d7bdac0ba392428d"),
    "P1-B5.M2": ("P1-B5", 2, "caf1368490f766b1df4be973450fbe8b4dc1867067bfc5a9069f9060528510f4"),
    "P1-B5.M3": ("P1-B5", 3, "36d58ad9c4e5bb0e70e163a50a322079458c9cfd2fee9251dec8d1ec363c8e35"),
}
STRONG_HEADER = b"p cnf 509915 5740394\n"
TAIL_CLAUSES = 126
PDT = datetime.timezone(datetime.timedelta(hours=-7))
NO_LAUNCH_AT = datetime.datetime(2026, 10, 18, 17, 29, 0, tzinfo=PDT).timestamp()    # 60 s before the 17:30 cutoff
NATIVE_STOP_AT = datetime.datetime(2026, 10, 18, 17, 57, 0, tzinfo=PDT).timestamp()  # in flight: SIGTERM at this

SOLVER_SECONDS, CHECKER_SECONDS = 3600, 7200
BACKSTOP = SOLVER_SECONDS + CHECKER_SECONDS + 120
GIB, MIB = 1 << 30, 1 << 20
LAUNCH_FLOOR = 12200000000 + 10 * MIB   # fresh check before each launch: 12.2e9 + projected retained growth
FLOOR = 12000000000                     # in flight: free below this -> SIGTERM -> UNKNOWN
LANE_BUSY_CAP, MINE = 4, 2
GATE_RSS = 76 * GIB // 10               # launch: lane RSS + projected <= 7.6 GiB
STOP_LANE_RSS = 785 * GIB // 100        # in flight: lane RSS > 7.85 GiB -> SIGTERM
DESK_MARGIN = GIB // 2                  # in flight: desk aggregate > projected + 0.5 GiB -> SIGTERM
FLOOR_HIGH = 46 * GIB // 10
SELFTEST_PROJECTED = 512 * MIB
WAIT_POLL, WAIT_BUDGET, GATE_STREAK = 60, 6 * 3600, 2
SAMPLE, LANE_SCAN_PERIOD, SIGTERM_GRACE = 0.25, 1.0, 120
HOT_CPU_FRACTION, HOT_WINDOW = 0.5, 2.0
CHUNK = 1 << 20
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
       "HOME": os.environ.get("HOME", DESK)}
NATIVE = {"cadical", "kissat", "drat-trim", "lrat-check", "lrat-trim", "cake_lpr", "dpr-trim", "glucose",
          "minisat", "lingeling", "plingeling", "treengeling", "cryptominisat5", "kissat_mab", "dpr2pr"}
LANE_MARKERS = ("/moqls8-problem16", "/review/moqls8-")
INFO_KEYS = (b"finished parsing", b"clauses in core", b"lemmas in core", b"RAT lemmas", b"verification time",
             b"ERROR", b"empty clause", b"conflict", b"TIMEOUT", b"timeout", b"FAIL", b"failed")

UNSAT3 = (b"p cnf 3 8\n1 2 3 0\n1 2 -3 0\n1 -2 3 0\n1 -2 -3 0\n-1 2 3 0\n-1 2 -3 0\n-1 -2 3 0\n"
          b"-1 -2 -3 0\n")
SAT3 = b"p cnf 3 7\n1 2 3 0\n1 2 -3 0\n1 -2 3 0\n1 -2 -3 0\n-1 2 3 0\n-1 2 -3 0\n-1 -2 3 0\n"
NOHEADER = b"c header-less control input: the parent drat-trim exits before it reads any proof byte\n"
SELFTESTS = {  # name -> (solver CNF, checker CNF, mode): the five v4 relay controls
    "unsat": (UNSAT3, UNSAT3, "refutation"),            # complete valid relay path
    "sat-checker": (UNSAT3, SAT3, "negative"),         # invalid: relay complete and equal, proof rejected
    "truncate": (UNSAT3, UNSAT3, "relay-truncate"),    # relay withholds the last TRUNCATE_BYTES proof bytes
    "early-close": (UNSAT3, NOHEADER, "early-close"),  # checker exits before reading the proof; relay gets EPIPE
    "suffix": (UNSAT3, UNSAT3, "relay-suffix"),        # relay appends SUFFIX after the solver's EOF
}
TRUNCATE_BYTES = 2      # truncation control: bytes the relay reads but never delivers (bounded tail buffer)
SUFFIX = b"d\x02\x04\x06\x00"  # suffix control: binary DRAT deletion of clause '1 2 3' ('d', lits 1 2 3, 0)
HOLD_SECONDS = 60       # early-close control only: bounded waits that make the event order deterministic
SELFTEST_WANT = {"refutation": "PASS", "negative": "AS_PREREGISTERED_NOT_VERIFIED",
                 "relay-truncate": "AS_PREREGISTERED_FAIL_CLOSED", "early-close": "AS_PREREGISTERED_FAIL_CLOSED",
                 "relay-suffix": "AS_PREREGISTERED_FAIL_CLOSED"}
RELAY_MODES = {"refutation": "plain", "negative": "plain", "relay-truncate": "truncate", "early-close": "plain",
               "relay-suffix": "suffix"}
DRAT_NO_HEADER_LINE = b"c ERROR: did not find p cnf line in input file"
HELPER_DEADLINE, HELPER_TERM_WAIT, STALE_SECONDS = 8.0, 5.0, 30.0
RECEIPT_SCHEMA = "moqls8-strengthened-parent-replay-receipt/4"
# Parent long-job disk-stability rule (formula launches only), read from the parent's 10 s disk monitor file
MONITOR = REVIEW + "/disk-monitor-v1-20261018T0722-to-1810.jsonl"  # parent monitor until 18:10 PDT
STABLE_FREE_MIN = 13500000000 + 10 * (1 << 20)   # last monitor free >= 13.5e9 B + 10 MiB projected growth
STABLE_WINDOW, STABLE_MAX_DROP = 300.0, 300000000  # max peak-to-later drop over the last 300 s <= 300 MB
STABLE_MAX_AGE, STABLE_MIN_SAMPLES, STABLE_MIN_SPAN = 30.0, 25, 290.0

SCOPE = ("Parent replay of the six exact strengthened P1 formulas only (source P1 leaf + 126-clause M_s tail; "
         "CaDiCaL 3.0.1 -> named FIFO -> parent hashing/counting relay -> parent drat-trim, measured parent feeds). "
         "Results are exact-formula facts; "
         "their transfer to the four open P1 templates needs separate parent acceptance of the normal form r2. It "
         "establishes no n=8 or Problem-16 conclusion and makes no theorem claim.")
ACCEPTANCE = ("PASS iff all of: solver rc 20; solver status lines (log with only '\\r' removed, lines starting "
              "with 's') exactly ['s UNSATISFIABLE']; checker rc 0; checker log with only '\\r' removed has a line "
              "exactly 's VERIFIED' and contains neither 's NOT VERIFIED' nor 's TIMEOUT'; no safety stop; solver "
              "and checker writer threads ok with no close error and finished, written == formula length, and "
              "sha256 of the bytes each actually wrote == the bound strengthened hash; the parent relay saw the FIFO "
              "EOF, read R > 0 proof bytes and delivered D bytes to the checker with R == D, equal sha256 of the "
              "bytes read and the bytes delivered, no delivery, drain or close error, nothing withheld, and its thread "
              "finished; the checker's own 'c finished parsing, read N bytes from proof file' line is present with "
              "N == D (absent line: fail-closed; drat-trim.c L986-988, L1107-1115: N == D means the delivered stream "
              "was consumed to EOF and well-formed); stricter than the brief: drat-trim's "
              "'c parsing input formula' line reports the header's variable and clause counts and the checker log "
              "has no 'early EOF' or 'clauses less than expected' warning. The proof-stream sha256 and byte count "
              "(relay read side) are recorded as provenance; they do not make a proof correct, only drat-trim's "
              "verdict on the delivered bytes does. Anything else is UNKNOWN, with reasons (SAT report, proof "
              "rejection, feed mismatch, timeout, guard stop, writer error, other). After a SAT report (rc 10 or "
              "'s SATISFIABLE') the model stays in the solver log and the desk launches nothing more; after a floor "
              "or safety stop the desk launches nothing more; any other UNKNOWN continues with the next formula. "
              "No retries without parent approval.")
GATE_RULE = ("Before each launch a fresh lane scan (native solver/checker processes plus python processes whose cwd "
             "or argv lies in the lane or a review/moqls8-* desk, excluding this desk's driver and children; python "
             "counts as busy if its CPU use over a 2 s libproc window is >= 50%; lane RSS conservatively includes "
             "every such python, busy or not) and a fresh statvfs: launch only if lane busy + 2 <= 4, lane RSS + "
             "projected <= 7.6 GiB and free >= 12,200,000,000 + 10 MiB. Stricter than the brief: two consecutive "
             "passing checks 60 s apart are required, so a launch never rides a transient gap of the priority "
             "worker pipeline. Otherwise sleep 60 s and re-check; total gate wait per run bounded by 6 h, then stop "
             "and report deferral. No launch at or after 2026-10-18 17:29:00 PDT (host clock; 60 s margin before "
             "the 17:30 cutoff). Formula launches additionally need the parent disk monitor "
             "(review/disk-monitor-v1-20261018T0722-to-1810.jsonl, 10 s cadence) to "
             "show: last sample <= 30 s old with free >= 13,500,000,000 + 10 MiB, >= 25 samples spanning >= 290 s "
             "within the last 300 s, and a max peak-to-later free drop over that window <= 300,000,000 B; an absent, "
             "unreadable or stale monitor refuses formulas (fail closed); controls keep the plain fresh gate. The "
             "fresh statvfs is re-read at the launch decision. Projected peak = "
             "max(1.5 x worker aggregate peak of the formula's source template leaf (the worker's 900 s attempt; "
             "no worker run of a strengthened formula exists), 4.6 GiB); self-tests 512 MiB.")
STOPS = ("In flight, every 0.25 s: desk aggregate RSS (driver + live children, libproc; a live child unreadable twice "
         "in a row is a guard failure) and free space; a scanner thread publishes lane scans every >= 1 s (helpers "
         "under %.0f s deadlines). SIGTERM own children if a lane reading failed or is older than %.0f s, lane RSS "
         "(other lane processes + desk) > 7.85 GiB, desk aggregate > projected + 0.5 GiB, free < 12,000,000,000, "
         "wall > %d + %d + 120 s, the host clock reaches 2026-10-18 17:57:00 PDT, the checker exits while the solver "
         "still runs, any exception after the first fd, or the driver receives SIGTERM (also checked immediately "
         "before each spawn and before gate success); then wait at most 120 s, never escalate; result UNKNOWN and "
         "the desk launches nothing more." % (HELPER_DEADLINE, STALE_SECONDS, SOLVER_SECONDS, CHECKER_SECONDS))


def die(msg):
    raise SystemExit("ABORT: %s" % msg)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_parts(parts):
    h, n = hashlib.sha256(), 0
    for part in parts:
        h.update(part)
        n += len(part)
    return h.hexdigest(), n


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def free_bytes():
    st = os.statvfs(REVIEW)
    return st.f_bavail * st.f_frsize


def write_json_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=1)
        f.write("\n")
    return sha_file(path)


def rel(path):
    return os.path.relpath(path, DESK)


# --- libproc (macOS sys/proc_info.h: PROC_PIDTASKINFO = 4; struct proc_taskinfo is 96 bytes: pti_virtual_size,
# pti_resident_size, pti_total_user, pti_total_system as the first four uint64; CPU times are mach ticks).
_LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
_LIBPROC.proc_pidinfo.restype = ctypes.c_int


class _Timebase(ctypes.Structure):
    _fields_ = [("numer", ctypes.c_uint32), ("denom", ctypes.c_uint32)]


_TB = _Timebase()
ctypes.CDLL("/usr/lib/libSystem.B.dylib").mach_timebase_info(ctypes.byref(_TB))


def taskinfo(pid):
    """(resident bytes, total CPU ns) or None."""
    buf = ctypes.create_string_buffer(96)
    if _LIBPROC.proc_pidinfo(pid, 4, 0, buf, 96) != 96:
        return None
    _vsz, resident, user, system = struct.unpack_from("=QQQQ", buf.raw, 0)
    return resident, (user + system) * _TB.numer // _TB.denom


def rss(pid):
    t = taskinfo(pid)
    return t[0] if t else 0


# --- phys-1 lane scan
def run_helper(argv):
    """Run one short ps/lsof helper in its own session (never in the driver's process group) under a monotonic
    deadline. On overrun: SIGTERM, wait at most HELPER_TERM_WAIT, never escalate. -> (rc or None, stdout, error)."""
    try:
        p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                             env=ENV, start_new_session=True)
    except OSError as e:
        return None, b"", "spawn %s: %r" % (argv[0], e)
    deadline = time.monotonic() + HELPER_DEADLINE
    fd = p.stdout.fileno()
    os.set_blocking(fd, False)
    chunks, err = [], None
    sel = selectors.DefaultSelector()
    sel.register(fd, selectors.EVENT_READ)
    try:
        eof = False
        while not eof and err is None:
            left = deadline - time.monotonic()
            if left <= 0:
                err = "%s exceeded the %.0f s deadline" % (argv[0], HELPER_DEADLINE)
                break
            for _key, _ev in sel.select(min(left, 0.5)):
                try:
                    b = os.read(fd, 65536)
                except BlockingIOError:
                    continue
                if b:
                    chunks.append(b)
                else:
                    eof = True
        while err is None and p.poll() is None:
            if time.monotonic() > deadline:
                err = "%s did not exit within the %.0f s deadline" % (argv[0], HELPER_DEADLINE)
                break
            time.sleep(0.01)
        if err is not None and p.poll() is None:
            try:
                os.kill(p.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            t_end = time.monotonic() + HELPER_TERM_WAIT
            while p.poll() is None and time.monotonic() < t_end:
                time.sleep(0.05)
            if p.poll() is None:
                err += "; still alive %.0f s after SIGTERM (no escalation)" % HELPER_TERM_WAIT
    finally:
        sel.close()
        p.stdout.close()
    return p.returncode, b"".join(chunks), err


def lane_scan():
    """Other lane processes -> (list, None), or (None, error) if a helper failed or overran its deadline.
    Excludes this process and its children."""
    me = os.getpid()
    rc, out, err = run_helper(["/bin/ps", "-axww", "-o", "pid=,ppid=,rss=,state=,comm="])
    if err is not None or rc != 0:
        return None, err or "ps rc %s" % rc
    cand = {}
    for line in out.decode("utf-8", "replace").splitlines():
        parts = line.split(None, 4)
        if len(parts) < 5:
            continue
        try:
            pid, ppid, rss_kb = int(parts[0]), int(parts[1]), int(parts[2])
        except ValueError:
            continue
        if pid == me or ppid == me:
            continue
        base = os.path.basename(parts[4].strip())
        native = base in NATIVE
        if native or base.lower().startswith("python"):
            cand[pid] = {"pid": pid, "ppid": ppid, "ps_rss_kb": rss_kb, "state": parts[3], "comm": base,
                         "native": native}
    if not cand:
        return [], None
    pids = ",".join(str(x) for x in cand)
    _rc, out, err = run_helper(["/usr/sbin/lsof", "-a", "-d", "cwd", "-p", pids, "-Fpn"])
    if err is not None:  # lsof exits 1 when a listed pid has gone; only a failed or overrun helper fails the scan
        return None, err
    cwd, cur = {}, None
    for line in out.decode("utf-8", "replace").splitlines():
        if line.startswith("p"):
            try:
                cur = int(line[1:])
            except ValueError:
                cur = None
        elif line.startswith("n") and cur is not None:
            cwd[cur] = line[1:]
    _rc, out, err = run_helper(["/bin/ps", "-ww", "-o", "pid=,args=", "-p", pids])
    if err is not None:
        return None, err
    args = {}
    for line in out.decode("utf-8", "replace").splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            try:
                args[int(parts[0])] = parts[1]
            except ValueError:
                pass
    lane = []
    for pid, c in cand.items():
        c["cwd"] = cwd.get(pid, "")
        full_args = args.get(pid, "")
        if any(mk in c["cwd"] or mk in full_args for mk in LANE_MARKERS):
            t = taskinfo(pid)
            c["rss_bytes"] = t[0] if t else c["ps_rss_kb"] * 1024
            c["cpu_ns"] = t[1] if t else None
            c["args"] = full_args[:240]
            lane.append(c)
    return lane, None


class Scanner(threading.Thread):
    """In-flight lane scanner: publishes (monotonic time, scan or None, error) after every scan, so the watchdog
    loop never blocks on a helper. A failed or stale published reading is a safety stop in pipeline()."""

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.halt = threading.Event()
        self.lock = threading.Lock()
        self.latest = None
        self.scans = self.failures = 0

    def run(self):
        while not self.halt.is_set():
            try:
                scan, err = lane_scan()
            except Exception as e:  # recorded, never hidden
                scan, err = None, "lane scan raised %r" % e
            with self.lock:
                self.latest = (time.monotonic(), scan, err)
                self.scans += 1
                self.failures += 1 if scan is None else 0
            self.halt.wait(LANE_SCAN_PERIOD)

    def reading(self):
        with self.lock:
            return self.latest


def compact(c):
    out = {k: c[k] for k in ("pid", "ppid", "comm", "native", "rss_bytes", "state", "cwd") if k in c}
    for k in ("busy", "cpu_fraction"):
        if k in c:
            out[k] = c[k]
    out["args"] = c.get("args", "")[:160]
    return out


def gate_scan():
    scan, err = lane_scan()
    if scan is None:
        return None, None, None, err
    c0 = {c["pid"]: c["cpu_ns"] for c in scan}
    t0 = time.monotonic()
    time.sleep(HOT_WINDOW)
    dt = time.monotonic() - t0
    busy = total = 0
    for c in scan:
        t = taskinfo(c["pid"])
        if t:
            c["rss_bytes"] = max(c["rss_bytes"], t[0])
        if c["native"]:
            c["busy"] = True
        else:
            frac = None
            if t and c0.get(c["pid"]) is not None:
                frac = (t[1] - c0[c["pid"]]) / (dt * 1e9)
            c["cpu_fraction"] = None if frac is None else round(frac, 3)
            c["busy"] = frac is not None and frac >= HOT_CPU_FRACTION
        busy += 1 if c["busy"] else 0
        total += c["rss_bytes"]
    return busy, total, scan, None


def monitor_stability():
    """Parent long-job disk-stability rule from the parent's 10 s monitor file -> (ok, info). Fail closed: an absent,
    unreadable, empty or stale monitor gives ok False. Read-only; no new statvfs polling."""
    info = {"monitor": rel(MONITOR), "read_at": now()}
    try:
        raw = read_bytes(MONITOR)
    except OSError as e:
        info.update(ok=False, error="monitor unreadable: %r" % e)
        return False, info
    samples = []
    for line in raw.split(b"\n"):
        try:
            r = json.loads(line)
            samples.append((datetime.datetime.fromisoformat(r["t"]).timestamp(), int(r["free"])))
        except (ValueError, KeyError, TypeError):
            continue  # the start record, blank lines and a partially written last line
    nowt = time.time()
    win = [(t, f) for t, f in samples if nowt - STABLE_WINDOW <= t <= nowt + 5.0]
    max_drop, peak = 0, None
    for _t, f in win:
        peak = f if peak is None else max(peak, f)
        max_drop = max(max_drop, peak - f)
    last_t, last_f = samples[-1] if samples else (None, None)
    age = None if last_t is None else nowt - last_t
    span = win[-1][0] - win[0][0] if win else 0.0
    checks = {"last_sample_fresh": age is not None and age <= STABLE_MAX_AGE,
              "last_free_ok": last_f is not None and last_f >= STABLE_FREE_MIN,
              "enough_samples": len(win) >= STABLE_MIN_SAMPLES, "span_ok": span >= STABLE_MIN_SPAN,
              "drop_ok": bool(win) and max_drop <= STABLE_MAX_DROP}
    ok = all(checks.values())
    info.update(ok=ok, checks=checks, monitor_bytes=len(raw), monitor_sha256_at_read=sha_bytes(raw),
                samples_total=len(samples), window_samples=len(win), window_span_seconds=round(span, 1),
                last_free=last_f, last_age_seconds=None if age is None else round(age, 1),
                max_peak_to_later_drop_bytes=max_drop)
    return ok, info


def gate(label, projected, budget, log, stop, stable=False):
    t_start = time.monotonic()
    samples, streak = [], 0
    while True:
        fb = free_bytes()
        busy, other, scan, scan_err = gate_scan()
        ok_disk = fb >= LAUNCH_FLOOR
        ok_busy = scan is not None and busy + MINE <= LANE_BUSY_CAP
        ok_rss = scan is not None and other + projected <= GATE_RSS
        ok_stable, sinfo = monitor_stability() if stable else (True, None)
        ok = ok_disk and ok_busy and ok_rss and ok_stable
        streak = streak + 1 if ok else 0
        samples.append({"at": now(), "free_bytes": fb, "lane_other_busy": busy, "lane_other_rss_bytes": other,
                        "scan_failed": scan is None, "scan_error": scan_err, "ok_disk": ok_disk, "ok_busy": ok_busy,
                        "ok_rss": ok_rss, "ok_stable": ok_stable, "stability": sinfo, "streak": streak})
        log("gate %s: free=%d other_busy=%s other_rss=%s projected=%d disk/busy/rss/stable=%s/%s/%s/%s streak=%d%s"
            % (label, fb, busy, other, projected, ok_disk, ok_busy, ok_rss, ok_stable, streak,
               "" if scan_err is None else " scan_error=" + scan_err))
        waited = time.monotonic() - t_start
        res = {"label": label, "projected_peak_bytes": projected, "rule": GATE_RULE, "samples": samples,
               "stability_rule_applied": stable, "waited_seconds": round(waited, 1)}
        if stop.get("signal"):  # latched SIGTERM wins over a passing streak
            budget["used"] += waited
            res.update({"launch": False, "stopped": "driver received " + stop["signal"], "stopped_at": now()})
            return res
        if time.time() >= NO_LAUNCH_AT:
            budget["used"] += waited
            res.update({"launch": False, "cutoff": True, "stopped": "launch cutoff 2026-10-18 17:29:00 PDT reached",
                        "stopped_at": now()})
            return res
        if streak >= GATE_STREAK:
            fb_final = free_bytes()  # the frozen fresh statvfs gate, re-read at the launch decision
            ok_final, s_final = monitor_stability() if stable else (True, None)
            if fb_final >= LAUNCH_FLOOR and ok_final:
                budget["used"] += waited
                res.update({"launch": True, "decided_at": now(), "free_bytes_at_launch": fb_final,
                            "stability_at_launch": s_final, "lane_other_busy_at_launch": busy,
                            "lane_other_rss_at_launch": other, "launch_scan": [compact(c) for c in scan]})
                return res
            streak = 0
            samples[-1]["final_recheck_failed"] = {"free_bytes": fb_final, "stability_ok": ok_final}
            log("gate %s: final re-check failed (free=%d stable=%s); streak reset" % (label, fb_final, ok_final))
        if budget["used"] + waited + WAIT_POLL > WAIT_BUDGET:
            budget["used"] += waited
            res.update({"launch": False, "deferred": True, "deferred_at": now(),
                        "wait_used_total_seconds": round(budget["used"], 1),
                        "last_scan": [compact(c) for c in (scan or [])]})
            return res
        for _ in range(WAIT_POLL):
            if stop.get("signal"):
                break
            time.sleep(1)


# --- inputs: pins, parent binding, in-memory leaf regeneration (as parent_binding_v1.py hashes the leaves)
def load_inputs(log):
    t0 = time.monotonic()
    raw = {}
    for k, v in PINS.items():
        raw[k] = read_bytes(os.path.join(LANE, k))
        if sha_bytes(raw[k]) != v:
            die("pin mismatch " + k)
    d = json.loads(raw[DELETIONS_REL])
    m = json.loads(raw[MANIFEST_REL])
    recipe = json.loads(raw[RECIPE_REL])
    bscript = read_bytes(BIND_DIR + "/parent_binding_v1.py")
    bpre_raw = read_bytes(BIND_DIR + "/PRE-EXEC.json")
    bres_raw = read_bytes(BIND_DIR + "/RESULT.json")
    bscript_sha, bpre_sha, bres_sha = sha_bytes(bscript), sha_bytes(bpre_raw), sha_bytes(bres_raw)
    if json.loads(bpre_raw)["script_sha256"] != bscript_sha:
        die("parent binding script differs from its PRE-EXEC pin")
    if not (bres_sha.startswith(BIND_RESULT_AFFIXES[0]) and bres_sha.endswith(BIND_RESULT_AFFIXES[1])):
        die("parent binding RESULT.json sha256 " + bres_sha)
    btext = bscript.decode()
    block = re.search(r"\nPINS=\{\n(.*?)\n\}\n", btext, re.S)
    if not block or dict(re.findall(r"'([^']+)':'([0-9a-f]{64})'", block.group(1))) != PINS:
        die("PINS differ from parent_binding_v1.py")
    for frag in ("weak_header=b'p cnf 509915 5740226\\n';leaf_header=b'p cnf 509915 5740268\\n'",
                 "for i,S in enumerate(supports,2):", "for c in range(1,8):", "units.append(v if c in S else -v)",
                 "hh=leaf.copy();hh.update(b''.join(('%d 0\\n'%u).encode('ascii') for u in units))"):
        if frag not in btext:
            die("parent binding construction fragment missing: " + frag)
    bres = json.loads(bres_raw)
    if bres.get("status") != "PASS":
        die("parent binding status")
    if sha_file(OLD_ENCODER_BINDING) != OLD_ENCODER_BINDING_SHA:
        die("previous encoder binding")
    source = os.path.join(LANE, d["source_base"])
    deleted = {r["clause_index_zero_based"]: r["clause_bytes_sha256"] for r in d["delete"]}
    keep = d["keep_q1"]
    keep_i = keep["clause_index_zero_based"]
    if keep_i in deleted:
        die("kept clause listed as deleted")
    body_len = recipe["weakened_body_bytes"]
    body = bytearray(body_len)
    mv = memoryview(body)
    full = hashlib.sha256()
    pos = nc = retained = removed = deleted_bytes = 0
    keep_seen = False
    with open(source, "rb") as f:
        header = f.readline()
        full.update(header)
        if header != SOURCE_HEADER:
            die("source header")
        for i, line in enumerate(f):
            full.update(line)
            nc += 1
            if not line.endswith(b" 0\n") or b"\r" in line or line.startswith(b"c"):
                die("clause format at index %d" % i)
            if i in deleted:
                if sha_bytes(line) != deleted[i]:
                    die("deleted clause %d" % i)
                removed += 1
                deleted_bytes += len(line)
            else:
                n = len(line)
                if pos + n > body_len:
                    die("retained body longer than recipe")
                mv[pos:pos + n] = line
                pos += n
                retained += 1
                if i == keep_i:
                    if sha_bytes(line) != keep["clause_bytes_sha256"]:
                        die("kept clause")
                    keep_seen = True
    mv.release()
    full_hex = full.hexdigest()
    if pos != body_len or not keep_seen:
        die("retained body length / kept clause")
    if (nc, retained, removed, deleted_bytes) != COUNTS:
        die("counts %r" % ((nc, retained, removed, deleted_bytes),))
    if not (full_hex == d["source_base_sha256"] == m["source_base_cnf_sha256"] == recipe["source_base_sha256"]
            == bres["source_cnf_sha256"]):
        die("source CNF hash " + full_hex)
    body_hex = sha_bytes(body)
    weak = hashlib.sha256(WEAK_HEADER)
    weak.update(body)
    weak_hex = weak.hexdigest()
    if not (weak_hex == m["base_cnf_sha256"] == recipe["weakened_base_sha256"] == bres["weak_base_sha256"]):
        die("weak base hash")
    if not (body_hex == recipe["weakened_body_sha256"] == bres["body_sha256"]):
        die("body hash")
    if (m["base_vars"], m["base_clauses"]) != (509915, COUNTS[1]):
        die("manifest base counts")
    # Template table -> support lists -> unit literals (the parent binding's own derivation, replicated).
    text = raw[TABLE_REL].decode()
    B, C = {}, {}
    for line in text.split("\n"):
        if re.match(r"^\| [BC][1-6]=", line):
            fields = line.split("|")
            key = fields[1].strip().split("=")[0]
            supports = [[int(x) for x in t.strip()] for t in fields[2].strip().split(";")]
            if key.startswith("B"):
                B[key] = supports
            else:
                C[key] = supports
    if len(B) != 6 or len(C) != 4:
        die("table parsed count")
    lists = {}
    for pre, tail in (("P0", [[1, 2, 3], [1, 2, 3]]), ("P1", [[2, 3], [1, 2, 3]])):
        for key, vals in B.items():
            lists[pre + "-" + key] = vals + tail
    for key, vals in C.items():
        lists["P2-" + key] = vals
    gmap = json.loads(raw[MAP_REL])
    lookup = {}
    for key, v in gmap["vars"].items():
        n = json.loads(key)
        if n[0] == "g":
            lookup[(n[1], tuple(n[2]), tuple(n[3]))] = v
    if (len(lookup) != 7840 or gmap["meta"]["cnf_sha256"] != full_hex
            or gmap["meta"]["script_sha256"] != PINS["code/gram_a.py"]):
        die("map binding")
    if len(m["cases"]) != 16 or set(lists) != {x["id"] for x in m["cases"]}:
        die("manifest IDs")
    bleaves = {x["id"]: x["cnf_sha256"] for x in bres["leaves"]}
    if set(bleaves) != set(lists) or len(bres["leaves"]) != 16:
        die("parent binding leaves")
    leafpre = hashlib.sha256(LEAF_HEADER)
    leafpre.update(body)
    cases = {}
    for case in m["cases"]:
        cid = case["id"]
        supports = lists[cid]
        if supports != case["supports_row2to7"]:
            die("support table identity " + cid)
        units = []
        for i, S in enumerate(supports, 2):
            for c in range(1, 8):
                v = lookup[(1, (0, c), (i, 0))]
                if v != 49 * c + 7 * i - 6:
                    die("map allocation")
                units.append(v if c in S else -v)
        if units != case["units"] or len(units) != 42:
            die("unit map " + cid)
        ub = b"".join(("%d 0\n" % u).encode("ascii") for u in units)
        hh = leafpre.copy()
        hh.update(ub)
        hx = hh.hexdigest()
        if hx != case["cnf_sha256"] or hx != bleaves[cid]:
            die("leaf identity " + cid)
        if (case["cnf_clauses"] != 5740268 or case["cnf_vars"] != 509915 or not case["run_required"]
                or case["excluded_by_imported_c112"]):
            die("leaf fields " + cid)
        mut = [-units[0]] + units[1:]
        mb = b"".join(("%d 0\n" % u).encode("ascii") for u in mut)
        mh = leafpre.copy()
        mh.update(mb)
        if mh.hexdigest() == hx:
            die("mutation not detected " + cid)
        cases[cid] = {"units": units, "unit_bytes": ub, "supports": supports, "cnf_sha256": hx,
                      "manifest_cnf_sha256": case["cnf_sha256"], "binding_cnf_sha256": bleaves[cid],
                      "cnf_bytes": len(LEAF_HEADER) + body_len + len(ub), "mutant_units": mut,
                      "mutant_unit_bytes": mb, "mutant_cnf_sha256": mh.hexdigest(),
                      "mutant_cnf_bytes": len(LEAF_HEADER) + body_len + len(mb)}
    info = {"pins_verified": dict(PINS), "lane": LANE, "source_cnf": source, "source_cnf_sha256": full_hex,
            "source_header": SOURCE_HEADER.decode().strip(), "leaf_header": LEAF_HEADER.decode().strip(),
            "weak_header": WEAK_HEADER.decode().strip(), "weak_base_sha256": weak_hex, "body_sha256": body_hex,
            "body_bytes": body_len, "counts_source_retained_deleted_deletedbytes": list(COUNTS),
            "deleted_clause_indices": sorted(deleted), "kept_q1_index": keep_i,
            "parent_binding": {"result": BIND_DIR + "/RESULT.json", "result_sha256": bres_sha,
                               "expected_affixes": list(BIND_RESULT_AFFIXES),
                               "script": BIND_DIR + "/parent_binding_v1.py", "script_sha256": bscript_sha,
                               "pre_exec_sha256": bpre_sha, "pins_dict_identical": True,
                               "construction_fragments_present": True},
            "previous_encoder_binding_sha256": OLD_ENCODER_BINDING_SHA,
            "not_rederived_here": "ALO-domain/name-table identity of the four deleted clauses (inherited from the "
                                  "parent binding RESULT above; leaf bytes do not depend on it)",
            "load_seconds": round(time.monotonic() - t0, 2)}
    log("inputs verified: source %s body %s weak %s binding RESULT %s (%.1f s)"
        % (full_hex[:12], body_hex[:12], weak_hex[:12], bres_sha, time.monotonic() - t0))
    return {"body": body, "body_view": memoryview(body).toreadonly(), "cases": cases, "info": info}


# --- strengthened formulas: M_s tails from the bound name map, composed with the regenerated source leaves
def load_strengthened(ctx, log):
    t0 = time.monotonic()
    raw, pins = {}, {}
    for path, exp in ((BINDING, BINDING_SHA), (BIND_SCRIPT, BIND_SCRIPT_SHA), (V1_SCRIPT, V1_SCRIPT_SHA),
                      (NF_R2, NF_R2_SHA), (NF_CHECK, NF_CHECK_SHA), (NF_RESULT, NF_RESULT_SHA),
                      (WORKER_HASHES, WORKER_HASHES_SHA), (V2_SCRIPT, V2_SCRIPT_SHA), (DIFF_V1_V2, DIFF_V1_V2_SHA),
                      (V3_SCRIPT, V3_SCRIPT_SHA), (DIFF_V2_V3, DIFF_V2_V3_SHA), (V4_SCRIPT, V4_SCRIPT_SHA),
                      (DIFF_V3_V4, DIFF_V3_V4_SHA)):
        raw[path] = read_bytes(path)
        if sha_bytes(raw[path]) != exp:
            die("pin mismatch " + path)
        pins[path] = exp
    binding = json.loads(raw[BINDING])
    nf = json.loads(raw[NF_RESULT])
    worker = json.loads(raw[WORKER_HASHES])
    if binding.get("status") != "MATCH" or binding.get("mismatches") or binding["script"]["sha256"] != BIND_SCRIPT_SHA:
        die("BINDING.json status/script")
    if (nf.get("status") != "PASS" or nf.get("name_map_sha256") != PINS[MAP_REL]
            or nf.get("manifest_sha256") != PINS[MANIFEST_REL] or nf.get("script_sha256") != NF_CHECK_SHA):
        die("parent normal-form RESULT fields")
    if {int(k): v["ordered_bytes_sha256"] for k, v in nf["mononomial_clause_checks"].items()} != TAIL_FP:
        die("parent M_s tail fingerprints")
    map_raw = read_bytes(os.path.join(LANE, MAP_REL))
    if sha_bytes(map_raw) != PINS[MAP_REL]:
        die("name map sha256")
    names = json.loads(map_raw)["vars"]
    tails = {}
    for s in sorted(TAIL_FP):
        clauses = []
        for i in range(2, 8):
            for c in range(1, 8):
                for d in range(c + 1, 8):
                    a = names[json.dumps(["g", s, [0, c], [i, 0]])]
                    b = names[json.dumps(["g", s, [0, d], [i, 0]])]
                    clauses.append(tuple(sorted((-a, -b))))
        tb = "".join("%d %d 0\n" % cl for cl in clauses).encode("ascii")
        if len(set(clauses)) != TAIL_CLAUSES or sha_bytes(tb) != TAIL_FP[s]:
            die("M_%d tail differs from the parent fingerprint" % s)
        tails[s] = tb
    m = re.match(br"^p cnf (\d+) (\d+)\n$", LEAF_HEADER)
    if b"p cnf %d %d\n" % (int(m.group(1)), int(m.group(2)) + TAIL_CLAUSES) != STRONG_HEADER:
        die("strengthened header")
    bforms = {f["id"]: f for f in binding["formulas"]}
    wforms = {f["id"]: f for f in worker["formulas"]}
    strong, finfo = {}, {}
    for fid, (template, s, expected) in FORMULAS.items():
        case = ctx["cases"][template]
        tb = tails[s]
        h, n = sha_parts([STRONG_HEADER, ctx["body_view"], case["unit_bytes"], tb])
        if not (h == expected == bforms[fid]["parent_composed_cnf_sha256"] == wforms[fid]["CNF_sha256_PLANNED"]
                and n == bforms[fid]["parent_composed_bytes"] == wforms[fid]["expected_stream_bytes_PLANNED"]
                and case["cnf_sha256"] == bforms[fid]["source_leaf_cnf_sha256"]):
            die("strengthened formula identity " + fid)
        strong[fid] = {"template": template, "square": s, "unit_bytes": case["unit_bytes"], "tail_bytes": tb,
                       "cnf_sha256": h, "cnf_bytes": n}
        finfo[fid] = {"source_template": template, "monomial_square": s, "source_leaf_cnf_sha256": case["cnf_sha256"],
                      "unit_lines_sha256": sha_bytes(case["unit_bytes"]), "tail_sha256": sha_bytes(tb),
                      "cnf_sha256": h, "cnf_bytes": n, "equals_binding_worker_and_brief": True}
    info = {"pins_verified": pins, "binding": {"path": rel(BINDING), "sha256": BINDING_SHA, "status": "MATCH"},
            "strong_header": STRONG_HEADER.decode().strip(),
            "composition": "STRONG_HEADER + unchanged weak body + the source leaf's 42 unit lines + M_s tail",
            "tails": {str(s): {"sha256": sha_bytes(tb), "bytes": len(tb), "clauses": TAIL_CLAUSES}
                      for s, tb in sorted(tails.items())},
            "formulas": finfo, "load_seconds": round(time.monotonic() - t0, 2)}
    log("strengthened formulas bound: %s (%.1f s)" % (", ".join("%s %s" % (k, v["cnf_sha256"][:12])
                                                                for k, v in strong.items()), time.monotonic() - t0))
    ctx["strong"] = strong
    ctx["strong_info"] = info
    return ctx


def worker_prefix(n, expected):
    b = read_bytes(WORKER_RESULTS)
    if b.count(b"\n") < n:
        die("worker RESULTS.jsonl has fewer than %d complete records" % n)
    lines = b.split(b"\n")[:n]
    prefix = b"".join(ln + b"\n" for ln in lines)
    got = sha_bytes(prefix)
    if got != expected:
        die("worker RESULTS.jsonl prefix sha256 %s != %s" % (got, expected))
    recs = {}
    for ln in lines:
        r = json.loads(ln)
        recs[r["id"]] = {k: r.get(k) for k in ("tag", "secs", "aggregate_peak_rss_bytes", "strict_ok", "cnf_sha256",
                                               "solver_returncode", "checker_status_lines")}
    return {"path": WORKER_RESULTS, "prefix_records": n, "prefix_sha256": got, "prefix_bytes": len(prefix),
            "complete_records_at_read": b.count(b"\n"), "read_at": now(), "records": recs,
            "use": "read only to learn IDs, solve seconds and peaks; nothing else is taken from it"}


def check_binaries():
    receipt = json.loads(read_bytes(DRAT_RECEIPT))
    exp = receipt["drat_trim"]["binary_sha256"]
    if exp != DRAT_SHA or not (exp.startswith(DRAT_AFFIXES[0]) and exp.endswith(DRAT_AFFIXES[1])):
        die("drat-trim receipt value " + exp)
    got_d, got_c = sha_file(DRAT), sha_file(CADICAL)
    if got_d != exp:
        die("drat-trim sha256 " + got_d)
    if got_c != CADICAL_SHA:
        die("cadical sha256 " + got_c)
    return {"cadical": {"path": CADICAL, "sha256": got_c, "expected": CADICAL_SHA},
            "drat-trim": {"path": DRAT, "sha256": got_d,
                          "expected_from": rel(DRAT_RECEIPT) + " drat_trim.binary_sha256",
                          "receipt_sha256": sha_file(DRAT_RECEIPT),
                          "upstream": receipt["drat_trim"].get("upstream")},
            "checked_at": now()}


def item_label(item):
    if item["kind"] == "selftest":
        return LABEL_PREFIX + "selftest-" + item["name"]
    if item["kind"] == "formula":
        return LABEL_PREFIX + item["id"]
    die("unknown item kind %r (v5 runs selftest and formula items only)" % item["kind"])


def header_counts(b):
    """[vars, clauses] of a leading 'p cnf' line, or None for the header-less early-close control input."""
    m = re.match(rb"^p cnf (\d+) (\d+)$", bytes(b).split(b"\n", 1)[0])
    return [int(m.group(1)), int(m.group(2))] if m else None


def item_parts(item, ctx):
    if item["kind"] == "selftest":
        s, c, _mode = SELFTESTS[item["name"]]
        return [s], [c]
    if item["kind"] == "formula":
        f = ctx["strong"][item["id"]]
        parts = [STRONG_HEADER, ctx["body_view"], f["unit_bytes"], f["tail_bytes"]]
        return parts, parts
    die("unknown item kind %r (v5 runs selftest and formula items only)" % item["kind"])


# --- the solver -> FIFO -> parent relay -> drat-trim pipeline with measured feeds
def _writer(fd, parts, res, gate=None):
    h, total = hashlib.sha256(), 0
    try:
        if gate is not None:  # early-close control only: write the checker CNF after the solver was reaped
            res["gate_released_by_event"] = gate.wait(HOLD_SECONDS)
        for part in parts:
            mv = memoryview(part)
            off, size = 0, len(mv)
            while off < size:
                n = os.write(fd, mv[off:off + CHUNK])
                h.update(mv[off:off + n])
                off += n
                total += n
        res["ok"] = True
    except Exception as e:  # recorded, never hidden
        res["ok"] = False
        res["error"] = repr(e)
    finally:
        try:
            os.close(fd)
        except OSError as e:
            res["close_error"] = repr(e)
        res["written"] = total
        res["sha256"] = h.hexdigest()


def _start_writer(fd, parts, gate=None):
    res = {"ok": False, "expected_len": sum(len(p) for p in parts)}
    t = threading.Thread(target=_writer, args=(fd, parts, res, gate), daemon=True)
    t.start()
    return t, res


def _relay(src, dst, res, mode, hold):
    """Parent proof relay: solver FIFO (src) -> sha256/count -> checker stdin pipe (dst). One CHUNK in flight.
    'read' = bytes read from the FIFO (the proof stream); 'delivered' = bytes os.write() accepted into the checker's
    pipe. Modes: 'plain' delivers everything; 'truncate' (control) never delivers the last TRUNCATE_BYTES; 'suffix'
    (control) delivers SUFFIX after the FIFO EOF. hold (early-close control only) delays the first delivery until the
    checker was reaped. fifo_eof_seen is set only when read() returns b''. A delivery error (EPIPE or another write
    error) stops delivery, but the FIFO is still read and hashed to EOF so the solver never blocks; drain (read)
    errors, close errors and exceptions are recorded separately. ok = EOF seen and no error of any kind."""
    hin, hout = hashlib.sha256(), hashlib.sha256()
    st = {"nin": 0, "nout": 0, "open_out": True}
    keep = TRUNCATE_BYTES if mode == "truncate" else 0
    tail = b""

    def deliver(data):
        if hold is not None and "hold_released_by_event" not in res:
            res["hold_released_by_event"] = hold.wait(HOLD_SECONDS)
        mv, off = memoryview(data), 0
        while off < len(mv):
            try:
                n = os.write(dst, mv[off:off + CHUNK])
            except OSError as e:
                res["delivery_error"] = ("%s: the checker's proof input refused bytes after %d delivered of %d read"
                                         % ("EPIPE" if isinstance(e, BrokenPipeError) else repr(e), st["nout"],
                                            st["nin"]))
                res["delivery_error_at"] = now()
                st["open_out"] = False
                return
            hout.update(mv[off:off + n])
            off += n
            st["nout"] += n

    try:
        while True:
            try:
                data = os.read(src, CHUNK)
            except OSError as e:
                res["drain_error"] = "read: %r after %d read bytes" % (e, st["nin"])
                break
            if not data:
                res["fifo_eof_seen"] = True
                res["fifo_eof_at"] = now()
                break
            if st["nin"] == 0:
                res["first_read_at"] = now()
            hin.update(data)
            st["nin"] += len(data)
            if st["open_out"]:
                if keep:
                    data = tail + data
                    tail, data = data[-keep:], data[:-keep]
                if data:
                    deliver(data)
        if mode == "suffix" and res.get("fifo_eof_seen") and st["open_out"]:
            before = st["nout"]
            deliver(SUFFIX)
            res["suffix_delivered_bytes"] = st["nout"] - before
    except Exception as e:  # recorded, never hidden
        res["relay_exception"] = repr(e)
    finally:
        close_errors = []
        for name, fd in (("dst", dst), ("src", src)):
            try:
                os.close(fd)
            except OSError as e:
                close_errors.append("%s: %r" % (name, e))
        res.update({"read_bytes": st["nin"], "read_sha256": hin.hexdigest(), "delivered_bytes": st["nout"],
                    "delivered_sha256": hout.hexdigest(), "withheld_bytes": len(tail), "close_errors": close_errors,
                    "finished_at": now(), "finished_mono": time.monotonic()})
        res["ok"] = (res.get("fifo_eof_seen") is True and not close_errors
                     and not any(k in res for k in ("delivery_error", "drain_error", "relay_exception")))


def _start_relay(src, dst, mode, hold):
    res = {"ok": False, "mode": mode, "chunk_bytes": CHUNK}
    t = threading.Thread(target=_relay, args=(src, dst, res, mode, hold), daemon=True)
    t.start()
    return t, res


def _lines(b):
    text = b.replace(b"\r", b"")
    return text, text.split(b"\n")


def pipeline(label, solver_parts, checker_parts, projected, log, stop, relay_mode="plain", early_close=False):
    fifo = os.path.join(DESK, "fifo", label + ".drat.fifo")
    slog = os.path.join(DESK, "logs", label + ".solver.log")
    clog = os.path.join(DESK, "logs", label + ".checker.log")
    tdir = os.path.join(TMP, label)
    stmp, ctmp = os.path.join(tdir, "solver"), os.path.join(tdir, "checker")
    for path in (fifo, slog, clog, tdir):
        if os.path.lexists(path):
            raise FileExistsError(path)
    os.mkdir(tdir)
    os.mkdir(stmp)
    os.mkdir(ctmp)
    senv, cenv = dict(ENV, TMPDIR=stmp + "/"), dict(ENV, TMPDIR=ctmp + "/")
    solver_argv = [CADICAL, "-q", "-t", str(SOLVER_SECONDS)]
    rec = {"label": label, "fifo": rel(fifo), "solver_log": rel(slog), "checker_log": rel(clog),
           "solver_argv": solver_argv + ["/dev/fd/<solver-cnf-pipe>", rel(fifo)],
           "checker_argv": [DRAT, "/dev/fd/<checker-cnf-pipe>", "-i", "-t", str(CHECKER_SECONDS)],
           "checker_stdin": "anonymous pipe written only by the parent relay thread, which reads the named FIFO %s "
                            "(read end opened by the parent before any child starts; parent keeps a FIFO write end "
                            "until the solver is reaped)" % rel(fifo),
           "relay_mode": relay_mode, "early_close_control": early_close,
           "cwd": {"solver": rel(stmp), "checker": rel(ctmp)}, "env": {"solver": senv, "checker": cenv},
           "projected_peak_bytes": projected, "desk_stop_bytes": projected + DESK_MARGIN,
           "lane_stop_bytes": STOP_LANE_RSS, "free_floor_bytes": FLOOR, "wall_backstop_seconds": BACKSTOP,
           "stale_lane_reading_seconds": STALE_SECONDS, "stops": STOPS}
    fds, procs, done, writers, events, rss_fail = {}, {}, {}, {}, [], {}
    ev_solver, ev_checker = threading.Event(), threading.Event()
    relay, scanner = None, Scanner()
    peak_desk = peak_lane = peak_other = other_rss = 0
    max_other_busy = 0
    min_free = None
    reason, term_at, grace_exceeded = None, None, False
    last_mono, prev_cpu, prev_mono, scan_started = None, None, None, None

    def close_fd(name):
        fd = fds.pop(name, None)
        if fd is not None:
            os.close(fd)

    def reap():
        for name, p in procs.items():
            if name in done:
                continue
            pid, status, ru = os.wait4(p.pid, os.WNOHANG)
            if pid:
                rc = os.waitstatus_to_exitcode(status)
                p.returncode = rc
                done[name] = {"rc": rc, "maxrss_bytes": ru.ru_maxrss,
                              "wall_seconds": round(time.monotonic() - t0, 3),
                              "user_seconds": round(ru.ru_utime, 3), "sys_seconds": round(ru.ru_stime, 3),
                              "reaped_at": now(), "reaped_mono": time.monotonic()}
                if name == "solver":
                    close_fd("keepalive")
                    ev_solver.set()
                else:
                    ev_checker.set()

    def term_live(why):
        for n, p in procs.items():
            if n not in done:
                try:
                    os.kill(p.pid, signal.SIGTERM)
                    events.append({"at": now(), "event": "SIGTERM", "target": n, "pid": p.pid, "reason": why})
                except ProcessLookupError:
                    pass

    rec["started_at"] = now()
    t0 = time.monotonic()
    os.mkfifo(fifo)
    with open(clog, "xb") as cl, open(slog, "xb") as sl:
        try:  # one cleanup scope for everything from the first fd to the last reap
            fds["fifo_read"] = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
            fcntl.fcntl(fds["fifo_read"], fcntl.F_SETFL,
                        fcntl.fcntl(fds["fifo_read"], fcntl.F_GETFL) & ~os.O_NONBLOCK)
            fds["keepalive"] = os.open(fifo, os.O_WRONLY)
            fds["ccr"], fds["ccw"] = os.pipe()
            fds["cpr"], fds["cpw"] = os.pipe()
            check = None
            if stop.get("signal"):  # latched SIGTERM: no spawn
                rec["stop_latched_before_spawn"] = "checker"
                reason = "driver received %s before the checker spawn" % stop["signal"]
            else:
                try:
                    check = subprocess.Popen([DRAT, "/dev/fd/%d" % fds["ccr"], "-i", "-t", str(CHECKER_SECONDS)],
                                             stdin=fds["cpr"], stdout=cl, stderr=subprocess.STDOUT,
                                             pass_fds=(fds["ccr"],), cwd=ctmp, env=cenv)
                except OSError as e:
                    rec["checker_spawn_error"] = repr(e)
            if check is not None:
                procs["checker"] = check
                rec["checker_pid"] = check.pid
                close_fd("cpr")
                close_fd("ccr")
                relay = _start_relay(fds.pop("fifo_read"), fds.pop("cpw"), relay_mode,
                                     ev_checker if early_close else None)
                writers["checker_feed"] = _start_writer(fds.pop("ccw"), checker_parts,
                                                        ev_solver if early_close else None)
                fds["scr"], fds["scw"] = os.pipe()
                solve = None
                if stop.get("signal"):  # latched SIGTERM: no solver spawn; the checker is stopped below
                    rec["stop_latched_before_spawn"] = "solver"
                    reason = "driver received %s before the solver spawn" % stop["signal"]
                else:
                    try:
                        solve = subprocess.Popen(solver_argv + ["/dev/fd/%d" % fds["scr"], fifo],
                                                 stdin=subprocess.DEVNULL, stdout=sl, stderr=subprocess.STDOUT,
                                                 pass_fds=(fds["scr"],), cwd=stmp, env=senv)
                    except OSError as e:
                        rec["solver_spawn_error"] = repr(e)
                close_fd("scr")
                if solve is not None:
                    procs["solver"] = solve
                    rec["solver_pid"] = solve.pid
                    writers["solver_feed"] = _start_writer(fds.pop("scw"), solver_parts)
                else:
                    close_fd("scw")
                    close_fd("keepalive")
                log("launched %s: checker pid %s, solver pid %s" % (label, rec.get("checker_pid"),
                                                                     rec.get("solver_pid")))
            if reason is not None and procs:
                term_at = time.monotonic()
                term_live(reason)
                log("SAFETY STOP %s: %s" % (label, reason))
            if procs:
                scanner.start()
                scan_started = time.monotonic()
            while procs:
                reap()
                if len(done) == len(procs):
                    break
                tnow = time.monotonic()
                guard_fail = None
                own = taskinfo(os.getpid())
                desk = own[0] if own else 0
                if own is None:
                    guard_fail = "driver RSS unreadable"
                for n, p in procs.items():
                    if n in done:
                        continue
                    t = taskinfo(p.pid)
                    if t is None:  # one miss can be an exit between wait4 and the read; two in a row cannot
                        rss_fail[n] = rss_fail.get(n, 0) + 1
                        if rss_fail[n] >= 2 and guard_fail is None:
                            guard_fail = "own child %s (pid %d) RSS unreadable twice in a row" % (n, p.pid)
                    else:
                        rss_fail[n] = 0
                        desk += t[0]
                peak_desk = max(peak_desk, desk)
                reading = scanner.reading()
                if reading is None:
                    if tnow - scan_started > STALE_SECONDS and guard_fail is None:
                        guard_fail = "no lane scan reading within %.0f s" % STALE_SECONDS
                else:
                    mono, scan, err = reading
                    if scan is None:
                        guard_fail = guard_fail or "lane scan failed: %s" % err
                    elif tnow - mono > STALE_SECONDS:
                        guard_fail = guard_fail or "lane scan reading stale (%.1f s old)" % (tnow - mono)
                    elif mono != last_mono:
                        last_mono = mono
                        other_rss = sum(c["rss_bytes"] for c in scan)
                        busy, cpu = 0, {}
                        for c in scan:
                            cpu[c["pid"]] = c["cpu_ns"]
                            if c["native"]:
                                busy += 1
                            elif (prev_cpu is not None and c["cpu_ns"] is not None
                                  and prev_cpu.get(c["pid"]) is not None and mono > prev_mono):
                                if (c["cpu_ns"] - prev_cpu[c["pid"]]) / ((mono - prev_mono) * 1e9) >= HOT_CPU_FRACTION:
                                    busy += 1
                        prev_cpu, prev_mono = cpu, mono
                        max_other_busy = max(max_other_busy, busy)
                        peak_other = max(peak_other, other_rss)
                lane_total = other_rss + desk
                peak_lane = max(peak_lane, lane_total)
                fb = free_bytes()
                min_free = fb if min_free is None else min(min_free, fb)
                if reason is None:
                    if stop.get("signal"):
                        reason = "driver received %s" % stop["signal"]
                    elif guard_fail is not None:
                        reason = "guard reading failed: " + guard_fail
                    elif lane_total > STOP_LANE_RSS:
                        reason = ("lane RSS %d > 7.85 GiB (%d): other lane %d + desk %d"
                                  % (lane_total, STOP_LANE_RSS, other_rss, desk))
                    elif desk > projected + DESK_MARGIN:
                        reason = "desk aggregate RSS %d > projected + 0.5 GiB (%d)" % (desk, projected + DESK_MARGIN)
                    elif fb < FLOOR:
                        reason = "free bytes %d < in-flight floor %d" % (fb, FLOOR)
                    elif tnow - t0 > BACKSTOP:
                        reason = "wall %.1f s > solver+checker+120 s (%d s)" % (tnow - t0, BACKSTOP)
                    elif time.time() >= NATIVE_STOP_AT:
                        reason = "host clock reached the native-work deadline 2026-10-18 17:57:00 PDT"
                    elif "checker" in done and "solver" in procs and "solver" not in done:
                        reason = "checker exited (rc %s) while the solver was still running" % done["checker"]["rc"]
                    if reason is not None:
                        term_at = time.monotonic()
                        term_live(reason)
                        log("SAFETY STOP %s: %s" % (label, reason))
                elif time.monotonic() - term_at > SIGTERM_GRACE:
                    grace_exceeded = True
                    events.append({"at": now(), "event": "SIGTERM grace of 120 s exceeded; no escalation",
                                   "alive": [n for n in procs if n not in done]})
                    log("SIGTERM grace exceeded for %s; no escalation" % label)
                    break
                time.sleep(SAMPLE)
        except BaseException as e:  # SIGTERM own children, bounded reap, UNKNOWN; cmd_run launches nothing more
            rec["exception"] = "%s: %s" % (type(e).__name__, e)
            rec["exception_traceback"] = traceback.format_exc()[-4000:]
            if reason is None:
                reason = "exception in pipeline: " + rec["exception"]
            term_live(reason)
            try:
                log("EXCEPTION in pipeline %s: %s" % (label, rec["exception"]))
            except Exception as e3:  # recorded, never hidden (e.g. a full disk refusing the log line)
                events.append({"at": now(), "event": "driver log write failed", "error": repr(e3)})
            t_end = time.monotonic() + SIGTERM_GRACE
            while any(n not in done for n in procs) and time.monotonic() < t_end:
                try:
                    reap()
                except Exception as e2:  # recorded, never hidden
                    events.append({"at": now(), "event": "reap failed during exception cleanup", "error": repr(e2)})
                    break
                time.sleep(SAMPLE)
            if any(n not in done for n in procs):
                grace_exceeded = True
                events.append({"at": now(), "event": "children alive after exception cleanup; no escalation",
                               "alive": [n for n in procs if n not in done]})
        finally:
            scanner.halt.set()
            for name in list(fds):
                try:
                    close_fd(name)
                except OSError as e:
                    events.append({"at": now(), "event": "fd close failed", "fd": name, "error": repr(e)})
    if scanner.is_alive():
        scanner.join(3 * (HELPER_DEADLINE + HELPER_TERM_WAIT) + 2)
    rec["lane_scanner"] = {"scans": scanner.scans, "failures": scanner.failures, "alive_after_join": scanner.is_alive()}
    for name, (t, res) in writers.items():
        t.join(5.0 if grace_exceeded else HOLD_SECONDS + 5.0)
        res["thread_finished"] = not t.is_alive()
    if relay is not None:
        relay[0].join(5.0 if grace_exceeded else HOLD_SECONDS + 30.0)
        relay[1]["thread_finished"] = not relay[0].is_alive()
    rel_res = dict(relay[1]) if relay is not None else {"ok": False, "relay_exception": "relay not started"}
    c_mono = done.get("checker", {}).get("reaped_mono")
    rel_res["checker_exited_before_relay_finished"] = (None if c_mono is None or "finished_mono" not in rel_res
                                                       else c_mono < rel_res["finished_mono"])
    rec["relay"] = rel_res
    rec["proof_stream_sha256"] = rel_res.get("read_sha256")
    rec["proof_stream_bytes"] = rel_res.get("read_bytes")
    rec["finished_at"] = now()
    rec["pipeline_seconds"] = round(time.monotonic() - t0, 3)
    rec["children"] = done
    rec["writers"] = {k: dict(v[1]) for k, v in writers.items()}
    rec["peak_desk_aggregate_rss_bytes"] = peak_desk
    rec["peak_lane_other_rss_bytes"] = peak_other
    rec["peak_lane_total_rss_bytes"] = peak_lane
    rec["max_lane_other_busy_in_flight"] = max_other_busy
    rec["min_free_bytes_in_flight"] = min_free
    rec["safety_stop_reason"] = reason
    rec["sigterm_grace_exceeded"] = grace_exceeded
    rec["events"] = events
    sbytes, cbytes = read_bytes(slog), read_bytes(clog)
    _stext, slines = _lines(sbytes)
    ctext, clines = _lines(cbytes)
    rec["solver_log_sha256"], rec["solver_log_bytes"] = sha_bytes(sbytes), len(sbytes)
    rec["solver_status_lines"] = [ln.decode("ascii", "replace") for ln in slines if ln.startswith(b"s")]
    if len(sbytes) <= 4096:
        rec["solver_log_text"] = sbytes.decode("ascii", "replace")
    rec["checker_log_sha256"], rec["checker_log_bytes"] = sha_bytes(cbytes), len(cbytes)
    rec["checker_status_lines"] = [ln.decode("ascii", "replace") for ln in clines if ln.startswith(b"s")]
    rec["solver_status_lines_raw"] = [ln.decode("utf-8", "backslashreplace") for ln in sbytes.split(b"\n")
                                      if ln.replace(b"\r", b"").startswith(b"s")]
    rec["checker_status_lines_raw"] = [ln.decode("utf-8", "backslashreplace") for ln in cbytes.split(b"\n")
                                       if ln.replace(b"\r", b"").startswith(b"s")]
    pm = re.search(rb"c parsing input formula with (\d+) variables and (\d+) clauses", ctext)
    rec["checker_parsed_header_counts"] = [int(pm.group(1)), int(pm.group(2))] if pm else None
    rec["checker_early_eof_marker"] = b"early EOF" in ctext or b"clauses less than expected" in ctext
    pb = re.search(rb"c finished parsing, read (\d+) bytes from proof file", ctext)
    rec["checker_parsed_proof_bytes"] = int(pb.group(1)) if pb else None
    rec["checker_has_verified_line"] = b"s VERIFIED" in clines
    rec["checker_has_not_verified"] = b"s NOT VERIFIED" in clines or b"s NOT VERIFIED" in ctext
    rec["checker_has_timeout"] = b"s TIMEOUT" in clines or b"s TIMEOUT" in ctext
    rec["checker_line_s_NOT_VERIFIED_exact"] = b"s NOT VERIFIED" in clines
    rec["checker_header_error_line"] = DRAT_NO_HEADER_LINE in clines
    rec["checker_info_lines"] = [ln.decode("ascii", "replace").strip() for ln in clines
                                 if ln.startswith(b"c") and any(k in ln for k in INFO_KEYS)][:40]
    return rec


def solver_reported_sat(rec):
    s = rec.get("children", {}).get("solver", {})
    return s.get("rc") == 10 or "s SATISFIABLE" in (rec.get("solver_status_lines") or [])


def feed_ok(w, n, e):
    """A measured CNF feed: no write or close error, thread finished, all n bytes written, sha256 == e."""
    return (w.get("ok") is True and "error" not in w and "close_error" not in w and w.get("thread_finished") is True
            and w.get("written") == n and w.get("sha256") == e)


def relay_clean(r):
    """FIFO EOF seen via read() == b'', no delivery/drain/close error or exception, relay thread finished."""
    return (r.get("ok") is True and r.get("fifo_eof_seen") is True and r.get("thread_finished") is True
            and not r.get("close_errors")
            and not any(k in r for k in ("delivery_error", "drain_error", "relay_exception")))


def relay_complete_and_equal(rec):
    r = rec.get("relay") or {}
    return (relay_clean(r) and r.get("mode") == "plain" and r.get("withheld_bytes") == 0
            and isinstance(r.get("read_bytes"), int) and r["read_bytes"] > 0
            and r["read_bytes"] == r.get("delivered_bytes") and r.get("read_sha256") == r.get("delivered_sha256"))


def evaluate(rec, item):
    exp_s, len_s = item["expected_solver_feed_sha256"], item["expected_solver_feed_bytes"]
    exp_c, len_c = item["expected_checker_feed_sha256"], item["expected_checker_feed_bytes"]
    s = rec.get("children", {}).get("solver", {})
    c = rec.get("children", {}).get("checker", {})
    sw = rec.get("writers", {}).get("solver_feed", {})
    cw = rec.get("writers", {}).get("checker_feed", {})
    r = rec.get("relay") or {}
    complete = (rec.get("safety_stop_reason") is None and not rec.get("sigterm_grace_exceeded")
                and "exception" not in rec and "solver_spawn_error" not in rec and "checker_spawn_error" not in rec)
    crit = {
        "solver_rc_20": s.get("rc") == 20,
        "solver_status_lines_exact": rec.get("solver_status_lines") == ["s UNSATISFIABLE"],
        "checker_rc_0": c.get("rc") == 0,
        "checker_line_s_VERIFIED": bool(rec.get("checker_has_verified_line")),
        "checker_no_s_NOT_VERIFIED": not rec.get("checker_has_not_verified", True),
        "checker_no_s_TIMEOUT": not rec.get("checker_has_timeout", True),
        "no_safety_stop": complete,
        "solver_feed_measured_ok": feed_ok(sw, len_s, exp_s),
        "checker_feed_measured_ok": feed_ok(cw, len_c, exp_c),
        "checker_parsed_header_counts_no_early_eof": (rec.get("checker_parsed_header_counts")
                                                      == item.get("expected_checker_header_counts")
                                                      and rec.get("checker_early_eof_marker") is False),
        "relay_complete_and_equal": relay_complete_and_equal(rec),
        "checker_parsed_proof_bytes_equal_delivered": (rec.get("checker_parsed_proof_bytes") is not None
                                                       and rec.get("checker_parsed_proof_bytes")
                                                       == r.get("delivered_bytes")),
    }
    failed = [k for k, v in crit.items() if not v]
    if item["kind"] == "formula":  # brief: PASS iff every criterion holds; anything else is UNKNOWN, with reasons
        if not failed:
            return "PASS", [], crit
        notes = []
        if solver_reported_sat(rec):
            notes.append("solver reported SATISFIABLE (rc %s); its full output, including any model, is kept in the "
                         "solver log; the desk launches nothing more" % s.get("rc"))
        if rec.get("checker_has_not_verified"):
            notes.append("checker printed s NOT VERIFIED")
        if any(w.get("written") == n and w.get("sha256") != e for w, n, e in ((sw, len_s, exp_s), (cw, len_c, exp_c))):
            notes.append("a measured feed sha256 differs from the bound strengthened hash")
        if rec.get("safety_stop_reason"):
            notes.append("safety stop: " + rec["safety_stop_reason"])
        if not crit["relay_complete_and_equal"]:
            notes.append("relay: eof %s, delivery %s, drain %s, close %s, exception %s, read %s B, delivered %s B, "
                         "withheld %s B, thread finished %s"
                         % (r.get("fifo_eof_seen"), r.get("delivery_error"), r.get("drain_error"),
                            r.get("close_errors"), r.get("relay_exception"), r.get("read_bytes"),
                            r.get("delivered_bytes"), r.get("withheld_bytes"), r.get("thread_finished")))
        if not crit["checker_parsed_proof_bytes_equal_delivered"]:
            notes.append("checker parsed proof bytes %s vs relay delivered %s"
                         % (rec.get("checker_parsed_proof_bytes"), r.get("delivered_bytes")))
        return "UNKNOWN", notes + failed, crit
    mode = item["mode"]  # selftest: the five relay controls; any deviation is INVALID_CONTROL and stops the run
    if mode == "refutation":
        return ("PASS", [], crit) if not failed else ("INVALID_CONTROL", failed, crit)
    base = ("no_safety_stop", "solver_feed_measured_ok", "checker_feed_measured_ok", "solver_rc_20",
            "solver_status_lines_exact")
    bad = [k for k in base if not crit[k]]
    if mode == "negative":
        seen = (crit["relay_complete_and_equal"] and crit["checker_parsed_proof_bytes_equal_delivered"]
                and c.get("rc") == 1 and rec.get("checker_line_s_NOT_VERIFIED_exact") is True
                and not rec.get("checker_has_verified_line")
                and rec.get("checker_parsed_header_counts") == item.get("expected_checker_header_counts")
                and rec.get("checker_early_eof_marker") is False)
    elif mode == "relay-truncate":
        seen = (relay_clean(r) and r.get("mode") == "truncate" and r.get("withheld_bytes") == TRUNCATE_BYTES
                and (r.get("read_bytes") or 0) > TRUNCATE_BYTES
                and r.get("delivered_bytes") == r["read_bytes"] - TRUNCATE_BYTES
                and r.get("read_sha256") != r.get("delivered_sha256") and not crit["relay_complete_and_equal"])
    elif mode == "relay-suffix":
        seen = (relay_clean(r) and r.get("mode") == "suffix" and r.get("suffix_delivered_bytes") == len(SUFFIX)
                and (r.get("read_bytes") or 0) > 0 and r.get("delivered_bytes") == r["read_bytes"] + len(SUFFIX)
                and rec.get("checker_parsed_proof_bytes") == r.get("delivered_bytes")
                and not crit["relay_complete_and_equal"])
    elif mode == "early-close":
        seen = (str(r.get("delivery_error", "")).startswith("EPIPE") and r.get("delivered_bytes") == 0
                and r.get("fifo_eof_seen") is True and not r.get("close_errors")
                and "drain_error" not in r and "relay_exception" not in r and r.get("thread_finished") is True
                and (r.get("read_bytes") or 0) > 0 and r.get("hold_released_by_event") is True
                and cw.get("gate_released_by_event") is True and c.get("rc") == 0
                and rec.get("checker_header_error_line") is True and not rec.get("checker_status_lines")
                and rec.get("checker_parsed_proof_bytes") is None)
    else:
        die("unknown control mode " + str(mode))
    if bad or not seen:
        return "INVALID_CONTROL", bad + ([] if seen else ["preregistered control observation missing"]), crit
    if mode == "negative":
        return "AS_PREREGISTERED_NOT_VERIFIED", [], crit
    return "AS_PREREGISTERED_FAIL_CLOSED", failed, crit


# --- subcommands
def check_env():
    if os.environ.get("TMPDIR") != TMP + "/":
        die("TMPDIR must be %s/" % TMP)
    os.chdir(TMP)


def validate_controls(script_sha):
    """Admission prerequisite for formulas: the five v5 control receipts exist for THIS script sha, the pinned
    binaries and their own PRE-EXEC (sha re-hashed), each with its preregistered verdict and no latched stop.
    -> (identities, problems)."""
    out, problems = [], []
    for name, (_s, _c, mode) in SELFTESTS.items():
        label = LABEL_PREFIX + "selftest-" + name
        path = os.path.join(DESK, "receipts", label + ".json")
        if not os.path.isfile(path):
            problems.append("%s: receipt missing" % label)
            continue
        raw = read_bytes(path)
        r = json.loads(raw)
        pe = r.get("pre_exec") or {}
        pre_path = os.path.join(DESK, pe.get("path", ""))
        bins = r.get("binaries") or {}
        bad = [k for k, ok in (
            ("schema", r.get("schema") == RECEIPT_SCHEMA),
            ("script sha256", (r.get("script") or {}).get("sha256") == script_sha),
            ("item", r.get("kind") == "selftest" and r.get("name") == name
             and (r.get("item") or {}).get("mode") == mode),
            ("verdict %s" % r.get("verdict"), r.get("verdict") == SELFTEST_WANT[mode]),
            ("binaries", (bins.get("cadical") or {}).get("sha256") == CADICAL_SHA
             and (bins.get("drat-trim") or {}).get("sha256") == DRAT_SHA),
            ("pre-exec binding", os.path.isfile(pre_path) and sha_file(pre_path) == pe.get("sha256")),
            ("stop latched", not r.get("stop_latched")),
        ) if not ok]
        if bad:
            problems.append("%s: %s" % (label, ", ".join(bad)))
            continue
        out.append({"label": label, "receipt": rel(path), "receipt_sha256": sha_bytes(raw), "verdict": r["verdict"],
                    "pre_exec": pe, "run_tag": r.get("run_tag")})
    return out, problems


def cmd_preexec(argv):
    check_env()
    if not argv:
        die("preexec OUT [--worker-prefix N SHA] ITEM...")
    out = os.path.abspath(argv[0])
    specs = argv[1:]
    prefix_n, prefix_sha = WORKER_PREFIX
    if specs and specs[0] == "--worker-prefix":
        prefix_n, prefix_sha = int(specs[1]), specs[2]
        specs = specs[3:]
    if not out.startswith(DESK + "/") or os.path.lexists(out):
        die("pre-exec path must be new and inside the desk")
    started = now()
    ctx = load_strengthened(load_inputs(print), print)
    dtext = read_bytes(DIFF)
    if ("replay_v5.py sha256 %s" % sha_file(SCRIPT)).encode() not in dtext:
        die("the recorded diff does not name this script's sha256")
    worker = worker_prefix(prefix_n, prefix_sha)
    binaries = check_binaries()
    items, seen = [], set()
    for spec in specs:
        if spec in seen:
            die("duplicate item " + spec)
        seen.add(spec)
        kind, _, name = spec.partition(":")
        if kind == "selftest":
            if name not in SELFTESTS:
                die("unknown selftest " + name)
            s, c, mode = SELFTESTS[name]
            items.append({"item": spec, "kind": kind, "name": name, "mode": mode,
                          "expected_solver_feed_sha256": sha_bytes(s), "expected_solver_feed_bytes": len(s),
                          "expected_checker_feed_sha256": sha_bytes(c), "expected_checker_feed_bytes": len(c),
                          "projected_peak_bytes": SELFTEST_PROJECTED,
                          "relay_mode": RELAY_MODES[mode], "early_close_control": mode == "early-close",
                          "preregistered_verdict": SELFTEST_WANT[mode],
                          "preregistered_expectation": {
                              "refutation": "PASS under the formula acceptance rules: relay read R == delivered D "
                                            "(equal sha256, EOF seen, no error) == checker-parsed N",
                              "negative": "relay complete and equal and N == D, checker rc 1 with the exact line "
                                          "'s NOT VERIFIED' and the parse line for 3 variables and 7 clauses: an "
                                          "equal digest does not make a proof correct",
                              "relay-truncate": "fail-closed: the relay reads R bytes to EOF but delivers R - %d, read "
                                                "and delivered sha256 differ, no relay error; the acceptance predicate "
                                                "fails on relay_complete_and_equal whatever drat-trim prints (native "
                                                "outcome recorded as observed)" % TRUNCATE_BYTES,
                              "early-close": "fail-closed: the header-less checker input is written only after the "
                                             "solver was reaped; drat-trim exits rc 0 after the exact line 'c ERROR: "
                                             "did not find p cnf line in input file' without a status line or a proof "
                                             "byte count; the relay's first delivery, held until the checker was "
                                             "reaped, gets EPIPE with 0 bytes delivered, and the relay still drains "
                                             "the FIFO to EOF without other errors",
                              "relay-suffix": "fail-closed: after the FIFO EOF the relay delivers the %d-byte "
                                              "deletion suffix 'd 1 2 3 0', so D == R + %d; the checker's parsed "
                                              "proof byte count N == D shows that drat-trim consumed the bytes after "
                                              "the empty clause; the acceptance predicate fails on "
                                              "relay_complete_and_equal (native verdict recorded as observed)"
                                              % (len(SUFFIX), len(SUFFIX))}[mode],
                          "purpose": "relay/pipeline control on a synthetic 3-variable formula; not part of the "
                                     "replay"})
            continue
        if kind == "formula":
            if name not in ctx["strong"]:
                die("unknown formula " + name)
            f = ctx["strong"][name]
            w = worker["records"].get(f["template"])
            peak = w.get("aggregate_peak_rss_bytes") if w else None
            projected = max(3 * peak // 2 if peak else 0, FLOOR_HIGH)
            items.append({"item": spec, "kind": kind, "id": name, "source_template": f["template"],
                          "monomial_square": f["square"],
                          "source_leaf_cnf_sha256": ctx["cases"][f["template"]]["cnf_sha256"],
                          "unit_lines_sha256": sha_bytes(f["unit_bytes"]), "tail_sha256": sha_bytes(f["tail_bytes"]),
                          "bound_cnf_sha256": FORMULAS[name][2],
                          "expected_solver_feed_sha256": f["cnf_sha256"], "expected_solver_feed_bytes": f["cnf_bytes"],
                          "expected_checker_feed_sha256": f["cnf_sha256"],
                          "expected_checker_feed_bytes": f["cnf_bytes"],
                          "worker_source_template_record": w, "projected_peak_bytes": projected,
                          "projected_rule": "max(1.5 x worker aggregate peak %s of source template %s, floor %d)"
                                            % (peak, f["template"], FLOOR_HIGH),
                          "acceptance": ACCEPTANCE})
            continue
        die("bad item %s (v5 takes selftest:NAME and formula:ID only)" % spec)
    kinds = {it["kind"] for it in items}
    if not items or len(kinds) != 1:
        die("a v5 PRE-EXEC holds either only controls or only formulas, and at least one item")
    admission = None
    if kinds == {"formula"}:
        admission, problems = validate_controls(sha_file(SCRIPT))
        if problems:
            die("formula admission refused: " + "; ".join(problems))
    for it in items:
        it["expected_checker_header_counts"] = header_counts(item_parts(it, ctx)[1][0])
        if it["expected_checker_header_counts"] is None and it.get("mode") != "early-close":
            die("no p cnf header in the checker feed of " + it["item"])
    fb = free_bytes()
    busy, other, scan, scan_err = gate_scan()
    pre = {"schema": "moqls8-strengthened-parent-replay-preexec/4", "at": now(), "started_at": started, "desk": DESK,
           "scope": SCOPE,
           "script": {"path": SCRIPT_REL, "sha256": sha_file(SCRIPT)},
           "python": {"executable": sys.executable, "version": sys.version.split()[0], "flags": "-I -B"},
           "binaries": binaries, "inputs": ctx["info"], "inputs_strengthened": ctx["strong_info"],
           "provenance": {"derived_from": V4_SCRIPT, "derived_from_sha256": V4_SCRIPT_SHA, "diff": rel(DIFF),
                          "diff_sha256": sha_bytes(dtext), "v3_script": V3_SCRIPT, "v3_script_sha256": V3_SCRIPT_SHA,
                          "v3_to_v4_diff": rel(DIFF_V3_V4), "v3_to_v4_diff_sha256": DIFF_V3_V4_SHA,
                          "v2_script": V2_SCRIPT, "v2_script_sha256": V2_SCRIPT_SHA,
                          "v2_to_v3_diff": rel(DIFF_V2_V3), "v2_to_v3_diff_sha256": DIFF_V2_V3_SHA,
                          "v1_script": V1_SCRIPT, "v1_script_sha256": V1_SCRIPT_SHA,
                          "v1_to_v2_diff": rel(DIFF_V1_V2), "v1_to_v2_diff_sha256": DIFF_V1_V2_SHA,
                          "bind_script": rel(BIND_SCRIPT), "bind_script_sha256": BIND_SCRIPT_SHA,
                          "binding": rel(BINDING), "binding_sha256": BINDING_SHA},
           "run_kind": "formulas" if admission is not None else "controls", "admission_controls": admission,
           "worker_results": worker, "items": items,
           "acceptance": ACCEPTANCE, "gate": GATE_RULE, "in_flight_stops": STOPS,
           "limits": {"solver_seconds": SOLVER_SECONDS, "checker_seconds": CHECKER_SECONDS,
                      "wall_backstop_seconds": BACKSTOP, "launch_floor_bytes": LAUNCH_FLOOR, "floor_bytes": FLOOR,
                      "gate_lane_rss_bytes": GATE_RSS, "stop_lane_rss_bytes": STOP_LANE_RSS,
                      "desk_margin_bytes": DESK_MARGIN, "lane_busy_cap": LANE_BUSY_CAP, "mine": MINE,
                      "wait_poll_seconds": WAIT_POLL, "wait_budget_seconds": WAIT_BUDGET,
                      "gate_consecutive_passes": GATE_STREAK, "sigterm_grace_seconds": SIGTERM_GRACE,
                      "projected_retained_growth_bytes": 10 * MIB, "no_launch_at": "2026-10-18T17:29:00-07:00",
                      "native_stop_at": "2026-10-18T17:57:00-07:00"},
           "transport": "CNF bytes in parent memory -> anonymous pipes (/dev/fd/N) with per-writer sha256 of the "
                        "bytes written; proof: cadical -> named FIFO in fifo/ -> parent relay thread (sha256 and "
                        "count of the bytes read = proof stream; sha256 and count of the bytes delivered) -> "
                        "anonymous pipe -> drat-trim stdin (-i). No CNF or proof file on disk. Each native tool gets "
                        "its own new TMPDIR and cwd, tmp/<label>/solver/ and tmp/<label>/checker/.",
           "sequencing": "one pipeline at a time, items in the listed order; a PRE-EXEC holds only controls or only "
                         "formulas; formulas are admitted only with the five v5 control receipts of this script sha, "
                         "re-validated before each launch; a control whose verdict differs from its preregistered "
                         "verdict stops the run; after a SAT report, a floor/safety stop, an exception, a driver "
                         "SIGTERM or the 17:29 PDT launch cutoff nothing more is launched; any other UNKNOWN "
                         "continues with the next formula",
           "fresh_check": {"free_bytes": fb, "lane_other_busy": busy, "lane_other_rss_bytes": other,
                           "lane_scan_error": scan_err, "lane_scan": [compact(c) for c in (scan or [])],
                           "monitor_stability": monitor_stability()[1]}}
    digest = write_json_x(out, pre)
    print("PRE-EXEC %s sha256 %s" % (out, digest))
    for it in items:
        print(it["item"], it["expected_solver_feed_sha256"][:12], it["expected_checker_feed_sha256"][:12],
              it["projected_peak_bytes"])


def cmd_run(argv):
    check_env()
    if len(argv) != 1:
        die("run PREEXEC")
    pre_path = os.path.abspath(argv[0])
    pre_raw = read_bytes(pre_path)
    pre, pre_sha = json.loads(pre_raw), sha_bytes(pre_raw)
    script_sha = sha_file(SCRIPT)
    if pre["script"]["sha256"] != script_sha:
        die("script sha256 differs from the pre-exec pin")
    runtag = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    log_path = os.path.join(DESK, "logs", "driver-%s.log" % runtag)
    logf = open(log_path, "x", buffering=1)

    def log(msg):
        line = "%s %s" % (now(), msg)
        logf.write(line + "\n")
        print(line, flush=True)

    stop = {}

    def on_term(signum, _frame):
        stop["signal"] = signal.Signals(signum).name

    signal.signal(signal.SIGTERM, on_term)
    summary = {"schema": "moqls8-strengthened-parent-replay-run/4", "run_tag": runtag, "started_at": now(),
               "pre_exec": {"path": rel(pre_path), "sha256": pre_sha}, "script_sha256": script_sha,
               "driver_log": rel(log_path), "items": [], "events": [], "stopped_reason": None}
    log("run %s start; pre-exec %s sha256 %s; driver pid %d" % (runtag, rel(pre_path), pre_sha, os.getpid()))
    ctx = load_strengthened(load_inputs(log), log)
    summary["strengthened_verified"] = ctx["strong_info"]
    summary["inputs_verified"] = ctx["info"]
    summary["driver_rss_after_load_bytes"] = rss(os.getpid())
    for it in pre["items"]:
        s_parts, c_parts = item_parts(it, ctx)
        if (sha_parts(s_parts) != (it["expected_solver_feed_sha256"], it["expected_solver_feed_bytes"])
                or sha_parts(c_parts) != (it["expected_checker_feed_sha256"], it["expected_checker_feed_bytes"])):
            die("regenerated bytes differ from the pre-exec for " + it["item"])
    log("all %d items regenerated in memory and equal to the pre-exec hashes" % len(pre["items"]))
    budget = {"used": 0.0}
    remaining = list(pre["items"])
    while remaining:
        it = remaining.pop(0)
        label = item_label(it)
        rpath = os.path.join(DESK, "receipts", label + ".json")
        entry = {"item": it["item"], "label": label}
        summary["items"].append(entry)
        if os.path.lexists(rpath):
            if it["kind"] == "selftest":  # never skip a control without checking its receipt
                _ids, probs = validate_controls(script_sha)
                mine = [x for x in probs if x.startswith(label + ":")]
                if mine:
                    entry.update({"status": "STOPPED",
                                  "reason": "existing control receipt invalid: " + "; ".join(mine)})
                    summary["stopped_reason"] = entry["reason"]
                    log("STOPPED %s: %s" % (label, entry["reason"]))
                    break
                entry.update({"status": "SKIPPED_VALIDATED", "reason": "receipt exists and validates for this script"})
            else:
                entry.update({"status": "SKIPPED", "reason": "receipt already exists; a re-run needs parent approval "
                                                             "and a new version name"})
            log("skip %s: %s" % (label, entry["reason"]))
            continue
        if it["kind"] == "formula":  # admission prerequisite, re-validated before every formula launch
            adm, probs = validate_controls(script_sha)
            same = ([(a["label"], a["receipt_sha256"]) for a in adm]
                    == [(a["label"], a["receipt_sha256"]) for a in (pre.get("admission_controls") or [])])
            if probs or not same:
                entry.update({"status": "STOPPED", "reason": "formula admission re-validation failed: %s"
                              % ("; ".join(probs) or "control receipts differ from the PRE-EXEC record")})
                summary["stopped_reason"] = entry["reason"]
                log("STOPPED %s: %s" % (label, entry["reason"]))
                break
            entry["admission_revalidated_at"] = now()
        s_parts, c_parts = item_parts(it, ctx)
        hs, ns = sha_parts(s_parts)
        hc, nc = sha_parts(c_parts)
        pre_launch = {"at": now(), "solver_feed_sha256": hs, "solver_feed_bytes": ns, "checker_feed_sha256": hc,
                      "checker_feed_bytes": nc}
        if it["kind"] == "formula":
            f = ctx["strong"][it["id"]]
            ok = (hs == it["expected_solver_feed_sha256"] == f["cnf_sha256"] == FORMULAS[it["id"]][2]
                  and ns == it["expected_solver_feed_bytes"] == f["cnf_bytes"])
            pre_launch["solver_buffer_equals_binding_and_worker_hash"] = ok
            if not ok:
                die("pre-launch formula hash for " + label)
        if (hs, ns, hc, nc) != (it["expected_solver_feed_sha256"], it["expected_solver_feed_bytes"],
                                it["expected_checker_feed_sha256"], it["expected_checker_feed_bytes"]):
            die("pre-launch buffer hash for " + label)
        bins = check_binaries()
        if sha_file(SCRIPT) != script_sha:
            die("script changed during the run")
        projected = it["projected_peak_bytes"]
        log("gate %s: projected %d" % (label, projected))
        g = gate(label, projected, budget, log, stop, stable=it["kind"] == "formula")
        if not g["launch"]:
            ev = {"at": now(), "event": "deferred" if g.get("deferred") else "stopped", "item": it["item"],
                  "wait_used_total_seconds": round(budget["used"], 1),
                  "last_sample": g["samples"][-1] if g["samples"] else None}
            summary["events"].append(ev)
            entry.update({"status": "DEFERRED" if g.get("deferred") else "STOPPED", "gate": g})
            summary["stopped_reason"] = ("total gate wait budget of 6 h exhausted at %s" % label
                                         if g.get("deferred") else g.get("stopped"))
            log("%s %s" % (entry["status"], label))
            break
        try:
            rec = pipeline(label, s_parts, c_parts, projected, log, stop, relay_mode=it.get("relay_mode", "plain"),
                           early_close=bool(it.get("early_close_control")))
        except BaseException as e:  # pipeline() reaps its own children; this records what escaped its scope
            rec = {"label": label, "exception": "%s: %s" % (type(e).__name__, e),
                   "exception_traceback": traceback.format_exc()[-4000:],
                   "safety_stop_reason": "exception outside the pipeline cleanup scope: %s: %s" % (type(e).__name__, e),
                   "sigterm_grace_exceeded": False, "children": {}, "writers": {}, "relay": {}, "events": []}
            log("EXCEPTION at %s: %s" % (label, rec["exception"]))
        verdict, reasons, crit = evaluate(rec, it)
        receipt = {"schema": RECEIPT_SCHEMA, "label": label, "kind": it["kind"],
                   "id": it.get("id"), "name": it.get("name"),
                   "scope": SCOPE if it["kind"] != "selftest" else it["purpose"],
                   "desk": DESK, "script": {"path": SCRIPT_REL, "sha256": script_sha},
                   "pre_exec": {"path": rel(pre_path), "sha256": pre_sha}, "run_tag": runtag,
                   "binaries": bins, "item": it, "pre_launch_buffer_check": pre_launch, "gate": g, "pipeline": rec,
                   "criteria": crit, "verdict": verdict, "reasons": reasons,
                   "solver_reported_sat": solver_reported_sat(rec), "stop_latched": stop.get("signal"),
                   "written_at": now()}
        rsha = write_json_x(rpath, receipt)
        entry.update({"status": "RECEIPT", "verdict": verdict, "reasons": reasons, "receipt": rel(rpath),
                      "receipt_sha256": rsha, "pipeline_seconds": rec.get("pipeline_seconds"),
                      "gate_waited_seconds": g["waited_seconds"],
                      "peak_desk_aggregate_rss_bytes": rec.get("peak_desk_aggregate_rss_bytes"),
                      "safety_stop_reason": rec.get("safety_stop_reason"), "stop_latched": stop.get("signal")})
        for ev in rec.get("events", []):
            summary["events"].append(dict(ev, item=it["item"]))
        log("%s verdict %s reasons %s receipt sha256 %s" % (label, verdict, reasons, rsha))
        if rec.get("sigterm_grace_exceeded"):
            summary["stopped_reason"] = "SIGTERM grace exceeded at %s; children may still be alive" % label
            break
        if stop.get("signal"):
            summary["stopped_reason"] = "driver received %s (latched; receipt records stop_latched)" % stop["signal"]
            break
        if rec.get("exception"):
            summary["stopped_reason"] = "exception at %s: %s; desk launches nothing more" % (label, rec["exception"])
            break
        if it["kind"] == "selftest":
            want = SELFTEST_WANT[it["mode"]]
            if verdict != want:
                summary["stopped_reason"] = "control %s gave %s, expected %s" % (label, verdict, want)
                break
        if solver_reported_sat(rec):
            summary["stopped_reason"] = ("solver reported SATISFIABLE at %s (rc %s); its output is kept in %s; desk "
                                         "stopped, no further launch" % (label, rec["children"].get("solver", {})
                                                                         .get("rc"), rec.get("solver_log")))
            log("SAT REPORTED %s: desk stops" % label)
            break
        if rec.get("safety_stop_reason") is not None:
            summary["stopped_reason"] = ("floor/safety stop at %s: %s; desk launches nothing more"
                                         % (label, rec["safety_stop_reason"]))
            break
    for it in remaining:
        summary["items"].append({"item": it["item"], "label": item_label(it), "status": "NOT_ATTEMPTED",
                                 "reason": summary["stopped_reason"]})
    summary["wait_budget_seconds"] = WAIT_BUDGET
    summary["wait_used_seconds"] = round(budget["used"], 1)
    summary["finished_at"] = now()
    log("run %s finished; stopped_reason %s" % (runtag, summary["stopped_reason"]))
    logf.close()
    summary["driver_log_sha256_at_close"] = sha_file(log_path)
    digest = write_json_x(os.path.join(DESK, "runs", "run-%s.json" % runtag), summary)
    print("RUN SUMMARY runs/run-%s.json sha256 %s" % (runtag, digest))


def _summ(r, rpath):
    p = r["pipeline"]
    s = p["children"].get("solver", {})
    c = p["children"].get("checker", {})
    sw = p["writers"].get("solver_feed", {})
    cw = p["writers"].get("checker_feed", {})
    it = r["item"]
    return {"label": r["label"], "id": r.get("id"), "kind": r["kind"], "verdict": r["verdict"],
            "reasons": r["reasons"], "receipt": rel(rpath), "receipt_sha256": sha_file(rpath),
            "source_template": it.get("source_template"), "monomial_square": it.get("monomial_square"),
            "bound_cnf_sha256": it.get("bound_cnf_sha256"), "solver_reported_sat": r.get("solver_reported_sat"),
            "criteria": r.get("criteria"),
            "expected_solver_feed_sha256": it["expected_solver_feed_sha256"],
            "expected_checker_feed_sha256": it["expected_checker_feed_sha256"],
            "expected_feed_bytes": [it["expected_solver_feed_bytes"], it["expected_checker_feed_bytes"]],
            "measured_solver_feed": {k: sw.get(k) for k in ("ok", "written", "sha256", "error", "close_error",
                                                            "thread_finished")},
            "measured_checker_feed": {k: cw.get(k) for k in ("ok", "written", "sha256", "error", "close_error",
                                                             "thread_finished", "gate_released_by_event")},
            "proof_stream": {"sha256": p.get("proof_stream_sha256"), "bytes": p.get("proof_stream_bytes"),
                             "delivered_sha256": (p.get("relay") or {}).get("delivered_sha256"),
                             "delivered_bytes": (p.get("relay") or {}).get("delivered_bytes"),
                             "withheld_bytes": (p.get("relay") or {}).get("withheld_bytes"),
                             "suffix_delivered_bytes": (p.get("relay") or {}).get("suffix_delivered_bytes"),
                             "relay_mode": (p.get("relay") or {}).get("mode"),
                             "fifo_eof_seen": (p.get("relay") or {}).get("fifo_eof_seen"),
                             "delivery_error": (p.get("relay") or {}).get("delivery_error"),
                             "drain_error": (p.get("relay") or {}).get("drain_error"),
                             "close_errors": (p.get("relay") or {}).get("close_errors"),
                             "relay_exception": (p.get("relay") or {}).get("relay_exception"),
                             "checker_parsed_proof_bytes": p.get("checker_parsed_proof_bytes")},
            "stop_latched": r.get("stop_latched"), "exception": p.get("exception"),
            "solver": {"rc": s.get("rc"), "status_lines": p.get("solver_status_lines"),
                       "status_lines_raw": p.get("solver_status_lines_raw"),
                       "wall_seconds": s.get("wall_seconds"), "user_seconds": s.get("user_seconds"),
                       "maxrss_bytes": s.get("maxrss_bytes"), "log": p.get("solver_log"),
                       "log_sha256": p.get("solver_log_sha256"), "log_bytes": p.get("solver_log_bytes")},
            "checker": {"rc": c.get("rc"), "status_lines": p.get("checker_status_lines"),
                        "status_lines_raw": p.get("checker_status_lines_raw"),
                        "wall_seconds": c.get("wall_seconds"), "user_seconds": c.get("user_seconds"),
                        "maxrss_bytes": c.get("maxrss_bytes"), "info_lines": p.get("checker_info_lines"),
                        "log": p.get("checker_log"), "log_sha256": p.get("checker_log_sha256"),
                        "log_bytes": p.get("checker_log_bytes")},
            "started_at": p.get("started_at"), "finished_at": p.get("finished_at"),
            "pipeline_seconds": p.get("pipeline_seconds"),
            "peak_desk_aggregate_rss_bytes": p.get("peak_desk_aggregate_rss_bytes"),
            "peak_lane_total_rss_bytes": p.get("peak_lane_total_rss_bytes"),
            "projected_peak_bytes": it.get("projected_peak_bytes"),
            "worker_record": it.get("worker_record") or it.get("worker_source_template_record"),
            "gate": {"decided_at": r["gate"].get("decided_at"), "waited_seconds": r["gate"].get("waited_seconds"),
                     "lane_other_busy_at_launch": r["gate"].get("lane_other_busy_at_launch"),
                     "lane_other_rss_at_launch": r["gate"].get("lane_other_rss_at_launch"),
                     "free_bytes_at_launch": r["gate"].get("free_bytes_at_launch")},
            "safety_stop_reason": p.get("safety_stop_reason"), "events": p.get("events"),
            "preregistered_verdict": it.get("preregistered_verdict"),
            "preregistered_expectation": it.get("preregistered_expectation")}


def cmd_assemble(argv):
    if len(argv) < 2:
        die("assemble OUT PREEXEC...")
    out = os.path.abspath(argv[0])
    if not out.startswith(DESK + "/") or os.path.lexists(out):
        die("result path must be new and inside the desk")
    pres, labels = [], {}
    for p in argv[1:]:
        p = os.path.abspath(p)
        raw = read_bytes(p)
        pre = json.loads(raw)
        if pre.get("script", {}).get("sha256") != sha_file(SCRIPT):
            die("PRE-EXEC %s pins another script" % rel(p))
        for it in pre["items"]:
            lab = item_label(it)
            if lab in labels:
                die("label %s appears in two PRE-EXECs" % lab)
            labels[lab] = (sha_bytes(raw), it)
        pres.append((p, sha_bytes(raw), pre))
    pre_shas = {h for _p, h, _pre in pres}
    runs = []
    for f in sorted(glob.glob(os.path.join(DESK, "runs", "*.json"))):
        rn = json.loads(read_bytes(f))
        if (rn.get("pre_exec") or {}).get("sha256") in pre_shas:
            runs.append((f, sha_file(f), rn))
    receipts, not_assembled = {}, []
    for f in sorted(glob.glob(os.path.join(DESK, "receipts", "*.json"))):
        r = json.loads(read_bytes(f))
        lab = r.get("label")
        if (lab in labels and (r.get("pre_exec") or {}).get("sha256") == labels[lab][0]
                and (r.get("script") or {}).get("sha256") == sha_file(SCRIPT)):
            receipts[lab] = (r, f)
        else:
            not_assembled.append(rel(f))
    groups = {"selftest": [], "formula": []}
    not_run = []
    for _p, _s, pre in pres:
        for it in pre["items"]:
            label = item_label(it)
            if label in receipts:
                r, f = receipts[label]
                groups[it["kind"]].append(_summ(r, f))
                continue
            why = [dict(e, run=rn["run_tag"]) for _f, _h, rn in runs for e in rn["items"] if e["label"] == label]
            not_run.append({"item": it["item"], "label": label,
                            "run_entries": [{k: e.get(k) for k in ("run", "status", "reason")} for e in why]})
    counts = {}
    for e in groups["formula"]:
        counts[e["verdict"]] = counts.get(e["verdict"], 0) + 1
    deferrals = [dict(e, run=rn["run_tag"]) for _f, _h, rn in runs for e in rn["events"]
                 if e.get("event") in ("deferred", "stopped")]
    guards = [dict(e, run=rn["run_tag"]) for _f, _h, rn in runs for e in rn["events"]
              if e.get("event") not in ("deferred", "stopped")]
    allx = groups["selftest"] + groups["formula"]
    first = pres[0][2]
    result = {"schema": "moqls8-strengthened-parent-replay-result/4", "assembled_at": now(), "desk": DESK,
              "scope": SCOPE,
              "statement": "Parent replay of the six exact strengthened formulas only. Results are exact-formula "
                           "facts; transfer to the four open P1 templates depends on separate parent acceptance of "
                           "the normal form r2. No n=8 or Problem-16 conclusion and no theorem claim.",
              "script": {"path": SCRIPT_REL, "sha256": sha_file(SCRIPT)},
              "pre_exec": [{"path": rel(p), "sha256": h} for p, h, _ in pres],
              "binaries": first["binaries"], "inputs": first["inputs"],
              "inputs_strengthened": first["inputs_strengthened"], "provenance": first["provenance"],
              "worker_results_prefix": {k: first["worker_results"][k] for k in
                                        ("path", "prefix_records", "prefix_sha256", "use")},
              "runs": [{"path": rel(f), "sha256": h, "run_tag": rn["run_tag"], "started_at": rn["started_at"],
                        "finished_at": rn.get("finished_at"), "wait_used_seconds": rn.get("wait_used_seconds"),
                        "stopped_reason": rn.get("stopped_reason"), "driver_log": rn.get("driver_log"),
                        "driver_log_sha256": rn.get("driver_log_sha256_at_close")} for f, h, rn in runs],
              "started_at": min([rn["started_at"] for _f, _h, rn in runs], default=None),
              "finished_at": max([rn.get("finished_at") or "" for _f, _h, rn in runs], default=None),
              "formula_verdict_counts": counts, "formulas": groups["formula"],
              "controls": groups["selftest"], "not_run": not_run, "deferrals": deferrals,
              "guard_events": guards, "desk_receipts_not_assembled": not_assembled,
              "peak_rss": {"max_desk_aggregate_sampled_bytes": max([e["peak_desk_aggregate_rss_bytes"] or 0
                                                                    for e in allx], default=None),
                           "max_lane_total_sampled_bytes": max([e["peak_lane_total_rss_bytes"] or 0 for e in allx],
                                                               default=None),
                           "max_child_maxrss_bytes": max([max(e["solver"]["maxrss_bytes"] or 0,
                                                              e["checker"]["maxrss_bytes"] or 0) for e in allx],
                                                         default=None)}}
    digest = write_json_x(out, result)
    print("RESULT %s sha256 %s" % (out, digest))


def main(argv):
    if len(argv) < 2:
        die(__doc__)
    cmd, rest = argv[1], argv[2:]
    if cmd == "preexec":
        cmd_preexec(rest)
    elif cmd == "run":
        cmd_run(rest)
    elif cmd == "assemble":
        cmd_assemble(rest)
    else:
        die("unknown subcommand " + cmd)


if __name__ == "__main__":
    main(sys.argv)
