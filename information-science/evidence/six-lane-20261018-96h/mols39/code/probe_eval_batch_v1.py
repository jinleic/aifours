#!/usr/bin/env python3
"""probe_eval_batch_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; self budget 270 s).
Encoder soundness controls: for each case (model, raw DM, expected verdict) run the frozen encoder's 'evaluate'
logic (sym_dm_cnf_v1.py, imported by path after a SHA-256 pin check) and compare with the expected verdict and,
for VIOLATES cases, the expected violated tags. Args: encoder_path encoder_sha cases_json cases_sha"""
import sys, json, hashlib, time, importlib.util, io, contextlib
T0 = time.monotonic(); BUD = 270.0
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
pinned(sys.argv[1], sys.argv[2]); cases = json.loads(pinned(sys.argv[3], sys.argv[4]))
spec = importlib.util.spec_from_file_location("symenc", sys.argv[1]); mod = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True; spec.loader.exec_module(mod)
res = []; ok_all = True
for c in cases["cases"]:
    if time.monotonic() - T0 > BUD: res.append({"case": c["name"], "status": "NOT_RUN_BUDGET"}); ok_all = False; continue
    pinned(c["model"], c["model_sha256"]); pinned(c["raw"], c["raw_sha256"])
    buf = io.StringIO(); old = sys.argv
    sys.argv = ["sym_dm_cnf_v1.py", "evaluate", c["model"], c["raw"]]
    with contextlib.redirect_stdout(buf): rc = mod.main()
    sys.argv = old
    out = json.loads(buf.getvalue())
    good = out.get("verdict") == c["expected"]
    if good and c["expected"] == "VIOLATES":
        tags = set(out["violated_by_tag"])
        good = tags == set(c["expected_tags"])
    if not good: ok_all = False
    res.append({"case": c["name"], "expected": c["expected"], "expected_tags": c.get("expected_tags"),
                "verdict": out.get("verdict"), "violated_by_tag": out.get("violated_by_tag"), "clauses": out.get("clauses"),
                "affine_consistent": out.get("affine_consistent"), "error": out.get("error"), "wall_s": out.get("wall_s"),
                "match": good})
print(json.dumps({"status": "OK", "all_match": ok_all, "results": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))
