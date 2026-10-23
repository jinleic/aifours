#!/usr/bin/env python3
"""PA19 96h lane probe 17: generic, spec-driven CNF pins and case coverage for a production batch
(notes/production-plan-v1.md rules R0-R6). Read-only: no solver, no checker, no CNF file.

Input: a frozen batch spec JSON (argv[2]) whose SHA-256 must equal argv[3]. Schema PA19-96H-BATCH-SPEC-v1:
  frontier          [path, sha256] of the parent's current frontier (lane-original M2; never M2H)
  submitted_pending ms06: [b, ...] already pinned/launched direct items not yet accepted;
                    ms09_intervals: {"b": [[lo, hi], ...]} already pinned/launched intervals not yet accepted
  ms06_order        {"hard_queue": [path, sha256], "slice": [i, j]}: the ms06 items must equal positions i..j-1 of
                    the frozen order (never-attempted open cases, |Aut(types)| ascending, then hard-queue position)
  items             [{"family": "ms09_partbatch", "b", "lo", "hi"} | {"family": "ms06_direct", "b"}]
For every item the probe:
  * checks the case is open in the frontier (and not in any new_case_closures* list) with equal skeleton fields;
  * ms09: takes the list path/SHA-256/n from the frontier entry, checks num_placements == len(placements) == n
    and 0 <= lo <= hi < n, and checks the interval is disjoint from the submitted and other new intervals of the
    same case; it reports whether submitted + new intervals cover 0..n-1 exactly ("closes_case_if_all_accepted");
  * ms06: checks there is no old direct record (cycle2/m2skel_drat/ms06_bNNNNN.json or _v6.json) and the case
    is not in submitted_pending;
  * builds the CNF in process exactly as the runner family does (ms09: E.build_partbatch(c0, types, empty,
    special, [list[i] for i in lo..hi]); ms06: E.build_v2(c0, types, empty, special); special = profiles !=
    [4,3,3,3,3,3]) and records (sha256, bytes, header).
Standard library plus the in-process vendored encoder (d0002e60...). The only child process is /bin/date.
Admission: fresh statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate marker. Self budget 280 s. The
exclusive receipt with the PID is written before any work; the output is created exclusively under
LANE/evidence/probes/.
Usage: probe_batch_pins_v1.py OUT_JSON SPEC_JSON SPEC_SHA256
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
SK = {"ms06": (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488"),
      "ms09": (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")}
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
P0 = [4, 3, 3, 3, 3, 3]
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


def main():
    out_path = os.path.abspath(sys.argv[1])
    spec_path, spec_sha = os.path.abspath(sys.argv[2]), sys.argv[3]
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only batch CNF pins; children /bin/date only; no solver/checker; no CNF file"}
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
    spec = json.loads(pinned(spec_path, spec_sha))
    if spec.get("schema") != "PA19-96H-BATCH-SPEC-v1":
        raise SystemExit("REFUSED: spec schema")
    F = json.loads(pinned(*spec["frontier"]))
    D = {k: json.loads(pinned(*v)) for k, v in SK.items()}
    pinned(*ENC)
    espec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
    E = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(E)
    special = {k: [p for p in D[k]["profiles"] if list(p) != P0] for k in D}
    open6 = {x["b_index"]: x for x in F["ms06_undecided"]}
    open9 = {x["b_index"]: x for x in F["ms09_undecided"]}
    closed = set()
    for k, v in F.items():
        if k.startswith("new_case_closures"):
            for c in v:
                closed.add(c.get("case"))
    sub6 = set(spec["submitted_pending"].get("ms06", []))
    sub9 = {int(b): [tuple(iv) for iv in ivs] for b, ivs in spec["submitted_pending"].get("ms09_intervals", {}).items()}
    # ms06 frozen order
    hard = []
    for line in pinned(*spec["ms06_order"]["hard_queue"]).decode().splitlines():
        if line.strip():
            a, b = line.strip().split(":")[1].split("-")
            hard += list(range(int(a), int(b) + 1))
    attempted = {b for b in hard for n in ("ms06_b%05d.json" % b, "ms06_b%05d_v6.json" % b)
                 if os.path.exists(OLD + "/cycle2/m2skel_drat/" + n)}
    never = [b for b in hard if b in open6 and b not in attempted]
    order = sorted(never, key=lambda b: (aut_count(D["ms06"]["skeletons"][b]["types"], 6), hard.index(b)))
    i, j = spec["ms06_order"]["slice"]
    new6 = [it["b"] for it in spec["items"] if it["family"] == "ms06_direct"]
    new9 = {}
    for it in spec["items"]:
        if it["family"] == "ms09_partbatch":
            new9.setdefault(it["b"], []).append((it["lo"], it["hi"]))
    budget("setup")
    items = []
    for it in spec["items"]:
        fam, b = it["family"], it["b"]
        if fam == "ms09_partbatch":
            x = open9.get(b)
            sk = D["ms09"]["skeletons"][b]
            case = "ms09_b%05d" % b
            if x is None:
                items.append({"family": fam, "b": b, "case": case, "error": "not open in frontier"})
                continue
            lst = json.loads(pinned(OLD + "/" + x["list"]["path"], x["list"]["sha256"]))
            n = x["list"]["n"]
            lo, hi = it["lo"], it["hi"]
            others = [iv for iv in sub9.get(b, [])] + [iv for iv in new9.get(b, []) if iv != (lo, hi)]
            disjoint = all(hi < a or lo > c for a, c in others)
            cover = sorted(sub9.get(b, []) + new9.get(b, []))
            exact = bool(cover) and cover[0][0] == 0 and cover[-1][1] == n - 1 and \
                all(cover[k][1] + 1 == cover[k + 1][0] for k in range(len(cover) - 1))
            nv, cl = E.build_partbatch(D["ms09"]["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special["ms09"],
                                       [lst["placements"][q] for q in range(lo, hi + 1)])
            cnf = E.cnf_bytes(nv, cl)
            del cl
            rec = {"family": fam, "id": "b%05d:%05d-%05d" % (b, lo, hi), "b": b, "lo": lo, "hi": hi, "case": case,
                   "s_tag": x["s_tag"], "list": [OLD + "/" + x["list"]["path"], x["list"]["sha256"]], "denominator": n,
                   "checks": {"open": case not in closed, "list_ok": lst["num_placements"] == len(lst["placements"]) == n
                              and 0 <= lo <= hi < n, "disjoint": disjoint,
                              "skeleton_fields_equal": x["skeleton_types"] == sk["types"] and x["skeleton_empty"] == sk["empty"]},
                   "case_intervals_after_batch": cover, "closes_case_if_all_accepted": exact}
        else:
            x = open6.get(b)
            sk = D["ms06"]["skeletons"][b]
            case = "ms06_b%05d" % b
            if x is None:
                items.append({"family": fam, "b": b, "case": case, "error": "not open in frontier"})
                continue
            nv, cl = E.build_v2(D["ms06"]["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special["ms06"])
            cnf = E.cnf_bytes(nv, cl)
            del cl
            rec = {"family": fam, "id": "ms06:b%05d:direct" % b, "b": b, "case": case, "s_tag": x["s_tag"],
                   "aut": aut_count(sk["types"], 6), "coverage": "whole case (direct build_v2)",
                   "checks": {"open": case not in closed and ("ms06:b%05d:direct" % b) not in closed,
                              "never_attempted": b not in attempted, "not_submitted": b not in sub6,
                              "skeleton_fields_equal": x["skeleton_types"] == sk["types"] and x["skeleton_empty"] == sk["empty"]},
                   "closes_case_if_all_accepted": True}
        rec["cnf"] = {"sha256": hashlib.sha256(cnf).hexdigest(), "bytes": len(cnf), "header": cnf.split(b"\n", 1)[0].decode()}
        del cnf
        items.append(rec)
        budget("item %s" % rec["id"])
    checks = {"all_items_ok": all("error" not in r and all(r["checks"].values()) for r in items),
              "ms06_items_equal_order_slice": new6 == order[i:j],
              "ids_distinct": len({r.get("id") for r in items}) == len(items)}
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-BATCH-PINS-v1", "spec": [spec_path, spec_sha], "receipt": receipt_path,
           "receipt_pid": receipt["pid"], "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK, "encoder": ENC, "frontier": spec["frontier"]},
           "ms06_order": [{"b": b, "aut": aut_count(D["ms06"]["skeletons"][b]["types"], 6)} for b in order],
           "items": items, "checks": checks, "all_ok": all(checks.values()),
           "scope": "CNF pins and case identity only; no coverage claim, no closure; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    budget("before output")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", res["all_ok"], flush=True)


if __name__ == "__main__":
    main()
