#!/usr/bin/env python3
"""Independent exact check of seven residual four-factor plane certificates.

Each row is rebuilt from graph/plane data; visibility rows are accepted only
when the incident selected-factor parity projection is injective on the plane.
Orbit images under the factor-preserving automorphisms must cover all 28
residual planes.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-fourfactor-seven-residual-dual-v1.json','f70245bd16654d19177a771ea897f55377803257d929b9c63d1c05b95e5816c5')
REMAIN=('frontier-20261028-fourfactor-remaining-orbit-check-result.json','69acd9041ea9d698b84bf0a75583df6b73ff006cbfb87764cae16f411e416b6e')
OUT=ROOT/'frontier-20261028-fourfactor-seven-residual-dual-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
S=1<<10;V=S-1;FULL=(1<<11)-1

def vmask(vs):return sum(1<<(v-1) for v in vs)

def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return raw

def rows_for(row,factors,plane):
    kind=row[0]
    if kind=='cmi':
        if len(row)!=4:raise ValueError('CMI_ROW')
        i,j,k=row[1:]
        if not 0<=i<j<11 or not 0<=k<=FULL or k&((1<<i)|(1<<j)):raise ValueError('CMI_ROW')
        a,b=1<<i,1<<j;return [(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],'nonnegative'
    if kind=='fd':
        v=row[1]
        if len(row)!=2 or v not in N:raise ValueError('FD_ROW')
        n=vmask(N[v]);return [(n|1<<(v-1),1),(n,-1)],'zero'
    if kind=='syndrome-neighborhood':
        v=row[1]
        if len(row)!=2 or v not in N:raise ValueError('VIS_ROW')
        incident=sum(1<<(t-1) for t in factors if v in TRI[t-1])
        if not all(m&incident for m in plane):raise ValueError('VISIBILITY_PREMISE')
        for t in factors:
            if v in TRI[t-1] and any(u!=v and u not in N[v] for u in TRI[t-1]):raise ValueError('TRIANGLE_EDGE')
        n=vmask(N[v]);return [(n|S,1),(n,-1)],'zero'
    if kind=='syndrome-global-fd':
        if len(row)!=1:raise ValueError('GLOBAL_ROW')
        return [(V|S,1),(V,-1)],'zero'
    if kind=='conditional-zero-rank-fd':
        if len(row)!=3:raise ValueError('LOCAL_ROW')
        A,v=row[1:]
        if not 0<=A<=V or v not in N or A>>(v-1)&1:raise ValueError('LOCAL_ROW')
        local={u for t in factors if v in TRI[t-1] for u in TRI[t-1] if u!=v}
        if not local or vmask(local)&A!=vmask(local):raise ValueError('LOCAL_PREMISE')
        return [(A|S|1<<(v-1),1),(A|S,-1)],'zero'
    raise ValueError(('UNKNOWN_ROW',row))

def check(case,change_target=False,plane_override=None):
    factors=tuple(case['factors']);plane=tuple(plane_override or case['syndrome_plane'])
    a,b,c=plane
    if a^b!=c or len({a,b,c})!=3 or not all(plane):raise ValueError('PLANE')
    union=a|b|c
    if factors!=tuple(i+1 for i in range(10) if union>>i&1) or len(factors)!=4:raise ValueError('FACTORS')
    if set().union(*(set(TRI[t-1]) for t in factors))!=set(N):raise ValueError('COVER')
    acc=[Fraction(0)]*(FULL+1);counts=Counter()
    for item in case['multipliers']:
        q=Fraction(item['multiplier']);terms,kind=rows_for(item['row'],factors,plane);counts[item['row'][0]]+=1
        if not q:raise ValueError('ZERO')
        if kind=='nonnegative' and q>=0:raise ValueError('SIGN')
        for m,w in terms:
            if m:acc[m]+=q*w
    target=[Fraction(0)]*(FULL+1);target[V]=Fraction(1)
    for i in range(10):target[1<<i]-=Fraction(2,3)
    if change_target:target[V]+=Fraction(1,7)
    if acc!=target:raise ValueError('COEFFICIENT_IDENTITY')
    return {'factors':factors,'plane':plane,'rows':dict(counts),'coefficients_checked':FULL}

def main():
    doc=json.loads(pin(CERT));remain=json.loads(pin(REMAIN))
    if not remain['all_checked'] or remain['remaining_planes']!=28:raise ValueError('REMAIN')
    residual={frozenset(p) for o in remain['orbits'] for p in o['members']}
    if len(residual)!=28 or len(doc['cases'])!=7:raise ValueError('COUNTS')
    edges={tuple(sorted((v,u))) for v in N for u in N[v]};lookup={tuple(sorted(t)):i for i,t in enumerate(TRI)};actions=[]
    for p in P:
        if {tuple(sorted((p[x-1],p[y-1]))) for x,y in edges}!=edges:raise ValueError('GRAPH_AUTOMORPHISM')
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(lookup):raise ValueError('FACTOR_AUTOMORPHISM')
        actions.append(tuple(lookup[t] for t in moved))
    results=[];covered=set()
    for case in doc['cases']:
        results.append(check(case));plane=frozenset(case['syndrome_plane'])
        if plane not in residual:raise ValueError('NOT_RESIDUAL')
        covered|={frozenset(sum(1<<f[i] for i in range(10) if m>>i&1) for m in plane) for f in actions}
    if covered!=residual:raise ValueError('ORBIT_COVERAGE')
    controls={}
    try:check(doc['cases'][0],change_target=True)
    except ValueError as e:controls['changed_target']=str(e)
    else:raise ValueError('TARGET_CONTROL')
    bad=json.loads(json.dumps(doc['cases'][0]));x=next(r for r in bad['multipliers'] if r['row'][0]=='cmi');x['multiplier']=str(-Fraction(x['multiplier']))
    try:check(bad)
    except ValueError as e:controls['flipped_cmi_sign']=str(e)
    else:raise ValueError('SIGN_CONTROL')
    # A plane on the same factors with an invisible direction at the used vertex must be rejected.
    vis=next(r for r in doc['cases'][1]['multipliers'] if r['row'][0]=='syndrome-neighborhood')['row'][1]
    F=doc['cases'][1]['factors'];inc=sum(1<<(t-1) for t in F if vis in TRI[t-1]);rest=sum(1<<(t-1) for t in F)&~inc
    if not rest:raise ValueError('CONTROL_SETUP')
    fake=(rest,inc,rest^inc)
    try:check(doc['cases'][1],plane_override=fake)
    except ValueError as e:controls['invisible_plane']=str(e)
    else:raise ValueError('VISIBILITY_CONTROL')
    if controls['invisible_plane']!='VISIBILITY_PREMISE':raise ValueError(('WRONG_CONTROL_REASON',controls['invisible_plane']))
    out={'certificate_sha256':CERT[1],'remaining_receipt_sha256':REMAIN[1],'all_checked':True,'cases':results,
         'residual_planes_covered_by_orbits':len(covered),'negative_controls':controls,
         'limits':'Exact coefficient, sign, row-premise and orbit-coverage checks only. Written lifting/tensorization and graph semantics require independent scientific review.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
