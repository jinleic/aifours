#!/usr/bin/env python3
"""Candidate universal R=p+1,F=3p-2 original-order selector.

REF is decided by an exact element DP. On REF failure, cyclic equal-neighbor
reduction MUST leave a p-term affine AP, and recorded equal pairs supply an
identity S of size2p-2. Full-S inverse rotation pair finishes immediately.
Otherwise drop ONE fixed recorded pair E and search same-anchor-gap/nonzero
signed-sum or different-anchor-gap/nonzero-signed-difference completions by
two actual anchors. No shortened-word witness is accepted as output.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
import random

SEED=2026102844


def mul(g,h,p):
    x,e=g;y,b=h
    return ((x+(-y if e else y))%p,e^b)


def product(w,idx,p):
    g=(0,0)
    for i in idx:g=mul(g,w[i],p)
    return g


def ref_witness(w,p):
    states={(0,0):()}
    for i,(y,b) in enumerate(w):
        if not b:continue
        new=dict(states)
        for (k,x),indices in states.items():
            if k<2*p:
                key=(k+1,(x+(y if k%2==0 else -y))%p)
                if key not in new:new[key]=indices+(i,)
        states=new
    return states.get((2*p,0))


def free_core(w):
    v=[i for i,(_,e) in enumerate(w) if e];pairs=[]
    while len(v)>1:
        j=next((j for j in range(len(v)) if w[v[j]][0]==w[v[(j+1)%len(v)]][0]),None)
        if j is None:break
        a,b=v[j],v[(j+1)%len(v)];pairs.append((a,b))
        v=[i for i in v if i not in (a,b)]
    return v,pairs


def transported_at_cut(w,S,extras,start,p):
    N=len(w);pref=(0,0);out={}
    for k in range(N):
        i=(start+k)%N
        if i in extras:
            y,b=w[i];x,e=pref
            out[i]=((2*x+(-y if e else y))%p,1) if b else (((-y if e else y)%p),0)
        if i in S:pref=mul(pref,w[i],p)
    if pref!=(0,0):raise ValueError('S_NOT_IDENTITY')
    return out


def construct(w,p):
    N=len(w);ref=ref_witness(w,p)
    if ref is not None:return sorted(ref),{'route':'REF'}
    anchors,pairs=free_core(w)
    if len(anchors)!=p or len(pairs)!=p-1:raise ValueError('REF_INVERSE_CORE_LENGTH')
    order=sorted(anchors);labs=[w[i][0] for i in order];d=(labs[1]-labs[0])%p
    if not d or any(labs[k]!=(labs[0]+k*d)%p for k in range(p)):raise ValueError('REF_INVERSE_CORE_NOT_AP')
    S={i for pair in pairs for i in pair};rots=[i for i,(_,e) in enumerate(w) if not e]
    if product(w,sorted(S),p)!=(0,0):raise ValueError('DELETION_RESERVOIR_NOT_IDENTITY')
    transported=transported_at_cut(w,S,set(rots),0,p)
    for r,s in itertools.combinations(rots,2):
        if (transported[r][0]+transported[s][0])%p==0:
            selected=sorted(S|{r,s})
            if len(selected)!=2*p or product(w,selected,p)!=(0,0):raise ValueError('FULL_S_COMPLETION')
            return selected,{'route':'FULL_S','anchors':order,'pairs':pairs,'rotations':[r,s]}
    E=pairs[0];Sd=S-set(E)
    if product(w,sorted(Sd),p)!=(0,0):raise ValueError('PAIR_DROP_NOT_IDENTITY')
    for r,s in itertools.combinations(rots,2):
        t=transported_at_cut(w,Sd,set(rots)|set(order),r,p)
        distance=(s-r)%N
        X=sorted((i for i in order if 0<(i-r)%N<distance),key=lambda i:(i-r)%N)
        Y=sorted((i for i in order if (i-r)%N>distance),key=lambda i:(i-r)%N)
        u,v=t[r][0],t[s][0]
        if not X or not Y:
            z=(u+v)%p
            if not z:continue
            Z=X if X else Y
            chosen=next(([i,j] for i,j in itertools.combinations(Z,2) if (t[i][0]-t[j][0]+z)%p==0),None)
            route='DROP_SAME_GAP'
        else:
            z=(v-u)%p
            if not z:continue
            chosen=next(([i,j] for i in X for j in Y if (t[i][0]-t[j][0])%p==z),None)
            route='DROP_DIFFERENT_GAPS'
        if chosen is None:raise ValueError('ANCHOR_DIFFERENCE_NOT_COVERED')
        selected=sorted(Sd|{r,s}|set(chosen))
        if len(selected)!=2*p or product(w,selected,p)!=(0,0):raise ValueError('ACTUAL_SELECTOR_FAILED')
        return selected,{'route':route,'anchors':order,'pairs':pairs,'dropped_pair':list(E),
                         'rotations':[r,s],'selected_anchors':chosen}
    raise ValueError('UNIVERSAL_BAND_CONSTRUCTION_FAILED')


def inserted_word(rng,p,reflection_values,forced_equal=False):
    F=len(reflection_values);core,pairs=free_core([[y,1] for y in reflection_values])
    S={i for pair in pairs for i in pair}
    occupied=[rng.randrange(F) for _ in range(p+1)]
    amounts=Counter(occupied);w=[];before=0;c=rng.randrange(1,p)
    for i,y in enumerate(reflection_values):
        w.append([y,1]);before+=i in S
        for _ in range(amounts[i]):
            b=(-c if before%2 else c)%p if forced_equal else rng.randrange(p)
            w.append([b,0])
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def expand_ap(rng,p,nested=False):
    c=rng.randrange(p);d=rng.randrange(1,p);z=[(c+k*d)%p for k in range(p)]
    if nested:
        at=rng.randrange(len(z)+1);head=[rng.randrange(p) for _ in range(p-1)]
        z=z[:at]+head+head[::-1]+z[at:]
    else:
        for _ in range(p-1):
            at=rng.randrange(len(z)+1);a=rng.randrange(p);z=z[:at]+[a,a]+z[at:]
    return z


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',required=True);args=ap.parse_args()
    rng=random.Random(SEED);cases=[];routes=Counter();serial=0
    def add(p,w,kind):
        nonlocal serial
        sel,meta=construct(w,p);serial+=1;routes[meta['route']]+=1
        cases.append({'p':p,'word':w,'selector':sel,'kind':kind,'proof_metadata':meta})
    # exhaustive NORMALISED p=3 reflection lists: all 729, two different actual rotation placements each
    for rest in itertools.product(range(3),repeat=6):
        refl=[0]+list(rest)
        for forced in (False,True):add(3,inserted_word(rng,3,refl,forced),'p3-exhaustive-reflection/forced-'+str(forced))
    for p in (5,7,11,13,17):
        for trial in range(120):
            refl=[rng.randrange(p) for _ in range(3*p-2)]
            add(p,inserted_word(rng,p,refl),'random')
        for nested in (False,True):
            for trial in range(160):
                refl=expand_ap(rng,p,nested)
                add(p,inserted_word(rng,p,refl,trial%2==0),'AP-tree/nested-'+str(nested))
    old='frontier-20261028-olson-affine-core-surplus2-check-results.json'
    with open(old,'rb') as f:family_raw=f.read()
    for case in json.loads(family_raw)['cases']:add(case['p'],case['word'],'p+4-low-raw-family')
    out={'seed':SEED,'result':'PASS_UNIVERSAL_ROTATION_BAND_CONSTRUCTION',
         'family_input_sha256':hashlib.sha256(family_raw).hexdigest(),'cases':cases,'routes':dict(routes)}
    with open(args.output,'x',encoding='utf-8') as f:json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    print(json.dumps({'result':out['result'],'actual_words':len(cases),'routes':dict(routes)},sort_keys=True))


if __name__=='__main__':main()
