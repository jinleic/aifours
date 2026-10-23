#!/usr/bin/env python3
"""make_jobs_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Deterministically builds run_native_v2 job JSONs
(exclusive create) from a pinned wave spec and the pinned CNFs it names. Each job pins its CNF (path, sha256) and
model; argv uses absolute solver paths and the solver's own self time limit (CaDiCaL -t, Kissat --time).
Args: wave_spec spec_sha go_path go_sha out_dir(new)"""
import sys, os, json, hashlib
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
spec_p, spec_sha, go_p, go_sha, outd = sys.argv[1:6]
if sha(spec_p) != spec_sha or sha(go_p) != go_sha: print(json.dumps({"status": "PIN_MISMATCH"})); sys.exit(2)
spec = json.load(open(spec_p)); os.makedirs(outd, exist_ok=False)
SOLVERS = {"cadical": "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical", "kissat": "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"}
SOLVER_SHA = {"cadical": "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa",
              "kissat": "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848"}
out = []
for j in spec["jobs"]:
    cnf = j["cnf"]; s = j["solver"]; seed = int(j["seed"]); B = int(j["budget_s"])
    if s == "cadical": argv = [SOLVERS[s], "--seed=%d" % seed, "-q", "-t", str(B), cnf]
    else: argv = [SOLVERS[s], "--seed=%d" % seed, "-q", "--time=%d" % B, cnf]
    job = {"item": j["item"], "go_path": go_p, "go_sha256": go_sha, "argv": argv, "budget_s": B,
           "inputs": [{"path": cnf, "sha256": sha(cnf)}, {"path": SOLVERS[s], "sha256": SOLVER_SHA[s]},
                      {"path": j["model"], "sha256": sha(j["model"])}],
           "rss_cap_bytes": int(spec["rss_cap_bytes"]), "stdout_cap_bytes": 16 * 1024 * 1024, "stderr_cap_bytes": 1024 * 1024,
           "projected_disk_bytes": int(spec["projected_disk_bytes"]), "long_job": bool(j.get("long_job", False)),
           "model": j["model"], "on_sat": "pin stdout; run verify_solution_v1.py; stop target wave; notify parent"}
    p = os.path.join(outd, j["item"] + ".json")
    with open(p, 'x') as f: f.write(json.dumps(job, indent=1) + "\n")
    out.append({"item": j["item"], "job": p, "sha256": sha(p)})
print(json.dumps({"status": "OK", "jobs": out}))
