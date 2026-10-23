"""runlib.py (parent moqls7-k1-parent-check-v1): run a pinned subprocess, record argv, exit, wall time, child
rusage (ru_maxrss bytes on macOS) and stdout/stderr files (created exclusively)."""
import datetime, hashlib, os, resource, subprocess, time


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def now():
    return datetime.datetime.now().astimezone().isoformat()


def run(argv, cwd, out_path, err_path, stdin_path=None, env=None):
    t0 = time.time()
    started = now()
    fin = open(stdin_path, "rb") if stdin_path else subprocess.DEVNULL
    with open(out_path, "xb") as fo, open(err_path, "xb") as fe:
        p = subprocess.Popen(argv, cwd=cwd, stdout=fo, stderr=fe, stdin=fin, env=env)
        _, status, ru = os.wait4(p.pid, 0)
        p.returncode = os.waitstatus_to_exitcode(status) if hasattr(os, "waitstatus_to_exitcode") else (
            (status >> 8) if (status & 0x7f) == 0 else -(status & 0x7f))
    if stdin_path:
        fin.close()
    rc = resource.getrusage(resource.RUSAGE_CHILDREN)
    return {"argv": argv, "cwd": cwd, "started": started, "finished": now(), "wall_s": round(time.time() - t0, 3),
            "exit": p.returncode, "child_maxrss_bytes": ru.ru_maxrss, "child_utime_s": ru.ru_utime,
            "all_waited_descendants_maxrss_bytes": rc.ru_maxrss,
            "stdout": os.path.basename(out_path), "stdout_sha256": sha_file(out_path),
            "stderr": os.path.basename(err_path), "stderr_sha256": sha_file(err_path)}
