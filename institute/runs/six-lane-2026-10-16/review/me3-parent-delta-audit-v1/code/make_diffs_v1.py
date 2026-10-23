"""ME3ParentDelta: parent-computed unified diffs of the lane texts (read-only inputs; outputs mode 'x').

Writes diffs/<name>.diff and diffs/inputs-sha256.json inside the desk. Never touches the lane.
"""
import difflib
import hashlib
import json
import os

LANE = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv"
DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(DESK, "diffs")

PAIRS = [
    ("reductions-v1-to-v2", "reductions/proof/reductions-v1.md", "reductions/proof/reductions-v2.md"),
    ("reductions-v2-to-v3", "reductions/proof/reductions-v2.md", "reductions/proof/reductions-v3.md"),
    ("reductions-v3-to-v4", "reductions/proof/reductions-v3.md", "reductions/proof/reductions-v4.md"),
    ("reductions-v1-to-v4", "reductions/proof/reductions-v1.md", "reductions/proof/reductions-v4.md"),
    ("theorem-v3-to-v4", "proof/me3-theorem-v3.md", "proof/me3-theorem-v4.md"),
    ("theorem-v4-to-v5", "proof/me3-theorem-v4.md", "proof/me3-theorem-v5.md"),
    ("theorem-v3-to-v5", "proof/me3-theorem-v3.md", "proof/me3-theorem-v5.md"),
    ("charts-spec-v1-to-v2", "proof/charts-spec-v1.md", "proof/charts-spec-v2.md"),
]
EXTRA = [
    "reductions/proof/reductions-v3.diff-from-v2.txt",
    "reductions/proof/reductions-v4.diff-from-v3.txt",
    "proof/me3-theorem-v5.diff-from-v4.txt",
    "reductions/proof/vcos-lower-bound-v1.md",
    "receipts/me3-candidate-pin-v3.json",
]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    hashes = {}
    for name, a, b in PAIRS:
        pa, pb = os.path.join(LANE, a), os.path.join(LANE, b)
        hashes[a] = sha(pa)
        hashes[b] = sha(pb)
        with open(pa, encoding="utf-8") as fh:
            la = fh.readlines()
        with open(pb, encoding="utf-8") as fh:
            lb = fh.readlines()
        diff = list(difflib.unified_diff(la, lb, fromfile=a, tofile=b, n=2))
        with open(os.path.join(OUT, name + ".diff"), "x", encoding="utf-8") as fh:
            fh.writelines(diff)
        print(name, "hunks", sum(1 for x in diff if x.startswith("@@")), "lines", len(diff))
    for e in EXTRA:
        hashes[e] = sha(os.path.join(LANE, e))
    with open(os.path.join(OUT, "inputs-sha256.json"), "x", encoding="utf-8") as fh:
        json.dump(hashes, fh, indent=1, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    main()
