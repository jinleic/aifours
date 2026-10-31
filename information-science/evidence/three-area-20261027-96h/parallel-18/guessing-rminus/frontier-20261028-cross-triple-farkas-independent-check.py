#!/usr/bin/env python3
"""Independent exact verification of a fixed three-auxiliary Farkas identity.

Four elemental CMIs minus one tuple-independence expression cancel all
three-auxiliary entropies. The remaining fixed pair/star terms have an exact
negative value. No claim about alternative auxiliary assignments follows.
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
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
P1=('frontier-20261028-crossbranch23-round4-pair-1-1-candidate.json','c60246f6499aa7ff83ddd4b2c5dbd4aae35ae80137954efd96a21eed113d1b9b')
P2=('frontier-20261028-crossbranch23-round4-pair-3-1-candidate.json','59ed2e3479e7dafbbe42d54aaad7e58d1fcd489f0ea0fd37a88ce0d23fd716bb')
PAIR_RECEIPT=('frontier-20261028-crossbranch23-pairs-round4-independent-result.json','143db08d3ce5caf8e2f764473d0eb2fe5ce4f14a760e95df33b47903a4fc4540')
RAY=('frontier-20261028-cross-triple-farkas-result.json','a63d738fed78255bdf59c4df54f4e71d60eff2fb30aafdfa0975b97b976bc96a')
OUT=ROOT/'frontier-20261028-cross-triple-farkas-independent-check-result.json'
ORIGINAL=tuple('abcdefghij');AUX=("d'1","g'2","f'3");VARS=ORIGINAL+AUX;FULL=8191


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def values(base,c12,c13,p1,p2):
    out={0:Fraction(0)};idx={v:i for i,v in enumerate(VARS)}
    def add(e,required=None):
        labs=e['entropy_variables'];m=sum(1<<idx[v] for v in labs)
        if not m or m in out or (required is not None and not required<=set(labs)):raise ValueError('DUPLICATE_OR_LABEL')
        out[m]=Fraction(e['value'])
    for e in base['primal_values']:
        if set(e['entropy_variables'])<=set(ORIGINAL):add(e)
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for doc,allowed in ((c12,set(ORIGINAL)|set(AUX[:2])),(c13,set(ORIGINAL)|{AUX[2]})):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if set(labs)<=allowed and set(labs)&set(AUX):add(e)
    for doc,required in ((p1,{AUX[0],AUX[2]}),(p2,{AUX[1],AUX[2]})):
        if set(doc['pair'])!=required:raise ValueError('PAIR_LABEL')
        for e in doc['cross_values']:
            if not set(e['entropy_variables'])<=set(ORIGINAL)|required:raise ValueError('PAIR_COORDINATE')
            add(e,required)
    if len(out)!=7168:raise ValueError(('KNOWN_SIZE',len(out)))
    return out


def verify(rows,h):
    agg={};kinds=Counter();decoded=[]
    for entry in rows:
        meta=entry['metadata'];terms=tuple(tuple(t) for t in meta['terms']);weight=Fraction(entry['ray_weight'])
        if meta['equality']:
            x=1023;a=1024|2048;b=4096
            if terms!=((x|a,1),(x|b,1),(x|a|b,-1),(x,-1)) or weight!=-1:raise ValueError('INDEPENDENCE_ROW')
            kinds['conditional_independence']+=1;decoded.append({'kind':'independence','weight':str(weight)})
        else:
            if len(terms)!=4 or weight<=0:raise ValueError('CMI_WEIGHT')
            pos=[m for m,c in terms if c==1];neg=[m for m,c in terms if c==-1]
            if len(pos)!=2 or len(neg)!=2:raise ValueError('CMI_COEFFICIENTS')
            z=pos[0]&pos[1];a=pos[0]^z;b=pos[1]^z
            if not a or not b or a&(a-1) or b&(b-1) or a==b or set(neg)!={z,pos[0]|pos[1]}:raise ValueError('CMI_STRUCTURE')
            kinds['CMI']+=1;decoded.append({'kind':'CMI','A':a.bit_length()-1,'B':b.bit_length()-1,'Z_mask':z,'weight':str(weight)})
        for m,c in terms:
            if m:agg[m]=agg.get(m,Fraction(0))+weight*c
    agg={m:c for m,c in agg.items() if c}
    if kinds!=Counter({'CMI':4,'conditional_independence':1}):raise ValueError(('KINDS',kinds))
    if any(m&7168==7168 for m in agg):raise ValueError('TRIPLE_ENTROPY_NOT_CANCELLED')
    try:constant=sum((c*h[m] for m,c in agg.items()),Fraction(0))
    except KeyError as exc:raise ValueError('MISSING_MARGINAL') from exc
    if constant!=Fraction(-1086281,69000000):raise ValueError(('CONSTANT',str(constant)))
    return {'row_kinds':dict(kinds),'known_entropy_terms':len(agg),'triple_auxiliary_terms':0,
            'known_constant':str(constant),'known_terms':[[m,str(c)] for m,c in sorted(agg.items())],
            'decoded_rows':decoded}


def main():
    base,c12,c13,p1,p2,pairs,ray=map(pin,(BASE,C12,C13,P1,P2,PAIR_RECEIPT,RAY))
    if not pairs['all_nine_checked'] or pairs['base_sha256']!=BASE[1] or pairs['cross12_sha256']!=C12[1] or pairs['cross13_sha256']!=C13[1]:raise ValueError('PAIR_RECEIPT')
    records={tuple(e['pair']):e['candidate_sha256'] for e in pairs['pairs']}
    if records.get((AUX[0],AUX[2]))!=P1[1] or records.get((AUX[1],AUX[2]))!=P2[1]:raise ValueError('PAIR_HASHES')
    h=values(base,c12,c13,p1,p2);rows=ray['exact_farkas_candidate']['weights'];result=verify(rows,h);controls={}
    def expect(tag,mut):
        rr=deepcopy(rows);hh=dict(h);mut(rr,hh)
        try:verify(rr,hh)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('dropped_cmi',lambda rr,hh:rr.pop(0))
    expect('negative_cmi_weight',lambda rr,hh:rr[0].__setitem__('ray_weight','-1'))
    expect('changed_independence_weight',lambda rr,hh:rr[-1].__setitem__('ray_weight','-2'))
    term=result['known_terms'][0][0]
    expect('altered_fixed_entropy',lambda rr,hh:hh.__setitem__(term,hh[term]+Fraction(1,7)))
    expect('missing_fixed_entropy',lambda rr,hh:hh.pop(term))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'pair_candidate_sha256':[P1[1],P2[1]],'pair_receipt_sha256':PAIR_RECEIPT[1],
         'ray_sha256':RAY[1],'variables':VARS,'exact_identity':result,'all_checked':True,
         'mutation_controls':controls,
         'limits':'With tuple independence the fixed pair marginals have no Shannon extension. An actual law satisfying both pairwise conditional independencies could be recoupled to tuple independence; other auxiliary/pair assignments and almost-entropic closure remain open.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
