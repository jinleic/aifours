"""Run every claims.json command, with negative controls expected to fail."""
import datetime
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import time

claims=json.loads(Path('claims.json').read_text())
start=time.monotonic()
records=[]
for claim in claims['claims']:
    for field in ('verify_command','check_command','control_command'):
        cmd=claim[field]
        if not cmd: continue
        log=Path('logs/final-%s-%s.log'%(claim['cid'],field))
        print('running',claim['cid'],field,flush=True)
        with open(log,'w') as out:
            result=subprocess.run(shlex.split(cmd),stdout=out,stderr=subprocess.STDOUT,timeout=600)
        expected_nonzero=field=='control_command'
        ok=(result.returncode!=0) if expected_nonzero else result.returncode==0
        rec={'cid':claim['cid'],'field':field,'command':cmd,'exit_code':result.returncode,'expected_nonzero':expected_nonzero,'passed':ok,'log':str(log)}
        records.append(rec)
        status='PASS' if all(r['passed'] for r in records) else 'FAIL'
        data={'status':status if len(records)==sum(bool(c[k]) for c in claims['claims'] for k in ('verify_command','check_command','control_command')) else 'IN_PROGRESS','claims_sha256':hashlib.sha256(Path('claims.json').read_bytes()).hexdigest(),'commands':records,'seconds':time.monotonic()-start,'last_update_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        Path('results/final-verification.json').write_text(json.dumps(data,indent=2)+'\n')
        assert ok,rec
        print('passed',claim['cid'],field,'exit',result.returncode,flush=True)
subprocess.run(['python3','code/validate_claims.py'],check=True)
print('PASS all command replays and intentional negative controls; seconds',time.monotonic()-start,flush=True)
