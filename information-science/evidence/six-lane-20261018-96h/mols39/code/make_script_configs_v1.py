#!/usr/bin/env python3
"""make_script_configs_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Deterministically writes one
owned_supervisor_v2.py config per stdlib-script job of a pinned job list, each in a NEW job directory (exclusive).
Child argv = [python, -I, -B, go_exec_shim_v1.py, python, -I, -B, <script>, args...]: the shim execs the interpreter only
after the supervisor's launch record and GO line. Args: jobs_json jobs_sha go_record go_sha out_base(new)"""
import sys, os, json, hashlib, datetime
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
jp, jsha, gp, gsha, outb = sys.argv[1:6]
if sha(jp) != jsha or sha(gp) != gsha: print(json.dumps({"status": "PIN_MISMATCH"})); sys.exit(2)
spec = json.load(open(jp)); os.makedirs(outb, exist_ok=False)
LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
PY = '/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python'
SHIM = LANE + '/code/go_exec_shim_v1.py'
SETTLE_BY = datetime.datetime.fromisoformat('2026-10-22T21:56:33-07:00').timestamp()
env = {"PATH": "/usr/bin:/bin", "TMPDIR": LANE + "/tmp", "HOME": LANE + "/tmp", "LC_ALL": "C", "PYTHONDONTWRITEBYTECODE": "1",
       "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"}
res = []
for j in spec["jobs"]:
    d = os.path.join(outb, j["item"]); os.makedirs(d, exist_ok=False)
    args = [a.replace("@JOBDIR@", d) for a in j["args"]]
    argv = [PY, "-I", "-B", SHIM, PY, "-I", "-B", j["script"]] + args
    cfg = {"lane": LANE, "argv": argv, "env": env,
           "stdout": os.path.join(d, "stdout.txt"), "stderr": os.path.join(d, "stderr.txt"),
           "outputs": [os.path.join(d, "stdout.txt"), os.path.join(d, "stderr.txt")],
           "launch_record": os.path.join(d, "launch.json"), "samples": os.path.join(d, "samples.jsonl"),
           "receipt": os.path.join(d, "receipt.json"),
           "pins": [{"path": p_["path"], "sha256": p_["sha256"]} for p_ in j["pins"]] +
                   [{"path": SHIM, "sha256": sha(SHIM)}, {"path": PY, "sha256": sha(PY)}, {"path": j["script"], "sha256": sha(j["script"])}],
           "max_wall_s": int(j["max_wall_s"]), "rss_trip_bytes": int(j["rss_trip_bytes"]), "free_trip_bytes": 12000000000,
           "output_trip_bytes": int(j["output_trip_bytes"]), "launch_free_min_bytes": 12200000000 + int(j["reserve_bytes"]),
           "sample_s": int(j.get("sample_s", 2)), "settle_s": 120, "max_chunk_seconds": 10800, "owned_compute_settled_by_epoch": SETTLE_BY,
           "meta": {"item": j["item"], "go_record": gp, "go_sha256": gsha, "role": j.get("role")}}
    cp = os.path.join(d, "config.json")
    with open(cp, 'x') as f: f.write(json.dumps(cfg, indent=1) + "\n")
    res.append({"item": j["item"], "config": cp, "sha256": sha(cp)})
print(json.dumps({"status": "OK", "configs": res}))
