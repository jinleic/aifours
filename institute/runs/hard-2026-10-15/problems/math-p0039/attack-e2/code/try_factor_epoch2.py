#!/usr/bin/env python3
"""One-CPU, 300-second optional witness search at the next family exponent.
No negative/primality claim follows from an empty search. A positive factor is
independently checked using Python before it is reported as a witness. This is
production only and is never a claims.json replay command.
"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time


def main():
    command=['code/factor_progression','59049','1000000000000000','300']
    record=dict(command=command,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                source_sha256=hashlib.sha256(Path('code/factor_progression.c').read_bytes()).hexdigest(),
                binary_sha256=hashlib.sha256(Path('code/factor_progression').read_bytes()).hexdigest(),
                cpu_workers=1,cap_seconds=300,
                limitation='Only a verified positive proper factor can eliminate this case; no factor means inconclusive.')
    output=Path('evidence/epoch2/factor-59049-extended.json')
    output.write_text(json.dumps(record,indent=2)+'\n');begin=time.monotonic()
    result=subprocess.run(command,capture_output=True,text=True,timeout=330,check=True)
    data=json.loads(result.stdout);q=data['proper_factor'];a=data['a']
    if q:
        residue=pow(2,a,q)
        assert 1<q<(1<<(2*a)) and (residue*residue+residue+1)%q==0
        assert residue==data['two_to_a_mod_factor']
    record.update(seconds=time.monotonic()-begin,result=data,verified_positive_factor=q or None,
                  last_tested_k=(data['last_q']-1)//(6*a) if data['last_q'] else 0)
    output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()
