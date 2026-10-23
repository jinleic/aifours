#!/usr/bin/env python3
"""check_ext2_controls_v1.py (ContinueCFR21, mols39 lane; frozen before the ext2 control runs; stdlib only; reads only).
Checks one finished ext2 control job directory against its frozen expectation (ext2-jobs-v1.json 'expect' strings,
made exact here) and prints one JSON line; exit 0 = as expected, 1 = deviation (caller stops the wave).
Args: item job_dir runs_base"""
import sys, json, os
item, d, base = sys.argv[1], sys.argv[2], sys.argv[3]
def load(p):
    try:
        return json.load(open(p))
    except Exception as e:
        return {"_error": repr(e)}
r = load(os.path.join(d, 'receipt.json'))
txt = open(os.path.join(d, 'stdout.txt')).read() if os.path.exists(os.path.join(d, 'stdout.txt')) else ''
lines = [ln for ln in txt.splitlines() if ln.strip()]
out = json.loads(lines[-1]) if len(lines) == 1 else None
res = {"item": item, "receipt_status": r.get("status"), "returncode": r.get("returncode"), "settlement": r.get("settlement"),
       "trips": r.get("trips"), "stdout_lines": len(lines)}
ok = r.get("status") == "EXITED" and r.get("settlement") == "SETTLED" and r.get("trips") == [] and out is not None
def sols(it):
    o = json.loads(open(os.path.join(base, it, 'stdout.txt')).read().strip())
    return o.get("solutions")
if ok:
    st, n_sol, w = out.get("status"), out.get("solutions"), out.get("written") or []
    res.update({"status": st, "solutions": n_sol, "nodes": out.get("nodes"), "written": len(w)})
    allok = all(x.get("dm_ok") is True for x in w)
    const = all(x.get("new_row_constant", x.get("constant")) is True for x in w)
    if item in ("V1-v2-x1rep", "R1-r2-x1"):
        ok = r["returncode"] == 0 and st == "COMPLETE" and n_sol == 35 and len(w) == 20 and allok and const
    elif item in ("V2-v2-x2rep", "R2-r2-x2"):
        ok = r["returncode"] == 0 and st == "COMPLETE" and n_sol == 1 and len(w) == 1 and allok and const
    elif item in ("V3-v2-x3rep", "R3-r2-x3"):
        ok = r["returncode"] == 3 and st == "NOT_INVARIANT"
    elif item == "V7-v2-t1rep":
        ok = r["returncode"] == 0 and st == "COMPLETE" and n_sol == 0
    elif item == "V4-v2-z13-free0":
        ok = (r["returncode"] == 0 and st == "COMPLETE" and isinstance(n_sol, int) and n_sol >= 7 and allok
              and all(x.get("new_row_at_zero_column") == 0 for x in w))
    elif item == "V5-v2-z13-free":
        ref = sols("V4-v2-z13-free0"); res["V4_solutions"] = ref
        ok = r["returncode"] == 0 and st == "COMPLETE" and allok and isinstance(ref, int) and n_sol == 13 * ref
    elif item == "R5-r2-z13-free0":
        ref = sols("V4-v2-z13-free0"); res["V4_solutions"] = ref
        ok = r["returncode"] == 0 and st == "COMPLETE" and allok and n_sol == ref
    else:
        ok = False; res["error"] = "unknown item"
res["as_expected"] = bool(ok)
print(json.dumps(res, sort_keys=True))
sys.exit(0 if ok else 1)
