"""Reproduce and independently verify a complete scoped exclusion.

--independent never imports producer code. Its semantic encoding audit
and proof checker are separate programs. Both modes check all required
lower radii, all three exact-radius certificates, and the planted SAT
control. No SAT result is inferred from a solver's printed status.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def run(args):
    print('+',' '.join(args),flush=True)
    subprocess.run(args,check=True)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--radius',type=int,choices=(6,8,10),default=6)
    p.add_argument('--independent',action='store_true')
    args=p.parse_args()
    run(['python3','code/check_radius2.py'])
    run(['python3','code/check_radius4.py'])
    for radius in range(6,args.radius+1,2):
        for seed in ('dsbf40','dsbf32','rsbf56'):
            prefix='results/%s-r%d'%(seed,radius)
            meta=json.loads(Path(prefix+'.encoding.json').read_text())
            assert meta['seed']==seed and meta['radius_exact']==radius and meta['bound']==28
            assert meta['forced_points'] is None
            assert not meta['degree_eight_necessary_constraint']
            if not args.independent:
                # Rebuild the question-to-CNF translation, then check it
                # using independently reconstructed semantics below.
                from local_sat import produce
                cnf,_=produce(seed,radius,28)
                txt='p cnf %d %d\n'%(cnf.n,len(cnf.clauses))+''.join(' '.join(map(str,c))+' 0\n' for c in cnf.clauses)
                assert hashlib.sha256(txt.encode()).hexdigest()==meta['cnf_sha256']
                assert Path(prefix+'.cnf').read_text()==txt
            run(['python3','code/audit_local_sat.py',prefix])
            proof=prefix+'-trimmed.lrat.gz'
            if not Path(proof).exists(): proof=prefix+'.lrat.gz'
            run(['python3','code/check_lrat.py',prefix+'.cnf',proof])
    run(['python3','code/audit_local_sat.py','results/control-r6-planted','--model-log','logs/control-r6-planted-solver.log'])
    run(['python3','code/check_witness.py','results/control-r6-planted-witness.json','--min-nl','240'])
    print('PASS complete scoped exclusion through radius',args.radius,flush=True)


if __name__=='__main__': main()
