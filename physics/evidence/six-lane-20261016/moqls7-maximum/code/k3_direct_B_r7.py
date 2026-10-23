#!/usr/bin/env python3
"""k3_direct_B_r7.py: ONE authorised B/C411 attempt after the external floor stop (parent 2026-10-18, after 04:10).

Path-only new version of k3_direct_B_r6.py (24fcfea8...c44d). The r6 B/C411 attempt (receipt 92354254...0184) was
stopped by the global free-space floor at 04:09:50, an external stop and not a checker or solver obstruction. Driver
r6 would now refuse its exclusive cert_B_r6/B_C411 names. Changes from r6, nothing else:
  * output directory evidence/k3cubes/cert_B_r7 (exclusive files; at most one attempt);
  * cube C411 only;
  * the precondition reads the r6 C411 receipt and requires the external floor stop: status UNKNOWN, verified_unsat
    false, safety_stop_reason "global free-space floor", pinned CNF. The B/C321 ordering check is dropped;
  * authority, delta-record and retry fields name this attempt.
Unchanged from r6: the frozen B cube CNF pin, the runtime B-map oracle prerequisite, A calibration and control
receipts, tested in-memory regeneration, outer 12.2e9-plus-growth gates, kissat --time=3600, proof_stream_r2 with
drat-trim -t 7200 and wall guard 7320 s, streamed binary DRAT only, binary pins and the acceptance predicate.
UNKNOWN is retained; no further limit increase or retry is automatic.
Usage: k3_direct_B_r7.py C411   (start only after the parent desk's B/C321 replay hands over slot 2)
"""
import argparse
import json
import os
import shutil

from gram_certify_r4 import CHECKER, now, sha
from k3_cube_certify_r3 import regeneration
from proof_stream_r2 import run_pair

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUTDIR = os.path.join(LANE, "evidence", "k3cubes", "cert_B_r7")
R6DIR = os.path.join(LANE, "evidence", "k3cubes", "cert_B_r6")
GROWTH = 10485760
SOLVER_SECONDS, CHECKER_SECONDS = 3600, 7200
ORACLE_RECEIPT = os.path.join(LANE, "evidence", "k3cubes", "bmap_oracle_r1.json")
ORACLE_SHA = "13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e"
ORACLE_RECEIPT_SHA = "6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c"
CNF_SHA = {"C321": "8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6",
           "C411": "01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8"}
KISSAT_SHA = "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848"
CHECKER_SHA = "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4"
CHECKER_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
AUTHORITY = ("Parent message after the 04:09:50 external floor stop (received about 04:16 PDT host clock): ONE new "
             "B/C411 attempt with the r6 limits (solver 3600 s, drat-trim 7200 s) in slot 2, only after the parent "
             "desk M7BCubeParentReplay finishes its B/C321 replay")


def gate(prefix, phase):
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    record = {"at": now(), "phase": phase, "available_bytes": available,
              "launch_threshold_bytes": 12200000000, "projected_retained_growth_bytes": GROWTH}
    if available < 12200000000 + GROWTH:
        record["status"] = "UNKNOWN / DEFERRED_RESOURCE; no solver/checker launched"
        with open(prefix + ".deferred.json", "x") as f:
            json.dump(record, f, indent=2)
            f.write("\n")
        print(json.dumps(record), flush=True)
        raise SystemExit(0)
    record["status"] = "PASS"
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cube", choices=("C411",))
    a = ap.parse_args()
    os.makedirs(OUTDIR, exist_ok=True)
    prefix = os.path.join(OUTDIR, "B_" + a.cube)
    receipt = prefix + ".json"
    for path in (receipt, prefix + ".deferred.json"):
        if os.path.exists(path):
            raise FileExistsError(path)
    r6_path = os.path.join(R6DIR, "B_" + a.cube + ".json")
    with open(r6_path) as f:
        r6 = json.load(f)
    if not (r6.get("encoder") == "B" and r6.get("cube") == a.cube and r6.get("status") == "UNKNOWN"
            and r6.get("verified_unsat") is False and r6.get("safety_stop_reason") == "global free-space floor"
            and r6.get("cnf_sha256") == CNF_SHA[a.cube]):
        raise SystemExit("r6 receipt does not show the external floor stop; attempt not authorised")
    kissat = os.path.realpath(shutil.which("kissat") or "")
    if not (os.path.isfile(kissat) and sha(kissat) == KISSAT_SHA and sha(CHECKER) == CHECKER_SHA
            and sha(CHECKER + ".c") == CHECKER_SOURCE_SHA and sha(ORACLE_RECEIPT) == ORACLE_RECEIPT_SHA):
        raise SystemExit("Solver, checker or oracle receipt differs from the frozen pins; no B retry attempted")
    first_gate = gate(prefix, "before in-memory B regeneration")
    with open(ORACLE_RECEIPT) as f:
        oracle = json.load(f)
    if not (oracle.get("status") == "PASS" and oracle.get("oracle_sha256") == ORACLE_SHA
            and oracle.get("decoded_identity_mismatches") == 0
            and oracle.get("encoder_B_sha256") == sha(os.path.join(HERE, "gram_encB.py"))
            and oracle.get("encoder_A_sha256") == sha(os.path.join(HERE, "gram_enc.py"))
            and oracle.get("cube_wrapper_sha256") == sha(os.path.join(HERE, "k3_cubes.py"))
            and oracle["B_cube_metadata_bindings"][a.cube]["equal"]):
        raise SystemExit("Runtime B-map oracle prerequisite not met; no B certificate attempted")
    acase = os.path.join(LANE, "evidence", "k3cubes", "cert_r2", "A_" + a.cube + ".json")
    with open(acase) as f:
        calibration = json.load(f)
    assert calibration["encoder"] == "A" and calibration["cube"] == a.cube
    assert calibration["verified_unsat"] and calibration["solver_rc"] == 20 and calibration["checker_rc"] == 0
    controls = {}
    for label, rel in (("component_controls", "evidence/gram/review_controls_r1/summary.json"),
                       ("transport_controls", "evidence/gram/transport_controls_r2/summary.json")):
        path = os.path.join(LANE, rel)
        with open(path) as f:
            assert json.load(f)["status"] == "PASS"
        controls[label] = sha(path)
    cnf, regen = regeneration("B", a.cube)
    if regen["regenerated_cnf_sha256"] != CNF_SHA[a.cube]:
        raise SystemExit("Regenerated CNF differs from the frozen pin; no B retry attempted")
    second_gate = gate(prefix, "before direct native B proof pipeline")
    result = run_pair(cnf, ["kissat", "-q", "-f", "--time=%d" % SOLVER_SECONDS, cnf], prefix,
                      SOLVER_SECONDS, CHECKER_SECONDS)
    result["verified_unsat"] = (result["verified_unsat"] and result["cnf_sha256"] == CNF_SHA[a.cube]
                                and result["solver_binary_sha256"] == KISSAT_SHA
                                and result["checker_binary_sha256"] == CHECKER_SHA)
    status = "VERIFIED_UNSAT_CASE" if result["verified_unsat"] else ("SAT_PATTERN_ONLY" if result["solver_rc"] == 10 else "UNKNOWN")
    result.update({"encoder": "B", "cube": a.cube, "status": status, "regeneration": regen,
                   "outer_gates": [first_gate, second_gate], "planned_new_retained_bytes": GROWTH,
                   "calibration_A_receipt_sha256": sha(acase), "B_pre_screened": False,
                   "bmap_oracle_receipt_sha256": sha(ORACLE_RECEIPT), "bmap_oracle_sha256": ORACLE_SHA,
                   "retry_of_r6_receipt_sha256": sha(r6_path), "authority": AUTHORITY,
                   "delta_record": "review/K3-DIRECT-B-DELTA.r7.json",
                   "controls": controls, "driver_sha256": sha(__file__),
                   "scope": "This original B cube only; parent whole-proof acceptance remains separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "status", "verified_unsat", "solver_rc", "checker_rc", "seconds")}), flush=True)


if __name__ == "__main__":
    main()
