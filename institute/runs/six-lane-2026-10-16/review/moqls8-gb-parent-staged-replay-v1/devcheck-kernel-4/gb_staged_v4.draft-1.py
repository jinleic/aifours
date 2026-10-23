#!/usr/bin/env python3
"""Parent staged GB replay desk v4: the counted parent replay of the eighteen GB (gram_b_r2) inputs of the MOQLS(8) n8
contract, implementing review/gb-parent-replay-brief-v1.md (sha256 d95f3a0b...27ed) exactly.

v2 = scripts/gb_staged_v1.py (b36fbb57...8151, kept unchanged) + DIFF-gb_staged_v1-to-v2.txt, which repairs only the
six MAJOR findings of the Codex source audit review/n8-gb-staged-v1-source-codex-v1.note.md (480ef541...24a6):
 F1 controls: every control preregisters its exact allowed (normal exit code, status lines) outcome(s) and its narrowly
    allowed fatal-class diagnostics; a checker TIMEOUT, a signal/abnormal termination, an unlisted fatal diagnostic or
    an unlisted outcome vetoes the control whatever may_fail says; science gains independent TIMEOUT and fatal-
    diagnostic criteria. F2 children: ownership slots exist before Popen; a child is marked reaped immediately after
    wait4 returns its pid, before any diagnostic allocation, and is never signalled or waited for again. F3
    descriptors: every os.open/os.pipe result is closed unless its registry insertion committed (acquire()); the
    feeder closes its descriptor in an unconditional nested finally before releasing the buffer or building
    diagnostics. F4 signals: stop, cutoff and deadline are re-checked immediately before each Popen; a signal latched
    during evaluation downgrades the verdict, and qualification needs the separate commit record written after the
    receipt (receipts/<label>.commit.json, qualified only if no signal was latched when the receipt was durable);
    SIGINT is latched like SIGTERM. F5 exclusions: foreign GB natives are identified by cwd/argv in a GB desk or GB
    evidence tree, by orphanhood (ppid 1) and by ownership (parent is a GB driver); the scanner latches the first
    exclusion itself, and the latch is checked at every completion break, before every spawn and at evaluation. F6
    resources: other busy + 1 <= 4 is enforced in flight, and the launch threshold 12.2e9 + 10 MiB (not the 12e9
    floor) is applied immediately before each spawn. Every v2 file name has the 'gbs2-' prefix.

v3 = scripts/gb_staged_v2.py (89db9635...2844, kept unchanged) + DIFF-gb_staged_v2-to-v3.txt, which repairs only the
three MAJOR findings of the Codex re-review review/n8-gb-staged-v2-source-codex-v1.note.md (f39a65cd...fe16):
 F3' every single descriptor is acquired by acquire_open(): the scalar fd returned by os.open() is stored in the
    helper's own cleanup scope before any other operation, and closed unless its registry insertion committed (no
    wrapper tuple exists any more); pipes by acquire_pipe() (os.pipe() returns the pair itself).
 F4' qualification publication is protected: the receipt and its directory are fsynced (+ F_FULLFSYNC) before the
    commit is prepared; publish_commit() blocks SIGTERM/SIGINT, takes the final decision at an explicit
    linearization point (latched signal, pending blocked signals, the driver being the only thread, durable receipt,
    qualifying verdict), writes and fsyncs the commit under <label>.commit.json.prepare, publishes it atomically with
    os.link() to <label>.commit.json (fails if the name exists; nothing is renamed or deleted), fsyncs the directory,
    and only then restores the signal mask, so a signal arriving during publication is handled after it and stops
    the desk. Any durability or publication failure fails closed (no qualified commit) and stops the desk.
Every v3 file name has the 'gbs3-' prefix.

v4 = scripts/gb_staged_v3.py (6f5b3a8a...0f14, kept unchanged) + DIFF-gb_staged_v3-to-v4.txt, which repairs only the
two MAJOR findings of the Codex delta review review/n8-gb-staged-v3-delta-codex-v1.note.md (eb8f8ac4...be17), keeping
the previous cancellation semantics (no snapshot linearization): a SIGTERM/SIGINT latched or pending at ANY point
through the successful publication of an item vetoes that item, and qualification never rests on the early commit
flag. publish_qualification() keeps both signals blocked from the decision through the end of the item's
publication: (1) commit = the decision record (published by link of its synced .prepare file, directory synced);
(2) a post-commit check of latched and pending signals; (3) only if the decision qualified and nothing is pending or
failed, the completion record <label>.complete.json bound to the exact receipt and commit sha256 (same durable link
publication); (4) a post-completion check; (5) any signal or failure after the commit -> the persistent cancellation
veto <label>.cancelled.json, whose exclusive creation alone vetoes (its directory entry is synced first); (6) the
mask is restored and a signal delivered then also cancels the item. The run summary is published the same way
(runs/run-<tag>.json, protected and durable; a signal during it creates runs/run-<tag>.cancelled.json). Admission
(qualification_problems, used by validate_controls and the read-only 'qualification' subcommand) requires the
durable receipt, the qualified commit, the completion bound to both, no item cancellation, and the durable summary of
the producing run with no stop, no signal at the summary, no run cancellation and an entry for the label with
publication COMPLETE and the same digests. Every v4 file name has the 'gbs4-' prefix.

Desk: institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1 (parent-owned, created exclusively
2026-10-18T10:08:20-07:00). Inputs, and no others: the twelve direct templates P1-B4, P0-B4, P0-B5, P0-B6, P1-B6, P2-C4,
P2-C3, P0-B1, P0-B2, P0-B3, P2-C2, P2-C1 and the strengthened P1-B2.M2, P1-B2.M4, P1-B5.M2, P1-B5.M3, P1-B3.M2,
P1-B1.M2. Scope: exact-input proof certification only; no n8 theorem, transfer or novelty claim.

Bytes. Each formula is regenerated in this process's memory and never written to disk. The hash-pinned parent binder
review/moqls8-gb-parent-binding-v1/scripts/bind_gb_v2.py (188c88de...5f51) is executed from its verified bytes into a
fresh module object (nothing is added to sys.modules or sys.path; its main() and generate() writer are never called;
no binding artifact is opened for writing). Its unchanged check_inputs() (pins of code/gram_b_r2.py 4b593e55...beae0 and
of its six other inputs, the exact GB source lines, the AST storage facts, main()'s own parser on --order 8 --quantum
12345 --ngeneric 0 --p4 1 --sb2 --g5 -> encode(8,[1,2,3,4,5],0,[1],True,None,True,False,False)), load_gb() and
make_sink_class() (segmented 16 MiB in-memory clause sink; F.new, F.n, F.tab unchanged) produce the GB base body. The 42
unit lines and the 126-line M_s tail come from that encode's own F.tab through the binder's compose() expressions
(compose_parts; no GA integer id is used). Before any launch the regenerated parts must equal, field by field, the
parent-bound record of review/moqls8-gb-parent-binding-v1/GBBINDING.json (d917203d...c673: header, variables, clauses,
bytes, sha256 and every piece) and the PRE-EXEC copy of that record. After admission, immediately before each native
spawn, the CNF parts are re-hashed together with this script, the interpreter, both binaries, GBBINDING, the binder,
the PRE-EXEC, the parent GO record and (gb items) the control receipts.

Staged transport. Stage 1 runs kissat 4.0.4 alone: CNF parts -> anonymous pipe /dev/fd/N (writer thread; sha256 and
count of exactly the bytes os.write() accepted) -> kissat --time=3600 -> named FIFO fifo/<label>.kissat.fifo ->
collector thread (sha256, byte count, the actual EOF read() == b''), which keeps the proof in RAM as the list of chunks
read (one read buffer of at most 1 MiB in flight). The FIFO read end and a keepalive write end are opened before the
spawn; the keepalive is closed when kissat is reaped. Stage 2 starts only after kissat was reaped (wait4) with
self-exit 20 and the exact status line and the collector and solver writer finished cleanly; an independent sha256 of
the RAM buffer must equal the collector's. Then the parent drat-trim runs alone: the same CNF through a second
measured pipe (/dev/fd/N as argv[1]), the RAM proof through a feeder thread on its stdin (-i binary mode; sha256/count
of exactly the bytes written; each chunk slot is released once written), -t 7200. drat-trim stdout+stderr go through
an anonymous pipe to a filter thread that hashes and counts the FULL raw stream and drops ONLY lines that fullmatch the
exact duplicate-literal normalization line of the pinned drat-trim.c L1162 (<CR>c WARNING: detected and deleted
duplicate literal %i at position %i of proof line %i<LF>; counted, split into formula and proof phase by the line
number); every other byte goes to logs/<label>.drat.filtered.log and is parsed for status, parse-count, NOT VERIFIED,
TIMEOUT, early EOF, less-than-expected, ERROR and WARNING lines. No CNF or proof regular file exists; spent FIFO nodes
are never unlinked (this script deletes nothing). The kissat log is kissat's raw stdout+stderr file, hashed after the
stage. Each native tool gets its own new TMPDIR and cwd under tmp/<label>/. Descriptors live in the Fds registry until
the worker thread that owns them claims them as the first action of its run (replay_v5d.py pattern: all worker state
exists before the claim; whoever takes a descriptor first is its only closer).

Proof-byte semantics (pinned drat-trim.c d834b649...c2ee): with -i every consumed proof byte increments nReads (L987
literal bytes, L1115 the 'a'/'d' marker); EOF at a marker position ends parsing without a count (L1107-1108), EOF at a
literal start adds one (L986-988), a wrong binary prefix stops reading early (L1113). So 'c finished parsing, read N
bytes from proof file' with N == the fed byte count D is an exact consumed-to-EOF check. drat-trim prints 's TIMEOUT'
with exit 0 (L905) and returns 0 only for a verified refutation (L1500); the header error exits 0 (L1065).

Process control: native limits kissat --time=3600 and drat-trim -t 7200, plus cooperative SIGTERM-only stops with a
bounded 120 s reap; never SIGKILL, Popen.kill, subprocess timeouts or Popen.wait; only owned child pids are signalled
(no process-group or broadcast signal). The ps/lsof lane helpers (replay_v5d.py run_helper/lane_scan/Scanner; lane_scan
adds exclusion flags computed on the full argv) run in their own session under monotonic deadlines; a helper survivor
stops the desk. A driver SIGTERM or SIGINT is latched and checked at the gate, at every identity check, immediately
before each spawn, at each completion break, before evaluation and at the commit. An unsettled child, thread or
descriptor, a latched signal, a scanner failure, an exclusion breach or a helper survivor vetoes PASS and stops the
desk. A timeout, guard stop or deferral is never success; no retries.

Usage (/opt/homebrew/opt/python@3.14/bin/python3.14 -I -B, environment TMPDIR=<desk>/tmp/; absolute paths):
  gb_staged_v4.py preexec OUT ITEM...    ITEM = control:NAME | gb:ID:aN  (only controls, or exactly one gb item)
  gb_staged_v4.py run PREEXEC GO         GO = the parent-written release record required by validate_go()
  gb_staged_v4.py qualification LABEL    read-only: the full admission predicate for one receipt label (JSON)
"""
import ctypes
import datetime
import errno
import fcntl
import hashlib
import importlib.util
import itertools
import json
import os
import re
import resource
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
DESK = REVIEW + "/moqls8-gb-parent-staged-replay-v1"
DESK_REL = "review/moqls8-gb-parent-staged-replay-v1"  # relative to RUN; the parent GO record names it
SCRIPT = os.path.realpath(__file__)
SCRIPT_REL = "scripts/gb_staged_v4.py"
LABEL_PREFIX = "gbs4-"  # every receipt/log/FIFO/TMPDIR name of this version (v1-v3: gbs1-, gbs2-, gbs3-)
TMP = DESK + "/tmp"

KISSAT = "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"
KISSAT_SHA = "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848"
DRAT = REVIEW + "/moqls7-parent-proofcheck-v1/drat-trim"
DRAT_RECEIPT = REVIEW + "/moqls7-parent-proofcheck-v1/parent-result.json"
DRAT_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"  # that desk's drat_trim.binary_sha256
GBBINDING = REVIEW + "/moqls8-gb-parent-binding-v1/GBBINDING.json"
GBBINDING_SHA = "d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673"
BINDER = REVIEW + "/moqls8-gb-parent-binding-v1/scripts/bind_gb_v2.py"
BINDER_SHA = "188c88de64fa994ca7e212f8d1618da9a0eb3433e2e162a835139bbfa4985f51"
GB_SOURCE = LANE + "/code/gram_b_r2.py"
GB_SOURCE_SHA = "4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0"
PROVENANCE = {  # read-only references of the brief, re-hashed at preexec and run (a changed file refuses)
    "brief": (REVIEW + "/gb-parent-replay-brief-v1.md",
              "d95f3a0b742978e4d9e6d3163898c7b5dd4fbbdc84d963226ef4548aeaa027ed"),
    "ga_runtime_patterns_replay_v5d": (REVIEW + "/moqls8-strengthened-parent-replay-v1/scripts/replay_v5d.py",
                                       "ee52004ba7d12edd673a10bc4ed73005d6c56588697215c9b06cc1dbb846339e"),
    "long_job_stability_amendment": (REVIEW + "/parent-rule-amendment-long-job-stability-v1.md",
                                     "0bbf4fdf6fd25e22e57b5c320262518dcf2df8a5a9e0a06c6b44b9afdac4ce87"),
    "lane_rss_decision": (REVIEW + "/parent-decision-m8-lane-rss-escalation-v1.md",
                          "b9886e242764750f55a2393323dfa7da7eb7696554d493bb107cd5f3815209ec"),
    "codex_v5b_findings": (REVIEW + "/n8-replay-v5b-source-codex-v1.note.md",
                           "1e2757234ab17bcca3fe2ddf5c23481be3851c69447d531fcf27fb68f6d7c64b"),
    "codex_v5c_findings": (REVIEW + "/n8-replay-v5c-delta-codex-v1.note.md",
                           "46f39aacc61d8e4ff85c90146adec78513db1108fcac5d3243294c520aafe748"),
    "codex_v5d_findings": (REVIEW + "/n8-replay-v5d-delta-codex-v1.note.md",
                           "98fe110b6ae28b8cca3c449992fecf3b40662987c9d297c57eaee99d025fb2f4"),
    "gb_r6_handoff_timing_api_only": (LANE + "/review/GB_R6_PARENT_HANDOFF.r1.md",
                                      "0870f26c2a3713a0e520b7e92721888de9ff8d7edc5dfdaeb684c58d4d63dc1b"),
    "drat_trim_source": (REVIEW + "/moqls7-parent-proofcheck-tools-v1/drat-trim.c",
                         "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"),
    "runtime_v1": (DESK + "/scripts/gb_staged_v1.py",
                   "b36fbb57f279d1b622c1b1b111ad36a542e0ac85c7b9edce92e4c6c7733f8151"),
    "codex_gbs1_source_audit": (REVIEW + "/n8-gb-staged-v1-source-codex-v1.note.md",
                                "480ef5418c85d2d2bc43fbddf6b5d0c8d6ca38337939570037b87adcc0ec24a6"),
    "runtime_v2": (DESK + "/scripts/gb_staged_v2.py",
                   "89db96359ba1a94c3c6a45f7386a34006178fd38d4653e9fefcd921c62532844"),
    "codex_gbs2_source_audit": (REVIEW + "/n8-gb-staged-v2-source-codex-v1.note.md",
                                "f39a65cda7eaf2a291f50e922501c8bc3b5a609418d3be39140e4c738ef4fe16"),
    "runtime_v3": (DESK + "/scripts/gb_staged_v3.py",
                   "6f5b3a8adab95d41f609f31c59704592071be91124dbeba622a329ff541a0f14"),
    "codex_gbs3_delta_audit": (REVIEW + "/n8-gb-staged-v3-delta-codex-v1.note.md",
                               "eb8f8ac40ebe8ad023b6f2ddf36da1299f9661b4a8524d4f1f2977840a90be17"),
}

# --- the eighteen authorized inputs, in the brief's order (no other input or refinement)
DIRECT12 = ("P1-B4", "P0-B4", "P0-B5", "P0-B6", "P1-B6", "P2-C4", "P2-C3", "P0-B1", "P0-B2", "P0-B3", "P2-C2", "P2-C1")
STRONG6 = {"P1-B2.M2": ("P1-B2", 2), "P1-B2.M4": ("P1-B2", 4), "P1-B5.M2": ("P1-B5", 2), "P1-B5.M3": ("P1-B5", 3),
           "P1-B3.M2": ("P1-B3", 2), "P1-B1.M2": ("P1-B1", 2)}
GB_ITEMS = DIRECT12 + tuple(STRONG6)
ATTEMPT_RE = re.compile(r"a[1-9][0-9]{0,2}")  # science artifacts are newly named per attempt: gb:ID:aN
BOUND_FIELDS = ("id", "kind", "direct", "source_template", "monomial_square", "header", "variables", "clauses", "bytes",
                "sha256", "pieces", "supports_row2to7")

PDT = datetime.timezone(datetime.timedelta(hours=-7))
NO_LAUNCH_AT = datetime.datetime(2026, 10, 18, 17, 29, 0, tzinfo=PDT).timestamp()    # no native spawn at/after this
NATIVE_STOP_AT = datetime.datetime(2026, 10, 18, 17, 57, 0, tzinfo=PDT).timestamp()  # in flight: SIGTERM at this

KISSAT_SECONDS, DRAT_SECONDS, STAGE_MARGIN = 3600, 7200, 120  # native limits; stage wall backstop = limit + 120 s
GIB, MIB = 1 << 30, 1 << 20
LAUNCH_FLOOR = 12200000000 + 10 * MIB   # fresh check before each launch: 12.2e9 + projected retained growth
FLOOR = 12000000000                     # in flight: free below this -> SIGTERM -> UNKNOWN
LANE_BUSY_CAP, MINE = 4, 1              # staged: this desk runs one native at a time
LANE_RSS_LIMIT = 11 * GIB               # lane total: other lane processes + max(desk measured, desk reservation)
GB_PIPELINE_CAP = 6 * GIB               # brief: pipeline RSS cap (driver incl. CNF parts and RAM proof + live child)
GB_RESERVATION = GB_PIPELINE_CAP        # a GB pipeline reserves its cap in the lane accounting
CONTROL_RESERVATION = 512 * MIB
CONTROL_CAP = CONTROL_RESERVATION + GIB // 2
WAIT_POLL, WAIT_BUDGET, GATE_STREAK = 60, 6 * 3600, 2
SAMPLE, LANE_SCAN_PERIOD, SIGTERM_GRACE = 0.25, 1.0, 120
HOT_CPU_FRACTION, HOT_WINDOW = 0.5, 2.0
CHUNK = 1 << 20
FILTER_READ = 1 << 16
JOIN_SECONDS = 60.0                     # bounded join of a stage's worker threads after its child was reaped
HOLD_SECONDS = 60                       # early-close control only: the feeder's first write waits for the reap
LIST_CAP = 40                           # receipt lists of parsed checker lines (counts are always complete)
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
       "HOME": os.environ.get("HOME", DESK)}
NATIVE = {"cadical", "kissat", "drat-trim", "lrat-check", "lrat-trim", "cake_lpr", "dpr-trim", "glucose",
          "minisat", "lingeling", "plingeling", "treengeling", "cryptominisat5", "kissat_mab", "dpr2pr"}
LANE_MARKERS = ("/moqls8-problem16", "/review/moqls8-")
GA_DESK_MARKER = "/review/moqls8-strengthened-parent-replay-v1"
GA_DRIVER_KEYS = ("replay_v", "launch_v")
GB_DRIVER_KEYS = ("gb_direct_r", "gb_staged_v")
GB_NATIVE_MARKERS = ("/review/moqls8-gb-", "/gb_direct_v", "/gb_one_p4", "/evidence/gb_")  # (F5) GB desks/evidence
CHILD_NAMES = ("solver", "checker")  # (F2) the two ownership slots of a pipeline
HELPER_DEADLINE, HELPER_TERM_WAIT, STALE_SECONDS = 8.0, 5.0, 30.0
HELPER_SURVIVORS = []  # helpers still alive after SIGTERM + HELPER_TERM_WAIT; any entry stops the desk
MONITOR = REVIEW + "/disk-monitor-v1-20261018T0722-to-1810.jsonl"
STABLE_FREE_MIN = 13500000000 + 10 * MIB  # last monitor free >= 13.5e9 + 10 MiB growth (replay_v5d.py value)
STABLE_RUNWAY_BASE, STABLE_RUNWAY_DIV = 13500000000, 12
STABLE_WINDOW, STABLE_MIN_DROP_CAP = 300.0, 300000000
STABLE_MAX_AGE, STABLE_MIN_SAMPLES, STABLE_MIN_SPAN = 30.0, 25, 290.0
RECEIPT_SCHEMA = "moqls8-gb-staged-replay-receipt/4"
COMMIT_SCHEMA = "moqls8-gb-staged-replay-commit/4"
COMPLETION_SCHEMA = "moqls8-gb-staged-replay-completion/4"
CANCELLATION_SCHEMA = "moqls8-gb-staged-replay-cancellation/4"
PREEXEC_SCHEMA = "moqls8-gb-staged-replay-preexec/4"
RUN_SCHEMA = "moqls8-gb-staged-replay-run/4"
PUBLICATION_SIGNALS = (signal.SIGTERM, signal.SIGINT)  # (F4') blocked across the final decision and publication
GO_STATUS = "PARENT_GO"

# --- controls on this runtime identity (synthetic 3-variable formulas; exclusive separate outputs)
UNSAT3 = (b"p cnf 3 8\n1 2 3 0\n1 2 -3 0\n1 -2 3 0\n1 -2 -3 0\n-1 2 3 0\n-1 2 -3 0\n-1 -2 3 0\n"
          b"-1 -2 -3 0\n")
UNSAT3D = b"p cnf 3 9\n" + UNSAT3.split(b"\n", 1)[1] + b"1 1 2 0\n"  # + one duplicate-literal clause (as GB has)
SAT3 = b"p cnf 3 7\n1 2 3 0\n1 2 -3 0\n1 -2 3 0\n1 -2 -3 0\n-1 2 3 0\n-1 2 -3 0\n-1 -2 3 0\n"
NOHEADER = b"c header-less control input: the parent drat-trim exits before it reads any proof byte\n"
SHORT_BYTES = 1          # short-cnf control: the checker CNF feed withholds its final LF
TRUNCATE_BYTES = 2       # truncate control: the feeder never writes the last 2 collected proof bytes
SUFFIX = b"d\x02\x04\x06\x00"  # suffix control: binary DRAT deletion of clause '1 2 3' after the collected proof
DRAT_NO_HEADER_LINE = b"c ERROR: did not find p cnf line in input file"

CRITERIA = (  # the PASS conjunction (brief section 'PASS only with every conjunct'); evaluate() builds each one
    "formula_identity_bound",                    # regenerated parts == GBBINDING record == PRE-EXEC copy
    "identity_rehashed_before_solver_spawn",     # script/python/binaries/binding/PRE-EXEC/GO/CNF parts re-hashed
    "identity_rehashed_before_checker_spawn",
    "solver_feed_measured_complete",             # written == bound bytes, sha256 == bound, no error, finished
    "checker_feed_measured_complete",
    "solver_self_exit_20",                       # wait4: normal exit 20 and no driver SIGTERM to it
    "solver_status_exact_unsat",                 # status lines (CR removed only) == ['s UNSATISFIABLE']
    "collector_eof_clean",                       # actual FIFO EOF, no read/close error or exception, finished
    "proof_positive",                            # collected R > 0
    "proof_buffer_digest_agrees",                # independent sha256/length of the RAM buffer == collector's
    "feeder_plain_complete",                     # plain mode, everything written, no delivery/close error, finished
    "proof_fed_equals_collected",                # fed D == R and fed sha256 == collected sha256 == buffer sha256
    "checker_self_exit_0",                       # wait4: normal exit 0 and no driver SIGTERM to it
    "checker_status_exact_verified",             # status lines (CR removed only) == ['s VERIFIED']
    "checker_no_not_verified",
    "checker_no_timeout",                        # (F1) independent: drat-trim's timeout prints s TIMEOUT, exit 0
    "checker_no_fatal_diagnostic",               # (F1) no ERROR/MEMOUT/illegal literal/error opening/wrong prefix
    "checker_no_early_eof_or_less_than_expected",
    "checker_header_counts_match",               # exactly one parse line, counts == the bound header
    "checker_consumed_proof_bytes_equal_fed",    # exactly one 'read N bytes from proof file' line with N == D
    "checker_stream_filter_clean",               # raw stream to EOF, no read/log/close error, log on disk == kept
    "no_safety_stop",                            # no stop, exception, spawn error, skipped stage or exceeded grace
    "no_driver_signal_latched",
    "no_exclusion_breach",                       # (F5) neither the scanner latch nor the supervise latch is set
    "lane_scanner_clean",
    "all_threads_finished",
    "all_fds_settled",
    "children_reaped",
    "no_helper_survivor",
)
CHECKER_VERDICT = ("checker_self_exit_0", "checker_status_exact_verified", "checker_no_not_verified")
PROOF_EQUALITY = ("feeder_plain_complete", "proof_fed_equals_collected")
VERIFIED_0 = {"exit_code": 0, "status_lines": ["s VERIFIED"], "allowed_diagnostics": []}
NOT_VERIFIED_1 = {"exit_code": 1, "status_lines": ["s NOT VERIFIED"], "allowed_diagnostics": []}
CONTROLS = {  # name -> inputs, feed modes and the preregistered outcome. (F1) outcomes: the ONLY allowed drat-trim
    # results (normal self-exit code, exact status lines, the fatal-class diagnostic lines allowed with it); must_fail:
    # criteria that must be False; may_fail: criteria that the allowed outcomes make False; every other criterion must
    # be True (checker_no_timeout never appears in may_fail); plus the control's observation in control_observation()
    "unsat": {
        "solver": UNSAT3D, "checker": UNSAT3D, "checker_feed": "full", "proof_feed": "plain", "verdict": "PASS",
        "outcomes": [VERIFIED_0], "must_fail": (), "may_fail": (),
        "observation": "genuine tiny UNSAT: the complete acceptance predicate holds and the stream filter dropped "
                       "exactly one duplicate-literal normalization line in the formula phase (clause 9 '1 1 2 0'), so "
                       "the exact filter class matches the pinned checker's real output (proof-phase lines, e.g. from "
                       "a kissat deletion of that original clause, are counted and recorded as observed)"},
    "sat-checker": {
        "solver": UNSAT3D, "checker": SAT3, "checker_feed": "full", "proof_feed": "plain",
        "verdict": "AS_PREREGISTERED_NOT_VERIFIED", "outcomes": [NOT_VERIFIED_1], "must_fail": CHECKER_VERDICT,
        "may_fail": (),
        "observation": "satisfiable checker CNF: complete equal transport (D == R, equal digests, N == D, parse line "
                       "3 variables / 7 clauses) and drat-trim self-exit 1 with the exact singleton status "
                       "['s NOT VERIFIED'] and no fatal-class diagnostic: an equal digest does not make a proof "
                       "correct"},
    "short-cnf": {
        "solver": UNSAT3D, "checker": UNSAT3D, "checker_feed": "short", "proof_feed": "plain",
        "verdict": "AS_PREREGISTERED_FAIL_CLOSED", "outcomes": [VERIFIED_0],
        "must_fail": ("checker_feed_measured_complete",), "may_fail": (),
        "observation": "intentionally short CNF delivery: the checker writer delivers the bound bytes except the "
                       "final LF (written == bound - 1, sha256 of exactly that prefix, no error) while drat-trim "
                       "self-exits 0 with exactly ['s VERIFIED'], N == D and the bound parse counts; only the measured "
                       "feed fails, so a native VERIFIED cannot substitute for incomplete delivery"},
    "truncate": {
        "solver": UNSAT3D, "checker": UNSAT3D, "checker_feed": "full", "proof_feed": "truncate",
        "verdict": "AS_PREREGISTERED_FAIL_CLOSED",
        "outcomes": [VERIFIED_0, dict(NOT_VERIFIED_1, allowed_diagnostics=["c ERROR: no conflict"])],
        "must_fail": PROOF_EQUALITY, "may_fail": CHECKER_VERDICT + ("checker_consumed_proof_bytes_equal_fed",
                                                                    "checker_no_fatal_diagnostic"),
        "observation": "truncated proof: the feeder writes the collected proof except its last 2 bytes without any "
                       "delivery error (D == R - 2, digests differ) and drat-trim consumes it to EOF (one count line, "
                       "N == D or D + 1 for an EOF at a literal start, drat-trim.c L986-988); its outcome must be "
                       "VERIFIED/0 or NOT VERIFIED/1 (the latter may carry only 'c ERROR: no conflict', L874, when the "
                       "withheld bytes held the empty clause); the predicate fails on byte/digest equality"},
    "suffix": {
        "solver": UNSAT3D, "checker": UNSAT3D, "checker_feed": "full", "proof_feed": "suffix",
        "verdict": "AS_PREREGISTERED_FAIL_CLOSED", "outcomes": [VERIFIED_0, NOT_VERIFIED_1],
        "must_fail": PROOF_EQUALITY, "may_fail": CHECKER_VERDICT,
        "observation": "suffix proof: after the collected proof the feeder writes the 5-byte binary deletion "
                       "'d 1 2 3 0' (D == R + 5, digests differ) and the checker's consumed count N == D shows it read "
                       "the suffix; outcome VERIFIED/0 or NOT VERIFIED/1 without fatal diagnostic; the predicate fails "
                       "on byte equality"},
    "digest-alter": {
        "solver": UNSAT3D, "checker": UNSAT3D, "checker_feed": "full", "proof_feed": "alter",
        "verdict": "AS_PREREGISTERED_FAIL_CLOSED", "outcomes": [VERIFIED_0, NOT_VERIFIED_1],
        "must_fail": PROOF_EQUALITY, "may_fail": CHECKER_VERDICT,
        "observation": "altered transported digest: the feeder flips bit 0 of the first one-byte literal of the first "
                       "'a' line in transit (that literal negated): D == R and N == D, but the transported digest "
                       "differs from the collected and independently recomputed digests; outcome VERIFIED/0 or NOT "
                       "VERIFIED/1 without fatal diagnostic; the predicate fails on digest equality alone"},
    "early-close": {
        "solver": UNSAT3D, "checker": NOHEADER, "checker_feed": "full", "proof_feed": "hold",
        "verdict": "AS_PREREGISTERED_FAIL_CLOSED",
        "outcomes": [{"exit_code": 0, "status_lines": [],
                      "allowed_diagnostics": ["c ERROR: did not find p cnf line in input file"]}],
        "must_fail": PROOF_EQUALITY + ("checker_status_exact_verified", "checker_no_fatal_diagnostic",
                                       "checker_header_counts_match", "checker_consumed_proof_bytes_equal_fed"),
        "may_fail": (),
        "observation": "early checker close: drat-trim reads the complete header-less CNF, prints exactly the one "
                       "diagnostic 'c ERROR: did not find p cnf line in input file' and self-exits 0 with no status "
                       "line and no proof byte count; the feeder's first write, held until the checker was reaped, "
                       "gets EPIPE with 0 bytes fed and stops cleanly (descriptor closed once, buffer released); every "
                       "thread finishes, every descriptor is settled and no child is left"},
}
WANT_VERDICTS = {name: spec["verdict"] for name, spec in CONTROLS.items()}

SCOPE = ("Parent replay of exact GB (gram_b_r2) formulas only: the twelve direct templates and the six strengthened "
         "formulas of review/gb-parent-replay-brief-v1.md, regenerated in memory by the pinned parent binder and "
         "bound to GBBINDING d917203d...c673; kissat 4.0.4 -> named FIFO -> parent RAM collector, then the parent "
         "drat-trim fed the measured CNF and the in-memory proof. Results are exact-input proof facts; no n8 "
         "theorem, transfer or novelty claim.")
ACCEPTANCE = ("PASS iff every conjunct holds: (1) the freshly regenerated formula equals the GBBINDING record "
              "(header, variables, clauses, bytes, sha256, every piece) and the PRE-EXEC copy, and is re-hashed after "
              "admission immediately before each native spawn; (2) BOTH measured CNF feeds (kissat pipe, drat-trim "
              "pipe) finished without write or close error with written == bound bytes and sha256 == bound sha256; "
              "(3) kissat self-exit 20 (normal exit, no driver SIGTERM) and its status lines (log with only CR "
              "removed, lines starting with 's') exactly ['s UNSATISFIABLE']; (4) drat-trim self-exit 0, status "
              "lines exactly ['s VERIFIED'], no 's NOT VERIFIED' or 's TIMEOUT', no fatal-class diagnostic (ERROR, "
              "MEMOUT, illegal literal, error opening, wrong binary prefix, failed to reallocate), no 'early EOF' or "
              "'clauses less than expected' line, exactly one 'c parsing input formula' line with the bound variable "
              "and clause counts; (5) the collector saw the actual FIFO EOF without error and read R > 0 bytes, an "
              "independent sha256 of the RAM buffer equals the collector's, and the plain-mode feeder wrote D == R "
              "bytes whose "
              "sha256 equals the collected digest, without delivery or close error; (6) exactly one 'c finished "
              "parsing, read N bytes from proof file' line with N == D; (7) the drat-trim stream filter read the raw "
              "stream to EOF without read, log-write or close error and the filtered log on disk hashes to the bytes "
              "it kept (it drops only exact duplicate-literal normalization lines, counted; the full raw stream "
              "hash/count is recorded separately); (8) no safety stop, exception, spawn error, skipped stage or "
              "exceeded SIGTERM grace; no driver signal latched during the pipeline or at evaluation; no exclusion "
              "breach latched by the scanner or the in-flight guard; no lane-scanner failure and the scanner "
              "stopped; all five worker threads started and finished; no descriptor left and no close error; both "
              "children reaped; no helper survivor. Anything else is UNKNOWN with reasons; a driver signal latched "
              "during evaluation downgrades PASS to UNKNOWN. Qualification additionally needs the commit record "
              "receipts/<label>.commit.json with qualified true: the receipt is first synced (file + directory), "
              "then the decision is taken with SIGTERM/SIGINT blocked (verdict PASS, durable receipt, no latched or "
              "pending signal, the driver the only thread) and published durably and atomically (os.link of the "
              "synced .prepare record); the item qualifies only when the completion record bound to that commit "
              "is published with no signal through the whole publication, no cancellation veto exists and the "
              "run's durable summary shows no stop or signal. A SAT report, a safety stop or any settlement failure "
              "stops the desk. No retries: a new attempt needs a new parent GO and a new attempt tag; old UNKNOWN "
              "receipts are retained.")
GATE_RULE = ("Before each launch (stage 1; stage 2 is not a new admission): a fresh lane scan (native solver/checker "
             "processes plus python processes whose cwd or argv lies in the lane or a review/moqls8-* desk, "
             "excluding this driver and its children; python counts as busy if its CPU use over a 2 s libproc window "
             "is >= 50%; lane RSS includes every such python) and a fresh statvfs: launch only if lane busy + 1 <= 4, "
             "lane RSS of all other lane processes + max(fresh measured driver RSS, reservation; unreadable refuses) "
             "<= 11 GiB (gb reservation = the 6 GiB pipeline cap; controls 512 MiB), free >= 12,200,000,000 + 10 MiB, "
             "no exclusion breach (no parent GA replay native or replay/launch driver: the parent GA driver must have "
             "exited; no other kissat; no other GB pipeline driver), no helper survivor; two consecutive passing "
             "checks 60 s apart; otherwise sleep 60 s and re-check, total gate wait bounded by 6 h. No native spawn at "
             "or after 2026-10-18 17:29:00 PDT. gb items additionally need the unchanged parent disk-monitor rule "
             "(review/disk-monitor-v1-20261018T0722-to-1810.jsonl; amendment 0bbf4fdf...ce87): complete JSON lines, "
             "event records (start/restart) ignored and never reconstructed, every sample tz-aware with an int "
             "free, strictly increasing timestamps, last sample 0 <= age <= 30 s with free >= 13.5e9 + 10 MiB, >= 25 "
             "samples spanning >= 290 s within the last 300 s, max peak-to-later drop <= max(300,000,000, (free_last "
             "- 13.5e9) // 12); a malformed complete line or a naive, non-monotone or stale sample refuses; the rule "
             "and a fresh statvfs are re-read at the launch decision. Immediately before EACH native spawn (kissat, "
             "drat-trim) the launch threshold free >= 12.2e9 + 10 MiB, the latched stop/exclusion/scanner state, the "
             "17:29 cutoff and the 17:57 deadline are checked again (stage 2 also lane busy + 1 <= 4 and the 11 GiB "
             "lane total from the newest reading). The run also needs the parent GO record (validate_go) and, for gb "
             "items, the seven qualified control receipts (receipt + commit) of this script sha256.")
STOPS = ("In flight, every 0.25 s: pipeline aggregate RSS (driver incl. CNF parts and the RAM proof + the live child, "
         "libproc; a live child unreadable twice in a row is a guard failure) and free space; a scanner thread "
         "publishes lane scans every >= 1 s (helpers under %.0f s deadlines; any failed reading is latched). SIGTERM "
         "the live child if a lane reading failed, a failure is latched or the reading is older than %.0f s, an "
         "exclusion breach appears (latched by the scanner itself; foreign GB natives are recognized by cwd/argv in a "
         "GB desk or GB evidence tree, by ppid 1 or by a GB-driver parent), lane busy (other lane natives + hot "
         "python) + 1 > 4, lane RSS (other lane + max(pipeline measured, reservation)) > 11 GiB, "
         "pipeline aggregate > the item's cap (6 GiB gb, 1 GiB controls), free < 12,000,000,000, stage wall > "
         "limit + 120 s (kissat %d s, drat-trim %d s), the host clock reaches 2026-10-18 17:57:00 PDT, a spawn error, "
         "a helper survivor, any exception after the first descriptor, or the driver receives SIGTERM (also checked "
         "immediately before each spawn and at each completion break); then wait at most 120 s, never escalate; "
         "result UNKNOWN and the desk launches nothing more. Stage 2 is skipped (UNKNOWN) unless stage 1 ended with "
         "kissat self-exit 20, the exact status line, a clean collector EOF with R > 0, a complete measured solver "
         "feed, finished stage-1 threads, no latched stop and the launch cutoff not reached."
         % (HELPER_DEADLINE, STALE_SECONDS, KISSAT_SECONDS, DRAT_SECONDS))
TRANSPORT = ("CNF parts in driver memory -> anonymous pipes /dev/fd/N (writer threads, sha256/count of exactly the "
             "bytes written; stage 1 kissat, stage 2 drat-trim argv[1]); proof: kissat -> named FIFO fifo/<label>."
             "kissat.fifo (read end and keepalive opened by the driver before the spawn; keepalive closed at the reap) "
             "-> collector thread (sha256/count, actual EOF, chunks in RAM) -> after the reap and an independent "
             "buffer digest -> feeder thread (sha256/count of the bytes written; chunks released once written) -> "
             "drat-trim stdin (-i); drat-trim stdout+stderr -> anonymous pipe -> filter thread (full raw stream "
             "sha256/bytes/lines; only exact duplicate-literal normalization lines dropped and counted) -> "
             "logs/<label>.drat.filtered.log. No CNF or proof regular file; FIFO nodes retained; each native tool "
             "has its own TMPDIR and cwd tmp/<label>/kissat/ and tmp/<label>/drat/.")
SEQUENCING = ("A PRE-EXEC holds only controls (control:NAME, run in the listed order) or exactly one gb item "
              "(gb:ID:aN). One native at a time. A gb PRE-EXEC is admitted only with the seven control receipts of "
              "this script sha256 with their preregistered verdicts and qualified commit records, re-validated at "
              "preexec, at the run start and at every identity check. A control whose commit is not qualified "
              "(verdict differs from its preregistration or a late signal) stops the run; after "
              "a SAT report, a safety stop, a spawn error, an exception, a driver SIGTERM, a scanner failure, an "
              "unfinished thread, an unsettled descriptor, an unreaped child, a helper survivor or the 17:29 PDT "
              "cutoff nothing more is launched. A label whose receipt exists is never re-run (controls: validated "
              "and skipped; gb: refused - a new attempt tag and a new parent GO are required).")
GO_RULE = ("run requires GO = a parent-written JSON record under review/ outside this desk with exactly: status "
           "'PARENT_GO', desk '%s', script_sha256 = this script's sha256, pre_exec_sha256 = the PRE-EXEC's sha256, "
           "scope 'controls' (control PRE-EXEC) or 'science' (gb PRE-EXEC) and items = the PRE-EXEC item specs in "
           "order. Its sha256 is recorded and re-checked at every identity check." % DESK_REL)


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


def full_sync(fd):
    """(F4') fsync plus the macOS full flush; any failure raises (fail closed)."""
    os.fsync(fd)
    fcntl.fcntl(fd, fcntl.F_FULLFSYNC)


def fsync_dir(path):
    dfd = os.open(path, os.O_RDONLY)
    try:
        full_sync(dfd)
    finally:
        os.close(dfd)


def write_json_durable(path, obj):
    """(F4') Exclusive create, complete write, file sync, close, directory sync; the on-disk bytes must hash to the
    serialized bytes. Any failure raises (fail closed). -> sha256 of the file."""
    data = (json.dumps(obj, indent=1) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        view, off = memoryview(data), 0
        while off < len(view):
            off += os.write(fd, view[off:])
        full_sync(fd)
    finally:
        os.close(fd)
    fsync_dir(os.path.dirname(path))
    digest = sha_file(path)
    if digest != sha_bytes(data):
        raise OSError("durable write of %s: on-disk sha256 %s differs from the written bytes" % (path, digest))
    return digest


def pending_publication_signals():
    return sorted(signal.Signals(s).name for s in signal.sigpending() if s in PUBLICATION_SIGNALS)


def publish_record(path, obj):
    """(F4'') Durable atomic publication of one record: written and synced under path + '.prepare', made visible by
    os.link() to path (fails if path exists; nothing is renamed or deleted), directory synced. Any failure raises.
    -> sha256."""
    digest = write_json_durable(path + ".prepare", obj)
    os.link(path + ".prepare", path)
    fsync_dir(os.path.dirname(path))
    return digest


def write_cancellation(path, obj):
    """(F4'') The persistent cancellation veto. Its exclusive creation alone vetoes (admission rejects whenever the name
    exists, whatever its content), so its directory entry is synced first, then the reason is written and synced.
    Any failure raises. -> sha256."""
    data = (json.dumps(obj, indent=1) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        fsync_dir(os.path.dirname(path))
        view, off = memoryview(data), 0
        while off < len(view):
            off += os.write(fd, view[off:])
        full_sync(fd)
    finally:
        os.close(fd)
    fsync_dir(os.path.dirname(path))
    return sha_file(path)


def publish_qualification(paths, base, eligible, stop):
    """(F4'') Protected publication of one item's qualification, keeping the previous cancellation semantics: a
    SIGTERM/SIGINT latched or pending at ANY point through the successful publication vetoes the item. Both signals
    stay blocked from the decision to the end: decision (eligible, no latched or pending signal, single-threaded driver,
    so no other thread can run the handler) -> commit record published -> post-commit check -> (qualified only) the
    completion record bound to the exact receipt and commit sha256 published -> post-completion check; any signal or
    failure after the decision of a qualified item creates the cancellation veto; the mask is then restored and a
    signal delivered at that moment cancels the item too. paths: commit, complete, cancel. -> publication record whose
    status is COMPLETE, CANCELLED, UNQUALIFIED or FAILED (only COMPLETE can ever be admitted)."""
    out = {"commit_sha256": None, "completion_sha256": None, "cancellation_sha256": None, "checks": [],
           "errors": [], "cancel_reason": None}
    commit = completion = None
    qualified = False
    old = signal.pthread_sigmask(signal.SIG_BLOCK, PUBLICATION_SIGNALS)
    try:
        try:
            pending, latched = pending_publication_signals(), stop.get("signal")
            threads_alive = threading.active_count()
            qualified = bool(eligible and latched is None and not pending and threads_alive == 1)
            commit = dict(base, qualified=qualified, stop_signal_at_decision=latched,
                          pending_signals_at_decision=pending, driver_threads_at_decision=threads_alive,
                          decided_at=now(), meaning="decision record only; admission also needs the bound completion "
                                                    "record, no cancellation and a clean durable run summary")
            out["commit_sha256"] = publish_record(paths["commit"], commit)
            check = {"after": "commit publication", "pending": pending_publication_signals(),
                     "latched": stop.get("signal")}
            out["checks"].append(check)
            if qualified and (check["pending"] or check["latched"]):
                out["cancel_reason"] = "signal through the commit publication: %s" % check
            elif qualified:
                completion = {"schema": COMPLETION_SCHEMA, "label": base["label"], "receipt": base["receipt"],
                              "receipt_sha256": base["receipt_sha256"], "commit": rel(paths["commit"]),
                              "commit_sha256": out["commit_sha256"], "publication_completed": True,
                              "checks_through_commit": out["checks"][:], "completed_at": now()}
                out["completion_sha256"] = publish_record(paths["complete"], completion)
                check = {"after": "completion publication", "pending": pending_publication_signals(),
                         "latched": stop.get("signal")}
                out["checks"].append(check)
                if check["pending"] or check["latched"]:
                    out["cancel_reason"] = "signal through the completion publication: %s" % check
        except Exception as e:  # a failure after a qualified decision cancels the item; before it, nothing qualifies
            out["errors"].append("%s: %s" % (type(e).__name__, e))
            if qualified and out["cancel_reason"] is None:
                out["cancel_reason"] = "publication failure after the decision: %s: %s" % (type(e).__name__, e)
        if out["cancel_reason"] is not None:
            try:
                out["cancellation_sha256"] = write_cancellation(paths["cancel"], {
                    "schema": CANCELLATION_SCHEMA, "label": base["label"], "reason": out["cancel_reason"],
                    "commit_sha256": out["commit_sha256"], "completion_sha256": out["completion_sha256"],
                    "at": now()})
            except Exception as e:  # recorded; the run stops on any error and the run summary records it
                out["errors"].append("cancellation: %s: %s" % (type(e).__name__, e))
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)  # a pending SIGTERM/SIGINT is delivered (latched) now
    late = _latched_after_unmask(stop)
    if qualified and out["cancel_reason"] is None and late is not None:
        out["cancel_reason"] = "signal %s delivered when the publication mask was restored" % late
        try:
            out["cancellation_sha256"] = write_cancellation(paths["cancel"], {
                "schema": CANCELLATION_SCHEMA, "label": base["label"], "reason": out["cancel_reason"],
                "commit_sha256": out["commit_sha256"], "completion_sha256": out["completion_sha256"], "at": now()})
        except Exception as e:
            out["errors"].append("cancellation: %s: %s" % (type(e).__name__, e))
    if out["cancel_reason"] is not None:
        out["status"] = "CANCELLED"
    elif out["errors"]:
        out["status"] = "FAILED"
    elif qualified and out["completion_sha256"] is not None:
        out["status"] = "COMPLETE"
    else:
        out["status"] = "UNQUALIFIED"
    out["qualified_decision"] = qualified
    return out


def _latched_after_unmask(stop):
    """A Python-level call boundary after the mask is restored, so a signal delivered by the restore has run its
    (latching) handler before the caller reads the latch."""
    return stop.get("signal")


def publish_run_summary(path, summary, stop):
    """(F4'') The run summary is the run's terminal evidence and is published the same way: signals blocked, the
    latched/pending state recorded in it, durable atomic publication, a post-publication check; a signal during it,
    or one delivered when the mask is restored, creates the run cancellation veto <path minus .json>.cancelled.json.
    -> (sha256 or None, errors, cancelled)."""
    cancel = path[:-len(".json")] + ".cancelled.json"
    errors, reason, digest = [], None, None
    old = signal.pthread_sigmask(signal.SIG_BLOCK, PUBLICATION_SIGNALS)
    try:
        try:
            summary["stop_latched_at_summary"] = stop.get("signal")
            summary["pending_signals_at_summary"] = pending_publication_signals()
            summary["published_at"] = now()
            digest = publish_record(path, summary)
            pending, latched = pending_publication_signals(), stop.get("signal")
            if pending or (latched and not summary["stop_latched_at_summary"]):
                reason = "signal through the run summary publication: pending %s latched %s" % (pending, latched)
        except Exception as e:
            errors.append("%s: %s" % (type(e).__name__, e))
            reason = "run summary publication failure: %s: %s" % (type(e).__name__, e)
        if reason is not None:
            try:
                write_cancellation(cancel, {"schema": CANCELLATION_SCHEMA, "run_summary": rel(path),
                                            "reason": reason, "at": now()})
            except Exception as e:
                errors.append("run cancellation: %s: %s" % (type(e).__name__, e))
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)
    late = _latched_after_unmask(stop)
    if reason is None and late is not None and not summary.get("stop_latched_at_summary"):
        reason = "signal %s delivered when the run-summary mask was restored" % late
        try:
            write_cancellation(cancel, {"schema": CANCELLATION_SCHEMA, "run_summary": rel(path), "reason": reason,
                                        "at": now()})
        except Exception as e:
            errors.append("run cancellation: %s: %s" % (type(e).__name__, e))
    return digest, errors, reason is not None


def _load_json(path):
    try:
        return json.loads(read_bytes(path))
    except (OSError, ValueError):
        return None


def qualification_problems(label, want_verdict):
    """(F4'') The reader side of the publication protocol -> (identity, problems). A receipt qualifies only with: its
    receipt (durable), its commit with a qualified decision (verdict == want_verdict, durable receipt, no signal
    latched or pending at the decision, single-threaded driver), the completion record bound to that exact commit and
    receipt sha256, NO item cancellation record, and the durable summary of the producing run (named by the receipt's
    run_tag) with stopped_reason None, no signal at the summary, no run cancellation, and an entry for this label with
    publication COMPLETE and the same receipt/commit/completion sha256. The early commit flag alone never qualifies."""
    rec_dir = os.path.join(DESK, "receipts")
    rpath = os.path.join(rec_dir, label + ".json")
    cpath, kpath, xpath = rpath[:-5] + ".commit.json", rpath[:-5] + ".complete.json", rpath[:-5] + ".cancelled.json"
    problems = []
    try:
        rraw = read_bytes(rpath)
        r = json.loads(rraw)
    except (OSError, ValueError):
        return None, ["%s: receipt missing or not JSON" % label]
    rsha = sha_bytes(rraw)
    c, k = _load_json(cpath), _load_json(kpath)
    csha = sha_file(cpath) if c is not None else None
    ksha = sha_file(kpath) if k is not None else None
    if os.path.lexists(xpath):
        problems.append("item cancellation record exists")
    if not (isinstance(c, dict) and c.get("schema") == COMMIT_SCHEMA and c.get("label") == label
            and c.get("receipt_sha256") == rsha and c.get("qualified") is True and c.get("verdict") == want_verdict
            and c.get("receipt_durable") is True and c.get("stop_signal_at_decision") is None
            and c.get("pending_signals_at_decision") == [] and c.get("driver_threads_at_decision") == 1):
        problems.append("commit missing, not bound to the receipt, or not a qualified decision")
    if not (isinstance(k, dict) and k.get("schema") == COMPLETION_SCHEMA and k.get("label") == label
            and k.get("receipt_sha256") == rsha and k.get("commit_sha256") == csha and csha is not None
            and k.get("publication_completed") is True):
        problems.append("completion record missing or not bound to this exact commit and receipt")
    run_tag = r.get("run_tag") if isinstance(r, dict) else None
    spath = os.path.join(DESK, "runs", "run-%s.json" % run_tag) if isinstance(run_tag, str) else None
    s = _load_json(spath) if spath else None
    if spath is None or s is None:
        problems.append("durable run summary of the producing run missing")
    else:
        entries = [e for e in (s.get("items") or []) if isinstance(e, dict) and e.get("label") == label]
        if os.path.lexists(spath[:-len(".json")] + ".cancelled.json"):
            problems.append("run cancellation record exists")
        if not (s.get("schema") == RUN_SCHEMA and s.get("stopped_reason") is None
                and s.get("stop_latched_at_summary") is None and s.get("pending_signals_at_summary") == []):
            problems.append("producing run stopped or signalled (stopped_reason %r)" % s.get("stopped_reason"))
        if not (len(entries) == 1 and entries[0].get("publication_status") == "COMPLETE"
                and entries[0].get("qualified") is True and entries[0].get("receipt_sha256") == rsha
                and entries[0].get("commit_sha256") == csha and entries[0].get("completion_sha256") == ksha):
            problems.append("run summary entry for the label is not a COMPLETE publication of these records")
    ident = {"label": label, "receipt_sha256": rsha, "commit_sha256": csha, "completion_sha256": ksha,
             "run_summary": rel(spath) if spath else None, "run_summary_sha256": sha_file(spath) if s else None}
    return ident, problems


def rel(path):
    return os.path.relpath(path, DESK)


def header_counts(b):
    """[vars, clauses] of a leading 'p cnf' line, or None (the header-less early-close control input)."""
    m = re.match(rb"^p cnf (\d+) (\d+)$", bytes(b[:64]).split(b"\n", 1)[0])
    return [int(m.group(1)), int(m.group(2))] if m else None


# --- libproc (replay_v5d.py, unchanged): macOS sys/proc_info.h PROC_PIDTASKINFO = 4; struct proc_taskinfo is 96
# bytes: pti_virtual_size, pti_resident_size, pti_total_user, pti_total_system as the first four uint64.
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


def pid_gone(pid):
    """libproc existence probe: True only if proc_pidinfo fails with ESRCH."""
    buf = ctypes.create_string_buffer(96)
    ctypes.set_errno(0)
    n = _LIBPROC.proc_pidinfo(pid, 4, 0, buf, 96)
    return n <= 0 and ctypes.get_errno() == errno.ESRCH


# --- lane scan helpers (replay_v5d.py _stop_helper and run_helper, unchanged)
def _stop_helper(p, argv, why):
    """SIGTERM a live helper and wait at most HELPER_TERM_WAIT for its reap; never escalate. -> note for the error.
    A helper not confirmed reaped (still alive, or the stop itself failed) is appended to HELPER_SURVIVORS."""
    notes, reaped = [], False
    try:
        if p.poll() is None:
            try:
                os.kill(p.pid, signal.SIGTERM)
                notes.append("SIGTERM sent")
            except ProcessLookupError:
                pass
            t_end = time.monotonic() + HELPER_TERM_WAIT
            while p.poll() is None and time.monotonic() < t_end:
                time.sleep(0.05)
        reaped = p.poll() is not None
    finally:
        if not reaped:
            HELPER_SURVIVORS.append({"pid": p.pid, "argv0": argv[0], "at": now(), "reason": why})
            notes.append("not reaped %.0f s after SIGTERM (no escalation); recorded as helper survivor pid %d, the "
                         "desk stops" % (HELPER_TERM_WAIT, p.pid))
    return "".join("; " + n for n in notes)


def run_helper(argv):
    """Run one short ps/lsof helper in its own session (never in the driver's process group) under a monotonic
    deadline -> (rc or None, stdout, error). (B, F2) All bookkeeping exists before the spawn, and one enclosing
    ownership scope runs from the spawn through the cleanup: once a helper exists, every exit (normal, overrun or
    exception) passes the finally block, which SIGTERMs a live helper with a bounded reap of HELPER_TERM_WAIT
    (_stop_helper, never escalated), records an unreaped one in HELPER_SURVIVORS and closes the selector and the
    stdout pipe independently of each other. While any survivor is recorded no helper is spawned (the error stops
    gate and run). A non-Exception BaseException (e.g. KeyboardInterrupt) is re-raised after the cleanup."""
    chunks, err, sel, fatal, p = [], None, None, None, None  # (F2) before the spawn: nothing is allocated after it
    if HELPER_SURVIVORS:
        return None, b"", "no helper launch: helper survivor(s) recorded (pid %s)" % ", ".join(
            str(s["pid"]) for s in HELPER_SURVIVORS)
    try:  # (F2) the one enclosing ownership scope: spawn, supervision and cleanup
        try:
            p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                 env=ENV, start_new_session=True)
        except OSError as e:  # no helper exists
            err = "spawn %s: %r" % (argv[0], e)
        else:
            deadline = time.monotonic() + HELPER_DEADLINE
            fd = p.stdout.fileno()
            os.set_blocking(fd, False)
            sel = selectors.DefaultSelector()
            sel.register(fd, selectors.EVENT_READ)
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
    except BaseException as e:  # recorded; the finally below runs the SIGTERM/reap/close cleanup first
        err = "%s supervision raised %s: %s" % (argv[0], type(e).__name__, e)
        if not isinstance(e, Exception):
            fatal = e
    finally:
        if p is not None:  # a helper exists: bounded SIGTERM-only cleanup on every exit path
            try:
                if err is not None or p.poll() is None:
                    why = err or "%s left the supervision scope while alive" % argv[0]
                    err = why + _stop_helper(p, argv, why)
            except Exception as e:  # _stop_helper has already recorded the survivor; never hidden
                err = (err or "") + "; helper stop raised %r" % e
            finally:
                for what, closer in (("selector", sel.close if sel is not None else None),
                                     ("stdout", p.stdout.close)):
                    if closer is None:
                        continue
                    try:
                        closer()
                    except Exception as e:  # independent closes; a close failure fails the reading
                        err = (err + "; " if err else "") + "%s close failed: %r" % (what, e)
    if fatal is not None:
        raise fatal
    return (None if p is None else p.returncode), b"".join(chunks), err


def exclusion_flags(c, full_args):
    """Brief: admit only after the parent GA driver has exited, no GA/GB concurrency, one GB native at a time. ->
    reasons for one lane process, computed on its full argv and cwd: a parent GA replay native (cwd or argv in the GA
    desk) or GA replay/launch driver; any other kissat; (F5) any native whose cwd or argv lies in a GB desk or GB
    evidence tree (an orphaned foreign GB drat-trim included) and any orphaned lane native (ppid 1); any other GB
    pipeline driver (gb_direct_r*, gb_staged_v*). lane_scan adds the ownership rule (a native whose parent is a GB
    driver). This driver and its own children never appear (lane_scan excludes them by pid/ppid)."""
    where = c["cwd"] + "\n" + full_args
    out = []
    if GA_DESK_MARKER in where and (c["native"] or any(k in full_args for k in GA_DRIVER_KEYS)):
        out.append("parent GA replay process: no GA/GB concurrency")
    if c["comm"] == "kissat":
        out.append("another kissat process: one GB native at a time")
    if c["native"] and any(k in where for k in GB_NATIVE_MARKERS):
        out.append("foreign GB native (cwd/argv in a GB desk or GB evidence tree): one GB native at a time")
    if c["native"] and c["ppid"] == 1:
        out.append("orphaned lane native (parent gone): unowned native work")
    if any(k in full_args for k in GB_DRIVER_KEYS):
        out.append("another GB pipeline driver")
    return out


def exclusions(scan):
    return [{"pid": c["pid"], "comm": c["comm"], "reasons": c["exclusion"]} for c in scan if c.get("exclusion")]


def lane_scan():
    """Other lane processes -> (list, None), or (None, error). Excludes this process and its children. (C) Every
    helper exit code is validated (ps rc 0 twice; lsof rc 0 or 1: lsof exits 1 when a listed pid has gone), and
    every candidate needs a cwd line (lsof) and an argv line (ps) unless libproc confirms it gone (ESRCH); an
    unresolved live candidate fails the scan instead of silently leaving the lane count. (gbs1) A malformed ps row
    fails the scan, and every lane process carries its exclusion flags (exclusion_flags)."""
    me = os.getpid()
    rc, out, err = run_helper(["/bin/ps", "-axww", "-o", "pid=,ppid=,rss=,state=,comm="])
    if err is not None or rc != 0:
        return None, err or "ps rc %s" % rc
    cand = {}
    for line in out.decode("utf-8", "replace").splitlines():
        if not line.strip():
            continue
        parts = line.split(None, 4)
        try:  # stricter than replay_v5d.py: a malformed row fails the scan instead of being skipped
            pid, ppid, rss_kb = int(parts[0]), int(parts[1]), int(parts[2])
        except (ValueError, IndexError):
            return None, "malformed ps row %r" % line[:120]
        if len(parts) < 5:
            return None, "malformed ps row %r" % line[:120]
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
    rc, out, err = run_helper(["/usr/sbin/lsof", "-a", "-d", "cwd", "-p", pids, "-Fpn"])
    if err is not None or rc not in (0, 1):
        return None, err or "lsof rc %s" % rc
    cwd, cur = {}, None
    for line in out.decode("utf-8", "replace").splitlines():
        if line.startswith("p"):
            try:
                cur = int(line[1:])
            except ValueError:
                cur = None
        elif line.startswith("n") and cur is not None:
            cwd[cur] = line[1:]
    rc, out, err = run_helper(["/bin/ps", "-ww", "-o", "pid=,args=", "-p", pids])
    if err is not None or rc != 0:
        return None, err or "ps -p rc %s" % rc
    args = {}
    for line in out.decode("utf-8", "replace").splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            try:
                args[int(parts[0])] = parts[1]
            except ValueError:
                pass
    unresolved = []
    for pid in list(cand):
        if pid in cwd and pid in args:
            continue
        if pid_gone(pid):  # exited between the helpers: confirmed gone, holds no lane slot or memory
            del cand[pid]
        else:
            unresolved.append(pid)
    if unresolved:
        return None, ("unresolved live candidate(s) without a cwd or argv line and not gone per libproc: %s"
                      % ", ".join(str(x) for x in sorted(unresolved)))
    lane = []
    for pid, c in cand.items():
        c["cwd"] = cwd.get(pid, "")
        full_args = args.get(pid, "")
        if any(mk in c["cwd"] or mk in full_args for mk in LANE_MARKERS):
            t = taskinfo(pid)
            c["rss_bytes"] = t[0] if t else c["ps_rss_kb"] * 1024
            c["cpu_ns"] = t[1] if t else None
            c["exclusion"] = exclusion_flags(c, full_args)  # computed on the full argv and cwd, before truncation
            c["args"] = full_args[:240]
            lane.append(c)
    gb_drivers = {c["pid"] for c in lane if "another GB pipeline driver" in c["exclusion"]}
    for c in lane:  # (F5) ownership: a native whose parent is a GB driver is GB native work whatever its cwd
        if c["native"] and c["ppid"] in gb_drivers:
            c["exclusion"].append("native owned by another GB pipeline driver: one GB native at a time")
    return lane, None


class Scanner(threading.Thread):
    """In-flight lane scanner (replay_v5d.py Scanner + the (F5) exclusion latch): publishes (monotonic time, scan or
    None, error) after every scan, so the watchdog loop never blocks on a helper. Every failed reading, and an exception
    escaping the loop, is latched in 'failed' independently of 'latest'; (F5) the first successful reading that carries
    an exclusion breach is latched in 'excluded' by this thread itself, so a breach seen just before a completion break
    cannot be bypassed. latched_stop() reports both latches; evaluate() vetoes PASS on either."""

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.halt = threading.Event()
        self.lock = threading.Lock()
        self.latest = None
        self.failed = None
        self.excluded = None
        self.scans = self.failures = 0

    def _latch(self, err):
        if self.failed is None:  # caller holds the lock
            self.failed = {"at": now(), "error": err}

    def run(self):
        try:
            while not self.halt.is_set():
                try:
                    scan, err = lane_scan()
                    ex = exclusions(scan) if scan is not None else []
                except Exception as e:  # recorded, never hidden
                    scan, err, ex = None, "lane scan raised %r" % e, []
                with self.lock:
                    self.latest = (time.monotonic(), scan, err)
                    self.scans += 1
                    if scan is None:
                        self.failures += 1
                        self._latch(err)
                    elif ex and self.excluded is None:
                        self.excluded = {"at": now(), "exclusions": ex}
                self.halt.wait(LANE_SCAN_PERIOD)
        except BaseException as e:  # latched; the published reading also goes stale
            with self.lock:
                self.failures += 1
                self._latch("scanner thread raised %s: %s" % (type(e).__name__, e))

    def reading(self):
        with self.lock:
            return self.latest

    def failure(self):
        with self.lock:
            return self.failed

    def exclusion(self):
        with self.lock:
            return self.excluded


def compact(c):
    out = {k: c[k] for k in ("pid", "ppid", "comm", "native", "rss_bytes", "state", "cwd", "exclusion") if k in c}
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


def monitor_stability(raw=None, nowt=None):
    """(G) Parent long-job disk-stability rule, as amended by the parent at 07:32 PDT, from the parent's 10 s monitor
    file -> (ok, info). Fail closed: an absent, unreadable or stale monitor, a complete line that is neither an event
    record nor a {"t": tz-aware ISO time, "free": int} sample, or timestamps that are not strictly increasing give
    ok False. Only a trailing unterminated fragment (a line being written) is ignored. Read-only (raw and nowt are
    injectable for the unit checks only)."""
    info = {"monitor": rel(MONITOR), "read_at": now()}
    if raw is None:
        try:
            raw = read_bytes(MONITOR)
        except OSError as e:
            info.update(ok=False, error="monitor unreadable: %r" % e)
            return False, info
    if nowt is None:
        nowt = time.time()
    lines = raw.split(b"\n")
    lines.pop()  # b"" after a final newline, else the line still being written
    samples, events, bad = [], 0, []
    for no, line in enumerate(lines, 1):
        try:
            r = json.loads(line)
        except ValueError:
            bad.append(no)
            continue
        if isinstance(r, dict) and "event" in r and "t" not in r and "free" not in r:
            events += 1
            continue
        t, f = (r.get("t"), r.get("free")) if isinstance(r, dict) else (None, None)
        try:
            when = datetime.datetime.fromisoformat(t) if isinstance(t, str) else None
        except ValueError:
            when = None
        if when is None or when.utcoffset() is None or type(f) is not int or f < 0:
            bad.append(no)
            continue
        samples.append((when.timestamp(), f))
    increasing = bool(samples) and all(b[0] > a[0] for a, b in zip(samples, samples[1:]))
    win = [(t, f) for t, f in samples if t >= nowt - STABLE_WINDOW]
    last_t, last_f = samples[-1] if samples else (None, None)
    age = None if last_t is None else nowt - last_t
    max_drop, peak = 0, None
    for _t, f in win:
        peak = f if peak is None else max(peak, f)
        max_drop = max(max_drop, peak - f)
    span = win[-1][0] - win[0][0] if win else 0.0
    allowance = (None if last_f is None
                 else max(STABLE_MIN_DROP_CAP, (last_f - STABLE_RUNWAY_BASE) // STABLE_RUNWAY_DIV))
    checks = {"no_malformed_complete_line": not bad, "timestamps_tz_aware_strictly_increasing": increasing,
              "last_sample_age_0_to_30_s": age is not None and 0 <= age <= STABLE_MAX_AGE,
              "last_free_ge_13.5e9_plus_10MiB": last_f is not None and last_f >= STABLE_FREE_MIN,
              "window_samples_ge_25": len(win) >= STABLE_MIN_SAMPLES,
              "window_span_ge_290_s": span >= STABLE_MIN_SPAN,
              "max_drop_le_allowance": bool(win) and allowance is not None and max_drop <= allowance}
    ok = all(checks.values())
    info.update(ok=ok, checks=checks, monitor_bytes=len(raw), monitor_sha256_at_read=sha_bytes(raw),
                samples_total=len(samples), event_records=events, malformed_lines=bad[:20],
                window_samples=len(win), window_span_seconds=round(span, 1), last_free=last_f,
                last_age_seconds=None if age is None else round(age, 1), max_peak_to_later_drop_bytes=max_drop,
                drop_allowance_bytes=allowance,
                rule="amended 07:32 PDT: allowance max(300,000,000, (free_last - 13.5e9) // 12)")
    return ok, info


def gate(label, reservation, budget, log, stop, stable):
    """replay_v5d.py gate() with this desk's rules: lane busy + 1 <= 4, other lane RSS + max(fresh measured driver
    RSS, reservation) <= 11 GiB (unreadable driver RSS refuses), free >= LAUNCH_FLOOR, no exclusion breach, no helper
    survivor, and (stable=True, gb items) the parent monitor rule, re-read with a fresh statvfs at the decision. Two
    consecutive passing checks WAIT_POLL apart; a latched SIGTERM, a survivor or the 17:29 cutoff ends the gate."""
    t_start = time.monotonic()
    samples, streak = [], 0
    while True:
        fb = free_bytes()
        busy, other, scan, scan_err = gate_scan()
        excl = exclusions(scan) if scan is not None else None
        ok_disk = fb >= LAUNCH_FLOOR
        ok_busy = scan is not None and busy + MINE <= LANE_BUSY_CAP
        own = taskinfo(os.getpid())  # fresh measured driver RSS (no pipeline child exists at a gate)
        desk = own[0] if own else None  # unreadable -> None -> refuse
        ok_rss = scan is not None and desk is not None and other + max(desk, reservation) <= LANE_RSS_LIMIT
        ok_excl = scan is not None and not excl
        ok_stable, sinfo = monitor_stability() if stable else (True, None)
        ok = ok_disk and ok_busy and ok_rss and ok_excl and ok_stable and not HELPER_SURVIVORS
        streak = streak + 1 if ok else 0
        samples.append({"at": now(), "free_bytes": fb, "lane_other_busy": busy, "lane_other_rss_bytes": other,
                        "scan_failed": scan is None, "scan_error": scan_err, "ok_disk": ok_disk, "ok_busy": ok_busy,
                        "ok_rss": ok_rss, "desk_rss_bytes": desk, "ok_exclusion": ok_excl, "exclusions": excl,
                        "ok_stable": ok_stable, "stability": sinfo, "helper_survivors": len(HELPER_SURVIVORS),
                        "streak": streak})
        log("gate %s: free=%d other_busy=%s other_rss=%s desk_rss=%s reservation=%d disk/busy/rss/excl/stable="
            "%s/%s/%s/%s/%s streak=%d%s%s"
            % (label, fb, busy, other, desk, reservation, ok_disk, ok_busy, ok_rss, ok_excl,
               ok_stable if stable else "n/a", streak, "" if scan_err is None else " scan_error=" + scan_err,
               "" if not excl else " exclusions=" + json.dumps(excl)[:300]))
        waited = time.monotonic() - t_start
        res = {"label": label, "reservation_bytes": reservation, "rule": GATE_RULE, "samples": samples,
               "stability_rule_applied": stable, "waited_seconds": round(waited, 1)}
        if stop.get("signal"):  # latched SIGTERM wins over a passing streak
            budget["used"] += waited
            res.update({"launch": False, "stopped": "driver received " + stop["signal"], "stopped_at": now()})
            return res
        if HELPER_SURVIVORS:
            budget["used"] += waited
            res.update({"launch": False, "stopped": "helper survivor(s) recorded; no further launch",
                        "helper_survivors": list(HELPER_SURVIVORS), "stopped_at": now()})
            return res
        if time.time() >= NO_LAUNCH_AT:
            budget["used"] += waited
            res.update({"launch": False, "cutoff": True, "stopped": "launch cutoff 2026-10-18 17:29:00 PDT reached",
                        "stopped_at": now()})
            return res
        if streak >= GATE_STREAK:
            final = None
            if stable:  # fresh statvfs and monitor rule at the launch decision itself
                fb_final = free_bytes()
                ok_final, s_final = monitor_stability()
                final = {"at": now(), "free_bytes": fb_final, "ok_disk": fb_final >= LAUNCH_FLOOR,
                         "ok_stable": ok_final, "stability": s_final}
            if final is None or (final["ok_disk"] and final["ok_stable"]):
                budget["used"] += waited
                res.update({"launch": True, "decided_at": now(),
                            "free_bytes_at_launch": fb if final is None else final["free_bytes"],
                            "final_recheck": final, "lane_other_busy_at_launch": busy,
                            "lane_other_rss_at_launch": other, "desk_rss_at_launch": desk,
                            "launch_scan": [compact(c) for c in scan]})
                return res
            streak = 0
            samples[-1]["final_recheck_failed"] = final
            log("gate %s: final re-check failed (free=%d stable=%s); streak reset"
                % (label, final["free_bytes"], final["ok_stable"]))
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


def latched_stop(stop, scanner):
    """A latched driver signal (SIGTERM or SIGINT), a latched lane-scanner failure, (F5) a scanner-latched exclusion
    breach or a recorded helper survivor -> reason or None."""
    if stop.get("signal"):
        return "driver received %s (latched)" % stop["signal"]
    failed = scanner.failure()
    if failed is not None:
        return "lane scanner failure latched at %s: %s" % (failed["at"], failed["error"])
    excl = scanner.exclusion()
    if excl is not None:
        return "exclusion breach latched by the scanner at %s: %s" % (excl["at"], json.dumps(excl["exclusions"])[:300])
    if HELPER_SURVIVORS:
        return "helper survivor(s) recorded (pid %s)" % ", ".join(str(s["pid"]) for s in HELPER_SURVIVORS)
    return None


# --- inputs: pins, the parent binding record, the binder's loader/sink, in-memory regeneration of one input
def verify_pins():
    """Every pinned file re-hashed; a mismatch aborts before any work. -> record."""
    out = {}
    for name, (path, exp) in sorted(PROVENANCE.items()):
        got = sha_file(path)
        if got != exp:
            die("pin mismatch %s %s: %s != %s" % (name, path, got, exp))
        out[name] = {"path": path, "sha256": got}
    for name, path, exp in (("gbbinding", GBBINDING, GBBINDING_SHA), ("binder_bind_gb_v2", BINDER, BINDER_SHA),
                            ("gb_source_gram_b_r2", GB_SOURCE, GB_SOURCE_SHA)):
        got = sha_file(path)
        if got != exp:
            die("pin mismatch %s %s: %s != %s" % (name, path, got, exp))
        out[name] = {"path": path, "sha256": got}
    return out


def check_binaries():
    receipt = json.loads(read_bytes(DRAT_RECEIPT))
    exp = receipt["drat_trim"]["binary_sha256"]
    if exp != DRAT_SHA:
        die("drat-trim receipt value " + exp)
    got_d, got_k = sha_file(DRAT), sha_file(KISSAT)
    if got_d != DRAT_SHA:
        die("drat-trim sha256 " + got_d)
    if got_k != KISSAT_SHA:
        die("kissat sha256 " + got_k)
    return {"kissat": {"path": KISSAT, "sha256": got_k, "expected": KISSAT_SHA, "version": "4.0.4"},
            "drat-trim": {"path": DRAT, "sha256": got_d, "expected_from": DRAT_RECEIPT + " drat_trim.binary_sha256",
                          "receipt_sha256": sha_file(DRAT_RECEIPT), "upstream": receipt["drat_trim"].get("upstream")},
            "checked_at": now()}


def load_binding():
    """GBBINDING.json (pinned sha256) -> {sha256, records, gb_base}; refuses unless status PASS without failures,
    written by the pinned binder, and each of the eighteen ids has the expected kind/source/square and every bound
    field."""
    raw = read_bytes(GBBINDING)
    got = sha_bytes(raw)
    if got != GBBINDING_SHA:
        die("GBBINDING sha256 %s != %s" % (got, GBBINDING_SHA))
    b = json.loads(raw)
    if (b.get("status") != "PASS" or b.get("failures") != [] or (b.get("script") or {}).get("sha256") != BINDER_SHA
            or b.get("cnf_or_proof_bytes_written_to_disk") is not False):
        die("GBBINDING status/failures/script/disk fields")
    recs = {}
    for f in b.get("formulas") or []:
        if f.get("id") in recs:
            die("GBBINDING duplicate formula id %r" % f.get("id"))
        recs[f.get("id")] = f
    for gid in GB_ITEMS:
        f = recs.get(gid)
        if f is None or any(k not in f for k in BOUND_FIELDS):
            die("GBBINDING record %s missing or incomplete" % gid)
        want = ("template", True, gid, None) if gid in DIRECT12 else ("strengthened", False) + STRONG6[gid]
        if (f["kind"], f["direct"], f["source_template"], f["monomial_square"]) != want:
            die("GBBINDING record %s kind/direct/source/square %r" % (gid, (f["kind"], f["direct"],
                                                                              f["source_template"],
                                                                              f["monomial_square"])))
    base = b.get("gb_base") or {}
    for k in ("vars", "clauses", "body_bytes", "body_sha256", "body_segments"):
        if k not in base:
            die("GBBINDING gb_base field " + k)
    return {"sha256": got, "records": recs, "gb_base": base}


def load_binder():
    """The pinned parent binder executed from its verified bytes into a fresh module object (its module code only
    defines constants and functions; __name__ is not '__main__', so main() does not run)."""
    raw = read_bytes(BINDER)
    if sha_bytes(raw) != BINDER_SHA:
        die("binder sha256 differs from the pin")
    spec = importlib.util.spec_from_loader("bind_gb_v2_pinned_for_gbs1", loader=None, origin=BINDER)
    mod = importlib.util.module_from_spec(spec)
    mod.__file__ = BINDER
    exec(compile(raw, BINDER, "exec", dont_inherit=True), mod.__dict__)
    return mod


def compose_parts(B, gid, tab, V, C, segs, sup):
    """One of the eighteen inputs with the binder's compose() expressions (bind_gb_v2.py L634-650 and L655-681):
    template T = 'p cnf V C+42' + the base segments + 42 unit lines; strengthened T.Ms = 'p cnf V C+168' + the base
    segments + the 42 unit lines of T + the 126-line M_s tail; every literal from GB's own F.tab (tab).
    -> (parts, pieces, source template, square or None). The segments are referenced, never copied."""
    if gid in STRONG6:
        t, s = STRONG6[gid]
    elif gid in DIRECT12:
        t, s = gid, None
    else:
        die("not one of the eighteen GB inputs: %r" % (gid,))
    lits = []
    for i, S in zip(B.ROWS, sup[t]):
        for c in B.COORDS:
            v = tab[("g", 1, (0, c), (i, 0))]
            lits.append(v if c in S else -v)
    units = B.unit_section(lits)
    parts = [b"p cnf %d %d\n" % (V, C + B.UNITS + (B.TAIL if s is not None else 0))]
    parts.extend(segs)
    parts.append(units)
    pieces = {"header_bytes": len(parts[0]), "units_sha256": sha_bytes(units), "units_bytes": len(units),
              "units_lines": units.count(b"\n")}
    if s is not None:
        cls = []
        for i in B.ROWS:
            for c, d in itertools.combinations(B.COORDS, 2):
                a = tab[("g", s, (0, c), (i, 0))]
                b = tab[("g", s, (0, d), (i, 0))]
                cls.append(tuple(sorted((-a, -b))))
        tail = "".join("%d %d 0\n" % cl for cl in cls).encode("ascii")
        parts.append(tail)
        pieces.update({"tail_sha256": sha_bytes(tail), "tail_bytes": len(tail), "tail_lines": tail.count(b"\n")})
    return parts, pieces, t, s


def bound_identity(parts, segs, pieces, V, C, sup_t, it, binding):
    """Field-by-field comparison of the regenerated parts with the GBBINDING record and the PRE-EXEC copy."""
    brec = binding["records"][it["id"]]
    base = binding["gb_base"]
    h, n = sha_parts(parts)
    bh, bn = sha_parts(segs)
    hc = header_counts(parts[0])
    got = {"header": parts[0].decode("ascii", "replace"), "variables": V, "clauses": hc[1] if hc else None,
           "bytes": n, "sha256": h, "supports_row2to7": sup_t,
           "pieces": dict(pieces, body_sha256=bh, body_bytes=bn, body_clauses=C)}
    problems = []
    if it.get("bound") != {k: brec[k] for k in BOUND_FIELDS}:
        problems.append("the PRE-EXEC bound copy differs from the GBBINDING record")
    for k in ("header", "variables", "clauses", "bytes", "sha256", "supports_row2to7", "pieces"):
        if got[k] != brec[k]:
            problems.append("regenerated %s differs from GBBINDING: %r != %r" % (k, got[k], brec[k]))
    if (V, C, bn, bh, len(segs)) != (base["vars"], base["clauses"], base["body_bytes"], base["body_sha256"],
                                     base["body_segments"]):
        problems.append("regenerated GB base (vars, clauses, body bytes, body sha256, segments) %r differs from "
                        "GBBINDING gb_base" % ((V, C, bn, bh, len(segs)),))
    if hc != it["expected_checker_header_counts"]:
        problems.append("header counts %r != expected %r" % (hc, it["expected_checker_header_counts"]))
    if ((h, n) != (it["expected_solver_feed_sha256"], it["expected_solver_feed_bytes"])
            or (h, n) != (it["expected_checker_feed_sha256"], it["expected_checker_feed_bytes"])):
        problems.append("regenerated sha256/bytes differ from the PRE-EXEC expected feeds")
    return {"ok": not problems, "problems": problems, "regenerated": got, "at": now()}


def regenerate(it, binding, log):
    """The single in-memory regeneration of one gb input. -> (parts, identity record). Raises on any binder Stop or
    Abort (nothing has been launched then)."""
    t0 = time.monotonic()
    B = load_binder()
    ctx = B.check_inputs()
    gb_rows = [r for r in ctx["rows"] if r["path"] == GB_SOURCE]
    if len(gb_rows) != 1 or gb_rows[0]["sha256"] != GB_SOURCE_SHA or gb_rows[0]["ok"] is not True:
        die("binder check_inputs() did not pin the GB source to %s" % GB_SOURCE_SHA)
    t1 = time.monotonic()
    gbmod = B.load_gb(ctx["src"], "gram_b_r2_pinned_gbs1")
    gbmod.F = B.make_sink_class(gbmod.F, B.SEGMENT)
    F8 = gbmod.encode(*ctx["args"])
    segs = F8.finish()
    V, C = F8.n, F8.ncl
    t2 = time.monotonic()
    parts, pieces, t, _s = compose_parts(B, it["id"], F8.tab, V, C, segs, ctx["sup"])
    del F8, gbmod
    ident = bound_identity(parts, segs, pieces, V, C, ctx["sup"][t], it, binding)
    ident.update({"binder": {"path": BINDER, "sha256": BINDER_SHA,
                             "check_inputs_pins": ctx["rows"],
                             "encode_args": json.loads(json.dumps(ctx["args"])),
                             "flags": ctx["checks"].get("flags"),
                             "encode_args_equal_brief_call": ctx["checks"].get("encode_args_equal_brief_call"),
                             "gb_ast_facts": ctx["checks"].get("gb_ast_facts"),
                             "segment_bytes": B.SEGMENT, "segments": len(segs)},
                  "seconds": {"check_inputs": round(t1 - t0, 2), "encode": round(t2 - t1, 2),
                              "compose_and_identity": round(time.monotonic() - t2, 2)},
                  "peak_rss_bytes_self_after_regeneration": rss_peak()})
    log("regenerated %s in memory: %d bytes sha256 %s identity %s (%.1f s)"
        % (it["id"], ident["regenerated"]["bytes"], ident["regenerated"]["sha256"], "OK" if ident["ok"] else "FAILED",
           time.monotonic() - t0))
    return parts, ident


def rss_peak():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


# --- items, the parent GO record and the control-receipt admission prerequisite
def control_item(name):
    spec = CONTROLS.get(name) if isinstance(name, str) else None
    if spec is None:
        raise ValueError("unknown control %r (one of %s)" % (name, ", ".join(CONTROLS)))
    s, c = spec["solver"], spec["checker"]
    return {"item": "control:" + name, "kind": "control", "name": name, "label": LABEL_PREFIX + "ctl-" + name,
            "checker_feed_mode": spec["checker_feed"], "proof_feed_mode": spec["proof_feed"],
            "checker_feed_limit_bytes": len(c) - SHORT_BYTES if spec["checker_feed"] == "short" else len(c),
            "expected_solver_feed_sha256": sha_bytes(s), "expected_solver_feed_bytes": len(s),
            "expected_checker_feed_sha256": sha_bytes(c), "expected_checker_feed_bytes": len(c),
            "expected_checker_header_counts": header_counts(c),
            "preregistered_verdict": spec["verdict"], "preregistered_checker_outcomes": spec["outcomes"],
            "must_fail": list(spec["must_fail"]), "may_fail": list(spec["may_fail"]),
            "preregistered_observation": spec["observation"],
            "reservation_bytes": CONTROL_RESERVATION, "desk_cap_bytes": CONTROL_CAP, "stability_rule": False,
            "native_limits": {"kissat_seconds": KISSAT_SECONDS, "drat_trim_seconds": DRAT_SECONDS},
            "purpose": "transport/acceptance control on a synthetic 3-variable formula; not part of the replay"}


def gb_item(gid, attempt, binding):
    if gid not in GB_ITEMS:
        raise ValueError("gb:%s is not one of the eighteen authorized GB inputs" % (gid,))
    if not isinstance(attempt, str) or not ATTEMPT_RE.fullmatch(attempt):
        raise ValueError("gb:%s needs an attempt tag aN (newly named artifacts per attempt), got %r" % (gid, attempt))
    r = binding["records"][gid]
    return {"item": "gb:%s:%s" % (gid, attempt), "kind": "gb", "id": gid, "attempt": attempt,
            "label": LABEL_PREFIX + gid + "-" + attempt, "gb_kind": r["kind"], "source_template": r["source_template"],
            "monomial_square": r["monomial_square"], "gbbinding_sha256": GBBINDING_SHA,
            "bound": {k: r[k] for k in BOUND_FIELDS},
            "checker_feed_mode": "full", "proof_feed_mode": "plain", "checker_feed_limit_bytes": r["bytes"],
            "expected_solver_feed_sha256": r["sha256"], "expected_solver_feed_bytes": r["bytes"],
            "expected_checker_feed_sha256": r["sha256"], "expected_checker_feed_bytes": r["bytes"],
            "expected_checker_header_counts": [r["variables"], r["clauses"]],
            "reservation_bytes": GB_RESERVATION, "desk_cap_bytes": GB_PIPELINE_CAP, "stability_rule": True,
            "native_limits": {"kissat_seconds": KISSAT_SECONDS, "drat_trim_seconds": DRAT_SECONDS},
            "acceptance": ACCEPTANCE}


def validate_items(items, binding):
    """Shared validator for every PRE-EXEC this script writes or consumes: each item must EQUAL the item this script
    derives from its spec (controls from CONTROLS, gb items from the GBBINDING record), labels are unique, and a
    PRE-EXEC holds only controls or exactly one gb item. -> problems."""
    if not isinstance(items, list) or not items:
        return ["no item list"]
    problems, labels, kinds = [], set(), []
    for it in items:
        if not isinstance(it, dict):
            problems.append("item is not an object: %r" % (it,))
            continue
        kinds.append(it.get("kind"))
        try:
            if it.get("kind") == "control":
                want = control_item(it.get("name"))
            elif it.get("kind") == "gb":
                want = gb_item(it.get("id"), it.get("attempt"), binding)
            else:
                raise ValueError("unknown item kind %r" % (it.get("kind"),))
        except ValueError as e:
            problems.append(str(e))
            continue
        if it != want:
            problems.append("item %r differs from the derived item in %s"
                            % (it.get("item"), sorted(k for k in set(it) | set(want) if it.get(k) != want.get(k))))
        if it.get("label") in labels:
            problems.append("duplicate label %r" % it.get("label"))
        labels.add(it.get("label"))
    if len(set(kinds)) != 1:
        problems.append("a PRE-EXEC holds exactly one item kind, found %r" % sorted(set(map(str, kinds))))
    if "gb" in kinds and len(kinds) != 1:
        problems.append("a gb PRE-EXEC holds exactly one gb item (at most one science item per run)")
    return problems


def validate_go(go_path, pre_sha, script_sha, items):
    """The parent release (brief: admit only when the parent explicitly releases this desk). -> (record, problems)."""
    real = os.path.realpath(go_path)
    problems = []
    if not real.startswith(REVIEW + "/") or real.startswith(DESK + "/"):
        problems.append("the GO record must be a parent file under review/ outside this desk: %s" % real)
    try:
        raw = read_bytes(real)
    except OSError as e:
        return None, problems + ["GO record unreadable: %r" % e]
    try:
        g = json.loads(raw)
    except ValueError:
        return None, problems + ["GO record is not JSON"]
    scope = "controls" if items[0].get("kind") == "control" else "science"
    want = {"status": GO_STATUS, "desk": DESK_REL, "script_sha256": script_sha, "pre_exec_sha256": pre_sha,
            "scope": scope, "items": [it.get("item") for it in items]}
    if not isinstance(g, dict):
        return None, problems + ["GO record is not a JSON object"]
    for k, v in want.items():
        if g.get(k) != v:
            problems.append("GO field %s = %r, required %r" % (k, g.get(k), v))
    return {"path": real, "sha256": sha_bytes(raw), "bytes": len(raw), "scope": scope, "required": want,
            "fields": g}, problems


def validate_controls(script_sha):
    """gb admission prerequisite: the seven control receipts of THIS script sha256 exist, each equal to its derived
    control item, with its preregistered verdict, the pinned binaries, its PRE-EXEC and controls GO record re-hashed,
    no latched stop, and (F4'') the complete qualification of qualification_problems(): qualified commit, bound
    completion, no cancellation, clean durable run summary. -> (identities, problems)."""
    out, problems = [], []
    for name in CONTROLS:
        label = LABEL_PREFIX + "ctl-" + name
        path = os.path.join(DESK, "receipts", label + ".json")
        if not os.path.isfile(path):
            problems.append("%s: receipt missing" % label)
            continue
        raw = read_bytes(path)
        try:
            r = json.loads(raw)
        except ValueError:
            problems.append("%s: receipt is not JSON" % label)
            continue
        qident, qprobs = qualification_problems(label, CONTROLS[name]["verdict"])
        try:
            pe, go, bins = r.get("pre_exec") or {}, r.get("go") or {}, r.get("binaries") or {}
            pre_ok = (isinstance(pe.get("path"), str) and os.path.isfile(os.path.join(DESK, pe["path"]))
                      and sha_file(os.path.join(DESK, pe["path"])) == pe.get("sha256"))
            go_ok = (go.get("scope") == "controls" and isinstance(go.get("path"), str) and os.path.isfile(go["path"])
                     and sha_file(go["path"]) == go.get("sha256"))
            bad = [k for k, ok in (
                ("schema", r.get("schema") == RECEIPT_SCHEMA),
                ("script sha256", (r.get("script") or {}).get("sha256") == script_sha),
                ("item", r.get("item") == control_item(name)),
                ("verdict %s" % r.get("verdict"), r.get("verdict") == CONTROLS[name]["verdict"]),
                ("binaries", (bins.get("kissat") or {}).get("sha256") == KISSAT_SHA
                 and (bins.get("drat-trim") or {}).get("sha256") == DRAT_SHA),
                ("pre-exec binding", pre_ok),
                ("go binding", go_ok),
                ("stop latched", r.get("stop_latched") is None and r.get("stop_latched_after_evaluation") is None),
                ("qualification (%s)" % "; ".join(qprobs), not qprobs),
            ) if not ok]
        except (AttributeError, TypeError, ValueError, OSError) as e:  # a malformed receipt is refused, not trusted
            bad = ["malformed receipt: %r" % e]
        if bad:
            problems.append("%s: %s" % (label, ", ".join(bad)))
            continue
        out.append({"label": label, "receipt": rel(path), "receipt_sha256": sha_bytes(raw), "verdict": r["verdict"],
                    "commit_sha256": qident["commit_sha256"], "completion_sha256": qident["completion_sha256"],
                    "run_summary": qident["run_summary"], "run_summary_sha256": qident["run_summary_sha256"],
                    "pre_exec": pe, "go": {"path": go.get("path"), "sha256": go.get("sha256")},
                    "run_tag": r.get("run_tag")})
    return out, problems


# --- the staged pipeline: descriptor registry (replay_v5d.py Fds, unchanged) and the five worker threads
class Fds:
    """(A) Descriptor registry with an explicit, exactly-once handoff. A worker thread claims its descriptors with
    take() as the first action of its own run, so a failed Thread.start() (no thread, no claim) leaves them here for
    the pipeline cleanup. Whoever takes a descriptor first (worker or cleanup) is its only closer; nothing is closed
    twice and nothing is left without an owner."""

    def __init__(self):
        self._lock = threading.Lock()
        self._fds = {}

    def put(self, name, fd):
        with self._lock:
            if name in self._fds:
                raise RuntimeError("descriptor %s registered twice" % name)
            self._fds[name] = fd

    def get(self, name):
        with self._lock:
            return self._fds[name]

    def take(self, *names):
        """(F1') -> the named descriptors (None where absent), removed from the registry. The result list exists
        BEFORE any entry is removed and the removal loop allocates nothing (dict.pop into a preallocated slot, small
        int counter), so an allocation failure leaves every descriptor registered for the cleanup."""
        with self._lock:
            out, i, k = [None] * len(names), 0, len(names)
            while i < k:
                out[i] = self._fds.pop(names[i], None)
                i += 1
            return out

    def names(self):
        with self._lock:
            return list(self._fds)


def _writer(fds, name, parts, res, limit):
    """Measured CNF feed (replay_v5d.py _writer with an explicit byte limit; limit < total only for the short-cnf
    control): writes the parts in order, at most `limit` bytes, hashing exactly the bytes os.write() accepted. All
    worker state exists before the claim; the claim and everything after it run inside the try whose finally closes
    what was claimed."""
    h, total, fd = hashlib.sha256(), 0, None
    try:
        (fd,) = fds.take(name)  # claim: from here on this thread is the descriptor's only closer
        res["fd_claimed"] = fd is not None
        if fd is None:
            res["ok"] = False
            res["error"] = "descriptor %s was not handed over (taken by the cleanup first)" % name
            return
        for part in parts:
            if total >= limit:
                break
            mv = memoryview(part)
            off, size = 0, min(len(mv), limit - total)
            while off < size:
                n = os.write(fd, mv[off:min(off + CHUNK, size)])
                h.update(mv[off:off + n])
                off += n
                total += n
        res["ok"] = True
    except Exception as e:  # recorded, never hidden (EPIPE when the reader closed early)
        res["ok"] = False
        res["error"] = repr(e)
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except OSError as e:
                res["close_error"] = repr(e)
        res["written"] = total
        res["sha256"] = h.hexdigest()


def _collector(fds, res, chunks):
    """Stage-1 proof collector: named FIFO read end ('fifo_read') -> sha256/count -> chunks (RAM). fifo_eof_seen is
    set only when read() returns b''. ok = EOF seen and no read error, close error or exception."""
    h, st, src, close_status = hashlib.sha256(), {"n": 0}, None, [None]
    try:
        (src,) = fds.take("fifo_read")
        res["fd_claimed"] = src is not None
        if src is None:
            raise RuntimeError("descriptor fifo_read was not handed over (taken by the cleanup first)")
        while True:
            try:
                data = os.read(src, CHUNK)
            except OSError as e:
                res["read_error"] = "read: %r after %d collected bytes" % (e, st["n"])
                break
            if not data:
                res["fifo_eof_seen"] = True
                res["fifo_eof_at"] = now()
                break
            if st["n"] == 0:
                res["first_read_at"] = now()
            h.update(data)
            st["n"] += len(data)
            chunks.append(data)
    except Exception as e:  # recorded, never hidden
        res["collector_exception"] = repr(e)
    finally:
        if src is not None:
            try:
                os.close(src)
            except OSError as e:
                close_status[0] = e
        if close_status[0] is not None:
            res["close_error"] = repr(close_status[0])
        res.update({"collected_bytes": st["n"], "collected_sha256": h.hexdigest(), "chunks": len(chunks),
                    "finished_at": now(), "finished_mono": time.monotonic()})
        res["ok"] = (res.get("fifo_eof_seen") is True
                     and not any(k in res for k in ("read_error", "collector_exception", "close_error")))


def _feeder(fds, res, chunks, mode, hold, alter_at):
    """Stage-2 proof feeder: the RAM chunks -> drat-trim stdin pipe ('cpw'), hashing/counting exactly the bytes
    os.write() accepted; each chunk slot is released once handled, so the driver holds only the unfed remainder.
    Modes: plain; truncate (control: the last TRUNCATE_BYTES collected bytes are never written); suffix (control:
    SUFFIX is written after the collected proof); alter (control: bit 0 of the collected byte at alter_at is flipped in
    transit); hold (early-close control: the first write waits until the checker was reaped). A delivery error (EPIPE
    when the checker closed its proof input) stops delivery and every remaining chunk is released; the descriptor is
    closed exactly once. ok = no delivery error, exception or close error."""
    h, st, fd, close_status = hashlib.sha256(), {"fed": 0, "proof_fed": 0, "total": 0, "open": True}, None, [None]

    def deliver(data):
        mv, off = memoryview(data), 0
        while off < len(mv):
            try:
                n = os.write(fd, mv[off:off + CHUNK])
            except OSError as e:
                res["delivery_error"] = ("%s: the checker's proof input refused bytes after %d fed"
                                         % ("EPIPE" if isinstance(e, BrokenPipeError) else repr(e), st["fed"]))
                res["delivery_error_at"] = now()
                st["open"] = False
                return off
            h.update(mv[off:off + n])
            off += n
            st["fed"] += n
        return off

    try:
        (fd,) = fds.take("cpw")
        res["fd_claimed"] = fd is not None
        if fd is None:
            raise RuntimeError("descriptor cpw was not handed over (taken by the cleanup first)")
        for c in chunks:
            st["total"] += len(c)
        limit = st["total"] - TRUNCATE_BYTES if mode == "truncate" else st["total"]
        if hold is not None:
            res["hold_released_by_event"] = hold.wait(HOLD_SECONDS)
        off = 0
        for i in range(len(chunks)):
            c = chunks[i]
            chunks[i] = None  # the slot is released whether or not the bytes are written
            if st["open"] and off < limit:
                data = memoryview(c)[:min(len(c), limit - off)]
                if mode == "alter" and alter_at is not None and off <= alter_at < off + len(data):
                    data = bytearray(data)
                    data[alter_at - off] ^= 1
                    res["altered_offset"] = alter_at
                st["proof_fed"] += deliver(data)
                data = None
            off += len(c)
            c = None
        if mode == "suffix" and st["open"]:
            res["suffix_delivered_bytes"] = deliver(SUFFIX)
    except Exception as e:  # recorded, never hidden
        res["feeder_exception"] = repr(e)
    finally:
        try:  # (F3) the claimed descriptor is closed first, unconditionally, before any release or diagnostic
            if fd is not None:
                try:
                    os.close(fd)
                except OSError as e:
                    close_status[0] = e
        finally:
            chunks.clear()  # release whatever an exception left (no iterator is allocated for this)
            if close_status[0] is not None:
                res["close_error"] = repr(close_status[0])
            res.update({"mode": mode, "fed_bytes": st["fed"], "fed_sha256": h.hexdigest(),
                        "collected_total": st["total"], "proof_bytes_fed": st["proof_fed"],
                        "undelivered_bytes": st["total"] - st["proof_fed"], "finished_at": now(),
                        "finished_mono": time.monotonic()})
            res["ok"] = not any(k in res for k in ("delivery_error", "feeder_exception", "close_error"))


DUP_LINE = re.compile(rb"\rc WARNING: detected and deleted duplicate literal (-?[1-9][0-9]*) at position ([1-9][0-9]*) "
                      rb"of proof line ([1-9][0-9]*)\n")
PARSE_LINE = re.compile(rb"c parsing input formula with (\d+) variables and (\d+) clauses")
FINISHED_LINE = re.compile(rb"c finished parsing(, read (\d+) bytes from proof file)?")
ERROR_KEYS = (b"ERROR", b"MEMOUT", b"illegal literal", b"error opening", b"wrong binary prefix",
              b"failed to reallocate")  # (F1) the fatal-class diagnostics of the pinned drat-trim.c


def _filter(fds, res, header_clauses):
    """drat-trim stdout+stderr ('cor') -> full raw sha256/bytes/LF count -> drop ONLY lines that fullmatch DUP_LINE
    (the exact duplicate-literal normalization line, counted per phase: proof line number <= the header clause count
    is the formula phase) -> every other byte to the filtered log ('dlog', O_EXCL). Each kept line is parsed with only
    CR removed: status lines (starting with 's'), the parse-count line, the finished-parsing line, NOT VERIFIED,
    TIMEOUT, early EOF, less-than-expected, ERROR-class and WARNING lines. A log write error stops writing but the raw
    stream is still read to EOF, so the checker never blocks; an unterminated final line is kept (it cannot match)."""
    hr, hk = hashlib.sha256(), hashlib.sha256()
    st = {"raw_bytes": 0, "raw_lf": 0, "dup_lines": 0, "dup_formula_phase": 0, "dup_proof_phase": 0,
          "kept_lines": 0, "kept_bytes": 0, "log_open": True, "unterminated_tail_bytes": 0}
    ob = {"status_lines": [], "status_line_count": 0, "header_counts": [], "header_count_lines": 0,
          "proof_bytes_parsed": [], "finished_lines": 0, "not_verified_lines": 0, "timeout_lines": 0,
          "early_eof_lines": 0, "less_than_expected_lines": 0, "error_lines": [], "error_line_count": 0,
          "warning_line_count": 0, "header_error_line_exact": False, "critical_lines": []}
    src = log = None
    close_status, pending = [None, None], [b""]

    def keep(line):
        if st["log_open"]:
            mv, off = memoryview(line), 0
            while off < len(mv):
                try:
                    n = os.write(log, mv[off:])
                except OSError as e:
                    res["log_write_error"] = repr(e)
                    st["log_open"] = False
                    break
                hk.update(mv[off:off + n])
                off += n
                st["kept_bytes"] += n
        st["kept_lines"] += 1
        text = line.replace(b"\r", b"")
        if text.endswith(b"\n"):
            text = text[:-1]
        critical = False
        if text.startswith(b"s"):
            ob["status_line_count"] += 1
            critical = True
            if len(ob["status_lines"]) < LIST_CAP:
                ob["status_lines"].append(text.decode("ascii", "replace"))
        if b"s NOT VERIFIED" in text:
            ob["not_verified_lines"] += 1
            critical = True
        if b"s TIMEOUT" in text:
            ob["timeout_lines"] += 1
            critical = True
        if b"early EOF" in text:
            ob["early_eof_lines"] += 1
            critical = True
        if b"clauses less than expected" in text:
            ob["less_than_expected_lines"] += 1
            critical = True
        m = PARSE_LINE.search(text)
        if m is not None:
            ob["header_count_lines"] += 1
            critical = True
            if len(ob["header_counts"]) < LIST_CAP:
                ob["header_counts"].append([int(m.group(1)), int(m.group(2))])
        m = FINISHED_LINE.search(text)
        if m is not None:
            ob["finished_lines"] += 1
            critical = True
            if m.group(2) is not None and len(ob["proof_bytes_parsed"]) < LIST_CAP:
                ob["proof_bytes_parsed"].append(int(m.group(2)))
        if text == DRAT_NO_HEADER_LINE:
            ob["header_error_line_exact"] = True
        if any(k in text for k in ERROR_KEYS):
            ob["error_line_count"] += 1
            critical = True
            if len(ob["error_lines"]) < LIST_CAP:
                ob["error_lines"].append(text[:300].decode("ascii", "replace"))
        if b"WARNING" in text:
            ob["warning_line_count"] += 1
            critical = True
        if critical and len(ob["critical_lines"]) < LIST_CAP:
            ob["critical_lines"].append(text[:300].decode("ascii", "replace"))

    def handle(line):
        m = DUP_LINE.fullmatch(line)
        if m is None:
            keep(line)
            return
        st["dup_lines"] += 1
        if header_clauses is not None and int(m.group(3)) <= header_clauses:
            st["dup_formula_phase"] += 1
        else:
            st["dup_proof_phase"] += 1

    try:
        src, log = fds.take("cor", "dlog")
        res["fds_claimed"] = {"cor": src is not None, "dlog": log is not None}
        if src is None or log is None:
            raise RuntimeError("descriptor handoff incomplete %s (taken by the cleanup first)" % res["fds_claimed"])
        while True:
            try:
                data = os.read(src, FILTER_READ)
            except OSError as e:
                res["read_error"] = "read: %r after %d raw bytes" % (e, st["raw_bytes"])
                break
            if not data:
                res["eof_seen"] = True
                break
            hr.update(data)
            st["raw_bytes"] += len(data)
            st["raw_lf"] += data.count(b"\n")
            lines = (pending[0] + data).split(b"\n")
            pending[0] = lines.pop()
            for line in lines:
                handle(line + b"\n")
        if pending[0]:
            st["unterminated_tail_bytes"] = len(pending[0])
            keep(pending[0])
            pending[0] = b""
    except Exception as e:  # recorded, never hidden
        res["filter_exception"] = repr(e)
    finally:
        try:  # both claimed descriptors are closed first, independently
            if log is not None:
                try:
                    os.close(log)
                except OSError as e:
                    close_status[0] = e
        finally:
            if src is not None:
                try:
                    os.close(src)
                except OSError as e:
                    close_status[1] = e
        errs = [repr(e) for e in close_status if e is not None]
        if errs:
            res["close_errors"] = errs
        res.update(st)
        res.update(ob)
        res.update({"raw_sha256": hr.hexdigest(), "kept_sha256": hk.hexdigest(), "header_clauses": header_clauses,
                    "finished_at": now(), "finished_mono": time.monotonic()})
        res["ok"] = (res.get("eof_seen") is True
                     and not any(k in res for k in ("read_error", "log_write_error", "filter_exception",
                                                    "close_errors")))


def first_literal_byte(proof):
    """Offset of the first one-byte literal (value 2..127) on an 'a' line of a binary DRAT proof, or None. Flipping its
    bit 0 negates that literal and keeps the byte count and the line structure (digest-alter control only)."""
    i, n = 0, len(proof)
    while i < n:
        marker = proof[i]
        i += 1
        if marker not in (0x61, 0x64):
            return None
        while True:
            start = i
            while i < n and proof[i] & 0x80:
                i += 1
            if i >= n:
                return None
            i += 1
            if i - start == 1 and proof[start] == 0:
                break
            if marker == 0x61 and i - start == 1 and 2 <= proof[start] <= 127:
                return start
    return None


def _thread(target, args, res):
    """A worker handle, NOT started: the pipeline registers it first and then starts it, so an interrupted start()
    is still joined and reported; its descriptors stay in the registry until the started thread claims them."""
    return threading.Thread(target=target, args=args, daemon=True), res


def acquire_open(fds, name, path, flags, mode, rollback):
    """(F3') Open one descriptor and register it under name. All state exists before the open; the scalar fd returned
    by os.open() is stored in this function's own cleanup scope before any other operation (no wrapper object is
    allocated), and it is closed here unless its registry insertion committed, so no failure between the open and the
    registration (e.g. a MemoryError in the insertion) leaves an untracked descriptor. Committed descriptors belong to
    the registry, whose cleanup closes any that no thread claims. rollback collects close errors of that rare path."""
    fd, committed = None, False
    try:
        fd = os.open(path, flags, mode)
        fds.put(name, fd)
        committed = True
    finally:
        if fd is not None and not committed:
            _rollback_close(fd, rollback)


def acquire_pipe(fds, rname, wname, rollback):
    """(F3') os.pipe() and register both ends; an end whose insertion did not commit is closed here (os.pipe returns
    the pair itself, so no wrapper is allocated by this script between the syscall and the bookkeeping)."""
    got, first, second = None, False, False
    try:
        got = os.pipe()
        fds.put(rname, got[0])
        first = True
        fds.put(wname, got[1])
        second = True
    finally:
        if got is not None:
            if not first:
                _rollback_close(got[0], rollback)
            if not second:
                _rollback_close(got[1], rollback)


def _rollback_close(fd, rollback):
    try:
        os.close(fd)
    except OSError as e:
        rollback.append(repr(e))


def _child_record(status, ru, spawn_mono, sigterm_sent):
    """Diagnostics of a reaped child (built only after the child is marked reaped, so a failure here can never lead to
    signalling or waiting for the reaped pid again)."""
    exited, signaled = os.WIFEXITED(status), os.WIFSIGNALED(status)
    return {"rc": os.waitstatus_to_exitcode(status), "exited": exited,
            "exit_code": os.WEXITSTATUS(status) if exited else None, "signaled": signaled,
            "term_signal": os.WTERMSIG(status) if signaled else None, "sigterm_sent": sigterm_sent,
            "maxrss_bytes": ru.ru_maxrss, "wall_seconds": round(time.monotonic() - spawn_mono, 3),
            "user_seconds": round(ru.ru_utime, 3), "sys_seconds": round(ru.ru_stime, 3), "reaped_at": now(),
            "reaped_mono": time.monotonic()}


THREAD_NAMES = ("collector", "solver_feed", "filter", "checker_feed", "feeder")


def pipeline(label, it, solver_parts, checker_parts, identity, log, stop):
    """Staged kissat -> RAM -> drat-trim pipeline for one item. identity(stage, parts) re-hashes every identity before
    the spawn of that stage; spawn_veto() re-checks stop, cutoff, deadline, scanner/exclusion latches and the launch
    threshold immediately before each Popen. One cleanup scope covers everything from the first descriptor to the
    last reap: any exception SIGTERMs the live (never an already reaped) child, reaps it within 120 s and closes every
    descriptor no thread claimed (exactly once). -> record."""
    fifo = os.path.join(DESK, "fifo", label + ".kissat.fifo")
    klog = os.path.join(DESK, "logs", label + ".kissat.log")
    dlog = os.path.join(DESK, "logs", label + ".drat.filtered.log")
    tdir = os.path.join(TMP, label)
    ktmp, dtmp = os.path.join(tdir, "kissat"), os.path.join(tdir, "drat")
    for path in (fifo, klog, dlog, tdir):
        if os.path.lexists(path):
            raise FileExistsError(path)
    os.mkdir(tdir)
    os.mkdir(ktmp)
    os.mkdir(dtmp)
    kenv, denv = dict(ENV, TMPDIR=ktmp + "/"), dict(ENV, TMPDIR=dtmp + "/")
    reservation, cap = it["reservation_bytes"], it["desk_cap_bytes"]
    kissat_argv = [KISSAT, "--time=%d" % KISSAT_SECONDS]
    drat_opts = ["-i", "-t", str(DRAT_SECONDS)]
    rec = {"label": label, "fifo": rel(fifo), "kissat_log": rel(klog), "drat_filtered_log": rel(dlog),
           "kissat_argv": kissat_argv + ["/dev/fd/<solver-cnf-pipe>", rel(fifo)],
           "drat_argv": [DRAT, "/dev/fd/<checker-cnf-pipe>"] + drat_opts,
           "drat_stdin": "anonymous pipe written only by the parent feeder thread from the RAM proof (stage 2)",
           "drat_stdout": "anonymous pipe (stdout and stderr) read only by the parent filter thread",
           "checker_feed_mode": it["checker_feed_mode"], "proof_feed_mode": it["proof_feed_mode"],
           "cwd": {"kissat": rel(ktmp), "drat": rel(dtmp)}, "env": {"kissat": kenv, "drat": denv},
           "reservation_bytes": reservation, "desk_cap_bytes": cap, "lane_rss_limit_bytes": LANE_RSS_LIMIT,
           "lane_busy_cap": LANE_BUSY_CAP, "free_floor_bytes": FLOOR, "launch_floor_bytes": LAUNCH_FLOOR,
           "stage_backstop_seconds": {"kissat": KISSAT_SECONDS + STAGE_MARGIN, "drat": DRAT_SECONDS + STAGE_MARGIN},
           "stale_lane_reading_seconds": STALE_SECONDS, "stops": STOPS}
    fds, threads, events, rollback = Fds(), {}, [], []
    procs = {"solver": None, "checker": None}  # (F2) ownership slots exist before any Popen
    reaped = {"solver": False, "checker": False}  # (F2) set immediately after wait4 returns the child's pid
    sigterm_sent = {"solver": None, "checker": None}
    rss_fail = {"solver": 0, "checker": 0}
    done = {}  # diagnostics of reaped children (built after the reaped mark)
    ev_checker = threading.Event()
    scanner = Scanner()
    chunks = []  # the RAM proof: appended by the collector, released slot by slot by the feeder
    S = {"reason": None, "term_at": None, "grace_exceeded": False, "spawn_mono": {"solver": None, "checker": None},
         "peak_desk": 0, "peak_driver": 0, "peak_child": {"solver": 0, "checker": 0}, "peak_lane_total": 0,
         "peak_lane_reserved": 0, "peak_other": 0, "other_rss": 0, "cur_busy": 0, "max_other_busy": 0,
         "min_free": None, "last_mono": None, "prev_cpu": None, "prev_mono": None, "scan_started": None,
         "exclusion_seen": None, "alter_at": None}
    closed_by_cleanup, cleanup_errors = [], []

    def close_fd(name):  # take() first: a descriptor is closed by exactly one owner
        (fd,) = fds.take(name)
        if fd is not None:
            os.close(fd)

    def live(name):
        return procs[name] is not None and not reaped[name]

    def term_live(why):
        for n in CHILD_NAMES:
            if live(n):  # (F2) never a reaped pid
                try:
                    os.kill(procs[n].pid, signal.SIGTERM)
                    sigterm_sent[n] = now()
                    events.append({"at": now(), "event": "SIGTERM", "target": n, "pid": procs[n].pid, "reason": why})
                except ProcessLookupError:
                    pass

    def stop_now(why):
        S["reason"] = why
        S["term_at"] = time.monotonic()
        term_live(why)
        log("SAFETY STOP %s: %s" % (label, why))

    def reap():
        for name in CHILD_NAMES:
            if not live(name):
                continue
            p = procs[name]
            pid, status, ru = os.wait4(p.pid, os.WNOHANG)
            if pid:
                reaped[name] = True  # (F2) ownership ends here, before any allocation: never signalled/waited again
                p.returncode = status  # (F2) Popen itself never polls this pid again (exit code set below)
                if name == "solver":
                    close_fd("keepalive")  # the collector sees EOF once kissat's own write end is gone too
                else:
                    ev_checker.set()
                p.returncode = os.waitstatus_to_exitcode(status)
                done[name] = _child_record(status, ru, S["spawn_mono"][name], sigterm_sent[name] is not None)

    def lane_guard(tnow):
        """Latched scanner failure, exclusion or survivor, a failed or stale reading, or an exclusion breach in the
        newest reading (latched here too) -> reason; otherwise refresh the other-lane RSS/busy figures -> None."""
        late = latched_stop({}, scanner)
        if late is not None:
            return late
        reading = scanner.reading()
        if reading is None:
            if S["scan_started"] is not None and tnow - S["scan_started"] > STALE_SECONDS:
                return "no lane scan reading within %.0f s" % STALE_SECONDS
            return None
        mono, scan, err = reading
        if scan is None:
            return "lane scan failed: %s" % err
        if tnow - mono > STALE_SECONDS:
            return "lane scan reading stale (%.1f s old)" % (tnow - mono)
        if mono != S["last_mono"]:
            S["last_mono"] = mono
            S["other_rss"] = sum(c["rss_bytes"] for c in scan)
            busy, cpu = 0, {}
            for c in scan:
                cpu[c["pid"]] = c["cpu_ns"]
                if c["native"]:
                    busy += 1
                elif (S["prev_cpu"] is not None and c["cpu_ns"] is not None
                      and S["prev_cpu"].get(c["pid"]) is not None and mono > S["prev_mono"]):
                    if (c["cpu_ns"] - S["prev_cpu"][c["pid"]]) / ((mono - S["prev_mono"]) * 1e9) >= HOT_CPU_FRACTION:
                        busy += 1
            S["prev_cpu"], S["prev_mono"] = cpu, mono
            S["cur_busy"] = busy
            S["max_other_busy"] = max(S["max_other_busy"], busy)
            S["peak_other"] = max(S["peak_other"], S["other_rss"])
            ex = exclusions(scan)
            if ex and S["exclusion_seen"] is None:
                S["exclusion_seen"] = ex
                events.append({"at": now(), "event": "exclusion breach", "exclusions": ex})
        if S["exclusion_seen"] is not None:
            return "exclusion breach (latched): %s" % json.dumps(S["exclusion_seen"])[:400]
        return None

    def supervise(name, backstop):
        """Poll until the stage's child is reaped (or the SIGTERM grace is exceeded); every safety stop SIGTERMs it."""
        p = procs[name]
        while True:
            reap()
            if reaped[name]:
                if S["reason"] is None:  # latched signal / scanner failure / exclusion / survivor before leaving
                    late = latched_stop(stop, scanner)
                    if late is not None:
                        S["reason"] = late
                        events.append({"at": now(), "event": "stop latched at the completion break", "stage": name,
                                       "reason": late})
                        log("SAFETY STOP %s at the %s completion break: %s" % (label, name, late))
                return
            tnow = time.monotonic()
            guard_fail = None
            own = taskinfo(os.getpid())
            driver = own[0] if own else 0
            if own is None:
                guard_fail = "driver RSS unreadable"
            desk = driver
            t = taskinfo(p.pid)
            if t is None:  # one miss can be an exit between wait4 and the read; two in a row cannot
                rss_fail[name] += 1
                if rss_fail[name] >= 2 and guard_fail is None:
                    guard_fail = "own child %s (pid %d) RSS unreadable twice in a row" % (name, p.pid)
            else:
                rss_fail[name] = 0
                desk += t[0]
                S["peak_child"][name] = max(S["peak_child"][name], t[0])
            S["peak_driver"] = max(S["peak_driver"], driver)
            S["peak_desk"] = max(S["peak_desk"], desk)
            lane_fail = lane_guard(tnow)
            if guard_fail is None:
                guard_fail = lane_fail
            lane_total = S["other_rss"] + desk
            lane_reserved = S["other_rss"] + max(desk, reservation)
            S["peak_lane_total"] = max(S["peak_lane_total"], lane_total)
            S["peak_lane_reserved"] = max(S["peak_lane_reserved"], lane_reserved)
            fb = free_bytes()
            S["min_free"] = fb if S["min_free"] is None else min(S["min_free"], fb)
            if S["reason"] is None:
                why = None
                if stop.get("signal"):
                    why = "driver received %s" % stop["signal"]
                elif guard_fail is not None:
                    why = "guard reading failed: " + guard_fail
                elif S["cur_busy"] + MINE > LANE_BUSY_CAP:  # (F6) the busy cap is enforced in flight too
                    why = "lane busy %d other + %d > %d in flight" % (S["cur_busy"], MINE, LANE_BUSY_CAP)
                elif lane_reserved > LANE_RSS_LIMIT:
                    why = ("lane RSS %d > 11 GiB (%d): other lane %d + max(pipeline %d, reservation %d)"
                           % (lane_reserved, LANE_RSS_LIMIT, S["other_rss"], desk, reservation))
                elif desk > cap:
                    why = ("pipeline aggregate RSS %d > cap %d (driver %d incl. CNF parts and RAM proof + %s)"
                           % (desk, cap, driver, name))
                elif fb < FLOOR:
                    why = "free bytes %d < in-flight floor %d" % (fb, FLOOR)
                elif tnow - S["spawn_mono"][name] > backstop:
                    why = "%s stage wall %.1f s > limit + 120 s (%d s)" % (name, tnow - S["spawn_mono"][name], backstop)
                elif time.time() >= NATIVE_STOP_AT:
                    why = "host clock reached the native-work deadline 2026-10-18 17:57:00 PDT"
                if why is not None:
                    stop_now(why)
            elif time.monotonic() - S["term_at"] > SIGTERM_GRACE:
                S["grace_exceeded"] = True
                events.append({"at": now(), "event": "SIGTERM grace of %d s exceeded; no escalation" % SIGTERM_GRACE,
                               "alive": [n for n in CHILD_NAMES if live(n)]})
                log("SIGTERM grace exceeded for %s (%s); no escalation" % (label, name))
                return
            time.sleep(SAMPLE)

    def settle(names):
        """Bounded joins of a stage's worker threads after its child was reaped; an unfinished one stops the item."""
        for name in names:
            if name not in threads or threads[name][0].ident is None:
                continue
            t, res = threads[name]
            t.join(JOIN_SECONDS)
            res["thread_started"] = True
            res["thread_finished"] = not t.is_alive()
            if t.is_alive() and S["reason"] is None:
                S["reason"] = "%s thread did not finish within %.0f s after its stage ended" % (name, JOIN_SECONDS)
                events.append({"at": now(), "event": "thread unfinished", "thread": name})
                log("SAFETY STOP %s: %s" % (label, S["reason"]))

    def boundary(stage):
        """(F4, F6) Shared launch-boundary predicate -> reason or None: a latched driver signal, scanner failure,
        exclusion breach or helper survivor, the 17:29 cutoff, the 17:57 deadline, free below the launch threshold
        12.2e9 + 10 MiB; for the checker also the newest lane reading (stale/failed/exclusion), lane busy + 1 <= 4 and
        the 11 GiB lane total."""
        late = latched_stop(stop, scanner)
        if late is not None:
            return "%s at the %s launch boundary" % (late, stage)
        if time.time() >= NO_LAUNCH_AT:
            return "launch cutoff 2026-10-18 17:29:00 PDT reached at the %s launch boundary" % stage
        if time.time() >= NATIVE_STOP_AT:
            return "native-work deadline 2026-10-18 17:57:00 PDT reached at the %s launch boundary" % stage
        fb = free_bytes()
        if fb < LAUNCH_FLOOR:
            return "free bytes %d < launch threshold %d at the %s launch boundary" % (fb, LAUNCH_FLOOR, stage)
        if stage == "checker":
            lane_fail = lane_guard(time.monotonic())
            if lane_fail is not None:
                return "guard reading failed at the checker launch boundary: " + lane_fail
            if S["cur_busy"] + MINE > LANE_BUSY_CAP:
                return "lane busy %d other + %d > %d at the checker launch boundary" % (S["cur_busy"], MINE,
                                                                                         LANE_BUSY_CAP)
            own = taskinfo(os.getpid())
            if own is None:
                return "driver RSS unreadable at the checker launch boundary"
            if S["other_rss"] + max(own[0], reservation) > LANE_RSS_LIMIT:
                return "lane RSS above 11 GiB at the checker launch boundary"
        return None

    def spawn_block(idrec, stage):
        """Before the stage's setup: the identity re-hash and the launch-boundary predicate."""
        if not idrec.get("ok"):
            return "identity re-hash before the %s spawn failed: %s" % (stage, "; ".join(idrec.get("problems") or []))
        return boundary(stage)

    def stage1_ok():
        s = done.get("solver") or {}
        co = threads["collector"][1] if "collector" in threads else {}
        sw = threads["solver_feed"][1] if "solver_feed" in threads else {}
        status = status_lines(read_bytes(klog))
        checks = {
            "no_stop_reason": S["reason"] is None,
            "solver_self_exit_20": s.get("exited") is True and s.get("exit_code") == 20 and not s.get("sigterm_sent"),
            "solver_status_exact_unsat": status == ["s UNSATISFIABLE"],
            "collector_finished_clean_eof": co.get("thread_finished") is True and co.get("ok") is True,
            "proof_positive": (co.get("collected_bytes") or 0) > 0,
            "solver_feed_measured_complete": feed_ok(sw, it["expected_solver_feed_bytes"],
                                                     it["expected_solver_feed_sha256"]),
            "no_latched_stop": latched_stop(stop, scanner) is None,
            "launch_cutoff_not_reached": time.time() < NO_LAUNCH_AT,
        }
        return {"ok": all(checks.values()), "checks": checks, "failed": [k for k, v in checks.items() if not v],
                "solver_status_lines": status, "at": now()}

    rec["started_at"] = now()
    t0 = time.monotonic()
    os.mkfifo(fifo)  # spent FIFO nodes are retained: this script never unlinks anything
    with open(klog, "xb") as kl:
        try:  # one cleanup scope for everything from the first descriptor to the last reap
            # ------------------------------------------------ stage 1: kissat alone; proof FIFO -> RAM collector
            rec["identity_solver"] = identity("solver", solver_parts)
            why = spawn_block(rec["identity_solver"], "solver")
            if why is not None:
                S["reason"] = why
                log("STOP before the kissat setup %s: %s" % (label, why))
            else:
                acquire_open(fds, "fifo_read", fifo, os.O_RDONLY | os.O_NONBLOCK, 0o644, rollback)
                fcntl.fcntl(fds.get("fifo_read"), fcntl.F_SETFL,
                            fcntl.fcntl(fds.get("fifo_read"), fcntl.F_GETFL) & ~os.O_NONBLOCK)
                acquire_open(fds, "keepalive", fifo, os.O_WRONLY, 0o644, rollback)
                acquire_pipe(fds, "scr", "scw", rollback)
                res = {"ok": False}
                threads["collector"] = _thread(_collector, (fds, res, chunks), res)  # registered before start()
                threads["collector"][0].start()
                why = boundary("solver")  # (F4) immediately before the Popen
                if why is not None:
                    S["reason"] = why
                    rec["stop_at_solver_launch_boundary"] = why
                    log("STOP at the kissat launch boundary %s: %s" % (label, why))
                else:
                    S["spawn_mono"]["solver"] = time.monotonic()
                    try:  # (F2) the preallocated slot is filled the moment Popen returns
                        procs["solver"] = subprocess.Popen(kissat_argv + ["/dev/fd/%d" % fds.get("scr"), fifo],
                                                           stdin=subprocess.DEVNULL, stdout=kl,
                                                           stderr=subprocess.STDOUT, pass_fds=(fds.get("scr"),),
                                                           cwd=ktmp, env=kenv)
                    except OSError as e:  # a spawn error is a stop reason; nothing more is launched
                        rec["solver_spawn_error"] = repr(e)
                        S["reason"] = "solver spawn failed: %r" % e
                if live("solver"):
                    rec["solver_pid"] = procs["solver"].pid
                    rec["solver_spawned_at"] = now()
                    close_fd("scr")
                    res = {"ok": False, "fd": "scw", "expected_len": sum(len(x) for x in solver_parts),
                           "limit": sum(len(x) for x in solver_parts)}
                    threads["solver_feed"] = _thread(_writer, (fds, "scw", solver_parts, res, res["limit"]), res)
                    threads["solver_feed"][0].start()
                    scanner.start()
                    S["scan_started"] = time.monotonic()
                    log("stage 1 %s: kissat pid %d" % (label, procs["solver"].pid))
                    supervise("solver", KISSAT_SECONDS + STAGE_MARGIN)
                else:
                    close_fd("scr")
                    close_fd("scw")
                    close_fd("keepalive")  # no writer: the collector reads EOF and finishes
                if not S["grace_exceeded"]:
                    settle(("collector", "solver_feed"))
            rec["stage1_finished_at"] = now()
            pre2 = stage1_ok() if reaped["solver"] else {"ok": False, "failed": ["kissat not run or not reaped"]}
            rec["stage2_preconditions"] = pre2
            if S["reason"] is None and not pre2["ok"]:
                rec["stage2_skipped"] = pre2["failed"]
                log("stage 2 of %s not started: %s" % (label, ", ".join(pre2["failed"])))
            if S["reason"] is None and pre2["ok"]:
                # ------------------------------------------ stage 2: drat-trim alone; measured CNF + RAM proof
                bh, bn = sha_parts(chunks)  # independent digest of the RAM buffer that the feeder will write
                rec["proof_buffer"] = {"chunks": len(chunks), "bytes": bn, "sha256": bh, "at": now()}
                if it["proof_feed_mode"] == "alter":
                    S["alter_at"] = first_literal_byte(b"".join(chunks))
                    rec["proof_buffer"]["alter_offset"] = S["alter_at"]
                rec["identity_checker"] = identity("checker", checker_parts)
                why = spawn_block(rec["identity_checker"], "checker")
                if why is not None:
                    S["reason"] = why
                    log("STOP before the drat-trim setup %s: %s" % (label, why))
                else:
                    acquire_pipe(fds, "ccr", "ccw", rollback)
                    acquire_pipe(fds, "cpr", "cpw", rollback)
                    acquire_pipe(fds, "cor", "cow", rollback)
                    acquire_open(fds, "dlog", dlog, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644, rollback)
                    res = {"ok": False}
                    threads["filter"] = _thread(_filter, (fds, res, (it["expected_checker_header_counts"] or
                                                                     [None, None])[1]), res)
                    threads["filter"][0].start()
                    why = boundary("checker")  # (F4, F6) immediately before the Popen
                    if why is not None:
                        S["reason"] = why
                        rec["stop_at_checker_launch_boundary"] = why
                        log("STOP at the drat-trim launch boundary %s: %s" % (label, why))
                    else:
                        S["spawn_mono"]["checker"] = time.monotonic()
                        try:  # (F2) the preallocated slot is filled the moment Popen returns
                            procs["checker"] = subprocess.Popen([DRAT, "/dev/fd/%d" % fds.get("ccr")] + drat_opts,
                                                                stdin=fds.get("cpr"), stdout=fds.get("cow"),
                                                                stderr=subprocess.STDOUT, pass_fds=(fds.get("ccr"),),
                                                                cwd=dtmp, env=denv)
                        except OSError as e:
                            rec["checker_spawn_error"] = repr(e)
                            S["reason"] = "checker spawn failed: %r" % e
                    close_fd("ccr")
                    close_fd("cpr")
                    close_fd("cow")  # from here the filter sees EOF when drat-trim's copies are gone
                    if live("checker"):
                        rec["checker_pid"] = procs["checker"].pid
                        rec["checker_spawned_at"] = now()
                        res = {"ok": False, "fd": "ccw", "expected_len": sum(len(x) for x in checker_parts),
                               "limit": it["checker_feed_limit_bytes"]}
                        threads["checker_feed"] = _thread(_writer, (fds, "ccw", checker_parts, res, res["limit"]), res)
                        threads["checker_feed"][0].start()
                        res = {"ok": False, "mode": it["proof_feed_mode"]}
                        hold = ev_checker if it["proof_feed_mode"] == "hold" else None
                        threads["feeder"] = _thread(_feeder, (fds, res, chunks, it["proof_feed_mode"], hold,
                                                              S["alter_at"]), res)
                        threads["feeder"][0].start()
                        log("stage 2 %s: drat-trim pid %d" % (label, procs["checker"].pid))
                        supervise("checker", DRAT_SECONDS + STAGE_MARGIN)
                    else:
                        close_fd("ccw")
                        close_fd("cpw")
                    if not S["grace_exceeded"]:
                        settle(("filter", "checker_feed", "feeder"))
        except BaseException as e:  # SIGTERM the live child, bounded reap, UNKNOWN; cmd_run launches nothing more
            rec["exception"] = "%s: %s" % (type(e).__name__, e)
            rec["exception_traceback"] = traceback.format_exc()[-4000:]
            if S["reason"] is None:
                S["reason"] = "exception in pipeline: " + rec["exception"]
            term_live(S["reason"])
            try:
                log("EXCEPTION in pipeline %s: %s" % (label, rec["exception"]))
            except Exception as e3:  # recorded, never hidden (e.g. a full disk refusing the log line)
                events.append({"at": now(), "event": "driver log write failed", "error": repr(e3)})
            t_end = time.monotonic() + SIGTERM_GRACE
            while (live("solver") or live("checker")) and time.monotonic() < t_end:
                try:
                    reap()
                except Exception as e2:  # recorded, never hidden
                    events.append({"at": now(), "event": "reap failed during exception cleanup", "error": repr(e2)})
                    break
                time.sleep(SAMPLE)
            if live("solver") or live("checker"):
                S["grace_exceeded"] = True
                events.append({"at": now(), "event": "children alive after exception cleanup; no escalation",
                               "alive": [n for n in CHILD_NAMES if live(n)]})
        finally:
            scanner.halt.set()
            for name in fds.names():  # only descriptors no thread has claimed; each taken exactly once
                try:
                    close_fd(name)
                    closed_by_cleanup.append(name)
                except OSError as e:
                    cleanup_errors.append({"fd": name, "error": repr(e)})
                    events.append({"at": now(), "event": "fd close failed", "fd": name, "error": repr(e)})
    rec["fds_closed_by_cleanup"] = closed_by_cleanup
    rec["fd_cleanup_errors"] = cleanup_errors
    rec["fd_rollback_close_errors"] = rollback
    rec["fds_left_after_cleanup"] = fds.names()
    if scanner.is_alive():
        scanner.join(3 * (HELPER_DEADLINE + HELPER_TERM_WAIT) + 2)
    for name, (t, res) in threads.items():  # a thread whose start() never ran is reported, not joined
        if t.ident is not None and t.is_alive():
            t.join(5.0 if S["grace_exceeded"] else JOIN_SECONDS)
        res["thread_started"] = t.ident is not None
        res["thread_finished"] = t.ident is not None and not t.is_alive()
    # latched state read after every join: stop, scanner (failure and exclusion), threads
    rec["lane_scanner"] = {"started": S["scan_started"] is not None, "scans": scanner.scans,
                           "failures": scanner.failures, "failed": scanner.failure(),
                           "exclusion": scanner.exclusion(), "alive_after_join": scanner.is_alive()}
    rec["exclusion_latched_in_flight"] = S["exclusion_seen"]
    rec["threads"] = {name: dict(res) for name, (_t, res) in threads.items()}
    rec["threads_started"] = sorted(n for n, (_t, r) in threads.items() if r["thread_started"])
    rec["threads_unfinished"] = sorted(n for n, (_t, r) in threads.items() if not r["thread_finished"])
    rec["stop_latched_during_pipeline"] = stop.get("signal")
    rec["helper_survivors"] = list(HELPER_SURVIVORS)
    rec["children"] = done
    rec["children_reaped_flags"] = dict(reaped)
    rec["children_spawned"] = sorted(n for n in CHILD_NAMES if procs[n] is not None)
    rec["children_alive"] = sorted(n for n in CHILD_NAMES if live(n))
    rec["sigterm_sent"] = sigterm_sent
    rec["safety_stop_reason"] = S["reason"]
    rec["sigterm_grace_exceeded"] = S["grace_exceeded"]
    rec["events"] = events
    rec["finished_at"] = now()
    rec["pipeline_seconds"] = round(time.monotonic() - t0, 3)
    rec["peak_pipeline_aggregate_rss_bytes"] = S["peak_desk"]
    rec["peak_driver_rss_bytes"] = S["peak_driver"]
    rec["peak_child_rss_bytes"] = dict(S["peak_child"])
    rec["peak_lane_other_rss_bytes"] = S["peak_other"]
    rec["peak_lane_total_rss_bytes"] = S["peak_lane_total"]
    rec["peak_lane_reserved_rss_bytes"] = S["peak_lane_reserved"]
    rec["max_lane_other_busy_in_flight"] = S["max_other_busy"]
    rec["min_free_bytes_in_flight"] = S["min_free"]
    kb = read_bytes(klog)
    rec["kissat_log_sha256"], rec["kissat_log_bytes"] = sha_bytes(kb), len(kb)
    rec["solver_status_lines"] = status_lines(kb)
    rec["solver_status_lines_raw"] = [ln.decode("utf-8", "backslashreplace") for ln in kb.split(b"\n")
                                      if ln.replace(b"\r", b"").startswith(b"s")][:LIST_CAP]
    if len(kb) <= 8192:
        rec["kissat_log_text"] = kb.decode("ascii", "replace")
    if os.path.lexists(dlog):
        db = read_bytes(dlog)
        rec["drat_filtered_log_on_disk"] = {"sha256": sha_bytes(db), "bytes": len(db)}
    return rec


def status_lines(b):
    """Status lines of a native log: lines starting with 's' after removing only CR characters."""
    return [ln.decode("ascii", "replace") for ln in b.replace(b"\r", b"").split(b"\n") if ln.startswith(b"s")]


def feed_ok(w, n, e):
    """A measured CNF feed: no write or close error, thread finished, exactly n bytes written, sha256 == e."""
    return (w.get("ok") is True and "error" not in w and "close_error" not in w and w.get("thread_finished") is True
            and w.get("written") == n and w.get("sha256") == e)


# --- acceptance
def _th(rec, name):
    return (rec.get("threads") or {}).get(name) or {}


def criteria(rec, it):
    """Every PASS conjunct, from the pipeline record and the pre-evaluation check. -> {name: bool} over CRITERIA."""
    ch = rec.get("children") or {}
    s, c = ch.get("solver") or {}, ch.get("checker") or {}
    sw, cw, co, fe, fi = (_th(rec, k) for k in ("solver_feed", "checker_feed", "collector", "feeder", "filter"))
    pe = rec.get("pre_evaluation_check") or {}
    ls = rec.get("lane_scanner") or {}
    pb = rec.get("proof_buffer") or {}
    disk = rec.get("drat_filtered_log_on_disk") or {}
    R, D = co.get("collected_bytes"), fe.get("fed_bytes")
    thread_close_errors = [k for k, r in (("solver_feed", sw), ("checker_feed", cw), ("collector", co),
                                          ("feeder", fe)) if "close_error" in r] + (["filter"] if "close_errors" in fi
                                                                                    else [])
    crit = {
        "formula_identity_bound": (rec.get("pre_launch_identity") or {}).get("ok") is True,
        "identity_rehashed_before_solver_spawn": (rec.get("identity_solver") or {}).get("ok") is True,
        "identity_rehashed_before_checker_spawn": (rec.get("identity_checker") or {}).get("ok") is True,
        "solver_feed_measured_complete": feed_ok(sw, it["expected_solver_feed_bytes"],
                                                 it["expected_solver_feed_sha256"]),
        "checker_feed_measured_complete": feed_ok(cw, it["expected_checker_feed_bytes"],
                                                  it["expected_checker_feed_sha256"]),
        "solver_self_exit_20": s.get("exited") is True and s.get("exit_code") == 20 and s.get("sigterm_sent") is False,
        "solver_status_exact_unsat": rec.get("solver_status_lines") == ["s UNSATISFIABLE"],
        "collector_eof_clean": (co.get("ok") is True and co.get("fifo_eof_seen") is True
                                and co.get("thread_finished") is True
                                and not any(k in co for k in ("read_error", "collector_exception", "close_error"))),
        "proof_positive": type(R) is int and R > 0,
        "proof_buffer_digest_agrees": (type(R) is int and pb.get("bytes") == R
                                       and pb.get("sha256") == co.get("collected_sha256")),
        "feeder_plain_complete": (fe.get("ok") is True and fe.get("mode") == "plain"
                                  and fe.get("thread_finished") is True and fe.get("undelivered_bytes") == 0
                                  and "suffix_delivered_bytes" not in fe and "altered_offset" not in fe
                                  and not any(k in fe for k in ("delivery_error", "feeder_exception", "close_error"))),
        "proof_fed_equals_collected": (type(R) is int and R > 0 and D == R
                                       and fe.get("fed_sha256") == co.get("collected_sha256") == pb.get("sha256")),
        "checker_self_exit_0": c.get("exited") is True and c.get("exit_code") == 0 and c.get("sigterm_sent") is False,
        "checker_status_exact_verified": (fi.get("status_lines") == ["s VERIFIED"]
                                          and fi.get("status_line_count") == 1),
        "checker_no_not_verified": fi.get("eof_seen") is True and fi.get("not_verified_lines") == 0,
        "checker_no_timeout": (fi.get("eof_seen") is True and fi.get("timeout_lines") == 0
                               and "s TIMEOUT" not in (fi.get("status_lines") or [])),
        "checker_no_fatal_diagnostic": fi.get("eof_seen") is True and fi.get("error_line_count") == 0,
        "checker_no_early_eof_or_less_than_expected": (fi.get("eof_seen") is True and fi.get("early_eof_lines") == 0
                                                       and fi.get("less_than_expected_lines") == 0),
        "checker_header_counts_match": (it.get("expected_checker_header_counts") is not None
                                        and fi.get("header_count_lines") == 1
                                        and fi.get("header_counts") == [it["expected_checker_header_counts"]]),
        "checker_consumed_proof_bytes_equal_fed": (type(D) is int and fi.get("finished_lines") == 1
                                                   and fi.get("proof_bytes_parsed") == [D]),
        "checker_stream_filter_clean": (fi.get("ok") is True and fi.get("eof_seen") is True
                                        and fi.get("thread_finished") is True
                                        and not any(k in fi for k in ("read_error", "log_write_error",
                                                                      "filter_exception", "close_errors"))
                                        and disk.get("sha256") == fi.get("kept_sha256")
                                        and disk.get("bytes") == fi.get("kept_bytes")),
        "no_safety_stop": (rec.get("safety_stop_reason") is None and rec.get("sigterm_grace_exceeded") is False
                           and not any(k in rec for k in ("exception", "solver_spawn_error", "checker_spawn_error",
                                                          "stage2_skipped"))),
        "no_driver_signal_latched": (pe.get("checked") is True and pe.get("stop_signal") is None
                                     and "stop_latched_during_pipeline" in rec
                                     and rec["stop_latched_during_pipeline"] is None),
        "no_exclusion_breach": ("exclusion" in ls and ls["exclusion"] is None and pe.get("checked") is True
                                and pe.get("scanner_exclusion") is None
                                and "exclusion_latched_in_flight" in rec
                                and rec["exclusion_latched_in_flight"] is None),
        "lane_scanner_clean": (ls.get("started") is True and ls.get("failures") == 0 and ls.get("failed") is None
                               and ls.get("alive_after_join") is False and pe.get("checked") is True
                               and pe.get("scanner_failed") is None),
        "all_threads_finished": (rec.get("threads_started") == sorted(THREAD_NAMES)
                                 and rec.get("threads_unfinished") == []),
        "all_fds_settled": (rec.get("fds_left_after_cleanup") == [] and rec.get("fds_closed_by_cleanup") == []
                            and rec.get("fd_cleanup_errors") == [] and rec.get("fd_rollback_close_errors") == []
                            and not thread_close_errors),
        "children_reaped": (sorted(ch) == ["checker", "solver"] and rec.get("children_alive") == []
                            and rec.get("children_reaped_flags") == {"solver": True, "checker": True}),
        "no_helper_survivor": (pe.get("checked") is True and not pe.get("helper_survivors")
                               and "helper_survivors" in rec and not rec["helper_survivors"]),
    }
    return {k: bool(crit[k]) for k in CRITERIA}


def control_observation(name, rec, it):
    """The preregistered observation of one control (the intended mechanism actually happened)."""
    ch = rec.get("children") or {}
    c = ch.get("checker") or {}
    cw, co, fe, fi = (_th(rec, k) for k in ("checker_feed", "collector", "feeder", "filter"))
    R, D = co.get("collected_bytes"), fe.get("fed_bytes")
    clean_feeder = (fe.get("thread_finished") is True
                    and not any(k in fe for k in ("delivery_error", "feeder_exception", "close_error")))
    differs = type(R) is int and R > 0 and fe.get("fed_sha256") != co.get("collected_sha256")
    if name == "unsat":
        return fi.get("dup_formula_phase") == 1 and fi.get("dup_lines") == 1 + fi.get("dup_proof_phase", -1)
    if name == "sat-checker":
        return (c.get("exited") is True and c.get("exit_code") == 1 and c.get("sigterm_sent") is False
                and fi.get("status_lines") == ["s NOT VERIFIED"] and fi.get("status_line_count") == 1
                and fi.get("not_verified_lines") == 1 and fi.get("header_counts") == [[3, 7]])
    if name == "short-cnf":
        lim = it["checker_feed_limit_bytes"]
        return (cw.get("ok") is True and "error" not in cw and "close_error" not in cw
                and cw.get("thread_finished") is True and lim == it["expected_checker_feed_bytes"] - SHORT_BYTES
                and cw.get("written") == lim and cw.get("sha256") == sha_bytes(CONTROLS[name]["checker"][:lim])
                and fi.get("status_lines") == ["s VERIFIED"])
    if name == "truncate":
        return (fe.get("mode") == "truncate" and clean_feeder and differs and R > TRUNCATE_BYTES
                and fe.get("undelivered_bytes") == TRUNCATE_BYTES and D == R - TRUNCATE_BYTES
                and fi.get("finished_lines") == 1 and fi.get("proof_bytes_parsed") in ([D], [D + 1]))
    if name == "suffix":
        return (fe.get("mode") == "suffix" and clean_feeder and differs and fe.get("undelivered_bytes") == 0
                and fe.get("suffix_delivered_bytes") == len(SUFFIX) and D == R + len(SUFFIX)
                and fi.get("proof_bytes_parsed") == [D])
    if name == "digest-alter":
        return (fe.get("mode") == "alter" and clean_feeder and differs and fe.get("undelivered_bytes") == 0
                and type(fe.get("altered_offset")) is int
                and fe.get("altered_offset") == (rec.get("proof_buffer") or {}).get("alter_offset")
                and D == R and fi.get("proof_bytes_parsed") == [D])
    if name == "early-close":
        return (fe.get("mode") == "hold" and str(fe.get("delivery_error", "")).startswith("EPIPE") and D == 0
                and fe.get("hold_released_by_event") is True and fe.get("thread_finished") is True
                and "feeder_exception" not in fe and "close_error" not in fe and fe.get("undelivered_bytes") == R
                and c.get("exited") is True and c.get("exit_code") == 0 and c.get("sigterm_sent") is False
                and fi.get("header_error_line_exact") is True and fi.get("status_line_count") == 0
                and fi.get("error_line_count") == 1 and fi.get("finished_lines") == 0
                and fi.get("header_count_lines") == 0)
    die("unknown control " + str(name))


def solver_reported_sat(rec):
    s = (rec.get("children") or {}).get("solver") or {}
    return s.get("exit_code") == 10 or "s SATISFIABLE" in (rec.get("solver_status_lines") or [])


def control_vetoes(name, rec):
    """(F1) Independent of must_fail/may_fail: kissat or drat-trim not exiting normally by itself (a signal, a driver
    SIGTERM), a drat-trim TIMEOUT, an outcome (exit code, exact status lines) outside the preregistered list, a
    fatal-class diagnostic not allowed with that outcome, or a truncated status/diagnostic list. -> vetoes."""
    spec = CONTROLS[name]
    ch = rec.get("children") or {}
    s, c = ch.get("solver") or {}, ch.get("checker") or {}
    fi = _th(rec, "filter")
    vetoes = []
    if not (s.get("exited") is True and s.get("signaled") is False and s.get("sigterm_sent") is False):
        vetoes.append("kissat did not exit normally by itself")
    if not (c.get("exited") is True and c.get("signaled") is False and c.get("sigterm_sent") is False):
        vetoes.append("drat-trim did not exit normally by itself")
    status, errors = fi.get("status_lines"), fi.get("error_lines")
    if fi.get("timeout_lines") != 0 or "s TIMEOUT" in (status or []):
        vetoes.append("drat-trim TIMEOUT")
    if (not isinstance(status, list) or fi.get("status_line_count") != len(status)
            or not isinstance(errors, list) or fi.get("error_line_count") != len(errors)):
        vetoes.append("status or diagnostic lines incomplete")
        return vetoes
    match = [o for o in spec["outcomes"] if o["exit_code"] == c.get("exit_code") and o["status_lines"] == status]
    if not match:
        vetoes.append("drat-trim outcome (exit %r, status %r) is not preregistered" % (c.get("exit_code"), status))
    else:
        extra = [e for e in errors if e not in match[0]["allowed_diagnostics"]]
        if extra:
            vetoes.append("fatal-class diagnostic not preregistered for this outcome: %r" % extra[:3])
    return vetoes


def evaluate(rec, it):
    """gb: PASS iff every criterion holds, else UNKNOWN with reasons. control: its preregistered verdict iff no veto
    (control_vetoes), exactly the intended criteria fail (must_fail all False, every criterion outside
    must_fail/may_fail True) and its observation holds; anything else is INVALID_CONTROL."""
    crit = criteria(rec, it)
    failed = [k for k in CRITERIA if not crit[k]]
    if it["kind"] == "gb":
        if not failed:
            return "PASS", [], crit
        notes = []
        if solver_reported_sat(rec):
            notes.append("kissat reported SATISFIABLE (exit %s); its full output stays in the kissat log; the desk "
                         "launches nothing more" % ((rec.get("children") or {}).get("solver") or {}).get("exit_code"))
        if _th(rec, "filter").get("not_verified_lines"):
            notes.append("drat-trim printed s NOT VERIFIED")
        if _th(rec, "filter").get("timeout_lines"):
            notes.append("drat-trim printed s TIMEOUT")
        if rec.get("safety_stop_reason"):
            notes.append("safety stop: " + rec["safety_stop_reason"])
        if rec.get("stage2_skipped"):
            notes.append("stage 2 not started: " + ", ".join(rec["stage2_skipped"]))
        return "UNKNOWN", notes + failed, crit
    spec = CONTROLS[it["name"]]
    must, may = set(spec["must_fail"]), set(spec["may_fail"])
    unexpected = [k for k in failed if k not in must and k not in may]
    absent = [k for k in spec["must_fail"] if crit[k]]
    vetoes = control_vetoes(it["name"], rec)
    seen = control_observation(it["name"], rec, it)
    if vetoes or unexpected or absent or not seen:
        return ("INVALID_CONTROL", ["veto: " + v for v in vetoes] + ["unexpected failure: " + k for k in unexpected]
                + ["intended failure absent: " + k for k in absent]
                + ([] if seen else ["preregistered control observation missing"]), crit)
    return spec["verdict"], failed, crit


def downgrade(verdict, reasons, it, why):
    """(F4) A driver signal latched after the pre-evaluation check never leaves a qualifying verdict."""
    if it["kind"] == "gb":
        return ("UNKNOWN" if verdict == "PASS" else verdict), reasons + [why]
    return "INVALID_CONTROL", reasons + [why]


# --- identity checks (after admission, immediately before each spawn) and subcommands
def identity_check(stage, parts, it, pre, pre_path, pre_sha, go, script_sha, stop):
    """Re-hash this script, the interpreter, kissat, drat-trim, GBBINDING, the binder, the PRE-EXEC and the GO
    record against the pins and the run's records; parts: the CNF parts of the stage's feed (None at post-gate); gb
    items: the seven control receipts are re-validated against the PRE-EXEC admission record. A latched SIGTERM, a
    helper survivor or the 17:29 cutoff also refuses. -> record; ok False forbids the spawn."""
    t0 = time.monotonic()
    py = os.path.realpath(sys.executable)
    pyrec = pre.get("python") or {}
    want = {"script_sha256": script_sha, "python_sha256": pyrec.get("sha256"), "kissat_sha256": KISSAT_SHA,
            "drat_trim_sha256": DRAT_SHA, "gbbinding_sha256": GBBINDING_SHA, "binder_sha256": BINDER_SHA,
            "pre_exec_sha256": pre_sha, "go_sha256": go["sha256"]}
    paths = {"script_sha256": SCRIPT, "python_sha256": py, "kissat_sha256": KISSAT, "drat_trim_sha256": DRAT,
             "gbbinding_sha256": GBBINDING, "binder_sha256": BINDER, "pre_exec_sha256": pre_path,
             "go_sha256": go["path"]}
    got, problems = {}, []
    for k, path in paths.items():
        try:
            got[k] = sha_file(path)
        except OSError as e:
            got[k] = None
            problems.append("%s unreadable: %r" % (path, e))
    problems += ["%s %s != expected %s" % (k, got[k], want[k]) for k in want
                 if got[k] is not None and got[k] != want[k]]
    if pyrec.get("realpath") != py:
        problems.append("python realpath %s != PRE-EXEC %s" % (py, pyrec.get("realpath")))
    out = {"stage": stage, "at": now(), "python_realpath": py, "hashed": got, "expected": want}
    if parts is not None:
        side = "solver" if stage == "solver" else "checker"
        exp = (it["expected_%s_feed_sha256" % side], it["expected_%s_feed_bytes" % side])
        h, n = sha_parts(parts)
        out["cnf_rehash"] = {"sha256": h, "bytes": n, "expected_sha256": exp[0], "expected_bytes": exp[1]}
        if (h, n) != exp:
            problems.append("CNF parts re-hash %s/%d != expected %s/%d" % (h, n, exp[0], exp[1]))
    if it["kind"] == "gb":
        adm, probs = validate_controls(script_sha)
        now_ids = [(a["label"], a["receipt_sha256"], a["commit_sha256"], a["completion_sha256"]) for a in adm]
        pre_ids = [(a.get("label"), a.get("receipt_sha256"), a.get("commit_sha256"), a.get("completion_sha256"))
                   for a in (pre.get("admission_controls") or [])]
        out["controls_revalidated"] = [{"label": a, "receipt_sha256": b, "commit_sha256": c, "completion_sha256": d}
                                       for a, b, c, d in now_ids]
        out["controls_equal_pre_exec"] = not probs and now_ids == pre_ids and len(now_ids) == len(CONTROLS)
        problems.extend(probs)
        if not out["controls_equal_pre_exec"]:
            problems.append("control receipts differ from the PRE-EXEC admission record")
    if stop.get("signal"):
        problems.append("driver received %s (latched)" % stop["signal"])
    if HELPER_SURVIVORS:
        problems.append("helper survivor(s) recorded")
    if time.time() >= NO_LAUNCH_AT:
        problems.append("launch cutoff 2026-10-18 17:29:00 PDT reached")
    out.update(ok=not problems, problems=problems, seconds=round(time.monotonic() - t0, 3))
    return out


def control_identity(it, s_parts, c_parts):
    hs, ns = sha_parts(s_parts)
    hc, nc = sha_parts(c_parts)
    problems = []
    if (hs, ns) != (it["expected_solver_feed_sha256"], it["expected_solver_feed_bytes"]):
        problems.append("solver control CNF differs from the PRE-EXEC")
    if (hc, nc) != (it["expected_checker_feed_sha256"], it["expected_checker_feed_bytes"]):
        problems.append("checker control CNF differs from the PRE-EXEC")
    if header_counts(c_parts[0]) != it["expected_checker_header_counts"]:
        problems.append("checker control header counts differ")
    return {"ok": not problems, "problems": problems, "solver_feed": {"sha256": hs, "bytes": ns},
            "checker_feed": {"sha256": hc, "bytes": nc}, "at": now()}


def artifact_paths(label):
    return [os.path.join(DESK, "receipts", label + ".json"), os.path.join(DESK, "receipts", label + ".commit.json"),
            os.path.join(DESK, "receipts", label + ".commit.json.prepare"),
            os.path.join(DESK, "receipts", label + ".complete.json"),
            os.path.join(DESK, "receipts", label + ".complete.json.prepare"),
            os.path.join(DESK, "receipts", label + ".cancelled.json"),
            os.path.join(DESK, "fifo", label + ".kissat.fifo"),
            os.path.join(DESK, "logs", label + ".kissat.log"), os.path.join(DESK, "logs", label + ".drat.filtered.log"),
            os.path.join(TMP, label)]


def check_env():
    if os.environ.get("TMPDIR") != TMP + "/":
        die("TMPDIR must be %s/" % TMP)
    if not (sys.flags.isolated and sys.dont_write_bytecode) or sys.version_info[:2] != (3, 14):
        die("run with /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B (the binder's interpreter)")
    os.chdir(TMP)


def cmd_preexec(argv):
    check_env()
    if len(argv) < 2:
        die("preexec OUT ITEM...  (ITEM = control:NAME | gb:ID:aN)")
    out = os.path.abspath(argv[0])
    if not out.startswith(DESK + "/") or os.path.lexists(out):
        die("pre-exec path must be new and inside the desk")
    started = now()
    pins = verify_pins()
    binaries = check_binaries()
    binding = load_binding()
    items = []
    for spec in argv[1:]:
        kind, _, rest = spec.partition(":")
        try:
            if kind == "control":
                items.append(control_item(rest))
            elif kind == "gb":
                gid, _, attempt = rest.partition(":")
                items.append(gb_item(gid, attempt, binding))
            else:
                raise ValueError("bad item %r (control:NAME or gb:ID:aN only)" % spec)
        except ValueError as e:
            die(str(e))
    problems = validate_items(items, binding)
    if problems:
        die("PRE-EXEC items refused: " + "; ".join(problems))
    for it in items:
        taken = [p for p in artifact_paths(it["label"]) if os.path.lexists(p)]
        if taken:
            die("artifacts of %s already exist (a new attempt tag is required): %s" % (it["label"], taken))
    admission = None
    if items[0]["kind"] == "gb":
        admission, probs = validate_controls(sha_file(SCRIPT))
        if probs:
            die("gb admission refused: " + "; ".join(probs))
    fb = free_bytes()
    busy, other, scan, scan_err = gate_scan()
    if HELPER_SURVIVORS:
        die("helper survivor(s) recorded during the fresh check: %r" % HELPER_SURVIVORS)
    py = os.path.realpath(sys.executable)
    pre = {"schema": PREEXEC_SCHEMA, "at": now(), "started_at": started, "desk": DESK, "scope": SCOPE,
           "script": {"path": SCRIPT_REL, "sha256": sha_file(SCRIPT), "bytes": os.path.getsize(SCRIPT)},
           "python": {"executable": sys.executable, "realpath": py, "sha256": sha_file(py),
                      "version": sys.version.split()[0], "flags": "-I -B"},
           "binaries": binaries, "pins_verified": pins,
           "gbbinding": {"path": GBBINDING, "sha256": binding["sha256"], "gb_base": binding["gb_base"]},
           "run_kind": "controls" if items[0]["kind"] == "control" else "science",
           "items": items, "admission_controls": admission, "acceptance": ACCEPTANCE, "gate": GATE_RULE,
           "in_flight_stops": STOPS, "transport": TRANSPORT, "sequencing": SEQUENCING, "parent_go": GO_RULE,
           "limits": {"kissat_seconds": KISSAT_SECONDS, "drat_trim_seconds": DRAT_SECONDS,
                      "stage_margin_seconds": STAGE_MARGIN, "launch_floor_bytes": LAUNCH_FLOOR,
                      "floor_bytes": FLOOR, "lane_rss_limit_bytes": LANE_RSS_LIMIT, "lane_busy_cap": LANE_BUSY_CAP,
                      "mine": MINE, "gb_pipeline_cap_bytes": GB_PIPELINE_CAP, "gb_reservation_bytes": GB_RESERVATION,
                      "control_reservation_bytes": CONTROL_RESERVATION, "control_cap_bytes": CONTROL_CAP,
                      "wait_poll_seconds": WAIT_POLL, "wait_budget_seconds": WAIT_BUDGET,
                      "gate_consecutive_passes": GATE_STREAK, "sigterm_grace_seconds": SIGTERM_GRACE,
                      "join_seconds": JOIN_SECONDS, "no_launch_at": "2026-10-18T17:29:00-07:00",
                      "native_stop_at": "2026-10-18T17:57:00-07:00", "monitor": MONITOR,
                      "stable_free_min_bytes": STABLE_FREE_MIN, "stable_window_seconds": STABLE_WINDOW,
                      "stable_drop_allowance": "max(%d, (free_last - %d) // %d)"
                                               % (STABLE_MIN_DROP_CAP, STABLE_RUNWAY_BASE, STABLE_RUNWAY_DIV),
                      "stable_max_age_seconds": STABLE_MAX_AGE, "stable_min_samples": STABLE_MIN_SAMPLES,
                      "stable_min_span_seconds": STABLE_MIN_SPAN},
           "fresh_check": {"free_bytes": fb, "lane_other_busy": busy, "lane_other_rss_bytes": other,
                           "lane_scan_error": scan_err, "lane_scan": [compact(c) for c in (scan or [])],
                           "exclusions": exclusions(scan) if scan is not None else None,
                           "monitor_stability": monitor_stability()[1]}}
    digest = write_json_x(out, pre)
    print("PRE-EXEC %s sha256 %s" % (out, digest))
    for it in items:
        print(it["item"], it["label"], it["expected_solver_feed_sha256"][:16], it["expected_checker_feed_bytes"])


def cmd_run(argv):
    check_env()
    if len(argv) != 2:
        die("run PREEXEC GO")
    pre_path = os.path.abspath(argv[0])
    if not pre_path.startswith(DESK + "/"):
        die("the PRE-EXEC must lie in this desk")
    pre_raw = read_bytes(pre_path)
    pre, pre_sha = json.loads(pre_raw), sha_bytes(pre_raw)
    script_sha = sha_file(SCRIPT)
    if (pre.get("script") or {}).get("sha256") != script_sha:
        die("script sha256 differs from the pre-exec pin")
    py = os.path.realpath(sys.executable)
    if (pre.get("python") or {}).get("realpath") != py or pre["python"].get("sha256") != sha_file(py):
        die("python interpreter differs from the pre-exec record")
    binding = load_binding()
    problems = validate_items(pre.get("items"), binding)  # before any regeneration, log or launch
    if problems:
        die("PRE-EXEC items refused: " + "; ".join(problems))
    items = pre["items"]
    go, problems = validate_go(argv[1], pre_sha, script_sha, items)
    if problems:
        die("parent GO record refused: " + "; ".join(problems))
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
    signal.signal(signal.SIGINT, on_term)  # (F4) latched too: no asynchronous KeyboardInterrupt inside the driver
    summary = {"schema": RUN_SCHEMA, "run_tag": runtag, "started_at": now(), "driver_pid": os.getpid(),
               "pre_exec": {"path": rel(pre_path), "sha256": pre_sha},
               "go": {"path": go["path"], "sha256": go["sha256"], "scope": go["scope"]}, "script_sha256": script_sha,
               "python": {"realpath": py, "sha256": pre["python"]["sha256"]}, "driver_log": rel(log_path),
               "items": [], "events": [], "stopped_reason": None}
    log("run %s start; pre-exec %s sha256 %s; GO %s sha256 %s; driver pid %d"
        % (runtag, rel(pre_path), pre_sha, go["path"], go["sha256"], os.getpid()))
    summary["pins_verified"] = pins = verify_pins()
    remaining = list(items)
    if items[0]["kind"] == "gb":
        adm, probs = validate_controls(script_sha)
        same = ([(a["label"], a["receipt_sha256"], a["commit_sha256"], a["completion_sha256"]) for a in adm]
                == [(a.get("label"), a.get("receipt_sha256"), a.get("commit_sha256"), a.get("completion_sha256"))
                    for a in (pre.get("admission_controls") or [])])
        if probs or not same:
            summary["stopped_reason"] = ("gb admission re-validation failed: %s"
                                         % ("; ".join(probs) or "control receipts differ from the PRE-EXEC record"))
            log("STOPPED: " + summary["stopped_reason"])
            remaining = []
    budget = {"used": 0.0}
    while remaining:
        it = remaining.pop(0)
        label = it["label"]
        rpath = os.path.join(DESK, "receipts", label + ".json")
        entry = {"item": it["item"], "label": label}
        summary["items"].append(entry)
        if os.path.lexists(rpath):
            if it["kind"] == "control":  # never skip a control without checking its receipt
                mine = [x for x in validate_controls(script_sha)[1] if x.startswith(label + ":")]
                if mine:
                    entry.update({"status": "STOPPED",
                                  "reason": "existing control receipt invalid: " + "; ".join(mine)})
                    summary["stopped_reason"] = entry["reason"]
                    log("STOPPED %s: %s" % (label, entry["reason"]))
                    break
                entry.update({"status": "SKIPPED_VALIDATED", "reason": "receipt exists and validates for this script"})
                log("skip %s: %s" % (label, entry["reason"]))
                continue
            entry.update({"status": "STOPPED", "reason": "receipt exists; a new attempt needs a new attempt tag and a "
                                                         "new parent GO"})
            summary["stopped_reason"] = entry["reason"]
            log("STOPPED %s: %s" % (label, entry["reason"]))
            break
        taken = [p for p in artifact_paths(label) if os.path.lexists(p)]
        if taken:
            entry.update({"status": "STOPPED", "reason": "artifacts of an earlier attempt exist: %s" % taken})
            summary["stopped_reason"] = entry["reason"]
            log("STOPPED %s: %s" % (label, entry["reason"]))
            break
        bins = check_binaries()
        if it["kind"] == "control":
            s_parts, c_parts = [CONTROLS[it["name"]]["solver"]], [CONTROLS[it["name"]]["checker"]]
            pre_launch = control_identity(it, s_parts, c_parts)
        else:
            try:
                s_parts, pre_launch = regenerate(it, binding, log)
            except BaseException as e:  # the binder's Stop/Abort or any error: nothing was launched
                entry.update({"status": "STOPPED", "reason": "in-memory regeneration failed: %s: %s"
                              % (type(e).__name__, e), "traceback": traceback.format_exc()[-4000:]})
                summary["stopped_reason"] = entry["reason"]
                log("STOPPED %s: %s" % (label, entry["reason"]))
                break
            c_parts = s_parts
        entry["pre_launch_identity_ok"] = pre_launch["ok"]
        if not pre_launch["ok"]:
            entry.update({"status": "STOPPED", "pre_launch_identity": pre_launch,
                          "reason": "regenerated bytes differ from the bound identity: "
                                    + "; ".join(pre_launch["problems"])})
            summary["stopped_reason"] = entry["reason"]
            log("STOPPED %s: %s" % (label, entry["reason"]))
            break
        summary["driver_rss_before_gate_bytes"] = (taskinfo(os.getpid()) or (None,))[0]
        log("gate %s: reservation %d cap %d stability rule %s"
            % (label, it["reservation_bytes"], it["desk_cap_bytes"], it["stability_rule"]))
        g = gate(label, it["reservation_bytes"], budget, log, stop, it["stability_rule"])
        if not g["launch"]:
            summary["events"].append({"at": now(), "event": "deferred" if g.get("deferred") else "stopped",
                                      "item": it["item"], "wait_used_total_seconds": round(budget["used"], 1),
                                      "last_sample": g["samples"][-1] if g["samples"] else None})
            entry.update({"status": "DEFERRED" if g.get("deferred") else "STOPPED", "gate": g})
            summary["stopped_reason"] = ("total gate wait budget of 6 h exhausted at %s" % label
                                         if g.get("deferred") else g.get("stopped"))
            log("%s %s" % (entry["status"], label))
            break
        pg = identity_check("post-gate", None, it, pre, pre_path, pre_sha, go, script_sha, stop)
        if not pg["ok"]:
            entry.update({"status": "STOPPED", "gate": g, "post_gate_identity": pg,
                          "reason": "post-gate identity check refused the launch: " + "; ".join(pg["problems"])})
            summary["stopped_reason"] = entry["reason"]
            log("STOPPED %s: %s" % (label, entry["reason"]))
            break

        def ident(stage, parts, it=it):
            return identity_check(stage, parts, it, pre, pre_path, pre_sha, go, script_sha, stop)
        try:
            rec = pipeline(label, it, s_parts, c_parts, ident, log, stop)
        except BaseException as e:  # pipeline() reaps its own children; this records what escaped its scope
            rec = {"label": label, "exception": "%s: %s" % (type(e).__name__, e),
                   "exception_traceback": traceback.format_exc()[-4000:],
                   "safety_stop_reason": "exception outside the pipeline cleanup scope: %s: %s" % (type(e).__name__, e),
                   "sigterm_grace_exceeded": False, "children": {}, "threads": {}, "events": []}
            log("EXCEPTION at %s: %s" % (label, rec["exception"]))
        s_parts = c_parts = None  # the regenerated CNF is released after the item
        rec["pre_launch_identity"] = pre_launch
        # the latched stop, scanner failure and survivors are checked again immediately before evaluation
        rec["pre_evaluation_check"] = {"checked": True, "at": now(), "stop_signal": stop.get("signal"),
                                       "scanner_failed": (rec.get("lane_scanner") or {}).get("failed"),
                                       "scanner_exclusion": (rec.get("lane_scanner") or {}).get("exclusion"),
                                       "helper_survivors": list(HELPER_SURVIVORS)}
        verdict, reasons, crit = evaluate(rec, it)
        late = stop.get("signal")  # (F4) a signal latched during evaluation never leaves a qualifying verdict
        if late is not None:
            verdict, reasons = downgrade(verdict, reasons, it, "driver signal %s latched during evaluation" % late)
        receipt = {"schema": RECEIPT_SCHEMA, "label": label, "kind": it["kind"], "id": it.get("id"),
                   "name": it.get("name"), "attempt": it.get("attempt"),
                   "scope": SCOPE if it["kind"] == "gb" else it["purpose"], "desk": DESK,
                   "script": {"path": SCRIPT_REL, "sha256": script_sha}, "python": pre["python"],
                   "pre_exec": {"path": rel(pre_path), "sha256": pre_sha},
                   "go": {"path": go["path"], "sha256": go["sha256"], "scope": go["scope"]}, "run_tag": runtag,
                   "binaries": bins, "pins_verified": pins, "item": it, "gate": g, "post_gate_identity": pg,
                   "pipeline": rec, "criteria": crit, "verdict": verdict, "reasons": reasons,
                   "solver_reported_sat": solver_reported_sat(rec),
                   "stop_latched": rec["pre_evaluation_check"]["stop_signal"],  # the value evaluate() saw
                   "stop_latched_after_evaluation": late,  # sampled after evaluate(); a signal here downgraded it
                   "qualification": ("this receipt qualifies only with receipts/%s.commit.json (qualified decision), "
                                     "receipts/%s.complete.json bound to it, no receipts/%s.cancelled.json and a clean "
                                     "durable run summary (qualification_problems)" % (label, label, label)),
                   "written_at": now()}
        durability_error = None
        try:  # (F4') the receipt is synced (file and directory) before any qualification decision
            rsha = write_json_durable(rpath, receipt)
        except Exception as e:  # a receipt that is not durable can never be qualified
            durability_error = "%s: %s" % (type(e).__name__, e)
            try:
                rsha = sha_file(rpath)
            except OSError:
                rsha = None
        want = "PASS" if it["kind"] == "gb" else it["preregistered_verdict"]
        base = {"schema": COMMIT_SCHEMA, "label": label, "receipt": rel(rpath), "receipt_sha256": rsha,
                "verdict": verdict, "qualifying_verdict": want, "receipt_durable": durability_error is None,
                "receipt_durability_error": durability_error,
                "stop_signal_at_pre_evaluation": receipt["stop_latched"], "stop_signal_after_evaluation": late,
                "rule": "qualified iff the receipt's verdict is the qualifying verdict, the receipt is durable, no "
                        "driver signal was latched at the pre-evaluation check, after evaluation or at the "
                        "linearization point, no SIGTERM/SIGINT was pending there, and the driver was the only "
                        "thread; published atomically and durably by publish_commit()"}
        eligible = (verdict == want and durability_error is None and late is None and receipt["stop_latched"] is None)
        stem = os.path.join(DESK, "receipts", label)
        pub = publish_qualification({"commit": stem + ".commit.json", "complete": stem + ".complete.json",
                                     "cancel": stem + ".cancelled.json"}, base, eligible, stop)
        qualified = pub["status"] == "COMPLETE"
        publish_error = "; ".join(pub["errors"]) or None
        entry.update({"status": "RECEIPT", "verdict": verdict, "reasons": reasons, "receipt": rel(rpath),
                      "receipt_sha256": rsha, "commit_sha256": pub["commit_sha256"],
                      "completion_sha256": pub["completion_sha256"], "cancellation_sha256": pub["cancellation_sha256"],
                      "publication_status": pub["status"], "publication_checks": pub["checks"],
                      "cancel_reason": pub["cancel_reason"], "qualified": qualified,
                      "receipt_durability_error": durability_error, "commit_publication_error": publish_error,
                      "pipeline_seconds": rec.get("pipeline_seconds"),
                      "gate_waited_seconds": g["waited_seconds"],
                      "peak_pipeline_aggregate_rss_bytes": rec.get("peak_pipeline_aggregate_rss_bytes"),
                      "safety_stop_reason": rec.get("safety_stop_reason"), "stop_latched": stop.get("signal")})
        for ev in rec.get("events", []):
            summary["events"].append(dict(ev, item=it["item"]))
        log("%s verdict %s reasons %s receipt sha256 %s publication %s"
            % (label, verdict, reasons, rsha, pub["status"]))
        if pub["status"] == "CANCELLED":
            summary["stopped_reason"] = "publication of %s cancelled: %s; desk launches nothing more" % (
                label, pub["cancel_reason"])
            break
        if durability_error or publish_error:
            summary["stopped_reason"] = ("receipt durability / commit publication failed at %s: %s; desk launches "
                                         "nothing more" % (label, durability_error or publish_error))
            break
        if rec.get("sigterm_grace_exceeded"):
            summary["stopped_reason"] = "SIGTERM grace exceeded at %s; a child may still be alive" % label
            break
        if stop.get("signal"):
            summary["stopped_reason"] = "driver received %s (latched; receipt records stop_latched)" % stop["signal"]
            break
        if rec.get("exception"):
            summary["stopped_reason"] = "exception at %s: %s; desk launches nothing more" % (label, rec["exception"])
            break
        if rec.get("checker_spawn_error") or rec.get("solver_spawn_error"):
            summary["stopped_reason"] = ("spawn error at %s: %s; desk launches nothing more"
                                         % (label, rec.get("checker_spawn_error") or rec.get("solver_spawn_error")))
            break
        vetoes = [k for k in ("no_driver_signal_latched", "no_exclusion_breach", "lane_scanner_clean",
                              "all_threads_finished", "all_fds_settled", "children_reaped", "no_helper_survivor")
                  if not crit.get(k)]
        if vetoes:
            summary["stopped_reason"] = "%s at %s; desk launches nothing more" % (", ".join(vetoes), label)
            break
        if it["kind"] == "control" and not qualified:
            summary["stopped_reason"] = "control %s gave %s (expected %s), commit qualified %s" % (
                label, verdict, it["preregistered_verdict"], qualified)
            break
        if solver_reported_sat(rec):
            summary["stopped_reason"] = ("kissat reported SATISFIABLE at %s; its output is kept in %s; desk stopped"
                                         % (label, rec.get("kissat_log")))
            log("SAT REPORTED %s: desk stops" % label)
            break
        if rec.get("safety_stop_reason") is not None:
            summary["stopped_reason"] = ("safety stop at %s: %s; desk launches nothing more"
                                         % (label, rec["safety_stop_reason"]))
            break
    for it in remaining:
        summary["items"].append({"item": it["item"], "label": it["label"], "status": "NOT_ATTEMPTED",
                                 "reason": summary["stopped_reason"]})
    summary["wait_budget_seconds"] = WAIT_BUDGET
    summary["wait_used_seconds"] = round(budget["used"], 1)
    summary["helper_survivors"] = list(HELPER_SURVIVORS)
    summary["finished_at"] = now()
    if stop.get("signal") and summary["stopped_reason"] is None:
        summary["stopped_reason"] = "driver received %s (latched) after the last item" % stop["signal"]
    log("run %s finished; stopped_reason %s" % (runtag, summary["stopped_reason"]))
    logf.close()
    summary["driver_log_sha256_at_close"] = sha_file(log_path)
    spath = os.path.join(DESK, "runs", "run-%s.json" % runtag)
    digest, errors, cancelled = publish_run_summary(spath, summary, stop)  # (F4'') the run's terminal evidence
    print("RUN SUMMARY runs/run-%s.json sha256 %s errors %s run cancelled %s" % (runtag, digest, errors, cancelled))


def cmd_qualification(argv):
    """Read-only: the full admission predicate of one receipt label (no write, no spawn). Prints JSON; exit 0 only if
    the label qualifies."""
    if len(argv) != 1 or not re.fullmatch(r"[A-Za-z0-9.\-]+", argv[0]):
        die("qualification LABEL")
    label = argv[0]
    r = _load_json(os.path.join(DESK, "receipts", label + ".json")) or {}
    item = r.get("item") if isinstance(r, dict) else None
    want = "PASS" if (item or {}).get("kind") == "gb" else (item or {}).get("preregistered_verdict")
    ident, problems = qualification_problems(label, want)
    print(json.dumps({"label": label, "qualifying_verdict": want, "identity": ident, "problems": problems,
                      "qualified": not problems}, indent=1))
    if problems:
        raise SystemExit(2)


def main(argv):
    if len(argv) < 2:
        die(__doc__)
    cmd, rest = argv[1], argv[2:]
    if cmd == "preexec":
        cmd_preexec(rest)
    elif cmd == "run":
        cmd_run(rest)
    elif cmd == "qualification":
        cmd_qualification(rest)
    else:
        die("unknown subcommand " + cmd)


if __name__ == "__main__":
    main(sys.argv)
