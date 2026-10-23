#!/usr/bin/env python3
"""Write RESULTS-manifest.json: SHA-256 and size of every file in the lane (except the manifest itself and
archive/), plus the eight witness records parsed from the certificates.  Stdlib only."""
import hashlib
import json
import os
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(LANE, "RESULTS-manifest.json")
WITNESSES = [(122, 6), (123, 6), (124, 6), (143, 5), (144, 5), (146, 5), (162, 5), (167, 5)]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    files = []
    for root, dirs, names in os.walk(LANE):
        dirs[:] = sorted(d for d in dirs if os.path.relpath(os.path.join(root, d), LANE) != "archive")
        for n in sorted(names):
            p = os.path.join(root, n)
            rel = os.path.relpath(p, LANE)
            if rel == "RESULTS-manifest.json":
                continue
            files.append({"path": rel, "sha256": sha(p), "bytes": os.path.getsize(p)})
    wit = []
    for v, k in WITNESSES:
        cert = os.path.join("certs", "v%d" % v, "cpcw_%d_%d.txt" % (v, k))
        rep = json.load(open(os.path.join(LANE, "certs", "v%d" % v, "verify_prep_cpcw_%d_%d.json" % (v, k))))
        lines = open(os.path.join(LANE, cert)).read().rstrip("\n").split("\n")
        wit.append({"v": v, "k": k, "s": len(lines) - 1, "certificate": cert, "sha256": sha(os.path.join(LANE, cert)),
                    "codewords": [[int(x) for x in ln.split(" ")] for ln in lines[1:]],
                    "prep_verifier_verdict": rep["verdict"], "uncovered_differences": rep["uncovered"]})
    man = {"generated": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "lane": "information-science/evidence/six-lane-20261016/cpcw-optimal",
           "claims": "eight finite existence witnesses only; no classification, nonexistence, novelty or priority claim",
           "witnesses": wit, "files": files}
    with open(OUT, "w") as f:
        json.dump(man, f, indent=1)
        f.write("\n")
    print("files=%d witnesses=%d -> %s sha256=%s" % (len(files), len(wit), OUT, sha(OUT)))


if __name__ == "__main__":
    main()
