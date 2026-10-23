#!/usr/bin/env python3
"""V11 qualification successor; WRITTEN ONLY. Fixed owned root, metadata only, no process launched.
Restores four explicitly injected helper negatives and five process-ownership negatives per parent correction
fabe57ab...4155a2. Busy2 reserves TWO CPU slots at threshold1; no busy3. All forking modes require individual negative
control GOs and are NOT admitted science children. Earlier v10/v9 packages remain frozen/unexecuted.
Usage: guard_qual_configs_v7.py SCENARIO ACTUAL_PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES
Creates a fresh fixed QROOT/scenario, config/preparation/optional pin fixture plus out/tmp through no-follow descriptors.
Parent exclusively writes /bin/date-stamped GO/authorization/audit/release, fresh stability receipt and captures.
"""
import hashlib
import json
import os
import stat
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v6-v11"
ITEM = "owned_supervisor_v11 restored ownership qualification"
CHILD = LANE + "/code/guard_qual_child_v8.py"
SUPERVISOR = LANE + "/code/owned_supervisor_v11.py"
CHILD_SHA = "002925444403fd9cecd6d0d724b207fb08eaa6bc51351f67604db3e94e69ba9b"
SUPERVISOR_SHA = "f43c7addf232cfe5e40de7e5622577fb7d883415ee0ad3e701887b376f97d90c"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
RESERVATION = 20971520
SC = {"go_unlisted": (60, 60, True, 2147483648), "ok": (60, 60, True, 2147483648),
      "rc_nonzero": (60, 60, True, 2147483648), "missing_output": (60, 60, True, 2147483648),
      "mutate_pin": (60, 60, True, 2147483648), "mutate_evidence": (60, 60, True, 2147483648),
      "stray_file": (60, 60, True, 2147483648), "deadline": (120, 10, False, 2147483648),
      "flood": (60, 60, False, 2147483648), "busy2": (60, 60, False, 2147483648),
      "rss": (60, 60, False, 268435456), "ignore": (60, 10, False, 2147483648),
      "identity": (60, 10, False, 2147483648), "date_fault": (60, 60, True, 2147483648),
      "helper_overrun": (60, 60, True, 2147483648), "helper_group": (60, 60, True, 2147483648),
      "helper_eof": (60, 60, True, 2147483648), "ownership_group": (40, 60, True, 2147483648),
      "ownership_slow": (40, 60, True, 2147483648), "ownership_fast": (40, 60, True, 2147483648),
      "ownership_double": (40, 60, True, 2147483648), "zombie_hold": (10, 60, True, 2147483648)}
FAULTS = {"identity": "identity_check_fails", "date_fault": "date_helper_fails",
          "helper_overrun": "helper_observation_overrun", "helper_group": "helper_group_unproved",
          "helper_eof": "helper_eof_unproved"}
NEGATIVE_PROCESS = {"busy2", "ownership_group", "ownership_slow", "ownership_fast", "ownership_double", "zombie_hold"}


def config_for(name, python, pysha, outstanding, lane_outstanding):
    life, wall, required, rss = SC[name]
    run, out = QROOT + "/" + name, QROOT + "/" + name + "/out"
    pins = [{"path": CHILD, "sha256": CHILD_SHA}, {"path": SUPERVISOR, "sha256": SUPERVISOR_SHA},
            {"path": python, "sha256": pysha}]
    if name == "mutate_pin":
        pins.append({"path": run + "/pinned-scratch.txt", "sha256": hashlib.sha256(FIXTURE).hexdigest()})
    call = 0.01 if name == "helper_overrun" else 0.2 if name in ("helper_group", "helper_eof") else 5.0
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
            "busy_limit": 1 if name == "busy2" else 2, "busy_cpu_fraction": 0.5,
            "cpu_slots": 2 if name == "busy2" else 1,
            "admission": {"go_path": run + "/go.json", "stability_receipt_path": run + "/stability.json",
                          "reservation_bytes": RESERVATION, "outstanding_reservations_bytes": outstanding,
                          "lane_outstanding_reservations_bytes": lane_outstanding},
            "helper_budget": {"max_calls": 8, "call_budget_s": call,
                              "term_grace_s": 0.5 if name in ("helper_group", "helper_eof") else 5.0},
            "fault_injection": {FAULTS[name]: True} if name in FAULTS else {}}


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
        raise ValueError("usage: SCENARIO ACTUAL_PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES")
    name, python = sys.argv[1:3]
    if name not in SC or not python.endswith("/Resources/Python.app/Contents/MacOS/Python") or os.path.realpath(python) != python:
        raise ValueError("scenario or actual Python.app path invalid")
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
        new = False
        try:
            os.mkdir("qual-pkg-v6-v11", dir_fd=lane)
            new = True
        except FileExistsError:
            pass
        qfd = os.open("qual-pkg-v6-v11", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=lane)
        if os.fstat(qfd).st_dev != os.fstat(lane).st_dev:
            raise ValueError("qualification volume mismatch")
        marker = (json.dumps({"kind": "v11-qualification-root", "supervisor_sha256": SUPERVISOR_SHA,
                              "child_sha256": CHILD_SHA}, sort_keys=True) + "\n").encode()
        if new:
            write_new(qfd, "package-root.json", marker)
        elif read_hash("package-root.json", 1 << 20, qfd) != hashlib.sha256(marker).hexdigest():
            raise ValueError("root marker mismatch")
        os.mkdir(name, dir_fd=qfd)
        rfd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=qfd)
        os.mkdir("out", dir_fd=rfd)
        os.mkdir("tmp", dir_fd=rfd)
        if name == "mutate_pin":
            write_new(rfd, "pinned-scratch.txt", FIXTURE)
        cfgsha = write_new(rfd, "config.json", data)
        entry = {k: cfg[k] for k in ("output_roots", "argv", "max_wall_s", "cpu_slots")}
        entry.update({k: cfg["admission"][k] for k in ("reservation_bytes", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes")})
        prep = {"kind": "v11-qualification-preparation", "scenario": name, "config_sha256": cfgsha,
                "supervisor_sha256": SUPERVISOR_SHA, "child_sha256": CHILD_SHA, "python": python, "python_sha256": pysha,
                "go_entry": entry, "cpu_slots": cfg["cpu_slots"], "reservation_bytes": RESERVATION,
                "ownership_negative": name in NEGATIVE_PROCESS, "helper_injection": name in FAULTS and name != "identity"}
        psha = write_new(rfd, "preparation.json", (json.dumps(prep, sort_keys=True, indent=1) + "\n").encode())
        os.fsync(rfd)
        os.fsync(qfd)
        print(json.dumps({"run": QROOT + "/" + name, "config_sha256": cfgsha,
                          "preparation_sha256": psha, "go_entry": entry}, sort_keys=True))
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
