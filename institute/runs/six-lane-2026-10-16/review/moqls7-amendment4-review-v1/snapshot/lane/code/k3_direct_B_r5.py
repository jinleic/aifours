#!/usr/bin/env python3
"""Direct B/C321 or B/C411 proof attempt, gated on the runtime B-map oracle (parent 2026-10-18 00:46 PDT).

Same as k3_direct_B_r4.py except that it refuses to run unless the pinned runtime oracle receipt shows that
encoder B's variables 1..2646 equal encoder A's (and the cube wrapper's) map, for the current encoder/wrapper
bytes and for this cube's B metadata; the oracle receipt SHA is bound into the certificate receipt.
Unchanged frozen encoders/cubes and tested in-memory regeneration; outer 12.2e9-plus-growth gates; no CNF/proof
copies; native limits 3600 s solver and 3600 s checker; one solver+checker pipeline. UNKNOWN is retained.
Usage: k3_direct_B_r5.py C321|C411 OUTDIR
"""
import argparse
import json
import os

from gram_certify_r4 import now, sha
from k3_cube_certify_r3 import regeneration
from proof_stream import run_pair

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GROWTH = 10485760
ORACLE_RECEIPT = os.path.join(LANE, "evidence", "k3cubes", "bmap_oracle_r1.json")
ORACLE_SHA = "13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e"



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
    ap.add_argument("outdir")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    prefix = os.path.join(a.outdir, "B_" + a.cube)
    receipt = prefix + ".json"
    for path in (receipt, prefix + ".deferred.json"):
        if os.path.exists(path):
            raise FileExistsError(path)
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
    second_gate = gate(prefix, "before direct native B proof pipeline")
    result = run_pair(cnf, ["kissat", "-q", "-f", "--time=3600", cnf], prefix, 3600, 3600)
    result["verified_unsat"] = result["verified_unsat"] and result["cnf_sha256"] == regen["regenerated_cnf_sha256"]
    status = "VERIFIED_UNSAT_CASE" if result["verified_unsat"] else ("SAT_PATTERN_ONLY" if result["solver_rc"] == 10 else "UNKNOWN")
    result.update({"encoder": "B", "cube": a.cube, "status": status, "regeneration": regen,
                   "outer_gates": [first_gate, second_gate], "planned_new_retained_bytes": GROWTH,
                   "calibration_A_receipt_sha256": sha(acase), "B_pre_screened": False,
                   "bmap_oracle_receipt_sha256": sha(ORACLE_RECEIPT), "bmap_oracle_sha256": ORACLE_SHA,
                   "authority": "Parent 2026-10-18 00:46 PDT ordered work (b)/(c): B/C321 then B/C411 after the oracle",
                   "controls": controls, "driver_sha256": sha(__file__),
                   "scope": "This original B cube only; parent whole-proof acceptance remains separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "status", "verified_unsat", "solver_rc", "checker_rc", "seconds")}), flush=True)


if __name__ == "__main__":
    main()
