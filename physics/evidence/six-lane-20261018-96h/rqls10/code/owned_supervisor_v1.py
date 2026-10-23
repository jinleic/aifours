#!/usr/bin/env python3
"""owned_supervisor_v1: run ONE child under its own process group with a launch record written before compute.

Config JSON (argv[1]) keys: lane, argv (list), env (dict), stdout, stderr, outputs (list of paths to size-check),
launch_record, samples, receipt, pins (list of {path, sha256}), max_wall_s, rss_trip_bytes, free_trip_bytes,
output_trip_bytes, launch_free_min_bytes, sample_s, settle_s.
Protocol: verify pins and launch free space; open stdout/stderr exclusively; start the child with stdin=PIPE in a new
session (PGID = PID); write the launch record (exclusive) with PID, PGID, argv sha256, cwd, /bin/date start and the
absolute wall deadline; only then send "GO\n" to the child's stdin. Every sample_s seconds: child alive?, free bytes
(statvfs of lane), child RSS (/bin/ps -o rss=), total output bytes, wall vs deadline; samples appended to an exclusive
file. On the first trip (RSS, free, output, deadline) send exactly ONE SIGTERM to the child's process group after an
identity check (child not yet reaped, getpgid(pid) == recorded PGID), then wait at most settle_s seconds; no escalation.
Receipt (exclusive): exit status, trips, max RSS, min free, output sizes and sha256, process-group census after exit,
settlement verdict SETTLED / UNSETTLED. Standard library only.
"""
import hashlib, json, os, signal, subprocess, sys, time


def date():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip()


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def rss_bytes(pid):
    r = subprocess.run(["/bin/ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True)
    t = r.stdout.strip()
    return int(t) * 1024 if (r.returncode == 0 and t.isdigit()) else None


def group_members(pgid):
    r = subprocess.run(["/bin/ps", "-A", "-o", "pid=,pgid="], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    out = []
    for line in r.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].isdigit() and int(parts[1]) == pgid:
            out.append(int(parts[0]))
    return out


def out_bytes(paths):
    tot = 0
    for p in paths:
        try:
            tot += os.path.getsize(p)
        except OSError:
            pass
    return tot


def main():
    cfg = json.load(open(sys.argv[1]))
    lane = cfg["lane"]
    rec = {"config": os.path.abspath(sys.argv[1]), "config_sha256": sha(sys.argv[1]), "supervisor_sha256": sha(os.path.abspath(__file__))}
    pin_ok = all(sha(p["path"]) == p["sha256"] for p in cfg["pins"])
    free0 = free_bytes(lane)
    if not pin_ok or free0 < cfg["launch_free_min_bytes"]:
        rec.update({"status": "NOT_LAUNCHED", "pins_ok": pin_ok, "free": free0, "at": date()})
        with open(cfg["receipt"], "x") as fh:
            json.dump(rec, fh, indent=1)
        return 10
    fo = open(cfg["stdout"], "x")
    fe = open(cfg["stderr"], "x")
    env = dict(cfg["env"])
    start_date = date()
    t0 = time.monotonic()
    child = subprocess.Popen(cfg["argv"], cwd=lane, env=env, stdin=subprocess.PIPE, stdout=fo, stderr=fe, start_new_session=True)
    pid = child.pid
    pgid = os.getpgid(pid)
    deadline = t0 + cfg["max_wall_s"]
    launch = {"pid": pid, "pgid": pgid, "argv": cfg["argv"], "argv_sha256": hashlib.sha256(json.dumps(cfg["argv"]).encode()).hexdigest(),
              "cwd": lane, "env": env, "start": start_date, "max_wall_s": cfg["max_wall_s"], "settle_s": cfg["settle_s"],
              "pins": cfg["pins"], "free_at_launch": free0, "supervisor_pid": os.getpid(), "supervisor_sha256": rec["supervisor_sha256"],
              "config_sha256": rec["config_sha256"]}
    with open(cfg["launch_record"], "x") as fh:
        json.dump(launch, fh, indent=1)
    child.stdin.write(b"GO\n")
    child.stdin.close()
    samples = open(cfg["samples"], "x")
    trips = []
    signalled_at = None
    max_rss, min_free, n_samples = 0, free0, 0
    status = None
    while True:
        rc = child.poll()
        now = time.monotonic()
        fr = free_bytes(lane)
        rs = rss_bytes(pid) if rc is None else None
        ob = out_bytes(cfg["outputs"])
        min_free = min(min_free, fr)
        if rs:
            max_rss = max(max_rss, rs)
        samples.write(json.dumps({"t": round(now - t0, 2), "free": fr, "rss": rs, "out": ob, "alive": rc is None}) + "\n")
        samples.flush()
        n_samples += 1
        if rc is not None:
            status = "EXITED"
            break
        trip = None
        if rs is not None and rs > cfg["rss_trip_bytes"]:
            trip = "RSS"
        elif fr < cfg["free_trip_bytes"]:
            trip = "FREE"
        elif ob > cfg["output_trip_bytes"]:
            trip = "OUTPUT"
        elif now > deadline:
            trip = "DEADLINE"
        if trip and signalled_at is None:
            ident_ok = child.poll() is None and os.getpgid(pid) == pgid
            trips.append({"trip": trip, "t": round(now - t0, 2), "identity_ok": ident_ok, "at": date()})
            if ident_ok:
                os.killpg(pgid, signal.SIGTERM)
                signalled_at = now
        if signalled_at is not None and now - signalled_at > cfg["settle_s"]:
            status = "UNSETTLED_AFTER_SIGTERM"
            break
        time.sleep(cfg["sample_s"])
    samples.close()
    end_date = date()
    rc = child.poll()
    fo.close()
    fe.close()
    members = group_members(pgid)
    outs = {}
    for p in cfg["outputs"]:
        if os.path.exists(p):
            outs[p] = {"bytes": os.path.getsize(p), "sha256": sha(p)}
    settled = (status == "EXITED" and rc is not None and members == [])
    rec.update({"status": status, "returncode": rc, "pid": pid, "pgid": pgid, "start": start_date, "end": end_date,
                "wall_s": round(time.monotonic() - t0, 2), "trips": trips, "sigterm_sent": signalled_at is not None,
                "max_rss_bytes": max_rss, "min_free_bytes": min_free, "samples": n_samples, "outputs": outs,
                "group_members_after": members, "settlement": "SETTLED" if settled else "UNSETTLED"})
    with open(cfg["receipt"], "x") as fh:
        json.dump(rec, fh, indent=1)
    return 0 if settled else 11


if __name__ == "__main__":
    sys.exit(main())
