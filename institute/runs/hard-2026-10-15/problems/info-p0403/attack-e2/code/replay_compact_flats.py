"""Exactly two preserved-certificate free-flat classes; no twelve-class claim."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse
import gzip
import json
from pathlib import Path
import subprocess

CASES=[
    dict(prefix='results/dsbf40-free64',seed='dsbf40',basis=[27,45,195,325,1,2],origin=5,
         control='results/continuation-free64-control',control_log='logs/continuation-free64-control-solver.log',
         attainer='results/dsbf40-flat-attainer.json'),
    dict(prefix='results/dsbf32-free128-origin0',seed='dsbf32',basis=[63,90,139,278,1,2,4],origin=0,
         control='results/dsbf32-free128-origin0-control',control_log='logs/dsbf32-free128-origin0-control-solver.log',
         attainer='results/dsbf32-free128-origin0-control-balanced-attainer.json'),
]

def metadata(prefix):
    with gzip.open(prefix+'.encoding.json.gz','rt') as fh:
        return json.load(fh)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--independent',action='store_true')
    a=p.parse_args()
    for case in CASES:
        prefix=case['prefix']; meta=metadata(prefix)
        assert meta['seed']==case['seed'] and meta['basis']==case['basis'] and meta['origin']==case['origin']
        assert meta['bound']==28 and meta['degree_eight_necessary_constraint']
        assert meta.get('forced_truth_json') is None and meta.get('required_zero_origin') is None
        assert meta.get('canonical_support_xor') is None and not meta.get('quadratic_spectral_bit',False)
        assert len(meta['points'])==(64 if case['seed']=='dsbf40' else 128)
        if not a.independent:
            subprocess.run(['python3','code/free_flat_sat.py','--seed',case['seed'],'--basis',','.join(map(str,case['basis'])),
                            '--origin',str(case['origin']),'--prefix',prefix,'--compare'],check=True)
        subprocess.run(['python3','code/audit_free_flat.py',prefix],check=True)
        subprocess.run(['python3','code/check_lrat.py',prefix+'.cnf.gz',prefix+'.lrat.gz'],check=True)
        control=metadata(case['control'])
        assert control['points']==meta['points'] and control['seed_hex']==meta['seed_hex'] and control['bound']==32
        subprocess.run(['python3','code/audit_free_flat.py',case['control'],'--model-log',case['control_log']],check=True)
        witness=json.loads(Path(case['attainer']).read_text()); shift=witness['linear_shift']
        seed=[int(b) for c in meta['seed_hex'] for b in format(int(c,16),'04b')]
        changed={x for x,b in enumerate(map(int,witness['bits'])) if b^(bin(x&shift).count('1')%2)^seed[x]}
        assert changed<=set(meta['points'])
        subprocess.run(['python3','code/check_witness.py',case['attainer'],'--min-nl','240'],check=True)
        print('PASS exact restricted balanced maximum 240:',prefix,'free points',len(meta['points']),flush=True)
    print('PASS exactly two free-flat classes, including their models, certificates, and attainers')

if __name__=='__main__':
    main()
