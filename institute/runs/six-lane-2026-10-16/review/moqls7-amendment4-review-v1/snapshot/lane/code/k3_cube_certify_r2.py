#!/usr/bin/env python3
"""Regenerate an UNSAT-screened original K3 cube, retain CNF, check binary DRAT.

Uses the controlled nonblocking-startup FIFO transport with native 3600-second limits,
15-minute persisted checkpoints and aggregate RSS/free-space safety stops.
No other scientific solver may overlap the two-child pipeline.
Usage: k3_cube_certify_r2.py A|B C311|C321|C411 OUTDIR SCREEN_RECEIPT
"""
import argparse
import json
import os

import k3_cubes
from proof_stream import run_pair
from gram_certify_r4 import sha

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("encoder", choices=("A", "B"))
    ap.add_argument("cube", choices=tuple(k3_cubes.CUBES))
    ap.add_argument("outdir")
    ap.add_argument("screen")
    a = ap.parse_args()
    with open(a.screen) as f:
        screen = json.load(f)
    assert screen["encoder"] == a.encoder and screen["cube"] == a.cube
    assert screen["status"] == "UNSAT exploratory" and screen["solver_rc"] == 20
    assert screen["safety_stop_reason"] is None
    # These are actual new matched controls, not presumed outcomes.
    controls = {}
    for label, rel in (("component_controls", "evidence/gram/review_controls_r1/summary.json"),
                       ("transport_controls", "evidence/gram/transport_controls_r2/summary.json")):
        path = os.path.join(LANE, rel)
        with open(path) as f:
            summary = json.load(f)
        assert summary["status"] == "PASS", path
        controls[label] = {"path": rel, "sha256": sha(path)}
    os.makedirs(a.outdir, exist_ok=True)
    prefix = os.path.join(a.outdir, a.encoder + "_" + a.cube)
    cnf, meta, receipt = prefix + ".cnf", prefix + ".meta.json", prefix + ".json"
    for path in (cnf, meta, receipt):
        if os.path.exists(path):
            raise FileExistsError(path)
    k3_cubes.make(a.encoder, a.cube, cnf, meta)
    assert sha(cnf) == screen["cnf_sha256"]
    command = (["cadical", "-q", "-t", "3600", cnf] if a.encoder == "A"
               else ["kissat", "-q", "-f", "--time=3600", cnf])
    result = run_pair(cnf, command, prefix, 3600, 3600)
    pins = {name: sha(os.path.join(HERE, name)) for name in
            ("gram_enc.py", "gram_encB.py", "gram_certify_r4.py", "k3_cubes.py", "proof_stream.py", "k3_cube_certify_r2.py")}
    result.update({"encoder": a.encoder, "cube": a.cube, "pins": pins, "controls": controls,
                   "screen_sha256": sha(a.screen), "metadata_sha256": sha(meta),
                   "scope": "Original covering cube only; whole K3 coverage/bridge acceptance is separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "verified_unsat", "solver_rc", "checker_rc", "seconds")}), flush=True)
    if not result["verified_unsat"]:
        raise SystemExit("Cube not certified; no exclusion claimed")


if __name__ == "__main__":
    main()
