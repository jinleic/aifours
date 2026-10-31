#!/usr/bin/env python3
"""Compare fully bound v3 receipt against pinned v2, without recomputing residues."""
import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
V2=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2-results.json'
V3=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-results.json'
PROG=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-progress.json'
LAUNCH=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-launch-receipt.json'
PINS={V2:'853f035099a6dadcf3a7fe6bdc1b368612670010e3523aa557ec2f643c3759c7',
      V3:'50f53a57e59eda9f40bb28ba2df1feb9ace8ce43e3a2d60530b1db8a34c95687',
      PROG:'5e7b5b7ce715a27e132d54844e895550509d78d7adaefbbb6898384275618810',
      LAUNCH:'8c92e424d87c9b372bb4ba5a303b07401642db69a9e491162f262030f1910350'}
OUT=ROOT/'frontier-20261028-d4-reverse-entrypoint-v3-receipt-check-results.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compare(a,b,progress,launch):
    fields=('archive_sha256','corrected_data_sha256','base_helper_sha256','helper_loading',
            'prime_count','primes_tested','prime_product','prime_product_bits','height_bound',
            'height_bound_bits','common_denominator_bits','orbit_counts','physical_row_pair_occurrences',
            'row_pattern_groups','independent_site_maps','independent_aux_maps','independent_equality_specs',
            'max_local_map','max_equality_map','max_W','block_factor','equality_part_factor',
            'max_objective_numerator','first_prime_residuals','in_memory_aab_plus_one_fault_residuals',
            'nonzero_residue_primes','product_exceeds_twice_fresh_bound','verdict')
    bad=[k for k in fields if a[k]!=b[k]]
    if progress['state']!='PRIMES_COMPLETE' or progress['tested_count']!=424 or progress['bad_primes']:bad.append('progress')
    if launch['verdict']!='PASS' or launch['main_return_code']!=0 or launch['result_sha256']!=PINS[V3] or launch['progress_sha256']!=PINS[PROG]:bad.append('launch')
    if launch['launcher_snapshot_sha256']!='dc5f3f4609b037f51b81155cbcdc7c7c6ca9ed5d8178b83eca50dbd7cddb697e' or launch['v2_executed_snapshot_sha256']!='425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971':bad.append('source_binding')
    return bad

if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('pinned input mismatch')
a=json.loads(V2.read_bytes());b=json.loads(V3.read_bytes());progress=json.loads(PROG.read_bytes());launch=json.loads(LAUNCH.read_bytes())
bad=compare(a,b,progress,launch);faults={}
for name in ('height_bound','prime_product','base_helper_sha256'):
    altered=copy.deepcopy(b);altered[name]=str(altered[name])+'0'
    faults['tampered_'+name]=bool(compare(a,altered,progress,launch))
altered=copy.deepcopy(launch);altered['v2_executed_snapshot_sha256']='0'*64
faults['tampered_entrypoint_binding']=bool(compare(a,b,progress,altered))
altered=copy.deepcopy(progress);altered['state']='INCOMPLETE'
faults['incomplete_progress']=bool(compare(a,b,altered,launch))
if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('inputs changed')
r={'kind':'stdlib_entrypoint_snapshot_v3_receipt_comparison','v2_result_sha256':PINS[V2],
   'v3_result_sha256':PINS[V3],'v3_progress_sha256':PINS[PROG],'launch_receipt_sha256':PINS[LAUNCH],
   'mismatched_fields':bad,'fault_controls_detected':faults,
   'scope':'Receipt equality/source-binding metadata only; does not recompute orbit residues or establish Python/OS runtime integrity, physical theorem, formal or independent-family review.',
   'verdict':'PASS' if not bad and all(faults.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
