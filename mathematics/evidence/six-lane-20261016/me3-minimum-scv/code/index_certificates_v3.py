"""Bookkeeping v3 (v2 kept): certificate index after the SWC repair; SWC = d03-SWC (spec v3, me3dual_v9);
audits = check_cover_v3 runs b03-cover-* (audit_ok); d02-SWC listed as INVALID. Built from receipts and

argv[1] = run directory. Reads (read-only) receipts/*-pre.json, *-post.json and the run outputs listed below.
Writes certificate_index.json (exclusive create). No mathematical computation.
"""
import sys
import json
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"
CERT = [("c03-primalP", "primal.json", "b03-cover-P", "spec_primal_P_v1.json", "P"),
        ("d01-G", "dual.json", "b03-cover-G", "spec_dual_v1.json", "G"),
        ("d01-SWB", "dual.json", "b03-cover-SWB", "spec_dual_v1.json", "SWB"),
        ("d03-SWC", "dual.json", "b03-cover-SWC", "spec_dual_v3.json", "SWC"),
        ("d01-LW", "dual.json", "b03-cover-LW", "spec_dual_v1.json", "LW"),
        ("d01-LD1", "dual.json", "b03-cover-LD1", "spec_dual_v1.json", "LD1"),
        ("d01-LD2", "dual.json", "b03-cover-LD2", "spec_dual_v1.json", "LD2")]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


rows = []
for run, summ, audit, spec, chart in CERT:
    r = {"chart": chart, "run": run, "spec": "code/" + spec, "spec_sha256": sha(L + "code/" + spec)}
    s = json.load(open(L + f"runs/{run}/{summ}"))
    r["certificate_ok"] = s.get("certificate_ok")
    r["counts"] = s.get("counts")
    r["evaluations"] = s.get("evaluations")
    r["leaf_lines_sha256"] = s.get("leaf_lines_sha256")
    r["leaves_gz_sha256"] = sha(L + f"runs/{run}/leaves.txt.gz")
    pre = json.load(open(L + f"receipts/{run}-pre.json"))
    post = json.load(open(L + f"receipts/{run}-post.json"))
    r["pre_receipt_sha256"] = sha(L + f"receipts/{run}-pre.json")
    r["post_receipt_sha256"] = sha(L + f"receipts/{run}-post.json")
    r["code_sha256_at_launch"] = pre["code_sha256"]
    r["wall_seconds"] = post["wall_seconds"]
    r["max_rss_bytes"] = post["max_rss_bytes"]
    a = json.load(open(L + f"runs/{audit}/cover.json"))
    r["audit_run"] = audit
    r["audit_tiling_ok"] = a.get("audit_ok")
    r["audit_leaves"] = a.get("leaves")
    nz = lambda d: {k: v for k, v in (d or {}).items() if v}  # noqa: E731
    r["audit_counts_match"] = nz(a.get("counts")) == nz(s.get("counts"))
    rows.append(r)
r_inv = {"chart": "SWC", "run": "d02-SWC", "status": "INVALID (me3dual_v8.py:28 float-rounded corner coefficients; hostile review me3-charts-codex-v1 finding 1); kept as failed evidence",
         "leaves_gz_sha256": sha(L + "runs/d02-SWC/leaves.txt.gz"), "spec": "code/spec_dual_v2.json"}
out = {"rows": rows, "invalid_runs": [r_inv],
       "all_certified_and_audited": all(x["certificate_ok"] and x["audit_tiling_ok"] and x["audit_counts_match"] for x in rows)}
with lane_guard.xopen(RUN + "/certificate_index.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"all": out["all_certified_and_audited"],
                  "rows": [(x["chart"], x["certificate_ok"], x["audit_tiling_ok"], x["audit_counts_match"],
                            x["audit_leaves"]) for x in rows]}))
