#!/usr/bin/env python3
"""zp_batch.py -- run the RESTRICTED cyclic models of README amendment A2 one at a time (stdlib).

For each model Zp-rR-cC in the amendment's list, ordered by p*(R+C) descending (ties: larger p first, then larger R):
code/inv_cnf_v2.py MODEL OUTDIR/MODEL.cnf, then code/sat_tools.py run OUTDIR/MODEL.cnf kissat 300 OUTDIR/MODEL-kissat
(native kissat --time=300, no proof).  Appends one JSON line per model to OUTDIR/batch.jsonl; stops at the first SAT
(a witness is decoded and checked by sat_tools.py).  OUTDIR must not exist.  Usage: zp_batch.py OUTDIR
"""
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)


def models():
    out = []
    for r in (1, 2):
        for c in range(0, 6):
            out.append((5, r, c))
    for r in range(1, 5):
        for c in range(0, 10):
            out.append((3, r, c))
    for c in range(0, 15):
        out.append((2, 7, c))
    out.sort(key=lambda t: (-t[0] * (t[1] + t[2]), -t[0], -t[1]))
    return [f"Z{p}-r{r}-c{c}" for p, r, c in out]


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    py = [sys.executable, "-B"]
    with open(os.path.join(out, "batch.jsonl"), "x") as f:
        for mdl in models():
            cnf = os.path.join(out, f"{mdl}.cnf")
            g = subprocess.run(py + [os.path.join(CODE, "inv_cnf_v2.py"), mdl, cnf], capture_output=True, text=True)
            if g.returncode != 0:
                rec = {"model": mdl, "status": "GEN_ERROR", "stderr": g.stderr[-300:]}
            else:
                t0 = time.time()
                s = subprocess.run(py + [os.path.join(CODE, "sat_tools.py"), "run", cnf, "kissat", "300",
                                         os.path.join(out, f"{mdl}-kissat")], capture_output=True, text=True)
                rec = {"model": mdl, "rc": s.returncode, "wall_s": round(time.time() - t0, 2),
                       "status": {10: "SAT", 20: "UNSAT"}.get(s.returncode, "UNKNOWN"),
                       "summary": s.stdout.strip()[-300:]}
            rec["ended_host"] = time.strftime("%H:%M:%S")
            f.write(json.dumps(rec) + "\n")
            f.flush()
            print(json.dumps(rec), flush=True)
            if rec["status"] == "SAT":
                break
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
