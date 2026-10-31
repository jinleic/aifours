#!/usr/bin/env python3
"""Version 2: enumerate subsets using the fixed original mask, not the evolving
subset; assert the complete 2^popcount cardinality whenever exhausted. Version 1
only followed a descending chain and is superseded for primal coverage.
Independent exact primal check of the V1_FULL_STATE_GATE_ONLY relaxation.
Usage: python3 script.py OUT.json PROFILES.jsonl PROFILES_SHA
Imports only the pinned OLD v1 semantic checker, not any producer, LP generator
or paused imported-functional-gates route. Expands symmetry-compressed profiles
and evaluates every full 11-variable elemental row and each v1 premise with
Python integers. Positive Delta witnesses a limitation of this relaxation,
NOT a realizable distribution or guessing strategy.
"""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
CHECK='frontier-20261028-plane-functional-check.py';CHECK_SHA='0d2f99580d9f939a6f6f4dba1e36b93ec84b9f111f92818571cdefd25ac931c3'
if sha256((ROOT/CHECK).read_bytes()).hexdigest()!=CHECK_SHA:raise ValueError('OLD_SEMANTIC_CHECKER_HASH')
s=spec_from_file_location('old_semantics',ROOT/CHECK);old=module_from_spec(s);s.loader.exec_module(old)

def subsets(mask):
    m=mask;count=0
    while True:
        yield m;count+=1
        if not m:break
        m=(m-1)&mask
    if count!=(1<<mask.bit_count()):raise ValueError('SUBSET_COVERAGE')

def names(col):
    for br in (1,2,3,4):
        for i in range(11):yield ('mono',br,i)
        for i,j in combinations(range(11),2):
            for z in subsets(2047^(1<<i)^(1<<j)):yield ('cmi',br,i,j,z)
        yield ('aux-determined',br)
    yield ('gate',1)
    for v in range(1,11):
        yield ('graph-fd',v)
        types={col[t] for t,T in enumerate(old.TRI) if v in T and col[t] is not None}
        for c in types:yield ('functional-neighborhood',v,c)
        if len(types)>=2:yield ('state-neighborhood',v)
        yield ('mixed-local-fd',v)
    for t,c in enumerate(col):
        if c is not None:yield ('functional-triangle',t+1)
    for a in range(1024):
        for j in (2,3,4):yield ('data-processing',a,j)
        for j,k in combinations((2,3,4),2):yield ('pair-determines-state',a,j,k)

def check(record):
    if record.get('model_scope')!='V1_FULL_STATE_GATE_ONLY' or not record.get('exact_grid_found'):raise ValueError('SCOPE_OR_GRID')
    D=record['common_denominator'];nums=record['numerators'];keys=[tuple(k) for k in record['keys']]
    if isinstance(D,bool) or not isinstance(D,int) or D<=0 or len(keys)!=len(nums) or len(set(keys))!=len(keys) or any(isinstance(v,bool) or not isinstance(v,int) for v in nums):raise ValueError('GRID_FORMAT')
    P=dict(zip(keys,nums));col=tuple(None if c=='-' else int(c) for c in record['colors']);acts=[]
    if len(col)!=10 or any(c not in (None,0,1,2) for c in col):raise ValueError('COLORING')
    edges={tuple(sorted((v,u))) for v in old.N for u in old.N[v]}
    for p,cp in record['actions']:
        p=tuple(p);cp=tuple(cp)
        if sorted(p)!=list(range(1,11)) or sorted(cp)!=[0,1,2] or {tuple(sorted((p[a-1],p[b-1]))) for a,b in edges}!=edges:raise ValueError('ACTION')
        moved=[tuple(sorted(p[v-1] for v in t)) for t in old.TRI]
        if set(moved)!=set(old.LOOK):raise ValueError('FACTOR_ACTION')
        new=[None]*10
        for t in range(10):new[old.LOOK[moved[t]]]=None if col[t] is None else cp[col[t]]
        if tuple(new)!=col:raise ValueError('COLOR_ACTION')
        acts.append((p,cp))
    if (tuple(range(1,11)),(0,1,2)) not in acts:raise ValueError('IDENTITY_ACTION')
    def canon(a,b):return min((sum(1<<(p[i]-1) for i in range(10) if a>>i&1),2+cp[b-2] if b>=2 else b) for p,cp in acts)
    def val(a,b):return 0 if a==b==0 else P[canon(a,b)]
    if sum(val(1<<i,0) for i in range(10))!=D:raise ValueError('NORMALIZATION')
    gap=3*val(1023,0)-2*D
    if gap<=0:raise ValueError('NO_POSITIVE_GAP')
    count=0
    for name in names(col):
        ts,kind=old.rows(name,col);v=sum(c*val(a,b) for a,b,c in ts)
        if kind=='ge' and v<0:raise ValueError(('GE',name))
        if kind=='le' and v>0:raise ValueError(('LE',name))
        if kind=='eq' and v!=0:raise ValueError(('EQ',name))
        count+=1
    expected=4*(11+55*(1<<9))+4+1+10+10+6*1024+sum(c is not None for c in col)
    for v in range(1,11):
        types={col[t] for t,T in enumerate(old.TRI) if v in T and col[t] is not None}
        expected+=len(types)+(1 if len(types)>=2 else 0)
    if count!=expected:raise ValueError(('ROW_COVERAGE',count,expected))
    return {'index':record['index'],'colors':record['colors'],'common_denominator':D,'full_rows_checked':count,
            'exact_3Delta':str(Fraction(gap,D)),'exact_Delta':str(Fraction(gap,3*D)),'original_joint':str(Fraction(val(1023,0),D))}

def main():
    t=time.monotonic();raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PROFILES_HASH')
    records=[json.loads(l) for l in raw.decode().splitlines()];results=[check(r) for r in records]
    controls={};first=records[0]
    mutant=deepcopy(first);key=(1023,0);idx=[tuple(k) for k in mutant['keys']].index(key);mutant['numerators'][idx]+=1
    try:check(mutant)
    except (ValueError,KeyError) as e:controls['changed_original_joint']=str(e)
    else:raise ValueError('CONTROL')
    mutant=deepcopy(first);mutant['common_denominator']+=1
    try:check(mutant)
    except (ValueError,KeyError) as e:controls['changed_normalization']=str(e)
    else:raise ValueError('CONTROL')
    doc={'profiles_sha256':sys.argv[3],'old_v1_semantic_checker_sha256':CHECK_SHA,'checker_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'all_checked':True,'count':len(results),'cases':results,
       'negative_controls':controls,'elapsed_s':time.monotonic()-t,
       'limits':'Exact polymatroid/functional-relaxation countermodels for the OLD full-state-only row family. No probability-law, code, unrestricted guessing-number, imported functional gate, formal-proof or novelty claim.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(json.dumps(doc,indent=1))
if __name__=='__main__':main()
