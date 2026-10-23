#!/usr/bin/env python3
"""check_ext2_targets_v1.py (ContinueCFR21, mols39 lane; frozen before any ext2 target run; stdlib only; reads only).
After one ext2 target job: prints one JSON line and returns
  0 = settled normally, no solution (COMPLETE with 0 solutions, or INCOMPLETE_BUDGET = UNKNOWN), replay consistent;
  2 = CANDIDATE: at least one solution reported or written (caller stops the wave; candidate protocol);
  1 = anything else (unsettled/tripped/bad output, or a route-2 replay that disagrees with its COMPLETE v2 counterpart).
Args: item job_dir runs_base"""
import sys, json, os
item, d, base = sys.argv[1], sys.argv[2], sys.argv[3]
REPLAY = {"R4-r2-t1": None, "R6-r2-t3": "T3-v2-anchor-C3", "R7-r2-t4": "T4-v2-anchor-C2"}
def outj(dd):
    t = open(os.path.join(dd, 'stdout.txt')).read().strip().splitlines()
    return json.loads(t[-1]) if len(t) == 1 else None
r = json.load(open(os.path.join(d, 'receipt.json')))
o = outj(d)
res = {"item": item, "receipt_status": r.get("status"), "returncode": r.get("returncode"), "settlement": r.get("settlement"), "trips": r.get("trips")}
if not (r.get("status") == "EXITED" and r.get("settlement") == "SETTLED" and r.get("trips") == [] and r.get("returncode") == 0 and o):
    res["verdict"] = "ABNORMAL"; print(json.dumps(res, sort_keys=True)); sys.exit(1)
st = o.get("status"); ns = o.get("solutions"); w = o.get("written") or []
res.update({"status": st, "solutions": ns, "nodes": o.get("nodes"), "written": len(w)})
if st == "ESTIMATE":
    res.update({"verdict": "INFORMATIONAL_ESTIMATE", "knuth_mean_nodes": o.get("knuth_mean_nodes"), "probes_done": o.get("probes_done")})
    print(json.dumps(res, sort_keys=True)); sys.exit(0)
if (isinstance(ns, int) and ns > 0) or w:
    res["verdict"] = "CANDIDATE"; print(json.dumps(res, sort_keys=True)); sys.exit(2)
if st not in ("COMPLETE", "INCOMPLETE_BUDGET"):
    res["verdict"] = "ABNORMAL_STATUS"; print(json.dumps(res, sort_keys=True)); sys.exit(1)
if item in REPLAY:
    ref = REPLAY[item]
    if ref is None:
        refst, refns = "COMPLETE", 0          # v1 T1 and v2 V7: COMPLETE 0
    else:
        ro = outj(os.path.join(base, ref)) if os.path.exists(os.path.join(base, ref, 'stdout.txt')) else None
        refst, refns = (ro.get("status"), ro.get("solutions")) if ro else (None, None)
    res.update({"reference": ref or "v1 T1 / v2 V7", "reference_status": refst, "reference_solutions": refns})
    if st == "COMPLETE" and refst == "COMPLETE" and ns != refns:
        res["verdict"] = "REPLAY_DISAGREES"; print(json.dumps(res, sort_keys=True)); sys.exit(1)
    res["verdict"] = "REPLAY_AGREES" if (st == "COMPLETE" and refst == "COMPLETE") else "REPLAY_NOT_COMPARABLE"
else:
    res["verdict"] = "NO_SOLUTION_COMPLETE" if st == "COMPLETE" else "UNKNOWN_BUDGET"
print(json.dumps(res, sort_keys=True)); sys.exit(0)
