#!/usr/bin/env python3
"""Certify an already-screened covering K3 cube; regenerate and retain its CNF.

Use the frozen cube wrapper and the proven r4 stdin-binary transport/monitor.
Two native children only; no exploratory solver may overlap this pipeline.
Usage: k3_cube_certify.py A|B C311|C321|C411 OUTDIR SCREEN_RECEIPT
"""
import argparse
import json
import os
import subprocess
import time

from gram_certify_r4 import CHECKER, monitor, now, rss, sha
import k3_cubes

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
    st = os.statvfs(LANE)
    if st.f_bavail * st.f_frsize < 12000000000:
        raise RuntimeError("Global free-space floor reached")
    os.makedirs(a.outdir, exist_ok=True)
    label = a.encoder + "_" + a.cube
    prefix = os.path.join(a.outdir, label)
    paths = {name: prefix + suffix for name, suffix in
             (("cnf", ".cnf"), ("meta", ".meta.json"), ("receipt", ".json"),
              ("fifo", ".drat.fifo"), ("solver", ".solver.log"), ("checker", ".checker.log"))}
    for path in paths.values():
        if os.path.exists(path):
            raise FileExistsError(path)
    k3_cubes.make(a.encoder, a.cube, paths["cnf"], paths["meta"])
    assert sha(paths["cnf"]) == screen["cnf_sha256"]
    os.mkfifo(paths["fifo"])
    if not rss(os.getpid()):
        raise RuntimeError("Native RSS sampler unavailable")
    solver = (["cadical", "-q", "-t", "1800", paths["cnf"], paths["fifo"]] if a.encoder == "A"
              else ["kissat", "-q", "-f", "--time=1800", paths["cnf"], paths["fifo"]])
    checker = [CHECKER, paths["cnf"], "-i", "-t", "3600"]
    start, t0 = now(), time.monotonic()
    with open(paths["solver"], "x") as sl, open(paths["checker"], "x") as cl:
        solve = subprocess.Popen(solver, stdout=sl, stderr=subprocess.STDOUT)
        with open(paths["fifo"], "rb") as proof:
            check = subprocess.Popen(checker, stdin=proof, stdout=cl, stderr=subprocess.STDOUT)
        peak, reason = monitor(solve, check, 5520)
    with open(paths["checker"]) as f:
        statuses = [line.strip() for line in f.read().replace("\r", "\n").splitlines()
                    if line.strip().startswith("s ")]
    ok = (reason is None and solve.returncode == 20 and check.returncode == 0 and statuses == ["s VERIFIED"])
    pins = {name: sha(os.path.join(HERE, name)) for name in
            ("gram_enc.py", "gram_encB.py", "gram_certify_r4.py", "k3_cubes.py", "k3_cube_certify.py")}
    pins["drat-trim"] = sha(CHECKER)
    pins["drat-trim.c"] = sha(CHECKER + ".c")
    rec = {"encoder": a.encoder, "cube": a.cube, "started_at": start, "finished_at": now(),
           "seconds": round(time.monotonic() - t0, 3), "verified_unsat": ok,
           "solver_rc": solve.returncode, "checker_rc": check.returncode, "checker_status_lines": statuses,
           "safety_stop_reason": reason, "peak_sampled_aggregate_rss_bytes": peak,
           "cnf_sha256": sha(paths["cnf"]), "metadata_sha256": sha(paths["meta"]),
           "screen_sha256": sha(a.screen), "solver_log_sha256": sha(paths["solver"]),
           "checker_log_sha256": sha(paths["checker"]), "pins": pins,
           "solver_command": solver, "checker_command": checker,
           "proof_storage": "FIFO-only; regenerated CNF and both logs retained"}
    with open(paths["receipt"], "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps(rec), flush=True)
    if not ok:
        raise SystemExit("Cube was not certified")


if __name__ == "__main__":
    main()
