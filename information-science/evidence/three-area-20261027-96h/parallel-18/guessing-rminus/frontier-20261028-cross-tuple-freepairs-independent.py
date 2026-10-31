#!/usr/bin/env python3
"""Independent exact check of a 13-variable tuple/single-auxiliary amalgam."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
CAND=('frontier-20261028-cross-tuple-freepairs-candidate.json','fc0e45092f735a8d17a7b7b0363b04b716e0a48c70c6a3a9f32d09855d2e76ec')
OUT=ROOT/'frontier-20261028-cross-tuple-freepairs-independent-result.json'
ORIGINAL=tuple('abcdefghij');AUX=("d'1","g'2","f'3");VARS=ORIGINAL+AUX


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def values(base,c12,c13,cand):
    if tuple(cand['variables'])!=VARS:raise ValueError('VARIABLES')
    out={0:Fraction(0)};idx={v:i for i,v in enumerate(VARS)}
    def add(e,required=None):
        labs=e['entropy_variables'];m=sum(1<<idx[v] for v in labs)
        if not m or m in out or (required and not set(labs)&required):raise ValueError('DUPLICATE_OR_LABEL')
        out[m]=Fraction(e['value'])
    for e in base['primal_values']:
        if set(e['entropy_variables'])<=set(ORIGINAL):add(e)
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for doc,aux in ((c12,set(AUX[:2])),(c13,{AUX[2]})):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if set(labs)<=set(ORIGINAL)|aux and set(labs)&aux:add(e,aux)
    if len(out)!=5120:raise ValueError('FIXED_SIZE')
    for e in cand['cross_values']:
        labs=set(e['entropy_variables'])
        if not labs<=set(VARS) or not labs&set(AUX[:2]) or AUX[2] not in labs:raise ValueError('CROSS_LABEL')
        add(e,set(AUX))
    if len(out)!=8192:raise ValueError('ALL_SIZE')
    return out


def verify(h):
    if len(h)!=8192 or h[0]!=0:raise ValueError('VECTOR')
    X=1023;D=1024;G=2048;F=4096
    if h[X|D|G]+h[X|F]-h[X|D|G|F]-h[X]!=0:raise ValueError('TUPLE_INDEPENDENCE')
    if h[X|D]+h[X|F]-h[X|D|F]-h[X]!=0 or h[X|G]+h[X|F]-h[X|G|F]-h[X]!=0:raise ValueError('PAIR_INDEPENDENCE')
    scale=lcm(*(x.denominator for x in h.values()));a=[int(h[m]*scale) for m in range(8192)]
    if min(a)<0:raise ValueError('NEGATIVE')
    full=8191;count=0;minimum=None
    for i in range(13):
        v=a[full]-a[full^(1<<i)]
        if v<0:raise ValueError('MONOTONE')
        minimum=v if minimum is None else min(minimum,v);count+=1
    for i,j in combinations(range(13),2):
        b,c=1<<i,1<<j;z=full^b^c
        while True:
            v=a[z|b]+a[z|c]-a[z|b|c]-a[z]
            if v<0:raise ValueError(('CMI',i,j,z))
            minimum=min(minimum,v);count+=1
            if not z:break
            z=(z-1)&(full^b^c)
    if count!=159757:raise ValueError('COUNT')
    return {'elemental_shannon_checks':count,'tuple_independence':1,'implied_pair_independences':2,
            'minimum_scaled_shannon_slack':minimum,'scale_digits':len(str(scale))}


def main():
    base,c12,c13,cand=map(pin,(BASE,C12,C13,CAND));h=values(base,c12,c13,cand);checks=verify(h);controls={}
    def expect(tag,mut):
        x=dict(h);mut(x)
        try:verify(x)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('changed_full_entropy',lambda x:x.__setitem__(8191,x[8191]+Fraction(1,7)))
    expect('missing_cross_entropy',lambda x:x.pop(1024|4096))
    expect('negative_entropy',lambda x:x.__setitem__(1024|4096,Fraction(-1)))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],'candidate_sha256':CAND[1],
         'variables':VARS,'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'One 13-variable tuple/single system with fixed same-branch marginals and reoptimized pair/triple coordinates; no global 17-variable or entropic realization is claimed.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
