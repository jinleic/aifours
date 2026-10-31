#!/usr/bin/env python3
"""Bounded source-copy LP plus all-original copy-family cutting planes.

The first LP reconstructs five copy steps of the public 1847/276 proof; further
rows are independently derived universal four-block copy-family inequalities.
All HiGHS results are floating-point proposals, never exact certificates.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
import json
import resource
import sys
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-highspy'))
OLD = Path('/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/code')
sys.path.insert(1, str(OLD))
from copy_lp import Model

spec = spec_from_file_location('frontier_cut',ROOT/'frontier-20261028-copy-family-cutting-plane.py')
cut = module_from_spec(spec); spec.loader.exec_module(cut)
base = cut.base
OUTPUT = ROOT / 'frontier-20261028-copy-branch-augmentation-result.json'
MAX_ROUNDS = 3
MAX_ROWS = 500
PER_SOLVE_SECONDS = 45.0

# Original vertices are indices 0..9. Each branch has its OWN 10,11,12.
BRANCHES = (
    (([1],[0,3,4,5,6,7,8,9]),),
    (([3,4],[0,1,2,5,6,7,8]), ([6],[0,1,2,3,11,5,7,8])),
    (([5,6],[0,1,2,3,4,7,8,9]), ([7],[0,1,2,3,4,5,10,8,9])),
)


def full_row(meta):
    n=meta['n']; a=meta['A_mask']; b=meta['B_mask']; c=meta['C_mask']
    d=meta['D_mask']; z=meta['condition_mask']; factor=n*(n+1)//2
    terms=(base.cmi(a,b,c|z,n+1)+base.cmi(a,b,d|z,n)
           +base.cmi(c,d,z,n)+base.cmi(a,b,z,-n)
           +base.cmi(a,c,b|z,factor)+base.cmi(b,c,a|z,factor))
    coeff={}
    for mask,value in terms:
        if mask:
            coeff[mask]=coeff.get(mask,0)+value
    return tuple((None,mask,value) for mask,value in sorted(coeff.items()) if value)


def write_round(record):
    target=ROOT/f"frontier-20261028-copy-branch-augmentation-round-{record['round']}.json"
    with target.open('x',encoding='utf-8') as stream:
        json.dump(record,stream,indent=2); stream.write('\n')


def main():
    t0=time.monotonic()
    group=base.automorphism_group()
    orbit,reps=base.canonical_orbits(group)
    candidate=json.loads(base.INPUT.read_bytes())
    sample=base.sample_sym_entropy(group,orbit,reps,candidate)
    masks=[]
    for v in range(1,11):
        masks.append(sum(1 << (u-1) for u in base.NEIGHBOURS[v]))
    model=Model(masks)
    for branch in BRANCHES:
        model.add_block(list(branch))
    base_ge_count, base_copy_eq_count = len(model.ge),len(model.eq)
    extras=[]; known=set(); rounds=[]
    for i in range(MAX_ROUNDS):
        t=time.monotonic()
        status,value,ncols,nrows=model.solve(extra_ge=extras,sym_perms=base.GENERATORS,
            options={'threads':1,'time_limit':PER_SOLVE_SECONDS})
        rec={'round':i,'status':status,'objective_float_unverified':value,
             'columns':ncols,'rows':nrows,'added_nonshannon_rows_before_solve':len(extras),
             'solve_elapsed_s_including_model_assembly':time.monotonic()-t,
             'max_rss_raw_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        if status!='Optimal':
            rec['stop']='not optimal; no separation based on incomplete LP'
            rounds.append(rec); write_round(rec); break
        primal=[model.last_hbase[mask] for mask in reps]
        scan_t=time.monotonic()
        checked,violations=cut.scan(primal,orbit,known)
        ordered=sorted(violations.items(),key=lambda item:item[1][0])[:MAX_ROWS]
        rec['expanded_substitutions_checked']=checked
        rec['unique_violated_orbit_rows']=len(violations)
        rec['scan_elapsed_s']=time.monotonic()-scan_t
        rec['minimum_slack_float']=min((x[0] for x in violations.values()),default=0.0)
        rec['new_rows']=[]
        for key,(slack,metadata) in ordered:
            assert sum(coef*sample[col] for col,coef in key)>-1e-8
            known.add(key); extras.append(full_row(metadata))
            rec['new_rows'].append({'slack_float':slack,'metadata':metadata})
        rec['new_rows_count']=len(ordered)
        rounds.append(rec); write_round(rec)
        if not ordered:
            break
    output={'source_paper_sha256':'373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8',
            'copy_model_source_path':str(OLD/'copy_lp.py'),
            'copy_model_source_sha256':hashlib.sha256((OLD/'copy_lp.py').read_bytes()).hexdigest(),
            'base_generator_sha256':hashlib.sha256((ROOT/'frontier-20261028-copy-family-upper-lp.py').read_bytes()).hexdigest(),
            'cutting_generator_sha256':hashlib.sha256((ROOT/'frontier-20261028-copy-family-cutting-plane.py').read_bytes()).hexdigest(),
            'copy_branches_zero_based':BRANCHES, 'group_size':len(group),
            'base_shannon_rows':base_ge_count,'base_copy_equality_rows':base_copy_eq_count,
            'solver_threads':1,'per_solve_time_limit_s':PER_SOLVE_SECONDS,
            'rounds':rounds,'total_elapsed_s':time.monotonic()-t0,
            'limits':'All numbers are floating LP proposals. Verify any improvement with a new exact dual certificate and independent checking; failure or numerical agreement is not a theorem.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(output,stream,indent=2); stream.write('\n')
    print(json.dumps({k:v for k,v in output.items() if k!='rounds'},indent=2))
    print(json.dumps([{k:v for k,v in r.items() if k!='new_rows'} for r in rounds],indent=2))


if __name__=='__main__':
    main()
