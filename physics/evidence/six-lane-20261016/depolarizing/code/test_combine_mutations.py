"""Discriminating mutation controls for combine.py / replay.py (v3.1) on the v3 p = 1/5 records.

Run from evidence/cert/code_snapshot_v3_1:  ../../../env/bin/python test_combine_mutations.py
Every mutation must be rejected with its EXPECTED reason (an arbitrary failure does not count); the
consistent-shift mutation is expected to PASS combine (documented limit) and FAIL replay.
"""
from __future__ import annotations

import copy
import glob
import json
import os
import subprocess

from combine import Reject, combine
from replay import replay

W = "../witness_g3_M2000_p1_5.json"
PARTS = sorted(glob.glob("../v3/p1_5_part_*.json.sectors.jsonl"))
MUT = "../v3_1/mutations"
os.makedirs(MUT, exist_ok=True)
PT, PIT = 1e-13, 1e-40
w0 = json.load(open(W))
recs = [json.loads(l) for f in PARTS for l in open(f) if l.strip()]


def write_parts(rs, name, raw_extra=None):
    path = f"{MUT}/{name}.sectors.jsonl"
    with open(path, "w") as fh:
        for r in rs:
            fh.write(json.dumps(r) + "\n")
        if raw_extra:
            fh.write(raw_extra + "\n")
    return [path]


def expect(name, reason, w=None, rs=None, ptail=PT, allow_missing=False, raw_extra=None):
    try:
        out = combine(w or w0, write_parts(rs if rs is not None else recs, name, raw_extra), ptail, PIT, allow_missing)
        got = "ACCEPT:" + out["classification"]
    except Reject as e:
        got = e.reason
    return {"mutation": name, "expected": reason, "got": got, "ok": got == reason}


def mut(i, **kv):
    rs = copy.deepcopy(recs)
    for key, val in kv.items():
        if val is DEL:
            del rs[i][key]
        else:
            rs[i][key] = val
    return rs


DEL = object()
res = [expect("baseline", "ACCEPT:POS")]
w1 = copy.deepcopy(w0)
w1["amps"][0][39] = (float.fromhex(w1["amps"][0][39]) * (1 + 2 ** -40)).hex()
res.append(expect("witness_amplitude_changed", "witness_hash", w=w1))
for field, val, reason in (("cert_py_sha256", "0" * 64, "cert_hash"), ("dd_py_sha256", "f" * 64, "dd_hash"),
                           ("M", 2001, "param_mismatch"), ("p", "201/1000", "param_mismatch"),
                           ("D_param", 439, "param_mismatch")):
    res.append(expect(f"record_{field}_changed", reason, rs=mut(17, **{field: val})))
res.append(expect("record_without_provenance", "no_provenance", rs=mut(17, cert_py_sha256=DEL)))
res.append(expect("duplicate_sector", "duplicate", rs=recs + [copy.deepcopy(recs[5])]))
rs = [r for i, r in enumerate(recs) if i != 40]
res.append(expect("sector_removed", "missing", rs=rs))
res.append(expect("sector_removed_allow_missing", "ACCEPT:POS", rs=rs, allow_missing=True))
res.append(expect("interval_inverted", "order", rs=mut(60, lo=recs[60]["hi"] + 1e-9, hi=recs[60]["lo"])))
res.append(expect("nan_bound", "nonfinite", rs=mut(61, lo=float("nan"))))
extra = copy.deepcopy(recs[0])
extra["N"] = 1000
res.append(expect("unselected_sector", "unexpected_sector", rs=recs + [extra]))
res.append(expect("wrong_ptail_at_combine", "param_mismatch", ptail=1e-12))
# v3.1 malformed-record controls (Codex re-review)
res.append(expect("ic_trunc_empty", "malformed", rs=mut(20, ic_trunc=[])))
res.append(expect("ic_trunc_three", "malformed", rs=mut(20, ic_trunc=[0.0, 1e-9, 2e-9])))
res.append(expect("lo_string", "malformed", rs=mut(20, lo="1e-8")))
res.append(expect("eps_tail_negative", "domain", rs=mut(21, eps_tail=-1e-30)))
res.append(expect("effective_D_changed", "D_effective", rs=mut(22, D=439)))
res.append(expect("pN_nonfinite", "nonfinite", rs=mut(23, pN=float("inf"))))
res.append(expect("pN_changed", "pN_mismatch", rs=mut(24, pN=recs[24]["pN"] * (1 + 1e-12))))
res.append(expect("unparsable_line", "malformed", raw_extra="{not json"))
# consistent numeric tampering: combine cannot see it (documented limit), replay must
rs = copy.deepcopy(recs)
idx = next(i for i, r in enumerate(rs) if r["N"] == 1452)
rs[idx]["lo"] += 1e-9
rs[idx]["hi"] += 1e-9
rs[idx]["ic_trunc"] = [v + 1e-9 for v in rs[idx]["ic_trunc"]]
r_c = expect("contribution_changed_combine", "ACCEPT:POS", rs=rs)
r_c["note"] = "expected: combine cannot detect consistent numeric tampering"
res.append(r_c)
rp = replay(w0, write_parts(rs, "contribution_changed_replay"), PT, PIT, [1452])
res.append({"mutation": "contribution_changed_replay", "expected": "replay_mismatch",
            "got": "replay_mismatch" if not rp[0]["identical"] else "identical", "ok": not rp[0]["identical"]})
rp0 = replay(w0, PARTS, PT, PIT, [1452])
res.append({"mutation": "unmutated_replay", "expected": "identical",
            "got": "identical" if rp0[0]["identical"] else "mismatch", "ok": rp0[0]["identical"]})
cp = subprocess.run(["../../../env/bin/python", "replay.py", W, *PARTS, "--ptail", "1e-13", "--pitail", "1e-40"],
                    capture_output=True, text=True)
got = "empty_selection" if (cp.returncode == 2 and "REJECT empty_selection" in cp.stdout) else f"rc={cp.returncode}"
res.append({"mutation": "replay_empty_selection", "expected": "empty_selection", "got": got, "ok": got == "empty_selection"})
summary = {"all_ok": all(r["ok"] for r in res), "n": len(res), "results": res, "parts": PARTS}
json.dump(summary, open("../v3_1/mutation_tests.json", "w"), indent=1)
print(json.dumps({"all_ok": summary["all_ok"], "n": summary["n"],
                  "failed": [r for r in res if not r["ok"]]}, indent=1))
raise SystemExit(0 if summary["all_ok"] else 1)
