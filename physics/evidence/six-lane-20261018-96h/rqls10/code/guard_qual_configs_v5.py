#!/usr/bin/env python3
"""guard_qual_configs_v5: write ONE guard-qualification scenario directory and config for code/owned_supervisor_v9.py
(plan evidence/owned_supervisor_v9-guard-qualification-plan-v5.md). Supersedes guard_qual_configs_v4.py (never run)
after the Codex review of package v4 (RUN/review/rqls10-guard-qualification-v4-codex-v1.prompt.stdout.txt, findings 4
and 6): one fixed fresh qualification root strictly inside the lane, every argument validated BEFORE anything is
created, exact per-scenario layout (config, tmp, stability receipt, parent GO, captured supervisor summary, checker
output and parent records all in RUN, outside the supervisor output root RUN/out), the v9 schema (helper_budget,
cpu_slots, faults identity_check_fails / date_helper_fails), busy2 with busy_limit 1 and cpu_slots 2 (both CPU slots
reserved), mutate_pin fixture created here. Metadata only: mkdir (QROOT if absent, RUN, RUN/out, RUN/tmp), exclusive
files RUN/config.json and (mutate_pin) RUN/pinned-scratch.txt; starts no process; never deletes.
Usage: guard_qual_configs_v5.py SCENARIO CHILD_SHA PY_REAL PY_SHA OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES
Prints one JSON line: config path and sha256, the exact GO entry for a per-invocation GO file at RUN/go.json (the parent
writes it; for go_unlisted the parent writes a GO that does NOT list this config), the reservation the parent must hold
(bytes and CPU slots) and the fixed paths of the remaining invocation artifacts.
"""
import hashlib, json, os, stat, sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v5"
CHILD = LANE + "/code/guard_qual_child_v6.py"
ITEM = "owned_supervisor_v9 guard qualification"
RESERVATION = 20971520
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
SC = {
    # name: (mode, life_s, max_wall_s, fault, out_required, rss_trip_bytes, target)
    "date_fault": ("ok", 5, 60, "date_helper_fails", True, 2147483648, None),
    "go_unlisted": ("ok", 5, 60, None, True, 2147483648, None),
    "ok": ("ok", 5, 60, None, True, 2147483648, None),
    "rc_nonzero": ("rc_nonzero", 5, 60, None, True, 2147483648, None),
    "missing_output": ("no_output", 5, 60, None, True, 2147483648, None),
    "mutate_pin": ("mutate_pin", 5, 60, None, True, 2147483648, "PIN"),
    "mutate_evidence": ("mutate_evidence", 5, 60, None, True, 2147483648, "LAUNCH_RECORD"),
    "stray_file": ("stray_file", 5, 60, None, True, 2147483648, None),
    "deadline": ("sleep", 120, 10, None, False, 2147483648, None),
    "flood": ("flood", 60, 60, None, False, 2147483648, None),
    "busy": ("busy2", 60, 60, None, False, 2147483648, None),
    "rss": ("rss", 60, 60, None, False, 268435456, None),
    "zombie_hold": ("zombie_hold", 10, 60, None, True, 2147483648, None),
    "escape_slow": ("escape_slow", 40, 60, None, True, 2147483648, None),
    "escape_fast": ("escape_fast", 40, 60, None, True, 2147483648, None),
    "double_fork_escape": ("double_fork_escape", 40, 60, None, True, 2147483648, None),
    "ignore": ("ignore_term", 60, 10, None, False, 2147483648, None),
    "identity": ("sleep", 60, 10, "identity_check_fails", False, 2147483648, None),
}


def real_dir_chain(d):
    cur = ""
    for comp in os.path.abspath(d).split("/")[1:]:
        cur = cur + "/" + comp
        try:
            st = os.lstat(cur)
        except OSError:
            return False
        if stat.S_ISLNK(st.st_mode) or not stat.S_ISDIR(st.st_mode):
            return False
    return True


def sha_regular(path, max_bytes):
    st0 = os.lstat(path)
    if not stat.S_ISREG(st0.st_mode) or st0.st_size > max_bytes:
        raise ValueError("not a bounded regular file: %s" % path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        h, got = hashlib.sha256(), 0
        while got < st0.st_size:
            chunk = os.read(fd, min(1 << 20, st0.st_size - got))
            if not chunk:
                raise ValueError("short read: %s" % path)
            h.update(chunk)
            got += len(chunk)
        if os.read(fd, 1):
            raise ValueError("grew while read: %s" % path)
    finally:
        os.close(fd)
    return h.hexdigest()


def is_hex64(x):
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def config_for(name, py, py_sha, child_sha, outstanding, lane_outstanding):
    """the exact config dict for a scenario (the checker reconstructs it with the same function body)."""
    mode, life, wall, fault, req, rss_trip, target = SC[name]
    run = os.path.join(QROOT, name)
    outd = os.path.join(run, "out")
    out = os.path.join(outd, "child-out.json")
    launch = os.path.join(outd, "launch.json")
    pins = [{"path": CHILD, "sha256": child_sha}, {"path": py, "sha256": py_sha}]
    argv = [py, "-I", "-B", CHILD, mode, out, str(life)]
    if target == "PIN":
        pins.append({"path": os.path.join(run, "pinned-scratch.txt"), "sha256": hashlib.sha256(FIXTURE).hexdigest()})
        argv.append(os.path.join(run, "pinned-scratch.txt"))
    elif target == "LAUNCH_RECORD":
        argv.append(launch)
    return {
        "item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE, "argv": argv,
        "env": {"TMPDIR": os.path.join(run, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
                "OMP_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "stdout": os.path.join(outd, "stdout.txt"), "stderr": os.path.join(outd, "stderr.txt"),
        "stdout_cap_bytes": 1048576, "stderr_cap_bytes": 1048576,
        "outputs": [{"path": out, "required": req}],
        "launch_record": launch, "samples": os.path.join(outd, "samples.jsonl"),
        "samples_cap_bytes": 2097152, "receipt": os.path.join(outd, "supervisor-receipt.json"),
        "settlement_record": os.path.join(outd, "settlement.json"), "output_roots": [outd], "pins": pins,
        "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0, "max_chunk_seconds": 10800,
        "owned_compute_settled_by_epoch": 1792731393.0, "rss_trip_bytes": rss_trip, "free_trip_bytes": 12200000000,
        "output_trip_bytes": 9437184, "launch_free_min_bytes": 12200000000, "lane_roots": [LANE],
        "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 5.0,
        "busy_limit": 1 if name == "busy" else 2, "cpu_slots": 2 if name == "busy" else 1,
        "busy_cpu_fraction": 0.5, "rss_projection_bytes": 67108864,
        "admission": {"go_path": os.path.join(run, "go.json"), "reservation_bytes": RESERVATION,
                      "outstanding_reservations_bytes": outstanding,
                      "lane_outstanding_reservations_bytes": lane_outstanding,
                      "stability_receipt_path": os.path.join(run, "stability.json"), "stability_max_age_s": 300},
        "helper_budget": {"max_calls": 8, "call_budget_s": 5.0, "term_grace_s": 5.0},
        "fault_injection": ({fault: True} if fault else {})}


def main():
    if len(sys.argv) != 7:
        sys.stderr.write("usage: SCENARIO CHILD_SHA PY_REAL PY_SHA OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES\n")
        return 2
    name, child_sha, py, py_sha, outst, lane_outst = sys.argv[1:7]
    try:
        if name not in SC:
            raise ValueError("unknown scenario %r" % name)
        if not (is_hex64(child_sha) and is_hex64(py_sha)):
            raise ValueError("sha256 arguments must be 64 lowercase hex digits")
        if not (py.startswith("/") and os.path.abspath(py) == py and os.path.realpath(py) == py):
            raise ValueError("PY_REAL must be a normalized absolute real path")
        if sha_regular(CHILD, 1 << 20) != child_sha or sha_regular(py, 1 << 30) != py_sha:
            raise ValueError("child or interpreter sha256 mismatch")
        outstanding, lane_outstanding = int(outst), int(lane_outst)
        if outstanding < 0 or lane_outstanding < 0:
            raise ValueError("outstanding reservations must be nonnegative")
        if not real_dir_chain(LANE):
            raise ValueError("lane is not a real directory chain")
        run = os.path.join(QROOT, name)
        if os.path.lexists(run):
            raise ValueError("scenario directory exists: %s" % run)
    except (ValueError, OSError) as ex:
        sys.stderr.write("REFUSED %r\n" % ex)
        return 2
    if not os.path.lexists(QROOT):
        os.mkdir(QROOT)
    if not real_dir_chain(QROOT):
        sys.stderr.write("REFUSED qualification root is not a real directory\n")
        return 2
    os.mkdir(run)
    os.mkdir(os.path.join(run, "out"))
    os.mkdir(os.path.join(run, "tmp"))
    cfg = config_for(name, py, py_sha, child_sha, outstanding, lane_outstanding)
    if SC[name][6] == "PIN":
        fd = os.open(os.path.join(run, "pinned-scratch.txt"), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
        try:
            if os.write(fd, FIXTURE) != len(FIXTURE):
                raise OSError("short fixture write")
            os.fsync(fd)
        finally:
            os.close(fd)
    data = (json.dumps(cfg, indent=1, sort_keys=True) + "\n").encode("utf-8")
    fd = os.open(os.path.join(run, "config.json"), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        view = memoryview(data)
        while view:
            k = os.write(fd, view)
            if k <= 0:
                raise OSError("zero-progress write")
            view = view[k:]
        os.fsync(fd)
    finally:
        os.close(fd)
    go_entry = {"output_roots": cfg["output_roots"], "argv": cfg["argv"], "max_wall_s": cfg["max_wall_s"],
                "cpu_slots": cfg["cpu_slots"], "reservation_bytes": RESERVATION,
                "outstanding_reservations_bytes": outstanding, "lane_outstanding_reservations_bytes": lane_outstanding}
    print(json.dumps({"scenario": name, "config": os.path.join(run, "config.json"),
                      "config_sha256": hashlib.sha256(data).hexdigest(), "item": ITEM, "go_entry": go_entry,
                      "list_in_go": name != "go_unlisted",
                      "parent_reservation": {"bytes": RESERVATION, "cpu_slots": cfg["cpu_slots"]},
                      "paths": {"go": cfg["admission"]["go_path"], "stability": cfg["admission"]["stability_receipt_path"],
                                "summary_capture": os.path.join(run, "supervisor-summary.txt"),
                                "checker_output": os.path.join(run, "check.json"),
                                "parent_records_prefix": os.path.join(run, "parent-")}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
