#!/usr/bin/env python3
"""verify_solution_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Post-solve chain for ONE solver output:
 (1) encoder 'decode' -> raw k x n DM (exclusive create);
 (2) encoder 'evaluate' of that raw DM against the same model (all clauses, incl. group transport);
 (3) checker A (cfr21/code/check_dm_mols_cfr_v1.py, accepted controls) with k rows;
 (4) for 7-row outputs: an explicit list-of-six-squares file is NOT written here (derivation is checker A's bridge).
Args: encoder enc_sha model model_sha solver_stdout stdout_sha out_dir(new) checker checker_sha python"""
import sys, os, json, hashlib, subprocess
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
enc, enc_sha, model, model_sha, sout, sout_sha, outd, chk, chk_sha, py = sys.argv[1:11]
for p, w in ((enc, enc_sha), (model, model_sha), (sout, sout_sha), (chk, chk_sha)):
    if sha(p) != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p})); sys.exit(2)
os.makedirs(outd, exist_ok=False)
env = {"PATH": "/usr/bin:/bin", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C"}
raw = os.path.join(outd, 'solution.raw')
r1 = subprocess.run([py, '-I', '-B', enc, 'decode', model, sout, raw], capture_output=True, text=True, stdin=subprocess.DEVNULL, env=env)
d1 = json.loads(r1.stdout) if r1.returncode == 0 else {"error": r1.stderr[-2000:]}
M = json.load(open(model)); k, n = M["k"], M["n"]
r2 = subprocess.run([py, '-I', '-B', enc, 'evaluate', model, raw], capture_output=True, text=True, stdin=subprocess.DEVNULL, env=env)
d2 = json.loads(r2.stdout) if r2.stdout.strip() else {"error": r2.stderr[-2000:]}
r3 = subprocess.run([py, '-I', '-B', chk, raw, str(n), str(k)], capture_output=True, text=True, stdin=subprocess.DEVNULL, env=env)
d3 = json.loads(r3.stdout) if r3.stdout.strip() else {"error": r3.stderr[-2000:]}
res = {"decode": d1, "evaluate": {kk: d2.get(kk) for kk in ("verdict", "violated_by_tag", "clauses", "affine_consistent")},
       "checker_A": {kk: d3.get(kk) for kk in ("overall", "dm_verdict", "mols_verdict", "cfr_verdict", "mols_count", "cfr_rows", "input_sha256")},
       "checker_A_returncode": r3.returncode, "raw_sha256": sha(raw) if os.path.exists(raw) else None}
res["chain_verdict"] = "VALID" if (d2.get("verdict") == "SATISFIES_ALL" and d3.get("overall") == "PASS") else "NOT_VALID"
with open(os.path.join(outd, 'verify.json'), 'x') as f: json.dump(res, f, indent=1)
print(json.dumps({"chain_verdict": res["chain_verdict"], "raw_sha256": res["raw_sha256"], "checker_A": res["checker_A"].get("overall"),
                  "evaluate": res["evaluate"].get("verdict")}))
