"""Discriminating mutation controls for combine.py / replay.py on the v3 p = 1/5 records.

Run from evidence/cert/code_snapshot_v3:  ../../../env/bin/python test_combine_mutations.py
Every mutation must be rejected with its EXPECTED reason (an arbitrary failure does not count); the
changed-contribution mutation is expected to PASS combine (documented limit) and FAIL replay.
"""
from __future__ import annotations

import copy
import glob
import json
import os

from combine import Reject, combine
from replay import replay

W = "../witness_g3_M2000_p1_5.json"
PARTS = sorted(glob.glob("../v3/p1_5_part_*.json.sectors.jsonl"))
MUT = "../v3/mutations"
os.makedirs(MUT, exist_ok=True)
PT, PIT = 1e-13, 1e-40
w0 = json.load(open(W))
recs = [json.loads(l) for f in PARTS for l in open(f) if l.strip()]


def write_parts(rs, name):
    path = f"{MUT}/{name}.sectors.jsonl"
    with open(path, "w") as fh:
        for r in rs:
            fh.write(json.dumps(r) + "\n")
    return [path]


def expect(name, reason, w=None, rs=None, ptail=PT, allow_missing=False):
    try:
        out = combine(w or w0, write_parts(rs if rs is not None else recs, name), ptail, PIT, allow_missing)
        got = "ACCEPT:" + out["classification"]
    except Reject as e:
        got = e.reason
    ok = got == reason
    return {"mutation": name, "expected": reason, "got": got, "ok": ok}


res = []
res.append(expect("baseline", "ACCEPT:POS"))
w1 = copy.deepcopy(w0)
v = float.fromhex(w1["amps"][0][39])
w1["amps"][0][39] = (v * (1 + 2 ** -40)).hex()
res.append(expect("witness_amplitude_changed", "witness_hash", w=w1))
for field, val, reason in (("cert_py_sha256", "0" * 64, "cert_hash"), ("dd_py_sha256", "f" * 64, "dd_hash"),
                           ("M", 2001, "param_mismatch"), ("p", "201/1000", "param_mismatch"),
                           ("D_param", 439, "param_mismatch")):
    rs = copy.deepcopy(recs)
    rs[17][field] = val
    res.append(expect(f"record_{field}_changed", reason, rs=rs))
res.append(expect("duplicate_sector", "duplicate", rs=recs + [copy.deepcopy(recs[5])]))
rs = [r for i, r in enumerate(recs) if i != 40]
res.append(expect("sector_removed", "missing", rs=rs))
r_allow = expect("sector_removed_allow_missing", "ACCEPT:POS", rs=rs, allow_missing=True)
res.append(r_allow)
rs = copy.deepcopy(recs)
rs[60]["lo"], rs[60]["hi"] = rs[60]["hi"] + 1e-9, rs[60]["lo"]
res.append(expect("interval_inverted", "order", rs=rs))
rs = copy.deepcopy(recs)
rs[61]["lo"] = float("nan")
res.append(expect("nan_bound", "nonfinite", rs=rs))
rs = copy.deepcopy(recs)
extra = copy.deepcopy(recs[0])
extra["N"] = 1000
res.append(expect("unselected_sector", "unexpected_sector", rs=rs + [extra]))
res.append(expect("wrong_ptail_at_combine", "param_mismatch", ptail=1e-12))
# changed contribution: combine cannot see it (limit), replay must
rs = copy.deepcopy(recs)
idx = next(i for i, r in enumerate(rs) if r["N"] == 1452)
rs[idx]["lo"] += 1e-9   # consistent shift of the whole sector interval (no ordering violation)
rs[idx]["hi"] += 1e-9
rs[idx]["ic_trunc"] = [v + 1e-9 for v in rs[idx]["ic_trunc"]]
r_c = expect("contribution_changed_combine", "ACCEPT:POS", rs=rs)
r_c["note"] = "expected: combine cannot detect consistent numeric tampering"
res.append(r_c)
rp = replay(w0, write_parts(rs, "contribution_changed_replay"), PT, PIT, [1452])
res.append({"mutation": "contribution_changed_replay", "expected": "replay_mismatch",
            "got": "replay_mismatch" if not rp[0]["identical"] else "identical", "ok": not rp[0]["identical"],
            "diff_fields": rp[0]["diff_fields"]})
rp0 = replay(w0, PARTS, PT, PIT, [1452])
res.append({"mutation": "unmutated_replay", "expected": "identical",
            "got": "identical" if rp0[0]["identical"] else "mismatch", "ok": rp0[0]["identical"]})
summary = {"all_ok": all(r["ok"] for r in res), "n": len(res), "results": res, "parts": PARTS}
json.dump(summary, open("../v3/mutation_tests.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
raise SystemExit(0 if summary["all_ok"] else 1)
