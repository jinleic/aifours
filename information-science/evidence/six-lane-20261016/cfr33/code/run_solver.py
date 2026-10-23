#!/usr/bin/env python3
"""Run one SAT solver call with a native time limit and write an exclusive JSON record (lane cfr33).

Usage: run_solver.py OUTDIR CNF SOLVER SEED SECONDS [PROOF_PATH]
  SOLVER in {kissat, cadical}. Native limits: kissat --time=SECONDS, cadical -t SECONDS. No Python-side timeout.
  OUTDIR is created with os.mkdir (must not exist). Writes OUTDIR/start.json, OUTDIR/solver.out, OUTDIR/record.json.
  SIGTERM/SIGINT to this process are forwarded to the solver, then we wait for it (cooperative stop -> UNKNOWN).
  Verdict: exit 10 + 's SATISFIABLE' -> SAT; exit 20 + 's UNSATISFIABLE' -> UNSAT (a DRAT check is separate);
  anything else -> UNKNOWN.
"""
import hashlib, json, os, resource, signal, subprocess, sys, time


def host_time():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"], capture_output=True, text=True).stdout.strip()


def main():
    outdir, cnf, solver, seed, secs = sys.argv[1:6]
    proof = sys.argv[6] if len(sys.argv) > 6 else None
    os.mkdir(outdir)
    cnf_sha = hashlib.sha256(open(cnf, "rb").read()).hexdigest()
    if solver == "kissat":
        cmd = ["kissat", "--seed=%d" % int(seed), "--time=%d" % int(secs), cnf]
        if proof:
            cmd += [proof]
    elif solver == "cadical":
        cmd = ["cadical", "--seed=%d" % int(seed), "-t", str(int(secs)), cnf]
        if proof:
            cmd += [proof]
    else:
        raise SystemExit("unknown solver")
    start = {"cnf": cnf, "cnf_sha256": cnf_sha, "command": cmd, "host_time_start": host_time(),
             "runner_pid": os.getpid(), "time_limit_s": int(secs), "seed": int(seed)}
    with open(os.path.join(outdir, "start.json"), "x") as fh:
        json.dump(start, fh, indent=1)
    t0 = time.time()
    out = open(os.path.join(outdir, "solver.out"), "x")
    child = subprocess.Popen(cmd, stdout=out, stderr=subprocess.STDOUT)
    stopped = {"signal": None}

    def forward(signum, frame):
        stopped["signal"] = signum
        try:
            child.send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass
    signal.signal(signal.SIGTERM, forward)
    signal.signal(signal.SIGINT, forward)
    rc = child.wait()
    out.close()
    wall = time.time() - t0
    ru = resource.getrusage(resource.RUSAGE_CHILDREN)
    status = None
    for line in open(os.path.join(outdir, "solver.out")):
        if line.startswith("s "):
            status = line.strip()
    if rc == 10 and status == "s SATISFIABLE":
        verdict = "SAT"
    elif rc == 20 and status == "s UNSATISFIABLE":
        verdict = "UNSAT(solver claim; DRAT check separate)"
    else:
        verdict = "UNKNOWN"
    rec = dict(start)
    rec.update({"host_time_end": host_time(), "wall_s": round(wall, 3), "exit_code": rc, "status_line": status,
                "verdict": verdict, "stopped_by_signal": stopped["signal"],
                "child_user_s": ru.ru_utime, "child_sys_s": ru.ru_stime,
                "child_maxrss_bytes(macOS ru_maxrss)": ru.ru_maxrss,
                "solver_out_sha256": hashlib.sha256(open(os.path.join(outdir, "solver.out"), "rb").read()).hexdigest()})
    with open(os.path.join(outdir, "record.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("verdict", "exit_code", "wall_s", "cnf_sha256")}))


if __name__ == "__main__":
    main()
