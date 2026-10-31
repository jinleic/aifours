#!/usr/bin/env python3
"""Reviewer-authored input verification for wave f185 (no author code imported).

Recomputes manifest SHA-256, then each declared input's SHA-256, byte length and
LF count, and compares against the manifest declarations.  Writes a JSON receipt
next to this script (exclusive create).
"""
import hashlib
import json
import os
import sys
import time

WAVE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(WAVE, "manifest-v1.json")
EXPECTED_MANIFEST_SHA = "da4e1497c11566e2380e4684082adc45931190ec0f28b09c992b1a7f9b93cc7a"
OUT = os.path.join(WAVE, "reviewer-input-verification-v1.json")


def main() -> int:
    t0 = time.time()
    raw = open(MANIFEST, "rb").read()
    msha = hashlib.sha256(raw).hexdigest()
    manifest = json.loads(raw.decode("utf-8"))
    rows = []
    ok_all = msha == EXPECTED_MANIFEST_SHA
    for idx, item in enumerate(manifest["inputs_in_read_order"], 1):
        data = open(item["path"], "rb").read()
        sha = hashlib.sha256(data).hexdigest()
        nbytes = len(data)
        lf = data.count(b"\n")
        ok = sha == item["sha256"] and nbytes == item["bytes"] and lf == item["LF"]
        ok_all = ok_all and ok
        rows.append({
            "order": idx,
            "path": item["path"],
            "role": item["role"],
            "sha256_observed": sha,
            "sha256_declared": item["sha256"],
            "bytes_observed": nbytes,
            "bytes_declared": item["bytes"],
            "LF_observed": lf,
            "LF_declared": item["LF"],
            "ends_with_LF": data.endswith(b"\n"),
            "match": ok,
        })
    receipt = {
        "manifest_path": MANIFEST,
        "manifest_sha256_observed": msha,
        "manifest_sha256_expected": EXPECTED_MANIFEST_SHA,
        "manifest_match": msha == EXPECTED_MANIFEST_SHA,
        "inputs": rows,
        "all_match": ok_all,
        "elapsed_seconds": round(time.time() - t0, 3),
    }
    with open(OUT, "x", encoding="utf-8") as fh:
        json.dump(receipt, fh, indent=2)
        fh.write("\n")
    print(json.dumps({"all_match": ok_all, "manifest_match": receipt["manifest_match"],
                      "n_inputs": len(rows)}, indent=None))
    for r in rows:
        print(r["order"], r["match"], r["bytes_observed"], r["LF_observed"], r["ends_with_LF"], os.path.basename(r["path"]))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
