"""Float headroom assay beyond the claimed asymptotic 0.2029161 (Gaussian-limit, exploration only; NOT a certificate).

python assay.py LANE_ID CONFIG_JSON_LIST
Each config: {"eta":..,"k":..,"res":"0,1","K":..,"D":..,"iters":..,"init":null|path,"tag":..}
Runs opt2_gauss.py (deterministic grid init: mus 10..90, ws 3..30, qs {0.4,0.45,0.5}; no random seed unless
init is a padded code) and appends one JSON line per config to ../evidence/gauss/assay_lane<ID>.jsonl.
"""
import json
import subprocess
import sys
import time

lane, configs = sys.argv[1], json.loads(sys.argv[2])
out = open(f"../evidence/gauss/assay_lane{lane}.jsonl", "a")
for c in configs:
    cmd = ["../env/bin/python", "opt2_gauss.py", "--eta", str(c["eta"]), "--k", str(c["k"]), "--res", c["res"],
           "--K", str(c["K"]), "--D", str(c["D"]), "--iters", str(c["iters"]), "--tag", c["tag"]]
    if c.get("init"):
        cmd += ["--init", c["init"]]
    if c.get("qs"):
        cmd += ["--qs", c["qs"]]
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    last = [l for l in p.stdout.splitlines() if l.startswith("{")]
    rec = {"config": c, "returncode": p.returncode, "secs": round(time.time() - t0, 1),
           "result": json.loads(last[-1]) if last else None, "stderr_tail": p.stderr[-300:]}
    out.write(json.dumps(rec) + "\n")
    out.flush()
