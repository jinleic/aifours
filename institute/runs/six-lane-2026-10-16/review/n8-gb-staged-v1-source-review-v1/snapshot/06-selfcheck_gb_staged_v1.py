#!/usr/bin/env python3
"""Pure-Python pre-review checks for scripts/gb_staged_v1.py (no native solver/checker, no n=8 generation).

The runtime is executed from the exact bytes hashed here into a fresh module object. kissat and drat-trim are never
started: pipeline tests replace them with python -I -B -c stubs through a subprocess shim keyed on the pinned
binary paths; ps/lsof lane helpers are replaced by fakes (the run_helper ownership checks use python sleepers). The
only GB encode run is the binder's own n=5 storage control (tiny). Everything is written under the new directory
selfcheck-gbs1-v1[-TAG]/ (logs, FIFOs, empty TMPDIRs, stub receipts in a sandbox desk) and the result file
SELFCHECK-gbs1-v1[-TAG].json, both created exclusively.
Usage: /opt/homebrew/opt/python@3.14/bin/python3.14 -I -B scripts/selfcheck_gb_staged_v1.py [TAG]
"""
import copy
import hashlib
import importlib.util
import json
import os
import random
import subprocess
import sys
import threading
import time
import traceback

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1"
TAG = ("-" + sys.argv[1]) if len(sys.argv) > 1 else ""
TARGET = DESK + "/scripts/gb_staged_v1.py"
OUT = DESK + "/SELFCHECK-gbs1-v1%s.json" % TAG
WORK = DESK + "/selfcheck-gbs1-v1%s" % TAG
V5D = DESK + "/../moqls8-strengthened-parent-replay-v1/scripts/replay_v5d.py"

RT_BYTES = open(TARGET, "rb").read()
RT_SHA = hashlib.sha256(RT_BYTES).hexdigest()
_spec = importlib.util.spec_from_loader("gb_staged_v1_under_selfcheck", loader=None, origin=TARGET)
m = importlib.util.module_from_spec(_spec)
m.__file__ = TARGET
exec(compile(RT_BYTES, TARGET, "exec", dont_inherit=True), m.__dict__)

RESULTS = []


def check(name, ok, **detail):
    RESULTS.append(dict({"check": name, "ok": bool(ok)}, **detail))
    print("%-4s %s %s" % ("ok" if ok else "FAIL", name, json.dumps(detail, default=str)[:240]), flush=True)


def run(name, fn):
    try:
        fn()
    except BaseException as e:  # a crashing check is a failed check
        check(name + " (crashed)", False, error="%s: %s" % (type(e).__name__, e), tb=traceback.format_exc()[-3000:])


def sha(b):
    return hashlib.sha256(b).hexdigest()


def open_fds():
    return set(int(x) for x in os.listdir("/dev/fd"))


# --- A: pins, binding, the binder's loader/sink and the composition
CTX = {}


def t_pins():
    pins = m.verify_pins()
    check("A1 every pinned provenance/binding/source file hashes to its pin", len(pins) == len(m.PROVENANCE) + 3,
          pins=sorted(pins))
    b = m.check_binaries()
    check("A2 pinned kissat 4.0.4 and parent drat-trim hash to their pins (hashed only, never executed here)",
          b["kissat"]["sha256"] == m.KISSAT_SHA and b["drat-trim"]["sha256"] == m.DRAT_SHA)
    binding = m.load_binding()
    CTX["binding"] = binding
    recs = binding["records"]
    check("A3 GBBINDING d917203d: PASS, the 18 ids with kind/source/square, 12 direct + 6 strengthened",
          binding["sha256"] == m.GBBINDING_SHA and all(g in recs for g in m.GB_ITEMS) and len(m.GB_ITEMS) == 18
          and sum(recs[g]["kind"] == "template" for g in m.GB_ITEMS) == 12
          and sum(recs[g]["kind"] == "strengthened" for g in m.GB_ITEMS) == 6
          and set(m.GB_ITEMS) == set(recs) - {"P1-B1", "P1-B2", "P1-B3", "P1-B5"})


def t_binder():
    B = m.load_binder()
    CTX["B"] = B
    ctx = B.check_inputs()
    CTX["ctx"] = ctx
    gbrow = [r for r in ctx["rows"] if r["path"] == m.GB_SOURCE]
    check("A4 binder bind_gb_v2 (188c88de) executed from verified bytes; its check_inputs() passes: pins, exact GB "
          "lines, AST facts, flags -> encode(8,[1,2,3,4,5],0,[1],True,None,True,False,False)",
          all(r["ok"] for r in ctx["rows"]) and len(gbrow) == 1 and gbrow[0]["sha256"] == m.GB_SOURCE_SHA
          and json.dumps(ctx["args"]) == json.dumps([8, [1, 2, 3, 4, 5], 0, [1], True, None, True, False, False])
          and "bind_gb_v2_pinned_for_gbs1" not in sys.modules, args=ctx["args"])
    st = B.storage_control(ctx["src"])
    ref = json.load(open(m.GBBINDING))["storage_replacement"]["storage_control_n5"]["reference_sha256"]
    check("A5 binder's n=5 storage control (tiny encode; no n=8 generation) passes here and reproduces the "
          "GBBINDING-recorded reference bytes", st["pass"] is True and st["reference_sha256"] == ref,
          reference=st["reference_sha256"], clauses=st["reference_clauses"])
    tab, V, C, segs = B.synthetic()
    out = B.compose(tab, V, C, segs, ctx["sup"], ctx["wman"], ctx["ga_binding"], ctx["ga_leaf"])
    recs = {f["id"]: f for f in out["formulas"]}
    bad = []
    for gid in m.GB_ITEMS:
        parts, pieces, t, s = m.compose_parts(B, gid, tab, V, C, segs, ctx["sup"])
        h, n = m.sha_parts(parts)
        r = recs[gid]
        if not (h == r["sha256"] and n == r["bytes"] and parts[0].decode() == r["header"]
                and pieces["units_sha256"] == r["pieces"]["units_sha256"]
                and pieces.get("tail_sha256") == r["pieces"].get("tail_sha256") and parts[1:1 + len(segs)] == segs
                and all(a is b for a, b in zip(parts[1:1 + len(segs)], segs))):
            bad.append(gid)
    check("A6 compose_parts == the binder's own compose() for all 18 ids on its synthetic name table (sha256, bytes, "
          "header, units, tail; base segments referenced, not copied)", not bad and not out["failures"], bad=bad)
    CTX["syn"] = (tab, V, C, segs, recs)
    for gid in ("P1-B4", "P1-B5.M3"):
        syn_binding = {"records": recs, "gb_base": {"vars": V, "clauses": C, "body_bytes": sum(map(len, segs)),
                                                     "body_sha256": m.sha_parts(segs)[0],
                                                     "body_segments": len(segs)}}
        it = m.gb_item(gid, "a1", syn_binding)
        parts, pieces, t, s = m.compose_parts(B, gid, tab, V, C, segs, ctx["sup"])
        ok = m.bound_identity(parts, segs, pieces, V, C, ctx["sup"][t], it, syn_binding)
        flipped = list(parts)
        ui = 1 + len(segs)
        flipped[ui] = (b"-" + flipped[ui]) if not flipped[ui].startswith(b"-") else flipped[ui][1:]
        bad1 = m.bound_identity(flipped, segs, pieces, V, C, ctx["sup"][t], it, syn_binding)
        it2 = copy.deepcopy(it)
        it2["bound"]["sha256"] = "0" * 64
        bad2 = m.bound_identity(parts, segs, pieces, V, C, ctx["sup"][t], it2, syn_binding)
        bad3 = m.bound_identity(parts, segs[:-1], pieces, V, C, ctx["sup"][t], it, syn_binding)
        check("A7 %s bound_identity: regenerated == bound record passes; a unit sign flip, a tampered PRE-EXEC "
              "copy and a changed base each refuse" % gid, ok["ok"] and not bad1["ok"] and not bad2["ok"]
              and not bad3["ok"], problems=[bad1["problems"][:1], bad2["problems"][:1], bad3["problems"][:1]])


# --- B: items, the parent GO record, the control admission prerequisite
def t_items():
    binding = CTX["binding"]
    ctl = [m.control_item(n) for n in m.CONTROLS]
    check("B1a the seven controls validate as one control PRE-EXEC", m.validate_items(ctl, binding) == []
          and len(ctl) == 7)
    ok18 = all(m.validate_items([m.gb_item(g, "a1", binding)], binding) == [] for g in m.GB_ITEMS)
    rt = all(m.validate_items([json.loads(json.dumps(m.gb_item(g, "a3", binding)))], binding) == [] for g in m.GB_ITEMS)
    check("B1b each of the 18 gb items validates alone (also after a JSON round trip)", ok18 and rt)
    refused = []
    for gid in ("P1-B1", "P1-B2", "P1-B3", "P1-B5", "P1-B5.M4", "P1-B4.M2", "P0-B7", ""):
        try:
            m.gb_item(gid, "a1", binding)
        except ValueError:
            refused.append(gid)
    for att in ("", "a0", "b1", "a1x", None, "a1000"):
        try:
            m.gb_item("P1-B4", att, binding)
        except ValueError:
            refused.append(repr(att))
    check("B1c the four normal-form templates, unknown ids and malformed attempt tags are refused",
          len(refused) == 14, refused=refused)
    g1, g2 = m.gb_item("P1-B4", "a1", binding), m.gb_item("P0-B4", "a1", binding)
    t = copy.deepcopy(g1)
    t["expected_checker_feed_bytes"] -= 1
    t2 = copy.deepcopy(g1)
    t2["bound"]["pieces"]["units_sha256"] = "f" * 64
    t3 = copy.deepcopy(ctl[0])
    t3["preregistered_verdict"] = "AS_PREREGISTERED_FAIL_CLOSED"
    probs = [m.validate_items(x, binding) for x in ([g1, g2], ctl[:1] + [g1], [t], [t2], [t3], ctl[:2] + ctl[:1],
                                                   [], [{"kind": "x"}])]
    check("B1d refused: two gb items, mixed kinds, tampered feed/bound/verdict fields, duplicate labels, empty, "
          "unknown kind", all(probs), problems=[p[:1] for p in probs])


def t_go():
    root = WORK + "/go"
    os.mkdir(root)
    os.mkdir(root + "/desk")
    saved = (m.REVIEW, m.DESK)
    m.REVIEW, m.DESK = root, root + "/desk"
    try:
        items = [m.control_item(n) for n in m.CONTROLS]
        want = {"status": "PARENT_GO", "desk": m.DESK_REL, "script_sha256": "a" * 64, "pre_exec_sha256": "b" * 64,
                "scope": "controls", "items": [it["item"] for it in items]}

        def put(name, obj, where=root):
            p = os.path.join(where, name)
            with open(p, "x") as f:
                f.write(obj if isinstance(obj, str) else json.dumps(obj))
            return p
        rec, probs = m.validate_go(put("go-ok.json", want), "b" * 64, "a" * 64, items)
        good = rec is not None and not probs and rec["sha256"] == sha(open(root + "/go-ok.json", "rb").read())
        bad = []
        for k, v in (("status", "GO"), ("desk", "review/x"), ("script_sha256", "c" * 64), ("pre_exec_sha256", "c" * 64),
                     ("scope", "science"), ("items", want["items"][:-1])):
            w = dict(want)
            w[k] = v
            bad.append(bool(m.validate_go(put("go-bad-%s.json" % k, w), "b" * 64, "a" * 64, items)[1]))
        bad.append(bool(m.validate_go(put("go-in-desk.json", want, root + "/desk"), "b" * 64, "a" * 64, items)[1]))
        bad.append(bool(m.validate_go(put("go-notjson.json", "{"), "b" * 64, "a" * 64, items)[1]))
        bad.append(bool(m.validate_go(root + "/absent.json", "b" * 64, "a" * 64, items)[1]))
        gbit = [m.gb_item("P1-B4", "a1", CTX["binding"])]
        bad.append(bool(m.validate_go(root + "/go-ok.json", "b" * 64, "a" * 64, gbit)[1]))  # controls GO, gb items
        check("B2 parent GO record: the exact record passes; each wrong field, a record inside the desk, non-JSON, a "
              "missing file and a controls GO for a gb PRE-EXEC are refused", good and all(bad), refusals=bad)
    finally:
        m.REVIEW, m.DESK = saved


def t_admission():
    root = WORK + "/admission"
    os.mkdir(root)
    os.mkdir(root + "/receipts")
    saved = m.DESK
    m.DESK = root
    try:
        out, probs = m.validate_controls("d" * 64)
        check("B3a gb admission: no control receipt -> seven problems, nothing admitted", out == [] and len(probs) == 7,
              first=probs[:1])
    finally:
        m.DESK = saved


# --- C: worker threads on plain pipes
def run_filter(stream, header_clauses, chunk=7):
    r, w = os.pipe()
    fds = m.Fds()
    fds.put("cor", r)
    lr, lw = os.pipe()
    fds.put("dlog", lw)
    res, kept = {}, []
    t = threading.Thread(target=m._filter, args=(fds, res, header_clauses), daemon=True)
    t.start()

    def drain():
        while True:
            b = os.read(lr, 65536)
            if not b:
                break
            kept.append(b)
    dt = threading.Thread(target=drain, daemon=True)
    dt.start()
    for i in range(0, len(stream), chunk):
        os.write(w, stream[i:i + chunk])
    os.close(w)
    t.join(10)
    dt.join(10)
    os.close(lr)
    return res, b"".join(kept), fds.names()


def dup(lit, pos, line):
    return (b"\rc WARNING: detected and deleted duplicate literal %d at position %d of proof line %d\n"
            % (lit, pos, line))


def t_filter():
    near = [b"\rc WARNING: detected and deleted duplicate literal 1 at position 1 of proof line 9 s VERIFIED\n",
            b"c WARNING: detected and deleted duplicate literal 1 at position 1 of proof line 9\n",
            b"\rc WARNING: detected and deleted duplicate literal 0 at position 1 of proof line 9\n",
            b"\rc WARNING: detected and deleted duplicate literal 1 at position 1 of proof line 9\r\n",
            b"\rc WARNING: early EOF of the input formula\n"]
    body = (b"\rc reading proof from stdin\n\rc parsing input formula with 3 variables and 9 clauses\n"
            + dup(1, 1, 9) + dup(-5, 2, 3) + b"".join(near) + dup(7, 1, 12)
            + b"\rc finished parsing, read 39 bytes from proof file\n\rs VERIFIED\n\rc verification time: 0.01\n"
            + b"unterminated-tail")
    res, kept, left = run_filter(body, 9)
    expect = body.replace(dup(1, 1, 9), b"", 1).replace(dup(-5, 2, 3), b"", 1).replace(dup(7, 1, 12), b"", 1)
    check("C1 stream filter: drops only the 3 exact duplicate-literal lines (formula phase 2, proof phase 1); keeps "
          "5 near-miss lines; raw sha/bytes/LF of the full stream; kept == stream minus exact lines; markers parsed",
          res["ok"] and res["dup_lines"] == 3 and res["dup_formula_phase"] == 2 and res["dup_proof_phase"] == 1
          and kept == expect and res["kept_sha256"] == sha(expect) and res["raw_sha256"] == sha(body)
          and res["raw_bytes"] == len(body) and res["raw_lf"] == body.count(b"\n")
          and res["status_lines"] == ["s VERIFIED"] and res["header_counts"] == [[3, 9]]
          and res["proof_bytes_parsed"] == [39] and res["early_eof_lines"] == 1 and res["unterminated_tail_bytes"] == 17
          and left == [], counts={k: res[k] for k in ("dup_lines", "kept_lines", "status_line_count",
                                                       "warning_line_count")})
    big = b"".join(dup(-(i % 97) - 1, 2, i + 1) for i in range(375334)) + b"\rs VERIFIED\n"
    t0 = time.monotonic()
    res, kept, left = run_filter(big, 17025620, chunk=1 << 16)
    check("C2 375334 exact duplicate lines (GB scale) are filtered and counted; only the status line is kept",
          res["ok"] and res["dup_lines"] == 375334 and res["dup_formula_phase"] == 375334 and kept == b"\rs VERIFIED\n"
          and res["raw_sha256"] == sha(big), seconds=round(time.monotonic() - t0, 2), raw_bytes=res["raw_bytes"])
    r, w = os.pipe()
    lr, lw = os.pipe()
    os.close(lr)  # the log 'file' refuses writes (EPIPE): the raw stream must still be read to EOF
    fds = m.Fds()
    fds.put("cor", r)
    fds.put("dlog", lw)
    res = {}
    t = threading.Thread(target=m._filter, args=(fds, res, 9), daemon=True)
    t.start()
    payload = b"\rc line one\n" * 20000
    os.write(w, payload[:60000])
    os.write(w, payload[60000:])
    os.close(w)
    t.join(10)
    check("C3 a log write error is recorded, the raw stream is still read to EOF (the checker never blocks) and ok is "
          "False", res.get("log_write_error") and res.get("eof_seen") is True and res["raw_bytes"] == len(payload)
          and res["ok"] is False and not t.is_alive(), error=res.get("log_write_error"))


def t_collector_writer_feeder():
    rnd = random.Random(11)
    proof = bytes(rnd.getrandbits(8) for _ in range(3 * (1 << 20) + 17))
    r, w = os.pipe()
    fds = m.Fds()
    fds.put("fifo_read", r)
    res, chunks = {"ok": False}, []
    t = threading.Thread(target=m._collector, args=(fds, res, chunks), daemon=True)
    t.start()
    for i in range(0, len(proof), 4093):
        os.write(w, proof[i:i + 4093])
    os.close(w)
    t.join(10)
    check("C4 collector: EOF only on read() == b'', sha256/count of exactly the bytes read, RAM chunks == stream, "
          "descriptor closed by its owner", res["ok"] and res["fifo_eof_seen"] and res["collected_bytes"] == len(proof)
          and res["collected_sha256"] == sha(proof) and b"".join(chunks) == proof and fds.names() == [])

    def feed(chs, mode, alter_at=None, close_first=False, hold=None):
        r, w = os.pipe()
        fds = m.Fds()
        fds.put("cpw", w)
        res, got = {"ok": False, "mode": mode}, []
        if close_first:
            os.close(r)
        t = threading.Thread(target=m._feeder, args=(fds, res, chs, mode, hold, alter_at), daemon=True)
        t.start()
        if not close_first:
            while True:
                b = os.read(r, 65536)
                if not b:
                    break
                got.append(b)
            os.close(r)
        t.join(10)
        return res, b"".join(got)

    def chunked(b, k=196613):
        return [b[i:i + k] for i in range(0, len(b), k)]
    rows = {}
    for mode, exp in (("plain", proof), ("truncate", proof[:-2]), ("suffix", proof + m.SUFFIX)):
        chs = chunked(proof)
        res, got = feed(chs, mode)
        rows[mode] = (res["ok"] and got == exp and res["fed_bytes"] == len(exp) and res["fed_sha256"] == sha(exp)
                      and all(c is None for c in chs))
    small = b"a\x02\x04\x00a\x03\x00d\x02\x04\x00a\x00"
    off = m.first_literal_byte(small)
    res, got = feed([small[:3], small[3:]], "alter", alter_at=off)
    exp = bytearray(small)
    exp[off] ^= 1
    rows["alter"] = (res["ok"] and got == bytes(exp) and res["fed_bytes"] == len(small)
                     and res["altered_offset"] == off and res["fed_sha256"] != sha(small))
    ev = threading.Event()
    ev.set()
    chs = chunked(proof)
    res, got = feed(chs, "hold", close_first=True, hold=ev)
    rows["hold-epipe"] = (res["ok"] is False and str(res.get("delivery_error")).startswith("EPIPE")
                          and res["fed_bytes"] == 0 and res["undelivered_bytes"] == len(proof)
                          and res["hold_released_by_event"] is True and all(c is None for c in chs))
    check("C5 feeder modes plain/truncate/suffix/alter/hold: exact bytes written and hashed, chunk slots released, "
          "EPIPE recorded with 0 fed and every chunk released", all(rows.values()), rows=rows)

    def write(parts, limit, close_first=False):
        r, w = os.pipe()
        fds = m.Fds()
        fds.put("x", w)
        res, got = {"ok": False}, []
        if close_first:
            os.close(r)
        t = threading.Thread(target=m._writer, args=(fds, "x", parts, res, limit), daemon=True)
        t.start()
        if not close_first:
            while True:
                b = os.read(r, 1 << 20)
                if not b:
                    break
                got.append(b)
            os.close(r)
        t.join(10)
        return res, b"".join(got)
    parts = [b"p cnf 3 9\n", proof[:1000000], proof[1000000:2500001], b"1 1 2 0\n"]
    whole = b"".join(parts)
    ok = True
    for lim in (len(whole), len(whole) - 1, 0, 10, 11):
        res, got = write(parts, lim)
        ok = ok and res["ok"] and res["written"] == lim and got == whole[:lim] and res["sha256"] == sha(whole[:lim])
    res, got = write(parts, len(whole), close_first=True)
    check("C6 measured writer: exact limit/short delivery hashed; EPIPE recorded as an error", ok
          and res["ok"] is False and "BrokenPipe" in res.get("error", ""))
    fds = m.Fds()
    r, w = os.pipe()
    fds.put("x", w)
    (fd,) = fds.take("x")
    os.close(fd)
    os.close(r)
    res = {"ok": False}
    m._writer(fds, "x", parts, res, len(whole))
    check("C7 a descriptor taken by the cleanup first is never used or closed by the worker",
          res["ok"] is False and res["fd_claimed"] is False and res["written"] == 0)
    cases = {b"a\x00a\x82\x01\x04\x00": 5, b"d\x02\x00a\x05\x00": 4, b"a\x00": None, b"x\x02\x00": None,
             b"a\x02": 1, b"": None, b"d\x02\x04\x00": None}
    check("C8 first_literal_byte on binary DRAT shapes", all(m.first_literal_byte(k) == v for k, v in cases.items()))


# --- D: the staged pipeline with python stubs for kissat and drat-trim
SOLVER_STUB = r"""
import sys, time
a = sys.argv[1:]
time.sleep(SLOW)
d = open(a[-2], "rb").read()
proof = b"a\x02\x04\x00" * 3000 + b"d\x02\x04\x00" + b"a\x00"
with open(a[-1], "wb") as f:
    f.write(proof)
print("c stub kissat read %d CNF bytes" % len(d))
print("s UNSATISFIABLE", flush=True)
sys.exit(20)
"""
CHECKER_STUB = r"""
import sys
a = sys.argv[1:]
out = sys.stdout
d = open(a[0], "rb").read()
out.write("\rc reading proof from stdin\n")
head = d.split(b"\n", 1)[0].split()
if len(head) != 4 or head[:2] != [b"p", b"cnf"]:
    out.write("\rc ERROR: did not find p cnf line in input file\n"); out.flush(); sys.exit(0)
out.write("\rc parsing input formula with %s variables and %s clauses\n" % (head[2].decode(), head[3].decode()))
for no, line in enumerate(d.split(b"\n")[1:], 1):
    s = sorted(int(x) for x in line.split()[:-1]) if line.strip() else []
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            out.write("\rc WARNING: detected and deleted duplicate literal %d at position %d of proof line %d\n"
                      % (s[i + 1], i + 1, no))
p = sys.stdin.buffer.read()
out.write("\rc finished parsing" + (", read %d bytes from proof file" % len(p) if p else "") + "\n")
if head[3] == b"7" or not p.endswith(b"a\x00"):
    out.write("\ns NOT VERIFIED\n"); out.flush(); sys.exit(1)
out.write("\rs VERIFIED\n\rc verification time: 0.001 seconds\n"); out.flush(); sys.exit(0)
"""
SAT_STUB = r"""
import sys
a = sys.argv[1:]
open(a[-2], "rb").read()
open(a[-1], "wb").close()
print("s SATISFIABLE\nv 1 2 3 0", flush=True)
sys.exit(10)
"""
EMPTY_STUB = r"""
import sys
a = sys.argv[1:]
open(a[-2], "rb").read()
open(a[-1], "wb").close()
print("s UNSATISFIABLE", flush=True)
sys.exit(20)
"""
SLEEP_STUB = r"""
import sys, time
a = sys.argv[1:]
open(a[-2], "rb").read()
f = open(a[-1], "wb"); f.write(b"a\x02\x00"); f.flush()
time.sleep(30)
sys.exit(20)
"""
IGNORE_STUB = r"""
import signal, sys, time
signal.signal(signal.SIGTERM, signal.SIG_IGN)
a = sys.argv[1:]
open(a[-2], "rb").read()
f = open(a[-1], "wb"); f.write(b"a\x02\x00"); f.flush()
time.sleep(4)
sys.exit(20)
"""


class Shim:
    """m.subprocess replacement: the pinned kissat/drat-trim argv[0] -> python -c stub; injected spawn failures."""

    def __init__(self, solver=None, checker=None, slow=0.0, fail=()):
        self.solver = solver or SOLVER_STUB.replace("SLOW", repr(slow))
        self.checker = checker or CHECKER_STUB
        self.fail = set(fail)
        self.spawned = []

    def __getattr__(self, k):
        return getattr(subprocess, k)

    def Popen(self, argv, **kw):
        if argv[0] == m.KISSAT:
            if "solver" in self.fail:
                raise FileNotFoundError(2, "injected solver spawn failure", argv[0])
            argv = [sys.executable, "-I", "-B", "-c", self.solver] + list(argv[1:])
        elif argv[0] == m.DRAT:
            if "checker" in self.fail:
                raise FileNotFoundError(2, "injected checker spawn failure", argv[0])
            argv = [sys.executable, "-I", "-B", "-c", self.checker] + list(argv[1:])
        else:
            raise AssertionError("unexpected spawn %r" % argv[:1])
        self.spawned.append(argv[0])
        return subprocess.Popen(argv, **kw)


COUNTER = {"n": 0}
PDIR = WORK + "/pipeline"


def pipe_run(it, shim=None, stop=None, ident_ok=True, lane=None, s_parts=None, c_parts=None):
    COUNTER["n"] += 1
    label = "sc-%02d-%s" % (COUNTER["n"], it["label"])
    stop = {} if stop is None else stop
    saved = (m.DESK, m.TMP, m.lane_scan, m.subprocess)
    m.DESK, m.TMP = PDIR, PDIR + "/tmp"
    m.lane_scan = lane or (lambda: ([], None))
    m.subprocess = shim or Shim()
    if s_parts is None:
        spec = m.CONTROLS[it["name"]]
        s_parts, c_parts = [spec["solver"]], [spec["checker"]]
    f0 = open_fds()
    try:
        def ident(stage, parts):
            return {"stage": stage, "ok": ident_ok, "problems": [] if ident_ok else ["injected identity refusal"]}
        rec = m.pipeline(label, it, s_parts, c_parts, ident, lambda s: None, stop)
    finally:
        m.DESK, m.TMP, m.lane_scan, m.subprocess = saved
    rec["pre_launch_identity"] = m.control_identity(it, s_parts, c_parts)
    rec["pre_evaluation_check"] = {"checked": True, "at": m.now(), "stop_signal": stop.get("signal"),
                                   "scanner_failed": (rec.get("lane_scanner") or {}).get("failed"),
                                   "helper_survivors": list(m.HELPER_SURVIVORS)}
    verdict, reasons, crit = m.evaluate(rec, it)
    time.sleep(0.05)
    return rec, verdict, reasons, crit, sorted(open_fds() ^ f0)


def settled(rec, leak):
    return (not leak and rec["fds_left_after_cleanup"] == [] and rec["children_alive"] == []
            and rec["threads_unfinished"] == [])


def t_pipeline_controls():
    for sub in ("", "/fifo", "/logs", "/tmp"):
        os.mkdir(PDIR + sub)
    for name in m.CONTROLS:
        it = m.control_item(name)
        rec, v, why, crit, leak = pipe_run(it)
        check("D1 %s through the staged pipeline with stubs -> %s (preregistered %s); settled, nothing left for the "
              "cleanup" % (name, v, it["preregistered_verdict"]),
              v == it["preregistered_verdict"] and settled(rec, leak) and rec["fds_closed_by_cleanup"] == [],
              reasons=why, leak=leak, failed=[k for k in m.CRITERIA if not crit[k]])
    it = dict(m.control_item("unsat"), kind="gb", id="P1-B4")
    del it["name"]
    rec, v, why, crit, leak = pipe_run(it, s_parts=[m.UNSAT3D], c_parts=[m.UNSAT3D])
    CTX["good_gb"] = (rec, it)
    check("D2 gb-kind item with stub natives: PASS only with the full conjunction; R == D == N, equal digests incl. "
          "the independent buffer digest", v == "PASS" and settled(rec, leak)
          and rec["threads"]["collector"]["collected_bytes"] == rec["threads"]["feeder"]["fed_bytes"]
          == rec["threads"]["filter"]["proof_bytes_parsed"][0] == rec["proof_buffer"]["bytes"], reasons=why)


def t_pipeline_failures():
    unsat = m.control_item("unsat")
    cases = [
        ("D3a kissat spawn error", dict(shim=Shim(fail=("solver",))), "solver spawn failed"),
        ("D3b drat-trim spawn error", dict(shim=Shim(fail=("checker",))), "checker spawn failed"),
        ("D3c identity refusal before the kissat spawn", dict(ident_ok=False), "identity re-hash before the solver"),
        ("D3d SIGTERM latched before the kissat spawn", dict(stop={"signal": "SIGTERM"}), "driver received SIGTERM"),
    ]
    for name, kw, want in cases:
        rec, v, why, crit, leak = pipe_run(unsat, **kw)
        check(name + ": stop reason, no stage 2 native, settled, not PASS", v != "PASS" and settled(rec, leak)
              and want in (rec.get("safety_stop_reason") or ""), reason=rec.get("safety_stop_reason"))
    orig_start = threading.Thread.start
    for target, after in ((m._collector, False), (m._writer, False), (m._filter, False), (m._feeder, False),
                          (m._feeder, True), (m._collector, True)):
        def failing_start(self, target=target, after=after):
            if getattr(self, "_target", None) is target:
                if after:
                    orig_start(self)
                    raise RuntimeError("injected: start() interrupted after the thread started")
                raise RuntimeError("injected: Thread.start failed")
            return orig_start(self)
        threading.Thread.start = failing_start
        try:
            rec, v, why, crit, leak = pipe_run(unsat)
        finally:
            threading.Thread.start = orig_start
        live_sigtermed = all(c.get("sigterm_sent") for c in rec["children"].values() if c.get("exit_code") is None)
        check("D4 %s start() fails%s: exception path SIGTERMs the live child, bounded reap, every unclaimed fd closed "
              "once by the cleanup, no leak, not PASS" % (target.__name__, " after starting" if after else ""),
              v != "PASS" and "exception" in rec and settled(rec, leak) and live_sigtermed,
              closed_by_cleanup=rec["fds_closed_by_cleanup"], children={k: c.get("exit_code") for k, c in
                                                                         rec["children"].items()})
    stop = {}
    threading.Timer(1.0, lambda: stop.__setitem__("signal", "SIGTERM")).start()
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(solver=SLEEP_STUB), stop=stop)
    check("D5a driver SIGTERM in flight: kissat SIGTERMed (not a self-exit), reaped, settled, not PASS",
          v != "PASS" and settled(rec, leak) and rec["children"]["solver"]["sigterm_sent"] is True
          and not crit["solver_self_exit_20"] and not crit["no_driver_signal_latched"])
    real_fb, cnt = m.free_bytes, {"n": 0}

    def fb_boom():
        cnt["n"] += 1
        if cnt["n"] == 3:
            raise KeyboardInterrupt("injected in supervise")
        return real_fb()
    m.free_bytes = fb_boom
    try:
        rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(solver=SLEEP_STUB))
    finally:
        m.free_bytes = real_fb
    check("D5b KeyboardInterrupt inside supervise: caught by the cleanup scope, child SIGTERMed and reaped, settled",
          v != "PASS" and "KeyboardInterrupt" in rec.get("exception", "") and settled(rec, leak))
    saved = m.SIGTERM_GRACE
    m.SIGTERM_GRACE = 1.5
    stop = {}
    threading.Timer(0.8, lambda: stop.__setitem__("signal", "SIGTERM")).start()
    try:
        rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(solver=IGNORE_STUB), stop=stop)
    finally:
        m.SIGTERM_GRACE = saved
    pid, reaped = rec.get("solver_pid"), False
    for _ in range(100):  # test hygiene: the SIGTERM-ignoring stub exits by itself after 4 s; reap it here
        p_, _st = os.waitpid(pid, os.WNOHANG)
        if p_:
            reaped = True
            break
        time.sleep(0.1)
    check("D5c a child ignoring SIGTERM: grace exceeded (patched to 1.5 s), no escalation, recorded alive, PASS vetoed",
          v != "PASS" and rec["sigterm_grace_exceeded"] is True and rec["children_alive"] == ["solver"]
          and not crit["children_reaped"] and reaped, events=[e["event"] for e in rec["events"]])
    calls = {"n": 0}

    def fail_once():
        calls["n"] += 1
        return (None, "injected scan failure") if calls["n"] == 1 else ([], None)
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(slow=1.5), lane=fail_once)
    check("D6a one failed lane reading: latched -> safety stop, never PASS", v != "PASS" and settled(rec, leak)
          and rec["lane_scanner"]["failed"] is not None and "latched" in (rec.get("safety_stop_reason") or ""))
    ga = lambda: ([{"pid": 999999, "ppid": 1, "comm": "cadical", "native": True, "rss_bytes": 1 << 20, "cpu_ns": 0,
                    "state": "R", "cwd": "/x/review/moqls8-strengthened-parent-replay-v1/tmp/a/solver",
                    "args": "cadical", "exclusion": ["parent GA replay process: no GA/GB concurrency"]}], None)
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(slow=1.5), lane=ga)
    check("D6b a GA replay native appearing in flight: exclusion breach latched -> safety stop", v != "PASS"
          and settled(rec, leak) and "exclusion breach" in (rec.get("safety_stop_reason") or ""))
    big = lambda: ([{"pid": 999998, "ppid": 1, "comm": "python3", "native": False, "rss_bytes": 11 << 30,
                     "cpu_ns": 0, "state": "S", "cwd": "/x/moqls8-problem16", "args": "x", "exclusion": []}], None)
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(slow=1.5), lane=big)
    check("D6c lane total above 11 GiB in flight -> safety stop", v != "PASS" and settled(rec, leak)
          and "lane RSS" in (rec.get("safety_stop_reason") or ""))
    rec, v, why, crit, leak = pipe_run(dict(unsat, desk_cap_bytes=1 << 20), shim=Shim(slow=1.0))
    check("D6d pipeline aggregate RSS (driver incl. buffers + child) above the cap -> safety stop", v != "PASS"
          and settled(rec, leak) and "pipeline aggregate RSS" in (rec.get("safety_stop_reason") or ""))
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(solver=SAT_STUB))
    check("D7a kissat SAT report (exit 10): stage 2 skipped, solver_reported_sat, not PASS", v != "PASS"
          and m.solver_reported_sat(rec) and "checker" not in rec["children"] and rec.get("stage2_skipped")
          and settled(rec, leak), skipped=rec.get("stage2_skipped"))
    rec, v, why, crit, leak = pipe_run(unsat, shim=Shim(solver=EMPTY_STUB))
    check("D7b exit 20 with an empty proof (R == 0): stage 2 skipped, not PASS", v != "PASS"
          and rec.get("stage2_skipped") == ["proof_positive"] and settled(rec, leak))


# --- E: the evaluator
def mutate(rec, path, value):
    r = copy.deepcopy(rec)
    o = r
    for k in path[:-1]:
        o = o[k]
    if value is KeyError:
        del o[path[-1]]
    else:
        o[path[-1]] = value
    return r


def t_evaluate():
    good, it = CTX["good_gb"]
    th = good["threads"]
    muts = {
        "formula_identity_bound": (("pre_launch_identity", "ok"), False),
        "identity_rehashed_before_solver_spawn": (("identity_solver", "ok"), False),
        "identity_rehashed_before_checker_spawn": (("identity_checker", "ok"), False),
        "solver_feed_measured_complete": (("threads", "solver_feed", "written"), th["solver_feed"]["written"] - 1),
        "checker_feed_measured_complete": (("threads", "checker_feed", "sha256"), "0" * 64),
        "solver_self_exit_20": (("children", "solver", "sigterm_sent"), True),
        "solver_status_exact_unsat": (("solver_status_lines",), ["s UNSATISFIABLE", "s UNSATISFIABLE"]),
        "collector_eof_clean": (("threads", "collector", "fifo_eof_seen"), KeyError),
        "proof_positive": (("threads", "collector", "collected_bytes"), 0),
        "proof_buffer_digest_agrees": (("proof_buffer", "sha256"), "1" * 64),
        "feeder_plain_complete": (("threads", "feeder", "undelivered_bytes"), 1),
        "proof_fed_equals_collected": (("threads", "feeder", "fed_sha256"), "2" * 64),
        "checker_self_exit_0": (("children", "checker", "exit_code"), 1),
        "checker_status_exact_verified": (("threads", "filter", "status_line_count"), 2),
        "checker_no_not_verified_or_timeout": (("threads", "filter", "timeout_lines"), 1),
        "checker_no_early_eof_or_less_than_expected": (("threads", "filter", "less_than_expected_lines"), 1),
        "checker_header_counts_match": (("threads", "filter", "header_counts"), [[3, 8]]),
        "checker_consumed_proof_bytes_equal_fed": (("threads", "filter", "proof_bytes_parsed"),
                                                   [th["feeder"]["fed_bytes"] + 1]),
        "checker_stream_filter_clean": (("drat_filtered_log_on_disk", "sha256"), "3" * 64),
        "no_safety_stop": (("stage2_skipped",), ["x"]),
        "no_driver_signal_latched": (("pre_evaluation_check", "stop_signal"), "SIGTERM"),
        "lane_scanner_clean": (("lane_scanner", "failures"), 1),
        "all_threads_finished": (("threads_unfinished",), ["feeder"]),
        "all_fds_settled": (("fds_closed_by_cleanup",), ["cpw"]),
        "children_reaped": (("children_alive",), ["checker"]),
        "no_helper_survivor": (("helper_survivors",), [{"pid": 1}]),
    }
    bad = []
    for k in m.CRITERIA:
        path, val = muts[k]
        v, why, crit = m.evaluate(mutate(good, path, val), it)
        failed = [x for x in m.CRITERIA if not crit[x]]
        if v != "UNKNOWN" or failed != [k]:
            bad.append((k, v, failed))
    check("E1 every single-criterion mutation of a PASS record gives UNKNOWN failing exactly that criterion (26)",
          not bad and set(muts) == set(m.CRITERIA) and m.evaluate(good, it)[0] == "PASS", bad=bad[:3])
    r = mutate(good, ("threads", "checker_feed", "written"), th["checker_feed"]["written"] - 1)
    r = mutate(r, ("threads", "checker_feed", "sha256"), sha(m.UNSAT3D[:-1]))
    v1, _w, c1 = m.evaluate(r, it)
    r = mutate(good, ("threads", "solver_feed", "written"), th["solver_feed"]["written"] - 1)
    v2, _w, c2 = m.evaluate(r, it)
    check("E2 native statuses cannot substitute for incomplete delivery: kissat exit 20 + exact UNSAT and drat-trim "
          "exit 0 + exact VERIFIED + N == D, with a short checker (or solver) feed -> UNKNOWN on the feed criterion "
          "alone", v1 == v2 == "UNKNOWN" and [k for k in m.CRITERIA if not c1[k]] == ["checker_feed_measured_complete"]
          and [k for k in m.CRITERIA if not c2[k]] == ["solver_feed_measured_complete"])
    r = mutate(good, ("threads", "collector", "collected_sha256"), "4" * 64)
    v3, _w, c3 = m.evaluate(r, it)
    r = mutate(good, ("threads", "feeder", "fed_sha256"), "5" * 64)
    v4, _w, c4 = m.evaluate(r, it)
    check("E3 an altered recorded collector digest or transported digest fails the predicate (digest equality)",
          v3 == v4 == "UNKNOWN" and not c3["proof_fed_equals_collected"] and not c3["proof_buffer_digest_agrees"]
          and not c4["proof_fed_equals_collected"])
    ok = True
    rows = {}
    for name in m.CONTROLS:
        cit = m.control_item(name)
        rec, v, why, crit, leak = pipe_run(cit)
        extra = mutate(rec, ("lane_scanner", "failures"), 1)
        ve = m.evaluate(extra, cit)[0]
        rows[name] = [v, ve]
        ok = ok and v == cit["preregistered_verdict"] and ve == "INVALID_CONTROL"
        if cit["must_fail"]:
            k = cit["must_fail"][0]
            # make the intended failure disappear: a control whose intended criterion holds is invalid
            fixed = mutate(rec, ("pre_evaluation_check", "checked"), True)
            if k == "checker_feed_measured_complete":
                fixed = mutate(fixed, ("threads", "checker_feed", "written"), cit["expected_checker_feed_bytes"])
                fixed = mutate(fixed, ("threads", "checker_feed", "sha256"), cit["expected_checker_feed_sha256"])
            elif k == "feeder_plain_complete":
                f = fixed["threads"]["feeder"]
                for kk in ("delivery_error", "suffix_delivered_bytes", "altered_offset"):
                    f.pop(kk, None)
                f.update(mode="plain", undelivered_bytes=0, ok=True)
            elif k == "checker_self_exit_0":
                fixed["children"]["checker"]["exit_code"] = 0
            vf = m.evaluate(fixed, cit)[0]
            rows[name].append(vf)
            ok = ok and vf == "INVALID_CONTROL"
    check("E4 control verdicts: each control yields its preregistered verdict; an extra unrelated failure, or the "
          "absence of its intended failure, yields INVALID_CONTROL", ok, rows=rows)


# --- F: gate, monitor rule, exclusion flags, lane_scan parsing, helper ownership
def mon(samples, extra=b"", start=True):
    lines = [b'{"event": "start", "at": "x", "interval": 10}'] if start else []
    for t, f in samples:
        lines.append(json.dumps({"t": t, "free": f}).encode())
    return b"\n".join(lines) + b"\n" + extra


def iso(ts):
    import datetime
    return datetime.datetime.fromtimestamp(ts, m.PDT).isoformat(timespec="seconds")


def t_monitor():
    now = 1792360000.0
    base = [(now - 5 - 10 * k, 186000000000) for k in range(31)][::-1]
    S = lambda arr: [(iso(t), f) for t, f in arr]
    ok = m.monitor_stability(mon(S(base)), now)[0]
    restart = b'{"at": "x", "event": "restart", "interval": 10, "note": "no missing samples reconstructed"}\n'
    raw = mon(S(base[:15])) + restart + mon(S(base[15:]), start=False)
    ok_restart = m.monitor_stability(raw, now)[0]
    gap = S(base[:10] + base[20:])
    cases = {
        "malformed complete line": mon(S(base), b"{bad\n"),
        "naive timestamp": mon(S(base[:-1]) + [(iso(base[-1][0])[:19], base[-1][1])]),
        "non-monotone": mon(S(base[:-1] + [(base[-2][0], base[-1][1])])),
        "stale": mon(S([(t - 40, f) for t, f in base])),
        "future sample": mon(S([(t + 20, f) for t, f in base])),
        "few samples (restart gap, nothing reconstructed)": mon(gap),
        "free below 13.5e9+10MiB": mon(S([(t, 13500000000) for t, f in base])),
        "drop over allowance": mon(S(base[:-1] + [(base[-1][0], 186000000000 - 15000000000)])),
        "bool free": mon(S(base[:-1])) + json.dumps({"t": iso(base[-1][0]), "free": True}).encode() + b"\n",
        "string free": mon(S(base[:-1])) + json.dumps({"t": iso(base[-1][0]), "free": "1"}).encode() + b"\n",
    }
    refused = {k: m.monitor_stability(v, now)[0] is False for k, v in cases.items()}
    tail_ok = m.monitor_stability(mon(S(base), b'{"t": "2026'), now)[0]
    check("F1 monitor rule (unchanged v5d code): passes on 31 good samples and across an event record (restart "
          "ignored, never reconstructed); refuses malformed, naive, non-monotone, stale, future, gap-thinned, low "
          "free, excessive drop, bool/str free; ignores only an unterminated last line",
          ok and ok_restart and all(refused.values()) and tail_ok, refused=refused)
    ok_real, info = m.monitor_stability()
    check("F2 real parent monitor read (informational: the rule's verdict now)", True, monitor_ok=ok_real,
          checks=info.get("checks"), events=info.get("event_records"), last_free=info.get("last_free"))


def lane(rows):
    return lambda: ([dict(r) for r in rows], None)


def row(pid, comm, native, rss, cwd="/x/moqls8-problem16", args="x", exclusion=(), cpu=0):
    return {"pid": pid, "ppid": 1, "comm": comm, "native": native, "rss_bytes": rss, "cpu_ns": cpu, "state": "S",
            "cwd": cwd, "args": args, "exclusion": list(exclusion)}


def t_gate():
    G = 1 << 30
    saved = (m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW, m.taskinfo, m.monitor_stability)
    try:
        m.WAIT_POLL, m.HOT_WINDOW, m.WAIT_BUDGET = 0, 0.01, 3600
        m.lane_scan = lane([])
        g = m.gate("sc-pass", m.GB_RESERVATION, {"used": 0.0}, lambda s: None, {}, stable=False)
        check("F3a empty lane: two consecutive passing checks launch", g["launch"] is True
              and len(g["samples"]) == 2)
        m.WAIT_BUDGET = 0
        refusals = {}
        for name, rows in (("busy 4 others", [row(10 + i, "cadical", True, 1) for i in range(4)]),
                           ("other 5.5 GiB + 6 GiB reservation", [row(20, "python3", False, 55 * G // 10)]),
                           ("GA native", [row(30, "cadical", True, 1, exclusion=["GA"])]),
                           ("other kissat", [row(31, "kissat", True, 1, exclusion=["kissat"])])):
            m.lane_scan = lane(rows)
            g = m.gate("sc-" + name, m.GB_RESERVATION, {"used": 0.0}, lambda s: None, {}, stable=False)
            refusals[name] = g["launch"] is False
        m.lane_scan = lane([row(20, "python3", False, 45 * G // 10)])
        m.WAIT_BUDGET = 3600
        g = m.gate("sc-fits", m.GB_RESERVATION, {"used": 0.0}, lambda s: None, {}, stable=False)
        fits = g["launch"] is True
        m.WAIT_BUDGET = 0
        me = os.getpid()
        real_ti = saved[4]
        m.taskinfo = lambda pid: None if pid == me else real_ti(pid)
        m.lane_scan = lane([])
        g = m.gate("sc-unreadable", m.GB_RESERVATION, {"used": 0.0}, lambda s: None, {}, stable=False)
        refusals["unreadable driver RSS"] = g["launch"] is False and g["samples"][0]["ok_rss"] is False
        m.taskinfo = real_ti
        m.monitor_stability = lambda raw=None, nowt=None: (False, {"ok": False})
        g = m.gate("sc-unstable", m.GB_RESERVATION, {"used": 0.0}, lambda s: None, {}, stable=True)
        refusals["monitor rule fails (gb)"] = g["launch"] is False and g["samples"][0]["ok_stable"] is False
        g = m.gate("sc-ctl-plain", m.CONTROL_RESERVATION, {"used": 0.0}, lambda s: None, {"signal": "SIGTERM"},
                   stable=False)
        refusals["latched SIGTERM"] = g["launch"] is False and "SIGTERM" in g.get("stopped", "")
        check("F3b gate refuses: 4 other busy natives (busy + 1 > 4), other 5.5 GiB + 6 GiB reservation > 11 GiB, a "
              "GA replay native, another kissat, unreadable driver RSS, a failing monitor rule (gb), a latched "
              "SIGTERM; other 4.5 GiB + 6 GiB fits", all(refusals.values()) and fits, refusals=refusals)
    finally:
        m.lane_scan, m.WAIT_POLL, m.WAIT_BUDGET, m.HOT_WINDOW, m.taskinfo, m.monitor_stability = saved
    far = " " * 300 + "/review/moqls8-strengthened-parent-replay-v1/scripts/replay_v5e.py run PRE"
    cases = {
        "GA native in the GA desk": ({"cwd": "/R/review/moqls8-strengthened-parent-replay-v1/tmp/x/solver",
                                      "native": True, "comm": "cadical"}, "cadical", True),
        "GA driver (marker beyond 240 chars of argv)": ({"cwd": "/R/review/moqls8-strengthened-parent-replay-v1/tmp",
                                                         "native": False, "comm": "Python"},
                                                        "/usr/bin/python3 -I -B" + far, True),
        "parent audit python with cwd in the GA desk": ({"cwd": "/R/review/moqls8-strengthened-parent-replay-v1",
                                                         "native": False, "comm": "python3.14"},
                                                        "python3.14 -c 'print(1)'", False),
        "other kissat": ({"cwd": "/L/moqls8-problem16/x", "native": True, "comm": "kissat"}, "kissat x", True),
        "worker GB driver": ({"cwd": "/L/moqls8-problem16", "native": False, "comm": "python3.14"},
                             "python3.14 code/gb_direct_r6.py run", True),
        "another gb_staged driver": ({"cwd": "/D/tmp", "native": False, "comm": "python3.14"},
                                     "python3.14 -I -B scripts/gb_staged_v1.py run X", True),
        "unrelated lane python": ({"cwd": "/L/moqls8-problem16", "native": False, "comm": "python3"},
                                  "python3 tools/x.py", False),
    }
    res = {k: bool(m.exclusion_flags(c, a)) == want for k, (c, a, want) in cases.items()}
    check("F4 exclusion flags on the full argv/cwd (GA natives and replay/launch drivers, other kissat, other GB "
          "drivers; not a parent audit python or an unrelated lane python)", all(res.values()), res=res)
    real = m.run_helper
    seq = {}

    def fake(argv):
        return seq[argv[0] + (":" + argv[1] if argv[0] == "/bin/ps" else "")]
    try:
        m.run_helper = fake
        seq.update({"/bin/ps:-axww": (0, b"  1 0 100 S launchd\nnot-a-row\n", None)})
        bad_row = m.lane_scan()
        seq.update({"/bin/ps:-axww": (0, b"  4242 1 1000 R kissat\n\n", None),
                    "/usr/sbin/lsof": (0, b"p4242\nn/L/moqls8-problem16/w\n", None),
                    "/bin/ps:-ww": (0, b"4242 /opt/kissat --time=1 /dev/fd/3 x.fifo\n", None)})
        good = m.lane_scan()
        seq.update({"/bin/ps:-axww": (1, b"", None)})
        rc1 = m.lane_scan()
    finally:
        m.run_helper = real
    check("F5 lane_scan: a malformed ps row fails the scan (stricter than v5d); a lane kissat carries its exclusion "
          "flag; a ps rc != 0 fails", bad_row[0] is None and "malformed ps row" in bad_row[1]
          and good[0] is not None and good[0][0]["exclusion"] == ["another kissat process: one GB native at a time"]
          and rc1[0] is None, bad=bad_row[1], good=good[0])
    saved = (m.HELPER_DEADLINE, m.HELPER_TERM_WAIT)
    m.HELPER_DEADLINE, m.HELPER_TERM_WAIT = 1.0, 2.0
    try:
        f0 = open_fds()
        rc, out, err = m.run_helper([sys.executable, "-I", "-B", "-c", "import time; time.sleep(30)"])
        check("F6 run_helper (unchanged v5d): an overrunning helper is SIGTERMed and reaped within the bounded wait, "
              "no survivor, no fd leak", rc == -15 and err and not m.HELPER_SURVIVORS and open_fds() == f0,
              rc=rc, err=err)
    finally:
        m.HELPER_DEADLINE, m.HELPER_TERM_WAIT = saved


# --- G: static checks on the exact runtime bytes
def t_static():
    import ast
    text = RT_BYTES.decode()
    tree = ast.parse(text)
    parents = {}
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node
    attrs = [n for n in ast.walk(tree) if isinstance(n, ast.Attribute)]
    bad_attr = sorted({n.attr for n in attrs if n.attr in ("SIGKILL", "killpg", "terminate", "communicate",
                                                            "send_signal", "rmtree", "check_output", "check_call")})
    bad_os = sorted({n.attr for n in attrs if isinstance(n.value, ast.Name) and n.value.id == "os"
                     and n.attr in ("unlink", "remove", "rmdir", "removedirs", "rename", "replace", "killpg")})
    bad_sp = sorted({n.attr for n in attrs if isinstance(n.value, ast.Name) and n.value.id == "subprocess"
                     and n.attr in ("run", "call", "check_call", "check_output", "getoutput", "getstatusoutput")})
    imports = sorted({a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                      for a in n.names} | {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)})
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)]
    kills = [n for n in calls if n.func.attr == "kill"]
    kill_ok = len(kills) == 2 and all(ast.unparse(k) == "os.kill(p.pid, signal.SIGTERM)" for k in kills)
    waits = sorted({ast.unparse(n.func.value) for n in calls if n.func.attr == "wait"})
    timeouts = [ast.unparse(n) for n in calls if any(k.arg == "timeout" for k in n.keywords)]
    tmp_consts = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)
                  and n.value.startswith("/tmp") and not (isinstance(parents.get(n), ast.BinOp)
                                                          and parents[n].right is n)]
    opens = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
             and n.func.id == "open"]
    modes = sorted({ast.unparse(n.args[1]) if len(n.args) > 1 else "'r'" for n in opens})
    osopens = [ast.unparse(n) for n in calls if n.func.attr == "open" and isinstance(n.func.value, ast.Name)
               and n.func.value.id == "os"]
    popens = [n for n in calls if n.func.attr == "Popen"]
    check("G1 static (AST of the exact runtime bytes): no SIGKILL/killpg/terminate/communicate/send_signal, no "
          "subprocess.run/call/check_*, no os.unlink/remove/rmdir/rename/replace, no shutil/tempfile, no /tmp path, "
          "no timeout= keyword anywhere; os.kill only as os.kill(p.pid, signal.SIGTERM) (helper and owned child); "
          ".wait only on threading Events; files created only with 'x'/'xb' or O_EXCL (FIFO opened O_RDONLY / "
          "keepalive O_WRONLY); three Popen calls (helper, kissat, drat-trim)",
          not bad_attr and not bad_os and not bad_sp and not ({"shutil", "tempfile"} & set(imports)) and kill_ok
          and waits == ["hold", "self.halt"] and not timeouts and not tmp_consts
          and set(modes) <= {"'x'", "'xb'", "'rb'"} and len(popens) == 3
          and all("O_EXCL" in o or "O_RDONLY" in o or o == "os.open(fifo, os.O_WRONLY)" for o in osopens),
          bad=[bad_attr, bad_os, bad_sp], waits=waits, timeouts=timeouts, modes=modes, os_opens=osopens)
    check("G2 native argv: kissat --time=3600 /dev/fd/N FIFO; drat-trim /dev/fd/N -i -t 7200 (argv[1] is the CNF)",
          m.KISSAT_SECONDS == 3600 and m.DRAT_SECONDS == 7200
          and 'kissat_argv = [KISSAT, "--time=%d" % KISSAT_SECONDS]' in text
          and 'drat_opts = ["-i", "-t", str(DRAT_SECONDS)]' in text
          and '[DRAT, "/dev/fd/%d" % fds.get("ccr")] + drat_opts' in text)
    v5 = open(V5D, "rb").read().decode()
    v5tree = ast.parse(v5)

    def seg(tree_, src, name):
        for n in tree_.body:
            if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name == name:
                return ast.get_source_segment(src, n)
        return None
    same = {n: seg(tree, text, n) is not None and seg(tree, text, n) == seg(v5tree, v5, n)
            for n in ("_stop_helper", "run_helper", "Scanner", "gate_scan", "monitor_stability", "latched_stop", "Fds",
                      "taskinfo", "_Timebase")}

    def node(tree_, name):
        return next(n for n in tree_.body if isinstance(n, ast.FunctionDef) and n.name == name)

    def nodoc(fn):
        fn = copy.deepcopy(fn)
        fn.body = fn.body[1:] if isinstance(fn.body[0], ast.Expr) and isinstance(fn.body[0].value, ast.Constant) \
            else fn.body
        return ast.dump(fn)
    pid_gone_same = nodoc(node(tree, "pid_gone")) == nodoc(node(v5tree, "pid_gone"))
    check("G3 reused replay_v5d.py (ee52004b) code: _stop_helper, run_helper, Scanner, gate_scan, monitor_stability, "
          "latched_stop, Fds, taskinfo, _Timebase byte-identical; pid_gone identical except its shortened docstring",
          all(same.values()) and pid_gone_same
          and hashlib.sha256(v5.encode()).hexdigest() == m.PROVENANCE["ga_runtime_patterns_replay_v5d"][1], same=same,
          pid_gone_same_without_docstring=pid_gone_same)
    limits = (m.LANE_BUSY_CAP, m.MINE, m.LANE_RSS_LIMIT, m.GB_PIPELINE_CAP, m.GB_RESERVATION, m.LAUNCH_FLOOR, m.FLOOR,
              m.SIGTERM_GRACE, m.STABLE_FREE_MIN, m.STABLE_MIN_DROP_CAP, m.STABLE_RUNWAY_DIV, m.STABLE_MAX_AGE,
              m.STABLE_MIN_SAMPLES, m.STABLE_MIN_SPAN, m.STABLE_WINDOW)
    check("G4 limits: busy cap 4 (one own native), lane 11 GiB, pipeline cap 6 GiB reserved, launch 12.2e9+10MiB, "
          "floor 12e9, grace 120 s, monitor 13.5e9+10MiB/300e6/12/30 s/25/290 s/300 s; 17:29 and 17:57 PDT",
          limits == (4, 1, 11811160064, 6442450944, 6442450944, 12210485760, 12000000000, 120, 13510485760,
                     300000000, 12, 30.0, 25, 290.0, 300.0)
          and m.NO_LAUNCH_AT == 1792369740.0 and m.NATIVE_STOP_AT == 1792371420.0, limits=limits)


# --- H: the CLI paths end to end with stub natives in a sandbox desk (no native tool, no n=8 generation)
def t_cli():
    root = WORK + "/cli"
    sdesk = root + "/desk"
    for d in (root, sdesk, sdesk + "/fifo", sdesk + "/logs", sdesk + "/receipts", sdesk + "/runs", sdesk + "/tmp"):
        os.mkdir(d)
    saved = (m.REVIEW, m.DESK, m.TMP, m.ENV, m.lane_scan, m.subprocess, m.WAIT_POLL, m.HOT_WINDOW,
             os.environ.get("TMPDIR"), os.getcwd(), m.monitor_stability)
    shim = Shim()
    try:
        m.REVIEW, m.DESK, m.TMP = root, sdesk, sdesk + "/tmp"
        m.ENV = dict(m.ENV, TMPDIR=m.TMP + "/")
        m.lane_scan, m.subprocess, m.WAIT_POLL, m.HOT_WINDOW = (lambda: ([], None)), shim, 0, 0.01
        os.environ["TMPDIR"] = m.TMP + "/"
        pre = sdesk + "/PRE-EXEC-controls.json"
        m.cmd_preexec([pre] + ["control:" + n for n in m.CONTROLS])
        pre_raw = open(pre, "rb").read()
        prej = json.loads(pre_raw)
        go = root + "/GO-controls.json"
        with open(go, "x") as f:
            json.dump({"status": "PARENT_GO", "desk": m.DESK_REL, "script_sha256": RT_SHA,
                       "pre_exec_sha256": sha(pre_raw), "scope": "controls",
                       "items": [it["item"] for it in prej["items"]]}, f)
        m.cmd_run([pre, go])
        runs = sorted(os.listdir(sdesk + "/runs"))
        summary = json.load(open(sdesk + "/runs/" + runs[-1]))
        verdicts = {e["label"]: e.get("verdict") for e in summary["items"]}
        adm, probs = m.validate_controls(RT_SHA)
        check("H1 sandbox CLI: preexec (7 controls) -> parent GO -> run: 7 receipts with the preregistered verdicts, "
              "no stop; validate_controls admits them for this script sha256 (stub natives only)",
              summary["stopped_reason"] is None and verdicts == {m.LABEL_PREFIX + "ctl-" + n: v
                                                                 for n, v in m.WANT_VERDICTS.items()}
              and len(adm) == 7 and not probs and all(x == "kissat" or x == sys.executable for x in shim.spawned[:1]),
              verdicts=verdicts)
        gpre = sdesk + "/PRE-EXEC-gb-P1-B4-a1.json"
        m.cmd_preexec([gpre, "gb:P1-B4:a1"])
        gj = json.loads(open(gpre, "rb").read())
        check("H2 sandbox gb preexec: admitted only with the seven control receipts of this script sha256; the "
              "PRE-EXEC carries the GBBINDING record and expected feeds; nothing regenerated or launched",
              gj["run_kind"] == "science" and len(gj["admission_controls"]) == 7
              and gj["items"][0]["bound"]["sha256"] == CTX["binding"]["records"]["P1-B4"]["sha256"]
              and gj["items"][0]["expected_solver_feed_bytes"] == CTX["binding"]["records"]["P1-B4"]["bytes"])
        refusals = {}

        def refused(fn, *a):
            try:
                fn(*a)
            except SystemExit as e:
                return str(e)
            return None
        refusals["run gb with the controls GO"] = refused(m.cmd_run, [gpre, go])
        refusals["preexec an unauthorized id"] = refused(m.cmd_preexec, [sdesk + "/x1.json", "gb:P1-B2:a1"])
        refusals["preexec mixed kinds"] = refused(m.cmd_preexec, [sdesk + "/x2.json", "control:unsat", "gb:P1-B4:a1"])
        refusals["preexec two gb items"] = refused(m.cmd_preexec, [sdesk + "/x3.json", "gb:P1-B4:a2", "gb:P0-B4:a1"])
        refusals["preexec an existing label (receipt exists)"] = refused(m.cmd_preexec, [sdesk + "/x4.json",
                                                                                         "control:unsat"])
        bad = dict(prej)
        bad["items"] = [dict(prej["items"][0], must_fail=["checker_feed_measured_complete"])]
        badp = sdesk + "/PRE-EXEC-tampered.json"
        with open(badp, "x") as f:
            json.dump(bad, f)
        refusals["run a tampered PRE-EXEC"] = refused(m.cmd_run, [badp, go])
        os.environ["TMPDIR"] = "/tmp/"
        refusals["TMPDIR outside the desk"] = refused(m.cmd_run, [pre, go])
        check("H3 CLI refusals before any spawn or regeneration", all(refusals.values())
              and not any(os.path.exists(sdesk + "/x%d.json" % i) for i in (1, 2, 3, 4)),
              refusals={k: (v or "")[:80] for k, v in refusals.items()})
    finally:
        (m.REVIEW, m.DESK, m.TMP, m.ENV, m.lane_scan, m.subprocess, m.WAIT_POLL, m.HOT_WINDOW, tmpdir, cwd,
         m.monitor_stability) = saved
        if tmpdir is None:
            os.environ.pop("TMPDIR", None)
        else:
            os.environ["TMPDIR"] = tmpdir
        os.chdir(cwd)
        import signal
        signal.signal(signal.SIGTERM, signal.SIG_DFL)


def main():
    started = m.now()
    os.mkdir(WORK)
    for name, fn in (("pins", t_pins), ("binder", t_binder), ("items", t_items), ("go", t_go),
                     ("admission", t_admission), ("filter", t_filter), ("threads", t_collector_writer_feeder),
                     ("pipeline_controls", t_pipeline_controls), ("pipeline_failures", t_pipeline_failures),
                     ("evaluate", t_evaluate), ("monitor", t_monitor), ("gate", t_gate), ("static", t_static),
                     ("cli", t_cli)):
        run(name, fn)
    fails = [r["check"] for r in RESULTS if not r["ok"]]
    out = {"schema": "moqls8-gb-staged-selfcheck/1", "started_at": started, "finished_at": m.now(),
           "runtime": {"path": TARGET, "sha256": RT_SHA, "bytes": len(RT_BYTES)},
           "selfcheck": {"path": os.path.realpath(__file__),
                         "sha256": hashlib.sha256(open(os.path.realpath(__file__), "rb").read()).hexdigest()},
           "python": {"executable": sys.executable, "realpath": os.path.realpath(sys.executable),
                      "version": sys.version.split()[0], "isolated": sys.flags.isolated,
                      "dont_write_bytecode": sys.dont_write_bytecode},
           "work_dir": WORK,
           "native_processes_started": "none: kissat and drat-trim replaced by python -I -B -c stubs through a "
                                       "subprocess shim; ps/lsof helpers replaced by fakes (run_helper checked with a "
                                       "python sleeper); no n=8 generation (only the binder's n=5 storage control)",
           "checks": RESULTS, "failed": fails, "status": "PASS" if not fails else "FAIL"}
    with open(OUT, "x") as f:
        json.dump(out, f, indent=1, default=str)
        f.write("\n")
    print("SELFCHECK %s %d/%d checks, sha256 %s" % (out["status"], len(RESULTS) - len(fails), len(RESULTS),
                                                     hashlib.sha256(open(OUT, "rb").read()).hexdigest()))
    return 0 if not fails else 2


if __name__ == "__main__":
    sys.exit(main())
