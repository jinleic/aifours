#!/usr/bin/env python3
"""Additive cycle-2 SHA-256 manifest (parent request 2026-10-17 ~12:15): case definitions,
generator outputs, comparison maps, split enumerations, job lists, data, sources and docs.
Writes cycle2/MANIFEST-cycle2-<stamp>.sha256 (sha256sum format, paths relative to the lane)
and a .json summary with per-group counts. Read-only over everything else.
"""
import glob
import hashlib
import json
import os
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GROUPS = [
    ("case_index", ["cases19skel/index.json"]),
    ("case_specs", ["cases19skel/specs/*.json"]),
    ("m1_skeleton_lists", ["skeletons/skeletons-ms*.json"]),
    ("m2_skeleton_lists_and_maps", ["cycle2/skel-b/*.json"]),
    ("genbg_flags_log", ["cycle2/genbg-help-flags.txt"]),
    ("job_and_tag_lists", ["cycle2/*.txt"]),
    ("a3_ext", ["cycle2/a3/*/ext.json"]),
    ("part_ext", ["cycle2/part/*/ext.json"]),
    ("m2part_ext", ["cycle2/m2part/*/ext.json"]),
    ("e0_inputs", ["data/quadgraphs-8v-13to16e-D4.g6", "data/quadgraphs-independent-check.json",
                   "data/profiles-19-8-6.json", "data/cpro1-pa-18-8-6.txt"]),
    ("sources", ["src/*.py", "src/*.c", "tools/drat-trim/*.c", "tools/drat-trim/COMMIT.txt"]),
    ("controls", ["cycle2/control*.json", "cycle2/control18/*", "cycle2/smoke-stream*.json",
                  "cycle2/control13-part/*", "cycle2/control13-m2part/*"]),
    ("docs", ["README.md", "checkpoints.md"]),
]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    stamp = time.strftime("%Y%m%dT%H%M%S")
    lines, counts = [], {}
    seen = set()
    for name, pats in GROUPS:
        files = []
        for p in pats:
            files += sorted(glob.glob(os.path.join(LANE, p)))
        n = 0
        for f in files:
            if not os.path.isfile(f):
                continue
            rel = os.path.relpath(f, LANE)
            if rel in seen:
                continue
            seen.add(rel)
            lines.append("%s  %s" % (sha(f), rel))
            n += 1
        counts[name] = n
    out = os.path.join(LANE, "cycle2", "MANIFEST-cycle2-%s.sha256" % stamp)
    with open(out, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    summ = {"created": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "manifest": os.path.relpath(out, LANE),
            "manifest_sha256": sha(out), "entries": len(lines), "groups": counts}
    json.dump(summ, open(out.replace(".sha256", ".json"), "w"), indent=1)
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()
