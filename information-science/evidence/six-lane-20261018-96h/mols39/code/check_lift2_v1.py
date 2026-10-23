#!/usr/bin/env python3
"""check_lift2_v1.py (ContinueCFR21, mols39 lane; frozen before the lift_route2 runs; stdlib; reads only).
Checks one finished lift_route2 job against the frozen expectation in lift2-jobs-v1.json; prints one JSON line.
Exit 0 = as expected (L1/L3), or recorded (L4/L2); exit 1 = deviation of a gating control or abnormal settlement."""
import sys, json, os
item, d, base = sys.argv[1], sys.argv[2], sys.argv[3]
r = json.load(open(os.path.join(d, 'receipt.json')))
lines = [ln for ln in open(os.path.join(d, 'stdout.txt')).read().splitlines() if ln.strip()]
o = json.loads(lines[-1]) if len(lines) == 1 else None
res = {"item": item, "receipt_status": r.get("status"), "returncode": r.get("returncode"), "settlement": r.get("settlement"), "trips": r.get("trips")}
settled = r.get("status") == "EXITED" and r.get("settlement") == "SETTLED" and r.get("trips") == [] and o is not None
if not settled:
    res["verdict"] = "ABNORMAL"; print(json.dumps(res, sort_keys=True)); sys.exit(1)
eq = sorted(c.get("equals") for c in (o.get("classes") or []))
res.update({k: o.get(k) for k in ("status", "N_classes", "N_total", "nodes", "fibres_all_size_3", "T_is_lift", "minusT_is_lift", "wall_s", "linear_propagator")})
res["class_labels"] = eq
base_ok = r.get("returncode") == 0 and o.get("status") == "COMPLETE" and o.get("fibres_all_size_3") is True and o.get("T_is_lift") is True and o.get("minusT_is_lift") is True
if item == "L1-dm21-linear":
    ok = base_ok and o.get("N_classes") == 2 and eq == ["-T", "T"] and o.get("N_total") == 486
    res["verdict"] = "AS_EXPECTED" if ok else "CONTROL_DEVIATION"; print(json.dumps(res, sort_keys=True)); sys.exit(0 if ok else 1)
if item == "L3-singer57-k8":
    ok = base_ok and o.get("N_classes") == 4 and "T" in eq and "-T" in eq and o.get("N_total") == 8748
    res["verdict"] = "AS_EXPECTED" if ok else "CONTROL_DEVIATION"; print(json.dumps(res, sort_keys=True)); sys.exit(0 if ok else 1)
if item == "L4-anchor":
    if not base_ok:
        res["verdict"] = "NOT_COMPLETE_OR_ABNORMAL_STATUS"
    else:
        res["verdict"] = "LEMMA_U_CONSISTENT" if (o.get("N_classes") == 2 and eq == ["-T", "T"]) else "LEMMA_U_CONTRADICTED"
    print(json.dumps(res, sort_keys=True)); sys.exit(0)
if item == "L2-dm21-pure":
    if o.get("status") != "COMPLETE":
        res["verdict"] = "NOT_COMPARABLE"
    else:
        ref = json.loads(open(os.path.join(base, "L1-dm21-linear", "stdout.txt")).read().strip())
        same = (o.get("N_classes") == ref.get("N_classes") and sorted(c["rep_sha256"] for c in o["classes"]) == sorted(c["rep_sha256"] for c in ref["classes"]))
        res["verdict"] = "CROSSCHECK_AGREES" if same else "CROSSCHECK_DISAGREES"
    print(json.dumps(res, sort_keys=True)); sys.exit(0)
res["verdict"] = "UNKNOWN_ITEM"; print(json.dumps(res, sort_keys=True)); sys.exit(1)
