"""Bounded SAT search without proof output. Negative statuses are not claims.

Proof-producing preliminary runs hit their size caps; this variant uses
the same audited constraints to search for a positive witness. A solver
UNSAT status alone is deliberately recorded as uncertified.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time
from seeds import fwht


def main():
    p=argparse.ArgumentParser()
    p.add_argument('prefix')
    p.add_argument('--seconds',type=int,default=600)
    a=p.parse_args()
    cnf=Path(a.prefix+'.cnf')
    assert not cnf.exists()
    cnf.write_bytes(gzip.decompress(Path(a.prefix+'.cnf.gz').read_bytes()))
    log=Path('logs/'+Path(a.prefix).name+'-search-solver.log')
    started=time.monotonic()
    with open(log,'w') as out:
        process=subprocess.Popen(['cadical','-t',str(a.seconds),str(cnf)],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
        while process.poll() is None:
            if time.monotonic()-started>a.seconds+10:
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL); process.wait()
                break
            time.sleep(.2)
    text=log.read_text()
    status=('SAT' if process.returncode==10 and 's SATISFIABLE' in text else
            'UNSAT-uncertified' if process.returncode==20 and 's UNSATISFIABLE' in text else 'UNKNOWN')
    result={'status':status,'exit_code':process.returncode,'seconds':time.monotonic()-started,
            'prefix':a.prefix,'solver_log':str(log),'proof_produced':False,
            'scope':'No negative exclusion is claimed from this search. A positive witness needs independent full verification.'}
    if status=='SAT':
        with gzip.open(a.prefix+'.encoding.json.gz','rt') as fh:
            meta=json.load(fh)
        model={}
        for line in text.splitlines():
            if line.startswith('v '):
                for literal in map(int,line.split()[1:]):
                    if literal:
                        model[abs(literal)]=literal>0
        f=[int(b) for c in meta['seed_hex'] for b in format(int(c,16),'04b')]
        for x,var in zip(meta['points'],meta['xs']):
            f[x]=int(model[var])
        W=fwht(f)
        assert max(map(abs,W))<=28 and 0 in W
        shift=W.index(0)
        f=[b^(bin(x&shift).count('1')%2) for x,b in enumerate(f)]
        bits=''.join(map(str,f)); W=fwht(f)
        witness={'bits':bits,'bit_order':'bits[x]=f(x); x_i=(x>>i)&1',
                 'sha256_ascii_bits':hashlib.sha256(bits.encode()).hexdigest(),'weight':sum(f),
                 'walsh':W,'nonlinearity':256-max(map(abs,W))//2,'linear_shift':shift}
        target=a.prefix+'-witness.json'
        Path(target).write_text(json.dumps(witness,indent=2)+'\n')
        subprocess.run(['python3','code/check_witness.py',target],check=True)
        result['independently_verified_witness']=target
    cnf.unlink()
    Path(a.prefix+'-search-run.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__':
    main()
