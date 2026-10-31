#!/usr/bin/env python3
"""Independent exact primal-row check and common-increment check.
Usage: python3 script.py OUT.json PRIMAL.json PRIMAL_SHA
No LP-generator or producer import. Rows are enumerated from their contracts
and reconstructed by the pinned independent semantic row checker. Python
integers evaluate all rows on a proposed common-denominator grid. A passing
result proves finite relaxation feasibility plus the affine-extension lemma's
hypothesis, NOT entropic realizability or a new guessing-number upper bound.
"""
from ast import literal_eval
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
CHECKER='frontier-20261029-exchangeable-certificate-check-v1.py';CHECKER_SHA='147a6d5201fdef3d39431131f9ff3d1475b4cbe91865827dad1155900e17dd4a'
if sha256((ROOT/CHECKER).read_bytes()).hexdigest()!=CHECKER_SHA:raise ValueError('ROW_CHECKER_HASH')
s=spec_from_file_location('semantic',ROOT/CHECKER);semantic=module_from_spec(s);s.loader.exec_module(semantic)

def subsets(m):
    while True:
        yield m
        if not m:return
        m=(m-1)&m

def rows(doc,specs):
    L=semantic.legacy
    for tag,names in L.BR.items():
        n=len(names);full=(1<<n)-1
        for i in range(n):yield ['mono',names,i]
        for i,j in combinations(range(n),2):
            for z in subsets(full^(1<<i)^(1<<j)):yield ['cmi',names,i,j,z]
    for v in range(1,11):yield ['fd',v];yield ['cap',v]
    for gi in range(2):
        for m in range(1,1024):yield ['sym',gi,m]
    for new,(tag,_,old,over,existing) in L.COPIES.items():
        pos={x:i for i,x in enumerate(L.BR[tag])};Y=sum(1<<pos[x] for x in over)
        for q in range(1,1<<len(new)):
            for u in subsets(Y):yield ['copy',list(new),q,u]
        yield ['independence',list(new)]
    for k,(_,T) in L.XSPEC.items():
        Y=sum(1<<(t-1) for t in T)
        for u in subsets(Y):yield ['xcopy',k,u]
        yield ['xindependence',k]
    for c in doc['cuts']:
        tag=c.get('tag','o');rs=[c[z] for z in ('A','B','C','D','Z')]
        yield ['dfz',c['coefficients'],*rs] if tag=='o' else ['dfzb',tag,c['coefficients'],*rs]
    for tag,(k,tail,b) in specs.items():
        full=(1<<b)-1
        for i in range(b):yield ['ecmono',tag,i]
        yield ['ecmono',tag,-1]
        for i,j in combinations(range(b),2):
            for z in subsets(full^(1<<i)^(1<<j)):
                for r in range(k+1):yield ['eccmi',tag,'bb',i,j,z,r]
        for i in range(b):
            for z in subsets(full^(1<<i)):
                for r in range(k):yield ['eccmi',tag,'bc',i,-1,z,r]
        for z in range(full+1):
            for r in range(k-1):yield ['eccmi',tag,'cc',-1,-2,z,r]
        for u in subsets(semantic.T2):yield ['ecfirstcopy',tag,u]
        yield ['ecfirstind',tag]
        for r in range(k):
            for u in subsets(semantic.T4|(1<<10)):yield ['ecblockcopy',tag,u,r]
            yield ['ecblockind',tag,r]
        if tail:
            for u in subsets(semantic.T2|(1<<10)):
                for r in range(k+1):yield ['ectailcopy',tag,u,r]
            yield ['ectailind',tag]

def check(doc,profile):
    if not doc.get('exact_grid_found'):raise ValueError('NO_EXACT_GRID')
    D=doc['common_denominator']
    if isinstance(D,bool) or not isinstance(D,int) or D<=0 or any(isinstance(x,bool) or not isinstance(x,int) for x in profile.values()):raise ValueError('GRID_FORMAT')
    if 389*profile[('o',1023)]!=2603*D:raise ValueError('TARGET')
    specs=semantic.compile_specs(doc);semantic.legacy.set_extra(doc.get('extra_single_copies'));semantic.legacy.set_programs([])
    increments={}
    def V(tag,m,r):
        if not m and not r:return 0
        return profile[('o',m) if r==0 and m<1024 else (tag,m,r)]
    for tag,(k,tail,b) in specs.items():
        inc=V(tag,0,k)-V(tag,0,k-1)
        if inc<0:raise ValueError('NEGATIVE_INCREMENT')
        for m in range(1<<b):
            if V(tag,m,k)-V(tag,m,k-1)!=inc:raise ValueError('COMMON_INCREMENT')
        increments[tag]=inc
    counts=Counter()
    for row in rows(doc,specs):
        ts,kind=semantic.terms(row,specs);value=sum(c*profile[key] for key,c in ts if key is not None)
        if kind=='ge' and value<0:raise ValueError(('GE',row))
        if kind=='eq' and value!=0:raise ValueError(('EQ',row))
        if kind=='cap' and value>D:raise ValueError(('CAP',row))
        counts[row[0]]+=1
    return counts,increments

def main():
    t=time.monotonic();raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PRIMAL_HASH')
    doc=json.loads(raw)
    if not doc.get('exact_grid_found'):raise ValueError('NO_EXACT_GRID')
    profile={literal_eval(k):v for k,v in doc['exact_profile'].items()};counts,increments=check(doc,profile);controls={}
    for name,key in (('changed_original_joint',('o',1023)),('changed_affine_increment',('e0',0,doc['exchangeable_copies'][0]['copies']))):
        mutant=dict(profile);mutant[key]+=1
        try:check(doc,mutant)
        except (ValueError,KeyError) as e:controls[name]=str(e)
        else:raise ValueError(('CONTROL_NOT_REJECTED',name))
    report={'primal_sha256':sys.argv[3],'semantic_checker_sha256':CHECKER_SHA,'all_finite_rows_checked':True,'all_common_increment_hypotheses_checked':True,
       'common_denominator':doc['common_denominator'],'target':'2603/389','rows_checked':sum(counts.values()),'row_kinds':dict(counts),'increment_numerators':increments,
       'negative_controls':controls,'elapsed_s':time.monotonic()-t,
       'limits':'Exact integer finite primal feasibility and affine-extension hypotheses only. This is not an upper-bound dual, entropy realization, independent mathematical review or novelty clearance. The written extension criterion is a separate premise.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f,indent=1);f.write('\n')
    print(json.dumps(report,indent=1))
if __name__=='__main__':main()
