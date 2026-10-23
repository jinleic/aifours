#!/usr/bin/env python3
"""k3_direct_B_r6.py: ONE authorised B/C321 or B/C411 retry after a checker-clock obstruction (parent 2026-10-18).

Same science as k3_direct_B_r5.py (0e391cc7...e4f6): unchanged frozen B cube CNFs (pinned below), runtime B-map
oracle prerequisite, A calibration and control receipts, tested in-memory regeneration, outer 12.2e9-plus-growth
gates, kissat --time=3600, streamed binary DRAT only (no proof file), unchanged acceptance predicate.
Driver-only deltas:
  * transport proof_stream_r2.run_pair with drat-trim -t 7200 (drat-trim's clock starts at checker start and so
    includes the FIFO wait for the solver); cooperative wall guard max(3600, 7200) + 120 = 7320 s < 10800 s;
  * refuses unless the r5 receipt for this cube ended ONLY on the checker-clock obstruction: status UNKNOWN,
    solver rc 20, checker rc 0, checker status lines exactly ["s TIMEOUT"], no safety stop, pinned CNF SHA;
  * refuses unless kissat, drat-trim (binary and source), the oracle receipt and the CNF match the frozen pins;
  * B/C321 refuses until the B/C411 r5 attempt has ended (its receipt or deferral exists);
  * fixed output directory evidence/k3cubes/cert_B_r6 with exclusive files, so each cube gets at most one attempt.
UNKNOWN is retained; no further limit increase or retry is automatic.
Usage: k3_direct_B_r6.py C321|C411
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
OUTDIR = os.path.join(LANE, "evidence", "k3cubes", "cert_B_r6")
R5DIR = os.path.join(LANE, "evidence", "k3cubes", "cert_B_r5")
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
AUTHORITY = ("Parent message 15aadaf1be5e6ec0 (received 2026-10-18 about 01:52 PDT host clock): ONE new-version "
             "B/C321 retry after the B/C411 r5 attempt ends, solver native 3600 s and drat-trim native 7200 s; ONE "
             "analogous B/C411 retry only if its r5 attempt ends only on the same checker-clock obstruction")


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
    ap.add_argument("cube", choices=("C321", "C411"))
    a = ap.parse_args()
    os.makedirs(OUTDIR, exist_ok=True)
    prefix = os.path.join(OUTDIR, "B_" + a.cube)
    receipt = prefix + ".json"
    for path in (receipt, prefix + ".deferred.json"):
        if os.path.exists(path):
            raise FileExistsError(path)
    if a.cube == "C321" and not any(os.path.exists(os.path.join(R5DIR, "B_C411" + s)) for s in (".json", ".deferred.json")):
        raise SystemExit("B/C411 r5 attempt has not ended; B/C321 retry not yet authorised")
    r5_path = os.path.join(R5DIR, "B_" + a.cube + ".json")
    with open(r5_path) as f:
        r5 = json.load(f)
    if not (r5.get("encoder") == "B" and r5.get("cube") == a.cube and r5.get("status") == "UNKNOWN"
            and r5.get("verified_unsat") is False and r5.get("solver_rc") == 20 and r5.get("checker_rc") == 0
            and r5.get("checker_status_lines") == ["s TIMEOUT"] and r5.get("safety_stop_reason") is None
            and r5.get("cnf_sha256") == CNF_SHA[a.cube]):
        raise SystemExit("r5 receipt does not show only the checker-clock obstruction; retry not authorised")
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
                   "retry_of_r5_receipt_sha256": sha(r5_path), "authority": AUTHORITY,
                   "delta_record": "review/K3-DIRECT-B-DELTA.r6.json",
                   "controls": controls, "driver_sha256": sha(__file__),
                   "scope": "This original B cube only; parent whole-proof acceptance remains separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "status", "verified_unsat", "solver_rc", "checker_rc", "seconds")}), flush=True)


if __name__ == "__main__":
    main()
