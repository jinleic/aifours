#!/usr/bin/env python3
"""In-memory test of absent vs forged launcher marker; no CRT launched."""
import hashlib
import json
import types
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launcher.py'
PIN='dc5f3f4609b037f51b81155cbcdc7c7c6ca9ed5d8178b83eca50dbd7cddb697e'
OUT=ROOT/'frontier-20261028-d4-v3-forged-marker-guard-check-results.json'
raw=SRC.read_bytes()
if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('launcher pin mismatch')
m=types.ModuleType('marker_guard_probe');m.__file__=str(SRC)
exec(compile(raw,str(SRC),'exec'),m.__dict__)
class ReachedEntrypoint(Exception):pass

def stop_before_read(*args):raise ReachedEntrypoint()

try:m.main()
except ValueError as e:missing_rejected='verified caller' in str(e)
else:missing_rejected=False
m.__dict__['__launcher_snapshot_sha__']='0'*64
m.verified_snapshot=stop_before_read
original=Path.exists
Path.exists=lambda self:False
try:
    try:m.main()
    except ReachedEntrypoint:forged_passed_marker=True
    else:forged_passed_marker=False
finally:Path.exists=original
if hashlib.sha256(SRC.read_bytes()).hexdigest()!=PIN:raise ValueError('source changed')
r={'kind':'launcher_marker_absent_vs_forged_in_memory_check',
   'launcher_sha256':PIN,'missing_marker_rejected':missing_rejected,
   'forged_64_character_marker_passes_marker_guard':forged_passed_marker,
   'crt_started':False,
   'scope':'The launcher marker itself is not authentication. The observed actual inline caller separately hashed and compiled exact launcher bytes. No real file or original target input changed; no conclusion about OS/runtime integrity or the mathematical theorem.',
   'verdict':'PASS' if missing_rejected and forged_passed_marker else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
