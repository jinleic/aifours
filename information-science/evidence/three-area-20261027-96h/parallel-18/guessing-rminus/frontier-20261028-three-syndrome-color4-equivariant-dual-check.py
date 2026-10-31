#!/usr/bin/env python3
"""Exact independent coefficient and sign check of a three-state certificate."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERTS=(('frontier-20261028-three-syndrome-color4-equivariant-dual-v1.json','7b7af573da508f314674a9eb3bbd21af65717946a2537f22877223d4a8744e62'),)
OUT=ROOT/'frontier-20261028-three-syndrome-color4-equivariant-dual-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
COL=(0,0,1,1,0,0,1,0,0,1);V=1023;S=1024;FULL=2047

def mask(vs):return sum(1<<(v-1) for v in vs)

def terms(row):
    k=row[0]
    if k=='mono':
        if len(row)!=3:raise ValueError('MONOTONICITY_ROW')
        _,br,i=row
        if br not in range(1,5) or not 0<=i<11:raise ValueError('MONOTONICITY_ROW')
        def H(a):return (a&V,br if a&S else 0)
        return [(*H(FULL),1),(*H(FULL^(1<<i)),-1)],'nonnegative'
    if k=='cmi':
        if len(row)!=5:raise ValueError('CMI_ROW')
        _,br,i,j,z=row
        if br not in range(1,5) or not 0<=i<j<11 or not 0<=z<=FULL or z&((1<<i)|(1<<j)):raise ValueError('CMI_ROW')
        def H(a):return (a&V,br if a&S else 0)
        a,b=1<<i,1<<j;return [(*H(z|a),1),(*H(z|b),1),(*H(z|a|b),-1),(*H(z),-1)],'nonnegative'
    if k=='aux-determined':
        if len(row)!=2 or row[1] not in range(1,5):raise ValueError('AUX_ROW')
        return [(V,row[1],1),(V,0,-1)],'equality'
    if k=='conditional-gap-gate':
        if len(row)!=2 or row[1] not in range(1,5):raise ValueError('GATE_ROW')
        return [(V,0,3),(0,row[1],17)]+[(1<<i,row[1],-2) for i in range(10)],'nonpositive'
    if k=='graph-fd':
        v=row[1];a=mask(N[v]);return [(a|1<<(v-1),0,1),(a,0,-1)],'equality'
    if k in ('indicator-neighborhood','state-neighborhood'):
        v=row[1];a=mask(N[v]);colors={COL[t] for t,T in enumerate(TRI) if v in T}
        if k=='state-neighborhood':
            if len(colors)<2:raise ValueError('NEIGH_STATE_PREMISE')
            branch=1
        else:
            c=row[2]
            if c not in colors:raise ValueError('NEIGH_INDICATOR_PREMISE')
            branch=2+c
        return [(a,branch,1),(a,0,-1)],'equality'
    if k=='indicator-triangle':
        t=row[1]
        if not 1<=t<=10:raise ValueError('TRIANGLE_ROW')
        a=mask(TRI[t-1]);return [(a,2+COL[t-1],1),(a,0,-1)],'equality'
    if k=='full-state-local-fd':
        v=row[1];local={u for T in TRI if v in T for u in T if u!=v};a=mask(local)
        return [(a|1<<(v-1),1,1),(a,1,-1)],'equality'
    if k in ('onehot-exclusion-lower','onehot-exclusion-upper'):
        a=row[1]
        if not 0<=a<=V:raise ValueError('ONEHOT_CONDITION')
        if k=='onehot-exclusion-lower':return [(a,1,5),(a,2,-3),(a,3,-3),(a,4,-3),(a,0,4)],'nonpositive'
        return [(a,2,1),(a,3,1),(a,4,1),(a,1,-2),(a,0,-1)],'nonpositive'
    if k=='indicator-data-processing':
        a,j=row[1:]
        if not 0<=a<=V or j not in (2,3,4):raise ValueError('DATA_ROW')
        return [(a,j,1),(a,1,-1)],'nonpositive'
    if k=='indicator-refined-cmi':
        a,i,j=row[1:];b=1<<i
        if not 0<=a<=V or not 0<=i<10 or a&b or j not in (2,3,4):raise ValueError('REFINED_CMI_ROW')
        return [(a|b,j,1),(a,1,1),(a|b,1,-1),(a,j,-1)],'nonnegative'
    if k=='onehot-pair-subadditivity':
        a,j,l=row[1:]
        if not 0<=a<=V or j not in (2,3,4) or l not in (2,3,4) or j>=l:raise ValueError('PAIR_ROW')
        return [(a,1,1),(a,j,-1),(a,l,-1),(a,0,1)],'nonpositive'
    raise ValueError(('UNKNOWN_ROW',row))


def check(doc,change_target=False):
    if tuple(doc['factor_colors'])!=COL:raise ValueError('COLOR_PIN')
    group=[tuple(p) for p in doc['group']];edges={tuple(sorted((v,u))) for v in N for u in N[v]};tri={tuple(sorted(T)):i for i,T in enumerate(TRI)}
    if len(group)!=4 or len(set(group))!=4:raise ValueError('GROUP')
    actions=[tuple(q) for q in doc['color_actions']]
    if len(actions)!=len(group):raise ValueError('COLOR_ACTION_COUNT')
    for p,cp in zip(group,actions):
        if set(p)!=set(N):raise ValueError('PERM')
        if set(cp)!=set(range(3)):raise ValueError('COLOR_PERM')
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in edges}!=edges:raise ValueError('GRAPH_AUTOMORPHISM')
        moved=[tuple(sorted(p[v-1] for v in T)) for T in TRI]
        if set(moved)!=set(tri):raise ValueError('FACTOR_AUTOMORPHISM')
        if any(cp[COL[i]]!=COL[tri[t]] for i,t in enumerate(moved)):raise ValueError('COLOR_AUTOMORPHISM')
    for p,cp in zip(group,actions):
        for q,cq in zip(group,actions):
            pq=tuple(p[q[i]-1] for i in range(10));cpcq=tuple(cp[cq[i]] for i in range(3))
            if not any(g==pq and ca==cpcq for g,ca in zip(group,actions)):raise ValueError('COLOR_ACTION_CLOSURE')
    if not all(tuple(p[q[i]-1] for i in range(10)) in group for p in group for q in group):raise ValueError('GROUP_CLOSURE')
    def move(a,p):return sum(1<<(p[i]-1) for i in range(10) if a>>i&1)
    acc={(a,b):Fraction(0) for a in range(V+1) for b in range(5) if a or b};counts=Counter();seen=set()
    for x in doc['multipliers']:
        row=x['row'];key=tuple(row)
        if key in seen:raise ValueError('DUPLICATE_ROW')
        seen.add(key);q=Fraction(x['multiplier']);rowterms,kind=terms(row);counts[row[0]]+=1
        if not q:raise ValueError('ZERO_WEIGHT')
        if kind=='nonnegative' and q>=0:raise ValueError('NONNEGATIVE_SIGN')
        if kind=='nonpositive' and q<=0:raise ValueError('NONPOSITIVE_SIGN')
        for p,cp in zip(group,actions):
            for a,b,c in rowterms:
                branch=2+cp[b-2] if b>=2 else b
                if a or b:acc[(move(a,p),branch)]+=q*c/len(group)
    target={k:Fraction(0) for k in acc};target[(V,0)]=1
    for i in range(10):target[(1<<i,0)]-=Fraction(2,3)
    if change_target:target[(V,0)]+=Fraction(1,7)
    if acc!=target:raise ValueError('COEFFICIENT_IDENTITY')
    return {'row_counts':dict(counts),'group_order':len(group),'entropy_coordinates_checked':len(acc),'nonzero_rows':len(seen),'target':'H(X_V)-(2/3)sum_i H(X_i)'}


def main():
    global COL
    results=[];controls={}
    for index,(filename,digest) in enumerate(CERTS):
        raw=(ROOT/filename).read_bytes()
        if sha256(raw).hexdigest()!=digest:raise ValueError('HASH')
        doc=json.loads(raw);COL=tuple(doc['factor_colors']);result=check(doc)
        results.append({'certificate_sha256':digest,'factor_colors':COL,**result})
        if index==0:
            try:check(doc,True)
            except ValueError as e:controls['changed_target']=str(e)
            else:raise ValueError('TARGET_CONTROL')
            bad=json.loads(raw);x=next(x for x in bad['multipliers'] if x['row'][0]=='cmi');x['multiplier']=str(-Fraction(x['multiplier']))
            try:check(bad)
            except ValueError as e:controls['flipped_cmi_sign']=str(e)
            else:raise ValueError('SIGN_CONTROL')
    out={'all_checked':True,'cases':results,'negative_controls':controls,
         'limits':'Exact arithmetic and combinatorial premises only. This pattern imports the repaired two-syndrome theorem through indicator gates; all one-hot inequalities, local decoding and tensor gates require independent scientific review.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
