#!/usr/bin/env python3
"""lane_launcher_v1 (ContinueOlson): exclusive pre-compute ownership record, Popen in its own session, reap, receipt.
Usage: python3 -B code/lane_launcher_v1.py RECORD_PREFIX MAX_WALL_S -- argv...   (run from the lane root)."""
import hashlib, json, os, subprocess, sys, time, datetime

def stamp():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

def main():
    prefix, max_wall = sys.argv[1], float(sys.argv[2])
    assert sys.argv[3] == "--"
    argv = sys.argv[4:]
    cwd = os.getcwd()
    env = dict(os.environ)
    env.update({"TMPDIR": os.path.join(cwd, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
                "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"})
    st = os.statvfs(cwd)
    free = st.f_bavail * st.f_frsize
    srcs = {a: hashlib.sha256(open(a, "rb").read()).hexdigest() for a in argv if a.endswith(".py") and os.path.isfile(a)}
    t_start = time.time()
    proc = subprocess.Popen(argv, cwd=cwd, env=env, start_new_session=True,
                            stdout=open(prefix + ".child.stdout", "x"), stderr=subprocess.STDOUT)
    pre = {"record": "pre-compute ownership", "at": stamp(), "owner": "ContinueOlson", "cwd": cwd, "argv": argv,
           "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(), "source_sha256": srcs,
           "pid": proc.pid, "pgid": os.getpgid(proc.pid), "launcher_pid": os.getpid(),
           "abs_child_end_bound_epoch": t_start + max_wall,
           "abs_child_end_bound_local": datetime.datetime.fromtimestamp(t_start + max_wall).astimezone().isoformat(timespec="seconds"),
           "free_bytes_at_launch": free, "env_overrides": {k: env[k] for k in ("TMPDIR", "PYTHONDONTWRITEBYTECODE", "OMP_NUM_THREADS")}}
    with open(prefix + ".pre.json", "x") as f:
        f.write(json.dumps(pre, indent=1) + "\n")
    rc = proc.wait()
    post = {"record": "settlement", "at": stamp(), "pid": proc.pid, "returncode": rc,
            "wall_s": round(time.time() - t_start, 3), "reaped": True}
    with open(prefix + ".post.json", "x") as f:
        f.write(json.dumps(post, indent=1) + "\n")
    print(json.dumps(post))

if __name__ == "__main__":
    main()
