#!/usr/bin/env python3
"""Retire revision-10 result records (staged pipeline rejected by the parent audit) so that revision 12 recomputes
those cases: every JSON record under cycle2/hard5, cycle2/part, cycle2/m2skel_drat, cycle2/m2part_drat whose
"stream_check_revision" is 10 or whose "runner" is run_hard10.py / run_m2_10.py (batch summaries) is MOVED to
archive/rev10-superseded-<time>/<same relative path> (collision-checked) with one archive/MANIFEST.tsv line each.
Nothing is deleted; ext.json placement lists stay (they were bound by the parent's R6). Usage: retire_rev10.py [--dry-run]
"""
import glob
import hashlib
import json
import os
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    dry = "--dry-run" in sys.argv
    ts = time.strftime("%Y%m%dT%H%M%S")
    base = os.path.join(LANE, "archive", "rev10-superseded-" + ts)
    files = []
    for sub in ("hard5", "part", "m2skel_drat", "m2part_drat"):
        for f in glob.glob(os.path.join(LANE, "cycle2", sub, "**", "*.json"), recursive=True):
            if os.path.basename(f) == "ext.json":
                continue
            try:
                r = json.load(open(f))
            except (OSError, ValueError):
                continue
            if r.get("stream_check_revision") == 10 or r.get("runner") in ("run_hard10.py", "run_m2_10.py"):
                files.append(f)
    print("rev-10 records:", len(files))
    if dry:
        for f in files[:10]:
            print("  would move", os.path.relpath(f, LANE))
        return
    for f in sorted(files):
        rel = os.path.relpath(f, LANE)
        dst = os.path.join(base, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            raise SystemExit("archive destination exists: " + dst)
        os.rename(f, dst)
        h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
        with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as m:
            m.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), rel, os.path.relpath(dst, LANE), h,
                                            "rev-10 record retired (staged rev 10 rejected by parent audit); recomputed under rev 12"))
    print("moved", len(files), "to", os.path.relpath(base, LANE))


if __name__ == "__main__":
    main()
