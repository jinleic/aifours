#!/usr/bin/env python3
"""Run one search command and write an exclusive JSON record (lane cfr33).

Usage: run_cmd.py OUTDIR -- CMD [ARGS...]
OUTDIR is created with os.mkdir (must not exist). Writes OUTDIR/start.json, OUTDIR/stdout.txt, OUTDIR/record.json.
No Python-side timeout: the command must carry its own (native/internal) limit. SIGTERM/SIGINT to this process are
forwarded to the child as SIGTERM, then we wait for it. Verdict: exit 10 and a line 's SATISFIABLE' -> FOUND;
otherwise UNKNOWN (with exit code recorded). sha256 of the executable (first argument, if a file) is recorded.
"""
import hashlib, json, os, resource, signal, subprocess, sys, time


def host_time():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"], capture_output=True, text=True).stdout.strip()


def main():
    outdir = sys.argv[1]
    assert sys.argv[2] == "--"
    cmd = sys.argv[3:]
    os.mkdir(outdir)
    exe = cmd[0]
    exe_sha = hashlib.sha256(open(exe, "rb").read()).hexdigest() if os.path.isfile(exe) else None
    start = {"command": cmd, "cwd": os.getcwd(), "exe_sha256": exe_sha, "host_time_start": host_time(), "runner_pid": os.getpid()}
    with open(os.path.join(outdir, "start.json"), "x") as fh:
        json.dump(start, fh, indent=1)
    t0 = time.time()
    out = open(os.path.join(outdir, "stdout.txt"), "x")
    child = subprocess.Popen(cmd, stdout=out, stderr=subprocess.STDOUT)
    sig = {"s": None}

    def fwd(signum, frame):
        sig["s"] = signum
        try:
            child.send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass
    signal.signal(signal.SIGTERM, fwd)
    signal.signal(signal.SIGINT, fwd)
    rc = child.wait()
    out.close()
    ru = resource.getrusage(resource.RUSAGE_CHILDREN)
    text = open(os.path.join(outdir, "stdout.txt")).read()
    found = rc == 10 and "s SATISFIABLE" in text.splitlines()
    rec = dict(start)
    rec.update({"host_time_end": host_time(), "wall_s": round(time.time() - t0, 3), "exit_code": rc,
                "verdict": "FOUND(candidate; checkers decide)" if found else "UNKNOWN", "stopped_by_signal": sig["s"],
                "child_user_s": ru.ru_utime, "child_maxrss_bytes(macOS ru_maxrss)": ru.ru_maxrss,
                "stdout_sha256": hashlib.sha256(text.encode()).hexdigest()})
    with open(os.path.join(outdir, "record.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("verdict", "exit_code", "wall_s")}))


if __name__ == "__main__":
    main()
