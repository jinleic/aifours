#!/usr/bin/env python3
"""rqls_assay_v9_r9_analysis_v1: stdlib read-only analysis of the R9 run JSONL (evidence/rqls_assay_v9.r9.sv2.result.jsonl).
Written and frozen while the run was in flight (before its output existed). Reports, per stage tag: endpoint counts, LM
status counts, verified counts (maxdev < 1e-8) with ray counts, maximal candidates; GATE records and summaries verbatim;
and the parent-requested model-defect screen REGARDLESS of LM status: endpoints with reduced residual < 1e-8 but full
maxdev >= 1e-8 (NEAR_ZERO_FULL_FAIL), the stronger resid < 1e-10 and maxdev >= 1e-6, and max maxdev/resid over
endpoints with resid < 1e-6. Also residual quantiles of unverified R9 endpoints. Usage: ... JSONL JSONL_SHA256 OUT.json
"""
import hashlib, json, sys

raw = open(sys.argv[1], "rb").read()
sha = hashlib.sha256(raw).hexdigest()
if sha != sys.argv[2]:
    sys.exit(9)
recs = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
BIG = ("B", "Z_re", "Z_im", "theta", "traj", "instances", "raw")
stages, gates, summaries, defects, strong, ratios, cands = {}, [], [], [], [], [], []
unver_r9, a9 = [], None
for r in recs:
    if "GATE" in r:
        gates.append(r)
        continue
    if r.get("tag") == "A9_z9p1_classical_anchors":
        a9 = r["instances"]
    if "tag" not in r or "maxdev" not in r:
        summaries.append({k: v for k, v in r.items() if k not in BIG})
        continue
    tag = r["tag"]
    if tag == "KP_perturbed_classical":
        tag = "KP/" + str((r.get("config") or {}).get("stage", "KPc"))
    st = stages.setdefault(tag, {"endpoints": 0, "status": {}, "verified": 0, "verified_rays": {}, "maximal": 0})
    st["endpoints"] += 1
    st["status"][str(r.get("status"))] = st["status"].get(str(r.get("status")), 0) + 1
    if r["maxdev"] < 1e-8:
        st["verified"] += 1
        k = str(r.get("rays"))
        st["verified_rays"][k] = st["verified_rays"].get(k, 0) + 1
    if r.get("maximal_candidate"):
        st["maximal"] += 1
        cands.append({"tag": tag, "seed": r.get("seed"), "config": r.get("config"), "resid": r.get("resid"),
                      "maxdev": r["maxdev"], "rays": r.get("rays"), "minsep": r.get("minsep")})
    res = r.get("resid")
    if res is None:
        continue
    if res < 1e-8 and r["maxdev"] >= 1e-8:
        defects.append({"tag": tag, "seed": r.get("seed"), "status": r.get("status"), "resid": res, "maxdev": r["maxdev"]})
    if res < 1e-10 and r["maxdev"] >= 1e-6:
        strong.append({"tag": tag, "seed": r.get("seed"), "status": r.get("status"), "resid": res, "maxdev": r["maxdev"]})
    if res < 1e-6:
        ratios.append(r["maxdev"] / max(res, 1e-300))
    if tag == "R9_9p1_reduced" and r["maxdev"] >= 1e-8:
        unver_r9.append(res)
unver_r9.sort()


def q(xs, f):
    return xs[min(len(xs) - 1, int(f * (len(xs) - 1)))] if xs else None

out = {"analysis": "rqls_assay_v9_r9_analysis_v1", "jsonl_sha256": sha, "records": len(recs), "stages": stages,
       "gates": gates, "summaries": summaries,
       "A9_instances_summary": ({"n": len(a9), "max_reduced_resid": max(x["reduced_resid"] for x in a9),
                                 "max_maxdev": max(x["maxdev"] for x in a9), "rays": sorted(set(x["rays"] for x in a9)),
                                 "all_orthogonal": all(x["orthogonal_pair"] for x in a9)} if a9 else None),
       "near_zero_full_fail_resid_lt_1e-8_maxdev_ge_1e-8": defects,
       "strong_defect_resid_lt_1e-10_maxdev_ge_1e-6": strong,
       "max_ratio_maxdev_over_resid_for_resid_lt_1e-6": max(ratios) if ratios else None,
       "n_endpoints_resid_lt_1e-6": len(ratios),
       "maximal_candidates": cands,
       "r9_unverified_resid_quantiles": {"n": len(unver_r9), "min": q(unver_r9, 0.0), "q01": q(unver_r9, 0.01),
                                         "q10": q(unver_r9, 0.10), "median": q(unver_r9, 0.5), "max": q(unver_r9, 1.0)}}
with open(sys.argv[3], "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"records": len(recs), "stages": {k: (v["endpoints"], v["verified"], v["verified_rays"], v["maximal"], v["status"])
                                                   for k, v in stages.items()},
                  "gates": [(g["GATE"], g["pass"]) for g in gates], "near_zero_full_fail": len(defects),
                  "strong_defects": len(strong), "max_ratio": out["max_ratio_maxdev_over_resid_for_resid_lt_1e-6"],
                  "maximal_candidates": len(cands), "r9_unverified_resid": out["r9_unverified_resid_quantiles"]}))
