"""Finite one-shot scientific checkpoint at a host-clock deadline. Does not
launch/stop/restart any solver, and is not an autonomous research scheduler.
Captures complete receipt lines, counts and disk once, then exits. This keeps
long bounded passes observable within the30-minute checkpoint contract.
"""
import argparse
import hashlib
import json
import shutil
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ap=argparse.ArgumentParser()
ap.add_argument('--at',type=float,required=True)
ap.add_argument('--results',required=True)
ap.add_argument('--out',required=True)
a=ap.parse_args()
remaining=a.at-time.time()
if remaining>0:
    time.sleep(remaining)
p=Path(a.results)
b=p.read_bytes() if p.exists() else b''
lines=b.splitlines(keepends=True)
rows=[]
for line in lines:
    if line.endswith(b'\n'):
        rows.append(json.loads(line))
r={'host_time':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
   'source':str(p),'snapshot_sha256':hashlib.sha256(b).hexdigest(),
   'complete_receipts':len(rows),'strict_ok':sum(x.get('strict_ok') is True for x in rows),
   'unknown':[x['id'] for x in rows if x.get('strict_ok') is not True],
   'peak_completed_leaf_rss':max((x.get('aggregate_peak_rss_bytes',0) for x in rows),default=0),
   'free_bytes':shutil.disk_usage(p.parent).free,'one_shot':True}
with Path(a.out).open('x') as f:
    json.dump(r,f,indent=1)
print(json.dumps(r),flush=True)
