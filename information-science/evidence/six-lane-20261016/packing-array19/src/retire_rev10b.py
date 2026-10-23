#!/usr/bin/env python3
"""Retire the revision-10 result records by MOVE (parent approval 2026-10-17 ~16:1x, conditions 1-5).
Selection predicate (explicit): a JSON file under cycle2/{hard5,part,m2skel_drat,m2part_drat} (recursively) that is
  (a) a result/batch record whose field "stream_check_revision" == 10, or
  (b) a batch summary named summary_batched.json whose field "runner" is "run_hard10.py" or "run_m2_10.py";
never an ext.json, never a record with another revision. Expected: 291 M2 direct (m2skel_drat), 27 M2 batch records
(m2part_drat), 3 M2 summaries, 53 M1 batch records (part/ms06_s00204), 1 M1 summary = 375.
Steps: inventory (path, size, sha256) of every file in the four directories -> selection -> dry-run list saved ->
read-only scan of institute/runs/six-lane-2026-10-16/review/pa19*/ for any reference to a selected path (abort if
found) -> before.json -> collision-checked os.rename into archive/rev10-superseded-<host time>/<relative path> ->
after.json (every moved file at its new path with identical sha256, old path absent, every other inventoried file
unchanged) -> one archive/MANIFEST.tsv line per moved file.
Usage: retire_rev10b.py dry-run | move
"""
import glob
import hashlib
import json
import os
import re
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("hard5", "part", "m2skel_drat", "m2part_drat")
REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review"
REASON = "rev10 staged pipeline rejected by PA19StagedAudit; superseded by REV11a final predicate"


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def inventory():
    inv = {}
    for d in DIRS:
        for f in glob.glob(os.path.join(LANE, "cycle2", d, "**", "*"), recursive=True):
            if os.path.isfile(f):
                inv[os.path.relpath(f, LANE)] = (os.path.getsize(f), sha(f))
    return inv


def select(inv):
    sel = {}
    for rel in sorted(inv):
        if not rel.endswith(".json") or os.path.basename(rel) == "ext.json":
            continue
        try:
            r = json.load(open(os.path.join(LANE, rel)))
        except (OSError, ValueError):
            continue
        if not isinstance(r, dict):
            continue
        sub = rel.split(os.sep)[1]
        if r.get("stream_check_revision") == 10:
            kind = {"m2skel_drat": "M2 direct", "m2part_drat": "M2 batch", "part": "M1 batch", "hard5": "M1 direct"}[sub]
            sel[rel] = kind
        elif os.path.basename(rel) == "summary_batched.json" and r.get("runner") in ("run_hard10.py", "run_m2_10.py"):
            sel[rel] = "M2 summary" if sub == "m2part_drat" else "M1 summary"
    return sel


def scan_review(paths):
    pats = sorted(set(paths) | {p.split("cycle2/", 1)[1] for p in paths})
    rx = re.compile("|".join(re.escape(p) for p in pats))
    hits = []
    nfiles = 0
    for d in glob.glob(os.path.join(REVIEW, "pa19*")):
        for f in glob.glob(os.path.join(d, "**", "*"), recursive=True):
            if not os.path.isfile(f) or os.path.getsize(f) > 300 * 1024 * 1024:
                continue
            nfiles += 1
            try:
                txt = open(f, "rb").read().decode("utf-8", errors="ignore")
            except OSError:
                continue
            m = rx.search(txt)
            if m:
                hits.append({"file": f, "match": m.group(0)})
    return nfiles, hits


def main():
    mode = sys.argv[1]
    ts = time.strftime("%Y%m%dT%H%M%S")
    inv = inventory()
    sel = select(inv)
    counts = {}
    for k in sel.values():
        counts[k] = counts.get(k, 0) + 1
    print("inventory files", len(inv), "selected", len(sel), counts)
    dry = {"time": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "predicate": __doc__.split("Selection predicate (explicit): ")[1].split("Steps:")[0].strip(),
           "counts": counts, "selected": [{"path": p, "kind": k, "size": inv[p][0], "sha256": inv[p][1]} for p, k in sorted(sel.items())]}
    dp = os.path.join(LANE, "cycle2", "rev10-retire-dryrun-%s.json" % ts)
    with open(dp, "w") as f:
        json.dump(dry, f, indent=1)
    print("dry-run list", os.path.relpath(dp, LANE))
    expected = {"M2 direct": 291, "M2 batch": 27, "M2 summary": 3, "M1 batch": 53, "M1 summary": 1}
    if counts != expected:
        raise SystemExit("selection counts differ from the approved set: %s" % counts)
    if mode != "move":
        return
    nfiles, hits = scan_review(list(sel))
    print("review files scanned", nfiles, "references", len(hits))
    if hits:
        with open(os.path.join(LANE, "cycle2", "rev10-retire-ABORTED-%s.json" % ts), "w") as f:
            json.dump({"hits": hits}, f, indent=1)
        raise SystemExit("selected paths referenced by parent receipts -- not moving")
    base = os.path.join(LANE, "archive", "rev10-superseded-%s" % ts)
    before = {"time": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "dry_run_list": os.path.relpath(dp, LANE),
              "review_scan": {"root": REVIEW + "/pa19*", "files_scanned": nfiles, "references": 0},
              "inventory_count": len(inv), "selected": dry["selected"], "destination_root": os.path.relpath(base, LANE)}
    with open(os.path.join(LANE, "cycle2", "rev10-retire-before-%s.json" % ts), "w") as f:
        json.dump(before, f, indent=1)
    moved = []
    for rel in sorted(sel):
        src = os.path.join(LANE, rel)
        dst = os.path.join(base, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            raise SystemExit("archive destination exists: " + dst)
        os.rename(src, dst)
        moved.append((rel, os.path.relpath(dst, LANE)))
        with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as m:
            m.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), rel, os.path.relpath(dst, LANE), inv[rel][1], REASON))
    inv2 = inventory()
    checks = []
    for rel, drel in moved:
        checks.append({"path": rel, "new_path": drel, "old_absent": not os.path.exists(os.path.join(LANE, rel)),
                       "sha256_equal": sha(os.path.join(LANE, drel)) == inv[rel][1]})
    remaining_expected = {p: v for p, v in inv.items() if p not in sel}
    unchanged = remaining_expected == inv2
    after = {"time": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "moved": checks,
             "all_moved_ok": all(c["old_absent"] and c["sha256_equal"] for c in checks),
             "other_files_unchanged": unchanged, "inventory_after_count": len(inv2),
             "inventory_expected_count": len(remaining_expected)}
    with open(os.path.join(LANE, "cycle2", "rev10-retire-after-%s.json" % ts), "w") as f:
        json.dump(after, f, indent=1)
    print("moved", len(moved), "all_moved_ok", after["all_moved_ok"], "other_files_unchanged", unchanged)


if __name__ == "__main__":
    main()
