#!/usr/bin/env python3
"""Parent-authorized direct B/C321 or B/C411 proof attempt, no prior B screen claimed.

Reuse unchanged frozen encoders/cubes and tested in-memory regeneration. Each
stage has an outer12.2e9-plus-growth gate; no CNF/proof copies. Both native limits
are3600 seconds and exactly one solver+checker pipeline runs. UNKNOWN is retained.
Usage: k3_direct_B_r4.py C321|C411 OUTDIR
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
                   "authority": "Parent23:56 release/prioritization of direct original B/C321 then B/C411 certification",
                   "controls": controls, "driver_sha256": sha(__file__),
                   "scope": "This original B cube only; parent whole-proof acceptance remains separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "status", "verified_unsat", "solver_rc", "checker_rc", "seconds")}), flush=True)


if __name__ == "__main__":
    main()
