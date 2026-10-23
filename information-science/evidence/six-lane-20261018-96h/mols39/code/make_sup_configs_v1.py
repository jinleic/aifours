#!/usr/bin/env python3
"""make_sup_configs_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Deterministically writes one
owned_supervisor_v2.py config per job of a pinned wave spec, each in a NEW job directory (exclusive creates).
Child argv = [python, -I, -B, go_exec_shim_v1.py, <solver abs path>, solver args..., <cnf>]; the solver's own time
limit (CaDiCaL -t B / Kissat --time=B) is the self-budget; the supervisor deadline is B + 60 s as backstop.
Args: wave_spec spec_sha go_record go_sha out_base(new)"""
import sys, os, json, hashlib, datetime
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
spec_p, spec_sha, go_p, go_sha, outb = sys.argv[1:6]
if sha(spec_p) != spec_sha or sha(go_p) != go_sha: print(json.dumps({"status": "PIN_MISMATCH"})); sys.exit(2)
spec = json.load(open(spec_p))
LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
PY = '/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python'
SHIM = LANE + '/code/go_exec_shim_v1.py'
SOLVERS = {"cadical": ("/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical", "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa"),
           "kissat": ("/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat", "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848")}
SETTLE_BY = datetime.datetime.fromisoformat('2026-10-22T21:56:33-07:00').timestamp()
os.makedirs(outb, exist_ok=False)
env = {"PATH": "/usr/bin:/bin", "TMPDIR": LANE + "/tmp", "HOME": LANE + "/tmp", "LC_ALL": "C", "PYTHONDONTWRITEBYTECODE": "1",
       "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"}
res = []
for j in spec["jobs"]:
    d = os.path.join(outb, j["item"]); os.makedirs(d, exist_ok=False)
    solver, ssha = SOLVERS[j["solver"]]; B = int(j["budget_s"]); seed = int(j["seed"])
    if j["solver"] == "cadical": sargs = ["--seed=%d" % seed, "-q", "-t", str(B)]
    else: sargs = ["--seed=%d" % seed, "-q", "--time=%d" % B]
    argv = [PY, "-I", "-B", SHIM, solver] + sargs + [j["cnf"]]
    cfg = {"lane": LANE, "argv": argv, "env": env,
           "stdout": os.path.join(d, "stdout.txt"), "stderr": os.path.join(d, "stderr.txt"),
           "outputs": [os.path.join(d, "stdout.txt"), os.path.join(d, "stderr.txt")],
           "launch_record": os.path.join(d, "launch.json"), "samples": os.path.join(d, "samples.jsonl"),
           "receipt": os.path.join(d, "receipt.json"),
           "pins": [{"path": j["cnf"], "sha256": sha(j["cnf"])}, {"path": solver, "sha256": ssha},
                    {"path": SHIM, "sha256": sha(SHIM)}, {"path": PY, "sha256": sha(PY)}, {"path": j["model"], "sha256": sha(j["model"])}],
           "max_wall_s": B + 60, "rss_trip_bytes": int(spec["rss_trip_bytes"]), "free_trip_bytes": 12000000000,
           "output_trip_bytes": 17 * 1024 * 1024, "launch_free_min_bytes": 12200000000 + int(spec["projected_disk_bytes"]),
           "sample_s": 10, "settle_s": 120, "max_chunk_seconds": 10800, "owned_compute_settled_by_epoch": SETTLE_BY,
           "meta": {"item": j["item"], "go_record": go_p, "go_sha256": go_sha, "model": j["model"], "solver": j["solver"],
                    "seed": seed, "self_budget_s": B, "long_job": bool(j.get("long_job", False)),
                    "on_sat": "pin stdout; run verify_solution_v1.py; for Z39 targets stop the wave and notify parent"}}
    cp = os.path.join(d, "config.json")
    with open(cp, 'x') as f: f.write(json.dumps(cfg, indent=1) + "\n")
    res.append({"item": j["item"], "config": cp, "sha256": sha(cp), "long_job": cfg["meta"]["long_job"]})
print(json.dumps({"status": "OK", "configs": res}))
