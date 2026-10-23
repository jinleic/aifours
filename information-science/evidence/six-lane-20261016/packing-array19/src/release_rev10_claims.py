#!/usr/bin/env python3
"""Release the claim files written by the rejected rev-10 runners (run_hard10.py / run_m2_10.py) whose result records were
retired (archive/rev10-superseded-20261017T160921), so that rev-12/13 runners can recompute those items. Selection: a
claim file in cycle2/claims whose content contains 'run_hard10' or 'run_m2_10' AND whose item has no current result
(no cycle2/hard5/<tag>.json for h5_, no cycle2/part/<tag>/summary_batched.json for pb9_, no
cycle2/m2skel_drat/<ms_b>.json for m2d9_, no cycle2/m2part_drat/<ms_b>/summary_batched.json for m2pbd9_). Each is moved
(collision-checked) to archive/claims-released/<name>.rev10.<time>.claim with an archive/MANIFEST.tsv line.
Usage: release_rev10_claims.py dry-run|move
"""
import glob
import hashlib
import os
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, "cycle2")


def has_result(name):
    if name.startswith("h5_"):
        return os.path.exists(os.path.join(C2, "hard5", name[3:] + ".json"))
    if name.startswith("pb9_"):
        return os.path.exists(os.path.join(C2, "part", name[4:], "summary_batched.json"))
    if name.startswith("m2d9_"):
        return os.path.exists(os.path.join(C2, "m2skel_drat", name[5:] + ".json"))
    if name.startswith("m2pbd9_"):
        return os.path.exists(os.path.join(C2, "m2part_drat", name[7:], "summary_batched.json"))
    return True


def main():
    mode = sys.argv[1]
    sel = []
    for c in sorted(glob.glob(os.path.join(C2, "claims", "*.claim"))):
        name = os.path.basename(c)[:-6]
        txt = open(c).read()
        if ("run_hard10" in txt or "run_m2_10" in txt) and not has_result(name):
            sel.append(c)
    print("selected", len(sel), "e.g.", [os.path.basename(x) for x in sel[:5]])
    if mode != "move":
        return
    ts = time.strftime("%Y%m%dT%H%M%S")
    rel = os.path.join(LANE, "archive", "claims-released")
    os.makedirs(rel, exist_ok=True)
    for c in sel:
        dst = os.path.join(rel, os.path.basename(c)[:-6] + ".rev10.%s.claim" % ts)
        if os.path.exists(dst):
            raise SystemExit("archive destination exists: " + dst)
        os.rename(c, dst)
        h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
        with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
            f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(c, LANE), os.path.relpath(dst, LANE),
                                              h, "claim of a rev-10 runner whose record was retired; released so rev 12/13 recompute the item"))
    print("moved", len(sel))


if __name__ == "__main__":
    main()
