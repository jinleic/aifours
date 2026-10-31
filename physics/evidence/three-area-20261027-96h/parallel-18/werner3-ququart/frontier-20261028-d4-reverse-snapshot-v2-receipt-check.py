#!/usr/bin/env python3
"""Stdlib comparison of pinned v2/v1 complete reverse-CRT receipts.

Does not recompute any orbit residue. Checks actual input-bound v2 fields and
exact D-bit/B/P/prime data against the independently audited v1 receipt.
"""
import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OLD=ROOT/'frontier-20261028-d4-reverse-independent-crt-check-results.json'
NEW=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2-results.json'
PROG=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2-progress.json'
V2=ROOT/'frontier-20261028-d4-reverse-snapshot-crt-v2.py'
BASE=ROOT/'frontier-20261028-independent-d4-base-check.py'
PINS={OLD:'3afc85cf5f47645314fa4ec369247f357c6e415a834707e273425253eea0ca19',
      NEW:'853f035099a6dadcf3a7fe6bdc1b368612670010e3523aa557ec2f643c3759c7',
      PROG:'97c1b7d00ab28496b5fc5965b1b9539ccbf404b60a1d262f05a6bea571585dea',
      V2:'425e5d827f1f4a9592732a124b5f791ebef90148c114084696131c81b9d7f971',
      BASE:'bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec'}
OUT=ROOT/'frontier-20261028-d4-reverse-snapshot-v2-receipt-check-results.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def compare(a,b,progress):
    shared=('archive_sha256','corrected_data_sha256','prime_count','primes_tested',
            'prime_product','prime_product_bits','height_bound','height_bound_bits',
            'common_denominator_bits','orbit_counts','physical_row_pair_occurrences',
            'row_pattern_groups','independent_site_maps','independent_aux_maps',
            'independent_equality_specs','max_local_map','max_equality_map','max_W',
            'block_factor','equality_part_factor','max_objective_numerator',
            'first_prime_residuals','in_memory_aab_plus_one_fault_residuals',
            'nonzero_residue_primes','product_exceeds_twice_fresh_bound','verdict')
    bad=[field for field in shared if a[field]!=b[field]]
    if b.get('base_helper_sha256')!=PINS[BASE]:bad.append('base_helper_sha256')
    if b.get('helper_loading')!='compiled directly from individually hash-verified immutable byte snapshots':bad.append('helper_loading')
    if progress.get('state')!='PRIMES_COMPLETE' or progress.get('tested_count')!=424 or progress.get('bad_primes'):
        bad.append('final_progress')
    return bad

if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('pinned input mismatch')
old=json.loads(OLD.read_bytes());new=json.loads(NEW.read_bytes());progress=json.loads(PROG.read_bytes())
bad=compare(old,new,progress)
faults={}
for field in ('height_bound','prime_product','base_helper_sha256'):
    x=copy.deepcopy(new);x[field]=str(x[field])+'0';faults['tampered_'+field]=bool(compare(old,x,progress))
x=copy.deepcopy(progress);x['state']='INCOMPLETE';faults['incomplete_progress']=bool(compare(old,new,x))
if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('inputs changed during check')
r={'kind':'stdlib_snapshot_v2_vs_v1_reverse_crt_receipt_check',
   'v1_result_sha256':PINS[OLD],'v2_result_sha256':PINS[NEW],'v2_progress_sha256':PINS[PROG],
   'v2_source_sha256':PINS[V2],'pinned_transitive_base_sha256':PINS[BASE],
   'mismatched_fields':bad,'fault_controls_detected':faults,
   'scope':'Exact receipt-field comparison only; no prime residual, local map, PSD or physical theorem recomputed. Python runtime and actual verifier execution remain trusted; not formal/human/model-family review.',
   'verdict':'PASS' if not bad and all(faults.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
