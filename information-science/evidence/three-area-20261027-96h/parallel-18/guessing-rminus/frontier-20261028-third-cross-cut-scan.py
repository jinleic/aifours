#!/usr/bin/env python3
"""Exact chunked scan of all active-role permutations of the third gluing cut.

Tests every 10P7 role assignment and all nine singleton auxiliary pairs on two
fixed star points. No full 17-variable or original-profile claim follows.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import islice,permutations
from math import lcm,perm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
OLD=('frontier-20261028-crossbranch13-twofamilies-exact-candidate.json','437b5045b998718395469fd47f216e5f426a42fcdc0dd6cfb4e63eff49e0764c')
NEW=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
CUT=('frontier-20261028-cross-pair-round3-farkas-independent-result.json','b2e4e3d31006c40774601f0e91bd4ba6651aba1de9b4de3c75f87d64fd1904ac')
OUT=ROOT/'frontier-20261028-third-cross-cut-scan-result.json'
ORIG=tuple('abcdefghij');V=("d'1","e'1","g'2");W=("f'3","g'3","h'4");ROLES=(1,3,4,5,6,8,9)


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def profile(doc,sym=None):
    data=doc['primal_values'] if sym is None else doc['auxiliary_values'];out=[None]*1024
    if sym is None:out[0]=Fraction(0)
    for e in data:
        labs=e['entropy_variables'];allowed=set(ORIG)|({sym} if sym else set())
        if not set(labs)<=allowed or (sym is not None and sym not in labs):continue
        m=sum(1<<ORIG.index(v) for v in labs if v in ORIG)
        if out[m] is not None:raise ValueError('DUPLICATE')
        out[m]=Fraction(e['value'])
    if any(x is None for x in out):raise ValueError(('PROFILE_SIZE',sym))
    return out


def main():
    start=monotonic();base,c12,old,new,cut=map(pin,(BASE,C12,OLD,NEW,CUT))
    if not cut['all_checked'] or cut['exact_identity']['known_constant']!='-7123/3450000':raise ValueError('CUT_RECEIPT')
    terms=[(int(m),int(Fraction(c))) for m,c in cut['exact_identity']['known_terms']]
    bg=1023^sum(1<<i for i in ROLES)
    if len(terms)!=18 or any((m&bg)!=bg or m&3072==3072 for m,c in terms):raise ValueError('TERM_SCOPE')
    H=profile(base);D={v:profile(c12,v) for v in V};F0={w:profile(old,w) for w in W};F1={w:profile(new,w) for w in W}
    scale=lcm(*(x.denominator for arr in [H,*D.values(),*F0.values(),*F1.values()] for x in arr))
    def integer(a):return np.array([int(x*scale) for x in a],dtype=np.int64)
    H=integer(H);D={k:integer(a) for k,a in D.items()};F0={k:integer(a) for k,a in F0.items()};F1={k:integer(a) for k,a in F1.items()}
    if max(abs(int(x)) for arr in [H,*D.values(),*F0.values(),*F1.values()] for x in arr)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    records={name:{'checked':0,'negative_count':0,'minimum_scaled':None,'negative_examples':[]} for name in ('old_twofamily','new_threefamily')}
    iterator=permutations(range(10),7)
    while True:
        chunk=list(islice(iterator,40000))
        if not chunk:break
        roles=np.array(chunk,dtype=np.int64);maps=[]
        for m,c in terms:
            missing=1023^(m&1023)
            if missing&bg:raise ValueError('BACKGROUND')
            key=np.full(len(roles),1023,dtype=np.int64)
            for j,oldrole in enumerate(ROLES):
                if missing&(1<<oldrole):key ^= np.left_shift(1,roles[:,j])
            k=1 if m&1024 else 2 if m&2048 else 0;maps.append((key,k,c))
        for name,F in (('old_twofamily',F0),('new_threefamily',F1)):
            record=records[name]
            for v in V:
                for w in W:
                    arrays=(H,D[v],F[w]);slack=np.zeros(len(roles),dtype=np.int64)
                    for key,k,c in maps:slack+=c*arrays[k][key]
                    record['checked']+=len(slack);record['negative_count']+=int((slack<0).sum())
                    local=int(slack.min());record['minimum_scaled']=local if record['minimum_scaled'] is None else min(record['minimum_scaled'],local)
                    for i in np.flatnonzero(slack<0)[:max(0,20-len(record['negative_examples']))]:
                        record['negative_examples'].append({'D':v,'F':w,'active_vertices':[int(x)+1 for x in roles[i]],'scaled_slack':int(slack[i])})
    expected=9*perm(10,7)
    for r in records.values():
        if r['checked']!=expected:raise ValueError(('COUNT',r['checked'],expected))
        r['minimum_exact']=str(Fraction(r.pop('minimum_scaled'),scale))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'old_star_sha256':OLD[1],'new_star_sha256':NEW[1],
         'cut_receipt_sha256':CUT[1],'scale':str(scale),'expected_per_point':expected,'scans':records,'elapsed_seconds':monotonic()-start,
         'limits':'All role permutations of one third gluing inequality on singleton aux pairs at two fixed star points; not all inequalities, entropic realization, or an original-base exclusion.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({name:{k:v for k,v in row.items() if k!='negative_examples'} for name,row in records.items()},indent=2))


if __name__=='__main__':main()
