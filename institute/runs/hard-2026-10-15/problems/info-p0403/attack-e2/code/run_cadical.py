"""Bounded production solver run with process/file resource limits."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time

p=argparse.ArgumentParser()
p.add_argument('prefix')
p.add_argument('--seconds',type=int,default=180)
p.add_argument('--proof-mb',type=int,default=220)
a=p.parse_args()
proof=Path(a.prefix+'.lrat.gz')
log=Path('logs/'+Path(a.prefix).name+'-solver.log')
start=time.monotonic()
with open(log,'w') as output:
    process=subprocess.Popen(['cadical','-t',str(a.seconds),'--lrat','--no-binary',a.prefix+'.cnf',str(proof)],stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
    reason=None
    while process.poll() is None:
        if time.monotonic()-start>a.seconds+10: reason='wall limit'
        if proof.exists() and proof.stat().st_size>a.proof_mb*1024**2: reason='proof-size limit'
        if reason:
            os.killpg(process.pid,signal.SIGTERM)
            try: process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL); process.wait()
            break
        time.sleep(.2)
    code=process.returncode
text=log.read_text()
status='UNSAT' if code==20 and 's UNSATISFIABLE' in text else 'SAT' if code==10 and 's SATISFIABLE' in text else 'UNKNOWN'
result={'status':status,'exit_code':code,'seconds':time.monotonic()-start,'prefix':a.prefix,'solver_log':str(log),'proof_limit_mb':a.proof_mb,'stop_reason':reason,'scope':'Solver status is not an accepted negative claim until encoding and proof are independently checked.'}
if proof.exists():
    result['proof_bytes']=proof.stat().st_size
    result['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
    if status=='UNKNOWN':
        proof.unlink()
        result['partial_trace_discarded']=True
Path(a.prefix+'-run.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
