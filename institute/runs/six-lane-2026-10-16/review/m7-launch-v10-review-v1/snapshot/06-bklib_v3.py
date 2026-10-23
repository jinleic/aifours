#!/usr/bin/env python3
"""Library of the parent B-side K3 cube replay desk review/moqls7-k3-B-cube-parent-replay-v1, v3. Imports no lane code.

v3 = bklib_v2.py plus the B/C311+cuts item "B_C311cuts" (kind "cuts"). It is pinned from PhysEpQutrit's route-B r6
receipt evidence/k3cubes/C311cuts_B_r6/C311cuts_B.json (1f003634...c535): strengthened CNF ae3b8309...783a, input
explore/k3cubes/B_C311.cnf b3ec0108...c077 (metadata bfa298ee...a056), cut block 05f31da4...e6dd with 238,140
clauses. Three item-kind branches are needed for it:
  * regenerate() runs the item's composition script (compose_Bcuts_v1.py for cuts; compose_B_v1.py otherwise);
  * producer_evidence() checks a cuts receipt's own fields and flattens them into the cube-receipt field names used by
    the driver and the assembler;
  * check_regen() adds the input, block and output pin checks.
CODE_PINS also cover k3_lex.py and k3_cuts_r1.py. Items B_C321 and B_C411 are unchanged.

v2 = bklib_v1.py plus one change: ITEMS gains B_C411, pinned from PhysEpQutrit's r7 producer receipt
evidence/k3cubes/cert_B_r7/B_C411.json (644b5b23...6f75): CNF 01acf464...8bf8, base 42a5f304...0aac, metadata
explore/k3cubes/B_C411.meta.json c0f769bb...8a12, encoder B c7583efe...2b45, regeneration code da9c210e...ac78.

Design reused from the A-side desk review/moqls7-k3-cube-parent-replay-v1/scripts/k3lib_v1.py (read, not imported):
  * the CNF bytes stay in the driver's memory; kissat and drat-trim each read them through their own anonymous pipe,
    passed as /dev/fd/N; each feed is written by a measured writer thread that counts and SHA-256 hashes exactly the
    bytes accepted by os.write;
  * the binary DRAT proof goes kissat -> desk FIFO -> drat-trim stdin (-i). The FIFO read end is opened
    non-blocking (then made blocking) before any child starts, and the driver holds a write end until the solver has
    been reaped, so drat-trim never sees a premature EOF and no open() can block;
  * native limits bound the children (kissat --time, drat-trim -t). Safety stops are cooperative: SIGTERM to this
    driver's own children only, then a bounded wait; no SIGKILL, no Popen.kill, no subprocess timeouts. Children are
    reaped with os.wait4 (ru_maxrss in bytes on Darwin); aggregate RSS (driver plus live children) is sampled through
    libproc every 0.25 s;
  * a fresh statvfs gate (>= 12.2e9 + projected retained growth) immediately before each native Popen; logs are
    created O_EXCL|O_APPEND; status lines are parsed with only CR removed.
Differences from the A side: kissat replaces cadical; the CNF comes from the encoder-B composition driver
compose_B_v1.py; measured feeds; strict exact status-line lists; the native run is wrapped by the lane's validated
supervise_r3.py (launch_B_v1.py) and the run mode refuses to start unsupervised; a capacity scanner for the shared
phys-2 lane (lane_scan) used by the launcher.
Lane files are opened only after an lstat S_ISREG check: no FIFO or other special file outside this desk is opened.
"""
import ctypes
import datetime
import fcntl
import glob
import hashlib
import json
import os
import re
import signal
import stat
import struct
import subprocess
import threading
import time

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
CODE = os.path.join(LANE, "code")
K3DIR = os.path.join(LANE, "evidence", "k3cubes")
EXPLORE = os.path.join(LANE, "explore", "k3cubes")
KISSAT = "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"
DRAT = os.path.join(REVIEW, "moqls7-parent-proofcheck-v1", "drat-trim")
LANE_DRAT_SHA256 = "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4"   # never used here
PY = "/Library/Developer/CommandLineTools/usr/bin/python3"
SUPERVISOR = os.path.join(CODE, "supervise_r3.py")
SUPERVISOR_SHA256 = "0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d"
SCRIPTS = os.path.join(DESK, "scripts")
RECEIPTS = os.path.join(DESK, "receipts")
LOGS = os.path.join(DESK, "logs")
FIFO_DIR = os.path.join(DESK, "fifo")
TMP = os.path.join(DESK, "tmp")

GIB = 1 << 30
FLOOR = 12000000000                   # in-flight free-space floor: cooperative stop below it
LAUNCH_BASE = 12200000000             # admission gate base (parent rule)
PROJECTED_GROWTH = 1048576            # upper bound on this desk's remaining retained growth (logs, receipts, report)
GATE = LAUNCH_BASE + PROJECTED_GROWTH
LANE_RSS_LIMIT = 8 * GIB              # phys-2 lane total RSS limit
LANE_NATIVE_MAX = 4                   # phys-2 lane busy native processes limit
OTHER_NATIVE_MAX_AT_LAUNCH = 2        # launch only if a fresh scan shows at most this many busy lane natives
PROJECTED_PEAK = 2 * GIB              # this run's projected aggregate peak (producer B/C321 peak 1,629,880,320 B)
CAP_MAX = 3584 * 1024 * 1024          # never set this desk's RSS cap above the lane's standard 3.5 GiB stop
MIN_CAP = 2560 * 1024 * 1024          # refuse admission if the computable cap is below 2.5 GiB
UNSUPERVISED_GROUP_RESERVE = 3584 * 1024 * 1024   # reserve for an unsupervised lane native group (lane's 3.5 GiB stop)
OTHER_LANE_MARGIN = 256 * 1024 * 1024 # added to the current RSS of uncovered non-native lane processes
SAFETY_MARGIN = 128 * 1024 * 1024
GRACE = 120                           # bounded wait after SIGTERM to own children, seconds
PERIOD = 0.25
CHECKPOINT_EVERY = 600
ENV = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "TMPDIR": TMP + "/", "LC_ALL": "C",
       "PYTHONDONTWRITEBYTECODE": "1", "HOME": TMP}

CODE_PINS = {  # parent brief / producer receipt fields
    os.path.join(CODE, "gram_enc.py"): "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833",
    os.path.join(CODE, "k3_cubes.py"): "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550",
    os.path.join(CODE, "gram_encB.py"): "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
    SUPERVISOR: SUPERVISOR_SHA256,
    os.path.join(CODE, "k3_lex.py"): "2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10",
    os.path.join(CODE, "k3_cuts_r1.py"): "0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a",
}
BIN_PINS = {KISSAT: "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848",
            DRAT: "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"}
ORACLE_RECEIPT = os.path.join(K3DIR, "bmap_oracle_r1.json")
ITEMS = {
    "B_C321": {"encoder": "B", "cube": "C321",
               "producer_receipt": os.path.join(K3DIR, "cert_B_r6", "B_C321.json"),
               "producer_receipt_sha256": "2ffc2fa87d1c1882a067125b0f6bc5520b1e215946b5285052c0355755d832ac",
               "producer_checker_log": os.path.join(K3DIR, "cert_B_r6", "B_C321.checker.log"),
               "producer_solver_log": os.path.join(K3DIR, "cert_B_r6", "B_C321.solver.log"),
               "cnf_sha256": "8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6",
               "base_cnf_sha256": "42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac",
               "meta": os.path.join(EXPLORE, "B_C321.meta.json"),
               "meta_sha256": "79c91883e72e8604f791747dd15ae54c693528563e5770a63012600bc1bf6120",
               "encoder_sha256": "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
               "regen_code_sha256_prefix_suffix": ["da9c210e", "ac78"],
               "lane_cnf": os.path.join(EXPLORE, "B_C321.cnf")},
    "B_C411": {"encoder": "B", "cube": "C411",
               "producer_receipt": os.path.join(K3DIR, "cert_B_r7", "B_C411.json"),
               "producer_receipt_sha256": "644b5b23d98a55c44df88f15531644b9e8f825b790a9391791d0f50d082a6f75",
               "producer_checker_log": os.path.join(K3DIR, "cert_B_r7", "B_C411.checker.log"),
               "producer_solver_log": os.path.join(K3DIR, "cert_B_r7", "B_C411.solver.log"),
               "cnf_sha256": "01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8",
               "base_cnf_sha256": "42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac",
               "meta": os.path.join(EXPLORE, "B_C411.meta.json"),
               "meta_sha256": "c0f769bb56342c2fe78df4051fa15900f8d2de67eff0f41a2471990b2fb58a12",
               "encoder_sha256": "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
               "regen_code_sha256_prefix_suffix": ["da9c210e", "ac78"],
               "lane_cnf": os.path.join(EXPLORE, "B_C411.cnf")},
    "B_C311cuts": {"kind": "cuts", "encoder": "B", "cube": "C311", "compose": "compose_Bcuts_v1.py",
                   "producer_receipt": os.path.join(K3DIR, "C311cuts_B_r6", "C311cuts_B.json"),
                   "producer_receipt_sha256": "1f00363467d3ed30787cd1b3e4c2e695b8b4d7249623fc6e3994130f4be6c535",
                   "producer_checker_log": os.path.join(K3DIR, "C311cuts_B_r6", "C311cuts_B.checker.log"),
                   "producer_solver_log": os.path.join(K3DIR, "C311cuts_B_r6", "C311cuts_B.solver.log"),
                   "cnf_sha256": "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a",
                   "input_sha256": "b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077",
                   "block_sha256": "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd",
                   "block_clauses": 238140,
                   "base_cnf_sha256": "42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac",
                   "meta": os.path.join(EXPLORE, "B_C311.meta.json"),
                   "meta_sha256": "bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056",
                   "encoder_sha256": "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
                   "lane_cnf": os.path.join(EXPLORE, "B_C311.cnf")},
}
STOP = {"requested": None}            # set by the driver's SIGTERM handler


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_regular(path):
    """SHA-256 and size of a regular file; refuses (raises) on FIFOs and other special files without opening them."""
    st = os.lstat(path)
    if not stat.S_ISREG(st.st_mode):
        raise ValueError("not a regular file, not opened: %s (mode %o)" % (path, st.st_mode))
    h = hashlib.sha256()
    n = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
            n += len(chunk)
    return h.hexdigest(), n


def sha_file(path):
    return sha_regular(path)[0]


def read_regular(path):
    st = os.lstat(path)
    if not stat.S_ISREG(st.st_mode):
        raise ValueError("not a regular file, not opened: %s" % path)
    with open(path, "rb") as f:
        return f.read()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def free_bytes():
    st = os.statvfs(DESK)
    return st.f_bavail * st.f_frsize


def gate(what):
    fb = free_bytes()
    return {"what": what, "at": now(), "free_bytes": fb, "threshold": GATE, "pass": fb >= GATE}


def write_json_x(path, obj):
    with open(path, "x") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")
    return sha_file(path)


def open_append_x(path):
    return os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_APPEND, 0o644)


def script_hashes():
    return {n: sha_file(os.path.join(SCRIPTS, n)) for n in sorted(os.listdir(SCRIPTS)) if n.endswith(".py")}


def binary_record(path):
    real = os.path.realpath(path)
    h, n = sha_regular(real)
    return {"path": path, "realpath": real, "sha256": h, "bytes": n}


def pin_status():
    got = {p: sha_file(p) for p in list(CODE_PINS) + list(BIN_PINS)}
    want = dict(CODE_PINS, **BIN_PINS)
    return got, {p: h for p, h in got.items() if h != want[p]}


def producer_evidence(item):
    """Producer receipt, cube metadata and the B-map oracle receipt (read-only, regular files only), hashed, parsed
    and cross-checked against the brief's pins. The lane CNF copy is hashed for the record only, never used."""
    if ITEMS[item].get("kind") == "cuts":
        return producer_evidence_cuts(item)
    it = ITEMS[item]
    rb = read_regular(it["producer_receipt"])
    mb = read_regular(it["meta"])
    ob = read_regular(ORACLE_RECEIPT)
    r, m, o = json.loads(rb), json.loads(mb), json.loads(ob)
    reg = r.get("regeneration") or {}
    pre, suf = it["regen_code_sha256_prefix_suffix"]
    cnf_sha, cnf_len = sha_regular(it["lane_cnf"])
    plog = {}
    for key in ("producer_checker_log", "producer_solver_log"):
        h, n = sha_regular(it[key])
        plog[key] = {"path": it[key], "sha256": h, "bytes": n}
    out = {"receipt": {"path": it["producer_receipt"], "sha256": sha_bytes(rb), "bytes": len(rb)},
           "meta": {"path": it["meta"], "sha256": sha_bytes(mb), "bytes": len(mb)},
           "oracle_receipt": {"path": ORACLE_RECEIPT, "sha256": sha_bytes(ob), "bytes": len(ob)},
           "lane_cnf_copy": {"path": it["lane_cnf"], "sha256": cnf_sha, "bytes": cnf_len,
                             "use": "hashed read-only for the record; never given to the solver or checker"},
           "producer_logs": plog,
           "receipt_fields": {k: r.get(k) for k in (
               "started_at", "finished_at", "seconds", "solver_command", "checker_command", "solver_rc",
               "checker_rc", "checker_status_lines", "verified_unsat", "peak_sampled_aggregate_rss_bytes",
               "safety_stop_reason", "cnf_sha256", "solver_binary_sha256", "checker_binary_sha256",
               "checker_source_sha256", "solver_log_sha256", "checker_log_sha256", "native_limits_seconds",
               "encoder", "cube", "status", "regeneration", "bmap_oracle_receipt_sha256", "bmap_oracle_sha256",
               "driver_sha256", "scope")},
           "meta_fields": m,
           "oracle_fields": {k: o.get(k) for k in ("status", "failures", "decoded_identity_mismatches",
                                                   "oracle_sha256", "encoder_A_sha256", "encoder_B_sha256",
                                                   "cube_wrapper_sha256", "A_map_equals_wrapper_map", "B_base",
                                                   "B_cube_metadata_bindings", "finished_at", "claim")}}
    checks = {
        "receipt_sha256_equals_pin": out["receipt"]["sha256"] == it["producer_receipt_sha256"],
        "receipt_cnf_equals_pin": r.get("cnf_sha256") == it["cnf_sha256"],
        "receipt_encoder_cube": r.get("encoder") == it["encoder"] and r.get("cube") == it["cube"],
        "receipt_solver_binary_equals_pin": r.get("solver_binary_sha256") == BIN_PINS[KISSAT],
        "receipt_regen_cnf_equals_pin": reg.get("regenerated_cnf_sha256") == it["cnf_sha256"],
        "receipt_regen_base_equals_pin": reg.get("base_cnf_sha256") == it["base_cnf_sha256"],
        "receipt_regen_meta_equals_pin": reg.get("existing_metadata_sha256") == it["meta_sha256"],
        "receipt_regen_encoder_equals_pin": reg.get("source_encoder_sha256") == it["encoder_sha256"],
        "receipt_regen_code_matches_abbrev": (isinstance(reg.get("regeneration_code_sha256"), str)
                                              and reg["regeneration_code_sha256"].startswith(pre)
                                              and reg["regeneration_code_sha256"].endswith(suf)),
        "receipt_oracle_receipt_sha_equals_file": r.get("bmap_oracle_receipt_sha256") == out["oracle_receipt"]["sha256"],
        "meta_sha256_equals_pin": out["meta"]["sha256"] == it["meta_sha256"],
        "meta_cnf_equals_pin": m.get("cnf_sha256") == it["cnf_sha256"],
        "meta_base_equals_pin": m.get("base_cnf_sha256") == it["base_cnf_sha256"],
        "meta_wrapper_equals_pin": m.get("wrapper_sha256") == CODE_PINS[os.path.join(CODE, "k3_cubes.py")],
        "meta_encoder_equals_pin": m.get("base_encoder_sha256") == it["encoder_sha256"],
        "meta_encoder_cube": m.get("encoder") == it["encoder"] and m.get("cube") == it["cube"],
        "oracle_status_pass": o.get("status") == "PASS" and o.get("decoded_identity_mismatches") == 0,
        "oracle_pins_equal": (o.get("encoder_B_sha256") == it["encoder_sha256"]
                              and o.get("encoder_A_sha256") == CODE_PINS[os.path.join(CODE, "gram_enc.py")]
                              and o.get("cube_wrapper_sha256") == CODE_PINS[os.path.join(CODE, "k3_cubes.py")]
                              and (o.get("B_base") or {}).get("sha256") == it["base_cnf_sha256"]),
        "producer_logs_equal_receipt": (plog["producer_checker_log"]["sha256"] == r.get("checker_log_sha256")
                                        and plog["producer_solver_log"]["sha256"] == r.get("solver_log_sha256")),
        "lane_cnf_copy_equals_pin": cnf_sha == it["cnf_sha256"],
    }
    out["checks"] = checks
    out["consistent"] = all(checks.values())
    return out


def producer_evidence_cuts(item):
    """Cuts-kind producer evidence: the route-B C311+cuts receipt, the B_C311 input metadata, the B-map oracle and the
    lane input-CNF copy (hashed only). Receipt fields are flattened into the cube-receipt names."""
    it = ITEMS[item]
    rb, mb, ob = read_regular(it["producer_receipt"]), read_regular(it["meta"]), read_regular(ORACLE_RECEIPT)
    r, m, o = json.loads(rb), json.loads(mb), json.loads(ob)
    res, prep, bind = r.get("result") or {}, r.get("prepared") or {}, r.get("bindings") or {}
    regen, mods = prep.get("regeneration") or {}, (r.get("environment") or {}).get("modules") or {}
    cnf_sha, cnf_len = sha_regular(it["lane_cnf"])
    plog = {}
    for key in ("producer_checker_log", "producer_solver_log"):
        h, n = sha_regular(it[key])
        plog[key] = {"path": it[key], "sha256": h, "bytes": n}
    fields = {k: res.get(k) for k in ("seconds", "solver_command", "checker_command", "solver_rc", "checker_rc",
                                       "checker_status_lines", "peak_sampled_aggregate_rss_bytes",
                                       "safety_stop_reason", "solver_binary_sha256", "checker_binary_sha256",
                                       "checker_source_sha256", "solver_log_sha256", "checker_log_sha256",
                                       "native_limits_seconds")}
    fields.update({"started_at": r.get("started_at"), "finished_at": r.get("finished_at"),
                   "verified_unsat": r.get("verified_unsat"), "status": r.get("status"), "route": r.get("route"),
                   "cnf_sha256": prep.get("strengthened_sha256"), "encoder": "B", "cube": "C311+cuts",
                   "prepared": prep, "bindings": bind})
    out = {"receipt": {"path": it["producer_receipt"], "sha256": sha_bytes(rb), "bytes": len(rb)},
           "meta": {"path": it["meta"], "sha256": sha_bytes(mb), "bytes": len(mb)},
           "oracle_receipt": {"path": ORACLE_RECEIPT, "sha256": sha_bytes(ob), "bytes": len(ob)},
           "lane_cnf_copy": {"path": it["lane_cnf"], "sha256": cnf_sha, "bytes": cnf_len,
                             "use": "input CNF; hashed read-only for the record; never given to the solver or checker"},
           "producer_logs": plog, "receipt_fields": fields, "meta_fields": m,
           "oracle_fields": {k: o.get(k) for k in ("status", "failures", "decoded_identity_mismatches",
                                                   "oracle_sha256", "encoder_A_sha256", "encoder_B_sha256",
                                                   "cube_wrapper_sha256", "A_map_equals_wrapper_map", "B_base",
                                                   "finished_at", "claim")}}
    checks = {
        "receipt_sha256_equals_pin": out["receipt"]["sha256"] == it["producer_receipt_sha256"],
        "receipt_route_B": r.get("route") == "B",
        "receipt_strengthened_equals_pin": (prep.get("strengthened_sha256") == it["cnf_sha256"]
                                            and bind.get("expected_strengthened_sha256") == it["cnf_sha256"]),
        "receipt_input_equals_pin": prep.get("input_sha256") == it["input_sha256"],
        "receipt_block_equals_pin": (prep.get("block_sha256") == it["block_sha256"]
                                     and prep.get("block_clauses") == it["block_clauses"]),
        "receipt_base_equals_pin": regen.get("base_sha256") == it["base_cnf_sha256"],
        "receipt_meta_equals_pin": regen.get("B_C311_metadata_sha256") == it["meta_sha256"],
        "receipt_solver_binary_equals_pin": res.get("solver_binary_sha256") == BIN_PINS[KISSAT],
        "receipt_oracle_receipt_sha_equals_file": bind.get("oracle_receipt_sha256") == out["oracle_receipt"]["sha256"],
        "receipt_module_pins_equal": all((mods.get(n) or {}).get("sha256") == CODE_PINS[os.path.join(CODE, n + ".py")]
                                         for n in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1")),
        "meta_sha256_equals_pin": out["meta"]["sha256"] == it["meta_sha256"],
        "meta_cnf_equals_input_pin": m.get("cnf_sha256") == it["input_sha256"],
        "meta_base_equals_pin": m.get("base_cnf_sha256") == it["base_cnf_sha256"],
        "meta_wrapper_equals_pin": m.get("wrapper_sha256") == CODE_PINS[os.path.join(CODE, "k3_cubes.py")],
        "meta_encoder_equals_pin": m.get("base_encoder_sha256") == it["encoder_sha256"],
        "meta_encoder_cube": m.get("encoder") == "B" and m.get("cube") == "C311",
        "oracle_status_pass": o.get("status") == "PASS" and o.get("decoded_identity_mismatches") == 0,
        "oracle_pins_equal": (o.get("encoder_B_sha256") == it["encoder_sha256"]
                              and o.get("encoder_A_sha256") == CODE_PINS[os.path.join(CODE, "gram_enc.py")]
                              and o.get("cube_wrapper_sha256") == CODE_PINS[os.path.join(CODE, "k3_cubes.py")]
                              and (o.get("B_base") or {}).get("sha256") == it["base_cnf_sha256"]),
        "producer_logs_equal_receipt": (plog["producer_checker_log"]["sha256"] == res.get("checker_log_sha256")
                                        and plog["producer_solver_log"]["sha256"] == res.get("solver_log_sha256")),
        "lane_input_copy_equals_input_pin": cnf_sha == it["input_sha256"],
    }
    out["checks"] = checks
    out["consistent"] = all(checks.values())
    return out


def run_capture(argv):
    """Popen with captured stdout/stderr (reader threads), reaped with a blocking os.wait4; no timeout."""
    t0 = time.monotonic()
    started = now()
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=TMP, env=ENV)
    bufs = {"out": [], "err": []}

    def pump(stream, key):
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            bufs[key].append(chunk)

    threads = [threading.Thread(target=pump, args=(p.stdout, "out"), daemon=True),
               threading.Thread(target=pump, args=(p.stderr, "err"), daemon=True)]
    for t in threads:
        t.start()
    pid, st, ru = os.wait4(p.pid, 0)
    p.returncode = os.waitstatus_to_exitcode(st)
    for t in threads:
        t.join()
    p.stdout.close()
    p.stderr.close()
    return {"argv": argv, "cwd": TMP, "started_at": started, "finished_at": now(), "rc": p.returncode,
            "seconds": round(time.monotonic() - t0, 3), "maxrss_bytes": ru.ru_maxrss,
            "user_seconds": round(ru.ru_utime, 3)}, b"".join(bufs["out"]), b"".join(bufs["err"])


def regenerate(item):
    """The item's composition script (compose_B_v1.py, or compose_Bcuts_v1.py for kind cuts) in a subprocess (cwd and
    TMPDIR = desk tmp); the CNF arrives on a pipe and stays in memory."""
    script = ITEMS[item].get("compose", "compose_B_v1.py")
    info, out, err = run_capture([PY, "-I", "-B", os.path.join(SCRIPTS, script), ITEMS[item]["cube"]])
    info["stdout_bytes"] = len(out)
    info["stderr_tail"] = err.decode(errors="replace")[-4000:]
    info["compose_info"] = None
    if info["rc"] == 0:
        try:
            info["compose_info"] = json.loads(err.decode().strip().splitlines()[-1])
        except Exception as e:  # recorded; the hash comparison does not depend on it
            info["compose_info_error"] = repr(e)
    return (out if info["rc"] == 0 else None), info


def check_regen(item, cnf, info, meta):
    it = ITEMS[item]
    got = sha_bytes(cnf) if cnf is not None else None
    ci = info.get("compose_info") or {}
    head = cnf[:cnf.index(b"\n")].decode("ascii", "replace") if cnf else None
    rec = {"item": item, "cnf_sha256": got, "expected_cnf_sha256": it["cnf_sha256"],
           "cnf_hash_match": (got == it["cnf_sha256"]) if got is not None else None,
           "cnf_bytes": len(cnf) if cnf is not None else None, "cnf_header": head,
           "compose_reported_sha_equals_stdout": ci.get("out_sha256") == got if got else None,
           "base_cnf_sha256": ci.get("base_cnf_sha256"),
           "base_cnf_equals_pin": ci.get("base_cnf_sha256") == it["base_cnf_sha256"],
           "base_empty_clause_lines": ci.get("base_empty_clause_lines"),
           "meta_agreement": {k: ci.get(k) == meta.get(k) for k in (
               "base_cnf_sha256", "support_sets", "cube_unit_clauses", "same_ray_identities", "extra_clauses")},
           "regen_run": info}
    if it.get("kind") == "cuts":
        rec["cuts"] = {"input_sha256_equals_pin": ci.get("input_sha256") == it["input_sha256"],
                       "block_sha256_equals_pin": ci.get("block_sha256") == it["block_sha256"],
                       "block_clauses_equal_pin": ci.get("block_clauses") == it["block_clauses"],
                       "input_header": ci.get("input_header"), "out_header": ci.get("out_header")}
    return rec


# --- RSS through libproc (macOS sys/proc_info.h: PROC_PIDTASKINFO = 4, struct proc_taskinfo is 96 bytes,
# pti_resident_size is the uint64 at offset 8). Same as the A-side desk.
_LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
_LIBPROC.proc_pidinfo.restype = ctypes.c_int


def rss(pid):
    buf = ctypes.create_string_buffer(96)
    n = _LIBPROC.proc_pidinfo(pid, 4, 0, buf, 96)
    return struct.unpack_from("=Q", buf.raw, 8)[0] if n == 96 else 0


# --- fresh phys-2 lane capacity scan (launcher only; never run inside the supervised driver)
LANE_MARKERS = ("/moqls7-maximum", "/review/moqls7-")
NATIVE = {"cadical", "kissat", "drat-trim", "lrat-check", "lrat-trim", "cake_lpr", "dpr-trim", "glucose",
          "minisat", "lingeling", "plingeling", "treengeling", "cryptominisat5", "kissat_mab", "dpr2pr"}
ROUTE_A = re.compile(r"C311cuts_A(?![A-Za-z0-9])|k3_cuts_certify_r\d+\.py A(\s|$)")
ROUTE_B = re.compile(r"C311cuts_B(?![A-Za-z0-9])|k3_cuts_certify_r\d+\.py B(\s|$)")
CAP_ARG = re.compile(r"--rss-cap[ =](\d+)")


def _run_text(argv):
    return subprocess.run(argv, stdin=subprocess.DEVNULL, capture_output=True, text=True, env=ENV, cwd=TMP)


def lane_scan(own_root=None):
    """One fresh scan. Lane processes: cwd or argv contains a lane marker. own_root (this launcher's pid) and its
    descendants are excluded. Returns counts, route flags, RSS reservations and the computable RSS cap."""
    at = now()
    a = _run_text(["/bin/ps", "-axww", "-o", "pid=,ppid=,pgid=,state=,rss=,comm="])
    b = _run_text(["/bin/ps", "-axww", "-o", "pid=,args="])
    if a.returncode != 0 or b.returncode != 0:
        return {"at": at, "error": "ps failed: rc %d/%d" % (a.returncode, b.returncode)}
    procs = {}
    for line in a.stdout.splitlines():
        parts = line.split(None, 5)
        if len(parts) < 6:
            continue
        pid, ppid, pgid, state, rss_kb, comm = parts
        procs[int(pid)] = {"pid": int(pid), "ppid": int(ppid), "pgid": int(pgid), "state": state,
                           "rss_bytes": int(rss_kb) * 1024, "comm": comm.strip(), "args": "", "cwd": ""}
    for line in b.stdout.splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2 and parts[0].isdigit() and int(parts[0]) in procs:
            procs[int(parts[0])]["args"] = parts[1]
    children = {}
    for p in procs.values():
        children.setdefault(p["ppid"], []).append(p["pid"])

    def descendants(root):
        out, stack = set(), [root]
        while stack:
            for c in children.get(stack.pop(), []):
                if c not in out:
                    out.add(c)
                    stack.append(c)
        return out

    own = ({own_root} | descendants(own_root)) if own_root else set()
    cand = [p["pid"] for p in procs.values() if p["pid"] not in own and (
        os.path.basename(p["comm"]) in NATIVE or "ython" in os.path.basename(p["comm"])
        or os.path.basename(p["comm"]) in ("bash", "sh", "zsh", "time"))]
    if cand:
        lo = _run_text(["/usr/sbin/lsof", "-a", "-d", "cwd", "-p", ",".join(map(str, cand)), "-Fpn"])
        cur = None
        for line in lo.stdout.splitlines():
            if line.startswith("p"):
                cur = int(line[1:])
            elif line.startswith("n") and cur in procs:
                procs[cur]["cwd"] = line[1:]
    lane = [p for p in procs.values() if p["pid"] not in own
            and any(m in p["args"] or m in p["cwd"] for m in LANE_MARKERS)]
    live = [p for p in lane if not p["state"].startswith("Z")]
    natives = [p for p in live if os.path.basename(p["comm"]) in NATIVE]
    lane_rss = sum(p["rss_bytes"] for p in live)
    # RSS reservations: supervised runs by their declared cap; unsupervised native groups by the lane's 3.5 GiB
    # standard stop (or their current RSS if larger); everything else by current RSS plus a margin.
    covered, supervised = set(), []
    for p in live:
        m = CAP_ARG.search(p["args"])
        if "supervise_r" in p["args"] and m:
            desc = descendants(p["pid"])
            groups = {procs[d]["pgid"] for d in desc if d in procs}
            cov = {p["pid"]} | desc | {q["pid"] for q in procs.values() if q["pgid"] in groups}
            covered |= cov
            supervised.append({"supervisor_pid": p["pid"], "rss_cap": int(m.group(1)),
                               "covered_pids": sorted(cov),
                               "covered_rss_now": sum(procs[c]["rss_bytes"] for c in cov if c in procs)})
    groups = {}
    for p in natives:
        if p["pid"] not in covered:
            groups.setdefault(p["pgid"], set()).add(p["pid"])
    unsup = []
    for pgid in groups:
        members = {q["pid"] for q in procs.values() if q["pgid"] == pgid and q["pid"] not in own}
        covered |= members
        cur_rss = sum(procs[q]["rss_bytes"] for q in members)
        unsup.append({"pgid": pgid, "pids": sorted(members), "rss_now": cur_rss,
                      "reserve": max(UNSUPERVISED_GROUP_RESERVE, cur_rss)})
    others = [p for p in live if p["pid"] not in covered]
    others_rss = sum(p["rss_bytes"] for p in others)
    reserved = (sum(s["rss_cap"] for s in supervised) + sum(u["reserve"] for u in unsup)
                + others_rss + OTHER_LANE_MARGIN)
    cap = min(CAP_MAX, LANE_RSS_LIMIT - reserved - SAFETY_MARGIN)
    route_a = [p["pid"] for p in live if ROUTE_A.search(p["args"])]
    route_b = [p["pid"] for p in live if ROUTE_B.search(p["args"])]
    route_b_dirs = sorted(d for d in glob.glob(os.path.join(K3DIR, "C311cuts_B_r*")) if os.path.isdir(d))
    route_a_records = sorted(glob.glob(os.path.join(K3DIR, "C311cuts_A_r*.supervisor.json")))
    return {"at": at, "own_excluded": sorted(own),
            "lane_natives": [{k: p[k] for k in ("pid", "ppid", "pgid", "state", "rss_bytes", "comm")}
                             | {"args": p["args"][:300], "cwd": p["cwd"]} for p in natives],
            "lane_native_busy": len(natives),
            "lane_processes": [{k: p[k] for k in ("pid", "ppid", "pgid", "state", "rss_bytes")}
                               | {"args": p["args"][:200], "cwd": p["cwd"]} for p in live],
            "lane_rss_bytes": lane_rss, "supervised": supervised, "unsupervised_native_groups": unsup,
            "other_lane_rss_bytes": others_rss, "reserved_bytes": reserved, "computable_cap": cap,
            "route_A_running_pids": route_a, "route_B_pids": route_b, "route_B_dirs": route_b_dirs,
            "route_A_supervisor_records": route_a_records,
            "route_A_running": bool(route_a), "route_B_started": bool(route_b or route_b_dirs)}


def admission(scan, fb, deadline_ok):
    """Parent slot rule (Main message received about 04:20 PDT 2026-10-18; it replaces the earlier route-A/route-B
    condition): this desk owns phys-2 lane slot 2; launch when a fresh scan shows <= 2 busy lane natives, the lane
    has RSS headroom for this run's projected peak, a fresh free-space reading is >= 12.2e9 + projected growth, and
    the clock is before this desk's launch deadline. Route flags are recorded by lane_scan for information only."""
    if "error" in scan:
        return {"ok": False, "why": [scan["error"]]}
    cond = {"natives_at_most_2": scan["lane_native_busy"] <= OTHER_NATIVE_MAX_AT_LAUNCH,
            "rss_headroom": scan["lane_rss_bytes"] + PROJECTED_PEAK <= LANE_RSS_LIMIT,
            "cap_at_least_min": scan["computable_cap"] >= MIN_CAP,
            "free_gate": fb >= GATE, "before_deadline": deadline_ok}
    return {"ok": all(cond.values()), "conditions": cond, "why": [k for k, v in cond.items() if not v]}


# --- strict status-line parser: only CR characters are removed; status lines are lines starting with 's '
def status_lines(log_bytes):
    out = []
    for raw in log_bytes.split(b"\n"):
        line = raw.replace(b"\r", b"")
        if line.startswith(b"s "):
            out.append(line.decode("ascii", "replace"))
    return out


def log_flags(log_bytes):
    return {"status_lines": status_lines(log_bytes), "not_verified_anywhere": b"NOT VERIFIED" in log_bytes,
            "timeout_anywhere": b"TIMEOUT" in log_bytes}


def strict_checks(rec, solver_feed_sha, checker_feed_sha, solver_feed_len, checker_feed_len):
    """The PASS conditions that a pipeline record alone can show (the run mode adds hash, binary and supervisor
    conditions)."""
    ch = rec.get("children") or {}
    s, c = ch.get("solver") or {}, ch.get("checker") or {}
    w = rec.get("writers") or {}
    sw, cw = w.get("solver_cnf") or {}, w.get("checker_cnf") or {}
    sf, cf = rec.get("solver_flags") or {}, rec.get("checker_flags") or {}
    return {
        "not_deferred": not rec.get("deferred"),
        "solver_rc_20": s.get("rc") == 20,
        "solver_status_exactly_unsat": sf.get("status_lines") == ["s UNSATISFIABLE"],
        "checker_rc_0": c.get("rc") == 0,
        "checker_status_exactly_verified": cf.get("status_lines") == ["s VERIFIED"],
        "no_NOT_VERIFIED_anywhere": cf.get("not_verified_anywhere") is False and sf.get("not_verified_anywhere") is False,
        "no_TIMEOUT_anywhere": cf.get("timeout_anywhere") is False and sf.get("timeout_anywhere") is False,
        "solver_feed_complete_and_equal": (sw.get("complete") is True and sw.get("written") == solver_feed_len
                                           and sw.get("sha256") == solver_feed_sha),
        "checker_feed_complete_and_equal": (cw.get("complete") is True and cw.get("written") == checker_feed_len
                                            and cw.get("sha256") == checker_feed_sha),
        "no_safety_stop": rec.get("safety_stop_reason") is None,
        "no_sigterm_sent": not rec.get("sigterm_sent"),
        "no_driver_signal": rec.get("driver_signal") is None,
        "all_children_reaped": "grace_exceeded" not in rec and set(ch) == {"solver", "checker"},
        "writer_threads_finished": all(v.get("thread_alive_after_join") is False for v in (sw, cw)),
    }


def checker_rejected(rec):
    cf = rec.get("checker_flags") or {}
    c = (rec.get("children") or {}).get("checker") or {}
    lines = cf.get("status_lines")
    return (lines is not None and "s VERIFIED" not in lines
            and ("s NOT VERIFIED" in lines or (c.get("rc") not in (None, 0))))


# --- kissat -> FIFO -> drat-trim pipeline with measured CNF feeds
def _writer(fd, data, res):
    mv, off, h = memoryview(data), 0, hashlib.sha256()
    try:
        while off < len(mv):
            n = os.write(fd, mv[off:off + (1 << 20)])
            h.update(mv[off:off + n])
            off += n
        res["complete"] = True
    except OSError as e:
        res["complete"] = False
        res["error"] = repr(e)
    finally:
        os.close(fd)
        res["written"] = off
        res["sha256"] = h.hexdigest()
        res["finished_at"] = now()


def _start_writer(fd, data):
    res = {"expected_bytes": len(data)}
    t = threading.Thread(target=_writer, args=(fd, data, res), daemon=True)
    t.start()
    return t, res


def pipeline(label, solver_cnf, solver_prefix, checker_seconds, backstop_seconds, rss_stop, checker_cnf=None):
    """kissat (argv prefix solver_prefix) reads solver_cnf from a pipe and writes binary DRAT to a desk FIFO;
    drat-trim reads checker_cnf (default solver_cnf) from a second pipe and the proof from the FIFO on stdin."""
    if checker_cnf is None:
        checker_cnf = solver_cnf
    fifo = os.path.join(FIFO_DIR, label + ".drat.fifo")
    slog = os.path.join(LOGS, label + ".solver.log")
    clog = os.path.join(LOGS, label + ".checker.log")
    cpl = os.path.join(LOGS, label + ".checkpoints.jsonl")
    for path in (fifo, slog, clog, cpl):
        if os.path.lexists(path):
            raise FileExistsError(path)
    rec = {"label": label, "solver_cnf_bytes": len(solver_cnf), "solver_cnf_sha256": sha_bytes(solver_cnf),
           "checker_cnf_bytes": len(checker_cnf), "checker_cnf_sha256": sha_bytes(checker_cnf),
           "checker_argv": [DRAT, "/dev/fd/<cnf-pipe>", "-i", "-t", str(checker_seconds)],
           "checker_stdin": os.path.relpath(fifo, DESK),
           "solver_argv": list(solver_prefix) + ["/dev/fd/<cnf-pipe>", os.path.relpath(fifo, DESK)],
           "fifo": os.path.relpath(fifo, DESK), "solver_log": os.path.relpath(slog, DESK),
           "checker_log": os.path.relpath(clog, DESK), "checkpoints": os.path.relpath(cpl, DESK),
           "checker_seconds": checker_seconds, "backstop_seconds": backstop_seconds, "rss_stop": rss_stop,
           "floor": FLOOR, "grace_seconds": GRACE, "cwd": TMP, "env": ENV, "gates": [], "sigterm_sent": [],
           "driver_signal": None, "free_bytes_start": free_bytes(), "started_at": now()}
    os.mkfifo(fifo, 0o600)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    fcntl.fcntl(rfd, fcntl.F_SETFL, fcntl.fcntl(rfd, fcntl.F_GETFL) & ~os.O_NONBLOCK)
    kfd = os.open(fifo, os.O_WRONLY)          # driver-held writer (keepalive) until the solver is reaped
    cl_fd = open_append_x(clog)
    sl_fd = open_append_x(slog)
    cp_fd = open_append_x(cpl)
    ccr, ccw = os.pipe()
    scr, scw = os.pipe()
    writers, procs, done = {}, {}, {}
    peak, samples, min_free, reason, term_at = 0, 0, None, None, None
    t0 = time.monotonic()
    next_cp = 0.0

    def terminate_live(why):
        for n, p in procs.items():
            if n not in done:
                try:
                    os.kill(p.pid, signal.SIGTERM)
                    rec["sigterm_sent"].append({"child": n, "pid": p.pid, "at": now(), "why": why})
                except OSError as e:
                    rec["sigterm_sent"].append({"child": n, "pid": p.pid, "at": now(), "why": why,
                                                "error": repr(e)})

    try:
        g = gate("immediately before drat-trim Popen")
        rec["gates"].append(g)
        if not g["pass"] or STOP["requested"]:
            rec["deferred"] = "launch gate failed before drat-trim" if not g["pass"] else STOP["requested"]
            rec["driver_signal"] = STOP["requested"]
            return rec
        check = subprocess.Popen([DRAT, "/dev/fd/%d" % ccr, "-i", "-t", str(checker_seconds)], stdin=rfd,
                                 stdout=cl_fd, stderr=subprocess.STDOUT, pass_fds=(ccr,), cwd=TMP, env=ENV)
        procs["checker"] = check
        rec["checker_pid"] = check.pid
        os.close(rfd)
        rfd = None
        os.close(ccr)
        ccr = None
        writers["checker_cnf"] = _start_writer(ccw, checker_cnf)
        ccw = None
        g = gate("immediately before kissat Popen")
        rec["gates"].append(g)
        if not g["pass"] or STOP["requested"]:
            reason = "launch gate failed before kissat" if not g["pass"] else STOP["requested"]
            rec["deferred"] = reason
            rec["safety_stop_at"] = now()
            term_at = time.monotonic()
            terminate_live(reason)
        else:
            solve = subprocess.Popen(list(solver_prefix) + ["/dev/fd/%d" % scr, fifo], stdin=subprocess.DEVNULL,
                                     stdout=sl_fd, stderr=subprocess.STDOUT, pass_fds=(scr,), cwd=TMP, env=ENV)
            procs["solver"] = solve
            rec["solver_pid"] = solve.pid
            os.close(scr)
            scr = None
            writers["solver_cnf"] = _start_writer(scw, solver_cnf)
            scw = None
        while True:
            for name, p in procs.items():
                if name in done:
                    continue
                pid, st, ru = os.wait4(p.pid, os.WNOHANG)
                if pid:
                    rc = os.waitstatus_to_exitcode(st)
                    p.returncode = rc
                    done[name] = {"rc": rc, "maxrss_bytes": ru.ru_maxrss, "ended_at": now(),
                                  "wall_seconds": round(time.monotonic() - t0, 3),
                                  "user_seconds": round(ru.ru_utime, 3), "sys_seconds": round(ru.ru_stime, 3)}
                    if name == "solver" and kfd is not None:
                        os.close(kfd)
                        kfd = None
            if len(done) == len(procs):
                break
            cur = rss(os.getpid()) + sum(rss(p.pid) for n, p in procs.items() if n not in done)
            peak = max(peak, cur)
            fb = free_bytes()
            min_free = fb if min_free is None else min(min_free, fb)
            samples += 1
            elapsed = time.monotonic() - t0
            if elapsed >= next_cp:
                os.write(cp_fd, (json.dumps({"at": now(), "elapsed_seconds": round(elapsed, 3),
                                             "aggregate_rss_bytes": cur, "peak_sampled_rss_bytes": peak,
                                             "free_bytes": fb, "done": {k: v["rc"] for k, v in done.items()}})
                                 + "\n").encode())
                next_cp += CHECKPOINT_EVERY
            if reason is None:
                if cur > rss_stop:
                    reason = "aggregate RSS safety stop: %d > %d" % (cur, rss_stop)
                elif fb < FLOOR:
                    reason = "free-space floor: %d < %d" % (fb, FLOOR)
                elif elapsed > backstop_seconds:
                    reason = "driver wall-clock backstop %d s" % backstop_seconds
                elif STOP["requested"]:
                    reason = STOP["requested"]
                    rec["driver_signal"] = STOP["requested"]
                if reason:
                    rec["safety_stop_at"] = now()
                    term_at = time.monotonic()
                    terminate_live(reason)
            elif time.monotonic() - term_at > GRACE:
                rec["grace_exceeded"] = ("children %s still alive %d s after SIGTERM; no SIGKILL sent; recorded "
                                         "for quarantine by the supervisor" % (sorted(set(procs) - set(done)), GRACE))
                break
            time.sleep(PERIOD)
    finally:
        for fd in (rfd, ccr, ccw, scr, scw, kfd):
            if fd is not None:
                os.close(fd)
        os.close(cl_fd)
        os.close(sl_fd)
        os.close(cp_fd)
    if STOP["requested"] and rec["driver_signal"] is None:
        rec["driver_signal"] = STOP["requested"]
    for name, (t, res) in writers.items():
        t.join(30)
        res["thread_alive_after_join"] = t.is_alive()
    rec["finished_at"] = now()
    rec["pipeline_seconds"] = round(time.monotonic() - t0, 3)
    rec["children"] = done
    rec["writers"] = {k: v[1] for k, v in writers.items()}
    rec["peak_sampled_aggregate_rss_bytes"] = peak
    rec["rss_samples"] = samples
    rec["min_sampled_free_bytes"] = min_free
    rec["free_bytes_end"] = free_bytes()
    rec["safety_stop_reason"] = reason
    cbytes = read_regular(clog)
    sbytes = read_regular(slog)
    rec["checker_log_sha256"] = sha_bytes(cbytes)
    rec["checker_log_bytes"] = len(cbytes)
    rec["checker_flags"] = log_flags(cbytes)
    rec["solver_log_sha256"] = sha_bytes(sbytes)
    rec["solver_log_bytes"] = len(sbytes)
    rec["solver_flags"] = log_flags(sbytes)
    rec["checkpoints_sha256"] = sha_file(cpl)
    return rec
