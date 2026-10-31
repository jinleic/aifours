#!/usr/bin/env python3
"""Independent checker: mixed-block visibility certificates and plane census.

Usage: python3 script.py OUT.json CERTS.json SHA
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
GEN=[{6},{7},{2,5},{9,10},{1,2,10},{1,5,9},{5,8,9},{2,8,10}]
S=1<<10;V=S-1;FULL=(1<<11)-1
def vm(vs):return sum(1<<(v-1) for v in vs)
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}

def factor_action(p):
    moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
    if set(moved)!=set(LOOK):raise ValueError('FACTOR_ACTION')
    return tuple(LOOK[t] for t in moved)

def fmap(J,f):return sum(1<<f[i] for i in range(10) if J>>i&1)

def rows(row,F,p,need):
    k=row[0]
    def pm(m):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)
    if k=='cmi':
        if len(row)!=4:raise ValueError('CMI')
        i,j,K=row[1:]
        if not 0<=i<j<11 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('CMI')
        a,b,K2=pm(1<<i),pm(1<<j),pm(K);return [(K2|a,1),(K2|b,1),(K2|a|b,-1),(K2,-1)],'nonnegative'
    if k=='mono':a=pm(1<<row[1]);return [(FULL,1),(FULL^a,-1)],'nonnegative'
    if k=='fd':v=p[row[1]-1];n=vm(N[v]);return [(n|1<<(v-1),1),(n,-1)],'zero'
    if k=='mixed-local-fd':
        v=p[row[1]-1];L={u for t in F if v in TRI[t-1] for u in TRI[t-1] if u!=v}
        if not L:raise ValueError('UNCOVERED_VERTEX')
        L=vm(L);return [(L|S|1<<(v-1),1),(L|S,-1)],'zero'
    if k=='syndrome-neighborhood':
        v=p[row[1]-1]
        if v not in need:raise ValueError('VISIBILITY_NOT_ASSUMED')
        n=vm(N[v]);return [(n|S,1),(n,-1)],'zero'
    if k=='syndrome-global-fd':return [(V|S,1),(V,-1)],'zero'
    if k=='conditional-factor-gate':return [(V,3),(S,17)]+[(S|(1<<i),-2) for i in range(10)],'nonpositive'
    raise ValueError(('ROW',row))

def check(c):
    J=c['J'];F=tuple(c['factors'])
    if F!=tuple(t+1 for t in range(10) if J>>t&1) or len(F)<5:raise ValueError('FACTORS')
    if set().union(*(set(TRI[t-1]) for t in F))!=set(N):raise ValueError('COVER')
    need=set(c['visibility_required']);group=[tuple(p) for p in c['group']]
    E={tuple(sorted((u,v))) for u in N for v in N[u]}
    if tuple(range(1,11)) not in group or len(set(group))!=len(group):raise ValueError('GROUP')
    for p in group:
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        f=factor_action(p)
        if fmap(J,f)!=J or {p[v-1] for v in need}!=need:raise ValueError('STABILIZER')
    if not all(tuple(p[q[i]-1] for i in range(10)) in group for p in group for q in group):raise ValueError('CLOSURE')
    acc=[Fraction(0)]*(FULL+1);g=len(group)
    for item in c['multipliers']:
        q=Fraction(item['multiplier'])
        if not q:raise ValueError('ZERO')
        for p in group:
            ts,kind=rows(item['row'],F,p,need)
            if kind=='nonnegative' and q>=0:raise ValueError('SIGN')
            if kind=='nonpositive' and q<=0:raise ValueError('GATE_SIGN')
            for m,w in ts:
                if m:acc[m]+=q*w/g
    tgt=[Fraction(0)]*(FULL+1);tgt[V]=Fraction(1)
    for i in range(10):tgt[1<<i]-=Fraction(2,3)
    if acc!=tgt:raise ValueError('IDENTITY')
    return need

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    certs=json.loads(raw)['certificates'];table={}
    for c in certs:
        need=check(c);table.setdefault(c['J'],[]).append(frozenset(need))
    # control: drop one visibility vertex from the first certificate with any
    c0=next(c for c in certs if c['visibility_required']);bad=json.loads(json.dumps(c0));bad['visibility_required']=bad['visibility_required'][1:]
    try:check(bad)
    except ValueError as e:control=str(e)
    else:raise ValueError('CONTROL')
    acts=[factor_action(p) for p in P];inc=[sum(1<<t for t,T in enumerate(TRI) if v in T) for v in range(1,11)];census=Counter()
    for a,b in combinations(range(1,1024),2):
        c=a^b
        if b>=c:continue
        J=a|b|c;k=bin(J).count('1')
        if set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))!=set(N):census['noncover']+=1;continue
        W={v+1 for v in range(10) if a&inc[v] and b&inc[v] and c&inc[v]}
        if k==4:census['four_factor_theorem']+=1;continue
        if any(g<=W for g in GEN):census['full_model_lattice']+=1;continue
        hit=False
        for p,f in zip(P,acts):
            J2=fmap(J,f);W2={p[v-1] for v in W}
            if any(u<=W2 for u in table.get(J2,[])):hit=True;break
        census['mixed_certificate' if hit else 'unresolved']+=1
    if sum(census.values())!=174251:raise ValueError('COUNT')
    rep={'certificates_sha256':sys.argv[3],'certificates_checked':len(certs),'all_checked':True,'negative_control':control,'plane_census':dict(census),
         'limits':'Exact identities, signs, stabilizer and premise bookkeeping, and exhaustive plane accounting with three cited imports (noncover gate, four-factor theorem, full-model lattice). Written lifting/tensorization requires review.'}
    with out.open('x',encoding='utf-8') as f:json.dump(rep,f,indent=2);f.write('\n')
    print(json.dumps(rep,indent=2))


if __name__=='__main__':main()
