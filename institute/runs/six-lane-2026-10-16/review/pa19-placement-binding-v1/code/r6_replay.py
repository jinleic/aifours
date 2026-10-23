#!/usr/bin/env python3
"""R6 parent replay driver: regenerate the placement-split lists with the pinned lane enumerators,
bind each list to its skeleton, and check them with the parent's independent semantics (r6_indep).

Per hard split case (31 ms01 A3 + 43 ms09 A3', from the pinned tag lists) and its M2 b-index
(compare-map a_to_b):
  M1  production command semantics, pinned code from S:
        ms01: extend_p1.py SPEC OUT            (run_hard4 a3; m = ns = 1)
        ms09: extend_p1q.py SPEC OUT 1         (run_hard5..8 part; m = 1)
  M2  extend_b.py SKEL_B INDEX OUT             (run_m2partbatch5)
  OUT is an anonymous pipe (/dev/fd/N); the regenerated JSON is hashed and compared in memory and
  never written to disk. Stored lists are read once from the live lane (read-only), hashed, and
  compared byte-for-byte; M2 bytes are compared after substituting the production `source` path.
Independent checks: row frames, explicit A->B skeleton isomorphisms, count vectors enumerated
block-wise, orbits by union-find and by Burnside, row-level validity of every placement, orbit
bijection of every list, M1->M2 transport bijection, row-level labeled controls.
Limits: one child at a time under nice; 1800 s wall and 3 GiB RSS per enumeration (SIGTERM and a
bounded wait only); host-clock heartbeat every 300 s; cooperative stop via OUT/STOP or SIGTERM.
Usage (research venv): python -B r6_replay.py RUN_ID [MAX_WALL_S] [TAG ...]
"""
import hashlib
import importlib.util
import json
import os
import signal
import subprocess
import sys
import threading
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import r6_indep as I  # noqa: E402

S = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-parent-cover-replay-v1/inputs"
L = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
VENV_PY = "/Users/jinleic/.local/state/research-explorer/venv/bin/python"
PIN = os.path.join(OUT, "pin-v1.json")
CASES = os.path.join(OUT, "cases")
LOGS = os.path.join(OUT, "logs")
STOPFILE = os.path.join(OUT, "STOP")
WALL_LIMIT_S = 1800
RSS_LIMIT_KB = 3 * 1024 * 1024
TERM_WAIT_S = 120
DISK_FLOOR = 12_000_000_000
HEARTBEAT_S = 300
MIN_AGE_S = 30
SRC_USED = ["extend_p1.py", "extend_p1q.py", "extend_b.py", "encode_skel.py", "encode_e1.py"]
P0 = [4, 3, 3, 3, 3, 3]
P1 = [4, 4, 3, 3, 3, 2]

STOP = {"flag": False}


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fsha(path):
    with open(path, "rb") as f:
        return sha(f.read())


def free_bytes():
    st = os.statvfs(L)
    return st.f_bavail * st.f_frsize


def write_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=1)


class Log:
    def __init__(self, path):
        self.f = open(path, "x", buffering=1)

    def __call__(self, *a):
        line = now() + " " + " ".join(str(x) for x in a)
        self.f.write(line + "\n")
        print(line, flush=True)


def stop_requested():
    return STOP["flag"] or os.path.exists(STOPFILE)


def read_stable(path):
    """Read a live file once: wait until it is >= MIN_AGE_S old, require identical stat before and
    after the read and a complete JSON parse. Returns (meta, bytes, obj)."""
    if not os.path.isfile(path):
        return {"status": "absent", "path": path, "checked_at": now()}, None, None
    for _ in range(3):
        st1 = os.stat(path)
        age = time.time() - st1.st_mtime
        if age < MIN_AGE_S:
            time.sleep(MIN_AGE_S - age + 1)
            continue
        with open(path, "rb") as f:
            b = f.read()
        st2 = os.stat(path)
        meta = {"path": path, "read_at": now(), "size": len(b), "sha256": sha(b),
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st1.st_mtime)),
                "mtime_ns": st1.st_mtime_ns}
        if (st1.st_size, st1.st_mtime_ns) != (st2.st_size, st2.st_mtime_ns) or len(b) != st1.st_size:
            time.sleep(MIN_AGE_S)
            continue
        try:
            obj = json.loads(b)
        except ValueError:
            meta["status"] = "unparseable"
            return meta, None, None
        meta["status"] = "read"
        return meta, b, obj
    return {"status": "unstable", "path": path, "checked_at": now()}, None, None


def run_capture(argv_of_out, log, label):
    """Run one enumerator with its OUT argument bound to a pipe; never touches the disk."""
    r, w = os.pipe()
    argv = argv_of_out("/dev/fd/%d" % w)
    cmd = ["/usr/bin/nice", "-n", "10"] + argv
    t0 = time.time()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, pass_fds=(w,), close_fds=True,
                            env=env, cwd=OUT)
    os.close(w)
    chunks = []
    h = hashlib.sha256()
    outs = {}

    def rd_main():
        with os.fdopen(r, "rb") as f:
            for b in iter(lambda: f.read(1 << 16), b""):
                chunks.append(b)
                h.update(b)

    def rd(name, f):
        outs[name] = f.read()

    ths = [threading.Thread(target=rd_main), threading.Thread(target=rd, args=("stdout", proc.stdout)),
           threading.Thread(target=rd, args=("stderr", proc.stderr))]
    for th in ths:
        th.start()
    peak_kb = 0
    reason = None
    term_at = None
    last_hb = t0
    status = rusage = None
    while True:
        pid, st, ru = os.wait4(proc.pid, os.WNOHANG)
        if pid == proc.pid:
            status, rusage = st, ru
            break
        el = time.time() - t0
        o = subprocess.run(["/bin/ps", "-o", "rss=", "-p", str(proc.pid)], capture_output=True, text=True).stdout.strip()
        if o.isdigit():
            peak_kb = max(peak_kb, int(o))
        if reason is None:
            if el > WALL_LIMIT_S:
                reason = "wall_limit_%ds" % WALL_LIMIT_S
            elif peak_kb > RSS_LIMIT_KB:
                reason = "rss_limit_%dkB" % RSS_LIMIT_KB
            elif stop_requested():
                reason = "driver_stop"
            if reason:
                log(label, "SIGTERM child pid", proc.pid, "reason", reason, "elapsed", round(el, 1))
                proc.send_signal(signal.SIGTERM)
                term_at = time.time()
        elif time.time() - term_at > TERM_WAIT_S:
            log(label, "child pid", proc.pid, "still alive %ds after SIGTERM; driver exits without SIGKILL" % TERM_WAIT_S)
            raise SystemExit(3)
        if time.time() - last_hb >= HEARTBEAT_S:
            log(label, "heartbeat elapsed", round(el, 1), "rss_kB", o, "peak_kB", peak_kb)
            last_hb = time.time()
        time.sleep(1.0)
    proc.returncode = os.waitstatus_to_exitcode(status)
    for th in ths:
        th.join()
    data = b"".join(chunks)
    meta = {"argv": argv, "out_arg": "anonymous pipe /dev/fd/%d (not stored)" % w, "nice": 10,
            "returncode": proc.returncode, "elapsed_s": round(time.time() - t0, 3),
            "ru_maxrss_bytes": rusage.ru_maxrss, "ru_utime_s": round(rusage.ru_utime, 3),
            "ru_stime_s": round(rusage.ru_stime, 3), "ps_peak_rss_kB": peak_kb, "limit_reason": reason,
            "out_bytes": len(data), "out_sha256": h.hexdigest(),
            "stdout": outs.get("stdout", b"").decode(errors="replace")[-2000:],
            "stderr_tail": outs.get("stderr", b"").decode(errors="replace")[-2000:]}
    meta["completed"] = proc.returncode == 0 and reason is None
    return meta, data


def load_pinned_rows_of():
    src = os.path.join(S, "src")
    sys.path.insert(0, src)
    try:
        spec = importlib.util.spec_from_file_location("pinned_encode_skel", os.path.join(src, "encode_skel.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path.remove(src)
    return mod.rows_of


def check_sources(pin):
    out = {}
    for f in SRC_USED:
        s = fsha(os.path.join(S, "src", f))
        lp = os.path.join(L, "src", f)
        lv = fsha(lp) if os.path.isfile(lp) else None
        out[f] = {"S_sha256": s, "L_sha256": lv, "S_matches_pin": s == pin["sources"][f]["S"]["sha256"],
                  "L_matches_pin": lv == pin["sources"][f]["L"]["sha256"]}
    return out


def list_diff(a, b):
    """Full semantic difference between two placement lists (JSON-normalized entries)."""
    ja = [json.dumps(x) for x in a]
    jb = [json.dumps(x) for x in b]
    sa, sb = set(ja), set(jb)
    first = next((i for i, (x, y) in enumerate(zip(ja, jb)) if x != y), None)
    return {"len": [len(a), len(b)], "ordered_equal": ja == jb, "set_equal": sa == sb,
            "first_order_difference_index": first, "only_in_first": sorted(sa - sb), "only_in_second": sorted(sb - sa),
            "duplicates_first": len(ja) - len(sa), "duplicates_second": len(jb) - len(sb)}


def m1_entries(obj):
    bad = [i for i, pl in enumerate(obj["full"]) if not (isinstance(pl, list) and len(pl) == 1 and len(pl[0]) == 3)]
    return [tuple(pl[0]) for pl in obj["full"] if isinstance(pl, list) and len(pl) == 1], bad


def m2_entries(obj):
    bad = [i for i, pl in enumerate(obj["placements"]) if not (isinstance(pl, list) and len(pl) == 3)]
    return [tuple(pl) for pl in obj["placements"]], bad


class Ctx:
    pass


def setup():
    C = Ctx()
    C.pin = json.load(open(PIN))
    C.pin_sha256 = fsha(PIN)
    C.skl = {mi: json.load(open(os.path.join(S, "skeletons", "skeletons-ms%02d.json" % mi))) for mi in (1, 9)}
    C.skb = {mi: json.load(open(os.path.join(S, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi))) for mi in (1, 9)}
    C.rows_of = load_pinned_rows_of()
    return C


def process_case(C, c, run_id, log):
    tag, mi, si, bi = c["tag"], c["multiset"], c["skel_index"], c["b_index"]
    rec = {"tag": tag, "multiset": mi, "skel_index": si, "b_index": bi, "run_id": run_id, "started": now(),
           "driver_sha256": fsha(os.path.abspath(__file__)), "indep_sha256": fsha(os.path.join(HERE, "r6_indep.py")),
           "pin_sha256": C.pin_sha256}
    srcchk = check_sources(C.pin)
    rec["source_check"] = srcchk
    if not all(v["S_matches_pin"] for v in srcchk.values()):
        raise SystemExit("pinned S source changed: %s" % srcchk)
    rec["live_source_drift"] = [f for f, v in srcchk.items() if not v["L_matches_pin"]]

    # ---- spec and skeleton binding
    sp_S = os.path.join(S, "cases19skel", "specs", tag + ".json")
    sp_L = os.path.join(L, "cases19skel", "specs", tag + ".json")
    bS = open(sp_S, "rb").read()
    bL = open(sp_L, "rb").read() if os.path.isfile(sp_L) else None
    spec = json.loads(bS)
    K = C.skl[mi]
    D = C.skb[mi]
    c0, Lv, N = spec["c0"], spec["L"], spec["N"]
    ns = len(spec["special"])
    left = ns - 1
    rec["spec"] = {"S_sha256": sha(bS), "L_sha256": sha(bL) if bL else None,
                   "pin_S_sha256": c["spec"]["S"]["sha256"]}
    rec["spec_binding"] = {
        "S_equals_L": bL == bS, "S_equals_pin": sha(bS) == c["spec"]["S"]["sha256"],
        "kind_N_k_q": [spec.get("kind"), spec.get("N"), spec.get("k"), spec.get("q")] == ["skel", 19, 8, 6],
        "indices": [spec["multiset_index"], spec["skel_index"]] == [mi, si],
        "skeleton_equals_list_entry": spec["skeleton"] == K["skeletons"][si],
        "c0_L_special_equal_list": [c0, Lv, spec["special"]] == [K["c0"], K["L"], K["special"]],
        "all_special_P1": all(list(p) == P1 for p in spec["special"]),
        "ns": ns,
        "m2_header_matches": [D["c0"], D["L"], sorted(map(tuple, D["profiles"]))] ==
                             [c0, Lv, sorted([tuple(P0)] * c0 + [tuple(p) for p in spec["special"]])],
    }
    rec["spec_binding"]["ok"] = all(v for k, v in rec["spec_binding"].items() if k != "ns")

    # ---- stored lists (read once from the live lane)
    m1sub = "a3" if mi == 1 else "part"
    m1_meta, m1_bytes, m1_obj = read_stable(os.path.join(L, "cycle2", m1sub, tag, "ext.json"))
    s_copy = os.path.join(S, "cycle2", m1sub, tag, "ext.json")
    m1_meta["S_copy_sha256"] = fsha(s_copy) if os.path.isfile(s_copy) else None
    m1_meta["pin_L_sha256"] = c["m1_ext"]["L"].get("sha256")
    rec["m1_stored"] = m1_meta
    m2name = "ms%02d_b%05d" % (mi, bi)
    m2_meta, m2_bytes, m2_obj = read_stable(os.path.join(L, "cycle2", "m2part_drat", m2name, "ext.json"))
    m2_meta["pin_sha256"] = c["m2_ext_m2part_drat"].get("sha256")
    legacy = os.path.join(L, "cycle2", "m2part", m2name, "ext.json")
    m2_meta["legacy_m2part_exists"] = os.path.isfile(legacy)
    rec["m2_stored"] = m2_meta

    # ---- M1 regeneration
    if free_bytes() < DISK_FLOOR:
        log(tag, "disk floor reached before M1; stopping", free_bytes())
        return None
    script = "extend_p1.py" if mi == 1 else "extend_p1q.py"
    extra = [] if mi == 1 else ["1"]
    log(tag, "M1 start", script, "stored", m1_meta["status"])
    r1, b1 = run_capture(lambda o: [VENV_PY, "-B", os.path.join(S, "src", script), sp_S, o] + extra, log, tag + " M1")
    log(tag, "M1 end", r1["returncode"], r1["elapsed_s"], "s maxrss", r1["ru_maxrss_bytes"], "limit", r1["limit_reason"])
    if r1["limit_reason"] == "driver_stop":
        return None
    o1 = None
    if r1["completed"]:
        o1 = json.loads(b1)
        r1["summary"] = {k: o1.get(k) for k in ("source", "raw", "num_full")}
        r1["keys"] = list(o1.keys())
        if m1_obj is not None:
            r1["bytes_equal_stored"] = b1 == m1_bytes
            if b1 != m1_bytes:
                r1["diff_vs_stored"] = {"keys": [list(m1_obj.keys()), list(o1.keys())],
                                        "fields": {k: [m1_obj.get(k), o1.get(k)] for k in ("source", "raw", "num_full")},
                                        "full": list_diff(m1_obj.get("full", []), o1.get("full", []))}
    write_x(os.path.join(CASES, "%s.m1.%s.json" % (tag, run_id)), {"tag": tag, "at": now(), "m1_regen": r1,
                                                                   "m1_stored": m1_meta})
    rec["m1_regen"] = r1

    # ---- M2 regeneration
    if free_bytes() < DISK_FLOOR:
        log(tag, "disk floor reached before M2; stopping", free_bytes())
        return None
    skp = os.path.join(S, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi)
    prod_source = os.path.join(L, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi)
    log(tag, "M2 start", m2name, "stored", m2_meta["status"])
    r2, b2 = run_capture(lambda o: [VENV_PY, "-B", os.path.join(S, "src", "extend_b.py"), skp, str(bi), o], log,
                         tag + " M2")
    log(tag, "M2 end", r2["returncode"], r2["elapsed_s"], "s maxrss", r2["ru_maxrss_bytes"], "limit", r2["limit_reason"])
    if r2["limit_reason"] == "driver_stop":
        return None
    o2 = None
    if r2["completed"]:
        o2 = json.loads(b2)
        r2["summary"] = {k: o2.get(k) for k in ("source", "index", "raw_class_assignments", "automorphisms",
                                                 "num_placements")}
        r2["keys"] = list(o2.keys())
        r2["reserialization_exact"] = json.dumps(o2).encode() == b2
        r2["source_is_S_path"] = o2.get("source") == skp
        norm = dict(o2)
        norm["source"] = prod_source
        nb = json.dumps(norm).encode()
        r2["production_source_string"] = prod_source
        r2["normalized_sha256"] = sha(nb)
        r2["normalized_bytes"] = len(nb)
        if m2_obj is not None:
            r2["stored_source_equals_production_string"] = m2_obj.get("source") == prod_source
            r2["normalized_bytes_equal_stored"] = nb == m2_bytes
            if nb != m2_bytes:
                r2["diff_vs_stored"] = {"keys": [list(m2_obj.keys()), list(o2.keys())],
                                        "fields": {k: [m2_obj.get(k), o2.get(k)] for k in
                                                   ("source", "index", "raw_class_assignments", "automorphisms",
                                                    "num_placements")},
                                        "placements": list_diff(m2_obj.get("placements", []),
                                                                o2.get("placements", []))}
    write_x(os.path.join(CASES, "%s.m2.%s.json" % (tag, run_id)), {"tag": tag, "at": now(), "m2_regen": r2,
                                                                   "m2_stored": m2_meta})
    rec["m2_regen"] = r2

    # ---- independent semantics
    t0 = time.time()
    ind = {}
    rows_a = I.m1_rows(c0, spec["skeleton"], N)
    sk = D["skeletons"][bi]
    rows_b = I.m2_rows(D["c0"], sk["types"], sk["empty"], N)
    ind["rows_a_equal_pinned_rows_of"] = [frozenset(t) for t in C.rows_of(c0, spec["skeleton"], N)] == rows_a
    ind["skeleton_sanity_a"] = I.skeleton_sanity(c0, rows_a)
    ind["skeleton_sanity_b"] = I.skeleton_sanity(c0, rows_b)
    isos = I.isomorphisms(c0, rows_a, rows_b)
    auts_a = I.automorphisms(c0, rows_a)
    auts_b = I.automorphisms(c0, rows_b)
    ind["isomorphisms"] = len(isos)
    ind["iso_first"] = list(isos[0]) if isos else None
    ind["aut_a"] = len(auts_a)
    ind["aut_b"] = len(auts_b)
    Xa, prod_a = I.count_vectors(rows_a, Lv, left)
    Xb, prod_b = I.count_vectors(rows_b, D["L"], left)
    ind["X_a"] = len(Xa)
    ind["X_b"] = len(Xb)
    ind["X_no_double_production"] = prod_a == len(Xa) and prod_b == len(Xb)
    ind["X_transport_equal_first_iso"] = bool(isos) and {I.transport(isos[0], v) for v in Xa} == Xb
    ind["X_transport_equal_last_iso"] = bool(isos) and {I.transport(isos[-1], v) for v in Xa} == Xb
    gens_a = I.generating_set(auts_a, c0)
    gens_b = I.generating_set(auts_b, c0)
    comp_a, norb_a = I.orbit_components(Xa, gens_a)
    comp_b, norb_b = I.orbit_components(Xb, gens_b)
    ind["orbits_a_unionfind"] = norb_a
    ind["orbits_b_unionfind"] = norb_b
    ba, bb = I.burnside(Xa, auts_a), I.burnside(Xb, auts_b)
    ind["orbits_a_burnside"] = str(ba)
    ind["orbits_b_burnside"] = str(bb)
    ind["burnside_equals_unionfind"] = ba == norb_a and bb == norb_b
    bad_real = [sorted((sorted(t), cc) for t, cc in v) for v in Xa
                if I.row_errors(rows_a, Lv, left, *I.realize(rows_a, v))]
    ind["X_a_realizable_all"] = not bad_real
    ind["X_a_unrealizable"] = bad_real[:20]
    # row-level labeled controls (no count-vector reduction in the enumeration)
    ctl = {}
    if mi == 1:
        n_lab, n_within, n_full, vecs = I.row_level_orbits(rows_a, Lv, left, auts_a)
        ctl = {"kind": "row-level labeled enumeration + union-find orbits (within-type transpositions, lifted "
                       "automorphisms, A/B swap)", "labeled": n_lab, "orbits_within_type": n_within,
               "orbits_full": n_full, "count_vectors_equal_X_a": vecs == Xa,
               "weight_sum_X_a": I.weight_sum(Xa, rows_a)}
        ctl["ok"] = (n_within == len(Xa) and n_full == norb_a and vecs == Xa and ctl["weight_sum_X_a"] == n_lab)
    else:
        n_lab = I.row_level_count(rows_a, Lv, left)
        ctl = {"kind": "row-level labeled count vs sum over X_a of multinomial weights (with X_a realizable this "
                       "forces X_a = all realizable count vectors)", "labeled": n_lab,
               "weight_sum_X_a": I.weight_sum(Xa, rows_a)}
        ctl["ok"] = n_lab == ctl["weight_sum_X_a"] and not bad_real
    ind["row_level_control"] = ctl

    # list checks
    lists = {}
    m1_lists = []
    if m1_obj is not None:
        m1_lists.append(("m1_stored", m1_obj))
    if o1 is not None and (m1_obj is None or b1 != m1_bytes):
        m1_lists.append(("m1_regen", o1))
    m1_comp = None
    for name, obj in m1_lists:
        ents, badfmt = m1_entries(obj)
        res, comp_of = I.check_list(rows_a, Lv, left, Xa, comp_a, norb_a, ents)
        res["format_errors"] = badfmt
        res["raw_equals_X"] = obj.get("raw") == len(Xa)
        res["num_full_equals_len"] = obj.get("num_full") == len(obj.get("full", []))
        res["num_full_equals_orbits"] = obj.get("num_full") == norb_a
        res["source_field_ok"] = obj.get("source") == tag + ".json"
        res["ordered_payload_sha256"] = sha(json.dumps(obj.get("full")).encode())
        lists[name] = res
        if m1_comp is None:
            m1_comp = (name, ents)
    m2_lists = []
    if o2 is not None:
        m2_lists.append(("m2_regen", o2))
    if m2_obj is not None and (o2 is None or not r2.get("normalized_bytes_equal_stored")):
        m2_lists.append(("m2_stored", m2_obj))
    m2_ref = None
    for name, obj in m2_lists:
        ents, badfmt = m2_entries(obj)
        res, comp_of = I.check_list(rows_b, D["L"], left, Xb, comp_b, norb_b, ents)
        res["format_errors"] = badfmt
        res["raw_equals_X"] = obj.get("raw_class_assignments") == len(Xb)
        res["automorphisms_equal"] = obj.get("automorphisms") == len(auts_b)
        res["num_equals_len"] = obj.get("num_placements") == len(obj.get("placements", []))
        res["num_equals_orbits"] = obj.get("num_placements") == norb_b
        res["index_field_ok"] = obj.get("index") == bi
        res["ordered_payload_sha256"] = sha(json.dumps(obj.get("placements")).encode())
        lists[name] = res
        if m2_ref is None:
            m2_ref = (name, comp_of)
    ind["lists"] = lists
    # M1 -> M2 transport bijection
    tr = None
    if m1_comp is not None and m2_ref is not None and isos:
        comp_to_j = {}
        for j, cc in enumerate(m2_ref[1]):
            if cc is not None:
                comp_to_j.setdefault(cc, j)
        match = []
        for (A, B, P) in m1_comp[1]:
            if I.row_errors(rows_a, Lv, left, A, B, P):
                match.append(None)
                continue
            v = I.transport(isos[0], I.vec_of(rows_a, A, B, P))
            match.append(comp_to_j.get(comp_b.get(v)))
        tr = {"m1_list": m1_comp[0], "m2_list": m2_ref[0], "iso_used": list(isos[0]),
              "unmatched_m1_indices": [i for i, j in enumerate(match) if j is None],
              "m2_indices_hit_twice": sorted(j for j, k in Counter(x for x in match if x is not None).items() if k > 1),
              "matching_sha256": sha(json.dumps(match).encode())}
        tr["bijection"] = (not tr["unmatched_m1_indices"] and not tr["m2_indices_hit_twice"]
                           and len(match) == len(m2_ref[1]))
    ind["m1_to_m2_transport"] = tr
    ind["elapsed_s"] = round(time.time() - t0, 3)
    rec["independent"] = ind

    # ---- verdict for this case
    chk = {}
    chk["spec_binding"] = rec["spec_binding"]["ok"]
    chk["rows_of_equal"] = ind["rows_a_equal_pinned_rows_of"]
    chk["skeleton_sanity"] = ind["skeleton_sanity_a"]["ok"] and ind["skeleton_sanity_b"]["ok"]
    chk["a_to_b_isomorphism_exists"] = ind["isomorphisms"] > 0
    chk["iso_count_equals_aut"] = ind["isomorphisms"] == ind["aut_a"] == ind["aut_b"]
    chk["X_transport_equal"] = ind["X_transport_equal_first_iso"] and ind["X_transport_equal_last_iso"]
    chk["X_well_formed"] = ind["X_no_double_production"] and ind["X_a_realizable_all"]
    chk["burnside_equals_unionfind"] = ind["burnside_equals_unionfind"]
    chk["orbits_equal_ab"] = norb_a == norb_b and len(Xa) == len(Xb)
    chk["row_level_control"] = ctl["ok"]
    for name, res in lists.items():
        keys = [k for k in res if k.endswith("_ok") or k.endswith("_equal") or k.startswith("num_")
                or k == "raw_equals_X" or k == "bijective_with_orbits"]
        chk[name + "_semantics"] = all(res[k] for k in keys) and not res["format_errors"]
    if tr is not None:
        chk["m1_m2_transport_bijection"] = tr["bijection"]
    if m1_obj is not None and r1["completed"]:
        chk["m1_regen_bytes_equal_stored"] = r1["bytes_equal_stored"]
    if m2_obj is not None and r2["completed"]:
        chk["m2_regen_normalized_bytes_equal_stored"] = r2["normalized_bytes_equal_stored"]
    if m1_obj is not None and m1_meta.get("S_copy_sha256"):
        chk["m1_live_equals_S_copy"] = m1_meta["S_copy_sha256"] == m1_meta["sha256"]
    if o1 is not None:
        chk["m1_regen_counts_equal_indep"] = [o1["raw"], o1["num_full"]] == [len(Xa), norb_a]
    if o2 is not None:
        chk["m2_regen_counts_equal_indep"] = [o2["raw_class_assignments"], o2["automorphisms"],
                                             o2["num_placements"]] == [len(Xb), len(auts_b), norb_b]
    if o1 is not None and o2 is not None:
        chk["m1_m2_regen_counts_equal"] = [o1["raw"], o1["num_full"]] == [o2["raw_class_assignments"],
                                                                         o2["num_placements"]]
    rec["checks"] = chk
    unknown = [n for n, r in (("M1", r1), ("M2", r2)) if not r["completed"]]
    if unknown:
        status = "UNKNOWN_ENUMERATION_" + "_".join(unknown)
    elif not all(chk.values()):
        status = "MISMATCH"
    else:
        status = "REPLAYED_MATCH"
    rec["status"] = status
    rec["m1_binding"] = ("STORED_REPLAYED_BYTE_EQUAL" if m1_obj is not None and r1.get("bytes_equal_stored") else
                         "STORED_DIFFERS" if m1_obj is not None else
                         "STORED_%s_PREDICTED_ONLY" % m1_meta["status"].upper())
    rec["m2_binding"] = ("STORED_REPLAYED_BYTE_EQUAL_AFTER_SOURCE_PATH" if m2_obj is not None and
                         r2.get("normalized_bytes_equal_stored") else
                         "STORED_DIFFERS" if m2_obj is not None else
                         "STORED_%s_PARENT_GENERATED_COUNT_ONLY" % m2_meta["status"].upper())
    rec["counts"] = {"m1_raw": o1["raw"] if o1 else (m1_obj or {}).get("raw"),
                     "m1_num_full": o1["num_full"] if o1 else (m1_obj or {}).get("num_full"),
                     "m2_raw": o2["raw_class_assignments"] if o2 else None,
                     "m2_aut": o2["automorphisms"] if o2 else None,
                     "m2_num": o2["num_placements"] if o2 else None,
                     "indep_X": len(Xa), "indep_orbits": norb_a, "indep_aut": len(auts_a)}
    rec["shas"] = {"spec_S": sha(bS), "m1_stored": m1_meta.get("sha256"), "m1_regen": r1.get("out_sha256"),
                   "m2_stored": m2_meta.get("sha256"), "m2_regen_raw_S_source": r2.get("out_sha256"),
                   "m2_regen_normalized_production_source": r2.get("normalized_sha256"),
                   "skel_b_entry": sha(json.dumps(sk, sort_keys=True).encode()),
                   "spec_skeleton_entry": sha(json.dumps(spec["skeleton"], sort_keys=True).encode())}
    rec["finished"] = now()
    write_x(os.path.join(CASES, tag + ".json"), rec)
    log(tag, "CASE", status, "m1", rec["m1_binding"], "m2", rec["m2_binding"], json.dumps(rec["counts"]),
        "indep_s", ind["elapsed_s"])
    return rec


def main():
    run_id = sys.argv[1]
    max_wall = float(sys.argv[2]) if len(sys.argv) > 2 else 10200.0
    only = sys.argv[3:]
    os.makedirs(CASES, exist_ok=True)
    os.makedirs(LOGS, exist_ok=True)
    log = Log(os.path.join(LOGS, "run-%s.log" % run_id))
    signal.signal(signal.SIGTERM, lambda *a: STOP.__setitem__("flag", True))
    C = setup()
    t_start = time.time()
    log("start run", run_id, "max_wall_s", max_wall, "pin", C.pin_sha256, "driver", fsha(os.path.abspath(__file__)),
        "free_bytes", free_bytes())
    done, results = [], {}
    for c in C.pin["cases"]:
        tag = c["tag"]
        if only and tag not in only:
            continue
        if os.path.exists(os.path.join(CASES, tag + ".json")):
            continue
        if stop_requested():
            log("stop requested before", tag)
            break
        if time.time() - t_start > max_wall:
            log("max wall reached before", tag)
            break
        rec = process_case(C, c, run_id, log)
        if rec is None:
            log("stopped inside", tag, "(no case file written)")
            break
        done.append(tag)
        results[tag] = rec["status"]
    rescan = {}
    for c in C.pin["cases"]:
        tag, mi, bi = c["tag"], c["multiset"], c["b_index"]
        m1sub = "a3" if mi == 1 else "part"
        for key, p in (("m1", os.path.join(L, "cycle2", m1sub, tag, "ext.json")),
                       ("m2", os.path.join(L, "cycle2", "m2part_drat", "ms%02d_b%05d" % (mi, bi), "ext.json"))):
            rescan["%s:%s" % (tag, key)] = fsha(p) if os.path.isfile(p) else None
    end = {"run_id": run_id, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t_start)),
           "ended": now(), "processed": done, "statuses": results, "stop_requested": stop_requested(),
           "end_rescan_sha256": rescan, "free_bytes": free_bytes()}
    write_x(os.path.join(LOGS, "run-%s-end.json" % run_id), end)
    log("end run", run_id, "processed", len(done))


if __name__ == "__main__":
    main()
