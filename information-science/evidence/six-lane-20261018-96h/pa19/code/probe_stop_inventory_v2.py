#!/usr/bin/env python3
"""PA19 96h lane probe 1 (v2; v1 is an unused, never-run draft with an inaccurate no-child docstring): read-only inventory of inherited STOP/HALT/VETO/QUARANTINE markers.

Scope: metadata-only, standard library only; the only child processes are /bin/date reads for
host-clock timestamps (no solver/checker/enumerator child); no writes outside
LANE/evidence/probes. Never opens FIFOs or non-regular files for reading.
Admission (fail closed): fresh statvfs free >= 12.2e9 + 16 MiB, and no NEW-round STOP/HALT
marker in LANE/control or RUN/control. Inherited old-round markers are the OBJECT of this
inventory; they are hashed and recorded, never moved, removed or reinterpreted here.
Output: one exclusive-created JSON file (argv[1]); refuses if it exists.
"""
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD_LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
OLD_RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16"
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
PAT = re.compile(r"(stop|halt|veto|quarantine|\.flag$|retire)", re.IGNORECASE)
MAX_SECONDS = 280.0
T0 = time.monotonic()


def host_clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True,
                          text=True, check=True, stdin=subprocess.DEVNULL).stdout.strip()


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def new_round_markers():
    found = []
    for d in (os.path.join(LANE, "control"), os.path.join(RUN, "control")):
        for name in sorted(os.listdir(d)):
            if re.match(r"(?i)^(stop|halt)", name) or "HALT" in name:
                found.append(os.path.join(d, name))
    return found


def sha256_regular(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def classify(rel):
    if rel.startswith("src/"):
        return "SOURCE_FILE_NOT_MARKER"
    if rel.startswith("scratch/fifo/"):
        return "CONTROL_FIFO_FIXTURE"
    control_tokens = ("-controls-", "required-controls", "smoke11/", "smoke12/",
                      "enumeration-guard-smoke", "supervise-v")
    if any(t in rel for t in control_tokens):
        return "CONTROL_FIXTURE"
    if rel.startswith("archive/"):
        return "RETIRED_BY_RECORDED_MOVE"
    if rel.count("/") == 1 and rel.startswith("cycle2/"):
        return "LIVE_OLD_ROUND_PATH"
    return "OTHER_OLD_ROUND_PATH"


def entry(root, full):
    rel = os.path.relpath(full, root)
    st = os.lstat(full)
    rec = {"rel": rel, "mode": stat.filemode(st.st_mode), "bytes": st.st_size,
           "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime)),
           "class": classify(rel)}
    if stat.S_ISREG(st.st_mode):
        rec["sha256"] = sha256_regular(full)
        with open(full, "rb") as f:
            rec["head"] = f.read(600).decode("utf-8", "replace")
    elif stat.S_ISFIFO(st.st_mode):
        rec["type"] = "fifo_not_opened"
    elif stat.S_ISDIR(st.st_mode):
        rec["type"] = "directory"
    elif stat.S_ISLNK(st.st_mode):
        rec["type"] = "symlink_not_followed"
    else:
        rec["type"] = "other_not_opened"
    return rec


def walk(root, only_prefix=None):
    out = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        if time.monotonic() - T0 > MAX_SECONDS:
            raise SystemExit("REFUSED: probe self-budget exceeded during walk; no output written")
        rel_dir = os.path.relpath(dirpath, root)
        if only_prefix and not (rel_dir == "." or any(rel_dir.startswith(p) for p in only_prefix)):
            dirnames[:] = [d for d in dirnames if any(d.startswith(p.split("/")[0]) for p in only_prefix)]
            continue
        dirnames.sort()
        for name in sorted(dirnames):
            if PAT.search(name):
                out.append(entry(root, os.path.join(dirpath, name)))
        for name in sorted(filenames):
            if PAT.search(name):
                out.append(entry(root, os.path.join(dirpath, name)))
    return out


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_stop_inventory_v2.py OUTPUT.json")
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(os.path.join(LANE, "evidence", "probes") + os.sep):
        raise SystemExit("REFUSED: output outside LANE/evidence/probes")
    started = host_clock()
    free0 = free_bytes(LANE)
    markers = new_round_markers()
    if free0 < FLOOR or markers:
        raise SystemExit(f"REFUSED: free={free0} floor={FLOOR} new_round_markers={markers}")
    with open(os.path.abspath(__file__), "rb") as f:
        self_sha = hashlib.sha256(f.read()).hexdigest()
    old_lane = walk(OLD_LANE)
    old_run = []
    for d in sorted(os.listdir(os.path.join(OLD_RUN, "review"))):
        if d.startswith("pa19"):
            p = os.path.join(OLD_RUN, "review", d)
            if os.path.isdir(p) and not os.path.islink(p):
                for rec in walk(p):
                    rec["rel"] = os.path.join("review", d, rec["rel"])
                    old_run.append(rec)
    top_old_run = [entry(OLD_RUN, os.path.join(OLD_RUN, n)) for n in sorted(os.listdir(OLD_RUN))
                   if PAT.search(n)]
    free1 = free_bytes(LANE)
    result = {
        "schema": "PA19-96H-PROBE-STOP-INVENTORY-v2",
        "started_host_clock": started,
        "finished_host_clock": host_clock(),
        "elapsed_seconds": round(time.monotonic() - T0, 3),
        "probe_sha256": self_sha,
        "admission": {"free_bytes_start": free0, "floor_bytes": FLOOR,
                      "new_round_markers": markers, "free_bytes_end": free1},
        "pattern": PAT.pattern,
        "old_lane_root": OLD_LANE,
        "old_run_root": OLD_RUN,
        "old_lane_entries": old_lane,
        "old_run_pa19_review_entries": old_run,
        "old_run_top_entries": top_old_run,
        "counts": {
            "old_lane_entries": len(old_lane),
            "old_lane_by_class": {c: sum(1 for r in old_lane if r["class"] == c)
                                  for c in sorted({r["class"] for r in old_lane})},
            "old_run_pa19_review_entries": len(old_run),
        },
        "not_done": "no marker moved/removed/edited; no FIFO opened; no solver/checker/enumerator child (only /bin/date clock reads); no old file written",
    }
    data = json.dumps(result, indent=1, sort_keys=True).encode()
    if len(data) > 16 * 1024 * 1024:
        raise SystemExit("REFUSED: output would exceed 16 MiB")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
