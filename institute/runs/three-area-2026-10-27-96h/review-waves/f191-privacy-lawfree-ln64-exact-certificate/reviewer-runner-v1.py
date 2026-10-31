#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json, subprocess, sys, time

HERE=Path(__file__).resolve().parent
MAN=HERE/'manifest-v1.json'
SRC=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-lawfree-lower-half-v1.md')
SCRIPT=HERE/'reviewer-exact-v1.py'

def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
def digest(path):
    return sha256(path.read_bytes()).hexdigest()
def exclusive(path, data):
    with path.open('xb') as f: f.write(data)

raw=SRC.read_bytes()
assert digest(MAN)=='a232531f6611ec2af301037df8eee30d156b00dcd90c8e76c90f2574b00c3011'
assert sha256(raw).hexdigest()=='ddd3fc87bd38475500589957e030119de451c6fa5f0b27ea54fb8e0856ea62ea'
assert len(raw)==34202 and raw.count(b'\n')==495 and raw.count(b'\r')==0 and raw.endswith(b'\n')
start=clock(); begin=time.monotonic()
try:
    proc=subprocess.run([sys.executable,'-B',str(SCRIPT)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,check=False)
    state='EXITED'; code=proc.returncode; out=proc.stdout; err=proc.stderr
except subprocess.TimeoutExpired as e:
    state='TIMEOUT_UNKNOWN'; code=None; out=e.stdout or b''; err=e.stderr or b''
end=clock(); elapsed=time.monotonic()-begin
outpath=HERE/'reviewer-run1-stdout-v1.json'; errpath=HERE/'reviewer-run1-stderr-v1.txt'
exclusive(outpath,out); exclusive(errpath,err)
receipt={'state':state,'exit_code':code,'timeout_seconds':120,'start_clock':start,'end_clock':end,'elapsed_monotonic_seconds':elapsed,'executable':sys.executable,'arguments':['-B',str(SCRIPT)],'manifest_sha256':digest(MAN),'input_sha256':sha256(raw).hexdigest(),'input_bytes':len(raw),'input_lf':raw.count(b'\n'),'input_cr':raw.count(b'\r'),'input_terminal_lf':raw.endswith(b'\n'),'script_sha256':digest(SCRIPT),'runner_sha256':digest(Path(__file__)),'stdout_sha256':digest(outpath),'stdout_bytes':len(out),'stderr_sha256':digest(errpath),'stderr_bytes':len(err)}
exclusive(HERE/'reviewer-run1-receipt-v1.json',(json.dumps(receipt,indent=2,sort_keys=True)+'\n').encode())
print(json.dumps(receipt,sort_keys=True))
sys.exit(0 if state=='EXITED' and code==0 else 1)
