#!/usr/bin/env python3
"""DFZ separator proposals from exported floating joint-Shannon LP points.
Usage: python3 script.py OUT.json POINTS.jsonl POINTS_SHA INDICES
The LP point is NOT an exact feasible entropy profile. Scan ordered singleton
roles and conditioning subsets in floating arithmetic; independently evaluate
each reported negative value as an exact Fraction of the binary float table.
Every proposed inequality itself is universally valid by the pinned DFZ
receipts, regardless of the proposal point's feasibility. No absence/optimality
claim is made from this scan. Final acceptance needs an exact dual check.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
MODEL_SHA='3d2404226d11b85b537002b6f7303571d58c9ca1f7c6057b9d32958489e5b4e3'
VERIFY=[('frontier-20261029-dfz-inequality-verify-result.json','12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727'),
 ('frontier-20261029-dfz-inequality-verify-base-used.json','206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5'),
 ('frontier-20261029-dfz-inequality-verify-v9b.json','614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5')]

def subsets(mask):
    u=mask
    while True:
        yield u
        if not u:return
        u=(u-1)&mask

def joint(r):
    if r.get('model_sha256')!=MODEL_SHA or not r.get('proposal_available'):raise ValueError('PROPOSAL_SCOPE')
    P={tuple(k):v for k,v in zip(r['keys'],r['float_values'])};acts=[(tuple(p),tuple(cp)) for p,cp in r['actions']];H=[]
    for mask in range(8192):
        a=mask&1023;u=mask>>10;b=0 if not u else (1+u.bit_length() if u.bit_count()==1 else 1)
        if not(a or b):H.append(0.);continue
        key=min((sum(1<<(p[i]-1) for i in range(10) if a>>i&1),2+cp[b-2] if b>=2 else b) for p,cp in acts);H.append(float(P[key]))
    if not all(np.isfinite(x) for x in H):raise ValueError('NONFINITE_PROPOSAL')
    return np.array(H,dtype=float)

def scan(record,keys):
    H=joint(record);W=np.array([[-k[0],*k[1:]] for k in keys],dtype=float).T;cache={};candidates=[];count=0;t=time.monotonic()
    for a,b,c,d in permutations(range(13),4):
        A,B,C,D=1<<a,1<<b,1<<c,1<<d;u=A|B|C|D
        if u not in cache:cache[u]=np.fromiter(subsets(8191^u),dtype=np.int64)
        Z=cache[u]
        def I(x,y,z):return H[x|z]+H[y|z]-H[x|y|z]-H[z]
        MF=np.stack([I(A,B,Z),I(A,B,C|Z),I(A,C,B|Z),I(B,C,A|Z),I(A,B,D|Z),I(A,D,B|Z),I(B,D,A|Z),I(C,D,Z),I(C,D,A|Z)],axis=1)
        V=MF@W;mins=V.min(axis=0);count+=len(Z)
        for j in np.nonzero(mins < -1e-8)[0]:
            z=int(V[:,j].argmin());candidates.append((float(mins[j]),int(j),A,B,C,D,int(Z[z])))
    @lru_cache(None)
    def F(mask):return Fraction(float(H[mask]))
    def MI(x,y,z):return F(x|z)+F(y|z)-F(x|y|z)-F(z)
    selected=[];per={}
    for value,j,A,B,C,D,Z in sorted(candidates):
        if per.get(j,0)>=40:continue
        k=keys[j];v=[MI(A,B,Z),MI(A,B,C|Z),MI(A,C,B|Z),MI(B,C,A|Z),MI(A,B,D|Z),MI(A,D,B|Z),MI(B,D,A|Z),MI(C,D,Z),MI(C,D,A|Z)]
        exact=-k[0]*v[0]+sum(k[i]*v[i] for i in range(1,9))
        if exact>=0:continue
        per[j]=per.get(j,0)+1;selected.append({'coefficients':list(k),'A':A,'B':B,'C':C,'D':D,'Z':Z,'proposal_slack_float':value,'exact_binary_table_slack':str(exact)})
        if len(selected)>=400:break
    return {'index':record['index'],'status_float':record['status_float'],'proposal_objective_3Delta':record['objective_3Delta_float'],
      'role_condition_assignments':count,'negative_quadruple_minimum_proposals':len(candidates),'cuts':selected,'elapsed_s':time.monotonic()-t}

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINTS_HASH')
    valid=set()
    for fn,h in VERIFY:
        data=(ROOT/fn).read_bytes()
        if sha256(data).hexdigest()!=h:raise ValueError('VERIFY_HASH')
        valid.update(tuple(r['coefficients']) for r in json.loads(data)['results'] if r['valid_exact'])
    records={r['index']:r for r in (json.loads(l) for l in raw.decode().splitlines())};keys=sorted(valid);cases=[]
    for i in map(int,sys.argv[4].split(',')):
        out=scan(records[i],keys);cases.append(out);print(i,'cuts',len(out['cuts']),'seconds',out['elapsed_s'],flush=True)
    doc={'points_sha256':sys.argv[3],'dfz_receipts':VERIFY,'cases':cases,'limits':'Floating separator search with exact binary-table sign replays only. Proposal points are not exact feasible profiles; no new exclusion or global bound until exact dual verification. No paused gate-import route used.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
if __name__=='__main__':main()
