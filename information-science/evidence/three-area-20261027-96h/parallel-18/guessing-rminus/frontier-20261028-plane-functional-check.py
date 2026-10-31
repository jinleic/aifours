#!/usr/bin/env python3
"""Independent checker for plane-functional certificates (exact Fractions).

Usage: python3 script.py OUT.json CERTS.json SHA
Each certificate: colors (list over {None,0,1,2} per factor), actions (list of
[vertex permutation, functional permutation]) and multipliers of named rows,
normalized so the identity target is 3*Delta. Rows are rebuilt from graph and
coloring data; every (vertex, functional) action is re-verified to preserve
the coloring up to the given functional permutation; signs and the averaged
identity on all 5,119 branch coordinates are checked exactly.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
V=(1<<10)-1;S=1<<10;FULL=(1<<11)-1
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}
def vm(vs):return sum(1<<(v-1) for v in vs)

def rows(name,col):
    k=name[0]
    def H(m,b):return (m&V,b if m&S else 0)
    if k=='mono':
        _,br,i=name
        if br not in range(1,5) or not 0<=i<11:raise ValueError('MONO')
        return [(*H(FULL,br),1),(*H(FULL^(1<<i),br),-1)],'ge'
    if k=='cmi':
        _,br,i,j,K=name
        if br not in range(1,5) or not 0<=i<j<11 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('CMI')
        a,b=1<<i,1<<j;return [(*H(K|a,br),1),(*H(K|b,br),1),(*H(K|a|b,br),-1),(*H(K,br),-1)],'ge'
    if k=='aux-determined':
        br=name[1];return [(V,br,1),(V,0,-1)],'eq'
    if k=='gate':
        if name[1]!=1:raise ValueError('ONLY_STATE_GATE_ALLOWED')
        return [(V,0,3),(0,1,17)]+[(1<<i,1,-2) for i in range(10)],'le'
    if k=='graph-fd':
        v=name[1];n=vm(N[v]);return [(n|1<<(v-1),0,1),(n,0,-1)],'eq'
    if k=='functional-neighborhood':
        _,v,c=name
        if c not in {col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None}:raise ValueError('FUNCTIONAL_VISIBILITY')
        for t,T in enumerate(TRI):
            if v in T and col[t]==c and any(u!=v and u not in N[v] for u in T):raise ValueError('TRIANGLE_EDGE')
        n=vm(N[v]);return [(n,2+c,1),(n,0,-1)],'eq'
    if k=='state-neighborhood':
        v=name[1]
        if len({col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None})<2:raise ValueError('STATE_VISIBILITY')
        n=vm(N[v]);return [(n,1,1),(n,0,-1)],'eq'
    if k=='mixed-local-fd':
        v=name[1];L={u for t,T in enumerate(TRI) if col[t] is not None and v in T for u in T if u!=v}
        if not L:raise ValueError('UNCOVERED')
        L=vm(L);return [(L|1<<(v-1),1,1),(L,1,-1)],'eq'
    if k=='functional-triangle':
        t=name[1]
        if col[t-1] is None:raise ValueError('FIXED_TRIANGLE')
        m=vm(TRI[t-1]);return [(m,2+col[t-1],1),(m,0,-1)],'eq'
    if k=='data-processing':
        _,a,j=name
        if not 0<=a<=V or j not in (2,3,4):raise ValueError('DP')
        return [(a,j,1),(a,1,-1)],'le'
    if k=='pair-determines-state':
        _,a,j,l=name
        if not 0<=a<=V or not (j in (2,3,4) and l in (2,3,4) and j<l):raise ValueError('PAIR')
        return [(a,1,1),(a,j,-1),(a,l,-1),(a,0,1)],'le'
    raise ValueError(('ROW',name))

def check(c,change=False):
    col=[None if x is None else int(x) for x in c['colors']]
    if len(col)!=10 or all(x is None for x in col):raise ValueError('COLORS')
    J={t for t in range(10) if col[t] is not None}
    if set().union(*(set(TRI[t]) for t in J))!=set(N):raise ValueError('COVER')
    E={tuple(sorted((u,v))) for u in N for v in N[u]};acts=[]
    for p,cp in c['actions']:
        p=tuple(p);cp=tuple(cp)
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E or sorted(cp)!=[0,1,2]:raise ValueError('ACTION')
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(LOOK):raise ValueError('FACTORS')
        f=[LOOK[m] for m in moved];new=[None]*10
        for t in range(10):new[f[t]]=None if col[t] is None else cp[col[t]]
        if new!=col:raise ValueError('COLOR_ACTION')
        acts.append((p,cp))
    if (tuple(range(1,11)),(0,1,2)) not in acts:raise ValueError('IDENTITY_ACTION')
    acc={};g=len(acts)
    for item in c['multipliers']:
        q=Fraction(item['multiplier']);ts,kind=rows(item['row'],col)
        if not q:raise ValueError('ZERO')
        if kind=='ge' and q>=0:raise ValueError('SIGN_GE')
        if kind=='le' and q<=0:raise ValueError('SIGN_LE')
        for p,cp in acts:
            for a,b,w in ts:
                a2=sum(1<<(p[i]-1) for i in range(10) if a>>i&1);b2=2+cp[b-2] if b>=2 else b
                if a2 or b2:acc[(a2,b2)]=acc.get((a2,b2),0)+q*w/g
    tgt={(V,0):Fraction(3)}
    for i in range(10):tgt[(1<<i,0)]=Fraction(-2)
    if change:tgt[(V,0)]+=1
    keys=set(acc)|set(tgt)
    if any(acc.get(k,0)!=tgt.get(k,0) for k in keys):raise ValueError('IDENTITY')
    return Counter(x['row'][0] for x in c['multipliers'])

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    certs=json.loads(raw)['certificates'];summary=[]
    for c in certs:
        cnt=check(c);summary.append({'colors':c['colors'],'rows':sum(cnt.values()),'kinds':dict(cnt)})
    try:check(certs[0],change=True)
    except ValueError as e:control=str(e)
    else:raise ValueError('CONTROL')
    rep={'certificates_sha256':sys.argv[3],'all_checked':True,'count':len(certs),'cases':summary,'negative_control':control,
         'limits':'Exact identities, signs, coloring-action and premise checks. No two-syndrome import (only the full-state gate). Written mixed-block lifting requires review.'}
    with out.open('x',encoding='utf-8') as f:json.dump(rep,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in rep.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
