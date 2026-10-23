#!/usr/bin/env python3
"""PA19 96h pilot runner v4.  v1-v3 are preserved, never run; v3 (dfd1036b...) was sent for GO and
returned NO-GO with parent findings, all addressed here:
  P1 monitor parsing: the authoritative v3 observer starts with an {"event":"observer_start",...}
     line; only that exact event schema (with the pinned observer source SHA) is allowed, every other
     complete line must be a strict sample {t, free, floor_bytes, scope}; an observer_end event refuses;
     the stability window is [time.time()-300, time.time()], not anchored at the last sample.
  P2 terminal consumer gate: after the checker and the post-check hashes, a final per-item gate
     (cancel latch, STOP registry, in-flight floor, trips, settlement, proof-sink completeness) must pass
     before any status UNSAT / count_for_scientific_coverage=true is written.
  P3 explicit nonzero exit codes (EXIT_* below); exit code describes runner execution only and never
     certifies science; per-item records carry the scientific status.
  P4 proof hard cap: kissat writes its binary DRAT proof into a lane-local FIFO read by an owned sink
     thread that writes the proof FILE and never writes beyond PROOF_CAP bytes; excess bytes are drained
     and discarded (counted) so the producer can exit, and the producer is SIGTERMed (trip proof_cap).
     The proof file is therefore hard-bounded; producer-read bytes/SHA are measured contemporaneously.

NOT TO BE RUN without the item-specific parent GO whose JSON names this file's SHA-256.

Scope (frozen): same-binary controls C1-C7, then three exact independent-M2
(encode_skel_b.build_partbatch) items of multiset ms09, sequentially, one native child at a time:
  b00070:00000-00024, b00005:00200-00299, b00005:00300-00350.
Per item: build the CNF in memory with the vendored unchanged encoder; require the frozen
digest/length/header; write it by exclusive creation and re-hash it from disk; run
  kissat -q -f --seed=1 --time=600 CNF PROOF_FIFO     (sink -> exclusive proof file, hard cap)
then, only on a self-exit rc20 's UNSATISFIABLE' with a complete sink, run
  drat-trim CNF PROOF_FILE -i -t 1200                 (lane copy of the pinned binary)
on the same regular files and re-hash both afterwards.
Safety: no deletion, no overwrite, no SIGKILL, no subprocess timeout, no ulimit; lane FIFOs are new
and never removed.  Each native child gets its own session/process group; the only signal ever sent
is one SIGTERM to an UNREAPED owned Popen child (Popen.send_signal polls first), followed by a bounded
60 s wait; a survivor gets a creation-only quarantine receipt, no further signal, no new child, and
the runner keeps waiting for it.  Settlement = Popen.wait() reaped, os.killpg(pgid, 0) ->
ProcessLookupError, capture and proof sinks closed and fsynced, artifacts hashed, receipt written.
Anything unobservable -> UNKNOWN/UNSETTLED, never UNSAT.
"""
import errno
import hashlib
import importlib.util
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
KISSAT = ("/opt/homebrew/bin/kissat", "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848")
DRAT_OLD = (OLD + "/tools/drat-trim/drat-trim", "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4")
DRAT = LANE + "/code/vendor/drat-trim"
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
REGISTRY = (LANE + "/evidence/inherited-stop-registry-v1.json", "ee370929f20ffe514e71bce6961e31ed32faaf243e0433d9268179956a0e9873")
LAUNCH_CONTRACT = (RUN + "/control/launch-contract-tightening-v1.json", "8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20")
MONITOR = RUN + "/control/resource-observer-live-v3.jsonl"
OBSERVER_SOURCE_SHA = "fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196"
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
ITEMS = [
    {"id": "b00070:00000-00024", "b": 70, "lo": 0, "hi": 24,
     "list": (OLD + "/cycle2/m2part_drat/ms09_b00070/ext.json", "c91d656a6c62426752fc6b9683bd8d491031d75bfdb9d3940055ddd22b536c10"),
     "denominator": 25, "cnf": ("565dd02cf532cb6a58fb70935d8e74fa7bca8e15432ad800c5019eaf5c98ff2b", 9448478, "p cnf 13495 433945")},
    {"id": "b00005:00200-00299", "b": 5, "lo": 200, "hi": 299,
     "list": (OLD + "/cycle2/m2part_drat/ms09_b00005/ext.json", "3f71e620c9efa7b3075f8579e357e5096f91282cf6434120706391bb8909fb00"),
     "denominator": 351, "cnf": ("952b8839f7daa66ba499ba0e523696562425cce047b845dbdaef87b8d696a642", 9482840, "p cnf 13570 436725")},
    {"id": "b00005:00300-00350", "b": 5, "lo": 300, "hi": 350,
     "list": (OLD + "/cycle2/m2part_drat/ms09_b00005/ext.json", "3f71e620c9efa7b3075f8579e357e5096f91282cf6434120706391bb8909fb00"),
     "denominator": 351, "cnf": ("4ed08d983896dfd5f27925dab5dc656be9374262c646a9c31792ec2cdb7e9196", 9460162, "p cnf 13521 434912")},
]
SOLVER_SECONDS = 600
CHECK_SECONDS = 1200
GRACE = 60
TERM_WAIT = 60
SINK_JOIN_SECONDS = 60
PROOF_CAP = 1_258_291_200            # HARD: the sink never writes more than this to the proof file
LOG_CAP = 16 * 1024 * 1024           # HARD per captured stdout+stderr stream
CNF_MAX = 9_500_000
ITEM_RESERVE = CNF_MAX + PROOF_CAP + 2 * LOG_CAP + 1_048_576
CONTROL_RESERVE = 64 * 1024 * 1024
FREE_FLOOR = 12_000_000_000
FRESH_BASE = 12_200_000_000
LANE_RSS_TRIP = 6 * 1024 ** 3
ITEM_WORST_SECONDS = 30 + SOLVER_SECONDS + GRACE + TERM_WAIT + SINK_JOIN_SECONDS + 30 + CHECK_SECONDS + GRACE + TERM_WAIT + 30
CONTROLS_WORST_SECONDS = 900
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
SAMPLE_KEYS = {"t", "free", "floor_bytes", "scope"}
START_KEYS = {"event", "at", "pid", "pgid", "cwd", "source_sha256"}

CANCEL = threading.Event()


def on_term(signum, frame):
    CANCEL.set()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True,
                          check=True, stdin=subprocess.DEVNULL).stdout.strip()


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


def write_x(path, obj):
    data = json.dumps(obj, indent=1, sort_keys=True).encode()
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


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def rss_bytes(pids):
    out = subprocess.run(["/bin/ps", "-o", "rss=", "-p", ",".join(str(p) for p in pids)],
                         capture_output=True, text=True, stdin=subprocess.DEVNULL)
    vals = [int(x) for x in out.stdout.split() if x.strip().isdigit()]
    return sum(vals) * 1024, len(vals)


def identity(pid):
    try:
        out = subprocess.run(["/bin/ps", "-o", "pid=,ppid=,pgid=,lstart=,comm=", "-p", str(pid)],
                             capture_output=True, text=True, stdin=subprocess.DEVNULL)
        return out.stdout.strip()
    except Exception as exc:  # identity is evidence only; never let it orphan a child
        return "unavailable: %r" % exc


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


def stability_refusals(projected):
    """resource-stability-addendum v1 rule over the v2-pinned v3 monitor (P1)."""
    st = os.lstat(MONITOR)
    if not stat.S_ISREG(st.st_mode):
        return ["monitor is not a regular file"]
    with open(MONITOR, "rb") as f:
        raw = f.read()
    complete = raw.split(b"\n")[:-1]  # the last element is b"" after a final newline or an ignored partial line
    rows = []
    for i, ln in enumerate(complete):
        try:
            o = json.loads(ln)
            if not isinstance(o, dict):
                raise ValueError("not an object")
            if "event" in o:
                if i == 0 and set(o) == START_KEYS and o["event"] == "observer_start" \
                        and o["source_sha256"] == OBSERVER_SOURCE_SHA \
                        and datetime.fromisoformat(o["at"]).tzinfo is not None:
                    continue
                return ["monitor event line %d not an allowed observer_start (or observer ended): %r" % (i, ln[:160])]
            if set(o) != SAMPLE_KEYS or not isinstance(o["free"], int) or isinstance(o["free"], bool):
                raise ValueError("sample schema")
            dt = datetime.fromisoformat(o["t"])
            if dt.tzinfo is None:
                raise ValueError("naive timestamp")
            rows.append((dt.timestamp(), o["free"]))
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
    elif win[-1][0] - win[0][0] < 290:
        why.append(f"window span {win[-1][0] - win[0][0]:.1f}s < 290 s")
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


class ProofSink:
    """Owned FIFO reader writing the proof FILE with a HARD byte cap (P4)."""

    def __init__(self, fifo_path, file_path, cap):
        if os.path.lexists(fifo_path) or os.path.lexists(file_path):
            raise RuntimeError("proof fifo/file path exists")
        os.mkfifo(fifo_path, 0o600)
        self.fifo_path, self.file_path, self.cap = fifo_path, file_path, cap
        self.file = open(file_path, "xb")
        self.sha = hashlib.sha256()
        self.written = self.received = self.discarded = 0
        self.over_cap = self.connected = self.eof = False
        self.error = None
        self.unblocked_by_runner = False
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def _run(self):
        try:
            fd = os.open(self.fifo_path, os.O_RDONLY)  # blocks until a writer opens the FIFO
            self.connected = True
            try:
                while True:
                    b = os.read(fd, 1 << 20)
                    if not b:
                        self.eof = True
                        break
                    self.received += len(b)
                    if not self.over_cap and self.written + len(b) <= self.cap:
                        self.file.write(b)
                        self.sha.update(b)
                        self.written += len(b)
                    else:
                        self.over_cap = True       # never write beyond the cap; drain so the producer can exit
                        self.discarded += len(b)
            finally:
                os.close(fd)
        except Exception as exc:
            self.error = repr(exc)
        finally:
            try:
                self.file.flush()
                os.fsync(self.file.fileno())
                self.file.close()
            except Exception as exc:
                self.error = (self.error or "") + " close:" + repr(exc)

    def finish(self):
        """After the producer is reaped: unblock a never-connected reader, then bounded join."""
        deadline = time.time() + 10
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
        self.thread.join(SINK_JOIN_SECONDS)
        rec = {"fifo": self.fifo_path, "file": self.file_path, "cap": self.cap, "connected": self.connected,
               "eof": self.eof, "received": self.received, "written": self.written, "discarded": self.discarded,
               "over_cap": self.over_cap, "error": self.error, "unblocked_by_runner": self.unblocked_by_runner,
               "thread_alive_after_join": self.thread.is_alive(), "sha256_of_written": self.sha.hexdigest()}
        if not rec["thread_alive_after_join"]:
            rec["file_rehash"] = list(sha_file(self.file_path))
        return rec


class Child:
    """One owned native child in its own session; HARD byte-capped stdout+stderr capture file."""

    def __init__(self, argv, out_path, cap):
        self.argv, self.out_path, self.cap = argv, out_path, cap
        self.captured, self.over_cap, self.reader_error = 0, False, None
        self.term_sent_at, self.stop = None, None
        self.sink = open(out_path, "xb")  # exclusive capture file BEFORE the child exists
        try:
            self.proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, start_new_session=True,
                                         close_fds=True, cwd=LANE + "/tmp", env=CHILD_ENV)
        except BaseException:
            self.sink.close()
            raise
        self.pid = self.pgid = self.proc.pid
        self.started = time.time()
        try:
            self.identity_at_start = identity(self.pid)
            self.reader = threading.Thread(target=self._read, daemon=True)
            self.reader.start()
        except BaseException:
            # never leave an owned child unsupervised: one SIGTERM to the unreaped child, then wait
            self.proc.send_signal(signal.SIGTERM)
            self.proc.wait()
            self.sink.close()
            raise

    def _read(self):
        try:
            while True:
                b = self.proc.stdout.read1(65536)
                if not b:
                    break
                room = self.cap - self.captured
                if room > 0:
                    self.sink.write(b[:room])
                self.captured += len(b)
                if self.captured > self.cap:
                    self.over_cap = True
        except Exception as exc:
            self.reader_error = repr(exc)
        finally:
            try:
                self.sink.flush()
                os.fsync(self.sink.fileno())
                self.sink.close()
                self.proc.stdout.close()
            except Exception as exc:
                self.reader_error = (self.reader_error or "") + " close:" + repr(exc)

    def alive(self):
        return self.proc.poll() is None

    def term(self, reason):
        if self.term_sent_at is None and self.proc.returncode is None:
            self.stop = reason
            self.term_sent_at = time.time()
            self.proc.send_signal(signal.SIGTERM)  # Popen polls first; never signals a reaped PID

    def settle(self, out_dir, label):
        """Explicit wait; after the single SIGTERM no further signal is ever sent."""
        quarantine = None
        if self.term_sent_at is not None:
            deadline = self.term_sent_at + TERM_WAIT
            while self.proc.poll() is None and time.time() < deadline:
                time.sleep(0.1)
            if self.proc.poll() is None:
                quarantine = os.path.join(out_dir, label + ".QUARANTINE.json")
                write_x(quarantine, {"host_clock": clock(), "pid": self.pid, "pgid": self.pgid,
                                     "argv": self.argv, "note": "survived SIGTERM + 60 s; no further signal; "
                                     "runner keeps waiting and starts no new child"})
        rc = self.proc.wait()
        self.reader.join()
        try:
            os.killpg(self.pgid, 0)
            group_empty = False
        except ProcessLookupError:
            group_empty = True
        except PermissionError:
            group_empty = False
        return {"pid": self.pid, "pgid": self.pgid, "identity_at_start": self.identity_at_start,
                "argv": self.argv, "returncode": rc, "stop": self.stop or "self",
                "seconds": round(time.time() - self.started, 3), "captured_bytes": self.captured,
                "capture_over_cap": self.over_cap, "reader_error": self.reader_error,
                "group_empty_after_reap": group_empty, "quarantine_record": quarantine,
                "output_path": self.out_path, "output_sha256": sha_file(self.out_path)[0]}


def segments(path):
    with open(path, "rb") as f:
        txt = f.read().decode("utf-8", "replace")
    return [s for s in re.split(r"[\r\n]", txt) if s != ""]


def supervise(child, wall, sink):
    """Monitor until exit or a single trip; any monitor exception is itself a trip."""
    me = os.getpid()
    last_rss = last_reg = 0.0
    peak = 0
    while child.alive():
        try:
            now = time.time()
            if CANCEL.is_set():
                child.term("owner_cancel_sigterm")
            elif now - child.started > wall + GRACE:
                child.term("runner_wall_bound")
            elif sink is not None and (sink.over_cap or sink.error):
                child.term("proof_cap" if sink.over_cap else "proof_sink_error")
            elif child.over_cap:
                child.term("capture_cap")
            elif free_bytes() < FREE_FLOOR:
                child.term("inflight_disk_floor")
            if child.term_sent_at is None and now - last_rss >= 1.0:
                last_rss = now
                r, n = rss_bytes([me, child.pid])
                peak = max(peak, r)
                if n < 2 and child.alive():
                    child.term("rss_unreadable")
                elif r > LANE_RSS_TRIP:
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
    return child.stop, peak


def run_child(argv, out_dir, label, wall, sink=None):
    ch = Child(argv, os.path.join(out_dir, label + ".out"), LOG_CAP)
    try:
        if CANCEL.is_set():
            ch.term("owner_cancel_sigterm")
        trip, peak = supervise(ch, wall, sink)
    except BaseException as exc:
        ch.term("runner_exception:%r" % exc)
        trip, peak = ch.stop, None
    finally:
        rec = ch.settle(out_dir, label)
    rec["trip"] = trip
    rec["peak_sampled_lane_rss_bytes"] = peak
    return rec, segments(ch.out_path)


def run_kissat(cnf_path, proof_file, out_dir, label, seconds, proof_cap=PROOF_CAP):
    """kissat with its proof routed through a hard-capped owned sink; proof_file None = no proof."""
    argv = [KISSAT[0], "-q", "-f", "--seed=1", "--time=%d" % seconds, cnf_path]
    sink = None
    if proof_file is not None:
        sink = ProofSink(os.path.join(out_dir, label + ".proof.fifo"), proof_file, proof_cap)
        argv.append(sink.fifo_path)
    try:
        rec, lines = run_child(argv, out_dir, label + ".kissat", seconds, sink)
    finally:
        sink_rec = sink.finish() if sink is not None else None
    rec["proof_sink"] = sink_rec
    return rec, lines


def run_drat(cnf_path, proof_path, out_dir, label, seconds):
    return run_child([DRAT, cnf_path, proof_path, "-i", "-t", str(seconds)], out_dir, label + ".drat", seconds)


def sink_complete(sink_rec):
    return (sink_rec is not None and sink_rec["connected"] and sink_rec["eof"] and not sink_rec["over_cap"]
            and sink_rec["error"] is None and not sink_rec["unblocked_by_runner"]
            and not sink_rec["thread_alive_after_join"] and sink_rec["discarded"] == 0
            and sink_rec["received"] == sink_rec["written"]
            and sink_rec.get("file_rehash") == [sink_rec["sha256_of_written"], sink_rec["written"]])


def qualify_unsat(cnf_expect, solver_rec, kissat_lines, proof_sha, proof_bytes, drat_rec, drat_lines,
                  cnf_post, proof_post):
    bad = []
    if solver_rec["returncode"] != 20 or solver_rec["stop"] != "self" or solver_rec["trip"] is not None:
        bad.append("solver not self-exit rc20")
    if [s for s in kissat_lines if s.startswith("s ")] != ["s UNSATISFIABLE"]:
        bad.append("solver status lines not exactly ['s UNSATISFIABLE']")
    if solver_rec.get("proof_sink") is not None and not sink_complete(solver_rec["proof_sink"]):
        bad.append("proof sink incomplete/over cap/error")
    if proof_bytes <= 0 or proof_bytes > PROOF_CAP:
        bad.append("proof size outside (0, cap]")
    if drat_rec["returncode"] != 0 or drat_rec["stop"] != "self" or drat_rec["trip"] is not None:
        bad.append("checker not self-exit rc0")
    st = [s for s in drat_lines if s.startswith("s ")]
    if st != ["s VERIFIED"]:
        bad.append("checker status lines %r" % st)
    v, c = cnf_expect[2].split()[2:4]
    if ("c parsing input formula with %s variables and %s clauses" % (v, c)) not in drat_lines:
        bad.append("checker parse header line missing/mismatched")
    if ("c finished parsing, read %d bytes from proof file" % proof_bytes) not in drat_lines:
        bad.append("checker-consumed proof bytes != proof file bytes")
    for pat in ("early EOF", "clauses less than expected", "trivial UNSAT", "ERROR", "MEMOUT",
                "wrong binary prefix", "no empty clause detected", "NOT VERIFIED", "TIMEOUT"):
        if any(pat in s for s in drat_lines):
            bad.append("checker output contains %r" % pat)
    if cnf_post != (cnf_expect[0], cnf_expect[1]):
        bad.append("CNF file changed during run")
    if proof_post != (proof_sha, proof_bytes):
        bad.append("proof file changed during check")
    for rec in (solver_rec, drat_rec):
        if rec["group_empty_after_reap"] is not True or rec["quarantine_record"] or rec["reader_error"] \
                or rec["capture_over_cap"]:
            bad.append("settlement/capture defect pid %s" % rec["pid"])
    return bad


def terminal_gate():
    """P2: final consumer gate evaluated immediately before a counted status is written."""
    why = []
    if CANCEL.is_set():
        why.append("cancel latched")
    try:
        why += registry_refusals()
        if free_bytes() < FREE_FLOOR:
            why.append("free below in-flight floor at terminal gate")
    except Exception as exc:
        why.append("terminal gate exception %r" % exc)
    return why


def verify_sat(cnf_path, kissat_lines, out_dir, label):
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
    cand = os.path.join(out_dir, label + ".SAT-CANDIDATE.json")
    write_x(cand, {"host_clock": clock(), "array": A, "clauses_all_satisfied": sat_all,
                   "cells_exactly_one": cells_ok, "row_pair_agreements_le_1": rowpair_ok,
                   "column_pair_ordered_pairs_distinct": colpair_ok,
                   "status": "CANDIDATE_UNVERIFIED - notify parent immediately"})
    latch = os.path.join(LANE, "control", "SAT-CANDIDATE-" + label)
    write_bytes_x(latch, cand.encode())
    return {"candidate": cand, "latch": latch, "clauses_all_satisfied": sat_all, "cells": cells_ok,
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


def controls(out_dir):
    """Same-binary positive and intended-reason mutation controls; returns (ok, records)."""
    recs, ok = {}, True
    d = os.path.join(out_dir, "controls")
    os.mkdir(d)
    raw = php_cnf(6, 5)
    cnf = os.path.join(d, "php6x5.cnf")
    h, n = write_bytes_x(cnf, raw)
    exp = (h, n, raw.split(b"\n", 1)[0].decode())
    proof = os.path.join(d, "php6x5.drat")
    ks, kl = run_kissat(cnf, proof, d, "C1", 60)
    ph, pn = sha_file(proof)
    dr, dl = run_drat(cnf, proof, d, "C1", 60)
    c1 = qualify_unsat(exp, ks, kl, ph, pn, dr, dl, sha_file(cnf), sha_file(proof))
    recs["C1_positive_php6x5"] = {"intended": "PASS (sink complete, consumed bytes equal)", "defects": c1,
                                  "kissat": ks, "drat": dr}
    ok &= (c1 == [])
    # C2: truncated CNF (last clause dropped, header unchanged) + valid proof -> early-EOF rejection.
    trunc = raw[: raw.rstrip(b"\n").rfind(b"\n") + 1]
    cnf2 = os.path.join(d, "php6x5-truncated.cnf")
    write_bytes_x(cnf2, trunc)
    dr2, dl2 = run_drat(cnf2, proof, d, "C2", 60)
    c2 = qualify_unsat(exp, ks, kl, ph, pn, dr2, dl2, (h, n), (ph, pn))
    recs["C2_truncated_cnf"] = {"intended": "REJECT: early EOF or proof never consumed", "defects": c2, "drat": dr2}
    ok &= any(("early EOF" in x) or ("clauses less than expected" in x) or ("consumed" in x) for x in c2)
    # C3: proof with one trailing garbage byte -> consumed bytes != file bytes (wrong binary prefix).
    with open(proof, "rb") as f:
        pbytes = f.read()
    proof3 = os.path.join(d, "php6x5-trailing.drat")
    p3h, p3n = write_bytes_x(proof3, pbytes + b"x")
    dr3, dl3 = run_drat(cnf, proof3, d, "C3", 60)
    c3 = qualify_unsat(exp, ks, kl, p3h, p3n, dr3, dl3, (h, n), (p3h, p3n))
    recs["C3_trailing_proof_byte"] = {"intended": "REJECT: consumed bytes / binary prefix", "defects": c3, "drat": dr3}
    ok &= any(("consumed" in x) or ("wrong binary prefix" in x) for x in c3)
    # C4: satisfiable formula (PHP 5x5) checked against the PHP 6x5 proof -> rejection.
    raw4 = php_cnf(5, 5)
    cnf4 = os.path.join(d, "php5x5-sat.cnf")
    h4, n4 = write_bytes_x(cnf4, raw4)
    exp4 = (h4, n4, raw4.split(b"\n", 1)[0].decode())
    dr4, dl4 = run_drat(cnf4, proof, d, "C4", 60)
    c4 = qualify_unsat(exp4, ks, kl, ph, pn, dr4, dl4, (h4, n4), (ph, pn))
    recs["C4_sat_formula_foreign_proof"] = {"intended": "REJECT", "defects": c4, "drat": dr4}
    ok &= (c4 != [])
    # C5: HARD proof cap 4096 B on a hard instance -> sink never writes beyond 4096, trip proof_cap, settled.
    cnf5 = os.path.join(d, "php11x10.cnf")
    write_bytes_x(cnf5, php_cnf(11, 10))
    proof5 = os.path.join(d, "php11x10.drat")
    ks5, kl5 = run_kissat(cnf5, proof5, d, "C5", 60, proof_cap=4096)
    size5 = os.lstat(proof5).st_size
    recs["C5_proof_hard_cap"] = {"intended": "trip=proof_cap, file<=4096 B, reaped, group empty, no quarantine",
                                 "kissat": ks5, "proof_file_bytes": size5}
    ok &= (ks5["trip"] == "proof_cap" and size5 <= 4096 and ks5["group_empty_after_reap"] is True
           and not ks5["quarantine_record"] and ks5["proof_sink"]["over_cap"] is True
           and not ks5["proof_sink"]["thread_alive_after_join"])
    # C6: native solver time limit, no proof file -> self exit without an UNSAT verdict.
    cnf6 = os.path.join(d, "php13x12.cnf")
    write_bytes_x(cnf6, php_cnf(13, 12))
    ks6, kl6 = run_kissat(cnf6, None, d, "C6", 1)
    recs["C6_native_time_limit"] = {"intended": "self exit, no s UNSATISFIABLE", "kissat": ks6,
                                    "status_lines": [s for s in kl6 if s.startswith("s ")]}
    ok &= (ks6["trip"] is None and ks6["returncode"] != 20 and ks6["group_empty_after_reap"] is True
           and "s UNSATISFIABLE" not in kl6)
    # C7: unreadable input (path does not exist) with a proof sink -> no verdict, sink settles, no hang.
    ks7, kl7 = run_kissat(os.path.join(d, "absent.cnf"), os.path.join(d, "absent.drat"), d, "C7", 10)
    recs["C7_no_input_sink_liveness"] = {"intended": "no rc20, reaped, sink thread finished", "kissat": ks7}
    ok &= (ks7["returncode"] != 20 and ks7["group_empty_after_reap"] is True
           and not ks7["proof_sink"]["thread_alive_after_join"])
    return ok, recs


def main():
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if len(sys.argv) != 4:
        print("usage: pilot_file_drat_v4.py GO.json GO_SHA256 OUT_DIR", flush=True)
        return EXIT_PRESTART_REFUSED
    go_path, go_sha, out_dir = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
    if not out_dir.startswith(LANE + "/evidence/pilot-v1/"):
        print("REFUSED: output outside LANE/evidence/pilot-v1/", flush=True)
        return EXIT_PRESTART_REFUSED
    self_sha = sha_file(os.path.abspath(__file__))[0]
    try:
        go = json.loads(read_pinned(go_path, go_sha))
    except Exception as exc:
        print("REFUSED: GO unreadable/pin mismatch %r" % exc, flush=True)
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
    reserve_total = CONTROL_RESERVE + len(ITEMS) * ITEM_RESERVE
    launch = {
        "schema": "PA19-96H-PILOT-LAUNCH-v4", "host_clock": clock(), "owner": "ContinuePA19",
        "go": {"path": go_path, "sha256": go_sha}, "runner": {"path": os.path.abspath(__file__), "sha256": self_sha},
        "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "identity": identity(os.getpid()),
        "cwd": os.getcwd(), "argv": sys.argv, "python": sys.version,
        "binaries": {"kissat": KISSAT, "drat_trim_lane_copy": DRAT, "drat_trim_old": DRAT_OLD},
        "inputs": {"encoder": ENC, "skeleton": SKEL, "items": ITEMS, "registry": REGISTRY,
                   "launch_contract": LAUNCH_CONTRACT, "monitor": MONITOR, "observer_source": OBSERVER_SOURCE_SHA},
        "absolute_child_end_epoch": abs_end, "max_chunk_end_epoch": t_start + MAX_CHUNK,
        "retained_output_reservation_bytes": reserve_total, "output_dir": out_dir,
        "limits": {"solver_s": SOLVER_SECONDS, "check_s": CHECK_SECONDS, "grace_s": GRACE, "term_wait_s": TERM_WAIT,
                   "proof_cap_hard": PROOF_CAP, "log_cap_hard": LOG_CAP, "lane_rss_trip": LANE_RSS_TRIP,
                   "free_floor": FREE_FLOOR, "fresh_base": FRESH_BASE},
        "exit_codes": {"0": "plan complete (each item terminal UNSAT/UNKNOWN); not a science verdict",
                       "10": "SAT candidate", "20": "controls failed", "30": "admission refused",
                       "40": "owner cancel", "50": "safety stop", "60": "exception", "70": "prestart refused"},
    }
    write_x(os.path.join(out_dir, "launch-record.json"), launch)
    print("LAUNCH_RECORD", os.path.join(out_dir, "launch-record.json"), flush=True)
    summary = {"schema": "PA19-96H-PILOT-SUMMARY-v4", "items": {}, "controls_ok": None, "stopped": None,
               "terminal_policy": "exit code reports runner execution only; per-item records carry the scientific "
                                  "status; an item counts only if status UNSAT passed qualify_unsat AND the terminal "
                                  "gate; case closure is decided by the parent audit, not by this runner"}
    code = EXIT_EXCEPTION

    def gate(projected, remaining_reserve):
        why = registry_refusals()
        fb = free_bytes()
        if fb < FRESH_BASE + projected:
            why.append(f"fresh free {fb} < 12.2e9 + {projected}")
        if fb - remaining_reserve < FREE_FLOOR:
            why.append(f"free {fb} - remaining reservations {remaining_reserve} < 12e9")
        if time.time() + ITEM_WORST_SECONDS > min(abs_end, OWNED_SETTLED_BY - 180):
            why.append("chunk-fit/absolute deadline")
        if CANCEL.is_set():
            why.append("owner cancel")
        why += stability_refusals(projected)
        return why, fb

    try:
        if sha_file(DRAT_OLD[0])[0] != DRAT_OLD[1] or sha_file(KISSAT[0])[0] != KISSAT[1]:
            raise RuntimeError("binary pin mismatch")
        if sha_file(DRAT)[0] != DRAT_OLD[1] or os.lstat(DRAT).st_ino == os.lstat(DRAT_OLD[0]).st_ino:
            raise RuntimeError("vendored drat-trim mismatch or shared inode")
        why, fb = gate(CONTROL_RESERVE, reserve_total)
        if why:
            summary["stopped"] = {"phase": "controls_gate", "why": why, "free": fb}
            code = EXIT_ADMISSION_REFUSED
            return code
        ok, recs = controls(out_dir)
        summary["controls_ok"] = ok
        summary["controls_record_sha256"] = write_x(os.path.join(out_dir, "controls.json"), recs)
        if CANCEL.is_set():
            summary["stopped"] = {"phase": "controls", "why": ["owner cancel"]}
            code = EXIT_CANCELLED
            return code
        if not ok:
            summary["stopped"] = {"phase": "controls", "why": ["a control did not behave as intended"]}
            code = EXIT_CONTROLS_FAILED
            return code
        read_pinned(ENC[0], ENC[1])
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
        E = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(E)
        D = json.loads(read_pinned(*SKEL))
        special = [p for p in D["profiles"] if list(p) != P0]
        remaining = len(ITEMS) * ITEM_RESERVE
        for it in ITEMS:
            label = it["id"].replace(":", "_")
            rec = {"id": it["id"], "status": "UNKNOWN", "count_for_scientific_coverage": False,
                   "host_clock_start": clock()}
            why, fb = gate(ITEM_RESERVE, remaining)
            rec["gate"] = {"why": why, "free": fb}
            if why:
                rec["reason"] = "admission refused"
                write_x(os.path.join(out_dir, label + ".record.json"), rec)
                summary["items"][it["id"]] = {"status": "UNKNOWN", "reason": "admission refused"}
                summary["stopped"] = {"phase": "item_gate", "item": it["id"], "why": why}
                code = EXIT_CANCELLED if CANCEL.is_set() else EXIT_ADMISSION_REFUSED
                return code
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
            proof_path = os.path.join(out_dir, label + ".drat")
            ks, kl = run_kissat(cnf_path, proof_path, out_dir, label, SOLVER_SECONDS)
            rec["solver"] = ks
            rec["solver_status_lines"] = [s for s in kl if s.startswith("s ")]
            safety = bool(ks["quarantine_record"]) or ks["group_empty_after_reap"] is not True \
                or (ks["proof_sink"] or {}).get("thread_alive_after_join", False)
            if ks["returncode"] == 10 and rec["solver_status_lines"] == ["s SATISFIABLE"] and ks["stop"] == "self":
                rec["status"] = "SAT_CANDIDATE"
                rec["sat"] = verify_sat(cnf_path, kl, out_dir, label)
                write_x(os.path.join(out_dir, label + ".record.json"), rec)
                summary["items"][it["id"]] = {"status": "SAT_CANDIDATE", "sat": rec["sat"]}
                summary["stopped"] = {"phase": "sat_candidate", "item": it["id"]}
                code = EXIT_SAT_CANDIDATE
                return code
            sink_ok = sink_complete(ks["proof_sink"])
            if sink_ok:
                rec["proof"] = {"sha256": ks["proof_sink"]["sha256_of_written"], "bytes": ks["proof_sink"]["written"]}
            if ks["returncode"] == 20 and ks["stop"] == "self" and ks["trip"] is None and not safety \
                    and sink_ok and not CANCEL.is_set():
                dr, dl = run_drat(cnf_path, proof_path, out_dir, label, CHECK_SECONDS)
                rec["checker"] = dr
                rec["checker_status_lines"] = [s for s in dl if s.startswith("s ")]
                rec["checker_parse_lines"] = [s for s in dl if s.startswith("c parsing") or s.startswith("c finished parsing")]
                post_cnf, post_proof = sha_file(cnf_path), sha_file(proof_path)
                rec["post_check_hashes"] = {"cnf": list(post_cnf), "proof": list(post_proof)}
                rec["defects"] = qualify_unsat(it["cnf"], ks, kl, rec["proof"]["sha256"], rec["proof"]["bytes"],
                                               dr, dl, post_cnf, post_proof)
                safety = safety or bool(dr["quarantine_record"]) or dr["group_empty_after_reap"] is not True
                rec["terminal_gate"] = terminal_gate()
                if not rec["defects"] and not rec["terminal_gate"] and not safety:
                    rec["status"] = "UNSAT"
                    rec["count_for_scientific_coverage"] = True
            else:
                rec["reason"] = "no self-exit rc20 verdict with a complete proof sink (or trip/cancel/safety)"
            rec["host_clock_end"] = clock()
            write_x(os.path.join(out_dir, label + ".record.json"), rec)
            summary["items"][it["id"]] = {k: rec.get(k) for k in ("status", "count_for_scientific_coverage",
                                                                  "defects", "terminal_gate", "reason", "proof")}
            remaining -= ITEM_RESERVE
            if safety:
                summary["stopped"] = {"phase": "safety", "item": it["id"]}
                code = EXIT_SAFETY_STOP
                return code
            if CANCEL.is_set():
                summary["stopped"] = {"phase": "owner_cancel", "item": it["id"]}
                code = EXIT_CANCELLED
                return code
        code = EXIT_PLAN_COMPLETE
        return code
    except BaseException as exc:
        summary["stopped"] = {"phase": "exception", "error": repr(exc)}
        code = EXIT_EXCEPTION
        return code
    finally:
        summary["exit_code"] = code
        summary["host_clock_end"] = clock()
        summary["settlement"] = "every child is reaped in Child.settle before control returns; per-child " \
                                "group_empty_after_reap/quarantine and proof-sink fields are in records; no child " \
                                "is started after an exception"
        write_x(os.path.join(out_dir, "summary.json"), summary)
        print("SUMMARY", os.path.join(out_dir, "summary.json"), "exit", code, flush=True)


if __name__ == "__main__":
    sys.exit(main())
