#!/usr/bin/env python3
"""PA19StoredProofReplay re-solve cross-reference v1 (own desk + pinned parent receipts only; no lane file, no child).
Joins the final re-solve receipts (resolve-receipts-*.jsonl.gz, plan resolve-plan-v2.jsonl 1ceb2204...) with:
  * split leaves (502): formula desk exposure-leaf-hashes-v1.json (72749bed...): the CNF the driver built and
    delivered (receipt cnf.sha256/bytes, checker parsing line) must equal 'parent_cnf' [sha, bytes, vars, clauses]
    for the same record path and record sha256;
  * base records (b, c5; 235): the delivered CNF sha must equal the plan's R5 parent rebuild sha (r5_cnf_sha256).
Writes DESK/CROSSREF-RESOLVE-v1.json (exclusive). Usage: crossref_resolve_v1.py --lane L
"""
import hashlib
import json
import os
import sys
import zlib

A = "/Users/jinleic/repos/aifours"
LANE = A + "/information-science/evidence/six-lane-20261016/packing-array19"
R = A + "/institute/runs/six-lane-2026-10-16/review"
DESK = R + "/pa19-final-stored-proof-replay-v1"
PLAN = DESK + "/resolve-plan-v2.jsonl"
LEAVES = R + "/pa19-final-formula-bindings-v1/exposure-leaf-hashes-v1.json"
PINS = {PLAN: "1ceb2204d9b72a139298c8f49958d91e14834cfcaf463cb7f0b3b8cbe3cbd38c",
        LEAVES: "72749beda24ffc950adf32a724d6d2c3d01911440c011fb0e5a82680b7636912"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    if sys.argv[1:] != ["--lane", LANE]:
        raise SystemExit("usage: crossref_resolve_v1.py --lane " + LANE)
    for p, w in PINS.items():
        if sha(p) != w:
            raise SystemExit("pin mismatch " + p)
    plan = [json.loads(x) for x in open(PLAN, encoding="utf-8")]
    leaves = {lf["path"]: lf for lf in json.load(open(LEAVES, encoding="utf-8"))["leaves"]}
    finals, files = {}, {}
    for fn in sorted(os.listdir(DESK)):
        if fn.startswith("resolve-receipts-") and fn.endswith(".jsonl.gz"):
            files[fn] = sha(os.path.join(DESK, fn))
            data = zlib.decompressobj(31).decompress(open(os.path.join(DESK, fn), "rb").read())
            for ln in data.split(b"\n")[:-1]:
                if ln.strip():
                    o = json.loads(ln)
                    if o.get("kind") == "final":
                        finals.setdefault(o["i"], []).append(o)
    out = {"split": {"pass_and_parent_formula_bound": 0, "mismatch": [], "not_pass": [], "leaf_missing": []},
           "base": {"pass_and_R5_bound": 0, "mismatch": [], "not_pass": []}}
    for e in plan:
        fl = finals.get(e["i"], [])
        o = fl[0] if len(fl) == 1 else None
        g = "split" if e["source"] == "build" else "base"
        if o is None or o.get("state") != "PASS":
            out[g]["not_pass"].append([e["i"], e["record"], o.get("state") if o else ("DUP" if fl else "NO_FINAL")])
            continue
        c = o["cnf"]
        vc = o["checker"]["parsing_lines"][0]
        if g == "split":
            lf = leaves.get(e["record"])
            if lf is None or lf.get("record_sha256") != e["record_sha256"]:
                out[g]["leaf_missing"].append(e["record"])
            elif [c["sha256"], c["bytes"]] + vc == lf["parent_cnf"]:
                out[g]["pass_and_parent_formula_bound"] += 1
            else:
                out[g]["mismatch"].append(e["record"])
        else:
            if c["sha256"] == e["r5_cnf_sha256"] and c["bytes"] == e["r5_cnf_bytes"] and vc == e["expect_header"]:
                out[g]["pass_and_R5_bound"] += 1
            else:
                out[g]["mismatch"].append(e["record"])
    res = {"schema": "pa19-resolve-crossref-v1", "script_sha256": sha(os.path.abspath(__file__)), "pins": PINS,
           "receipt_files": files, "result": out,
           "not_claimed": "Join of re-solve receipts with existing parent formula bindings; no new binding computed."}
    with open(DESK + "/CROSSREF-RESOLVE-v1.json", "xb") as f:
        f.write(json.dumps(res, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({g: {k: (v if isinstance(v, int) else len(v)) for k, v in d.items()} for g, d in out.items()}))


if __name__ == "__main__":
    main()
