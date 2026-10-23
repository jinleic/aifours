#!/usr/bin/env python3
"""PA19 96h P-STREAM runner v4, multiset ms06: code/pilot_stream_drat_ms06_v3.py (ab95e40f...) + B1, the parent
precheck fix (IRC 2026-10-19 ~07:2x) of the unbounded quarantine wait; every v3 fix (N1-N12) is unchanged.
  B1  No unbounded wait anywhere (owner contract resources.stop: SIGTERM + BOUNDED wait only).  Owned.reap_owned
      is finite: after the single identity-verified group SIGTERM (or a refused stop) and at most the grace
      (TERM_WAIT for children, HELPER_TERM_WAIT for helpers; a hard bound from entry covers a stop that could not be
      requested), a survivor is recorded UNSETTLED irreversibly (latch + exclusive receipt with its exact
      identities, a live census and the late-artifact obligations) and the reap returns None; nothing ever waits
      for it again, signals it again or escalates.  settle_all makes one bounded pass (SETTLE_ALL_ATTEMPTS per
      child).  With the latch held nothing new is admitted; the run closes out (bounded) and returns to the parent
      with exit 50.  The summary publishes every UNSETTLED owner and states that the reservation stays held:
      release_refusals releases an UNSETTLED (or summary-less) attempt only with a NEW parent disposition
      (DISPOSITION_SCHEMA) confirming that every listed process ended, re-checked with libproc.  No synthetic
      settlement; an unexpected survivor is a parent blocker, not a code path that waits.
      Inherited notes below that describe waiting without bound for an unreaped owner (v14 r3#1, r4#1, r5#4,
      r6#1-#2; v2 V1/V3; v3 N7 and its residual list) are SUPERSEDED by B1.
PA19 96h P-STREAM runner v3 notes follow.
PA19 96h P-STREAM runner v3, multiset ms06: code/pilot_stream_drat_ms06_v2.py (776daf13...) + focused fixes for the
parent-routed Codex follow-up review (RUN/review/pa19-PSTREAM-v2-source-codex-v1.prompt.stdout.txt 3da83be6..., HOLD,
N1-N12) under the parent runtime-guard HOLD (RUN/review/runtime-guard-admission-HOLD-v1.json 6c1d8440...) and the
parent's N3 instruction (single parent allocator, one-use admission, verified parent release; no second scheduler):
  N1  Stop = class Owned: ONE SIGTERM to the owned process GROUP (KILLPG), only after the retained, unreaped leader is
      re-verified against its start identity (libproc BSD info: pid, pgid == pid, ppid == runner, same start time;
      or exited-unreaped and still listed in its own group).  Unverifiable identity: no signal, latch, UNSETTLED.
  N2  /bin/date Helper under the same rules as a native child: admission (no latch, no cancel, every owned process
      settled, HELPER_ALLOW fits the frozen cutoffs), launch boundary, verified identity, supervised incremental
      capture bounded at HELPER_OUT_CAP, cancel/wall/descendant/RSS trips, verified stop, bounded reap then UNSETTLED
      quarantine, cleanup in a finally, explicit settlement predicate; closeout counts only SETTLED helpers.
  N3  Admission authority = the parent's allocation inside the pinned GO (schema ALLOCATION_SCHEMA): out_dir ==
      OUT_DIR (exclusive creation: one use), reservation_bytes >= this run's reservation, lane_ceiling_bytes and
      busy_slots == the contract values, and released_attempts listing EVERY existing pilot-v1 entry with the
      SHA-256 of its launch record and summary; each release is re-verified (regular bounded files, exact digests,
      known schema, every owned process settled, no quarantine receipt, no reuse of this GO).  A missing, stale,
      malformed or UNSETTLED summary releases nothing.  In-run ledger: pilot root entries unchanged (one busy
      holder) and lane usage + outstanding reservation <= ceiling.
  N4  Timing evidence: last-alive and exit observations bound every child's exit time; SETTLED requires settlement
      within the child deadline + SETTLE_TAIL; qualification requires the exit observed by the deadline
      (SOLVER_TIMING / X.TIMING); terminal gate and commit re-check the frozen cutoffs (a late commit latches and
      can only be UNKNOWN); a late closeout or a voided chunk claim latches (no exit 0).
  N5  Item commits are charged to the output guard before their anchored O_EXCL creation; prestart admits the full
      reservation against free space, the STOP registry and the stability rule before any retained write.
  N6  Proof RAM: a live collector stays charged and keeps its blocks (release is deferred, retried at closeout);
      buffers are owned by the caller's list from creation (run_kissat owner), so every path releases them.
  N7  Monotonic unblock/TERM/quarantine transitions; metadata reads (GO, pinned inputs, monitor, prior launch
      records/summaries, quarantine receipts, captures) are regular-file, no-follow, non-blocking and bounded.
      Quarantine stays an explicit UNSETTLED state (continuing owner: this runner; disposition: parent).
  N8  Run tree created exclusively and anchored to directory descriptors opened without following symlinks; every
      runner-side creation/read in it goes through those descriptors; confinement (ancestry + anchored identities)
      re-validated at every admission, settlement, terminal gate and closeout; census = os.fwalk on the anchored
      root with (dev, ino, size, mtime_ns, ctime_ns, mode, nlink); every runner-written file's digest is
      re-verified at closeout.
  N9  Closeout reads the cancel stamp AFTER its boundary.
  N10 C6 runs kissat --time=CONTROL_TIMER_S and requires monotonic runtime bounds [C6_MIN_RUN_S, C6_MAX_RUN_S]
      (cleanup excluded), rc 0 and exactly ['s UNKNOWN'].
  N12 proc_listpids results are validated (whole entries, positive pids); unreadable descendant RSS stays None.
Residual limits (disclosed): native children receive path strings (confinement is re-validated around them, not
enforced inside them); OS process creation is not atomic with signal delivery (V7 orders the logical boundary);
absolute filesystem-call latency is not bounded (overruns fail closed); a quarantined owner is waited for without
bound by design. [superseded in v4 by B1]
PA19 96h P-STREAM runner v2 notes follow.
PA19 96h P-STREAM runner v2, multiset ms06: code/pilot_stream_drat_ms06_v1.py (e66cbc5d...) + focused fixes for the
parent-routed Codex source review (RUN/review/pa19-PSTREAM-source-codex-v1.prompt.stdout.txt af15a4e1..., HOLD, 13
findings) under the parent runtime-guard HOLD (RUN/review/runtime-guard-admission-HOLD-v1.json 6c1d8440...):
  V1 (Codex 1) No /bin/ps.  The start identity, the owned-process census (own process group + transitive PPID closure,
     zombies listed) and RSS (PROC_PIDTASKINFO) are read in-process through libproc (ctypes), fail-closed.  The
     user-required /bin/date host clock is KEPT as an owned, bounded metadata helper (class Helper): pinned binary,
     own session, pre-registered in HELPERS, admitted only while no native child or helper is unreaped and no cancel
     is stamped (V7 boundary), communicate() bounded by HELPER_WALL, then ONE SIGTERM and HELPER_TERM_WAIT; a
     survivor is latched and quarantined (waited for without bound, no further signal, UNSETTLED, parent
     disposition). [superseded in v4 by B1]  Helpers never overlap a native child (busy <= 2 processes, contract per_lane_busy_processes);
     HELPER_ALLOW per call is in the timing model.  A refused or failed read records null; no timestamp is invented.
     After an owner cancel no new process of any kind starts.
  V2 (Codex 2) Cumulative lane ceiling: lane usage (lstat walk of LANE, hard links once, traversal errors raise) +
     this run's outstanding reservation + every other admitted attempt (a pilot-v1 launch record without a summary,
     at its recorded reservation) <= LANE_CEILING (RUN/contract-v1.json per_lane_new_disk_bytes, pinned and
     re-read at prestart), checked at prestart, at every child admission and at every terminal gate.  Hard output
     guard: every retained write is charged against the run's reservation before it is made (capture files
     pre-charged at LOG_CAP each).
  V3 (Codex 3) Absolute (epoch) and elapsed (monotonic) cutoffs are enforced separately for the run and every child;
     helper allowances are in the arithmetic.  The chunk claim holds only if every owned process settles within
     its tail; a quarantined process voids it (recorded) and stays UNSETTLED under parent disposition.
  V4 (Codex 4) The output directory must be a new direct child of LANE/evidence/pilot-v1 whose ancestors are all
     real directories (lstat; a symlink refuses); its (dev, inode) is re-checked at closeout.  A complete,
     fail-closed run-tree census (every entry kind, lstat only, never opens FIFO/socket payloads, removals
     detected, traversal errors raise) brackets EVERY child.  The monitor must begin with the pinned observer_start
     provenance record.
  V5 (Codex 5) Proof RAM stays charged while ANY collector or feeder holds it (one frozen tuple counted once); every
     buffer is released in a finally on every control and item path; closeout reports per-buffer holders and
     latches if any proof RAM is still held.
  V6 (Codex 6) Ownership fields are set immediately after Popen; never-started transport endpoints are closed before
     reaping; every descriptor/cleanup step is independent and its outcome enters the settlement record before
     publication; a capture reader error trips supervision.  Single-SIGTERM behaviour unchanged.
  V7 (Codex 7) Launch/cancel boundary: launch_order = next(ORDER) is drawn, then latch/cancel/deadlines are checked,
     then Popen.  A cancel ordered before the boundary prevents the launch; a later one applies to the owned child.
  V8 (Codex 8, PS1-F1) After an over-long partial line is flushed, the rest of that physical line passes through
     unconditionally; duplicate matching resumes only at a genuine line start.  Duplicate warnings of BOTH phases
     are counted and disclosed per item, never required and never gated.
  V9 (Codex 9) Canonical parser records: exactly one stdin record, exactly one parse header equal to the CNF pin
     header, exactly one consumed record equal to the fed bytes, exactly one status line; the complete solver
     output must be exactly ['s UNSATISFIABLE'].
  V10 (Codex 10) Every defect carries a stable ID ('ID: text'); controls and tests compare complete ID sets.
  V11 (Codex 11) Each control evaluates a checker's intended predicate before the next child is launched; C2/C3/C4
     compare complete defect-ID sets; C6 is bound to kissat's measured timer expiry (rc 0, output exactly
     ['s UNKNOWN'], >= 1 s); C7 to kissat's missing-input diagnostic (rc 1, exactly "kissat: error: can not read
     '<path>'"); C7b to drat-trim's (rc 255, exactly 'c error opening "<path>".', drat-trim.c:1425-1427).
  V12 (Codex 12) Items are type/shape-checked at prestart and again before generation (ms09: exact non-bool ints,
     0 <= lo <= hi < denominator, canonical id; ms06: canonical id, no interval fields).
  V13 (Codex 13) Capture records distinguish non-dropped bytes from bytes physically written to the capped file.
Not changed: transport identity checks of v1 (C3 + offline tests establish only the transport-identity rejection
predicate; native checker behaviour on altered/truncated proofs is NOT claimed), CHECK_SECONDS 600, at most two
items per run, ITEMS = [] (controls-only qualification; production only by a later reviewed item-only delta bound
to the then-current frontier).
PA19 96h P-STREAM runner v1 notes follow.
PA19 96h P-STREAM runner v1, multiset ms06: pilot_file_drat_v26.py (d31f1a8e...) + the P-STREAM transport
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
checkers.  Production items of multiset ms06 are added only by a later item-only delta with its own parent GO:
  encode_skel_b.build_v2, DIRECT whole case.
Per item: CNF built in memory by the vendored unchanged encoder, frozen digest required, written by exclusive
creation and re-hashed (the only retained input); kissat -q -f --seed=1 --time=300 CNF PROOF_FIFO (owned RAM
collector, HARD cap, nothing on disk); then, only on a settled self-exit rc20 's UNSATISFIABLE' with a complete
buffer, checker A and then checker B with the frozen buffer on stdin; CNF and buffer re-hashed.
No deletion/overwrite, no SIGKILL, no subprocess timeout, no ulimit; lane FIFOs are new and never
removed.  The only signal ever sent is ONE SIGTERM to the identity-verified process group of an UNREAPED owned
Popen child (N1), then a bounded 60 s wait; a survivor is recorded UNSETTLED (receipt with identities, live census
and late obligations), no further signal, LATCH, and the runner returns to the parent without waiting (B1).
"""
import ctypes
import errno
import hashlib
import importlib.util
import itertools
import json
import os
import re
import select
import signal
import stat
import struct
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
DATE = ("/bin/date", "931edbfcbd847f3c1ccb504325a502db313ce20db27634744a7416c3c4b812f0")   # V1: pinned helper
CONTRACT = (RUN + "/contract-v1.json", "55baff0cf1ac1a4b0ab38b0eb1b1fa5a35a47c890f352b79dae4dfea919ffcaa")
LANE_CEILING = 10_737_418_240         # V2: contract resources.per_lane_new_disk_bytes (re-read at prestart)
PILOT_ROOT = LANE + "/evidence/pilot-v1"
CONTROL_DIR = LANE + "/control"            # N8: anchored directory of the SAT-candidate latch
TREE_SUBDIRS = ("children", "cwd", "fifo", "controls")   # N8: created and anchored with the run tree
BUSY_SLOTS = 2                              # N3: contract resources.per_lane_busy_processes (runner + one child)
ALLOCATION_SCHEMA = "PA19-96H-PARENT-ALLOCATION-v1"       # N3: the parent's single-allocator record inside the GO
KNOWN_SUMMARY_SCHEMAS = {"PA19-96H-PILOT-SUMMARY-v14": "v14", "PA19-96H-PSTREAM-SUMMARY-v4": "v4",
                         "PA19-96H-PILOT-SUMMARY-v32": "v4"}   # N3/B1: terminal schemas a release can verify
DISPOSITION_SCHEMA = "PA19-96H-PARENT-UNSETTLED-DISPOSITION-v1"   # B1: NEW parent disposition of UNSETTLED owners
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
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
FAMILY = "ms06"                       # V12: item shape family of this runner
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
HELPER_WALL = 5                       # V1: /bin/date helper bounded wait
HELPER_TERM_WAIT = 10                 # V1: bounded wait after the helper's single SIGTERM
HELPER_ALLOW = HELPER_WALL + HELPER_TERM_WAIT + 5   # V1/V3: per helper call in the timing model
HELPERS_PER_ITEM = 3                  # item start, item end, SAT candidate
HELPERS_PER_RUN = 2                   # launch record, closeout
HELPER_OUT_CAP = 4096
SUPERVISE_SLICE = 0.05                # N4/N10: poll slice of supervision, reaping and helpers
META_MAX = 64 * 1024 * 1024           # N7: bound of a whole-file metadata read (GO, pinned inputs, records)
MONITOR_MAX = 32 * 1024 * 1024        # N7: bound of the monitor read
SHA_FILE_MAX = 1 << 30                # N7: bound of a streamed hash
CONTROL_TIMER_S = 2                   # N10: kissat --time of C6
C6_MIN_RUN_S = 1.5                    # N10: required monotonic runtime lower bound of C6
C6_MAX_RUN_S = 5.0                    # N10: allowed monotonic runtime upper bound of C6
UNSETTLED_PUBLISH_ATTEMPTS = 3        # B1: immediate attempts to publish an UNSETTLED receipt
SETTLE_ALL_ATTEMPTS = 3               # B1: settle() attempts per child in the bounded settle_all pass
ITEM_WORST_SECONDS = (30 + (SOLVER_SECONDS + GRACE + SETTLE_TAIL) + 30
                      + len(CHECKERS) * (CHECK_SECONDS + GRACE + SETTLE_TAIL + 30) + HELPERS_PER_ITEM * HELPER_ALLOW)
RUN_HELPER_SECONDS = HELPERS_PER_RUN * HELPER_ALLOW
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
EXIT_CODES = (0, 10, 20, 30, 40, 50, 60, 70)
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
DATE_ARGV = [DATE[0], "+%Y-%m-%dT%H:%M:%S%z"]
DATE_RE = re.compile(rb"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{4}\n")
LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)   # V1: in-process process metadata (no /bin/ps)
LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_pidinfo.restype = ctypes.c_int
LIBPROC.proc_listpids.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_listpids.restype = ctypes.c_int
PROC_PGRP_ONLY, PROC_PPID_ONLY = 2, 6
PROC_PIDTBSDINFO, BSD_SIZE = 3, 136   # sys/proc_info.h struct proc_bsdinfo
PROC_PIDTASKINFO, TASK_SIZE = 4, 96   # sys/proc_info.h struct proc_taskinfo
SZOMB = 5
LIST_SLOTS = 4096

ORDER = itertools.count(1)
LATCH = []          # persistent safety/unsettled reasons; non-empty refuses every later child
OWNED = []          # every Child (pre-allocated before Popen), for the computed settlement summary
LIVE_BUFFERS = []   # S5: every ProofBuffer; the unreleased ones are charged to the lane RSS trip
LIVE_FEEDERS = []   # V5: every Feeder; a feeder still holding its tuple is charged too
HELPERS = []        # V1: every metadata Helper (pre-allocated before Popen)
HELPER_LOG = []     # V1: bounded helper records for the summary
TREE = {}           # N8: anchored directories: path -> (fd, dev, ino)
WRITTEN = {}        # N8: runner-written retained files: path -> (sha256, bytes), re-verified at closeout
KILLPG = os.killpg  # N1: the only signalling primitive (one verified group SIGTERM)
STATE = {"seq": 0, "out": None, "abs_end": None, "chunk_end": None, "remaining_reserve": 0,
         "cancel_order": None, "run_record": None, "go": None, "runner_sha": None, "mono0": None, "mono_end": None,
         "mono_chunk_end": None, "written": 0, "output_limit": None, "last_ledger": None, "reservation": 0,
         "pilot_entries": None}


def on_term(signum, frame):
    """r3#2: lock-free; only stamps a scalar order once."""
    if STATE["cancel_order"] is None:
        STATE["cancel_order"] = next(ORDER)


def cancelled():
    return STATE["cancel_order"] is not None


def latch(reason):
    LATCH.append(str(reason)[:STR_MAX])


def clock():
    """V1: host clock read through the owned, bounded /bin/date Helper.  Returns the /bin/date text, or None when the
    helper is refused (cancel stamped) or fails (latched); a timestamp is never invented."""
    try:
        return Helper(DATE_ARGV).run()
    except HelperRefused as exc:
        if len(HELPER_LOG) < LIST_MAX:
            HELPER_LOG.append({"refused": str(exc)[:STR_MAX]})
        return None
    except BaseException as exc:
        latch("host clock helper failed %r" % (exc,))
        return None


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


def charge_output(n):
    """V2: hard output guard.  Every retained write is counted against this run's total reservation before it is
    made; capture files are pre-charged at LOG_CAP each when their child is prepared; N5: item commits too."""
    if STATE["output_limit"] is not None and STATE["written"] + n > STATE["output_limit"]:
        latch("output guard: %d + %d > %d" % (STATE["written"], n, STATE["output_limit"]))
        raise RuntimeError("output guard: retained bytes would exceed the run reservation")
    STATE["written"] += n


def write_all(fd, data):
    view = memoryview(data)
    while view:
        k = os.write(fd, view)
        view = view[k:]


def register_written(path, digest, n):
    """N8: digest registry of every runner-written retained file; re-verified at closeout."""
    WRITTEN[path] = (digest, n)


def write_x(path, obj):
    data = serialize(obj)
    charge_output(len(data))
    fd = create_excl(path)                         # N8: anchored, exclusive, no-follow
    try:
        write_all(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    h = hashlib.sha256(data).hexdigest()
    register_written(path, h, len(data))
    return h


def write_bytes_x(path, data):
    charge_output(len(data))
    fd = create_excl(path)                         # N8: anchored, exclusive, no-follow
    try:
        write_all(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    h = hashlib.sha256(data).hexdigest()
    register_written(path, h, len(data))
    return h, len(data)


def open_regular(path, dir_fd=None):
    """N7/N8: open an existing REGULAR file read-only without following a final symlink and without blocking on a
    FIFO (O_NONBLOCK; the fstat check refuses every non-regular kind); returns (fd, fstat)."""
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC, dir_fd=dir_fd)
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode):
            raise RuntimeError("not a regular file: %s" % path)
    except BaseException:
        os.close(fd)
        raise
    return fd, st


def read_regular_bounded(path, limit, dir_fd=None):
    """N7: whole-file read of a regular file of at most `limit` bytes; larger files and growth are refused."""
    fd, st = open_regular(path, dir_fd)
    try:
        if st.st_size > limit:
            raise RuntimeError("%s is %d bytes > limit %d" % (path, st.st_size, limit))
        parts, n = [], 0
        while True:
            b = os.read(fd, min(1 << 20, limit + 1 - n))
            if not b:
                break
            parts.append(b)
            n += len(b)
            if n > limit:
                raise RuntimeError("%s grew beyond limit %d" % (path, limit))
        return b"".join(parts)
    finally:
        os.close(fd)


def sha_file(path, limit=SHA_FILE_MAX, dir_fd=None):
    """Streaming SHA-256 of a regular file: (hex, bytes).  N7: no final symlink, never blocks on a FIFO, bounded."""
    fd, _st = open_regular(path, dir_fd)
    try:
        h, n = hashlib.sha256(), 0
        while True:
            b = os.read(fd, 1 << 20)
            if not b:
                break
            h.update(b)
            n += len(b)
            if n > limit:
                raise RuntimeError("%s exceeds the hashing limit %d" % (path, limit))
        return h.hexdigest(), n
    finally:
        os.close(fd)


def sha_tree(path, limit=SHA_FILE_MAX):
    """N8: SHA-256 of a run-tree file read through its anchored directory descriptor."""
    dfd, name = tree_path(path)
    return sha_file(name, limit, dfd)


def read_tree(path, limit):
    """N8: bounded read of a run-tree file through its anchored directory descriptor."""
    dfd, name = tree_path(path)
    return read_regular_bounded(name, limit, dfd)


def read_pinned(path, expect, limit=META_MAX):
    """Pinned input read: bounded regular-file read (N7) whose SHA-256 must equal `expect`."""
    raw = read_regular_bounded(path, limit)
    got = hashlib.sha256(raw).hexdigest()
    if got != expect:
        raise RuntimeError(f"pin mismatch {path}: {got} != {expect}")
    return raw


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def _pidinfo(pid, flavor, size):
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    n = LIBPROC.proc_pidinfo(pid, flavor, 0, buf, size)
    return n, ctypes.get_errno(), buf.raw


def parse_pid_buffer(values, nbytes):
    """N12: validate a proc_listpids result: the byte count must be a whole number of c_int entries within the
    buffer, and every returned entry must be a positive pid; anything else raises (fail closed)."""
    size = ctypes.sizeof(ctypes.c_int)
    if not isinstance(nbytes, int) or nbytes < 0 or nbytes % size != 0 or nbytes // size > len(values):
        raise OSError(errno.EIO, "malformed proc_listpids byte count %r" % (nbytes,))
    entries = list(values[:nbytes // size])
    if any(p <= 0 for p in entries):
        raise OSError(errno.EIO, "malformed proc_listpids entry in %r" % (entries[:8],))
    return sorted(set(entries))


def list_pids(kind, value):
    """V1: proc_listpids in-process (no /bin/ps); fail-closed: raises on an error, a possibly truncated listing or
    (N12) a malformed result.  The kernel lists exited-but-unreaped processes too."""
    buf = (ctypes.c_int * LIST_SLOTS)()
    ctypes.set_errno(0)
    n = LIBPROC.proc_listpids(kind, value, buf, ctypes.sizeof(buf))
    err = ctypes.get_errno()
    if n < 0 or (n == 0 and err != 0) or n >= ctypes.sizeof(buf):
        raise OSError(err, "proc_listpids(%d, %d) returned %d" % (kind, value, n))
    return parse_pid_buffer(buf, n)


def bsd_identity(pid):
    """(identity, None) from PROC_PIDTBSDINFO (sys/proc_info.h struct proc_bsdinfo, 136 bytes), or (None, error)."""
    n, err, raw = _pidinfo(pid, PROC_PIDTBSDINFO, BSD_SIZE)
    if n != BSD_SIZE:
        return None, {"bsd_bytes": n, "errno": err}
    status, _xstatus, rpid, ppid = struct.unpack_from("=IIII", raw, 4)
    return {"pid": rpid, "ppid": ppid, "pgid": struct.unpack_from("=I", raw, 100)[0], "status": status,
            "start": list(struct.unpack_from("=QQ", raw, 120)),
            "comm": raw[48:64].split(b"\0")[0].decode("ascii", "replace")}, None


def task_rss(pid):
    """Resident bytes from PROC_PIDTASKINFO (struct proc_taskinfo, 96 bytes, pti_resident_size at offset 8); None
    when unreadable, never mapped to zero."""
    n, _err, raw = _pidinfo(pid, PROC_PIDTASKINFO, TASK_SIZE)
    if n != TASK_SIZE:
        return None
    return struct.unpack_from("=Q", raw, 8)[0]


def identity_checked(pid, runner_pid):
    """V1: start identity through libproc.  A readable child must show pid, ppid == runner and pgid == pid (own
    session).  A child that already exited is unreaped (Popen still owns the pid, which cannot be reused): its
    BSD read fails with ESRCH while the kernel still lists it in its own process group; that is recorded as such.
    Anything else raises (fail closed)."""
    ident, err = bsd_identity(pid)
    if ident is not None:
        if ident["pid"] != pid or ident["ppid"] != runner_pid or ident["pgid"] != pid:
            raise RuntimeError("start identity mismatch %r" % (ident,))
        return dict(ident, state="zombie" if ident["status"] == SZOMB else "alive")
    if err["errno"] == errno.ESRCH and pid in list_pids(PROC_PGRP_ONLY, pid):
        return {"pid": pid, "state": "exited_unreaped_listed_in_own_group", "bsd_read": err}
    raise RuntimeError("unavailable start identity %r" % (err,))


def descendants(pid, pgid):
    """V1/V4: owned-process census through libproc, fail-closed: every member of the child's own process group other
    than the child, plus the transitive closure of PROC_PPID_ONLY listings from the child (zombies included).
    Limit (documented): a descendant that both leaves the group and is re-parented away is not linkable."""
    found = {p for p in list_pids(PROC_PGRP_ONLY, pgid) if p != pid}
    seen, todo = {pid}, [pid]
    while todo:
        q = todo.pop()
        for c in list_pids(PROC_PPID_ONLY, q):
            if c not in seen:
                if len(seen) > LIST_SLOTS:
                    raise RuntimeError("descendant census exceeds %d processes" % LIST_SLOTS)
                seen.add(c)
                found.add(c)
                todo.append(c)
    return sorted(found)


def _entry_kind(m):
    return ("dir" if stat.S_ISDIR(m) else "file" if stat.S_ISREG(m) else "symlink" if stat.S_ISLNK(m)
            else "fifo" if stat.S_ISFIFO(m) else "socket" if stat.S_ISSOCK(m) else "other")


def _walk_fail(exc):
    raise exc


def census_entry(st):
    """N8: census evidence of one entry: directories (kind, dev, ino, mode) (their content is covered entry by
    entry); every other kind (kind, dev, ino, size, mtime_ns, ctime_ns, mode, nlink), so an in-place same-size
    rewrite or a replacement is visible."""
    k = _entry_kind(st.st_mode)
    if k == "dir":
        return (k, st.st_dev, st.st_ino, stat.S_IMODE(st.st_mode))
    return (k, st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns, stat.S_IMODE(st.st_mode), st.st_nlink)


def run_tree_census(root=None):
    """V4/N8: complete entry set of the run tree through os.fwalk on the ANCHORED root descriptor (no symlink is
    followed, every entry is lstat'ed relative to its directory descriptor, no payload is ever opened); `root`
    (a path) is for test fixtures only.  Any traversal or stat error raises."""
    if root is None:
        base, top, dfd0 = STATE["out"], ".", TREE[STATE["out"]][0]
    else:
        base, top, dfd0 = root, root, None
    snap = {}
    for dp, dns, fns, dfd in os.fwalk(top, onerror=_walk_fail, follow_symlinks=False, dir_fd=dfd0):
        for n in dns + fns:
            st = os.stat(n, dir_fd=dfd, follow_symlinks=False)
            rel = os.path.normpath(os.path.join(dp, n))
            p = os.path.join(base, rel) if root is None else rel
            snap[p] = census_entry(st)
    return snap


def lane_usage(root=LANE):
    """V2: logical bytes of every non-directory entry under root (lstat, symlinks not followed, hard links counted
    once); any traversal or stat error raises (fail closed)."""
    total, seen = 0, set()
    for dp, dns, fns in os.walk(root, onerror=_walk_fail, followlinks=False):
        for n in dns + fns:
            st = os.lstat(os.path.join(dp, n))
            if stat.S_ISDIR(st.st_mode):
                continue
            key = (st.st_dev, st.st_ino)
            if key not in seen:
                seen.add(key)
                total += st.st_size
    return total


def ancestry_refusal(path):
    """N8: every component of `path` must be a real directory (lstat; a symlink anywhere refuses)."""
    p = os.sep
    for comp in [c for c in path.split(os.sep) if c]:
        p = os.path.join(p, comp)
        try:
            st = os.lstat(p)
        except OSError as exc:
            return "ancestor %s unreadable %r" % (p, exc)
        if not stat.S_ISDIR(st.st_mode):
            return "ancestor %s is not a real directory" % p
    return None


def out_dir_refusal(out_dir, parent=PILOT_ROOT):
    """V4: the output must be a NEW direct child of parent, and parent and each of its ancestors must be a real
    directory (lstat: a symlink anywhere refuses); creation stays exclusive."""
    if os.path.dirname(out_dir) != parent or os.path.basename(out_dir) in ("", ".", ".."):
        return "output must be a direct child of " + parent
    why = ancestry_refusal(parent)
    if why:
        return why
    if os.path.lexists(out_dir):
        return "output path exists"
    return None


def anchor_dir(path, dir_fd, name):
    """N8: anchor an existing real directory: open it without following symlinks; returns (fd, dev, ino) and
    records it in TREE under `path`."""
    fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=dir_fd)
    st = os.fstat(fd)
    TREE[path] = (fd, st.st_dev, st.st_ino)
    return TREE[path]


def anchor_existing_dir(path):
    """N8: anchor an existing directory given by absolute path after an ancestry check, then re-validate that the
    path still names the anchored directory (closes the check/open window)."""
    why = ancestry_refusal(path)
    if why:
        raise RuntimeError(why)
    fd, dev, ino = anchor_dir(path, None, path)
    st = os.lstat(path)
    if not stat.S_ISDIR(st.st_mode) or (st.st_dev, st.st_ino) != (dev, ino) or ancestry_refusal(path):
        raise RuntimeError("directory changed while anchoring: " + path)
    return fd


def tree_path(path):
    """N8: (anchored directory fd, final name) for a path whose parent directory is anchored; refuses others."""
    d, name = os.path.dirname(path), os.path.basename(path)
    if d not in TREE or not name or name in (".", ".."):
        raise RuntimeError("path is not inside an anchored directory: " + path)
    return TREE[d][0], name


def create_excl(path, mode=0o644):
    """N8: exclusive, no-follow file creation through the anchored parent descriptor; returns a writable fd."""
    dfd, name = tree_path(path)
    return os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, mode, dir_fd=dfd)


def mkdir_anchored(path):
    """N8: exclusive directory creation through the anchored parent; the new directory is anchored too."""
    dfd, name = tree_path(path)
    os.mkdir(name, 0o755, dir_fd=dfd)
    return anchor_dir(path, dfd, name)


def create_run_tree(out_dir, parent=PILOT_ROOT):
    """N8: exclusive creation of the run tree, anchored to directory descriptors opened without following
    symlinks; every later runner-side creation or read in the tree goes through these descriptors."""
    why = out_dir_refusal(out_dir, parent)
    if why:
        raise RuntimeError(why)
    anchor_existing_dir(parent)
    mkdir_anchored(out_dir)
    for sub in TREE_SUBDIRS:
        mkdir_anchored(os.path.join(out_dir, sub))
    why = confinement_refusals(out_dir)
    if why:
        raise RuntimeError("run tree confinement: %r" % (why,))


def confinement_refusals(out_dir=None):
    """N8: every anchored directory still resolves by path, without symlinks, to its anchored (dev, inode), and
    every ancestor of the run tree is a real directory."""
    why = []
    try:
        root = out_dir or STATE["out"]
        if root is not None:
            w = ancestry_refusal(root)
            if w:
                why.append(w)
        for path, (fd, dev, ino) in list(TREE.items()):
            st, fst = os.lstat(path), os.fstat(fd)
            if not stat.S_ISDIR(st.st_mode) or (st.st_dev, st.st_ino) != (dev, ino) \
                    or (fst.st_dev, fst.st_ino) != (dev, ino):
                why.append("anchored directory moved or replaced: " + path)
    except BaseException as exc:
        why.append("confinement check failed %r" % (exc,))
    return why


def preservation_refusals():
    """N8: every runner-written retained file still has exactly its registered digest and size (anchored reads)."""
    why = []
    for path, (digest, n) in list(WRITTEN.items()):
        try:
            if sha_tree(path, limit=n) != (digest, n):
                why.append("retained file changed: " + path)
        except BaseException as exc:
            why.append("retained file unverifiable %s %r" % (path, exc))
    return why


def _hex64(x):
    return isinstance(x, str) and HEX64.fullmatch(x) is not None


def owner_identities_of_attempt(entry_dir, summary):
    """B1: (pid, start) identities a parent disposition must cover: the summary's UNSETTLED owners when a summary
    exists, otherwise every child launch record and every UNSETTLED receipt of the attempt (bounded reads)."""
    ids = []
    if isinstance(summary, dict):
        for u in summary.get("unsettled_owners") or []:
            u = u if isinstance(u, dict) else {}
            s0 = u.get("identity_at_start") if isinstance(u.get("identity_at_start"), dict) else {}
            ids.append((u.get("pid"), s0.get("start")))
        return ids
    cdir = os.path.join(entry_dir, "children")
    for n in sorted(os.listdir(cdir)):
        if n.endswith(".launch.json") or n.endswith(".QUARANTINE.json"):
            d = json.loads(read_regular_bounded(os.path.join(cdir, n), RECORD_MAX))
            d = d if isinstance(d, dict) else {}
            ident = d.get("identity") if isinstance(d.get("identity"), dict) else d.get("identity_at_start")
            ids.append((d.get("pid"), ident.get("start") if isinstance(ident, dict) else None))
    return ids


def disposition_refusals(entry_dir, release, idents, summary_sha):
    """B1: a NEW parent disposition must confirm that every listed process of an UNSETTLED (or summary-less) attempt
    ended.  The release entry names it by path and SHA-256; it must be a regular bounded file with that digest,
    schema DISPOSITION_SCHEMA, the same attempt_dir and summary digest (None for a summary-less attempt),
    all_processes_ended true and identities covering every (pid, start) the attempt lists.  The runner re-checks
    with libproc that none of them is alive: a live pid with the same start (or any live pid when the start is
    unknown) refuses; ESRCH or a zombie counts as ended; an unreadable pid refuses."""
    name = os.path.basename(entry_dir)
    disp = release.get("disposition")
    if not (isinstance(disp, dict) and isinstance(disp.get("path"), str) and _hex64(disp.get("sha256"))):
        return ["%s: UNSETTLED or summary-less attempt without a NEW parent disposition (reservation retained)" % name]
    try:
        d = json.loads(read_pinned(disp["path"], disp["sha256"], RECORD_MAX))
    except BaseException as exc:
        return ["%s: parent disposition unreadable or digest mismatch %r" % (name, exc)]
    if not isinstance(d, dict) or d.get("schema") != DISPOSITION_SCHEMA or d.get("attempt_dir") != entry_dir \
            or d.get("summary_sha256") != summary_sha or d.get("all_processes_ended") is not True \
            or not isinstance(d.get("identities"), list):
        return ["%s: parent disposition does not confirm the end of this attempt's processes" % name]
    covered = set()
    for x in d["identities"]:
        if isinstance(x, dict):
            covered.add((x.get("pid"), tuple(x["start"]) if isinstance(x.get("start"), list) else None))
    why = []
    for pid, start in idents:
        key = (pid, tuple(start) if isinstance(start, list) else None)
        if not (isinstance(pid, int) and not isinstance(pid, bool) and key in covered):
            why.append("%s: identity %r not covered by the parent disposition" % (name, (pid, start)))
            continue
        try:
            ident, err = bsd_identity(pid)
        except BaseException as exc:
            why.append("%s: pid %d unreadable %r" % (name, pid, exc))
            continue
        if ident is None:
            if (err or {}).get("errno") != errno.ESRCH:
                why.append("%s: pid %d unreadable %r" % (name, pid, err))
        elif ident.get("status") != SZOMB and (start is None or ident.get("start") == start):
            why.append("%s: pid %d still alive with the listed identity" % (name, pid))
    return why


def release_refusals(entry_dir, release, go_sha):
    """N3/B1: verified parent release of ONE prior attempt directory.  The parent allocation must list it with the
    SHA-256 of its launch record and of its summary (None only for a summary-less attempt); the files must be
    regular and bounded (no symlink, no FIFO) with exactly those digests; a summary must be a known terminal schema.
    A CLEAN attempt (all children settled, no quarantine/UNSETTLED receipt; for v4/v32 summaries also all helpers
    settled, no UNSETTLED owner and no proof RAM outstanding) is released by the plain entry.  An UNSETTLED or
    summary-less attempt keeps its reservation until a NEW parent disposition confirms that every listed process
    ended (disposition_refusals); a legacy v14 summary must be clean.  The attempt's launch record must not name
    this GO (one-use admission).  A stale, malformed, partial or symlinked summary releases nothing."""
    name = os.path.basename(entry_dir)
    try:
        st = os.lstat(entry_dir)
    except OSError as exc:
        return ["%s unreadable %r" % (name, exc)]
    if not stat.S_ISDIR(st.st_mode):
        return ["%s is not a real directory" % name]
    if release is None:
        return ["%s is not released by the parent allocation" % name]
    why = []
    try:
        lr = read_regular_bounded(os.path.join(entry_dir, "launch-record.json"), RECORD_MAX)
        quarantine = sorted(n for n in os.listdir(os.path.join(entry_dir, "children")) if n.endswith(".QUARANTINE.json"))
        l = json.loads(lr)
    except BaseException as exc:
        return ["%s: launch record or children unreadable %r" % (name, exc)]
    if hashlib.sha256(lr).hexdigest() != release.get("launch_record_sha256"):
        why.append("%s: launch record digest != parent release" % name)
    go = l.get("go") if isinstance(l, dict) else None
    if not isinstance(go, dict) or go.get("sha256") == go_sha:
        why.append("%s: launch record missing a GO or already consumed this GO (one-use)" % name)
    summary_sha = release.get("summary_sha256")
    if summary_sha is None:
        if os.path.lexists(os.path.join(entry_dir, "summary.json")):
            why.append("%s: a summary exists but the release names none" % name)
        try:
            idents = owner_identities_of_attempt(entry_dir, None)
        except BaseException as exc:
            return why + ["%s: identities unreadable %r" % (name, exc)]
        return why + disposition_refusals(entry_dir, release, idents, None)
    try:
        sm = read_regular_bounded(os.path.join(entry_dir, "summary.json"), RECORD_MAX)
        s = json.loads(sm)
    except BaseException as exc:
        return why + ["%s: summary unreadable or malformed %r" % (name, exc)]
    if hashlib.sha256(sm).hexdigest() != summary_sha:
        why.append("%s: summary digest != parent release" % name)
    if not isinstance(s, dict) or s.get("schema") not in KNOWN_SUMMARY_SCHEMAS:
        return why + ["%s: unknown summary schema" % name]
    ec = s.get("exit_code")
    if not (isinstance(ec, int) and not isinstance(ec, bool) and ec in EXIT_CODES):
        why.append("%s: no terminal exit code" % name)
    ch = s.get("children")
    clean = (s.get("all_children_settled") is True and isinstance(ch, list) and not quarantine
             and all(isinstance(c, dict) and c.get("settled") is True for c in ch))
    if KNOWN_SUMMARY_SCHEMAS[s["schema"]] == "v4":
        clean = clean and (s.get("all_helpers_settled") is True and s.get("quarantine_receipts") == []
                           and s.get("unsettled_owners") == [] and s.get("proof_ram_outstanding_bytes") in (0, None))
    if not clean:
        if KNOWN_SUMMARY_SCHEMAS[s["schema"]] == "v14":
            why.append("%s: legacy summary is not fully settled" % name)
        else:
            try:
                idents = owner_identities_of_attempt(entry_dir, s)
            except BaseException as exc:
                return why + ["%s: identities unreadable %r" % (name, exc)]
            why += disposition_refusals(entry_dir, release, idents, summary_sha)
    return why


def allocation_refusals(go, go_sha, out_dir, full_reserve, root=PILOT_ROOT):
    """N3/B1: the parent's explicit allocation inside the GO is the ONLY admission authority (no second scheduler).
    Required: schema ALLOCATION_SCHEMA; out_dir == OUT_DIR (with exclusive creation: one-use); reservation_bytes
    >= this run's reservation; lane_ceiling_bytes == LANE_CEILING; busy_slots == BUSY_SLOTS; released_attempts
    covering EVERY existing entry of the pilot root with a verified release (release_refusals; an UNSETTLED or
    summary-less attempt additionally needs a NEW parent disposition), so no other attempt holds a busy slot or an
    unreleased reservation; measured lane usage + reservation <= ceiling.  Returns (refusals, ledger)."""
    a = go.get("allocation") if isinstance(go, dict) else None
    if not isinstance(a, dict) or a.get("schema") != ALLOCATION_SCHEMA:
        return ["GO lacks the parent allocation %r" % ALLOCATION_SCHEMA], None
    why = []
    if a.get("out_dir") != out_dir:
        why.append("allocation out_dir != OUT_DIR")
    res = a.get("reservation_bytes")
    if not (_nat(res) and res >= full_reserve):
        why.append("allocation reservation %r < runner reservation %d" % (res, full_reserve))
    if a.get("lane_ceiling_bytes") != LANE_CEILING or a.get("busy_slots") != BUSY_SLOTS:
        why.append("allocation ceiling/busy slots differ from the contract values")
    rel = a.get("released_attempts")
    by_dir = {}
    if not isinstance(rel, list):
        why.append("allocation released_attempts is not a list")
        rel = []
    for r in rel:
        ok = (isinstance(r, dict) and isinstance(r.get("dir"), str) and os.path.dirname(r["dir"]) == root
              and _hex64(r.get("launch_record_sha256"))
              and (r.get("summary_sha256") is None or _hex64(r.get("summary_sha256"))) and r["dir"] not in by_dir)
        if not ok:
            why.append("malformed or duplicate release entry %r" % (r,))
            continue
        by_dir[r["dir"]] = r
    try:
        entries = sorted(os.listdir(root))
        usage = lane_usage()
    except BaseException as exc:
        return why + ["pilot root or lane usage unreadable %r" % (exc,)], None
    for e in entries:
        d = os.path.join(root, e)
        if d == out_dir:
            why.append("OUT_DIR already exists (GO already used)")
            continue
        why += release_refusals(d, by_dir.get(d), go_sha)
    for d in by_dir:
        if os.path.basename(d) not in entries:
            why.append("released attempt %s does not exist" % d)
    if not _nat(res):
        res = 0
    if usage + res > LANE_CEILING:
        why.append("lane usage %d + reservation %d > ceiling %d" % (usage, res, LANE_CEILING))
    led = {"allocation_id": a.get("allocation_id"), "lane_usage_bytes": usage, "reservation_bytes": res,
           "runner_reservation_bytes": full_reserve, "ceiling_bytes": LANE_CEILING, "pilot_entries": entries,
           "released_attempts": len(by_dir)}
    return why, led



def ledger_refusals():
    """N3: in-run ledger: the pilot root still holds exactly the prestart entries plus this run (no other attempt
    appeared: one busy holder) and measured lane usage + this run's outstanding reservation (reservation minus
    bytes already charged) <= LANE_CEILING.  Returns (refusals, ledger)."""
    try:
        now = sorted(os.listdir(PILOT_ROOT))
        usage = lane_usage()
    except BaseException as exc:
        return ["lane ledger unavailable %r" % (exc,)], None
    expect = sorted(STATE["pilot_entries"] + [os.path.basename(STATE["out"])])
    outstanding = max(0, STATE["reservation"] - STATE["written"])
    led = {"lane_usage_bytes": usage, "outstanding_reservation_bytes": outstanding, "ceiling_bytes": LANE_CEILING,
           "pilot_entries_unchanged": now == expect}
    why = []
    if now != expect:
        why.append("pilot root entries changed (another attempt or a prior attempt changed): %r" % (sorted(set(now) ^ set(expect))[:6],))
    if usage + outstanding > LANE_CEILING:
        why.append("lane ledger %d + %d > ceiling %d" % (usage, outstanding, LANE_CEILING))
    return why, led


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
    """resource-stability-addendum v1 rule over the v2-pinned v3 monitor; strict schema.  V4: the first record must be
    the pinned observer_start provenance header (a sample-only log is refused)."""
    try:
        raw = read_regular_bounded(MONITOR, MONITOR_MAX)   # N7: regular, no symlink, never blocks, bounded
    except BaseException as exc:
        return ["monitor unreadable %r" % (exc,)]
    complete = raw.split(b"\n")[:-1]  # last element: b"" after a final newline, or an ignored partial line
    rows = []
    header_seen = False
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
                header_seen = True
                continue
            if set(o) != {"t", "free", "floor_bytes", "scope"} or o["floor_bytes"] != 12_000_000_000 \
                    or o["scope"] != SAMPLE_SCOPE:
                raise ValueError("sample schema/fixed values")
            _int(o["floor_bytes"], 0)
            rows.append((_aware(o["t"]).timestamp(), _int(o["free"], 0)))
        except Exception as exc:
            return ["malformed monitor line %d: %r (%r)" % (i, ln[:160], exc)]
    if not header_seen:
        return ["monitor lacks the pinned observer_start provenance header"]
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



def full_admission(projected, child_deadline, child_deadline_mono):
    """Blocking part of admission (registry, monitor, statvfs, N3 lane ledger, N8 confinement, V3 absolute and
    elapsed fit).  Returns refusal reasons."""
    why = []
    try:
        why += registry_refusals()
        why += stability_refusals(projected)
        fb = free_bytes()
        if fb < FRESH_BASE + projected:
            why.append(f"fresh free {fb} < 12.2e9 + {projected}")
        if fb - STATE["remaining_reserve"] < FREE_FLOOR:
            why.append(f"free {fb} - remaining reservations {STATE['remaining_reserve']} < 12e9")
        led_why, STATE["last_ledger"] = ledger_refusals()
        why += led_why
        why += confinement_refusals()
    except Exception as exc:
        why.append("admission exception %r" % exc)
    if child_deadline + SETTLE_TAIL > STATE["abs_end"] or child_deadline + SETTLE_TAIL + MARGIN > STATE["chunk_end"] \
            or child_deadline + SETTLE_TAIL > OWNED_SETTLED_BY - 180 \
            or child_deadline_mono + SETTLE_TAIL > STATE["mono_end"] \
            or child_deadline_mono + SETTLE_TAIL + MARGIN > STATE["mono_chunk_end"]:
        why.append("per-child chunk fit / absolute or elapsed end (with full settlement tail)")
    return why


def buffer_charge():
    """V5/N6: proof RAM still held by ANY collector or feeder.  A buffer counts its retained bytes while its
    collector thread is alive or until it is released; a feeder that has not dropped its blocks counts its tuple
    even after the buffer was released; one frozen tuple is counted once (keyed by identity)."""
    held = {}
    for b in list(LIVE_BUFFERS):
        if b.thread.is_alive() or not b.released:
            blocks = b.blocks
            key = ("tuple", id(blocks)) if isinstance(blocks, tuple) and blocks else ("collector", id(b))
            held[key] = max(held.get(key, 0), b.retained)
    for f in list(LIVE_FEEDERS):
        blocks = f.blocks
        if blocks:
            key = ("tuple", id(blocks))
            held[key] = max(held.get(key, 0), f.expected)
    return sum(held.values())


class ProofBuffer:
    """S1: owned FIFO reader retaining the proof in RAM only (immutable FEED_BLOCK blocks) with a HARD byte cap;
    bytes and SHA-256 are measured as they arrive from the producer; nothing is written to disk.  N8: the FIFO is
    created, opened and re-checked through its anchored directory descriptor; N7: monotonic unblock deadline;
    N6: charged while the collector thread lives or until released."""

    def __init__(self, fifo_path, cap):
        self.dir_fd, self.fifo_name = tree_path(fifo_path)
        os.mkfifo(self.fifo_name, 0o600, dir_fd=self.dir_fd)          # exclusive: FileExistsError if present
        self.fifo_ino = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False).st_ino
        self.fifo_path, self.cap = fifo_path, cap
        self.blocks = []
        self.sha = hashlib.sha256()
        self.retained = self.received = self.discarded = 0
        self.over_cap = self.connected = self.eof = self.released = self.release_requested = False
        self.frozen_id = None                   # V5: identity of the frozen tuple shared with feeders
        self.error = None
        self.unblocked_by_runner = False
        self.finished = None
        LIVE_BUFFERS.append(self)
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def _run(self):
        acc = bytearray()
        try:
            fd = os.open(self.fifo_name, os.O_RDONLY | os.O_CLOEXEC, dir_fd=self.dir_fd)  # blocks until a writer opens
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
        deadline = time.monotonic() + SINK_UNBLOCK            # N7: monotonic
        while self.thread.is_alive() and not self.connected and time.monotonic() < deadline:
            try:
                fd = os.open(self.fifo_name, os.O_WRONLY | os.O_NONBLOCK | os.O_CLOEXEC, dir_fd=self.dir_fd)
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
            st = os.stat(self.fifo_name, dir_fd=self.dir_fd, follow_symlinks=False)
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
                self.frozen_id = id(self.blocks)
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
        """N6: drop this buffer's reference to its RAM blocks, but only once its collector thread has ended: a live
        collector keeps its blocks (it may still append) and stays charged; release is retried by the owner's
        finally and at closeout.  The bytes stay charged while any feeder still holds the frozen tuple.  Returns
        True iff released."""
        self.release_requested = True
        if self.thread.is_alive():
            return False
        self.released = True
        self.blocks = ()
        return True

    def holders(self):
        """V5: feeders that still hold this buffer's frozen tuple."""
        return [f.label for f in list(LIVE_FEEDERS) if f.blocks and self.frozen_id is not None
                and id(f.blocks) == self.frozen_id]

    def accounting(self):
        return {"fifo": self.fifo_path, "retained": self.retained, "released": self.released,
                "release_requested": self.release_requested, "collector_alive": self.thread.is_alive(),
                "still_held_by_feeders": self.holders(), "frozen": self.frozen_id is not None}



class Feeder:
    """S2: owned writer of a frozen RAM proof buffer into ONE checker's stdin pipe; hashes/counts exactly the
    bytes os.write() accepted.  Modes: plain; suffix (C3: SUFFIX after the proof); hold (C7b: the first write
    waits until the checker was reaped).  The runner's read end is closed right after Popen (close_read);
    the write end is closed exactly once: by the thread, or by abandon() when the thread never started."""

    def __init__(self, blocks, mode="plain", label=""):
        if mode not in ("plain", "suffix", "hold"):
            raise RuntimeError("unknown feed mode %r" % (mode,))
        if not isinstance(blocks, tuple):
            raise RuntimeError("proof buffer not frozen")
        self.blocks, self.mode, self.label = blocks, mode, label
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
        LIVE_FEEDERS.append(self)                  # V5: charged while it holds the tuple

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
        """Never-started feeder: close each still-open pipe end independently and drop the blocks.  V6: returns the
        close errors so that the caller incorporates them before any settlement is published."""
        errs = []
        for name in ("rfd", "wfd"):
            fd = getattr(self, name)
            setattr(self, name, None)
            if fd is not None:
                try:
                    os.close(fd)
                except OSError as exc:
                    errs.append("%s %r" % (name, exc))
        self.blocks = ()
        if errs:
            self.close_error = "; ".join(errs)
        return errs

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
    """S3: per-checker capture-filter state; V8: 'cont' = pass through until the next newline after an over-long
    partial line was flushed."""
    return {"raw_sha": hashlib.sha256(), "raw_bytes": 0, "raw_eof": False, "pending": b"", "header_clauses": None,
            "dup_low": 0, "dup_high": 0, "dup_bytes": 0, "tail": 0, "cont": False, "flushes": 0}


class Owned:
    """N1/N7/B1: ownership, stop and reap state shared by native children and metadata helpers.
    Stop: the ONLY signal ever sent is ONE SIGTERM to the owned process GROUP (KILLPG), and only after the retained,
    unreaped leader has been re-verified against its start identity (verify_owned); an unverifiable identity
    refuses the signal (no speculative signalling), latches, and the owner stays UNSETTLED.  No escalation.
    Reap (B1, contract resources.stop = SIGTERM + BOUNDED wait only): monotonic and FINITE.  If the owner is not
    reaped within the grace (term_wait after the stop request or refusal), UNSETTLED is recorded irreversibly
    (latch + exclusive receipt with the exact identities, a live census and the late-artifact obligations), the
    reap RETURNS None and nothing waits for that owner again; the run then stops admitting work, closes out
    (bounded) and returns to the parent with exit 50.  The reservation stays held until a NEW parent disposition
    confirms that every listed process ended (release_refusals).  No synthetic settlement.
    Exit evidence: the first monotonic/epoch observation of the exit, taken after the poll that saw it, is a
    conservative upper bound of the exit time; last_alive_mono (taken before a poll that saw the process alive)
    is a lower bound."""

    def _owned_init(self):
        self.proc = self.pid = self.pgid = None
        self.identity_at_start = None
        self.launch_order = None
        self.stop = None
        self.term_sent_mono = self.term_sent_epoch = self.term_refused_mono = None
        self.term_delivery = None
        self.quarantined = False
        self.quarantine_receipt_state = "none"
        self.quarantine_path = None
        self.unsettled = None
        self.popen_call_mono = self.started_mono = self.started_epoch = None
        self.last_alive_mono = None
        self.exit_observed_mono = self.exit_observed_epoch = None

    def stop_requested(self):
        return self.term_sent_mono is not None or self.term_refused_mono is not None

    def observe_exit(self):
        """Poll once; on the first observed exit record the observation time (an upper bound of the exit time)."""
        rc = self.proc.poll()
        if rc is not None and self.exit_observed_mono is None:
            self.exit_observed_mono, self.exit_observed_epoch = time.monotonic(), time.time()
        return rc

    def verify_owned(self):
        """N1: (True, evidence) iff the retained Popen is unreaped and its leader is still the process whose start
        identity was verified at launch (same pid and pgid, ppid == this runner, same start time), or the unreaped
        leader has exited and is still listed in its own process group (an unreaped pid/pgid cannot be reused)."""
        if self.proc is None or self.proc.returncode is not None:
            return False, "not an unreaped owned process"
        ident0 = self.identity_at_start
        if not isinstance(ident0, dict) or ident0.get("pid") != self.pid:
            return False, "no verified start identity"
        try:
            ident, err = bsd_identity(self.pid)
            if ident is not None:
                same_start = ident0.get("start") is None or ident.get("start") == ident0.get("start")
                if ident["pid"] == self.pid and ident["pgid"] == self.pgid == self.pid \
                        and ident["ppid"] == os.getpid() and same_start:
                    return True, "leader identity re-verified"
                return False, "leader identity mismatch %r" % (ident,)
            if err["errno"] == errno.ESRCH and self.pid in list_pids(PROC_PGRP_ONLY, self.pgid):
                return True, "unreaped leader listed in its own group"
            return False, "leader unreadable %r" % (err,)
        except BaseException as exc:
            return False, "identity check failed %r" % (exc,)

    def term(self, reason):
        """N1: record the stop reason; at most ONE identity-verified group SIGTERM; never signals a reaped or an
        unverifiable owner (the refusal latches and leaves the owner UNSETTLED)."""
        if self.stop is None:
            self.stop = reason
        if self.proc is None or self.stop_requested():
            return
        if self.observe_exit() is not None:
            return
        ok, evidence = self.verify_owned()
        if not ok:
            self.term_refused_mono = time.monotonic()
            self.term_delivery = {"delivered": False, "refused": evidence}
            latch("stop refused for pid %s: %s; UNSETTLED" % (self.pid, evidence))
            return
        t_m, t_e = time.monotonic(), time.time()
        try:
            KILLPG(self.pgid, signal.SIGTERM)
            self.term_delivery = {"delivered": True, "pgid": self.pgid, "evidence": evidence}
        except OSError as exc:
            self.term_delivery = {"delivered": False, "pgid": self.pgid, "error": repr(exc), "evidence": evidence}
        self.term_sent_mono, self.term_sent_epoch = t_m, t_e

    def late_obligations(self):
        """B1: what an unreaped owner can still touch after the runner returns (overridden by Child)."""
        return [{"what": "stdout pipe", "note": "this runner's read end closes when it returns; the survivor may then "
                                                "see EPIPE/SIGPIPE on its next write"}]

    def live_census(self):
        """B1: exact identities of the leader, its process group and its PPID-closure descendants, read now."""
        out = {"leader_pid": self.pid, "pgid": self.pgid, "start_identity": self.identity_at_start}
        try:
            ident, err = bsd_identity(self.pid)
            out["leader_now"] = ident if ident is not None else err
            members = list_pids(PROC_PGRP_ONLY, self.pgid)
            out["group_members"] = [{"pid": p, "identity": bsd_identity(p)[0], "rss": task_rss(p)}
                                    for p in members[:LIST_MAX]]
            out["descendants"] = descendants(self.pid, self.pgid)[:LIST_MAX]
        except BaseException as exc:
            out["census_error"] = repr(exc)
        return out

    def _unsettled_receipt(self):
        return {"pid": self.pid, "pgid": self.pgid, "argv": self.argv, "identity_at_start": self.identity_at_start,
                "epoch": time.time(), "stop": self.stop, "term_delivery": self.term_delivery,
                "settlement": "UNSETTLED", "chunk_claim": "voided", "live_census": self.live_census(),
                "late_obligations": self.late_obligations(),
                "runner_action": "recorded at finite grace expiry; returns to the parent without any further wait, "
                                 "signal or escalation",
                "reservation": "retained until a NEW parent disposition confirms that every listed process ended",
                "disposition_owner": "parent"}

    def _receipt_valid(self):
        try:
            d = json.loads(read_tree(self.quarantine_path, RECORD_MAX))
            return isinstance(d, dict) and d.get("pid") == self.pid and d.get("settlement") == "UNSETTLED"
        except BaseException:
            return False

    def _record_unsettled(self):
        """B1: irreversible UNSETTLED record: latch, exclusive receipt (at most UNSETTLED_PUBLISH_ATTEMPTS immediate
        attempts; no loop beyond them) and the in-memory record the summary publishes."""
        self.quarantined = True
        try:
            latch("UNSETTLED pid %s after the bounded stop grace; reservation retained; parent disposition" % self.pid)
        except BaseException:
            pass
        receipt = self._unsettled_receipt()
        self.unsettled = {k: receipt[k] for k in ("pid", "pgid", "identity_at_start", "stop", "term_delivery",
                                                  "live_census", "late_obligations")}
        if self.quarantine_path is None:
            self.quarantine_receipt_state = "unpublishable: no run tree"
            return
        for _attempt in range(UNSETTLED_PUBLISH_ATTEMPTS):
            try:
                write_x(self.quarantine_path, receipt)
                self.quarantine_receipt_state = "written"
                return
            except FileExistsError:                # r5#3: validate, never assume
                self.quarantine_receipt_state = "written" if self._receipt_valid() else "failed"
                return
            except BaseException as exc:
                self.quarantine_receipt_state = "failed %r" % (exc,)

    def reap_owned(self, term_wait):
        """N1/N7/B1: bounded, exception-resistant reap (monotonic).  Requests the verified stop for a live owner,
        then waits at most term_wait after the stop request or refusal (a hard bound from entry covers a stop that
        could not even be requested).  Returns the return code if reaped within the bound; otherwise records
        UNSETTLED and returns None.  Never loops beyond the bound; never signals again."""
        entry = time.monotonic()
        while True:
            try:
                if self.observe_exit() is not None:
                    return self.proc.wait()
                if self.quarantined:
                    return None                    # already recorded UNSETTLED: never wait again
                if self.stop is None:
                    self.stop = "reap_of_a_live_owner"     # a live owner is only reaped after a stop request
                if not self.stop_requested():
                    self.term(self.stop)
                t0 = self.term_sent_mono if self.term_sent_mono is not None else self.term_refused_mono
                if time.monotonic() >= (entry if t0 is None else t0) + term_wait:
                    self._record_unsettled()
                    return None
                time.sleep(SUPERVISE_SLICE)
            except BaseException:
                if time.monotonic() >= entry + term_wait + SUPERVISE_SLICE:
                    try:
                        self._record_unsettled()
                    except BaseException:
                        self.quarantined = True
                    return None
                try:
                    time.sleep(0.05)
                except BaseException:
                    pass


class HelperRefused(Exception):
    pass


class Helper(Owned):
    """N2: one OWNED, BOUNDED metadata helper process (only the pinned /bin/date) under the same ownership rules as
    a native child.  Admission: no latch, no cancel stamped, every earlier owned process settled, and HELPER_ALLOW
    fits before the frozen run cutoffs; pre-registration in HELPERS and the V7 launch/cancel boundary before
    Popen; own session; start identity verified.  Supervision (monotonic, SUPERVISE_SLICE): cancel, HELPER_WALL,
    capture bounded at HELPER_OUT_CAP bytes read incrementally (never more than HELPER_OUT_CAP + 1 retained),
    descendant census, resident bytes of runner + helper within LANE_RSS_TRIP.  Stop: Owned.term (one verified
    group SIGTERM); reap bounded by HELPER_TERM_WAIT, then (B1) an irreversible UNSETTLED record and no further wait.
    Cleanup runs in a finally on every path.  Settlement and output validity are separate explicit predicates (_settle); only a settled helper
    with valid output returns its line; closeout counts only settled helpers."""

    def __init__(self, argv):
        self._owned_init()
        self.argv = argv
        self.settled = False
        self.out = bytearray()
        self.out_total = 0
        self.eof = False
        self.record = {"argv": argv}

    def admission_refusals(self):
        why = []
        if LATCH:
            why.append("latch held")
        if STATE["cancel_order"] is not None:
            why.append("cancel stamped (order %s)" % STATE["cancel_order"])
        if any(c.proc is not None and c.settled_rec is None for c in OWNED) or \
                any(h.proc is not None and not h.settled for h in HELPERS):
            why.append("an owned process is not settled")
        if STATE["mono_end"] is not None and (time.monotonic() + HELPER_ALLOW > STATE["mono_end"]
                                              or time.time() + HELPER_ALLOW > STATE["abs_end"]):
            why.append("helper allowance does not fit before the frozen run cutoffs")
        return why

    def run(self):
        why = self.admission_refusals()
        if why:
            if "an owned process is not settled" in why:
                latch("metadata helper refused: an owned process is not settled")
            raise HelperRefused("; ".join(why))
        if sha_file(self.argv[0])[0] != DATE[1]:
            raise RuntimeError("helper binary pin mismatch")
        HELPERS.append(self)                        # ownership exists before the process does
        self.launch_order = next(ORDER)             # V7 boundary
        if STATE["cancel_order"] is not None or LATCH:
            HELPERS.remove(self)
            raise HelperRefused("cancel or latch at the helper launch boundary %d" % self.launch_order)
        children_dir = None if STATE["out"] is None else os.path.join(STATE["out"], "children")
        if children_dir in TREE:
            self.quarantine_path = os.path.join(children_dir, "helper-%d.QUARANTINE.json" % self.launch_order)
        self.popen_call_mono = time.monotonic()
        try:
            self.proc = subprocess.Popen(self.argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, start_new_session=True, close_fds=True)
        except BaseException:
            HELPERS.remove(self)
            raise
        rc = None
        try:
            self.pid = self.pgid = self.proc.pid    # ownership fields first, before any fallible step
            self.started_mono, self.started_epoch = time.monotonic(), time.time()
            self.identity_at_start = identity_checked(self.pid, os.getpid())
            self._supervise_and_capture()
        except BaseException as exc:
            self.record["exception"] = repr(exc)[:STR_MAX]
            if self.stop is None:
                self.stop = "helper_exception"
        finally:
            rc = self.reap_owned(HELPER_TERM_WAIT)   # verified stop if one is set; bounded; None = UNSETTLED (B1)
            try:
                self.proc.stdout.close()
            except BaseException as exc:
                self.record["stdout_close_error"] = repr(exc)
        return self._settle(rc)

    def _supervise_and_capture(self):
        fd = self.proc.stdout.fileno()
        end = self.started_mono + HELPER_WALL
        hard_end = end + HELPER_TERM_WAIT
        peak = 0
        while True:
            now = time.monotonic()
            alive = self.observe_exit() is None
            if alive:
                if cancelled():
                    self.term("owner_cancel_sigterm")
                elif now > end:
                    self.term("helper_wall")
                elif self.out_total > HELPER_OUT_CAP:
                    self.term("helper_output_cap")
                else:
                    found = descendants(self.pid, self.pgid)
                    rss_h, rss_r = task_rss(self.pid), task_rss(os.getpid())
                    if found:
                        self.term("helper_descendant")
                    elif rss_r is None or (rss_h is None and self.observe_exit() is None):
                        self.term("helper_rss_unreadable")
                    else:
                        peak = max(peak, (rss_h or 0) + rss_r)
                        if peak > LANE_RSS_TRIP:
                            self.term("helper_lane_rss")
                if self.stop_requested():
                    break
            if self.eof and not alive:
                break
            if now > hard_end:
                break                               # settlement records the missing EOF / exit
            if not self.eof:
                ready, _w, _x = select.select([fd], [], [], SUPERVISE_SLICE)
                if ready:
                    b = os.read(fd, 65536)
                    if not b:
                        self.eof = True
                    else:
                        self.out_total += len(b)
                        room = HELPER_OUT_CAP + 1 - len(self.out)
                        if room > 0:
                            self.out += b[:room]
            else:
                time.sleep(SUPERVISE_SLICE)
        self.record["peak_rss_bytes"] = peak

    def _settle(self, rc):
        """N2: SETTLED = the resources are released: reaped, process group empty, not quarantined, no refused stop,
        verified start identity.  VALID output additionally needs no stop, EOF, output within the cap and exactly one
        /bin/date line, rc 0, exit within HELPER_WALL and settlement within HELPER_ALLOW.  An unsettled helper or an
        invalid output latches and raises; a settled helper stopped by an owner cancel raises HelperRefused."""
        unsettled = []
        if self.quarantined:
            unsettled.append("quarantined (receipt %s)" % self.quarantine_receipt_state)
        if self.term_refused_mono is not None:
            unsettled.append("stop refused: identity unverifiable")
        if self.identity_at_start is None:
            unsettled.append("no verified start identity")
        if rc is None:
            unsettled.append("not reaped")
        try:
            if list_pids(PROC_PGRP_ONLY, self.pgid):
                unsettled.append("process group not empty after reap")
        except BaseException as exc:
            unsettled.append("group census failed %r" % (exc,))
        invalid = []
        if self.stop is not None:
            invalid.append("stopped: %s" % self.stop)
        if not self.eof:
            invalid.append("no EOF on the helper output")
        if self.out_total > HELPER_OUT_CAP:
            invalid.append("helper output over the cap")
        if rc != 0:
            invalid.append("helper rc %r" % (rc,))
        if DATE_RE.fullmatch(bytes(self.out)) is None:
            invalid.append("output is not exactly one /bin/date line")
        done = time.monotonic()
        if self.exit_observed_mono is None or self.exit_observed_mono > self.popen_call_mono + HELPER_WALL \
                or done > self.popen_call_mono + HELPER_ALLOW:
            invalid.append("helper exit or settlement not within its bound")
        self.settled = not unsettled
        self.record.update(pid=self.pid, launch_order=self.launch_order, rc=rc, settled=self.settled,
                           unsettled=unsettled, invalid=invalid, identity=self.identity_at_start,
                           term_delivery=self.term_delivery, out_bytes=self.out_total,
                           quarantine_receipt=self.quarantine_receipt_state,
                           exit_after_launch_s=None if self.exit_observed_mono is None
                           else round(self.exit_observed_mono - self.popen_call_mono, 4),
                           settled_after_launch_s=round(done - self.popen_call_mono, 4))
        if len(HELPER_LOG) < LIST_MAX:
            HELPER_LOG.append(self.record)
        if not self.settled:
            latch("metadata helper not settled: %r" % (unsettled,))
            raise RuntimeError("metadata helper not settled")
        if invalid:
            if self.stop == "owner_cancel_sigterm":
                raise HelperRefused("helper stopped by an owner cancel (settled; no timestamp)")
            latch("metadata helper output invalid: %r" % (invalid,))
            raise RuntimeError("metadata helper output invalid")
        return bytes(self.out).decode("ascii").strip()



class Child(Owned):
    """One owned native child: pre-allocated ownership, V7 launch/cancel boundary, own session, HARD capped capture
    created through the anchored run tree (N8), V4/N8 complete run-tree census before admission and after
    settlement, V6 independent descriptor cleanup, N1 identity-verified single group SIGTERM (Owned), N4 timing
    evidence: settled only if the settlement completes within its frozen tail; qualifying only if the exit was
    observed by the child's deadline; B1: a survivor of the bounded stop grace is recorded UNSETTLED (identities,
    live census, late obligations) and never waited for again."""

    def __init__(self, argv, label, wall, reserve, inputs, sink, cwd, feeder=None):
        self._owned_init()
        STATE["seq"] += 1
        self.seq = STATE["seq"]
        self.argv, self.label, self.sink_obj, self.cwd = argv, label, sink, cwd
        self.feeder = feeder                       # S2: owned stdin feeder (checker children only)
        self.filt = None if feeder is None else new_filter()  # S3
        base = os.path.join(STATE["out"], "children", "%02d-%s" % (self.seq, label))
        self.out_path, self.launch_path, self.settle_path = base + ".out", base + ".launch.json", base + ".settle.json"
        self.quarantine_path = base + ".QUARANTINE.json"
        self.captured, self.capture_written = 0, 0  # V13: non-dropped bytes vs bytes physically in the capped file
        self.over_cap, self.reader_error = False, None
        self.reader, self.settled_rec = None, None
        self.descendants = []
        self.inputs, self.reserve = inputs, reserve
        self.refused = None
        self.fd_errors = []
        charge_output(LOG_CAP)                     # V2: the capped capture file is pre-charged in full
        self.capture = os.fdopen(create_excl(self.out_path), "wb")   # N8: anchored; prepared BEFORE admission
        child_env = dict(CHILD_ENV, TMPDIR=cwd)    # r4#5: private TMPDIR inside the run tree
        try:
            self.tree_before = run_tree_census()   # V4: complete census before admission, for EVERY child
        except BaseException:
            self._close_refused_capture()
            raise
        now, mono = time.time(), time.monotonic()
        self.deadline = min(now + wall + GRACE, STATE["abs_end"] - SETTLE_TAIL)
        self.deadline_mono = min(mono + wall + GRACE, STATE["mono_end"] - SETTLE_TAIL)   # V3: elapsed cutoff
        why = full_admission(reserve, self.deadline, self.deadline_mono)
        if why:
            self._close_refused_capture()
            self.refused = why
            return
        OWNED.append(self)  # r3#1: ownership exists before the process does
        self.launch_order = next(ORDER)            # V7: launch/cancel boundary, drawn BEFORE the final check
        if LATCH or STATE["cancel_order"] is not None or time.time() + wall > self.deadline \
                or time.monotonic() + wall > self.deadline_mono:
            OWNED.remove(self)
            self._close_refused_capture()
            self.refused = ["final pre-spawn check: latch=%r cancel_order=%r launch_order=%d deadline_close=%r"
                            % (bool(LATCH), STATE["cancel_order"], self.launch_order,
                               time.time() + wall > self.deadline or time.monotonic() + wall > self.deadline_mono)]
            return
        self.popen_call_mono = time.monotonic()    # N4/N10: lower bound of the process start
        try:
            self.proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL if feeder is None else feeder.rfd,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         start_new_session=True, close_fds=True, cwd=cwd, env=child_env)
        except BaseException:
            OWNED.remove(self)                     # V6: no process exists; release ownership and the capture
            self._close_refused_capture()
            raise
        try:
            self.pid = self.pgid = self.proc.pid   # V6: ownership fields first, before any fallible step
            self.started_mono, self.started_epoch = time.monotonic(), time.time()
            if feeder is not None:
                feeder.close_read()                # S2: from here only the checker holds the read end
            self.identity_at_start = identity_checked(self.pid, os.getpid())   # N1: the stop needs it
            write_x(self.launch_path, {"seq": self.seq, "label": label, "runner_pid": os.getpid(), "pid": self.pid,
                                       "pgid": self.pgid, "identity": self.identity_at_start, "argv": argv,
                                       "cwd": cwd, "start_epoch": self.started_epoch, "launch_order": self.launch_order,
                                       "cancel_order_at_launch": STATE["cancel_order"],
                                       "absolute_deadline_epoch": self.deadline,
                                       "elapsed_deadline_s": round(self.deadline_mono - STATE["mono0"], 3),
                                       "capture": self.out_path, "capture_cap": LOG_CAP,
                                       "retained_reservation_bytes": reserve, "lane_ledger": STATE["last_ledger"],
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
            if feeder is not None and not feeder.started:
                self.fd_errors += feeder.abandon()   # V6: never-started endpoints closed BEFORE reaping (child sees EOF)
            try:
                latch("post-Popen registration failure %r" % (exc,))
            except BaseException:
                pass
            self.reap_owned(TERM_WAIT)             # N1: verified group stop only; unverifiable -> UNSETTLED
            raise

    def _close_refused_capture(self):
        try:
            self.capture.close()
        except Exception as exc:
            self.fd_errors.append("capture close %r" % (exc,))
            latch("refused child capture close failed %r" % (exc,))

    def _keep(self, b):
        room = LOG_CAP - self.capture_written
        if room > 0:
            chunk = b[:room]
            self.capture.write(chunk)
            self.capture_written += len(chunk)
        self.captured += len(b)
        if self.captured > LOG_CAP:
            self.over_cap = True

    def _read(self):
        """Capped capture.  S3: for a checker child the raw stream is hashed/counted in-stream and ONLY lines that
        fullmatch DUP_LINE at a genuine line start are dropped (counted by phase and bytes); V8: after an over-long
        partial line is flushed, the rest of that physical line is kept unconditionally."""
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
                    if f["cont"]:                  # V8: tail of a flushed physical line, never a whole line
                        f["cont"] = False
                        self._keep(ln)
                        continue
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
                    f["cont"] = True
                    f["flushes"] += 1
            if f is not None and f["pending"]:
                f["tail"] = len(f["pending"])
                self._keep(f["pending"])
                f["pending"] = b""
        except Exception as exc:
            self.reader_error = repr(exc)
        finally:
            for what, fn in (("flush", self.capture.flush), ("fsync", lambda: os.fsync(self.capture.fileno())),
                             ("capture close", self.capture.close), ("stdout close", self.proc.stdout.close)):
                try:
                    fn()                           # V6: every cleanup step independent
                except Exception as exc:
                    self.reader_error = (self.reader_error or "") + " %s:%r" % (what, exc)

    def late_obligations(self):
        """B1: paths and pipes an unreaped child can still touch after the runner returns (published with UNSETTLED)."""
        obl = [{"path": self.cwd, "kind": "dir", "note": "the child's cwd and TMPDIR: may gain entries"},
               {"path": self.out_path, "kind": "file", "note": "capture: written only by this runner's reader thread, "
                                                                "which ends when the runner returns"},
               {"what": "stdout/stderr pipe", "note": "the runner's read end closes when it returns; EPIPE/SIGPIPE"}]
        if self.feeder is not None:
            obl.append({"what": "stdin pipe", "note": "the runner's write end closes when it returns (EOF)"})
        if self.sink_obj is not None:
            obl.append({"path": self.sink_obj.fifo_path, "kind": "fifo",
                        "note": "proof FIFO: the child may still hold its write end"})
            fp = getattr(self.sink_obj, "file_path", None)
            if fp is not None:
                obl.append({"path": fp, "kind": "file", "note": "partial proof file: written only by this runner's "
                                                                "collector thread, which ends when the runner returns"})
        return obl

    def alive(self):
        return self.observe_exit() is None

    def census(self):
        """V1: owned-process census through libproc (no /bin/ps): descendants of the child (own group + PPID
        closure) and the resident bytes of the child plus every listed descendant; N12: None if ANY of them is
        unreadable (never mapped to zero).  Raises on a failed listing (the monitor trips)."""
        found = descendants(self.pid, self.pgid)
        rss = task_rss(self.pid)
        for d in found:
            r = task_rss(d)
            rss = None if (rss is None or r is None) else rss + r
        return found, rss

    def timing(self):
        """N4/N10: monotonic evidence relative to the run start, plus epoch exit/deadline values."""
        rel = lambda t: None if t is None else round(t - STATE["mono0"], 4)   # noqa: E731
        return {"popen_call_s": rel(self.popen_call_mono), "started_s": rel(self.started_mono),
                "last_alive_s": rel(self.last_alive_mono), "exit_observed_s": rel(self.exit_observed_mono),
                "deadline_s": rel(self.deadline_mono), "exit_observed_epoch": self.exit_observed_epoch,
                "deadline_epoch": self.deadline}

    def settle(self):
        """Always reaches wait(); settlement final only after streams, transport endpoints, sink, cwd/run-tree
        checks, hashes, N8 confinement and the receipt; every cleanup outcome is incorporated BEFORE the record is
        published; N4: settled requires completion within the child's deadline + SETTLE_TAIL (monotonic and
        epoch), and the record states whether the exit was observed by the deadline; any failure clears
        'settled' and latches."""
        if self.settled_rec is not None:
            return self.settled_rec
        problems = []
        rc = self.reap_owned(TERM_WAIT)            # B1: bounded; None = survivor recorded UNSETTLED
        if rc is None:
            problems.append("not reaped within the bounded stop grace: UNSETTLED (reservation retained; parent "
                            "disposition)")
        if self.quarantined and self.quarantine_receipt_state != "written":
            problems.append("UNSETTLED receipt not published (%s)" % self.quarantine_receipt_state)
        if self.quarantined:
            problems.append("UNSETTLED: chunk claim voided, parent disposition")
        if self.term_refused_mono is not None:
            problems.append("stop refused: identity unverifiable (UNSETTLED)")
        stream_alive = None
        if self.reader is not None and self.reader.ident is not None:
            self.reader.join(STREAM_JOIN)
            stream_alive = self.reader.is_alive()
        else:
            problems.append("no started capture reader")  # r6#2: explicit settlement failure
            for what, fn in (("stdout close", self.proc.stdout.close), ("capture close", self.capture.close)):
                try:
                    fn()                           # V6: independent closes
                except Exception as exc:
                    problems.append("%s %r" % (what, exc))
        if self.reader_error is not None:
            problems.append("capture reader error %s" % self.reader_error)
        feed_rec = filt_rec = None
        if self.feeder is not None:
            if not self.feeder.started:
                self.fd_errors += self.feeder.abandon()   # V6: before the record is published
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
                            "dup_lines_above_header_clauses": f["dup_high"], "nondropped_bytes": self.captured,
                            "capture_file_bytes": self.capture_written, "unterminated_tail_bytes": f["tail"],
                            "over_long_line_flushes": f["flushes"]}
        if self.fd_errors:
            problems.append("descriptor close errors %r" % self.fd_errors)
        group_empty = None
        try:
            group_empty = list_pids(PROC_PGRP_ONLY, self.pgid) == []   # V1: zombies are listed too
            if not group_empty:
                problems.append("process group not empty after reap")
        except BaseException as exc:
            problems.append("group census failed %r" % exc)
        try:
            after = descendants(self.pid, self.pgid)
            if after:
                problems.append("descendants after reap %r" % after[:10])
        except BaseException as exc:
            problems.append("post-reap census failed %r" % exc)
        if self.descendants:
            problems.append("descendants seen during run %r" % self.descendants[:5])
        sink_rec = None
        if self.sink_obj is not None:
            try:
                sink_rec = self.sink_obj.finish()
                if not sink_rec["sink_settled"]:
                    problems.append("proof collector not settled")
            except BaseException as exc:
                problems.append("collector finish failed %r" % exc)
        try:
            listing = os.listdir(TREE[self.cwd][0])   # N8: through the anchored cwd descriptor
            if listing:
                problems.append("child cwd not empty: %r" % listing[:10])
        except BaseException as exc:
            problems.append("cwd check failed %r" % exc)
        try:
            expected = {self.out_path, self.launch_path, self.settle_path, self.quarantine_path}  # S1: no proof file
            if self.sink_obj is not None:
                expected.add(self.sink_obj.fifo_path)     # N8: a written FIFO's times change
            now = run_tree_census()
            changed = sorted(p for p in set(now) | set(self.tree_before)
                             if p not in expected and now.get(p) != self.tree_before.get(p))
            if changed:
                problems.append("unexpected run-tree changes (added/changed/removed) %r" % changed[:10])
        except BaseException as exc:
            problems.append("run-tree census failed %r" % exc)
        problems += confinement_refusals()                # N8
        diag = []
        out_sha = None
        if stream_alive is False:
            try:
                out_sha, out_len = sha_tree(self.out_path, limit=LOG_CAP)
                if out_len != self.capture_written:
                    problems.append("capture file bytes %d != written %d" % (out_len, self.capture_written))
                else:
                    register_written(self.out_path, out_sha, out_len)
                text = read_tree(self.out_path, LOG_CAP).decode("utf-8", "replace")
                diag = sorted(set(m.group(0) for m in RESOURCE_DIAG.finditer(text)))
            except BaseException as exc:
                problems.append("capture hash/scan failed %r" % exc)
        if diag:
            latch("native memory diagnostic in %s: %r" % (self.label, diag))  # r3#3
        exit_by_deadline = (self.exit_observed_mono is not None and self.exit_observed_mono <= self.deadline_mono
                            and self.exit_observed_epoch <= self.deadline)
        done_mono, done_epoch = time.monotonic(), time.time()       # N4: settlement completion (before publication)
        if done_mono > self.deadline_mono + SETTLE_TAIL or done_epoch > self.deadline + SETTLE_TAIL:
            problems.append("settlement completed after the child deadline + SETTLE_TAIL")
        timing = dict(self.timing(), settle_done_s=round(done_mono - STATE["mono0"], 4),
                      cleanup_s=None if self.exit_observed_mono is None else round(done_mono - self.exit_observed_mono, 4))
        rec = {"seq": self.seq, "label": self.label, "pid": self.pid, "pgid": self.pgid,
               "identity_at_start": self.identity_at_start, "argv": self.argv, "returncode": rc,
               "stop": self.stop or "self", "term_delivery": self.term_delivery, "unsettled": self.unsettled,
               "stop_refused": self.term_refused_mono is not None,
               "seconds": round(time.time() - self.started_epoch, 3), "timing": timing,
               "exit_observed_by_deadline": exit_by_deadline,
               "launch_order": self.launch_order, "cancel_order": STATE["cancel_order"],
               "nondropped_bytes": self.captured, "capture_file_bytes": self.capture_written,
               "capture_over_cap": self.over_cap, "reader_error": self.reader_error,
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
    """Capture lines (CR or LF separated), read through the anchored run tree (N8), bounded by LOG_CAP (N7)."""
    txt = read_tree(path, LOG_CAP).decode("utf-8", "replace")
    return [s for s in re.split(r"[\r\n]", txt) if s != ""]


def supervise(child, sink):
    """Monitor until exit or a single stop request; any monitor exception is itself a trip.  V1: census and RSS
    through libproc; V3/N7: absolute AND elapsed (monotonic) deadlines; N4: last_alive_mono (taken BEFORE each
    poll that saw the child alive) and the exit observation (taken AFTER the poll that saw the exit) bound the
    exit time; V6: a capture reader error trips; N1: stops go through Child.term (one verified group SIGTERM)."""
    me = os.getpid()
    last_rss = last_reg = float("-inf")
    peak = 0
    while True:
        mono = time.monotonic()
        if child.observe_exit() is not None:
            break
        child.last_alive_mono = mono
        try:
            now = time.time()
            if cancelled():
                child.term("owner_cancel_sigterm")
            elif now > child.deadline or mono > child.deadline_mono:
                child.term("absolute_or_elapsed_deadline")
            elif sink is not None and sink.over_cap:
                child.term("proof_cap")
            elif sink is not None and sink.error:
                child.term("proof_sink_error")
            elif child.feeder is not None and child.feeder.exception is not None:
                child.term("feeder_exception")
            elif child.reader_error is not None:
                child.term("capture_reader_error")
            elif child.over_cap:
                child.term("capture_cap")
            elif free_bytes() < FREE_FLOOR:
                child.term("inflight_disk_floor")
            if not child.stop_requested() and mono - last_rss >= 1.0:
                last_rss = mono
                found, rss = child.census()
                runner_rss = task_rss(me)
                if found:
                    child.descendants.extend(found)
                    child.term("descendant_process")
                elif runner_rss is None or (rss is None and child.alive()):
                    child.term("rss_unreadable")
                else:
                    total = (rss or 0) + max(runner_rss, buffer_charge())  # S5/V5/N6: proof RAM charged in full
                    peak = max(peak, total)
                    if total > LANE_RSS_TRIP:
                        child.term("lane_rss")
            if not child.stop_requested() and mono - last_reg >= 5.0:
                last_reg = mono
                if registry_refusals():
                    child.term("stop_registry")
        except Exception as exc:
            child.term("monitor_exception:%r" % exc)
        if child.stop_requested():
            break
        time.sleep(SUPERVISE_SLICE)
    if child.stop is not None and child.stop not in NONLATCHING_TRIPS:
        latch("trip %s on %s" % (child.stop, child.label))
    return child.stop, peak


def run_child(argv, label, wall, reserve, inputs, sink=None, feeder=None):
    """Prepared outputs -> admission -> spawn -> supervise -> settle.  Returns (rec|None, lines, refusal)."""
    ch = None
    try:
        cwd = os.path.join(STATE["out"], "cwd", "%02d-%s" % (STATE["seq"] + 1, label))
        mkdir_anchored(cwd)  # r4#4: inside the cleanup guard; N8: exclusive and anchored
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
            errs = feeder.abandon()  # never-spawned checker: both pipe ends closed; V6: errors latch
            if errs:
                latch("never-started feeder endpoint close errors %r" % (errs,))



def settle_all():
    """r6#1/#2/B1: one BOUNDED pass over OWNED with the index iteration inside the retry guard.  Every owned child that
    has no settlement record gets settle() (itself bounded: a survivor of the stop grace is recorded UNSETTLED and
    returns); a child whose settle() keeps raising is recorded UNSETTLED (not reaped or bookkeeping failed) with
    the latch held after SETTLE_ALL_ATTEMPTS attempts; the pass itself ends after a bounded number of guard
    iterations.  Nothing is retried without bound and no settlement is synthesized."""
    i = failures = guard = 0
    while True:
        guard += 1
        if guard > SETTLE_ALL_ATTEMPTS * (len(OWNED) + 1) + SETTLE_ALL_ATTEMPTS:
            try:
                LATCH.append("settle_all exhausted its bounded attempts: UNSETTLED children remain")
            except BaseException:
                pass
            return
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
                    if failures < SETTLE_ALL_ATTEMPTS:
                        continue
                    c.settled_rec = {"seq": c.seq, "label": c.label, "pid": c.pid, "settled": False,
                                     "returncode": c.proc.returncode, "stop": c.stop, "unsettled": c.unsettled,
                                     "note": "settlement failed %d times: UNSETTLED (reservation retained; parent "
                                             "disposition)" % SETTLE_ALL_ATTEMPTS}
                    LATCH.append("child settlement failed %d times: UNSETTLED" % SETTLE_ALL_ATTEMPTS)
            i += 1
            failures = 0
        except BaseException:
            continue


def run_kissat(cnf_path, label, seconds, cap, reserve, inputs, owner):
    """kissat -q -f --seed=1 --time=S CNF [PROOF_FIFO]; with a cap the proof goes ONLY to a RAM ProofBuffer (S1).
    N6: a created ProofBuffer is appended to the caller's `owner` list at creation, so the caller's finally
    releases it on every path, including an exception before this function returns.
    Returns (rec|None, lines, refusal, buffer|None)."""
    argv = [KISSAT[0], "-q", "-f", "--seed=1", "--time=%d" % seconds, cnf_path]
    sink = None
    if cap is not None:
        sink = ProofBuffer(os.path.join(STATE["out"], "fifo", label + ".proof.fifo"), cap)
        owner.append(sink)
        argv.append(sink.fifo_path)
    rec, lines, refused = run_child(argv, label + ".kissat", seconds, reserve,
                                    dict(inputs, proof_storage=None if sink is None else "RAM only", proof_cap=cap),
                                    sink)
    return rec, lines, refused, sink


def run_check(cnf_path, buf, checker, label, seconds, reserve, inputs, mode="plain"):
    """S2: one pinned checker [DRAT_X, CNF, -i, -t S] with the frozen RAM buffer on stdin via an owned Feeder;
    the binary is re-hashed when its child is prepared."""
    name, path, pin = checker
    if sha_file(path)[0] != pin:
        latch("checker %s binary pin mismatch at spawn" % name)
        raise RuntimeError("checker %s binary pin mismatch" % name)
    if buf.released:
        raise RuntimeError("proof buffer already released")
    feeder = Feeder(buf.blocks, mode, label="%s.drat%s" % (label, name))
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


FORBIDDEN = (("early EOF", "EARLY_EOF"), ("clauses less than expected", "LESS_THAN_EXPECTED"),
             ("trivial UNSAT", "TRIVIAL_UNSAT"), ("ERROR", "ERROR"), ("MEMOUT", "MEMOUT"),
             ("wrong binary prefix", "WRONG_PREFIX"), ("no empty clause detected", "NO_EMPTY_CLAUSE"),
             ("NOT VERIFIED", "NOT_VERIFIED"), ("TIMEOUT", "TIMEOUT"), ("illegal literal", "ILLEGAL_LITERAL"),
             ("error opening", "ERROR_OPENING"), ("failed to reallocate", "FAILED_REALLOC"))


def defect(code, text):
    """V10: every defect carries a stable ID: 'ID: text'."""
    return "%s: %s" % (code, text)


def defect_ids(defects):
    """V10: the complete, sorted list of stable defect IDs (the comparison key of controls and tests)."""
    return sorted(d.split(": ", 1)[0] for d in defects)


def checker_defects(name, cnf_expect, buf_sha, buf_bytes, drat_rec, drat_lines):
    """S4/V9/V10: per-checker P-STREAM qualification with canonical (unique) parser records; every defect ID is
    prefixed with the checker name."""
    bad = []
    X = name + "."
    feed = drat_rec.get("stdin_feed") or {}
    filt = drat_rec.get("stdout_filter") or {}
    if drat_rec.get("returncode") != 0 or drat_rec.get("stop") != "self":
        bad.append(defect(X + "EXIT", "checker not self-exit rc0"))
    st = status_lines(drat_lines)
    if st != ["s VERIFIED"]:
        bad.append(defect(X + "STATUS", "status lines %r != ['s VERIFIED']" % (st,)))
    v, c = cnf_expect[2].split()[2:4]
    hdr = [s[:200] for s in drat_lines if s.startswith("c parsing input formula")]
    if hdr != ["c parsing input formula with %s variables and %s clauses" % (v, c)]:
        bad.append(defect(X + "HEADER", "parser header records %r != the CNF pin header" % (hdr[:4],)))
    rd = [s[:200] for s in drat_lines if s.startswith("c reading proof")]
    if rd != [STDIN_LINE]:
        bad.append(defect(X + "STDIN", "stdin records %r != [%r]" % (rd[:4], STDIN_LINE)))
    if feed.get("mode") != "plain":
        bad.append(defect(X + "FEED_MODE", "feed mode %r is not plain" % (feed.get("mode"),)))
    if feed.get("fed_bytes") != buf_bytes or feed.get("fed_sha256") != buf_sha or feed.get("proof_bytes_fed") != buf_bytes:
        bad.append(defect(X + "FEED_DIGEST", "fed bytes/SHA-256 != collected proof buffer"))
    if feed.get("started") is not True or feed.get("delivery_error") is not None or feed.get("exception") is not None \
            or feed.get("close_error") is not None or feed.get("thread_alive_after_join") is not False:
        bad.append(defect(X + "FEED_STATE", "stdin feed incomplete, failed or unsettled"))
    fb = feed.get("fed_bytes")
    fin = [s[:200] for s in drat_lines if s.startswith("c finished parsing")]
    if not isinstance(fb, int) or isinstance(fb, bool) or fin != ["c finished parsing, read %d bytes from proof file" % fb]:
        bad.append(defect(X + "CONSUMED", "consumed records %r != [read %r bytes]" % (fin[:4], fb)))
    nd = drat_rec.get("nondropped_bytes")
    if filt.get("raw_eof") is not True or not isinstance(filt.get("dup_bytes_dropped"), int) or not isinstance(nd, int) \
            or isinstance(nd, bool) or filt.get("raw_bytes") != nd + filt["dup_bytes_dropped"]:
        bad.append(defect(X + "FILTER", "checker output filter accounting mismatch"))
    for pat, key in FORBIDDEN:
        if any(pat in s for s in drat_lines):
            bad.append(defect(X + "FORBIDDEN." + key, "checker output contains %r" % pat))
    if not drat_rec.get("settled") or drat_rec.get("capture_over_cap") is not False:
        bad.append(defect(X + "SETTLE", "settlement/capture defect seq %s" % drat_rec.get("seq")))
    if drat_rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect(X + "TIMING", "exit not observed by the checker deadline (N4)"))
    return bad



def qualify_stream(cnf_expect, solver_rec, kissat_lines, proof_cap, checks, cnf_post, buf_post):
    """S4/V9/V10: item-level qualification over the solver leg (complete output exactly ['s UNSATISFIABLE']), the
    RAM buffer and every pinned checker in order; checks = [(name, drat_rec, drat_lines), ...].  UNSAT requires []."""
    bad = []
    if solver_rec.get("returncode") != 20 or solver_rec.get("stop") != "self":
        bad.append(defect("SOLVER_EXIT", "solver not self-exit rc20"))
    if kissat_lines != ["s UNSATISFIABLE"]:
        bad.append(defect("SOLVER_OUTPUT", "complete solver output %r != ['s UNSATISFIABLE']" % (kissat_lines[:4],)))
    buf = solver_rec.get("proof_sink") or {}
    if not sink_complete(solver_rec.get("proof_sink")):
        bad.append(defect("BUFFER_INCOMPLETE", "proof buffer incomplete/over cap/error"))
    buf_sha, buf_bytes = buf.get("sha256_of_retained"), buf.get("retained")
    if not isinstance(buf_bytes, int) or isinstance(buf_bytes, bool) or buf_bytes <= 0 or buf_bytes > proof_cap:
        bad.append(defect("BUFFER_SIZE", "proof size outside (0, cap]"))
    if [c[0] for c in checks] != [c[0] for c in CHECKERS]:
        bad.append(defect("CHECKER_SET", "not every pinned checker ran, in order"))
    for name, rec, lines in checks:
        bad += checker_defects(name, cnf_expect, buf_sha, buf_bytes, rec, lines)
    if cnf_post != (cnf_expect[0], cnf_expect[1]):
        bad.append(defect("CNF_POST", "CNF file digest/bytes != expected"))
    if buf_post != [buf_sha, buf_bytes]:
        bad.append(defect("BUFFER_POST", "proof buffer re-hash after the checks != collector measurement"))
    if not solver_rec.get("settled") or solver_rec.get("capture_over_cap") is not False:
        bad.append(defect("SOLVER_SETTLE", "settlement/capture defect seq %s" % solver_rec.get("seq")))
    if solver_rec.get("exit_observed_by_deadline") is not True:
        bad.append(defect("SOLVER_TIMING", "exit not observed by the solver deadline (N4)"))
    return bad



def verify_sat(cnf_path, kissat_lines, label):
    """Two independent checks of a SAT model: clause satisfaction and both PA19 definitions."""
    lits = set()
    for s in kissat_lines:
        if s.startswith("v "):
            lits.update(int(x) for x in s[2:].split() if x != "0")
    sat_all = True
    dfd, name = tree_path(cnf_path)                # N8: anchored read of the run-tree CNF
    fd, _st = open_regular(name, dfd)
    with os.fdopen(fd, "rb") as f:
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
    """A control child must have exited by itself (rc>=0), with no trip, fully settled, no resource diagnostic,
    and (N4) its exit observed by its deadline."""
    return rec is not None and rec["stop"] == "self" and rec["settled"] and not rec["capture_over_cap"] \
        and rec["returncode"] is not None and rec["returncode"] >= 0 and not rec["resource_diagnostics"] \
        and rec.get("exit_observed_by_deadline") is True


def c6_timer_refusals(rec, lines):
    """N10: C6 intended cause = expiry of kissat's --time=CONTROL_TIMER_S timer, bound to monotonic execution
    evidence rather than cleanup-inclusive wall time: healthy self-exit rc 0 with complete output exactly
    ['s UNKNOWN']; runtime lower bound (last_alive - started: the process was seen alive at last_alive and had
    started before started) >= C6_MIN_RUN_S; runtime upper bound (exit_observed - popen_call) <= C6_MAX_RUN_S.
    Cleanup time is recorded separately and plays no role.  Returns refusal reasons ([] = intended)."""
    why = []
    if not healthy(rec) or rec.get("returncode") != 0:
        why.append("not a healthy rc-0 self-exit observed by its deadline")
    if lines != ["s UNKNOWN"]:
        why.append("complete output %r != ['s UNKNOWN']" % (lines[:4],))
    t = rec.get("timing") or {}
    nums = [t.get(k) for k in ("popen_call_s", "started_s", "last_alive_s", "exit_observed_s")]
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in nums):
        why.append("monotonic timing evidence incomplete %r" % (nums,))
    else:
        popen_call, started, last_alive, exit_obs = nums
        if last_alive - started < C6_MIN_RUN_S:
            why.append("runtime lower bound %.3f s < %.1f s" % (last_alive - started, C6_MIN_RUN_S))
        if exit_obs - popen_call > C6_MAX_RUN_S:
            why.append("runtime upper bound %.3f s > %.1f s" % (exit_obs - popen_call, C6_MAX_RUN_S))
    return why


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
    """S6/V11: same-binary positive and intended-reason controls through the RAM/stdin transport for BOTH pinned
    checkers.  Each checker's intended predicate is evaluated before the next child is launched; C2/C3/C4 compare
    complete defect-ID sets; C6/C7/C7b are bound to the pinned binaries' measured or source-stated diagnostics.
    Stops at the first refused, unhealthy or not-as-intended control (later controls are not started).  V5/N6:
    every control buffer is owned by `bufs` from its creation (run_kissat) and released in the finally.  N10: C6
    is bound to monotonic execution evidence of the --time=CONTROL_TIMER_S expiry (c6_timer_refusals)."""
    recs = {}
    bufs = []
    d = os.path.join(STATE["out"], "controls")    # N8: created and anchored with the run tree
    per_child = LOG_CAP + 3 * RECORD_MAX

    def fail(name, why):
        recs[name] = dict(recs.get(name, {}), failed=why)
        return False, recs

    def checked(tag, cnf_path, pins, buf, mode, predicate):
        out = []
        for chk in CHECKERS:
            dr, dl, rf = run_check(cnf_path, buf, chk, tag, CONTROL_CHILD_WALL, per_child, pins, mode)
            if dr is None:
                return out, "checker %s refused %r" % (chk[0], rf)
            out.append((chk[0], dr, dl))
            why = predicate(chk[0], dr, dl)
            if why:
                return out, "checker %s: %s" % (chk[0], why)   # V11: the next checker is never launched
        return out, None

    def view(checks):
        return {n: {"drat": r, "checker_status_lines": status_lines(l)} for n, r, l in checks}

    try:
        raw = php_cnf(6, 5)
        cnf = os.path.join(d, "php6x5.cnf")
        h, n = write_bytes_x(cnf, raw)
        exp = (h, n, raw.split(b"\n", 1)[0].decode())
        ks, kl, rf, b1 = run_kissat(cnf, "C1", CONTROL_CHILD_WALL, CONTROL_PROOF_CAP, per_child, {"cnf_pin": [h, n]},
                                    bufs)
        if ks is None:
            return fail("C1_positive_php6x5", "refused %r" % rf)
        recs["C1_positive_php6x5"] = {"kissat": ks, "kissat_lines": kl[:8]}
        if not (healthy(ks) and ks["returncode"] == 20 and kl == ["s UNSATISFIABLE"] and sink_complete(ks["proof_sink"])):
            return fail("C1_positive_php6x5", "solver leg not exactly rc20 ['s UNSATISFIABLE'], unhealthy or buffer incomplete")
        ph, pn = ks["proof_sink"]["sha256_of_retained"], ks["proof_sink"]["retained"]
        pins = {"cnf_pin": [h, n], "proof_pin": [ph, pn]}

        def positive(name, r, l):
            ids = defect_ids(checker_defects(name, exp, ph, pn, r, l))
            return None if ids == [] and completed_checker(r, l, "VERIFIED") else "positive predicate failed %r" % ids

        c1k, why = checked("C1", cnf, pins, b1, "plain", positive)
        recs["C1_positive_php6x5"]["checkers"] = view(c1k)
        if why:
            return fail("C1_positive_php6x5", why)
        c1 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c1k, sha_tree(cnf), b1.digest())
        recs["C1_positive_php6x5"].update(intended="PASS: qualify_stream == [] through checker A then checker B", defects=c1)
        if c1 != []:
            return fail("C1_positive_php6x5", "positive control did not pass %r" % defect_ids(c1))
        # C2 (deterministic): same header and clause count, first clause missing one literal; the deterministic
        # PHP(6,5) proof stays VERIFIED (measured in every earlier run), so the ONLY item defect is CNF_POST.
        lines = raw.split(b"\n")
        first = lines[1].split()
        mutated = b"\n".join([lines[0], b" ".join(first[:-2] + first[-1:])] + lines[2:])
        cnf2 = os.path.join(d, "php6x5-one-literal-removed.cnf")
        h2, n2 = write_bytes_x(cnf2, mutated)
        c2k, why = checked("C2", cnf2, {"cnf_pin": [h2, n2], "proof_pin": [ph, pn]}, b1, "plain", positive)
        recs["C2_mutated_cnf_digest"] = {"intended": "each checker completed 's VERIFIED' with no checker defect; item "
                                                     "defect IDs exactly ['CNF_POST']", "checkers": view(c2k)}
        if why:
            return fail("C2_mutated_cnf_digest", why)
        c2 = qualify_stream(exp, ks, kl, CONTROL_PROOF_CAP, c2k, sha_tree(cnf2), b1.digest())
        recs["C2_mutated_cnf_digest"]["defects"] = c2
        if defect_ids(c2) != ["CNF_POST"]:
            return fail("C2_mutated_cnf_digest", "item defect IDs %r != ['CNF_POST']" % defect_ids(c2))
        # C3: the valid proof + one trailing byte appended IN TRANSIT.
        def suffix_reject(name, r, l):
            ids = defect_ids(checker_defects(name, exp, ph, pn, r, l))
            want = sorted(name + "." + k for k in ("FEED_MODE", "FEED_DIGEST", "CONSUMED", "FORBIDDEN.WRONG_PREFIX"))
            if ids != want or not completed_checker(r, l, "VERIFIED") \
                    or (r.get("stdin_feed") or {}).get("fed_bytes") != pn + len(SUFFIX):
                return "suffix predicate failed: IDs %r != %r or not completed/fed+1" % (ids, want)
            return None

        c3k, why = checked("C3", cnf, pins, b1, "suffix", suffix_reject)
        recs["C3_trailing_proof_byte"] = {"intended": "per checker: completed 's VERIFIED', checker defect IDs exactly "
                                                      "{FEED_MODE, FEED_DIGEST, CONSUMED, FORBIDDEN.WRONG_PREFIX}, fed == "
                                                      "buffer + 1", "checkers": view(c3k)}
        if why:
            return fail("C3_trailing_proof_byte", why)
        # C4: satisfiable PHP(5,5) with the PHP(6,5) proof.
        raw4 = php_cnf(5, 5)
        cnf4 = os.path.join(d, "php5x5-sat.cnf")
        h4, n4 = write_bytes_x(cnf4, raw4)
        exp4 = (h4, n4, raw4.split(b"\n", 1)[0].decode())

        def foreign_reject(name, r, l):
            ids = defect_ids(checker_defects(name, exp4, ph, pn, r, l))
            want = sorted(name + "." + k for k in ("EXIT", "STATUS", "FORBIDDEN.NOT_VERIFIED"))
            if ids != want or not completed_checker(r, l, "NOT VERIFIED"):
                return "foreign-proof predicate failed: IDs %r != %r or not completed 's NOT VERIFIED' rc1" % (ids, want)
            return None

        c4k, why = checked("C4", cnf4, {"cnf_pin": [h4, n4], "proof_pin": [ph, pn]}, b1, "plain", foreign_reject)
        recs["C4_sat_formula_foreign_proof"] = {"intended": "per checker: completed exactly ['s NOT VERIFIED'] rc1, "
                                                            "checker defect IDs exactly {EXIT, STATUS, "
                                                            "FORBIDDEN.NOT_VERIFIED}", "checkers": view(c4k)}
        if why:
            return fail("C4_sat_formula_foreign_proof", why)
        # C5: HARD RAM proof cap 4096 B on PHP(11,10).
        raw5 = php_cnf(11, 10)
        cnf5 = os.path.join(d, "php11x10.cnf")
        h5, n5 = write_bytes_x(cnf5, raw5)
        ks5, kl5, rf, b5 = run_kissat(cnf5, "C5", CONTROL_CHILD_WALL, 4096, per_child, {"cnf_pin": [h5, n5]}, bufs)
        if ks5 is None:
            return fail("C5_proof_hard_cap", "refused %r" % rf)
        ps5 = ks5["proof_sink"] or {}
        recs["C5_proof_hard_cap"] = {"intended": "stop=proof_cap, retained<=4096 B, received == retained + discarded > "
                                                 "retained, settled, over_cap, collector joined", "kissat": ks5}
        if not (ks5["stop"] == "proof_cap" and ps5.get("retained", 4097) <= 4096 and ps5.get("over_cap")
                and ps5.get("discarded", 0) > 0 and ps5.get("received") == ps5.get("retained", 0) + ps5.get("discarded", 0)
                and ks5["settled"] and ps5.get("thread_alive_after_join") is False and not ks5["resource_diagnostics"]):
            return fail("C5_proof_hard_cap", "intended reason or settlement missing")
        # C6: kissat --time=CONTROL_TIMER_S, no proof, on PHP(13,12): N10 timer expiry bound to monotonic
        # execution evidence (runtime in [C6_MIN_RUN_S, C6_MAX_RUN_S]), rc 0 and exactly ['s UNKNOWN'].
        raw6 = php_cnf(13, 12)
        cnf6 = os.path.join(d, "php13x12.cnf")
        h6, n6 = write_bytes_x(cnf6, raw6)
        ks6, kl6, rf, _ = run_kissat(cnf6, "C6", CONTROL_TIMER_S, None, per_child, {"cnf_pin": [h6, n6]}, bufs)
        if ks6 is None:
            return fail("C6_native_time_limit", "refused %r" % rf)
        why6 = c6_timer_refusals(ks6, kl6)
        recs["C6_native_time_limit"] = {"intended": "healthy self-exit rc 0, complete output exactly ['s UNKNOWN'], "
                                                    "monotonic runtime lower bound >= %.1f s and upper bound <= %.1f "
                                                    "s for --time=%d (runs 008/010/012 at --time=1: rc 0, "
                                                    "'s UNKNOWN')" % (C6_MIN_RUN_S, C6_MAX_RUN_S, CONTROL_TIMER_S),
                                        "kissat": ks6, "kissat_lines": kl6[:8], "refusals": why6}
        if why6:
            return fail("C6_native_time_limit", "intended timer-expiry outcome missing %r" % (why6,))
        # C7: missing input with a RAM proof buffer: kissat's missing-input diagnostic, collector unblocked and joined.
        absent = os.path.join(d, "absent.cnf")
        ks7, kl7, rf, b7 = run_kissat(absent, "C7", 10, CONTROL_PROOF_CAP, per_child, {"cnf_pin": None}, bufs)
        if ks7 is None:
            return fail("C7_no_input_sink_liveness", "refused %r" % rf)
        ps7 = ks7["proof_sink"] or {}
        want7 = ["kissat: error: can not read '%s'" % absent]
        recs["C7_no_input_sink_liveness"] = {"intended": "healthy self-exit rc 1, complete output exactly %r (runs "
                                                         "008/010/012), collector unblocked by the runner, 0 bytes, "
                                                         "joined" % want7, "kissat": ks7, "kissat_lines": kl7[:8]}
        if not (healthy(ks7) and ks7["returncode"] == 1 and kl7 == want7 and ps7.get("unblocked_by_runner") is True
                and ps7.get("retained") == 0 and ps7.get("thread_alive_after_join") is False):
            return fail("C7_no_input_sink_liveness", "intended missing-input outcome or collector settlement missing")
        # C7b: missing CNF for each checker with a HELD feed: drat-trim.c:1425-1427 prints exactly
        # 'c error opening "<path>".' and returns ERROR (-1, exit status 255) before reading stdin; the feeder then
        # meets a closed read end (EPIPE, 0 bytes fed); every thread settles.
        absent2 = os.path.join(d, "absent-checker.cnf")
        want7b = ['c error opening "%s".' % absent2]

        def missing_input(name, r, l):
            f7 = r.get("stdin_feed") or {}
            if not (healthy(r) and r["returncode"] == 255 and l == want7b and f7.get("fed_bytes") == 0
                    and str(f7.get("delivery_error")).startswith("EPIPE") and f7.get("hold_released_by_event") is True
                    and f7.get("thread_alive_after_join") is False):
                return "missing-input predicate failed (rc %r, lines %r, feed %r)" % (r.get("returncode"), l[:4],
                                                                                    {k: f7.get(k) for k in ("fed_bytes", "delivery_error")})
            return None

        c7k, why = checked("C7b", absent2, {"cnf_pin": None, "proof_pin": [ph, pn]}, b1, "hold", missing_input)
        recs["C7b_checker_no_input_feed_liveness"] = {"intended": "per checker: healthy self-exit rc 255, complete output "
                                                                  "exactly %r, held feed EPIPE with 0 bytes fed, hold "
                                                                  "released by the reap, feeder joined" % want7b,
                                                      "checkers": view(c7k)}
        if why:
            return fail("C7b_checker_no_input_feed_liveness", why)
        return True, recs
    finally:
        for b in bufs:
            if b is not None:
                b.release()
        recs["buffer_accounting"] = [b.accounting() for b in bufs if b is not None]



def cutoff_refusals():
    """N4: the frozen run cutoffs (elapsed and absolute) have not passed."""
    why = []
    if STATE["mono_end"] is None or time.monotonic() > STATE["mono_end"]:
        why.append("after the frozen elapsed cutoff")
    if STATE["abs_end"] is None or time.time() > STATE["abs_end"]:
        why.append("after the frozen absolute cutoff")
    return why


def terminal_gate():
    """Registry, disk, N3 lane ledger, N8 confinement and N4 cutoff evidence collected BEFORE the commit boundary;
    any failure latches."""
    why = []
    try:
        why += registry_refusals()
        if free_bytes() < FREE_FLOOR:
            why.append("free below in-flight floor at terminal gate")
        why += ledger_refusals()[0]
        why += confinement_refusals()
        why += cutoff_refusals()
    except Exception as exc:
        why.append("terminal gate exception %r" % exc)
    for w in why:
        latch("terminal gate: " + w)
    return why


def commit_record(path, rec_unknown, rec_unsat):
    """Explicit commit boundary.  Both serializations exist and N5 the larger one is charged to the output guard
    before the anchored O_EXCL fd (N8) is created; N4 the frozen cutoffs are re-checked (a late commit latches,
    so only UNKNOWN can be chosen); the boundary is one atomic next(ORDER); a cancel stamped before it (or any
    latch) forces UNKNOWN."""
    unknown_bytes = serialize(rec_unknown)
    unsat_bytes = None if rec_unsat is None else serialize(rec_unsat)
    charge_output(max(len(unknown_bytes), len(unsat_bytes or b"")))
    fd = create_excl(path)
    try:
        for w in cutoff_refusals():
            latch("commit: " + w)
        boundary = next(ORDER)
        co = STATE["cancel_order"]
        chosen = unsat_bytes if (unsat_bytes is not None and not LATCH and (co is None or co > boundary)) else unknown_bytes
        write_all(fd, chosen)
        os.fsync(fd)
    finally:
        os.close(fd)
    h = hashlib.sha256(chosen).hexdigest()
    register_written(path, h, len(chosen))
    return {"boundary": boundary, "cancel_order": STATE["cancel_order"], "committed_unsat": chosen is unsat_bytes,
            "sha256": h}


HEX64 = re.compile(r"[0-9a-f]{64}")
HEADER_RE = re.compile(r"p cnf [1-9][0-9]* [1-9][0-9]*")


def _nat(x):
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


def item_shape_refusals(it):
    """V12: exact item types and shape for this runner's family.  ms09: exact non-bool ints with
    0 <= lo <= hi < denominator, canonical id 'bBBBBB:LLLLL-HHHHH', pinned list (path, sha256); ms06: canonical id
    'ms06:bBBBBB:direct' and no interval fields; both: pinned CNF triple (sha256, bytes > 0, header)."""
    if not isinstance(it, dict) or not _nat(it.get("b")):
        return ["item or b malformed"]
    why = []
    cnf = it.get("cnf")
    if not (isinstance(cnf, tuple) and len(cnf) == 3 and isinstance(cnf[0], str) and HEX64.fullmatch(cnf[0])
            and _nat(cnf[1]) and cnf[1] > 0 and isinstance(cnf[2], str) and HEADER_RE.fullmatch(cnf[2])):
        why.append("cnf pin malformed")
    interval_keys = {"lo", "hi", "denominator", "list"}
    if FAMILY == "ms09":
        lo, hi, den, lst = it.get("lo"), it.get("hi"), it.get("denominator"), it.get("list")
        if not (_nat(lo) and _nat(hi) and _nat(den) and lo <= hi < den):
            why.append("interval not exact ints with 0 <= lo <= hi < denominator")
        elif it.get("id") != "b%05d:%05d-%05d" % (it["b"], lo, hi):
            why.append("id not canonical")
        if not (isinstance(lst, tuple) and len(lst) == 2 and isinstance(lst[0], str) and isinstance(lst[1], str)
                and HEX64.fullmatch(lst[1])):
            why.append("list pin malformed")
    else:
        if interval_keys & set(it):
            why.append("interval fields on a whole-case item")
        if it.get("id") != "ms06:b%05d:direct" % it["b"]:
            why.append("id not canonical")
    return why


def main():
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if len(sys.argv) != 4:
        print("usage: pilot_stream_drat_%s_v4.py GO.json GO_SHA256 OUT_DIR" % FAMILY, flush=True)
        return EXIT_PRESTART_REFUSED
    go_path, go_sha, out_dir = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
    why = out_dir_refusal(out_dir)                 # V4: direct child of a symlink-free pilot-v1, new
    if why:
        print("REFUSED: " + why, flush=True)
        return EXIT_PRESTART_REFUSED
    shape = [w for it in ITEMS for w in item_shape_refusals(it)]
    if shape or len({it.get("id") for it in ITEMS if isinstance(it, dict)}) != len(ITEMS):
        print("REFUSED: item shape %r" % ((shape or ["duplicate item ids"])[:4],), flush=True)   # V12
        return EXIT_PRESTART_REFUSED
    self_sha = sha_file(os.path.abspath(__file__))[0]
    try:
        go = json.loads(read_pinned(go_path, go_sha))
        read_pinned(*BINARY_IMPORTS)
        read_pinned(*KISSAT_SOURCE)
        contract = json.loads(read_pinned(*CONTRACT))
        ceiling_ok = contract["resources"]["per_lane_new_disk_bytes"] == LANE_CEILING
        busy_ok = contract["resources"]["per_lane_busy_processes"] == BUSY_SLOTS
    except Exception as exc:
        print("REFUSED: GO/evidence/contract unreadable or pin mismatch %r" % exc, flush=True)
        return EXIT_PRESTART_REFUSED
    if not (ceiling_ok and busy_ok):
        print("REFUSED: contract per_lane_new_disk_bytes/per_lane_busy_processes != LANE_CEILING/BUSY_SLOTS", flush=True)
        return EXIT_PRESTART_REFUSED
    if go.get("runner_sha256") != self_sha or go.get("decision") != "GO" \
            or go.get("items") != [it["id"] for it in ITEMS]:
        print("REFUSED: GO record does not name this runner/items", flush=True)
        return EXIT_PRESTART_REFUSED
    span = RUN_HELPER_SECONDS + CONTROLS_WORST_SECONDS + len(ITEMS) * ITEM_WORST_SECONDS
    if span + SETTLE + MARGIN > MAX_CHUNK or time.time() + span > OWNED_SETTLED_BY - 180:
        print("REFUSED: chunk-fit", flush=True)
        return EXIT_PRESTART_REFUSED
    full_reserve = RUN_RESERVE + CONTROL_RESERVE + len(ITEMS) * ITEM_RESERVE
    alloc_why, led = allocation_refusals(go, go_sha, out_dir, full_reserve)   # N3: the parent's single allocator
    if alloc_why:
        print("REFUSED: parent allocation %r" % (alloc_why[:6],), flush=True)
        return EXIT_PRESTART_REFUSED
    try:                                           # N5: free-space admission BEFORE any retained output
        fb = free_bytes()
        pre_why = registry_refusals() + stability_refusals(full_reserve)
        if fb < FRESH_BASE + full_reserve or fb - full_reserve < FREE_FLOOR:
            pre_why.append("free %d cannot hold the reservation %d above the floors" % (fb, full_reserve))
    except Exception as exc:
        pre_why = ["prestart admission exception %r" % (exc,)]
    if pre_why:
        print("REFUSED: prestart admission %r" % (pre_why[:6],), flush=True)
        return EXIT_PRESTART_REFUSED
    t_start, mono0 = time.time(), time.monotonic()
    abs_end = t_start + span
    STATE.update(abs_end=abs_end, chunk_end=t_start + MAX_CHUNK, mono0=mono0, mono_end=mono0 + span,
                 mono_chunk_end=mono0 + MAX_CHUNK, remaining_reserve=full_reserve, reservation=full_reserve,
                 output_limit=full_reserve, written=0, last_ledger=led, pilot_entries=list(led["pilot_entries"]),
                 go={"path": go_path, "sha256": go_sha}, runner_sha=self_sha)
    try:                                           # N8: anchored, exclusive run tree (and the SAT latch directory)
        anchor_existing_dir(CONTROL_DIR)
        create_run_tree(out_dir)
    except BaseException as exc:
        print("REFUSED: run tree creation %r" % (exc,), flush=True)
        return EXIT_PRESTART_REFUSED
    STATE["out"] = out_dir
    summary = {"schema": "PA19-96H-PSTREAM-SUMMARY-v4", "items": {}, "controls_ok": None, "stopped": None,
               "terminal_policy": "exit code reports runner execution only; per-item records carry the scientific "
                                  "status; an item counts only if qualify_stream (both pinned checkers on the same "
                                  "RAM buffer), the terminal gate and the commit boundary all pass; case closure is "
                                  "decided by the parent audit"}
    outcome = {"sat": False, "controls_failed": False, "refused": False, "exception": False, "complete": False}
    try:                                           # N4/N8: every post-tree failure still reaches closeout
        launch = {
            "schema": "PA19-96H-PSTREAM-LAUNCH-v4", "host_clock": clock(), "owner": "ContinuePA19b",
            "go": STATE["go"], "runner": {"path": os.path.abspath(__file__), "sha256": self_sha},
            "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "cwd": os.getcwd(), "argv": sys.argv,
            "python": sys.version, "binaries": {"kissat": KISSAT, "drat_trim_lane_copy": DRAT, "drat_trim_old": DRAT_OLD,
                                                "drat_trim_provenanced": DRAT_PROV, "provenance_receipt": DRAT_PROV_RECEIPT,
                                                "drat_trim_source_sha256": DRAT_SOURCE_SHA, "checkers_in_order": CHECKERS},
            "inputs": {"encoder": ENC, "skeleton": SKEL, "items": ITEMS, "registry": REGISTRY,
                       "launch_contract": LAUNCH_CONTRACT, "binary_imports": BINARY_IMPORTS,
                       "kissat_source_evidence": KISSAT_SOURCE, "monitor": MONITOR, "observer_source": OBSERVER_SOURCE_SHA},
            "absolute_end_epoch": abs_end, "max_chunk_end_epoch": t_start + MAX_CHUNK, "elapsed_span_s": span,
            "timing": {"run_helper_s": RUN_HELPER_SECONDS, "controls_worst_s": CONTROLS_WORST_SECONDS,
                       "item_worst_s": ITEM_WORST_SECONDS, "settle_plus_margin_s": SETTLE + MARGIN, "max_chunk_s": MAX_CHUNK,
                       "claim": "holds only if every owned process settles within its tail; a quarantined process voids "
                                "it (UNSETTLED; never waited for again; reservation retained until a NEW parent "
                                "disposition)"},
            "metadata_helper": {"binary": DATE, "argv": DATE_ARGV, "wall_s": HELPER_WALL, "term_wait_s": HELPER_TERM_WAIT,
                                "allow_s": HELPER_ALLOW, "per_item": HELPERS_PER_ITEM, "per_run": HELPERS_PER_RUN,
                                "policy": "owned, bounded, never concurrent with a native child, none after a cancel"},
            "lane_ceiling": {"ceiling_bytes": LANE_CEILING, "busy_slots": BUSY_SLOTS, "contract": CONTRACT,
                             "allocation_ledger_at_prestart": led},
            "anchored_tree": {p: [v[1], v[2]] for p, v in TREE.items()},
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
        run_plan(summary, outcome)
    except BaseException as exc:
        outcome["exception"] = True
        summary["stopped"] = {"phase": "exception", "error": repr(exc)}
    finally:
        settle_all()
        code = final_code(summary, outcome)
    return code



def run_plan(summary, outcome):
    """The plan body; every early stop is a plain return with the outcome flags set.  V5: an item's proof buffer is
    released in a finally on every path (N6: owned by `item_bufs` from its creation); V12: item shape re-checked
    immediately before generation; N8: run-tree files are hashed through the anchored tree."""
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
        why = item_shape_refusals(it)
        if why:
            raise RuntimeError("item shape %r" % (why,))
        label = it["id"].replace(":", "_")
        rec = {"id": it["id"], "status": "UNKNOWN", "count_for_scientific_coverage": False,
               "host_clock_start": clock()}
        rec_path = os.path.join(out_dir, label + ".record.json")
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = (hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode())
        if got != it["cnf"]:
            raise RuntimeError("CNF digest mismatch %r" % (got,))
        cnf_path = os.path.join(out_dir, label + ".cnf")
        write_bytes_x(cnf_path, cnf)
        del cnf
        if sha_tree(cnf_path) != (it["cnf"][0], it["cnf"][1]):
            raise RuntimeError("CNF file re-hash mismatch")
        inputs = {"item": it["id"], "cnf_pin": [it["cnf"][0], it["cnf"][1]], "case_b": it["b"],
                  "skeleton_pin": SKEL[1], "encoder_pin": ENC[1]}
        buf = None
        item_bufs = []                             # N6: owns the item's buffer from its creation
        try:
            ks, kl, refused, buf = run_kissat(cnf_path, label, SOLVER_SECONDS, PROOF_CAP, LOG_CAP + 3 * RECORD_MAX,
                                              inputs, item_bufs)
            if ks is None:
                rec.update(reason="solver admission refused", refusal=refused, host_clock_end=clock())
                write_x(rec_path, rec)
                summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "solver admission refused"}
                summary["stopped"] = {"phase": "solver_admission", "item": it["id"], "why": refused}
                outcome["refused"] = True
                return
            rec["solver"] = ks
            rec["solver_lines"] = kl[:8]
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
                        rec.update(reason="checker %s admission refused" % name, refusal=refused,
                                   host_clock_end=clock())
                        write_x(rec_path, rec)
                        summary["items"][it["id"]] = {"status": "UNKNOWN",
                                                      "reason": "checker %s admission refused" % name}
                        summary["stopped"] = {"phase": "checker_admission", "item": it["id"], "checker": name,
                                              "why": refused}
                        outcome["refused"] = True
                        return
                    checks.append((name, dr, dl))
                    filt = dr.get("stdout_filter") or {}
                    rec["checkers"][name] = {
                        "record": dr, "status_lines": status_lines(dl),
                        "parse_lines": [s[:200] for s in dl if s.startswith("c parsing") or
                                        s.startswith("c finished parsing") or s.startswith("c reading proof")][:6],
                        "duplicate_literal_warnings": {   # V8/P3: both phases counted and disclosed, never gated
                            "formula_phase_proof_line_le_header_clauses": filt.get("dup_lines_at_or_below_header_clauses"),
                            "proof_phase_proof_line_gt_header_clauses": filt.get("dup_lines_above_header_clauses"),
                            "basis": "drat-trim.c:1133/1153/1229: exact phase partition for any log without early EOF"}}
                    if checker_defects(name, it["cnf"], rec["proof"]["sha256"], rec["proof"]["bytes"], dr, dl) \
                            or LATCH or cancelled():
                        break  # S4: a later checker cannot rescue the item
                post_cnf, post_buf = sha_tree(cnf_path), buf.digest()
                buf.release()
                rec["post_check_hashes"] = {"cnf": list(post_cnf), "proof_buffer": post_buf}
                rec["defects"] = qualify_stream(it["cnf"], ks, kl, PROOF_CAP, checks, post_cnf, post_buf)
                rec["defect_ids"] = defect_ids(rec["defects"])
                rec["host_clock_end"] = clock()
                rec["terminal_gate"] = terminal_gate()
                unsat = None
                if not rec["defects"] and not rec["terminal_gate"] and not LATCH:
                    unsat = dict(rec, status="UNSAT", count_for_scientific_coverage=True,
                                 commit="UNSAT chosen at an explicit commit boundary with no earlier cancel stamp or "
                                        "latch")
                commit = commit_record(rec_path, dict(rec, commit="UNKNOWN record"), unsat)
                rec["status"] = "UNSAT" if commit["committed_unsat"] else "UNKNOWN"
                summary.setdefault("commits", {})[it["id"]] = commit
            else:
                rec["reason"] = "no settled self-exit rc20 verdict with a complete proof buffer (or latch/cancel)"
                rec["host_clock_end"] = clock()
                write_x(rec_path, rec)
        finally:
            for b in item_bufs:
                b.release()                        # N6: a live collector stays charged; closeout retries
        summary["items"][it["id"]] = {k: rec.get(k) for k in ("status", "defect_ids", "terminal_gate", "reason", "proof")}
        summary["items"][it["id"]]["duplicate_literal_warnings"] = {
            n: v.get("duplicate_literal_warnings") for n, v in (rec.get("checkers") or {}).items()}
        STATE["remaining_reserve"] -= ITEM_RESERVE
        if LATCH or cancelled():
            summary["stopped"] = {"phase": "latch_or_cancel", "item": it["id"]}
            return
    outcome["complete"] = True



def final_code(summary, outcome):
    """r3#9/N9/B1: blocking closeout metadata first: host clock (owned helper), child and helper SETTLEMENT (N2: a
    helper counts only if its settlement predicate held), proof RAM (N6: releases are retried, anything still held
    is a defect), N8 anchored confinement, run-tree bytes and digest preservation of every runner-written file, N4
    closeout timing, B1 the UNSETTLED owners (exact identities, live census, late obligations) with the reservation
    retained until a NEW parent disposition; then the explicit closeout boundary; the cancel stamp is read AFTER the
    boundary and compared with it (N9).  Any closeout defect latches (exit 50); exit 0 is impossible with a voided
    chunk claim.  Nothing here waits for an owner."""
    out_dir = STATE["out"]
    host_end = clock()                             # V1: owned helper; None after a cancel, a latch or a failure
    children = [c.settled_rec if c.settled_rec is not None else {"seq": c.seq, "label": c.label, "pid": c.pid,
                                                                   "settled": False, "note": "never settled"}
                for c in OWNED if c.proc is not None]
    all_settled = all(r.get("settled") for r in children)
    helpers_settled = all(h.settled for h in HELPERS)
    unsettled_owners = [dict(c.unsettled, kind="child", seq=c.seq, label=c.label, receipt=c.quarantine_path,
                             receipt_state=c.quarantine_receipt_state)
                        for c in OWNED if c.proc is not None and c.unsettled is not None] + \
                       [dict(h.unsettled, kind="helper", launch_order=h.launch_order, receipt=h.quarantine_path,
                             receipt_state=h.quarantine_receipt_state)
                        for h in HELPERS if h.unsettled is not None]
    for b in list(LIVE_BUFFERS):
        if b.release_requested and not b.released:
            b.release()                            # N6: retried now that collectors may have ended
    try:
        outstanding = buffer_charge()
        buffers = [b.accounting() for b in LIVE_BUFFERS][:LIST_MAX]
    except BaseException as exc:
        outstanding, buffers = None, ["accounting failed %r" % (exc,)]
    confinement = confinement_refusals()
    try:
        tree = run_tree_census()
        tree_bytes = sum(v[3] for v in tree.values() if v[0] != "dir")
        quarantine = sorted(p for p in tree if p.endswith(".QUARANTINE.json"))
    except BaseException as exc:
        tree_bytes, quarantine = None, ["run-tree census failed %r" % (exc,)]
    preservation = preservation_refusals()
    m, e = time.monotonic(), time.time()
    elapsed = m - STATE["mono0"]
    late = m > STATE["mono_end"] + SETTLE or e > STATE["abs_end"] + SETTLE
    boundary = next(ORDER)
    co = STATE["cancel_order"]                     # N9: sampled AFTER the closeout boundary
    cancel_before = co is not None and co < boundary
    launch_after_cancel = [c.seq for c in OWNED if c.proc is not None and co is not None and c.launch_order is not None
                           and co < c.launch_order] + \
                          ["helper %s" % h.launch_order for h in HELPERS if h.proc is not None and co is not None
                           and co < h.launch_order]
    closeout_defects = []
    if not helpers_settled:
        closeout_defects.append("metadata helper unsettled or quarantined")
    if unsettled_owners:
        closeout_defects.append("UNSETTLED owners %r: reservation retained; parent disposition required"
                                % ([u.get("pid") for u in unsettled_owners][:LIST_MAX],))
    if outstanding != 0:
        closeout_defects.append("proof RAM still held at closeout: %r" % (outstanding,))
    closeout_defects += confinement
    closeout_defects += preservation
    if tree_bytes is None or tree_bytes > STATE["output_limit"]:
        closeout_defects.append("run-tree bytes %r unreadable or above the reservation %d" % (tree_bytes,
                                                                                             STATE["output_limit"]))
    if quarantine:
        closeout_defects.append("quarantine receipts present %r" % (quarantine[:4],))
    if late:
        closeout_defects.append("closeout after the frozen cutoffs + SETTLE (N4)")
    if launch_after_cancel:
        closeout_defects.append("launch ordered after a cancel: %r" % launch_after_cancel)
    chunk_claim = "held" if (all_settled and helpers_settled and not quarantine and not unsettled_owners and not late
                             and elapsed + SETTLE <= MAX_CHUNK) else "voided"
    if chunk_claim == "voided":
        closeout_defects.append("chunk claim voided")
    for w in closeout_defects:
        latch("closeout: " + w)
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
                   children=[{k: r.get(k) for k in ("seq", "label", "pid", "returncode", "stop", "settled",
                                                    "launch_order", "exit_observed_by_deadline")} for r in children],
                   all_children_settled=all_settled, metadata_helpers=HELPER_LOG[:LIST_MAX],
                   unsettled_owners=unsettled_owners[:LIST_MAX], reservation_retained=bool(unsettled_owners),
                   release_requires=("a NEW parent disposition confirming that every listed process ended"
                                     if unsettled_owners else "verified parent release"),
                   all_helpers_settled=helpers_settled, proof_ram_outstanding_bytes=outstanding,
                   proof_buffers=buffers, quarantine_receipts=quarantine, run_tree_bytes=tree_bytes,
                   retained_bytes_charged=STATE["written"], output_limit_bytes=STATE["output_limit"],
                   elapsed_mono_s=round(elapsed, 3), closeout_late=late, chunk_claim=chunk_claim,
                   closeout_defects=closeout_defects, lane_ledger_last=STATE["last_ledger"])
    try:
        write_x(os.path.join(out_dir, "summary.json"), summary)
    except BaseException as exc:
        print("SUMMARY WRITE FAILED %r" % exc, flush=True)
        code = EXIT_SAFETY_STOP
    print("SUMMARY", os.path.join(out_dir, "summary.json"), "exit", code, flush=True)
    return code



if __name__ == "__main__":
    sys.exit(main())
