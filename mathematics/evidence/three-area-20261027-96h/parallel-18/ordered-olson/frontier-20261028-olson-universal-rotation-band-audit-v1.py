#!/usr/bin/env python3
"""Independent saved-word audit and different-pair witness reconstruction.

Imports no producer. Group products use affine signs +/-1. REF uses a bitset
count DP. Reported pairs are checked as a literal cyclic deletion trace, and
EVERY recorded pair is independently dropped to check the identity/anchor
interface. A NEW selector is found from the LAST pair (producer uses first)
by brute force on four transported optional occurrences (early exit, not an
exhaustive-subset claim), and is then multiplied on ORIGINAL actual indices.
"""
import argparse
from collections import Counter
import copy
from itertools import combinations, product as cartesian
import hashlib
import json
import random


def group_product(w,idx,p):
    off,sign=0,1
    for i in idx:
        y,b=w[i];off=(off+sign*y)%p
        if b:sign=-sign
    return off,sign


def ref_bits(values,p):
    mask=(1<<p)-1;B=[0]*(len(values)+1);B[0]=1
    for n,y in enumerate(values):
        for k in range(n,-1,-1):
            a=y if k%2==0 else -y;a%=p;x=B[k]
            shifted=((x<<a)|(x>>(p-a)))&mask if a else x
            B[k+1]|=shifted
    return B


def optional_transports(w,S,extras,p):
    off,sign=0,1;T={}
    for i,(y,b) in enumerate(w):
        if i in extras:T[i]=((2*off+sign*y)%p,-1) if b else ((sign*y)%p,1)
        if i in S:
            off=(off+sign*y)%p
            if b:sign=-sign
    if (off,sign)!=(0,1):raise ValueError('FIXED_IDENTITY')
    return T


def four_optional_product(T,ids,p):
    off,sign=0,1
    for i in sorted(ids):
        a,s=T[i];off=(off+sign*a)%p;sign*=s
    return off,sign


def audit_case(case,reconstruct=True):
    p,w=case['p'],case['word'];N=len(w);selection=case['selector'];M=case['proof_metadata']
    if N!=4*p-1 or any(len(z)!=2 or not isinstance(z[0],int) or not 0<=z[0]<p or z[1] not in (0,1) for z in w):
        raise ValueError('WORD_ENCODING')
    refs=[i for i,z in enumerate(w) if z[1]];rots=[i for i,z in enumerate(w) if not z[1]]
    if len(refs)!=3*p-2 or len(rots)!=p+1:raise ValueError('COUNTS')
    if len(selection)!=2*p or selection!=sorted(set(selection)) or any(not 0<=i<N for i in selection):
        raise ValueError('SELECTION')
    if group_product(w,selection,p)!=(0,1):raise ValueError('ORIGINAL_PRODUCT')
    B=ref_bits([w[i][0] for i in refs],p)
    REF=bool(B[2*p]&1)
    if M['route']=='REF':
        if not REF or any(i in rots for i in selection):raise ValueError('REF_ROUTE')
        return M['route'],0,0
    if REF:raise ValueError('UNNECESSARY_NONREF_ROUTE')
    if max(k for k in range(0,len(B),2) if B[k]&1)!=2*p-2:raise ValueError('MAX_REF_IDENTITY')
    anchors=M['anchors'];pairs=M['pairs']
    if len(anchors)!=p or anchors!=sorted(set(anchors)) or any(i not in refs for i in anchors):raise ValueError('ANCHORS')
    if len(pairs)!=p-1 or len({i for pair in pairs for i in pair})!=2*p-2:raise ValueError('PAIR_PARTITION')
    if set(anchors)|{i for pair in pairs for i in pair}!=set(refs):raise ValueError('PAIR_PARTITION')
    present=refs[:]
    for pair in pairs:
        if len(pair)!=2:raise ValueError('PAIR_TRACE')
        a,b=pair
        if a not in present or b not in present or w[a]!=w[b]:raise ValueError('PAIR_TRACE')
        j=present.index(a)
        if present[(j+1)%len(present)]!=b:raise ValueError('PAIR_TRACE')
        present.remove(a);present.remove(b)
    if set(present)!=set(anchors):raise ValueError('ANCHOR_SURVIVORS')
    labels=[w[i][0] for i in anchors];d=(labels[1]-labels[0])%p
    if not d or any(labels[k]!=(labels[0]+k*d)%p for k in range(p)):raise ValueError('ANCHOR_AP')
    S=set(refs)-set(anchors)
    if group_product(w,sorted(S),p)!=(0,1):raise ValueError('FULL_REF_IDENTITY')
    # Every drop preserves identity and one common affine-conjugate AP of actual anchors.
    pair_checks=0
    for E in pairs:
        D=S-set(E)
        T=optional_transports(w,D,set(anchors)|set(rots),p)
        delta=(T[anchors[1]][0]-T[anchors[0]][0])%p
        eps=1 if delta==d else -1 if delta==(-d)%p else 0
        if not eps or any(T[i]!=((T[anchors[0]][0]+eps*(w[i][0]-w[anchors[0]][0]))%p,-1) for i in anchors):
            raise ValueError('ANCHOR_AP_CHANGED_BY_PAIR_DROP')
        pair_checks+=1
    if not reconstruct:return M['route'],pair_checks,0
    # Generic independent search: all full-S pairs first, then four extras after LAST pair drop.
    T=optional_transports(w,S,set(rots),p)
    for r,s in combinations(rots,2):
        if four_optional_product(T,[r,s],p)==(0,1):
            found=sorted(S|{r,s})
            if group_product(w,found,p)!=(0,1):raise ValueError('INDEPENDENT_FULL_COMPLETION')
            return M['route'],pair_checks,1
    D=S-set(pairs[-1]);T=optional_transports(w,D,set(anchors)|set(rots),p)
    for r,s in combinations(rots,2):
        for a,b in combinations(anchors,2):
            if four_optional_product(T,[r,s,a,b],p)==(0,1):
                found=sorted(D|{r,s,a,b})
                if len(found)!=2*p or group_product(w,found,p)!=(0,1):raise ValueError('INDEPENDENT_DROP_COMPLETION')
                return M['route'],pair_checks,1
    raise ValueError('INDEPENDENT_LAST_PAIR_WITNESS_NOT_FOUND')


def adjacent_distinct_diagnostics():
    results=[]
    for p,h in ((3,1),(3,2),(5,1),(5,2)):
        n=p+2*h;count=0
        # Enumerate adjacent-distinct lists directly, normalising first value to 0.
        def visit(prefix):
            if len(prefix)==n:
                if prefix[-1]!=prefix[0]:yield prefix
                return
            for y in range(p):
                if y!=prefix[-1]:yield from visit(prefix+[y])
        for seq in visit([0]):
            bits=ref_bits(seq,p)
            if not any(bits[k]&1 for k in range(2*h+2,n+1,2)):raise ValueError('ADJACENT_DISTINCT_LEMMA_COUNTEREXAMPLE')
            count+=1
        results.append({'p':p,'h':h,'normalised_cyclic_adjacent_distinct_lists':count})
    rng=random.Random(2026102846)
    for p,h in ((7,2),(11,2),(11,3),(13,4)):
        count=0;n=p+2*h
        while count<1000:
            seq=[rng.randrange(p)]
            while len(seq)<n:seq.append(rng.choice([y for y in range(p) if y!=seq[-1]]))
            if seq[-1]==seq[0]:continue
            bits=ref_bits(seq,p)
            if not any(bits[k]&1 for k in range(2*h+2,n+1,2)):raise ValueError('SAMPLED_ADJACENCY_COUNTEREXAMPLE')
            count+=1
        results.append({'p':p,'h':h,'sampled_lists':count})
    return results


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('inputs',nargs='+');ap.add_argument('--output',required=True);args=ap.parse_args()
    pins={};routes=Counter();pairchecks=0;newwitness=0;sample=None
    for path in args.inputs:
        with open(path,'rb') as f:raw=f.read()
        pins[path]=hashlib.sha256(raw).hexdigest()
        for case in json.loads(raw)['cases']:
            route,k,w=audit_case(case);routes[route]+=1;pairchecks+=k;newwitness+=w
            if route!='REF' and sample is None:sample=case
    c=copy.deepcopy(sample);c['selector'][1]=c['selector'][0]
    try:audit_case(c,False)
    except ValueError as e:
        if str(e)!='SELECTION':raise
    else:raise ValueError('DUPLICATE_CONTROL_SURVIVED')
    c=copy.deepcopy(sample);r=next(i for i in c['selector'] if not c['word'][i][1]);c['word'][r][0]=(c['word'][r][0]+1)%c['p']
    try:audit_case(c,False)
    except ValueError as e:
        if str(e)!='ORIGINAL_PRODUCT':raise
    else:raise ValueError('ROTATION_CONTROL_SURVIVED')
    c=copy.deepcopy(sample);c['proof_metadata']['anchors'][0]=next(i for i,z in enumerate(c['word']) if not z[1])
    try:audit_case(c,False)
    except ValueError as e:
        if str(e)!='ANCHORS':raise
    else:raise ValueError('ANCHOR_CONTROL_SURVIVED')
    diagnostics=adjacent_distinct_diagnostics()
    out={'result':'PASS_INDEPENDENT_UNIVERSAL_ROTATION_BAND','input_sha256':pins,
         'actual_words_and_selectors':sum(routes.values()),'routes':dict(routes),
         'matched_pair_drops_checked':pairchecks,'new_full_or_last_pair_witnesses':newwitness,
         'adjacent_distinct_diagnostics':diagnostics,
         'controls':['DUPLICATE_SELECTED_INDEX','ALTERED_SELECTED_ROTATION','ROTATION_AS_ANCHOR'],
         'scope':'bounded actual fixtures and field-list diagnostics, not a disjoint proof/formal/novelty review'}
    with open(args.output,'x',encoding='utf-8') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps({k:out[k] for k in ('result','actual_words_and_selectors','routes','matched_pair_drops_checked','new_full_or_last_pair_witnesses','controls')},sort_keys=True))


if __name__=='__main__':main()
