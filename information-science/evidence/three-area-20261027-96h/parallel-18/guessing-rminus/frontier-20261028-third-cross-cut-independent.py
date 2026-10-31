#!/usr/bin/env python3
"""Independent vectorized exact replay of all third-gluing cross-cut instances.

Uses role-permutation arrays rather than the producer's scalar nested scan.
The earlier violating point is rechecked as a negative control.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import lcm
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
OLD=('frontier-20261028-crossbranch13-twofamilies-exact-candidate.json','437b5045b998718395469fd47f216e5f426a42fcdc0dd6cfb4e63eff49e0764c')
NEW=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
CUT=('frontier-20261028-cross-pair-round3-farkas-independent-result.json','b2e4e3d31006c40774601f0e91bd4ba6651aba1de9b4de3c75f87d64fd1904ac')
OUT=ROOT/'frontier-20261028-third-cross-cut-independent-result.json'
ORIG=tuple('abcdefghij');V=("d'1","e'1","g'2");W=("f'3","g'3","h'4");ROLES=(1,3,4,5,6,8,9)


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
        if out[m] is not None:raise ValueError('DUPLICATE')
        out[m]=Fraction(e['value'])
    if any(x is None for x in out):raise ValueError(('PROFILE_SIZE',sym))
    return out


def main():
    base,c12,old,new,receipt=map(pin,(BASE,C12,OLD,NEW,CUT))
    if not receipt['all_checked'] or receipt['exact_identity']['known_constant']!='-7123/3450000':raise ValueError('CUT_RECEIPT')
    terms=[(int(m),int(Fraction(c))) for m,c in receipt['exact_identity']['known_terms']]
    bg=1023^sum(1<<x for x in ROLES)
    if len(terms)!=18 or any((m&bg)!=bg or m&3072==3072 for m,c in terms):raise ValueError('TERM_SCOPE')
    H=profile(base);D={v:profile(c12,v) for v in V};F0={w:profile(old,w) for w in W};F1={w:profile(new,w) for w in W}
    scale=lcm(*(x.denominator for arr in [H,*D.values(),*F0.values(),*F1.values()] for x in arr))
    def ints(a):return np.array([int(x*scale) for x in a],dtype=np.int64)
    H=ints(H);D={k:ints(x) for k,x in D.items()};F0={k:ints(x) for k,x in F0.items()};F1={k:ints(x) for k,x in F1.items()}
    if max(abs(int(x)) for arr in [H,*D.values(),*F0.values(),*F1.values()] for x in arr)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    roles=np.array(list(permutations(range(10),7)),dtype=np.int64)
    if len(roles)!=604800:raise ValueError('ROLE_COUNT')
    mapped=[]
    for m,c in terms:
        missing=1023^(m&1023)
        if missing&bg:raise ValueError('BACKGROUND')
        mask=np.full(len(roles),1023,dtype=np.int64)
        for j,oldrole in enumerate(ROLES):
            if missing&(1<<oldrole):mask ^= np.left_shift(1,roles[:,j])
        kind=1 if m&1024 else 2 if m&2048 else 0
        mapped.append((mask,kind,c))
    def scan(F):
        count=neg=0;minimum=None
        for v in V:
            for w in W:
                arrays=(H,D[v],F[w]);slack=np.zeros(len(roles),dtype=np.int64)
                for mask,k,c in mapped:slack+=c*arrays[k][mask]
                count+=len(slack);neg+=int((slack<0).sum());local=int(slack.min());minimum=local if minimum is None else min(minimum,local)
        if count!=5443200:raise ValueError('COUNT')
        return {'checked':count,'negative_count':neg,'minimum':str(Fraction(minimum,scale))}
    oldresult=scan(F0);newresult=scan(F1)
    if oldresult['negative_count']!=18 or oldresult['minimum']!='-17569/6900000':raise ValueError(('NEGATIVE_CONTROL',oldresult))
    if newresult['negative_count']!=0 or Fraction(newresult['minimum'])<0:raise ValueError(('NEW_CUT_VIOLATION',newresult))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'old_star_sha256':OLD[1],
         'new_star_sha256':NEW[1],'cut_receipt_sha256':CUT[1],
         'old_point_negative_control':oldresult,'new_point_exact_scan':newresult,
         'limits':'Only all active-role permutations of this one second gluing inequality on singleton aux pairs; no other inequalities, full-cross Shannon, or entropic realization follows.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
