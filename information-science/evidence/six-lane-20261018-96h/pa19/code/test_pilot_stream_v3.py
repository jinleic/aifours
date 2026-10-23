#!/usr/bin/env python3
"""P-STREAM runner v2 offline tests, test v3 = code/test_pilot_stream_v2.py (de278c39..., preserved) adapted to runner v2
(code/pilot_stream_drat_ms06_v2.py / _ms09_v2.py) and to the parent-routed Codex review (af15a4e1...):
  - cooperative budget kept from v2 (monotonic deadline, sliced bounded joins, daemon helper threads, stamp-only
    SIGTERM/SIGINT, terminal result.json always written; no SIGALRM, kill, ulimit or tool deadline);
  - host timestamps only through the runner's OWNED, BOUNDED /bin/date Helper (R.clock), never after a stamped
    signal; a failed read is recorded as null (never invented);
  - the qualification matrix compares COMPLETE sorted defect-ID lists (R.defect_ids) per single-scenario mutation,
    including conflicting/duplicated canonical records and the C3/C4 intended-reason shapes;
  - new deterministic checks: V8 continuation after a flushed over-long line (scripted reader, adversarial and
    genuine-line alignments), V13 capture accounting, V5 proof-RAM charge while a feeder holds the tuple, V6
    abandon() error reporting, V1 libproc reads of this test process (identity fields, RSS, listings), V4 run-tree
    census / lane usage / out-dir ancestry on test-owned trees, V4 monitor provenance header, V12 item shapes,
    V1 helper refusal (unreaped owned process, stamped cancel) and V2 output guard;
  - constant/default pinning is not tested (not behavioral evidence); chunk fit is proven separately by a native
    prestart-refusal scenario.
Preservation scope (T1:148 disposition by the parent): the only rename is of a FIFO this test created inside
OUT_DIR/work (moved, never deleted); the only permission change is chmod 000 -> 0755 of a directory this test
created inside OUT_DIR/work; no other path is created, changed, moved or deleted.

NOT TO BE RUN without a parent GO/WINDOW or parent supervision (small-probe rules: frozen source; receipt with PID
written before any work; <= 300 s; one process besides the bounded /bin/date helper; outputs only under
LANE/evidence/probes/).  No solver/checker binary is executed.

usage: test_pilot_stream_v3.py RUNNER.py RUNNER_SHA256 OUT_DIR
  RUNNER: code/pilot_stream_drat_ms06_v2.py or code/pilot_stream_drat_ms09_v2.py (identical transport code).
  OUT_DIR must not exist; its parent must be LANE/evidence/probes.  Writes OUT_DIR/receipt.json first and
  OUT_DIR/result.json last (both exclusive); FIFOs, pipes and fixture trees only inside OUT_DIR/work.
Exit 0 ALL_OK; 1 FAILURES or SETUP_FAILED; 2 BUDGET_EXHAUSTED; 3 CANCELLED; 70 refused start (no OUT_DIR);
71 result.json could not be written.
"""
import copy
import datetime
import hashlib
import importlib.util
import json
import os
import signal
import sys
import threading
import time
import traceback
import types

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
BUDGET_S = 280
PROV_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"
RESULT_RESERVE_S = 15                 # B1: kept free for the terminal result
SLICE_S = 0.2                         # B1: wait slice (cancel/budget noticed within this)
STATE = {"t0": None, "deadline": None, "signal": None}


class BudgetExhausted(Exception):
    pass


class Cancelled(Exception):
    pass


def on_signal(signum, frame):
    """B2: lock-free; only stamps the first signal number."""
    if STATE["signal"] is None:
        STATE["signal"] = signum


def remaining():
    return STATE["deadline"] - time.monotonic()


def check():
    if STATE["signal"] is not None:
        raise Cancelled("signal %d stamped" % STATE["signal"])
    if remaining() <= RESULT_RESERVE_S:
        raise BudgetExhausted("budget exhausted: %.1f s left, result reserve %d s" % (remaining(), RESULT_RESERVE_S))


def need(seconds, what):
    check()
    if remaining() - RESULT_RESERVE_S < seconds:
        raise BudgetExhausted("%s may take up to %.0f s; only %.1f s left before the result reserve"
                              % (what, seconds, remaining() - RESULT_RESERVE_S))


def spawn(target, args, name):
    th = threading.Thread(target=target, args=args, name=name, daemon=True)
    th.start()
    return th


def wait_thread(th, cap, what):
    """B1: cooperative bounded join (at most `cap` s, in SLICE_S slices); raises Cancelled/BudgetExhausted when a
    signal is stamped or the budget less the reserve runs out; True iff the thread ended."""
    end = time.monotonic() + cap
    while th.is_alive():
        check()
        left = end - time.monotonic()
        if left <= 0:
            return False
        th.join(max(0.0, min(SLICE_S, left, remaining() - RESULT_RESERVE_S)))
    return True


def buffer_finish(R, b, connected):
    """B1: waits for a connected collector cooperatively; ProofBuffer.finish() with a live collector may unblock
    (<= SINK_UNBLOCK) and join (<= STREAM_JOIN), so it is entered only if the budget can absorb that bound."""
    if connected:
        wait_thread(b.thread, 60, "proof collector")
    if b.thread.is_alive():
        need(R.SINK_UNBLOCK + R.STREAM_JOIN + 1, "ProofBuffer.finish")
    else:
        check()
    return b.finish()


def feeder_finish(f):
    """B1: a started non-hold feeder is awaited cooperatively; Feeder.finish() (which releases a held feed itself)
    then joins for at most min(10 s, remaining budget less the reserve)."""
    if f.started and f.mode != "hold":
        wait_thread(f.thread, 60, "feeder")
    need(1, "Feeder.finish")
    return f.finish(max(0.0, min(10.0, remaining() - RESULT_RESERVE_S)))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def write_x(path, obj):
    data = (json.dumps(obj, indent=1, sort_keys=True) + "\n").encode()
    with open(path, "xb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    return sha(data)


def det_bytes(n, seed):
    out = bytearray()
    i = 0
    while len(out) < n:
        out += hashlib.sha256(b"%d:%d" % (seed, i)).digest()
        i += 1
    return bytes(out[:n])


def fifo_writer(path, chunks, res):
    try:
        fd = os.open(path, os.O_WRONLY)
        try:
            for c in chunks:
                mv = memoryview(c)
                while mv:
                    k = os.write(fd, mv)
                    mv = mv[k:]
        finally:
            os.close(fd)
        res["ok"] = True
    except Exception as exc:
        res["error"] = repr(exc)


def drain(fd, out, limit=None):
    """Plays the checker's stdin: reads to EOF (or closes after `limit` bytes)."""
    h, n = hashlib.sha256(), 0
    try:
        while limit is None or n < limit:
            b = os.read(fd, 65536 if limit is None else min(65536, limit - n))
            if not b:
                break
            h.update(b)
            n += len(b)
            out.setdefault("tail", b"")
            out["tail"] = (out["tail"] + b)[-8:]
    finally:
        os.close(fd)
    out.update(sha=h.hexdigest(), n=n)


def blocks_of(R, data):
    return tuple(data[i:i + R.FEED_BLOCK] for i in range(0, len(data), R.FEED_BLOCK))




def host_clock(R):
    """Host clock through the runner's owned bounded helper; None after a stamped signal or without the runner."""
    if R is None or STATE["signal"] is not None:
        return None
    return R.clock()


def t_buffer_roundtrip(R, W):
    data = det_bytes(3 * R.FEED_BLOCK + 12345, 1)
    b = R.ProofBuffer(os.path.join(W, "t1.fifo"), 10 * R.FEED_BLOCK)
    res = {}
    th = spawn(fifo_writer, (b.fifo_path, [data[i:i + 7777] for i in range(0, len(data), 7777)], res), "t1-writer")
    assert wait_thread(th, 60, "fifo writer"), "fifo writer did not finish"
    rec = buffer_finish(R, b, True)
    assert res.get("ok"), res
    assert R.sink_complete(rec), rec
    assert rec["retained"] == rec["received"] == len(data) and rec["sha256_of_retained"] == sha(data)
    assert isinstance(b.blocks, tuple) and all(len(x) == R.FEED_BLOCK for x in b.blocks[:-1])
    assert b"".join(b.blocks) == data and rec["buffer_rehash"] == [sha(data), len(data)]
    assert R.buffer_charge() == len(data), R.buffer_charge()
    b.release()
    assert b.blocks == () and R.buffer_charge() == 0
    return {"bytes": len(data), "blocks": rec["blocks"]}


def t_buffer_cap(R, W):
    b = R.ProofBuffer(os.path.join(W, "t2.fifo"), 4096)
    res = {}
    th = spawn(fifo_writer, (b.fifo_path, [b"y" * 1000] * 10, res), "t2-writer")
    assert wait_thread(th, 60, "fifo writer"), "fifo writer did not finish"
    rec = buffer_finish(R, b, True)
    b.release()
    assert res.get("ok"), res
    assert rec["over_cap"] and rec["retained"] <= 4096 and rec["received"] == 10000
    assert rec["discarded"] == 10000 - rec["retained"] and not R.sink_complete(rec)
    assert rec["thread_alive_after_join"] is False
    return {"retained": rec["retained"], "discarded": rec["discarded"]}


def t_buffer_never_connected(R, W):
    b = R.ProofBuffer(os.path.join(W, "t3.fifo"), 4096)
    rec = buffer_finish(R, b, False)
    b.release()
    assert rec["unblocked_by_runner"] and rec["eof"] and rec["retained"] == 0
    assert rec["thread_alive_after_join"] is False and not R.sink_complete(rec)
    return {"unblocked_by_runner": True}


def t_buffer_fifo_replaced(R, W):
    p = os.path.join(W, "t4.fifo")
    b = R.ProofBuffer(p, 4096)
    res = {}
    th = spawn(fifo_writer, (p, [b"z" * 100], res), "t4-writer")
    assert wait_thread(th, 60, "fifo writer"), "fifo writer did not finish"
    assert wait_thread(b.thread, 60, "proof collector"), "proof collector did not finish"
    os.rename(p, p + ".moved")
    os.mkfifo(p, 0o600)
    n0 = len(R.LATCH)
    rec = buffer_finish(R, b, True)
    b.release()
    latched = R.LATCH[n0:]
    del R.LATCH[n0:]
    assert rec["fifo_same_inode_still_fifo"] is False and not rec["sink_settled"] and not R.sink_complete(rec)
    assert any("proof FIFO replaced" in x for x in latched), latched
    return {"latched": latched, "preservation_scope": "only the test-created FIFO OUT_DIR/work/t4.fifo was moved "
                                                      "(to t4.fifo.moved), never deleted; a new FIFO was created at "
                                                      "the old path"}


def t_feeder_plain(R, W):
    data = det_bytes(2 * R.FEED_BLOCK + 70000, 2)
    f = R.Feeder(blocks_of(R, data), "plain")
    rfd, f.rfd = f.rfd, None
    out = {}
    th = spawn(drain, (rfd, out), "drain")
    f.start()
    assert wait_thread(th, 60, "drain"), "drain did not finish"
    rec = feeder_finish(f)
    assert out["n"] == len(data) and out["sha"] == sha(data)
    assert rec["fed_bytes"] == rec["proof_bytes_fed"] == len(data) and rec["fed_sha256"] == sha(data)
    assert rec["delivery_error"] is None and rec["exception"] is None and rec["close_error"] is None
    assert rec["thread_alive_after_join"] is False and rec["undelivered_proof_bytes"] == 0 and f.blocks == ()
    return {"fed": rec["fed_bytes"]}


def t_feeder_suffix(R, W):
    data = det_bytes(5000, 3)
    f = R.Feeder(blocks_of(R, data), "suffix")
    rfd, f.rfd = f.rfd, None
    out = {}
    th = spawn(drain, (rfd, out), "drain")
    f.start()
    assert wait_thread(th, 60, "drain"), "drain did not finish"
    rec = feeder_finish(f)
    assert out["n"] == len(data) + len(R.SUFFIX) and out["sha"] == sha(data + R.SUFFIX)
    assert rec["fed_bytes"] == len(data) + 1 and rec["proof_bytes_fed"] == len(data)
    assert rec["fed_sha256"] == sha(data + R.SUFFIX) != sha(data)
    return {"fed": rec["fed_bytes"]}


def t_feeder_hold_epipe(R, W):
    data = det_bytes(5000, 4)
    f = R.Feeder(blocks_of(R, data), "hold")
    rfd, f.rfd = f.rfd, None
    os.close(rfd)                     # the checker exited before reading stdin (C7b)
    f.start()
    rec = feeder_finish(f)
    assert rec["hold_released_by_event"] is True and rec["fed_bytes"] == 0
    assert str(rec["delivery_error"]).startswith("EPIPE") and rec["thread_alive_after_join"] is False
    assert rec["undelivered_proof_bytes"] == len(data)
    return {"delivery_error": rec["delivery_error"]}


def t_feeder_midstream_close(R, W):
    data = det_bytes(2 * R.FEED_BLOCK, 5)
    f = R.Feeder(blocks_of(R, data), "plain")
    rfd, f.rfd = f.rfd, None
    out = {}
    th = spawn(drain, (rfd, out, 100000), "drain-limited")
    f.start()
    assert wait_thread(th, 60, "drain"), "drain did not finish"
    rec = feeder_finish(f)
    assert out["n"] == 100000 and rec["fed_bytes"] < len(data)
    assert str(rec["delivery_error"]).startswith("EPIPE") and rec["thread_alive_after_join"] is False
    assert rec["proof_bytes_fed"] == rec["fed_bytes"] and rec["undelivered_proof_bytes"] > 0
    return {"fed": rec["fed_bytes"], "read_by_peer": out["n"]}


def t_feeder_guards(R, W):
    ok_unknown = ok_list = False
    try:
        R.Feeder((b"a",), "alter")
    except RuntimeError:
        ok_unknown = True
    try:
        R.Feeder([b"a"], "plain")
    except RuntimeError:
        ok_list = True
    f = R.Feeder((b"a",), "plain")
    fds = (f.rfd, f.wfd)
    f.abandon()
    closed = []
    for fd in fds:
        try:
            os.fstat(fd)
            closed.append(False)
        except OSError:
            closed.append(True)
    assert ok_unknown and ok_list and f.rfd is None and f.wfd is None and all(closed), (ok_unknown, ok_list, closed)
    rec = f.finish(1)
    assert rec["started"] is False and rec["fed_bytes"] == 0
    return {"abandon_closed_both_ends": True}


def pipe_writer(w, raw, step, res):
    """Plays the checker's stdout: writes `raw` in `step` slices (partial writes completed), then closes."""
    try:
        for i in range(0, len(raw), step):
            mv = memoryview(raw)[i:i + step]
            while mv:
                k = os.write(w, mv)
                mv = mv[k:]
        res["ok"] = True
    except Exception as exc:
        res["error"] = repr(exc)
    finally:
        os.close(w)


def run_filter(R, W, name, raw, step):
    r, w = os.pipe()
    c = R.Child.__new__(R.Child)
    c.proc = types.SimpleNamespace(stdout=os.fdopen(r, "rb"))
    cap = os.path.join(W, name)
    c.capture = open(cap, "xb")
    c.captured, c.capture_written, c.over_cap, c.reader_error, c.filt = 0, 0, False, None, R.new_filter()
    rd = spawn(c._read, (), name + "-reader")
    wres = {}
    wr = spawn(pipe_writer, (w, raw, step, wres), name + "-writer")
    assert wait_thread(wr, 60, "pipe writer") and wres.get("ok"), wres
    assert wait_thread(rd, 60, "capture reader"), "capture reader did not finish"
    with open(cap, "rb") as fh:
        kept = fh.read()
    return c, kept


def t_filter(R, W):
    lines = [b"\rc reading proof from stdin\n",
             b"\rc parsing input formula with 10 variables and 20 clauses\n",
             b"\rc WARNING: detected and deleted duplicate literal -3 at position 1 of proof line 7\n",
             b"\rc WARNING: detected and deleted duplicate literal 3 at position 2 of proof line 20\n",
             b"\rc WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 21\n",
             b"\rc WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 21 x\n",
             b"c WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 22\n",
             b"\rc WARNING: detected and deleted duplicate literal 0 at position 2 of proof line 23\n",
             b"\rc finished parsing, read 100 bytes from proof file\n",
             b"\rs VERIFIED\n",
             b"\rc unterminated tail"]
    raw = b"".join(lines)
    dropped = (2, 3, 4)
    want = b"".join(x for i, x in enumerate(lines) if i not in dropped)
    c, kept = run_filter(R, W, "filter.out", raw, 13)
    f = c.filt
    assert c.reader_error is None and f["raw_eof"] is True
    assert f["raw_bytes"] == len(raw) and f["raw_sha"].hexdigest() == sha(raw)
    assert kept == want and c.captured == c.capture_written == len(want)
    assert (f["dup_low"], f["dup_high"]) == (2, 1) and f["dup_bytes"] == sum(len(lines[i]) for i in dropped)
    assert f["header_clauses"] == 20 and f["tail"] == len(lines[-1])
    assert f["raw_bytes"] == c.captured + f["dup_bytes"]
    return {"kept_bytes": c.captured, "dup_bytes": f["dup_bytes"]}


def t_filter_long_line(R, W):
    raw = b"B" * (3 * 65536 + 5) + b"\rc WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 9\n"
    c, kept = run_filter(R, W, "filter-long.out", raw, 65536)
    f = c.filt
    assert c.reader_error is None and kept == raw and f["dup_bytes"] == 0 and f["raw_bytes"] == c.captured
    assert f["flushes"] >= 1                       # a 196 KiB line is always flushed at least once (read1 <= 64 KiB)
    return {"kept_bytes": c.captured, "flushes": f["flushes"]}



class ScriptedStdout:
    """Deterministic read1() source for the capture filter (each call returns the next scripted chunk)."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.closed = False

    def read1(self, n):
        return self.chunks.pop(0) if self.chunks else b""

    def close(self):
        self.closed = True


def scripted_filter(R, W, name, chunks):
    c = R.Child.__new__(R.Child)
    c.proc = types.SimpleNamespace(stdout=ScriptedStdout(chunks))
    cap = os.path.join(W, name)
    c.capture = open(cap, "xb")
    c.captured, c.capture_written, c.over_cap, c.reader_error, c.filt = 0, 0, False, None, R.new_filter()
    c._read()                                      # never blocks: the script is finite
    with open(cap, "rb") as fh:
        kept = fh.read()
    return c, kept


DUPL = b"\rc WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 9\n"


def t_filter_continuation_adversarial(R, W):
    """V8: the flush lands exactly before a DUP-shaped tail of the same physical line: the tail must be kept."""
    chunks = [b"B" * R.PENDING_MAX, b"B", DUPL]
    c, kept = scripted_filter(R, W, "cont-adv.out", chunks)
    f = c.filt
    raw = b"".join(chunks)
    assert c.reader_error is None and f["raw_eof"] is True and f["flushes"] == 1
    assert kept == raw and f["dup_bytes"] == 0 and (f["dup_low"], f["dup_high"]) == (0, 0)
    assert f["raw_bytes"] == c.captured + f["dup_bytes"] == len(raw)
    return {"kept_bytes": len(kept), "flushes": f["flushes"]}


def t_filter_continuation_genuine_line(R, W):
    """V8: after the flushed line ends at its newline, a genuine DUP line is dropped and counted again."""
    chunks = [b"B" * (R.PENDING_MAX + 1), b"\n" + DUPL]
    c, kept = scripted_filter(R, W, "cont-gen.out", chunks)
    f = c.filt
    raw = b"".join(chunks)
    assert c.reader_error is None and f["flushes"] == 1 and kept == raw[:-len(DUPL)]
    assert f["dup_bytes"] == len(DUPL) and (f["dup_low"], f["dup_high"]) == (0, 1)
    assert f["raw_bytes"] == c.captured + f["dup_bytes"] == len(raw)
    return {"kept_bytes": len(kept), "dup_bytes": f["dup_bytes"]}


def t_capture_accounting(R, W):
    """V13: non-dropped bytes vs bytes physically written to the capped file (LOG_CAP patched for this test)."""
    saved = R.LOG_CAP
    R.LOG_CAP = 100
    try:
        c, kept = scripted_filter(R, W, "cap.out", [b"x" * 60 + b"\n", b"y" * 89 + b"\n"])
    finally:
        R.LOG_CAP = saved
    assert c.captured == 150 and c.capture_written == 100 and c.over_cap is True and len(kept) == 100
    return {"nondropped": c.captured, "file_bytes": c.capture_written}


def t_feeder_holder_charge(R, W):
    """V5: proof RAM stays charged while a feeder holds the frozen tuple after the buffer's own release."""
    data = det_bytes(2 * R.FEED_BLOCK + 3, 7)
    b = R.ProofBuffer(os.path.join(W, "t5h.fifo"), 4 * R.FEED_BLOCK)
    res = {}
    th = spawn(fifo_writer, (b.fifo_path, [data], res), "t5h-writer")
    assert wait_thread(th, 60, "fifo writer") and res.get("ok"), res
    rec = buffer_finish(R, b, True)
    assert R.sink_complete(rec) and R.buffer_charge() == len(data)
    f = R.Feeder(b.blocks, "plain", label="holder-test")
    b.release()
    assert b.released and R.buffer_charge() == len(data), R.buffer_charge()
    assert b.accounting()["still_held_by_feeders"] == ["holder-test"]
    errs = f.abandon()
    assert errs == [] and f.blocks == () and f.rfd is None and f.wfd is None
    assert R.buffer_charge() == 0 and b.accounting()["still_held_by_feeders"] == []
    return {"charged_while_held": len(data)}


def t_libproc_self(R, W):
    """V1: libproc reads of this test process (no child process): BSD identity fields, RSS, group/parent listings."""
    me = os.getpid()
    ident, err = R.bsd_identity(me)
    assert err is None and ident["pid"] == me and ident["ppid"] == os.getppid() and ident["pgid"] == os.getpgid(0), ident
    assert ident["comm"] and len(ident["start"]) == 2 and ident["start"][0] > 0
    rss = R.task_rss(me)
    assert isinstance(rss, int) and rss > 0
    assert me in R.list_pids(R.PROC_PGRP_ONLY, os.getpgid(0))
    assert me in R.list_pids(R.PROC_PPID_ONLY, os.getppid())
    return {"comm": ident["comm"], "rss": rss}


def t_tree_census_and_usage(R, W):
    """V4/V2: complete census (every kind, hard links, symlink, FIFO) and lane usage on a test-owned tree."""
    root = os.path.join(W, "tree")
    os.mkdir(root)
    os.mkdir(os.path.join(root, "sub"))
    with open(os.path.join(root, "a.txt"), "xb") as fh:
        fh.write(b"0123456789")
    with open(os.path.join(root, "sub", "b.bin"), "xb") as fh:
        fh.write(b"x" * 20)
    os.link(os.path.join(root, "a.txt"), os.path.join(root, "hl"))
    os.symlink("a.txt", os.path.join(root, "ln"))
    os.mkfifo(os.path.join(root, "f.fifo"), 0o600)
    snap = R.run_tree_census(root)
    kinds = {os.path.relpath(p, root): v[0] for p, v in snap.items()}
    assert kinds == {"sub": "dir", "a.txt": "file", "sub/b.bin": "file", "hl": "file", "ln": "symlink",
                     "f.fifo": "fifo"}, kinds
    assert snap[os.path.join(root, "ln")][2] == len("a.txt") and snap[os.path.join(root, "f.fifo")][2] == 0
    assert R.lane_usage(root) == 10 + 20 + len("a.txt")
    with open(os.path.join(root, "c.txt"), "xb") as fh:      # an added entry is visible to the comparison
        fh.write(b"z")
    snap2 = R.run_tree_census(root)
    assert set(snap2) - set(snap) == {os.path.join(root, "c.txt")}
    return {"entries": len(snap2), "usage": R.lane_usage(root)}


def t_tree_census_fail_closed(R, W):
    """V4: an unreadable directory makes the census raise (fail closed); permissions restored afterwards."""
    root = os.path.join(W, "tree2")
    os.mkdir(root)
    locked = os.path.join(root, "locked")
    os.mkdir(locked)
    os.chmod(locked, 0)
    try:
        raised = False
        try:
            R.run_tree_census(root)
        except OSError:
            raised = True
        raised_usage = False
        try:
            R.lane_usage(root)
        except OSError:
            raised_usage = True
    finally:
        os.chmod(locked, 0o755)
    assert raised and raised_usage
    return {"census_raised": True, "usage_raised": True}


def t_out_dir_ancestry(R, W):
    """V4: direct-child rule, symlink ancestor refusal and existing-path refusal on a test-owned tree."""
    real = os.path.join(W, "real")
    pilot = os.path.join(real, "pilot")
    os.makedirs(pilot)
    alias = os.path.join(W, "alias")
    os.symlink(real, alias)
    assert R.out_dir_refusal(os.path.join(pilot, "run-x"), pilot) is None
    why = R.out_dir_refusal(os.path.join(alias, "pilot", "run-x"), os.path.join(alias, "pilot"))
    assert why is not None and "not a real directory" in why, why
    os.mkdir(os.path.join(pilot, "run-y"))
    assert R.out_dir_refusal(os.path.join(pilot, "run-y"), pilot) == "output path exists"
    assert "direct child" in R.out_dir_refusal(os.path.join(pilot, "a", "b"), pilot)
    return {"symlink_ancestor_refusal": why}


def _iso(t):
    return datetime.datetime.fromtimestamp(t).astimezone().isoformat(timespec="seconds")


def t_monitor_provenance_header(R, W):
    """V4: a sample-only monitor is refused; the same samples behind the pinned observer_start header pass."""
    now = time.time()
    samples = [json.dumps({"t": _iso(now - 290 + 10 * i), "free": 100_000_000_000, "floor_bytes": 12_000_000_000,
                           "scope": R.SAMPLE_SCOPE}) for i in range(30)]
    header = json.dumps({"event": "observer_start", "at": _iso(now - 300), "pid": 1, "pgid": 1, "cwd": R.OBSERVER_CWD,
                         "source_sha256": R.OBSERVER_SOURCE_SHA})
    bare, full = os.path.join(W, "mon-bare.jsonl"), os.path.join(W, "mon-full.jsonl")
    with open(bare, "xb") as fh:
        fh.write(("\n".join(samples) + "\n").encode())
    with open(full, "xb") as fh:
        fh.write(("\n".join([header] + samples) + "\n").encode())
    saved = R.MONITOR
    try:
        R.MONITOR = bare
        got_bare = R.stability_refusals(1)
        R.MONITOR = full
        got_full = R.stability_refusals(1)
    finally:
        R.MONITOR = saved
    assert got_bare == ["monitor lacks the pinned observer_start provenance header"], got_bare
    assert got_full == [], got_full
    return {"bare": got_bare, "full": got_full}


def t_item_shapes(R, W):
    """V12: exact item types and shapes for both families (FAMILY patched for the test, then restored)."""
    good9 = {"id": "b00025:00100-00373", "b": 25, "lo": 100, "hi": 373, "denominator": 374,
             "list": ("/x/ext.json", "a" * 64), "cnf": ("b" * 64, 9568889, "p cnf 13744 443162")}
    good6 = {"id": "ms06:b00318:direct", "b": 318, "cnf": ("c" * 64, 8784502, "p cnf 12391 406388")}
    bad9 = [dict(good9, lo=-1), dict(good9, lo=True), dict(good9, lo=100.0), dict(good9, hi=374),
            dict(good9, lo=200, hi=150), dict(good9, id="b00025:100-373"), dict(good9, list=("/x", "A" * 64)),
            dict(good9, cnf=("b" * 64, 9568889, "p cnf 0 1")), dict(good9, denominator=False), dict(good9, b=-25)]
    bad6 = [dict(good6, lo=0), dict(good6, id="ms06:b318:direct"), dict(good6, cnf=("c" * 63, 1, "p cnf 1 1"))]
    saved = R.FAMILY
    try:
        R.FAMILY = "ms09"
        r9 = (R.item_shape_refusals(good9), [R.item_shape_refusals(x) for x in bad9])
        R.FAMILY = "ms06"
        r6 = (R.item_shape_refusals(good6), [R.item_shape_refusals(x) for x in bad6])
    finally:
        R.FAMILY = saved
    assert r9[0] == [] and all(r9[1]), r9
    assert r6[0] == [] and all(r6[1]), r6
    return {"ms09_refused": len(bad9), "ms06_refused": len(bad6)}


def t_helper_refusals_and_clock(R, W):
    """V1: the helper is refused (no process) while an owned process is unreaped or a cancel is stamped; the normal
    path returns one /bin/date line through the owned bounded helper."""
    fake = types.SimpleNamespace(proc=types.SimpleNamespace(returncode=None))
    n_helpers, n_latch = len(R.HELPERS), len(R.LATCH)
    R.OWNED.append(fake)
    try:
        refused = False
        try:
            R.Helper(R.DATE_ARGV).run()
        except R.HelperRefused:
            refused = True
    finally:
        R.OWNED.remove(fake)
    latched = R.LATCH[n_latch:]
    del R.LATCH[n_latch:]
    assert refused and len(R.HELPERS) == n_helpers and latched, (refused, latched)
    R.STATE["cancel_order"] = 1
    try:
        refused_cancel = False
        try:
            R.Helper(R.DATE_ARGV).run()
        except R.HelperRefused:
            refused_cancel = True
    finally:
        R.STATE["cancel_order"] = None
    assert refused_cancel and len(R.HELPERS) == n_helpers and len(R.LATCH) == n_latch
    check()
    stamp = R.clock()
    assert isinstance(stamp, str) and R.DATE_RE.fullmatch((stamp + "\n").encode()), stamp
    last = R.HELPERS[-1]
    assert last.proc is not None and last.proc.returncode == 0 and not last.quarantined
    return {"clock": stamp, "helpers": len(R.HELPERS)}


def t_output_guard(R, W):
    """V2: the hard output guard refuses a write that would exceed the run reservation, and latches."""
    saved = (R.STATE["output_limit"], R.STATE["written"])
    n_latch = len(R.LATCH)
    R.STATE["output_limit"], R.STATE["written"] = 10, 0
    try:
        R.charge_output(5)
        raised = False
        try:
            R.charge_output(6)
        except RuntimeError:
            raised = True
        written = R.STATE["written"]
    finally:
        R.STATE["output_limit"], R.STATE["written"] = saved
    latched = R.LATCH[n_latch:]
    del R.LATCH[n_latch:]
    assert raised and written == 5 and len(latched) == 1
    return {"refused_at": 11}


def t_other_admitted_reservations(R, W):
    """V2: other admitted attempts = run dirs with a launch record and no summary; malformed records raise."""
    root = os.path.join(W, "pilot-ledger")
    for name, res, summ in (("run-a", 123, False), ("run-b", 456, True), ("run-c", 7, False)):
        os.makedirs(os.path.join(root, name))
        with open(os.path.join(root, name, "launch-record.json"), "xb") as fh:
            fh.write(json.dumps({"retained_output_reservation_bytes": res}).encode())
        if summ:
            with open(os.path.join(root, name, "summary.json"), "xb") as fh:
                fh.write(b"{}")
    total, names = R.other_admitted_reservations(root)
    assert (total, names) == (130, ["run-a", "run-c"]), (total, names)
    os.makedirs(os.path.join(root, "run-d"))
    with open(os.path.join(root, "run-d", "launch-record.json"), "xb") as fh:
        fh.write(json.dumps({"retained_output_reservation_bytes": True}).encode())
    raised = False
    try:
        R.other_admitted_reservations(root)
    except RuntimeError:
        raised = True
    assert raised
    return {"others": total}


def good_fixture(R):
    S = sha(b"proof")
    sink = {"sink_settled": True, "connected": True, "eof": True, "over_cap": False, "error": None,
            "unblocked_by_runner": False, "discarded": 0, "received": 100, "retained": 100,
            "sha256_of_retained": S, "buffer_rehash": [S, 100], "thread_alive_after_join": False}
    solver = {"returncode": 20, "stop": "self", "settled": True, "capture_over_cap": False, "seq": 1,
              "proof_sink": sink}

    def chk(seq):
        rec = {"returncode": 0, "stop": "self", "settled": True, "capture_over_cap": False, "seq": seq,
               "nondropped_bytes": 500,
               "stdin_feed": {"mode": "plain", "started": True, "fed_bytes": 100, "fed_sha256": S,
                              "proof_bytes_fed": 100, "delivery_error": None, "exception": None, "close_error": None,
                              "thread_alive_after_join": False},
               "stdout_filter": {"raw_eof": True, "raw_bytes": 700, "dup_bytes_dropped": 200}}
        lines = [R.STDIN_LINE, "c parsing input formula with 10 variables and 20 clauses",
                 "c finished parsing, read 100 bytes from proof file", "s VERIFIED"]
        return [rec, lines]
    return {"cnf_expect": ("c" * 64, 1000, "p cnf 10 20"), "solver": solver, "kl": ["s UNSATISFIABLE"], "cap": 1000,
            "checks": [["A"] + chk(2), ["B"] + chk(3)], "cnf_post": ("c" * 64, 1000), "buf_post": [S, 100], "S": S}


def qualify(R, fx):
    return R.qualify_stream(fx["cnf_expect"], fx["solver"], fx["kl"], fx["cap"], [tuple(c) for c in fx["checks"]],
                            fx["cnf_post"], fx["buf_post"])


def _zero_proof(fx):
    """A coherent zero-byte proof: every buffer/feed/consumed field agrees, so only BUFFER_SIZE remains."""
    S0 = sha(b"")
    fx["solver"]["proof_sink"].update(retained=0, received=0, sha256_of_retained=S0, buffer_rehash=[S0, 0])
    for c in fx["checks"]:
        c[1]["stdin_feed"].update(fed_bytes=0, fed_sha256=S0, proof_bytes_fed=0)
        c[2][2] = "c finished parsing, read 0 bytes from proof file"
    fx["buf_post"] = [S0, 0]


def _suffix_shape(fx, k):
    """C3 shape for checker k: suffix mode, one extra byte fed and hashed, 'wrong binary prefix', read N == buffer."""
    rec, lines = fx["checks"][k][1], fx["checks"][k][2]
    rec["stdin_feed"].update(mode="suffix", fed_bytes=101, fed_sha256=sha(b"proof" + b"x"))
    lines.insert(2, "c WARNING: wrong binary prefix, stop reading proof")


def _foreign_shape(fx, k):
    """C4 shape for checker k: completed 's NOT VERIFIED' rc1."""
    fx["checks"][k][1]["returncode"] = 1
    fx["checks"][k][2][3] = "s NOT VERIFIED"


def mutations(R):
    S2 = sha(b"other")
    A = lambda fx: fx["checks"][0][1]          # noqa: E731
    B = lambda fx: fx["checks"][1][1]          # noqa: E731
    LA = lambda fx: fx["checks"][0][2]         # noqa: E731
    LB = lambda fx: fx["checks"][1][2]         # noqa: E731
    sink = lambda fx: fx["solver"]["proof_sink"]  # noqa: E731
    m = [
        ("solver rc 0", lambda fx: fx["solver"].update(returncode=0), ["SOLVER_EXIT"]),
        ("solver tripped", lambda fx: fx["solver"].update(stop="lane_rss"), ["SOLVER_EXIT"]),
        ("solver two status lines", lambda fx: fx["kl"].append("s UNSATISFIABLE"), ["SOLVER_OUTPUT"]),
        ("solver SAT line", lambda fx: fx["kl"].__setitem__(0, "s SATISFIABLE"), ["SOLVER_OUTPUT"]),
        ("solver extra diagnostic line", lambda fx: fx["kl"].append("kissat: warning: x"), ["SOLVER_OUTPUT"]),
        ("solver no output", lambda fx: fx["kl"].clear(), ["SOLVER_OUTPUT"]),
        ("solver unsettled", lambda fx: fx["solver"].update(settled=False), ["SOLVER_SETTLE"]),
        ("solver capture over cap", lambda fx: fx["solver"].update(capture_over_cap=True), ["SOLVER_SETTLE"]),
        ("buffer no EOF", lambda fx: sink(fx).update(eof=False), ["BUFFER_INCOMPLETE"]),
        ("buffer over cap", lambda fx: sink(fx).update(over_cap=True), ["BUFFER_INCOMPLETE"]),
        ("buffer I/O error", lambda fx: sink(fx).update(error="OSError()"), ["BUFFER_INCOMPLETE"]),
        ("buffer unblocked by runner", lambda fx: sink(fx).update(unblocked_by_runner=True), ["BUFFER_INCOMPLETE"]),
        ("buffer discarded bytes", lambda fx: sink(fx).update(discarded=1), ["BUFFER_INCOMPLETE"]),
        ("buffer received != retained", lambda fx: sink(fx).update(received=101), ["BUFFER_INCOMPLETE"]),
        ("buffer re-hash differs", lambda fx: sink(fx).update(buffer_rehash=[S2, 100]), ["BUFFER_INCOMPLETE"]),
        ("buffer not settled", lambda fx: sink(fx).update(sink_settled=False), ["BUFFER_INCOMPLETE"]),
        ("buffer never connected", lambda fx: sink(fx).update(connected=False), ["BUFFER_INCOMPLETE"]),
        ("coherent zero-byte proof", _zero_proof, ["BUFFER_SIZE"]),
        ("proof above cap", lambda fx: fx.update(cap=99), ["BUFFER_SIZE"]),
        ("checker B missing", lambda fx: fx.update(checks=fx["checks"][:1]), ["CHECKER_SET"]),
        ("checkers reversed", lambda fx: fx.update(checks=fx["checks"][::-1]), ["CHECKER_SET"]),
        ("checker A rc 1", lambda fx: A(fx).update(returncode=1), ["A.EXIT"]),
        ("checker B deadline trip", lambda fx: B(fx).update(stop="absolute_or_elapsed_deadline"), ["B.EXIT"]),
        ("checker A two VERIFIED", lambda fx: LA(fx).append("s VERIFIED"), ["A.STATUS"]),
        ("checker A VERIFIED + NOT VERIFIED", lambda fx: LA(fx).append("s NOT VERIFIED"),
         ["A.FORBIDDEN.NOT_VERIFIED", "A.STATUS"]),
        ("checker A TIMEOUT rc0", lambda fx: LA(fx).__setitem__(3, "s TIMEOUT"), ["A.FORBIDDEN.TIMEOUT", "A.STATUS"]),
        ("checker B header mismatch",
         lambda fx: LB(fx).__setitem__(1, "c parsing input formula with 11 variables and 20 clauses"), ["B.HEADER"]),
        ("checker B duplicate header", lambda fx: LB(fx).insert(2, LB(fx)[1]), ["B.HEADER"]),
        ("checker B conflicting extra header",
         lambda fx: LB(fx).insert(2, "c parsing input formula with 11 variables and 21 clauses"), ["B.HEADER"]),
        ("checker A no stdin record", lambda fx: LA(fx).remove(R.STDIN_LINE), ["A.STDIN"]),
        ("checker A duplicate stdin record", lambda fx: LA(fx).insert(1, R.STDIN_LINE), ["A.STDIN"]),
        ("checker A suffix mode only", lambda fx: A(fx)["stdin_feed"].update(mode="suffix"), ["A.FEED_MODE"]),
        ("checker A fed +1", lambda fx: A(fx)["stdin_feed"].update(fed_bytes=101), ["A.CONSUMED", "A.FEED_DIGEST"]),
        ("checker B fed SHA differs (alter in transit)", lambda fx: B(fx)["stdin_feed"].update(fed_sha256=S2),
         ["B.FEED_DIGEST"]),
        ("checker A truncated feed", lambda fx: A(fx)["stdin_feed"].update(fed_bytes=90, proof_bytes_fed=90),
         ["A.CONSUMED", "A.FEED_DIGEST"]),
        ("checker A delivery error", lambda fx: A(fx)["stdin_feed"].update(delivery_error="EPIPE after 50 fed bytes"),
         ["A.FEED_STATE"]),
        ("checker A feeder exception", lambda fx: A(fx)["stdin_feed"].update(exception="MemoryError()"),
         ["A.FEED_STATE"]),
        ("checker B feeder close error", lambda fx: B(fx)["stdin_feed"].update(close_error="OSError()"),
         ["B.FEED_STATE"]),
        ("checker A feeder unsettled", lambda fx: A(fx)["stdin_feed"].update(thread_alive_after_join=True),
         ["A.FEED_STATE"]),
        ("checker A feeder never started", lambda fx: A(fx)["stdin_feed"].update(started=False), ["A.FEED_STATE"]),
        ("checker A no feed record", lambda fx: A(fx).update(stdin_feed=None),
         ["A.CONSUMED", "A.FEED_DIGEST", "A.FEED_MODE", "A.FEED_STATE"]),
        ("checker B consumed 99", lambda fx: LB(fx).__setitem__(2, "c finished parsing, read 99 bytes from proof file"),
         ["B.CONSUMED"]),
        ("checker B no consumed record", lambda fx: LB(fx).pop(2), ["B.CONSUMED"]),
        ("checker B conflicting extra consumed record",
         lambda fx: LB(fx).insert(3, "c finished parsing, read 99 bytes from proof file"), ["B.CONSUMED"]),
        ("checker A filter no EOF", lambda fx: A(fx)["stdout_filter"].update(raw_eof=False), ["A.FILTER"]),
        ("checker A filter raw +1", lambda fx: A(fx)["stdout_filter"].update(raw_bytes=701), ["A.FILTER"]),
        ("checker B filter missing", lambda fx: B(fx).update(stdout_filter=None), ["B.FILTER"]),
        ("checker A nondropped bytes missing", lambda fx: A(fx).pop("nondropped_bytes"), ["A.FILTER"]),
        ("checker A unsettled", lambda fx: A(fx).update(settled=False), ["A.SETTLE"]),
        ("checker B capture over cap", lambda fx: B(fx).update(capture_over_cap=True), ["B.SETTLE"]),
        ("CNF post digest differs", lambda fx: fx.update(cnf_post=("d" * 64, 1000)), ["CNF_POST"]),
        ("CNF post bytes differ", lambda fx: fx.update(cnf_post=("c" * 64, 999)), ["CNF_POST"]),
        ("buffer post-check re-hash differs", lambda fx: fx.update(buf_post=[S2, 100]), ["BUFFER_POST"]),
        ("buffer post-check bytes differ", lambda fx: fx.update(buf_post=[fx["S"], 99]), ["BUFFER_POST"]),
        ("C3 shape on both checkers", lambda fx: (_suffix_shape(fx, 0), _suffix_shape(fx, 1)),
         ["A.CONSUMED", "A.FEED_DIGEST", "A.FEED_MODE", "A.FORBIDDEN.WRONG_PREFIX",
          "B.CONSUMED", "B.FEED_DIGEST", "B.FEED_MODE", "B.FORBIDDEN.WRONG_PREFIX"]),
        ("C4 shape on checker A", lambda fx: _foreign_shape(fx, 0), ["A.EXIT", "A.FORBIDDEN.NOT_VERIFIED", "A.STATUS"]),
    ]
    for pat, key, line in (("early EOF", "EARLY_EOF", "c WARNING: early EOF of the input formula"),
                           ("clauses less than expected", "LESS_THAN_EXPECTED", "c WARNING: 3 clauses less than expected"),
                           ("trivial UNSAT", "TRIVIAL_UNSAT", "c trivial UNSAT"),
                           ("ERROR", "ERROR", "c ERROR: no conflict"),
                           ("MEMOUT", "MEMOUT", "c MEMOUT: reallocation of DB failed"),
                           ("wrong binary prefix", "WRONG_PREFIX", "c WARNING: wrong binary prefix, stop reading proof"),
                           ("no empty clause detected", "NO_EMPTY_CLAUSE", "c WARNING: no empty clause detected"),
                           ("NOT VERIFIED", "NOT_VERIFIED", "c s NOT VERIFIED echo"),
                           ("TIMEOUT", "TIMEOUT", "c TIMEOUT echo"),
                           ("illegal literal", "ILLEGAL_LITERAL", "c illegal literal 5 due to max var 4"),
                           ("error opening", "ERROR_OPENING", 'c error opening "x".'),
                           ("failed to reallocate", "FAILED_REALLOC", "c failed to reallocate unit stack")):
        m.append(("checker A forbidden %r" % pat, (lambda ln: lambda fx: LA(fx).insert(1, ln))(line),
                  ["A.FORBIDDEN." + key]))
    return m


def t_qualify_matrix(R, W):
    """V10: complete sorted defect-ID list per scenario; the baseline must be exactly []."""
    base = good_fixture(R)
    got0 = qualify(R, copy.deepcopy(base))
    assert got0 == [], got0
    rows = []
    for name, mut, want in mutations(R):
        check()
        fx = copy.deepcopy(base)
        mut(fx)
        got = qualify(R, fx)
        rows.append({"mutation": name, "intended_ids": sorted(want), "got_ids": R.defect_ids(got),
                     "exact": R.defect_ids(got) == sorted(want), "defects": got})
    bad = [r for r in rows if not r["exact"]]
    assert not bad, bad
    return {"scenarios": len(rows), "all_complete_id_sets_exact": True}


TESTS = [t_buffer_roundtrip, t_buffer_cap, t_buffer_never_connected, t_buffer_fifo_replaced,
         t_feeder_plain, t_feeder_suffix, t_feeder_hold_epipe, t_feeder_midstream_close, t_feeder_guards,
         t_feeder_holder_charge, t_filter, t_filter_long_line, t_filter_continuation_adversarial,
         t_filter_continuation_genuine_line, t_capture_accounting, t_libproc_self, t_tree_census_and_usage,
         t_tree_census_fail_closed, t_out_dir_ancestry, t_monitor_provenance_header, t_item_shapes,
         t_helper_refusals_and_clock, t_output_guard, t_other_admitted_reservations, t_qualify_matrix]


def main():
    if len(sys.argv) != 4:
        print("usage: test_pilot_stream_v3.py RUNNER.py RUNNER_SHA256 OUT_DIR", flush=True)
        return 70
    runner, runner_sha, out = os.path.abspath(sys.argv[1]), sys.argv[2], os.path.abspath(sys.argv[3])
    if os.path.dirname(out) != LANE + "/evidence/probes" or os.path.lexists(out):
        print("REFUSED: OUT_DIR must be a new directory directly under LANE/evidence/probes", flush=True)
        return 70
    with open(runner, "rb") as fh:
        got = sha(fh.read())
    if got != runner_sha:
        print("REFUSED: runner pin mismatch %s" % got, flush=True)
        return 70
    STATE["t0"] = time.monotonic()
    STATE["deadline"] = STATE["t0"] + BUDGET_S          # B1: cooperative budget; no SIGALRM
    signal.signal(signal.SIGTERM, on_signal)            # B2: stamp only; settle and report
    signal.signal(signal.SIGINT, on_signal)
    os.mkdir(out)
    with open(os.path.abspath(__file__), "rb") as fh:
        self_sha = sha(fh.read())
    write_x(os.path.join(out, "receipt.json"), {"pid": os.getpid(), "ppid": os.getppid(), "argv": sys.argv,
                                                "start": None, "start_note": "host clock is read after the runner "
                                                "import through its owned bounded /bin/date helper (result.json)",
                                                "runner": [runner, runner_sha],
                                                "test_source_sha256": self_sha, "budget_s": BUDGET_S,
                                                "budget_mode": "cooperative monotonic deadline; no SIGALRM/kill/ulimit",
                                                "result_reserve_s": RESULT_RESERVE_S,
                                                "signals_handled": ["SIGTERM", "SIGINT"]})
    results, in_flight, not_started, terminal, setup_error, R = [], None, [], None, None, None
    start_clock = None
    work = os.path.join(out, "work")
    try:
        check()
        os.mkdir(work)
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("pstream_runner_under_test", runner)
        R = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(R)
        start_clock = host_clock(R)
    except BudgetExhausted as exc:
        terminal, setup_error = "BUDGET_EXHAUSTED", repr(exc)
    except Cancelled as exc:
        terminal, setup_error = "CANCELLED", repr(exc)
    except BaseException as exc:
        terminal, setup_error = "SETUP_FAILED", repr(exc)[:4000]
    if terminal is not None:
        not_started = [t.__name__ for t in TESTS]
    else:
        for k, t in enumerate(TESTS):
            try:
                check()
            except (BudgetExhausted, Cancelled) as exc:
                terminal = "CANCELLED" if isinstance(exc, Cancelled) else "BUDGET_EXHAUSTED"
                not_started = [x.__name__ for x in TESTS[k:]]
                in_flight = {"test": None, "stopped_before_start_of": t.__name__, "reason": repr(exc)}
                break
            started = time.monotonic()
            try:
                detail = t(R, work)
                results.append({"test": t.__name__, "ok": True, "detail": detail,
                                "seconds": round(time.monotonic() - started, 3)})
            except (BudgetExhausted, Cancelled) as exc:
                terminal = "CANCELLED" if isinstance(exc, Cancelled) else "BUDGET_EXHAUSTED"
                not_started = [x.__name__ for x in TESTS[k + 1:]]
                in_flight = {"test": t.__name__, "reason": repr(exc), "seconds": round(time.monotonic() - started, 3),
                             "traceback": traceback.format_exc()[-4000:]}
                break
            except BaseException as exc:
                results.append({"test": t.__name__, "ok": False, "error": repr(exc)[:4000],
                                "traceback": traceback.format_exc()[-4000:],
                                "seconds": round(time.monotonic() - started, 3)})
        if terminal is None:
            terminal = "ALL_OK" if all(r["ok"] for r in results) and len(results) == len(TESTS) else "FAILURES"
    alive = sorted(th.name for th in threading.enumerate() if th is not threading.main_thread() and th.is_alive())
    final = {"start_host_clock": start_clock, "end_host_clock": host_clock(R), "terminal": terminal,
             "all_ok": terminal == "ALL_OK", "results": results,
             "in_flight": in_flight, "not_started": not_started, "setup_error": setup_error,
             "threads_alive_at_result": alive, "elapsed_s": round(time.monotonic() - STATE["t0"], 3),
             "budget_s": BUDGET_S, "signal": STATE["signal"],
             "runner_latch_after_tests": None if R is None else list(R.LATCH),
             "runner_helper_log": None if R is None else R.HELPER_LOG,
             "preservation_scope": "only test-created entries under OUT_DIR/work were created; one test-created "
                                   "FIFO was moved (never deleted) and one test-created directory was chmod 000 "
                                   "then 0755",
             "runner": [runner, runner_sha], "test_source_sha256": self_sha}
    try:
        write_x(os.path.join(out, "result.json"), final)
    except BaseException as exc:
        print("RESULT WRITE FAILED %r" % (exc,), flush=True)
        return 71
    print("RESULT", os.path.join(out, "result.json"), "terminal", terminal, flush=True)
    return {"ALL_OK": 0, "FAILURES": 1, "SETUP_FAILED": 1, "BUDGET_EXHAUSTED": 2, "CANCELLED": 3}[terminal]


if __name__ == "__main__":
    sys.exit(main())
