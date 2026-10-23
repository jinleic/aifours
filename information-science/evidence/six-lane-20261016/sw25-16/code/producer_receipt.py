#!/usr/bin/env python3
"""Producer receipt for the pinned SW(25,16) witness (hashes only; no solving).

Usage (lane root): python3 -B code/producer_receipt.py OUT.json
Records: witness and short form (Z_5 circulant first rows) with the expander; model spec, CNF, map, encoder and
decoder code; kissat binary, version, exact command, seed (default) and time limit; solver stdout and the canonical
model (sorted true literals) hash; decoded file hash; replay record of controls/witness-v1.
"""
import hashlib
import json
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha(p):
    h = hashlib.sha256()
    with open(os.path.join(LANE, p) if not os.path.isabs(p) else p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    out = sys.argv[1]
    run = "runs/b2-z5-plain-v1/z5-plain"
    rec_run = json.load(open(os.path.join(LANE, run + "-kissat.json")))
    job = json.loads(open(os.path.join(LANE, "runs/b2-z5-plain-v1/batch.jsonl")).readline())
    true_lits = []
    for line in open(os.path.join(LANE, run + "-kissat.stdout")):
        if line.startswith("v "):
            true_lits += [int(t) for t in line.split()[1:] if int(t) != 0]
    canon = " ".join(map(str, sorted(true_lits, key=abs))) + "\n"
    kissat_path = subprocess.run(["which", "kissat"], capture_output=True, text=True).stdout.strip()
    kissat_real = os.path.realpath(kissat_path)
    files = ["certs/sw25-16-witness-v1.sw", "certs/sw25-16-witness-v1.circulant-first-rows.txt",
             "code/expand_circulant_array.py", "controls/witness-v1/expanded-from-first-rows.sw",
             run + ".spec.json", run + ".cnf", run + ".cnf.map.json", run + "-kissat.json", run + "-kissat.stdout",
             run + ".sw", "runs/b2-z5-plain-v1/batch.jsonl", "runs/b2-z5-plain-v1.jobs.json",
             "code/sw_models.py", "code/sw_cnf.py", "code/sw_decode.py", "code/sat_run.py", "code/batch.py",
             "code/sw_common.py", "code/verify_sw.py", "code/sw_check.c", "bin/sw_check",
             "controls/witness-v1/witness-controls.json", "controls/witness-v1/replay.cnf",
             "controls/witness-v1/replay-noproof.sw", "controls/witness-v1/replay-proof.sw"]
    rec = {
        "witness": "certs/sw25-16-witness-v1.sw",
        "witness_sha256": sha("certs/sw25-16-witness-v1.sw"),
        "model": {"args": job["job"]["model"], "cnf_opts": job["job"].get("cnf_opts", []),
                  "meaning": "G = <g>, g unsigned permutation of cycle type 5^5: point 5a+u -> 5a+((u+1) mod 5), "
                             "a,u in 0..4; Fix(G) = symmetric W with W[g i][g j] = W[i][j] (5x5 array of 5x5 "
                             "circulants)"},
        "solver": {"path": kissat_path, "realpath": kissat_real, "binary_sha256": sha(kissat_real),
                   "version": subprocess.run(["kissat", "--version"], capture_output=True, text=True).stdout.strip(),
                   "cmd_recorded": rec_run["cmd"], "time_limit_s": rec_run["time_limit_s"],
                   "seed": "default (no --seed option; kissat default seed 0)",
                   "proof_stream": "binary DRAT to a FIFO read by zstd (SAT run, proof unused); replay without the "
                                   "proof stream gives identical witness bytes (controls/witness-v1)",
                   "start": rec_run["start"], "end": rec_run["end"], "wall_s": rec_run["wall_s"],
                   "exit_code": rec_run["exit_code"]},
        "canonical_model_sha256": hashlib.sha256(canon.encode()).hexdigest(),
        "canonical_model_definition": "all literals from the solver's 'v' lines except 0, sorted by variable, "
                                      "space separated, final LF",
        "files_sha256": {p: sha(p) for p in files},
        "replay_recipe_lane_root": [
            "python3 -B code/sw_models.py cyc 25 16 5 0 X.spec.json",
            "python3 -B code/sw_cnf.py X.spec.json X.cnf",
            "kissat --time=3600 X.cnf  (exit 10; or: python3 -B code/sat_run.py kissat X.cnf 3600 X-kissat)",
            "python3 -B code/sw_decode.py X.cnf.map.json X-kissat.stdout X.sw",
            "short form: python3 -B code/expand_circulant_array.py expand "
            "certs/sw25-16-witness-v1.circulant-first-rows.txt Y.sw (identical bytes)"],
    }
    with open(out, "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("witness_sha256", "canonical_model_sha256")}))
    print(json.dumps(rec["solver"]))


if __name__ == "__main__":
    main()
