#!/usr/bin/env python3
"""Exact integer conditional-DFZ scan on 13-variable joint counterprofiles.
Usage: python3 script.py OUT.json PROFILES.jsonl PROFILES_SHA INDICES
All ordered singleton roles A,B,C,D and every conditioning subset Z of their
nine-variable complement. Only nine coefficient tuples already re-derived
exactly in the pinned receipts below are allowed. Reported separators are
re-evaluated with Python integers. Absence of cuts applies ONLY to this finite
singleton-role family, not arbitrary union roles or the entropic cone.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
VERIFY=[('frontier-20261029-dfz-inequality-verify-result.json','12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727'),
 ('frontier-20261029-dfz-inequality-verify-base-used.json','206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5'),
 ('frontier-20261029-dfz-inequality-verify-v9b.json','614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5')]
JOINT_RECEIPT='frontier-20261029-functional-joint-completions-all20-check.json';JOINT_SHA='3259785f6fa83bceb2ec322526cc3bb38caf57494cfbd82e39516a141dcdc506'

def subsets(mask):
    q=mask
    while True:
        yield q
        if not q:return
        q=(q-1)&mask

def joint(record):
    P={tuple(k):v for k,v in zip(record['keys'],record['numerators'])};acts=[(tuple(p),tuple(cp)) for p,cp in record['actions']];out=[]
    for m in range(8192):
        base=m&1023;aux=m>>10;br=0 if not aux else (1+aux.bit_length() if aux.bit_count()==1 else 1)
        if not(base or br):out.append(0);continue
        key=min((sum(1<<(p[i]-1) for i in range(10) if base>>i&1),2+cp[br-2] if br>=2 else br) for p,cp in acts);out.append(P[key])
    return np.array(out,dtype=np.int64)

def exact_value(H,k,A,B,C,D,Z):
    def I(a,b,z):return int(H[a|z])+int(H[b|z])-int(H[a|b|z])-int(H[z])
    v=[I(A,B,Z),I(A,B,C|Z),I(A,C,B|Z),I(B,C,A|Z),I(A,B,D|Z),I(A,D,B|Z),I(B,D,A|Z),I(C,D,Z),I(C,D,A|Z)]
    return -k[0]*v[0]+sum(k[i]*v[i] for i in range(1,9))

def scan(record,keys):
    H=joint(record);Dden=record['common_denominator'];W=np.array([[-k[0],*k[1:]] for k in keys],dtype=np.int64).T
    bound=4*max(abs(int(v)) for v in H)*max(sum(abs(int(v)) for v in W[:,j]) for j in range(len(keys)))
    if bound>=1<<63:raise ValueError('INT64_BOUND')
    minima=np.full(len(keys),np.iinfo(np.int64).max,dtype=np.int64);candidates=[];count=0;cache={};t=time.monotonic()
    for a,b,c,d in permutations(range(13),4):
        A,B,C,D=1<<a,1<<b,1<<c,1<<d;union=A|B|C|D
        if union not in cache:cache[union]=np.fromiter(subsets(8191^union),dtype=np.int64)
        Z=cache[union];h=lambda m:H[m]
        def I(x,y,z):return h(x|z)+h(y|z)-h(x|y|z)-h(z)
        MF=np.stack([I(A,B,Z),I(A,B,C|Z),I(A,C,B|Z),I(B,C,A|Z),I(A,B,D|Z),I(A,D,B|Z),I(B,D,A|Z),I(C,D,Z),I(C,D,A|Z)],axis=1)
        values=MF@W;local=values.min(axis=0);minima=np.minimum(minima,local);count+=len(Z)
        for j in np.nonzero(local<0)[0]:
            r=int(values[:,j].argmin());candidates.append((int(local[j]),int(j),A,B,C,D,int(Z[r])))
    selected=[];per={}
    for value,j,A,B,C,D,Z in sorted(candidates):
        if per.get(j,0)>=40:continue
        if exact_value(H,keys[j],A,B,C,D,Z)!=value:raise ValueError('EXACT_REPLAY')
        per[j]=per.get(j,0)+1;selected.append({'coefficients':list(keys[j]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'slack_numerator':value,'denominator':Dden,'slack':str(Fraction(value,Dden))})
        if len(selected)>=400:break
    if count!=13*12*11*10*(1<<9):raise ValueError('ENUMERATION_COUNT')
    return {'index':record['index'],'colors':record['colors'],'role_condition_assignments':count,'inequality_instances':count*len(keys),
      'minimum_numerators_by_tuple':[[list(k),int(v)] for k,v in zip(keys,minima)],'negative_ordered_quadruple_minima':len(candidates),
      'cuts':selected,'int64_absolute_sum_bound':bound,'elapsed_s':time.monotonic()-t}

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PROFILE_HASH')
    jr=(ROOT/JOINT_RECEIPT).read_bytes()
    if sha256(jr).hexdigest()!=JOINT_SHA:raise ValueError('JOINT_CHECK_HASH')
    jdoc=json.loads(jr)
    if not jdoc['all_full_joint_completions_checked'] or jdoc['profiles_sha256']!=sys.argv[3]:raise ValueError('JOINT_BINDING')
    valid=set()
    for fn,expected in VERIFY:
        data=(ROOT/fn).read_bytes()
        if sha256(data).hexdigest()!=expected:raise ValueError('VERIFY_HASH')
        valid.update(tuple(r['coefficients']) for r in json.loads(data)['results'] if r['valid_exact'])
    keys=sorted(valid);records={r['index']:r for r in (json.loads(l) for l in raw.decode().splitlines())};indices=[int(i) for i in sys.argv[4].split(',')]
    results=[]
    for i in indices:
        result=scan(records[i],keys);results.append(result);print(i,'cuts',len(result['cuts']),'candidates',result['negative_ordered_quadruple_minima'],'seconds',result['elapsed_s'],flush=True)
    doc={'profiles_sha256':sys.argv[3],'joint_receipt_sha256':JOINT_SHA,'dfz_receipts':VERIFY,'coefficient_tuples':len(keys),'cases':results,
       'limits':'Exact finite singleton-role conditional-DFZ screen; no new guessing-number or entropy-law bound until a separate exact dual is checked. No paused imported-gate episode used.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
if __name__=='__main__':main()
