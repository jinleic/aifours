#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,time
here=Path(__file__).resolve().parent
script=here/'reviewer-boundary-v1.py'
manifest=here/'manifest-v1.json'
source=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-lawfree-lower-half-v1.md')
def hashfile(p): return sha256(p.read_bytes()).hexdigest()
def clock(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
def put(p,b):
    with p.open('xb') as f: f.write(b)
raw=source.read_bytes()
assert hashfile(manifest)=='a232531f6611ec2af301037df8eee30d156b00dcd90c8e76c90f2574b00c3011'
assert sha256(raw).hexdigest()=='ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea' and len(raw)==34202 and raw.count(b'\n')==495
begin=clock(); t0=time.monotonic()
try:
    p=subprocess.run([sys.executable,'-B',str(script)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,check=False)
    state='EXITED'; rc=p.returncode; out=p.stdout; err=p.stderr
except subprocess.TimeoutExpired as e:
    state='TIMEOUT_UNKNOWN'; rc=None; out=e.stdout or b''; err=e.stderr or b''
end=clock(); elapsed=time.monotonic()-t0
op=here/'reviewer-boundary-run1-stdout-v1.json'; ep=here/'reviewer-boundary-run1-stderr-v1.txt'
put(op,out); put(ep,err)
r={'state':state,'exit_code':rc,'start_clock':begin,'end_clock':end,'elapsed_monotonic_seconds':elapsed,'timeout_seconds':120,'executable':sys.executable,'arguments':['-B',str(script)],'manifest_sha256':hashfile(manifest),'input_sha256':sha256(raw).hexdigest(),'input_bytes':len(raw),'input_lf':raw.count(b'\n'),'script_sha256':hashfile(script),'runner_sha256':hashfile(Path(__file__)),'stdout_sha256':hashfile(op),'stdout_bytes':len(out),'stderr_sha256':hashfile(ep),'stderr_bytes':len(err)}
put(here/'reviewer-boundary-run1-receipt-v1.json',(json.dumps(r,indent=2,sort_keys=True)+'\n').encode())
print(json.dumps(r,sort_keys=True))
sys.exit(0 if state=='EXITED' and rc==0 else 1)
