#!/usr/bin/env python3
"""In-memory guards for verified launcher and v2 entrypoint snapshots."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LAUNCHER=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launcher.py'
PIN='dc5f3f4609b037f51b81155cbcdc7c7c6ca9ed5d8178b83eca50dbd7cddb697e'
OUT=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-fault-check-results.json'
raw=LAUNCHER.read_bytes()
if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('launcher mismatch')
spec=importlib.util.spec_from_file_location('launcher_guard_test',LAUNCHER)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks={}
checks['real_v2_snapshot_accepted']=hashlib.sha256(m.verified_snapshot(m.V2,m.PIN_V2)).hexdigest()==m.PIN_V2
checks['tampered_launcher_snapshot_rejected']=hashlib.sha256(raw+b'\x00').hexdigest()!=PIN
try:m.main()
except ValueError as e:checks['unverified_caller_rejected']='verified caller' in str(e)
else:checks['unverified_caller_rejected']=False
original=Path.read_bytes
def altered(self):
    b=original(self)
    return b+b'\x00' if self==m.V2 else b
Path.read_bytes=altered
try:
    try:m.verified_snapshot(m.V2,m.PIN_V2)
    except ValueError as e:checks['tampered_v2_snapshot_rejected']='SHA mismatch' in str(e)
    else:checks['tampered_v2_snapshot_rejected']=False
finally:Path.read_bytes=original
checks['actual_v2_bytes_unchanged']=hashlib.sha256(m.V2.read_bytes()).hexdigest()==m.PIN_V2
checks['actual_launcher_bytes_unchanged']=hashlib.sha256(LAUNCHER.read_bytes()).hexdigest()==PIN
r={'kind':'entrypoint_snapshot_launcher_in_memory_guard_controls',
   'launcher_sha256':PIN,'v2_sha256':m.PIN_V2,'controls':checks,
   'scope':'In-memory launcher/entrypoint guard sensitivity only; not a CRT run or runtime-integrity, physical theorem, formal or model-family proof. No source file is modified.',
   'verdict':'PASS' if all(checks.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
