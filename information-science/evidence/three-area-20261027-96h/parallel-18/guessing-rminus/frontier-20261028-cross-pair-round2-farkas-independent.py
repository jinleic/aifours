#!/usr/bin/env python3
"""Independent exact check of the twelve-row fixed-marginal cross-copy obstruction.

Eleven rows are explicit elemental CMIs and one is the imposed conditional
independence. All mixed-auxiliary entropy coefficients cancel identically.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-all-cuts-exact-candidate.json','1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703')
RAY=('frontier-20261028-cross-pair-round2-farkas-result.json','a10333eff083b493edff9e791e2def45f3a5a55309310f643cc01113bc7369da')
R12=('frontier-20261028-crossbranch12-independent-check-result.json','371ed6d0da680cdbacf36704f61f7d1888b800a5489470c9c36512811df9a86e')
R13=('frontier-20261028-crossbranch13-all-cuts-independent-check-result.json','2575991ec2e5fc62fa3b606d5884dddb9d98f1ba270eae6d882cb641ecb4c76c')
OUT=ROOT/'frontier-20261028-cross-pair-round2-farkas-independent-result.json'
ORIGINAL=tuple('abcdefghij');PAIR=("d'1","g'3");VARS=ORIGINAL+PAIR;FULL=4095


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def values(base,c12,c13):
    idx={v:i for i,v in enumerate(VARS)};out={0:Fraction(0)}
    def add(e):
        m=sum(1<<idx[v] for v in e['entropy_variables'])
        if not m or m in out:raise ValueError('DUPLICATE')
        out[m]=Fraction(e['value'])
    for e in base['primal_values']:
        if set(e['entropy_variables'])<=set(ORIGINAL):add(e)
    if len(out)!=1024:raise ValueError('BASE_COUNT')
    for doc,sym in ((c12,PAIR[0]),(c13,PAIR[1])):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if sym in labs and set(labs)<=set(ORIGINAL)|{sym}:add(e)
    if len(out)!=3072:raise ValueError('MARGINAL_COUNT')
    return out


def verify(rows,h):
    agg={};kinds=Counter()
    for entry in rows:
        meta=entry['metadata'];kind=meta['kind']['kind'];weight=Fraction(entry['ray_weight']);kinds[kind]+=1
        if kind=='CMI':
            i,j,z=(meta['kind'][x] for x in ('i','j','z'))
            if not (0<=i<j<12 and 0<=z<=FULL and not z&((1<<i)|(1<<j)) and weight>0 and not meta['equality']):raise ValueError('CMI_METADATA')
            a,b=1<<i,1<<j;terms=((z|a,1),(z|b,1),(z|a|b,-1),(z,-1))
        elif kind=='conditional_independence':
            if not meta['equality'] or weight!=-2:raise ValueError('INDEPENDENCE_METADATA')
            x,a,b=1023,1024,2048;terms=((x|a,1),(x|b,1),(x|a|b,-1),(x,-1))
        else:raise ValueError(('UNKNOWN_ROW',kind))
        if [list(t) for t in terms]!=meta['terms']:raise ValueError('ROW_TERMS')
        for m,c in terms:
            if m:agg[m]=agg.get(m,Fraction(0))+weight*c
    agg={m:c for m,c in agg.items() if c}
    if kinds!=Counter({'CMI':11,'conditional_independence':1}):raise ValueError(('KINDS',kinds))
    if any(m&3072==3072 for m in agg):raise ValueError('MIXED_ENTROPY_NOT_CANCELLED')
    try:constant=sum((c*h[m] for m,c in agg.items()),Fraction(0))
    except KeyError as exc:raise ValueError('MISSING_MARGINAL') from exc
    if constant!=Fraction(-867,460000):raise ValueError(('CONSTANT',str(constant)))
    return {'row_kinds':dict(kinds),'distinct_known_entropy_terms':len(agg),
            'mixed_auxiliary_entropy_terms':0,'known_constant':str(constant),
            'known_terms':[[m,str(c)] for m,c in sorted(agg.items())]}


def main():
    base,c12,c13,ray,r12,r13=map(pin,(BASE,C12,C13,RAY,R12,R13))
    if not r12['all_checked'] or r12['candidate_sha256']!=C12[1] or not r13['all_checked'] or r13['candidate_sha256']!=C13[1] or r13['shared_branch1_sha256']!=C12[1]:raise ValueError('STAR_RECEIPTS')
    h=values(base,c12,c13);rows=ray['exact_farkas_candidate']['weights'];result=verify(rows,h);controls={}
    def expect(name,mut):
        rr=deepcopy(rows);hh=dict(h);mut(rr,hh)
        try:verify(rr,hh)
        except (ValueError,KeyError):controls[name]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    expect('dropped_cmi',lambda rr,hh:rr.pop(0))
    expect('negative_cmi_weight',lambda rr,hh:rr[0].__setitem__('ray_weight','-1'))
    expect('overlapping_condition',lambda rr,hh:rr[0]['metadata']['kind'].__setitem__('z',1<<rr[0]['metadata']['kind']['i']))
    expect('changed_independence_weight',lambda rr,hh:rr[-1].__setitem__('ray_weight','-1'))
    term=result['known_terms'][0][0]
    expect('altered_fixed_marginal',lambda rr,hh:hh.__setitem__(term,hh[term]+Fraction(1,7)))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],'ray_sha256':RAY[1],
         'pair':PAIR,'exact_identity':result,'all_checked':True,'mutation_controls':controls,
         'limits':'If I(d1;g3|X)=0, these particular fixed auxiliary marginals have no Shannon joint extension. Other auxiliary assignments of the same original profile may extend.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
