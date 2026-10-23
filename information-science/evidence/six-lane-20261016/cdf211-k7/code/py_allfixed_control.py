"""Positive control for the ORIGINAL Python routine multiplier_headroom.order3_all_fixed (unchanged code,
imported, not copied): run it on prime p with cap=1 and NO node cap, then record the result.
usage: python3 py_allfixed_control.py P OUT_JSON
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multiplier_headroom import order3_all_fixed

p, out = int(sys.argv[1]), sys.argv[2]
t0 = time.time(); started = time.strftime("%Y-%m-%dT%H:%M:%S%z")
rec = order3_all_fixed(p, cap=1, node_cap=None)
rec.update(started=started, finished=time.strftime("%Y-%m-%dT%H:%M:%S%z"), wall_s=round(time.time() - t0, 1))
json.dump(rec, open(out, "w"), indent=1, default=str)
print(json.dumps(rec, default=str)[:1500])
