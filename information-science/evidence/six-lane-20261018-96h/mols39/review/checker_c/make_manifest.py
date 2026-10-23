#!/usr/bin/env python3
"""make_manifest.py - write manifest.json (mode "x") with the SHA-256 of every file
under this directory except manifest.json itself.

Run last:  python3 -I -B make_manifest.py
"""

import hashlib
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    entries = []
    for root, dirs, files in os.walk(HERE):
        dirs.sort()
        for name in sorted(files):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, HERE)
            if rel == "manifest.json":
                continue
            with open(path, "rb") as handle:
                data = handle.read()
            entries.append({"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    entries.sort(key=lambda entry: entry["path"])
    doc = {
        "directory": HERE,
        "author": "ContinueCFR21.CheckerRouteC",
        "written": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "note": "every file of route C; each was created with mode x and never modified",
        "files": entries,
    }
    with open(os.path.join(HERE, "manifest.json"), "x", encoding="ascii") as handle:
        handle.write(json.dumps(doc, indent=1, sort_keys=True) + "\n")
    print(json.dumps({"manifest": "manifest.json", "files": len(entries)}))


if __name__ == "__main__":
    main()
