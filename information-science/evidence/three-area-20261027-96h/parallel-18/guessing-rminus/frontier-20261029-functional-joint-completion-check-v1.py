#!/usr/bin/env python3
"""Exact 13-variable joint polymatroid completions of v1 counterprofiles.
Usage: python3 script.py OUT.json PROFILES.jsonl PROFILES_SHA
Only corrected v2 primal checker is imported. Joint variables are Y1..Y10 and
A,B,C. Empty auxiliary subset uses h(Y); a singleton uses its functional
branch; any pair or triple uses h(Y,S). Checks every full elemental row and
all pair-determination equalities. This is a stronger relaxation obstruction,
NOT an entropic realization or a coding witness. No paused imported-gate
source/output is used.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
CHECK='frontier-20261029-plane-functional-primal-check-v2.py';CHECK_SHA='00092f5252bef63638c215cb596e6727a37bd31823d7759b96603739908ebd81'
if sha256((ROOT/CHECK).read_bytes()).hexdigest()!=CHECK_SHA:raise ValueError('CORRECTED_CHECKER_HASH')
s=spec_from_file_location('primal',ROOT/CHECK);primal=module_from_spec(s);s.loader.exec_module(primal)

def completion(record):
    P={tuple(k):v for k,v in zip(record['keys'],record['numerators'])};acts=[(tuple(p),tuple(cp)) for p,cp in record['actions']]
    values=[]
    for m in range(8192):
        base=m&1023;aux=m>>10
        br=0 if not aux else (2+(aux.bit_length()-1) if aux.bit_count()==1 else 1)
        if not(base or br):values.append(0);continue
        key=min((sum(1<<(p[i]-1) for i in range(10) if base>>i&1),2+cp[br-2] if br>=2 else br) for p,cp in acts)
        values.append(P[key])
    return values

def joint_check(values):
    if len(values)!=8192 or values[0]!=0:raise ValueError('JOINT_COORDINATES')
    count=0
    for i in range(13):
        if values[8191]-values[8191^(1<<i)]<0:raise ValueError(('MONO',i))
        count+=1
    for i,j in combinations(range(13),2):
        rest=8191^(1<<i)^(1<<j)
        for z in primal.subsets(rest):
            if values[z|1<<i]+values[z|1<<j]-values[z|1<<i|1<<j]-values[z]<0:raise ValueError(('CMI',i,j,z))
            count+=1
    if count!=159757:raise ValueError(('FULL_ROW_COVERAGE',count))
    abc=7<<10
    for u in range(1024):
        for omitted in range(3):
            if values[u|abc]!=values[u|(abc^(1<<(10+omitted)))]:raise ValueError('AUX_CIRCUIT')
    if values[8191]!=values[1023]:raise ValueError('AUX_DETERMINED_BY_ORIGINALS')
    return count

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PROFILE_HASH')
    t=time.monotonic();records=[json.loads(l) for l in raw.decode().splitlines()];results=[]
    for r in records:
        base=primal.check(r);values=completion(r);count=joint_check(values)
        results.append({'index':r['index'],'colors':r['colors'],'exact_Delta':base['exact_Delta'],'common_denominator':r['common_denominator'],
          'joint_elemental_rows_checked':count,'auxiliary_pair_determination_equalities':3072})
    mutant=completion(records[0]);mutant[7<<10]+=1
    try:joint_check(mutant)
    except ValueError as e:control=str(e)
    else:raise ValueError('NEGATIVE_CONTROL')
    doc={'profiles_sha256':sys.argv[3],'corrected_primal_checker_sha256':CHECK_SHA,'all_full_joint_completions_checked':True,'count':len(results),'cases':results,
      'negative_control':control,'elapsed_s':time.monotonic()-t,
      'limits':'Exact 13-variable Shannon polymatroid completions with the rank-two auxiliary circuit and the v1 full-state-only premises. No entropic/code realization, imported functional gates, global guessing-number, formal-proof or novelty claim.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(json.dumps(doc,indent=1))
if __name__=='__main__':main()
