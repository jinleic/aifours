#!/usr/bin/env python3
"""Finite check of the raw possible-switch run bound (single file, self-contained).

For random actual zero-free singleton-gap words (N=4p-1, R=p+1, F=3p-2),
biased toward few projected runs, compute:
  * nu_M of the literal raw possible-switch graph (edge between cyclically
    consecutive reflections iff values differ OR the gap holds a rotation),
    by exhaustive dynamic programming over the cycle (two linear cases);
  * eta = (#cyclic projected runs if >=2 else 0) + g_int, g_int = rotations in
    gaps between EQUAL consecutive reflection values;
  * o_pi, e_pi, and reflection-only REF existence by an element DP.
It asserts nu_M >= ceil(eta/2) when eta<F, nu_M=(F-1)/2 when eta=F, and, for
REF-failing words with nu_M<=p-3, that p<=o_pi and o_pi+e_pi+g_int<=2p-6.
"""
import argparse
import hashlib
import json
import random

SEED=2026102843


def matching_path(edges):
    a,b=0,0  # best ending without/with last vertex used
    best=[0]
    prev_free,prev_used=0,0
    for e in edges:
        nf=max(prev_free,prev_used)
        nu=prev_free+1 if e else -10**9
        prev_free,prev_used=nf,nu
    return max(prev_free,prev_used)


def nu_cycle(edges):
    F=len(edges)
    if not edges[-1]:return matching_path(edges[:-1])
    # case 1: closing edge unused -> path on all vertices with edges[:-1]
    c1=matching_path(edges[:-1])
    # case 2: closing edge (F-1,0) used -> remove vertices F-1 and 0: path on 1..F-2 with edges[1:F-2]
    c2=1+matching_path(edges[1:F-2])
    return max(c1,c2)


def analyse(w,p):
    N=len(w);refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    edges=[];g_int=0
    for k in range(F):
        i,j=refs[k],refs[(k+1)%F];occ=(j-i)%N!=1
        diff=w[i][0]!=w[j][0];edges.append(diff or occ)
        if occ and not diff:g_int+=1
    lab=[w[i][0] for i in refs]
    st=next((k for k in range(F) if lab[k]!=lab[k-1]),None)
    if st is None:runs=[F]
    else:
        runs=[]
        for k in range(F):
            if not runs or lab[(st+k)%F]!=lab[(st+k-1)%F]:runs.append(1)
            else:runs[-1]+=1
    nruns=len(runs) if len(runs)>=2 else 0
    eta=nruns+g_int
    if eta!=sum(edges):raise ValueError('eta formula')
    nu=nu_cycle(edges)
    o=sum(L%2 for L in runs);e=len(runs)-o
    states={(0,0)}
    for y in lab:
        new=set(states)
        for c,x in states:
            if c<2*p:new.add((c+1,(x+(y if c%2==0 else -y))%p))
        states=new
    ref=(2*p,0) in states
    return nu,eta,F,o,e,g_int,ref


def gen(rng,p):
    F=3*p-2;nr=rng.randrange(1,min(F,2*p)+1)
    cuts=sorted(rng.sample(range(1,F),nr-1)) if nr>1 else []
    lens=[b-a for a,b in zip([0]+cuts,cuts+[F])]
    labels=[rng.randrange(p)]
    for _ in range(nr-1):labels.append(rng.choice([x for x in range(p) if x!=labels[-1]]))
    if nr>1 and labels[-1]==labels[0]:return None
    vals=[l for l,L in zip(labels,lens) for _ in range(L)]
    bnd=[sum(lens[:k+1])-1 for k in range(nr)]
    pool=bnd if rng.random()<0.7 else list(range(F))
    if len(pool)<p+1:pool=list(range(F))
    gaps=set(rng.sample(pool,p+1))
    w=[]
    for i,y in enumerate(vals):
        w.append((y,1))
        if i in gaps:w.append((rng.randrange(1,p),0))
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);stats={}
    for p in (7,11,13):
        n=0;residual_like=0;max_o=0
        while n<3000:
            w=gen(rng,p)
            if w is None:continue
            nu,eta,F,o,e,g,ref=analyse(w,p);n+=1
            if eta<F and nu<-(-eta//2):raise ValueError('RM bound violated')
            if eta==F and nu!=(F-1)//2:raise ValueError('full cycle value')
            if nu<=p-3 and not ref:
                residual_like+=1;max_o=max(max_o,o)
                if not (p<=o and o+e+g<=2*p-6):raise ValueError('stratum corollary violated')
        stats[str(p)]={'words':n,'ref_failing_with_nu_le_p_minus_3':residual_like,'max_o_pi_seen_there':max_o}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'result':'PASS_RAW_RUN_BOUND','seed':SEED,'stats':stats},out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps({'result':'PASS_RAW_RUN_BOUND','stats':stats},sort_keys=True))


if __name__=='__main__':
    main()
