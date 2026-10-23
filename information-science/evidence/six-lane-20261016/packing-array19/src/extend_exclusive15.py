#!/usr/bin/env python3
"""[Guard15 margin variant; existing semantics/predicate unchanged.]
[Guard14 variant of the approved exclusive helper tool: identical all-token+bigmem exclusivity and sampled5GiB own-child guard; only per-stage fresh admission floor is12.2e9+64MiB. COUNT must remain0.]
Exclusive extend runs (REV11c, parent decision ~17:0x): memory-heavy placement enumerations (extend_p1q for M1,
extend_b for M2) run ALONE in the lane.
Preconditions checked: cycle2/tokens/COUNT is 0 (admissions paused by the operator) and the operator has stopped the
production runners at a stage boundary. The tool then acquires EXCLUSIVE flocks on every CPU token file t0..t7 and on
the bigmem lock (blocking, so any still-held stage is drained first), which makes it the only stage in the lane even if
COUNT were raised; it runs each enumeration through stream_check13.run_helper (helper lock, lane-RSS headroom check,
per-helper RSS guard 5 GiB sampled every second on its own registered child -- a sampled guard, not an instantaneous OS
bound; SIGTERM to that child only; wait until it exits; a cap trip is a failure even with rc 0), writes the placement
list to a temporary file renamed to ext.json only on success, records extend-receipt-<time>.json or
extend-failed-<time>.json next to it, and finally releases all locks. It never changes COUNT.
Usage: extend_exclusive.py m1 TAG [TAG ...] | m2 MS:B [MS:B ...]
"""
import fcntl
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check15 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(C2, "STOP-extend")])
    mode, items = sys.argv[1], sys.argv[2:]
    if open(os.path.join(S.TOK, "COUNT")).read().split()[0] != "0":
        raise SystemExit("COUNT must be 0 (admissions paused) before an exclusive extend")
    t0 = time.time()
    fds = []
    for name in ["t%d" % i for i in range(8)] + ["bigmem"]:
        fd = os.open(os.path.join(S.TOK, name), os.O_CREAT | os.O_RDWR)
        fcntl.flock(fd, fcntl.LOCK_EX)
        fds.append(fd)
    for fd in fds[:8]:
        os.ftruncate(fd, 0)
        os.pwrite(fd, ("%d %.3f extend-exclusive\n" % (os.getpid(), time.time())).encode(), 0)
    log = {"locks_acquired_after_s": round(time.time() - t0, 1), "start": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "items": []}
    print(json.dumps({"exclusive": True, "wait_s": log["locks_acquired_after_s"]}), flush=True)
    try:
        for it in items:
            if mode == "m1":
                d = os.path.join(C2, "part", it)
                spec = os.path.join(LANE, "cases19skel", "specs", it + ".json")
                cmd_of = lambda tmp: [VENV_PY, os.path.join(HERE, "extend_p1q.py"), spec, tmp, "1"]  # noqa: E731
            else:
                mi, bi = (int(x) for x in it.split(":"))
                d = os.path.join(C2, "m2part_drat", "ms%02d_b%05d" % (mi, bi))
                skp = os.path.join(C2, "skel-b", "skeletons-b-ms%02d.json" % mi)
                cmd_of = lambda tmp: [sys.executable, os.path.join(HERE, "extend_b.py"), skp, str(bi), tmp]  # noqa: E731
            os.makedirs(d, exist_ok=True)
            ext = os.path.join(d, "ext.json")
            if os.path.exists(ext):
                log["items"].append({"item": it, "skipped": "ext.json exists"})
                continue
            tmp = "%s.tmp-%d-%d" % (ext, os.getpid(), time.time_ns())
            ts0 = time.time()
            try:
                rc, out = S.run_helper(cmd_of(tmp))
            except S.AdmissionDenied as e:
                log["items"].append({"item": it, "admission_denied": str(e)})
                break
            info = dict(S.LAST_HELPER, out_tail=out[-300:], tmp=os.path.relpath(tmp, LANE), seconds=round(time.time() - ts0, 1),
                        tool="extend_exclusive15.py")
            if rc != 0 or info.get("cap_hit") or not os.path.exists(tmp):
                S.write_json(os.path.join(d, "extend-failed-%s.json" % time.strftime("%Y%m%dT%H%M%S")), info)
                log["items"].append({"item": it, "failed": True, "rc": rc, "cap_hit": info.get("cap_hit"), "peak_rss_kb": info.get("peak_rss_kb")})
            else:
                os.rename(tmp, ext)
                S.write_json(os.path.join(d, "extend-receipt-%s.json" % time.strftime("%Y%m%dT%H%M%S")), info)
                log["items"].append({"item": it, "ok": True, "peak_rss_kb": info.get("peak_rss_kb"), "seconds": info["seconds"]})
            print(json.dumps(log["items"][-1]), flush=True)
            if S.ABORT[0]:
                break
    finally:
        for fd in fds:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
        log["end"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        S.write_json(os.path.join(C2, "extend-exclusive-%s.json" % time.strftime("%Y%m%dT%H%M%S")), log)


if __name__ == "__main__":
    main()
