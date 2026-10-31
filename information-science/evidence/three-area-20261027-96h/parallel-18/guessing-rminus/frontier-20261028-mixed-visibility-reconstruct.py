#!/usr/bin/env python3
"""Rationalize mixed-block visibility duals into exact certificates.

Usage: python3 script.py OUT.json SOURCE1 [SOURCE2 ...]
Sources are batch JSON files (key good_full_duals) or JSONL streams (key full).
Each dual is rationalized by limit_denominator at increasing bounds and kept
only if the exact averaged identity holds; the plane cap must carry zero
weight. Writes a certificate list for the independent checker.
"""
from fractions import Fraction
from pathlib import Path
import json,sys
from collections import defaultdict

ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;V=S-1;FULL=(1<<11)-1
def vm(vs):return sum(1<<(v-1) for v in vs)
def move(m,p):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)

def terms(row,F):
    k=row[0]
    if k=='cmi':
        i,j,K=row[1:];a,b=1<<i,1<<j;return [(K|a,1),(K|b,1),(K|a|b,-1),(K,-1)]
    if k=='mono':a=1<<row[1];return [(FULL,1),(FULL^a,-1)]
    if k=='fd':v=row[1];n=vm(N[v]);return [(n|1<<(v-1),1),(n,-1)]
    if k=='mixed-local-fd':
        v=row[1];L=vm({u for t in F if v in TRI[t-1] for u in TRI[t-1] if u!=v});return [(L|S|1<<(v-1),1),(L|S,-1)]
    if k=='syndrome-neighborhood':n=vm(N[row[1]]);return [(n|S,1),(n,-1)]
    if k=='syndrome-global-fd':return [(V|S,1),(V,-1)]
    if k=='conditional-factor-gate':return [(V,3),(S,17)]+[(S|(1<<i),-2) for i in range(10)]
    if k=='plane-syndrome-cap':return [(S,1)]
    raise ValueError(row)

def exact(r):
    F=r['factors'];G=[tuple(p) for p in r['group']];reps=r['orbit_representatives'];mi={x:i for i,x in enumerate(reps)}
    orb=lambda m:mi[min(move(m,p) for p in G)]
    tr=[Fraction(0)]*len(reps);tr[orb(V)]+=1
    for i in range(10):tr[orb(1<<i)]-=Fraction(2,3)
    for n in (100,1000,10000,100000,1000000):
        q=[Fraction(x['float']).limit_denominator(n) for x in r['dual_support']];vec=[Fraction(0)]*len(reps);ok=True
        for z,w in zip(r['dual_support'],q):
            k=z['name'][0]
            if k in ('cmi','mono') and w>=0:ok=False
            if k=='conditional-factor-gate' and w<=0:ok=False
            if k=='plane-syndrome-cap':ok=False
            for m,c in terms(z['name'],F):
                if m:vec[orb(m)]+=w*c
        if ok and vec==tr:return [{'row':z['name'],'multiplier':str(w)} for z,w in zip(r['dual_support'],q)]
    return None

def main():
    out=ROOT/sys.argv[1];duals=[]
    for name in sys.argv[2:]:
        p=ROOT/name
        if name.endswith('.jsonl'):
            for line in p.read_text().splitlines():
                x=json.loads(line)
                if x.get('full'):duals.append(x['full'])
        else:duals.extend(json.loads(p.read_text()).get('good_full_duals',[]))
    certs=[];failed=[]
    for r in duals:
        used=sorted({p[z['name'][1]-1] for z in r['dual_support'] if z['name'][0]=='syndrome-neighborhood' for p in r['group']})
        m=exact(r)
        if m is None:failed.append({'J':r['J'],'W':r['W']});continue
        certs.append({'J':r['J'],'factors':r['factors'],'W_tested':r['W'],'visibility_required':used,'group':r['group'],'multipliers':m})
    with out.open('x',encoding='utf-8') as f:json.dump({'certificates':certs,'failed_rationalization':failed,'target':'H(Y_V)-(2/3)sum_i H(Y_i)'},f);f.write('\n')
    print(json.dumps({'certificates':len(certs),'failed':len(failed)}))


if __name__=='__main__':main()
