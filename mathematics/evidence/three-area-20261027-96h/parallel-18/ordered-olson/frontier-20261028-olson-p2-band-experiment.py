#!/usr/bin/env python3
"""Constructive selectors for the o_pi=p+2 projection stratum.

Implements exactly the case analysis of frontier-20261028-olson-p2-band-v1.md:
REF from a zero odd-label quadruple; otherwise (triple multiset) the stretched
two-gap cases H(i)-(v), or canonical spares with sector Case A/B and loss 0-2.
Every selector is mapped to a random linear cut and multiplied directly.
"""
import argparse
import itertools
import json
import random

SEED=2026102839


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def runs_of(w):
    N=len(w);refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    st=next(k for k in range(F) if w[refs[k]][0]!=w[refs[k-1]][0])
    runs=[]
    for k in range(F):
        i=refs[(st+k)%F]
        if not runs or w[runs[-1][-1]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    return runs


def pieces(w,seq):
    out=[]
    for i in seq:
        if out and w[out[-1][-1]][0]==w[i][0]:out[-1].append(i)
        else:out.append([i])
    return out


def split(w,r1,r2):
    N=len(w);d=(r2-r1)%N
    X=[(r1+k)%N for k in range(1,d) if w[(r1+k)%N][1]]
    Y=[(r2+k)%N for k in range(1,N-d) if w[(r2+k)%N][1]]
    return pieces(w,X),pieces(w,Y)


def fill(w,p,PX,PY,TX,TY,r1,r2):
    allp=PX+PY;T=set(TX)|{len(PX)+j for j in TY}
    k=[1 if t in T else 0 for t in range(len(allp))]
    total=sum(k);target=2*p-2
    for t in range(len(allp)):
        while total<target and k[t]+2<=len(allp[t]):k[t]+=2;total+=2
    if total!=target:raise ValueError('capacity')
    sel=[i for t,pc in enumerate(allp) for i in pc[:k[t]]]+[r1,r2]
    if product(w,sorted(sel),p)!=(0,0):raise ValueError('product')
    return sorted(sel)


def lab(w,pc):
    return w[pc[0]][0]


def D(w,p,Y,cands,t):
    for a,b in itertools.combinations(cands,2):
        if (lab(w,Y[a])-lab(w,Y[b]))%p==t%p:return [a,b]
    raise ValueError('directed difference missing')


def ccTau(w,p,Y,cands,c,tau):
    cs=[j for j in cands if lab(w,Y[j])==c]
    if tau%p==c and len(cs)>=3:return cs[:3]
    for t in cands:
        if lab(w,Y[t])==tau%p and t not in cs:
            before=[j for j in cs if j<t];after=[j for j in cs if j>t]
            if len(before)>=2:return [before[0],before[1],t]
            if len(after)>=2:return [t,after[0],after[1]]
    raise ValueError('c,c,tau missing')


def zero_quadruple(labels,p):
    for q in itertools.combinations(range(len(labels)),4):
        a,b,c,d=(labels[i] for i in q)
        if (a-b+c-d)%p==0:return q
    return None


def construct(w,p):
    N=len(w);runs=runs_of(w);runof={i:t for t,r in enumerate(runs) for i in r}
    odd=[t for t,r in enumerate(runs) if len(r)%2]
    if len(odd)!=p+2:raise ValueError('o_pi')
    q=zero_quadruple([w[runs[t][0]][0] for t in odd],p)
    if q is not None:
        T={odd[i] for i in q};k=[1 if t in T else 0 for t in range(len(runs))];total=4
        for t in range(len(runs)):
            while total<2*p and k[t]+2<=len(runs[t]):k[t]+=2;total+=2
        sel=sorted(i for t,r in enumerate(runs) for i in r[:k[t]])
        if total!=2*p or product(w,sel,p)!=(0,0):raise ValueError('REF')
        return sel,'REF'
    from collections import Counter
    mult=Counter(w[runs[t][0]][0] for t in odd)
    trip=[v for v,m in mult.items() if m==3]
    if len(trip)!=1 or len(mult)!=p:raise ValueError('multiset lemma violated')
    c=trip[0]
    rots=[i for i,(_,e) in enumerate(w) if not e]
    before={r:(r-1)%N for r in rots}
    gaps={}
    for r in rots:gaps.setdefault(runof[before[r]],[]).append(r)
    multi=[t for t,g in gaps.items() if len(g)>=2]
    if multi:
        G=multi[0];run=runs[G]
        g=sorted(gaps[G],key=lambda r:run.index(before[r]))
        r1,r2=g[0],g[1];e=w[run[0]][0];u,v=w[r1][0],w[r2][0];s=(u+v)%p
        a=run.index(before[r1])+1;x=run.index(before[r2])+1-a;b=len(run)-a-x
        PX,PY=split(w,r1,r2)
        if len(PX)!=1:raise ValueError('X not single piece')
        hasP=b>0;first=0;last=len(PY)-1
        spares=[j for j in range(len(PY)) if len(PY[j])%2 and not (hasP and j==first) and j!=last]
        Godd=len(run)%2
        if not Godd and a%2==0 and x%2==0 and b%2==0:
            TX=[];TY=D(w,p,PY,spares,-s) if s else [j for j in spares if lab(w,PY[j])==c][:2];case='H-i'
        elif not Godd and x%2==1:
            TX=[0];TY=ccTau(w,p,PY,spares,c,u-v+e);case='H-ii'
        elif not Godd:
            mid=D(w,p,PY,spares,s) if s else [j for j in spares if lab(w,PY[j])==c][:2]
            TX=[];TY=[first]+mid+[last];case='H-iii'
        elif x%2==1 and a%2==0 and b%2==0:
            bp=(e+u-v)%p;cand=[j for j in spares if lab(w,PY[j])==bp]
            if cand:TX=[0];TY=[cand[0]];case='H-iva'
            else:
                cs=[j for j in spares if lab(w,PY[j])==c][:2]
                TX=[0];TY=([first]+cs) if hasP else (cs+[last]);case='H-iva-gamma'
        elif x%2==0:
            oddY=[j for j in range(len(PY)) if len(PY[j])%2]
            if s:TY=D(w,p,PY,oddY,-s)
            else:
                from collections import defaultdict
                byl=defaultdict(list)
                for j in oddY:byl[lab(w,PY[j])].append(j)
                TY=next(v[:2] for v in byl.values() if len(v)>=2)
            TX=[];case='H-ivbc'
        else:
            tau=(u-v+e)%p;cpieces=[j for j in range(len(PY)) if len(PY[j])%2 and lab(w,PY[j])==c]
            if tau==e:
                cs=[j for j in spares if lab(w,PY[j])==c][:2];TY=[first]+cs
            else:
                TY=ccTau(w,p,PY,sorted(set(spares)|set(cpieces)),c,tau)
            TX=[0];case='H-v'
        return fill(w,p,PX,PY,TX,TY,r1,r2),case
    spare=set()
    for t in odd:
        run=runs[t]
        if t in gaps:
            kk=run.index(before[gaps[t][0]])+1;piece=run[:kk] if kk%2 else run[kk:]
        else:piece=run
        spare.add(piece[-1])
    sp=sorted(spare);M=len(sp)
    sectors=[]
    for idx,a in enumerate(sp):
        end=sp[(idx+1)%M];dist=(end-a)%N or N
        sectors.append(sorted((r for r in rots if 0<(r-a)%N<dist),key=lambda r:(r-a)%N))
    full=[sec for sec in sectors if len(sec)>=2]
    if full:
        r1,r2=full[0][0],full[0][1];case='A'
    else:
        zc=None
        for idx,z in enumerate(sp):
            if w[z][0]==c and sectors[idx-1] and sectors[idx]:zc=idx;break
        r1,r2=sectors[zc-1][0],sectors[zc][0];case='B'
    u,v=w[r1][0],w[r2][0];s=(u+v)%p
    PX,PY=split(w,r1,r2)
    oX=[j for j in range(len(PX)) if len(PX[j])%2];oY=[j for j in range(len(PY)) if len(PY[j])%2]
    lam=(len(oX)+len(oY)-(p+2))//2
    spY=[j for j in oY if any(i in spare for i in PY[j])]
    if case=='A':
        if lam==0:
            TX=[];TY=D(w,p,PY,spY,-s) if s else [j for j in spY if lab(w,PY[j])==c][:2]
        elif lam==1:
            TX=oX;TY=ccTau(w,p,PY,spY,c,u-v+lab(w,PX[oX[0]]))
        else:
            mid=D(w,p,PY,spY,s) if s else [j for j in spY if lab(w,PY[j])==c][:2]
            TX=oX;TY=[oY[0]]+mid+[oY[-1]]
            if oY[0] in spY or oY[-1] in spY:raise ValueError('A2 ends')
    else:
        if lam==0:
            bp=(c+u-v)%p;TX=oX;TY=[next(j for j in spY if lab(w,PY[j])==bp)]
        elif lam==1:
            ls=[lab(w,PX[j]) for j in oX];altX=(ls[0]-ls[1])%p;t=(-(s+altX))%p
            TX=oX;TY=D(w,p,PY,spY,t) if t else [j for j in spY if lab(w,PY[j])==c][:2]
        else:
            ls=[lab(w,PX[j]) for j in oX];tau=(u-v+ls[0]-ls[1]+ls[2])%p
            e2=lab(w,PY[oY[0]]);t=(e2-tau)%p
            rest=[j for j in spY if j>oY[0]]
            TX=oX;TY=[oY[0]]+(D(w,p,PY,rest,t) if t else [j for j in rest if lab(w,PY[j])==c][:2])
    return fill(w,p,PX,PY,TX,TY,r1,r2),'%s/L%d'%(case,lam)


def gen(rng,p,mode):
    if mode=='free':odd=[rng.randrange(p) for _ in range(p+2)]
    else:
        c=rng.randrange(p);odd=[c,c,c]+[x for x in range(p) if x!=c];rng.shuffle(odd)
        if mode=='ap':
            c0=rng.randrange(p);d=rng.randrange(1,p);odd=[c0,c0,c0]+[(c0+k*d)%p for k in range(1,p)]
    m=len(odd);mand=[i for i in range(m) if odd[i]==odd[(i+1)%m]];units=p-2
    if len(mand)>units:return None
    e=rng.randrange(len(mand),units+1);slots=mand+[rng.randrange(m) for _ in range(e-len(mand))]
    runs=[]
    for i,l in enumerate(odd):
        runs.append([l,1])
        for _ in range(slots.count(i)):runs.append([None,2])
    n=len(runs)
    for i in range(n):
        if runs[i][0] is None:runs[i][0]=rng.choice([x for x in range(p) if x!=runs[i-1][0]])
    if any(runs[i][0]==runs[(i+1)%n][0] for i in range(n)):return None
    for _ in range((3*p-2-sum(r[1] for r in runs))//2):runs[rng.randrange(n)][1]+=2
    vals=[l for l,L in runs for _ in range(L)];F=len(vals)
    if rng.random()<0.35:
        starts=[];pos=0
        for l,L in runs:starts.append((pos,L));pos+=L
        big=[(s0,L) for s0,L in starts if L>=2]
        if not big:return None
        s0,L=rng.choice(big);first=rng.sample(range(s0,s0+L),2)
        rest=[i for i in range(F) if i not in first];gaps=set(first)|set(rng.sample(rest,p-1))
    else:gaps=set(rng.sample(range(F),p+1))
    w=[]
    for i,y in enumerate(vals):
        w.append([y,1])
        if i in gaps:w.append([rng.randrange(1,p),0])
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];skipped=0;branches={}
    for p in (5,7,11,13):
        for mode in ('free','triple','ap'):
            got=0
            while got<150:
                w=gen(rng,p,mode)
                if w is None:skipped+=1;continue
                sel,case=construct(w,p)
                cases.append({'p':p,'word':w,'selector':sel,'case':case,'mode':mode});got+=1
                branches[case]=branches.get(case,0)+1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'skipped_generation_draws':skipped,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_P2_BAND_CONSTRUCTION','actual_words':len(cases),'branches':dict(sorted(branches.items())),
                      'skipped':skipped},sort_keys=True))


if __name__=='__main__':
    main()
