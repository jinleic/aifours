#!/usr/bin/env python3
"""Independently verify nine exact pairwise Shannon/coupling extensions.

Every pair reuses the same pinned original and star single-auxiliary
marginals. The pairwise systems do not imply a full multi-auxiliary joint.
"""
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
SUMMARY=('frontier-20261028-crossbranch23-pairs-round4-result.json','d2883058aa5cf663d0539e41e2f6712c3bec3155220e588eb8e93edaa2f76516')
OUT=ROOT/'frontier-20261028-crossbranch23-pairs-round4-independent-result.json'
ORIGINAL=tuple('abcdefghij');V=("d'1","e'1","g'2");W=("f'3","g'3","h'4")


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def read_values(base,c12,c13,doc,pair):
    variables=ORIGINAL+tuple(pair);idx={v:i for i,v in enumerate(variables)};out={0:Fraction(0)}
    def add(e,required=None):
        labs=e['entropy_variables'];m=sum(1<<idx[v] for v in labs)
        if not m or m in out or (required is not None and not required<=set(labs)):raise ValueError('DUPLICATE_OR_LABEL')
        out[m]=Fraction(e['value'])
    for e in base['primal_values']:
        if set(e['entropy_variables'])<=set(ORIGINAL):add(e)
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for source,sym in ((c12,pair[0]),(c13,pair[1])):
        for e in source['auxiliary_values']:
            labs=e['entropy_variables']
            if sym in labs and set(labs)<=set(ORIGINAL)|{sym}:add(e,{sym})
    if len(out)!=3072 or tuple(doc['pair'])!=tuple(pair):raise ValueError('MARGINALS')
    for e in doc['cross_values']:add(e,set(pair))
    if len(out)!=4096:raise ValueError('ALL_SIZE')
    return out


def verify(values):
    if len(values)!=4096 or values[0]!=0:raise ValueError('VECTOR')
    X=1023;A=1024;B=2048
    if values[X|A]+values[X|B]-values[X|A|B]-values[X]!=0:raise ValueError('CONDITIONAL_INDEPENDENCE')
    scale=lcm(*(v.denominator for v in values.values()));h=[int(values[m]*scale) for m in range(4096)]
    if min(h)<0:raise ValueError('NEGATIVE_ENTROPY')
    checks=0;minimum=None;full=4095
    for i in range(12):
        x=h[full]-h[full^(1<<i)]
        if x<0:raise ValueError('MONOTONICITY')
        minimum=x if minimum is None else min(minimum,x);checks+=1
    for i,j in combinations(range(12),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            x=h[z|a]+h[z|b]-h[z|a|b]-h[z]
            if x<0:raise ValueError(('CMI',i,j,z))
            minimum=min(minimum,x);checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    if checks!=67596:raise ValueError('COUNT')
    return {'elemental_shannon_checks':checks,'independence_equalities':1,
            'minimum_scaled_shannon_slack':minimum,'scale_digits':len(str(scale))}


def main():
    base,c12,c13,summary=map(pin,(BASE,C12,C13,SUMMARY))
    if summary['base_sha256']!=BASE[1] or summary['cross12_sha256']!=C12[1] or summary['cross13_sha256']!=C13[1] or len(summary['pairs'])!=9:
        raise ValueError('SUMMARY_BINDING')
    expected={(a,b) for a in V for b in W};seen=set();records=[]
    for record in summary['pairs']:
        pair=tuple(record['pair'])
        if pair not in expected or pair in seen or not record.get('exact_candidate_found'):raise ValueError('PAIR_COVERAGE')
        seen.add(pair);item=(record['candidate_file'],record['candidate_sha256']);doc=pin(item)
        vals=read_values(base,c12,c13,doc,pair);checks=verify(vals);controls={}
        modified=dict(vals);modified[4095]+=Fraction(1,7)
        try:verify(modified)
        except ValueError:controls['changed_full_entropy']='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',pair))
        modified=dict(vals);modified.pop(3072)
        try:verify(modified)
        except (ValueError,KeyError):controls['missing_cross_entropy']='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',pair))
        records.append({'pair':pair,'candidate_file':item[0],'candidate_sha256':item[1],
                        'exact_checks':checks,'mutation_controls':controls})
    if seen!=expected:raise ValueError('PAIR_SET')
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'producer_summary_sha256':SUMMARY[1],'pairs':records,'all_nine_checked':True,
         'total_elemental_shannon_checks':sum(x['exact_checks']['elemental_shannon_checks'] for x in records),
         'total_conditional_independence_equalities':len(records),
         'limits':'Nine separately consistent 12-variable pair systems only; joint constraints involving multiple auxiliaries from each branch and the full 17-variable cone are not checked.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'all_nine_checked':True,'pair_count':len(records),
                      'total_elemental_shannon_checks':out['total_elemental_shannon_checks'],
                      'total_conditional_independence_equalities':len(records)},indent=2))


if __name__=='__main__':main()
