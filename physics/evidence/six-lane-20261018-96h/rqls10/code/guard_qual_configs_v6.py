#!/usr/bin/env python3
"""Qualification PACKAGE v5, v10 binding: metadata-only config writer (no subprocesses).
Supersedes frozen/unrun v9-bound draft guard_qual_configs_v5.py. The earlier file was cited by a snapshot and is not
rewritten. This new file forms the requested package v5 bound to supervisor v10, not a launch authorization.
Usage: guard_qual_configs_v6.py SCENARIO PYTHON_APP_REAL OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES
All arguments/source pins are validated before creation. Fixed QROOT strictly inside the lane; no arbitrary base path.
Retained directory fds and no-follow component traversal for mkdir/creation. Existing scenario directories are refused.
Creates only RUN/{config.json,preparation.json,tmp/,out/} plus the exact mutate_pin fixture. Parent creates GO,
stability, captures, approval, audit and release files exclusively in RUN (outside out/). busy is SINGLE-process with
busy_limit0/cpu_slots1; <=2 global lane cap unchanged. No fork/zombie/escape or /bin/date-helper scenario is offered.
Prints configuration and preparation digests plus the exact per-invocation GO entry (without a stability digest yet).
The parent supplies that digest and raw not_after_epoch AFTER its fresh gate; no broad GO or automatic chaining.
"""
import hashlib
import json
import os
import stat
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v5-v10"
ITEM = "owned_supervisor_v10 single-process qualification"
CHILD = LANE + "/code/guard_qual_child_v7.py"
SUPERVISOR = LANE + "/code/owned_supervisor_v10.py"
CHILD_SHA = "80e61ed42145e797fbc9bacb5ba120e75af54dd87c8873a503f925e77eb1329f"
SUPERVISOR_SHA = "fc6ef48a041d82d8253f158c996626f62776965f8947eb80c322a71a07620a9d"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
RESERVATION = 20971520
# scenario: lifetime from test module entry, supervisor wall, required child output, RSS trip
SC = {"go_unlisted": (60, 60, True, 2147483648), "ok": (60, 60, True, 2147483648),
      "rc_nonzero": (60, 60, True, 2147483648), "missing_output": (60, 60, True, 2147483648),
      "mutate_pin": (60, 60, True, 2147483648), "mutate_evidence": (60, 60, True, 2147483648),
      "stray_file": (60, 60, True, 2147483648), "deadline": (120, 10, False, 2147483648),
      "flood": (60, 60, False, 2147483648), "busy": (60, 60, False, 2147483648),
      "rss": (60, 60, False, 268435456), "ignore": (60, 10, False, 2147483648),
      "identity": (60, 10, False, 2147483648)}


def config_for(name, python, pysha, outstanding, lane_outstanding):
    life, wall, required, rss = SC[name]
    run, out = QROOT + "/" + name, QROOT + "/" + name + "/out"
    pins = [{"path": CHILD, "sha256": CHILD_SHA}, {"path": SUPERVISOR, "sha256": SUPERVISOR_SHA},
            {"path": python, "sha256": pysha}]
    if name == "mutate_pin":
        pins.append({"path": run + "/pinned-scratch.txt", "sha256": hashlib.sha256(FIXTURE).hexdigest()})
    return {"item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE,
            "argv": [python, "-I", "-B", CHILD, name, str(life)],
            "env": {"TMPDIR": run + "/tmp", "PYTHONDONTWRITEBYTECODE": "1"},
            "stdout": out + "/stdout.txt", "stderr": out + "/stderr.txt", "stdout_cap_bytes": 1048576,
            "stderr_cap_bytes": 1048576, "samples": out + "/samples.jsonl", "samples_cap_bytes": 2097152,
            "launch_record": out + "/launch.json", "receipt": out + "/supervisor-receipt.json",
            "settlement_record": out + "/settlement.json", "outputs": [{"path": out + "/child-out.json", "required": required}],
            "output_roots": [out], "pins": pins, "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0,
            "max_chunk_seconds": 10800, "owned_compute_settled_by_epoch": 1792731393.0,
            "rss_trip_bytes": rss, "rss_projection_bytes": 67108864, "free_trip_bytes": 12200000000,
            "launch_free_min_bytes": 12200000000, "output_trip_bytes": 9437184, "lane_roots": [LANE],
            "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 5.0,
            "busy_limit": 0 if name == "busy" else 2, "busy_cpu_fraction": 0.5, "cpu_slots": 1,
            "admission": {"go_path": run + "/go.json", "stability_receipt_path": run + "/stability.json",
                          "reservation_bytes": RESERVATION, "outstanding_reservations_bytes": outstanding,
                          "lane_outstanding_reservations_bytes": lane_outstanding},
            "fault_injection": {"identity_check_fails": True} if name == "identity" else {}}


def directory(path):
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for c in path.lstrip("/").split("/"):
            if c in ("", ".", ".."):
                raise ValueError("invalid directory component")
            nxt = os.open(c, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def read_hash(path, cap, dir_fd=None):
    deadline = time.monotonic() + 30
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=dir_fd)
    h = hashlib.sha256()
    try:
        s = os.fstat(fd)
        if not stat.S_ISREG(s.st_mode) or s.st_size > cap:
            raise ValueError("not a bounded regular file")
        remaining = s.st_size
        while remaining:
            b = os.read(fd, min(remaining, 1 << 20))
            if not b:
                raise OSError("short read")
            h.update(b)
            remaining -= len(b)
            if time.monotonic() > deadline:
                raise OSError("hash budget")
        if os.read(fd, 1):
            raise OSError("file grew")
    finally:
        os.close(fd)
    if time.monotonic() > deadline:
        raise OSError("hash completion budget")
    return h.hexdigest()


def write_new(fd, name, data):
    out = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=fd)
    try:
        view = memoryview(data)
        while view:
            n = os.write(out, view)
            if n <= 0:
                raise OSError("zero-progress write")
            view = view[n:]
        os.fsync(out)
    finally:
        os.close(out)
    return hashlib.sha256(data).hexdigest()


def main():
    if len(sys.argv) != 5:
        raise ValueError("usage: SCENARIO PYTHON_APP_REAL OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES")
    name, python = sys.argv[1:3]
    if name not in SC or not python.endswith("/Resources/Python.app/Contents/MacOS/Python") or os.path.realpath(python) != python:
        raise ValueError("scenario invalid or not the actual non-launcher Python.app executable")
    outstanding, lane_outstanding = (int(x) for x in sys.argv[3:5])
    if not (0 <= outstanding <= 1 << 60 and 0 <= lane_outstanding <= 10737418240):
        raise ValueError("reservation range")
    if read_hash(CHILD, 1 << 20) != CHILD_SHA or read_hash(SUPERVISOR, 1 << 20) != SUPERVISOR_SHA:
        raise ValueError("source pin mismatch")
    pysha = read_hash(python, 64 << 20)
    cfg = config_for(name, python, pysha, outstanding, lane_outstanding)
    data = (json.dumps(cfg, sort_keys=True, indent=1, allow_nan=False) + "\n").encode()
    lane = directory(LANE)
    qfd = rfd = None
    try:
        # All semantic arguments and pins have passed. No arbitrary BASE_DIR is accepted.
        created_root = False
        try:
            os.mkdir("qual-pkg-v5-v10", dir_fd=lane)
            created_root = True
        except FileExistsError:
            pass
        qfd = os.open("qual-pkg-v5-v10", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=lane)
        if os.fstat(qfd).st_dev != os.fstat(lane).st_dev:
            raise ValueError("qualification root on another filesystem")
        rootbytes = (json.dumps({"kind": "v10-qualification-root", "supervisor_sha256": SUPERVISOR_SHA,
                                 "child_sha256": CHILD_SHA}, sort_keys=True) + "\n").encode()
        if created_root:
            write_new(qfd, "package-root.json", rootbytes)
        elif read_hash("package-root.json", 1 << 20, qfd) != hashlib.sha256(rootbytes).hexdigest():
            raise ValueError("existing qualification root is not this package's root")
        os.mkdir(name, dir_fd=qfd)
        rfd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=qfd)
        os.mkdir("out", dir_fd=rfd)
        os.mkdir("tmp", dir_fd=rfd)
        if name == "mutate_pin":
            write_new(rfd, "pinned-scratch.txt", FIXTURE)
        cfgsha = write_new(rfd, "config.json", data)
        entry = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots")}
        entry.update({k: cfg["admission"][k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
        prep = {"kind": "v10-qualification-preparation", "scenario": name, "config_sha256": cfgsha,
                "supervisor_sha256": SUPERVISOR_SHA, "child_sha256": CHILD_SHA, "python": python, "python_sha256": pysha,
                "go_entry": entry, "cpu_slots": 1, "reservation_bytes": RESERVATION,
                "expected_go_listing": "omit config deliberately" if name == "go_unlisted" else "exactly this one config"}
        prepsha = write_new(rfd, "preparation.json", (json.dumps(prep, sort_keys=True, indent=1) + "\n").encode())
        os.fsync(rfd)
        os.fsync(qfd)
        print(json.dumps({"run": QROOT + "/" + name, "config_sha256": cfgsha,
                          "preparation_sha256": prepsha, "go_entry": entry}, sort_keys=True))
    finally:
        if rfd is not None:
            os.close(rfd)
        if qfd is not None:
            os.close(qfd)
        os.close(lane)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write("PREPARATION_REFUSED %r\n" % e)
        sys.exit(2)
