#!/usr/bin/env python3
"""Directly exercise pinned owner Gram-group code on exact modular-projected Z.

An in-memory data adapter replaces each rational Z by its residue mod p; the
pinned owner's unmodified main builds its ACTUAL grouped full word tensor. A
callback intercepts each of 17 Gram tensors before orbit addition, compares two
full-word projections to independent per-type/Kronecker results, and stops
before equality/objective/result writes. This is a diagnostic, not a full
rational certificate identity. No source/data bytes or existing results change.
"""
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
DIRECT=ROOT/'frontier-20261028-d4-grouped-versus-per-type-contraction-check.py'
DIRECT_RESULT=ROOT/'frontier-20261028-d4-grouped-versus-per-type-contraction-check-results.json'
PIN_G='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
PIN_D='68e226dd6888b26d33364b0f6ce56e38a4a04b34da3f828c830ffec4a8efb6bc'
PIN_R='0c93b7316404981a4395bdc43f8925052d23d616e8b2d26624a3480b103a877a'
OUT=ROOT/'frontier-20261028-d4-actual-owner-gram-aggregation-check-results.json'
p=65521


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

class FinishedGram(Exception):pass


def main():
    st=time.monotonic();sys.set_int_max_str_digits(0)
    pins={GLOBAL:PIN_G,DIRECT:PIN_D,DIRECT_RESULT:PIN_R}
    if any(sha(k)!=v for k,v in pins.items()):raise ValueError('pinned input mismatch')
    expected=json.loads(DIRECT_RESULT.read_text())
    if expected['verdict']!='PASS' or expected['prime']!=p or expected['weight_tensors']!=2:raise ValueError('bad direct receipt')
    if any(p%d==0 for d in range(2,math.isqrt(p)+1)):raise ValueError('nonprime modulus')
    diag=load('direct_grouping_diagnostic',DIRECT);g=load('actual_owner_main',GLOBAL)
    original_load=g.load_data;pkg,corr=original_load()
    groups={}
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                f,kp,lp=g.literal_rule(a,b);cut=t['modules'][0].split('|')[1]
                groups.setdefault((f,kp,lp,cut),[]).append((ti,r,s))
    ordered=sorted(groups.items(),key=lambda z:str(z[0]))
    if len(ordered)!=17 or len(expected['groups'])!=17:raise ValueError('wrong group count')
    for ((key,items),e) in zip(ordered,expected['groups']):
        if key[0]!=e['family'] or len(items)!=e['type_row_pairs'] or not e['match']:
            raise ValueError('direct-receipt group order mismatch')
    for matrix in corr['matrices']:
        for pair in matrix['values']:
            den=int(pair[1])%p
            if not den:raise ValueError('Z denominator divides modulus')
            pair[0]=str((int(pair[0])%p)*pow(den,-1,p)%p);pair[1]='1'
    corr['equality_coefficients']=[]
    # g.main computes D=2^31 on these in-memory inputs, which we cancel mod p.
    D=2**31;dinv=pow(D,-1,p);reports=[];fault=False
    g.load_data=lambda:(pkg,corr)
    g.OUT=ROOT/'frontier-20261028-unused-owner-stop-before-output.json'
    def capture(acc,oid,arr,sign):
        nonlocal fault
        j=len(reports)
        if j>=17 or sign!=-1 or arr.shape!=(24,24,24,24):raise ValueError('unexpected actual owner callback')
        vals=np.fromiter((int(v)%p for v in arr.ravel()),dtype=np.int64,count=24**4).reshape((24,)*4)
        actual=[]
        for which in range(2):
            vectors=[diag.weights(which,axis,p) for axis in range(4)]
            val=diag.projection(vals,vectors,p)*dinv%p;actual.append(val)
            if not fault:
                bad=vals.copy();bad[(0,0,0,0)]=(int(bad[(0,0,0,0)])+1)%p
                fault=(diag.projection(bad,vectors,p)*dinv%p)!=val
        exp=expected['groups'][j]['direct']
        reports.append({'group':j+1,'family':ordered[j][0][0],
                        'type_row_pairs':len(ordered[j][1]),'actual_owner':actual,'per_type_reference':exp,'match':actual==exp})
        print('actual owner group',j+1,'match',actual==exp,'elapsed',round(time.monotonic()-st,2),flush=True)
        if len(reports)==17:raise FinishedGram()
    g.add_orbits=capture
    try:g.main()
    except FinishedGram:pass
    else:raise ValueError('owner did not stop at expected Gram boundary')
    if any(sha(k)!=v for k,v in pins.items()):raise ValueError('input changed during run')
    ok=len(reports)==17 and all(v['match'] for v in reports) and fault
    out={'kind':'actual_pinned_owner_gram_code_versus_per_type_projection',
         'owner_checker_sha256':PIN_G,'per_type_script_sha256':PIN_D,'per_type_result_sha256':PIN_R,
         'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
         'prime':p,'prime_trial_division':'PASS','actual_owner_source_groups':len(reports),
         'weights_per_group':2,'groups':reports,'one_word_tensor_entry_fault_detected':fault,
         'elapsed_seconds':round(time.monotonic()-st,3),
         'method':'Run the pinned owner main unmodified except in-memory Z modular projection and a callback replacing orbit accumulation; intercept each actual full-word grouped tensor and compare two field projections with prior independent per-type Kronecker results. Stop before equality/objective/result writes.',
         'scope':'Actual owner Gram aggregation under in-memory modular Z on two weighted projections per group. This does not repeat or prove the full rational identity, corrected PSD or equality/objective maps. No original physical target state is sampled; no author core, formal kernel or model-family review.',
         'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
