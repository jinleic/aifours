#!/usr/bin/env python3
"""owned_supervisor_v2: run ONE child in its own session/process group; launch record before compute; fail-closed guard.

v2 fixes (parent HOLD on v1): every post-spawn path runs inside try/finally that settles the child (one identity-checked
SIGTERM to its process group, bounded wait settle_s, no escalation) and writes a receipt; SIGTERM/SIGINT/SIGHUP to the
supervisor set a cooperative cancel flag handled the same way; an unreadable live RSS, free-space or output reading is
a trip (never a silent pass); the deadline is enforced on BOTH the monotonic clock and the absolute epoch wall clock
(survives sleep/resume), and launch is refused unless start + max_wall <= min(start + max_chunk - 120,
owned_compute_settled_by - 180). The child must read the line "GO" from stdin before computing; if the supervisor dies
before GO, the pipe closes and the child exits on EOF.

Config JSON (argv[1]): lane, argv, env, stdout, stderr, outputs, launch_record, samples, receipt, pins [{path, sha256}],
max_wall_s, rss_trip_bytes, free_trip_bytes, output_trip_bytes, launch_free_min_bytes, sample_s, settle_s,
max_chunk_seconds, owned_compute_settled_by_epoch. Standard library only.
"""
import hashlib, json, os, signal, subprocess, sys, time

CANCEL = [None]


def _cancel(signum, frame):
    if CANCEL[0] is None:
        CANCEL[0] = signum


def date():
    try:
        return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip()
    except Exception as ex:
        return "DATE_UNAVAILABLE " + repr(ex)


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
    return sum(os.path.getsize(p) for p in paths if os.path.exists(p))


def main():
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, _cancel)
    cfg_path = os.path.abspath(sys.argv[1])
    cfg = json.load(open(cfg_path))
    lane = cfg["lane"]
    rec = {"config": cfg_path, "config_sha256": sha(cfg_path), "supervisor": os.path.abspath(__file__),
           "supervisor_sha256": sha(os.path.abspath(__file__)), "supervisor_pid": os.getpid()}
    pins_ok = all(os.path.isfile(p["path"]) and not os.path.islink(p["path"]) and sha(p["path"]) == p["sha256"] for p in cfg["pins"])
    free0 = free_bytes(lane)
    w0 = time.time()
    abs_end = w0 + cfg["max_wall_s"]
    fit_limit = min(w0 + cfg["max_chunk_seconds"] - 120, cfg["owned_compute_settled_by_epoch"] - 180)
    fit_ok = abs_end <= fit_limit
    if not pins_ok or free0 < cfg["launch_free_min_bytes"] or not fit_ok or CANCEL[0] is not None:
        rec.update({"status": "NOT_LAUNCHED", "pins_ok": pins_ok, "free": free0, "fit_ok": fit_ok, "abs_end_epoch": abs_end,
                    "fit_limit_epoch": fit_limit, "cancel": CANCEL[0], "at": date()})
        with open(cfg["receipt"], "x") as fh:
            json.dump(rec, fh, indent=1)
        return 10
    fo = open(cfg["stdout"], "x")
    fe = open(cfg["stderr"], "x")
    start_date = date()
    t0 = time.monotonic()
    w0 = time.time()
    abs_end = w0 + cfg["max_wall_s"]
    child = subprocess.Popen(cfg["argv"], cwd=lane, env=dict(cfg["env"]), stdin=subprocess.PIPE, stdout=fo, stderr=fe,
                             start_new_session=True)
    pid = child.pid
    st = {"pgid": None, "trips": [], "signalled_mono": None, "signal_at": None, "max_rss": 0, "min_free": free0, "samples": 0,
          "error": None, "status": None, "go_sent": False}
    samples = None
    try:
        st["pgid"] = os.getpgid(pid)
        launch = {"pid": pid, "pgid": st["pgid"], "argv": cfg["argv"],
                  "argv_sha256": hashlib.sha256(json.dumps(cfg["argv"]).encode()).hexdigest(), "cwd": lane, "env": cfg["env"],
                  "start_date": start_date, "start_epoch": w0, "abs_end_epoch": abs_end, "max_wall_s": cfg["max_wall_s"],
                  "settle_s": cfg["settle_s"], "fit_limit_epoch": fit_limit, "pins": cfg["pins"], "free_at_launch": free0,
                  "supervisor_pid": os.getpid(), "supervisor_sha256": rec["supervisor_sha256"], "config_sha256": rec["config_sha256"],
                  "outputs": cfg["outputs"], "receipt": cfg["receipt"]}
        with open(cfg["launch_record"], "x") as fh:
            json.dump(launch, fh, indent=1)
        samples = open(cfg["samples"], "x")
        if CANCEL[0] is None:
            child.stdin.write(b"GO\n")
            st["go_sent"] = True
        child.stdin.close()
        while True:
            rc = child.poll()
            if rc is not None:
                st["status"] = "EXITED"
                break
            now, wnow = time.monotonic(), time.time()
            trip = None
            try:
                fr = free_bytes(lane)
            except Exception:
                fr, trip = None, "FREE_UNREADABLE"
            rs = rss_bytes(pid)
            if rs is None:
                if child.poll() is not None:
                    st["status"] = "EXITED"
                    break
                trip = trip or "RSS_UNREADABLE"
            try:
                ob = out_bytes(cfg["outputs"])
            except Exception:
                ob, trip = None, trip or "OUTPUT_UNREADABLE"
            if fr is not None:
                st["min_free"] = min(st["min_free"], fr)
            if rs is not None:
                st["max_rss"] = max(st["max_rss"], rs)
            if trip is None:
                if CANCEL[0] is not None:
                    trip = "SUPERVISOR_CANCEL_%d" % CANCEL[0]
                elif rs > cfg["rss_trip_bytes"]:
                    trip = "RSS"
                elif fr < cfg["free_trip_bytes"]:
                    trip = "FREE"
                elif ob > cfg["output_trip_bytes"]:
                    trip = "OUTPUT"
                elif now - t0 > cfg["max_wall_s"] or wnow > abs_end:
                    trip = "DEADLINE"
            samples.write(json.dumps({"t": round(now - t0, 2), "w": round(wnow, 1), "free": fr, "rss": rs, "out": ob, "trip": trip}) + "\n")
            samples.flush()
            st["samples"] += 1
            if trip is not None and st["signalled_mono"] is None:
                st["trips"].append({"trip": trip, "t": round(now - t0, 2), "at": date()})
                term_once(child, pid, st)
            if st["signalled_mono"] is not None and time.monotonic() - st["signalled_mono"] > cfg["settle_s"]:
                st["status"] = "UNSETTLED_AFTER_SIGTERM"
                break
            time.sleep(cfg["sample_s"])
    except BaseException as ex:
        st["error"] = repr(ex)
    finally:
        try:
            if not st["go_sent"]:
                try:
                    child.stdin.close()
                except Exception:
                    pass
            if child.poll() is None and st["status"] != "UNSETTLED_AFTER_SIGTERM":
                if st["signalled_mono"] is None:
                    st["trips"].append({"trip": "FINALLY_SETTLE" + ("_ERROR" if st["error"] else ""), "at": date()})
                    term_once(child, pid, st)
                limit = (st["signalled_mono"] or time.monotonic()) + cfg["settle_s"]
                while child.poll() is None and time.monotonic() < limit:
                    time.sleep(1)
                st["status"] = "EXITED_AFTER_SIGTERM" if child.poll() is not None else "UNSETTLED_AFTER_SIGTERM"
        finally:
            write_receipt(cfg, rec, st, child, pid, start_date, w0, t0, fo, fe, samples)
    return 0 if st.get("settlement") == "SETTLED" else 11


def term_once(child, pid, st):
    if st["signalled_mono"] is not None:
        return
    try:
        ident = child.poll() is None and st["pgid"] is not None and os.getpgid(pid) == st["pgid"]
    except Exception:
        ident = False
    st["identity_ok_at_signal"] = ident
    if ident:
        os.killpg(st["pgid"], signal.SIGTERM)
        st["signalled_mono"] = time.monotonic()
        st["signal_at"] = date()


def write_receipt(cfg, rec, st, child, pid, start_date, w0, t0, fo, fe, samples):
    for f in (fo, fe, samples):
        try:
            if f is not None:
                f.close()
        except Exception:
            pass
    rc = child.poll()
    members = group_members(st["pgid"]) if st["pgid"] is not None else None
    outs = {}
    for p in cfg["outputs"] + [cfg["samples"], cfg["launch_record"]]:
        try:
            if os.path.exists(p):
                outs[p] = {"bytes": os.path.getsize(p), "sha256": sha(p)}
        except Exception as ex:
            outs[p] = {"error": repr(ex)}
    settled = (rc is not None and members == [] and st["status"] in ("EXITED", "EXITED_AFTER_SIGTERM") and st["error"] is None)
    st["settlement"] = "SETTLED" if settled else "UNSETTLED"
    rec.update({"status": st["status"], "returncode": rc, "pid": pid, "pgid": st["pgid"], "start_date": start_date, "start_epoch": w0,
                "end_date": date(), "end_epoch": time.time(), "wall_s": round(time.monotonic() - t0, 2), "trips": st["trips"],
                "sigterm_sent": st["signalled_mono"] is not None, "signal_at": st["signal_at"],
                "identity_ok_at_signal": st.get("identity_ok_at_signal"), "error": st["error"], "max_rss_bytes": st["max_rss"],
                "min_free_bytes": st["min_free"], "samples": st["samples"], "outputs": outs, "group_members_after": members,
                "go_sent": st["go_sent"], "cancel_signal": CANCEL[0], "settlement": st["settlement"]})
    try:
        with open(cfg["receipt"], "x") as fh:
            json.dump(rec, fh, indent=1)
    except Exception as ex:
        sys.stderr.write("RECEIPT_WRITE_FAILED %r %s\n" % (ex, json.dumps(rec)))


if __name__ == "__main__":
    sys.exit(main())
