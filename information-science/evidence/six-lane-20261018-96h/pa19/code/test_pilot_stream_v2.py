#!/usr/bin/env python3
"""P-STREAM v1 offline mutation tests, test v2 = code/test_pilot_stream_v1.py (53e5fe57..., preserved, never run)
with the parent-requested cooperative-budget correction (parent IRC 2026-10-19 05:3x).  No native binary, no network,
stdlib only.
  B1 No SIGALRM, no kill, no ulimit and no reliance on a tool deadline.  The budget is a monotonic deadline (BUDGET_S
     from the start) checked before every test, between mutation rows and inside every wait.  Every helper thread is
     a daemon thread; every FIFO/pipe read and pipe write runs in such a thread, joined in SLICE_S slices bounded by
     the remaining budget less RESULT_RESERVE_S.  A runner call with its own internal bound (ProofBuffer.finish with
     a live collector: <= SINK_UNBLOCK + STREAM_JOIN) is entered only if the budget can absorb that bound;
     Feeder.finish is given a join timeout of min(10 s, remaining budget less the reserve).
  B2 Once OUT_DIR exists a terminal OUT_DIR/result.json is always written (exclusive): ALL_OK, FAILURES,
     BUDGET_EXHAUSTED, CANCELLED (SIGTERM/SIGINT: the handler only stamps a scalar; no new test starts, the
     in-flight one stops at its next check, and the result is written) or SETUP_FAILED.  It lists finished,
     in-flight and not-started tests and the threads still alive; the receipt with the PID is written before any
     work, as in v1.
  B3 t_constants (implementation/default pinning) is omitted from the executed suite; chunk-fit behaviour is to be
     proven by a separate prestart-refusal scenario.  Every other test is unchanged in intent.

NOT TO BE RUN without a parent WINDOW or parent supervision (small-probe rules: frozen source; receipt with PID
written before any work; <= 300 s; one process; outputs only under LANE/evidence/probes/).

usage: test_pilot_stream_v2.py RUNNER.py RUNNER_SHA256 OUT_DIR
  RUNNER: code/pilot_stream_drat_ms06_v1.py or code/pilot_stream_drat_ms09_v1.py (identical transport code).
  OUT_DIR must not exist; its parent must be LANE/evidence/probes.  Writes OUT_DIR/receipt.json first and
  OUT_DIR/result.json last (both exclusive); FIFOs, pipes and capture files only inside OUT_DIR/work.
Transport tests drive the runner's ProofBuffer, Feeder and capture filter with real FIFOs/pipes in-process.
The qualification matrix applies ONE single-field mutation at a time to a passing synthetic fixture and asserts
that qualify_stream rejects it for the intended reason (every S4 protection is load-bearing).
Exit 0 ALL_OK; 1 FAILURES or SETUP_FAILED; 2 BUDGET_EXHAUSTED; 3 CANCELLED; 70 refused start (no OUT_DIR);
71 result.json could not be written.
"""
import copy
import hashlib
import importlib.util
import json
import os
import signal
import subprocess
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


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


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
    return {"latched": latched}


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
    c.captured, c.over_cap, c.reader_error, c.filt = 0, False, None, R.new_filter()
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
    assert kept == want and c.captured == len(want)
    assert (f["dup_low"], f["dup_high"]) == (2, 1) and f["dup_bytes"] == sum(len(lines[i]) for i in dropped)
    assert f["header_clauses"] == 20 and f["tail"] == len(lines[-1])
    assert f["raw_bytes"] == c.captured + f["dup_bytes"]
    return {"kept_bytes": c.captured, "dup_bytes": f["dup_bytes"]}


def t_filter_long_line(R, W):
    raw = b"B" * (3 * 65536 + 5) + b"\rc WARNING: detected and deleted duplicate literal 4 at position 2 of proof line 9\n"
    c, kept = run_filter(R, W, "filter-long.out", raw, 65536)
    f = c.filt
    assert c.reader_error is None and kept == raw and f["dup_bytes"] == 0 and f["raw_bytes"] == c.captured
    return {"kept_bytes": c.captured}


def good_fixture(R):
    S = sha(b"proof")
    sink = {"sink_settled": True, "connected": True, "eof": True, "over_cap": False, "error": None,
            "unblocked_by_runner": False, "discarded": 0, "received": 100, "retained": 100,
            "sha256_of_retained": S, "buffer_rehash": [S, 100], "thread_alive_after_join": False}
    solver = {"returncode": 20, "stop": "self", "settled": True, "capture_over_cap": False, "seq": 1,
              "proof_sink": sink}

    def chk(seq):
        rec = {"returncode": 0, "stop": "self", "settled": True, "capture_over_cap": False, "seq": seq,
               "captured_bytes": 500,
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


def mutations(R):
    S2 = sha(b"other")
    A = lambda fx: fx["checks"][0][1]          # noqa: E731
    B = lambda fx: fx["checks"][1][1]          # noqa: E731
    LA = lambda fx: fx["checks"][0][2]         # noqa: E731
    LB = lambda fx: fx["checks"][1][2]         # noqa: E731
    sink = lambda fx: fx["solver"]["proof_sink"]  # noqa: E731
    m = [
        ("solver rc 0", lambda fx: fx["solver"].update(returncode=0), "solver not self-exit rc20"),
        ("solver tripped", lambda fx: fx["solver"].update(stop="lane_rss"), "solver not self-exit rc20"),
        ("solver two status lines", lambda fx: fx["kl"].append("s UNSATISFIABLE"), "solver status lines not exactly"),
        ("solver SAT line", lambda fx: fx["kl"].__setitem__(0, "s SATISFIABLE"), "solver status lines not exactly"),
        ("solver unsettled", lambda fx: fx["solver"].update(settled=False), "settlement/capture defect seq 1"),
        ("solver capture over cap", lambda fx: fx["solver"].update(capture_over_cap=True),
         "settlement/capture defect seq 1"),
        ("buffer no EOF", lambda fx: sink(fx).update(eof=False), "proof buffer incomplete"),
        ("buffer over cap", lambda fx: sink(fx).update(over_cap=True), "proof buffer incomplete"),
        ("buffer I/O error", lambda fx: sink(fx).update(error="OSError()"), "proof buffer incomplete"),
        ("buffer unblocked by runner", lambda fx: sink(fx).update(unblocked_by_runner=True), "proof buffer incomplete"),
        ("buffer discarded bytes", lambda fx: sink(fx).update(discarded=1), "proof buffer incomplete"),
        ("buffer received != retained", lambda fx: sink(fx).update(received=101), "proof buffer incomplete"),
        ("buffer re-hash differs", lambda fx: sink(fx).update(buffer_rehash=[S2, 100]), "proof buffer incomplete"),
        ("buffer not settled", lambda fx: sink(fx).update(sink_settled=False), "proof buffer incomplete"),
        ("buffer never connected", lambda fx: sink(fx).update(connected=False), "proof buffer incomplete"),
        ("buffer empty", lambda fx: sink(fx).update(retained=0, received=0, buffer_rehash=[sha(b""), 0]),
         "proof size outside (0, cap]"),
        ("buffer above cap", lambda fx: fx.update(cap=99), "proof size outside (0, cap]"),
        ("checker B missing", lambda fx: fx.update(checks=fx["checks"][:1]), "not every pinned checker ran, in order"),
        ("checkers reversed", lambda fx: fx.update(checks=fx["checks"][::-1]), "not every pinned checker ran, in order"),
        ("checker A rc 1", lambda fx: A(fx).update(returncode=1), "checker A: checker not self-exit rc0"),
        ("checker B deadline trip", lambda fx: B(fx).update(stop="absolute_or_wall_deadline"),
         "checker B: checker not self-exit rc0"),
        ("checker A two VERIFIED", lambda fx: LA(fx).append("s VERIFIED"), "checker A: checker status lines not exactly"),
        ("checker A TIMEOUT rc0", lambda fx: LA(fx).__setitem__(3, "s TIMEOUT"), "checker A: checker output contains 'TIMEOUT'"),
        ("checker B header mismatch",
         lambda fx: LB(fx).__setitem__(1, "c parsing input formula with 11 variables and 20 clauses"),
         "checker B: checker parse header line missing/mismatched"),
        ("checker A no stdin line", lambda fx: LA(fx).remove(R.STDIN_LINE),
         "checker A: checker did not report reading the proof from stdin"),
        ("checker A suffix mode", lambda fx: A(fx)["stdin_feed"].update(mode="suffix"), "checker A: feed mode is not plain"),
        ("checker A fed +1", lambda fx: A(fx)["stdin_feed"].update(fed_bytes=101),
         "checker A: fed bytes/SHA-256 != collected proof buffer"),
        ("checker B fed SHA differs (alter in transit)", lambda fx: B(fx)["stdin_feed"].update(fed_sha256=S2),
         "checker B: fed bytes/SHA-256 != collected proof buffer"),
        ("checker A truncated feed", lambda fx: A(fx)["stdin_feed"].update(fed_bytes=90, proof_bytes_fed=90),
         "checker A: fed bytes/SHA-256 != collected proof buffer"),
        ("checker A delivery error", lambda fx: A(fx)["stdin_feed"].update(delivery_error="EPIPE after 50 fed bytes"),
         "checker A: stdin feed incomplete, failed or unsettled"),
        ("checker A feeder exception", lambda fx: A(fx)["stdin_feed"].update(exception="MemoryError()"),
         "checker A: stdin feed incomplete, failed or unsettled"),
        ("checker B feeder close error", lambda fx: B(fx)["stdin_feed"].update(close_error="OSError()"),
         "checker B: stdin feed incomplete, failed or unsettled"),
        ("checker A feeder unsettled", lambda fx: A(fx)["stdin_feed"].update(thread_alive_after_join=True),
         "checker A: stdin feed incomplete, failed or unsettled"),
        ("checker A feeder never started", lambda fx: A(fx)["stdin_feed"].update(started=False),
         "checker A: stdin feed incomplete, failed or unsettled"),
        ("checker A no feed record", lambda fx: A(fx).update(stdin_feed=None),
         "checker A: stdin feed incomplete, failed or unsettled"),
        ("checker B consumed 99", lambda fx: LB(fx).__setitem__(2, "c finished parsing, read 99 bytes from proof file"),
         "checker B: checker-consumed proof bytes != fed bytes"),
        ("checker B no finished line", lambda fx: LB(fx).pop(2), "checker B: checker-consumed proof bytes != fed bytes"),
        ("checker A filter no EOF", lambda fx: A(fx)["stdout_filter"].update(raw_eof=False),
         "checker A: checker output filter accounting mismatch"),
        ("checker A filter raw +1", lambda fx: A(fx)["stdout_filter"].update(raw_bytes=701),
         "checker A: checker output filter accounting mismatch"),
        ("checker B filter missing", lambda fx: B(fx).update(stdout_filter=None),
         "checker B: checker output filter accounting mismatch"),
        ("checker A unsettled", lambda fx: A(fx).update(settled=False), "checker A: settlement/capture defect seq 2"),
        ("checker B capture over cap", lambda fx: B(fx).update(capture_over_cap=True),
         "checker B: settlement/capture defect seq 3"),
        ("CNF post digest differs", lambda fx: fx.update(cnf_post=("d" * 64, 1000)), "CNF file digest/bytes != expected"),
        ("CNF post bytes differ", lambda fx: fx.update(cnf_post=("c" * 64, 999)), "CNF file digest/bytes != expected"),
        ("buffer post-check re-hash differs", lambda fx: fx.update(buf_post=[S2, 100]),
         "proof buffer re-hash after the checks != collector measurement"),
        ("buffer post-check bytes differ", lambda fx: fx.update(buf_post=[fx["S"], 99]),
         "proof buffer re-hash after the checks != collector measurement"),
    ]
    for pat, line in (("early EOF", "c WARNING: early EOF of the input formula"),
                      ("clauses less than expected", "c WARNING: 3 clauses less than expected"),
                      ("trivial UNSAT", "c trivial UNSAT"), ("ERROR", "c ERROR: no conflict"),
                      ("MEMOUT", "c MEMOUT: reallocation of DB failed"),
                      ("wrong binary prefix", "c WARNING: wrong binary prefix, stop reading proof"),
                      ("no empty clause detected", "c WARNING: no empty clause detected"),
                      ("NOT VERIFIED", "c s NOT VERIFIED echo"), ("TIMEOUT", "c TIMEOUT echo"),
                      ("illegal literal", "c illegal literal 5 due to max var 4"),
                      ("error opening", 'c error opening "x".'),
                      ("failed to reallocate", "c failed to reallocate unit stack")):
        m.append(("checker A forbidden %r" % pat, (lambda ln: lambda fx: LA(fx).insert(1, ln))(line),
                  "checker A: checker output contains %r" % pat))
    return m


def t_qualify_matrix(R, W):
    base = good_fixture(R)
    assert qualify(R, copy.deepcopy(base)) == [], qualify(R, copy.deepcopy(base))
    rows = []
    for name, mut, want in mutations(R):
        check()
        fx = copy.deepcopy(base)
        mut(fx)
        got = qualify(R, fx)
        rows.append({"mutation": name, "intended": want, "rejected": bool(got), "intended_reason_present": want in got,
                     "defects": got})
    bad = [r for r in rows if not (r["rejected"] and r["intended_reason_present"])]
    assert not bad, bad
    return {"mutations": len(rows), "all_rejected_for_intended_reason": True}


TESTS = [t_buffer_roundtrip, t_buffer_cap, t_buffer_never_connected, t_buffer_fifo_replaced,
         t_feeder_plain, t_feeder_suffix, t_feeder_hold_epipe, t_feeder_midstream_close, t_feeder_guards,
         t_filter, t_filter_long_line, t_qualify_matrix]  # B3: t_constants omitted (implementation pinning)


def main():
    if len(sys.argv) != 4:
        print("usage: test_pilot_stream_v2.py RUNNER.py RUNNER_SHA256 OUT_DIR", flush=True)
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
                                                "start": clock(), "runner": [runner, runner_sha],
                                                "test_source_sha256": self_sha, "budget_s": BUDGET_S,
                                                "budget_mode": "cooperative monotonic deadline; no SIGALRM/kill/ulimit",
                                                "result_reserve_s": RESULT_RESERVE_S,
                                                "signals_handled": ["SIGTERM", "SIGINT"]})
    results, in_flight, not_started, terminal, setup_error, R = [], None, [], None, None, None
    work = os.path.join(out, "work")
    try:
        check()
        os.mkdir(work)
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("pstream_runner_under_test", runner)
        R = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(R)
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
    final = {"end": clock(), "terminal": terminal, "all_ok": terminal == "ALL_OK", "results": results,
             "in_flight": in_flight, "not_started": not_started, "setup_error": setup_error,
             "threads_alive_at_result": alive, "elapsed_s": round(time.monotonic() - STATE["t0"], 3),
             "budget_s": BUDGET_S, "signal": STATE["signal"],
             "runner_latch_after_tests": None if R is None else list(R.LATCH),
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
