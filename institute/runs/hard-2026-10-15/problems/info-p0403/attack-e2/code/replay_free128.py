"""Rebuild and replay checked quarter-table class exclusions and controls."""
import argparse
import json
from pathlib import Path
import subprocess


p=argparse.ArgumentParser()
p.add_argument('--independent',action='store_true')
a=p.parse_args()
batch=json.loads(Path('results/free128-batch.json').read_text())
assert batch['complete'] and batch['planned_cases']==len(batch['cases'])==12
seeds={}
for case in batch['cases']:
    prefix=case['prefix']
    meta=json.loads(Path(prefix+'.encoding.json').read_text())
    assert meta['bound']==28 and len(meta['points'])==128
    assert meta.get('forced_truth_json') is None and meta.get('required_zero_origin') is None
    assert meta['degree_eight_necessary_constraint'] and not meta.get('quadratic_spectral_bit',False)
    assert meta.get('canonical_support_xor') is None
    seeds.setdefault(case['seed'],[]).append((case,meta))
    if not a.independent:
        subprocess.run(['python3','code/free_flat_sat.py','--seed',case['seed'],'--basis',','.join(map(str,case['basis'])),'--origin',str(case['origin']),'--prefix',prefix,'--compare'],check=True)
    subprocess.run(['python3','code/audit_free_flat.py',prefix],check=True)
    subprocess.run(['python3','code/check_lrat.py',prefix+'.cnf',prefix+'.lrat.gz'],check=True)
    subprocess.run(['python3','code/audit_free_flat.py',case['control_prefix'],'--model-log',case['control_model_log']],check=True)
    attainer=case['control_prefix']+'-balanced-attainer.json'
    subprocess.run(['python3','code/check_witness.py',attainer,'--min-nl','240'],check=True)
    balanced=json.loads(Path(attainer).read_text())
    inp=json.loads(Path(case['control_prefix']+'-input.json').read_text())
    shift=balanced['linear_shift']
    assert all(int(balanced['bits'][x])^(bin(x&shift).count('1')%2)==int(inp['bits'][x]) for x in range(512))
flat=json.loads(Path('results/flat-class.json').read_text())
for seed,cases in seeds.items():
    assert len(cases)==4
    basis=cases[0][0]['basis']; V={0}
    for b in basis: V|={v^b for v in list(V)}
    assert len(V)==128
    reps=sorted({min(x^v for v in V) for x in range(512)})
    assert sorted(c['coset_representative'] for c,m in cases)==reps
    assert all(c['basis']==basis for c,m in cases)
    assert all(min(m['points'])==c['coset_representative'] for c,m in cases)
    domains=[set(m['points']) for c,m in cases]
    assert len(set.union(*domains))==512 and all(len(x&y)==0 for i,x in enumerate(domains) for y in domains[i+1:])
    assert any(set(flat['seeds'][seed]['free_points_sorted'])<=points for points in domains)
    subprocess.run(['python3','code/check_witness.py',flat['seeds'][seed]['attainer'],'--min-nl','240'],check=True)
assert set(seeds)=={'dsbf40','dsbf32','rsbf56'}
print('PASS all twelve quarter-table class certificates, controls, coverage, and attaining balanced tables')
