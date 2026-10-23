#!/usr/bin/env python3
"""Three-phase decode (README §4, 10:11 memory note): rebuild the colouring CNF of a `--no-solve`
run from the arguments recorded in RUNDIR/summary.json, check that the retained kissat model in LOG
satisfies it (pipeline2.py --model-from) and write the certificate into the fresh OUTDIR.  The CNF
sha256 rebuilt here is compared with the one recorded by the build run.
Usage: decode_run.py RUNDIR LOG OUTDIR"""
import lane_guard  # noqa: F401

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    rundir, log, out = sys.argv[1:4]
    summ = json.load(open(os.path.join(rundir, "summary.json")))
    a = summ["args"]
    cmd = [sys.executable, os.path.join(HERE, "pipeline2.py"), out, "--group", a["group"], "--g", str(a["g"]),
           "--res", a["res"], "--avoid", a["avoid"], "--rows-from", a["rows_from"], "--workers", "1",
           "--model-from", log, "--stop-on-first"]
    for flag, key in (("--strengthen", "strengthen"), ("--hybrid", "hybrid"), ("--symbreak", "symbreak"),
                      ("--skip-lemma-p", "skip_lemma_p")):
        if a.get(key):
            cmd.append(flag)
    if a.get("profile"):
        cmd += ["--profile", a["profile"]]
    print(" ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout[-2000:], r.stderr[-2000:])
    built = [c for s in summ["samples"] for c in s.get("colourings", [])]
    new = json.load(open(os.path.join(out, "summary.json")))
    rebuilt = [c for s in new["samples"] for c in s.get("colourings", [])]
    print("CNF sha256 recorded", built[0]["col_cnf_sha256"], "rebuilt", rebuilt[0]["col_cnf_sha256"],
          "equal", built[0]["col_cnf_sha256"] == rebuilt[0]["col_cnf_sha256"])
    print("certificates", new["certificates"])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
