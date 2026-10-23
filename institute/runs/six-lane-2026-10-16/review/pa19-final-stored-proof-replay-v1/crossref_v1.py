#!/usr/bin/env python3
"""PA19StoredProofReplay cross-reference v1 (reads own desk + pinned parent receipts only; no lane file, no child).
Joins the stored-proof replay final receipts (receipts-*.jsonl.gz, manifest-v1.jsonl 31756564...) with:
  * E0: the formula desk's parent rebuild rows R/pa19-final-formula-bindings-v1/e0-v1.jsonl (5cd5cb6c...; result
    e0-result-v1.json 660c74c6...): per graph, the CNF sha256 hashed by the replay driver before AND after drat-trim
    must equal the rebuilt encode_q0 sha ('gen'[0]) and the formula desk's in-place stored hash ('stored'[1]), and
    drat-trim's parsed (V, C) must equal 'gen'[2:4]; the row must be PASS.
  * route a: the replay pre/post CNF sha256 must equal the parent R5 sha (manifest expectation, R5 2a14a1dc...).
Writes DESK/CROSSREF-v1.json (exclusive). Usage: crossref_v1.py --lane L
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
MANIFEST = DESK + "/manifest-v1.jsonl"
FB = R + "/pa19-final-formula-bindings-v1"
PINS = {MANIFEST: "3175656454733c39e217ef89816c67b837dbb2465411312dfe5d1d7455c62d54",
        FB + "/e0-v1.jsonl": "5cd5cb6ce090fc50136f25ecebce558eb1349c92dc72037d6f7a301ab99f647b",
        FB + "/e0-result-v1.json": "660c74c63cf1119497fbf68187377790826b453f5f858d30915355a5c1e29fce"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    if sys.argv[1:] != ["--lane", LANE]:
        raise SystemExit("usage: crossref_v1.py --lane " + LANE)
    for p, w in PINS.items():
        if sha(p) != w:
            raise SystemExit("pin mismatch " + p)
    man = [json.loads(x) for x in open(MANIFEST, encoding="utf-8")]
    fb = {o["tag"]: o for o in (json.loads(x) for x in open(FB + "/e0-v1.jsonl", encoding="utf-8"))}
    finals, files = {}, {}
    for fn in sorted(os.listdir(DESK)):
        if fn.startswith("receipts-") and fn.endswith(".jsonl.gz"):
            files[fn] = sha(os.path.join(DESK, fn))
            data = zlib.decompressobj(31).decompress(open(os.path.join(DESK, fn), "rb").read())
            for ln in data.split(b"\n")[:-1]:
                if ln.strip():
                    o = json.loads(ln)
                    if o.get("kind") == "final":
                        finals.setdefault(o["i"], []).append(o)
    out = {"E0": {"replay_PASS_and_parent_formula_bound": 0, "replay_PASS_binding_mismatch": [],
                  "replay_not_PASS": [], "formula_row_missing_or_not_PASS": []},
           "A2-route-a": {"replay_PASS_and_R5_bound": 0, "replay_PASS_binding_mismatch": [], "replay_not_PASS": []}}
    for c in man:
        fl = finals.get(c["i"], [])
        o = fl[0] if len(fl) == 1 else None
        s = c["set"]
        if o is None or o.get("state") != "PASS":
            out[s]["replay_not_PASS"].append([c["i"], c["tag"], o.get("state") if o else
                                              ("DUPLICATE" if fl else "NO_FINAL")])
            continue
        pre, post = o["pre"]["cnf_sha256"], o["post"]["cnf_sha256"]
        vc = o["parse"]["parsing_lines"][0]
        if s == "E0":
            row = fb.get(c["tag"])
            if not row or row.get("status") != "PASS":
                out[s]["formula_row_missing_or_not_PASS"].append(c["tag"])
                continue
            ok = (pre == post == row["gen"][0] == row["stored"][1] == c["expect_cnf_sha256"] and
                  row["stored"][0] == "cases19q0/cnf/%s.cnf" % c["tag"] and vc == row["gen"][2:4] and
                  o["pre"]["cnf_bytes"] == row["gen"][1] == row["stored"][2])
            if ok:
                out[s]["replay_PASS_and_parent_formula_bound"] += 1
            else:
                out[s]["replay_PASS_binding_mismatch"].append(c["tag"])
        else:
            if pre == post == c["expect_cnf_sha256"] and vc == c["expect_header"]:
                out[s]["replay_PASS_and_R5_bound"] += 1
            else:
                out[s]["replay_PASS_binding_mismatch"].append(c["tag"])
    res = {"schema": "pa19-stored-proof-replay-crossref-v1", "script_sha256": sha(os.path.abspath(__file__)),
           "pins": PINS, "receipt_files": files, "result": out,
           "not_claimed": "Join of replay receipts with existing parent binding receipts; no new binding computed."}
    with open(DESK + "/CROSSREF-v1.json", "xb") as f:
        f.write(json.dumps(res, indent=1, sort_keys=True).encode() + b"\n")
    print(json.dumps({s: {k: (v if isinstance(v, int) else len(v)) for k, v in d.items()} for s, d in out.items()}))


if __name__ == "__main__":
    main()
