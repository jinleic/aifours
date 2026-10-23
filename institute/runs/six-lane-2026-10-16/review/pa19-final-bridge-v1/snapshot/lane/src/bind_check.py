#!/usr/bin/env python3
"""Binding check (parent audit item b): re-derive CNFs in memory from the frozen specs and
compare SHA-256 with the hashes recorded in results.
  * all 5,577 A2 cases: encode_skel(spec) vs cases19skel/results/<tag>.json cnf_sha256 (the
    CNF that pass 1, the cycle-1 stored-proof checks, the cycle-2 streamed proof pass and the
    direct runs used);
  * a deterministic sample (every STEP-th) of split subcases/batches: A3 encode_full(spec,
    ext placement i), A3' encode_partq(spec, placement i), A3'' encode_partbatch(spec,
    placements of the batch) vs the cnf_sha256 in their result files.
Writes cycle2/binding-pass1.json. Read-only otherwise. Usage: bind_check.py [STEP]
"""
import glob
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full  # noqa: E402
import encode_partbatch  # noqa: E402
import encode_partq  # noqa: E402
import encode_skel  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def h(F):
    return hashlib.sha256(S.cnf_bytes_of(F)).hexdigest()


def main():
    step = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    idx = json.load(open(os.path.join(LANE, "cases19skel", "index.json")))
    bad, n = [], 0
    for c in idx["cases"]:
        tag = c["tag"]
        spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
        F, _, _ = encode_skel.build(spec)
        rec = json.load(open(os.path.join(LANE, "cases19skel", "results", tag + ".json")))["cnf_sha256"]
        n += 1
        if h(F) != rec:
            bad.append(tag)
    split_checked, split_bad = 0, []
    for d in sorted(glob.glob(os.path.join(LANE, "cycle2", "a3", "*"))) + sorted(glob.glob(os.path.join(LANE, "cycle2", "part", "*"))):
        tag = os.path.basename(d)
        E = json.load(open(os.path.join(d, "ext.json"))) if os.path.exists(os.path.join(d, "ext.json")) else None
        if not E:
            continue
        spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
        kind = "a3" if "/a3/" in d else "part"
        files = sorted(glob.glob(os.path.join(d, "f*.json")))
        for f in files[::step]:
            m = re.match(r".*/f(\d+)(_r2|_exact)?\.json$", f)
            if not m or m.group(2):
                continue
            i = int(m.group(1))
            r = json.load(open(f))
            sub = dict(spec)
            sub["placed"] = E["full"][i]
            F = encode_full.build(sub)[0] if kind == "a3" else encode_partq.build(sub)[0]
            split_checked += 1
            if h(F) != r["cnf_sha256"]:
                split_bad.append(os.path.relpath(f, LANE))
        for f in sorted(glob.glob(os.path.join(d, "batch_*.json")))[::max(1, step // 10)]:
            if f.endswith("_r2.json"):
                continue
            r = json.load(open(f))
            F = encode_partbatch.build(spec, [E["full"][i] for i in r["indices"]])[0]
            split_checked += 1
            if h(F) != r["cnf_sha256"]:
                split_bad.append(os.path.relpath(f, LANE))
    out = {"summary": {"a2_cases_rederived": n, "a2_mismatches": len(bad), "split_results_sampled": split_checked,
                       "split_mismatches": len(split_bad), "sample_step": step},
           "a2_mismatch_tags": bad, "split_mismatch_files": split_bad}
    json.dump(out, open(os.path.join(LANE, "cycle2", "binding-pass1.json"), "w"), indent=1)
    print(json.dumps(out["summary"]))


if __name__ == "__main__":
    main()
