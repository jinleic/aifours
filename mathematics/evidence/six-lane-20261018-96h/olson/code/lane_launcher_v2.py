#!/usr/bin/env python3
"""lane_launcher_v2 (ContinueOlson).  Supersedes v1 (never used): the child is spawned BLOCKED on a stdin gate, the
exclusive pre-compute ownership record (PID, PGID, argv sha256, source sha256, cwd, absolute end bound, free bytes) is
written, and only then the gate byte is sent; the child is reaped and a settlement record written.
Usage (from the lane root): python3 -B code/lane_launcher_v2.py RECORD_PREFIX MAX_WALL_S -- script.py args...
The child runs as: python3 -B -c GATE script.py args...  (GATE reads one byte from stdin, then runpy-runs script.py)."""
import hashlib, json, os, subprocess, sys, time, datetime

GATE = ("import sys, runpy; b = sys.stdin.buffer.read(1); "
        "sys.exit(97) if b != b'G' else None; sys.argv = sys.argv[1:]; "
        "runpy.run_path(sys.argv[0], run_name='__main__')")

def stamp():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

def main():
    prefix, max_wall = sys.argv[1], float(sys.argv[2])
    assert sys.argv[3] == "--"
    script_argv = sys.argv[4:]
    argv = [sys.executable, "-B", "-c", GATE] + script_argv
    cwd = os.getcwd()
    env = dict(os.environ)
    env.update({"TMPDIR": os.path.join(cwd, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
                "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"})
    st = os.statvfs(cwd)
    free = st.f_bavail * st.f_frsize
    srcs = {a: hashlib.sha256(open(a, "rb").read()).hexdigest()
            for a in script_argv if a.endswith(".py") and os.path.isfile(a)}
    out = open(prefix + ".child.stdout", "x")
    t_start = time.time()
    proc = subprocess.Popen(argv, cwd=cwd, env=env, start_new_session=True, stdin=subprocess.PIPE,
                            stdout=out, stderr=subprocess.STDOUT)
    pre = {"record": "pre-compute ownership (child blocked on stdin gate)", "at": stamp(), "owner": "ContinueOlson",
           "cwd": cwd, "argv": argv, "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(),
           "source_sha256": srcs, "launcher_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version.split()[0], "pid": proc.pid, "pgid": os.getpgid(proc.pid), "launcher_pid": os.getpid(),
           "abs_child_end_bound_epoch": t_start + max_wall,
           "abs_child_end_bound_local": datetime.datetime.fromtimestamp(t_start + max_wall).astimezone().isoformat(timespec="seconds"),
           "free_bytes_at_launch": free,
           "env_overrides": {k: env[k] for k in ("TMPDIR", "PYTHONDONTWRITEBYTECODE", "OMP_NUM_THREADS")}}
    with open(prefix + ".pre.json", "x") as f:
        f.write(json.dumps(pre, indent=1) + "\n")
    proc.stdin.write(b"G")
    proc.stdin.close()
    rc = proc.wait()
    out.close()
    post = {"record": "settlement", "at": stamp(), "pid": proc.pid, "returncode": rc,
            "wall_s": round(time.time() - t_start, 3), "reaped": True,
            "child_stdout_sha256": hashlib.sha256(open(prefix + ".child.stdout", "rb").read()).hexdigest()}
    with open(prefix + ".post.json", "x") as f:
        f.write(json.dumps(post, indent=1) + "\n")
    print(json.dumps(post))

if __name__ == "__main__":
    main()
