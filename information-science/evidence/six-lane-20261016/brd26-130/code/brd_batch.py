#!/usr/bin/env python3
"""brd_batch.py -- run already generated model CNFs one at a time with kissat (README 1.5), stdlib only.

Usage: brd_batch.py RUNDIR SECONDS MODEL [MODEL ...]
For each MODEL in the given order: code/brd_run.py RUNDIR/MODEL.cnf SECONDS RUNDIR/MODEL-kissat-tSECONDS (kissat
native --time).  Appends one JSON line per model to RUNDIR/batch-tSECONDS.jsonl (created exclusively) and stops at
the first SAT (a witness candidate is decoded and checked by brd_run.py).  One solver process at a time.
"""
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    if len(argv) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    rundir, secs, models = argv[1], int(argv[2]), argv[3:]
    with open(os.path.join(rundir, f"batch-t{secs}.jsonl"), "x") as f:
        for m in models:
            t0 = time.time()
            p = subprocess.run([sys.executable, "-B", os.path.join(CODE, "brd_run.py"),
                                os.path.join(rundir, f"{m}.cnf"), str(secs),
                                os.path.join(rundir, f"{m}-kissat-t{secs}")], capture_output=True, text=True)
            rec = {"model": m, "rc": p.returncode, "status": {10: "SAT", 20: "UNSAT"}.get(p.returncode, "UNKNOWN"),
                   "wall_s": round(time.time() - t0, 2), "summary": p.stdout.strip()[-400:],
                   "started_host": time.strftime("%H:%M:%S", time.localtime(t0)),
                   "ended_host": time.strftime("%H:%M:%S")}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            print(json.dumps(rec), flush=True)
            if rec["status"] == "SAT":
                break
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
