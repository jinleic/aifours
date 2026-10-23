#!/usr/bin/env python3
"""Sequential batch: model spec -> CNF -> solver (native limit) -> decode (SAT) / DRAT check (UNSAT with proof).

Usage (lane root): python3 -B code/batch.py JOBS.json OUTDIR
JOBS.json: list of {"name", "model": [sw_models.py args], "cnf_opts": [...], "solver": "kissat"|"cadical",
                    "time": seconds, "proof": bool, "stop_on_sat": bool (default true), "expect": optional}
OUTDIR must not exist. Writes OUTDIR/batch.jsonl (created with mode x, one line appended per finished job) and
per job NAME.spec.json, NAME.cnf(+.map.json), NAME-SOLVER.{stdout,json[,drat.zst]}, NAME.sw (SAT),
NAME-SOLVER.drat-check.json (UNSAT with proof).  One process at a time (the solver is the only busy child).
"""
import json
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, "-B"]


def host_date():
    return subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def main():
    jobs = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.mkdir(out)
    log = open(os.path.join(out, "batch.jsonl"), "x")
    log.close()
    for job in jobs:
        name = job["name"]
        P = lambda s: os.path.join(out, name + s)  # noqa: E731
        rec = {"name": name, "start": host_date(), "job": job}
        rc, so, se = run(PY + [os.path.join(LANE, "code/sw_models.py")] + job["model"] + [P(".spec.json")])
        rec["spec"] = so
        if rc != 0:
            rec["error"] = "spec: " + se[-500:]
        else:
            rc, so, se = run(PY + [os.path.join(LANE, "code/sw_cnf.py"), P(".spec.json"), P(".cnf")] +
                             job.get("cnf_opts", []))
            if rc != 0:
                rec["error"] = "cnf: " + se[-500:]
            else:
                rec["cnf"] = json.loads(so)
                sargs = [job["solver"], P(".cnf"), str(job["time"]), P("-" + job["solver"])]
                if job.get("proof"):
                    sargs.append("--proof")
                for x in job.get("solver_extra", []):
                    sargs += ["--extra", x]
                if "seed" in job:
                    sargs += ["--seed", str(job["seed"])]
                rc, so, se = run(PY + [os.path.join(LANE, "code/sat_run.py")] + sargs)
                rec["solve"] = json.loads(so) if rc == 0 and so else {"error": se[-500:]}
                verdict = rec["solve"].get("verdict")
                if verdict == "SAT":
                    rc, so, se = run(PY + [os.path.join(LANE, "code/sw_decode.py"), P(".cnf.map.json"),
                                           P("-" + job["solver"] + ".stdout"), P(".sw")])
                    rec["decode"] = json.loads(so) if rc == 0 and so else {"error": se[-500:]}
                elif verdict == "UNSAT" and job.get("proof"):
                    rc, so, se = run(PY + [os.path.join(LANE, "code/drat_check.py"), P(".cnf"),
                                           P("-" + job["solver"] + ".drat.zst"),
                                           P("-" + job["solver"] + ".drat-check.json")])
                    rec["drat"] = json.loads(so) if rc == 0 and so else {"error": se[-500:]}
        rec["end"] = host_date()
        with open(os.path.join(out, "batch.jsonl"), "a") as f:
            f.write(json.dumps(rec) + "\n")
        v = rec.get("solve", {}).get("verdict")
        print(name, v, rec.get("solve", {}).get("wall_s"), rec.get("decode", {}).get("verify_sw_py", ""),
              rec.get("drat", {}).get("verified", ""), rec.get("error", ""), flush=True)
        if v == "SAT" and job.get("stop_on_sat", True) and job.get("expect") != "SAT":
            print("STOP: first SAT in batch", flush=True)
            break


if __name__ == "__main__":
    main()
