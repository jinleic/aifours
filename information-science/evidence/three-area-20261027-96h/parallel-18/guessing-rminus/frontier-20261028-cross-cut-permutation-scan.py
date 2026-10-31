#!/usr/bin/env python3
"""Exact scan of a valid cross-copy separator under all active-role choices.

The pinned eight-CMI identity has six original background variables and four
active roles. For each of 9 cross-branch auxiliary pairs and 10P4 role maps,
the resulting L>=0 cut is checked at the two pinned star candidates.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
OLD=('frontier-20261028-crossbranch13-fixed-u-exact-candidate.json','9744448c5473f3781ef616d46c5615dff649c0f4581dcf7f9bbd4b5c25ee9ce1')
NEW=('frontier-20261028-crossbranch13-one-cut-exact-candidate.json','7769476a34e418e76b2387305533fe688b4d5aee2ec975e8f6b1d8aef311da48')
CUT=('frontier-20261028-cross-pair-farkas-independent-check-result.json','199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45')
OUT=ROOT/'frontier-20261028-cross-cut-permutation-scan-result.json'
ORIG=tuple('abcdefghij');V=("d'1","e'1","g'2");W=("f'3","g'3","h'4");ROLES=(1,2,3,7)


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def profile(doc,sym=None):
    items=doc['primal_values'] if sym is None else doc['auxiliary_values'];out=[None]*1024
    if sym is None:out[0]=Fraction(0)
    for e in items:
        labs=e['entropy_variables'];allowed=set(ORIG)|({sym} if sym else set())
        if not set(labs)<=allowed or (sym is not None and sym not in labs):continue
        m=sum(1<<ORIG.index(v) for v in labs if v in ORIG)
        if out[m] is not None:raise ValueError('DUPLICATE_COORDINATE')
        out[m]=Fraction(e['value'])
    if any(x is None for x in out):raise ValueError(('INCOMPLETE_PROFILE',sym))
    return out


def main():
    base,c12,old,new,cert=map(pin,(BASE,C12,OLD,NEW,CUT))
    if not cert['all_checked'] or cert['exact_identity']['known_constant']!='-12637/1725000':raise ValueError('CUT_CERTIFICATE')
    terms=[(int(m),Fraction(c)) for m,c in cert['exact_identity']['known_terms']]
    bg=1023^sum(1<<x for x in ROLES)
    if len(terms)!=16 or any((m&bg)!=bg or (m&3072)==3072 or c.denominator!=1 for m,c in terms):raise ValueError('CUT_FORM')
    H=profile(base);D={v:profile(c12,v) for v in V};F0={w:profile(old,w) for w in W};F1={w:profile(new,w) for w in W}
    scale=lcm(*(x.denominator for arr in [H,*D.values(),*F0.values(),*F1.values()] for x in arr))
    def ints(arr):return [int(x*scale) for x in arr]
    H=ints(H);D={k:ints(x) for k,x in D.items()};F0={k:ints(x) for k,x in F0.items()};F1={k:ints(x) for k,x in F1.items()}
    # Every source entropy contains the common background. Encode which of
    # the four active roles is missing and which auxiliary marginal is used.
    desc=[]
    for m,c in terms:
        missing=1023^(m&1023);bits=sum(((missing>>old)&1)<<j for j,old in enumerate(ROLES))
        if missing&bg:raise ValueError('UNEXPECTED_BACKGROUND')
        kind=1 if m&1024 else 2 if m&2048 else 0
        desc.append((bits,kind,int(c)))
    records=[]
    for label,Fmap in (('old_star',F0),('one_cut_reoptimized',F1)):
        neg=[];minimum=None;checked=0
        for roles in permutations(range(10),4):
            missing=[sum((1<<roles[j]) for j in range(4) if bits&(1<<j)) for bits in range(16)]
            for v in V:
                for w in W:
                    arrays=(H,D[v],Fmap[w]);value=sum(c*arrays[k][1023^missing[b]] for b,k,c in desc);checked+=1
                    if minimum is None or value<minimum:minimum=value
                    if value<0:neg.append({'V':v,'W':w,'roles_bc_dh':[x+1 for x in roles],'scaled_value':value})
        if checked!=45360:raise ValueError('COUNT')
        records.append({'profile':label,'cuts_checked':checked,'negative_count':len(neg),
                        'minimum':str(Fraction(minimum,scale)),'negative_cuts':neg})
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'old_star_sha256':OLD[1],
         'new_one_cut_sha256':NEW[1],'cut_certificate_sha256':CUT[1],'scale':str(scale),'scans':records,
         'limits':'Checks only permutations of one eight-CMI cross-copy inequality, on the fixed auxiliary profiles. A negative cut invalidates that fixed star point for conditionally independent copies; it does not exclude the original profile with other auxiliaries.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='negative_cuts'} for r in records],indent=2))


if __name__=='__main__':main()
