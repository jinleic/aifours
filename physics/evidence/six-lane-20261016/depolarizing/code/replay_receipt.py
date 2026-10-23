"""Reconstruct a complete coverage/equality receipt for a full sector replay from the retained replay logs.

Read-only with respect to all evidence; writes only the receipt JSON given by --out. Run from
evidence/cert/code_snapshot_v3 so that `cert` resolves to the hash-bound v3 cert.py (used only to recompute the
ptail-selected sector set).

python ../../../code/replay_receipt.py --witness ../witness_g3_M2000_p201_1000.json \
    --records '../v3/p201_1000_part_*.json.sectors.jsonl' --logs '../v3_1/p201_1000_full_replay_*.log' \
    --ptail 1e-13 --out ../v3_1/p201_1000_full_replay_RECEIPT.json

Verdict COMPLETE only if: every log parses to exactly one replay JSON (no REJECT, no traceback), the union of
replayed sectors equals the ptail-selected set AND the record set, no sector is replayed twice, and every replayed
sector is equal on all compared fields. Anything else is PARTIAL / FAILED and must not be promoted.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import time
from fractions import Fraction


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def mtime(path):
    return time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(os.path.getmtime(path)))


ap = argparse.ArgumentParser()
ap.add_argument("--witness", required=True)
ap.add_argument("--records", required=True)
ap.add_argument("--logs", required=True)
ap.add_argument("--ptail", type=float, required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()

import cert  # noqa: E402  (hash-bound v3 cert.py from the working directory)

w = json.load(open(a.witness))
M, p = int(w["M"]), Fraction(w["p"])
eta = 1 - Fraction(4, 3) * p
pN = cert.sector_probs_arb(M, eta)
selected = sorted(n for n in pN if float(pN[n].mid()) >= a.ptail)

rec_files = sorted(glob.glob(a.records))
rec_N = []
for f in rec_files:
    for line in open(f):
        if line.strip():
            rec_N.append(json.loads(line)["N"])

logs = []
replayed = []
problems = []
for f in sorted(glob.glob(a.logs)):
    txt = open(f).read()
    lines = [l for l in txt.splitlines() if l.strip()]
    json_lines = [l for l in lines if l.startswith("{")]
    entry = {"path": f, "sha256": sha(f), "mtime": mtime(f), "bytes": len(txt.encode()), "lines": len(lines),
             "has_REJECT": "REJECT" in txt, "has_Traceback": "Traceback" in txt}
    if len(json_lines) != 1 or entry["has_REJECT"] or entry["has_Traceback"] or len(lines) != 1:
        problems.append(f"{f}: unexpected log structure")
        entry["parsed"] = False
    else:
        d = json.loads(json_lines[0])
        res = d["results"]
        entry.update({"parsed": True, "mode": d["mode"], "requested": d["requested"], "records": d["records"],
                      "results": len(res), "all_identical": all(r["identical"] for r in res),
                      "diffs": [r for r in res if not r["identical"]],
                      "N_min": min(r["N"] for r in res), "N_max": max(r["N"] for r in res)})
        if d["requested"] != len(res):
            problems.append(f"{f}: requested {d['requested']} != results {len(res)}")
        replayed += [r["N"] for r in res]
        problems += [f"{f}: sector {r['N']} differs in {r['diff_fields']}" for r in res if not r["identical"]]
    logs.append(entry)

dup = sorted({n for n in replayed if replayed.count(n) > 1})
cov = {
    "selected_count": len(selected), "selected_range": [selected[0], selected[-1]],
    "record_count": len(rec_N), "record_set_equals_selected": sorted(rec_N) == selected,
    "replayed_count": len(replayed), "replayed_unique": len(set(replayed)),
    "replayed_set_equals_selected": sorted(set(replayed)) == selected,
    "missing_from_replay": sorted(set(selected) - set(replayed)),
    "extra_in_replay": sorted(set(replayed) - set(selected)),
    "replayed_more_than_once": dup,
}
if not cov["record_set_equals_selected"]:
    problems.append("record set != selected set")
if not cov["replayed_set_equals_selected"] or dup:
    problems.append("replay coverage incomplete or duplicated")

v3 = "../code_snapshot_v3"
v3_sums = {l.split()[1]: l.split()[0] for l in open(f"{v3}/SHA256SUMS.txt")}
v3_now = {k: sha(f"{v3}/{k}") for k in v3_sums}
receipt = {
    "written": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "witness": {"path": a.witness, "raw_file_sha256": sha(a.witness), "canonical_json_sha256": cert.witness_sha256(w),
                "M": M, "p": str(p)},
    "selection_rule": f"N selected iff mid(p_N) >= ptail = {a.ptail} (cert.sector_probs_arb, cert.py {cert.CODE_SHA256[:16]}...)",
    "record_files": [{"path": f, "sha256": sha(f), "mtime": mtime(f)} for f in rec_files],
    "logs": logs,
    "coverage": cov,
    "equality": {"compared": "exact equality (Python ==) of 19 decoded JSON fields per sector (replay.FIELDS); "
                             "elapsed time excluded; not a byte comparison",
                 "all_replayed_identical": all(e.get("all_identical") for e in logs if e.get("parsed")) and
                 all(e.get("parsed") for e in logs)},
    "code": {"recomputation": {"cert.py": "81d50d9759953ac68fd12a42a0f8394bbe690b6c355b6aa2a883a7dfddb17ee2",
                               "dd.py": "cbfb39f420cf9fe47476c088e4f40650e5a4b1f35675c37def14834335237a21"},
             "comparison_replay.py": "c9395870ef9e5d7704fdc7723b4981ca12e65fb7aa54db16f71666a4ba1f4efd",
             "v3_certified_code_byte_identical_now": v3_now == v3_sums,
             "v3_sha256sums_now": v3_now},
    "problems": problems,
    "verdict": "COMPLETE" if not problems else "PARTIAL_OR_FAILED (do not promote)",
}
json.dump(receipt, open(a.out, "w"), indent=1)
print(json.dumps({"verdict": receipt["verdict"], "coverage": cov, "equality": receipt["equality"],
                  "problems": problems, "v3_code_identical": receipt["code"]["v3_certified_code_byte_identical_now"]},
                 indent=1))
