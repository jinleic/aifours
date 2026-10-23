#!/usr/bin/env python3
"""PA19 96h lane probe 14: read-only CNF pins and case identity for production Wave 1
(notes/production-plan-v1.md). No solver, no checker, no CNF file.

Wave 1 has 18 items, frozen below.
  ms06 DIRECT whole-case items (runner family v17, build_v2): the 9 lane-original ms06 cases that are open in
    parent frontier v4, have no direct attempt record, and come first under the frozen order. The order is
    |Aut(types)| ascending, then position in cycle2/m2-jobs-hard-direct.txt (21fdc72f...). The probe
    recomputes the order from the pinned inputs and requires it to equal W1_MS06.
  ms09 PLACEMENT-INTERVAL items (runner family v16, build_partbatch over the frozen extend_b list):
    b9 [0..814] (whole list) and the B100 measurement intervals [0..99] of b25, b69, b10, b67, b11, b8, b49, b61.
For every item the probe:
  * checks the case is open in RUN/review/pa19-parent-frontier-v4.json (5bc07039...), that its skeleton fields
    equal the pinned skeleton file entry, and, for ms09, that the list file SHA-256 and n equal the frontier entry
    and num_placements == len(placements) == n;
  * builds the CNF in process exactly as the runner family does and records (sha256, bytes, header,
    build seconds):
      ms06: E.build_v2(c0, types, empty, special) then E.cnf_bytes;
      ms09: E.build_partbatch(c0, types, empty, special, [list[i] for i in lo..hi]) then E.cnf_bytes;
    where special = profiles != [4,3,3,3,3,3] (the runner's P0);
  * records the coverage it would contribute: the whole case for ms06; [lo..hi] of 0..n-1 for ms09.
It also records |Aut| for every never-attempted open ms06 case (the full order) and the ms09 skeleton
structure (types, empty rows, |Aut|) of every open ms09 case.
Standard library plus the in-process encoder; the only child process is /bin/date. Admission: fresh
statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate marker. Self budget 280 s. The exclusive receipt with
the PID is written before any work.
Usage: probe_production_wave1_pins_v1.py OUT_JSON
"""
import hashlib
import importlib.util
import itertools
import json
import os
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
T0 = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
SK6 = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
SK9 = (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
FRONT4 = (RUN + "/review/pa19-parent-frontier-v4.json", "5bc070391d61c6e65fb49c9851d776b5468bcd4fa60bf9bdb04a6c079c52adc4")
HARDQ = (OLD + "/cycle2/m2-jobs-hard-direct.txt", "21fdc72f7ed21feda7cbc56d246421453c1e8c7dc3a47ddb82425f5b8d985c96")
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
P0 = [4, 3, 3, 3, 3, 3]
W1_MS06 = [88, 89, 186, 154, 168, 169, 282, 299, 269]
W1_MS09 = [(9, 0, 814), (25, 0, 99), (69, 0, 99), (10, 0, 99), (67, 0, 99), (11, 0, 99), (8, 0, 99), (49, 0, 99), (61, 0, 99)]
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def budget(stage):
    if time.monotonic() - T0 > BUDGET:
        raise SystemExit("REFUSED: self budget exhausted at %s; no output" % stage)


def pinned(path, h):
    with open(path, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED pin mismatch " + path)
    return raw


def aut_count(types, c0):
    ts = [tuple(sorted(t)) for t in types]
    tset = sorted(ts)
    return sum(1 for p in itertools.permutations(range(c0)) if sorted(tuple(sorted(p[v] for v in t)) for t in ts) == tset)


def digest(cnf):
    return {"sha256": hashlib.sha256(cnf).hexdigest(), "bytes": len(cnf), "header": cnf.split(b"\n", 1)[0].decode()}


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only CNF pins; children /bin/date only; no solver/checker; no CNF file"}
    with open(receipt_path, "xb") as f:
        f.write(json.dumps(receipt, indent=1, sort_keys=True).encode())
    print("RECEIPT", receipt_path, receipt["pid"], flush=True)
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    D6 = json.loads(pinned(*SK6))
    D9 = json.loads(pinned(*SK9))
    F4 = json.loads(pinned(*FRONT4))
    hard = []
    for line in pinned(*HARDQ).decode().splitlines():
        if line.strip():
            a, b = line.strip().split(":")[1].split("-")
            hard += list(range(int(a), int(b) + 1))
    pinned(*ENC)
    spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
    E = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(E)
    if not (D6["c0"] == 6 and D6["L"] == 1 and D9["c0"] == 5 and D9["L"] == 0):
        raise SystemExit("REFUSED: unexpected skeleton headers")
    sp6 = [p for p in D6["profiles"] if list(p) != P0]
    sp9 = [p for p in D9["profiles"] if list(p) != P0]
    open6 = {x["b_index"]: x for x in F4["ms06_undecided"]}
    open9 = {x["b_index"]: x for x in F4["ms09_undecided"]}
    # ms06 never-attempted order: open, in the hard queue, without any old direct record
    attempted = set()
    for b in hard:
        for n in ("ms06_b%05d.json" % b, "ms06_b%05d_v6.json" % b):
            if os.path.exists(OLD + "/cycle2/m2skel_drat/" + n):
                attempted.add(b)
    never = [b for b in hard if b in open6 and b not in attempted]
    order = sorted(never, key=lambda b: (aut_count(D6["skeletons"][b]["types"], 6), hard.index(b)))
    order_rows = [{"b": b, "aut": aut_count(D6["skeletons"][b]["types"], 6), "hard_queue_position": hard.index(b),
                   "s_tag": open6[b]["s_tag"]} for b in order]
    budget("ms06 order")
    items = []
    for b in W1_MS06:
        sk = D6["skeletons"][b]
        x = open6.get(b)
        t1 = time.monotonic()
        nv, cl = E.build_v2(D6["c0"], [tuple(t) for t in sk["types"]], sk["empty"], sp6)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        dg = digest(cnf)
        del cnf
        items.append({"family": "ms06_direct_v17", "id": "ms06:b%05d:direct" % b, "b": b,
                      "case": "ms06_b%05d" % b, "s_tag": None if x is None else x["s_tag"],
                      "open_in_frontier_v4": x is not None, "never_attempted": b in never,
                      "skeleton_fields_equal": x is not None and x["skeleton_types"] == sk["types"]
                      and x["skeleton_empty"] == sk["empty"],
                      "aut": aut_count(sk["types"], 6), "coverage": "whole case (direct build_v2)",
                      "cnf": dg, "build_seconds": round(time.monotonic() - t1, 3)})
        budget("ms06 item %d" % b)
    for b, lo, hi in W1_MS09:
        sk = D9["skeletons"][b]
        x = open9.get(b)
        lst = json.loads(pinned(OLD + "/" + x["list"]["path"], x["list"]["sha256"]))
        n = x["list"]["n"]
        list_ok = lst["num_placements"] == len(lst["placements"]) == n and 0 <= lo <= hi < n
        t1 = time.monotonic()
        nv, cl = E.build_partbatch(D9["c0"], [tuple(t) for t in sk["types"]], sk["empty"], sp9,
                                   [lst["placements"][i] for i in range(lo, hi + 1)])
        cnf = E.cnf_bytes(nv, cl)
        del cl
        dg = digest(cnf)
        del cnf
        items.append({"family": "ms09_partbatch_v16", "id": "b%05d:%05d-%05d" % (b, lo, hi), "b": b, "lo": lo, "hi": hi,
                      "case": "ms09_b%05d" % b, "s_tag": x["s_tag"], "open_in_frontier_v4": True,
                      "skeleton_fields_equal": x["skeleton_types"] == sk["types"] and x["skeleton_empty"] == sk["empty"],
                      "list": [OLD + "/" + x["list"]["path"], x["list"]["sha256"]], "denominator": n,
                      "list_ok": list_ok, "aut": aut_count(sk["types"], 5),
                      "coverage": "[%d..%d] of 0..%d (%d placements; %s)" % (lo, hi, n - 1, hi - lo + 1,
                                                                          "whole list" if (lo, hi) == (0, n - 1) else "partial"),
                      "cnf": dg, "build_seconds": round(time.monotonic() - t1, 3)})
        budget("ms09 item %d" % b)
    ms09_struct = [{"b": b, "s_tag": x["s_tag"], "n": x["list"]["n"], "types": D9["skeletons"][b]["types"],
                    "empty": D9["skeletons"][b]["empty"], "aut": aut_count(D9["skeletons"][b]["types"], 5)}
                   for b, x in sorted(open9.items())]
    checks = {"ms06_order_prefix_equals_frozen": order[:len(W1_MS06)] == W1_MS06,
              "all_items_open_in_frontier_v4": all(i["open_in_frontier_v4"] for i in items),
              "skeleton_fields_equal": all(i["skeleton_fields_equal"] for i in items),
              "ms06_items_never_attempted": all(i["never_attempted"] for i in items if i["family"] == "ms06_direct_v17"),
              "ms09_lists_ok": all(i["list_ok"] for i in items if i["family"] == "ms09_partbatch_v16"),
              "frontier_v4_counts": [len(open6), len(open9)] == [80, 63],
              "ids_distinct": len({i["id"] for i in items}) == len(items)}
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PRODUCTION-WAVE1-PINS-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons_ms06": SK6, "skeletons_ms09": SK9, "frontier_v4": FRONT4, "hard_queue": HARDQ, "encoder": ENC},
           "ms06_never_attempted_order": order_rows, "ms09_open_structure": ms09_struct,
           "items": items, "checks": checks, "all_ok": all(checks.values()),
           "scope": "CNF pins and case identity only; no coverage claim, no closure; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    budget("before output")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", res["all_ok"], flush=True)


if __name__ == "__main__":
    main()
