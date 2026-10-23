"""Fixed-net K2 batch (README §3): for each of the 39 E–W 3-MOLS(8) representatives, build FK2 with encoders A8r2
(CaDiCaL) and B8r2 (kissat): classical squares = the representative (rows 0 = 0..7), quantum squares 1, 2 with
(P1)-(P4) in the row-0 frame. Optional --proof: certificate run through proof_run.py (zstd DRAT + drat-trim check).
Fail-closed: any status other than UNSAT is reported; never deletes; fresh output directory.

python -B run_fixed_k2.py --nets ../evidence/k2_fixed/ew_nets.json --outdir ../evidence/k2_fixed/all_v1 [--proof]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
DT = os.path.normpath(os.path.join(HERE, "..", "..", "moqls7-problem16", "env", "drat-trim", "drat-trim"))


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(cmd):
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r, round(time.time() - t0, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--time", type=int, default=1800)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    nets = json.load(open(a.nets))["nets"]
    rec = {"argv": sys.argv, "python": sys.version, "script_sha256": sha(__file__), "nets_sha256": sha(a.nets),
           "enc_a_sha256": sha(os.path.join(HERE, "enc8_a2.py")), "enc_b_sha256": sha(os.path.join(HERE, "enc8_b2.py")),
           "results": []}
    for item in nets:
        tag = item["tag"]
        sq = os.path.join(a.outdir, tag + ".squares.json")
        with open(sq, "x") as fh:
            json.dump(item["squares"], fh)
        for enc in ("a", "b"):
            cnf = os.path.join(a.outdir, "%s_%s.cnf" % (enc, tag))
            if enc == "a":
                cmd = [PY, "-B", os.path.join(HERE, "enc8_a2.py"), "--mode", "fixed", "--slopes", "", "--squares", sq,
                       "--quantum", "12", "--p4", "12", "--cnf", cnf, "--map", cnf + ".map.json"]
            else:
                cmd = [PY, "-B", os.path.join(HERE, "enc8_b2.py"), "--mode", "fixed", "--slopes", "", "--squares", sq,
                       "--quantum", "12", "--p4", "12", "--cnf", cnf]
            r, _ = run(cmd)
            item_rec = {"net": tag, "encoder": enc, "encode_exit": r.returncode, "encode_stderr": r.stderr[-500:]}
            if r.returncode == 0:
                item_rec["cnf_sha256"] = sha(cnf)
                if a.proof:
                    solver = "cadical" if enc == "a" else "kissat"
                    proof = cnf + ".drat.zst"
                    r2, secs = run([PY, "-B", os.path.join(HERE, "proof_run.py"), "solve", "--solver", solver,
                                    "--cnf", cnf, "--proof", proof, "--time", str(a.time),
                                    "--receipt", cnf + ".solve.json"])
                    s = json.load(open(cnf + ".solve.json"))
                    item_rec.update({"status": s["status"], "solve_secs": s["secs"], "proof_sha256": s["proof_sha256"],
                                     "proof_bytes_compressed": s["proof_bytes_compressed"]})
                    if s["status"] == "UNSAT":
                        run([PY, "-B", os.path.join(HERE, "proof_run.py"), "check", "--cnf", cnf, "--proof", proof,
                             "--drat-trim", DT, "--receipt", cnf + ".check.json"])
                        c = json.load(open(cnf + ".check.json"))
                        item_rec.update({"verified": c["verified"], "check_secs": c["secs"]})
                else:
                    if enc == "a":
                        r2, secs = run(["cadical", "-q", "-t", str(a.time), cnf])
                    else:
                        r2, secs = run(["kissat", "-q", "--time=%d" % a.time, cnf])
                    item_rec.update({"status": {10: "SAT", 20: "UNSAT"}.get(r2.returncode, "UNKNOWN(%d)" % r2.returncode),
                                     "solve_secs": secs})
            rec["results"].append(item_rec)
            print(json.dumps({k: item_rec.get(k) for k in ("net", "encoder", "status", "solve_secs", "verified")}),
                  flush=True)
    rec["all_unsat"] = all(x.get("status") == "UNSAT" for x in rec["results"])
    if a.proof:
        rec["all_verified"] = all(x.get("verified") for x in rec["results"])
    rec["count"] = len(rec["results"])
    with open(os.path.join(a.outdir, "RECEIPT.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("count", "all_unsat") + (("all_verified",) if a.proof else ())}))
    if not rec["all_unsat"]:
        raise SystemExit("NOT ALL UNSAT")


if __name__ == "__main__":
    main()
