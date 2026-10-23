#!/usr/bin/env python3
"""Frozen-plan interpreter for the sun6-second-checker-v1 intended-reason controls.

NOT RUN. Execute only after parent source review and an item GO.  Standard library only.
Executes exactly the hashed checker bytes, reads the pinned inputs read-only, keeps every
mutation in memory, and writes only inside a new --out-dir (exclusive creation, no deletion).
Exit: 0 all controls MATCH; 1 some MISMATCH/ERROR; 2 stopped (deadline/signal); 3 setup rejected.
"""

import argparse
import copy
import gzip
import hashlib
import json
import os
import signal
import sys
import time
import types

CHECKER_SHA256 = "1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f"
PLAN_SHA256 = "42cd627528121b3a26ce886514b4cc24b0ec33ac83ee8f75fe11768b4563b01b"
HERE = os.path.dirname(os.path.abspath(__file__))


class SetupError(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_checker(path):
    with open(path, "rb") as f:
        data = f.read()
    if sha(data) != CHECKER_SHA256:
        raise SetupError("checker sha256 mismatch")
    mod = types.ModuleType("sun6_second_checker_v1")
    mod.__file__ = path
    exec(compile(data, path, "exec"), mod.__dict__)
    return mod


class Env:
    def __init__(self, ck, input_dir, deadline_ns, out_dir):
        self.ck = ck
        self.deadline_ns = deadline_ns
        self.out_dir = out_dir
        self.blobs = ck.read_inputs(input_dir)
        for name in ck.INPUT_NAMES:
            b = self.blobs.get(name)
            size, h = ck.INPUT_PINS[name]
            if type(b) is not bytes or len(b) != size or sha(b) != h:
                raise SetupError("input pin mismatch: " + name)
        self.plain = gzip.decompress(self.blobs["orbits.jsonl.gz"])
        if (len(self.plain), sha(self.plain)) != tuple(ck.ORBITS_PLAIN_PIN):
            raise SetupError("decompressed pin mismatch")
        self.records = ck.parse_orbit_lines(self.plain)
        self.duals = ck.parse_duals(self.blobs["rlp_duals.json"])
        self._leaves = {}

    def guard(self):
        return self.ck.Guard(self.deadline_ns)

    def leaves(self, tp):
        if tp not in self._leaves:
            self._leaves[tp] = self.ck.enumerate_leaves(self.ck.Status(tp), self.guard())[0]
        return self._leaves[tp]


def tp_of(x):
    return tuple(x)


def rationals(ck, strs):
    t = tuple(ck.parse_rational(s) for s in strs)
    if any(v is None for v in t):
        raise SetupError("non-rational string in plan")
    return t


def c_unit_tri(env, a, cid):
    ck = env.ck
    tmin, tmax = ck.tri_bounds(a["a_ij"], a["a_ik"], a["a_jk"], a["i"], a["j"], a["k"],
                               ck.Status(tp_of(a["type"])))
    return {"tau_min": tmin, "tau_max": tmax, "consistent": tmin <= tmax}


def c_unit_leaf(env, a, cid):
    ck = env.ck
    tp = tp_of(a["type"])
    out = {"t_consistent": ck.t_consistent(ck.matrix_from_code(a["code"]), ck.Status(tp))}
    if a.get("enumerate"):
        out["member"] = ck.lexkey_from_code(a["code"]) in env.leaves(tp)
    return out


def c_unit_stabilizer(env, a, cid):
    return {"size": len(env.ck.stabilizer(tp_of(a["type"])))}


def c_unit_orbit(env, a, cid):
    ck = env.ck
    getters = ck.lex_image_getters(ck.stabilizer(tp_of(a["type"])))
    return {"size": len(ck.orbit_of(ck.lexkey_from_code(a["rep"]), getters))}


def c_unit_placement(env, a, cid):
    r = env.ck.placement_reduction()
    return {"placements": r["placements"], "exactly_one": r["exactly_one"], "ok": r["ok"]}


def c_unit_dual(env, a, cid):
    ck = env.ck
    ctx = ck.RuleContext({}, env.guard())
    r = ck.dual_condition(tuple(a["q"]), tuple(tuple(s) for s in a["st5"]),
                          rationals(ck, a["y"]), ctx)
    return {"result": "VALID" if r is None else r[0]}


def c_unit_pbounds(env, a, cid):
    ck = env.ck
    lo, hi, u = ck.p_bounds(ck.matrix_from_code(a["rep"]), ck.Status(tp_of(a["type"])),
                            a["v"], a["j"], a["k"])
    return {"lo": str(lo), "hi": str(hi), "u": str(u)}


def c_unit_forced(env, a, cid):
    ck = env.ck
    A = ck.matrix_from_code(a["rep"])
    st = ck.Status(tp_of(a["type"]))
    N, st5, forced, amasks, _ylo, _yhi = ck.rplp_frame(A, st, a["v"])
    out = {"forced": sorted([N[x], N[y]] for (x, y) in forced), "admissible_A": len(amasks)}
    if "q" in a:
        ctx = ck.RuleContext({}, env.guard())
        allowed = set(ck.allowed_masks(tuple(a["q"]), st5, ctx))
        allowed.add(0)
        n = 0
        for am in amasks:
            sm = am
            while True:
                if sm in allowed:
                    n += 1
                if sm == 0:
                    break
                sm = (sm - 1) & am
        out["columns"] = n
    return out


def c_unit_fgcd(env, a, cid):
    ck = env.ck
    st = ck.Status(tp_of(a["type"]))
    ex = ck.fh5_exponents(st, a["x"], a["tx"], a["e5"])
    ey = ck.fh5_exponents(st, a["y"], a["ty"], a["e5"])
    return {"fgcd": ck.fgcd_value(ex, ey)}


def verify_outcome(env, tp, rep, rule, witness, duals):
    ck = env.ck
    ctx = ck.RuleContext(duals, env.guard())
    try:
        ck.verify_record(tp, rep, rule, witness, ctx)
        return {"status": "VERIFIED"}
    except ck.WitnessFail as exc:
        return {"status": "FAILED", "reason": exc.reason, "detail": exc.detail}


def c_record(env, a, cid):
    duals = {k: rationals(env.ck, ys) for k, ys in (a.get("duals") or {}).items()}
    return verify_outcome(env, tp_of(a["type"]), a["rep"], a["rule"], copy.deepcopy(a["witness"]),
                          duals)


def find_line(env, sel):
    tp = tp_of(sel["type"])
    hits = [r for r in env.records if r[1] == tp and r[2] == sel["rep"] and r[3] == sel["rule"]]
    if len(hits) != 1:
        raise SetupError("selector matched %d lines" % len(hits))
    return hits[0]


def nav(obj, path):
    for p in path:
        obj = obj[p]
    return obj


def c_record_data(env, a, cid):
    n, tp, rep, rule, wit = find_line(env, a["select"])
    w = copy.deepcopy(wit)
    duals = dict(env.duals)
    m = a["mutation"]
    op = m["op"]
    if op == "none":
        pass
    elif op == "duals_remove":
        if m["key"] not in duals:
            raise SetupError("dual key absent")
        del duals[m["key"]]
    elif op == "duals_replace":
        if m["key"] not in duals:
            raise SetupError("dual key absent")
        duals[m["key"]] = rationals(env.ck, m["y"])
    elif op == "witness_set":
        parent = nav(w, m["path"][:-1])
        idx = m["path"][-1]
        if type(parent) is not list or not 0 <= idx < len(parent):
            raise SetupError("bad witness path")
        parent[idx] = copy.deepcopy(m["value"])
    elif op == "witness_pop":
        lst = nav(w, m["path"])
        if type(lst) is not list or not lst:
            raise SetupError("bad witness path")
        lst.pop()
    elif op == "witness_swap":
        lst = nav(w, m["path"])
        lst[m["i"]], lst[m["j"]] = lst[m["j"]], lst[m["i"]]
    else:
        raise SetupError("unknown record_data op " + op)
    out = verify_outcome(env, tp, rep, rule, w, duals)
    out["line"] = n
    return out


def c_coverage(env, a, cid):
    ck = env.ck
    tp = tp_of(a["type"])
    items = [(r[0], ck.lexkey_from_code(r[2])) for r in env.records if r[1] == tp]
    m = a["mutation"]
    op = m["op"]
    if op == "none":
        pass
    elif op == "remove_rep":
        key = ck.lexkey_from_code(m["rep"])
        before = len(items)
        items = [it for it in items if it[1] != key]
        if len(items) != before - 1:
            raise SetupError("remove_rep did not remove exactly one line")
    elif op == "add_rep":
        items.append((10 ** 9, ck.lexkey_from_code(m["rep"])))
    elif op == "replace_rep":
        key = ck.lexkey_from_code(m["rep"])
        idx = [i for i, it in enumerate(items) if it[1] == key]
        if len(idx) != 1:
            raise SetupError("replace_rep selector")
        items[idx[0]] = (items[idx[0]][0], ck.lexkey_from_code(m["new_rep"]))
    else:
        raise SetupError("unknown coverage op " + op)
    cov = ck.check_coverage(items, env.leaves(tp), ck.lex_image_getters(ck.stabilizer(tp)),
                            env.guard())
    return {"clean": cov["clean"], "missing": cov["missing"], "missing_orbits": cov["missing_orbits"],
            "duplicates": len(cov["duplicate"]), "rep_not_leaf": len(cov["rep_not_leaf"]),
            "orbits_owned": cov["orbits_owned"], "covered": cov["covered"]}


def c_pipeline(env, a, cid):
    ck = env.ck
    blobs = dict(env.blobs)
    plain = env.plain
    m = a["mutation"]
    op = m["op"]
    plain_changed = False
    if op == "none":
        pass
    elif op == "flip_byte":
        b = bytearray(blobs[m["file"]])
        b[m["offset"]] ^= 0xFF
        blobs[m["file"]] = bytes(b)
    elif op == "append_bytes":
        blobs[m["file"]] = blobs[m["file"]] + m["text"].encode("ascii")
    elif op == "text_replace":
        old = m["old"].encode("ascii")
        b = blobs[m["file"]]
        if b.count(old) != 1:
            raise SetupError("text_replace anchor not unique")
        blobs[m["file"]] = b.replace(old, m["new"].encode("ascii"))
    elif op == "file_replace":
        blobs[m["file"]] = m["text"].encode("ascii")
    elif op == "plain_line_replace":
        lines = plain.split(b"\n")
        lines[m["line"] - 1] = m["text"].encode("ascii")
        plain = b"\n".join(lines)
        plain_changed = True
    elif op == "plain_strip_final_newline":
        if not plain.endswith(b"\n"):
            raise SetupError("no final newline to strip")
        plain = plain[:-1]
        plain_changed = True
    elif op == "plain_insert_empty_line":
        lines = plain.split(b"\n")
        lines.insert(m["after"], b"")
        plain = b"\n".join(lines)
        plain_changed = True
    else:
        raise SetupError("unknown pipeline op " + op)
    if plain_changed:
        blobs["orbits.jsonl.gz"] = gzip.compress(plain, compresslevel=9, mtime=0)
    rp = a["repin"]
    pins = None
    plain_pin = None
    if rp in ("all", "compressed_only"):
        pins = {n: (len(blobs[n]), sha(blobs[n])) for n in ck.INPUT_NAMES}
        if rp == "all":
            plain_pin = (len(plain), sha(plain))
    elif rp != "none":
        raise SetupError("unknown repin mode")
    g = a["guard"]
    mode = g["mode"]
    if mode == "far":
        guard = env.guard()
    elif mode == "past":
        guard = ck.Guard(0)
    elif mode == "cancel":
        guard = env.guard()
        guard.request_cancel("control")
    elif mode == "clock_after":
        calls = [0]
        limit = g["calls"]

        def clock():
            calls[0] += 1
            return 0 if calls[0] < limit else 2 ** 62

        guard = ck.Guard(10 ** 18, None, clock)
    else:
        raise SetupError("unknown guard mode")
    R = ck.run_check(blobs, guard, pins, plain_pin)
    W = R.get("witnesses") or {}
    return {"verdict": R["verdict"], "exit_code": R["exit_code"],
            "inputs_reject": (R["inputs"].get("reject") or {}).get("reason"),
            "parse_reject": ((R.get("parse") or {}).get("reject") or {}).get("reason"),
            "stop": R.get("stop"), "witnesses_verified": W.get("verified"),
            "witnesses_incomplete": W.get("incomplete")}


def c_publish(env, a, cid):
    ck = env.ck
    d = os.path.join(env.out_dir, "publish-" + cid)
    os.mkdir(d)
    pre = b"preexisting control bytes\n"
    rpath = os.path.join(d, "REPORT.json")
    spath = os.path.join(d, "REPORT.seal.json")
    if a["preexisting_report"]:
        ck.write_exclusive(rpath, pre)
    R = {"checker": ck.CHECKER_ID, "synthetic_control": cid, "verdict": a["verdict"],
         "exit_code": {"PASS": 0, "FAIL": 1, "INCOMPLETE": 2}[a["verdict"]]}
    guard = env.guard() if a["guard"] == "far" else ck.Guard(0)
    code = ck.publish(R, d, guard)
    out = {"exit_code": code, "seal": os.path.exists(spath)}
    with open(rpath, "rb") as f:
        body = f.read()
    if a["preexisting_report"]:
        out["preexisting_unchanged"] = (body == pre)
    else:
        out["report_verdict"] = json.loads(body.decode("ascii"))["verdict"]
        if out["seal"]:
            with open(spath, "rb") as f:
                seal = json.loads(f.read().decode("ascii"))
            out["seal_verdict"] = seal["verdict"]
            out["seal_hash_ok"] = (seal["report_sha256"] == sha(body))
    return out


RUNNERS = {"unit_tri": c_unit_tri, "unit_leaf": c_unit_leaf, "unit_stabilizer": c_unit_stabilizer,
           "unit_orbit": c_unit_orbit, "unit_placement": c_unit_placement, "unit_dual": c_unit_dual,
           "unit_pbounds": c_unit_pbounds, "unit_forced": c_unit_forced, "unit_fgcd": c_unit_fgcd,
           "record": c_record, "record_data": c_record_data, "coverage": c_coverage,
           "pipeline": c_pipeline, "publish": c_publish}


def write_result(out_dir, doc):
    body = (json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")
    path = os.path.join(out_dir, "CONTROLS-RESULT.json")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        view = memoryview(body)
        while len(view):
            n = os.write(fd, view)
            view = view[n:]
        os.fsync(fd)
    finally:
        os.close(fd)
    return sha(body)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="sun6-second-checker-v1-controls")
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--out-dir", required=True, help="must not exist; created exclusively")
    ap.add_argument("--deadline-epoch", required=True, type=int)
    ap.add_argument("--plan", default=os.path.join(os.path.dirname(HERE), "CONTROLS-PLAN-v1.json"))
    ap.add_argument("--checker", default=os.path.join(HERE, "sun6_second_checker_v1.py"))
    args = ap.parse_args(argv)
    flag = []

    def on_signal(signum, _frame):
        flag.append("signal-%d" % signum)

    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    try:
        os.mkdir(args.out_dir)
    except OSError as exc:
        sys.stderr.write("controls: out-dir not created exclusively: %s\n" % exc)
        return 3
    deadline_ns = args.deadline_epoch * 1000000000
    started = time.time_ns()
    doc = {"harness": "sun6-second-checker-v1-controls", "checker_sha256": CHECKER_SHA256,
           "plan_sha256": PLAN_SHA256, "started_ns": started, "python": sys.version}
    try:
        ck = load_checker(args.checker)
        with open(args.plan, "rb") as f:
            pb = f.read()
        if sha(pb) != PLAN_SHA256:
            raise SetupError("plan sha256 mismatch")
        plan = json.loads(pb.decode("ascii"))
        if plan["checker"]["sha256"] != CHECKER_SHA256:
            raise SetupError("plan names a different checker")
        env = Env(ck, args.input_dir, deadline_ns, args.out_dir)
    except Exception as exc:
        doc["setup_error"] = repr(exc)[:400]
        doc["exit_code"] = 3
        write_result(args.out_dir, doc)
        return 3
    results = []
    stopped = None
    for c in plan["controls"]:
        if stopped is None and flag:
            stopped = flag[0]
        if stopped is None and time.time_ns() >= deadline_ns:
            stopped = "DEADLINE"
        if stopped is not None:
            results.append({"id": c["id"], "status": "NOT_RUN", "reason": stopped})
            continue
        t0 = time.monotonic_ns()
        try:
            obs = RUNNERS[c["kind"]](env, c["args"], c["id"])
            match = all(k in obs and obs[k] == v for k, v in c["expect"].items())
            results.append({"id": c["id"], "kind": c["kind"],
                            "status": "MATCH" if match else "MISMATCH",
                            "expect": c["expect"], "observed": obs,
                            "elapsed_ns": time.monotonic_ns() - t0})
        except ck.StopRequested as exc:
            stopped = exc.reason
            results.append({"id": c["id"], "status": "STOPPED", "reason": exc.reason})
        except SetupError as exc:
            results.append({"id": c["id"], "status": "SETUP_ERROR", "detail": str(exc)[:300]})
        except Exception as exc:
            results.append({"id": c["id"], "status": "ERROR", "detail": repr(exc)[:300]})
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    doc["results"] = results
    doc["counts"] = counts
    doc["stopped"] = stopped
    doc["ended_ns"] = time.time_ns()
    if stopped is not None:
        code = 2
    elif counts.get("MATCH", 0) == len(plan["controls"]):
        code = 0
    else:
        code = 1
    doc["exit_code"] = code
    write_result(args.out_dir, doc)
    return code


if __name__ == "__main__":
    sys.exit(main())
