#!/usr/bin/env python3
"""Producer-replay receipt for the two pinned gcDCQS(20^4:0) certificates (read-only except OUT).
* provenance: rebuilds the block set of E1 KM samples 0 and 1 from the pinned KM rows and compares it
  with the BLOCKS section of each certificate (exact set equality);
* replays: byte comparison of every listed replay output with the pinned certificate;
* hashes of the pinned inputs, the producer code (current tree and the hash-matched reconstruction of
  the 06:45:55 snapshot) and the binaries.
Usage: producer_receipt.py OUT.json"""
import lane_guard  # noqa: F401

import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
import groups as grp

E = "evidence/gcdcqs20-a4c20"
P = E + "/producer"
CERTS = {"e1s0": E + "/gcdcqs20_a4c20_e1s0.txt", "e1s1": E + "/gcdcqs20_a4c20_e1s1.txt"}
REPLAYS = {
    "decode_only_current_code": "runs/replay/decode2_e1s{S}/gcdcqs20_s0.txt",
    "full_solver_current_code": "runs/replay/col_e1s{S}_p10/gcdcqs20_s0.txt",
    "full_solver_original_code": "runs/replay/orig_full_e1s{S}/gcdcqs20_s0.txt",
    "seed_expansion_stdlib": "runs/replay/seed/expanded_e1s{S}.txt",
}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest() if os.path.exists(path) else None


def cert_blocks(path):
    out, on = set(), False
    for line in open(path):
        s = line.strip()
        if s == "BLOCKS":
            on = True
            continue
        if on:
            if s.startswith("POINT"):
                break
            out.add(tuple(int(t) for t in s.split()))
    return out


def main():
    out = sys.argv[1]
    km_summary = json.load(open(P + "/e1_km_summary.json"))
    spec = grp.build("A4xC", 4, 20)
    km = CQSKM(80, spec["group_of"], spec["gens"])
    km_blocks = {S: {tuple(sorted(b)) for b in km.blocks_of(km_summary["samples"][S]["rows"])} for S in (0, 1)}
    rec = {"certificates": {}, "replays": {}, "inputs": {}, "code": {}, "binaries": {}}
    for name, path in CERTS.items():
        cb = cert_blocks(path)
        rec["certificates"][name] = {
            "path": path, "sha256": sha(path), "bytes": os.path.getsize(path),
            "header_line": open(path).readline().rstrip("\n"),
            "blocks_equal_E1_KM_sample": [S for S in (0, 1) if km_blocks[S] == cb],
            "E1_KM_sample_record": {k: km_summary["samples"][int(name[-1])][k]
                                    for k in ("sample", "km_seed", "km_cnf_sha256", "km_status")}}
    for kind, pat in REPLAYS.items():
        for name in CERTS:
            p = pat.format(S=name[-1])
            rec["replays"][f"{kind}:{name}"] = {"output": p, "sha256": sha(p),
                                                "byte_identical_to_pinned": sha(p) == sha(CERTS[name])}
    for f in sorted(os.listdir(P)):
        rec["inputs"][f"{P}/{f}"] = sha(f"{P}/{f}")
    for name in ("km", "e1s0", "e1s1"):
        for f in ("evidence/gcdcqs20-a4c20/gcdcqs20_a4c20_%s_seed.json" % name,):
            if os.path.exists(f):
                rec["inputs"][f] = sha(f)
    snap = dict(reversed(l.split()) for l in open("runs/e9/code_sha256_at_launch.txt") if l.strip())
    for f in sorted(os.listdir("runs/replay/orig_code")):
        h = sha("runs/replay/orig_code/" + f)
        rec["code"]["runs/replay/orig_code/" + f] = {"sha256": h, "matches_06:45:55_snapshot": h == snap.get("code/" + f)}
    for f in ("pipeline2.py", "lanelib.py", "colour_model.py", "cqs_km.py", "groups.py", "pipeline.py",
              "check_gcdcqs.py", "check_gcdcqs.c", "seed_tools.py", "replay_km.py", "equivariance_audit.py",
              "describe_cert.py", "mutation_controls.py", "producer_receipt.py", "lane_guard.py"):
        rec["code"]["code/" + f] = {"sha256": sha("code/" + f)}
    kv = subprocess.run(["kissat", "--version"], capture_output=True, text=True).stdout.strip()
    rec["binaries"] = {"kissat": {"path": "/opt/homebrew/bin/kissat", "version": kv, "sha256": sha("/opt/homebrew/bin/kissat")},
                       "check_gcdcqs_c": {"path": "code/bin/check_gcdcqs_c", "sha256": sha("code/bin/check_gcdcqs_c")},
                       "python_stdlib": {"path": "/usr/bin/python3", "version": "3.9.6"},
                       "python_producer": {"path": os.path.expanduser("~/.local/state/research-explorer/venv/bin/python"),
                                           "version": sys.version.split()[0]}}
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({"certificates": {k: (v["sha256"][:12], v["blocks_equal_E1_KM_sample"]) for k, v in rec["certificates"].items()},
                      "replays": {k: v["byte_identical_to_pinned"] for k, v in rec["replays"].items()}}))


if __name__ == "__main__":
    main()
