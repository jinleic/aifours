#!/usr/bin/env python3
"""Run the self-authored diagnostic once with a 120 s wall cap and receipt."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, sys, time

base=Path(__file__).resolve().parent
source=base/'reviewer-f186-controls-v1.py'
stdout_path=base/'reviewer-f186-controls-stdout-v1.txt'
stderr_path=base/'reviewer-f186-controls-stderr-v1.txt'
output_path=base/'reviewer-f186-controls-output-v1.json'
receipt_path=base/'reviewer-f186-run-receipt-v1.json'
for path in [stdout_path,stderr_path,output_path,receipt_path]:
    if path.exists():raise SystemExit('refusing to overwrite '+str(path))
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
start=datetime.now(timezone.utc).isoformat(); t0=time.monotonic()
timeout=False
try:
    proc=subprocess.run([sys.executable,'-B',str(source)],cwd=base,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
    stdout,stderr,exit_code=proc.stdout,proc.stderr,proc.returncode
except subprocess.TimeoutExpired as exc:
    timeout=True;stdout,stderr,exit_code=exc.stdout or b'',exc.stderr or b'',None
end=datetime.now(timezone.utc).isoformat();wall=time.monotonic()-t0
with stdout_path.open('xb') as f:f.write(stdout)
with stderr_path.open('xb') as f:f.write(stderr)
summary=None
if output_path.exists():
    parsed=json.loads(output_path.read_text())
    # Parse every result, and validate the summary rather than trusting PASS text.
    assert isinstance(parsed['results'],list)
    assert all(set(x)=={'id','kind','as_expected','data'} for x in parsed['results'])
    expected=sum(x['as_expected'] is True for x in parsed['results'])
    unexpected=sum(x['as_expected'] is not True for x in parsed['results'])
    assert parsed['summary']['expected_outcomes']==expected
    assert parsed['summary']['unexpected_outcomes']==unexpected
    summary=parsed['summary']
receipt={'schema_version':1,'kind':'BOUNDED_INDEPENDENT_REVIEWER_CONTROL_RECEIPT','start_utc':start,'end_utc':end,'wall_seconds':wall,'wall_cap_seconds':120,'command':[sys.executable,'-B',str(source)],'stdin':'DEVNULL','exit_code':exit_code,'timed_out':timeout,'verdict':'UNKNOWN_CAP' if timeout else ('EXPECTED_OUTCOMES' if exit_code==0 and summary is not None and summary['unexpected_outcomes']==0 else 'CONTROL_FAILURE_NOT_SOURCE_VERDICT'),'summary':summary,'files':{path.name:{'sha256':sha(path),'bytes':path.stat().st_size,'LF':path.read_bytes().count(b'\n')} for path in [source,Path(__file__),stdout_path,stderr_path]+([output_path] if output_path.exists() else [])},'theorems_accepted_from_control':False}
with receipt_path.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(0 if receipt['verdict']=='EXPECTED_OUTCOMES' else 1)
